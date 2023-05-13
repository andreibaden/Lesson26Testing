from Task_Lesson26.bus import *
class Manager:
    def find_bus(buses):
        if not isinstance(buses, (list, tuple)):
            return Bus()

        target = buses[0]
        for vel in buses:
            if isinstance(vel, Bus):
                if (vel.get_price() / vel.get_number()) < (target.get_price() / target.get_number()):
                    target = vel

        return target

if __name__ == "__main__":
    bus = Bus()
    bus.set_price(55000)
    bus.set_brand("volvo")
    bus.set_number(100)
    print(bus)
    print(bus.get_price() / bus.get_number())