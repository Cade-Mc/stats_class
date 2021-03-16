from fractions import Fraction as fc
from numpy import prod
"""

Multiplication Rule:
The P() A and B Occur
    If Independent P(A and B) = P(A) * P(B)
    If Dependent P(A and B) = P(A) * P(B|A)
============================================================

Addition Rules:
The P() A or B will occur
    P(A or B) = A/X + B/X 
    If they lap over each other:
        P(A or B) = P(A) + P(B) - P(A and B)
        
    What is the probability of P(A or B or C)
        P(A) + P(B) + P(C) - P(A and B) - P(A and C) - P(B and C) + P(A and B and C)

============================================================
Independent Events:
    Events A and B are independent if A occuring does not affect the probability of B occurring. (Vice-Versa)

Examples:
    Event A:
        A coin turned up heads when flipped.
        Then a die is rolled.
    Event B:
        The die comes up a 6.
                                    P(B) = 1/6 | Note: Independent or if A occurred or not.
                                    P(A) = 1/2 | Note: Independent or if B occurred or not.

    Event A: rolling a die.
    Event B: Picking a queen out of a deck
                                    P(B) = 4/52

Multiplication Rule:
    If A and B are independent the probability of both occurring is P(A) * P(B)


Probability of a coin flipped 10 times landing on heads or tails 10 times in a row.
x = 1/2
w = x**10
print(w)

Ten percent of people are left handed. A card I picked then a random person is chosen find the probability of picking
a face card then a left handed person.

P(A|B) = 12/52 * 1/10 = 12/520

Dependent Events:
    Events A and B are dependent if the P(B) is affected by P(A) occurring.
    P(A and B) = P(A) * P(B|A)

    Example:
        Two cards are drawn without replacement. What is the P() both cards are kings.
        4/52
        3/51
        x = 4/52
        y = 3/51
        w = x*y
        print(w)
        # 0.004524886877828055

Importing fractions:

    Example: 2
        First card king second card queen
        4/52
        4/51
        a = fc(4, 52)
        b = fc(4, 51)
        c = a * b
        print(c)
        4/663
        
Complements of Events:
    E' is the set of outcomes not in E.
    1: a coin is flipped 3 times
        S: {HHH, HHT, HTT, TTT, TTH, THH, THT, TTT} 2^3
        E: Exactly 1 tail {THH, HTH, HHT}
        E': {HHH, HTT, TTT, TTH, THT, TTT}
    
A coin is flipped 15 times 
Find the prob of getting heads at least once.
S: 2^15 = 32768
E: At least one flip is heads 
E': Zero heads (all tails) TTTTTTTTTTTTTTT
How many outcomes in E'? One

P(E) = 1 - P(E') = 1 - 1/32768 = 32767/32768

    A card is picked from 4 decks.
    What is the P() what is the probability of getting at least one king 
    E = 1 king
    E' = 0 king
    
    P(E') = (48/52)^4 (12/13)^4  
    P(E) = (4/52)^4 or (1/13)^4 1/28561
    
    A die is rolled 7 times
    P() of a 4 just once
    E = 1 Four 1/6 ^7
    E'= 0 Four  5/6 ^7
    P(E') = 5/6 ^7 78125/279936
    P(E) = 1 - (78125 / 279936 ) = 0.72091835

Addition Rules:
    The P() A or B will occur
    P(A or B) = A/X + B/X 

    
    Experiments:
        Whats the P() it's Queen or red card? A:Queen B:Red
        Careful! a Red can also be a Queen
        Answer: 2/52 
        P(A or B) = P(A) + P(B) - P(A and B) = 4/52 + 26/52 - 2/52 - 28/52 = 7/13
        
        Whats the P() its a face card or a black card? 
        A: Face B Black
        A: 12/52 B: 26/52 
        Half of the face cards are black 6
        6/52 + 26/52 = 32/52 = 8/13
        
                Under 21:       21-40       Over 40     Total
Oceanside:      8               10              15          33
Vista:          7               4               2           13
San Marcos:     9               11              4           24
-----------------------------------------------------------------
                24              25              21          70

A): Is under 21 or from Oceanside:
    24/70 + 33/70 - 8/70 = 49/70 = 7/10


B): Is over 40 or from Vista:  
    21/70 + 13/70 - 2/70 = 32/70 = 16/35

C): Is 21-40 from San Marcos:
    25 + 24 - 11 = 38/70 = 19/35


What is the probability of P(A or B or C)
    P(A) + P(B) + P(C) - P(A and B) - P(A and C) - P(B and C) + P(A and B and C)
    
   
"""
# PA = 0.42
# PB = 0.51
# PC = 0.23

"Using *** it was counted 3 times but uncounted 3 times so we add it back."
# P(A and B) = 0.17 P(A and C) = 0.15 P(B and C) = 0.15
#           P(A and B and C) = 0.05
#     Find P(A or B or C) = .42 + .51 + .23 - .17 -.15 -.15 +.05 = .74


"Too Much logic to add while coding along"
# abc = []
# def ABC():
#     A = input("A: ")
#     B = input("B: ")
#     C = input("C: ")
#     denom = input("Denominator: ")
#     ABC = A + B + C
#     If x in abc
#     ABC / denom




fracs = []

def probab_frac():
    x = True
    while x:
        a = float(input("How much: "))
        b = float(input("Out of how much: "))
        c = a/b
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


probab_frac()


