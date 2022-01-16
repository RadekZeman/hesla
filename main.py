

def listtostring(list):
    str = ""
    for i in list:
        str += i
    return(str)


def level1(a, delka1, delka2):
    z = 0
    y = 0
    x = 0
    for i in a[delka1: delka2]:
        if 65 <= i <= 90:
            z = 1
        if 97 <= i <= 122:
            y = 1
        if z == 1 and y == 1:
            x = 1
    return(x)


def level(heslo):
    a = []
    b = heslo.split()
    delky = []
    print(b)
    for i in b:
        print(i)
        for j in i:
            z = ord(j)
            print(z)
            a.append(z)
        delky.append(len(i))
    print(a)
    print(delky)
    x = []
    c = 0
    d = delky[0]
    e = -1
    while e < len(delky) - 1:
        x1 = level1(a, c, d)
        e = e + 1
        c = c + delky[e]
        d = d + delky[e]
        print(x1)
        x.append(x1)
    print(x)
    return(x)


if __name__ == '__main__':
    f = open("zadanihesel", "r")
    a = [f.read()]
    for i in a:
        print(i)
        x = level(i)
    a = listtostring(a)
    b = a.split()
    print(b)
    c = 0
    e = []
    for i in b:
        d = (f"{i} {x[c]} ")
        c = c + 1
        e.append(d)
    e = listtostring(e)
    f = open("hesla.txt", "w")
    f.write(e)
    f = open("hesla.txt", "r")
    print(f.read())
