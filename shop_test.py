class Shop:

    def __init__(self, name, owner, address, products):
        self.name = name
        self.owner = owner
        self.address = address
        self.products = products

    def __str__(self):
        return self.name + " - " + self.address

    def add_product(self, product):
        self.products.append(product)

    def get_all_products(self):
        if len(self.products) > 0:
            for p in self.products:
                print("{0} - IDR {1} - Discount {2}".format(p.title,
                      p.price, p.discounted_price))
        else:
            print("the shop has no products yet")

    #homework (unfinished)
    def get_product(self, id):
        pass


class Product:

    def __init__(self, id, title, price, quantity, description, discount):
        self.id = id
        self.title = title
        self.price = price
        self.quantity = quantity
        self.description = description
        self.discount = discount

    #homework (unfinished)
    def discounted_price(self, discount):
        self.discount.append(Shop)

    def discounted_price_total(self):
        if len(self.discount) > 0:
            calculation = self.price*self.discount/100
            calculation - self.price
        else:
            print("no discounts")

    #homework (unfinished)
    #def discounted_price(self, discount):
        #calculation = self.price * self.discount // 100
        #calculation - self.price


abc_shop = Shop(name="Toko ABC", owner="John Doe",
                address="Jalan Raya no 3", products=[])

abc_product = Product(id=[], title=[], price=[],
                      quantity=[], description=[], discount=[])

print(abc_shop)


playstation_4 = Product(id=1, title='Playstation 4', price=4500000, quantity=4,
                        description='A good console', discount=50)

vintage_gameboy = Product(id=2, title='Vintage Gameboy', price=800000, quantity=3,
                          description='A vintage gameboy', discount=50)

abc_shop.add_product(playstation_4)
abc_shop.add_product(vintage_gameboy)

abc_product.discounted_price(playstation_4)
abc_product.discounted_price(vintage_gameboy)

print(abc_shop.products)
print(abc_shop.get_all_products())

print(abc_product.discount)
print(abc_product.discounted_price_total())
