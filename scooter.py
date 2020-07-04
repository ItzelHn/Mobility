from .vehicle import Vehicle
from .mixins.electric_vehicle import ElectricVehicle


class Scooter(Vehicle, ElectricVehicle):
    __MAX_SPEED = 35

    def __init__(self, _id, battery=99):
        super().__init__(battery, _id=_id)

    @classmethod
    def from_db(cls, **kwargs):
        # uuid = kwargs['id']
        instance = cls(kwargs['id'], battery=kwargs['battery'])
        instance.status = kwargs['status']
        instance.current_speed = kwargs['current_speed']
        return instance

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, value):
        if value > Scooter.__MAX_SPEED:
            self._current_speed = Scooter.__MAX_SPEED
        else:
            self._current_speed = value
            self.update_vehicle()

    def begin_ride(self):
        super().begin_ride()

    def back_to_service(self):
        if not self.needs_charge:
            super().back_to_service()
        else:
            print('The scooter needs charge, can\'t leave warehouse')

    def unlock(self):
        if not self.needs_charge:
            super().unlock()
        else:
            print('This scooter has no enough battery, please charge it')

    def end_ride(self):
        if super().end_ride():
            self.battery -= 17

    def charge(self):
        if self.status == 'in-warehouse':
            super().charge()
