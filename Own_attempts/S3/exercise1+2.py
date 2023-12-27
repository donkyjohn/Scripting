#~/bin/python3
givenlist = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]   
print("Given list: {}".format(givenlist))
even_list = [number for number in givenlist if number % 2 == 0] 
print("Even list: ",even_list)

birthyears = [1990, 1995, 1990, 1991, 1992, 1991]
print("\nYears of birth: {}".format(birthyears))
ages = [2020 - year for year in birthyears]
print("Ages: {}".format(ages))

day = int(input("What day were u born?:"))
month = str(input("What month were u born?:"))
if month == "January" or month == "jan" or month == "Jan" and day >= 20:
    print("Aquarius")
elif month == "February" or month == 'feb' or month == "Feb" and day <= 18:
    print("Aquarius")
elif month == "February" or month == 'feb' or month == "Feb" and day >= 19:
    print("Pisces")
elif month == "March" and day <= 20:
    print("Pisces")
elif month == "March" and day >= 21:
    print("Aries")
elif month == "April" and day <= 19:
    print("Aries")
elif month == "April" and day >= 20:
    print("Taurus")
elif month == "May" and day <= 20:
    print("Taurus")
elif month == "May" and day >= 21:
    print("Gemini")
elif month == "June" and day <= 20:
    print("Gemini")
elif month == "June" and day >= 21:
    print("Cancer")
elif month == "July" and day <= 22:
    print("Cancer")
elif month == "July" and day >= 23:
    print("Leo")
elif month == "August" and day <= 22:
    print("Leo")
elif month == "August" and day >= 23:
    print("Virgo")
elif month == "September" and day <= 22:
    print("Virgo")
elif month == "September" and day >= 23:
    print("Libra")
elif month == "October" and day <= 22:
    print("Libra")
elif month == "October" and day >= 23:
    print("Scorpio")
elif month == "November" and day <= 21:
    print("Scorpio")
elif month == "November" and day >= 22:
    print("Sagittarius")
elif month == "December" and day <= 21:
    print("Sagittarius")
elif month == "December" and day >= 22:
    print("Capricorn")
elif month == "January" and day <= 19:
    print("Capricorn")
else:
    print("Invalid input")

#################################################################################
