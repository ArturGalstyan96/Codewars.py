import re
def validate_pin(pin):
    regex = re.compile(r'^\d{4}$|^\d{6}$')
    mo = regex.match(pin)
    if mo and mo.end() == len(pin):
        return True
    else:
        return False