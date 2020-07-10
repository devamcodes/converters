"""
Explain how output_list name will affect this program if it is used as global variable
"""
from list_generator import generate_list
from  list_to_set import convert_list_to_set

my_list = []
my_list = generate_list()
my_set = convert_list_to_set(my_list)


