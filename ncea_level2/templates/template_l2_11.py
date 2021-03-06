#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Sphere_Plotter. template_l2_11.py based on template_master_l2.py
# Introduces: Get integer entry as radius. Use functions to calculate
# circumference, surface area and volume of sphere. Use iteration and
# output data each loop.
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
_program_ = "Sphere_Plotter"  # "template_l2_11.py"
_version_ = "1.0"
_date_ = "2016-10-25"
_author_ = "Ian Stewart"
_copyright_ = "© https://creativecommons.org/licenses/by/4.0/"
_description_ = ("When provided with a range of integer values for a radius\n"
                 "the sphere plotter program will determine the\n"
                 "circumference, surface area and volume.\n"
                 "The output may be cut and pasted into a spreadsheet.\n"
                 "If so, space delimiters must be merged.")
_original_ = ("template_master_l2.py - Ian Stewart - October 2016.\n"
              "© https://creativecommons.org/licenses/by/4.0/")

# Global Constants and variables init values. Can be read within functions.
# Can be the default values for arguments of a function.
PYTHON_MIN_VERSION = "3.2"
debug = False
log = "log_{}.txt".format(_program_)
radius = 1
sample = 20
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


def main(data=radius, sample=sample, log=log, in_file=input_file,
         out_file=output_file):
    """
    Main function that calls all other defined functions and statements.
    Edit this function to make your program...
    """
    message = "Program {} launched.".format(sys.argv[0])
    append_logfile(message, log)

    if debug: print("Program is starting...")
    if debug: print("data: {}, sample: {}, logfile: {}"
                    .format(data, sample, log))
    if debug: print("in_file: {}, out_file: {}".format(in_file, out_file))
    #
    # Call functions here...
    print("{} is executing...".format(_program_))

    # Get a integer value for the radius.
    radius = get_integer_entry(data, text="Enter radius of the sphere")

    # Get a integer value for the number of samples i.e. range.
    iteration = get_integer_entry(sample, text="Enter number of iterations")

    print("{: <15}{: <15}{: <15}{: <15}"
          .format("Radius", "Circumference", "Surface_Area", "Volume"))

    for i in range(radius, radius + iteration):

        if debug: print("\nPerforming circumference calculation...")
        circumference = calculate_circumference(i)

        if debug: print("\nPerforming surface area calculation...")
        surface = calculate_surface(i)

        if debug: print("\nPerforming volume calculation...")
        volume = calculate_volume(i)

        print("{: <15g}{: <15g}{: <15g}{: <15g}"
              .format(i, circumference, surface, volume))

    append_logfile("Min Radius:{}, Max Radius:{}"
                   .format(radius, radius + iteration - 1))

    if debug: print("Program is finished.")
    append_logfile("Program {} finished.".format(_program_))
    input("\nPress Enter key to end program.")
    sys.exit()
    # ===== end of main function =====


def get_integer_entry(prompt="0", text="Input integer value"):
    """
    Return an integer value from input on the console.
    An integer value as a prompt may be provided. Default prompt string is "0".
    The input prompting text may also be provided.
    """
    while True:
        data = input("{} [{}]:".format(text, prompt))
        if data == "":
            data = prompt
        try:
            return int(data)
        except ValueError as e:
            if debug: print("Value Error: {}".format(e))
            continue


def calculate_circumference(radius):
    """
    calculate_circumference of sphere.
    Algorithm: 2 * Pi * radius
    Argument = radius (integer)
    Set by the variable "radius=" or modified by the command line
    option of -r= or --radius=
    Return the circumference
    """
    circumference = 2 * math.pi * radius
    return circumference


def calculate_surface(radius):
    """
    calculate_surface of sphere.
    Algorithm: 4 * Pi * radius ^ 2
    Argument = radius (integer)
    Set by the variable "radius=" or modified by the command line
    option of -r= or --radius=
    Return the surface area
    """
    surface = 4 * math.pi * radius ** 2
    return surface


def calculate_volume(radius):
    """
    calculate_volume of sphere.
    Algorithm: 4/3 * Pi * radius ^ 3
    Argument = radius (integer)
    Set by the variable "radius=" or modified by the command line
    option of -r= or --radius=
    Return the volume
    """
    volume = 4 / 3 * math.pi * radius ** 3
    return volume


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
    print("  -r=, --radius=[VALUE]      Radius of sphere.")
    print("  -s=, --sample=[VALUE]      Samples. Number of iterations")
    print("  -h,  --help                Provide this help information.")
    print("  -d,  --debug               Provide additional information \n"
          "                             during program development.")
    # print("  -i=, --input=[FILE]        Input file")
    # print("  -o=, --output=[FILE]       Output file")
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
        # -s = total_sample
        if "-s" in option:
            sample_list = sys.argv[index].split("=")
            if len(sample_list) > 1:
                sample = sample_list[1]

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
    if debug: print("Variables: debug:{}, radius:{}, sample:{}, log:{}, "
                    "input_file:{}, output_file:{}"
                    .format(debug, radius, sample, log, input_file,
                            output_file))

    # Check the version of Python that is being run against Minimum version
    python_version_check()

    # Call main program, pass values from command line arguments, or variables
    # with their default values which may not have been modified by the cli.
    main(radius, sample, log, input_file, output_file)

"""
Notes:

To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 template_l2_11.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 template_l2_11.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""
