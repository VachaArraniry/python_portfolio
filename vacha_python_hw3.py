# print the even numbers between 37 and 99
# use range function to have the list of numbers between 37-99
  
start, end = [37, 99]

for num in range(start + 1, end):
   if num % 2 == 0:
      print("List of even numbers : {0}".format(num))

for x in range(37, 100):
    print("List of all the numbers : {0}".format(x))