def deposit(account, amount):
    account.balance += amount

def withdraw(account, amount):
    if account.balance < amount:
        print('Insufficient balance')
        return amount
    account.balance -= amount

