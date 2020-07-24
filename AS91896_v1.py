print("Hello welcome to the Waikato Air discount programe, please fill in the following questions to sign up for our personised email of daily discount fares :)")
def error():
    print("ERROR: Please type a valid input: ")
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
            
print("test")
