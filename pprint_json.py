import json
import sys


def load_data(file_path):
    try:
        with open(file_path, "r") as file:
            json_data = json.load(file)
            return json_data
    except (FileNotFoundError, json.decoder.JSONDecodeError) as err:
        return err


def pretty_print_json(json_data):
    print(json.dumps(json_data, ensure_ascii=False, sort_keys=True, indent=4))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        input_data = load_data(file_name)
        print(type(input_data))
        if type(input_data) == dict:
            pretty_print_json(input_data)
        elif type(input_data) == FileNotFoundError:
            print("File %s not found" % sys.argv[1])
        elif type(input_data) == json.decoder.JSONDecodeError:
            print('JSON is not valid')
    else:
        print("Please, put a file name as a parameter. For example: 'python pprint_json.py in.json' ")
