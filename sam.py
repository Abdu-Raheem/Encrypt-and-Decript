import sys

catch = []
encrypted = []
words = []
letters = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



def encrypt(a, text, n, opt):
    i = 0
    while n > i:
        words.append(text[i])
        i = i + 1
    i = 0
    for k in range(n):
        for x in range(53):
            if letters[x] == words[i]:
                catch.append(x)
        i = i + 1

    for x in range(0, n):
        r = int(a / 53)
        r = r * 53
        r = a - r
        l = catch[x] + r
        if l < 53:
            el = letters[l]
            encrypted.append(el)
        elif l >= 53:
            h = l - 53
            ele = letters[h]
            encrypted.append(ele)
    if opt == 1:
        print('\nEncrypted code: ')
        for x in range(len(encrypted)):
            print(encrypted[x], end='')
    elif opt == 2:
        print('\nDecrypted code: ')
        for x in range(len(encrypted)):
            print(encrypted[x], end='')
    list.clear(encrypted)


def main():
    n = 1
    while n != 0:
        print("\nselect the option")
        opt = int(input('1)Encrypt\n2)Decrypt\n'))
        if opt == 1:
            text = input("Enter the text: ")
            a = int(input("enter the times to be scipher: "))
            n = len(text)
            encrypt(a, text, n, opt)
        elif opt == 2:
            text = input("Enter the text: ")
            a = int(input("enter the times to be scipher: "))
            n = len(text)
            a = a - 3
            encrypt(a, text, n, opt)
        else:
            sys.exit(0)

main()
