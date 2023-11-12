#!/usr/bin/env python3
# Created By: Ishami Sebgoya
# Date: October 5, 2023
# This program asks the user to identify whether a number is positive, negative, or zero

def main():
    user_num = float(input("Enter a number: "))  # Assuming you want the user to input a number

    if user_num > 0:
        print(f"{user_num} is a positive number")
    elif user_num < 0:
        print(f"{user_num} is a negative number")
    else:
        print("The number is 0")

if __name__ == "__main__":
    main()
