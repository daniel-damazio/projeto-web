class UserContact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f'Contact name: {self.name} | Contact email: {self.email}'