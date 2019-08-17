# Start Laura Sex pose //////////////////////////////////////////////////////////////////////////////////
# L_Sex_P //////////////////////////////////////////////////////////////////////

label L_Sex_P:  
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
    if L_Sex >= 7: # She loves it
        $ Tempmod += 15
    elif L_Sex >= 3: #You've done it before several times
        $ Tempmod += 12
    elif L_Sex: #You've done it before
        $ Tempmod += 10    
        
    if L_Addict >= 75 and (L_CreamP + L_CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 20
    elif L_Addict >= 75:
        $ Tempmod += 15
        
    if L_Lust > 85:
        $ Tempmod += 10
    elif L_Lust > 75: #She's really horny
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 10 
    if "exhibitionist" in L_Traits:    
        $ Tempmod += (4*Taboo)      
    if "dating" in L_Traits or "sex friend" in L_Petnames:
        $ Tempmod += 10
    elif "ex" in L_Traits:
        $ Tempmod -= 40
    if L_ForcedCount and not L_Forced:
        $ Tempmod -= 5 * L_ForcedCount
    
    
        
    if Taboo and "tabno" in L_DailyActions:        
        $ Tempmod -= 10 
        
    if "no sex" in L_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no sex" in L_RecentActions else 0                  
             
        
    $ Approval = ApprovalCheck("Laura", 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)
    
    if Situation == "Laura":                                                                  #Laura auto-starts   
                if Approval > 2:                                                      # fix, add laura auto stuff here
                    call Laura_Sex_Launch("L")   
                    if L_Legs == "skirt":
                        "Laura lays back, sliding her skirt up as she does so."
                        $ L_Upskirt = 1
                    elif PantsNum("Laura") >= 5:
                        "Laura lays back, sliding her [L_Legs] off as she does so." 
                        $ L_Legs = 0
                    else:
                        "Laura lays back."
                    $ L_SeenPanties = 1
                    "She slides the tip along her pussy and seems to want you to insert it."
                    menu:
                        "What do you do?"
                        "Nothing.":                    
                            call Statup("Laura", "Inbt", 80, 3) 
                            call Statup("Laura", "Inbt", 50, 2)
                            "Laura slides it in."
                        "Praise her.":       
                            call LauraFace("sexy", 1)                    
                            call Statup("Laura", "Inbt", 80, 3) 
                            ch_p "Oh yeah, [L_Pet], let's do this."
                            call Laura_Namecheck
                            "Laura slides it in."
                            call Statup("Laura", "Love", 85, 1)
                            call Statup("Laura", "Obed", 90, 1)
                            call Statup("Laura", "Obed", 50, 2)
                        "Ask her to stop.":
                            call LauraFace("surprised")       
                            call Statup("Laura", "Inbt", 70, 1) 
                            ch_p "Let's not do that right now, [L_Pet]."
                            call Laura_Namecheck
                            "Laura pulls back."
                            call LauraOutfit
                            call Statup("Laura", "Obed", 90, 1)
                            call Statup("Laura", "Obed", 50, 1)
                            call Statup("Laura", "Obed", 30, 2)
                            return            
                    jump L_SexPrep
                    # End high approval
                else:                
                    $ Tempmod = 0                               # fix, add laura auto stuff here
                    $ Trigger2 = 0
                return   
    #End Laura's lead
    
    if Situation == "auto":   
                call Laura_Sex_Launch("L")   
                if L_Legs == "skirt":
                    "You push Laura onto her back, sliding her skirt up as you go."
                    $ L_Upskirt = 1                
                elif PantsNum("Laura") >= 5:
                    "You push Laura onto her back, sliding her pants down as you do."    
                    $ L_Legs = 0    
                else:
                    "You push Laura onto her back."
                $ L_SeenPanties = 1
                "You rub the tip of your cock against her moist slit."        
                call LauraFace("surprised", 1)
                
                if (L_Sex and Approval) or (Approval > 1):
                    #this is not the first time you've had sex, or she's into it         
                    "Laura glances down and then breaks into a smile."
                    call LauraFace("sly")
                    call Statup("Laura", "Obed", 70, 3)
                    call Statup("Laura", "Inbt", 50, 3) 
                    call Statup("Laura", "Inbt", 70, 1) 
                    ch_l "Fine by me, [L_Petname]."            
                    jump L_SexPrep         
                else:                                                                                                            
                    #she's questioning it
                    $ L_Brows = "angry"                
                    menu:
                        ch_l "Oh, taking it all the way, are we?" 
                        "Sorry, sorry! Never mind.":
                            if Approval:     
                                    call LauraFace("sexy", 1)
                                    call Statup("Laura", "Obed", 70, 3)
                                    call Statup("Laura", "Inbt", 50, 3) 
                                    call Statup("Laura", "Inbt", 70, 1) 
                                    ch_l "No no, not a problem. . ."
                                    jump L_SexPrep
                            else:
                                    "You pull back before you really get it in."                    
                                    call LauraFace("bemused", 1)
                                    if L_Sex:
                                        ch_l "Maybe ask first, [L_Petname]?" 
                                    else:
                                        ch_l "Maybe if you'd asked first. . ."
                        "Just fucking.":                    
                            call Statup("Laura", "Love", 80, -10, 1)  
                            call Statup("Laura", "Love", 200, -10)
                            "You press inside some more."                              
                            call Statup("Laura", "Obed", 70, 3)
                            call Statup("Laura", "Inbt", 50, 3) 
                            if not ApprovalCheck("Laura", 700, "O", TabM=1):   #Checks if Obed is 700+                          
                                call LauraFace("angry")
                                "Laura shoves you away and backhands you in the face."
                                ch_l "Dick."
                                ch_l "Don't push me."                                                  
                                call Statup("Laura", "Love", 50, -10, 1)                        
                                call Statup("Laura", "Obed", 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                call Laura_Sex_Reset
                                $ L_RecentActions.append("angry")
                                $ L_DailyActions.append("angry")                    
                            else:
                                call LauraFace("sad")
                                "Laura doesn't seem to be into this, you're lucky she's so obedient."                        
                                jump L_SexPrep
                return   
    #End Auto
    
   
    if not L_Sex and "no sex" not in L_RecentActions:                           
            #first time    
            call LauraFace("surprised", 1)
            $ L_Mouth = "kiss"
            ch_l "Huh, you wanna fuck me? . . "    
            if L_Forced:
                call LauraFace("sad")
                ch_l "Pretty bold of you. . ."
            
            
    if not L_Sex and Approval:                                                  
            #First time dialog        
            if L_Forced: 
                call LauraFace("sad")
                call Statup("Laura", "Love", 70, -30, 1)
                call Statup("Laura", "Love", 20, -20, 1)
            elif L_Love >= (L_Obed + L_Inbt):
                call LauraFace("sexy")
                $ L_Brows = "sad"
                $ L_Mouth = "smile" 
                ch_l "Well, you look so cute when you ask. . ."            
            elif L_Obed >= L_Inbt:
                call LauraFace("normal")
                ch_l "Yes, [L_Petname]. . ."            
            elif L_Addict >= 50:
                call LauraFace("manic", 1)
                ch_l "Sounds fun. . ."
            else: # Uninhibited 
                call LauraFace("sad")
                $ L_Mouth = "smile"             
                ch_l "I was hoping you'd ask. . ."   
            #End first time dialog
            
    elif Approval:                                                                      
            #Second time+ dialog        
            call LauraFace("sexy", 1)
            if L_Forced: 
                call LauraFace("sad")
                call Statup("Laura", "Love", 70, -3, 1)
                call Statup("Laura", "Love", 20, -2, 1)
                ch_l "I hope I don't wear you out." 
            elif not Taboo and "tabno" in L_DailyActions:        
                ch_l "Yeah, this is more covert."        
            elif "sex" in L_RecentActions:
                ch_l "Again? Your funeral." 
                jump L_SexPrep
            elif "sex" in L_DailyActions:
                $ Line = renpy.random.choice(["Back again?",                 
                    "You'd like another round?",                 
                    "I must be better than I thought.", 
                    "Didn't get enough earlier?",
                    "Your funeral, " + L_Petname + "."]) 
                ch_l "[Line]"
            elif L_Sex < 3:        
                $ L_Brows = "confused"
                $ L_Mouth = "kiss"
                ch_l "Oh? Another round?"      
            else:       
                $ Line = renpy.random.choice(["Oh, you want some of this?",                 
                    "You'd like another round?",                 
                    "I must be better than I thought.", 
                    "I hope you don't plan on wearing me out.",
                    "You want to plow me?"]) 
                ch_l "[Line]"
            $ Line = 0
            #end Second time+ dialog
            
    if Approval >= 2:                                                                  
            #She's into it. . .               
            if L_Forced:
                call LauraFace("sad")
                call Statup("Laura", "Obed", 90, 1)
                call Statup("Laura", "Inbt", 60, 1)
                ch_l "Ok, fine. Just make it good."  
            elif "no sex" in L_DailyActions:               
                ch_l "Ok, whatever. . ."
            else:
                call LauraFace("sexy", 1)
                call Statup("Laura", "Love", 90, 1)
                call Statup("Laura", "Inbt", 50, 3) 
                $ Line = renpy.random.choice(["Well. . . fine, let's do it.",                 
                    "Sure.", 
                    "We could, I guess.",
                    "Hmmm, sure.",
                    "Sounds fun."]) 
                ch_l "[Line]"
                $ Line = 0
            call Statup("Laura", "Obed", 20, 1)
            call Statup("Laura", "Obed", 60, 1)
            call Statup("Laura", "Inbt", 70, 2) 
            jump L_SexPrep   
    
    else:                                                                               
            #She's not into it, but maybe. . .    
            call LauraFace("angry")       
            if "no sex" in L_RecentActions:  
                ch_l "Sorry, [L_Petname] \"no.\""
            elif Taboo and "tabno" in L_DailyActions and "no sex" in L_DailyActions:  
                ch_l "I told you. . . this place is too exposed." 
            elif "no sex" in L_DailyActions:       
                ch_l "I just told you \"no.\""
            elif Taboo and "tabno" in L_DailyActions:  
                ch_l "I already told you this is too public!"     
            elif not L_Sex:
                call LauraFace("bemused")
                ch_l "Oh, you have no idea what you're in for. . ."
            else:
                call LauraFace("bemused")
                ch_l "Maybe later? . ."
            menu:
                extend ""
                "Sorry, never mind." if "no sex" in L_DailyActions:
                        call LauraFace("bemused")
                        ch_l "Well, you are persistant."
                        return
                "Maybe later?" if "no sex" not in L_DailyActions:
                        call LauraFace("sexy")  
                        ch_l "Probably. . ."
                        call Statup("Laura", "Love", 80, 2)
                        call Statup("Laura", "Inbt", 70, 2)   
                        if Taboo:                    
                            $ L_RecentActions.append("tabno")                      
                            $ L_DailyActions.append("tabno") 
                        $ L_RecentActions.append("no sex")                      
                        $ L_DailyActions.append("no sex")            
                        return
                "I think you'd enjoy it as much as I would. . .":             
                        if Approval:
                            call LauraFace("sexy")     
                            call Statup("Laura", "Obed", 90, 2)
                            call Statup("Laura", "Obed", 50, 2)
                            call Statup("Laura", "Inbt", 70, 3) 
                            call Statup("Laura", "Inbt", 40, 2) 
                            $ Line = renpy.random.choice(["Yeah, probably. . .",     
                                "I guess. . .", 
                                "Good point. . ."]) 
                            ch_l "[Line]"
                            $ Line = 0                   
                            jump L_SexPrep       
                "Just deal with it.":                                               # Pressured into it
                        $ Approval = ApprovalCheck("Laura", 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
                        if Approval > 1 or (Approval and L_Forced):
                            call LauraFace("sad")
                            call Statup("Laura", "Love", 70, -5, 1)
                            call Statup("Laura", "Love", 200, -5)                 
                            ch_l "Fine, if it'll shut you up."  
                            call Statup("Laura", "Obed", 80, 4)
                            call Statup("Laura", "Inbt", 80, 1) 
                            call Statup("Laura", "Inbt", 60, 3)  
                            $ L_Forced = 1  
                            jump L_SexPrep
                        else:                          
                            call Statup("Laura", "Love", 200, -20)   
                            $ L_RecentActions.append("angry")
                            $ L_DailyActions.append("angry")  
                #end menu
    #end Approval check
    
    #She refused all offers.
    $ Laura_Arms = 1  
    if "no sex" in L_DailyActions:
        ch_l "Don't push me." 
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif L_Forced:
        call LauraFace("angry", 1)
        ch_l "I'm over taking orders."
        call Statup("Laura", "Lust", 200, 5) 
        if L_Love > 300:   
                call Statup("Laura", "Love", 70, -2) 
        call Statup("Laura", "Obed", 50, -2)     
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call LauraFace("angry", 1)
        $ L_RecentActions.append("tabno")                      
        $ L_DailyActions.append("tabno") 
        ch_l "This place is way too exposed."     
        call Statup("Laura", "Lust", 200, 5)  
        call Statup("Laura", "Obed", 50, -3)
    elif L_Sex:
        call LauraFace("sad") 
        ch_l "Just jack it or something."       
    else:
        call LauraFace("normal", 1)
        ch_l "Yeah, no."     
    $ L_RecentActions.append("no sex")                      
    $ L_DailyActions.append("no sex") 
    $ Tempmod = 0    
    return

label L_SexPrep:
    call Seen_First_Peen("Laura",Partner)
    call Laura_Sex_Launch("hotdog")
    
    if Situation != "auto":
        call Laura_Bottoms_Off       
        
        
        if (L_Panties and not L_PantiesDown) or (L_Legs and not L_Upskirt) or HoseNum("Laura") >= 6: #If she refuses to take off her pants but agreed to anal
            ch_l "Huh. . ."
            
            if (L_Panties and not L_PantiesDown) and (PantsNum("Laura") > 5 and not L_Upskirt):
                "She quickly drops her pants and her [L_Panties]."
            elif (L_Panties and not L_PantiesDown) and (L_Legs == "shorts" and not L_Upskirt):
                "She quickly drops her shorts and her [L_Panties]."
            elif PantsNum("Laura") > 5 and not L_Upskirt:
                "She tugs her pants down, exposing her bare pussy."
            elif L_Legs == "shorts" and not L_Upskirt:
                "She tugs her shorts down, exposing her bare pussy."
            elif HoseNum("Laura") >= 6 and (L_Panties and not L_PantiesDown):
                "She tugs her [L_Hose] and [L_Panties] off."
                $ L_Hose = 0
            elif HoseNum("Laura") >= 6:
                "She tugs her [L_Hose] off and drops them to the ground."
                $ L_Hose = 0
            elif (L_Panties and not L_PantiesDown):
                "She tugs her [L_Panties] off and drops them to the ground."  
            
        $ L_Upskirt = 1
        $ L_PantiesDown = 1       
        $ L_SeenPanties = 1
        call Laura_First_Bottomless
        
        if Taboo: # Laura gets started. . .
            "Laura glances around to see if anyone notices what she's doing."
            if "cockout" in P_RecentActions:
                "Then she lays back and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and lays back."
                "She slowly presses against your rigid member."
            $ L_Inbt += int(Taboo/10)  
            $ L_Lust += int(Taboo/5)
        else:    
            if "cockout" in P_RecentActions:
                "Laura lays back and slowly presses against your rigid member."
            else:
                "Laura pulls down your pants and lays back."
                "She slowly presses against your rigid member."
        "She leans back a bit and your cock slides in."
                            
    else:  #if Situation == "auto"         
        if (L_Legs == "pants" and not L_Upskirt) and (L_Panties and not L_PantiesDown):
            "You quickly pull down her pants and her [L_Panties] and press against her slit."
        elif (L_Panties and not L_PantiesDown):
            "You quickly pull down her [L_Panties] and press against her slit."  
        $ L_Upskirt = 1
        $ L_PantiesDown = 1       
        $ L_SeenPanties = 1
        call Laura_First_Bottomless(1)
    
    if P_Focus >= 50:
            ch_l "Nice to see you're ready for business. . ."
    if not L_Sex:        
        if L_Forced:
            call Statup("Laura", "Love", 90, -150)
            call Statup("Laura", "Obed", 70, 60)
            call Statup("Laura", "Inbt", 80, 50) 
        else:
            call Statup("Laura", "Love", 90, 30)
            call Statup("Laura", "Obed", 70, 30)
            call Statup("Laura", "Inbt", 80, 60) 
    
    if Situation:   
        $ renpy.pop_call() 
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ P_Cock = "in"
    $ Trigger = "sex"
    $ Speed = 1
    if Taboo:
        call DrainWord("Laura","tabno")
    call DrainWord("Laura","no sex")
    $ L_RecentActions.append("sex")                      
    $ L_DailyActions.append("sex")     

label L_Sex_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Laura")
        call Laura_Sex_Launch("sex") 
        if Speed >= 4:     
            $ Speed = 2
#            call Speed_Shift(2) 
        call LauraLust        
        $ P_Cock = "in"
        $ Trigger = "sex"
        $ L_Upskirt = 1
        $ L_PantiesDown = 1  
        
        if  P_Focus < 100:                                                    
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass
                        "Keep going. . . (locked)" if not Speed:
                                    pass
                                 
                        "Start moving? . ." if not Speed:     
                                    $ Speed = 1
#                                    call Speed_Shift(1)                  
                        "Speed up. . ." if 0 < Speed < 3:    
                                    $ Speed += 1
#                                    call Speed_Shift(Speed+1) 
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass
                            
                        "Slow Down. . ." if Speed:    
                                    $ Speed -= 1
#                                    call Speed_Shift(Speed-1) 
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
                            
                        "Slap her ass":                     
                                    call L_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump L_Sex_Cycle  
                                    
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
                                            if L_Action and MultiAction:
                                                call Laura_Offhand_Set
                                                if Trigger2:
                                                     $ L_Action -= 1
                                            else:
                                                ch_l "I think we could take a little break." 
                                                
                                    "Shift primary action":
                                            if L_Action and MultiAction:
                                                    menu:
                                                        "How about anal?":
                                                                $ Situation = "shift"
                                                                call L_SexAfter
                                                                call L_Sex_A
                                                        "Just stick it in her ass [[without asking].":
                                                                $ Situation = "auto"
                                                                call L_SexAfter
                                                                call L_Sex_A
                                                        "Pull back to hotdog her.":
                                                                $ Situation = "pullback"
                                                                call L_SexAfter
                                                                call L_Sex_H
                                                        "Never Mind":
                                                                jump L_Sex_Cycle
                                            else:
                                                ch_l "I think we could take a little break." 
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask Laura to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Laura_Les_Change
                                            "Ask Laura to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Laura") 
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0   
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Laura")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump L_Sex_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump L_Sex_Cycle 
                                            "Never mind":
                                                        jump L_Sex_Cycle 
                                    "Undress Laura":
                                            call L_Undress   
                                    "Clean up Laura (locked)" if not L_Spunk:
                                            pass  
                                    "Clean up Laura" if L_Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump L_Sex_Cycle                                    
                                                        
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Laura_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump L_SexAfter
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Laura_Sex_Reset
                                    $ Line = 0
                                    jump L_SexAfter
        #End menu (if Line)              
        
        call Shift_Focus("Laura")    
        call Sex_Dialog("Laura",Partner)
        
        $ Cnt += 1
        $ Round -= 1     
        
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or L_Lust >= 100:   
                    #If either of you could cum    
                    if P_Focus >= 100:
                            #If you can cum:                                                
                            call PL_Cumming
                            if "angry" in L_RecentActions:  
                                call Laura_Sex_Reset
                                return    
                            call Statup("Laura", "Lust", 200, 5) 
                            if 100 > L_Lust >= 70 and L_OCount < 2:             
                                    $ L_RecentActions.append("unsatisfied")                      
                                    $ L_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump L_SexAfter 
                            $ Line = "came"

                    if L_Lust >= 100:         
                            #If you're still going at it and Laura can cum
                            call L_Cumming
                            if Situation == "shift" or "angry" in L_RecentActions:
                                jump L_SexAfter
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump L_SexAfter
                            elif "unsatisfied" in L_RecentActions:
                                #And Laura is unsatisfied,  
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if P_Semen:
                                        $ Line = "You get back into it" 
                                        jump L_Sex_Cycle  
                                    "No, I'm done." if P_Semen:
                                        "You pull back."
                                        jump L_SexAfter
                                    "No, I'm spent." if not P_Semen:
                                        "You pull back."
                                        jump L_SexAfter        
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if L_SEXP >= 100 or ApprovalCheck("Laura", 1200, "LO"):
            pass
        elif Cnt == (5 + L_Sex):
                    $ L_Brows = "confused"
                    ch_l "So are we getting close?"   
        elif Cnt == (10 + L_Sex):
                    $ L_Brows = "angry"        
                    menu:
                        ch_l "Hey. . . could we. . . try something. . . else?"
                        "How about a BJ?" if L_Action and MultiAction:
                                $ Situation = "shift"
                                call L_SexAfter
                                call L_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                jump L_Sex_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Laura_Sex_Reset
                                $ Situation = "shift"
                                jump L_SexAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "O"):                        
                                    call Statup("Laura", "Love", 200, -5)
                                    call Statup("Laura", "Obed", 50, 3)                    
                                    call Statup("Laura", "Obed", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call LauraFace("angry", 1)   
                                    call Laura_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_l "Not with that attitude."
                                    call Statup("Laura", "Love", 50, -3, 1)
                                    call Statup("Laura", "Love", 80, -4, 1)
                                    call Statup("Laura", "Obed", 30, -1, 1)                    
                                    call Statup("Laura", "Obed", 50, -1, 1)  
                                    $ L_RecentActions.append("angry")
                                    $ L_DailyActions.append("angry")   
                                    jump L_SexAfter
        #End Count check
   
        if Round == 10:
            ch_l "It's getting kinda late. . ."  
        elif Round == 5:
            ch_l "We should take a break for a minute."     
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, that's enough of that for now."
    
label L_SexAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Laura_Sex_Reset
        
    call LauraFace("sexy") 
    
    $ L_Sex += 1  
    $ L_Action -=1
    $ L_Addictionrate += 1
    if "addictive" in P_Traits:
        $ L_Addictionrate += 1        
    call Statup("Laura", "Inbt", 30, 2) 
    call Statup("Laura", "Inbt", 70, 1) 
        
    call Partner_Like("Laura",3,2)
    
    if "Laura Sex Addict" in Achievements:
            pass 
            
    elif L_Sex >= 10:
        $ L_SEXP += 5
        $ Achievements.append("Laura Sex Addict")
        if not Situation:
            call LauraFace("smile", 1)
            ch_l "We're making this a regular thing, huh. . ."               
    elif L_Sex == 1:            
            $L_SEXP += 20        
            if not Situation: 
                if L_Love >= 500 and "unsatisfied" not in L_RecentActions:
                    ch_l "I can tell, I was the best you've had."
                elif L_Obed <= 500 and P_Focus <= 20:
                    $ L_Mouth = "sad"
                    ch_l "Satisfied?"
    elif L_Sex == 5:
            ch_l "You know, this was a good idea."
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in L_RecentActions:
            call LauraFace("angry")
            $ L_Eyes = "side"
            ch_l "Forgetting someone? . ."
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Did you[L_like]want to try something else?"
    call Checkout
    return   

# End laura sex //////////////////////////////////////////////////////////////////////////////////


# Laura anal //////////////////////////////////////////////////////////////////////

label L_Sex_A:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
    if L_Anal >= 7: # She loves it
        $ Tempmod += 20   
    elif L_Anal >= 3: #You've done it before several times
        $ Tempmod += 17
    elif L_Anal: #You've done it before
        $ Tempmod += 15 
        
    if L_Addict >= 75 and (L_CreamP + L_CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 25
    elif L_Addict >= 75: 
        $ Tempmod += 15
    
    if L_Lust > 85:
        $ Tempmod += 10
    elif L_Lust > 75: #She's really horny
        $ Tempmod += 5
        
    $ Tempmod += 10  # she starts out loose    
        
    if Situation == "shift":
        $ Tempmod += 10    
    if "exhibitionist" in L_Traits:
        $ Tempmod += (5*Taboo) 
        
    if "dating" in L_Traits or "sex friend" in L_Petnames:
        $ Tempmod += 10      
    elif "ex" in L_Traits:
        $ Tempmod -= 40  
    if L_ForcedCount and not L_Forced:
        $ Tempmod -= 5 * L_ForcedCount
        
    if Taboo and "tabno" in L_DailyActions:        
        $ Tempmod -= 10 
    if "no anal" in L_DailyActions:               
        $ Tempmod -= 5         
        $ Tempmod -= 10 if "no anal" in L_RecentActions else 0  
            
    $ Approval = ApprovalCheck("Laura", 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)
    
    if Situation == "Laura":                                                                  
            #Laura auto-starts   
            if Approval > 2:                                                      
                # fix, add laura auto stuff here
                call Laura_Sex_Launch("L")   
                if L_Legs == "skirt":
                    "Laura lays back, sliding her skirt up as she does so."
                    $ L_Upskirt = 1
                elif PantsNum("Laura") >= 5:
                    "Laura lays back, sliding her [L_Legs] off as she does so." 
                    $ L_Legs = 0
                else:
                    "Laura lays back."
                $ L_SeenPanties = 1
                "She slides the tip up to her back door, and presses against it."
                menu:
                    "What do you do?"
                    "Nothing.":                    
                        call Statup("Laura", "Inbt", 80, 3) 
                        call Statup("Laura", "Inbt", 50, 2)
                        "Laura slides it in."
                    "Praise her.":       
                        call LauraFace("sexy", 1)                    
                        call Statup("Laura", "Inbt", 80, 3) 
                        ch_p "Ooo, dirty girl, [L_Pet], let's do this."
                        call Laura_Namecheck
                        "Laura slides it in."
                        call Statup("Laura", "Love", 85, 1)
                        call Statup("Laura", "Obed", 90, 1)
                        call Statup("Laura", "Obed", 50, 2)
                    "Ask her to stop.":
                        call LauraFace("surprised")       
                        call Statup("Laura", "Inbt", 70, 1) 
                        ch_p "Let's not do that right now, [L_Pet]."
                        call Laura_Namecheck
                        "Laura pulls back."
                        call LauraOutfit
                        call Statup("Laura", "Obed", 90, 1)
                        call Statup("Laura", "Obed", 50, 1)
                        call Statup("Laura", "Obed", 30, 2)                    
                        return            
                jump L_AnalPrep
            else:                
                $ Tempmod = 0                               # fix, add laura auto stuff here
                $ Trigger2 = 0
            return  
            #end if Laura initiates
    
    if Situation == "auto":   
            call Laura_Sex_Launch("L")   
            if L_Legs == "skirt":
                "You push Laura onto her back, sliding her skirt up as you go."
                $ L_Upskirt = 1                
            elif PantsNum("Laura") >= 5:
                "You push Laura onto her back, sliding her pants down as you do."    
                $ L_Legs = 0    
            else:
                "You push Laura onto her back."
            $ L_SeenPanties = 1
            "You press the tip of your cock against her tight rim."        
            call LauraFace("surprised", 1)
            
            if (L_Anal and Approval) or (Approval > 1):                                                                      
                #this is not the first time you've had sex, or she's into it    
                call Statup("Laura", "Obed", 70, 3)
                call Statup("Laura", "Inbt", 50, 3) 
                call Statup("Laura", "Inbt", 70, 1) 
                "Laura glances down and then breaks into a smile."
                ch_l "Yeah, ok. . ."          
                jump L_AnalPrep         
            else:                                                                                                            
                #she's questioning it
                $ L_Brows = "angry"                
                menu:
                    ch_l "Oh? A backdoor intruder?" 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            call LauraFace("sexy", 1)
                            call Statup("Laura", "Obed", 70, 3)
                            call Statup("Laura", "Inbt", 50, 3) 
                            call Statup("Laura", "Inbt", 70, 1) 
                            ch_l "Hey, whatever floats your boat. . ."
                            ch_l "Get in there."
                            jump L_AnalPrep
                        "You pull back before you really get it in."                    
                        call LauraFace("bemused", 1)
                        
                        if L_Anal:
                            ch_l "You coulda warned me. . ." 
                        else:
                            ch_l "Hey, all I expect is a little warning. . ."
                    "Just fucking.":                    
                        call Statup("Laura", "Love", 80, -10, 1)  
                        call Statup("Laura", "Love", 200, -8)
                        "You press into her."                              
                        call Statup("Laura", "Obed", 70, 3)
                        call Statup("Laura", "Inbt", 50, 3) 
                        if not ApprovalCheck("Laura", 700, "O", TabM=1):                        
                            call LauraFace("angry")
                            "Laura shoves you away and backhands you in the face."
                            ch_l "Yeah, not like that you won't."                                           
                            call Statup("Laura", "Love", 50, -10, 1)                        
                            call Statup("Laura", "Obed", 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            call Laura_Sex_Reset
                            $ L_RecentActions.append("angry")
                            $ L_DailyActions.append("angry")                        
                        else:
                            call LauraFace("sad")
                            "Laura doesn't seem to be into this, you're lucky she's so obedient."                        
                            jump L_AnalPrep
            return  
            #end "auto" 
    
   
    if not L_Anal and "no anal" not in L_RecentActions:                                                               
            #first time    
            call LauraFace("surprised", 1)
            $ L_Mouth = "kiss"
            ch_l "Huh, anal?"
      
            if L_Forced:
                call LauraFace("sad")
                ch_l "Anal? That's what you're pushing for?"
        
    if "anal" in L_RecentActions:
            call LauraFace("sexy", 1)
            ch_l "Sure, get in there."
            jump L_AnalPrep
        
    
    if not L_Anal and Approval:                                                 
            #First time dialog        
            if L_Forced: 
                call LauraFace("sad")
                call Statup("Laura", "Love", 70, -3, 1)
                call Statup("Laura", "Love", 20, -2, 1)
            elif L_Love >= (L_Obed + L_Inbt):
                call LauraFace("sexy")
                $ L_Brows = "sad"
                $ L_Mouth = "smile" 
                ch_l "I was hoping you'd ask. . ."           
            elif L_Obed >= L_Inbt:
                call LauraFace("normal")
                ch_l "I expected that. . ."
            elif L_Addict >= 50:
                call LauraFace("manic", 1)
                ch_l "Hmm, sounds fun. . ."
            else: # Uninhibited 
                call LauraFace("sad")
                $ L_Mouth = "smile"             
                ch_l "I was tired of waiting. . ."  
    
    elif Approval:                                                                       
            #Second time+ dialog
            if L_Forced: 
                call LauraFace("sad")
                call Statup("Laura", "Love", 70, -3, 1)
                call Statup("Laura", "Love", 20, -2, 1)
                ch_l "You don't hold back. . ."
            elif not Taboo and "tabno" in L_DailyActions:        
                ch_l "I guess this is secluded enough. . ."   
            elif "anal" in L_DailyActions and not L_Loose:
                pass      
            elif "anal" in L_RecentActions:
                ch_l "I am warmed up. . ."
                jump L_AnalPrep
            elif "anal" in L_DailyActions:
                call LauraFace("sexy", 1)
                $ Line = renpy.random.choice(["Back again so soon?",                 
                    "So you'd like another round?",                 
                    "Again? Sure.", 
                    "Didn't get enough earlier?",
                    "Your funeral, " + L_Petname + "."]) 
                ch_l "[Line]"    
            else:       
                call LauraFace("sexy", 1)
                $ Laura_Arms = 2
                $ Line = renpy.random.choice(["Oooh, you want some of this?",                 
                    "So you'd like another round?",                 
                    "I knew you enjoyed it. . .", 
                    "I hope you don't plan on wearing me out.",
                    "You want to plow me?"]) 
                ch_l "[Line]"
            $ Line = 0
            
    if Approval >= 2:                                                                   
            #She's into it. . .               
            if L_Forced:
                call LauraFace("sad")
                call Statup("Laura", "Obed", 90, 1)
                call Statup("Laura", "Inbt", 60, 1)
                ch_l "Whatever."   
            elif "no anal" in L_DailyActions:               
                ch_l "Well, if you're going to keep asking. . ."
                ch_l "Might be fun. . ."
            else:
                call LauraFace("sexy", 1)
                call Statup("Laura", "Love", 90, 1)
                call Statup("Laura", "Inbt", 50, 3) 
                $ Line = renpy.random.choice(["Well. . . ok.",                 
                    "Sure.", 
                    "You could, I guess.",
                    "Um, yeah.",
                    "Heh, ok, ok."]) 
                ch_l "[Line]"
                $ Line = 0
            call Statup("Laura", "Obed", 20, 1)
            call Statup("Laura", "Obed", 60, 1)
            call Statup("Laura", "Inbt", 70, 2) 
            jump L_AnalPrep   
               
    else:                                                                               
            #She's not into it, but maybe. . .            
            call LauraFace("angry")
            if "no anal" in L_RecentActions:  
                ch_l "Sorry, [L_Petname] \"no.\""
            elif Taboo and "tabno" in L_DailyActions and "no anal" in L_DailyActions:
                ch_l "I told you. . . this place is too exposed." 
            elif "no anal" in L_DailyActions:       
                ch_l "I just told you \"no.\""
            elif Taboo and "tabno" in L_DailyActions:  
                ch_l "I already told you this is too public!"      
            elif not L_Anal:
                call LauraFace("bemused")
                ch_l "I don't know that you're ready for that yet."
            else:
                call LauraFace("bemused")
                ch_l "Maybe eventually. . ."
            menu:
                extend ""
                "Sorry, never mind." if "no anal" in L_DailyActions:
                    call LauraFace("bemused")
                    ch_l "Hey, I can't blame you."              
                    return
                "Maybe later?" if "no anal" not in L_DailyActions:
                    call LauraFace("sexy")  
                    ch_l "Oh, probably. . ."
                    ch_l ". . . often."
                    call Statup("Laura", "Love", 80, 2)
                    call Statup("Laura", "Inbt", 70, 2)  
                    if Taboo:                    
                        $ L_RecentActions.append("tabno")                      
                        $ L_DailyActions.append("tabno") 
                    $ L_RecentActions.append("no anal")                      
                    $ L_DailyActions.append("no anal") 
                    return
                "I bet it would feel really good. . .":             
                    if Approval:
                        call LauraFace("sexy")     
                        call Statup("Laura", "Obed", 90, 2)
                        call Statup("Laura", "Obed", 50, 2)
                        call Statup("Laura", "Inbt", 70, 3) 
                        call Statup("Laura", "Inbt", 40, 2) 
                        $ Line = renpy.random.choice(["Yeah, probably. . .",     
                                "I guess. . .", 
                                "Good point. . ."]) 
                        ch_l "[Line]"
                        $ Line = 0                   
                        jump L_AnalPrep
                    else:   
                        pass
                        
                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Laura", 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                    if Approval > 1 or (Approval and L_Forced):
                        call LauraFace("sad")
                        call Statup("Laura", "Love", 70, -5, 1)
                        call Statup("Laura", "Love", 200, -5)                 
                        ch_l "Oh fine, get it over with."  
                        call Statup("Laura", "Obed", 80, 4)
                        call Statup("Laura", "Inbt", 80, 1) 
                        call Statup("Laura", "Inbt", 60, 3)  
                        $ L_Forced = 1  
                        jump L_AnalPrep
                    else:                              
                        call Statup("Laura", "Love", 200, -20)    
                        $ L_RecentActions.append("angry")
                        $ L_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Laura_Arms = 1  
    if "no anal" in L_DailyActions:
        ch_l "Don't push it."   
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif L_Forced:
        call LauraFace("angry", 1)
        ch_l "You're going too far."
        call Statup("Laura", "Lust", 200, 5)     
        if L_Love > 300:     
                call Statup("Laura", "Love", 70, -2)
        call Statup("Laura", "Obed", 50, -2)    
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif Taboo:                             
        # she refuses and this is too public a place for her
        call LauraFace("angry", 1)
        $ L_RecentActions.append("tabno")                      
        $ L_DailyActions.append("tabno") 
        ch_l "This place is way too exposed."
        call Statup("Laura", "Lust", 200, 5)  
        call Statup("Laura", "Obed", 50, -3) 
    elif "anal" in L_DailyActions:
        call LauraFace("bemused")
        ch_l "Not right now."    
    elif L_Anal:
        call LauraFace("sad") 
        ch_l "You'll have to earn it."
    else:
        call LauraFace("normal", 1)
        ch_l "You haven't earned it yet."    
    $ L_RecentActions.append("no anal")                      
    $ L_DailyActions.append("no anal") 
    $ Tempmod = 0    
    return

label L_AnalPrep:    
    call Seen_First_Peen("Laura",Partner)
    call Laura_Sex_Launch("hotdog")
    
    if Situation != "auto":
        call Laura_Bottoms_Off    
        if (L_Panties and not L_PantiesDown) or (L_Legs and not L_Upskirt) or HoseNum("Laura") >= 6: #If she refuses to take off her pants but agreed to anal
            ch_l "Huh. . ."
            
            if (L_Panties and not L_PantiesDown) and (PantsNum("Laura") > 5 and not L_Upskirt):
                "She quickly drops her pants and her [L_Panties]."
            elif (L_Panties and not L_PantiesDown) and (L_Legs == "shorts" and not L_Upskirt):
                "She quickly drops her shorts and her [L_Panties]."
            elif PantsNum("Laura") > 5 and not L_Upskirt:
                "She tugs her pants down, exposing her bare pussy."
            elif L_Legs == "shorts" and not L_Upskirt:
                "She tugs her shorts down, exposing her bare pussy."
            elif HoseNum("Laura") >= 6 and (L_Panties and not L_PantiesDown):
                "She tugs her [L_Hose] and [L_Panties] off."
                $ L_Hose = 0
            elif HoseNum("Laura") >= 6:
                "She tugs her [L_Hose] off and drops them to the ground."
                $ L_Hose = 0
            elif (L_Panties and not L_PantiesDown):
                "She tugs her [L_Panties] off and drops them to the ground."  
                
        $ L_Upskirt = 1
        $ L_PantiesDown = 1       
        $ L_SeenPanties = 1
        call Laura_First_Bottomless
        
        if Taboo: # Laura gets started. . .
            "Laura glances around to see if anyone notices what she's doing."
            if "cockout" in P_RecentActions:
                "Then she lays back and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and lays back."
                "She slowly presses against your rigid member."
            $ L_Inbt += int(Taboo/10)  
            $ L_Lust += int(Taboo/5)
        else:    
            if "cockout" in P_RecentActions:
                "Laura lays back and slowly presses against your rigid member."
            else:
                "Laura pulls down your pants and lays back."
                "She slowly presses against your rigid member."
        "She leans back a bit and your cock pops in."
                     
    else: #if Situation == "auto"       
        if (L_Legs == "pants" and not L_Upskirt) and (L_Panties and not L_PantiesDown):
            "You quickly pull down her pants and her [L_Panties] and press against her back door."
        elif (L_Panties and not L_PantiesDown):
            "You quickly pull down her [L_Panties] and press against her back door."  
        $ L_Upskirt = 1
        $ L_PantiesDown = 1       
        $ L_SeenPanties = 1
        call Laura_First_Bottomless(1)
            
    if not L_Anal:                                                      #First time stat buffs       
        if L_Forced:
            call Statup("Laura", "Love", 90, -150)
            call Statup("Laura", "Obed", 70, 70)
            call Statup("Laura", "Inbt", 80, 40) 
        else:
            call Statup("Laura", "Love", 90, 10)
            call Statup("Laura", "Obed", 70, 30)
            call Statup("Laura", "Inbt", 80, 70) 
    elif not L_Loose:                                                   #first few times stat buffs       
        if L_Forced:
            call Statup("Laura", "Love", 90, -20)
            call Statup("Laura", "Obed", 70, 10)
            call Statup("Laura", "Inbt", 80, 5) 
        else:
            call Statup("Laura", "Obed", 70, 7)
            call Statup("Laura", "Inbt", 80, 5) 
                
    if Situation:    
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ P_Cock = "anal"
    $ Trigger = "anal"
    $ Speed = 1
    if Taboo:
        call DrainWord("Laura","tabno")
    call DrainWord("Laura","no anal")
    $ L_RecentActions.append("anal")                      
    $ L_DailyActions.append("anal") 

label L_Anal_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Laura")
        call Laura_Sex_Launch("anal") 
        if Speed >= 4:    
            $ Shift = 2
#            call Speed_Shift(2) 
        call LauraLust        
        $ P_Cock = "anal"
        $ Trigger = "anal"
        
        if P_Focus < 100:                                                    
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass
                        "Keep going. . . (locked)" if not Speed:
                                    pass
                             
                        "Start moving? . ." if not Speed:     
                                    $ Speed = 1
#                                    call Speed_Shift(1)                  
                        "Speed up. . ." if 0 < Speed < 3:    
                                    $ Speed += 1
#                                    call Speed_Shift(Speed+1) 
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass
                            
                        "Slow Down. . ." if Speed:    
                                    $ Speed -= 1
#                                    call Speed_Shift(Speed-1) 
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
                                    
                        "Slap her ass":                     
                                    call L_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump L_Anal_Cycle  
                                    
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
                                            if L_Action and MultiAction:
                                                call Laura_Offhand_Set
                                                if Trigger2:
                                                     $ L_Action -= 1
                                            else:
                                                ch_l "I think we could take a little break." 
                                                
                                    "Shift primary action":
                                            if L_Action and MultiAction:
                                                    menu:
                                                        "How about sex?":
                                                                $ Situation = "shift"
                                                                call L_AnalAfter
                                                                call L_Sex_P
                                                        "Just stick it in her pussy [[without asking].":
                                                                $ Situation = "auto"
                                                                call L_AnalAfter
                                                                call L_Sex_P
                                                        "Pull back to hotdog her.":
                                                                $ Situation = "pullback"
                                                                call L_AnalAfter
                                                                call L_Sex_H
                                                        "Never Mind":
                                                                jump L_Anal_Cycle
                                            else:
                                                ch_l "I think we could take a little break." 
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask Laura to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Laura_Les_Change
                                            "Ask Laura to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Laura") 
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0   
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Laura")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump L_Anal_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump L_Anal_Cycle 
                                            "Never mind":
                                                        jump L_Anal_Cycle 
                                    "Undress Laura":
                                            call L_Undress   
                                    "Clean up Laura (locked)" if not L_Spunk:
                                            pass  
                                    "Clean up Laura" if L_Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump L_Anal_Cycle                                    
                                                        
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Laura_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump L_AnalAfter
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Laura_Sex_Reset
                                    $ Line = 0
                                    jump L_AnalAfter
        #End menu (if Line)              
        
        call Shift_Focus("Laura")    
        call Sex_Dialog("Laura",Partner)
        
        $ Cnt += 1
        $ Round -= 1     
        
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or L_Lust >= 100:   
                    #If either of you could cum    
                    if P_Focus >= 100:
                            #If you can cum:                                                
                            call PL_Cumming
                            if "angry" in L_RecentActions:  
                                call Laura_Sex_Reset
                                return    
                            call Statup("Laura", "Lust", 200, 5) 
                            if 100 > L_Lust >= 70 and L_OCount < 2:             
                                    $ L_RecentActions.append("unsatisfied")                      
                                    $ L_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump L_AnalAfter 
                            $ Line = "came"

                    if L_Lust >= 100:         
                            #If you're still going at it and Laura can cum
                            call L_Cumming
                            if Situation == "shift" or "angry" in L_RecentActions:
                                jump L_AnalAfter
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump L_AnalAfter
                            elif "unsatisfied" in L_RecentActions:
                                #And Laura is unsatisfied,  
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if P_Semen:
                                        $ Line = "You get back into it" 
                                        jump L_Anal_Cycle  
                                    "No, I'm done." if P_Semen:
                                        "You pull back."
                                        jump L_AnalAfter
                                    "No, I'm spent." if not P_Semen:
                                        "You pull back."
                                        jump L_AnalAfter        
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if L_SEXP >= 100 or ApprovalCheck("Laura", 1200, "LO"):
            pass
        elif Cnt == (5 + L_Anal):
                    $ L_Brows = "confused"
                    ch_l "We getting close here?"   
        elif Cnt == (10 + L_Anal):
                    $ L_Brows = "angry"        
                    menu:
                        ch_l "Can we. . . do something. . . else?"
                        "How about a BJ?" if L_Action and MultiAction:
                                $ Situation = "shift"
                                call L_AnalAfter
                                call L_Blowjob  
                        "How about a Handy?" if L_Action and MultiAction:
                                $ Situation = "shift"
                                call L_AnalAfter
                                call L_Handjob     
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                jump L_Anal_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Laura_Sex_Reset
                                $ Situation = "shift"
                                jump L_AnalAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "O"):                        
                                    call Statup("Laura", "Love", 200, -5)
                                    call Statup("Laura", "Obed", 50, 3)                    
                                    call Statup("Laura", "Obed", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call LauraFace("angry", 1)   
                                    call Laura_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_l "Not with that attitude."                         
                                    call Statup("Laura", "Love", 50, -3, 1)
                                    call Statup("Laura", "Love", 80, -4, 1)
                                    call Statup("Laura", "Obed", 30, -1, 1)                    
                                    call Statup("Laura", "Obed", 50, -1, 1)  
                                    $ L_RecentActions.append("angry")
                                    $ L_DailyActions.append("angry")   
                                    jump L_AnalAfter
        #End Count check
   
        if Round == 10:
            ch_l "It's getting kinda late. . ."  
        elif Round == 5:
            ch_l "We should take a break for a minute."        
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, that's enough of that for now."
    
label L_AnalAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Laura_Sex_Reset
        
    call LauraFace("sexy") 
    
    $ L_Anal += 1  
    $ L_Action -=1
    $ L_Addictionrate += 1
    if "addictive" in P_Traits:
        $ L_Addictionrate += 1        
    call Statup("Laura", "Inbt", 30, 3) 
    call Statup("Laura", "Inbt", 70, 1) 
    
    if Partner == "Kitty":
        call Partner_Like("Laura",4,2)
    else:
        call Partner_Like("Laura",3,2)
    
    if "Laura Anal Addict" in Achievements:
            pass 
            
    elif L_Anal >= 10:
        $ L_SEXP += 7
        $ Achievements.append("Laura Anal Addict")
        if not Situation:
            call LauraFace("bemused", 1)
            ch_l "I think you've got a knack for that."                  
    elif L_Anal == 1:            
            $L_SEXP += 25        
            if not Situation: 
                if L_Love >= 500 and "unsatisfied" not in L_RecentActions:
                    ch_l "You seem to know your way around back there."  
                elif L_Obed <= 500 and P_Focus <= 20:
                    $ L_Mouth = "sad"
                    ch_l "That was pleasant."
    elif L_Anal == 5:
            ch_l "I'm glad you're into this."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in L_RecentActions:
            call LauraFace("angry")
            $ L_Eyes = "side"
            ch_l  "Forgetting someone? . ."
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Mmm, so what else did you have in mind?"
    call Checkout
    return   


# End Laura Anal //////////////////////////////////////////////////////////////////////////////////
    

  
# Laura hotdog //////////////////////////////////////////////////////////////////////

label L_Sex_H: 
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
    if L_Hotdog >= 3: #You've done it before several times
        $ Tempmod += 10
    elif L_Hotdog: #You've done it before
        $ Tempmod += 5    
    
    if L_Lust > 85:
        $ Tempmod += 10
    elif L_Lust > 75: #She's really horny
        $ Tempmod += 5
    if Situation == "shift":
        $ Tempmod += 10   
    if "exhibitionist" in L_Traits:
        $ Tempmod += (3*Taboo)  
    if "dating" in L_Traits or "sex friend" in L_Petnames:
        $ Tempmod += 10
    elif "ex" in L_Traits:
        $ Tempmod -= 40 
    if L_ForcedCount and not L_Forced:
        $ Tempmod -= 5 * L_ForcedCount 
    
    if Taboo and "tabno" in L_DailyActions:        
        $ Tempmod -= 10 
        
    if "no hotdog" in L_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no hotdog" in L_RecentActions else 0      
        
    $ Approval = ApprovalCheck("Laura", 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)
    
    if Situation == "Laura":                                                                  
            #Laura auto-starts   
            if Approval > 2:                                                      # fix, add laura auto stuff here
                call Laura_Sex_Launch("L") 
                "Laura pulls you onto her, rubbing your cock against against her mound."
                menu:
                    "What do you do?"
                    "Nothing.":                     
                        call Statup("Laura", "Inbt", 50, 3)
                        "Laura starts to grind against you."
                    "Praise her.":       
                        call LauraFace("sexy", 1)                    
                        call Statup("Laura", "Inbt", 80, 2) 
                        ch_p "Hmmm, that's good, [L_Pet]."
                        call Laura_Namecheck
                        "Laura starts to grind against you."
                        call Statup("Laura", "Love", 85, 1)
                        call Statup("Laura", "Obed", 60, 2)
                    "Ask her to stop.":
                        call LauraFace("surprised")       
                        call Statup("Laura", "Inbt", 70, 1) 
                        ch_p "Let's not do that right now, [L_Pet]."
                        call Laura_Namecheck
                        "Laura pulls back."
                        call LauraOutfit
                        call Statup("Laura", "Obed", 80, 1)
                        call Statup("Laura", "Obed", 30, 2)                    
                        return            
                jump L_HotdogPrep
            else:                
                $ Tempmod = 0                               # fix, add laura auto stuff here
                $ Trigger2 = 0
            return            
            #end Laura initates
    
    if Situation == "auto":   
            call Laura_Sex_Launch("L")   
            "You push Laura down, and press your cock against her."    
            call LauraFace("surprised", 1)
            
            if (L_Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
                "Laura glances down and then breaks into a smile."
                call LauraFace("sly")
                call Statup("Laura", "Obed", 70, 3)
                call Statup("Laura", "Inbt", 50, 3) 
                call Statup("Laura", "Inbt", 70, 1) 
                ch_l "Oh, what did you have in mind with that? . ."            
                jump L_HotdogPrep         
            else:                                                                                                            #she's questioning it
                $ L_Brows = "angry"                
                menu:
                    ch_l "You might want to take a step back, [L_Petname]?" 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            call LauraFace("sexy", 1)
                            call Statup("Laura", "Obed", 70, 3)
                            call Statup("Laura", "Inbt", 50, 3) 
                            call Statup("Laura", "Inbt", 70, 1) 
                            ch_l "Or not. . ."
                            jump L_HotdogPrep
                        "You pull back from her."                    
                        call LauraFace("bemused", 1)
                        ch_l "Maybe ask first?"                                             
                    "You'll see.":                    
                        call Statup("Laura", "Love", 80, -10, 1)  
                        call Statup("Laura", "Love", 200, -8)
                        "You grind against her crotch."                              
                        call Statup("Laura", "Obed", 70, 3)
                        call Statup("Laura", "Inbt", 50, 3) 
                        if not ApprovalCheck("Laura", 500, "O", TabM=1): #Checks if Obed is 700+  
                            call LauraFace("angry")
                            "Laura shoves you away."
                            ch_l "Don't push it, [L_Petname]."                                                  
                            call Statup("Laura", "Love", 50, -10, 1)                        
                            call Statup("Laura", "Obed", 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            call Laura_Sex_Reset
                            $ L_RecentActions.append("angry")
                            $ L_DailyActions.append("angry")                       
                        else:
                            call LauraFace("sad")
                            "Laura doesn't seem to be into this, but she knows her place."                        
                            jump L_HotdogPrep
            return     
            #end auto
    
   
    if not L_Hotdog and "no hotdog" not in L_RecentActions:                                                               
            #first time    
            call LauraFace("surprised", 1)
            $ L_Mouth = "kiss"
            ch_l "What, just grinding?"
      
            if L_Forced:
                call LauraFace("sad")
                ch_l ". . . nothing more?"
        
        
    if not L_Hotdog and Approval:                                                
            #First time dialog        
            if L_Forced: 
                call LauraFace("sad")
                call Statup("Laura", "Love", 70, -3, 1)
                call Statup("Laura", "Love", 20, -2, 1)
            elif L_Love >= (L_Obed + L_Inbt):
                call LauraFace("sexy")
                $ L_Brows = "sad"
                $ L_Mouth = "smile" 
                ch_l "If that's what you're into. . ."           
            elif L_Obed >= L_Inbt:
                call LauraFace("normal")
                ch_l "If that's what works for you. . ."
            elif L_Addict >= 50:
                call LauraFace("manic", 1)
                ch_l "Hrmm. . ."
            else: # Uninhibited 
                call LauraFace("sad")
                $ L_Mouth = "smile"             
                ch_l "Well if that's what gets you off. . ."    
            
    elif Approval:                                                                      
            #Second time+ dialog
            if L_Forced: 
                call LauraFace("sad")
                call Statup("Laura", "Love", 70, -3, 1)
                call Statup("Laura", "Love", 20, -2, 1)
                ch_l "That's pushing it. . ."  
            elif not Taboo and "tabno" in L_DailyActions:        
                ch_l "I guess this is a better location . ."   
            elif "hotdog" in L_RecentActions:
                call LauraFace("sexy", 1)
                ch_l "Again? Fine, whatever."
                jump L_HotdogPrep
            elif "hotdog" in L_DailyActions:
                call LauraFace("sexy", 1)
                $ Line = renpy.random.choice(["Back again so soon?",                 
                    "So you'd like another round?",                 
                    "You're really into this. . .", 
                    "Are you sure that's all you want?"]) 
                ch_l "[Line]"    
            else:       
                call LauraFace("sexy", 1)
                $ Laura_Arms = 2
                $ Line = renpy.random.choice(["Oooh, you want some of this?",                 
                    "So you'd like another round?",                       
                    "You're really into this. . .", 
                    "You want another rub?"]) 
                ch_l "[Line]"
            $ Line = 0
            
    if Approval >= 2:                                                                  
            #She's into it. . .               
            if L_Forced:
                call LauraFace("sad")
                call Statup("Laura", "Obed", 80, 1)
                call Statup("Laura", "Inbt", 60, 1)
                ch_l "Ok, fine."    
            elif "no hotdog" in L_DailyActions:               
                ch_l "It was rather entertaining. . ."
            else:
                call LauraFace("sexy", 1)
                call Statup("Laura", "Love", 80, 1)
                call Statup("Laura", "Inbt", 50, 2) 
                $ Line = renpy.random.choice(["Well, sure, let me give it a rub.",                 
                    "Very well.",                 
                    "Nice!", 
                    "I guess we could do that.",
                    "Ok, let me. . .",
                    "Heh, ok, ok."]) 
                ch_l "[Line]"
                $ Line = 0
            call Statup("Laura", "Obed", 60, 1)
            call Statup("Laura", "Inbt", 70, 2) 
            jump L_HotdogPrep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            call LauraFace("angry")
            if "no hotdog" in L_RecentActions:  
                ch_l "Sorry, [L_Petname] \"no.\""
            elif Taboo and "tabno" in L_DailyActions and "no hotdog" in L_DailyActions: 
                ch_l "I just told you. . .not in such an exposed location." 
            elif "no hotdog" in L_DailyActions:       
                ch_l "I'm believe I just told you \"no,\" [L_Petname]."
            elif Taboo and "tabno" in L_DailyActions:  
                ch_l "I told you. . . this place is too exposed." 
            elif not L_Hotdog:
                call LauraFace("bemused")
                ch_l "Hmm, that could be amusing, [L_Petname]. . ."
            else:
                call LauraFace("bemused")
                ch_l "I don't think that would be appropriate. . ."
            menu:
                extend ""
                "Sorry, never mind." if "no hotdog" in L_DailyActions:
                    call LauraFace("bemused")
                    ch_l "So long as you don't push it."              
                    return
                "Maybe later?" if "no hotdog" not in L_DailyActions:
                    call LauraFace("sexy")  
                    ch_l "I gues eventually. . ."
                    call Statup("Laura", "Love", 80, 1)
                    call Statup("Laura", "Inbt", 50, 1)   
                    if Taboo:                    
                        $ L_RecentActions.append("tabno")                      
                        $ L_DailyActions.append("tabno") 
                    $ L_RecentActions.append("no hotdog")                      
                    $ L_DailyActions.append("no hotdog")                          
                    return
                "You might like it. . .":             
                    if Approval:
                        call LauraFace("sexy")     
                        call Statup("Laura", "Obed", 60, 2)
                        call Statup("Laura", "Inbt", 50, 2) 
                        $ Line = renpy.random.choice(["Yeah, probably. . .",     
                                "I guess. . .", 
                                "Good point. . ."]) 
                        ch_l "[Line]"
                        $ Line = 0                   
                        jump L_HotdogPrep
                    else:   
                        pass
                        
                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Laura", 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                    if Approval > 1 or (Approval and L_Forced):
                        call LauraFace("sad")
                        call Statup("Laura", "Love", 70, -2, 1)
                        call Statup("Laura", "Love", 200, -2)                 
                        ch_l "Alright, fine."  
                        call Statup("Laura", "Obed", 80, 4)
                        call Statup("Laura", "Inbt", 60, 2)  
                        $ L_Forced = 1  
                        jump L_HotdogPrep
                    else:                              
                        call Statup("Laura", "Love", 200, -10)     
                        $ L_RecentActions.append("angry")
                        $ L_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Laura_Arms = 1      
    
    if "no hotdog" in L_DailyActions:
        ch_l "What did I tell you?"   
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    if L_Forced:
        call LauraFace("angry", 1)
        ch_l "There's no point trying."
        call Statup("Laura", "Lust", 200, 5)  
        if L_Love > 300:   
                call Statup("Laura", "Love", 70, -1)
        call Statup("Laura", "Obed", 50, -1)  
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call LauraFace("angry", 1)        
        $ L_RecentActions.append("tabno")                      
        $ L_DailyActions.append("tabno") 
        ch_l "This area is a bit too exposed for that sort of thing. . ."  
        call Statup("Laura", "Lust", 200, 5)  
        call Statup("Laura", "Obed", 50, -3)  
    elif L_Hotdog:
        call LauraFace("sad") 
        ch_l "Not anymore."
    else:
        call LauraFace("normal", 1)
        ch_l "No thanks."    
    $ L_RecentActions.append("no hotdog")                      
    $ L_DailyActions.append("no hotdog") 
    $ Tempmod = 0    
    return

label L_HotdogPrep:  
    call Seen_First_Peen("Laura",Partner)
    call Laura_Sex_Launch("hotdog")
    
    if Situation != "auto":
#        call Laura_Bottoms_Off    
        
        if Taboo: # Laura gets started. . .
            "Laura glances around to see if anyone notices what she's doing."
            if "cockout" in P_RecentActions:
                "Then she lays back and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and lays back."
                "She slowly presses against your rigid member."
            $ L_Inbt += int(Taboo/10)  
            $ L_Lust += int(Taboo/5)
        else:    
            if "cockout" in P_RecentActions:
                "Laura lays back and slowly presses against your rigid member."
            else:
                "Laura pulls down your pants and lays back."
                "She slowly presses against your rigid member."
                     
    else: #if Situation == "auto"       
        "She lays back, pulling you against her with your rigid member."
    
    if not L_Hotdog:                                                      #First time stat buffs      
        if L_Forced:
            call Statup("Laura", "Love", 90, -5)
            call Statup("Laura", "Obed", 70, 20)
            call Statup("Laura", "Inbt", 80, 10) 
        else:
            call Statup("Laura", "Love", 90, 20)
            call Statup("Laura", "Obed", 70, 20)
            call Statup("Laura", "Inbt", 80, 20)  
    
            
    if Situation:    
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ Trigger = "hotdog"
    $ Speed = 1
    if Taboo:
        call DrainWord("Laura","tabno")
    call DrainWord("Laura","no hotdog")
    $ L_RecentActions.append("hotdog")                      
    $ L_DailyActions.append("hotdog") 

label L_Hotdog_Cycle: #Repeating strokes 
    while Round >=0:  
        call Shift_Focus("Laura")
        call Laura_Sex_Launch("hotdog") 
        if Speed >= 4:        
            $ Speed = 2
#            call Speed_Shift(2) 
        call LauraLust        
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
#                                    call Speed_Shift(1)                  
                        "Speed up. . ." if 0 < Speed < 3:    
                                    $ Speed += 1
#                                    call Speed_Shift(Speed+1) 
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass
                            
                        "Slow Down. . ." if Speed:    
                                    $ Speed -= 1
#                                    call Speed_Shift(Speed-1) 
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
                            
                        "Slap her ass":                     
                                    call L_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump L_Hotdog_Cycle  
                                    
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
                                            if L_Action and MultiAction:
                                                call Laura_Offhand_Set
                                                if Trigger2:
                                                     $ L_Action -= 1
                                            else:
                                                ch_l "I think we could take a little break." 
                                                
                                    "Shift primary action":
                                            if L_Action and MultiAction:
                                                    menu:
                                                        "How about sex?":
                                                            $ Situation = "shift"
                                                            call L_HotdogAfter
                                                            call L_Sex_P
                                                        "Just stick it in her pussy [[without asking].":
                                                            $ Situation = "auto"
                                                            call L_HotdogAfter
                                                            call L_Sex_P
                                                        "How about anal?":
                                                            $ Situation = "shift"
                                                            call L_HotdogAfter
                                                            call L_Sex_A
                                                        "Just stick it in her ass [[without asking].":
                                                            $ Situation = "auto"
                                                            call L_HotdogAfter
                                                            call L_Sex_A
                                                        "Never Mind":
                                                                jump L_Hotdog_Cycle
                                            else:
                                                ch_l "I think we could take a little break." 
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask Laura to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Laura_Les_Change
                                            "Ask Laura to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Laura") 
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0   
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Laura")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump L_Hotdog_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump L_Hotdog_Cycle 
                                            "Never mind":
                                                        jump L_Hotdog_Cycle 
                                    "Undress Laura":
                                            call L_Undress   
                                    "Clean up Laura (locked)" if not L_Spunk:
                                            pass  
                                    "Clean up Laura" if L_Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump L_Hotdog_Cycle                                    
                                                        
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Laura_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump L_HotdogAfter
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Laura_Sex_Reset
                                    $ Line = 0
                                    jump L_HotdogAfter
        #End menu (if Line)              
        
        call Shift_Focus("Laura")    
        call Sex_Dialog("Laura",Partner)
        
        $ Cnt += 1
        $ Round -= 1     
        
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or L_Lust >= 100:   
                    #If either of you could cum    
                    if P_Focus >= 100:
                            #If you can cum:                                                
                            call PL_Cumming
                            if "angry" in L_RecentActions:  
                                call Laura_Sex_Reset
                                return    
                            call Statup("Laura", "Lust", 200, 5) 
                            if 100 > L_Lust >= 70 and L_OCount < 2:             
                                    $ L_RecentActions.append("unsatisfied")                      
                                    $ L_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump L_HotdogAfter 
                            $ Line = "came"

                    if L_Lust >= 100:         
                            #If you're still going at it and Laura can cum
                            call L_Cumming
                            if Situation == "shift" or "angry" in L_RecentActions:
                                jump L_HotdogAfter
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump L_HotdogAfter
                            elif "unsatisfied" in L_RecentActions:
                                #And Laura is unsatisfied,  
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if P_Semen:
                                        $ Line = "You get back into it" 
                                        jump L_Hotdog_Cycle  
                                    "No, I'm done." if P_Semen:
                                        "You pull back."
                                        jump L_HotdogAfter
                                    "No, I'm spent." if not P_Semen:
                                        "You pull back."
                                        jump L_HotdogAfter        
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if L_SEXP >= 100 or ApprovalCheck("Laura", 1200, "LO"):
            pass
        elif Cnt == (5 + L_Hotdog):
                    $ L_Brows = "confused"
                    ch_l "Are we getting close here?"   
        elif Cnt == (10 + L_Hotdog):
                    $ L_Brows = "angry"        
                    menu:
                        ch_l "I'm kinda bored by this."
                        "How about a BJ?" if L_Action and MultiAction:
                                $ Situation = "shift"
                                call L_HotdogAfter
                                call L_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                jump L_Hotdog_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Laura_Sex_Reset
                                $ Situation = "shift"
                                jump L_HotdogAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "O"):                        
                                    call Statup("Laura", "Love", 200, -5)
                                    call Statup("Laura", "Obed", 50, 3)                    
                                    call Statup("Laura", "Obed", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call LauraFace("angry", 1)   
                                    call Laura_Sex_Reset
                                    "She scowls at you and pulls away."
                                    ch_l "Not with that attitude."                         
                                    call Statup("Laura", "Love", 50, -3, 1)
                                    call Statup("Laura", "Love", 80, -4, 1)
                                    call Statup("Laura", "Obed", 30, -1, 1)                    
                                    call Statup("Laura", "Obed", 50, -1, 1)  
                                    $ L_RecentActions.append("angry")
                                    $ L_DailyActions.append("angry")   
                                    jump L_HotdogAfter
        #End Count check
   
        if Round == 10:
            ch_l "It's getting kinda late. . ."  
        elif Round == 5:
            ch_l "We should take a break for a minute."        
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, that's enough of that for now."
    
label L_HotdogAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Laura_Sex_Reset
        
    call LauraFace("sexy") 
    
    $ L_Hotdog += 1  
    $ L_Action -=1
    $ L_Addictionrate += 1
    if "addictive" in P_Traits:
        $ L_Addictionrate += 1        
    call Statup("Laura", "Inbt", 30, 1) 
    call Statup("Laura", "Inbt", 70, 1) 
    
    call Partner_Like("Laura",2)
    
    if L_Hotdog == 10:
        $ L_SEXP += 5             
    elif L_Hotdog == 1:            
            $L_SEXP += 10        
            if not Situation: 
                if L_Love >= 500 and "unsatisfied" not in L_RecentActions:
                    ch_l "That was. . . nice."
                elif L_Obed <= 500 and P_Focus <= 20:
                    $ L_Mouth = "sad"
                    ch_l "Enough for you?" 
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in L_RecentActions:
            call LauraFace("angry")
            $ L_Eyes = "side"
            ch_l "That didn't do much for me. . ."
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# End Laura hotdogging //////////////////////////////////////////////////////////////////////////////////
