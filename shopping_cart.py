import math

print("Welcome to the Healthy Food Shop")
fives = 5
dollars = 1
nickels = dollars * 0.05
dimes = dollars * .1
quarters = dollars * .25
pennies = dollars*0.01

i = 1

potatoes = int(input("Please enter how many potatoes you would like to buy ($0.75 per potatoes):"))
tomatoes = int(input("Please enter how many tomatoes you would like to buy ($1.25 per tomato):"))
apples = int(input("Please enter how many apples you would like to buy ($0.50 per apple):"))
mangos = int(input("Please enter how many mangoes you would like to buy ($1.75 per mango):"))

while i > 0:
    total = (p_price*potatoes) + (t_price*tomatoes) + (a_price*apples) + (m_price*mangos)
    print("The total comes out to: $" + str(total))
    user_amount = float(input("How much will it be out of ? "))
    if total>user_amount:
        more = float(input("Add more money"))
        total = total + more
    if total == user_amount:
        print("Thank you for shopping with us :) have a great day!")
    elif total < user_amount:
        remaining = user_amount - total
        print("Your change is:", format(remaining,'.2f'),sep='')

    if remaining>= fives:
        five = int(remaining//fives)
        remaining-=(five*fives)
        print("Fives:", five)
    else:
        print("Fives: 0")

    if remaining>=dollars:
        ones = int(remaining//dollars)
        remaining-=(ones*dollars)
        print("Ones: ", ones)
    else:
        print("Dollars: 0")

    if remaining>= quarters:
        quarter = int(remaining//quarters)
        remaining-=(quarter*quarters)
        print("Quarters: ", quarter)
    else:
        print("Quarters: 0")

    if remaining>= dimes:
        dime = int(remaining//dimes)
        remaining-=(dime*dimes)
        remaining = round(remaining,2)
        print("Dimes: ", dime)
    else:
        print("Dimes: 0")

    if remaining>=nickels:
        nickel = int(remaining//nickels)
        remaining-=(nickel*nickels)
        remaining = round(remaining,2)
        print("Nickels: ", nickel)
    else:
        print("Nickels: 0")

    if remaining>=pennies:
        penny = int(remaining//pennies)
        remaining-=(penny*pennies)
        print("Pennies: ", penny)
    else:
        print("Pennies: 0")
    i-=1
