# Dictionary for unit order
my_dict = {
    "sec": 1,
    "min": 2,
    "hr": 3,
}

# Ask user for units
unit_current = input("Current unit (sec, min, hr): ")
unit_wanted = input("Wanted unit (sec, min, hr): ")

# Replace statement below with call to number checker
value = float(input("Value: "))

# Make the Conversion
if unit_wanted and unit_current in my_dict:

    # Converting up
    if my_dict[unit_wanted] > my_dict[unit_current]:

        multiplier = 60 / (my_dict[unit_wanted] - my_dict[unit_current])
        answer = value / multiplier

    # Converting down
    else:

        multiplier = 60 / (my_dict[unit_current] - my_dict[unit_wanted])
        answer = value * multiplier
