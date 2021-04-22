from math import sqrt
import scipy.stats as st

"""
Confidence intervals

Population STD
σ = √ Σ(x-µ)^2 / √N

A sample standard deviation
S = √ Σ(x-µ)^2 / √ (n - 1)

Exercise

    A sample is as a follows 8 10 11 11 12
    
        X = ( 8 + 10 + 11 + 11 + 12 ) / 5 
            = 52 / 5 
                = 10.4
                
X              (X - x)^2              = 
8              (8 - 10.4)^2             5.760
10             (10 - 10.4)^2            0.160
11                                      0.359
11                                      0.359
12                                      2.559
"""

numbers = [8, 10, 11, 11, 12]


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

    pop_deviation = squared_sum / len(numbers)
    print(f'\nDeviation: {pop_deviation}')
    samp_dev = squared_sum / (len(numbers) - 1)

    samp_std = sqrt(samp_dev)
    pop_std = sqrt(pop_deviation)
    print(f'Pop Standard Deviation: {pop_std}')
    print(f'Samp Standard Deviation: {samp_std}')


"""
Confidence intervals for large samples  n ≥ 30

if lots of people take a sample size of 30 their X's will be normally distributed and the average of their X's will be µ

That means if a sample is large , you can still construct a confidence interval for µ even if the pop is not normally 
distributed. 

Also if n < 30, we cant construct interval if the pop is not normally distributed.

Exercises:
    Do not assume the pop is normally distributed unless stated.
    if σ is not known we will use s
    
    1. Sample n = 35, X = 87.6, s = 5.8
    Construct 90% 95% and 99% confidence intervals for µ
    n ≥ 30, 
    90%: E = 1.645 s/√n 
        = 1.645 * 5.8/√35 = 1.612
            = 87.6 - 1.6 < µ < 87.6 + 1.6
                = 90% 85.99 < µ < 89.21
                
    2. Sample n = 23, X = 80, s = 5
        n < 30 and the pop is not known to be normally distributed. So we can not construct confidence intervals
        
    3. n = 23, X = 80, s = 5 
        n < 30 and The population is normally distributed.
        n < 30 but σ is unknown. Cant do this yet
        
    4. n = 23, X = 80 σ = 5
        The pop is normally distributed.

"""

# S = sigma
# x =
# n = sample size
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
    percent90 = ninty * (s / sqrt(n))
    print(f"90% | {round(X - percent90, 2)} < µ < {round(X + percent90, 2)} | {round(percent90, 2)}")
    percent95 = ninty_five * (s / sqrt(n))
    print(f"95% | {round(X - percent95, 2)} < µ < {round(X + percent95, 2)} | {round(percent95, 2)}")
    percent99 = ninty_nine * (s / sqrt(n))
    print(f"99% | {round(X - percent99, 2)} < µ < {round(X + percent99, 2)} | {round(percent99, 2)}")


con_int_normal_dist(35, 12, 145)
"""
Remark: The higher the confidence, the wider the interval.

If n ≥ 30 then you can always construct a confidence interval for µ use σ if its known, if not use s.

If n < 30 then the pop must be normally distributed.

If σ is known, calculate E as above.

Find 95% confidence int for µ if possible. Do not assume normal distribution

    1. n = 40, X = 600, s = 40
        n ≥ 30 
        E = 1.96 40/ √40
        95% CI: 600 - 12 < µ < 600 + 12
            588 < µ < 612
    
    2. n = 19, X = 22.3, s = 1.97
        The pop is normally distributed.
        We do not know sigma.
        We cannot calculate E.
        
    2.5 n = 19, X = 22.3, σ = 1.97
        The pop is normally distributed.
        We do know sigma.
        We can calculate E
                            90% | 22.09 < µ < 23.57 | 0.74
                            95% | 21.94 < µ < 23.72 | 0.89
                            99% | 21.67 < µ < 23.99 | 1.16
    
    3. n = 13, X = 43.19, σ = 3.44
        The pop is not normally distributed.
        We do know sigma.
        We cannot calculate E
    
    4. n = 13, X = 43.19, σ = 3.44
        The pop is normally distributed.
        We do know sigma.
        We can calculate E      
                    con_int_s(13, 43.19, 3.44)
                    90% | 41.62 < µ < 44.76 | 1.57
                    95% | 41.32 < µ < 45.06 | 1.87
                    99% | 40.73 < µ < 45.65 | 2.46

---------------------------------------------------------------------------
Determine if confidence intervals can be constructed using this method:

1. n = 43, X = 70, s = 13
    pop. normal dist.
    because n > 30 we didn't need normal dist
    Yes, you can find the confidence interval.

2. n = 27, X = 70, σ = 13
    pop is ND.
    because pop is ND and we have σ
    Yes you can find the confidence interval.
    
3. n = 26, s = 8
    pop is not ND
    N is < 30 and pop is not ND along with no sigma
    No you can not find the confidence interval.

4. n = 25, σ = 5.3
    pop is not ND
    N is < 30 
    No you can not find the confidence interval.
    
5. n = 22, σ = 19
    pop is ND
    because pop is ND and sigma is known.
    Yes you can find the confidence interval.
    
6. n = 38, X = 80, s = 10
    n > 30
    Yes you can find the confidence interval.
    
==========================================================
        Summary:
    if n ≥ 30 we can construct confidence intervals. 
        We do not need pop to be ND. 
        We can also use S and don't need σ.
    if n < 30, 
        the pop must be ND 
        and the σ must be known
    
"""
