# Functions go here
def statement_generator (statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
Instructions.
- Enter a valid metric unit and press <enter> to confirm
- Enter a second valid metric unit and press <enter>
- Enter a number
- Press enter to terminate the program else press any letter
  then <enter> to continue
''')


# checks users enter a valid unit (does not check domain)
def check_unit(question, to_check):

    while True:

        response = input(question).lower()

        # iterate through each mini-list and see if our response is in them
        for item in to_check:
            if response in item:

                # return the first item in the mini-list
                return item[0]

        print("Houston we have a problem..."
              "that's not a valid unit")


def number_checker(question):
    error = f"Please enter a whole number\n"
    while True:

        # ask the user for a integer
        response = input(question)

        # xxx break code
        if response == "xxx":
            return response

        try:
            if float(response) > 0:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


def format_number(number):
    # Format the number with a precision that avoids trailing zeros
    return f"{number:.10g}"


# Main routine goes here

# Title
statement_generator("Cameron's Awesome Ultimate Conversion Calculator", "*")

# Display instructions if requested
print()
want_instructions = input("Press <enter> to read the instructions or any key to continue ")


if want_instructions == "":
    instructions()

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

while True:
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

    # get 'to' unit from user and check that it's valid
    # ie: it is in the same domain as the 'from' unit

    while True:

        # checks domain, repeats question if it's not OK
        # domain_ok = "yes"

        to_unit = check_unit("Unit that you want to convert to: ", unit_all)

        if to_unit in domain_check:
            break

        else:
            print(f"\nOops - {from_unit} is not in the same domain as {to_unit}")

    # gets the value of the unit and checks that and is more than zero.
    value = number_checker("Value: ")

    multiplier = domain_check[from_unit]
    standard = float(value) * multiplier

    divide_by = domain_check[to_unit]
    answer = format_number(standard / divide_by)

    print(f"{answer} {to_unit}"
          f"\nie: {value}{from_unit} is {answer}{to_unit}")

    # stop the program if wanted
    stop = input("\nPress <enter> to continue, or any key to stop: ")
    if stop != "":
        break
