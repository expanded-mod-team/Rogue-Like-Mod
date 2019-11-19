# Date Night //////////////////////////////////////////////////////////////////////
# Count = price of things
# Count2 = tempmod
    
label Kitty_Date_Ask:
    #From the chat menu, you ask Kitty to meet you
    call Shift_Focus("Kitty")
    if "yesdate" in K_DailyActions:  
        call KittyFace("bemused")
        ch_k "Lol, I already said \"yes.\""  
        return         
    if "askeddate" in K_DailyActions:  
        call KittyFace("angry")
        ch_k "Geez, stop bothering me already!"  
        return 
    if "stoodup" in K_Traits:  
        call Kitty_Date_Stood_Up
        $ K_DailyActions.append("askeddate")    
        return 
    $ K_RecentActions.append("askeddate")   
    $ K_DailyActions.append("askeddate")   
    
    if K_Break[0] and "ex" in K_Traits:
        call KittyFace("angry")
        ch_k "You can't just pretend that nothing happened!"  
        return     
    if "ex" in K_Traits:
        if ApprovalCheck("Kitty", 1200):
            call KittyFace("bemused",Brows = "sad" ) 
            ch_k "I don't know, we used to have fun. Maybe. . ."            
        else:
            call KittyFace("angry",Eyes = "side")
            ch_k "I[K_like]don't think so." 
            return 
       
    if "stoodup" in K_History or "deadbeat" in K_History: 
        if "stoodup" in K_History:
            call KittyFace("angry",Eyes = "side")                
            ch_k "I don't want to be left in the quad again." 
        if "deadbeat" in K_History:  
            call KittyFace("angry")  
            if "stoodup" in K_History:
                ch_k "And last time we went out, you[K_like]left me with the check!"  
            else:
                ch_k "Last time we went out, you[K_like]left me with the check!"           
        menu:
            extend ""
            "Sorry about that, I'll take care of it this time.":
                    if ApprovalCheck("Kitty", 650):
                        call KittyFace("sad")
                        ch_k "Well, I guess I can give you another chance, just don't disappoint me again."
                    else:
                        call KittyFace("angry")
                        ch_k "Yeah[K_like]fool me once. . . no thanks, [K_Petname]." 
                        return
            "Yeah, so?":
                    if ApprovalCheck("Kitty", 1400):
                        call KittyFace("angry", Mouth = "grimace")
                        ch_k "Why do I[K_like]put up with you?"
                        call KittyFace("bemused")        
                    elif ApprovalCheck("Kitty", 500, "O"):
                        call KittyFace("sad")
                        call Statup("Kitty", "Obed", 80, 3)
                        ch_k "Well, I guess we can still have fun. . ."
                    elif ApprovalCheck("Kitty", 650):
                        call KittyFace("angry")
                        call Statup("Kitty", "Love", 80, -5)
                        call Statup("Kitty", "Inbt", 60, 2) 
                        ch_k "Yeah[K_like]I'm going out with {i}you,{/i} dick."  
                        return 
                    else:
                        call KittyFace("angry")
                        call Statup("Kitty", "Love", 80, -10)
                        call Statup("Kitty", "Obed", 80, -3)
                        call Statup("Kitty", "Inbt", 60, 2) 
                        ch_k "Asshole."  
                        return             
        call Statup("Kitty", "Obed", 30, 3)
        call Statup("Kitty", "Obed", 80, 2)
    elif ApprovalCheck("Kitty", 650):
        call KittyFace("smile")
        ch_k "Sure, see you then."
    elif ApprovalCheck("Kitty", 400):                
        call KittyFace("angry",Eyes = "side")
        ch_k "I've[K_like]got better things to do. . ."
        return
    else:
        call KittyFace("angry")
        ch_k "[K_Like]no way."
        return 
    
    $ Count = 0
    #She mostly agreed, do you ask for a double date?
    menu:
        "Good, I'll meet you in the campus square." if bg_current != "bg campus" or Current_Time != "Evening": 
                    call KittyFace("smile")
        "Good, let's get going then." if bg_current == "bg campus" and Current_Time == "Evening": 
                    call KittyFace("smile")
        "And I was thinking of asking. . .": 
                    menu:
                        ch_p "And I was thinking of asking. . ."
                        "Rogue along too." if "yesdate" in R_DailyActions or "yesdate" not in P_DailyActions:
                                    $ Count = K_LikeRogue
                        "Emma along too." if "yesdate" in E_DailyActions or "yesdate" not in P_DailyActions:
                                    $ Count = K_LikeEmma
                        "Laura along too." if "yesdate" in L_DailyActions or "yesdate" not in P_DailyActions:
                                    $ Count = K_LikeLaura
                        "Never mind, probably a bad idea.":  
                                    call KittyFace("confused")
                                    ch_k "Um. . ."
                                    if bg_current != "bg campus": 
                                            ch_p "Ok, I'll meet you in the campus square."
    if Count:
        #If you asked about another girl. . .
        if Count >= 600 and ApprovalCheck("Kitty", 800, "OI"): #Count is "K_LikeX"
            call KittyFace("smile")
            ch_k "Sure, sounds fun."                                
        elif Count >= 750:
            call KittyFace("bemused")
            ch_k "Hm, yeah. . ."                                
        elif ApprovalCheck("Kitty", 1300, "LO"): 
            call KittyFace("sad")
            ch_k "I guess if that's what you want. . ."             
        else:
            call KittyFace("angry")
            ch_k "You wish, player!"  
            $ Count = 0
            return
        $ K_DailyActions.append("yesdouble") 
        if bg_current != "bg campus": 
                ch_p "Ok, I'll meet you in the campus square."    
        $ Count = 0
    
    if bg_current != "bg campus" or Current_Time != "Evening": 
            ch_k "K', see you then!"
    $ K_DailyActions.append("yesdate")                  
    $ P_DailyActions.append("yesdate") 
    return


label Kitty_Date_Stood_Up:
    # if "stoodup" in K_Traits
    if K_Loc != bg_current:
            "Kitty storms into the room." 
            $ K_Loc = bg_current
            call Display_Kitty
    else:
            "Kitty turns to you." 
    call KittyFace("confused")
    call Statup("Kitty", "Love", 80, -10)
    ch_k "Hey, what gives? You didn't show up for our date!"
    if "stoodup" in K_History:
        call KittyFace("angry")
        call Statup("Kitty", "Love", 80, -5)
        ch_k "Again!"
    menu:
            extend ""
            "Oh, sorry about that, slipped my mind.":
                if ApprovalCheck("Kitty", 800, "LO") or ApprovalCheck("Kitty", 1200):
                        call KittyFace("angry")
                        call Statup("Kitty", "Love", 80, 5)
                        ch_k "I guess it can happen, but don't make a habit of it."
                        if "stoodup" in K_History:
                            call KittyFace("sad",Eyes="side")
                            call Statup("Kitty", "Obed", 80, 5)
                            ch_k "You really need to get your priorities in order."  
                elif "stoodup" in K_History:
                        call KittyFace("sad",Eyes="side")
                        call Statup("Kitty", "Love", 80, -5)
                        call Statup("Kitty", "Obed", 80, 5)
                        ch_k "You really need to get your priorities in order."                    
                else:
                        call KittyFace("angry")
                        call Statup("Kitty", "Obed", 80, -2)
                        call Statup("Kitty", "Inbt", 60, 2) 
                        ch_k "You'll really have to make it up to me next time."
                
            "I can't imagine that happening, maybe you got the date wrong?":
                if "stoodup" in K_History and ApprovalCheck("Kitty", 800, "O"):                            
                        call KittyFace("confused")
                        call Statup("Kitty", "Obed", 90, 15)
                        ch_k "Are you. . . I was sure that I. . ."                            
                        call KittyFace("confused",Eyes="side")
                        ch_k "Huh."                                
                elif ApprovalCheck("Kitty", 700, "O"):
                        call KittyFace("angry")
                        call Statup("Kitty", "Obed", 80, 5)
                        call Statup("Kitty", "Obed", 90, 10)
                        ch_k "Um. . . I don't think so, but I guess it's possible. . ."     
                elif ApprovalCheck("Kitty", 500, "I"):
                        call KittyFace("angry")           
                        $ K_RecentActions.append("angry") 
                        $ K_DailyActions.append("angry")   
                        call Statup("Kitty", "Love", 80, -10)
                        call Statup("Kitty", "Inbt", 70, 10) 
                        ch_k "Pull the other one, jerk."
                else:
                        call KittyFace("sad",Eyes="side")    
                        $ K_RecentActions.append("angry") 
                        $ K_DailyActions.append("angry")  
                        call Statup("Kitty", "Love", 80, -5)
                        call Statup("Kitty", "Obed", 80, -5)
                        call Statup("Kitty", "Inbt", 60, 5) 
                        ch_k "Well. . . I don't think so, stop bothering me."
                        
            "Yeah, I found something better to do.": 
                if ApprovalCheck("Kitty", 1200, "LO"):
                        call KittyFace("sad",Eyes="side")
                        call Statup("Kitty", "Love", 80, -5)
                        call Statup("Kitty", "Obed", 80, 5)
                        if "stoodup" in K_History:
                                ch_k "Yeah. . . "
                                ch_k "You always seem to. . ."                            
                        else:
                                call Statup("Kitty", "Obed", 80, 10)
                                ch_k "Well. . . "
                                ch_k "well don't let it happen again."
                elif ApprovalCheck("Kitty", 800, "LO"):
                        call KittyFace("angry",Eyes="side")
                        $ K_RecentActions.append("angry") 
                        $ K_DailyActions.append("angry")  
                        call Statup("Kitty", "Love", 80, -10)
                        call Statup("Kitty", "Obed", 80, 20) 
                        ch_k "Well that's rude."
                else:
                        call KittyFace("angry")
                        $ K_RecentActions.append("angry") 
                        $ K_DailyActions.append("angry")  
                        call Statup("Kitty", "Love", 80, -15)
                        call Statup("Kitty", "Inbt", 60, 5) 
                        ch_k "Asshole."
                        
    $ K_Traits.remove("stoodup") 
    if "stoodup" not in K_History:  
            $ K_History.append("stoodup") 
            
    call CleartheRoom("All",Check=1)
    if _return >= 3:
        #if the room is full,
        call Remove_Girl("Kitty")
        "Kitty wanders off." 
    return
    
# End Kitty Ask / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Kitty_Date_Prep:
    #This gets Kitty Dressed and ready for Dinner, called by Date_Night
    $ Taboo = 40
    if K_Schedule[7]:
        #if she has a date outfit set
        if K_Schedule[7] == 2:
            $ K_Outfit = "red outfit"
        elif K_Schedule[7] == 3:
            $ K_Outfit = "custom1"
        elif K_Schedule[7] == 4:
            $ K_Outfit = "gym"
        elif K_Schedule[7] == 5:
            $ K_Outfit = "custom2"
        elif K_Schedule[7] == 6:
            $ K_Outfit = "custom3"
        else:
            $ K_Outfit = "pink outfit"
    else:
        $ Options = ["pink outfit", "red outfit"]
        $ Options.append("custom1") if K_Custom[0] == 2 else Options
        $ Options.append("custom2") if K_Custom2[0] == 2 else Options
        $ Options.append("custom3") if K_Custom3[0] == 2 else Options
        $ renpy.random.shuffle(Options) 
        $ K_Outfit = Options[0]
        $ del Options[:]  
    $ K_Loc = "date"
    call KittyOutfit(Changed=1)
    call KittyFace("smile")
    return

# End Kitty Prep / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Kitty Dinner Menu/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /       
label Kitty_Dinner(K_Cost=0):
    #Called by Date Dinner, picked Kitty's food
    menu:
        "For Kitty you order. . ."
        "Surf and turf. ($20)":
                call KittyFace("sad",Brows = "surprised")
                ch_k "Um, I[K_like]don't really eat shellfish. . ."  
                call KittyFace
                call Statup("Kitty", "Love", 80, -5)
                call Statup("Kitty", "Love", 200, -2)
                $ K_Cost = 20
                call Date_Bonus("Kitty",-11)
                $ K_RecentActions.append("surfturf")
        "Steak. ($15)":  
                call KittyFace("smile")
                ch_k "Sounds delish."
                call Statup("Kitty", "Love", 80, 5)
                call Statup("Kitty", "Love", 200, 2)
                $ K_Cost = 15
                $ K_RecentActions.append("ribeye")
        "Chicken. ($10)":
                call KittyFace("smile")
                ch_k "Chicken's fine."
                call Statup("Kitty", "Love", 50, 1)
                call Statup("Kitty", "Love", 80, 3)
                $ K_Cost = 10
                $ K_RecentActions.append("chicken")
        "Just a salad. ($5)":
                $ K_Mouth = "sad"
                $ K_Eyes = "sexy"
                $ K_Brows = "confused"            
                ch_k "I do enjoy a nice salad."  
                call Statup("Kitty", "Love", 60, -3)
                call Statup("Kitty", "Obed", 50, 2)
                $ K_Cost = 5
                $ K_RecentActions.append("salad")
        "Why don't you choose, Kitty?":
                call Date_Bonus("Kitty",2)
                call KittyFace("smile")
                ch_k "Well thanks, [K_Petname]. I think I'll have the steak."            
                call Statup("Kitty", "Love", 80, 7)   
                call Statup("Kitty", "Love", 200, 2) 
                $ K_Cost = 15
                $ K_RecentActions.append("ribeye")
                
    if Party[0] == "Kitty":
        $ Prime_Cost = K_Cost
    else:
        $ Second_Cost = K_Cost
    call Date_Bonus("Kitty",K_Cost)
    return
# End Kitty Menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /          

    
# Start Kitty Dinner Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Kitty_Dinner_Sex(Previous=0,K_Bonus=0,Options=["nothing"]):
    #Called by Dinner Sex, if Kitty is chosen.
    
    if Party[0] == "Kitty":
        $ K_Bonus = Prime_Bonus + Prime_Cost
    else:
        $ K_Bonus = Second_Bonus + Second_Cost
        
    if K_Anal and ApprovalCheck("Kitty", 1500) and K_Bonus >=15: 
        $ Options.append("anal")        
    if K_Sex and ApprovalCheck("Kitty", 1500) and K_Bonus >=10:
        $ Options.append("sex")
    if K_Blow and ApprovalCheck("Kitty", 1300) and K_Bonus >=10:
        $ Options.append("blow")      
    if K_Hand and ApprovalCheck("Kitty", 1000) and K_Bonus >=10:
        $ Options.append("hand")
    if K_FondleP and ApprovalCheck("Kitty", 1000) and K_Bonus >=10:
        $ Options.append("pussy")
    if ApprovalCheck("Kitty", 1000) and K_Bonus >=10:
        $ Options.append("foot")
    
    if "Rogue" in Previous:
        $ Previous = "Rogue"
    elif "Emma" in Previous:
        $ Previous = "Emma"
    elif "Laura" in Previous:
        $ Previous = "Laura"
    else:
        $ Previous = 0
        
    $ renpy.random.shuffle(Options) 
    
    call KittyFace("sexy")
    if Options[0] == "nothing":
        pass
    elif Options[0] == "anal":        
        "Halfway through the meal, Kitty gets a sly look on her face." 
        "She nods her head suggestively towards the restrooms, and then excuses herself."
        call Date_Sex_Break("Kitty",Previous)
        if _return == 4: #you refused
                call KittyFace("sadside", 2)
                "You wait a few minutes until she returns, seemingly a bit annoyed at you."
                call Statup("Kitty", "Love", 90, -5)
                call Statup("Kitty", "Inbt", 80, -10)
                call Date_Bonus("Kitty",-5)
        else:
                if _return == 1: #other girl is fine
                        "A few seconds later, you and [Previous] follow her and she drags you both inside, locking the door behind you." 
                        "She spends the next several minutes taking it up the ass while [Previous] feels you both up."
                else:
                        "A few seconds later, you follow her and she drags you inside, locking the door behind you." 
                        "She spends the next several minutes taking it up the ass."
                if _return == 3:
                    "[Previous] stares daggers at you both as you return to the table."
                    call Date_Bonus(Previous,-10)
                ch_k "That was {i}so{/i} worth it."  
                call Statup("Kitty", "Inbt", 50, 9)
                call Statup("Kitty", "Inbt", 80, 3)
                $ K_SeenPeen += 1
                $ K_Anal += 1
                $ P_Semen -= 1
                $ K_RecentActions.append("anal")    
                $ K_RecentActions.append("dinnersex")                    
                $ K_DailyActions.append("anal") 
    elif Options[0] == "sex":        
        "Halfway through the meal, Kitty gets a sly look on her face." 
        "She nods her head suggestively towards the restrooms, and then excuses herself."
        call Date_Sex_Break("Kitty",Previous)
        if _return == 4: #you refused
                call KittyFace("sadside", 2)
                "You wait a few minutes until she returns, seemingly a bit annoyed at you."
                call Statup("Kitty", "Love", 90, -5)
                call Statup("Kitty", "Inbt", 80, -10)
                call Date_Bonus("Kitty",-5)
        else:
                if _return == 1: #other girl is fine
                        "A few seconds later, you and [Previous] follow her and she drags you both inside, locking the door behind you." 
                        "She spends the next several minutes fucking you raw while [Previous] feels you both up."
                else:
                        "A few seconds later, you follow her and she drags you inside, locking the door behind you." 
                        "She spends the next several minutes fucking you raw."
                if _return == 3:
                    "[Previous] stares daggers at you both as you return to the table."
                    call Date_Bonus(Previous,-10)
                ch_k "That was a workout."
                call Statup("Kitty", "Inbt", 50, 8)
                call Statup("Kitty", "Inbt", 80, 2)
                $ K_SeenPeen += 1
                $ K_Sex += 1
                $ P_Semen -= 1            
                $ K_RecentActions.append("sex")   
                $ K_RecentActions.append("dinnersex")                    
                $ K_DailyActions.append("sex") 
    elif Options[0] == "blow":
        "Halfway through the meal, Kitty gets a sly look on her face, then knocks her fork off the table."
        "She ducks under the table after it, and unzips your pants." 
        call Date_Sex_Break("Kitty",Previous)
        if _return == 4: #you refused
                call KittyFace("sadside", 2)
                "You zip them back up and shoo her away. She gets back up from under the table."
                call Statup("Kitty", "Love", 90, -5)
                call Statup("Kitty", "Inbt", 80, -5)
                call Date_Bonus("Kitty",-3)
        else:
                if _return == 1: #other girl is fine
                        "[Previous] shifts closer and wraps one arm around you, the other hand caressing Kitty's cheek."
                        "Kitty then procedes to blow you for several minutes until you cum."
                elif _return == 2: #other girl is fine
                        "She then procedes to blow you for several minutes until you cum, while [Previous] pretends to be occupied."
                else: 
                        "She then procedes to blow you for several minutes until you cum."
                call Statup("Kitty", "Inbt", 50, 6)
                call Statup("Kitty", "Inbt", 80, 2)
                $ K_RecentActions.append("blow")   
                $ K_RecentActions.append("dinnersex")                    
                $ K_DailyActions.append("blow") 
                if K_Swallow:
                    "Kitty wipes her mouth as she climbs out from under the table."
                    ch_k "That hit the spot. . ."            
                    $ K_Addict -= 20
                    $ K_Swallow += 1  
                    $ K_RecentActions.append("swallow")                      
                    $ K_DailyActions.append("swallow")       
                else:
                    "Kitty grabs the napkin off your lap and uses it to collect the jiz."
                    ch_k "I feel kinda sorry for the busboys."
                call Statup("Kitty", "Inbt", 30, 4)
                call Statup("Kitty", "Inbt", 80, 2)
                $ K_SeenPeen += 1
                $ K_Blow += 1
                $ P_Semen -= 1
                if _return == 3:
                    "[Previous] stares daggers at you both as she crawls out from under the table."  
                    call Date_Bonus(Previous,-10)
    elif Options[0] == "hand":
        "Halfway through the meal, Kitty gets a sly look on her face, then shifts her chair around next to yours."
        call Date_Sex_Break("Kitty",Previous)
        if _return == 4: #you refused
                call KittyFace("sadside", 2)
                "She tries to unzip your pants under the table, but you shoo her away."
                call Statup("Kitty", "Love", 90, -5)
                call Statup("Kitty", "Inbt", 80, -5)
                call Date_Bonus("Kitty",-2)
        else:
                if _return == 1: #other girl is fine
                        "She unzips your pants under the table, and proceeds to caress your cock."
                        "On the other side, [Previous] also reaches down and gets into the action."
                        "They continue stroking it until you cum into the napkin."
                elif _return == 2: #other girl is fine
                        "She unzips your pants under the table, and proceeds to caress your cock, while [Previous] pretends to be occupied."
                        "She continues stroking it until you cum into the napkin."
                else: 
                        "She unzips your pants under the table, and proceeds to caress your cock."
                        "She continues stroking it until you cum into the napkin."
                ch_k "I feel kinda sorry for the busboys."
                call Statup("Kitty", "Inbt", 30, 4)
                call Statup("Kitty", "Inbt", 80, 2)
                $ K_Hand += 1
                $ P_Semen -= 1
                $ K_RecentActions.append("hand")     
                $ K_RecentActions.append("dinnersex")                  
                $ K_DailyActions.append("hand") 
                if _return == 3:
                    "[Previous] stares daggers at you both from across the table."
                    call Date_Bonus(Previous,-5)
    elif Options[0] == "pussy":
        "Halfway through the meal, Kitty gets a sly look on her face, then shifts her chair around next to yours."
        call Date_Sex_Break("Kitty",Previous)
        if _return == 4: #you refused
                if K_Legs:
                    "She takes your hand and pulls it over to her crotch, shoving it under her [K_Legs]."
                else:
                    "She takes your hand and shoves it into her crotch."
                call KittyFace("sadside", 2)
                "With a glance at [Previous], you jerk your hand away."
                call Statup("Kitty", "Love", 90, -5)
                call Statup("Kitty", "Inbt", 80, -5)
                call Date_Bonus("Kitty",-3)
        else:
                if K_Legs:
                    "She takes your hand and pulls it over to her crotch, shoving it under her [K_Legs]."
                else:
                    "She takes your hand and shoves it into her crotch."
                "You can feel that she's warm as a furnace."
                if _return == 1: #other girl is fine
                        "On the other side, [Previous] also reaches down and gets into the action."
                        "You both stroke her pussy for several minutes, until finally she shudders in orgasm." 
                        "You slowly pulls your hands free with a sly smile."
                else: 
                    "You stroke her pussy for several minutes, until finally she shudders in orgasm." 
                    "You slowly pulls your hand free with a sly smile."
                if _return == 3:
                    call Date_Bonus(Previous,-3)
                ch_k "Thanks, [K_Petname], I needed that."
                if _return == 1:
                    ch_k "You too, [Previous]."
                    $ K_Les += 1
                call Statup("Kitty", "Love", 90, 3)
                call Statup("Kitty", "Inbt", 30, 5)            
                call Statup("Kitty", "Inbt", 90, 2)
                $ K_FondleP += 1
                $ K_Org += 1
                $ K_RecentActions.append("fondle pussy") 
                $ K_RecentActions.append("dinnersex")                      
                $ K_DailyActions.append("fondle pussy") 
    elif Options[0] == "foot":
        "Halfway through the meal, Kitty gets a sly look on her face, then shifts a bit lower in her seat."
        "You suddenly feel her foot in your lap, gently caressing your cock."
        call Date_Sex_Break("Kitty",Previous)
        if _return == 4: #you refused
                call KittyFace("sadside", 2)
                "You shift uncomfortably and push her foot away."
                call Statup("Kitty", "Love", 90, -5)
                call Statup("Kitty", "Inbt", 80, -3)
                call Date_Bonus("Kitty",-1)
        else:
                call Statup("Player", "Focus", 60, 10)
                if _return == 1: #other girl is fine
                        "[Previous] decides to join in the fun and adds her foot to the mix."
                        call Statup("Player", "Focus", 60, 5)
                if _return == 3:
                    call Date_Bonus(Previous,-3)
                "After several minutes of this, she pulls back."
                ch_k "Just a taste of things to come, [K_Petname]."
                call Statup("Kitty", "Inbt", 80, 3)
                $ K_RecentActions.append("dinnersex") 
    
    call KittyFace(B = 0)
    return    
# End Kitty Dinner Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    

    
    
# Start Kitty Movie Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Kitty_Movie_Sex(Previous=0,K_Bonus=0, Options=["nothing"]):
    # Called by Movie_Sex if Kitty is chosen
    if Party[0] == "Kitty":
        $ K_Bonus = Prime_Bonus
    else:
        $ K_Bonus = Second_Bonus
    
    if "horror" in P_RecentActions:
        $ K_Bonus += 20
    
    if "Rogue" in Previous:
        $ Previous = "Rogue"
    elif "Emma" in Previous:
        $ Previous = "Emma"
    elif "Laura" in Previous:
        $ Previous = "Laura"
    else:
        $ Previous = 0
        
    if ApprovalCheck("Kitty", 500, Bonus=(10*K_Bonus)):
        call KittyFace("kiss", 1)
        if "romcom" in P_RecentActions: 
            "Halfway through the movie, inspired by the action on screen, Kitty turns to you and starts to make out with you."
        elif "action" in P_RecentActions:        
            "Halfway through the movie, adrenaline pumping from the action on screen, Kitty turns to you and starts to make out with you."
        elif "horror" in P_RecentActions:  
            "Halfway through the movie, freaked out by the tension on screen, Kitty huddles in your arms, and then starts to make out with you."
        elif "drama" in P_RecentActions:   
            "Halfway through the movie, Kitty turns to you with a shrug and starts to make out with you."
        $ K_RecentActions.append("kissing") 
        $ K_RecentActions.append("moviesex")                       
        $ K_DailyActions.append("kissing")      
        call Date_Sex_Break("Kitty",Previous)   
        if _return == 4:
                #the other girl stops you
                "You settle back into your seats and watch the rest of the film."
                return
        elif _return == 1:
                #the other girl joins in. . .
                "[Previous] also leans in and begins kissing the both of you."
        elif _return == 3:
                #the other girl is mad. . .
                "You get back to it, [Previous] settles back into her seat with a glare."
            
    
        if K_Anal and ApprovalCheck("Kitty", 2000, Bonus=(10*K_Bonus)) and PantsNum("Kitty") <= 5:
                    call KittyFace("sexy", 1)
                    if K_Panties:
                        "As you make out, Kitty reaches down and undoes your fly. She pulls her panties aside and shifts into your lap."
                    else:
                        "As you make out, Kitty reaches down and undoes your fly. She hikes her skirt up a bit and shifts into your lap."
                    call Date_Sex_Break("Kitty",Previous,1)
                    if _return == 3:
                            #the other girl stormed out. . .
                            ch_k "Well that was awkward."                
                    "She gingerly squeezes your cock into her ass and begins to grind up and down, quietly enough that the other patrons don't seem to notice."
                    if _return == 1:
                            #the other girl joins you. . .
                            "[Previous] also leans over and toys with Kitty's pussy."
                    if K_CreamA:
                            if K_Panties:
                                "After several minutes of this, you can't take it anymore and come inside her."
                                "She pulls her panties back up and returns to her seat."
                            else:
                                "After several minutes of this, you can't take it anymore and come inside her."
                                "She wipes off as best she can and shifts back into her seat."
                            $ K_CreamA += 1
                            $ K_RecentActions.append("creampie anal")                      
                            $ K_DailyActions.append("creampie anal") 
                    else:
                            "After several minutes of this, she pulls out and shifts back into her seat, finishing you off with her hand."
                            if K_Swallow:
                                if 0 < _return < 3: #if 1 or 2
                                    "You cum into the popcorn bucket, which she and [Previous] then finish off together."
                                else:
                                    "You cum into the popcorn bucket, which she then finishes off."
                                $ K_Addict -= 20
                                $ K_Swallow += 1
                                $ K_Spunk.append("mouth")                          
                                $ K_RecentActions.append("swallowed")                      
                                $ K_DailyActions.append("swallowed") 
                            else:
                                "You cum into the popcorn bucket, which she phases into the floor."
                    ch_k "Talk about a \"4D\" movie."
                    call Statup("Kitty", "Inbt", 50, 4)
                    call Statup("Kitty", "Inbt", 90, 3)
                    $ K_SeenPeen += 1
                    $ K_Anal += 1
                    $ P_Semen -= 1
                    $ K_RecentActions.append("anal")                      
                    $ K_DailyActions.append("anal")  
        elif K_Sex and ApprovalCheck("Kitty", 2000, Bonus=(10*K_Bonus)) and PantsNum("Kitty") <= 5:
                    call KittyFace("sexy", 1)
                    if K_Panties:
                        "As you make out, Kitty reaches down and undoes your fly. She pulls her panties aside and shifts into your lap."
                    else:
                        "As you make out, Kitty reaches down and undoes your fly. She hikes her skirt up a bit and shifts into your lap."
                    call Date_Sex_Break("Kitty",Previous,1)                    
                    if _return == 3:
                            #the other girl stormed out. . .
                            ch_k "Well that was awkward."                
                    "Seconds later, she's slowly rocking on your cock, quietly enough that the other patrons don't seem to notice."
                    if _return == 1:
                            #the other girl joins you. . .
                            "[Previous] also leans over and toys with Kitty's pussy."
                    if K_CreamP:
                        if K_Panties:
                            "After several minutes of this, you can't take it anymore and come inside her."
                            "She pulls her panties up over her dripping slit and returns to her seat."
                        else:
                            "After several minutes of this, you can't take it anymore and come inside her."
                            "She wipes up as best she can and returns to her seat."
                        $ K_CreamP += 1
                        $ K_RecentActions.append("creampie sex")                      
                        $ K_DailyActions.append("creampie sex") 
                    else:
                        "After several minutes of this, she pulls out and shifts back into her seat, finishing you off with her hand."
                        if K_Swallow:
                                if 0 < _return < 3: #if 1 or 2
                                    "You cum into the popcorn bucket, which she and [Previous] then finish off together."
                                else:                                    
                                    "You cum into the popcorn bucket, which she then finishes off."   
                                $ K_Spunk.append("mouth")   
                                $ K_Addict -= 20
                                $ K_Swallow += 1
                                $ K_RecentActions.append("swallowed")                      
                                $ K_DailyActions.append("swallowed") 
                        else:
                                "You cum into the popcorn bucket, which she phases into the floor."
                    ch_k "Talk about a \"4D\" movie."
                    call Statup("Kitty", "Inbt", 50, 4)
                    call Statup("Kitty", "Inbt", 90, 3)
                    $ K_SeenPeen += 1
                    $ K_Sex += 1
                    $ P_Semen -= 1
                    $ K_RecentActions.append("sex")                      
                    $ K_DailyActions.append("sex")             
        elif K_Blow and ApprovalCheck("Kitty", 1300, Bonus=(10*K_Bonus)):
                    call KittyFace("sucking", 1)
                    "As you make out, Kitty reaches down and undoes your fly. She then bends down and wraps her lips around it."
                    call Date_Sex_Break("Kitty",Previous,1)                
                    if _return == 3:
                            #the other girl stormed out. . .
                            ch_k "Well that was awkward."                
                    if _return == 1:
                            #the other girl joins you. . .
                            "[Previous] also leans over joins Kitty at licking your cock."
                            "They take turns sucking on it contentedly for several minutes before you finally cum."   
                    else:
                            "She sucks on it contentedly for several minutes before you finally cum."            
                    $ K_Spunk.append("mouth")  
                    if K_Swallow:
                        "Kitty wipes her mouth as she shifts back into her seat and washes it down with some soda."
                        call KittyFace("sexy")
                        ch_k "Mmmm, that hit the spot. . ."
                        $ K_Addict -= 20
                        $ K_Swallow += 1
                        $ K_RecentActions.append("swallowed")                      
                        $ K_DailyActions.append("swallowed") 
                    else:
                        "You cum into the popcorn bucket, which she phases into the floor."
                        ch_k "That should give archeolgists a surprise."
                    call Statup("Kitty", "Inbt", 40, 3)
                    call Statup("Kitty", "Inbt", 80, 2)
                    $ K_SeenPeen += 1
                    $ K_Blow += 1
                    $ P_Semen -= 1
                    $ K_RecentActions.append("blow")                      
                    $ K_DailyActions.append("blow") 
        elif K_Hand and ApprovalCheck("Kitty", 1000, Bonus=(10*Count2)):
                    call KittyFace("sexy")
                    "As you make out, Kitty reaches down and pulls out your cock." 
                    call Date_Sex_Break("Kitty",Previous,1)             
                    if _return == 3:
                            #the other girl stormed out. . .
                            ch_k "Well that was awkward."   
                            "She then leans over and begins to stroke your cock." 
                    elif _return == 1: 
                            #the other girl joins in. . .
                            "She then leans over and begins to stroke your cock."
                            "[Previous] leans in and joins her, and they share a smile."
                    else:
                            "She then leans over and begins to stroke it." 
                    call KittyFace("surprised")
                    if K_FondleP:
                        if _return == 1: 
                                #the other girl joins in. . .
                                "You also reach down and begin stroking their pussies."
                        else:
                            if K_Legs:
                                    "You also lean over, reach into her [K_Legs], and begin to stroke her pussy."
                            elif K_Hose:
                                    "You also lean in, reach under her [K_Hose], and begin to stroke her pussy."
                            elif K_Panties:
                                    "You also lean in, reach under her panties, and begin to stroke her pussy."
                            else:
                                    "You also lean over, notice she isn't wearing anything down there, and begin to stroke her pussy."
                    call KittyFace("sexy", 1, Eyes = "closed")
                    if K_FondleP:
                        if _return == 1: 
                            "After several minutes of this, Kitty and [Previous] shudder in orgasm, which sets you off as well."
                        else:
                            "After several minutes of this, she shudders in orgasm, which sets you off as well."
                        "Kitty catches the jiz in the popcorn bucket."
                    $ K_Eyes = "sexy"
                    if K_Swallow:
                            if 0 < _return < 3: #if 1 or 2
                                "The girls finish off the remaining popcorn with a grin."    
                            else:
                                "She finishes off the remaining popcorn with a grin."                    
                            $ K_Spunk.append("mouth")  
                            ch_k "Best topping they got here, [K_Petname]."     
                            $ K_Addict -= 20
                            $ K_Swallow += 1
                            $ K_RecentActions.append("swallowed")                      
                            $ K_DailyActions.append("swallowed") 
                    else:
                            "You cum into the popcorn bucket, which she phases into the floor."
                            ch_k "That should give archeolgists a surprise."
                    call Statup("Kitty", "Love", 90, 2)
                    call Statup("Kitty", "Inbt", 40, 3)
                    call Statup("Kitty", "Inbt", 80, 2)
                    $ K_FondleP += 1
                    $ K_Org += 1        
                    $ K_Hand += 1
                    $ P_Semen -= 1
                    $ K_RecentActions.append("hand")                      
                    $ K_DailyActions.append("hand") 
        elif K_FondleP and ApprovalCheck("Kitty", 900, Bonus=(10*K_Bonus)):
                    call KittyFace("sexy")                    
                    if K_Legs:
                            "As you make out, Kitty grabs your hand and shoves it down her [K_Legs]."
                    elif K_Hose:
                            "As you make out, Kitty grabs your hand and shoves it down her [K_Hose]."
                    elif K_Panties:
                            "As you make out, Kitty grabs your hand and shoves it down her panties."
                    else:
                            "As you make out, Kitty grabs your hand and shoves it between her legs."
                    call Date_Sex_Break("Kitty",Previous,1)
                    $ K_Eyes = "closed"
                    if _return == 3:
                            #the other girl stormed out. . .
                            ch_k "Well that was awkward." 
                            "You get back to work."
                    elif _return == 1: 
                            #the other girl joins in. . .
                            "[Previous] leans in and begins to fondle her breasts as well."   
                    "After several minutes of this, she shudders in orgasm and leans back with a contented sigh."
                    $ K_Eyes = "sexy"
                    ch_k "Hmm, that felt great, [K_Petname]."
                    call Statup("Kitty", "Love", 90, 2)
                    call Statup("Kitty", "Inbt", 40, 2)
                    call Statup("Kitty", "Inbt", 80, 2)
                    $ K_FondleP += 1
                    $ K_Org += 1    
                    $ K_RecentActions.append("fondle pussy")                      
                    $ K_DailyActions.append("fondle pussy") 
        elif ApprovalCheck("Kitty", 1200, Bonus=(5*K_Bonus)) and K_Panties:
                    call KittyFace("sexy")
                    "After making out for a few minutes, Kitty gets a sly look on her face and reaches into her pocket."
                    "After a second, she hands you a cloth lump, apparently her panties." 
                    $ K_DailyActions.append("pantyless") 
                    call Statup("Kitty", "Inbt", 60, 2)
                    $ K_Panties = 0
                    ch_k "[K_Like]hold on to those for me, uh?"
        elif ApprovalCheck("Kitty", 1200, Bonus=(5*K_Bonus)):
                    call KittyFace("sexy")
                    "After making out for a few minutes, Kitty gets a sly look on her face, then shifts a bit lower in her seat."
                    if PantsNum("Kitty") > 5:
                        "Looking down, you notice she's pulled down her pants enough that you can see her bare pussy, lit by the movie screen."  
                    elif K_Legs == "shorts":
                        "Looking down, you notice she's pulled down her shorts enough that you can see her bare pussy, lit by the movie screen."   
                    else:
                        "Looking down, you notice she's hiked up her skirt enough that you can see her bare pussy, lit by the movie screen."            
                    call Statup("Kitty", "Inbt", 60, 2)
                    call Kitty_First_Bottomless(1)
                    ch_k "Just giving you a little taste. . ."
    #End Kitty movie sex options
    call KittyOutfit
    return
# End Kitty Movie Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    

    
# Start Kitty Date End/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label K_Date_End:   
    #Called if you end up with Kitty at the end of the date
    if bg_current != "bg player":
            #skips this portion if you are in the player's room already
            menu:
                "Take Kitty back to her room?":
                    pass
                "Just leave and head back to yours.":
                    call Date_Ditched
                    jump Date_Over    
                    
            $ bg_current = "bg kitty"
            $ K_Loc = "bg kitty"
            if "Rogue" in Party:
                $ R_Loc = "bg kitty"
            if "Emma" in Party:
                $ E_Loc = "bg kitty"
            if "Laura" in Party:
                $ L_Loc = "bg kitty"
            call Set_The_Scene(Dress=0)
            call Taboo_Level    
    
    if Party[0] == "Kitty":
        $ Count = Prime_Bonus
        $ Count2 = Party[1] #the other girl
    else:
        $ Count = Second_Bonus
        $ Count2 = Party[0] #the other girl
            
    if bg_current != "bg player":
        "You walk Kitty back to her room."
    if Count < 0:      
        call KittyFace("angry", 0,Eyes = "side")
        ch_k "You[K_like]really need to get your shit together, [Playername]."
        if bg_current == "bg player":
                "She phases through the wall toward her room."
        else:
                "She slams the door on you."
        call Set_The_Scene(Entry=1,Dress=0)
        $ Count = 0
        call Kitty_Date_Over(0)
        jump Date_End
    else: 
        if Count > 20:
            call KittyFace("sexy", 1)
            if bg_current == "bg player":
                    ch_k "That was fun, [K_Petname]. Do I have to go . . ."    
            else:
                    ch_k "That was fun, [K_Petname]. Do you have to go . . ."             
        else:
            call KittyFace("smile", 1)
            ch_k "Well that was fun, [K_Petname]. Text me later."
        
        $ K_Date += 1
        menu:
            extend ""
            "Could I get a good night kiss?":
                if ApprovalCheck("Kitty", 600, Bonus=(10*Count)):
                    $ K_Mouth = "smile"
                    ch_k "Heh, I guess so. . ."
                    call Date_Sex_Break("Kitty",Count2,2)
                    $ MultiAction = 0
                    call K_KissPrep 
                    $ MultiAction = 1
                if ApprovalCheck("Kitty", 900, Bonus=(10*Count)):
                    call KittyFace("sexy", 1)
                    ch_k "Hmmm . . ."   
                    if bg_current == "bg player":
                            ch_k "Could I. . . maybe come inside for a minute?"
                    else:
                            ch_k "Maybe. . . come inside for a minute?"
                    call Date_Sex_Break("Kitty",Count2)
                    if _return == 4:
                        if bg_current == "bg player":
                                ch_p "You should probably get going, sorry."
                        else:
                                ch_p "I should probably get going, sorry."
                        call Kitty_Date_Over(0)
                        jump Date_End                  

                else:
                    call KittyFace("smile", 1)
                    ch_k "That was nice, text you later!"
                    $ Count = 0
                    call Kitty_Date_Over(0)
                    jump Date_End
                    
            "Want to have a little fun first?" if bg_current == "bg player":
                if ApprovalCheck("Kitty", 800, Bonus=(10*Count)):
                    call KittyFace("sexy", 1)
                    ch_k "Heh, I guess so. . ."
                    call Date_Sex_Break("Kitty",Count2)
                    if _return == 4:
                        ch_p "You should probably get going, sorry."  
                        call Kitty_Date_Over(0)
                        jump Date_End  
            "Could I come in for a bit?" if bg_current != "bg player":
                if ApprovalCheck("Kitty", 800, Bonus=(10*Count)):
                    call KittyFace("sexy", 1)
                    ch_k "Heh, I guess so. . ."
                    call Date_Sex_Break("Kitty",Count2)
                    if _return == 4:
                        ch_p "I should probably get going, sorry."  
                        call Kitty_Date_Over(0)
                        jump Date_End                   
                    
            "Ok, good night then.":
                call KittyFace("confused", 1)
                if bg_current == "bg player":
                        "Kitty looks a little confused, but she heads out."
                else:
                        "Kitty looks a little confused, but you head out."
                call Kitty_Date_Over(0)
                jump Date_End
                
    # Kitty lets you into her room:
    if bg_current != "bg player":
            $ bg_current = "bg kitty"  
    call Set_The_Scene(Dress=0)
    call Taboo_Level 
    call KittyFace("sexy", 1)
    ch_k "So[K_like]here we are. . . "
    $ P_DailyActions.append("post date") 
    $ renpy.pop_call() #removes call to date
    $ renpy.pop_call() #removes call to Events
    call Kitty_SexMenu                       # You have what sex you can get away with
    
    if "angry" in K_RecentActions:       
        if bg_current == "bg player":  
                "Kitty storms off through the nearest wall."
        else:
                "Kitty shoves you out into the hall. You head back to your room."
                $ bg_current = "bg player"
        $ Count = 0
        call Remove_Girl("All",0,1)
        $ P_DailyActions.append("post date") 
        jump Player_Room
             
    call Sleepover("Kitty")      
    jump Misplaced

# End Kitty Date End / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    

    
    
# Start Kitty Date Over / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Kitty_Date_Over(Angry=1):
    # Called if Kitty is pissed and leaves
    if Angry:
            $ K_RecentActions.append("angry") 
            $ K_DailyActions.append("angry")  
            call KittyFace("angry")
            ch_k "You know what?" 
            ch_k "[Playername]'s a Jerk!" 
            "Kitty storms out." 
    if "study" in P_RecentActions:        
            call Remove_Girl("Kitty")
            return
    if Party[0] == "Kitty":
            $ Prime_Bonus = Second_Bonus
            $ Prime_Cost = Second_Cost
            $ Second_Cost = 0    
    $ Party.remove("Kitty")
    $ Party.append(0)    
    call Remove_Girl("Kitty")
    call Shift_Focus(Party[0])        
    return
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
