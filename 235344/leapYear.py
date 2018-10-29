# -*-coding:utf-8 -*

# A leap year is a multiple of 4, unless if it is a multiple of 100
# However, it is considered as a leay year if it is a multiple of 400

# Type the year
year = input("choose a year : ")

try :
    # Convert it into integer
    year = int(year)
    if year < 0 :
        raise ValueError("Year must be great than 0")

    # Code
    if year % 400 == 0 or (year % 4  == 0 and year % 100 != 0):
        print(year,'is a leap year')
    else:
        print(year, "is not a leap year" )

except ValueError as err :
    print("############  error converting to year", err)

except AssertionError as ass :
    print("year less than 0", ass)

else :
    print(" réussie")

finally :
    print("------------ le plus têtu -----------")

