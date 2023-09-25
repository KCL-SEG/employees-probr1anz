"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name
        self.total_pay = 0  # Initialize total pay to 0

    def get_pay(self):
        pass

    def __str__(self):
        pay_explanation = self.get_pay_explanation()
        return f"{self.name} - {pay_explanation}"

    def get_pay_explanation(self):
        return "Pay calculation explanation not available"


class MonthlyEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def get_pay(self):
        return self.monthly_salary

    def get_pay_explanation(self):
        return f"Monthly Salary: {self.monthly_salary}"


class ContractEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate, num_commissions=0, commission_rate=0):
        super().__init__(name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.num_commissions = num_commissions
        self.commission_rate = commission_rate

    def get_pay(self):
        contract_pay = self.hours_worked * self.hourly_rate
        commission_pay = self.num_commissions * self.commission_rate
        return contract_pay + commission_pay

    def get_pay_explanation(self):
        contract_explanation = f"Contract Pay: {self.hours_worked} hours * {self.hourly_rate}/hour"
        commission_explanation = f"Commission: {self.num_commissions} contracts * {self.commission_rate}/contract"
        return f"{contract_explanation}\n{commission_explanation}"


# Examples of different employees
billie = MonthlyEmployee('Billie', 4000)
charlie = ContractEmployee('Charlie', 100, 25, 0, 0)
renee = MonthlyEmployee('Renee', 3000)
renee.num_commissions = 4
renee.commission_rate = 200
jan = ContractEmployee('Jan', 150, 25, 3, 220)
robbie = MonthlyEmployee('Robbie', 2000)
robbie.total_pay = 1500  # Bonus commission
ariel = ContractEmployee('Ariel', 120, 30, 0, 600)

# Print each employee's details including pay explanation
employees = [billie, charlie, renee, jan, robbie, ariel]
for employee in employees:
    print(str(employee))
