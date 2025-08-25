#Functions

#Calculate the final balance
def calculate_balance(initial_balance, transactions):
    res = initial_balance
    for amount in transactions:
        res += amount
    return res

def main():
    #Read the input
    initial_balance = int(input())
    transactions = list(map(int, input().split(',')))
    res = calculate_balance(initial_balance, transactions)

    #Print the result
    print(res)
if __name__ == "__main__":
    main()
