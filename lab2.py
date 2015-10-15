#!/usr/bin/env python3

""" Graded Lab #2 for Inf1340, Fall 2015 """

__author__ = 'Hirra'


"""
Instructions: Add a function to to get input from the user and use that
function in name_that_shape()

The function should prompt the user for input until a legal value is
entered. A legal value is any integer.

"""

def name_that_shape():



    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs | Expected Outputs
    -------------------------
      < 3  | Error
      3    | triangle
      4    | quadrilateral
      5    | pentagon
      6    | hexagon
      7    | heptagon
      8    | octagon
      9    | nonagon
      10   | decagon
      > 10 | Error

    Errors: ValueError when input is a string or float

    """

    sides = get_user_input()
    print sides
    if sides == 3:
        print("triangle")
    elif sides == 4:
        print("quadrilateral")
    elif sides == 5:
        print("pentagon")
    elif sides == 6:
        print("hexagon")
    elif sides == 7:
        print("heptagon")
    elif sides == 8:
        print("octagon")
    elif sides == 9:
        print("nonagon")
    elif sides == 10:
        print("decagon")
    else:
        print("Error")


def get_user_input():

    output = ""

    input_is_an_integer = False

    while not input_is_an_integer:
        # while loop so we can get input
        output = raw_input("Number of sides:")

        # check whether input is the correct form
        if output.isdigit() or (output[0] == '-' and output[1:].isdigit()):
            output = int(output)
            input_is_an_integer = True
        else:
            print("Numbers Only")


    return output


name_that_shape()


