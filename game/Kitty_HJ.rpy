## K_Handjob //////////////////////////////////////////////////////////////////////
label K_Handjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Kitty")
    if K_Hand >= 7: # She loves it
        $ Tempmod += 10
    elif K_Hand >= 3: #You've done it before several times
        $ Tempmod += 7
    elif K_Hand: #You've done it before
        $ Tempmod += 3
        
    if K_Addict >= 75 and K_Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 15
    if K_Addict >= 75:
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 15
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
        
    if "no hand" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no hand" in K_RecentActions else 0    
        
    $ Approval = ApprovalCheck("Kitty", 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)
            
    if not K_Hand and "no hand" not in K_RecentActions:        
        call KittyFace("confused", 2)
        ch_k "So you want a handy then?"
        $ K_Blush = 1
            
    if not K_Hand and Approval:                                                 #First time dialog        
        if K_Forced: 
            call KittyFace("sad",1)
            call Statup("Kitty", "Love", 70, -3, 1)
            call Statup("Kitty", "Love", 20, -2, 1)
        elif K_Love >= (K_Obed + K_Inbt):
            call KittyFace("sexy",1)
            $ K_Brows = "sad"
            $ K_Mouth = "smile" 
            ch_k "I guess it could be interesting. . ."            
        elif K_Obed >= K_Inbt:
            call KittyFace("normal",1)
            ch_k "If you want, [K_Petname]. . ."            
        elif K_Addict >= 50:
            call KittyFace("manic", 1)
            ch_k "I kind of {i}need{/i} to. . ."  
        else: # Uninhibited 
            call KittyFace("lipbite",1)    
            ch_k "I guess. . ."    
            
    elif Approval:                                                                       #Second time+ dialog
        if K_Forced: 
            call KittyFace("sad")
            call Statup("Kitty", "Love", 70, -3, 1)
            call Statup("Kitty", "Love", 20, -2, 1)
            ch_k "That's it, right?" 
        elif not Taboo and "tabno" in K_DailyActions:        
            ch_k "Well, I guess if it's here. . ."    
        elif "hand" in K_RecentActions:
            call KittyFace("sexy", 1)
            ch_k "You're giving me carpal tunnel. . ."
            jump KHJ_Prep
        elif "hand" in K_DailyActions:
            call KittyFace("sexy", 1)
            $ Line = renpy.random.choice(["Another one?",   
                "You're going to give me calluses.", 
                "Didn't get enough earlier?",
                "My hand's kinda sore from earlier.",
                "My hand's kinda sore from earlier."]) 
            ch_k "[Line]"
        elif K_Hand < 3:        
            call KittyFace("sexy", 1)
            $ K_Brows = "confused"
            $ K_Mouth = "kiss"
            ch_k "Hmm, magic fingers. . ."        
        else:       
            call KittyFace("sexy", 1)
            $ Kitty_Arms = 2
            $ Line = renpy.random.choice(["You want some of this?",                 
                "So you'd like another handy?",                 
                "A little. . . [fist pumping hand gestures]?", 
                "A little TLC?"]) 
            ch_k "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if K_Forced:
            call KittyFace("sad")
            call Statup("Kitty", "Obed", 90, 1)
            call Statup("Kitty", "Inbt", 60, 1)
            ch_k "Ok, fine." 
        elif "no hand" in K_DailyActions:               
            ch_k "OK, geeze!"   
        else:
            call KittyFace("sexy", 1)
            call Statup("Kitty", "Love", 90, 1)
            call Statup("Kitty", "Inbt", 50, 3) 
            $ Line = renpy.random.choice(["Sure, I guess.",                 
                "Ooooookay.",                 
                "Cool, lemme see it.", 
                "I guess I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Heh, ok, ok."]) 
            ch_k "[Line]"
            $ Line = 0
        call Statup("Kitty", "Obed", 20, 1)
        call Statup("Kitty", "Obed", 60, 1)
        call Statup("Kitty", "Inbt", 70, 2) 
        jump KHJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call KittyFace("angry")
        if "no hand" in K_RecentActions:  
            ch_k "You don't[K_like]listen do you, [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions and "no hand" in K_DailyActions: 
            ch_k "I said not in public!"  
        elif "no hand" in K_DailyActions:       
            ch_k "I told you \"no,\" [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "I said not in public!"     
        elif not K_Hand:
            call KittyFace("bemused")
            ch_k "I don't know, [K_Petname]. . ."
        else:
            call KittyFace("bemused")
            ch_k "Not now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no hand" in K_DailyActions:
                call KittyFace("bemused")
                ch_k "Yeah."              
                return
            "Maybe later?" if "no hand" not in K_DailyActions:
                call KittyFace("sexy")  
                ch_k ". . ."
                ch_k "Maybe."
                call Statup("Kitty", "Love", 80, 2)
                call Statup("Kitty", "Inbt", 70, 2)   
                if Taboo:                    
                    $ K_RecentActions.append("tabno")                      
                    $ K_DailyActions.append("tabno") 
                $ K_RecentActions.append("no hand")                      
                $ K_DailyActions.append("no hand")            
                return
            "I'd really appreciate it. . .":             
                if Approval:
                    call KittyFace("sexy")     
                    call Statup("Kitty", "Obed", 90, 2)
                    call Statup("Kitty", "Obed", 50, 2)
                    call Statup("Kitty", "Inbt", 70, 3) 
                    call Statup("Kitty", "Inbt", 40, 2) 
                    $ Line = renpy.random.choice(["Sure, I guess.",                 
                            "Ooooookay.",                 
                            "Cool, lemme see it.", 
                            "I guess I could. . .",
                            "Ok. . . [She gestures for you to come over].",
                            "Heh, ok, ok."]) 
                    ch_k "[Line]"
                    $ Line = 0                   
                    jump KHJ_Prep
                else:   
                    pass
                    
            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Kitty", 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and K_Forced):
                    call KittyFace("sad")
                    call Statup("Kitty", "Love", 70, -5, 1)
                    call Statup("Kitty", "Love", 200, -2)                 
                    ch_k "Ok, fine."  
                    call Statup("Kitty", "Obed", 50, 4)
                    call Statup("Kitty", "Inbt", 80, 1) 
                    call Statup("Kitty", "Inbt", 60, 3)  
                    $ K_Forced = 1  
                    jump KHJ_Prep
                else:                              
                    call Statup("Kitty", "Love", 200, -15)     
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Kitty_Arms = 1 
    if "no hand" in K_DailyActions:
        call KittyFace("angry", 1)
        ch_k "I'm not telling you again."   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1)
        ch_k "Not even if you had a ten foot pole."
        call KittyFace("surprised", 2)
        ch_k "I mean. . ."
        call KittyFace("angry", 1)        
        ch_k "You know what I mean!"
        call Statup("Kitty", "Lust", 200, 5)
        if K_Love > 300:
                call Statup("Kitty", "Love", 70, -2)
        call Statup("Kitty", "Obed", 50, -2)    
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call KittyFace("angry", 1)          
        $ K_DailyActions.append("tabno") 
        ch_k "Not here, not anywhere near here."
        call Statup("Kitty", "Lust", 200, 5)  
        call Statup("Kitty", "Obed", 50, -3)   
    elif K_Hand:
        call KittyFace("sad") 
        ch_k "I'm not feeling it today. . ."       
    else:
        call KittyFace("normal", 1)
        ch_k "I don't wanna touch that."  
    $ K_RecentActions.append("no hand")                      
    $ K_DailyActions.append("no hand") 
    $ Tempmod = 0    
    return
    

label K_HJ_Prep:
label KHJ_Prep:
    if Trigger2 == "hand": 
        return
    
    if Taboo:
        $ K_Inbt += int(Taboo/10)  
        $ K_Lust += int(Taboo/5)
                
    call KittyFace("sexy")
    if K_Forced:
        call KittyFace("sad")
    elif K_Hand:
        $ K_Brows = "confused"
        $ K_Eyes = "sexy"
        $ K_Mouth = "smile"
    
    call Seen_First_Peen("Kitty",Partner,React=Situation)
    call Kitty_HJ_Launch("L")
        
    if Situation == "Kitty":                                                          
            #Kitty auto-starts  
            $ Situation = 0 
            if Trigger2 == "jackin":
                "Kitty brushes your hand aside and starts stroking your cock."
            else:
                "Kitty gives you a mischevious smile, and starts to fondle your cock."
            menu:
                "What do you do?"
                "Nothing.":                    
                    call Statup("Kitty", "Inbt", 70, 3) 
                    call Statup("Kitty", "Inbt", 30, 2)                     
                    "Kitty continues her actions."
                "Praise her.":       
                    call KittyFace("sexy", 1)                    
                    call Statup("Kitty", "Inbt", 70, 3) 
                    ch_p "Oooh, that's good, [K_Pet]."
                    call Kitty_Namecheck
                    "Kitty continues her actions."
                    call Statup("Kitty", "Love", 80, 1)
                    call Statup("Kitty", "Obed", 90, 1)
                    call Statup("Kitty", "Obed", 50, 2)
                "Ask her to stop.":
                    call KittyFace("surprised")       
                    call Statup("Kitty", "Inbt", 70, 1) 
                    ch_p "Let's not do that for now, [K_Pet]."
                    call Kitty_Namecheck
                    "Kitty puts it down."
                    call Statup("Kitty", "Obed", 90, 1)
                    call Statup("Kitty", "Obed", 50, 1)
                    call Statup("Kitty", "Obed", 30, 2)
                    $ P_RecentActions.append("nope")      
                    call AnyWord("Kitty",1,"refused","refused")  
                    return   
                    
    if not K_Hand:        
        if K_Forced:
            call Statup("Kitty", "Love", 90, -20)
            call Statup("Kitty", "Obed", 70, 25)
            call Statup("Kitty", "Inbt", 80, 30) 
        else:
            call Statup("Kitty", "Love", 90, 5)
            call Statup("Kitty", "Obed", 70, 20)
            call Statup("Kitty", "Inbt", 80, 20)     
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Kitty","tabno")
    call DrainWord("Kitty","no hand")
    $ K_RecentActions.append("hand")                      
    $ K_DailyActions.append("hand") 
  
label KHJ_Cycle:    
    while Round >=0:  
        call Shift_Focus("Kitty") 
        call Kitty_HJ_Launch    
        call KittyLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                          
                        "Start moving? . ." if not Speed:
                                    $ Speed = 1
                            
                        "Speed up. . ." if Speed < 2:                    
                                    $ Speed = 2
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 2:
                                    pass
                            
                        "Slow Down. . ." if Speed:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
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
                                    "I also want to fondle her breasts." if Trigger2 != "fondle breasts":
                                            if K_Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ K_Action -= 1
                                            else:
                                                ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"  
                                         
                                    "Shift primary action":
                                            if K_Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    if K_Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call KHJ_After                
                                                                        call K_Blowjob
                                                                    else:
                                                                        ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."
                                                                        
#                                                        "How about a titjob?":
#                                                                    if K_Action and MultiAction:
#                                                                        $ Situation = "shift"
#                                                                        call KHJ_After
#                                                                        call K_Titjob
#                                                                    else:
#                                                                        ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."
                                                        "Never Mind":
                                                                jump KHJ_Cycle
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
                                                        jump KHJ_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump KHJ_Cycle 
                                            "Never mind":
                                                        jump KHJ_Cycle 
                                    "Undress Kitty":
                                            call K_Undress   
                                    "Clean up Kitty (locked)" if not K_Spunk:
                                            pass  
                                    "Clean up Kitty" if K_Spunk:
                                            call Kitty_Cleanup("ask")                                         
                                    "Never mind":
                                            jump KHJ_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Kitty_HJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump KHJ_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Kitty_HJ_Reset
                                    $ Line = 0
                                    jump KHJ_After
        #End menu (if Line)
        
        call Shift_Focus("Kitty")  
        call Sex_Dialog("Kitty",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or K_Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PK_Cumming
                            if "angry" in K_RecentActions:  
                                call Kitty_HJ_Reset
                                return    
                            call Statup("Kitty", "Lust", 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2 and K_SEXP >= 20:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump KHJ_After 
                            $ Line = "came"
     
                    if K_Lust >= 100:  
                            #If Kitty can cum                                             
                            call K_Cumming
                            if Situation == "shift" or "angry" in K_RecentActions:
                                jump KHJ_After
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in K_RecentActions:#And Kitty is unsatisfied,  
                                "Kitty still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump KHJ_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Kitty")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if Cnt == 20:
                    $ K_Brows = "angry"        
                    menu:
                        ch_k "Ouch, hand cramp, can we[K_like]take a break?"
                        "How about a BJ?" if K_Action and MultiAction:
                                $ Situation = "shift"
                                call KHJ_After
                                call K_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                jump KHJ_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Kitty_HJ_Reset
                                $ Situation = "shift"
                                jump KHJ_After
                        "No, get back down there.":
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):
                                    call Statup("Kitty", "Love", 200, -5)
                                    call Statup("Kitty", "Obed", 50, 3)                    
                                    call Statup("Kitty", "Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    call KittyFace("angry", 1)   
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_k "Hey, I've got better things to do if you're[K_like]going to be a dick about it."                                               
                                    call Statup("Kitty", "Love", 50, -3, 1)
                                    call Statup("Kitty", "Love", 80, -4, 1)
                                    call Statup("Kitty", "Obed", 30, -1, 1)                    
                                    call Statup("Kitty", "Obed", 50, -1, 1)                     
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump KHJ_After
        elif Cnt == 10 and K_SEXP <= 100 and not ApprovalCheck("Kitty", 1200, "LO"):
                    $ K_Brows = "confused"
                    ch_k "Can we[K_Like]be done with this now? I'm getting sore."         
        #End Count check
                   
        call Escalation("Kitty","K") #sees if she wants to escalate things
        
        if Round == 10:
            ch_k "It's kind of time to get moving."   
        elif Round == 5:
            ch_k "For real[K_like]time's up."      
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0)
    $ Line = 0
    ch_k "Ok, we need to take a break."
    
label KHJ_After:
    call KittyFace("sexy") 
    
    $ K_Hand += 1  
    $ K_Action -=1
    $ K_Addictionrate += 1
    if "addictive" in P_Traits:
        $ K_Addictionrate += 1        
    call Statup("Kitty", "Lust", 90, 5)
    
    call Partner_Like("Kitty",1)
            
    if "Kitty Handi-Queen" in Achievements:
            pass  
    elif K_Hand >= 10:
            call KittyFace("smile", 1)
            ch_k "I've kinda become[K_like]a \"Handi-Queen\" or something."
            $ Achievements.append("Kitty Handi-Queen")
            $K_SEXP += 5          
    elif K_Hand == 1:            
            $K_SEXP += 10
            if K_Love >= 500:
                $ K_Mouth = "smile"
                ch_k "It was so warm to the touch. . ."
            elif P_Focus <= 20:
                $ K_Mouth = "sad"
                ch_k "Did that work out for you?"
    elif K_Hand == 5:
                ch_k "Let me know any time you need me to give you a hand."                  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_k "Ok, so what were you thinking?"
    else:
        call Kitty_HJ_Reset    
    call Checkout
    return

## end K_Handjob //////////////////////////////////////////////////////////////////////


## K_Titjob //////////////////////////////////////////////////////////////////////              Not finished
label K_Titjob:
    $ Round -= 5 if Round > 5 else (Round-1)    
    call Shift_Focus("Kitty")
    if K_Tit >= 7: # She loves it
        $ Tempmod += 10
    elif K_Tit >= 3: #You've done it before several times
        $ Tempmod += 7
    elif K_Tit: #You've done it before
        $ Tempmod += 5
    
    if K_Addict >= 75 and K_Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 15
    elif K_Addict >= 75:
        $ Tempmod += 5
        
    if K_SeenChest and ApprovalCheck("Kitty", 500): # You've seen her tits.
        $ Tempmod += 10    
    if not K_Chest and not K_Over: #She's already topless
        $ Tempmod += 10
    if K_Lust > 75: #She's really horny
        $ Tempmod += 10
    if Situation == "shift":
        $ Tempmod += 15
    if "exhibitionist" in K_Traits:
        $ Tempmod += (5*Taboo)
    if "dating" in K_Traits or "sex friend" in K_Petnames:
        $ Tempmod += 10
    elif "ex" in K_Traits:
        $ Tempmod -= 30 
    if K_ForcedCount and not K_Forced:
        $ Tempmod -= 5 * K_ForcedCount    
    
    if Taboo and "tabno" in K_DailyActions:        
        $ Tempmod -= 10 
        
    if "no titjob" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no titjob" in K_RecentActions else 0    
        
    $ Approval = ApprovalCheck("Kitty", 1200, TabM = 5) # 120, 135, 150, Taboo -200(320)
    
    if not K_Tit and "no titjob" not in K_RecentActions:        
        call KittyFace("surprised", 1)
        $ K_Mouth = "kiss"
        ch_k "You want to rub your cock against my. . . breasts?"  
            
    if not K_Tit and Approval:                                                 #First time dialog    
        if K_Forced: 
            call KittyFace("sad")
            call Statup("Kitty", "Love", 70, -3, 1)
            call Statup("Kitty", "Love", 20, -2, 1)
        elif K_Love >= (K_Obed + K_Inbt):
            call KittyFace("sexy")
            $ K_Brows = "sad"
            $ K_Mouth = "smile" 
            ch_k "It's nice that you even thought about it."            
        elif K_Obed >= K_Inbt:
            call KittyFace("normal")
            ch_k "I mean. . ."              
        elif K_Addict >= 50:
            call KittyFace("manic", 1)
            ch_k "Hmmmm. . . ."     
        else: # Uninhibited 
            call KittyFace("sad")
            $ K_Mouth = "smile"             
            ch_k "Hadn't really considered that."      
    elif Approval:                                                                       #Second time+ dialog
        if K_Forced: 
            call KittyFace("sad")
            call Statup("Kitty", "Love", 70, -3, 1)
            call Statup("Kitty", "Love", 20, -2, 1)
            ch_k "This isn't going to become a habit, will it?"
        elif not Taboo and "tabno" in K_DailyActions:        
            ch_k "Ok, I guess this is private enough. . ."   
        elif "titjob" in K_RecentActions:
            call KittyFace("sexy", 1)
            ch_k "Mmm, again?"
            jump KTJ_Prep
        elif "titjob" in K_DailyActions:
            call KittyFace("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",   
                "You're going to make me sore.", 
                "Didn't get enough earlier?",
                "My tits are still kinda sore from earlier."]) 
            ch_k "[Line]"
        elif K_Tit < 3:        
            call KittyFace("sexy", 1)
            $ K_Brows = "confused"
            $ K_Mouth = "kiss"
            ch_k "So you'd like another titjob?"        
        else:       
            call KittyFace("sexy", 1)
            $ Kitty_Arms = 2
            $ Line = renpy.random.choice(["You want some of this action [rubs her chest]?",                 
                "So you'd like another titjob?",                  
                "So you'd like another titjob?",                               
                "So you'd like another titjob?",                              
                "A little. . . puffpuff?", 
                "A little soft embrace?"]) 
            ch_k "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if K_Forced:
            call KittyFace("sad")
            call Statup("Kitty", "Obed", 90, 1)
            call Statup("Kitty", "Inbt", 60, 1)
            ch_k "Well, could be worse. . ." 
        elif "no titjob" in K_DailyActions:               
            ch_k "Hmm, I guess. . ."       
        else:
            call KittyFace("sexy", 1)
            call Statup("Kitty", "Love", 90, 1)
            call Statup("Kitty", "Inbt", 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, put it here.",                 
                "Well. . . ok.",                 
                "Yum.", 
                "Sure, whip it out.",
                "Fine. . . [She drools a bit into her cleavage].",
                "Heh, ok."]) 
            ch_k "[Line]"
            $ Line = 0
        call Statup("Kitty", "Obed", 20, 1) 
        call Statup("Kitty", "Obed", 70, 1)      
        call Statup("Kitty", "Inbt", 80, 2) 
        jump KTJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call KittyFace("angry")
        if "no titjob" in K_RecentActions:  
            ch_k "I {i}just{/i} told you \"no,\" [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions and "no titjob" in K_DailyActions:  
            ch_k "This is just way too exposed!"     
        elif "no titjob" in K_DailyActions:       
            ch_k "I already told you \"no,\" [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "This is just way too exposed!"     
        elif not K_Tit:
            call KittyFace("bemused")
            ch_k "I'm not really up for that, [K_Petname]. . ."
        else:
            call KittyFace("bemused")
            ch_k "Not, right now [K_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no titjob" in K_DailyActions:
                call KittyFace("bemused")
                ch_k "Yeah, ok, [K_Petname]."              
                return
            "Maybe later?" if "no titjob" not in K_DailyActions:
                call KittyFace("sexy")  
                ch_k "Maybe."
                call Statup("Kitty", "Love", 80, 2)
                call Statup("Kitty", "Inbt", 70, 2)   
                if Taboo:                    
                    $ K_RecentActions.append("tabno")                      
                    $ K_DailyActions.append("tabno") 
                $ K_RecentActions.append("no titjob")                      
                $ K_DailyActions.append("no titjob")            
                return
            "I think this could be fun for both of us. . .":             
                if Approval:
                    call KittyFace("sexy")     
                    call Statup("Kitty", "Obed", 80, 2)
                    call Statup("Kitty", "Obed", 40, 2)
                    call Statup("Kitty", "Inbt", 70, 3) 
                    call Statup("Kitty", "Inbt", 40, 2) 
                    $ Line = renpy.random.choice(["Well, ok, put it here.",                 
                        "Well. . . ok.",                 
                        "I guess.", 
                        "I guess, whip it out.",
                        "Fine. . . [She drools a bit into her cleavage].",
                        "Heh, ok."])
                    ch_k "[Line]"
                    $ Line = 0    
                    jump KTJ_Prep
                else:   
                    $ Approval = ApprovalCheck("Kitty", 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)             Handy instead?
                    if Approval >= 2 and K_Blow:       
                        call Statup("Kitty", "Inbt", 80, 1) 
                        call Statup("Kitty", "Inbt", 60, 3) 
                        call KittyFace("confused", 1)
                        ch_k "Could I[K_like]. . . blow you instead?"
                        menu:
                            ch_k "What do you say [[blowjob]?"
                            "Ok, get down there.":
                                call Statup("Kitty", "Love", 80, 2)  
                                call Statup("Kitty", "Inbt", 60, 1)                                
                                call Statup("Kitty", "Obed", 50, 1) 
                                jump KBJ_Prep
                            "Nah, it's all about dem titties.":  
                                $ Line = "no BJ"
                    if Approval and K_Hand:       
                        call Statup("Kitty", "Inbt", 80, 1) 
                        call Statup("Kitty", "Inbt", 60, 3) 
                        call KittyFace("confused", 1)
                        ch_k "Maybe you'd[K_like]settle for a handy?"
                        menu:
                            ch_k "What do you say?"
                            "Sure, that's fine.":
                                call Statup("Kitty", "Love", 80, 2)  
                                call Statup("Kitty", "Inbt", 60, 1)                                
                                call Statup("Kitty", "Obed", 50, 1) 
                                jump KHJ_Prep
                            "Seriously, titties." if Line == "no BJ":  
                                $ Line = 0
                            "Nah, it's all about dem titties." if Line != "no BJ":  
                                pass
                    call Statup("Kitty", "Love", 200, -2)                 
                    ch_k "Nah."  
                    call Statup("Kitty", "Obed", 70, 2) 
                    
                    
            "Come on, let me fuck those titties, [K_Pet]":                                               # Pressured into it                
                call Kitty_Namecheck
                $ Approval = ApprovalCheck("Kitty", 700, "OI", TabM = 4) # 70, 85, 100, -160(230)
                if Approval > 1 or (Approval and K_Forced):
                    call KittyFace("sad")
                    call Statup("Kitty", "Love", 70, -5, 1)
                    call Statup("Kitty", "Love", 200, -2)                 
                    ch_k "Ok, fine, whip it out."  
                    call Statup("Kitty", "Obed", 50, 4)
                    call Statup("Kitty", "Inbt", 80, 1) 
                    call Statup("Kitty", "Inbt", 60, 3)  
                    $ K_Forced = 1
                    jump KTJ_Prep
                else:                              
                    call Statup("Kitty", "Love", 200, -15)     
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")   
    
    #She refused all offers.   
    if "no titjob" in K_DailyActions:
        call KittyFace("angry", 1)
        ch_k "Look, I already told you no thanks, [K_Petname]."   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1)
        ch_k "No, that's just weird."
        call Statup("Kitty", "Lust", 200, 5)      
        if K_Love > 300:
                call Statup("Kitty", "Love", 70, -2)
        call Statup("Kitty", "Obed", 50, -2)      
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call KittyFace("angry", 1)          
        $ K_DailyActions.append("tabno") 
        ch_k "You really expect me to do that here? You realize how. . . exposed that would be?"
        call Statup("Kitty", "Lust", 200, 5)  
        call Statup("Kitty", "Obed", 50, -3)  
    elif K_Tit:
        call KittyFace("sad") 
        ch_k "I think I'll let you know when I want you touching these again."       
    else:
        call KittyFace("normal", 1)
        ch_k "How about let's not, [K_Petname]."
    $ K_RecentActions.append("no titjob")                      
    $ K_DailyActions.append("no titjob") 
    $ Tempmod = 0    
    return
    
label K_TJ_Prep:
label KTJ_Prep:
      
    if Taboo:
        $ K_Inbt += int(Taboo/10)  
        $ K_Lust += int(Taboo/5)

        
    call KittyFace("sexy")
    if K_Forced:
        call KittyFace("sad")
    elif K_Tit:
        $ K_Brows = "confused"
        $ K_Eyes = "sexy"
        $ K_Mouth = "smile"
        
    call Seen_First_Peen("Kitty",Partner,React=Situation)
    call Kitty_TJ_Launch("L") 
    
    if Situation == "Kitty":                                                               
            #Kitty auto-starts   
            $ Situation = 0
            call Kitty_TJ_Launch("L")            
            "Kitty slides down and presses your dick between her tits."
            menu:
                "What do you do?"
                "Nothing.":                    
                    call Statup("Kitty", "Inbt", 80, 3) 
                    call Statup("Kitty", "Inbt", 40, 2)                     
                    "Kitty starts to slide up and down."
                "Praise her.":       
                    call KittyFace("sexy", 1)                    
                    call Statup("Kitty", "Inbt", 80, 3) 
                    ch_p "Oh, that sounds like a good idea, [K_Pet]."
                    call Kitty_Namecheck
                    "Kitty continues her actions."
                    call Statup("Kitty", "Love", 85, 1)
                    call Statup("Kitty", "Obed", 90, 1)
                    call Statup("Kitty", "Obed", 50, 2)
                "Ask her to stop.":     
                    call KittyFace("confused")  
                    call Statup("Kitty", "Inbt", 70, 1) 
                    ch_p "Let's not do that for now, [K_Pet]."
                    call Kitty_Namecheck
                    "Kitty lets it drop out from between her breasts."
                    call Statup("Kitty", "Obed", 90, 1)
                    call Statup("Kitty", "Obed", 50, 3)
                    $ P_RecentActions.append("nope")      
                    call AnyWord("Kitty",1,"refused","refused")  
                    return 
    if not K_Tit:        
        if K_Forced:
            call Statup("Kitty", "Love", 90, -25)
            call Statup("Kitty", "Obed", 70, 30)
            call Statup("Kitty", "Inbt", 80, 35) 
        else:
            call Statup("Kitty", "Love", 90, 5)
            call Statup("Kitty", "Obed", 70, 25)
            call Statup("Kitty", "Inbt", 80, 30)   
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0  
    if Taboo:
        call DrainWord("Kitty","tabno")
    call DrainWord("Kitty","no titjob")
    $ K_RecentActions.append("titjob")                      
    $ K_DailyActions.append("titjob") 

label KTJ_Cycle: #Repeating strokes  
    while Round >=0:  
        call Shift_Focus("Kitty") 
        call Kitty_TJ_Launch    
        call KittyLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                           
                        "Start moving? . ." if Speed == 0:
                                    $ Speed = 1
                            
                        "Speed up. . ." if  Speed == 1:                    
                                    $ Speed = 2
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 2:
                                    pass
                            
                        "Stop moving" if Speed == 1 or Speed == 3:                                          
                                    $ Speed = 0
                        "Slow Down. . ." if Speed == 2:                    
                                    $ Speed = 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
                                    
                        "Lick it" if Speed != 3:
                                    $ Speed = 3
                        "Lick it (locked)" if Speed == 3:
                                    pass
                                    
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
                                    "I also want to fondle her breasts." if Trigger2 != "fondle breasts":
                                            if K_Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ K_Action -= 1
                                            else:
                                                ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"  
                                         
                                    "Shift primary action":
                                            if K_Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                if K_Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call KTJ_After                
                                                                    call K_Blowjob
                                                                else:
                                                                    ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."
                                                                    
                                                        "How about a handy?":
                                                                if K_Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call KBJ_After
                                                                    call K_Handjob
                                                                else:
                                                                    ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."                                                            
                                                        "Never Mind":
                                                                jump KTJ_Cycle
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
                                                        jump KTJ_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump KTJ_Cycle 
                                            "Never mind":
                                                        jump KTJ_Cycle 
                                    "Undress Kitty":
                                            call K_Undress   
                                    "Clean up Kitty (locked)" if not K_Spunk:
                                            pass  
                                    "Clean up Kitty" if K_Spunk:
                                            call Kitty_Cleanup("ask")                                         
                                    "Never mind":
                                            jump KTJ_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Kitty_TJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump KTJ_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Kitty_TJ_Reset
                                    $ Line = 0
                                    jump KTJ_After
        #End menu (if Line)
        
        call Shift_Focus("Kitty")  
        call Sex_Dialog("Kitty",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or K_Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PK_Cumming
                            if "angry" in K_RecentActions:  
                                call Kitty_TJ_Reset
                                return    
                            call Statup("Kitty", "Lust", 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2 and K_SEXP >= 20:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump KTJ_After 
                            $ Line = "came"
     
                    if K_Lust >= 100:  
                            #If Kitty can cum                                             
                            call K_Cumming
                            if Situation == "shift" or "angry" in K_RecentActions:
                                jump KTJ_After
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in K_RecentActions:#And Kitty is unsatisfied,  
                                "Kitty still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump KTJ_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Kitty")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if K_SEXP >= 100 or ApprovalCheck("Kitty", 1200, "LO"):
                pass
        elif Cnt == (5 + K_Tit):
                $ K_Brows = "confused"
                ch_k "Are you getting close here? I'm getting as little sore."        
        if Cnt == (10 + K_Tit):
                $ K_Brows = "angry"        
                menu:
                    ch_k "I'm getting rug-burn here [K_Petname]. Can we do something else?"
                    "How about a BJ?" if K_Action and MultiAction:
                        $ Situation = "shift"
                        call KTJ_After
                        call K_Blowjob 
                        return
                    "Finish up." if P_FocusX:
                        "You release your concentration. . ."             
                        $ P_FocusX = 0
                        $ P_Focus += 15
                        jump KTJ_Cycle                
                    "Let's try something else." if MultiAction: 
                        $ Line = 0
                        call Kitty_TJ_Reset
                        $ Situation = "shift"
                        jump KTJ_After
                    "No, get back down there.":
                        if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                            call Statup("Kitty", "Love", 200, -5)
                            call Statup("Kitty", "Obed", 50, 3)                    
                            call Statup("Kitty", "Obed", 80, 2)
                            "She grumbles but gets back to work."
                        else:
                            call KittyFace("angry", 1)   
                            "She scowls at you, drops you cock and pulls back."
                            ch_k "Well fuck you then."                      
                            call Statup("Kitty", "Love", 50, -3, 1)
                            call Statup("Kitty", "Love", 80, -4, 1)
                            call Statup("Kitty", "Obed", 30, -1, 1)                    
                            call Statup("Kitty", "Obed", 50, -1, 1)  
                            $ K_RecentActions.append("angry")
                            $ K_DailyActions.append("angry")   
                            jump KTJ_After
            #End Count check
               
        call Escalation("Kitty","K") #sees if she wants to escalate things
        
        if Round == 10:
            ch_k "It's kinda time to get moving."   
        elif Round == 5:
            ch_k "For real[K_like]time's up."      
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0)
    $ Line = 0
    ch_k "Ok, we need to take a break."
        
label KTJ_After:    
    call KittyFace("sexy")  
        
    $ K_Tit += 1
    $ K_Action -=1
    $ K_Addictionrate += 1
    if "addictive" in P_Traits:
        $ K_Addictionrate += 1
        
    call Partner_Like("Kitty",4)
            
    if K_Tit > 5:
        pass    
    elif K_Tit == 1:
        $ K_SEXP += 12
        if K_Love >= 500:
            $ K_Mouth = "smile"
            ch_k "That was kinda fun."
        elif P_Focus <= 20:
            $ K_Mouth = "sad"
            ch_k "Well I hope you got something out of that."        
    elif K_Tit == 5:
            ch_k "Huh, I guess these are good for something."   
            
    $ Tempmod = 0    
    
    if Situation == "shift":
            ch_k "Mmm, so what else did you have in mind?"
    else:
            call Kitty_TJ_Reset    
    call Checkout
    return

## end K_Titjob //////////////////////////////////////////////////////////////////////

# K_Blowjob //////////////////////////////////////////////////////////////////////

label K_Blowjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Kitty")
    if K_Blow >= 7: # She loves it
        $ Tempmod += 15  
    elif K_Blow >= 3: #You've done it before several times
        $ Tempmod += 10
    elif K_Blow: #You've done it before
        $ Tempmod += 7    
        
    if K_Addict >= 75 and K_Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 25
    elif K_Addict >= 75: #She's really strung out
        $ Tempmod += 15
        
    if Situation == "shift":
        $ Tempmod += 15
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
        
    if "no blow" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no blow" in K_RecentActions else 0    
    
    $ Approval = ApprovalCheck("Kitty", 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)
    
    if not K_Blow and "no blow" not in K_RecentActions:        
        call KittyFace("surprised", 2)
        $ K_Mouth = "kiss"
        ch_k "You want me to suck your dick?"
        if K_Hand:          
            $ K_Mouth = "smile"
            ch_k "Not satisfied with handies?"        
        $ K_Blush = 1
            
    if not K_Blow and Approval:                                                 #First time dialog        
        if K_Forced: 
            call KittyFace("sad")
            call Statup("Kitty", "Love", 70, -3, 1)
            call Statup("Kitty", "Love", 20, -2, 1)
        elif K_Love >= (K_Obed + K_Inbt):
            call KittyFace("sexy")
            $ K_Brows = "sad"
            $ K_Mouth = "smile" 
            ch_k "I have wondered what you. . . taste like."            
        elif K_Obed >= K_Inbt:
            call KittyFace("normal")
            ch_k "If you want me to. . ."               
        elif K_Addict >= 50:
            call KittyFace("manic", 1)
            ch_k "My mouth is watering. . ."   
        else: # Uninhibited 
            call KittyFace("sad")
            $ K_Mouth = "smile"             
            ch_k "[K_Like]sure. . ."       
    elif Approval:                                                                       #Second time+ dialog
        if K_Forced: 
            call KittyFace("sad")
            call Statup("Kitty", "Love", 70, -3, 1)
            call Statup("Kitty", "Love", 20, -2, 1)
            ch_k "You want me to do that again?"
        elif not Taboo and "tabno" in K_DailyActions:        
            ch_k "Ok, I guess this is private enough. . ."    
        elif "blow" in K_RecentActions:
            call KittyFace("sexy", 1)
            ch_k "Mmm, again? [[stretches her jaw]"
            jump KBJ_Prep                
        elif "blow" in K_DailyActions:
            call KittyFace("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",   
                "You're going to give me lockhee- . . . jaw.", 
                "Let me get some saliva going.",
                "Didn't get enough earlier?",
                "My jaw's still a bit sore from earlier.",
                "My jaw's still a bit sore from earlier."]) 
            ch_k "[Line]"
        elif K_Blow < 3:        
            call KittyFace("sexy", 1)
            $ K_Brows = "confused"
            $ K_Mouth = "kiss"
            ch_k "So you'd like another blowjob?"        
        else:       
            call KittyFace("sexy", 1)
            $ Kitty_Arms = 2
            $ Line = renpy.random.choice(["You want me to [mimes blowing]?",                 
                "So you wanna 'nother blowjob?",                 
                "A little. . . lick?", 
                "You want me to suck you off?",
                "A little tlc?"]) 
            ch_k "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if K_Forced:
            call KittyFace("sad")
            call Statup("Kitty", "Obed", 90, 1)
            call Statup("Kitty", "Inbt", 60, 1)
            ch_k "Whatever."    
        elif "no blow" in K_DailyActions:               
            ch_k "Ok, fine, I suppose it isn't {i}sooo{/i} bad. . ."  
        else:
            call KittyFace("sexy", 1)
            call Statup("Kitty", "Love", 90, 1)
            call Statup("Kitty", "Inbt", 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, ahhhhhh.",                 
                "Well. . . ok.",                 
                "Yum.", 
                "Sure, whip it out.",
                "Ok. . . [She licks her lips].",
                "Lol, ok, alright."]) 
            ch_k "[Line]"
            $ Line = 0
        call Statup("Kitty", "Obed", 20, 1) 
        call Statup("Kitty", "Obed", 70, 1)      
        call Statup("Kitty", "Inbt", 80, 2) 
        jump KBJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call KittyFace("angry")
        if "no blow" in K_RecentActions:  
            ch_k "What did I[K_like]{i}just{/i} tell you [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions and "no blow" in K_DailyActions:  
            ch_k "I told you, not in public!"  
        elif "no blow" in K_DailyActions:       
            ch_k "I told you \"no,\" [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "I told you this is too public!"      
        elif not K_Blow:
            call KittyFace("bemused")
            ch_k "I don't know about the taste, [K_Petname]. . ."
        else:
            call KittyFace("bemused")
            ch_k "Later, [K_Petname]!"
        menu:
            extend ""
            "Sorry, never mind." if "no blow" in K_DailyActions:
                call KittyFace("bemused")
                ch_k "Aw, it's ok, [K_Petname]."              
                return
            "Maybe later?" if "no blow" not in K_DailyActions:
                call KittyFace("sexy")  
                ch_k "You[K_like]never know, [K_Petname]."
                call Statup("Kitty", "Love", 80, 2)
                call Statup("Kitty", "Inbt", 70, 2)   
                if Taboo:                    
                    $ K_RecentActions.append("tabno")                      
                    $ K_DailyActions.append("tabno") 
                $ K_RecentActions.append("no blow")                      
                $ K_DailyActions.append("no blow")            
                return
            "Come on, please?":             
                if Approval:
                    call KittyFace("sexy")     
                    call Statup("Kitty", "Obed", 90, 2)
                    call Statup("Kitty", "Obed", 50, 2)
                    call Statup("Kitty", "Inbt", 70, 3) 
                    call Statup("Kitty", "Inbt", 40, 2) 
                    $ Line = renpy.random.choice(["Well, sure, I guess.",                 
                        "Well. . . ok.",                 
                        "I could maybe give it a try.", 
                        "I guess I could. . .",
                        "Fiiine. . . [She licks her lips].",
                        "Heh, ok, fine."]) 
                    ch_k "[Line]"
                    $ Line = 0                   
                    jump KBJ_Prep
                else:   
                    if ApprovalCheck("Kitty", 1100, TabM = 3): # 110, 125, 140, Taboo -120(230)             Handy instead?    
                        call Statup("Kitty", "Inbt", 80, 1) 
                        call Statup("Kitty", "Inbt", 60, 3) 
                        call KittyFace("confused", 1)
                        $ Kitty_Arms = 1
                        if K_Hand:
                            ch_k "Maybe I could just use my hand?"
                        else:
                            ch_k "I could maybe. . . [[she makes a jerking motion with her hand]?"
                        menu:
                            ch_k "Would that work?"
                            "Sure, that's fine.":
                                call Statup("Kitty", "Love", 80, 2)  
                                call Statup("Kitty", "Inbt", 60, 1)                                
                                call Statup("Kitty", "Obed", 50, 1) 
                                jump KHJ_Prep
                            "Nah, if it's not a BJ, forget it.":
                                call Statup("Kitty", "Love", 200, -2)                                
                                $ Kitty_Arms = 0                
                                ch_k "Ok, your loss."  
                                call Statup("Kitty", "Obed", 70, 2)  
                    
                    
            "Suck it, [K_Pet]":                                               # Pressured into it                
                call Kitty_Namecheck
                $ Approval = ApprovalCheck("Kitty", 750, "OI", TabM = 3) # 75, 90, 105, -120(195)
                if Approval > 1 or (Approval and K_Forced):
                    call KittyFace("sad")
                    call Statup("Kitty", "Love", 70, -5, 1)
                    call Statup("Kitty", "Love", 200, -2)                 
                    ch_k "Ok, fine. . ."  
                    call Statup("Kitty", "Obed", 50, 4)
                    call Statup("Kitty", "Inbt", 80, 1) 
                    call Statup("Kitty", "Inbt", 60, 3)  
                    $ K_Forced = 1
                    jump KBJ_Prep
                else:                              
                    call Statup("Kitty", "Love", 200, -15)     
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")   
    
    #She refused all offers.   
    if "no blow" in K_DailyActions:
        call KittyFace("angry", 1)
        ch_k "You can eat a dick, 'cos I'm not."   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1)
        ch_k "I just can't do that!"
        call Statup("Kitty", "Lust", 200, 5)     
        if K_Love > 300:
                call Statup("Kitty", "Love", 70, -2)
        call Statup("Kitty", "Obed", 50, -2)      
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
        $ K_RecentActions.append("no blow")                      
        $ K_DailyActions.append("no blow") 
        return
    elif Taboo:                             # she refuses and this is too public a place for her
        call KittyFace("angry", 1)          
        $ K_DailyActions.append("tabno") 
        ch_k "This is way too exposed!"
        call Statup("Kitty", "Lust", 200, 5)  
        call Statup("Kitty", "Obed", 50, -3)    
        return                
    elif K_Blow:
        call KittyFace("sad") 
        ch_k "No, not this time."       
    else:
        call KittyFace("normal", 1)
        ch_k "Nope."  
    $ K_RecentActions.append("no blow")                      
    $ K_DailyActions.append("no blow") 
    $ Tempmod = 0    
    return
    

label K_BJ_Prep:
label KBJ_Prep:   
    if renpy.showing("Kitty_HJ_Animation"):
        hide Kitty_HJ_Animation with easeoutbottom
    if Taboo:
        $ K_Inbt += int(Taboo/10)  
        $ K_Lust += int(Taboo/5)
                
    call KittyFace("sexy")
    if K_Forced:
        call KittyFace("sad")
    elif K_Hand:
        $ K_Brows = "confused"
        $ K_Eyes = "sexy"
        $ K_Mouth = "smile"
    
    call Seen_First_Peen("Kitty",Partner,React=Situation)
    call Kitty_BJ_Launch("L")   
    
    if Situation == "Kitty":                                                                  
            #Kitty auto-starts   
            $ Situation = 0      
            "Kitty slides down and gives your cock a little lick."
            menu:
                "What do you do?"
                "Nothing.":                    
                    call Statup("Kitty", "Inbt", 80, 3) 
                    call Statup("Kitty", "Inbt", 40, 2)                     
                    "Kitty continues licking at it."
                "Praise her.":       
                    call KittyFace("sexy", 1)                    
                    call Statup("Kitty", "Inbt", 80, 3) 
                    ch_p "Hmmm, keep doing that, [K_Pet]."
                    call Kitty_Namecheck
                    "Kitty continues her actions."
                    call Statup("Kitty", "Love", 85, 1)
                    call Statup("Kitty", "Obed", 90, 1)
                    call Statup("Kitty", "Obed", 50, 2)
                "Ask her to stop.":     
                    call KittyFace("surprised")  
                    call Statup("Kitty", "Inbt", 70, 1) 
                    ch_p "Let's not do that for now, [K_Pet]."
                    call Kitty_Namecheck
                    "Kitty puts it down."
                    call Statup("Kitty", "Obed", 90, 1)
                    call Statup("Kitty", "Obed", 50, 3)
                    $ P_RecentActions.append("nope")      
                    call AnyWord("Kitty",1,"refused","refused")  
                    return  
    if not K_Blow:        
        if K_Forced:
            call Statup("Kitty", "Love", 90, -70)
            call Statup("Kitty", "Obed", 70, 45)
            call Statup("Kitty", "Inbt", 80, 60) 
        else:
            call Statup("Kitty", "Love", 90, 5)
            call Statup("Kitty", "Obed", 70, 35)
            call Statup("Kitty", "Inbt", 80, 40)     
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Kitty","tabno")
    call DrainWord("Kitty","no blow")
    $ K_RecentActions.append("blow")                      
    $ K_DailyActions.append("blow")     

label KBJ_Cycle: #Repeating strokes  
    while Round >=0:  
        call Shift_Focus("Kitty") 
        call Kitty_BJ_Launch    
        call KittyLust   
        
        if P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                          
                        "Lick it. . ." if Speed != 1:
                                $ Speed = 1   
                        "Lick it. . . (locked)" if Speed == 1:
                                pass  
                            
                        "Just the head. . ." if Speed != 2:
                            $ Speed = 2
                        "Just the head. . . (locked)" if Speed == 2:
                                pass
                            
                        "Suck on it." if Speed != 3:
                                $ Speed = 3  
                                if Trigger2 == "jackin":
                                    "She dips her head a bit lower, and you move your hand out of the way."
                                    
                        "Suck on it. (locked)" if Speed == 3:
                                pass
                            
                        "Take it deeper." if Speed != 4:
                                if "pushed" in K_RecentActions:
                                    ch_k "Sorry, I just can't handle all of you yet."
                                elif K_Blow < 5:
                                    call Statup("Kitty", "Love", 80, -(20-(2*K_Blow))) 
                                    call Statup("Kitty", "Obed", 80, (30-(3*K_Blow)))
                                    "She gags on it slightly and moves back to a more comfortable pace."
                                    $ K_RecentActions.append("pushed")
                                else:
                                    if Trigger2 == "jackin" and Speed != 3:
                                        "She takes it to the root, and you move your hand out of the way."
                                    $ Speed = 4  
                        "Take it deeper. (locked)" if Speed == 4:
                                pass
                            
                        "Set your own pace. . .":                
                                "Kitty hums contentedly."    
                                if "setpace" not in K_RecentActions:
                                    call Statup("Kitty", "Love", 80, 2)
                                $ D20 = renpy.random.randint(1, 20)     
                                if K_Blow < 5:
                                    $ D20 -= 10
                                elif K_Blow < 10:
                                    $ D20 -= 5
                                    
                                if D20 > 15:
                                    $ Speed = 4              
                                    if "setpace" not in K_RecentActions:      
                                        call Statup("Kitty", "Inbt", 80, 3) 
                                elif D20 > 10:
                                    $ Speed = 3
                                elif D20 > 5:
                                    $ Speed = 2
                                else:
                                    $ Speed = 1
                                $ K_RecentActions.append("setpace")
                                
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
                                    "I also want to fondle her breasts." if Trigger2 != "fondle breasts":
                                            if K_Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ K_Action -= 1
                                            else:
                                                ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"  
                                         
                                    "Shift primary action":
                                            if K_Action and MultiAction:
                                                    menu:
                                                        "How about a handy?":
                                                                if K_Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call KBJ_After
                                                                    call K_Handjob
                                                                else:
                                                                    ch_k "I'm kinda tired, could we just wrap this up. . ."
                                                        "How about a titjob?":
                                                                if K_Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call KBJ_After
                                                                    call K_Titjob
                                                                else:
                                                                    ch_k "I'm kinda tired, could we just wrap this up. . ."                                        
                                                        "Never Mind":
                                                                jump KBJ_Cycle
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
                                                        jump KBJ_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump KBJ_Cycle  
                                            "Never mind":
                                                        jump KBJ_Cycle 
                                    "Undress Kitty":
                                            call K_Undress   
                                    "Clean up Kitty (locked)" if not K_Spunk:
                                            pass  
                                    "Clean up Kitty" if K_Spunk:
                                            call Kitty_Cleanup("ask")                                         
                                    "Never mind":
                                            jump KBJ_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Kitty_BJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump KBJ_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Kitty_BJ_Reset
                                    $ Line = 0
                                    jump KBJ_After
        #End menu (if Line)
                    
        call Shift_Focus("Kitty")  
        call Sex_Dialog("Kitty",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
        if Speed:
            $ P_Wet = 1 #wets penis        
            $ P_Spunk = 0 if P_Spunk else P_Spunk #cleans you off after one cycle
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or K_Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PK_Cumming
                            if "angry" in K_RecentActions:  
                                call Kitty_BJ_Reset
                                return    
                            call Statup("Kitty", "Lust", 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2 and K_SEXP >= 20:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump KBJ_After 
                            $ Line = "came"
     
                    if K_Lust >= 100:  
                            #If Kitty can cum                                             
                            call K_Cumming
                            if Situation == "shift" or "angry" in K_RecentActions:
                                jump KBJ_After
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."
                                                        
                            if "unsatisfied" in K_RecentActions:#And Kitty is unsatisfied,  
                                "Kitty still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump KBJ_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Kitty")            
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if K_SEXP >= 100 or ApprovalCheck("Kitty", 1200, "LO"):
            pass
        elif Cnt == (10 + K_Blow):
                $ K_Brows = "angry"        
                menu:
                    ch_k "I'm[K_like]totally worn out here. Can we do something else?"
                    "How about a Handy?" if K_Action and MultiAction:
                            $ Situation = "shift"
                            call KBJ_After
                            call K_Handjob 
                            return
                    "Finish up." if P_FocusX:
                            "You release your concentration. . ."             
                            $ P_FocusX = 0
                            $ P_Focus += 15
                            jump KBJ_Cycle
                    "Let's try something else." if MultiAction: 
                            $ Line = 0
                            call Kitty_BJ_Reset
                            $ Situation = "shift"
                            jump KBJ_After
                    "No, get back down there.":
                            if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):
                                call Statup("Kitty", "Love", 200, -5)
                                call Statup("Kitty", "Obed", 50, 3)
                                call Statup("Kitty", "Obed", 80, 2)
                                "She grumbles but gets back to work."
                            else:
                                call KittyFace("angry", 1)  
                                "She scowls at you, drops you cock and pulls back."
                                ch_k "Well fuck you then."
                                call Statup("Kitty", "Love", 50, -3, 1)
                                call Statup("Kitty", "Love", 80, -4, 1)
                                call Statup("Kitty", "Obed", 30, -1, 1)
                                call Statup("Kitty", "Obed", 50, -1, 1)  
                                $ K_RecentActions.append("angry")
                                $ K_DailyActions.append("angry")   
                                jump KBJ_After        
        elif Cnt == (5 + K_Blow) and K_SEXP <= 100 and not ApprovalCheck("Kitty", 1200, "LO"):
                    $ K_Brows = "confused"
                    ch_k "Are you getting close here? I'm cramping up."  
        #End Count check
        
        call Escalation("Kitty","K") #sees if she wants to escalate things
        
        if Round == 10:
            ch_k "It's kind of time to get moving."   
        elif Round == 5:
            ch_k "For real[K_like]time's up."      
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0)
    $ Line = 0
    ch_k "Ok, I gotta rest my jaw for a minute. . ."

label KBJ_After:    
    call KittyFace("sexy")  
        
    $ K_Blow += 1
    $ K_Action -=1
    $ K_Addictionrate += 1
    if "addictive" in P_Traits:
        $ K_Addictionrate += 1
                
    call Partner_Like("Kitty",2)
            
    if "Kitty Jobber" in Achievements:
        pass
    elif K_Blow >= 10:
        call KittyFace("smile", 1)
        ch_k "I can't[K_like]get your taste out of my mind."      
        $ Achievements.append("Kitty Jobber")
        $K_SEXP += 5
    elif Situation == "shift":
        pass
    elif K_Blow == 1:
            $K_SEXP += 15
            if K_Love >= 500:
                $ K_Mouth = "smile"
                ch_k "Huh, that wasn't bad."
            elif P_Focus <= 20:
                $ K_Mouth = "sad"
                ch_k "I hope you enjoyed that."     
    elif K_Blow == 5:
        ch_k "I'm getting better at this. . . right?"
        menu:
            "[[nod]":
                call KittyFace("smile", 1)
                call Statup("Kitty", "Love", 90, 15)
                call Statup("Kitty", "Obed", 80, 5)
                call Statup("Kitty", "Inbt", 90, 10) 
            "[[shake head \"no\"]":        
                if ApprovalCheck("Kitty", 500, "O"):
                    call KittyFace("sad", 2)
                    call Statup("Kitty", "Love", 200, -5)
                else:
                    call KittyFace("angry", 2)
                    call Statup("Kitty", "Love", 200, -25)
                call Statup("Kitty", "Obed", 80, 10)
                ch_k ". . ."         
                call KittyFace("sad", 1)
    
    $ Tempmod = 0    
    if Situation != "shift":
        call Kitty_BJ_Reset    
    call Checkout
    return
    


# end K_Blowjob                                 //////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label K_Dildo_Check:
    if "dildo" in P_Inventory:   
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in K_Inventory:
        "You ask Kitty to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1
            
label K_Dildo_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Kitty")
    call K_Dildo_Check    
    if not _return:
        return 

    if K_DildoP: #You've done it before
        $ Tempmod += 15
    if K_Legs == "pants:": # she's got pants on.
        $ Tempmod -= 20
        
    if K_Lust > 95:
        $ Tempmod += 20    
    elif K_Lust > 85: #She's really horny
        $ Tempmod += 15
        
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
        
    if "no dildo" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no dildo" in K_RecentActions else 0       
        
    $ Approval = ApprovalCheck("Kitty", 1250, TabM = 4) # 125, 140, 155, Taboo -160(335)
    
    if Situation == "Kitty":                                                                  #Kitty auto-starts   
                if Approval > 2:                                                      # fix, add kitty auto stuff here
                    if K_Legs == "blue skirt":
                        "Kitty grabs her dildo, hiking up her skirt as she does."
                        $ K_Upskirt = 1
                    elif K_Legs == "pants":
                        "Kitty grabs her dildo, pulling down her pants as she does."              
                        $ K_Legs = 0
                    else:
                        "Kitty grabs her dildo, rubbing is suggestively against her crotch."
                    $ K_SeenPanties = 1
                    "She slides the tip along her pussy and seems to want you to insert it."
                    menu:
                        "What do you do?"
                        "Nothing.":                    
                            call Statup("Kitty", "Inbt", 80, 3) 
                            call Statup("Kitty", "Inbt", 50, 2)
                            "Kitty slides it in."
                        "Go for it.":       
                            call KittyFace("sexy", 1)                    
                            call Statup("Kitty", "Inbt", 80, 3) 
                            ch_p "Oh yeah, [K_Pet], let's do this."
                            call Kitty_Namecheck
                            "You grab the dildo and slide it in."
                            call Statup("Kitty", "Love", 85, 1)
                            call Statup("Kitty", "Obed", 90, 1)
                            call Statup("Kitty", "Obed", 50, 2)
                        "Ask her to stop.":
                            call KittyFace("surprised")       
                            call Statup("Kitty", "Inbt", 70, 1) 
                            ch_p "Let's not do that right now, [K_Pet]."
                            call Kitty_Namecheck
                            "Kitty sets the dildo down."
                            call KittyOutfit
                            call Statup("Kitty", "Obed", 90, 1)
                            call Statup("Kitty", "Obed", 50, 1)
                            call Statup("Kitty", "Obed", 30, 2)
                            return            
                    jump KDP_Prep
                else:                
                    $ Tempmod = 0                               # fix, add kitty auto stuff here
                    $ Trigger2 = 0
                return            
    
    if Situation == "auto":    
                "You rub the dildo across her body, and along her moist slit."
                call KittyFace("surprised", 1)
                
                if (K_DildoP and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
                    "Kitty is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                    call KittyFace("sexy")
                    call Statup("Kitty", "Obed", 70, 3)
                    call Statup("Kitty", "Inbt", 50, 3) 
                    call Statup("Kitty", "Inbt", 70, 1) 
                    ch_k "Ooo, [K_Petname], toys!"            
                    jump KDP_Prep         
                else:                                                                                                            #she's questioning it
                    $ K_Brows = "angry"                
                    menu:
                        ch_k "Hey, what are you planning to do with that?!" 
                        "Sorry, sorry! Never mind.":
                            if Approval:     
                                call KittyFace("sexy", 1)
                                call Statup("Kitty", "Obed", 70, 3)
                                call Statup("Kitty", "Inbt", 50, 3) 
                                call Statup("Kitty", "Inbt", 70, 1) 
                                ch_k "Well, now that you mention it. . ."
                                jump KDP_Prep
                            "You pull back before you really get it in."                    
                            call KittyFace("bemused", 1)
                            if K_DildoP:
                                ch_k "Well ok, [K_Petname], maybe warn me next time?" 
                            else:
                                ch_k "Well ok, [K_Petname], that's a little much. . . for now . . ."                                               
                        "Just playing with my favorite toys.":                    
                            call Statup("Kitty", "Love", 80, -10, 1)  
                            call Statup("Kitty", "Love", 200, -10)
                            "You press it inside some more."                              
                            call Statup("Kitty", "Obed", 70, 3)
                            call Statup("Kitty", "Inbt", 50, 3) 
                            if not ApprovalCheck("Kitty", 700, "O", TabM=1): #Checks if Obed is 700+                             
                                call KittyFace("angry")
                                "Kitty shoves you away and slaps you in the face."
                                ch_k "Jerk!"
                                ch_k "Ask nice if you want to stick something in my pussy!"                                               
                                call Statup("Kitty", "Love", 50, -10, 1)                        
                                call Statup("Kitty", "Obed", 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                if renpy.showing("Kitty_SexSprite"):
                                    call Kitty_Sex_Reset 
                                $ K_RecentActions.append("angry")
                                $ K_DailyActions.append("angry")                          
                            else:
                                call KittyFace("sad")
                                "Kitty doesn't seem to be into this, you're lucky she's so obedient."                        
                                jump KDP_Prep
                return             
    #end Auto
   
    if not K_DildoP:                                                               
            #first time    
            call KittyFace("surprised", 1)
            $ K_Mouth = "kiss"
            ch_k "Hmmm, so you'd like to try out some toys?"    
            if K_Forced:
                call KittyFace("sad")
                ch_k "I suppose there are worst things you could ask for."
            
    if not K_DildoP and Approval:                                                 
            #First time dialog        
            if K_Forced: 
                call KittyFace("sad")
                call Statup("Kitty", "Love", 70, -3, 1)
                call Statup("Kitty", "Love", 20, -2, 1)
            elif K_Love >= (K_Obed + K_Inbt):
                call KittyFace("sexy")
                $ K_Brows = "sad"
                $ K_Mouth = "smile" 
                ch_k "I've had a reasonable amount of experience with these, you know. . ."            
            elif K_Obed >= K_Inbt:
                call KittyFace("normal")
                ch_k "If that's what you want, [K_Petname]. . ."            
            else: # Uninhibited 
                call KittyFace("sad")
                $ K_Mouth = "smile"             
                ch_k "I guess it could be fun with a partner. . ."    
            
    elif Approval:                                                                       
            #Second time+ dialog
            if K_Forced: 
                call KittyFace("sad")
                call Statup("Kitty", "Love", 70, -3, 1)
                call Statup("Kitty", "Love", 20, -2, 1)
                ch_k "The toys again?" 
            elif not Taboo and "tabno" in K_DailyActions:        
                ch_k "Well, at least you got us some privacy this time. . ."   
            elif "dildo pussy" in K_RecentActions:
                call KittyFace("sexy", 1)
                ch_k "Mmm, again? Ok, let's get to it."
                jump KDP_Prep
            elif "dildo pussy" in K_DailyActions:
                call KittyFace("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "You're going to wear me out."]) 
                ch_k "[Line]"
            elif K_DildoP < 3:        
                call KittyFace("sexy", 1)
                $ K_Brows = "confused"
                $ K_Mouth = "kiss"
                ch_k "You want to stick it in my pussy again?"       
            else:       
                call KittyFace("sexy", 1)
                $ Kitty_Arms = 2
                $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my pussy again?",
                    "You want me ta lube up your toy?"]) 
                ch_k "[Line]"
                $ Line = 0
            
    if Approval >= 2:                                                                   
            #She's into it. . .               
            if K_Forced:
                call KittyFace("sad")
                call Statup("Kitty", "Obed", 90, 1)
                call Statup("Kitty", "Inbt", 60, 1)
                ch_k "Ok, fine."    
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
            jump KDP_Prep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            call KittyFace("angry")
            if "no dildo" in K_RecentActions:  
                ch_k "What part of \"no,\" did you not get, [K_Petname]?"
            elif Taboo and "tabno" in K_DailyActions and "no dildo" in K_DailyActions:
                ch_k "Stop swinging that thing around in public!"   
            elif "no dildo" in K_DailyActions:       
                ch_k "I already told you \"no,\" [K_Petname]."
            elif Taboo and "tabno" in K_DailyActions:  
                ch_k "Stop swinging that thing around in public!"  
            elif not K_DildoP:
                call KittyFace("bemused")
                ch_k "I'm just not into toys, [K_Petname]. . ."
            else:
                call KittyFace("bemused")
                ch_k "I don't think we need any toys, [K_Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in K_DailyActions:
                    call KittyFace("bemused")
                    ch_k "Yeah, ok, [K_Petname]."              
                    return
                "Maybe later?" if "no dildo" not in K_DailyActions:
                    call KittyFace("sexy")  
                    ch_k "Maybe I'll practice on my own time, [K_Petname]."
                    call Statup("Kitty", "Love", 80, 2)
                    call Statup("Kitty", "Inbt", 70, 2)  
                    if Taboo:                    
                        $ K_RecentActions.append("tabno")                      
                        $ K_DailyActions.append("tabno") 
                    $ K_RecentActions.append("no dildo")                      
                    $ K_DailyActions.append("no dildo") 
                    return
                "I think you'd like it. . .":             
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
                        jump KDP_Prep
                    else:   
                        pass
                        
                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Kitty", 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                    if Approval > 1 or (Approval and K_Forced):
                        call KittyFace("sad")
                        call Statup("Kitty", "Love", 70, -5, 1)
                        call Statup("Kitty", "Love", 200, -5)                 
                        ch_k "Ok, fine. If we're going to do this, stick it in already."  
                        call Statup("Kitty", "Obed", 80, 4)
                        call Statup("Kitty", "Inbt", 80, 1) 
                        call Statup("Kitty", "Inbt", 60, 3)  
                        $ K_Forced = 1  
                        jump KDP_Prep
                    else:                              
                        call Statup("Kitty", "Love", 200, -20)     
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Kitty_Arms = 1  
    if "no dildo" in K_DailyActions:
            ch_k "Learn to take \"no\" for an answer, [K_Petname]."   
            $ K_RecentActions.append("angry")
            $ K_DailyActions.append("angry")   
    elif K_Forced:
            call KittyFace("angry", 1)
            ch_k "I'm not going to let you use that on me."
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
            ch_k "Not here!"     
            call Statup("Kitty", "Lust", 200, 5)  
            call Statup("Kitty", "Obed", 50, -3)  
    elif K_DildoP:
            call KittyFace("sad") 
            ch_k "Sorry, you can keep your toys to yourself."     
    else:
            call KittyFace("normal", 1)
            ch_k "No way."  
    $ K_RecentActions.append("no dildo")                      
    $ K_DailyActions.append("no dildo")  
    $ Tempmod = 0    
    return
                
label KDP_Prep: #Animation set-up 
    if Trigger2 == "dildo pussy":
        return
        
    if not K_Forced and Situation != "auto":
        $ Tempmod = 15 if K_Legs == "pants" else 0           
        call Kitty_Bottoms_Off
        if "angry" in K_RecentActions:
            return    
            
    $ Tempmod = 0      
    call K_Pussy_Launch("dildo pussy")
    if not K_DildoP:        
        if K_Forced:
            call Statup("Kitty", "Love", 90, -75)
            call Statup("Kitty", "Obed", 70, 60)
            call Statup("Kitty", "Inbt", 80, 35) 
        else:
            call Statup("Kitty", "Love", 90, 10)
            call Statup("Kitty", "Obed", 70, 20)
            call Statup("Kitty", "Inbt", 80, 45)
    if Taboo:
        $ K_Inbt += int(Taboo/10)  
        $ K_Lust += int(Taboo/5)
    
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0    
    $ Cnt = 0
    if Taboo:
        call DrainWord("Kitty","tabno")
    call DrainWord("Kitty","no dildo")
    $ K_RecentActions.append("dildo pussy")                      
    $ K_DailyActions.append("dildo pussy") 
    
label KDP_Cycle: #Repeating strokes    
    while Round >=0:  
        call Shift_Focus("Kitty") 
        call K_Pussy_Launch("dildo pussy")
        call KittyLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                               
                        "Slap her ass":                     
                                call K_Slap_Ass
                                jump KDP_Cycle  
                                
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
                                                        "I want to stick a finger in her ass.":
                                                                $ Situation = "shift"
                                                                call KDP_After
                                                                call K_Insert_Ass    
                                                        "Just stick a finger in her ass without asking.":
                                                                $ Situation = "auto"
                                                                call KDP_After
                                                                call K_Insert_Ass                                           
                                                        "I want to shift the dildo to her ass.":
                                                                $ Situation = "shift"
                                                                call KDP_After
                                                                call K_Dildo_Ass   
                                                        "Never Mind":
                                                                jump KDP_Cycle
                                            else: 
                                                ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"           
                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call KDP_After
                                                call Kitty_Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
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
                                                        jump KDP_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump KDP_Cycle  
                                            "Never mind":
                                                        jump KDP_Cycle 
                                    "Undress Kitty":
                                            call K_Undress   
                                    "Clean up Kitty (locked)" if not K_Spunk:
                                            pass  
                                    "Clean up Kitty" if K_Spunk:
                                            call Kitty_Cleanup("ask")                                         
                                    "Never mind":
                                            jump KDP_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call K_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump KDP_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call K_Pos_Reset
                                    $ Line = 0
                                    jump KDP_After
        #End menu (if Line)
        
        if K_Panties or K_Legs == "pants" or HoseNum("Kitty") >= 5: #This checks if Kitty wants to strip down.
                call K_Undress("auto")
            
        call Shift_Focus("Kitty")  
        call Sex_Dialog("Kitty",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or K_Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PK_Cumming
                            if "angry" in K_RecentActions:  
                                call K_Pos_Reset
                                return    
                            call Statup("Kitty", "Lust", 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump KDP_After 
                            $ Line = "came"
     
                    if K_Lust >= 100:  
                            #If Kitty can cum                                             
                            call K_Cumming
                            if Situation == "shift" or "angry" in K_RecentActions:
                                jump KDP_After
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in K_RecentActions:#And Kitty is unsatisfied,  
                                "Kitty still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump KDP_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Kitty")            
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if K_SEXP >= 100 or ApprovalCheck("Kitty", 1200, "LO"):
            pass
        elif Cnt == (5 + K_DildoP):
                    $ K_Brows = "confused"
                    ch_k "What are you even doing down there?" 
        elif K_Lust >= 80:
                    pass
        elif Cnt == (15 + K_DildoP) and K_SEXP >= 15 and not ApprovalCheck("Kitty", 1500):
                    $ K_Brows = "confused"        
                    menu:
                        ch_k "[K_Petname], this is getting uncomfortable, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump KDP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump KDP_After
                        "No, this is fun.":   
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                                    call Statup("Kitty", "Love", 200, -5)
                                    call Statup("Kitty", "Obed", 50, 3)                    
                                    call Statup("Kitty", "Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call KittyFace("angry", 1)   
                                    call K_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_k "Well if that's your attitude, I don't need your \"help\"."                         
                                    call Statup("Kitty", "Love", 50, -3, 1)
                                    call Statup("Kitty", "Love", 80, -4, 1)
                                    call Statup("Kitty", "Obed", 30, -1, 1)                    
                                    call Statup("Kitty", "Obed", 50, -1, 1)  
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump KDP_After
        #End Count check
           
        if Round == 10:
            ch_k "It's kind of time to get moving."   
        elif Round == 5:
            ch_k "For real[K_like]time's up."      
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0)
    $ Line = 0
    ch_k "Ok, we need to take a break."
    
    
label KDP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call K_Pos_Reset
        
    call KittyFace("sexy") 
    
    $ K_DildoP += 1  
    $ K_Action -=1   
            
    call Partner_Like("Kitty",1)
            
    if K_DildoP == 1:            
            $ K_SEXP += 10         
            if not Situation: 
                if K_Love >= 500 and "unsatisfied" not in K_RecentActions:
                    ch_k "Thanks for the extra hand. . ."
                elif K_Obed <= 500 and P_Focus <= 20:
                    call KittyFace("perplexed", 1)
                    ch_k "Did you like that?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_k "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# end K_Dildo Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Insert Ass    

label K_Dildo_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Kitty")
    call K_Dildo_Check
    if not _return:
        return 
      
    if K_Loose:
        $ Tempmod += 30   
    elif "anal" in K_RecentActions or "dildo anal" in K_RecentActions:
        $ Tempmod -= 20 
    elif "anal" in K_DailyActions or "dildo anal" in K_DailyActions:
        $ Tempmod -= 10
    elif (K_Anal + K_DildoA + K_Plug) > 0: #You've done it before
        $ Tempmod += 20   
        
    if K_Legs == "pants:": # she's got pants on.
        $ Tempmod -= 20   
        
    if K_Lust > 95:
        $ Tempmod += 20
    elif K_Lust > 85: #She's really horny
        $ Tempmod += 15
        
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
        
    if "no dildo" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no dildo" in K_RecentActions else 0   
        
    $ Approval = ApprovalCheck("Kitty", 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)
    
    if Situation == "Kitty":                                                                  
            #Kitty auto-starts   
            if Approval > 2:                                                      # fix, add kitty auto stuff here
                if K_Legs == "blue skirt":
                    "Kitty grabs her dildo, hiking up her skirt as she does."
                    $ K_Upskirt = 1
                elif K_Legs == "pants":
                    "Kitty grabs her dildo, pulling down her pants as she does."              
                    $ K_Legs = 0
                else:
                    "Kitty grabs her dildo, rubbing is suggestively against her ass."
                $ K_SeenPanties = 1
                "She slides the tip against her asshole, and seems to want you to insert it."
                menu:
                    "What do you do?"
                    "Nothing.":                    
                        call Statup("Kitty", "Inbt", 80, 3) 
                        call Statup("Kitty", "Inbt", 50, 2)
                        "Kitty slides it in."
                    "Go for it.":       
                        call KittyFace("sexy", 1)                    
                        call Statup("Kitty", "Inbt", 80, 3) 
                        ch_p "Oh yeah, [K_Pet], let's do this."
                        call Kitty_Namecheck
                        "You grab the dildo and slide it in."
                        call Statup("Kitty", "Love", 85, 1)
                        call Statup("Kitty", "Obed", 90, 1)
                        call Statup("Kitty", "Obed", 50, 2)
                    "Ask her to stop.":
                        call KittyFace("surprised")       
                        call Statup("Kitty", "Inbt", 70, 1) 
                        ch_p "Let's not do that right now, [K_Pet]."
                        call Kitty_Namecheck
                        "Kitty sets the dildo down."
                        call KittyOutfit
                        call Statup("Kitty", "Obed", 90, 1)
                        call Statup("Kitty", "Obed", 50, 1)
                        call Statup("Kitty", "Obed", 30, 2)
                        return            
                jump KDA_Prep
            else:                
                $ Tempmod = 0                               # fix, add kitty auto stuff here
                $ Trigger2 = 0
            return            
    
    if Situation == "auto":    
            "You rub the dildo across her body, and against her tight anus."
            call KittyFace("surprised", 1)
            
            if (K_DildoA and Approval) or (Approval > 1):                                                                      
                #this is not the first time you've had sex, or she's into it         
                "Kitty is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                call KittyFace("sexy")
                call Statup("Kitty", "Obed", 70, 3)
                call Statup("Kitty", "Inbt", 50, 3) 
                call Statup("Kitty", "Inbt", 70, 1)
                ch_k "Ooo, [K_Petname], toys!"                
                jump KDA_Prep         
            else:                                                                                                            
                #she's questioning it
                $ K_Brows = "angry"                
                menu:
                    ch_k "Hey, what are you planning to do with that?!" 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            call KittyFace("sexy", 1)
                            call Statup("Kitty", "Obed", 70, 3)
                            call Statup("Kitty", "Inbt", 50, 3) 
                            call Statup("Kitty", "Inbt", 70, 1) 
                            ch_k "Well, now that you mention it. . ."
                            jump KDA_Prep
                        "You pull back before you really get it in."                    
                        call KittyFace("bemused", 1)
                        if K_DildoA:
                            ch_k "Well ok, [K_Petname], maybe warn me next time?" 
                        else:
                            ch_k "Well ok, [K_Petname], that's a little much. . . for now . . ."                                                   
                    "Just playing with my favorite toys.":                    
                        call Statup("Kitty", "Love", 80, -10, 1)  
                        call Statup("Kitty", "Love", 200, -10)
                        "You press it inside some more."                              
                        call Statup("Kitty", "Obed", 70, 3)
                        call Statup("Kitty", "Inbt", 50, 3) 
                        if not ApprovalCheck("Kitty", 700, "O", TabM=1): #Checks if Obed is 700+                           
                            call KittyFace("angry")
                            "Kitty shoves you away and slaps you in the face."
                            ch_k "Jerk!"
                            ch_k "Ask nice if you want to stick something in my ass!"                                                  
                            call Statup("Kitty", "Love", 50, -10, 1)                        
                            call Statup("Kitty", "Obed", 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            if renpy.showing("Kitty_SexSprite"):
                                call Kitty_Sex_Reset 
                            $ K_RecentActions.append("angry")
                            $ K_DailyActions.append("angry")                         
                        else:
                            call KittyFace("sad")
                            "Kitty doesn't seem to be into this, you're lucky she's so obedient."                        
                            jump KDA_Prep
            return             
    #end auto
   
    if not K_DildoA:                                                               
            #first time    
            call KittyFace("surprised", 1)
            $ K_Mouth = "kiss"
            ch_k "You want to try and fit that. . .?"    
            if K_Forced:
                call KittyFace("sad")
                ch_k "Always about the butt, huh?"
    
    if not K_Loose and ("dildo anal" in K_RecentActions or "anal" in K_RecentActions or "dildo anal" in K_DailyActions or "anal" in K_DailyActions):
            call KittyFace("bemused", 1)
            ch_k "I'm still[K_like]sore from earlier. . ."
            
    if not K_DildoA and Approval:                                                 
            #First time dialog        
            if K_Forced: 
                call KittyFace("sad")
                call Statup("Kitty", "Love", 70, -3, 1)
                call Statup("Kitty", "Love", 20, -2, 1)
            elif K_Love >= (K_Obed + K_Inbt):
                call KittyFace("sexy")
                $ K_Brows = "sad"
                $ K_Mouth = "smile" 
                ch_k "I[K_like]haven't actually used one of these, back there before. . ."            
            elif K_Obed >= K_Inbt:
                call KittyFace("normal")
                ch_k "If that's what you want, [K_Petname]. . ."            
            else: # Uninhibited 
                call KittyFace("sad")
                $ K_Mouth = "smile"             
                ch_k "I guess it could be fun two-player. . ."    
            
    elif Approval:                                                                       
            #Second time+ dialog
            if K_Forced: 
                call KittyFace("sad")
                call Statup("Kitty", "Love", 70, -3, 1)
                call Statup("Kitty", "Love", 20, -2, 1)
                ch_k "The toys again?"  
            elif not Taboo and "tabno" in K_DailyActions:        
                ch_k "Well, at least you got us some privacy this time. . ."   
            elif "dildo anal" in K_DailyActions and not K_Loose:
                pass
            elif "dildo anal" in K_DailyActions:
                call KittyFace("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "I'm still a bit sore from earlier.",
                    "You're going to wear me out."]) 
                ch_k "[Line]"
            elif K_DildoA < 3:        
                call KittyFace("sexy", 1)
                $ K_Brows = "confused"
                $ K_Mouth = "kiss"
                ch_k "You want to stick it in my ass again?"       
            else:       
                call KittyFace("sexy", 1)
                $ Kitty_Arms = 2
                $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my ass again?",
                    "You want me ta lube up your toy?"]) 
                ch_k "[Line]"
                $ Line = 0
            
    if Approval >= 2:                                                                  
            #She's into it. . .               
            if K_Forced:
                call KittyFace("sad")
                call Statup("Kitty", "Obed", 90, 1)
                call Statup("Kitty", "Inbt", 60, 1)
                ch_k "Ok, fine."    
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
            jump KDA_Prep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            call KittyFace("angry")
            if "no dildo" in K_RecentActions:  
                ch_k "What part of \"no,\" did you not get, [K_Petname]?"
            elif Taboo and "tabno" in K_DailyActions and "no dildo" in K_DailyActions:
                ch_k "Stop swinging that thing around in public!"  
            elif "no dildo" in K_DailyActions:       
                ch_k "I already told you \"no,\" [K_Petname]."
            elif Taboo and "tabno" in K_DailyActions:  
                ch_k "I already told you that I wouldn't do that out here!"  
            elif not K_DildoA:
                call KittyFace("bemused")
                ch_k "I'm just not into toys, [K_Petname]. . ."
            elif not K_Loose and "dildo anal" not in K_DailyActions:
                call KittyFace("perplexed")
                ch_k "You could have been a bit more gentle last time, [K_Petname]. . ."
            else:
                call KittyFace("bemused")
                ch_k "I don't think we need any toys, [K_Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in K_DailyActions:
                    call KittyFace("bemused")
                    ch_k "Yeah, ok, [K_Petname]."              
                    return
                "Maybe later?" if "no dildo" not in K_DailyActions:
                    call KittyFace("sexy")  
                    ch_k "Maybe I'll practice on my own time, [K_Petname]."
                    call Statup("Kitty", "Love", 80, 2)
                    call Statup("Kitty", "Inbt", 70, 2)  
                    if Taboo:                    
                        $ K_RecentActions.append("tabno")                      
                        $ K_DailyActions.append("tabno") 
                    $ K_RecentActions.append("no dildo")                      
                    $ K_DailyActions.append("no dildo") 
                    return
                "I think you'd like it. . .":             
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
                        jump KDA_Prep
                    else:   
                        pass
                        
                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Kitty", 1050, "OI", TabM = 3) # 105, 120, 135, -120(225)
                    if Approval > 1 or (Approval and K_Forced):
                        call KittyFace("sad")
                        call Statup("Kitty", "Love", 70, -5, 1)
                        call Statup("Kitty", "Love", 200, -5)                 
                        ch_k "Ok, fine. If we're going to do this, stick it in already."  
                        call Statup("Kitty", "Obed", 80, 4)
                        call Statup("Kitty", "Inbt", 80, 1) 
                        call Statup("Kitty", "Inbt", 60, 3)  
                        $ K_Forced = 1  
                        jump KDA_Prep
                    else:                              
                        call Statup("Kitty", "Love", 200, -20)    
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Kitty_Arms = 1   
    if "no dildo" in K_DailyActions:
            ch_k "Learn to take \"no\" for an answer, [K_Petname]."   
            $ K_RecentActions.append("angry")
            $ K_DailyActions.append("angry")   
    elif K_Forced:
            call KittyFace("angry", 1)
            ch_k "I'm not going to let you use that on me."
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
            ch_k "Not here!"     
            call Statup("Kitty", "Lust", 200, 5)  
            call Statup("Kitty", "Obed", 50, -3)  
    elif not K_Loose and "dildo anal" in K_DailyActions:
            call KittyFace("bemused")
            ch_k "Sorry, I just need a little break back there, [K_Petname]."    
    elif K_DildoA:
            call KittyFace("sad") 
            ch_k "Sorry, you can keep your toys out of there."     
    else:
            call KittyFace("normal", 1)
            ch_k "No way." 
    $ K_RecentActions.append("no dildo")                      
    $ K_DailyActions.append("no dildo")   
    $ Tempmod = 0    
    return
                
label KDA_Prep: #Animation set-up 
    if Trigger2 == "dildo anal":
        return
        
    if not K_Forced and Situation != "auto":
        $ Tempmod = 20 if K_Legs == "pants" else 0           
        call Kitty_Bottoms_Off
        if "angry" in K_RecentActions:
            return    
            
    $ Tempmod = 0      
    call K_Pussy_Launch("dildo anal")
    if not K_DildoA:        
        if K_Forced:
            call Statup("Kitty", "Love", 90, -75)
            call Statup("Kitty", "Obed", 70, 60)
            call Statup("Kitty", "Inbt", 80, 35) 
        else:
            call Statup("Kitty", "Love", 90, 10)
            call Statup("Kitty", "Obed", 70, 20)
            call Statup("Kitty", "Inbt", 80, 45)
    if Taboo:
        $ K_Inbt += int(Taboo/10)  
        $ K_Lust += int(Taboo/5)
    
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0    
    $ Cnt = 0
    if Taboo:
        call DrainWord("Kitty","tabno")
    call DrainWord("Kitty","no dildo")
    $ K_RecentActions.append("dildo anal")                      
    $ K_DailyActions.append("dildo anal") 
    
label KDA_Cycle: #Repeating strokes    
    while Round >=0:  
        call Shift_Focus("Kitty") 
        call K_Pussy_Launch("dildo anal")
        call KittyLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                               
                        "Slap her ass":                     
                                call K_Slap_Ass
                                jump KDA_Cycle  
                                
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
                                                        "I want to stick a finger in her pussy.":
                                                                $ Situation = "shift"
                                                                call KDA_After
                                                                call K_Fondle_Pussy    
                                                        "Just stick a finger in her pussy without asking.":
                                                                $ Situation = "auto"
                                                                call KDA_After
                                                                call K_Fondle_Pussy                                           
                                                        "I want to shift the dildo to her pussy.":
                                                                $ Situation = "shift"
                                                                call KDA_After
                                                                call K_Dildo_Pussy 
                                                        "Never Mind":
                                                                jump KDA_Cycle
                                            else: 
                                                ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"           
                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call KDA_After
                                                call Kitty_Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
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
                                                        jump KDA_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump KDA_Cycle                                        
                                    "Never mind":
                                            jump KDA_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call K_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump KDA_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call K_Pos_Reset
                                    $ Line = 0
                                    jump KDA_After
        #End menu (if Line)
        
        if K_Panties or K_Legs == "pants" or HoseNum("Kitty") >= 5: #This checks if Kitty wants to strip down.
                call K_Undress("auto")
            
        call Shift_Focus("Kitty")  
        call Sex_Dialog("Kitty",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or K_Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PK_Cumming
                            if "angry" in K_RecentActions:  
                                call K_Pos_Reset
                                return    
                            call Statup("Kitty", "Lust", 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump KDA_After 
                            $ Line = "came"
     
                    if K_Lust >= 100:  
                            #If Kitty can cum                                             
                            call K_Cumming
                            if Situation == "shift" or "angry" in K_RecentActions:
                                jump KDA_After
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in K_RecentActions:#And Kitty is unsatisfied,  
                                "Kitty still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump KDA_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Kitty")            
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if K_SEXP >= 100 or ApprovalCheck("Kitty", 1200, "LO"):
            pass
        elif Cnt == (5 + K_DildoA):
                    $ K_Brows = "confused"
                    ch_k "What are you even doing down there?" 
        elif K_Lust >= 80:
                    pass
        elif Cnt == (15 + K_DildoA) and K_SEXP >= 15 and not ApprovalCheck("Kitty", 1500):
                    $ K_Brows = "confused"        
                    menu:
                        ch_k "[K_Petname], this is getting uncomfortable, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump KDA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump KDA_After
                        "No, this is fun.":   
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                                    call Statup("Kitty", "Love", 200, -5)
                                    call Statup("Kitty", "Obed", 50, 3)                    
                                    call Statup("Kitty", "Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call KittyFace("angry", 1)   
                                    call K_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_k "Well if that's your attitude, I don't need your \"help\"."                         
                                    call Statup("Kitty", "Love", 50, -3, 1)
                                    call Statup("Kitty", "Love", 80, -4, 1)
                                    call Statup("Kitty", "Obed", 30, -1, 1)                    
                                    call Statup("Kitty", "Obed", 50, -1, 1)  
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump KDA_After
        #End Count check
           
        if Round == 10:
            ch_k "It's kind of time to get moving."   
        elif Round == 5:
            ch_k "For real[K_like]time's up."      
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0)
    $ Line = 0
    ch_k "Ok, we need to take a break."
    
label KDA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call K_Pos_Reset
        
    call KittyFace("sexy") 
    
    $ K_DildoA += 1  
    $ K_Action -=1            
    
    call Partner_Like("Kitty",1)
            
    if K_DildoA == 1:            
            $ K_SEXP += 10         
            if not Situation: 
                if K_Love >= 500 and "unsatisfied" not in K_RecentActions:
                    if K_Loose:
                        ch_k "That was. . . interesting. . ."
                    else:
                        ch_k "Ouch. . ."
                elif K_Obed <= 500 and P_Focus <= 20:
                    call KittyFace("perplexed", 1)
                    ch_k "Did you like that?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_k "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# end K_Dildo Ass /////////////////////////////////////////////////////////////////////////////

label K_Vibrator_Check:                                                                                 #fix this whole section is copy/paste unfinished
    if "vibrator" in P_Inventory:   
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in K_Inventory:
        "You ask Kitty to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1    
    
## K_Footjob //////////////////////////////////////////////////////////////////////
label K_Footjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Kitty")
    if K_Foot >= 7: # She loves it
        $ Tempmod += 10
    elif K_Foot >= 3: #You've done it before several times
        $ Tempmod += 7
    elif K_Foot: #You've done it before
        $ Tempmod += 3
        
    if K_Addict >= 75 and K_Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 10
    if K_Addict >= 75:
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 15
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
        
    if "no foot" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no foot" in K_RecentActions else 0    
        
    $ Approval = ApprovalCheck("Kitty", 1250, TabM = 3) # 110, 125, 140, Taboo -120(230)
    
    if Situation == "Kitty":                                                                  #Kitty auto-starts   
        if Approval > 2:                                                      # fix, add kitty auto stuff here
            "Kitty leans back  and starts rubbing your cock between her feet."
            menu:
                "What do you do?"
                "Nothing.":                    
                    call Statup("Kitty", "Inbt", 70, 3) 
                    call Statup("Kitty", "Inbt", 30, 2)                     
                    "Kitty continues her actions."
                "Praise her.":       
                    call KittyFace("sexy", 1)                    
                    call Statup("Kitty", "Inbt", 70, 3) 
                    ch_p "Oooh, that's good, [K_Pet]."
                    call Kitty_Namecheck
                    "Kitty continues her actions."
                    call Statup("Kitty", "Love", 80, 1)
                    call Statup("Kitty", "Obed", 90, 1)
                    call Statup("Kitty", "Obed", 50, 2)
                "Ask her to stop.":
                    call KittyFace("surprised")       
                    call Statup("Kitty", "Inbt", 70, 1) 
                    ch_p "Let's not do that for now, [K_Pet]."
                    call Kitty_Namecheck
                    "Kitty puts it down."
                    call Statup("Kitty", "Obed", 90, 1)
                    call Statup("Kitty", "Obed", 50, 1)
                    call Statup("Kitty", "Obed", 30, 2)
                    return            
            if Trigger:
                $ Trigger3 = "foot"
                return
            jump KFJ_Prep
        else:                
            $ Tempmod = 0                               # fix, add kitty auto stuff here
            $ Trigger2 = 0
            return            
    
    if not K_Foot and "no foot" not in K_RecentActions:        
        call KittyFace("confused", 2)
        ch_k "Huh, so you'd like me to touch your cock with my feet?"
        $ K_Blush = 1
            
    if not K_Foot and Approval:                                                 #First time dialog        
        if K_Forced: 
            call KittyFace("sad",1)
            call Statup("Kitty", "Love", 70, -3, 1)
            call Statup("Kitty", "Love", 20, -2, 1)
        elif K_Love >= (K_Obed + K_Inbt):
            call KittyFace("sexy",1)
            $ K_Brows = "sad"
            $ K_Mouth = "smile" 
            ch_k "I guess it couldn't hurt. . ."            
        elif K_Obed >= K_Inbt:
            call KittyFace("normal",1)
            ch_k "If you want, [K_Petname]. . ."            
        elif K_Addict >= 50:
            call KittyFace("manic", 1)
            ch_k "Okay. . ."  
        else: # Uninhibited 
            call KittyFace("lipbite",1)    
            ch_k "Sure. . ."    
            
    elif Approval:                                                                       #Second time+ dialog
        if K_Forced: 
            call KittyFace("sad")
            call Statup("Kitty", "Love", 70, -3, 1)
            call Statup("Kitty", "Love", 20, -2, 1)
            ch_k "That's all?" 
        elif not Taboo and "tabno" in K_DailyActions:        
            ch_k "Um, I guess this is secluded enough. . ."    
        elif "foot" in K_RecentActions:
            call KittyFace("sexy", 1)
            ch_k "I'm getting foot cramps. . ."
            jump KFJ_Prep
        elif "foot" in K_DailyActions:
            call KittyFace("sexy", 1)
            $ Line = renpy.random.choice(["Another one?",   
                "You're going to give me calluses.", 
                "Didn't get enough earlier?",
                "My feet are kinda sore from earlier.",
                "My feet are kinda sore from earlier."]) 
            ch_k "[Line]"
        elif K_Foot < 3:        
            call KittyFace("sexy", 1)
            $ K_Brows = "confused"
            $ K_Mouth = "kiss"
            ch_k "Hmm, magic toes. . ."        
        else:       
            call KittyFace("sexy", 1)
            $ Kitty_Arms = 2
            $ Line = renpy.random.choice(["You want me to use my feet?",                 
                "So you'd like another foot sesh?",                 
                "A little. . . [she rubs her foot along your leg]?", 
                "A little TLC?"]) 
            ch_k "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if K_Forced:
            call KittyFace("sad")
            call Statup("Kitty", "Obed", 90, 1)
            call Statup("Kitty", "Inbt", 60, 1)
            ch_k "Ok, fine." 
        elif "no foot" in K_DailyActions:               
            ch_k "OK, geeze!"   
        else:
            call KittyFace("sexy", 1)
            call Statup("Kitty", "Love", 90, 1)
            call Statup("Kitty", "Inbt", 50, 3) 
            $ Line = renpy.random.choice(["Sure, I guess.",                 
                "Ooooookay.",                 
                "Cool, lemme see it.", 
                "I guess I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Heh, ok, ok."]) 
            ch_k "[Line]"
            $ Line = 0
        call Statup("Kitty", "Obed", 20, 1)
        call Statup("Kitty", "Obed", 60, 1)
        call Statup("Kitty", "Inbt", 70, 2) 
        jump KFJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call KittyFace("angry")
        if "no foot" in K_RecentActions:  
            ch_k "You don't[K_like]listen do you, [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions and "no foot" in K_DailyActions: 
            ch_k "I said not in public!"  
        elif "no foot" in K_DailyActions:       
            ch_k "I told you \"no,\" [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "I said not in public!"     
        elif not K_Foot:
            call KittyFace("bemused")
            ch_k "I don't know, [K_Petname]. . ."
        else:
            call KittyFace("bemused")
            ch_k "Not now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no foot" in K_DailyActions:
                call KittyFace("bemused")
                ch_k "Yeah."              
                return
            "Maybe later?" if "no foot" not in K_DailyActions:
                call KittyFace("sexy")  
                ch_k ". . ."
                ch_k "Maybe."
                call Statup("Kitty", "Love", 80, 2)
                call Statup("Kitty", "Inbt", 70, 2)   
                if Taboo:                    
                    $ K_RecentActions.append("tabno")                      
                    $ K_DailyActions.append("tabno") 
                $ K_RecentActions.append("no foot")                      
                $ K_DailyActions.append("no foot")            
                return
            "I'd really appreciate it. . .":             
                if Approval:
                    call KittyFace("sexy")     
                    call Statup("Kitty", "Obed", 90, 2)
                    call Statup("Kitty", "Obed", 50, 2)
                    call Statup("Kitty", "Inbt", 70, 3) 
                    call Statup("Kitty", "Inbt", 40, 2) 
                    $ Line = renpy.random.choice(["Sure, I guess.",                 
                            "Ooooookay.",                 
                            "Cool, lemme see it.", 
                            "I guess I could. . .",
                            "Ok. . . [She gestures for you to come over].",
                            "Heh, ok, ok."]) 
                    ch_k "[Line]"
                    $ Line = 0                   
                    jump KFJ_Prep
                else:   
                    pass
                    
            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Kitty", 400, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and K_Forced):
                    call KittyFace("sad")
                    call Statup("Kitty", "Love", 70, -5, 1)
                    call Statup("Kitty", "Love", 200, -2)                 
                    ch_k "Ok, fine."  
                    call Statup("Kitty", "Obed", 50, 4)
                    call Statup("Kitty", "Inbt", 80, 1) 
                    call Statup("Kitty", "Inbt", 60, 3)  
                    $ K_Forced = 1  
                    jump KFJ_Prep
                else:                              
                    call Statup("Kitty", "Love", 200, -15)     
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Kitty_Arms = 1 
    if "no foot" in K_DailyActions:
        call KittyFace("angry", 1)
        ch_k "I'm not telling you again."   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1)
        ch_k "I don't even want to step on it."
        call Statup("Kitty", "Lust", 200, 5)    
        if K_Love > 300:
                call Statup("Kitty", "Love", 70, -2)
        call Statup("Kitty", "Obed", 50, -2)    
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call KittyFace("angry", 1)          
        $ K_DailyActions.append("tabno") 
        ch_k "Not here, not anywhere near here."
        call Statup("Kitty", "Lust", 200, 5)  
        call Statup("Kitty", "Obed", 50, -3)   
    elif K_Foot:
        call KittyFace("sad") 
        ch_k "I'm not feeling it today. . ."       
    else:
        call KittyFace("normal", 1)
        ch_k "I don't know about using my feet for. . . that."  
    $ K_RecentActions.append("no foot")                      
    $ K_DailyActions.append("no foot") 
    $ Tempmod = 0    
    return
    

label KFJ_Prep:
    if Trigger2 == "foot": 
        return
    
    if Taboo:
        $ K_Inbt += int(Taboo/10)  
        $ K_Lust += int(Taboo/5)
                
    call KittyFace("sexy")
    if K_Forced:
        call KittyFace("sad")
    elif K_Foot:
        $ K_Brows = "confused"
        $ K_Eyes = "sexy"
        $ K_Mouth = "smile"
    
    call Seen_First_Peen("Kitty",Partner,React=Situation)
    
    if not K_Foot:        
        if K_Forced:
            call Statup("Kitty", "Love", 90, -20)
            call Statup("Kitty", "Obed", 70, 25)
            call Statup("Kitty", "Inbt", 80, 30) 
        else:
            call Statup("Kitty", "Love", 90, 5)
            call Statup("Kitty", "Obed", 70, 20)
            call Statup("Kitty", "Inbt", 80, 20)     
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Kitty","tabno")
    call DrainWord("Kitty","no foot")
    $ K_RecentActions.append("foot")                      
    $ K_DailyActions.append("foot") 
  
label KFJ_Cycle:    
    while Round >=0:  
        call Shift_Focus("Kitty") 
        call Kitty_Sex_Launch("foot")    
        call KittyLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                          
                        "Start moving? . ." if not Speed:
                                    $ Speed = 1
                            
                        "Speed up. . ." if Speed < 2:                    
                                    $ Speed = 2
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 2:
                                    pass
                            
                        "Slow Down. . ." if Speed:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
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
                                                ch_k "I kinda need a break, so if we could wrap this up?"  
                                                
                                    "Shift primary action":
                                            if K_Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    if K_Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call KFJ_After                
                                                                        call K_Blowjob
                                                                    else:
                                                                        ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."
                                                        "How about a handjob?":
                                                                    if K_Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call KFJ_After                
                                                                        call K_Handjob
                                                                    else:
                                                                        ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."
                                                                        
#                                                        "How about a titjob?":
#                                                                    if K_Action and MultiAction:
#                                                                        $ Situation = "shift"
#                                                                        call KFJ_After
#                                                                        call K_Titjob
#                                                                    else:
#                                                                        ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."
                                                                
                                                        
                                                        
                                                        "Never Mind":
                                                                jump KFJ_Cycle
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
                                                        jump KFJ_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump KFJ_Cycle 
                                            "Never mind":
                                                        jump KFJ_Cycle 
                                    "Undress Kitty":
                                            call K_Undress   
                                    "Clean up Kitty (locked)" if not K_Spunk:
                                            pass  
                                    "Clean up Kitty" if K_Spunk:
                                            call Kitty_Cleanup("ask")                                         
                                    "Never mind":
                                            jump KFJ_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Kitty_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump KFJ_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Kitty_Sex_Reset
                                    $ Line = 0
                                    jump KFJ_After
        #End menu (if Line)
        
        call Shift_Focus("Kitty")  
        call Sex_Dialog("Kitty",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or K_Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PK_Cumming
                            if "angry" in K_RecentActions:  
                                call Kitty_Sex_Reset
                                return    
                            call Statup("Kitty", "Lust", 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump KFJ_After 
                            $ Line = "came"
     
                    if K_Lust >= 100:  
                            #If Kitty can cum                                             
                            call K_Cumming
                            if Situation == "shift" or "angry" in K_RecentActions:
                                jump KFJ_After
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in K_RecentActions:#And Kitty is unsatisfied,  
                                "Kitty still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump KFJ_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Kitty")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if Cnt == 20:
                    $ K_Brows = "angry"        
                    menu:
                        ch_k "Ouch, foot cramp, can we[K_like]take a break?"
                        "How about a BJ?" if K_Action and MultiAction:
                                $ Situation = "shift"
                                call KFJ_After
                                call K_Blowjob   
                        "How about a Handy?" if K_Action and MultiAction:
                                $ Situation = "shift"
                                call KFJ_After
                                call K_Handjob  
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump KFJ_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Kitty_Sex_Reset
                                $ Situation = "shift"
                                jump KFJ_After
                        "No, get back down there.":
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):
                                    call Statup("Kitty", "Love", 200, -5)
                                    call Statup("Kitty", "Obed", 50, 3)                    
                                    call Statup("Kitty", "Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    call KittyFace("angry", 1)   
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_k "Hey, I've got better things to do if you're[K_like]going to be a dick about it."                                               
                                    call Statup("Kitty", "Love", 50, -3, 1)
                                    call Statup("Kitty", "Love", 80, -4, 1)
                                    call Statup("Kitty", "Obed", 30, -1, 1)                    
                                    call Statup("Kitty", "Obed", 50, -1, 1)                     
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump KFJ_After
        elif Cnt == 10 and K_SEXP <= 100 and not ApprovalCheck("Kitty", 1200, "LO"):
                    $ K_Brows = "confused"
                    ch_k "Can we[K_Like]be done with this now? I'm getting sore."         
        #End Count check
                   
        call Escalation("Kitty","K") #sees if she wants to escalate things
        
        if Round == 10:
            ch_k "It's kind of time to get moving."   
        elif Round == 5:
            ch_k "For real[K_like]time's up."      
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0)
    $ Line = 0
    ch_k "Ok, we need to take a break."
    
label KFJ_After:
    call KittyFace("sexy") 
    
    $ K_Foot += 1  
    $ K_Action -=1
    $ K_Addictionrate += 1
    if "addictive" in P_Traits:
        $ K_Addictionrate += 1        
    call Statup("Kitty", "Lust", 90, 5)
    
    call Partner_Like("Kitty",1)
    
    if "Kittypedi" in Achievements:
            pass  
    elif K_Foot >= 10:
            call KittyFace("smile", 1)
            ch_k "I guess I've gotten pretty smooth at the \"Kittypedi.\""
            $ Achievements.append("Kittypedi")
            $ K_SEXP += 5          
    elif K_Foot == 1:            
            $ K_SEXP += 10
            if K_Love >= 500:
                $ K_Mouth = "smile"
                ch_k "I could feel you down there. . ."
            elif P_Focus <= 20:
                $ K_Mouth = "sad"
                ch_k "Did that work out for you?"
    elif K_Foot == 5:
                ch_k "Let me know any time you need me to \"foot you up.\""                  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_k "Ok, so what were you thinking?"
    else:
        call Kitty_Sex_Reset    
    call Checkout
    return

## end K_Footjob //////////////////////////////////////////////////////////////////////




# Start K_Lesbian ////////////////////////////////////////////////////////////////////////
label K_Les_Interupted:  
        # Called if you catch them fucking 
        if "unseen" not in K_RecentActions:
                if K_Org < 3 and K_Action:                
                    menu:
                        "Did you want to stop them?"
                        "Yeah.":
                            pass
                        "No, let them keep going.":
                            $ K_Action -= 1 if K_Action > 0 else 0
                            jump K_Les_Cycle 
                else:
                    ch_k "Ok, that's probably enough of that. . ."
                jump K_Les_After
        call DrainWord("Kitty","unseen",1,0) #She sees you, so remove unseens
        call DrainWord(Partner,"unseen",1,0) #She sees you, so remove unseens
        call KittyFace("surprised", 2) 
        call AnyFace(Partner,"surprised",2) 
        "Suddenly, Kitty jerks up from what she was doing with a start, and gives [Partner] a nudge."
        ch_k "Eep! [Playername], how long have you been there?!"
        call KittyFace("perplexed", 1) 
        call AnyFace(Partner,"perplexed",1) 
        $ K_Action -= 1 if K_Action > 0 else 0
        call Checkout(1)
        $ Line = 0
    
        #If you've been jacking it
        if Trigger2 == "jackin":
                $ K_Eyes = "down"
                menu:
                    ch_k "and why are you fapping?!"
                    "Long enough, it was an excellent show.":   
                            call KittyFace("sexy")
                            call Statup("Kitty", "Obed", 50, 3)
                            call Statup("Kitty", "Obed", 70, 2)
                            "Kitty glances over at [Partner]."
                            ch_k "I mean, I guess. . ."
                            if K_Love >= 800 or K_Obed >= 500 or K_Inbt >= 500:
                                $ Tempmod += 10
                                call Statup("Kitty", "Lust", 90, 5)
                                ch_k "And[K_like]you're not so bad yourself. . ."  
                            
                    "I. . . just got here?":
                            call KittyFace("angry")                   
                            call Statup("Kitty", "Love", 70, 2)
                            call Statup("Kitty", "Love", 90, 1)
                            call Statup("Kitty", "Obed", 50, 2)
                            call Statup("Kitty", "Obed", 70, 2)
                            "She looks pointedly at your cock,"
                            ch_k "Riiight. . ."   
                            if K_Love >= 800 or K_Obed >= 500 or K_Inbt >= 500:
                                    $ Tempmod += 10
                                    call Statup("Kitty", "Lust", 90, 5)
                                    call KittyFace("bemused", 1)
                                    ch_k "-I can't exactly blame you though. . ."   
                            else:
                                    $ Tempmod -= 10
                                    call Statup("Kitty", "Lust", 200, -5)
                call Seen_First_Peen("Kitty",Partner) 
        else:         
                #you haven't been jacking it         
                menu:                    
                    ch_k "Eep! [Playername], how long have you been there?!"  
                    "Long enough.":   
                            call KittyFace("sexy", 1)
                            call Statup("Kitty", "Obed", 50, 3)
                            call Statup("Kitty", "Obed", 70, 2)
                            ch_k "I guess we[K_like]really put on a show, huh. . ."
                    "I just got here.":
                            call KittyFace("bemused", 1)
                            call Statup("Kitty", "Love", 70, 2)
                            call Statup("Kitty", "Love", 90, 1)                    
                            ch_k "Uh HUH. . ."   
                            call Statup("Kitty", "Obed", 50, 2)
                            call Statup("Kitty", "Obed", 70, 2)    
                                
        if not ApprovalCheck("Kitty", 1350):
                #If she doesn't like you enough to have you around. . .
                call Statup("Kitty", "Love", 200, -5)
                call KittyFace("angry")
                $ K_RecentActions.append("angry")
                $ K_DailyActions.append("angry")
                ch_k "So maybe you could[K_like]leave us to it?"
                $ renpy.pop_call()
                $ renpy.pop_call()
                if bg_current == "bg player":                                        
                    jump Campus_Map  
                else:
                    jump Player_Room  
        
        if Round <= 10:
            ch_k "We were just about to take a break though."
            return
        $ Situation = "interrupted"
    
label K_LesScene(Bonus = 0): #Repeating strokes
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Kitty")
    if K_LesWatch:
        $ Tempmod += 10
    elif K_Les:
        $ Tempmod += 5
    if K_SEXP >= 50:
        $ Tempmod += 25
    elif K_SEXP >= 30:
        $ Tempmod += 15
    elif K_SEXP >= 15:
        $ Tempmod += 5
        
    if K_Lust >= 90:
        $ Tempmod += 5
    elif K_Lust >= 75:
        $ Tempmod += 5
        
    elif K_Inbt >= 750:
        $ Tempmod += 5
        
    if "exhibitionist" in K_Traits:      
        $ Tempmod += (3*Taboo) 
        
    if "dating" in K_Traits or "sex friend" in K_Petnames:
        $ Tempmod += 10        
    elif "ex" in K_Traits:
        $ Tempmod -= 40  
        
    if R_Loc == bg_current:
            #if it's Rogue. . .
            $ Partner = "Rogue"  
            if K_LikeRogue >= 900:
                    $ Bonus += 150
            elif K_LikeRogue >= 800 or "poly Rogue" in K_Traits:
                    $ Bonus += 100
            elif K_LikeRogue >= 700:
                    $ Bonus += 50
            elif K_LikeRogue <= 200:
                    $ Bonus -= 200
            elif K_LikeRogue <= 500:
                    $ Bonus -= 100
            call DrainWord("Rogue","unseen",1,0) #She sees you, so remove unseens
    elif E_Loc == bg_current:
            #if it's Emma. . .
            $ Partner = "Emma"  
            if K_LikeEmma >= 900:
                    $ Bonus += 150
            elif K_LikeEmma >= 800 or "poly Emma" in K_Traits:
                    $ Bonus += 100
            elif K_LikeEmma >= 700:
                    $ Bonus += 50
            elif K_LikeEmma <= 200:
                    $ Bonus -= 200
            elif K_LikeEmma <= 500:
                    $ Bonus -= 100
            call DrainWord("Emma","unseen",1,0) #She sees you, so remove unseens
    elif L_Loc == bg_current:
            #if it's Laura. . .
            $ Partner = "Laura"  
            if K_LikeLaura >= 900:
                    $ Bonus += 150
            elif K_LikeLaura >= 800 or "poly Laura" in K_Traits:
                    $ Bonus += 100
            elif K_LikeLaura >= 700:
                    $ Bonus += 50
            elif K_LikeLaura <= 200:
                    $ Bonus -= 200
            elif K_LikeLaura <= 500:
                    $ Bonus -= 100
            call DrainWord("Laura","unseen",1,0) #She sees you, so remove unseens
            
     
    if R_Loc == bg_current:
            #if it's Rogue. . .
            $ Partner = "Rogue"  
    elif E_Loc == bg_current:
            #if it's Emma. . .
            $ Partner = "Emma"  
    elif L_Loc == bg_current:
            #if it's Laura. . .
            $ Partner = "Laura"  
           
    $ Line = GirlLikeCheck("Kitty",Partner)      
    if Line >= 900:
            $ Bonus += 150
    elif Line >= 800 or "poly "+Partner in K_Traits:
            $ Bonus += 100
    elif Line >= 700:
            $ Bonus += 50
    elif Line <= 200:
            $ Bonus -= 200
    elif Line <= 500:
            $ Bonus -= 100
    call DrainWord(Partner,"unseen",1,0) #She sees you, so remove unseens    
    $ Line = 0
            
    call AnyWord("Kitty",1,"noticed "+Partner,"noticed "+Partner) #ie $ L_RecentActions.append("noticed Rogue") 
    call AnyWord(Partner,1,"noticed Kitty","noticed Kitty") #ie $ R_RecentActions.append("noticed Laura") 
            
    if bg_current in ("bg player", "bg kitty", "bg rogue", "bg emma"):
        $ Taboo == 0
    if K_ForcedCount and not K_Forced:
        $ Tempmod -= 5 * K_ForcedCount   
        
    $ Approval = ApprovalCheck("Kitty", 1350, TabM = 2, Bonus = Bonus) # 1350, 1500, 1650, Taboo -800
    
    call DrainWord("Kitty","unseen",1,0) #She sees you, so remove unseens
    
    if Situation == "interrupted":    
        menu:
            extend ""
            "I guess I should probably get going then. . .":
                    call Statup("Kitty", "Love", 80, 3)
                    if Approval >= 2:
                            # if Kitty is very much in
                            ch_k "Hmmmm, I don't know about that. . ."
                            if R_Loc == bg_current:
                                    call R_Les_Response("Kitty",3,B2=Bonus)                          
                            elif E_Loc == bg_current:
                                    call E_Les_Response("Kitty",3,B2=Bonus)                        
                            elif L_Loc == bg_current:
                                    call L_Les_Response("Kitty",3,B2=Bonus)
                            if not _return:
                                    return
                    else:
                            # If Kitty is only so/so, but Rogue is on board, she tries to convince Kitty
                            if R_Loc == bg_current:
                                    call R_Les_Response("Kitty",1,B2=Bonus)                         
                            elif E_Loc == bg_current:
                                    call E_Les_Response("Kitty",1,B2=Bonus)                          
                            elif L_Loc == bg_current:
                                    call L_Les_Response("Kitty",1,B2=Bonus)                  
                            if not _return:
                                    #this is the default reaction if Rogue is not into it either
                                    if Approval:
                                        ch_k "You could at least stick around. . ."
                                        return
                                    else:
                                        ch_k "I guess so. . ."  
                                        $ renpy.pop_call()
                                        $ renpy.pop_call()
                                        if bg_current == "bg player":                                        
                                            jump Campus_Map  
                                        else:
                                            jump Player_Room  
                            elif not Approval:
                                    ch_k "Sorry [K_Petname], I guess we'd like to keep this private."
                                    return                            
                            elif not K_Action:
                                    ch_k "Sorry [K_Petname], I'm kinda worn out already. . ."
                                    return        
                            else:
                                    ch_k "Sure."    
                    #if it passed the hurdles. . .
                    jump K_Les_Prep
            "So maybe I could join you girls?" if P_Semen and K_Action:
                    call KittyFace("sexy")
                    ch_k "Mmmm, what would you like?"    
                    $ Situation = "join"
                    return                      #returns to sexmenu=
            "So maybe I could watch a bit longer?":
                    call KittyFace("bemused", 1)   
    #End "Interrupted" content.
    
    #first time
    if not K_LesWatch:                                                                
            call KittyFace("surprised", 1)
            $ K_Mouth = "kiss"
            ch_k "You wanna watch me and [Partner] hook up?"
            if K_Forced:
                call KittyFace("sad")
                ch_k "but {i}just{/i} watch, right?"
                
    if Approval and Partner == "Rogue" and "touch" not in R_Traits:
            ch_k "I don't know, isn't Rogue's touch. . . dangerous?"
            ch_p "Don't worry, I can keep it turned off."
            ch_k "Oh, well I guess. . ."
                     
    if not K_LesWatch and Approval:   
            #First time dialog                                                       
            if K_Forced: 
                call KittyFace("sad")
                call Statup("Kitty", "Love", 70, -3, 1)
                call Statup("Kitty", "Love", 20, -2, 1)
            elif Bonus >= 100:
                call KittyFace("sly", Eyes="side")
                ch_k "Heh, you don't know what you're asking for. . ."   
            elif K_Love >= (K_Obed + K_Inbt):
                call KittyFace("sexy")
                $ K_Brows = "sad"
                $ K_Mouth = "smile" 
                ch_k "I hadn't really considered putting on a show like this. . ."          
            elif K_Obed >= K_Inbt:
                call KittyFace("normal")
                ch_k "If that's what you want, [K_Petname]. . ."            
            else: # Uninhibited 
                call KittyFace("sad")
                $ K_Mouth = "smile"             
                ch_k "I guess it could be fun with you watching. . ."    
    
    
    elif Approval:            
                #Second time+ initial dialog                                                           
                if K_Forced: 
                        call KittyFace("sad")
                        call Statup("Kitty", "Love", 70, -3, 1)
                        call Statup("Kitty", "Love", 20, -2, 1)
                        ch_k "You really like this girl-on-girl stuff, huh?"  
                elif Approval and "lesbian" in K_RecentActions:
                        call KittyFace("sexy", 1)
                        ch_k "A little more wouldn't hurt. . ."    
                        jump K_Les_Prep
                elif Approval and "lesbian" in K_DailyActions:
                        call KittyFace("sexy", 1)
                        $ Line = renpy.random.choice(["You enjoyed the show?",       
                            "Didn't get enough earlier?",
                            "It is nice to have an audience. . ."]) 
                        ch_k "[Line]"            
                elif K_Mast < 3:        
                        call KittyFace("sexy", 1)
                        $ K_Brows = "confused"
                        ch_k "You really do like to watch."       
                else:       
                        call KittyFace("sexy", 1)
                        $ Kitty_Arms = 2
                        $ Line = renpy.random.choice(["You sure do like to watch.",                 
                            "So you'd like me to go again?",                 
                            "You want to watch some more?",
                            "You want me to get down with "+Partner+"?"]) 
                        ch_k "[Line]"
                        $ Line = 0                        
    #End second time+ initial dialog
    
    if Approval >= 2:      
                #If she's into it. . .                                                                            
                if K_Forced:
                    call KittyFace("sad")
                    call Statup("Kitty", "Obed", 90, 1)
                    call Statup("Kitty", "Inbt", 60, 1)
                    ch_k "Well, I guess if she's fine with it. . ." 
                else:
                    call KittyFace("sexy", 1)
                    call Statup("Kitty", "Love", 90, 1)
                    call Statup("Kitty", "Inbt", 50, 3) 
                    if Situation == "interrupted":
                            ch_k "Well I guess we could get back to it. . ."
                    else:
                            $ Line = renpy.random.choice(["Well. . . ok.",                 
                                "I don't mind getting cozy with her. . .",
                                "I kinda needed this anyways. . .",
                                "Sure!", 
                                "I guess. . .",
                                "Heh, ok, fine."]) 
                            ch_k "[Line]"
                            $ Line = 0
                call Statup("Kitty", "Obed", 20, 1)
                call Statup("Kitty", "Obed", 60, 1)
                call Statup("Kitty", "Inbt", 70, 2) 
                jump K_Les_Partner   
    #end instant approval
            
    else:       
        #If she's not into it, but maybe. . .                                                                                    
        menu:
            ch_k "I don't know about that, [K_Petname]."
            "Maybe later?":
                    call KittyFace("sexy", 1)  
                    if Bonus >= 100:
                        call Statup("Kitty", "Inbt", 90, 5)  
                        ch_k "I mean, eventually. . ."
                    elif Bonus >= 0:
                        call LikeUpdater("Kitty",3)
                        ch_k "Um, I don't know. . . maybe?"
                    else:
                        call KittyFace("angry", 1, Eyes="side") 
                        ch_k "Not likely."
                    call KittyFace("smile", 1) 
                    ch_k "Thanks for being cool though. . ."
                    call Statup("Kitty", "Love", 80, 2)
                    call Statup("Kitty", "Inbt", 70, 5)   
                    call Taboo_Level
                    return
                    
            "You look like you might be into it. . .":             
                    if Approval:
                            call KittyFace("sexy")     
                            call Statup("Kitty", "Obed", 90, 4)
                            call Statup("Kitty", "Obed", 50, 5)
                            call Statup("Kitty", "Inbt", 70, 4) 
                            call Statup("Kitty", "Inbt", 40, 4) 
                            $ Line = renpy.random.choice(["Well. . . ok.",                 
                                    "I don't mind getting cozy with her. . .",
                                    "I kinda needed this anyways. . .",
                                    "Sure!", 
                                    "I guess. . .",
                                    "Heh, ok, fine."]) 
                            ch_k "[Line]"
                            $ Line = 0                   
                            jump K_Les_Partner
                    else:   
                            pass
                    
            "Just get at it already.":                                              
                    # Pressured into it
                    $ Approval = ApprovalCheck("Kitty", 550, "OI", TabM = 2) # 55, 70, 85
                    if Approval > 1 or (Approval and K_Forced):
                            call KittyFace("sad")
                            call Statup("Kitty", "Love", 70, -5, 1)
                            call Statup("Kitty", "Love", 200, -5)                 
                            ch_k "Ok, whatever."  
                            call Statup("Kitty", "Obed", 80, 4)
                            call Statup("Kitty", "Inbt", 80, 1) 
                            call Statup("Kitty", "Inbt", 60, 3)  
                            $ K_Forced = 1  
                            jump K_Les_Partner
                    else:                              
                            call Statup("Kitty", "Love", 200, -20)     
                            $ K_RecentActions.append("angry")
                            $ K_DailyActions.append("angry")
    # end of asking her to do it
    
    if R_Loc == bg_current:
            call R_Les_Response("Kitty",1,B2=Bonus)
    elif E_Loc == bg_current:
            call E_Les_Response("Kitty",1,B2=Bonus)
    elif L_Loc == bg_current:
            call L_Les_Response("Kitty",1,B2=Bonus)
    if _return:
            #if the other girl convinces her
            call KittyFace("smile", 1)
            ch_k "Ok, if {i}you{/i} want to."
            ch_k "Commere. . ."
            jump K_Les_Prep
            
            
    #She refused all offers.
    $ Kitty_Arms = 1                
    if not Partner:
            ch_k "Seems like she wasn't into it. . ."
    elif K_Forced:
            call KittyFace("angry", 1)
            ch_k "I'm just not into that."
            call Statup("Kitty", "Lust", 90, 5)         
            if K_Love > 300:
                call Statup("Kitty", "Love", 70, -2)
            call Statup("Kitty", "Obed", 50, -2)    
            $ K_RecentActions.append("angry")
            $ K_DailyActions.append("angry")  
    elif Taboo:                            
            # she refuses and this is too public a place for her
            call KittyFace("angry", 1)          
            $ K_DailyActions.append("tabno") 
            ch_k "Totally not around here."     
            call Statup("Kitty", "Lust", 90, 5)  
            call Statup("Kitty", "Obed", 50, -3) 
    elif K_Les:
            call KittyFace("sad") 
            if Bonus >= 100:
                ch_k "I'm not really comfortable with that."     
            else:    
                ch_k "I don't think I'm ready for an audience."     
    else:
            call KittyFace("normal", 1)
            ch_k "No way."  
    $ K_RecentActions.append("no lesbian")                      
    $ K_DailyActions.append("no lesbian") 
    $ Tempmod = 0 
    call Taboo_Level
    return
    
label K_Les_Partner:
    # This checks to see if the other girl is into it. 
    if R_Loc == bg_current:
            call R_Les_Response("Kitty",2)
            if not _return:
                    # If Rogue refused
                    return
    elif E_Loc == bg_current:
            call E_Les_Response("Kitty",2)
            if not _return:
                    # If Emma refused
                    return
    elif L_Loc == bg_current:
            call L_Les_Response("Kitty",2)
            if not _return:
                    # If Laura refused
                    return
            
label K_Les_Prep:    
    #sets the scene up   
    
    if R_Loc == bg_current:          
            $ Partner = "Rogue"  
    elif E_Loc == bg_current:        
            $ Partner = "Emma"  
    elif L_Loc == bg_current:      
            $ Partner = "Laura" 
            
    call AnyWord("Kitty",1,"noticed "+Partner,"noticed "+Partner) #ie $ L_RecentActions.append("noticed Rogue") 
    call AnyWord(Partner,1,"noticed Kitty","noticed Kitty") #ie $ R_RecentActions.append("noticed Laura") 
            
    if "unseen" not in K_RecentActions:
            #if she knows you're there. . .
            call KittyFace("sexy")
            $ Kitty_Arms = 2
            "Kitty move's closer to [Partner] and wraps her arms around her neck."
            if not K_LesWatch:
                    #First time        
                    if K_Forced:
                        call Statup("Kitty", "Love", 90, -20)
                        call Statup("Kitty", "Obed", 70, 55)
                        call Statup("Kitty", "Inbt", 80, 55) 
                    else:
                        call Statup("Kitty", "Love", 90, 5)
                        call Statup("Kitty", "Obed", 70, 20)
                        call Statup("Kitty", "Inbt", 80, 60)  
            call K_Les_FirstKiss
            $ Trigger3 == "kiss girl"
            $ Trigger4 == "kiss girl"
        
    $ Trigger = "lesbian"   
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0 
    $ Line = 0
    if Taboo:
        call DrainWord("Kitty","tabno")
    call DrainWord("Kitty","no lesbian")
    call AnyWord("Kitty",0,"lesbian","lesbian") #ie $ L_RecentActions.append("noticed Rogue") 
    call AnyWord(Partner,0,"lesbian","lesbian") #ie $ R_RecentActions.append("noticed Laura") 
    
label K_Les_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Kitty")
        call Les_Launch("Kitty")  
        call KittyLust     

        if  P_Focus < 100:                                                    
                    #Player Command menu
                    menu:
                        "Keep watching. . .":
                                    pass
                                   
                        "\"Ahem. . .\"" if "unseen" in K_RecentActions:  
                                jump K_Les_Interupted   
                                
                        "Start jack'in it." if Trigger2 != "jackin":
                                call K_Jackin                   
                        "Stop jack'in it." if Trigger2 == "jackin":
                                $ Trigger2 = 0
                                        
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
                                                ch_k "I'm kinda worn out, so[K_like]maybe we could wrap this up?"  
                                            
                                    "Threesome actions":   
                                        menu:
                                            "Ask Kitty to do something else with [Partner]":
                                                    if "unseen" in K_RecentActions:
                                                            ch_p "Oh yeah, why don't you. . ."
                                                            jump K_Les_Interupted
                                                    else:                        
                                                            call Kitty_Les_Change
                                            "Ask [Partner] to do something else":
                                                    if "unseen" in K_RecentActions:
                                                            ch_p "Oh yeah, why don't you. . ."
                                                            jump K_Les_Interupted
                                                    else:                        
                                                        call Partner_Threechange("Kitty")  
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                    if "unseen" in K_RecentActions:
                                                            ch_p "Oh, that's good. . ."
                                                            jump K_Les_Interupted
                                                    else:                        
                                                            $ ThreeCount = 0  
                                                            
#                                            "Swap to [Partner]":
#                                                        call Trigger_Swap("Kitty")
                                            "Undress [Partner]":
                                                    if "unseen" in K_RecentActions:
                                                            ch_p "Oh, yeah, take it off. . ."
                                                            jump K_Les_Interupted
                                                    else:                        
                                                            call Partner_Undress
                                                            jump K_Les_Cycle 
                                            "Clean up Partner":
                                                    if "unseen" in K_RecentActions:
                                                            ch_p "You've got a little something. . ."
                                                            jump K_Les_Interupted
                                                    else:                        
                                                            call Partner_Cleanup
                                                            jump K_Les_Cycle 
                                            "Never mind":
                                                        jump K_Les_Cycle 
                                    "Undress Kitty":
                                            if "unseen" in K_RecentActions:
                                                    ch_p "Oh yeah, why don't you. . ."
                                                    jump K_Les_Interupted
                                            else:                        
                                                    call K_Undress   
                                    "Clean up Kitty (locked)" if not K_Spunk:
                                            pass  
                                    "Clean up Kitty" if K_Spunk:
                                            if "unseen" in K_RecentActions:
                                                ch_p "You've got a little something. . ."
                                                jump K_Les_Interupted
                                            else:                        
                                                call Kitty_Cleanup("ask")                                         
                                    "Never mind":
                                            jump K_Les_Cycle  
                                            
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call K_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump K_Les_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call K_Pos_Reset
                                    $ Line = 0
                                    jump K_Les_After   
        #End menu (if Line)
        
        call Shift_Focus("Kitty")  
        call Sex_Dialog("Kitty",Partner)
        
        $ Cnt += 1
        $ Round -= 1
             
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or K_Lust >= 100:    
                    #If either of you can cum:
                    if P_Focus >= 100:
                            #If you can cum:  
                            if "unseen" not in K_RecentActions: #if she knows you're there
                                call PK_Cumming
                                if "angry" in K_RecentActions:  
                                    call K_Pos_Reset
                                    return    
                                call Statup("Kitty", "Lust", 200, 5) 
                                if 100 > K_Lust >= 70 and K_OCount < 2:             
                                    $ K_RecentActions.append("unsatisfied")                      
                                    $ K_DailyActions.append("unsatisfied") 
                                $ Line = "came"
                            else: #If she wasn't aware you were there
                                "You grunt and try to hold it in."
                                $ P_Focus = 95
                                jump K_Les_Interupted
     
                    if K_Lust >= 100: 
                            #If Kitty can cum                                              
                            call K_Cumming
                            jump K_Les_Interupted
                       
                    if Line == "came": 
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."      
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Kitty")            
                            
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if "unseen" in K_RecentActions:
                if Round == 10:
                    "It's getting a bit late, Kitty and [Partner] will probably be wrapping up soon."  
                elif Round == 5:
                    "They're definitely going to stop soon."
        else:
                if Round == 10:
                    ch_k "We might want to wrap this up, it's getting late." 
                elif Round == 5:
                    ch_k "Seriously, it'll be time to stop soon."   
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0)
    $ Line = 0
    if "unseen" not in K_RecentActions:
        ch_k "Ok, [K_Petname], that's enough of that for now."
    

label K_Les_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call K_Pos_Reset
        
    call KittyFace("sexy") 
        
    if Partner == "Emma":
        call Partner_Like("Kitty",4)
    else:
        call Partner_Like("Kitty",3)
            
    $ K_LesWatch += 1 
    if K_LesWatch == 1:            
            $ K_SEXP += 15    
            if K_Love >= 500 and K_Org:
                    ch_k "Hmm, that's kinda fun with an audience. . ." 
    
    if not Situation:
            call Post_Les_Dialog("Kitty")
                    
    call AnyWord("Kitty",1,0,0,0,"les "+Partner) #ie $ L_RecentActions.append("noticed Rogue") 
    call AnyWord(Partner,1,0,0,0,"les Kitty") #ie $ R_RecentActions.append("noticed Laura") 
                    
                        
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_k "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# End R LesScene


    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

label Kitty_Les_Change(D20S=0, Secondary=Partner, Primary = "Kitty", PrimaryLust=0, SecondaryLust=0):
        # for Lesbian primary activity: Kitty_Threeway_Set("preset", "lesbian", Trigger3, ActiveGirl)
        #this is called when the player wants to change over a lesbian T3 behavior.
        $ Line = 0
        menu:
            "Hey Kitty. . ."
            "why don't you kiss her?" if Trigger5 != "kiss girl" and Trigger5 != "kiss both":
                    call Kitty_Threeway_Set("kiss girl", "lesbian", Trigger3)
            "why don't you grab her tits?" if Trigger3 != "fondle breasts":
                    call Kitty_Threeway_Set("fondle breasts", "lesbian", Trigger3)
            "why don't you suck her breasts?" if Trigger3 != "suck breasts":
                    call Kitty_Threeway_Set("suck breasts", "lesbian", Trigger3)
            "why don't you finger her?" if Trigger3 != "fondle pussy":
                    call Kitty_Threeway_Set("fondle pussy", "lesbian", Trigger3)
            "why don't you go down on her?" if Trigger3 != "lick pussy":
                    call Kitty_Threeway_Set("lick pussy", "lesbian", Trigger3)
            "why don't you grab her ass?" if Trigger3 != "fondle ass":
                    call Kitty_Threeway_Set("fondle ass", "lesbian", Trigger3)
            "why don't you lick her ass?" if Trigger3 != "lick ass":
                    call Kitty_Threeway_Set("lick ass", "lesbian", Trigger3) 
            "never mind.":
                pass
        if not Line:
            $ Line = "You return to what you were doing." 
        else:
            $ Situation = "skip"
        "[Line]"
        return

label Kitty_Three_Change(ActiveGirl = "Rogue", D20S=0, Secondary="Kitty", PrimaryLust=0, SecondaryLust=0):
        #this is called when the player wants to change over a threeway behavior.
        # for Threeway secondary activity: Kitty_Threeway_Set("preset", 0, Trigger4, "ActiveGirl")        
        menu K_Three_Change:
            ch_p "Hey Kitty. . ."
            "about [ActiveGirl]. . .":
                menu:
                    ch_p "about [ActiveGirl]. . ."
                    "why don't you kiss her?" if Trigger5 != "kiss girl" and Trigger5 != "kiss both":
                            call Kitty_Threeway_Set("kiss girl", 0, Trigger4, ActiveGirl)                            
                    "why don't you grab her tits?" if Trigger4 != "fondle breasts":
                            call Kitty_Threeway_Set("fondle breasts",0, Trigger4, ActiveGirl)                    
                    "why don't you suck her breasts?" if Trigger4 != "suck breasts":
                            call Kitty_Threeway_Set("suck breasts",0, Trigger4, ActiveGirl)                            
                    "why don't you finger her?" if Trigger4 != "fondle pussy":
                            call Kitty_Threeway_Set("fondle pussy",0, Trigger4, ActiveGirl)                            
                    "why don't you go down on her?" if Trigger4 != "lick pussy":
                            call Kitty_Threeway_Set("lick pussy", 0, Trigger4, ActiveGirl)                            
                    "why don't you grab her ass?" if Trigger4 != "fondle ass":
                            call Kitty_Threeway_Set("fondle ass", 0, Trigger4, ActiveGirl)                            
                    "why don't you lick her ass?" if Trigger4 != "lick ass":
                            call Kitty_Threeway_Set("lick ass", 0, Trigger4, ActiveGirl)
                    "wait, I meant. . .":
                            jump K_Three_Change
                    
            "about me. . .":
                menu:
                    ch_p "about me. . ."
                    "why don't you kiss me?" if Trigger5 != "kiss you" and Trigger5 != "kiss both":
                            call Kitty_Threeway_Set("kiss you", 0, Trigger4, ActiveGirl)                            
                    "maybe take me in hand?" if Trigger4 != "hand":
                            call Kitty_Threeway_Set("hand", 0, Trigger4, ActiveGirl)                            
                    "maybe give me a lick?" if Trigger4 != "blow":
                            call Kitty_Threeway_Set("blow", 0, Trigger4, ActiveGirl)
                    "wait, I meant. . .":
                            jump K_Three_Change
            "never mind.":
                pass
        return

#Start K_Les_Response >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >
label K_Les_Response(Girl="Rogue", Step=1, B=0, B2=0, Tempmod=0, Result=0, Approval = 0):
        #Dialog for responses to Lesbian scenes, Girl is the initial girl in the scene. Step is the phase of the conversation
        # call K_Les_Response("Rogue",1)
        if K_Les:
            $ Tempmod += 10
        if K_SEXP >= 50:
            $ Tempmod += 25
        elif K_SEXP >= 30:
            $ Tempmod += 15
        elif K_SEXP >= 15:
            $ Tempmod += 5
                    
        elif K_Inbt >= 750:
            $ Tempmod += 5
            
        if "exhibitionist" in K_Traits:      
            $ Tempmod += (3*Taboo) 
            
        if "dating" in K_Traits or "sex friend" in K_Petnames:
            $ Tempmod += 10        
        elif "ex" in K_Traits:
            $ Tempmod -= 40  
            
        if Girl == "Rogue":
                #if it's Rogue. . .
                if K_LikeRogue >= 900:
                        $ B += 150
                elif K_LikeRogue >= 800 or "poly Rogue" in K_Traits:
                        $ B += 100
                elif K_LikeRogue >= 700:
                        $ B += 50
                elif K_LikeRogue <= 200:
                        $ B -= 200
                elif K_LikeRogue <= 500:
                        $ B -= 100
        elif Girl == "Emma":
                #if it's Emma. . .
                if K_LikeEmma >= 900:
                        $ B += 150
                elif K_LikeEmma >= 800 or "poly Emma" in K_Traits:
                        $ B += 100
                elif K_LikeEmma >= 700:
                        $ B += 50
                elif K_LikeEmma <= 200:
                        $ B -= 200
                elif K_LikeEmma <= 500:
                        $ B -= 100
        elif Girl == "Laura":
                #if it's Laura. . .
                if K_LikeLaura >= 900:
                        $ B += 150
                elif K_LikeLaura >= 800 or "poly Laura" in K_Traits:
                        $ B += 100
                elif K_LikeLaura >= 700:
                        $ B += 50
                elif K_LikeLaura <= 200:
                        $ B -= 200
                elif K_LikeLaura <= 500:
                        $ B -= 100
                        
        $ Approval = ApprovalCheck("Kitty", 1300, TabM = 2, Bonus = B) # 1300, 1450, 1600, Taboo -800
        
        if Step == 1:
            #this is if the first girl's check failed, but Kitty likes her.
            if Approval >= 2 or (Approval and B >= 150):
                call KittyFace("sexy", 1)
                ch_k "Come on [Girl], it could be kinda fun."
                if B2 >= 100:
                    $ Result = 1
                    if Girl == "Rogue":
                            $ K_LikeRogue += (int(B/10))
                            $ R_LikeKitty += (int(B2/10))
                    elif Girl == "Emma":
                            $ K_LikeEmma += (int(B/10))
                            $ E_LikeKitty += (int(B2/10))
                    elif Girl == "Laura":
                            $ K_LikeLaura += (int(B/10))
                            $ L_LikeKitty += (int(B2/10))
            else:
                return Result
        
        if Step == 2:
            #this is the second step, usually in the Prep phase
            if Approval >= 2:
                call KittyFace("smile", 1)
                ch_k "'Course!"
                $ Result = 1
            elif Approval:
                call KittyFace("sly", 2)
                if B >= 100:
                        ch_k "Yeah, I mean I guess. . ."
                if B >= 0:
                        ch_k "No offense [Girl], but. . ."
                $ K_Blush = 1
                menu:
                    extend ""
                    "Ok, that's fine. . .":
                            if B >= 100:                            
                                ch_k "No, no, let's do this."
                                $ Result = 1
                            else:
                                call KittyFace("smile")
                                ch_k "Thanks, I appreciate it."
                    "Come on, you might enjoy it. . .":
                            if B >= 50:
                                ch_k "I mean, maybe?" 
                                $ Result = 1
                            else:
                                call KittyFace("sad", 2)
                                ch_k "Probably not." 
                    "Get in there, now.":
                            if ApprovalCheck("Kitty", 550, "OI", TabM = 2):
                                call KittyFace("sadside", 1)
                                ch_k "Fiiine."
                                $ Result = 1
                            else:
                                call KittyFace("angry")
                                ch_k "You're not the boss of me!"  
                                $ K_RecentActions.append("angry")
                                $ K_DailyActions.append("angry")
                    "[Girl], what do you think?":
                            if Girl == "Rogue":
                                call RogueFace("sexy", 1)
                                if R_Les and K_Les:
                                        ch_r "You know that we work well together."
                                else:
                                        ch_r "It could be a lot of fun."
                                $ K_LikeRogue += (int(B/10))
                                if B >= 50:
                                        $ R_LikeKitty += 5
                            elif Girl == "Emma":
                                call EmmaFace("sexy", 1)
                                if E_Les and K_Les:
                                        ch_e "What's the matter Kitty, too shy around [Playername]?"
                                else:
                                        ch_e "What's the matter Kitty, I've seen how you look at me. . ."
                                $ K_LikeEmma += (int(B/10))
                                if B >= 50:
                                        $ E_LikeKitty += 5
                            elif Girl == "Laura":
                                call LauraFace("sexy", 1)
                                if L_Les and K_Les:
                                        ch_l "What, you don't want to fuck with [L_Petname] around?"
                                else:
                                        ch_l "Come on, you look like you have it in you."
                                $ K_LikeLaura += (int(B/10))
                                if B >= 50:
                                        $ L_LikeKitty += 5
                            if B >= 50:
                                call KittyFace("smile", 1)
                                ch_k "Heh, I guess so, [Girl]."
                                $ Result = 1
                            else:
                                call KittyFace("angry", 1, Eyes="side")
                                ch_k "Sorry [Girl], I don't mean anything personal."
            if Step == 3:
                    #This is a check if you interrupted them and Primary wants to do it, does Secondary?
                    if Approval:
                            call KittyFace("smile", 1)
                            ch_k "I mean, I guess. . ."
                            $ Result = 1
                    else:
                            call KittyFace("sadside", 1)
                            ch_k "I'm really not into it atm. . ."
            
            if not Result:      
                #no approval
                $ K_RecentActions.append("no lesbian")                      
                $ K_DailyActions.append("no lesbian") 
                call KittyFace("sadside", 1)
                if B <= 0:
                    ch_k "Sorry, [K_Petname], I'm just not into her."
                if Taboo:
                    ch_k "Sorry, [K_Petname], this isn't exactly the right place for that."
                if B >= 100:
                    ch_k "Sorry, [K_Petname], not with you watching. . ."
                else:
                    ch_k "Sorry, [K_Petname], I'm just not into it."
                
        return Result
#End K_Les_Response >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >


label K_Les_FirstKiss:
    # called when there is a first kiss situation between two girls
    if Partner == "Rogue":
            if "les Rogue" in K_History:
                #if they've been together before              
                $ Line = "experienced"
            elif K_Les and R_Les:   
                #if both have kissed girls before
                $ Line = "first both"
            elif K_Les:
                #Kitty's had experience              
                $ Line = "first girl"
            elif R_Les:
                #Rogue's had experience                
                $ Line = "first partner"
    elif Partner == "Emma":
            if "les Emma" in K_History:
                #if they've been together before              
                $ Line = "experienced"
            elif K_Les and E_Les:   
                #if both have kissed girls before
                $ Line = "first both"
            elif K_Les:
                #Kitty's had experience              
                $ Line = "first girl"
            elif E_Les:
                #Emma's had experience                
                $ Line = "first partner"
    elif Partner == "Laura":
            if "les Laura" in K_History:
                #if they've been together before              
                $ Line = "experienced"
            elif K_Les and L_Les:   
                #if both have kissed girls before
                $ Line = "first both"
            elif K_Les:
                #Kitty's had experience              
                $ Line = "first girl"
            elif L_Les:
                #Laura's had experience                
                $ Line = "first partner"
    
    if Line == "experienced":
            "Kitty and [Partner] move together in a passionate kiss."
            "Kitty's arms firmly grasp [Partner]'s neck and pull her close."
    else:
            if Line in ("first both", "first girl"):
                # Kitty's first time
                "Kitty tentatively moves in and gives [Partner] a soft kiss."
            else:
                #not Kitty's first time
                "Kitty casually places a hand on the back of [Partner]'s head and draws their lips together."
            if Line == "first partner":
                #other girl's first time
                "[Partner] pulls back a bit, but slowly leans into the enbrace."
            else:
                #not other girl's first time
                "[Partner]'s lips curl up into a smile and she draws Kitty even closer."                    
            "After a few seconds, it begins to grow more passionate."
    return
#End K_Les_Response >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >