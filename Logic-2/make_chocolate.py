def make_chocolate(small, big, goal):
    """
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
    :param small: int value, worth 1 kilo
    :param big: int value, to be multiplied by 5 kilos
    :param goal: int value
    :return: int value, equal to the number of small kilos used to reach the goal, -1 if the goal cannot be reached with a combination of big and small kilos
    """
    if goal >= big * 5:
        if goal - (big * 5) <= small:
            return goal - (big * 5)
        else:
            return -1
    else:
        if goal % 5 <= small:
            return goal % 5
        else:
            return -1