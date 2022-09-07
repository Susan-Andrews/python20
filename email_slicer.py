# collect email from user
# split the email using the  @ ,save the first part as user name and second part as domain name
# split domain using the .



def main():
    print("WELCOME TO EMAIL SLICER")
    print("") # blank space

    emailinput=input("Enter your email: ")

    (username,domain)=emailinput.split("@")
    (domain,extension)=domain.split(".")

    print("Username :",username)
    print("Domain :",domain)
    print("Extension :",extension)
while True:
    main()
