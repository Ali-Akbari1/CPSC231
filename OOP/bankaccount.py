
class BankAccount:
	
	def __init__(self, bal):  # This is my constructor
		self._balance = bal  # _balance is attribute/field
		
	def deposit(self, amount):  # This is the method
		self._balance = self._balance + amount
		
	def withdraw(self, amount):  # This is the method
	
		if self._balance >= amount:
			self._balance = self._balance - amount
		else:
			print("Error! You have insufficient funds. ")
			
	def get_balance(self):  # This is the method
		return self._balance

