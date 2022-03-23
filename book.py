from functools import total_ordering

@total_ordering
class Order:
	def __init__(self, quantity, price):
	      self.quantity = quantity
	      self.price = price
	def __eq__(self, other): # self == other
		return other and self.quantity == other.quantity and self.price == other.price
	def __lt__(self, other): # self < other 
		return other and self.price < other.price
