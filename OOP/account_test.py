import bankaccount


def main():
	start_balance = int(input("Enter the initial balance: "))
	
	# Create a bank account object
	# Saving is the object
	saving = bankaccount.BankAccount(start_balance)
	
	# Deposit the user's pay
	
	pay = int(input("How much were you paid in this week "))
	
	saving.deposit(pay)
	
	# Display the balance
	
	print(saving.get_balance())
	
	# Withdraw amount
	
	amount = int(input("How much would you like to withdraw?"))
	saving.withdraw(amount)
	
	# Remaining balance
	
	print("Your remaining balance is: ", saving.get_balance())


if __name__ == "__main__":
	main()
	