# Original/Incorrect Version
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 4000 == 0:  # The year must be divided by 400 (not 4000)
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# Correct Version:
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
