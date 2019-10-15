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
        huhuhu = int(user_input)
        if huhuhu >= 25 and huhuhu <= 40:
            # output
            print("you can date her (:")
        else:
            print("you can't date her because you are too old :(")
    except Exception:
        print("This is not an integer")
    finally:
        print("Thank you for wasting you time to request a date")


if __name__ == "__main__":
    main()
