def inhospitable_weather(temp):
    """ (number) -> Bool
    Return the True if and onl if the given tempreature in degrees celcius is unplesent (too hot or too cold)
    >>> inhospitable_weather(20)
    False
    """
    if temp > 28:
        return True
    elif temp < 12:
        return True
    else:
        return False

room_temp=inhospitable_weather(20)
print(room_temp)