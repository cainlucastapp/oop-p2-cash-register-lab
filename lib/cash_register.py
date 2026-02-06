#!/usr/bin/env python3

#from ast import If

class CashRegister:
    # Constructor
    def __init__(self, discount=0):
        # Total
        self.total = 0
        # Discount #Note that discount is a percentage off of the total cash register price (e.g. a discount of 20 means the customer receives 20% off of their total price)
        self.discount = discount
        # Items array
        self.items = []
        # Previous transactions array
        self.previous_transactions = []

    # Property getter for discount
    @property
    def discount(self):
        return self._discount

    # Property setter for discount
    @discount.setter
    def discount(self, value):
        if not isinstance(value, int):
            print("Not valid discount")
        elif not 0 <= value <= 100:
            print("Not valid discount")
        else:
            self._discount = value
            
            
    def add_item(self, item, price, quantity=1):
        # Add price to total
        self.total += price * quantity
        # Add item to the items array
        for _ in range(quantity):
            self.items.append(item)
        # Add an object to the previous transactions with the item, price and quantity.
        self.previous_transactions.append(
            {"item": item, "price": price, "quantity": quantity}
        )
    
    def apply_discount(self):
        # If there's no discount, print message
        if self.discount == 0:
            print("There is no discount to apply.")
            return
        # Apply discount as percentage off from total
        discount_amount = (self.discount / 100) * self.total
        self.total -= discount_amount
        # Optionally print the new total
        print(f"After the discount, the total comes to ${int(self.total)}.")
    
    def void_last_transaction(self):
        # Check if there are any transactions to void
        if not self.previous_transactions:
            print("There are no transactions to void.")
            return
        
        # Remove the last transaction from array
        last_transaction = self.previous_transactions.pop()
        item = last_transaction["item"]
        price = last_transaction["price"]
        quantity = last_transaction["quantity"]
        
        # Subtract the transaction amount from total
        self.total -= price * quantity
        
        # Remove the items from the items array
        for _ in range(quantity):
            self.items.remove(item)