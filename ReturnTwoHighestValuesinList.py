def two_highest(arg1):
    return False if type(arg1) is not list else sorted(list(set(arg1)), reverse=True)[:2]
