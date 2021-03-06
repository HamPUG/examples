#!/usr/bin/env python3
import sys
import time
import platform

_description_ = """
    Demonstrate ANSI escape sequences for direct cursor addressing and setting
    forground and back ground colours on a console.
    Perform line drawing on a console using the box drawing character set.
    On Microsoft Windows console this is better than using the ANSI escape
    sequence box drawing as it is missing the ability to do the cross-hairs.
    Draw reducing sized rectangles in different colours.
    Use print(EscapeSequence, end="", flush=True) to prevent newline character.
    Functions: draw_rectangle(), colour_check(), write_text()
    Also added COLOUR as a read-only dictionary to convert colour names to
    numeric string for the colour. If invalid colour data then remain with the
    default console colours.
    Sets the console windows title with ESC ] 2 ; <string> BEL
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_23_c.py

# Initialise constants
ESC = chr(27)  # Escape character
CSI = ESC + "["  # Control Sequence Introducer
BEL = chr(7)  # Bell character
# Set if you want to pause between screens and hit return to continue
pause = True
delay = True
delay_duration = 0.3
# Create a colour dictionary to translate colours to numeric values
# Dictionary values are (foreground colours, background colours).
COLOUR = {"black": (30, 40),  # 16 colours available
          "red": (31, 41),
          "green": (32, 42),
          "yellow": (33, 43),
          "blue": (34, 44),
          "magenta": (35, 45),
          "cyan": (36, 46),
          "light_grey": (37, 47),
          "grey": (90, 100),
          "light_red": (91, 101),
          "light_green": (92, 102),
          "light_yellow": (93, 103),
          "light_blue": (94, 104),
          "light_magenta": (95, 105),
          "light_cyan": (96, 106),
          "white": (97, 107),
          "dark_red": (31, 41),  # Allow dark prefix for 7 x normal colours
          "dark_green": (32, 42),
          "dark_yellow": (33, 43),
          "dark_blue": (34, 44),
          "dark_magenta": (35, 45),
          "dark_cyan": (36, 46),
          "dark_grey": (90, 100),
          "bright_grey": (37, 47),  # Allow bright prefix for 7 x light colours
          "bright_red": (91, 101),
          "bright_green": (92, 102),
          "bright_yellow": (93, 103),
          "bright_blue": (94, 104),
          "bright_magenta": (95, 105),
          "bright_cyan": (96, 106),
          "default": (39, 49)  # Allow name "default" for the default colours
          }

# Enable Win10 CMD window to support ANSI esacpe sequences.
if platform.system() == "Windows":
    print("\nMicrosoft {} Release: {} Version: {}"
          .format(platform.system(), platform.release(), platform.version()))
    ver_list = platform.version().split(".")
    if int(platform.release()) < 10:
        print("Requires Windows version 10 or higher for ANSI support.")
        print("Exiting...")
        sys.exit()

    if len(ver_list) >= 2:  # E.g. ['10', '0', '14393']
        # print(ver_list)
        minor_version = float((ver_list[1] + "." + ver_list[2]))
        # print(minor_version)  # E.g. 0.14393

        if minor_version >= 0.10586:
            print("Version of Win10 should support ANSI escape sequences.")
        else:
            print("Win10 requires updating to support ANSI escape sequences.")
            print("Minimum version: 10.0.10586 'Threshold 2' 10 May 2016.")
            print("Exiting...")
            sys.exit()
            # 10.0.14393 is "The Anniversary Update". Released 2 Aug 2016.
    if int(platform.release()) >= 10:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        status = kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        if status == 0:
            print("Error returned attempting to set ANSI escape sequences.")
        else:
            print("Windows CMD window has been set for ANSI escape sequences.")
            print()
            t = ("For more information on Microsoft use of ANSI escape codes"
                 "\nplease visit this web-page...\n"
                 "https://msdn.microsoft.com/en-us/library/mt638032(v=vs.85)"
                 ".aspx")
            print(t)
    if delay: time.sleep(2)
    if pause: input("\nType Return key to continue")


else:
    # The Linux platform normally has a console terminal that supports ANSI
    # escape sequences.
    pass


def draw_rectangle(start_column=1, start_row=1, width=80, height=23,
                   foreground_colour=39, background_colour=49):
    """
    Draw a rectangle using characters from Box Drawing character set.
    0x2500 to 0x257f
    Single top and single side from box drawing characgter set.
    ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼

    # start_column = 1  # Columns start count at 1
    # start_row = 1  # Rows start count at 1
    # width = 80  # Min. width = 2 Max greater than 80 columns then drop chars
    # height = 24  # Min. height = 2 Max of 24 or 25. But could be more.
    """
    # Execute function to check for valid colours and force correction
    foreground_colour, background_colour = colour_check(foreground_colour,
                                                        background_colour)
    # Set foreground and background colours
    print("{}{}m{}{}m".format(CSI, foreground_colour, CSI, background_colour),
          end="", flush=True)

    # Top line
    # Prints Left corner at position 1, then horizontal line. E.g. From
    # position 2 to column 79, Adds right corner. E.g. At position 80.
    print("{}{};{}H┌".format(CSI, start_row, start_column),
          end="", flush=True)
    for i in range(start_column + 1, start_column + width - 1):
        print("{}{};{}H─".format(CSI, start_row, i),
              end="", flush=True)
    print("{}{};{}H┐".format(CSI, start_row, start_column + width - 1),
          end="", flush=True)

    # Middle lines
    # Adds the vertical lines on each side of the rectangle. Positions 1 and 80
    for j in range(start_row + 1, start_row + height - 1):
        print("{}{};{}H│".format(CSI, j, start_column),
              end="", flush=True)
        print("{}{};{}H│".format(CSI, j, start_column + width - 1),
              end="", flush=True)

    # Bottom line
    # Prints bottom corner e.g. Position 1, then horizontal line. E.g. From
    # position 2 to column 79. Adds bottom corners. E.g. At position 80.
    print("{}{};{}H└".format(CSI, start_row + height - 1, start_column),
          end="", flush=True)
    for i in range(start_column + 1, start_column + width - 1):
        print("{}{};{}H─".format(CSI, start_row + height - 1, i),
              end="", flush=True)
    print("{}{};{}H┘"
          .format(CSI, start_row + height - 1, start_column + width - 1),
          end="", flush=True)

    # Restore foreground and background colours.
    print("{}39m{}49m".format(CSI, CSI), end="", flush=True)
    return 0


def colour_check(foreground_colour=39, background_colour=49):
    """
    Check colours are valid.
    If invalid colour set foreground to default of 39, and background to
    default of 49.
    To translate colour name strings to integers, use the COLOUR dictionary.
    Requires: COLOUR dictionary.
    """
    # print(COLOUR.keys())
    # print(COLOUR.values())
    if foreground_colour in COLOUR:
        # print(COLOUR[foreground_colour][0])
        foreground_colour = COLOUR[foreground_colour][0]
    if background_colour in COLOUR:
        # print(COLOUR[background_colour][1])
        background_colour = COLOUR[background_colour][1]
    # Check for if an invalid colour string was entered.
    try:
        int(foreground_colour)
        if (foreground_colour >= 30 and foreground_colour <= 37 or
            foreground_colour >= 90 and foreground_colour <= 97 or
                foreground == 39):
            # print("Foreground colour OK: {}".format(foreground_colour))
            pass
        else:
            # Foreground colour out of range, force it to be 97, i.e. white.
            # print("Foreground Out of range: {}".format(foreground_colour))
            foreground_colour = 39
    except:
        # Foreground colour is a string that is not a dictionary key.
        # Force the foreground to be the integer of white i.e. 97
        foreground_colour = 39

    # Check for if an invalid background colour string was entered.
    try:
        int(background_colour)
        if (background_colour >= 40 and background_colour <= 47 or
            background_colour >= 100 and background_colour <= 107 or
                background == 49):
            # print("background colour OK: {}".format(background_colour))
            pass
        else:
            # Background colour out of range, force it to be 40, i.e. black.
            # print("background Out of range: {}".format(background_colour))
            background_colour = 49
    except:
        # Background colour is a string that is not a dictionary key.
        # Force the background to be the integer of black i.e. 40
        background_colour = 49
    return foreground_colour, background_colour

    """
    # Check colour_check() code...
    fg,bg = colour_check(35,107)
    print(fg, bg)
    sys.exit()
    """


def write_text(text="", start_column=1, start_row=1, foreground_colour=39,
               background_colour=49):
    """
    Write text using x, y, foreground colour and background colour
    Using x,y order may overcome confusion of y,x in cursor addressing.
    E.g. Esc [ y x H Some text starting at y x cursor position.
    Print statement prohibits the newline with end="" and flush=True may
    overcome buffering issues.
    """
    # Execute function to check for valid colours and force correction
    foreground_colour, background_colour = colour_check(foreground_colour,
                                                        background_colour)

    # Apply foreground and background colours
    print("{}{}m{}{}m"
          .format(CSI, foreground_colour, CSI, background_colour),
          end="", flush=True)

    # Apply direct cursor addressing and write the text.
    print("{}{};{}H{}".format(CSI, start_row, start_column, text),
          end="", flush=True)

    # Restore foreground (39) and background (49) colours to default values
    print("{}39m{}49m".format(CSI, CSI),
          end="", flush=True)


# Start of program...
# Eraze display. i.e. Replace with spaces
print("{}2J".format(CSI), end="", flush=True)

# Set the Console window title bar...
# Note right square bracket - not left bracket - ESC ] 2 ; <string> BEL
# These are OSC 'Operating system command' sequences
# ESC ] 0 ; <string> BEL provide title, plus if saved on desktop it also
# provides name to the desktop icon.
text = "Coloured Rectangles -Call functions to draw rectangles and write text."
print("{}]2;{}{}".format(ESC, text, BEL), end="", flush=True)
print(BEL)
if delay: time.sleep(1)

# draw_rectangle()  # Will pick up default values (1, 1, 80, 24, 97, 40)

# Draw reducing sized rectangles bright foreground and normal background.
draw_rectangle(1, 1, 80, 24, 97, 40)
if delay: time.sleep(delay_duration)
draw_rectangle(2, 2, 78, 22, 91, 41)
if delay: time.sleep(delay_duration)
draw_rectangle(3, 3, 76, 20, 92, 42)
if delay: time.sleep(delay_duration)
draw_rectangle(4, 4, 74, 18, 93, 43)
if delay: time.sleep(delay_duration)
draw_rectangle(5, 5, 72, 16, 94, 44)
if delay: time.sleep(delay_duration)
draw_rectangle(6, 6, 70, 14, 95, 45)
if delay: time.sleep(delay_duration)
draw_rectangle(7, 7, 68, 12, 96, 46)
if delay: time.sleep(delay_duration)
draw_rectangle(8, 8, 66, 10, 97, 40)
if delay: time.sleep(delay_duration)
draw_rectangle(9, 9, 64, 8, 91, 41)
if delay: time.sleep(delay_duration)
draw_rectangle(10, 10, 62, 6, 92, 42)
if delay: time.sleep(delay_duration)
draw_rectangle(11, 11, 60, 4, 93, 43)
if delay: time.sleep(delay_duration)
draw_rectangle(12, 12, 58, 2, 94, 44)
if pause: input("{}{};{}HType Return key to continue"
                .format(CSI, 12, 25))

print("{}2J".format(CSI))  # Eraze display. i.e. Replace with spaces
if delay: time.sleep(delay_duration)
for i in range(12):
    x_axis = 12 - i
    y_axis = 12 - i
    width = 58 + i * 2
    height = 2 + i * 2
    # Forecolour and backcolour are the same using bright colour sets
    f_colour = 90 + i % 8
    b_colour = 100 + i % 8
    draw_rectangle(x_axis, y_axis, width, height, f_colour, b_colour)
    if delay: time.sleep(delay_duration)

# Change the Console window title bar...
# Note right square bracket - not left bracket - ESC ] 2 ; <string> BEL
text = "Coloured Rectangles - Use naming for the colours - See the code."
print("{}]2;{}{}".format(ESC, text, BEL), end="", flush=True)
print(BEL)
if delay: time.sleep(1)

# text = "This is the centre of a 80 x 24 matrix"
# write_text(text, 20, 12, 40, 97)

text = "This is the centre of a 80 x 24 matrix"
write_text(text, 20, 12, "light_magenta", "light_cyan")

time.sleep(2)
text = "This is the centre of a 80 x 24 matrix"
write_text(text, 20, 12, "dark_grey", "bright_yellow")

time.sleep(2)
text = "For how the following messages are created see the programs code"
write_text(text, 10, 12, "white", "black")

# Three methods of issuing the Type Return key to continue...
if pause: input("{}{};{}HType Return key to continue"
                .format(CSI, 13, 25))

# Displaying using write_text()
write_text("Type Return key to continue", 25, 14, 39, "green")
if pause: input()

# To issue pause in one line. colon and then semi-colon delimiters
if pause: write_text("Type Return key to continue", 25, 15, 31, 107); input()

# To issue pause in one line. colon and then semi-colon delimiters
text = "Type Return key to continue"
if pause: write_text(text, 25, 16, "white", "red"); input()

text = "Type Return key to end program"
# Call the console default colours
if pause: write_text(text, 25, 17, "default", "default"); input()

print("{}{};{}H".format(CSI, 24, 1), end="", flush=True)
input("Press Enter key to end program")
sys.exit()

"""
Notes / Links:

http://stackoverflow.com/questions/36760127/how-to-use-the-new-support-for-ansi-escape-sequences-in-the-windows-10-console

http://www.nivot.org/blog/post/2016/02/04/Windows-10-TH2-%28v1511%29-Console-Host-Enhancements

Draw a rectangle using characters from Box Drawing character set.
0x2500 to 0x257f. Single top and single side from box drawing character set.
 ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼

ANSI escape codes invoked by microsoft...
https://msdn.microsoft.com/en-us/library/mt638032(v=vs.85).aspx

Support for Direct Cursor addressing CSI y ; x H
text = "Hello"
print("{}{};{}H{}".format(CSI, 22, 1, text), end="", flush=True)

Enter Line drawing...
print(ESC + "(0") # Enter line drawing

Line drawing that fails under Win10...
print('n') <-- should produce a crossing of lines

Undocumented Win10 output in Line drawing mode...
print("|")  # <-- π
print("}")  # <-- £
print("|")  # <-- ≠
print("a")  # <-- Hash block
print("f")  # <-- degrees symbol
print("y")  # <-- ≤
print("z")  # <-- ≥
print("g")  # <-- plus or minus symbol

Exit line drawing - Return to Ascii
print(ESC + "(B") # Ascii character mode

Note: Better to use characters from the Box Drawing set 0x2500 to 0x257f.

===
Colours
Background
16 colours - Background
49 = Background default
48 = Background Extended - Does not provide and more colours

40 = Black

41 = Dark Red
42 = Dark Green
43 = Dark Yellow
44 = Dark Blue
45 = Dark Magenta
46 = Dark Cyan

47 = Light Grey
100 = Dark Grey

101 = Bright Red
102 = Bright Green
103 = Bright Yellow
104 = Bright Blue
105 = Bright Magenta
106 = Bright Cyan

107 = White

===

Foreground
16 colours - Foreground
38 Foreground extended
39 Foreground default

30 = Black

31 = Dark Red
32 = Dark Green
33 = Dark Yellow
34 = Dark Blue
35 = Dark Magenta
36 = Dark Cyan

37 = Light Grey
90 = Dark Grey

91 = Bright Red
92 = Bright Green
93 = Bright Yellow
94 = Bright Blue
95 = Bright Magenta
96 = Bright Cyan

97 = White

    # Normal Background/foreground and Bright background/foreground Colours
    # Tuples. light_colour and bright_colour are the same.
    COLOUR = (("black", 30, 40),
            ("red", 31, 41),
            ("green", 32, 42),
            ("yellow", 33, 43),
            ("blue", 34, 44),
            ("magenta", 35, 45),
            ("cyan", 36, 46),
            ("light_grey", 37, 47),
            ("grey", 90, 100),
            ("light_red", 91, 101),
            ("light_green", 92, 102),
            ("light_yellow", 93, 103),
            ("light_blue", 94, 104),
            ("light_magenta", 95, 105),
            ("light_cyan", 96, 106),
            ("white", 97, 107),
            ("dark_red", 31, 41),
            ("dark_green", 32, 42),
            ("dark_yellow", 33, 43),
            ("dark_blue", 34, 44),
            ("dark_magenta", 35, 45),
            ("dark_cyan", 36, 46),
            ("dark_grey", 90, 100),
            ("bright_grey", 37, 47),
            ("bright_red", 91, 101),
            ("bright_green", 92, 102),
            ("bright_yellow", 93, 103),
            ("bright_blue", 94, 104),
            ("bright_magenta", 95, 105),
            ("bright_cyan", 96, 106),
           )

To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_23_c.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_23_c.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""
