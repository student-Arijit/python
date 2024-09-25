print("to print") #print func
list = [1, 2, 3, 4]
print(len(list)) #calculate length of list
for i in range(5): #Returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default) and stops before a specified number.
    print(i)
print(sum(list)) #sum of numbers
print(max(list)) #find max num
print(min(list)) #find min num
name = input("enter your name: ") #get input by user
print("hello!" + name)
print(input()) #valid
numbers = [5, 2, 8, 1, 4]
print(sorted(numbers)) #to sort
squre = lambda x: x**2 #lambda for single use only
print(squre(int(input()))) #input() returns str so type specified
numbers = [1, 2, 3, 4]
square = lambda x: x ** 2
sq = list(map(square, numbers)) #list for creating a new list map for apply every element
print(sq)
