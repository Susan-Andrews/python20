# collect thenecessary inputs(principal,apr,years)
# calculate monthly payment
# display to user

def main():
    print("This is a monthly loan calculator")
    print("")

    principal=float(input("Input the loan amount:"))
    apr=float(input("Input the annual intrest rate:"))
    years=int(input("Input thew amount of years:"))

    montly_intrest_rate=apr/1200
    amount_of_months=years*12
    montly_payment=principal*montly_intrest_rate/ (1-(1+montly_intrest_rate)**(-amount_of_months))

    print("The montly payment for this loan is:%.2f" %montly_payment)

main()
