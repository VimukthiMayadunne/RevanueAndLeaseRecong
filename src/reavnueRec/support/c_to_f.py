from re import sub

def c_to_f(data):
    print(data)
    number = int(sub(r'[^\d]', '', data))
    return number

def c_to_d(data):
    print(data)
    number = float(sub(r'[^\d]', '', data))
    return number
