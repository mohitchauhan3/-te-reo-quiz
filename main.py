#4.0
#10/06/2022
print("Kia Ora Ko Wai Tou Ingoa? / meaning Hello What is your name?")
n = input()
print("Kia Ora / hello " + n )

# Asking The user name in te reo 
#is a Python quiz programme to assist the user in learning Te Reo
score = 0

#Question 1
answer1 = input("He aha te kupu mo Instagram / meaning What is the term for Instagram? \na. Paeāhua \nb. Tīhau \nc. Pukamata \nd. Pāhorangi \nAnswer: ")

if answer1 == "a" or answer1 == "A":
   score += 1
   print("CORRECT! / HAEPAPA!")
   print("score: ", score)
   print("\n")
else:
  print("hē / meaning INCORRECT! The answer is A: Paeāhua")
  print("score: ", score)
  print("\n")

#Question 2
answer2 = input("He aha te kupu mo Twitter / meaning What is the term for Twitter? \na. Tīhau \nb Paeāhua \nc. Ahokore \nd.kiriāhua: ")  
if answer2 == "a" or answer2 == "A":
  score += 1
  print("CORRECT! / HAEPAPA!")
  print("score: ", score)
  print("\n")
else:
  print("hē / meaning INCORRECT! The answer is A: Tīhau")
  print("score: ", score)
  print("\n")

#Question 3  
answer3 = input("How do you say New Zealand in Te Reo? \na. Tāmaki Makaurau \nb. Wellington \nc. Aotearoa \nd. Christchurch: ")
if answer3 == "c" or answer3 == "C" or answer3 == "aotearoa":
  score += 1
  print("CORRECT! / HAEPAPA!")
  print("score: ", score)
  print("\n")
else:
  print("hē / meaning INCORRECT! The answer is C: Aotearoa")
  print("score: ", score)
  print("\n")

  
#Question 4
answer4 = input("what Is the Te Reo word for Hungry? \na. Kai \nb. Hiakai \nc. Whāngai \nd. Hākari: ")
if answer4 == "b" or answer4 == "B":
  score += 1
  print("CORRECT! / HAEPAPA!")
  print("score: ", score)
  print("\n")
else:  
  print("hē / meaning INCORRECT! The answer is B: Hiakai")
  print("score: ", score)
  print("\n")

#Question 5
answer5 = input("How do you say auckland in Te Reo? \na.  Aotearoa \nb. Tāmaki Makaurau \nc. tauranga \nd. Christchurch : ")
if answer5 == "b" or answer5 == "B":
  score += 1
  print("CORRECT! / HAEPAPA!")
  print("score: ", score)
  print("\n")
else:  
  print("hē / meaning INCORRECT! The answer is B: Tāmaki Makaurau")
  print("score: ", score)
  print("\n")

#Question 6
answer6 = input("What is the term of LOVE in te reo? \na. Whānau \nb. Tauoko \nc. Awhi \nd. Aroha : ")
if answer6 == "d" or answer6 == "D":
  score += 1
  print("CORRECT! / HAEPAPA!")
  print("score: ", score)
  print("\n")
else:
  print("hē / meaning INCORRECT! The answer is D: Aroha")
  print("score: ", score)
  print("\n")

#Question 7
answer7 = input("How do you say one in te reo? \na. wha \nb. rua \nc. toru \nd. tahi : ")
if answer7 == "d" or answer7 == "D":
  score += 1
  print("CORRECT! / HAEPAPA!")
  print("score: ", score)
  print("\n")
else:
  print("hē / meaning INCORRECT! The answer is D: tahi")
  print("score: ", score)
  print("\n")

#Question 8
answer8 = input("How do you say Good night in te reo? \na. Kia ora \nb. Tēnā koe \nc.  haere mai \nd. pō mārie : ")
if answer8 == "d" or answer8 == "D":
  score += 1
  print("CORRECT! / HAEPAPA!")
  print("score: ", score)
  print("\n")
else:
  print("hē / meaning INCORRECT! The answer is D: pō mārie")
  print("score: ", score)
  print("\n")

#Question 9
answer9 = input("How do you tribe, nation, large group of people? \na. Whānau \nb. Aroha \nc. Iwi \nd. tahi : ")
if answer9 == "c" or answer9 == "C":
  score += 1
  print("CORRECT! / HAEPAPA!")
  print("score: ", score)
  print("\n")
else:
  print("hē / meaning INCORRECT! The answer is C: Iwi")
  print("score: ", score)
  print("\n") 

#Question 10 
answer10 = input("How do you say family in Te Reo? \na. Whānau \nb. tahi \nc. Iwi \nd. Aroha : ")
if answer10 == "a" or answer10 == "A":
  score += 1
  print("CORRECT! / HAEPAPA!")
  print("score: ", score)
  print("\n")
else:
  print("hē / meaning INCORRECT! The answer is A: Whānau")
  print("score: ", score)
  print("\n")   

#Question 11 
answer11 = input("how do you say Good morning in Te Reo \na. Kia ora \nb. Kei te pai \nc. Tino pai \nd. Mōrena : ")
if answer11 == "d" or answer11 == "D":
  score += 1
  print("CORRECT! / HAEPAPA!")
  print("score: ", score)
  print("\n")
else:
  print("hē / meaning INCORRECT! The answer is D: Mōrena")
  print("score: ", score)
  print("\n")     

#Question 12
answer12 = input("How do you say goodbye in Te Reo? \na. Kia ora \nb. Ka kite anō \nc. Kei te pai \nd. Mōrena : ")
if answer12 == "b" or answer12 == "B":
  score += 1
  print("CORRECT! / HAEPAPA!")
  print("score: ", score)
  print("\n")
else:
  print("hē / meaning INCORRECT! The answer is B: Ka kite anō")
  print("score: ", score)
  print("\n") 

if score <= 1:
  print("Your total score is:", score, "- better luck next time")
elif score == 2:
  print("you total score is:", score, "- you went ok.")
else:
  print("your total score is:", score, "- your amazing ")  
    
  

