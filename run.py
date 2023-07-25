
def measurement_type():
    """
    Determines if the user is using meters or feet 
    """
    while True:
        print("Are you using Meters or Feet ? Enter m or f")
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
            raise TypeError(f"You Entered {values}. Only LowerCase m or f will be accepted")
    except TypeError as e:
        print(f"{e}. Please Try again")
        return False

    return True


user_input = measurement_type()


def validate_num(values):
    if values.isnumeric():
        return True
    try:
        if type(values) != float or int:
            raise ValueError(f"You Entered {values}. Only Numbers will be accepted")
    except ValueError as e:
        print(f"{e}. Please Try Again")
        return False

    return True


def calculate_length():
    while True:
        length = input("Please enter the length of the room \n")
        
        if validate_num(length):
            break
    return length


floor_length = calculate_length()

def calculate_width():
    while True:
        width = input("Please enter the width of the room \n")
        
        if validate_num(width):
            break
    return width


width = calculate_width()

def calculate_boxes_needed():
    box_size = float(input("Enter the SQM coverage of the box (in numbers only)\n"))
    if user_input == 'm':
        boxes_required = floor / float(box_size)
    elif user_input == 'f':
        boxes_required = (floor /10.764) / box_size
    
    print(f"You need {round(boxes_required)} boxes\n") 
    return round(boxes_required)
    

boxes_needed = calculate_boxes_needed()


def cost_of_room():
    cost = float(input("Enter cost per box (numbers only leave out the € sign)\n"))
    total_cost = boxes_needed * cost
    print(f"The total cost will be €{total_cost}")


cost_of_room()
