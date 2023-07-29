import math


def measurement_type():
    """
    Determines if the user is using meters or feet 
    """
    while True:
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
        box_size = input("Enter the SQM coverage of the box (in numbers only)\n")

        if validate_num(box_size):
            break
    return box_size


def boxes_needed():
    if user_input == 'm':
        boxes = (float(floor_size) / float(box_size))
    elif user_input == 'f':
        boxes = ((float(floor_size) /10.764) / float(box_size))
    print(f"you need {math.ceil(boxes)} boxes")

    return math.ceil(boxes)


def cost_per_box():
    while True:
        cost_of_box = input("Enter cost per box (numbers only)\n")

        if validate_num(cost_of_box):
            break
    return cost_of_box


user_input = measurement_type()
floor_length = calculate_length()
floor_width = calculate_width()
box_size = box_coverage()

floor_size = (float(floor_length) * float(floor_width))
boxes_needed = boxes_needed()
cost_of_box = cost_per_box()
total_cost = (float(cost_of_box) * float(boxes_needed))
print(f"The total cost will be €{(total_cost)}")
