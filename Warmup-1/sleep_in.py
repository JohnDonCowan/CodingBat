def sleep_in(weekday, vacation):
    """
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
    :param weekday: boolean, True on a weekday
    :param vacation: boolean, True on vacation
    :return: boolean, True if we can sleep in
    """
    return(not weekday or vacation)