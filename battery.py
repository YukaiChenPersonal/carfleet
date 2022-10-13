class spindler_battery:
    def __init__(self, cur_date, last_serv_date):
        self.cur_date = cur_date
        self.last_serv_date = last_serv_date

    def need_serv(self):
        return self.cur_date - self.last_serv_date > 2 * 365

class nubbin_battery:
    def __init__(self, cur_date, last_serv_date):
        self.cur_date = cur_date
        self.last_serv_date = last_serv_date

    def need_serv(self):
        return self.cur_date - self.last_serv_date > 4 * 365
