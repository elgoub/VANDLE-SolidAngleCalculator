#!/usr/bin/env python3
# ------------------------------------------------------------------------------
#  Calculator for solid angle of a rectangular solid at a given distance in
#  centimeters.
#
#  Author: S. V. Paulauskas
#  Date: July 30, 2016
# ------------------------------------------------------------------------------
import sys
import math


# Calculate the percent of 4pi that we cover
def calc_percent_four_pi(o):
    return o / 4 / math.pi


# Define a function to calculate the coverage of an array
def calc_array_coverage(o):
    return number_of_bars * o


# Define a function to calculate the position along x
def calc_position(x):
    return x / 2 / distance_to_bars


# Define a function to calculate the solid angle coverage in sr
def calc_omega(l, w):
    numerator = 1 + calc_position(l) ** 2 + calc_position(w) ** 2
    denominator = (1 + calc_position(l) ** 2) * (1 + calc_position(w) ** 2)
    return 4.0 * math.acos(math.sqrt(numerator / denominator))


# Print a help statement
def print_help():
    print("Usage: python sacalc.py <Bar Type> <Distance to Bar (cm)> "
          "<Number of Bars>")


# The minimum number of arguments we need is 4
min_num_args = 4
# Figure out how many command line arguments that we have
argc = len(sys.argv)

# Print the help statement if we do not have the right number of args
if argc != min_num_args:
    print_help()
    exit(1)

# Set the bar type based off of cmd line input 1
bar_type = sys.argv[1]
# Set the distance to the bars from cmd line input 2
distance_to_bars = float(sys.argv[2])
# Set the number of bars in the array from cmd line input 3
number_of_bars = float(sys.argv[3])

# Set the length and width of the different bars
length = 0
width = 0
if bar_type == "small":
    length = 60
    width = 3
elif bar_type == "medium":
    length = 120
    width = 6
elif (bar_type == "large") | (bar_type == "big"):
    length = 200
    width = 5
else:
    print("Unknown bar type " + bar_type + ". Known types:small, medium, "
                                           "large/big")
    exit(0)

omega = calc_omega(length, width)
print("---------- Single Bar ----------")
print("Geometric Coverage (sr) =", omega)
print("Geometric Efficiency(abs)", calc_percent_four_pi(omega))
print("")

print("---------- Array Coverage ----------")
print("Geometric Coverage (sr) =", calc_array_coverage(omega))
print("Geometric Efficiency(abs)",
      calc_percent_four_pi(calc_array_coverage(omega)))
print("")
