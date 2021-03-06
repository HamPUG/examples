#!/usr/bin/env python3
#
import sys
import math
_description_ = """
    Cube calculations. Enter the length of an edge.
    Calculate surface area, volume and internal diagonal using functions.
    formats {:g} provides numeric rounding. E.g. 314.1592653589793 to  314.159.
    Procedural programming style.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_09_b.py

# Variables
edge_prompt = 2
debug = False

print("Program {} has started...".format(sys.argv[0]))


def main(prompt):
    "Main rountine for calculating cube dimensions"
    if debug: print("Prompt value for edge: {}".format(prompt))
    edge = get_float_entry(prompt, text="Enter length of an edge of the cube")
    if debug: print("Value for edge: {}".format(edge))

    surface = calculate_surface(edge)
    print("Cube Surface Area: {:g}".format(surface))

    volume = calculate_volume(edge)
    print("Cube Volume: {:g}".format(volume))

    diagonal = calculate_diagonal(edge)
    print("Cube Space Diagonal: {:g}".format(diagonal))


def get_float_entry(prompt="0", text="Input floating point value"):
    """
    Return a floating point value from input on the console.
    A float value as a prompt may be provided. Default prompt string is "0".
    The input prompting text may also be provided.
    """
    while True:
        data = input("{} [{}]:".format(text, prompt))
        if data == "":
            data = prompt
        try:
            return float(data)
        except ValueError as e:
            if debug: print("Value Error: {}".format(e))
            continue


def calculate_surface(edge):
    """
    calculate_surface of cube.
    Algorithm: 6 * edge ^2
    """
    surface = 6 * edge ** 2
    return surface


def calculate_volume(edge):
    """
    calculate_volume of cube.
    Algorithm: edge ^3
    """
    volume = edge ** 3
    return volume


def calculate_diagonal(edge):
    """
    calculate_diagonal through the space of the cube.
    Algorithm: square root 3 * edge
    """
    diagonal = math.sqrt(3) * edge
    return diagonal


if __name__ == "__main__":
    print("Program {} has started...".format(sys.argv[0]))
    print("Enable debugging with -d or --debug")
    print("E.g. python {} --debug".format(sys.argv[0]))
    print("Set edge prompt value -e= or --edge=")
    print("E.g. python {} --edge=5.1".format(sys.argv[0]))

    # Get command line options from sys.argv list
    for index, option in enumerate(sys.argv):

        if "-d" in option:
            debug = not debug

        # Collect string data from command line interface (cli) sys.argv list
        if "-e" in option:
            edge_prompt_list = sys.argv[index].split("=")
            if len(edge_prompt_list) > 1:
                edge_prompt = edge_prompt_list[1]

    main(edge_prompt)

    print("End of program.")

input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_09_b.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_09_b.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""
