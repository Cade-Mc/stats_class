import math

"""
    E = 1.645 for a 90% interval
    E = 1.960 for 95%
    E = 2.575 for 99%


Confidence Intervals for Population Proportions
This involves binomial thinking that is a member of pop either has certain characteristics or does not

Notation n = sample size , x = # of members of that sample with a characteristic
and p = P() of having that char.

if np ≥ 5 and nq ≥ 5, then we use numbers from standard normal distribution
q = 1 -p

Example:
    71 out of 120 people in a large city say they plan to vote yes on Prop X
    
    p = x / n  = 71 / 120 
        q = 1 - p   or 120/120 - 71/120 = 49 / 120
        
Confidence intervals for the proportion of the  pop that plan to vote yes are in the form
    p - E < p < P + E
    
What is E? E = 1.96 √( p * q / n ) for a 95% interval
    E = 1.645 for a 90% interval
    E = 2.575 for 99%


For a 95% CI:  E = 1.96 * ( √ (71/120) * √ (49/120) ) / √ 120 
71 / 120 * 49 / 120 / 120

"""

z = 1.96 * ((math.sqrt(71 / 120) * math.sqrt(49 / 120)) / math.sqrt(120))
print(round(z, 3))  # 0.088
"""
A 95% Confidence Interval for the proportion that plans to vote yes on Prop X is 
71 / 120 -.088 < P < 71/120 + .088

From below we can determine
.504 < p < .0680
We are 95% confident that between 50.4% and 68.0% wll vote yes on Prop X
"""
w = 71 / 120
print(w - .088)          # 0.5036666666666667
print(f"{w + .088} \n")  # 0.6796666666666666
"""
Exercises
    1. 137 out of 300 surveyed plan to vote No on Prop Z
        Find a 95% CI for the proportion of the population tha plans to vote No
        
        p = 137/300 or .457
        q = 1 - .457 or .543
        E = 1.96

    .457 - .056 < p < .457 + .056
    .401 < p < .513
    
    There are values below 50% and values above 50%
    Are we at least 95% confident whether this will pass or fail? 
    No we are not. .401 < .5
"""
def confidence_intervals(percent, x, n):
    # x = how many
    q = 1 - (x / n)
    # n = sample size
    y = percent * ((math.sqrt(x / n) * math.sqrt(q)) / math.sqrt(n))
    print(f"{percent} * √{round(x/n, 3)} * √{round(q, 3)} / √{n}")
    print(f"Your confidence interval: {round(y, 4)}")
    print(f"{round(x/n - y, 3)} < p < {round(x/n + y, 3)} \n")



confidence_intervals(1.96, 137, 300)
f"""
Exercises:
    2. A coin is flipped 200 times. Heads comes up 116 times. 
        Find 90%, 95%, 99% Confidence intervals for the proportion of times it comes up heads.
        p = 116/200 = .580 
        q = 84/200  = .420 
     {confidence_intervals(1.645, 116, 200)}   0.523 < p < 0.637 
     {confidence_intervals(1.96, 116, 200)}    0.512 < p < 0.648 
     {confidence_intervals(2.575, 116, 200)}   0.490 < p < 0.670 
        
        We are at least 90% confident that the coin is unfair
        We are at least 95% confident that the coin is unfair
        

    3. Proposition Q needs a 60% majority to pass.
        Out of 77 surveyed 52 say yes
        Fine a 95% CI for the proportion of the pop
            p = 52 / 77 = .675
            q = 25/77 = .325
    {confidence_intervals(1.96, 52, 77)}                0.571 < p < 0.78 
    Are we at least 95% certain it will pass?
    No, for this question: .571 is < .6
    This is due to how the problem is asked.

    3.5. 520 out of 770 plan to vote Yes
        Find 95% CI
        {confidence_intervals(1.96, 520, 770)}           .642 < p < .708
        Yes we are at least 95% certain it will pass
        Because all values are above .6 or 60%
        
        z = 1.96 * ((math.sqrt(520 / 770) * math.sqrt(250 / 770)) / math.sqrt(770))

        z = 1.96 * √ (520 / 770) * √(250/ 770) / √120

"""

print(math.sqrt(520 / 770) * math.sqrt(250/770))  # 0.46825341239792073









