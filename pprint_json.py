import json
import sys


def load_data(file_path):
    try:
        with open(file_path, "r") as file:
            json_data = json.load(file)
            return json_data
    except FileNotFoundError:
        print("File %s not found!" % file_name)
        return None
    except json.decoder.JSONDecodeError:
        print("JSON is not valid!")
        return None


def pretty_print_json(json_data):
    print(json.dumps(json_data, ensure_ascii=False, sort_keys=True, indent=4))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        input_data = load_data(file_name)
        if input_data:
            pretty_print_json(input_data)
    else:
        print("Please, put a file name as a parameter. For example: 'python pprint_json.py in.json' ")
