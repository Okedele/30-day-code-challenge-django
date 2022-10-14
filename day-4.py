# NAME DISPLAY
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")


print(f"Initials: {first_name[0].upper()}.{last_name[0].upper()} \nName: {first_name[0].upper()}{first_name[1:]} {last_name.upper()} \nUsername: {first_name[0].lower()}{last_name.lower()}")

# ALPHABETIC TELEPHONE NUMBER TRANSLATOR
telephone_number = input("Enter your telephone number in the format XXX-XXX-XXXX: ")
telephone_number = telephone_number.lower()
for i in telephone_number:
    if (i == 'a' or i == 'b' or i == 'c'):
        telephone_number = telephone_number.replace(i, '2')
    elif (i == 'd' or i == 'e' or i == 'f'):
        telephone_number = telephone_number.replace(i, '3')
    elif (i == 'g' or i == 'h' or i == 'i'):
        telephone_number = telephone_number.replace(i, '4')
    elif (i == 'j' or i == 'k' or i == 'l'):
        telephone_number = telephone_number.replace(i, '5')
    elif (i == 'm' or i == 'n' or i == 'o'):
        telephone_number = telephone_number.replace(i, '6')
    elif (i == 'p' or i == 'q' or i == 'r' or i == 's'):
        telephone_number = telephone_number.replace(i, '7')
    elif (i == 't' or i == 'u' or i == 'v'):
        telephone_number = telephone_number.replace(i, '8')
    elif (i == 'w' or i == 'x' or i == 'y' or i == 'z'):
        telephone_number = telephone_number.replace(i, '9')
print(f"Your telephone number is {telephone_number}")