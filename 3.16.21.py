import math
import numpy as np
from math import pi
from math import sqrt
import matplotlib.pyplot as plt
import scipy.stats as st


"""
Standard Normal Distribution Continued

    z = x - μ / σ

    Example Lots of people flip a fair coin 10000 times.
    The expected or mean number of heads is μ = np = 10000(.5) = 5000

    Standard Dev. for the number of heads = σ = √npq

    √10000(.5(.5) = 50

    Largest number of people get 5000 heads. Equal numbers will get 4999 and 5001 Heads.

    68.26% will get 5000 -50 5000 + 50    4950 | 5050
    95.44% will get between 5000 -2(50) and 5000 +2(50)     4900 | 5100

Exercises
    1. The mean score on a test is μ = 310 and the STD is σ = 29
        A. Find the percentage of pop below 316.
              Z = x - μ / σ
              Z = 316 - 310 / 29
              Z = 0.20689655172413793
              Normal Dist. = 58%

        B. A random member of the pop is chosen. What is the P() this member scores below 316?
            58%

        C. Find the percentage that scores above 316
            P(z <.21) = .5832, so P(>.21)
            print(scipy.stats.norm(310, 29).cdf(316))
                1 - .5832 - .4168
                = About 42%
        
        D. Find the prob a random member scores above 341
            Z = 1.07
            P(z < 1.07) = .8577
                So P(z > 1.07) = 1 - .8577 = .1423
                = About 14%
        
        E. Above 297
            297 - 310 / 29 = -.45
            P(z < -.45) = .3264
                So P(z > -.45) 1 - .3264 = .6736
                = About 67%
            
        F. What percentage scores between 297 and 341
            x = 341 | Z = 1.07
            x = 297 | Z = -.45
                P(z > 1.07) = .8577
                P(z > -.45) = .3264
                    .8577 - .3264
                    = About 53%
        

"""

def zscore(pop, mean, STD):
    z = (pop - mean) / STD
    print(z)
    return z


zscore(316, 310, 29)


def gaussian(x, mu, sigma):
    b_gaussian = st.norm(mu, sigma).cdf(x)
    a_gaussian = 1 - b_gaussian
    print(f"What percentage scores compared to {x}: "
          f"\nBelow: {round(b_gaussian * 100, 3) }% \nAbove: {round(a_gaussian * 100, 3)}%")
    return b_gaussian, a_gaussian


gaussian(316, 310, 29)


"""

Exercise #2
    mu = 89.7, sigma = 5.8
        A. Find the percentage that scores between 88.0 and 91.0
            x = 91.0 | Z = 91.0 - 89.7 / 5.8 = .22
            x = 88.0 | Z = 88.0 - 89.7 / 5.8 = -.29
                P(z > .22) = .5871
                P(z > -.29) = .3859
                    = .2012
                    = About 20%

        B. Between 83.2 and 87.1
            x = 83.2   | = -.45
            x = 87.1   | = -1.12
                P(z > -.45) = .
                P(z > -1.12) = .1314

        C. Prob of scoring below 112.0
            3.84 off the chart
                = About 100%

        D. Prob of scoring above 112.0
            = About 0%



Calculating z score for samples
    z == X - mu / (sigma/ sqrt/ n)
    n = size of sample
    X is the mean of the sample, n is the size of the sample. *** X is supposed to have a line over it ***


Exercise #3
    1.  μ = 200,  σ = 20
        A. Find the Prob a random member scores between 198 and 202
            198 - 200 / 20
            202 - 200 / 20
                P(z > -.10) = .4602
                P(z > .10) = .5040
                    About 8%

        B. four members are randomly chosen. Find the prob they have a mean score between 198 and 202
            X = 202 | 202 - 200 / (20/√4) = .20
            X = 198 | 198 - 200 / (20/√4) = .20
                P(z <  .20) = .5793
                P(z < -.20) = .4207
                    About 16%

        C. 25 members are randomly chosen. Find the prob they have a mean score between 198 and 202
            X = 202 | 202 - 200 / (20/√25) =  .5
            X = 198 | 198 - 200 / (20/√25) = -.5
                P(z <  .50) = .6915
                P(z < -.50) = .3085
                    About 38%

        D. 100 random members
            X = 202 | 202 - 200 / (20/√100) =  1
            X = 198 | 198 - 200 / (20/√100) = -1
                P(z <  1.0) = .8413
                P(z < -1.0) = 0.1587
                    About 68.26%


    2. Mean weight of beagles = μ 25.0 STD = σ = 3.0
        A. Find the prob that a random beagle weighs below 29.5
            z = 29.5 - 25.0 / 3.0 = 1.50
            P(z < 1.50 ) = .9332

        B. Prob weighs above 29.5
            P( z > 1.50 ) 1 - .9332 = .0668

        C Prob 7 random beagles will have a mean weight above 29.5
        X = 29.5 | z = 29.5 - 25.0 / (3.0 / √7) = 3.97
            P( z < 3.97 ) = 1.00
            P( z > 3.97 ) = 0






Standard Distribution is == a Gaussian Distribution.
1 / √2(π) * σ^2


"""
