import math

def welcome():
    """
    Prints Welcome Message and explains how to use.
    """
    print("Welcome to Sean's Floor measuring tool\n")
    print("Please follow the input instructions carefully")
    

def measurement_type():
    """
    Determines if the user is using meters or feet 
    """
    while True:

        print()
        print("Are you using Meters or Feet ? Enter m or f \n")
        user_input = input()
    
        if validate_measurement_type(user_input):
            break

    return user_input


def validate_measurement_type(values):
    """
    Validates the measurement type prefered by the user
    """
    if values == 'm' or values == 'f':
        return True
    try:
        if values != ('m' or 'f'):
            raise TypeError(f"You Entered {values}. Only LowerCase m or f will be accepted \n")
    except TypeError as e:
        print(f"{e}. Please Try again")
        return False

    return True


def validate_num(values):
    """
    Determines is the input is a number and raises an error if not. 
    """
    try:
        if not float(values):
            raise ValueError(f"You Entered {values}. \n")
    except ValueError as e:
        print(f"{e}. Please Enter a Number")
        return False

    return True


def calculate_length():
    """
    Take the input from the user for the Length
    """
    while True:
        length = input("Please enter the length of the room \n")
        
        if validate_num(length):
            break
    return length


def calculate_width():
    """
    Take the input from the user for the Width
    """
    while True:
        width = input("Please enter the width of the room \n")
        
        if validate_num(width):
            break
    return width

  
def box_coverage():
    """
    Take the input from the user to determine the coverage in each box.
    """
    while True:
        box_size = input("Enter the Square Meter coverage of the box (in numbers only)\n")

        if validate_num(box_size):
            break
    return box_size


def calc_boxes_needed():
    """
    Calculates the amount of boxes needed and converts from feet
    to meters if the user chooses feet. 
    """
    
    if user_input == 'm':
        #calculates the size in meters
        boxes = (float(floor_size) / float(box_size))

    elif user_input == 'f':
        #converts from feet to meters
        boxes = ((float(floor_size) /10.764) / float(box_size))
    print(f"you need {math.ceil(boxes)} boxes")

    return math.ceil(boxes)


def cost_per_box():
    """
    Takes the input from the user for the price of each box.
    """
    while True:
        cost_of_box = input("Enter cost per box (numbers only)\n")

        if validate_num(cost_of_box):
            break
    return cost_of_box


def calc_total_cost():
    total_cost = (float(cost_of_box) * float(boxes_needed))
    print('')
    print(f"The total cost will be €{(total_cost)}")


welcome()
user_input = measurement_type()
floor_length = calculate_length()
floor_width = calculate_width()
box_size = box_coverage()
floor_size = (float(floor_length) * float(floor_width))
boxes_needed = calc_boxes_needed()
cost_of_box = cost_per_box()
calc_total_cost()

def offer_input():
    """
    Takes input to determine if there is an offer on
    """
    while True:
        print('')
        print("Is there currently an offer on ?\n")
        offer = input("Enter 1 to select '3 for 2' or Enter 2 for '4 for 3' Or 3 to exit\n")
    
        if validate_offer_type(offer):
            break
    return offer


def validate_offer_type(values):
    """
    Validates the offer type prefered by the user
    """
    if values == '1' or values == '2' or values == '3':
        return True
    try:
        if values != ('1' or '2' or '3'):
            raise TypeError(f"You Entered {values}. Only 1, 2 or 3 will be accepted \n")
    except TypeError as e:
        print(f"{e}. Please Try again")
        return False

    return True


def calc_3_for_2():
    """
    Calculates the cost with a 3 for 2 offer.
    """  
    if offer == '1':
        remainder = boxes_needed % 3
        offer_price = ((math.floor((boxes_needed / 3)) * 2) + remainder) * float(cost_of_box)
        print(f"the price with 3 for 2 applied is €{math.ceil(offer_price)}\n")


def calc_4_for_3():
    """
    Calculates the cost with a 4 for 3 offer.
    """  
    if offer == '2':
        remainder = boxes_needed % 4
        offer_price = ((math.floor((boxes_needed / 4)) * 3) + remainder) * float(cost_of_box)
        print(f"the price with 4 for 3 applied is €{math.ceil(offer_price)}\n")


offer = offer_input()
calc_3_for_2()
calc_4_for_3()



