"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')

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
        salary_info = f"{self.name} works on a monthly salary of {self.monthly_salary}"
        bonus_info = f"and receives a bonus commission of {self.bonus_commission}."
        total_pay_info = f"Their total pay is {self.get_pay()}."
        return f"{salary_info} {bonus_info} {total_pay_info}"


class HourlyEmployeeWithBonus(HourlyEmployee):
    def __init__(self, name, hours_worked, hourly_rate, bonus_commission):
        super().__init__(name, hours_worked, hourly_rate)
        self.bonus_commission = bonus_commission

    def get_pay(self):
        return super().get_pay() + self.bonus_commission

    def __str__(self):
        hourly_info = f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour"
        bonus_info = f"and receives a bonus commission of {self.bonus_commission}."
        total_pay_info = f"Their total pay is {self.get_pay()}."
        return f"{hourly_info} {bonus_info} {total_pay_info}"



class SalaryEmployeeWithContractCommission(SalaryEmployee):
    def __init__(self, name, monthly_salary, num_commissions, commission_rate):
        super().__init__(name, monthly_salary)
        self.num_commissions = num_commissions
        self.commission_rate = commission_rate

    def get_pay(self):
        commission_pay = self.num_commissions * self.commission_rate
        return super().get_pay() + commission_pay

    def __str__(self):
        salary_info = f"{self.name} works on a monthly salary of {self.monthly_salary}"
        commission_info = f"and receives a commission for {self.num_commissions} contract(s) at {self.commission_rate}/contract."
        total_pay_info = f"Their total pay is {self.get_pay()}.$"
        return f"{salary_info} {commission_info} {total_pay_info}"

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
        hourly_info = f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour"
        commission_info = f"and receives a commission for {self.num_commissions} contract(s) at {self.commission_rate}/contract."
        total_pay_info = f"Their total pay is {self.get_pay()}.$"
        return f"{hourly_info} {commission_info} {total_pay_info}"

        
# Examples of different employees
billie = SalaryEmployee('Billie', 4000)
charlie = HourlyEmployee('Charlie', 100, 25)
renee = SalaryEmployeeWithContractCommission('Renee', 3000, 4, 200)
jan = HourlyEmployeeWithContractCommission('Jan', 150, 25, 3, 220)
robbie = SalaryEmployeeWithBonus('Robbie', 2000, 1500)
ariel = HourlyEmployeeWithBonus('Ariel', 120, 30, 600)

# Test cases
#print(f"{billie}: billie.get_pay() must return {billie.get_pay()}.")
#print(f"{charlie}: charlie.get_pay() must return {charlie.get_pay()}.")
#print(f"{renee}: renee.get_pay() must return {renee.get_pay()}.")
#print(f"{jan}: jan.get_pay() must return {jan.get_pay()}.")
#print(f"{robbie}: robbie.get_pay() must return {robbie.get_pay()}.")
#print(f"{ariel}: ariel.get_pay() must return {ariel.get_pay()}.")
