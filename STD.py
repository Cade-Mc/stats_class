from math import sqrt

numbers = [11.0, 12.0, 12.0, 17.0, 17.0, 18.0, 18.0]

k = [2, 3, 4, 5]

def standard_deviation():
    squared_num = []
    sum_ = sum(numbers)
    print(f'\nSum of Numbers: {sum(numbers)}\n')
    sub_num = sum_ / len(numbers)

    print(f'Mean: {sub_num}\n')

    for number in numbers:
        difference = number - sub_num
        squared = difference**2
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
        consider = 1 - 1/number**2
        counter += 1
        considered = (f'Consider: {counter} = {round(consider*100,4)}%')
        print(considered)


def Chevyshevs_Theorem():
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


Chevyshevs_Theorem()


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









