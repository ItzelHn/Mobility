class ElectricVehicle:
    __FULL_CHARGE = 100

    def __init__(self, battery, *args, **kwargs):
        self.__battery = battery
        self.__needs_charge = False
        super(ElectricVehicle, self).__init__()

    @property
    def needs_charge(self):
        return self.__needs_charge

    @needs_charge.setter
    def needs_charge(self, value):
        self.__needs_charge = value
        self.update_vehicle()

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__needs_charge = value < 15

        if value < 0:
            self.__battery = 0
        elif value > 100:
            self.__battery = 100
        else:
            self.__battery = value
            self.update_vehicle()

    def charge(self):
        self.__battery = ElectricVehicle.__FULL_CHARGE
        self.__needs_charge = False
