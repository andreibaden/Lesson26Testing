class Bus:
    def __init__(self, brand='no name', number=0, price=0):
        self.__brand = brand
        self.__number = number
        self.__price = price
    def get_brand(self):
        return self.__brand
    def set_brand(self, name):
        self.__brand = name
    def get_number(self):
        return self.__number
    def set_number(self, name):
        self.__number = name

    def get_price(self):
        return self.__price
    def set_price(self, price):
        if price > 0:
            self.__price = price

    # def __del__(self):
    #     print(f"destructor for {self.brand}")

    def __str__(self):
        return f"Bus: {self.__brand}, price = ${self.__price}," \
               f"number = {self.__number}"


# if __name__ == "__main__":
#     bus = Bus()
#     print(bus)
#     bus.set_price(5500)
#     bus.set_brand("Ferrari")
#     bus.set_number(3333)
#     print(bus)
#     print(bus.get_price() / bus.get_number())
