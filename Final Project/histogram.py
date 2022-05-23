import sys
from IC_calculator import get_max_ic
from project_helper import read_from_file, Color, ALPHABET


def print_histogram(char_list, length):
    char_lists = [[] for _ in range(length)]
    ans_lists = [[] for _ in range(length)]
    for i in range(len(char_list)):
        char_lists[i % length].append(char_list[i])
    for i in range(len(char_lists)):
        for char in ALPHABET:
            print("|", end="")
            print(f"{char:>{3}}", end=" ")
        for char in ALPHABET:
            print("|", end="")
            print(f"{char:>{3}}", end=" ")
        print("|")

        for j in range(26):
            num = char_lists[i].count(ALPHABET[j])
            print("|", end="")
            if num == 0:
                print(Color.RED + Color.BOLD + '████', end="" + Color.END)
                ans_lists[i].append(True)
            else:
                print(f"{num:>{3}}", end=" ")
                ans_lists[i].append(False)
        for j in range(26):
            num = char_lists[i].count(ALPHABET[j])
            print("|", end="")
            if num == 0:
                print(Color.RED + Color.BOLD + '████', end="" + Color.END)
            else:
                print(f"{num:>{3}}", end=" ")
        print("|")
        print("------------------------------------")

    for i in range(length):
        for j in range(i + 1, length):
            print("Possible shifting between %d and %d" % (i + 1, j + 1))
            if i == 2 and j == 3:
                pass
            for l in range(26):
                num = 0
                for k in range(26):
                    if ans_lists[i][k] and ans_lists[j][(k + 26 - l) % 26]:
                        num += 1
                if num >= 4:
                    print("shift by", Color.RED + Color.BOLD + "%d" % l + Color.END, end=", with ")
                    if num <= 6:
                        print(Color.RED + Color.BOLD + "%d" % num, Color.END + "common voids")
                    else:
                        print(Color.GREEN + Color.BOLD + "%d" % num, Color.END + "common voids")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: %s <path to file>" % sys.argv[0])
        exit(-1)
    charlist = read_from_file(sys.argv[1])
    print_histogram(charlist, get_max_ic(charlist, 3, 8)[0])
