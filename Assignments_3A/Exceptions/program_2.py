class PayOutOfBoundsException(Exception): pass

class AccountManagement:
    def __init__(self):
        self.balance = 80000
        self.limit = 30000

    def withdraw(self, amount):
        if amount > self.limit or amount > self.balance:
            raise PayOutOfBoundsException("Transaction amount exceed the limit or insufficient balance")
        self.balance -= amount
        print("Withdrawal successful.")
        print("Updated balance:", self.balance)

def main():
    acc = AccountManagement()
    try:
        amt = int(input("Enter withdrawal amount:"))
        acc.withdraw(amt)
    except PayOutOfBoundsException as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
