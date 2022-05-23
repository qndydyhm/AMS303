def read_from_file(file):
    try:
        f = open(file, 'r')
    except FileNotFoundError:
        print("Cannot find file", file)
        exit(-1)
    content = f.read()

    char_list = []
    for char in content:
        if char.isalpha():
            char_list.append(char.upper())
    f.close()

    return char_list


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
