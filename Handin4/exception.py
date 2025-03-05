
def check_even(number:int):
    print("Information about error:", error)
    assert (number % 2) == 0
    print(number)

try:
    check_even(7)
except:
    pass