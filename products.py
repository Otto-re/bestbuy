class Product:
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("ungültiger Eingabewert")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        #gibt die menge des produkts zurück
        return self.quantity

    def set_quantity(self, quantity):
        #setzt die menge des produkts und deaktiviert sie wenn die menge 0 erreicht
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        #gibt zurück ob das produkt aktive ist
        return self.active

    def activate(self):
        #aktiviert das produkt
        self.active = True

    def deactivate(self):
        #deaktiviert das produkt
        self.active = False

    def show(self) -> str:
        #zeigt beschreibung des produkts
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        #kauf eine bestimmte menge und gibt gesammtpreis zurück
        if quantity > self.quantity:
            raise ValueError("nicht genügend Artikel vorhanden")

        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total_price

