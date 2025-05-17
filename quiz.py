questions = ("1. What is the capital city of France?",
             "2. What is the chemical symbol for water?",
             "3. Who wrote the play 'Romeo and Juliet'?",
             "4. Which planet is known as the 'Red Planet'?",
             "5. What is the largest mammal in the world?")

options = (("A) Berlin", "B) Madrid", "C) Paris", "D) Rome"),
           ("A) CO₂", "B) H₂O", "C) NaCl", "D) O₂"),
           ("A) William Shakespeare", "B) Charles Dickens", "C) Mark Twain", "D) Jane Austen"),
           ("A) Jupiter", "B) Mars", "C) Venus", "D) Saturn"),
           ("A) African Elephant", "B) Blue Whale", "C) Giraffe", "D) Polar Bear"))

question_num = 0
answers = ("C", "B", "A", "B", "B")
guesses = []
score = 0.0

for question in questions:
    print("_______________________________________________")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter your ans: (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("Correct")
        score += 1
    else:
        print("Incorrect")
        print(f"Correct ans is {answers[question_num]}")
        score -= 0.5
    question_num += 1

print("_____ RESULT _____")
for answer in answers:
    print(answer, end=" ")
print()
for guess in guesses:
    print(guess, end=" ")

print()
print(f"Your final score is {score}")

if score > 3.0:
    print("Good")
elif 3.0 > score > 2.0:
    print("Average")
else:
    print("Try Hard! You can do it")