# Use the keyword method for starting the List comprehension and fill in the relevant parts.
# First, you will need to read from the files and create a list using the lines in the files.
# This method will be really useful: https://www.w3schools.com/python/ref_file_readlines.asp
# Remember you can check if a value exists in a list using the in keyword. https://www.w3schools.com/python/ref_keyword_in.asp
# Remember you can convert a string to an int using the int() method. https://www.w3schools.com/python/ref_func_int.asp

with open("file1.txt", "r") as file:
    file_list1 = file.readlines();

with open("file2.txt", "r") as file:
    file_list2 = file.readlines();

file_list1 = [int(n.strip()) for n in file_list1]
file_list2 = [int(n.strip()) for n in file_list2]

common_list = [n for n in file_list1 if n in file_list2]
print(common_list)