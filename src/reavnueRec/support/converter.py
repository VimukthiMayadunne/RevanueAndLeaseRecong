from re import sub



def covert_to_number(money):
    try:
        value = sub(r'[^\d.]', '', money)
        return value
    except:
        return EOFError
