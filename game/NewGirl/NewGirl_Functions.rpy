label Mod_Taboo_Level:
        #Set your taboo level
        if bg_current in ("bg player", "bg rogue", "bg kitty", "bg emma", "bg Mystique"):                     
                    $ Taboo = 0
        elif bg_current == "bg classroom" or "bg study":
                if Current_Time == "Night":
                    $ Taboo = 0
                elif Current_Time == "Evening" or Weekday >= 5:
                    if "locked" in E_RecentActions:
                            $ Taboo = 0
                    else:
                            $ Taboo = 30
                else:
                    $ Taboo = 40
        elif bg_current == "bg dangerroom":
                if Current_Time == "Night":
                    $ Taboo = 0
                else:
                    $ Taboo = 40

        elif bg_current == "bg pool":
                if Current_Time == "Night":
                    $ Taboo = 0
                else:
                    $ Taboo = 40

        elif bg_current == "bg field":
                if Current_Time == "Night":
                    $ Taboo = 0
                else:
                    $ Taboo = 40

        elif bg_current == "bg campus":
                if Current_Time == "Night":
                    $ Taboo = 20
                else:
                    $ Taboo = 40
        elif bg_current == "bg showerroom":        
                    $ Taboo = 20    
        else:
                    $ Taboo = 0
                    
        #Set Rogue's Taboo level
        if R_Loc in ("bg player", "bg rogue", "bg kitty", "bg emma", "bg Mystique"):  
                    if R_Loc == K_Loc and R_LikeKitty <= 800:
                        $ R_Taboo = 20
                        $ Taboo = 20    
                    elif R_Loc == E_Loc and R_LikeEmma <= 800:
                        $ R_Taboo = 20
                        $ Taboo = 20                       
                    else:
                        $ R_Taboo = 0
        elif R_Loc == "bg classroom":
                if Current_Time == "Night" or "locked" in E_RecentActions:
                    $ R_Taboo = 0
                elif Current_Time == "Evening" or Weekday >= 5:
                    $ R_Taboo = 30
                else:
                    $ R_Taboo = 40
        elif R_Loc == "bg dangerroom":
                if Current_Time == "Night":
                    $ R_Taboo = 0
                else:
                    $ R_Taboo = 40
        elif R_Loc == "bg pool":
                if Current_Time == "Night":
                    $ R_Taboo = 0
                else:
                    $ R_Taboo = 40
        elif R_Loc == "bg field":
                if Current_Time == "Night":
                    $ R_Taboo = 0
                else:
                    $ R_Taboo = 40
        elif R_Loc == "bg campus":
                if Current_Time == "Night":
                    $ R_Taboo = 20
                else:
                    $ R_Taboo = 40
        elif R_Loc == "bg showerroom":        
                    $ R_Taboo = 20    
        else:
                    $ R_Taboo = 0    
            
        #Set Kitty's Taboo level 
        if K_Loc in ("bg player", "bg rogue", "bg kitty", "bg emma", "bg Mystique"):  
                    if K_Loc == R_Loc and K_LikeRogue <= 800:
                        $ K_Taboo = 20
                        $ Taboo = 20  
                    elif K_Loc == E_Loc and K_LikeEmma <= 800:
                        $ K_Taboo = 20
                        $ Taboo = 20   
                    else:
                        $ K_Taboo = 0
        elif K_Loc == "bg classroom":
                if Current_Time == "Night" or "locked" in E_RecentActions:
                    $ K_Taboo = 0
                elif Current_Time == "Evening" or Weekday >= 5:
                    $ K_Taboo = 30
                else:
                    $ K_Taboo = 40
        elif K_Loc == "bg dangerroom":
                if Current_Time == "Night":
                    $ K_Taboo = 0
                else:
                    $ K_Taboo = 40
        elif K_Loc == "bg pool":
                if Current_Time == "Night":
                    $ K_Taboo = 0
                else:
                    $ K_Taboo = 40
        elif K_Loc == "bg field":
                if Current_Time == "Night":
                    $ K_Taboo = 0
                else:
                    $ K_Taboo = 40
        elif K_Loc == "bg campus":
                if Current_Time == "Night":
                    $ K_Taboo = 20
                else:
                    $ K_Taboo = 40
        elif K_Loc == "bg showerroom":        
                    $ K_Taboo = 20    
        else:
                    $ K_Taboo = 0   
                    
        #Set Emma's Taboo level 
        if E_Loc in ("bg player", "bg rogue", "bg kitty", "bg emma", "bg Mystique"):  
                    if E_Loc == R_Loc and E_LikeRogue <= 800:
                        $ E_Taboo = 20
                        $ Taboo = 20     
                    elif E_Loc == K_Loc and E_LikeKitty <= 800:
                        $ E_Taboo = 20
                        $ Taboo = 20                       
                    else:
                        $ E_Taboo = 0
        elif E_Loc == "bg classroom":
                if Current_Time == "Night" or "locked" in E_RecentActions:
                    $ E_Taboo = 0
                elif (Current_Time == "Evening" or Weekday >= 5):
                    $ E_Taboo = 30
                else:
                    $ E_Taboo = 40
        elif E_Loc == "bg dangerroom":
                if Current_Time == "Night":
                    $ E_Taboo = 0
                else:
                    $ E_Taboo = 40
        elif E_Loc == "bg pool":
                if Current_Time == "Night":
                    $ E_Taboo = 0
                else:
                    $ E_Taboo = 40
        elif E_Loc == "bg field":
                if Current_Time == "Night":
                    $ E_Taboo = 0
                else:
                    $ E_Taboo = 40
        elif E_Loc == "bg campus":
                if Current_Time == "Night":
                    $ E_Taboo = 20
                else:
                    $ E_Taboo = 40
        elif E_Loc == "bg showerroom":        
                    $ E_Taboo = 20    
        else:
                    $ E_Taboo = 0 

        
        #Set Mystique's Taboo level 
        if "Mystique" in Party:
                    $ newgirl["Mystique"].Loc = bg_current
        if newgirl["Mystique"].Loc == bg_current:
                $ newgirl["Mystique"].Taboo = Taboo            
        elif newgirl["Mystique"].Loc in ("bg player", "bg rogue", "bg kitty", "bg emma", "bg Mystique"): 
                $ newgirl["Mystique"].Taboo = 0
        elif newgirl["Mystique"].Loc == "bg classroom" or "bg study":
                if Current_Time == "Night":
                            $ newgirl["Mystique"].Taboo = 5
                elif Current_Time == "Evening" or Weekday >= 5:
                    if "locked" in P_RecentActions:
                            $ newgirl["Mystique"].Taboo = 0
                    else:
                            $ newgirl["Mystique"].Taboo = 30
                else:
                    $ newgirl["Mystique"].Taboo = 40
        elif newgirl["Mystique"].Loc == "bg dangerroom":
                if Current_Time == "Night":
                    $ newgirl["Mystique"].Taboo = 5
                else:
                    $ newgirl["Mystique"].Taboo = 40
        elif newgirl["Mystique"].Loc == "bg pool":
                if Current_Time == "Night":
                    $ newgirl["Mystique"].Taboo = 0
                else:
                    $ newgirl["Mystique"].Taboo = 40
        elif newgirl["Mystique"].Loc == "bg field":
                if Current_Time == "Night":
                    $ newgirl["Mystique"].Taboo = 0
                else:
                    $ newgirl["Mystique"].Taboo = 40
        elif newgirl["Mystique"].Loc == "bg campus":
                if Current_Time == "Night":
                    $ newgirl["Mystique"].Taboo = 20
                else:
                    $ newgirl["Mystique"].Taboo = 40
        elif newgirl["Mystique"].Loc == "bg showerroom":        
                    $ newgirl["Mystique"].Taboo = 20    
        else:
                    $ newgirl["Mystique"].Taboo = 40   


        return
        
        #end taboo level
       
label Mystique_Schedule(Clothes = 1, Location = 1, LocTemp = newgirl["Mystique"].Loc): 
        #Mystique's natural movements   
        # If not Clothes, don't bother with her outfit in the scheduel
        # Clothes 2 is ordered to change regardless of time of day
        # If not Location, don't bother with the location portion of the schedule
        
        if "met" not in newgirl["Mystique"].History or ("Mystique" in Party and Clothes != 2): 
                #if she's in a party, never mind
                return  
        if LocTemp == bg_current and Current_Time == "morning":
                #she slept over, so just forget this for now  
                if "sleepover" not in newgirl["Mystique"].RecentActions:
                    $ newgirl["Mystique"].RecentActions.append("sleepover")
                    return           
                #the second time this is called, it skips through    
        
        $ D20 = renpy.random.randint(1, 20) 
        
        if (Current_Time == "Morning" and Clothes and Round >= 90) or Clothes == 2:                                                       #Pick clothes for the day
                $ Options = ["regular"]
                #$ Options = ["regular"]
                #$ Options.append("costume") if ApprovalCheck("Mystique", 1000) else Options
                $ Options.append("custom1") if newgirl["Mystique"].Custom[0] == 2 else Options
                $ Options.append("custom2") if newgirl["Mystique"].Custom2[0] == 2 else Options
                $ Options.append("custom3") if newgirl["Mystique"].Custom3[0] == 2 else Options
                $ Options.append("custom4") if newgirl["Mystique"].Custom4[0] == 2 else Options
                $ Options.append("custom5") if newgirl["Mystique"].Custom5[0] == 2 else Options
                $ Options.append("custom6") if newgirl["Mystique"].Custom6[0] == 2 else Options
                $ Options.append("custom7") if newgirl["Mystique"].Custom7[0] == 2 else Options
                $ renpy.random.shuffle(Options) 
                $ newgirl["Mystique"].OutfitDay = Options[0]
                $ del Options[:]  
                $ newgirl["Mystique"].Outfit = newgirl["Mystique"].OutfitDay 
        #End clothing portion
        # if newgirl["Mystique"].Loc == "bg teacher" or newgirl["Mystique"].Loc == "bg classroom":
        #         $ newgirl["Mystique"].Outfit = "teacher" 
            
        #Location portion   
        if "Mystique" in Party or newgirl["Mystique"].Loc == "hold":
                pass          
                
        elif Weekday == 0 or Weekday == 2 or Weekday == 4:
        #MoWeFr   
                if Current_Time == "Morning":
                        $ newgirl["Mystique"].Loc = "bg Mystique"
                elif Current_Time == "Midday": 
                        $ newgirl["Mystique"].Loc = "bg Mystique"
                else:
                        $ newgirl["Mystique"].Loc = "bg Mystique"
        elif Weekday == 1 or Weekday == 3:
        #TuThu      
                if Current_Time == "Morning":
                        $ newgirl["Mystique"].Loc = "bg Mystique"
                elif Current_Time == "Midday":
                        $ newgirl["Mystique"].Loc = "bg Mystique"
                elif Current_Time == "Evening":
                        $ newgirl["Mystique"].Loc = "bg Mystique"
                else:
                        $ newgirl["Mystique"].Loc = "bg Mystique"
        else:
        #Weekend                               
                if Current_Time == "Morning":
                        $ Options = ["bg Mystique", "bg Mystique"]
                        $ renpy.random.shuffle(Options)
                        $ newgirl["Mystique"].Loc = Options[0]
                        $ del Options[:]
                elif Current_Time == "Midday":
                        $ Options = ["bg Mystique", "bg Mystique"]
                        $ renpy.random.shuffle(Options)
                        $ newgirl["Mystique"].Loc = Options[0]
                        $ del Options[:]
                else:
                        $ newgirl["Mystique"].Loc = "bg Mystique"

                if Current_Time == "Night":
                        $ newgirl["Mystique"].Loc = "bg Mystique"
                else:
                        $ Options = ["bg Mystique", "bg Mystique"]
                        $ renpy.random.shuffle(Options)
                        $ newgirl["Mystique"].Loc = Options[0]
                        $ del Options[:]

                        
        #If Mystique has moved from where she started this action. . .   
        if newgirl["Mystique"].Loc != LocTemp and "Mystique" not in Party:    
                if LocTemp == bg_current: #If she was where you were
                    $ newgirl["Mystique"].RecentActions.append("leaving") 
                elif newgirl["Mystique"].Loc == bg_current: #If she's showed up
                    $ newgirl["Mystique"].RecentActions.append("arriving") 
        return
#End Mystique's Schedule


label Mystique_Todo:                       
        #Actions checked each night  
        #causes her to grow her pubes out over a week
        if "pubes" in newgirl["Mystique"].Todo:
                $ newgirl["Mystique"].PubeC -= 1
                if newgirl["Mystique"].PubeC >= 1:
                        pass
                else:            
                        $ newgirl["Mystique"].Pubes = 1
                        $ newgirl["Mystique"].Todo.remove("pubes") 
                        
        #causes her to wax her pubes
        if "shave" in newgirl["Mystique"].Todo:               
                $ newgirl["Mystique"].Pubes = 0
                $ newgirl["Mystique"].Todo.remove("shave")
                
        #causes her to put in piercings     
        if "ring" in newgirl["Mystique"].Todo:                
                $ newgirl["Mystique"].Pierce = "ring"
                $ newgirl["Mystique"].Todo.remove("ring")
        if "barbell" in newgirl["Mystique"].Todo:
                $ newgirl["Mystique"].Pierce = "barbell"
                $ newgirl["Mystique"].Todo.remove("barbell")            
        return

# label Mod_Daily_Math:
    
#     if Day != BH_Day:
#         $ BH_Day = Day
#         call Mod_Wait
#         return
    
#     if Current_Time != BH_Current_Time:
#         $ BH_Current_Time = Current_Time
#         call Mod_Hourly
#         return



label Mod_Wait (Outfit = 1, Lights = 1, Wait = 1):
    if Wait:
        call Wait(Outfit, Lights)
    $ newgirl["Mystique"].Addict += newgirl["Mystique"].Addictionrate

    if Time_Count < 3:  #not sleep time                                          
                $ newgirl["Mystique"].Action += 1

    # Things that happen when you sleep   
    else:                                                          

        # Things about Mystique when you sleep:
                if newgirl["Mystique"].Loc == "hold":
                        $ newgirl["Mystique"].Loc = "bg Mystique"  
                if newgirl["Mystique"].Todo:
                        call Mystique_Todo
                
                if "addict mystique" in P_Traits:
                        $ newgirl["Mystique"].Addict += newgirl["Mystique"].Addictionrate
                        $ newgirl["Mystique"].Addict -= (3*newgirl["Mystique"].Resistance)
                else:
                        $ newgirl["Mystique"].Addict = 0
                        $ newgirl["Mystique"].Addictionrate = 0
        
                if "addictive" in P_Traits:  
                        pass
                elif "nonaddictive" in P_Traits:        
                        $ newgirl["Mystique"].Addictionrate -= 2
                        $ newgirl["Mystique"].Addict -= 5
                elif newgirl["Mystique"].Addictionrate:
                        $ newgirl["Mystique"].Addictionrate -= newgirl["Mystique"].Resistance
                    
                $ newgirl["Mystique"].ForcedCount -= 1 if newgirl["Mystique"].ForcedCount > 0 else 0
                $ newgirl["Mystique"].Action = newgirl["Mystique"].MaxAction    
                
                $ newgirl["Mystique"].Rep = 0 if newgirl["Mystique"].Rep < 0 else newgirl["Mystique"].Rep 
                $ newgirl["Mystique"].Rep += 10 if newgirl["Mystique"].Rep < 800 else 0
                $ newgirl["Mystique"].Rep = 1000 if newgirl["Mystique"].Rep > 1000 else newgirl["Mystique"].Rep 
                $ newgirl["Mystique"].Lust -= 5 if newgirl["Mystique"].Lust >= 50 else 0
                
                if "painted" not in newgirl["Mystique"].DailyActions or "cleaned" not in newgirl["Mystique"].DailyActions:   
                        $ del newgirl["Mystique"].Spunk[:]  
                
                if "lover" in newgirl["Mystique"].Petnames and newgirl["Mystique"].Love > 800:
                        $ newgirl["Mystique"].Love += 10
                if "master" in newgirl["Mystique"].Petnames and newgirl["Mystique"].Obed > 600:
                        $ newgirl["Mystique"].Obed += 10
                if "fuck buddy" in newgirl["Mystique"].Petnames:
                        $ newgirl["Mystique"].Inbt += 10    
     
    #End of things when you sleep
    call Mod_Hourly(Outfit)
    return


label Mod_Hourly(Outfit = 0):
    
    #Things that are about you:
    $ newgirl["Mystique"].OCount = 0

    #Things that are about Mystique:   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  
    if newgirl["Mystique"].Lust >= 70 and newgirl["Mystique"].Loc != bg_current:
        $ newgirl["Mystique"].Lust = 25
            
    #Resets her flirt  options
    $ newgirl["Mystique"].Chat[5] = 0 
    
    #Resets her addiction fix attempts
    if newgirl["Mystique"].Event[3]:
        $ newgirl["Mystique"].Event[3] -= 1               
    
    $ newgirl["Mystique"].Forced = 0
    if newgirl["Mystique"].Loc == "bg teacher" and "bg classroom" in (bg_current, R_Loc, K_Loc):
            $ newgirl["Mystique"].XP += 10 
    if newgirl["Mystique"].Loc == "bg classroom" or newgirl["Mystique"].Loc == "bg dangerroom" :
            $ newgirl["Mystique"].XP += 10    
    elif newgirl["Mystique"].Loc == "bg showerroom":
            call Remove_Girl("Mystique")
        
    #Appearance clean-up
    $ newgirl["Mystique"].Blush = 0
    $ newgirl["Mystique"].Water = 0
    $ newgirl["Mystique"].Held = 0 
    
    # Reduce addiction
    $ newgirl["Mystique"].Addictionrate -= newgirl["Mystique"].Resistance if newgirl["Mystique"].Addictionrate > 3 else 0    
    $ newgirl["Mystique"].Addictionrate = 0 if newgirl["Mystique"].Addictionrate < 0 else newgirl["Mystique"].Addictionrate    
    
    #Adjusts shame rate
    if newgirl["Mystique"].Taboo and newgirl["Mystique"].Shame:
            if newgirl["Mystique"].Loc == "bg dangerroom":            
                    $ newgirl["Mystique"].Shame -= 10 if newgirl["Mystique"].Shame >=10 else newgirl["Mystique"].Shame
            $ Count = int((newgirl["Mystique"].Taboo * newgirl["Mystique"].Shame) / 200)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 90, Count)         
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, Count) 
            $ newgirl["Mystique"].Rep -= int(1.5 * Count)
    
    $ newgirl["Mystique"].Love -= 5*(Mod_Action_Check("Mystique","recent","unsatisfied")) #subtracts newgirl["Mystique"].Love by 5* the number of recent unsatisfieds
    
    # Clears out recent and daily actions
    $ del newgirl["Mystique"].RecentActions[:]                            # Clears out recent and daily actions
    if Time_Count == 0: 
        $ del newgirl["Mystique"].DailyActions[:]
        
    call Mystique_Schedule
    call Stat_Checks
    if Outfit:
        call MystiqueOutfit(newgirl["Mystique"].OutfitDay)
    #end Mystique hourly actions 


    return


label Mod_Round10(Options = ["none"]):    
        #Called when it's time to auto-wait/sleep
        if Current_Time == "Night":
                if bg_current == "bg Mystique":         
                        #If it's Mystique's room, she gets dibs                         
                        if newgirl["Mystique"].Loc != bg_current: 
                                # if Mystique isn't around. . .
                                if newgirl["Mystique"].Sleep >= 5: 
                                        call CleartheRoom("Mystique",1)
                                        "She probably wouldn't mind you taking a quick nap. . ."
                                        call Mod_Wait
                                        if newgirl["Mystique"].Loc == bg_current:
                                                call DrainWord("Mystique","arriving")
                                                ch_m "Well look whos sleeping in my bed. . ."
                                else:
                                        "She probably wouldn't appreciate you staying over, you head back to your own room."
                                        $ renpy.pop_call()
                                        jump Player_Room
                        call CleartheRoom("Mystique",1)
                        call Mystique_Sleepover
                else: 
                        #You're not in anyone else's room
                        if R_Loc == bg_current and R_Sleep >= 2 and ApprovalCheck("Rogue", 1000): 
                                    $ Options.append("Rogue")
                                    $ Options.append("Rogue")
                        if K_Loc == bg_current and K_Sleep >= 2 and ApprovalCheck("Kitty", 1000): 
                                    $ Options.append("Kitty")
                                    $ Options.append("Kitty")
                        if E_Loc == bg_current and E_Sleep >= 2 and ApprovalCheck("Emma", 1000): 
                                    $ Options.append("Emma")
                                    $ Options.append("Emma")
                        if newgirl["Mystique"].Loc == bg_current and newgirl["Mystique"].Sleep >= 2 and ApprovalCheck("Mystique", 1000): 
                                    $ Options.append("Mystique")
                                    $ Options.append("Mystique")
                                    
                        $ renpy.random.shuffle(Options)
                        if Options[0] == "none":
                                if R_Loc == bg_current and ApprovalCheck("Rogue", 1000): 
                                            $ Options[0] = "Rogue"
                                elif K_Loc == bg_current and ApprovalCheck("Kitty", 1000): 
                                            $ Options[0] = "Kitty"
                                elif E_Loc == bg_current and ApprovalCheck("Emma", 1000): 
                                            $ Options[0] = "Emma"  
                                elif newgirl["Mystique"].Loc == bg_current and ApprovalCheck("Mystique", 1000): 
                                            $ Options[0] = "Mystique"                            
                                
                        if Options[0] == "Rogue":                                
                                call CleartheRoom("Rogue",1)
                                call Rogue_Sleepover
                        elif Options[0] == "Kitty":    
                                call CleartheRoom("Kitty",1)
                                call Kitty_Sleepover
                        elif Options[0] == "Emma":    
                                call CleartheRoom("Emma",1)
                                call Emma_Sleepover
                        elif Options[0] == "Mystique":    
                                call CleartheRoom("Mystique",1)
                                call Mystique_Sleepover
                        else:   
                                call CleartheRoom("All",1)
                                #if nobody is here, you just go to sleep
                                "It's getting late, so you go to sleep."
                                call Mod_Wait
                #End night time
        else:
                    #if it's not night time, just wait
                    if bg_current == "bg rogue":
                            if R_Loc == bg_current:
                                ch_r "Sure, you can wait around a bit."     
                            else:
                                "You wait for Rogue to return."
                            call Mod_Wait
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
                            call Mod_Wait
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
                            call Mod_Wait
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
                    else:
                        call Mod_Wait
        return


label Mod_Sex_Dialog(Primary = Ch_Focus, Secondary = 0, TempFocus = 0, PrimaryLust = 0, SecondaryLust = 0, Line1 = 0, Line2 = 0, Line3 = 0, Line4 = 0, D20S = 0): #call Sex_Dialog("Rogue","Kitty") 
        # Primary is main female, secondary is supporting female, action is what they are doing.
        $ Line = 0
        
        $ D20S = renpy.random.randint(1, 20) if not D20S else D20S #Sets random seed factor for the encounter
        # If the seed is 0-5, only offhands will play. If it's 15-20, only trigger3's will play. If it's 5-10, offhand and Secondaries will play.
        # If it's 10-15 all things will play. 
           
        # Checks for Taboo, and if it passes through, calls the first sex dialog
        if Primary == "Rogue":
                    if K_Loc == bg_current and not Taboo:                           #If Kitty is around and it's otherwise private
                        call Kitty_Noticed("Rogue")
                        $ Secondary = "Kitty" if K_Loc == bg_current else Secondary
                    elif E_Loc == bg_current and not Taboo:                           #If Emma is around and it's otherwise private
                        call Emma_Noticed("Rogue")
                        $ Secondary = "Emma" if E_Loc == bg_current else Secondary
                    # elif newgirl["Laura"].Loc == bg_current and not Taboo:
                        # call Laura_Noticed(Primary)
                        # $ Secondary = "Laura" if newgirl["Laura"].Loc == bg_current else Secondary
                    elif Taboo and (D20S + (int(Taboo/10)) - Stealth) >= 10:        #If there is a Taboo level, and your modified roll is over 10
                        call Rogue_Taboo
                    call Rogue_SexDialog
                                    
        elif Primary == "Kitty":
                    if R_Loc == bg_current and not Taboo:                           #If Rogue is around and it's otherwise private
                        call Rogue_Noticed("Kitty")
                        $ Secondary = "Rogue" if R_Loc == bg_current else Secondary
                    elif E_Loc == bg_current and not Taboo:                           #If Emma is around and it's otherwise private
                        call Emma_Noticed("Kitty")
                        $ Secondary = "Emma" if E_Loc == bg_current else Secondary
                    elif Taboo and (D20S + (int(Taboo/10)) - Stealth) >= 10:        #If there is a Taboo level, and your modified roll is over 10
                        call Kitty_Taboo
                    call Kitty_SexDialog
                    
        elif Primary == "Emma":
                    if R_Loc == bg_current and not Taboo:                           #If Rogue is around and it's otherwise private
                        call Rogue_Noticed("Emma")
                        $ Secondary = "Rogue" if R_Loc == bg_current else Secondary
                    elif K_Loc == bg_current and not Taboo:                           #If Kitty is around and it's otherwise private
                        call Kitty_Noticed("Emma")
                        $ Secondary = "Kitty" if K_Loc == bg_current else Secondary
                    # elif newgirl["Laura"].Loc == bg_current and not Taboo:
                        # call Laura_Noticed(Primary)
                        # $ Secondary = "Laura" if newgirl["Laura"].Loc == bg_current else Secondary
                    elif Taboo and (D20S + (int(Taboo/10)) - Stealth) >= 10:        #If there is a Taboo level, and your modified roll is over 10
                        call Emma_Taboo
                    call Emma_SexDialog

        elif Primary == "Mystique":
                    if R_Loc == bg_current and not Taboo:                           #If Rogue is around and it's otherwise private
                        call Rogue_Noticed("Mystique")
                        $ Secondary = "Rogue" if R_Loc == bg_current else Secondary
                    elif K_Loc == bg_current and not Taboo:                           #If Kitty is around and it's otherwise private
                        call Kitty_Noticed("Mystique")
                        $ Secondary = "Kitty" if K_Loc == bg_current else Secondary
                    # elif newgirl["Laura"].Loc == bg_current and not Taboo:
                        # call Laura_Noticed(Primary)
                        # $ Secondary = "Laura" if newgirl["Laura"].Loc == bg_current else Secondary
                    elif Taboo and (D20S + (int(Taboo/10)) - Stealth) >= 10:        #If there is a Taboo level, and your modified roll is over 10
                        call Mystique_Taboo
                    call Mystique_SexDialog

        elif Primary == "Laura":
                    if R_Loc == bg_current and not Taboo:                           #If Rogue is around and it's otherwise private
                        call Rogue_Noticed("Laura")
                        $ Secondary = "Rogue" if R_Loc == bg_current else Secondary
                    elif K_Loc == bg_current and not Taboo:                           #If Kitty is around and it's otherwise private
                        call Kitty_Noticed("Laura")
                        $ Secondary = "Kitty" if K_Loc == bg_current else Secondary
                    elif E_Loc == bg_current and not Taboo:                           #If Emma is around and it's otherwise private
                        call Emma_Noticed("Kitty")
                        $ Secondary = "Emma" if E_Loc == bg_current else Secondary
                    elif Taboo and (D20S + (int(Taboo/10)) - Stealth) >= 10:        #If there is a Taboo level, and your modified roll is over 10
                        call Laura_Taboo
                    call Laura_SexDialog
        
        
        $ Line1 = Line #Set Line1 to the current state of the Line variable
                
        # If there is a player offhand Trigger set and the random value is 1-15, add an Offhand dialog
        if Trigger2 and D20S <= 15:
                    $ Line = ""
                    if Primary == "Rogue":                        
                        call Rogue_Offhand
                    elif Primary == "Kitty":
                        call Kitty_Offhand
                    elif Primary == "Emma":
                        call Emma_Offhand
                    elif Primary == "Mystique":
                        call Mystique_Offhand
                    elif Primary == "Laura":
                        call Laura_Offhand
                    
                    $ Line1 = Line1 + Line
        else:                
                    $ Line1 = Line1 +"."
        
        # If there is a Primary offhand Trigger set and the random value is 1-10, add a self-directed dialog
        if D20S >= 7 and Trigger not in ("masturbation", "lesbian"):
                    $ Line = 0
                    if Primary == "Rogue":
                        call Rogue_Self_Lines("T3",Trigger3)
                    elif Primary == "Kitty":
                        call Kitty_Self_Lines("T3",Trigger3)
                    elif Primary == "Emma":
                        call Emma_Self_Lines("T3",Trigger3)
                    elif Primary == "Mystique":
                        call NewGirl_Self_Lines("Mystique","T3",Trigger3)
                    elif Primary == "Laura":
                        call NewGirl_Self_Lines("Laura","T3",Trigger3)
                    if Line:
                        $ Line3 = Line + "."
           
        # If there is a Secondary character and the random value is 5-15, add a threeway dialog
        if Secondary and (7 <= D20S <= 17 or Trigger4 == "watch"):
                    $ Line = 0
                    if Secondary == "Rogue":
                        call Rogue_SexDialog_Threeway
                    elif Secondary == "Kitty":
                        call Kitty_SexDialog_Threeway
                    elif Secondary == "Emma":
                        call Emma_SexDialog_Threeway
                    elif Secondary == "Mystique":
                        call Mystique_SexDialog_Threeway
                    elif Secondary == "Laura":
                        call Laura_SexDialog_Threeway
                    if Line:
                        $ Line4 = Line + "."
        
        #Applying player's satisfaction
        $ P_Focus = Statupdate("Player", "Focus", P_Focus, 200, TempFocus) 
        
        #Applying primary girl's satisfaction
        if Primary == "Rogue":
                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, PrimaryLust) 
                call RogueLust
        elif Primary == "Kitty":
                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, PrimaryLust)
                call KittyLust
        elif Primary == "Emma":
                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, PrimaryLust)
                call EmmaLust
        elif Primary == "Mystique":
                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, PrimaryLust)
                call MystiqueLust
        elif Primary == "Laura":
                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, PrimaryLust)
                call MystiqueLust
        
        #Applying secondary girl's satisfaction
        if Secondary == "Rogue":
                $ SecondaryLust += (int(PrimaryLust/10)) if Primary == "Kitty" and R_LikeKitty >= 70 else 0  
                $ SecondaryLust += (int(PrimaryLust/10)) if Primary == "Emma" and R_LikeEmma >= 70 else 0 
                $ SecondaryLust += (int(PrimaryLust/10)) if (Primary == "Laura" or Primary == "Mystique") and R_LikeNewGirl[Primary] >= 70 else 0 
                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, SecondaryLust) 
                call RogueLust
        elif Secondary == "Kitty":
                $ SecondaryLust += (int(PrimaryLust/10)) if Primary == "Rogue" and K_LikeRogue >= 70 else 0  
                $ SecondaryLust += (int(PrimaryLust/10)) if Primary == "Emma" and K_LikeEmma >= 70 else 0        
                $ SecondaryLust += (int(PrimaryLust/10)) if (Primary == "Laura" or Primary == "Mystique") and K_LikeNewGirl[Primary] >= 70 else 0        
                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, SecondaryLust)
                call KittyLust
        elif Secondary == "Emma":
                $ SecondaryLust += (int(PrimaryLust/10)) if Primary == "Rogue" and E_LikeRogue >= 50 else 0   
                $ SecondaryLust += (int(PrimaryLust/10)) if Primary == "Kitty" and E_LikeKitty >= 50 else 0     
                $ SecondaryLust += (int(PrimaryLust/10)) if (Primary == "Laura" or Primary == "Mystique") and E_LikeNewGirl[Primary] >= 50 else 0     
                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, SecondaryLust)
                call EmmaLust
        elif Secondary == "Mystique" or Secondary == "Laura":
                $ SecondaryLust += (int(PrimaryLust/10)) if Primary == "Rogue" and newgirl[Secondary].LikeRogue >= 50 else 0   
                $ SecondaryLust += (int(PrimaryLust/10)) if Primary == "Kitty" and newgirl[Secondary].LikeKitty >= 50 else 0     
                $ SecondaryLust += (int(PrimaryLust/10)) if Primary == "Emma" and newgirl[Secondary].LikeEmma >= 50 else 0     
                $ SecondaryLust += (int(PrimaryLust/10)) if (Primary == "Laura" or Primary == "Mystique") and newgirl[Secondary].LikeNewGirl[Primary] >= 50 else 0     
                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl[Secondary].Lust, 200, SecondaryLust)
                if Secondary == "Mystique":
                    call MystiqueLust
                elif Secondary == "Laura":
                    call LauraLust

        # Dialog begins to play out. . .  
        
        "[Line1]"
        $ Line = Line1
        if Line3:
                #If there's a secondary line, play it
                "[Line3]"
                $ Line = Line3
        if Line4:   
                #add call to First Les here."
                #If there's a third person line, play it
                "[Line4]"
                $ Line = Line4
        call NewGirl_Dirty_Talk
                        
        return
        
    
label Mod_Activity_Check(Girl=0,Girl2=0,Silent=0,Removal=1,ClothesCheck=1,Mod=0,Approval=1,Tempshame=0):
        # This checks whether a girl is up for watching a given activity
        # Silent is whether it plays dialog or not, Removal is whether it auto-removes the girl on a fail,
        # ClothesCheck is whether it bothers checking clothing, 2 if skip first girl
        # Mod gets set to her Like stat -600, so 600 Like, you break even, otherwise it's a penalty
        # call Activity_Check("Rogue",0,1,0)
        if not Girl2 or ClothesCheck == 2:
                $ Mod = 0
        else:
                $ Mod = (GirlLikeCheck(Girl,Girl2)-600)
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
                        $ Tempshame = newgirl["Laura"].Shame
                
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
                        
        if not Approval:
                    # If it fails the clothing check, skip the next part
                    pass
        elif Trigger == "strip" and Trigger2 != "jackin":
                    pass #covered by the above check
        elif not Trigger:
                    pass
        elif Trigger == "lick ass":
                    $ Approval = ApprovalCheck(Girl,1550,Bonus=Mod, TabM = 3)
        elif Trigger == "anal":
                    $ Approval = ApprovalCheck(Girl,1550,Bonus=Mod, TabM = 3)
        elif Trigger == "sex":
                    $ Approval = ApprovalCheck(Girl,1400,Bonus=Mod, TabM = 3)
        elif Trigger == "lick pussy":            
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = 2)
        elif Trigger2 == "jackin":            
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = 2)
        elif Trigger == "blow":            
                    $ Approval = ApprovalCheck(Girl,1300,Bonus=Mod, TabM = 2)
        elif Trigger == "titjob":              
                    $ Approval = ApprovalCheck(Girl,1200,Bonus=Mod, TabM = 3) 
        elif Trigger == "hotdog":
                    $ Approval = ApprovalCheck(Girl,1000,Bonus=Mod, TabM = 3)                
        elif Trigger == "hand" or Trigger3 == "hand":              
                    $ Approval = ApprovalCheck(Girl,1100,Bonus=Mod, TabM = 2)
        elif Trigger == "foot":
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = 2)  
        elif Trigger == "dildo anal":
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = 2)
        elif Trigger == "dildo pussy":
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = 2)
        elif Trigger == "insert ass":
                    $ Approval = ApprovalCheck(Girl,1300,Bonus=Mod, TabM = 2)
        elif Trigger == "fondle pussy" or Trigger == "insert pussy":
                    $ Approval = ApprovalCheck(Girl,1050,Bonus=Mod, TabM = 2)
        elif Trigger == "suck breasts":            
                    $ Approval = ApprovalCheck(Girl,1050,Bonus=Mod, TabM = 3)
        elif Trigger == "fondle breasts":                        
                    $ Approval = ApprovalCheck(Girl,950,Bonus=Mod, TabM = 2)
        elif Trigger == "fondle ass":
                    $ Approval = ApprovalCheck(Girl,850,Bonus=Mod, TabM = 1)
                    
        elif Trigger == "masturbation": 
                    $ Approval = ApprovalCheck(Girl,1200,Bonus=Mod, TabM = 2)
                    
        elif Trigger == "kiss you":
                    $ Approval = ApprovalCheck(Girl,500,Bonus=Mod, TabM = 0)                    
        elif Trigger == "fondle thighs":
                    $ Approval = ApprovalCheck(Girl,750,Bonus=Mod, TabM = 0)
                    
        elif Trigger == "lesbian": 
                    $ Approval = ApprovalCheck(Girl,1350,Bonus=Mod, TabM = 2)                           
        
        if not Silent and not Approval:
            if Girl == "Rogue":
                    ch_r "Ain't none a this right, [R_Petname]."
            elif Girl == "Kitty":
                    ch_k "I'm[K_like]not really comfortable here?"
            elif Girl == "Emma":
                    ch_e "This has become a bit too. . . scandalous for my tastes."
            elif Girl == "Laura":
                    ch_l "This is getting weird."
        
        if Removal and not Approval:
                call Remove_Girl(Girl,2)
                "[Girl] takes off."
                
        return Approval

# to remove words from the daily/recent lists , ie call DrainWord("Rogue","sex",1,0)
label Mod_DrainWord(Character = "Rogue", Word = "word", Recent = 1, Daily = 1):
            if Character == "Kitty" or Character == "All":
                            if Word == "around" and Word in K_Traits:
                                while Word in K_Traits:
                                        $ K_Traits.remove(Word) 
                            if Word in K_RecentActions and Recent:
                                while Word in K_RecentActions:
                                        $ K_RecentActions.remove(Word) 
                            if Word in K_DailyActions and Daily:
                                while Word in K_DailyActions:
                                        $ K_DailyActions.remove(Word) 
            elif Character == "Emma" or Character == "All":
                            if Word in E_RecentActions and Recent:
                                while Word in E_RecentActions:
                                        $ E_RecentActions.remove(Word) 
                            if Word in E_DailyActions and Daily:
                                while Word in E_DailyActions:
                                        $ E_DailyActions.remove(Word) 
            elif Character == "Player":
                            if Word in P_RecentActions and Recent:
                                while Word in P_RecentActions:
                                        $ P_RecentActions.remove(Word) 
                            if Word in P_DailyActions and Daily:
                                while Word in P_DailyActions:
                                        $ P_DailyActions.remove(Word)  
            elif Character == "Rogue":
                            if Word == "around" and Word in R_Traits:
                                while Word in R_Traits:
                                        $ R_Traits.remove(Word) 
                            if Word in R_RecentActions and Recent:
                                while Word in R_RecentActions:
                                        $ R_RecentActions.remove(Word) 
                            if Word in R_DailyActions and Daily:
                                while Word in R_DailyActions:
                                        $ R_DailyActions.remove(Word)  
            elif Character in ModdedGirls or Character == "All":
                            if Word in newgirl[Character].RecentActions and Recent:
                                while Word in newgirl[Character].RecentActions:
                                        $ newgirl[Character].RecentActions.remove(Word) 
                            if Word in newgirl[Character].DailyActions and Daily:
                                while Word in newgirl[Character].DailyActions:
                                        $ newgirl[Character].DailyActions.remove(Word)    
            return

label NewGirl_Noticed(Girl_ = "Mystique", Other = "Rogue", B = 0):
    if "noticed rogue" in newgirl[Girl_].RecentActions and Other == "Rogue":
            return
    if "noticed kitty" in newgirl[Girl_].RecentActions and Other == "Kitty":
            return
    if "noticed emma" in newgirl[Girl_].RecentActions and Other == "Emma":
            return
    
    call NewGirl_Face(Girl_,"surprised", 1)

    if Other == "Rogue":            
            "[Girl_] noticed what you and Rogue are up to."
            $ newgirl[Girl_].RecentActions.append("noticed rogue")
            if "poly rogue" in newgirl[Girl_].Traits:
                    $ B = (1000-(20*Taboo))  
            else:
                    $ B = (newgirl[Girl_].LikeRogue - 500)
                    if "dating" in newgirl[Girl_].Traits:
                        $ B -= 200
    elif Other == "Kitty":            
            "[Girl_] noticed what you and Kitty are up to."
            $ newgirl[Girl_].RecentActions.append("noticed kitty")
            if "poly kitty" in newgirl[Girl_].Traits:
                    $ B = (1000-(20*Taboo))  
            else:
                    $ B = (newgirl[Girl_].LikeKitty - 500)
                    if "dating" in newgirl[Girl_].Traits:
                        $ B -= 200

    elif Other == "Emma":            
            "[Girl_] noticed what you and Emma are up to."
            $ newgirl[Girl_].RecentActions.append("noticed emma")
            if "poly emma" in newgirl[Girl_].Traits:
                    $ B = (1000-(20*Taboo))  
            else:
                    $ B = (newgirl[Girl_].LikeEmma - 500)
                    if "dating" in newgirl[Girl_].Traits:
                        $ B -= 200

    elif Other in ModdedGirls:            
            call NewGirl_Face(Girl_, "surprised", 1)
            "[Girl_] noticed what you and [Other] are up to."
            $ newgirl[Girl_].RecentActions.append("noticed " + Other)
            $ PolyVariable = "poly " + Other
            if PolyVariable in newgirl[Girl_].Traits:
                $ B = (1000-(20*Taboo))  
            else:
                $ B = (newgirl[Girl_].LikeNewGirl[Other] - 500)               
                if "dating" in newgirl[Girl_].Traits:
                    $ B -= 200
                        
    $ Partner = Girl_
    if ApprovalCheck(Girl_, 2000, TabM=2, Bonus = B) or ApprovalCheck(Girl_, 950, "L", TabM=2, Bonus = (B/3)):
            #if she's very loose or really likes you
            call NewGirl_Face(Girl_,"sexy", 1)
            "She decides to join you."                                      
            $ newgirl[Girl_].Obed = Statupdate(Girl_, "Obed", newgirl[Girl_].Obed, 90, 5)
            $ newgirl[Girl_].Inbt = Statupdate(Girl_, "Inbt", newgirl[Girl_].Inbt, 90, 5) 
            $ newgirl[Girl_].Lust = Statupdate(Girl_, "Lust", newgirl[Girl_].Lust, 90, 3) 
            if Other == "Rogue" and "poly rogue" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly rogue") 
            elif Other == "Kitty" and "poly kitty" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly kitty") 
            elif Other == "Emma" and "poly emma" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly emma") 
            elif Other and ("poly " + Other) not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly " + Other) 
            call NewGirl_Threeway_Set(Girl_)
    elif ApprovalCheck(Girl_, 650, "O", TabM=2) and ApprovalCheck(Girl_, 450, "L", TabM=1) or ApprovalCheck(Girl_, 800, "O", TabM=2, Bonus = (B/3)): 
            #if she likes you, but is very obedient
            call NewGirl_Face(Girl_,"sexy")
            "She takes a seat off to the side and watches."          
            $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 90, 5) 
            $ newgirl[Girl_].Inbt = Statupdate(Girl_, "Inbt", newgirl[Girl_].Inbt, 90, 5)  
            $ newgirl[Girl_].Lust = Statupdate(Girl_, "Lust", newgirl[Girl_].Lust, 90, 2)  
            if Other == "Rogue" and "poly rogue" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly rogue") 
            elif Other == "Kitty" and "poly kitty" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly kitty") 
            elif Other == "Emma" and "poly emma" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly emma") 
            elif Other and ("poly " + Other) not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly " + Other)
            call NewGirl_Threeway_Set(Girl_, "watch")
    elif ApprovalCheck(Girl_, 650, "I", TabM=2) and ApprovalCheck(Girl_, 450, "L", TabM=1) or ApprovalCheck(Girl_, 800, "I", TabM=2, Bonus = (B/3)):
            #if she likes you, but is very uninhibited
            call NewGirl_Face(Girl_,"sexy")
            "She sits down and watches you intently."             
            $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 90, 5) 
            $ newgirl[Girl_].Obed = Statupdate(Girl_, "Obed", newgirl[Girl_].Obed, 90, 2)
            $ newgirl[Girl_].Inbt = Statupdate(Girl_, "Inbt", newgirl[Girl_].Inbt, 90, 2)     
            $ newgirl[Girl_].Lust = Statupdate(Girl_, "Lust", newgirl[Girl_].Lust, 90, 5) 
            if Other == "Rogue" and "poly rogue" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly rogue") 
            elif Other == "Kitty" and "poly kitty" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly kitty") 
            elif Other == "Emma" and "poly emma" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly emma") 
            elif Other and ("poly " + Other) not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly " + Other)
            call NewGirl_Threeway_Set(Girl_, "watch")
    elif ApprovalCheck(Girl_, 1500, TabM=2, Bonus = B):
            call NewGirl_Face(Girl_,"perplexed", 1)
            "She looks a little annoyed, but she stays and watches."
            if newgirl[Girl_].Love >= newgirl[Girl_].Obed and newgirl[Girl_].Love >= newgirl[Girl_].Inbt:
                $ newgirl[Girl_].Obed = Statupdate(Girl_, "Obed", newgirl[Girl_].Obed, 90, 2)
                $ newgirl[Girl_].Inbt = Statupdate(Girl_, "Inbt", newgirl[Girl_].Inbt, 90, 2)                     
            elif newgirl[Girl_].Obed >= newgirl[Girl_].Inbt:
                $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 90, 2) 
                $ newgirl[Girl_].Inbt = Statupdate(Girl_, "Inbt", newgirl[Girl_].Inbt, 90, 2)   
            else:
                $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 90, 2) 
                $ newgirl[Girl_].Obed = Statupdate(Girl_, "Obed", newgirl[Girl_].Obed, 90, 1)
                $ newgirl[Girl_].Inbt = Statupdate(Girl_, "Inbt", newgirl[Girl_].Inbt, 90, 1) 
            $ newgirl[Girl_].Lust = Statupdate(Girl_, "Lust", newgirl[Girl_].Lust, 90, 5)
            call NewGirl_Threeway_Set(Girl_, "watch")
    elif ApprovalCheck(Girl_, 650, "L", TabM=1) or ApprovalCheck(Girl_, 400, "O", TabM=2):
            #if she likes you or is obedient, but not enough
            call NewGirl_Face(Girl_,"angry", 2)
            if bg_current == ("bg " + Girl_): 
                    "She looks betrayed, and kicks you both out of the room."
            else:
                    "She looks betrayed, and storms out of the room."                   
            $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 200, -5) 
            $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 80, -5) 
            $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 70, -5) 
            $ newgirl[Girl_].Obed = Statupdate(Girl_, "Obed", newgirl[Girl_].Obed, 90, -5)
            $ newgirl[Girl_].Lust = Statupdate(Girl_, "Lust", newgirl[Girl_].Lust, 89, 10) 
            if Other == "Rogue" and "saw with rogue" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("saw with rogue") 
            elif Other == "Kitty" and "saw with kitty" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("saw with kitty")
            elif Other == "Emma" and "saw with emma" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("saw with emma") 
            elif Other and ("saw with " + Other) not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("saw with " + Other) 
            $ Partner = 0
            if bg_current == ("bg " + Girl_): #Kicks you out if in Girl_'s room
                    $ newgirl[Girl_].RecentActions.append("angry")
                    call GirlsAngry
            call Remove_Girl(Girl_)
    else:
            #if she doesn't like you much
            call NewGirl_Face(Girl_,"surprised", 2)
            $ newgirl[Girl_].Inbt = Statupdate(Girl_, "Inbt", newgirl[Girl_].Inbt, 90, 2) 
            $ newgirl[Girl_].Lust = Statupdate(Girl_, "Lust", newgirl[Girl_].Lust, 40, 20)
            if Trigger != "kissing":
                    $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 90, -10) 
                    $ newgirl[Girl_].Obed = Statupdate(Girl_, "Obed", newgirl[Girl_].Obed, 90, -5)
                    $ newgirl[Girl_].Lust = Statupdate(Girl_, "Lust", newgirl[Girl_].Lust, 80, 10)
            if bg_current == ("bg " + Girl_):
                    $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 90, -5) 
                    $ newgirl[Girl_].Obed = Statupdate(Girl_, "Obed", newgirl[Girl_].Obed, 90, -5)
                    "She looks annoyed, and shoves you both out of the room."                 
            elif Trigger != "kissing":
                "She looks annoyed, and storms out of the room." 
            else:
                "She looks a bit disgusted and walks away."                                  
            $ Partner = 0      
            if bg_current == ("bg " + Girl_): #Kicks you out if in Girl_'s room
                    $ newgirl[Girl_].RecentActions.append("angry")
                    call GirlsAngry
            call Remove_Girl(Girl_)
    return

label NewGirl_Face(Girl_ = "Mystique", Emote = "normal", B = 0, M = 0, Mouth = 0, Eyes = 0, Brows = 0):

        # Emote is the chosen emote, B is the lush state, and M is whether the character is in a  manic state 
        if (newgirl[Girl_].Forced or "angry" in newgirl[Girl_].RecentActions) and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "angry"     
        elif newgirl[Girl_].ForcedCount and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "sad"  
            
        if Emote == "normal":
                $ newgirl[Girl_].Mouth = "normal"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "normal"
        elif Emote == "angry":
                $ newgirl[Girl_].Mouth = "sad"
                $ newgirl[Girl_].Brows = "angry"
                $ newgirl[Girl_].Eyes = "sexy"
        elif Emote == "bemused":
                $ newgirl[Girl_].Mouth = "normal"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "closed":
                $ newgirl[Girl_].Mouth = "normal"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "closed"  
        elif Emote == "confused":
                $ newgirl[Girl_].Mouth = "kiss"
                $ newgirl[Girl_].Brows = "confused"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "kiss":
                $ newgirl[Girl_].Mouth = "kiss"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "closed"
        elif Emote == "tongue":
                $ newgirl[Girl_].Mouth = "tongue"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "stunned" #"stunned"
        elif Emote == "manic":
                $ newgirl[Girl_].Mouth = "smile"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "surprised"
                $ newgirl[Girl_].Blush = 1
        elif Emote == "sad":
                $ newgirl[Girl_].Mouth = "sad"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "sexy"
        elif Emote == "sadside":
                $ newgirl[Girl_].Mouth = "sad"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "side"
        elif Emote == "sexy":
                $ newgirl[Girl_].Mouth = "lipbite"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "smile":
                $ newgirl[Girl_].Mouth = "smile"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "normal"
        elif Emote == "sucking":
                $ newgirl[Girl_].Mouth = "sucking"
                $ newgirl[Girl_].Brows = "surprised"
                $ newgirl[Girl_].Eyes = "closed"
        elif Emote == "surprised":
                $ newgirl[Girl_].Mouth = "kiss"
                $ newgirl[Girl_].Brows = "surprised"
                $ newgirl[Girl_].Eyes = "surprised"
        elif Emote == "startled":
                $ newgirl[Girl_].Mouth = "smile"
                $ newgirl[Girl_].Brows = "surprised"
                $ newgirl[Girl_].Eyes = "surprised"
        elif Emote == "down":
                $ newgirl[Girl_].Mouth = "sad"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "down"  
        elif Emote == "perplexed":
                $ newgirl[Girl_].Mouth = "smile"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "normal"
        elif Emote == "sly":
                $ newgirl[Girl_].Mouth = "smirk"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "grimace":
                $ newgirl[Girl_].Mouth = "grimace"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "laugh":
                $ newgirl[Girl_].Mouth = "grimace"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "closed"
            
        if M:
                $ newgirl[Girl_].Eyes = "surprised"        
        if B > 1:
                $ newgirl[Girl_].Blush = 2
        elif B:
                $ newgirl[Girl_].Blush = 1
        else:
                $ newgirl[Girl_].Blush = 0
        
        if Mouth:
                $ newgirl[Girl_].Mouth = Mouth
        if Eyes:
                $ newgirl[Girl_].Eyes = Eyes
        if Brows:
                $ newgirl[Girl_].Brows = Brows
        
        return


label NewGirl_FaceSpecial(Girl_ = "Mystique", Emote = "normal", B = 0, M = 0, Mouth = 0, Eyes = 0, Brows = 0):

        # Emote is the chosen emote, B is the lush state, and M is whether the character is in a  manic state 
            
        if Emote == "normal":
                $ newgirl[Girl_].Mouth = "normal"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "normal"
        elif Emote == "angry":
                $ newgirl[Girl_].Mouth = "sad"
                $ newgirl[Girl_].Brows = "angry"
                $ newgirl[Girl_].Eyes = "sexy"
        elif Emote == "bemused":
                $ newgirl[Girl_].Mouth = "normal"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "closed":
                $ newgirl[Girl_].Mouth = "normal"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "closed"  
        elif Emote == "confused":
                $ newgirl[Girl_].Mouth = "kiss"
                $ newgirl[Girl_].Brows = "confused"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "kiss":
                $ newgirl[Girl_].Mouth = "kiss"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "closed"
        elif Emote == "tongue":
                $ newgirl[Girl_].Mouth = "tongue"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "stunned" #"stunned"
        elif Emote == "manic":
                $ newgirl[Girl_].Mouth = "smile"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "surprised"
                $ newgirl[Girl_].Blush = 1
        elif Emote == "sad":
                $ newgirl[Girl_].Mouth = "sad"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "sexy"
        elif Emote == "sadside":
                $ newgirl[Girl_].Mouth = "sad"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "side"
        elif Emote == "sexy":
                $ newgirl[Girl_].Mouth = "lipbite"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "smile":
                $ newgirl[Girl_].Mouth = "smile"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "normal"
        elif Emote == "sucking":
                $ newgirl[Girl_].Mouth = "sucking"
                $ newgirl[Girl_].Brows = "surprised"
                $ newgirl[Girl_].Eyes = "closed"
        elif Emote == "surprised":
                $ newgirl[Girl_].Mouth = "kiss"
                $ newgirl[Girl_].Brows = "surprised"
                $ newgirl[Girl_].Eyes = "surprised"
        elif Emote == "startled":
                $ newgirl[Girl_].Mouth = "smile"
                $ newgirl[Girl_].Brows = "surprised"
                $ newgirl[Girl_].Eyes = "surprised"
        elif Emote == "down":
                $ newgirl[Girl_].Mouth = "sad"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "down"  
        elif Emote == "perplexed":
                $ newgirl[Girl_].Mouth = "smile"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "normal"
        elif Emote == "sly":
                $ newgirl[Girl_].Mouth = "smirk"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "grimace":
                $ newgirl[Girl_].Mouth = "grimace"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "laugh":
                $ newgirl[Girl_].Mouth = "grimace"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "closed"
            
        if M:
                $ newgirl[Girl_].Eyes = "surprised"        
        if B > 1:
                $ newgirl[Girl_].Blush = 2
        elif B:
                $ newgirl[Girl_].Blush = 1
        else:
                $ newgirl[Girl_].Blush = 0
        
        if Mouth:
                $ newgirl[Girl_].Mouth = Mouth
        if Eyes:
                $ newgirl[Girl_].Eyes = Eyes
        if Brows:
                $ newgirl[Girl_].Brows = Brows
        
        return

label NewGirl_Threeway_Set(Girl_ = "Mystique", Preset = 0, Mode = 0, Action = Trigger4, ActiveGirl = Primary, State = "watcher", TempLust = 0, TempLust2 = 0, TempFocus = 0):
    # Action defaults to Trigger4, the action of the seondary girl and ActiveGirl to the lead girl in the scene
    # In lesbian mode, Action becomes Trigger3, the secondary action of the primary girl, and ActiveGirl is the secondary girl
    # If Set gets passed a preset, it chooses that preset, otherwise it chooses one randomly
    # for Lesbian: NewGirl_Threeway_Set("activity", "lesbian", Trigger3, Girl)
    # for Threeway: NewGirl_Threeway_Set("activity", 0, Trigger4, Girl)
    
            if Mode == "lesbian" and Trigger3:
                    #If it's in lesbian mode, there is already a trigger set, and the roll is good, continue
                    if 5 <= D20S <= 15:
                            return
                    if Trigger3 == "kissing" and K_Lust <= 30:
                            # If kissing at low lust, keep doing it
                            return
            elif Trigger4 and D20S < 10 and Trigger4 != "watch": 
                    #If there is a trigger, it's not set to "watch," and the roll is good, continue
                    return
                    
            $ Options = ["watch", "masturbation", "masturbation", "masturbation"]
                        
            if Trigger == "lesbian":
                    $ State = "lesbian"
                    if Secondary != Girl_:
                            $ ActiveGirl = Secondary
                    $ Options = ["kiss girl","kiss girl","fondle ass"]                    
            elif not ApprovalCheck(Girl_, 500, "I"): # If Girl_ is too timid to do anything
                    pass
            elif Primary == "Rogue":
                    if newgirl[Girl_].LikeRogue >= 500 and ApprovalCheck(Girl_, (1300-(10*newgirl[Girl_].Les)-(10*(newgirl[Girl_].LikeRogue-60)))): #If she likes both of you a lot, threeway
                            $ State = "threeway"
                    elif ApprovalCheck(Girl_, 1000): #If she likes you well enough, Hetero
                            $ State = "hetero"            
                    elif newgirl[Girl_].LikeRogue >= 700: #if she doesn't like you but likes Rogue, lesbian
                            $ State = "lesbian"
            elif Primary == "Kitty":
                    if newgirl[Girl_].LikeKitty >= 500 and ApprovalCheck(Girl_, (1300-(10*newgirl[Girl_].Les)-(10*(newgirl[Girl_].LikeKitty-60)))): #If she likes both of you a lot, threeway
                            $ State = "threeway"
                    elif ApprovalCheck(Girl_, 1000): #If she likes you well enough, Hetero
                            $ State = "hetero"            
                    elif newgirl[Girl_].LikeKitty >= 700: #if she doesn't like you but likes Kitty, lesbian
                            $ State = "lesbian"
            elif Primary == "Emma":
                    if newgirl[Girl_].LikeKitty >= 500 and ApprovalCheck(Girl_, (1300-(10*newgirl[Girl_].Les)-(10*(newgirl[Girl_].LikeKitty-60)))): #If she likes both of you a lot, threeway
                            $ State = "threeway"
                    elif ApprovalCheck(Girl_, 1000): #If she likes you well enough, Hetero
                            $ State = "hetero"            
                    elif newgirl[Girl_].LikeKitty >= 700: #if she doesn't like you but likes Kitty, lesbian
                            $ State = "lesbian"
            else:
                #$ k = 0
                #while k < len(ModdedGirls):
                if Primary in ModdedGirls and Primary != Girl_:
                    if newgirl[Girl_].LikeOtherGirl[Primary] >= 500 and ApprovalCheck(Girl_, (1300-(10*newgirl[Girl_].Les)-(10*(newgirl[Girl_].LikeOtherGirl[Primary]-60)))): #If she likes both of you a lot, threeway
                        $ State = "threeway"
                    elif ApprovalCheck(Girl_, 1000): #If she likes you well enough, Hetero
                        $ State = "hetero"            
                    elif newgirl[Girl_].LikeOtherGirl[Primary] >= 700: #if she doesn't like you but likes Kitty, lesbian
                        $ State = "lesbian"    
                    #$ k += 1
            
            
            if State == "lesbian" or State == "threeway":
                $ Options.extend(("fondle breasts","suck breasts","fondle pussy","fondle ass","kiss girl")) 
                if ActiveGirl == "Rogue":
                            if ApprovalCheck(Girl_, 800, "I") or newgirl[Girl_].LikeRogue >= 700:
                                $ Options.append("lick pussy")
                            if ApprovalCheck(Girl_, 900, "I") and newgirl[Girl_].LikeRogue >= 800:
                                $ Options.append("lick ass")  
                elif ActiveGirl == "Kitty":
                            if ApprovalCheck(Girl_, 800, "I") or newgirl[Girl_].LikeKitty >= 700:
                                $ Options.append("lick pussy")
                            if ApprovalCheck(Girl_, 900, "I") and newgirl[Girl_].LikeKitty >= 800:
                                $ Options.append("lick ass") 
                elif ActiveGirl == "Emma":
                            if ApprovalCheck(Girl_, 800, "I") or newgirl[Girl_].LikeEmma >= 700:
                                $ Options.append("lick pussy")
                            if ApprovalCheck(Girl_, 900, "I") and newgirl[Girl_].LikeEmma >= 800:
                                $ Options.append("lick ass") 
                else:
                    # $ k = 0
                    # while k < len(ModdedGirls):
                    if ActiveGirl in ModdedGirls and ActiveGirl != Girl_:
                        if ApprovalCheck(Girl_, 800, "I") or newgirl[Girl_].LikeOtherGirl[ActiveGirl] >= 700:
                            $ Options.append("lick pussy")
                        if ApprovalCheck(Girl_, 900, "I") and newgirl[Girl_].LikeOtherGirl[ActiveGirl] >= 800:
                            $ Options.append("lick ass")     
                        # $ k += 1
                    
            if State == "hetero" or State == "threeway":
                    $ Options.extend(("hand","blow","kiss you"))                 
            $ renpy.random.shuffle(Options)
            
            if Preset in Options:
                    #if the suggested action is in the possible actions. . .
                    $ Options[0] = Preset 
                    ch_m "Oh, very well. . ."
            elif Preset:
                    ch_m "That doesn't really seem appropriate. . ."
                    
            #Sets opening lines. . .
            if Options[0] == Action:                          
                    #If it's the same result, just hop back
                    return
            elif Mode == "lesbian":
                    $ Line = Girl_ + " shifts her position"
            elif not Trigger4 or Trigger4 == "masturbation":    
                    #If this is the first action,
                    $ Line = Girl_ + " moves closer"            
            else:                                              
                    #If this is a new action
                    $ Line = Girl_ + " shifts her position"
                    
                    
            if Options[0] == "masturbation":
                        $ Action = "masturbation"  
                        if Trigger != "lesbian" and Trigger5 in ("kiss you", "kiss girl", "kiss both"):
                                #Clear out Trigger 5 if it's for kissing.  
                                $ Trigger5 = 0 
                        call NewGirl_Self_Lines(Girl_,"T5",Trigger5)
            elif Options[0] == "hand":
                        $ Line = Line + " before she slides her hand down and firmly grabs your dick"
                        $ Action = "hand"   
                        
                        $ TempFocus += 3 if P_Focus > 70 else 2                              
                        $ TempLust += 2 if newgirl[Girl_].Lust < 60 else 0
                        $ TempLust += 2 if newgirl[Girl_].Hand > 2 else 0
                        $ newgirl[Girl_].Addict -= 1 if D20S > 10 else 2
            elif Options[0] == "blow":
                        $ Line = Line + " before she slides down and begins to slowly lick your cock"
                        $ Action = "blow"  
                        
                        $ TempFocus += 20 if P_Focus > 60 else 10                      
                        $ TempLust += 2 if newgirl[Girl_].Lust > 80 else 1  
                        $ newgirl[Girl_].Addict -= 2
            #the above three do not apply to lesbian actions.
                        
            elif Options[0] == "fondle breasts":
                        # call RThreewayBreasts_Launch #Launches position change
                        $ Line = Line + " and slides her hands along " + ActiveGirl + "'s breasts" 
                        $ Action = "fondle breasts"   
                        if "lesbian" not in newgirl[Girl_].RecentActions:
                                $ newgirl[Girl_].Les += 1
                                $ newgirl[Girl_].RecentActions.append("lesbian") 
                        if ActiveGirl == "Rogue": #If Girl_ is fondling Rogue's breasts
                                $ TempLust += 2 if ApprovalCheck(Girl_, 500, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 4 if R_LikeNewGirl[Girl_] >= 800 else 2
                        elif ActiveGirl == "Kitty": #If Girl_ is fondling Kitty's breasts
                                $ TempLust += 2 if ApprovalCheck(Girl_, 500, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 4 if K_LikeNewGirl[Girl_] >= 800 else 2
                        elif ActiveGirl == "Emma": #If Girl_ is fondling Emma's breasts
                                $ TempLust += 2 if ApprovalCheck(Girl_, 500, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 4 if E_LikeNewGirl[Girl_] >= 800 else 2
                        elif ActiveGirl in ModdedGirls and ActiveGirl != Girl_:
                                $ TempLust += 2 if ApprovalCheck(Girl_, 500, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 4 if newgirl[ActiveGirl].LikeNewGirl[Girl_] >= 800 else 2
                        $ TempFocus += 1 
            elif Options[0] == "suck breasts":
                        # call RThreewayBreasts_Launch #Launches position change
                        $ Line = Line + " and slurps " + ActiveGirl + "'s nipple into her mouth" 
                        $ Action = "suck breasts"    
                        if "lesbian" not in newgirl[Girl_].RecentActions:
                                $ newgirl[Girl_].Les += 1
                                $ newgirl[Girl_].RecentActions.append("lesbian") 
                        if ActiveGirl == "Rogue": #If Girl_ is fondling Rogue's breasts
                                $ TempLust += 2 if ApprovalCheck(Girl_, 500, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 4 if R_LikeNewGirl[Girl_] >= 800 else 2
                        elif ActiveGirl == "Kitty": #If Girl_ is sucking Kitty's breasts
                                $ TempLust += 2 if ApprovalCheck(Girl_, 500, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 5 if K_LikeNewGirl[Girl_] >= 800 else 2
                        elif ActiveGirl == "Emma": #If Girl_ is fondling Emma's breasts
                                $ TempLust += 2 if ApprovalCheck(Girl_, 500, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 5 if E_LikeNewGirl[Girl_] >= 800 else 2
                        elif ActiveGirl in ModdedGirls and ActiveGirl != Girl_:
                                $ TempLust += 2 if ApprovalCheck(Girl_, 500, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 5 if newgirl[ActiveGirl].LikeNewGirl[Girl_] >= 800 else 2
                        $ TempFocus += 1  
            elif Options[0] == "fondle pussy":
                        # call RThreewayPussy_Launch #Launches position change
                        $ Line = Line + " and runs her finger along " + ActiveGirl + "'s pussy" 
                        $ Action = "fondle pussy"  
                        if "lesbian" not in newgirl[Girl_].RecentActions:
                                $ newgirl[Girl_].Les += 1
                                $ newgirl[Girl_].RecentActions.append("lesbian")                         
                        if ActiveGirl == "Rogue": #If Girl_ is fondling Rogue's breasts
                                $ TempLust += 2 if ApprovalCheck(Girl_, 500, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 5 if R_LikeNewGirl[Girl_] >= 800 else 4
                        elif ActiveGirl == "Kitty": #If Girl_ is stroking Kitty's pussy
                                $ TempLust += 2 if ApprovalCheck(Girl_, 500, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 5 if K_LikeNewGirl[Girl_] >= 800 else 3
                        elif ActiveGirl == "Emma": #If Girl_ is fondling Emma's breasts
                                $ TempLust += 2 if ApprovalCheck(Girl_, 500, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 5 if E_LikeNewGirl[Girl_] >= 800 else 3
                        elif ActiveGirl in ModdedGirls and ActiveGirl != Girl_:
                                $ TempLust += 2 if ApprovalCheck(Girl_, 500, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 5 if newgirl[ActiveGirl].LikeNewGirl[Girl_] >= 800 else 3
                        $ TempFocus += 2  
            elif Options[0] == "lick pussy":
                        # call RThreewayPussy_Launch #Launches position change
                        $ Line = Line + " and runs her tongue along " + ActiveGirl + "'s pussy" 
                        $ Action = "lick pussy"  
                        if "lesbian" not in newgirl[Girl_].RecentActions:
                                $ newgirl[Girl_].Les += 1
                                $ newgirl[Girl_].RecentActions.append("lesbian") 
                        if ActiveGirl == "Rogue": #If Girl_ is fondling Rogue's breasts
                                $ TempLust += 3 if ApprovalCheck(Girl_, 600, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 7 if R_LikeNewGirl[Girl_] >= 800 else 4
                        elif ActiveGirl == "Kitty": #If Girl_ is licking Kitty's pussy
                                $ TempLust += 3 if ApprovalCheck(Girl_, 600, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 7 if K_LikeNewGirl[Girl_] >= 800 else 4
                        elif ActiveGirl == "Emma": #If Girl_ is fondling Emma's breasts
                                $ TempLust += 3 if ApprovalCheck(Girl_, 600, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 7 if E_LikeNewGirl[Girl_] >= 800 else 4
                        elif ActiveGirl in ModdedGirls and ActiveGirl != Girl_:
                                $ TempLust += 3 if ApprovalCheck(Girl_, 600, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 7 if newgirl[ActiveGirl].LikeNewGirl[Girl_] >= 800 else 4
                        $ TempFocus += 3  
            elif Options[0] == "fondle ass": 
                        # call RThreewayPussy_Launch #Launches position change
                        $ Line = Line + " and gives " + ActiveGirl + "'s ass a firm squeeze" 
                        $ Action = "fondle ass" 
                        if "lesbian" not in newgirl[Girl_].RecentActions:
                                $ newgirl[Girl_].Les += 1
                                $ newgirl[Girl_].RecentActions.append("lesbian")                         
                        if ActiveGirl == "Rogue": #If Girl_ is fondling Rogue's breasts
                                $ TempLust += 1 if ApprovalCheck(Girl_, 400, "I") else 0  # Girl_'s lust
                                $ TempLust2 += 3 if R_LikeNewGirl[Girl_] >= 800 else 1
                        elif ActiveGirl == "Kitty": #If Girl_ is fondling Kitty's ass
                                $ TempLust += 1 if ApprovalCheck(Girl_, 400, "I") else 0  # Girl_'s lust
                                $ TempLust2 += 3 if K_LikeNewGirl[Girl_] >= 600 else 1
                        elif ActiveGirl == "Emma": #If Girl_ is fondling Emma's breasts
                                $ TempLust += 1 if ApprovalCheck(Girl_, 400, "I") else 0  # Girl_'s lust
                                $ TempLust2 += 3 if E_LikeNewGirl[Girl_] >= 600 else 1
                        elif ActiveGirl in ModdedGirls and ActiveGirl != Girl_:
                                $ TempLust += 1 if ApprovalCheck(Girl_, 400, "I") else 0  # Girl_'s lust
                                $ TempLust2 += 3 if newgirl[ActiveGirl].LikeNewGirl[Girl_] >= 600 else 1
                        $ TempFocus += 1  
            elif Options[0] == "lick ass":
                        # call RThreewayPussy_Launch #Launches position change
                        $ Line = Line + " and starts to lick around " + ActiveGirl + "'s ass" 
                        $ Action = "lick ass"  
                        if "lesbian" not in newgirl[Girl_].RecentActions:
                                $ newgirl[Girl_].Les += 1
                                $ newgirl[Girl_].RecentActions.append("lesbian") 
                        if ActiveGirl == "Rogue": #If Girl_ is fondling Rogue's breasts
                                $ TempLust += 3 if ApprovalCheck(Girl_, 800, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 5 if R_LikeNewGirl[Girl_] >= 800 else 2
                                $ TempLust2 += 2 if R_Loose > 1 else 0
                        elif ActiveGirl == "Kitty": #If Girl_ is licking Kitty's ass
                                $ TempLust += 3 if ApprovalCheck(Girl_, 800, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 5 if K_LikeNewGirl[Girl_] >= 800 else 2
                                $ TempLust2 += 2 if K_Loose > 1 else 0
                        elif ActiveGirl == "Emma": #If Girl_ is fondling Emma's breasts
                                $ TempLust += 3 if ApprovalCheck(Girl_, 800, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 5 if E_LikeNewGirl[Girl_] >= 800 else 2
                                $ TempLust2 += 2 if E_Loose > 1 else 0
                        elif ActiveGirl in ModdedGirls and ActiveGirl != Girl_:
                                $ TempLust += 3 if ApprovalCheck(Girl_, 800, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 5 if newgirl[ActiveGirl].LikeNewGirl[Girl_] >= 800 else 2
                                $ TempLust2 += 2 if newgirl[ActiveGirl].Loose > 1 else 0
                        $ TempFocus += 2  
                        
            elif Options[0] == "kiss girl" or Mode == "lesbian":   
                        # call RThreewayBreasts_Launch #Launches position change                                
                        $ Line = Line + " and gives " + ActiveGirl + " a passionate kiss" #use T5 on this to choose targets
                        $ Action = "kissing"  
                        if Mode != "lesbian":
                            if "kiss you" in Options:
                                $ Trigger5 = "kiss both" 
                            else:
                                $ Trigger5 = "kiss girl"  
                        if "lesbian" not in newgirl[Girl_].RecentActions:
                                $ newgirl[Girl_].Les += 1
                                $ newgirl[Girl_].RecentActions.append("lesbian") 
                        if ActiveGirl == "Rogue": #If Girl_ is kissing Rogue
                                $ TempLust += 1 if ApprovalCheck(Girl_, 500, "I") else 0  # Girl_'s lust
                                $ TempLust += 1 if newgirl[Girl_].LikeRogue >= 800 else 0
                                $ TempLust2 += 2 if R_LikeNewGirl[Girl_] >= 800 else 1
                        elif ActiveGirl == "Kitty": #If Girl_ is kissing Kitty
                                $ TempLust += 1 if ApprovalCheck(Girl_, 500, "I") else 0  # Girl_'s lust
                                $ TempLust += 1 if newgirl[Girl_].LikeKitty >= 800 else 0
                                $ TempLust2 += 2 if K_LikeNewGirl[Girl_] >= 800 else 1
                        elif ActiveGirl == "Emma": #If Girl_ is Kissing Emma
                                $ TempLust += 1 if ApprovalCheck(Girl_, 500, "I") else 0  # Girl_'s lust
                                $ TempLust += 1 if newgirl[Girl_].LikeEmma >= 800 else 0
                                $ TempLust2 += 2 if E_LikeNewGirl[Girl_] >= 800 else 1
                        elif ActiveGirl in ModdedGirls and ActiveGirl != Girl_:
                                $ TempLust += 1 if ApprovalCheck(Girl_, 500, "I") else 0  # Girl_'s lust
                                $ TempLust += 1 if newgirl[Girl_].LikeNewGirl[ActiveGirl] >= 800 else 0
                                $ TempLust2 += 2 if newgirl[ActiveGirl].LikeNewGirl[Girl_] >= 800 else 1
                        $ TempFocus += 1  
            elif Options[0] == "kiss you":   
                        # call RThreewayBreasts_Launch #Launches position change
                        $ Line = Line + " and gives you a passionate kiss" #use T5 on this to choose targets
                        $ Action = "kissing"   
                        if "kiss girl" in Options:
                            $ Trigger5 = "kiss both" 
                            if "lesbian" not in newgirl[Girl_].RecentActions:
                                    $ newgirl[Girl_].Les += 1
                                    $ newgirl[Girl_].RecentActions.append("lesbian")                                     
                            if ActiveGirl == "Rogue": #If Girl_ is fondling Rogue's breasts
                                    $ TempLust += 1 if ApprovalCheck(Girl_, 500, "I") else 0  # Girl_'s lust
                                    $ TempLust += 1 if newgirl[Girl_].LikeRogue >= 800 else 0
                                    $ TempLust2 += 2 if R_LikeNewGirl[Girl_] >= 800 else 1
                            elif ActiveGirl == "Kitty": #If Girl_ is kissing Kitty
                                    $ TempLust += 1 if ApprovalCheck(Girl_, 500, "I") else 0  # Girl_'s lust
                                    $ TempLust += 1 if newgirl[Girl_].LikeKitty >= 800 else 0
                                    $ TempLust2 += 2 if K_LikeNewGirl[Girl_] >= 800 else 1
                            elif ActiveGirl == "Emma": #If Girl_ is Kissing Emma
                                    $ TempLust += 1 if ApprovalCheck(Girl_, 500, "I") else 0  # Girl_'s lust
                                    $ TempLust += 1 if newgirl[Girl_].LikeEmma >= 800 else 0
                                    $ TempLust2 += 2 if E_LikeNewGirl[Girl_] >= 800 else 1
                            elif ActiveGirl in ModdedGirls and ActiveGirl != Girl_:
                                    $ TempLust += 1 if ApprovalCheck(Girl_, 500, "I") else 0  # Girl_'s lust
                                    $ TempLust += 1 if newgirl[Girl_].LikeNewGirl[ActiveGirl] >= 800 else 0
                                    $ TempLust2 += 2 if newgirl[ActiveGirl].LikeNewGirl[Girl_] >= 800 else 1
                            $ TempFocus += 1 
                        else:
                            $ Trigger5 = "kiss you" 
                        $ TempLust += 1 
                        $ TempFocus += 1 
                        
            # elif Options[0] == "dildo pussy":  
            # elif Options[0] == "dildo ass":        
            # elif Options[0] == "vibrator":    

            else:
                        "[Girl_] is just watching the two of you intently."
                        $ Action = "watch"
                        if ActiveGirl == "Rogue": #If Girl_ is fondling Rogue's breasts
                                $ TempLust += 1 if newgirl[Girl_].LikeRogue >= 600 else 0  # Girl_'s lust
                                $ TempLust += 2 if newgirl[Girl_].LikeRogue >= 800 else 1  # Girl_'s lust
                                $ TempLust2 += 1 if ApprovalCheck("Rogue", 500, "I") else 0
                                $ TempLust2 += 1 if ApprovalCheck("Rogue", 700, "I") else 0
                        elif ActiveGirl == "Kitty": #If Girl_ is watching Kitty
                                $ TempLust += 1 if newgirl[Girl_].LikeKitty >= 600 else 0  # Girl_'s lust
                                $ TempLust += 2 if newgirl[Girl_].LikeKitty >= 800 else 1  # Girl_'s lust
                                $ TempLust2 += 1 if ApprovalCheck("Kitty", 500, "I") else 0
                                $ TempLust2 += 1 if ApprovalCheck("Kitty", 700, "I") else 0
                        elif ActiveGirl == "Emma": #If Girl_ is watching Emma
                                $ TempLust += 1 if newgirl[Girl_].LikeEmma >= 600 else 0
                                $ TempLust += 2 if newgirl[Girl_].LikeEmma >= 800 else 1
                                $ TempLust += 1 if ApprovalCheck("Emma", 500, "I") else 0  # Girl_'s lust
                                $ TempLust += 1 if ApprovalCheck("Emma", 700, "I") else 0  # Girl_'s lust
                        elif ActiveGirl in ModdedGirls and ActiveGirl != Girl_:
                                $ TempLust += 1 if newgirl[Girl_].LikeNewGirl[ActiveGirl] >= 600 else 0
                                $ TempLust += 2 if newgirl[Girl_].LikeNewGirl[ActiveGirl] >= 800 else 1
                                $ TempLust += 1 if ApprovalCheck(Girl_, 500, "I") else 0  # Girl_'s lust
                                $ TempLust += 1 if ApprovalCheck(Girl_, 700, "I") else 0  # Girl_'s lust
                        $ TempFocus += 1 
                 
            # Wrap-up
            $ TempLust2 += 2       
            if Mode == "lesbian":
                #Sets Primary Girl's secondary action
                $ Trigger3 = Action
                $ PrimaryLust += TempLust
                $ SecondaryLust += TempLust2
            else:
                #Sets Secondary girl's action
                $ Trigger4 = Action
                $ SecondaryLust += TempLust
                $ PrimaryLust += TempLust2
            $ P_Focus += TempFocus

            return

label NewGirl_Self_Lines(Girl_ = "Mystique", Mode = "T3", Action = Trigger3, TempLustX = 0): 
    # The Mode can be T3 for Trigger 3 for a masturbation option, or T5/Trigger5 if it's setting a Threeway action. 
    # call NewGirl_Self_Lines("T5",Trigger5) 
    # This sets a Action if there isn't one, or sets an intitial line
    $ Line = 0
    if not Action or D20S >= 15: 
            if Trigger != "masturbation" and "passive" in newgirl[Girl_].Traits:
                    # This bypasses self-set if Girl_ is told not to take initiative
                    $ Line = 0
                    return            
            call Mystique_Self_Set(Mode, Action)
            
            if Mode == "T3": #Sets Action based on the result
                    $ Action = Trigger3
            else: #if Mode == "T5"
                    $ Action = Trigger5  
            if not Action: 
                    return
            elif (newgirl[Girl_].Over == "bondage" or newgirl[Girl_].Over == "bondage cuffs" or newgirl[Girl_].Over == "armbinder") and not Line:
                    $ Line = "Also, " + Girl_ + "continues stroke your cock. "
            elif Action == "hand" and not Line: 
                    $ Line = "Also, " + Girl_ + " continues stroke your cock. "
            elif not Line:        
                    $ Line = "Also, " + Girl_ + " continues to masturbate. "      
    elif Action == "hand": 
            $ Line = "" + Girl_ + " continues stroke your cock. "
    elif newgirl[Girl_].Over == "bondage" or newgirl[Girl_].Over == "bondage cuffs" or newgirl[Girl_].Over == "armbinder": 
            $ Line = renpy.random.choice(["" + Girl_ + " tries to move her arms around. ", 
                    "" + Girl_ + " can't keep still. ",
                    "" + Girl_ + " can't keep still. "])
    else:       
            $ Line = renpy.random.choice(["" + Girl_ + " continues to masturbate. ", 
                    "" + Girl_ + "'s hands move across her body. ",
                    "" + Girl_ + " continues to feel herself. ",
                    "" + Girl_ + " can't keep still. "]) 
            
    if Action == "hand": 
            $ Line = Line + renpy.random.choice(["She lightly strokes the shaft, fingers sliding along the vein", 
                    "She grasps the shaft firmly, and slowly slides along its length", 
                    "She's becoming something of a handjob expert, making up for years of lost time",
                    "Her expert strokes will have you boiling over in seconds",
                    "She strokes the shaft vigorously, lightly touching the tip",
                    "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                    "Her hand slides slowly down your shaft"]) 
            $ TempFocus += 10 if P_Focus > 60 else 4
            $ TempFocus += 2 if newgirl[Girl_].Hand > 2 else 0
                    
            $ TempLustX += 2 if newgirl[Girl_].Lust < 60 else 1
            $ TempLustX += 2 if newgirl[Girl_].Hand > 2 else 0
            $ newgirl[Girl_].Addict -= 1            
    else:
        if newgirl[Girl_].Lust >= 80:   
            if Action == "fondle pussy":
                    $ Line = Line + renpy.random.choice(["Her hand rapidly moves across her mound, firmly stroking her clit", 
                            "She inserts two fingers into her dripping pussy and rapidly pistons them",
                            "She gasps as her fingers bury themselves deeply inside her",
                            "She gives a little squeal as she pinches her clit between her fingers",           
                            "She fingers move quickly across her mound, constantly sliding across her clit",
                            "She fingers move rapidly up and down her inner thighs and belly, building towards their center",
                            "She spreads her lower lips and furiously strokes the inner lining",
                            "She alternately dives her fingers into herself, and licks the juices off of them",
                            "She slides two fingers firmly in and out of her tight gap as she massages the clit with her palm",
                            "She rapidly circles her fingers against her erect clit",
                            "She quickly slides a finger up and down the crease of her pussy", 
                            "She lets out a moan as her fingers brush against her erect clit"])
            elif Action == "dildo pussy":
                    $ Line = Line + renpy.random.choice(["She moves the dildo in circles across her mound, firmly rubbing into it", 
                            "She hungrily slams the dildo into her tight pussy, and pistons it in and out",
                            "She shoves the dildo firmly in and out of her grasping pussy",               
                            "She quickly slides the phallus up and down her crease"])
            elif Action == "fondle ass":
                    $ Line = Line + renpy.random.choice(["Her hand rapidly moves across her ass, firmly stroking her tight hole", 
                            "She inserts a finger deep into her grasping hole and rapidly pistons it",
                            "She gasps as she buries a finger deeply into her tight anus",
                            "She gives a little squeal as she pinches her clit between her fingers",           
                            "Her fingers move quickly across her ass, constantly sliding across her rim",
                            "Her fingers move rapidly up and down her inner thighs and ass, building towards their center",
                            "She spreads her cheeks and furiously strokes the puckered rim",
                            "She slides two fingers firmly in and out of her tight hole",
                            "She rapidly circles her fingers against the sensitive rim",
                            "She lets out a moan as her fingers brush against her quivering hole"])
            elif Action == "dildo anal":
                    $ Line = Line + renpy.random.choice(["She moves the dildo in circles across her ass, firmly rubbing into it", 
                            "She hungrily slams the dildo into her tight hole, and pistons it in and out",
                            "She shoves the dildo firmly in and out of her grasping asshole",               
                            "She quickly slides the phallus up and down the crease of her ass"])
            elif Action == "vibrator pussy":
                    $ Line = Line + renpy.random.choice(["She traces the buzzing ball slowly down her body, barely grazing her mound",                 
                            "Her vibrator slides lightly across her pubic region, subtly avoiding her lips",
                            "She slides the buzzing egg into her dripping pussy and tugs it in and out",    
                            "She presses the vibrator firmly against her clit and a shiver runs through her",                
                            "Her whirring toy is dragged up and down her inner thighs, slowing building towards their center",
                            "She  spreads her lower lips and runs the device along the inner lining",
                            "She presses the toy deep into her and the vibrations send a shock through her body"])
            else: # Action == "fondle breasts"
                    $ Line = Line + renpy.random.choice(["She passionately rubs her breasts, desperately tugging at her nipples",
                            "Her hands squeeze at her breasts, massaging them firmly with both hands",                 
                            "She hungrily cups her breasts and moves them in rapid circles",
                            "Her hands move constantly across her chest, alternately pulling at her nipples or just grazing her skin",
                            "She firmly pinches her nipples and gives them steady tugs",
                            "She passionately rubs her breasts, desperately tugging at her nipples"])     
            #End newgirl[Girl_].Lust >= 80
            
                
        elif newgirl[Girl_].Lust >= 50:   
                if Action == "fondle pussy":
                        $ Line = Line + renpy.random.choice(["Her hand moves in circles across her mound, firmly rubbing into it", 
                                "Her hands move along her sides, carefully caressing them",                
                                "Her fingers move smoothly across her delta, occasionally grazing her lips",
                                "Her fingers move up and down her inner thighs, slowing building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She gently slides a finger up and down the crease of her pussy", 
                                "She lets out a gasp as her fingers brush against her erect clit"])
                elif Action == "dildo pussy":
                        $ Line = Line + renpy.random.choice(["She moves the dildo in circles across her mound, firmly rubbing into it",  
                                "She traces the rubber phallus slowly down her body, barely grazing her mound",  
                                "Her dildo slides lightly across her pubic region, subtly avoiding her lips",
                                "Her dildo is dragged up and down her inner thighs, slowing building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",                
                                "She gently slides the phallus up and down the crease of her pussy", 
                                "She drags the dildo slowly along her sides, carefully caressing them"])
                elif Action == "fondle ass":
                        $ Line = Line + renpy.random.choice(["Her hand moves in circles across her ass, firmly rubbing into it", 
                                "Her hands move along her sides, carefully caressing them",                
                                "Her fingers move smoothly along her crack, occasionally grazing her asshole",
                                "Her fingers move up and down her inner thighs, slowing building towards their center",
                                "She slowly spreads her cheeks and caresses the tight hole within",
                                "She gently slides a finger up and down the crease of ass", 
                                "She lets out a gasp as her fingers brush against her puckered hole"]) 
                elif Action == "dildo anal":
                        $ Line = Line + renpy.random.choice(["She traces the rubber phallus slowly down her body, barely grazing her ass",                 
                                "Her dildo slides lightly across her crack, subtly avoiding the hole",
                                "Her dildo is dragged up and down her inner thighs, slowing building towards their center",
                                "She slowly spreads her cheeks and caresses the rim beneath",
                                "She drags the dildo slowly along her sides, carefully caressing them"])
                elif Action == "vibrator pussy":
                        $ Line = Line + renpy.random.choice(["She traces the buzzing ball slowly down her body, barely grazing her mound",                 
                                "Her vibrator slides lightly across her pubic region, subtly avoiding her lips",
                                "Her whirring toy is dragged up and down her inner thighs, slowing building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She drags the vibrator slowly along her sides, carefully caressing them"])
                else: # Action == "fondle breasts"
                        $ Line = Line + renpy.random.choice(["She gently rubs her breasts, dragging a finger across her nipple",                  
                                "She gently cups her breasts and moves them in slow circles",
                                "She moves her hands from her breasts to rub her neck",
                                "She lightly pinches one of her nipples",
                                "Her hands firmly caress her breasts, massaging them in circular motions",
                                "Her hands move along her breasts, carefully caressing them",
                                "She gasps as her finger brushes against an erect nipple"])
                #End newgirl[Girl_].Lust >= 50
                
        else: #if newgirl[Girl_].Lust < 50:      
                if Action == "fondle pussy":
                        $ Line = Line + renpy.random.choice(["Her hand traces slowly down her body, barely grazing her mound", 
                                "Her fingers move lightly across her pubic region, subtly avoiding her lips",
                                "Her fingers move up and down her inner thighs, slowing building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "Her hands move along her sides, carefully caressing them"])  
                elif Action == "dildo pussy":
                        $ Line = Line + renpy.random.choice(["She traces the rubber phallus slowly down her body, barely grazing her mound",                 
                                "Her dildo slides lightly across her pubic region, subtly avoiding her lips",
                                "Her dildo is dragged up and down her inner thighs, slowing building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She drags the dildo slowly along her sides, carefully caressing them"])
                elif Action == "fondle ass":
                        $ Line = Line + renpy.random.choice(["Her hand traces slowly down her body, barely passing smoothly across her hips", 
                                "Her fingers move lightly across her crack, subtly avoiding her rosebud",
                                "Her fingers move up and down her inner thighs, slowing building towards their center",
                                "Her hands move along her sides, carefully caressing them"])              
                elif Action == "dildo anal":
                        $ Line = Line + renpy.random.choice(["She traces the rubber phallus slowly down her body, barely grazing her ass",                 
                                "Her dildo slides lightly across her crack, subtly avoiding the hole",
                                "Her dildo is dragged up and down her inner thighs, slowing building towards their center",
                                "She slowly spreads her cheeks and caresses the rim beneath",
                                "She drags the dildo slowly along her sides, carefully caressing them"])
                elif Action == "vibrator pussy":
                        $ Line = Line + renpy.random.choice(["She traces the buzzing ball slowly down her body, barely grazing her mound",                 
                                "Her vibrator slides lightly across her pubic region, subtly avoiding her lips",
                                "Her whirring toy is dragged up and down her inner thighs, slowing building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She drags the vibrator slowly along her sides, carefully caressing them"])
                else: # Action == "fondle breasts"
                        $ Line = Line + renpy.random.choice(["She gently rubs her breasts, dragging a finger across her nipple", 
                                "She gently cups her breasts and moves them in slow circles",
                                "She moves her hands from her breasts to rub her neck",
                                "She lightly pinches one of her nipples",
                                "She gasps as her finger brushes against an erect nipple"])   
                #End newgirl[Girl_].Lust 0-60
        #End Girl_ Action masturbation dialog        
                        
            
        # Girl_ Self-stat boosts  
        $ TempLustX += 4 if newgirl[Girl_].Lust > 80 else 0        
        $ TempLustX += 5 if newgirl[Girl_].Lust < 40 else 3                   #Bonus if she is relatively low lust
        $ TempLustX += 5 if Trigger == "masturbation" else 0     #Bonus if masturbation is her primary action
        
        if Primary == Girl_: #If this is a primary, Trigger3 action
            $ TempLust = TempLustX
        else: #If this is a Secondary, Trigger5 action
            $ TempLust2 = TempLustX
        
        $ TempFocus += 3         
        $ TempFocus += 1 if P_Focus < 50 else 0 
        
    #End Girl_ Action all dialog     
    
    return

label NewGirl_Dirty_Talk(D20=0, TempCheck=0, Line=0):    
    $ D20 = renpy.random.randint(1, 20)   
    if D20 >= 15 and Secondary:
            #if it's a high roll and there is a second girl, do a threesome line
            #$ Line = "threesome" #fix this when there are threesome lines to add.
            $ Line = "partner"
    elif D20 >= 10 and Secondary:
            #if it's a medium roll and there is a second girl, do a partner line
            $ Line = "partner"
    else:
            #if it's a lower roll, do a single girl line. Primary
            $ Line = "primary"
        
    #Rogue    
    $ D20 = renpy.random.randint(1, 20)   
    if Primary == "Rogue" or (Line == "partner" and Secondary == "Rogue" and D20 >= 15):
            #If the primary is Rogue or Rogue is the Partner
            if D20 <= 5 or (R_SEXP <= 30 and ApprovalCheck("Rogue", 400, "I")):
                    #If she's relatively inexperienced or there is a low roll
                    $ Line = renpy.random.choice([
                            "Touching ya is so amazing, " + R_Petname + ".",
                            "Every time you touch me. . .it's like, I can't even put it into words.",
                            "Mmmm. . .right there.",
                            "Ya like that, " + R_Petname + "?"
                            ])
            elif D20 <= 15: 
                    #If she's relatively experienced and there's a moderate roll
                    $ Line = renpy.random.choice([
                                "I want ya so bad, " + R_Petname + ".",
                                "I'm all yours, " + R_Petname + ". Take me however ya want.",
                                "I love it when ya do that, " + R_Petname + ".",
                                "I love the look you get on your face when we do that, " + R_Petname + "."
                                ])
            else: #a 15+ roll and experienced
                    if Primary == "Rogue":
                        #if Rogue is primary, Tempcheck is the Trigger variable
                        $ TempCheck = Trigger
                    else:
                        #if Rogue is secondary, Tempcheck is the Trigger4 variable
                        $ TempCheck = Trigger4
                    
                    if TempCheck == "hand":
                        $ Line = "Seems like you like this, huh, " + R_Petname + "?" #hand
                    elif TempCheck == "blow":
                        $ Line = "You taste so nice, " + R_Petname + "." #blow
                    elif TempCheck == "sex":
                        $ Line = "Ohhh. . .that's sooo good." #sex
                    elif TempCheck == "anal":
                        $ Line = "It. . .hurts. But it kinda feels good, too." #anal
                    else:
                        #if it's none of those, this will work
                        $ Line = renpy.random.choice([
                                "I want ya so bad, " + R_Petname + ".",
                                "I'm all yours, " + R_Petname + ". Take me however ya want.",
                                "I love it when ya do that, " + R_Petname + ".",
                                "I love the look you get on your face when we do that, " + R_Petname + "."
                                ])
            if Line and Line != "partner":
                    ch_r "[Line]"
    #end Primary Rogue        
            
    elif Primary == "Kitty" or (Line == "partner" and Secondary == "Kitty" and D20 >= 15):
            if D20 <= 5 or (K_SEXP <= 30 and ApprovalCheck("Kitty", 400, "I")):
                    #If she's relatively inexperienced or there is a low roll
                    $ Line = renpy.random.choice([
                            "You're so amazing, " + K_Petname + ".",
                            "You know how to push, like, every one of my buttons. . .",
                            "Heh. . .{i}somebody{/i} seems to like that.",
                            "That's, like, {i}so{/i} good."
                            ])
            elif D20 <= 15: 
                    #If she's relatively experienced and there's a moderate roll
                    $ Line = renpy.random.choice([
                                "This is {i}so{/i} hot, " + K_Petname + ".",
                                "I think I just, like, discovered one of your other mutant powers, " + K_Petname + ".",
                                "I like it.  Like, a {i}lot{/i}.",
                                "I've never wanted a guy like I want you, " + K_Petname + "."
                                ])
            else: #a 15+ roll and experienced
                    if Primary == "Kitty":
                        #if Kitty is primary, Tempcheck is the Trigger variable
                        $ TempCheck = Trigger
                    else:
                        #if Kitty is secondary, Tempcheck is the Trigger4 variable
                        $ TempCheck = Trigger4
                    
                    if TempCheck == "hand":
                        $ Line = "I love the way it, like, feels in my hands." #hand
                    elif TempCheck == "blow":
                        $ Line = "I hope you don't think I'm, like, a slut for saying this. . .but I love how you taste, " + K_Petname + "." #blow
                    elif TempCheck == "sex":
                        $ Line = "Oooohh. . .just like {i}that{/i}." #sex
                    elif TempCheck == "anal":
                        $ Line = "Please. . .go slow, 'kay?  You feel so {i}big{/i}." #anal
                    else:
                        #if it's none of those, this will work
                        $ Line = renpy.random.choice([
                                "This is {i}so{/i} hot, " + K_Petname + ".",
                                "I think I just, like, discovered one of your other mutant powers, " + K_Petname + ".",
                                "I like it.  Like, a {i}lot{/i}.",
                                "I've never wanted a guy like I want you, " + K_Petname + "."
                                ])
            if Line and Line != "partner":
                    ch_k "[Line]"
                        
    #end Primary Kitty  

    elif Primary == "Emma" or (Line == "partner" and Secondary == "Emma" and D20 >= 15):
            if D20 <= 5 or (E_SEXP <= 30 and ApprovalCheck("Emma", 400, "I")):
                    #If she's relatively inexperienced or there is a low roll
                    $ Line = renpy.random.choice([
                            "You're incredible, " + E_Petname + ".",
                            "You're surprisingly skilled at this. . .",
                            "Well, that certainly got a positive response.",
                            "Exceptional work, darling.",
                            ])
            elif D20 <= 15: 
                    #If she's relatively experienced and there's a moderate roll
                    $ Line = renpy.random.choice([
                                "I'm overwhelmed, " + E_Petname + ".",
                                "Well now we have another skill to develop, " + E_Petname + ".",                                        
                                "Oooh, that's lovely. . .",
                                "More, I want more!",
                                "You're simply adorable, " + E_Petname + ".",
                                "Ooh, you'll {i}have{/i} to do that one again. . .",
                                "You certainly do leave an impression, " + E_Petname + "."
                                ])
            else: #a 15+ roll and experienced
                    if Primary == "Emma":
                        #if Emma is primary, Tempcheck is the Trigger variable
                        $ TempCheck = Trigger
                    else:
                        #if Emma is secondary, Tempcheck is the Trigger4 variable
                        $ TempCheck = Trigger4
                    
                    if TempCheck == "hand":
                        $ Line = "I love the way it, like, feels in my hands." #hand
                    elif TempCheck == "blow":
                        $ Line = "I hope you don't think I'm, like, a slut for saying this. . .but I love how you taste, " + E_Petname + "." #blow
                    elif TempCheck == "sex":
                        $ Line = "Oooohh. . .just like {i}that{/i}." #sex
                    elif TempCheck == "anal":
                        $ Line = "Please. . .go slow, 'kay?  You feel so {i}big{/i}." #anal
                    else:
                        #if it's none of those, this will work
                        $ Line = renpy.random.choice([
                                "This is {i}so{/i} hot, " + E_Petname + ".",
                                "I think I just, like, discovered one of your other mutant powers, " + E_Petname + ".",
                                "I like it.  Like, a {i}lot{/i}.",
                                "I've never wanted a guy like I want you, " + E_Petname + "."
                                ])
            if Line and Line != "partner":
                    ch_e "[Line]"
                        
    #end Primary Emma  

    elif Primary == "Mystique" or (Line == "partner" and Secondary == "Mystique" and D20 >= 15):
            if D20 <= 5 or (newgirl["Mystique"].SEXP <= 30 and ApprovalCheck("Mystique", 400, "I")):
                    #If she's relatively inexperienced or there is a low roll
                    $ Line = renpy.random.choice([
                            "You're so amazing, " + newgirl["Mystique"].Petname + ".",
                            "You know how to push, like, every one of my buttons. . .",
                            "Heh. . .{i}somebody{/i} seems to like that.",
                            "That's, like, {i}so{/i} good."
                            ])
            elif D20 <= 15: 
                    #If she's relatively experienced and there's a moderate roll
                    $ Line = renpy.random.choice([
                                "This is {i}so{/i} hot, " + newgirl["Mystique"].Petname + ".",
                                "I think I just, like, discovered one of your other mutant powers, " + newgirl["Mystique"].Petname + ".",
                                "I like it.  Like, a {i}lot{/i}.",
                                "I've never wanted a guy like I want you, " + newgirl["Mystique"].Petname + "."
                                ])
            else: #a 15+ roll and experienced
                    if Primary == "Mystique":
                        #if Mystique is primary, Tempcheck is the Trigger variable
                        $ TempCheck = Trigger
                    else:
                        #if Mystique is secondary, Tempcheck is the Trigger4 variable
                        $ TempCheck = Trigger4
                    
                    if TempCheck == "hand":
                        $ Line = "I love the way it, like, feels in my hands." #hand
                    elif TempCheck == "blow":
                        $ Line = "I hope you don't think I'm, like, a slut for saying this. . .but I love how you taste, " + newgirl["Mystique"].Petname + "." #blow
                    elif TempCheck == "sex":
                        $ Line = "Oooohh. . .just like {i}that{/i}." #sex
                    elif TempCheck == "anal":
                        $ Line = "Please. . .go slow, 'kay?  You feel so {i}big{/i}." #anal
                    else:
                        #if it's none of those, this will work
                        $ Line = renpy.random.choice([
                                "This is {i}so{/i} hot, " + newgirl["Mystique"].Petname + ".",
                                "I think I just, like, discovered one of your other mutant powers, " + newgirl["Mystique"].Petname + ".",
                                "I like it.  Like, a {i}lot{/i}.",
                                "I've never wanted a guy like I want you, " + newgirl["Mystique"].Petname + "."
                                ])
            if Line and Line != "partner":
                    ch_m "[Line]"
                        
    #end Primary Mystique  

    return

label NewGirl_RemoveClothes(Girl_ = "Mystique"):
    
    $ newgirl[Girl_].Over = 0
    $ newgirl[Girl_].Legs = 0
    $ newgirl[Girl_].Chest = 0
    $ newgirl[Girl_].Panties = 0
    $ newgirl[Girl_].Neck = 0
    $ newgirl[Girl_].Hose = 0
    $ newgirl[Girl_].Glasses = 0
    if Girl_ == "Mystique":
        if newgirl["Mystique"].LooksLike == "Mystique":
            call Mod_Update_Mystique_Image(1)

    return

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////