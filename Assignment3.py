class Staff:
    def __init__(self, eid, emp_name, salary):
        self.eid = eid
        self.emp_name = emp_name
        self.salary = salary

    def compute(self):
        hra = 0.2 * self.salary
        da = 0.1 * self.salary
        gross = self.salary + hra + da
        tax = 0.05 * gross
        net = gross - tax

        return hra, da, tax, gross, net

    def show_details(self):
        hra, da, tax, gross, net = self.compute()

        print("\n - Salary Details - \n")
        print(f"ID            : {self.eid}")
        print(f"Name          : {self.emp_name}")
        print(f"Basic Salary  : ₹{self.salary:.2f}")
        print(f"HRA           : ₹{hra:.2f}")
        print(f"DA            : ₹{da:.2f}")
        print(f"Tax           : ₹{tax:.2f}")
        print(f"Gross Salary  : ₹{gross:.2f}")
        print(f"Net Salary    : ₹{net:.2f}")


# Taking input
try:
    eid = int(input("Enter ID: "))
    emp_name = input("Enter Name: ")
    salary = float(input("Enter Basic Salary: "))

    employee = Staff(eid, emp_name, salary)
    employee.show_details()

except ValueError:
    print("Invalid input! Please enter correct values.")