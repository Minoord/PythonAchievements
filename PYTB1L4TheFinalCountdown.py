from PIL import Image
afbeelding = Image.open("boo.jpg")



Cijfers = 1000

print("Start te Countdown?")
antwoord = input()
if antwoord == ("yes"):
    while (Cijfers >=0 ):
        if Cijfers != 0:
            print(Cijfers)
            Cijfers = Cijfers - 1
        else:
            afbeelding.show()
            break

elif antwoord == ("no"):
    print("I guess not then.")
else:
    print ( "I dont understand....Quiting the program") 
        
    
    
