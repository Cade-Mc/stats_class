from math import factorial as fac


def dperms():
    Factorial = 1
    Factorial2 = 1
    Factorial3 = 1
    N = 1
    count = 0
    n = input("How many items total?: ")
    fact = input("How many items of category 1 are there?: ")
    fact2 = input("How many items of category 2 are there? 0 if None: ")
    fact3 = input("How many items of category 3 are there? 0 if None: ")
    n = eval(n)
    fact = eval(fact)

    for x in range(1, fact + 1):
        Factorial = Factorial * x
        count += 1

    for x in range(1, n + 1):
        N = N * x
        count += 1

    if fact2 is 0 or None:
        pass
    else:
        fact2 = eval(fact2)
        for x in range(1, fact2 + 1):
            Factorial2 = Factorial2 * x
            count += 1
        answer = N / (Factorial * Factorial2)
        print(f"Two Facts: {answer}")

    if fact3 is 0 or None:
        pass
    else:
        fact3 = eval(fact3)
        for x in range(1, fact3 + 1):
            Factorial3 = Factorial3 * x
            count += 1
            answer = N / Factorial * Factorial * Factorial3
            print(f"Three Facts: {answer}")
            break

    if fact2 == 0 and fact3 == 0:
        answer = N / Factorial
        print(answer)
    else:
        pass


dperms()


def probDperms():
    cat1 = input("How many in category 1?: ")
    cat2 = input("How many in category 2?: ")
    cat3 = input("How many in category 2? 0 if None: ")
    random = input("How many were chosen at random?: ")
    try:
        cat1 = int(cat1)
        cat2 = int(cat2)
        cat3 = int(cat3)
        random = int(random)
    except:
        print("All inputs must be integers!")

    cat1 = fac(cat1)
    cat2 = fac(cat2)
    cat3 = fac(cat3)
    total_items = fac(random)

    if cat2 == 0:
        pass
    else:
        answer = cat1 * cat2 / total_items
        print(answer)

    if cat3 == 0:
        pass
    else:
        answer = cat1 * cat2 * cat3 / total_items
        print(answer)


def div_factorial():
    fact = input("What is the top factorial row: ")
    fact2 = input("What is the second factorial: ")
    fact = eval(fact)
    fact2 = eval(fact2)
    Factorial = 1
    Factorial2 = 1
    count = 0
    for x in range(1, fact + 1):
        Factorial = Factorial * x
        count += 1
    print(f"Factorial {fact} is {Factorial}")
    for x in range(1, fact2 + 1):
        Factorial2 = Factorial2 * x
        count += 1
    print(f"Factorial 2:+ {fact} is {Factorial2}")
    print(f"\tDivided is {Factorial / Factorial2}")
