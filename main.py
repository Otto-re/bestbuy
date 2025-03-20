import products
import store

product_list = [
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Google Pixel 7", price=500, quantity=250)
]

best_buy = store.Store(product_list)

def start(store):
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        chose = input("Please choose a number:")

        if chose == "1":
            #list all products
            for product in store.get_all_products():
                print(product.show())

        elif chose == "2":
            #show total quantity of products in store
            print(f"Total quantity in store: {store.get_total_quantity()}")



        elif chose == "3":

            # Make an order

            shopping_list = []

            print("------")

            # List all products with a number

            for i, product in enumerate(store.get_all_products(), 1):
                print(f"{i}. {product.show()}")

            while True:
                product_choice = input("------\nWhen you want to finish order, enter empty text.\nWhich product # do you want? ")
                # If input is empty, stop the order
                if not product_choice:
                    break

                product_choice = int(product_choice) - 1
                if 0 <= product_choice < len(store.get_all_products()):
                    product = store.get_all_products()[product_choice]
                    quantity = int(input(f"What amount do you want? "))
                    shopping_list.append((product, quantity))
                    print("Product added to list!")
                else:
                    print("Invalid product selection.")

            if shopping_list:
                total_price = store.order(shopping_list)
                print(f"Order placed. Total cost: {total_price} dollars.")
            else:
                print("No products were ordered.")

        elif chose == "4":
            print("exiting the programm")
            break

        else:
            print("invalid choise  please select valid choise")

if __name__ == "__main__":
    start(best_buy)