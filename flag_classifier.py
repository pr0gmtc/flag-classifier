from sklearn import tree
import numpy as np
import csv

params_descs = ['red ', 'green ', 'blue ', 'gold ', 'white ', 'black ', 'orange ', 'colours ', 'number of vertical bars in the flag: ', 'number of horizontal stripes in the flag: ', 'number of circles: ', 'number of upright crosses: ', 'number of diagonal crosses: ', 'number of quartered sections: ', 'number of sun or star symbols: ', '1 if a crescent moon symbol present, else 0: ', '1 if any triangles present, 0 otherwise: ', '1 if an inanimate image present (e.g., a boat), otherwise 0: ', '1 if an animate image (e.g., an eagle, a tree, a human hand) present, 0 otherwise: ', '1 if any letters or writing on the flag (e.g., a motto or slogan), 0 otherwise: ']
input_params = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#data
_params = []
_names = []
with open('flag_data_raw_mod.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
    for row in reader:
        _params.append(row)

with open('names.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
    for row in reader:
        _names.append(row)


# Classifier
clf_tree = tree.DecisionTreeClassifier()

# Training the model
clf_tree.fit(_params, _names)

print("Enter colors: ")

clrs_list = input().split(" ")

def strings_to_numbers():
    switcher = {
        "red": 0,
        "green": 1,
        "blue": 2,
        "gold": 3,
        "yellow": 3,
        "white": 4,
        "black": 5,
        "orange": 6,
    }
    for x in clrs_list:
        if x in switcher:
            input_params[switcher.get(x, 0)] = 1
            input_params[7] = input_params[7] + 1

strings_to_numbers()

for x in range(8, len(params_descs)):
    param = input(params_descs[x])
    if param != "":
        input_params[x] = param

prediction = clf_tree.predict([input_params])
print(prediction)