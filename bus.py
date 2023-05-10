# private
# public
# protected


class Bus:
    def __init__(self, brand='no name', price=0, number=0000):
        self.__brand = brand    # protected
        self.__price = price    # protected
        self.__number = number  # protected

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

    def set_price(self, name):
        self.__price = name

    # def __del__(self):
    #     print(f"destructor for {self.brand}")

    def __str__(self):
        return f"Bus: {self.__brand}, price = ${self.__price}," \
    f"number = {self.__number}"

if __name__ == "__main__":
    bus = Bus()
    # bus.price = 12000
    # bus.brand = "VAZ"
    # bus.number = 7777
    # print(bus.price, bus.brand, bus.number)

    bus.set_price(5500)
    bus.set_brand("Ferrari")
    bus.set_number(3333)
    print(bus.get_brand(), bus.get_price(),bus.get_number())
