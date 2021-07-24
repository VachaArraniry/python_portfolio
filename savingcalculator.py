monthly_income = input("enter your monthly income : ")
saving_percentage = input("how many percent are you willing to save? : ")
product = input("what are you planning to buy : ")
product_price = input("enter the price of the {0} : ".format(product))

saving_amount = 0


def saving_amount_calculation(income, percentage):
    return income * (percentage / 100)

def length_saving(price, saving_amount):
    return price / saving_amount

if monthly_income:
    saving_amount = saving_amount_calculation(int(monthly_income), int(saving_percentage))
    length = length_saving(int(product_price), saving_amount)
    print("You need to save money for {0} months".format(round(length)))
