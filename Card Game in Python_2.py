import random
import time

def Arcadius(self):
    global A_Attack, A_Wisdom, A_Athleticism, A_Immoral, A_Maniacal
    A_Attack = random.randrange(0, 50)
    A_Wisdom = random.randrange(0, 50)
    A_Athleticism = random.randrange(0, 50)
    A_Immoral = random.randrange(0, 50)
    A_Maniacal = random.randrange(0, 50)
    print("Arcadius: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
    .format(A_Attack, A_Wisdom, A_Athleticism, A_Immoral, A_Maniacal)) 

def Demetrius(self):
    global D_Attack, D_Wisdom, D_Athleticism, D_Immoral, D_Maniacal
    D_Attack = random.randrange(0, 50)
    D_Wisdom = random.randrange(0, 50)
    D_Athleticism = random.randrange(0, 50)
    D_Immoral = random.randrange(0, 50)
    D_Maniacal = random.randrange(0, 50)
    print("Demetrius: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
    .format(D_Attack, D_Wisdom, D_Athleticism, D_Immoral, D_Maniacal))

def Eugenius(self):
    global E_Attack, E_Wisdom, E_Athleticism, E_Immoral, E_Maniacal
    E_Attack = random.randrange(0, 50)
    E_Wisdom = random.randrange(0, 50)
    E_Athleticism = random.randrange(0, 50)
    E_Immoral = random.randrange(0, 50)
    E_Maniacal = random.randrange(0, 50)
    print("Eugenius: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
    .format(E_Attack, E_Wisdom, E_Athleticism, E_Immoral, E_Maniacal))
    
def Heraclius(self):
    global H_Attack, H_Wisdom, H_Athleticism, H_Immoral, H_Maniacal
    H_Attack = random.randrange(0, 50)
    H_Wisdom = random.randrange(0, 50)
    H_Athleticism = random.randrange(0, 50)
    H_Immoral = random.randrange(0, 50)
    H_Maniacal = random.randrange(0, 50)
    print("Heraclius: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
    .format(H_Attack, H_Wisdom, H_Athleticism, H_Immoral, H_Maniacal))

def battle(self):
    global P1_points
    global P2_points
    P1_points = 0
    P2_points = 0
    if fc >= 4:
        time.sleep(2)
        print("Player 1's Turn")
        self.Arcadius()
        inp = ""
        inp = input("1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
        if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
            print("You must choose 1 trait")
        else:
            pass 
        time.sleep(2)
        print("Player 2's Turn")
        self.Demetrius()
        cont = input("Press enter to continue ")
        time.sleep(2)
        if inp == "1":
            if A_Attack > D_Attack:
                print ("Player 1 wins this round")
                P1_points = P1_points + 1
            else:
                print ("Player 2 wins this round")
                P2_points = P2_points + 1
        if inp == "2":
            if Wisdom > Wisdom:
                print ("Player 1 wins this round")
                P1_points = P1_points + 1
            else:
                print ("Player 2 wins this round")
                P2_points = P2_points + 1
        if inp == "3":
            if Athleticism > Athleticism:
                print ("Player 1 wins this round")
                P1_points = P1_points + 1
            else:
                print ("Player 2 wins this round")
                P2_points = P2_points + 1
        if inp == "4":
            if Immoral > Immoral:
                print ("Player 1 wins this round")
                P1_points = P1_points + 1
            else:
                print ("Player 2 wins this round")
                P2_points = P2_points + 1
        if inp == "5":
            if Maniacal > Maniacal:
                print ("Player 1 wins this round")
                P1_points = P1_points + 1
            else:
                print ("Player 2 wins this round")
                P2_points = P2_points + 1    
    else:    
        time.sleep(3)
        print("Player 2's Turn")
        print("Demetrius: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
        .format(Attack, Wisdom, Athleticism, Immoral, Maniacal))
        inp = ""
        inp = input("1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
        if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
            print("You must choose 1 trait")
        else:
            pass 
        time.sleep(2) 
        print("Player 1's Turn")
        print("Arcadius: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
        .format(Attack, Wisdom, Athleticism, Immoral, Maniacal))
        cont = input("Press enter to continue ")
        time.sleep(2)
        if inp == "1":
            if Attack > Attack:
                print ("Player 2 wins this round")
                P2_points = P2_points + 1
            else:
                print ("Player 1 wins this round")
                P1_points = P1_points + 1
        if inp == "2":
            if Wisdom > Wisdom:
                print ("Player 2 wins this round")
                P2_points = P2_points + 1
            else:
                print ("Player 1 wins this round")
                P1_points = P1_points + 1
        if inp == "3":
            if Athleticism > Athleticism:
                print ("Player 2 wins this round")
                P2_points = P2_points + 1
            else:
                print ("Player 1 wins this round")
                P1_points = P1_points + 1
        if inp == "4":
            if Immoral > Immoral:
                print ("Player 2 wins this round")
                P2_points = P2_points + 1
            else:
                print ("Player 1 wins this round")
                P1_points = P1_points + 1
        if inp == "5":
            if Maniacal > Maniacal:
                print ("Player 2 wins this round")
                P2_points = P2_points + 1
            else:
                print ("Player 1 wins this round")
                P1_points = P1_points + 1

def firstChance(self):
    global fc
    fc = random.randint(1,6)
    time.sleep(2)
    print(fc)
    if fc >= 4:
        time.sleep(2)
        print("Player 1 goes first")
        
    else:
        time.sleep(2)
        print("Player 2 goes first")

dice = input("Press enter to roll dice ")