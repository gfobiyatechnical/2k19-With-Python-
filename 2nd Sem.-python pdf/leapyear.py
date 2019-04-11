def is_leap(year):
    if 1900<= year <= (10**5) :
        if year%4 != 0:
            print(bool(0))

year = int(input("Enter Any Year..."))
is_leap(year)

