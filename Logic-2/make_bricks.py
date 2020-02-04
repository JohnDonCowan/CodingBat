def make_bricks(small, big, goal):
    """
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks

make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
    :param small: int value, equal to 1 inch
    :param big: int value, to be multiplied by 5 inches
    :param goal: int value
    :return: boolean, True if goal can be made by any combination of small and big bricks
    """
    if big * 5 >= goal:
        return goal % 5 <= small
    else:
        return goal - 5 * big <= small