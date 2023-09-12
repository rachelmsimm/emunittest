import json

def add(demo):
    check_for_duplicates(demo.name, demo.key)
    json_obj = create_entry(demo)
    insert_entry(json_obj)
    return

def get_existing_demos():
    with open("demo_list.json") as json_file:
        data = json.load(json_file)
        return data

def check_for_duplicates(name, key):
    demos = get_existing_demos()

    for demo in demos:
        if demo["name"] == name or demo["key"] == key:
            raise Exception("Duplicate name or key")
    return

def create_entry(demo):
    entry = json.dumps(demo.__dict__)
    return entry

def insert_entry(json_obj):
    with open("demo_list.json", "w") as outfile:
        outfile.write(json_obj)
    return