from products import Product
from cart import Cart
from discounts import  apply_discount

def main():
    p1 = Product(101, "Laptop", 50000)
    p2 = Product(102, "Mouse", 1000)
    p3 = Product(201, "Phone", 30000)
    p4 = Product(202,"Charger", 1500)
    p5 = Product(203,  "Case", 500)

    cart = Cart([])

    mp = {"Laptop" : p1 , "Mouse": p2, "Phone": p3
          , "Charger": p4, "Case": p5}

    print('Available Products details...')
    print("Laptop, 50000")
    print("Mouse, 1000")
    print("Phone, 30000")
    print("Charger, 1500")
    print("Case, 500")

    # print('Actions...')
    print("Add product")
    print('Enter a product:')
    product_name = input()

    cart.add_product(mp[product_name])

    print("Add another product")
    print('Enter a product:')
    product_name = input()

    cart.add_product(mp[product_name])

    print('Want to remove product:(y/n):')
    choice = input()

    if choice == 'y':
        product_name = input()
        if cart.remove_product(product_name):
            print('removed')

            print("Add another product")
            print('Enter a product:')
            product_name = input()

            cart.add_product(mp[product_name])
        else:
            print('Product not found')

    print('Enter coupon code:')
    code = input()

    cart.display()

    total_price = cart.calculate_total_price()
    print('Total before discount: ₹', total_price)

    discount_price = apply_discount(total_price, code)
    print('discount: ₹',discount_price)
    print('Final total: ₹' , total_price - discount_price)






if __name__ == "__main__":
    main()