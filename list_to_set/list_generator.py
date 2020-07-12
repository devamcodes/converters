"""
Project: list generator

Author: Umang A
Date: 10 July 2020

Description:
-This program prompts input from user to generate a list.

Status: Tested
"""

print("\t\t\t\tList generator\n\n\n")
def generate_list():
    output_list = []
    form_list = 0
    while(form_list != 1):
        list_elements = input("Please enter a list element: ")
        output_list.append(list_elements)
        form_list = int(input("Please enter 1 to form list or enter any value to continue:"))
    print(output_list)
    return output_list

