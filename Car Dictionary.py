## Assignment: Week 2 Module 2 Critical Thinking
## Option: Option 2



from collections import OrderedDict
# Empty dictionary
dictionary = OrderedDict()

# Functions to get the car brand, model, year, starting odometer, ending odometer, and miles per gallon.
def brand():
    key = "brand: "
    value = str(input("Enter car brand: "))
    dictionary[key] = value
def model():
    key = "model: "
    value = str(input("Enter car model: "))
    dictionary[key] = value
def year():
    key = "year: "
    value = int(input("Enter car year: "))
    dictionary[key] = value
def starting_odometer():
    key = "starting odometer: "
    value = int(input("Enter car starting odometer: "))
    dictionary[key] = value
def ending_odometer():
    key = "ending odometer: "
    value = int(input("Enter car ending odometer: "))
    dictionary[key] = value
def estimated_miles_per_gallon():
    key = "miles/gallon: "
    value = int(input("Enter estimated miles per gallon: "))
    dictionary[key] = value

# Call the functions
brand()
model()
year()
starting_odometer()
ending_odometer()
estimated_miles_per_gallon()

# Print the dictionary
print("\nThe Dictionary:")
for key, value in dictionary.items():
    print(key, value)
