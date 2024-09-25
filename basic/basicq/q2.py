#Write a program that checks if a user is eligible to vote. A user is eligible if they are 18 years or older.
vote = lambda x: [["no", "not"], ["yes", ""]][x >= 18]
result = vote(int(input("Enter your age: ")))
print(result[0] + ", you\'re " + result[1] + " eligible", sep = " ")
