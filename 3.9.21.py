"""
Binomial Probability Continued
mu μ = np
Sigma σ  = sqrt/npq
Exercise: A for coin is flipped 10 times find the p() of getting 0 heads 1 head 2 heads 3 heads... 10 heads.
P(x=0)
P(x=1)
P(x=2)
P(x=3)
P(x=4)
P(x=5)

                                        n = 10, P = .5 Q = .5
                                        P(X Successes) = (nCx)p^x * q^n-x

Q ^ 10  =                               P(x = 0) = (10C0) * (.5)^0 * (.5)^10
                                            10! / 0! (10-0)! | (1) (.5)^10 = .001
                                                (= 1/1024)
-----------------------------------------------------------------------------------------------------------------
P(x = 1) = (10C1) = (.5)^1 * (.5)^9
            = 10(.5)(..001953125)
                = 10(.5)^10
                    = .010
-----------------------------------------------------------------------------------------------------------------
P(x = 2) = (10C2) = (.5)^2 * (.5)^8
            = 10! / 2! * 8! | * (.05)^10
                = 45(.5)^10
                    = .044
-----------------------------------------------------------------------------------------------------------------
P(x = 3) = (10C3) = (.5)^3 * (.5)^7
            = 10! / 3! * 7! | * (.05)^10
                10 * 9 * 8 * 7!  / 3! * 7!   720 / 6 = 120
                = 120(.5)^10
                    = .117
-----------------------------------------------------------------------------------------------------------------
P(x = 4) = (10C4) = (.5)^4 * (.5)^6
            = 10! / 4! * 6! | * (.5)^10
                = 210(.05)^10
                    = .205
-----------------------------------------------------------------------------------------------------------------
P(x = 5) = (10C5) = (.5)^5 * (.5)^5
            = 10! / 5! * 5! | * (.5)^10
                = 252(.5)^10
                    = .246
-----------------------------------------------------------------------------------------------------------------
P(x = 6) = (10C6) = (.5)^6 * (.5)^4  == P(x = 4) = (10C4) = (.5)^4 * (.5)^6
    = .205

P(x = 7) = P(x = 3)
All future the same as opposite


μ = np = 5

σ = sqrt/10(.5)(.5) = 1.6

=================================================================================================================
      μ - σ = .3414
      μ + σ = .3414
      μ - 2σ = .1359
      μ + 2σ = .1359


Exercises
    1. The scores on a test are normally distributed.
       The mean score is 200 and the STD is 30
        A) What percentage of the population scores between 200 and 230
            μ = 200 σ = 30
            Z = X - μ / STD
            X = μ + (z)(STD)
            What is the percentage scores between μ and μ + 30
            Z = 230 - 200 / 30
            = .3413

        B) Between 170 and 200
            Between μ - σ and μ
            = .3413

        C) Between 170 and 260
            Between μ - σ and μ + 2σ
            = .1359 + .3413 + .3413
                = .8185

        D) Between 140 and 260
            Between μ - 2σ and μ + 2σ
             -------|----    -----|--------
            .1359 + .1359 + .3413 + .3413

        E) Between 140 and 170
            μ - 2σ and μ - σ
            = .1359 because μ - 2σ includes μ - σ

        F) Below 200?
            = .5

        G) Above 200?
            = .5

        H) Below 230?
            .5 + .3413
                = .8413

        I) Below 260
            .5 + .3413 + .1359
                =0.9772
---------------------------------------------------------------------------------------------------------------
                                The Normal Distribution Table:
Z - scores: Z = x - μ / σ
Example:
    μ = 200
    σ = 30
    Convert score of 215 to Z score:
        = 215 - 200 / 30
           Z = .50
    What percentage of the population scores below 215
        215 = μ + .5σ
            .6915

Exercises:
Assume the population is normally distributed                    *use the table*
    1. Find the percentage of the population that scores below
        z = 1.13
            P(Z < 1.13)
                = .8708

    2. Find the P() a random member of the pop scores below
        z = 1.13
            P(Z < 1.13)
                = .8708

Find P(a < Z < b). The probability that a standard normal random variables lies between two values is also easy to find.
The P(a < Z < b) = P(Z < b) - P(Z < a).

"""

print (.5 + .3413 + .1359)