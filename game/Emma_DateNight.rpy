# Date Night //////////////////////////////////////////////////////////////////////
# Count = price of things
# Count2 = tempmod
    
label Emma_Date_Ask:
    #From the chat menu, you ask Emma to meet you
    call Shift_Focus("Emma")
    if "yesdate" in E_DailyActions:  
        call EmmaFace("bemused")
        ch_e "Learn to take \"yes\" for an answer, [E_Petname]."  
        return         
    if "askeddate" in E_DailyActions:  
        call EmmaFace("angry")
        ch_e "Persistance will not be rewarded, [E_Petname]."  
        return 
    if "stoodup" in E_Traits:  
        call Emma_Date_Stood_Up
        $ E_DailyActions.append("askeddate")    
        return 
    $ E_RecentActions.append("askeddate")   
    $ E_DailyActions.append("askeddate")   
    
      
    if "classcaught" not in E_History:  
        #if you haven't caught her yet
        ch_e "I don't really think it would be appropriate for the two of us to be seen together."
        return
    if "taboo" not in E_History:
        #if she hasn't agreed to go public yet
        call Emma_Taboo_Talk
        if "taboo" not in E_History:
            return
    if E_Break[0] and "ex" in E_Traits:
        call EmmaFace("angry")
        ch_e "I think you have some work to do before you're ready to ask that question." 
        return     
    if "ex" in E_Traits:
        if ApprovalCheck("Emma", 1200):
            call EmmaFace("bemused",Brows = "sad" ) 
            ch_e "You were an entertaining date, I suppose, this once."              
        else:
            call EmmaFace("angry",Eyes = "side")
            ch_e "I don't think we really worked out, [E_Petname]." 
            return 
       
    if "stoodup" in E_History or "deadbeat" in E_History: 
        if "stoodup" in E_History:
            call EmmaFace("angry",Eyes = "side")                
            ch_e "I believe you know better than to leave me waiting again."
        if "deadbeat" in E_History:  
            call EmmaFace("angry")  
            if "stoodup" in E_History:
                ch_e "Nor do I expect to be picking up the check again."          
            else:
                ch_e "I don't I expect to be picking up the check again."         
        menu:
            extend ""
            "Sorry about that, I'll take care of it this time.":
                    if ApprovalCheck("Emma", 650):
                        call EmmaFace("sad")
                        ch_e "I'll take you at your word, [E_Petname]."
                    else:
                        call EmmaFace("angry")
                        ch_e "A likely story." 
                        return
            "Yeah, so?":
                    if ApprovalCheck("Emma", 1500):
                        call EmmaFace("angry", Mouth = "grimace")
                        ch_e "I suppose I can appreciate confidence."
                        call EmmaFace("bemused")     
                        ch_e "Just don't get {i}too{/i} confident."   
                    elif ApprovalCheck("Emma", 700, "O"):
                        call EmmaFace("surprised")
                        ch_e ". . ."
                        call EmmaFace("sad")
                        call Statup("Emma", "Obed", 80, 3)
                        ch_e "Well, I suppose I could join you for a bit. . ."
                    elif ApprovalCheck("Emma", 650):
                        call EmmaFace("angry")
                        call Statup("Emma", "Love", 80, -5)
                        call Statup("Emma", "Inbt", 60, 2) 
                        ch_e "Then I believe you can figure out the answer to your own question."    
                        return 
                    else:
                        call EmmaFace("angry")
                        call Statup("Emma", "Love", 80, -10)
                        call Statup("Emma", "Obed", 80, -3)
                        call Statup("Emma", "Inbt", 60, 2) 
                        ch_e "You don't want to stick around."  
                        return             
        call Statup("Emma", "Obed", 30, 3)
        call Statup("Emma", "Obed", 80, 2)
    elif ApprovalCheck("Emma", 650):
        call EmmaFace("smile")
        ch_e "Sounds lovely, I'll see you later then, [E_Petname]."
    elif ApprovalCheck("Emma", 400):                
        call EmmaFace("angry",Eyes = "side")
        ch_e "I have some papers to take care of tonight. . ."
        return
    else:
        call EmmaFace("angry")
        ch_e "I can't imagine why I would."
        return 
    
    $ Count = 0
    #She mostly agreed, do you ask for a double date?
    menu:
        "Good, I'll meet you in the campus square." if bg_current != "bg campus" or Current_Time != "Evening":  
                    call EmmaFace("smile")
        "Good, let's get going then." if bg_current == "bg campus" and Current_Time == "Evening":  
                    call EmmaFace("smile")
        "And I was thinking of asking. . .": 
                    menu:
                        ch_p "And I was thinking of asking. . ."
                        "Rogue along too." if "yesdate" in R_DailyActions or "yesdate" not in P_DailyActions:
                                    $ Count = E_LikeRogue
                        "Kitty along too." if "yesdate" in K_DailyActions or "yesdate" not in P_DailyActions:
                                    $ Count = E_LikeKitty
                        "Laura along too." if "yesdate" in L_DailyActions or "yesdate" not in P_DailyActions:
                                    $ Count = E_LikeLaura
                        "Never mind, probably a bad idea.":  
                                    call EmmaFace("confused")
                                    ch_e "I see. . ."
                                    if bg_current != "bg campus": 
                                            ch_p "I'll meet you in the campus square then."
    if Count:
        #If you asked about another girl. . .
        if Count >= 600 and ApprovalCheck("Emma", 800, "OI"): #Count is "E_LikeX"
            call EmmaFace("smile")
            ch_e "She'd be lovely company."                                
        elif Count >= 750:
            call EmmaFace("bemused")
            ch_e "Hmmm, you have good taste. . ."                                
        elif ApprovalCheck("Emma", 1300, "LO"): 
            call EmmaFace("sad")
            ch_e "Oh, if that's what you'd like. . ."             
        else:
            call EmmaFace("angry")
            ch_e "No, I don't think I would be up for that."  
            $ Count = 0
            return
        $ E_DailyActions.append("yesdouble")  
        if bg_current != "bg campus": 
                ch_p "I'll meet you in the campus square then." 
        $ Count = 0
        
    if bg_current != "bg campus" or Current_Time != "Evening": 
            ch_e "Yes, see you then."
    $ E_DailyActions.append("yesdate")                  
    $ P_DailyActions.append("yesdate") 
    return


label Emma_Date_Stood_Up:
    # if "stoodup" in E_Traits
    if E_Loc != bg_current:
            "Emma storms into the room." 
            $ E_Loc = bg_current
            call Display_Emma
    else:
            "Emma turns to you." 
    call EmmaFace("confused")
    call Statup("Emma", "Love", 80, -10)
    ch_e "Can you explain where you were the other night?"
    if "stoodup" in E_History:
        call EmmaFace("angry")
        call Statup("Emma", "Love", 80, -5)
        ch_e "And not for the first time!"
    menu:
            extend ""
            "Oh, sorry about that, slipped my mind.":
                if ApprovalCheck("Emma", 800, "LO") or ApprovalCheck("Emma", 1200):
                        call EmmaFace("angry")
                        call Statup("Emma", "Love", 80, 5)
                        ch_e "Hmph. Well at least you can be honest."
                        if "stoodup" in E_History:
                            call EmmaFace("sad",Eyes="side")
                            call Statup("Emma", "Obed", 80, 5)
                            ch_e "You need to do better than that, however."   
                elif "stoodup" in E_History:
                        call EmmaFace("sad",Eyes="side")
                        call Statup("Emma", "Love", 80, -5)
                        call Statup("Emma", "Obed", 80, 5)
                        ch_e "Well you need to stop slipping up."                    
                else:
                        call EmmaFace("angry")
                        call Statup("Emma", "Obed", 80, -2)
                        call Statup("Emma", "Inbt", 60, 2) 
                        ch_e "The next time, an apology may not be enough."
                        ch_e "If there is a next time."
                
            "I can't imagine that happening, maybe you got the date wrong?":
                if "stoodup" in E_History and ApprovalCheck("Emma", 900, "O"):                            
                        call EmmaFace("confused")
                        call Statup("Emma", "Obed", 95, 15)
                        ch_e "What? . . No, we definitely. . ."                            
                        call EmmaFace("confused",Eyes="side")
                        ch_e "Hm."                                
                elif ApprovalCheck("Emma", 800, "O"):
                        call EmmaFace("angry")
                        call Statup("Emma", "Obed", 95, 10)
                        ch_e "No. . . we definitely. . ."     
                elif not ApprovalCheck("Emma", 700, "L"):
                        call EmmaFace("angry")
                        $ E_RecentActions.append("angry") 
                        $ E_DailyActions.append("angry")  
                        call Statup("Emma", "Love", 80, -10)
                        call Statup("Emma", "Obed", 80, -5)
                        call Statup("Emma", "Inbt", 70, 10) 
                        ch_e "Don't even try that nonsense on me, [E_Petname]!"
                        ch_e "I INVENTED gaslighting."
                else:
                        call EmmaFace("sad")
                        $ E_RecentActions.append("angry") 
                        $ E_DailyActions.append("angry")  
                        call Statup("Emma", "Love", 80, -5)
                        call Statup("Emma", "Obed", 80, -5)
                        call Statup("Emma", "Inbt", 60, 5) 
                        ch_e "Oh, [E_Petname], surely you can do better than that."
                        
            "Yeah, I found something better to do.": 
                if ApprovalCheck("Emma", 1200, "LO"):
                        call EmmaFace("sad",Eyes="side")
                        call Statup("Emma", "Love", 80, -5)
                        call Statup("Emma", "Obed", 80, 5)
                        if "stoodup" in E_History:
                                ch_e "Oh. . . "
                                ch_e "This independent streaks of yours is growing tiresome. . ."                            
                        else:
                                call Statup("Emma", "Obed", 80, 10)
                                ch_e "Oh. . . "
                                ch_e "don't push your luck."
                elif ApprovalCheck("Emma", 800, "LO"):
                        call EmmaFace("angry",Eyes="side")
                        call Statup("Emma", "Love", 80, -10)
                        call Statup("Emma", "Obed", 80, 20) 
                        ch_e "Surely you can do better than that."
                else:
                        call EmmaFace("angry")
                        $ E_RecentActions.append("angry") 
                        $ E_DailyActions.append("angry")  
                        call Statup("Emma", "Love", 80, -15)
                        call Statup("Emma", "Inbt", 60, 5) 
                        ch_e "Well then I suppose I have as well."
                        
    $ E_Traits.remove("stoodup") 
    if "stoodup" not in E_History:  
            $ E_History.append("stoodup") 
    call CleartheRoom("All",Check=1)
    if _return >= 3:
        #if the room is full,
        call Remove_Girl("Emma")
        "Emma wanders off." 
    return
    
# End Emma Ask / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Emma_Date_Prep:
    #This gets Emma Dressed and ready for Dinner, called by Date_Night
    $ Taboo = 40
    if E_Schedule[7]:
        # if she has a date outfit set
        if E_Schedule[7] == 2:
            $ E_Outfit = "costume"
        elif E_Schedule[7] == 3:
            $ E_Outfit = "custom1"
        elif E_Schedule[7] == 4:
            $ E_Outfit = "gym"
        elif E_Schedule[7] == 5:
            $ E_Outfit = "custom2"
        elif E_Schedule[7] == 6:
            $ E_Outfit = "custom3"
        else:
            $ E_Outfit = "teacher"
    else:
        $ Options = ["teacher", "costume"]
        $ Options.append("custom1") if E_Custom[0] == 2 else Options
        $ Options.append("custom2") if E_Custom2[0] == 2 else Options
        $ Options.append("custom3") if E_Custom3[0] == 2 else Options
        $ renpy.random.shuffle(Options) 
        $ E_Outfit = Options[0]
        $ del Options[:]  
    $ E_Loc = "date"
    call EmmaOutfit(Changed=1)
    call EmmaFace("smile")
    return

# End Emma Prep / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Emma Dinner Menu/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /       
label Emma_Dinner(E_Cost=0):
    #Called by Date Dinner, picked Emma's food
    menu:
        "For Emma you order. . ."
        "Surf and turf. ($20)":
                call EmmaFace("sly")
                ch_e "Hmm, a refined choice."  
                call EmmaFace
                call Statup("Emma", "Love", 80, 7)
                call Statup("Emma", "Love", 200, 3)
                $ E_Cost = 20
                $ E_RecentActions.append("surfturf")
        "Steak. ($15)":  
                call EmmaFace("smile")
                ch_e "I do enjoy tender meat."
                call Statup("Emma", "Love", 80, 5)
                $ E_Cost = 15
                $ E_RecentActions.append("ribeye")
        "Chicken. ($10)":
                call EmmaFace("smile")
                ch_e "Chicken is fine."
                call Statup("Emma", "Love", 50, 1)
                call Statup("Emma", "Love", 80, 3)
                $ E_Cost = 10
                $ E_RecentActions.append("chicken")
        "Just a salad. ($5)":
                $ E_Mouth = "sad"
                $ E_Eyes = "sexy"
                $ E_Brows = "confused"            
                ch_e "I suppose I could go for a salad. . ."  
                call Statup("Emma", "Love", 60, -3)
                call Statup("Emma", "Obed", 50, -2)
                $ E_Cost = 5
                $ E_RecentActions.append("salad")
        "Why don't you choose, Emma?":
                call Date_Bonus("Emma",2)
                call EmmaFace("smile")
                ch_e "Thank you, [E_Petname]. I believe I'll have the steak."     
                call EmmaFace("sly")  
                ch_e ". . .and the lobster, of course." 
                call Statup("Emma", "Love", 80, 5)        
                call Statup("Emma", "Inbt", 50, 3)
                call Statup("Emma", "Obed", 50, -2)
                $ E_Cost = 20
                $ E_RecentActions.append("surfturf")
                
    if Party[0] == "Emma":
        $ Prime_Cost = E_Cost
    else:
        $ Second_Cost = E_Cost
    call Date_Bonus("Emma",E_Cost)
    return
# End Emma Menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /          

    
# Start Emma Dinner Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Emma_Dinner_Sex(Previous=0,E_Bonus=0,Options=["nothing"]):
    #Called by Dinner Sex, if Emma is chosen.
    
    if Party[0] == "Emma":
        $ E_Bonus = Prime_Bonus + Prime_Cost
    else:
        $ E_Bonus = Second_Bonus + Second_Cost
        
    if E_Anal and ApprovalCheck("Emma", 1300) and E_Bonus >=15: 
        $ Options.append("anal")        
    if E_Sex and ApprovalCheck("Emma", 1300) and E_Bonus >=10:
        $ Options.append("sex")
    if E_Blow and ApprovalCheck("Emma", 1300) and E_Bonus >=10:
        $ Options.append("blow")      
    if E_Hand and ApprovalCheck("Emma", 1000) and E_Bonus >=10:
        $ Options.append("hand")
    if E_FondleP and ApprovalCheck("Emma", 1000) and E_Bonus >=10:
        $ Options.append("pussy")
    if ApprovalCheck("Emma", 1000) and E_Bonus >=10:
        $ Options.append("foot")
    
    if "Rogue" in Previous:
        $ Previous = "Rogue"
    elif "Kitty" in Previous:
        $ Previous = "Kitty"
    elif "Laura" in Previous:
        $ Previous = "Laura"
    else:
        $ Previous = 0
        
    $ renpy.random.shuffle(Options) 
    
    call EmmaFace("sexy")
    if Options[0] == "nothing":
        pass
    elif Options[0] == "anal":        
        "Halfway through the meal, Emma gets a sly look on her face." 
        "She nods her head suggestively towards the restrooms, and then excuses herself."
        call Date_Sex_Break("Emma",Previous)
        if _return == 4: #you refused
                call EmmaFace("confused")
                "You wait a few minutes until she returns, and shrugs in your direction."
                call Statup("Emma", "Obed", 70, 5)
                call Statup("Emma", "Inbt", 80, -5)
                call Date_Bonus("Emma",-5)
                call EmmaFace("normal")
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
                ch_e "Thank you for helping with the stuffing, [E_Petname]."  
                call Statup("Emma", "Inbt", 50, 9)
                call Statup("Emma", "Inbt", 80, 3)
                $ E_SeenPeen += 1
                $ E_Anal += 1
                $ P_Semen -= 1
                $ E_RecentActions.append("anal")    
                $ E_RecentActions.append("dinnersex")                    
                $ E_DailyActions.append("anal") 
    elif Options[0] == "sex":        
        "Halfway through the meal, Emma gets a sly look on her face." 
        "She nods her head suggestively towards the restrooms, and then excuses herself."
        call Date_Sex_Break("Emma",Previous)
        if _return == 4: #you refused
                call EmmaFace("confused")
                "You wait a few minutes until she returns, and shrugs in your direction."
                call Statup("Emma", "Obed", 70, 5)
                call Statup("Emma", "Inbt", 80, -5)
                call Date_Bonus("Emma",-5)
                call EmmaFace("normal")
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
                ch_e "A little after dinner workout never hurt."
                call Statup("Emma", "Inbt", 50, 8)
                call Statup("Emma", "Inbt", 80, 2)
                $ E_SeenPeen += 1
                $ E_Sex += 1
                $ P_Semen -= 1            
                $ E_RecentActions.append("sex")   
                $ E_RecentActions.append("dinnersex")                    
                $ E_DailyActions.append("sex") 
    elif Options[0] == "blow":
        "Halfway through the meal, Emma gets a sly look on her face, then knocks her fork off the table."
        "She ducks under the table after it, and unzips your pants." 
        call Date_Sex_Break("Emma",Previous)
        if _return == 4: #you refused
                call EmmaFace("sadside", 2)
                "You zip them back up and shoo her away. She gets back up from under the table."
                call Statup("Emma", "Love", 90, -5)
                call Statup("Emma", "Obed", 70, 5)
                call Statup("Emma", "Inbt", 80, -5)
                call Date_Bonus("Emma",-3)
                ch_e "Found it. . ."
        else:
                if _return == 1: #other girl is fine
                        "[Previous] shifts closer and wraps one arm around you, the other hand caressing Emma's cheek."
                        "Emma then procedes to blow you for several minutes until you cum."
                elif _return == 2: #other girl is fine
                        "She then procedes to blow you for several minutes until you cum, while [Previous] pretends to be occupied."
                else: 
                        "She then procedes to blow you for several minutes until you cum."
                call Statup("Emma", "Inbt", 50, 6)
                call Statup("Emma", "Inbt", 80, 2)
                $ E_RecentActions.append("blow")   
                $ E_RecentActions.append("dinnersex")                    
                $ E_DailyActions.append("blow") 
                if E_Swallow:
                    "Emma wipes her mouth as she climbs out from under the table."
                    ch_e "Hmm, a creamy aperitif."          
                    $ E_Addict -= 20
                    $ E_Swallow += 1  
                    $ E_RecentActions.append("swallow")                      
                    $ E_DailyActions.append("swallow")       
                else:
                    "Emma grabs the napkin off your lap and uses it to collect the jiz."
                    ch_e "I suppose that is a bit rude to the help."
                call Statup("Emma", "Inbt", 30, 4)
                call Statup("Emma", "Inbt", 80, 2)
                $ E_SeenPeen += 1
                $ E_Blow += 1
                $ P_Semen -= 1
                if _return == 3:
                    "[Previous] stares daggers at you both as she crawls out from under the table."  
                    call Date_Bonus(Previous,-10)
    elif Options[0] == "hand":
        "Halfway through the meal, Emma gets a sly look on her face, then shifts her chair around next to yours."
        call Date_Sex_Break("Emma",Previous)
        if _return == 4: #you refused
                call EmmaFace("sadside", 2)
                "She tries to unzip your pants under the table, but you shoo her away."
                call Statup("Emma", "Love", 90, -5)
                call Statup("Emma", "Obed", 70, 3)
                call Statup("Emma", "Inbt", 80, -5)
                call Date_Bonus("Emma",-2)
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
                ch_e "I bet the cleaning crew will enjoy that."
                call Statup("Emma", "Inbt", 30, 4)
                call Statup("Emma", "Inbt", 80, 2)
                $ E_Hand += 1
                $ P_Semen -= 1
                $ E_RecentActions.append("hand")     
                $ E_RecentActions.append("dinnersex")                  
                $ E_DailyActions.append("hand") 
                if _return == 3:
                    "[Previous] stares daggers at you both from across the table."
                    call Date_Bonus(Previous,-5)
    elif Options[0] == "pussy":
        "Halfway through the meal, Emma gets a sly look on her face, then shifts her chair around next to yours."
        call Date_Sex_Break("Emma",Previous)
        if _return == 4: #you refused
                if E_Legs:
                    "She takes your hand and pulls it over to her crotch, shoving it under her [E_Legs]."
                else:
                    "She takes your hand and shoves it into her crotch."
                call EmmaFace("sadside", 2)
                "With a glance at [Previous], you jerk your hand away."
                call Statup("Emma", "Love", 90, -7)
                call Statup("Emma", "Obed", 70, 3)
                call Statup("Emma", "Inbt", 80, -5)
                call Date_Bonus("Emma",-3)
        else:
                if E_Legs:
                    "She takes your hand and pulls it over to her crotch, shoving it under her [E_Legs]."
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
                ch_e "Ah, that was lovely, [E_Petname]."
                if _return == 1:
                    ch_e "And thank you, [Previous]."
                    $ E_Les += 1
                call Statup("Emma", "Love", 90, 3)
                call Statup("Emma", "Inbt", 30, 5)            
                call Statup("Emma", "Inbt", 90, 2)
                $ E_FondleP += 1
                $ E_Org += 1
                $ E_RecentActions.append("fondle pussy") 
                $ E_RecentActions.append("dinnersex")                      
                $ E_DailyActions.append("fondle pussy") 
    elif Options[0] == "foot":
        "Halfway through the meal, Emma gets a sly look on her face, then shifts a bit lower in her seat."
        "You suddenly feel her foot in your lap, gently caressing your cock."
        call Date_Sex_Break("Emma",Previous)
        if _return == 4: #you refused
                call EmmaFace("sadside", 2)
                "You shift uncomfortably and push her foot away."
                call Statup("Emma", "Love", 90, -5)
                call Statup("Emma", "Obed", 70, 3)
                call Statup("Emma", "Inbt", 80, -3)
                call Date_Bonus("Emma",-1)
        else:
                call Statup("Player", "Focus", 60, 10)
                if _return == 1: #other girl is fine
                        "[Previous] decides to join in the fun and adds her foot to the mix."
                        call Statup("Player", "Focus", 60, 5)
                if _return == 3:
                    call Date_Bonus(Previous,-3)
                "After several minutes of this, she pulls back."
                ch_e "Patience. . . [E_Petname]."
                call Statup("Emma", "Inbt", 80, 3)
                $ E_RecentActions.append("dinnersex") 
    
    call EmmaFace(B = 0)
    return    
# End Emma Dinner Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    

    
    
# Start Emma Movie Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Emma_Movie_Sex(Previous=0,E_Bonus=0, Options=["nothing"]):
    # Called by Movie_Sex if Emma is chosen
    if Party[0] == "Emma":
        $ E_Bonus = Prime_Bonus
    else:
        $ E_Bonus = Second_Bonus
    
    if "horror" in P_RecentActions:
        $ E_Bonus += 5
    
    if "Rogue" in Previous:
        $ Previous = "Rogue"
    elif "Kitty" in Previous:
        $ Previous = "Kitty"
    elif "Laura" in Previous:
        $ Previous = "Laura"
    else:
        $ Previous = 0
        
    if ApprovalCheck("Emma", 500, Bonus=(10*E_Bonus)):
        call EmmaFace("kiss", 1)
        if "romcom" in P_RecentActions: 
            "Halfway through the movie, inspired by the action on screen, Emma turns to you and starts to make out with you."
        elif "action" in P_RecentActions:        
            "Halfway through the movie, adrenaline pumping from the action on screen, Emma turns to you and starts to make out with you."
        elif "horror" in P_RecentActions:  
            "Halfway through the movie, slightly bored by it, Emma shrugs and starts to make out with you."
        elif "drama" in P_RecentActions:   
            "Halfway through the movie, Emma turns to you with a shrug and starts to make out with you."
        $ E_RecentActions.append("kissing") 
        $ E_RecentActions.append("moviesex")                       
        $ E_DailyActions.append("kissing")      
        call Date_Sex_Break("Emma",Previous)   
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
            
    
        if E_Anal and ApprovalCheck("Emma", 2000, Bonus=(10*E_Bonus)) and PantsNum("Emma") < 5:
                    call EmmaFace("sexy", 1)
                    if E_Panties:
                        "As you make out, Emma reaches down and undoes your fly. She pulls her panties aside and shifts into your lap."
                    else:
                        "As you make out, Emma reaches down and undoes your fly. She hikes her skirt up a bit and shifts into your lap."
                    call Date_Sex_Break("Emma",Previous,1)
                    if _return == 3:
                            #the other girl stormed out. . .
                            ch_e "Hmm, that was uncomfortable."                      
                    "She squeezes your cock into her ass and begins to grind up and down, quietly enough that the other patrons don't seem to notice."
                    if _return == 1:
                            #the other girl joins you. . .
                            "[Previous] also leans over and toys with Emma's pussy."
                    if E_CreamA:
                            if E_Panties:
                                "After several minutes of this, you can't take it anymore and come inside her."
                                "She pulls her panties back up and returns to her seat."
                            else:
                                "After several minutes of this, you can't take it anymore and come inside her."
                                "She wipes off as best she can and shifts back into her seat."
                            $ E_CreamA += 1
                            $ E_RecentActions.append("creampie anal")                      
                            $ E_DailyActions.append("creampie anal") 
                    else:
                            "After several minutes of this, she pulls out and shifts back into her seat, finishing you off with her hand."
                            if E_Swallow:
                                if 0 < _return < 3: #if 1 or 2
                                    "You cum into the popcorn bucket, which she and [Previous] then finish off together."
                                else:
                                    "You cum into the popcorn bucket, which she then finishes off."
                                $ E_Addict -= 20
                                $ E_Swallow += 1
                                $ E_Spunk.append("mouth")                          
                                $ E_RecentActions.append("swallowed")                      
                                $ E_DailyActions.append("swallowed") 
                            else:
                                "You cum into the popcorn bucket, which she sets in the seat next to her."
                    ch_e "Well, that was exciting."
                    call Statup("Emma", "Inbt", 50, 4)
                    call Statup("Emma", "Inbt", 90, 3)
                    $ E_SeenPeen += 1
                    $ E_Anal += 1
                    $ P_Semen -= 1
                    $ E_RecentActions.append("anal")                      
                    $ E_DailyActions.append("anal")  
        elif E_Sex and ApprovalCheck("Emma", 2000, Bonus=(10*E_Bonus)) and PantsNum("Emma") < 5:
                    call EmmaFace("sexy", 1)
                    if E_Panties:
                        "As you make out, Emma reaches down and undoes your fly. She pulls her panties aside and shifts into your lap."
                    else:
                        "As you make out, Emma reaches down and undoes your fly. She hikes her skirt up a bit and shifts into your lap."
                    call Date_Sex_Break("Emma",Previous,1)                    
                    if _return == 3:
                            #the other girl stormed out. . .
                            ch_e "Hmm, that was uncomfortable."     
                    "Seconds later, she's slowly rocking on your cock, quietly enough that the other patrons don't seem to notice."
                    if _return == 1:
                            #the other girl joins you. . .
                            "[Previous] also leans over and toys with Emma's pussy."
                    if E_CreamP:
                        if E_Panties:
                            "After several minutes of this, you can't take it anymore and come inside her."
                            "She pulls her panties up over her dripping slit and returns to her seat."
                        else:
                            "After several minutes of this, you can't take it anymore and come inside her."
                            "She wipes up as best she can and returns to her seat."
                        $ E_CreamP += 1
                        $ E_RecentActions.append("creampie sex")                      
                        $ E_DailyActions.append("creampie sex") 
                    else:
                        "After several minutes of this, she pulls out and shifts back into her seat, finishing you off with her hand."
                        if E_Swallow:
                                if 0 < _return < 3: #if 1 or 2
                                    "You cum into the popcorn bucket, which she and [Previous] then finish off together."
                                else:                                    
                                    "You cum into the popcorn bucket, which she then finishes off."   
                                $ E_Spunk.append("mouth")   
                                $ E_Addict -= 20
                                $ E_Swallow += 1
                                $ E_RecentActions.append("swallowed")                      
                                $ E_DailyActions.append("swallowed") 
                        else:
                                "You cum into the popcorn bucket, which she sets in the seat next to her."
                    ch_e "Well, that was exciting."
                    call Statup("Emma", "Inbt", 50, 4)
                    call Statup("Emma", "Inbt", 90, 3)
                    $ E_SeenPeen += 1
                    $ E_Sex += 1
                    $ P_Semen -= 1
                    $ E_RecentActions.append("sex")                      
                    $ E_DailyActions.append("sex")             
        elif E_Blow and ApprovalCheck("Emma", 1300, Bonus=(10*E_Bonus)):
                    call EmmaFace("sucking", 1)
                    "As you make out, Emma reaches down and undoes your fly. She then bends down and wraps her lips around it."
                    call Date_Sex_Break("Emma",Previous,1)                
                    if _return == 3:
                            #the other girl stormed out. . .
                            ch_e "Hmm, that was uncomfortable."             
                    if _return == 1:
                            #the other girl joins you. . .
                            "[Previous] also leans over joins Emma at licking your cock."
                            "They take turns sucking on it contentedly for several minutes before you finally cum."   
                    else:
                            "She sucks on it contentedly for several minutes before you finally cum."            
                    $ E_Spunk.append("mouth")  
                    if E_Swallow:
                        "Emma wipes her mouth as she shifts back into her seat and washes it down with some soda."
                        call EmmaFace("sexy")
                        ch_e "Mmmm, refreshing. . ."
                        $ E_Addict -= 20
                        $ E_Swallow += 1
                        $ E_RecentActions.append("swallowed")                      
                        $ E_DailyActions.append("swallowed") 
                    else:
                        "You cum into the popcorn bucket, which she sets in the seat next to her."
                        ch_e "That is a bit of a mess for the help."
                    call Statup("Emma", "Inbt", 40, 3)
                    call Statup("Emma", "Inbt", 80, 2)
                    $ E_SeenPeen += 1
                    $ E_Blow += 1
                    $ P_Semen -= 1
                    $ E_RecentActions.append("blow")                      
                    $ E_DailyActions.append("blow") 
        elif E_Hand and ApprovalCheck("Emma", 1000, Bonus=(10*Count2)):
                    call EmmaFace("sexy")
                    "As you make out, Emma reaches down and pulls out your cock." 
                    call Date_Sex_Break("Emma",Previous,1)             
                    if _return == 3:
                            #the other girl stormed out. . .
                            ch_e "Hmm, that was uncomfortable." 
                            "She then leans over and begins to stroke your cock." 
                    elif _return == 1: 
                            #the other girl joins in. . .
                            "She then leans over and begins to stroke your cock."
                            "[Previous] leans in and joins her, and they share a smile."
                    else:
                            "She then leans over and begins to stroke it." 
                    call EmmaFace("surprised")
                    if E_FondleP:
                        if _return == 1: 
                                #the other girl joins in. . .
                                "You also reach down and begin stroking their pussies."
                        else:
                            if E_Legs:
                                    "You also lean over, reach into her [E_Legs], and begin to stroke her pussy."
                            elif E_Hose:
                                    "You also lean in, reach under her [E_Hose], and begin to stroke her pussy."
                            elif E_Panties:
                                    "You also lean in, reach under her panties, and begin to stroke her pussy."
                            else:
                                    "You also lean over, notice she isn't wearing anything down there, and begin to stroke her pussy."
                    call EmmaFace("sexy", 1, Eyes = "closed")
                    if E_FondleP:
                        if _return == 1: 
                            "After several minutes of this, Emma and [Previous] shudder in orgasm, which sets you off as well."
                        else:
                            "After several minutes of this, she shudders in orgasm, which sets you off as well."
                        "Emma catches the jiz in the popcorn bucket."
                    $ E_Eyes = "sexy"
                    if E_Swallow:
                            if 0 < _return < 3: #if 1 or 2
                                "The girls finish off the remaining popcorn with a grin."    
                            else:
                                "She finishes off the remaining popcorn with a grin."                    
                            $ E_Spunk.append("mouth")  
                            ch_e "I do enjoy this new flavor they have, [E_Petname]."     
                            $ E_Addict -= 20
                            $ E_Swallow += 1
                            $ E_RecentActions.append("swallowed")                      
                            $ E_DailyActions.append("swallowed") 
                    else:
                            "You cum into the popcorn bucket, which she sets in the seat next to her."
                            ch_e "That is a bit of a mess for the help."
                    call Statup("Emma", "Love", 90, 2)
                    call Statup("Emma", "Inbt", 40, 3)
                    call Statup("Emma", "Inbt", 80, 2)
                    $ E_FondleP += 1
                    $ E_Org += 1        
                    $ E_Hand += 1
                    $ P_Semen -= 1
                    $ E_RecentActions.append("hand")                      
                    $ E_DailyActions.append("hand") 
        elif E_FondleP and ApprovalCheck("Emma", 900, Bonus=(10*E_Bonus)):
                    call EmmaFace("sexy")                    
                    if E_Legs:
                            "As you make out, Emma grabs your hand and shoves it down her [E_Legs]."
                    elif E_Hose:
                            "As you make out, Emma grabs your hand and shoves it down her [E_Hose]."
                    elif E_Panties:
                            "As you make out, Emma grabs your hand and shoves it down her panties."
                    else:
                            "As you make out, Emma grabs your hand and shoves it between her legs."
                    call Date_Sex_Break("Emma",Previous,1)
                    $ E_Eyes = "closed"
                    if _return == 3:
                            #the other girl stormed out. . .
                            ch_e "Hmm, that was uncomfortable." 
                            "You get back to work."
                    elif _return == 1: 
                            #the other girl joins in. . .
                            "[Previous] leans in and begins to fondle her breasts as well."   
                    "After several minutes of this, she shudders in orgasm and leans back with a contented sigh."
                    $ E_Eyes = "sexy"
                    ch_e "Very. . . kind of you, [E_Petname]. I needed that."
                    call Statup("Emma", "Love", 90, 2)
                    call Statup("Emma", "Inbt", 40, 2)
                    call Statup("Emma", "Inbt", 80, 2)
                    $ E_FondleP += 1
                    $ E_Org += 1    
                    $ E_RecentActions.append("fondle pussy")                      
                    $ E_DailyActions.append("fondle pussy") 
        elif ApprovalCheck("Emma", 1200, Bonus=(5*E_Bonus)) and E_Panties:
                    call EmmaFace("sexy")
                    "After making out for a few minutes, Emma gets a sly look on her face and reaches into her pocket."
                    "After a second, she hands you a cloth lump, apparently her panties." 
                    $ E_DailyActions.append("pantyless") 
                    call Statup("Emma", "Inbt", 60, 2)
                    $ E_Panties = 0
                    ch_e "Just a hint at later, [E_Petname]."
        elif ApprovalCheck("Emma", 1200, Bonus=(5*E_Bonus)):
                    call EmmaFace("sexy")
                    "After making out for a few minutes, Emma gets a sly look on her face, then shifts a bit lower in her seat."
                    if PantsNum("Emma") > 5:
                        "Looking down, you notice she's pulled down her pants enough that you can see her bare pussy, lit by the movie screen."  
                    elif E_Legs == "shorts":
                        "Looking down, you notice she's pulled down her shorts enough that you can see her bare pussy, lit by the movie screen."   
                    else:
                        "Looking down, you notice she's hiked up her skirt enough that you can see her bare pussy, lit by the movie screen."            
                    call Statup("Emma", "Inbt", 60, 2)
                    call Emma_First_Bottomless(1)
                    ch_e "Just a hint at later, [E_Petname]."
    #End Emma movie sex options
    call EmmaOutfit
    return
# End Emma Movie Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    

    
# Start Emma Date End/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label E_Date_End:   
    #Called if you end up with Emma at the end of the date
    if bg_current != "bg player":
            #skips this portion if you are in the player's room already
            menu:
                "Take Emma back to her room?":
                    pass
                "Just leave and head back to yours.":
                    call Date_Ditched
                    jump Date_Over    
                        
            $ bg_current = "bg emma"
            $ E_Loc = "bg emma"
            if "Rogue" in Party:
                $ R_Loc = "bg emma"
            if "Kitty" in Party:
                $ K_Loc = "bg emma" 
            if "Laura" in Party:
                $ L_Loc = "bg emma"
            call Set_The_Scene(Dress=0)
            call Taboo_Level    
    
    if Party[0] == "Emma":
        $ Count = Prime_Bonus
        $ Count2 = Party[1] #the other girl
    else:
        $ Count = Second_Bonus
        $ Count2 = Party[0] #the other girl
    if bg_current != "bg player":   
            "You walk Emma back to her room."
    if Count < 0:      
        call EmmaFace("angry", 0,Eyes = "side")
        ch_e "It's possible I could have had a worse evening, [Playername]."
        if bg_current == "bg player":
                "She marches back to her room. Alone." 
        else:
                "She slams the door on you."
        call Set_The_Scene(Entry=1,Dress=0)
        $ Count = 0
        call Emma_Date_Over(0)
        jump Date_End
    else: 
        if Count > 20:
            call EmmaFace("sexy", 1)            
            if bg_current == "bg player":
                    ch_e "That was a lovely evening, [E_Petname]. Could I come in for a nightcap?"
            else:
                    ch_e "That was a lovely evening, [E_Petname]. Care for a nightcap? . ."           
        else:
            call EmmaFace("smile", 1)
            ch_e "That was a lovely evening, [E_Petname]. We'll have to do it again."
        
        $ E_Date += 1
        menu:
            extend ""
            "Could I get a good night kiss?":
                if ApprovalCheck("Emma", 600, Bonus=(10*Count)):
                    $ E_Mouth = "smile"
                    ch_e "[E_Petname], I suppose I could indulge you."
                    call Date_Sex_Break("Emma",Count2,2)
                    $ MultiAction = 0
                    call E_KissPrep 
                    $ MultiAction = 1
                if ApprovalCheck("Emma", 900, Bonus=(10*Count)):
                    call EmmaFace("sexy", 1)
                    if bg_current == "bg player":
                            ch_e "Hmm, are you sure I couldn't come in? . ."
                    else:
                            ch_e "Hmm, are you sure you couldn't come in? . ."
                    call Date_Sex_Break("Emma",Count2)
                    if _return == 4:
                        if bg_current == "bg player":
                                ch_p "You should probably get going, sorry." 
                        else:
                                ch_p "I should probably get going, sorry."
                        call Emma_Date_Over(0)
                        jump Date_End    
                else:
                    call EmmaFace("smile", 1)
                    ch_e "And now, I'll see you tomorrow, [E_Petname]." 
                    $ Count = 0
                    call Emma_Date_Over(0)
                    jump Date_End
            "Want to have a little fun first?" if bg_current == "bg player":
                if ApprovalCheck("Emma", 800, Bonus=(10*Count)):
                    call EmmaFace("sexy", 1)
                    ch_e "Oh, fine, [E_Petname]. I'll indulge you."
                    call Date_Sex_Break("Emma",Count2)
                    if _return == 4:
                        ch_p "You should probably get going, sorry."  
                        call Emma_Date_Over(0)
                        jump Date_End                  
            
            "Could I come in for a bit?" if bg_current != "bg player":
                if ApprovalCheck("Emma", 800, Bonus=(10*Count)):
                    call EmmaFace("sexy", 1)
                    ch_e "Oh, fine, [E_Petname]. I'll indulge you."
                    call Date_Sex_Break("Emma",Count2)
                    if _return == 4:
                        ch_p "I should probably get going, sorry."  
                        call Emma_Date_Over(0)
                        jump Date_End  
                        
            "Ok, good night then.":
                call EmmaFace("confused", 1, Mouth="smirk")
                if bg_current == "bg player":
                        "Emma looks a little annoyed, but heads out."
                else:
                        "Emma looks a little annoyed, but you head out."
                call Emma_Date_Over(0)
                jump Date_End
                
    # Emma lets you into her room:
    if bg_current != "bg player":
            $ bg_current = "bg emma"  
    call Set_The_Scene(Dress=0)
    call Taboo_Level 
    call EmmaFace("sexy", 1)
    if not Party[1]:
            ch_e "Now, [E_Petname], we're alone together, what would you like to do next? . ."
    else:
            if bg_current == "bg player":           
                    ch_e "Now, [E_Petname], we're in your room together, what would you like to do next? . ."
            else:
                    ch_e "Now, [E_Petname], we're in my room together, what would you like to do next? . ."
    $ P_DailyActions.append("post date") 
    $ renpy.pop_call() #removes call to date
    $ renpy.pop_call() #removes call to Events
    call Emma_SexMenu                       # You have what sex you can get away with
    
    if "angry" in E_RecentActions:      
        if bg_current == "bg player": 
                "Emma stalks through the door and back to her room."  
        else:
                "Emma shoves you out into the hall. You head back to your room."
                $ bg_current = "bg player"
        $ Count = 0
        call Remove_Girl("All")
        $ P_DailyActions.append("post date") 
        jump Player_Room        
    
    if bg_current == "bg player":
            ch_e "I should get going now though. . ."
            "Emma returns to her room." 
            call Remove_Girl("Emma")
            jump Player_Room
                 
    call Sleepover("Emma")  
    jump Misplaced

# End Emma Date End / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    

    
    
# Start Emma Date Over / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Emma_Date_Over(Angry=1):
    # Called if Emma is pissed and leaves
    if Angry:
            $ E_RecentActions.append("angry") 
            $ E_DailyActions.append("angry")  
            call EmmaFace("angry")
            ch_e "I think that's enough of that, [E_Petname]." 
            "Emma leaves."       
    if "study" in P_RecentActions:        
            call Remove_Girl("Emma")
            return  
    if Party[0] == "Emma":
            $ Prime_Bonus = Second_Bonus
            $ Prime_Cost = Second_Cost
            $ Second_Cost = 0    
    $ Party.remove("Emma")
    $ Party.append(0)    
    call Remove_Girl("Emma")
    call Shift_Focus(Party[0])     
    return
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
