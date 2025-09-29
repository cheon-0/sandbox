print("Welcom to the Python Quiz!")
score = 0

# Question 1
answer = input("Q1: What keyword is used to define a fuction in Python? ")
if answer.lower() == "def":
    print("Correct!")
    score += 1
else:
    print("Oops, the answer is 'def'.")

# Question 2
answer = input("Q2 : What symbol is used for modulo(remainder) in Python? ")
if answer == "%":
    print("Correct!")
    score += 1
else:
    print("Oops, the answer is '%'.")

# Question 3
answer = input("Q3 : What will this print : print(2 * 3)? ")
if answer == "6":
    print("Correct!")
    score += 1
else:
    print("Oops, the answer is '6'.")

print(f"/n Your final score is {score}/3")
