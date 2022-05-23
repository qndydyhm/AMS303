import sys
from shift import shift
from project_helper import read_from_file, ALPHABET

KEY = "HOLLY"


def analyze(char_list):
    dictionary = [{} for _ in range(26)]
    print(char_list)
    maximum = ("", 0)
    for i in range(len(char_list)):
        index = ord(char_list[i]) - ord('A')
        string = ""
        if i == 0:
            string += "-"
        else:
            string += char_list[i-1]
        string += char_list[i]
        if i == len(char_list) - 1:
            string += '-'
        else:
            string += char_list[i+1]
        keypair = dictionary[index].get(string)
        if keypair is None:
            num = 1
        else:
            num = keypair + 1
        if num > maximum[1]:
            maximum = (string, num)
        dictionary[index][string] = num

    for i in range(26):
        print(ALPHABET[i] + ":", end=" ")
        for key, value in dictionary[i].items():
            for j in range(value):
                print(key, end=" ")
        print()
    print("------------------------------------------")
    print("Most frequency pattern is", maximum[0])
    print("It appears %d times" % maximum[1])


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: %s <path to file>" % sys.argv[0])
        exit(-1)
    charlist = read_from_file(sys.argv[1])
    shifted = shift(charlist, KEY)
    analyze(shifted)
