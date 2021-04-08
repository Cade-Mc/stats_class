from numpy import prod
from math import factorial as fac
import math
import scipy.stats as st


def basic_prob():
    out = float(input("How many outcomes are in the variable?: "))
    sample = float(input("How many possible outcomes exist?: "))
    answer = float(out / sample)
    print(answer)
    return answer


def probab_frac():
    fracs = []
    x = True
    while x:
        a = float(input("How much: "))
        b = float(input("Out of how much: "))
        c = a / b
        print(c)
        again = float(input("Again? 1 Yes 2 No: "))
        if again == 1:
            fracs.append(c)
            continue
        else:
            fracs.append(c)
            p = prod(fracs)
            print(f"Probability: {p}")
            x = False


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


def standard_deviation():
    numbers = []
    squared_num = []
    sum_ = sum(numbers)
    print(f'\nSum of Numbers: {sum(numbers)}\n')
    sub_num = sum_ / len(numbers)

    print(f'Mean: {sub_num}\n')

    for number in numbers:
        difference = number - sub_num
        squared = difference ** 2
        squared_num.append(squared)
        print(f'Difference Squared: {squared}')

    squared_sum = sum(squared_num)
    print(f'Squared sum: {squared_sum}')

    pop_deviation = squared_sum / len(numbers)
    print(f'\nDeviation: {pop_deviation}')
    samp_dev = squared_sum / (len(numbers) - 1)

    samp_std = math.sqrt(samp_dev)
    pop_std = math.sqrt(pop_deviation)
    print(f'Pop Standard Deviation: {pop_std}')
    print(f'Samp Standard Deviation: {samp_std}')


def consider():
    k = []
    print("\n")
    counter = 0
    for number in k:
        consider = 1 - 1 / number ** 2
        counter += 1
        considered = (f'Consider: {counter} = {round(consider * 100, 4)}%')
        print(considered)


def Chevyshevs_Theorem():
    k = []
    print("\n\n")
    mean = float(input("What is the Mean?: "))
    std = float(input("What is the Standard Deviation?: "))
    for number in k:
        sub_numb = mean - number * std
        sum_numb = mean + number * std
        print(f'\nNumber: {number}\nDifference: {sub_numb}\nSum: {sum_numb}')
    consider()
    question = input("Would you like a Z score? y/n: ")
    if question == "y":
        x = float(input("What is x?: "))
        z = (x - mean) / std
        print(z)
    if question != "y":
        pass


def zscore(pop, mean, STD):
    z = (pop - mean) / STD
    print(z)
    return z


def gaussian(x, mu, sigma):
    b_gaussian = st.norm(mu, sigma).cdf(x)
    a_gaussian = 1 - b_gaussian
    print(f"What percentage scores compared to {x}: "
          f"\nBelow: {round(b_gaussian * 100, 3) }% \nAbove: {round(a_gaussian * 100, 3)}%")
    return b_gaussian, a_gaussian


def single_gaussian(mu, sigma, x1):
    print("Single Gaussian Distribution: \n")
    b_gaussian = st.norm(mu, sigma).cdf(x1)
    a_gaussian = 1 - b_gaussian
    print(f"\nWhat P() scores compared to {x1}: "
          f"\nBelow: {round(b_gaussian * 100, 3) }% \nAbove: {round(a_gaussian * 100, 3)}%")
    return b_gaussian, a_gaussian


def single_sample_distr(mu, sigma, x1, sample):
    print("Single Sample Distribution: \n")
    x = (x1 - mu) / (sigma / (math.sqrt(sample)))
    b_gaussian = st.norm.sf(x)
    a_gaussian = 1 - b_gaussian
    print(f"\nWhat P() scores compared to {x1}: "
          f"\nBelow: {round(b_gaussian * 100, 3) }% \nAbove: {round(a_gaussian * 100, 3)}%")
    return b_gaussian, a_gaussian


def double_gaussian(mu, sigma, x1, x2):
    print("Double Gaussian Distribution: \n")
    b_gaussian = st.norm(mu, sigma).cdf(x1)
    b2_gaussian = st.norm(mu, sigma).cdf(x2)
    between = b_gaussian - b2_gaussian
    between = abs(between)
    print(f"\nThe P() score is between {x1} and {x2}: "
          f"\n{round(between * 100, 3)}%")


def double_sample_distr(mu, sigma, x1, x2, sample):
    print("Double Sample Distribution: \n")
    first = (x1 - mu) / (sigma / (math.sqrt(sample)))
    second = (x2 - mu) / (sigma / (math.sqrt(sample)))
    p = st.norm.sf(first)
    p2 = st.norm.sf(second)
    between = p - p2
    between = abs(between)
    print(f"\nThe P() score is between {x1} and {x2}: "
          f"\n{round(between * 100, 3)}%")


def distributions(mu, sigma, x1, x2=None, sample=None):
    if x2 == None and sample == None:
        zscore(mu, sigma, x1)
        single_gaussian(mu, sigma, x1)
    if x2 == None and sample != None:
        zscore(mu, sigma, x1, sample)
        single_sample_distr(mu, sigma, x1, sample)
    if x2 != None and sample == None:
        print(f"Score 1: {x1} ")
        zscore(mu, sigma, x1)
        print(f"Score 2: {x2} ")
        zscore(mu, sigma, x2)
        double_gaussian(mu, sigma, x1, x2)
    if x2 != None and sample != None:
        print(f"Score 1: {x1} ")
        zscore(mu, sigma, x1, sample)
        print(f"Score 2: {x2} ")
        zscore(mu, sigma, x2, sample)
        double_sample_distr(mu, sigma, x1, x2, sample)


def con_int_normal_dist(n, s, X=None):
    if X == None:
        X = 0
    if n < 30:
        w = input("Is this problem normally distributed? Y|N: ")
        if w == "Y":
            pass
        if w == "N":
            print("You cannot find the confidence interval.")

    ninty = 1.645
    ninty_five = 1.96
    ninty_nine = 2.575
    percent90 = ninty * (s / math.sqrt(n))
    print(f"90% | {round(X - percent90, 2)} < µ < {round(X + percent90, 2)} | {round(percent90, 2)}")
    percent95 = ninty_five * (s / math.sqrt(n))
    print(f"95% | {round(X - percent95, 2)} < µ < {round(X + percent95, 2)} | {round(percent95, 2)}")
    percent99 = ninty_nine * (s / math.sqrt(n))
    print(f"99% | {round(X - percent99, 2)} < µ < {round(X + percent99, 2)} | {round(percent99, 2)}")
