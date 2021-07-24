email = input("Enter your email address : ")

# Valid email john@gmail.com
# Invalid email john@gmail

if email != "":
    # check if the email address have a @ character
    if email.count("@") == 1:
        index_atsign = email.find("@") # this will return the index (position) or -1
        dot = email.find(".", index_atsign)
        if dot != -1:
            print("Email is valid")
        else:
            print("Email is not valid")
    else:
        print("Email is not valid")
else:
    print('Please enter an email address')