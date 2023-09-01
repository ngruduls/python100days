student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
# result = data_frame.to_dict()
# print(result)
for (index, row) in data_frame.iterrows():
    #print(row.letter)
    pass

dictionary = {row.letter:row.code for (index,row) in data_frame.iterrows()}
print(dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def validate_input(user_text):
    for letter in user_input.upper():
        if letter not in dictionary:
            return False
    return True

user_input = input("Enter a word? \n")
valid_input = validate_input(user_input)

while valid_input == False:
    user_input = input("Enter a word? \n")
    valid_input = validate_input(user_input)

result = [dictionary.get(letter) for letter in user_input.upper()]
print(result)
