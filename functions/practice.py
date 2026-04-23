year = int(input("Enter a year: "))
month = int(input("Enter a month (1-12): "))
space = ["0", "31", "28","31", "30", "31", "30", "31", "31", "30", "31", "30", "31"]
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def days_in_month(year, month):
    if month < 1 or month > 12:
        return print("Invalid month. Please enter a number between 1 and 12.")
    if month == 2 and is_leap_year(year):
        return print(f"the number of days in year {year} in month {month} is 29")
    return print(f"the number of days in year {year} in month {month} is {space[month]}")
days_in_month(year, month)

# this is a dynamic function that checks user input to give the no of days in month by checking a leap year and return the result