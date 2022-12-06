score = 0
with open('questions.txt','r') as f:
  question = f.readline().strip()
  while question != "":
    optionA = f.readline().strip()
    optionB = f.readline().strip()
    optionC = f.readline().strip()
    optionD = f.readline().strip()
    answer = f.readline().strip()

    print(question)
    
    print(optionA)
    print(optionB)
    print(optionC)
    print(optionD)
  
    myAnswer = input("What is your answer? ")
    if myAnswer[0] == answer:
      print ("Correct!")
      score = score + 1
    else: 
      print("Better luck next time!")
    print("")
    
    question = f.readline().strip()

print("You got "+ str(score))