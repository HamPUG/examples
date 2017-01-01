#!/usr/bin/env python3
#
import sys
import math
import time

_description_ = """
    Locate prime numbers. Use recursive division up to the square root of
    the integer being tested for being a prime
    int(math.sqrt(integer_under_test))
    Provide heading with number of primes located
    Include the time taken to perform the calculations
    Procedural programming style.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_21_d.py

start_prompt = 0
range_prompt = 100


def main(start_integer=start_prompt, range_integer=range_prompt):
    "Locate prime numbers. Call functions for input and report generation."
    prime_list = []

    # Get the start and range of integers in which to locate prime numbers.
    start_integer = get_positive_integer("Enter start integer", start_integer)
    range_integer = get_positive_integer("Enter range", range_integer)

    # For each integer call function to check if it is a prime. Time this.
    start_time = time.time()
    for i in range(start_integer, start_integer + range_integer + 1):
        is_prime = locate_prime(i)
        if is_prime:
            prime_list.append(i)
    total_time = time.time() - start_time

    # Generate the reports.
    generate_report_1(start_integer, range_integer, prime_list)
    generate_report_2(total_time)
    input("\nType Return key to continue...")
    generate_report_3(prime_list)


def locate_prime(integer):
    "Return True if an integer is a prime and a count of the modulo operations"
    max_value = int(math.sqrt(integer))
    is_prime = True
    for j in range(2, max_value + 1):
        if integer % j == 0:
            is_prime = False
            return is_prime
        else:
            continue
    return is_prime


def generate_report_1(start_int, range_int, prime_list):
    "Report the start, range and primes located."
    print("\n{} prime numbers in the range {} to {}"
          .format(len(prime_list), start_int, start_int + range_int))


def generate_report_2(tot_time):
    "Report time"
    print("\nTotal time to locate all prime numbers: {:g} seconds"
          .format(tot_time))


def generate_report_3(prime_list):
    "Output the list of prime numbers, and provide a sum total of the primes"
    sum_of_prime = 0
    for prime in prime_list:
        print("{: >20}".format(prime))
        sum_of_prime = sum_of_prime + prime
    print("\nThe sum of these {} prime numbers is: {}"
          .format(len(prime_list), sum_of_prime))


def get_positive_integer(query="Enter a positive integer", prompt=0):
    "Return a positive integer from the console"
    while True:
        response = input("{} [{}]: ".format(query, prompt))
        if not response:
            response = prompt
        try:
            response = abs(int(response))
            return response
        except ValueError as e:
            print("Value Error: {}".format(e))
            print("Please re-enter...")
            continue

if __name__ == "__main__":
    print("Prime number locater... ")

    for index, item in enumerate(sys.argv):
        if "-s=" in item:
            start_list = item.split("=")
            if len(start_list) > 1:
                start_prompt = start_list[1]

        if "-r=" in item:
            range_list = item.split("=")
            if len(range_list) > 1:
                range_prompt = range_list[1]

    main(start_prompt, range_prompt)
print("\nPrime number locater program ended.")
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_21_d.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_21_d.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""
