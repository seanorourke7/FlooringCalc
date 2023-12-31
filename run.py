import math
"""
Use for calculating measurements.
"""
import os

import colorama

from colorama import Back, Fore, Style

colorama.init(autoreset=True)

"""
Use for changing colour of text
"""

logo = """
  ______ _                  _                _____      _      
 |  ____| |                (_)              / ____|    | |     
 | |__  | | ___   ___  _ __ _ _ __   __ _  | |     __ _| | ___ 
 |  __| | |/ _ \ / _ \| '__| | '_ \ / _` | | |    / _` | |/ __|
 | |    | | (_) | (_) | |  | | | | | (_| | | |___| (_| | | (__ 
 |_|    |_|\___/ \___/|_|  |_|_| |_|\__, |  \_____\__,_|_|\___|
                                     __/ |                     
                                    |___/                                                    
"""


def measurement_type():
    """
    Determines if the user is using meters or feet
    """
    while True:

        print("Are you using Meters or Feet ? Enter m or f. \n")
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
            raise TypeError(Fore.RED + f"You Entered {values}.\n")
    except TypeError as e:
        print(f"{e}Only LowerCase m or f will be accepted. Please Try again")
        return False

    return True


def validate_num(values):
    """
    Determines is the input is a number and raises an error if not.
    """

    try:
        float(values)
        if float(values) <= 0:
            raise ValueError(Fore.RED + f"You entered {values} \n")
    except ValueError:
        print(Fore.RED + "Please Enter Numbers only \n")
        return False

    return True


def calculate_length():
    """
    Take the input from the user for the Length
    """
    while True:
        length = input("Please enter the length of the room. (numbers only)\n")
        if validate_num(length):
            break
    return length


def calculate_width():
    """
    Take the input from the user for the Width
    """
    while True:
        width = input("Please enter the width of the room. (numbers only)\n")
        if validate_num(width):
            break
    return width


def box_coverage():
    """
    Take the input from the user to determine the SQM coverage in each box.
    """
    while True:
        box_size = input("Enter the Square Meter coverage of the box.\n")

        if validate_num(box_size):
            break
    return box_size


def calc_boxes_needed(user_input, floor_size, box_size):
    """
    Calculates the amount of boxes needed and converts from feet
    to meters if the user chooses feet.
    """

    if user_input == 'm':
        boxes = (float(floor_size) / float(box_size))

    elif user_input == 'f':
        boxes = ((float(floor_size) / 10.764) / float(box_size))
    print(Fore.GREEN + f"You will need {math.ceil(boxes)} boxes.")

    return math.ceil(boxes)


def cost_per_box():
    """
    Takes the input from the user for the price of each box.
    """
    while True:
        cost_of_box = input("Enter cost per box (numbers only).\n")

        if validate_num(cost_of_box):
            break
    return cost_of_box


def calc_total_cost(cost_of_box, boxes):
    """
    Calculates the Total cost before any offers are applied
    """
    total_cost = (float(cost_of_box) * float(boxes))
    print(Fore.GREEN + f"The total cost will be €{math.ceil(total_cost)}.\n")
    return float(total_cost)


def offer_input(total_cost, cost_of_box, boxes):
    """
    Takes input to determine if there is an offer on
    """
    while True:
        print("Is there currently an offer on ?\n")
        print("Enter 1 to select '3 for 2'.\n")
        print("Enter 2 to select '4 for 3'.\n")
        print("Enter 3 for a percentage reduction\n")
        offer = input("Enter 4 to restart.\n")

        if validate_offer_type(offer):
            if offer == '1':
                calc_3_for_2(boxes, cost_of_box)
            elif offer == '2':
                calc_4_for_3(boxes, cost_of_box)
            elif offer == '3':
                perc = get_percentage()
                cal_perc_off(total_cost, perc)
            elif offer == '4':
                main()
            break

    return offer


def validate_offer_type(values):
    """
    Validates the input from the user to determine the offer type
    """
    if values == '1' or values == '2' or values == '3' or values == '4':
        return True
    try:
        if values != ('1' or '2' or '3' or '4'):
            raise TypeError(Fore.RED + f"You Entered {values}. \n")
    except TypeError as e:
        print(f"{e}. Only 1, 2, 3 or 4 will be accepted. Please Try again.\n")
        return False

    return True


def calc_3_for_2(boxes, cost_of_box):
    """
    Calculates the cost with a 3 for 2 offer. By dividing by 3 and multiplying
    by 2. If their is a remainder this is removed form the initial calculation
    and added later to give a true cost of each box and avoid fractions.
    """
    r = boxes % 3
    offer_price = ((math.floor((boxes / 3)) * 2) + r) * float(cost_of_box)
    print(Fore.GREEN + f"The price with '3 for 2'")
    print(Fore.GREEN + f"is €{math.ceil(offer_price)}.\n")
    start_over()


def calc_4_for_3(boxes, cost_of_box):
    """
    Calculates the cost with a 4 for 3 offer. By dividing by 4 and multiplying
    by 3. If their is a remainder this is removed form the initial calculation
    and added later to give a true cost of each box and avoid fractions.
    """

    r = boxes % 4
    offer_price = ((math.floor((boxes / 4)) * 3) + r) * float(cost_of_box)
    print(Fore.GREEN + f"The price with '4 for 3'")
    print(Fore.GREEN + f"is €{math.ceil(offer_price)}.\n")
    start_over()


def get_percentage():
    """
    Gets the input from the user to determine the percentage discount amount
    """

    while True:
        perc = input("Please enter the percentage amount (numbers only)\n")
        if validate_num(perc):
            break
    return perc


def cal_perc_off(total_cost, perc):
    """
    Calculates the percentage discount by dividing the total by 100
    and multiplying by the percentage entered
    then taking this away from the total cost.
    """
    perc_cost = (total_cost - ((float(total_cost) / 100) * float(perc)))
    print(Fore.GREEN + f"The total minus {perc}% discount ")
    print(Fore.GREEN + f"is €{math.ceil(perc_cost)}\n")
    start_over()


def start_over():
    """
    Asks the user if they want to start again
    and runs the program if 'y' is input.
    """
    while True:
        print("Do you want to start again ? y/n \n")
        user_input = input()
        if user_input == 'y':
            main()
        if user_input == 'n':
            print("Thank you for using Sean's Flooring Calculator.")
        if validate_start_over(user_input):
            break

    return True


def validate_start_over(values):
    """
    Validates the input for the start over function.
    """
    if values == 'y' or values == 'n':
        return True
    try:
        if values != ('y' or 'n'):
            raise TypeError(Fore.RED + f"You Entered {values}.\n")
    except TypeError as e:
        print(f"{e}Only LowerCase y or n will be accepted. Please Try again")
        return False


def main():
    """
    Runs all of the functions.
    """

    user_input = measurement_type()
    floor_length = calculate_length()
    floor_width = calculate_width()
    box_size = box_coverage()
    floor_size = (float(floor_length) * float(floor_width))
    boxes = calc_boxes_needed(user_input, floor_size, box_size)
    cost_of_box = cost_per_box()
    total_cost = calc_total_cost(cost_of_box, boxes)
    offer_input(total_cost, cost_of_box, boxes)


print(logo)
print("Welcome to Sean's Flooring Calculator.\n")
print("Please follow the input instructions carefully.\n")


if __name__ == "__main__":
    main()
