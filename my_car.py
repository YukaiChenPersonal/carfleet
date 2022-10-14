from abc import ABC, abstractmethod
from engine import capulet_engine
from engine import sternman_engine
from engine import willoughby_engine

from battery import spindler_battery
from battery import nubbin_battery
from datetime import datetime, date



# class Serviceable(ABC):
#     @abstractmethod
#     def need_serv(self):
#         pass


class Car:
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_serv(self) -> bool:
        return self.engine.need_serv() or self.battery.need_serv()


class CarFactory:
    @staticmethod
    def create_calliope(cur_date, last_serv_date, cur_mileage, last_serv_mileage):
        engine = capulet_engine(cur_mileage, last_serv_mileage)
        battery = spindler_battery(cur_date, last_serv_date)
        return Car(engine, battery)

    @staticmethod
    def create_glissade(cur_date, last_serv_date, cur_mileage, last_serv_mileage):
        engine = willoughby_engine(cur_mileage, last_serv_mileage)
        battery = spindler_battery(cur_date, last_serv_date)
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(cur_date, last_serv_date, warning_on):
        engine = sternman_engine(warning_on)
        battery = spindler_battery(cur_date, last_serv_date)
        return Car(engine, battery)

    @staticmethod
    def create_rorschach(cur_date, last_serv_date, cur_mileage, last_serv_mileage):
        engine = willoughby_engine(cur_mileage, last_serv_mileage)
        battery = nubbin_battery(cur_date, last_serv_date)
        return Car(engine, battery)

    @staticmethod
    def create_thovex(self, cur_date, last_serv_date, cur_mileage, last_serv_mileage):
        engine = capulet_engine(cur_mileage, last_serv_mileage)
        battery = nubbin_battery(cur_date, last_serv_date)
        return Car(engine, battery)




