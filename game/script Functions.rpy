default HolderCount = 1
init python:
    
#            call Statup("Rogue", "Lust", 50, 3)
#            call Statup("Rogue", "Love", 50, 3)
#            call Statup("Rogue", "Love", 80, 4)
#            call Statup("Rogue", "Obed", 30, 1)
#            call Statup("Rogue", "Obed", 50, 1)
#            call Statup("Rogue", "Inbt", 50, 1)
#            call Statup("Rogue", "Inbt", 50, 1)
    
# This updates a stat based on the call "$ statname = Statupdate("Rogue", statname, checked percent, amount changed, 1 if >)"  eg: call Statup("Rogue", "Obed", 70, 12)
    
    
    def Statupdate(Name, Flavor, Type, Check=100, Value=1, Greater=0):
        
        if Flavor == "Love" or Flavor == "Obed" or Flavor == "Inbt":
                Check = Check * 10                  #bumps this stat into the 1000s
        
        if Greater:                             #this checks if it's greater or less than the intended value
                if Type >= Check:
                    Type += Value                   #If it passes the check, add Value to it 
                else:
                    Value = 0                       #If not, don't add Value and set Value to 0
        else:
                if Type <= Check:
                    Type += Value  
                else:
                    Value = 0
                
        if Value:                                       #If there is any change to the stat
                        
            if Type > 1000:                              #If the value would overflow the stat, on Rogue
                if Name == "Rogue" and R_Chat[4]:
                        global R_Love
                        global R_Obed                    
                        global R_Inbt
                        
                        Value = Type - 1000
                        if Flavor == "Love":                    
                                if R_Chat[4] == 1:
                                    R_Obed += Value    #[Love to Obedience]
                                    Flavor = "Obed"
                                elif R_Chat[4] == 2:
                                    R_Inbt += Value   #[Love to Inhibition] 
                                    Flavor = "Inbt"
                        elif Flavor == "Obed":             
                                if R_Chat[4] == 3:
                                    R_Inbt += Value    #[Obedience to Inhibition]
                                    Flavor = "Inbt"
                                elif R_Chat[4] == 4:
                                    R_Love += Value    #[Obedience to Love] 
                                    Flavor = "Love"  
                        elif Flavor == "Inbt":            
                                if R_Chat[4] == 5:
                                    R_Obed += Value    #[Inhibition to Obedience]
                                    Flavor = "Obed"
                                elif R_Chat[4] == 6:
                                    R_Love += Value    #[Inhibition to Love]
                                    Flavor = "Love"
                        R_Love = 1000 if R_Love > 1000 else R_Love  #fix, check this works, not sure.
                        R_Obed = 1000 if R_Obed > 1000 else R_Obed
                        R_Inbt = 1000 if R_Inbt > 1000 else R_Inbt
                #End Rogue content
                        
                elif Name == "Kitty" and K_Chat[4]:
                        global K_Love
                        global K_Obed                    
                        global K_Inbt
                        
                        Value = Type - 1000
                        if Flavor == "Love":                    
                                if K_Chat[4] == 1:
                                    K_Obed += Value    #[Love to Obedience]
                                    Flavor = "Obed"
                                elif K_Chat[4] == 2:
                                    K_Inbt += Value   #[Love to Inhibition] 
                                    Flavor = "Inbt"
                        elif Flavor == "Obed":             
                                if K_Chat[4] == 3:
                                    K_Inbt += Value    #[Obedience to Inhibition]
                                    Flavor = "Inbt"
                                elif K_Chat[4] == 4:
                                    K_Love += Value    #[Obedience to Love] 
                                    Flavor = "Love"  
                        elif Flavor == "Inbt":            
                                if K_Chat[4] == 5:
                                    K_Obed += Value    #[Inhibition to Obedience]
                                    Flavor = "Obed"
                                elif K_Chat[4] == 6:
                                    K_Love += Value    #[Inhibition to Love]
                                    Flavor = "Love"
                        K_Love = 1000 if K_Love > 1000 else K_Love  #fix, check this works, not sure.
                        K_Obed = 1000 if K_Obed > 1000 else K_Obed
                        K_Inbt = 1000 if K_Inbt > 1000 else K_Inbt
                #End Kitty content
                
                elif Name == "Emma" and E_Chat[4]:
                        global E_Love
                        global E_Obed                    
                        global E_Inbt
                        
                        Value = Type - 1000
                        if Flavor == "Love":                    
                                if E_Chat[4] == 1:
                                    E_Obed += Value    #[Love to Obedience]
                                    Flavor = "Obed"
                                elif E_Chat[4] == 2:
                                    E_Inbt += Value   #[Love to Inhibition] 
                                    Flavor = "Inbt"
                        elif Flavor == "Obed":             
                                if E_Chat[4] == 3:
                                    E_Inbt += Value    #[Obedience to Inhibition]
                                    Flavor = "Inbt"
                                elif E_Chat[4] == 4:
                                    E_Love += Value    #[Obedience to Love] 
                                    Flavor = "Love"  
                        elif Flavor == "Inbt":            
                                if E_Chat[4] == 5:
                                    E_Obed += Value    #[Inhibition to Obedience]
                                    Flavor = "Obed"
                                elif E_Chat[4] == 6:
                                    E_Love += Value    #[Inhibition to Love]
                                    Flavor = "Love"
                        E_Love = 1000 if E_Love > 1000 else E_Love  #fix, check this works, not sure.
                        E_Obed = 1000 if E_Obed > 1000 else E_Obed
                        E_Inbt = 1000 if E_Inbt > 1000 else E_Inbt
                #End Emma content
                
                elif Name == "Laura" and L_Chat[4]:
                        global L_Love
                        global L_Obed                    
                        global L_Inbt
                        
                        Value = Type - 1000
                        if Flavor == "Love":                    
                                if L_Chat[4] == 1:
                                    L_Obed += Value    #[Love to Obedience]
                                    Flavor = "Obed"
                                elif L_Chat[4] == 2:
                                    L_Inbt += Value   #[Love to Inhibition] 
                                    Flavor = "Inbt"
                        elif Flavor == "Obed":             
                                if L_Chat[4] == 3:
                                    L_Inbt += Value    #[Obedience to Inhibition]
                                    Flavor = "Inbt"
                                elif L_Chat[4] == 4:
                                    L_Love += Value    #[Obedience to Love] 
                                    Flavor = "Love"  
                        elif Flavor == "Inbt":            
                                if L_Chat[4] == 5:
                                    L_Obed += Value    #[Inhibition to Obedience]
                                    Flavor = "Obed"
                                elif L_Chat[4] == 6:
                                    L_Love += Value    #[Inhibition to Love]
                                    Flavor = "Love"
                        L_Love = 1000 if L_Love > 1000 else L_Love  #fix, check this works, not sure.
                        L_Obed = 1000 if L_Obed > 1000 else L_Obed
                        L_Inbt = 1000 if L_Inbt > 1000 else L_Inbt
                #End Laura content
                
                Type = 1000
                
                
            #I need to change this bit with the following line: 
#            if Flavor == "Lust" and Value >= 100 and not Trigger:
#                if Name == "Rogue":        #calls orgasm if Lust goes over 100, breaks routine
#                    renpy.call("R_Cumming")
#                elif Name == "Kitty":        #calls orgasm if Lust goes over 100, breaks routine
#                    renpy.call("K_Cumming")
#                elif Name == "Emma":        #calls orgasm if Lust goes over 100, breaks routine
#                    renpy.call("E_Cumming")
                    
            
            if Flavor == "Love":                        #Sets reporting text color based on Flavor
                    Color = "#c11b17"
            elif Flavor == "Obed":
                    Color = "#2554c7"
            elif Flavor == "Inbt":
                    Color = "#FFF380"
            elif Flavor == "Lust":
                    Color = "#FAAFBE"
            else:
                    Color = "#FFFFFF"
            
            if Name == "Rogue":
                    XPOS = R_SpriteLoc
            elif Name == "Kitty":
                    XPOS = K_SpriteLoc
            elif Name == "Emma":
                    XPOS = E_SpriteLoc
            elif Name == "Laura":
                    XPOS = L_SpriteLoc
            else:
                    XPOS = 0.75
                
            CallHolder(Value, Color, XPOS)
                            
        if Type < 0:                                    #If Type ends up less than zero, set it to zero
            Type = 0
            
        return Type
  
    def CallHolder(Value, Color, XPOS):        
            global HolderCount
            
            if HolderCount == 1:                        #Shows the "+3" style feedback screen
                    renpy.show_screen("StatHolder1", Value, Color, XPOS)
            elif HolderCount == 2:
                    renpy.show_screen("StatHolder2", Value, Color, XPOS)
            elif HolderCount == 3:
                    renpy.show_screen("StatHolder3", Value, Color, XPOS)
            elif HolderCount == 4:
                    renpy.show_screen("StatHolder4", Value, Color, XPOS)        
            elif HolderCount == 5:
                    renpy.show_screen("StatHolder5", Value, Color, XPOS)
            else:           #== 6:
                    renpy.show_screen("StatHolder6", Value, Color, XPOS)
                
            HolderCount += 1 if HolderCount <= 6 else -5                             #Resets holder screens when it maxes out.
            
            return

    
transform StatAnimation(Timer, XPOS):                         #this is the animation for the Stat ticker
    alpha 0
    pause Timer
#    xpos 0.75 ypos 0.15 alpha 1 #original version that works
    xpos XPOS ypos 0.15 alpha 1
#    linear 1 ypos 0.0 alpha 0
    parallel:
        linear 1 ypos 0.0
    parallel:
        pause .5
        linear .5 alpha 0
    
screen StatGraphic(Value, Color, Timer, XPOS):                #this displays the stat ticker when called
        showif Value > 0:
            text "+[Value]" size 30 color Color at StatAnimation(Timer, XPOS)
        else:
            text "[Value]" size 30 color Color at StatAnimation(Timer, XPOS)    
        
screen StatHolder1(Value, Color, XPOS):                       #This cycles through the possible stat ticker frameworks
        use StatGraphic(Value, Color, 0.0, XPOS)
        timer 1.0 action Hide("StatHolder1") 
screen StatHolder2(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.2, XPOS)
        timer 1.2 action Hide("StatHolder2") 
screen StatHolder3(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.4, XPOS)
        timer 1.4 action Hide("StatHolder3") 
screen StatHolder4(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.6, XPOS)
        timer 1.6 action Hide("StatHolder4")    
screen StatHolder5(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.8, XPOS)
        timer 1.8 action Hide("StatHolder5") 
screen StatHolder6(Value, Color, XPOS):
        use StatGraphic(Value, Color, 1.0, XPOS)
        timer 2.0 action Hide("StatHolder6") 
    
# End Stat update function. . .

init python:
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#this function checks how many of "item" are in the player's inventory

    def Inventory_Check(Item = "item", Count = 0):      #remove, unneeded
            if Item in P_Inventory:
                Count = P_Inventory.count(Item) 
            else:
                Count = 0
            return Count
       
#This function checks how many times you've accessed a given action within the timeframe specified. Example: $ Count = Action_Check("Rogue", "recent", "sex")   
    def Action_Check(Chr = "Rogue", Time = "recent", Act = "act", Count = 0): 
            if Chr == "Rogue":
                        if Time == "recent" and Act in R_RecentActions:
                            Count = R_RecentActions.count(Act) 
                        elif Act in R_DailyActions:
                            Count = R_DailyActions.count(Act) 
            elif Chr == "Kitty":
                        if Time == "recent" and Act in K_RecentActions:
                            Count = K_RecentActions.count(Act) 
                        elif Act in K_DailyActions:
                            Count = K_DailyActions.count(Act) 
            elif Chr == "Emma":
                        if Time == "recent" and Act in E_RecentActions:
                            Count = E_RecentActions.count(Act) 
                        elif Act in E_DailyActions:
                            Count = E_DailyActions.count(Act) 
            elif Chr == "Laura":
                        if Time == "recent" and Act in L_RecentActions:
                            Count = L_RecentActions.count(Act) 
                        elif Act in L_DailyActions:
                            Count = L_DailyActions.count(Act) 
                    
            return Count


    
                        
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def Personality(Chr = "Rogue", Type = "high", Love = 0): #Determines character personality choices. ie Personality("Rogue", "high", 0)
        if Chr == "Rogue":                              #sets the data based on Rogue's data            
                L = R_Love
                O = R_Obed
                I = R_Inbt
                if R_Chat[4]:
                    if R_Chat[4] == 1 or R_Chat[4] == 5:
                        return "Obed"  
                    elif R_Chat[4] == 2 or R_Chat[4] == 3:
                        return "Inbt" 
                    elif R_Chat[4] == 4 or R_Chat[4] == 6:
                        return "Love" 
        
        L = L - Love                            #can subtract a value to balance out love advantage
        
        if Type == "high":                      #Picks out highest stat of three
                if L >= O and L >= I:
                    return "Love"  
                elif O >= L and O >= I:
                    return "Obed"   
                else:
                    return "Inbt"
                
        if Type == "LO":                        #picks out highest of two values
                if L >= O:
                    return "Love"           
                else:
                    return "Obed" 
        if Type == "OI":
                if O >= I:
                    return "Obed"           
                else:
                    return "Inbt"
        if Type == "LI":
                if L >= I:
                    return "Love"           
                else:
                    return "Inbt"
            
        if Type == "LOI":
                if L >= O >= I:
                    return "LOI"
                elif L >= I >= O:
                    return "LIO"            
                elif O >= L >= I:
                    return "OLI"
                elif O >= I >= L:
                    return "OIL"
                elif I >= L >= O:
                    return "ILO"
                else:
                    return "IOL"
                
        return 1
                
                
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def ApprovalCheck(Chr = "Rogue", T = 1000, Type = "LOI", Spread = 150, TmpM = 1, TabM = 0, C = 1, Bonus = 0, Loc = 0, Check=0):  
        # $ Count = ApprovalCheck("Rogue",125)
        # T is the value being checked against, Type is the LOI condition in play, Spread is the difference between basic approval and high approval
        # TmpM is Tempmod multiplier, TabM is the taboo modifier, C is cologne modifiers, Bonus is a random bonus applied, and Loc is the girl's location

        if Chr == "Kitty":                                     
                #sets the data based on Kitty's data
                if Type == "X":
                    if K_Lust >= T:
                        return 1
                    else:
                        return 0
                elif Type == "TRST":
                    return K_Thirst                    
                L = K_Love
                O = K_Obed
                I = K_Inbt
                LocalTaboo = K_Taboo
                Loc = K_Loc if not Loc else Loc
        elif Chr == "Emma":                                      
                #sets the data based on Emma's data
                if Type == "X":
                    if E_Lust >= T:
                        return 1
                    else:
                        return 0
                elif Type == "TRST":
                    return E_Thirst  
                L = E_Love
                O = E_Obed
                I = E_Inbt
                LocalTaboo = E_Taboo
                Loc = E_Loc if not Loc else Loc
        elif Chr == "Laura":                                      
                #sets the data based on Laura's data
                if Type == "X":
                    if L_Lust >= T:
                        return 1
                    else:
                        return 0
                elif Type == "TRST":
                    return L_Thirst  
                L = L_Love
                O = L_Obed
                I = L_Inbt
                LocalTaboo = L_Taboo
                Loc = L_Loc if not Loc else Loc
        else: # Chr == "Rogue":                                 
                #sets the data based on Rogue's data
                if Type == "X":
                    if R_Lust >= T:
                        return 1
                    else:
                        return 0
                elif Type == "TRST":
                    return R_Thirst  
                L = R_Love
                O = R_Obed
                I = R_Inbt
                LocalTaboo = R_Taboo
                Loc = R_Loc if not Loc else Loc
        
        if Loc == bg_current:
                #Bumps stats based on colognes
                if Chr == "Laura":
                        if "mandrill" in P_Traits and C:                      
                                if L <= 400:
                                    L += 600
                                else:
                                    L = 1200
                                if "drugged" not in L_Traits:
                                        L_Traits.append("drugged")
                        elif "purple" in P_Traits and C:
                                if O <= 400:
                                    O += 600
                                else:
                                    O = 1200
                                if "drugged" not in L_Traits:
                                        L_Traits.append("drugged")
                        elif "corruption" in P_Traits and C:
                                if I <= 400:
                                    I += 600
                                else:
                                    I = 1200   
                                if "drugged" not in L_Traits:
                                        L_Traits.append("drugged")                     
                else:
                        if "mandrill" in P_Traits and C:                      
                                if L <= 500:
                                    L += 500
                                else:
                                    L = 1000
                        elif "purple" in P_Traits and C:
                                if O <= 500:
                                    O += 500
                                else:
                                    O = 1000
                        elif "corruption" in P_Traits and C:
                                if I <= 500:
                                    I += 500
                                else:
                                    I = 1000
       
        if Type == "LOI":
                LocalTaboo = LocalTaboo * 10
                LocalTempmod = Tempmod * 10
                
        elif Type == "LO":                      #40 -> 240
                #culls unwanted parameters.
                #These bits multiply everything from the 0-300 range to the 0-3000 range  
                I = 0
                LocalTaboo = LocalTaboo * 6                              
                LocalTempmod = Tempmod * 6
        elif Type == "OI":
                L = 0
                LocalTaboo = LocalTaboo * 6
                LocalTempmod = Tempmod * 6
        elif Type == "LI":
                O = 0
                LocalTaboo = LocalTaboo * 6      
                LocalTempmod = Tempmod * 6
                
        elif Type == "L":                       #40 -> 120
                O = 0
                I = 0
                LocalTaboo = LocalTaboo * 3
                LocalTempmod = Tempmod * 3
        elif Type == "O":
                L = 0
                I = 0
                LocalTaboo = LocalTaboo * 3
                LocalTempmod = Tempmod * 3
        elif Type == "I":
                O = 0
                L = 0
                LocalTaboo = LocalTaboo * 3      
                LocalTempmod = Tempmod * 3
                
        else:            
                LocalTaboo = LocalTaboo * 10         #40 -> 400
                LocalTempmod = Tempmod * 10
        
        TabM = 0 if TabM <= 0 else TabM #test this, makes sure TabM is positive
        
        if Check:
                #this returns the actual value of the tested stat.
                Check = (L + O + I + Bonus + (TmpM * LocalTempmod) - (TabM * LocalTaboo))
                return Check        
        
        if (L + O + I + Bonus + (TmpM * LocalTempmod) - (TabM * LocalTaboo)) >= (T + (2 * Spread)):                           
                #She passes and loves it
                return 3    
        elif (L + O + I + Bonus + (TmpM * LocalTempmod) - (TabM * LocalTaboo)) >= (T + Spread):                                  
                #She passes
                return 2
        elif (L + O + I + Bonus + (TmpM * LocalTempmod) - (TabM * LocalTaboo)) >= T:                         
                #She doesn't really want to, but can be convinced
                return 1
        else:                                                                                                   #She's out
                return 0

#end approval function //////////////////////////////////////////////////////////////////////////////

    def Room_Full(Present = []):
        # Culls parties down to 2 max
        # if Room_Full(): do something to empty it. 
        
        global Party
        Present = []
        while len(Party) > 2:    
                # If two or more members in the party    
                #Culls down party size to two
                Party.remove(Party[2])   
        
        # checks to see which girls are present at a given location
        # adds members who are not currently in the party
        if R_Loc == bg_current:
                if "Rogue" not in Party:        
                    Present.append("Rogue")
        if K_Loc == bg_current:
                if "Kitty" not in Party:         
                    Present.append("Kitty") 
        if E_Loc == bg_current:
                if "Emma" not in Party: 
                    Present.append("Emma") 
        if L_Loc == bg_current:
                if "Laura" not in Party: 
                    Present.append("Laura") 
        
        if len(Party) + len(Present) >= 2:                
            return 1      
        else:
            return 0   
            
    #end RoomFull

    def Zero_Loc(Girl=0):
                #returns the location of the girl fed to it.
                # if Zero_Loc(Girl) == bg_current: #. . .
                if Girl == "Rogue":
                        return R_Loc
                elif Girl == "Kitty":
                        return K_Loc
                elif Girl == "Emma":
                        return E_Loc
                elif Girl == "Laura":                
                        return L_Loc                        
                return 
    
    def AloneCheck(Girl=0,Alone=0):
                # returns a positive value if other people are around
                # if Girl, it checks if she's the only one in the room
                Alone = 0
                if R_Loc == bg_current and Girl != "Rogue":
                        Alone += 1
                if K_Loc == bg_current and Girl != "Kitty":
                        Alone += 1
                if E_Loc == bg_current and Girl != "Emma":
                        Alone += 1
                if L_Loc == bg_current and Girl != "Laura": 
                        Alone += 1
                return Alone
                        
    def ChestNum(Chr = "Rogue"): 
                #This function determines how much Bra are on, 5 for decent, less for less.                
                if Chr == "Rogue":
                        if R_Uptop and R_Chest:
                            return 1
                        if R_Chest == "tank":
                            return 5
                        elif R_Chest == "lace bra":
                            return 2
                        elif R_Chest:
                            return 4
                        else:
                            return 0
                elif Chr == "Kitty":
                        if K_Uptop and K_Chest:
                            return 1
                        if K_Chest == "lace bra":
                            return 2    
                        elif K_Chest:
                            return 4      
                        else:
                            return 0
                elif Chr == "Emma":   
                        if E_Uptop and E_Chest:
                            return 1    
                        if E_Chest == "corset":
                            return 5     
                        elif E_Chest == "lace bra":
                            return 2    
                        elif E_Chest:
                            return 4      
                        else:
                            return 0
                elif Chr == "Laura":
                        if L_Uptop and L_Chest:
                            return 1
                        if L_Chest == "leather bra":
                            return 5         
                        elif L_Chest == "wolvie top":
                            return 3        
                        elif L_Chest == "lace corset":
                            return 2    
                        elif L_Chest:
                            return 4  
                        else:
                            return 0                            
                #if it falls though. . .
                return 0 
    
    def OverNum(Chr = "Rogue"): 
                #This function determines how much Over are on, 5 for decent, less for less.
                if Chr == "Rogue":
                        if R_Uptop and R_Over:
                            return 1
                        if R_Over == "mesh top":
                            return 2
                        elif R_Over == "towel":
                            return 3
                        elif R_Over:
                            return 5
                        else:
                            return 0
                elif Chr == "Kitty":
                        if K_Uptop and K_Over:
                            return 1
                        if K_Over == "pink top":
                            return 4
                        elif K_Over == "towel":
                            return 3
                        elif K_Over:
                            return 5
                        else:
                            return 0
                elif Chr == "Emma":   
                        if E_Uptop and E_Over:
                            return 1
                        if E_Over == "jacket":
                            return 4
                        elif E_Over == "towel":
                            return 3
                        elif E_Over == "nighty":
                            return 3
                        elif E_Over:
                            return 5
                        else:
                            return 0
                elif Chr == "Laura":
                        if L_Uptop and L_Over:
                            return 1
                        if L_Over == "jacket":
                            return 4
                        elif L_Over == "towel":
                            return 3
                        elif L_Over:
                            return 5
                        else:
                            return 0                         
                #if it falls though. . .
                return 0 
                
    def PantsNum(Chr = "Rogue"): 
                #This function determines how much pants are on, 10 for pants, 5 for skirt, <5 for less.
                if Chr == "Rogue":
                        if R_Upskirt and R_Legs:
                            return 1
                        if R_Legs == "skirt":
                            return 5
                        elif IsOutfitModdedRogue("Legs"):
                            return ModPantsNum("Rogue")    
                        elif R_Legs == "pants":
                            return 10
                        elif R_Panties == "shorts":
                            return 6
                        else:
                            return 0
                elif Chr == "Kitty":
                        if K_Upskirt and K_Legs:
                            return 1
                        if K_Legs == "black jeans":
                            return 10
                        elif IsOutfitModdedKitty("Legs"):
                            return ModPantsNum("Kitty")            
                        elif K_Legs == "capris":
                            return 10    
                        elif K_Legs == "yoga pants":
                            return 8                    
                        elif K_Legs == "shorts":
                            return 6       
                        elif K_Legs == "blue skirt":
                            return 5
                        else:
                            return 0
                elif Chr == "Emma":
                        if E_Upskirt and E_Legs:
                            return 1
                        if E_Legs == "pants":
                            return 10                           
                        elif E_Legs == "yoga pants":
                            return 10 
                        elif E_Legs == "skirt":
                            return 5   
                        else:
                            return 0
                elif Chr == "Laura":
                        if L_Upskirt and L_Legs:
                            return 1
                        if L_Legs == "leather pants":
                            return 10        
                        elif L_Legs == "skirt":
                            return 5   
                        elif L_Legs == "mesh pants":
                            return 2        
                        else:
                            return 0
                            
                #if it falls though. . .
                return 0 
    
    def PantiesNum(Chr = "Rogue"): 
                #This function determines how much panties are on, 5 for decent, less for less.
                if Chr == "Rogue":
                        if R_PantiesDown and R_Panties:
                            return 1
                        if R_Panties == "lace panties":
                            return 2
                        elif R_Panties:
                            return 5
                elif Chr == "Kitty":
                        if K_PantiesDown and K_Panties:
                            return 1
                        if K_Panties == "lace panties":
                            return 2
                        elif K_Panties:
                            return 5
                elif Chr == "Emma":  
                        if E_PantiesDown and E_Panties:
                            return 1  
                        if E_Panties == "lace panties":
                            return 2
                        elif E_Panties:
                            return 5
                elif Chr == "Laura":
                        if L_PantiesDown and L_Panties:
                            return 1
                        if L_Panties == "lace panties":
                            return 2
                        elif L_Panties:
                            return 5                        
                #if it falls though. . .
                return 0 
                
    def HoseNum(Chr = "Rogue"): 
                #This function determines how seethrough her hose is, 5 for "visible," 10 for "solid"
                if Chr == "Rogue":
                            if R_PantiesDown and R_Hose:
                                return 0
                            if R_Hose == "stockings":
                                return 1
                            elif R_Hose == "pantyhose":
                                return 6
                            elif R_Hose == "tights":
                                return 10
                            elif R_Hose == "stockings and gaterbelt":
                                return 5
                            elif R_Hose == "ripped pantyhose":
                                return 5
                            elif R_Hose == "ripped tights":
                                return 5
                            else:
                                return 0
                                
                elif Chr == "Kitty":
                            if K_PantiesDown and K_Hose:
                                return 0
                            if K_Hose == "stockings":
                                return 1
                            else:
                                return 0
                elif Chr == "Emma":
                            if E_PantiesDown and E_Hose:
                                return 0
                            if E_Hose == "stockings":
                                return 1
                            else:
                                return 0
                elif Chr == "Laura":
                            if L_PantiesDown and L_Hose:
                                return 0
                            if L_Hose == "stockings":
                                return 1
                            elif L_Hose == "stockings and garterbelt":
                                return 1
                            else:
                                return 0
                                
                #if it falls though. . .        
                return 0 
       
    def ClothingCheck(Chr = "Rogue", C = 0): 
                C = 0
                #This function counts how many items of clothing she has on and returns that number.
                if Chr == "Rogue":
                        if R_Over:
                            C += 1
                        if R_Chest:
                            C += 1
                        if R_Legs:
                            C += 1
                        if HoseNum("Rogue") >= 5:
                            C += 1
                        if R_Panties:
                            C += 1
                elif Chr == "Kitty":
                        if K_Over:
                            C += 1
                        if K_Chest:
                            C += 1
                        if K_Legs:
                            C += 1
                        if HoseNum("Kitty") >= 5:
                            C += 1
                        if K_Panties:
                            C += 1
                elif Chr == "Emma":
                        if E_Over:
                            C += 1
                        if E_Chest:
                            C += 1
                        if E_Legs:
                            C += 1
                        if HoseNum("Emma") >= 5:
                            C += 1
                        if E_Panties:
                            C += 1
                elif Chr == "Laura":
                        if L_Over:
                            C += 1
                        if L_Chest:
                            C += 1
                        if L_Legs:
                            C += 1
                        if HoseNum("Laura") >= 5:
                            C += 1
                        if L_Panties:
                            C += 1
                return C 
                
    def SeenCheck(Chr = "Rogue", Check=0, C = 0): 
                C = 0
                #This function returns 1-2 if she is partiallly naked and this is the first the player's seen of it.
                # "Check" is 1 if it's intended to see whether she has been seen at all.
                # "Check" is 2 if it's intended to see whether she has been seen topless.
                # "Check" is 3 if it's intended to see whether she has been seen bottomless.
                if Chr == "Rogue":
                        if not R_SeenChest:
                            if (not R_Over and not R_Chest) or R_Uptop or Check == 1 or Check == 2:
                                        C += 1
                        if not R_SeenPussy:
                            if Check == 1 or Check == 3:
                                        C += 1
                            elif not R_Legs or R_Upskirt: #if no pants or pants down
                                if R_PantiesDown or (HoseNum("Rogue") < 5 and not R_Panties): # if no panties and loose hose or they're down
                                        C += 1
                elif Chr == "Kitty":
                        if not K_SeenChest:
                            if (not K_Over and not K_Chest) or K_Uptop or Check == 1 or Check == 2:
                                        C += 1
                        if not K_SeenPussy:
                            if Check == 1 or Check == 3:
                                        C += 1
                            elif not K_Legs or K_Upskirt: #if no pants or pants down
                                if K_PantiesDown or (HoseNum("Rogue") < 5 and not K_Panties): # if no panties and loose hose or they're down
                                        C += 1
                elif Chr == "Emma":
                        if not E_SeenChest:
                            if (not E_Over and not E_Chest) or E_Uptop or Check == 1 or Check == 2:
                                        C += 1
                        if not E_SeenPussy:
                            if Check == 1 or Check == 3:
                                        C += 1
                            elif not E_Legs or E_Upskirt: #if no pants or pants down
                                if E_PantiesDown or (HoseNum("Rogue") < 5 and not E_Panties): # if no panties and loose hose or they're down
                                        C += 1
                elif Chr == "Laura":
                        if not L_SeenChest:
                            if (not L_Over and not L_Chest) or L_Uptop or Check == 1 or Check == 2:
                                        C += 1
                        if not L_SeenPussy:
                            if Check == 1 or Check == 3:
                                        C += 1
                            elif not L_Legs or L_Upskirt: #if no pants or pants down
                                if L_PantiesDown or (HoseNum("Rogue") < 5 and not L_Panties): # if no panties and loose hose or they're down
                                        C += 1
                return C 
                
    def ExhibitionistCheck(Chr = "Rogue"): 
                #This function returns 1-2 if she is partiallly naked and this is the first the player's seen of it.
                if Chr == "Rogue":
                        if "exhibitionist" in R_Traits:
                            return 1
                elif Chr == "Kitty":
                        if "exhibitionist" in K_Traits:
                            return 1
                elif Chr == "Emma":
                        if "exhibitionist" in E_Traits:
                            return 1
                elif Chr == "Laura":
                        if "exhibitionist" in L_Traits:
                            return 1
                return 0 
                
    def GirlLikeCheck(GirlA=0,GirlB=0):
            # returns how much A likes B
            # if GirlLikeCheck("Rogue","Kitty") >= 500:
            
            if GirlA == "Rogue":  
                    if GirlB == "Kitty":
                                return R_LikeKitty
                    elif GirlB == "Emma":
                                return R_LikeEmma
                    elif GirlB == "Laura":
                                return R_LikeLaura
            elif GirlA == "Kitty":  
                    if GirlB == "Rogue":
                                return K_LikeRogue
                    elif GirlB == "Emma":
                                return K_LikeEmma
                    elif GirlB == "Laura":
                                return K_LikeLaura
            elif GirlA == "Emma":  
                    if GirlB == "Rogue":
                                return E_LikeRogue
                    elif GirlB == "Kitty":
                                return E_LikeKitty
                    elif GirlB == "Laura":
                                return E_LikeLaura
            elif GirlA == "Laura":  
                    if GirlB == "Rogue":
                                return L_LikeRogue
                    elif GirlB == "Kitty":
                                return L_LikeKitty
                    elif GirlB == "Emma":
                                return L_LikeEmma
            return 0        


    def CheckWord(Girl=0,Type=0,Check=0):
            # checks whether the girl has the required stat
            # CheckWord("Rogue","Recent","something")
            
#            "[Girl],[Type],[Check]" #fix, remove, diagnostic
            if Girl == "Rogue":
                    if Type == "Recent":
                        if Check in R_RecentActions:
                            return 1
                    elif Type == "Daily":
                        if Check in R_DailyActions:
                            return 1
                    elif Type == "Traits":
                        if Check in R_Traits:
                            return 1
                    elif Type == "History":
                        if Check in R_History:
                            return 1 
                    elif Type == "Petnames":
                        if Check in R_Petnames:
                            return 1                                      
            elif Girl == "Kitty":
                    if Type == "Recent":
                        if Check in K_RecentActions:
                            return 1
                    elif Type == "Daily":
                        if Check in K_DailyActions:
                            return 1
                    elif Type == "Traits":
                        if Check in K_Traits:
                            return 1
                    elif Type == "History":
                        if Check in K_History:
                            return 1    
                    elif Type == "Petnames":
                        if Check in K_Petnames:
                            return 1      
            elif Girl == "Emma":
                    if Type == "Recent":
                        if Check in E_RecentActions:
                            return 1
                    elif Type == "Daily":
                        if Check in E_DailyActions:
                            return 1
                    elif Type == "Traits":
                        if Check in E_Traits:
                            return 1
                    elif Type == "History":
                        if Check in E_History:
                            return 1     
                    elif Type == "Petnames":
                        if Check in E_Petnames:
                            return 1     
            elif Girl == "Laura":
                    if Type == "Recent":
                        if Check in L_RecentActions:
                            return 1
                    elif Type == "Daily":
                        if Check in L_DailyActions:
                            return 1
                    elif Type == "Traits":
                        if Check in L_Traits:
                            return 1
                    elif Type == "History":
                        if Check in L_History:
                            return 1    
                    elif Type == "Petnames":
                        if Check in L_Petnames:
                            return 1      
            return 0
            
# Start History checker / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    def HistoryCheck(Girl=0,Check=0):
        #girl is the girl, Check is the condition being checked, returns the value of that stat
        if Girl == "Rogue":
                if Check == "caught":
                    return R_Caught
                elif Check == "kissed":
                    return R_Kissed 
                elif Check == "hand":
                    return R_Hand
                elif Check == "sex":
                    return R_Sex
                elif Check == "anal":
                    return R_Anal                  
                elif Check == "blow":
                    return R_Blow 
                elif Check == "foot":
                    return R_Foot
                elif Check == "titjob":
                    return R_Tit                      
                elif Check == "hotdog":
                    return R_Hotdog                    
                elif Check == "masturbation":
                    return R_Mast 
                elif Check == "orgasm":
                    return R_Org
                elif Check == "fondle breast":
                    return R_FondleB 
                elif Check == "fondle thighs":
                    return R_FondleT
                elif Check == "fondle pussy":
                    return R_FondleP 
                elif Check == "fondle ass":
                    return R_FondleA 
                elif Check == "dildo pussy":
                    return R_DildoP
                elif Check == "dildo ass":
                    return R_DildoA 
                elif Check == "suck breasts":
                    return R_SuckB                
                elif Check == "insert ass":
                    return R_InsertA
                elif Check == "lick pussy":
                    return R_LickP                    
                elif Check == "lick ass":
                    return R_LickA                
                elif Check == "swallowed":
                    return R_Swallow
                elif Check == "strip":
                    return R_Strip 
        if Girl == "Rogue":
                if Check == "caught":
                    return R_Caught
                elif Check == "kissed":
                    return R_Kissed 
                elif Check == "hand":
                    return R_Hand
                elif Check == "sex":
                    return R_Sex
                elif Check == "anal":
                    return R_Anal                  
                elif Check == "blow":
                    return R_Blow 
                elif Check == "foot":
                    return R_Foot
                elif Check == "titjob":
                    return R_Tit                      
                elif Check == "hotdog":
                    return R_Hotdog                    
                elif Check == "masturbation":
                    return R_Mast 
                elif Check == "orgasm":
                    return R_Org
                elif Check == "fondle breast":
                    return R_FondleB 
                elif Check == "fondle thighs":
                    return R_FondleT
                elif Check == "fondle pussy":
                    return R_FondleP 
                elif Check == "fondle ass":
                    return R_FondleA 
                elif Check == "dildo pussy":
                    return R_DildoP
                elif Check == "dildo ass":
                    return R_DildoA 
                elif Check == "suck breasts":
                    return R_SuckB                
                elif Check == "insert ass":
                    return R_InsertA
                elif Check == "lick pussy":
                    return R_LickP                    
                elif Check == "lick ass":
                    return R_LickA                
                elif Check == "swallowed":
                    return R_Swallow
                elif Check == "strip":
                    return R_Strip 
        elif Girl == "Kitty":
                if Check == "caught":
                    return K_Caught
                elif Check == "kissed":
                    return K_Kissed 
                elif Check == "hand":
                    return K_Hand
                elif Check == "sex":
                    return K_Sex
                elif Check == "anal":
                    return K_Anal                  
                elif Check == "blow":
                    return K_Blow 
                elif Check == "foot":
                    return K_Foot
                elif Check == "titjob":
                    return K_Tit                      
                elif Check == "hotdog":
                    return K_Hotdog                    
                elif Check == "masturbation":
                    return K_Mast 
                elif Check == "orgasm":
                    return K_Org
                elif Check == "fondle breast":
                    return K_FondleB 
                elif Check == "fondle thighs":
                    return K_FondleT
                elif Check == "fondle pussy":
                    return K_FondleP 
                elif Check == "fondle ass":
                    return K_FondleA 
                elif Check == "dildo pussy":
                    return K_DildoP
                elif Check == "dildo ass":
                    return K_DildoA 
                elif Check == "suck breasts":
                    return K_SuckB                
                elif Check == "insert ass":
                    return K_InsertA
                elif Check == "lick pussy":
                    return K_LickP                    
                elif Check == "lick ass":
                    return K_LickA                
                elif Check == "swallowed":
                    return K_Swallow
                elif Check == "strip":
                    return K_Strip 
        elif Girl == "Emma":
                if Check == "caught":
                    return E_Caught
                elif Check == "kissed":
                    return E_Kissed 
                elif Check == "hand":
                    return E_Hand
                elif Check == "sex":
                    return E_Sex
                elif Check == "anal":
                    return E_Anal                  
                elif Check == "blow":
                    return E_Blow 
                elif Check == "foot":
                    return E_Foot
                elif Check == "titjob":
                    return E_Tit                      
                elif Check == "hotdog":
                    return E_Hotdog                    
                elif Check == "masturbation":
                    return E_Mast 
                elif Check == "orgasm":
                    return E_Org
                elif Check == "fondle breast":
                    return E_FondleB 
                elif Check == "fondle thighs":
                    return E_FondleT
                elif Check == "fondle pussy":
                    return E_FondleP 
                elif Check == "fondle ass":
                    return E_FondleA 
                elif Check == "dildo pussy":
                    return E_DildoP
                elif Check == "dildo ass":
                    return E_DildoA 
                elif Check == "suck breasts":
                    return E_SuckB                
                elif Check == "insert ass":
                    return E_InsertA
                elif Check == "lick pussy":
                    return E_LickP                    
                elif Check == "lick ass":
                    return E_LickA                
                elif Check == "swallowed":
                    return E_Swallow
                elif Check == "strip":
                    return E_Strip 
        elif Girl == "Laura":
                if Check == "caught":
                    return L_Caught
                elif Check == "kissed":
                    return L_Kissed 
                elif Check == "hand":
                    return L_Hand
                elif Check == "sex":
                    return L_Sex
                elif Check == "anal":
                    return L_Anal                  
                elif Check == "blow":
                    return L_Blow 
                elif Check == "foot":
                    return L_Foot
                elif Check == "titjob":
                    return L_Tit                      
                elif Check == "hotdog":
                    return L_Hotdog                    
                elif Check == "masturbation":
                    return L_Mast 
                elif Check == "orgasm":
                    return L_Org
                elif Check == "fondle breast":
                    return L_FondleB 
                elif Check == "fondle thighs":
                    return L_FondleT
                elif Check == "fondle pussy":
                    return L_FondleP 
                elif Check == "fondle ass":
                    return L_FondleA 
                elif Check == "dildo pussy":
                    return L_DildoP
                elif Check == "dildo ass":
                    return L_DildoA 
                elif Check == "suck breasts":
                    return L_SuckB                
                elif Check == "insert ass":
                    return L_InsertA
                elif Check == "lick pussy":
                    return L_LickP                    
                elif Check == "lick ass":
                    return L_LickA                
                elif Check == "swallowed":
                    return L_Swallow
                elif Check == "strip":
                    return L_Strip         
        return
# End History checker / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# End Python Init stuff/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / // / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Speed_Shift(S=0):   
    #adjusts the speed of animations to S, uses fade to hide glitches
    # call Speed_Shift(2)
    $ Speed = S
    show blackscreen onlayer black 
    pause 0.01 
    hide blackscreen onlayer black 
    return

label Statup(Name=0, Flavor=0, Check=100, Value=1, Greater=0, Type=0, Overflow=0, BStat=0, XPOS = 0.75):
        # Name is the target girl
        # "Flavor" is the thing being modified, such as Love
        # Type is the base value of that stat
        # Check is the maximum threshold, it won't raise if already above that value
        # Greater reverses the above check
        # Value is the amount raised
        # Overflow checks whether you've assigned a stat overflow
        # BStat stores the leftovers in the overflowed stat
        
        if Flavor == "Love" or Flavor == "Obed" or Flavor == "Inbt":
                #bumps this stat into the 1000s
                $ Check = Check * 10                  
        
        
        if Flavor == "Focus":
                $ Type = P_Focus
        elif Name == "Rogue":
                #sets the details based on character
                if Flavor == "Love":
                        $ Type = R_Love
                elif Flavor == "Obed":
                        $ Type = R_Obed
                elif Flavor == "Inbt":
                        $ Type = R_Inbt
                elif Flavor == "Lust":
                        $ Type = R_Lust
                $ Overflow = R_Chat[4]
                $ XPOS = R_SpriteLoc
        elif Name == "Kitty":
                if Flavor == "Love":
                        $ Type = K_Love
                elif Flavor == "Obed":
                        $ Type = K_Obed
                elif Flavor == "Inbt":
                        $ Type = K_Inbt
                elif Flavor == "Lust":
                        $ Type = K_Lust
                $ Overflow = K_Chat[4]
                $ XPOS = K_SpriteLoc
        elif Name == "Emma":
                if Flavor == "Love":
                        $ Type = E_Love
                elif Flavor == "Obed":
                        $ Type = E_Obed
                elif Flavor == "Inbt":
                        $ Type = E_Inbt
                elif Flavor == "Lust":
                        $ Type = E_Lust
                $ Overflow = E_Chat[4]
                $ XPOS = E_SpriteLoc
        elif Name == "Laura":
                if Flavor == "Love":
                        $ Type = L_Love
                elif Flavor == "Obed":
                        $ Type = L_Obed
                elif Flavor == "Inbt":
                        $ Type = L_Inbt
                elif Flavor == "Lust":
                        $ Type = L_Lust
                $ Overflow = L_Chat[4]
                $ XPOS = L_SpriteLoc
        else:
                # If there is no valid name, then return
                return
        # endset
        
#        if Clear:
#            #if set to Clear, subtract the full amount from the trait.
#            # ie call Statup(Options[0], "Lust", 25, 5, 1, Clear=1), if Lust is >25, it will subtract all Lust from Lust
#            $ Value = -Type
            
        if Greater:                             
                #this checks if it's greater or less than the intended value
                #if it fails, the value is zeroed out, cancelling the rest
                if Type >= Check:
                    #If it passes the check, add Value to it 
                    $ Type += Value                   
                else:
                    #If not, don't add Value and set Value to 0
                    $ Value = 0                      
        else:
                if Type <= Check:
                    $ Type += Value  
                else:
                    $ Value = 0
                            
        if Value:                                       
            #If there is any change to the stat           
            if Flavor == "Love":                        
                    #Sets reporting text color based on Flavor
                    $ Color = "#c11b17"
            elif Flavor == "Obed":
                    $ Color = "#2554c7"
            elif Flavor == "Inbt":
                    $ Color = "#FFF380"
            elif Flavor == "Lust":
                    $ Color = "#FAAFBE"
            elif Flavor == "Focus":
                    $ Color = "#FFFFFF"                    
                    $ P_Focus += Value
                    $ CallHolder(Value, Color, XPOS)
                    return
                 
            if Type > 1000 and Flavor != "Lust":    
                    #if the value overflows, play one value meter, then. . .
                    $ CallHolder((-(Type-1000-Value)), Color, XPOS)  
                    $ Value = Type - 1000
                    if Flavor == "Love":    
                            $ BStat = "Love"
                            if Overflow == 1:       #[Love to Obedience]
                                $ Flavor = "Obed"
                            elif Overflow == 2:     #[Love to Inhibition] 
                                $ Flavor = "Inbt"
                            else: 
                                $ Value = 0  
                    elif Flavor == "Obed":    
                            $ BStat = "Obed"
                            if Overflow == 3:       #[Obedience to Inhibition]
                                $ Flavor = "Obed"
                            elif Overflow == 4:    
                                $ Flavor = "Love"   #[Obedience to Love] 
                            else: 
                                $ Value = 0  
                    elif Flavor == "Inbt":    
                            $ BStat = "Inbt"
                            if Overflow == 5:       #[Inhibition to Obedience]
                                $ Flavor = "Obed"
                            elif Overflow == 6:    
                                $ Flavor = "Love"    #[Inhibition to Love]
                            else: 
                                $ Value = 0  
                               
                    if Flavor == "Love":                        
                            #Sets reporting text color based on Flavor
                            $ Color = "#c11b17"
                    elif Flavor == "Obed":
                            $ Color = "#2554c7"
                    elif Flavor == "Inbt":
                            $ Color = "#FFF380"
                    else:
                            $ Color = "#FFFFFF"
                    
            if Value:                
                $ CallHolder(Value, Color, XPOS)
            
            if Flavor == "Lust" and Type >= 100:
                if not Trigger:
                        #calls orgasm if Lust goes over 100, breaks routine
                        if Name == "Rogue":        
                            call R_Cumming(1)
                        elif Name == "Kitty":     
                            call K_Cumming(1)
                        elif Name == "Emma":    
                            call E_Cumming(1)
                        elif Name == "Laura":    
                            call L_Cumming(1)  
                        $ Value = 0
                        return
                    
        #end "if value is positive"
                    
        $ Type = 1000 if Type > 1000 else Type
        
        if Name == "Rogue":
                if Flavor == "Love":
                        $ R_Love += Value
                        $ R_Love = 1000 if R_Love > 1000 else R_Love
                elif Flavor == "Obed":
                        $ R_Obed += Value
                        $ R_Obed = 1000 if R_Obed > 1000 else R_Obed
                elif Flavor == "Inbt":
                        $ R_Inbt += Value
                        $ R_Inbt = 1000 if R_Inbt > 1000 else R_Inbt
                elif Flavor == "Lust":
                        $ R_Lust += Value
                        $ R_Lust = 100 if R_Lust > 100 else R_Lust
                        
                if BStat == "Love":
                        $ R_Love = 1000
                elif BStat == "Obed":
                        $ R_Obed = 1000
                elif BStat == "Inbt":
                        $ R_Inbt = 1000
        elif Name == "Kitty":
                if Flavor == "Love":
                        $ K_Love += Value   
                        $ K_Love = 1000 if K_Love > 1000 else K_Love                     
                elif Flavor == "Obed":
                        $ K_Obed += Value
                        $ K_Obed = 1000 if K_Obed > 1000 else K_Obed 
                elif Flavor == "Inbt":
                        $ K_Inbt += Value
                        $ K_Inbt = 1000 if K_Inbt > 1000 else K_Inbt 
                elif Flavor == "Lust":
                        $ K_Lust += Value
                        $ K_Lust = 100 if K_Lust > 100 else K_Lust 
                        
                if BStat == "Love":
                        $ K_Love = 1000
                elif BStat == "Obed":
                        $ K_Obed = 1000
                elif BStat == "Inbt":
                        $ K_Inbt = 1000
        elif Name == "Emma":
                if Flavor == "Love":
                        $ E_Love += Value
                        $ E_Love = 1000 if E_Love > 1000 else E_Love
                elif Flavor == "Obed":
                        $ E_Obed += Value
                        $ E_Obed = 1000 if E_Obed > 1000 else E_Obed
                elif Flavor == "Inbt":
                        $ E_Inbt += Value
                        $ E_Inbt = 1000 if E_Inbt > 1000 else E_Inbt
                elif Flavor == "Lust":
                        $ E_Lust += Value
                        $ E_Lust = 100 if E_Lust > 100 else E_Lust
                        
                if BStat == "Love":
                        $ E_Love = 1000
                elif BStat == "Obed":
                        $ E_Obed = 1000
                elif BStat == "Inbt":
                        $ E_Inbt = 1000
        elif Name == "Laura":
                if Flavor == "Love":
                        $ L_Love += Value
                        $ L_Love = 1000 if L_Love > 1000 else L_Love
                elif Flavor == "Obed":
                        $ L_Obed += Value
                        $ L_Obed = 1000 if L_Obed > 1000 else L_Obed
                elif Flavor == "Inbt":
                        $ L_Inbt += Value
                        $ L_Inbt = 1000 if L_Inbt > 1000 else L_Inbt
                elif Flavor == "Lust":
                        $ L_Lust += Value
                        $ L_Lust = 100 if L_Lust > 100 else L_Lust
                        
                if BStat == "Love":
                        $ L_Love = 1000
                elif BStat == "Obed":
                        $ L_Obed = 1000
                elif BStat == "Inbt":
                        $ L_Inbt = 1000
                # endset
            
        return

label RoomStatboost(Type=0,Check=0,Amount=0):
        # raises/lowers stats of all girls in the room by a fixed amount
        #ie call RoomStatboost("Love",80,2)
        if R_Loc == bg_current or "Rogue" in Nearby:
                call Statup("Rogue", Type, Check, Amount)
        if K_Loc == bg_current or "Kitty" in Nearby:
                call Statup("Kitty", Type, Check, Amount)
        if E_Loc == bg_current or "Emma" in Nearby:
                call Statup("Emma", Type, Check, Amount)
        if E_Loc == "bg teacher" and bg_current == "bg classroom":
                call Statup("Emma", Type, Check, Amount)
        if L_Loc == bg_current or "Laura" in Nearby:
                call Statup("Laura", Type, Check, Amount)
        return
    
label Quick_O(Girl=0,Quick=1):
    #used to call up a quick orgasm, mostly animation. 
    # call Quick_O("Rogue"), used 0 if you want the full dialogs.
    if Girl == "Rogue":
            call R_Cumming(1)
    elif Girl == "Kitty":
            call K_Cumming(1)
    elif Girl == "Emma":
            call E_Cumming(1)
    elif Girl == "Laura":
            call L_Cumming(1)
    return
    
    
label AnyFace(Girl=0,Emote = 5, B = 5, M = 0, Mouth = 0, Eyes = 0, Brows = 0):
        #this sends a face change to any girl listed
        #call AnyFace("Kitty","sadside",1)
        if Girl == "Rogue": 
                        call RogueFace(Emote=Emote,B=B,M=M,Mouth=Mouth,Eyes=Eyes,Brows=Brows)
        elif Girl == "Kitty": 
                        call KittyFace(Emote=Emote,B=B,M=M,Mouth=Mouth,Eyes=Eyes,Brows=Brows)
        elif Girl == "Emma": 
                        call EmmaFace(Emote=Emote,B=B,M=M,Mouth=Mouth,Eyes=Eyes,Brows=Brows)
        elif Girl == "Laura": 
                        call LauraFace(Emote=Emote,B=B,M=M,Mouth=Mouth,Eyes=Eyes,Brows=Brows)
        return

label AnyLine(Girl=0,PassLine=". . ."):
        #This calls a line from any girl you reference
        if Girl == "Rogue":
                ch_r "[PassLine]"
        elif Girl == "Kitty":
                ch_k "[PassLine]"
        elif Girl == "Emma":
                ch_e "[PassLine]"
        elif Girl == "Laura":
                ch_l "[PassLine]"
        return                          #fix try returning PassLine, and see if extend can use that. . .

label AnyOutfit(Girl=0,OutfitTemp = 5, Spunk = 0, Undressed = 0, Changed = 1, Perm=0, TempOver=0,TempChest=0,TempLegs=0,TempPanties=0,TempUpskirt=1,TempUptop=1,TempHose=0):
        #this sends a face change to any girl listed
        # "Perm" gets sent if the outfit is meant to stick        
        # if OutfitTemp == 5: $ R_OutfitTemp = R_Outfit
        # if OutfitTemp == 6: $ R_OutfitTemp = R_OutfitDay
        # Above that, it's based on changing one specific clothing item, 
        # if OutfitTemp == 7: $ R_Over = TempOver
        # if OutfitTemp == 8: $ R_Chest = TempChest
        # if OutfitTemp == 9: $ R_Legs = TempLegs
        # if OutfitTemp == 10: $ R_Panties = TempPanties
        # if OutfitTemp == 11: $ R_Upskirt = TempUpskirt
        # if OutfitTemp == 12: $ R_Uptop = TempUptop
        # if OutfitTemp == 13: $ R_Hose = TempHose
        # call AnyOutfit(Girl,8,TempChest=0)
                                
        if Girl == "Rogue": 
                    if 7 <= OutfitTemp <= 20:
                        # if Outfittemp is between 7 and 20                        
                        if OutfitTemp == 7: 
                                $ R_Over = TempOver
                        elif OutfitTemp == 8: 
                                $ R_Chest = TempChest
                        elif OutfitTemp == 9: 
                                $ R_Legs = TempLegs
                        elif OutfitTemp == 10: 
                                $ R_Panties = TempPanties
                        elif OutfitTemp == 11: 
                                $ R_Upskirt = TempUpskirt
                        elif OutfitTemp == 12: 
                                $ R_Uptop = TempUptop
                        elif OutfitTemp == 13: 
                                $ R_Hose = TempHose
                    else:
                        $ R_Outfit = OutfitTemp if Perm else R_Outfit
                        call RogueOutfit(OutfitTemp,Spunk,Undressed,Changed)
        elif Girl == "Kitty": 
                    if 7 <= OutfitTemp <= 20:
                        # if Outfittemp is between 7 and 20                        
                        if OutfitTemp == 7: 
                                $ K_Over = TempOver
                        elif OutfitTemp == 8: 
                                $ K_Chest = TempChest
                        elif OutfitTemp == 9: 
                                $ K_Legs = TempLegs
                        elif OutfitTemp == 10: 
                                $ K_Panties = TempPanties
                        elif OutfitTemp == 11: 
                                $ K_Upskirt = TempUpskirt
                        elif OutfitTemp == 12: 
                                $ K_Uptop = TempUptop
                        elif OutfitTemp == 13: 
                                $ K_Hose = TempHose
                    else:
                        $ K_Outfit = OutfitTemp if Perm else K_Outfit
                        call KittyOutfit(OutfitTemp,Spunk,Undressed,Changed)
        elif Girl == "Emma": 
                    if 7 <= OutfitTemp <= 20:
                        # if Outfittemp is between 7 and 20                        
                        if OutfitTemp == 7: 
                                $ E_Over = TempOver
                        elif OutfitTemp == 8: 
                                $ E_Chest = TempChest
                        elif OutfitTemp == 9: 
                                $ E_Legs = TempLegs
                        elif OutfitTemp == 10: 
                                $ E_Panties = TempPanties
                        elif OutfitTemp == 11: 
                                $ E_Upskirt = TempUpskirt
                        elif OutfitTemp == 12: 
                                $ E_Uptop = TempUptop
                        elif OutfitTemp == 13: 
                                $ E_Hose = TempHose
                    else:
                        $ E_Outfit = OutfitTemp if Perm else E_Outfit
                        call EmmaOutfit(OutfitTemp,Spunk,Undressed,Changed)
        elif Girl == "Laura": 
                    if 7 <= OutfitTemp <= 20:
                        # if Outfittemp is between 7 and 20                        
                        if OutfitTemp == 7: 
                                $ L_Over = TempOver
                        elif OutfitTemp == 8: 
                                $ L_Chest = TempChest
                        elif OutfitTemp == 9: 
                                $ L_Legs = TempLegs
                        elif OutfitTemp == 10: 
                                $ L_Panties = TempPanties
                        elif OutfitTemp == 11: 
                                $ L_Upskirt = TempUpskirt
                        elif OutfitTemp == 12: 
                                $ L_Uptop = TempUptop
                        elif OutfitTemp == 13: 
                                $ L_Hose = TempHose
                    else:
                        $ L_Outfit = OutfitTemp if Perm else L_Outfit
                        call LauraOutfit(OutfitTemp,Spunk,Undressed,Changed)
        return
    
    
label GirlLikesGirl(ChrA = "Rogue", ChrB = "Kitty", Check=200, Modifier = 1, Auto = 0, Jealousy = 0, Ok = 0, Likes=0):
        # ChrA is the subject girl, ChrB is the object girl,
        # Modifier is sent as the amount of offense this might cause,
        # Jealousy is the temp value for how mad the girl will get
        # Likes stores the XLikesY stat temporarily
        # Auto quickly raises lust and like by a sent amount
        # call GirlLikesGirl(Party[0],Party[1],700,5,1)
        
#        "[ChrA], [ChrB], [Check], [Modifier]" #diagnostic
        if ChrA == "Rogue":                                             
                #If the first girl is Rogue
                if ChrB == "Kitty" and R_LikeKitty <= Check: 
                        $ R_LikeKitty += Modifier if Auto else 0
                        $ Likes = R_LikeKitty
                        if "dating" in R_Traits or "Rogue" in P_Harem:
                            if "Kitty" not in P_Harem and "poly Kitty" not in R_Traits:
                                $ Jealousy = 100
                elif ChrB == "Emma" and R_LikeEmma <= Check:   
                        $ R_LikeEmma += Modifier if Auto else 0
                        $ Likes = R_LikeEmma
                        if "dating" in R_Traits or "Rogue" in P_Harem:
                            if "Emma" not in P_Harem and "poly Emma" not in R_Traits:
                                $ Jealousy = 100
                elif ChrB == "Laura" and R_LikeLaura <= Check:  
                        $ R_LikeLaura += Modifier if Auto else 0 
                        $ Likes = R_LikeLaura
                        if "dating" in R_Traits or "Rogue" in P_Harem:
                            if "Laura" not in P_Harem and "poly Laura" not in R_Traits:
                                $ Jealousy = 100
                if False:
                    #test this, should fairly replace above system
                    $ Likes = GirlLikeCheck(ChrA,ChrB) #ie R_LikeKitty
                    if CheckWord(ChrA,"Traits","dating") or ChrA in P_Harem: 
                            #if "dating" in R_Traits or "Rogue" in P_Harem:
                            if ChrB not in P_Harem and not CheckWord(ChrA,"Traits","poly " + ChrB): 
                                    #if "Kitty" not in P_Harem and "poly Kitty" not in R_Traits:
                                    $ Jealousy = 100
                                
        elif ChrA == "Kitty":                                             
                #If the first girl is Kitty
                if ChrB == "Rogue" and K_LikeRogue <= Check: 
                        $ K_LikeRogue += Modifier if Auto else 0
                        $ Likes = K_LikeRogue
                        if "dating" in K_Traits or "Kitty" in P_Harem:
                            if "Rogue" not in P_Harem and "poly Rogue" not in K_Traits:
                                $ Jealousy = 100
                elif ChrB == "Emma" and K_LikeEmma <= Check:   
                        $ K_LikeEmma += Modifier if Auto else 0
                        $ Likes = K_LikeEmma
                        if "dating" in K_Traits or "Kitty" in P_Harem:
                            if "Emma" not in P_Harem and "poly Emma" not in K_Traits:
                                $ Jealousy = 100
                elif ChrB == "Laura" and K_LikeLaura <= Check:  
                        $ K_LikeLaura += Modifier if Auto else 0 
                        $ Likes = K_LikeLaura
                        if "dating" in K_Traits or "Kitty" in P_Harem:
                            if "Laura" not in P_Harem and "poly Laura" not in K_Traits:
                                $ Jealousy = 100
        elif ChrA == "Emma":                                             
                #If the first girl is Emma
                if ChrB == "Rogue" and E_LikeRogue <= Check:   
                        $ E_LikeRogue += Modifier if Auto else 0
                        $ Likes = E_LikeRogue
                        if "dating" in E_Traits or "Emma" in P_Harem:
                            if "Rogue" not in P_Harem and "poly Rogue" not in E_Traits:
                                $ Jealousy = 100
                elif ChrB == "Kitty" and E_LikeKitty <= Check: 
                        $ E_LikeKitty += Modifier if Auto else 0
                        $ Likes = E_LikeKitty
                        if "dating" in E_Traits or "Emma" in P_Harem:
                            if "Kitty" not in P_Harem and "poly Kitty" not in E_Traits:
                                $ Jealousy = 100
                elif ChrB == "Laura" and E_LikeLaura <= Check:  
                        $ E_LikeLaura += Modifier if Auto else 0 
                        $ Likes = E_LikeLaura
                        if "dating" in E_Traits or "Emma" in P_Harem:
                            if "Laura" not in P_Harem and "poly Laura" not in E_Traits:
                                $ Jealousy = 100
        elif ChrA == "Laura":                                             
                #If the first girl is Laura
                if ChrB == "Rogue" and L_LikeRogue <= Check:  
                        $ L_LikeRogue += Modifier if Auto else 0 
                        $ Likes = L_LikeRogue
                        if "dating" in L_Traits or "Laura" in P_Harem:
                            if "Rogue" not in P_Harem and "poly Rogue" not in L_Traits:
                                $ Jealousy = 100
                elif ChrB == "Kitty" and L_LikeKitty <= Check: 
                        $ L_LikeKitty += Modifier if Auto else 0
                        $ Likes = L_LikeKitty
                        if "dating" in L_Traits or "Laura" in P_Harem:
                            if "Kitty" not in P_Harem and "poly Kitty" not in L_Traits:
                                $ Jealousy = 100
                elif ChrB == "Emma" and L_LikeEmma <= Check:   
                        $ L_LikeEmma += Modifier if Auto else 0
                        $ Likes = L_LikeEmma
                        if "dating" in L_Traits or "Laura" in P_Harem:
                            if "Emma" not in P_Harem and "poly Emma" not in L_Traits:
                                $ Jealousy = 100
        #end start-up, returns by now if on Auto
        
        if Auto: #this is a quick return, 
                call Statup(ChrA, "Lust", 200, (int(Modifier/5)))
                return        
                        
        #this is for more nuanced comparisons  
        if ChrA == "Rogue": 
                    #Establishes how jealous Rogue is likely to get
                    $ Jealousy += (R_Love - 600) if R_Love > 600 else 0              
                            #How much her Love stat is over 600, +0-400                                        
                    $ Jealousy += R_SEXP if R_Inbt <= 500 else 0  
                            #plus her SexP rating if she has low inhibitions, +0-200                      
                    $ Jealousy -= (R_Obed - 250) if R_Obed > 250 else 0             
                            #minus how much her Obed stat is over 250, -0-750                                                                                    
                            # = result of up to 700 if high love, dating, and low obedience
        if ChrA == "Kitty": 
                    $ Jealousy += (K_Love - 600) if K_Love > 600 else 0                                     
                    $ Jealousy += K_SEXP if K_Inbt <= 500 else 0                      
                    $ Jealousy -= (K_Obed - 250) if K_Obed > 250 else 0                           
        if ChrA == "Emma": 
                    $ Jealousy += (E_Love - 600) if E_Love > 600 else 0                                    
                    $ Jealousy += E_SEXP if E_Inbt <= 500 else 0                      
                    $ Jealousy -= (E_Obed - 250) if E_Obed > 250 else 0                       
        if ChrA == "Laura": 
                    $ Jealousy += (L_Love - 600) if L_Love > 600 else 0                                    
                    $ Jealousy += L_SEXP if L_Inbt <= 500 else 0                       
                    $ Jealousy -= (L_Obed - 250) if L_Obed > 250 else 0
                    
        $ Jealousy = 0 if Jealousy < 1 else Jealousy                    
            #Balances it to no less than zero                    
        $ Modifier += 1 if not Jealousy and Likes >= 500 else 0   
            #+ modifier if she doesn't hate Kitty but has no jealousy left
                    
        if Likes >= 900:          
                    #If she really likes the girl, then she is turned on, likes both of you more. 
                    $ Likes += Modifier
                    call Statup(ChrA, "Love", 80, (int(Modifier/2)))
                    call Statup(ChrA, "Lust", 200, (int(Modifier/5)))
                    $ Ok = 2
        
        elif Likes >= 800:        
                #If she mostly likes the girl, and is not super jealous, she likes you both more. 
                if Jealousy <= 300:
                    $ Likes += Modifier
                    call Statup(ChrA, "Love", 80, (int(Modifier/2)))
                    call Statup(ChrA, "Lust", 200, (int(Modifier/2)))
                    $ Ok = 2
                else:
                    $ Likes -= Modifier                        
                    call Statup(ChrA, "Lust", 200, (int(Modifier/5)))
                    $ Ok = 1
                
        elif Likes >= 600:        
                #If she's friends with the girl, only low jealousy is positive
                if Jealousy <= 100:
                    $ Likes += Modifier                        
                    call Statup(ChrA, "Love", 80, (int(Modifier/4)))                        
                    call Statup(ChrA, "Lust", 200, (int(Modifier/2)))
                    $ Ok = 2
                elif Jealousy <= 300:
                    $ Likes -= Modifier
                    call Statup(ChrA, "Lust", 200, (int(Modifier/2)))
                    $ Ok = 1
                else:
                    $ Likes -= (Modifier + (int(Jealousy/50)))
                    call Statup(ChrA, "Love", 80, (-(int(Modifier)))) 
                    call Statup(ChrA, "Lust", 200, (int(Modifier/5)))

        elif Likes >= 400:       
                #If she is neutral to the girl, it's all negative                 
                if Jealousy <= 100:
                    $ Likes -= Modifier
                    $ Ok = 1
                else:
                    $ Likes -= (Modifier + (int(Jealousy/100)))
                call Statup(ChrA, "Lust", 200, (int(Modifier/10)))            
        else:                           
                #If she hates the girl, it's all very negative
                $ Likes -= (Modifier + (int(Jealousy/50)))
                call Statup(ChrA, "Lust", 200, (int(Modifier/10))) 

        call Statup(ChrA, "Inbt", 60, (int(Modifier/10)))                                                                         
        #drops through to the final return                                                                     
        #end Jealousy
        #end nuanced checks
        
        # restores "likes" to target character. 
        if ChrA == "Rogue":               
                if ChrB == "Kitty":   
                    $ R_LikeKitty = Likes
                elif ChrB == "Emma":   
                    $ R_LikeEmma = Likes
                elif ChrB == "Laura":   
                    $ R_LikeLaura = Likes
        elif ChrA == "Kitty":               
                if ChrB == "Rogue":   
                    $ K_LikeRogue = Likes
                elif ChrB == "Emma":   
                    $ K_LikeEmma = Likes
                elif ChrB == "Laura":   
                    $ K_LikeLaura = Likes
        elif ChrA == "Emma":     
                if ChrB == "Rogue":   
                    $ E_LikeRogue = Likes          
                elif ChrB == "Kitty":   
                    $ E_LikeKitty = Likes
                elif ChrB == "Laura":   
                    $ E_LikeLaura = Likes
        elif ChrA == "Laura":               
                if ChrB == "Rogue":   
                    $ L_LikeRogue = Likes
                elif ChrB == "Kitty":   
                    $ L_LikeKitty = Likes
                elif ChrB == "Emma":   
                    $ L_LikeEmma = Likes
                                
        return Ok
        # returns 2 if very into it, 1 if ok with it, 0 if not cool with it.

label GirlWaitAttract(Local=0,Check=70,D20=0,Teach=0):
    #call GirlWaitAttract(1,5)
    #This adjusts girl's liking each other based on shared activities
    #Local =1 only checks if they are in the room with you.
    #it goes R+K, R+E, R+L, K+E, K+L, E+L, etc. 
    
    $ D20 = renpy.random.randint(0,1) if not D20 else D20
    
    if E_Loc == "bg teacher":
        $ E_Loc = "bg classroom" #Sets Emma to being in class if she's teaching
        $ Teach = 1
        
    if R_Loc == K_Loc:            
            #This adjusts how much Rogue and Kitty like each other if they are in the same room
            if not Local or R_Loc == bg_current:
                #if they are elsewhere
                if R_Loc == "bg classroom":
                        $ R_LikeKitty += 1 if R_LikeKitty <= 70 else 0
                        $ K_LikeRogue += 1 if K_LikeRogue <= 70 else 0
                elif R_Loc == "bg dangerroom":
                        $ R_LikeKitty += (1+D20) if R_LikeKitty <= 70 else 0
                        $ K_LikeRogue += (1+D20) if K_LikeRogue <= 70 else 0
                elif R_Loc == "bg showerroom":  
                        $ R_LikeKitty += 2 if R_LikeKitty <= 90 else 0 
                        $ K_LikeRogue += 2 if K_LikeRogue <= 90 else 0
                else:
                        $ R_LikeKitty += D20 if R_LikeKitty <= Check else 0 
                        $ K_LikeRogue += D20 if K_LikeRogue <= Check else 0
                        
                $ R_LikeKitty += (int(K_Shame/5)) if R_LikeKitty >= Check else 0 #Rogue likes Kitty based on how slutty Kitty looks
                $ K_LikeRogue += (int(R_Shame/5)) if K_LikeRogue >= Check else 0 #Kitty likes Rogue based on how slutty Rogue looks 
    if R_Loc == E_Loc:   
            #This adjusts how much Rogue and Emma like each other if they are in the same room    
            if not Local or R_Loc == bg_current:    
                if R_Loc == "bg classroom":
                        $ R_LikeEmma += 1 if R_LikeEmma <= 70 else 0
                        $ E_LikeRogue += 1 if E_LikeRogue <= 70 else 0
                elif R_Loc == "bg dangerroom":
                        $ R_LikeEmma += (1+D20) if R_LikeEmma <= 70 else 0
                        $ E_LikeRogue += (1+D20) if E_LikeRogue <= 70 else 0
                elif R_Loc == "bg showerroom":  
                        $ R_LikeEmma += 2 if R_LikeEmma <= 90 else 0 
                        $ E_LikeRogue += 3 if E_LikeRogue <= 90 else 0
                else:
                        $ R_LikeEmma += D20 if R_LikeEmma <= Check else 0 
                        $ E_LikeRogue += D20 if E_LikeRogue <= Check else 0
                        
                $ R_LikeEmma += (int(E_Shame/5)) if R_LikeEmma >= Check else 0 #Rogue likes Emma based on how slutty Emma looks
                $ E_LikeRogue += (int(R_Shame/4)) if E_LikeRogue >= Check else 0 #Emma likes Rogue based on how slutty Rogue looks                       
    if R_Loc == L_Loc:            
            #This adjusts how much Rogue and Laura like each other if they are in the same room 
            if not Local or R_Loc == bg_current:
                if R_Loc == "bg classroom":
                        $ R_LikeLaura += 1 if R_LikeLaura <= 70 else 0
                        $ L_LikeRogue += 1 if L_LikeRogue <= 70 else 0
                elif R_Loc == "bg dangerroom":
                        $ R_LikeLaura += (1+D20) if R_LikeLaura <= 70 else 0
                        $ L_LikeRogue += (1+D20) if L_LikeRogue <= 70 else 0
                elif R_Loc == "bg showerroom":  
                        $ R_LikeLaura += 2 if R_LikeLaura <= 90 else 0 
                        $ L_LikeRogue += 2 if L_LikeRogue <= 90 else 0
                else:
                        $ R_LikeLaura += D20 if R_LikeLaura <= Check else 0 
                        $ L_LikeRogue += D20 if L_LikeRogue <= Check else 0
                        
                $ R_LikeLaura += (int(L_Shame/5)) if R_LikeLaura >= Check else 0 #Rogue likes Laura based on how slutty Laura looks
                $ L_LikeRogue += (int(R_Shame/5)) if L_LikeRogue >= Check else 0 #Laura likes Rogue based on how slutty Rogue looks                 
    #end Rogue checks
    
    if K_Loc == E_Loc:  
            #this adjusts how much Kitty and Emma like each other if they are in the same room 
            if not Local or K_Loc == bg_current:
                if K_Loc == "bg classroom":
                        $ K_LikeEmma += 1 if K_LikeEmma <= 70 else 0
                        $ E_LikeKitty += 1 if E_LikeKitty <= 70 else 0
                elif K_Loc == "bg dangerroom":
                        $ K_LikeEmma += (1+D20) if K_LikeEmma <= 70 else 0
                        $ E_LikeKitty += (1+D20) if E_LikeKitty <= 70 else 0
                elif K_Loc == "bg showerroom":  
                        $ K_LikeEmma += 2 if K_LikeEmma <= 90 else 0 
                        $ E_LikeKitty += 3 if E_LikeKitty <= 90 else 0
                else:
                        $ K_LikeEmma += D20 if K_LikeEmma <= Check else 0 
                        $ E_LikeKitty += D20 if E_LikeKitty <= Check else 0
                        
                $ K_LikeEmma += (int(E_Shame/5)) if K_LikeEmma >= Check else 0 #Kitty likes Emma based on how slutty Emma looks
                $ E_LikeKitty += (int(K_Shame/4)) if E_LikeKitty >= Check else 0 #Emma likes Kitty based on how slutty Kitty looks
    if K_Loc == L_Loc:            
            #This adjusts how much Kitty and Laura like each other if they are in the same room 
            if not Local or K_Loc == bg_current:
                if K_Loc == "bg classroom":
                        $ K_LikeLaura += 1 if K_LikeLaura <= 70 else 0
                        $ L_LikeKitty += 1 if L_LikeKitty <= 70 else 0
                elif K_Loc == "bg dangerroom":
                        $ K_LikeLaura += (1+D20) if K_LikeLaura <= 70 else 0
                        $ L_LikeKitty += (1+D20) if L_LikeKitty <= 70 else 0
                elif K_Loc == "bg showerroom":  
                        $ K_LikeLaura += 2 if K_LikeLaura <= 90 else 0 
                        $ L_LikeKitty += 2 if L_LikeKitty <= 90 else 0
                else:
                        $ K_LikeLaura += D20 if K_LikeLaura <= Check else 0 
                        $ L_LikeKitty += D20 if L_LikeKitty <= Check else 0
                        
                $ K_LikeLaura += (int(L_Shame/5)) if K_LikeLaura >= Check else 0 #Kitty likes Laura based on how slutty Laura looks
                $ L_LikeKitty += (int(K_Shame/5)) if L_LikeKitty >= Check else 0 #Laura likes Kitty based on how slutty Kitty looks                 
    #end Kitty checks
    
    if E_Loc == L_Loc:   
            #This adjusts how much Emma and Laura like each other if they are in the same room    
            if not Local or E_Loc == bg_current:    
                if E_Loc == "bg classroom":
                        $ E_LikeLaura += 1 if E_LikeLaura <= 70 else 0
                        $ L_LikeEmma += 1 if L_LikeEmma <= 70 else 0
                elif E_Loc == "bg dangerroom":
                        $ E_LikeLaura += (1+D20) if E_LikeLaura <= 70 else 0
                        $ L_LikeEmma += (1+D20) if L_LikeEmma <= 70 else 0
                elif E_Loc == "bg showerroom":  
                        $ E_LikeLaura += 2 if E_LikeLaura <= 90 else 0 
                        $ L_LikeEmma += 3 if L_LikeEmma <= 90 else 0
                else:
                        $ E_LikeLaura += D20 if E_LikeLaura <= Check else 0 
                        $ L_LikeEmma += D20 if L_LikeEmma <= Check else 0
                        
                $ E_LikeLaura += (int(L_Shame/5)) if E_LikeLaura >= Check else 0 #Emma likes Laura based on how slutty Laura looks
                $ L_LikeEmma += (int(E_Shame/4)) if L_LikeEmma >= Check else 0 #Laura likes Emma based on how slutty Emma looks                       
    #end Emma checks
    
    if Teach:
            $ E_Loc = "bg teacher" #Sets Emma to being a teacher again        
    return
    
label Faces(Character="All"):
    #This sets a default face for the girl
    if Character == "Rogue" or Character == "All":
            if R_Lust >= 50 and ApprovalCheck("Rogue", 1200):
                    $ R_Emote = "sexy"           
            elif R_Addict > 75:
                    $ R_Emote = "manic"
            elif R_Love >= R_Obed and R_Love >= 500:
                    $ R_Emote = "smile"      
            elif R_Inbt >= R_Obed and R_Inbt >= 500:
                    $ R_Emote = "smile"      
            elif R_Addict > 50:
                    $ R_Emote = "manic"
            elif (R_Love + R_Obed) < 300:
                    $ R_Emote = "angry"
            else:
                    $ R_Emote = "normal"
            call RogueFace    
    
    if Character == "Kitty" or Character == "All":
            if K_Lust >= 50 and ApprovalCheck("Kitty", 1200):
                    $ K_Emote = "sexy"           
            elif K_Addict > 75:
                    $ K_Emote = "manic"
            elif K_Love >= K_Obed and K_Love >= 500:
                    $ K_Emote = "smile"      
            elif K_Inbt >= K_Obed and K_Inbt >= 500:
                    $ K_Emote = "smile"      
            elif K_Addict > 50:
                    $ K_Emote = "manic"
            elif (K_Love + K_Obed) < 300:
                    $ K_Emote = "angry"
            else:
                    $ K_Emote = "normal"
            call KittyFace   
            
    if Character == "Emma" or Character == "All":
            if E_Lust >= 50 and ApprovalCheck("Emma", 1000):
                    $ E_Emote = "sexy"           
            elif E_Addict > 75:
                    $ E_Emote = "manic"
            elif E_Love >= E_Obed and E_Love >= 500:
                    $ E_Emote = "smile"      
            elif E_Inbt >= E_Obed and E_Inbt >= 500:
                    $ E_Emote = "smile"      
            elif E_Addict > 50:
                    $ E_Emote = "manic"
            elif (E_Love + E_Obed) < 300:
                    $ E_Emote = "angry"
            else:
                    $ E_Emote = "normal"
            call EmmaFace 
            
    if Character == "Laura" or Character == "All":
            if L_Lust >= 50 and ApprovalCheck("Laura", 1000):
                    $ L_Emote = "sexy"           
            elif L_Addict > 75:
                    $ L_Emote = "manic"
            elif L_Love >= L_Obed and L_Love >= 500:
                    $ L_Emote = "smile"      
            elif L_Inbt >= L_Obed and L_Inbt >= 500:
                    $ L_Emote = "smile"      
            elif L_Addict > 50:
                    $ L_Emote = "manic"
            elif (L_Love + L_Obed) < 300:
                    $ L_Emote = "angry"
            else:
                    $ L_Emote = "normal"
            call EmmaFace   
    return


label Activity_Check(Girl=0,Girl2=0,Silent=0,Removal=1,ClothesCheck=1,Mod=0,Approval=1,Tempshame=0,TabooM=1):
        # This checks whether a girl is up for watching a given activity
        # Silent is whether it plays dialog or not, Removal is whether it auto-removes the girl on a fail,
        # ClothesCheck is whether it bothers checking clothing, 2 if skip first girl
        # Mod gets set to her Like stat -600, so 600 Like, you break even, otherwise it's a penalty
        # call Activity_Check("Rogue",0,1,0)
              
        if Girl == Girl2:
            "Tell oni that the activity check failed after [Trigger]."
            
        #if they don't know you're there, they don't run
        if Girl == "Rogue" and "unseen" in R_RecentActions:
                    return 2  
        elif Girl == "Kitty" and "unseen" in K_RecentActions:
                    return 2
        elif Girl == "Emma" and ("unseen" in E_RecentActions or "classcaught" in E_RecentActions):
                    return 2 
        elif Girl == "Laura" and "unseen" in L_RecentActions:
                    return 2
                
        if Girl == "Rogue":
                $ Mod += 200 if R_Forced else 0             #bonus if in the Forced state
                $ Mod += (R_Lust*5) if R_Lust >= 50 else 0  #bonus if high lust (50 = +250, 75= +375, 90 = +450)
                
        elif Girl == "Kitty":
                $ Mod += 200 if K_Forced else 0
                $ Mod += (K_Lust*5) if K_Lust >= 50 else 0
        elif Girl == "Emma":     
                $ Mod += 200 if E_Forced else 0
                $ Mod += (E_Lust*5) if E_Lust >= 50 else 0
        elif Girl == "Laura":
                $ Mod += 200 if L_Forced else 0
                $ Mod += (L_Lust*5) if L_Lust >= 50 else 0
            
        if Girl2 and ClothesCheck != 2:
                #if there is a second girl and it's not told to skip it
                $ Mod = int(Mod/2) if Mod > 0 else Mod 
                #halves the benefits from the above mechanisms
                $ Mod = (GirlLikeCheck(Girl,Girl2)-600)
                # if 500 = -100, if 700 = +100 if 900 = +300
                if Girl in P_Harem and Girl2 in P_Harem: #bonus for if both in harem
                        $ Mod += 500
                    
        if ClothesCheck and Girl2:
                if Girl2 == "Rogue":
                        #sets her shame level to be accurate to current look
                        call Rogue_OutfitShame(20)
                        $ Tempshame = R_Shame
                elif Girl2 == "Kitty":
                        call Kitty_OutfitShame(20)
                        $ Tempshame = K_Shame
                elif Girl2 == "Emma":
                        call Emma_OutfitShame(20)
                        $ Tempshame = E_Shame
                elif Girl2 == "Laura":
                        call Laura_OutfitShame(20)
                        $ Tempshame = L_Shame
                
                if Tempshame <= 15 and (ApprovalCheck(Girl, 600,Bonus=Mod) or ApprovalCheck(Girl, 350, "I")):
                        #If the outfit is hot but she's ok     
                        if ApprovalCheck(Girl, 900,Bonus=Mod) or ApprovalCheck(Girl, 450, "I"): 
                                $ Approval = 2   
                elif Tempshame <= 20 and (ApprovalCheck(Girl, 900,Bonus=Mod) or ApprovalCheck(Girl, 450, "I")):
                        #If the outfit is sexy but she's cool with that 
                        if ApprovalCheck(Girl, 1100,Bonus=Mod) or ApprovalCheck(Girl, 550, "I"): 
                                $ Approval = 2   
                elif Tempshame <= 25 and (ApprovalCheck(Girl, 1100,Bonus=Mod) or ApprovalCheck(Girl, 550, "I")):
                        #If the outfit is sexy but she's cool with that
                        if ApprovalCheck(Girl, 1400,Bonus=Mod) or ApprovalCheck(Girl, 650, "I"): 
                                $ Approval = 2    
                elif (ApprovalCheck(Girl, 1400,Bonus=Mod) or ApprovalCheck(Girl, 650, "I")):
                        #If the outfit is very scandelous but she's ok with that     
                        if ApprovalCheck(Girl, 1600,Bonus=Mod) or ApprovalCheck(Girl, 850, "I"): 
                                $ Approval = 2     
                        pass
                else:
                        $ Approval = 0
        
        
        if CheckWord(Girl,"Traits","exhibitionist")or ApprovalCheck(Girl,900,"I"):
                #this negates or reduces the taboo modifier if they are slutty
                $ TabooM = 0 
        elif ApprovalCheck(Girl,50,"X") or ApprovalCheck(Girl,800,"I"):
                $ TabooM = .5
                 
        if not Approval:
                    # If it fails the clothing check, skip the next part
                    pass
        elif Trigger == "strip" and Trigger2 != "jackin":
                    pass #covered by the above check
        elif not Trigger:
                    pass
        elif Trigger == "lick ass":
                    $ Approval = ApprovalCheck(Girl,1550,Bonus=Mod, TabM = (TabooM* 3 ))
        elif Trigger == "anal":
                    $ Approval = ApprovalCheck(Girl,1550,Bonus=Mod, TabM = (TabooM* 3 ))
        elif Trigger == "sex":
                    $ Approval = ApprovalCheck(Girl,1400,Bonus=Mod, TabM = (TabooM* 3 ))
        elif Trigger == "lick pussy":            
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = (TabooM* 2 ))
        elif Trigger2 == "jackin":            
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = (TabooM* 2 ))
        elif Trigger == "blow":            
                    $ Approval = ApprovalCheck(Girl,1300,Bonus=Mod, TabM = (TabooM* 2 ))
        elif Trigger == "titjob":              
                    $ Approval = ApprovalCheck(Girl,1200,Bonus=Mod, TabM = (TabooM* 3 ))
        elif Trigger == "hotdog":
                    $ Approval = ApprovalCheck(Girl,1000,Bonus=Mod, TabM = (TabooM* 3 ))                
        elif Trigger == "hand" or Trigger3 == "hand":              
                    $ Approval = ApprovalCheck(Girl,1100,Bonus=Mod, TabM = (TabooM* 2 ))
        elif Trigger == "foot":
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = (TabooM* 2 ))  
        elif Trigger == "dildo anal":
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = (TabooM* 2 ))
        elif Trigger == "dildo pussy":
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = (TabooM* 2 ))
        elif Trigger == "insert ass":
                    $ Approval = ApprovalCheck(Girl,1300,Bonus=Mod, TabM = (TabooM* 2 ))
        elif Trigger == "fondle pussy" or Trigger == "insert pussy":
                    $ Approval = ApprovalCheck(Girl,1050,Bonus=Mod, TabM = (TabooM* 2 ))
        elif Trigger == "suck breasts":            
                    $ Approval = ApprovalCheck(Girl,1050,Bonus=Mod, TabM = (TabooM* 3 ))
        elif Trigger == "fondle breasts":                        
                    $ Approval = ApprovalCheck(Girl,950,Bonus=Mod, TabM = (TabooM* 2 ))
        elif Trigger == "fondle ass":
                    $ Approval = ApprovalCheck(Girl,850,Bonus=Mod, TabM = (TabooM* 1 ))
                    
        elif Trigger == "masturbation": 
                    $ Approval = ApprovalCheck(Girl,1200,Bonus=Mod, TabM = (TabooM* 2 ))
                    
        elif Trigger == "kiss you":
                    $ Approval = ApprovalCheck(Girl,500,Bonus=Mod, TabM = 0)                    
        elif Trigger == "fondle thighs":
                    $ Approval = ApprovalCheck(Girl,750,Bonus=Mod, TabM = 0)
                    
        elif Trigger == "lesbian": 
                    $ Approval = ApprovalCheck(Girl,1350,Bonus=Mod, TabM = (TabooM* 2 ))                           
        
        #Threesomecheck
        if not Approval:
                    # If it fails the primary trigger check, skip the next part
                    pass
        elif not Trigger4:
                    pass
        elif Trigger4 == "lick ass":
                    $ Approval = ApprovalCheck(Girl,1750,Bonus=(Mod+200), TabM = (TabooM* 3 ))
        elif Trigger4 == "lick pussy":            
                    $ Approval = ApprovalCheck(Girl,1450,Bonus=(Mod+200), TabM = (TabooM* 2 ))
        elif Trigger4 == "blow":            
                    $ Approval = ApprovalCheck(Girl,1300,Bonus=(Mod+200), TabM = (TabooM* 2 ))           
        elif Trigger4 == "hand":              
                    $ Approval = ApprovalCheck(Girl,1200,Bonus=(Mod+200), TabM = (TabooM* 2 ))
        elif Trigger4 == "insert ass":
                    $ Approval = ApprovalCheck(Girl,1500,Bonus=(Mod+200), TabM = (TabooM* 2 ))
        elif Trigger4 == "fondle pussy":
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=(Mod+200), TabM = (TabooM* 2 ))
        elif Trigger4 == "suck breasts":            
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=(Mod+200), TabM = (TabooM* 3 ))
        elif Trigger4 == "fondle breasts":                        
                    $ Approval = ApprovalCheck(Girl,1150,Bonus=(Mod+200), TabM = (TabooM* 2 ))                  
        elif Trigger4 == "kiss girl":
                    $ Approval = ApprovalCheck(Girl,1050,Bonus=(Mod+200), TabM = 0)                 
        elif Trigger4 == "kiss both":
                    $ Approval = ApprovalCheck(Girl,1050,Bonus=(Mod+200), TabM = 0)  
        elif Trigger4 == "fondle ass":
                    $ Approval = ApprovalCheck(Girl,1050,Bonus=(Mod+200), TabM = (TabooM* 1 ))                    
        elif Trigger4 == "masturbation": 
                    $ Approval = ApprovalCheck(Girl,1400,Bonus=(Mod+200), TabM = (TabooM* 2 ))                   
        elif Trigger4 == "watch":
                    $ Approval = ApprovalCheck(Girl,1000,Bonus=(Mod+200), TabM = 0)                    
        elif Trigger4 == "kiss you":
                    $ Approval = ApprovalCheck(Girl,600,Bonus=Mod, TabM = 0)    
                        
        if not Silent and not Approval:
            call AnyFace(Girl,"sadside",1)
            if Girl == "Rogue":
                    if Girl2:
                        ch_r "I don't know, with [Girl2] here and all."
                    ch_r "Ain't none a this right, [R_Petname]."
            elif Girl == "Kitty":
                    if Girl2:
                        ch_k "I don't know, with [Girl2] being here."
                    ch_k "I'm[K_like]not really comfortable with this?"
            elif Girl == "Emma":
                    if Girl2:
                        ch_e "I'm unsure that I'm comfortable doing this with [Girl2] here."
                    ch_e "This has become a bit too. . . scandalous for my tastes."
            elif Girl == "Laura":
                    if Girl2:
                        ch_l "[Girl2]'s weirding me out."
                    else:
                        ch_l "This is getting weird."
                    ch_l "I'll see you later."
        
        if Removal and not Approval:
                call Remove_Girl(Girl,2)  
                "[Girl] takes off."
                
        return Approval

label DrainWord(Character = "Rogue", Word = "word", Recent = 1, Daily = 1, Traits=0):
            # to remove words from the daily/recent lists , ie call DrainWord("Rogue","sex",1,0)
            if Character == "Rogue" or Character == "All":
                            if Traits and Word in R_Traits:
                                while Word in R_Traits:
                                        $ R_Traits.remove(Word) 
                            if Word in R_RecentActions and Recent:
                                while Word in R_RecentActions:
                                        $ R_RecentActions.remove(Word) 
                            if Word in R_DailyActions and Daily:
                                while Word in R_DailyActions:
                                        $ R_DailyActions.remove(Word)   
            if Character == "Kitty" or Character == "All":
                            if Traits and Word in K_Traits:
                                while Word in K_Traits:
                                        $ K_Traits.remove(Word) 
                            if Word in K_RecentActions and Recent:
                                while Word in K_RecentActions:
                                        $ K_RecentActions.remove(Word) 
                            if Word in K_DailyActions and Daily:
                                while Word in K_DailyActions:
                                        $ K_DailyActions.remove(Word) 
            if Character == "Emma" or Character == "All":
                            if Traits and Word in E_Traits:
                                while Word in E_Traits:
                                        $ E_Traits.remove(Word) 
                            if Word in E_RecentActions and Recent:
                                while Word in E_RecentActions:
                                        $ E_RecentActions.remove(Word) 
                            if Word in E_DailyActions and Daily:
                                while Word in E_DailyActions:
                                        $ E_DailyActions.remove(Word) 
            if Character == "Laura" or Character == "All":
                            if Traits and Word in L_Traits:
                                while Word in L_Traits:
                                        $ L_Traits.remove(Word) 
                            if Word in L_RecentActions and Recent:
                                while Word in L_RecentActions:
                                        $ L_RecentActions.remove(Word) 
                            if Word in L_DailyActions and Daily:
                                while Word in L_DailyActions:
                                        $ L_DailyActions.remove(Word) 
            if Character == "Player":
                            if Word in P_RecentActions and Recent:
                                while Word in P_RecentActions:
                                        $ P_RecentActions.remove(Word) 
                            if Word in P_DailyActions and Daily:
                                while Word in P_DailyActions:
                                        $ P_DailyActions.remove(Word)    
            return

label AnyWord(Girl=0,Only=0,Recent=0,Daily=0,Trait=0,History=0):
            #applies variables to appropriate character stats
            # call AnyWord(Girl,1,0,0,0,0)
            #if Only, then only apply it if it's not already there
            if Girl == "Rogue":
                    if (Recent and not Only) or (Recent and Recent not in R_RecentActions):
                            $ R_RecentActions.append(Recent)
                    if (Daily and not Only) or (Daily and Daily not in R_DailyActions):
                            $ R_DailyActions.append(Daily)
                    if (Trait and not Only) or (Trait and Trait not in R_Traits):
                            $ R_Traits.append(Trait)
                    if (History and not Only) or (History and History not in R_History):
                            $ R_History.append(History)
            elif Girl == "Kitty":
                    if (Recent and not Only) or (Recent and Recent not in K_RecentActions):
                            $ K_RecentActions.append(Recent)
                    if (Daily and not Only) or (Daily and Daily not in K_DailyActions):
                            $ K_DailyActions.append(Daily)
                    if (Trait and not Only) or (Trait and Trait not in K_Traits):
                            $ K_Traits.append(Trait)
                    if (History and not Only) or (History and History not in K_History):
                            $ K_History.append(History)
            elif Girl == "Emma":
                    if (Recent and not Only) or (Recent and Recent not in E_RecentActions):
                            $ E_RecentActions.append(Recent)
                    if (Daily and not Only) or (Daily and Daily not in E_DailyActions):
                            $ E_DailyActions.append(Daily)
                    if (Trait and not Only) or (Trait and Trait not in E_Traits):
                            $ E_Traits.append(Trait)
                    if (History and not Only) or (History and History not in E_History):
                            $ E_History.append(History)
            elif Girl == "Laura":
                    if (Recent and not Only) or (Recent and Recent not in L_RecentActions):
                            $ L_RecentActions.append(Recent)
                    if (Daily and not Only) or (Daily and Daily not in L_DailyActions):
                            $ L_DailyActions.append(Daily)
                    if (Trait and not Only) or (Trait and Trait not in L_Traits):
                            $ L_Traits.append(Trait)
                    if (History and not Only) or (History and History not in L_History):
                            $ L_History.append(History)
            return
            
#End AnyWord / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#This is intended to clear the room of non-essential characters
#the named character is the one who stays, everyone else is kicked out.
label CleartheRoom(Character = 0, Passive = 0, Silent = 0, Check = 0, Girls=[]):
            #Character is the one asking to clear the room. 
            #Passive is when the second person leaves on their own. 
            #Silent removes dialog
            # Check only checks to see if anyone is there. It will start at 1 and raise with each girl
            
            #this populates a list of other girls at the current location
            if Character != "Rogue" and (R_Loc == bg_current or "Rogue" in Party):
                    $ Girls.append("Rogue")
            if Character != "Kitty" and (K_Loc == bg_current or "Kitty" in Party):   
                    $ Girls.append("Kitty")
            if Character != "Emma" and (E_Loc == bg_current or "Emma" in Party or (E_Loc == "bg teacher" and bg_current == "bg classroom")):         
                    $ Girls.append("Emma")
            if Character != "Laura" and (L_Loc == bg_current or "Laura" in Party):    
                    $ Girls.append("Laura") 
                    
            if Check:                
                    return len(Girls) #test this, hope it works. . .
                            
            $ Nearby = [] #empties the nearby list
            
            if not Silent and not Passive:
                    #this section asks a question that a later phase will answer                                        
                    if Character == "Rogue":
                            # if the clearing character is Rogue
                            if R_Loc != bg_current:
                                "Rogue enters the room."
                                $ R_Loc = bg_current
                                
                            if len(Girls) > 1:
                                #if there is at least two other girls. . .
                                ch_r "Ladies, could I talk to [Playername] alone for a minute?"
                            elif Girls:
                                #if there is at least one other girl. . .
                                ch_r "[Girls[0]], could I talk to [Playername] alone for a minute?"
                            else:
                                #if there is no other girl. . .
                                return
                    elif Character == "Kitty":
                            if K_Loc != bg_current:
                                "Kitty enters the room."
                                $ K_Loc = bg_current                                
                            if len(Girls) > 1:
                                ch_k "Girls, could I talk to [Playername] alone for a sec?" 
                            elif Girls:
                                ch_k "[Girls[0]]could I talk to [Playername] alone for a sec?" 
                            else:
                                return
                    elif Character == "Emma":
                            if E_Loc != bg_current:
                                "Emma enters the room."
                                $ E_Loc = bg_current                                
                            if len(Girls) > 1:
                                ch_e "Girls, would you mind if I had a word alone with [Playername]?"
                            elif Girls:
                                ch_e "[Girls[0]], would you mind if I had a word alone with [Playername]?"
                            else:
                                return
                    elif Character == "Laura":
                            if L_Loc != bg_current:
                                "Laura enters the room."
                                $ L_Loc = bg_current                                
                            if len(Girls) > 1:
                                ch_l "Hey, clear out, I need to talk with [Playername]."
                            elif Girls:
                                ch_l "[Girls[0]], clear out, I need to talk with [Playername]."
                            else:
                                return
            #end portion asking about each girl
                      
            if "Rogue" in Girls:  
                    #if the character asking is not Rogue, this removes Rogue from the room
                    if Silent:
                        pass
                    elif Passive:
                        ch_r "I should get going, see you later, [R_Petname]."  
                    elif Character != "All":
                        #if there are other girls. . .
                        ch_r "No problem, I'll see you later then." 
                    else:
                        ch_r "I should get going, see you later, [R_Petname]."                          
                      
                    if "Rogue" in Party:
                            $ Party.remove("Rogue")  
                    if "leaving" in R_RecentActions:
                            call DrainWord("Rogue","leaving")  
                    if "arriving" in R_RecentActions:
                            call DrainWord("Rogue","arriving") 
                    if bg_current == "bg rogue":
                            if Character != "All": #if it's not clearing all girls. . .
                                    #if the girl is not Rogue but you're in Rogue's room, the girl takes you to her room
                                    call TaketoRoom(Character)
                            else:
                                    $ R_Loc = "bg campus"
                    else:
                            $ R_Loc = "bg rogue"
                    hide Rogue with easeoutright 
            if "Kitty" in Girls:   
                    #if the character asking is not Kitty, this removes Kitty from the room
                    if Silent:
                        pass
                    elif Passive:
                        ch_k "I think I'll head out, I'll see you later."  
                    elif Character != "All":
                        ch_k "[K_Like]sure, I'll see you later."                                    
                    else:
                        ch_k "I think I'll head out, I'll see you later."  
                        
                    if "Kitty" in Party:
                            $ Party.remove("Kitty")  
                    if "leaving" in K_RecentActions:
                            call DrainWord("Kitty","leaving") 
                    if "arriving" in K_RecentActions:
                            call DrainWord("Kitty","arriving")  
                    if bg_current == "bg kitty":
                            if Character != "All": #if it's not clearing all girls. . .
                                    #if the girl is not Kitty but you're in Kitty's room, the girl takes you to her room
                                    call TaketoRoom(Character)
                            else:
                                    $ K_Loc = "bg campus"
                    else:
                            $ K_Loc = "bg kitty"    
                    hide Kitty_Sprite with easeoutbottom 
            if "Emma" in Girls:                               
                    #if the character asking is not Emma, this removes Emma from the room
                    if Silent:
                        pass
                    elif Passive:
                        ch_e "I think I should be going now."  
                    elif Character != "All":
                        ch_e "Fine, I'll see you later then."   
                    else:
                        ch_e "I think I should be going now."   
                        
                    if "Emma" in Party:
                            $ Party.remove("Emma")  
                    if "leaving" in E_RecentActions:
                            call DrainWord("Emma","leaving")  
                    if "arriving" in E_RecentActions:
                            call DrainWord("Emma","arriving")                   
                    if bg_current == "bg emma":
                            if Character != "All": #if it's not clearing all girls. . .
                                    #if the girl is not Emma but you're in Emma's room, the girl takes you to her room
                                    call TaketoRoom(Character)
                            else:
                                    $ E_Loc = "bg campus"
                    else:
                            $ E_Loc = "bg emma"                    
                    hide Emma_Sprite with easeoutright
            if "Laura" in Girls:  
                    #if the character asking is not Laura, this removes Laura from the room
                    if Silent:
                        pass
                    elif Passive:
                        ch_l "I'm leaving."  
                    elif Character != "All":
                        ch_l "Ok. I'm leaving."  
                    else:
                        ch_l "I'm leaving."   
                        
                    if "Laura" in Party:
                            $ Party.remove("Laura")  
                    if "leaving" in L_RecentActions:
                            call DrainWord("Laura","leaving")  
                    if "arriving" in L_RecentActions:
                            call DrainWord("Laura","arriving")                   
                    if bg_current == "bg laura":
                            if Character != "All": #if it's not clearing all girls. . .
                                    #if the girl is not Laura but you're in Laura's room, the girl takes you to her room
                                    call TaketoRoom(Character)
                            else:
                                    $ L_Loc = "bg campus"
                    else:
                            $ L_Loc = "bg laura"                    
                    hide Laura_Sprite with easeoutright
            return 

label TaketoRoom(Girl = "Rogue"):
        if Girl == "Rogue":
                $ bg_current = "bg rogue"
                $ R_Loc = "bg rogue"
        elif Girl == "Kitty":
                $ bg_current = "bg kitty"
                $ K_Loc = "bg kitty"
        elif Girl == "Emma":                  
                $ bg_current = "bg emma"
                $ E_Loc = "bg emma"
        elif Girl == "Laura":                    
#                $ bg_current = "bg laura"
#                $ L_Loc = "bg laura"           
                $ bg_current = "bg playerroom"
                $ L_Loc = "bg playerroom"
        call Set_The_Scene
        call CleartheRoom(Girl)
        call Taboo_Level
        if not Silent:
            "[Girl] brings you back to her room. . ."
        $ renpy.pop_call()
        return
        
label Round10(Options = ["none"]):    
        #Called when it's time to auto-wait/sleep
        if Current_Time == "Night":
                    call Sleepover
                    #End night time
                    if "blanket" in R_RecentActions:  
                            $ R_RecentActions.remove("blanket") 
                    if "blanket" in K_RecentActions:
                            $ K_RecentActions.remove("blanket") 
                    if "blanket" in E_RecentActions:
                            $ E_RecentActions.remove("blanket") 
                    if "blanket" in L_RecentActions:
                            $ L_RecentActions.remove("blanket")
        else:
                    #if it's not night time, just wait
                    if bg_current == "bg rogue":
                            if R_Loc == bg_current:
                                ch_r "Sure, you can wait around a bit."     
                            else:
                                "You wait for Rogue to return."
                            call Wait
                            if Current_Time == "Night" and R_Loc == bg_current:               
                                if R_Sleep or R_SEXP >= 30:                                                         
                                        #It's late but she really likes you
                                        ch_r "It's pretty late, [R_Petname], but you're welcome to stick around. . ."   
                                elif ApprovalCheck("Rogue", 1000, "LI") or ApprovalCheck("Rogue", 600, "OI"):           
                                        #It's late but she really likes you
                                        ch_r "It's pretty late, [R_Petname], but you can stay for a little bit."     
                                else:                                                                                   
                                        #she likes you well enough but it's late so you should go
                                        ch_r "It's getting a little late [R_Petname]. You should head out." 
                                        $ renpy.pop_call()
                                        jump Campus_Map   
                            #end Rogue's room                
                    elif bg_current == "bg kitty":
                            if K_Loc == bg_current:
                                ch_k "Sure, you can hang out for a bit."     
                            else:
                                "You wait for Kitty to return."
                            call Wait
                            if Current_Time == "Night" and K_Loc == bg_current:               
                                if K_Sleep or K_SEXP >= 30:                                                         
                                        #It's late but she really likes you
                                        ch_k "It's kinda late, [K_Petname], but you can stay if you like. . ."   
                                elif ApprovalCheck("Kitty", 1000, "LI") or ApprovalCheck("Kitty", 600, "OI"):           
                                        #It's late but she really likes you
                                        ch_k "It's kinda late, [K_Petname], but you can stay for a bit."     
                                else:                                                                                   
                                        #she likes you well enough but it's late so you should go
                                        ch_k "It's getting late [K_Petname]. You should get some sleep." 
                                        $ renpy.pop_call()
                                        jump Campus_Map   
                            #end Kitty's room            
                    elif bg_current == "bg emma":
                            if E_Loc == bg_current:
                                ch_e "You can stay for a while, if you'd like."     
                            else:
                                "You wait for Emma to return."
                            call Wait
                            if Current_Time == "Night" and E_Loc == bg_current:               
                                if E_Sleep or E_SEXP >= 30:                                                         
                                        #It's late but she really likes you
                                        ch_e "It's getting a bit late, [E_Petname], but I'd like you to stay. . ."   
                                elif ApprovalCheck("Emma", 1000, "LI") or ApprovalCheck("Emma", 600, "OI"):           
                                        #It's late but she really likes you
                                        ch_e "It's getting a bit late, [E_Petname], but you can stay."     
                                else:                                                                                   
                                        #she likes you well enough but it's late so you should go
                                        ch_e "It's getting late, [E_Petname]. I need to get some sleep." 
                                        $ renpy.pop_call()
                                        jump Campus_Map   
                            #end Emma's room       
                    elif bg_current == "bg laura":
                            if L_Loc == bg_current:
                                ch_l "You can stay."     
                            else:
                                "You wait for Laura to return."
                            call Wait
                            if Current_Time == "Night" and L_Loc == bg_current:               
                                if L_Sleep or L_SEXP >= 30:                                                         
                                        #It's late but she really likes you
                                        ch_l "I'm going to sleep soon. You can stay."   
                                elif ApprovalCheck("Laura", 1000, "LI") or ApprovalCheck("Laura", 600, "OI"):           
                                        #It's late but she really likes you
                                        ch_l "It's late, you can stay though."     
                                else:                                                                                   
                                        #she likes you well enough but it's late so you should go
                                        ch_l "I'm going to sleep. You should leave." 
                                        $ renpy.pop_call()
                                        jump Campus_Map   
                            #end Laura's room       
                    else: #if none of those rooms
                        call Wait 
                    #end "if not night time"
        return
#Chat Function >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  

label Chat(Girl=0):
    if Current_Time == "Evening" and "yesdate" in P_DailyActions:
            #checks to see if you want to go on a date
            call Readytogo
    
    if Girl:
            #if a character was pre-selected
            if Girl == "Rogue":
                    if R_Loc == bg_current:
                            call Rogue_Chat_Set("chat")    
                    elif "Rogue" in Digits:
                        if R_Loc == "hold":
                            "She doesn't seem to be picking up."
                        else:
                            "You send Rogue a text."
                            call Rogue_Chat_Set("chat") 
                    else:
                            "You don't know her number, you'll have to go to her." 
                        
            elif Girl == "Kitty":
                    if K_Loc == bg_current:
                            call Kitty_Chat_Set("chat") 
                    elif "Kitty" in Digits:
                        if K_Loc == "hold":
                            "She doesn't seem to be picking up."
                        else:
                            "You send Kitty a text."
                            call Kitty_Chat_Set("chat") 
                    else:
                            "You don't know her number, you'll have to go to her." 
                        
            elif Girl == "Emma":                
                    if "classcaught" not in E_History:
                            "She seems busy." 
                    else:
                            if E_Loc == bg_current:
                                    call Emma_Chat_Set("chat") 
                            elif "Emma" in Digits:
                                if E_Loc == "hold":
                                    "She doesn't seem to be picking up."
                                else:
                                    "You send Emma a text."
                                    call Emma_Chat_Set("chat") 
                            else:
                                    "You don't know her number, you'll have to go to her." 
            elif Girl == "Laura":
                    if L_Loc == bg_current:
                            call Laura_Chat_Set("chat") 
                    elif "Laura" in Digits:
                        if L_Loc == "hold":
                            "She doesn't seem to be picking up."
                        else:
                            "You send Laura a text."
                            call Laura_Chat_Set("chat") 
                    else:
                            "You don't know her number, you'll have to go to her." 
    else:
            #if no-one was pre-selected
            menu:
                "Chat with Rogue" if R_Loc == bg_current: 
                        call Rogue_Chat        
                "Text Rogue" if R_Loc != bg_current: 
                        if "Rogue" in Digits:
                            if R_Loc == "hold":
                                "She doesn't seem to be responding."
                            else:
                                "You send Rogue a text."
                                call Rogue_Chat  
                        else:
                                "You don't know her number, you'll have to go to her." 
                            
                "Chat with Kitty" if K_Loc == bg_current: 
                        call Kitty_Chat        
                "Text Kitty" if K_Loc != bg_current and "met" in K_History: 
                        if "Kitty" in Digits:
                            if K_Loc == "hold":
                                "She doesn't seem to be responding."
                            else:
                                "You send Kitty a text."
                                call Kitty_Chat  
                        else:
                                "You don't know her number, you'll have to go to her." 
                            
                "Chat with [EmmaName]" if E_Loc == bg_current:                     
                        if "classcaught" not in E_History:
                                call Emma_Chat_Minimal
                        else:
                                call Emma_Chat
                "Text [EmmaName]" if E_Loc != bg_current and "met" in E_History: 
                        if "Emma" in Digits:
                            if E_Loc == "hold":
                                "She doesn't seem to be responding."
                            else:
                                if E_Loc == "bg teacher" and bg_current == "bg classroom":
                                        "She texts back, \"We can speak after class, [E_Petname].\"" 
                                        return
                                "You send [EmmaName] a text."                 
                                if "classcaught" not in E_History:
                                        call Emma_Chat_Minimal
                                else:
                                        call Emma_Chat  
                        else:
                            "You don't know her number, you'll have to go to her." 
                
                "Chat with [LauraName]" if L_Loc == bg_current:        
                        call Laura_Chat    
                "Text [LauraName]" if L_Loc != bg_current and "met" in L_History: 
                        if "Laura" in Digits:
                            if L_Loc == "hold":
                                "She doesn't seem to be responding."
                            else:
                                "You send [LauraName] a text."      
                                call Laura_Chat  
                        else:
                            "You don't know her number, you'll have to go to her." 
                "Never Mind":
                    pass
            
            
    return
            
# End Chat  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  

label Present_Check(Present = []):
    # Culls parties down to 2 max
    # call Present_Check(1) will _return positive if the room is filled with the current inhabitants
    # call Present Check will cull inhabitants of the room down to zero
    
    while len(Party) > 2:    
            # If two or more members in the party    
            #Culls down party size to two
            $ Party.remove(Party[2])   
    
    # checks to see which girls are present at a given location
    # If they are in the party, makes sure they are in the room
    # adds members who are not currently in the party
    if "Rogue" in Party: 
                    $ R_Loc = bg_current
    elif R_Loc == bg_current:       
                    $ Present.append("Rogue")
    if "Kitty" in Party: 
                    $ K_Loc = bg_current
    elif K_Loc == bg_current:       
                    $ Present.append("Kitty")
    if "Emma" in Party: 
                    $ E_Loc = bg_current
    elif E_Loc == bg_current:       
                    $ Present.append("Emma")
    if "Laura" in Party: 
                    $ L_Loc = bg_current
    elif L_Loc == bg_current:       
                    $ Present.append("Laura")
        
    
    $ renpy.random.shuffle(Present) #Randomizes pool
    
    if len(Party) >= 1:
        #adds the first party member if it exists
        $ Present.append(Party[0]) 
    if len(Party) == 2:
        #adds the second party member if it exists
        $ Present.append(Party[1]) 
    
    while len(Present) > 2:
            #culls the Present list down to two items (or less if the party is full)
            #Removes the rest
            if Present[0] == "Rogue": 
                    $ Present.remove("Rogue")        
                    call Remove_Girl("Rogue",Hold=1)
            elif Present[0] == "Kitty":      
                    $ Present.remove("Kitty")
                    call Remove_Girl("Kitty",Hold=1)
            elif Present[0] == "Emma":      
                    $ Present.remove("Emma")
                    call Remove_Girl("Emma",Hold=1)
            elif Present[0] == "Laura":      
                    $ Present.remove("Laura")
                    call Remove_Girl("Laura",Hold=1)
                       
    if Present and Ch_Focus not in Present:
            $ renpy.random.shuffle(Present) 
            call Shift_Focus(Present[0])
          
    return




label Remove_Girl(Girl = 0, HideGirl = 1, Hold=0):
    # Girl is the girl being removed, this is for putting girls in a safe location if they run.  
    # "Hold" is sent by Present_Check/Girls_Arrive, if active, and you are in public, it sets the girl nearby 
    
    if Partner == Girl or Girl == "All":
            $ Partner = 0    
    if Girl == "All":
            $ Party = []
            $ Nearby = []
            $ Adjacent = []
    else:        
            if Girl in Party:        
                    $ Party.remove(Girl)
            if Girl in Adjacent:
                    $ Adjacent.remove(Girl)
            if Girl in Nearby:
                    $ Nearby.remove(Girl)
        
    if Girl == "Rogue" or Girl == "All": 
#            if "Rogue" in Party:        
#                    $ Party.remove("Rogue")
            if "leaving" in R_RecentActions:
                    call DrainWord("Rogue","leaving")  
            if "arriving" in R_RecentActions:
                    call DrainWord("Rogue","arriving") 
            if bg_current == R_Loc:                
                if Hold and bg_current in ("bg campus","bg classroom","bg dangerroom"):
                    if "Rogue" not in Nearby:
                            $ Nearby.append("Rogue")
                    $ R_Loc = "nearby"
                elif bg_current == "bg rogue":
                    $ R_Loc = "bg campus"
                else:
                    $ R_Loc = "bg rogue"
                if HideGirl:
                    if HideGirl == 2:
                        hide Rogue with easeoutright
                    else:
                        hide Rogue
                    call Rogue_Hide
    if Girl == "Kitty" or Girl == "All": 
            if "leaving" in K_RecentActions:
                    call DrainWord("Kitty","leaving")  
            if "arriving" in K_RecentActions:
                    call DrainWord("Kitty","arriving")   
            if bg_current == K_Loc:                              
                if Hold and bg_current in ("bg campus","bg classroom","bg dangerroom"):
                    if "Kitty" not in Nearby:
                            $ Nearby.append("Kitty")
                    $ K_Loc = "nearby"
                elif bg_current == "bg kitty":
                    $ K_Loc = "bg campus"
                else:
                    $ K_Loc = "bg kitty"
                if HideGirl:
                    if HideGirl == 2:
                        hide Kitty_Sprite with easeoutbottom
                    else:
                        hide Kitty_Sprite
                    call Kitty_Hide
    if Girl == "Emma" or Girl == "All": 
            if "leaving" in E_RecentActions:
                    call DrainWord("Emma","leaving")  
            if "arriving" in E_RecentActions:
                    call DrainWord("Emma","arriving")   
            if bg_current == E_Loc or (bg_current == "bg classroom" and E_Loc == "bg teacher"):
                if Hold and bg_current in ("bg campus","bg classroom","bg dangerroom"):
                    if "Emma" not in Nearby:
                            $ Nearby.append("Emma")
                    $ E_Loc = "nearby"
                elif bg_current == "bg emma":
                    $ E_Loc = "bg campus"
                else:
                    $ E_Loc = "bg emma"
                if HideGirl:
                    if HideGirl == 2:
                        hide Emma_Sprite with easeoutright
                    else:
                        hide Emma_Sprite
                    call Emma_Hide
    if Girl == "Laura" or Girl == "All": 
            if "leaving" in L_RecentActions:
                    call DrainWord("Laura","leaving")  
            if "arriving" in L_RecentActions:
                    call DrainWord("Laura","arriving")   
            if bg_current == L_Loc:                              
                if Hold and bg_current in ("bg campus","bg classroom","bg dangerroom"):
                    if "Laura" not in Nearby:
                            $ Nearby.append("Laura")
                    $ L_Loc = "nearby"
                elif bg_current == "bg laura":
                    $ L_Loc = "bg campus"
                else:
                    $ L_Loc = "bg laura"
                if HideGirl:
                    if HideGirl == 2:
                        hide Laura_Sprite with easeoutright
                    else:
                        hide Laura_Sprite
                    call Laura_Hide
    #end of Remove Girl
    return
  


label Swap_Nearby(Girl=0,Here=0):
        #allows you to bring nearby girls in. 
        # girl is the girl in question, here is a counter for locals
        if Girl not in Nearby:        
            return
        if bg_current not in ("bg campus","bg classroom","bg dangerroom"):
            #if you aren't in a space that supports this. . .
            "There's no room for that here."
            return
            
        if R_Loc == bg_current:
            $ Here += 1
        if K_Loc == bg_current:
            $ Here += 1
        if E_Loc == bg_current:
            $ Here += 1
        if L_Loc == bg_current:
            $ Here += 1
        
        if Here >= 2:
            #if two or more girls are adjacent so there is no room. . .
            call AnyLine(Girl,"It's a little crowded over there.")
            menu:
                "Move away from an adjacent girl?"
                "Rogue" if R_Loc == bg_current:
                        "You shift away from Rogue."
                        call Remove_Girl("Rogue",1,1)#Hide+moveto nearby
                "Kitty" if K_Loc == bg_current:
                        "You shift away from Kitty."
                        call Remove_Girl("Kitty",1,1)#Hide+moveto nearby
                "Emma" if E_Loc == bg_current:
                        "You shift away from Emma."
                        call Remove_Girl("Emma",1,1)#Hide+moveto nearby
                "Laura" if L_Loc == bg_current:
                        "You shift away from Laura."
                        call Remove_Girl("Laura",1,1)#Hide+moveto nearby        
                "No, never mind.":
                    return
        "[Girl] comes over and joins you."
        if bg_current == "bg classroom":
                $ Adjacent.append(Girl)
        $ Nearby.remove(Girl)   
        call Shift_Focus(Girl)
        if Girl == "Rogue":
                $ R_Loc = bg_current
#                call Display_Rogue
        elif Girl == "Kitty":
                $ K_Loc = bg_current
#                call Display_Kitty
        elif Girl == "Emma":
                $ E_Loc = bg_current
#                call Display_Emma
        elif Girl == "Laura":
                $ L_Loc = bg_current 
#                call Display_Laura
        call Set_The_Scene(1,0,0,0)
        return
#end Swap_Nearby / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    
label Dismissed: 
        # this is called to dismiss any girl in the local area.
        menu:
            "Did you want to ask someone to leave?"
            "Rogue" if R_Loc == bg_current or "Rogue" in Party:
                call Rogue_Dismissed
            "Kitty" if K_Loc == bg_current or "Kitty" in Party:
                call Kitty_Dismissed
            "Emma" if E_Loc == bg_current or "Emma" in Party:
                call Emma_Dismissed
            "Laura" if L_Loc == bg_current or "Laura" in Party:
                call Laura_Dismissed
            "Nevermind.":
                pass
        return
        
# Favorite sex acts >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

label Favorite_Actions(Character=0, Quick=0, Temp=0, ATemp=0, PTemp=0, BTemp=0, TTemp=0, HTemp=0, FTemp=0, D20F=0):
    # Character is the selected girl    
    # if there's no selected character, it does it for all girls
    # if Quick is True, it just returns a string of the action as a value, otherwise it sets it as a lasting variable. 
    if not Character or Character == "Rogue":
                #ass, pussy, blow, tits, hand, fondling, kiss
                $ ATemp = R_Anal + R_DildoA + R_FondleA + R_InsertA + R_LickA        
                $ PTemp = R_Sex + R_DildoP + R_FondleP + R_InsertP + R_LickP
                $ BTemp = R_Blow
                $ TTemp = R_Tit
                $ HTemp = R_Hand
                $ FTemp = R_FondleB + R_FondleT + R_SuckB + R_Hotdog
                                
                #This portion sets a bonus based on the player's favorite activity with her.
                if R_PlayerFav and ApprovalCheck("Rogue", 1500): 
                        if R_PlayerFav == "anal":
                            $ ATemp += 20
                        elif R_PlayerFav == "sex":
                            $ PTemp += 20
                        elif R_PlayerFav == "blow":
                            $ BTemp += 20
                        elif R_PlayerFav == "tit":
                            $ TTemp += 20
                        elif R_PlayerFav == "hand":
                            $ HTemp += 20
                        else:
                            $ FTemp += 20
                elif R_PlayerFav and ApprovalCheck("Rogue", 800):
                        if R_PlayerFav == "anal":
                            $ ATemp += 5
                        elif R_PlayerFav == "sex":
                            $ PTemp += 5
                        elif R_PlayerFav == "blow":
                            $ BTemp += 5
                        elif R_PlayerFav == "tit":
                            $ TTemp += 5
                        elif R_PlayerFav == "hand":
                            $ HTemp += 5
                        else:
                            $ FTemp += 5
                
                #This adds the numbers together to make a large number, then generates a random number between 1 and that total
                $ Total = ATemp + PTemp + BTemp + TTemp + HTemp + FTemp + R_Kissed 
                if Total <= 0:
                    $ D20F = 999
                else:
                    $ D20F = renpy.random.randint(1, Total)
                
                # This selects a favorite activity based on which number is picked.
                if D20F <= ATemp:
                    if R_Anal >= 5:
                            $ Temp = "anal"
                    elif R_LickA >= 5:
                            $ Temp = "lick ass"
                    else:
                            $ Temp = "insert ass"
                elif D20F <= ATemp + PTemp:
                        if R_Sex >= 5:
                            $ Temp = "sex"
                        elif R_LickP >= 5:
                            $ Temp = "lick pussy"
                        else:
                            $ Temp = "fondle pussy"
                elif D20F <= ATemp + PTemp + BTemp:
                            $ Temp = "blow"
                elif D20F <= ATemp + PTemp + BTemp + TTemp:
                            $ Temp = "tit"
                elif D20F <= ATemp + PTemp + BTemp + TTemp + HTemp:
                            $ Temp = "hand"
                elif D20F <= ATemp + PTemp + BTemp + TTemp + HTemp + FTemp:
                        $ D20F = renpy.random.randint(1, 20)
                        if D20F >= 15 and R_Hotdog:
                            $ Temp = "hotdog"
                        elif D20F >= 10 and R_SuckB:
                            $ Temp = "suck breasts"
                        elif D20F >= 5 and R_FondleB:
                            $ Temp = "fondle breasts"
                        else:
                            $ Temp = "fondle thighs"
                else:
                            $ Temp = "kiss you"
                
                if not Quick:
                    $ R_Favorite = Temp
                else:
                    return Temp
    #End Rogue Stuff
    
    if not Character or Character == "Kitty":
                #ass, pussy, blow, tits, hand, fondling, kiss
                $ ATemp = K_Anal + K_DildoA + K_FondleA + K_InsertA + K_LickA        
                $ PTemp = K_Sex + K_DildoP + K_FondleP + K_InsertP + K_LickP
                $ BTemp = K_Blow
                $ TTemp = K_Tit
                $ HTemp = K_Hand
                $ FTemp = K_FondleB + K_FondleT + K_SuckB + K_Hotdog
                                
                #This portion sets a bonus based on the player's favorite activity with her.
                if K_PlayerFav and ApprovalCheck("Kitty", 1500): 
                        if K_PlayerFav == "anal":
                            $ ATemp += 20
                        elif K_PlayerFav == "sex":
                            $ PTemp += 20
                        elif K_PlayerFav == "blow":
                            $ BTemp += 20
                        elif K_PlayerFav == "tit":
                            $ TTemp += 20
                        elif K_PlayerFav == "hand":
                            $ HTemp += 20
                        else:
                            $ FTemp += 20
                elif K_PlayerFav and ApprovalCheck("Kitty", 800):
                        if K_PlayerFav == "anal":
                            $ ATemp += 5
                        elif K_PlayerFav == "sex":
                            $ PTemp += 5
                        elif K_PlayerFav == "blow":
                            $ BTemp += 5
                        elif K_PlayerFav == "tit":
                            $ TTemp += 5
                        elif K_PlayerFav == "hand":
                            $ HTemp += 5
                        else:
                            $ FTemp += 5
                
                #This adds the numbers together to make a large number, then generates a random number between 1 and that total
                $ Total = ATemp + PTemp + BTemp + TTemp + HTemp + FTemp + K_Kissed  
                if Total <= 0:
                    $ D20F = 999
                else:
                    $ D20F = renpy.random.randint(1, Total)
                
                # This selects a favorite activity based on which number is picked.
                if D20F <= ATemp:
                    if K_Anal >= 5:
                            $ Temp = "anal"
                    elif K_LickA >= 5:
                            $ Temp = "lick ass"
                    else:
                            $ Temp = "insert ass"
                elif D20F <= ATemp + PTemp:
                        if K_Sex >= 5:
                            $ Temp = "sex"
                        elif K_LickP >= 5:
                            $ Temp = "lick pussy"
                        else:
                            $ Temp = "fondle pussy"
                elif D20F <= ATemp + PTemp + BTemp:
                            $ Temp = "blow"
                elif D20F <= ATemp + PTemp + BTemp + TTemp:
                            $ Temp = "tit"
                elif D20F <= ATemp + PTemp + BTemp + TTemp + HTemp:
                            $ Temp = "hand"
                elif D20F <= ATemp + PTemp + BTemp + TTemp + HTemp + FTemp:
                        $ D20F = renpy.random.randint(1, 20)
                        if D20F >= 15 and K_Hotdog:
                            $ Temp = "hotdog"
                        elif D20F >= 10 and K_SuckB:
                            $ Temp = "suck breasts"
                        elif D20F >= 5 and K_FondleB:
                            $ Temp = "fondle breasts"
                        else:
                            $ Temp = "fondle thighs"
                else:
                            $ Temp = "kiss you"
                
                if not Quick:
                    $ K_Favorite = Temp
                else:
                    return Temp
    #End Kitty Stuff    
    if not Character or Character == "Emma":
                #ass, pussy, blow, tits, hand, fondling, kiss
                $ ATemp = E_Anal + E_DildoA + E_FondleA + E_InsertA + E_LickA        
                $ PTemp = E_Sex + E_DildoP + E_FondleP + E_InsertP + E_LickP
                $ BTemp = E_Blow
                $ TTemp = E_Tit
                $ HTemp = E_Hand
                $ FTemp = E_FondleB + E_FondleT + E_SuckB + E_Hotdog
                                
                #This portion sets a bonus based on the player's favorite activity with her.
                if E_PlayerFav and ApprovalCheck("Emma", 1500): 
                        if E_PlayerFav == "anal":
                            $ ATemp += 20
                        elif E_PlayerFav == "sex":
                            $ PTemp += 20
                        elif E_PlayerFav == "blow":
                            $ BTemp += 20
                        elif E_PlayerFav == "tit":
                            $ TTemp += 20
                        elif E_PlayerFav == "hand":
                            $ HTemp += 20
                        else:
                            $ FTemp += 20
                        $ TTemp += 20
                elif E_PlayerFav and ApprovalCheck("Emma", 800):
                        if E_PlayerFav == "anal":
                            $ ATemp += 5
                        elif E_PlayerFav == "sex":
                            $ PTemp += 5
                        elif E_PlayerFav == "blow":
                            $ BTemp += 5
                        elif E_PlayerFav == "tit":
                            $ TTemp += 5
                        elif E_PlayerFav == "hand":
                            $ HTemp += 5
                        else:
                            $ FTemp += 5
                        $ TTemp += 10
                
                #This adds the numbers together to make a large number, then generates a random number between 1 and that total
                $ Total = ATemp + PTemp + BTemp + TTemp + HTemp + FTemp + E_Kissed  
                if Total <= 0:
                    $ D20F = 999
                else:
                    $ D20F = renpy.random.randint(1, Total)
                
                # This selects a favorite activity based on which number is picked.
                if D20F <= ATemp:
                    if E_Anal >= 5:
                            $ Temp = "anal"
                    elif E_LickA >= 5:
                            $ Temp = "lick ass"
                    else:
                            $ Temp = "insert ass"
                elif D20F <= ATemp + PTemp:
                        if E_Sex >= 5:
                            $ Temp = "sex"
                        elif E_LickP >= 5:
                            $ Temp = "lick pussy"
                        else:
                            $ Temp = "fondle pussy"
                elif D20F <= ATemp + PTemp + BTemp:
                            $ Temp = "blow"
                elif D20F <= ATemp + PTemp + BTemp + TTemp:
                            $ Temp = "tit"
                elif D20F <= ATemp + PTemp + BTemp + TTemp + HTemp:
                            $ Temp = "hand"
                elif D20F <= ATemp + PTemp + BTemp + TTemp + HTemp + FTemp:
                        $ D20F = renpy.random.randint(1, 20)
                        if D20F >= 15 and E_Hotdog:
                            $ Temp = "hotdog"
                        elif D20F >= 10 and E_SuckB:
                            $ Temp = "suck breasts"
                        elif D20F >= 5 and E_FondleB:
                            $ Temp = "fondle breasts"
                        else:
                            $ Temp = "fondle thighs"
                else:
                            $ Temp = "kiss you"
                
                if not Quick:
                    $ E_Favorite = Temp
                else:
                    return Temp
    #End Emma Stuff            
    
    if not Character or Character == "Laura":
                #ass, pussy, blow, tits, hand, fondling, kiss
                $ ATemp = L_Anal + L_DildoA + L_FondleA + L_InsertA + L_LickA        
                $ PTemp = L_Sex + L_DildoP + L_FondleP + L_InsertP + L_LickP
                $ BTemp = L_Blow
                $ TTemp = L_Tit
                $ HTemp = L_Hand
                $ FTemp = L_FondleB + L_FondleT + L_SuckB + L_Hotdog
                                
                #This portion sets a bonus based on the player's favorite activity with her.
                if L_PlayerFav and ApprovalCheck("Laura", 1500): 
                        if L_PlayerFav == "anal":
                            $ ATemp += 20
                        elif L_PlayerFav == "sex":
                            $ PTemp += 20
                        elif L_PlayerFav == "blow":
                            $ BTemp += 20
                        elif L_PlayerFav == "tit":
                            $ TTemp += 20
                        elif L_PlayerFav == "hand":
                            $ HTemp += 20
                        else:
                            $ FTemp += 20
                        $ TTemp += 20
                elif L_PlayerFav and ApprovalCheck("Laura", 800):
                        if L_PlayerFav == "anal":
                            $ ATemp += 5
                        elif L_PlayerFav == "sex":
                            $ PTemp += 5
                        elif L_PlayerFav == "blow":
                            $ BTemp += 5
                        elif L_PlayerFav == "tit":
                            $ TTemp += 5
                        elif L_PlayerFav == "hand":
                            $ HTemp += 5
                        else:
                            $ FTemp += 5
                        $ TTemp += 10
                
                #This adds the numbers together to make a large number, then generates a random number between 1 and that total
                $ Total = ATemp + PTemp + BTemp + TTemp + HTemp + FTemp + L_Kissed  
                if Total <= 0:
                    $ D20F = 999
                else:
                    $ D20F = renpy.random.randint(1, Total)
                
                # This selects a favorite activity based on which number is picked.
                if D20F <= ATemp:
                    if L_Anal >= 5:
                            $ Temp = "anal"
                    elif L_LickA >= 5:
                            $ Temp = "lick ass"
                    else:
                            $ Temp = "insert ass"
                elif D20F <= ATemp + PTemp:
                        if L_Sex >= 5:
                            $ Temp = "sex"
                        elif L_LickP >= 5:
                            $ Temp = "lick pussy"
                        else:
                            $ Temp = "fondle pussy"
                elif D20F <= ATemp + PTemp + BTemp:
                            $ Temp = "blow"
                elif D20F <= ATemp + PTemp + BTemp + TTemp:
                            $ Temp = "tit"
                elif D20F <= ATemp + PTemp + BTemp + TTemp + HTemp:
                            $ Temp = "hand"
                elif D20F <= ATemp + PTemp + BTemp + TTemp + HTemp + FTemp:
                        $ D20F = renpy.random.randint(1, 20)
                        if D20F >= 15 and L_Hotdog:
                            $ Temp = "hotdog"
                        elif D20F >= 10 and L_SuckB:
                            $ Temp = "suck breasts"
                        elif D20F >= 5 and L_FondleB:
                            $ Temp = "fondle breasts"
                        else:
                            $ Temp = "fondle thighs"
                else:
                            $ Temp = "kiss you"
                
                if not Quick:
                    $ L_Favorite = Temp
                else:
                    return Temp
    #End Laura Stuff     
    return

# End favorite sex acts >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Start First Seen Peen / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 

label Seen_First_Peen(Primary=0, Secondary=0, Silent=0, Undress=0, Passive=0, GirlsNum=0, React=0):
    # call Seen_First_Peen(Primary,Secondary,Silent,Undress)
    # Primary is the first girl, Secondary the second, if there is one    
    # _return will be 0 if other girl didn't comment, 
    # 1 = if the other girl commented, 2 = didn't like it
    # Girlsnum will pass Second to the next girl, and keep track of whether anyone acted
    if not Primary:
            #if this is not during a sex act
            $ D20 = renpy.random.randint(1, 20)
            if R_Loc == bg_current:  
                #If Rogue is around, check to see if she noticed your cock yet
                if (Ch_Focus == "Rogue" or D20 >= 10) and "peen" not in R_RecentActions:
                        #If Rogue is the prinary or secondary character, and hasn't seen your cock yet, call the thing 
                        call Rogue_First_Peen(Silent,Undress)
                        $ GirlsNum = _return                        
            if K_Loc == bg_current:  
                #If Kitty is around, check to see if she noticed your cock yet
                if (Ch_Focus == "Kitty" or D20 >= 10) and "peen" not in K_RecentActions:
                        #If Kitty hasn't seen your cock yet, call the thing 
                        call Kitty_First_Peen(Silent,Undress,GirlsNum)
                        $ GirlsNum = _return        
            if E_Loc == bg_current:  
                #If Emma is around, check to see if she noticed your cock yet
                if (Ch_Focus == "Emma" or D20 >= 10) and "peen" not in E_RecentActions:
                        #If Emma hasn't seen your cock yet, call the thing 
                        call Emma_First_Peen(Silent,Undress,GirlsNum)
                        $ GirlsNum = _return        
            if L_Loc == bg_current:  
                #If Laura is around, check to see if she noticed your cock yet
                if (Ch_Focus == "Laura" or D20 >= 10) and "peen" not in L_RecentActions:
                        #If Laura hasn't seen your cock yet, call the thing 
                        call Laura_First_Peen(Silent,Undress,GirlsNum)
                        $ GirlsNum = _return       
        
            if not GirlsNum:
                #if no girls are present   
                if "naked" not in P_RecentActions and Undress:
                        "You strip nude."
                        $ P_RecentActions.append("naked")
                elif "cockout" in P_RecentActions:
                        return
                else:
                        "You whip your cock out."                
                $ P_RecentActions.append("cockout") 
    #end if not during a sex act  
    else:
            #It's during a sex act
            if Passive:
                    #if in Passive mode, during sex dialog, it only activates if cock is already out.
                    if Approval == Passive and "cockout" not in P_RecentActions:
                        #if both are 3 or both are 4, meaning the activities matched up, 
                        call CockOut
                    if "cockout" not in P_RecentActions:
                        return
                    
            if Primary == "Rogue":
                    call Rogue_First_Peen(Silent,Undress,React=React)               
            elif Primary == "Kitty":
                    call Kitty_First_Peen(Silent,Undress,React=React)
            elif Primary == "Emma":
                    call Emma_First_Peen(Silent,Undress,React=React)
            elif Primary == "Laura":
                    call Laura_First_Peen(Silent,Undress,React=React)
                
            if not Secondary: 
                    pass
            elif Secondary == "Rogue":
                    call Rogue_First_Peen(Silent,Undress,Second = _return)
            elif Secondary == "Kitty":
                    call Kitty_First_Peen(Silent,Undress,Second = _return)
            elif Secondary == "Emma":
                    call Emma_First_Peen(Silent,Undress,Second = _return)
            elif Secondary == "Laura":
                    call Laura_First_Peen(Silent,Undress,Second = _return)
          
    return
    
label CockOut:        
        if (Approval == 3 and Primary == "Rogue") or (Approval == 4 and Secondary == "Rogue"):
                    call Rogue_First_Peen(React=1)   
        elif (Approval == 3 and Primary == "Kitty") or (Approval == 4 and Secondary == "Kitty"):
                    call Kitty_First_Peen(React=1) 
        elif (Approval == 3 and Primary == "Emma") or (Approval == 4 and Secondary == "Emma"):
                    call Emma_First_Peen(React=1) 
        elif (Approval == 3 and Primary == "Laura") or (Approval == 4 and Secondary == "Laura"):
                    call Laura_First_Peen(React=1) 
        $ Approval = 0
        return
    
label Get_Dressed: #checked each time she sees your cock
        #if no girls are present
        if "naked" in P_RecentActions:   
                "You get dressed."
                call DrainWord("Player","naked") 
                call DrainWord("Player","cockout")
        elif "cockout" in P_RecentActions:                 
                "You put your cock away."
                call DrainWord("Player","cockout")
        return
        
# End First Seen Peen / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /     
    
# Start First Les scene / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label Seen_Les(Silent = 0, Undress = 0, GirlsNum = 0): 
        return
# End First Les scene / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /        

label FlashTits(Girl = "Rogue", Timing = 1, Over = 0, Under = 0):
    #This function quickly removes and replaces the girl's tops, put the girl's name in the function call.
    if Girl == "Rogue":
            $ Over = R_Over
            $ Under = R_Chest
            $ R_Over = 0
            $ R_Chest = 0  
            if Timing:
                    pause Timing     
                    $ R_Over = Over
                    $ R_Chest = Under
    elif Girl == "Kitty":
            $ Over = K_Over
            $ Under = K_Chest
            $ K_Over = 0
            $ K_Chest = 0   
            if Timing:
                    pause Timing     
                    $ K_Over = Over
                    $ K_Chest = Under
    elif Girl == "Emma":
            $ Over = E_Over
            $ Under = E_Chest
            $ E_Over = 0
            $ E_Chest = 0   
            if Timing:
                    pause Timing     
                    $ E_Over = Over
                    $ E_Chest = Under
    elif Girl == "Laura":
            $ Over = L_Over
            $ Under = L_Chest
            $ L_Over = 0
            $ L_Chest = 0   
            if Timing:
                    pause Timing     
                    $ L_Over = Over
                    $ L_Chest = Under
    return

# Start Gym Clothes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label Gym_Clothes(Mode = 0, Girl = 0, GirlsNum = 0): #checked each time you enter the Gym
        #GirlsNum tracks whether multiple girls have changed clothes
        #Mode: "change" forces her to change to street clothes
        #"pre" is for if she was meant to have changed before you got there
        #"auto" is for if it happens silently
        #"exit" is for leaving people only.
        if Taboo == 0 and bg_current == "bg dangerroom" and Mode != "change":
            menu:
                "Is this visit for work or for play?"
                "Work [[get geared up]":
                    pass
                "Play [[keep on this outfit]":
                    return
        if not Girl or Girl == "Rogue":
                if R_Loc != "bg dangerroom" or Mode == "change" or Mode == "exit":  
                        #If Rogue has left the gym or was told to change back
                        if Mode == "exit" and "leaving" not in R_RecentActions:
                                #this means she will only change into street clothes if leaving
                                #during the "exit" phase.
                                pass
                        elif R_Outfit == "gym":
                                if bg_current == "bg dangerroom" and "leaving" in R_RecentActions:
                                        #if you're in the danger room, and so is Rogue
                                        show blackscreen onlayer black
                                $ R_Outfit = R_OutfitDay
                                call RogueOutfit(Changed=1)                        
                elif R_Outfit == "gym":
                            #If it's already gym clothes, skip this
                            pass           
                elif Mode == "pre":
                        #If she was already in the gym when you got there
                        if R_Loc == "bg dangerroom" and "Rogue" not in Party:
                                $ R_Outfit = "gym"
                                call RogueOutfit(Changed=1)
                elif Mode == "auto":
                        #If it's set to do it automatically by the call
                        if R_Loc == "bg dangerroom" and R_Loc == bg_current:
                                show blackscreen onlayer black
                                $ R_Outfit = "gym"
                        call RogueOutfit(Changed=1)        
                elif R_Loc == bg_current:
                        #If Rogue is in the gym, see if she'll change clothes                
                        if ApprovalCheck("Rogue", 1200, "LO") or "sub" in R_Traits:
                            pass
                        elif ApprovalCheck("Rogue", 800, "LO") and R_Custom[0]:
                            pass
                        elif ApprovalCheck("Rogue", 600, "LO") and R_Gym[0]:
                            pass
                        else:
                            $ Line = "no"
                        if Line == "no"  or "asked gym" in R_DailyActions or "no ask gym" in R_Traits:   
                            #If she decides not to ask you
                            ch_r "I'll be right back, gotta change."                       
                            show blackscreen onlayer black
                            $ R_Outfit = "gym"
                            call RogueOutfit(Changed=1)
                        else:
                            # She asks to change outfits
                            $ R_DailyActions.append("asked gym")
                            menu:
                                    ch_r "Did you want me to change into my gym clothes?"
                                    "Yeah, they look great.":   
                                        call RogueFace("smile")                          
                                        call Statup("Rogue", "Love", 80, 2)
                                        call Statup("Rogue", "Obed", 40, 1)
                                        call Statup("Rogue", "Inbt", 30, 1)
                                        $ Line = 1                            
                                    "No, stay in that.":
                                        call RogueFace("confused")    
                                        call Statup("Rogue", "Obed", 50, 4)
                                        $ Line = 0
                                    "Whichever you like.":
                                        call RogueFace("confused")                                    
                                        call Statup("Rogue", "Inbt", 50, 2)
                                        $ Line = renpy.random.randint(0, 3)
                                    "I don't care.":        
                                        call RogueFace("angry")   
                                        call Statup("Rogue", "Love", 50, -2, 1)
                                        call Statup("Rogue", "Obed", 50, 2)
                                        call Statup("Rogue", "Inbt", 50, 2)  
                                        $ Line = renpy.random.randint(0, 1)
                            if Line:
                                    #If she decided to change     
                                    ch_r "Ok, be right back."                       
                                    show blackscreen onlayer black
                                    $ R_Outfit = "gym"
                                    call RogueOutfit(Changed=1)
                            #end asked
                        if R_Outfit == "gym":
                            $ GirlsNum += 1 
                        $ Line = 0
                hide blackscreen onlayer black
        # End Rogue      
            
        if not Girl or Girl == "Kitty" or Mode == "exit":
                if K_Loc != "bg dangerroom" or Mode == "change":  
                        #If Kitty has left the gym or was told to change back
                        if Mode == "exit" and "leaving" not in K_RecentActions:
                                #this means she will only change into street clothes if leaving
                                #during the "exit" phase.
                                pass
                        elif K_Outfit == "gym":
                                if bg_current == "bg dangerroom" and "leaving" in K_RecentActions:
                                        #if you're in the danger room, and so is Kitty
                                        show blackscreen onlayer black
                                $ K_Outfit = K_OutfitDay
                                call KittyOutfit(Changed=1)                        
                elif K_Outfit == "gym":
                            #If it's already gym clothes, skip this
                            pass   
                elif Mode == "pre":
                        #If she was already here
                        if K_Loc == "bg dangerroom" and "Kitty" not in Party:
                            $ K_Outfit = "gym"
                            call KittyOutfit(Changed=1)
                elif Mode == "auto":
                        #If it's set to do it automatically by the call
                                if K_Loc == "bg dangerroom" and K_Loc == bg_current:
                                        show blackscreen onlayer black
                                $ K_Outfit = "gym"
                                call KittyOutfit(Changed=1)
                elif K_Loc == bg_current:
                        #If Kitty is in the gym, see if she'll change clothes
                        if ApprovalCheck("Kitty", 1300, "LO") or "sub" in K_Traits:
                            pass
                        elif ApprovalCheck("Kitty", 800, "LO") and K_Custom[0]:
                            pass
                        elif ApprovalCheck("Kitty", 600, "LO") and K_Gym[0]:
                            pass
                        else:
                            $ Line = "no"
                        if Line == "no" or "asked gym" in K_DailyActions or "no ask gym" in K_Traits:   
                            #If she decides not to ask you   
                            if GirlsNum:
                                ch_k "I'll be right back too."  
                            else:
                                ch_k "I'll be back soon, gotta change."                       
                            show blackscreen onlayer black
                            $ K_Outfit = "gym"
                            call KittyOutfit(Changed=1)
                        else:
                            # She asks to change outfits
                            $ K_DailyActions.append("asked gym")
                            if GirlsNum:
                                $ Line = "Should I change too?"  
                            else:
                                $ Line = "Would you like me to change into my gym clothes?"   
                            menu:
                                    ch_k "[Line]"
                                    "Yeah, they look great.":  
                                        call KittyFace("smile")                              
                                        call Statup("Kitty", "Love", 80, 2)
                                        call Statup("Kitty", "Obed", 40, 1)
                                        call Statup("Kitty", "Inbt", 30, 1)
                                        $ Line = 1                            
                                    "No, stay in that.":
                                        call KittyFace("confused")    
                                        call Statup("Kitty", "Obed", 50, 5)
                                        $ Line = 0
                                    "Whichever you like.": 
                                        call KittyFace("confused")                                      
                                        call Statup("Kitty", "Inbt", 50, 1)
                                        $ Line = renpy.random.randint(0, 3)
                                    "I don't care.":        
                                        call KittyFace("angry")      
                                        call Statup("Kitty", "Love", 50, -3, 1)
                                        call Statup("Kitty", "Obed", 50, 4)
                                        call Statup("Kitty", "Inbt", 50, 2)  
                                        $ Line = renpy.random.randint(0, 1)
                            if Line:
                                    #If she decided to change     
                                    ch_k "Ok, back in a bit"                       
                                    show blackscreen onlayer black
                                    $ K_Outfit = "gym"
                                    call KittyOutfit(Changed=1)
                            #end asked
                        if K_Outfit == "gym":
                            $ GirlsNum += 1 
                        $ Line = 0
                hide blackscreen onlayer black
        # End Kitty   
            
        if not Girl or Girl == "Emma" or Mode == "exit":
                if E_Loc != "bg dangerroom" or Mode == "change":  
                        #If Emma has left the gym or was told to change back
                        if Mode == "exit" and "leaving" not in E_RecentActions:
                                #this means she will only change into street clothes if leaving
                                #during the "exit" phase.
                                pass
                        elif E_Outfit == "gym":
                                if bg_current == "bg dangerroom" and "leaving" in E_RecentActions:
                                        #if you're in the danger room, and so is Emma
                                        show blackscreen onlayer black
                                $ E_Outfit = E_OutfitDay
                                call EmmaOutfit(Changed=1)                        
                elif E_Outfit == "gym":
                            #If it's already gym clothes, skip this
                            pass   
                elif Mode == "pre":
                        #If she was already here
                        if E_Loc == "bg dangerroom" and "Emma" not in Party:
                            $ E_Outfit = "gym"
                            call EmmaOutfit(Changed=1)
                elif Mode == "auto":
                        #If it's set to do it automatically by the call
                                if E_Loc == "bg dangerroom" and E_Loc == bg_current:
                                        show blackscreen onlayer black
                                $ E_Outfit = "gym"
                                call EmmaOutfit(Changed=1)
                elif E_Loc == bg_current:
                        #If Emma is in the gym, see if she'll change clothes
                        if ApprovalCheck("Emma", 1300, "LO") or "sub" in E_Traits:
                            pass
                        elif ApprovalCheck("Emma", 900, "LO") and E_Custom[0]:
                            pass
                        elif ApprovalCheck("Emma", 700, "LO") and E_Gym[0]:
                            pass
                        else:
                            $ Line = "no"
                        if Line == "no" or "asked gym" in E_DailyActions or "no ask gym" in E_Traits:   
                            #If she decides not to ask you
                            if GirlsNum:
                                ch_e "I should change too."  
                            else:
                                ch_e "I need to change into something more appropriate."                       
                            show blackscreen onlayer black
                            $ E_Outfit = "gym"
                            call EmmaOutfit(Changed=1)
                        else:
                            # She asks to change outfits
                            $ E_DailyActions.append("asked gym")
                            if GirlsNum:
                                $ Line = "Do you think I should change as well?"  
                            else:
                                $ Line = "Did you want me to change into my gear?"   
                            menu:
                                    ch_e "[Line]"
                                    "Yeah, they look great.":  
                                        call EmmaFace("smile")                              
                                        call Statup("Emma", "Love", 60, 1)
                                        call Statup("Emma", "Obed", 50, 1)
                                        call Statup("Emma", "Inbt", 30, 1)
                                        $ Line = 1                            
                                    "No, stay in that.":
                                        call EmmaFace("confused")    
                                        call Statup("Emma", "Obed", 50, 5)
                                        $ Line = 0
                                    "Whichever you like.": 
                                        call EmmaFace("confused")                                      
                                        call Statup("Emma", "Inbt", 50, 1)
                                        $ Line = renpy.random.randint(0, 3)
                                    "I don't care.":        
                                        call EmmaFace("angry")      
                                        call Statup("Emma", "Love", 50, -3, 1)
                                        call Statup("Emma", "Obed", 50, 4)
                                        call Statup("Emma", "Inbt", 50, 2)  
                                        $ Line = renpy.random.randint(0, 1)
                            if Line:
                                    #If she decided to change     
                                    ch_e "Fine, I'll be right back."                       
                                    show blackscreen onlayer black
                                    $ E_Outfit = "gym"
                                    call EmmaOutfit(Changed=1)
                            #end asked
                        if E_Outfit == "gym":
                            $ GirlsNum += 1 
                        $ Line = 0
                hide blackscreen onlayer black
        # End Emma 
            
        if not Girl or Girl == "Laura" or Mode == "exit":
                if L_Loc != "bg dangerroom" or Mode == "change":  
                        #If Laura has left the gym or was told to change back
                        if Mode == "exit" and "leaving" not in L_RecentActions:
                                #this means she will only change into street clothes if leaving
                                #during the "exit" phase.
                                pass
                        elif L_Outfit == "gym":
                                if bg_current == "bg dangerroom" and "leaving" in L_RecentActions:
                                        #if you're in the danger room, and so is Laura
                                        show blackscreen onlayer black
                                $ L_Outfit = L_OutfitDay
                                call LauraOutfit(Changed=1)                        
                elif L_Outfit == "gym":
                            #If it's already gym clothes, skip this
                            pass           
                elif Mode == "pre":
                        #If she was already in the gym when you got there
                        if L_Loc == "bg dangerroom" and "Laura" not in Party:
                            $ L_Outfit = "gym"
                            call LauraOutfit(Changed=1)
                elif Mode == "auto":
                        #If it's set to do it automatically by the call
                        if L_Loc == "bg dangerroom" and L_Loc == bg_current:
                                show blackscreen onlayer black
                                $ L_Outfit = "gym"
                        call LauraOutfit(Changed=1)        
                elif L_Loc == bg_current:
                        #If Laura is in the gym, see if she'll change clothes                
                        if ApprovalCheck("Laura", 1200, "LO") or "sub" in L_Traits:
                            pass
                        elif ApprovalCheck("Laura", 800, "LO") and L_Custom[0]:
                            pass
                        elif ApprovalCheck("Laura", 600, "LO") and L_Gym[0]:
                            pass
                        else:
                            $ Line = "no"
                        if Line == "no"  or "asked gym" in L_DailyActions or "no ask gym" in L_Traits:   
                            #If she decides not to ask you
                            ch_l "I'll be right back.."                       
                            show blackscreen onlayer black
                            $ L_Outfit = "gym"
                            call LauraOutfit(Changed=1)
                        else:
                            # She asks to change outfits
                            $ L_DailyActions.append("asked gym")
                            menu:
                                    ch_l "Did you want me to change into my gym clothes?"
                                    "Yeah, they look great.":   
                                        call LauraFace("smile")                          
                                        call Statup("Laura", "Love", 80, 2)
                                        call Statup("Laura", "Obed", 40, 1)
                                        call Statup("Laura", "Inbt", 30, 1)
                                        $ Line = 1                            
                                    "No, stay in that.":
                                        call LauraFace("confused")    
                                        call Statup("Laura", "Obed", 50, 4)
                                        $ Line = 0
                                    "Whichever you like.":
                                        call LauraFace("confused")                                    
                                        call Statup("Laura", "Inbt", 50, 2)
                                        $ Line = renpy.random.randint(0, 3)
                                    "I don't care.":        
                                        call LauraFace("angry")   
                                        call Statup("Laura", "Love", 50, -2, 1)
                                        call Statup("Laura", "Obed", 50, 2)
                                        call Statup("Laura", "Inbt", 50, 2)  
                                        $ Line = renpy.random.randint(0, 1)
                            if Line:
                                    #If she decided to change     
                                    ch_l "I'll be right back then."                       
                                    show blackscreen onlayer black
                                    $ L_Outfit = "gym"
                                    call LauraOutfit(Changed=1)
                            #end asked
                        if L_Outfit == "gym":
                            $ GirlsNum += 1 
                        $ Line = 0
                hide blackscreen onlayer black
        # End Laura  
            
        return
# End Gym clothes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /        




# Start Girls Location / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girls_Location(GirlsNum = 0, Change=0):
        #this figures out where girls are and where to put spares. 
        #it's called most often by Locations, after Waits
        #Girlsnum sets the number of girls that have already talked
        #"arriving" is set by the "Schedule" code, and will not be applied unless 
        # the girl in questions was someplace else, and just showed up here on their own.
        if "leaving" in R_RecentActions:
                if "sleepover" in R_Traits:
                        $ R_Traits.remove("sleepover")
                call Rogue_Leave
                if "Rogue" in Adjacent and R_Loc != "bg classroom":
                        $ Adjacent.remove("Rogue")
                if R_Loc != bg_current:
                        $ Change = 1
                        $ GirlsNum += 1
        if "leaving" in K_RecentActions:
                if "sleepover" in K_Traits:
                        $ K_Traits.remove("sleepover")
                call Kitty_Leave(GirlsNum)
                if "Kitty" in Adjacent and K_Loc != "bg classroom":
                        $ Adjacent.remove("Kitty")
                if K_Loc != bg_current:
                        $ Change = 1   
                        $ GirlsNum += 1
        if "leaving" in E_RecentActions:
                if "sleepover" in E_Traits:
                        $ E_Traits.remove("sleepover")
                call Emma_Leave(GirlsNum)
                if E_Loc != bg_current:
                        $ Change = 1
                        $ GirlsNum += 1
        if "leaving" in L_RecentActions:
                if "sleepover" in L_Traits:
                        $ L_Traits.remove("sleepover")
                call Laura_Leave(GirlsNum)
                if "Laura" in Adjacent and L_Loc != "bg classroom":
                        $ Adjacent.remove("Laura")
                if L_Loc != bg_current:
                        $ Change = 1   
                        $ GirlsNum += 1
        
        
        #if Girl was in Nearby, but was moved to a new location
        if "Rogue" in Nearby and R_Loc != bg_current and R_Loc != "nearby":
                    $ Nearby.remove("Rogue")
        if "Kitty" in Nearby and K_Loc != bg_current and K_Loc != "nearby":                    
                    $ Nearby.remove("Kitty")
        if "Emma" in Nearby and E_Loc != bg_current and E_Loc != "nearby":                    
                    $ Nearby.remove("Emma")
        if "Laura" in Nearby and L_Loc != bg_current and L_Loc != "nearby":                    
                    $ Nearby.remove("Laura")
                        
        if Change:
            #if there are any fewer girls than there were, Set the Scene
            call Set_The_Scene(Dress=0)
            
        if "arriving" in R_RecentActions:
                call Girls_Arrive
        elif "arriving" in K_RecentActions:
                call Girls_Arrive
        elif "arriving" in E_RecentActions:
                call Girls_Arrive
        elif "arriving" in L_RecentActions:
                call Girls_Arrive
                
        return
        
# End Girls Location / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    
label GirlsAngry(Girls = 0):
        # Causes girls to storm off if you've pissed them off. 
        $ Tempmod = 0
        if R_Loc == bg_current and "angry" in R_RecentActions:
                if bg_current == "bg rogue":                
                    ch_r "You should get out, I'm fix'in ta throw down."
                    "You head back to your room."
                    $ renpy.pop_call()
                    jump Player_Room_Entry
                else:        
                    $ R_Loc = "bg rogue"            
                if "Rogue" in Party:
                    $ Party.remove("Rogue")  
                "Rogue storms off."
                $ Girls += 1
                hide Rogue with easeoutleft
        if K_Loc == bg_current and "angry" in K_RecentActions:
                if bg_current == "bg kitty":
                    ch_k "You should get out of here, I can't even look at you right now."
                    "You head back to your room."
                    $ renpy.pop_call()
                    jump Player_Room_Entry
                else:        
                    $ K_Loc = "bg kitty"
                    if Girls:
                        ". . . and so does Kitty."
                    else:
                        "Kitty storms off."            
                if "Kitty" in Party:
                    $ Party.remove("Kitty")  
                $ Girls += 1
                hide Kitty_Sprite with easeoutleft
        if E_Loc == bg_current and "angry" in E_RecentActions:
                if bg_current == "bg emma":
                    ch_e "You should leave, or do you want to test me?"
                    "You head back to your room."
                    $ renpy.pop_call()
                    jump Player_Room_Entry
                else:        
                    $ E_Loc = "bg emma"
                    if Girls:
                        ". . . and so does [EmmaName]."
                    else:
                        "[EmmaName] storms off."            
                if "Emma" in Party:
                    $ Party.remove("Emma")  
                $ Girls += 1
                hide Emma_Sprite with easeoutleft
        if L_Loc == bg_current and "angry" in L_RecentActions:
                if bg_current == "bg laura":
                    ch_l "You should leave."
                    "You head back to your room."
                    $ renpy.pop_call()
                    jump Player_Room_Entry
                else:        
                    $ L_Loc = "bg laura"
                    if Girls:
                        ". . . and so does [LauraName]."
                    else:
                        "[LauraName] storms off."            
                if "Laura" in Party:
                    $ Party.remove("Laura")  
                $ Girls += 1
                hide Laura_Sprite with easeoutleft
        return    
    
# Start Girls Arrive / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
label Girls_Arrive(Primary = 0, Secondary = 0, GirlsNum = 0):
        #"arriving" is set by the "Schedule" code, and will not be applied unless 
        # the girl in questions was someplace else, and just showed up here on their own.
        
        $ Options = []
        if "arriving" in R_RecentActions and "Rogue" not in Party:   
                $ GirlsNum += 1
                $ Options.append("Rogue")
                call DrainWord("Rogue","arriving")  
        if "arriving" in K_RecentActions and "Kitty" not in Party: 
                $ GirlsNum += 1
                $ Options.append("Kitty")
                call DrainWord("Kitty","arriving")  
        if "arriving" in E_RecentActions and "Emma" not in Party: 
                $ GirlsNum += 1
                $ Options.append("Emma")
                call DrainWord("Emma","arriving")  
        if "arriving" in L_RecentActions and "Laura" not in Party: 
                $ GirlsNum += 1
                $ Options.append("Laura")
                call DrainWord("Laura","arriving")  
             
        $ renpy.random.shuffle(Options)
                
        if len(Options) <= 0 or (len(Party)+len(Adjacent)) >= 2:                
                    #If nobody's here, or if the space is full, return
                    return    
        elif (len(Party)+len(Adjacent)) <= 1:
                    #if the party is one or less and people are in the room
                    $ Primary = Options[0] 
                    if (len(Party)+len(Adjacent)) == 0 and len(Options) >= 2:                    
                        #if the party is empty and 2+ people are in the room
                        $ Secondary = Options[1] 
                    
        if len(Options) > 2:
                #This triggers if there are more than two girls in the room. Primary and Secondary have been chosen and removed.            
                #If it's her room, she gets to be primary, otherwise she goes to her room            
                $ Options.remove(Primary)
                $ Options.remove(Secondary)
                if "Rogue" in Options:
                            if bg_current == "bg rogue":
                                $ Secondary = Primary
                                $ Primary = "Rogue"
                            else:
                                $ R_Loc = "bg rogue"
                            $ Options.remove("Rogue")
                if "Kitty" in Options:
                            if bg_current == "bg kitty":
                                $ Secondary = Primary
                                $ Primary = "Kitty"
                            else:
                                $ K_Loc = "bg kitty"
                            $ Options.remove("Kitty")   
                if "Emma" in Options:
                            if bg_current == "bg emma":
                                $ Secondary = Primary
                                $ Primary = "Emma"
                            else:
                                $ E_Loc = "bg emma"
                            $ Options.remove("Emma")    
                if "Laura" in Options:
                            if bg_current == "bg laura":
                                $ Secondary = Primary
                                $ Primary = "Laura"
                            else:
                                $ E_Loc = "bg laura"
                            $ Options.remove("Laura")            
                #end list clearing
        
        if "locked" in P_Traits:
                if Primary == "Kitty":
                        call Locked_Door("Kitty")
                        if K_Loc != bg_current:
                            $ Primary = 0
                        elif Secondary:
                            #since Kitty can just barg right in, if she does so, 
                            #flip the two girls in their order
                            $ Primary = Secondary
                            $ Secondary = "Kitty"
                            "You hear a \"thump\" as if someone was trying to follow Kitty."
                        
                if Primary == "Rogue":
                        call Locked_Door("Rogue")
                        if R_Loc != bg_current:
                            $ Primary = 0
                elif Primary == "Emma":
                        call Locked_Door("Emma")
                        if E_Loc != bg_current:
                            $ Primary = 0
                elif Primary == "Laura":
                        call Locked_Door("Laura")
                        if L_Loc != bg_current:
                            $ Primary = 0
        #End "if the door was locked." 
                    
        if len(Options) > 2:
                # if there is two girl in the area, remove the excess.
                # If "nearby" is a valid place to put them, it puts them there
                if R_Loc == bg_current and "Rogue" not in (Primary,Secondary) and "Rogue" not in Party and "Rogue" not in Adjacent:
                        call Remove_Girl("Rogue",Hold=1)
                if K_Loc == bg_current and "Kitty" not in (Primary,Secondary) and "Kitty" not in Party and "Kitty" not in Adjacent:
                        call Remove_Girl("Kitty",Hold=1)
                if E_Loc == bg_current and "Emma" not in (Primary,Secondary) and "Emma" not in Party and "Emma" not in Adjacent:
                        call Remove_Girl("Emma",Hold=1)
                if L_Loc == bg_current and "Laura" not in (Primary,Secondary) and "Laura" not in Party and "Laura" not in Adjacent:
                        call Remove_Girl("Laura",Hold=1)
        
        if not Primary:
                return
        $ Options = []    
        #This sequence sets the pecking order, more important once there are more girls
        #girls left out of this are put into "Nearby" for the current space
            
        if bg_current == "bg dangerroom":   
                call Gym_Clothes("auto")
        call Set_The_Scene #causes the girls to display
        if bg_current == "bg player":
                    if Secondary:  
                            #if there's a second girl
                            "[Primary] and [Secondary] just entered your room."
                    else:
                            #if there's no second girl,
                            "[Primary] just entered your room."
                            
                    if Primary == "Rogue":
                                if Secondary:                        
                                    ch_r "Hey, [R_Petname], can we come in?"
                                else:
                                    ch_r "Hey, [R_Petname], can I come in?"
                    elif Primary == "Kitty":
                                if Secondary:                        
                                    ch_k "Hey[K_like]can we come in?"
                                else:
                                    ch_k "Hey[K_like]can I come in?"
                    elif Primary == "Emma":
                                if Secondary:                        
                                    ch_e "Ah, good, you're here. May we come in?"
                                else:
                                    ch_e "Ah, good, you're here. May I come in?"
                    elif Primary == "Laura":                      
                                ch_l "Hey."
                                ch_p ". . . [[She seems to want to stay]."
                    menu:
                        extend ""
                        "Sure.":
                            $ Line = "sure"                               
                        "Not right now, maybe later.":
                            $ Line = "later"
                        "Nope.":  
                            $ Line = "no"
                                   
                                    
                    if Line == "sure":
                        if Primary == "Rogue" or Secondary == "Rogue":
                                    call Statup("Rogue", "Love", 80, 1)
                                    call Statup("Rogue", "Obed", 50, 2)
                                    call Statup("Rogue", "Inbt", 50, 2) 
                                    if Primary == "Rogue": 
                                            ch_r "Thanks."
                        if Primary == "Kitty" or Secondary == "Kitty":
                                    call Statup("Kitty", "Love", 80, 1)
                                    call Statup("Kitty", "Obed", 60, 2)
                                    call Statup("Kitty", "Inbt", 50, 3)
                                    if Primary == "Kitty":
                                            ch_k "Thanks."
                        if Primary == "Emma" or Secondary == "Emma":
                                    call Statup("Emma", "Love", 50, 1)
                                    call Statup("Emma", "Obed", 60, 1)
                                    call Statup("Emma", "Inbt", 50, 2)
                                    if Primary == "Emma":
                                            ch_e "Good."
                        if Primary == "Laura" or Secondary == "Laura":
                                    call Statup("Laura", "Love", 50, 1)
                                    call Statup("Laura", "Obed", 60, 1)
                                    call Statup("Laura", "Inbt", 50, 2)
                                    if Primary == "Laura":
                                            "She doesn't leave."
                        #end "sure"
                    if Line == "later":     
                        if Primary == "Rogue" or Secondary == "Rogue":
                                    call Statup("Rogue", "Love", 60, -1, 1)
                                    call Statup("Rogue", "Obed", 70, 5) 
                                    call RogueFace("confused") 
                                    if Primary == "Rogue" and Secondary: 
                                            ch_r "Um, ok, we'll go then."
                                    elif Primary == "Rogue":
                                            ch_r "Um, ok."
                                    call Remove_Girl("Rogue")
                        if Primary == "Kitty" or Secondary == "Kitty":  
                                    call Statup("Kitty", "Love", 60, -2, 1)
                                    call Statup("Kitty", "Obed", 70, 7) 
                                    call KittyFace("confused") 
                                    if Primary == "Kitty" and Secondary: 
                                            ch_k "Oh[K_like]we'll get going then."
                                    elif Primary == "Kitty":
                                            ch_k "Oh[K_like]I'll get going then."
                                    call Remove_Girl("Kitty")
                        if Primary == "Emma" or Secondary == "Emma":  
                                    call Statup("Emma", "Love", 90, -2)
                                    call Statup("Emma", "Love", 50, -5)
                                    call Statup("Emma", "Obed", 70, 5) 
                                    call Statup("Emma", "Obed", 30, -7) 
                                    call EmmaFace("confused") 
                                    if Primary == "Emma": 
                                            ch_e "If that's how you wish to play it. . ."
                                    call Remove_Girl("Emma")
                        if Primary == "Laura" or Secondary == "Laura":  
                                    call Statup("Laura", "Love", 90, -2)
                                    call Statup("Laura", "Love", 50, -5)
                                    call Statup("Laura", "Obed", 70, 5) 
                                    call Statup("Laura", "Obed", 30, -7) 
                                    call LauraFace("confused") 
                                    if Primary == "Laura": 
                                            ch_l "Ok, later."
                                    call Remove_Girl("Laura")
                        #end "later"
                    if Line == "no":
                        if Primary == "Rogue" or Secondary == "Rogue":
                                    call Statup("Rogue", "Obed", 50, 5)         
                                    if ApprovalCheck("Rogue", 1800) or ApprovalCheck("Rogue", 500, "O"):
                                        call Statup("Rogue", "Obed", 80, 2)
                                        ch_r "I guess that's ok. See you later then."
                                    else:    
                                        call RogueFace("angry") 
                                        call Statup("Rogue", "Love", 60, -5, 1)
                                        call Statup("Rogue", "Love", 80, -2)
                                        call Statup("Rogue", "Obed", 80, 3)
                                        call Statup("Rogue", "Inbt", 50, 1) 
                                        ch_r "Well fine!"
                                    call Remove_Girl("Rogue")
                        if Primary == "Kitty" or Secondary == "Kitty":  
                                    call Statup("Kitty", "Obed", 50, 7)         
                                    if ApprovalCheck("Kitty", 1800) or ApprovalCheck("Kitty", 500, "O"):
                                        call Statup("Kitty", "Obed", 80, 2)
                                        ch_k "If you want some alone time. . ."
                                    else:    
                                        call KittyFace("angry") 
                                        call Statup("Kitty", "Love", 60, -6, 1)
                                        call Statup("Kitty", "Love", 80, -4)
                                        call Statup("Kitty", "Obed", 80, 5)
                                        call Statup("Kitty", "Inbt", 50, 1) 
                                        ch_k "Jerk!"
                                    call Remove_Girl("Kitty")
                        if Primary == "Emma" or Secondary == "Emma":  
                                    call Statup("Emma", "Obed", 50, 7)         
                                    if ApprovalCheck("Emma", 2000) or ApprovalCheck("Emma", 500, "O"):
                                        call Statup("Emma", "Obed", 80, 2)
                                        ch_e "I suppose you can have your personal space. . ."
                                    else:    
                                        call EmmaFace("angry") 
                                        call Statup("Emma", "Love", 60, -6, 1)
                                        call Statup("Emma", "Love", 90, -4)
                                        call Statup("Emma", "Obed", 80, 5)
                                        call Statup("Emma", "Inbt", 50, 1) 
                                        ch_e "We'll see how long that attitude lasts. . ."
                                    call Remove_Girl("Emma")
                        if Primary == "Laura" or Secondary == "Laura":  
                                    call Statup("Laura", "Obed", 50, 7)         
                                    if ApprovalCheck("Laura", 2000) or ApprovalCheck("Laura", 500, "O"):
                                        call Statup("Laura", "Obed", 80, 2)
                                        ch_l "Not a problem."
                                    else:    
                                        call LauraFace("angry") 
                                        call Statup("Laura", "Love", 60, -6, 1)
                                        call Statup("Laura", "Love", 90, -4)
                                        call Statup("Laura", "Obed", 80, 5)
                                        call Statup("Laura", "Inbt", 50, 1) 
                                        "She seems upset."
                                    call Remove_Girl("Laura")
                        if Secondary:
                                    "The girls storm out."
                        #end "nope"
                    #end girls showed up to player's room.
        elif bg_current == "bg rogue":       
                    if Secondary:  
                            #if there's a second girl
                            "[Primary] and [Secondary] just entered the room."
                    else:
                            #if there's no second girl,
                            "[Primary] just entered the room."         
                    if Primary == "Rogue" or Secondary == "Rogue":
                                    if "angry" in R_DailyActions:
                                            call RogueFace("bemused", 1) 
                                            ch_r "I'm kinda pissed at you right now, get out of here." 
                                    elif Current_Time == "Night" and ApprovalCheck("Rogue", 1000, "LI") and ApprovalCheck("Rogue", 600, "OI"):
                                            ch_r "Oh, hey, [R_Petname], it's pretty late, but I guess you can stick around for a bit."  
                                            $ Line = "stay"                     
                                    elif ApprovalCheck("Rogue", 1300) or ApprovalCheck("Rogue", 500, "O"):
                                            ch_r "Oh, hey, [R_Petname], nice to see you here."
                                            $ Line = "stay"
                                    elif Current_Time == "Night":
                                            ch_r "Oh, hey, [R_Petname], it's kind late, could you head out of here?" 
                                    elif ApprovalCheck("Rogue", 600, "LI") or ApprovalCheck("Rogue", 300, "OI"):
                                            ch_r "Oh, hey, [R_Petname]. You can stick around, I guess."
                                            $ Line = "stay"
                                    else: 
                                            ch_r "Hey, [R_Petname], I'm not sure why you're here, but I'd rather you leave."  
                                    if Line != "stay":
                                        menu:
                                            extend ""
                                            "Sure, ok. [[you go]":
                                                        call Statup("Rogue", "Love", 80, 1)
                                                        call Statup("Rogue", "Obed", 50, 2)
                                                        call Statup("Rogue", "Inbt", 50, 2)  
                                                        ch_r "Thanks."
                                                        "You head back to your room."
                                            "Sorry, I'll go.":
                                                        call Statup("Rogue", "Love", 90, 2)
                                                        call Statup("Rogue", "Obed", 50, 3) 
                                                        call RogueFace("smile") 
                                                        ch_r "Thanks."
                                                        "You head back to your room."
                                            "Are you sure I can't stay?":
                                                        if "angry" in R_DailyActions:
                                                                call RogueFace("angry") 
                                                                ch_r "What part of \"no\" don't ya get?"                  
                                                        elif Current_Time == "Night" and ApprovalCheck("Rogue", 800, "LI") and ApprovalCheck("Rogue", 400, "OI"):                                                            
                                                                call RogueFace("sadside") 
                                                                ch_r "I suppose I can make an exception this once." 
                                                                $ Line = "stay"
                                                        elif Current_Time == "Night":
                                                                ch_r "No way, [R_Petname]. Try again tomorrow."                                                 
                                                        elif ApprovalCheck("Rogue", 750):
                                                                ch_r "Oh, fine. For a little bit."
                                                                $ Line = "stay"
                                                        else: 
                                                                call RogueFace("angry") 
                                                                ch_r "No, seriously, get."   
                                                        if Line != "stay": 
                                                                call Statup("Rogue", "Love", 80, -1)
                                                                call Statup("Rogue", "Inbt", 50, 3) 
                                                                "Rogue kicks you out of the room."                                                    
                                            "I'm sticking around, thanks.":   
                                                        if "angry" in R_DailyActions:
                                                                call RogueFace("angry") 
                                                                ch_r "Oh {i}hell{/i} no."
                                                        elif not ApprovalCheck("Rogue", 1800) and not ApprovalCheck("Rogue", 500, "O"):
                                                                call RogueFace("angry") 
                                                                ch_r "No way, buster! Out!"
                                                        else:
                                                                call Statup("Rogue", "Obed", 80, 5)
                                                                call RogueFace("sad") 
                                                                ch_r ". . ." 
                                                                ch_r "I guess that's ok."
                                                                $ Line = "stay"
                                                        if Line != "stay":
                                                                call Statup("Rogue", "Love", 60, -5, 1)
                                                                call Statup("Rogue", "Love", 80, -5)
                                                                call Statup("Rogue", "Obed", 50, 2)
                                                                call Statup("Rogue", "Inbt", 60, 5) 
                                                                "Rogue kicks you out of the room."
                                    if Line != "stay":
                                        $ bg_current = "bg player"  
                                        jump Player_Room
                                    #End Rogue tells you to leave. 
                    elif Primary == "Kitty":                       
                                    ch_k "Hey[K_like]funny meeting you here."
                    elif Primary == "Emma":                       
                                    ch_e "I didn't expect to run into you here."
                    elif Primary == "Laura":                       
                                    ch_l "Oh, hey."
                    #end girls showed up to Rogues's room.    
                
        elif bg_current == "bg kitty":   
                    if Secondary:  
                            #if there's a second girl
                            "[Primary] and [Secondary] just entered the room."
                    else:
                            #if there's no second girl,
                            "[Primary] just entered the room."         
                    if Primary == "Kitty" or Secondary == "Kitty":
                                    if "angry" in K_DailyActions:
                                            call KittyFace("angry") 
                                            ch_k "You shouldn't be here right now." 
                                    elif Current_Time == "Night" and ApprovalCheck("Kitty", 1000, "LI") and ApprovalCheck("Kitty", 600, "OI"):
                                            ch_k "Oh, hey, it's kinds late, but you can stay for a bit."  
                                            $ Line = "stay"                     
                                    elif ApprovalCheck("Kitty", 1300) or ApprovalCheck("Kitty", 500, "O"):
                                            ch_k "Oh, hey, nice to see you."
                                            $ Line = "stay"
                                    elif Current_Time == "Night":
                                            ch_k "Oh, hey, [K_Petname]. It's kind of late, could you come back tomorrow?" 
                                    elif ApprovalCheck("Kitty", 600, "LI") or ApprovalCheck("Kitty", 300, "OI"):
                                            ch_k "Oh, hey, [K_Petname], what's up?"
                                            $ Line = "stay"
                                    else: 
                                            call KittyFace("confused") 
                                            ch_k "Hey, [K_Petname], what are you even doing here?"
                                            ch_k "Could you[K_like]get out?"  
                                    if Line != "stay":
                                        menu:
                                            extend ""
                                            "Sure, ok. [[you go]":
                                                        call Statup("Kitty", "Love", 80, 1)
                                                        call Statup("Kitty", "Obed", 50, 2)
                                                        call Statup("Kitty", "Inbt", 50, 2)  
                                                        ch_k "Thanks."
                                                        "You head back to your room."
                                            "Sorry, I'll go.":
                                                        call Statup("Kitty", "Love", 90, 2)
                                                        call Statup("Kitty", "Obed", 50, 3) 
                                                        call KittyFace("smile") 
                                                        ch_k "Thanks."
                                                        "You head back to your room."
                                            "Are you sure I can't stay?":
                                                        if "angry" in K_DailyActions:
                                                                call KittyFace("angry") 
                                                                ch_k "I think I said {i}NO!{/i}"                  
                                                        elif Current_Time == "Night" and ApprovalCheck("Kitty", 800, "LI") and ApprovalCheck("Kitty", 400, "OI"):
                                                                call KittyFace("sadside") 
                                                                ch_k "Maybe just this once. . ." 
                                                                $ Line = "stay"
                                                        elif Current_Time == "Night":
                                                                ch_k "Noooope. Try again tomorrow."                                                 
                                                        elif ApprovalCheck("Kitty", 750):
                                                                ch_k "Oh, fiiiine."
                                                                ch_k "Just for a little bit."
                                                                $ Line = "stay"
                                                        else: 
                                                                ch_k "Noooope."  
                                                        if Line != "stay":  
                                                                call Statup("Kitty", "Love", 80, -1)
                                                                call Statup("Kitty", "Inbt", 50, 3) 
                                                                "Kitty kicks you out of the room."                                                    
                                            "I'm sticking around, thanks.":   
                                                        if "angry" in K_DailyActions:
                                                                call KittyFace("angry") 
                                                                ch_k "Oh no you do not!"
                                                        elif not ApprovalCheck("Kitty", 1800) and not ApprovalCheck("Kitty", 500, "O"):
                                                                call KittyFace("angry") 
                                                                ch_k "Nooope, out!"
                                                        else:
                                                                call Statup("Kitty", "Obed", 80, 5)
                                                                call KittyFace("sad") 
                                                                ch_k ". . ." 
                                                                ch_k "Fine."
                                                                $ Line = "stay"
                                                        if Line != "stay":
                                                                call Statup("Kitty", "Love", 60, -5, 1)
                                                                call Statup("Kitty", "Love", 80, -5)
                                                                call Statup("Kitty", "Obed", 50, 2)
                                                                call Statup("Kitty", "Inbt", 60, 5) 
                                                                "Kitty kicks you out of the room."
                                    if Line != "stay":
                                            $ bg_current = "bg player"  
                                            jump Player_Room
                                            #End Kitty tells you to leave. 
                    elif Primary == "Rogue":                       
                                    ch_r "Sorry, I wasn't expecting to bump into you here."
                    elif Primary == "Emma":                       
                                    ch_e "I didn't expect to run into you here."
                    elif Primary == "Laura":                       
                                    ch_l "Oh, hey."
                    #end girls showed up to Kitty's room.
        elif bg_current == "bg emma": 
                    if Secondary:  
                            #if there's a second girl
                            "[Primary] and [Secondary] just entered the room."
                    else:
                            #if there's no second girl,
                            "[Primary] just entered the room."         
                    if Primary == "Emma" or Secondary == "Emma":
                                    if "angry" in E_DailyActions:
                                            call EmmaFace("angry") 
                                            ch_e "I don't think you should be here." 
                                    elif Current_Time == "Night" and ApprovalCheck("Emma", 1000, "LI") and ApprovalCheck("Emma", 600, "OI"):
                                            ch_e "Oh, it's a bit late, but you're welcome."  
                                            $ Line = "stay"                     
                                    elif ApprovalCheck("Emma", 1300) or ApprovalCheck("Emma", 500, "O"):
                                            ch_e "Oh, nice to see you."
                                            $ Line = "stay"
                                    elif Current_Time == "Night":
                                            ch_e "Oh, hello, [E_Petname]. It's a bit late, could you come back tomorrow?" 
                                    elif ApprovalCheck("Emma", 600, "LI") or ApprovalCheck("Emma", 300, "OI"):
                                            ch_e "Oh, hello, [E_Petname], can I help you with anything?"
                                            $ Line = "stay"
                                    else: 
                                            call EmmaFace("confused") 
                                            ch_e "Oh, hello, [E_Petname]?"
                                            ch_e "Did you have a reason to be visiting me?"  
                                    if Line != "stay":
                                        menu:
                                            extend ""
                                            "Sure, ok. [[you go]":
                                                        call Statup("Emma", "Love", 80, 1)
                                                        call Statup("Emma", "Obed", 50, 2)
                                                        call Statup("Emma", "Inbt", 50, 2)  
                                                        ch_e "Appreciated."
                                                        "You head back to your room."
                                            "Sorry, I'll go.":
                                                        call Statup("Emma", "Love", 90, 2)
                                                        call Statup("Emma", "Obed", 50, 3) 
                                                        call EmmaFace("smile") 
                                                        ch_e "Thank you."
                                                        "You head back to your room."
                                            "Are you sure I can't stay?":
                                                        if "angry" in E_DailyActions:
                                                                call EmmaFace("angry") 
                                                                ch_e "I believe I said {i}no.{/i}"                  
                                                        elif Current_Time == "Night" and ApprovalCheck("Emma", 800, "LI") and ApprovalCheck("Emma", 400, "OI"):
                                                                call EmmaFace("sadside") 
                                                                ch_e "Perhaps just this once. . ." 
                                                                $ Line = "stay"
                                                        elif Current_Time == "Night":
                                                                ch_e "I'm afraid not. Try again tomorrow."                                                 
                                                        elif ApprovalCheck("Emma", 750):
                                                                ch_e "Oh, very well. . ."
                                                                ch_e "Just for a little bit."
                                                                $ Line = "stay"
                                                        else: 
                                                                ch_e "Definitely not."    
                                                        if Line != "stay":
                                                                call Statup("Emma", "Love", 80, -1)
                                                                call Statup("Emma", "Inbt", 50, 3) 
                                                                "Emma kicks you out of the room."                                                    
                                            "I'm sticking around, thanks.":   
                                                        if "angry" in E_DailyActions:
                                                                call EmmaFace("angry") 
                                                                ch_e "You must be joking."
                                                        elif not ApprovalCheck("Emma", 1800) and not ApprovalCheck("Emma", 500, "O"):
                                                                call EmmaFace("angry") 
                                                                ch_e "No, get out."
                                                        else:
                                                                call Statup("Emma", "Obed", 80, 5)
                                                                call EmmaFace("sad") 
                                                                ch_e ". . ." 
                                                                ch_e "Fine."
                                                                $ Line = "stay"
                                                        if Line != "stay":
                                                                call Statup("Emma", "Love", 60, -5, 1)
                                                                call Statup("Emma", "Love", 80, -5)
                                                                call Statup("Emma", "Obed", 50, 2)
                                                                call Statup("Emma", "Inbt", 60, 5) 
                                                                "Emma kicks you out of the room."
                                    if Line != "stay":
                                            $ bg_current = "bg player"  
                                            jump Player_Room
                                            #End Emma tells you to leave. 
                    elif Primary == "Rogue":                       
                                    ch_r "Sorry, I wasn't expecting to bump into you here."
                    elif Primary == "Kitty":                       
                                    ch_k "Hey[K_like]funny meeting you here."
                    elif Primary == "Laura":                       
                                    ch_l "Oh, hey."
                    #end girls showed up to Emma's room.                
        elif bg_current == "bg laura": 
                    if Secondary:  
                            #if there's a second girl
                            "[Primary] and [Secondary] just entered the room."
                    else:
                            #if there's no second girl,
                            "[Primary] just entered the room."         
                    if Primary == "Laura" or Secondary == "Laura":
                                    if "angry" in L_DailyActions:
                                            call LauraFace("angry") 
                                            ch_l "You should get away while you can." 
                                    elif Current_Time == "Night" and ApprovalCheck("Laura", 1000, "LI") and ApprovalCheck("Laura", 600, "OI"):
                                            ch_l "It's late."  
                                            $ Line = "stay"                     
                                    elif ApprovalCheck("Laura", 1300) or ApprovalCheck("Laura", 500, "O"):
                                            ch_l "Oh, hey."
                                            $ Line = "stay"
                                    elif Current_Time == "Night":
                                            ch_l "Oh, hey, it's late." 
                                    elif ApprovalCheck("Laura", 600, "LI") or ApprovalCheck("Laura", 300, "OI"):
                                            ch_l "Oh, hey, [L_Petname]."
                                            $ Line = "stay"
                                    else: 
                                            call LauraFace("confused") 
                                            ch_l "Hey, [L_Petname], why are you here?"
                                    if Line != "stay":
                                        menu:
                                            extend ""
                                            "Sorry, I'll go.":
                                                        call Statup("Laura", "Love", 90, 2)
                                                        call Statup("Laura", "Obed", 50, 3) 
                                                        call LauraFace("smile") 
                                                        ch_l "Thanks."
                                                        "You head back to your room."
                                            "Can I stay?":
                                                        if "angry" in L_DailyActions:
                                                                call LauraFace("angry") 
                                                                ch_l "[[growls] . . .You probably shouldn't."                  
                                                        elif Current_Time == "Night" and ApprovalCheck("Laura", 800, "LI") and ApprovalCheck("Laura", 400, "OI"):
                                                                call LauraFace("sadside") 
                                                                ch_l "I guess. . ." 
                                                                $ Line = "stay"
                                                        elif Current_Time == "Night":
                                                                ch_l "No. Maybe tomorrow."                                                 
                                                        elif ApprovalCheck("Laura", 750):
                                                                ch_l "Ok."
                                                                ch_l "Just for a minute."
                                                                $ Line = "stay"
                                                        else: 
                                                                ch_l "No."  
                                                        if Line != "stay":  
                                                                call Statup("Laura", "Love", 80, -1)
                                                                call Statup("Laura", "Inbt", 50, 3) 
                                                                "Laura kicks you out of the room."                                                    
                                            "I'm sticking around.":   
                                                        if "angry" in L_DailyActions:
                                                                call LauraFace("angry") 
                                                                ch_l "You really shouldn't."
                                                        elif not ApprovalCheck("Laura", 1800) and not ApprovalCheck("Laura", 500, "O"):
                                                                call LauraFace("angry") 
                                                                ch_l "No."
                                                        else:
                                                                call Statup("Laura", "Obed", 80, 5)
                                                                call LauraFace("sad") 
                                                                ch_l ". . ." 
                                                                $ Line = "stay"
                                                        if Line != "stay":
                                                                call Statup("Laura", "Love", 60, -5, 1)
                                                                call Statup("Laura", "Love", 80, -5)
                                                                call Statup("Laura", "Obed", 50, 2)
                                                                call Statup("Laura", "Inbt", 60, 5) 
                                                                "Laura kicks you out of the room."
                                    if Line != "stay":
                                            $ bg_current = "bg player"  
                                            jump Player_Room
                                            #End Laura tells you to leave. 
                    elif Primary == "Rogue":                       
                                    ch_r "Sorry, I wasn't expecting to bump into you here."
                    elif Primary == "Kitty":                       
                                    ch_k "Hey[K_like]funny meeting you here."
                    elif Primary == "Emma":                       
                                    ch_e "I didn't expect to run into you here."
                    #end girls showed up to Laura's room.
        elif bg_current == "bg classroom":  

                
                
                #if this is triggered, Adjacent should never be higher than 1. 
                #adjacent characters who are neither Primary nor secondary should have been removed from adjacency

                if Secondary:  
                        #if there's a second girl
                        "[Primary] and [Secondary] just entered the room."
                else:
                        #if there's no second girl,
                        "[Primary] just entered the room."       
                        
                if Primary == "Rogue" or Secondary == "Rogue":
                                ch_r "Hey, [R_Petname]."
                if Primary == "Kitty" or Secondary == "Kitty":
                                ch_k "Oh, hey."
                if Primary == "Emma" or Secondary == "Emma":
                                ch_e "Oh, hello, [E_Petname]."
                if Primary == "Laura" or Secondary == "Laura":
                                ch_l "Hey."     
                            
                            
                $ Line = 0
                $ D20 = renpy.random.randint(1, 20)
                
                if Primary and Primary != "Emma":                
                        #Determines who sits next to you
                        if ApprovalCheck(Primary, 1000): 
                            if len(Adjacent) < 2 and D20 >= 10:
                                    $Line = Primary + " takes the seat next to you"
                                    $ Adjacent.append(Primary)
                            else:
                                    $Line = Primary + " sits across the room from you"
                                    $ Nearby.append(Primary)
                        else:
                                $Line = Primary + " sits across the room from you"
                                $ Nearby.append(Primary)
                if Secondary and Secondary != "Emma":                
                        #Determines who sits next to you
                        if Primary == "Emma":
                            $ Line = "Emma walks over and stands near you"
                        if ApprovalCheck(Secondary, 1000): 
                            if len(Adjacent) < 2 and D20 >= 10:
                                #changes dialog based on whether she does the same or differently than the last person
                                if Primary in Adjacent and Primary != "Emma":
                                    $Line = Primary + " and " + Secondary + " sit down next to you"
                                else:
                                    $Line = Line + ", while " + Secondary + " takes the seat next to you"
                                $ Adjacent.append(Secondary)
                            else:
                                if Primary in Nearby and Primary != "Emma":
                                    $Line = Primary + " and " + Secondary + " sit across the room from you"
                                else:
                                    $Line = Line + ", while " + Secondary + " sits across the room from you"
                                $ Nearby.append(Secondary)
                        else:
                                if Primary in Nearby and Primary != "Emma":
                                    $Line = Primary + " and " + Secondary + " sit across the room from you"
                                else:
                                    $Line = Line + ", while " + Secondary + " sits across the room from you"
                                $ Nearby.append(Secondary)
                if Line:
                    "[Line]."
                                    
                if E_Loc == "bg teacher":
                        "Emma takes her position behind the podium."                    
                #end girls showed up to class
        elif bg_current == "bg dangerroom":   
                if Secondary:  
                        #if there's a second girl
                        "[Primary] and [Secondary] just entered the room."
                else:
                        #if there's no second girl,
                        "[Primary] just entered the room."   
                #end girls showed up to the Danger Room
        elif bg_current == "bg campus":   
                if Secondary:  
                        #if there's a second girl
                        "[Primary] and [Secondary] just entered the square."
                else:
                        #if there's no second girl,
                        "[Primary] just entered the square."   
                #end girls showed up to the campus
        else: #if it's anywhere else,   
                if Secondary:  
                        #if there's a second girl
                        "[Primary] and [Secondary] just entered the room."
                else:
                        #if there's no second girl,
                        "[Primary] just entered the room."  
                #end girls showed up someplace
                                    
        if bg_current in ("bg campus","bg dangerroom"):
            if Primary == "Rogue" or Secondary == "Rogue":
                            ch_r "Hey, [R_Petname]."
            if Primary == "Kitty" or Secondary == "Kitty":
                            ch_k "Oh, hey."
            if Primary == "Emma" or Secondary == "Emma":
                            ch_e "Oh, hello, [E_Petname]."
            if Primary == "Laura" or Secondary == "Laura":
                            ch_l "Hey."                          
        #end "girls showed up"    
        
        
        if "Rogue" in Nearby:
                $ R_Loc = "nearby"
        if "Kitty" in Nearby:
                $ K_Loc = "nearby"   
        if "Laura" in Nearby:
                $ L_Loc = "nearby"
                
        call Present_Check #updates who is present  
        if Nearby:
                "There were some others as well, but they kept their distance." 
        return
# End Girls Arrive / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        
label Locked_Door(Girl=0):
        # called when a girl tries to enter a locked room, mainly from the summon function
        # Girl is the indicated girl
        
        if Girl == "Kitty":
                "You look to the door just as Kitty phases into the room."
                $ K_Loc = bg_current 
                call KittyOutfit
                call Display_Kitty
                ch_k "Hi, [K_Petname]!"
                return

        if Girl == "Rogue":
            if R_Loc == "bg rogue":
                "You hear a key in the lock, and Rogue enters the room." 
            else:    
                "The doorknob jiggles. A moment later, you hear a knock."
                ch_r "Could I come in, [R_Petname]?"
                menu:
                    extend ""
                    "Open door":
                            ch_p "Hold on, Rogue!" 
                            "You unlock the door and let her in."
                            $ R_Loc = bg_current 
                            call RogueOutfit
                    "Send her away":
                            ch_p "Er, sorry, could you come back later?"
                            call Statup("Rogue","Love", 80, -2)
                            ch_r "C'mon, [R_Petname], don't yank my chain like this!"
                            if R_Loc == bg_current:
                                call Remove_Girl("Rogue")
                            return
        elif Girl == "Emma":      
            if E_Loc == "bg emma" or E_Loc:
                "You hear a key in the lock, and Emma enters the room." 
            else:    
                "The doorknob jiggles. A moment later, you hear a knock."  
                ch_e "[E_Petname], I'm waiting."
                menu:
                    extend ""
                    "Open door":
                            ch_p "Hold on, [EmmaName]!" 
                            "You unlock the door and let her in."
                            $ E_Loc = bg_current 
                            call EmmaOutfit
                    "Send her away":
                            ch_p "Er, sorry, could you come back later?"
                            call Statup("Emma","Obed", 80, -2)
                            ch_e "I have to say, [E_Petname], I understand the appeal of having someone at your beck and call. . ."
                            call Statup("Emma","Love", 80, -2)
                            ch_e "but I don't appreciate being on the receiving end!"
                            if E_Loc == bg_current:
                                call Remove_Girl("Emma")
                            return
        elif Girl == "Laura":
            if L_Loc == "bg laura":
                "You hear a key in the lock, and Laura enters the room." 
            else:    
                "The doorknob jiggles. A moment later, you hear a knock."
                ch_l "It's me."
                menu:
                    extend ""
                    "Open door":
                            "You walk over to the door and open it."
                            ch_p "Come on in, [LauraName]."
                            $ L_Loc = bg_current 
                            call LauraOutfit
                    "Send her away":
                        ch_p "Er, sorry, could you come back later?"
                        "Laura goes quiet."
                        if ApprovalCheck("Laura", 500,"I") and not ApprovalCheck("Laura", 500,"O"):
                                $ L_Loc = bg_current 
                                call LauraOutfit
                                $ Laura_Arms = 2
                                $ L_Claws = 1
                                "snickt"
                                call Display_Laura
                                "The door swings open."
                                call Statup("Laura", "Love", 80, -2)
                                call Statup("Laura", "Obed", 80, -4)
                                $ L_Claws = 0
                                ch_l "Hey, so I don't like being jerked around, so don't do that, okay?"
                        else:
                                call Statup("Laura", "Love", 80, -3)
                                call Statup("Laura", "Obed", 80, 3)
                                ch_l "Ok."
                                "You hear her shuffling off."
                                if L_Loc == bg_current:
                                    call Remove_Girl("Laura")
                                return
         
        if "locked" in P_Traits:         
                $ P_Traits.remove("locked")
        call Set_The_Scene(1,0,0,0)#characters, no entry, no clothes changes, no triggers
        return
#End Locked door responses / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        
    
# Start Last Namer / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label LastNamer(NameTemp = Playername, Wordcount = 0, Splitname = 0, Lastname = 0):
        # Wordcount = number of words
        $ Wordcount = Playername.count(" ")
        
        # Splitname turns the name into a list, ie [Charles, Francis, Xavier]
        $ Splitname = Playername.split()
        
        # Lastname picks the last word in that set
        $ Lastname = "Mr. " + Splitname[Wordcount]
        return Lastname
    
# End Last Namer / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 


# Start LikeUpdater / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 

label LikeUpdater(Primary = "Rogue", Value = 1, Noticed = 1):
    # call LikeUpdater("Rogue",1)
    # Primary is the primary girl in action, Value is the amount added/subtracted
    # Noticed is whether it matters if she notices or not.
                  
    if Primary == "Rogue":
            if K_Loc == bg_current:
                if not Noticed or "noticed Rogue" in K_RecentActions: 
                    #If Kitty was participating in Rogue's activity
                    $ K_LikeRogue += Value
                    $ R_LikeKitty += Value
    
            if E_Loc == bg_current:
                if not Noticed or "noticed Rogue" in E_RecentActions: 
                    #If Emma was participating in Rogue's activity
                    $ E_LikeRogue += Value
                    $ R_LikeEmma += Value
            
            if L_Loc == bg_current:
                if not Noticed or "noticed Rogue" in L_RecentActions: 
                    #If Laura was participating in Rogue's activity
                    $ L_LikeRogue += Value
                    $ R_LikeLaura += Value
                    
    elif Primary == "Kitty":
            if R_Loc == bg_current:
                if not Noticed or "noticed Kitty" in R_RecentActions: 
                    #If Rogue was participating in Kitty's activity
                    $ R_LikeKitty += Value
                    $ K_LikeRogue += Value
            
            if E_Loc == bg_current:
                if not Noticed or "noticed Kitty" in E_RecentActions: 
                    #If Emma was participating in Kitty's activity
                    $ E_LikeRogue += Value
                    $ K_LikeEmma += Value
                    
            if L_Loc == bg_current:
                if not Noticed or "noticed Kitty" in L_RecentActions: 
                    #If Laura was participating in Kitty's activity
                    $ L_LikeKitty += Value
                    $ K_LikeLaura += Value                    
                    
    elif Primary == "Emma":
            if R_Loc == bg_current:
                if not Noticed or "noticed Emma" in R_RecentActions: 
                    #If Rogue was participating in Emma's activity
                    $ R_LikeEmma += Value
                    $ E_LikeRogue += Value
            
            if K_Loc == bg_current:
                if not Noticed or "noticed Emma" in K_RecentActions: 
                    #If Kitty was participating in Emma's activity
                    $ K_LikeEmma += Value
                    $ E_LikeRogue += Value
                    
            if L_Loc == bg_current:
                if not Noticed or "noticed Emma" in L_RecentActions: 
                    #If Laura was participating in Emma's activity
                    $ L_LikeEmma += Value
                    $ E_LikeLaura += Value
                    
    elif Primary == "Laura":
            if R_Loc == bg_current:
                if not Noticed or "noticed Laura" in R_RecentActions: 
                    #If Rogue was participating in Laura's activity
                    $ R_LikeLaura += Value
                    $ L_LikeRogue += Value
            
            if K_Loc == bg_current:
                if not Noticed or "noticed Laura" in K_RecentActions: 
                    #If Kitty was participating in Laura's activity
                    $ K_LikeLaura += Value
                    $ L_LikeRogue += Value
                    
            if E_Loc == bg_current:
                if not Noticed or "noticed Laura" in E_RecentActions: 
                    #If Emma was participating in Laura's activity
                    $ E_LikeLaura += Value
                    $ L_LikeEmma += Value
    
    return
    
# End LikeUpdater / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 


label Girls_Noticed(Primary=0):
    #Checks to see if some other girl noticed the primary in action.
    if not Primary:
                "Tell Oni that in noticed, no primary is set."
                return
    if R_Loc == bg_current and Primary != "Rogue":
                call Rogue_Noticed(Primary)
    if K_Loc == bg_current and Primary != "Kitty":
                call Kitty_Noticed(Primary)
    if E_Loc == bg_current and Primary != "Emma":
                call Emma_Noticed(Primary)
    if L_Loc == bg_current and Primary != "Laura":
                call Laura_Noticed(Primary)
    return

label Girls_Taboo(Primary=0):
    #Checks to see if they trigger a taboo situation
    if not Primary:
                "Tell Oni that in taboo, no primary is set."
    elif Primary == "Rogue":
                call Rogue_Taboo
    elif Primary == "Kitty":
                call Kitty_Taboo
    elif Primary == "Emma":
                call Emma_Taboo
    elif Primary == "Laura":
                call Laura_Taboo
    return
    

label Add_Poly(Girl=0,Other=0,Type=0,Check=0,Trait=0):
    # Type would either be "poly " or "saw with "
    # call Add_Poly("Rogue","Kitty","poly ",1)
    # the above would check to see if Rogue had the "poly Kitty" trait. 
    $ Trait = Type + Other
#    if Other == "Rogue":
#            $ Trait = Type + "rogue"
#    elif Other == "Kitty":
#            $ Trait = Type + "kitty"
#    elif Other == "Emma":
#            $ Trait = Type + "emma"
#    elif Other == "Laura":
#            $ Trait = Type + "laura"
    # end Trait setting        
    
    # start Trait writing/checking
    if Girl == "Rogue":
            if Trait not in R_Traits: #ie "poly Rogue"
                    $ R_Traits.append(Trait) 
            elif Check:
                    return 1
    elif Girl == "Kitty":
            if Trait not in K_Traits: #ie "poly Rogue"
                    $ K_Traits.append(Trait) 
            elif Check:
                    return 1
    elif Girl == "Emma":
            if Trait not in E_Traits: #ie "poly Rogue"
                    $ E_Traits.append(Trait) 
            elif Check:
                    return 1
    elif Girl == "Laura":
            if Trait not in L_Traits: #ie "poly Rogue"
                    $ L_Traits.append(Trait) 
            elif Check:
                    return 1
    
    return 0
                
                
    
label Sex_Menu_Threesome(Girl=0):
        if not Girl:
            return
        menu:          
            "Do you want to join us Rogue?" if R_Loc == bg_current and Girl != "Rogue":
                    if Partner == "Rogue":
                        #if she's already involved
                        ch_r "If I'd been do'in it right you wouldn't hafta ask. . ."
                    else: 
                        call Rogue_Noticed(Girl,1)
                        if R_Loc == bg_current:
                            ch_r "I s'pose I could lend a hand . ."
                        else:
                            "She seems uncomfortable with this situation and leaves the room." 
                            
            "Do you want to join us Kitty?" if K_Loc == bg_current and Girl != "Kitty":
                    if Partner == "Kitty":
                        #if she's already involved
                        ch_k "Lol, what are you even talking about?"
                    else: 
                        call Kitty_Noticed(Girl,1)
                        if K_Loc == bg_current:
                            ch_k "I could[K_like]give it a try. . ."
                        else:
                            "She seems uncomfortable with this situation and leaves the room." 
                            
            "Do you want to join us Emma?" if E_Loc == bg_current and Girl != "Emma":
                    if Partner == "Emma":
                        #if she's already involved
                        ch_e "Have I not been keeping up?"
                    else: 
                        call Emma_Noticed(Girl,1)
                        if E_Loc == bg_current:
                            ch_e "So what did you have in mind for us. . ."
                        else:
                            "She seems uncomfortable with this situation and leaves the room." 
                                        
            "Do you want to join us Laura?" if L_Loc == bg_current and Girl != "Laura":
                    if Partner == "Laura":
                        #if she's already involved
                        ch_l "I already am."
                    else: 
                        call Laura_Noticed(Girl,1)
                        if L_Loc == bg_current:
                            ch_l "Hm, ok. . ."
                        else:
                            "She seems uncomfortable with this situation and leaves the room." 
                            
            "Switch lead girl." if Partner:
                    if Partner == "Rogue":
                        call Rogue_SexAct("switch")
                    if Partner == "Kitty":
                        call Kitty_SexAct("switch")
                    if Partner == "Emma":
                        call Emma_SexAct("switch")
                    if Partner == "Laura":
                        call Laura_SexAct("switch")
                        
            "Never mind [[something else]":
                pass
        return
                       
label Partner_Threechange(Girl=0):  
        # this routine thorws it to the specific character's threresome activity change
        # Girl is the lead of the encounter, this is called from Threesome actions during sex scenes
        if Partner == Girl:
                "Let Oni know that both roles are set to [Girl]."
                return
        if Partner == "Rogue":
                call Rogue_Three_Change(Girl)        
        elif Partner == "Kitty":
                call Kitty_Three_Change(Girl)
        elif Partner == "Emma":
                call Emma_Three_Change(Girl) 
        elif Partner == "Laura":
                call Laura_Three_Change(Girl) 
        return
    
label Partner_Cleanup:
        # this routine checks if the Partner has jiz on her, and cleans up if yes
        # this is called from Threesome actions during sex scenes
        if not Partner:
                return
        if Partner == "Rogue" and R_Spunk:
                call Rogue_Cleanup("ask")  
        elif Partner == "Kitty" and K_Spunk:
                call Kitty_Cleanup("ask")    
        elif Partner == "Emma" and E_Spunk:
                call Emma_Cleanup("ask")  
        elif Partner == "Laura" and L_Spunk:
                call Laura_Cleanup("ask")  
        else:
                "She seems fine."
        return
    
label Partner_Undress:   
        # this routine undresses the partner in a scene
        # this is called from Threesome actions during sex scenes 
        if Partner == "Rogue":
                call R_Undress   
        elif Partner == "Kitty":
                call K_Undress   
        elif Partner == "Emma":
                call E_Undress 
        elif Partner == "Laura":
                call L_Undress
        return
    
label Partner_Cumming(Girl=0):
        # this routine is called if the Partner might cum
        #Girl would be the non-Partner
        if R_Lust >= 100 and R_Loc == bg_current and Girl != "Rogue":                                          
            call R_Cumming
        if K_Lust >= 100 and K_Loc == bg_current and Girl != "Kitty":                                          
            call K_Cumming
        if E_Lust >= 100 and E_Loc == bg_current and Girl != "Emma":                                          
            call E_Cumming     
        if L_Lust >= 100 and L_Loc == bg_current and Girl != "Laura":                                          
            call L_Cumming    
        return

label Partner_Like(Girl=0,Value=1,AltValue=1,Measure=800,Backsies=0,Partner=Partner):
        # Thi raises a partner's "like" stat by an amount
        # call Partner_Like("Rogue",2)
        # Girl is the lead, Partner is the second girl
        # Value is the amount it changes if Measure is met, otherwise AltValue
        # Set Backsies to 1, or this will looptwice to cover both girls equally
        
        if not Girl or not Partner:
                return
                
        if Trigger4:
                # if the Partner is doing a secondary action. . .
                if Trigger4 == "watch":
                        pass
                elif Trigger4 in ("hand","blow"):
                        $ Value += 1
                elif Trigger4 in ("lick pussy","lick ass"):
                        $ Value += 3                
                else:
                        $ Value += 2
#                if not Backsies:        #I can remove this if the other way works
#                        # this bit causes the function to go through a second cycle, 
#                        # skipping this bit and then returning here
#                        # the point is to give points going the opposite direction
#                        $ Backsies = Partner 
#                        $ Partner = Girl 
#                        $ Girl = Backsies
#                        call Partner_Like(Girl,Value,AltValue)                        
#                        $ Backsies = Partner
#                        $ Partner = Girl
#                        $ Girl = Backsies 
        #End Trigger4 bonuses
            
        if Girl == "Rogue":
                if Partner == "Kitty": 
                        #If Kitty was participating
                        $ K_LikeRogue += Value if K_LikeRogue >= Measure else AltValue
                elif Partner == "Emma":  
                        #If Emma was participating
                        $ E_LikeRogue += Value if E_LikeRogue >= Measure else AltValue
                elif Partner == "Laura":  
                        #If Laura was participating
                        $ L_LikeRogue += Value if L_LikeRogue >= Measure else AltValue
        elif Girl == "Kitty":
                if Partner == "Rogue": 
                        #If Kitty was participating
                        $ R_LikeKitty += Value if R_LikeKitty >= Measure else AltValue
                elif Partner == "Emma":  
                        #If Emma was participating
                        $ E_LikeKitty += Value if E_LikeKitty >= Measure else AltValue
                elif Partner == "Laura":  
                        #If Laura was participating
                        $ L_LikeKitty += Value if L_LikeKitty >= Measure else AltValue
        elif Girl == "Emma":
                if Partner == "Rogue":  
                        #If Emma was participating
                        $ R_LikeEmma += Value if R_LikeEmma >= Measure else AltValue
                elif Partner == "Kitty": 
                        #If Kitty was participating
                        $ K_LikeEmma += Value if K_LikeEmma >= Measure else AltValue
                elif Partner == "Laura":  
                        #If Laura was participating
                        $ L_LikeEmma += Value if L_LikeEmma >= Measure else AltValue
        elif Girl == "Laura":
                if Partner == "Rogue":  
                        #If Emma was participating
                        $ R_LikeLaura += Value if R_LikeLaura >= Measure else AltValue
                elif Partner == "Kitty": 
                        #If Kitty was participating
                        $ K_LikeLaura += Value if K_LikeLaura >= Measure else AltValue
                elif Partner == "Emma":  
                        #If Emma was participating
                        $ E_LikeLaura += Value if E_LikeLaura >= Measure else AltValue
        
        if not Backsies:        
                        # this bit causes the function to go through a second cycle, 
                        # skipping this bit and then returning here
                        # the point is to give points going the opposite direction
                        $ Backsies = Partner 
                        $ Partner = Girl 
                        $ Girl = Backsies
                        call Partner_Like(Girl,Value,AltValue,Backsies=Backsies)  
                        $ Partner = Girl
                        
        return
#End Partner_Like
    


        
# Start Lesbian Jumping check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label LesCheck(Girls=[]):
        #Checks if any girls will jump each other behind the scenes. . . 
        # They will if they have over 500 Inbt and are thirsty
        if "touch" in R_Traits and ApprovalCheck("Rogue", 500, "I") and R_Thirst >= 30: #and "refused" not in R_DailyActions:
                if ("mono" not in R_Traits or R_Break[0]) and "Rogue" not in Party:
                    $ Girls.append("Rogue")      
                    if R_Thirst >= 60:
                            $ Girls.append("Rogue")      
                if R_Thirst >= 90:
                        $ Girls.append("Rogue")     
        if ApprovalCheck("Kitty", 500, "I") and K_Thirst >= 30 and "met" in K_History:
                if ("mono" not in K_Traits or K_Break[0]) and "Kitty" not in Party:
                    $ Girls.append("Kitty")   
                    if K_Thirst >= 60:
                            $ Girls.append("Kitty")      
                if K_Thirst >= 90:
                        $ Girls.append("Kitty")     
        if ApprovalCheck("Emma", 500, "I") and E_Thirst >= 30 and "met" in E_History:
                if "threecheck" not in E_History:  
                        if ApprovalCheck("Emma", 800, "I"):
                                #this addes threecheck if she's really slutty
                                $ E_History.append("threecheck")                                 
                if "threecheck" in E_History: 
                        if ("mono" not in E_Traits or E_Break[0]) and "Emma" not in Party:
                            $ Girls.append("Emma")  
                            if E_Thirst >= 60:
                                    $ Girls.append("Emma")      
                        if E_Thirst >= 90:
                                $ Girls.append("Emma")      
        if ApprovalCheck("Laura", 500, "I") and L_Thirst >= 30 and "met" in L_History:
                if ("mono" not in L_Traits or L_Break[0]) and "Laura" not in Party:
                    $ Girls.append("Laura")   
                    if L_Thirst >= 60:
                            $ Girls.append("Laura")      
                if L_Thirst >= 90:
                        $ Girls.append("Laura")                     
        
        if not Girls:
            return
            
        $ renpy.random.shuffle(Girls)   
#        $ Lead = Girls[0] #sets lead girl to the first one in the list
        
        $ Partner = 0
        while len(Girls) > 2:
                # So long as the list has two people in it, check to see if the second girl is viable
                # if not, remove her and try again                
                if Partner:
                        # if a partner's been picked, cull out the 3+ girls
                        $ Girls.remove(Girls[2])                    
                elif (Girls[1] in P_Harem and Girls[0] in P_Harem) and GirlLikeCheck(Girls[0],Girls[1]) >= 600: 
                        $ Partner = Girls[1]
                elif GirlLikeCheck(Girls[1],Girls[0]) >= 800 and GirlLikeCheck(Girls[0],Girls[1]) >= 800: 
                        $ Partner = Girls[1]
                elif ApprovalCheck(Girls[1], 0, "TRST") >= 90 and GirlLikeCheck(Girls[0],Girls[1]) >= 600: 
                        $ Partner = Girls[1]
                else:   
                        #if not picked, remove this girl from the list
                        $ Girls.remove(Girls[1])
        if not Partner:
                # if nobody is picked, then return, otherwise you should have at least two girls picked
                return
                
        $ Partner = 0
        #move both girls into the same room   
        if "Rogue" in Girls and bg_current != "bg rogue":
                $ R_Loc = "bg rogue"
                if "Kitty" in Girls:
                        $ K_Loc = "bg rogue"
                if "Emma" in Girls:
                        $ E_Loc = "bg rogue"
                if "Laura" in Girls:
                        $ L_Loc = "bg rogue"  
        elif "Kitty" in Girls and bg_current != "bg kitty":
                $ K_Loc = "bg kitty"
                if "Rogue" in Girls:
                        $ R_Loc = "bg kitty"
                if "Emma" in Girls:
                        $ E_Loc = "bg kitty"
                if "Laura" in Girls:
                        $ L_Loc = "bg kitty" 
        elif "Emma" in Girls and bg_current != "bg emma":
                $ E_Loc = "bg emma"
                if "Rogue" in Girls:
                        $ R_Loc = "bg emma"
                if "Kitty" in Girls:
                        $ K_Loc = "bg emma"
                if "Laura" in Girls:
                        $ L_Loc = "bg emma" 
        elif "Laura" in Girls and bg_current != "bg laura":
                $ L_Loc = "bg laura"
                if "Rogue" in Girls:
                        $ R_Loc = "bg laura"
                if "Kitty" in Girls:
                        $ K_Loc = "bg laura"
                if "Emma" in Girls:
                        $ E_Loc = "bg laura"
             
        call AnyWord(Girls[0],1,"les") #adds "les" to recent actions for both girls
        call AnyWord(Girls[1],1,"les") 
        
        call GirlLikesGirl(Girls[0],Girls[1],700,15,1) #Like +15 if under 700
        call GirlLikesGirl(Girls[1],Girls[0],700,15,1)
        
        call GirlLikesGirl(Girls[0],Girls[1],900,10,1) #Like +10 if under 900
        call GirlLikesGirl(Girls[1],Girls[0],900,10,1)
        
        call GirlLikesGirl(Girls[0],Girls[1],1000,5,1) #Like +5 if under 1000
        call GirlLikesGirl(Girls[1],Girls[0],1000,5,1)
                
        call DrainWord(Girls[0],"arriving",1,0) #removes "arriving" from recent  
        call DrainWord(Girls[1],"arriving",1,0) #removes "arriving" from recent  
        
        call Statup(Girls[0], "Lust", 60, 20) 
        call Statup(Girls[1], "Lust", 60, 20) 
                
        if "Rogue" in Girls: 
                    #if she had a lesbian encounter without you. . .
                    $ R_Thirst -= 5 
        if "Kitty" in Girls:
                    $ K_Thirst -= 5 
        if "Emma" in Girls:
                    $ E_Thirst -= 5 
        if "Laura" in Girls:
                    $ L_Thirst -= 5 
                
        return
# end Les_Check, checking to see if the girls jump each other
       
# Start Jumping check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label JumperCheck(Girls=[]):
        #decides whether a girl wants to jump you unexpectedly
        if "nope" in P_RecentActions:
                #if you refused sex. . .
                return
        if R_Action and R_Thirst >= 30 and ApprovalCheck("Rogue", 500, "I") and "refused" not in R_DailyActions:
                if "chill" not in R_Traits and "Rogue" not in P_DailyActions:
                    if renpy.random.randint(0,3) > 1:
                            $ Girls.append("Rogue")      
                    if R_Thirst >= 60:
                            $ Girls.append("Rogue")      
                if R_Thirst >= 90:
                        $ Girls.append("Rogue")     
        if K_Action and K_Thirst >= 30 and ApprovalCheck("Kitty", 500, "I") and "refused" not in K_DailyActions and "met" in K_History:
                if "chill" not in K_Traits and "Kitty" not in P_DailyActions:
                    if renpy.random.randint(0,3) > 1:
                            $ Girls.append("Kitty")   
                    if K_Thirst >= 60:
                            $ Girls.append("Kitty")      
                if K_Thirst >= 90:
                        $ Girls.append("Kitty")     
        if E_Action and E_Thirst >= 30 and ApprovalCheck("Emma", 500, "I") and "refused" not in E_DailyActions and "met" in E_History:
                if "chill" not in E_Traits and "Emma" not in P_DailyActions and E_Loc != "bg teacher":
                    # I rule out if she is teaching, she won't jump you. . .
                    if renpy.random.randint(0,3) > 1:
                            $ Girls.append("Emma")  
                    if E_Thirst >= 60:
                            $ Girls.append("Emma")      
                if E_Thirst >= 90:
                        $ Girls.append("Emma")      
        if L_Action and L_Thirst >= 30 and ApprovalCheck("Laura", 500, "I") and "refused" not in L_DailyActions and "met" in L_History:
                if "chill" not in L_Traits and "Laura" not in P_DailyActions:
                    if renpy.random.randint(0,3) > 1:
                            $ Girls.append("Laura")   
                    if L_Thirst >= 60:
                            $ Girls.append("Laura")      
                if L_Thirst >= 90:
                        $ Girls.append("Laura")                     
        
        if not Girls:
            return
            
        if len(Girls) >= 2:
            $ renpy.random.shuffle(Girls)                
            while len(Girls) >= 2 and Girls[0] == Girls[1]:
                    $ Girls.remove(Girls[1])    #removes duplicates
                    #$ del Girls[1]     
            while len(Girls) > 2:
                    $ Girls.remove(Girls[2])    #removes any over 2
                    
        $ Partner = 0
        if len(Girls) >= 2:        
            #if there are two girls, it adds the second as a potential partner
            if Girls[0] in P_Harem and Girls[1] in P_Harem:
                    $ Partner = Girls[1]
            elif GirlLikeCheck(Girls[0],Girls[1]) >= 800 and GirlLikeCheck(Girls[1],Girls[0]) >= 800:
                    $ Partner = Girls[1]
        
        call Jumped #Launches the main event        
        
        if "nope" in P_RecentActions:
                #if you refused sex. . .
                while Girls:         #clears list           
                    call Remove_Girl(Girls[0])
                    $ Girls.remove(Girls[0])                        
                jump Misplaced
        elif Girls:
                #if you had some sort of sexual encounter, it will hop you to the appropriate sex menu
                if Zero_Loc(Girls[0]) == bg_current:
                        call expression Girls[0] + "_SexMenu" #call Rogue_SexMenu 
        
        if bg_current == "bg player":
                #if it jumped to your room. . .
                jump Player_Room
        return      
#End Jumper_Check, checking to see if a girl wants to jump you

label Jumped(Initial=0,Act=0):    
        # called by JumperCheck if a girl jumps you
        # Girl is the girl, Intitial is the first initial of her name        
        # make sure that this puts people in the right rooms after they do stuff. . .
        
        if Girls[0] == "Emma" and Partner and "three" not in E_History:
                    #if lead is Emma, there is a partner, but she doesn't share. . .
                    $ Girls.remove(Partner) 
                    $ Partner = 0  
        elif "Emma" in Girls and ((Taboo and "taboo" not in E_History) or "three" not in E_History):
                    #if partner is Emma and she doesn't share. . .
                    $ Girls.remove("Emma") 
                    $ Partner = 0        
        
        if not Girls:
                return
                
        if Zero_Loc(Girls[0]) != bg_current and "locked" in P_Traits:
            #if the girl is not in the room with you, and your door is locked. . .            
            call Locked_Door(Girls[0])
            if not Girls or Zero_Loc(Girls[0]) != bg_current:
                    #if you refused her entry. . .
                    $ P_RecentActions.append("nope")      
                    return     
                                        
        #sets their location
        if "Rogue" in Girls:
                $ R_Loc = bg_current
        if "Kitty" in Girls:
                $ K_Loc = bg_current
        if "Emma" in Girls:
                $ E_Loc = bg_current
        if "Laura" in Girls:
                $ L_Loc = bg_current  
                
        call Taboo_Level #makes sure Taboo level is accurate
        
        if Taboo and (not ApprovalCheck(Girls[0], 1500, TabM=3) or (Girls[0] == "Emma" and Taboo and "taboo" not in E_History)):
                #causes you to leave if the girl is not ready for public stuff                
                $ Act = "leave"
        
        if bg_current in ("bg rogue","bg kitty","bg emma","bg laura"):             
                #Causes the girl to pull you out if she doesn't live in the room you're in
                if bg_current == "bg rogue" and "Rogue" not in Girls:
                        $ Act = "leave"                        
                elif bg_current == "bg kitty" and "Kitty" not in Girls:
                        $ Act = "leave"
                elif bg_current == "bg emma" and "Emma" not in Girls:
                        $ Act = "leave"
                elif bg_current == "bg laura" and "Laura" not in Girls:
                        $ Act = "leave"
        
        call Set_The_Scene
                      
        call AnyFace(Girls[0],"sly",1)     
        if Act == "leave":        
                #if she's not supercool with public stuff. . .    
                "Suddenly, [Girls[0]] grabs your arm with a miscevious smile, and starts to lead you back towards your room."                
                menu:                
                    "Go along with it":                      
                        "You follow after her."
                    "Pull away from her and head back.":                    
                        call Statup(Girls[0], "Love", 90, -10) 
                        call Statup(Girls[0], "Obed", 50, 10) 
                        call Statup(Girls[0], "Obed", 95, 5) 
                        call Statup(Girls[0], "Inbt", 95, -5) 
                        call AnyFace(Girls[0],"sad",1)           
                        "You tell her to cut it out, and head back to what you were doing."
                        $ P_RecentActions.append("nope")      
                        call AnyWord(Girls[0],1,"refused","refused") 
                        if not ApprovalCheck(Girls[0], 500, "O"):                        
                                call AnyWord(Girls[0],1,"angry","angry") 
                        return  
                        
                if Partner:       
                        "[Partner] also follows along behind you."
                
                $ bg_current = "bg player"                   
                call CleartheRoom(Girls[0],1,1)  
                if "Rogue" in Girls:
                        $ R_Loc = bg_current
                if "Kitty" in Girls:
                        $ K_Loc = bg_current
                if "Emma" in Girls:
                        $ E_Loc = bg_current
                if "Laura" in Girls:
                        $ L_Loc = bg_current                 
                call Set_The_Scene(Dress=0) 
                        
                call Taboo_Level #makes sure Taboo level is accurate                
        else:                     
            if Partner:  
                    call AnyFace(Girls[1],"sly",1)                       
                    "Suddenly, [Girls[0]] pulls you aside and [Partner] follows along."
            else:
                    "Suddenly, [Girls[0]] pulls you aside."
        
        call AnyWord(Girls[0],1,"jumped","jumped",0,"jumped") #adds jumped to recent, daily, and history
        
        if Girls[0] == "Rogue":
                ch_r "You've been dodge'in me lately."
                ch_r "Figured it was about time we did something about that."
                $ Initial = "R"
        elif Girls[0] == "Kitty":
                ch_k "Why haven't you been coming by?"
                ch_k "Wouldn't you enjoy some \"Kitty\" time?"
                $ Initial = "K"
        elif Girls[0] == "Emma":
                ch_e "You haven't been coming around to visit lately."
                ch_e "Is there any way I could tempt you?"
                $ Initial = "E"
        elif Girls[0] == "Laura":
                ch_l "I'm horny, let's fuck."
                $ Initial = "L"
        else: 
                return
            
        call Favorite_Actions(Girls[0],1) #returns a string of the action
        $ Act = _return
        $ Situation = Girls[0]
        
        if Act in ("anal","sex","blow","tit","hand","hotdog"):
                # if cock needs to be out. . .
                "[Girls[0]] reaches down and unzips your fly. . ."
                call Seen_First_Peen(Girls[0],Partner,1)
        
        if Partner:
                call expression Partner + "_Noticed" pass (Girls[0],1) #calls the "noticed check" for this girl. 
                        
        call AnyWord(Girls[0],1,0,0,0,"jumped")  #makes in History that this happened
        
        # launches the appropriate scene based on the sex act in question.
        if Act == "anal":        
                call expression Initial + "_AnalPrep" #call R_AnalPrep                
        elif Act == "sex":
                call expression Initial + "_SexPrep" #call R_SexPrep
        elif Act ==  "lick pussy":
                call expression Initial + "_LP_Prep" #call R_LP_Prep 
        elif Act == "fondle pussy":
                call expression Initial + "_FP_Prep" #call R_FP_Prep
        elif Act == "blow":
                call expression Initial + "_BJ_Prep" #call R_BJ_Prep
        elif Act == "tit":
                call expression Initial + "_TJ_Prep" #call R_TJ_Prep
        elif Act == "hand":
                call expression Initial + "_HJ_Prep" #call R_HJ_Prep 
        elif Act == "hotdog":
                call expression Initial + "_HotdogPrep" #call R_HotdogPrep
        elif Act == "suck breasts":               
                call expression Initial + "_SB_Prep" #call R_SB_Prep
        elif Act == "fondle breasts":
                call expression Initial + "_FB_Prep" #call R_FB_Prep
        elif Act == "insert ass" or Act == "lick ass":
                call expression Initial + "_IA_Prep" #call R_IA_Prep
        else: #Act == "kiss you"
                call expression Initial + "_KissPrep" #call R_KissPrep                 
        return
        
#End Jumped, when a girl does try to jump you
        
 
# Start sex act escalation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Escalation(Girl=0,Initial=0):
        #call Escalation("Rogue","R")
        # raises the level of the sexual activity if the girl would like that. 
        if Cnt < 10 or ThreeCount <= Round:
                #if things just started, or you recently made a change, return
                return
                
        $ Situation = Girl
        
        if Trigger == "fondle breast" and ApprovalCheck(Girl,1050,TabM=4) and ApprovalCheck(Girl,30,"X") and HistoryCheck(Girl,"suck breasts"):
                    #if you're fondling her breasts, she has over 30 Lust, and she's had her breasts sucked before. . .
                    call expression Initial + "_SB_Prep" #call R_SB_Prep  
                    if CheckWord(Girl,"Recent","suck breasts"):
                            # If you went through with it, drop one phase back when returning to this point
                            $ renpy.pop_call()
        elif Trigger == "fondle thighs" and ApprovalCheck(Girl,1050,TabM=4) and ApprovalCheck(Girl,30,"X") and HistoryCheck(Girl,"fondle pussy"):
                    #if you're fondling her thighs, she has over 30 Lust, and she's had her pussy fondled before. . .
                    call expression Initial + "_FP_Prep" #call R_FP_Prep  
                    if CheckWord(Girl,"Recent","fondle pussy"):
                            # If you went through with it, drop one phase back when returning to this point
                            $ renpy.pop_call()
        elif Trigger == "handjob" and ApprovalCheck(Girl,1200,TabM=4) and ApprovalCheck(Girl,30,"X") and HistoryCheck(Girl,"blow"):
                    #if she's giving a handy, she has over 30 Lust, and she's sucked cock before. . .
                    call expression Initial + "_BJ_Prep" #call R_BJ_Prep  
                    if CheckWord(Girl,"Recent","blow"):
                            # If you went through with it, drop one phase back when returning to this point
                            $ renpy.pop_call()                  
        elif Trigger not in ("sex","anal") and ApprovalCheck(Girl,1400,TabM=5) and ApprovalCheck(Girl,60,"X") and HistoryCheck(Girl,"sex") >= 3:
                    #if you're not having sex, she has over 60 Lust, and she's had sex before. . .
                    call expression Initial + "_SexPrep" #call R_SexPrep  
                    if CheckWord(Girl,"Recent","sex"):
                            # If you went through with it, drop one phase back when returning to this point
                            $ renpy.pop_call()  
        elif Trigger != "anal" and ApprovalCheck(Girl,1400,TabM=5) and ApprovalCheck(Girl,70,"X") and HistoryCheck(Girl,"anal") >= 5:
                    #if you're not having anal, she has over 70 Lust, and she's had anal before. . .
                    call expression Initial + "_AnalPrep" #call R_AnalPrep  
                    if CheckWord(Girl,"Recent","anal"):
                            # If you went through with it, drop one phase back when returning to this point
                            $ renpy.pop_call() 
        
        
        
        #if it falls through the options
        $ ThreeCount = 0
        $ Situation = 0
        return
#end Escalation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Danger Room Historia / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
  
label Danger_Room_Historia(Character="Rogue",Scenario="Meeting"):
    # Character is the lead character, Scenario is the scene being played out
    default DangerStore = [0,0,0,0,0,0,0,0,0,0,0,0]
    ch_danger "Now booting up the Danger Room historical simulation protocols. . ."
    menu:
        ch_danger "Which girl did you want to simulate?"
        "Rogue":
            $ Character="Rogue"
        "Kitty" if "met" in K_History:
            $ Character="Kitty"  
        "Kitty (locked)" if "met" not in K_History:
            $ Character="Kitty"            
        "Emma" if "met" in E_History:
            $ Character="Emma"          
        "Emma (locked)" if "met" not in E_History:
            $ Character="Emma"
        "Never mind.":
            return
    menu:
        ch_danger "And Which type of scenario?"
        "First meeting":
            $ Scenario="Meeting"
        "A Relationship milestone" if Character != "Emma":
            $ Scenario="Relationship"   
        "A Relationship milestone (locked)" if Character == "Emma":
            pass
        "Caught after Class" if Character == "Emma" and "classcaught" in E_History:
            $ Scenario="ClassCaught"   
        "Never mind.":
            return
    ch_danger "Launching simulation settings. . ."
    ch_danger "Take care not to save the game until the simulation ends, as these saves may become corrupted at a later date."
    $ P_Traits.append("Historia")
    call Shift_Focus(Character)    
    call CleartheRoom("All",0,1)
    if Character == "Rogue":
            #store data for later
            # cover petnames, achievements, rules in scenes themselves
            $ DangerStore = [0,0,0,0,0,0,0,0,0,0,0,0]
            $ DangerStore[1] = Time_Count
            $ DangerStore[2] = R_Love
            $ DangerStore[3] = R_Obed
            $ DangerStore[4] = R_Inbt
            $ DangerStore[5] = R_Lust
            
            $ DangerStore[6] = list(R_History)
            $ DangerStore[7] = list(R_Traits)
            $ DangerStore[8] = list(R_RecentActions)
            $ DangerStore[9] = list(R_DailyActions)
            
            $ DangerStore[10] = R_Addict
            $ DangerStore[11] = R_Addictionrate
            #run scenario
            
            if Scenario == "Meeting":
                    #add Rogue's default stats
                    $ R_Love = 500
                    $ R_Obed = 0
                    $ R_Inbt = 0 
                    $ R_Lust = 0
                    $ Current_Time = "Evening"
                    # Rogue's lists are irrelevant to this one, but add them to other scenarios
                    $ DangerStore.append(R_Kissed)
                    
                    call Prologue
                    
                    $ R_Kissed = DangerStore[12]
            elif Scenario == "Relationship":  
                    $ DangerStore.append(R_Kissed)
                    $ DangerStore.append(R_SEXP)
                    $ DangerStore.append(list(R_Petnames))                                  
                    $ bg_current = "bg player"   
                    menu:
                        "Which scene?"
                        "Girlfriend"    if "boyfriend" in R_Petnames:
                                $ DangerStore.append(R_Event[5]) 
                                call Historia_Counter
                                $ R_Event[5] = _return       
                                call Rogue_BF                                
                                $ R_Event[5] = DangerStore[15]  
                        "Girlfriend (locked)" if "boyfriend" not in R_Petnames:
                                pass
                                
                        "Lover"         if "lover" in R_Petnames:
                                $ DangerStore.append(R_Event[6])  
                                call Historia_Counter                             
                                $ R_Event[6] = _return                                                               
                                call Rogue_Love                                
                                $ R_Event[6] = DangerStore[15]                                  
                        "Lover (locked)" if "lover" not in R_Petnames:
                                pass
                                
                        "Submissive"    if "sir" in R_Petnames:
                                $ DangerStore.append(R_Event[7])   
                                call Historia_Counter                            
                                $ R_Event[7] = _return                                                                
                                call Rogue_Sub                                
                                $ R_Event[7] = DangerStore[15]  
                        "Submissive (locked)" if "sir" not in R_Petnames:
                                pass
                                
                        "Slave"         if "master" in R_Petnames:
                                $ DangerStore.append(R_Event[8])  
                                call Historia_Counter                             
                                $ R_Event[8] = _return                                                               
                                call Rogue_Slave                                
                                $ R_Event[8] = DangerStore[15]  
                        "Slave (locked)" if "master" not in R_Petnames:
                                pass
                                
                        "Sex Friend"    if "sex friend" in R_Petnames:
                                $ DangerStore.append(R_Event[9]) 
                                call Historia_Counter                              
                                $ R_Event[9] = _return                                                               
                                call Rogue_Sexfriend                                
                                $ R_Event[9] = DangerStore[15]  
                        "Sex Friend (locked)" if "sex friend" not in R_Petnames:
                                pass
                                
                        "Fuckbuddy"     if "fuck buddy" in R_Petnames:
                                $ DangerStore.append(R_Event[10])  
                                call Historia_Counter                             
                                $ R_Event[10] = _return                                                               
                                call Rogue_Fuckbuddy                                
                                $ R_Event[10] = DangerStore[15]  
                        "Fuckbuddy (locked)" if "fuck buddy" not in R_Petnames:
                                pass
                                
                        "Daddy"         if "daddy" in R_Petnames:                                                    
                                call Rogue_Daddy                 
                        "Daddy (locked)" if "daddy" not in R_Petnames:
                                pass
                        "Never mind":
                                $ DangerStore = []              
                                $ bg_current = "bg dangerroom" 
                                jump Historia_Clear
                
                    $ R_Kissed = DangerStore[12]
                    $ R_SEXP = DangerStore[13]    
                    $ R_Petnames = DangerStore[14]
            # end Relationship scenarios
                    
            #clean up after the scenario
            
            if _return:
                ch_danger "-Bzzt- Oversimulation detected."
            ch_danger "Simulation Ending. . ."

            $ Time_Count        = DangerStore[1]

            $ R_Love            = DangerStore[2]
            $ R_Obed            = DangerStore[3]
            $ R_Inbt            = DangerStore[4] 
            $ R_Lust            = DangerStore[5]
            
            $ R_History         = DangerStore[6]
            $ R_Traits          = DangerStore[7] 
            $ R_RecentActions   = DangerStore[8] 
            $ R_DailyActions    = DangerStore[9]            
            $ R_Addict          = DangerStore[10]
            $ R_Addictionrate   = DangerStore[11]
            $ DangerStore = []
            
            $ Current_Time = Time_Options[(Time_Count)]     
    
            $ bg_current = "bg dangerroom"
            call Rogue_Schedule
            call Remove_Girl("Rogue")
            call Set_The_Scene
            hide BlueScreen onlayer black
            call RogueOutfit 
            $ Taboo = 40
    #end Rogue stuff
    
    elif Character == "Kitty":
            #store data for later
            # cover petnames, achievements, rules in scenes themselves
            $ DangerStore = [0,0,0,0,0,0,0,0,0,0,0,0]
            $ DangerStore[1] = Time_Count
            $ DangerStore[2] = K_Love
            $ DangerStore[3] = K_Obed
            $ DangerStore[4] = K_Inbt
            $ DangerStore[5] = K_Lust
            
            $ DangerStore[6] = list(K_History)
            $ DangerStore[7] = list(K_Traits)
            $ DangerStore[8] = list(K_RecentActions)
            $ DangerStore[9] = list(K_DailyActions)
            
            $ DangerStore[10] = K_Addict
            $ DangerStore[11] = K_Addictionrate
            #run scenario
            
            if Scenario == "Meeting":
                    #add Kitty's default stats
                    $ K_Love = 400
                    $ K_Obed = 100
                    $ K_Inbt = 0 
                    $ K_Lust = 0
                    # Kitty's lists are irrelevant to this one, but add them to other scenarios
                    $ DangerStore.append(K_Petname)#12
                    
                    call KittyMeet
                    
                    $ K_Petname = DangerStore[12]
            elif Scenario == "Relationship":  
                    $ DangerStore.append(K_Kissed)#12
                    $ DangerStore.append(K_SEXP)#13
                    $ DangerStore.append(list(K_Petnames))#14
                    $ DangerStore.append(K_Petname)#15                       
                    $ bg_current = "bg player"   
                    menu:
                        "Which scene?"
                        "Girlfriend"    if "boyfriend" in K_Petnames:
                                $ DangerStore.append(K_Event[5])#16 
                                call Historia_Counter
                                $ K_Event[5] = _return       
                                call Kitty_BF                                
                                $ K_Event[5] = DangerStore[16]  
                        "Girlfriend (locked)" if "boyfriend" not in K_Petnames:
                                pass
                                
                        "Lover"         if "lover" in K_Petnames:
                                $ DangerStore.append(K_Event[6])#16  
                                menu:
                                        "How many times has she asked you already?"
                                        "None":
                                            $ K_Event[6] = 0
                                        "Once":
                                            $ K_Event[6] = 1
                                        "Many times (enough)":
                                            $ K_Event[6] = 6                                  
                                call Kitty_Love                                
                                $ K_Event[6] = DangerStore[16]                                  
                        "Lover (locked)" if "lover" not in K_Petnames:
                                pass
                                
                        "Submissive"    if "sir" in K_Petnames:       
                                $ K_Petnames.remove("sir")
                                menu:
                                    "First time":                                                       
                                        call Kitty_Sub         
                                    "Second chance":                           
                                        ch_p "You said you wanted me to be more in control?"
                                        call Kitty_Sub_Asked
                                $ K_Petnames.append("sir")
                        "Submissive (locked)" if "sir" not in K_Petnames:
                                pass
                                
                        "Slave"         if "master" in K_Petnames: 
                                $ K_Petnames.remove("master")
                                menu:
                                    "First time": 
                                        call Kitty_Master  
                                    "Second chance":                                          
                                        if "sir" not in K_Petnames:
                                                $ K_Petnames.append("sir") 
                                        ch_p "You said you wanted me to be your Master?" 
                                        call Kitty_Sub_Asked
                                $ K_Petnames.append("master")
                        "Slave (locked)" if "master" not in K_Petnames:
                                pass
                                
                        "Sex Friend"    if "sex friend" in K_Petnames:                                          
                                call Kitty_Sexfriend            
                        "Sex Friend (locked)" if "sex friend" not in K_Petnames:
                                pass
                                
                        "Fuckbuddy"     if "fuck buddy" in K_Petnames:                                       
                                call Kitty_Fuckbuddy                                
                                $ K_Event[10] = 1
                        "Fuckbuddy (locked)" if "fuck buddy" not in K_Petnames:
                                pass
                                
                        "Daddy"         if "daddy" in K_Petnames:                                                    
                                call Kitty_Daddy                 
                        "Daddy (locked)" if "daddy" not in K_Petnames:
                                pass
                        "Never mind":
                                $ DangerStore = []              
                                $ bg_current = "bg dangerroom"   
                                jump Historia_Clear
                
                    $ K_Kissed = DangerStore[12]
                    $ K_SEXP = DangerStore[13]    
                    $ K_Petnames = DangerStore[14]
                    $ K_Petname = DangerStore[15]
            # end Relationship scenarios
                    
            #clean up after the scenario
            
            if _return:
                ch_danger "-Bzzt- Oversimulation detected."
            ch_danger "Simulation Ending. . ."

            $ Time_Count        = DangerStore[1]

            $ K_Love            = DangerStore[2]
            $ K_Obed            = DangerStore[3]
            $ K_Inbt            = DangerStore[4] 
            $ K_Lust            = DangerStore[5]
            
            $ K_History         = DangerStore[6]
            $ K_Traits          = DangerStore[7] 
            $ K_RecentActions   = DangerStore[8] 
            $ K_DailyActions    = DangerStore[9]            
            $ K_Addict          = DangerStore[10]
            $ K_Addictionrate   = DangerStore[11]
            $ DangerStore = []
            
            $ Current_Time = Time_Options[(Time_Count)]     
    
            $ bg_current = "bg dangerroom"
            call Kitty_Schedule
            call Remove_Girl("Kitty")
            call Set_The_Scene
            hide BlueScreen onlayer black
            call KittyOutfit 
            $ Taboo = 40
    #end Kitty stuff
    
    elif Character == "Emma":
            #store data for later
            # cover petnames, achievements, rules in scenes themselves
            $ DangerStore = [0,0,0,0,0,0,0,0,0,0,0,0]
            $ DangerStore[1] = Time_Count
            $ DangerStore[2] = E_Love
            $ DangerStore[3] = E_Obed
            $ DangerStore[4] = E_Inbt
            $ DangerStore[5] = E_Lust
            
            $ DangerStore[6] = list(E_History)
            $ DangerStore[7] = list(E_Traits)
            $ DangerStore[8] = list(E_RecentActions)
            $ DangerStore[9] = list(E_DailyActions)
            
            $ DangerStore[10] = E_Addict
            $ DangerStore[11] = E_Addictionrate
            #run scenario
            
            if Scenario == "Meeting":
                    #add Emma's default stats
                    $ E_Love = 300
                    $ E_Obed = 0
                    $ E_Inbt = 200 
                    $ E_Lust = 0
                    # Emma's lists are irrelevant to this one, but add them to other scenarios
                    $ DangerStore.append(E_Petname)#12
                    $ DangerStore.append(P_Rep)#13
                    $ DangerStore.append(R_SEXP)#14
                    $ DangerStore.append(K_SEXP)#15
                    $ DangerStore.append(P_Lvl)#16
                    menu:
                        "How often do you get caught in public?"
                        "Never":
                            $ P_Rep = 800
                        "Rarely":
                            $ P_Rep = 500
                        "Very Often":
                            $ P_Rep = 0
                    menu:
                        "How far have you gotten with other girls?"
                        "No progress":
                            $ R_SEXP = 0
                            $ K_SEXP = 0
                        "Sex with one" if R_SEXP >= 60 or K_SEXP >= 60:
                            $ R_SEXP = 70
                            $ K_SEXP = 0
                        "Sex with one (locked)" if R_SEXP < 60 and K_SEXP < 60:
                            pass
                        "Sex with more than one" if R_SEXP >= 60 and K_SEXP >= 60:
                            $ R_SEXP = 70
                            $ K_SEXP = 70
                        "Sex with more than one (locked)" if not (R_SEXP >= 60 and K_SEXP >= 60):
                            pass
                    menu:
                        "And how has your schooling gone so far?"
                        "Barely started":
                            $ P_Lvl = 0
                        "Decent progress" if P_Lvl >= 3:
                            $ P_Lvl = 3
                        "Decent progress (locked)" if P_Lvl < 3:
                            pass
                        "Very advanced" if P_Lvl >= 7:
                            $ P_Lvl = 7
                        "Very advanced (locked)" if P_Lvl < 7:
                            pass
                            
                    call EmmaMeet
                    
                    $ E_Petname = DangerStore[12]
                    $ P_Rep = DangerStore[13]
                    $ R_SEXP = DangerStore[14]
                    $ K_SEXP = DangerStore[15]
                    $ P_Lvl = DangerStore[16]
                    
            elif Scenario == "ClassCaught":
                    # Emma's lists are irrelevant to this one, but add them to other scenarios
                    
                    $ E_History.remove("classcaught")
                                            
                    call Emma_Caught_Classroom
                    $ E_Mast -= 1
                    
#            elif Scenario == "Relationship":  
#                    $ DangerStore.append(E_Kissed)#12
#                    $ DangerStore.append(E_SEXP)#13
#                    $ DangerStore.append(list(E_Petnames))#14
#                    $ DangerStore.append(E_Petname)#15                       
#                    $ bg_current = "bg player"   
#                    menu:
#                        "Which scene?"
#                        "Girlfriend"    if "boyfriend" in E_Petnames:
#                                $ DangerStore.append(E_Event[5])#16 
#                                call Historia_Counter
#                                $ E_Event[5] = _return       
#                                call Emma_BF                                
#                                $ E_Event[5] = DangerStore[16]  
#                        "Girlfriend (locked)" if "boyfriend" not in E_Petnames:
#                                pass
                                
#                        "Lover"         if "lover" in E_Petnames:
#                                $ DangerStore.append(E_Event[6])#16  
#                                menu:
#                                        "How many times has she asked you already?"
#                                        "None":
#                                            $ E_Event[6] = 0
#                                        "Once":
#                                            $ E_Event[6] = 1
#                                        "Many times (enough)":
#                                            $ E_Event[6] = 6                                  
#                                call Emma_Lover                                
#                                $ E_Event[6] = DangerStore[16]                                  
#                        "Lover (locked)" if "lover" not in E_Petnames:
#                                pass
                                
#                        "Submissive"    if "sir" in E_Petnames:       
#                                $ E_Petnames.remove("sir")
#                                menu:
#                                    "First time":                                                       
#                                        call Emma_Sub         
#                                    "Second chance":                           
#                                        ch_p "You said you wanted me to be more in control?"
#                                        call Emma_Sub_Asked
#                                $ E_Petnames.append("sir")
#                        "Submissive (locked)" if "sir" not in E_Petnames:
#                                pass
                                
#                        "Slave"         if "master" in E_Petnames: 
#                                $ E_Petnames.remove("master")
#                                menu:
#                                    "First time": 
#                                        call Emma_Master  
#                                    "Second chance":                                          
#                                        if "sir" not in E_Petnames:
#                                                $ E_Petnames.append("sir") 
#                                        ch_p "You said you wanted me to be your Master?" 
#                                        call Emma_Sub_Asked
#                                $ E_Petnames.append("master")
#                        "Slave (locked)" if "master" not in E_Petnames:
#                                pass
                                
#                        "Sex Friend"    if "sex friend" in E_Petnames:                                          
#                                call Emma_Sexfriend            
#                        "Sex Friend (locked)" if "sex friend" not in E_Petnames:
#                                pass
                                
#                        "Fuckbuddy"     if "fuck buddy" in E_Petnames:                                       
#                                call Emma_Fuckbuddy                                
#                                $ E_Event[10] = 1
#                        "Fuckbuddy (locked)" if "fuck buddy" not in E_Petnames:
#                                pass
                                
#                        "Daddy"         if "daddy" in E_Petnames:                                                    
#                                call Emma_Daddy                 
#                        "Daddy (locked)" if "daddy" not in E_Petnames:
#                                pass
#                        "Never mind":
#                                $ DangerStore = []              
#                                $ bg_current = "bg dangerroom" 
#                                jump Historia_Clear
                
#                    $ E_Kissed = DangerStore[12]
#                    $ E_SEXP = DangerStore[13]    
#                    $ E_Petnames = DangerStore[14]
#                    $ E_Petname = DangerStore[15]
#            # end Relationship scenarios
                    
            #clean up after the scenario
            
            if _return:
                ch_danger "-Bzzt- Oversimulation detected."
            ch_danger "Simulation Ending. . ."

            $ Time_Count        = DangerStore[1]

            $ E_Love            = DangerStore[2]
            $ E_Obed            = DangerStore[3]
            $ E_Inbt            = DangerStore[4] 
            $ E_Lust            = DangerStore[5]
            
            $ E_History         = DangerStore[6]
            $ E_Traits          = DangerStore[7] 
            $ E_RecentActions   = DangerStore[8] 
            $ E_DailyActions    = DangerStore[9]            
            $ E_Addict          = DangerStore[10]
            $ E_Addictionrate   = DangerStore[11]
            $ DangerStore = []
            
            $ Current_Time = Time_Options[(Time_Count)]     
    
            $ bg_current = "bg dangerroom"
            call Emma_Schedule
            call Remove_Girl("Emma")
            call Set_The_Scene
            hide BlueScreen onlayer black
            call EmmaOutfit 
            $ Taboo = 40
    #end Emma stuff

label Historia_Clear:
    $ Tempmod = 0
    $ Line = 0
    $ MultiAction = 1    
    if "Historia" in P_Traits:
        while "Historia" in P_Traits:
                $ P_Traits.remove("Historia") 
    call Checkout(1)
    ch_danger "Simulation Over, it is again safe to save your progress."
    return
 

label Historia_Counter:
        # Called if the scenario has a repeat function
        menu:
            "How many times has she asked you already?"
            "None":
                return 0
            "Once":
                return 1
            "Twice":
                return 2
        return
        
image BlueScreen:
    alpha .1
    contains:
        Solid("#00B3D6", xysize=(1024, 768))  

# End Danger Room Historia / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  

label Trig_Reset(Visual=0):
    # Resets all triggers, and sprites if Visual
    $ Trigger = 0    
    $ Trigger2 = 0
    $ Trigger3 = 0
    $ Trigger4 = 0
    $ Trigger5 = 0
    $ Situation = 0
    if Visual:
            call AllReset
    return
    
# Start Primary Sex Dialog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
label Sex_Dialog(Primary=Ch_Focus,Secondary=0,TempFocus=0,PrimaryLust=0,SecondaryLust=0,Line1=0,Line2=0,Line3=0,Line4=0,D20S=0): 
        #call Sex_Dialog("Rogue",Partner) 
        # Primary is main female, secondary is supporting female, action is what they are doing.
                
        $ D20S = renpy.random.randint(1, 20) if not D20S else D20S #Sets random seed factor for the encounter
        # If the seed is 0-5, only offhands will play. If it's 15-20, only trigger3's will play. If it's 5-10, offhand and Secondaries will play.
        # If it's 10-15 all things will play. 
           
        # Checks for Taboo, and if it passes through, calls the first sex dialog
        
        $ Line = 0
        
        if Taboo and Zero_Loc(Primary) == bg_current:
            if (D20S + (int(Taboo/10)) - Stealth) >= 10:        
                    #If there is a Taboo level, and your modified roll is over 10
                    call Girls_Taboo(Primary)
        else:            
                    call Girls_Noticed(Primary)  
                    
        $ Secondary = Partner
        
        call expression Primary + "_SexDialog" #call Rogue_SexDialog
        
#        if Primary == "Rogue":                                 
#                    call Rogue_SexDialog                                      
#        elif Primary == "Kitty":                  
#                    call Kitty_SexDialog                    
#        elif Primary == "Emma":
#                    call Emma_SexDialog                    
#        elif Primary == "Laura":
#                    call Laura_SexDialog
                    
        $ Line1 = Line #Set Line1 to the current state of the Line variable
        #End Primary Dialog
        
        #Trigger 2
        if Trigger2 and D20S <= 15:
                    # If there is a player offhand Trigger set and the random value is 1-15, add an Offhand dialog
                    $ Line = ""
                    
                    call expression Primary + "_Offhand" #call Rogue_Offhand
                    
#                    if Primary == "Rogue":                        
#                            call Rogue_Offhand
#                    elif Primary == "Kitty":
#                            call Kitty_Offhand
#                    elif Primary == "Emma":
#                            call Emma_Offhand
#                    elif Primary == "Laura":
#                            call Laura_Offhand
                    
                    $ Line1 = Line1 + Line
        #End Offhand
        
        #Trigger 3
        if D20S >= 7 and Trigger not in ("masturbation", "lesbian"):
                    # If there is a Primary offhand Trigger set and the random value is 1-10, add a self-directed dialog
                    $ Line = 0
                    
                    call expression Primary + "_Self_Lines" pass ("T3",Trigger3) #call Rogue_Self_Lines("T3",Trigger3)  
                    
#                    if Primary == "Rogue":
#                            call Rogue_Self_Lines("T3",Trigger3)      
#                    elif Primary == "Kitty":
#                            call Kitty_Self_Lines("T3",Trigger3)      
#                    elif Primary == "Emma":
#                            call Emma_Self_Lines("T3",Trigger3)     
#                    elif Primary == "Laura":
#                            call Laura_Self_Lines("T3",Trigger3) 
                    if Line:
                            $ Line3 = Line + "."
        #End Primary girl offhand
        
        #Trigger 4
        if Secondary and (not Trigger4 or 7 <= D20S <= 17 or Trigger4 == "watch"):
                    # If there is a Secondary character and the random value is 5-15, add a threeway dialog
                    $ Line = 0
                    
                    call expression Secondary + "_SexDialog_Threeway" #call Rogue_SexDialog_Threeway
                    
#                    if Secondary == "Rogue":
#                            call Rogue_SexDialog_Threeway
#                    elif Secondary == "Kitty":
#                            call Kitty_SexDialog_Threeway
#                    elif Secondary == "Emma":
#                            call Emma_SexDialog_Threeway
#                    elif Secondary == "Laura":
#                            call Laura_SexDialog_Threeway
                    if Line:
                            $ Line4 = Line + "."
        #End Secondary Dialog
        
        #Applying player's satisfaction
        call Statup("Player", "Focus", 200, TempFocus)
        
        #Applying primary girl's satisfaction
        call Statup(Primary, "Lust", 200, PrimaryLust) 
        
        call expression Primary + "Lust" #call RogueLust
                    
#        if Primary == "Rogue":
#                call RogueLust                         
#        elif Primary == "Kitty":
#                call KittyLust                          
#        elif Primary == "Emma":
#                call EmmaLust                           
#        elif Primary == "Laura":
#                call LauraLust       
        
        #Applying secondary girl's satisfaction      
        if Secondary:
                $ SecondaryLust += (int(PrimaryLust/10)) if GirlLikeCheck(Secondary,Primary) >= 700 else 0
                call Statup(Secondary, "Lust", 200, SecondaryLust) 
                
                call expression Secondary + "Lust" #call KittyLust
                    
#        if Secondary == "Rogue": 
#                call RogueLust
#        elif Secondary == "Kitty":
#                call KittyLust 
#        elif Secondary == "Emma":
#                call EmmaLust 
#        elif Secondary == "Laura":
#                call LauraLust 
        
        
        # Dialog begins to play out. . . 
#        "Middialog=[Line]"

        "[Line1]"
        if Line3:
                #If there's a secondary line, play it
                call Seen_First_Peen(Primary,Secondary,Passive=3)
                "[Line3]"
        if Line4:   
                #add call to First Les here."
                #If there's a third person line, play it
                call Seen_First_Peen(Primary,Secondary,Passive=4)
                "[Line4]"  
                if Trigger4 == "suck breasts" or Trigger4 == "fondle breasts":
                    #if breastplay is involved. . .
                    if ApprovalCheck(Primary,500,"I",TabM=2) and ApprovalCheck(Primary,50,"X") and (ChestNum(Primary) > 1 or OverNum(Primary) > 1):
                            # if the girl is horny and her top is on. . .
                            call AnyOutfit(Primary,12) #Uptop up    
                            "[Primary] seems frustrated and pulls her top open."   
                
        call Activity_Check(Primary,Secondary,0) 
        #sees if girl is cool with what's happening, if not, removes her. 
        if not _return:
            if Secondary:
                    #if the first girl leaves, but there is another,  
                    $ Trigger = Secondary
                    $ Partner = 0
                    $ Trigger4 = 0
                    $ Trigger5 = 0
#                    $ renpy.pop_call() #negates call to Sex Dialog                   
#                    $ renpy.pop_call() #negates call to sexaction in progress        
#                    $ renpy.pop_call() #negates call to sex menu
            jump Misplaced
        else:
            call Dirty_Talk 
                        
        return
#        "prereturn=[Line]"                        
        
    
# End Primary Sex Dialog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  


# Start Trigger swap  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
label Trigger_Swap(Current = 0, TriggerX1 = Trigger, TriggerX3 = Trigger3, Primary = Partner):
    #this would switch primary character triggers over to secondary characters.
    # call Trigger_Swap("Rogue") 
    # TriggerX1 and TriggerX3 store the primary girl's actions
    # Current is the old lead girl
    # Primary is the new lead girl
    
    $ Trigger2 = 0 if Trigger2 != "jackin" else Trigger2
    $ Tempmod = 0
    
    if Trigger4:
        #if the second girl is already doing something
        if Trigger4 == "masturbation":
                $ Trigger = "masturbation"
                $ Trigger3 = Trigger5
                $ Trigger4 = 0
                #"hand","fondle breasts","suck breasts","fondle pussy","dildo pussy",
                #"vibrator pussy","fondle ass","dildo anal" 
        elif TriggerX1 == "lesbian":  
                $ Trigger = "lesbian"
                $ Trigger3 = Trigger4  
                $ Trigger4 = 0
        elif Trigger4 in ("hand","blow","kiss you"):  
                $ Trigger = Trigger4
                $ Trigger3 = 0
                $ Trigger4 = 0
        else:   
                $ Trigger = 0
                $ Trigger3 = 0
                $ Trigger4 = 0
                #"fondle breasts","suck breasts","fondle pussy","lick pussy",
                #"fondle ass","lick ass",
    else:
        #if the second girl is not already doing anything
        $ Trigger = 0
        $ Trigger3 = 0
        
    call Shift_Focus(Primary)  
    if not Current:
            if R_Loc == bg_current and Primary != "Rogue":
                    $ Partner = "Rogue"
            elif K_Loc == bg_current and Primary != "Kitty":
                    $ Partner = "Kitty"
            elif E_Loc == bg_current and Primary != "Emma":
                    $ Partner = "Emma"
            elif L_Loc == bg_current and Primary != "Laura":
                    $ Partner = "Laura"
    else:
            $ Partner = Current
        
    #if the primary girl was doing something
    if TriggerX1 == "masturbation":
            $ Trigger4 = "masturbation"
            $ Trigger5 = TriggerX3
            #"hand","fondle breasts","suck breasts","fondle pussy","dildo pussy",
            #"vibrator pussy","fondle ass","dildo anal" 
    elif TriggerX1 == "lesbian":
            $ Trigger4 = TriggerX3            
    else:   
            if TriggerX1 in ("hand","blow","kiss you"):  
                $ Trigger4 = TriggerX1     
                $ Trigger5 = 0 
            else:
                $ Trigger4 = "masturbation"
                if TriggerX1 in ("fondle thighs","fondle ass","insert ass","lick ass"):                    
                        $ Trigger5 = "fondle ass"
                        "You pull back from [Partner]."
                elif TriggerX1 in ("dildo pussy","dildo anal"):
                        $ Trigger5 = TriggerX1
                        "You pull back from [Partner]."
                elif TriggerX1 in ("titjob","hotdog","fondle breasts","suck breasts"):
                        $ Trigger5 = "fondle breasts"
                        "You pull back from [Partner]."
                elif TriggerX1 in ("fondle pussy","lick pussy"):
                        $ Trigger5 = "fondle pussy"
                        "You pull back from [Partner]."
                elif TriggerX1 == "sex":
                        $ Trigger5 = "fondle pussy"
                        "You pull out of [Partner] and shift your attention to [Primary]."
                elif TriggerX1 == "anal":
                        $ Trigger5 = "fondle ass"
                        "You pull out of [Partner] and shift your attention to [Primary]."                
                else:                          
                        $ Trigger5 = 0  
    
    if Partner == "Rogue":
            call AllReset("Rogue")
    if Partner == "Kitty":
            call AllReset("Kitty")
    if Partner == "Emma":
            call AllReset("Emma")
    if Partner == "Laura":
            call AllReset("Laura")
            
#    $ renpy.pop_call() #causes it to skip past the cycle you were in before
#    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
    #popcall doesn't work here because it deletes the called variables.
    if not Trigger:                 
#            call Set_The_Scene(Dress = 0, TrigReset = 0, Quiet=1)
#            "What would you like her to do?"
            if Primary == "Rogue":
                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
                    jump Rogue_SMenu
            if Primary == "Kitty":
                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
                    jump Kitty_SMenu
            if Primary == "Emma":
                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
                    jump Emma_SMenu
            if Primary == "Laura":
                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
                    jump Laura_SMenu
    else:
            call Set_The_Scene(Dress = 0, TrigReset = 0, Quiet=1)
            if Primary == "Rogue":
                    call Rogue_SexAct("SkipTo")
            if Primary == "Kitty":
                    call Kitty_SexAct("SkipTo")
            if Primary == "Emma":
                    call Emma_SexAct("SkipTo")
            if Primary == "Laura":
                    call Laura_SexAct("SkipTo")
    return
# End Trigger swap  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  


# Start CloseOut  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
label CloseOut(Chr = "Rogue"):
    # This exits out of the current sex act, whichever it might be, then returns
    if Chr == "Rogue":
            if Trigger == "blow":
                call RBJ_After
            elif Trigger == "hand":  
                call RHJ_After  
            elif Trigger == "titjob":
                call RTJ_After
            elif Trigger == "kiss you":
                call R_Kiss_After
            elif Trigger == "fondle breasts":
                call RFB_After
            elif Trigger == "suck breasts":
                call RSB_After
            elif Trigger == "fondle thighs":
                call RFT_After
            elif Trigger == "fondle pussy":
                call RFP_After
            elif Trigger == "lick pussy":
                call RLP_After
            elif Trigger == "fondle ass":
                call RFA_After
            elif Trigger == "insert ass":
                call RIA_After
            elif Trigger == "lick ass":
                call RLA_After
            elif Trigger == "sex":
                call R_SexAfter
            elif Trigger == "hotdog":
                call R_HotdogAfter
            elif Trigger == "anal":
                call R_AnalAfter
            elif Trigger == "dildo pussy":
                call RDP_After
            elif Trigger == "dildo anal":
                call RDA_After
            elif Trigger == "strip":
                call Group_Strip_End
            elif Trigger == "masturbation":   
                $ R_Action -= 1
                $ R_Mast += 1    
            elif Trigger == "lesbian":                
                call R_Les_After
            else:
                "That's odd, tell Oni how you got here, Close Rogue [Trigger]."
    #End Rogue
    elif Chr == "Kitty":
            if Trigger == "blow":
                call KBJ_After
            elif Trigger == "hand":  
                call KHJ_After  
            elif Trigger == "titjob":
                call KTJ_After
            elif Trigger == "kiss you":
                call K_Kiss_After
            elif Trigger == "fondle breasts":
                call KFB_After
            elif Trigger == "suck breasts":
                call KSB_After
            elif Trigger == "fondle thighs":
                call KFT_After
            elif Trigger == "fondle pussy":
                call KFP_After
            elif Trigger == "lick pussy":
                call KLP_After
            elif Trigger == "fondle ass":
                call KFA_After
            elif Trigger == "insert ass":
                call KIA_After
            elif Trigger == "lick ass":
                call KLA_After
            elif Trigger == "sex":
                call K_SexAfter
            elif Trigger == "hotdog":
                call K_HotdogAfter
            elif Trigger == "anal":
                call K_AnalAfter
            elif Trigger == "foot":
                call KFJ_After
            elif Trigger == "dildo pussy":
                call KDP_After
            elif Trigger == "dildo anal":
                call KDA_After
            elif Trigger == "masturbation":   
                $ K_Action -= 1
                $ K_Mast += 1    
            elif Trigger == "strip":
                call Group_Strip_End
            elif Trigger == "lesbian":                
                call K_Les_After
            else:
                "That's odd, tell Oni how you got here, Close Kitty [Trigger]."
    elif Chr == "Emma":
            if Trigger == "blow":
                call E_BJ_After
            elif Trigger == "hand":  
                call E_HJ_After  
            elif Trigger == "titjob":
                call E_TJ_After
            elif Trigger == "kiss you":
                call E_Kiss_After
            elif Trigger == "fondle breasts":
                call E_FB_After
            elif Trigger == "suck breasts":
                call E_SB_After
            elif Trigger == "fondle thighs":
                call E_FT_After
            elif Trigger == "fondle pussy":
                call E_FP_After
            elif Trigger == "lick pussy":
                call E_LP_After
            elif Trigger == "fondle ass":
                call E_FA_After
            elif Trigger == "insert ass":
                call E_IA_After
            elif Trigger == "lick ass":
                call E_LA_After
            elif Trigger == "sex":
                call E_SexAfter
            elif Trigger == "hotdog":
                call E_HotdogAfter
            elif Trigger == "anal":
                call E_AnalAfter
            elif Trigger == "dildo pussy":
                call E_DP_After
            elif Trigger == "dildo anal":
                call E_DA_After
            elif Trigger == "strip":
                call Group_Strip_End
            elif Trigger == "masturbation":   
                $ E_Action -= 1
                $ E_Mast += 1   
            elif Trigger == "lesbian":                
                call E_Les_After
            else:
                "That's odd, tell Oni how you got here, Close Emma [Trigger]."
    #End Emma    
    elif Chr == "Laura":
            if Trigger == "blow":
                call L_BJ_After
            elif Trigger == "hand":  
                call L_HJ_After  
            elif Trigger == "titjob":
                call L_TJ_After
            elif Trigger == "kiss you":
                call L_Kiss_After
            elif Trigger == "fondle breasts":
                call L_FB_After
            elif Trigger == "suck breasts":
                call L_SB_After
            elif Trigger == "fondle thighs":
                call L_FT_After
            elif Trigger == "fondle pussy":
                call L_FP_After
            elif Trigger == "lick pussy":
                call L_LP_After
            elif Trigger == "fondle ass":
                call L_FA_After
            elif Trigger == "insert ass":
                call L_IA_After
            elif Trigger == "lick ass":
                call L_LA_After
            elif Trigger == "sex":
                call L_SexAfter
            elif Trigger == "hotdog":
                call L_HotdogAfter
            elif Trigger == "anal":
                call L_AnalAfter
            elif Trigger == "dildo pussy":
                call L_DP_After
            elif Trigger == "dildo anal":
                call L_DA_After
            elif Trigger == "strip":
                call Group_Strip_End
            elif Trigger == "masturbation":   
                $ L_Action -= 1
                $ L_Mast += 1   
            elif Trigger == "lesbian":                
                call L_Les_After
            else:
                "That's odd, tell Oni how you got here, Close Laura [Trigger]."
    #End Laura
    return
# End CloseOut  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  

# Start Sex_Over  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
label Sex_Over(Clothes=1,Girls=0):
        #this routine plays out at the end of any sex menu session
        #it cleans them up and puts their clothes on, only returning a line of dialog if they were undressed
        $ Line = 0
        if R_Loc == bg_current:
                # if Rogue is present
                $ R_OCount = 0    
                call Rogue_Cleanup("after")
                if P_Spunk:
                    ch_r "Let me take care of that for you. . ."
                    call R_CleanCock                    
        if K_Loc == bg_current:
                # if Kitty is present
                $ K_OCount = 0    
                call Kitty_Cleanup("after")
                if P_Spunk:
                    ch_k "You've got a little something. . ."
                    ch_k "just let me get that."
                    call K_CleanCock
        if E_Loc == bg_current:
                # if Emma is present
                $ E_OCount = 0    
                call Emma_Cleanup("after") 
                if P_Spunk:
                    ch_e "[E_Petname], let's get you presentable. . ."
                    call E_CleanCock
        if L_Loc == bg_current:
                # if Laura is present
                $ L_OCount = 0    
                call Laura_Cleanup("after") 
                if P_Spunk:
                    ch_l "[L_Petname], you've got a little something. . ."
                    call L_CleanCock
        
        if Girls and Ch_Focus != Girls:
                #swaps lead back to original
                call Shift_Focus(Partner)
        $ Girls = 0            
        call AllReset("all") #resets all sex positions.       
        
        if Clothes:   
                #if asked to put their clothes back on. 
                if R_Loc == bg_current:
                        # if Rogue is present
                        call RogueOutfit(Changed=1)
                        if _return:
                                $ Line = "Rogue"
                                $ Girls += 1
                if K_Loc == bg_current:
                        # if Kitty is present
                        call KittyOutfit(Changed=1)
                        if _return:
                                if Line:
                                    $ Line = Line + " and Kitty"
                                else:
                                    $ Line = "Kitty"
                                $ Girls += 1
                if E_Loc == bg_current:
                        # if Emma is present
                        call EmmaOutfit(Changed=1) 
                        if _return:
                                if Line:
                                    $ Line = Line + " and Emma"
                                else:
                                    $ Line = "Emma"  
                                $ Girls += 1   
                if L_Loc == bg_current:
                        # if Laura is present
                        call LauraOutfit(Changed=1) 
                        if _return:
                                if Line:
                                    $ Line = Line + " and Laura"
                                else:
                                    $ Line = "Laura"  
                                $ Girls += 1   
                if Girls > 1:
                    "[Line] throw their clothes back on."
                elif Girls:
                    "[Line] throws her clothes back on."
        call Get_Dressed
        call Checkout(1)
        return
        
label AllHide(Cull=0):    
    if Cull or R_Loc != bg_current:
            hide Rogue
            call Rogue_Hide
    if Cull or K_Loc != bg_current:
            hide Kitty_Sprite
            call Kitty_Hide
    if Cull or E_Loc != bg_current:
            hide Emma_Sprite
            call Emma_Hide
    if Cull or L_Loc != bg_current:
            hide Laura_Sprite
            call Laura_Hide
    if Cull or "bg study" != bg_current:
            hide Professor
    return
            
# End Sex_Over  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /         
       
# Start SkipTo  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
label SkipTo(Primary = 0):
        # This jumps to the chosen sex act, called from the sex menu
        if Primary == "Rogue":
                if Trigger:                    
                        if Trigger == "blow":
                            jump RBJ_Cycle
                        elif Trigger == "hand":  
                            jump RHJ_Cycle  
                        elif Trigger == "kiss you":
                            jump R_KissCycle
                        elif Trigger == "fondle breasts":
                            jump RFB_Cycle
                        elif Trigger == "suck breasts":
                            jump RSB_Cycle
                        elif Trigger == "fondle pussy":
                            jump RFP_Cycle
                        elif Trigger == "lick pussy":
                            jump RLP_Cycle
                        elif Trigger == "fondle ass":
                            jump RFA_Cycle
                        elif Trigger == "lick ass":
                            jump RLA_Cycle
                        elif Trigger == "lesbian": 
                            jump R_Les_Cycle
                        elif Trigger == "masturbation": 
                            jump RM_Cycle
                "That's odd, tell Oni how you got here, Skip Rogue [Trigger]."
        #End Rogue
        elif Primary == "Kitty":
                if Trigger:                    
                        if Trigger == "blow":
                            jump KBJ_Cycle
                        elif Trigger == "hand":  
                            jump KHJ_Cycle  
                        elif Trigger == "kiss you":
                            jump K_KissCycle
                        elif Trigger == "fondle breasts":
                            jump KFB_Cycle
                        elif Trigger == "suck breasts":
                            jump KSB_Cycle
                        elif Trigger == "fondle pussy":
                            jump KFP_Cycle
                        elif Trigger == "lick pussy":
                            jump KLP_Cycle
                        elif Trigger == "fondle ass":
                            jump KFA_Cycle
                        elif Trigger == "lick ass":
                            jump KLA_Cycle
                        elif Trigger == "lesbian": 
                            jump K_Les_Cycle
                        elif Trigger == "masturbation": 
                            jump KM_Cycle
                "That's odd, tell Oni how you got here, Skip Kitty [Trigger]"
        elif Primary == "Emma":
                if Trigger:                    
                        if Trigger == "blow":
                            jump E_BJ_Cycle
                        elif Trigger == "hand":  
                            jump E_HJ_Cycle  
                        elif Trigger == "kiss you":
                            jump E_KissCycle
                        elif Trigger == "fondle breasts":
                            jump E_FB_Cycle
                        elif Trigger == "suck breasts":
                            jump E_SB_Cycle
                        elif Trigger == "fondle thighs":
                            jump E_FT_Cycle
                        elif Trigger == "fondle pussy":
                            jump E_FP_Cycle
                        elif Trigger == "lick pussy":
                            jump E_LP_Cycle
                        elif Trigger == "fondle ass":
                            jump E_FA_Cycle
                        elif Trigger == "lick ass":
                            jump E_LA_Cycle
                        elif Trigger == "lesbian": 
                            jump E_Les_Cycle
                        elif Trigger == "masturbation": 
                            jump EM_Cycle
                "That's odd, tell Oni how you got here, Skip Emma [Trigger]"
        #End Emma
        elif Primary == "Laura":
                if Trigger:                    
                        if Trigger == "blow":
                            jump L_BJ_Cycle
                        elif Trigger == "hand":  
                            jump L_HJ_Cycle  
                        elif Trigger == "kiss you":
                            jump L_KissCycle
                        elif Trigger == "fondle breasts":
                            jump L_FB_Cycle
                        elif Trigger == "suck breasts":
                            jump L_SB_Cycle
                        elif Trigger == "fondle thighs":
                            jump L_FT_Cycle
                        elif Trigger == "fondle pussy":
                            jump L_FP_Cycle
                        elif Trigger == "lick pussy":
                            jump L_LP_Cycle
                        elif Trigger == "fondle ass":
                            jump L_FA_Cycle
                        elif Trigger == "lick ass":
                            jump L_LA_Cycle
                        elif Trigger == "lesbian": 
                            jump L_Les_Cycle
                        elif Trigger == "masturbation": 
                            jump LM_Cycle
                "That's odd, tell Oni how you got here, Skip Laura [Trigger]"
        #End Laura
        return
# End SkipTo/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Clear_Stack:
    #this empties the call stack of stray items, and is called when the player goes to his room
    $ StackDepth = renpy.call_stack_depth() #Count = number of items in the call stack
    while StackDepth > 0:
        $ StackDepth -= 1
        $ renpy.pop_call()
    jump Player_Room
    
    
#Character Specific stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
    
    
# Rogue emotion editor ///////////////////////////////////////////////////////////////////////////////////////////////
label RogueEmotionEditor(CountStore = "normal"):
    menu:
        "Normal":
            $ R_Emote = "normal"
            call RogueFace
        "Angry":
            $ R_Emote = "angry"
            call RogueFace
        "Smiling":
            $ R_Emote = "smile"
            call RogueFace
        "Sexy":
            $ R_Emote = "sexy"
            call RogueFace
        "Suprised":
            $ R_Emote = "surprised"
            call RogueFace
        "Bemused":
            $ R_Emote = "bemused"
            call RogueFace
        "Manic":
            $ R_Emote = "manic"
            call RogueFace
        "Sad":
            $ R_Emote = "sad"
            call RogueFace
        "Sucking":
            $ R_Emote = "sucking"
            call RogueFace
        "kiss":
            $ R_Emote = "kiss"
            call RogueFace
        "Tongue":
            $ R_Emote = "tongue"
            call RogueFace
        "confused":
            $ R_Emote = "confused"
            call RogueFace
        "Closed":
            $ R_Emote = "closed"
            call RogueFace
        "Down":
            $ R_Emote = "down"
            call RogueFace
        "Toggle Squint eyes":
            if R_Eyes == "squint":
                $ R_Eyes = CountStore
            else:
                $ CountStore = R_Eyes
                $ R_Eyes = "squint"
        "Toggle grimace":
            if R_Mouth == "grimace":
                $ R_Mouth = CountStore
            else:
                $ CountStore = R_Mouth
                $ R_Mouth = "grimace"
        "Blush":
            if R_Blush == 2:
                $ R_Blush = 1
            elif R_Blush:
                $ R_Blush = 0
            else:
                $ R_Blush = 2  
        "Exit.":
            return
    jump RogueEmotionEditor
return


                

# Rogue's Wardrobe //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label RogueWardrobe:

    menu:      
        "View":
            while True:
                menu:
                    "Default":
                        call R_Pos_Reset
                    "Face":
                        call R_Kissing_Launch(0)
                    "Body":
                        call R_Pussy_Launch(0)
                    "Doggy":
                        if not renpy.showing("Rogue_Doggy"):
                            call Rogue_Doggy_Launch
                        else:
                            call Rogue_Doggy_Reset
                    "Back":
                        jump RogueWardrobe 
        # Outfits
        "Green outfit":
            $ R_Outfit = "evo_green"
            call RogueOutfit
        "Pink outfit":
            $ R_Outfit = "evo_pink"
            call RogueOutfit
        "Nude":
            $ R_Outfit = "nude"
            call RogueOutfit
        "Over":              
            while True:
                menu:
                    # Overshirts    
                    "Remove [R_Over]" if R_Over:
                        $ R_Over = 0
                    "Add mesh top":
                        $ R_Over = "mesh top"
                        $ R_Neck = "spiked collar"
                        $ R_Arms = "gloved"
                        if R_Chest == "buttoned tank":
                            $ R_Chest = "tank"     
                    "Add pink top":
                        $ R_Over = "pink top"  
                        $ R_Arms = "gloved"
                    "Add nighty":
                        $ R_Over = "nighty"   
                        $ R_Arms = 0
                    "Add towel":
                        $ R_Over = "towel"   
                        $ R_Arms = 0
                    "Toggle up-top":
                        if R_Uptop:
                            $ R_Uptop = 0
                        else:
                            $ R_Uptop = 1   
                    "Back":
                        jump RogueWardrobe                
        "Tops":            
            while True:
                menu:
                    # Tops    
                    "Remove [R_Chest]" if R_Chest:
                        $ R_Chest = 0
                    "Add tank top":
                        $ R_Chest = "tank"
                    "Add sports bra":
                        $ R_Chest = "sports bra"
                    "Add buttoned tank top" if R_Over != "mesh top":
                        $ R_Chest = "buttoned tank"
                    "Add lace bra":
                        $ R_Chest = "lace bra"
                    "Add bra":
                        $ R_Chest = "bra"     
                    "Add bikini":
                        $ R_Chest = "bikini top"       
                    "Toggle up-top":
                        if R_Uptop:
                            $ R_Uptop = 0
                        else:
                            $ R_Uptop = 1                         
                    "Toggle Piercings":
                        if R_Pierce == "ring":
                            $ R_Pierce = "barbell"
                        elif R_Pierce == "barbell":
                            $ R_Pierce = 0
                        else:
                            $ R_Pierce = "ring"
                    "Back":
                        jump RogueWardrobe    
    #                "Toggle Top lift" if R_Chest:
    #                    if R_Uptop:
    #                        $ R_Uptop = 0
    #                    else:
    #                        $ R_Uptop = 1           
        
        "Legs":            
            while True:
                menu:
                    # Legs   
                    "Remove legs" if R_Legs:     
                        $ R_Legs = 0
                    "Add Skirt":  
                        $ R_Legs = "skirt"
                        $ R_Upskirt = 0
                    "Add pants":
                        $ R_Legs = "pants"
                        $ R_Hose = 0
                    "Toggle upskirt":
                        if R_Upskirt:
                            $ R_Upskirt = 0
                        else:
                            $ R_Upskirt = 1
                    "Back":
                        jump RogueWardrobe    
        
        "Underwear":            
            while True:
                menu:
                    # Underwear
                    "Hose":
                        menu:
                            "Add hose":     
                                $ R_Hose = "stockings"  
                            "Add garter":     
                                $ R_Hose = "garterbelt"  
                            "Add stockings and garter":     
                                $ R_Hose = "stockings and garterbelt"  
                            "Add pantyhose":     
                                $ R_Hose = "pantyhose"   
                            "Add tights":     
                                $ R_Hose = "tights"   
                            "Add ripped hose":     
                                $ R_Hose = "ripped pantyhose"   
                            "Add ripped tights":     
                                $ R_Hose = "ripped tights"   
                            "Add tights":     
                                $ R_Hose = "tights"    
                            "Remove hose" if R_Hose:     
                                $ R_Hose = 0  
                    "Remove panties" if R_Panties:     
                        $ R_Panties = 0     
                    "Add black panties":
                        $ R_Panties = "black panties"
                    "Add bikini":
                        $ R_Panties = "bikini bottoms"
                    "Add shorts":
                        $ R_Panties = "shorts"
                    "Add green panties":
                        $ R_Panties = "green panties"  
                    "Add lace panties":
                        $ R_Panties = "lace panties"    
                    "pull down-up panties":
                        if R_PantiesDown:
                            $ R_PantiesDown = 0
                        else:
                            $ R_PantiesDown = 1
                    "Back":
                        jump RogueWardrobe    
        "Misc":
            while True:
                menu: 
                    "Emotions":
                        call RogueEmotionEditor
                    "Toggle Arms":
                        if Rogue_Arms == 1:
                            $ Rogue_Arms = 2
                        else:
                            $ Rogue_Arms = 1
                    "Toggle Wetness":
                        if not R_Wet:
                            $ R_Wet = 1
                        elif R_Wet == 1:
                            $ R_Wet = 2
                        else:
                            $ R_Wet  = 0
                    "Toggle wet look":
                        if not R_Water:
                            $ R_Water = 1
                        elif R_Water == 1:
                            $ R_Water = 3
                        else:
                            $ R_Water  = 0
                    "Toggle pubes":
                        if not R_Pubes:
                            $ R_Pubes = 1
                        else:
                            $ R_Pubes = 0
                    "Toggle held":
                        if not R_Held:
                            $ R_Held  = "phone"
                        elif R_Held == "phone":
                            $ R_Held  = "dildo"
                        elif R_Held == "dildo":
                            $ R_Held  = "vibrator"
                        elif R_Held == "vibrator":
                            $ R_Held  = "panties"
                        else:
                            $ R_Held  = 0    
                    "Add Gloves" if not R_Arms:
                        $ R_Arms = "gloved"
                    "Remove Gloves" if R_Arms:
                        $ R_Arms = 0
                    "Back":
                        jump RogueWardrobe               
        "Set Custom Outfit #1.":
            $ R_Custom[0] = 1
            $ R_Custom[1] = R_Arms
            $ R_Custom[2] = R_Legs
            $ R_Custom[3] = R_Over
            $ R_Custom[4] = R_Under #fix, this can be changed to something else, no longer necessary
            $ R_Custom[5] = R_Chest
            $ R_Custom[6] = R_Panties 
            $ R_Custom[7] = R_Pubes 
            $ R_Custom[8] = R_Hair
            $ R_Custom[9] = R_Hose
        "Wear Custom Outfit #[R_Custom[0]]." if R_Custom[0]:
            $ Line = R_Outfit
            $ R_Outfit = "custom1"
            call RogueOutfit
            $ R_Outfit = Line
        "Nothing":
            return
    jump RogueWardrobe
return

# Rogue stathacks //////////////////////
label RogueStats:    
    menu:
        "My Love is %(R_Love)d, Inhibition is %(R_Inbt)d, my Obedience is %(R_Obed)d, my Lust is %(R_Lust)d, my Addiction is %(R_Addict)d, my addiction rate is %(R_Addictionrate)d, and I've been kissed %(R_Kissed)d times."
        "Print actions":
            "[R_RecentActions]"
        "Gwen's face":
            call Gwen_FaceEditor
        "Raise Love":
            $ R_Love += 100
        "Lower Love":
            $ R_Love -= 100
        "Raise Obedience":
            $ R_Obed += 100
        "Lower Obedience":
            $ R_Obed -= 100
        "Raise Inhibitions":
            $ R_Inbt += 100
        "Lower Inhibitions":
            $ R_Inbt -= 100
        "Taboo toggle":
            $ Taboo = 40 if Taboo != 40 else 0
            "[Taboo]"
        "Small":
            $ Count = 1
            while Count:
                menu:
                    "Raise Love":
                        $ R_Love += 10
                    "Lower Love":
                        $ R_Love -= 10
                    "Raise Obedience":
                        $ R_Obed += 10
                    "Lower Obedience":
                        $ R_Obed -= 10
                    "Raise Inhibitions":
                        $ R_Inbt += 10
                    "Lower Inhibitions":
                        $ R_Inbt -= 10
                    "Back":
                        $ Count = 0                    
        "Other":
            menu:        
                "Raise Lust":
                    $ R_Lust += 10
                "Lower Lust":
                    $ R_Lust -= 10
                "Raise Addiction":
                    $ R_Addict += 10
                "Lower Addiction":
                    $ R_Addict -= 10
                "Back":
                    pass
        "Wardrobe":
            call RogueWardrobe
            
        "Return":
            call Checkout
            return
    jump RogueStats
    

# Kitty emotion editor ///////////////////
label KittyEmotionEditor(CountStore = "normal"):
    menu:
        "Emotions1: Normal Angry Smiling Sexy Surprised Bemused Manic.":        
            menu:
                "Normal":
                    $ K_Emote = "normal"
                    call KittyFace
                "Angry":
                    $ K_Emote = "angry"
                    call KittyFace
                "Smiling":
                    $ K_Emote = "smile"
                    call KittyFace
                "Sexy":
                    $ K_Emote = "sexy"
                    call KittyFace
                "Suprised":
                    $ K_Emote = "surprised"
                    call KittyFace
                "Bemused":
                    $ K_Emote = "bemused"
                    call KittyFace
                "Manic":
                    $ K_Emote = "manic"
                    call KittyFace
                    
        "Emotions2: Sad Sucking Kiss Tongue Confused Closed Down.":  
            menu:
                "Sad":
                    $ K_Emote = "sad"
                    call KittyFace
                "Sucking":
                    $ K_Emote = "sucking"
                    call KittyFace
                "kiss":
                    $ K_Emote = "kiss"
                    call KittyFace
                "Tongue":
                    $ K_Emote = "tongue"
                    call KittyFace
                "confused":
                    $ K_Emote = "confused"
                    call KittyFace
                "Closed":
                    $ K_Emote = "closed"
                    call KittyFace
                "Down":
                    $ K_Emote = "down"
                    call KittyFace
                    
        "Emotions3: Sadside Startled Perplexed Sly":  
            menu:
                "Sadside":
                    $ K_Emote = "sadside"
                    call KittyFace
                "Startled":
                    $ K_Emote = "startled"
                    call KittyFace
                "Perplexed":
                    $ K_Emote = "perplexed"
                    call KittyFace
                "Sly":
                    $ K_Emote = "sly"
                    call KittyFace
        "Toggle Mouth Spunk":
            if "mouth" in K_Spunk:
                $ K_Spunk.remove("mouth")
            else:
                $ K_Spunk.append("mouth")
                
        "Toggle Facial Spunk":
            if "facial" in K_Spunk and "hair" not in K_Spunk:
                $ K_Spunk.append("hair")
            elif "facial" in K_Spunk:
                $ K_Spunk.remove("facial")                
                $ K_Spunk.remove("hair")
            else:
                $ K_Spunk.append("facial")
            
        "Blush":
            if K_Blush == 2:
                $ K_Blush = 1
            elif K_Blush:
                $ K_Blush = 0
            else:
                $ K_Blush = 2  
        "Exit.":
            return
    jump KittyEmotionEditor
return

# Kitty's Wardrobe ///////////////////
label KittyWardrobe:

    menu:        
        "Kitty's custom outfit is [K_Custom].[K_Arms]"        
        # Outfits
        "Toggle Kitty":
            if renpy.showing("Kitty_Sprite"):
                hide Kitty_Sprite  
            else:
                call Display_Kitty
        "Outfits":              
            while True:
                menu:
                    "[K_Outfit]"
                    # Outfits   
                    "Pink outfit" if K_Outfit != "pink outfit":
                        $ K_Outfit = "pink outfit"
                    "Red outfit" if K_Outfit != "red outfit":
                        $ K_Outfit = "red outfit"
                    "Nude" if K_Outfit != "nude":
                        $ K_Outfit = "nude"
                    "Back":
                        jump KittyWardrobe 
                call KittyOutfit
        "Tops":              
            while True:
                menu:
                    "[K_Over]"
                    # Tops       
                    "Remove pink top" if K_Over == "pink top":
                        $ K_Over = 0
                    "Add pink top" if K_Over != "pink top":
                        $ K_Over = "pink top"  
                    "Remove red shirt" if K_Over == "red shirt": 
                        $ K_Over = 0
                    "Add red shirt" if K_Over != "red shirt":
                        $ K_Over = "red shirt"
                    "Remove towel" if K_Over == "towel": 
                        $ K_Over = 0
                    "Add towel" if K_Over != "towel":
                        $ K_Over = "towel"
                    "Toggle up-top":
                        if K_Uptop:
                            $ K_Uptop = 0
                        else:
                            $ K_Uptop = 1     
                    "Back":
                        jump KittyWardrobe   
        "Bras":              
            while True:
                menu:
                    "[K_Chest]"
                    # Bras   
                    "Remove cami" if K_Chest == "cami":
                        $ K_Chest = 0
                    "Add cami" if K_Chest != "cami":
                        $ K_Chest = "cami"
                    "Remove bra" if K_Chest == "bra":
                        $ K_Chest = 0
                    "Add bra" if K_Chest != "bra":
                        $ K_Chest = "bra"
                    "Remove lace bra" if K_Chest == "lace bra":
                        $ K_Chest = 0
                    "Add lace bra" if K_Chest != "lace bra":
                        $ K_Chest = "lace bra"
                    "Remove bikini top" if K_Chest == "bikini top":
                        $ K_Chest = 0
                    "Add bikini top" if K_Chest != "bikini top":
                        $ K_Chest = "bikini top"
                    "Remove sports bra" if K_Chest == "sports bra":
                        $ K_Chest = 0
                    "Add sports bra" if K_Chest != "sports bra":
                        $ K_Chest = "sports bra"
                    "Toggle up-top":
                        if K_Uptop:
                            $ K_Uptop = 0
                        else:
                            $ K_Uptop = 1     
                    "Back":
                        jump KittyWardrobe                     
        "Legs":              
            while True:
                menu:
                    "[K_Legs]"
                    # Legs             
                    "Remove capris pants" if K_Legs == "capris":
                        $ K_Legs = 0
                    "Add capris pants" if K_Legs != "capris":
                        $ K_Legs = "capris"
                    "Remove black jeans" if K_Legs == "black jeans":
                        $ K_Legs = 0
                    "Add black jeans" if K_Legs != "black jeans":
                        $ K_Legs = "black jeans"
                    "Remove Yoga Pants" if K_Legs == "yoga pants":
                        $ K_Legs = 0
                    "Add Yoga Pants" if K_Legs != "yoga pants":
                        $ K_Legs = "yoga pants"
                    "Remove shorts" if K_Legs == "shorts":
                        $ K_Legs = 0
                    "Add shorts" if K_Legs != "shorts":
                        $ K_Legs = "shorts"    
                    "Remove blue skirt" if K_Legs == "blue skirt":
                        $ K_Legs = 0
                    "Add blue skirt" if K_Legs != "blue skirt":
                        $ K_Legs = "blue skirt"                         
                    "Toggle upskirt":
                        if K_Upskirt:
                            $ K_Upskirt = 0
                        else:
                            $ K_Upskirt = 1
                    "Back":
                        jump KittyWardrobe   
        "Underwear":              
            while True:
                menu:
                    "[K_Panties]"
                    # Underwear                            
                    "Remove green panties" if K_Panties == "green panties":
                        $ K_Panties = 0
                    "Add green panties" if K_Panties != "green panties":
                        $ K_Panties = "green panties"        
                    "Remove lace panties" if K_Panties == "lace panties":
                        $ K_Panties = 0
                    "Add lace panties" if K_Panties != "lace panties":
                        $ K_Panties = "lace panties"
                    "Remove bikini bottoms" if K_Panties == "bikini bottoms":
                        $ K_Panties = 0
                    "Add bikini bottoms" if K_Panties != "bikini bottoms":
                        $ K_Panties = "bikini bottoms"
                    "Toggle panties down":
                        $ K_PantiesDown = 1 if not K_PantiesDown else 0   
                        "[K_PantiesDown]"
                    "Back":
                        jump KittyWardrobe 
        "Misc":
            while True:
                menu: 
                    "Emotions":
                        call KittyEmotionEditor
                    "Toggle Arms":
                        $ Kitty_Arms = 0 if Kitty_Arms == 1 else 1
                    "Toggle pubes":
                        $ K_Pubes = 1 if not K_Pubes else 0 
                    "Toggle Piercings":
                        if K_Pierce == "ring":
                            $ K_Pierce = "barbell"
                        elif K_Pierce == "barbell":
                            $ K_Pierce = 0
                        else:
                            $ K_Pierce = "ring"
                    "Toggle wetness":
                        if not K_Wet:                            
                            $ K_Wet = 1
                        elif K_Wet == 1:
                            $ K_Wet = 2
                        else:
                            $ K_Wet = 0
                    "Toggle wet look":
                        $ K_Water = 1 if not K_Water else 0 
                    "Toggle hair":
                        $ K_Hair = "evo" if K_Hair == "long" else "long"   
                    "Back":
                        jump KittyWardrobe  
                        
        "View":
            menu:
                "Breasts":
                    call K_Breasts_Launch
                "Pussy":
                    call K_Pussy_Launch
                "Default":
                    call K_Pos_Reset
                
        "Set Custom Outfit #1.":
            $ K_Custom[0] = 1
            $ K_Custom[1] = K_Arms
            $ K_Custom[2] = K_Legs
            $ K_Custom[3] = K_Over
            $ K_Custom[4] = K_Under
            $ K_Custom[5] = K_Chest
            $ K_Custom[6] = K_Panties 
            $ K_Custom[7] = K_Pubes 
            $ K_Custom[8] = K_Hair
            $ K_Custom[9] = K_Hose
        "Wear Custom Outfit #[K_Custom[0]]." if K_Custom[0] == 1:
            $ K_Outfit = "custom1"
            call KittyOutfit
        "Nothing":
            return
    jump KittyWardrobe
return
     
# Kitty stathacks //////////////////////
label KittyStats:    
    menu:
        "My Love is %(K_Love)d, Inhibition is %(K_Inbt)d, my Obedience is %(K_Obed)d, my Lust is %(K_Lust)d, my Addiction is %(K_Addict)d, my addiction rate is %(K_Addictionrate)d, and I've been kissed %(K_Kissed)d times."
        "Print actions":
            "[K_RecentActions]"
        "Raise Love":
            $ K_Love += 100
        "Lower Love":
            $ K_Love -= 100
        "Raise Obedience":
            $ K_Obed += 100
        "Lower Obedience":
            $ K_Obed -= 100
        "Raise Inhibitions":
            $ K_Inbt += 100
        "Lower Inhibitions":
            $ K_Inbt -= 100
        "Taboo toggle":
            $ Taboo = 40 if Taboo != 40 else 0
            "[Taboo]"
        "Small":
            $ Count = 1
            while Count:
                menu:
                    "Raise Love":
                        $ K_Love += 10
                    "Lower Love":
                        $ K_Love -= 10
                    "Raise Obedience":
                        $ K_Obed += 10
                    "Lower Obedience":
                        $ K_Obed -= 10
                    "Raise Inhibitions":
                        $ K_Inbt += 10
                    "Lower Inhibitions":
                        $ K_Inbt -= 10
                    "Back":
                        $ Count = 0                    
        "Other":
            menu:        
                "Raise Lust":
                    $ K_Lust += 10
                "Lower Lust":
                    $ K_Lust -= 10
                "Raise Addiction":
                    $ K_Addict += 10
                "Lower Addiction":
                    $ K_Addict -= 10
                "Back":
                    pass
        "Wardrobe":
            call KittyWardrobe
            
        "Return":
            call Checkout
            return
    jump KittyStats
    
# Emma stathacks //////////////////////
label EmmaStats:    
    menu:
        "My Love is %(E_Love)d, Inhibition is %(E_Inbt)d, my Obedience is %(E_Obed)d, my Lust is %(E_Lust)d, my Addiction is %(E_Addict)d, my addiction rate is %(E_Addictionrate)d, and I've been kissed %(E_Kissed)d times."
        "Print actions":
            "[E_RecentActions]"
        "Raise Love":
            $ E_Love += 100
        "Lower Love":
            $ E_Love -= 100
        "Raise Obedience":
            $ E_Obed += 100
        "Lower Obedience":
            $ E_Obed -= 100
        "Raise Inhibitions":
            $ E_Inbt += 100
        "Lower Inhibitions":
            $ E_Inbt -= 100
        "Taboo toggle":
            $ Taboo = 40 if Taboo != 40 else 0
            "[Taboo]"
        "Small":
            $ Count = 1
            while Count:
                menu:
                    "Raise Love":
                        $ E_Love += 10
                    "Lower Love":
                        $ E_Love -= 10
                    "Raise Obedience":
                        $ E_Obed += 10
                    "Lower Obedience":
                        $ E_Obed -= 10
                    "Raise Inhibitions":
                        $ E_Inbt += 10
                    "Lower Inhibitions":
                        $ E_Inbt -= 10
                    "Back":
                        $ Count = 0                    
        "Other":
            menu:        
                "Raise Lust":
                    $ E_Lust += 10
                "Lower Lust":
                    $ E_Lust -= 10
                "Raise Addiction":
                    $ E_Addict += 10
                "Lower Addiction":
                    $ E_Addict -= 10
                "Back":
                    pass
        "Wardrobe":
            call EmmaWardrobe
            
        "Return":
            call Checkout
            return
    jump EmmaStats
    
# Laura stathacks //////////////////////
label LauraStats:    
    menu:
        "My Love is %(L_Love)d, Inhibition is %(L_Inbt)d, my Obedience is %(L_Obed)d, my Lust is %(L_Lust)d, my Addiction is %(L_Addict)d, my addiction rate is %(L_Addictionrate)d, and I've been kissed %(L_Kissed)d times."
        "Print actions":
            "[L_RecentActions]"
        "Raise Love":
            $ L_Love += 100
        "Lower Love":
            $ L_Love -= 100
        "Raise Obedience":
            $ L_Obed += 100
        "Lower Obedience":
            $ L_Obed -= 100
        "Raise Inhibitions":
            $ L_Inbt += 100
        "Lower Inhibitions":
            $ L_Inbt -= 100
        "Taboo toggle":
            $ Taboo = 40 if Taboo != 40 else 0
            "[Taboo]"
        "Small":
            $ Count = 1
            while Count:
                menu:
                    "Raise Love":
                        $ L_Love += 10
                    "Lower Love":
                        $ L_Love -= 10
                    "Raise Obedience":
                        $ L_Obed += 10
                    "Lower Obedience":
                        $ L_Obed -= 10
                    "Raise Inhibitions":
                        $ L_Inbt += 10
                    "Lower Inhibitions":
                        $ L_Inbt -= 10
                    "Back":
                        $ Count = 0                    
        "Other":
            menu:        
                "Raise Lust":
                    $ L_Lust += 10
                "Lower Lust":
                    $ L_Lust -= 10
                "Raise Addiction":
                    $ L_Addict += 10
                "Lower Addiction":
                    $ L_Addict -= 10
                "Back":
                    pass
        "Wardrobe":
            call LauraWardrobe
            
        "Return":
            call Checkout
            return
    jump LauraStats
    
label Emergency_Clothing_Reset:
    "This resets all customized clothing to their defaults."
    menu:
        "Do you want to continue?"
        "Yes":
                $ R_Custom = [0,0,0,0,0,0,0,0,0,0,0]
                $ R_Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
                $ R_Custom3 = [0,0,0,0,0,0,0,0,0,0,0]  
                $ R_Gym = [2,"gloved",0,"hoodie",0,"sports bra","shorts",0,0,0,0]
                $ R_Sleepwear = [0,0,0,0,0,"tank","green panties",0,0,0]
                $ R_Swim = [0,0,0,"hoodie",0,"bikini top","bikini bottoms",0,0,0,0] 
                $ R_Schedule = [0,0,0,0,0,0,0,0,0,0] 
                
                $ K_Custom = [0,0,0,0,0,0,0,0,0,0]
                $ K_Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
                $ K_Custom3 = [0,0,0,0,0,0,0,0,0,0,0]    
                $ K_Gym = [2,0,"shorts",0,0,"sports bra","green panties",0,0,0,0]
                $ K_Sleepwear = [0,0,"shorts",0,0,"cami","green panties",0,0,0]
                $ K_Swim = [0,0,"blue skirt",0,0,"bikini top","bikini bottoms",0,0,0,0] 
                $ K_Schedule = [0,0,0,0,0,0,0,0,0,0] 
                
                $ E_Custom = [0,0,0,0,0,0,0,0,0,0]
                $ E_Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
                $ E_Custom3 = [0,0,0,0,0,0,0,0,0,0,0]    
                $ E_Gym = [2,0,0,0,0,"sports bra","sports panties",0,0,0,0]
                $ E_Sleepwear = [0,0,0,0,0,"corset","white panties",0,0,0]
                $ E_Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0] 
                $ E_Schedule = [0,0,0,0,0,0,0,0,0,0] 
                
                $ L_Custom = [0,0,0,0,0,0,0,0,0,0]
                $ L_Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
                $ L_Custom3 = [0,0,0,0,0,0,0,0,0,0,0]    
                $ L_Gym = [2,0,"leather pants",0,0,"leather bra","leather panties",0,0,0,0]
                $ L_Sleepwear = [0,0,0,0,0,"leather bra","leather panties",0,0,0]
                $ L_Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0] 
                $ L_Schedule = [0,0,0,0,0,0,0,0,0,0] 
                "Done."
                "You will now need to set their custom outfits again."
        "No":
            pass
    return
            
label Clothing_Schedule_Check(Girl=0,Changed=0,Value=0,Count=0):
    #this clears out clothing items that are out of date. 
    #call Clothing_Schedule_Check("Rogue",3,1)    
    
    # Girl is the checked girl, "changed" is the outfit to compare against
    # Value defaults to 0, but if set, it will only check if the value is not 2.
    # (0-6) = Mon-Sun, (7) Datewear, (8) Teach, (9) Private (skips this one)
    # R_Schedule = [0,0,0,0,0,0,0,0,0,0]  
    # Custom1=3,Cusotm2=5,Custom3=6,Gym=4,Sleep=7,Swim=10
                                    
    while Count < 9:  
        if Girl == "Rogue":    
                    if R_Schedule[Count] == Changed:
                        if Value:
                            #if the Outfit is custom1, and the outfit is SFW, then leave it alone.
                            if R_Schedule[Count] == 3 and R_Custom[0] == 2:
                                    pass
                            elif R_Schedule[Count] == 5 and R_Custom2[0] == 2:
                                    pass
                            elif R_Schedule[Count] == 6 and R_Custom3[0] == 2:
                                    pass
                            elif R_Schedule[Count] == 4 and R_Gym[0] == 2:
                                    pass
                            else:
                                $ R_Schedule[Count] = 0
                        else:
                                $ R_Schedule[Count] = 0
                              
        elif Girl == "Kitty":
                    if K_Schedule[Count] == Changed:
                        if Value:
                            if K_Schedule[Count] == 3 and K_Custom[0] == 2:
                                    pass
                            elif K_Schedule[Count] == 5 and K_Custom2[0] == 2:
                                    pass
                            elif K_Schedule[Count] == 6 and K_Custom3[0] == 2:
                                    pass
                            elif K_Schedule[Count] == 4 and K_Gym[0] == 2:
                                    pass                            
                            else:
                                $ K_Schedule[Count] = 0
                        else:
                                $ K_Schedule[Count] = 0
        elif Girl == "Emma":
                    if E_Schedule[Count] == Changed:
                        if Value:
                            if E_Schedule[Count] == 3 and E_Custom[0] == 2:
                                    pass
                            elif E_Schedule[Count] == 5 and E_Custom2[0] == 2:
                                    pass
                            elif E_Schedule[Count] == 6 and E_Custom3[0] == 2:
                                    pass
                            elif E_Schedule[Count] == 4 and E_Gym[0] == 2:
                                    pass
                            else:
                                $ E_Schedule[Count] = 0
                        else:
                                $ E_Schedule[Count] = 0
        elif Girl == "Laura":
                    if L_Schedule[Count] == Changed:
                        if Value:
                            if L_Schedule[Count] == 3 and L_Custom[0] == 2:
                                    pass
                            elif L_Schedule[Count] == 5 and L_Custom2[0] == 2:
                                    pass
                            elif L_Schedule[Count] == 6 and L_Custom3[0] == 2:
                                    pass
                            elif L_Schedule[Count] == 4 and L_Gym[0] == 2:
                                    pass
                            else:
                                $ L_Schedule[Count] = 0
                        else:
                                $ L_Schedule[Count] = 0        
        $ Count += 1
    return
    
label Failsafe: 
    #This routine is meant to set any variables that aren't already set.     
    $ TestVariableBeta = 10 if "TestVariableBeta" not in globals().keys() else TestVariableBeta 
    $ SaveVersion = 976 #keep updated to latest version
    $ Day = 1 if "Day" not in globals().keys() else Day 
    $ Cheat = 0 if "Cheat" not in globals().keys() else Cheat
    $ Time_Options = ["Morning", "Midday", "Evening", "Night"]
    $ Time_Count = 2 if "Time_Count" not in globals().keys() else Time_Count
    $ Current_Time = Time_Options[(Time_Count)]     
    $ Week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    $ Weekday = 6 if "Weekday" not in globals().keys() else Weekday
    $ DayofWeek = Week[Weekday]
    $ bg_current = "bg study" if "bg_current" not in globals().keys() else bg_current
    $ Party = [] if "Party" not in globals().keys() else Party
    $ Taboo = 0 if "Taboo" not in globals().keys() else Taboo
    $ Rules = ["rules"] if "Rules" not in globals().keys() else Rules
    $ Line = 0 if "Line" not in globals().keys() else Line 
    $ Situation = 0 if "Situation" not in globals().keys() else Situation                #Whether Auto/Shift
    $ MultiAction = 1 if "MultiAction" not in globals().keys() else MultiAction              #0 if the action cannot continue, 1 if it can
    $ Trigger = 0 if "Trigger" not in globals().keys() else Trigger                 #Mainhand
    $ Trigger2 = 0 if "Trigger2" not in globals().keys() else Trigger2                #Offhand
    $ Trigger3 = 0 if "Trigger3" not in globals().keys() else Trigger3                #Girl's offhand    
    $ Trigger4 = 0 if "Trigger4" not in globals().keys() else Trigger4                #this is the 4th sexual act performed by the second girl 
    $ Trigger5 = 0 if "Trigger5" not in globals().keys() else Trigger5                #this is the 5th sexual act performed by the second girl if masturbating
    $ Present = [] if "Present" not in globals().keys() else Present
    $ Adjacent = 0 if "Adjacent" not in globals().keys() else Adjacent                #this is the girl you're sitting next to in class
    $ Partner = 0 if "Partner" not in globals().keys() else Partner                 #this is the second character involved in a sex act, make sure to set Partner to 0 after each sex act
    $ Events = [] if "Events" not in globals().keys() else Events
    $ Tempmod = 0 if "Tempmod" not in globals().keys() else Tempmod
    $ Approval = 0  if "Approval" not in globals().keys() else Approval               #for approval checks
    $ Count = 0 if "Count" not in globals().keys() else Count                   #For within an event
    $ Count2 = 0 if "Count2" not in globals().keys() else Count2                  #For between several events
    $ Round = 100 if "Round" not in globals().keys() else Round   
    $ Stealth = 0 if "Stealth" not in globals().keys() else Stealth                #How careful you're being
    $ Cnt = 0 if "Cnt" not in globals().keys() else Cnt                     #a mini Count variable for discrete operations
    $ Speed = 0 if "Speed" not in globals().keys() else Speed
    $ CountStore = 0 if "CountStore" not in globals().keys() else CountStore              #Stores values for after an event ends
    $ Achievements = [] if "Achievements" not in globals().keys() else Achievements
    $ Options = [] if "Options" not in globals().keys() else Options
    $ Vibration = 0 if "Vibration" not in globals().keys() else Vibration
    $ UI_Tool = 0 if "UI_Tool" not in globals().keys() else UI_Tool
    $ Ch_Focus = "Rogue" if "Ch_Focus" not in globals().keys() else Ch_Focus
    $ TravelMode = 0 if "TravelMode" not in globals().keys() else TravelMode           #used for wandering around, if 0, you use the worldmap
    $ StageRight = 900            #these are values for location points on the screen
    $ StageCenter = 715
    $ StageLeft = 500
    $ StageFarLeft = 150
#Player Stats    
    $ Playername = "Zero" if "Playername" not in globals().keys() else Playername
    $ P_Male = 1 if "P_Male" not in globals().keys() else P_Male
    $ R_Petname = "sugar" if "R_Petname" not in globals().keys() else R_Petname       #What Rogue calls the player
    $ R_Petnames = ["sugar"] if "R_Petnames" not in globals().keys() else R_Petnames
    $ R_Pet = "Rogue" if "R_Pet" not in globals().keys() else R_Pet           #What you call Rogue
    $ R_Pets = ["Rogue"] if "R_Pets" not in globals().keys() else R_Pets
    $ K_Petname = "sweetie" if "K_Petname" not in globals().keys() else K_Petname       #What Rogue calls the player
    $ K_Petnames = ["sweetie"] if "K_Petnames" not in globals().keys() else K_Petnames
    $ K_Pet = "Kitty" if "K_Pet" not in globals().keys() else K_Pet           #What you call Rogue
    $ K_Pets = ["Kitty"] if "K_Pets" not in globals().keys() else K_Pets
    $ P_Semen = 2 if "P_Semen" not in globals().keys() else P_Semen
    $ P_Semen_Max = 3 if "P_Semen_Max" not in globals().keys() else P_Semen_Max
    $ P_Focus = 0 if "P_Focus" not in globals().keys() else P_Focus
    $ P_FocusX = 0 if "P_FocusX" not in globals().keys() else P_FocusX
    $ P_XP = 0 if "P_XP" not in globals().keys() else P_XP
    $ P_StatPoints = 0 if "P_StatPoints" not in globals().keys() else P_StatPoints    
    $ P_XPgoal = 100 if "P_XPgoal" not in globals().keys() else P_XPgoal
    $ P_Lvl = 1 if "P_Lvl" not in globals().keys() else P_Lvl
    $ P_Traits = [] if "P_Traits" not in globals().keys() else P_Traits
    $ P_Rep = 600 if "P_Rep" not in globals().keys() else P_Rep
    $ P_RecentActions = [] if "P_RecentActions" not in globals().keys() else P_RecentActions
    $ P_DailyActions = [] if "P_DailyActions" not in globals().keys() else P_DailyActions
# Player Inventory Variables 
    $ P_Income = 12 if "P_Income" not in globals().keys() else P_Income               #how much you make each day
    $ P_Cash = 20 if "P_Cash" not in globals().keys() else P_Cash
    $ P_Inventory = [] if "P_Inventory" not in globals().keys() else P_Inventory
    $ Inventory_Count = 0 if "Inventory_Count" not in globals().keys() else Inventory_Count
    $ Digits = [] if "Digits" not in globals().keys() else Digits
    $ Keys = [] if "Keys" not in globals().keys() else Keys
    $ PunishmentX = 0 if "PunishmentX" not in globals().keys() else PunishmentX
# Player Sprite
    $ P_Sprite = 0 if "P_Sprite" not in globals().keys() else P_Sprite
    $ P_Color = "green" if "P_Color" not in globals().keys() else P_Color
    $ P_Cock = "out" if "P_Cock" not in globals().keys() else P_Cock
    $ P_Spunk = 0 if "P_Spunk" not in globals().keys() else P_Spunk
    $ P_Wet = 0 if "P_Wet" not in globals().keys() else P_Wet
#Rogue Stats   
    $ R_Loc = "bg rogue" if "R_Loc" not in globals().keys() else R_Loc
    $ R_Love = 500 if "R_Love" not in globals().keys() else R_Love
    $ R_Obed = 0 if "R_Obed" not in globals().keys() else R_Obed
    $ R_Inbt = 0 if "R_Inbt" not in globals().keys() else R_Inbt
    $ R_Lust = 10 if "R_Lust" not in globals().keys() else R_Lust
    $ R_LikeKitty = 600 if "R_LikeKitty" not in globals().keys() else R_LikeKitty
    $ R_Addict = 0 if "R_Addict" not in globals().keys() else R_Addict                #how addicted she is
    $ R_Addictionrate = 0 if "R_Addictionrate" not in globals().keys() else R_Addictionrate         #How faster her addiciton rises
    $ R_AddictStore = 0 if "R_AddictStore" not in globals().keys() else R_AddictStore           #stores her base addiction level
    $ R_Resistance = 0 if "R_Resistance" not in globals().keys() else R_Resistance            #how fast her rate falls
    $ R_OCount = 0 if "R_OCount" not in globals().keys() else R_OCount                #Orgasm counter
    $ R_Loose = 0 if "R_Loose" not in globals().keys() else R_Loose
    $ R_Inventory = [] if "R_Inventory" not in globals().keys() else R_Inventory
    $ R_XP = 0 if "R_XP" not in globals().keys() else R_XP
    $ R_ShameLevel = 0 if "R_ShameLevel" not in globals().keys() else R_ShameLevel
    $ R_Cheated = 0 if "R_Cheated" not in globals().keys() else R_Cheated               #number of times you've cheated on her    
    $ R_Break = [0,0] if "R_Break" not in globals().keys() else R_Break                 #minimum time between break-ups/number of total break-ups
    $ R_StatPoints = 0 if "R_StatPoints" not in globals().keys() else R_StatPoints    
    $ R_XPgoal = 100 if "R_XPgoal" not in globals().keys() else R_XPgoal
    $ R_Lvl = 0 if "R_Lvl" not in globals().keys() else R_Lvl
    $ R_Traits = [] if "R_Traits" not in globals().keys() else R_Traits
    $ R_Rep = 800 if "R_Rep" not in globals().keys() else R_Rep
    $ R_OutfitShame = [50,0,0,0,20,0,0,10,0,0,0,0,0,0,0] if "R_OutfitShame" not in globals().keys() else R_OutfitShame
    $ R_Shame = 0 if "R_Shame" not in globals().keys() else R_Shame                 #The amount of shame Rogue generates with her current clothing/action
    $ R_Taboo = 0 if "R_Taboo" not in globals().keys() else R_Taboo                 #The taboo level of the location Rogue is at when not with you
    $ R_Chat = [0,0,0,0,0,0] if "R_Chat" not in globals().keys() else R_Chat
    $ R_Event = [0,0,0,0,0,0,0,0,0,0,0] if "R_Event" not in globals().keys() else R_Event  
    $ R_Todo = [] if "R_Todo" not in globals().keys() else R_Todo
    $ R_PubeC = 0 if "R_PubeC" not in globals().keys() else R_PubeC
  # Sexual Encounters
    $ R_History = [] if "R_History" not in globals().keys() else R_History
    $ R_RecentActions = [] if "R_RecentActions" not in globals().keys() else R_RecentActions
    $ R_DailyActions = [] if "R_DailyActions" not in globals().keys() else R_DailyActions
    $ R_Action = 3 if "R_Action" not in globals().keys() else R_Action
    $ R_MaxAction = 3 if "R_MaxAction" not in globals().keys() else R_MaxAction
    $ R_Caught = 0 if "R_Caught" not in globals().keys() else R_Caught
    $ R_Kissed = 0 if "R_Kissed" not in globals().keys() else R_Kissed              #How many times they've kissed
    $ R_Hand = 0 if "R_Hand" not in globals().keys() else R_Hand
    $ R_Slap = 0 if "R_Slap" not in globals().keys() else R_Slap
    $ R_Strip = 0 if "R_Strip" not in globals().keys() else R_Strip
    $ R_Tit = 0 if "R_Tit" not in globals().keys() else R_Tit
    $ R_Sex = 0 if "R_Sex" not in globals().keys() else R_Sex
    $ R_Anal = 0 if "R_Anal" not in globals().keys() else R_Anal
    $ R_Hotdog = 0 if "R_Hotdog" not in globals().keys() else R_Hotdog
    $ R_Mast = 0 if "R_Mast" not in globals().keys() else R_Mast
    $ R_Org = 0 if "R_Org" not in globals().keys() else R_Org
    $ R_FondleB = 0 if "R_FondleB" not in globals().keys() else R_FondleB
    $ R_FondleT = 0 if "R_FondleT" not in globals().keys() else R_FondleT
    $ R_FondleP = 0 if "R_FondleP" not in globals().keys() else R_FondleP
    $ R_FondleA = 0 if "R_FondleA" not in globals().keys() else R_FondleA
    $ R_DildoP = 0 if "R_DildoP" not in globals().keys() else R_DildoP
    $ R_DildoA = 0 if "R_DildoA" not in globals().keys() else R_DildoA
    $ R_Vib = 0 if "R_Vib" not in globals().keys() else R_Vib
    $ R_Plug = 0 if "R_Plug" not in globals().keys() else R_Plug
    $ R_SuckB = 0 if "R_SuckB" not in globals().keys() else R_SuckB
    $ R_InsertP = 0 if "R_InsertP" not in globals().keys() else R_InsertP
    $ R_InsertA = 0 if "R_InsertA" not in globals().keys() else R_InsertA
    $ R_LickP = 0 if "R_LickP" not in globals().keys() else R_LickP
    $ R_LickA = 0 if "R_LickA" not in globals().keys() else R_LickA
    $ R_Blow = 0 if "R_Blow" not in globals().keys() else R_Blow
    $ R_Swallow = 0 if "R_Swallow" not in globals().keys() else R_Swallow
    $ R_CreamP = 0 if "R_CreamP" not in globals().keys() else R_CreamP
    $ R_CreamA = 0 if "R_CreamA" not in globals().keys() else R_CreamA
    $ R_Les = 0 if "R_Les" not in globals().keys() else R_Les                           #how many times she's done lesbian stuff
    $ R_SexKitty = 0 if "R_SexKitty" not in globals().keys() else R_SexKitty                      #how many times she's had sex involving Kitty
    $ R_SEXP = 0 if "R_SEXP" not in globals().keys() else R_SEXP
    $ R_PlayerFav = 0 if "R_PlayerFav" not in globals().keys() else R_PlayerFav                     #The player's favorite activity with her
    $ R_Favorite = 0 if "R_Favorite" not in globals().keys() else R_Favorite                      #her favorite activity
    $ R_SeenChest = 0 if "R_SeenChest" not in globals().keys() else R_SeenChest
    $ R_SeenPanties = 0 if "R_SeenPanties" not in globals().keys() else R_SeenPanties
    $ R_SeenPussy = 0 if "R_SeenPussy" not in globals().keys() else R_SeenPussy
    $ R_SeenPeen = 0 if "R_SeenPeen" not in globals().keys() else R_SeenPeen                      #How many times she's seen your cock
    $ R_Sleep = 0 if "R_Sleep" not in globals().keys() else R_Sleep 
    $ R_Personality = "normal" if "R_Personality" not in globals().keys() else R_Personality
    $ R_Date = 0 if "R_Date" not in globals().keys() else R_Date 
    $ R_Forced = 0 if "R_Forced" not in globals().keys() else R_Forced                        #This is a toggle for if she's being coerced
    $ R_ForcedCount = 0 if "R_ForcedCount" not in globals().keys() else R_ForcedCount                   #This is a counter for each time she's been coerced lately
#Rogue Sprite Variables
    $ R_Outfit = "evo_green" if "R_Outfit" not in globals().keys() else R_Outfit
    $ R_OutfitDay = "evo_green" if "R_OutfitDay" not in globals().keys() else R_OutfitDay
    $ Rogue_Arms = 1 if "Rogue_Arms" not in globals().keys() else Rogue_Arms
    $ R_Emote = "normal" if "R_Emote" not in globals().keys() else R_Emote
    $ R_Arms = "collargloved" if "R_Arms" not in globals().keys() else R_Arms
    $ R_Legs = "skirt" if "R_Legs" not in globals().keys() else R_Legs
    $ R_Over = "mesh top" if "R_Over" not in globals().keys() else R_Over
    $ R_Under = 0 if "R_Under" not in globals().keys() else R_Under
    $ R_Chest = "tank" if "R_Chest" not in globals().keys() else R_Chest
    $ R_Pierce = 0 if "R_Pierce" not in globals().keys() else R_Pierce
    $ R_Panties = "black panties" if "R_Panties" not in globals().keys() else R_Panties
    $ R_Neck = "spiked collar" if "R_Neck" not in globals().keys() else R_Neck
    $ R_Hose = "stockings" if "R_Hose" not in globals().keys() else R_Hose
    $ R_Mouth = "normal" if "R_Mouth" not in globals().keys() else R_Mouth
    $ R_Brows = "normal" if "R_Brows" not in globals().keys() else R_Brows
    $ R_Eyes = "normal" if "R_Eyes" not in globals().keys() else R_Eyes
    $ R_Hair = "evo" if "R_Hair" not in globals().keys() else R_Hair
    $ R_Gag = 0 if "R_Gag" not in globals().keys() else R_Gag
    $ R_Blush = 0 if "R_Blush" not in globals().keys() else R_Blush
    $ R_Spunk = [] if "R_Spunk" not in globals().keys() else R_Spunk
    $ R_Sperm = [] if "R_Sperm" not in globals().keys() else R_Sperm
    $ R_Pubes = 1 if "R_Pubes" not in globals().keys() else R_Pubes
    $ R_Wet = 0 if "R_Wet" not in globals().keys() else R_Wet
    $ R_Water = 0 if "R_Water" not in globals().keys() else R_Water
    $ R_Upskirt = 0 if "R_Upskirt" not in globals().keys() else R_Upskirt
    $ R_PantiesDown = 0 if "R_PantiesDown" not in globals().keys() else R_PantiesDown
    $ R_Uptop = 0 if "R_Uptop" not in globals().keys() else R_Uptop
    $ R_Held = 0 if "R_Held" not in globals().keys() else R_Held
    $ R_Custom = [0,0,0,0,0,0,0,0,0,0,0] if "R_Custom" not in globals().keys() else R_Custom
    $ R_Custom2 = [0,0,0,0,0,0,0,0,0,0,0] if "R_Custom2" not in globals().keys() else R_Custom2
    $ R_Custom3 = [0,0,0,0,0,0,0,0,0,0,0] if "R_Custom3" not in globals().keys() else R_Custom3
    $ R_Gym = [0,"gloved",0,"hoodie",0,"sports bra","shorts",0,0,0,0] if "R_Gym" not in globals().keys() else R_Gym
    $ R_Sleepwear = [0,0,0,0,"tank","green panties",0] if "R_Sleepwear" not in globals().keys() else R_Sleepwear
    $ R_Schedule = [0,0,0,0,0,0,0,0,4,0] if "R_Schedule" not in globals().keys() else R_Schedule                      #chooses when she wears what
    $ R_SpriteVer = 0 if "R_SpriteVer" not in globals().keys() else R_SpriteVer
    $ RogueLayer = 50 if "RogueLayer" not in globals().keys() else RogueLayer
    $ R_SpriteLoc = StageRight if "R_SpriteLoc" not in globals().keys() else R_SpriteLoc                        #Sets Rogue to $ to the right side  
#Kitty Stats   
    $ K_Loc = 0 if "K_Loc" not in globals().keys() else K_Loc
    $ K_Love = 400 if "K_Love" not in globals().keys() else K_Love
    $ K_Obed = 100 if "K_Obed" not in globals().keys() else K_Obed
    $ K_Inbt = 0 if "K_Inbt" not in globals().keys() else K_Inbt
    $ K_Lust = 10 if "K_Lust" not in globals().keys() else K_Lust
    $ K_LikeRogue = 700 if "K_LikeRogue" not in globals().keys() else K_LikeRogue
    $ K_Addict = 0 if "K_Addict" not in globals().keys() else K_Addict                #how addicted she is
    $ K_Addictionrate = 0 if "K_Addictionrate" not in globals().keys() else K_Addictionrate         #How faster her addiciton rises
    $ K_AddictStore = 0 if "K_AddictStore" not in globals().keys() else K_AddictStore          #stores her base addiction level
    $ K_Resistance = 0 if "K_Resistance" not in globals().keys() else K_Resistance            #how fast her rate falls
    $ K_OCount = 0 if "K_OCount" not in globals().keys() else K_OCount                #Orgasm counter
    $ K_Loose = 0 if "K_Loose" not in globals().keys() else K_Loose
    $ K_Inventory = [] if "K_Inventory" not in globals().keys() else K_Inventory
    $ K_XP = 0 if "K_XP" not in globals().keys() else K_XP
    $ K_ShameLevel = 0 if "K_ShameLevel" not in globals().keys() else K_ShameLevel
    $ K_Cheated = 0 if "K_Cheated" not in globals().keys() else K_Cheated               #number of times you've cheated on her    
    $ K_Break = [0,0] if "K_Break" not in globals().keys() else K_Break                 #minimum time between break-ups/number of total break-ups
    $ K_StatPoints = 0 if "K_StatPoints" not in globals().keys() else K_StatPoints    
    $ K_XPgoal = 100 if "K_XPgoal" not in globals().keys() else K_XPgoal
    $ K_Lvl = 0 if "K_Lvl" not in globals().keys() else K_Lvl
    $ K_Traits = [] if "K_Traits" not in globals().keys() else K_Traits
    $ K_Rep = 800 if "K_Rep" not in globals().keys() else K_Rep
    $ K_OutfitShame = [50,0,0,0,20,0,0,10,0,0,0,0,0,0,0] if "K_OutfitShame" not in globals().keys() else K_OutfitShame
    $ K_Shame = 0 if "K_Shame" not in globals().keys() else K_Shame                 #The amount of shame Rogue generates with her current clothing/action
    $ K_Taboo = 0 if "K_Taboo" not in globals().keys() else K_Taboo                 #The taboo level of the location Rogue is at when not with you
    $ K_Chat = [0,0,0,0,0,0] if "K_Chat" not in globals().keys() else K_Chat
    $ K_Event = [0,0,0,0,0,0,0,0,0,0,0] if "K_Event" not in globals().keys() else K_Event  
    $ K_Todo = [] if "K_Todo" not in globals().keys() else K_Todo
    $ K_PubeC = 0 if "K_PubeC" not in globals().keys() else K_PubeC
    $ K_Like = "Like, " if "K_Like" not in globals().keys() else K_Like
    $ K_like = ", like, " if "K_like" not in globals().keys() else K_like
  # Sexual Encounters
    $ K_History = [] if "K_History" not in globals().keys() else K_History
    $ K_RecentActions = [] if "K_RecentActions" not in globals().keys() else K_RecentActions
    $ K_DailyActions = [] if "K_DailyActions" not in globals().keys() else K_DailyActions
    $ K_Action = 3 if "K_Action" not in globals().keys() else K_Action
    $ K_MaxAction = 3 if "K_MaxAction" not in globals().keys() else K_MaxAction
    $ K_Caught = 0 if "K_Caught" not in globals().keys() else K_Caught
    $ K_Kissed = 0 if "K_Kissed" not in globals().keys() else K_Kissed              #How many times they've kissed
    $ K_Hand = 0 if "K_Hand" not in globals().keys() else K_Hand
    $ K_Slap = 0 if "K_Slap" not in globals().keys() else K_Slap
    $ K_Strip = 0 if "K_Strip" not in globals().keys() else K_Strip
    $ K_Tit = 0 if "K_Tit" not in globals().keys() else K_Tit
    $ K_Sex = 0 if "K_Sex" not in globals().keys() else K_Sex
    $ K_Anal = 0 if "K_Anal" not in globals().keys() else K_Anal
    $ K_Hotdog = 0 if "K_Hotdog" not in globals().keys() else K_Hotdog
    $ K_Mast = 0 if "K_Mast" not in globals().keys() else K_Mast
    $ K_Org = 0 if "K_Org" not in globals().keys() else K_Org
    $ K_FondleB = 0 if "K_FondleB" not in globals().keys() else K_FondleB
    $ K_FondleT = 0 if "K_FondleT" not in globals().keys() else K_FondleT
    $ K_FondleP = 0 if "K_FondleP" not in globals().keys() else K_FondleP
    $ K_FondleA = 0 if "K_FondleA" not in globals().keys() else K_FondleA
    $ K_DildoP = 0 if "K_DildoP" not in globals().keys() else K_DildoP
    $ K_DildoA = 0 if "K_DildoA" not in globals().keys() else K_DildoA
    $ K_Vib = 0 if "K_Vib" not in globals().keys() else K_Vib
    $ K_Plug = 0 if "K_Plug" not in globals().keys() else K_Plug
    $ K_SuckB = 0 if "K_SuckB" not in globals().keys() else K_SuckB
    $ K_InsertP = 0 if "K_InsertP" not in globals().keys() else K_InsertP
    $ K_InsertA = 0 if "K_InsertA" not in globals().keys() else K_InsertA
    $ K_LickP = 0 if "K_LickP" not in globals().keys() else K_LickP
    $ K_LickA = 0 if "K_LickA" not in globals().keys() else K_LickA
    $ K_Blow = 0 if "K_Blow" not in globals().keys() else K_Blow
    $ K_Swallow = 0 if "K_Swallow" not in globals().keys() else K_Swallow
    $ K_CreamP = 0 if "K_CreamP" not in globals().keys() else K_CreamP
    $ K_CreamA = 0 if "K_CreamA" not in globals().keys() else K_CreamA
    $ K_Les = 0 if "K_Les" not in globals().keys() else K_Les                           #how many times she's done lesbian stuff
    $ K_SexRogue = 0 if "K_SexRogue" not in globals().keys() else K_SexRogue                      #how many times she's had sex involving Rogue
    $ K_SEXP = 0 if "K_SEXP" not in globals().keys() else K_SEXP
    $ K_PlayerFav = 0 if "K_PlayerFav" not in globals().keys() else K_PlayerFav                     #The player's favorite activity with her
    $ K_Favorite = 0 if "K_Favorite" not in globals().keys() else K_Favorite                      #her favorite activity
    $ K_SeenChest = 0 if "K_SeenChest" not in globals().keys() else K_SeenChest
    $ K_SeenPanties = 0 if "K_SeenPanties" not in globals().keys() else K_SeenPanties
    $ K_SeenPussy = 0 if "K_SeenPussy" not in globals().keys() else K_SeenPussy
    $ K_SeenPeen = 0 if "K_SeenPeen" not in globals().keys() else K_SeenPeen                      #How many times she's seen your cock
    $ K_Sleep = 0 if "K_Sleep" not in globals().keys() else K_Sleep 
    $ K_Personality = "normal" if "K_Personality" not in globals().keys() else K_Personality
    $ K_Date = 0 if "K_Date" not in globals().keys() else K_Date 
    $ K_Forced = 0 if "K_Forced" not in globals().keys() else K_Forced                        #This is a toggle for if she's being coerced
    $ K_ForcedCount = 0 if "K_ForcedCount" not in globals().keys() else K_ForcedCount                   #This is a counter for each time she's been coerced lately
#Kitty Sprite Variables
    $ K_Outfit = "pink outfit" if "K_Outfit" not in globals().keys() else K_Outfit
    $ K_OutfitDay = "pink outfit" if "K_OutfitDay" not in globals().keys() else K_OutfitDay
    $ Kitty_Arms = 1 if "Kitty_Arms" not in globals().keys() else Kitty_Arms
    $ K_Emote = "normal" if "K_Emote" not in globals().keys() else K_Emote
    $ K_Arms = 0 if "K_Arms" not in globals().keys() else K_Arms
    $ K_Legs = "capris" if "K_Legs" not in globals().keys() else K_Legs
    $ K_Over = "pink top" if "K_Over" not in globals().keys() else K_Over
    $ K_Chest = "cami" if "K_Chest" not in globals().keys() else K_Chest
    $ K_Pierce = 0 if "K_Pierce" not in globals().keys() else K_Pierce
    $ K_Panties = "green panties" if "K_Panties" not in globals().keys() else K_Panties
    $ K_Neck = "gold necklace" if "K_Neck" not in globals().keys() else K_Neck
    $ K_Hose = 0 if "K_Hose" not in globals().keys() else K_Hose
    $ K_Mouth = "normal" if "K_Mouth" not in globals().keys() else K_Mouth
    $ K_Brows = "normal" if "K_Brows" not in globals().keys() else K_Brows
    $ K_Eyes = "normal" if "K_Eyes" not in globals().keys() else K_Eyes
    $ K_Hair = "evo" if "K_Hair" not in globals().keys() else K_Hair
    $ K_Blush = 0 if "K_Blush" not in globals().keys() else K_Blush
    $ K_Gag = 0 if "K_Gag" not in globals().keys() else K_Gag
    $ K_Spunk = [] if "K_Spunk" not in globals().keys() else K_Spunk
    $ K_Sperm = [] if "K_Sperm" not in globals().keys() else K_Sperm
    $ K_Pubes = 1 if "K_Pubes" not in globals().keys() else K_Pubes
    $ K_Wet = 0 if "K_Wet" not in globals().keys() else K_Wet
    $ K_Water = 0 if "K_Water" not in globals().keys() else K_Water
    $ K_Upskirt = 0 if "K_Upskirt" not in globals().keys() else K_Upskirt
    $ K_PantiesDown = 0 if "K_PantiesDown" not in globals().keys() else K_PantiesDown
    $ K_Uptop = 0 if "K_Uptop" not in globals().keys() else K_Uptop
    $ K_Held = 0 if "K_Held" not in globals().keys() else K_Held
    $ K_Custom = [0,0,0,0,0,0,0,0,0,0,0] if "K_Custom" not in globals().keys() else K_Custom
    $ K_Custom2 = [0,0,0,0,0,0,0,0,0,0,0] if "K_Custom2" not in globals().keys() else K_Custom2
    $ K_Custom3 = [0,0,0,0,0,0,0,0,0,0,0] if "K_Custom3" not in globals().keys() else K_Custom3
    $ K_Gym = [1,0,"shorts",0,0,"sports bra","green panties",0,0,0,0] if "K_Gym" not in globals().keys() else K_Gym
    $ K_Sleepwear = [0,"shorts",0,0,"cami","green panties",0] if "K_Sleepwear" not in globals().keys() else K_Sleepwear
    $ K_Schedule = [0,0,0,0,0,0,0,0,4,0] if "K_Schedule" not in globals().keys() else K_Schedule                      #chooses when she wears what
    $ K_SpriteVer = 0 if "K_SpriteVer" not in globals().keys() else K_SpriteVer
    $ KittyLayer = 100 if "KittyLayer" not in globals().keys() else KittyLayer
    $ K_SpriteLoc = StageCenter if "K_SpriteLoc" not in globals().keys() else K_SpriteLoc                        #Sets Kitty to $ to the center   
#Xavier Sprite Variables    
    $ X_Brows = "happy" if "X_Brows" not in globals().keys() else X_Brows
    $ X_Mouth = "happy" if "X_Mouth" not in globals().keys() else X_Mouth
    $ X_Eyes = "happy" if "X_Eyes" not in globals().keys() else X_Eyes
    $ X_Psychic = 0 if "X_Psychic" not in globals().keys() else X_Psychic
    $ X_Emote = "happy" if "X_Emote" not in globals().keys() else X_Emote
    $ XSpriteLoc = StageCenter if "XSpriteLoc" not in globals().keys() else XSpriteLoc
    return