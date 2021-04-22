"""
Assume Normal Dist.


1. A sample of 16 tires of a certain brand had a mean life of 40000 miles with a sample STD of s = 5000 miles
    A) Find a 95% confidence Interval for the mean life of tire.

    E = tc * (s / sqrt(n))
    tc = 2.131
    E = 2.131 * (5000 / sqrt(16)) = 2664
    95% CI: X - E < µ < X + E
        40000 - 2664 < µ < 40000 + 2664

    We are 95% in  37336 < µ < 42664

2. X = 87.2, s = 9.8, n = 20
    A) Find a 90% CI for the pop mean µ
        d.f. = 20 - 1 = 19
            tc = 1.729
            E = 1.729 * (9.8 / sqrt(20) = 3.8

            90% CI = 87.2 -3.9 < µ < 87.2 + 3.8
            53.4 < µ < 91.0

    B) Find a 95%
        E = 2.093 * (9.8 / sqrt(20) = 4.6
        87.2 - 4.6 < µ < 87.2 + 4.6
        82.6 < µ < 91.8

    C) Find a 99% CI
        TC = 2.861
        E = 2.861 ( 9.8 / √20 ) = 6.3
            87.2 - 6.3 < µ < 87.2 + 6.3
            80.9 < µ < 93.5

3. X = 75.0, n = 22, σ = 8.0
    Find a 95% CI for µ
    We know σ, So we go back to.
        E = 1.96 (σ / √n ) = 1.96 ( 8 / √22 ) = 3.3
        75.0 - 3.3 < µ < 75.0 + 3.3
        71.7 < µ < 78.3


"""