import unittest
from datetime import date, datetime

from engine import capulet_engine
from engine import sternman_engine
from engine import willoughby_engine

from battery import spindler_battery
from battery import nubbin_battery


class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        cur_mileage = 30001
        last_serv_mileage = 0

        engine = capulet_engine(cur_mileage, last_serv_mileage)
        self.assertTrue(engine.need_serv(), "capulet, expect yes service")

    def test_engine_should_not_be_serviced(self):
        cur_mileage = 30000
        last_serv_mileage = 0

        engine = capulet_engine(cur_mileage, last_serv_mileage)
        self.assertFalse(engine.need_serv(), "capulet, expect no service")


class TestSternman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_on = True

        engine = sternman_engine(warning_on)
        self.assertTrue(engine.need_serv(), "sternman, expect yes service")

    def test_engine_should_not_be_serviced(self):
        warning_on = False

        engine = sternman_engine(warning_on)
        self.assertFalse(engine.need_serv(), "sternman, expect no service")


class TestWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        cur_mileage = 60001
        last_serv_mileage = 0

        engine = willoughby_engine(cur_mileage, last_serv_mileage)
        self.assertTrue(engine.need_serv(), "willoughby, expect yes service")

    def test_engine_should_not_be_serviced(self):
        cur_mileage = 60000
        last_serv_mileage = 0

        engine = willoughby_engine(cur_mileage, last_serv_mileage)
        self.assertFalse(engine.need_serv(), "willoughby, expect no service")

class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_serv_date = today.replace(year=today.year -3)

        battery = spindler_battery(today, last_serv_date)
        self.assertTrue((battery.need_serv()), "spindler, expect yes service")

    def test_battery_should_not_be_Serviced(self):
        today = datetime.today().date()
        last_serv_date = today.replace(year=today.year -1)

        battery = spindler_battery(today, last_serv_date)
        self.assertFalse(battery.need_serv(), "spindler, expect no service")


class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_serv_date = today.replace(year=today.year - 5)

        battery = nubbin_battery(today, last_serv_date)
        self.assertTrue((battery.need_serv()), "nubbin, expect yes service")

    def test_battery_should_not_be_Serviced(self):
        today = datetime.today().date()
        last_serv_date = today.replace(year=today.year - 3)

        battery = nubbin_battery(today, last_serv_date)
        self.assertFalse(battery.need_serv(), "nubbin, expect no service")


if __name__ == '__main__':
    unittest.main()