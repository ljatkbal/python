# -*- coding: utf8 -*-
import random
import json

print("Lest begin coding in Python !!!")

### The target is :
#       define two JSon files that contain the characters and the quotes
#       print quote of random character from the file
def get_data_from_json_file(json_file,key):
    values = []
    # load the file
    with open(json_file) as f:
        data = json.load(f)
    # load the file into an array
    for entry in data:
        values.append(entry[key])
    # return the array
    return values

# random fonction definition
def get_random_item(my_list):
    random_item = random.randint(0, len(my_list) - 1)
    return my_list[random_item]

def message(character,quote):
    print("{charac} has say : {quo}".format(quo=quote,charac=character))

# make a choice
user_answer = input('Tape your choice : ')

# show a quote randomly in a while loop
while user_answer != "B":
    message(get_random_item(get_data_from_json_file("characters.json","character")),
            get_random_item(get_data_from_json_file("quotes.json","quote")))
    user_answer = input('Tape your choice : ')

