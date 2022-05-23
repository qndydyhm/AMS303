import sys
from project_helper import read_from_file


def decode(ciphertexts, passphrase1, passphrase2):
    alphabet = ['' for _ in range(26)]

    index = 0
    for i in range(len(passphrase1)):
        if passphrase1.find(passphrase1[i]) == i:
            alphabet[index] = passphrase1[i]
            index += 1

    length = index

    for i in range(26):
        if passphrase1.find(chr(ord('A') + i)) == -1:
            alphabet[index] = chr(ord('A') + i)
            index += 1

    alphabet1 = ['' for _ in range(26)]
    for i in range(26):
        j = i // length
        k = i % length
        index = 0
        for l in range(k):
            index += (26 // length + 1) if l < 26 % length else (26 // length)
        index += j
        alphabet1[index] = alphabet[i]

    count = 0
    ans = ""
    for char in ciphertexts:
        if char == ' ':
            print(" ", end='')
            continue
        ans += alphabet1[(ord(char) - ord(passphrase2[count % len(passphrase2)]) + 26) % 26]
        count += 1
    return ans


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: %s <path to file>" % sys.argv[0])
        exit(-1)
    print(decode(read_from_file(sys.argv[1]), "HANDSOME", "HOLLY"))
