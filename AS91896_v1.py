num_seats_per_plane = 130
wellington_regular_fare = 70
auckland_regular_fare = 80
rotorua_regular_fare = 50

#ask the user where their flight destinaiton is
print("Hello welcome to the Waikato Air discount programe, please fill in the following questions to sign up for our personised email of daily discount fares :)")

#creating a defintion for errors in the program
def error():
    print("ERROR: Please type a valid input: ")

#class defintion to gain all of the user inputs needed for discount calculations
def user_inputs():
#code to get the destination input from the user and to error catch invalid inputs
  destination_loop = True
  while destination_loop == True:
    destination = str(input("Firstly, where are you looking to fly to out of our available destinations. (Type: Auckland, Wellington or Rotorua): "))
    destination = destination.upper()
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
  next_day_loop = True
  while next_day_loop == True:
    next_day = bool(input("Would you be able to travel to your destination tommorow (Type 'YES' or 'NO'): "))
    next_day = next_day.upper()
    if next_day == "YES":
      next_day_loop = False
    elif next_day == "NO":
      next_day_loop = False
    else:
      error()
      next_day_loop = True

  return destination, next_day

#class defintion to calculate all the discounts for the users fare
def user_calculations(destination, next_day):
  if next_day == "YES":
    num_seats = num_seats_per_plane - 1
    

  elif next_day == "NO":
    
  #percentage_discount = discount / 100

#Get the information from the user the calculate discount

           
