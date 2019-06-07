import random, time, sys

class MyCardGame():
    #Round 1 Player 1
    def Arcadius(self):
        global A_Attack, A_Wisdom, A_Athleticism, A_Immoral, A_Maniacal
        A_Attack = random.randrange(0, 50)
        A_Wisdom = random.randrange(0, 50)
        A_Athleticism = random.randrange(0, 50)
        A_Immoral = random.randrange(1, 50)
        A_Maniacal = random.randrange(1, 50)
        '''print("Arcadius: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
        .format(A_Attack, A_Wisdom, A_Athleticism, A_Immoral, A_Maniacal))'''

    #Round 1 Player 2
    def Demetrius(self):
        global D_Attack, D_Wisdom, D_Athleticism, D_Immoral, D_Maniacal
        D_Attack = random.randrange(0, 50)
        D_Wisdom = random.randrange(0, 50)
        D_Athleticism = random.randrange(0, 50)
        D_Immoral = random.randrange(1, 50)
        D_Maniacal = random.randrange(1, 50)
        '''print("Demetrius: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
        .format(D_Attack, D_Wisdom, D_Athleticism, D_Immoral, D_Maniacal))'''
    
    #Round 2 Player 1
    def Eugenius(self):
        global E_Attack, E_Wisdom, E_Athleticism, E_Immoral, E_Maniacal
        E_Attack = random.randrange(0, 50)
        E_Wisdom = random.randrange(0, 50)
        E_Athleticism = random.randrange(0, 50)
        E_Immoral = random.randrange(1, 50)
        E_Maniacal = random.randrange(1, 50)
        '''print("Eugenius: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
        .format(E_Attack, E_Wisdom, E_Athleticism, E_Immoral, E_Maniacal))'''

    #Round 2 Player 2    
    def Heraclius(self):
        global H_Attack, H_Wisdom, H_Athleticism, H_Immoral, H_Maniacal
        H_Attack = random.randrange(0, 50)
        H_Wisdom = random.randrange(0, 50)
        H_Athleticism = random.randrange(0, 50)
        H_Immoral = random.randrange(1, 50)
        H_Maniacal = random.randrange(1, 50)
        '''print("Heraclius: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
        .format(H_Attack, H_Wisdom, H_Athleticism, H_Immoral, H_Maniacal))'''

    #Round 3 Player 1
    def Orpheus(self):
        global O_Attack, O_Wisdom, O_Athleticism, O_Immoral, O_Maniacal
        O_Attack = random.randrange(0, 50)
        O_Wisdom = random.randrange(0, 50)
        O_Athleticism = random.randrange(0, 50)
        O_Immoral = random.randrange(1, 50)
        O_Maniacal = random.randrange(1, 50)
        '''print("Orpheus: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
        .format(O_Attack, O_Wisdom, O_Athleticism, O_Immoral, O_Maniacal))'''
    
    #Round 3 Player 2
    def Bastian(self):
        global B_Attack, B_Wisdom, B_Athleticism, B_Immoral, B_Maniacal
        B_Attack = random.randrange(0, 50)
        B_Wisdom = random.randrange(0, 50)
        B_Athleticism = random.randrange(0, 50)
        B_Immoral = random.randrange(1, 50)
        B_Maniacal = random.randrange(1, 50)
        '''print("Bastian: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
        .format(B_Attack, B_Wisdom, B_Athleticism, B_Immoral, B_Maniacal))'''

    #Round 4 Player 1
    def Zeuxis(self):
        global Z_Attack, Z_Wisdom, Z_Athleticism, Z_Immoral, Z_Maniacal
        Z_Attack = random.randrange(0, 50)
        Z_Wisdom = random.randrange(0, 50)
        Z_Athleticism = random.randrange(0, 50)
        Z_Immoral = random.randrange(1, 50)
        Z_Maniacal = random.randrange(1, 50)
        '''print("Zeuxis: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
        .format(Z_Attack, Z_Wisdom, Z_Athleticism, Z_Immoral, Z_Maniacal))'''

    #Round 4 Player 2
    def Pericles(self):
        global P_Attack, P_Wisdom, P_Athleticism, P_Immoral, P_Maniacal
        P_Attack = random.randrange(0, 50)
        P_Wisdom = random.randrange(0, 50)
        P_Athleticism = random.randrange(0, 50)
        P_Immoral = random.randrange(1, 50)
        P_Maniacal = random.randrange(1, 50)
        '''print("Pericles: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
        .format(P_Attack, P_Wisdom, P_Athleticism, P_Immoral, P_Maniacal))'''
    
    #Round 5 Player 1
    def Irenaeus(self):
        global I_Attack, I_Wisdom, I_Athleticism, I_Immoral, I_Maniacal
        I_Attack = random.randrange(0, 50)
        I_Wisdom = random.randrange(0, 50)
        I_Athleticism = random.randrange(0, 50)
        I_Immoral = random.randrange(1, 50)
        I_Maniacal = random.randrange(1, 50)
        '''print("Irenaeus: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
        .format(I_Attack, I_Wisdom, I_Athleticism, I_Immoral, I_Maniacal))'''

    #Round 5 Player 2
    def Cyril(self):
        global C_Attack, C_Wisdom, C_Athleticism, C_Immoral, C_Maniacal
        C_Attack = random.randrange(0, 50)
        C_Wisdom = random.randrange(0, 50)
        C_Athleticism = random.randrange(0, 50)
        C_Immoral = random.randrange(1, 50)
        C_Maniacal = random.randrange(1, 50)
        '''print("Cyril: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
        .format(C_Attack, C_Wisdom, C_Athleticism, C_Immoral, C_Maniacal))'''

    def roundOne(self):
        print("\nROUND 1")
        global P1_points, P2_points, R1_1, R1_2, checkGS1_1, checkGS2_1
        P1_points = P2_points = R1_1 = R1_2 = checkGS1_1 = checkGS2_1 = 0
        if fc1 > fc2:
            time.sleep(2)
            print("\nPlayer 1's Turn")
            print("\nThe card picked is: \nArcadius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
            .format(A_Attack, A_Wisdom, A_Athleticism, A_Immoral, A_Maniacal))
            inp = ""
            inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
            if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                print("You must choose 1 trait")
                sys.exit()
                #raise NoTraitChosenError
            else:
                inpg = ""
                inpg = input("\nDo you want to use the God Spell? (Y/N) \n")
                if inpg == "Y" or inpg == "Yes" or inpg == "y" or inpg == "yes":
                    if checkGS1_1 == 0:
                        checkGS1_1 = checkGS1_1 + 1
                        print("\nThe card picked by Player 2 is: \nDemetrius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(D_Attack, D_Wisdom, D_Athleticism, D_Immoral, D_Maniacal))
                        time.sleep(2)
                        print("\nThe strength of each character is changed (random)")
                        time.sleep(2)
                        self.Demetrius()
                        time.sleep(2)
                        print("\nPlayer 1 used the god spell")
                        pass
                    else:
                        print("\nGod Spell has already been used by you.\n")
                        pass
                else:
                    pass
            time.sleep(2)
            print("\nPlayer 2's Turn")
            print("\nThe card picked is: \nDemetrius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
            .format(D_Attack, D_Wisdom, D_Athleticism, D_Immoral, D_Maniacal))
            _cont = input("\nPress enter to continue \n")
            time.sleep(2)
            if inp == "1":
                if A_Attack > D_Attack:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R1_1 = R1_1 + 1
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R1_2 = R1_2 + 1
            if inp == "2":
                if A_Wisdom > D_Wisdom:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R1_1 = R1_1 + 1
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R1_2 = R1_2 + 1
            if inp == "3":
                if A_Athleticism > D_Athleticism:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R1_1 = R1_1 + 1
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R1_2 = R1_2 + 1
            if inp == "4":
                if A_Immoral < D_Immoral:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R1_1 = R1_1 + 1
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R1_2 = R1_2 + 1
            if inp == "5":
                if A_Maniacal < D_Maniacal:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R1_1 = R1_1 + 1
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1 
                    R1_2 = R1_2 + 1
        else:    
            time.sleep(3)
            print("\nPlayer 2's Turn")
            print("\nThe card picked is: \nDemetrius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
            .format(D_Attack, D_Wisdom, D_Athleticism, D_Immoral, D_Maniacal))
            inp = ""
            inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
            if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                print("You must choose 1 trait")
                sys.exit()
                #raise NoTraitChosenError
            else:
                inpg = ""
                inpg = input("\nDo you want to use the God Spell? (Y/N) ")
                if inpg == "Y" or inpg == "Yes" or inpg == "y" or inpg == "yes":
                    if checkGS2_1 == 0:
                        checkGS2_1 = checkGS2_1 + 1
                        print("\nThe card picked by Player 1 is: \nArcadius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(A_Attack, A_Wisdom, A_Athleticism, A_Immoral, A_Maniacal))
                        time.sleep(2)
                        print("\nThe strength of each character is changed (random)")
                        self.Arcadius()
                        time.sleep(2)
                        print("\nPlayer 2 used the god spell")
                        pass
                    else:
                        print("\nGod Spell has already been used by you.\n")
                        pass
                else:
                    pass 
            time.sleep(2) 
            print("\nPlayer 1's Turn")
            print("\nThe card picked is: \nArcadius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
            .format(A_Attack, A_Wisdom, A_Athleticism, A_Immoral, A_Maniacal))
            _cont = input("\nPress enter to continue \n")
            time.sleep(2)
            if inp == "1":
                if D_Attack > A_Attack:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R1_2 = R1_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R1_1 = R1_1 + 1
            if inp == "2":
                if D_Wisdom > A_Wisdom:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R1_2 = R1_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R1_1 = R1_1 + 1
            if inp == "3":
                if D_Athleticism > A_Athleticism:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R1_2 = R1_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R1_1 = R1_1 + 1
            if inp == "4":
                if D_Immoral < A_Immoral:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R1_2 = R1_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R1_1 = R1_1 + 1
            if inp == "5":
                if D_Maniacal < A_Maniacal:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R1_2 = R1_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R1_1 = R1_1 + 1

    def roundTwo(self):
        print("\nROUND 2")
        global P1_points, P2_points, R1_1, R1_2, R2_1, R2_2, checkGS1_2, checkGS2_2, checkRS1_2, checkRS2_2
        R2_1 = R2_2 = checkGS1_2 = checkGS2_2 = checkRS1_2 = checkRS2_2 = 0
        checkGS1_2 = checkGS1_1
        checkGS2_2 = checkGS2_1
        if R1_1 > R1_2:
            time.sleep(2)
            print("\nPlayer 1's Turn")
            if checkRS1_2 == 0:
                inpr = ""
                inpr = input("\nDo you want to use the Resurrect Spell? (Y/N) ")
                if inpr == "Y" or inpr == "Yes" or inpr == "y" or inpr == "yes":
                    checkRS1_2 = checkRS1_2 + 1
                    time.sleep(2)
                    print("\nUsing Resurrect Spell...")
                    time.sleep(2)
                    print("The Outdated Deck has 1 card")
                    time.sleep(2)
                    print("\nThe card picked is: \nArcadius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                    .format(A_Attack, A_Wisdom, A_Athleticism, A_Immoral, A_Maniacal))
                    inp = ""
                    inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
                    if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                        print("You must choose 1 trait")
                        sys.exit()
                        #raise NoTraitChosenError
                    else:
                        pass 
                    time.sleep(2)
                    print("\nPlayer 2's Turn")
                    print("\nThe card picked is: \nHeraclius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                    .format(H_Attack, H_Wisdom, H_Athleticism, H_Immoral, H_Maniacal))
                    _cont = input("\nPress enter to continue \n")
                    time.sleep(2)
                    if inp == "1":
                        if A_Attack > H_Attack:
                            print ("Player 1 wins this round")
                            P1_points = P1_points + 1
                            R2_1 = R2_1 + 1
                        else:
                            print ("Player 2 wins this round")
                            P2_points = P2_points + 1
                            R2_2 = R2_2 + 1
                    if inp == "2":
                        if A_Wisdom > H_Wisdom:
                            print ("Player 1 wins this round")
                            P1_points = P1_points + 1
                            R2_1 = R2_1 + 1
                        else:
                            print ("Player 2 wins this round")
                            P2_points = P2_points + 1
                            R2_2 = R2_2 + 1
                    if inp == "3":
                        if A_Athleticism > H_Athleticism:
                            print ("Player 1 wins this round")
                            P1_points = P1_points + 1
                            R2_1 = R2_1 + 1
                        else:
                            print ("Player 2 wins this round")
                            P2_points = P2_points + 1
                            R2_2 = R2_2 + 1
                    if inp == "4":
                        if A_Immoral < H_Immoral:
                            print ("Player 1 wins this round")
                            P1_points = P1_points + 1
                            R2_1 = R2_1 + 1
                        else:
                            print ("Player 2 wins this round")
                            P2_points = P2_points + 1
                            R2_2 = R2_2 + 1
                    if inp == "5":
                        if A_Maniacal < H_Maniacal:
                            print ("Player 1 wins this round")
                            P1_points = P1_points + 1
                            R2_1 = R2_1 + 1
                        else:
                            print ("Player 2 wins this round")
                            P2_points = P2_points + 1
                            R2_2 = R2_2 + 1
                    return
                else:
                    #Not using resurrect spell
                    pass
            else:
                #No resurrect spell left
                pass
            print("\nThe card picked is: \nEugenius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
            .format(E_Attack, E_Wisdom, E_Athleticism, E_Immoral, E_Maniacal))
            inp = ""
            inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
            if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                print("You must choose 1 trait")
                sys.exit()
                #raise NoTraitChosenError
            else:
                inpg = ""
                inpg = input("\nDo you want to use the God Spell? (Y/N) \n")
                if inpg == "Y" or inpg == "Yes" or inpg == "y" or inpg == "yes":
                    if checkGS1_2 == 0: 
                        checkGS1_2 = checkGS1_2 + 1
                        print("\nThe card picked by Player 2 is: \nHeraclius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(H_Attack, H_Wisdom, H_Athleticism, H_Immoral, H_Maniacal))
                        time.sleep(2)
                        time.sleep(2)
                        print("\nThe strength of each character is changed (random)")
                        self.Heraclius()
                        time.sleep(2)
                        print("\nPlayer 1 used the god spell")
                        pass
                    else:
                        print("\nGod Spell has already been used by you.\n")
                        pass
                else:
                    #Not using god spell
                    pass 
            time.sleep(2)
            print("\nPlayer 2's Turn")
            print("\nThe card picked is: \nHeraclius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
            .format(H_Attack, H_Wisdom, H_Athleticism, H_Immoral, H_Maniacal))
            _cont = input("\nPress enter to continue \n")
            time.sleep(2)
            if inp == "1":
                if E_Attack > H_Attack:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R2_1 = R2_1 + 1
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R2_2 = R2_2 + 1
            if inp == "2":
                if E_Wisdom > H_Wisdom:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R2_1 = R2_1 + 1
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R2_2 = R2_2 + 1
            if inp == "3":
                if E_Athleticism > H_Athleticism:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R2_1 = R2_1 + 1
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R2_2 = R2_2 + 1
            if inp == "4":
                if E_Immoral < H_Immoral:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R2_1 = R2_1 + 1
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R2_2 = R2_2 + 1
            if inp == "5":
                if E_Maniacal < H_Maniacal:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R2_1 = R2_1 + 1
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R2_2 = R2_2 + 1
        else:    
            time.sleep(3)
            print("\nPlayer 2's Turn")
            if checkRS2_2 == 0:
                inpr = ""
                inpr = input("\nDo you want to use the Resurrect Spell? (Y/N) \n")
                if inpr == "Y" or inpr == "Yes" or inpr == "y" or inpr == "yes":
                    checkRS2_2 = checkRS2_2 + 1
                    time.sleep(2)
                    print("\nUsing Resurrect Spell...")
                    time.sleep(2)
                    print("The Outdated Deck has 1 card")
                    time.sleep(2)
                    print("\nThe card picked is: \nDemetrius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                    .format(D_Attack, D_Wisdom, D_Athleticism, D_Immoral, D_Maniacal))
                    inp = ""
                    inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
                    if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                        print("You must choose 1 trait")
                        sys.exit()
                        #raise NoTraitChosenError
                    else:
                        pass 
                    time.sleep(2)
                    print("\nPlayer 1's Turn")
                    print("\nThe card picked is: \nEugenius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                    .format(E_Attack, E_Wisdom, E_Athleticism, E_Immoral, E_Maniacal))
                    _cont = input("\nPress enter to continue \n")
                    time.sleep(2)
                    if inp == "1":
                        if D_Attack > E_Attack:
                            print ("Player 2 wins this round")
                            P2_points = P2_points + 1
                            R2_2 = R2_2 + 1
                        else:
                            print ("Player 1 wins this round")
                            P1_points = P1_points + 1
                            R2_1 = R2_1 + 1
                    if inp == "2":
                        if D_Wisdom > E_Wisdom:
                            print ("Player 2 wins this round")
                            P2_points = P2_points + 1
                            R2_2 = R2_2 + 1
                        else:
                            print ("Player 1 wins this round")
                            P1_points = P1_points + 1
                            R2_1 = R2_1 + 1
                    if inp == "3":
                        if D_Athleticism > E_Athleticism:
                            print ("Player 2 wins this round")
                            P2_points = P2_points + 1
                            R2_2 = R2_2 + 1
                        else:
                            print ("Player 1 wins this round")
                            P1_points = P1_points + 1
                            R2_1 = R2_1 + 1
                    if inp == "4":
                        if D_Immoral < E_Immoral:
                            print ("Player 2 wins this round")
                            P2_points = P2_points + 1
                            R2_2 = R2_2 + 1
                        else:
                            print ("Player 1 wins this round")
                            P1_points = P1_points + 1
                            R2_1 = R2_1 + 1
                    if inp == "5":
                        if D_Maniacal < E_Maniacal:
                            print ("Player 2 wins this round")
                            P2_points = P2_points + 1
                            R2_2 = R2_2 + 1
                        else:
                            print ("Player 1 wins this round")
                            P1_points = P1_points + 1
                            R2_1 = R2_1 + 1
                    return
                else:
                    pass
            else:
                pass
            print("\nThe card picked is: \nHeraclius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
            .format(H_Attack, H_Wisdom, H_Athleticism, H_Immoral, H_Maniacal))
            inp = ""
            inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
            if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                print("You must choose 1 trait")
                sys.exit()
                #raise NoTraitChosenError
            else:
                inpg = ""
                inpg = input("\nDo you want to use the God Spell? (Y/N) \n")
                if inpg == "Y" or inpg == "Yes" or inpg == "y" or inpg == "yes":
                    if checkGS2_2 == 0:
                        checkGS2_2 = checkGS2_2 + 1
                        print("\nThe card picked by Player 1 is: \nEugenius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(E_Attack, E_Wisdom, E_Athleticism, E_Immoral, E_Maniacal))
                        time.sleep(2)
                        print("\nThe strength of each character is changed (random)")
                        time.sleep(2)
                        self.Eugenius()
                        time.sleep(2)
                        print("\nPlayer 2 used the god spell")
                        pass
                    else:
                        print("\nGod Spell has already been used by you.\n")
                        pass
                else:
                    pass 
            time.sleep(2) 
            print("\nPlayer 1's Turn")
            print("\nThe card picked is: \nEugenius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
            .format(E_Attack, E_Wisdom, E_Athleticism, E_Immoral, E_Maniacal))
            _cont = input("\nPress enter to continue \n")
            time.sleep(2)
            if inp == "1":
                if H_Attack > E_Attack:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R2_2 = R2_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R2_1 = R2_1 + 1
            if inp == "2":
                if H_Wisdom > E_Wisdom:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R2_2 = R2_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R2_1 = R2_1 + 1
            if inp == "3":
                if H_Athleticism > E_Athleticism:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R2_2 = R2_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R2_1 = R2_1 + 1
            if inp == "4":
                if H_Immoral < E_Immoral:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R2_2 = R2_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R2_1 = R2_1 + 1
            if inp == "5":
                if H_Maniacal < E_Maniacal:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R2_2 = R2_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R2_1 = R2_1 + 1

    def roundThree(self):
        print("\nROUND 3")
        global P1_points, P2_points, R2_1, R2_2, R3_1, R3_2, checkGS1_3, checkGS2_3, checkRS1_3, checkRS2_3
        R3_1 = R3_2 = checkGS1_3 = checkGS2_3 = checkRS1_3 = checkRS2_3 = 0
        checkGS1_3 = checkGS1_2
        checkGS2_3 = checkGS2_2
        checkRS1_3 = checkRS1_2
        checkRS2_3 = checkRS2_2
        if R2_1 > R2_2:
            #Last round was won by Player 1
            time.sleep(2)
            print("\nPlayer 1's Turn")
            if checkRS1_3 == 0:
                inpr = ""
                inpr = input("\nDo you want to use the Resurrect Spell? (Y/N) ")
                if inpr == "Y" or inpr == "Yes" or inpr == "y" or inpr == "yes":
                    checkRS1_3 = checkRS1_3 + 1
                    time.sleep(2)
                    print("\nUsing Resurrect Spell...")
                    time.sleep(2)
                    print("The Outdated Deck has 2 cards")
                    time.sleep(2)
                    n = random.randint(1,2)
                    if n == 1:
                        #Arcadius for Player 1
                        print("\nThe card picked is: \nArcadius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(A_Attack, A_Wisdom, A_Athleticism, A_Immoral, A_Maniacal))
                        inp = ""
                        inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
                        if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                            print("You must choose 1 trait")
                            sys.exit()
                            #raise NoTraitChosenError
                        else:
                            pass 
                        time.sleep(2)
                        print("\nPlayer 2's Turn")
                        print("\nThe card picked is: \nBastian \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(B_Attack, B_Wisdom, B_Athleticism, B_Immoral, B_Maniacal))
                        _cont = input("\nPress enter to continue \n")
                        time.sleep(2)
                        if inp == "1":
                            if A_Attack > B_Attack:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R3_1 = R3_1 + 1
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R3_2 = R3_2 + 1
                        if inp == "2":
                            if A_Wisdom > B_Wisdom:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R3_1 = R3_1 + 1
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R3_2 = R3_2 + 1
                        if inp == "3":
                            if A_Athleticism > B_Athleticism:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R3_1 = R3_1 + 1
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R3_2 = R3_2 + 1
                        if inp == "4":
                            if A_Immoral < B_Immoral:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R3_1 = R3_1 + 1
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R3_2 = R3_2 + 1
                        if inp == "5":
                            if A_Maniacal < B_Maniacal:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R3_1 = R3_1 + 1
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R3_2 = R3_2 + 1
                        return
                    else:
                        #Eugenius for Player 1
                        print("\nThe card picked is: \nEugenius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(E_Attack, E_Wisdom, E_Athleticism, E_Immoral, E_Maniacal))
                        inp = ""
                        inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
                        if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                            print("You must choose 1 trait")
                            sys.exit()
                            #raise NoTraitChosenError
                        else:
                            pass 
                        time.sleep(2)
                        print("\nPlayer 2's Turn")
                        print("\nThe card picked is: \nBastian \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(B_Attack, B_Wisdom, B_Athleticism, B_Immoral, B_Maniacal))
                        _cont = input("\nPress enter to continue \n")
                        time.sleep(2)
                        if inp == "1":
                            if E_Attack > B_Attack:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R3_1 = R3_1 + 1
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R3_2 = R3_2 + 1
                        if inp == "2":
                            if E_Wisdom > B_Wisdom:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R3_1 = R3_1 + 1
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R3_2 = R3_2 + 1
                        if inp == "3":
                            if E_Athleticism > B_Athleticism:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R3_1 = R3_1 + 1
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R3_2 = R3_2 + 1
                        if inp == "4":
                            if E_Immoral < B_Immoral:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R3_1 = R3_1 + 1
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R3_2 = R3_2 + 1
                        if inp == "5":
                            if E_Maniacal < B_Maniacal:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R3_1 = R3_1 + 1
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R3_2 = R3_2 + 1
                        return
            else:
                #Not using resurrect spell
                pass
            print("\nThe card picked is: \nOrpheus \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
            .format(O_Attack, O_Wisdom, O_Athleticism, O_Immoral, O_Maniacal))
            inp = ""
            inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
            if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                print("You must choose 1 trait")
                sys.exit()
                #raise NoTraitChosenError
            else:
                inpg = ""
                inpg = input("\nDo you want to use the God Spell? (Y/N) \n")
                if inpg == "Y" or inpg == "Yes" or inpg == "y" or inpg == "yes":
                    if checkGS1_3 == 0:
                        checkGS1_3 = checkGS1_3 + 1
                        print("\nThe card picked by Player 2 is: \nBastian \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(B_Attack, B_Wisdom, B_Athleticism, B_Immoral, B_Maniacal))
                        time.sleep(2)
                        print("\nThe strength of each character is changed (random)")
                        time.sleep(2)
                        self.Bastian()
                        time.sleep(2)
                        print("\nPlayer 1 used the god spell")
                        pass
                    else:
                        print("\nGod Spell has already been used by you.\n")
                        pass
                else:
                    pass 
            time.sleep(2)
            print("\nPlayer 2's Turn")
            print("\nThe card picked is: \nBastian \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
            .format(B_Attack, B_Wisdom, B_Athleticism, B_Immoral, B_Maniacal))
            _cont = input("\nPress enter to continue \n")
            time.sleep(2)
            if inp == "1":
                if O_Attack > B_Attack:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R3_1 = R3_1 + 1
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R3_2 = R3_2 + 1
            if inp == "2":
                if O_Wisdom > B_Wisdom:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R3_1 = R3_1 + 1
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R3_2 = R3_2 + 1
            if inp == "3":
                if O_Athleticism > B_Athleticism:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R3_1 = R3_1 + 1
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R3_2 = R3_2 + 1
            if inp == "4":
                if O_Immoral < B_Immoral:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R3_1 = R3_1 + 1
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R3_2 = R3_2 + 1
            if inp == "5":
                if O_Maniacal < B_Maniacal:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R3_1 = R3_1 + 1
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1 
                    R3_2 = R3_2 + 1
        else:    
            #Last round was won by Player 2
            time.sleep(3)
            print("\nPlayer 2's Turn")
            if checkRS2_3 == 0:
                inpr = ""
                inpr = input("\nDo you want to use the Resurrect Spell? (Y/N) ")
                if inpr == "Y" or inpr == "Yes" or inpr == "y" or inpr == "yes":
                    checkRS2_3 = checkRS2_3 + 1
                    time.sleep(2)
                    print("\nUsing Resurrect Spell...")
                    time.sleep(2)
                    print("The Outdated Deck has 2 cards")
                    time.sleep(2)
                    n = random.randint(1,2)
                    if n == 1:
                        #Demetrius
                        print("\nThe card picked is: \nDemetrius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(D_Attack, D_Wisdom, D_Athleticism, D_Immoral, D_Maniacal))
                        inp = ""
                        inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
                        if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                            print("You must choose 1 trait")
                            sys.exit()
                            #raise NoTraitChosenError
                        else:
                            pass 
                        time.sleep(2) 
                        print("\nPlayer 1's Turn")
                        print("\nThe card picked is: \nOrpheus \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(O_Attack, O_Wisdom, O_Athleticism, O_Immoral, O_Maniacal))
                        _cont = input("\nPress enter to continue \n")
                        time.sleep(2)
                        if inp == "1":
                            if D_Attack > O_Attack:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R3_2 = R3_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R3_1 = R3_1 + 1
                        if inp == "2":
                            if D_Wisdom > O_Wisdom:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R3_2 = R3_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R3_1 = R3_1 + 1
                        if inp == "3":
                            if D_Athleticism > O_Athleticism:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R3_2 = R3_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R3_1 = R3_1 + 1
                        if inp == "4":
                            if D_Immoral < O_Immoral:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R3_2 = R3_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R3_1 = R3_1 + 1
                        if inp == "5":
                            if D_Maniacal < O_Maniacal:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R3_2 = R3_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R3_1 = R3_1 + 1
                        return
                    else:
                        #Heraclius
                        print("\nThe card picked is: \nHeraclius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(E_Attack, E_Wisdom, E_Athleticism, E_Immoral, E_Maniacal))
                        inp = ""
                        inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
                        if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                            print("You must choose 1 trait")
                            sys.exit()
                            #raise NoTraitChosenError
                        else:
                            pass 
                        time.sleep(2) 
                        print("\nPlayer 1's Turn")
                        print("\nThe card picked is: \nOrpheus \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(O_Attack, O_Wisdom, O_Athleticism, O_Immoral, O_Maniacal))
                        _cont = input("\nPress enter to continue \n")
                        time.sleep(2)
                        if inp == "1":
                            if H_Attack > O_Attack:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R3_2 = R3_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R3_1 = R3_1 + 1
                        if inp == "2":
                            if H_Wisdom > O_Wisdom:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R3_2 = R3_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R3_1 = R3_1 + 1
                        if inp == "3":
                            if H_Athleticism > O_Athleticism:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R3_2 = R3_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R3_1 = R3_1 + 1
                        if inp == "4":
                            if H_Immoral < O_Immoral:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R3_2 = R3_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R3_1 = R3_1 + 1
                        if inp == "5":
                            if H_Maniacal < O_Maniacal:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R3_2 = R3_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R3_1 = R3_1 + 1
                        return
                else:
                    #Not using resurrect spell
                    pass
            print("\nThe card picked is: \nBastian \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
            .format(B_Attack, B_Wisdom, B_Athleticism, B_Immoral, B_Maniacal))
            inp = ""
            inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
            if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                print("You must choose 1 trait")
                sys.exit()
                #raise NoTraitChosenError
            else:
                inpg = ""
                inpg = input("\nDo you want to use the God Spell? (Y/N) \n")
                if inpg == "Y" or inpg == "Yes" or inpg == "y" or inpg == "yes":
                    if checkGS2_3 == 0:
                        checkGS2_3 = checkGS2_3 + 1
                        print("\nThe card picked by Player 1 is: \nOrpheus \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(O_Attack, O_Wisdom, O_Athleticism, O_Immoral, O_Maniacal))
                        time.sleep(2)
                        print("\nThe strength of each character is changed (random)")
                        time.sleep(2)
                        self.Orpheus()
                        time.sleep(2)
                        print("\nPlayer 2 used the god spell")
                        pass
                    else:
                        print("\nGod Spell has already been used by you.\n")
                        pass
                else:
                    #Not using god spell
                    pass 
            time.sleep(2) 
            print("\nPlayer 1's Turn")
            print("\nThe card picked is: \nOrpheus \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
            .format(O_Attack, O_Wisdom, O_Athleticism, O_Immoral, O_Maniacal))
            _cont = input("\nPress enter to continue \n")
            time.sleep(2)
            if inp == "1":
                if B_Attack > O_Attack:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R3_2 = R3_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R3_1 = R3_1 + 1
            if inp == "2":
                if B_Wisdom > O_Wisdom:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R3_2 = R3_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R3_1 = R3_1 + 1
            if inp == "3":
                if B_Athleticism > O_Athleticism:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R3_2 = R3_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R3_1 = R3_1 + 1
            if inp == "4":
                if B_Immoral < O_Immoral:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R3_2 = R3_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R3_1 = R3_1 + 1
            if inp == "5":
                if B_Maniacal < O_Maniacal:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R3_2 = R3_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R3_1 = R3_1 + 1
    
    def roundFour(self):
        print("\nROUND 4")
        global P1_points, P2_points, R3_1, R3_2, R4_1, R4_2, checkGS1_4, checkGS2_4, checkRS1_4, checkRS2_4
        R4_1 = R4_2 = checkGS1_4 = checkGS2_4 = checkRS1_4 = checkRS2_4 = 0
        checkGS1_4 = checkGS1_3
        checkGS2_4 = checkGS2_3
        checkRS1_4 = checkRS1_3
        checkRS2_4 = checkRS2_3
        if R3_1 > R3_2:
            time.sleep(2)
            print("\nPlayer 1's Turn")
            if checkRS1_4 == 0:
                inpr = ""
                inpr = input("\nDo you want to use the Resurrect Spell? (Y/N) ")
                if inpr == "Y" or inpr == "Yes" or inpr == "y" or inpr == "yes":
                    checkRS1_4 = checkRS1_4 + 1
                    time.sleep(2)
                    print("\nUsing Resurrect Spell...")
                    time.sleep(2)
                    print("The Outdated Deck has 3 cards")
                    time.sleep(2)
                    n = random.randint(1,3)
                    if n == 1:
                        #Arcadius
                        print("\nThe card picked is: \nArcadius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(A_Attack, A_Wisdom, A_Athleticism, A_Immoral, A_Maniacal))
                        inp = ""
                        inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
                        if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                            print("You must choose 1 trait")
                            sys.exit()
                            #raise NoTraitChosenError
                        else:
                            pass 
                        time.sleep(2)
                        print("\nPlayer 2's Turn")
                        print("\nThe card picked is: \nCyril \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(C_Attack, C_Wisdom, C_Athleticism, C_Immoral, C_Maniacal))
                        _cont = input("\nPress enter to continue \n")
                        time.sleep(2)
                        if inp == "1":
                            if A_Attack > C_Attack:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                        if inp == "2":
                            if A_Wisdom > C_Wisdom:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                        if inp == "3":
                            if A_Athleticism > C_Athleticism:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                        if inp == "4":
                            if A_Immoral < C_Immoral:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                        if inp == "5":
                            if A_Maniacal < C_Maniacal:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1 
                                R4_2 = R4_2 + 1
                        return
                    elif n == 2:
                        #Eugenius
                        print("\nThe card picked is: \nEugenius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(E_Attack, E_Wisdom, E_Athleticism, E_Immoral, E_Maniacal))
                        inp = ""
                        inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
                        if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                            print("You must choose 1 trait")
                            sys.exit()
                            #raise NoTraitChosenError
                        else:
                            pass 
                        time.sleep(2)
                        print("\nPlayer 2's Turn")
                        print("\nThe card picked is: \nCyril \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(C_Attack, C_Wisdom, C_Athleticism, C_Immoral, C_Maniacal))
                        _cont = input("\nPress enter to continue \n")
                        time.sleep(2)
                        if inp == "1":
                            if E_Attack > C_Attack:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                        if inp == "2":
                            if E_Wisdom > C_Wisdom:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                        if inp == "3":
                            if E_Athleticism > C_Athleticism:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                        if inp == "4":
                            if E_Immoral < C_Immoral:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                        if inp == "5":
                            if E_Maniacal < C_Maniacal:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1 
                                R4_2 = R4_2 + 1
                        return
                    else:
                        #Orpheus
                        print("\nThe card picked is: \nOrpheus \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(O_Attack, O_Wisdom, O_Athleticism, O_Immoral, O_Maniacal))
                        inp = ""
                        inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
                        if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                            print("You must choose 1 trait")
                            sys.exit()
                            #raise NoTraitChosenError
                        else:
                            pass 
                        time.sleep(2)
                        print("\nPlayer 2's Turn")
                        print("\nThe card picked is: \nCyril \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(C_Attack, C_Wisdom, C_Athleticism, C_Immoral, C_Maniacal))
                        _cont = input("\nPress enter to continue \n")
                        time.sleep(2)
                        if inp == "1":
                            if O_Attack > C_Attack:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                        if inp == "2":
                            if O_Wisdom > C_Wisdom:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                        if inp == "3":
                            if O_Athleticism > C_Athleticism:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                        if inp == "4":
                            if O_Immoral < C_Immoral:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                        if inp == "5":
                            if O_Maniacal < C_Maniacal:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1 
                                R4_2 = R4_2 + 1
                        return
                else:
                    #Not using resurrect spell
                    pass
            print("\nThe card picked is: \nIrenaeus \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
            .format(I_Attack, I_Wisdom, I_Athleticism, I_Immoral, I_Maniacal))
            inp = ""
            inp = input("1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
            if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                print("You must choose 1 trait")
                sys.exit()
                #raise NoTraitChosenError
            else:
                inpg = ""
                inpg = input("\nDo you want to use the God Spell? (Y/N) \n")
                if inpg == "Y" or inpg == "Yes" or inpg == "y" or inpg == "yes":
                    if checkGS1_4 == 0:
                        checkGS1_4 = checkGS1_4 + 1
                        print("\nThe card picked by Player 2 is: \nCyril \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(C_Attack, C_Wisdom, C_Athleticism, C_Immoral, C_Maniacal))
                        time.sleep(2)
                        print("\nThe strength of each character is changed (random)")
                        time.sleep(2)
                        self.Cyril()
                        time.sleep(2)
                        print("\nPlayer 1 used the god spell")
                        pass
                    else:
                        print("\nGod Spell has already been used by you.\n")
                        pass
                else:
                    pass 
            time.sleep(2)
            print("\nPlayer 2's Turn")
            print("\nThe card picked is: \nCyril \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
            .format(C_Attack, C_Wisdom, C_Athleticism, C_Immoral, C_Maniacal))
            _cont = input("\nPress enter to continue \n")
            time.sleep(2)
            if inp == "1":
                if I_Attack > C_Attack:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R4_1 = R4_1 + 2
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R4_2 = R4_2 + 1
            if inp == "2":
                if I_Wisdom > C_Wisdom:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R4_1 = R4_1 + 2
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R4_2 = R4_2 + 1
            if inp == "3":
                if I_Athleticism > C_Athleticism:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R4_1 = R4_1 + 2
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R4_2 = R4_2 + 1
            if inp == "4":
                if I_Immoral < C_Immoral:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R4_1 = R4_1 + 2
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R4_2 = R4_2 + 1
            if inp == "5":
                if I_Maniacal < C_Maniacal:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R4_1 = R4_1 + 2
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1 
                    R4_2 = R4_2 + 1
        else:    
            time.sleep(3)
            print("\nPlayer 2's Turn")
            if checkRS2_4 == 0:
                inpr = ""
                inpr = input("\nDo you want to use the Resurrect Spell? (Y/N) ")
                if inpr == "Y" or inpr == "Yes" or inpr == "y" or inpr == "yes":
                    checkRS2_4 = checkRS2_4 + 1
                    time.sleep(2)
                    print("\nUsing Resurrect Spell...")
                    time.sleep(2)
                    print("The Outdated Deck has 3 cards")
                    time.sleep(2)
                    n = random.randint(1,3)
                    if n == 1:
                        #Demetrius
                        print("\nThe card picked is: \nDemetrius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(D_Attack, D_Wisdom, D_Athleticism, D_Immoral, D_Maniacal))
                        inp = ""
                        inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
                        if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                            print("You must choose 1 trait")
                            sys.exit()
                            #raise NoTraitChosenError
                        else:
                            pass 
                        time.sleep(2)
                        print("\nPlayer 1's Turn")
                        print("\nThe card picked is: \nIrenaeus \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(I_Attack, I_Wisdom, I_Athleticism, I_Immoral, I_Maniacal))
                        _cont = input("\nPress enter to continue \n")
                        time.sleep(2)
                        if inp == "1":
                            if D_Attack > I_Attack:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                        if inp == "2":
                            if D_Wisdom > I_Wisdom:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                        if inp == "3":
                            if D_Athleticism > I_Athleticism:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                        if inp == "4":
                            if D_Immoral < I_Immoral:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                        if inp == "5":
                            if D_Maniacal < I_Maniacal:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                        return
                    elif n == 2:
                        #Heraclius
                        print("\nThe card picked is: \nHeraclius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(H_Attack, H_Wisdom, H_Athleticism, H_Immoral, H_Maniacal))
                        inp = ""
                        inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
                        if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                            print("You must choose 1 trait")
                            sys.exit()
                            #raise NoTraitChosenError
                        else:
                            pass 
                        time.sleep(2)
                        print("\nPlayer 1's Turn")
                        print("\nThe card picked is: \nZeuxis \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(Z_Attack, Z_Wisdom, Z_Athleticism, Z_Immoral, Z_Maniacal))
                        _cont = input("\nPress enter to continue \n")
                        time.sleep(2)
                        if inp == "1":
                            if H_Attack > Z_Attack:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                        if inp == "2":
                            if H_Wisdom > Z_Wisdom:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                        if inp == "3":
                            if H_Athleticism > Z_Athleticism:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                        if inp == "4":
                            if H_Immoral < Z_Immoral:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                        if inp == "5":
                            if H_Maniacal < Z_Maniacal:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                        return
                    else:
                        #Bastian
                        print("\nThe card picked is: \nBastian \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(B_Attack, B_Wisdom, B_Athleticism, B_Immoral, B_Maniacal))
                        inp = ""
                        inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
                        if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                            print("You must choose 1 trait")
                            sys.exit()
                            #raise NoTraitChosenError
                        else:
                            pass 
                        time.sleep(2)
                        print("\nPlayer 1's Turn")
                        print("\nThe card picked is: \nIrenaeus \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(I_Attack, I_Wisdom, I_Athleticism, I_Immoral, I_Maniacal))
                        _cont = input("\nPress enter to continue \n")
                        time.sleep(2)
                        if inp == "1":
                            if B_Attack > I_Attack:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                        if inp == "2":
                            if B_Wisdom > I_Wisdom:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                        if inp == "3":
                            if B_Athleticism > I_Athleticism:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                        if inp == "4":
                            if B_Immoral < I_Immoral:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                        if inp == "5":
                            if B_Maniacal < I_Maniacal:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R4_2 = R4_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R4_1 = R4_1 + 2
                        return
                else:
                    #Not using resurrect spell
                    pass
            print("\nThe card picked is: \nCyril \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
            .format(C_Attack, C_Wisdom, C_Athleticism, C_Immoral, C_Maniacal))
            inp = ""
            inp = input("1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
            if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                print("You must choose 1 trait")
                sys.exit()
                #raise NoTraitChosenError
            else:
                inpg = ""
                inpg = input("\nDo you want to use the God Spell? (Y/N) \n")
                if inpg == "Y" or inpg == "Yes" or inpg == "y" or inpg == "yes":
                    if checkGS2_4 == 0:
                        checkGS2_4 = checkGS2_4 + 1
                        print("\nThe card picked by Player 1 is: \nIrenaeus \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(I_Attack, I_Wisdom, I_Athleticism, I_Immoral, I_Maniacal))
                        time.sleep(2)
                        print("\nThe strength of each character is changed (random)")
                        time.sleep(2)
                        self.Irenaeus()
                        time.sleep(2)
                        print("\nPlayer 2 used the god spell")
                        pass
                    else:
                        print("\nGod Spell has already been used by you.\n")
                        pass
                else:
                    pass 
            time.sleep(2) 
            print("\nPlayer 1's Turn")
            print("\nThe card picked is: \nIrenaeus \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
            .format(I_Attack, I_Wisdom, I_Athleticism, I_Immoral, I_Maniacal))
            _cont = input("\nPress enter to continue \n")
            time.sleep(2)
            if inp == "1":
                if C_Attack > I_Attack:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R4_2 = R4_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R4_1 = R4_1 + 2
            if inp == "2":
                if C_Wisdom > I_Wisdom:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R4_2 = R4_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R4_1 = R4_1 + 2
            if inp == "3":
                if C_Athleticism > I_Athleticism:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R4_2 = R4_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R4_1 = R4_1 + 2
            if inp == "4":
                if C_Immoral > I_Immoral:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R4_2 = R4_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R4_1 = R4_1 + 2
            if inp == "5":
                if C_Maniacal > I_Maniacal:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R4_2 = R4_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R4_1 = R4_1 + 2

    def roundFive(self):
        print("\nROUND 5")
        global P1_points, P2_points, R4_1, R4_2, R5_1, R5_2, checkGS1_5, checkGS2_5, checkRS1_5, checkRS2_5, checkRS1_4
        R5_1 = R5_2 = checkGS1_5 = checkGS2_5 = checkRS1_5 = checkRS2_5 = 0
        checkGS1_5 = checkGS1_4
        checkGS2_5 = checkGS2_4
        checkRS1_5 = checkRS1_4
        checkRS2_5 = checkRS2_4
        if R4_1 > R4_2:
            time.sleep(2)
            print("\nPlayer 1's Turn")
            if checkRS1_4 == 0:
                inpr = ""
                inpr = input("\nDo you want to use the Resurrect Spell? (Y/N) ")
                if inpr == "Y" or inpr == "Yes" or inpr == "y" or inpr == "yes":
                    checkRS1_4 = checkRS1_4 + 1
                    time.sleep(2)
                    print("\nUsing Resurrect Spell...")
                    time.sleep(2)
                    print("The Outdated Deck has 4 cards")
                    time.sleep(2)
                    n = random.randint(1,4)
                    if n == 1:
                        #Arcadius
                        print("\nThe card picked is: \nArcadius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(A_Attack, A_Wisdom, A_Athleticism, A_Immoral, A_Maniacal))
                        inp = ""
                        inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
                        if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                            print("You must choose 1 trait")
                            sys.exit()
                            #raise NoTraitChosenError
                        else:
                            pass 
                        time.sleep(2)
                        print("\nPlayer 2's Turn")
                        print("\nThe card picked is: \nPericles \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(P_Attack, P_Wisdom, P_Athleticism, P_Immoral, P_Maniacal))
                        _cont = input("\nPress enter to continue \n")
                        time.sleep(2)
                        if inp == "1":
                            if A_Attack > P_Attack:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                        if inp == "2":
                            if A_Wisdom > P_Wisdom:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                        if inp == "3":
                            if A_Athleticism > P_Athleticism:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                        if inp == "4":
                            if A_Immoral < P_Immoral:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                        if inp == "5":
                            if A_Maniacal < P_Maniacal:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1 
                                R5_2 = R5_2 + 1
                        return
                    elif n == 2:
                        #Eugenius
                        print("\nThe card picked is: \nEugenius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(E_Attack, E_Wisdom, E_Athleticism, E_Immoral, E_Maniacal))
                        inp = ""
                        inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
                        if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                            print("You must choose 1 trait")
                            sys.exit()
                            #raise NoTraitChosenError
                        else:
                            pass 
                        time.sleep(2)
                        print("\nPlayer 2's Turn")
                        print("\nThe card picked is: \nPericles \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(P_Attack, P_Wisdom, P_Athleticism, P_Immoral, P_Maniacal))
                        _cont = input("\nPress enter to continue \n")
                        time.sleep(2)
                        if inp == "1":
                            if E_Attack > P_Attack:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                        if inp == "2":
                            if E_Wisdom > P_Wisdom:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                        if inp == "3":
                            if E_Athleticism > P_Athleticism:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                        if inp == "4":
                            if E_Immoral < P_Immoral:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                        if inp == "5":
                            if E_Maniacal < P_Maniacal:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1 
                                R5_2 = R5_2 + 1
                        return
                    elif n == 3:
                        #Orpheus
                        print("\nThe card picked is: \nOrpheus \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(O_Attack, O_Wisdom, O_Athleticism, O_Immoral, O_Maniacal))
                        inp = ""
                        inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
                        if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                            print("You must choose 1 trait")
                            sys.exit()
                            #raise NoTraitChosenError
                        else:
                            pass 
                        time.sleep(2)
                        print("\nPlayer 2's Turn")
                        print("\nThe card picked is: \nPericles \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(P_Attack, P_Wisdom, P_Athleticism, P_Immoral, P_Maniacal))
                        _cont = input("\nPress enter to continue \n")
                        time.sleep(2)
                        if inp == "1":
                            if O_Attack > P_Attack:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                        if inp == "2":
                            if O_Wisdom > P_Wisdom:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                        if inp == "3":
                            if O_Athleticism > P_Athleticism:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                        if inp == "4":
                            if O_Immoral < P_Immoral:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                        if inp == "5":
                            if O_Maniacal < P_Maniacal:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1 
                                R5_2 = R5_2 + 1
                        return
                    else:
                        #Zeuxis
                        print("\nThe card picked is: \nZeuxis \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(Z_Attack, Z_Wisdom, Z_Athleticism, Z_Immoral, Z_Maniacal))
                        inp = ""
                        inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
                        if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                            print("You must choose 1 trait")
                            sys.exit()
                            #raise NoTraitChosenError
                        else:
                            pass 
                        time.sleep(2)
                        print("\nPlayer 2's Turn")
                        print("\nThe card picked is: \nPericles \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(P_Attack, P_Wisdom, P_Athleticism, P_Immoral, P_Maniacal))
                        _cont = input("\nPress enter to continue \n")
                        time.sleep(2)
                        if inp == "1":
                            if Z_Attack > P_Attack:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                        if inp == "2":
                            if Z_Wisdom > P_Wisdom:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                        if inp == "3":
                            if Z_Athleticism > P_Athleticism:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                        if inp == "4":
                            if Z_Immoral < P_Immoral:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                        if inp == "5":
                            if Z_Maniacal < P_Maniacal:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                            else:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1 
                                R5_2 = R5_2 + 1
                        return
            print("\nThe card picked is: \nZeuxis \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
            .format(Z_Attack, Z_Wisdom, Z_Athleticism, Z_Immoral, Z_Maniacal))
            inp = ""
            inp = input("1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
            if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                print("You must choose 1 trait")
                sys.exit()
                #raise NoTraitChosenError
            else:
                inpg = ""
                inpg = input("\nDo you want to use the God Spell? (Y/N) \n")
                if inpg == "Y" or inpg == "Yes" or inpg == "y" or inpg == "yes":
                    if checkGS1_5 == 0:
                        checkGS1_5 = checkGS1_5 + 1
                        print("\nThe card picked by Player 2 is: \nPericles \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(P_Attack, P_Wisdom, P_Athleticism, P_Immoral, P_Maniacal))
                        time.sleep(2)
                        print("\nThe strength of each character is changed (random)")
                        time.sleep(2)
                        self.Pericles()
                        time.sleep(2)
                        print("\nPlayer 1 used the god spell")
                        pass
                    else:
                        print("\nGod Spell has already been used by you.\n")
                        pass
                else:
                    pass 
            time.sleep(2)
            print("\nPlayer 2's Turn")
            print("\nThe card picked is: \nPericles \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
            .format(P_Attack, P_Wisdom, P_Athleticism, P_Immoral, P_Maniacal))
            _cont = input("\nPress enter to continue \n")
            time.sleep(2)
            if inp == "1":
                if Z_Attack > P_Attack:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R5_1 = R5_1 + 2
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R5_2 = R5_2 + 1
            if inp == "2":
                if Z_Wisdom > P_Wisdom:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R5_1 = R5_1 + 2
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R5_2 = R5_2 + 1
            if inp == "3":
                if Z_Athleticism > P_Athleticism:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R5_1 = R5_1 + 2
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R5_2 = R5_2 + 1
            if inp == "4":
                if Z_Immoral < P_Immoral:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R5_1 = R5_1 + 2
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R5_2 = R5_2 + 1
            if inp == "5":
                if Z_Maniacal < P_Maniacal:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R5_1 = R5_1 + 2
                else:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1 
                    R5_2 = R5_2 + 1
        else:    
            time.sleep(3)
            print("\nPlayer 2's Turn")
            if checkRS2_5 == 0:
                inpr = ""
                inpr = input("\nDo you want to use the Resurrect Spell? (Y/N) ")
                if inpr == "Y" or inpr == "Yes" or inpr == "y" or inpr == "yes":
                    checkRS2_5 = checkRS2_5 + 1
                    time.sleep(2)
                    print("\nUsing Resurrect Spell...")
                    time.sleep(2)
                    print("The Outdated Deck has 4 cards")
                    time.sleep(2)
                    n = random.randint(1,4)
                    if n == 1:
                        #Demetrius
                        print("\nThe card picked is: \nDemetrius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(D_Attack, D_Wisdom, D_Athleticism, D_Immoral, D_Maniacal))
                        inp = ""
                        inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
                        if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                            print("You must choose 1 trait")
                            sys.exit()
                            #raise NoTraitChosenError
                        else:
                            pass 
                        time.sleep(2)
                        print("\nPlayer 1's Turn")
                        print("\nThe card picked is: \nZeuxis \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(Z_Attack, Z_Wisdom, Z_Athleticism, Z_Immoral, Z_Maniacal))
                        _cont = input("\nPress enter to continue \n")
                        time.sleep(2)
                        if inp == "1":
                            if D_Attack > Z_Attack:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                        if inp == "2":
                            if D_Wisdom > Z_Wisdom:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                        if inp == "3":
                            if D_Athleticism > Z_Athleticism:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                        if inp == "4":
                            if D_Immoral < Z_Immoral:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                        if inp == "5":
                            if D_Maniacal < Z_Maniacal:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                        return
                    elif n == 2:
                        #Heraclius
                        print("\nThe card picked is: \nHeraclius \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(E_Attack, E_Wisdom, E_Athleticism, E_Immoral, E_Maniacal))
                        inp = ""
                        inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
                        if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                            print("You must choose 1 trait")
                            sys.exit()
                            #raise NoTraitChosenError
                        else:
                            pass 
                        time.sleep(2)
                        print("\nPlayer 1's Turn")
                        print("\nThe card picked is: \nZeuxis \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(Z_Attack, Z_Wisdom, Z_Athleticism, Z_Immoral, Z_Maniacal))
                        _cont = input("\nPress enter to continue \n")
                        time.sleep(2)
                        if inp == "1":
                            if H_Attack > Z_Attack:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                        if inp == "2":
                            if H_Wisdom > Z_Wisdom:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                        if inp == "3":
                            if H_Athleticism > Z_Athleticism:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                        if inp == "4":
                            if H_Immoral < Z_Immoral:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                        if inp == "5":
                            if H_Maniacal < Z_Maniacal:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                        return
                    elif n == 3:
                        #Bastian
                        print("\nThe card picked is: \nBastian \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(B_Attack, B_Wisdom, B_Athleticism, B_Immoral, B_Maniacal))
                        inp = ""
                        inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
                        if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                            print("You must choose 1 trait")
                            sys.exit()
                            #raise NoTraitChosenError
                        else:
                            pass 
                        time.sleep(2)
                        print("\nPlayer 1's Turn")
                        print("\nThe card picked is: \nZeuxis \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(Z_Attack, Z_Wisdom, Z_Athleticism, Z_Immoral, Z_Maniacal))
                        _cont = input("\nPress enter to continue \n")
                        time.sleep(2)
                        if inp == "1":
                            if B_Attack > Z_Attack:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                        if inp == "2":
                            if B_Wisdom > Z_Wisdom:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                        if inp == "3":
                            if B_Athleticism > Z_Athleticism:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                        if inp == "4":
                            if B_Immoral < Z_Immoral:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                        if inp == "5":
                            if B_Maniacal < Z_Maniacal:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                        return
                    else:
                        #Pericles
                        print("\nThe card picked is: \nPericles \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(P_Attack, P_Wisdom, P_Athleticism, P_Immoral, P_Maniacal))
                        inp = ""
                        inp = input("\n1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
                        if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                            print("You must choose 1 trait")
                            sys.exit()
                            #raise NoTraitChosenError
                        else:
                            pass 
                        time.sleep(2)
                        print("\nPlayer 1's Turn")
                        print("\nThe card picked is: \nZeuxis \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(Z_Attack, Z_Wisdom, Z_Athleticism, Z_Immoral, Z_Maniacal))
                        _cont = input("\nPress enter to continue \n")
                        time.sleep(2)
                        if inp == "1":
                            if P_Attack > Z_Attack:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                        if inp == "2":
                            if P_Wisdom > Z_Wisdom:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                        if inp == "3":
                            if P_Athleticism > Z_Athleticism:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                        if inp == "4":
                            if P_Immoral < Z_Immoral:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                        if inp == "5":
                            if P_Maniacal < Z_Maniacal:
                                print ("Player 2 wins this round")
                                P2_points = P2_points + 1
                                R5_2 = R5_2 + 1
                            else:
                                print ("Player 1 wins this round")
                                P1_points = P1_points + 1
                                R5_1 = R5_1 + 2
                        return
                else:
                    #Not using resurrect spell
                    pass
            print("\nThe card picked is: \nPericles \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
            .format(P_Attack, P_Wisdom, P_Athleticism, P_Immoral, P_Maniacal))
            inp = ""
            inp = input("1. Attack\n2. Wisdom\n3. Athleticism\n4. Immoral\n5. Manical\nChoose a trait you want to fight with: ")
            if inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5":
                print("You must choose 1 trait")
                sys.exit()
                #raise NoTraitChosenError
            else:
                inpg = ""
                inpg = input("\nDo you want to use the God Spell? (Y/N) \n")
                if inpg == "Y" or inpg == "Yes" or inpg == "y" or inpg == "yes":
                    if checkGS2_5 == 0:
                        checkGS2_5 = checkGS2_5 + 1
                        print("\nThe card picked by Player 1 is: \nZeuxis \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
                        .format(Z_Attack, Z_Wisdom, Z_Athleticism, Z_Immoral, Z_Maniacal))
                        time.sleep(2)
                        print("\nThe strength of each character is changed (random)")
                        time.sleep(2)
                        self.Zeuxis()
                        time.sleep(2)
                        print("\nPlayer 2 used the god spell")
                        pass
                    else:
                        print("\nGod Spell has already been used by you.\n")
                        pass
                else:
                    pass 
            time.sleep(2) 
            print("\nPlayer 1's Turn")
            print("\nThe card picked is: \nZeuxis \nCharacteristics: Attack = {0}, Wisdom = {1}, Athleticism = {2}, Immoral = {3}, Maniacal = {4}"
            .format(Z_Attack, Z_Wisdom, Z_Athleticism, Z_Immoral, Z_Maniacal))
            _cont = input("\nPress enter to continue \n")
            time.sleep(2)
            if inp == "1":
                if P_Attack > Z_Attack:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R5_2 = R5_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R5_1 = R5_1 + 2
            if inp == "2":
                if P_Wisdom > Z_Wisdom:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R5_2 = R5_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R5_1 = R5_1 + 2
            if inp == "3":
                if P_Athleticism > Z_Athleticism:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R5_2 = R5_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R5_1 = R5_1 + 2
            if inp == "4":
                if P_Immoral < Z_Immoral:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R5_2 = R5_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R5_1 = R5_1 + 2
            if inp == "5":
                if P_Maniacal < Z_Maniacal:
                    print ("Player 2 wins this round")
                    P2_points = P2_points + 1
                    R5_2 = R5_2 + 1
                else:
                    print ("Player 1 wins this round")
                    P1_points = P1_points + 1
                    R5_1 = R5_1 + 2

""" class NoTraitChosenError(Exception):
    sys.exit()
    pass """

if __name__ == "__main__":
    def rulesOfGame():
        ii = ""
        ii = input("Do you want to view the rules of the game? (Y/N) ")
        if ii == "Y" or ii == "Yes" or ii == "y" or ii == "yes":
            print("Rules of the game\n0. This game is played between 2 players. There are 10 cards (10 characters) in total. The cards are divided equally among the players.\n1. Each player is given equal number of cards. The strength of each trait / characteristic of a card/character is random in every game. \n2. The one with higher dice roll starts the game and rounds after that are started with the winner of the previous round.\n3. The first player chooses a characteristic to fight with.\n4. The characteristics are in range of 1 to 50 with no character having a perfect strength (i.e. 50 or 0).\n5. Two of the traits/characteristics (Immoral, Maniacal) are different than the others. The one with less strength wins.\n6. If there is a draw in the strength of characteristics/traits, preference goes to the second player, the first player loses that round (i.e. the one who choses which characteristic to fight with. The player winning the round gets one point.\n7. In the end, the player with the most points, wins the game.\n")
        else:
            pass

    def diceRoll():
        global fc1, fc2
        _dice1 = input("Player 1: Press enter to roll dice ")
        fc1 = random.randint(1,6)
        print("Dice thrown by Player 1 shows: ",fc1)
        _dice2 = input("\nPlayer 2: Press enter to roll dice ")
        fc2 = random.randint(1,6)
        print("Dice thrown by Player 2 shows: {0}\n".format(fc2))
        time.sleep(2)

        firstChance()

    def firstChance():
        if fc1 > fc2:
            print("\nDealing cards...\n")
            time.sleep(2)
            print("5 cards are distributed among the two players")
            print("\nPlayer 1 goes first")
            Player1 = MyCardGame()
            Player2 = MyCardGame()
            Player1.Arcadius()
            Player1.Eugenius()
            Player1.Orpheus()
            Player1.Irenaeus()
            Player1.Zeuxis()
            Player2.Demetrius()
            Player2.Heraclius()
            Player2.Bastian()
            Player2.Cyril()
            Player2.Pericles()
        elif fc1 == fc2:
            diceRoll()
        else:
            print("\nDealing cards...\n")
            time.sleep(2)
            print("5 cards are distributed among the two players")
            print("\nPlayer 2 goes first")
            Player1 = MyCardGame()
            Player2 = MyCardGame()
            Player1.Arcadius()
            Player1.Eugenius()
            Player1.Orpheus()
            Player1.Irenaeus()
            Player1.Zeuxis()
            Player2.Demetrius()
            Player2.Heraclius()
            Player2.Bastian()
            Player2.Cyril()
            Player2.Pericles()

    rulesOfGame()
    print("\nCreating 2 Players...\n")
    time.sleep(2)    
    diceRoll()
    
    global checkGS1_1, checkGS1_2, checkGS1_3, checkGS1_4, checkGS1_5, checkGS2_1, checkGS2_2, checkGS2_3, checkGS2_4, checkGS2_5
    global checkRS1_2, checkRS1_3, checkRS1_4, checkRS1_5, checkRS2_2, checkRS2_3, checkRS2_4, checkRS2_5
    GameOn = MyCardGame()
    GameOn.roundOne()
    time.sleep(2)
    GameOn.roundTwo()
    time.sleep(2)
    GameOn.roundThree()
    time.sleep(2)
    GameOn.roundFour()
    time.sleep(2)
    GameOn.roundFive()
    time.sleep(2)

    def finalResult():
        print("\nCalculating Final Results...")
        time.sleep(2)
        print("\nPlayer 1's points = ", P1_points)
        print("Player 2's points = ", P2_points)
        if P1_points > P2_points:
            time.sleep(2)
            print ("\nPLAYER 1 WINS THE GAME")
        else:
            time.sleep(2)
            print("\nPLAYER 2 WINS THE GAME")
    finalResult()
