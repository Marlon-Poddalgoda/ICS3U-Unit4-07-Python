#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on December 2020
# This program displays every integer from 1000-2000
#      using 1 loop and an if statement


def main():
    # This function displays every integer from 1000-2000
    #      using 1 loop and an if statement

    print("This program displays every integer from "
          "1000 to 2000.")

    # variable declarations
    loop_counter = 0

    # process
    for loop_counter in range(1000, 2000 + 1):
        if loop_counter % 5 == 0:
            print("{0}  ".format(loop_counter))
        else:
            print("{0}  ".format(loop_counter), end="")


if __name__ == "__main__":
    main()
