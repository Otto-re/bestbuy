import products
from store import Store

if __name__ == "__main__":

    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = products.Product("MacBook Air M2", price=1450, quantity=100)
    pixel = products.Product("Google Pixel 7", price=500, quantity=250)

    best_buy = Store([bose, mac])
    best_buy.add_product(pixel)

    price = best_buy.order([(bose, 5), (mac, 5), (bose, 5),])
    print(f"order cost: {price} dollers.")

    print(best_buy.get_total_quantity())
    for product in best_buy.get_all_products():
        print(product.show())

