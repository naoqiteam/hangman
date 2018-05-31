naam = input("Wat is jouw naam? ")
print ("Hallo " + naam +", Het is tijd om galgje te spelen!")
print (" ")

#----------------------^^niet belangrijk^^------------------------------

print ("Start maar met raden")


import random
data = ['peer','appel','woord','perzik','ananas']
woord = random.choice(data)

guesses = ''
kansen = 10

while kansen > 0:         
    failed = 0               

    for char in woord:      
        if char in guesses:    
            print (char,)    
        else:
            print ("_"),     
            failed += 1
            
    if failed == 0:        
        print ("Jij wint")
        
        break              
    
    guess = input("Raad een letter:") 
    guesses += guess
    
    if guess not in woord:  
        kansen -= 1        
        print ("Fout")    
        print ("Jij hebt nog", + kansen, 'kansen') 

        if kansen == 0:           
            print ("Jij verliest")
