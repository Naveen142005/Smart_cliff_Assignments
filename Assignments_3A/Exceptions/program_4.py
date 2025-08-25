class InvalidAgeError(Exception): pass
class SeatLimitError(Exception): pass
def book_ticket(name, age, seats):
    if age < 0 or age > 120:
        raise InvalidAgeError("Age should be between 0 and 120.")
    if seats > 6:
        raise SeatLimitError("Can't book more than 6 seats...")
    print(f"Booking successful for {name}")

def main():
    try:
        name = input("name: ")
        age = int(input("age:"))
        seats = int(input("seats: "))
        book_ticket(name, age, seats)
    except ValueError:
        print("Error: Age and seats must be integers.")
    except InvalidAgeError as e:
        print("Error:",e)
    except SeatLimitError as e:
        print("Error:",e)

if __name__ == "__main__":
    main()
