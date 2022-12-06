with open('questions.txt','r') as f:
  question = f.readline().strip()
  optionA = f.readline().strip()
  optionB = f.readline().strip()
  optionC = f.readline().strip()
  optionD = f.readline().strip()
  answer = f.readline().strip()

print(optionA)
print(optionB)
print(optionC)
print(optionD)

myAnswer = input("What is your answer? ")
if myAnswer[0] == answer:
  print ("Correct!")
else: 
  print("Better luck next time!")