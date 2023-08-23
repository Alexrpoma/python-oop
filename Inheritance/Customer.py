from Inheritance.Person import Person


class Customer(Person):
    def __init__(self, first_name, last_name, email, age, status):
        super().__init__(first_name, last_name, email, age)
        self.status = status

    def person_info(self):
        return """
            Customer info:
            First name: %s
            Last name: %s
            Email: %s
            Age: %i
            Status: %s
        """ % (self.first_name, self.last_name, self.email, self.age, self.status)
