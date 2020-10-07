#Doel:
# Codeer de lijst met namen
# Gebruik een for loop of een while loop om door de lijst te krijgen
#print Dus: Waldo zit op stoel nr...
#print de lijst met name
# check of alles werkt

import random
people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)

zitpleknummer = 1;
for ppl in people: 
 
    if ( ppl ==  "Waldo"   ) :
        isRunning = False
        print("Waldo is found")
        print("Dus Waldo zit op stoel nr", zitpleknummer )
        print(people)
        print("Klopt De Stoel nummer ( Ja of Nee )?") 
        Antwoord= input()
        if ( Antwoord == "ja", "Ja", "JA", "jA"):
            print("Dat is mooi!, wil je dit nog een keer doen? Bedankt voor het testen.")
        elif ( Antwoord ==  "Nee","nee","NEE", ):
            print("Dat is jammer, dan ben ik niet goed geprogameerd. Bedankt voor het testen.")
        else:
            print("Sorry, ik berijp dit niet. Bedankt voor het testen.")
                
            
        
        break

    else:
        zitpleknummer = zitpleknummer + 1
        print("Scanning")



  
      
