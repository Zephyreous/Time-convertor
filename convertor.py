# Base time values
minute = 60
hour = minute * 60
day = hour * 24
week = day * 7
month = int(day * 30)
year = int(day * 365)

# Conversion functions
def days_to_hours(n):
    return f"{n} days are {n * 24} hours."

def hours_to_minutes(n):
    return f"{n} hours are {n * 60} minutes."

def minutes_to_seconds(n):
    return f"{n} minutes are {n * 60} seconds."

def days_to_weeks(n):
    return f"{n} days are {n / 7:.2f} weeks."

def weeks_to_months(n):
    return f"{n} weeks are {n / 4:.2f} months."

def months_to_years(n):
    return f"{n} months are {n / 12:.2f} years."

# Main logic
def validate_and_execute(option, number):
    try:
        number = int(number)
        if number < 0:
            print("Negative numbers are not allowed.")
            return

        if option == "1":
            print(days_to_hours(number))
        elif option == "2":
            print(hours_to_minutes(number))
        elif option == "3":
            print(minutes_to_seconds(number))
        elif option == "4":
            print(days_to_weeks(number))
        elif option == "5":
            print(weeks_to_months(number))
        elif option == "6":
            print(months_to_years(number))
        else:
            print("Invalid option selected.")

    except ValueError:
        print("Invalid number input. Please enter a valid integer.")

# Main loop
while True:
    print("\n--- TIME CONVERSION MENU ---")
    print("1. Days to Hours")
    print("2. Hours to Minutes")
    print("3. Minutes to Seconds")
    print("4. Days to Weeks")
    print("5. Weeks to Months")
    print("6. Months to Years")
    print("Type 'exit' to quit.\n")

    option = input("Select a conversion option: ")
    if option.lower() == "exit":
        print("Goodbye!")
        break

    number = input("Enter the number to convert: ")
    validate_and_execute(option, number)