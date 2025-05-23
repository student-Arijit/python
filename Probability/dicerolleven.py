omega = [1, 2, 3, 4, 5, 6]

A = [i for i in omega if i % 2 == 0]

P_A = len(A) / len(omega)

print(f'"Probability of even outcome is {P_A:.2f}"')
