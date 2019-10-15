#!/usr/bin/env python3

# Created by: Khang Le
# Created on: Sep 2019
# This program guesses random number

import random


def main():
    # this function guesses random number

    # input
    user_input = input("Enter a number: ")
    print("")

    # process

    try:
        nb1 = random.randint(1, 10+1)
        integer_as_number = int(user_input)
        if nb1 == user_input:
            # output
            print("it is correct!")
        else:
            print("it is wrong")
            print("The number is {}".format(nb1))
    except Exception:
        print("This is not an integer")
    finally:
        print("niceee")


if __name__ == "__main__":
    main()
