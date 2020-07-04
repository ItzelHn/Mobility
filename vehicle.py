from Homework4.micro_mobility.helpers.db_helper import update_db


class Vehicle:
    def __new__(cls, *args, **kwargs):
        if cls != Vehicle:
            return super().__new__(cls)
        raise TypeError("Class Vehicle may not be instantiated")

    def __init__(self, *args, **kwargs):
        self.__id = kwargs['_id']
        self.__status = 'locked'
        self._current_speed = 0
        super().__init__(*args)

    @property
    def id(self):
        return self.__id

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    def unlock(self):
        if self.__status == 'locked':
            self.__status = 'unlocked'
            self.update_vehicle()
        else:
            print(f'{self.__status} to \'unlocked\' is not a valid transition')

    def pick_up(self):
        if self.__status == 'locked':
            self.__status = 'in-transit'
            self.update_vehicle()
        else:
            print(f'{self.__status} to \'in-transit\' is not a valid transition')

    def stashed(self):
        if self.__status == 'in-transit':
            self.__status = 'in-warehouse'
            self.update_vehicle()
        else:
            print(f'{self.__status} to \'in-warehouse\' is not a valid transition')

    def back_to_service(self):
        if self.__status == 'in-warehouse':
            self.__status = 'deploying'
            self.update_vehicle()
        else:
            print(f'{self.__status} to \'in-warehouse\' is not a valid transition')

    def deploy(self):
        if self.__status == 'deploying':
            self.__status = 'locked'
            self.update_vehicle()
        else:
            print(f'{self.__status} to \'deploying\' is not a valid transition')

    def begin_ride(self):
        if self.__status == 'unlocked':
            self.__status = 'in-ride'
            self.update_vehicle()
        else:
            print(f'{self.__status} to \'in-ride\' is not a valid transition')

    def end_ride(self):
        if self.__status == 'in-ride' and self._current_speed == 0:
            self.__status = 'locked'
            self.update_vehicle()
            return True
        elif self._current_speed != 0:
            print(f'vehicle must be in a complete stop in order to end the ride')
        else:
            print(f'{self.__status} to \'locked\' is not a valid transition')
        return False

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, value):
        if self.__status == 'in-ride':
            self._current_speed = value
            self.update_vehicle()

    def update_vehicle(self):
        update_db(self)
