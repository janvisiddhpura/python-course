class InValidAgeException(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InValidAgeException("Age must be 18 or above!")
    print("Access Granted!")

try:
    check_age(19)
    check_age(10)
except InValidAgeException as e:
    print("Custom Exception:", e)
    