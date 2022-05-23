import sys
from project_helper import read_from_file

KEY = "VOLLY"


def shift(char_list, key):
    ans = ""
    for i in range(len(char_list)):
        char = chr((ord(char_list[i]) - ord('A') + 26 - (ord(key[i % len(key)]) - ord('A'))) % 26 + ord('A'))
        ans += char
    return ans


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: %s <path to file>" % sys.argv[0])
        exit(-1)
    char_list = read_from_file(sys.argv[1])
    print(shift(char_list, KEY))
