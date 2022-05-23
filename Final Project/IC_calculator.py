import sys
from project_helper import read_from_file, Color, ALPHABET


def IC_calculate_helper(char_list):
    ans = 0.0
    for char in ALPHABET:
        num = char_list.count(char)
        ans += num * (num - 1)

    return ans / (len(char_list) * (len(char_list) - 1))


def IC_calculate(char_list, length):
    char_lists = [[] for _ in range(length)]
    for i in range(len(char_list)):
        char_lists[i % length].append(char_list[i])

    print("IC for length %d is " % length, end="")
    ans = 0.0
    for i in range(length):
        ic = IC_calculate_helper(char_lists[i])
        print("%.5f" % ic, end=", ")
        ans += ic
    print("average is " + Color.BOLD + Color.GREEN + "%.5f" % (
                ans / length) + Color.END)
    print("------------------------------------")
    return ans / length


def get_max_ic(char_list, start, end):
    ans = (0, 0)
    for i in range(start, end):
        ic = IC_calculate(char_list, i)
        if ic > ans[1]:
            ans = (i, ic)

    print("The highest probability length is", end=" ")
    print(Color.RED + Color.BOLD + "%d" % ans[0] + Color.END, end=" ")
    print("with IC" + Color.RED + Color.BOLD, "%.5f" % ans[1] + Color.END)
    print("------------------------------------")
    return ans


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: %s <path to file>" % sys.argv[0])
        exit(-1)
    charlist = read_from_file(sys.argv[1])
    get_max_ic(charlist, 4, 6)
