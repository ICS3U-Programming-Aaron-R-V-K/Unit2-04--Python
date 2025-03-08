#!/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: March 3, 2025
# This code calculates the perimeter and area of a rectangle

import math


def main():
    # get radius length with user input
    rad = float(input("Enter the radius of a circle (cm): "))

    # calculations to get the circumference and area
    circ = math.pi * 2 * rad
    area = math.pi * (rad**2)

    # display the results of the calculations with two decimal places
    print(f"The area of the circle is: {area:.2f}")
    print(f"The perimeter (circumference) of the circle is: {circ:.2f}")


if __name__ == "__main__":
    main()
