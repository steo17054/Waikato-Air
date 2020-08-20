#loop to restart the programme if the user wants to enter for another user
restart_loop = True
while restart_loop == True:
  #constant variables for calculating discouts on fares
  num_seats = 130
  wellington_regular_fare = 70
  auckland_regular_fare = 80
  rotorua_regular_fare = 50

  #ask the user where their flight destinaiton is
  #print("Hello welcome to the Waikato Air discount programe, please fill in the following questions to sign up for our personised email of daily discount fares :)")

  #creating a defintion for errors in the program
  def error():
    print("ERROR: Please type a valid input: ")

  #creating a defintion for restarting the programe if the user wants to enter for another discount
  def restart():
    restart_bool_loop = True
    while restart_bool_loop == True:
      restart_bool = bool(input("Would you like to enter for another user? (Type 'YES' or 'NO'): "))
      restart_bool = restart_bool.upper()
      if restart_bool == "YES":
        restart_loop = True
        restart_bool_loop = False
      elif restart_bool == "NO":
        restart_loop = False
        restart_bool_loop = False
      else:
        error()
        restart_bool_loop = True 

  #class defintion to gain all of the user inputs needed for discount calculations
  class user_inputs(destination, next_day):
  #code to get the destination input from the user and to error catch invalid inputs
    def destinaiton_input():
      destination_loop = True
      while destination_loop == True:
        destination = str(input("Firstly, where are you looking to fly to out of our available destinations. (Type: Auckland, Wellington or Rotorua): "))
        destination = destination.upper()
        global destination
        if destination == "AUCKLAND":
            destination_loop = False
        elif destination == "WELLINGTON":
            destination_loop = False
        elif destination == "ROTORUA":
            destination_loop = False
        else:
            error()
            destination_loop = True
  #code to get the input on whether the user can travel tommorow or not and to error catch invalid inputs
    def next_day_input():
      next_day_loop = True
      while next_day_loop == True:
        next_day = str(input("Would you be able to travel to your destination tommorow (Type 'YES' or 'NO'): "))
        next_day = next_day.upper()
        if next_day == "YES":
          next_day_loop = False
        elif next_day == "NO":
          print("Sorry there are no discounts we can offer you if you can't travel tommorow")
          restart()
          next_day_loop = False
        else:
          error()
          next_day_loop = True

      return destination, next_day

  #class defintion to calculate all the discounts for the users fare
  def user_calculations(destination, next_day, num_seats, discount, percentage_discount, discount_fare):
    if next_day == "YES":
      num_seats = num_seats - 1
      discount = num_seats / 5
      percentage_discount = discount / 100
      if destination == "AUCKLAND":
        discount_fare = auckland_regular_fare - discount      
      elif destination == "WELLINGTON":
        discount_fare = wellington_regular_fare - discount
      elif destination == "ROTORUA":
        discount_fare = rotorua_regular_fare - discount
    return num_seats, discount, percentage_discount, discount_fare 

  #creating defintion to form the paragraph for the user to present their discounts
  def discount_paragraph(destinaiton, num_seats, discount, percentage_discount, discount_fare):
    print("Hello, today we are able to offer you a {}% discount on your flight tommorow to {}. As there was {} seats left on the plane we are able to offer you the ... discount this being a discount of ${}, bringing the total cost of your flight to {} down to ${}. Thank you for working with Waikato Air and we look foward to seeing you tommorow for your flight" .format(percentage_discount, destinaiton, num_seats, discount, destinaiton, discount_fare))

  #running the defintions in the code
  user_inputs(destination, next_day)
  user_calculations(destination, next_day)
  discount_paragraph(destinaiton, num_seats, discount, percentage_discount, discount_fare)            
