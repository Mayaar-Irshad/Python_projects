#
# this program calculates if a year is leap year or not.
# leap year has 366 day
# normal year has 365 days

year = int(input("Which year do you want to check for leap years? "))

if year % 4 == 0:
    if year % 100 != 0:
        print(f"so the year {year} is a leap year")
    else:
        if year % 400 == 0:
            print(f"so the year {year} is a leap year")

else:
    print(f"the year {year} is not a leap year")
