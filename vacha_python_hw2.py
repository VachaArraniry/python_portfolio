# ask user for his/her full name
# print to console "Hello Jack Bauber, how are you"
# print to console "Your name has 10 characters"
# print to console "Your name starts with J"

full_name = input("Enter your full name : ")
clean_full_name = full_name.strip()

print("Hello {0} {1}".format(full_name.title(), "how are you"))
print("Your name has {0} {1}".format(len(clean_full_name), "characters"))
print("Your name starts with {0}".format(full_name[0].title()))