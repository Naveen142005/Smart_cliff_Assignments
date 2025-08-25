from account import Account
from transactions import deposit, withdraw
from loan import calculate_emi

def main():
    account_1 = Account("John", 10000)
    account_2 = Account("Alice", 5000)

    deposit(account_1, 5000)
    deposit(account_2, 3000)

    withdraw(account_1, 2000)
    withdraw(account_2, 1000)

    account_1_emi = calculate_emi(account_1, 5000,10,2)
    account_2_emi = calculate_emi(account_2, 10000, 12, 1)

    print("Account_1 details:")
    print("Final Balance:", account_1.balance)
    print("EMI", account_1_emi)
    print( )
    print("Account_2 details:")
    print("Final Balance:", account_2.balance)
    print("EMI", account_2_emi)



if __name__ == '__main__':
    main()