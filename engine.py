class capulet_engine:
    def __init__(self, cur_mileage, last_serv_mileage):
        self.cur_mileage = cur_mileage
        self.last_serv_mileage = last_serv_mileage

    def need_serv(self):
        return self.cur_mileage - self.last_serv_mileage > 30000

class sternman_engine:
    def __init__(self, warning_on):
        self.warning_on = warning_on

    def need_serv(self):
        if self.warning_on:
            return True
        else:
            return False

class willoughby_engine:
    def __init__(self, cur_mileage, last_serv_mileage):
        self.cur_mileage = cur_mileage
        self.last_serv_mileage = last_serv_mileage

    def need_serv(self):
        return self.cur_mileage - self.last_serv_mileage > 60000