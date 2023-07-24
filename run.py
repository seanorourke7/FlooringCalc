def measurement_type():
    """
    Determines if the user is using meters or feet 
    """
    while True:
        print("Are you using Meters or Feet ? Enter m or f")
        user_input = input()
    
        if validate_data(user_input):
            print("data is valid")
            break

    return user_input


def validate_data(values):
    try:
        if type(values) == float or int:
            raise TypeError(f"You Entered {values}. Only LowerCase m or f will be accepted")
    except TypeError as e:
            print(f"{e} Please Try again")

            return False
    return True   


user_input = measurement_type()


def calculate_floor_size():
    length = float(input("Please enter the length of the room \n"))
    width = float(input("Please enter the width of the room\n"))
    floor_size = length * width
    print(f"The floor size is {floor_size} {user_input} Squared ")
    return floor_size


floor = calculate_floor_size()


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
