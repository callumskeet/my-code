import string
import os
import json


# credit to reddit user /u/tangerinelion 
def read_json(folder, file_name, subdir=''):
    file_path = os.path.join('data', folder, subdir, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def make_db(pardir, subdir, database={}):
    for root, dirs, files in os.walk(pardir):
        if root == pardir:
            for folder in dirs:
                database.setdefault(folder, {})
        for model in database.keys():
            database[model].setdefault(subdir, {})
            for file in files:
                if os.path.join(model, subdir) in root:
                    reflector = file.split('.')[0]
                    database[model][subdir].setdefault(reflector, read_json(model, file, subdir))
                elif model in root:
                    rotor = file.split('.')[0]
                    database[model].setdefault(rotor, read_json(model, file))
    return database


# Alphabet
ab_list = list(string.ascii_uppercase)

# Rotor database
database = make_db('data', 'reflectors')
