import scipy.stats as st
import math


def zscore(mu, sigma, x1, sample=None):
    if sample == None:
        z = (x1 - mu) / sigma
    if sample != None:
        z = (x1 - mu) / (sigma / math.sqrt(sample))
    print(f"Z-Score: {z} \n")
    return z


# zscore(310, 29, 316)


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


# distributions(200, 20, 198, sample=25)


