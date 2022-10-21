def main():
    print("This program converts US dollars to Pounds Sterling")
    print()


    dollars=eval(input("enter the amount in dollars:"))

    pounds=convert_to_pounds(dollars)

    print("That is" , pounds, "pounds.")

convert_to_pounds=lambda dollars: dollars * 0.82    
main()