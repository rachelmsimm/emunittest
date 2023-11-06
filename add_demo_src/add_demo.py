import json

NAME_INDEX = 0
KEY_INDEX = 1

def add(demo):
    check_for_duplicates(demo.name, demo.key)
    insert_demo(demo)
    return

def get_existing_demos():
    with open("../demo_list.json") as json_file:
        data = json.load(json_file)
        return data

def check_for_duplicates(name, key):
    demos = get_existing_demos()
    print(demos)

    try:
        for demo in demos:
            if demo[NAME_INDEX] == name or demo[KEY_INDEX] == key:
                raise Exception("Duplicate name or key; names and keys must be unique.")
        return
    except Exception as e:
        print(f"An exception occurred: {e}")

def insert_demo(new_demo):
    demos = get_existing_demos()
    new_demo = json.dumps(new_demo.__dict__)
    demos.append(new_demo)
    print(demos)
    with open("../demo_list.json", "w") as outfile:
        outfile.write(json.dumps(demos, indent=4))
    return