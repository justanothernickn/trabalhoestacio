
import time

nome = input("Nome? ")

print ("olá, " + nome, "bem-vindo ao jogo da forca!")

time.sleep(1)

print ("pode adivinhar!")
time.sleep(0.5)

palavra = ("chance")

palpites = ''

chances = 6

while chances > 0:         

    rip = 0             

    for char in palavra:      

        if char in palpites:    

            print (char,end=""),    

        else:

            print ("_",end=""),     

            rip += 1    


    if rip == 0:        
        print ("Parabens, você ganhou!")
        break            
    palpite = input(" adivinhe:") 

    palpites += palpite                    

    if palpite not in palavra:  

        chances -= 1        
 
        print ("Errou!")  

        print ("Você tem", + chances, 'palpites' )
 
        if chances == 0:           
    
            print ("Perdeu!"  )