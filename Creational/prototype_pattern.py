
import copy
"""
    The difference between shallow and deep copying is only relevant for compound objects (objects that 
    contain other objects, like lists or class instances):
    
    A shallow copy constructs a new compound object and then (to the extent possible) inserts references into 
    it to the objects found in the original.
    
    A deep copy constructs a new compound object and then, recursively, 
    inserts copies into it of the objects found in the original.
"""
List1 = [[1, 2, 3], 2, 3, 4]

print(f"OBJECT1 {List1}")

List2 = copy.copy(List1)
List2[0][0] = 101

print(f"OBJECT2 {List2}")
print(f"OBJECT1 {List1}")
