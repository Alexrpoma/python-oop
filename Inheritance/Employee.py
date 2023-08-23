from Inheritance.Person import Person


class Employee(Person):
    def __init__(self, first_name, last_name, email, age, role_name, salary):
        super().__init__(first_name, last_name, email, age)
        self.salary = salary
        self.role_name = role_name

    def role(self):
        return "The %s has a salary of %i" % (self.role_name, self.salary)

    def person_info(self):
        return """
            Employee name: %s %s
            Email: %s
            Age: %i
            Role: %s
        """ % (self.first_name, self.last_name, self.email, self.age, self.role_name)
