number_of_pizzas = int(input("How many pizzas would you like? "))
if number_of_pizzas > 0 and number_of_pizzas <= 5:
    print("You have ordered {} pizzas".format(number_of_pizzas))
elif number_of_pizzas > 5: 
    print("Please input a valid amount of pizzas. You may have a maximum of 5.")
elif number_of_pizzas <= 0:
    print("Please input a valid amount of pizzas. It is not possible to have a negative amount of pizzas. You may have a maximum of 5.")
    