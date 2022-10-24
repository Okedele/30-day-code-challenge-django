class PersonalInfo:
    def __init__(self, name, address, age, phone_number):
        self.name = name
        self.address = address
        self.age = age
        self.phone_number = phone_number

    def print_name(self):
        print(f"Name: {self.name}")

    def print_address(self):
        print(f"Address: {self.address}")

    def print_age(self):
        print(f"Age: {self.age}")

    def print_phone(self):
        print(f"Phone Number: {self.phone_number}")
