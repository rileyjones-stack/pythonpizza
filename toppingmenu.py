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

pizza_type = input("Would you like any extra toppings? ").lower()
if pizza_type == 'pepperoni slices':
    print("Extra pepperoni will be added onto the ordered pizza.")
    
elif pizza_type == 'olives':
    print("Extra olives will be added onto the ordered pizza.")
    
elif pizza_type == 'capers':
    print("Extra capers will be added onto the ordered pizza.")
    
elif pizza_type == 'anchovies':
    print("Extra anchovies will be added onto the ordered pizza.")
    
elif pizza_type == 'capsicum':
    print("Extra capsicum will be added onto the ordered pizza.")
    
elif pizza_type == 'more cheese':
    print("More cheese will be added onto the ordered pizza.")
    
elif pizza_type == 'muchrooms':
    print("Extra mushrooms will be added onto the ordered pizza.")
    
elif pizza_type == 'sausage pieces':
    print("Extra sausage pieces will be added onto the ordered pizza.")
    
elif pizza_type == 'hot peppers':
    print("Extra hot peppers will be added onto the ordered pizza.")
    
elif pizza_type == 'pineapple chunks':
    print("Extra pineapple chunks will be added onto the ordered pizza.")
    
elif pizza_type == 'red onion':
    print("Extra red onion will be added onto the ordered pizza.")
    
elif pizza_type == 'eggplant':
    print("Extra eggplant will be added onto the ordered pizza.")
    
else: 
    print("That is not an avaliable topping to add to your pizza.")