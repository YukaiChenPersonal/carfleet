from abc import ABC
import numpy as np


class Tire(ABC):
    def need_serv(self):
        pass


class carrigan_tire(Tire):
    def __init__(self, sensor_array):
        if len(sensor_array) != 4:
            print("syntax error, tire sensor array length should be 4...")
            return
        for num in sensor_array:
            if num>1 or num<0:
                print("value error, tire sensor array value should be between 0 to 1")
                return

        self.sensor_array = sensor_array

    def need_serv(self):
        count = 0
        for num in self.sensor_array:
            if num >= 0.9:
                count += 1

        if count >= 1:
            return True
        else:
            return False


class octoprime_tire(Tire):
    def __init__(self, sensor_array):
        if len(sensor_array) != 4:
            print("syntax error, tire sensor array length should be 4...")
            return
        for num in sensor_array:
            if num > 1 or num < 0:
                print("value error, tire sensor array value should be between 0 to 1...")
                return

        self.sensor_array = sensor_array

    def need_serv(self):
        if sum(self.sensor_array) >= 3:
            return True
        else:
            return False
