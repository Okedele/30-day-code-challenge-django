# PERSONAL INFO CLASS
from PersonalInfo import PersonalInfo
from Car import Car


def personal_info():
    info1 = PersonalInfo("Promise", "Lagos", "20", "07063612121")
    info2 = PersonalInfo("Kayode", "Lagos", "20", "08122344423")
    info3 = PersonalInfo("Ahmad", "Lagos", "20", "07022344332")

    info1.print_name()
    info1.print_address()
    info1.print_age()
    info1.print_phone()

    info2.print_name()
    info2.print_address()
    info2.print_age()
    info2.print_phone()

    info3.print_name()
    info3.print_address()
    info3.print_age()
    info3.print_phone()


def car():
    car = Car("2022", "Toyota Corolla")
    for i in range(5):
        print("Accelerating.....")
        car.accelerate()
        speed = car.get_speed()
        print(f"The current speed of the {car.year_model} {car.make} is: {speed}")

    for i in range(5):
        print("Braking.....")
        car.brake()
        speed = car.get_speed()
        print(f"The current speed of the {car.year_model} {car.make} is: {speed}")


personal_info()
car()
