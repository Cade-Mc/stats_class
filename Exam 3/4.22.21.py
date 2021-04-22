from math import sqrt
f"""
Testing claims about population means

Well need the pop to be ND if sigma is known then we proceed as if the sample were large
    use the z table
if only the same STD s is know we use the t-table
    Well use the t-table to identify critical regions
    Three cases:
    1. H0: µ = k so that Ha :µ > k or µ < k (Two Tailed Test)

        We reject the null hypothesis if the t-score or  z is above the positive critical value or below the negative
        critical value. (The value at the end of the critical region.

    2. H0: µ ≤ k so that Ha: µ > k (Right Tailed Test)

        We reject the null hypothesis if the t-score is above the positive critical value.

    3. H0: µ ≥ k so that Ha: µ < k (Left Tailed Test)

        We reject hte null hypothesis if the T-score or z is below the negative critical value.


Exercises: Assume Normal Distribution:

    1. Claim µ = 47.3
        Test the claim with alpha α = 0.05 based on the following sample. Find null and alternate hypotheses.
            n = 23,    X-bar = 49.2,        s = 4.3


            null          H0: µ = 47.3
            alternate     Ha: µ < 47.3 OR µ > 47.3

            Find score on T-table:
            Use Degree Freedom n-1 
            Critical t-value: 2.074

                                        t = ( X-bar - µ )  / ( s / √n )
                                        (49,2 - 47.3) / ( 4.3 / √23 )
                                    {print((49.2 - 47.3) / (4.3 / sqrt(23) ))} = 2.12

                2.12 > 2.074. Our t-value is in the critical region, meaning we reject the null hypothesis
                At alpha α = 0.05 we have strong evidence that the claim is false.


        Now test with a = 0.01
        New Critical T-value: 2.819
            2.12 is not above 2.819 so its not in the critical region. We fail to reject the null hypothesis
        At alpha = 0.01, we do not have strong evidence that the claim is false.


"""
def tScore(X, mu, s, n):
    t = (X - mu) / (s / sqrt(n))
    print(round(t, 3))
    return t


f"""
    2. Claim µ = 900
        Test with Alpha  α = 0.05
        Critical T-table score = 2.086
        
        n = 21, X-bar = 850, s = 78
            {tScore(850, 900, 78, 21)} = -2.938
        
        
        -2.94 < -2.086 Our t-value is in the critical region, meaning we reject the null hypothesis.
        At Alpha α = 0.05 we have strong evidence that the claim is false. 

        At Alpha = 0.01 
            critical value = 2.845
                t= -2.94 is in the critical region, we reject the null hypothesis
                    At α = 0.01 we have strong evidence that the claim is false. 

    3. Claim: µ ≤ 8.34
        Test the claim α 0.05 
            n = 17, X-bar = 9.02, s 1.75
                Critical value = 1.746

            H0: µ ≤ 8.34
            Ha: µ > 8.34
            {tScore(9.02, 8.34, 1.75, 17)} = 1.602
            T = 1.602 is not in the critical region. We fail to reject the null hypothesis.
                At α = 0.05 we do not have strong evidence that the claim is false.

    4. Claim µ  < 38.24
        Test α = 0.01 
            n = 26, X = 37.18, s = 2.46
                Critical Value = 2.485
            {tScore(37.18, 38.24, 2.46, 26)} =  -2.197

        H0: µ ≥ 38.24
        Ha: µ < 38.24
            T = -2.197 is not in the critical region. We fail to reject the null hypothesis.
                At α = 0.01 we do not have strong evidence that the claim is true.
        
        For α = 0.05 
            Critical Value = 1.708
                T = -2.197 is  in the critical region. We reject the null hypothesis.
                    At α = 0.05 we have strong evidence that the claim is true.
            

QUIZ
Claim: μ=57.8 

Test the claim with α=0.05 based on the sample: n=39, xbar=56.6, s=5.1 

{tScore(59.5, 57.8, 5.1, 39)} 



"""

