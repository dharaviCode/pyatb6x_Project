def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

input_year = check_leap_year(int(input("Enter year: ")))
print(input_year)