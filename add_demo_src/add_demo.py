import json

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

    for demo in demos:
        if demo["name"] == name or demo["key"] == key:
            raise Exception("Duplicate name or key")
    return

def insert_demo(demo):
    demos = get_existing_demos()
    demos.append(demo)
    print(demos)
    with open("../demo_list.json", "w") as outfile:
        outfile.write(json.dumps([demos], indent=4))
    return