class capulet_engine:
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def need_serv(self):
        return self.current_mileage - self.last_service_mileage > 30000

class sternman_engine:
    def __init__(self, warning_on):
        self.warning_on = warning_on

    def need_serv(self):
        if self.warning_on:
            return True
        else:
            return False

class willoughby_engine:
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def need_serv(self):
        return self.current_mileage - self.last_service_mileage > 60000
