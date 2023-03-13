import csv
import datetime

# Creating Menu.txt file
with open("Menu.txt", "w") as menu_file:
  menu_file.write("* Pizza Types:\n1: Classic Pizza\n2: Margarita Pizza\n3: Turkish Pizza\n4: Plain Pizza\n\n* Extra Ingredients:\n1: Olives\n2: Mushrooms\n3: Goat Cheese\n4: Meat\n5: Onions\n6: Corn\n\n*Enjoy your meal!")

# Creating Orders_Database.csv file
header_row =["Name", "Identity Number", "Order", "Total Price", "Card Number", "Card Password", "Date"]
with open("Orders_Database.csv", "w", newline="") as database:
  writer = csv.writer(database)
  writer.writerow(header_row)

# Defining Pizza class
class Pizza(object):
  
  #constructor method
  def __init__(self, description, cost):
    self._description = description
    self._cost = cost
    
  # get_cost method to get the cost
  def get_cost(self):
    return self._cost
  
  #get_description method to get the description
  def get_description(self):
    return self._description
  
#Defining subclasses of Pizza
class ClassicPizza(Pizza):
  def __init__(self):
    super().__init__("Classic Pizza: Pizza Sauce, Mozzarella, Pepperoni, Mushrooms, Peppers ", 40)
  
class MargaritaPizza(Pizza):
  def __init(self):
    super().__init__("Margarita Pizza: Pizza Sauce, Mozzarella", 20)

class TurkishPizza(Pizza):
  def __init__(self):
    super().__init__("Turkish Pizza: Pizza Sauce, Mozzarella, Pepperoni, Peppers", 40)

class PlainPizza(Pizza):
  def __init__(self):
    super().__init__("Plain Pizza: Pizza Sauce, Mozzarella, Pepperoni ", 30)

#Defining a class for ingredients
class Decorator(Pizza):
  def __init__(self, component):
    self.component = component

  #add ingredient cost and pizza cost 
  def get_cost(self):
    return self.component.get_cost() + Pizza.get_cost(self)

  #concatenate ingredient and pizza descriptions
  def get_description(self):
    return self.component.get_description() + " " + Pizza.get_description(self)

#Defining subclasses of Decorator
class Olive(Decorator):

  def __init__(self, component):
    self.component = component
    self._description = "Extra Olives"
    self._cost = 3

class Mushroom(Decorator):

  def __init__(self, component):
    super().__init__(component)
    self._description = "Extra Mushrooms"
    self._cost = 3

class GoatCheese(Decorator):

  def __init__(self, component):
    super().__init__(component)
    self._description = "Extra Goat Cheese"
    self._cost = 5

class Meat(Decorator):
  def __init__(self, component):
    super().__init__(component)
    self._description = "Extra Meat"
    self._cost = 7

class Onions(Decorator):
  def __init__(self, component):
    super().__init__(component)
    self._description = "Extra Onion"
    self._cost = 3

class Corn(Decorator):
  def __init__(self, component):
    super().__init__(component)
    self._description = "Extra Corn"
    self._cost = 3 

#Function for display the menu
def menu():
  with open("Menu.txt", "r") as menu:
    print(menu.read())

#Function to get required informations if the order confirmed 
def confirmed_order(order, price):
  name = input("Please enter your full name: ")
  identity_number = input("Please enter your identity number: ")
  card_number = input("Please enter your card number: ")
  card_password = input("Please enter your card password: ")

  now = datetime.datetime.now()

  #saving the order details to the database
  data = [[name, identity_number, order, price, card_number, card_password, now]]
  with open("Orders_Database.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

#Function for ordering
def order_system():

  menu()

  pizza = None
  
  #Asking to user for a pizza choice until a valid option selected
  #match case will only work with Python 3.10 and later versions
  while pizza == None:
   pizza_choice = input("Enter your pizza choice: ")
   match pizza_choice:
     case "1":
       pizza = ClassicPizza()
       print("Your choice: Classic Pizza")
     case "2":
       pizza = MargaritaPizza()
       print("Your choice: Margarita Pizza")
     case "3":
       pizza = TurkishPizza()
       print("Your choice: Turkish Pizza")
     case "4":
       pizza = PlainPizza()
       print("Your choice: Plain Pizza")
     case _:
       print("İnvalid choice!")

  extra_ingredients = []
  added_ingredients = [] #to check added ingredients before
  ingredient_choice = None

  #Asking to user for ingredient choices until the user does not want to add ingredient
  print("Please choose an ingredient, if you want to exit enter 0")
  while ingredient_choice != "0":
    ingredient_choice = input("Enter your ingredient choice: ")
    #if the chosen ingredient added before
    if ingredient_choice in added_ingredients:
      print("You already add this ingredient!")
    else:
      added_ingredients.append(ingredient_choice)

      match ingredient_choice:
        case "1":
          print("Added: Olives")
          extra_ingredients.append(Olive(pizza))
        case "2":
          print("Added: Mushrooms")
          extra_ingredients.append(Mushroom(pizza))
        case "3":
          print("Added: Goat Cheese")
          extra_ingredients.append(GoatCheese(pizza))
        case "4":
          print("Added: Meat")
          extra_ingredients.append(Meat(pizza))
        case "5":
          print("Added: Onions")
          extra_ingredients.append(Onions(pizza))
        case "6":
          print("Added: Corn")
          extra_ingredients.append(Corn(pizza))
        case "0":
          added_ingredients.remove(ingredient_choice)
          break
        case _:
          print("Invalid choice")
          added_ingredients.remove(ingredient_choice)

  #calculating total price
  total_price = sum(item.get_cost() for item in extra_ingredients) - (len(extra_ingredients)-1) * pizza.get_cost()
  
  #concatenating descriptions
  description = ",".join(item.get_description() for item in extra_ingredients)
  description = pizza.get_description() + description.replace(pizza.get_description(), "")
  
  #Asking user to confirm their order
  print(f"**********\nPlease confirm your order:\n{description}\nTotal Price: {total_price}\n**********")
  confirm = None
  while confirm != "Yes" and confirm != "No":
    confirm = input("To confirm your order enter Yes otherwise enter No: ")
    if confirm == "Yes":
        confirmed_order(description, total_price)
        print("Your order has been received. Thank you for choosing us.")
    elif confirm == "No":
        print("You cancelled your order.")
    else:
      print("Invalid input!")

#main function
def main():
  order_system()

if __name__ == "__main__":
  main()