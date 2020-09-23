print("Wat is jou naam?") 
naam= input()
print("Hallo " + naam + ", Hoe oud ben je?")
leeftijd= input()
print("Wat is jouw favriete hobby?")
hobby= input()
if hobby == 'lezen':
     print(" Cool, mijn hobby is ook lezen.")
else:
     print("Cool, Mischien moet ik dat ook eens een keer proberen.")
print(" ")
print(" ")
print("Zo jij bent " + naam + ". Jij bent " + leeftijd + " jaar oud en jouw favoriete hobby is " + hobby + ". Dit klopt toch?")
antwoord= input() 
if antwoord == 'ja':
     print("Dus dan ben ik toch goed geprogammeerd.Bedankt voor het testen!")  
elif antwoord == 'nee':
     print(" Dan heb jij iets verkeerds getypt. Dat geeft niet maar probeer er op te letten. Als nog bedankt voor het testen!")
else:
     print("Ik begrijp dit antwoord niet, sorry. Als nog bedankt voor het testen.")  