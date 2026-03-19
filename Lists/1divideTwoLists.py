"""
Safe Division with map() + Exception
Given two lists:
a = [10, 20, 30, 40]
b = [2, 0, 5, 0]
- Divide elements of a by b using map()
- If division by zero occurs, return "Error"
"""

def division(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        return "Error"

a = [10, 20, 30, 40]
b = [2, 0, 5, 0]
m=list(map(division, a, b))
print(m)
