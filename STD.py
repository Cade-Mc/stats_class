from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

# numbers = [10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 51, 52]

numbers = []


def innumbs():
    numb = True
    while numb == True:
        try:
            innumb = float(input("Input numbers one at a time: "))
            numbers.append(innumb)
        except:
            numb = False
            pass


lower_lims = []
upper_lims = []


def limits():
    for number in numbers:
        number = number / 5
        roundnumber = round(number)
        multnumber = roundnumber * 5
        if multnumber not in lower_lims:
            lower_lims.append(multnumber)

    for number in lower_lims:
        plusnumber = number + 4
        if plusnumber not in upper_lims:
            upper_lims.append(plusnumber)
    print(f"Lower Lim Classes: {lower_lims}")
    print(f"Upper Lim Classes: {upper_lims}")


k = [2, 3, 4, 5]


def standard_deviation():
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

    deviation = squared_sum / len(numbers)
    print(f'\nDeviation: {deviation}')

    std = sqrt(deviation)
    print(f'Standard Deviation: {std}')
    print("\n")


def consider():
    print("\n")
    counter = 0
    for number in k:
        consider = 1 - 1 / number ** 2
        counter += 1
        considered = (f'Consider: {counter} = {round(consider * 100, 4)}%')
        print(considered)


def Chevyshevs_Theorem():
    print("\n\n")
    mean = float(input("What is the Mean?: "))
    std = float(input("What is the Standard Deviation?: "))
    for number in k:
        sub_numb = mean - number * std
        sum_numb = mean + number * std
        print(f'\nNumber: {number}\nDifference: {sub_numb}\nSum: {sum_numb}')
    # consider()
    question = input("Would you like a Z score? y/n: ")
    if question == "y":
        x = float(input("What is x?: "))
        z = (x - mean) / std
        print(z)
    if question != "y":
        pass


def standard_dev():

    std = True
    while std:
        try:
            stdin = int(input("Would you like to run a Standard Deviation?: Type 1 for yes: "))
            if stdin == 1:
                standard_deviation()
                Chevyshevs_Theorem()
        except:
            print("Opted out of Standard Deviation.")
            std = False
            pass


listranges = []


def rangecount():
    upper_lims.sort()
    lower_lims.sort()
    try:
        range0 = 0
        range1 = 0
        range2 = 0
        range3 = 0
        range4 = 0
        range5 = 0
        range6 = 0
        range7 = 0
        range8 = 0
        range9 = 0
        range10 = 0

        for number in numbers:
            if number in range(lower_lims[0], upper_lims[0] + 1):
                range0 += 1
        listranges.append(range0)
        for number in numbers:
            if number in range(lower_lims[1], upper_lims[1] + 1):
                range1 += 1
        listranges.append(range1)
        for number in numbers:
            if number in range(lower_lims[2], upper_lims[2] + 1):
                range2 += 1
        listranges.append(range2)
        for number in numbers:
            if number in range(lower_lims[3], upper_lims[3] + 1):
                range3 += 1
        listranges.append(range3)
        for number in numbers:
            if number in range(lower_lims[4], upper_lims[4] + 1):
                range4 += 1
        listranges.append(range4)
        for number in numbers:
            if number in range(lower_lims[5], upper_lims[5] + 1):
                range5 += 1
        listranges.append(range5)
        for number in numbers:
            if number in range(lower_lims[6], upper_lims[6] + 1):
                range6 += 1
        listranges.append(range6)
        for number in numbers:
            if number in range(lower_lims[7], upper_lims[7] + 1):
                range7 += 1
        listranges.append(range7)
        for number in numbers:
            if number in range(lower_lims[8], upper_lims[8] + 1):
                range8 += 1
        listranges.append(range8)
        for number in numbers:
            if number in range(lower_lims[9], upper_lims[9] + 1):
                range9 += 1
        listranges.append(range9)
        for number in numbers:
            if number in range(lower_lims[10], upper_lims[10] + 1):
                range10 += 1
        listranges.append(range10)
    except:
        print("Done counting.")


innumbs()
limits()
standard_dev()
rangecount()

print(listranges)
yaxis = listranges


#
def graph():
    x = np.array(upper_lims)
    print(x)
    y = np.array(yaxis)
    print(y)
    plt.xlabel("Ranges")
    plt.ylabel("Frequency")
    plt.bar(x, y)
    plt.scatter(x, y)
    plt.show()


graph()

""" Test A has a mean score of 72 with a std of 11.
    Student A scores 80 on this test. (Z-score: 0.7272727272727273)
    Test B has a mean score is 72 with a std of 7.
    Student B scores a 78 on this test. (Z-Score: 0.8571428571428571) 
    Test C mean score 150 std 13 
    Student C score 147 (Z = -0.23076923076923078)
    Test D mean score 150 std 17 
    Student D 145 (Z = -0.29411764705882354)
    """

# Chevyshev's Theorem
# (Significance of Standard Deviation)
# Supposed that u=200, std= 30
# consider k = 1, 2, ...
# k = 1: u - ko = 170
# u + ko = 230


# for number in k:
#     u = 200
#     std = 30
#     sub_numb = u - number * std
#     sum_numb = u + number * std
#     print(f'Difference: {sub_numb}\nSum: {sum_numb}')


# Chevyshev's Theorem
# Sigma = STD
# k = 2: At least 75% of the numbers in the data set will be between mean - 2 Sigma and mean + 2 Sigma
#                                                                        u - 2o and u + 2o
# The numbers in the data set must be between 140 and 260
# k = 3: At least 88.88% of the numbers in the data set will be between mean - 3 Sigma and mean + 3 Sigma
#                                                                        u - 3o and u + 3o
# The numbers in the data set must be between 110 and 290


# # Beagle weight
# for number in k:
#     mean = 25.0
#     std = 3.0
#
#     sub_numb = mean - number * std
#     sum_numb = mean + number * std
#     print(f'\nNumber: {number}\nDifference: {sub_numb}\nSum: {sum_numb}')
#
# # Tire life
# print("\nTire Life:")
# for number in k:
#     mean = 40000
#     std = 4000
#     sub_numb = mean - number * std
#     sum_numb = mean + number * std
#     print(f'\nNumber: {number}\nDifference: {sub_numb}\nSum: {sum_numb}')
#
# # Mean score of test
# print("\nTest scores:")
# for number in k:
#     mean = 500
#     std = 60
#     sub_numb = mean - number * std
#     sum_numb = mean + number * std
#     print(f'\nNumber: {number}\nDifference: {sub_numb}\nSum: {sum_numb}')
