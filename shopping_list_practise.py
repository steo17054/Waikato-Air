def error_input():
    print("That isn't a valid input, please type in a valid input")
    list_input_loop = True

user_name = str(input("What is your name? "))
shopping_list = []
list_input_loop = True
while list_input_loop:
        list_input = str(input("What would you like to add to your shopping list {}? (Type 'stop' at anytime to print out current list): " .format(user_name)))
        list_input = list_input.upper
        print("{} has been added!" .format(list_input))
        if list_input == 'STOP':
            print(shopping_list)
            list_input_loop = False                
        else:
            shopping_list.append(list_input)
            list_input_loop = True


                
                
