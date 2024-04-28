# Vectory Library at home
# diy_vector.py

import math

class vec3:
    # constructors. Using floats bc I don t have doubles
    def __init__(self):
        self.e = [float(0),float(0),float(0)]
    def __init__(self, e0, e1, e2):
        self.e = [float(e0), float(e1), float(e2)]
    # reference vector components
    def x(self):
        return self.e[0]
    def y(self):
        return self.e[1]
    def z(self):
        return self.e[2]
    # basic operations
    def __neg__(self):  # overload - op
        return vec3(-self.e[0], -self.e[1], -self.e[2])
    def __iadd__(self, v): # overload += op... want to do (self, v:vec3) but cant?? 
        self.e[0] += v.e[0]
        self.e[1] += v.e[1]
        self.e[2] += v.e[2]
    def __imul__(self, t: float): # overload *= op
        self.e[0] = self.e[0] * t
        self.e[1] = self.e[1] * t
        self.e[2] = self.e[2] * t
        return self
    

def unit_test():
    # TODO create tests here
    test_vec = vec3(.4, .5, .6)
    def test_helper(test_function, test_input, expected_value):
        # this unfortunately doesn't work the way I want it too, but look into it.
        # Tried "test_helper(vec3.z(), test_vec, float(.6))" for z() test but didn't work
        #   bc it's looking for "self" arg in vec3.z()
        a = test_function.__name__
        print(a + " test:  passed" if test_input.test_function() == expected_value else a + " test: failed")
    # test for x()
    print("x() test:  passed" if test_vec.x() == .4 else "x() test: failed")
    # test for y()
    print("y() test:  passed" if test_vec.y() == .5 else "y() test: failed")
    # tests for z()
    test_helper(vec3.z, test_vec, float(.6))
    # TODO tests for __neg__()
    # TODO tests for __iadd__()
    # TODO tests for __imul__()
    # TODO tests for 
    # TODO tests for 
    # TODO tests for 
    # TODO tests for 
    return 0

class test_class:
    def __init__(self):
        self.e = "test variable"
    def access_e(self):
        return self.e
    
def test_helper(test_function, test_input, expected_value):
        a = test_function.__name__
        print(a + " test:  passed" if test_input.test_function() == expected_value else a + " test: failed")