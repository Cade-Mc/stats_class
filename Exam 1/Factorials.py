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


def factorial():
    fact = int(input("What is the factorial: "))
    Factorial = 1
    count = 0
    if fact == 0:
        print("Factorial 0 is 1")
    else:
        for x in range(1, fact + 1):
            Factorial = Factorial * x
            count += 1
        print(f"Factorial {count} is {Factorial}")

