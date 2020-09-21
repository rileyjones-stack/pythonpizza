number_of_pizzas = int(input("How many pizzas would you like? "))
if number_of_pizzas > 0 and number_of_pizzas <= 5:
    print("You have ordered {} pizzas".format(number_of_pizzas))
elif number_of_pizzas > 5: 
    print("Please input a valid amount of pizzas. You may have a maximum of 5.")
elif number_of_pizzas <= 0:
    print("Please input a valid amount of pizzas. It is not possible to have a negative amount of pizzas. You may have a maximum of 5.")
    


print("""
      1 Pepperoni
      2 Beef & Onion
      3 Meat Lovers
      4 Vegetarian
      5 Mozerella
      6 Hawaiian
      """)

pizza_type = input("Which type of pizza would you like? ").lower()
if pizza_type == 'pepperoni':
    print("You have ordered {} pepperoni pizzas.".format(number_of_pizzas))
    
elif pizza_type == 'beef & onion':
    print("You have ordered {} beef & onion pizzas.".format(number_of_pizzas))
    
elif pizza_type == 'meat lovers':
    print("You have ordered {} meat lovers pizzas.".format(number_of_pizzas))
    
elif pizza_type == 'vegetarian':
    print("You have ordered {} vegetarian pizzas.".format(number_of_pizzas))
    
elif pizza_type == 'mozerella':
    print("You have ordered {} mozerella pizzas.".format(number_of_pizzas))
    
elif pizza_type == 'hawaiian':
    print("You have ordered {} beef & onion pizzas.".format(number_of_pizzas))
else: 
    print("That is not an avaliable type of pizza.")