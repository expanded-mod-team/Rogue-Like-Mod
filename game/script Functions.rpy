
# Stat-ups popups / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
init python:   
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
            HolderCount += 1 if HolderCount < 6 else -5                             #Resets holder screens when it maxes out.            
            return

transform StatAnimation(Timer, XPOS):                         #this is the animation for the Stat ticker
    alpha 0
    pause Timer
    xpos XPOS ypos 0.15 alpha 1
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
    
# End Stat-ups popups / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

init python:
# Start Approval Check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
    def ApprovalCheck(Chr = 0, T = 1000, Type = "LOI", Spread = 150, TmpM = 1, TabM = 0, C = 1, Bonus = 0, Loc = 0, Check=0, Alt=[[],0]):  
            # $ Count = ApprovalCheck(Rogue,125,"L")
            # T is the value being checked against, Type is the LOI condition in play, Spread is the difference between basic approval and high approval
            # TmpM is Tempmod multiplier, TabM is the taboo modifier, C is cologne modifiers, Bonus is a random bonus applied, and Loc is the girl's location
            #figure out a way to send a matrix variable for altering the results based on character Alt=[[RogueX,KittyX],800]
            
            if Chr not in TotalGirls: #should remove "character don't exist" errors
                return 0
                
            while Alt[0]:
                    #if there is an alternate character option. . .
                    if Chr in Alt[0]:
                            T = Alt[1] if Alt[1] else T
                    Alt[0].remove(Alt[0][0])
                                
#            if Type == "X":             #remove eventually as unnecessary
#                if Chr.Lust >= T:
#                    return 1
#                else:
#                    return 0
#            elif Type == "TRST":        #remove eventually as unnecessary
#                return Chr.Thirst  
                
            L = Chr.Love
            O = Chr.Obed
            I = Chr.Inbt
            LocalTaboo = Chr.Taboo
            Loc = Chr.Loc if not Loc else Loc
            
            if Chr.Tag == "Jean" and O <= 900:
                    # Reduces effective value of Inhibition by 500 to a minimum of 0.
                    I = (I - 500) if I >= 500 else 0
                
            if Loc == bg_current and C:
                    #Bumps stats based on colognes
                    if Chr == LauraX:
                            if "mandrill" in Player.Traits:                      
                                    if L <= 400:
                                        L += 600
                                    else:
                                        L = 1200
                                    if "drugged" not in Chr.Traits:
                                            Chr.Traits.append("drugged")
                            elif "purple" in Player.Traits:
                                    if O <= 400:
                                        O += 600
                                    else:
                                        O = 1200
                                    if "drugged" not in Chr.Traits:
                                            Chr.Traits.append("drugged")
                            elif "corruption" in Player.Traits:
                                    if I <= 400:
                                        I += 600
                                    else:
                                        I = 1200   
                                    if "drugged" not in Chr.Traits:
                                            Chr.Traits.append("drugged")                   
                    else:
                            if "mandrill" in Player.Traits:                      
                                    if L <= 500:
                                        L += 500
                                    else:
                                        L = 1000
                            elif "purple" in Player.Traits:
                                    if O <= 500:
                                        O += 500
                                    else:
                                        O = 1000
                            elif "corruption" in Player.Traits:
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
            else:                                                                                                  
                    return 0
# End Approval Check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    
    
# Room Full / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    def Room_Full(Here = [],BO=[]):
            # Culls parties down to 2 max
            # if Room_Full(): do something to empty it.             
            global Party
            Here = []
            while len(Party) > 2:    
                    # If two or more members in the party    
                    #Culls down party size to two
                    Party.remove(Party[2])   
            
            # checks to see which girls are present at a given location
            # adds members who are not currently in the party
            
            BO = TotalGirls[:]  
            while BO:   
                    if BO[0].Loc == bg_current and BO[0] not in Party: 
                                Here.append(BO[0]) 
                    BO.remove(BO[0])            
            if len(Party) + len(Here) >= 2:                
                return 1      
            else:
                return 0              
#end RoomFull  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# AloneCheck / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    def AloneCheck(Girl=0,BO=[]):
            # returns a positive value if alone
            # if Girl, it checks if she's the only one in the room
            BO = TotalGirls[:]  
            if Girl and Girl in TotalGirls:
                    BO.remove(Girl)
            while BO:   
                    if BO[0].Loc == bg_current:
                            return 0
                    BO.remove(BO[0])
            return 1
                   
# End Python Init stuff/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / // / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Time and Space Stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
# Start Round 10 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label Round10(Options = ["none"]):    
        #Called when it's time to auto-wait/sleep
        if Current_Time == "Night":
                    call Sleepover
                    #End night time
                    if "blanket" in RogueX.RecentActions:  
                            $ RogueX.RecentActions.remove("blanket") 
                    if "blanket" in KittyX.RecentActions:
                            $ KittyX.RecentActions.remove("blanket") 
                    if "blanket" in EmmaX.RecentActions:
                            $ EmmaX.RecentActions.remove("blanket") 
                    if "blanket" in LauraX.RecentActions:
                            $ LauraX.RecentActions.remove("blanket")
        else:
                    #if it's not night time, just wait                                                
                    if bg_current == RogueX.Home:
                            if RogueX.Loc == bg_current:
                                ch_r "Sure, you can wait around a bit."     
                            else:
                                "You wait for [RogueX.Name] to return."
                            call Wait
                            if Current_Time == "Night" and RogueX.Loc == bg_current:               
                                if RogueX.Sleep or RogueX.SEXP >= 30:                                                         
                                        #It's late but she really likes you
                                        ch_r "It's pretty late, [RogueX.Petname], but you're welcome to stick around. . ."   
                                elif ApprovalCheck(RogueX, 1000, "LI") or ApprovalCheck(RogueX, 600, "OI"):           
                                        #It's late but she really likes you
                                        ch_r "It's pretty late, [RogueX.Petname], but you can stay for a little bit."     
                                else:                                                                                   
                                        #she likes you well enough but it's late so you should go
                                        ch_r "It's getting a little late [RogueX.Petname]. You should head out." 
                                        $ renpy.pop_call()
                                        jump Campus_Map   
                            #end Rogue's room                
                    elif bg_current == KittyX.Home:
                            if KittyX.Loc == bg_current:
                                ch_k "Sure, you can hang out for a bit."     
                            else:
                                "You wait for Kitty to return."
                            call Wait
                            if Current_Time == "Night" and KittyX.Loc == bg_current:               
                                if KittyX.Sleep or KittyX.SEXP >= 30:                                                         
                                        #It's late but she really likes you
                                        ch_k "It's kinda late, [KittyX.Petname], but you can stay if you like. . ."   
                                elif ApprovalCheck(KittyX, 1000, "LI") or ApprovalCheck(KittyX, 600, "OI"):           
                                        #It's late but she really likes you
                                        ch_k "It's kinda late, [KittyX.Petname], but you can stay for a bit."     
                                else:                                                                                   
                                        #she likes you well enough but it's late so you should go
                                        ch_k "It's getting late [KittyX.Petname]. You should get some sleep." 
                                        $ renpy.pop_call()
                                        jump Campus_Map   
                            #end Kitty's room            
                    elif bg_current == EmmaX.Home:
                            if EmmaX.Loc == bg_current:
                                ch_e "You can stay for a while, if you'd like."     
                            else:
                                "You wait for [EmmaX.Name] to return."
                            call Wait
                            if Current_Time == "Night" and EmmaX.Loc == bg_current:               
                                if EmmaX.Sleep or EmmaX.SEXP >= 30:                                                         
                                        #It's late but she really likes you
                                        ch_e "It's getting a bit late, [EmmaX.Petname], but I'd like you to stay. . ."   
                                elif ApprovalCheck(EmmaX, 1000, "LI") or ApprovalCheck(EmmaX, 600, "OI"):           
                                        #It's late but she really likes you
                                        ch_e "It's getting a bit late, [EmmaX.Petname], but you can stay."     
                                else:                                                                                   
                                        #she likes you well enough but it's late so you should go
                                        ch_e "It's getting late, [EmmaX.Petname]. I need to get some sleep." 
                                        $ renpy.pop_call()
                                        jump Campus_Map   
                            #end Emma's room       
                    elif bg_current == LauraX.Home:
                            if LauraX.Loc == bg_current:
                                ch_l "You can stay."     
                            else:
                                "You wait for [LauraX.Name] to return."
                            call Wait
                            if Current_Time == "Night" and LauraX.Loc == bg_current:               
                                if LauraX.Sleep or LauraX.SEXP >= 30:                                                         
                                        #It's late but she really likes you
                                        ch_l "I'm going to sleep soon. You can stay."   
                                elif ApprovalCheck(LauraX, 1000, "LI") or ApprovalCheck(LauraX, 600, "OI"):           
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
# End Round 10 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
        

#Start Checkout  Overrun checking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Checkout(Total = 0,BO=[]):    
#        call VersionNumber
        
        $ BO = TotalGirls[:]  
        while BO:   
                $ BO[0].Love = 1000 if BO[0].Love > 1000 else BO[0].Love    
                $ BO[0].Obed = 1000 if BO[0].Obed > 1000 else BO[0].Obed    
                $ BO[0].Inbt = 1000 if BO[0].Inbt > 1000 else BO[0].Inbt    
                $ BO[0].Lust = 99 if BO[0].Lust > 99 else BO[0].Lust   
                    
                $ BO[0].Love = 0 if BO[0].Love < 0 else BO[0].Love    
                $ BO[0].Obed = 0 if BO[0].Obed < 0 else BO[0].Obed    
                $ BO[0].Inbt = 0 if BO[0].Inbt < 0 else BO[0].Inbt    
                $ BO[0].Lust = 0 if BO[0].Lust < 0 else BO[0].Lust    
                            
                $ BO[0].Action = BO[0].MaxAction if BO[0].Action > BO[0].MaxAction else BO[0].Action  
                $ BO[0].Action = 0 if BO[0].Action < 0 else BO[0].Action  
                
                $ BO[0].Addict = 100 if BO[0].Addict > 100 else BO[0].Addict  
                $ BO[0].Addict = 0 if BO[0].Addict < 0 else BO[0].Addict  
                $ BO[0].Addictionrate = 10 if BO[0].Addictionrate > 10 else BO[0].Addictionrate  
                $ BO[0].Addictionrate = 0 if BO[0].Addictionrate < 0 else BO[0].Addictionrate  
                $ BO[0].Thirst = 100 if BO[0].Thirst > 100 else BO[0].Thirst 
                $ BO[0].Thirst = 0 if BO[0].Thirst < 0 else BO[0].Thirst 
                
                if BO[0].Forced and BO[0].ForcedCount < 10:
                            $ BO[0].ForcedCount += 1
                if BO[0].Tag == "Laura":
                            $ LauraX.ScentTimer = 0
                $ BO.remove(BO[0])   
                
        #Player
        $ Player.Focus = 99 if Player.Focus > 99 else Player.Focus
        $ Player.Focus = 0 if Player.Focus < 0 else Player.Focus
        $ Player.Semen = Player.Semen_Max if Player.Semen > Player.Semen_Max else Player.Semen  
        $ Player.Semen = 0 if Player.Semen < 0 else Player.Semen   
        
        if Total: 
                $ MultiAction = 1 
                $ Player.DrainWord("cockout")
                $ Player.DrainWord("nude")
                $ Trigger = 0        
                $ Trigger2 = 0
                $ Trigger3 = 0
                $ Trigger4 = 0
                $ Trigger5 = 0
                $ ThreeCount = 100
                $ Partner = 0 
                $ Player.FocusX = 0
        return
#End Checkout  Overrun checking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    

# Wait/Sleep Cycle //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #Wait
label Wait (Outfit = 1, Lights = 1, BO=[]):
    # If Outfit is 1, it changes her clothes to the scheduled default, otherwise it does not. 
    # If Lights is 1, it removes the blackout screen, otherwise it does not. 
    show blackscreen onlayer black 
                            
    call Checkout(1)
    $ Player.XP = 3330 if Player.XP > 3330 else Player.XP
    
    if Time_Count < 3:  #not sleep time                                          
                $ Time_Count += 1
    else:         
        # Things that happen when you sleep                                                  
                $ del Party[:]
                
                #Setting the time/date
                $ Time_Count = 0   
                $ Day += 1
                if Weekday < 6:
                    $ Weekday += 1
                else:
                    $ Weekday = 0
                $ DayofWeek = Week[Weekday]
                
                if PunishmentX: #Event[3]:   
                        #If you're under punishment
                        $ Player.Cash += int(Player.Income / 2)
                        if PunishmentX == 1:
                            "Your punishment from Xavier has expired."
                        $ PunishmentX -= 1
                else:
                        #otherwise, you make money
                        $ Player.Cash += Player.Income             
                
                
        # Things about you when you sleep:
                $ Player.Semen = Player.Semen_Max    
                $ Player.Spunk = 0      
                $ Player.Rep = 0 if Player.Rep < 0 else Player.Rep 
                $ Player.Rep += 10 if Player.Rep < 800 else 0
                $ Player.Rep = 1000 if Player.Rep > 1000 else Player.Rep 
                
                $ TotalSEXP = 0 #zeros out so that next bit and add to it
                
                #Clearing colognes
                if "mandrill" in Player.Traits:  
                        $ Player.Traits.remove("mandrill")
                if "purple" in Player.Traits:
                        $ Player.Traits.remove("purple")  
                if "corruption" in Player.Traits:
                        $ Player.Traits.remove("corruption")  
                call Favorite_Actions # Sets the girl's favorite activities once per day
                        
        # Things about the girls when you sleep:  
                $ BO = TotalGirls[:]                
                while BO:
                        #loops through and makes choices. 
                        if BO[0] in ActiveGirls and BO[0].Loc != bg_current:
                                $ BO[0].Loc = BO[0].Home      
                        if BO[0].Todo:
                                call Todo(BO[0])
                        $ BO[0].Outfit = "sleep"
                        $ BO[0].OutfitChange()
                        
                        #Addiction
                        $ BO[0].Addict += BO[0].Addictionrate   #(0-10)
                        $ BO[0].Addict -= (3*BO[0].Resistance)  #(0,3,6, or 9)                        
                        if "nonaddictive" in Player.Traits:        
                                    $ BO[0].Addictionrate -= 2
                                    $ BO[0].Addict -= 5
                        if "addictive" not in Player.Traits:  
                                    $ BO[0].Addictionrate -= BO[0].Resistance
                                    if BO[0] != RogueX and BO[0].Addictionrate >= 3:
                                            # further bonus for anyone other than Rogue
                                            $ BO[0].Addictionrate -= BO[0].Resistance
                                    
                        $ BO[0].ForcedCount -= 1 if BO[0].ForcedCount > 0 else 0
                        if BO[0].ForcedCount > 0:
                                $ BO[0].ForcedCount -= 1 if ApprovalCheck(BO[0], 1000, "LO") else 0 
                        $ BO[0].Action = BO[0].MaxAction   
                        
                        $ BO[0].Rep = 0 if BO[0].Rep < 0 else BO[0].Rep 
                        $ BO[0].Rep += 10 if BO[0].Rep < 800 else 0
                        $ BO[0].Rep = 1000 if BO[0].Rep > 1000 else BO[0].Rep 
                        $ BO[0].Lust -= 5 if BO[0].Lust >= 50 else 0
                        $ TotalSEXP += BO[0].SEXP #tabulates total based on combined score
                        
                        if BO[0].SEXP >= 15:
                                #raises thirst if you've had sex before
                                if BO[0].SEXP >= 50:
                                    $ BO[0].Thirst += 8 if BO[0].Thirst <= 70 else 4
                                elif BO[0].SEXP >= 25:
                                    $ BO[0].Thirst += 5 if BO[0].Thirst <= 60 else 2
                                else:
                                    $ BO[0].Thirst += 3 if BO[0].Thirst <= 50 else 1
                                    
                                $ BO[0].Thirst -= 5 if BO[0].Break[0] else 0
                                $ BO[0].Thirst += 1 if BO[0].Lust >= 50 else 0 
                        
                        if "gonnafap" in BO[0].DailyActions and BO[0].Loc != bg_current:
                                #if it's morning and she wanted to fap yesterday. . .
                                $ BO[0].Lust = 25
                                $ BO[0].Thirst -= int(BO[0].Thirst/2) if BO[0].Thirst >= 50 else int(BO[0].Thirst/4) 
                        elif "wannafap" in BO[0].DailyActions:
                                #if it's morning and she didn't get to fap yesterday. . .
                                $ BO[0].Thirst += 10 if BO[0].Thirst <= 50 else 5  
                                
                        $ BO[0].Break[0] -= 1 if BO[0].Break[0] > 0 else 0
                        
                        if "painted" not in BO[0].DailyActions or "cleaned" not in BO[0].DailyActions:   
                                $ del BO[0].Spunk[:]  
                            
                        if "lover" in BO[0].Petnames and BO[0].Love > 800:
                                $ BO[0].Love += 10
                        if "master" in BO[0].Petnames and BO[0].Obed > 600:
                                $ BO[0].Obed += 10
                        if "fuck buddy" in BO[0].Petnames:
                                $ BO[0].Inbt += 10   
                                
                        $ BO[0].SluttyClothes   #checks to see if they want to change their default look
                        
                        if BO[0].Tag == "Jean":
                                if BO[0].StatStore and BO[0].Obed >= 900 and BO[0].Love <= 1000:
                                        #for Jean, after her obedience raises above 900, it starts filling her Love stat from her Stored stat
                                        $  BO[0].Love += 5
                                        $  BO[0].StatStore -= 5
                        $ BO.remove(BO[0])
    #End of things when you sleep
                    
    # Things that happen every time you wait            
    #Things that are about you:
    $ Player.Semen += 1    
    $ MultiAction = 1 
    $ Player.Focus -= 5 if Player.Focus >= 10 else 0  
    $ Situation = 0      
    $ Current_Time = Time_Options[(Time_Count)]    
    $ Round = 100 
    # Clears out recent and daily actions    
    $ del Player.RecentActions[:]                            
    if Time_Count == 0: 
            $ del Player.DailyActions[:]            
    call Taboo_Level(0)  
    call GirlWaitUp #checks girls attraction based on who's in the room
    
    #Things that are about the girls:      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    $ BO = TotalGirls[:]  
    while BO:        
            #cycles through each girl possible  
            
            $ BO[0].Action += 1 if Time_Count != 0 else 0  #not morning  
            
            $ BO[0].OCount = 0                
            if BO[0].Lust >= 70 or BO[0].Thirst >= 30 or (renpy.random.randint(1, 40) + BO[0].Lust)>= 70:
                        # checks if she wants to fap
                        if "nofap" in BO[0].Traits:
                                $ BO[0].AddWord(1,0,"wannafap",0,0) #adds "wannafap" tag to daily 
                        else:
                                $ BO[0].AddWord(1,0,"gonnafap",0,0) #adds "wannafap" tag to daily 
                            
            if "les" in BO[0].RecentActions: #if she had a lesbian encounter without you. . .
                        $ BO[0].Thirst -= int(BO[0].Thirst/2) 
                        $ BO[0].Lust = 20 
            
            #Resets her flirt  options
            $ BO[0].Chat[5] = 0  
            #Resets her addiction fix attempts            :
            $ BO[0].Event[3] -= 1 if BO[0].Event[3] else 0 #resets her addiction fix, takes at least five turns before she hassles you again             
            
            $ BO[0].Forced = 0
            if BO[0].Loc == "bg classroom" or BO[0].Loc == "bg dangerroom" :
                    $ BO[0].XP += 10    
            elif BO[0].Loc == "bg showerroom": 
                    call Remove_Girl(BO[0])
                  
            #Appearance clean-up
            $ BO[0].Blush = 0
            $ BO[0].Water = 0
            $ BO[0].Held = 0 
            
            #Reduced addiction
            $ BO[0].Addict += BO[0].Addictionrate # +0-10            
            $ BO[0].Addictionrate -= BO[0].Resistance if BO[0].Addictionrate > 3 else 0         #if rate is above 3, drop it by an extra Resistance
                
            #Adjusts shame rate
            if BO[0].Taboo and BO[0].Shame and BO[0] in ActiveGirls:
                        if BO[0].Loc == "bg dangerroom":            
                                $ BO[0].Shame -= 10 if BO[0].Shame >=10 else BO[0].Shame
                        $ Count = int((BO[0].Taboo * BO[0].Shame) / 200)                    
                        $ BO[0].Statup("Obed", 90, Count)
                        $ BO[0].Statup("Inbt", 90, Count)
                        $ BO[0].Rep -= Count
                    
            #subtracts BO[0].Love by 5* the number of recent unsatisfieds
            $ BO[0].Love -= 5 * BO[0].RecentActions.count("unsatisfied")
                        
            # Clears out recent and daily actions   
            $ del BO[0].RecentActions[:] 
            if "angry" in BO[0].DailyActions:
                        $ BO[0].RecentActions.append("angry")
            if Time_Count == 0: 
                        $ del BO[0].DailyActions[:]
            elif Time_Count == 3 and "yesdate" in BO[0].DailyActions and "stoodup" not in BO[0].Traits:
                        #if you stood her up for a date. . .
                        $ BO[0].Traits.append("stoodup")
                    
            if BO[0].Loose < 2:  #checks how tight the girl's asshole is                   
                        if (BO[0].Anal + BO[0].DildoA + BO[0].Plug) >= 15:
                                $ BO[0].Loose = 2   
                        elif (BO[0].Anal + BO[0].DildoA + BO[0].Plug) >= 3:
                                $ BO[0].Loose = 1
                    
            $ BO[0].XP = 3330 if BO[0].XP > 3330 else BO[0].XP #caps XP
            if BO[0].XP >= BO[0].XPgoal and BO[0].Lvl < 10:
                        $ BO[0].XPgoal = int((1.15 * BO[0].XPgoal) + 100)
                        $ BO[0].Lvl += 1
                        $ BO[0].StatPoints += 1
                        "[BO[0].Name]'s leveled up! I bet she has some new tricks to learn."
                        if BO[0].Lvl == 10:
                                "[BO[0].Name]'s reached max level!"
            if BO[0] == LauraX:
                        $ BO[0].Addictionrate -= (2 * BO[0].Resistance) if BO[0].Addictionrate > 5 else 0
                        
            $ BO[0].DefaultFaces()      #sets a default face based on conditions
            $ BO[0].FaceChange(5)       #resets face
                
            $ BO.remove(BO[0]) 
    #end loop
            
    call Girls_Schedule #schedules all the girls. . .
    
    if Outfit:
            $ BO = TotalGirls[:]                
            while BO:
                    #loops through and makes choices.                
                    $ BO[0].OutfitChange(BO[0].OutfitDay)
                    $ BO.remove(BO[0])
                    
    #Player leveling check
    if Player.Lvl < 10 and Player.XP >= Player.XPgoal:        
            $ Player.XPgoal = int((1.15 * Player.XPgoal) + 100)
            $ Player.Lvl += 1
            $ Player.StatPoints += 1
            if Player.Lvl <5:
                $ Count = 1
            elif Player.Lvl <9:
                $ Count = 2
            else:
                $ Count = 3
            $ Player.Income += Count
            "You've leveled up!"
            "Xavier has noticed your achievements and raised your stipend by $[Count] per day. It is now $[Player.Income]."
            if Player.Lvl == 10:
                "You've reached max level!"
    
    #End Hourly actions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    
    if Time_Count == 1:  
            #if it's post-morning
            $ BO = TotalGirls[:]                
            while BO:
                    #loops through and makes choices.       
                    if "sleepover" in BO[0].Traits: 
                            $ BO[0].Traits.remove("sleepover")
                    $ BO.remove(BO[0])
                
    call LesCheck #checks to see if the girls hook up with each other. . . 
    #end wait items: 
    
    call Checkout
    if Current_Time != "Night":        
            hide NightMask onlayer nightmask  
    if Lights:
            hide blackscreen onlayer black 
    return


# End Wait/Sleep Cycle / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Girl's clothes/location scheduler / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girls_Schedule(Girls = [], Clothes = 1, Location = 1, LocTemp = 0):
        # Set the girl's natural movements        
        # If not Clothes, don't bother with her outfit in the schedule
        # Clothes 2 is ordered to change regardless of time of day
        # If not Location, don't bother with the location portion of the schedule
        if not Girls:
                #fills list unless a specific girl is sent
                $ Girls = ActiveGirls[:]
        elif Girls[0] not in TotalGirls:
                return
        while Girls:
                if Girls[0] in Party and Clothes != 2 or not Location: 
                        #if she's in a party, never mind
                        pass         
                elif Clothes != 2 and "sleepover" in Girls[0].Traits and Current_Time == "morning":
                        #she slept over, so just forget this for now  
                        pass           
                else:                                
                        if (Current_Time == "Morning" and Clothes and Round >= 90) or Clothes == 2:
                                #In the morning, or if ordered to reschedule, pick an outfit for the day. 
                                $ Girls[0].OutfitDay = 0
                                if Girls[0].Break[0]:
                                    pass #she won't pick clothes if she's mad at you
                                elif Girls[0].Clothing[Weekday] == 1:
                                        $ Girls[0].OutfitDay = "casual1"
                                elif Girls[0].Clothing[Weekday] == 2:
                                        $ Girls[0].OutfitDay = "casual2"
                                elif Girls[0].Clothing[Weekday] == 3 and Girls[0].Custom1[0]:
                                        $ Girls[0].OutfitDay = "custom1"
                                elif Girls[0].Clothing[Weekday] == 4:
                                        $ Girls[0].OutfitDay = "gym"
                                elif Girls[0].Clothing[Weekday] == 5 and Girls[0].Custom2[0]:
                                        $ Girls[0].OutfitDay = "custom2"
                                elif Girls[0].Clothing[Weekday] == 6 and Girls[0].Custom3[0]:
                                        $ Girls[0].OutfitDay = "custom3"
                                if not Girls[0].OutfitDay: 
                                        $ Options = ["casual1", "casual2"]
                                        if not Girls[0].Break[0]:
                                                $ Options.append("custom1") if Girls[0].Custom1[0] == 2 else Options
                                                $ Options.append("custom2") if Girls[0].Custom2[0] == 2 else Options
                                                $ Options.append("custom3") if Girls[0].Custom3[0] == 2 else Options
                                        $ renpy.random.shuffle(Options) 
                                        $ Girls[0].OutfitDay = Options[0]
                                        $ del Options[:] 
                                $ Girls[0].Outfit = Girls[0].OutfitDay
                        #End clothing portion
                        
                        #Location portion
                        $ LocTemp = Girls[0].Loc
                        if Girls[0] not in ActiveGirls:
                                $ LocTemp = "hold"
                                $ Girls[0].Loc = "hold"
                        elif Girls[0] in Party or Girls[0].Loc == "hold":
                                pass
                        else:
                                $ Girls[0].Loc = Girls[0].Schedule[Weekday][Time_Count]                        
                                                                
                        if Girls[0].Loc != LocTemp and Girls[0] not in Party:  
                                #if she moved                                                                    
                                if LocTemp == bg_current:                     
                                        if ApprovalCheck(Girls[0], 1200) and Girls[0].Loc not in ("bg classroom","bg teacher","bg dangerroom"):
                                                # if she's contented, then she just sticks around
                                                $ Girls[0].Loc = LocTemp  
                                        else:    
                                                #If she was where you were, but left
                                                $ Girls[0].RecentActions.append("leaving") 
                                elif Girls[0].Loc == bg_current: 
                                                #If she's showed up
                                                $ Girls[0].RecentActions.append("arriving") 
                        if Girls[0] in Nearby:
                                        $ Nearby.remove(Girls[0])    
                $ Girls.remove(Girls[0])
        #end while looping
        return
#End Schedule / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Todo list / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Todo(Chr=0):                       
        #Actions checked each night  
        #causes her to grow her pubes out
        if Chr not in TotalGirls:
            return
                        
        if Chr == LauraX:            
                if "pubes" in Chr.Todo:         
                        $ Chr.Pubes = 1
                        $ Chr.Todo.remove("pubes") 
                
                if "mission" in Chr.Todo: #puts her on ice until a week after the first meeting
                        $ Chr.PubeC -= 1
                        if Chr.PubeC >= 1:
                                $ Chr.Loc = "hold"
                        else:          
                                $ Chr.History.append("dress0") #starts dress event where you'll meet again
                                $ Chr.Todo.remove("mission") 
                if "cleanhouse" in Chr.Todo:
                        #if you promised to break up with other girls, this counts it down
                        if LauraX in Player.Harem or not Player.Harem:
                                # mission complete
                                $ LauraX.Event[5] = 2
                                $ Chr.Todo.remove("cleanhouse")
                        $ LauraX.Event[5] -= 1 if LauraX.Event[5] > 1 else 0
        else:
                if "pubes" in Chr.Todo:  
                        $ Chr.PubeC -= 1
                        if Chr.PubeC >= 1:
                                pass
                        else:            
                                $ Chr.Pubes = 1
                                $ Chr.Todo.remove("pubes") 
        #causes her to wax her pubes
        if "shave" in Chr.Todo:               
                $ Chr.Pubes = 0
                $ Chr.Todo.remove("shave")
                
        #causes her to put in piercings     
        if "ring" in Chr.Todo:                
                $ Chr.Pierce = "ring"
                $ Chr.Todo.remove("ring")
        if "barbell" in Chr.Todo:
                $ Chr.Pierce = "barbell"
                $ Chr.Todo.remove("barbell")            
        return

# End Todo list / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Event Calls / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label EventCalls(EGirls=[]):
        call Present_Check           
        $ D20 = renpy.random.randint(1, 20)       
        call Get_Dressed
        
        if Current_Time == "Evening" and "yesdate" in Player.DailyActions:
            if bg_current == "bg campus": 
                    call DateNight
                    $ Player.DrainWord("yesdate",0,1)
                    return
            else:
                    menu:
                        "You have a date to get to, head for the square?"
                        "Yes":
                            $ renpy.pop_call()
                            jump Campus_Entry
                        "No":
                            "Suit yourself. . ."
        
        if Day < 5 or Round <= 10:
                    #Disables events when it's too early in the game or the turn is about to end 
                    return
                                        
    #Activates Kitty meet                
        if KittyX in ActiveGirls:
                if "Kate" not in KittyX.Names and KittyX.Inbt >= 500 and KittyX.Loc == bg_current:
                        #She calls herself Kate now.
                        call Kitty_Kate
                        return
        else:
                if "traveling" in Player.RecentActions and "met" not in KittyX.History and bg_current == "bg classroom": 
                        jump KittyMeet
                        return
        
    #Activates Laura meet                      
        if LauraX in ActiveGirls:
                    pass
        elif "met" not in LauraX.History and "traveling" in Player.RecentActions:
                    if bg_current == "bg dangerroom":
                            if Day >= 7 and "dress0" not in LauraX.History and "mission" not in LauraX.Todo:
                                    call LauraMeet
                                    return       
                    
                    #Calls Kitty starting dressup event
                    if Current_Time != "Night" and "met" in KittyX.History:
                            if "dress0" in LauraX.History:
                                    call Laura_Dressup
                                    return
            
    #Activates Emma meet and class stuff                       
        if EmmaX in ActiveGirls:
                if bg_current == "bg classroom" and Current_Time == "Evening" and Weekday < 5:
                        #If you've met Emma, it's evening on a school night                    
                        if "traveling" in Player.RecentActions and not Party:
                                #if you are in motion,                            
                                if "classcaught" not in EmmaX.History:   
                                        #if first time you catch her, 100% chance
                                        jump Emma_Caught_Classroom
                                        return     
                                elif D20 <= 10 and "gonnafap" in EmmaX.DailyActions:  
                                        #50/50 chance of catching Emma in class
                                        jump Emma_Caught_Classroom
                                        return   
                        
                        if "detention" in Player.Traits and not Party:    
                                        jump Emma_Detention
                                
                        if Round >= 70:
                                #if you are in class and not travelling. . .
                                $ EmmaX.Loc = "bg classroom"
        else:   
                #Emma is not in ActiveGirls
                if Day >= 6 and "met" not in EmmaX.History and "traveling" in Player.RecentActions and bg_current == "bg classroom" and Weekday < 5:     
                        jump EmmaMeet
                        return   
           
    #activates if you haven't done an addiction event today 
        call AddictCheck            
                                 
    #This scene has Girl A asks Girl B off camera if she wants to have a poly Relationship with you    
        call ShareCheck
        
    #Activates if any girl caught you cheating
        #checks to see if any of the girls noticed you cheating on them
        #returns if not
        call CheatCheck
                                 
    #checks to see if a girl wants to jump you. . .
        call JumperCheck
              
    #Checks to see if any girls want to fap. 
        #If they have "wannafap" in their daily, and "nofap" in their traits, and are not in the room, they will ask you
        #otherwise, they will automatically fap. If you meet them after this, they will be fapping, 
        #if you keep them busy, they will do it overnight
        if Time_Count >= 2 and "fapcall" not in Player.DailyActions:
                #if it's evening or later and nobody has yet called you about fapping. . .
                $ EGirls = ActiveGirls[:]    
                $ renpy.random.shuffle(EGirls)
                while EGirls:
                    if "wannafap" in EGirls[0].DailyActions:
                            #if she's wants to fap and is not in the room with you                         
                            call CalltoFap(EGirls[0]) #checks to see if she's allowed
                            if not EGirls:
                                    return
                    $ EGirls.remove(EGirls[0])
        #end fap call check
        
    #locked door check
        if "locked" in Player.Traits:
                #exits if the door is locked, but maybe open this up a bit later. 
                return
                
    #Start relationship checks
        $ EGirls = ActiveGirls[:]    
        $ renpy.random.shuffle(EGirls)
        #fills list and then randomly shuffles it. 
        while EGirls:
                if "relationship" not in EGirls[0].DailyActions:
                        if "stoodup" in EGirls[0].Traits: #you stood her up
                                        call Date_Stood_Up(EGirls[0])
                                        return  
                        if EGirls[0].Break[0] or "angry" in EGirls[0].DailyActions:
                                        #skip all this if you're broken up
                                        pass
                        elif not EGirls[0].Event[0] and EGirls[0].Sleep >= 5:               
                                if EGirls[0].Loc == bg_current or EGirls[0] in Party:
                                        call expression EGirls[0].Tag + "_Key"
                                        return  
                        elif "boyfriend" not in EGirls[0].Petnames and EGirls[0].Love >= 800 and EGirls[0].Event[5] != 20 and EGirls[0].Tag + "No" not in Player.Traits: # EGirls[0].Event[5]
                                # EGirls[0].Event[5] is 20 if you refused due to other girlfriend    
                                # if "RogueNo" it means you can't date her.    
                                if EGirls[0] == LauraX and LauraX.Event[5] == 3:
                                        call Laura_Cleanhouse
                                        return
                                elif Player.Harem and EGirls[0].Tag + "Yes" not in Player.Traits:
                                        call Poly_Start(EGirls[0])    
                                        return
                                elif bg_current == EGirls[0].Home or bg_current == "bg player":
                                        call expression EGirls[0].Tag + "_BF"
                                        return
                                else:
                                        call AskedMeet(EGirls[0],"bemused")   
                        elif "lover" not in EGirls[0].Petnames and EGirls[0].Love >= 950 and EGirls[0].Event[6] < 15: # EGirls[0].Event[6]   
                                # <15 is also != 20, but double check that there isn't more to that. . .K_Event[6] != 20? and E_Event[6] != 20:
                                if bg_current == EGirls[0].Home or bg_current == "bg player":
                                        call expression EGirls[0].Tag + "_Love"
                                        return
                                else:
                                        call AskedMeet(EGirls[0],"bemused")   
                        elif "sir" not in EGirls[0].History and "sir" not in EGirls[0].Petnames and EGirls[0].Obed >= 500: # EGirls[0].Event[7]
                                if bg_current == EGirls[0].Home or bg_current == "bg player":
                                        call expression EGirls[0].Tag + "_Sub"
                                        return
                                else:
                                        call AskedMeet(EGirls[0],"bemused")
                        elif "master" not in EGirls[0].History and "master" not in EGirls[0].Petnames and EGirls[0].Obed >= 850 and EGirls[0].Event[8] < 2: 
                                #and EGirls[0].Event[8] < 2, remove that bit when Rogue's scene is updated to not need it. 
                                if bg_current == EGirls[0].Home or bg_current == "bg player":
                                        call expression EGirls[0].Tag + "_Master"
                                        return
                                else:
                                        call AskedMeet(EGirls[0],"bemused")
                        elif "daddy" not in EGirls[0].Petnames and ApprovalCheck(EGirls[0], 750, "L") and ApprovalCheck(EGirls[0], 500, "O") and ApprovalCheck(EGirls[0], 500, "I"): # EGirls[0].Event[5]
                                if bg_current == EGirls[0].Home or bg_current == "bg player" and EGirls[0].Loc == bg_current:
                                        call expression EGirls[0].Tag + "_Daddy"
                                        return
                                        
                        elif "sex friend" not in EGirls[0].Petnames and EGirls[0].Inbt >= 500: # EGirls[0].Event[9]  Fix this one
                                if EGirls[0] == EmmaX:
                                        if bg_current == "bg classroom" and Time_Count == 2: # E_Event[9]  Fix this one
                                                    call Emma_Sexfriend
                                                    return  
                                elif bg_current == EGirls[0].Home or bg_current == "bg player":  
                                        call expression EGirls[0].Tag + "_Sexfriend"
                                        return
                                elif "dating" in EGirls[0].Traits and EGirls[0].Loc == bg_current:
                                        call expression EGirls[0].Tag + "_Sexfriend"   
                                        return
                                elif EGirls[0] == LauraX:                                    
                                        call expression EGirls[0].Tag + "_Sexfriend"   
                                        return
                                else:
                                        call AskedMeet(EGirls[0],"bemused")
                        
                        elif "fuck buddy" not in EGirls[0].Petnames and EGirls[0].Inbt >= 800: # EGirls[0].Event[10]  Fix this one 
                                if EGirls[0] != RogueX and bg_current != EGirls[0].Loc:
                                        call expression EGirls[0].Tag + "_Fuckbuddy"
                                        return
                                elif bg_current == EGirls[0].Home or bg_current == "bg player":
                                        call expression EGirls[0].Tag + "_Fuckbuddy"
                                        return
                                elif "dating" in EGirls[0].Traits and EGirls[0].Loc == bg_current:
                                        call expression EGirls[0].Tag + "_Fuckbuddy" 
                                        return   
                                else:
                                        call AskedMeet(EGirls[0],"bemused")
                $ EGirls.remove(EGirls[0])  
        # EndPrimary Event Calls / / / / / / / / / / / / / / / / / Drops down to. . .
       
label QuickEvents(EGirls=[]):                                              
        #These events get checked every screen refresh
        $ Options = []       
        call Present_Check
        
        $ EGirls = TotalGirls[:]   
        $ renpy.random.shuffle(EGirls)
        while EGirls:                         
                if EGirls[0].Loc == bg_current:
                        if EGirls[0].Lust >= 90:       
                                $ EGirls[0].Blush = 1
                                $ EGirls[0].Wet = 2 
                        elif EGirls[0].Lust >= 60:        
                                $ EGirls[0].Blush = 1
                                $ EGirls[0].Wet = 1
                        else:
                                $ EGirls[0].Wet = 0
                                
                        #Girl reacts to getting horny
                        if Taboo and EGirls[0].Lust >= 75:
                                if EGirls[0].Inbt > 800 or "exhibitionist" in EGirls[0].Traits:
                                        "[EGirls[0].Name] gets a sly smile on her face and squirms a bit."
                                elif EGirls[0].Inbt > 500 and EGirls[0].Lust < 90:
                                        "[EGirls[0].Name] looks a bit flushed and uncomfortable."
                                elif bg_current != "bg showerroom":
                                        "[EGirls[0].Name] gets an embarrassed look on her face and suddenly leaves the room."
                                        call Remove_Girl(EGirls[0])
                                        call Set_The_Scene        
                else:
                        #if Girl is not around
                        if EGirls[0].Loc == "bg showerroom" and "showered" in EGirls[0].DailyActions:
                                #if she's recently showered and still in the shower, send her elsewhere
                                $ EGirls[0].Loc = EGirls[0].Schedule[Weekday][Time_Count]  
                                $ EGirls[0].OutfitChange()
                #End girl's Quick Events  
                $ EGirls.remove(EGirls[0])      
        return   
#End Quick Events
# End Event Calls / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label AskedMeet(Girl = 0, Emotion = "bemused"): # Use AskedMeet(RogueX,"angry")
    #This asks the player to meet the chosen character later    
    if "asked meet" in Girl.DailyActions:
                    $ Girl.FaceChange(Emotion)
                    "[Girl.Name] asks if you could meet her in your room later."
                    $ Girl.AddWord(1,"asked meet","asked meet",0,0) # adds "asked meet" to recent and daily
                    $ Player.AddWord(1,0,"meet girl",0,0)
    return
    
# End Asked Meet / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# start Tutorial //////////////////////////////////////////////////////////
menu Tutorial:
    "What did you want to know about?"
    "UI":
        while True:
            menu:                
                "Which UI element did you want to hear about?"
                "Relationship Bar":
                        "The bar covering the top left of the screen displays the stats of the primary girl in the scene. These stats are described elsewhere in the tutorial."
                        "If the bar is green, it represents Rogue's stats. If it's dark blue, it represents Kitty's."
                "Focus Button":
                        "You can switch between available girls by hitting the small blue icon to the right of the Relationship Bar." 
                        "This changes which girl is currently the focus of your attention. You can do this as often as you like."
                "Inventory":
                        "The small backpack to the left of that is your inventory."
                "Time":
                        "The next panel shows the day since you started, the day of the week, and the time of day."
                        "There are four periods in the day, Morning, Midday, Evening, and Night, representing roughly 4 hours each (not counting sleep time"   
                "Menus":
                        "Much of the gameplay choices are made via menus along the left side of the screen."
                        "Don't worry too much about making \"bad\" choices, they are only temporary setbacks."
                        "There are no absolute fail states, and even choices that upset a girl can have eventual payoffs."
                        "Play how you want to play, have fun."
                "Back":
                    jump Tutorial
    "Stats":
        menu Tutorial_Stats: 
            "Which stat were you interested in?"
            "Relationship Stats":
                "Stats are what is used to track your progress with the various girls in the mansion."
                while True:
                    menu:
                        "Which Stat would you like to hear about?"
                        "Love Stat":
                                "If you look at the top-left of the screen, there is a red bar."
                                "This represents the girl's \"love level.\""
                                "You can raise this stat by doing things that make the girl happy. This produces a red +X number."
                                $ RogueX.Statup("Love", 200, 1)
                                "You can also lower this number if you do things that make the girl upset, which is represented by a red -X."
                                $ RogueX.Statup("Love", 200, -1)
                        "Obedience Stat":
                                "The blue bar to the right of that is the \"Obedience level.\""
                                "This represents the girl's willingness to do what you want, and raises when you convince her to do something."
                                $ RogueX.Statup("Obed", 200, 1)
                                "It lowers when you push her too far and she refuses."
                                $ RogueX.Statup("Obed", 200, -1)
                        "Inhibition Stat":
                                "The yellow bar to the right of that is the \"Inhibition level.\""
                                "This represent's the girl's own sexual interest, and raises when she decides to do something on her own, or something naughty for the first time."
                                $ RogueX.Statup("Inbt", 200, 1)
                                "It lowers when she becomes overly ashamed, like when caught doing something sexier than she's comfortable with."
                                $ RogueX.Statup("Inbt", 200, -1)
                                "These are the three core relationship stats, and most activities in the game are gated by how high each is, either alone or in combinations."
                                "If you can reach 1000 in all three stats, she will be up for just about anything, although some activities do require special conditions." 
                        "Back":
                                jump Tutorial_Stats
            "Sexual stats":
                "There are several stats which are used in sexual encounters."
                while True:
                    menu:
                        "Which Stat would you like to hear about?"
                        "Lust":                    
                                "The bar underneath \"Love\" represents the girl's \"Lust.\""
                                "This stat raises as she becomes excited, and falls as she gets turned off or after she orgasms (at 100\%)."
                                $ RogueX.Statup("Lust", 200, 1)
                                $ RogueX.Lust -= 1
                        "Player Excitement":
                                "The rather \"suggestive\" bar to the right of Inhibitions represents your own excitement." 
                                $ Player.Statup("Focus", 200, 1)
                                $ Player.Focus -= 1
                                "When it reaches 100\%, you orgasm. If you wish to delay this, you can learn to \"focus\" during sex and slow the progression."                
                                "The better you get at each sexual activity, the faster these stats will rise."
                                "The bar underneath this represents the amount of times you can \"get it up\" before needing some time out. You can raise this stat when you level."
                                "It's also worth noting that each girl will only be up for doing a certain number of activities in a given time period."
                        "Back":
                                jump Tutorial_Stats                            
            "Player Stats":
                    "Aside from the sexual ones mentioned above, the player has a few stats of note."                
                    "One is his XP. This raises as you study, attend classes, or attend training sessions."
                    "It represents your advancement as a mutant student of the academy. As you gain levels, you gain stat points."
                    "You can spend these to unlock new traits, either refining your powers or your sexual prowess."
                    "The girls also gain traits which unlock new abilities."
                    "You also have an income level, based on the stipend Xavier grants you. This rises as you level, but may be reduced for bad behavior."            
            "Addiction":
                    "The Addiction stat is represented by the bar below Obedience. This stat rises as she begins to crave your touch."
                    "It lowers when she comes into physical contact with you, the more intense the contact, the lower the craving gets."
                    "At high Addiction levels, she is highly susceptible to your advances, but will not be happy about it if you press her."
                    "The Addiction Rate is represented by the bar to the right of it. This stat represents how quickly her cravings build, and falls off over time."
                    "There are various ways that you can increase or decrease how addictive your touch becomes to her. Use this capability at your own risk." 
                    "If this aspect does not interest you, you can just choose the more benign options to satisfy her cravings until her interest dies down."
            "Back":                
                    jump Tutorial
        jump Tutorial_Stats
    "Activities":
        while True:
            menu:
                "So what can you do with your time?"
                "Wait/Sleep":
                        "You can always just \"Wait.\" This causes you to waste time, but who knows, maybe something interesting will happen."
                        "Of course when it's night time, this becomes \"Sleep.\" You can only sleep in your own room at first, but maybe someone else would let you sleep in her room."
                "Shop":
                        "You can also access the school's fabricator store, where you can order various items to be delivered to your room."
                "Class":
                        "You can always attend classes. These are typically not that interesting, but will raise your XP, and various events might occur in class."
                        "Classes are open during weekday morning and midday periods. You might bump into Rogue there."
                        "You can access the classroom by using \"Leave [[Go to Campus Square].\""                        
                "Danger Room":
                        "You can also attend a Danger Room training session. These also raise your XP."
                        "The Danger Room is open any time except late at night (students need their sleep)."
                        "You can access the Danger Room by using \"Leave [[Go to Campus Square].\""
                "Shower": 
                        "You can also take a shower, but don't worry, you'll do that off camera automatically if you don't get around to it."
                        "You can access the showers by using \"Leave [[Go to Campus Square].\""
                "Study":
                        "You can also choose to study with one of the other students. This will gain you XP, and who knows what else might happen?"
                "Dating":    
                        "You can also go out on a date with one of the other students in the evenings. She will probably expect you to pay, so be prepared."
                "Chat":    
                        "And of course you can just hang out with one of the other students, or talk to them on the phone if you have their number." 
                "Back":                
                        jump Tutorial
              
    "Never mind.":
        return
jump Tutorial

label SpecialMenu:
    while True:
        menu:
            "Tutorial":
                    jump Tutorial                        
            "Statchecker" if False:
                    "This element will check all the stats and make sure that they work in your current savegame."
                    "This is a good idea if you're getting 'variable not found' syle errors."
                    menu:
                        "Do you want to do this?"
                        "Yes":
                                $ renpy.pop_call()
                                call Failsafe
                                jump Player_Room
                        "Never mind.":
                                pass
            "Visit McCoy's lab to change things about myself.":
                    call Hanks_Lab    
            "Reset Custom Outfits":
                    call Emergency_Clothing_Reset
            "Leveling Menu":
                while True:
                    menu:
                        "Level-up menu"
                        "Level Yourself":
                                call Level_Up(Player)
                        "Level Yourself [[No points to spend] (locked)" if Player.StatPoints <= 0:
                                pass
                        "Level [RogueX.Name]" if RogueX.StatPoints > 0:
                                call Level_Up(RogueX)
                        "Level [KittyX.Name]" if KittyX.StatPoints > 0 and "met" in KittyX.History:
                                call Level_Up(KittyX)
                        "Level [EmmaX.Name]" if EmmaX.StatPoints > 0 and "met" in EmmaX.History:
                                call Level_Up(EmmaX)
                        "Level [LauraX.Name]" if LauraX.StatPoints > 0 and "met" in LauraX.History:
                                call Level_Up(LauraX)
                        "Back":
                                jump SpecialMenu
                "You need to gain experience first by training or going to class."
                
            "Activate Travel Mode" if not TravelMode:
                    "This mode causes you to travel directly to adjacent areas, but not directly to more distant ones."
                    "If you would prefer to use the default, more \"world map\" style of travel, you can toggle this back off."
                    "You can use \"Leave\" to open the location directory." 
                    $ TravelMode = 1
            "Deactivate Travel Mode" if TravelMode:
                    $ TravelMode = 0
            
            "Press the red button" if False:
                "Huh, wonder what that was about. . ."
                    
            "Never mind.":
                return
    return
# end Tutorial//////////////////////////////////////////////////////////

# start Hank's Lab//////////////////////////////////////////////////////////
label Hanks_Lab(Line=0):
        "This is Professor McCoy's lab. You can do various self-modifications here."
        "The changes will be so seemless, it's almost like nobody will even notice!"
        while True:
            $ Line = 0
            menu:
                "What would you like to do?"
                "Alter skin color":  
                        menu:
                            "What skin color would you like?"        
                            "Green":
                                    $ Player.Color = "green"
                            "White":
                                    $ Player.Color = "pink"
                            "Black":
                                    $ Player.Color = "brown"
                            "Never mind":
                                    $ Line = 1
                        if not Line:
                                "You fiddle with some of McCoy's machinery and a glowing blue liquid pours into a flask."                    
                                "You down it in a single gulp, and within minutes your skin tone shifts to be more [Player.Color]ish."
                    
                "Change my name.":
                            "You log in to McCoy's high end computer, this should allow you to change your name in all offical databases."  
                            $ Player.Name = renpy.input("What name would you like?", default="Zero", length = 10)
                            $ Player.Name = Player.Name.strip()        
                            if not Player.Name:
                                    $ Player.Name = "Zero"
                            if Player.Name in ("master", "sir", "lover", "boyfriend", "sex friend", "fuck buddy"):
                                    "Nice try, smartass."
                                    $ Player.Name = "Zero"  
                            if "met" in KittyX.History:
                                    $ KittyX.Petnames.append(Player.Name[:1])
                            if "met" in EmmaX.History:
                                    call LastNamer                         
                                    $ EmmaX.Petnames.append(_return)
                            "That should do it, your name has been updated and an email has been sent out to everyne on campus about the change."
                "Red Button":
                            if not Player.Harem:
                                "No harem"
                            elif len(Player.Harem) == 4:
                                "[Player.Harem[0].Tag],[Player.Harem[1].Tag],[Player.Harem[2].Tag],[Player.Harem[3].Tag]"
                            elif len(Player.Harem) == 3:
                                "[Player.Harem[0].Tag],[Player.Harem[1].Tag],[Player.Harem[2].Tag]"
                            elif len(Player.Harem) == 2:
                                "[Player.Harem[0].Tag],[Player.Harem[1].Tag]"
                            else:
                                "[Player.Harem[0].Tag]"            
                "Blue Button":
                            $ Count = len(ActiveGirls)
                            "[Count]"
                            if len(ActiveGirls) == 8:
                                "A-[ActiveGirls[0].Tag],[ActiveGirls[1].Tag],[ActiveGirls[2].Tag],[ActiveGirls[3].Tag]"
                                "B-[ActiveGirls[4].Tag],[ActiveGirls[5].Tag],[ActiveGirls[6].Tag],[ActiveGirls[7].Tag]"
                            elif len(ActiveGirls) == 7:
                                "A-[ActiveGirls[0].Tag],[ActiveGirls[1].Tag],[ActiveGirls[2].Tag],[ActiveGirls[3].Tag]"
                                "B-[ActiveGirls[4].Tag],[ActiveGirls[5].Tag],[ActiveGirls[6].Tag]"
                            elif len(ActiveGirls) == 6:
                                "A-[ActiveGirls[0].Tag],[ActiveGirls[1].Tag],[ActiveGirls[2].Tag],[ActiveGirls[3].Tag]"
                                "B-[ActiveGirls[4].Tag],[ActiveGirls[5].Tag]"
                            elif len(ActiveGirls) == 5:
                                "A-[ActiveGirls[0].Tag],[ActiveGirls[1].Tag],[ActiveGirls[2].Tag],[ActiveGirls[3].Tag]"
                                "B-[ActiveGirls[4].Tag]"
                            elif len(ActiveGirls) == 4:
                                "[ActiveGirls[0].Tag],[ActiveGirls[1].Tag],[ActiveGirls[2].Tag],[ActiveGirls[3].Tag]"
                            elif len(ActiveGirls) == 3:
                                "[ActiveGirls[0].Tag],[ActiveGirls[1].Tag],[ActiveGirls[2].Tag]"
                            elif len(ActiveGirls) == 2:
                                "[ActiveGirls[0].Tag],[ActiveGirls[1].Tag]"
                            else:
                                "[ActiveGirls[0].Tag]"    
                            $ Count = 0                
                "Yellow Button":
                            $ Count = len(TotalGirls)
                            "[Count]"
                            if len(TotalGirls) == 8:
                                "A-[TotalGirls[0].Tag],[TotalGirls[1].Tag],[TotalGirls[2].Tag],[TotalGirls[3].Tag]"
                                "B-[TotalGirls[4].Tag],[TotalGirls[5].Tag],[TotalGirls[6].Tag],[TotalGirls[7].Tag]"
                            elif len(TotalGirls) == 7:
                                "A-[TotalGirls[0].Tag],[TotalGirls[1].Tag],[TotalGirls[2].Tag],[TotalGirls[3].Tag]"
                                "B-[TotalGirls[4].Tag],[TotalGirls[5].Tag],[TotalGirls[6].Tag]"
                            elif len(TotalGirls) == 6:
                                "A-[TotalGirls[0].Tag],[TotalGirls[1].Tag],[TotalGirls[2].Tag],[TotalGirls[3].Tag]"
                                "B-[TotalGirls[4].Tag],[TotalGirls[5].Tag]"
                            elif len(TotalGirls) == 5:
                                "A-[TotalGirls[0].Tag],[TotalGirls[1].Tag],[TotalGirls[2].Tag],[TotalGirls[3].Tag]"
                                "B-[TotalGirls[4].Tag]"
                            elif len(TotalGirls) == 4:
                                "[TotalGirls[0].Tag],[TotalGirls[1].Tag],[TotalGirls[2].Tag],[TotalGirls[3].Tag]"
                            elif len(TotalGirls) == 3:
                                "[TotalGirls[0].Tag],[TotalGirls[1].Tag],[TotalGirls[2].Tag]"
                            elif len(TotalGirls) == 2:
                                "[TotalGirls[0].Tag],[TotalGirls[1].Tag]"
                            else:
                                "[TotalGirls[0].Tag]"    
                            $ Count = 0       
                "Leave.":
                            return
        
        return

# end Hank's Lab//////////////////////////////////////////////////////////

# Start player/girl leveling / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Level_Up(Chr=Player):
        if Chr != Player and Chr not in TotalGirls:
            return
        if Chr == Player:
            while Player.StatPoints > 0 or "addict control" in Player.Traits:
                menu:
                    "You have [Player.StatPoints] points to spend. How would you like to spend them?"
                    "Increase sexual stamina. [[One point]" if "focus" not in Player.Traits:
                        menu:
                            "This trait will unlock the \"Focus\" option during sex, giving you more time before you blow."
                            "Unlock Focus.":
                                if Player.StatPoints > 0:
                                        $ Player.StatPoints -= 1  
                                        $ Player.Traits.append("focus") 
                                else:
                                        "You don't have enough points for that."
                            "Cancel.":
                                        pass
                                
                    "Increase your addictiveness. [[One point]" if "addict control" not in Player.Traits and "nonaddictive" not in Player.Traits and "addictive" not in Player.Traits:
                        menu:
                            "This trait will increase the addictiveness of your touch, making you harder for girls to quit."
                            "Increase addictiveness.":
                                if Player.StatPoints > 0:
                                        $ Player.StatPoints -= 1 
                                        $ Player.Traits.append("addictive") 
                                else:
                                        "You don't have enough points for that."
                            "Cancel.":
                                        pass
                                
                    "Reduce your addictiveness. [[One point]" if "addict control" not in Player.Traits and "nonaddictive" not in Player.Traits and "addictive" not in Player.Traits:
                        menu:
                            "This trait will reduce the addictiveness of your touch, making it easier for girls to resist it."
                            "Reduce addictiveness.":
                                if Player.StatPoints > 0:
                                        $ Player.StatPoints -= 1 
                                        $ Player.Traits.append("nonaddictive") 
                                else:
                                        "You don't have enough points for that."
                            "Cancel.":
                                        pass
                                
                    "Control your Addiction level. [[Two points]" if "addict control" not in Player.Traits and ("nonaddictive" in Player.Traits or "addictive" in Player.Traits):
                        menu:
                            "This trait will allow you to freely control the amount you addict girls to your touch."
                            "Gain addiction control.":
                                if Player.StatPoints >= 2:
                                        $ Player.StatPoints -= 2 
                                        $ Player.Traits.append("addict control") 
                                else:
                                        "You don't have enough points for that."
                            "Cancel.":
                                        pass       
                                
                    "Increase your addictiveness. [[Free]" if "addict control" in Player.Traits: #If you have Addict-control
                        menu:
                            "This trait will increase the addictiveness of your touch, making you harder for girls to quit."
                            "Increase addictiveness, no cost.":
                                if "nonaddictive" in Player.Traits:
                                        $ Player.Traits.remove("nonaddictive")
                                        "You are now at the baseline addictiveness level."
                                elif "addictive" not in Player.Traits:
                                        $ Player.Traits.append("addictive") 
                                        "You are now at the enhanced addictiveness level."
                                else:
                                        "You are already at the max addictiveness level."
                            "Cancel.":
                                        pass
                    "Reduce your addictiveness. [[Free]" if "addict control" in Player.Traits:
                        menu:
                            "This trait will reduce the addictiveness of your touch, making it easier for girls to resist it."
                            "Reduce addictiveness.":
                                if "addictive" in Player.Traits:
                                        $ Player.Traits.remove("addictive")
                                        "You are now at the baseline addictiveness level."
                                elif "nonaddictive" not in Player.Traits:
                                        $ Player.Traits.append("nonaddictive") 
                                        "You are now at the reduced addictiveness level."
                                else:
                                        "You are already at the minimum addictiveness level."                
                                
                                if "addictive" in Player.Traits:
                                        $ Player.Traits.remove("addictive") 
                                        $ Player.Traits.append("nonaddictive") 
                                        $ Player.Traits.append("addict control") 
                                else:
                                        $ Player.Traits.append("nonaddictive") 
                            "Cancel.":
                                        pass
                                
                    "Increase semen production. [[One point]" if Player.Semen_Max < 5:            
                        menu:
                            "This trait will increase by 1 the number of times you can climax before needing a break."
                            "Increase max semen.":                    
                                if Player.StatPoints > 0:
                                        $ Player.StatPoints -= 1  
                                        $ Player.Semen_Max += 1
                                else:
                                        "You don't have enough points for that."
                                if Player.Semen_Max >= 5:
                                        "You're already at the max level."
                            "Cancel.":
                                        pass
                                                
                    "Never Mind, I'll come back later.":
                                        return
        else:       
            #Girls leveling system
            while Chr.StatPoints > 0:
                menu:
                    "[Chr.Name] is Level [Chr.Lvl] and has [Chr.StatPoints] points to spend. How would you like to spend them?"
                    "Increase sexual focus. [[One point]" if "focus" not in Chr.Traits:
                        menu:
                            "This trait will unlock the \"Focus\" option during sex, giving [Chr.Name] more time before she orgasms."
                            "Unlock Focus.":
                                if Chr.StatPoints:
                                        $ Chr.StatPoints -= 1  
                                        $ Chr.Traits.append("focus") 
                                else:
                                        "You don't have enough points for that."
                            "Cancel.":
                                pass                   
                 
                    "Increase [Chr.Name]'s resistance. [[One point]" if 0 < Chr.Resistance < 3:
                        menu:
                            "This trait will increase [Chr.Name]'s resistance to your touch's addictive properties."
                            "Increase Resistance.":
                                if Chr.StatPoints:
                                        $ Chr.StatPoints -= 1  
                                        $ Chr.Resistance += 1 
                                else:
                                        "You don't have enough points for that."
                            "Cancel.":
                                        pass    
                            
                                
                    "Increase stamina. [[One point]" if Chr.MaxAction < 10:
                        "This trait will increase by 2 the number of sex actions [Chr.Name] can take before needing a break."
                        menu:
                            "She currently has [Chr.MaxAction] actions."
                            "Increase sex actions.":
                                if Chr.StatPoints:
                                    $ Chr.StatPoints -= 1  
                                    $ Chr.MaxAction += 2
                                    if Chr.MaxAction > 10:
                                        $ Chr.MaxAction = 10
                                        "[Chr.Name] has reached her maximum actions."
                                else:
                                        "You don't have enough points for that."
                            "Cancel.":
                                        pass
                                
                    "Allow [Chr.Name] to touch. [[One point]" if Chr == RogueX and "touch" not in Chr.Traits and Chr.Lvl >= 5:
                        "This trait will allow [Chr.Name] to touch other people, not just you, without harming them."
                        menu:
                            "She can still borrow their abilities if they have any."
                            "Unlock touch ability.":                    
                                if Chr.StatPoints:
                                        $ Chr.StatPoints -= 1  
                                        $ Chr.Traits.append("touch") 
                                else:
                                        "You don't have enough points for that."
                            "Cancel.":
                                        pass
                                
                    "Allow [Chr.Name] to permanently Steal. [[Two points]" if Chr == RogueX and "touch" in Chr.Traits and "steal" not in Chr.Traits:
                        "This trait will allow [Chr.Name] to permanently copy one other mutant ability at a time."            
                        menu:
                            "This does not harm the person she borrows from and can switch abilities with a touch."
                            "Unlock steal ability.":
                                if Chr.StatPoints >= 2:
                                        $ Chr.StatPoints -= 2  
                                        $ Chr.Traits.append("steal") 
                                else:
                                        "You don't have enough points for that."                    
                            "Cancel.":
                                        pass
                    "Never Mind, I'll come back later.":
                                        return
            
        return
       
# End leveling menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Remove Girl / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
label Remove_Girl(Girl = 0, HideGirl = 1, Hold=0,BO=[]):
        # Girl is the girl being removed, this is for putting girls in a safe location if they run.  
        # "Hold" is sent by Present_Check/Girls_Arrive, if active, and you are in public, it sets the girl nearby 
        
        if Partner == Girl or Girl == "All":
                $ Partner = 0    
        if Girl == "All":
                $ Party = []
                $ Nearby = []
        else:        
                while Girl in Party:        
                        $ Party.remove(Girl)
                while Girl in Present:
                        $ Present.remove(Girl)
                while Girl in Nearby:
                        $ Nearby.remove(Girl)
            
        if Girl == "All":   
                    $ BO = TotalGirls[:]  
        else:
                    $ BO = [Girl]
                    
        while BO:
                $ BO[0].DrainWord("leaving",1,0,0)            
                $ BO[0].DrainWord("arriving",1,0,0)
                
                if BO[0].Loc == bg_current or (bg_current == "bg classroom" and BO[0].Loc == "bg teacher"):  
                    if Hold and bg_current in ("bg campus","bg classroom","bg dangerroom"):
                            # "Hold" is sent by Present_Check/Girls_Arrive, if active, and you are in public, it sets the girl nearby 
                            if BO[0] not in Nearby:
                                    $ Nearby.append(BO[0])
                            $ BO[0].Loc = "nearby"
                    elif bg_current == BO[0].Home:
                            #if you are in the girl's room, send her to the campus
                            $ BO[0].Loc = "bg campus"
                    else:
                            #if you are not in the girl's room, send her home
                            $ BO[0].Loc = BO[0].Home
                        
                #below portion visually removes girls. 
                if HideGirl:
                            call expression BO[0].Tag + "_Hide" pass (1)
                $ BO.remove(BO[0])
        return
# End Remove Girl / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 


# Start Clear the Room / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label CleartheRoom(Character = 0, Passive = 0, Silent = 0, Girls=[],BO=[]):
        #This is intended to clear the room of non-essential characters
        #the named character is the one who stays, everyone else is kicked out.
        #Character is the one asking to clear the room. 
        #Passive is when the second person leaves on their own. 
        #Silent removes dialog
        # call CleartheRoom(RogueX,1,1)
        
        #this populates a list of other girls at the current location
        if not Silent and bg_current not in PersonalRooms and Time_Count <= 1:
                    #if it's not a player room and it's not evening+, give up on whatever this is supposed to be
                    #Fix this mess, It's breaking Kitty's intro scene anyway. . .
                    jump Misplaced
        
        $ BO = TotalGirls[:]  
        while BO:                   
                if Character != BO[0] and (BO[0].Loc == bg_current or BO[0] in Party):
                        $ Girls.append(BO[0]) 
                $ BO.remove(BO[0])
        if Character != EmmaX and EmmaX not in Girls and EmmaX.Loc == "bg teacher" and bg_current == "bg classroom":        
                $ Girls.append(EmmaX)
                                                            
        $ Nearby = [] #empties the nearby list
        
        if not Silent and not Passive:
                #this section asks a question that a later phase will answer   
                if Character.Loc != bg_current:
                    "[Character.Name] enters the room."
                    $ Character.Loc = bg_current
                if Character == RogueX:
                        # if the clearing character is Rogue
                        if len(Girls) > 1:
                            #if there is at least two other girls. . .
                            ch_r "Ladies, could I talk to [Player.Name] alone for a minute?"
                        elif Girls:
                            #if there is at least one other girl. . .
                            ch_r "[Girls[0].Name], could I talk to [Player.Name] alone for a minute?"
                        else:
                            #if there is no other girl. . .
                            return
                elif Character == KittyX:                             
                        if len(Girls) > 1:
                            ch_k "Girls, could I talk to [Player.Name] alone for a sec?" 
                        elif Girls:
                            ch_k "[Girls[0].Name], could I talk to [Player.Name] alone for a sec?" 
                        else:
                            return
                elif Character == EmmaX:                             
                        if len(Girls) > 1:
                            ch_e "Girls, would you mind if I had a word alone with [Player.Name]?"
                        elif Girls:
                            ch_e "[Girls[0].Name], would you mind if I had a word alone with [Player.Name]?"
                        else:
                            return
                elif Character == LauraX:                           
                        if len(Girls) > 1:
                            ch_l "Hey, clear out, I need to talk with [Player.Name]."
                        elif Girls:
                            ch_l "[Girls[0].Name], clear out, I need to talk with [Player.Name]."
                        else:
                            return
        #end portion asking about each girl
                           
        $ renpy.random.shuffle(Girls)
        while Girls:   
                if Girls[0] in Party:
                        $ Party.remove(Girls[0])  
                $ Girls[0].DrainWord("leaving",1,0,0)            
                $ Girls[0].DrainWord("arriving",1,0,0)
                
                if Silent:
                    pass
                elif not Passive and Character != "All":
                    #if there are other girls. . .
                    if Girls[0] == RogueX:
                            ch_r "No problem, I'll see you later then." 
                    elif Girls[0] == KittyX:
                            ch_k "[KittyX.Like]sure, I'll see you later."
                    elif Girls[0] == EmmaX:
                            ch_e "Fine, I'll see you later then."   
                    elif Girls[0] == LauraX:
                            ch_l "Ok. I'm leaving."  
                else:
                    if Girls[0] == RogueX:
                            ch_r "I should get going, see you later, [RogueX.Petname]." 
                    elif Girls[0] == KittyX:
                            ch_k "I think I'll head out, I'll see you later." 
                    elif Girls[0] == EmmaX:
                            ch_e "I think I should be going now."  
                    elif Girls[0] == LauraX: 
                            ch_l "I'm leaving."    
                            
                if bg_current == Girls[0].Home:
                        if Character != "All": #if it's not clearing all girls. . .
                                #if the girl is not Rogue but you're in Rogue's room, the girl takes you to her room
                                $ bg_current = Character.Home
                                $ Character.Loc = Character.Home
                                call Set_The_Scene
                                call CleartheRoom(Character)
                                call Taboo_Level
                                if not Silent:
                                    "[Character.Name] brings you back to her room. . ."
                                jump Misplaced
                                return
                        else:
                                $ Girls[0].Loc = "bg campus"
                else:
                        $ Girls[0].Loc = Girls[0].Home 
                        
                if Girls[0] == RogueX:
                        hide Rogue_Sprite with easeoutright 
                elif Girls[0] == KittyX:
                        hide Kitty_Sprite with easeoutbottom 
                elif Girls[0] == EmmaX:
                        hide Emma_Sprite with easeoutright 
                elif Girls[0] == LauraX: 
                        hide Laura_Sprite with easeoutright 
                $ Girls.remove(Girls[0])
                                   
        return 
            
# End Clear the Room / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
       

# Start Girls Location / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girls_Location(GirlsNum = 0, Change=0, BOptions=[]):
        #this figures out where girls are and where to put spares. 
        #it's called most often by Locations, after Waits
        #Girlsnum sets the number of girls that have already talked
        #"arriving" is set by the "Schedule" code, and will not be applied unless 
        # the girl in questions was someplace else, and just showed up here on their own.
        
        $ BOptions = TotalGirls[:]  
        $ renpy.random.shuffle(BOptions)
        while BOptions:        
                #cycles through each girl possible, adds them to the local area if possible
                if "leaving" in BOptions[0].RecentActions:
                        if "sleepover" in BOptions[0].Traits:
                                $ BOptions[0].DrainWord("sleepover",0,0,1)  #remove from Traits
                        call expression BOptions[0].Tag + "_Leave" #call Rogue_Leave
                        if BOptions[0].Loc != bg_current:                            
                                if BOptions[0] in Present:
                                        $ Present.remove(BOptions[0])
                                $ Change = 1
                        $ GirlsNum += 1     
                #if Girl was in Nearby, but was moved to a new location
                if BOptions[0] in Nearby and BOptions[0].Loc != "nearby": #and BOptions[0].Loc != bg_current 
                                $ Nearby.remove(BOptions[0])
                $ BOptions.remove(BOptions[0]) 
                
        if Change:
            #if there are any fewer girls than there were, Set the Scene
            call Set_The_Scene(Dress=0)    
            
        $ BOptions = TotalGirls[:]  
        while BOptions:  
                        if "arriving" in BOptions[0].RecentActions:
                                call Girls_Arrive
                                return
                        $ BOptions.remove(BOptions[0])                
        return
        
# End Girls Location / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Girls Arrive / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
label Girls_Arrive(Primary = 0, Secondary = 0, GirlsNum = 0,BO=[]):
        # Called by Girls_Location after a Wait period
        #"arriving" is set by the "Schedule" code, and will not be applied unless 
        # the girl in questions was someplace else, and just showed up here on their own.
        # Present contains all girls already local
        
        $ Options = []
        
        $ BO = TotalGirls[:]  
        while BO:  
                #Each girl trying to arrive is added to the Options
                if "arriving" in BO[0].RecentActions and BO[0] not in Party:                          
                        $ GirlsNum += 1                        
                        $ Options.append(BO[0])
                        $ BO[0].DrainWord("arriving")  
                $ BO.remove(BO[0])        
             
        $ renpy.random.shuffle(Options)
                
        if len(Options) <= 0 or (len(Party)+len(Present)) >= 2:                
                    #If nobody's here, or if the space is full, return
                    return    
        elif (len(Party)+len(Present)) <= 1:
                    #if the party is one or less and people are in the room
                    $ Primary = Options[0] 
                    if (len(Party)+len(Present)) == 0 and len(Options) >= 2:                    
                            #if the party is empty and 2+ people are in the room
                            $ Secondary = Options[1] 
                    
        if len(Options) > 2:
                #This triggers if there are more than two girls in the room. Primary and Secondary have been chosen and removed.            
                #If it's her room, she gets to be primary, otherwise she goes to her room            
                $ Options.remove(Primary)
                $ Options.remove(Secondary)
                while Options:
                        if bg_current == Options[0].Home:       #if you're in Options[0]'s room,
                            $ Secondary = Primary               #Make the Primary into the Secondary
                            $ Primary = Options[0]              #Make the Options[0] into the Primary
                        else:
                            $ Options[0] = Options[0].Home      #If you're anywhere else, move the girl to her home
                        if Options[0] == bg_current and Options[0] not in (Primary,Secondary) and Options[0] not in Party and Options[0] not in Present:
                                call Remove_Girl(Options[0],1,1)                        
                        $ Options.remove(Options[0])        
                #end list clearing
        if Secondary not in TotalGirls:
                $ Secondary = 0
        if Secondary and Secondary.Home == bg_current:
                #if it's the home of the owner
                $ Options.append(Primary)
                $ Secondary = Primary 
                $ Primary = Options[0]
        $ Options = []   
                
        if "locked" in Player.Traits:
                if Primary == KittyX:
                        call Locked_Door(KittyX)
                        if KittyX.Loc != bg_current:
                            $ Primary = 0
                        elif Secondary:
                            #since Kitty can just barg right in, if she does so, 
                            "You hear a \"thump\" as if someone was trying to follow Kitty."
                            call Locked_Door(Secondary)
                            if Secondary.Loc != bg_current:
                                    $ Secondary = 0                    
                elif Primary.Home == bg_current:
                        #if it's the girl's room. . .
                        "You hear a key jiggling in the lock."
                else:        
                        call Locked_Door(Primary)
                        if Primary.Loc != bg_current:
                            $ Primary = 0
        #End "if the door was locked." 
                        
        if not Primary:
                return 
                
        #This sequence sets the pecking order, more important once there are more girls
        #girls left out of this are put into "Nearby" for the current space
        
        call Shift_Focus(Primary)    
        if bg_current == "bg dangerroom":   
                    call Gym_Clothes("auto")
        call Set_The_Scene #causes the girls to display
        if bg_current == "bg player":
                    if Secondary:  
                            #if there's a second girl
                            "[Primary.Name] and [Secondary.Name] just entered your room."
                    else:
                            #if there's no second girl,
                            "[Primary.Name] just entered your room."
                            
                    if Primary == RogueX:
                                if Secondary:                        
                                    ch_r "Hey, [RogueX.Petname], can we come in?"
                                else:
                                    ch_r "Hey, [RogueX.Petname], can I come in?"
                    elif Primary == KittyX:
                                if Secondary:                        
                                    ch_k "Hey[KittyX.like]can we come in?"
                                else:
                                    ch_k "Hey[KittyX.like]can I come in?"
                    elif Primary == EmmaX:
                                if Secondary:                        
                                    ch_e "Ah, good, you're here. May we come in?"
                                else:
                                    ch_e "Ah, good, you're here. May I come in?"
                    elif Primary == LauraX:                      
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
                            $ Primary.Statup("Love", 80, 1)
                            $ Primary.Statup("Obed", 50, 2)
                            $ Primary.Statup("Inbt", 50, 2) 
                            if Primary == RogueX:
                                    ch_r "Thanks."
                            elif Primary == KittyX:
                                    $ KittyX.Statup("Inbt", 50, 1)
                                    ch_k "Cool."
                            elif Primary == EmmaX:
                                    ch_e "Good."
                            elif Primary == LauraX:
                                    $ LauraX.Statup("Love", 50, 1)
                                    $ LauraX.Statup("Obed", 60, 1)
                                    "She doesn't leave."
                            if Secondary:                                
                                    $ Secondary.Statup("Love", 80, 1)
                                    $ Secondary.Statup("Obed", 50, 2)
                                    $ Secondary.Statup("Inbt", 50, 2) 
                            #end "sure"
                    if Line == "later":  
                            $ Primary.Statup("Love", 60, -1, 1)
                            $ Primary.Statup("Obed", 70, 5) 
                            $ Primary.FaceChange("confused")
                            if Secondary:
                                    $ Secondary.Statup("Love", 60, -1, 1)
                                    $ Secondary.Statup("Obed", 70, 5) 
                                    $ Secondary.FaceChange("confused")
                                    if Primary == RogueX: 
                                            ch_r "Um, ok, we'll go then."
                                    elif Primary == KittyX:                                      
                                            $ KittyX.Statup("Love", 60, -1, 1)
                                            $ KittyX.Statup("Obed", 70, 2) 
                                            ch_k "Oh[KittyX.like]we'll get going then."
                                    elif Primary == EmmaX:
                                            $ EmmaX.Statup("Love", 90, -2)
                                            $ EmmaX.Statup("Obed", 30, -7) 
                                            ch_e "If that's how you wish to play it. . ."                       
                                    elif Primary == LauraX: 
                                            $ LauraX.Statup("Love", 90, -2)
                                            $ LauraX.Statup("Obed", 30, -7) 
                                            ch_l "Ok, later."
                                    call Remove_Girl(Secondary)
                            elif Primary == RogueX:
                                    ch_r "Um, ok."
                            elif Primary == KittyX:                      
                                    $ KittyX.Statup("Love", 60, -1, 1)
                                    $ KittyX.Statup("Obed", 70, 2) 
                                    ch_k "Oh[KittyX.like]I'll get going then."                                
                            elif Primary == EmmaX: 
                                    $ EmmaX.Statup("Love", 90, -2)
                                    $ EmmaX.Statup("Obed", 30, -7) 
                                    ch_e "If that's how you wish to play it. . ."                        
                            elif Primary == LauraX: 
                                    $ LauraX.Statup("Love", 90, -2)
                                    $ LauraX.Statup("Obed", 30, -7) 
                                    ch_l "Ok, later."             
                            call Remove_Girl(Primary)
                            #end "later"
                    if Line == "no":
                            $ Primary.Statup("Obed", 50, 5)  
                            if ApprovalCheck(Primary, 1800) or ApprovalCheck(Primary, 500, "O"):
                                $ Primary.Statup("Obed", 80, 2)                            
                                if Primary == RogueX:
                                        ch_r "I guess that's ok. See you later then."
                                elif Primary == KittyX:
                                        ch_k "If you want some alone time. . ."
                                elif Primary == EmmaX:
                                        $ EmmaX.Statup("Obed", 50, 2)  
                                        ch_e "I suppose you can have your personal space. . ."
                                elif Primary == LauraX:
                                        ch_l "Not a problem."
                            else:    
                                $ Primary.FaceChange("angry")
                                $ Primary.Statup("Love", 60, -5, 1)
                                $ Primary.Statup("Love", 80, -2)
                                $ Primary.Statup("Obed", 80, 3)
                                $ Primary.Statup("Inbt", 50, 1)
                                if Primary == RogueX:
                                        ch_r "Well fine!"
                                elif Primary == KittyX:                    
                                        $ KittyX.Statup("Love", 80, -2)
                                        $ KittyX.Statup("Obed", 80, 2)
                                        ch_k "Jerk!"
                                elif Primary == EmmaX:
                                        $ EmmaX.Statup("Love", 90, -2)
                                        $ EmmaX.Statup("Obed", 80, 3) 
                                        ch_e "We'll see how long that attitude lasts. . ."
                                elif Primary == LauraX:
                                        $ LauraX.Statup("Love", 90, -2)
                                        "She seems upset."
                            call Remove_Girl(Primary)                        
                            if Secondary:
                                    $ Secondary.Statup("Obed", 50, 5)  
                                    if ApprovalCheck(Secondary, 1800) or ApprovalCheck(Secondary, 500, "O"):
                                        $ Secondary.Statup("Obed", 80, 2)
                                        if Secondary == RogueX:
                                                ch_r "I guess that's ok. See you later then."
                                        elif Secondary == KittyX:
                                                ch_k "If you want some alone time. . ."
                                        elif Secondary == EmmaX:
                                                $ EmmaX.Statup("Obed", 50, 2)  
                                                ch_e "I suppose you can have your personal space. . ."
                                        elif Secondary == LauraX:
                                                ch_l "Not a problem."
                                    else:    
                                        $ Secondary.FaceChange("angry")
                                        $ Secondary.Statup("Love", 60, -5, 1)
                                        $ Secondary.Statup("Love", 80, -2)
                                        $ Secondary.Statup("Obed", 80, 3)
                                        $ Secondary.Statup("Inbt", 50, 1) 
                                        if Secondary == RogueX:
                                                ch_r "Well fine!"
                                        elif Secondary == KittyX:                    
                                                $ KittyX.Statup("Love", 80, -2)
                                                $ KittyX.Statup("Obed", 80, 2)
                                                ch_k "Jerk!"
                                        elif Secondary == EmmaX:
                                                $ EmmaX.Statup("Love", 90, -2)
                                                $ EmmaX.Statup("Obed", 80, 3) 
                                                ch_e "We'll see how long that attitude lasts. . ."
                                        elif Secondary == LauraX:
                                                $ LauraX.Statup("Love", 90, -2)
                                                "She seems upset."
                                    call Remove_Girl(Secondary)                        
                                    "The girls storm out."                                
                        #end "nope"
                    #end girls showed up to player's room.
        elif bg_current in PersonalRooms:       
                    #if you show up at one of the girls' rooms
                    if Secondary:  
                            #if there's a second girl
                            "[Primary.Name] and [Secondary.Name] just entered the room."
                    else:
                            #if there's no second girl,
                            "[Primary.Name] just entered the room."     
                    if bg_current == Primary.Home:
                                    if "angry" in Primary.DailyActions:
                                            #She's angry
                                            $ Primary.FaceChange("bemused", 1,Brows="angry") 
                                            if Primary == RogueX:                       
                                                            ch_r "I'm kinda pissed at you right now, get out of here." 
                                            elif Primary == KittyX:                       
                                                            ch_k "You shouldn't be here right now." 
                                            elif Primary == EmmaX:       
                                                            ch_e "I don't think you should be here." 
                                            elif Primary == LauraX:      
                                                            ch_l "You should get away while you can." 
                                    
                                    elif Current_Time == "Night" and ApprovalCheck(Primary, 1000, "LI") and ApprovalCheck(Primary, 600, "OI"):
                                            #it's night and she likes you
                                            if Primary == RogueX:                       
                                                            ch_r "Oh, hey, [RogueX.Petname], it's pretty late, but I guess you can stick around for a bit."  
                                            elif Primary == KittyX:                       
                                                            ch_k "Oh, hey, it's kinds late, but you can stay for a bit."  
                                            elif Primary == EmmaX:
                                                            ch_e "Oh, it's a bit late, but you're welcome."  
                                            elif Primary == LauraX:     
                                                            ch_l "It's late."  
                                            $ Line = "stay"                     
                                    elif ApprovalCheck(Primary, 1300) or ApprovalCheck(Primary, 500, "O"):
                                            #it's not night and she likes you
                                            if Primary == RogueX:                       
                                                            ch_r "Oh, hey, [RogueX.Petname], nice to see you here."
                                            elif Primary == KittyX:               
                                                            ch_k "Oh, hey, nice to see you."
                                            elif Primary == EmmaX:      
                                                            ch_e "Oh, nice to see you."
                                            elif Primary == LauraX:           
                                                            ch_l "Oh, hey."
                                            $ Line = "stay"
                                    elif Current_Time == "Night":
                                            #it's night and she wants you gone
                                            if Primary == RogueX:                       
                                                            ch_r "Oh, hey, [RogueX.Petname], it's kind late, could you head out of here?" 
                                            elif Primary == KittyX:     
                                                            ch_k "Oh, hey, [KittyX.Petname]. It's kind of late, could you come back tomorrow?" 
                                            elif Primary == EmmaX:    
                                                            ch_e "Oh, hello, [EmmaX.Petname]. It's a bit late, could you come back tomorrow?" 
                                            elif Primary == LauraX:          
                                                            ch_l "Oh, hey, it's late." 
                                    elif ApprovalCheck(Primary, 600, "LI") or ApprovalCheck(Primary, 300, "OI"):
                                            #it's not night and she wants you gone
                                            if Primary == RogueX:                       
                                                            ch_r "Oh, hey, [RogueX.Petname]. You can stick around, I guess."
                                            elif Primary == KittyX:             
                                                            ch_k "Oh, hey, [KittyX.Petname], what's up?"
                                            elif Primary == EmmaX:     
                                                            ch_e "Oh, hello, [EmmaX.Petname], can I help you with anything?"
                                            elif Primary == LauraX:  
                                                            ch_l "Oh, hey, [LauraX.Petname]."
                                            $ Line = "stay"
                                    else: 
                                            #she's fine with you around
                                            if Primary == RogueX:                       
                                                            ch_r "Hey, [RogueX.Petname], I'm not sure why you're here, but I'd rather you leave."  
                                            elif Primary == KittyX:    
                                                            ch_k "Hey, [KittyX.Petname], what are you even doing here?"
                                                            ch_k "Could you[KittyX.like]get out?"  
                                            elif Primary == EmmaX:  
                                                            ch_e "Oh, hello, [EmmaX.Petname]?"
                                                            ch_e "Did you have a reason to be visiting me?"  
                                            elif Primary == LauraX:    
                                                            $ Primary.FaceChange("confused") 
                                                            ch_l "Hey, [LauraX.Petname], why are you here?"
                                    if Line != "stay":
                                        #if she asked you to leave. . .
                                        menu:
                                            extend ""
                                            "Sure, ok. [[you go]":
                                                        $ Primary.Statup("Love", 80, 1)
                                                        $ Primary.Statup("Obed", 50, 2)
                                                        $ Primary.Statup("Inbt", 50, 2)  
                                                        call AnyLine(Primary,"Thanks.")
                                                        "You head back to your room."
                                            "Sorry, I'll go.":
                                                        $ Primary.Statup("Love", 90, 2)
                                                        $ Primary.Statup("Obed", 50, 3) 
                                                        $ Primary.FaceChange("smile") 
                                                        call AnyLine(Primary,"Thanks.")
                                                        "You head back to your room."
                                            "Are you sure I can't stay?":
                                                        if "angry" in Primary.DailyActions:
                                                                $ Primary.FaceChange("angry")                                                                    
                                                                if Primary == RogueX:                       
                                                                                ch_r "What part of \"no\" don't ya get?" 
                                                                elif Primary == KittyX:   
                                                                                ch_k "I think I said {i}NO!{/i}"   
                                                                elif Primary == EmmaX:    
                                                                                ch_e "I believe I said {i}no.{/i}"   
                                                                elif Primary == LauraX:    
                                                                                ch_l "[[growls] . . .You probably shouldn't."              
                                                        elif Current_Time == "Night" and ApprovalCheck(Primary, 800, "LI") and ApprovalCheck(Primary, 400, "OI"):                                                            
                                                                $ Primary.FaceChange("sadside") 
                                                                if Primary == RogueX:                       
                                                                                ch_r "I suppose I can make an exception this once." 
                                                                elif Primary == KittyX:   
                                                                                ch_k "Maybe just this once. . ." 
                                                                elif Primary == EmmaX:         
                                                                                ch_e "Perhaps just this once. . ." 
                                                                elif Primary == LauraX:   
                                                                                ch_l "I guess. . ."             
                                                                $ Line = "stay"
                                                        elif Current_Time == "Night":                                                                  
                                                                if Primary == RogueX:                       
                                                                                ch_r "No way, [RogueX.Petname]. Try again tomorrow." 
                                                                elif Primary == KittyX:              
                                                                                ch_k "Noooope. Try again tomorrow."    
                                                                elif Primary == EmmaX:       
                                                                                ch_e "I'm afraid not. Try again tomorrow."   
                                                                elif Primary == LauraX:   
                                                                                ch_l "No. Maybe tomorrow."                                                            
                                                        elif ApprovalCheck(Primary, 750):
                                                                if Primary == RogueX:                       
                                                                                ch_r "Oh, fine. For a little bit." 
                                                                elif Primary == KittyX:    
                                                                                ch_k "Oh, fiiiine."
                                                                                ch_k "Just for a little bit."
                                                                elif Primary == EmmaX:       
                                                                                ch_e "Oh, very well. . ."
                                                                                ch_e "Just for a little bit."
                                                                elif Primary == LauraX:          
                                                                                ch_l "Ok."
                                                                                ch_l "Just for a minute."     
                                                                $ Line = "stay"
                                                        else: 
                                                                $ Primary.FaceChange("angry")                                                                   
                                                                if Primary == RogueX:                       
                                                                                ch_r "No, seriously, get."   
                                                                elif Primary == KittyX:     
                                                                                ch_k "Noooope." 
                                                                elif Primary == EmmaX:      
                                                                                ch_e "Definitely not."   
                                                                elif Primary == LauraX:       
                                                                                ch_l "No."           
                                                        if Line != "stay": 
                                                                $ Primary.Statup("Love", 80, -1)
                                                                $ Primary.Statup("Inbt", 50, 3) 
                                                                "[Primary.Name] kicks you out of the room."  
                                                                
                                            "I'm sticking around, thanks.":   
                                                        if "angry" in Primary.DailyActions or (not ApprovalCheck(Primary, 1800) and not ApprovalCheck(Primary, 500, "O")):
                                                                $ Primary.FaceChange("angry")   
                                                                if Primary == RogueX:             
                                                                                ch_r "No way, buster! Out!"
                                                                elif Primary == KittyX:    
                                                                                ch_k "Nooope, out!"
                                                                elif Primary == EmmaX:      
                                                                                ch_e "You must be joking."
                                                                elif Primary == LauraX:                 
                                                                                ch_l "You really shouldn't."
                                                        else:
                                                                $ Primary.Statup("Obed", 80, 5)
                                                                $ Primary.FaceChange("sad")   
                                                                if Primary == RogueX:             
                                                                                ch_r ". . ." 
                                                                                ch_r "I guess that's ok."
                                                                elif Primary == KittyX:  
                                                                                ch_k ". . ." 
                                                                                ch_k "Fine."
                                                                elif Primary == EmmaX:    
                                                                                ch_e ". . ." 
                                                                                ch_e "Fine."
                                                                elif Primary == LauraX:  
                                                                                ch_l ". . ."      
                                                                $ Line = "stay"
                                                        if Line != "stay":
                                                                $ Primary.Statup("Love", 60, -5, 1)
                                                                $ Primary.Statup("Love", 80, -5)
                                                                $ Primary.Statup("Obed", 50, 2)
                                                                $ Primary.Statup("Inbt", 60, 5) 
                                                                "[Primary.Name] kicks you out of the room."
                                                                                                                                  
                                    if Line != "stay":
                                            $ bg_current = "bg player"  
                                            jump Misplaced
                                    #End the girl tells you to leave. 
                    elif Primary == RogueX:                       
                                    ch_r "Sorry, I wasn't expecting to bump into you here."
                    elif Primary == KittyX:                       
                                    ch_k "Hey[KittyX.like]funny meeting you here."
                    elif Primary == EmmaX:                       
                                    ch_e "I didn't expect to run into you here."
                    elif Primary == LauraX:                       
                                    ch_l "Oh, hey."
        #end girls showed up to Primary's room.  
                  
        elif bg_current == "bg classroom": 
                #if this is triggered, Adjacent should never be higher than 1. 
                #adjacent characters who are neither Primary nor secondary should have been removed from adjacency

                if Secondary:  
                        #if there's a second girl
                        "[Primary.Name] and [Secondary.Name] just entered the room."
                else:
                        #if there's no second girl,
                        "[Primary.Name] just entered the room."       
                        
                if Primary == RogueX or Secondary == RogueX:
                                ch_r "Hey, [RogueX.Petname]."
                if Primary == KittyX or Secondary == KittyX:
                                ch_k "Oh, hey."
                if Primary == EmmaX or Secondary == EmmaX:
                                ch_e "Oh, hello, [EmmaX.Petname]."
                if Primary == LauraX or Secondary == LauraX:
                                ch_l "Hey."    
                                
                $ Line = 0
                $ D20 = renpy.random.randint(1, 20)
                         
                if Primary and Primary != EmmaX:                
                        #Determines who sits next to you
                        if ApprovalCheck(Primary, 1000): 
                                if len(Present) < 2 and D20 >= 10:
                                        $ Line = Primary.Name + " takes the seat next to you"
                                        $ Present.append(Primary)
                                else:
                                        $ Line = Primary.Name + " sits across the room from you"
                                        $ Nearby.append(Primary)
                        else:
                                        $ Line = Primary.Name + " sits across the room from you"
                                        $ Nearby.append(Primary)
                if Secondary == EmmaX and len(Present) < 2 and D20 >= 10:
                                        $ Line = Line + ", while " + EmmaX.Name + " walks up next to you"
                elif Secondary and Secondary != EmmaX:                
                        #Determines who sits next to you
                        if Primary == EmmaX:
                                        $ Line = "[EmmaX.Name] walks over and stands near you"
                        if ApprovalCheck(Secondary, 1000): 
                            if len(Present) < 2 and D20 >= 10:
                                        #changes dialog based on whether she does the same or differently than the last person
                                        if Primary in Present and Primary != EmmaX:
                                                $ Line = Primary.Name + " and " + Secondary.Name + " sit down next to you"
                                        else:
                                                $ Line = Line + ", while " + Secondary.Name + " takes the seat next to you"
                                        $ Present.append(Secondary)
                            else:
                                        if Primary in Nearby and Primary != EmmaX:
                                                $ Line = Primary.Name + " and " + Secondary.Name + " sit across the room from you"
                                        else:
                                                $ Line = Line + ", while " + Secondary.Name + " sits across the room from you"
                                        $ Nearby.append(Secondary)
                        else:
                                        if Primary in Nearby and Primary != EmmaX:
                                                $ Line = Primary.Name + " and " + Secondary.Name + " sit across the room from you"
                                        else:
                                                $ Line = Line + ", while " + Secondary.Name + " sits across the room from you"
                                        $ Nearby.append(Secondary)
                if Line:
                    "[Line]."
                                    
                if EmmaX.Loc == "bg teacher":
                        "[EmmaX.Name] takes her position behind the podium."                    
                #end girls showed up to class
        elif bg_current == "bg dangerroom":   
                if Secondary:  
                        #if there's a second girl
                        "[Primary.Name] and [Secondary.Name] just entered the room."
                else:
                        #if there's no second girl,
                        "[Primary.Name] just entered the room."   
                #end girls showed up to the Danger Room
        elif bg_current == "bg campus":   
                if Secondary:  
                        #if there's a second girl
                        "[Primary.Name] and [Secondary.Name] just entered the square."
                else:
                        #if there's no second girl,
                        "[Primary.Name] just entered the square."   
                #end girls showed up to the campus
        else: #if it's anywhere else,   
                if Secondary:  
                        #if there's a second girl
                        "[Primary.Name] and [Secondary.Name] just entered the room."
                else:
                        #if there's no second girl,
                        "[Primary.Name] just entered the room."  
                #end girls showed up someplace
                                    
        if bg_current in ("bg campus","bg dangerroom"):
            if Primary == RogueX or Secondary == RogueX:
                            ch_r "Hey, [RogueX.Petname]."
            if Primary == KittyX or Secondary == KittyX:
                            ch_k "Oh, hey."
            if Primary == EmmaX or Secondary == EmmaX:
                            ch_e "Oh, hello, [EmmaX.Petname]."
            if Primary == LauraX or Secondary == LauraX:
                            ch_l "Hey."                          
        #end "girls showed up"    
                
        $ BO = TotalGirls[:]  
        while BO:   
                if BO[0] in Nearby:
                        $ BO[0].Loc = "nearby"
                elif BO[0].Loc == bg_current:
                        $ Present.append(BO[0])  
                $ BO.remove(BO[0])
        if Nearby:
                "There were some others as well, but they kept their distance." 
        return
# End Girls Arrive / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Gym Clothes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label Gym_Clothes(Mode = 0, Girl = [], GirlsNum = 0, BO=[]): #checked each time you enter the Gym
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
        if Girl:
                $ BO = Girl[:]                
        else:
                $ BO = TotalGirls[:]          
        while BO: #or Mode == "exit"?
                #while there are still girls to do or the Mode is exit. . .
                if BO[0].Loc != "bg dangerroom" or Mode == "change" or "leaving" in BO[0].RecentActions:  
                        #If the girl has left the gym or was told to change back
                        if Mode == "exit" and "leaving" not in BO[0].RecentActions:
                                #this means she will only change into street clothes if leaving
                                #during the "exit" phase.
                                pass
                        elif BO[0].Outfit == "gym":
                            if bg_current == "bg dangerroom" and "leaving" in BO[0].RecentActions:
                                #if you're in the danger room, and so is this girl
                                $ BO[0].Outfit = BO[0].OutfitDay
                elif BO[0].Outfit == "gym":
                                #If she's already in gym clothes, skip this
                                pass
                elif Mode == "pre":
                        #If she was already here
                        if BO[0].Loc == "bg dangerroom" and BO[0] not in Party:
                                $ BO[0].Outfit = "gym"
                elif Mode == "auto":
                        #If it's set to do it automatically by the call
                        if BO[0].Loc == "bg dangerroom" and BO[0].Loc == bg_current:
                                show blackscreen onlayer black
                        $ BO[0].Outfit = "gym"                        
                elif BO[0].Loc == bg_current:
                        #If girl is in the gym, see if she'll change clothes
                        if ApprovalCheck(BO[0], 1300, "LO") or "passive" in BO[0].Traits:
                            pass
                        elif ApprovalCheck(BO[0], 800, "LO") and BO[0].Custom1[0]:
                            pass
                        elif ApprovalCheck(BO[0], 600, "LO") and BO[0].Gym[0] != 1:
                            pass
                        else:
                            $ Line = "no"
                        
                        if Line == "no" or "asked gym" in BO[0].DailyActions or "no ask gym" in BO[0].Traits:   
                                #If she decides not to ask you   
                                show blackscreen onlayer black 
                                if BO[0] == EmmaX:
                                        ch_e "I should change too."  
                                elif BO[0] == LauraX:
                                        ch_l "I'll be right back. . ."   
                                else:
                                    if GirlsNum:
                                            call AnyLine(BO[0],"I'll be right back too.")
                                    else: 
                                            call AnyLine(BO[0],"I'll be back soon, gotta change.")  
                                $ BO[0].Outfit = "gym"
                        else:
                                # She asks to change outfits
                                $ BO[0].DailyActions.append("asked gym")
                                if GirlsNum:
                                    if BO[0] == EmmaX:
                                            $ Line = "Do you think I should change as well?"
                                    elif BO[0] == LauraX:
                                            $ Line = "Did you want me to change into my gym clothes?"   
                                    else: 
                                            $ Line = "Should I change too?"  
                                else:
                                    if BO[0] == EmmaX:
                                            $ Line = "Did you want me to change into my gear?"   
                                    elif BO[0] == LauraX:
                                            $ Line = "Did you want me to change into my gym clothes?" 
                                    else: 
                                            $ Line = "Would you like me to change into my gym clothes?"  
                                call AnyLine(BO[0],Line)
                                menu:
                                        extend ""
                                        "Yeah, they look great.":  
                                                    $ BO[0].FaceChange("smile")    
                                                    $ BO[0].Statup("Love", 80, 2)
                                                    $ BO[0].Statup("Obed", 40, 1)
                                                    $ BO[0].Statup("Inbt", 30, 1)
                                                    $ Line = 1                            
                                        "No, stay in that.":
                                                    $ BO[0].FaceChange("confused")     
                                                    $ BO[0].Statup("Obed", 50, 5)
                                                    $ Line = 0
                                        "Whichever you like.": 
                                                    $ BO[0].FaceChange("confused")                                       
                                                    $ BO[0].Statup("Inbt", 50, 1)
                                                    $ Line = renpy.random.randint(0, 3)
                                        "I don't care.":        
                                                    $ BO[0].FaceChange("angry")      
                                                    $ BO[0].Statup("Love", 50, -3, 1)
                                                    $ BO[0].Statup("Obed", 50, 4)
                                                    $ BO[0].Statup("Inbt", 50, 2)  
                                                    $ Line = renpy.random.randint(0, 1)
                                if Line:
                                        #If she decided to change   
                                        if BO[0] == RogueX:
                                                ch_r "Ok, be right back."  
                                        elif BO[0] == KittyX:
                                                ch_k "Ok, back in a bit" 
                                        elif BO[0] == EmmaX:
                                                ch_e "Fine, I'll be right back."   
                                        elif BO[0] == LauraX:
                                                ch_l "I'll be right back then." 
                                        $ BO[0].Outfit = "gym"
                            #end asked
                        if BO[0].Outfit == "gym":
                            $ GirlsNum += 1 
                        $ Line = 0
                # End girl loop   
                $ BO.remove(BO[0])
                
        if Girl:
                $ BO = Girl[:]
        else:
                $ BO = TotalGirls[:]                
        while BO:
                #loops through and makes choices.                
#                if bg_current == "bg dangerroom" and BO[0].Loc == bg_current:
#                        #if you're in the danger room, and so is this girl
#                        show blackscreen onlayer black                        
#                        if BO[0] == RogueX:
#                                ch_r "Ok, be right back."  
#                        elif BO[0] == KittyX:
#                                ch_k "Ok, back in a bit" 
#                        elif BO[0] == EmmaX:
#                                ch_e "Fine, I'll be right back."   
#                        elif BO[0] == LauraX:
#                                ch_l "I'll be right back then." 
                $ BO[0].OutfitChange()
                $ BO.remove(BO[0])
        hide blackscreen onlayer black
                        
        return
# End Gym clothes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /        

# Start Present Check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label Present_Check(Hold=1,BO=[]):
        # Culls parties down to 2 max
        # call Present_Check(1) will _return positive if the room is filled with the current inhabitants
        # call Present Check will cull inhabitants of the room down to zero
        
        $ Present = []
        
        while len(Party) > 2:    
                # If two or more members in the party    
                #Culls down party size to two
                $ Party.remove(Party[2])   
        
        # checks to see which girls are present at a given location
        # If they are in the party, makes sure they are in the room
        # adds members who are not currently in the party            
        $ BO = TotalGirls[:]  
        while BO:        
                #cycles through each girl possible, adds them to the local area if possible
                if BO[0] in Party: 
                                $ BO[0].Loc = bg_current
                elif BO[0].Loc == bg_current:       
                                $ Present.append(BO[0])  
                $ BO.remove(BO[0])
            
        $ renpy.random.shuffle(Present) #Randomizes pool
             
        if len(Party) == 2:
                #adds the second party member if to Present it exists
                if Party[1] in TotalGirls:
                        $ Present.append(Party[1]) 
                else:
                        $ Party.remove(Party[1])
        if len(Party) >= 1:
                #adds the first party member to Present if it exists
                if Party[0] in TotalGirls:
                        $ Present.append(Party[0]) 
                else:
                        $ Party.remove(Party[0])
        
        while len(Present) > 2:
                #culls the Present list down to two items (or less if the party is full)
                #Removes the rest
                call Remove_Girl(Present[0],Hold=Hold) #Moves girls to Nearby if that's an option. 
                $ Present.remove(Present[0]) 
                           
        if Present and Ch_Focus not in Present:
                $ renpy.random.shuffle(Present) 
                call Shift_Focus(Present[0]) 
                               
        $ BO = Present[:]  
        while BO:        
                #cycles through each girl possible, removes them from NEarby if they were there.
                if BO[0] in Nearby:
                                $ Nearby.remove(BO[0])  
                if BO[0].Loc == "nearby":
                                $ BO[0].Loc = bg_current 
                $ BO.remove(BO[0])
                
        return
    
# End Present Check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 

# Start Swap Nearby Girls / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 

label Swap_Nearby(Girl=0):
        #allows you to bring nearby girls in. 
        # girl is the girl in question, here is a counter for locals
        if Girl not in Nearby:        
            return
        if bg_current not in ("bg campus","bg classroom","bg dangerroom"):
            #if you aren't in a space that supports this. . .
            "There's no room for that here."
            return
                    
        if len(Present) >= 2:
            #if two or more girls are adjacent so there is no room. . .
            call AnyLine(Girl,"It's a little crowded over there.")
            menu:
                "Move away from an adjacent girl?"
                "[RogueX.Name]" if RogueX.Loc == bg_current:
                        "You shift away from [RogueX.Name]"
                        call Remove_Girl(RogueX,1,1)    #Hide+moveto nearby
                "[KittyX.Name]" if KittyX.Loc == bg_current:
                        "You shift away from [KittyX.Name]"
                        call Remove_Girl(KittyX,1,1)    #Hide+moveto nearby
                "[EmmaX.Name]" if EmmaX.Loc == bg_current:
                        "You shift away from [EmmaX.Name]"
                        call Remove_Girl(EmmaX,1,1)     #Hide+moveto nearby
                "[LauraX.Name]" if LauraX.Loc == bg_current:
                        "You shift away from [LauraX.Name]"
                        call Remove_Girl(LauraX,1,1)    #Hide+moveto nearby        
                "No, never mind.":
                    return
        "[Girl.Name] comes over and joins you."
#        if bg_current == "bg classroom":
#                $ Adjacent.append(Girl)
        $ Nearby.remove(Girl)   
        $ Present.append(Girl) 
        call Shift_Focus(Girl)
        $ Girl.Loc = bg_current
        call Set_The_Scene(1,0,0,0)
        return
#end Swap_Nearby / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 


# Start Dismiss girl / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label Dismissed: 
        # this is called to dismiss any girl in the local area.
        menu:
            "Did you want to ask someone to leave?"
            "[RogueX.Name]" if RogueX.Loc == bg_current or RogueX in Party:
                call Girl_Dismissed(RogueX)
            "[KittyX.Name]" if KittyX.Loc == bg_current or KittyX in Party:
                call Girl_Dismissed(KittyX)
            "[EmmaX.Name]" if EmmaX.Loc == bg_current or EmmaX in Party:
                call Girl_Dismissed(EmmaX)
            "[LauraX.Name]" if LauraX.Loc == bg_current or LauraX in Party:
                call Girl_Dismissed(LauraX)
            "Nevermind.":
                pass
        return

# End Dismiss Girl / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 


label Locked_Door(Girl=0,Entry=0):
        # called when a girl tries to enter a locked room, mainly from the summon function
        # Girl is the indicated girl, Entry is True if you want to always have her enter with dialog
        if Girl not in TotalGirls:
                return  
        if not Trigger:
                #resets the scene if not during a sex act
                call Set_The_Scene
        if Girl == KittyX:
                "You look to the door just as [KittyX.Name] phases into the room."
                $ KittyX.Loc = bg_current 
                call Taboo_Level
                $ KittyX.OutfitChange()
                call Display_Girl(KittyX,TrigReset=0)
                ch_k "Hi, [KittyX.Petname]!"
                return 1        
        if "locked" not in Player.Traits:
                if Entry:                  
                        call Display_Girl(Girl)  
                        if Girl == RogueX:
                                ch_r "Hey, got a minute, [Girl.Petname]?"
                        elif Girl == EmmaX:
                                ch_e "[Girl.Petname], I had something I wanted to discuss. . ."
                        elif Girl == LauraX:
                                ch_l "Hey, [Girl.Petname]."
                return 1
        if Girl.Loc == Girl.Home:
            "You hear a key in the lock, and [Girl.Name] enters the room." 
        else:    
            "The doorknob jiggles. A moment later, you hear a knock."
            if Girl == RogueX:
                    ch_r "Could I come in, [RogueX.Petname]?"
            elif Girl == EmmaX:
                    ch_e "[EmmaX.Petname], I'm waiting."
            elif Girl == LauraX:
                    ch_l "It's me."
            menu:
                extend ""
                "Open door":
                        ch_p "Hold on, [Girl.Name]!" 
                        "You unlock the door and let her in."
                        $ Girl.Loc = bg_current 
                        $ Girl.OutfitChange()
                "Open door [[but stop fucking first]" if Trigger:
                        ch_p "Hold on, [Girl.Name]!" 
                        call Sex_Over(1,Primary) #Cleans up after the sex stuff
                        "You unlock the door and let her in."
                        $ Girl.Loc = bg_current 
                        $ Girl.OutfitChange()
                        call Display_Girl(Girl,TrigReset=0)  
                        if Girl == RogueX:
                                ch_r "Hey, got a minute, [Girl.Petname]?"
                        elif Girl == EmmaX:
                                ch_e "[Girl.Petname], I had something I wanted to discuss. . ."
                        elif Girl == LauraX:
                                ch_l "Hey, [Girl.Petname]."
                        jump Misplaced
                "Send her away":
                        ch_p "Er, sorry, could you come back later?"
                        $ Girl.Statup("Love", 80, -2)
                        if Girl == RogueX:
                                ch_r "C'mon, [Girl.Petname], don't yank my chain like this!"
                                if Girl.Loc == bg_current:
                                    call Remove_Girl(Girl)
                                return 0
                        elif Girl == EmmaX:  
                                $ Girl.Statup("Obed", 80, -2)
                                ch_e "I have to say, [EmmaX.Petname], I understand the appeal of having someone at your beck and call. . ."
                                ch_e "but I don't appreciate being on the receiving end!"
                                if Girl.Loc == bg_current:
                                    call Remove_Girl(Girl)
                                return 0
                        elif Girl == LauraX:
                            "[Girl.Name] goes quiet."
                            if ApprovalCheck(LauraX, 500,"I") and not ApprovalCheck(LauraX, 500,"O"):
                                    $ Girl.Loc = bg_current 
                                    $ LauraX.OutfitChange()
                                    $ LauraX.ArmPose = 2
                                    $ LauraX.Claws = 1
                                    "snickt"
                                    call Display_Girl(LauraX,TrigReset=0)
                                    "The door swings open."
                                    $ Girl.Statup("Obed", 80, -4)
                                    $ LauraX.Claws = 0
                                    ch_l "Hey, so I don't like being jerked around, so don't do that, okay?"
                            else:
                                    $ Girl.Statup("Love", 80, -1)
                                    $ Girl.Statup("Obed", 80, 3)
                                    ch_l "Ok."
                                    "You hear her shuffling off."
                                    if Girl.Loc == bg_current:
                                        call Remove_Girl(Girl)
                                    return 0
        call Taboo_Level
        $ Player.DrainWord("locked",0,0,1)
        call Set_The_Scene(1,0,0,0)#characters, no entry, no clothes changes, no triggers
        return 1
#End Locked door responses / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Taboo stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Taboo_Level(Taboo_Loc=1,Teach=0,BO=[]):
        #cycles through each girl, setting their taboo level.
        # if Taboo_Loc, will only work on local characters.
        #Set your taboo level
        
        if EmmaX.Loc == "bg teacher":
                $ EmmaX.Loc = "bg classroom" #Sets Emma to being in class if she's teaching
                $ Teach = 1
                        
        call CheckTaboo(Player,bg_current)      
        
        $ BO = TotalGirls[:]  
        while BO:        
                #cycles through each girl possible, setting them to local if they are in the party
                #Then it checks their taboo level
                if BO[0] in Party:
                        $ BO[0].Loc = bg_current
                if BO[0].Loc == "nearby":
                        $ Taboo_Check = bg_current
                else:
                        $ Taboo_Check = BO[0].Loc                
                if not Taboo_Loc or Taboo_Check == bg_current:
                        #only checks if they are local if it's not a general check
                        call CheckTaboo(BO[0],Taboo_Check)   
                $ BO.remove(BO[0])
        if Teach:
                $ EmmaX.Loc = "bg teacher" #Sets Emma to being a teacher again   
        return
        #end taboo level

label CheckTaboo(Girl=0,Taboo_Check=0,Girl2=[]):
        #Girl is the girl being tested
        # Taboo_Check is the location she is at
                      
        if Taboo_Check in PersonalRooms or Taboo_Check == "hold": 
                            $ Girl.Taboo = 0
        elif Taboo_Check in ("bg classroom", "bg study"):
                if Current_Time == "Night":
                            $ Girl.Taboo = 5
                elif Current_Time == "Evening" or Weekday >= 5:
                    if "locked" in Player.Traits and Taboo_Check == bg_current:
                            $ Girl.Taboo = 0
                    else:
                            $ Girl.Taboo = 30
                else:
                            $ Girl.Taboo = 40
        elif Taboo_Check == "bg dangerroom":
                if Current_Time == "Night":
                    if "locked" in Player.Traits and Taboo_Check == bg_current:
                            $ Girl.Taboo = 0
                    else:
                            $ Girl.Taboo = 5
                else:
                            $ Girl.Taboo = 40
        elif Taboo_Check == "bg campus" or Taboo_Check == "bg pool":
                if Current_Time == "Night":
                            $ Girl.Taboo = 20
                else:
                            $ Girl.Taboo = 40
        elif Taboo_Check == "bg showerroom":   
                            $ Girl.Taboo = 20
        else:
                            $ Girl.Taboo = 40
        if Girl == Player:
                # if it's already 20+, or if we're testing the player stat, there's no point to this      
                $ Taboo = Girl.Taboo
                return                
        if Girl.Taboo >= 20:
                # if it's already 20+, or if we're testing the player stat, there's no point to this                
                return
                
        $ Girl2 = TotalGirls[:]
        while Girl2:
                #compares the first girl to each of the others. 
                if Girl2[0] != Girl:
                        #loops through the girls in an inner loop if they are not the same 
                        if Girl.Loc == Girl2[0].Loc and Girl.GirlLikeCheck(Girl2[0]) <= 700 and not (Girl in Player.Harem and Girl2[0] in Player.Harem):
                                #if either she likes the second girl, or both are in the harem, skip                                
                                $ Girl.Taboo = 20
                $ Girl2.remove(Girl2[0])
                
        $ Taboo = Girl.Taboo if (Girl.Taboo > Taboo and bg_current == Girl.Loc) else Taboo
        
        return
            
#End Taboo stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

        
# End Time and Space Stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /       

label Speed_Shift(S=0):   
        #adjusts the speed of animations to S, uses fade to hide glitches
        # call Speed_Shift(2)
        $ Speed = S
        show blackscreen onlayer black 
        pause 0.01 
        hide blackscreen onlayer black 
        return
    
                

# Start shop interface / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Shop:
    menu:
        "You are logged into the store. You have [Player.Cash] dollars."       
        "Buy dildo for $20.":
                if Player.Inventory.count("dildo") >= 10:
                    "You already have way more dildos than you need. 2, 4, 6. . . yes, way too many."
                elif Player.Cash >= 20:                
                    "You purchase one dildo."
                    $ Player.Inventory.append("dildo")
                    $ Player.Cash -= 20
                else:
                    "You don't have enough for that."
        "Buy \"Shocker\" vibrator for $25.":
                if Player.Inventory.count("vibrator") >= 10:
                    "If you bought one more vibrator, you would risk a geological event."
                elif Player.Cash >= 25:
                    "You purchase one vibrator."
                    $ Player.Inventory.append("vibrator")
                    $ Player.Cash -= 25
                else:
                    "You don't have enough for that."   
        "Gifts for [RogueX.Name]":
            menu:
                "Buy green lace nighty for $75." if "nighty" not in RogueX.Inventory and "Rogue nighty" not in Player.Inventory:            
                    if Player.Cash >= 75:
                        "You purchase the nighty, this will look nice on [RogueX.Name]."
                        $ Player.Inventory.append("Rogue nighty")
                        $ Player.Cash -= 75
                    else:
                        "You don't have enough for that."    
                "Buy black lace bra for $90." if "lace bra" not in RogueX.Inventory and "Rogue lace bra" not in Player.Inventory:            
                    if Player.Cash >= 90:
                        "You purchase the lace bra, this will look nice on [RogueX.Name]."
                        $ Player.Inventory.append("Rogue lace bra")
                        $ Player.Cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy black lace panties for $110." if "lace panties" not in RogueX.Inventory and "Rogue lace panties" not in Player.Inventory:            
                    if Player.Cash >= 110:
                        "You purchase the lace panties, these will look nice on [RogueX.Name]."
                        $ Player.Inventory.append("Rogue lace panties")
                        $ Player.Cash -= 110
                    else:
                        "You don't have enough for that."  
                "Buy stockings and garterbelt for $100." if "stockings and garterbelt" not in RogueX.Inventory and "stockings and garterbelt" not in Player.Inventory and ApprovalCheck(RogueX, 1500):          
                    if Player.Cash >= 100:
                        "You purchase the stockings, these will look nice on [RogueX.Name]."             
                        $ Player.Inventory.append("stockings and garterbelt")
                        $ Player.Cash -= 100
                    else:
                        "You don't have enough for that."   
                "Buy yellow bikini top for $50." if "bikini top" not in RogueX.Inventory and "Rogue bikini top" not in Player.Inventory:            
                        if Player.Cash >= 50:
                            "You purchase the bikini top, this will look nice on [RogueX.Name]."
                            $ Player.Inventory.append("Rogue bikini top")
                            $ Player.Cash -= 50
                        else:
                            "You don't have enough for that."
                "Buy green bikini bottoms for $50." if "bikini bottoms" not in RogueX.Inventory and "Rogue bikini bottoms" not in Player.Inventory:            
                        if Player.Cash >= 50:
                            "You purchase the bikini bottoms, these will look nice on [RogueX.Name]."
                            $ Player.Inventory.append("Rogue bikini bottoms")
                            $ Player.Cash -= 50
                        else:
                            "You don't have enough for that."  
                "Never mind.":
                    pass
        "Gifts for [KittyX.Name]" if "met" in KittyX.History:
            menu:  
                "Buy white lace bra for $90." if "lace bra" not in KittyX.Inventory and "Kitty lace bra" not in Player.Inventory:            
                    if Player.Cash >= 90:
                        "You purchase the lace bra, this will look nice on [KittyX.Name]."
                        $ Player.Inventory.append("Kitty lace bra")
                        $ Player.Cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy white lace panties for $110." if "lace panties" not in KittyX.Inventory and "Kitty lace panties" not in Player.Inventory:            
                    if Player.Cash >= 110:
                        "You purchase the lace panties, these will look nice on [KittyX.Name]."
                        $ Player.Inventory.append("Kitty lace panties")
                        $ Player.Cash -= 110
                    else:
                        "You don't have enough for that."  
                "Buy blue cat bikini top for $60." if "bikini top" not in KittyX.Inventory and "Kitty bikini top" not in Player.Inventory:            
                        if Player.Cash >= 60:
                            "You purchase the bikini top, this will look nice on [KittyX.Name]."
                            $ Player.Inventory.append("Kitty bikini top")
                            $ Player.Cash -= 60
                        else:
                            "You don't have enough for that."
                "Buy blue bikini bottoms for $60." if "bikini bottoms" not in KittyX.Inventory and "Kitty bikini bottoms" not in Player.Inventory:            
                        if Player.Cash >= 60:
                            "You purchase the bikini bottoms, these will look nice on [KittyX.Name]."
                            $ Player.Inventory.append("Kitty bikini bottoms")
                            $ Player.Cash -= 60
                        else:
                            "You don't have enough for that."  
                "Buy blue miniskirt for $50." if "blue skirt" not in KittyX.Inventory and "Kitty blue skirt" not in Player.Inventory:            
                        if Player.Cash >= 50:
                            "You purchase the blue skirt, this will look nice on [KittyX.Name]."
                            $ Player.Inventory.append("Kitty blue skirt")
                            $ Player.Cash -= 50
                        else:
                            "You don't have enough for that."  
                "Never mind.":
                    pass
        "Gifts for [EmmaX.Name]" if "met" in EmmaX.History:
            menu:  
                "Buy white lace bra for $90." if "lace bra" not in EmmaX.Inventory and "Emma lace bra" not in Player.Inventory:            
                        if Player.Cash >= 90:
                            "You purchase the lace bra, this will look nice on [EmmaX.Name]."
                            $ Player.Inventory.append("Emma lace bra")
                            $ Player.Cash -= 90
                        else:
                            "You don't have enough for that."
                "Buy white lace panties for $110." if "lace panties" not in EmmaX.Inventory and "Emma lace panties" not in Player.Inventory:            
                        if Player.Cash >= 110:
                            "You purchase the lace panties, these will look nice on [EmmaX.Name]."
                            $ Player.Inventory.append("Emma lace panties")
                            $ Player.Cash -= 110
                        else:
                            "You don't have enough for that."   
                "Buy pantyhose for $50." if "pantyhose" not in EmmaX.Inventory and "Emma pantyhose" not in Player.Inventory:          
                    if Player.Cash >= 50:
                        "You purchase the hose, these will look nice on [EmmaX.Name]."             
                        $ Player.Inventory.append("Emma pantyhose")
                        $ Player.Cash -= 50
                    else:
                        "You don't have enough for that."   
                "Buy stockings and garterbelt for $100." if "stockings and garterbelt" not in EmmaX.Inventory and "stockings and garterbelt" not in Player.Inventory and ApprovalCheck(EmmaX, 1500):          
                    if Player.Cash >= 100:
                        "You purchase the stockings, these will look nice on [EmmaX.Name]."             
                        $ Player.Inventory.append("stockings and garterbelt")
                        $ Player.Cash -= 100
                    else:
                        "You don't have enough for that."   
                "Buy white bikini top for $60." if "bikini top" not in EmmaX.Inventory and "Emma bikini top" not in Player.Inventory:            
                        if Player.Cash >= 60:
                            "You purchase the bikini top, this will look nice on [EmmaX.Name]."
                            $ Player.Inventory.append("Emma bikini top")
                            $ Player.Cash -= 60
                        else:
                            "You don't have enough for that."
                "Buy white bikini bottoms for $60." if "bikini bottoms" not in EmmaX.Inventory and "Emma bikini bottoms" not in Player.Inventory:            
                        if Player.Cash >= 60:
                            "You purchase the bikini bottoms, these will look nice on [EmmaX.Name]."
                            $ Player.Inventory.append("Emma bikini bottoms")
                            $ Player.Cash -= 60
                        else:
                            "You don't have enough for that."  
                "Never mind.":
                    pass
        "Gifts for [LauraX.Name]" if "met" in LauraX.History:
            menu:  
                "Buy red corset for $70." if "corset" not in LauraX.Inventory and "Laura corset" not in Player.Inventory:            
                    if Player.Cash >= 70:
                        "You purchase the corset, this will look nice on [LauraX.Name]."
                        $ Player.Inventory.append("Laura corset")
                        $ Player.Cash -= 70
                    else:
                        "You don't have enough for that."
                "Buy red lace corset for $90." if "lace corset" not in LauraX.Inventory and "Laura lace corset" not in Player.Inventory:            
                    if Player.Cash >= 90:
                        "You purchase the lace corset, this will look nice on [LauraX.Name]."
                        $ Player.Inventory.append("Laura lace corset")
                        $ Player.Cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy red lace panties for $110." if "lace panties" not in LauraX.Inventory and "Laura lace panties" not in Player.Inventory:            
                    if Player.Cash >= 110:
                        "You purchase the lace panties, these will look nice on [LauraX.Name]."
                        $ Player.Inventory.append("Laura lace panties")
                        $ Player.Cash -= 110
                    else:
                        "You don't have enough for that."  
                "Buy black bikini top for $50." if "bikini top" not in LauraX.Inventory and "Laura bikini top" not in Player.Inventory:            
                        if Player.Cash >= 50:
                            "You purchase the bikini top, this will look nice on [LauraX.Name]."
                            $ Player.Inventory.append("Laura bikini top")
                            $ Player.Cash -= 50
                        else:
                            "You don't have enough for that."
                "Buy black bikini bottoms for $50." if "bikini bottoms" not in LauraX.Inventory and "Laura bikini bottoms" not in Player.Inventory:            
                        if Player.Cash >= 50:
                            "You purchase the bikini bottoms, these will look nice on [LauraX.Name]."
                            $ Player.Inventory.append("Laura bikini bottoms")
                            $ Player.Cash -= 50
                        else:
                            "You don't have enough for that."  
                "Never mind.":
                    pass
        "Buy books":
            menu Shop_Books:
                "Buy \"Dazzler and Longshot\" for $20.":
                    "A sappy romantic novel about two starcrossed lovers."
                    if "DL" not in Shop_Inventory: #if Inventory_Check("Dazzler and Longshot") >= 4:
                        "They seem to be out of stock at the moment."
                    elif Player.Cash >= 20:                
                        "You purchase the book."
                        $ Shop_Inventory.remove("DL")
                        $ Player.Inventory.append("Dazzler and Longshot")
                        $ Player.Cash -= 20
                    else:
                        "You don't have enough for that."        
                "Buy \"256 Shades of Grey\" for $20.":
                    "A gripping sexual thriller about a stern red-headed \"goblin queen\" and her subject."
                    if "G" not in Shop_Inventory: #if "256 Shades of Grey" in Player.Inventory:
                        "They seem to be out of stock at the moment."
                    elif Player.Cash >= 20:                
                        "You purchase the book."
                        $ Shop_Inventory.remove("G")
                        $ Player.Inventory.append("256 Shades of Grey")
                        $ Player.Cash -= 20
                    else:
                        "You don't have enough for that."
                "Buy \"Avengers Tower Penthouse\" for $20.":
                    "A book filled with nude pictures of various Avengers, sexy."
                    if "A" not in Shop_Inventory:
                        "They seem to be out of stock at the moment."
                    elif Player.Cash >= 20:                
                        "You purchase the book."
                        $ Shop_Inventory.remove("A")
                        $ Player.Inventory.append("Avengers Tower Penthouse")
                        $ Player.Cash -= 20
                    else:
                        "You don't have enough for that."
                "Back":
                    jump Shop
            jump Shop_Books
        "Buy Cologne":
            if Day < 50:
                "These are currently out of stock, check back later."
                jump Shop
            menu:
                "Examine the Mandrill Cologne (\"Nothin says lovin like a shiny red butt\").":            
                    menu:
                        "This cologne is guaranteed to make women love you more [[+Love]."
                        "Buy Mandrill Cologne for $150":
                            pass
                        "Never mind.":
                            jump Shop                 
                    if "Mandrill Cologne" in Player.Inventory:
                        "They seem to be out of stock, maybe check back later."
                    elif Player.Cash >= 150:                
                        "You purchase one bottle of Mandrill Cologne."
                        $ Player.Inventory.append("Mandrill Cologne")
                        $ Player.Inventory.append("Mandrill Cologne")
                        $ Player.Inventory.append("Mandrill Cologne")
                        $ Player.Inventory.append("Mandrill Cologne")
                        $ Player.Inventory.append("Mandrill Cologne")
                        $ Player.Cash -= 150
                    else:
                        "You don't have enough for that."
                "Examine the Purple Rain Cologne (\"They can't resist your charms\").":
                    menu:
                        "This cologne is guaranteed to make women more suggestible to your orders until tomorrow [[+Obedience]."
                        "Buy Purple Rain Cologne for $200":
                            pass
                        "Never mind.":
                            jump Shop   
                    if "Purple Rain Cologne" in Player.Inventory:
                        "They seem to be out of stock, maybe check back later."
                    elif Player.Cash >= 200:                
                        "You purchase one bottle of Purple Rain Cologne."
                        $ Player.Inventory.append("Purple Rain Cologne")
                        $ Player.Inventory.append("Purple Rain Cologne")
                        $ Player.Inventory.append("Purple Rain Cologne")
                        $ Player.Inventory.append("Purple Rain Cologne")
                        $ Player.Inventory.append("Purple Rain Cologne")
                        $ Player.Inventory.append("Purple Rain Cologne")
                        $ Player.Cash -= 200
                    else:
                        "You don't have enough for that."
                "Examine the Corruption Cologne (\"Let the wild out\").":
                    menu:
                        "This cologne is guaranteed to make women let loose their wild side [[-Inhibition]."
                        "Buy Corruption Cologne for $250":
                            pass
                        "Never mind.":
                            jump Shop   
                    if "Corruption Cologne" in Player.Inventory:
                        "They seem to be out of stock, maybe check back later."
                    elif Player.Cash >= 250:                
                        "You purchase one bottle of Corruption Cologne."
                        $ Player.Inventory.append("Corruption Cologne")
                        $ Player.Inventory.append("Corruption Cologne")
                        $ Player.Inventory.append("Corruption Cologne")
                        $ Player.Inventory.append("Corruption Cologne")
                        $ Player.Inventory.append("Corruption Cologne")
                        $ Player.Cash -= 250
                    else:
                        "You don't have enough for that."
                "Back":
                    pass                
        "Exit Store":
            return
    jump Shop
return

# end Shop Interface / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start LikeUpdater / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 

#label LikeUpdater(Primary = 0, Value = 1, Noticed = 1,BO=[]):
#    # call LikeUpdater(RogueX,1)
#    # Primary is the primary girl in action, Value is the amount added/subtracted
#    # Noticed is whether it matters if she notices or not.
#    $ BO = TotalGirls[:]                
#    if Primary 
#    while BO:
#            if BO[0]Loc == bg_current:
#                    if not Noticed or "noticed " + Primary.Tag in BO[0].RecentActions: # if "noticed Rogue"
#                                #If girl was participating in Primary's activity
#                                $ Primary.GirlLikeUp(BO[0],Value)
#                                $ BO[0].GirlLikeUp(Primary,Value)
#            $ BO.remove(BO[0])
#    return
    
# End LikeUpdater / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 



# Start Display/Animation Stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /   
# Start Set the Scene  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /      
label Set_The_Scene(Chr = 1, Entry = 0, Dress = 1, TrigReset = 1, Quiet=0,BO=[]):
        # If Chr, then display the characters in the room
        # If Entry, then show the "entry" version of a room, such as a closed door, does not display characters
        # If Dress, then check whether the character is underdressed when displaying her
        # Trigreset resets triggers
        # if Quiet, no fade to black                
        
        if not Quiet:
            show blackscreen onlayer black 
        
        if Entry:
            $ Chr = 0
            call AllHide 
            
        call Display_Background(Entry) 
        
        if Current_Time == 'Night':
                show NightMask onlayer nightmask
        else:          
                hide NightMask onlayer nightmask  
                         
        if TrigReset:
                # resets triggers
                $ Trigger = 0    
                $ Trigger2 = 0 if Trigger2 != "jackin" else "jackin"
                $ Trigger3 = 0
                $ Trigger4 = 0
                $ Trigger5 = 0
                $ TrigReset = 0
                        
        if Chr:
                call Present_Check  #culls out Party to 2,
                #sets location to bg_current, removes extra girls, sets Focus to a girl in the room   
                
                $ BO = TotalGirls[:]   
                
                while BO:
                        #loops through and makes choices. 
                        if Ch_Focus.Loc != bg_current and BO[0].Loc == bg_current: 
                                #if the focused girl is not in the room, pick someone else
                                call Shift_Focus(BO[0])
                                
                        if Ch_Focus != BO[0]:
                                #moves all other girls to Stage Right, 75 layer
                                $ BO[0].SpriteLoc = StageRight 
                                $ BO[0].Layer = 75                                
                        call Display_Girl(BO[0],Dress,TrigReset) 
                        $ BO.remove(BO[0])      
                # set and display primary girl
                if Ch_Focus.Loc == bg_current: 
                        $ Ch_Focus.SpriteLoc = StageCenter
                        $ Ch_Focus.Layer = 100
                        call Display_Girl(Ch_Focus,Dress,TrigReset) 
                    
                if bg_current == "bg study" and Current_Time != "Night":   
                        show Professor at SpriteLoc(StageLeft) zorder 25 
                else:
                        hide Professor
                
        else:            
                call AllHide(1) #removes all girls that aren't there.  
        show Chibi_UI
        hide Cellphone
        
        if bg_current == "bg classroom" and EmmaX.Loc == "bg teacher": 
                #if Emma is teaching, sets teaching outfit 
                call AltClothes(EmmaX,8)      
                $ EmmaX.OutfitChange()
                        
        if TrigReset and Dress:       
                #resets your clothing if nude
                call Get_Dressed
        
        hide DressScreen
        if "Historia" in Player.Traits: #Simulation haze
                show BlueScreen onlayer black
        else:
                hide BlueScreen onlayer black
        hide blackscreen onlayer black
        
        return
# End primary Display function / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /      
        
    
# Start shift Focus / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /      
label Shift_Focus(Chr = RogueX, Second = 0,BO=[]):      
        #When used like Shift_Focus(KittyX), changes the focus character and relative default positions
        if Chr not in TotalGirls:
                "Tell Oni [Chr]"
                $ RogueX.Gibberish = 0
        if Chr == Ch_Focus == Partner:
                #if somehow the partner and chosen girl are the same. . .    
                $ BO = TotalGirls[:]  
                $ BO.remove(Partner)
                while BO:
                        #loops through and makes choices.                
                        if BO[0].Loc == bg_current:
                                $ Partner = BO[0]
                        $ BO.remove(BO[0])
                #if anyone else is in the room, make her the partner. Do I want this? 
        if Chr.Loc == bg_current:
                #If she is where you're at. . .                  
                $ BO = TotalGirls[:]   
                $ BO.remove(Chr)             
                while BO:
                        #loops through and makes choices.    
                        if BO[0].Loc == bg_current:
                                #if other girl is in the room, shift her to second position
                                $ BO[0].SpriteLoc = StageRight
                                $ BO[0].Layer = 75
                                $ BO = [1]
                        $ BO.remove(BO[0])
                #and move Girl to first position
                $ Chr.SpriteLoc = StageCenter
                $ Chr.Layer = 100
        if Ch_Focus == Chr: 
                #If Girl was already the focal character, return
                pass
        elif Second and Second != Chr:
                #if a deliberate partner was offered to the call, use it
                $ Partner = Second
        elif Partner == Chr: 
                #If Chr was the Partner in a scene, make the existing focal character the Partner
                $ Partner = Ch_Focus
        $ Ch_Focus = Chr
        $ renpy.restart_interaction() 
        return  
# End shift Focus / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /      

# Start Display Girls / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
transform SpriteLoc(Loc = StageRight, LocY = 50):  
        #This puts the sprite at a location relative to the sent variable
        pos (Loc,LocY)
        
label Display_Girl(Chr=0,Dress = 1, TrigReset = 1, DLoc = 0, YLoc=50):
                # If Dress, then check whether the character is underdressed when displaying her
                # call Display_Girl(RogueX,0,0)
                if Chr not in TotalGirls:
                        "Tell Oni that in Display_Girl, Chr is [Chr]"
                
                if Chr not in Party and Chr.Loc != bg_current: 
                        # If girl isn't there, put her away 
                        if Chr == RogueX:
                                hide Rogue_Sprite
                        elif Chr == KittyX:
                                hide Kitty_Sprite
                        elif Chr == EmmaX:
                                hide Emma_Sprite
                        elif Chr == LauraX:
                                hide Laura_Sprite
                        call expression Chr.Tag + "_Hide"   
                        $ Chr.OutfitChange(Changed=1)
                        return
                        
                if Taboo and Dress: #If not in the showers, get dressed and dry off        
                        $ Chr.OutfitChange(Changed=1)
                        $ Chr.Wet = 0
                elif Dress and Chr.Loc != "bg dangerroom" and Chr.OutfitDay != "gym":
                        #if she's not in the gym and arw wearing gym clothes. . .
                        $ Chr.Outfit = Chr.OutfitDay      
                        $ Chr.OutfitChange(Changed=1)
                          
                if Chr.Loc != "bg showerroom" and Chr.Loc != "bg pool":
                        $ Chr.Water = 0
                                                    
                if TrigReset:
                        # resets triggers
                        $ Trigger = 0    
                        $ Trigger2 = 0 if Trigger2 != "jackin" else "jackin"
                        $ Trigger3 = 0
                        $ Trigger4 = 0
                        $ Trigger5 = 0
                
                if Partner == Chr:
                        $ DLoc = StageRight #Moves Girl over if she's secondary
                
                if DLoc: #if sent a pre-location, use that, otherwise, accept the existing one. 
                        $ Chr.SpriteLoc = DLoc
                else:
                        $ DLoc = Chr.SpriteLoc
                
                call expression Chr.Tag + "_Hide"
                
                #displays girl if present, Sets her as local if in a party
                $ Chr.Loc = bg_current 
                
                if Dress:   
                        #If in public, check to see if clothes are too sexy, and change them if necessary
                        call OutfitShame(Chr)
                                                
                if bg_current == "bg movies" or bg_current == "bg restaurant":
                        #shifts them downward if on a date
                        $ YLoc = 250

                #Display Girl              
                if Chr == RogueX:
                        if not renpy.showing("Rogue_Sprite"): 
                            show Rogue_Sprite at SpriteLoc(1000,YLoc) zorder Chr.Layer:
                                    offset (0,0)
                                    anchor (0.5, 0.0)  
                                    pos (1000,YLoc)  
                        show Rogue_Sprite zorder Chr.Layer: # Chr.Layer:
                                easeout .5 alpha 1
                                easeout .5 zoom 1
                                offset (0,0)
                                anchor (0.5, 0.0)  
                                easeout .5 pos (DLoc,YLoc)
                        show Rogue_Sprite: # Chr.Layer:
                                alpha 1
                                zoom 1
                                offset (0,0)
                                anchor (0.5, 0.0)  
                                pos (DLoc,YLoc)  
                elif Chr == KittyX:
                        if not renpy.showing("Kitty_Sprite"): 
                            show Kitty_Sprite at SpriteLoc(1000,YLoc) zorder Chr.Layer:   
                                    offset (0,0)
                                    anchor (0.5, 0.0)  
                                    pos (1000,YLoc)  
                        show Kitty_Sprite zorder Chr.Layer: # Chr.Layer:
                                easeout .5 alpha 1
                                easeout .5 zoom 1
                                offset (0,0)
                                anchor (0.5, 0.0)  
                                easeout .5 pos (DLoc,YLoc) 
                        show Kitty_Sprite: # Chr.Layer:
                                alpha 1
                                zoom 1
                                offset (0,0)
                                anchor (0.5, 0.0)  
                                pos (DLoc,YLoc)  
                elif Chr == EmmaX:
                        if not renpy.showing("Emma_Sprite"): 
                            show Emma_Sprite at SpriteLoc(1000,YLoc) zorder Chr.Layer:   
                                    offset (0,0)
                                    anchor (0.5, 0.0)  
                                    pos (1000,YLoc)  
                        show Emma_Sprite zorder Chr.Layer: # Chr.Layer:
                                easeout .5 alpha 1
                                easeout .5 zoom 1
                                offset (0,0)
                                anchor (0.5, 0.0)  
                                easeout .5 pos (DLoc,YLoc) 
                        show Emma_Sprite: # Chr.Layer:
                                alpha 1
                                zoom 1
                                offset (0,0)
                                anchor (0.5, 0.0)  
                                pos (DLoc,YLoc)  
                elif Chr == LauraX:
                        $ Chr.Claws = 0 # Resets her claws
                        if not renpy.showing("Laura_Sprite"): 
                            show Laura_Sprite at SpriteLoc(1000,YLoc) zorder Chr.Layer:
                                    offset (0,0)
                                    anchor (0.5, 0.0)  
                                    pos (1000,YLoc)  
                        show Laura_Sprite zorder Chr.Layer: # Chr.Layer:
                                easeout .5 alpha 1
                                easeout .5 zoom 1
                                offset (0,0)
                                anchor (0.5, 0.0)  
                                easeout .5 pos (DLoc,YLoc) 
                        show Laura_Sprite: # Chr.Layer:
                                alpha 1
                                zoom 1
                                offset (0,0)
                                anchor (0.5, 0.0)  
                                pos (DLoc,YLoc) 
                #End show Chr     
                
                return
                            
#                $ Char_Temp = Chr.Name + "_Sprite" 
#                if not renpy.showing("Char_Temp"):                    
#                        "CX" #diagnostic    
#                show "Chr.Name + '_Sprite'": 
##                show expression Chr.Tag + "_Sprite": 
#                            alpha 1
#                            zoom 1
#                            offset (0,0)
#                            anchor (0.5, 0.0)  
#                            easeout .5 pos (DLoc,YLoc)   
#                show "Chr.Name + '_Sprite'":  
##                show expression Chr.Tag + "_Sprite":   
#                            alpha 1
#                            zoom 1
#                            offset (0,0)
#                            anchor (0.5, 0.0)  
#                            pos (DLoc,YLoc)

# End Display Girls / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /     

image Punchout:
    Null(0,0)
    
label Punch:
    #causes the screen to shake a bit
    show Punchout with vpunch
    hide Punchout
    return

# All Reset / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label AllReset(Chr = 0,BO=[]):     
    #resets all the sex animation poses
    #call AllReset("all")
    if Chr in TotalGirls:
            $ BO = [Chr] 
    else:
            $ BO = TotalGirls[:]
            
    while BO:
            call expression BO[0].Tag + "_BJ_Reset"
            call expression BO[0].Tag + "_TJ_Reset"
            call expression BO[0].Tag + "_HJ_Reset"
            call expression BO[0].Tag + "_Sex_Reset"
            call expression BO[0].Tag + "_Doggy_Reset"
            call expression BO[0].Tag + "_Hide"    
            if BO[0] == RogueX:
                if RogueX.Loc == bg_current:
                        show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc,50) zorder RogueX.Layer:
                                ease .5 zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.6, 0.0)
                        show Rogue_Sprite:
                                zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.6, 0.0) pos (RogueX.SpriteLoc,50)                                
                else:
                        hide Rogue_Sprite   
            if BO[0] == KittyX:
                if KittyX.Loc == bg_current:
                        show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc,50) zorder KittyX.Layer:
                                ease .5 zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0)
                        show Kitty_Sprite:
                                zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0) pos (KittyX.SpriteLoc,50)
                else:
                        hide Kitty_Sprite
            if BO[0] == EmmaX:       
                if EmmaX.Loc == bg_current:
                        show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc,50) zorder EmmaX.Layer:
                                ease .5 zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0)
                        show Emma_Sprite:
                                zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0) pos (EmmaX.SpriteLoc,50)
                else:
                        hide Emma_Sprite
            if BO[0] == LauraX:     
                if LauraX.Loc == bg_current:
                        show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc,50) zorder LauraX.Layer:
                                ease .5 zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0)
                        show Laura_Sprite:
                                zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0) pos (LauraX.SpriteLoc,50)
                else:
                        hide Laura_Sprite
            $ BO.remove(BO[0])
    return
# End All Reset / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label AllHide(Cull=0):    
        if Cull or RogueX.Loc != bg_current:
                hide Rogue_Sprite
                call Rogue_Hide
        if Cull or KittyX.Loc != bg_current:
                hide Kitty_Sprite
                call Kitty_Hide
        if Cull or EmmaX.Loc != bg_current:
                hide Emma_Sprite
                call Emma_Hide
        if Cull or LauraX.Loc != bg_current:
                hide Laura_Sprite
                call Laura_Hide
        if Cull or "bg study" != bg_current:
                hide Professor
        return
# End Display/Animation Stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 


# Start Threesome/Lesbian stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label Sex_Menu_Threesome(Girl=0):
        if not Girl or Girl not in TotalGirls:
            return
        menu:          
            "Do you want to join us [RogueX.Name]?" if RogueX.Loc == bg_current and Girl != RogueX:
                    if Partner == RogueX:
                        #if she's already involved
                        ch_r "If I'd been do'in it right you wouldn't hafta ask. . ."
                    else: 
                        call Girls_Noticed(Girl,RogueX,1)
                        if Girl.Loc != bg_current:
                            # if the lead ran away
                            ch_r "Oh, well. . . I'm still game. . ."                            
                            call Rogue_SexAct("switch")   
                        elif RogueX.Loc == bg_current:
                            ch_r "I s'pose I could lend a hand . ."
                        else:
                            "She seems uncomfortable with this situation and leaves the room." 
                            
            "Do you want to join us [KittyX.Name]?" if KittyX.Loc == bg_current and Girl != KittyX:
                    if Partner == KittyX:
                        #if she's already involved
                        ch_k "Lol, what are you even talking about?"
                    else: 
                        call Girls_Noticed(Girl,KittyX,1)                        
                        if Girl.Loc != bg_current:
                            # if the lead ran away
                            ch_k "Whoa, drama much? . ."
                            call Kitty_SexAct("switch")   
                        elif KittyX.Loc == bg_current:
                            ch_k "I could[KittyX.like]give it a try. . ."
                        else:
                            "She seems uncomfortable with this situation and leaves the room." 
                            
            "Do you want to join us [EmmaX.Name]?" if EmmaX.Loc == bg_current and Girl != EmmaX:
                    if Partner == EmmaX:
                        #if she's already involved
                        ch_e "Have I not been keeping up?"
                    else: 
                        call Girls_Noticed(Girl,EmmaX,1)                        
                        if Girl.Loc != bg_current:
                            # if the lead ran away
                            ch_e "Pity. . ."
                            call Emma_SexAct("switch")   
                        elif EmmaX.Loc == bg_current:
                            ch_e "So what did you have in mind for us. . ."
                        else:
                            "She seems uncomfortable with this situation and leaves the room." 
                                        
            "Do you want to join us [LauraX.Name]?" if LauraX.Loc == bg_current and Girl != LauraX:
                    if Partner == LauraX:
                        #if she's already involved
                        ch_l "I already am."
                    else: 
                        call Girls_Noticed(Girl,LauraX,1)                        
                        if Girl.Loc != bg_current:
                            # if the lead ran away
                            ch_l "Her loss. . ."
                            call Laura_SexAct("switch")   
                        elif LauraX.Loc == bg_current:
                            ch_l "Hm, ok. . ."
                        else:
                            "She seems uncomfortable with this situation and leaves the room." 
                                            
            "Never mind [[something else]":
                    pass        
        if AloneCheck(Girl) and Girl.Taboo == 20:
                $ Girl.Taboo = 0
                $ Taboo = 0
        return
          
label Partner_Like(Girl=0,Value=1,AltValue=1,Measure=800,Partner=Partner):
        # This raises a partner's "like" stat by an amount
        # call Partner_Like(RogueX,2)
        # Girl is the lead, Partner is the second girl
        # Value is the amount it changes if Measure is met, otherwise AltValue
        if Girl not in TotalGirls or Partner not in TotalGirls: #should remove "character don't exist" errors
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
        #End Trigger4 bonuses
        
        $ Partner.GLG(Girl,Measure,Value,1)
        $ Girl.GLG(Partner,Measure,Value,1)                         
        return
#End Partner_Like
    
      
# Start Room Stat Booster / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label RoomStatboost(Type=0,Check=0,Amount=0,BO=[]):
        # raises/lowers stats of all girls in the room by a fixed amount
        # ie call RoomStatboost("Love",80,2)  
        $ BO = TotalGirls[:]
        while BO:
            if BO[0].Loc == bg_current or BO[0] in Nearby:
                    $ BO[0].Statup(Type, Check, Amount) 
            $ BO.remove(BO[0])
        return
# end Room Stat Booster / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 


# Start GirlWaitUp / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label GirlWaitUp(Local=0,Check=70,D20=0,Teach=0,BOA=[],BOB=[]):                
        #This adjusts girl's liking each other based on shared activities
        #Local =1 only checks if they are in the room with you.
        #it goes R+K, R+E, R+L, K+E, K+L, E+L, etc. 
        # was call GirlWaitAttract()
        # now call GirlWaitUp
        
        $ D20 = renpy.random.randint(0,1) if not D20 else D20
        
        if EmmaX.Loc == "bg teacher":
                $ EmmaX.Loc = "bg classroom" #Sets Emma to being in class if she's teaching
                $ Teach = 1
        $ BOA = TotalGirls[:]
        #$ BOA.extend(TotalGirls) 
        while BOA:
            #loops through the girls in an outer loop
            $ BOB = TotalGirls[:]
            while BOB:
                    #loops through the girls in an inner loop
                    if BOA[0] != BOB[0] and BOA[0].Loc == BOB[0].Loc:                                
                            #if the two girls are not identical, and are in the same location. . .
                            if BOA[0].Loc == "bg classroom":
                                            $ BOA[0].GLG(BOB[0],700,1,1) 
                                            #R_LikeKitty += 1
                            elif BOA[0].Loc == "bg dangerroom":
                                            $ BOA[0].GLG(BOB[0],700,(1+D20),1) 
                                            #R_LikeKitty += 1+D20
                            elif BOA[0].Loc == "bg showerroom":                             
                                    if BOA[0] == EmmaX:
                                            #if it's EmmaX. . .                
                                            $ BOA[0].GLG(BOB[0],900,3,1) 
                                            #EmmaX.LikeKitty += 3  
                                    elif BOB[0] == EmmaX and BOA[0] != LauraX:
                                            #If it's anyone other than Laura seeing Emma's body. . .                    
                                            $ BOA[0].GLG(BOB[0],900,3,1) 
                                            #RogueX.LikeEmma += 3 
                                    else:                                                                 
                                            $ BOA[0].GLG(BOB[0],900,2,1) 
                                            #RogueX.LikeKitty += 2                                                          
                            else:                                            
                                    $ BOA[0].GLG(BOB[0],Check, D20,1) 
                                    #RogueX.LikeKitty += D20  
                            
                            #RogueX.LikeKitty += (int(KittyX.Shame/5)) #Rogue likes Kitty based on how slutty Kitty looks        
                            if BOA[0] == EmmaX:
                                    #if it's Emma. . .        
                                    #raise Emma's like by 1/4 other girl's shame
                                    $ BOA[0].GLG(BOB[0],1000,(int(BOB[0].Shame/4)),1) 
                            elif BOB[0] == EmmaX and BOA[0] != LauraX:
                                    #If it's anyone other than Laura seeing Emma's body. . .    
                                    #raise girl's like by 1/4 other girl's shame
                                    $ BOA[0].GLG(BOB[0],1000, (int(BOB[0].Shame/4)),1) 
                            else:                                           
                                    #raise girls's like by 1/5 other girl's shame
                                    $ BOA[0].GLG(BOB[0],1000, (int(BOB[0].Shame/5)),1) 
                            
                    $ BOB.remove(BOB[0])
            $ BOA.remove(BOA[0])
        if Teach:
                $ EmmaX.Loc = "bg teacher" #Sets Emma to being a teacher again        
        return
# End GirlWaitUp / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 

# Start Lesbian Jumping check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label LesCheck(Girls=[],BO=[]):
        #Called by Wait, Checks if any girls will jump each other behind the scenes. . . 
        # They will if they have over 500 Inbt and are thirsty
        
        if "three" not in EmmaX.History:  
                #this addes threecheck if she's really slutty
                if EmmaX.Thirst >= 30 and ApprovalCheck(EmmaX, 800, "I"):
                        $ EmmaX.History.append("three") 
                                
        $ BO = ActiveGirls[:]                
        while BO:
                #loops through and makes choices. 
                if BO[0] == RogueX and "touch" not in RogueX.Traits:
                        #skip if Rogue and she doesn't have touch upgrade
                        pass
                elif BO[0] == EmmaX and "three" in EmmaX.History: 
                        #skip if it's Emma and she doesn't do threesomes
                        pass
                elif ApprovalCheck(BO[0], 500, "I") and BO[0].Thirst >= 30: #and "refused" not in R_DailyActions?
                        if ("mono" not in BO[0].Traits or BO[0].Break[0]) and BO[0] not in Party:
                            $ Girls.append(BO[0])      
                            if BO[0].Thirst >= 60:
                                    $ Girls.append(BO[0])      
                        if BO[0].Thirst >= 90:
                                $ Girls.append(BO[0]) 
                
                $ BO.remove(BO[0])
                   
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
                elif (Girls[1] in Player.Harem and Girls[0] in Player.Harem) and Girls[0].GirlLikeCheck(Girls[1]) >= 600: 
                        $ Partner = Girls[1]
                elif Girls[1].GirlLikeCheck(Girls[0]) >= 800 and Girls[0].GirlLikeCheck(Girls[1]) >= 800: 
                        $ Partner = Girls[1]
                elif Girls[1].Thirst >= 90 and Girls[0].GirlLikeCheck(Girls[1]) >= 600: 
                        $ Partner = Girls[1]
                else:   
                        #if not picked, remove this girl from the list
                        $ Girls.remove(Girls[1])
        if not Partner:
                # if nobody is picked, then return, otherwise you should have at least two girls picked
                return
                
        $ Partner = 0
        #move both girls into the same room   
                
        if bg_current != Girls[0].Home:
                #if you aren't in first girl's room, move both there. 
                $ Girls[0].Loc = Girls[0].Home
                $ Girls[1].Loc = Girls[0].Home
        elif bg_current != Girls[1].Home:
                #if you are in the first girl's room, move both to the seconds'. 
                $ Girls[0].Loc = Girls[1].Home
                $ Girls[1].Loc = Girls[1].Home
                             
        $ Girls[0].AddWord(1,"les",0,0,0) #adds "les" to recent actions for both girls
        $ Girls[1].AddWord(1,"les",0,0,0) #adds "les" to recent actions for both girls
        
        $ Girls[0].GLG(Girls[1],700,15,1)         #Like +15 if under 700
        $ Girls[1].GLG(Girls[0],700,15,1)         #Like +15 if under 700
        
        $ Girls[0].GLG(Girls[1],900,10,1)         #Like +10 if under 900
        $ Girls[1].GLG(Girls[0],900,10,1)         #Like +10 if under 900
        
        $ Girls[0].GLG(Girls[1],1000,5,1)         #Like +5 if under 1000
        $ Girls[1].GLG(Girls[0],1000,5,1)         #Like +5 if under 1000
                
        $ Girls[0].DrainWord("arriving",1,0) #removes "arriving" from recent 
        $ Girls[1].DrainWord("arriving",1,0) #removes "arriving" from recent 
        
        $ Girls[0].Statup("Lust", 60, 20) 
        $ Girls[1].Statup("Lust", 60, 20) 
        
        $ Girls[0].Thirst -= 5
        $ Girls[1].Thirst -= 5
        return
# end Les_Check, checking to see if the girls jump each other / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
       

# Start Harem stat boost  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label HaremStatup(Girl=0,Check=1000,Value=0,Greater=0,BOA=[],BOB=[]):
        # This cycles through every Harem member and applies a like-up to each one. 
        # if Girl == "All", it cycles all of them.
        # call HaremStatup(LauraX,700,-5)
        if "Historia" in Player.Traits:
                return
        if Girl == "All" or Girl == 0:
                $ BOA = Player.Harem[:]
        elif Girl in TotalGirls:
                $ BOA = [Girl]
        else: 
                return
        while BOA:
                #loops entire harem is "all," else just loops the one girl through.
                $ BOB = Player.Harem[:]
                if BOA[0] in BOB: 
                    # remove the girl being checked from the potential matches
                    $ BOB.remove(BOA[0])
                while BOB:
                    # If Girl likes the Harem Member below the Check value, apply Value to it. 
                    $ BOA[0].GLG(BOB[0],Check,Value,1)           
                    $ BOB.remove(BOB[0])
                $ BOA.remove(BOA[0])
        return
#End Harem stat boost  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# End Lesbian stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /        
       
       
       
# Start Jumping check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label JumperCheck(Girls=[],BO=[]):
        #decides whether a girl wants to jump you unexpectedly
        if "nope" in Player.RecentActions or Party:
                #if you refused sex. . .
                return
        
        $ BO = ActiveGirls[:]                
        while BO: 
                if "les" in BO[0].RecentActions and ApprovalCheck(BO[0], 1600 - BO[0].SEXP, TabM=0):
                        #if they might be into you joining their lesbian adventure. . .
                        call Call_For_Les(BO[0])
                    
                if "locked" in Player.Traits and BO[0].Loc != bg_current:
                        #if the door's locked and she's not in the room, skip it
                        pass
                elif BO[0].Action and BO[0].Thirst >= 30 and ApprovalCheck(BO[0], 500, "I") and "refused" not in BO[0].DailyActions and "met" in BO[0].History:
                        if "chill" not in BO[0].Traits and BO[0].Tag not in Player.DailyActions and "jumped" not in BO[0].DailyActions and BO[0].Loc != "bg teacher":
                            # I rule out if she is teaching, she won't jump you. . .
                            if renpy.random.randint(0,3) > 1:
                                    $ Girls.append(BO[0])  
                            if BO[0].Thirst >= 60:
                                    $ Girls.append(BO[0])      
                        if BO[0].Thirst >= 90:
                                    $ Girls.append(BO[0])   
                $ BO.remove(BO[0]) 
                 
        if not Girls:
            return
                        
        if len(Girls) >= 2:
            $ renpy.random.shuffle(Girls)                
            while len(Girls) >= 2 and Girls[0] == Girls[1]:
                    $ Girls.remove(Girls[1])    #removes duplicates
            while len(Girls) > 2:
                    $ Girls.remove(Girls[2])    #removes any over 2
                    
        $ Partner = 0
        if len(Girls) >= 2:        
            #if there are two girls, it adds the second as a potential partner
            if Girls[0] in Player.Harem and Girls[1] in Player.Harem:
                    $ Partner = Girls[1]
            elif Girls[0].GirlLikeCheck(Girls[1]) >= 800 and Girls[1].GirlLikeCheck(Girls[0]) >= 800:
                    $ Partner = Girls[1]
        
        call Jumped #Launches the main event        
        
        if "nope" in Player.RecentActions:
                #if you refused sex. . .
                while Girls:         #clears list           
                        call Remove_Girl(Girls[0])
                        $ Girls.remove(Girls[0])                        
                jump Misplaced
        elif Girls:
                #if you had some sort of sexual encounter, it will hop you to the appropriate sex menu
                if Girls[0].Loc == bg_current:
                        call expression Girls[0].Tag + "_SexMenu" #call Rogue_SexMenu 
        
        if bg_current == "bg player":
                #if it jumped to your room. . .
                jump Player_Room
        return      
#End Jumper_Check, checking to see if a girl wants to jump you

label Jumped(Act=0):    
        # called by JumperCheck if a girl jumps you
        # Girls[0] is the girl    
        # make sure that this puts people in the right rooms after they do stuff. . .
        
        if Girls[0] == EmmaX and Partner and "three" not in EmmaX.History:
                    #if lead is Emma, there is a partner, but she doesn't share. . .
                    $ Girls.remove(Partner) 
                    $ Partner = 0  
        elif EmmaX in Girls and ((Taboo and "taboo" not in EmmaX.History) or "three" not in EmmaX.History):
                    #if partner is Emma and she doesn't share. . .
                    $ Girls.remove(EmmaX) 
                    $ Partner = 0        
        
        if not Girls:
                return
                
        if Girls[0].Loc != bg_current and "locked" in Player.Traits:
            #if the girl is not in the room with you, and your door is locked. . .            
            call Locked_Door(Girls[0])
            if not Girls or Girls[0].Loc != bg_current:
                    #if you refused her entry. . .
                    $ Player.RecentActions.append("nope")      
                    return     
                                        
        #sets their location        
        $ BO = Girls[:]                
        while BO:
                $ BO[0].Loc = bg_current
                $ BO.remove(BO[0]) 
        $ Girls[0].AddWord(1,"jumped","jumped") 
                        
        call Taboo_Level #makes sure Taboo level is accurate
        
        if Taboo and (not ApprovalCheck(Girls[0], 1500, TabM=3) or (Girls[0] == EmmaX and Taboo and "taboo" not in EmmaX.History)):
                #causes you to leave if the girl is not ready for public stuff                
                $ Act = "leave"
        
        if bg_current in PersonalRooms:             
                #Causes the girl to pull you out if she doesn't live in the room you're in  
                if bg_current == "bg player":
                                pass
                elif Girls[0].Home != bg_current and not (Partner and Partner.Home == bg_current):
                                #if it's not the first girl's room, and also not the second's
                                $ Act = "leave" 
                                
        if Room_Full(): #if the room is full. . .
                $ Act = "leave" 
        
        call Shift_Focus(Girls[0]) #this is not working, sometimes?
        call Set_The_Scene
         
        $ Player.RecentActions.append("jumped")  
        $ Girls[0].FaceChange("sly",1)
        if Act == "leave":        
                #if she's not supercool with public stuff. . .    
                "Suddenly, [Girls[0].Name] grabs your arm with a miscevious smile, and starts to lead you back towards your room."                
                menu:                
                    "Go along with it":                      
                        "You follow after her."
                    "Pull away from her and head back.":                    
                        $ Girls[0].Statup("Love", 90, -10) 
                        $ Girls[0].Statup("Obed", 50, 10) 
                        $ Girls[0].Statup("Obed", 95, 5) 
                        $ Girls[0].Statup("Inbt", 95, -5) 
                        $ Girls[0].FaceChange("sad",1)           
                        "You tell her to cut it out, and head back to what you were doing."
                        $ Player.RecentActions.append("nope")      
                        $ Girls[0].AddWord(1,"refused","refused") 
                        if not ApprovalCheck(Girls[0], 500, "O"):                        
                                $ Girls[0].AddWord(1,"angry","angry") 
                        return  
                        
                if Partner:       
                        "[Partner.Name] also follows along behind you."
                
                $ bg_current = "bg player"                   
                call CleartheRoom(Girls[0],1,1)    
                        
                call Taboo_Level #makes sure Taboo level is accurate                
        else:                     
            if Partner in TotalGirls:  
                    $ Girls[1].FaceChange("sly",1)                       
                    "Suddenly, [Girls[0].Name] pulls you aside and [Partner.Name] follows along."
            else:
                    "Suddenly, [Girls[0].Name] pulls you aside."
                      
        $ BO = Girls[:]                
        while BO:
                $ BO[0].Loc = bg_current
                $ BO.remove(BO[0])            
        call Set_The_Scene(Dress=0) 
                
        $ Girls[0].AddWord(1,"jumped","jumped",0,"jumped") #adds jumped to recent, daily, and history
        
        if Girls[0] == RogueX:
                ch_r "You've been dodge'in me lately."
                ch_r "Figured it was about time we did something about that."
        elif Girls[0] == KittyX:
                ch_k "Why haven't you been coming by?"
                ch_k "Wouldn't you enjoy some \"Kitty\" time?"
        elif Girls[0] == EmmaX:
                ch_e "You haven't been coming around to visit lately."
                ch_e "Is there any way I could tempt you?"
        elif Girls[0] == LauraX:
                ch_l "I'm horny, let's fuck."
        else: 
                return
            
        call Favorite_Actions(Girls[0],1) #returns a string of the action
        $ Act = _return
        $ Situation = Girls[0]
        
        if Act in ("anal","sex","blow","tit","hand","hotdog"):
                # if cock needs to be out. . .
                "[Girls[0].Name] reaches down and unzips your fly. . ."
                call Seen_First_Peen(Girls[0],Partner,1)
        
        if Partner:
                call Girls_Noticed(Girls[0],1) #calls the "noticed check" for this girl. 
                                
        # launches the appropriate scene based on the sex act in question.
        if Act == "anal":        
                call expression Girls[0].Tag + "_AnalPrep" #call R_AnalPrep                
        elif Act == "sex":
                call expression Girls[0].Tag + "_SexPrep" #call R_SexPrep
        elif Act ==  "lick pussy":
                call expression Girls[0].Tag + "_LP_Prep" #call R_LPlayer.Prep 
        elif Act == "fondle pussy":
                call expression Girls[0].Tag + "_FP_Prep" #call R_FPlayer.Prep
        elif Act == "blow":
                call expression Girls[0].Tag + "_BJ_Prep" #call R_BJ_Prep
        elif Act == "tit":
                call expression Girls[0].Tag + "_TJ_Prep" #call R_TJ_Prep
        elif Act == "hand":
                call expression Girls[0].Tag + "_HJ_Prep" #call R_HJ_Prep 
        elif Act == "hotdog":
                call expression Girls[0].Tag + "_HotdogPrep" #call R_HotdogPrep
        elif Act == "suck breasts":               
                call expression Girls[0].Tag + "_SB_Prep" #call R_SB_Prep
        elif Act == "fondle breasts":
                call expression Girls[0].Tag + "_FB_Prep" #call R_FB_Prep
        elif Act == "insert ass" or Act == "lick ass":
                call expression Girls[0].Tag + "_IA_Prep" #call R_IA_Prep
        else: #Act == "kiss you"
                call KissPrep(Girls[0]) #call R_KissPrep                 
        return
        
#End Jumped, when a girl does try to jump you/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        
        
# Start quick sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Quick_Sex(Girl=Ch_Focus,Act=0):    
        # called by Chitchat if a girl is horny
     
        $ Girl.FaceChange("sly",1)    
        $ Girl.AddWord(1,"quicksex","quicksex")
        menu:
            extend ""
            "Sure":
                    $ Girl.Statup("Love", 95, 4)
                    $ Girl.Statup("Obed", 50, 1)
                    $ Girl.Statup("Inbt", 90, 3)
            "No thanks":
                    $ Line = 0
                    $ Girl.Statup("Love", 80, -2)
                    if (2*Girl.Obed) >= (Girl.Love + Girl.Inbt + (5*Girl.Thirst)):
                            #she's more obedient than horny
                            $ Girl.FaceChange("sadside",1) 
                            $ Girl.Statup("Obed", 90, 7)
                            if Girl == RogueX: 
                                    ch_r "Ok, fine. . ."
                            elif Girl == KittyX:
                                    ch_k "Fine, whatever. . ."
                            elif Girl == EmmaX:
                                    ch_e "I can accept this. . ."
                            elif Girl == LauraX:                                
                                    ch_l "Ok. . ."
                            menu:
                                "Wait, on second thought. . .":
                                        $ Girl.Statup("Love", 80, -2)
                                        $ Girl.Statup("Obed", 80, -8)
                                        $ Line = "ask"
                                ". . . [[say nothing, still no].":
                                        pass
                    elif (ApprovalCheck(Girl, 600, "I") and Girl.Thirst >= 30) or Girl.Thirst >= 50:
                                        #she's pretty horny
                                        $ Girl.FaceChange("confused",1,Eyes="surprised") 
                                        $ Girl.Statup("Love", 80, -1)
                                        $ Girl.Statup("Obed", 70, 4)
                                        $ Girl.Statup("Inbt", 60, 5)
                                        $ Girl.Statup("Inbt", 90, 3)
                                        if Girl == RogueX: 
                                                ch_r "You're sure about that?"
                                        elif Girl == KittyX:
                                                ch_k "Seriously"
                                        elif Girl == EmmaX:
                                                ch_e "Have you thought this through?"
                                        elif Girl == LauraX:
                                                ch_l "Seriously, free sex here."
                                        $ Line = "ask"
                    #above stack falls through to here.            
                    if Line == "ask":
                            $ Line = 0
                            $ Count = 2
                            $ Cnt = 0
                            while Count:
                                    #loops at least twice, more if she starts begging
                                    $ Count -= 1
                                    menu:
                                        extend ""
                                        "Ok, fine.":
                                                $ Act = 1
                                                $ Count = 0
                                                $ Girl.FaceChange("sly",1) 
                                                $ Girl.Statup("Love", 80, 2)
                                                $ Girl.Statup("Love", 95, 3)
                                                $ Girl.Statup("Obed", 70, 2)
                                                $ Girl.Statup("Inbt", 90, 3)
                                                
                                        "Beg me." if Cnt < 100:
                                                $ Girl.Statup("Obed", 80, 2)
                                                $ Line = "beg"
                                        "Beg me again." if Cnt >= 100:
                                                $ Girl.Statup("Obed", 90, 2)
                                                $ Line = "beg"
                                            
                                        "Only if I get to choose.":
                                                $ Girl.FaceChange("smile",1,Brows="confused") 
                                                $ Girl.Statup("Love", 90, 2)
                                                $ Girl.Statup("Obed", 80, 3)
                                                $ Girl.Statup("Obed", 95, 3)
                                                $ Girl.Statup("Inbt", 85, 2)
                                                if Girl == RogueX: 
                                                        ch_r "Ok, fine."
                                                elif Girl == KittyX:
                                                        ch_k "Yeah, whatever."
                                                elif Girl == EmmaX:
                                                        ch_e "I suppose."
                                                elif Girl == LauraX:
                                                        ch_l "Fair."
                                                call expression Girl.Tag + "_SexMenu"
                                                return
                                                
                                        "Still no.":
                                                $ Girl.Statup("Love", 85, -2)
                                                $ Girl.Statup("Obed", 90, 3)
                                                if ApprovalCheck(Girl, 1500+(5*Cnt)-(10*Girl.Thirst), "LI"):
                                                            #if she's obedient, or her horniness is higher than her Inhibition
                                                            $ Line = "beg"
                                                elif not Cnt and Count:
                                                            #if you've never refused before
                                                            $ Girl.Uptop = 1 #Uptop up      
                                                            pause 1
                                                            call expression Girl.Tag + "_First_Topless" pass (1)    
                                                            $ Girl.Uptop = 0 #Uptop up       
                                                            $ Girl.FaceChange("confused",1,Mouth="smile") 
                                                            $ Girl.Statup("Inbt", 70, 3)
                                                            $ Girl.Statup("Inbt", 95, 3)
                                                            if Girl == RogueX: 
                                                                    ch_r "You -really- sure about that?"
                                                            elif Girl == KittyX:
                                                                    ch_k "Reaaaaally?"
                                                            elif Girl == EmmaX:
                                                                    ch_e "-No- second thoughts, [Girl.Petname]?"
                                                            elif Girl == LauraX:
                                                                    ch_l "I mean, come on."
                                                            $ Cnt += 25
                                    if Line == "beg":                                            
                                            if ApprovalCheck(Girl, 600+Cnt, "O") or ApprovalCheck(Girl, 1500+(5*Cnt)-(10*Girl.Thirst)):
                                                    #if she's obedient, or her horniness is higher than her Inhibition
                                                    if Cnt < 50:
                                                            #first time
                                                            $ Girl.FaceChange("sad",2) 
                                                            $ Girl.Statup("Love", 90, -2)
                                                            $ Girl.Statup("Obed", 50, 5)
                                                            $ Girl.Statup("Obed", 95, 3)
                                                            $ Girl.Statup("Inbt", 90, 3)
                                                            if Girl == RogueX: 
                                                                    ch_r "Please?"
                                                            elif Girl == KittyX:
                                                                    ch_k "Pretty please?"
                                                            elif Girl == EmmaX:
                                                                    ch_e ". . ."
                                                                    $ Girl.Statup("Love", 90, -2)
                                                                    $ Girl.Statup("Obed", 200, 3)
                                                                    ch_e ". . .Please?"
                                                            elif Girl == LauraX:
                                                                    ch_l "Um. . . Please?"
                                                    else:
                                                            #second time
                                                            $ Girl.FaceChange("sad",2,Eyes="surprised") 
                                                            $ Girl.Statup("Love", 90, -4)
                                                            $ Girl.Statup("Obed", 70, 6)
                                                            $ Girl.Statup("Obed", 200, 3)
                                                            $ Girl.Statup("Inbt", 90, 5)
                                                            if Girl == RogueX: 
                                                                    ch_r "Come on, I really need it. . ."
                                                            elif Girl == KittyX:
                                                                    ch_k "I need you, [Girl.Petname]!"
                                                            elif Girl == EmmaX:
                                                                    $ Girl.Statup("Love", 90, -2)
                                                                    $ Girl.Statup("Obed", 200, 1)
                                                                    ch_e "I. . . really need you here, [Girl.Petname]. . ."
                                                            elif Girl == LauraX:
                                                                    $ Girl.Statup("Obed", 80, 1)
                                                                    ch_l "I've got a fevah, and the only prescription is your dick. . ."
                                                    $ Count = 1 if Count <= 0 else Count #allows it to cycle one more time
                                                    $ Cnt += 100
                                            elif Cnt > 50:                     
                                                            #she refuses on second time
                                                            $ Girl.FaceChange("angry",1) 
                                                            $ Girl.Statup("Love", 70, -3)
                                                            $ Girl.Statup("Love", 85, -5)
                                                            $ Girl.Statup("Obed", 80, -2)
                                                            $ Girl.Statup("Inbt", 90, 4)
                                                            if Girl == RogueX: 
                                                                    ch_r "I'm not going to beg again."
                                                            elif Girl == KittyX:
                                                                    ch_k "Not even!"
                                                            elif Girl == EmmaX:
                                                                    $ Girl.Statup("Love", 90, -3)
                                                                    $ Girl.Statup("Obed", 70, -3)
                                                                    $ Girl.Statup("Obed", 200, 2)
                                                                    ch_e "I. . . Once was too much!"
                                                            elif Girl == LauraX:
                                                                    ch_l "Ooooh, you are pushing it, [Player.Name]."
                                            else:                                                        
                                                            #she refuses
                                                            $ Girl.FaceChange("sad",2,Brows="confused") 
                                                            $ Girl.Statup("Love", 95, -2)
                                                            $ Girl.Statup("Obed", 50, -2)
                                                            $ Girl.Statup("Obed", 90, -2)
                                                            $ Girl.Statup("Inbt", 90, 5)
                                                            if Girl == RogueX: 
                                                                    ch_r "I'm not going to beg."
                                                            elif Girl == KittyX:
                                                                    ch_k "That's. . . rude."
                                                            elif Girl == EmmaX:
                                                                    $ Girl.Statup("Obed", 70, -2)
                                                                    ch_e "That is so beneath me."
                                                            elif Girl == LauraX:
                                                                    ch_l "Not worth it. ."
                                    #end of "beg" chain               
                            #end of loop, if not Act, return disappointed  
                    $ Line = 0         
                    if not Act:
                            #she accepts your refusal
                            $ Girl.Statup("Love", 80, -2)
                            if Girl == RogueX: 
                                    ch_r "Ok, your loss, I guess. . ."
                            elif Girl == KittyX:
                                    ch_k "Too bad . ."
                            elif Girl == EmmaX:
                                    ch_e "Fine. . . I'll handle my own arrangements. . ."
                            elif Girl == LauraX:
                                    ch_l "Your loss. . ."
                            return
                            
        call Favorite_Actions(Girl,1) #returns a string of the action
        $ Act = _return
        
        if Act in ("anal","sex","blow","tit","hand","hotdog"):
                # if cock needs to be out. . .
                "[Girl.Name] reaches down and unzips your fly. . ."
                call Seen_First_Peen(Girl,Partner,1)
                                
        $ Situation = Girl
        
        # launches the appropriate scene based on the sex act in question.
        if Act == "anal":        
                call expression Girl.Tag + "_AnalPrep" #call R_AnalPrep                
        elif Act == "sex":
                call expression Girl.Tag + "_SexPrep" #call R_SexPrep
        elif Act ==  "lick pussy":
                call expression Girl.Tag + "_LP_Prep" #call R_LPlayer.Prep 
        elif Act == "fondle pussy":
                call expression Girl.Tag + "_FP_Prep" #call R_FPlayer.Prep
        elif Act == "blow":
                call expression Girl.Tag + "_BJ_Prep" #call R_BJ_Prep
        elif Act == "tit":
                call expression Girl.Tag + "_TJ_Prep" #call R_TJ_Prep
        elif Act == "hand":
                call expression Girl.Tag + "_HJ_Prep" #call R_HJ_Prep 
        elif Act == "hotdog":
                call expression Girl.Tag + "_HotdogPrep" #call R_HotdogPrep
        elif Act == "suck breasts":               
                call expression Girl.Tag + "_SB_Prep" #call R_SB_Prep
        elif Act == "fondle breasts":
                call expression Girl.Tag + "_FB_Prep" #call R_FB_Prep
        elif Act == "insert ass" or Act == "lick ass":
                call expression Girl.Tag + "_IA_Prep" #call R_IA_Prep
        else: #Act == "kiss you"
                call KissPrep(Girl) #call R_KissPrep                 
        return

#end quick sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start sex act escalation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Escalation(Girl=0):
        #call Escalation("Rogue","R")
        # raises the level of the sexual activity if the girl would like that. 
        if Cnt < 10 or ThreeCount <= Round:
                #if things just started, or you recently made a change, return
                return
                
        $ Situation = Girl
        
        if Trigger == "fondle breast" and ApprovalCheck(Girl,1050,TabM=4) and Girl.Lust >= 30 and Girl.SuckB:
                    #if you're fondling her breasts, she has over 30 Lust, and she's had her breasts sucked before. . .
                    call expression Girl.Tag + "_SB_Prep" #call Rogue_SB_Prep  
                    if "suck breasts" in Girl.RecentActions:
                            # If you went through with it, drop one phase back when returning to this point
                            $ renpy.pop_call()
        elif Trigger == "fondle thighs" and ApprovalCheck(Girl,1050,TabM=4) and Girl.Lust >= 30 and Girl.FondleP:
                    #if you're fondling her thighs, she has over 30 Lust, and she's had her pussy fondled before. . .
                    call expression Girl.Tag + "_FP_Prep" #call Rogue_FPlayer.Prep  
                    if "fondle pussy" in Girl.RecentActions:
                            # If you went through with it, drop one phase back when returning to this point
                            $ renpy.pop_call()
        elif Trigger == "handjob" and ApprovalCheck(Girl,1200,TabM=4) and Girl.Lust >= 30 and Girl.Blow:
                    #if she's giving a handy, she has over 30 Lust, and she's sucked cock before. . .
                    call expression Girl.Tag + "_BJ_Prep" #call Rogue_BJ_Prep  
                    if "blow" in Girl.RecentActions:
                            # If you went through with it, drop one phase back when returning to this point
                            $ renpy.pop_call()                  
        elif Trigger not in ("sex","anal") and ApprovalCheck(Girl,1400,TabM=5) and Girl.Lust >= 60 and Girl.Sex >= 3:
                    #if you're not having sex, she has over 60 Lust, and she's had sex before. . .
                    call expression Girl.Tag + "_SexPrep" #call Rogue_SexPrep  
                    if "sex" in Girl.RecentActions:
                            # If you went through with it, drop one phase back when returning to this point
                            $ renpy.pop_call()  
        elif Trigger != "anal" and ApprovalCheck(Girl,1400,TabM=5) and Girl.Lust >= 70 and Girl.Anal >= 5:
                    #if you're not having anal, she has over 70 Lust, and she's had anal before. . .
                    call expression Girl.Tag + "_AnalPrep" #call Rogue_AnalPrep  
                    if "anal" in Girl.RecentActions:
                            # If you went through with it, drop one phase back when returning to this point
                            $ renpy.pop_call() 
        
        #if it falls through the options
        $ ThreeCount = 0
        $ Situation = 0
        return
#end Escalation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start General sex stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
    
# Start Primary Sex Dialog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
label Sex_Dialog(Primary=Ch_Focus,Secondary=0,TempFocus=0,PrimaryLust=0,SecondaryLust=0,Line1=0,Line2=0,Line3=0,Line4=0,D20S=0): 
        # call Sex_Dialog(RogueX,Partner) 
        # Primary is main female, secondary is supporting female, action is what they are doing.
                
        # If the seed is 0-5, only offhands will play. If it's 15-20, only trigger3's will play. If it's 5-10, offhand and Secondaries will play.
        # If it's 10-15 all things will play. 
                 
        $ D20S = renpy.random.randint(1, 20) if not D20S else D20S
        $ Line = 0
        
        # Checks for Taboo, and if it passes through, calls the first sex dialog  
        if Taboo and Primary.Loc == bg_current:
            if (D20S + (int(Taboo/10)) - Stealth) >= 10:        
                    #If there is a Taboo level, and your modified roll is over 10
                    call Girls_Taboo(Primary)
        else:            
                    call Girls_Noticed(Primary)  
        if not Trigger:
                return
                    
        $ Secondary = Partner
        
        call Primary_SexDialog                    
        $ Line1 = Line #Set Line1 to the current state of the Line variable
        #End Primary Dialog
        
        #Trigger 2
        if Trigger2 and D20S <= 15:
                    # If there is a player offhand Trigger set and the random value is 1-15, add an Offhand dialog
                    $ Line = ""
                    call Offhand_Dialog                    
                    $ Line1 = Line1 + Line
        #End Offhand
        
        #Trigger 3
        if D20S >= 7 and Trigger not in ("masturbation", "lesbian"):
                    # If there is a Primary offhand Trigger set and the random value is 1-10, add a self-directed dialog
                    $ Line = 0
                    call Girl_Self_Lines(Primary,"T3",Trigger3) 
                    if Line:
                            $ Line3 = Line + "."
        #End Primary girl offhand
        
        #Trigger 4
        if Secondary and (not Trigger4 or 7 <= D20S <= 17 or Trigger4 == "watch"):
                    # If there is a Secondary character and the random value is 5-15, add a threeway dialog
                    $ Line = 0
                    call SexDialog_Threeway
                    if Line:
                            $ Line4 = Line + "."
        #End Secondary Dialog
        
        #Applying player's satisfaction
        $Player.Statup("Focus", 200, TempFocus)
        
        #Applying primary girl's satisfaction
        $ Primary.Statup("Lust", 200, PrimaryLust)         
        $ Primary.LustFace()      
        
        #Applying secondary girl's satisfaction      
        if Secondary:
                $ SecondaryLust += (int(PrimaryLust/10)) if Secondary.GirlLikeCheck(Primary) >= 700 else 0
                $ Secondary.Statup("Lust", 200, SecondaryLust)                 
                $ Secondary.LustFace()
                           
        # Dialog begins to play out. . . 
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
                    if ApprovalCheck(Primary,500,"I",TabM=2) and Primary.Lust >= 50 and (Primary.ChestNum() > 1 or Primary.OverNum() > 1):
                            # if the girl is horny and her top is on. . .
                            $ Primary.Uptop = 1
                            "[Primary.Name] seems frustrated and pulls her top open."   
               
        call Activity_Check(Primary,Secondary,0) 
        if not _return:
                #sees if girl is cool with what's happening, if not, removes her. 
                if Primary.Forced:
                        #if you're coercing her, it just reverts to the previous tier
                        $ renpy.pop_call() #negates call to Sex Dialog 
                        return
                if Secondary and Secondary.Loc == bg_current:
                        #if the first girl leaves, but there is another,  
                        $ Trigger = Secondary
                        $ Partner = 0
                        $ Trigger4 = 0
                        $ Trigger5 = 0
                        #$ renpy.pop_call() #negates call to Sex Dialog                   
                        #$ renpy.pop_call() #negates call to sexaction in progress        
                        #$ renpy.pop_call() #negates call to sex menu
                else:
                        call Trig_Reset
                jump Misplaced   #moved out of previous column 
                
        call Dirty_Talk 
                     
        return  
# End Primary Sex Dialog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  

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
        
# Start Trigger swap  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
label Trigger_Swap(Active = 0, TriggerX1 = Trigger, TriggerX3 = Trigger3, Primary = Partner):
    #this would switch primary character triggers over to secondary characters.
    # call Trigger_Swap("Rogue") 
    # TriggerX1 and TriggerX3 store the primary girl's actions
    # Active is the old lead girl
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
    if not Active:
            if RogueX.Loc == bg_current and Primary != RogueX:
                    $ Partner = RogueX
            elif KittyX.Loc == bg_current and Primary != KittyX:
                    $ Partner = KittyX
            elif EmmaX.Loc == bg_current and Primary != EmmaX:
                    $ Partner = EmmaX
            elif LauraX.Loc == bg_current and Primary != LauraX:
                    $ Partner = LauraX
    else:
                    $ Partner = Active
        
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
                        "You pull back from [Partner.Name]."
                elif TriggerX1 in ("dildo pussy","dildo anal"):
                        $ Trigger5 = TriggerX1
                        "You pull back from [Partner.Name]."
                elif TriggerX1 in ("titjob","hotdog","fondle breasts","suck breasts"):
                        $ Trigger5 = "fondle breasts"
                        "You pull back from [Partner.Name]."
                elif TriggerX1 in ("fondle pussy","lick pussy"):
                        $ Trigger5 = "fondle pussy"
                        "You pull back from [Partner.Name]."
                elif TriggerX1 == "sex":
                        $ Trigger5 = "fondle pussy"
                        "You pull out of [Partner.Name] and shift your attention to [Primary.Name]."
                elif TriggerX1 == "anal":
                        $ Trigger5 = "fondle ass"
                        "You pull out of [Partner.Name] and shift your attention to [Primary.Name]."                
                else:                          
                        $ Trigger5 = 0  
    call AllReset(Partner)
            
#    $ renpy.pop_call() #causes it to skip past the cycle you were in before
#    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
    #popcall doesn't work here because it deletes the called variables.
    if not Trigger:                 
#            call Set_The_Scene(Dress = 0, TrigReset = 0, Quiet=1)
#            "What would you like her to do?"
            if Primary == RogueX:
                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
                    jump Rogue_SMenu
            if Primary == KittyX:
                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
                    jump Kitty_SMenu
            if Primary == EmmaX:
                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
                    jump Emma_SMenu
            if Primary == LauraX:
                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
                    jump Laura_SMenu
    else:
                    call Set_The_Scene(Dress = 0, TrigReset = 0, Quiet=1)
                    call expression Primary.Tag + "_SexAct" pass ("SkipTo") #call Kitty_SexAct("SkipTo")
    return
# End Trigger swap  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  

#Start Activity Checker  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
label Activity_Check(Girl=0,Girl2=0,Silent=0,Removal=1,ClothesCheck=1,Mod=0,Approval=1,Tempshame=0,TabooM=1):
        # This checks whether a girl is up for watching a given activity
        # Silent is whether it plays dialog or not, Removal is whether it auto-removes the girl on a fail,
        # ClothesCheck is whether it bothers checking clothing, 2 if skip first girl
        # Mod gets set to her Like stat -600, so 600 Like, you break even, otherwise it's a penalty
        # call Activity_Check("Rogue",0,1,0)
              
        if Girl == Girl2:
            "Tell oni that the activity check failed after [Trigger]."
            $ Girl.NotAStat = 5
            
        #if they don't know you're there, they don't run
        if "unseen" in Girl.RecentActions or "classcaught" in Girl.RecentActions:
                    return 2
                    
        $ Mod += 200 if Girl.Forced else 0             #bonus if in the Forced state
        $ Mod += (Girl.Lust*5) if Girl.Lust >= 50 else 0  #bonus if high lust (50 = +250, 75= +375, 90 = +450)              
        
        if Girl2 and ClothesCheck != 2:
                #if there is a second girl and it's not told to skip it
                $ Mod = int(Mod/2) if Mod > 0 else Mod 
                #halves the benefits from the above mechanisms
                $ Mod = (Girl.GirlLikeCheck(Girl2)-600)
                # if 500 = -100, if 700 = +100 if 900 = +300
                if Girl in Player.Harem and Girl2 in Player.Harem: #bonus for if both in harem
                        $ Mod += 500
                    
        if ClothesCheck and Girl2:
                #sets her shame level to be accurate to current look
                #call expression Girl2.Tag + "_OutfitShame" pass (20)
                call OutfitShame(Girl2,20)
                $ Tempshame = Girl2.Shame
                             
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
                else:
                                $ Approval = 0        
                
        if "exhibitionist" in Girl.Traits or ApprovalCheck(Girl,900,"I"):
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
            $ Girl.FaceChange("sadside",1)
            if Girl == RogueX:
                    if Girl2:
                        ch_r "I don't know, with [Girl2.Name] here and all."
                    ch_r "Ain't none a this right, [Girl.Petname]."
            elif Girl == KittyX:
                    if Girl2:
                        ch_k "I don't know, with [Girl2.Name] being here."
                    ch_k "I'm[KittyX.like]not really comfortable with this?"
            elif Girl == EmmaX:
                    if Girl2:
                        ch_e "I'm unsure that I'm comfortable doing this with [Girl2.Name] here."
                    ch_e "This has become a bit too. . . scandalous for my tastes."
            elif Girl == LauraX:
                    if Girl2:
                        ch_l "[Girl2.Name]'s weirding me out."
                    else:
                        ch_l "This is getting weird."
                    ch_l "I'll see you later."
        
        if Removal and not Approval and not Girl.Forced:
                call Remove_Girl(Girl,2)  
                "[Girl.Name] takes off."
                
        return Approval
#end Activity Checker  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  

# Start First Seen Peen / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label Seen_First_Peen(Primary=0, Secondary=0, Silent=0, Undress=0, Passive=0, GirlsNum=0, React=0, BOptions=[]):
    # call Seen_First_Peen(Primary,Secondary,Silent,Undress)
    # Primary is the first girl, Secondary the second, if there is one    
    # _return will be 0 if other girl didn't comment, 
    # 1 = if the other girl commented, 2 = didn't like it
    # Girlsnum will pass Second to the next girl, and keep track of whether anyone acted
    # Passive will be 3 or 4 if linked to Sex dialog acts 3 or 4
    if not Primary:
            #if this is not during a sex act            
            $ BOptions = Present[:]  #loads up all local girls               
            $ renpy.random.shuffle(BOptions)
            while BOptions:        
                    #cycles through each girl possible,
                    #If girl is around, check to see if she noticed your cock yet
                    if (Ch_Focus == BOptions[0] or D20 >= 10) and "peen" not in BOptions[0].RecentActions:
                            #If BOptions[0] is the prinary or secondary character, and hasn't seen your cock yet, call the thing 
                            #call expression BOptions[0].Tag + "_First_Peen" pass (Silent,Undress)
                            call Girl_First_Peen(BOptions[0],Silent,Undress)
                            $ GirlsNum = _return   
                    $ BOptions.remove(BOptions[0])
            
            if not GirlsNum:
                #if no girls are present   
                if "naked" not in Player.RecentActions and Undress:
                        "You strip nude."      
                        $ Player.AddWord(1,"naked",0,0,0)
                elif "cockout" in Player.RecentActions:
                        return
                else:
                        "You whip your cock out."         
                $ Player.AddWord(1,"cockout",0,0,0)
    #end if not during a sex act  
    else:
            #It's during a sex act
            if Passive:
                    #if in Passive mode, during sex dialog, it only activates if cock is already out.
                    if Approval == Passive and "cockout" not in Player.RecentActions:
                        #if both are 3 or both are 4, meaning the activities matched up, 
                        call CockOut
                    if "cockout" not in Player.RecentActions:
                        return
                    
            #call expression Primary.Tag + "_First_Peen" pass (Silent,Undress,React=React)
            call Girl_First_Peen(Primary,Silent,Undress,React=React)
            
            if Secondary: 
                    #call expression Secondary.Tag + "_First_Peen" pass (Silent,Undress,Second = _return)
                    call Girl_First_Peen(Secondary,Silent,Undress,Second = _return)
    return
    
label CockOut:       
        # Passive and therefore Approval will be 3 or 4 if linked to Sex dialog acts 3 or 4 
        if Approval == 3:      
                    #if attached to line 3, use the Primary girl
                    #call expression Primary.Tag + "_First_Peen" pass (React=1)   
                    call Girl_First_Peen(Primary,React=1)
        elif Approval == 4:
                    #if attached to line 4, use the Secondary girl
                    #call expression Secondary.Tag + "_First_Peen" pass (React=1)  
                    call Girl_First_Peen(Secondary,React=1)
        $ Approval = 0
        return
    
label Get_Dressed: #checked each time she sees your cock
        #if no girls are present
        if "naked" in Player.RecentActions:   
                "You get dressed."
                $ Player.DrainWord("naked") 
                $ Player.DrainWord("cockout") 
        elif "cockout" in Player.RecentActions:                 
                "You put your cock away."
                $ Player.DrainWord("cockout") 
        return
        
# End First Seen Peen / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  


# Start Seen Peen / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_First_Peen(Girl = 0, Silent = 0, Undress = 0, Second = 0, React = 0): 
        #checked each time she sees your cock  ## call Girl_First_Peen(RogueX,0,1)
        #if Silent it doesn't say anything
        #if Undress then you get nude
        #if Secondary then this is the second girl to see it.
        # React 0 if other girl didn't comment, 
        # 1 = if the other girl commented, 2 = didn't like it
        
        if Girl.Loc != bg_current:
                    if Partner == Girl:
                            $ Partner = 0
                    return
        if "cockout" in Player.RecentActions and "peen" in Girl.RecentActions: 
                    #If the cock is already out and she's seen it, return
                    return
                
        $ Girl.RecentActions.append("peen")                      
        $ Girl.DailyActions.append("peen")
        $ Girl.SeenPeen += 1                      
        $ Girl.Statup("Inbt", 30, 2) 
        $ Girl.Statup("Inbt", 80, 1)
        
        if Second:
                #If another girl commented on it first. . .
                if Girl.SeenPeen == 1: 
                                $ Girl.FaceChange("surprised", 2)  
                                if Girl == RogueX: 
                                        ch_r "Wow, yeah, that's pretty nice. . ."
                                elif Girl == KittyX:    
                                        ch_k "Oh, wow, you aren't kidding. . ."               
                                elif Girl == EmmaX:      
                                        $ Girl.FaceChange("smirk", 2, Eyes = "down")  
                                        ch_e "My, that certainly is an impressive specimen. . ."            
                                elif Girl == LauraX:
                                        $ Girl.FaceChange("smirk", 2, Eyes = "down")  
                                        ch_l "Huh, that's a pretty good one you got there. . ."
                                $ Girl.FaceChange("bemused", 1)  
                elif Second == 1:
                        # The other girl liked it
                        if not ApprovalCheck(Girl, 800) and not ApprovalCheck(Girl, 500, "I"):
                                $ Girl.FaceChange("sad", 1) 
                                if Girl == RogueX: 
                                        ch_r "If you're inta that sorta thing. . ."
                                elif Girl == KittyX:       
                                        ch_k "I mean I guess. . ."            
                                elif Girl == EmmaX:      
                                        ch_e "I suppose you haven't had a lot of experience. . ."            
                                elif Girl == LauraX:
                                        ch_l "I guess . ."
                        else:
                                $ Girl.FaceChange("bemused", 1)  
                                if Girl == RogueX: 
                                        ch_r "Yeah, it really is a beauty. . ."
                                elif Girl == KittyX: 
                                        ch_k "I know, right?!"                 
                                elif Girl == EmmaX:   
                                        ch_e "Yes, it caught me off guard as well. . ."               
                                elif Girl == LauraX:
                                        ch_l "Yeah, nice, isn't it. . ."
                elif Second == 2:
                        # The other girl didn't like it
                        if not ApprovalCheck(Girl, 800) and not ApprovalCheck(Girl, 500, "I"):
                                $ Girl.FaceChange("sad", 1)  
                                if Girl == RogueX: 
                                        ch_r "Right, whatever. . ."
                                elif Girl == KittyX:        
                                        ch_k "So over it. . ."           
                                elif Girl == EmmaX:     
                                        ch_e "A fine judge of quality. . ."             
                                elif Girl == LauraX:
                                        ch_l "I guess. . ."
                        else:
                                $ Girl.FaceChange("confused", 1)  
                                if Girl == RogueX: 
                                        ch_r "Well I liked it. . ."
                                        $ Girl.FaceChange("sexy", 1)  
                                elif Girl == KittyX:  
                                        ch_k "Come on, it's really cute!"
                                        $ Girl.FaceChange("smile", 1)                   
                                elif Girl == EmmaX:      
                                        ch_e "You just don't appreciate the finer things. . ."
                                        $ Girl.FaceChange("sly",0)               
                                elif Girl == LauraX:
                                        ch_l "Aw, come on, it's not that bad. . ."
                                        $ Girl.FaceChange("sly",0)  
                $ Silent = 1
                            
        if Undress:
            $ Player.AddWord(1,"naked")    
        if not Silent:
            if "cockout" in Player.RecentActions:
                    $ Girl.FaceChange("down", 2)  
                    "[Girl.Name] glances down at your exposed cock"
            elif React:
                    #If called by a sex dialog      
                    "[Girl.Name] reaches for your pants and pulls out your cock."
            elif Undress:
                    "You strip nude."
            else:
                    "You whip your cock out."
            $ Player.AddWord(1,"cockout") 
            if not Girl.Forced and not React and bg_current != "bg showerroom" and not ApprovalCheck(Girl, 800) and not ApprovalCheck(Girl, 500, "I"):
                    if Girl == EmmaX and "detention" in Girl.RecentActions or "classcaught" in Girl.RecentActions:  
                        #special exceptions for detention and classcaught events
                        $ Girl.FaceChange("confused", Eyes="down")  
                        ch_e "Mmm?"                    
                        $ Girl.FaceChange("surprised", Eyes="squint") 
                        if Girl.SeenPeen == 1: 
                                $ Girl.Statup("Love", 30, 10) 
                                $ Girl.Statup("Love", 90, 5)                
                                $ Girl.Statup("Obed", 50, 20)
                                $ Girl.Statup("Inbt", 60, 30)
                        else:                         
                                $ Girl.Statup("Love", 90, 2)                
                                $ Girl.Statup("Obed", 50, 3)
                                $ Girl.Statup("Inbt", 60, 5) 
                        ch_e "Well I suppose I can make an exception in this case."
                        $ React = 1 
                    else:
                        $ Girl.FaceChange("surprised", 2) 
                        if Girl == RogueX: 
                                ch_r "What the hell?"
                        elif Girl == KittyX:  
                                ch_k "Huh?!"                  
                        elif Girl == EmmaX:   
                                $ Girl.Eyes = "down"
                                ch_e "Mmm?"               
                        elif Girl == LauraX:
                                $ Girl.Eyes = "down"
                                ch_l "Mmm?"
                        $ Girl.FaceChange("angry", 1)  
                        $ Girl.RecentActions.append("angry")
                        $ Girl.DailyActions.append("angry")  
                        $ React = 2
                        if Girl.SeenPeen == 1: 
                                    $ Girl.Statup("Love", 90, -20)                
                                    $ Girl.Statup("Obed", 50, 30)
                                    $ Girl.Statup("Inbt", 60, 20)
                        else:       
                            #if this is the second time you've done this today. . .
                            if Girl == RogueX: 
                                    ch_r "What is {i}wrong{/i} with you?"
                            elif Girl == KittyX:               
                                    ch_k "Dude, seriously, you've got a problem!"    
                            elif Girl == EmmaX:           
                                    ch_e "[Girl.Petname]! We are going to have to work through this. . . problem of yours."       
                            elif Girl == LauraX:
                                    ch_l "Dude, not cool."
                            if Girl.DailyActions.count("peen") >= 2:
                                    #if she's seen more than one peen today         
                                    $ Girl.Statup("Love", 90, -1)     
                                    $ Girl.Statup("Obed", 50, 1)
                                    $ Girl.Statup("Inbt", 60, 2)
                            else:
                                    $ Girl.Statup("Love", 90, -5)                
                                    $ Girl.Statup("Obed", 50, 10)
                                    $ Girl.Statup("Inbt", 60, 10)  
            elif not Girl.Forced and not React and Taboo > 20 and (not ApprovalCheck(Girl, 1500) or Girl.SEXP < 10) and bg_current != "bg showerroom":
                        #if it's a semi-public space that isn't the showers, and she is not down with this. . .
                        $ Girl.FaceChange("surprised", 2)                     
                        if Girl == RogueX: 
                                ch_r "What are you- you should really put that thing away!"
                        elif Girl == KittyX:        
                                ch_k "Um, you should[Girl.like]put that away in public."           
                        elif Girl == EmmaX:     
                                ch_e "You really should be careful where you display that thing."              
                        elif Girl == LauraX:
                                ch_l "I think there's a time and place for that sort of thing." 
                        $ Girl.FaceChange("bemused", 1)  
                        if Girl.SeenPeen == 1: 
                                if Girl == RogueX: 
                                        ch_r "I mean. . . no, definitely put that away!"
                                elif Girl == KittyX:   
                                        ch_k "Or[Girl.like]maybe. . ."                
                                elif Girl == EmmaX:  
                                        $ Girl.Eyes = "down"     
                                        ch_e ". . . impressive though it may be. . ."           
                                elif Girl == LauraX:
                                        ch_l ". . . not that I mind, myself. . ." 
                                $ Girl.Statup("Love", 90, 20)                
                                $ Girl.Statup("Obed", 50, 20)
                                $ Girl.Statup("Inbt", 60, 30)  
                        $ React = 2
            elif Girl.SeenPeen > 10:
                        #if it's been more than 10 times, return
                        return 0   
            elif ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "L"):
                    $ Girl.FaceChange("sly",1) 
                    if Girl.SeenPeen == 1: 
                            $ Girl.FaceChange("surprised",2)  
                            if Girl == RogueX: 
                                    ch_r "Whoa, I didn't know they looked so big up close."
                                    $ Girl.FaceChange("bemused",1)  
                                    $ Girl.Statup("Love", 90, 5) 
                            elif Girl == KittyX:   
                                    $ Girl.FaceChange("surprised",2)  
                                    ch_k "That's. . . impressive."
                                    $ Girl.FaceChange("bemused",1)  
                                    $ Girl.Statup("Love", 90, 3)                  
                            elif Girl == EmmaX:      
                                    $ Girl.FaceChange("surprised",1, Eyes="down")  
                                    ch_e "Well that's certainly an interesting specimen."
                                    $ Girl.FaceChange("bemused",1)  
                                    $ Girl.Statup("Love", 50, 5) 
                                    $ Girl.Statup("Love", 90, 10)             
                            elif Girl == LauraX:
                                    $ Girl.FaceChange("surprised",1, Eyes="down")  
                                    ch_l "Huh, that's a pretty good one you got there. . ."
                                    $ Girl.FaceChange("bemused",1)  
                                    $ Girl.Statup("Love", 50, 5) 
                                    $ Girl.Statup("Love", 90, 10)    
                    elif Girl.SeenPeen == 2:  
                            if Girl == RogueX: 
                                    ch_r "That thing sure is impressive." 
                                    $ Girl.Statup("Obed", 50, 5) 
                            elif Girl == KittyX:    
                                    ch_k "I can't get over that."  
                                    $ Girl.Statup("Obed", 50, 7)                      
                            elif Girl == EmmaX: 
                                    $ Girl.Eyes = "down"
                                    ch_e "Oh, hello again."     
                                    $ Girl.Statup("Inbt", 50, 5)                       
                            elif Girl == LauraX:
                                    $ Girl.Eyes = "down"
                                    ch_l "Oh, there it is."     
                                    $ Girl.Statup("Obed", 50, 2)  
                                    $ Girl.Statup("Inbt", 50, 3)          
                    elif Girl.SeenPeen == 5:   
                            if Girl == RogueX: 
                                    ch_r "I certainly appreciate that guy."
                                    $ Girl.Statup("Inbt", 60, 5)  
                            elif Girl == KittyX: 
                                    ch_k "There it is."    
                                    $ Girl.Statup("Inbt", 60, 5)                
                            elif Girl == EmmaX:  
                                    ch_e "Yes, we've seen that before." 
                                    $ Girl.Statup("Obed", 60, 7)                  
                            elif Girl == LauraX:
                                    ch_l "Yeah, I've seen that one." 
                                    $ Girl.Statup("Obed", 60, 4)  
                                    $ Girl.Statup("Inbt", 60, 3) 
                    elif Girl.SeenPeen == 10: 
                            if Girl == RogueX: 
                                    ch_r "I never get tired of seeing that."
                                    $ Girl.Statup("Love", 90, 10)
                            elif Girl == KittyX:  
                                    ch_k "So beautiful."
                                    $ Girl.Statup("Obed", 80, 10)
                                    $ Girl.Statup("Inbt", 60, 3)                
                            elif Girl == EmmaX:     
                                    $ Girl.Eyes = "down"
                                    ch_e "I do appreciate some of your features."
                                    $ Girl.Statup("Obed", 80, 5)
                                    $ Girl.Statup("Inbt", 60, 10)    
                            elif Girl == LauraX:
                                    $ Girl.Eyes = "down"
                                    ch_l "I don't get tired of that view."
                                    $ Girl.Statup("Obed", 80, 8)
                                    $ Girl.Statup("Inbt", 60, 7) 
                    $ React = 1
            else:
                    $ Girl.FaceChange("sad",1) 
                    if Girl.SeenPeen == 1: 
                            $ Girl.FaceChange("perplexed",1 )
                            if Girl == RogueX: 
                                    ch_r "Well, I guess that's impressive. What do you plan to do with it?"
                                    $ Girl.Statup("Obed", 50, 5)
                                    $ Girl.Statup("Inbt", 60, 5)  
                            elif Girl == KittyX:       
                                    ch_k "Well that happened. . ."           
                            elif Girl == EmmaX:            
                                    ch_e "Are you aware that your dick is out?"
                                    $ Girl.Statup("Obed", 50, 2)
                            elif Girl == LauraX:
                                    ch_l "Your dick is out."
                                    $ Girl.Statup("Inbt", 60, 2)   
                            $ Girl.Statup("Obed", 50, 5)
                            $ Girl.Statup("Inbt", 60, 5)  
                    elif Girl.SeenPeen < 5: 
                            $ Girl.FaceChange("sad",0) 
                            if Girl == RogueX: 
                                    ch_r "Yeah, I've seen it." 
                            elif Girl == KittyX:       
                                    ch_k "Huh."            
                            elif Girl == EmmaX:         
                                    ch_e "You might want to put that away, [Girl.Petname]."
                            elif Girl == LauraX:
                                    ch_l "Hey. . ."
                                    ch_l "You might want to put that away, [Girl.Petname]."
                            $ Girl.Statup("Inbt", 60, 2) 
                    elif Girl.SeenPeen == 10: 
                            if Girl == RogueX:                    
                                    ch_r "I'm getting tired of seeing that."  
                                    $ Girl.Statup("Obed", 50, 5)
                                    $ Girl.Statup("Inbt", 60, 5)  
                            elif Girl == KittyX:    
                                    ch_k "[Girl.Like]put that away."       
                                    $ Girl.Statup("Obed", 50, 7)
                                    $ Girl.Statup("Inbt", 60, 3)                
                            elif Girl == EmmaX:   
                                    ch_e "Yes, we've all seen that before." 
                                    $ Girl.Statup("Obed", 50, 7)
                                    $ Girl.Statup("Inbt", 60, 5)                  
                            elif Girl == LauraX:
                                    ch_l "Yeah, yeah, waving your cock around again." 
                                    $ Girl.Statup("Obed", 50, 8)
                                    $ Girl.Statup("Inbt", 60, 4)  
                    $ React = 2
        else: #Silent mode
                    $ Player.RecentActions.append("cockout") 
                    if Girl.SeenPeen > 10:
                        return
                    elif ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "L"):
                            if Girl.SeenPeen == 1: 
                                $ Girl.Statup("Love", 90, 5) 
                            elif Girl.SeenPeen == 2:              
                                $ Girl.Statup("Obed", 50, 5) 
                            elif Girl.SeenPeen == 5: 
                                $ Girl.Statup("Inbt", 60, 5)  
                            elif Girl.SeenPeen == 10: 
                                $ Girl.Statup("Love", 90, 10)  
                    else:
                            if Girl.SeenPeen == 1: 
                                $ Girl.Statup("Obed", 50, 5)
                                $ Girl.Statup("Inbt", 60, 5) 
                                $ Girl.AddWord(1,0,0,0,"seenpeen") #$ Girl.History.append("seenpeen")  
                            elif Girl.SeenPeen < 5: 
                                $ Girl.Statup("Inbt", 60, 2)  
                            elif Girl.SeenPeen == 10:              
                                $ Girl.Statup("Obed", 50, 5)
                                $ Girl.Statup("Inbt", 60, 5) 
        if Girl.SeenPeen == 1:            
                $ Girl.Statup("Love", 90, 15)                
                $ Girl.Statup("Obed", 90, 20)
                $ Girl.Statup("Inbt", 60, 20) 
                $ Girl.Statup("Lust", 200, 5)
        $ Girl.FaceChange("sly",1)  
        return React
        
# End Seen Peen / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start public sex check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girls_Taboo(Girl=0,Cnt= 1,Choice=0,D20=0):  #nee  Rogue_Taboo(Cnt= 1,Choice=0)
        #Called by Sex_Dialog
        #Girl is the Primary actor, Cnt is a count of how many times you've been spotted,
        #Choice is how the girl is reacting, D20 is a randomizer
        
        if Girl not in TotalGirls:
                $ Girl = Ch_Focus
        $ Player.AddWord(1,0,Girl.Tag) #$ Player.DailyActions.append(Girl.Tag) 
        $ Player.AddWord(1,0,"scent") #$ Player.DailyActions.append("scent") Allows Laura to track you.
                
        $ Cnt = Girl.RecentActions.count("spotted") if "spotted" in Girl.RecentActions else 1
        $ Cnt = 4 if Cnt > 4 else Cnt   
        
        $ D20 = renpy.random.randint(1, 20)     
        if D20 < 10:    
                #if you're at the point where the girls would notice you. . .    
                if Taboo > 20:
                        if (Trigger == "kiss you" and not Trigger2 and not Trigger3):
                                #if it's very innocent, skip this part
                                pass
                        elif Girl not in Rules:
                                #if Xavier is looking. . .
                                $ Girl.FaceChange("surprised", 1)
                                if Trigger == "blow" or Trigger == "hand" or Trigger == "titjob":
                                        "[Girl.Name] stops what she's doing with a startled look."                
                                else:
                                        "You feel a slight buzzing in your head and stop what you're doing."
                                ch_x "Cease that behavior at once! Come to my office immediately!" 
                                call AllReset(Girl)
                                call Girls_Caught(Girl) #Rogue_Caught
                                return
                        else:
                                #if you've disabled Xavier's looking
                                ch_x "Hmmm. . ."
                                $ Girl.Statup("Inbt", 90, 2) 
                                $ Girl.Statup("Lust", 200, 3) 
                if bg_current == "bg classroom" and EmmaX.Loc == "bg teacher" and Girl != EmmaX:
                                #If you're in class and Emma's there as a teacher. . .
                                call Emma_Teacher_Caught(Girl)
                elif D20 < 3 and AloneCheck(Girl) and Current_Time != "Night":
                                #bad luck, a girl showed up out of nowhere. . .
                                $ Choice = ActiveGirls[:]
                                $ Choice.remove(Girl)
                                $ renpy.random.shuffle(Choice)
                                while Choice:                     
                                        if Choice[0].Loc != bg_current:
                                                $ Trigger5 = Choice[0]
                                                $ Choice = [1]
                                        $ Choice.remove(Choice[0])
                                if Trigger5:
                                        call Locked_Door(Trigger5,1)
                                # either this new girl will be allowed in and stay, or she will run away
                                $ Choice = 0
                                $ Trigger5 = 0
                    
                    
                #now the girls get their turn to notice. . .
                call Girls_Noticed(Girl)
                
        if Taboo <= 20:
                #This is a private space with others around.
                call Girls_Noticed(Girl)
                return
        elif Cnt < 4:                                                       
                #if this has happened less than 4 times within the current cycle of events
                
                if Girl == EmmaX and "public" not in EmmaX.History:
                        $ EmmaX.History.append("public")
                
                if "spotted" not in Girl.RecentActions:
                        "Some of the other students notice you and [Girl.Name]."
                        $ Girl.Statup("Inbt", 200, 2)               
                        $ Girl.Rep -= 2                      
                        $ Player.Rep -= 2                       
                elif Cnt < 3:
                        "A few more students notice you and [Girl.Name]."   
                        $ Girl.Statup("Inbt", 200, 2)               
                        $ Girl.Rep -= 1                    
                        $ Player.Rep -= 1  
                elif Cnt == 3:
                        "You've got quite an audience."               
                        $ Girl.Statup("Inbt", 200, 3)                
                        $ Girl.Rep -= 1                    
                        $ Player.Rep -= 1
                    
                if "exhibitionist" in Girl.Traits:                
                        $ Girl.FaceChange("sexy", 0)                     
                        if "spotted" not in Girl.RecentActions:
                                if Girl == RogueX:
                                        ch_r "Let'em watch, [Girl.Petname]."
                                elif Girl == KittyX:
                                        ch_k "I think we can give'em a show, [Girl.Petname]." 
                                elif Girl == EmmaX:
                                        ch_e "Hmm, perhaps they can learn a few things, [Girl.Petname]." 
                                elif Girl == LauraX:
                                        ch_l "Well, let's give'em what they want."
                        $ Girl.Statup("Lust", 200, 4) 
                        $ Choice = "A"
                elif ApprovalCheck(Girl, 650, "I", TabM=Cnt):            
                        #not an exhibitionist but very uninhibited       
                        $ Girl.FaceChange("sexy", 1, Brows="sad")       
                        if "spotted" not in Girl.RecentActions:     
                                if Girl == RogueX:
                                        ch_r "Hmm, what should we do about this, [Girl.Petname]?" 
                                elif Girl == KittyX:                                                                                
                                        ch_k "What should we do?"   
                                elif Girl == EmmaX:
                                        ch_e "Well, this is something of a situation." 
                                elif Girl == LauraX:                                                       
                                        ch_l "How do you want to play this?"      
                        $ Girl.Statup("Lust", 200, 3)   
                        $ Choice = "B"
                elif ApprovalCheck(Girl, 1000, "OI", TabM=Cnt):     
                        #not an exhibitionist but obedient/uninhibited          
                        $ Girl.FaceChange("surprised", 2)
                        if Girl == EmmaX:
                                "[Girl.Name] looks a bit concerned."
                        elif Girl == LauraX:
                                "[Girl.Name] looks a bit uncomfortable."
                        else:
                                "[Girl.Name] looks a bit panicked."
                        $ Girl.Statup("Lust", 200, 3)
                        $ Choice = "C"
                else:  
                        # She fails her inhibition checks
                        $ Girl.FaceChange("surprised", 2)
                        if "spotted" not in Girl.RecentActions:    
                                if Girl == KittyX:
                                        "[Girl.Name] bolts up with an embarassed look. She grabs her clothes and flings herself through the nearest wall."  
                                elif Girl == EmmaX:
                                        "[Girl.Name] bolts up with an embarassed look. She grabs her clothes and stalks off."  
                                else:
                                        "[Girl.Name] bolts up with an embarassed look. She runs off while putting her clothes back on."  
                                $ Girl.Rep -= 3 if Girl.Rep >= 30 else Girl.Rep            
                        else:
                                if Girl == KittyX:
                                        $ Girl.Statup("Love", 90, -15)  
                                        "With a sudden embarrassed start, [Girl.Name] panics. She dives through the nearest wall."
                                elif Girl == EmmaX:
                                        $ Girl.Statup("Love", 90, -15)  
                                        "With a sudden embarrassed start, [Girl.Name] stop what she's doing. She grabs her clothes and stalks off."
                                else:
                                        "With a sudden embarrassed start, [Girl.Name] panics. She takes off while throwing her clothes together."
                        "You head back to your room."                    
                        $ Choice = "stop"
                    
                if Choice != "stop":
                    menu:
                        "What would you like to do?"
                        "Let them watch. . ." if "spotted" not in Girl.RecentActions:   
                            if Choice == "A":                
                                    $ Girl.FaceChange("sexy", 0)                                     
                                    if Girl == RogueX:
                                            ch_r "That's what I'm talking about."
                                    elif Girl == KittyX:
                                            ch_k "I'll bring my \"A\" game." 
                                    elif Girl == EmmaX:   
                                            ch_e "It's only fair."       
                                    elif Girl == LauraX:
                                            ch_l "I can handle that."   
                            elif Choice == "B":            
                                    #not an exhibitionist but very uninhibited       
                                    $ Girl.FaceChange("sexy", 1,Brows="sad")
                                    if Girl == RogueX:
                                            ch_r "Uh, ok."       
                                    elif Girl == KittyX:  
                                            ch_k "Hehe, um, yeah."    
                                    elif Girl == EmmaX:
                                            ch_e "I do suppose we can show them how it's done."    
                                    elif Girl == LauraX:                                    
                                            ch_l "Ok."                                    
                            elif Choice == "C":     
                                    $ Girl.FaceChange("sexy",2)
                                    if Girl.Obed > Girl.Inbt:
                                        $ Girl.Eyes = "side"
                                        if Girl == RogueX:
                                                ch_r "If you say so, [Girl.Petname]."  
                                        elif Girl == KittyX:                                      
                                                ch_k "If you insist, [KittyX.Petname]." 
                                        elif Girl == EmmaX:                                       
                                                ch_e "I won't back down if you won't, [EmmaX.Petname]."
                                        elif Girl == LauraX:
                                                ch_l "I guess."
                                    else:          
                                        $ Girl.Mouth = "smile"
                                        $ Girl.Brows = "sad"
                                        if Girl == RogueX:
                                                ch_r "Uh, I guess. . ." 
                                        elif Girl == KittyX:
                                                ch_k "Yeah[KittyX.like]sure. . ."
                                        elif Girl == EmmaX:
                                                ch_e "Not that I mind, of course."  
                                        elif Girl == LauraX:   
                                                ch_l "Whatever. . ." 
                                    $ Girl.Statup("Obed", 200, 5)                       
                            "You get back to it." 
                            $ Girl.Blush = 1
                        "Continue" if "spotted" in Girl.RecentActions:
                            if Choice == "C":          
                                    $ Girl.Statup("Obed", 200, 4) 
                        "Ok, let's stop.":   
                            if Choice == "A":                            
                                    $ Girl.FaceChange("sad")
                                    if Girl == KittyX:
                                            ch_k "Booo."   
                                    elif Girl == LauraX:
                                            ch_l "Sissy."
                                    else:
                                            call AnyLine(Girl,"Spoilsport.")                                       
                            elif Choice == "B":            
                                    $ Girl.FaceChange("sad")
                                    if Girl == RogueX:
                                            ch_r "Yeah, probably." 
                                    elif Girl == KittyX:
                                            ch_k "Um, yeah."  
                                    elif Girl == EmmaX:
                                            ch_e "I suppose." 
                                    elif Girl == LauraX:
                                            ch_l "Probably a good call." 
                            elif Choice == "C":     
                                    $ Girl.Statup("Love", 90, 5)          
                                    $ Girl.FaceChange("smile")                                       
                                    if Girl == RogueX:
                                            ch_r "Heh, thanks [Girl.Petname]" 
                                    elif Girl == KittyX:
                                            ch_k "Heh, thanks [Girl.Petname]." 
                                            $ Girl.Statup("Love", 90, 5)   
                                    elif Girl == EmmaX:
                                            ch_e "That probably would be for the best. . ." 
                                    elif Girl == LauraX:
                                            ch_l "Yeah, thanks." 
                                            $ Girl.Statup("Love", 90, 5)  
                            "You both run back to your rooms."
                            $ Choice = "stop"
                            
                if Choice == "stop":            
                            $ Girl.RecentActions.append("caught")
                            $ Girl.DailyActions.append("caught")         
                            show blackscreen onlayer black 
                            call AllReset(Girl)
                            call Remove_Girl(Girl)
                            $ Girl.OutfitChange(Changed=0)
                            hide blackscreen onlayer black 
                            $ renpy.pop_call()          
                            $ renpy.pop_call()       
                            $ renpy.pop_call()                    
                            jump Player_Room             
        elif "exhibitionist" not in Girl.Traits:     
                            $ Girl.FaceChange("sly")   
                            $ Girl.Traits.append("exhibitionist") 
                            "[Girl.Name] seems to have become something of an exhibitionist."
        elif D20 > 15:
                            $ Girl.FaceChange("sexy")
                            "The crowd cheers."
            
        $ Girl.RecentActions.append("spotted") if Cnt < 4 else Girl.RecentActions
        $ Girl.DailyActions.append("spotted")  if "spotted" not in Girl.DailyActions else Girl.DailyActions
        return
    
# end public sex check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    

# Start girls noticed / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girls_Noticed(Girl=Primary,Other=0,Silent=0,B=0,BO=[]):
        # Called by Sex_Dialog or Girls_Taboo
        # Girl is lead girl, Other is a girl who notices you
        # if Silent, no dialog plays, B is a carried bonus value.
        if not Girl or Girl not in TotalGirls:
                        "Tell Oni that in noticed, no primary is set."
                        return
        $ BO = TotalGirls[:]  
        $ BO.remove(Girl)              
        while BO: 
                if BO[0].Loc == bg_current:
                        # if there is a girl who is not primary, but is in the location
                        # set her as the one being noticed by the primary girl
                        $ Other = BO[0]
                        $ BO = [1]
                $ BO.remove(BO[0])        
        if Other not in TotalGirls or Other == Girl:
                return
        if "threesome" in Other.RecentActions:
                return
        if Partner == Other and "noticed " + Girl.Tag in Other.RecentActions:
                return
                
        if not Silent:
            if Partner != Other:
                    #if there has been no connection yet. . .
                    $ Other.FaceChange("surprised", 1)           
                    "[Other.Name] noticed what you and [Girl.Name] are up to."
            else:
                    #if there has been some noticing already. . .
                    $ Other.FaceChange("sly", 1)       
                    if Other == KittyX:                    
                            "[Other.Name] is glancing at you and [Girl.Name] carefully. . ."    
                    elif Other == EmmaX:         
                            "[Other.Name] is carefully appraising you and [Girl.Name]. . ."
                    else:
                            "[Other.Name] is staring at you and [Girl.Name]. . ."
                    
        if "cockout" in Player.RecentActions:
                    #call Girl_First_Peen(Other)
                    call Seen_First_Peen(Other,Girl)
                    
        $ Girl.RecentActions.append("noticed " + Other.Tag)
        $ Other.RecentActions.append("noticed " + Girl.Tag)
        if Other == EmmaX and "three" not in EmmaX.History or "classcaught" not in EmmaX.History: 
                    #Emma-specific code
                    $ Other.AddWord(1,0,0,"saw with " + Girl.Tag) #adds to Traits.
                    if bg_current == EmmaX.Home:
                            #if you're in her room. . .
                            ch_e "If the two of you cannot keep your hands off each other, please do so elsewhere. . ."
                            "She shoves the two of you out of her room and slams the door."
                            $ Girl.Loc = "bg player"
                            jump Misplaced
                    call Remove_Girl(EmmaX)    
                    if not Silent:
                            "She seems uncomfortable with the situation and leaves the room."
                            "Perhaps you should ask her about it later."
                    return
                    
        if "poly " + Girl.Tag in Other.Traits or (Girl in Player.Harem and Other in Player.Harem):
                #if they already have a relationship. . .
                $ B = (1000-(20*Taboo))  
        else:             
                #if they don't have a relationship. . .
                $ B = (Other.GirlLikeCheck(Girl) - 500) #RogueX.LikeLaura - 500
                if "dating" in Other.Traits or Other in Player.Harem:
                        #if you and the other girl have a relationship. . .
                        $ B -= 200    
                
        $ Other.SpriteLoc = StageFarRight  
        call Display_Girl(Other,0,0) 
        if Partner == Other:
                #if this is already a Partner, skip this dialog
                $ Silent = 1
        $ Partner = Other    
        $ Line = 0   
        if ApprovalCheck(Other, 2000, TabM=2, Bonus = B) or ApprovalCheck(Other, 950, "L", TabM=2, Bonus = (B/3)): 
                    #if she's very loose or really likes you
                    $ Other.FaceChange("sexy", 1)
                    if not Silent:
                            "She decides to join you."                                      
                    $ Other.Statup("Obed", 90, 5)
                    $ Other.Statup("Inbt", 90, 5) 
                    $ Other.Statup("Lust", 90, 3)  
                    $ Other.AddWord(1,0,0,"poly " + Girl.Tag)
                    call Threeway_Set(Other,Mode="start",GirlB=Girl) 
        elif ApprovalCheck(Other, 650, "O", TabM=2) and ApprovalCheck(Other, 450, "L", TabM=1) or ApprovalCheck(Other, 800, "O", TabM=2, Bonus = (B/3)): 
                    #if she likes you, but is very obedient
                    $ Other.FaceChange("sexy")
                    if not Silent:
                            "She sits down patiently off to the side and watches."          
                    $ Other.Statup("Love", 90, 5) 
                    $ Other.Statup("Inbt", 90, 5)  
                    $ Other.Statup("Lust", 90, 2) 
                    $ Other.AddWord(1,0,0,"poly " + Girl.Tag)
                    call Threeway_Set(Other,"watch",Mode="start",GirlB=Girl)   
        elif ApprovalCheck(Other, 650, "I", TabM=2) and ApprovalCheck(Other, 450, "L", TabM=1) or ApprovalCheck(Other, 800, "I", TabM=2, Bonus = (B/3)):
                    #if she likes you, but is very uninhibited
                    $ Other.FaceChange("sexy")
                    if not Silent:
                            "She sits down and watches you with a hungry look."             
                    $ Other.Statup("Love", 90, 5) 
                    $ Other.Statup("Obed", 90, 2)
                    $ Other.Statup("Inbt", 90, 2)     
                    $ Other.Statup("Lust", 90, 5)
                    $ Other.AddWord(1,0,0,"poly " + Girl.Tag)
                    call Threeway_Set(Other,"watch",Mode="start",GirlB=Girl)  
        elif ApprovalCheck(Other, 1500, TabM=2, Bonus = B):
                    $ Other.FaceChange("perplexed", 1)
                    if not Silent:
                            "She looks a little confused at what's happening, but she stays put and watches."
                    if Other.Love >= Other.Obed and Other.Love >= Other.Inbt:
                        $ Other.Statup("Obed", 90, 2)
                        $ Other.Statup("Inbt", 90, 2)                 
                    elif Other.Obed >= Other.Inbt:
                        $ Other.Statup("Love", 90, 2) 
                        $ Other.Statup("Inbt", 90, 2)  
                    else:
                        $ Other.Statup("Love", 90, 2) 
                        $ Other.Statup("Obed", 90, 1)
                        $ Other.Statup("Inbt", 90, 1) 
                    $ Other.Statup("Lust", 90, 5) 
                    call Threeway_Set(Other,"watch",Mode="start",GirlB=Girl) 
        elif ApprovalCheck(Other, 650, "L", TabM=1) or ApprovalCheck(Other, 400, "O", TabM=2):
                    #if she likes you or is obedient, but not enough
                    $ Other.FaceChange("angry", 2)
                    if bg_current == Other.Home: 
                            if Other == LauraX:
                                "She looks annoyed, and kicks you both out of the room."
                            else: 
                                "She looks betrayed, and kicks you both out of the room."
                    else:
                            if Other == LauraX:
                                "She looks annoyed, and storms out of the room."  
                            else:
                                "She looks betrayed, and storms out of the room."                   
                    $ Other.Statup("Love", 200, -5) 
                    $ Other.Statup("Love", 80, -5) 
                    $ Other.Statup("Love", 70, -5) 
                    $ Other.Statup("Obed", 90, -5)
                    $ Other.Statup("Lust", 89, 10)
                    $ Partner = 0                             
                    $ Other.AddWord(1,0,0,"saw with " + Girl.Tag)
                    if bg_current == Other.Home: #Kicks you out if in Rogue's room
                            $ Other.RecentActions.append("angry")
                            call GirlsAngry
                    call Remove_Girl(Other)
        else:
                    #if she doesn't like you much
                    $ Other.FaceChange("surprised", 2)
                    $ Other.Statup("Inbt", 90, 2) 
                    $ Other.Statup("Lust", 40, 20)     
                    if Trigger != "kiss you":
                            $ Other.Statup("Love", 90, -10) 
                            $ Other.Statup("Obed", 90, -5)
                            $ Other.Statup("Lust", 80, 10)                    
                    if bg_current == Other.Home:
                            $ Other.Statup("Love", 90, -5) 
                            $ Other.Statup("Obed", 90, -5)
                            if Other == LauraX:
                                    "She looks uncomfortable with this, and shoves you both out of the room."  
                            else:
                                    "She looks embarrassed, and shoves you both out of the room."                   
                    elif Trigger != "kiss you":
                            if Other == LauraX:
                                    "She looks uncomfortable with this, and stalks out of the room." 
                            else:
                                    "She looks embarrassed, and bolts from the room." 
                    else:
                                    "She looks a bit disgusted and walks away."   
                    $ Partner = 0                   
                    if bg_current == Other.Home: #Kicks you out if in Rogue's room
                            $ Other.RecentActions.append("angry")
                            call GirlsAngry
                    call Remove_Girl(Other)        
        if AloneCheck(Girl) and Girl.Taboo == 20:
                #if the second girl ran away, it removes the taboo factor she added.
                $ Girl.Taboo = 0
                $ Taboo = 0
        if Line:
            # This plays a line from a threesome action, if there is one. 
            "[Line]."
            $ Line = 0
        return    
# End girls noticed / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start CloseOut  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
label CloseOut(Chr = Ch_Focus):
        # This exits out of the current sex act, whichever it might be, then returns                
        if Trigger == "blow":
            call expression Chr.Tag + "_BJ_After"
        elif Trigger == "hand":  
            call expression Chr.Tag + "_HJ_After"  
        elif Trigger == "titjob":
            call expression Chr.Tag + "_TJ_After"
        elif Trigger == "kiss you":
            call Kiss_After
        elif Trigger == "fondle breasts":
            call expression Chr.Tag + "_FB_After"
        elif Trigger == "suck breasts":
            call expression Chr.Tag + "_SB_After"
        elif Trigger == "fondle thighs":
            call expression Chr.Tag + "_FT_After"
        elif Trigger == "fondle pussy":
            call expression Chr.Tag + "_FP_After"
        elif Trigger == "lick pussy":
            call expression Chr.Tag + "_LP_After"
        elif Trigger == "fondle ass":
            call expression Chr.Tag + "_FA_After"
        elif Trigger == "insert ass":
            call expression Chr.Tag + "_IA_After"
        elif Trigger == "lick ass":
            call expression Chr.Tag + "_LA_After"
        elif Trigger == "sex":
            call expression Chr.Tag + "_SexAfter"
        elif Trigger == "hotdog":
            call expression Chr.Tag + "_HotdogAfter"
        elif Trigger == "anal":
            call expression Chr.Tag + "_AnalAfter"
        elif Trigger == "dildo pussy":
            call expression Chr.Tag + "_DP_After"
        elif Trigger == "dildo anal":
            call expression Chr.Tag + "_DA_After"
        elif Trigger == "strip":
            call Group_Strip_End
        elif Trigger == "masturbation":   
            $ Chr.Action -= 1
            $ Chr.Mast += 1    
        elif Trigger == "lesbian":                
            call Les_After
        else:
            "That's odd, tell Oni how you got here, Close [Chr.Name] [Trigger]."
        return
# End CloseOut  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  

# Start Sex_Over  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label Sex_Over(Clothes=1,Girls=0,BO=[]):
        #this routine plays out at the end of any sex menu session
        #it cleans them up and puts their clothes on, only returning a line of dialog if they were undressed
        # call Sex_Over(1,Girl)
        $ Line = 0
        call Trig_Reset  
        if Girls in TotalGirls:
                $ BO = [Girls]
        else:
                $ BO = TotalGirls[:]  
                $ renpy.random.shuffle(BO)
        while BO:   
                if BO[0].Loc == bg_current:
                        # if this girl is present
                        $ BO[0].OCount = 0    
                        call Girl_Cleanup(BO[0],"after")
                        if Player.Spunk:
                                if BO[0] == RogueX:
                                        ch_r "Let me take care of that for you. . ."
                                elif BO[0] == KittyX:
                                        ch_k "You've got a little something. . ."
                                        ch_k "just let me get that."
                                elif BO[0] == EmmaX:
                                        ch_e "[EmmaX.Petname], let's get you presentable. . ."
                                elif BO[0] == LauraX:
                                        ch_l "[LauraX.Petname], you've got a little something. . ."
                                call Girl_CleanCock(BO[0])
                $ BO.remove(BO[0])
                                        
        if Girls == Partner and Girls in TotalGirls:
                #swaps lead back to original
                call Shift_Focus(Girls)
        $ Girls = 0            
        call AllReset("all") #resets all sex positions.       
        
        if Clothes:   
                #if asked to put their clothes back on. 
                $ BO = TotalGirls[:]  
                while BO:   
                        if BO[0].Loc == bg_current:                                    
                                if BO[0].OutfitChange(Changed=1) == 2:
                                        if Line:
                                            $ Line = Line + " and " + BO[0].Name
                                        else:
                                            $ Line = BO[0].Name
                                        $ Girls += 1
                        $ BO.remove(BO[0])
                        
                if Girls > 1:
                    "[Line] throw their clothes back on."
                elif Girls:
                    "[Line] throws her clothes back on."        
        call Get_Dressed
        call Checkout(1)
        return
          
            
# End Sex_Over  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /         
       

# Start SkipTo  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
label SkipTo(Chr = Ch_Focus):
        # This jumps to the chosen sex act, called from the sex menu                     
        if Trigger == "blow":
            call expression Chr.Tag + "_BJ_Cycle"
        elif Trigger == "hand":  
            call expression Chr.Tag + "_HJ_Cycle"  
        elif Trigger == "titjob":
            call expression Chr.Tag + "_TJ_Cycle"
        elif Trigger == "kiss you":
            call KissCycle(Chr)
        elif Trigger == "fondle breasts":
            call expression Chr.Tag + "_FB_Cycle"
        elif Trigger == "suck breasts":
            call expression Chr.Tag + "_SB_Cycle"
        elif Trigger == "fondle thighs":
            call expression Chr.Tag + "_FT_Cycle"
        elif Trigger == "fondle pussy":
            call expression Chr.Tag + "_FP_Cycle"
        elif Trigger == "lick pussy":
            call expression Chr.Tag + "_LP_Cycle"
        elif Trigger == "fondle ass":
            call expression Chr.Tag + "_FA_Cycle"
        elif Trigger == "insert ass":
            call expression Chr.Tag + "_IA_Cycle"
        elif Trigger == "lick ass":
            call expression Chr.Tag + "_LA_Cycle"
        elif Trigger == "sex":
            call expression Chr.Tag + "_SexCycle"
        elif Trigger == "hotdog":
            call expression Chr.Tag + "_HotdogCycle"
        elif Trigger == "anal":
            call expression Chr.Tag + "_AnalCycle"
        elif Trigger == "dildo pussy":
            call expression Chr.Tag + "_DP_Cycle"
        elif Trigger == "dildo anal":
            call expression Chr.Tag + "_DA_Cycle"
        elif Trigger == "strip":
            call Group_Strip_End
        elif Trigger == "masturbation":   
            $ Chr.Action -= 1
            $ Chr.Mast += 1    
        elif Trigger == "lesbian":                
            call Les_Cycle(Chr)
        else:
            "That's odd, tell Oni how you got here, Close [Chr.Name] [Trigger]."            
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
        
       
    