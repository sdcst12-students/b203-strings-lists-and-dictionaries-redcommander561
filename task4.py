#!python3
"""
Have the user enter an integer value 'n'
write a python script to use all of the integers from 1-n as the keys and the squares of those numbers as the values (2 points)
sample result:
x = { 1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25, 6 : 36, 7 : 49, 8 : 64, 9 : 81, 10 : 100 }
"""

def squares(n):
    # x will be the generated dictionary
    x={}
    # your code goes here
    for i in range(1, n + 1 ):
        x[i] = i**2  
    print(x)
    return x

n = int(input("Enter a number: "))
result = squares(n)
print(result)
        
assert squares(8) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
assert squares(10) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


