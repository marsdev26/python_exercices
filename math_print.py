import math


def golden_ratio():
    """ Calculates and prints the golden ratio """
    golden = (1 + math.sqrt(5)) / 2
    print(golden)

def six_squared():
    """
    Uses the math module (pow function) and print 6^2
    """
    print(math.pow(6, 2))


def hypotenuse():
    """
    Uses the math module (hypot function) to return
    the hypotenuse of a triangle whose sides are 5 and 12
    """
    hyp = math.hypot(5,12)
    print(hyp)


def pi():
    """
    Uses the math module (pi function) to return the value of pi
    """
    print(math.pi)


def e():
    """
    Uses the math module (e function) to return the value of e
    """
    print(math.e)


def squares_area():
    """
    Returns (manually typed) the area of 10 squares, the first
    square starting with a side of length l = 1, and continue to square 10th
    with a side of length l = 10
    (square n has sides of length l = n,
    ex: square number 5 has sides of length l = 5)
    """
    print(1**2,2**2,3**2,4**2,5**2,6**2,7**2,8**2,9**2,10**2)

if __name__ == "__main__" :

    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()



