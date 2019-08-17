# Start R Doggy //////////////////////////////////////////////////////////////////////////////////
# E_Doggy_P //////////////////////////////////////////////////////////////////////

label E_Doggy_P:  
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Emma")
    if E_Sex >= 7: # She loves it
        $ Tempmod += 15
    elif E_Sex >= 3: #You've done it before several times
        $ Tempmod += 12
    elif E_Sex: #You've done it before
        $ Tempmod += 10    
        
    if E_Addict >= 75 and (E_CreamP + E_CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 20
    elif E_Addict >= 75:
        $ Tempmod += 15
        
    if E_Lust > 85:
        $ Tempmod += 10
    elif E_Lust > 75: #She's really horny
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 10 
    if "exhibitionist" in E_Traits:    
        $ Tempmod += (4*Taboo)      
    if "dating" in E_Traits or "sex friend" in E_Petnames:
        $ Tempmod += 10
    elif "ex" in E_Traits:
        $ Tempmod -= 40
    if E_ForcedCount and not E_Forced:
        $ Tempmod -= 5 * E_ForcedCount
    
    
        
    if Taboo and "tabno" in E_DailyActions:        
        $ Tempmod -= 10 
        
    if "no sex" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no sex" in E_RecentActions else 0                  
             
        
    $ Approval = ApprovalCheck("Emma", 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)
    
    if Situation == "Emma":                                                                  #Emma auto-starts   
        if Approval > 2:                                                      # fix, add emma auto stuff here
            call Emma_Doggy_Launch("L")   
            if E_Legs == "skirt":
                "Emma turns and backs up against your cock, sliding her skirt up as she does so."
                $ E_Upskirt = 1
            elif E_Legs == "pants":
                "Emma turns and backs up against your cock, sliding her pants off as she does so."                
                $ E_Legs = 0
            else:
                "Emma turns and backs up against your cock."
            $ E_SeenPanties = 1
            "She slides the tip along her pussy and seems to want you to insert it."
            menu:
                "What do you do?"
                "Nothing.":                    
                    call Statup("Emma", "Inbt", 80, 3) 
                    call Statup("Emma", "Inbt", 50, 2)
                    "Emma slides it in."
                "Praise her.":       
                    call EmmaFace("sexy", 1)                    
                    call Statup("Emma", "Inbt", 80, 3) 
                    ch_p "Oh yeah, [E_Pet], let's do this."
                    call Emma_Namecheck
                    "Emma slides it in."
                    call Statup("Emma", "Love", 85, 1)
                    call Statup("Emma", "Obed", 90, 1)
                    call Statup("Emma", "Obed", 50, 2)
                "Ask her to stop.":
                    call EmmaFace("surprised")       
                    call Statup("Emma", "Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [E_Pet]."
                    call Emma_Namecheck
                    "Emma pulls back."
                    call Statup("Emma", "Obed", 90, 1)
                    call Statup("Emma", "Obed", 50, 1)
                    call Statup("Emma", "Obed", 30, 2)
                    return            
            jump E_Doggy_SexPrep
        else:                
            $ Tempmod = 0                               # fix, add emma auto stuff here
            $ Trigger2 = 0
        return            
    
    if Situation == "auto":   
        call Emma_Doggy_Launch("L")   
        if E_Legs == "skirt":
            "You press up against Emma's backside, sliding her skirt up as you go."
            $ E_Upskirt = 1
        elif E_Legs == "pants":
            "You press up against Emma's backside, sliding her pants down as you do."                
            $ E_Legs = 0
        else:
            "You press up against Emma's backside."
        $ E_SeenPanties = 1
        "You rub the tip of your cock against her moist slit."        
        call EmmaFace("surprised", 1)
        
        if (E_Sex and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
            "Emma is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            call EmmaFace("sexy")
            call Statup("Emma", "Obed", 70, 3)
            call Statup("Emma", "Inbt", 50, 3) 
            call Statup("Emma", "Inbt", 70, 1) 
            ch_e "Ok, [E_Petname], let's do this."            
            jump E_Doggy_SexPrep         
        else:                                                                                                            #she's questioning it
            $ E_Brows = "angry"                
            menu:
                ch_e "Hey, what do you think you're doing back there?!" 
                "Sorry, sorry! Never mind.":
                    if Approval:     
                        call EmmaFace("sexy", 1)
                        call Statup("Emma", "Obed", 70, 3)
                        call Statup("Emma", "Inbt", 50, 3) 
                        call Statup("Emma", "Inbt", 70, 1) 
                        ch_e "Well, since you're be'in so nice about it, I guess we can give it a go. . ."
                        jump E_Doggy_SexPrep
                    "You pull back before you really get it in."                    
                    call EmmaFace("bemused", 1)
                    if E_Sex:
                        ch_e "Well ok, [E_Petname], no harm done. Just give me a little warning next time." 
                    else:
                        ch_e "Well ok, [E_Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."                                               
                "Just fucking.":                    
                    call Statup("Emma", "Love", 80, -10, 1)  
                    call Statup("Emma", "Love", 200, -10)
                    "You press inside some more."                              
                    call Statup("Emma", "Obed", 70, 3)
                    call Statup("Emma", "Inbt", 50, 3) 
                    if not ApprovalCheck("Emma", 700, "O", TabM=1):   #Checks if Obed is 700+                          
                        call EmmaFace("angry")
                        "Emma shoves you away and slaps you in the face."
                        ch_e "Jackass!"
                        ch_e "If that's how you want to treat me, we're done here!"                                                  
                        call Statup("Emma", "Love", 50, -10, 1)                        
                        call Statup("Emma", "Obed", 50, 3)
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Emma_Sex_Reset
                        $ E_RecentActions.append("angry")
                        $ E_DailyActions.append("angry")                    
                    else:
                        call EmmaFace("sad")
                        "Emma doesn't seem to be into this, you're lucky she's so obedient."                        
                        jump E_Doggy_SexPrep
        return             
    
   
    if not E_Sex and "no sex" not in E_RecentActions:                           #first time    
        call EmmaFace("surprised", 1)
        $ E_Mouth = "kiss"
        ch_e "So, you'd like to take this to the next level? Actual sex? . . ."    
        if E_Forced:
            call EmmaFace("sad")
            ch_e "You'd really take it that far?"
            
            
    if not E_Sex and Approval:                                                  #First time dialog        
        if E_Forced: 
            call EmmaFace("sad")
            call Statup("Emma", "Love", 70, -30, 1)
            call Statup("Emma", "Love", 20, -20, 1)
        elif E_Love >= (E_Obed + E_Inbt):
            call EmmaFace("sexy")
            $ E_Brows = "sad"
            $ E_Mouth = "smile" 
            ch_e "Well, I've never been able to do this before now, so this might be fun."            
        elif E_Obed >= E_Inbt:
            call EmmaFace("normal")
            ch_e "If that's what you want, [E_Petname]. . ."            
        elif E_Addict >= 50:
            call EmmaFace("manic", 1)
            ch_e "Well. . . I bet it would feel really good down there."
        else: # Uninhibited 
            call EmmaFace("sad")
            $ E_Mouth = "smile"             
            ch_e "Hmm, I've always wanted to try it. . ."   
            
    elif Approval:                                                                       #Second time+ dialog        
        call EmmaFace("sexy", 1)
        if E_Forced: 
            call EmmaFace("sad")
            call Statup("Emma", "Love", 70, -3, 1)
            call Statup("Emma", "Love", 20, -2, 1)
            ch_e "That's really what you want?" 
        elif not Taboo and "tabno" in E_DailyActions:        
            ch_e "Well, at least you got us some privacy this time. . ."        
        elif "sex" in E_RecentActions:
            ch_e "You want to go again? Ok."
            jump E_Doggy_SexPrep
        elif "sex" in E_DailyActions:
            $ Line = renpy.random.choice(["Back again so soon?",                 
                "So you'd like another go?",                 
                "You can't stay away from this. . .", 
                "Didn't get enough earlier?",
                "You're going to wear me out."]) 
            ch_e "[Line]"
        elif E_Sex < 3:        
            $ E_Brows = "confused"
            $ E_Mouth = "kiss"
            ch_e "So you'd like another go?"       
        else:       
            $ Line = renpy.random.choice(["You want some of this action?",                 
                "So you'd like another go?",                 
                "You can't stay away from this. . .", 
                "You want me to ride your pole?",
                "You wanna dip your wick?"]) 
            ch_e "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if E_Forced:
            call EmmaFace("sad")
            call Statup("Emma", "Obed", 90, 1)
            call Statup("Emma", "Inbt", 60, 1)
            ch_e "Ok, fine."  
        elif "no sex" in E_DailyActions:               
            ch_e "Ok, you've won me over on this one. . ."
        else:
            call EmmaFace("sexy", 1)
            call Statup("Emma", "Love", 90, 1)
            call Statup("Emma", "Inbt", 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                "Well. . . ok.",                 
                "Sure!", 
                "I guess I could. . . stick it in.",
                "Hells yeah.",
                "Heh, ok, ok."]) 
            ch_e "[Line]"
            $ Line = 0
        call Statup("Emma", "Obed", 20, 1)
        call Statup("Emma", "Obed", 60, 1)
        call Statup("Emma", "Inbt", 70, 2) 
        jump E_Doggy_SexPrep   
    
    else:                                                                               #She's not into it, but maybe. . .    
        call EmmaFace("angry")       
        if "no sex" in E_RecentActions:  
            ch_e "I {i}just{/i} told you \"no,\" [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no sex" in E_DailyActions:  
            ch_e "I already told you that I wouldn't bang you in public!" 
        elif "no sex" in E_DailyActions:       
            ch_e "I already told you \"no,\" [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "I already told you this is too public!"     
        elif not E_Sex:
            call EmmaFace("bemused")
            ch_e "I just don't think I'm ready yet, [E_Petname]. . ."
        else:
            call EmmaFace("bemused")
            ch_e "Not, right now [E_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no sex" in E_DailyActions:
                call EmmaFace("bemused")
                ch_e "Yeah, ok, [E_Petname]."              
                return
            "Maybe later?" if "no sex" not in E_DailyActions:
                call EmmaFace("sexy")  
                ch_e "I'll give it some thought, [E_Petname]."
                call Statup("Emma", "Love", 80, 2)
                call Statup("Emma", "Inbt", 70, 2)   
                if Taboo:                    
                    $ E_RecentActions.append("tabno")                      
                    $ E_DailyActions.append("tabno") 
                $ E_RecentActions.append("no sex")                      
                $ E_DailyActions.append("no sex")            
                return
            "I think you'd enjoy it as much as I would. . .":             
                if Approval:
                    call EmmaFace("sexy")     
                    call Statup("Emma", "Obed", 90, 2)
                    call Statup("Emma", "Obed", 50, 2)
                    call Statup("Emma", "Inbt", 70, 3) 
                    call Statup("Emma", "Inbt", 40, 2) 
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                        "I suppose. . .", 
                        "You've got me there."]) 
                    ch_e "[Line]"
                    $ Line = 0                   
                    jump E_Doggy_SexPrep       
            "Bend over.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Emma", 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad")
                    call Statup("Emma", "Love", 70, -5, 1)
                    call Statup("Emma", "Love", 200, -5)                 
                    ch_e "Ok, fine. If we're going to do this, stick it in already."  
                    call Statup("Emma", "Obed", 80, 4)
                    call Statup("Emma", "Inbt", 80, 1) 
                    call Statup("Emma", "Inbt", 60, 3)  
                    $ E_Forced = 1  
                    jump E_Doggy_SexPrep
                else:                          
                    call Statup("Emma", "Love", 200, -20)   
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Emma_Arms = 1  
    if "no sex" in E_DailyActions:
        ch_e "Learn to take \"no\" for an answer, [E_Petname]." 
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1)
        ch_e "I'm not doing that just because you have me over a barrel."
        call Statup("Emma", "Lust", 200, 5)   
        if E_Love > 300: 
                call Statup("Emma", "Love", 70, -2)
        call Statup("Emma", "Obed", 50, -2)     
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call EmmaFace("angry", 1)
        $ E_RecentActions.append("tabno")                      
        $ E_DailyActions.append("tabno") 
        ch_e "Even if I wanted to, it certainly wouldn't be here!"      
        call Statup("Emma", "Lust", 200, 5)  
        call Statup("Emma", "Obed", 50, -3)
    elif E_Sex:
        call EmmaFace("sad") 
        ch_e "Maybe you could go fuck yourself instead."       
    else:
        call EmmaFace("normal", 1)
        ch_e "No way."     
    $ E_RecentActions.append("no sex")                      
    $ E_DailyActions.append("no sex") 
    $ Tempmod = 0    
    return

label E_Doggy_SexPrep:
    call Seen_First_Peen("Emma",Partner)
    call Emma_Doggy_Launch("hotdog")
    
    if Situation != "auto":
        call Emma_Bottoms_Off       
        
        
        if (E_Panties and not E_PantiesDown) or (E_Legs and not E_Upskirt) or HoseNum("Emma") >= 6: #If she refuses to take off her pants but agreed to sex
            ch_e "Well, I guess some things are necessary, [E_Petname]."            
            if (E_Legs == "pants" and not E_Upskirt) and (E_Panties and not E_PantiesDown):
                "She quickly pulls down her pants and drops her [E_Panties]."
            elif (E_Legs == "pants" and not E_Upskirt):
                "She quickly pulls down her pants, exposing her bare ass."
            elif HoseNum("Emma") >= 6 and (E_Panties and not E_PantiesDown):
                "She quickly pulls down her [E_Hose] and drops her [E_Panties]."
                $ E_Hose = 0
            elif HoseNum("Emma") >= 6:
                "She quickly pulls down her [E_Hose], exposing her bare ass."
                $ E_Hose = 0
            elif (E_Panties and not E_PantiesDown):
                "She quickly pulls down her [E_Panties]."  
            
        $ E_Upskirt = 1
        $ E_PantiesDown = 1       
        $ E_SeenPanties = 1
        call Emma_First_Bottomless
        
        if Taboo: # Emma gets started. . .
            if not E_Sex:
                "Emma glances around for voyeurs. . ."
                "Emma hesitantly pulls down your pants and slowly backs up against your rigid member."
                "You guide it into place and slide it in."
            else:
                "Emma glances around to see if anyone notices what she's doing, then backs her ass up against your cock."
                "You guide your cock into place and ram it home."
            $ E_Inbt += int(Taboo/10)  
            $ E_Lust += int(Taboo/5)
        else:    
            if not E_Sex:
                "Emma hesitantly pulls down your pants slowly backs up against your rigid member."
                "You press her folds aside and nudge your cock in."
            else:
                "Emma bends over and presses her backside against you suggestively."
                "You take careful aim and then ram your cock in."
                            
    else:  #if Situation == "auto"         
        if (E_Legs == "pants" and not E_Upskirt) and (E_Panties and not E_PantiesDown):
            "You quickly pull down her pants and her [E_Panties] and press against her slit."
        elif (E_Panties and not E_PantiesDown):
            "You quickly pull down her [E_Panties] and press against her slit."  
        $ E_Upskirt = 1
        $ E_PantiesDown = 1       
        $ E_SeenPanties = 1
        call Emma_First_Bottomless(1)
            
    if not E_Sex:        
        if E_Forced:
            call Statup("Emma", "Love", 90, -150)
            call Statup("Emma", "Obed", 70, 60)
            call Statup("Emma", "Inbt", 80, 50) 
        else:
            call Statup("Emma", "Love", 90, 30)
            call Statup("Emma", "Obed", 70, 30)
            call Statup("Emma", "Inbt", 80, 60) 
    
    if Situation:   
        $ renpy.pop_call() 
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ P_Cock = "in"
    $ Trigger = "sex"
    $ Speed = 1
    if Taboo:
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no sex")
    $ E_RecentActions.append("sex")                      
    $ E_DailyActions.append("sex") 

label E_Doggy_Sex_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Emma")
        call Emma_Doggy_Launch("sex") 
        call EmmaLust        
        $ P_Cock = "in"
        $ Trigger = "sex"
        
        if  P_Focus < 100:                                                    
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass
                        "Keep going. . . (locked)" if not Speed:
                                    pass
                                    
                        "Start moving? . ." if not Speed:
                                    $ Speed = 1                            
                        "Speed up. . ." if 0 < Speed < 3:                    
                                    $ Speed += 1
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass
                            
                        "Slow Down. . ." if Speed:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
                            
                        "Slap her ass":                     
                                    call E_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump E_Doggy_Sex_Cycle  
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                        
                        "Other options":
                                menu:   
                                    "Offhand action":
                                            if E_Action and MultiAction:
                                                call Emma_Offhand_Set
                                                if Trigger2:
                                                     $ E_Action -= 1
                                            else:
                                                ch_e "I'm actually getting a little tired, so maybe we could wrap this up?"  
                                                
                                    "Shift primary action":
                                            if E_Action and MultiAction:
                                                    menu:
                                                        "How about anal?":
                                                                $ Situation = "shift"
                                                                call E_Doggy_SexAfter
                                                                call E_Doggy_A
                                                        "Just stick it in her ass [[without asking].":
                                                                $ Situation = "auto"
                                                                call E_Doggy_SexAfter
                                                                call E_Doggy_A
                                                        "Pull back to hotdog her.":
                                                                $ Situation = "pullback"
                                                                call E_Doggy_SexAfter
                                                                call E_Doggy_H
                                                        "Never Mind":
                                                                jump E_Doggy_Sex_Cycle
                                            else:
                                                ch_e "I'm actually getting a little tired, so maybe we could wrap this up?" 
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:  
                                        menu:
                                            "Ask Emma to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Emma_Les_Change
                                            "Ask Emma to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Emma")  
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0    
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Emma")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump E_Doggy_Sex_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump E_Doggy_Sex_Cycle 
                                            "Never mind":
                                                        jump E_Doggy_Sex_Cycle 
                                    "Undress Emma":
                                            call E_Undress   
                                    "Clean up Emma (locked)" if not E_Spunk:
                                            pass  
                                    "Clean up Emma" if E_Spunk:
                                            call Emma_Cleanup("ask")                                         
                                    "Never mind":
                                            jump E_Doggy_Sex_Cycle                                    
                                                        
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Emma_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_Doggy_SexAfter
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Emma_Sex_Reset
                                    $ Line = 0
                                    jump E_Doggy_SexAfter
        #End menu (if Line)              
        
        call Shift_Focus("Emma")
        call Sex_Dialog("Emma",Partner)
        
        $ Cnt += 1
        $ Round -= 1        
        $ P_Wet = 1 #wets penis
        $ P_Spunk = 0 if (P_Spunk and "in" not in E_Spunk) else P_Spunk #cleans you off after one cycle
        
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or E_Lust >= 100:   
                    #If either of you could cum    
                    if P_Focus >= 100:
                            #If you can cum:                                                
                            call PE_Cumming
                            if "angry" in E_RecentActions:  
                                call Emma_Sex_Reset
                                return    
                            call Statup("Emma", "Lust", 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                    $ E_RecentActions.append("unsatisfied")                      
                                    $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_Doggy_SexAfter 
                            $ Line = "came"

                    if E_Lust >= 100:         
                            #If you're still going at it and Emma can cum
                            call E_Cumming
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_Doggy_SexAfter
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump E_Doggy_SexAfter
                            elif "unsatisfied" in E_RecentActions:
                                #And Emma is unsatisfied,  
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if P_Semen:
                                        $ Line = "You get back into it" 
                                        jump E_Doggy_Sex_Cycle  
                                    "No, I'm done." if P_Semen:
                                        "You pull back."
                                        jump E_Doggy_SexAfter
                                    "No, I'm spent." if not P_Semen:
                                        "You pull back."
                                        jump E_Doggy_SexAfter        
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Emma")            
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
        elif Cnt == (5 + E_Sex):
                    $ E_Brows = "confused"
                    ch_e "Are you getting close here? I'm getting as little sore."   
        elif Cnt == (10 + E_Sex):
                    $ E_Brows = "angry"        
                    ch_e "I'm . . .getting . . .worn out. . . here, . . [E_Petname]."
                    menu:
                        ch_e "Can we. . . do something. . . else?"
                        "How about a BJ?" if E_Action and MultiAction:
                                $ Situation = "shift"
                                call E_Doggy_SexAfter
                                call E_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                jump E_Doggy_Sex_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Emma_Sex_Reset
                                $ Situation = "shift"
                                jump E_Doggy_SexAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    call Statup("Emma", "Love", 200, -5)
                                    call Statup("Emma", "Obed", 50, 3)                    
                                    call Statup("Emma", "Obed", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call EmmaFace("angry", 1)   
                                    call Emma_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_e "Well if that's your attitude you can handle your own business."                         
                                    call Statup("Emma", "Love", 50, -3, 1)
                                    call Statup("Emma", "Love", 80, -4, 1)
                                    call Statup("Emma", "Obed", 30, -1, 1)                    
                                    call Statup("Emma", "Obed", 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_Doggy_SexAfter
        #End Count check
   
        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    ch_e "Ok, [E_Petname], that's enough of that for now."
    
label E_Doggy_SexAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Emma_Sex_Reset
        
    call EmmaFace("sexy") 
    
    $ E_Sex += 1  
    $ E_Action -=1
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1        
    call Statup("Emma", "Inbt", 30, 2) 
    call Statup("Emma", "Inbt", 70, 1) 
    
    call Partner_Like("Emma",3,2)
    
    if "Emma Sex Addict" in Achievements:
            pass 
            
    elif E_Sex >= 10:
        $ E_SEXP += 5
        $ Achievements.append("Emma Sex Addict")
        if not Situation:
            call EmmaFace("smile", 1)
            ch_e "I think I'm getting addicted to this."               
    elif E_Sex == 1:            
            $E_SEXP += 20        
            if not Situation: 
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "That was really great, [E_Petname], we'll have to do that again sometime."
                elif E_Obed <= 500 and P_Focus <= 20:
                    $ E_Mouth = "sad"
                    ch_e "Did you get what you needed here?"
    elif E_Sex == 5:
            ch_e "We're making a regular habit of this."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in E_RecentActions:
            call EmmaFace("angry")
            $ E_Eyes = "side"
            ch_e "I didn't exactly get off there. . ."
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_e "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# End R Doggy //////////////////////////////////////////////////////////////////////////////////


# E_Doggy_A anal //////////////////////////////////////////////////////////////////////

label E_Doggy_A:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Emma")
    if E_Anal >= 7: # She loves it
        $ Tempmod += 20   
    elif E_Anal >= 3: #You've done it before several times
        $ Tempmod += 17
    elif E_Anal: #You've done it before
        $ Tempmod += 15 
        
    if E_Addict >= 75 and (E_CreamP + E_CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 25
    elif E_Addict >= 75: 
        $ Tempmod += 15
    
    if E_Lust > 85:
        $ Tempmod += 10
    elif E_Lust > 75: #She's really horny
        $ Tempmod += 5
        
    if E_Loose:
        $ Tempmod += 10  
    elif "anal" in E_RecentActions:
        $ Tempmod -= 20 
    elif "anal" in E_DailyActions:
        $ Tempmod -= 10
        
    if Situation == "shift":
        $ Tempmod += 10    
    if "exhibitionist" in E_Traits:
        $ Tempmod += (5*Taboo) 
        
    if "dating" in E_Traits or "sex friend" in E_Petnames:
        $ Tempmod += 10      
    elif "ex" in E_Traits:
        $ Tempmod -= 40  
    if E_ForcedCount and not E_Forced:
        $ Tempmod -= 5 * E_ForcedCount
        
    if Taboo and "tabno" in E_DailyActions:        
        $ Tempmod -= 10 
    if "no anal" in E_DailyActions:               
        $ Tempmod -= 5         
        $ Tempmod -= 10 if "no anal" in E_RecentActions else 0  
            
    $ Approval = ApprovalCheck("Emma", 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)
    
    if Situation == "Emma":                                                                  #Emma auto-starts   
        if Approval > 2:                                                      # fix, add emma auto stuff here
            call Emma_Doggy_Launch("L")   
            if E_Legs == "skirt":
                "Emma turns and backs up against your cock, sliding her skirt up as she does so."
                $ E_Upskirt = 1
            elif E_Legs == "pants":
                "Emma turns and backs up against your cock, sliding her pants off as she does so."                
                $ E_Legs = 0
            else:
                "Emma turns and backs up against your cock."
            $ E_SeenPanties = 1
            "She slides the tip up to her anus, and presses against it."
            menu:
                "What do you do?"
                "Nothing.":                    
                    call Statup("Emma", "Inbt", 80, 3) 
                    call Statup("Emma", "Inbt", 50, 2)
                    "Emma slides it in."
                "Praise her.":       
                    call EmmaFace("sexy", 1)                    
                    call Statup("Emma", "Inbt", 80, 3) 
                    ch_p "Ooo, dirty girl, [E_Pet], let's do this."
                    call Emma_Namecheck
                    "Emma slides it in."
                    call Statup("Emma", "Love", 85, 1)
                    call Statup("Emma", "Obed", 90, 1)
                    call Statup("Emma", "Obed", 50, 2)
                "Ask her to stop.":
                    call EmmaFace("surprised")       
                    call Statup("Emma", "Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [E_Pet]."
                    call Emma_Namecheck
                    "Emma pulls back."
                    call Statup("Emma", "Obed", 90, 1)
                    call Statup("Emma", "Obed", 50, 1)
                    call Statup("Emma", "Obed", 30, 2)                    
                    return            
            jump E_Doggy_AnalPrep
        else:                
            $ Tempmod = 0                               # fix, add emma auto stuff here
            $ Trigger2 = 0
        return            
    
    if Situation == "auto":   
        call Emma_Doggy_Launch("L")   
        if E_Legs == "skirt":
            "You press up against Emma's backside, sliding her skirt up as you go."
            $ E_Upskirt = 1
        elif E_Legs == "pants":
            "You press up against Emma's backside, sliding her pants down as you do."                
            $ E_Legs = 0
        else:
            "You press up against Emma's backside."
        $ E_SeenPanties = 1
        "You press the tip of your cock against her tight rim."        
        call EmmaFace("surprised", 1)
        
        if (E_Anal and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
            "Emma is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            call EmmaFace("sexy")
            call Statup("Emma", "Obed", 70, 3)
            call Statup("Emma", "Inbt", 50, 3) 
            call Statup("Emma", "Inbt", 70, 1) 
            ch_e "Hmm, stick it in. . ."            
            jump E_Doggy_AnalPrep         
        else:                                                                                                            #she's questioning it
            $ E_Brows = "angry"                
            menu:
                ch_e "Hey, what do you think you're doing back there?!" 
                "Sorry, sorry! Never mind.":
                    if Approval:     
                        call EmmaFace("sexy", 1)
                        call Statup("Emma", "Obed", 70, 3)
                        call Statup("Emma", "Inbt", 50, 3) 
                        call Statup("Emma", "Inbt", 70, 1) 
                        ch_e "I guess if you really want to try it. . ."
                        jump E_Doggy_AnalPrep
                    "You pull back before you really get it in."                    
                    call EmmaFace("bemused", 1)
                    if E_Anal:
                        ch_e "Well ok, [E_Petname], no harm done. Just give me a little warning next time." 
                    else:
                        ch_e "Well ok, [E_Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."                                               
                "Just fucking.":                    
                    call Statup("Emma", "Love", 80, -10, 1)  
                    call Statup("Emma", "Love", 200, -8)
                    "You press into her."                              
                    call Statup("Emma", "Obed", 70, 3)
                    call Statup("Emma", "Inbt", 50, 3) 
                    if not ApprovalCheck("Emma", 700, "O", TabM=1):                        
                        call EmmaFace("angry")
                        "Emma shoves you away and slaps you in the face."
                        ch_e "Jackass!"
                        ch_e "If that's how you want to treat me, we're done here!"                                                  
                        call Statup("Emma", "Love", 50, -10, 1)                        
                        call Statup("Emma", "Obed", 50, 3)
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Emma_Sex_Reset
                        $ E_RecentActions.append("angry")
                        $ E_DailyActions.append("angry")                        
                    else:
                        call EmmaFace("sad")
                        "Emma doesn't seem to be into this, you're lucky she's so obedient."                        
                        jump E_Doggy_AnalPrep
        return             
    
   
    if not E_Anal and "no anal" not in E_RecentActions:                                                               #first time    
        call EmmaFace("surprised", 1)
        $ E_Mouth = "kiss"
        ch_e "Wait, so you want to stick it in my butt?!"
  
        if E_Forced:
            call EmmaFace("sad")
            ch_e "Seriously?"
        
    if not E_Loose and ("dildo anal" in E_DailyActions or "anal" in E_DailyActions):
        call EmmaFace("bemused", 1)
        ch_e "I'm still a little sore from earlier."
            
    elif "anal" in E_RecentActions:
        call EmmaFace("sexy", 1)
        ch_e "You want to go again? Ok."
        jump E_Doggy_AnalPrep
        
    
    if not E_Anal and Approval:                                                 #First time dialog        
        if E_Forced: 
            call EmmaFace("sad")
            call Statup("Emma", "Love", 70, -3, 1)
            call Statup("Emma", "Love", 20, -2, 1)
        elif E_Love >= (E_Obed + E_Inbt):
            call EmmaFace("sexy")
            $ E_Brows = "sad"
            $ E_Mouth = "smile" 
            ch_e "I guess if you really want to try it. . ."           
        elif E_Obed >= E_Inbt:
            call EmmaFace("normal")
            ch_e "Ok, [E_Petname], I'm ready."
        elif E_Addict >= 50:
            call EmmaFace("manic", 1)
            ch_e "Well. . . I bet it would feel really good down there."
        else: # Uninhibited 
            call EmmaFace("sad")
            $ E_Mouth = "smile"             
            ch_e "Hmm, it has been on my list. . ."  
    
    elif Approval:                                                                       #Second time+ dialog
        if E_Forced: 
            call EmmaFace("sad")
            call Statup("Emma", "Love", 70, -3, 1)
            call Statup("Emma", "Love", 20, -2, 1)
            ch_e "That's really what you want?"
        elif not Taboo and "tabno" in E_DailyActions:        
            ch_e "Well, at least you got us some privacy this time. . ."   
        elif "anal" in E_DailyActions and not E_Loose:
            pass      
        elif "anal" in E_RecentActions:
            ch_e "I think I'm warmed up. . ."
            jump E_Doggy_AnalPrep
        elif "anal" in E_DailyActions:
            call EmmaFace("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",                 
                "So you'd like another go?",                 
                "I'm still a little sore from earlier.", 
                "Didn't get enough earlier?",
                "You're going to wear me out."]) 
            ch_e "[Line]"
        elif E_Anal < 3:        
            call EmmaFace("sexy", 1)
            $ E_Brows = "confused"
            $ E_Mouth = "kiss"
            ch_e "So you'd like another go?"       
        else:       
            call EmmaFace("sexy", 1)
            $ Emma_Arms = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                "So you'd like another go?",                 
                "You can't stay away from this booty.", 
                "You want me to ride your pole?",
                "You wanna dip your wick?"]) 
            ch_e "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if E_Forced:
            call EmmaFace("sad")
            call Statup("Emma", "Obed", 90, 1)
            call Statup("Emma", "Inbt", 60, 1)
            ch_e "Ok, fine."   
        elif "no anal" in E_DailyActions:               
            ch_e "Ok, ok, I have been itching for this. . ." 
        else:
            call EmmaFace("sexy", 1)
            call Statup("Emma", "Love", 90, 1)
            call Statup("Emma", "Inbt", 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                "Well. . . ok.",                 
                "Sure!", 
                "I guess I could. . . stick it in.",
                "Hells yeah.",
                "Heh, ok, ok."]) 
            ch_e "[Line]"
            $ Line = 0
        call Statup("Emma", "Obed", 20, 1)
        call Statup("Emma", "Obed", 60, 1)
        call Statup("Emma", "Inbt", 70, 2) 
        jump E_Doggy_AnalPrep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call EmmaFace("angry")
        if "no anal" in E_RecentActions:  
            ch_e "What part of \"no,\" did you not get, [E_Petname]?"
        elif Taboo and "tabno" in E_DailyActions and "no anal" in E_DailyActions:
            ch_e "I already told you that I wouldn't do that out here!"  
        elif "no anal" in E_DailyActions:       
            ch_e "I already told you \"no,\" [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "I already told you that I wouldn't do that out here!"  
        elif not E_Anal:
            call EmmaFace("bemused")
            ch_e "I'm just not into that, [E_Petname]. . ."
        elif not E_Loose and "anal" not in E_DailyActions:
            call EmmaFace("perplexed")
            ch_e "You could have been a bit more gentle last time, [E_Petname]. . ."
        else:
            call EmmaFace("bemused")
            ch_e "Not, right now [E_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no anal" in E_DailyActions:
                call EmmaFace("bemused")
                ch_e "Yeah, ok, [E_Petname]."              
                return
            "Maybe later?" if "no anal" not in E_DailyActions:
                call EmmaFace("sexy")  
                ch_e "I'll give it some thought, [E_Petname]."
                call Statup("Emma", "Love", 80, 2)
                call Statup("Emma", "Inbt", 70, 2)  
                if Taboo:                    
                    $ E_RecentActions.append("tabno")                      
                    $ E_DailyActions.append("tabno") 
                $ E_RecentActions.append("no anal")                      
                $ E_DailyActions.append("no anal") 
                return
            "I bet it would feel really good. . .":             
                if Approval:
                    call EmmaFace("sexy")     
                    call Statup("Emma", "Obed", 90, 2)
                    call Statup("Emma", "Obed", 50, 2)
                    call Statup("Emma", "Inbt", 70, 3) 
                    call Statup("Emma", "Inbt", 40, 2) 
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                        "I suppose. . .", 
                        "You've got me there."]) 
                    ch_e "[Line]"
                    $ Line = 0                   
                    jump E_Doggy_AnalPrep
                else:   
                    pass
                    
            "Bend over.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Emma", 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad")
                    call Statup("Emma", "Love", 70, -5, 1)
                    call Statup("Emma", "Love", 200, -5)                 
                    ch_e "Ok, fine. If we're going to do this, stick it in already."  
                    call Statup("Emma", "Obed", 80, 4)
                    call Statup("Emma", "Inbt", 80, 1) 
                    call Statup("Emma", "Inbt", 60, 3)  
                    $ E_Forced = 1  
                    jump E_Doggy_AnalPrep
                else:                              
                    call Statup("Emma", "Love", 200, -20)    
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Emma_Arms = 1  
    if "no anal" in E_DailyActions:
        ch_e "Learn to take \"no\" for an answer, [E_Petname]."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1)
        ch_e "That's a bit much, even for you."
        call Statup("Emma", "Lust", 200, 5)       
        if E_Love > 300: 
                call Statup("Emma", "Love", 70, -2)
        call Statup("Emma", "Obed", 50, -2)    
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call EmmaFace("angry", 1)
        $ E_RecentActions.append("tabno")                      
        $ E_DailyActions.append("tabno") 
        ch_e "That you would even suggest such a thing in a place like this. . ."    
        call Statup("Emma", "Lust", 200, 5)  
        call Statup("Emma", "Obed", 50, -3) 
    elif not E_Loose and "anal" in E_DailyActions:
        call EmmaFace("bemused")
        ch_e "Sorry, I just need a little break back there, [E_Petname]."    
    elif E_Anal:
        call EmmaFace("sad") 
        ch_e "The only thing you can do with my ass is kiss it, [E_Petname]."
        ch_e ". . .Don't get any ideas."   
    else:
        call EmmaFace("normal", 1)
        ch_e "Not happening."    
    $ E_RecentActions.append("no anal")                      
    $ E_DailyActions.append("no anal") 
    $ Tempmod = 0    
    return

label E_Doggy_AnalPrep:    
    call Seen_First_Peen("Emma",Partner)            
    call Emma_Doggy_Launch("hotdog")
    
    if Situation != "auto":
        call Emma_Bottoms_Off        
        if (E_Panties and not E_PantiesDown) or (E_Legs and not E_Upskirt) or HoseNum("Emma") >= 6: #If she refuses to take off her pants but agreed to sex
            ch_e "Well, I guess some things are necessary, [E_Petname]."            
            if (E_Legs == "pants" and not E_Upskirt) and (E_Panties and not E_PantiesDown):
                "She quickly pulls down her pants and drops her [E_Panties]."
            elif (E_Legs == "pants" and not E_Upskirt):
                "She quickly pulls down her pants, exposing her bare ass."
            elif HoseNum("Emma") >= 6 and (E_Panties and not E_PantiesDown):
                "She quickly pulls down her [E_Hose] and drops her [E_Panties]."
                $ E_Hose = 0
            elif HoseNum("Emma") >= 6:
                "She quickly pulls down her [E_Hose], exposing her bare ass."
                $ E_Hose = 0
            elif (E_Panties and not E_PantiesDown):
                "She quickly pulls down her [E_Panties]."    
            
        $ E_Upskirt = 1
        $ E_PantiesDown = 1       
        $ E_SeenPanties = 1
        call Emma_First_Bottomless
        
        if Taboo: # Emma gets started. . .
            if E_Anal:                
                "Emma glances around to see if anyone notices what she's doing, then backs her ass up against your cock."
                "You guide your cock into place and ram it home."   
                
            else:         
                "Emma glances around for voyeurs. . ."
                "Emma hesitantly pulls down your pants and slowly backs up against your rigid member."
                "You guide it into place and slide it in."
            $ E_Inbt += int(Taboo/10)  
            $ E_Lust += int(Taboo/5)
        else:    
            if not E_Anal:
                "Emma bends over and presses her backside against you suggestively."
                "You take careful aim and then push your cock in."
            else:
                "Emma hesitantly pulls down your pants slowly backs up against your rigid member."
                "You press against her rim and nudge your cock in."
                     
    else: #if Situation == "auto"               
        if (E_Legs == "pants" and not E_Upskirt) and (E_Panties and not E_PantiesDown):
            "You quickly pull down her pants and her [E_Panties] and press against her ass."
        elif (E_Panties and not E_PantiesDown):
            "You quickly pull down her [E_Panties] and press against her ass."  
            
        $ E_Upskirt = 1
        $ E_PantiesDown = 1       
        $ E_SeenPanties = 1
        call Emma_First_Bottomless(1)
    
    if not E_Anal:                                                      #First time stat buffs       
        if E_Forced:
            call Statup("Emma", "Love", 90, -150)
            call Statup("Emma", "Obed", 70, 70)
            call Statup("Emma", "Inbt", 80, 40) 
        else:
            call Statup("Emma", "Love", 90, 10)
            call Statup("Emma", "Obed", 70, 30)
            call Statup("Emma", "Inbt", 80, 70) 
    elif not E_Loose:                                                   #first few times stat buffs       
        if E_Forced:
            call Statup("Emma", "Love", 90, -20)
            call Statup("Emma", "Obed", 70, 10)
            call Statup("Emma", "Inbt", 80, 5) 
        else:
            call Statup("Emma", "Obed", 70, 7)
            call Statup("Emma", "Inbt", 80, 5) 
                
    if Situation:    
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ P_Cock = "anal"
    $ Trigger = "anal"
    $ Speed = 1
    if Taboo:
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no anal")
    $ E_RecentActions.append("anal")                      
    $ E_DailyActions.append("anal") 

label E_Doggy_Anal_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Emma")
        call Emma_Doggy_Launch("anal") 
        call EmmaLust        
        $ P_Cock = "anal"
        $ Trigger = "anal"
        
        if  P_Focus < 100:                                                    
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass
                        "Keep going. . . (locked)" if not Speed:
                                    pass
                                    
                        "Start moving? . ." if not Speed:
                                    $ Speed = 1                            
                        "Speed up. . ." if 0 < Speed < 3:                    
                                    $ Speed += 1
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass
                            
                        "Slow Down. . ." if Speed:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
                            
                        "Slap her ass":                     
                                    call E_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump E_Doggy_Anal_Cycle  
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                        
                        "Other options":
                                menu:   
                                    "Offhand action":
                                            if E_Action and MultiAction:
                                                call Emma_Offhand_Set
                                                if Trigger2:
                                                     $ E_Action -= 1
                                            else:
                                                ch_e "I'm actually getting a little tired, so maybe we could wrap this up?"  
                                                
                                    "Shift primary action":
                                            if E_Action and MultiAction:
                                                    menu:
                                                        "How about sex?":
                                                                $ Situation = "shift"
                                                                call E_Doggy_AnalAfter
                                                                call E_Doggy_P
                                                        "Just stick it in her pussy [[without asking].":
                                                                $ Situation = "auto"
                                                                call E_Doggy_AnalAfter
                                                                call E_Doggy_P
                                                        "Pull back to hotdog her.":
                                                                $ Situation = "pullback"
                                                                call E_Doggy_AnalAfter
                                                                call E_Doggy_H
                                                        "Never Mind":
                                                                jump E_Doggy_Anal_Cycle
                                            else:
                                                ch_e "I'm actually getting a little tired, so maybe we could wrap this up?" 
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:  
                                        menu:
                                            "Ask Emma to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Emma_Les_Change
                                            "Ask Emma to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Emma")  
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0    
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Emma")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump E_Doggy_Anal_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump E_Doggy_Anal_Cycle 
                                            "Never mind":
                                                        jump E_Doggy_Anal_Cycle 
                                    "Undress Emma":
                                            call E_Undress   
                                    "Clean up Emma (locked)" if not E_Spunk:
                                            pass  
                                    "Clean up Emma" if E_Spunk:
                                            call Emma_Cleanup("ask")                                         
                                    "Never mind":
                                            jump E_Doggy_Anal_Cycle                                    
                                                        
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Emma_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_Doggy_AnalAfter
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Emma_Sex_Reset
                                    $ Line = 0
                                    jump E_Doggy_AnalAfter
        #End menu (if Line)              
        
        call Shift_Focus("Emma")
        call Sex_Dialog("Emma",Partner)
        
        $ Cnt += 1
        $ Round -= 1     
        
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or E_Lust >= 100:   
                    #If either of you could cum    
                    if P_Focus >= 100:
                            #If you can cum:                                                
                            call PE_Cumming
                            if "angry" in E_RecentActions:  
                                call Emma_Sex_Reset
                                return    
                            call Statup("Emma", "Lust", 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                    $ E_RecentActions.append("unsatisfied")                      
                                    $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_Doggy_AnalAfter 
                            $ Line = "came"

                    if E_Lust >= 100:         
                            #If you're still going at it and Emma can cum
                            call E_Cumming
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_Doggy_AnalAfter
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump E_Doggy_AnalAfter
                            elif "unsatisfied" in E_RecentActions:
                                #And Emma is unsatisfied,  
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if P_Semen:
                                        $ Line = "You get back into it" 
                                        jump E_Doggy_Anal_Cycle  
                                    "No, I'm done." if P_Semen:
                                        "You pull back."
                                        jump E_Doggy_AnalAfter
                                    "No, I'm spent." if not P_Semen:
                                        "You pull back."
                                        jump E_Doggy_AnalAfter        
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Emma")            
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
        elif Cnt == (5 + E_Anal):
                    $ E_Brows = "confused"
                    ch_e "Are you getting close here? I'm getting as little sore."   
        elif Cnt == (10 + E_Anal):
                    $ E_Brows = "angry"        
                    ch_e "I'm . . .getting . . .worn out. . . here, . . [E_Petname]."
                    menu:
                        ch_e "Can we. . . do something. . . else?"
                        "How about a BJ?" if E_Action and MultiAction:
                                if E_Anal >= 5 and E_Blow >= 10 and E_SEXP >= 50:
                                    $ Situation = "shift"
                                    call E_Doggy_AnalAfter
                                    call E_Blowjob      
                                else:
                                    ch_e "No thanks, [E_Petname]. Maybe a Handy instead?"
                                    $ Situation = "shift"
                                    call E_Doggy_AnalAfter
                                    call RHJ_Prep   
                        "How about a Handy?" if E_Action and MultiAction:
                                $ Situation = "shift"
                                call E_Doggy_AnalAfter
                                call E_Handjob     
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                jump E_Doggy_Anal_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Emma_Sex_Reset
                                $ Situation = "shift"
                                jump E_Doggy_AnalAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    call Statup("Emma", "Love", 200, -5)
                                    call Statup("Emma", "Obed", 50, 3)                    
                                    call Statup("Emma", "Obed", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call EmmaFace("angry", 1)   
                                    call Emma_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_e "Well if that's your attitude you can handle your own business."                         
                                    call Statup("Emma", "Love", 50, -3, 1)
                                    call Statup("Emma", "Love", 80, -4, 1)
                                    call Statup("Emma", "Obed", 30, -1, 1)                    
                                    call Statup("Emma", "Obed", 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_Doggy_AnalAfter
        #End Count check
   
        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    ch_e "Ok, [E_Petname], that's enough of that for now."
    
label E_Doggy_AnalAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Emma_Sex_Reset
        
    call EmmaFace("sexy") 
    
    $ E_Anal += 1  
    $ E_Action -=1
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1        
    call Statup("Emma", "Inbt", 30, 3) 
    call Statup("Emma", "Inbt", 70, 1) 
    
    if Partner == "Kitty":
        call Partner_Like("Emma",3,1)
    else:
        call Partner_Like("Emma",4,2)
    
    if "Emma Anal Addict" in Achievements:
            pass 
            
    elif E_Anal >= 10:
        $ E_SEXP += 7
        $ Achievements.append("Emma Anal Addict")
        if not Situation:
            call EmmaFace("bemused", 1)
            ch_e "I. . . really think I enjoy this. . ."                  
    elif E_Anal == 1:            
            $E_SEXP += 25        
            if not Situation: 
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "That was . . . interesting [E_Petname]. We'll have to do that again sometime."
                elif E_Obed <= 500 and P_Focus <= 20:
                    $ E_Mouth = "sad"
                    ch_e "Ouch."
                    ch_e "Did you get what you needed here?"
    elif E_Anal == 5:
            ch_e "We're making a regular habit of this."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in E_RecentActions:
            call EmmaFace("angry")
            $ E_Eyes = "side"
            ch_e  "Hmm, you seemed to get more out of that than me. . ."
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_e "Mmm, so what else did you have in mind?"
    call Checkout
    return   


# End R Doggy Anal //////////////////////////////////////////////////////////////////////////////////
    

  
# E_Doggy_A hotdog //////////////////////////////////////////////////////////////////////

label E_Doggy_H: 
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Emma")
    if E_Hotdog >= 3: #You've done it before several times
        $ Tempmod += 10
    elif E_Hotdog: #You've done it before
        $ Tempmod += 5    
    
    if E_Lust > 85:
        $ Tempmod += 10
    elif E_Lust > 75: #She's really horny
        $ Tempmod += 5
    if Situation == "shift":
        $ Tempmod += 10   
    if "exhibitionist" in E_Traits:
        $ Tempmod += (3*Taboo)  
    if "dating" in E_Traits or "sex friend" in E_Petnames:
        $ Tempmod += 10
    elif "ex" in E_Traits:
        $ Tempmod -= 40 
    if E_ForcedCount and not E_Forced:
        $ Tempmod -= 5 * E_ForcedCount 
    
    if Taboo and "tabno" in E_DailyActions:        
        $ Tempmod -= 10 
        
    if "no hotdog" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no hotdog" in E_RecentActions else 0      
        
    $ Approval = ApprovalCheck("Emma", 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)
    
    if Situation == "Emma":                                                                  #Emma auto-starts   
        if Approval > 2:                                                      # fix, add emma auto stuff here
            call Emma_Doggy_Launch("L") 
            "Emma turns and backs up against your cock, rubbing it against her ass."
            menu:
                "What do you do?"
                "Nothing.":                     
                    call Statup("Emma", "Inbt", 50, 3)
                    "Emma starts to grind against you."
                "Praise her.":       
                    call EmmaFace("sexy", 1)                    
                    call Statup("Emma", "Inbt", 80, 2) 
                    ch_p "Hmmm, that's good, [E_Pet]."
                    call Emma_Namecheck
                    "Emma starts to grind against you."
                    call Statup("Emma", "Love", 85, 1)
                    call Statup("Emma", "Obed", 60, 2)
                "Ask her to stop.":
                    call EmmaFace("surprised")       
                    call Statup("Emma", "Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [E_Pet]."
                    call Emma_Namecheck
                    "Emma pulls back."
                    call Statup("Emma", "Obed", 80, 1)
                    call Statup("Emma", "Obed", 30, 2)                    
                    return            
            jump E_Doggy_HotdogPrep
        else:                
            $ Tempmod = 0                               # fix, add emma auto stuff here
            $ Trigger2 = 0
        return            
    
    if Situation == "auto":   
        call Emma_Doggy_Launch("L")   
        "You press up against Emma's backside."    
        call EmmaFace("surprised", 1)
        
        if (E_Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
            "Emma is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            call EmmaFace("sexy")
            call Statup("Emma", "Obed", 70, 3)
            call Statup("Emma", "Inbt", 50, 3) 
            call Statup("Emma", "Inbt", 70, 1) 
            ch_e "Hmm, I've apparently got someone's attention. . ."            
            jump E_Doggy_HotdogPrep         
        else:                                                                                                            #she's questioning it
            $ E_Brows = "angry"                
            menu:
                ch_e "Hmm, kinda rude, [E_Petname]." 
                "Sorry, sorry! Never mind.":
                    if Approval:     
                        call EmmaFace("sexy", 1)
                        call Statup("Emma", "Obed", 70, 3)
                        call Statup("Emma", "Inbt", 50, 3) 
                        call Statup("Emma", "Inbt", 70, 1) 
                        ch_e "I guess it doesn't feel so bad. . ."
                        jump E_Doggy_HotdogPrep
                    "You pull back before you really get it in."                    
                    call EmmaFace("bemused", 1)
                    if E_Hotdog:
                        ch_e "Well ok, [E_Petname], it has been kinda fun." 
                    else:
                        ch_e "Well ok, [E_Petname], that's a bit dirty, maybe ask a girl?"                                               
                "You'll see.":                    
                    call Statup("Emma", "Love", 80, -10, 1)  
                    call Statup("Emma", "Love", 200, -8)
                    "You grind against her asscrack."                              
                    call Statup("Emma", "Obed", 70, 3)
                    call Statup("Emma", "Inbt", 50, 3) 
                    if not ApprovalCheck("Emma", 500, "O", TabM=1): #Checks if Obed is 700+  
                        call EmmaFace("angry")
                        "Emma shoves you away."
                        ch_e "Dick!"
                        ch_e "If that's how you want want to act, I'm out of here!"                                                  
                        call Statup("Emma", "Love", 50, -10, 1)                        
                        call Statup("Emma", "Obed", 50, 3)
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Emma_Sex_Reset
                        $ E_RecentActions.append("angry")
                        $ E_DailyActions.append("angry")                       
                    else:
                        call EmmaFace("sad")
                        "Emma doesn't seem to be into this, but she knows her place."                        
                        jump E_Doggy_HotdogPrep
        return             
    
   
    if not E_Hotdog and "no hotdog" not in E_RecentActions:                                                               #first time    
        call EmmaFace("surprised", 1)
        $ E_Mouth = "kiss"
        ch_e "Wait, so you want to grind against my butt?!"
  
        if E_Forced:
            call EmmaFace("sad")
            ch_e ". . . That's all?"
        
        
    if not E_Hotdog and Approval:                                                 #First time dialog        
        if E_Forced: 
            call EmmaFace("sad")
            call Statup("Emma", "Love", 70, -3, 1)
            call Statup("Emma", "Love", 20, -2, 1)
        elif E_Love >= (E_Obed + E_Inbt):
            call EmmaFace("sexy")
            $ E_Brows = "sad"
            $ E_Mouth = "smile" 
            ch_e "It looks like you need some relief. . ."           
        elif E_Obed >= E_Inbt:
            call EmmaFace("normal")
            ch_e "If that's what you need, [E_Petname]."
        elif E_Addict >= 50:
            call EmmaFace("manic", 1)
            ch_e "Hmmm. . ."
        else: # Uninhibited 
            call EmmaFace("sad")
            $ E_Mouth = "smile"             
            ch_e "Hmm, you look ready for it, at least. . ."    
            
    elif Approval:                                                                       #Second time+ dialog
        if E_Forced: 
            call EmmaFace("sad")
            call Statup("Emma", "Love", 70, -3, 1)
            call Statup("Emma", "Love", 20, -2, 1)
            ch_e "That's all you want?"  
        elif not Taboo and "tabno" in E_DailyActions:        
            ch_e "Well, at least you got us some privacy this time. . ."   
        elif "hotdog" in E_RecentActions:
            call EmmaFace("sexy", 1)
            ch_e "You want to go again? Ok."
            jump E_Doggy_HotdogPrep
        elif "hotdog" in E_DailyActions:
            call EmmaFace("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",                 
                "So you'd like another go?",                 
                "You can't stay away from this booty. . .", 
                "Are you sure that's all you want?"]) 
            ch_e "[Line]"
        elif E_Hotdog < 3:        
            call EmmaFace("sexy", 1)
            $ E_Brows = "confused"
            $ E_Mouth = "kiss"
            ch_e "So you'd like another go?"       
        else:       
            call EmmaFace("sexy", 1)
            $ Emma_Arms = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                "So you'd like another go?",                 
                "You can't stay away from this booty.", 
                "You want me to slick your pole?"]) 
            ch_e "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if E_Forced:
            call EmmaFace("sad")
            call Statup("Emma", "Obed", 80, 1)
            call Statup("Emma", "Inbt", 60, 1)
            ch_e "Ok, fine."    
        elif "no hotdog" in E_DailyActions:               
            ch_e "Well, I guess it's not so bad. . ."
        else:
            call EmmaFace("sexy", 1)
            call Statup("Emma", "Love", 80, 1)
            call Statup("Emma", "Inbt", 50, 2) 
            $ Line = renpy.random.choice(["Well, sure, give it a rub.",                 
                "Well. . . ok.",                 
                "Sure!", 
                "I guess we could do that.",
                "Hells yeah.",
                "Heh, ok, ok."]) 
            ch_e "[Line]"
            $ Line = 0
        call Statup("Emma", "Obed", 60, 1)
        call Statup("Emma", "Inbt", 70, 2) 
        jump E_Doggy_HotdogPrep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call EmmaFace("angry")
        if "no hotdog" in E_RecentActions:  
            ch_e "I {i}just{/i} told you \"no,\" [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no hotdog" in E_DailyActions: 
            ch_e "I told you that I didn't want you rubb'in up on me in public!" 
        elif "no hotdog" in E_DailyActions:       
            ch_e "I told you \"no\" earlier, [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "I told you that I didn't want you rubb'in up on me in public!"     
        elif not E_Hotdog:
            call EmmaFace("bemused")
            ch_e "That's kinda naughty, [E_Petname]. . ."
        else:
            call EmmaFace("bemused")
            ch_e "Not, right now [E_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no hotdog" in E_DailyActions:
                call EmmaFace("bemused")
                ch_e "Yeah, ok, [E_Petname]."              
                return
            "Maybe later?" if "no hotdog" not in E_DailyActions:
                call EmmaFace("sexy")  
                ch_e "Yeah, maybe, [E_Petname]."
                call Statup("Emma", "Love", 80, 1)
                call Statup("Emma", "Inbt", 50, 1)   
                if Taboo:                    
                    $ E_RecentActions.append("tabno")                      
                    $ E_DailyActions.append("tabno") 
                $ E_RecentActions.append("no hotdog")                      
                $ E_DailyActions.append("no hotdog")                          
                return
            "You might like it. . .":             
                if Approval:
                    call EmmaFace("sexy")     
                    call Statup("Emma", "Obed", 60, 2)
                    call Statup("Emma", "Inbt", 50, 2) 
                    $ Line = renpy.random.choice(["Well, sure, give it a rub.",     
                        "I suppose. . .", 
                        "You've got me there."]) 
                    ch_e "[Line]"
                    $ Line = 0                   
                    jump E_Doggy_HotdogPrep
                else:   
                    pass
                    
            "Bend over.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Emma", 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad")
                    call Statup("Emma", "Love", 70, -2, 1)
                    call Statup("Emma", "Love", 200, -2)                 
                    ch_e "Ok, fine. Whatever."  
                    call Statup("Emma", "Obed", 80, 4)
                    call Statup("Emma", "Inbt", 60, 2)  
                    $ E_Forced = 1  
                    jump E_Doggy_HotdogPrep
                else:                              
                    call Statup("Emma", "Love", 200, -10)     
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Emma_Arms = 1      
    
    if "no hotdog" in E_DailyActions:
        ch_e "I just don't want to, [E_Petname]."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    if E_Forced:
        call EmmaFace("angry", 1)
        ch_e "Even that's not worth it."
        call Statup("Emma", "Lust", 200, 5)  
        if E_Love > 300: 
                call Statup("Emma", "Love", 70, -1)
        call Statup("Emma", "Obed", 50, -1)  
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call EmmaFace("angry", 1)        
        $ E_RecentActions.append("tabno")                      
        $ E_DailyActions.append("tabno") 
        ch_e "I'd be a bit embarassed doing that here."  
        call Statup("Emma", "Lust", 200, 5)  
        call Statup("Emma", "Obed", 50, -3)  
    elif E_Hotdog:
        call EmmaFace("sad") 
        ch_e "Eh-eh, not anymore, [E_Petname]."
    else:
        call EmmaFace("normal", 1)
        ch_e "Not interested."    
    $ E_RecentActions.append("no hotdog")                      
    $ E_DailyActions.append("no hotdog") 
    $ Tempmod = 0    
    return

label E_Doggy_HotdogPrep:  
    call Seen_First_Peen("Emma",Partner)
    call Emma_Doggy_Launch("hotdog")
    
    if Situation != "auto":
        call Emma_Bottoms_Off    
        
        if Taboo: # Emma gets started. . .
            if E_Hotdog:                
                "Emma glances around to see if anyone notices what she's doing, then backs her ass up against your cock."
                
            else:         
                "Emma glances around for voyeurs. . ."
                "Emma hesitantly pulls down your pants and slowly backs up against your rigid member."
            $ E_Inbt += int(Taboo/10)  
            $ E_Lust += int(Taboo/5)
        else:    
            if not E_Hotdog:
                "Emma bends over and presses her backside against you suggestively."
            else:
                "Emma hesitantly pulls down your pants slowly backs up against your rigid member."
                     
    else: #if Situation == "auto"       
        "You press yourself against her ass."
        
    if not E_Hotdog:                                                      #First time stat buffs      
        if E_Forced:
            call Statup("Emma", "Love", 90, -5)
            call Statup("Emma", "Obed", 70, 20)
            call Statup("Emma", "Inbt", 80, 10) 
        else:
            call Statup("Emma", "Love", 90, 20)
            call Statup("Emma", "Obed", 70, 20)
            call Statup("Emma", "Inbt", 80, 20)  
    
            
    if Situation:    
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ Trigger = "hotdog"
    $ Speed = 1
    if Taboo:
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no hotdog")
    $ E_RecentActions.append("hotdog")                      
    $ E_DailyActions.append("hotdog") 

label E_Doggy_Hotdog_Cycle: #Repeating strokes  
    while Round >=0:  
        call Shift_Focus("Emma")
        call Emma_Doggy_Launch("hotdog") 
        call EmmaLust        
        $ P_Cock = "out"
        $ Trigger = "hotdog"
        
        if  P_Focus < 100:                                                    
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass
                        "Keep going. . . (locked)" if not Speed:
                                    pass
                                    
                        "Start moving? . ." if not Speed:
                                    $ Speed = 1                            
                        "Speed up. . ." if 0 < Speed < 3:                    
                                    $ Speed += 1
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass
                            
                        "Slow Down. . ." if Speed:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
                            
                        "Slap her ass":                     
                                    call E_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump E_Doggy_Hotdog_Cycle  
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                        
                        "Other options":
                                menu:   
                                    "Offhand action":
                                            if E_Action and MultiAction:
                                                call Emma_Offhand_Set
                                                if Trigger2:
                                                     $ E_Action -= 1
                                            else:
                                                ch_e "I'm actually getting a little tired, so maybe we could wrap this up?"  
                                                
                                    "Shift primary action":
                                            if E_Action and MultiAction:
                                                    menu:
                                                        "How about sex?":
                                                            $ Situation = "shift"
                                                            call E_Doggy_HotdogAfter
                                                            call E_Doggy_P
                                                        "Just stick it in her pussy [[without asking].":
                                                            $ Situation = "auto"
                                                            call E_Doggy_HotdogAfter
                                                            call E_Doggy_P
                                                        "How about anal?":
                                                            $ Situation = "shift"
                                                            call E_Doggy_HotdogAfter
                                                            call E_Doggy_A
                                                        "Just stick it in her ass [[without asking].":
                                                            $ Situation = "auto"
                                                            call E_Doggy_HotdogAfter
                                                            call E_Doggy_A
                                                        "Never Mind":
                                                                jump E_Doggy_Hotdog_Cycle
                                            else:
                                                ch_e "I'm actually getting a little tired, so maybe we could wrap this up?" 
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask Emma to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Emma_Les_Change
                                            "Ask Emma to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Emma")  
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0    
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Emma")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump E_Doggy_Hotdog_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump E_Doggy_Hotdog_Cycle 
                                            "Never mind":
                                                        jump E_Doggy_Hotdog_Cycle 
                                    "Undress Emma":
                                            call E_Undress   
                                    "Clean up Emma (locked)" if not E_Spunk:
                                            pass  
                                    "Clean up Emma" if E_Spunk:
                                            call Emma_Cleanup("ask")                                         
                                    "Never mind":
                                            jump E_Doggy_Hotdog_Cycle                                    
                                                        
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Emma_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_Doggy_HotdogAfter
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Emma_Sex_Reset
                                    $ Line = 0
                                    jump E_Doggy_HotdogAfter
        #End menu (if Line)              
        
        call Shift_Focus("Emma")  
        call Sex_Dialog("Emma",Partner)
        
        $ Cnt += 1
        $ Round -= 1     
        
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or E_Lust >= 100:   
                    #If either of you could cum    
                    if P_Focus >= 100:
                            #If you can cum:                                                
                            call PE_Cumming
                            if "angry" in E_RecentActions:  
                                call Emma_Sex_Reset
                                return    
                            call Statup("Emma", "Lust", 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                    $ E_RecentActions.append("unsatisfied")                      
                                    $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_Doggy_HotdogAfter 
                            $ Line = "came"

                    if E_Lust >= 100:         
                            #If you're still going at it and Emma can cum
                            call E_Cumming
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_Doggy_HotdogAfter
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump E_Doggy_HotdogAfter
                            elif "unsatisfied" in E_RecentActions:
                                #And Emma is unsatisfied,  
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if P_Semen:
                                        $ Line = "You get back into it" 
                                        jump E_Doggy_Hotdog_Cycle  
                                    "No, I'm done." if P_Semen:
                                        "You pull back."
                                        jump E_Doggy_HotdogAfter
                                    "No, I'm spent." if not P_Semen:
                                        "You pull back."
                                        jump E_Doggy_HotdogAfter        
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Emma")            
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
        elif Cnt == (5 + E_Hotdog):
                    $ E_Brows = "confused"
                    ch_e "Are you getting close here?"   
        elif Cnt == (10 + E_Hotdog):
                    $ E_Brows = "angry"        
                    menu:
                        ch_e "I'm kinda done with this, [E_Petname]."
                        "How about a BJ?" if E_Action and MultiAction:
                                $ Situation = "shift"
                                call E_Doggy_HotdogAfter
                                call E_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                jump E_Doggy_Hotdog_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Emma_Sex_Reset
                                $ Situation = "shift"
                                jump E_Doggy_HotdogAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    call Statup("Emma", "Love", 200, -5)
                                    call Statup("Emma", "Obed", 50, 3)                    
                                    call Statup("Emma", "Obed", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call EmmaFace("angry", 1)   
                                    call Emma_Sex_Reset
                                    "She scowls at you and pulls away."
                                    ch_e "Well if that's your attitude you can handle your own business."                         
                                    call Statup("Emma", "Love", 50, -3, 1)
                                    call Statup("Emma", "Love", 80, -4, 1)
                                    call Statup("Emma", "Obed", 30, -1, 1)                    
                                    call Statup("Emma", "Obed", 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_Doggy_HotdogAfter
        #End Count check
   
        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    ch_e "Ok, [E_Petname], that's enough of that for now."
    
label E_Doggy_HotdogAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Emma_Sex_Reset
        
    call EmmaFace("sexy") 
    
    $ E_Hotdog += 1  
    $ E_Action -=1
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1        
    call Statup("Emma", "Inbt", 30, 1) 
    call Statup("Emma", "Inbt", 70, 1) 
    
    call Partner_Like("Emma",1)
    
    if "Emma Full Buns" in Achievements:
            pass 
            
    elif E_Hotdog >= 10:
        $ E_SEXP += 5
        $ Achievements.append("Emma Full Buns")
        if not Situation:
            call EmmaFace("smile", 1)
            ch_e "I think I'm getting addicted to this."               
    elif E_Hotdog == 1:            
            $E_SEXP += 10        
            if not Situation: 
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "That was pretty hot, [E_Petname], we'll have to do that again sometime."
                elif E_Obed <= 500 and P_Focus <= 20:
                    $ E_Mouth = "sad"
                    ch_e "Did you get what you needed here?"
    elif E_Hotdog == 5:
            ch_e "This is. . . interesting."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in E_RecentActions:
            call EmmaFace("angry")
            $ E_Eyes = "side"
            ch_e "That didn't really do it for me. . ."
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_e "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# End R Doggy hotdogging //////////////////////////////////////////////////////////////////////////////////


            
image AssBase:                  #This is the base image, used in masks
    "images/EmmaDoggy/Emma_Doggy_Ass.png"

image Dildo_Animation:
    contains:
        "UI_Dildo"
        block: 
            ease 1 pos (100,300) #pos (0,50)
            ease 1 pos (100,400) #pos (0,0)
            repeat
    
image AssTest:
#    "Dildo_Animation"
    AlphaMask("Dildo_Animation", "AssBase")

