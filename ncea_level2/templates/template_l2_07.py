#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Circle_Calculator. template_l2_07.py based on template_master_l2.py
# Introduces: Get floating point entry as radius. Use functions to calculate
# circle circumference and area. Change -s --stuff to -r --radius
#
# TODO: Describe your program here so that its description will be displayed
# using help(). See pydocs https://docs.python.org/3/library/pydoc.html
# E.g. $ pydoc3 -p 1234 then in a browser http://localhost:1234/
#

# Template functions utilize modules. Import them now to avoid problems later.
# import modules    # Functions, St trings, Lists used in template:
import sys          # .version(), .hexversion(), .exit(), .argv .stdout.write()
#                   # .stdout.flush()
import os           # .sep, .getcwd()
import datetime     # .datetime.now().strftime() .datetime.utcnow().strftime()
#                   # .datetime.today()
import textwrap     # .TextWrapper()
import tempfile     # .TemporaryFile(), .gettempdir()
import time         # .time(), .sleep()
import locale       # .setlocale(), .currency()

# Modules that could be handy...
import decimal
import math
import random

# Program details variables.
_program_ = "Circle_Calculator"  # "template_l2_07.py"
_version_ = "1.0"
_date_ = "2016-10-25"
_author_ = "Ian Stewart"
_copyright_ = "© https://creativecommons.org/licenses/by/4.0/"
_description_ = ("When provided with the a value for the radius, the circle \n"
                 "calculator program will determine the circles \n"
                 "circumference and area.")
_original_ = ("template_master_l2.py - Ian Stewart - October 2016.\n"
              "© https://creativecommons.org/licenses/by/4.0/")

# Global Constants and variables init values. Can be read within functions.
# Can be the default values for arguments of a function.
PYTHON_MIN_VERSION = "3.2"
debug = False
log = "log_{}.txt".format(_program_)
radius = 1
stuff = 42
input_file = "./temp/some_data.txt"
output_file = "./temp/some_data.txt"
timer_activated = 0

# Global variables that could be handy...
sep = os.sep
cwd = os.getcwd() + sep

# Check python is not below version 3. Prohibit running version 2.
if int(sys.version[:1]) < 3:
    print("Python version {} is not supported. \n"
          "Please restart using Python version 3 or higher. Exiting..."
          .format(sys.version.split(" ")[0]))
    sys.exit()


def main(data=radius, log=log, in_file=input_file, out_file=output_file):
    """
    Main function that calls all other defined functions and statements.
    Edit this function to make your program...
    """
    message = "Program {} launched.".format(sys.argv[0])
    append_logfile(message, log)

    if debug: print("Program is starting...")
    if debug: print("data: {}, logfile: {}".format(data, log))
    if debug: print("in_file: {}, out_file: {}".format(in_file, out_file))
    #
    # Call functions here...
    print("{} is executing...".format(_program_))

    # Get a floating point value for the radius.
    radius = get_float_entry(data, text="Enter radius of the circle")

    if debug: print("\nPerforming circumference calculation...")
    circumference = calculate_circumference(radius)
    print("Circle circumference: {:g}".format(circumference))

    if debug: print("\nPerforming area calculation...")
    area = calculate_area(radius)
    print("Circle area: {:g}".format(area))

    append_logfile("Radius:{:g}, Circumference:{:g}, Area:{:g}"
                   .format(radius, circumference, area))

    if debug: print("Program is finished.")
    append_logfile("Program {} finished.".format(_program_))
    input("Press Enter key to end program.")
    sys.exit()
    # ===== end of main function =====


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


def calculate_circumference(radius):
    """
    calculate_circumference of circle.
    Algorithm: 2 * Pi * radius
    Argument = radius (floating point)
    Set by the variable "radius=" or modified by the command line
    option of -r= or --radius=
    Return the circumference
    """
    circumference = 2 * math.pi * radius
    return circumference


def calculate_area(radius):
    """
    calculate_area of circle.
    Algorithm: Pi * radius ^ 2
    Argument = radius (floating point)
    Set by the variable "radius=" or modified by the command line
    option of -r= or --radius=
    Return the area
    """
    area = math.pi * radius ** 2
    return area


def python_version_check():
    """
    Check the version of python used is at the minimum or above the value for
    PYTHON_MIN_VERSION.
    sys.hexversion are: aa (major) bb (minor) cc (micro) f0 (final release)
    E.g. 0xaabbccf0. 0x30502f0 is 3.5.2 (final release)
    """
    min_version_list = PYTHON_MIN_VERSION.split(".")
    # Truncate if the list is more the 4 items
    if len(min_version_list) > 4:
        min_version_list = min_version_list[:4]
    # Fill if the list is less then 4 items
    if len(min_version_list) == 1:
        min_version_list.append("0")
    if len(min_version_list) == 2:
        min_version_list.append("0")
    if len(min_version_list) == 3:
        min_version_list.append("f0")
    # Calculate the minimum version and an integer, which, when displayed as
    # hex, is easily recognised as the version. E.g. 0x30502f0 is 3.5.2
    min_version_value = 0
    for index, item in enumerate(min_version_list[::-1]):
        min_version_value = min_version_value + int(item, 16) * 2**(index * 8)
    if debug: print("Python Version Minimum:{}, Decimal:{}, Hex:{}"
                    .format(PYTHON_MIN_VERSION, min_version_value,
                            hex(min_version_value)))
    # test value and exit if below minimum revision
    if sys.hexversion < min_version_value:
        print("Python Version: {}. Required minimum version is: {}. Exiting..."
              .format(sys.version.split(" ")[0], PYTHON_MIN_VERSION))
        sys.exit()


def append_logfile(message=None, logfile=log, path=cwd):
    """
    Append a time stamp and message to a log file.
    Default to using the current working directory (cwd)
    Prefix with a time stamp.
    Example: 2016-10-18 10:37:38.306: A message
    If message exceeds 55 characters, then use textwrap to indent next line
    Uses: datetime
          textwrap
    """
    if message is None:
        return
    # Wrap the text if it is greater than 80 - 25 = 55 characters.
    # Indent 25 spaces to on left to allow for width of time stamp
    wrapper = textwrap.TextWrapper()
    wrapper.initial_indent = " " * 25
    wrapper.subsequent_indent = " " * 25
    wrapper.width = 80
    message = wrapper.fill(message).lstrip()

    if debug: print(path + logfile)
    f = open(path + logfile, "a")
    # Truncate the 6 digit microseconds to be 3 digits of milli-seconds
    stamp = ("{0:%Y-%m-%d %H:%M:%S}.{1}:".format(datetime.datetime.now(),
             datetime.datetime.now().strftime("%f")[:-3]))
    if debug: print(stamp + " " + message)
    f.write(stamp + " " + message + "\n")


def help():
    "Provide help on command line options available."
    print("Program: {0}, Version: {1}, Date: {2}, Author: {3}"
          .format(_program_, _version_, _date_, _author_))
    print("{}".format(_description_))
    print("Usage: {} [OPTION]".format(_program_))
    print("Arguments...")
    print("  -r=, --radius=[VALUE]      Radius of circle.")
    print("  -h,  --help                Provide this help information.")
    print("  -d,  --debug               Provide additional information \n"
          "                             during program development.")
    # print("  -i=, --input=[FILE]        Input file")
    # print("  -o=, --output=[FILE]       Output file")
    # print("  -s=, --stuff=[VALUE]       Assign a value to stuff")
    print("  -l=, --log=[FILE]          Provide a filename for logging.")
    print("")
    print("Copyright: {}\n".format(_copyright_))


if __name__ == "__main__":
    # Get command line options from sys.argv list
    for index, option in enumerate(sys.argv):
        if "-h" in option:
            help()
            sys.exit()

        if "-d" in option:
            debug = not debug

        # Collect string data from command line interface (cli) sys.argv list
        # Overide "stuff" global variable.
        # Use = as the delimiter to split keyword and value. E.g.
        # -s=1, --stuff=2, -s="  Has spaces  ", --stuff=Smith, -s=4=four, etc.
        if "-s" in option:
            stuff_list = sys.argv[index].split("=")
            if len(stuff_list) > 1:
                stuff = stuff_list[1]

        if "-r" in option:
            radius_list = sys.argv[index].split("=")
            if len(radius_list) > 1:
                radius = radius_list[1]

        if "-i" in option:
            input_list = sys.argv[index].split("=")
            if len(input_list) > 1:
                input_file = input_list[1]

        if "-o" in option:
            output_list = sys.argv[index].split("=")
            if len(output_list) > 1:
                output_file = output_list[1]

        # Provide for a log file. Changes file name assigned to "log" variable.
        if "-l" in option:
            log_list = sys.argv[index].split("=")
            if len(log_list) > 1:
                # Avoid complexity of log file in sub-directories. In cwd.
                if os.sep not in log_list[1]:
                    log = log_list[1]

    if debug: print("sys.argv list = {}".format(sys.argv))
    if debug: print("Variables: debug:{}, radius:{}, log:{}, input_file:{},"
                    "output_file:{}"
                    .format(debug, radius, log, input_file, output_file))

    # Check the version of Python that is being run against Minimum version
    python_version_check()

    # Call main program, pass values from command line arguments, or variables
    # with their default values which may not have been modified by the cli.
    main(radius, log, input_file, output_file)

"""
Notes:

To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 template_l2_07.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 template_l2_07.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""
