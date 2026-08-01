#Implement bisection method to find a positive root from a non-linear equation.

from tabulate import tabulate

class BisectionMethod:
  def __init__(self, a, b, f):
    self.a = a
    self.b = b
    self.func = f
    self.entry = []
  
  def solve(self, iterations=20, tolerance=1e-6):
    if self.func(self.a)*self.func(self.b) >= 0:
      raise ValueError("Invaild Interval")
    a = self.a
    b = self.b

    for step in range(1, iterations+1):
      c = (a+b)/2
      f = self.func
      self.entry.append([
          step,
          a,
          b,
          c,
          f(c)
      ])

      if f(c) > 0:
        b = c
      elif f(c) < 0:
        a = c
      
      if abs(f(c)) < tolerance:
        break
      
    return c

  def display(self):
    headers = [
            "Step",
            "a",
            "b",
            "Midpoint",
            "f(c)"
        ]
    print(tabulate(self.entry, headers=headers, tablefmt="fancy_grid", floatfmt=".6f"))

def f(x):
  return ((x*x*x) - (2*x) - 5)

b = BisectionMethod(2, 3, f)
root = b.solve(iterations=15)
b.display()

print(f"\nApproximate Root: {round(root, 6)}")
