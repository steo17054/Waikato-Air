#setting global variables for the program to be used and modified in the defintions
destination = ""
next_day = ""
user_name = ""
discount = 0
percentage_discount = 0
discount_fare = 0
num_seats_wel = 110
num_seats_auk = 130
num_seats_rot = 100
wellington_regular_fare = 70
rotorua_regular_fare = 50
auckland_regular_fare = 80
regular_fare_dict = {"Wellington" : 70, "Rotorua" : 50, "Auckland" : 80}
num_seats_user_files_wel = {}
num_seats_user_files_auk = {}
num_seats_user_files_rot = {}

#main loop for the program allowing the user to restart it to enter another input
main_program_loop = True
while main_program_loop == True:

#creating a definiton to add line spacing in the programe
  def space():
    print(" ")

#creating a defintion for errors in the program
  def error():
    print("ERROR: Please type a valid input: ")
    space()

#creating a defintion for restarting the programe if the user wants to enter for another discount
  def restart():
    global num_seats_user_files
    global main_program_loop
    restart_bool_loop = True
    while restart_bool_loop == True:
      restart_bool = input("Would you like to enter for another user? (Type 'YES' or 'NO'): ")
      space()
      restart_bool = restart_bool.upper()
      if restart_bool == "YES":
        restart_bool_loop = False
        main_program_loop = True
      elif restart_bool == "NO":
        print("Thank you for working with us, here are your dictionary of users and their seat numbers for each destination: ")
        space()
        print("Wellington: {}" .format(num_seats_user_files_wel))
        space()
        print("Auckland: {}" .format(num_seats_user_files_auk))
        space()
        print("Rotorua: {}" .format(num_seats_user_files_rot))
        restart_bool_loop = False
        main_program_loop = False
      else:
        error()
        restart_bool_loop = True 
  
#creating a definition to get the users name input
  def name_input():
    global user_name
    #user_name_loop = True
    #while user_name_loop == True:
    user_name = str(input("Hello I am the Waikato Air Bot here to calculate your discount, please enter your name for this order: "))
    space()
    user_name = user_name.title()
    return user_name

#creating a definition to get the destination input from the user  
  def destination_input():
    global destination
    destination_loop = True
    while destination_loop == True:
      destination = str(input("Firstly, where are you looking to fly to out of our available destinations. (Type: Auckland, Wellington, Rotorua of fares to see their standard costs): "))
      space()
      destination = destination.upper()
      if destination == "AUCKLAND":
          destination_loop = False
      elif destination == "WELLINGTON":
          destination_loop = False
      elif destination == "ROTORUA":
          destination_loop = False
      elif destination == "FARES":
        print("Here are the regular fares for our available destinations: {}" .format(regular_fare_dict))
        space()
        destination_loop = True
      else:
          error()
          destination_loop = True
    return destination

#creating a definition to get the input on whether the user can travel tommorow or not
  def next_day_input():
    global next_day
    next_day_loop = True
    while next_day_loop == True:
      next_day = str(input("Would you be able to travel to your destination tommorow (Type 'YES' or 'NO'): "))
      space()
      next_day = next_day.upper()
      if next_day == "YES":
          next_day_loop = False
      elif next_day == "NO":
        print("Sorry there are no discounts we can offer you if you can't travel tommorow")
        restart()
        space()
        next_day_loop = False
      else:
        error()
        next_day_loop = True

    return next_day

#creating a defintion to calculate all the discounts for the users fare
  def user_calculations():
    global num_seats_user_files
    global num_seats_auk
    global num_seats_wel
    global num_seats_rot
    global discount
    global percentage_discount
    global discount_fare
    if next_day == "YES":
      if destination == "AUCKLAND":
        num_seats_auk = num_seats_auk - 1
        num_seats_user_files_auk[num_seats_auk] = user_name
        discount = (30 - (len(num_seats_user_files_auk) / 2)) * 1.5
        percentage_discount = discount / 100
        discount_fare = auckland_regular_fare - discount      
      elif destination == "WELLINGTON":
        num_seats_wel = num_seats_wel - 1
        num_seats_user_files_wel[num_seats_wel] = user_name
        discount = (30 - (len(num_seats_user_files_wel) / 2)) * 1.5
        percentage_discount = discount / 100
        discount_fare = wellington_regular_fare - discount
      elif destination == "ROTORUA":
        num_seats_rot = num_seats_rot - 1
        num_seats_user_files_rot[num_seats_rot] = user_name
        discount = (30 - (len(num_seats_user_files_rot) / 2)) * 1.5
        percentage_discount = discount / 100
        discount_fare = rotorua_regular_fare - discount
      return num_seats_auk, num_seats_wel, num_seats_rot, discount, percentage_discount, discount_fare

#creating defintion to form the paragraph for the user to present their discounts
  def discount_paragraph():
    global user_name
    global num_seats_wel
    global num_seats_auk
    global num_seats_rot
    global discount
    global percentage_discount
    global discount_fare
    global destination
    if destination == "AUCKLAND":
      print("Hello {}, today we are able to offer you a {}% discount on your flight tommorow to {}. As there was {} seats left on the plane we are able to offer you a discount of ${}, bringing the total cost of your flight to {} down to ${}. Thank you for working with Waikato Air and we look foward to seeing you tommorow for your flight" .format(user_name, percentage_discount, destination, num_seats_auk, discount, destination, discount_fare))
      space()
    elif destination == "WELLINGTON":
      print("Hello {}, today we are able to offer you a {}% discount on your flight tommorow to {}. As there was {} seats left on the plane we are able to offer you a discount of ${}, bringing the total cost of your flight to {} down to ${}. Thank you for working with Waikato Air and we look foward to seeing you tommorow for your flight" .format(user_name, percentage_discount, destination, num_seats_wel, discount, destination, discount_fare))
      space()
    elif destination == "ROTORUA":
      print("Hello {}, today we are able to offer you a {}% discount on your flight tommorow to {}. As there was {} seats left on the plane we are able to offer you a discount of ${}, bringing the total cost of your flight to {} down to ${}. Thank you for working with Waikato Air and we look foward to seeing you tommorow for your flight" .format(user_name, percentage_discount, destination, num_seats_rot, discount, destination, discount_fare))
      space()

#running the defintions in the code 
  name_input()
  destination_input()
  next_day_input()
  user_calculations()
  discount_paragraph()  
  restart()        