"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name


class SalaryEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def get_pay(self):
        return self.monthly_salary

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary}. Their total pay is {self.get_pay()}."


class HourlyEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        super().__init__(name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def get_pay(self):
        return self.hours_worked * self.hourly_rate

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour. Their total pay is {self.get_pay()}."


class SalaryEmployeeWithBonus(SalaryEmployee):
    def __init__(self, name, monthly_salary, bonus_commission):
        super().__init__(name, monthly_salary)
        self.bonus_commission = bonus_commission

    def get_pay(self):
        return super().get_pay() + self.bonus_commission

    def __str__(self):
        salary_info = super().__str__()
        return f"{salary_info} and receives a bonus commission of {self.bonus_commission}. Their total pay is {self.get_pay()}."


class HourlyEmployeeWithBonus(HourlyEmployee):
    def __init__(self, name, hours_worked, hourly_rate, bonus_commission):
        super().__init__(name, hours_worked, hourly_rate)
        self.bonus_commission = bonus_commission

    def get_pay(self):
        return super().get_pay() + self.bonus_commission

    def __str__(self):
        hourly_info = super().__str__()
        return f"{hourly_info} and receives a bonus commission of {self.bonus_commission}. Their total pay is {self.get_pay()}."


class SalaryEmployeeWithContractCommission(SalaryEmployee):
    def __init__(self, name, monthly_salary, num_commissions, commission_rate):
        super().__init__(name, monthly_salary)
        self.num_commissions = num_commissions
        self.commission_rate = commission_rate

    def get_pay(self):
        commission_pay = self.num_commissions * self.commission_rate
        return super().get_pay() + commission_pay

    def __str__(self):
        salary_info = super().__str__()
        return f"{salary_info} and receives a commission for {self.num_commissions} contract(s) at {self.commission_rate}/contract. Their total pay is {self.get_pay()}."


class HourlyEmployeeWithContractCommission(HourlyEmployee):
    def __init__(self, name, hours_worked, hourly_rate, num_commissions, commission_rate):
        super().__init__(name, hours_worked, hourly_rate)
        self.num_commissions = num_commissions
        self.commission_rate = commission_rate

    def get_pay(self):
        contract_pay = super().get_pay()
        commission_pay = self.num_commissions * self.commission_rate
        return contract_pay + commission_pay

    def __str__(self):
        hourly_info = super().__str__()
        return f"{hourly_info} and receives a commission for {self.num_commissions} contract(s) at {self.commission_rate}/contract. Their total pay is {self.get_pay()}."


# Examples of different employees
billie = SalaryEmployee('Billie', 4000)
charlie = HourlyEmployee('Charlie', 100, 25)
renee = SalaryEmployeeWithContractCommission('Renee', 3000, 4, 200)
jan = HourlyEmployeeWithContractCommission('Jan', 150, 25, 3, 220)
robbie = SalaryEmployeeWithBonus('Robbie', 2000, 1500)
ariel = HourlyEmployeeWithBonus('Ariel', 120, 30, 600)

# Test cases
print(str(billie))
print(str(charlie))
print(str(renee))
print(str(jan))
print(str(robbie))
print(str(ariel))
