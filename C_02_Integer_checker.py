def number_checker(question):
    error = f"Please enter a whole number\n"
    while True:

        # ask the user for a integer
        response = input(question)

        # xxx break code
        if response == "xxx":
            return response

        if float(response):
            return response

        else:
            print(error)


# main routine goes here
error = "please enter a number"
while True:
    try:
        number = number_checker("Number: ")
        if number == "xxx":
            break
        elif float(number):
            print(number)
        else:
            print(error)
    except ValueError:
        print(error)
