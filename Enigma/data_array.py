import json
import os


def read_json(folder, file_name, subdir=''):
    file_path = os.path.join('data', folder, subdir, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def array_convert(root, subdir):
    for path, folders, files in os.walk(root):
        if path == root:
            for folder in folders:
                database.setdefault(folder, {})
        for model in database.keys():
            database[model].setdefault(subdir, {})
            for file in files:
                if os.path.join(model, subdir) in path:
                    reflector = file.split('.')[0]
                    database[model][subdir].setdefault(
                        reflector, read_json(model, file, subdir))
                elif model in path:
                    rotor = file.split('.')[0]
                    database[model].setdefault(rotor, read_json(model, file))
    return database
