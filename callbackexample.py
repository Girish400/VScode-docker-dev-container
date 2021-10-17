import time 

def print_with_param(num):
    print("Yay ### just completed "+ str(num) + " iteration")

# to pass this callback function to slow calculation function we need to pass a parameter to cb in original function.
def slow_calculation_with_callback_param(cb = None):
    res = 0
    for i in range(5):
        res += i * i
        time.sleep(1)
        if cb:
            cb(i)
    return res

print(slow_calculation_with_callback_param(print_with_param))