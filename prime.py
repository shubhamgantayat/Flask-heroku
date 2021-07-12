def prime(n):
    if type(n) == int and n > 0:
        if n == 1:
            return False
        for i in (2, int(n ** 0.5 + 1)):
            if n % i == 0:
                return False
        return True
    else:
        raise TypeError('Not a valid input')
