# private
# public
# protected


class Bus:
    def __init__(self, brand='no name', price=0, number=0):
        self._brand = brand    # protected
        self._price = price    # protected
        self._number = number  # protected

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
            self.__number = name

    # def __del__(self):
    #     print(f"destructor for {self.brand}")

    def __str__(self):
        return f"Bus: {self._brand}, price = ${self._price}," \
    f"number = {self._number}"

if __name__ == "__main__":
    bus = Bus()


    # bus1 = Bus("Scania", 23000, 42)
    # bus2 = Bus("MAZ", 12000, 34)
    # bus3 = Bus("Volvo", 31000, 48)
    # bus4 = Bus("PAZ", 11000, 15)
    # bus5 = Bus("Mercedes Benz", 123000, 67)
    # # print(bus1.__str__())
    # print(Bus._number)



