from demo import Demo

import json

def add(demo):
    #demo = Demo("name", "key", "url")
    check_for_duplicates(demo.name, demo.key)
    json_obj = create_entry(demo)
    insert_entry(json_obj)
    return

def get_existing_demos():
    with open("demo_list.json") as json_file:
        data = json.load(json_file)
        print(data)
        return data

def check_for_duplicates(name, key, demos=get_existing_demos()):
    # searches for name and key in json file
    # if found, throw error
    # else return true
    return

def create_entry(demo):
    entry = json.dumps(demo.__dict__)
    print(entry)
    return entry

def insert_entry(json_obj):
    with open("demo_list.json", "w") as outfile:
        outfile.write(json_obj)
    return