def GetAnimals(p_number):
    Dogs = 0
    Cats = 0
    Mice = 0
    for i in range(1, p_number):
        prime = True
        for p in range(2,(i - 1)):
            if (i % p) == 0:
                prime = False
        if prime: #If prime, then doesn't divide into 3, 5 or anything else
            print(i, ': Dog')
            Dogs = Dogs + 1
        elif (i % 3) == 0 and (i % 5) == 0:
            #print(i, ': Cat and Mouse')
            Cats = Cats + 1
            Mice = Mice + 1
        elif (i % 3) == 0:
            print(i, ': Cat')
            #Cats = Cats + 1
        elif (i % 5) == 0:
            print(i, ': Mouse')
            #Mice = Mice + 1
        else:
            print(i)

    #print(Dogs, " dogs!")
    #print(Cats, " cats!")
    #print(Mice, " mice!")
    return Dogs, Cats, Mice
