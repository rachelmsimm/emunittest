from exceptions import DuplicateNameOrKeyException

import json

def add(demo):
    try:
        check_for_duplicates(demo.name, demo.key)
        insert_demo(demo)
    except DuplicateNameOrKeyException:
        print(f"Duplicate name or key; names and keys must be unique.")

    return

def get_existing_demos():
    with open("../demo_list.json") as json_file:
        data = json.load(json_file)
        
        return data

def check_for_duplicates(name, key):
    demos = get_existing_demos()
    print(f"demos from file: {demos}")

    for demo in demos:
        if demo['name'] == name or demo['key'] == key:
            raise DuplicateNameOrKeyException
        
    return

def insert_demo(new_demo):
    demos = get_existing_demos()
    demos.append(new_demo.__dict__)
    with open("../demo_list.json", "w") as outfile:
        outfile.write(json.dumps(demos, indent=4))
    
    return