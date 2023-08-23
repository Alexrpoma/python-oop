class Person:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

    def person_info(self):
        return """
            First name: %s
            Last name: %s
            Email: %s
            Age: %i
        """ % (self.first_name, self.last_name, self.email, self.age)
