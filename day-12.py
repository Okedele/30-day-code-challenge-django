# Exception Handling
try:
    f = open('random_number_file.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("Reading file.....")
    print(f.read())
    f.close()
finally:
    print("Process completed")
