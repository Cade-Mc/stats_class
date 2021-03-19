import gaussian
"""
Confidence Intervals

Z = x - mu / sigma /√ sample

Exercises:

    1. The mean body temp of humans is  98.2 with a STD of 0.7
        A): P() sample of 11 people will have a mean temp of 97.9 and 98.3
        gaussian.distributions(98.2, .7, 97.9, 98.3, 11)
"""

""" 
Function Output:

Score 1: 
Z-Score: -0.42857142857142455 

Score 2: 
Z-Score: 0.14285714285713474 

Double Sample Distribution: 

The P() score is between 97.9 and 98.3: 
60.458%
"""
"""
NOTES:

x = 98.3 Z = 98.3 - 98.2 / 0.7 /√11 = .47
x = 97.9 Z = 98.3 - 98.2 / 0.7 /√11 = - 1.42

P(z < .47)   = .6808   68.08%
P(z < -1.42) = .0778    7.78%
            = 0.6030  About 60%
            
"""
"""
        B) P() between 96.8 and 99.6
        
gaussian.distributions(98.2, .7, 96.8, 99.6)
"""

"""
    2.  mu = 1000, Sigma = 100
        A): Find P() sample size 16 is between 950 and 1050
    
    3. mu = 57.60, Sigma = 3.80
        A) Find P() sample size 22 is between 55.98 and 57.60
        Z score 59.22 = 2.00
        Z score 55.98 = -2.00
        gaussian.distributions(57.60, 3.80, 55.98, 59.22, 22)
        
    4.  mu = 1000 STD = 100
        B) between 980.4 and 1019.6 sample size 100
        gaussian.distributions(1000, 100, 980.4, 1019.6, 100)
    
    5. mu = 175.0, Sigma = 20.0 
        A): between 135.8 and 214.2 
            Z-Score: -1.9599999999999995
            Z-Score: 1.9599999999999995 
            214.2 = 175.0 + 1.96(20.0)
            135.8 = 175.0 - 1.96(20.0)
        
        Mu + 1.96(sigma)    
        Mu - 1.96(sigma)
        gaussian.distributions(175.0, 20.0, 135.8, 214.2)
        
        
    With sample sizes formula = 
    Mu + 1.96(Sigma / sqrt(sample))
    Mu - 1.96(Sigma / sqrt(sample))
    
"""
gaussian.distributions(175.0, 20.0, 135.8, 214.2)


