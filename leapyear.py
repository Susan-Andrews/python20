def is_leap_year(year):
    if year %4 == 0:
        if year %100 == 0:
            if year %400 == 0:
                print("Leap year")
            else:
                print("Not a leap Year")
        else:
            print("Leap Year")
    else:
        print("Not a leap year")


is_leap_year(2024)                            



#What is a Leap Year? It takes approximately 365.25 days for our planet Earth to orbit the Sun — that is a solar year. We usually round the days in a calendar year to 365, that is 365 days in a year. To make up for the missing partial day, we add one day to our calendar approximately every four years and that is known as a leap year.
