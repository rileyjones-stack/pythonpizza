# defines the function which will allow the code to restart if the user requests to do so
def main():
    print("Welcome to Henderson Pizza Place! Please start your order by typing your name. ")
    # asks for the users name and stores this information for later statements
    name = input("What is your name? ")

    form_of_consumption = input("Delivery or pickup? Delivery is an additional $3 charge. ").lower()
    # While loop - prints different input questions for 'pickup' and 'delivery'. 
    # if the user enters false input then loop will occur    
    while True: 
        if form_of_consumption == 'pickup':
            print("pickup it is.")
            phone_number = input("What is your phone number? ")
            break
        if form_of_consumption == 'delivery':
            # Ask the user for their address, since the user chose delivery
            address = input("What is your address or desired delivery location? ")
            phone_number = input("What is your phone number? ")
            break
        else:
            print("That is not a valid form of consumption. ")
            form_of_consumption = input("Delivery or pickup? Delivery is an additional $3 charge. ").lower()
            
        

    # Asks the user how many pizzas they would like from 1-5, and code loops if number is invalid
    number_of_pizzas = int(input("How many pizzas would you like? You may order a maximum of 5. "))
    if number_of_pizzas > 0 and number_of_pizzas <= 5:
        print("You have ordered {} pizzas".format(number_of_pizzas))
    # if the number of pizzas is above the maximum of five, it will repeat the question    
    elif number_of_pizzas > 5: 
        print("Please input a valid amount of pizzas. You may have a maximum of 5.")
        number_of_pizzas = int(input("How many pizzas would you like? You may order a maximum of 5. "))
    # if the number of pizzas is below the minimum of 1, it will repeat the question   
    elif number_of_pizzas <= 0:
        print("Please input a valid amount of pizzas. It is not possible to have a negative amount of pizzas. You may have a maximum of 5.")
        number_of_pizzas = int(input("How many pizzas would you like? You may order a maximum of 5. "))
        
    special_or_basic = input("Would you like a special, more expensive type of pizza, or one of our basic pizza options? ").lower() 
    while True:  
        
        if special_or_basic == 'special':
            
            # Prints a menu display for the user to choose from
            print("The special pizzas are $13.50 each. Please choose one type from our menu.")
            print("""
        
              1 Hawaiian - $13.50
              2 Sausage - $13.50
              3 Ham and Cheese - $13.50
              4 Italiano - $13.50
              5 Hot and Spicy - $13.50
              6 Cheese Supreme - $13.50
              7 Chicken Supreme - $13.50
        
            """)
        
            pizza_special = input("Which type of special pizza would you like? ").lower()
            while True:
                if pizza_special == 'hawaiian' or pizza_special == '1':
                    print("You have ordered {} hawaiian pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
                    break # Breaks out to the next part of code to prevent an infinite while loop
            
                elif pizza_special == 'sausage' or pizza_special == '2':
                    print("You have ordered {} sausage pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
                    break # Breaks out to the next part of code to prevent an infinite while loop
        
                elif pizza_special == 'ham and cheese' or pizza_special == '3':
                    print("You have ordered {} ham and cheese pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
                    break # Breaks out to the next part of code to prevent an infinite while loop
        
                elif pizza_special == 'italiano' or pizza_special == '4':
                    print("You have ordered {} italiano pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
                    break # Breaks out to the next part of code to prevent an infinite while loop
        
                elif pizza_special == 'hot and spicy' or pizza_special == '5':
                    print("You have ordered {} hot and spicy pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
                    break # Breaks out to the next part of code to prevent an infinite while loop
        
                elif pizza_special == 'cheese supreme' or pizza_special == '6':
                    print("You have ordered {} cheese supreme pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
                    break # Breaks out to the next part of code to prevent an infinite while loop
        
                elif pizza_special == 'chicken supreme' or pizza_special == '7':
                    print("You have ordered {} chicken supreme pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
                    break # Breaks out to the next part of code to prevent an infinite while loop
        
                else: 
                    print("That is not an available type of pizza.")
                    pizza_special = input("Which type of special pizza would you like? ").lower()
        

        
        elif special_or_basic == 'basic':
            # States the cost of basic pizza and displays menu
            print("The basic pizzas are $8.50 each. Please choose one type from our menu.")
            print("""
        
              1 Pepperoni - $8.50
              2 Beef and Onion - $8.50
              3 Meat Lovers - $8.50
              4 Vegetarian - $8.50
              5 Mozerella - $8.50
          
                  """)
        
            pizza_basic = input("Which type of basic pizza would you like? ").lower()
            while True:
                
                
                if pizza_basic == 'pepperoni' or pizza_basic == '1':
                    print("You have ordered {} pepperoni pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
                    break # Breaks out to the next part of code to prevent an infinite while loop
                
                    
                elif pizza_basic == 'beef and onion' or pizza_basic == '2':
                    print("You have ordered {} beef and onion pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
                    break # Breaks out to the next part of code to prevent an infinite while loop
            
                elif pizza_basic == 'meat lovers' or pizza_basic == '3':
                    print("You have ordered {} meat lovers pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
                    break # Breaks out to the next part of code to prevent an infinite while loop
            
                elif pizza_basic == 'vegetarian' or pizza_basic == '4':
                    print("You have ordered {} vegetarian pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
                    break # Breaks out to the next part of code to prevent an infinite while loop
            
                elif pizza_basic == 'mozerella' or pizza_basic == '5':
                    print("You have ordered {} mozerella pizzas. You have also chosen {}.".format(number_of_pizzas, form_of_consumption))
                    break # Breaks out to the next part of code to prevent an infinite while loop
                
                else: 
                    print("That is not an available type of pizza.")
                    pizza_basic = input("Which type of basic pizza would you like? ").lower()
                    
                

        else:
            print("Please select a valid type of pizza.")
            special_or_basic = input("Would you like a special, more expensive type of pizza, or one of our basic pizza options? ").lower()
            continue # Loop continues until input is correct, and if it is then the loop will break
        break
        

        
    # Ask the user if they would like any extra toppings
    topping_ask = input("Would you like any extra toppings on your pizza? yes or no. ").lower()

    if topping_ask == 'yes':
        # Displays a toppings menu for the user to choose from
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

        topping = input("What extra toppings would you like? ").lower()
        while True:
            if topping == 'pepperoni slices' or topping == '1':
                print("Extra pepperoni will be added onto the ordered pizza amount.")
                break # Breaks out to the next part of code to prevent an infinite while loop
        
            elif topping == 'olives' or topping == '2':
                print("Extra olives will be added onto the ordered pizza amount.")
                break # Breaks out to the next part of code to prevent an infinite while loop
        
            elif topping == 'capers' or topping == '3':
                print("Extra capers will be added onto the ordered pizza amount.")
                break # Breaks out to the next part of code to prevent an infinite while loop
        
            elif topping == 'anchovies' or topping == '4':
                print("Extra anchovies will be added onto the ordered pizza amount.")
                break # Breaks out to the next part of code to prevent an infinite while loop
        
            elif topping == 'capsicum' or topping == '5':
                print("Extra capsicum will be added onto the ordered pizza amount.")
                break # Breaks out to the next part of code to prevent an infinite while loop
        
            elif topping == 'more cheese' or topping == '6':
                print("More cheese will be added onto the ordered pizza amount.")
                break # Breaks out to the next part of code to prevent an infinite while loop
        
            elif topping == 'mushrooms' or topping == '7':
                print("Extra mushrooms will be added onto the ordered pizza amount.")
                break # Breaks out to the next part of code to prevent an infinite while loop
        
            elif topping == 'sausage pieces' or topping == '8':
                print("Extra sausage pieces will be added onto the ordered pizza amount.")
                break # Breaks out to the next part of code to prevent an infinite while loop
        
            elif topping == 'hot peppers' or topping == '9':
                print("Extra hot peppers will be added onto the ordered pizza amount.")
                break # Breaks out to the next part of code to prevent an infinite while loop
        
            elif topping == 'pineapple chunks' or topping == '10':
                print("Extra pineapple chunks will be added onto the ordered pizza amount.")
                break # Breaks out to the next part of code to prevent an infinite while loop
        
            elif topping == 'red onion' or topping == '11':
                print("Extra red onion will be added onto the ordered pizza amount.")
                break # Breaks out to the next part of code to prevent an infinite while loop
        
            elif topping == 'eggplant' or topping == '12':
                print("Extra eggplant will be added onto the ordered pizza amount.")
                break # Breaks out to the next part of code to prevent an infinite while loop
                 
        
            else: 
                print("That is not an available topping to add to your ordered pizza amount.")
                topping = input("What extra toppings would you like? ").lower()
        


# Calculate the total cost of the order if the user chose pickup, no toppings, and a special pizza
    if topping_ask == 'no' and form_of_consumption == 'pickup':
        if special_or_basic == 'special':
            total_cost = number_of_pizzas * 13.50
            # Asks the user if they would like to cancel before their order is finalized
            cancel = input("You have ordered [{}] from our special pizza menu, and have chosen not to add any extra toppings. The total cost of your order is ${}. Would you like to cancel your order? ".format(pizza_special, total_cost)).lower()
            if cancel == 'yes':
                print("Your order has been successfully cancelled.")
            if cancel == 'no':
                print("The order will be ready shortly, {}. Please come to the front counter and tell us your name. If no one shows up to collect the order then the number {} will be called.".format(name, phone_number))
                
        # Calculate the total cost of the order if the user chose pickup, no toppings, and a basic pizza
        elif special_or_basic == 'basic':
            total_cost = number_of_pizzas * 8.50
            # Asks the user if they would like to cancel before their order is finalized
            cancel = input("You have ordered [{}] from our basic pizza menu, and have chosen not to add any extra toppings. The total cost of your order is ${}. Would you like to cancel your order? ".format(pizza_basic, total_cost)).lower()
            if cancel == 'yes':
                print("Your order has been successfully cancelled.")
            if cancel == 'no':
                print("The order will be ready shortly, {}. Please come to the front counter and tell us your name. If no one shows up to collect the order then the number {} will be called.".format(name, phone_number))
            
# Calculate the total cost of the order if the user chose pickup, yes to toppings, and a special pizza
    if topping_ask == 'yes' and form_of_consumption == 'pickup':
        if special_or_basic == 'special':
            total_cost = number_of_pizzas * 13.50 + 0.50
            # Asks the user if they would like to cancel before their order is finalized 
            cancel = input("You have ordered [{}] from our special pizza menu, and have chosen to add extra toppings. The total cost of your order is ${}. Would you like to cancel your order? ".format(pizza_special, total_cost)).lower()
            if cancel == 'yes':
                print("Your order has been successfully cancelled.")
            if cancel == 'no':
                print("The order will be ready shortly, {}. Please come to the front counter and tell us your name. If no one shows up to collect the order then the number {} will be called.".format(name, phone_number))
                
        # Calculate the total cost of the order if the user chose pickup, yes to toppings, and a basic pizza 
        elif special_or_basic == 'basic':
            total_cost = number_of_pizzas * 8.50 + 0.50
            # Asks the user if they would like to cancel before their order is finalized
            cancel = input("You have ordered [{}] from our basic pizza menu, and have chosen to add extra toppings. The total cost of your order is ${}. Would you like to cancel your order? ".format(pizza_basic, total_cost)).lower()
            if cancel == 'yes':
                print("Your order has been successfully cancelled.")
            if cancel == 'no':
                print("The order will be ready shortly, {}. Please come to the front counter and tell us your name. If no one shows up to collect the order then the number {} will be called.".format(name, phone_number))
            
    # Calculate the total cost of the order if the user chose delivery, yes to toppings, and a special pizza       
    if topping_ask == 'yes' and form_of_consumption == 'delivery':
        if special_or_basic == 'special':
            total_cost = number_of_pizzas * 13.50 + 0.50 + 3
            # Asks the user if they would like to cancel before their order is finalized
            cancel = input("You have ordered [{}] from our special pizza menu, and have chosen not to add any extra toppings. The total cost of your order plus delivery is ${}. Would you like to cancel your order? ".format(pizza_special, total_cost)).lower()
            if cancel == 'yes':
                print("Your order has been successfully cancelled.")
            if cancel == 'no':
                print("The order will shortly be delivered to {}, {}. Please have a form of payment ready. The number {} will be called if no one is at the door.".format(address, name, phone_number))
                
        # Calculate the total cost of the order if the user chose delivery, yes to toppings, and a basic pizza 
        elif special_or_basic == 'basic':
            total_cost = number_of_pizzas * 8.50 + 0.50 + 3
            # Asks the user if they would like to cancel before their order is finalized
            cancel = input("You have ordered [{}] from our basic pizza menu, and have chosen to add extra toppings. The total cost of your order plus delivery is ${}. Would you like to cancel your order? ".format(pizza_basic, total_cost)).lower()
            if cancel == 'yes':
                print("Your order has been successfully cancelled.")
            if cancel == 'no':
                print("The order will shortly be delivered to {}, {}. Please have a form of payment ready. The number {} will be called if no one is at the door.".format(address, name, phone_number))
                
    # Calculate the total cost of the order if the user chose delivery, no extra toppings, and a special pizza         
    if topping_ask == 'no' and form_of_consumption == 'delivery':
        if special_or_basic == 'special':
            total_cost = number_of_pizzas * 13.50 + 3
            # Asks the user if they would like to cancel before their order is finalized
            cancel = input("You have ordered [{}] from our special pizza menu, and have chosen not to add any extra toppings. The total cost of your order plus delivery is ${}. Would you like to cancel your order? ".format(pizza_special, total_cost)).lower()
            if cancel == 'yes':
                print("Your order has been successfully cancelled.")
            if cancel == 'no':
                print("The order will shortly be delivered to {}, {}. Please have a form of payment ready. The number {} will be called if no one is at the door.".format(address, name, phone_number))
                
        # Calculate the total cost of the order if the user chose delivery, yes to toppings, and a basic pizza 
        elif special_or_basic == 'basic':
            total_cost = number_of_pizzas * 8.50 + 3
            # Asks the user if they would like to cancel before their order is finalized
            cancel = input("You have ordered [{}] from our basic pizza menu, and have chosen not to add any extra toppings. The total cost of your order plus delivery is ${}. Would you like to cancel your order? ".format(pizza_basic, total_cost)).lower()
            if cancel == 'yes':
                print("Your order has been successfully cancelled.")
            if cancel == 'no':
                print("The order will shortly be delivered to {}, {}. Please have a form of payment ready. The number {} will be called if no one is at the door.".format(address, name, phone_number))
                
    # Asks the user if they want to order again            
    restart = input("Would you like to place another order? ").lower()
    # main() is the entire program, so if the user types yes, then it runs the function 'main()' again
    if restart == 'yes':
        main()
    # if the user does not type yes then the program will end    
    else:
        print("Another order will not be placed. Have a nice day!")
        exit()

# starts the program
main()
