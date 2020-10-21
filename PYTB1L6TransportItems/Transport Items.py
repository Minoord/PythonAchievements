import time 

Factory = [ ] 
Distribution = [ ]
Shop = [ ]

Car = True
while ( Car == True ) :
    print("Factory =" + str(Factory) )
    print("Distribution =" + str(Distribution))
    print("Shop =" + str(Shop) ) 
    print("Start the production? Y/N")
    Antwoord = input()
    if Antwoord == "Y" or Antwoord == "y":
        print("Building a car. . .")
        Factory.append("car")
        time.sleep(1)
        print("Car build")
        time.sleep(1)
        print("factory = " + str(Factory))
        print("Distribution =" + str(Distribution))
        print("Shop =" + str(Shop))
        print("-----------------------------------------------")
        time.sleep(1)
        print("Transporting the car. . .")
        Distribution.append("car")
        time.sleep(1)
        Factory.clear()
        print("The car has reach the Distribution")
        time.sleep(1)
        print("factory = " + str(Factory))
        print("Distribution =" + str(Distribution))
        print("Shop =" + str(Shop))
        print("-----------------------------------------------")
        time.sleep(1)
        print("Transporting the car. . .")
        Distribution.clear()
        Shop.append ("car")
        time.sleep(1)
        print("The car has reach the store")
        time.sleep(1)
        print("factory = " + str(Factory))
        print("Distribution =" + str(Distribution))
        print("Shop =" + str(Shop))
        print("---------------------------------------------")
        time.sleep(1)
        print("Car is being sold")
        Shop.clear()
        time.sleep(1)
        print("The car is sold")
        time.sleep(1)
        print("factory = " + str(Factory))
        print("Distribution =" + str(Distribution))
        print("Shop =" + str(Shop))
        print("--------------------------------------------")
        time.sleep(1)
        print("Would you like to produce more cars? Y/N")
        Antword = input()
        if Antword == "Y" or Antword == "y":
            Car = True
        else:
            print ("Shutting down the program")
            Car = False
    else:
        print ("Shutting down the program")
        Car = False
    
