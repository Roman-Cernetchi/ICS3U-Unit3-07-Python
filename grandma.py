#!/usr/bin/env python3
#
# Created by: Roman Cernetchi
# Created on: December 2020
# This program checks if a person is old enough

import math


def main():
    # This function checks the persons age

    # Input

    participants_age = input("Enter your age: ")
    print("")

    # process
    try:
        if int(participants_age) >= 25 and int(participants_age) <= 50:
            # Output
            print("You are old enough")
        else:
            print("You are not old enough")
    except Exception:
        print("This was not an integer")


if __name__ == "__main__":
    main()
