import random as rnd


def test00():
    t = 100
    print(t)

    for _ in range(t):
        n = rnd.randint(1, 50)
        m = rnd.randint(2, 100)
        print(n,end=" ")
        print(m)

        for _ in range(n):
            s = rnd.randint(0,m)

            print(s, end=" ")

        print()


def test01():
    t = 20
    print(t)

    for _ in range(t):
        n = rnd.randint(1, 800)
        m = rnd.randint(2, 200)
        print(n,end=" ")
        print(m)

        for _ in range(n):
            s = rnd.randint(0,m)

            print(s, end=" ")

        print()


def test02():
    t = 20
    print(t)

    for _ in range(t):
        n = rnd.randint(1, 500)
        m = rnd.randint(2, 400)
        print(n,end=" ")
        print(m)

        for _ in range(n):
            s = rnd.randint(0,m)

            print(s, end=" ")

        print()


def test03():
    t = 20
    print(t)

    for _ in range(t):
        n = rnd.randint(1, 700)
        m = rnd.randint(2, 100)
        print(n,end=" ")
        print(m)

        for _ in range(n):
            s = rnd.randint(0,m)

            print(s, end=" ")

        print()


def test04():
    t = 20
    print(t)

    for _ in range(t):
        n = rnd.randint(1, 1000)
        m = rnd.randint(2, 1000)
        print(n,end=" ")
        print(m)

        for _ in range(n):
            s = rnd.randint(0,m)

            print(s, end=" ")

        print()
        

test04()