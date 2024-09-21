# ASSIGNMNET calendar
num_days = int(input("Enter the number of days in the month: "))
start_day = input(
    "Enter the starting day of the month (Sun, Mon, Tue, Wed, Thu, Fri, Sat): ")


def print_month_days(num_days, start_day):
    # Days of the week
    days_of_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    print(" ".join(days_of_week))

    start_pos = days_of_week.index(start_day)

    # Fill in with empty spaces for the starting day
    calendar = ["   "] * start_pos

    for day in range(1, num_days + 1):
        # {day:3} is a formating type it adds three spaces
        calendar.append(f"{day:3} ")

    for i in range(0, len(calendar), 7):  # HERE 7 is the iteration increament
        print("".join(calendar[i: i+7]))


print_month_days(num_days, start_day)
