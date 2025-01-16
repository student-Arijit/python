class Numberchecker:
    def __init__(self, number):
        self.number = number
    
    def check_even_odd(self):
        if self._is_even():
            return f"{self.number} is even"
        else:
            return f"{self.number} is odd"
    
    def _is_even(self):
        return divmod(self.number, 2)[1] == 0

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    checker = Numberchecker(num)
    result = checker.check_even_odd()
    print(result)
