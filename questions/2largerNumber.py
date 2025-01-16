#find the larger number betwwen two numbers

#with class
'''class findLarger:
    def __init__ (self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    
    def find_larger(self):
        return self._large()
    
    def _large(self):
        return max(self.number1, self.number2)

if __name__ == "__main__":
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")

    checker = findLarger(num1, num2)

    print(checker.find_larger())'''

#without class

print(max(int(input('enter e number')), int(input('enter another number'))))
