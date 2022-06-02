#1.2
print("Kia Ora Ko Wai Tou Ingoa? / meaning Hello What is your name?")
n = input()
print("Kia Ora / hello " + n )

# Asking The user name in te reo 

score = 0

#Question 1
answer1 = input("What is the term for Instagram? \na. Paeāhua \nb. Tīhau \nc. Pukamata \nd. Pāhorangi \nAnswer: ")

if answer1 == "a" or answer1 == "A":
   score += 1
   print("CORRECT!")
   print("score: ", score)
   print("\n")
else:
  print("INCORRECT! The answer is A: Paeāhua")
  print("score: ", score)
  print("\n")

#Question 2
answer2 = input("What is the term for Twitter? \na. Tīhau \nb Paeāhua \nc. Ahokore \nd.kiriāhua: ")  
if answer2 == "a" or answer2 == "A":
  score += 1
  print("CORRECT!")
  print("score: ", score)
  print("\n")
else:
  print("INCORRECT! The answer is A: Tīhau")
  print("score: ", score)
  print("\n")

#Question 3  


