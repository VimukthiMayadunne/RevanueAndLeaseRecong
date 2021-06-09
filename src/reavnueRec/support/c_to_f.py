from re import sub

def c_to_f(data):
    number = int(sub(r'[^\d]', '', data))
    return number
