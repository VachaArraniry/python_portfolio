class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_discount_price(self, discount):
        return self.price - (self.price * (discount/100))

class Shoes(Product):

    def __init__(self, name, price, brand, size, color):
        Product.__init__(self, name, price)
        self.brand = brand
        self.size = size
        self.color = color

class Book(Product):

    def __init__(self, name, price, author, genre):
        Product.__init__(self, name, price)
        self.author = author
        self.genre = genre

air_max = Shoes(name="Nike Air Max", price=4000000, brand="Nike", size=43, color="White")
python_book = Book(name="Python Book", price=2000, author="John", genre="Computer")

print(air_max.price)
print(python_book.author)
print(air_max.calculate_discount_price(50))