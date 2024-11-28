# loop to get 10ques -ans
quiz_dict = {}

print("Let's create a quiz with 10 questions!")
print("Enter a question and its answer.")
for i in range(1, 11):
    question = input(f"Enter question {i}: ")
    answer = input(f"Enter answer for question {i}: ")

    quiz_dict[question] = answer

print("\nYour quiz is ready! Here are the questions and their answers:")
for q, a in quiz_dict.items():
    print(f"Q: {q} \nA: {a}")
