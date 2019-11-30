# Start R Doggy //////////////////////////////////////////////////////////////////////////////////
# K_Doggy_P //////////////////////////////////////////////////////////////////////

label K_Doggy_P:  
label K_Sex_P:  
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Kitty")
    if K_Sex >= 7: # She loves it
        $ Tempmod += 15
    elif K_Sex >= 3: #You've done it before several times
        $ Tempmod += 12
    elif K_Sex: #You've done it before
        $ Tempmod += 10    
        
    if K_Addict >= 75 and (K_CreamP + K_CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 20
    elif K_Addict >= 75:
        $ Tempmod += 15
        
    if K_Lust > 85:
        $ Tempmod += 10
    elif K_Lust > 75: #She's really horny
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 10 
    if "exhibitionist" in K_Traits:    
        $ Tempmod += (4*Taboo)      
    if "dating" in K_Traits or "sex friend" in K_Petnames:
        $ Tempmod += 10
    elif "ex" in K_Traits:
        $ Tempmod -= 40
    if K_ForcedCount and not K_Forced:
        $ Tempmod -= 5 * K_ForcedCount
    
    
        
    if Taboo and "tabno" in K_DailyActions:        
        $ Tempmod -= 10 
        
    if "no sex" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no sex" in K_RecentActions else 0                  
             
        
    $ Approval = ApprovalCheck("Kitty", 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)
            
    if Situation == "auto":   
        call Kitty_Doggy_Launch("L")   
        if K_Legs == "skirt":
            "You press up against Kitty's backside, sliding her skirt up as you go."
            $ K_Upskirt = 1
        elif K_Legs == "pants":
            "You press up against Kitty's backside, sliding her pants down as you do."                
            $ K_Legs = 0
        else:
            "You press up against Kitty's backside."
        $ K_SeenPanties = 1
        "You rub the tip of your cock against her moist slit."        
        call KittyFace("surprised", 1)
        
        if (K_Sex and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
            "Kitty is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            call KittyFace("sexy")
            call Statup("Kitty", "Obed", 70, 3)
            call Statup("Kitty", "Inbt", 50, 3) 
            call Statup("Kitty", "Inbt", 70, 1) 
            ch_k "Ok, [K_Petname], let's do this."            
            jump K_Doggy_SexPrep         
        else:                                                                                                            #she's questioning it
            $ K_Brows = "angry"                
            menu:
                ch_k "Hey, what do you think you're doing back there?!" 
                "Sorry, sorry! Never mind.":
                    if Approval:     
                        call KittyFace("sexy", 1)
                        call Statup("Kitty", "Obed", 70, 3)
                        call Statup("Kitty", "Inbt", 50, 3) 
                        call Statup("Kitty", "Inbt", 70, 1) 
                        ch_k "Well, since you're be'in so nice about it, I guess we can give it a go. . ."
                        jump K_Doggy_SexPrep
                    "You pull back before you really get it in."                    
                    call KittyFace("bemused", 1)
                    if K_Sex:
                        ch_k "Well ok, [K_Petname], no harm done. Just give me a little warning next time." 
                    else:
                        ch_k "Well ok, [K_Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."                                               
                "Just fucking.":                    
                    call Statup("Kitty", "Love", 80, -10, 1)  
                    call Statup("Kitty", "Love", 200, -10)
                    "You press inside some more."                              
                    call Statup("Kitty", "Obed", 70, 3)
                    call Statup("Kitty", "Inbt", 50, 3) 
                    if not ApprovalCheck("Kitty", 700, "O", TabM=1):   #Checks if Obed is 700+                          
                        call KittyFace("angry")
                        "Kitty shoves you away and slaps you in the face."
                        ch_k "Jackass!"
                        ch_k "If that's how you want to treat me, we're done here!"                                                  
                        call Statup("Kitty", "Love", 50, -10, 1)                        
                        call Statup("Kitty", "Obed", 50, 3)
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Kitty_Doggy_Reset
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")                    
                    else:
                        call KittyFace("sad")
                        "Kitty doesn't seem to be into this, you're lucky she's so obedient."                        
                        jump K_Doggy_SexPrep
        return             
    
   
    if not K_Sex and "no sex" not in K_RecentActions:                           #first time    
        call KittyFace("surprised", 1)
        $ K_Mouth = "kiss"
        ch_k "So, you'd like to take this to the next level? Actual sex? . . ."    
        if K_Forced:
            call KittyFace("sad")
            ch_k "You'd really take it that far?"
            
            
    if not K_Sex and Approval:                                                  #First time dialog        
        if K_Forced: 
            call KittyFace("sad")
            call Statup("Kitty", "Love", 70, -30, 1)
            call Statup("Kitty", "Love", 20, -20, 1)
        elif K_Love >= (K_Obed + K_Inbt):
            call KittyFace("sexy")
            $ K_Brows = "sad"
            $ K_Mouth = "smile" 
            ch_k "Well, I've never been able to do this before now, so this might be fun."            
        elif K_Obed >= K_Inbt:
            call KittyFace("normal")
            ch_k "If that's what you want, [K_Petname]. . ."            
        elif K_Addict >= 50:
            call KittyFace("manic", 1)
            ch_k "Well. . . I bet it would feel really good down there."
        else: # Uninhibited 
            call KittyFace("sad")
            $ K_Mouth = "smile"             
            ch_k "Hmm, I've always wanted to try it. . ."   
            
    elif Approval:                                                                       #Second time+ dialog        
        call KittyFace("sexy", 1)
        if K_Forced: 
            call KittyFace("sad")
            call Statup("Kitty", "Love", 70, -3, 1)
            call Statup("Kitty", "Love", 20, -2, 1)
            ch_k "That's really what you want?" 
        elif not Taboo and "tabno" in K_DailyActions:        
            ch_k "Well, at least you got us some privacy this time. . ."        
        elif "sex" in K_RecentActions:
            ch_k "You want to go again? Ok."
            jump K_Doggy_SexPrep
        elif "sex" in K_DailyActions:
            $ Line = renpy.random.choice(["Back again so soon?",                 
                "So you'd like another go?",                 
                "You can't stay away from this. . .", 
                "Didn't get enough earlier?",
                "You're going to wear me out."]) 
            ch_k "[Line]"
        elif K_Sex < 3:        
            $ K_Brows = "confused"
            $ K_Mouth = "kiss"
            ch_k "So you'd like another go?"       
        else:       
            $ Line = renpy.random.choice(["You want some of this action?",                 
                "So you'd like another go?",                 
                "You can't stay away from this. . .", 
                "You want me to ride your pole?",
                "You wanna dip your wick?"]) 
            ch_k "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if K_Forced:
            call KittyFace("sad")
            call Statup("Kitty", "Obed", 90, 1)
            call Statup("Kitty", "Inbt", 60, 1)
            ch_k "Ok, fine."  
        elif "no sex" in K_DailyActions:               
            ch_k "Ok, you've won me over on this one. . ."
        else:
            call KittyFace("sexy", 1)
            call Statup("Kitty", "Love", 90, 1)
            call Statup("Kitty", "Inbt", 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                "Well. . . ok.",                 
                "Sure!", 
                "I guess I could. . . stick it in.",
                "Hells yeah.",
                "Heh, ok, ok."]) 
            ch_k "[Line]"
            $ Line = 0
        call Statup("Kitty", "Obed", 20, 1)
        call Statup("Kitty", "Obed", 60, 1)
        call Statup("Kitty", "Inbt", 70, 2) 
        jump K_Doggy_SexPrep   
    
    else:                                                                               #She's not into it, but maybe. . .    
        call KittyFace("angry")       
        if "no sex" in K_RecentActions:  
            ch_k "I {i}just{/i} told you \"no,\" [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions and "no sex" in K_DailyActions:  
            ch_k "I already told you that I wouldn't bang you in public!" 
        elif "no sex" in K_DailyActions:       
            ch_k "I already told you \"no,\" [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "I already told you this is too public!"     
        elif not K_Sex:
            call KittyFace("bemused")
            ch_k "I just don't think I'm ready yet, [K_Petname]. . ."
        else:
            call KittyFace("bemused")
            ch_k "Not, right now [K_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no sex" in K_DailyActions:
                call KittyFace("bemused")
                ch_k "Yeah, ok, [K_Petname]."              
                return
            "Maybe later?" if "no sex" not in K_DailyActions:
                call KittyFace("sexy")  
                ch_k "I'll give it some thought, [K_Petname]."
                call Statup("Kitty", "Love", 80, 2)
                call Statup("Kitty", "Inbt", 70, 2)   
                if Taboo:                    
                    $ K_RecentActions.append("tabno")                      
                    $ K_DailyActions.append("tabno") 
                $ K_RecentActions.append("no sex")                      
                $ K_DailyActions.append("no sex")            
                return
            "I think you'd enjoy it as much as I would. . .":             
                if Approval:
                    call KittyFace("sexy")     
                    call Statup("Kitty", "Obed", 90, 2)
                    call Statup("Kitty", "Obed", 50, 2)
                    call Statup("Kitty", "Inbt", 70, 3) 
                    call Statup("Kitty", "Inbt", 40, 2) 
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                        "I suppose. . .", 
                        "You've got me there."]) 
                    ch_k "[Line]"
                    $ Line = 0                   
                    jump K_Doggy_SexPrep       
            "Bend over.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Kitty", 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
                if Approval > 1 or (Approval and K_Forced):
                    call KittyFace("sad")
                    call Statup("Kitty", "Love", 70, -5, 1)
                    call Statup("Kitty", "Love", 200, -5)                 
                    ch_k "Ok, fine. If we're going to do this, stick it in already."  
                    call Statup("Kitty", "Obed", 80, 4)
                    call Statup("Kitty", "Inbt", 80, 1) 
                    call Statup("Kitty", "Inbt", 60, 3)  
                    $ K_Forced = 1  
                    jump K_Doggy_SexPrep
                else:                          
                    call Statup("Kitty", "Love", 200, -20)   
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Kitty_Arms = 1  
    if "no sex" in K_DailyActions:
        ch_k "Learn to take \"no\" for an answer, [K_Petname]." 
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1)
        ch_k "I'm not doing that just because you have me over a barrel."
        call Statup("Kitty", "Lust", 200, 5)   
        if K_Love > 300: 
                call Statup("Kitty", "Love", 70, -2)
        call Statup("Kitty", "Obed", 50, -2)     
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call KittyFace("angry", 1)
        $ K_RecentActions.append("tabno")                      
        $ K_DailyActions.append("tabno") 
        ch_k "Even if I wanted to, it certainly wouldn't be here!"      
        call Statup("Kitty", "Lust", 200, 5)  
        call Statup("Kitty", "Obed", 50, -3)
    elif K_Sex:
        call KittyFace("sad") 
        ch_k "Maybe you could go fuck yourself instead."       
    else:
        call KittyFace("normal", 1)
        ch_k "No way."     
    $ K_RecentActions.append("no sex")                      
    $ K_DailyActions.append("no sex") 
    $ Tempmod = 0    
    return

label K_Doggy_SexPrep:
    call Seen_First_Peen("Kitty",Partner,React=Situation)
    call Kitty_Doggy_Launch("hotdog")
        
    if Situation == "Kitty":                                                                 
            #Rogue auto-starts   
            $ Situation = 0
            if K_Legs == "skirt":
                "Kitty turns and backs up against your cock, sliding her skirt up as she does so."
                $ K_Upskirt = 1
            elif K_Legs == "pants":
                "Kitty turns and backs up against your cock, sliding her pants down as she does so."    
                $ K_Upskirt = 1
            else:
                "Kitty turns and backs up against your cock."
            $ K_SeenPanties = 1
            "She slides the tip along her pussy and seems to want you to insert it."
            menu:
                "What do you do?"
                "Go with it.":                    
                    call Statup("Kitty", "Inbt", 80, 3) 
                    call Statup("Kitty", "Inbt", 50, 2)
                    "Kitty slides it in."
                "Praise her.":       
                    call KittyFace("sexy", 1)                    
                    call Statup("Kitty", "Inbt", 80, 3) 
                    ch_p "Oh yeah, [K_Pet], let's do this."
                    call Kitty_Namecheck
                    "Kitty slides it in."
                    call Statup("Kitty", "Love", 85, 1)
                    call Statup("Kitty", "Obed", 90, 1)
                    call Statup("Kitty", "Obed", 50, 2)
                "Ask her to stop.":
                    call KittyFace("surprised")       
                    call Statup("Kitty", "Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [K_Pet]."
                    call Kitty_Namecheck
                    "Kitty pulls back."
                    call Statup("Kitty", "Obed", 90, 1)
                    call Statup("Kitty", "Obed", 50, 1)
                    call Statup("Kitty", "Obed", 30, 2)
                    $ P_RecentActions.append("nope")      
                    call AnyWord("Kitty",1,"refused","refused")  
                    return      
            $ K_PantiesDown = 1  
            call Kitty_First_Bottomless(1)
            
    elif Situation != "auto":
            call Kitty_Bottoms_Off       
            
            
            if (K_Panties and not K_PantiesDown) or (K_Legs and not K_Upskirt) or HoseNum("Kitty") >= 6: #If she refuses to take off her pants but agreed to sex
                ch_k "Well, I guess some things are necessary, [K_Petname]."            
                if (K_Legs == "pants" and not K_Upskirt) and (K_Panties and not K_PantiesDown):
                    "She quickly pulls down her pants and drops her [K_Panties]."
                elif (K_Legs == "pants" and not K_Upskirt):
                    "She quickly pulls down her pants, exposing her bare ass."
                elif HoseNum("Kitty") >= 6 and (K_Panties and not K_PantiesDown):
                    "She quickly pulls down her [K_Hose] and drops her [K_Panties]."
                    $ K_Hose = 0
                elif HoseNum("Kitty") >= 6:
                    "She quickly pulls down her [K_Hose], exposing her bare ass."
                    $ K_Hose = 0
                elif (K_Panties and not K_PantiesDown):
                    "She quickly pulls down her [K_Panties]."  
                
            $ K_Upskirt = 1
            $ K_PantiesDown = 1       
            $ K_SeenPanties = 1
            call Kitty_First_Bottomless
            
            if Taboo: # Kitty gets started. . .
                if not K_Sex:
                    "Kitty glances around for voyeurs. . ."
                    "Kitty hesitantly pulls down your pants and slowly backs up against your rigid member."
                    "You guide it into place and slide it in."
                else:
                    "Kitty glances around to see if anyone notices what she's doing, then backs her ass up against your cock."
                    "You guide your cock into place and ram it home."
                $ K_Inbt += int(Taboo/10)  
                $ K_Lust += int(Taboo/5)
            else:    
                if not K_Sex:
                    "Kitty hesitantly pulls down your pants slowly backs up against your rigid member."
                    "You press her folds aside and nudge your cock in."
                else:
                    "Kitty bends over and presses her backside against you suggestively."
                    "You take careful aim and then ram your cock in."
            #end auto
                            
    else:  #if Situation == "auto"         
            if (K_Legs == "pants" and not K_Upskirt) and (K_Panties and not K_PantiesDown):
                "You quickly pull down her pants and her [K_Panties] and press against her slit."
            elif (K_Panties and not K_PantiesDown):
                "You quickly pull down her [K_Panties] and press against her slit."  
            $ K_Upskirt = 1
            $ K_PantiesDown = 1       
            $ K_SeenPanties = 1
            call Kitty_First_Bottomless(1)
            
    if not K_Sex:        
        if K_Forced:
            call Statup("Kitty", "Love", 90, -150)
            call Statup("Kitty", "Obed", 70, 60)
            call Statup("Kitty", "Inbt", 80, 50) 
        else:
            call Statup("Kitty", "Love", 90, 30)
            call Statup("Kitty", "Obed", 70, 30)
            call Statup("Kitty", "Inbt", 80, 60) 
    
    if Situation:   
        $ renpy.pop_call() 
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ P_Cock = "in"
    $ Trigger = "sex"
    $ Speed = 1
    if Taboo:
        call DrainWord("Kitty","tabno")
    call DrainWord("Kitty","no sex")
    $ K_RecentActions.append("sex")                      
    $ K_DailyActions.append("sex") 

label K_Doggy_Sex_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Kitty")
        call Kitty_Doggy_Launch("sex") 
        call KittyLust        
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
                                    call K_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump K_Doggy_Sex_Cycle  
                                    
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
                                            if K_Action and MultiAction:
                                                call Kitty_Offhand_Set
                                                if Trigger2:
                                                     $ K_Action -= 1
                                            else:
                                                ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"  
                                                
                                    "Shift primary action":
                                            if K_Action and MultiAction:
                                                    menu:
                                                        "How about anal?":
                                                                $ Situation = "shift"
                                                                call K_Doggy_SexAfter
                                                                call K_Doggy_A
                                                        "Just stick it in her ass [[without asking].":
                                                                $ Situation = "auto"
                                                                call K_Doggy_SexAfter
                                                                call K_Doggy_A
                                                        "Pull back to hotdog her.":
                                                                $ Situation = "pullback"
                                                                call K_Doggy_SexAfter
                                                                call K_Doggy_H
                                                        "Never Mind":
                                                                jump K_Doggy_Sex_Cycle
                                            else:
                                                ch_k "I'm actually getting a little tired, so maybe we could wrap this up?" 
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:  
                                        menu:
                                            "Ask Kitty to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Kitty_Les_Change
                                            "Ask Kitty to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Kitty")  
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0    
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Kitty")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump K_Doggy_Sex_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump K_Doggy_Sex_Cycle 
                                            "Never mind":
                                                        jump K_Doggy_Sex_Cycle 
                                    "Undress Kitty":
                                            call K_Undress   
                                    "Clean up Kitty (locked)" if not K_Spunk:
                                            pass  
                                    "Clean up Kitty" if K_Spunk:
                                            call Kitty_Cleanup("ask")                                         
                                    "Never mind":
                                            jump K_Doggy_Sex_Cycle                                    
                                                        
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Kitty_Doggy_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump K_Doggy_SexAfter
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Kitty_Doggy_Reset
                                    $ Line = 0
                                    jump K_Doggy_SexAfter
        #End menu (if Line)              
        
        call Shift_Focus("Kitty")
        call Sex_Dialog("Kitty",Partner)
        
        $ Cnt += 1
        $ Round -= 1        
        $ P_Wet = 1 #wets penis
        $ P_Spunk = 0 if (P_Spunk and "in" not in K_Spunk) else P_Spunk #cleans you off after one cycle
        
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or K_Lust >= 100:   
                    #If either of you could cum    
                    if P_Focus >= 100:
                            #If you can cum:                                                
                            call PK_Cumming
                            if "angry" in K_RecentActions:  
                                call Kitty_Doggy_Reset
                                return    
                            call Statup("Kitty", "Lust", 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                    $ K_RecentActions.append("unsatisfied")                      
                                    $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump K_Doggy_SexAfter 
                            $ Line = "came"

                    if K_Lust >= 100:         
                            #If you're still going at it and Kitty can cum
                            call K_Cumming
                            if Situation == "shift" or "angry" in K_RecentActions:
                                jump K_Doggy_SexAfter
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump K_Doggy_SexAfter
                            elif "unsatisfied" in K_RecentActions:
                                #And Kitty is unsatisfied,  
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if P_Semen:
                                        $ Line = "You get back into it" 
                                        jump K_Doggy_Sex_Cycle  
                                    "No, I'm done." if P_Semen:
                                        "You pull back."
                                        jump K_Doggy_SexAfter
                                    "No, I'm spent." if not P_Semen:
                                        "You pull back."
                                        jump K_Doggy_SexAfter        
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Kitty")            
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if K_SEXP >= 100 or ApprovalCheck("Kitty", 1200, "LO"):
            pass
        elif Cnt == (5 + K_Sex):
                    $ K_Brows = "confused"
                    ch_k "Are you getting close here? I'm getting as little sore."   
        elif Cnt == (10 + K_Sex):
                    $ K_Brows = "angry"        
                    ch_k "I'm . . .getting . . .worn out. . . here, . . [K_Petname]."
                    menu:
                        ch_k "Can we. . . do something. . . else?"
                        "How about a BJ?" if K_Action and MultiAction:
                                $ Situation = "shift"
                                call K_Doggy_SexAfter
                                call K_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                jump K_Doggy_Sex_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Kitty_Doggy_Reset
                                $ Situation = "shift"
                                jump K_Doggy_SexAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                                    call Statup("Kitty", "Love", 200, -5)
                                    call Statup("Kitty", "Obed", 50, 3)                    
                                    call Statup("Kitty", "Obed", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call KittyFace("angry", 1)   
                                    call Kitty_Doggy_Reset
                                    "She scowls at you and pulls out."
                                    ch_k "Well if that's your attitude you can handle your own business."                         
                                    call Statup("Kitty", "Love", 50, -3, 1)
                                    call Statup("Kitty", "Love", 80, -4, 1)
                                    call Statup("Kitty", "Obed", 30, -1, 1)                    
                                    call Statup("Kitty", "Obed", 50, -1, 1)  
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump K_Doggy_SexAfter
        #End Count check
   
        call Escalation("Kitty","R") #sees if she wants to escalate things
        
        if Round == 10:
            ch_k "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_k "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0)
    $ Line = 0
    ch_k "Ok, [K_Petname], that's enough of that for now."
    
label K_Doggy_SexAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Kitty_Doggy_Reset
        
    call KittyFace("sexy") 
    
    $ K_Sex += 1  
    $ K_Action -=1
    $ K_Addictionrate += 1
    if "addictive" in P_Traits:
        $ K_Addictionrate += 1        
    call Statup("Kitty", "Inbt", 30, 2) 
    call Statup("Kitty", "Inbt", 70, 1) 
    
    call Partner_Like("Kitty",3,2)
    
    if "Kitty Sex Addict" in Achievements:
            pass 
            
    elif K_Sex >= 10:
        $ K_SEXP += 5
        $ Achievements.append("Kitty Sex Addict")
        if not Situation:
            call KittyFace("smile", 1)
            ch_k "I think I'm getting addicted to this."               
    elif K_Sex == 1:            
            $K_SEXP += 20        
            if not Situation: 
                if K_Love >= 500 and "unsatisfied" not in K_RecentActions:
                    ch_k "That was really great, [K_Petname], we'll have to do that again sometime."
                elif K_Obed <= 500 and P_Focus <= 20:
                    $ K_Mouth = "sad"
                    ch_k "Did you get what you needed here?"
    elif K_Sex == 5:
            ch_k "We're making a regular habit of this."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in K_RecentActions:
            call KittyFace("angry")
            $ K_Eyes = "side"
            ch_k "I didn't exactly get off there. . ."
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_k "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# End R Doggy //////////////////////////////////////////////////////////////////////////////////


# K_Doggy_A anal //////////////////////////////////////////////////////////////////////

label K_Doggy_A:
label K_Sex_A:  
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Kitty")
    if K_Anal >= 7: # She loves it
        $ Tempmod += 20   
    elif K_Anal >= 3: #You've done it before several times
        $ Tempmod += 17
    elif K_Anal: #You've done it before
        $ Tempmod += 15 
        
    if K_Addict >= 75 and (K_CreamP + K_CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 25
    elif K_Addict >= 75: 
        $ Tempmod += 15
    
    if K_Lust > 85:
        $ Tempmod += 10
    elif K_Lust > 75: #She's really horny
        $ Tempmod += 5
        
    if K_Loose:
        $ Tempmod += 10  
    elif "anal" in K_RecentActions:
        $ Tempmod -= 20 
    elif "anal" in K_DailyActions:
        $ Tempmod -= 10
        
    if Situation == "shift":
        $ Tempmod += 10    
    if "exhibitionist" in K_Traits:
        $ Tempmod += (5*Taboo) 
        
    if "dating" in K_Traits or "sex friend" in K_Petnames:
        $ Tempmod += 10      
    elif "ex" in K_Traits:
        $ Tempmod -= 40  
    if K_ForcedCount and not K_Forced:
        $ Tempmod -= 5 * K_ForcedCount
        
    if Taboo and "tabno" in K_DailyActions:        
        $ Tempmod -= 10 
    if "no anal" in K_DailyActions:               
        $ Tempmod -= 5         
        $ Tempmod -= 10 if "no anal" in K_RecentActions else 0  
            
    $ Approval = ApprovalCheck("Kitty", 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)
    
    if Situation == "auto":   
        call Kitty_Doggy_Launch("L")   
        if K_Legs == "skirt":
            "You press up against Kitty's backside, sliding her skirt up as you go."
            $ K_Upskirt = 1
        elif K_Legs == "pants":
            "You press up against Kitty's backside, sliding her pants down as you do."                
            $ K_Legs = 0
        else:
            "You press up against Kitty's backside."
        $ K_SeenPanties = 1
        "You press the tip of your cock against her tight rim."        
        call KittyFace("surprised", 1)
        
        if (K_Anal and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
            "Kitty is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            call KittyFace("sexy")
            call Statup("Kitty", "Obed", 70, 3)
            call Statup("Kitty", "Inbt", 50, 3) 
            call Statup("Kitty", "Inbt", 70, 1) 
            ch_k "Hmm, stick it in. . ."            
            jump K_Doggy_AnalPrep         
        else:                                                                                                            #she's questioning it
            $ K_Brows = "angry"                
            menu:
                ch_k "Hey, what do you think you're doing back there?!" 
                "Sorry, sorry! Never mind.":
                    if Approval:     
                        call KittyFace("sexy", 1)
                        call Statup("Kitty", "Obed", 70, 3)
                        call Statup("Kitty", "Inbt", 50, 3) 
                        call Statup("Kitty", "Inbt", 70, 1) 
                        ch_k "I guess if you really want to try it. . ."
                        jump K_Doggy_AnalPrep
                    "You pull back before you really get it in."                    
                    call KittyFace("bemused", 1)
                    if K_Anal:
                        ch_k "Well ok, [K_Petname], no harm done. Just give me a little warning next time." 
                    else:
                        ch_k "Well ok, [K_Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."                                               
                "Just fucking.":                    
                    call Statup("Kitty", "Love", 80, -10, 1)  
                    call Statup("Kitty", "Love", 200, -8)
                    "You press into her."                              
                    call Statup("Kitty", "Obed", 70, 3)
                    call Statup("Kitty", "Inbt", 50, 3) 
                    if not ApprovalCheck("Kitty", 700, "O", TabM=1):                        
                        call KittyFace("angry")
                        "Kitty shoves you away and slaps you in the face."
                        ch_k "Jackass!"
                        ch_k "If that's how you want to treat me, we're done here!"                                                  
                        call Statup("Kitty", "Love", 50, -10, 1)                        
                        call Statup("Kitty", "Obed", 50, 3)
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Kitty_Doggy_Reset
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")                        
                    else:
                        call KittyFace("sad")
                        "Kitty doesn't seem to be into this, you're lucky she's so obedient."                        
                        jump K_Doggy_AnalPrep
        return             
    
   
    if not K_Anal and "no anal" not in K_RecentActions:                                                               #first time    
        call KittyFace("surprised", 1)
        $ K_Mouth = "kiss"
        ch_k "Wait, so you want to stick it in my butt?!"
  
        if K_Forced:
            call KittyFace("sad")
            ch_k "Seriously?"
        
    if not K_Loose and ("dildo anal" in K_DailyActions or "anal" in K_DailyActions):
        call KittyFace("bemused", 1)
        ch_k "I'm still a little sore from earlier."
            
    elif "anal" in K_RecentActions:
        call KittyFace("sexy", 1)
        ch_k "You want to go again? Ok."
        jump K_Doggy_AnalPrep
        
    
    if not K_Anal and Approval:                                                 #First time dialog        
        if K_Forced: 
            call KittyFace("sad")
            call Statup("Kitty", "Love", 70, -3, 1)
            call Statup("Kitty", "Love", 20, -2, 1)
        elif K_Love >= (K_Obed + K_Inbt):
            call KittyFace("sexy")
            $ K_Brows = "sad"
            $ K_Mouth = "smile" 
            ch_k "I guess if you really want to try it. . ."           
        elif K_Obed >= K_Inbt:
            call KittyFace("normal")
            ch_k "Ok, [K_Petname], I'm ready."
        elif K_Addict >= 50:
            call KittyFace("manic", 1)
            ch_k "Well. . . I bet it would feel really good down there."
        else: # Uninhibited 
            call KittyFace("sad")
            $ K_Mouth = "smile"             
            ch_k "Hmm, it has been on my list. . ."  
    
    elif Approval:                                                                       #Second time+ dialog
        if K_Forced: 
            call KittyFace("sad")
            call Statup("Kitty", "Love", 70, -3, 1)
            call Statup("Kitty", "Love", 20, -2, 1)
            ch_k "That's really what you want?"
        elif not Taboo and "tabno" in K_DailyActions:        
            ch_k "Well, at least you got us some privacy this time. . ."   
        elif "anal" in K_DailyActions and not K_Loose:
            pass      
        elif "anal" in K_RecentActions:
            ch_k "I think I'm warmed up. . ."
            jump K_Doggy_AnalPrep
        elif "anal" in K_DailyActions:
            call KittyFace("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",                 
                "So you'd like another go?",                 
                "I'm still a little sore from earlier.", 
                "Didn't get enough earlier?",
                "You're going to wear me out."]) 
            ch_k "[Line]"
        elif K_Anal < 3:        
            call KittyFace("sexy", 1)
            $ K_Brows = "confused"
            $ K_Mouth = "kiss"
            ch_k "So you'd like another go?"       
        else:       
            call KittyFace("sexy", 1)
            $ Kitty_Arms = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                "So you'd like another go?",                 
                "You can't stay away from this booty.", 
                "You want me to ride your pole?",
                "You wanna dip your wick?"]) 
            ch_k "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if K_Forced:
            call KittyFace("sad")
            call Statup("Kitty", "Obed", 90, 1)
            call Statup("Kitty", "Inbt", 60, 1)
            ch_k "Ok, fine."   
        elif "no anal" in K_DailyActions:               
            ch_k "Ok, ok, I have been itching for this. . ." 
        else:
            call KittyFace("sexy", 1)
            call Statup("Kitty", "Love", 90, 1)
            call Statup("Kitty", "Inbt", 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                "Well. . . ok.",                 
                "Sure!", 
                "I guess I could. . . stick it in.",
                "Hells yeah.",
                "Heh, ok, ok."]) 
            ch_k "[Line]"
            $ Line = 0
        call Statup("Kitty", "Obed", 20, 1)
        call Statup("Kitty", "Obed", 60, 1)
        call Statup("Kitty", "Inbt", 70, 2) 
        jump K_Doggy_AnalPrep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call KittyFace("angry")
        if "no anal" in K_RecentActions:  
            ch_k "What part of \"no,\" did you not get, [K_Petname]?"
        elif Taboo and "tabno" in K_DailyActions and "no anal" in K_DailyActions:
            ch_k "I already told you that I wouldn't do that out here!"  
        elif "no anal" in K_DailyActions:       
            ch_k "I already told you \"no,\" [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "I already told you that I wouldn't do that out here!"  
        elif not K_Anal:
            call KittyFace("bemused")
            ch_k "I'm just not into that, [K_Petname]. . ."
        elif not K_Loose and "anal" not in K_DailyActions:
            call KittyFace("perplexed")
            ch_k "You could have been a bit more gentle last time, [K_Petname]. . ."
        else:
            call KittyFace("bemused")
            ch_k "Not, right now [K_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no anal" in K_DailyActions:
                call KittyFace("bemused")
                ch_k "Yeah, ok, [K_Petname]."              
                return
            "Maybe later?" if "no anal" not in K_DailyActions:
                call KittyFace("sexy")  
                ch_k "I'll give it some thought, [K_Petname]."
                call Statup("Kitty", "Love", 80, 2)
                call Statup("Kitty", "Inbt", 70, 2)  
                if Taboo:                    
                    $ K_RecentActions.append("tabno")                      
                    $ K_DailyActions.append("tabno") 
                $ K_RecentActions.append("no anal")                      
                $ K_DailyActions.append("no anal") 
                return
            "I bet it would feel really good. . .":             
                if Approval:
                    call KittyFace("sexy")     
                    call Statup("Kitty", "Obed", 90, 2)
                    call Statup("Kitty", "Obed", 50, 2)
                    call Statup("Kitty", "Inbt", 70, 3) 
                    call Statup("Kitty", "Inbt", 40, 2) 
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                        "I suppose. . .", 
                        "You've got me there."]) 
                    ch_k "[Line]"
                    $ Line = 0                   
                    jump K_Doggy_AnalPrep
                else:   
                    pass
                    
            "Bend over.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Kitty", 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                if Approval > 1 or (Approval and K_Forced):
                    call KittyFace("sad")
                    call Statup("Kitty", "Love", 70, -5, 1)
                    call Statup("Kitty", "Love", 200, -5)                 
                    ch_k "Ok, fine. If we're going to do this, stick it in already."  
                    call Statup("Kitty", "Obed", 80, 4)
                    call Statup("Kitty", "Inbt", 80, 1) 
                    call Statup("Kitty", "Inbt", 60, 3)  
                    $ K_Forced = 1  
                    jump K_Doggy_AnalPrep
                else:                              
                    call Statup("Kitty", "Love", 200, -20)    
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Kitty_Arms = 1  
    if "no anal" in K_DailyActions:
        ch_k "Learn to take \"no\" for an answer, [K_Petname]."   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1)
        ch_k "That's a bit much, even for you."
        call Statup("Kitty", "Lust", 200, 5)       
        if K_Love > 300: 
                call Statup("Kitty", "Love", 70, -2)
        call Statup("Kitty", "Obed", 50, -2)    
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call KittyFace("angry", 1)
        $ K_RecentActions.append("tabno")                      
        $ K_DailyActions.append("tabno") 
        ch_k "That you would even suggest such a thing in a place like this. . ."    
        call Statup("Kitty", "Lust", 200, 5)  
        call Statup("Kitty", "Obed", 50, -3) 
    elif not K_Loose and "anal" in K_DailyActions:
        call KittyFace("bemused")
        ch_k "Sorry, I just need a little break back there, [K_Petname]."    
    elif K_Anal:
        call KittyFace("sad") 
        ch_k "The only thing you can do with my ass is kiss it, [K_Petname]."
        ch_k ". . .Don't get any ideas."   
    else:
        call KittyFace("normal", 1)
        ch_k "Not happening."    
    $ K_RecentActions.append("no anal")                      
    $ K_DailyActions.append("no anal") 
    $ Tempmod = 0    
    return

label K_Doggy_AnalPrep:    
    call Seen_First_Peen("Kitty",Partner,React=Situation)            
    call Kitty_Doggy_Launch("hotdog")
    
    if Situation == "Kitty":                                                                  
            #Rogue auto-starts  
            $ Situation = 0  
            if K_Legs == "skirt":
                "Kitty turns and backs up against your cock, sliding her skirt up as she does so."
                $ K_Upskirt = 1
            elif K_Legs == "pants":
                "Kitty turns and backs up against your cock, sliding her pants down as she does so."                
                $ K_Upskirt = 1
            else:
                "Kitty turns and backs up against your cock."
            $ K_SeenPanties = 1
            "She slides the tip up to her anus, and presses against it."
            menu:
                "What do you do?"
                "Go with it.":                    
                    call Statup("Kitty", "Inbt", 80, 3) 
                    call Statup("Kitty", "Inbt", 50, 2)
                    "Kitty slides it in."
                "Praise her.":       
                    call KittyFace("sexy", 1)                    
                    call Statup("Kitty", "Inbt", 80, 3) 
                    ch_p "Ooo, dirty girl, [K_Pet], let's do this."
                    call Kitty_Namecheck
                    "Kitty slides it in."
                    call Statup("Kitty", "Love", 85, 1)
                    call Statup("Kitty", "Obed", 90, 1)
                    call Statup("Kitty", "Obed", 50, 2)
                "Ask her to stop.":
                    call KittyFace("surprised")       
                    call Statup("Kitty", "Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [K_Pet]."
                    call Kitty_Namecheck
                    "Kitty pulls back."
                    call Statup("Kitty", "Obed", 90, 1)
                    call Statup("Kitty", "Obed", 50, 1)
                    call Statup("Kitty", "Obed", 30, 2)   
                    $ P_RecentActions.append("nope")      
                    call AnyWord("Kitty",1,"refused","refused")                    
                    return   
            $ K_PantiesDown = 1   
            call Kitty_First_Bottomless(1)  
    
    elif Situation != "auto":
            call Kitty_Bottoms_Off        
            if (K_Panties and not K_PantiesDown) or (K_Legs and not K_Upskirt) or HoseNum("Kitty") >= 6: #If she refuses to take off her pants but agreed to sex
                ch_k "Well, I guess some things are necessary, [K_Petname]."            
                if (K_Legs == "pants" and not K_Upskirt) and (K_Panties and not K_PantiesDown):
                    "She quickly pulls down her pants and drops her [K_Panties]."
                elif (K_Legs == "pants" and not K_Upskirt):
                    "She quickly pulls down her pants, exposing her bare ass."
                elif HoseNum("Kitty") >= 6 and (K_Panties and not K_PantiesDown):
                    "She quickly pulls down her [K_Hose] and drops her [K_Panties]."
                    $ K_Hose = 0
                elif HoseNum("Kitty") >= 6:
                    "She quickly pulls down her [K_Hose], exposing her bare ass."
                    $ K_Hose = 0
                elif (K_Panties and not K_PantiesDown):
                    "She quickly pulls down her [K_Panties]."    
                
            $ K_Upskirt = 1
            $ K_PantiesDown = 1       
            $ K_SeenPanties = 1
            call Kitty_First_Bottomless
            
            if Taboo: # Kitty gets started. . .
                if K_Anal:                
                    "Kitty glances around to see if anyone notices what she's doing, then backs her ass up against your cock."
                    "You guide your cock into place and ram it home."   
                    
                else:         
                    "Kitty glances around for voyeurs. . ."
                    "Kitty hesitantly pulls down your pants and slowly backs up against your rigid member."
                    "You guide it into place and slide it in."
                $ K_Inbt += int(Taboo/10)  
                $ K_Lust += int(Taboo/5)
            else:    
                if not K_Anal:
                    "Kitty bends over and presses her backside against you suggestively."
                    "You take careful aim and then push your cock in."
                else:
                    "Kitty hesitantly pulls down your pants slowly backs up against your rigid member."
                    "You press against her rim and nudge your cock in."
            #end auto
                     
    else: #if Situation == "auto"               
            if (K_Legs == "pants" and not K_Upskirt) and (K_Panties and not K_PantiesDown):
                "You quickly pull down her pants and her [K_Panties] and press against her ass."
            elif (K_Panties and not K_PantiesDown):
                "You quickly pull down her [K_Panties] and press against her ass."  
                
            $ K_Upskirt = 1
            $ K_PantiesDown = 1       
            $ K_SeenPanties = 1
            call Kitty_First_Bottomless(1)
    
    if not K_Anal:                                                      #First time stat buffs       
        if K_Forced:
            call Statup("Kitty", "Love", 90, -150)
            call Statup("Kitty", "Obed", 70, 70)
            call Statup("Kitty", "Inbt", 80, 40) 
        else:
            call Statup("Kitty", "Love", 90, 10)
            call Statup("Kitty", "Obed", 70, 30)
            call Statup("Kitty", "Inbt", 80, 70) 
    elif not K_Loose:                                                   #first few times stat buffs       
        if K_Forced:
            call Statup("Kitty", "Love", 90, -20)
            call Statup("Kitty", "Obed", 70, 10)
            call Statup("Kitty", "Inbt", 80, 5) 
        else:
            call Statup("Kitty", "Obed", 70, 7)
            call Statup("Kitty", "Inbt", 80, 5) 
                
    if Situation:    
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ P_Cock = "anal"
    $ Trigger = "anal"
    $ Speed = 1
    if Taboo:
        call DrainWord("Kitty","tabno")
    call DrainWord("Kitty","no anal")
    $ K_RecentActions.append("anal")                      
    $ K_DailyActions.append("anal") 

label K_Doggy_Anal_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Kitty")
        call Kitty_Doggy_Launch("anal") 
        call KittyLust        
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
                                    call K_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump K_Doggy_Anal_Cycle  
                                    
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
                                            if K_Action and MultiAction:
                                                call Kitty_Offhand_Set
                                                if Trigger2:
                                                     $ K_Action -= 1
                                            else:
                                                ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"  
                                                
                                    "Shift primary action":
                                            if K_Action and MultiAction:
                                                    menu:
                                                        "How about sex?":
                                                                $ Situation = "shift"
                                                                call K_Doggy_AnalAfter
                                                                call K_Doggy_P
                                                        "Just stick it in her pussy [[without asking].":
                                                                $ Situation = "auto"
                                                                call K_Doggy_AnalAfter
                                                                call K_Doggy_P
                                                        "Pull back to hotdog her.":
                                                                $ Situation = "pullback"
                                                                call K_Doggy_AnalAfter
                                                                call K_Doggy_H
                                                        "Never Mind":
                                                                jump K_Doggy_Anal_Cycle
                                            else:
                                                ch_k "I'm actually getting a little tired, so maybe we could wrap this up?" 
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:  
                                        menu:
                                            "Ask Kitty to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Kitty_Les_Change
                                            "Ask Kitty to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Kitty")  
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0    
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Kitty")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump K_Doggy_Anal_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump K_Doggy_Anal_Cycle 
                                            "Never mind":
                                                        jump K_Doggy_Anal_Cycle 
                                    "Undress Kitty":
                                            call K_Undress   
                                    "Clean up Kitty (locked)" if not K_Spunk:
                                            pass  
                                    "Clean up Kitty" if K_Spunk:
                                            call Kitty_Cleanup("ask")                                         
                                    "Never mind":
                                            jump K_Doggy_Anal_Cycle                                    
                                                        
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Kitty_Doggy_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump K_Doggy_AnalAfter
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Kitty_Doggy_Reset
                                    $ Line = 0
                                    jump K_Doggy_AnalAfter
        #End menu (if Line)              
        
        call Shift_Focus("Kitty")
        call Sex_Dialog("Kitty",Partner)
        
        $ Cnt += 1
        $ Round -= 1     
        
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or K_Lust >= 100:   
                    #If either of you could cum    
                    if P_Focus >= 100:
                            #If you can cum:                                                
                            call PK_Cumming
                            if "angry" in K_RecentActions:  
                                call Kitty_Doggy_Reset
                                return    
                            call Statup("Kitty", "Lust", 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                    $ K_RecentActions.append("unsatisfied")                      
                                    $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump K_Doggy_AnalAfter 
                            $ Line = "came"

                    if K_Lust >= 100:         
                            #If you're still going at it and Kitty can cum
                            call K_Cumming
                            if Situation == "shift" or "angry" in K_RecentActions:
                                jump K_Doggy_AnalAfter
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump K_Doggy_AnalAfter
                            elif "unsatisfied" in K_RecentActions:
                                #And Kitty is unsatisfied,  
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if P_Semen:
                                        $ Line = "You get back into it" 
                                        jump K_Doggy_Anal_Cycle  
                                    "No, I'm done." if P_Semen:
                                        "You pull back."
                                        jump K_Doggy_AnalAfter
                                    "No, I'm spent." if not P_Semen:
                                        "You pull back."
                                        jump K_Doggy_AnalAfter        
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Kitty")            
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if K_SEXP >= 100 or ApprovalCheck("Kitty", 1200, "LO"):
            pass
        elif Cnt == (5 + K_Anal):
                    $ K_Brows = "confused"
                    ch_k "Are you getting close here? I'm getting as little sore."   
        elif Cnt == (10 + K_Anal):
                    $ K_Brows = "angry"        
                    ch_k "I'm . . .getting . . .worn out. . . here, . . [K_Petname]."
                    menu:
                        ch_k "Can we. . . do something. . . else?"
                        "How about a BJ?" if K_Action and MultiAction:
                                if K_Anal >= 5 and K_Blow >= 10 and K_SEXP >= 50:
                                    $ Situation = "shift"
                                    call K_Doggy_AnalAfter
                                    call K_Blowjob      
                                else:
                                    ch_k "No thanks, [K_Petname]. Maybe a Handy instead?"
                                    $ Situation = "shift"
                                    call K_Doggy_AnalAfter
                                    call RHJ_Prep   
                        "How about a Handy?" if K_Action and MultiAction:
                                $ Situation = "shift"
                                call K_Doggy_AnalAfter
                                call K_Handjob     
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                jump K_Doggy_Anal_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Kitty_Doggy_Reset
                                $ Situation = "shift"
                                jump K_Doggy_AnalAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                                    call Statup("Kitty", "Love", 200, -5)
                                    call Statup("Kitty", "Obed", 50, 3)                    
                                    call Statup("Kitty", "Obed", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call KittyFace("angry", 1)   
                                    call Kitty_Doggy_Reset
                                    "She scowls at you and pulls out."
                                    ch_k "Well if that's your attitude you can handle your own business."                         
                                    call Statup("Kitty", "Love", 50, -3, 1)
                                    call Statup("Kitty", "Love", 80, -4, 1)
                                    call Statup("Kitty", "Obed", 30, -1, 1)                    
                                    call Statup("Kitty", "Obed", 50, -1, 1)  
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump K_Doggy_AnalAfter
        #End Count check
   
        if Round == 10:
            ch_k "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_k "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0)
    $ Line = 0
    ch_k "Ok, [K_Petname], that's enough of that for now."
    
label K_Doggy_AnalAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Kitty_Doggy_Reset
        
    call KittyFace("sexy") 
    
    $ K_Anal += 1  
    $ K_Action -=1
    $ K_Addictionrate += 1
    if "addictive" in P_Traits:
        $ K_Addictionrate += 1        
    call Statup("Kitty", "Inbt", 30, 3) 
    call Statup("Kitty", "Inbt", 70, 1) 
    
    if Partner == "Kitty":
        call Partner_Like("Kitty",3,1)
    else:
        call Partner_Like("Kitty",4,2)
    
    if "Kitty Anal Addict" in Achievements:
            pass 
            
    elif K_Anal >= 10:
        $ K_SEXP += 7
        $ Achievements.append("Kitty Anal Addict")
        if not Situation:
            call KittyFace("bemused", 1)
            ch_k "I. . . really think I enjoy this. . ."                  
    elif K_Anal == 1:            
            $K_SEXP += 25        
            if not Situation: 
                if K_Love >= 500 and "unsatisfied" not in K_RecentActions:
                    ch_k "That was . . . interesting [K_Petname]. We'll have to do that again sometime."
                elif K_Obed <= 500 and P_Focus <= 20:
                    $ K_Mouth = "sad"
                    ch_k "Ouch."
                    ch_k "Did you get what you needed here?"
    elif K_Anal == 5:
            ch_k "We're making a regular habit of this."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in K_RecentActions:
            call KittyFace("angry")
            $ K_Eyes = "side"
            ch_k  "Hmm, you seemed to get more out of that than me. . ."
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_k "Mmm, so what else did you have in mind?"
    call Checkout
    return   


# End R Doggy Anal //////////////////////////////////////////////////////////////////////////////////
    

  
# K_Doggy_A hotdog //////////////////////////////////////////////////////////////////////

label K_Doggy_H: 
label K_Sex_H:  
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Kitty")
    if K_Hotdog >= 3: #You've done it before several times
        $ Tempmod += 10
    elif K_Hotdog: #You've done it before
        $ Tempmod += 5    
    
    if K_Lust > 85:
        $ Tempmod += 10
    elif K_Lust > 75: #She's really horny
        $ Tempmod += 5
    if Situation == "shift":
        $ Tempmod += 10   
    if "exhibitionist" in K_Traits:
        $ Tempmod += (3*Taboo)  
    if "dating" in K_Traits or "sex friend" in K_Petnames:
        $ Tempmod += 10
    elif "ex" in K_Traits:
        $ Tempmod -= 40 
    if K_ForcedCount and not K_Forced:
        $ Tempmod -= 5 * K_ForcedCount 
    
    if Taboo and "tabno" in K_DailyActions:        
        $ Tempmod -= 10 
        
    if "no hotdog" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no hotdog" in K_RecentActions else 0      
        
    $ Approval = ApprovalCheck("Kitty", 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)
    
    if Situation == "auto":   
        call Kitty_Doggy_Launch("L")   
        "You press up against Kitty's backside."    
        call KittyFace("surprised", 1)
        
        if (K_Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
            "Kitty is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            call KittyFace("sexy")
            call Statup("Kitty", "Obed", 70, 3)
            call Statup("Kitty", "Inbt", 50, 3) 
            call Statup("Kitty", "Inbt", 70, 1) 
            ch_k "Hmm, I've apparently got someone's attention. . ."            
            jump K_Doggy_HotdogPrep         
        else:                                                                                                            #she's questioning it
            $ K_Brows = "angry"                
            menu:
                ch_k "Hmm, kinda rude, [K_Petname]." 
                "Sorry, sorry! Never mind.":
                    if Approval:     
                        call KittyFace("sexy", 1)
                        call Statup("Kitty", "Obed", 70, 3)
                        call Statup("Kitty", "Inbt", 50, 3) 
                        call Statup("Kitty", "Inbt", 70, 1) 
                        ch_k "I guess it doesn't feel so bad. . ."
                        jump K_Doggy_HotdogPrep
                    "You pull back before you really get it in."                    
                    call KittyFace("bemused", 1)
                    if K_Hotdog:
                        ch_k "Well ok, [K_Petname], it has been kinda fun." 
                    else:
                        ch_k "Well ok, [K_Petname], that's a bit dirty, maybe ask a girl?"                                               
                "You'll see.":                    
                    call Statup("Kitty", "Love", 80, -10, 1)  
                    call Statup("Kitty", "Love", 200, -8)
                    "You grind against her asscrack."                              
                    call Statup("Kitty", "Obed", 70, 3)
                    call Statup("Kitty", "Inbt", 50, 3) 
                    if not ApprovalCheck("Kitty", 500, "O", TabM=1): #Checks if Obed is 700+  
                        call KittyFace("angry")
                        "Kitty shoves you away."
                        ch_k "Dick!"
                        ch_k "If that's how you want want to act, I'm out of here!"                                                  
                        call Statup("Kitty", "Love", 50, -10, 1)                        
                        call Statup("Kitty", "Obed", 50, 3)
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Kitty_Doggy_Reset
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")                       
                    else:
                        call KittyFace("sad")
                        "Kitty doesn't seem to be into this, but she knows her place."                        
                        jump K_Doggy_HotdogPrep
        return             
    
   
    if not K_Hotdog and "no hotdog" not in K_RecentActions:                                                               #first time    
        call KittyFace("surprised", 1)
        $ K_Mouth = "kiss"
        ch_k "Wait, so you want to grind against my butt?!"
  
        if K_Forced:
            call KittyFace("sad")
            ch_k ". . . That's all?"
        
        
    if not K_Hotdog and Approval:                                                 #First time dialog        
        if K_Forced: 
            call KittyFace("sad")
            call Statup("Kitty", "Love", 70, -3, 1)
            call Statup("Kitty", "Love", 20, -2, 1)
        elif K_Love >= (K_Obed + K_Inbt):
            call KittyFace("sexy")
            $ K_Brows = "sad"
            $ K_Mouth = "smile" 
            ch_k "It looks like you need some relief. . ."           
        elif K_Obed >= K_Inbt:
            call KittyFace("normal")
            ch_k "If that's what you need, [K_Petname]."
        elif K_Addict >= 50:
            call KittyFace("manic", 1)
            ch_k "Hmmm. . ."
        else: # Uninhibited 
            call KittyFace("sad")
            $ K_Mouth = "smile"             
            ch_k "Hmm, you look ready for it, at least. . ."    
            
    elif Approval:                                                                       #Second time+ dialog
        if K_Forced: 
            call KittyFace("sad")
            call Statup("Kitty", "Love", 70, -3, 1)
            call Statup("Kitty", "Love", 20, -2, 1)
            ch_k "That's all you want?"  
        elif not Taboo and "tabno" in K_DailyActions:        
            ch_k "Well, at least you got us some privacy this time. . ."   
        elif "hotdog" in K_RecentActions:
            call KittyFace("sexy", 1)
            ch_k "You want to go again? Ok."
            jump K_Doggy_HotdogPrep
        elif "hotdog" in K_DailyActions:
            call KittyFace("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",                 
                "So you'd like another go?",                 
                "You can't stay away from this booty. . .", 
                "Are you sure that's all you want?"]) 
            ch_k "[Line]"
        elif K_Hotdog < 3:        
            call KittyFace("sexy", 1)
            $ K_Brows = "confused"
            $ K_Mouth = "kiss"
            ch_k "So you'd like another go?"       
        else:       
            call KittyFace("sexy", 1)
            $ Kitty_Arms = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                "So you'd like another go?",                 
                "You can't stay away from this booty.", 
                "You want me to slick your pole?"]) 
            ch_k "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if K_Forced:
            call KittyFace("sad")
            call Statup("Kitty", "Obed", 80, 1)
            call Statup("Kitty", "Inbt", 60, 1)
            ch_k "Ok, fine."    
        elif "no hotdog" in K_DailyActions:               
            ch_k "Well, I guess it's not so bad. . ."
        else:
            call KittyFace("sexy", 1)
            call Statup("Kitty", "Love", 80, 1)
            call Statup("Kitty", "Inbt", 50, 2) 
            $ Line = renpy.random.choice(["Well, sure, give it a rub.",                 
                "Well. . . ok.",                 
                "Sure!", 
                "I guess we could do that.",
                "Hells yeah.",
                "Heh, ok, ok."]) 
            ch_k "[Line]"
            $ Line = 0
        call Statup("Kitty", "Obed", 60, 1)
        call Statup("Kitty", "Inbt", 70, 2) 
        jump K_Doggy_HotdogPrep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call KittyFace("angry")
        if "no hotdog" in K_RecentActions:  
            ch_k "I {i}just{/i} told you \"no,\" [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions and "no hotdog" in K_DailyActions: 
            ch_k "I told you that I didn't want you rubb'in up on me in public!" 
        elif "no hotdog" in K_DailyActions:       
            ch_k "I told you \"no\" earlier, [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "I told you that I didn't want you rubb'in up on me in public!"     
        elif not K_Hotdog:
            call KittyFace("bemused")
            ch_k "That's kinda naughty, [K_Petname]. . ."
        else:
            call KittyFace("bemused")
            ch_k "Not, right now [K_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no hotdog" in K_DailyActions:
                call KittyFace("bemused")
                ch_k "Yeah, ok, [K_Petname]."              
                return
            "Maybe later?" if "no hotdog" not in K_DailyActions:
                call KittyFace("sexy")  
                ch_k "Yeah, maybe, [K_Petname]."
                call Statup("Kitty", "Love", 80, 1)
                call Statup("Kitty", "Inbt", 50, 1)   
                if Taboo:                    
                    $ K_RecentActions.append("tabno")                      
                    $ K_DailyActions.append("tabno") 
                $ K_RecentActions.append("no hotdog")                      
                $ K_DailyActions.append("no hotdog")                          
                return
            "You might like it. . .":             
                if Approval:
                    call KittyFace("sexy")     
                    call Statup("Kitty", "Obed", 60, 2)
                    call Statup("Kitty", "Inbt", 50, 2) 
                    $ Line = renpy.random.choice(["Well, sure, give it a rub.",     
                        "I suppose. . .", 
                        "You've got me there."]) 
                    ch_k "[Line]"
                    $ Line = 0                   
                    jump K_Doggy_HotdogPrep
                else:   
                    pass
                    
            "Bend over.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Kitty", 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and K_Forced):
                    call KittyFace("sad")
                    call Statup("Kitty", "Love", 70, -2, 1)
                    call Statup("Kitty", "Love", 200, -2)                 
                    ch_k "Ok, fine. Whatever."  
                    call Statup("Kitty", "Obed", 80, 4)
                    call Statup("Kitty", "Inbt", 60, 2)  
                    $ K_Forced = 1  
                    jump K_Doggy_HotdogPrep
                else:                              
                    call Statup("Kitty", "Love", 200, -10)     
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Kitty_Arms = 1      
    
    if "no hotdog" in K_DailyActions:
        ch_k "I just don't want to, [K_Petname]."   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    if K_Forced:
        call KittyFace("angry", 1)
        ch_k "Even that's not worth it."
        call Statup("Kitty", "Lust", 200, 5)  
        if K_Love > 300: 
                call Statup("Kitty", "Love", 70, -1)
        call Statup("Kitty", "Obed", 50, -1)  
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call KittyFace("angry", 1)        
        $ K_RecentActions.append("tabno")                      
        $ K_DailyActions.append("tabno") 
        ch_k "I'd be a bit embarassed doing that here."  
        call Statup("Kitty", "Lust", 200, 5)  
        call Statup("Kitty", "Obed", 50, -3)  
    elif K_Hotdog:
        call KittyFace("sad") 
        ch_k "Eh-eh, not anymore, [K_Petname]."
    else:
        call KittyFace("normal", 1)
        ch_k "Not interested."    
    $ K_RecentActions.append("no hotdog")                      
    $ K_DailyActions.append("no hotdog") 
    $ Tempmod = 0    
    return

label K_Doggy_HotdogPrep:  
    call Seen_First_Peen("Kitty",Partner,React=Situation)
    call Kitty_Doggy_Launch("hotdog")
    
    if Situation == "Kitty":                                                                
            #Rogue auto-starts  
            $ Situation = 0
            "Kitty turns and backs up against your cock, rubbing it against her ass."
            menu:
                "What do you do?"
                "Go with it.":                     
                    call Statup("Kitty", "Inbt", 50, 3)
                    "Kitty starts to grind against you."
                "Praise her.":       
                    call KittyFace("sexy", 1)                    
                    call Statup("Kitty", "Inbt", 80, 2) 
                    ch_p "Hmmm, that's good, [K_Pet]."
                    call Kitty_Namecheck
                    "Kitty starts to grind against you."
                    call Statup("Kitty", "Love", 85, 1)
                    call Statup("Kitty", "Obed", 60, 2)
                "Ask her to stop.":
                    call KittyFace("surprised")       
                    call Statup("Kitty", "Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [K_Pet]."
                    call Kitty_Namecheck
                    "Kitty pulls back."
                    call Statup("Kitty", "Obed", 80, 1)
                    call Statup("Kitty", "Obed", 30, 2) 
                    $ P_RecentActions.append("nope")      
                    call AnyWord("Kitty",1,"refused","refused")                     
                    return  
    elif Situation != "auto":
            call Kitty_Bottoms_Off    
            
            if Taboo: # Kitty gets started. . .
                if K_Hotdog:                
                    "Kitty glances around to see if anyone notices what she's doing, then backs her ass up against your cock."
                    
                else:         
                    "Kitty glances around for voyeurs. . ."
                    "Kitty hesitantly pulls down your pants and slowly backs up against your rigid member."
                $ K_Inbt += int(Taboo/10)  
                $ K_Lust += int(Taboo/5)
            else:    
                if not K_Hotdog:
                    "Kitty bends over and presses her backside against you suggestively."
                else:
                    "Kitty hesitantly pulls down your pants slowly backs up against your rigid member."
                         
    else: #if Situation == "auto"       
            "You press yourself against her ass."
        
    if not K_Hotdog:                                                      #First time stat buffs      
        if K_Forced:
            call Statup("Kitty", "Love", 90, -5)
            call Statup("Kitty", "Obed", 70, 20)
            call Statup("Kitty", "Inbt", 80, 10) 
        else:
            call Statup("Kitty", "Love", 90, 20)
            call Statup("Kitty", "Obed", 70, 20)
            call Statup("Kitty", "Inbt", 80, 20)  
    
            
    if Situation:    
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ Trigger = "hotdog"
    $ Speed = 1
    if Taboo:
        call DrainWord("Kitty","tabno")
    call DrainWord("Kitty","no hotdog")
    $ K_RecentActions.append("hotdog")                      
    $ K_DailyActions.append("hotdog") 

label K_Doggy_Hotdog_Cycle: #Repeating strokes  
    while Round >=0:  
        call Shift_Focus("Kitty")
        call Kitty_Doggy_Launch(0) #"hotdog"
        call KittyLust  
        if Speed:
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
                                    call K_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump K_Doggy_Hotdog_Cycle  
                                    
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
                                            if K_Action and MultiAction:
                                                call Kitty_Offhand_Set
                                                if Trigger2:
                                                     $ K_Action -= 1
                                            else:
                                                ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"  
                                                
                                    "Shift primary action":
                                            if K_Action and MultiAction:
                                                    menu:
                                                        "How about sex?":
                                                            $ Situation = "shift"
                                                            call K_Doggy_HotdogAfter
                                                            call K_Doggy_P
                                                        "Just stick it in her pussy [[without asking].":
                                                            $ Situation = "auto"
                                                            call K_Doggy_HotdogAfter
                                                            call K_Doggy_P
                                                        "How about anal?":
                                                            $ Situation = "shift"
                                                            call K_Doggy_HotdogAfter
                                                            call K_Doggy_A
                                                        "Just stick it in her ass [[without asking].":
                                                            $ Situation = "auto"
                                                            call K_Doggy_HotdogAfter
                                                            call K_Doggy_A
                                                        "Never Mind":
                                                                jump K_Doggy_Hotdog_Cycle
                                            else:
                                                ch_k "I'm actually getting a little tired, so maybe we could wrap this up?" 
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask Kitty to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Kitty_Les_Change
                                            "Ask Kitty to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Kitty")  
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0    
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Kitty")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump K_Doggy_Hotdog_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump K_Doggy_Hotdog_Cycle 
                                            "Never mind":
                                                        jump K_Doggy_Hotdog_Cycle 
                                    "Just take a look at her.":                                           
                                            $ P_Cock = 0
                                            $ Speed = 0
                                    "Undress Kitty":
                                            call K_Undress   
                                    "Clean up Kitty (locked)" if not K_Spunk:
                                            pass  
                                    "Clean up Kitty" if K_Spunk:
                                            call Kitty_Cleanup("ask")                                         
                                    "Never mind":
                                            jump K_Doggy_Hotdog_Cycle                                    
                                                        
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Kitty_Doggy_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump K_Doggy_HotdogAfter
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Kitty_Doggy_Reset
                                    $ Line = 0
                                    jump K_Doggy_HotdogAfter
        #End menu (if Line)              
        
        call Shift_Focus("Kitty")  
        call Sex_Dialog("Kitty",Partner)
        
        $ Cnt += 1
        $ Round -= 1     
        
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or K_Lust >= 100:   
                    #If either of you could cum    
                    if P_Focus >= 100:
                            #If you can cum:                                                
                            call PK_Cumming
                            if "angry" in K_RecentActions:  
                                call Kitty_Doggy_Reset
                                return    
                            call Statup("Kitty", "Lust", 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                    $ K_RecentActions.append("unsatisfied")                      
                                    $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump K_Doggy_HotdogAfter 
                            $ Line = "came"

                    if K_Lust >= 100:         
                            #If you're still going at it and Kitty can cum
                            call K_Cumming
                            if Situation == "shift" or "angry" in K_RecentActions:
                                jump K_Doggy_HotdogAfter
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump K_Doggy_HotdogAfter
                            elif "unsatisfied" in K_RecentActions:
                                #And Kitty is unsatisfied,  
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if P_Semen:
                                        $ Line = "You get back into it" 
                                        jump K_Doggy_Hotdog_Cycle  
                                    "No, I'm done." if P_Semen:
                                        "You pull back."
                                        jump K_Doggy_HotdogAfter
                                    "No, I'm spent." if not P_Semen:
                                        "You pull back."
                                        jump K_Doggy_HotdogAfter        
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Kitty")            
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if K_SEXP >= 100 or ApprovalCheck("Kitty", 1200, "LO"):
            pass
        elif Cnt == (5 + K_Hotdog):
                    $ K_Brows = "confused"
                    ch_k "Are you getting close here?"   
        elif Cnt == (10 + K_Hotdog):
                    $ K_Brows = "angry"        
                    menu:
                        ch_k "I'm kinda done with this, [K_Petname]."
                        "How about a BJ?" if K_Action and MultiAction:
                                $ Situation = "shift"
                                call K_Doggy_HotdogAfter
                                call K_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                jump K_Doggy_Hotdog_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Kitty_Doggy_Reset
                                $ Situation = "shift"
                                jump K_Doggy_HotdogAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                                    call Statup("Kitty", "Love", 200, -5)
                                    call Statup("Kitty", "Obed", 50, 3)                    
                                    call Statup("Kitty", "Obed", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call KittyFace("angry", 1)   
                                    call Kitty_Doggy_Reset
                                    "She scowls at you and pulls away."
                                    ch_k "Well if that's your attitude you can handle your own business."                         
                                    call Statup("Kitty", "Love", 50, -3, 1)
                                    call Statup("Kitty", "Love", 80, -4, 1)
                                    call Statup("Kitty", "Obed", 30, -1, 1)                    
                                    call Statup("Kitty", "Obed", 50, -1, 1)  
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump K_Doggy_HotdogAfter
        #End Count check
   
        call Escalation("Kitty","R") #sees if she wants to escalate things
        
        if Round == 10:
            ch_k "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_k "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0)
    $ Line = 0
    ch_k "Ok, [K_Petname], that's enough of that for now."
    
label K_Doggy_HotdogAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Kitty_Doggy_Reset
        
    call KittyFace("sexy") 
    
    $ K_Hotdog += 1  
    $ K_Action -=1
    $ K_Addictionrate += 1
    if "addictive" in P_Traits:
        $ K_Addictionrate += 1        
    call Statup("Kitty", "Inbt", 30, 1) 
    call Statup("Kitty", "Inbt", 70, 1) 
    
    call Partner_Like("Kitty",1)
    
    if "Kitty Full Buns" in Achievements:
            pass 
            
    elif K_Hotdog >= 10:
        $ K_SEXP += 5
        $ Achievements.append("Kitty Full Buns")
        if not Situation:
            call KittyFace("smile", 1)
            ch_k "I think I'm getting addicted to this."               
    elif K_Hotdog == 1:            
            $K_SEXP += 10        
            if not Situation: 
                if K_Love >= 500 and "unsatisfied" not in K_RecentActions:
                    ch_k "That was pretty hot, [K_Petname], we'll have to do that again sometime."
                elif K_Obed <= 500 and P_Focus <= 20:
                    $ K_Mouth = "sad"
                    ch_k "Did you get what you needed here?"
    elif K_Hotdog == 5:
            ch_k "This is. . . interesting."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in K_RecentActions:
            call KittyFace("angry")
            $ K_Eyes = "side"
            ch_k "That didn't really do it for me. . ."
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_k "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# End R Doggy hotdogging //////////////////////////////////////////////////////////////////////////////////


            
image AssBase:                  #This is the base image, used in masks
    "images/KittyDoggy/Kitty_Doggy_Ass.png"

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

