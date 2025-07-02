def is_leap(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print("Please enter the year:")
year = int(input())
leap: bool = is_leap(year)

if leap:
    print("The year is a leap year")
else:
    print("The year is not a leap year") 