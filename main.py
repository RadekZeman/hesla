def zmena(a):
    b = []
    str1 = ""
    for i in a:
        b = ((chr(i)))
        str1+=b
    return(str1)

def level(heslo):
    a = []
    for i in heslo:
        b = ord(i)
        print(b)
        a.append(b)
    print(a)
    c = []
    d = []
    z = c
    for j in a:
        if j == 10:
            z = d
        else:
            z.append(j)
    print(c, d)
    xc = 0
    w = 0
    v = 0
    for k in c:
        if 65 <= k <= 90:
            w = 1
        if 97 <= k <= 122:
            v = 1
        if w == 1 and v == 1:
            xc = 1
    xd = 0
    w1 = 0
    v1 = 0
    for l in d:
        if 65 <= l <= 90:
            w1 = 1
        if 97 <= l <= 122:
            v1 = 1
        if w1 == 1 and v1 == 1:
            xd = 1
    print(xc, xd)
    x = [xc, xd]
    print(x)
    return(x,c,d)


if __name__ == '__main__':
    f = open("zadanihesel", "r")
    a = [f.read()]
    for i in a:
        print(i)
        x,b,c = level(i)
    f = open("hesla.txt", "w")
    d = zmena(b)
    e = zmena(c)
    f.write(f"{(d)}_{x[0]} {(e)}_{x[1]}")
    f = open("hesla.txt", "r")
    print(f.read())
