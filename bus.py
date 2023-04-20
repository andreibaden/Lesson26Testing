# private
# public
# protected


class Bus:
    def __init__(self, brand='no name', price=0, number=0):
        self.brand = brand    # public
        self.price = price    # public
        self.number = number  # public

    # def __del__(self):
    #     print(f"destructor for {self.brand}")

    def __str__(self):
        return f"Bus: {self.brand}, price = ${self.price}," \
    f"number = {self.number}"

if __name__ == "__main__":
    # bus1 = Bus("Scania", 23000, 42)
    # bus2 = Bus("MAZ", 12000, 34)
    # bus3 = Bus("Volvo", 31000, 48)
    # bus4 = Bus("PAZ", 11000, 15)
    # bus5 = Bus("Mercedes Benz", 123000, 67)
    #
    # print(bus1.__str__())


