"""
Basic Probability:
A probability experiment is action with a describable result, called an outcome.

The set of possible outcomes is called the sample space.

Experiment: 1
    Example: 1
        Flip a coin twice.
        Sample space: {HH, HT, TH, TT}
        There are four possible outcomes in this sample space
        An event is a subset of the sample space aka One Tails |Stop| One Heads
        E: {HT,TH}
        The probability of E: = Outcomes in E / outcomes in sample space

    Example: 2
        Getting heads 3 times on 2 flips
        0%
    Example: 3
        Getting 0 1 or 2 heads
        100%

    0 ≤ P(E) ≤ 1

    There are two possibilities for the 1st flip and 2 possibilities in the 2nd flip
    possible outcome 2 * 2.

Experiment 2:
    Exam: 1
        Roll 2 dice
        Same Space S: 24
        1,1 1,2 1,3 1,4 1,5 1,6
        2,1 2,2, 2,3, 2,4 2,5 2,6
        3,1 3,2 3,3, 3,4, 3,5 3,6
        4,1 4,2 4,3 4,4 4,5 4,6
        5,1 5,2 5,3 5,4 5,5, 5,6
        6,1 6,2 6,3 6,4 6,5 6,6

Expiremnt 3:
    Finding sample sizes:

    Exam 1:
        Flip a coin 5 times the roll a die four times:
        2*2*2*2*2 6*6*6*6 = 2^5 6^4
    Exam 2:
        Pick a card then roll a die 11 times
        52 * 6^11
    Exam 3:
        Pick a card from four decks, then roll a die 3 times, then flip a coin
        52*52*52*52 6*6*6 2 = 52^4 * 6^3 * 2

"""


def p():
    out = float(input("How many outcomes are in the variable?: "))
    sample = float(input("How many possible outcomes exist?: "))
    answer = float(out/sample)
    print(answer)
    return answer


p()



