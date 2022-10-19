# 'capital' QUIZ
import random
def capital():

    nigerian_states = [
        {"state": "Abia", "capital": "Umuahia"},
        {"state": "Adamawa", "capital": "Yola"},
        {"state": "Akwa Ibom", "capital": "Uyo"},
        {"state": "Anambra", "capital": "Awka"},
        {"state": "Bauchi", "capital": "Bauchi"},
        {"state": "Bayelsa", "capital": "Yenagoa"},
        {"state": "Benue", "capital": "Makurdi"},
        {"state": "Borno", "capital": "Maiduguri"},
        {"state": "Cross River", "capital": "Calabar"},
        {"state": "Delta", "capital": "Asaba"},
        {"state": "Ebonyi", "capital": "Abakaliki"},
        {"state": "Edo", "capital": "Benin"},
        {"state": "Ekiti", "capital": "Ado - Ekiti"},
        {"state": "Enugu", "capital": "Enugu"},
        {"state": "Gombe", "capital": "Gombe"},
        {"state": "Imo", "capital": "Owerri"},
        {"state": "Jigawa", "capital": "Dutse"},
        {"state": "Kaduna", "capital": "Kaduna"},
        {"state": "Kano", "capital": "Kano"},
        {"state": "Katsina", "capital": "Katsina"},
        {"state": "Kebbi", "capital": "Birnin Kebbi"},
        {"state": "Kogi", "capital": "Lokoja"},
        {"state": "Kwara", "capital": "Ilorin"},
        {"state": "Lagos", "capital": "Ikeja"},
        {"state": "Nasarawa", "capital": "Lafia"},
        {"state": "Niger", "capital": "Minna"},
        {"state": "Ogun", "capital": "Abeokuta"},
        {"state": "Ondo", "capital": "Akure"},
        {"state": "Osun", "capital": "Oshogbo"},
        {"state": "Oyo", "capital": "Ibadan"},
        {"state": "Plateau", "capital": "Jos"},
        {"state": "Rivers", "capital": "Port Harcourt"},
        {"state": "Sokoto", "capital": "Sokoto"},
        {"state": "Taraba", "capital": "Jalingo"},
        {"state": "Yobe", "capital": "Damaturu"},
        {"state": "Zamfara", "capital": "Gusau"},
    ]

    random_number = random.randint(1, 36)
    state = nigerian_states[random_number]["state"]
    capital = nigerian_states[random_number]["capital"]
    print(f"State: {state}")
    user_capital = input("Enter the state capital: ")
    guesses = 1
    while user_capital.lower() != capital.lower():
        user_capital = input("Wrong capital. Enter the state capital: ")
        guesses += 1
    if user_capital.lower() != state.lower():
        print(f"Correct. You got it right in {guesses} guess(es)")

capital()

# GALILEAN MOONS OF JUPITER
def jupiter_moons():
    moons = ["Io", "Europa", "Ganymede", "Callisto"]
    moon_radius = [
        {"moon": "Io", "radius": 1821.6},
        {"moon": "Europa", "radius": 1560.8},
        {"moon": "Ganymede", "radius": 2634.1},
        {"moon": "Callisto", "radius": 2410.3},
    ]
    moon_gravity = [
        {"moon": "Io", "gravity": 1.796},
        {"moon": "Europa", "gravity": 1.314},
        {"moon": "Ganymede", "gravity": 1.428},
        {"moon": "Callisto", "gravity": 1.235},
    ]
    moon_orbital_period = [
        {"moon": "Io", "period": 1.769},
        {"moon": "Europa", "period": 3.551},
        {"moon": "Ganymede", "period": 7.154},
        {"moon": "Callisto", "period": 16.689},
    ]

    moon_name = input("Enter a jupiter moon: ")
    moon_name = f"{moon_name[0].upper()}{moon_name[1:]}"
    valid_moon = moon_name in moons
    if valid_moon == False:
        print("Invalid moon name")
    for radius in moon_radius:
        if radius["moon"].lower() == moon_name.lower():
            print(f"{radius['moon']} mean radius: {radius['radius']}km")
    
    for gravity in moon_gravity:
        if gravity["moon"].lower() == moon_name.lower():
            print(f"{gravity['moon']} surface gravity: {gravity['gravity']} meters per second squared")
    
    for period in moon_orbital_period:
        if period["moon"].lower() == moon_name.lower():
            print(f"{period['moon']} orbital period: {period['period']} days")

jupiter_moons()