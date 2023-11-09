import json

def add(new_demo):
    valid_key_and_name = key_and_name_are_valid(new_demo.name, new_demo.key)
    if (valid_key_and_name):
        insert_demo(new_demo)

    return

def get_existing_demos():
    with open("../demo_list.json") as json_file:
        data = json.load(json_file)
        
        return data

def key_and_name_are_valid(name, key):
    demos = get_existing_demos()
    are_valid = True

    for demo in demos:
        if demo['name'] == name or demo['key'] == key:
            print(f"Failed to add demo with name: {name} and key: {key}." +
                  "The name or key of the demo you are trying to add already exists. Names and keys must be unique.")
            are_valid = False
            break
        
    return are_valid

def insert_demo(new_demo):
    demos = get_existing_demos()
    demos.append(new_demo.__dict__)
    with open("../demo_list.json", "w") as outfile:
        outfile.write(json.dumps(demos, indent=4))
    
    return