from abc import ABC, abstractmethod
from engine import capulet_engine
from engine import sternman_engine
from engine import willoughby_engine

from battery import spindler_battery
from battery import nubbin_battery

from tire import carrigan_tire
from tire import octoprime_tire



# class Serviceable(ABC):
#     @abstractmethod
#     def need_serv(self):
#         pass


class Car:
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_serv(self) -> bool:
        return self.engine.need_serv() or self.battery.need_serv() or self.tire.need_serv()


class CarFactory:
    @staticmethod
    def create_calliope(cur_date, last_serv_date, cur_mileage, last_serv_mileage, sensor_array):
        engine = capulet_engine(cur_mileage, last_serv_mileage)
        battery = spindler_battery(cur_date, last_serv_date)
        tire = carrigan_tire(sensor_array)
        return Car(engine, battery, tire)

    @staticmethod
    def create_glissade(cur_date, last_serv_date, cur_mileage, last_serv_mileage, sensor_array):
        engine = willoughby_engine(cur_mileage, last_serv_mileage)
        battery = spindler_battery(cur_date, last_serv_date)
        tire = octoprime_tire(sensor_array)
        return Car(engine, battery, tire)

    @staticmethod
    def create_palindrome(cur_date, last_serv_date, warning_on, sensor_array):
        engine = sternman_engine(warning_on)
        battery = spindler_battery(cur_date, last_serv_date)
        tire = carrigan_tire(sensor_array)
        return Car(engine, battery, tire)

    @staticmethod
    def create_rorschach(cur_date, last_serv_date, cur_mileage, last_serv_mileage, sensor_array):
        engine = willoughby_engine(cur_mileage, last_serv_mileage)
        battery = nubbin_battery(cur_date, last_serv_date)
        tire = octoprime_tire(sensor_array)
        return Car(engine, battery, tire)

    @staticmethod
    def create_thovex(self, cur_date, last_serv_date, cur_mileage, last_serv_mileage, sensor_array):
        engine = capulet_engine(cur_mileage, last_serv_mileage)
        battery = nubbin_battery(cur_date, last_serv_date)
        tire = carrigan_tire(sensor_array)
        return Car(engine, battery, tire)




