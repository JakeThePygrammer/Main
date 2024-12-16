
from datetime import datetime, date, time


def timefunction(strdate1,strdate2):
    date1 = datetime.strptime(strdate1, "%Y-%m-%d")
    date2 = datetime.strptime(strdate2, "%Y-%m-%d")
    if date1 > date2:
        return date1
    elif date2 > date1:
        return date2
    else:
        return "The dates are equal"

print(timefunction("2024-3-11", "2024-4-11"))



def age(dateofbirthstr):
    dateofbirth = datetime.strptime(dateofbirthstr, "%Y-%m-%d")
    age = datetime.now() - dateofbirth
    age_in_years = age.days / 365.25
    return int(age_in_years)

print(age("2012-11-03"))

def password(password):
    speccharachters = ["$", "@", "#", "%"]
    if len(password) >= 9:
        has_upper = False
        has_lower = False
        has_digit = False
        has_spec = False
        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            else:
                has_spec = True
        if has_upper and has_lower and has_digit and has_spec == True:
            return True
    return False

print(password("Password1@"))
