#1.5
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
answer3 = input("How do you say New Zealand in Te Reo? \na. Tāmaki Makaurau \nb. Wellington \nc. Aotearoa \nd. Christchurch: ")
if answer3 == "c" or answer3 == "C" or answer3 == "aotearoa":
  score += 1
  print("CORRECT!")
  print("score: ", score)
  print("\n")
else:
  print("INCORRECT! The answer is C: Aotearoa")
  print("score: ", score)
  print("\n")

  
#Question 4
answer4 = input("what Is the Te Reo word for Hungry? \na. Kai \nb. Hākari \nc. Whāngai \nd. Hākari: ")
if answer4 == "b" or answer4 == "B":
  score += 1
  print("CORRECT!")
  print("score: ", score)
  print("\n")
else:  
  print("INCORRECT! The answer is B: Hākari")
  print("score: ", score)
  print("\n")

#Question 5
answer5 = input("How do you say auckland in Te Reo? \na.  Aotearoa \nb. Tāmaki Makaurau \nc. tauranga \nd. Christchurch : ")
if answer5 == "b" or answer5 == "B":
  score += 1
  print("CORRECT!")
  print("score: ", score)
  print("\n")
else:  
  print("INCORRECT! The answer is B: Tāmaki Makaurau")
  print("score: ", score)
  print("\n")
