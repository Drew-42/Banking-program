# Important functions of the program are defined here:

def show_balance(balance):
	print(f'Your balance is: ${balance:.2f}')

def deposit(balance):
	while True:
		try:
			deposit_quantity = float(input('Enter the amount you want to deposit (in $): '))
		except ValueError:
			print ('Value is invalid (must be numeric)')
		else:
			if deposit_quantity <= 0:
				print('Value is invalid (must be greater than 0)')
			else:
				return deposit_quantity

def withdraw(balance):
	while True:
		withdraw_quantity = input('Enter the amount you want to withdraw (in $): ')
		
		try:
			withdraw_quantity = float(withdraw_quantity)
		except ValueError:
			print('Value is invalid (must be numeric)')
		else:
			if withdraw_quantity <= 0:
				print('Value is invalid (must be greater than 0)')
			else:
				return withdraw_quantity

# The main body of code exists inside the main() function:

def main():

	balance = 0
	is_running = True

# The main menu is set up here:

	while is_running:
		print('-------------------------------')
		print('    <<< BANKING PROGRAM >>>')
		print('-------------------------------')
		print()
		print('1. Show Balance')
		print('2. Deposit')
		print('3. Withdraw')
		print('4. Exit')
		print('-------------------------------')

# The user can choose an item from the menu, and each possible choice is tied with a specific 
# action:

		while True:
			choice = input('Enter your choice (1-4): ')
			
			if choice == '1':
				show_balance(balance)
				break

			elif choice == '2':
				deposit_quantity = deposit(balance)
				balance += deposit_quantity	
				print(f'${deposit_quantity:.2f} successfully added to your bank account!')
				break

			elif choice == '3':
				withdraw_quantity = withdraw(balance)
				balance -= withdraw_quantity

				if balance < 0:
					balance += withdraw_quantity
					print ('You don\'t have enough money in your account! Action couldn\'t be performed')
				else:
					print(f'${withdraw_quantity:.2f} successfully withdrawn from your bank account!')
				break

			elif choice == '4':
				is_running = False
				break
			else:
				print('Invalid option, try again')

		print()

		while is_running:
			back_menu = input('To go back to menu press \'enter\': ')

			if back_menu == '':
				print()
				break
			else:
				print('Invalid option, try again')

	print('Thanks for using our banking services. See you around!')

# The main() function will execute only if the file is run as a script, not imported as 
# a module. I learned this is a good practice when writing Python code:

if __name__ == '__main__':
	main()