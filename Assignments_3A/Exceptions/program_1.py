def main():

    books = ["Book1", "Book2", "Book3"]

    # read quantity
    try:
        q = int(input("Enter the quantity of books:"))
    except ValueError:
        print("Error: Input should be a valid integer. Please enter quantity again.")

    # read price
    try:
        price = float(input("Enter the price of the book:"))
    except ValueError:
        print("Error: Invalid price format. Please enter price again.")

    # read index
    try:
        index = int(input("Enter index to update:"))
        books[index] = "Updated Book"
        print(books)
    except IndexError:
        print("Error: Index out of bounds. Please enter a valid index.")


if __name__ == "__main__":
    main()
