import math
import traceback
def function12(x):
    if x<(-10):
            function12= (x/13)-(x**7)
    if (x>=(-10)) and (x<29):
            function12= (math.cos(70*x**3 + math.tan(x)) - x**8)
    if (x>=29) and (x<62):
            function12 = math.log(82*(x**2)+45*(x**8),math.e)+(24*(x**7))-55
    if (x>=62) and (x<140):
            function12= ((11*x**6+ x**7)**2) + math.sin(x)
    if (x>=140):
            function12= (66*x**2)-x**4
    print(function12)
    function12= '%.2e'% function12
    return function12

try:    
    assert function12(40) == '3.93e+12'
    assert function12(114) == '7.53e+28'
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")