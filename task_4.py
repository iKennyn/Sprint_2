class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls ,name, rest_days, email):
        current_hour = (7 - rest_days) * 8
        return cls(name, current_hour, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days):
        current_email = f"{name}@email.com"
        return cls(name, hours, rest_days, current_email)

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        return self.hours * self.hourly_payment