class NegativeValueError(Exception): pass
class ZeroOrderError(Exception): pass

def main():
    try:
        orders = [("Laptop", "2", "50000"), ("Mouse", "1", "1000")]
        # orders = [("Keyboard", "-1", "2000")]
        # orders = []

        if  0 == len(orders):
            raise ZeroOrderError("Order list is empty.")

        total = 0
        for i, qty, price in orders:
            qty = int(qty)
            price = int(price)

            if qty < 0:
                raise NegativeValueError("Quantity cannot be negative.")
            if price < 0:
                raise NegativeValueError("Price cannot be negative.")

            total += qty * price

        print("Total cost: ₹", total)

    except ValueError:
        print("Error: Quantity or price must be a number.")
    except (NegativeValueError, ZeroOrderError) as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
