form_of_consumption = input("Delivery or pickup? Delivery is an additional $3 charge. ").lower()
if form_of_consumption == 'delivery':
    print("Delivery it is. $3 will be added to your order total.")
elif form_of_consumption == 'pickup':
    print("Pickup it is.")
else: 
    print("That is not a valid form of consumption.")


number_of_pizzas = int(input("How many pizzas would you like? "))
if number_of_pizzas > 0 and number_of_pizzas <= 5:
    print("You have ordered {} pizzas".format(number_of_pizzas))
elif number_of_pizzas > 5: 
    print("Please input a valid amount of pizzas. You may have a maximum of 5.")
elif number_of_pizzas <= 0:
    print("Please input a valid amount of pizzas. It is not possible to have a negative amount of pizzas. You may have a maximum of 5.")
    


print("""
      1 Pepperoni - $8.50
      2 Beef and Onion - $8.50
      3 Meat Lovers - $8.50
      4 Vegetarian - $8.50
      5 Mozerella - $8.50
      6 Hawaiian - $13.50
      7 Sausage - $13.50
      8 Ham and Cheese - $13.50
      9 Italiano - $13.50
      10 Hot and Spicy - $13.50
      11 Cheese Supreme - $13.50
      12 Chicken Supreme - $13.50
      """)

pizza_type = input("Which type of pizza would you like? ").lower()
if pizza_type == 'pepperoni':
    print("You have ordered {} pepperoni pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
    
elif pizza_type == 'beef and onion':
    print("You have ordered {} beef and onion pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
    
elif pizza_type == 'meat lovers':
    print("You have ordered {} meat lovers pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
    
elif pizza_type == 'vegetarian':
    print("You have ordered {} vegetarian pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
    
elif pizza_type == 'mozerella':
    print("You have ordered {} mozerella pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
    
elif pizza_type == 'hawaiian':
    print("You have ordered {} beef & onion pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
    
elif pizza_type == 'sausage':
    print("You have ordered {} sausage pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
    
elif pizza_type == 'ham and cheese':
    print("You have ordered {} ham and cheese pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
    
elif pizza_type == 'italiano':
    print("You have ordered {} italiano pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
    
elif pizza_type == 'hot and spicy':
    print("You have ordered {} hot and spicy pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
    
elif pizza_type == 'cheese supreme':
    print("You have ordered {} cheese supreme pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
    
elif pizza_type == 'chicken supreme':
    print("You have ordered {} chicken supreme pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
    
else: 
    print("That is not an avaliable type of pizza.")
    
print("""
      1 Pepperoni Slices - $0.50
      2 Olives - $0.50
      3 Capers - $0.50
      4 Anchovies - $0.50
      5 Capsicum - $0.50
      6 More Cheese - $0.50
      7 Mushrooms - $0.50
      8 Sausage Pieces - $0.50
      9 Hot Peppers - $0.50
      10 Pineapple Chunks - $0.50
      11 Red Onion - $0.50
      12 Eggplant - $0.50
      """)

topping = input("Would you like any extra toppings? ").lower()
if topping == 'pepperoni slices':
    print("Extra pepperoni will be added onto the ordered pizza amount.")
    
elif topping == 'olives':
    print("Extra olives will be added onto the ordered pizza amount.")
    
elif topping == 'capers':
    print("Extra capers will be added onto the ordered pizza amount.")
    
elif topping == 'anchovies':
    print("Extra anchovies will be added onto the ordered pizza amount.")
    
elif topping == 'capsicum':
    print("Extra capsicum will be added onto the ordered pizza amount.")
    
elif topping == 'more cheese':
    print("More cheese will be added onto the ordered pizza amount.")
    
elif topping == 'muchrooms':
    print("Extra mushrooms will be added onto the ordered pizza amount.")
    
elif topping == 'sausage pieces':
    print("Extra sausage pieces will be added onto the ordered pizza amount.")
    
elif topping == 'hot peppers':
    print("Extra hot peppers will be added onto the ordered pizza amount.")
    
elif topping == 'pineapple chunks':
    print("Extra pineapple chunks will be added onto the ordered pizza amount.")
    
elif topping == 'red onion':
    print("Extra red onion will be added onto the ordered pizza amount.")
    
elif topping == 'eggplant':
    print("Extra eggplant will be added onto the ordered pizza amount.")

elif topping == 'no' or 'nope' or 'no thanks' or 'nah' or 'none' or 'none please':
    print("No extra toppings will be added to your ordered pizza.")
    
    
else: 
    print("That is not an avaliable topping to add to your pizza amount.")
    
