# Dictionary for unit order
time_dict = {
    "sec": 1,
    "min": 60,
    "hr": 3600,
}

# Ask user for units
unit_current = input("Current unit (sec, min, hr): ")
unit_wanted = input("Wanted unit (sec, min, hr): ")

# Replace statement below with call to number checker
value = float(input("Value: "))

multiplier = time_dict[unit_current]
standard = value * multiplier

divide_by = time_dict[unit_wanted]
answer = standard / divide_by

print(answer)