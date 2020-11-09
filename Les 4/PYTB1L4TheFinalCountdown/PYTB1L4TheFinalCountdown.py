

Cijfer = True
Cijfers = 1000

print("Start te Countdown?")
antwoord = input()
if antwoord == ("yes"):
    while (Cijfer == True):
        print(Cijfers)
        Cijfers = Cijfers - 1
    if ( Cijfers == "0" ):
        break 
    
    else:
        print (Cijfers)
        Cijfers = Cijfers - 1
elif antwoord == ("no"):
    print("I guess not then.")
else:
    print ( "I dont understand....Quiting the program") 
        
    
    
