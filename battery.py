from abc import ABC
from datetime import date


def add_years(olddate, addnum):
    try:
        newdate = date(olddate.year+addnum, olddate.month, olddate.day)
        return newdate
    except ValueError:
        newdate = date(olddate.year+addnum, olddate.month, 28)
        return newdate


class Battery(ABC):
    def need_serv(self):
        pass


class spindler_battery(Battery):
    def __init__(self, cur_date, last_serv_date):
        self.cur_date = cur_date
        self.last_serv_date = last_serv_date

    def need_serv(self):
        date_should_service = add_years(self.last_serv_date, 3)
        if date_should_service < self.cur_date:
            return True
        else:
            return False


class nubbin_battery(Battery):
    def __init__(self, cur_date, last_serv_date):
        self.cur_date = cur_date
        self.last_serv_date = last_serv_date

    def need_serv(self):
        date_should_service = add_years(self.last_serv_date, 4)
        if date_should_service < self.cur_date:
            return True
        else:
            return False
