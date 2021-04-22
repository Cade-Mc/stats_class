import math
import formulas as f
f"""
Testing Claims about Population Means


Hypotheses"
    Null hypotheses are statements that contain equality.
    Here are three types:
    H0 : µ = 50
    H0: µ ≥ 50
    H0: µ ≤ 50


    We will test these hypotheses with samples.

    H0 : µ = 50

    Alternate hypotheses negate a null hypothesis and thus do not contain equality. Three types of alternate hypotheses
    Ha = Alternate Hypotheses
    H0: µ = 50
        Ha: µ > 50 or µ < 50
            Ha is not = to 50

    H0: µ ≥ 50
        Ha: µ < 50
            Ha is not = 50

    H0: µ ≤ 50
        Ha: µ > 50
            Ha is not = 50


    Exercises: State the alternate hypothesis

        1. H0: µ = 67.4
            Ha: µ > 67.4 or µ < 67.4

        2. Ha: µ ≥ 98.2
            µ < 98.2

    Other Exercises

        1. A claim is made that µ = 50 (What type of Hypothesis is this claim.)
            - null hypothesis
            We will take a sample and reject the null hypothesis if our X-bar is much larger
            or much smaller than 50.
            n = 33, X-bar = 55, STD = 12
"""


def Zscore(n, Xbar, STD, mu):
    z = (Xbar - mu) / (STD / math.sqrt(n))
    print(round(z, 3))
    return z


f"""
{Zscore(33, 55, 12, 50)} = 2.394
    P(z < 2.39) = .09916, so P(z> 2.39) = 1 - 0.9916 = .0084
        So?
            If µ is equal to 50 there is only a 0.0084 = .84% probability of gettting an
            Xbar this large or larger.
            
            This means the claim is likely false. We have strong evidence that the claim is false.
            

{Zscore(33, 53, 15, 50)} = 1.149
    P(z < 1.15) = 0.8749, so P(z > 1.15) = 1 - .08749 = .1251
    
    if µ is equal to 50, there is a 12.51% prob of getting an Xbar this high.
    This is not a small probability. 
    This sample does not give strong evidence that the null hypothesis is false. 

In summary:
    We have a null hypothesis H0: µ = k
    We will have to either reject it or fail to reject it.
    We will have either strong evidence the claim is false or we will not.

    We are not able to prove claims true with a sample.

Testing the null hypotheses
    Confidence intervals are typically 90% 95% and 99%

    We typically test a null Hypothesis H0: µ = k with a significance level
    a = 0.10, a = 0.05, or a= 0.01
    
    If we use a = 0.05
    Then we reject the null hypothesis if we get an Xbar so high or low that it has less than 
    a 5% chance of happening.
    
    a / 2 = 0.025 in this case

    More specifically well reject a NH if Xbar is so high it has less than a 5%
    chance of happening.
    
"""
