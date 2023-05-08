# private
# public
# protected


class Bus:
    def __init__(self, brand='no name', price=0, number=0):
        self.__brand = brand    # protected
        self.__price = price    # protected
        self.__number = number  # protected

    def get__brand(self):
        return self.__brand

    def set_brand(self, name):
        self.__brand = name

    def get_number(self):
        return self.__number

    def set_number(self, name):
        self.__number = name
    def get_price(self):
        return self.__price

    def set_price(self, name):
        self.__number = name

    # def __del__(self):
    #     print(f"destructor for {self.brand}")

    def __str__(self):
        return f"Bus: {self.__brand}, price = ${self.__price}," \
    f"number = {self.__number}"

if __name__ == "__main__":
    bus = Bus()
    # bus.price = 12000
    # print(bus.price)

    bus.set_price(12000)
    print(bus.get_price())