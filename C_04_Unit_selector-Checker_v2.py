# Valid units

# checks users enter a valid unit (does not check domain)
def check_unit(question, to_check):

    while True:

        response = input(question).lower()

        # iterate through each mini-list and see if our response is in them
        for item in to_check:
            if response in item:

                # return the first item in the mini-list
                return item[0]

        print("Houston we have a problem...")


# Lists used to check users enter a unit of mass
valid_tonne = ['t', 'tonne', 'tonnes']
valid_kg = ['kg', 'kilogram', 'kilograms']
valid_g = ['g', 'gram', 'grams']
valid_mg = ['mg', 'milligram', 'milligrams']

# Valid time units
valid_seconds = ['sec', 's', 'second', 'seconds']
valid_min = ['min', 'minute', 'minutes']
valid_hr = ['hr', 'hrs', 'hour', 'hours']

# Valid distance units
valid_km = ['km', 'kilometer', 'kilometers']
valid_m = ['m', 'meter', 'meters']
valid_cm = ['cm', 'centimeter', 'centimeters']
valid_mm = ['mm', 'millimeter', 'millimeters']

# Valid volume units
valid_l = ['l', 'litre', 'litres']
valid_ml = ['ml', 'millilitre', 'millilitres']

# combine 'domain' lists so that we can check users are converting
# within a domain (eg: can't convert kilograms to seconds)
mass_all = [valid_g, valid_mg, valid_kg, valid_tonne]
time_all = [valid_hr, valid_min, valid_seconds]
distance_all = [valid_mm, valid_cm, valid_m, valid_km]
volume_all = [valid_l, valid_ml]

unit_all = volume_all + distance_all + mass_all + time_all

# dictionaries for checking domains and doing calculations
mass_dict = {
    "mg": 0.001,
    "g": 1,
    "kg": 1000,
    "t": 1000000,
}

distance_dict = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
}

volume_dict = {
    "ml": 0.001,
    "l": 1,
}

time_dict = {

    "sec": 1,
    "min": 60,
    "hr": 3600,
}


valid_ans = []
ask_unit = ""

# adding all lists into one master list
for item in unit_all:
    valid_ans += item

# Ask a question and lowercase the answer
from_unit = check_unit("Unit that you want to convert from: ", unit_all)


# figure out if we are working with mass / volume / time or distance
if from_unit in mass_dict:
    domain_check = mass_dict

elif from_unit in volume_dict:
    domain_check = volume_dict

elif from_unit in time_dict:
    domain_check = time_dict

else:
    domain_check = distance_dict

while True:

    domain_ok = "yes"

    to_unit = check_unit("Unit that you want to convert to: ", unit_all)

    if to_unit in domain_check:
        print("hi")
        break
    else:
        print(f"Oops - {from_unit} is not in the same domain as {to_unit}")

# print(f"You chose {ask_unit}")
