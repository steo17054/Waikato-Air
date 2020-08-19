#ask the user where their flight destinaiton is
print("Hello welcome to the Waikato Air discount programe, please fill in the following questions to sign up for our personised email of daily discount fares :)")

#creating a defintion for errors in the program
def error():
    print("ERROR: Please type a valid input: ")

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

#defintion to calculate discounts for the fare
#def calc_discount(): 


#Get the information from the user the calculate discount

           
print(destination)
