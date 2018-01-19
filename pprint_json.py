import json
import sys


def load_data(file_path):
    with open(file_path, "r") as file:
        json_data = json.load(file)
        return json_data


def pretty_print_json(json_data):
    print(json.dumps(json_data, ensure_ascii=False, sort_keys=True, indent=4))


def main(argv):
    file_name = sys.argv[1]
    input_data = load_data(file_name)
    pretty_print_json(input_data)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            main(sys.argv[1])
        except FileNotFoundError:
            print("File %s not found" % sys.argv[1])
        except json.decoder.JSONDecodeError:
            print("JSON is not valid")
    else:
        print("Please, put a file name as a parameter. For example: 'python pprint_json.py in.json' ")
