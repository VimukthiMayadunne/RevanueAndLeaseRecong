from re import sub



def covert_to_number(money):
    try:
        value = sub(r'[^\d.]', '', money)
        return int(value)
    except:
        return EOFError

def covert_to_money(money):
    try:
        value = sub(r'[^\d.]', '', money)
        return float(value)
    except:
        return EOFError
