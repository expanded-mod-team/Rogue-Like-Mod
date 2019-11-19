# Date Night //////////////////////////////////////////////////////////////////////
# Count = price of things
# Count2 = tempmod
    
label Rogue_Date_Ask:
    #From the chat menu, you ask Rogue to meet you
    call Shift_Focus("Rogue")
    if "yesdate" in R_DailyActions:  
        call RogueFace("bemused")
        ch_r "Come on, I already said \"yes.\""  
        return         
    if "askeddate" in R_DailyActions:  
        call RogueFace("angry")
        ch_r "I think you got your answer already."  
        return 
    if "stoodup" in R_Traits:  
        call Rogue_Date_Stood_Up
        $ R_DailyActions.append("askeddate")    
        return 
    $ R_RecentActions.append("askeddate")   
    $ R_DailyActions.append("askeddate")   
    
    if R_Break[0] and "ex" in R_Traits:
        call RogueFace("angry")
        ch_r "Seriously? You're asking me that after what you just did?" 
        return     
    if "ex" in R_Traits:
        if ApprovalCheck("Rogue", 1200):
            call RogueFace("bemused",Brows = "sad" ) 
            ch_r "We had some fun, I guess we could go out, as friends maybe."              
        else:
            call RogueFace("angry",Eyes = "side")
            ch_r "I don't think we really worked out, [R_Petname]." 
            return 
       
    if "stoodup" in R_History or "deadbeat" in R_History: 
        if "stoodup" in R_History:
            call RogueFace("angry",Eyes = "side")                
            ch_r "Don't you be leavin me behind this time."
        if "deadbeat" in R_History:  
            call RogueFace("angry")  
            if "stoodup" in R_History:
                ch_r "And last time, you even made me pay for your broke ass?"          
            else:
                ch_r "Remember last time, when you made me pay for your broke ass?"         
        menu:
            extend ""
            "Sorry about that, I'll take care of it this time.":
                    if ApprovalCheck("Rogue", 650):
                        call RogueFace("sad")
                        ch_r "Ok, [R_Petname], you'd better."
                    else:
                        call RogueFace("angry")
                        ch_r "Yeah, I'aint buy'in that hogwash, [R_Petname]." 
                        return
            "Yeah, so?":
                    if ApprovalCheck("Rogue", 1400):
                        call RogueFace("angry", Mouth = "grimace")
                        ch_r "It's a good thing you're so pretty."
                        call RogueFace("bemused")        
                    elif ApprovalCheck("Rogue", 500, "O"):
                        call RogueFace("surprised")
                        ch_r ". . ."
                        call RogueFace("sad")
                        call Statup("Rogue", "Obed", 80, 3)
                        ch_r "I. . . guess I can give you another shot. . ."
                    elif ApprovalCheck("Rogue", 650):
                        call RogueFace("angry")
                        call Statup("Rogue", "Love", 80, -5)
                        call Statup("Rogue", "Inbt", 60, 2) 
                        ch_r "\"So\" it looks like we won't be going out again."    
                        return 
                    else:
                        call RogueFace("angry")
                        call Statup("Rogue", "Love", 80, -10)
                        call Statup("Rogue", "Obed", 80, -3)
                        call Statup("Rogue", "Inbt", 60, 2) 
                        ch_r "Fuck off."  
                        return             
        call Statup("Rogue", "Obed", 30, 3)
        call Statup("Rogue", "Obed", 80, 2)
    elif ApprovalCheck("Rogue", 650):
        call RogueFace("smile")
        ch_r "Yeah, sounds good. See ya in a bit, [R_Petname]."
    elif ApprovalCheck("Rogue", 400):                
        call RogueFace("angry",Eyes = "side")
        ch_r "I think I'm washing my hair tonight. . ."
        return
    else:
        call RogueFace("angry")
        ch_r "Yeah, you wish."
        return 
    
    $ Count = 0
    #She mostly agreed, do you ask for a double date?
    menu:
        "Good, I'll meet you in the campus square." if bg_current != "bg campus" or Current_Time != "Evening": 
                    call RogueFace("smile")
        "Good, let's get going then." if bg_current == "bg campus" and Current_Time == "Evening": 
                    call RogueFace("smile")
        "And I was thinking of asking. . .": 
                    menu:
                        ch_p "And I was thinking of asking. . ."
                        "Kitty along too." if "yesdate" in K_DailyActions or "yesdate" not in P_DailyActions:
                                    $ Count = R_LikeKitty
                        "Emma along too." if "yesdate" in E_DailyActions or "yesdate" not in P_DailyActions:
                                    $ Count = R_LikeEmma
                        "Laura along too." if "yesdate" in L_DailyActions or "yesdate" not in P_DailyActions:
                                    $ Count = R_LikeLaura
                        "Never mind, probably a bad idea.":  
                                    call RogueFace("confused")
                                    ch_r "Okay. . ."
                                    if bg_current != "bg campus": 
                                            ch_p "I'll meet you in the campus square then."
    if Count:
        #If you asked about another girl. . .
        if Count >= 600 and ApprovalCheck("Rogue", 800, "OI"): #Count is "R_LikeX"
            call RogueFace("smile")
            ch_r "Oh, yeah, sounds good."                                
        elif Count >= 750:
            call RogueFace("bemused")
            ch_r "Oh, nice. . ."                                
        elif ApprovalCheck("Rogue", 1300, "LO"): 
            call RogueFace("sad")
            ch_r "If that's what you're into. . ."             
        else:
            call RogueFace("angry")
            ch_r "Keep tryin, polecat."  
            $ Count = 0
            return
        $ R_DailyActions.append("yesdouble") 
        if bg_current != "bg campus": 
                ch_p "I'll meet you in the campus square then." 
        $ Count = 0
    
    if bg_current != "bg campus" or Current_Time != "Evening": 
            ch_r "Yeah, see you then!"
    $ R_DailyActions.append("yesdate")                  
    $ P_DailyActions.append("yesdate") 
    return


label Rogue_Date_Stood_Up:
    # if "stoodup" in R_Traits    
    if R_Loc != bg_current:
            "Rogue storms into the room." 
            $ R_Loc = bg_current
            call Display_Rogue
    else:
            "Rogue turns to you." 
    call RogueFace("confused")
    call Statup("Rogue", "Love", 80, -10)
    ch_r "What're you thinkin not showin up for our date?"
    if "stoodup" in R_History:
        call RogueFace("angry")
        call Statup("Rogue", "Love", 80, -5)
        ch_r "Again!"
    menu:
            extend ""
            "Oh, sorry about that, slipped my mind.":
                if ApprovalCheck("Rogue", 800, "LO") or ApprovalCheck("Rogue", 1200):
                        call RogueFace("angry")
                        call Statup("Rogue", "Love", 80, 5)
                        ch_r "Well, 'least you own up ta your mistakes."
                        if "stoodup" in R_History:
                            call RogueFace("sad",Eyes="side")
                            call Statup("Rogue", "Obed", 80, 5)
                            ch_r "You need ta shape up."   
                elif "stoodup" in R_History:
                        call RogueFace("sad",Eyes="side")
                        call Statup("Rogue", "Love", 80, -5)
                        call Statup("Rogue", "Obed", 80, 5)
                        ch_r "You need ta shape up!"                    
                else:
                        call RogueFace("angry")
                        call Statup("Rogue", "Obed", 80, -2)
                        call Statup("Rogue", "Inbt", 60, 2) 
                        ch_r "\"Sorry\" ain't gonna cut it next time."
                
            "I can't imagine that happening, maybe you got the date wrong?":
                if "stoodup" in R_History and ApprovalCheck("Rogue", 800, "O"):                            
                        call RogueFace("confused")
                        call Statup("Rogue", "Obed", 90, 15)
                        ch_r "What? . . No, we definitely. . ."                            
                        call RogueFace("confused",Eyes="side")
                        ch_r "Hm."                                
                elif ApprovalCheck("Rogue", 700, "O"):
                        call RogueFace("angry")
                        call Statup("Rogue", "Obed", 80, 5)
                        call Statup("Rogue", "Obed", 90, 10)
                        ch_r "No. . . we definitely. . ."     
                elif ApprovalCheck("Rogue", 500, "I"):
                        call RogueFace("angry")
                        $ R_RecentActions.append("angry") 
                        $ R_DailyActions.append("angry")  
                        call Statup("Rogue", "Love", 80, -10)
                        call Statup("Rogue", "Inbt", 70, 10) 
                        ch_r "Don't you try and twist that around on me!"
                else:
                        call RogueFace("sad",Eyes="side")
                        $ R_RecentActions.append("angry") 
                        $ R_DailyActions.append("angry")  
                        call Statup("Rogue", "Love", 80, -5)
                        call Statup("Rogue", "Obed", 80, -5)
                        call Statup("Rogue", "Inbt", 60, 5) 
                        ch_r "Doubt it, maybe think about a better apology."
                        
            "Yeah, I found something better to do.": 
                if ApprovalCheck("Rogue", 1200, "LO"):
                        call RogueFace("sad",Eyes="side")
                        call Statup("Rogue", "Love", 80, -5)
                        call Statup("Rogue", "Obed", 80, 5)
                        if "stoodup" in R_History:
                                ch_r "Oh. . . "
                                ch_r "Well, I guess you have your way. . ."                            
                        else:
                                call Statup("Rogue", "Obed", 80, 10)
                                ch_r "Oh. . . "
                                ch_r "just, don't do it again."
                elif ApprovalCheck("Rogue", 800, "LO"):
                        call RogueFace("angry",Eyes="side")
                        call Statup("Rogue", "Love", 80, -10)
                        call Statup("Rogue", "Obed", 80, 20) 
                        ch_r "You can do better than that."
                else:
                        call RogueFace("angry")
                        call Statup("Rogue", "Love", 80, -15)
                        call Statup("Rogue", "Inbt", 60, 5) 
                        ch_r "Oh, fuck off."
                        $ R_RecentActions.append("angry") 
                        $ R_DailyActions.append("angry")  
                        
    $ R_Traits.remove("stoodup") 
    if "stoodup" not in R_History:  
            $ R_History.append("stoodup") 
    
    call CleartheRoom("All",Check=1)
    if _return >= 3:            #fix, maybe reduce this to 2 if CtR is sending returns back properly
        #if the room is full,
        call Remove_Girl("Rogue")
        "Rogue wanders off."        
    return
    
# End Rogue Ask / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Rogue_Date_Prep:
    #This gets Rogue Dressed and ready for Dinner, called by Date_Night
    $ Taboo = 40
    if R_Schedule[7]:
        # if she has a date outfit set
        if R_Schedule[7] == 2:
            $ R_Outfit = "evo_pink"
        elif R_Schedule[7] == 3:
            $ R_Outfit = "custom1"
        elif R_Schedule[7] == 4:
            $ R_Outfit = "gym"
        elif R_Schedule[7] == 5:
            $ R_Outfit = "custom2"
        elif R_Schedule[7] == 6:
            $ R_Outfit = "custom3"
        else:
            $ R_Outfit = "evo_green"
    else:
        $ Options = ["evo_pink", "evo_green"]
        $ Options.append("custom1") if R_Custom[0] == 2 else Options
        $ Options.append("custom2") if R_Custom2[0] == 2 else Options
        $ Options.append("custom3") if R_Custom3[0] == 2 else Options
        $ renpy.random.shuffle(Options) 
        $ R_Outfit = Options[0]
        $ del Options[:]  
    $ R_Loc = "date"
    call RogueOutfit(Changed=1)
    call RogueFace("smile")
    return

# End Rogue Prep / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Rogue Dinner Menu/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /       
label Rogue_Dinner(R_Cost=0):
    #Called by Date Dinner, picked Rogue's food
    menu:
        "For Rogue you order. . ."
        "Surf and turf. ($20)":
                call RogueFace("smile", Brows = "surprised")
                ch_r "Ooh, you're really pulling out the stops here."  
                call RogueFace
                call Statup("Rogue", "Love", 80, 5)
                call Statup("Rogue", "Love", 200, 2)
                $ R_Cost = 20
                $ R_RecentActions.append("surfturf")
        "Steak. ($15)":  
                call RogueFace("smile")
                ch_r "I love a big, juicy steak."
                call Statup("Rogue", "Love", 80, 5)
                $ R_Cost = 15
                $ R_RecentActions.append("ribeye")
        "Chicken. ($10)":
                call RogueFace("smile")
                ch_r "I could always go for some chicken."
                call Statup("Rogue", "Love", 50, 1)
                call Statup("Rogue", "Love", 80, 3)
                $ R_Cost = 10
                $ R_RecentActions.append("chicken")
        "Just a salad. ($5)":
                $ R_Mouth = "sad"
                $ R_Eyes = "sexy"
                $ R_Brows = "confused"            
                ch_r "Well, I guess salad isn't that bad. . ."  
                call Statup("Rogue", "Love", 60, -5)
                call Statup("Rogue", "Obed", 50, 2)
                $ R_Cost = 5
                $ R_RecentActions.append("salad")
        "Why don't you choose, Rogue?":
                call Date_Bonus("Rogue",2)
                call RogueFace("smile")
                ch_r "Well thanks, [R_Petname]. I think I'll have the chicken."            
                call Statup("Rogue", "Love", 80, 5)        
                call Statup("Rogue", "Inbt", 50, 3)
                call Statup("Rogue", "Obed", 50, -2)
                $ R_Cost = 10
                $ R_RecentActions.append("chicken")
                
    if Party[0] == "Rogue":
        $ Prime_Cost = R_Cost
    else:
        $ Second_Cost = R_Cost
    call Date_Bonus("Rogue",R_Cost)
    return
# End Rogue Menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /          

    
# Start Rogue Dinner Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Rogue_Dinner_Sex(Previous=0,R_Bonus=0,Options=["nothing"]):
    #Called by Dinner Sex, if Rogue is chosen.
    
    if Party[0] == "Rogue":
        $ R_Bonus = Prime_Bonus + Prime_Cost
    else:
        $ R_Bonus = Second_Bonus + Second_Cost
        
    if R_Anal and ApprovalCheck("Rogue", 1500) and R_Bonus >=15: 
        $ Options.append("anal")        
    if R_Sex and ApprovalCheck("Rogue", 1500) and R_Bonus >=10:
        $ Options.append("sex")
    if R_Blow and ApprovalCheck("Rogue", 1300) and R_Bonus >=10:
        $ Options.append("blow")      
    if R_Hand and ApprovalCheck("Rogue", 1000) and R_Bonus >=10:
        $ Options.append("hand")
    if R_FondleP and ApprovalCheck("Rogue", 1000) and R_Bonus >=10:
        $ Options.append("pussy")
    if ApprovalCheck("Rogue", 1000) and R_Bonus >=10:
        $ Options.append("foot")
    
    if "Kitty" in Previous:
        $ Previous = "Kitty"
    elif "Emma" in Previous:
        $ Previous = "Emma"
    elif "Laura" in Previous:
        $ Previous = "Laura"
    else:
        $ Previous = 0
        
    $ renpy.random.shuffle(Options) 
    
    call RogueFace("sexy")
    if Options[0] == "nothing":
        pass
    elif Options[0] == "anal":        
        "Halfway through the meal, Rogue gets a sly look on her face." 
        "She nods her head suggestively towards the restrooms, and then excuses herself."
        call Date_Sex_Break("Rogue",Previous)
        if _return == 4: #you refused
                call RogueFace("sadside", 2)
                "You wait a few minutes until she returns, seemingly a bit annoyed at you."
                call Statup("Rogue", "Love", 90, -5)
                call Statup("Rogue", "Inbt", 80, -10)
                call Date_Bonus("Rogue",-5)
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
                ch_r "I hope I'll still be able to sit down later."  
                call Statup("Rogue", "Inbt", 50, 9)
                call Statup("Rogue", "Inbt", 80, 3)
                $ R_SeenPeen += 1
                $ R_Anal += 1
                $ P_Semen -= 1
                $ R_RecentActions.append("anal")    
                $ R_RecentActions.append("dinnersex")                    
                $ R_DailyActions.append("anal") 
    elif Options[0] == "sex":        
        "Halfway through the meal, Rogue gets a sly look on her face." 
        "She nods her head suggestively towards the restrooms, and then excuses herself."
        call Date_Sex_Break("Rogue",Previous)
        if _return == 4: #you refused
                call RogueFace("sadside", 2)
                "You wait a few minutes until she returns, seemingly a bit annoyed at you."
                call Statup("Rogue", "Love", 90, -5)
                call Statup("Rogue", "Inbt", 80, -10)
                call Date_Bonus("Rogue",-5)
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
                ch_r "I needed to work off that meal a bit."
                call Statup("Rogue", "Inbt", 50, 8)
                call Statup("Rogue", "Inbt", 80, 2)
                $ R_SeenPeen += 1
                $ R_Sex += 1
                $ P_Semen -= 1            
                $ R_RecentActions.append("sex")   
                $ R_RecentActions.append("dinnersex")                    
                $ R_DailyActions.append("sex") 
    elif Options[0] == "blow":
        "Halfway through the meal, Rogue gets a sly look on her face, then knocks her fork off the table."
        "She ducks under the table after it, and unzips your pants." 
        call Date_Sex_Break("Rogue",Previous)
        if _return == 4: #you refused
                call RogueFace("sadside", 2)
                "You zip them back up and shoo her away. She gets back up from under the table."
                call Statup("Rogue", "Love", 90, -5)
                call Statup("Rogue", "Inbt", 80, -5)
                call Date_Bonus("Rogue",-3)
        else:
                if _return == 1: #other girl is fine
                        "[Previous] shifts closer and wraps one arm around you, the other hand caressing Rogue's cheek."
                        "Rogue then procedes to blow you for several minutes until you cum."
                elif _return == 2: #other girl is fine
                        "She then procedes to blow you for several minutes until you cum, while [Previous] pretends to be occupied."
                else: 
                        "She then procedes to blow you for several minutes until you cum."
                call Statup("Rogue", "Inbt", 50, 6)
                call Statup("Rogue", "Inbt", 80, 2)
                $ R_RecentActions.append("blow")   
                $ R_RecentActions.append("dinnersex")                    
                $ R_DailyActions.append("blow") 
                if R_Swallow:
                    "Rogue wipes her mouth as she climbs out from under the table."
                    ch_r "I don't think we need desert, [R_Petname]."          
                    $ R_Addict -= 20
                    $ R_Swallow += 1  
                    $ R_RecentActions.append("swallow")                      
                    $ R_DailyActions.append("swallow")       
                else:
                    "Rogue grabs the napkin off your lap and uses it to collect the jiz."
                    ch_r "I bet the cleaning crew will enjoy that."
                call Statup("Rogue", "Inbt", 30, 4)
                call Statup("Rogue", "Inbt", 80, 2)
                $ R_SeenPeen += 1
                $ R_Blow += 1
                $ P_Semen -= 1
                if _return == 3:
                    "[Previous] stares daggers at you both as she crawls out from under the table."  
                    call Date_Bonus(Previous,-10)
    elif Options[0] == "hand":
        "Halfway through the meal, Rogue gets a sly look on her face, then shifts her chair around next to yours."
        call Date_Sex_Break("Rogue",Previous)
        if _return == 4: #you refused
                call RogueFace("sadside", 2)
                "She tries to unzip your pants under the table, but you shoo her away."
                call Statup("Rogue", "Love", 90, -5)
                call Statup("Rogue", "Inbt", 80, -5)
                call Date_Bonus("Rogue",-2)
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
                ch_r "I bet the cleaning crew will enjoy that."
                call Statup("Rogue", "Inbt", 30, 4)
                call Statup("Rogue", "Inbt", 80, 2)
                $ R_Hand += 1
                $ P_Semen -= 1
                $ R_RecentActions.append("hand")     
                $ R_RecentActions.append("dinnersex")                  
                $ R_DailyActions.append("hand") 
                if _return == 3:
                    "[Previous] stares daggers at you both from across the table."
                    call Date_Bonus(Previous,-5)
    elif Options[0] == "pussy":
        "Halfway through the meal, Rogue gets a sly look on her face, then shifts her chair around next to yours."
        call Date_Sex_Break("Rogue",Previous)
        if _return == 4: #you refused
                if R_Legs:
                    "She takes your hand and pulls it over to her crotch, shoving it under her [R_Legs]."
                else:
                    "She takes your hand and shoves it into her crotch."
                call RogueFace("sadside", 2)
                "With a glance at [Previous], you jerk your hand away."
                call Statup("Rogue", "Love", 90, -5)
                call Statup("Rogue", "Inbt", 80, -5)
                call Date_Bonus("Rogue",-3)
        else:
                if R_Legs:
                    "She takes your hand and pulls it over to her crotch, shoving it under her [R_Legs]."
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
                ch_r "I needed to take a bit of the edge off, [R_Petname]."
                if _return == 1:
                    ch_r "Thanks to you too, [Previous]."
                    $ R_Les += 1
                call Statup("Rogue", "Love", 90, 3)
                call Statup("Rogue", "Inbt", 30, 5)            
                call Statup("Rogue", "Inbt", 90, 2)
                $ R_FondleP += 1
                $ R_Org += 1
                $ R_RecentActions.append("fondle pussy") 
                $ R_RecentActions.append("dinnersex")                      
                $ R_DailyActions.append("fondle pussy") 
    elif Options[0] == "foot":
        "Halfway through the meal, Rogue gets a sly look on her face, then shifts a bit lower in her seat."
        "You suddenly feel her foot in your lap, gently caressing your cock."
        call Date_Sex_Break("Rogue",Previous)
        if _return == 4: #you refused
                call RogueFace("sadside", 2)
                "You shift uncomfortably and push her foot away."
                call Statup("Rogue", "Love", 90, -5)
                call Statup("Rogue", "Inbt", 80, -3)
                call Date_Bonus("Rogue",-1)
        else:
                call Statup("Player", "Focus", 60, 10)
                if _return == 1: #other girl is fine
                        "[Previous] decides to join in the fun and adds her foot to the mix."
                        call Statup("Player", "Focus", 60, 5)
                if _return == 3:
                    call Date_Bonus(Previous,-3)
                "After several minutes of this, she pulls back."
                ch_r "Just a little downpayment on later, [R_Petname]."
                call Statup("Rogue", "Inbt", 80, 3)
                $ R_RecentActions.append("dinnersex") 
    
    call RogueFace(B = 0)
    return    
# End Rogue Dinner Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    

    
    
# Start Rogue Movie Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Rogue_Movie_Sex(Previous=0,R_Bonus=0, Options=["nothing"]):
    # Called by Movie_Sex if Rogue is chosen
    if Party[0] == "Rogue":
        $ R_Bonus = Prime_Bonus
    else:
        $ R_Bonus = Second_Bonus
    
    if "horror" in P_RecentActions:
        $ R_Bonus += 20
    
    if "Kitty" in Previous:
        $ Previous = "Kitty"
    elif "Emma" in Previous:
        $ Previous = "Emma"
    elif "Laura" in Previous:
        $ Previous = "Laura"
    else:
        $ Previous = 0
        
    if ApprovalCheck("Rogue", 500, Bonus=(10*R_Bonus)):
        call RogueFace("kiss", 1)
        if "romcom" in P_RecentActions: 
            "Halfway through the movie, inspired by the action on screen, Rogue turns to you and starts to make out with you."
        elif "action" in P_RecentActions:        
            "Halfway through the movie, adrenaline pumping from the action on screen, Rogue turns to you and starts to make out with you."
        elif "horror" in P_RecentActions:  
            "Halfway through the movie, freaked out by the tension on screen, Rogue huddles in your arms, and then starts to make out with you."
        elif "drama" in P_RecentActions:   
            "Halfway through the movie, profoundly bored by the movie, Rogue turns to you with a shrug and starts to make out with you."
        $ R_RecentActions.append("kissing") 
        $ R_RecentActions.append("moviesex")                       
        $ R_DailyActions.append("kissing")      
        call Date_Sex_Break("Rogue",Previous)   
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
            
    
        if R_Anal and ApprovalCheck("Rogue", 2000, Bonus=(10*R_Bonus)) and PantsNum("Rogue") < 5:
                    call RogueFace("sexy", 1)
                    if R_Panties:
                        "As you make out, Rogue reaches down and undoes your fly. She pulls her panties aside and shifts into your lap."
                    else:
                        "As you make out, Rogue reaches down and undoes your fly. She hikes her skirt up a bit and shifts into your lap."
                    call Date_Sex_Break("Rogue",Previous,1)
                    if _return == 3:
                            #the other girl stormed out. . .
                            ch_r "Sorry about that."                      
                    "She gingerly squeezes your cock into her ass and begins to grind up and down, quietly enough that the other patrons don't seem to notice."
                    if _return == 1:
                            #the other girl joins you. . .
                            "[Previous] also leans over and toys with Rogue's pussy."
                    if R_CreamA:
                            if R_Panties:
                                "After several minutes of this, you can't take it anymore and come inside her."
                                "She pulls her panties back up and returns to her seat."
                            else:
                                "After several minutes of this, you can't take it anymore and come inside her."
                                "She wipes off as best she can and shifts back into her seat."
                            $ R_CreamA += 1
                            $ R_RecentActions.append("creampie anal")                      
                            $ R_DailyActions.append("creampie anal") 
                    else:
                            "After several minutes of this, she pulls out and shifts back into her seat, finishing you off with her hand."
                            if R_Swallow:
                                if 0 < _return < 3: #if 1 or 2
                                    "You cum into the popcorn bucket, which she and [Previous] then finish off together."
                                else:
                                    "You cum into the popcorn bucket, which she then finishes off."
                                $ R_Addict -= 20
                                $ R_Swallow += 1
                                $ R_Spunk.append("mouth")                          
                                $ R_RecentActions.append("swallowed")                      
                                $ R_DailyActions.append("swallowed") 
                            else:
                                "You cum into the popcorn bucket, which she sets in the seat next to her."
                    ch_r "This makes for a better ride than a movie."
                    call Statup("Rogue", "Inbt", 50, 4)
                    call Statup("Rogue", "Inbt", 90, 3)
                    $ R_SeenPeen += 1
                    $ R_Anal += 1
                    $ P_Semen -= 1
                    $ R_RecentActions.append("anal")                      
                    $ R_DailyActions.append("anal")  
        elif R_Sex and ApprovalCheck("Rogue", 2000, Bonus=(10*R_Bonus)) and PantsNum("Rogue") < 5:
                    call RogueFace("sexy", 1)
                    if R_Panties:
                        "As you make out, Rogue reaches down and undoes your fly. She pulls her panties aside and shifts into your lap."
                    else:
                        "As you make out, Rogue reaches down and undoes your fly. She hikes her skirt up a bit and shifts into your lap."
                    call Date_Sex_Break("Rogue",Previous,1)                    
                    if _return == 3:
                            #the other girl stormed out. . .
                            ch_r "Sorry about that."                
                    "Seconds later, she's slowly rocking on your cock, quietly enough that the other patrons don't seem to notice."
                    if _return == 1:
                            #the other girl joins you. . .
                            "[Previous] also leans over and toys with Rogue's pussy."
                    if R_CreamP:
                        if R_Panties:
                            "After several minutes of this, you can't take it anymore and come inside her."
                            "She pulls her panties up over her dripping slit and returns to her seat."
                        else:
                            "After several minutes of this, you can't take it anymore and come inside her."
                            "She wipes up as best she can and returns to her seat."
                        $ R_CreamP += 1
                        $ R_RecentActions.append("creampie sex")                      
                        $ R_DailyActions.append("creampie sex") 
                    else:
                        "After several minutes of this, she pulls out and shifts back into her seat, finishing you off with her hand."
                        if R_Swallow:
                                if 0 < _return < 3: #if 1 or 2
                                    "You cum into the popcorn bucket, which she and [Previous] then finish off together."
                                else:                                    
                                    "You cum into the popcorn bucket, which she then finishes off."   
                                $ R_Spunk.append("mouth")   
                                $ R_Addict -= 20
                                $ R_Swallow += 1
                                $ R_RecentActions.append("swallowed")                      
                                $ R_DailyActions.append("swallowed") 
                        else:
                                "You cum into the popcorn bucket, which she sets in the seat next to her."
                    ch_r "This makes for a better ride than a movie."
                    call Statup("Rogue", "Inbt", 50, 4)
                    call Statup("Rogue", "Inbt", 90, 3)
                    $ R_SeenPeen += 1
                    $ R_Sex += 1
                    $ P_Semen -= 1
                    $ R_RecentActions.append("sex")                      
                    $ R_DailyActions.append("sex")             
        elif R_Blow and ApprovalCheck("Rogue", 1300, Bonus=(10*R_Bonus)):
                    call RogueFace("sucking", 1)
                    "As you make out, Rogue reaches down and undoes your fly. She then bends down and wraps her lips around it."
                    call Date_Sex_Break("Rogue",Previous,1)                
                    if _return == 3:
                            #the other girl stormed out. . .
                            ch_r "Sorry about that."                      
                    if _return == 1:
                            #the other girl joins you. . .
                            "[Previous] also leans over joins Rogue at licking your cock."
                            "They take turns sucking on it contentedly for several minutes before you finally cum."   
                    else:
                            "She sucks on it contentedly for several minutes before you finally cum."            
                    $ R_Spunk.append("mouth")  
                    if R_Swallow:
                        "Rogue wipes her mouth as she shifts back into her seat and washes it down with some soda."
                        call RogueFace("sexy")
                        ch_r "Mmmm, refreshing. . ."
                        $ R_Addict -= 20
                        $ R_Swallow += 1
                        $ R_RecentActions.append("swallowed")                      
                        $ R_DailyActions.append("swallowed") 
                    else:
                        "You cum into the popcorn bucket, which she sets in the seat next to her."
                        ch_r "I bet the cleaning crew will enjoy that."
                    call Statup("Rogue", "Inbt", 40, 3)
                    call Statup("Rogue", "Inbt", 80, 2)
                    $ R_SeenPeen += 1
                    $ R_Blow += 1
                    $ P_Semen -= 1
                    $ R_RecentActions.append("blow")                      
                    $ R_DailyActions.append("blow") 
        elif R_Hand and ApprovalCheck("Rogue", 1000, Bonus=(10*Count2)):
                    call RogueFace("sexy")
                    "As you make out, Rogue reaches down and pulls out your cock." 
                    call Date_Sex_Break("Rogue",Previous,1)             
                    if _return == 3:
                            #the other girl stormed out. . .
                            ch_r "Sorry about that."          
                            "She then leans over and begins to stroke your cock." 
                    elif _return == 1: 
                            #the other girl joins in. . .
                            "She then leans over and begins to stroke your cock."
                            "[Previous] leans in and joins her, and they share a smile."
                    else:
                            "She then leans over and begins to stroke it." 
                    call RogueFace("surprised")
                    if R_FondleP:
                        if _return == 1: 
                                #the other girl joins in. . .
                                "You also reach down and begin stroking their pussies."
                        else:
                            if R_Legs:
                                    "You also lean over, reach into her [R_Legs], and begin to stroke her pussy."
                            elif R_Hose:
                                    "You also lean in, reach under her [R_Hose], and begin to stroke her pussy."
                            elif R_Panties:
                                    "You also lean in, reach under her panties, and begin to stroke her pussy."
                            else:
                                    "You also lean over, notice she isn't wearing anything down there, and begin to stroke her pussy."
                    call RogueFace("sexy", 1, Eyes = "closed")
                    if R_FondleP:
                        if _return == 1: 
                            "After several minutes of this, Rogue and [Previous] shudder in orgasm, which sets you off as well."
                        else:
                            "After several minutes of this, she shudders in orgasm, which sets you off as well."
                        "Rogue catches the jiz in the popcorn bucket."
                    $ R_Eyes = "sexy"
                    if R_Swallow:
                            if 0 < _return < 3: #if 1 or 2
                                "The girls finish off the remaining popcorn with a grin."    
                            else:
                                "She finishes off the remaining popcorn with a grin."                    
                            $ R_Spunk.append("mouth")  
                            ch_r "Best topping they got here, [R_Petname]."     
                            $ R_Addict -= 20
                            $ R_Swallow += 1
                            $ R_RecentActions.append("swallowed")                      
                            $ R_DailyActions.append("swallowed") 
                    else:
                            "You cum into the popcorn bucket, which she sets in the seat next to her."
                            ch_r "I bet the cleaning crew will enjoy that."
                    call Statup("Rogue", "Love", 90, 2)
                    call Statup("Rogue", "Inbt", 40, 3)
                    call Statup("Rogue", "Inbt", 80, 2)
                    $ R_FondleP += 1
                    $ R_Org += 1        
                    $ R_Hand += 1
                    $ P_Semen -= 1
                    $ R_RecentActions.append("hand")                      
                    $ R_DailyActions.append("hand") 
        elif R_FondleP and ApprovalCheck("Rogue", 900, Bonus=(10*R_Bonus)):
                    call RogueFace("sexy")                    
                    if R_Legs:
                            "As you make out, Rogue grabs your hand and shoves it down her [R_Legs]."
                    elif R_Hose:
                            "As you make out, Rogue grabs your hand and shoves it down her [R_Hose]."
                    elif R_Panties:
                            "As you make out, Rogue grabs your hand and shoves it down her panties."
                    else:
                            "As you make out, Rogue grabs your hand and shoves it between her legs."
                    call Date_Sex_Break("Rogue",Previous,1)
                    $ R_Eyes = "closed"
                    if _return == 3:
                            #the other girl stormed out. . .
                            ch_r "Sorry about that."          
                            "You get back to work."
                    elif _return == 1: 
                            #the other girl joins in. . .
                            "[Previous] leans in and begins to fondle her breasts as well."   
                    "After several minutes of this, she shudders in orgasm and leans back with a contented sigh."
                    $ R_Eyes = "sexy"
                    ch_r "Thanks [R_Petname]. I needed that. . . distraction."
                    call Statup("Rogue", "Love", 90, 2)
                    call Statup("Rogue", "Inbt", 40, 2)
                    call Statup("Rogue", "Inbt", 80, 2)
                    $ R_FondleP += 1
                    $ R_Org += 1    
                    $ R_RecentActions.append("fondle pussy")                      
                    $ R_DailyActions.append("fondle pussy") 
        elif ApprovalCheck("Rogue", 1200, Bonus=(5*R_Bonus)) and R_Panties:
                    call RogueFace("sexy")
                    "After making out for a few minutes, Rogue gets a sly look on her face and reaches into her pocket."
                    "After a second, she hands you a cloth lump, apparently her panties." 
                    $ R_DailyActions.append("pantyless") 
                    call Statup("Rogue", "Inbt", 60, 2)
                    $ R_Panties = 0
                    ch_r "Just a little downpayment on later, [R_Petname]."
        elif ApprovalCheck("Rogue", 1200, Bonus=(5*R_Bonus)):
                    call RogueFace("sexy")
                    "After making out for a few minutes, Rogue gets a sly look on her face, then shifts a bit lower in her seat."
                    if PantsNum("Rogue") > 5:
                        "Looking down, you notice she's pulled down her pants enough that you can see her bare pussy, lit by the movie screen."  
                    elif R_Legs == "shorts":
                        "Looking down, you notice she's pulled down her shorts enough that you can see her bare pussy, lit by the movie screen."   
                    else:
                        "Looking down, you notice she's hiked up her skirt enough that you can see her bare pussy, lit by the movie screen."            
                    call Statup("Rogue", "Inbt", 60, 2)
                    call Rogue_First_Bottomless(1)
                    ch_r "Just a little downpayment on later, [R_Petname]."
    #End Rogue movie sex options
    call RogueOutfit(Changed=0)
    return
# End Rogue Movie Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    

    
# Start Rogue Date End/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label R_Date_End:   
    #Called if you end up with Rogue at the end of the date
    if bg_current != "bg player":  
            #skips this portion if you are in the player's room already
            menu:
                "Take Rogue back to her room?":
                    pass
                "Just leave and head back to yours.":
                    call Date_Ditched
                    jump Date_Over    
                    
            $ bg_current = "bg rogue"
            $ R_Loc = "bg rogue"
            if "Kitty" in Party:
                $ K_Loc = "bg rogue"
            if "Emma" in Party:
                $ E_Loc = "bg rogue"
            if "Laura" in Party:
                $ L_Loc = "bg rogue"
            call Set_The_Scene(Dress=0)
            call Taboo_Level    
    
    if Party[0] == "Rogue":
        #sets the bonus stats based on your performance during the date.
        $ Count = Prime_Bonus
        $ Count2 = Party[1] #the other girl
    else:
        $ Count = Second_Bonus
        $ Count2 = Party[0] #the other girl
        
    if bg_current != "bg player":    
        "You walk Rogue back to her room."
    if Count < 0:      
        call RogueFace("angry", 0,Eyes = "side")
        ch_r "Well that was a waste of an evening. I'll see you around, [Playername]."
        if bg_current == "bg player":
                "She storms off down the hall."
        else:
                "She slams the door on you."
        call Set_The_Scene(Entry=1,Dress=0)
        $ Count = 0
        call Rogue_Date_Over(0)
        jump Date_End
    else: 
        if Count > 20:
            call RogueFace("sexy", 1)
            ch_r "Well that was a lot of fun, [R_Petname]. I don't want the night to end . . ."           
        else:
            call RogueFace("smile", 1)
            ch_r "Well that was a lot of fun, [R_Petname]. We'll have to do it again."
        
        $ R_Date += 1
        menu:
            extend ""
            "Could I get a good night kiss?":
                if ApprovalCheck("Rogue", 600, Bonus=(10*Count)):
                    $ R_Mouth = "smile"
                    ch_r "Ok, [R_Petname]. I suppose you've earned it."
                    call Date_Sex_Break("Rogue",Count2,2)
                    $ MultiAction = 0
                    call R_KissPrep 
                    $ MultiAction = 1
                if ApprovalCheck("Rogue", 900, Bonus=(10*Count)):
                    call RogueFace("sexy", 1)
                    if bg_current == "bg player":
                            ch_r "That was real nice, how about I come inside for a minute. . ."  
                    else:
                            ch_r "That was real nice, how about you come inside for a minute. . ." 
                    call Date_Sex_Break("Rogue",Count2)
                    if _return == 4:
                        if bg_current == "bg player":
                                ch_p "You should probably get going, sorry."
                        else:
                                ch_p "I should probably get going, sorry."
                        call Rogue_Date_Over(0)
                        jump Date_End                  

                else:
                    call RogueFace("smile", 1)
                    ch_r "That was real nice, I'll see you later, [R_Petname]." 
                    $ Count = 0
                    call Rogue_Date_Over(0)
                    jump Date_End
                    
            "Want to have a little fun first?" if bg_current != "bg player":
                if ApprovalCheck("Rogue", 800, Bonus=(10*Count)):
                    call RogueFace("sexy", 1)
                    ch_r "Alright, [R_Petname]. I think you've earned it."
                    call Date_Sex_Break("Rogue",Count2)
                    if _return == 4:
                        ch_p "I should probably get going, sorry."  
                        call Rogue_Date_Over(0)
                        jump Date_End  
            "Could you come in for a bit?" if bg_current == "bg player":
                if ApprovalCheck("Rogue", 800, Bonus=(10*Count)):
                    call RogueFace("sexy", 1)
                    ch_r "Alright, [R_Petname]. I think you've earned it."
                    call Date_Sex_Break("Rogue",Count2)
                    if _return == 4:
                        ch_p "You should probably get going, sorry."  
                        call Rogue_Date_Over(0)
                        jump Date_End                  
                    
            "Ok, good night then.":
                call RogueFace("confused", 1)
                if bg_current == "bg player":
                        "Rogue looks a little confused, but she heads out."
                else:
                        "Rogue looks a little confused, but you head out."
                call Rogue_Date_Over(0)
                jump Date_End
                
    # Rogue lets you into her room:
    if bg_current != "bg player":
            $ bg_current = "bg rogue"  
    call Set_The_Scene(Dress=0)
    call Taboo_Level 
    call RogueFace("sexy", 1)
    if not Party[1]:
            ch_r "So, [R_Petname], you've got me all alone, what are your intentions? . ."
    else:
            if bg_current == "bg player":
                    ch_r "So, [R_Petname], we're in your room together, what are your intentions? . ."
            else:
                    ch_r "So, [R_Petname], we're in my room together, what are your intentions? . ."
    $ P_DailyActions.append("post date") 
    $ renpy.pop_call() #removes call to date
    $ renpy.pop_call() #removes call to Events
    call Rogue_SexMenu                       # You have what sex you can get away with
    
    if "angry" in R_RecentActions:       
        if bg_current == "bg player":  
                "Rogue storms off down the hall."
        else:
                "Rogue shoves you out into the hall. You head back to your room."
                $ bg_current = "bg player"
        $ Count = 0
        call Remove_Girl("All")
        $ P_DailyActions.append("post date") 
        jump Player_Room
                             
    call Sleepover("Rogue")  
    jump Misplaced

# End Rogue Date End / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    

    
    
# Start Rogue Date Over / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Rogue_Date_Over(Angry=1):
    # Called if Rogue is pissed and leaves
    if Angry:
            $ R_RecentActions.append("angry") 
            $ R_DailyActions.append("angry")  
            call RogueFace("angry")
            ch_r "I think I'm done here, [R_Petname]." 
            "Rogue storms out." 
    if "study" in P_RecentActions:        
            call Remove_Girl("Rogue")
            return
    if Party[0] == "Rogue":
            $ Prime_Bonus = Second_Bonus
            $ Prime_Cost = Second_Cost
            $ Second_Cost = 0    
    $ Party.remove("Rogue")
    $ Party.append(0)    
    call Remove_Girl("Rogue")
    call Shift_Focus(Party[0])      
    return
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
