# //////////////////////////////////////////////////////////////////////                World Map Interface 

label Worldmap:
#    if Current_Time == 'Evening':    
#        scene Crossroads_E onlayer backdrop
#    elif Current_Time == 'Night':
#        scene Crossroads_N onlayer backdrop        
#    else: 
#        scene Crossroads_D onlayer backdrop    
    scene bg_campus onlayer backdrop   
    scene 
    $ Taboo = 0
    menu:
        "Where would you like to go?"
        "My Room":
                    $ renpy.pop_call() 
                    jump Player_Room_Entry  
        "Testbed" if config.developer:          
                    $ renpy.pop_call() 
                    jump Rogue_Room_Test
        "Girl's Rooms":
            menu:
                "Rogue's Room":   
                            $ renpy.pop_call() 
                            jump Rogue_Room_Entry 
                "Kitty's Room" if "met" in K_History:   
                            $ renpy.pop_call() 
                            jump Kitty_Room_Entry   
                "Emma's Room" if "met" in E_History:   
                            $ renpy.pop_call() 
                            jump Emma_Room_Entry  
                "Laura's Room" if "met" in L_History:   
                            $ renpy.pop_call() 
                            jump Laura_Room_Entry  
                "Back":
                            jump Worldmap
        "University Square":
                    $ renpy.pop_call() 
                    jump Campus_Entry 
        "Class":
            if Current_Time != "Night":
                $ renpy.pop_call() 
                jump Class_Room_Entry 
            elif "Xavier" in Keys:
                        "The door is locked, but you were able to use Xavier's key to get in."
                        $ renpy.pop_call() 
                        jump Class_Room_Entry 
            else:
                        "It's late for classes and the classrooms are locked down."
                        jump Worldmap
        "The Danger Room":         
                    $ renpy.pop_call()    
                    jump Danger_Room_Entry
        "The showers":
                    $ renpy.pop_call() 
                    jump Shower_Room_Entry    
        "The pool": 
                    $ renpy.pop_call() 
                    jump Pool_Entry           
        "Xavier's Study":
                    $ renpy.pop_call() 
                    jump Study_Room_Entry 
        "Stay where I am.":
                    return
    return          
                    
# end World Map Interface //////////////////////////////////////////////////////////////////////

# start Misplaced location checker  //////////////////////////////////////////////////////////////////////
label Misplaced:
        if Trigger:
            #sent here by a broken sex action
            call Misplaced_Sex 
        if "locked" in P_Traits:
                $ P_Traits.remove("locked")
        $ StackDepth = renpy.call_stack_depth() #Count = number of items in the call stack
        while StackDepth > 0:
            $ StackDepth -= 1
            $ renpy.pop_call()
        if bg_current == "bg player":
                jump Player_Room 
        if bg_current == "bg rogue":
                jump Rogue_Room 
        if bg_current == "bg kitty":
                jump Kitty_Room 
        if bg_current == "bg emma":
                jump Emma_Room 
        if bg_current == "bg laura":
                jump Laura_Room 
        if bg_current == "bg dangerroom":
                jump Danger_Room 
        if bg_current == "bg classroom":
                jump Class_Room 
        if bg_current == "bg showerroom":
                jump Shower_Room 
        if bg_current == "bg study":
                jump Study_Room 
        if bg_current == "bg pool":
                jump Pool_Entry
        jump Campus 
            
        return
        
label Misplaced_Sex:
        #sent here by a broken sex action
        if Trigger == "Rogue":
                call Rogue_SexMenu
        if Trigger == "Kitty":
                call Kitty_SexMenu
        if Trigger == "Emma":
                call Emma_SexMenu
        if Trigger == "Laura":
                call Laura_SexMenu
        return
# end Misplaced location checker  //////////////////////////////////////////////////////////////////////


# Player's Room Interface //////////////////////////////////////////////////////////////////////
label Player_Room_Entry:
    if "locked" in P_Traits:
            $ P_Traits.remove("locked")
    $ bg_current = "bg player"   
    call Gym_Clothes
    $ P_RecentActions.append("traveling")
    $ Nearby = []
    call EventCalls
    call Set_The_Scene
    jump Clear_Stack #removes stray calls in the call stack
    
label Player_Room:
    $ bg_current = "bg player"
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                call Round10
                call Girls_Location
                call EventCalls                
    call GirlsAngry      

# Player Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    menu:
        "You are in your room. What would you like to do?"
        "Chat":
                    call Chat
            
        "Would you like to study?":
                    call Study_Session
                
        "Lock the door" if "locked" not in P_Traits:
                    "You lock the door"
                    $ P_Traits.append("locked")
                    call Taboo_Level
                            
        "Unlock the door" if "locked" in P_Traits:
                    "You unlock the door"
                    $ P_Traits.remove("locked")
                    call Taboo_Level
                    
        "Sleep" if Current_Time == "Night":            
                    call Round10
                    call Girls_Location
                    call EventCalls  
        "Wait" if Current_Time != "Night":
                    "You wait around a bit."
                    call Wait                 
                    call Girls_Location
                    call EventCalls      
            
        "Shop":
                    call Shop                
        "Special Options":
                    call SpecialMenu #found in Rogue Scenes
        
        
        "Girl's Rooms" if TravelMode:
            menu:
                "Rogue's Room":   
                            jump Rogue_Room_Entry 
                "Kitty's Room" if "met" in K_History:   
                            jump Kitty_Room_Entry   
                "Emma's Room" if "met" in E_History:   
                            jump Emma_Room_Entry  
                "Laura's Room" if "met" in L_History: 
                            jump Laura_Room_Entry  
                "Back":
                            pass
        "Go to the Showers" if TravelMode:         
                    jump Shower_Room_Entry
                    
        "Leave" if not TravelMode:
                    call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
                    jump Campus_Entry
                    
    jump Player_Room

# end Player's Room Interface //////////////////////////////////////////////////////////////////////

# Rogue's Room Interface //////////////////////////////////////////////////////////////////////
label Rogue_Room_Entry:
    if "locked" in P_Traits:
            $ P_Traits.remove("locked")
    call Shift_Focus("Rogue")
    $ bg_current = "bg rogue"      
    $ Nearby = []     
    call Gym_Clothes
    call Set_The_Scene(Entry = 1)    
    call Taboo_Level
    $ P_RecentActions.append("traveling")
    $ D20 = renpy.random.randint(1, 20)
    
    if "Rogue" in Party:
                    if Current_Time == "Night" or (Current_Time == "Evening" and Round <= 10):                         
                        if ApprovalCheck("Rogue", 1000, "LI") or ApprovalCheck("Rogue", 600, "OI"):     
                                #It's late but she really likes you
                                ch_r "It's pretty late, [R_Petname], but you can come in for a little bit."    
                        elif R_Addict >= 50:
                                ch_r "Um, yeah, you'd better come in. . ."         
                        elif ApprovalCheck("Rogue", 500, "LI") or ApprovalCheck("Rogue", 300, "OI"):     
                                #she likes you well enough but it's late
                                ch_r "It's a little late [R_Petname]. See you tomorrow."
                                $ R_RecentActions.append("noentry")                      
                                $ R_DailyActions.append("noentry")  
                                if "Rogue" in Party:
                                        $ Party.remove("Rogue")   
                                "She heads inside and closes the door behind her."
                                jump Campus_Map         
                    else: #If Rogue is in the party and it's not late in the day        
                                ch_r "Come on in, [R_Petname]."
                    call EventCalls
                    jump Rogue_Room   
    #End if Rogue in Party
    
    if Round >= 10 and R_Loc == bg_current and "les" in R_RecentActions:
            call Girls_Caught_Lesing("Rogue")
            if not _return: #if nobody was there for it, drop through
                jump Rogue_Room
    if Round >= 10 and R_Loc == bg_current and "gonnafap" in R_DailyActions and D20 >= 10: 
                    #Rogue caught fapping  
                    call Girl_Caught_Mastubating("Rogue")
    
    else: #not auto-caught fapping
            if "Rogue" in Keys:
                menu:
                    "You have a key, what do you do?"
                    "Knock politely":
                            $ Line = "knock"
                            
                    "Use the key to enter.":
                            $ bg_current = "bg rogue"
                            call Set_The_Scene
                        
            if Line != "knock" and "Rogue" in Keys: 
                if R_Loc == "bg rogue":
                        if Round <= 10:        #add "no" condtion here
                                if  "noentry" in R_RecentActions or "angry" in R_RecentActions:
                                        call RogueFace("angry")
                                        ch_r "Buzz off already."  
                                        "Rogue shoves you back into the hall."
                                        jump Campus_Map   
                                if Current_Time == "Night" :    
                                        "She's asleep in bed. You slip out quietly." #fix add options here.                            
                                        jump Campus_Map   
                        elif "gonnafap" in R_DailyActions and D20 >= 10: 
                                #Rogue caught fapping  
                                call Girl_Caught_Mastubating("Rogue")
                        elif D20 >=15 and (Current_Time == "Night" or Current_Time == "Morning"):                          
                                #Rogue caught changing
                                call Rogue_Caught_Changing
            #End "if you enter without knocking"
                
            else:#You knocked
                        $ Round -= 10 
                        "You knock on Rogue's door."        
                        if R_Loc != "bg rogue":
                                "Looks like she's not home right now."
                                jump Campus_Map
                            
                        if Round <= 10:
                                if Current_Time == "Night" :
                                    "There's no answer, she's probably asleep."  
                                    jump Campus_Map    
                    
                        if (D20 >=19 and R_Lust >= 50) or (D20 >=15 and R_Lust >= 70) or (D20 >=10 and R_Lust >= 80):    
                                #Rogue caught fapping
                                "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
                                "After several seconds and some more shuffling of clothing, Rogue comes to the door."
                                $ R_Brows = "confused"
                                $ R_Eyes = "surprised"
                                $ R_Mouth = "smile"
                                $ R_Blush = 1
                                call Set_The_Scene
                                ch_r "Sorry about that [R_Petname], I was. . . working out."
                                $ Tempmod += 10
                        elif D20 >=15 and (Current_Time == "Night" or Current_Time == "Morning"):                          
                                #Rogue caught changing
                                "You hear the rustling of fabric and some knocking around, but after a few seconds Rogue comes to the door."
                                call Set_The_Scene
                                ch_r "Sorry about that [R_Petname], I was just getting changed."        
                        elif "angry" in R_RecentActions:
                                ch_r "I don't want to deal with you right now."
                                "Rogue pushes you back into the hall and slams the door."
                                $ Trigger = 0
                                jump Campus_Map    
                        else:
                                call Set_The_Scene
                                "Rogue opens the door and leans out."
                                "You ask if you can come inside."
            #End "if you knocked"
                    
            #if you reach this point then you've asked to enter.               
            if R_Loc != "bg rogue":
                    "Looks like she's not home right now."                
                    if "Rogue" in Keys:
                            menu:
                                "Go in and wait for her?"
                                "Yes":
                                        $ Line = 0
                                        jump Rogue_Room
                                "No":
                                        pass
                    "You head back."
                    jump Campus_Map 
                    
            elif  "noentry" in R_RecentActions or "angry" in R_RecentActions:
                    call RogueFace("angry")
                    ch_r "Buzz off already."  
                    jump Campus_Map    
                    
            elif Current_Time == "Night" and "noentry" in R_RecentActions:
                    ch_r "Hey, I told you you're not welcome. I'll see you tomorrow."
                    jump Campus_Map 
                    
            elif "noentry" in R_RecentActions:
                    call RogueFace("angry")
                    ch_r "Hey, I told you you're not welcome."  
                    call Statup("Rogue", "Love", 200, -5)
                    call Statup("Rogue", "Obed", 50, -2)
                    $ R_RecentActions.append("angry")                      
                    $ R_DailyActions.append("angry") 
                    jump Campus_Map  
            
            elif Current_Time == "Night" and (R_Sleep or R_SEXP >= 30):                                                  
                    #It's late but she really likes you
                    ch_r "It's pretty late, [R_Petname], but it's always nice to see you."                    
            elif Current_Time == "Night" and (ApprovalCheck("Rogue", 1000, "LI") or ApprovalCheck("Rogue", 600, "OI")):     
                    #It's late but she really likes you
                    ch_r "It's pretty late, [R_Petname], but you can come in for a little bit."                
            elif R_Addict >= 50:
                    ch_r "Um, yeah, you'd better come in. . ."
                    
            elif Current_Time == "Night" and (ApprovalCheck("Rogue", 500, "LI") or ApprovalCheck("Rogue", 300, "OI")):      
                    #she likes you well enough but it's late
                    ch_r "It's a little late [R_Petname]. Maybe tomorrow."
                    $ R_RecentActions.append("noentry")                      
                    $ R_DailyActions.append("noentry")  
                    jump Campus_Map    
                    
            elif ApprovalCheck("Rogue", 600, "LI") or ApprovalCheck("Rogue", 300, "OI"):                                   
                    #She quite likes you and lets you in   
                    ch_r "Sure, come on in [R_Petname]."        
            else:                                                                                                           
                    #She doesn't like you      
                    ch_r "I'd rather you didn't come in, thanks."
                    $ R_RecentActions.append("noentry")                      
                    $ R_DailyActions.append("noentry")  
                    jump Campus_Map
    
    # If you get this far, she's allowed you in
    $ bg_current = "bg rogue"         
    call EventCalls
    if R_Loc == "bg rogue" and "angry" in R_RecentActions:
        "Rogue pushes you back into the hall and slams the door. You head back to your room."
        $ Line = 0
        $ Trigger = 0
        jump Player_Room
    if bg_current != "bg rogue":
        jump Misplaced
            
label Rogue_Room:
    $ bg_current = "bg rogue"
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)    
    if Round <= 10:
                call Round10
                call Girls_Location
                call EventCalls    
    call GirlsAngry    
    
# Rogue's Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if R_Loc == bg_current:
        $ Line = "You are in Rogue's room. What would you like to do?"
    else:
        $ Line = "You are in Rogue's room, but she isn't here. What would you like to do?"
    menu:
        "[Line]"
        
        "Chat":
                    call Chat
        
        "Would you like to study?":
                    call Study_Session
                    
        "Lock the door" if "locked" not in P_Traits:
                if R_Loc == bg_current and not ApprovalCheck("Rogue", 1000):
                    ch_r "Hey, could you maybe keep that open, [R_Petname]?"
                else:
                    "You lock the door"
                    $ P_Traits.append("locked")   
                    call Taboo_Level
                   
        "Unlock the door" if "locked" in P_Traits:
                    "You unlock the door"
                    $ P_Traits.remove("locked")
                    call Taboo_Level  
            
        "Sleep." if Current_Time == "Night":
                    call Round10
                    call Girls_Location
                    call EventCalls    
                    
        "Wait." if Current_Time != "Night":
                    call Round10
                    call Girls_Location
                    call EventCalls 
                    
        "Return to Your Room" if TravelMode:            
                    jump Player_Room_Entry   
        "Other Girl's Rooms" if TravelMode:
            menu:
                "Kitty's Room" if "met" in K_History:   
                            jump Kitty_Room_Entry   
                "Emma's Room" if "met" in E_History:   
                            jump Emma_Room_Entry  
                "Laura's Room" if "met" in L_History: 
                            jump Laura_Room_Entry  
                "Back":
                            pass      
        "Go to the Showers" if TravelMode:            
                    jump Shower_Room_Entry
                    
        "Leave" if not TravelMode:
                    call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
                    jump Campus_Entry
    
    if "angry" in R_RecentActions:
            call RogueFace("angry")
            ch_r "I really think you should leave."
            "Rogue pushes you back into the hall and slams the door. You head back to your room."
            $ Line = 0
            $ Trigger = 0
            jump Player_Room
    jump Rogue_Room
    
label Rogue_Caught_Changing:
            call Shift_Focus("Rogue")
            $ D20 = renpy.random.randint(1, 20)
            
            call RogueFace("surprised", 1)
            $ R_Mouth = "kiss"
            if D20 > 17:        
                    #She's naked
                    call RogueOutfit("nude")
            elif D20 >15:       
                    #She's bottomless
                    $ R_Legs = 0
                    $ R_Panties = 0
            elif D20 >14:       
                    #She's Topless
                    $ R_Over = 0
                    $ R_Chest = 0
            elif D20 >10:       
                    #She's in her underwear
                    $ R_Over = 0
                    $ R_Legs = 0
                    $ R_Panties = "black panties"
            elif D20 >5:        
                    #She's wearing pants/skirt
                    $ R_Over = 0
            #else: #fully dressed
            call Set_The_Scene(Dress=0)
            if D20 > 17:        
                    #She's naked
                    "As you enter the room, you see Rogue is naked, and seems to be getting dressed."      
            elif D20 >14:       
                    #She's Topless
                    "As you enter the room, you see Rogue is practically naked, and seems to be getting dressed."  
            elif D20 >10:       
                    #She's in her underwear
                    "As you enter the room, you see Rogue is in her underwear, and seems to be getting dressed." 
            elif D20 >5:        
                    #She's wearing pants/skirt
                    "As you enter the room, you see Rogue has her top off, and seems to be getting dressed." 
            else:
                    #She's done
                    "As you enter the room, you see Rogue has just pulled her top on, and seems to have been getting dressed." 
                 
            if D20 > 5: 
                    if not ApprovalCheck("Rogue", (D20 *70)) or (not R_SeenPussy and not R_Panties) or (not R_SeenChest and not R_Chest):
                            # She is mad
                            call RogueFace("surprised")
                            $R_Brows = "angry"  
                            call Statup("Rogue", "Love", 80, -50)
                            if not R_Over or not R_Legs:
                                $ R_Over = "towel"
                                "She grabs a towel and covers up."
                    else:       
                            #She's cool with it, but confused.
                            call RogueFace("surprised", 1)      
                            $R_Brows = "confused"
                            if "exhibitionist" in R_Traits:
                                call Statup("Rogue", "Lust", 200, (2*D20))  
                            else:
                                call Statup("Rogue", "Lust", 200, D20)
                          
                    call Statup("Rogue", "Inbt", 70, 20)
                    if D20 > 17:
                        call Rogue_First_Bottomless
                        call Rogue_First_Topless(1)
                    elif D20 > 15:
                        call Rogue_First_Bottomless
                    elif D20 > 14:
                        call Rogue_First_Topless
                    menu:
                        ch_r "Hey! Learn to knock maybe?!"
                        "Sorry, I should have knocked.":  
                            call Statup("Rogue", "Love", 50, 2)
                            call Statup("Rogue", "Love", 80, 4)
                        "And miss the view?":
                            call Statup("Rogue", "Obed", 50, 2)
                            call Statup("Rogue", "Obed", 80, 2)
                            call Statup("Rogue", "Inbt", 60, 1)
                    #end if she's partially nude
            else:              
                    #She's fully dressed      
                    if not ApprovalCheck("Rogue", 800) and (not R_SeenPussy or not R_SeenChest):            
                            call RogueFace("angry")
                            $R_Brows = "confused"
                            call Statup("Rogue", "Love", 80, -5)
                    else:
                            call RogueFace("sexy")
                            $R_Brows = "confused"
                    call Statup("Rogue", "Inbt", 50, 3)
                    menu:
                        ch_r "Well hello there, [R_Petname]. Hoping to see something more?"
                        "Sorry, I should have knocked.":   
                            call Statup("Rogue", "Love", 50, 2)
                            call Statup("Rogue", "Love", 80, 2)
                        "Well, to be honest. . .":
                            call Statup("Rogue", "Love", 50, -2)
                            call Statup("Rogue", "Obed", 50, 2)
                            call Statup("Rogue", "Obed", 80, 2)
                            call Statup("Rogue", "Inbt", 60, 1)
            call RogueFace("sexy")                
            if ApprovalCheck("Rogue", 750) and R_SeenPussy and R_SeenChest:
                    ch_r "You could have just asked, [R_Petname]."                
                    $ R_Over = 0
                    $ R_Upskirt = 1
                    pause 1     
                    call RogueOutfit
                    $ R_Upskirt = 0
                    "She flashes you real quick."  
            else:
                    ch_r "Well, it happens, just be careful next time."   
            menu:
                    ch_r "Well, are you planning to stick around?" 
                    "Sure, for a bit.":
                        pass
                    "Actually, I should get going. . .":
                        call RogueOutfit(Changed=0)
                        call Worldmap            
            jump Rogue_Room
            return
            #End Rogue Caught Changing
# end Rogue's Room Interface //////////////////////////////////////////////////////////////////////



# University Square Interface //////////////////////////////////////////////////////////////////////

label Campus_Map:
    $ Line = 0
    $ Trigger = 0
    $ Trigger2 = 0
    $ Trigger3 = 0
    $ bg_current = "bg campus"    
    if "locked" in P_Traits:
            $ P_Traits.remove("locked")
    call Set_The_Scene
    if not TravelMode: 
        call Worldmap
    jump Campus
    
label Campus_Entry:
    if "locked" in P_Traits:
            $ P_Traits.remove("locked")
    $ bg_current = "bg campus"        
    $ Nearby = []             
    call Gym_Clothes  
    call Taboo_Level
    $ P_RecentActions.append("traveling")
    call EventCalls
    call Set_The_Scene
    
label Campus:
    $ bg_current = "bg campus"
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents    
    call Checkout(1)    
    call GirlsAngry    
    if Current_Time == "Evening" and "yesdate" in P_DailyActions:
            #if it's evening and you have a date lined up. . .
            menu:
                "Ready to go on that date?"
                "Yes":
                        call DateNight
                        if "yesdate" in P_DailyActions:
                                $ P_DailyActions.remove("yesdate")
                "One moment. . .":
                        pass
    if Round <= 10:
                if Current_Time == "Night":   
                    "You're getting tired, you head back to your room."
                    jump Player_Room
                call Wait   
                call EventCalls
                call Girls_Location
    #End date code

# Uni Square Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    menu:
        "You are in the university square. What would you like to do?"
        
        "Chat":
            call Chat
            
        "Wait." if Current_Time != "Night":
            "You wait around a bit."
            call Wait   
            call EventCalls            
            call Girls_Location
            
        "Go to my Room" if TravelMode:
                    jump Player_Room_Entry  
        "Girl's Rooms" if TravelMode:
            menu:
                "Rogue's Room":   
                            jump Rogue_Room_Entry 
                "Kitty's Room" if "met" in K_History:   
                            jump Kitty_Room_Entry   
                "Emma's Room" if "met" in E_History:   
                            jump Emma_Room_Entry  
                "Laura's Room" if "met" in L_History: 
                            jump Laura_Room_Entry  
                "Back":
                            pass
        "Go to the classroom" if TravelMode: 
                    if Current_Time != "Night":
                        jump Class_Room_Entry 
                    elif "Xavier" in Keys:
                        "The door is locked, but you were able to use Xavier's key to get in."
                        jump Class_Room_Entry 
                    else:
                        "It's late for classes and the classrooms are locked down."   
        "Go to the Danger Room" if TravelMode: 
                    jump Danger_Room_Entry
        "Go to the showers" if TravelMode: 
                    jump Shower_Room_Entry   
        "Go to the pool" if TravelMode: 
                    jump Pool_Entry         
        "Xavier's Study" if TravelMode: 
                    jump Study_Room_Entry 
                    
        "Leave" if not TravelMode:
                    call Worldmap
                    
    jump Campus

# end University Square Interface //////////////////////////////////////////////////////////////////////



# Classroom Interface //////////////////////////////////////////////////////////////////////

label Class_Room_Entry:
    if "locked" in P_Traits:
            $ P_Traits.remove("locked")
    $ Adjacent = []
    $ bg_current = "bg classroom"       
    $ Nearby = []               
    call Gym_Clothes 
    call Taboo_Level
    $ P_RecentActions.append("traveling")
    call EventCalls
    call Set_The_Scene(0) #won't display characters yet)
    if Current_Time != "Night" and Current_Time != "Evening" and Weekday < 5:   
            call Class_Room_Seating    
    $ Line = "entry"
    if "goto" in P_RecentActions:
        $ P_RecentActions.remove("goto")
                
label Class_Room:    
    $ bg_current = "bg classroom"    
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")
    if "goto" in P_RecentActions:
        $ Adjacent = []        
        if Current_Time != "Night" and Current_Time != "Evening" and Weekday < 5:   
                call Class_Room_Seating    
        $ P_RecentActions.remove("goto")
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents    
    call Checkout(1)
    if Round <= 10:
                if Current_Time == "Night":   
                    "You're getting tired, you head back to your room."
                    jump Player_Room
                call Wait   
                call EventCalls
                call Girls_Location
    call GirlsAngry  
    
    if Line == "entry":
        if E_Loc == "bg teacher":
            $ Line = "As you sit down, you see "+ EmmaName +" at the podium. What would you like to do?" 
        elif Current_Time == "Evening" or Weekday > 5:   
            $ Line = "You enter the classroom. What would you like to do?" 
        else:
            $ Line = "You sit down at a desk. What would you like to do?" 
    else:
        if Line != "What would you like to do next?":
                $ Line = "You are in class right now. What would you like to do?" 
    #End Room Set-up
    
# Class Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<        
    menu:
        "[Line]" 
        "Take the morning class" if Weekday < 5 and Current_Time == "Morning":
                if Round >= 30:
                    jump Take_Class
                else: 
                    "Class is already letting out. You can hang out until the next one."             
        "Take the afternoon class" if Weekday < 5 and Current_Time == "Midday":
                if Round >= 30:
                    jump Take_Class
                else: 
                    "Class is already letting out. You can hang out until they lock up for the night." 
        "There are no classes right now (locked)" if Weekday >= 5 or Current_Time == "Evening" or Current_Time == "Night":
                pass
            
        "Chat":
                call Chat
                $ Line = "You are in class right now. What would you like to do?" 
           
        "Lock the door" if "locked" not in P_Traits:
                    if Current_Time == "Evening" or Current_Time == "Night" or Weekday >=5:
                            "You lock the door"
                            $ P_Traits.append("locked")
                            call Taboo_Level
                    else:
                            "You can't really do that during class."
                            
        "Unlock the door" if "locked" in P_Traits:
                    "You unlock the door"
                    $ P_Traits.remove("locked")
                    call Taboo_Level                    
                    
        "Wait" if Current_Time != "Night":
                "You hang out for a bit."
                call Wait   
                call EventCalls            
                call Girls_Location 
                    
                if Current_Time == "Midday":
                            $ Line = "A new class is in session. What would you like to do?"
                if Current_Time == "Evening":
                            $ Line = "Classes have let out for the day. What would you like to do?"
                                
        "Leave" if not TravelMode:
                    call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
                    jump Campus_Entry
    
    $ Line = 0
    jump Class_Room

# End Core Classroom menu <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    
label Take_Class:                       #Class events 
    call Set_The_Scene  
    if "class" in P_DailyActions:
            $ Line = "The session begins."
    elif Round >= 80:
            $ Line = "You make it in time for the start of the class."
    elif Round >= 50:
            $ Line = "You get in a bit late, but there's plenty of class left."
    elif Round >= 30:
            $ Line = "You're pretty late, but catch the tail end of the class."
    $ Trigger = 0
    
    $ D20 = renpy.random.randint(1, 20)
    if "Rogue" in Adjacent and D20 > 10 and R_Inbt >= 500 and R_Loc == "bg classroom":        
        "[Line]"    
        call Rogue_Frisky_Class
    else:        
        $ Line = Line + renpy.random.choice([" It was fairly boring.", 
                " It was a lesson in mutant biology.", 
                " You took a math course.",
                " You watched a movie about sealions.",
                " That was fun.",
                " Applied trigonometry is surprisingly interesting, especially when Cyclops demonstrates using it for trick shots.",
                " Geopolitical science: Latveria to Madripoor.",
                " Today's lecture is on reading body language. You suppose if anyone would know about reading people. . .",
                " The topic of the day is Mutants and the larger superhuman community.", 
                " Capes: What Your Name and Costume Say About You turns out to be pretty lively as you participate in a debate on costume designs.",
                " The topic is \"Mutants VS Mutates.\" As it turns out, the terms aren’t interchangeable.",  
                " Today's class is on how to present yourself to the public. She uses Spider-Man as an example of how bad PR makes your life harder than it needs to be.",                     
                " Mutant History, Apocalypse to Dark Phoenix.",
                " Game writing for dummies, eh?"]) 
        "[Line]"    
    $ P_RecentActions.append("class")                      
    $ P_DailyActions.append("class")   
    $ P_XP += (5 + (int(Round / 10)))
        
    call Wait   
    call Girls_Location
    call Set_The_Scene 
    call EventCalls
    $ Line = "What would you like to do next?"    
    jump Class_Room
    
# End "Taking Class" <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<          


label Class_Room_Seating(Girls=[],GirlB=0,GirlLike=0,Line=0,D20=0):
    # Girls is the amount of girls in the room. 
    # active ones get priority, then shuffled, then nearby girls
    $ Adjacent = []
    if R_Loc == bg_current:  
                $ Girls.append("Rogue")
    if K_Loc == bg_current:
                $ Girls.append("Kitty")
    if L_Loc == bg_current:
                $ Girls.append("Laura") 
        
    $ renpy.random.shuffle(Girls)
    
    if "Rogue" in Nearby and "Rogue" not in Girls: 
                $ Girls.append("Rogue")
    if "Kitty" in Nearby and "Kitty" not in Girls:
                $ Girls.append("Kitty")
    if "Laura" in Nearby and "Laura" not in Girls:
                $ Girls.append("Laura")   
    #End Girl selections
        
    $ Nearby = []
    
    if len(Girls) == 2:
            # there are two girls
            $ D20 = renpy.random.randint(500, 1500)
            if (GirlLikeCheck(Girls[0],Girls[1]) + GirlLikeCheck(Girls[1],Girls[0])) >= D20:
                "You see that [Girls[0]] and [Girls[1]] are sitting next to each other, which do you sit next to?"
            else:
                "You see that [Girls[0]] and [Girls[1]] are in the room, but on opposite sides."               
                if "Rogue" in Girls and "Rogue" not in Nearby:
                            $ Nearby.append("Rogue") 
                if "Kitty" in Girls and "Kitty" not in Nearby:
                            $ Nearby.append("Kitty")    
                if "Laura" in Girls and "Laura" not in Nearby:
                            $ Nearby.append("Laura")  
            menu:
                extend ""
                "[Girls[0]]":
                        $ Adjacent = [Girls[0]]
                        if Girls[0] in Nearby:
                            $ Nearby.remove(Girls[0])
                "[Girls[1]]":
                        $ Adjacent = [Girls[1]]   
                        if Girls[1] in Nearby:
                            $ Nearby.remove(Girls[1])
                "Between them." if not Nearby:
                        $ Adjacent = [Girls[0],Girls[1]] 
                        if Girls[1] in Nearby: 
                            $ Nearby.remove(Girls[1])
                        if Girls[0] in Nearby:
                            $ Nearby.remove(Girls[0])                                  
                "Neither":
                        "You decide to sit a distance away from either of them."
                        if "Rogue" in Girls and "Rogue" not in Nearby:
                                    $ Nearby.append("Rogue") 
                        if "Kitty" in Girls and "Kitty" not in Nearby:
                                    $ Nearby.append("Kitty")    
                        if "Laura" in Girls and "Laura" not in Nearby:
                                    $ Nearby.append("Laura")  

    #end two-girl option
    elif len(Girls) > 2:
            # there are two+ girls
            "You see several girls are in the room, who would you like to sit near?"                            
            while len(Adjacent) < 2:
                    menu:
                        "Select up to two."
                        "Rogue" if "Rogue" in Girls:
                                $ R_Loc = "bg classroom"
                                $ Adjacent.append("Rogue")
                        "Kitty" if "Kitty" in Girls:
                                $ K_Loc = "bg classroom"
                                $ Adjacent.append("Kitty")    
                        "Laura" if "Laura" in Girls:
                                $ L_Loc = "bg classroom"
                                $ Adjacent.append("Laura")                                
                        "Done":                                
                                $ Adjacent.append("junk")      
                                $ Adjacent.append("junk2") 
                    
            if "junk" in Adjacent:
                    $ Adjacent.remove("junk")
            if "junk2" in Adjacent:
                    $ Adjacent.remove("junk2") 
            if len(Adjacent) == 2:
                    "You sit between [Adjacent[0]] and [Adjacent[1]]."
            elif Adjacent:
                    "You sit next to [Adjacent[0]]."
            else:
                    "You sit off to the side."
                                
            if len(Girls) > len(Adjacent):
                
                    #if there were girls not picked
                    "The rest are scattered around the room."                    
                    if "Rogue" in Girls and "Rogue" not in Adjacent and "Rogue" not in Nearby:
                                $ Nearby.append("Rogue") 
                    if "Kitty" in Girls and "Kitty" not in Adjacent and "Kitty" not in Nearby:
                                $ Nearby.append("Kitty")    
                    if "Laura" in Girls and "Laura" not in Adjacent and "Laura" not in Nearby:
                                $ Nearby.append("Laura")    
                                
    #end two-girl option
    elif Girls:
            # there is one girl
            menu:
                "You see [Girls[0]] is there, do you sit next to her?"
                "Yes":
                        $ Adjacent.append(Girls[0])
                "No, I'll sit away from her a bit.":
                        $ Nearby.append(Girls[0]) 
    #end one-girl option
    #else: no girls at all
    
    if "Rogue" in Girls and "Rogue" in Nearby:
            $ R_Loc = "nearby"
    if "Kitty" in Girls and "Kitty" in Nearby:
            $ K_Loc = "nearby"   
    if "Laura" in Girls and "Laura" in Nearby:
            $ L_Loc = "nearby"
           
    if Adjacent:
            call Shift_Focus(Adjacent[0])
    call Set_The_Scene(Quiet=1)
    
    return
    
# end Class Room Interface //////////////////////////////////////////////////////////////////////


# Danger Room Interface //////////////////////////////////////////////////////////////////////

label Danger_Room_Entry:
    if "locked" in P_Traits:
            $ P_Traits.remove("locked")
    $ bg_current = "bg dangerroom"       
    $ Nearby = []     
    call Taboo_Level
    $ P_RecentActions.append("traveling")
    call EventCalls
    call Gym_Clothes("pre")#Automatically puts them in gym clothes if they've been here
    call Set_The_Scene
    
label Danger_Room:
    $ bg_current = "bg dangerroom"  
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling") 
    call Taboo_Level
    call Set_The_Scene(Quiet=1) 
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                if Current_Time == "Night":   
                    "You're getting tired, you head back to your room."
                    jump Player_Room
                call Wait   
                call EventCalls
                call Gym_Clothes("exit")
                call Girls_Location 
                call Gym_Clothes                
    call GirlsAngry  
    #End Room Set-up
    
# Danger Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
    menu:
        "This is the Danger Room. What would you like to do?" 
#        extend ""        
        "Train" if Current_Time != "Night":
                if Current_Time == "Night":
                        "The Danger Room has been powered off for the night, maybe take a break."
                if Round >= 30:
                        jump Training
                else:
                        "There really isn't time to do much before the next rotation, maybe wait a bit."
                    
        "Chat":
                call Chat
        "Historical Simulator":    
                ch_danger "This function allows you to revisit previous events in your history."
                call Danger_Room_Historia
              
        "Lock the door" if "locked" not in P_Traits:
                    if Current_Time == "Night":
                            "You lock the door"
                            $ P_Traits.append("locked")
                            call Taboo_Level
                    else:
                            "You can't really do that during free hours."
                            
        "Unlock the door" if "locked" in P_Traits:
                    "You unlock the door"
                    $ P_Traits.remove("locked")
                    call Taboo_Level        
                    
        "Wait. (locked)" if Current_Time == "Night":
                pass
        "Wait." if Current_Time != "Night":
                "You hang out for a bit."
                call Wait   
                call EventCalls
                call Gym_Clothes("exit")
                call Girls_Location 
                call Gym_Clothes
                      
        "Leave" if not TravelMode:       
                    call Gym_Clothes("change")
                    call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:         
                    call Gym_Clothes("change")
                    jump Campus_Entry
                    
        "Go to the showers" if TravelMode:             
                call Gym_Clothes("change")
                jump Shower_Room_Entry         
    jump Danger_Room

label Training:
    $ D20 = renpy.random.randint(1, 20)
#    if D20 > 10 and R_Inbt >= 500:
#        call Rogue_Frisky_Danger
        
    $ P_XP += (5 + (int(Round / 10)))
    $ P_DailyActions.append("dangerroom")
    call Set_The_Scene
    
    if Round >= 80:
            $ Line = "You have a long session in the Danger Room."
    elif Round >= 50:
            $ Line = "You have a short workout in the Danger Room."
    else:
            $ Line = "You squeeze in a quick session in the Danger Room."
        
    $ Trigger = 0
    if D20 >= 18:
            #if "cyclops":
            "[Line] During the exercise, Cyclops accidentally shoots you."
            "Luckily you're immune to the beams, but your clothes weren't so lucky."
            call RoomStatboost("Love",80,2)
            call RoomStatboost("Lust",80,5)
    elif D20 >= 17:
            "[Line] You participate in a hand-to-hand combat class." 
            "Before you begin, Cyclops explains that it’s always good to know how to defend yourself when you can’t rely on your powers."
            "It sounds like there’s a story there."
    elif D20 >= 16:
            "Some of the senior students walk over to talk about your powers."
            "Nightcrawler wonders aloud what would happen if he grabbed you and tried to teleport while you tried to disable his powers."
            "You succeed in freaking each other out."
    else:
            $ Line = Line + renpy.random.choice([" It was fairly boring.", 
                    " You do some training with basic firearms.", 
                    " You run the obstacle course.",
                    " You fight in a simulated battle against the Brotherhood.",
                    " You help take down a holographic Sentinel.",
                    " You take part in a training exercise against the Avengers. As if the X-Men and Avengers would ever fight.",                     
                    " You and some of the others take part in a survival exercise. . . also known as \"try to last as long as you can while Wolverine hunts you down one by one.\"",
                    " You decide to test yourself by facing off against Magneto solo. It goes about as well as you’d expect.",
                    " You use the Danger Room’s holograms to relive some of the original X-Men’s biggest battles. You learn quite a bit about teamwork.", 
                    " Beast is teaching a class on parkour. You take part and pick up a few pointers. You’re no Spider-Man, but at least you pick up a few things.",  
                    " You participate in an emergency drill. You pick up quite a few tips about first aid, triage and the proper way to move injured people.", 
                    " You take part in an urban emergency situation exercise. Cyclops takes the time to explain to you how to use cover to get close enough to use your powers.", 
                    " You take part in a jungle simulation exercise under Wolverine. You learn some basic survival techniques, but you privately hope you never need them.", 
                    " Your team fight a simulation of Magneto."])   
            "[Line]"    
    if R_Loc == bg_current:
        call Rogue_TightsRipped
    
    call Wait
    call Girls_Location 
    call Set_The_Scene
    $ Line = "The training session has ended, what would you like to do next?"
    
    jump Danger_Room

label Rogue_TightsRipped(Count = 0):
        if R_Hose == "tights":
                $ Count = 1
                $ R_Hose = "ripped tights"    
                call RogueFace("angry")
                if "ripped tights" in R_Inventory:  
                    ch_r "Damnation, that's another pair ruined!"
                else:
                    $ Count = 2               
                    ch_r "Well that's a good pair of tights down the chute."                
        elif R_Hose == "pantyhose":
                $ Count = 1
                $ R_Hose = "ripped pantyhose"              
                call RogueFace("angry")
                if "ripped pantyhose" in R_Inventory:  
                    ch_r "Tsk, another pair ruined!"
                else:
                    $ Count = 2               
                    ch_r "I hate getting a run in these things."     
        if Count:
                #If they ripped
                if not R_Legs and R_Panties != "shorts":
                        if R_Panties: 
                            if R_SeenPanties:
                                $ Count = 3 if not ApprovalCheck("Rogue", 600) else Count
                            else:
                                $ R_SeenPanties = 1
                                $ Count = 3 if not ApprovalCheck("Rogue", 900) else Count                            
                            call Statup("Rogue", "Lust", 60, 2)
                        else:
                            if R_SeenPussy:
                                $ Count = 3 if not ApprovalCheck("Rogue", 900) else Count
                            else:
                                call Rogue_First_Bottomless 
                                $ Count = 3 if not ApprovalCheck("Rogue", 1400) else Count
                            
                if Count == 2: 
                        #first time
                        menu:
                            extend ""
                            "I think those look really good on you.":                
                                call RogueFace("smile", 1)                     
                                $ R_Inventory.append(R_Hose) 
                                ch_r "You think so? That's sweet, maybe I'll keep them on hand." 
                            "Yeah, too bad.":             
                                call RogueFace("bemused")    
                                ch_r ". . ."         
                            "Ha! Those don't leave much to the imagination!":                        
                                ch_r "Thanks for that. . ."
                                
                elif Count == 3: #She is embarassed and takes off             
                    call RogueFace("startled", 2)  
                    ch_r "I, um, I should get out of here."
                    $ R_Blush = 1
                    call Remove_Girl("Rogue")
                    call RogueOutfit
                #end "if they ripped"
        return
                
# end Danger Room Interface //////////////////////////////////////////////////////////////////////


# Danger Room Interface //////////////////////////////////////////////////////////////////////

label Pool_Entry:
    if "locked" in P_Traits:
            $ P_Traits.remove("locked")
    $ bg_current = "bg pool"       
    $ Nearby = []     
    call Taboo_Level
    $ P_RecentActions.append("traveling")
    call EventCalls
    call Gym_Clothes
    call Set_The_Scene
    
label Pool_Room:
    $ bg_current = "bg pool"  
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling") 
    call Taboo_Level
    call Set_The_Scene(Quiet=1,Dress=0) 
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                if Current_Time == "Night":   
                    "You're getting tired, you head back to your room."
                    jump Player_Room
                call Wait   
                call EventCalls
                call Girls_Location            
    call GirlsAngry  
    #End Room Set-up
    
# Pool Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
    menu:
        "You're at the pool. What would you like to do?" 
                    
        "Chat":
                call Chat    
        
        "Want to sunbathe?":
            call Pool_Sunbathe
        "Want to swim?":
            call CleartheRoom(Check=1)
            if Current_Time == "Night" and not _return:
                "It's a bit late for a swim." 
            else:                
                call Pool_Swim
        "Want to skinnydip?":
            call Pool_Skinnydip
                        
        "Wait. (locked)" if Current_Time == "Night":
                pass
        "Wait." if Current_Time != "Night":
                "You hang out for a bit."
                call Wait   
                call EventCalls
                call Girls_Location 
                      
        "Leave" if not TravelMode:       
                    call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:      
                    jump Campus_Entry
                    
        "Go to the showers" if TravelMode:   
                jump Shower_Room_Entry         
    jump Pool_Room

label Pool_Swim:
    $ D20 = renpy.random.randint(1, 20)
        
    $ P_DailyActions.append("swim")
    call Set_The_Scene
    
    $ Line = 0
    if bg_current == R_Loc and ApprovalCheck("Rogue", 900):                                
            if ChestNum("Rogue") or OverNum("Rogue") or PantiesNum("Rogue") or PantsNum("Rogue") or HoseNum("Rogue"):                
                    call AnyOutfit("Rogue","swimwear")
            $ Line = "Rogue"            
            call AnyWord("Rogue",0,"swim","swim")  #adds "swim" tag to recent and daily actions             
    if bg_current == K_Loc and ApprovalCheck("Kitty", 900):   
            if ChestNum("Kitty") or OverNum("Kitty") or PantiesNum("Kitty") or PantsNum("Kitty") or HoseNum("Kitty"):          
                    call AnyOutfit("Kitty","swimwear")
            $ Line = "Kitty" if Line > 0 else -1 #should be -1 if there are multiple girls, otherwise name.
            call AnyWord("Kitty",0,"swim","swim")  #adds "swim" tag to recent and daily actions 
    if bg_current == E_Loc and ApprovalCheck("Emma", 900):   
            if ChestNum("Emma") or OverNum("Emma") or PantiesNum("Emma") or PantsNum("Emma") or HoseNum("Emma"):           
                    call AnyOutfit("Emma","swimwear")
            $ Line = "Emma" if Line > 0 else -1
            call AnyWord("Emma",0,"swim","swim")  #adds "swim" tag to recent and daily actions 
    if bg_current == L_Loc and ApprovalCheck("Laura", 900):  
            if ChestNum("Laura") or OverNum("Laura") or PantiesNum("Laura") or PantsNum("Laura") or HoseNum("Laura"):             
                    call AnyOutfit("Laura","swimwear")
            $ Line = "Laura" if Line > 0 else -1
            call AnyWord("Laura",0,"swim","swim")  #adds "swim" tag to recent and daily actions 
    if Line == -1:
        "The girls get changed and join you."
    elif Line:
        "[Line] gets changed and joins you." 
        
    call ShowPool #displays pool graphics
    
    if D20 >= 15:
            call Pool_Topless
            
    if D20 >= 11:
            "You take a nice, refreshing swim." 
    elif D20 == 2:
            "You join some of the others in a rousing game of Marco Polo."
    elif D20 == 3:
            "You manage to snag one of the floating chairs and drift lazily on the water." 
    elif D20 == 4:
            "You manage to snag one of the floating chairs and drift lazily on the water."
            "Until, that is, Kurt teleports up in the air nearby and performs an admittedly awesome cannonball."
            "Too bad it capsizes your chair."
    elif D20 == 5:
            "You test yourself by swimming from one end of the pool to the other."
    elif D20 == 6:
            "You try to impress some of the girls by doing a running jump into the pool."
            "You wind up triggering a cannonball competition that’s ironically NOT won by Cannonball, much to his shock." 
    elif D20 == 7:
            "You are about to get into the pool when you hear annoyed cries and shouts of, \"Bobby!\""
            "Looks like Iceman made himself a floating chair again."
            "You stick to the far end of the pool, where it isn’t freezing cold."
    elif D20 == 8:
            "You relax on one of the poolside chairs instead." 
    elif D20 == 9:
            "Cyclops is instructing some of the other students in water rescues."
            "You listen in as he talks about approaching a drowning victim from behind so that their panicked flailing won’t cause you injury."  
    elif D20 == 10:
            "You decide to make use of the diving board. You do a couple of dives before taking it easy and just swimming around." 
            
    $ Line = 0
    call GirlWaitAttract(1,3,80) #makes any girls in the room like each other a bit more.
    call RoomStatboost("Love",80,3)
    call RoomStatboost("Lust",30,5)
    $ Round -= 20 if Round >= 20 else Round    
    hide FullPool
    call Set_The_Scene(1,0,0)
    "You all get out of the pool and rest for a bit."
    return   
                
# end Pool Interface //////////////////////////////////////////////////////////////////////


image FullPool:
        #water
        AlphaMask("bg_pool", "images/PoolMask.png")
        
label ShowPool(DLoc=0):
        #displays the pool with girls in it
        if R_Loc == bg_current:
                    $ R_Water = 1
                    $ DLoc = 500 if Ch_Focus == "Rogue" else 650                        
                    show Rogue zorder RogueLayer:
                            alpha 1
                            zoom .45
                            offset (0,0)
                            anchor (0.5, 0.0)  
                            pos (DLoc,450)   
                    show Rogue at Pool_Bob
        if K_Loc == bg_current:
                    $ K_Water = 1
                    $ DLoc = 500 if Ch_Focus == "Kitty" else 650 
                    show Kitty_Sprite zorder KittyLayer:
                            alpha 1
                            zoom .45
                            offset (0,0)
                            anchor (0.5, 0.0)  
                            pos (DLoc,450)  
                    show Kitty_Sprite at Pool_Bob
        if E_Loc == bg_current:
                    $ E_Water = 1
                    $ DLoc = 500 if Ch_Focus == "Emma" else 650 
                    show Emma_Sprite zorder EmmaLayer:
                            alpha 1
                            zoom .45
                            offset (0,0)
                            anchor (0.5, 0.0)  
                            pos (DLoc,450)  
                    show Emma_Sprite at Pool_Bob
        if L_Loc == bg_current:
                    $ L_Water = 1
                    $ DLoc = 500 if Ch_Focus == "Laura" else 650 
                    show Laura_Sprite zorder LauraLayer:
                            alpha 1
                            zoom .45
                            offset (0,0)
                            anchor (0.5, 0.0)  
                            pos (DLoc,450)   
                    show Laura_Sprite at Pool_Bob            
        show FullPool zorder 175 #should put masked pool above girls
        return
        
transform Pool_Bob():     
        subpixel True 
        xoffset 0
        yoffset 0
        choice:
            yoffset 0
        choice:
            pause .3
        choice:
            pause .5
        block:     
            ease 1 yoffset 10 
            ease 1.5 yoffset 0 
            repeat
        
# Showers Interface //////////////////////////////////////////////////////////////////////
label Shower_Room_Entry:
    $ bg_current = "bg showerroom"      
    if "locked" in P_Traits:
            $ P_Traits.remove("locked")  
    $ Nearby = []             
    call Gym_Clothes  
    call Taboo_Level
    call Set_The_Scene(0,1,0)
    if Round <= 10 or len(Party) >= 2:         
            jump Shower_Room
                        
    $ Options = []
    if "Rogue" not in Party and "showered" not in R_DailyActions and (R_Loc == "bg rogue" or R_Loc == "bg dangerroom"):  #Checks if Rogue is in the shower
            $ Options.append("Rogue")   
    if "Kitty" not in Party and "showered" not in K_DailyActions and (K_Loc == "bg kitty" or K_Loc == "bg dangerroom"):  #Checks if Kitty is in the shower
            $ Options.append("Kitty")     
    if "Emma" not in Party and "showered" not in E_DailyActions and (E_Loc == "bg emma" or E_Loc == "bg dangerroom"):  #Checks if Emma is in the shower
            $ Options.append("Emma")   
    if "Laura" not in Party and "showered" not in L_DailyActions and (L_Loc == "bg laura" or L_Loc == "bg dangerroom"):  #Checks if Laura is in the shower
            $ Options.append("Laura")
    if Options:        
            $ renpy.random.shuffle(Options)
    
    while Options and (len(Options) + len(Party) > 2):        
                # culls out list to 2 if there is a party
                $ Options.remove(Options[0])
    
    $ D20 = renpy.random.randint(1, 20) 
    # <5 is they show up late, 5-10 is they haven't showered yet, 10-15 is they finished, 
    # >15 is you walk in on them, >17 they might be masturbating
        
    if not Options or D20 < 5:  
                # if nobody is around, skip it.
                # if < 5, they show up late
                $ Nearby = Options[:]
                if "Rogue" in Options:
                        $ R_Loc = "nearby"  
                if "Kitty" in Options:
                        $ K_Loc = "nearby" 
                if "Emma" in Options:
                        $ E_Loc = "nearby"  
                if "Laura" in Options:
                        $ L_Loc = "nearby"  
                jump Shower_Room

    if D20 > 15 and Options[0]:                    
            call Girl_Caught_Shower(Options[0])
            if _return:
                jump Campus_Map #if there is a return value, jump to the campus, but not otherwise
            jump Shower_Room
    #End Caught Check
    
    # If none of the caught dialogs plays, checks to see if anyone is in the room, and allows them to be there if they are. 
    if "Rogue" in Options:        
            $ R_Loc = bg_current  
    if "Kitty" in Options:
            $ K_Loc = bg_current  
    if "Emma" in Options:
            $ E_Loc = bg_current  
    if "Laura" in Options:
            $ L_Loc = bg_current  
    call Present_Check
    
    if R_Loc == bg_current and "Rogue" not in Party:
            if D20 >= 10:
                    $ R_RecentActions.append("showered")                      
                    $ R_DailyActions.append("showered")  
            call RogueOutfit("towel") 
    if K_Loc == bg_current and "Kitty" not in Party:
            if D20 >= 10:
                    $ K_RecentActions.append("showered")                      
                    $ K_DailyActions.append("showered")   
            call KittyOutfit("towel") 
    if E_Loc == bg_current and "Emma" not in Party:
            if D20 >= 10:
                    $ E_RecentActions.append("showered")                      
                    $ E_DailyActions.append("showered") 
            call EmmaOutfit("towel")   
    if L_Loc == bg_current and "Laura" not in Party:
            if D20 >= 10:
                    $ L_RecentActions.append("showered")                      
                    $ L_DailyActions.append("showered")  
            call LauraOutfit("towel")  
    #End Count set-up
    
    call Set_The_Scene(Dress=0)
    if len(Options) >= 2:    
        "As you enter, you see [Options[0]] and [Options[1]] standing there."           
    elif Options:
        "As you enter, you see [Options[0]] standing there."
        
    if Options:          
            $ Line = 0
            if Options[0] == "Rogue":
                    ch_r "Hey, [R_Petname]."
                    if "showered" in R_RecentActions:                    
                            ch_r "I was just getting ready to head out." 
            if Options[0]  == "Kitty":
                    ch_k "Hey, [K_Petname]."
                    if "showered" in K_RecentActions:
                            ch_k "I just got finished."
            if Options[0]  == "Emma":
                    ch_e "Oh, hello, [E_Petname]." 
                    if "showered" in E_RecentActions:
                            ch_e "I was about finished here." 
            if Options[0]  == "Laura":
                    ch_l "Oh, hey." 
                    if "showered" in L_RecentActions:
                            ch_l "I'm done here." 
                            
            if len(Options) >= 2:                               
                    if Options[1] == "Rogue":
                            ch_r "Yeah, hey."
                    if Options[1] == "Kitty":
                            ch_k "Yeah, hi."
                    if Options[1] == "Emma":
                            ch_e "Yes, hello."
                    if Options[1] == "Laura":
                            ch_l "Hey."
                            
            # End welcomes
            if "Rogue" in Party:
                    ch_r "Hey, [Options[0]]."
            if "Kitty" in Party:
                    ch_k "Hi, [Options[0]]."
            if "Emma" in Party:
                    ch_e "Oh, hello, [Options[0]]."
            if "Laura" in Party:
                    ch_l "Hey."
                    
    # End Reply portion
    
    $ Options = []
            
    
# Shower Room Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Shower_Room:
    $ bg_current = "bg showerroom" 
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")  
    call Taboo_Level 
    call Set_The_Scene(Dress=0)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                if Current_Time == "Night":   
                    "You're getting tired, you head back to your room."
                    jump Player_Room
                call Wait   
                call EventCalls
                call Girls_Location 
    call GirlsAngry      
    #End Room Set-up

# Shower Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    menu:
        "You're in the showers. What would you like to do?"

        "Chat":
                call Chat
            
        "Shower" if Round > 30:             
                call Showering
        "Shower [[no time](locked)" if Round <= 30:            
                pass
            
        "Lock the door" if "locked" not in P_Traits:
                    "You lock the door"
                    $ P_Traits.append("locked")                    
                    $ Nearby = []             
                    call Taboo_Level
                   
        "Unlock the door" if "locked" in P_Traits:
                    "You unlock the door"
                    $ P_Traits.remove("locked")
                    call Taboo_Level      
                    
        "Wait." if Current_Time != "Night":
                "You hang out for a bit."
                "In the showers."
                "Not gonna lie, kinda weird."
                call Wait   
                call EventCalls            
                call Girls_Location 
                
                #this bit sets up drop-in characters
                $ Nearby = []
                if R_Loc != bg_current and "showered" not in R_DailyActions and (R_Loc == "bg rogue" or R_Loc == "bg dangerroom"):  #Checks if Rogue is in the shower
                        $ Nearby.append("Rogue")   
                if K_Loc != bg_current and "showered" not in K_DailyActions and (K_Loc == "bg kitty" or K_Loc == "bg dangerroom"):  #Checks if Kitty is in the shower
                        $ Nearby.append("Kitty")     
                if E_Loc != bg_current and "showered" not in E_DailyActions and (E_Loc == "bg emma" or E_Loc == "bg dangerroom"):  #Checks if Emma is in the shower
                        $ Nearby.append("Emma")   
               #if L_Loc != bg_current and "showered" not in L_DailyActions and (L_Loc == "bg laura" or L_Loc == "bg dangerroom"):  #Checks if Laura is in the shower
               #       $ Nearby.append("Laura")
                if Nearby:        
                        $ renpy.random.shuffle(Nearby)
                        while len(Nearby) > 2:        
                                    # culls out list to 2 if there is a party
                                    $ Nearby.remove(Nearby[0])
                        if renpy.random.randint(1, 20) < 5:  
                            if "Rogue" in Nearby:
                                    $ R_Loc = "nearby"  
                            if "Kitty" in Nearby:
                                    $ K_Loc = "nearby" 
                            if "Emma" in Nearby:
                                    $ E_Loc = "nearby"  
                            if "Laura" in Nearby:
                                    $ L_Loc = "nearby"   
        "Wait.  [[no time](locked)" if Current_Time == "Night":
                pass
                
        "Go to the Danger Room" if TravelMode: 
                call No_Towels
                jump Danger_Room_Entry 
        "Return to Your Room" if TravelMode:  
                call No_Towels
                jump Player_Room_Entry   
        "Girl's Rooms" if TravelMode:
            menu:
                "Rogue's Room":   
                            call No_Towels
                            jump Rogue_Room_Entry 
                "Kitty's Room" if "met" in K_History:  
                            call No_Towels 
                            jump Kitty_Room_Entry   
                "Emma's Room" if "met" in E_History:  
                            call No_Towels 
                            jump Emma_Room_Entry  
                "Laura's Room" if "met" in L_History: 
                            call No_Towels
                            jump Laura_Room_Entry  
                "Back":
                            pass                              
        "Leave" if not TravelMode:
                call QuickEvents  
                call No_Towels        
                call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
                call QuickEvents   
                call No_Towels       
                jump Campus_Entry
                    
    jump Shower_Room

# Shower Room Menu End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label No_Towels:
    #Removes their towels if playher is leaving the showers
    if R_Over == "towel":
            $ R_Outfit = R_OutfitDay
            call RogueOutfit
            $ R_Water = 0
    elif K_Over == "towel":
            $ K_Outfit = K_OutfitDay
            call KittyOutfit
            $ K_Water = 0
    elif E_Over == "towel":
            $ E_Outfit = E_OutfitDay
            call EmmaOutfit
            $ E_Water = 0
    elif L_Over == "towel":
            $ L_Outfit = L_OutfitDay
            call LauraOutfit
            $ L_Water = 0
    return
    
label Showering(Occupants = [], StayCount=[] , Showered = 0, Line = 0):
    # Occupants tallies how many girls are here. 
    # StayCount tallies how many girls are willing to stick around. 
        
    if R_Loc == "bg showerroom":
            $ Occupants.append("Rogue")
    if K_Loc == "bg showerroom":   
            $ Occupants.append("Kitty")
    if E_Loc == "bg showerroom":   
            $ Occupants.append("Emma")
    if L_Loc == "bg showerroom":  
            $ Occupants.append("Laura")
        
    if Occupants:
            ch_p "I'm taking a shower, care to join me?" 
            if Occupants[0] == "Rogue" and "showered" in R_RecentActions:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there
                        ch_r "We actually just finished up, so we'll head out."
                    else:
                        ch_r "I actually just finished up, so I'll head out."
                    $ Showered = 1
            elif Occupants[0] == "Kitty" and "showered" in K_RecentActions:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there
                        ch_k "We actually just showered, so we're heading out."
                    else:
                        ch_k "I actually just showered, so I'm heading out."
                    $ Showered = 1
            elif Occupants[0] == "Emma" and "showered" in E_RecentActions:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there                        
                        ch_e "We were actually finishing up, so we're heading out."
                    else:
                        ch_e "I was actually finishing up, so I'm heading out."
                    $ Showered = 1
            elif Occupants[0] == "Laura" and "showered" in L_RecentActions:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there                        
                        ch_l "We were done, actually."
                    else:
                        ch_l "I'm heading out now."
                    $ Showered = 1
            else:
                #None of them have showered yet
                if Occupants[0] == "Rogue":
                        if ApprovalCheck("Rogue", 1200) or (ApprovalCheck("Rogue", 600) and R_SeenChest and R_SeenPussy):
                                    # Rogue says yes
                                    ch_r "I suppose I could stick around. . ."
                                    $ StayCount.append("Rogue") 
                        else:
                                    # Rogue says no
                                    ch_r "Nah, I should probably get going."
                            
                elif Occupants[0] == "Kitty":
                        if ApprovalCheck("Kitty", 1400) or (ApprovalCheck("Kitty", 700) and K_SeenChest and K_SeenPussy):
                                    ch_k "Yeah, I could stick around."
                                    $ StayCount.append("Kitty")
                        else:
                                    ch_k "I've got to get going."
                                
                elif Occupants[0] == "Emma":
                        if not "classcaught" in E_History or "three" not in E_History:
                                ch_e "I really should be going. . ."
                        elif ApprovalCheck("Emma", 1400) or (ApprovalCheck("Emma", 700) and E_SeenChest and E_SeenPussy):
                                    ch_e "I suppose I could stay, for a bit."
                                    $ StayCount.append("Emma")
                        else:
                                    ch_e "I'm afraid I really must be going."
                                    
                elif Occupants[0] == "Laura":
                        if ApprovalCheck("Laura", 1400) or (ApprovalCheck("Laura", 700) and L_SeenChest and L_SeenPussy):
                                    ch_l "I got nothing better to do."
                                    $ StayCount.append("Laura")
                        else:
                                    ch_l "I gotta get going."
                #end first girls
                          
                if len(Occupants) >= 2:
                    #seond girls
                    if Occupants[1] == "Rogue":
                        if ApprovalCheck("Rogue", 1200) or (ApprovalCheck("Rogue", 600) and R_SeenChest and R_SeenPussy):
                                if StayCount:                          
                                    #If Rogue said yes
                                    ch_r "I could stick around too. . ."
                                else:                     
                                    #If Rogue said no
                                    ch_r "Well, I could probably stay."
                                $ StayCount.append("Rogue")
                        else:
                                if StayCount:#RogueCount > 1:                          
                                    #If Rogue said yes
                                    ch_r "I can't though . ."
                                else:                     
                                    #If Rogue said no
                                    ch_r "I should get going too."
                            
                    if Occupants[1] == "Kitty":
                        if ApprovalCheck("Kitty", 1400) or (ApprovalCheck("Kitty", 700) and K_SeenChest and K_SeenPussy):
                                if StayCount:                          
                                    #If Rogue said yes
                                    ch_k "I guess I could stay too. . ."
                                else:                     
                                    #If Rogue said no
                                    ch_k "Well, I could stay though."
                                $ StayCount.append("Kitty")
                        else:
                                if StayCount:#RogueCount > 1:                          
                                    #If Rogue said yes
                                    ch_k "I've really got to go though. . ."
                                else:                     
                                    #If Rogue said no
                                    ch_k "Yeah, I should head out too."
                                
                    elif Occupants[1] == "Emma":
                        if not "classcaught" in E_History or "three" not in E_History:
                                ch_e "I really should be going. . ."
                        elif ApprovalCheck("Emma", 1400) or (ApprovalCheck("Emma", 700) and E_SeenChest and E_SeenPussy):
                                if StayCount:                          
                                    #If Rogue said yes
                                    ch_e "I suppose I could also stay. . ."
                                else:                     
                                    #If Rogue said no
                                    ch_e "But {i}I{/i} could stick around. . ."
                                $ StayCount.append("Emma")
                        else:
                                if StayCount:                       
                                    #If Rogue said yes
                                    ch_e "But I really must be going. . ."
                                else:                     
                                    #If Rogue said no
                                    ch_e "Yes, let's go."
                                    
                    elif Occupants[1] == "Laura":
                        if ApprovalCheck("Laura", 1400) or (ApprovalCheck("Laura", 700) and L_SeenChest and L_SeenPussy):
                                if StayCount:                          
                                    #If Rogue said yes
                                    ch_l "I could stay too. . ."
                                else:                     
                                    #If Rogue said no
                                    ch_l "I could stick around."
                                $ StayCount.append("Laura")
                        else:
                                if StayCount:                        
                                    #If Rogue said yes
                                    ch_l "I gotta get going though. . ."
                                else:                     
                                    #If Rogue said no
                                    ch_l "Yeah, me too."
                #end none have showered yet
                            
            if len(Occupants) > len(StayCount):                    
                    #if either said no. If they're at StayCount = 2 here, they have already agreed.
                    
                    menu:
                        extend ""
                        "Ok, see you later then.":
                                if R_Loc == bg_current and "Rogue" not in StayCount:
                                    ch_r "Yeah, later."
                                if K_Loc == bg_current and "Kitty" not in StayCount:
                                    ch_k "Bye!"
                                if E_Loc == bg_current and "Emma" not in StayCount:
                                    ch_e "Yes, later."
                                if L_Loc == bg_current and "Laura" not in StayCount:
                                    ch_l "Yup."
                            
                        "Sure you got every spot?" if Showered:
                                $ Line = "spot"
                                                            
                        #fix Add "Take off your own clothes" option.
                        
                        "Maybe you could stay and watch?":
                                $ Line = "watch me"
                            
                        "But I didn't get to watch." if Showered:
                                $ Line = "watch you"
                            
                    if Line:
                        if R_Loc == bg_current and "Rogue" not in StayCount:
                                if ApprovalCheck("Rogue", 1200) or (ApprovalCheck("Rogue", 600) and R_SeenChest and R_SeenPussy):
                                    $ StayCount.append("Rogue") 
                                elif Line == "spot" and ApprovalCheck("Rogue", 1000, "LI"):     
                                    $ StayCount.append("Rogue") 
                                elif Line == "watch you" and ApprovalCheck("Rogue", 600, "O"):    
                                    $ StayCount.append("Rogue") 
                                #else, she doesn't agree
                                
                        if K_Loc == bg_current and "Kitty" not in StayCount:
                                if ApprovalCheck("Kitty", 1400) or (ApprovalCheck("Kitty", 700) and K_SeenChest and K_SeenPussy):
                                    $ StayCount.append("Kitty") 
                                elif Line == "spot" and ApprovalCheck("Kitty", 1200, "LI"):     
                                    $ StayCount.append("Kitty") 
                                elif Line == "watch you" and ApprovalCheck("Kitty", 600, "O"):   
                                    $ StayCount.append("Kitty") 
                                #else, she doesn't agree
                                
                        if E_Loc == bg_current and "Emma" not in StayCount:                            
                                if not "classcaught" in E_History or (StayCount and "three" not in E_History):
                                    pass
                                elif ApprovalCheck("Emma", 1400) or (ApprovalCheck("Emma", 700) and E_SeenChest and E_SeenPussy):
                                    $ StayCount.append("Emma") 
                                elif Line == "spot" and ApprovalCheck("Emma", 1100, "LI"):     
                                    $ StayCount.append("Emma") 
                                elif Line == "watch you" and ApprovalCheck("Emma", 550, "O"):   
                                    $ StayCount.append("Emma") 
                                #else, she doesn't agree
                        
                        if L_Loc == bg_current and "Laura" not in StayCount:
                                if ApprovalCheck("Laura", 1400) or (ApprovalCheck("Emma", 700) and L_SeenChest and L_SeenPussy):
                                    $ StayCount.append("Laura") 
                                elif Line == "spot" and ApprovalCheck("Emma", 1200, "LI"):     
                                    $ StayCount.append("Laura") 
                                elif Line == "watch you" and ApprovalCheck("Emma", 600, "O"):   
                                    $ StayCount.append("Laura") 
                                #else, she doesn't agree
                        
                        if Line == "spot":      
                                #"Sure you got every spot?"
                                if StayCount:
                                        #if at least one girl agreed to stay
                                        if StayCount[0] == "Rogue": #RogueCount == 2:                                 
                                            #Rogue agreed
                                            ch_r "Fine, I could use another scrub."                                                
                                        elif StayCount[0] == "Kitty":                               
                                            #Kitty agreed
                                            ch_k "Oh, I guess I could take another pass at it."                                            
                                        elif StayCount[0] == "Emma":                               
                                            #Emma agreed
                                            ch_e "I suppose we could take a look. . ."                                         
                                        elif StayCount[0] == "Laura":                               
                                            #Laura agreed
                                            ch_l "Well, maybe. . ."
                                
                                        if len(StayCount) > 1:
                                                #if there are multiple girls                                    
                                                if StayCount[1] == "Rogue":                               
                                                    #Rogue too
                                                    ch_r "Sure."                                      
                                                elif StayCount[1] == "Kitty":                               
                                                    #Kitty too
                                                    ch_k "Um, me too!"                                 
                                                elif StayCount[1] == "Emma":                               
                                                    #Emma too
                                                    ch_e "Oh, fine. . ."                           
                                                elif StayCount[1] == "Laura":                               
                                                    #Laura too
                                                    ch_l "Yeah."                                    
                                    
                                if R_Loc == bg_current and "Rogue" not in StayCount: #RogueCount == 1:                                  
                                    #Rogue refused
                                    if StayCount:
                                            ch_r "Well, [R_Petname], I think I'm fine."
                                    else:
                                            ch_r "No, [R_Petname], I think I'm covered."
                                if K_Loc == bg_current and "Kitty" not in StayCount: # KittyCount == 1:                                  
                                    #Kitty refused
                                    if StayCount:
                                            ch_k "Oh, well I think I[K_like]got it?"
                                            ch_k "See you later, [K_Petname]."
                                    else:
                                            ch_k "Ha, I'm squeeky clean, [K_Petname], see you later."       
                                if E_Loc == bg_current and "Emma" not in StayCount:
                                    #Emma refused
                                    if StayCount:
                                            ch_e "Well it appears you'll be taken care of."
                                            ch_e "I'll be going, [E_Petname]."
                                    else:
                                            ch_e "I'm afraid not, [E_Petname], I'll be going."       
                                if L_Loc == bg_current and "Laura" not in StayCount:
                                    #Laura refused
                                    if StayCount:
                                            ch_l "Looks like you got this handled."
                                            ch_l "I'm out, [L_Petname]."
                                    else:
                                            ch_l "I'm out."         
                                #end "missed a spot?"    
                            
                        elif Line == "watch me":  
                                #"Maybe you could stay and watch?"
                                if StayCount:
                                        if StayCount[0] == "Rogue":                                
                                            #Rogue agreed
                                            ch_r "Yeah, I guess I do enjoy the view."                                        
                                        elif StayCount[0] == "Kitty":                               
                                            #Kitty agreed
                                            ch_k "I. . . guess I wouldn't mind that. . ."                                            
                                        elif StayCount[0] == "Emma":                               
                                            #Emma agreed
                                            ch_e "Oh, a show then?"                                        
                                        elif StayCount[0] == "Laura":                               
                                            #Laura agreed
                                            ch_l "Ok, let's see what you got."
                                
                                        if len(StayCount) > 1:
                                                #if there are multiple girls      
                                                if StayCount[1] == "Rogue":                               
                                                    #Rogue too
                                                    ch_r "Sure."                                      
                                                elif StayCount[1] == "Kitty":                               
                                                    #Kitty too
                                                    ch_k "Um, me too!"                                 
                                                elif StayCount[1] == "Emma":                               
                                                    #Emma too
                                                    ch_e "Oh, fine. . ."                           
                                                elif StayCount[1] == "Laura":                               
                                                    #Laura too
                                                    ch_l "Yeah."     
                                    
                                if R_Loc == bg_current and "Rogue" not in StayCount: #RogueCount == 1:                                  
                                    #Rogue refused
                                    if StayCount:
                                            ch_r "Oh, well, I'm gonna pass on that, [R_Petname]."
                                    else:
                                            ch_r "Yeah, I'm gonna pass on that, [R_Petname]."
                                if K_Loc == bg_current and "Kitty" not in StayCount: # KittyCount == 1:                                  
                                    #Kitty refused
                                    if StayCount:
                                            ch_k "Well, [K_like]I don't need to see that."   
                                            ch_k "See you later, [K_Petname]."
                                    else:
                                            ch_k "[K_Like]I don't need to see that."       
                                if E_Loc == bg_current and "Emma" not in StayCount:
                                    #Emma refused
                                    if StayCount:
                                            ch_e "You appear to have enough of an audience."
                                            ch_e "I'll be going, [E_Petname]."
                                    else:
                                            ch_e "I think I'll be fine, [E_Petname], I'll be going."     
                                if L_Loc == bg_current and "Laura" not in StayCount:
                                    #Laura refused
                                    if StayCount:
                                            ch_l "She's got you covered."
                                            ch_l "I'm out, [L_Petname]."
                                    else:
                                            ch_l "I'm out."         
                                #end "Watch me"
                                            
                        elif Line == "watch you": 
                                #"But I didn't get to watch."                                    
                                if StayCount:
                                        if StayCount[0] == "Rogue":                                
                                            #Rogue agreed
                                            ch_r "Well, I don't mind putting on a show."                                          
                                        elif StayCount[0] == "Kitty":                               
                                            #Kitty agreed
                                            ch_k "You want to watch me. . ."
                                            ch_k "Ok."                                                              
                                        elif StayCount[0] == "Emma":                               
                                            #Emma agreed
                                            ch_e "I suppose I can't blame you for that. . ."                                    
                                        elif StayCount[0] == "Laura":                               
                                            #Laura agreed
                                            ch_l "Huh. Suit yourself."
                                
                                        if len(StayCount) > 1:
                                                #if there are multiple girls      
                                                if StayCount[1] == "Rogue":                               
                                                    #Rogue too
                                                    ch_r "I guess I could too."                                      
                                                elif StayCount[1] == "Kitty":                               
                                                    #Kitty too
                                                    ch_k "I- yeah, me neither!"                            
                                                elif StayCount[1] == "Emma":                               
                                                    #Emma too
                                                    ch_e "I suppose I don't want to be left out of this. . ."
                                                elif StayCount[1] == "Laura":                               
                                                    #Laura too
                                                    ch_l "Fine."    
                                    
                                if R_Loc == bg_current and "Rogue" not in StayCount: #RogueCount == 1:                                  
                                    #Rogue refused
                                    if StayCount:
                                            ch_r "Really? Well not me."
                                            ch_r "Have fun, [R_Petname]."
                                    else:
                                            ch_r "Keep dreaming, [R_Petname]."
                                if K_Loc == bg_current and "Kitty" not in StayCount: # KittyCount == 1:                                  
                                    #Kitty refused
                                    if StayCount:
                                            ch_k "Seriously?! Well I'm not into that."   
                                            ch_k "Later, [K_Petname]."
                                    else:
                                            ch_k "[K_Like]no way!"     
                                if E_Loc == bg_current and "Emma" not in StayCount:
                                    #Emma refused
                                    if StayCount:
                                            ch_e "I wouldn't want to intrude."
                                            ch_e "I'll be going."
                                    else:
                                            ch_e "Hmm, I doubt you could handle it."
                                            ch_e "I'll be going."          
                                if L_Loc == bg_current and "Laura" not in StayCount:
                                    #Laura refused
                                    if StayCount:
                                            ch_l "She's got you covered."
                                            ch_l "I'm out, [L_Petname]."
                                    else:
                                            ch_l "I'm out."            
                                #end "Watch you?"
                                            
                    #end "if you asked then a question"                
                    #fix, add jeolousy angle here, if roguelikekitty low, get rid of her. . .
                            
            if R_Loc == bg_current:
                if "Rogue" in StayCount:  
                        #If Rogue Stays
                        call RogueOutfit("nude")
                        $ R_Water = 1
                        $ R_Spunk = []                    
                        $ R_RecentActions.append("showered")                      
                        $ R_DailyActions.append("showered")   
                else:   
                        #If Rogue leaves
                        call Remove_Girl("Rogue")  
            if K_Loc == bg_current:
                if "Kitty" in StayCount:  
                        #If Kitty Stays
                        call KittyOutfit("nude")
                        $ K_Water = 1
                        $ K_Spunk = []
                        $ K_RecentActions.append("showered")                      
                        $ K_DailyActions.append("showered")      
                else:     
                        #If Kitty leaves
                        call Remove_Girl("Kitty")
            if E_Loc == bg_current:
                if "Emma" in StayCount:  
                        #If Emma Stays
                        call EmmaOutfit("nude")
                        $ E_Water = 1
                        $ E_Spunk = []
                        $ E_RecentActions.append("showered")                      
                        $ E_DailyActions.append("showered")      
                else:     
                        #If Emma leaves
                        call Remove_Girl("Emma")
            if L_Loc == bg_current:
                if "Laura" in StayCount:  
                        #If Laura Stays
                        call LauraOutfit("nude")
                        $ L_Water = 1
                        $ L_Spunk = []
                        $ L_RecentActions.append("showered")                      
                        $ L_DailyActions.append("showered")      
                else:     
                        #If Laura leaves
                        call Remove_Girl("Laura")
                    
    call Seen_First_Peen(0,0,0,1) #You get naked
    
    if Nearby and len(StayCount) < 2:
            # This value carries over from the Entry scene if there are girls who show up late
            if len(StayCount) == 1 and len(Nearby) >= 2:
                #if there is at least one person sticking around and 2 on the waitlist. . .
                $ renpy.random.shuffle(Nearby)
                $ Nearby.remove(Nearby[0])
            
            if len(Nearby) >= 2:
                "As you finish getting undressed, [Nearby[0]] and [Nearby[1]] enter the room." 
            else:
                "As you finish getting undressed, [Nearby[0]] enters the room." 
            if "Rogue" in Nearby and "Rogue" not in StayCount:        
                    $ R_Loc = bg_current  
            if "Kitty" in Nearby and "Kitty" not in StayCount:
                    $ K_Loc = bg_current  
            if "Emma" in Nearby and "Emma" not in StayCount:
                    $ E_Loc = bg_current  
            if "Laura" in Nearby and "Laura" not in StayCount:
                    $ L_Loc = bg_current  
            call Present_Check
            call Set_The_Scene(Dress=0)
                
            call Seen_First_Peen(0,0,1,1) #You get naked, silent reactions
            
            if "Rogue" in Nearby:  
                    if R_SeenPeen == 1:
                        call AnyFace("Rogue","surprised",2,Eyes="down")    
                        ch_r "Oh!"
                        call AnyFace("Rogue","bemused",1,Eyes="side")  
                        ch_r "I am so sorry, I should {i}not{/i} have just barged in like that."
                    else:                    
                        call AnyFace("Rogue","bemused",1,Eyes="side")  
                        ch_r "I simply {i}must{/i} be more careful. . ."
            if "Kitty" in Nearby:  
                    call AnyFace("Kitty","bemused",2,Eyes="side")
                    if K_SeenPeen == 1:
                        ch_k "Sorry! Sorry! I need to stop just casually phasing into places!"
                    else:                    
                        ch_k "I have {i}got{/i} to knock more. . ."
            if "Emma" in Nearby:                      
                    if E_SeenPeen == 1:
                        call AnyFace("Emma","surprised")
                        ch_e "Oh! Dreadfully sorry." 
                        call AnyFace("Emma","sexy",Eyes="down")
                        ch_e "I hope we can meet again under. . . different circumstances."
                    else:              
                        call AnyFace("Emma","sexy",Eyes="down")      
                        ch_e "I really should pay closer attention. . ."
                    if "classcaught" not in E_History or (StayCount and "three" not in E_History):
                            #if Emma just showed up, but there are other girls around and she's not ok with that
                            "Emma decides to leave immediately."  
                            $ Nearby.remove("Emma")                 
                            call Remove_Girl("Emma")
                            call EmmaOutfit
            if "Laura" in Nearby:  
                    if L_SeenPeen == 1:
                        call AnyFace("Laura","surprised",Eyes="down")    
                        ch_l "Hey. That's interesting. . ."
                    else:         
                        call AnyFace("Laura","normal",Eyes="down")             
                        ch_l ". . ."
                        call AnyFace("Laura","normal")    
                        ch_l "I'm supposed to knock, aren't I."
            
            
            if "Emma" in StayCount and "three" not in E_History:
                    #if Emma was already here, but there are other girls around and she's not ok with that
                    if len(Nearby) >= 2:
                            "Seeing the other girls arrive, Emma quickly excuses herself."      
                    else:
                            "Seeing [Nearby[0]] arrive, Emma quickly excuses herself."              
                    $ StayCount.remove("Emma")  
                    call Remove_Girl("Emma")
                    call EmmaOutfit   
            
            if Nearby:
                #if there are still girls around to join in. . .
                if ApprovalCheck(Nearby[0], 1200):
                    $ StayCount.append(Nearby[0])                     
                if len(Nearby) >=2 and ApprovalCheck(Nearby[1], 1200) and len(StayCount) < 2:
                    $ StayCount.append(Nearby[1]) 
                    
                if len(Nearby) >=2:
                        if Nearby[0] not in StayCount and Nearby[1] not in StayCount:
                                "They both turn right back around."                                   
                                $ Nearby.remove(Nearby[1])                                   
                                $ Nearby.remove(Nearby[0])    
                        elif Nearby[0] not in StayCount:
                                "[Nearby[0]] turns right back around, but [Nearby[1]] stays."                                   
                                $ Nearby.remove(Nearby[0])  
                        elif Nearby[1] not in StayCount:
                                "[Nearby[1]] turns right back around, but [Nearby[0]] stays."                                   
                                $ Nearby.remove(Nearby[1])                      
                elif Nearby[0] not in StayCount:
                                "She turns right back around."                                    
                                $ Nearby.remove(Nearby[0])  
                                
                if "Rogue" in Nearby:  
                        #If Rogue Stays
                        call RogueOutfit("nude")
                        $ R_Water = 1
                        $ R_Spunk = []                    
                        $ Nearby.remove("Rogue")           
                        $ R_RecentActions.append("showered")                      
                        $ R_DailyActions.append("showered") 
                        ch_r "I wouldn't mind stickin around though." 
                else:   
                        #If Rogue leaves
                        call Remove_Girl("Rogue")  
                if "Kitty" in Nearby:  
                        #If Kitty Stays
                        call KittyOutfit("nude")
                        $ K_Water = 1
                        $ K_Spunk = []
                        $ Nearby.remove("Kitty")           
                        $ K_RecentActions.append("showered")                      
                        $ K_DailyActions.append("showered")   
                        ch_k "I {i}could{/i} get in on this."
                else:     
                        #If Kitty leaves
                        call Remove_Girl("Kitty")
                if "Emma" in Nearby:  
                        #If Emma Stays
                        call EmmaOutfit("nude")
                        $ E_Water = 1
                        $ E_Spunk = []
                        $ Nearby.remove("Emma")           
                        $ E_RecentActions.append("showered")                      
                        $ E_DailyActions.append("showered")    
                        ch_e "But, I could use some face time." 
                else:     
                        #If Emma leaves
                        call Remove_Girl("Emma")
                if "Laura" in Nearby:  
                        #If Laura Stays
                        call LauraOutfit("nude")
                        $ L_Water = 1
                        $ L_Spunk = []
                        $ Nearby.remove("Laura")           
                        $ L_RecentActions.append("showered")                      
                        $ L_DailyActions.append("showered")   
                        ch_l "Scoot over."
                else:     
                        #If Laura leaves
                        call Remove_Girl("Laura")
    #End "girl crashes in"
                                
    $ Round -= 30
    $ Trigger = 0
    
    if StayCount:
                #If at least one stays
                if len(StayCount) > 1:
                        #If both stay
                        call Shift_Focus(StayCount[0], StayCount[1]) 
                        "You take a quick shower with [StayCount[0]] and [StayCount[1]]."
                else:
                        call Shift_Focus(StayCount[0]) 
                        "You take a quick shower with [StayCount[0]]."
                        
                call Shower_Sex
                
                if StayCount[0] == "Rogue":                                
                    #Rogue agreed
                    ch_r "That was real nice, [R_Petname]."                                            
                elif StayCount[0] == "Kitty":                               
                    #Kitty agreed
                    ch_k "That was. . . nice."                                                       
                elif StayCount[0] == "Emma":                               
                    #Emma agreed
                    ch_e "That was. . . distracting."                                
                elif StayCount[0] == "Laura":                               
                    #Laura agreed
                    ch_l "Well that was fun."

                if len(StayCount) > 1:
                        #if there are multiple girls      
                        if StayCount[1] == "Rogue":                               
                            #Rogue too
                            ch_r "Yeah."                                      
                        elif StayCount[1] == "Kitty":                               
                            #Kitty too
                            ch_k "Yeah, I had fun."                            
                        elif StayCount[1] == "Emma":                               
                            #Emma too
                            ch_e "Indeed."
                        elif StayCount[1] == "Laura":                               
                            #Laura too
                            ch_l "Yup."   
                                                                                       
    else:        
                #solo shower
                $ Line = "You take a quick shower" + renpy.random.choice([". It was fairly uneventful.", 
                        ". A few people came and went as you did so.", 
                        ". That was refreshing."])  
                "[Line]"    
    #insert random events here
    $ P_RecentActions.append("showered")
    $ P_DailyActions.append("showered")
    if "scent" in P_DailyActions:
            $ P_DailyActions.remove("scent") 
                   
    call Get_Dressed
    if R_Loc == bg_current:  
            call RogueOutfit("towel")
    if K_Loc == bg_current:
            call KittyOutfit("towel")
    if E_Loc == bg_current:
            call EmmaOutfit("towel")
    if L_Loc == bg_current:
            call LauraOutfit("towel")
    $ Options = []
#    if Round < 5:
#        if Current_Time != "Night":
#                call Wait
#                call Girls_Location
#                call Set_The_Scene
#        else:
#                $ renpy.pop_call()
#                "After the shower, it's getting late, you head back to your room."
#                jump Player_Room
    return
# End Showering / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Shower Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Shower_Sex(Options=0,Line=0):
        #called from showering if sex is on the table. 
        if len(StayCount) > 1 and (ApprovalCheck(StayCount[1], 1800,Check=1) > ApprovalCheck(StayCount[0], 1800,Check=1)):
                $ renpy.random.shuffle(StayCount) #swaps girls if second girl likes you more
        call Shift_Focus(StayCount[0])
                
        $ D20 = renpy.random.randint(1,20)  
        $ D20 += 5 if ApprovalCheck(StayCount[0], 1800) else 0 #bonus if girl really likes you
        
        if "showered" in P_RecentActions:
                $ D20 = 0
                
        call AnyFace(StayCount[0],"sly")  
        #A set
        if len(StayCount) > 1 and D20 >= 10:
            "As you do so, both girls press their bodies body up against yours."
            $ Line = StayCount[0]
            call Close_Launch(StayCount[0],StayCount[1])
        elif D20 >= 5:
            "As you do so, [StayCount[0]] presses her body up against you."
            $ Line = "She"
            call Close_Launch(StayCount[0])
        else:
            $ Line = renpy.random.choice(["It was fairly uneventful.", 
                "A few people came and went as you did so.", 
                "That was refreshing."]) 
            "[Line]"
            if len(StayCount) > 1: 
                    call Statup(StayCount[0], "Lust", 50, 15)
                    call Statup(StayCount[1], "Lust", 50, 15)
                    call Statup(StayCount[0], "Lust", 90, 10)
                    call Statup(StayCount[1], "Lust", 90, 10)
                    "You got a good look at them washing off, and they didn't seem to mind the view either."
                    call GirlLikesGirl(StayCount[0],StayCount[1],600,4,1)
                    call GirlLikesGirl(StayCount[1],StayCount[0],600,4,1)
                    call GirlLikesGirl(StayCount[0],StayCount[1],800,2,1)
                    call GirlLikesGirl(StayCount[1],StayCount[0],800,2,1) 
            else: 
                    call Statup(StayCount[0], "Lust", 50, 15)
                    call Statup(StayCount[0], "Lust", 90, 10)
                    "You got a good look at her washing off, and she didn't seem to mind the view either."
            return
            
        if Line:
            if len(StayCount) > 1: 
                    call Statup(StayCount[0], "Lust", 50, 5)
                    call Statup(StayCount[0], "Lust", 70, 3)
                    call Statup(StayCount[1], "Lust", 50, 5)
                    call Statup(StayCount[1], "Lust", 70, 3)
            else:
                    call Statup(StayCount[0], "Lust", 50, 6)
                    call Statup(StayCount[0], "Lust", 70, 3)
            call Statup("Player", "Focus", 50, 5)
            call Statup("Player", "Focus", 80, 2)
            menu:
                extend ""
                "Continue?":
                    pass
                "Stop her." if len(StayCount) < 2: #if one
                    $Line = 0
                    call QuickReset(StayCount[0])  
                    "You take a step back, pulling away from her."
                    call Statup(StayCount[0], "Love", 80, -1)
                    call Statup(StayCount[0], "Obed", 80, 5)
                    call Statup(StayCount[0], "Inbt", 80, -1)
                    call AnyFace(StayCount[0],"sad")  
                    "She seems a bit disappointed."
                "Stop them." if len(StayCount) > 1: #if both
                    $Line = 0 
                    call QuickReset(StayCount[1])  
                    call QuickReset(StayCount[0])  
                    "You take a step back, pulling away from them."
                    call Statup(StayCount[0], "Love", 80, -1)
                    call Statup(StayCount[0], "Obed", 80, 5)
                    call Statup(StayCount[0], "Inbt", 80, -1)
                    call Statup(StayCount[1], "Obed", 80, 5)
                    call Statup(StayCount[1], "Inbt", 80, -1)
                    call AnyFace(StayCount[0],"sad")  
                    call AnyFace(StayCount[1],"sad") 
                    "They seem a bit disappointed."
        if Line:            
            #B set     
            $ Options = [1]
            
            if len(StayCount) > 1: 
                    if ApprovalCheck(StayCount[0], 1300) and GirlLikeCheck(StayCount[0],StayCount[1]) >= 800:
                        $ Options.append(2)     #"She reaches over to [StayCount[1]] and begins soaping up her pussy."
                    if ApprovalCheck(StayCount[0], 1200) and GirlLikeCheck(StayCount[0],StayCount[1]) >= 700:
                        $ Options.append(3)     #"She reaches over to [StayCount[1]] and begins soaping up her chest."
                
            if ApprovalCheck(StayCount[0], 1300): 
                $ Options.append(4)     #"She reaches down and takes your cock in her hand, soaping it up."
            if ApprovalCheck(StayCount[0], 1400): 
                $ Options.append(5)     #"She kneels down and wraps her breasts around your cock, soaping it up."
            
            if ApprovalCheck(StayCount[0], 1300): 
                $ Options.append(6)     #"She reaches down and begins fondling her own pussy, building a nice lather." 
            if ApprovalCheck(StayCount[0], 1200): 
                $ Options.append(7)     #"She begins rubbing her own breasts in circles, building a nice lather." 
                
            if not ApprovalCheck(StayCount[0], 1400):
                #only adds these if there's not much in there. 
                if ApprovalCheck(StayCount[0], 1000): 
                    $ Options.append(8)         #"She draws her breasts up and down your arm, the soap bubbles squirting out."
                if ApprovalCheck(StayCount[0], 1100): 
                    $ Options.append(9)         #"She kneels down and rubs her breasts against your leg, soaping it up."
                if ApprovalCheck(StayCount[0], 1000): 
                    $ Options.append(10)        #"She presses against your back, her soapy breasts rubbing back and forth against it."
                if ApprovalCheck(StayCount[0], 1100): 
                    $ Options.append(11)        #"She presses against your chest, her soapy breasts rubbing back and forth against it."
            
            $ renpy.random.shuffle(Options) 
            
            #"Line" will be either the first girl's name, or "She" 
            #lesbian
            if Options[0] == 2:
                    call Statup(StayCount[0], "Lust", 50, 5)
                    call Statup(StayCount[0], "Lust", 70, 2)
                    call Statup(StayCount[1], "Lust", 50, 7)
                    call Statup(StayCount[1], "Lust", 70, 3)
                    call Statup("Player", "Focus", 50, 8)
                    call Statup("Player", "Focus", 80, 4)
                    "[Line] reaches over to [StayCount[1]] and begins soaping up her chest."
            elif Options[0] == 3:
                    call Statup(StayCount[0], "Lust", 50, 7)
                    call Statup(StayCount[0], "Lust", 70, 3)
                    call Statup(StayCount[1], "Lust", 50, 8)
                    call Statup(StayCount[1], "Lust", 70, 4)
                    call Statup("Player", "Focus", 50, 8)
                    call Statup("Player", "Focus", 80, 5)
                    "[Line] reaches over to [StayCount[1]] and begins soaping up her pussy."
            
            #fondling you
            elif Options[0] == 4:
                    if len(StayCount) > 1: 
                            call Statup(StayCount[0], "Lust", 50, 10)
                            call Statup(StayCount[0], "Lust", 70, 7)
                    else:
                            call Statup(StayCount[0], "Lust", 50, 8)
                            call Statup(StayCount[0], "Lust", 70, 5)
                    call Statup("Player", "Focus", 50, 10)
                    call Statup("Player", "Focus", 80, 6)
                    "[Line] reaches down and takes your cock in her hand, soaping it up."
            elif Options[0] == 5:
                    if len(StayCount) > 1: 
                            call Statup(StayCount[0], "Lust", 50, 12)
                            call Statup(StayCount[0], "Lust", 70, 8)
                    else:
                            call Statup(StayCount[0], "Lust", 50, 9)
                            call Statup(StayCount[0], "Lust", 70, 6)
                    call Statup("Player", "Focus", 50, 10)
                    call Statup("Player", "Focus", 80, 4)
                    "[Line] kneels down and wraps her breasts around your cock, soaping it up."
                    
            #msturbation
            elif Options[0] == 6:
                    if len(StayCount) > 1: 
                            call Statup(StayCount[0], "Lust", 50, 11)
                            call Statup(StayCount[0], "Lust", 70, 6)
                    else:
                            call Statup(StayCount[0], "Lust", 50, 9)
                            call Statup(StayCount[0], "Lust", 70, 5)
                    call Statup("Player", "Focus", 50, 9)
                    call Statup("Player", "Focus", 80, 4)
                    "[Line] reaches down and begins fondling her own pussy, building a nice lather." 
            elif Options[0] == 7:
                    if len(StayCount) > 1: 
                            call Statup(StayCount[0], "Lust", 50, 10)
                            call Statup(StayCount[0], "Lust", 70, 5)
                    else:
                            call Statup(StayCount[0], "Lust", 50, 9)
                            call Statup(StayCount[0], "Lust", 70, 4)
                    call Statup("Player", "Focus", 50, 8)
                    call Statup("Player", "Focus", 80, 3)
                    "[Line] begins rubbing her own breasts in circles, building a nice lather." 
            
            #gentle tease
            elif Options[0] == 8:
                    call Statup(StayCount[0], "Lust", 50, 6)
                    call Statup(StayCount[0], "Lust", 70, 3)
                    call Statup("Player", "Focus", 50, 7)
                    call Statup("Player", "Focus", 80, 3)
                    "[Line] draws her breasts up and down your arm, the soap bubbles squirting out."
            elif Options[0] == 9:
                    call Statup(StayCount[0], "Lust", 50, 8)
                    call Statup(StayCount[0], "Lust", 70, 3)
                    call Statup("Player", "Focus", 50, 8)
                    call Statup("Player", "Focus", 80, 3)
                    "[Line] kneels down and rubs her breasts against your leg, soaping it up."
            elif Options[0] == 10:
                    call Statup(StayCount[0], "Lust", 50, 7)
                    call Statup(StayCount[0], "Lust", 70, 3)
                    call Statup("Player", "Focus", 50, 6)
                    call Statup("Player", "Focus", 80, 3)
                    "[Line] presses against your back, her soapy breasts rubbing back and forth against it."
            elif Options[0] == 11:
                    call Statup(StayCount[0], "Lust", 50, 7)
                    call Statup(StayCount[0], "Lust", 70, 3)
                    call Statup("Player", "Focus", 50, 8)
                    call Statup("Player", "Focus", 80, 4)
                    "[Line] presses against your chest, her soapy breasts rubbing back and forth against it."
            elif Options[0] == 1:
                    call Statup(StayCount[0], "Lust", 50, 5)
                    call Statup(StayCount[0], "Lust", 70, 2)
                    call Statup("Player", "Focus", 50, 6)
                    call Statup("Player", "Focus", 80, 3)
                    "[Line] stares silently at you as she moves her hands along her soapy body. . ."
                    $ Line = 0
             
        if Line and len(StayCount) > 1:
            #C Set, check what the other girl thinks. . .
            $ D20 += 5 if ApprovalCheck(StayCount[1], 1800) else 0
            if GirlLikeCheck(StayCount[1],StayCount[0]) <= 800 and 2 <= Options[0] <=3: 
                $ D20 -= 5
            if GirlLikeCheck(StayCount[1],StayCount[0]) <= 600: 
                $ D20 -= 5
                
            if 2 <= Options[0] <= 3:
                # if it's lesbian stuff. . .
                if ApprovalCheck(StayCount[1], 1300) and GirlLikeCheck(StayCount[1],StayCount[0]) >= 800:
                    call AnyFace(StayCount[1],"sexy",1)  
                    call Statup(StayCount[0], "Lust", 50, 5)
                    call Statup(StayCount[0], "Lust", 70, 5)
                    call Statup(StayCount[1], "Lust", 50, 12)
                    call Statup(StayCount[1], "Lust", 70, 12)
                    call Close_Launch(0,StayCount[1])
                    "[StayCount[1]] seems really into this, and returns the favor."  
                    call Statup("Player", "Focus", 50, 7)
                    call Statup("Player", "Focus", 80, 3) 
                    $ Line = 4
                elif ApprovalCheck(StayCount[1], 1200) and GirlLikeCheck(StayCount[1],StayCount[0]) >= 700: 
                    call AnyFace(StayCount[1],"sexy",2,Eyes="closed")  
                    call Statup(StayCount[1], "Lust", 50, 10)
                    call Statup(StayCount[1], "Lust", 70, 10)
                    call Statup("Player", "Focus", 50, 5)
                    call Statup("Player", "Focus", 80, 3)
                    call Close_Launch(0,StayCount[1])
                    "[StayCount[1]] seems really into this, and leans into it."
                else:                         
                    call Statup(StayCount[1], "Lust", 50, 10)
                    call AnyFace(StayCount[1],"sadside",Brows="confused")  
                    "[StayCount[1]] doesn't really seem to appreciate this."
                    "She pulls away."
                    $ Line = 3
            else:
                # if it's not lesbian stuff. . .
                if (ApprovalCheck(StayCount[1], 1300) and GirlLikeCheck(StayCount[1],StayCount[0]) >= 700) or ApprovalCheck(StayCount[1], 2000):
                    if Options[0] == 5: #titjob
                        call Statup(StayCount[1], "Lust", 50, 10)
                        call Statup(StayCount[1], "Lust", 70, 5)
                        call Statup("Player", "Focus", 50, 6)
                        call Statup("Player", "Focus", 80, 3)
                        call Close_Launch(0,StayCount[1])
                        "[StayCount[1]] seems really into this, slowly rubbing against you as she watches."  
                    else:
                        call Statup(StayCount[1], "Lust", 50, 10)
                        call Statup(StayCount[1], "Lust", 70, 5)
                        call Statup("Player", "Focus", 50, 5)
                        call Statup("Player", "Focus", 80, 3)
                        call Close_Launch(0,StayCount[1])
                        "[StayCount[1]] seems really into this, and joins her on the other side."  
                    $ Line = 4
                elif ((ApprovalCheck(StayCount[1], 1200) and GirlLikeCheck(StayCount[1],StayCount[0]) >= 600)) or ApprovalCheck(StayCount[1], 1600): 
                    call AnyFace(StayCount[1],"sexy",2,Eyes="down")  
                    call Statup(StayCount[1], "Lust", 50, 10)
                    call Statup(StayCount[1], "Lust", 70, 5)
                    "[StayCount[1]] seems really into this, and watches her do it."
                else:                       
                    call AnyFace(StayCount[1],"sadside",Brows="confused")  
                    call Statup(StayCount[1], "Lust", 50, 5)
                    "[StayCount[1]] doesn't really seem to appreciate this."
                    $ Line = 3
                    
        if Line:
            menu:
                extend ""
                "Continue?":
                    pass
                "Stop her." if len(StayCount) < 2: #if one
                    $Line = 0
                    call QuickReset(StayCount[0])     
                    "You take a step back, pulling away from her."
                    call Statup(StayCount[0], "Love", 80, -2)
                    call Statup(StayCount[0], "Obed", 80, 5)
                    call Statup(StayCount[0], "Inbt", 80, -2)
                    call AnyFace(StayCount[0],"sad")  
                    "She seems a bit disappointed."
                "Stop them." if len(StayCount) > 1: #if both
                    $Line = 0
                    call QuickReset(StayCount[1])  
                    call QuickReset(StayCount[0])  
                    "You take a step back, pulling away from them."
                    call AnyFace(StayCount[0],"sad")  
                    call Statup(StayCount[0], "Love", 80, -2)
                    call Statup(StayCount[0], "Obed", 80, 5)
                    call Statup(StayCount[0], "Inbt", 80, -2)
                    if Line == 3:
                        call Statup(StayCount[1], "Love", 80, 4)
                        call Statup(StayCount[1], "Obed", 80, 5)
                        call AnyFace(StayCount[1],"bemused")  
                        "[StayCount[0]] seems a bit disappointed, but [StayCount[1]] seems pleased."
                    else:
                        call Statup(StayCount[1], "Love", 80, -1)
                        call Statup(StayCount[1], "Obed", 80, 5)
                        call Statup(StayCount[1], "Inbt", 80, -1)
                        call AnyFace(StayCount[1],"sad")  
                        "They seem a bit disappointed."
                     
        if Line: 
            #D set, wrap-up  
            if len(StayCount) > 1 and Line != 3: #if second didn't disapprove
                    call GirlLikesGirl(StayCount[0],StayCount[1],600,4,1)
                    call GirlLikesGirl(StayCount[1],StayCount[0],600,4,1)
                    call GirlLikesGirl(StayCount[0],StayCount[1],800,3,1)
                    call GirlLikesGirl(StayCount[1],StayCount[0],800,3,1)
                    call GirlLikesGirl(StayCount[0],StayCount[1],900,1,1)
                    call GirlLikesGirl(StayCount[1],StayCount[0],900,1,1)                  
            if 2 <= Options[0] <= 3 and D20 >= 15:
                    #if it's lesbian. . .       
                    call GirlLikesGirl(StayCount[1],StayCount[0],900,4,1)    
                    call Statup("Player", "Focus", 50, 10)
                    call Statup("Player", "Focus", 80, 5)                 
                    "After a few minutes of this, it looks like [StayCount[1]] gets off."
                    call Quick_O(StayCount[0])
                    if Line == 4:                                
                        call GirlLikesGirl(StayCount[0],StayCount[1],900,3,1)
                        "It looks like [StayCount[0]] is reacting positively to it as well. . ."
                        call Quick_O(StayCount[1])
                    if len(StayCount) > 1:
                            "The girls take a step back."
                            call QuickReset(StayCount[1]) 
                    else:
                            "[StayCount[0]] takes a step back."
                    call QuickReset(StayCount[0])   
                                                        
            elif 4 <= Options[0] <= 5 and D20 >= 10:
                    #if it's her fondling you
                    $ P_Focus = 15
                    if Options[0] == 5: #if it was titjob
                            if StayCount[0] == "Rogue":
                                    $ R_Spunk.append("tits")
                            elif StayCount[0] == "Kitty":
                                    $ K_Spunk.append("tits")
                            elif StayCount[0] == "Emma":
                                    $ E_Spunk.append("tits")
                            elif StayCount[0] == "Laura":
                                    $ L_Spunk.append("tits")
                        
                    if Line == 4:
                        call Statup(StayCount[0], "Inbt", 90, 7) 
                        call Statup(StayCount[1], "Inbt", 90, 4) 
                        call GirlLikesGirl(StayCount[0],StayCount[1],900,3,1)
                        call GirlLikesGirl(StayCount[1],StayCount[0],900,3,1)                                
                        "After a few minutes of this, the two of them manage to get you off."                                 
                    else:
                        call Statup(StayCount[0], "Inbt", 90, 5) 
                        "After a few minutes of this, she manages to get you off." 
                    "A little more work is needed to clean up the mess." 
                    if Options[0] == 5: #if it was titjob
                            if StayCount[0] == "Rogue":
                                    $ R_Spunk = []
                            elif StayCount[0] == "Kitty":
                                    $ K_Spunk = []
                            elif StayCount[0] == "Emma":
                                    $ E_Spunk = []
                            elif StayCount[0] == "Laura":
                                    $ L_Spunk = []
                    if len(StayCount) > 1:
                            "The girls take a step back."
                            call QuickReset(StayCount[1]) 
                    else:
                            "[StayCount[0]] takes a step back."
                    call QuickReset(StayCount[0])   
                    
            elif 6 <= Options[0] <= 7 and D20 >= 15:
                    #if it's her masturbation. . .         
                    call Statup(StayCount[0], "Inbt", 90, 7)   
                    call Statup("Player", "Focus", 50, 15)
                    call Statup("Player", "Focus", 80, 5)             
                    "After a few minutes of this, it looks like [StayCount[0]] gets off."
                    call Quick_O(StayCount[0])
                    if Line == 4:
                        call Statup(StayCount[1], "Inbt", 90, 6) 
                        call GirlLikesGirl(StayCount[0],StayCount[1],900,3,1)
                        "It looks like [StayCount[1]] is enjoying herself as well. . ."
                        call Quick_O(StayCount[1])
                    if len(StayCount) > 1:
                            call GirlLikesGirl(StayCount[1],StayCount[0],900,3,1)
                            "The girls take a step back."
                            call QuickReset(StayCount[1]) 
                    else:
                            "[StayCount[0]] takes a step back."
                    call QuickReset(StayCount[0])   
            else:
                #nobody got off
                if len(StayCount) > 1:
                        call QuickReset(StayCount[1])    
                call QuickReset(StayCount[0])      
                call Statup("Player", "Focus", 50, 15)
                call Statup("Player", "Focus", 80, 5)
                if D20 >= 15:
                    "After a minute or two, it sounds like someone is coming, so you scramble apart."   
                    "Disappointing. . ."
                elif D20 >= 10:
                    "After a minute or two, she seems satisfied with her efforts, and pulls back."
                    if 4 <= Options[0] <= 5:
                            "You're left pretty hard."
                else:
                    "After a minute or so of this, she draws back and finshes washing herself off."
                    if 4 <= Options[0] <= 5:
                            "You're left pretty hard." 
        call Shift_Focus(StayCount[0])  
        return
# End Shower Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




label Rogue_Caught_Shower:  
    call Shift_Focus("Rogue")     
    $ R_RecentActions.append("showered")                      
    $ R_DailyActions.append("showered")     
    call Remove_Girl("All")
    $ R_Loc = "bg showerroom"
    call RogueOutfit("nude")
    $ R_Blush = 2
    $ R_Water = 1
    $ R_Spunk = []
    menu:
            "What do you do?"
            "Enter":     
                $ Line = "enter"                
            "Knock":
                $ Line = "knock"
            "Come back later":
                $ R_Loc = "bg rogue"
                call RogueOutfit
                $ R_Water = 0
                jump Campus_Map
            
    if Line == "knock":                                                                                         
            #You knock
            $ Line = 0
            "You knock on the door. You hear some shuffling inside"        
            $ R_Over = "towel"       
            if (D20 >=18 and R_Lust >= 70) or (D20 >=15 and R_Lust >= 80):                                          
                    #Rogue caught fapping
                    "You hear a startled gasp, followed by some shuffling around as a brush hits the floor."
                    "After several seconds and some more shuffling, Rogue comes to the door."
                    $ R_Brows = "confused"
                    $ R_Eyes = "surprised"
                    $ R_Mouth = "smile"
                    call Set_The_Scene(Dress=0)
                    ch_r "Sorry about that [R_Petname], I was. . . just wrapping up my shower."
                    call Statup("Rogue", "Lust", 90, 5)
                    $ Tempmod += 10
            else:                                                                                                   
                    #Rogue caught showering
                    "You hear the rustling of a towel and some knocking around, but after a few seconds Rogue comes to the door."
                    call Set_The_Scene(Dress=0)
                    ch_r "Sorry about that [R_Petname], I was just wrapping up my shower."
            #end "knocked"
    else:                                                                                                       
        #You don't knock    
        $ Line = 0    
        if (D20 >=18 and R_Lust >= 70) or (D20 >=15 and R_Lust >= 80):                                         
                #Caught masturbating in the shower. 
                call RogueFace("sexy")
                $ R_Eyes = "closed"
                $ Rogue_Arms = 2
                call Set_The_Scene(Dress=0)
                $ Count = 0        
                "You see Rogue under the shower, feeling herself up."
                $ Trigger = "masturbation"
                $ R_DailyActions.append("unseen") if "unseen" not in R_DailyActions else R_DailyActions   
                $ R_RecentActions.append("unseen") if "unseen" not in R_RecentActions else R_RecentActions 
                call Rogue_SexAct("masturbate")   
                jump Shower_Room
            
        elif D20 >= 15:                                                                                         
                #She's just showering and naked
                call Set_The_Scene(Dress=0)                
                call RogueFace("surprised", 1)
                "As you enter the showers, you see Rogue washing up."        
                if not ApprovalCheck("Rogue", 1200) or not R_SeenPussy or not R_SeenChest:
                        $ R_Brows = "angry"     
                        $ R_Over = "towel"
                        "She grabs a towel and covers up."             
                        call RogueFace("angry", 1)
                        call Statup("Rogue", "Love", 80, -5) 
                else:
                        if "exhibitionist" in R_Traits:
                            call Statup("Rogue", "Lust", 90, (2*D20)) 
                        else:
                            call Statup("Rogue", "Lust", 80, D20)
                        $ R_Brows = "confused"        
                
                call Rogue_First_Topless(1)
                call Rogue_First_Bottomless(1) 
                call Statup("Rogue", "Inbt", 70, 3)
                menu:
                        ch_r "Hey! Learn to knock maybe?!"
                        "Sorry, I should have knocked.":  
                            call Statup("Rogue", "Love", 50, 2)
                            call Statup("Rogue", "Love", 80, 4)
                        "And miss the view?":
                            call Statup("Rogue", "Obed", 50, 2)
                            call Statup("Rogue", "Obed", 80, 2)
                            call Statup("Rogue", "Inbt", 60, 1)
                #end caught showering naked
            
        else:                                                                                   
                #She's done showering and in a towel
                $ R_Over = "towel"
                call Set_The_Scene(Dress=0)
                "As you enter the showers, you see Rogue putting on a towel."        
                if not ApprovalCheck("Rogue", 1100) and (not R_SeenPussy or not R_SeenChest):          
                        call RogueFace("angry")
                        $R_Brows = "confused"
                        call Statup("Rogue", "Love", 80, -5)
                else:
                        call RogueFace("sexy")
                        $R_Brows = "confused"        
                call Statup("Rogue", "Inbt", 50, 3)
                menu:
                        ch_r "Well hello there, [R_Petname]. Hoping to see something more?"
                        "Sorry, I should have knocked.":   
                            call Statup("Rogue", "Love", 50, 2)
                            call Statup("Rogue", "Love", 80, 2)
                        "Well, to be honest. . .":                
                            call Statup("Rogue", "Love", 50, 2)
                            call Statup("Rogue", "Obed", 50, 2)
                            call Statup("Rogue", "Obed", 80, 2)
                            call Statup("Rogue", "Inbt", 60, 1)
                #end caught in towel
                    
        call RogueFace("sexy")          
        if not ApprovalCheck("Rogue", 750) and (R_SeenPussy < 3 or R_SeenChest < 3): 
                ch_r "Well, it happens, just be careful next time."
        elif not ApprovalCheck("Rogue", 1300): 
                ch_r "Well, it happens, just be careful next time."
        else:                
                ch_r "You could have just asked, [R_Petname]."      
                if R_Over == "towel": 
                    $ R_Over = 0
                    pause 0.5                      
                    $ R_Over = "towel"  
                    "She flashes you real quick."                        
                    $ R_Over = "towel" 
                call Rogue_First_Topless(1)
                call Rogue_First_Bottomless(1) 
        #end didn't knock
    
    menu:
        ch_r "Well, I should probably get going. . ." 
        "Sure, see you later then.":
                call Remove_Girl("Rogue")
                $ R_Water = 0
                call RogueOutfit
        "Actually, could you stick around a minute?":
            if ApprovalCheck("Rogue", 900):
                $ R_Loc = "bg showerroom"            
                ch_r "Sure, what's up?"
            else:
                ch_r "Um, actually, I'm not really comfortable being so. . . exposed?"
                ch_r "I'll just see you around later."
                call RogueOutfit    
                call Remove_Girl("Rogue")
                $ R_Water = 0           
            
    jump Shower_Room
# End Rogue Caught Shower / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Kitty_Caught_Shower:  
    call Shift_Focus("Kitty")     
    $ K_RecentActions.append("showered")                      
    $ K_DailyActions.append("showered")     
    call Remove_Girl("All")
    $ K_Loc = "bg showerroom"
    call KittyOutfit("nude")
    $ K_Blush = 2
    $ K_Water = 1
    $ K_Spunk = []
    menu:
            "What do you do?"
            "Enter":     
                $ Line = "enter"                
            "Knock":
                $ Line = "knock"
            "Come back later":
                $ K_Loc = "bg kitty"
                call KittyOutfit
                $ K_Water = 0
                jump Campus_Map
            
    if Line == "knock":                                                                                         
            #You knock
            $ Line = 0
            "You knock on the door. You hear some shuffling inside"        
            $ K_Over = "towel"       
            if (D20 >=18 and K_Lust >= 70) or (D20 >=15 and K_Lust >= 80):                                          
                    #Kitty caught fapping
                    "You hear a startled gasp, followed by some shuffling around as a shampoo bottle hits the floor."
                    "After several seconds and some more shuffling, Kitty comes to the door."
                    $ K_Brows = "confused"
                    $ K_Eyes = "surprised"
                    $ K_Mouth = "smile"
                    call Set_The_Scene(Dress=0)
                    ch_k "Oh, hey, [K_Petname]. I was just[K_like]showering."
                    call Statup("Kitty", "Lust", 90, 5)
                    $ Tempmod += 10
            else:                                                                                                   
                    #Kitty caught showering
                    "You hear the rustling of a towel and some knocking around, but after a few seconds Kitty comes to the door."
                    call Set_The_Scene(Dress=0)
                    ch_k "Oh, hey, [K_Petname]. I was just[K_like]showering."
            #end knocked
            
    else:                                                                                                       
        #You don't knock   
        if not K_SeenPussy or not K_SeenChest:
            $ D20 -=5 if D20 > 5 else D20
        $ Line = 0    
        if (D20 >=18 and K_Lust >= 70) or (D20 >=15 and K_Lust >= 80):                                          
                #Caught masturbating in the shower. 
                call KittyFace("sexy")
                $ K_Eyes = "closed"
                $ Kitty_Arms = 2
                call Set_The_Scene(Dress=0)
                $ Count = 0        
                "You see Kitty under the shower, feeling herself up."
                $ Trigger = "masturbation"
                $ K_DailyActions.append("unseen") if "unseen" not in K_DailyActions else K_DailyActions   
                $ K_RecentActions.append("unseen") if "unseen" not in K_RecentActions else K_RecentActions 
                call Kitty_SexAct("masturbate")   
                jump Shower_Room
        
        #change to elif when I fix the above option
        if D20 >= 15:                                                                                         
                #She's just showering and naked
                call Set_The_Scene(Dress=0)                
                call KittyFace("surprised", 1)
                "As you enter the showers, you see Kitty washing up."        
                if not ApprovalCheck("Kitty", 1200) or not K_SeenPussy or not K_SeenChest:
                        $ K_Brows = "angry"     
                        $ K_Over = "towel"
                        "She grabs a towel and covers up."             
                        call KittyFace("angry", 1)
                        call Statup("Kitty", "Love", 80, -5) 
                else:
                        if "exhibitionist" in K_Traits:
                            call Statup("Kitty", "Lust", 90, (2*D20)) 
                        else:
                            call Statup("Kitty", "Lust", 80, D20)
                        $ K_Brows = "confused"        
                
                call Kitty_First_Topless(1)
                call Kitty_First_Bottomless(1) 
                call Statup("Kitty", "Inbt", 70, 3)
                menu:
                    ch_k "Did you[K_like]get a good look?"
                    "Sorry, I should have knocked.":  
                        call Statup("Kitty", "Love", 50, 2)
                        call Statup("Kitty", "Love", 80, 4)
                    "Definitely.":
                        call Statup("Kitty", "Obed", 50, 2)
                        call Statup("Kitty", "Obed", 80, 2)
                        call Statup("Kitty", "Inbt", 60, 1)
                #end caught showering naked
            
        else:                                                                                   
                #She's done showering and in a towel
                $ K_Over = "towel"
                call Set_The_Scene(Dress=0)
                "As you enter the showers, you see Kitty putting on a towel."        
                if not ApprovalCheck("Kitty", 1100) and (not K_SeenPussy or not K_SeenChest):          
                        call KittyFace("angry")
                        $K_Brows = "confused"
                        call Statup("Kitty", "Love", 80, -5)
                else:
                        call KittyFace("sexy")
                        $K_Brows = "confused"        
                call Statup("Kitty", "Inbt", 50, 3)
                menu:
                    ch_k "Oh, hey. Were you hoping I'd be naaaaaked?"
                    "Sorry, I should have knocked.":   
                            call KittyFace("smile",1)
                            call Statup("Kitty", "Love", 50, 2)
                            call Statup("Kitty", "Love", 80, 2)
                            if ApprovalCheck("Kitty", 850) and K_SeenPussy and K_SeenChest: 
                                ch_k "Well, it's not like I totally mind. . ."  
                            else:
                                ch_k "Yeah, appreciated."
                    "Now that you mention it. . .":                
                            call Statup("Kitty", "Love", 50, 2)
                            call Statup("Kitty", "Obed", 50, 2)
                            call Statup("Kitty", "Obed", 80, 2)
                            call Statup("Kitty", "Inbt", 60, 1)
                            
                            call KittyFace("sexy")       
                            if not ApprovalCheck("Kitty", 850) and (K_SeenPussy < 3 or K_SeenChest < 3): 
                                    ch_k "Well too bad." 
                            elif not ApprovalCheck("Kitty", 1400): 
                                    ch_k "Well too bad." 
                            else:
                                ch_k "Well, it's not like it's totally off the table. . ."      
                                if K_Over == "towel": 
                                    $ K_Over = 0
                                    pause 0.5                      
                                    $ K_Over = "towel"  
                                    "She flashes you real quick."                        
                                    $ K_Over = "towel"   
                                call Kitty_First_Topless(1)
                                call Kitty_First_Bottomless(1) 
                #end done showering naked
    
    menu:
        ch_k "I'm done here, see you later?" 
        "Sure, see you later then.":
                hide Kitty_Sprite with easeoutright
                call Remove_Girl("Kitty")
                $ K_Water = 0
                call KittyOutfit
                "Kitty heads out."
        "Actually, could you stick around a minute?":
            if ApprovalCheck("Kitty", 900):
                call KittyFace("sexy",1)
                $ K_Loc = "bg showerroom"            
                ch_k "Yeah?"
            else: 
                call KittyFace("perplexed",1)
                ch_k "I'm[K_like]totally exposed here?"
                ch_k "I'm just going to head out."
                hide Kitty_Sprite with easeoutright
                call Remove_Girl("Kitty")
                $ K_Water = 0
                call KittyOutfit               
            
    jump Shower_Room
# End Kitty Caught Shower / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    

label Emma_Caught_Shower:  
    call Shift_Focus("Emma")     
    $ E_RecentActions.append("showered")                      
    $ E_DailyActions.append("showered")     
    call Remove_Girl("All")
    $ E_Loc = "bg showerroom"
    call EmmaOutfit("nude")
    $ E_Blush = 2
    $ E_Water = 1
    $ E_Spunk = []
    menu:
            "What do you do?"
            "Enter":     
                $ Line = "enter"                
            "Knock":
                $ Line = "knock"
            "Come back later":
                $ E_Loc = "bg emma"
                call EmmaOutfit
                $ E_Water = 0
                jump Campus_Map
            
    if Line == "knock":                                                                                         
            #You knock
            $ Line = 0
            "You knock on the door. You hear some shuffling inside"        
            $ E_Over = "towel"       
            if (D20 >=18 and E_Lust >= 70) or (D20 >=15 and E_Lust >= 80):                                          
                    #Emma caught fapping
                    "You hear a sharp shuffling sound and the water gets cut off."
                    "After several seconds and some more shuffling, Emma comes to the door."
                    $ E_Brows = "confused"
                    $ E_Eyes = "surprised"
                    $ E_Mouth = "smile"
                    call Set_The_Scene(Dress=0)
                    ch_e "Oh, hello [E_Petname]. I was. . . taking care of some personal business."
                    call Statup("Emma", "Lust", 90, 5)
                    $ Tempmod += 10
            else:                                                                                                   
                    #Emma caught showering
                    "You hear the rustling of a towel and some knocking around, but after a few seconds Emma comes to the door."
                    call Set_The_Scene(Dress=0)
                    ch_e "Oh, hello [E_Petname]. I was just finishing my shower."
            #end "knocked"
    else:                                                                                                       
        #You don't knock    
        $ Line = 0    
        if "classcaught" in E_History and ((D20 >=18 and E_Lust >= 70) or (D20 >=15 and E_Lust >= 80)):
                #Caught masturbating in the shower. 
                call EmmaFace("sexy")
                $ E_Eyes = "closed"
                $ Emma_Arms = 2
                call Set_The_Scene(Dress=0)
                $ Count = 0        
                "You see Emma under the shower, feeling herself up."
                $ Trigger = "masturbation"
                $ E_DailyActions.append("unseen") if "unseen" not in E_DailyActions else E_DailyActions   
                $ E_RecentActions.append("unseen") if "unseen" not in E_RecentActions else E_RecentActions 
                call Emma_SexAct("masturbate")   
                jump Shower_Room
            
        elif D20 >= 15:                                                                                         
                #She's just showering and naked
                call Set_The_Scene(Dress=0)                
                call EmmaFace("surprised", 1)
                "As you enter the showers, you see Emma washing up."        
                if not ApprovalCheck("Emma", 1200) or not E_SeenPussy or not E_SeenChest:
                        $ E_Brows = "angry"     
                        $ E_Over = "towel"
                        "She grabs a towel and covers up."             
                        call EmmaFace("angry", 1)
                        call Statup("Emma", "Love", 80, -5) 
                else:
                        if "exhibitionist" in E_Traits:
                            call Statup("Emma", "Lust", 90, (2*D20)) 
                        else:
                            call Statup("Emma", "Lust", 80, D20)
                        $ E_Brows = "confused"        
                
                call Emma_First_Topless(1)
                call Emma_First_Bottomless(1) 
                call Statup("Emma", "Inbt", 70, 3)
                menu:
                        ch_e "Hello. Haven't you learned to knock before entering?"
                        "Sorry, I should have.":  
                            call Statup("Emma", "Love", 50, 2)
                            call Statup("Emma", "Love", 80, 2)
                            call Statup("Emma", "Inbt", 60, 2)
                        "And miss the view?":
                            call Statup("Emma", "Obed", 50, 2)
                            call Statup("Emma", "Obed", 80, 2)
                            call Statup("Emma", "Inbt", 60, 2)
                        "It's not as if you're leaving that much to the imagination. . .": 
                            call Statup("Emma", "Obed", 50, 2)
                            call Statup("Emma", "Obed", 80, 2)
                            call Statup("Emma", "Inbt", 60, 2)
                #end caught showering naked
            
        else:                                                                                   
                #She's done showering and in a towel
                $ E_Over = "towel"
                call Set_The_Scene(Dress=0)
                "As you enter the showers, you see Emma putting on a towel."        
                if not ApprovalCheck("Emma", 1100) and (not E_SeenPussy or not E_SeenChest):          
                        call EmmaFace("angry")
                        $E_Brows = "confused"
                        call Statup("Emma", "Love", 80, -5)
                else:
                        call EmmaFace("sexy")
                        $E_Brows = "confused"        
                call Statup("Emma", "Inbt", 50, 3)
                menu:
                        ch_e "Oh, hello, [E_Petname]. Sorry you didn't get here sooner?"
                        "Oh, I should have knocked.":   
                            call Statup("Emma", "Love", 50, 2)
                            call Statup("Emma", "Love", 80, 1)
                            call Statup("Emma", "Inbt", 60, 1)
                        "Well, to be honest. . .":                
                            call Statup("Emma", "Love", 50, 2)
                            call Statup("Emma", "Obed", 50, 2)
                            call Statup("Emma", "Obed", 80, 1)
                            call Statup("Emma", "Inbt", 60, 2)
                        "It's not as if you're leaving that much to the imagination. . .": 
                            call Statup("Emma", "Obed", 50, 2)
                            call Statup("Emma", "Obed", 80, 2)
                            call Statup("Emma", "Inbt", 60, 2)
                #end caught in towel
                    
        call EmmaFace("sexy")          
        if not ApprovalCheck("Emma", 750) and (E_SeenPussy < 3 or E_SeenChest < 3): 
                ch_e "Hmm. Yes, a likely excuse."
        elif not ApprovalCheck("Emma", 1300): 
                ch_e "Hmm. Yes, a likely excuse."
        else:                
                ch_e "Well, it's not that I mind. . ."
                if E_Over == "towel": 
                    $ E_Over = 0
                    pause 0.5                      
                    $ E_Over = "towel"  
                    "She flashes you real quick."                        
                    $ E_Over = "towel" 
                call Emma_First_Topless(1)
                call Emma_First_Bottomless(1) 
        #end didn't knock
    
    menu:
        ch_e "I should probably be leaving. . ." 
        "Sure, see you later then.":
                call Remove_Girl("Emma")
                $ E_Water = 0
                call EmmaOutfit
        "Actually, could you stick around a minute?":
            if ApprovalCheck("Emma", 900):
                $ E_Loc = "bg showerroom"            
                ch_e "Very well, what did you need?"
            else:
                ch_e "I really shouldn't be \"hanging out\" in such a state."
                ch_e "We can talk later."
                call Remove_Girl("Emma")
                $ E_Water = 0
                call EmmaOutfit               
            
    jump Shower_Room
# End Emma Caught Shower / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



label Laura_Caught_Shower:  
    call Shift_Focus("Laura")     
    $ L_RecentActions.append("showered")                      
    $ L_DailyActions.append("showered")     
    call Remove_Girl("All")
    $ L_Loc = "bg showerroom"
    call LauraOutfit("nude")
    $ L_Blush = 2
    $ L_Water = 1
    $ L_Spunk = []
    menu:
            "What do you do?"
            "Enter":     
                $ Line = "enter"                
            "Knock":
                $ Line = "knock"
            "Come back later":
                $ L_Loc = "bg laura"
                call LauraOutfit
                $ L_Water = 0
                jump Campus_Map
            
    if Line == "knock":                                                                                         
            #You knock
            $ Line = 0
            "You knock on the door. You hear some shuffling inside"        
            $ L_Over = "towel"       
            if (D20 >=18 and L_Lust >= 70) or (D20 >=15 and L_Lust >= 80):                                          
                    #Laura caught fapping
                    "You hear a sharp shuffling sound and the water gets cut off."
                    "After several seconds and some more shuffling, Laura comes to the door."
                    $ L_Brows = "confused"
                    $ L_Eyes = "surprised"
                    $ L_Mouth = "normal"
                    call Set_The_Scene(Dress=0)
                    ch_l "Oh, hey [L_Petname]. I was just. . . working off some stress."
                    call Statup("Laura", "Lust", 90, 5)
                    $ Tempmod += 10
            else:                                                                                                   
                    #Laura caught showering
                    "You hear the rustling of a towel and some knocking around, but after a few seconds Laura comes to the door."
                    call Set_The_Scene(Dress=0)
                    ch_l "Oh, hey [L_Petname]. I was just finishing up."
            #end "knocked"
    else:                                                                                                       
        #You don't knock    
        $ Line = 0    
        if (D20 >=18 and L_Lust >= 70) or (D20 >=15 and L_Lust >= 80):
                #Caught masturbating in the shower. 
                call LauraFace("sexy",Eyes="closed")
                $ Laura_Arms = 2
                call Set_The_Scene(Dress=0)
                $ Count = 0        
                "You see Laura under the shower, feeling herself up."
                $ Trigger = "masturbation"
                $ L_DailyActions.append("unseen") if "unseen" not in L_DailyActions else L_DailyActions   
                $ L_RecentActions.append("unseen") if "unseen" not in L_RecentActions else L_RecentActions 
                call Laura_SexAct("masturbate")   
                jump Shower_Room
            
        elif D20 >= 15:                                                                                         
                #She's just showering and naked
                call Set_The_Scene(Dress=0)                
                call LauraFace("surprised", 1)
                "As you enter the showers, you see Laura washing up."        
                if not ApprovalCheck("Laura", 1200) or not L_SeenPussy or not L_SeenChest:
                        $ L_Brows = "angry"     
                        $ L_Over = "towel"
                        "She grabs a towel and covers up."             
                        call LauraFace("angry", 1)
                        call Statup("Laura", "Love", 80, -5) 
                else:
                        if "exhibitionist" in L_Traits:
                            call Statup("Laura", "Lust", 90, (2*D20)) 
                        else:
                            call Statup("Laura", "Lust", 80, D20)
                        $ L_Brows = "confused"        
                
                call Laura_First_Topless(1)
                call Laura_First_Bottomless(1) 
                call Statup("Laura", "Inbt", 70, 3)
                menu:
                        ch_l "Um, hey? Don't knock much?"
                        "Sorry, I should have.":  
                            call Statup("Laura", "Love", 50, 1)
                            call Statup("Laura", "Love", 80, 1)
                            call Statup("Laura", "Inbt", 60, 2)
                        "And miss the view?":
                            call Statup("Laura", "Obed", 50, 3)
                            call Statup("Laura", "Obed", 80, 2)
                            call Statup("Laura", "Inbt", 60, 3)
                        "Why, would it have made a difference?": 
                            if L_Inbt <= 50:
                                call Statup("Laura", "Love", 50, -3)
                                call Statup("Laura", "Obed", 50, 2)
                            call Statup("Laura", "Obed", 80, 2)
                            call Statup("Laura", "Inbt", 60, 2)
                #end caught showering naked
            
        else:                                                                                   
                #She's done showering and in a towel
                $ L_Over = "towel"
                call Set_The_Scene(Dress=0)
                "As you enter the showers, you see Laura putting on a towel."        
                if not ApprovalCheck("Laura", 1100) and (not L_SeenPussy or not L_SeenChest):          
                        call LauraFace("angry",Brows="confused")
                        call Statup("Laura", "Love", 80, -5)
                else:
                        call LauraFace("sexy",Brows="confused")
                call Statup("Laura", "Inbt", 50, 3)
                menu:
                        ch_l "Oh, hey [L_Petname]. Trying to slip in unnoticed?"
                        "Oh, I should have knocked.":   
                            call Statup("Laura", "Love", 80, 1)
                            call Statup("Laura", "Obed", 80, -1)
                            call Statup("Laura", "Inbt", 60, 1)
                        "Well, to be honest. . .":                
                            call Statup("Laura", "Love", 80, 1)
                            call Statup("Laura", "Obed", 50, 2)
                            call Statup("Laura", "Obed", 80, 1)
                            call Statup("Laura", "Inbt", 60, 2)
                        "I still like the view. . .": 
                            if L_Inbt <= 50:
                                call Statup("Laura", "Love", 50, -1)
                                call Statup("Laura", "Obed", 50, 2)
                            else:
                                call Statup("Laura", "Love", 80, 1)
                            call Statup("Laura", "Obed", 80, 2)
                            call Statup("Laura", "Inbt", 60, 3)
                #end caught in towel
                    
        call LauraFace("sexy")          
        if not ApprovalCheck("Laura", 750) and (L_SeenPussy < 3 or L_SeenChest < 3): 
                ch_l "Well, just keep an eye on your own bits."
                ch_l "Wouldn't want them going missing."
        elif not ApprovalCheck("Laura", 1300): 
                ch_l "Uh-huh."
        else:                
                ch_l "Nah, I don't mind much. . ."
                if L_Over == "towel": 
                    $ L_Over = 0
                    pause 0.5                      
                    $ L_Over = "towel"  
                    "She flashes you real quick."                        
                    $ L_Over = "towel" 
                    ch_l "Heh!"
                call Laura_First_Topless(1)
                call Laura_First_Bottomless(1) 
        #end didn't knock
    
    menu:
        ch_l "I should get going. . ." 
        "Sure, see you later then.":
                call Remove_Girl("Laura")
                $ L_Water = 0
                call LauraOutfit
        "Actually, could you stick around a minute?":
            if ApprovalCheck("Laura", 900):
                $ L_Loc = "bg showerroom"            
                ch_l "Huh? Ok, what's up?"
            else:
                ch_l "I probably shouldn't hang out like this."
                ch_l "We'll talk later."
                call Remove_Girl("Laura")
                $ L_Water = 0
                call LauraOutfit     
    jump Shower_Room
# End Laura Caught Shower / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# end Shower Interface //////////////////////////////////////////////////////////////////////


# Kitty's Room Interface //////////////////////////////////////////////////////////////////////
label Kitty_Room_Entry:   
    if "locked" in P_Traits:
            $ P_Traits.remove("locked")
    $ Nearby = []     
    call Shift_Focus("Kitty")
    $ bg_current = "bg kitty"           
    call Gym_Clothes
    call Taboo_Level
    call Set_The_Scene(Entry = 1)  
    $ P_RecentActions.append("traveling")
    $ D20 = renpy.random.randint(1, 20)
    
    if "Kitty" in Party:
                    if Current_Time == "Night" or (Current_Time == "Evening" and Round <= 10):                         
                        if ApprovalCheck("Kitty", 1000, "LI") or ApprovalCheck("Kitty", 600, "OI"):     #It's late but she really likes you
                                ch_k "It's kinda late, [K_Petname], but you can have a minute."    
                        elif K_Addict >= 50:
                                ch_k "I'd really like to see you. . ."            
                        elif ApprovalCheck("Kitty", 500, "LI") or ApprovalCheck("Kitty", 300, "OI"):      #she likes you well enough but it's late
                                ch_k "It's a little late [K_Petname]. Tomorrow?"
                                $ K_RecentActions.append("noentry")                      
                                $ K_DailyActions.append("noentry")  
                                if "Kitty" in Party:
                                        $ Party.remove("Kitty")   
                                "She heads inside and closes the door behind her."
                                jump Campus_Map         
                    else: #If Kitty is in the party and it's not late in the day        
                                ch_k "Come on in!"
                    call EventCalls
                    jump Kitty_Room   
    #End if Kitty in Party
    
    if Round >= 10 and K_Loc == bg_current and "les" in K_RecentActions:
            call Girls_Caught_Lesing("Kitty")
            if not _return:
                jump Kitty_Room
                
    if "dress2" in L_History and not Party:
            #if you helped buy clothes for Laura earlier. . .
            call Laura_Dressup3
            jump Campus
                    
    if Round >= 10 and K_Loc == bg_current and "gonnafap" in K_DailyActions and D20 >= 10: 
                    #Kitty caught fapping ( 
                    call Girl_Caught_Mastubating("Kitty")
    
    else: #not auto-caught fapping
            if "Kitty" in Keys:
                menu:
                    "You have a key, what do you do?"
                    "Knock politely":
                            $ Line = "knock"
                            
                    "Use the key to enter.":
                            $ bg_current = "bg kitty"
                            call Set_The_Scene
                        
            if Line != "knock" and "Kitty" in Keys: 
                if K_Loc == "bg kitty":
                        if Round <= 10:        
                                if  "noentry" in K_RecentActions or "angry" in K_RecentActions:
                                        call KittyFace("angry")
                                        ch_k "GTFO."    
                                        "Kitty shoves you back into the hall."
                                        jump Campus_Map   
                                if Current_Time == "Night" :    
                                        "She's asleep in bed. You slip out quietly." #fix add options here.                            
                                        jump Campus_Map   
                        elif "gonnafap" in K_DailyActions and D20 >= 10: 
                                #Kitty caught fapping  
                                call Girl_Caught_Mastubating("Kitty")
                        elif D20 >=15 and (Current_Time == "Night" or Current_Time == "Morning"):                           
                                #Kitty caught changing
                                call Kitty_Caught_Changing
            #End "if you enter without knocking"
                
            else:#You knocked
                        $ Round -= 10 
                        "You knock on Kitty's door."        
                        if K_Loc != "bg kitty":
                                "Looks like she's not home right now."
                                jump Campus_Map
                            
                        if Round <= 10:
                                if Current_Time == "Night" :
                                    "There's no answer, she's probably asleep."  
                                    jump Campus_Map    
                    
                        if (D20 >=19 and K_Lust >= 50) or (D20 >=15 and K_Lust >= 70) or (D20 >=10 and K_Lust >= 80):    
                                #Kitty caught fapping
                                "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
                                "After several seconds and some more shuffling of clothing, Kitty comes to the door."
                                $ K_Brows = "confused"
                                $ K_Eyes = "surprised"
                                $ K_Mouth = "smile"
                                $ K_Blush = 1
                                call Set_The_Scene
                                ch_k "Oh, hey, [K_Petname], I was. . . never mind."
                                $ Tempmod += 10
                        elif D20 >=15 and (Current_Time == "Night" or Current_Time == "Morning"):                          
                                #Kitty caught changing
                                "You hear the rustling of fabric and some knocking around, but after a few seconds Kitty comes to the door."
                                call Set_The_Scene
                                ch_k "Oh, hi [K_Petname], I was[K_like]just getting changed."   
                        elif "angry" in K_RecentActions:
                                ch_k "Nooope."
                                "Kitty pushes you back into the hall and slams the door."
                                $ Trigger = 0
                                jump Campus_Map    
                        else:
                                call Set_The_Scene
                                "Kitty opens the door and leans out."
                                "You ask if you can come inside."
            #End "if you knocked"
                    
            #if you reach this point then you've asked to enter.               
            if K_Loc != "bg kitty":
                    "Looks like she's not home right now."                
                    if "Kitty" in Keys:
                            menu:
                                "Go in and wait for her?"
                                "Yes":
                                        $ Line = 0
                                        jump Kitty_Room
                                "No":
                                        pass
                    "You head back."
                    jump Campus_Map 
                    
            elif  "noentry" in K_RecentActions or "angry" in K_RecentActions:
                    call KittyFace("angry")
                    ch_k "What part of \"GTFO\" was unclear?"  
                    jump Campus_Map    
                    
            elif Current_Time == "Night" and "noentry" in K_RecentActions:
                    ch_k "Scram. I'll see you tomorrow."  
                    jump Campus_Map 
                    
            elif "noentry" in K_RecentActions:
                    call KittyFace("angry")
                    ch_k "GTFO."
                    call Statup("Kitty", "Love", 200, -5)
                    call Statup("Kitty", "Obed", 50, -2)
                    $ K_RecentActions.append("angry")                      
                    $ K_DailyActions.append("angry") 
                    jump Campus_Map  
            
            elif Current_Time == "Night" and (K_Sleep or K_SEXP >= 30):                                                   
                    #It's late but she really likes you
                    ch_k "It's late, [K_Petname], but you're so cute."                   
            elif Current_Time == "Night" and (ApprovalCheck("Kitty", 1000, "LI") or ApprovalCheck("Kitty", 600, "OI")):     
                    #It's late but she really likes you
                    ch_k "It's late, [K_Petname], but I could hang out a bit."                  
            elif K_Addict >= 50:
                    ch_k "I could use some attention. . ."
                    
            elif Current_Time == "Night" and (ApprovalCheck("Kitty", 500, "LI") or ApprovalCheck("Kitty", 300, "OI")):     
                    #she likes you well enough but it's late
                    ch_k "It's late [K_Petname]. Tomorrow?"
                    $ K_RecentActions.append("noentry")                      
                    $ K_DailyActions.append("noentry")  
                    jump Campus_Map    
                    
            elif ApprovalCheck("Kitty", 600, "LI") or ApprovalCheck("Kitty", 300, "OI"):                                    
                    #She quite likes you and lets you in   
                    ch_k "Sure, come on in [K_Petname]."        
            else:                                                                                                          
                    #She doesn't like you      
                    ch_k "Nah, you can stay out."
                    $ K_RecentActions.append("noentry")                      
                    $ K_DailyActions.append("noentry")  
                    jump Campus_Map
    
    # If you get this far, she's allowed you in
    $ bg_current = "bg kitty"         
    call EventCalls
    if K_Loc == "bg kitty" and "angry" in K_RecentActions:
        "Kitty pushes you back into the hall and slams the door. You head back to your room."
        $ Line = 0
        $ Trigger = 0
        jump Player_Room
    if bg_current != "bg kitty":
        jump Misplaced
            
label Kitty_Room:
    $ bg_current = "bg kitty"
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10: 
                call Round10
                call Girls_Location
                call EventCalls 
    call GirlsAngry        
    
# Kitty's Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if K_Loc == bg_current:
        $ Line = "You are in Kitty's room. What would you like to do?"
    else:
        $ Line = "You are in Kitty's room, but she isn't here. What would you like to do?"
    menu:
        "[Line]"
        
        "Chat":
                    call Chat
        
        "Would you like to study?":
                    call Study_Session
          
        "Lock the door" if "locked" not in P_Traits:
                if K_Loc == bg_current and not ApprovalCheck("Kitty", 1000):
                    ch_k "Um, I'd[K_like]rather you didn't lock my door, [K_Petname]?"
                else:
                    "You lock the door"
                    $ P_Traits.append("locked")     
                    call Taboo_Level
                   
        "Unlock the door" if "locked" in P_Traits:
                    "You unlock the door"
                    $ P_Traits.remove("locked")
                    call Taboo_Level  
                    
        "Sleep." if Current_Time == "Night" and K_Loc == bg_current:
                    call Round10
                    call Girls_Location
                    call EventCalls 
                    
        "Wait." if Current_Time != "Night":
                    call Round10
                    call Girls_Location
                    call EventCalls 
                            
        "Return to Your Room" if TravelMode:            
                    jump Player_Room_Entry 
        "Other Girl's Rooms" if TravelMode:
            menu:
                "Rogue's Room":   
                            jump Rogue_Room_Entry 
                "Emma's Room" if "met" in E_History:   
                            jump Emma_Room_Entry  
                "Laura's Room" if "met" in L_History: 
                            jump Laura_Room_Entry  
                "Back":
                            pass
        "Go to the Showers" if TravelMode:            
                    jump Shower_Room_Entry
                    
        "Leave" if not TravelMode:
                    call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
                    jump Campus_Entry
    
    if "angry" in K_RecentActions:
            call KittyFace("angry")
            ch_k "Go. Now."
            "Kitty pushes you back into the hall and slams the door. You head back to your room."
            $ Line = 0
            $ Trigger = 0
            jump Player_Room
    jump Kitty_Room


label Kitty_Study:                       #study events
            call Shift_Focus("Kitty")
            if Current_Time == "Night":
                ch_k "It's kinda late for studying. . . Tomorrow?"
                return
            elif Round <= 30:        
                ch_k "I don't know that there's time for that, maybe if we wait a bit. . ."
                return
            else:
                ch_k "Sure."
                        
            $ P_XP += 5
            $ Trigger = 0
            $ Line = renpy.random.choice(["You study for a while, it was fairly boring.", 
                    "You study up for the mutant biology test.", 
                    "You study for the math quiz.",
                    "You get bored and watch a movie instead.",
                    "You study for a few hours, that was fun.",
                    "You spend the next few hours studying the lit test."
                    "You study for the game design course."]) 
            "[Line]"       
            $ Line = 0
            call Statup("Kitty", "Love", 80, 2)
            $ D20 = renpy.random.randint(1, 20)    
            if D20 > 10:
                call Kitty_Frisky_Study   
            else:        
                $ P_XP += 5  
            call Wait  
            call Girls_Location
            return
#End Kitty Study
            
label Kitty_Frisky_Study:
            if D20 > 17 and ApprovalCheck("Kitty", 1000) and K_Blow > 5:
                        "Kitty reaches her hand through your textbook and you can feel it in your lap."
                        "She unzips you pants and pulls your dick out, stroking it slowly."
                        "She then dives her head under the book, and starts to lick it."        
                        call Kitty_SexAct("blow") 
            elif D20 > 14 and ApprovalCheck("Kitty", 1000) and K_Hand >= 5:
                        "Kitty reaches her hand through your textbook and you can feel it in your lap."
                        "She runs her finger along your erection, her hand passing through the jeans to touch your bare skin."
                        "She unzips you pants and pulls your dick out, stroking it slowly."  
                        call Kitty_SexAct("hand") 
            elif D20 > 10 and (ApprovalCheck("Kitty", 1300) or (K_Mast and ApprovalCheck("Kitty", 1000)))and K_Lust >= 70:
                        "Kitty wriggles against your shoulder, and her hand starts to stroke her crotch."  
                        if "unseen" in K_RecentActions:
                                $ K_RecentActions.remove("unseen")
                        $ Trigger = "masturbation"
                        call Kitty_SexAct("masturbate")      
            elif D20 > 10 and ApprovalCheck("Kitty", 1200) and K_Lust >= 30:
                        "Kitty takes the book from your hand, and sets it aside."
                        if not K_Over and not K_Legs:
                                #if she's mostly naked, cheat
                                call KittyFace("sly")                                
                                ch_k "I was[K_like]thinking about maybe \"strip studying,\". . ." 
                                $ K_Eyes = "down"
                                ch_k "but it would be a pretty short game. . ."
                                $ K_Eyes = "squint"
                                ch_k "Was there something you'd rather do?"                                
                                call Kitty_SexMenu   
                        else:
                                "She then asks if maybe you want to do some \"strip studying?\""
                                call Kitty_Strip_Study
            elif D20 >5 and ApprovalCheck("Kitty", 700) and K_Kissed > 1:
                        "Kitty leans close to you, and presses her lips to yours."         
                        call Kitty_SexAct("kissing")
            elif ApprovalCheck("Kitty", 500):
                        "Kitty squeezes close to you, and you spend the rest of the night cuddling."
            else:
                        return
                
            "Well that was certainly a productive use of your study time. . ."    
            return
    
label Kitty_Caught_Changing:
            call Shift_Focus("Kitty")
            $ D20 = renpy.random.randint(1, 20)
            
            call KittyFace("surprised", 1)
            $ K_Mouth = "kiss"
            if D20 > 17:        
                    #She's naked
                    call KittyOutfit("nude")
            elif D20 >15:       
                    #She's bottomless
                    $ K_Legs = 0
                    $ K_Panties = 0
            elif D20 >14:       
                    #She's Topless
                    $ K_Over = 0
                    $ K_Chest = 0
            elif D20 >10:       
                    #She's in her underwear
                    $ K_Over = 0
                    $ K_Legs = 0
                    $ K_Panties = "black panties"
            elif D20 >5:        
                    #She's wearing pants/skirt
                    $ K_Over = 0
            #else: #fully dressed
            call Set_The_Scene(Dress=0)
            if D20 > 17:        
                    #She's naked
                    "As you enter the room, you see Kitty is naked, and seems to be getting dressed."      
            elif D20 >14:       
                    #She's Topless
                    "As you enter the room, you see Kitty is practically naked, and seems to be getting dressed."  
            elif D20 >10:       
                    #She's in her underwear
                    "As you enter the room, you see Kitty is in her underwear, and seems to be getting dressed." 
            elif D20 >5:        
                    #She's wearing pants/skirt
                    "As you enter the room, you see Kitty has her top off, and seems to be getting dressed." 
            else:
                    #She's done
                    "As you enter the room, you see Kitty has just pulled her top on, and seems to have been getting dressed." 
                 
            if D20 > 5: 
                    if not ApprovalCheck("Kitty", (D20 *70)) or (not K_SeenPussy and not K_Panties) or (not K_SeenChest and not K_Chest):
                            # She is mad
                            call KittyFace("surprised")
                            $K_Brows = "angry"  
                            call Statup("Kitty", "Love", 80, -50)
                            if not K_Over or not K_Legs:
                                $ K_Over = "towel"
                                "She grabs a towel and covers up."
                    else:       
                            #She's cool with it, but confused.
                            call KittyFace("surprised", 1)      
                            $K_Brows = "confused"
                            if "exhibitionist" in K_Traits:
                                call Statup("Kitty", "Lust", 200, (2*D20))  
                            else:
                                call Statup("Kitty", "Lust", 200, D20)
                          
                    call Statup("Kitty", "Inbt", 70, 20)
                    if D20 > 17:
                        call Kitty_First_Bottomless
                        call Kitty_First_Topless(1)
                    elif D20 > 15:
                        call Kitty_First_Bottomless
                    elif D20 > 14:
                        call Kitty_First_Topless
                    menu:
                        ch_k "Why didn't you knock?!"
                        "Sorry, I should have.":  
                            call Statup("Kitty", "Love", 50, 3)
                            call Statup("Kitty", "Love", 80, 2)
                        "And miss the view?":
                            call Statup("Kitty", "Obed", 50, 3)
                            call Statup("Kitty", "Obed", 80, 2)
                            call Statup("Kitty", "Inbt", 60, 2)
                    #end if she's partially nude
            else:              
                    #She's fully dressed      
                    if not ApprovalCheck("Kitty", 900) and (not K_SeenPussy or not K_SeenChest):            
                            call KittyFace("angry")
                            $K_Brows = "confused"
                            call Statup("Kitty", "Love", 80, -5)
                    else:
                            call KittyFace("sexy")
                            $K_Brows = "confused"
                    call Statup("Kitty", "Inbt", 50, 4)
                    menu:
                        ch_k "Hey, [K_Petname]. . . {i}you{/i} were hoping I'd be naaaked."
                        "Sorry, I should have knocked.":   
                            call Statup("Kitty", "Love", 50, 2)
                            call Statup("Kitty", "Love", 80, 1)
                        "Well, to be honest. . .":
                            call Statup("Kitty", "Love", 50, -2)
                            call Statup("Kitty", "Obed", 50, 3)
                            call Statup("Kitty", "Obed", 80, 2)
                            call Statup("Kitty", "Inbt", 60, 2)
            call KittyFace("sexy")                
            if ApprovalCheck("Kitty", 750) and K_SeenPussy and K_SeenChest:
                    ch_k "I didn't say that I {i}minded{/i}. . ."                
                    $ K_Over = 0
                    pause 1     
                    call KittyOutfit
                    "She flashes you real quick."  
            else:
                    ch_k "Yeah. . . we wouldn't want any accidents. . ."   
            menu:
                    ch_k "So were you planning on staying?" 
                    "Sure, for a bit.":
                        pass
                    "Actually, I should get going. . .":
                        call KittyOutfit
                        call Worldmap            
            jump Kitty_Room
            return
            #End Kitty Caught Changing
# end Kitty's Room Interface //////////////////////////////////////////////////////////////////////


# Emma's Room Interface //////////////////////////////////////////////////////////////////////
label Emma_Room_Entry:   
    if "locked" in P_Traits:
            $ P_Traits.remove("locked")
    $ Nearby = []     
    call Shift_Focus("Emma")
    $ bg_current = "bg emma"           
    call Gym_Clothes
    call Taboo_Level
    call Set_The_Scene(Entry = 1) 
    $ P_RecentActions.append("traveling")
    $ D20 = renpy.random.randint(1, 20)
    
    if "Emma" in Party:
                    if Current_Time == "Night" or (Current_Time == "Evening" and Round <= 10):                         
                        if ApprovalCheck("Emma", 1000, "LI") or ApprovalCheck("Emma", 600, "OI"):     #It's late but she really likes you
                                ch_e "It's rather late, [E_Petname], but I can spare you some time." 
                        elif ApprovalCheck("Emma", 500, "LI") or ApprovalCheck("Emma", 300, "OI"):      #she likes you well enough but it's late
                                ch_e "It's late [E_Petname]. I'll see you tomorrow."
                                $ E_RecentActions.append("noentry")                      
                                $ E_DailyActions.append("noentry")  
                                if "Emma" in Party:
                                        $ Party.remove("Emma")   
                                "She heads inside and closes the door behind her."
                                jump Campus_Map         
                    else: #If Emma is in the party and it's not late in the day        
                                ch_e "Don't just stand at the door."
                    call EventCalls
                    jump Emma_Room   
    #End if Emma in Party
    
         
    if Round >= 10 and E_Loc == bg_current and "les" in E_RecentActions:
            call Girls_Caught_Lesing("Emma")
            if not _return:
                jump Emma_Room
                
    if Round >= 10 and E_Loc == bg_current and "gonnafap" in E_DailyActions and D20 >= 10: 
                    #Emma caught fapping  
                    call Girl_Caught_Mastubating("Emma")
    
    else: #not auto-caught fapping
            if "Emma" in Keys:
                menu:
                    "You have a key, what do you do?"
                    "Knock politely":
                            $ Line = "knock"
                            
                    "Use the key to enter.":
                            $ bg_current = "bg emma"
                            call Set_The_Scene
                        
            if Line != "knock" and "Emma" in Keys: 
                if E_Loc == "bg emma":
                        if Round <= 10:        
                                if  "noentry" in E_RecentActions or "angry" in E_RecentActions:
                                        call EmmaFace("angry")
                                        ch_e "Out!"    
                                        "Emma shoves you back into the hall."
                                        jump Campus_Map   
                                if Current_Time == "Night" :    
                                        "She's asleep in bed. You slip out quietly." #fix add options here.                            
                                        jump Campus_Map   
                        elif "gonnafap" in E_DailyActions and D20 >= 10: 
                                #Emma caught fapping  
                                call Girl_Caught_Mastubating("Emma")
                        elif D20 >=15 and (Current_Time == "Night" or Current_Time == "Morning"):                           
                                #Emma caught changing
                                call Emma_Caught_Changing
            #End "if you enter without knocking"
                
            else:#You knocked
                        $ Round -= 10 
                        "You knock on Emma's door."        
                        if E_Loc != "bg emma":
                                "Looks like she's not home right now."
                                jump Campus_Map
                            
                        if Round <= 10:
                                if Current_Time == "Night" :
                                    "There's no answer, she's probably asleep."  
                                    jump Campus_Map    
                    
                        if (D20 >=19 and E_Lust >= 50) or (D20 >=15 and E_Lust >= 70) or (D20 >=10 and E_Lust >= 80):    
                                #Emma caught fapping
                                "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
                                "After several seconds and some more shuffling of clothing, Emma comes to the door." 
                                call EmmaFace("perplexed")
                                call Set_The_Scene
                                ch_e "Well, I suppose you could tell I was a bit. . . occupied."
                                $ Tempmod += 10
                        elif D20 >=15 and (Current_Time == "Night" or Current_Time == "Morning"):                          
                                #Emma caught changing
                                "You hear the rustling of fabric and some knocking around, but after a few seconds Emma comes to the door."
                                call Set_The_Scene
                                ch_e "Oh, do come in [E_Petname], don't mind that I was just getting changed."   
                        elif "angry" in E_RecentActions:
                                ch_e "I haven't any time for this."
                                "Emma pushes you back into the hall and slams the door."
                                $ Trigger = 0
                                jump Campus_Map    
                        else:
                                call Set_The_Scene
                                "Emma opens the door and leans out."
                                "You ask if you can come inside."
            #End "if you knocked"
                    
            #if you reach this point then you've asked to enter.               
            if E_Loc != "bg emma":
                    "Looks like she's not home right now."                
                    if "Emma" in Keys:
                            menu:
                                "Go in and wait for her?"
                                "Yes":
                                        $ Line = 0
                                        jump Emma_Room
                                "No":
                                        pass
                    "You head back."
                    jump Campus_Map 
                    
            elif  "noentry" in E_RecentActions or "angry" in E_RecentActions:
                    call EmmaFace("angry")
                    ch_e "I believe I've made myself clear."  
                    jump Campus_Map    
                    
            elif Current_Time == "Night" and "noentry" in E_RecentActions:
                    ch_e "Later, [E_Petname]."  
                    jump Campus_Map 
                    
            elif "noentry" in E_RecentActions:
                    call EmmaFace("angry")
                    ch_e "Out."
                    call Statup("Emma", "Love", 200, -5)
                    call Statup("Emma", "Obed", 50, -2)
                    $ E_RecentActions.append("angry")                      
                    $ E_DailyActions.append("angry") 
                    jump Campus_Map  
            
            elif Current_Time == "Night" and (E_Sleep or E_SEXP >= 30):                                                   
                    #It's late but she really likes you
                    ch_e "It is getting late, [E_Petname]."
                    ch_e "but you are so adorable."                   
            elif Current_Time == "Night" and (ApprovalCheck("Emma", 1000, "LI") or ApprovalCheck("Emma", 600, "OI")):     
                    #It's late but she really likes you
                    ch_e "It is getting late, [E_Petname], but I could make some time."    
                    
            elif Current_Time == "Night" and (ApprovalCheck("Emma", 500, "LI") or ApprovalCheck("Emma", 300, "OI")):     
                    #she likes you well enough but it's late
                    ch_e "It's late [E_Petname]. I'll see you tomorrow."
                    $ E_RecentActions.append("noentry")                      
                    $ E_DailyActions.append("noentry")  
                    jump Campus_Map    
                    
            elif ApprovalCheck("Emma", 600, "LI") or ApprovalCheck("Emma", 300, "OI"):                                    
                    #She quite likes you and lets you in   
                    ch_e "Come in, [E_Petname]."        
            else:                                                                                                          
                    #She doesn't like you      
                    ch_e "I don't think that would be appropriate."
                    $ E_RecentActions.append("noentry")                      
                    $ E_DailyActions.append("noentry")  
                    jump Campus_Map
    
    # If you get this far, she's allowed you in
    $ bg_current = "bg emma"         
    call EventCalls
    if E_Loc == "bg emma" and "angry" in E_RecentActions:
        "Emma pushes you back into the hall and slams the door. You head back to your room."
        $ Line = 0
        $ Trigger = 0
        jump Player_Room
    if bg_current != "bg emma":
        jump Misplaced
            
label Emma_Room:
    $ bg_current = "bg emma"
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")
    call Taboo_Level
    call Set_The_Scene(Quiet=1)   
    call QuickEvents
    call Checkout(1)
    if Round <= 10: 
                call Round10
                call Girls_Location
                call EventCalls 
    call GirlsAngry        
    
# Emma's Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if E_Loc == bg_current:
        $ Line = "You are in Emma's room. What would you like to do?"
    else:
        $ Line = "You are in Emma's room, but she isn't here. What would you like to do?"
    menu:
        "[Line]"
        
        "Chat":
                    call Chat
        
        "Would you like to study?":                
                    call Study_Session
            
        "Lock the door" if "locked" not in P_Traits:
                if E_Loc == bg_current and not ApprovalCheck("Emma", 1000):
                    ch_e "Do you really think it's appropriate for you to lock the door to my room?"
                else:
                    "You lock the door"
                    $ P_Traits.append("locked")     
                    call Taboo_Level
                   
        "Unlock the door" if "locked" in P_Traits:
                    "You unlock the door"
                    $ P_Traits.remove("locked")
                    call Taboo_Level  
                    
        "Sleep." if Current_Time == "Night" and E_Loc == bg_current:
                    call Round10
                    call Girls_Location
                    call EventCalls 
                    
        "Wait." if Current_Time != "Night":
                    call Round10
                    call Girls_Location
                    call EventCalls 
                            
        "Return to Your Room" if TravelMode:            
                    jump Player_Room_Entry 
        "Other Girl's Rooms" if TravelMode:
            menu:
                "Rogue's Room":   
                            jump Rogue_Room_Entry 
                "Kitty's Room" if "met" in K_History:   
                            jump Kitty_Room_Entry  
                "Laura's Room" if "met" in L_History: 
                            jump Laura_Room_Entry  
                "Back":
                            pass
        "Go to the Showers" if TravelMode:            
                    jump Shower_Room_Entry
                    
        "Leave" if not TravelMode:
                    call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
                    jump Campus_Entry
    
    if "angry" in E_RecentActions:
            call EmmaFace("angry")
            ch_e "I think you should leave now."
            "Emma pushes you back into the hall and slams the door. You head back to your room."
            $ Line = 0
            $ Trigger = 0
            jump Player_Room
    jump Emma_Room
    
    


label Emma_Caught_Changing:
            call Shift_Focus("Emma")
            $ D20 = renpy.random.randint(1, 20)
            
            call EmmaFace("surprised", 1)
            $ E_Mouth = "kiss"
            if D20 > 17:        
                    #She's naked
                    call EmmaOutfit("nude")
            elif D20 >15:       
                    #She's bottomless
                    $ E_Legs = 0
                    $ E_Panties = 0
            elif D20 >14:       
                    #She's Topless
                    $ E_Over = 0
                    $ E_Chest = 0
            elif D20 >10:       
                    #She's in her underwear
                    $ E_Over = 0
                    $ E_Legs = 0
                    $ E_Panties = "white panties"
            elif D20 >5:        
                    #She's wearing pants/skirt
                    $ E_Over = 0
            #else: #fully dressed
            call Set_The_Scene(Dress=0)
            if D20 > 17:        
                    #She's naked
                    "As you enter the room, you see Emma is naked, and seems to be getting dressed."      
            elif D20 >14:       
                    #She's Topless
                    "As you enter the room, you see Emma is practically naked, and seems to be getting dressed."  
            elif D20 >10:       
                    #She's in her underwear
                    "As you enter the room, you see Emma is in her underwear, and seems to be getting dressed." 
            elif D20 >5:        
                    #She's wearing pants/skirt
                    "As you enter the room, you see Emma has her top off, and seems to be getting dressed." 
            else:
                    #She's done
                    "As you enter the room, you see Emma has just pulled her top on, and seems to have been getting dressed." 
                 
            if D20 > 5: 
                    if not ApprovalCheck("Emma", (D20 *70)) or (not E_SeenPussy and not E_Panties) or (not E_SeenChest and not E_Chest):
                            # She is mad
                            call EmmaFace("surprised")
                            $E_Brows = "angry"  
                            call Statup("Emma", "Love", 80, -50)
                            if not E_Over or not E_Legs:
                                $ E_Over = "towel"
                                "She grabs a towel and covers up."
                    else:       
                            #She's cool with it, but confused.
                            call EmmaFace("surprised", 1)      
                            $E_Brows = "confused"
                            if "exhibitionist" in E_Traits:
                                call Statup("Emma", "Lust", 200, (2*D20))  
                            else:
                                call Statup("Emma", "Lust", 200, D20)
                          
                    call Statup("Emma", "Inbt", 70, 20)
                    if D20 > 17:
                        call Emma_First_Bottomless
                        call Emma_First_Topless(1)
                    elif D20 > 15:
                        call Emma_First_Bottomless
                    elif D20 > 14:
                        call Emma_First_Topless
                    menu:
                        ch_e "Did you consider knocking?"
                        "Sorry, I should have.":  
                            call Statup("Emma", "Love", 50, 3)
                            call Statup("Emma", "Love", 80, 2)
                        "And miss the view?":
                            call Statup("Emma", "Obed", 50, 3)
                            call Statup("Emma", "Obed", 80, 2)
                            call Statup("Emma", "Inbt", 60, 2)
                    #end if she's partially nude
            else:              
                    #She's fully dressed      
                    if not ApprovalCheck("Emma", 900) and (not E_SeenPussy or not E_SeenChest):            
                            call EmmaFace("angry")
                            $E_Brows = "confused"
                            call Statup("Emma", "Love", 80, -5)
                    else:
                            call EmmaFace("sexy")
                            $E_Brows = "confused"
                    call Statup("Emma", "Inbt", 50, 4)
                    menu:
                        ch_e "Were you hoping to catch me in a compromising position?."
                        "Sorry, I should have knocked.":   
                            call Statup("Emma", "Love", 50, 2)
                            call Statup("Emma", "Love", 80, 1)
                        "Well, to be honest. . .":
                            call Statup("Emma", "Obed", 50, 3)
                            call Statup("Emma", "Obed", 80, 3)
                            call Statup("Emma", "Inbt", 60, 2)
            call EmmaFace("sexy")                
            if ApprovalCheck("Emma", 750) and E_SeenPussy and E_SeenChest:
                    ch_e "That does show initiative. . ."                
                    $ E_Over = 0
                    pause 1     
                    call EmmaOutfit
                    "She flashes you real quick."  
            else:
                    ch_e "Hmm, show a bit more care next time. . ."   
            menu:
                    ch_e "Did you have business with me?" 
                    "Yeah, a little.":
                        pass
                    "Actually, I should get going. . .":
                        call EmmaOutfit
                        call Worldmap            
            jump Emma_Room
            return
            #End Emma Caught Changing
            
# end Emma's Room Interface //////////////////////////////////////////////////////////////////////


# Laura's Room Interface //////////////////////////////////////////////////////////////////////
label Laura_Room_Entry:
    if "locked" in P_Traits:
            $ P_Traits.remove("locked")
    call Shift_Focus("Laura")
    $ bg_current = "bg laura"      
    $ Nearby = []     
    call Gym_Clothes
    call Set_The_Scene(Entry = 1)    
    call Taboo_Level
    $ P_RecentActions.append("traveling")
    $ D20 = renpy.random.randint(1, 20)
    
    if "Laura" in Party:
                    if Current_Time == "Night" or (Current_Time == "Evening" and Round <= 10):                         
                        if ApprovalCheck("Laura", 1000, "LI") or ApprovalCheck("Laura", 600, "OI"):     #It's late but she really likes you
                                ch_l "It's getting late, but come on in."    
                        elif L_Addict >= 50:
                                ch_l "Um, yeah, you'd better come in. . ."         
                        elif ApprovalCheck("Laura", 500, "LI") or ApprovalCheck("Laura", 300, "OI"):      #she likes you well enough but it's late
                                ch_l "See you tomorrow."
                                $ L_RecentActions.append("noentry")                      
                                $ L_DailyActions.append("noentry")  
                                if "Laura" in Party:
                                        $ Party.remove("Laura")   
                                "She heads inside and closes the door behind her."
                                jump Campus_Map         
                    else: #If Laura is in the party and it's not late in the day        
                                ch_l "Come on in."
                    call EventCalls
                    jump Laura_Room   
    #End if Laura in Party
    
     
    if Round >= 10 and L_Loc == bg_current and "les" in L_RecentActions:
            call Girls_Caught_Lesing("Laura")
            if not _return:
                jump Laura_Room
                
    if Round >= 10 and L_Loc == bg_current and "gonnafap" in L_DailyActions and D20 >= 5: 
                    #Laura caught fapping  
                    call Girl_Caught_Mastubating("Laura") 
    else: 
            #not auto-caught fapping
            if "Laura" in Keys:
                menu:
                    "You have a key, what do you do?"
                    "Knock politely":
                            $ Line = "knock"
                            
                    "Use the key to enter.":
                            $ bg_current = "bg laura"
                            call Set_The_Scene
                        
            if Line != "knock" and "Laura" in Keys: 
                    if L_Loc == "bg laura":
                        if Round <= 10:        #add "no" condtion here
                                if  "noentry" in L_RecentActions or "angry" in L_RecentActions:
                                        call LauraFace("angry")
                                        ch_l "Get out of my face."  
                                        "Laura shoves you back into the hall."
                                        jump Campus_Map   
                                if Current_Time == "Night" :    
                                        "She's asleep in bed. You slip out quietly." #fix add options here.                            
                                        jump Campus_Map   
                        elif "gonnafap" in L_DailyActions and D20 >= 5: 
                                #Laura caught fapping  
                                call Girl_Caught_Mastubating("Laura") 
                        elif D20 >=15 and (Current_Time == "Night" or Current_Time == "Morning"):                          
                                #Laura caught changing
#                                call Laura_Caught_Changing
                                call Girl_Caught_Changing
                                jump Laura_Room
            #End "if you enter without knocking"
                
            else:
                        #You knocked
                        $ Round -= 10 
                        "You knock on Laura's door."        
                        if L_Loc != "bg laura":
                                "Looks like she's not home right now."
                                jump Campus_Map
                            
                        if Round <= 10:
                                if Current_Time == "Night" :
                                    "There's no answer, she's probably asleep."  
                                    jump Campus_Map    
                    
                        if (D20 >=19 and L_Lust >= 50) or (D20 >=15 and L_Lust >= 70) or (D20 >=10 and L_Lust >= 80):    #Laura caught fapping
                                "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
                                "After several seconds and some more shuffling of clothing, Laura comes to the door."
                                call LauraFace("perplexed",1)
                                call Set_The_Scene              
                                ch_l "Um, hey [L_Petname], just working off some stress."
                                $ Tempmod += 10
                        elif D20 >=15 and (Current_Time == "Night" or Current_Time == "Morning"):                          #Laura caught changing
                                "You hear the rustling of fabric and some knocking around, but after a few seconds Laura comes to the door."
                                call Set_The_Scene
                                ch_l "Hey [L_Petname], I was just getting dressed."        
                        elif "angry" in L_RecentActions:
                                ch_l "Nope."
                                $ Trigger = 0
                                "Laura knocks you back into the hall and slams the door."
                                jump Campus_Map    
                        else:
                                call Set_The_Scene
                                "Laura opens the door and leans out."
                                "You ask if you can come inside."
            #End "if you knocked"
                    
            #if you reach this point then you've asked to enter.               
            if L_Loc != "bg laura":
                    "Looks like she's not home right now."                
                    if "Laura" in Keys:
                            menu:
                                "Go in and wait for her?"
                                "Yes":
                                        $ Line = 0
                                        jump Laura_Room
                                "No":
                                        pass
                    "You head back."
                    jump Campus_Map 
                    
            elif "noentry" in L_RecentActions or "angry" in L_RecentActions:
                    call LauraFace("angry")
                    ch_l "Fuck off."  
                    jump Campus_Map    
                    
            elif Current_Time == "Night" and "noentry" in L_RecentActions:
                    ch_l "Not tonight, [L_Petname]."
                    jump Campus_Map 
                                
            elif Current_Time == "Night" and (L_Sleep or L_SEXP >= 30):                                                   
                    #It's late but she really likes you
                    ch_l "It's late, but I was hoping you'd stop by."                    
            elif Current_Time == "Night" and (ApprovalCheck("Laura", 1000, "LI") or ApprovalCheck("Laura", 600, "OI")):     
                    #It's late but she really likes you
                    ch_l "It's late, [L_Petname], but you can come in."                
            elif L_Addict >= 50:
                    ch_l "You should come in. . ."                    
            elif Current_Time == "Night" and (ApprovalCheck("Laura", 500, "LI") or ApprovalCheck("Laura", 300, "OI")):     
                    #she likes you well enough but it's late
                    ch_l "It's late [L_Petname]. Come back tomorrow."
                    $ L_RecentActions.append("noentry")                      
                    $ L_DailyActions.append("noentry")  
                    jump Campus_Map                        
            elif ApprovalCheck("Laura", 600, "LI") or ApprovalCheck("Laura", 300, "OI"):                                    
                    #She quite likes you and lets you in   
                    ch_l "Make yourself at home, I guess."        
            else:                                                                                                           
                    #She doesn't like you      
                    ch_l "Nah."
                    $ L_RecentActions.append("noentry")                      
                    $ L_DailyActions.append("noentry")  
                    jump Campus_Map
    
    # If you get this far, she's allowed you in
    $ bg_current = "bg laura"         
    call EventCalls
    if L_Loc == "bg laura" and "angry" in L_RecentActions:
        $ Line = 0
        $ Trigger = 0
        "Laura shoves you back into the hall and slams the door. You head back to your room."
        jump Player_Room
    if bg_current != "bg laura":
        jump Misplaced
            
label Laura_Room:
    $ bg_current = "bg laura"
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)    
    if Round <= 10:
                call Round10
                call Girls_Location
                call EventCalls    
    call GirlsAngry    
    
# Laura's Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if L_Loc == bg_current:
        $ Line = "You are in Laura's room. What would you like to do?"
    else:
        $ Line = "You are in Laura's room, but she isn't here. What would you like to do?"
    menu:
        "[Line]"
        
        "Chat":
                    call Chat
        
        "Would you like to study?":
                    call Study_Session
         
        "Lock the door" if "locked" not in P_Traits:
                if L_Loc == bg_current and not ApprovalCheck("Laura", 1200):
                    ch_l "I don't want to feel caged up like that, [L_Petname]."
                else:
                    "You lock the door"
                    $ P_Traits.append("locked") 
                    call Taboo_Level
                   
        "Unlock the door" if "locked" in P_Traits:
                    "You unlock the door"
                    $ P_Traits.remove("locked")
                    call Taboo_Level  
                    
        "Sleep." if Current_Time == "Night":
                    call Round10
                    call Girls_Location
                    call EventCalls    
                    
        "Wait." if Current_Time != "Night":
                    call Round10
                    call Girls_Location
                    call EventCalls 
                    
        "Return to Your Room" if TravelMode:            
                    jump Player_Room_Entry   
        "Other Girl's Rooms" if TravelMode:
            menu:
                "Rogue's Room":   
                            jump Rogue_Room_Entry   
                "Kitty's Room" if "met" in K_History:   
                            jump Kitty_Room_Entry   
                "Emma's Room" if "met" in E_History:   
                            jump Emma_Room_Entry  
                "Back":
                            pass      
        "Go to the Showers" if TravelMode:            
                    jump Shower_Room_Entry
                    
        "Leave" if not TravelMode:
                    call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
                    jump Campus_Entry
    
    if "angry" in L_RecentActions:
            call LauraFace("angry")
            $ Line = 0
            $ Trigger = 0
            ch_l "Get out before we both regret it."
            "Laura shoves you back into the hall and slams the door. You head back to your room."
            jump Player_Room
    jump Laura_Room
    
#label Laura_Caught_Changing:
#            call Shift_Focus("Laura")
#            $ D20 = renpy.random.randint(1, 20)
            
#            call LauraFace("surprised", 1)
#            $ L_Mouth = "kiss"
#            if D20 > 17:        
#                    #She's naked
#                    call LauraOutfit("nude")
#            elif D20 >15:       
#                    #She's bottomless
#                    $ L_Legs = 0
#                    $ L_Panties = 0
#            elif D20 >14:       
#                    #She's Topless
#                    $ L_Over = 0
#                    $ L_Chest = 0
#            elif D20 >10:       
#                    #She's in her underwear
#                    $ L_Over = 0
#                    $ L_Legs = 0
#                    $ L_Panties = "black panties"
#            elif D20 >5:        
#                    #She's wearing pants/skirt
#                    $ L_Over = 0
#            #else: #fully dressed
#            call Set_The_Scene(Dress=0)
#            if D20 > 17:        
#                    #She's naked
#                    "As you enter the room, you see Laura is naked, and seems to be getting dressed."      
#            elif D20 >14:       
#                    #She's Topless
#                    "As you enter the room, you see Laura is practically naked, and seems to be getting dressed."  
#            elif D20 >10:       
#                    #She's in her underwear
#                    "As you enter the room, you see Laura is in her underwear, and seems to be getting dressed." 
#            elif D20 >5:        
#                    #She's wearing pants/skirt
#                    "As you enter the room, you see Laura has her top off, and seems to be getting dressed." 
#            else:
#                    #She's done
#                    "As you enter the room, you see Laura has just pulled her top on, and seems to have been getting dressed." 
                 
#            if D20 > 5: 
#                    if not ApprovalCheck("Laura", (D20 *70)) or (not L_SeenPussy and not L_Panties) or (not L_SeenChest and not L_Chest):
#                            # She is mad
#                            call LauraFace("surprised")
#                            $L_Brows = "angry"  
#                            call Statup("Laura", "Love", 80, -50)
#                            if not L_Over or not L_Legs:
#                                $ L_Over = "towel"
#                                "She grabs a towel and covers up."
#                    else:       
#                            #She's cool with it, but confused.
#                            call LauraFace("surprised", 1)      
#                            $L_Brows = "confused"
#                            if "exhibitionist" in L_Traits:
#                                call Statup("Laura", "Lust", 200, (2*D20))  
#                            else:
#                                call Statup("Laura", "Lust", 200, D20)
                          
#                    call Statup("Laura", "Inbt", 70, 20)
#                    if D20 > 17:
#                        call Laura_First_Bottomless
#                        call Laura_First_Topless(1)
#                    elif D20 > 15:
#                        call Laura_First_Bottomless
#                    elif D20 > 14:
#                        call Laura_First_Topless
#                    menu:
#                        ch_l "Yeah?"
#                        "Sorry, I should have knocked.":  
#                            call Statup("Laura", "Love", 50, 2)
#                            call Statup("Laura", "Love", 80, 4)
#                        "And miss the view?":
#                            call Statup("Laura", "Obed", 50, 2)
#                            call Statup("Laura", "Obed", 80, 2)
#                            call Statup("Laura", "Inbt", 60, 1)
#                    #end if she's partially nude
#            else:              
#                    #She's fully dressed      
#                    if not ApprovalCheck("Laura", 800) and (not L_SeenPussy or not L_SeenChest):            
#                            call LauraFace("angry")
#                            $L_Brows = "confused"
#                            call Statup("Laura", "Love", 80, -5)
#                    else:
#                            call LauraFace("sexy")
#                            $L_Brows = "confused"
#                    call Statup("Laura", "Inbt", 50, 3)
#                    menu:
#                        ch_l "Hey, [L_Petname]. Trying to catch a peek?"
#                        "Sorry, I should have knocked.":   
#                            call Statup("Laura", "Love", 50, 2)
#                            call Statup("Laura", "Love", 80, 2)
#                        "Well, to be honest. . .":
#                            call Statup("Laura", "Love", 50, -2)
#                            call Statup("Laura", "Obed", 50, 2)
#                            call Statup("Laura", "Obed", 80, 2)
#                            call Statup("Laura", "Inbt", 60, 1)
#            call LauraFace("sexy")                
#            if ApprovalCheck("Laura", 750) and L_SeenPussy and L_SeenChest:
#                    ch_l "I don't mind."
#                    $ L_Over = 0
#                    $ L_Upskirt = 1
#                    pause 1     
#                    call LauraOutfit
#                    $ L_Upskirt = 0
#                    "She flashes you real quick."  
#            else:
#                    ch_l "Uh-huh . . ."   
#            menu:
#                    ch_l "So did you plan to stay?" 
#                    "Sure, for a bit.":
#                        pass
#                    "Actually, I should get going. . .":
#                        call LauraOutfit(Changed=0)
#                        call Worldmap            
#            jump Laura_Room
#            return
#            #End Laura Caught Changing
# end Laura's Room Interface //////////////////////////////////////////////////////////////////////


 

#label Girl_Caught_Changing(Girl=0):
#            #This is called by room entries when the girl might have been changing. 
#            if not Girl:
#                    return
#            call Shift_Focus(Girl)
#            $ D20 = renpy.random.randint(1, 20)
            
#            call AnyFace(Girl,"surprised", 1,Mouth="kiss")
            
#            if D20 > 17:        
#                    #She's naked
#                    call AnyOutfit(Girl,"nude")
#            else:
#                    #restore base outfit
#                    call AnyOutfit(Girl,6)                     
#                    if D20 >15:       
#                            #She's bottomless
#                            call AnyOutfit(Girl,9) #Legs
#                            call AnyOutfit(Girl,10) #Panties
#                    elif D20 >14:       
#                            #She's Topless
#                            call AnyOutfit(Girl,7) #Over
#                            call AnyOutfit(Girl,8) #Chest
#                    elif D20 >10:       
#                            #She's in her underwear
#                            call AnyOutfit(Girl,7) #Over
#                            call AnyOutfit(Girl,9) #Legs
#                    elif D20 >5:        
#                            #She's wearing pants/skirt
#                            call AnyOutfit(Girl,7) #Over
#            #else: #fully dressed
#            call Set_The_Scene(Dress=0)
#            if D20 > 17:        
#                    #She's naked
#                    "As you enter the room, you see [Girl] is naked, and seems to be getting dressed."      
#            elif D20 >14:       
#                    #She's Topless
#                    "As you enter the room, you see [Girl] is practically naked, and seems to be getting dressed."  
#            elif D20 >10:       
#                    #She's in her underwear
#                    "As you enter the room, you see [Girl] is in her underwear, and seems to be getting dressed." 
#            elif D20 >5:        
#                    #She's wearing pants/skirt
#                    "As you enter the room, you see [Girl] has her top off, and seems to be getting dressed." 
#            else:
#                    #She's done
#                    "As you enter the room, you see [Girl] has just pulled her top on, and seems to have been getting dressed." 
                 
#            if D20 > 5: 
#                    if not ApprovalCheck(Girl, (D20 *70)) and SeenCheck(Girl):
#                            # if D20*70 is less than her approval, and this is the first you've seen of her bits. . .
#                            call AnyFace(Girl,"surprised",Brows="angry")  
#                            call Statup(Girl, "Love", 80, -50)
                            
#                            if not OverNum(Girl) or (OverNum(Girl)+ChestNum(Girl) <5) or (PantsNum(Girl) < 5 and HoseNum(Girl) < 10):
#                                # if either she is mostly topless or mostly bottomless)
#                                call AnyOutfit(Girl,7,TempOver="towel")  
#                                "She grabs a towel and covers up."
#                    else:       
#                            #She's cool with it, but confused.
#                            call AnyFace(Girl,"surprised", 1,Brows = "confused")
#                            if ExhibitionistCheck(Girl):
#                                call Statup(Girl, "Lust", 200, (2*D20))  
#                            else:
#                                call Statup(Girl, "Lust", 200, D20)
                          
#                    call Statup(Girl, "Inbt", 70, 20)
                    
#                    if D20 > 17:
#                        call expression Girl + "_First_Bottomless"
#                        call expression Girl + "_First_Topless" pass (1) #same as "call Rogue_First_Topless(1)"
#                    elif D20 > 15:
#                        call expression Girl + "_First_Bottomless"
#                    elif D20 > 14:
#                        call expression Girl + "_First_Topless"
                       
#                    if Girl == "Rogue":
#                            ch_r "Hey! Learn to knock maybe?!"
#                    elif Girl == "Kitty":
#                            ch_k "Why didn't you knock?!"
#                    elif Girl == "Emma":
#                            ch_e "Did you consider knocking?"
#                    elif Girl == "Laura":
#                            ch_l "Yeah?"
#                    menu:
#                        extend ""
#                        "Sorry, I should have knocked.":  
#                                call Statup(Girl, "Love", 50, 2)
#                                call Statup(Girl, "Love", 80, 4)
#                        "And miss the view?":
#                                call Statup(Girl, "Obed", 50, 2)
#                                call Statup(Girl, "Obed", 80, 2)
#                                call Statup(Girl, "Inbt", 60, 1)
#                    #end if she's partially nude
#            else:              
#                    #She's fully dressed      
#                    if not ApprovalCheck(Girl, 800) and not SeenCheck(Girl):            
#                            call AnyFace(Girl,"angry",Brows="confused")
#                            call Statup(Girl, "Love", 80, -5)
#                    else:
#                            call AnyFace(Girl,"sexy",Brows="confused")
#                    call Statup(Girl, "Inbt", 50, 3)
                    
#                    if Girl == "Rogue":
#                            ch_r "Well hello there, [R_Petname]. Hoping to see something more?"
#                    elif Girl == "Kitty":
#                            ch_k "Hey, [K_Petname]. . . {i}you{/i} were hoping I'd be naaaked."
#                    elif Girl == "Emma":
#                            ch_e "Were you hoping to catch me in a compromising position?."
#                    elif Girl == "Laura":
#                            ch_l "Hey, [L_Petname]. Trying to catch a peek?"
                            
#                    menu:
#                        extend ""
#                        "Sorry, I should have knocked.":   
#                                call Statup(Girl, "Love", 50, 2)
#                                call Statup(Girl, "Love", 80, 2)
#                        "Well, to be honest. . .":
#                                call Statup(Girl, "Love", 50, -2)
#                                call Statup(Girl, "Obed", 50, 2)
#                                call Statup(Girl, "Obed", 80, 2)
#                                call Statup(Girl, "Inbt", 60, 1)
#            call AnyFace(Girl,"sexy")
#            if ApprovalCheck(Girl, 750) and SeenCheck(Girl) >= 3:
#                    #she flashes you
#                    if Girl == "Rogue":
#                            ch_r "You could have just asked, [R_Petname]."           
#                    elif Girl == "Kitty":
#                            ch_k "I didn't say that I {i}minded{/i}. . ."              
#                    elif Girl == "Emma":
#                            ch_e "That does show initiative. . ."                
#                    elif Girl == "Laura":
#                            ch_l "I don't mind."
                         
#                    call AnyOutfit(Girl,7) #Over off                      
#                    call AnyOutfit(Girl,11) #Upskirt up
#                    pause 1                         
#                    call AnyOutfit(Girl,5,0,0) #restore current outfit
#                    if not PantiesNum(Girl):
#                            call expression Girl + "_First_Bottomless" pass (1)
#                    if not ChestNum(Girl):                    
#                            call expression Girl + "_First_Topless" pass (1) #same as "call Rogue_First_Topless(1)"
#                    "She flashes you real quick."  
#            else:
#                    #if she doesn't flash you
#                    if Girl == "Rogue":
#                            ch_r "Well, it happens, just be careful next time."  
#                    elif Girl == "Kitty":
#                            ch_k "Yeah. . . we wouldn't want any accidents. . ."  
#                    elif Girl == "Emma":
#                            ch_e "Hmm, show a bit more care next time. . ." 
#                    elif Girl == "Laura":
#                            ch_l "Uh-huh . . ."  
#            if Girl == "Rogue": 
#                    ch_r "Well, are you planning to stick around?" 
#            elif Girl == "Kitty":
#                    ch_k "So were you planning on staying?" 
#            elif Girl == "Emma": 
#                    ch_e "Did you have business with me?" 
#            elif Girl == "Laura":
#                    ch_l "So did you plan to stay?"  
#            menu:
#                    extend ""
#                    "Sure, for a bit.":
#                            pass
#                    "Actually, I should get going. . .":
#                            call AnyOutfit(Girl,6,Changed=0)
#                            call Worldmap            
##            jump Laura_Room
#            return
##End Girl Caught Changing / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
         
label Study_Room_Entry:  
    if "locked" in P_Traits:
            $ P_Traits.remove("locked") 
    $ Nearby = []     
    $ bg_current = "bg study"     
    call Gym_Clothes
    call Taboo_Level
    call Set_The_Scene(Entry = 1)  
    menu:
            "You're at the door, what do you do?"
            "Knock politely":
                    $ Line = "knock"
                    
            "Enter without knocking":
                 if Current_Time == "Night":
                         "The door is locked. It's not like you could just walk through it."
                         jump Study_Room_Entry
                                                 
            "Use the key to enter" if Current_Time == "Night" and "Xavier" in Keys:
                    "You use your key."
                    $ Line = 0
            
            "Ask Kitty" if Current_Time == "Night" and "Kitty" in Party:
                    $ Line = "kitty"
                    
            "Leave":
                    "You head back."
                    jump Campus_Map 
     
    if Line == "knock": 
        if Current_Time == "Night":
            "There's no answer, he's probably asleep." 
            jump Study_Room_Entry
        else:           
            ch_x "Yes, enter. . ."
            "You enter the room."
    elif Line == "kitty":
            ch_k "Yeah?"
            while True:
                menu:
                    extend ""
                    "Could you phase through the door and open it for me?":
                            if "Sneakthief" in K_Traits:
                                ch_k "No problem. . ."
                                jump Study_Room
                            elif "no thief" in K_RecentActions:
                                ch_k "I told you, no."
                            elif ApprovalCheck("Kitty", 400, "I") or ApprovalCheck("Kitty", 1400):
                                call Statup("Kitty", "Love", 90, 3) 
                                call Statup("Kitty", "Obed", 50, 10) 
                                call Statup("Kitty", "Inbt", 60, 10)  
                                ch_k "Heh, you have a wicked mind. . ."
                                $ K_Traits.append("Sneakthief")
                                jump Study_Room
                            else:
                                call Statup("Kitty", "Love", 90, -3) 
                                call Statup("Kitty", "Obed", 50, 2) 
                                call Statup("Kitty", "Inbt", 60, 2)  
                                ch_k "Um, I don't really feel comfortable doing that. . ."
                                $ K_RecentActions.append("no thief")
                    "Open the door.":
                            if "Sneakthief" in K_Traits:
                                ch_k "No problem. . ."
                                jump Study_Room
                            elif "no thief" in K_RecentActions:
                                ch_k "I told you, no."
                            elif ApprovalCheck("Kitty", 500, "O") or ApprovalCheck("Kitty", 1600):
                                call Statup("Kitty", "Obed", 50, 15) 
                                call Statup("Kitty", "Inbt", 60, 10)  
                                ch_k "Heh, if you say so. . ."
                                $ K_Traits.append("Sneakthief")
                                jump Study_Room
                            else:
                                call Statup("Kitty", "Love", 90, -5) 
                                call Statup("Kitty", "Obed", 50, 2) 
                                call Statup("Kitty", "Inbt", 60, 2)  
                                ch_k "Um, no."
                                $ K_RecentActions.append("no thief")
                    "Never mind. [[Leave]":
                            "You head back."
                            jump Campus_Map 
            jump Study_Room_Entry
    elif Current_Time != "Night":                
            ch_x "You know, [Playername], it is not polite to enter a room unannounced."
    $ Cnt = 0                        
                
label Study_Room:
    $ bg_current = "bg study"
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:         
            if Current_Time == "Night":                         
                "It's late, you head back to your room."
                jump Player_Room
            else:
                call Wait                 
                call Girls_Location
    
    call GirlsAngry
    
# Study Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if Current_Time == "Night":
        $ Line = "You are in Xavier's Study, but he isn't in at the moment. What would you like to do?"
    else:
        $ Line = "You are in Xavier's Study. What would you like to do?"
    menu:
        "[Line]"        
        "Chat" if Current_Time == "Night": #fix, open up once sex while in office is fine
                    call Chat
        
        "Plan Omega!" if Current_Time != "Night" and R_Loc == bg_current:
                    if ApprovalCheck("Rogue", 1500, TabM=1, Loc="No") and P_Lvl >= 5:
                        jump Plan_Omega
                    else:
                        ch_r "What?"
        "Plan Kappa!" if Current_Time != "Night" and K_Loc == bg_current:
                    if "Xavier's photo" in P_Inventory and P_Lvl >= 5 and ApprovalCheck("Kitty", 1500, TabM=1, Loc="No"):                   
                        jump Plan_Kappa
                    else:
                        ch_k "What?"     
        "Plan Psi!" if Current_Time != "Night" and E_Loc == bg_current:
                    if ApprovalCheck("Emma", 1500, TabM=1, Loc="No") and P_Lvl >= 5:
                        jump Plan_Psi
                    else:
                        ch_e "What?"        
            
        "Explore" if Current_Time == "Night" and "explore" not in P_RecentActions: 
                    $ Cnt = 0    
                    $ P_RecentActions.append("explore")
                    jump Study_Room_Explore
            
        "Wait":
                    if Current_Time == "Night":
                            "You probably don't want to be here when Xavier gets in."
                    elif Current_Time == "Evening":
                            ch_x "If you don't mind, I would like to close up for the evening?"
                            "You return to your room."
                            jump Player_Room                    
                    else:           
                            call Wait  
                            call Girls_Location
                            ch_x "Not that I mind the company, but is there something I can do for you?"
                              
        "Leave" if not TravelMode:
                    call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
                    jump Campus_Entry  
        "Return to Your Room" if TravelMode:            
                    jump Player_Room_Entry 
                    
    jump Study_Room
    
    
label Study_Room_Explore:
    $ Line = 0
    $ D20 = renpy.random.randint(1, 20)    
    menu:
        "Where would you like to look?"
        "Bookshelf":
            if D20 >= 5 + Cnt:
                    $ Line = "book"
            else:
                    "As you search the bookshelf, you accidentally knock one of the books off."
                    "It hammers against the floor, and a little light blinks on the desk."
        "Left Desk Drawer":
            if K_Loc != bg_current:
                    "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            elif D20 >= 10 + Cnt:
                    $ Line = "left"
            else:
                    "As you open the drawer, it makes a loud a squeak."
                    "As you look around, you notice a little light starts blinking on the desk."
        "Middle Desk Drawer":
            if K_Loc != bg_current:
                    "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            elif D20 >= 15 + Cnt:
                    $ Line = "mid"
            else:
                    "As you open the drawer, it makes a loud a squeak."
                    "As you look around, you notice a little light starts blinking on the desk."
        "Right Desk Drawer":
            if K_Loc != bg_current:
                    "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            elif D20 >= 5 + Cnt:
                    $ Line = "right"
            else:
                    "As you open the drawer, it makes a loud a squeak."
                    "As you look around, you notice a little light starts blinking on the desk."
        "Never mind [[back]": 
                    jump Study_Room
    
    $ D20 = renpy.random.randint(1, 20)
    if not Line:
                "Probably best to get out of here."
                "You slip out and head back to your room."
                jump Player_Room_Entry 
    elif Line == "book":
            if D20 >= 15 and "Well Studied" not in Achievements:            
                "As you check the books on the shelf, you notice that one of them is actually a disguised lockbox."
                if K_Loc == bg_current:
                    menu:
                        "Since Kitty is around, have her check inside?"
                        "Check in the box":
                            if ApprovalCheck("Kitty", 700, "I") or ApprovalCheck("Kitty", 1800):
                                if "Well Studied" not in Achievements:
                                        call Statup("Kitty", "Obed", 50, 10) 
                                        call Statup("Kitty", "Inbt", 60, 15)  
                                        ch_k "Sounds like a plan."
                                        "Kitty swipes her hand through the box, and pulls out a stack of bills."
                                        "Looks like Xavier was hiding a rainy day fund in here."
                                        $ P_Cash += 500
                                        "[[$500 acquired.]"
                                        $ Achievements.append("Well Studied")
                                else:
                                        "Looks like this has been thoroughly looted."
                            else:#Kitty doesn't approve 
                                call Statup("Kitty", "Love", 90, -3) 
                                call Statup("Kitty", "Obed", 50, 1) 
                                call Statup("Kitty", "Inbt", 60, 2)  
                                ch_k "I really don't think we should do that."                            
                        "Put it back.":
                            "You place the box back on the shelf."
                else:#Kitty's not there
                            "You can't think of any way to get it open, too bad you aren't a ghost or something."
                            "You place the box back on the shelf."
            elif D20 >= 15:
                "There doesn't seem to be anything more of interest in here."
            else:
                "You search through the books for a few minutes, but don't find anything."
                "It would probably take a more thorough search."            
    elif Line == "left":            
            if "Xavier's photo" not in P_Inventory: 
                if D20 >= 10:
                        "Buried under a pile of documents, you find a printed out photo."
                        "It appears to be a selfie of Mystique making out with Xavier."
                        "She's reaching down to adjust his . . . oh, {i}that's{/i} interesting."
                        "[[Xavier's photo acquired.]"
                        $ P_Inventory.append("Xavier's photo")
                else:                 
                        "You search through some documents, but don't find anything."
                        "It would probably take a more thorough search."   
            else:      
                        "There doesn't seem to be anything more of interest in here."
    elif Line == "mid":
            if "All" not in Keys:
                "Under a few trinkets, you find a small keyring."
                "[[Keyring acquired.]"
                if "Xavier" not in Keys:
                        $ Keys.append("Xavier") 
                if "Rogue" not in Keys:
                        $ Keys.append("Rogue")
                if "Kitty" not in Keys:
                        $ Keys.append("Kitty")
                if "Emma" not in Keys:
                        $ Keys.append("Emma")
                if "Laura" not in Keys:
                        $ Keys.append("Laura")
                if "All" not in Keys:
                        $ Keys.append("All")
            else:
                "There doesn't seem to be anything interesting in here."
    elif Line == "right":
            "There doesn't seem to be anything more of interest in here, maybe later?"
    $ Cnt += 3
    jump Study_Room_Explore
# end Study's Room Interface //////////////////////////////////////////////////////////////////////