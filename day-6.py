# RESTAURANT SELECTOR
vegetarian = input("Is anyone in your party a vegetarian? ").lower()
vegan = input("Is anyone in your party a vegan? ").lower()
gluten_free = input("Is anyone in your party gluten-free? ").lower()
restaurant = ""

if (vegetarian == "yes" and vegan == "yes" and gluten_free == "yes"):
    restaurant = "Corner Café\nThe Chef’s Kitchen"
elif (vegetarian == "no" and vegan == "no" and gluten_free == "no"):
    restaurant = "Joe’s Gourmet Burgers\nCorner Café\nThe Chef’s Kitchen"
elif (vegetarian == "yes" and vegan == "no" and gluten_free == "yes"):
    restaurant = "Main Street Pizza Company\nCorner Café\nThe Chef’s Kitchen"
elif (vegetarian == "yes" and vegan == "no" and gluten_free == "no"):
    restaurant = "Mama’s Fine Italian\nCorner Café\nThe Chef’s Kitchen"

print(f"Here are your restaurant choices:\n{restaurant}")
