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
    
special_or_basic = input("Would you like a special, more expensive type of pizza, or one of our basic pizza options? ").lower()

if special_or_basic == 'special':
    print("The special pizzas are $13.50 each. Please choose one type from our menu.")
    print("""
      6 Hawaiian - $13.50
      7 Sausage - $13.50
      8 Ham and Cheese - $13.50
      9 Italiano - $13.50
      10 Hot and Spicy - $13.50
      11 Cheese Supreme - $13.50
      12 Chicken Supreme - $13.50
    
    """)
    pizza_special = input("Which type of special pizza would you like? ").lower()
    if pizza_special == 'hawaiian':
        print("You have ordered {} hawaiian pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
        
    elif pizza_special == 'sausage':
        print("You have ordered {} sausage pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
    
    elif pizza_special == 'ham and cheese':
        print("You have ordered {} ham and cheese pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
    
    elif pizza_special == 'italiano':
        print("You have ordered {} italiano pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
    
    elif pizza_special == 'hot and spicy':
        print("You have ordered {} hot and spicy pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
    
    elif pizza_special == 'cheese supreme':
        print("You have ordered {} cheese supreme pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
    
    elif pizza_special == 'chicken supreme':
        print("You have ordered {} chicken supreme pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
    
    else: 
        print("That is not an avaliable type of pizza.")
    

    
elif special_or_basic == 'basic':
    print("The basic pizzas are $8.50 each. Please choose one type from our menu.")
    print("""
      1 Pepperoni - $8.50
      2 Beef and Onion - $8.50
      3 Meat Lovers - $8.50
      4 Vegetarian - $8.50
      5 Mozerella - $8.50
          """)
    pizza_basic = input("Which type of basic pizza would you like? ").lower()
    if pizza_basic == 'pepperoni':
        print("You have ordered {} pepperoni pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
        
    elif pizza_basic == 'beef and onion' or 'beef & onion':
        print("You have ordered {} beef and onion pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
        
    elif pizza_basic == 'meat lovers':
        print("You have ordered {} meat lovers pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
        
    elif pizza_basic == 'vegetarian':
        print("You have ordered {} vegetarian pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
        
    elif pizza_basic == 'mozerella':
        print("You have ordered {} mozerella pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
       

    
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

if special_or_basic == 'special':
    total_cost = number_of_pizzas * 13.50
    print("The total cost of your order is {}".format(total_cost))
    
elif special_or_basic == 'basic':
    total_cost = number_of_pizzas * 8.50
    print("The total cost of your order is {}".format(total_cost))
        

#print("The total cost of your order is {}".format{n})"""
    
