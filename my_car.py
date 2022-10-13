from abc import ABC, abstractmethod
from .engine import capulet_engine
from .engine import sternman_engine
from .engine import willoughby_engine
from .battery import spindler_battery
from .battery import nubbin_battery



class Servicable(ABC):
    @abstractmethod
    def need_serv():
        pass

class Car(Servicable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_serv(self)->bool:
        return self.engine.need_serv() | self.battery.need_serv()

class CarFactory:
    def create_calliope(self, cur_date, last_serv_date, cur_mileage, last_serv_mileage):
        engine = capulet_engine(cur_mileage, last_serv_mileage)
        battery = spindler_battery(cur_date, last_serv_date)
        return Car(engine, battery)

    def create_glissade(self, cur_date, last_serv_date, cur_mileage, last_serv_mileage):
        engine = willoughby_engine(cur_mileage, last_serv_mileage)
        battery = spindler_battery(cur_date, last_serv_date)
        return Car(engine, battery)

    def create_palindrome(self, cur_date, last_serv_date, warning_on):
        engine = sternman_engine(warning_on)
        battery = spindler_battery(cur_date, last_serv_date)
        return Car(engine, battery)

    def create_rorschach(self, cur_date, last_serv_date, cur_mileage, last_serv_mileage):
        engine = willoughby_engine(cur_mileage, last_serv_mileage)
        battery = nubbin_battery(cur_date, last_serv_date)
        return Car(engine, battery)

    def create_thovex(self, cur_date, last_serv_date, cur_mileage, last_serv_mileage):
        engine = capulet_engine(cur_mileage, last_serv_mileage)
        battery = nubbin_battery(cur_date, last_serv_date)
        return Car(engine, battery)
    






        


