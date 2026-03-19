"""
Clean Numeric Strings
data = ["10", "20", "abc", "40", "xyz"]
- Convert to integers using map()
- Replace invalid values with 0 using exception handling
"""

def convert(x):
    try:
        return int(x)
    except ValueError:
        return 0
        
data = ["10", "-20", "abc", "40", "xyz"]
m = list(map(convert, data))
print(m)
