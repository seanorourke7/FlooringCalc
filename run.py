
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


user_input = measurement_type()


def validate_num(values):
    """
    Determines is the input is a number and raises an error if not. 
    """
    try:
        if values.isnumeric():
            return True
        else:
            raise ValueError(f"You Entered {values}. Only Numbers will be accepted \n")
    except ValueError as e:
        print(f"{e}. Please Try Again")
        return False

def calculate_length():
    """
    Take the input from the user for the Length
    """
    while True:
        length = input("Please enter the length of the room \n")
        
        if validate_num(length):
            break
    return length


floor_length = calculate_length()


def calculate_width():
    """
    Take the input from the user for the Width
    """
    while True:
        width = input("Please enter the width of the room \n")
        
        if validate_num(width):
            break
    return width


floor_width = calculate_width()

  
def box_coverage():
    """
    Take the input from the user to determine the coverage in each box.
    """
    while True:
        box_size = input("Enter the SQM coverage of the box (in numbers only)\n")

        if validate_num(box_size):
            break
    return box_size


box_size = box_coverage()
floor_size = (float(floor_length) * float(floor_width))

def boxes_needed():
    if user_input == 'm':
        boxes = (float(floor_size) / float(box_size))
    elif user_input == 'f':
        boxes = ((float(floor_size) /10.764) / float(box_size))
        
    return boxes

    print(f"you need {boxes} boxes")


boxes_needed = boxes_needed()

def cost_of_room():
    while True:
        cost = input("Enter cost per box (numbers only leave out the € sign)\n")

        if validate_num(cost):
            break
    return cost

cost = cost_of_room()

total_cost = (float(cost) * float(boxes_needed))
print(f"The total cost will be €{(total_cost)}")



