

def listtostring(list):
    str = ""
    for i in list:
        str += i
    return(str)


def level1(a, delka1, delka2):
    print(f"od {delka1} do {delka2}")
    parametr = 4
    if parametr < 4:
        b = parametr
    else:
        b = 4
    velkapismena = 0
    pismena = 0
    cisla = 0
    znaky = 0
    x = 0
    for i in a[delka1: delka2]:
        if 65 <= i <= 90:
            velkapismena = 1
        if 97 <= i <= 122:
            pismena = 1
        if 48 <= i <= 57:
            cisla = 1
        if 32 <= i < 48 or 57 < i < 65 or 90 < i < 97 or 122 < i <= 126:
            znaky = 1
        if velkapismena == 1 and pismena == 1:
            if b <= velkapismena + pismena + cisla + znaky:
                x = 2
            else:
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
    g = 1
    f = 0
    for i in a:
        print(f"{f}: {i}")
        f = f + 1
    while g <= len(delky):
        print(f"g = {g}")
        x1 = level1(a, c, d - 1)
        e = e + 1
        c = c + delky[e]
        if g < len(delky):
          d = d + delky[g]
        g = g + 1
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
        d = (f"{i} {x[c]}\n")
        c = c + 1
        e.append(d)
    e = listtostring(e)
    f = open("hesla.txt", "w")
    f.write(e)
    f = open("hesla.txt", "r")
    print(f.read())
