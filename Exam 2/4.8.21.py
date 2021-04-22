import scipy.stats
from scipy.stats import chi2_contingency
import math
f"""
Confidence intervals for variance and standard deviation

That is well estimate a populations variance and or deviation by using a sample. We'll have to assume that the pop is
normally distributed.


S^2 = sum (x - X) ^2 / n-1         Sample Variance. Square root to get STD


Chi square Distribution

n= 20 d.f. = 19
Find values for a 90% Confidence Interval for σ .

99% confidence
.5% to the left
.5% to the right
Look at Chi Squared Distr.

.005 = 32.852
.99 = 8.260

Example:
    1: Find X2L and X2R
        n = 16, 95% confidence interval, D.F. = 15
        X2L = 97.5% = 6.262
        X2R = 2.5% = 27.488

    # Have to subtract numbers so
    X2L is found under .975
    X2R is found under .025
    2. Find X2L and X2R
        n = 22, 95% CI
        D.F = n - 1 = 21
        X2L = 95% = 10.283
        X2R = 2.5% = 35.479

    3. Find X2L and X2R
        n =
        
        
√( (n-1) * s^2 / X2R ) < σ < √( (n-1)* s^2 / X2L )       
        
Example 2:
    1. A sample of size n = 21 has a a STD of s = 22.6 find 90% and 95% confidence interval for the pop STD
    D.F = 21 - 1 = 20
        A:  For 90%
            95% = 10.851  
            5%  = 31.410
            
            (21 - 1) * (22.6^2) / 31.410 
            < σ <
            (21-1) * (22.6^2) / 10.851
                
                352.2 < σ^2 < 941.4
                18.7 < σ < 30.7
    
        B: For 95%
            97.5% = 9.591
            2.5%  = 34.170
            (21 - 1) * (22.6^2) / 34.170
            < σ^2 <
            (21-1) * (22.6^2) / 9.591
            
                228.952 < σ^2 < 1065.082
                17.3 < σ < 32.6

    2.  n = 10, s = 40. Find a 90% CI for σ
        DF = 10 - 1 = 9
        Chi-Square Values: 
            95% = 3.325
            5%  = 16.919
                29 < σ < 66

    3.  n = 20, s = 40 Find 90% CI
        Chi Square Values:
            95%  = 10.117
            5%   = 30.144
                32 < σ < 55
"""
def chi_values(n, s, XR, XL):
    DF = n-1
    High = DF * (s**2) / XR
    Low = DF * (s**2) / XL
    print(f"{Low} < σ^2 < {High} ")
    print(f"{round(math.sqrt(Low), 1)} < σ < {round(math.sqrt(High), 1)} ")

f"""
    4.  n = 30, s = 40 Find a 90% CI
        Chi Square Values:
            95%  = 17.708
            5%   = 42.557
                (30 - 1) * (40^2) / 42.557
                        < σ^2 <
                (30-1) * (40^2) / 17.708
{chi_values(30, 40, 17.708, 42.557)}
"""


