import pickle
import sys
from collections import Counter

arg = sys.argv[1]
name = sys.argv[2].split(".")[0]


def huffman_code(text):
    d = dict(Counter(text).most_common())

    def tree(d):
        m = Counter(d).most_common()[:-3:-1]
        d.pop(m[0][0])
        d.pop(m[1][0])
        d[(m[0], m[1])] = m[0][1] + m[1][1]
        if len(d) > 1:
            return tree(d)
        else:
            return Counter(d).most_common()[0]

    tree = tree(d)
    k = {}

    def kod(t, ch=''):
        nonlocal k
        e1, e2 = t[0], t[1]
        if type(e1) is tuple and type(e2) is int:
            kod(e1, ch)
        elif type(e1) is tuple and type(e2) is tuple:
            kod(e1, ch + '0')
            kod(e2, ch + '1')
        elif type(e1) is str:
            k[e1] = ch

        return k

    return kod(tree)


def encryption(text_in, slov):
    promezh = ''

    for char in text_in:
        promezh += slov[char]

    a = 8 - len(promezh) % 8
    promezh = promezh + "0" * a

    string = ''
    strings = []

    for i in promezh:
        if len(string) == 8:
            strings.append(string)
            string = ''
        string += i

    strings.append(string)

    result = bytes([int(j, 2) for j in strings])

    return result, bytes([a])


def dec(data):
    slov, text = data.split("Rasdilenie".encode())
    slov = pickle.loads(slov)
    slov = {j: i for i, j in slov.items()}

    dob = text
    text = ''.join([bin(i)[2:].rjust(8, '0') for i in text[1:]])

    result = ""
    string = ""

    for i in text[0:-dob[0]]:
        if string in slov:
            result += slov[string]
            string = i
        else:
            string += i
    result += slov[string]

    return result


match arg:
    case "-e":
        with open(f"{name}.txt", "r") as f:
            t = f.read()
        slovar = huffman_code(t)
        with open(f"{name}.par", "wb") as file:
            file = open(f'{name}.par', "wb")
            file.write(pickle.dumps(slovar))
            text, dob = encryption(t, slovar)
            file.write('Rasdilenie'.encode())
            file.write(dob + text)

    case "-d":
        with open(f"{name}.par", "rb") as f:
            text = f.read()
            result_text = dec(text)
        file = open(f"{name}.txt", "w")
        file.write(result_text)
        file.close()
