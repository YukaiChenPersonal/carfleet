from abc import ABC, abstractmethod

class Battery(ABC):
    
    @abstractmethod
    def battery_type(self):
        pass


class SpindlerBattery(Battery):
    def battery_type(self, cur_date, last_serv_date):
        self.cur_date = cur_date
        self.last_serv_date = last_serv_date

    def battery_should_be_serviced(self):
        return self.cur_date - self.last_serv_date > 2 * 365

class NubbinBattery(Battery):
    def battery_type(self, cur_date, last_serv_date):
        self.cur_date = cur_date
        self.last_serv_date = last_serv_date

    def battery_should_be_serviced(self):
        return self.cur_date - self.last_serv_date > 4 * 365
