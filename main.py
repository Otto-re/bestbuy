from products import Product

def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))  # 50 * 250 = 12500
    print(mac.buy(100))  # 100 * 1450 = 145000
    print(mac.is_active())  # False, weil Menge 0 ist

    print(bose.show())  # "Bose QuietComfort Earbuds, Preis: 250, Menge: 450"
    print(mac.show())   # "MacBook Air M2, Preis: 1450, Menge: 0"

    bose.set_quantity(1000)
    print(bose.show())  # "Bose QuietComfort Earbuds, Preis: 250, Menge: 1000"

if __name__ == "__main__":
    main()