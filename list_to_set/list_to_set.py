"""
Project: converter_list_to_set

Author: Umang A, Devam A
Date: 10 July 2020

Modified: None

Description:
-This mofule contains function which converters a user input list into set.
Status: Tested
"""

def convert_list_to_set(input_list):
    output_set = set()
    for elements in input_list:
        output_set.add(elements)
    else:
        print("List converted!")
    print(output_set)
    return output_set
