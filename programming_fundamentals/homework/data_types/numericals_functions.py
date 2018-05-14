#!/usr/bin/env python
"""
This module contains tasks related to data types in Python.
Please read docstrings and complete the functions.
All functions should returns results of described type.
"""
__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

TEST_NUMBER = 42


def decimal_to_binary(n):
    """
    Implement this function!
    This function should convert decimal(integer) into binary.

    Args:
        n (int) - integer number to convert.

    Returns:
        int - integer number of binary representation for enterd n.
    """


    return int(bin(n)[2:])
  
#for checking user_input = int(input())
#print(decimal_to_binary(user_input))


def binary_to_decimal(n):
    """
    Implement this function!
    This function should convert binary into integer(decimal).

    Args:
        n (int) - binary representation of a number.
 
    Returns:
        int - decimal representation of a proper number.
    """
 
    #n = input()
    decimal = int(str(n), 2)
    return decimal
  


def storage(data_storage = None):
    # Your function should return list with added `data` value
    # into passed list into function or just `data` value in empty list.
    # Example:
    # storage([]) -> ["data"]
    # storage() -> ["data"]
    # storage(["test"]) -> ["test", "data"]

    # Change parameters in function for needed.
    # Also you is able to add some additional code here if needed.
    if (data_storage is None):
        data_storage = []

    # DON'T MODIFY THESE LINES.
    data_storage.append("data")
    return data_storage
# for checking :
# print(storage(["hey"]))


def handle_exceptions(user_number):
    # Write a function which uses `user_number` as a value entered by user.
    # If their number is higher than `TEST_NUMBER`, return `Yey! My number is higher!`,
 
 try:
   if int(user_number) > TEST_NUMBER:
      return 'Yey! My number is higher!'
   else: 
      return 'Wow! My number is lower.'
 except:
   return 'not a number'
 # return `Wow! My number is lower.` otherwise.
    # Handle possible exceptions.

    # ADD YOUR CODE HERE.
 
