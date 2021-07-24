paid = False
age = 14

# movie for 13+
if age > 13 and paid == True:
    print("You can watch the movie")
else:
    print("You can't watch the movie")

# movie for 13+
if age > 13 or paid == True:
    print("You can watch the movie")
else:
    print("You can't watch the movie")


