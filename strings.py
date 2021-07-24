# create a string
"This is a string"

'This is also a  string'

'i can\'t do this' # escape using the backslash

"This is a nice quote \"to be or not to be\""

email = "john@gmail.com"

full_name = "john doe"
city = "JAKARTA"

# make it upper case
print(full_name.upper())    
print(city.lower())
print(full_name.title())

# index: the position of an object inside something
print(full_name[0])
print(full_name[2])

# exercise, print out the last letter in variable full name
print(full_name[-1]) # -1 will count the index from the back
print(full_name[len(full_name)-1]) # never use a hardcoded value for example print(full_name[7])

# to find characters
print('---')
print(full_name.find('doe'))

print(full_name.count('o'))

# check if a string starts with something
# this method return boolean (True or False)
print(full_name.lower().startswith("john"))
print(full_name.endswith("e"))

password = "password"
print(password.isalpha()) # checks if the string is alphabetical
print(password.isnumeric()) # checks if the string is numerical
print(password.isalnum()) # checks if the string is alphabetical and numerical

username = " vacha ar "
print(len(username))
clean_username = username.strip() # this will remove leading and trailing empty spaces
print(len(clean_username))

website = "http://google.com"

print(website.index('h')) # find the character and return the index or error if not found
print(website.find('x')) # find the character and return the index or -1 if not found
