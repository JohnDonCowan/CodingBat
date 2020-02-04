def caught_speeding(speed, is_birthday):
    """
    You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(65, True) → 0
    :param speed: int value
    :param is_birthday: boolean
    :return: int value; 2 if speed is over 80, 1 if speed is over 60, 0 otherwise; speed can be 5 higher if is_birthday is True
    """
    if is_birthday:
        speed = speed - 5
    if speed > 80:
        return 2
    elif speed > 60:
        return 1
    else:
        return 0