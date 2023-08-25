#!/usr/bin/env python3

class Item:
    def __init__(self, name, price, quantity):
      self.name = name
      self.price = price
      self.quantity = quantity

class CashRegister:
   def __init__(self):
      self.items = []
      self.discount_percentage = 0.0

   def add_item(self, name, price, quantity):
      self.items.append(Item(name, price, quantity))

   def calculate_total(self):
      total = sum(item.price * item.quantity for item in self.items)
      total -= total * (self.discount_percentage / 100)
      return total
   
   def apply_discount(self, percentage):
      self.discount_percentage = percentage

   def void_last_transaction(self):
      if self.items:
         self.items.pop()
    
   def display_items(self):
      for item in self.items:
         print(f"{item.name} - {item.quantity} x ${item.price:.2f}")


register = CashRegister()

register.add_item("Apple", 0.75, 3)
register.add_item("Banana", 0.5, 5)

print("Items in the cart:")
register.display_items()

register.apply_discount(10)

total = register.calculate_total()
print(f"Total after discount: ${total:2f}")
  
register.void_last_transaction()
print("After voiding last transaction:")
register.display_items()

register.add_item("Orange", 1.0, 2)
register.add_item("Grapes", 2.5, 1)


print("Updated items in the cart:")
register.display_items()


total = register.calculate_total()
print(f"Total after adding more items: ${total:.2f}")