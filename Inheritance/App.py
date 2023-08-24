from Inheritance.Customer import Customer
from Inheritance.Employee import Employee
from Inheritance.Roles import Roles
from Inheritance.Status import Status


alex = Customer(
    "alex",
    "doe",
    "alex@gmail.com",
    25,
    Status.ACTIVE.name)
print(alex.person_info())

anna = Employee(
    "Anna",
    "Garden",
    "anna@outlook.com",
    21, Roles.ENGINEER.name,
    8000)
print(anna.person_info())
