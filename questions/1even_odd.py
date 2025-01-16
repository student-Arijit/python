#find the number is even or odd

#with class
print("The number is Even" if divmod(int(input("Enter a number: ")), 2)[1] == 0 else "The number is Odd")

#with class
'''class NumberChecker:
    def __init__(self, number):
        self.number = number
    
    def check_even_odd(self):
        if self._is_even():
            return "Even"
        else:
            return "Odd"

    def _is_even(self):
        return divmod(self.number, 2)[1] == 0
    
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    checker = NumberChecker(num)

    print(checker.check_even_odd())'''
