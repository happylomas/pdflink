


bank_account_name = []
account_balance = []
account_name = None

print('')
print('Enter the names and balances of bank accounts (type: quit when done)')
while account_name != 'quit':
    account_name = input('what is the name of this account? ')
    if account_name != 'quit': 
        balance = float(input('What is the balance? '))

        bank_account_name.append(account_name)
        account_balance.append(balance)

# account name with their balance then total balance.
total = 0
print('Account Information:')

for i in range(len(bank_account_name)):
    print(f'{bank_account_name}[i]-&{account_balance[i]}')
    total += balance[i]