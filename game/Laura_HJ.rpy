## L_Handjob //////////////////////////////////////////////////////////////////////
label L_Handjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
    if L_Hand >= 7: # She loves it
        $ Tempmod += 10
    elif L_Hand >= 3: #You've done it before several times
        $ Tempmod += 7
    elif L_Hand: #You've done it before
        $ Tempmod += 3
        
    if L_Addict >= 75 and L_Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 15
    if L_Addict >= 75:
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 15
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
        
    if "no hand" in L_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no hand" in L_RecentActions else 0    
        
    $ Approval = ApprovalCheck("Laura", 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)
    
    if Situation == "Laura":                                                                  #Laura auto-starts   
        if Approval > 2:                                                      # fix, add laura auto stuff here
            if Trigger2 == "jackin":
                "Laura brushes your hand aside and starts stroking your cock."
            else:
                "Laura gives you a mischevious smile, and starts to fondle your cock."
            menu:
                "What do you do?"
                "Nothing.":                    
                    call Statup("Laura", "Inbt", 70, 3) 
                    call Statup("Laura", "Inbt", 30, 2)                     
                    "Laura continues her actions."
                "Praise her.":       
                    call LauraFace("sexy", 1)                    
                    call Statup("Laura", "Inbt", 70, 3) 
                    ch_p "Oooh, that's good, [L_Pet]."
                    call Laura_Namecheck
                    "Laura continues her actions."
                    call Statup("Laura", "Love", 80, 1)
                    call Statup("Laura", "Obed", 90, 1)
                    call Statup("Laura", "Obed", 50, 2)
                "Ask her to stop.":
                    call LauraFace("surprised")       
                    call Statup("Laura", "Inbt", 70, 1) 
                    ch_p "Let's not do that for now, [L_Pet]."
                    call Laura_Namecheck
                    "Laura puts it down."
                    call Statup("Laura", "Obed", 90, 1)
                    call Statup("Laura", "Obed", 50, 1)
                    call Statup("Laura", "Obed", 30, 2)
                    return            
            if Trigger:
                $ Trigger3 = "hand"
                return
            jump L_HJ_Prep
        else:                
            $ Tempmod = 0                               # fix, add laura auto stuff here
            $ Trigger2 = 0
            return            
    
    if not L_Hand and "no hand" not in L_RecentActions:        
        call LauraFace("confused", 2)
        ch_l "Handjob, huh. . ."
        $ L_Blush = 1
            
    if not L_Hand and Approval:                                                 #First time dialog        
        if L_Forced: 
            call LauraFace("sad",1)
            call Statup("Laura", "Love", 70, -3, 1)
            call Statup("Laura", "Love", 20, -2, 1)
        elif L_Love >= (L_Obed + L_Inbt):
            call LauraFace("sexy",1)
            $ L_Brows = "sad"
            $ L_Mouth = "smile" 
            ch_l "You'd like that. . ."            
        elif L_Obed >= L_Inbt:
            call LauraFace("normal",1)
            ch_l "If you want, [L_Petname]. . ."      
        else: # Uninhibited 
            call LauraFace("lipbite",1)    
            ch_l "Hmm. . ."    
            
    elif Approval:                                                                       #Second time+ dialog
        if L_Forced: 
            call LauraFace("sad")
            call Statup("Laura", "Love", 70, -3, 1)
            call Statup("Laura", "Love", 20, -2, 1)
            ch_l "Nothing more than that?" 
        elif not Taboo and "tabno" in L_DailyActions:        
            ch_l "Well,this is a bit more secure. . ."    
        elif "hand" in L_RecentActions:
            call LauraFace("sexy", 1)
            ch_l "Hmm, another handy then. . ."
            jump L_HJ_Prep
        elif "hand" in L_DailyActions:
            call LauraFace("sexy", 1)
            $ Line = renpy.random.choice(["Another one?",   
                "I'm glad I don't grow calluses.", 
                "Didn't get enough earlier?",
                "Again the with handjobs, huh?",
                "I guess you want more."]) 
            ch_l "[Line]"
        elif L_Hand < 3:        
            call LauraFace("sexy", 1)
            $ L_Brows = "confused"
            $ L_Mouth = "kiss"
            ch_l "You seem to like this one. . ."        
        else:       
            call LauraFace("sexy", 1)
            $ Laura_Arms = 2
            $ Line = renpy.random.choice(["You want some more?",                 
                "So you'd like another handy?",                 
                "You want a. . . [fist pumping hand gestures]?", 
                "Another handjob?"]) 
            ch_l "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if L_Forced:
            call LauraFace("sad")
            call Statup("Laura", "Obed", 90, 1)
            call Statup("Laura", "Inbt", 60, 1)
            ch_l "Ok, fine." 
        elif "no hand" in L_DailyActions:               
            ch_l "If it'll get you off my back. . ."   
        else:
            call LauraFace("sexy", 1)
            call Statup("Laura", "Love", 90, 1)
            call Statup("Laura", "Inbt", 50, 3) 
            $ Line = renpy.random.choice(["Sure, I guess.",                 
                "O-kay.",                 
                "Fine.", 
                "I suppose I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Ok, ok."]) 
            ch_l "[Line]"
            $ Line = 0
        call Statup("Laura", "Obed", 20, 1)
        call Statup("Laura", "Obed", 60, 1)
        call Statup("Laura", "Inbt", 70, 2) 
        jump L_HJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call LauraFace("angry")
        if "no hand" in L_RecentActions:  
            ch_l "I just told you no, [L_Petname]."
        elif Taboo and "tabno" in L_DailyActions and "no hand" in L_DailyActions: 
            ch_l "I said not in public."  
        elif "no hand" in L_DailyActions:       
            ch_l "I told you \"no,\" [L_Petname]."
        elif Taboo and "tabno" in L_DailyActions:  
            ch_l "I said not in public."     
        elif not L_Hand:
            call LauraFace("bemused")
            ch_l "Seriously, [L_Petname]. . ."
        else:
            call LauraFace("bemused")
            ch_l "Nah."
        menu:
            extend ""
            "Sorry, never mind." if "no hand" in L_DailyActions:
                call LauraFace("bemused")
                ch_l "It's fine."              
                return
            "Maybe later?" if "no hand" not in L_DailyActions:
                call LauraFace("bemused")  
                ch_l "Maybe."
                call Statup("Laura", "Love", 80, 2)
                call Statup("Laura", "Inbt", 70, 2)   
                if Taboo:                    
                    $ L_RecentActions.append("tabno")                      
                    $ L_DailyActions.append("tabno") 
                $ L_RecentActions.append("no hand")                      
                $ L_DailyActions.append("no hand")            
                return
            "I'd really appreciate it. . .":             
                if Approval:
                    call LauraFace("sexy")     
                    call Statup("Laura", "Obed", 90, 2)
                    call Statup("Laura", "Obed", 50, 2)
                    call Statup("Laura", "Inbt", 70, 3) 
                    call Statup("Laura", "Inbt", 40, 2) 
                    $ Line = renpy.random.choice(["Sure, I guess.",                 
                        "O-kay.",                 
                        "Fine.", 
                        "I suppose I could. . .",
                        "Ok. . . [She gestures for you to come over].",
                        "Ok, ok."]) 
                    ch_l "[Line]"
                    $ Line = 0                   
                    jump L_HJ_Prep
                else:   
                    pass
                    
            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Laura", 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and L_Forced):
                    call LauraFace("sad")
                    call Statup("Laura", "Love", 70, -5, 1)
                    call Statup("Laura", "Love", 200, -2)                 
                    ch_l "Ok, fine."  
                    call Statup("Laura", "Obed", 50, 4)
                    call Statup("Laura", "Inbt", 80, 1) 
                    call Statup("Laura", "Inbt", 60, 3)  
                    $ L_Forced = 1  
                    jump L_HJ_Prep
                else:                              
                    call Statup("Laura", "Love", 200, -15)     
                    $ L_RecentActions.append("angry")
                    $ L_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Laura_Arms = 1 
    if "no hand" in L_DailyActions:
        call LauraFace("angry", 1)
        ch_l "Don't ask again."   
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif L_Forced:
        call LauraFace("angry", 1)
        ch_l "No."
        call Statup("Laura", "Lust", 200, 5) 
        if L_Love > 300:
                call Statup("Laura", "Love", 70, -2)
        call Statup("Laura", "Obed", 50, -2)    
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call LauraFace("angry", 1)          
        $ L_DailyActions.append("tabno") 
        ch_l "This area's too exposed."
        call Statup("Laura", "Lust", 200, 5)  
        call Statup("Laura", "Obed", 50, -3)   
    elif L_Hand:
        call LauraFace("sad") 
        ch_l "I'm not into it today. . ."       
    else:
        call LauraFace("normal", 1)
        ch_l "I don't know where that's been lately."  
    $ L_RecentActions.append("no hand")                      
    $ L_DailyActions.append("no hand") 
    $ Tempmod = 0    
    return
    

label L_HJ_Prep:
    if Trigger2 == "hand": 
        return
    
    if Taboo:
        $ L_Inbt += int(Taboo/10)  
        $ L_Lust += int(Taboo/5)
                
    call LauraFace("sexy")
    if L_Forced:
        call LauraFace("sad")
    elif L_Hand:
        $ L_Brows = "confused"
        $ L_Eyes = "sexy"
        $ L_Mouth = "smile"
    
    call Seen_First_Peen("Laura",Partner)
    call Laura_HJ_Launch("L")
    if not L_Hand:        
        if L_Forced:
            call Statup("Laura", "Love", 90, -20)
            call Statup("Laura", "Obed", 70, 25)
            call Statup("Laura", "Inbt", 80, 30) 
        else:
            call Statup("Laura", "Love", 90, 5)
            call Statup("Laura", "Obed", 70, 20)
            call Statup("Laura", "Inbt", 80, 20)     
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Laura","tabno")
    call DrainWord("Laura","no hand")
    $ L_RecentActions.append("hand")                      
    $ L_DailyActions.append("hand") 
  
label L_HJ_Cycle:    
    while Round >=0:  
        call Shift_Focus("Laura") 
        call Laura_HJ_Launch    
        call LauraLust   
        
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
                                            if L_Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ L_Action -= 1
                                            else:
                                                ch_l "Maybe we could finish this up for now?"  
                                         
                                    "Shift primary action":
                                            if L_Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    if L_Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call L_HJ_After                
                                                                        call L_Blowjob
                                                                    else:
                                                                        ch_l "Maybe we could finish this up for now?"
                                                                        
#                                                        "How about a titjob?":
#                                                                    if L_Action and MultiAction:
#                                                                        $ Situation = "shift"
#                                                                        call L_HJ_After
#                                                                        call L_Titjob
#                                                                    else:
#                                                                        ch_l "Maybe we could finish this up for now?"
                                                        "Never Mind":
                                                                jump L_HJ_Cycle
                                            else: 
                                                ch_l "Maybe we could finish this up for now?"           
                    
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
                                                        jump L_HJ_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump L_HJ_Cycle 
                                            "Never mind":
                                                        jump L_HJ_Cycle 
                                    "Undress Laura":
                                            call L_Undress   
                                    "Clean up Laura (locked)" if not L_Spunk:
                                            pass  
                                    "Clean up Laura" if L_Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump L_HJ_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Laura_HJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump L_HJ_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Laura_HJ_Reset
                                    $ Line = 0
                                    jump L_HJ_After
        #End menu (if Line)
        
        call Shift_Focus("Laura")  
        call Sex_Dialog("Laura",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or L_Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PL_Cumming
                            if "angry" in L_RecentActions:  
                                call Laura_HJ_Reset
                                return    
                            call Statup("Laura", "Lust", 200, 5) 
                            if 100 > L_Lust >= 70 and L_OCount < 2:             
                                $ L_RecentActions.append("unsatisfied")                      
                                $ L_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump L_HJ_After 
                            $ Line = "came"
     
                    if L_Lust >= 100:  
                            #If Laura can cum                                             
                            call L_Cumming
                            if Situation == "shift" or "angry" in L_RecentActions:
                                jump L_HJ_After
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in L_RecentActions:#And Laura is unsatisfied,  
                                "Laura still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump L_HJ_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if Cnt == 20:
                    $ L_Brows = "angry"        
                    menu:
                        ch_l "Hmm, this is boring, can we take a break?"
                        "How about a BJ?" if L_Action and MultiAction:
                                $ Situation = "shift"
                                call L_HJ_After
                                call L_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                jump L_HJ_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Laura_HJ_Reset
                                $ Situation = "shift"
                                jump L_HJ_After
                        "No, get back down there.":
                                if ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "O"):
                                    call Statup("Laura", "Love", 200, -5)
                                    call Statup("Laura", "Obed", 50, 3)                    
                                    call Statup("Laura", "Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    call LauraFace("angry", 1)   
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_l "I have better things to do with my time."                                               
                                    call Statup("Laura", "Love", 50, -3, 1)
                                    call Statup("Laura", "Love", 80, -4, 1)
                                    call Statup("Laura", "Obed", 30, -1, 1)                    
                                    call Statup("Laura", "Obed", 50, -1, 1)                     
                                    $ L_RecentActions.append("angry")
                                    $ L_DailyActions.append("angry")   
                                    jump L_HJ_After
        elif Cnt == 10 and L_SEXP <= 100 and not ApprovalCheck("Laura", 1200, "LO"):
                    $ L_Brows = "confused"
                    ch_l "This working for you?"         
        #End Count check
                   
        if Round == 10:
            ch_l "It's getting late, we should wrap this up."   
        elif Round == 5:
            ch_l "Tic tock, [L_Petname]."       
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, [L_Petname], breaktime."
    
label L_HJ_After:
    call LauraFace("sexy") 
    
    $ L_Hand += 1  
    $ L_Action -=1
    $ L_Addictionrate += 1
    if "addictive" in P_Traits:
        $ L_Addictionrate += 1        
    call Statup("Laura", "Lust", 90, 5)
    
    call Partner_Like("Laura",1)
            
    if "Laura Handi-Queen" in Achievements:
            pass  
    elif L_Hand >= 10:
            call LauraFace("smile", 1)
            ch_l "Looks like you filled out the punch card, [L_Petname]."
            $ Achievements.append("Laura Handi-Queen")
            $L_SEXP += 5          
    elif L_Hand == 1:            
            $L_SEXP += 10
            if L_Love >= 500:
                $ L_Mouth = "smile"
                ch_l "That was kind of. . . pleasant. . ."
            elif P_Focus <= 20:
                $ L_Mouth = "sad"
                ch_l "Did that do it for you?"
    elif L_Hand == 5:
                ch_l "I think I've got this down, maybe I should get a punch card."                  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_l "Ok, so what did you have in mind?"
    else:
        call Laura_HJ_Reset    
    call Checkout
    return

## end L_Handjob //////////////////////////////////////////////////////////////////////


## L_Titjob //////////////////////////////////////////////////////////////////////              Not finished
label L_Titjob:
    $ Round -= 5 if Round > 5 else (Round-1)    
    call Shift_Focus("Laura")
    if L_Tit >= 7: # She loves it
        $ Tempmod += 10
    elif L_Tit >= 3: #You've done it before several times
        $ Tempmod += 7
    elif L_Tit: #You've done it before
        $ Tempmod += 5
    
    if L_Addict >= 75 and L_Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 15
    elif L_Addict >= 75:
        $ Tempmod += 5
        
    if L_SeenChest and ApprovalCheck("Laura", 500): # You've seen her tits.
        $ Tempmod += 10    
    if not L_Chest and not L_Over: #She's already topless
        $ Tempmod += 10
    if L_Lust > 75: #She's really horny
        $ Tempmod += 10
    if Situation == "shift":
        $ Tempmod += 15
    if "exhibitionist" in L_Traits:
        $ Tempmod += (5*Taboo)
    if "dating" in L_Traits or "sex friend" in L_Petnames:
        $ Tempmod += 10
    elif "ex" in L_Traits:
        $ Tempmod -= 30 
    if L_ForcedCount and not L_Forced:
        $ Tempmod -= 5 * L_ForcedCount    
    
    if Taboo and "tabno" in L_DailyActions:        
        $ Tempmod -= 10 
        
    if "no titjob" in L_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no titjob" in L_RecentActions else 0    
        
    $ Approval = ApprovalCheck("Laura", 1200, TabM = 5) # 120, 135, 150, Taboo -200(320)
    
    if Situation == "Laura":                                                                  #Laura auto-starts   
        if Approval > 2:                                                      # fix, add laura auto stuff here
            call Laura_TJ_Launch("L")            
            "Laura slides down and presses your dick against her chest."
            menu:
                "What do you do?"
                "Nothing.":                    
                    call Statup("Laura", "Inbt", 80, 3) 
                    call Statup("Laura", "Inbt", 40, 2)                     
                    "Laura starts to slide up and down against it."
                "Praise her.":       
                    call LauraFace("sexy", 1)                    
                    call Statup("Laura", "Inbt", 80, 3) 
                    ch_p "Oh, that sounds like a good idea, [L_Pet]."
                    call Laura_Namecheck
                    "Laura continues her actions."
                    call Statup("Laura", "Love", 85, 1)
                    call Statup("Laura", "Obed", 90, 1)
                    call Statup("Laura", "Obed", 50, 2)
                "Ask her to stop.":     
                    call LauraFace("confused")  
                    call Statup("Laura", "Inbt", 70, 1) 
                    ch_p "Let's not do that for now, [L_Pet]."
                    call Laura_Namecheck
                    "Laura lets it drop."
                    call Statup("Laura", "Obed", 90, 1)
                    call Statup("Laura", "Obed", 50, 3)
                    call Laura_TJ_Reset  
                    return            
            jump L_TJ_Cycle
        else:                
            $ Tempmod = 0                               # fix, add laura auto stuff here
            $ Trigger2 = 0
            return            
    
    if not L_Tit and "no titjob" not in L_RecentActions:        
        call LauraFace("surprised", 1)
        $ L_Mouth = "kiss"
        ch_l "You want to rub your cock against my. . . breasts?"  
            
    if not L_Tit and Approval:                                                 #First time dialog    
        if L_Forced: 
            call LauraFace("sad")
            call Statup("Laura", "Love", 70, -3, 1)
            call Statup("Laura", "Love", 20, -2, 1)
        elif L_Love >= (L_Obed + L_Inbt):
            call LauraFace("sexy")
            $ L_Brows = "sad"
            $ L_Mouth = "smile" 
            ch_l "It's nice that you even thought about it."            
        elif L_Obed >= L_Inbt:
            call LauraFace("normal")
            ch_l "I mean. . ."              
        elif L_Addict >= 50:
            call LauraFace("manic", 1)
            ch_l "Hmmmm. . . ."     
        else: # Uninhibited 
            call LauraFace("sad")
            $ L_Mouth = "smile"             
            ch_l "Hadn't really considered that."      
    elif Approval:                                                                       #Second time+ dialog
        if L_Forced: 
            call LauraFace("sad")
            call Statup("Laura", "Love", 70, -3, 1)
            call Statup("Laura", "Love", 20, -2, 1)
            ch_l "This isn't going to become a habit, will it?"
        elif not Taboo and "tabno" in L_DailyActions:        
            ch_l "Ok, I guess this is private enough. . ."   
        elif "titjob" in L_RecentActions:
            call LauraFace("sexy", 1)
            ch_l "Mmm, again?"
            jump L_TJ_Prep
        elif "titjob" in L_DailyActions:
            call LauraFace("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",   
                "You're going to make me sore.", 
                "Didn't get enough earlier?",
                "My tits are still kinda sore from earlier."]) 
            ch_l "[Line]"
        elif L_Tit < 3:        
            call LauraFace("sexy", 1)
            $ L_Brows = "confused"
            $ L_Mouth = "kiss"
            ch_l "So you'd like another titjob?"        
        else:       
            call LauraFace("sexy", 1)
            $ Laura_Arms = 2
            $ Line = renpy.random.choice(["You want some of this action [rubs her chest]?",                 
                "So you'd like another titjob?",                  
                "So you'd like another titjob?",                               
                "So you'd like another titjob?",                              
                "A little. . . puffpuff?", 
                "A little soft embrace?"]) 
            ch_l "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if L_Forced:
            call LauraFace("sad")
            call Statup("Laura", "Obed", 90, 1)
            call Statup("Laura", "Inbt", 60, 1)
            ch_l "Well, could be worse. . ." 
        elif "no titjob" in L_DailyActions:               
            ch_l "Hmm, I guess. . ."       
        else:
            call LauraFace("sexy", 1)
            call Statup("Laura", "Love", 90, 1)
            call Statup("Laura", "Inbt", 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, put it here.",                 
                "Well. . . ok.",                 
                "Yum.", 
                "Sure, whip it out.",
                "Fine. . . [She drools a bit into her cleavage].",
                "Heh, ok."]) 
            ch_l "[Line]"
            $ Line = 0
        call Statup("Laura", "Obed", 20, 1) 
        call Statup("Laura", "Obed", 70, 1)      
        call Statup("Laura", "Inbt", 80, 2) 
        jump L_TJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call LauraFace("angry")
        if "no titjob" in L_RecentActions:  
            ch_l "I {i}just{/i} told you \"no,\" [L_Petname]."
        elif Taboo and "tabno" in L_DailyActions and "no titjob" in L_DailyActions:  
            ch_l "This is just way too exposed!"     
        elif "no titjob" in L_DailyActions:       
            ch_l "I already told you \"no,\" [L_Petname]."
        elif Taboo and "tabno" in L_DailyActions:  
            ch_l "This is just way too exposed!"     
        elif not L_Tit:
            call LauraFace("bemused")
            ch_l "I'm not really up for that, [L_Petname]. . ."
        else:
            call LauraFace("bemused")
            ch_l "Not, right now [L_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no titjob" in L_DailyActions:
                call LauraFace("bemused")
                ch_l "Yeah, ok, [L_Petname]."              
                return
            "Maybe later?" if "no titjob" not in L_DailyActions:
                call LauraFace("sexy")  
                ch_l "Maybe."
                call Statup("Laura", "Love", 80, 2)
                call Statup("Laura", "Inbt", 70, 2)   
                if Taboo:                    
                    $ L_RecentActions.append("tabno")                      
                    $ L_DailyActions.append("tabno") 
                $ L_RecentActions.append("no titjob")                      
                $ L_DailyActions.append("no titjob")            
                return
            "I think this could be fun for both of us. . .":             
                if Approval:
                    call LauraFace("sexy")     
                    call Statup("Laura", "Obed", 80, 2)
                    call Statup("Laura", "Obed", 40, 2)
                    call Statup("Laura", "Inbt", 70, 3) 
                    call Statup("Laura", "Inbt", 40, 2) 
                    $ Line = renpy.random.choice(["Well, ok, put it here.",                 
                        "Well. . . ok.",                 
                        "I guess.", 
                        "I guess, whip it out.",
                        "Fine. . . [She drools a bit into her cleavage].",
                        "Heh, ok."])
                    ch_l "[Line]"
                    $ Line = 0    
                    jump L_TJ_Prep
                else:   
                    $ Approval = ApprovalCheck("Laura", 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)             Handy instead?
                    if Approval >= 2 and L_Blow:       
                        call Statup("Laura", "Inbt", 80, 1) 
                        call Statup("Laura", "Inbt", 60, 3) 
                        call LauraFace("confused", 1)
                        ch_l "Could I[L_like]. . . blow you instead?"
                        menu:
                            ch_l "What do you say [[blowjob]?"
                            "Ok, get down there.":
                                call Statup("Laura", "Love", 80, 2)  
                                call Statup("Laura", "Inbt", 60, 1)                                
                                call Statup("Laura", "Obed", 50, 1) 
                                jump L_BJ_Prep
                            "Nah, it's all about dem titties.":  
                                $ Line = "no BJ"
                    if Approval and L_Hand:       
                        call Statup("Laura", "Inbt", 80, 1) 
                        call Statup("Laura", "Inbt", 60, 3) 
                        call LauraFace("confused", 1)
                        ch_l "Maybe you'd[L_like]settle for a handy?"
                        menu:
                            ch_l "What do you say?"
                            "Sure, that's fine.":
                                call Statup("Laura", "Love", 80, 2)  
                                call Statup("Laura", "Inbt", 60, 1)                                
                                call Statup("Laura", "Obed", 50, 1) 
                                jump L_HJ_Prep
                            "Seriously, titties." if Line == "no BJ":  
                                $ Line = 0
                            "Nah, it's all about dem titties." if Line != "no BJ":  
                                pass
                    call Statup("Laura", "Love", 200, -2)                 
                    ch_l "Nah."  
                    call Statup("Laura", "Obed", 70, 2) 
                    
                    
            "Come on, let me fuck those titties, [L_Pet]":                                               # Pressured into it                
                call Laura_Namecheck
                $ Approval = ApprovalCheck("Laura", 700, "OI", TabM = 4) # 70, 85, 100, -160(230)
                if Approval > 1 or (Approval and L_Forced):
                    call LauraFace("sad")
                    call Statup("Laura", "Love", 70, -5, 1)
                    call Statup("Laura", "Love", 200, -2)                 
                    ch_l "Ok, fine, whip it out."  
                    call Statup("Laura", "Obed", 50, 4)
                    call Statup("Laura", "Inbt", 80, 1) 
                    call Statup("Laura", "Inbt", 60, 3)  
                    $ L_Forced = 1
                    jump L_TJ_Prep
                else:                              
                    call Statup("Laura", "Love", 200, -15)     
                    $ L_RecentActions.append("angry")
                    $ L_DailyActions.append("angry")   
    
    #She refused all offers.   
    if "no titjob" in L_DailyActions:
        call LauraFace("angry", 1)
        ch_l "Look, I already told you no thanks, [L_Petname]."   
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif L_Forced:
        call LauraFace("angry", 1)
        ch_l "No, that's just weird."
        call Statup("Laura", "Lust", 200, 5)      
        if L_Love > 300:
                call Statup("Laura", "Love", 70, -2)
        call Statup("Laura", "Obed", 50, -2)      
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call LauraFace("angry", 1)          
        $ L_DailyActions.append("tabno") 
        ch_l "You really expect me to do that here? You realize how. . . exposed that would be?"
        call Statup("Laura", "Lust", 200, 5)  
        call Statup("Laura", "Obed", 50, -3)  
    elif L_Tit:
        call LauraFace("sad") 
        ch_l "I think I'll let you know when I want you touching these again."       
    else:
        call LauraFace("normal", 1)
        ch_l "How about let's not, [L_Petname]."
    $ L_RecentActions.append("no titjob")                      
    $ L_DailyActions.append("no titjob") 
    $ Tempmod = 0    
    return
    
label L_TJ_Prep:
      
    if Taboo:
        $ L_Inbt += int(Taboo/10)  
        $ L_Lust += int(Taboo/5)

        
    call LauraFace("sexy")
    if L_Forced:
        call LauraFace("sad")
    elif L_Tit:
        $ L_Brows = "confused"
        $ L_Eyes = "sexy"
        $ L_Mouth = "smile"
        
    call Seen_First_Peen("Laura",Partner)
    call Laura_TJ_Launch("L")    
    if not L_Tit:        
        if L_Forced:
            call Statup("Laura", "Love", 90, -25)
            call Statup("Laura", "Obed", 70, 30)
            call Statup("Laura", "Inbt", 80, 35) 
        else:
            call Statup("Laura", "Love", 90, 5)
            call Statup("Laura", "Obed", 70, 25)
            call Statup("Laura", "Inbt", 80, 30)   
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0  
    if Taboo:
        call DrainWord("Laura","tabno")
    call DrainWord("Laura","no titjob")
    $ L_RecentActions.append("titjob")                      
    $ L_DailyActions.append("titjob") 

label L_TJ_Cycle: #Repeating strokes  
    while Round >=0:  
        call Shift_Focus("Laura") 
        call Laura_TJ_Launch    
        call LauraLust   
        
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
                                            if L_Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ L_Action -= 1
                                            else:
                                                ch_l "Maybe we could finish this up for now?"  
                                         
                                    "Shift primary action":
                                            if L_Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                if L_Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call L_TJ_After                
                                                                    call L_Blowjob
                                                                else:
                                                                    ch_l "Maybe we could finish this up for now?"
                                                                    
                                                        "How about a handy?":
                                                                if L_Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call L_BJ_After
                                                                    call L_Handjob
                                                                else:
                                                                    ch_l "Maybe we could finish this up for now?"                                                            
                                                        "Never Mind":
                                                                jump L_TJ_Cycle
                                            else: 
                                                ch_l "Maybe we could finish this up for now?"           
                    
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
                                                        jump L_TJ_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump L_TJ_Cycle 
                                            "Never mind":
                                                        jump L_TJ_Cycle 
                                    "Undress Laura":
                                            call L_Undress   
                                    "Clean up Laura (locked)" if not L_Spunk:
                                            pass  
                                    "Clean up Laura" if L_Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump L_TJ_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Laura_TJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump L_TJ_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Laura_TJ_Reset
                                    $ Line = 0
                                    jump L_TJ_After
        #End menu (if Line)
        
        call Shift_Focus("Laura")  
        call Sex_Dialog("Laura",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or L_Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PL_Cumming
                            if "angry" in L_RecentActions:  
                                call Laura_TJ_Reset
                                return    
                            call Statup("Laura", "Lust", 200, 5) 
                            if 100 > L_Lust >= 70 and L_OCount < 2:             
                                $ L_RecentActions.append("unsatisfied")                      
                                $ L_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump L_TJ_After 
                            $ Line = "came"
     
                    if L_Lust >= 100:  
                            #If Laura can cum                                             
                            call L_Cumming
                            if Situation == "shift" or "angry" in L_RecentActions:
                                jump L_TJ_After
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in L_RecentActions:#And Laura is unsatisfied,  
                                "Laura still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump L_TJ_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if L_SEXP >= 100 or ApprovalCheck("Laura", 1200, "LO"):
                pass
        elif Cnt == (5 + L_Tit):
                $ L_Brows = "confused"
                ch_l "Are you getting close here? I'm getting as little sore."        
        if Cnt == (10 + L_Tit):
                $ L_Brows = "angry"        
                menu:
                    ch_l "I'm getting rug-burn here [L_Petname]. Can we do something else?"
                    "How about a BJ?" if L_Action and MultiAction:
                        $ Situation = "shift"
                        call L_TJ_After
                        call L_Blowjob 
                        return
                    "Finish up." if P_FocusX:
                        "You release your concentration. . ."             
                        $ P_FocusX = 0
                        $ P_Focus += 15
                        jump L_TJ_Cycle                
                    "Let's try something else." if MultiAction: 
                        $ Line = 0
                        call Laura_TJ_Reset
                        $ Situation = "shift"
                        jump L_TJ_After
                    "No, get back down there.":
                        if ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "O"):                        
                            call Statup("Laura", "Love", 200, -5)
                            call Statup("Laura", "Obed", 50, 3)                    
                            call Statup("Laura", "Obed", 80, 2)
                            "She grumbles but gets back to work."
                        else:
                            call LauraFace("angry", 1)   
                            "She scowls at you, drops you cock and pulls back."
                            ch_l "Well fuck you then."                      
                            call Statup("Laura", "Love", 50, -3, 1)
                            call Statup("Laura", "Love", 80, -4, 1)
                            call Statup("Laura", "Obed", 30, -1, 1)                    
                            call Statup("Laura", "Obed", 50, -1, 1)  
                            $ L_RecentActions.append("angry")
                            $ L_DailyActions.append("angry")   
                            jump L_TJ_After
            #End Count check
               
        if Round == 10:
            ch_l "It's kinda time to get moving."   
        elif Round == 5:
            ch_l "Tic tock, [L_Petname]."       
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, [L_Petname], breaktime."
        
label L_TJ_After:    
    call LauraFace("sexy")  
        
    $ L_Tit += 1
    $ L_Action -=1
    $ L_Addictionrate += 1
    if "addictive" in P_Traits:
        $ L_Addictionrate += 1
        
    call Partner_Like("Laura",4)
            
    if L_Tit > 5:
        pass    
    elif L_Tit == 1:
        $ L_SEXP += 12
        if L_Love >= 500:
            $ L_Mouth = "smile"
            ch_l "That was kinda fun."
        elif P_Focus <= 20:
            $ L_Mouth = "sad"
            ch_l "Well I hope you got something out of that."        
    elif L_Tit == 5:
            ch_l "Huh, I guess these are good for something."   
            
    $ Tempmod = 0    
    
    if Situation == "shift":
            ch_l "Mmm, so what else did you have in mind?"
    else:
            call Laura_TJ_Reset    
    call Checkout
    return

## end L_Titjob //////////////////////////////////////////////////////////////////////

# L_Blowjob //////////////////////////////////////////////////////////////////////

label L_Blowjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
    if L_Blow >= 7: # She loves it
        $ Tempmod += 15  
    elif L_Blow >= 3: #You've done it before several times
        $ Tempmod += 10
    elif L_Blow: #You've done it before
        $ Tempmod += 7    
        
    if L_Addict >= 75 and L_Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 25
    elif L_Addict >= 75: #She's really strung out
        $ Tempmod += 15
        
    if Situation == "shift":
        $ Tempmod += 15
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
        
    if "no blow" in L_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no blow" in L_RecentActions else 0    
    
    $ Approval = ApprovalCheck("Laura", 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)
    
    if Situation == "Laura":                                                                  #Laura auto-starts   
        if Approval > 2:                                                      # fix, add laura auto stuff here
            "Laura slides down and gives your cock a little lick."
            menu:
                "What do you do?"
                "Nothing.":                    
                    call Statup("Laura", "Inbt", 80, 3) 
                    call Statup("Laura", "Inbt", 40, 2)                     
                    "Laura continues licking at it."
                "Praise her.":       
                    call LauraFace("sexy", 1)                    
                    call Statup("Laura", "Inbt", 80, 3) 
                    ch_p "Hmmm, keep doing that, [L_Pet]."
                    call Laura_Namecheck
                    "Laura continues her actions."
                    call Statup("Laura", "Love", 85, 1)
                    call Statup("Laura", "Obed", 90, 1)
                    call Statup("Laura", "Obed", 50, 2)
                "Ask her to stop.":     
                    call LauraFace("surprised")  
                    call Statup("Laura", "Inbt", 70, 1) 
                    ch_p "Let's not do that for now, [L_Pet]."
                    call Laura_Namecheck
                    "Laura puts it down."
                    call Statup("Laura", "Obed", 90, 1)
                    call Statup("Laura", "Obed", 50, 3)
                    return            
            jump L_BJ_Prep
        else:                
            $ Tempmod = 0                               # fix, add laura auto stuff here
            $ Trigger2 = 0
            return            
    
    if not L_Blow and "no blow" not in L_RecentActions:        
        call LauraFace("surprised", 2)
        $ L_Mouth = "kiss"
        ch_l "You want me to suck your cock?"
        if L_Hand:          
            $ L_Mouth = "smile"
            ch_l "Handjobs not enough now?"        
        $ L_Blush = 1
            
    if not L_Blow and Approval:                                                 #First time dialog        
        if L_Forced: 
            call LauraFace("sad")
            call Statup("Laura", "Love", 70, -3, 1)
            call Statup("Laura", "Love", 20, -2, 1)
        elif L_Love >= (L_Obed + L_Inbt):
            call LauraFace("sexy")
            $ L_Brows = "sad"
            $ L_Mouth = "smile" 
            ch_l "I have wondered how you taste."            
        elif L_Obed >= L_Inbt:
            call LauraFace("normal")
            ch_l "If that's what you want. . ."               
        elif L_Addict >= 50:
            call LauraFace("manic", 1)
            ch_l "[[wipes away a little drool]"   
        else: # Uninhibited 
            call LauraFace("sad")
            $ L_Mouth = "smile"             
            ch_l "Huh. . ."       
    elif Approval:                                                                       #Second time+ dialog
        if L_Forced: 
            call LauraFace("sad")
            call Statup("Laura", "Love", 70, -3, 1)
            call Statup("Laura", "Love", 20, -2, 1)
            ch_l "Again?"
        elif not Taboo and "tabno" in L_DailyActions:        
            ch_l "Hmm, this is private enough. . ."    
        elif "blow" in L_RecentActions:
            call LauraFace("sexy", 1)
            ch_l "Mmm, again? [[yawns]"
            jump L_BJ_Prep                
        elif "blow" in L_DailyActions:
            call LauraFace("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",   
                "Wear'in me out here.",  
                "I must be too good at this.", 
                "Let me get some saliva going.",
                "Didn't get enough earlier?"]) 
            ch_l "[Line]"
        elif L_Blow < 3:        
            call LauraFace("sexy", 1)
            $ L_Brows = "confused"
            $ L_Mouth = "kiss"
            ch_l "You'd like another blowjob?"        
        else:       
            call LauraFace("sexy", 1)
            $ Laura_Arms = 2
            $ Line = renpy.random.choice(["You want me to [mimes blowing]?",                 
                "So you want another blowjob?",                 
                "You want me to lick you?", 
                "You want me to suck you off?",
                "A little bj?"]) 
            ch_l "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if L_Forced:
            call LauraFace("sad")
            call Statup("Laura", "Obed", 90, 1)
            call Statup("Laura", "Inbt", 60, 1)
            ch_l "Whatever."    
        elif "no blow" in L_DailyActions:               
            ch_l "Fine. . ."  
        else:
            call LauraFace("sexy", 1)
            call Statup("Laura", "Love", 90, 1)
            call Statup("Laura", "Inbt", 50, 3) 
            $ Line = renpy.random.choice(["Sure. Ahhhhhh.",                 
                "Well. . . alright.",                 
                "Yum.", 
                "Sure, whip it out.",
                "Ok. . . [She licks her lips].",
                "Alright, let's see it."]) 
            ch_l "[Line]"
            $ Line = 0
        call Statup("Laura", "Obed", 20, 1) 
        call Statup("Laura", "Obed", 70, 1)      
        call Statup("Laura", "Inbt", 80, 2) 
        jump L_BJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call LauraFace("angry")
        if "no blow" in L_RecentActions:  
            ch_l "Just told you I wouldn't, [L_Petname]."
        elif Taboo and "tabno" in L_DailyActions and "no blow" in L_DailyActions:  
            ch_l "Like I told you, not in public."  
        elif "no blow" in L_DailyActions:       
            ch_l "Told you \"no,\" [L_Petname]."
        elif Taboo and "tabno" in L_DailyActions:  
            ch_l "Like I told you, too public!"      
        elif not L_Blow:
            call LauraFace("bemused")
            ch_l "I don't know if your taste will match your scent, [L_Petname]. . ."
        else:
            call LauraFace("bemused")
            ch_l "I don't know, [L_Petname]!"
        menu:
            extend ""
            "Sorry, never mind." if "no blow" in L_DailyActions:
                call LauraFace("bemused")
                ch_l "Cool."              
                return
            "Maybe later?" if "no blow" not in L_DailyActions:
                call LauraFace("sexy")  
                ch_l "Yeah, maybe, [L_Petname]."
                call Statup("Laura", "Love", 80, 2)
                call Statup("Laura", "Inbt", 70, 2)   
                if Taboo:                    
                    $ L_RecentActions.append("tabno")                      
                    $ L_DailyActions.append("tabno") 
                $ L_RecentActions.append("no blow")                      
                $ L_DailyActions.append("no blow")            
                return
            "Come on, please?":             
                if Approval:
                    call LauraFace("sexy")     
                    call Statup("Laura", "Obed", 90, 2)
                    call Statup("Laura", "Obed", 50, 2)
                    call Statup("Laura", "Inbt", 70, 3) 
                    call Statup("Laura", "Inbt", 40, 2) 
                    $ Line = renpy.random.choice(["Sure. Ahhhhhh.",                 
                        "Well. . . alright.",                 
                        "Yum.", 
                        "Sure, whip it out.",
                        "Ok. . . [She licks her lips].",
                        "Alright, let's see it."]) 
                    ch_l "[Line]"
                    $ Line = 0                   
                    jump L_BJ_Prep
                else:   
                    if ApprovalCheck("Laura", 1100, TabM = 3): # 110, 125, 140, Taboo -120(230)             Handy instead?    
                        call Statup("Laura", "Inbt", 80, 1) 
                        call Statup("Laura", "Inbt", 60, 3) 
                        call LauraFace("confused", 1)
                        $ L_Arms = 1
                        if L_Hand:
                            ch_l "Couldn't I just use my hand again?"
                            ch_l "You seemed to like that."
                        else:
                            ch_l "I could maybe use my hand instead, how's that sound?"
                        menu:
                            extend ""
                            "Sure, that's fine.":
                                call Statup("Laura", "Love", 80, 2)  
                                call Statup("Laura", "Inbt", 60, 1)                                
                                call Statup("Laura", "Obed", 50, 1) 
                                jump L_HJ_Prep
                            "Nah, if it's not a BJ, forget it.":
                                call Statup("Laura", "Love", 200, -2)                                
                                $ L_Arms = 0                
                                ch_l "Fine, be that way."  
                                call Statup("Laura", "Obed", 70, 2)  
                    
                    
            "Suck it, [L_Pet]":                                               # Pressured into it                
                call Laura_Namecheck
                $ Approval = ApprovalCheck("Laura", 750, "OI", TabM = 3) # 75, 90, 105, -120(195)
                if Approval > 1 or (Approval and L_Forced):
                    call LauraFace("sad")
                    call Statup("Laura", "Love", 70, -5, 1)
                    call Statup("Laura", "Love", 200, -2)                 
                    ch_l "Whatever. . ."  
                    call Statup("Laura", "Obed", 50, 4)
                    call Statup("Laura", "Inbt", 80, 1) 
                    call Statup("Laura", "Inbt", 60, 3)  
                    $ L_Forced = 1
                    jump L_BJ_Prep
                else:                              
                    call Statup("Laura", "Love", 200, -15)     
                    $ L_RecentActions.append("angry")
                    $ L_DailyActions.append("angry")   
    
    #She refused all offers.   
    if "no blow" in L_DailyActions:
        call LauraFace("angry", 1)        
        $ Laura_Arms = 2
        $ L_Claws = 1
        ch_l "Suck this then."  
        $ Laura_Arms = 1
        $ L_Claws = 0
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif L_Forced:
        call LauraFace("angry", 1)
        ch_l "That's just pushing it."
        call Statup("Laura", "Lust", 200, 5)     
        if L_Love > 300:
                call Statup("Laura", "Love", 70, -2)
        call Statup("Laura", "Obed", 50, -2)      
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
        $ L_RecentActions.append("no blow")                      
        $ L_DailyActions.append("no blow") 
        return
    elif Taboo:                             # she refuses and this is too public a place for her
        call LauraFace("angry", 1)          
        $ L_DailyActions.append("tabno") 
        ch_l "This area's too exposed."
        call Statup("Laura", "Lust", 200, 5)  
        call Statup("Laura", "Obed", 50, -3)    
        return                
    elif L_Blow:
        call LauraFace("sad") 
        ch_l "Nah, not this time."       
    else:
        call LauraFace("normal", 1)
        ch_l "Nope."  
    $ L_RecentActions.append("no blow")                      
    $ L_DailyActions.append("no blow") 
    $ Tempmod = 0    
    return
    

label L_BJ_Prep:   
    if renpy.showing("Laura_HJ_Animation"):
        hide Laura_HJ_Animation with easeoutbottom
    if Taboo:
        $ L_Inbt += int(Taboo/10)  
        $ L_Lust += int(Taboo/5)
                
    call LauraFace("sexy")
    if L_Forced:
        call LauraFace("sad")
    elif L_Hand:
        $ L_Brows = "confused"
        $ L_Eyes = "sexy"
        $ L_Mouth = "smile"
    
    call Seen_First_Peen("Laura",Partner)
    call Laura_BJ_Launch("L")
    if not L_Blow:        
        if L_Forced:
            call Statup("Laura", "Love", 90, -70)
            call Statup("Laura", "Obed", 70, 45)
            call Statup("Laura", "Inbt", 80, 60) 
        else:
            call Statup("Laura", "Love", 90, 5)
            call Statup("Laura", "Obed", 70, 35)
            call Statup("Laura", "Inbt", 80, 40)     
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Laura","tabno")
    call DrainWord("Laura","no blow")
    $ L_RecentActions.append("blow")                      
    $ L_DailyActions.append("blow")     

label L_BJ_Cycle: #Repeating strokes  
    while Round >=0:  
        call Shift_Focus("Laura") 
        call Laura_BJ_Launch    
        call LauraLust   
                            
        if P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                          
                        "Lick it. . ." if Speed != 1:
                                call Speed_Shift(1)
                        "Lick it. . . (locked)" if Speed == 1:
                                pass  
                            
                        "Just the head. . ." if Speed != 2:
                                call Speed_Shift(2)
                        "Just the head. . . (locked)" if Speed == 2:
                                pass
                            
                        "Suck on it." if Speed != 3:
                                call Speed_Shift(3) 
                                if Trigger2 == "jackin":
                                    "She dips her head a bit lower, and you move your hand out of the way."
                                    
                                if "Gwentro" not in L_History: #calls the special Gwentro event
                                            call Gwentro
                                    
                        "Suck on it. (locked)" if Speed == 3:
                                pass
                            
                        "Take it deeper." if Speed != 4:
                                    if Trigger2 == "jackin" and Speed != 3:
                                        "She takes it to the root, and you move your hand out of the way."
                                    call Speed_Shift(4)
                        "Take it deeper. (locked)" if Speed == 4:
                                pass
                            
                        "Set your own pace. . .":                
                                "Laura hums contentedly."    
                                if "setpace" not in L_RecentActions:
                                    call Statup("Laura", "Love", 80, 2)
                                $ D20 = renpy.random.randint(1, 20)     
                                if L_Blow < 5:
                                    $ D20 -= 10
                                elif L_Blow < 10:
                                    $ D20 -= 5
                                    
                                if D20 > 15:
                                    call Speed_Shift(4)             
                                    if "setpace" not in L_RecentActions:      
                                        call Statup("Laura", "Inbt", 80, 3) 
                                elif D20 > 10:
                                    call Speed_Shift(3)
                                elif D20 > 5:
                                    call Speed_Shift(2)
                                else:
                                    call Speed_Shift(1)
                                $ L_RecentActions.append("setpace")
                                
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
                                            if L_Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ L_Action -= 1
                                            else:
                                                ch_l "Maybe we could finish this up for now?"  
                                         
                                    "Shift primary action":
                                            if L_Action and MultiAction:
                                                    menu:
                                                        "How about a handy?":
                                                                if L_Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call L_BJ_After
                                                                    call L_Handjob
                                                                else:
                                                                    ch_l "I need a break, can we wrap on this?"
#                                                        "How about a titjob?":
#                                                                if L_Action and MultiAction:
#                                                                    $ Situation = "shift"
#                                                                    call L_BJ_After
#                                                                    call L_Titjob
#                                                                else:
#                                                                    ch_l "I need a break, can we wrap on this?"                                        
                                                        "Never Mind":
                                                                jump L_BJ_Cycle
                                            else: 
                                                ch_l "Maybe we could finish this up for now?"           
                    
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
                                                        jump L_BJ_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump L_BJ_Cycle  
                                            "Never mind":
                                                        jump L_BJ_Cycle 
                                    "Undress Laura":
                                            call L_Undress   
                                    "Clean up Laura (locked)" if not L_Spunk:
                                            pass  
                                    "Clean up Laura" if L_Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump L_BJ_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Laura_BJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump L_BJ_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Laura_BJ_Reset
                                    $ Line = 0
                                    jump L_BJ_After
        #End menu (if Line)
                    
        call Shift_Focus("Laura")  
        call Sex_Dialog("Laura",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
        if Speed:
            $ P_Wet = 1 #wets penis        
            $ P_Spunk = 0 if P_Spunk else P_Spunk #cleans you off after one cycle
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or L_Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PL_Cumming
                            if "angry" in L_RecentActions:  
                                call Laura_BJ_Reset
                                return    
                            call Statup("Laura", "Lust", 200, 5) 
                            if 100 > L_Lust >= 70 and L_OCount < 2:             
                                $ L_RecentActions.append("unsatisfied")                      
                                $ L_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump L_BJ_After 
                            $ Line = "came"
     
                    if L_Lust >= 100:  
                            #If Laura can cum                                             
                            call L_Cumming
                            if Situation == "shift" or "angry" in L_RecentActions:
                                jump L_BJ_After
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."
                                                        
                            if "unsatisfied" in L_RecentActions:#And Laura is unsatisfied,  
                                "Laura still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump L_BJ_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if L_SEXP >= 100 or ApprovalCheck("Laura", 1200, "LO"):
            pass
        elif Cnt == (10 + L_Blow):
                $ L_Brows = "angry"        
                menu:
                    ch_l "I'm getting kinda bored. Can we do something else?"
                    "How about a Handy?" if L_Action and MultiAction:
                            $ Situation = "shift"
                            call L_BJ_After
                            call L_Handjob 
                            return
                    "Finish up." if P_FocusX:
                            "You release your concentration. . ."             
                            $ P_FocusX = 0
                            $ P_Focus += 15
                            jump L_BJ_Cycle
                    "Let's try something else." if MultiAction: 
                            $ Line = 0
                            call Laura_BJ_Reset
                            $ Situation = "shift"
                            jump L_BJ_After
                    "No, get back down there.":
                            if ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "O"):
                                call Statup("Laura", "Love", 200, -5)
                                call Statup("Laura", "Obed", 50, 3)
                                call Statup("Laura", "Obed", 80, 2)
                                "She grumbles but gets back to work."
                            else:
                                call LauraFace("angry", 1)  
                                "She scowls at you, drops you cock and pulls back."
                                ch_l "Well fuck you then."
                                call Statup("Laura", "Love", 50, -3, 1)
                                call Statup("Laura", "Love", 80, -4, 1)
                                call Statup("Laura", "Obed", 30, -1, 1)
                                call Statup("Laura", "Obed", 50, -1, 1)  
                                $ L_RecentActions.append("angry")
                                $ L_DailyActions.append("angry")   
                                jump L_BJ_After        
        elif Cnt == (5 + L_Blow) and L_SEXP <= 100 and not ApprovalCheck("Laura", 1200, "LO"):
                    $ L_Brows = "confused"
                    ch_l "Are you getting close here? I'm bored."  
        #End Count check
        
        if Round == 10:
            ch_l "It's getting late, we should wrap this up."   
        elif Round == 5:
            ch_l "Tic tock, [L_Petname]."       
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, I'm taking a quick break. . ."

label L_BJ_After:    
    call LauraFace("sexy")  
        
    $ L_Blow += 1
    $ L_Action -=1
    $ L_Addictionrate += 1
    if "addictive" in P_Traits:
        $ L_Addictionrate += 1
                
    call Partner_Like("Laura",2)
            
    if "Laura Jobber" in Achievements:
        pass
    elif L_Blow >= 10:
        call LauraFace("smile", 1)
        ch_l "Your flavor is intoxicating."      
        $ Achievements.append("Laura Jobber")
        $L_SEXP += 5
    elif Situation == "shift":
        pass
    elif L_Blow == 1:
            $L_SEXP += 15
            if L_Love >= 500:
                $ L_Mouth = "smile"
                ch_l "Hey, whaddaya know, that wasn't bad."
            elif P_Focus <= 20:
                $ L_Mouth = "sad"
                ch_l "I hope you enjoyed that."     
    elif L_Blow == 5:
        ch_l "I'm really getting the hang of this. . . right?"
        menu:
            "[[nod]":
                call LauraFace("smile", 1)
                call Statup("Laura", "Love", 90, 15)
                call Statup("Laura", "Obed", 80, 5)
                call Statup("Laura", "Inbt", 90, 10) 
            "[[shake head \"no\"]":        
                if ApprovalCheck("Laura", 500, "O"):
                    call LauraFace("sad", 2)
                    call Statup("Laura", "Love", 200, -5)
                else:
                    call LauraFace("angry", 2)
                    call Statup("Laura", "Love", 200, -25)
                call Statup("Laura", "Obed", 80, 10)
                ch_l ". . ."         
                call LauraFace("sad", 1)
    
    $ Tempmod = 0    
    if Situation != "shift":
        call Laura_BJ_Reset    
    call Checkout
    return
    


# end L_Blowjob                                 //////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label L_Dildo_Check:
    if "dildo" in P_Inventory:   
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in L_Inventory:
        "You ask Laura to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1
            
label L_Dildo_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
    call L_Dildo_Check    
    if not _return:
        return 

    if L_DildoP: #You've done it before
        $ Tempmod += 15
    if L_Legs == "pants:": # she's got pants on.
        $ Tempmod -= 20
        
    if L_Lust > 95:
        $ Tempmod += 20    
    elif L_Lust > 85: #She's really horny
        $ Tempmod += 15
        
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
        
    if "no dildo" in L_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no dildo" in L_RecentActions else 0       
        
    $ Approval = ApprovalCheck("Laura", 1250, TabM = 4) # 125, 140, 155, Taboo -160(335)
    
    if Situation == "Laura":                                                                  #Laura auto-starts   
                if Approval > 2:                                                      # fix, add laura auto stuff here
                    if L_Legs == "skirt":
                        "Laura grabs her dildo, hiking up her skirt as she does."
                        $ L_Upskirt = 1
                    elif L_Legs == "pants":
                        "Laura grabs her dildo, pulling down her pants as she does."              
                        $ L_Legs = 0
                    else:
                        "Laura grabs her dildo, rubbing is suggestively against her crotch."
                    $ L_SeenPanties = 1
                    "She slides the tip along her pussy and seems to want you to insert it."
                    menu:
                        "What do you do?"
                        "Nothing.":                    
                            call Statup("Laura", "Inbt", 80, 3) 
                            call Statup("Laura", "Inbt", 50, 2)
                            "Laura slides it in."
                        "Go for it.":       
                            call LauraFace("sexy", 1)                    
                            call Statup("Laura", "Inbt", 80, 3) 
                            ch_p "Oh yeah, [L_Pet], let's do this."
                            call Laura_Namecheck
                            "You grab the dildo and slide it in."
                            call Statup("Laura", "Love", 85, 1)
                            call Statup("Laura", "Obed", 90, 1)
                            call Statup("Laura", "Obed", 50, 2)
                        "Ask her to stop.":
                            call LauraFace("surprised")       
                            call Statup("Laura", "Inbt", 70, 1) 
                            ch_p "Let's not do that right now, [L_Pet]."
                            call Laura_Namecheck
                            "Laura sets the dildo down."
                            call LauraOutfit
                            call Statup("Laura", "Obed", 90, 1)
                            call Statup("Laura", "Obed", 50, 1)
                            call Statup("Laura", "Obed", 30, 2)
                            return            
                    jump L_DP_Prep
                else:                
                    $ Tempmod = 0                               # fix, add laura auto stuff here
                    $ Trigger2 = 0
                return            
    
    if Situation == "auto":    
                "You rub the dildo across her body, and along her moist slit."
                call LauraFace("surprised", 1)
                
                if (L_DildoP and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
                    "Laura is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                    call LauraFace("sexy")
                    call Statup("Laura", "Obed", 70, 3)
                    call Statup("Laura", "Inbt", 50, 3) 
                    call Statup("Laura", "Inbt", 70, 1) 
                    ch_l "Ooo, [L_Petname], toys!"            
                    jump L_DP_Prep         
                else:                                                                                                            #she's questioning it
                    $ L_Brows = "angry"                
                    menu:
                        ch_l "Hey, what are you planning to do with that?!" 
                        "Sorry, sorry! Never mind.":
                            if Approval:     
                                call LauraFace("sexy", 1)
                                call Statup("Laura", "Obed", 70, 3)
                                call Statup("Laura", "Inbt", 50, 3) 
                                call Statup("Laura", "Inbt", 70, 1) 
                                ch_l "Well, now that you mention it. . ."
                                jump L_DP_Prep
                            "You pull back before you really get it in."                    
                            call LauraFace("bemused", 1)
                            if L_DildoP:
                                ch_l "Well ok, [L_Petname], maybe warn me next time?" 
                            else:
                                ch_l "Well ok, [L_Petname], that's a little much. . . for now . . ."                                               
                        "Just playing with my favorite toys.":                    
                            call Statup("Laura", "Love", 80, -10, 1)  
                            call Statup("Laura", "Love", 200, -10)
                            "You press it inside some more."                              
                            call Statup("Laura", "Obed", 70, 3)
                            call Statup("Laura", "Inbt", 50, 3) 
                            if not ApprovalCheck("Laura", 700, "O", TabM=1): #Checks if Obed is 700+                             
                                call LauraFace("angry")
                                "Laura shoves you away and slaps you in the face."
                                ch_l "Jerk!"
                                ch_l "Ask nice if you want to stick something in my pussy!"                                               
                                call Statup("Laura", "Love", 50, -10, 1)                        
                                call Statup("Laura", "Obed", 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                if renpy.showing("Laura_SexSprite"):
                                    call Laura_Sex_Reset 
                                $ L_RecentActions.append("angry")
                                $ L_DailyActions.append("angry")                          
                            else:
                                call LauraFace("sad")
                                "Laura doesn't seem to be into this, you're lucky she's so obedient."                        
                                jump L_DP_Prep
                return             
    #end Auto
   
    if not L_DildoP:                                                               
            #first time    
            call LauraFace("surprised", 1)
            $ L_Mouth = "kiss"
            ch_l "Hmmm, so you'd like to try out some toys?"    
            if L_Forced:
                call LauraFace("sad")
                ch_l "I suppose there are worst things you could ask for."
            
    if not L_DildoP and Approval:                                                 
            #First time dialog        
            if L_Forced: 
                call LauraFace("sad")
                call Statup("Laura", "Love", 70, -3, 1)
                call Statup("Laura", "Love", 20, -2, 1)
            elif L_Love >= (L_Obed + L_Inbt):
                call LauraFace("sexy")
                $ L_Brows = "sad"
                $ L_Mouth = "smile" 
                ch_l "I've had a reasonable amount of experience with these, you know. . ."            
            elif L_Obed >= L_Inbt:
                call LauraFace("normal")
                ch_l "If that's what you want, [L_Petname]. . ."            
            else: # Uninhibited 
                call LauraFace("sad")
                $ L_Mouth = "smile"             
                ch_l "I guess it could be fun with a partner. . ."    
            
    elif Approval:                                                                       
            #Second time+ dialog
            if L_Forced: 
                call LauraFace("sad")
                call Statup("Laura", "Love", 70, -3, 1)
                call Statup("Laura", "Love", 20, -2, 1)
                ch_l "The toys again?" 
            elif not Taboo and "tabno" in L_DailyActions:        
                ch_l "Well, at least you got us some privacy this time. . ."   
            elif "dildo pussy" in L_RecentActions:
                call LauraFace("sexy", 1)
                ch_l "Mmm, again? Ok, let's get to it."
                jump L_DP_Prep
            elif "dildo pussy" in L_DailyActions:
                call LauraFace("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "You're going to wear me out."]) 
                ch_l "[Line]"
            elif L_DildoP < 3:        
                call LauraFace("sexy", 1)
                $ L_Brows = "confused"
                $ L_Mouth = "kiss"
                ch_l "You want to stick it in my pussy again?"       
            else:       
                call LauraFace("sexy", 1)
                $ Laura_Arms = 2
                $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my pussy again?",
                    "You want me ta lube up your toy?"]) 
                ch_l "[Line]"
                $ Line = 0
            
    if Approval >= 2:                                                                   
            #She's into it. . .               
            if L_Forced:
                call LauraFace("sad")
                call Statup("Laura", "Obed", 90, 1)
                call Statup("Laura", "Inbt", 60, 1)
                ch_l "Ok, fine."    
            else:
                call LauraFace("sexy", 1)
                call Statup("Laura", "Love", 90, 1)
                call Statup("Laura", "Inbt", 50, 3) 
                $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."]) 
                ch_l "[Line]"
                $ Line = 0
            call Statup("Laura", "Obed", 20, 1)
            call Statup("Laura", "Obed", 60, 1)
            call Statup("Laura", "Inbt", 70, 2) 
            jump L_DP_Prep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            call LauraFace("angry")
            if "no dildo" in L_RecentActions:  
                ch_l "What part of \"no,\" did you not get, [L_Petname]?"
            elif Taboo and "tabno" in L_DailyActions and "no dildo" in L_DailyActions:
                ch_l "Stop swinging that thing around in public!"   
            elif "no dildo" in L_DailyActions:       
                ch_l "I already told you \"no,\" [L_Petname]."
            elif Taboo and "tabno" in L_DailyActions:  
                ch_l "Stop swinging that thing around in public!"  
            elif not L_DildoP:
                call LauraFace("bemused")
                ch_l "I'm just not into toys, [L_Petname]. . ."
            else:
                call LauraFace("bemused")
                ch_l "I don't think we need any toys, [L_Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in L_DailyActions:
                    call LauraFace("bemused")
                    ch_l "Yeah, ok, [L_Petname]."              
                    return
                "Maybe later?" if "no dildo" not in L_DailyActions:
                    call LauraFace("sexy")  
                    ch_l "Maybe I'll practice on my own time, [L_Petname]."
                    call Statup("Laura", "Love", 80, 2)
                    call Statup("Laura", "Inbt", 70, 2)  
                    if Taboo:                    
                        $ L_RecentActions.append("tabno")                      
                        $ L_DailyActions.append("tabno") 
                    $ L_RecentActions.append("no dildo")                      
                    $ L_DailyActions.append("no dildo") 
                    return
                "I think you'd like it. . .":             
                    if Approval:
                        call LauraFace("sexy")     
                        call Statup("Laura", "Obed", 90, 2)
                        call Statup("Laura", "Obed", 50, 2)
                        call Statup("Laura", "Inbt", 70, 3) 
                        call Statup("Laura", "Inbt", 40, 2) 
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You've got me there."]) 
                        ch_l "[Line]"
                        $ Line = 0                   
                        jump L_DP_Prep
                    else:   
                        pass
                        
                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Laura", 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                    if Approval > 1 or (Approval and L_Forced):
                        call LauraFace("sad")
                        call Statup("Laura", "Love", 70, -5, 1)
                        call Statup("Laura", "Love", 200, -5)                 
                        ch_l "Ok, fine. If we're going to do this, stick it in already."  
                        call Statup("Laura", "Obed", 80, 4)
                        call Statup("Laura", "Inbt", 80, 1) 
                        call Statup("Laura", "Inbt", 60, 3)  
                        $ L_Forced = 1  
                        jump L_DP_Prep
                    else:                              
                        call Statup("Laura", "Love", 200, -20)     
                        $ L_RecentActions.append("angry")
                        $ L_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Laura_Arms = 1  
    if "no dildo" in L_DailyActions:
            ch_l "Learn to take \"no\" for an answer, [L_Petname]."   
            $ L_RecentActions.append("angry")
            $ L_DailyActions.append("angry")   
    elif L_Forced:
            call LauraFace("angry", 1)
            ch_l "I'm not going to let you use that on me."
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
            ch_l "Not here!"     
            call Statup("Laura", "Lust", 200, 5)  
            call Statup("Laura", "Obed", 50, -3)  
    elif L_DildoP:
            call LauraFace("sad") 
            ch_l "Sorry, you can keep your toys to yourself."     
    else:
            call LauraFace("normal", 1)
            ch_l "No way."  
    $ L_RecentActions.append("no dildo")                      
    $ L_DailyActions.append("no dildo")  
    $ Tempmod = 0    
    return
                
label L_DP_Prep: #Animation set-up 
    if Trigger2 == "dildo pussy":
        return
        
    if not L_Forced and Situation != "auto":
        $ Tempmod = 15 if L_Legs == "pants" else 0           
        call Laura_Bottoms_Off
        if "angry" in L_RecentActions:
            return    
            
    $ Tempmod = 0      
    call L_Pussy_Launch("dildo pussy")
    if not L_DildoP:        
        if L_Forced:
            call Statup("Laura", "Love", 90, -75)
            call Statup("Laura", "Obed", 70, 60)
            call Statup("Laura", "Inbt", 80, 35) 
        else:
            call Statup("Laura", "Love", 90, 10)
            call Statup("Laura", "Obed", 70, 20)
            call Statup("Laura", "Inbt", 80, 45)
    if Taboo:
        $ L_Inbt += int(Taboo/10)  
        $ L_Lust += int(Taboo/5)
    
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0    
    $ Cnt = 0
    if Taboo:
        call DrainWord("Laura","tabno")
    call DrainWord("Laura","no dildo")
    $ L_RecentActions.append("dildo pussy")                      
    $ L_DailyActions.append("dildo pussy") 
    
label L_DP_Cycle: #Repeating strokes    
    while Round >=0:  
        call Shift_Focus("Laura") 
        call L_Pussy_Launch("dildo pussy")
        call LauraLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                               
                        "Slap her ass":                     
                                call L_Slap_Ass
                                jump L_DP_Cycle  
                                
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
                                                ch_l "Maybe we could finish this up for now?"  
                                                
                                    "Shift primary action":
                                            if L_Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in her ass.":
                                                                $ Situation = "shift"
                                                                call L_DP_After
                                                                call L_Insert_Ass    
                                                        "Just stick a finger in her ass without asking.":
                                                                $ Situation = "auto"
                                                                call L_DP_After
                                                                call L_Insert_Ass                                           
                                                        "I want to shift the dildo to her ass.":
                                                                $ Situation = "shift"
                                                                call L_DP_After
                                                                call L_Dildo_Ass   
                                                        "Never Mind":
                                                                jump L_DP_Cycle
                                            else: 
                                                ch_l "Maybe we could finish this up for now?"           
                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call L_DP_After
                                                call Laura_Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
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
                                                        jump L_DP_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump L_DP_Cycle  
                                            "Never mind":
                                                        jump L_DP_Cycle 
                                    "Undress Laura":
                                            call L_Undress   
                                    "Clean up Laura (locked)" if not L_Spunk:
                                            pass  
                                    "Clean up Laura" if L_Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump L_DP_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call L_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump L_DP_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call L_Pos_Reset
                                    $ Line = 0
                                    jump L_DP_After
        #End menu (if Line)
        
        if L_Panties or L_Legs == "pants" or HoseNum("Laura") >= 5: #This checks if Laura wants to strip down.
                call L_Undress("auto")
            
        call Shift_Focus("Laura")  
        call Sex_Dialog("Laura",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or L_Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PL_Cumming
                            if "angry" in L_RecentActions:  
                                call L_Pos_Reset
                                return    
                            call Statup("Laura", "Lust", 200, 5) 
                            if 100 > L_Lust >= 70 and L_OCount < 2:             
                                $ L_RecentActions.append("unsatisfied")                      
                                $ L_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump L_DP_After 
                            $ Line = "came"
     
                    if L_Lust >= 100:  
                            #If Laura can cum                                             
                            call L_Cumming
                            if Situation == "shift" or "angry" in L_RecentActions:
                                jump L_DP_After
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in L_RecentActions:#And Laura is unsatisfied,  
                                "Laura still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump L_DP_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if L_SEXP >= 100 or ApprovalCheck("Laura", 1200, "LO"):
            pass
        elif Cnt == (5 + L_DildoP):
                    $ L_Brows = "confused"
                    ch_l "What are you even doing down there?" 
        elif L_Lust >= 80:
                    pass
        elif Cnt == (15 + L_DildoP) and L_SEXP >= 15 and not ApprovalCheck("Laura", 1500):
                    $ L_Brows = "confused"        
                    menu:
                        ch_l "[L_Petname], this is getting uncomfortable, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump L_DP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump L_DP_After
                        "No, this is fun.":   
                                if ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "O"):                        
                                    call Statup("Laura", "Love", 200, -5)
                                    call Statup("Laura", "Obed", 50, 3)                    
                                    call Statup("Laura", "Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call LauraFace("angry", 1)   
                                    call L_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_l "Well if that's your attitude, I don't need your \"help\"."                         
                                    call Statup("Laura", "Love", 50, -3, 1)
                                    call Statup("Laura", "Love", 80, -4, 1)
                                    call Statup("Laura", "Obed", 30, -1, 1)                    
                                    call Statup("Laura", "Obed", 50, -1, 1)  
                                    $ L_RecentActions.append("angry")
                                    $ L_DailyActions.append("angry")   
                                    jump L_DP_After
        #End Count check
           
        if Round == 10:
            ch_l "It's getting late, we should wrap this up."   
        elif Round == 5:
            ch_l "Tic tock, [L_Petname]."       
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, [L_Petname], breaktime."
    
    
label L_DP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call L_Pos_Reset
        
    call LauraFace("sexy") 
    
    $ L_DildoP += 1  
    $ L_Action -=1   
            
    call Partner_Like("Laura",1)
            
    if L_DildoP == 1:            
            $ L_SEXP += 10         
            if not Situation: 
                if L_Love >= 500 and "unsatisfied" not in L_RecentActions:
                    ch_l "Thanks for the extra hand. . ."
                elif L_Obed <= 500 and P_Focus <= 20:
                    call LauraFace("perplexed", 1)
                    ch_l "Did you like that?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# end L_Dildo Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Insert Ass    

label L_Dildo_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
    call L_Dildo_Check
    if not _return:
        return 
      
    if L_Loose:
        $ Tempmod += 30   
    elif "anal" in L_RecentActions or "dildo anal" in L_RecentActions:
        $ Tempmod -= 20 
    elif "anal" in L_DailyActions or "dildo anal" in L_DailyActions:
        $ Tempmod -= 10
    elif (L_Anal + L_DildoA + L_Plug) > 0: #You've done it before
        $ Tempmod += 20   
        
    if L_Legs == "pants:": # she's got pants on.
        $ Tempmod -= 20   
        
    if L_Lust > 95:
        $ Tempmod += 20
    elif L_Lust > 85: #She's really horny
        $ Tempmod += 15
        
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
        
    if "no dildo" in L_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no dildo" in L_RecentActions else 0   
        
    $ Approval = ApprovalCheck("Laura", 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)
    
    if Situation == "Laura":                                                                  
            #Laura auto-starts   
            if Approval > 2:                                                      # fix, add laura auto stuff here
                if L_Legs == "skirt":
                    "Laura grabs her dildo, hiking up her skirt as she does."
                    $ L_Upskirt = 1
                elif L_Legs == "pants":
                    "Laura grabs her dildo, pulling down her pants as she does."              
                    $ L_Legs = 0
                else:
                    "Laura grabs her dildo, rubbing is suggestively against her ass."
                $ L_SeenPanties = 1
                "She slides the tip against her asshole, and seems to want you to insert it."
                menu:
                    "What do you do?"
                    "Nothing.":                    
                        call Statup("Laura", "Inbt", 80, 3) 
                        call Statup("Laura", "Inbt", 50, 2)
                        "Laura slides it in."
                    "Go for it.":       
                        call LauraFace("sexy", 1)                    
                        call Statup("Laura", "Inbt", 80, 3) 
                        ch_p "Oh yeah, [L_Pet], let's do this."
                        call Laura_Namecheck
                        "You grab the dildo and slide it in."
                        call Statup("Laura", "Love", 85, 1)
                        call Statup("Laura", "Obed", 90, 1)
                        call Statup("Laura", "Obed", 50, 2)
                    "Ask her to stop.":
                        call LauraFace("surprised")       
                        call Statup("Laura", "Inbt", 70, 1) 
                        ch_p "Let's not do that right now, [L_Pet]."
                        call Laura_Namecheck
                        "Laura sets the dildo down."
                        call LauraOutfit
                        call Statup("Laura", "Obed", 90, 1)
                        call Statup("Laura", "Obed", 50, 1)
                        call Statup("Laura", "Obed", 30, 2)
                        return            
                jump L_DA_Prep
            else:                
                $ Tempmod = 0                               # fix, add laura auto stuff here
                $ Trigger2 = 0
            return            
    
    if Situation == "auto":    
            "You rub the dildo across her body, and against her tight anus."
            call LauraFace("surprised", 1)
            
            if (L_DildoA and Approval) or (Approval > 1):                                                                      
                #this is not the first time you've had sex, or she's into it         
                "Laura is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                call LauraFace("sexy")
                call Statup("Laura", "Obed", 70, 3)
                call Statup("Laura", "Inbt", 50, 3) 
                call Statup("Laura", "Inbt", 70, 1)
                ch_l "Ooo, [L_Petname], toys!"                
                jump L_DA_Prep         
            else:                                                                                                            
                #she's questioning it
                $ L_Brows = "angry"                
                menu:
                    ch_l "Hey, what are you planning to do with that?!" 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            call LauraFace("sexy", 1)
                            call Statup("Laura", "Obed", 70, 3)
                            call Statup("Laura", "Inbt", 50, 3) 
                            call Statup("Laura", "Inbt", 70, 1) 
                            ch_l "Well, now that you mention it. . ."
                            jump L_DA_Prep
                        "You pull back before you really get it in."                    
                        call LauraFace("bemused", 1)
                        if L_DildoA:
                            ch_l "Well ok, [L_Petname], maybe warn me next time?" 
                        else:
                            ch_l "Well ok, [L_Petname], that's a little much. . . for now . . ."                                                   
                    "Just playing with my favorite toys.":                    
                        call Statup("Laura", "Love", 80, -10, 1)  
                        call Statup("Laura", "Love", 200, -10)
                        "You press it inside some more."                              
                        call Statup("Laura", "Obed", 70, 3)
                        call Statup("Laura", "Inbt", 50, 3) 
                        if not ApprovalCheck("Laura", 700, "O", TabM=1): #Checks if Obed is 700+                           
                            call LauraFace("angry")
                            "Laura shoves you away and slaps you in the face."
                            ch_l "Jerk!"
                            ch_l "Ask nice if you want to stick something in my ass!"                                                  
                            call Statup("Laura", "Love", 50, -10, 1)                        
                            call Statup("Laura", "Obed", 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            if renpy.showing("Laura_SexSprite"):
                                call Laura_Sex_Reset 
                            $ L_RecentActions.append("angry")
                            $ L_DailyActions.append("angry")                         
                        else:
                            call LauraFace("sad")
                            "Laura doesn't seem to be into this, you're lucky she's so obedient."                        
                            jump L_DA_Prep
            return             
    #end auto
   
    if not L_DildoA:                                                               
            #first time    
            call LauraFace("surprised", 1)
            $ L_Mouth = "kiss"
            ch_l "You want to try and fit that. . .?"    
            if L_Forced:
                call LauraFace("sad")
                ch_l "Always about the butt, huh?"
    
    if not L_Loose and ("dildo anal" in L_RecentActions or "anal" in L_RecentActions or "dildo anal" in L_DailyActions or "anal" in L_DailyActions):
            call LauraFace("bemused", 1)
            ch_l "I'm still[L_like]sore from earlier. . ."
            
    if not L_DildoA and Approval:                                                 
            #First time dialog        
            if L_Forced: 
                call LauraFace("sad")
                call Statup("Laura", "Love", 70, -3, 1)
                call Statup("Laura", "Love", 20, -2, 1)
            elif L_Love >= (L_Obed + L_Inbt):
                call LauraFace("sexy")
                $ L_Brows = "sad"
                $ L_Mouth = "smile" 
                ch_l "I[L_like]haven't actually used one of these, back there before. . ."            
            elif L_Obed >= L_Inbt:
                call LauraFace("normal")
                ch_l "If that's what you want, [L_Petname]. . ."            
            else: # Uninhibited 
                call LauraFace("sad")
                $ L_Mouth = "smile"             
                ch_l "I guess it could be fun two-player. . ."    
            
    elif Approval:                                                                       
            #Second time+ dialog
            if L_Forced: 
                call LauraFace("sad")
                call Statup("Laura", "Love", 70, -3, 1)
                call Statup("Laura", "Love", 20, -2, 1)
                ch_l "The toys again?"  
            elif not Taboo and "tabno" in L_DailyActions:        
                ch_l "Well, at least you got us some privacy this time. . ."   
            elif "dildo anal" in L_DailyActions and not L_Loose:
                pass
            elif "dildo anal" in L_DailyActions:
                call LauraFace("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "I'm still a bit sore from earlier.",
                    "You're going to wear me out."]) 
                ch_l "[Line]"
            elif L_DildoA < 3:        
                call LauraFace("sexy", 1)
                $ L_Brows = "confused"
                $ L_Mouth = "kiss"
                ch_l "You want to stick it in my ass again?"       
            else:       
                call LauraFace("sexy", 1)
                $ Laura_Arms = 2
                $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my ass again?",
                    "You want me ta lube up your toy?"]) 
                ch_l "[Line]"
                $ Line = 0
            
    if Approval >= 2:                                                                  
            #She's into it. . .               
            if L_Forced:
                call LauraFace("sad")
                call Statup("Laura", "Obed", 90, 1)
                call Statup("Laura", "Inbt", 60, 1)
                ch_l "Ok, fine."    
            else:
                call LauraFace("sexy", 1)
                call Statup("Laura", "Love", 90, 1)
                call Statup("Laura", "Inbt", 50, 3) 
                $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."]) 
                ch_l "[Line]"
                $ Line = 0
            call Statup("Laura", "Obed", 20, 1)
            call Statup("Laura", "Obed", 60, 1)
            call Statup("Laura", "Inbt", 70, 2) 
            jump L_DA_Prep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            call LauraFace("angry")
            if "no dildo" in L_RecentActions:  
                ch_l "What part of \"no,\" did you not get, [L_Petname]?"
            elif Taboo and "tabno" in L_DailyActions and "no dildo" in L_DailyActions:
                ch_l "Stop swinging that thing around in public!"  
            elif "no dildo" in L_DailyActions:       
                ch_l "I already told you \"no,\" [L_Petname]."
            elif Taboo and "tabno" in L_DailyActions:  
                ch_l "I already told you that I wouldn't do that out here!"  
            elif not L_DildoA:
                call LauraFace("bemused")
                ch_l "I'm just not into toys, [L_Petname]. . ."
            elif not L_Loose and "dildo anal" not in L_DailyActions:
                call LauraFace("perplexed")
                ch_l "You could have been a bit more gentle last time, [L_Petname]. . ."
            else:
                call LauraFace("bemused")
                ch_l "I don't think we need any toys, [L_Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in L_DailyActions:
                    call LauraFace("bemused")
                    ch_l "Yeah, ok, [L_Petname]."              
                    return
                "Maybe later?" if "no dildo" not in L_DailyActions:
                    call LauraFace("sexy")  
                    ch_l "Maybe I'll practice on my own time, [L_Petname]."
                    call Statup("Laura", "Love", 80, 2)
                    call Statup("Laura", "Inbt", 70, 2)  
                    if Taboo:                    
                        $ L_RecentActions.append("tabno")                      
                        $ L_DailyActions.append("tabno") 
                    $ L_RecentActions.append("no dildo")                      
                    $ L_DailyActions.append("no dildo") 
                    return
                "I think you'd like it. . .":             
                    if Approval:
                        call LauraFace("sexy")     
                        call Statup("Laura", "Obed", 90, 2)
                        call Statup("Laura", "Obed", 50, 2)
                        call Statup("Laura", "Inbt", 70, 3) 
                        call Statup("Laura", "Inbt", 40, 2) 
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You've got me there."]) 
                        ch_l "[Line]"
                        $ Line = 0                   
                        jump L_DA_Prep
                    else:   
                        pass
                        
                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Laura", 1050, "OI", TabM = 3) # 105, 120, 135, -120(225)
                    if Approval > 1 or (Approval and L_Forced):
                        call LauraFace("sad")
                        call Statup("Laura", "Love", 70, -5, 1)
                        call Statup("Laura", "Love", 200, -5)                 
                        ch_l "Ok, fine. If we're going to do this, stick it in already."  
                        call Statup("Laura", "Obed", 80, 4)
                        call Statup("Laura", "Inbt", 80, 1) 
                        call Statup("Laura", "Inbt", 60, 3)  
                        $ L_Forced = 1  
                        jump L_DA_Prep
                    else:                              
                        call Statup("Laura", "Love", 200, -20)    
                        $ L_RecentActions.append("angry")
                        $ L_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Laura_Arms = 1   
    if "no dildo" in L_DailyActions:
            ch_l "Learn to take \"no\" for an answer, [L_Petname]."   
            $ L_RecentActions.append("angry")
            $ L_DailyActions.append("angry")   
    elif L_Forced:
            call LauraFace("angry", 1)
            ch_l "I'm not going to let you use that on me."
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
            ch_l "Not here!"     
            call Statup("Laura", "Lust", 200, 5)  
            call Statup("Laura", "Obed", 50, -3)  
    elif not L_Loose and "dildo anal" in L_DailyActions:
            call LauraFace("bemused")
            ch_l "Sorry, I just need a little break back there, [L_Petname]."    
    elif L_DildoA:
            call LauraFace("sad") 
            ch_l "Sorry, you can keep your toys out of there."     
    else:
            call LauraFace("normal", 1)
            ch_l "No way." 
    $ L_RecentActions.append("no dildo")                      
    $ L_DailyActions.append("no dildo")   
    $ Tempmod = 0    
    return
                
label L_DA_Prep: #Animation set-up 
    if Trigger2 == "dildo anal":
        return
        
    if not L_Forced and Situation != "auto":
        $ Tempmod = 20 if L_Legs == "pants" else 0           
        call Laura_Bottoms_Off
        if "angry" in L_RecentActions:
            return    
            
    $ Tempmod = 0      
    call L_Pussy_Launch("dildo anal")
    if not L_DildoA:        
        if L_Forced:
            call Statup("Laura", "Love", 90, -75)
            call Statup("Laura", "Obed", 70, 60)
            call Statup("Laura", "Inbt", 80, 35) 
        else:
            call Statup("Laura", "Love", 90, 10)
            call Statup("Laura", "Obed", 70, 20)
            call Statup("Laura", "Inbt", 80, 45)
    if Taboo:
        $ L_Inbt += int(Taboo/10)  
        $ L_Lust += int(Taboo/5)
    
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0    
    $ Cnt = 0
    if Taboo:
        call DrainWord("Laura","tabno")
    call DrainWord("Laura","no dildo")
    $ L_RecentActions.append("dildo anal")                      
    $ L_DailyActions.append("dildo anal") 
    
label L_DA_Cycle: #Repeating strokes    
    while Round >=0:  
        call Shift_Focus("Laura") 
        call L_Pussy_Launch("dildo anal")
        call LauraLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                               
                        "Slap her ass":                     
                                call L_Slap_Ass
                                jump L_DA_Cycle  
                                
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
                                                ch_l "Maybe we could finish this up for now?"  
                                                
                                    "Shift primary action":
                                            if L_Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in her pussy.":
                                                                $ Situation = "shift"
                                                                call L_DA_After
                                                                call L_Fondle_Pussy    
                                                        "Just stick a finger in her pussy without asking.":
                                                                $ Situation = "auto"
                                                                call L_DA_After
                                                                call L_Fondle_Pussy                                           
                                                        "I want to shift the dildo to her pussy.":
                                                                $ Situation = "shift"
                                                                call L_DA_After
                                                                call L_Dildo_Pussy 
                                                        "Never Mind":
                                                                jump L_DA_Cycle
                                            else: 
                                                ch_l "Maybe we could finish this up for now?"           
                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call L_DA_After
                                                call Laura_Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
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
                                                        jump L_DA_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump L_DA_Cycle                                        
                                    "Never mind":
                                            jump L_DA_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call L_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump L_DA_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call L_Pos_Reset
                                    $ Line = 0
                                    jump L_DA_After
        #End menu (if Line)
        
        if L_Panties or L_Legs == "pants" or HoseNum("Laura") >= 5: #This checks if Laura wants to strip down.
                call L_Undress("auto")
            
        call Shift_Focus("Laura")  
        call Sex_Dialog("Laura",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or L_Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PL_Cumming
                            if "angry" in L_RecentActions:  
                                call L_Pos_Reset
                                return    
                            call Statup("Laura", "Lust", 200, 5) 
                            if 100 > L_Lust >= 70 and L_OCount < 2:             
                                $ L_RecentActions.append("unsatisfied")                      
                                $ L_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump L_DA_After 
                            $ Line = "came"
     
                    if L_Lust >= 100:  
                            #If Laura can cum                                             
                            call L_Cumming
                            if Situation == "shift" or "angry" in L_RecentActions:
                                jump L_DA_After
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in L_RecentActions:#And Laura is unsatisfied,  
                                "Laura still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump L_DA_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if L_SEXP >= 100 or ApprovalCheck("Laura", 1200, "LO"):
            pass
        elif Cnt == (5 + L_DildoA):
                    $ L_Brows = "confused"
                    ch_l "What are you even doing down there?" 
        elif L_Lust >= 80:
                    pass
        elif Cnt == (15 + L_DildoA) and L_SEXP >= 15 and not ApprovalCheck("Laura", 1500):
                    $ L_Brows = "confused"        
                    menu:
                        ch_l "[L_Petname], this is getting uncomfortable, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump L_DA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump L_DA_After
                        "No, this is fun.":   
                                if ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "O"):                        
                                    call Statup("Laura", "Love", 200, -5)
                                    call Statup("Laura", "Obed", 50, 3)                    
                                    call Statup("Laura", "Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call LauraFace("angry", 1)   
                                    call L_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_l "Well if that's your attitude, I don't need your \"help\"."                         
                                    call Statup("Laura", "Love", 50, -3, 1)
                                    call Statup("Laura", "Love", 80, -4, 1)
                                    call Statup("Laura", "Obed", 30, -1, 1)                    
                                    call Statup("Laura", "Obed", 50, -1, 1)  
                                    $ L_RecentActions.append("angry")
                                    $ L_DailyActions.append("angry")   
                                    jump L_DA_After
        #End Count check
           
        if Round == 10:
            ch_l "It's getting late, we should wrap this up."   
        elif Round == 5:
            ch_l "Tic tock, [L_Petname]."       
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, [L_Petname], breaktime."
    
label L_DA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call L_Pos_Reset
        
    call LauraFace("sexy") 
    
    $ L_DildoA += 1  
    $ L_Action -=1            
    
    call Partner_Like("Laura",1)
            
    if L_DildoA == 1:            
            $ L_SEXP += 10         
            if not Situation: 
                if L_Love >= 500 and "unsatisfied" not in L_RecentActions:
                    if L_Loose:
                        ch_l "That was. . . interesting. . ."
                    else:
                        ch_l "Ouch. . ."
                elif L_Obed <= 500 and P_Focus <= 20:
                    call LauraFace("perplexed", 1)
                    ch_l "Did you like that?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# end L_Dildo Ass /////////////////////////////////////////////////////////////////////////////

label L_Vibrator_Check:                                                                                 #fix this whole section is copy/paste unfinished
    if "vibrator" in P_Inventory:   
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in L_Inventory:
        "You ask Laura to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1    
    
## L_Footjob //////////////////////////////////////////////////////////////////////
label L_Footjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
    if L_Foot >= 7: # She loves it
        $ Tempmod += 10
    elif L_Foot >= 3: #You've done it before several times
        $ Tempmod += 7
    elif L_Foot: #You've done it before
        $ Tempmod += 3
        
    if L_Addict >= 75 and L_Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 10
    if L_Addict >= 75:
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 15
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
        
    if "no foot" in L_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no foot" in L_RecentActions else 0    
        
    $ Approval = ApprovalCheck("Laura", 1250, TabM = 3) # 110, 125, 140, Taboo -120(230)
    
    if Situation == "Laura":                                                                  #Laura auto-starts   
        if Approval > 2:                                                      # fix, add laura auto stuff here
            "Laura leans back  and starts rubbing your cock between her feet."
            menu:
                "What do you do?"
                "Nothing.":                    
                    call Statup("Laura", "Inbt", 70, 3) 
                    call Statup("Laura", "Inbt", 30, 2)                     
                    "Laura continues her actions."
                "Praise her.":       
                    call LauraFace("sexy", 1)                    
                    call Statup("Laura", "Inbt", 70, 3) 
                    ch_p "Oooh, that's good, [L_Pet]."
                    call Laura_Namecheck
                    "Laura continues her actions."
                    call Statup("Laura", "Love", 80, 1)
                    call Statup("Laura", "Obed", 90, 1)
                    call Statup("Laura", "Obed", 50, 2)
                "Ask her to stop.":
                    call LauraFace("surprised")       
                    call Statup("Laura", "Inbt", 70, 1) 
                    ch_p "Let's not do that for now, [L_Pet]."
                    call Laura_Namecheck
                    "Laura puts it down."
                    call Statup("Laura", "Obed", 90, 1)
                    call Statup("Laura", "Obed", 50, 1)
                    call Statup("Laura", "Obed", 30, 2)
                    return            
            if Trigger:
                $ Trigger3 = "foot"
                return
            jump L_FJ_Prep
        else:                
            $ Tempmod = 0                               # fix, add laura auto stuff here
            $ Trigger2 = 0
            return            
    
    if not L_Foot and "no foot" not in L_RecentActions:        
        call LauraFace("confused", 2)
        ch_l "Huh, so you'd like me to touch your cock with my feet?"
        $ L_Blush = 1
            
    if not L_Foot and Approval:                                                 #First time dialog        
        if L_Forced: 
            call LauraFace("sad",1)
            call Statup("Laura", "Love", 70, -3, 1)
            call Statup("Laura", "Love", 20, -2, 1)
        elif L_Love >= (L_Obed + L_Inbt):
            call LauraFace("sexy",1)
            $ L_Brows = "sad"
            $ L_Mouth = "smile" 
            ch_l "I guess it couldn't hurt. . ."            
        elif L_Obed >= L_Inbt:
            call LauraFace("normal",1)
            ch_l "If you want, [L_Petname]. . ."            
        elif L_Addict >= 50:
            call LauraFace("manic", 1)
            ch_l "Okay. . ."  
        else: # Uninhibited 
            call LauraFace("lipbite",1)    
            ch_l "Sure. . ."    
            
    elif Approval:                                                                       #Second time+ dialog
        if L_Forced: 
            call LauraFace("sad")
            call Statup("Laura", "Love", 70, -3, 1)
            call Statup("Laura", "Love", 20, -2, 1)
            ch_l "That's all?" 
        elif not Taboo and "tabno" in L_DailyActions:        
            ch_l "Um, I guess this is secluded enough. . ."    
        elif "foot" in L_RecentActions:
            call LauraFace("sexy", 1)
            ch_l "I'm getting foot cramps. . ."
            jump L_FJ_Prep
        elif "foot" in L_DailyActions:
            call LauraFace("sexy", 1)
            $ Line = renpy.random.choice(["Another one?",   
                "You're going to give me calluses.", 
                "Didn't get enough earlier?",
                "My feet are kinda sore from earlier.",
                "My feet are kinda sore from earlier."]) 
            ch_l "[Line]"
        elif L_Foot < 3:        
            call LauraFace("sexy", 1)
            $ L_Brows = "confused"
            $ L_Mouth = "kiss"
            ch_l "Hmm, magic toes. . ."        
        else:       
            call LauraFace("sexy", 1)
            $ Laura_Arms = 2
            $ Line = renpy.random.choice(["You want me to use my feet?",                 
                "So you'd like another foot sesh?",                 
                "A little. . . [she rubs her foot along your leg]?", 
                "A little TLC?"]) 
            ch_l "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if L_Forced:
            call LauraFace("sad")
            call Statup("Laura", "Obed", 90, 1)
            call Statup("Laura", "Inbt", 60, 1)
            ch_l "Ok, fine." 
        elif "no foot" in L_DailyActions:               
            ch_l "OK, geeze!"   
        else:
            call LauraFace("sexy", 1)
            call Statup("Laura", "Love", 90, 1)
            call Statup("Laura", "Inbt", 50, 3) 
            $ Line = renpy.random.choice(["Sure, I guess.",                 
                "Ooooookay.",                 
                "Cool, lemme see it.", 
                "I guess I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Heh, ok, ok."]) 
            ch_l "[Line]"
            $ Line = 0
        call Statup("Laura", "Obed", 20, 1)
        call Statup("Laura", "Obed", 60, 1)
        call Statup("Laura", "Inbt", 70, 2) 
        jump L_FJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call LauraFace("angry")
        if "no foot" in L_RecentActions:  
            ch_l "You don't[L_like]listen do you, [L_Petname]."
        elif Taboo and "tabno" in L_DailyActions and "no foot" in L_DailyActions: 
            ch_l "I said not in public!"  
        elif "no foot" in L_DailyActions:       
            ch_l "I told you \"no,\" [L_Petname]."
        elif Taboo and "tabno" in L_DailyActions:  
            ch_l "I said not in public!"     
        elif not L_Foot:
            call LauraFace("bemused")
            ch_l "I don't know, [L_Petname]. . ."
        else:
            call LauraFace("bemused")
            ch_l "Not now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no foot" in L_DailyActions:
                call LauraFace("bemused")
                ch_l "Yeah."              
                return
            "Maybe later?" if "no foot" not in L_DailyActions:
                call LauraFace("sexy")  
                ch_l ". . ."
                ch_l "Maybe."
                call Statup("Laura", "Love", 80, 2)
                call Statup("Laura", "Inbt", 70, 2)   
                if Taboo:                    
                    $ L_RecentActions.append("tabno")                      
                    $ L_DailyActions.append("tabno") 
                $ L_RecentActions.append("no foot")                      
                $ L_DailyActions.append("no foot")            
                return
            "I'd really appreciate it. . .":             
                if Approval:
                    call LauraFace("sexy")     
                    call Statup("Laura", "Obed", 90, 2)
                    call Statup("Laura", "Obed", 50, 2)
                    call Statup("Laura", "Inbt", 70, 3) 
                    call Statup("Laura", "Inbt", 40, 2) 
                    $ Line = renpy.random.choice(["Sure, I guess.",                 
                            "Ooooookay.",                 
                            "Cool, lemme see it.", 
                            "I guess I could. . .",
                            "Ok. . . [She gestures for you to come over].",
                            "Heh, ok, ok."]) 
                    ch_l "[Line]"
                    $ Line = 0                   
                    jump L_FJ_Prep
                else:   
                    pass
                    
            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Laura", 400, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and L_Forced):
                    call LauraFace("sad")
                    call Statup("Laura", "Love", 70, -5, 1)
                    call Statup("Laura", "Love", 200, -2)                 
                    ch_l "Ok, fine."  
                    call Statup("Laura", "Obed", 50, 4)
                    call Statup("Laura", "Inbt", 80, 1) 
                    call Statup("Laura", "Inbt", 60, 3)  
                    $ L_Forced = 1  
                    jump L_FJ_Prep
                else:                              
                    call Statup("Laura", "Love", 200, -15)     
                    $ L_RecentActions.append("angry")
                    $ L_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Laura_Arms = 1 
    if "no foot" in L_DailyActions:
        call LauraFace("angry", 1)
        ch_l "I'm not telling you again."   
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif L_Forced:
        call LauraFace("angry", 1)
        ch_l "I don't even want to step on it."
        call Statup("Laura", "Lust", 200, 5)    
        if L_Love > 300:
                call Statup("Laura", "Love", 70, -2)
        call Statup("Laura", "Obed", 50, -2)    
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call LauraFace("angry", 1)          
        $ L_DailyActions.append("tabno") 
        ch_l "Not here, not anywhere near here."
        call Statup("Laura", "Lust", 200, 5)  
        call Statup("Laura", "Obed", 50, -3)   
    elif L_Foot:
        call LauraFace("sad") 
        ch_l "I'm not feeling it today. . ."       
    else:
        call LauraFace("normal", 1)
        ch_l "I don't know about using my feet for. . . that."  
    $ L_RecentActions.append("no foot")                      
    $ L_DailyActions.append("no foot") 
    $ Tempmod = 0    
    return
    

label L_FJ_Prep:
    if Trigger2 == "foot": 
        return
    
    if Taboo:
        $ L_Inbt += int(Taboo/10)  
        $ L_Lust += int(Taboo/5)
                
    call LauraFace("sexy")
    if L_Forced:
        call LauraFace("sad")
    elif L_Foot:
        $ L_Brows = "confused"
        $ L_Eyes = "sexy"
        $ L_Mouth = "smile"
    
    call Seen_First_Peen("Laura",Partner)
    
    if not L_Foot:        
        if L_Forced:
            call Statup("Laura", "Love", 90, -20)
            call Statup("Laura", "Obed", 70, 25)
            call Statup("Laura", "Inbt", 80, 30) 
        else:
            call Statup("Laura", "Love", 90, 5)
            call Statup("Laura", "Obed", 70, 20)
            call Statup("Laura", "Inbt", 80, 20)     
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Laura","tabno")
    call DrainWord("Laura","no foot")
    $ L_RecentActions.append("foot")                      
    $ L_DailyActions.append("foot") 
  
label L_FJ_Cycle:    
    while Round >=0:  
        call Shift_Focus("Laura") 
        call Laura_Sex_Launch("foot")    
        call LauraLust   
        
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
                                            if L_Action and MultiAction:
                                                call Laura_Offhand_Set
                                                if Trigger2:
                                                     $ L_Action -= 1
                                            else:
                                                ch_l "I kinda need a break, so if we could wrap this up?"  
                                                
                                    "Shift primary action":
                                            if L_Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    if L_Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call L_FJ_After                
                                                                        call L_Blowjob
                                                                    else:
                                                                        ch_l "Maybe we could finish this up for now?"
                                                        "How about a handjob?":
                                                                    if L_Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call L_FJ_After                
                                                                        call L_Handjob
                                                                    else:
                                                                        ch_l "Maybe we could finish this up for now?"
                                                                        
#                                                        "How about a titjob?":
#                                                                    if L_Action and MultiAction:
#                                                                        $ Situation = "shift"
#                                                                        call L_FJ_After
#                                                                        call L_Titjob
#                                                                    else:
#                                                                        ch_l "Maybe we could finish this up for now?"
                                                                
                                                        
                                                        
                                                        "Never Mind":
                                                                jump L_FJ_Cycle
                                            else: 
                                                ch_l "Maybe we could finish this up for now?"           
                    
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
                                                        jump L_FJ_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump L_FJ_Cycle 
                                            "Never mind":
                                                        jump L_FJ_Cycle 
                                    "Undress Laura":
                                            call L_Undress   
                                    "Clean up Laura (locked)" if not L_Spunk:
                                            pass  
                                    "Clean up Laura" if L_Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump L_FJ_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Laura_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump L_FJ_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Laura_Sex_Reset
                                    $ Line = 0
                                    jump L_FJ_After
        #End menu (if Line)
        
        call Shift_Focus("Laura")  
        call Sex_Dialog("Laura",Partner)
                
        #If either of you could cum 
        
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
                                jump L_FJ_After 
                            $ Line = "came"
     
                    if L_Lust >= 100:  
                            #If Laura can cum                                             
                            call L_Cumming
                            if Situation == "shift" or "angry" in L_RecentActions:
                                jump L_FJ_After
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in L_RecentActions:#And Laura is unsatisfied,  
                                "Laura still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump L_FJ_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if Cnt == 20:
                    $ L_Brows = "angry"        
                    menu:
                        ch_l "Ouch, foot cramp, can we[L_like]take a break?"
                        "How about a BJ?" if L_Action and MultiAction:
                                $ Situation = "shift"
                                call L_FJ_After
                                call L_Blowjob   
                        "How about a Handy?" if L_Action and MultiAction:
                                $ Situation = "shift"
                                call L_FJ_After
                                call L_Handjob  
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump L_FJ_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Laura_Sex_Reset
                                $ Situation = "shift"
                                jump L_FJ_After
                        "No, get back down there.":
                                if ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "O"):
                                    call Statup("Laura", "Love", 200, -5)
                                    call Statup("Laura", "Obed", 50, 3)                    
                                    call Statup("Laura", "Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    call LauraFace("angry", 1)   
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_l "Hey, I've got better things to do if you're[L_like]going to be a dick about it."                                               
                                    call Statup("Laura", "Love", 50, -3, 1)
                                    call Statup("Laura", "Love", 80, -4, 1)
                                    call Statup("Laura", "Obed", 30, -1, 1)                    
                                    call Statup("Laura", "Obed", 50, -1, 1)                     
                                    $ L_RecentActions.append("angry")
                                    $ L_DailyActions.append("angry")   
                                    jump L_FJ_After
        elif Cnt == 10 and L_SEXP <= 100 and not ApprovalCheck("Laura", 1200, "LO"):
                    $ L_Brows = "confused"
                    ch_l "Can we[L_Like]be done with this now? I'm getting sore."         
        #End Count check
                   
        if Round == 10:
            ch_l "It's getting late, we should wrap this up."   
        elif Round == 5:
            ch_l "Tic tock, [L_Petname]."       
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, [L_Petname], breaktime."
    
label L_FJ_After:
    call LauraFace("sexy") 
    
    $ L_Foot += 1  
    $ L_Action -=1
    $ L_Addictionrate += 1
    if "addictive" in P_Traits:
        $ L_Addictionrate += 1        
    call Statup("Laura", "Lust", 90, 5)
    
    call Partner_Like("Laura",1)
    
    if "Laurapedi" in Achievements:
            pass  
    elif L_Foot >= 10:
            call LauraFace("smile", 1)
            ch_l "I guess I've gotten pretty smooth at the \"Laurapedi.\""
            $ Achievements.append("Laurapedi")
            $ L_SEXP += 5          
    elif L_Foot == 1:            
            $ L_SEXP += 10
            if L_Love >= 500:
                $ L_Mouth = "smile"
                ch_l "I could feel you down there. . ."
            elif P_Focus <= 20:
                $ L_Mouth = "sad"
                ch_l "Did that work out for you?"
    elif L_Foot == 5:
                ch_l "Let me know any time you need me to \"foot you up.\""                  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_l "Ok, so what did you have in mind?"
    else:
        call Laura_Sex_Reset    
    call Checkout
    return

## end L_Footjob //////////////////////////////////////////////////////////////////////




# Start L_Lesbian ////////////////////////////////////////////////////////////////////////
label L_Les_Interupted:  
        # Called if you catch them fucking 
        if "unseen" not in L_RecentActions:
                if L_Org < 3 and L_Action:                
                    menu:
                        "Did you want to stop them?"
                        "Yeah.":
                            pass
                        "No, let them keep going.":
                            $ L_Action -= 1 if L_Action > 0 else 0
                            jump L_Les_Cycle 
                else:
                    ch_l "Ahhh, that hit the spot. . ."
                jump L_Les_After
        call DrainWord("Laura","unseen",1,0) #She sees you, so remove unseens
        call DrainWord(Partner,"unseen",1,0) #She sees you, so remove unseens
        call LauraFace("surprised", 1)
        "Suddenly, Laura jerks up from what she was doing with a start, and gives [Partner] a nudge."
        call LauraFace("bemused", 0)
        ch_l "Oh! Hey [Playername], how long have you been there?"
        $ L_Action -= 1 if L_Action > 0 else 0
        call Checkout(1)
        $ Line = 0
    
        #If you've been jacking it
        if Trigger2 == "jackin":
                $ L_Eyes = "down"
                menu:
                    ch_l "Looks like you're taking care of yourself."
                    "Yeah, it was an excellent show.":   
                            call LauraFace("sexy")
                            call Statup("Laura", "Obed", 50, 3)
                            call Statup("Laura", "Obed", 70, 2)
                            "Laura glances over at [Partner]."
                            ch_l "I get that. . ."
                            if L_Love >= 800 or L_Obed >= 500 or L_Inbt >= 500:
                                $ Tempmod += 10
                                call Statup("Laura", "Lust", 90, 5)
                                ch_l "You're not so bad to look at either. . ."  
                            
                    "I. . . just got here?":
                            call LauraFace("angry")                   
                            call Statup("Laura", "Love", 70, 2)
                            call Statup("Laura", "Love", 90, 1)
                            call Statup("Laura", "Obed", 50, 2)
                            call Statup("Laura", "Obed", 70, 2)
                            "She looks pointedly at your cock,"
                            ch_l "Uh HUH. . ."   
                            if L_Love >= 800 or L_Obed >= 500 or L_Inbt >= 500:
                                    $ Tempmod += 10
                                    call Statup("Laura", "Lust", 90, 5)
                                    call LauraFace("bemused", 1)
                                    ch_l "-can't blame you though."   
                            else:
                                    $ Tempmod -= 10
                                    call Statup("Laura", "Lust", 200, -5)
                call Seen_First_Peen("Laura",Partner) 
        else:         
                #you haven't been jacking it         
                menu:                    
                    ch_l "Oh! Hey [Playername], how long have you been there?"
                    "Long enough.":   
                            call LauraFace("sexy", 1)
                            call Statup("Laura", "Obed", 50, 3)
                            call Statup("Laura", "Obed", 70, 2)
                            ch_l "Didn't intend to put on a show. . ."
                    "I just got here.":
                            call LauraFace("bemused", 1)
                            call Statup("Laura", "Love", 70, 2)
                            call Statup("Laura", "Love", 90, 1)                    
                            ch_l "Uh HUH. . ."   
                            call Statup("Laura", "Obed", 50, 2)
                            call Statup("Laura", "Obed", 70, 2)    
                                
        if not ApprovalCheck("Laura", 1350):
                #If she doesn't like you enough to have you around. . .
                call Statup("Laura", "Love", 200, -5)
                call LauraFace("angry")
                $ L_RecentActions.append("angry")
                $ L_DailyActions.append("angry")
                ch_l "So maybe just leave us to it?"
                $ renpy.pop_call()
                $ renpy.pop_call()
                if bg_current == "bg player":                                        
                    jump Campus_Map  
                else:
                    jump Player_Room  
        
        if Round <= 10:
            ch_l "I guess we could take a break though."
            return
        $ Situation = "interrupted"
    
label L_LesScene(Bonus = 0): #Repeating strokes
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
    if L_LesWatch:
        $ Tempmod += 10
    elif L_Les:
        $ Tempmod += 5
    if L_SEXP >= 50:
        $ Tempmod += 25
    elif L_SEXP >= 30:
        $ Tempmod += 15
    elif L_SEXP >= 15:
        $ Tempmod += 5
        
    if L_Lust >= 90:
        $ Tempmod += 5
    elif L_Lust >= 75:
        $ Tempmod += 5
        
    elif L_Inbt >= 750:
        $ Tempmod += 5
        
    if "exhibitionist" in L_Traits:      
        $ Tempmod += (3*Taboo) 
        
    if "dating" in L_Traits or "sex friend" in L_Petnames:
        $ Tempmod += 10        
    elif "ex" in L_Traits:
        $ Tempmod -= 40  
        
    if R_Loc == bg_current:
            #if it's Rogue. . .
            $ R_RecentActions.append("noticed Laura")
            $ L_RecentActions.append("noticed Rogue")
            $ Partner = "Rogue"  
            if L_LikeRogue >= 900:
                    $ Bonus += 150
            elif L_LikeRogue >= 800 or "poly Rogue" in L_Traits:
                    $ Bonus += 100
            elif L_LikeRogue >= 700:
                    $ Bonus += 50
            elif L_LikeRogue <= 200:
                    $ Bonus -= 200
            elif L_LikeRogue <= 500:
                    $ Bonus -= 100
            call DrainWord("Rogue","unseen",1,0) #She sees you, so remove unseens
    elif E_Loc == bg_current:
            #if it's Emma. . .
            $ E_RecentActions.append("noticed Laura")
            $ L_RecentActions.append("noticed Emma")
            $ Partner = "Emma"  
            if L_LikeEmma >= 900:
                    $ Bonus += 150
            elif L_LikeEmma >= 800 or "poly Emma" in L_Traits:
                    $ Bonus += 100
            elif L_LikeEmma >= 700:
                    $ Bonus += 50
            elif L_LikeEmma <= 200:
                    $ Bonus -= 200
            elif L_LikeEmma <= 500:
                    $ Bonus -= 100
            call DrainWord("Emma","unseen",1,0) #She sees you, so remove unseens
    elif K_Loc == bg_current:
            #if it's Kitty. . .
            $ K_RecentActions.append("noticed Laura")
            $ L_RecentActions.append("noticed Kitty")
            $ Partner = "Kitty"  
            if L_LikeKitty >= 900:
                    $ Bonus += 150
            elif L_LikeKitty >= 800 or "poly Kitty" in L_Traits:
                    $ Bonus += 100
            elif L_LikeKitty >= 700:
                    $ Bonus += 50
            elif L_LikeKitty <= 200:
                    $ Bonus -= 200
            elif L_LikeKitty <= 500:
                    $ Bonus -= 100
            call DrainWord("Kitty","unseen",1,0) #She sees you, so remove unseens
            
    if bg_current in ("bg player", "bg laura", "bg rogue", "bg emma"):
        $ Taboo == 0
    if L_ForcedCount and not L_Forced:
        $ Tempmod -= 5 * L_ForcedCount   
        
    $ Approval = ApprovalCheck("Laura", 1350, TabM = 2, Bonus = Bonus) # 1350, 1500, 1650, Taboo -800
    
    call DrainWord("Laura","unseen",1,0) #She sees you, so remove unseens
    
    if Situation == "interrupted":    
        menu:
            extend ""
            "I guess I should probably get going then. . .":
                    call Statup("Laura", "Love", 80, 3)
                    if Approval >= 2:
                            # if Laura is very much in
                            ch_l "Hmmmm, I don't know about that. . ."
                            if R_Loc == bg_current:
                                    call R_Les_Response("Laura",3,B2=Bonus)                          
                            elif E_Loc == bg_current:
                                    call E_Les_Response("Laura",3,B2=Bonus)                        
                            elif K_Loc == bg_current:
                                    call K_Les_Response("Laura",3,B2=Bonus)
                            if not _return:
                                    return
                    else:
                            # If Laura is only so/so, but Rogue is on board, she tries to convince Laura
                            if R_Loc == bg_current:
                                    call R_Les_Response("Laura",1,B2=Bonus)                         
                            elif E_Loc == bg_current:
                                    call E_Les_Response("Laura",1,B2=Bonus)                          
                            elif K_Loc == bg_current:
                                    call K_Les_Response("Laura",1,B2=Bonus)                  
                            if not _return:
                                    #this is the default reaction if Rogue is not into it either
                                    if Approval:
                                        ch_l "You could chill here."
                                        return
                                    else:
                                        ch_l "Yeah. . ."  
                                        $ renpy.pop_call()
                                        $ renpy.pop_call()
                                        if bg_current == "bg player":                                        
                                            jump Campus_Map  
                                        else:
                                            jump Player_Room  
                            elif not Approval:
                                    ch_l "Sorry [L_Petname], maybe come back later."
                                    return                            
                            elif not L_Action:
                                    ch_l "Sorry [L_Petname], looks like we're taking a break. . ."
                                    return        
                            else:
                                    ch_l "Sure."    
                    #if it passed the hurdles. . .
                    jump L_Les_Prep
            "So maybe I could join you girls?" if P_Semen and L_Action:
                    call LauraFace("sexy")
                    ch_l "Oh, what are you bringing to the table?"    
                    $ Situation = "join"
                    return                      #returns to sexmenu=
            "So maybe I could watch a bit longer?":
                    call LauraFace("bemused", 1)   
    #End "Interrupted" content.
    
    #first time
    if not L_LesWatch:                                                                
            call LauraFace("surprised", 1)
            $ L_Mouth = "kiss"
            ch_l "You want to watch me and [Partner] hook up?"
            if L_Forced:
                call LauraFace("sad")
                ch_l "{i}Just{/i} watching, right?"
                
    if Approval and Partner == "Rogue" and "touch" not in R_Traits:
            ch_l "I don't know, Rogue's touch can be. . . intense. . ."
            ch_p "Don't worry, I can keep it turned off."
            ch_l "Oh, well I guess. . ."
                     
    if not L_LesWatch and Approval:   
            #First time dialog                                                       
            if L_Forced: 
                call LauraFace("sad")
                call Statup("Laura", "Love", 70, -3, 1)
                call Statup("Laura", "Love", 20, -2, 1)
            elif Bonus >= 100:
                call LauraFace("sly", Eyes="side")
                ch_l "Well you'd be in for a treat. . ."   
            elif L_Love >= (L_Obed + L_Inbt):
                call LauraFace("sexy")
                $ L_Brows = "sad"
                $ L_Mouth = "smile" 
                ch_l "I hadn't really considered putting on a show like this. . ."          
            elif L_Obed >= L_Inbt:
                call LauraFace("normal")
                ch_l "I'm ok with that, [L_Petname]. . ."            
            else: # Uninhibited 
                call LauraFace("sad")
                $ L_Mouth = "smile"             
                ch_l "Not that I mind. . ."    
    
    
    elif Approval:            
                #Second time+ initial dialog                                                           
                if L_Forced: 
                        call LauraFace("sad")
                        call Statup("Laura", "Love", 70, -3, 1)
                        call Statup("Laura", "Love", 20, -2, 1)
                        ch_l "This is what gets you off?"  
                elif Approval and "lesbian" in L_RecentActions:
                        call LauraFace("sexy", 1)
                        ch_l "I wouldn't mind a little more. . ."    
                        jump L_Les_Prep
                elif Approval and "lesbian" in L_DailyActions:
                        call LauraFace("sexy", 1)
                        $ Line = renpy.random.choice(["Enjoyed the show?",       
                            "Didn't get enough earlier?",
                            "I don't mind having an audience. . ."]) 
                        ch_l "[Line]"            
                elif L_Mast < 3:        
                        call LauraFace("sexy", 1)
                        $ L_Brows = "confused"
                        ch_l "You do like to watch."       
                else:       
                        call LauraFace("sexy", 1)
                        $ Laura_Arms = 2
                        $ Line = renpy.random.choice(["You do like to watch.",                 
                            "So you'd like us to go again?",                 
                            "You want to watch some more?",
                            "You want me to get it on with "+Partner+"?"]) 
                        ch_l "[Line]"
                        $ Line = 0                        
    #End second time+ initial dialog
    
    if Approval >= 2:      
                #If she's into it. . .                                                                            
                if L_Forced:
                    call LauraFace("sad")
                    call Statup("Laura", "Obed", 90, 1)
                    call Statup("Laura", "Inbt", 60, 1)
                    ch_l "Not the worst way to spend some time. . ." 
                else:
                    call LauraFace("sexy", 1)
                    call Statup("Laura", "Love", 90, 1)
                    call Statup("Laura", "Inbt", 50, 3) 
                    $ Line = renpy.random.choice(["Well. . . ok.",                 
                        "I don't mind getting with her. . .",
                        "I kinda needed to blow off some steam. . .",
                        "Sure.", 
                        "I guess. . .",
                        "Heh, ok, fine."]) 
                    ch_l "[Line]"
                    $ Line = 0
                call Statup("Laura", "Obed", 20, 1)
                call Statup("Laura", "Obed", 60, 1)
                call Statup("Laura", "Inbt", 70, 2) 
                jump L_Les_Partner   
    #end instant approval
            
    else:       
        #If she's not into it, but maybe. . .                                                                                    
        menu:
            ch_l "I don't know, [L_Petname]."
            "Maybe later?":
                    call LauraFace("sexy", 1)  
                    if Bonus >= 100:
                        call Statup("Laura", "Inbt", 90, 5)  
                        ch_l "Maybe some other time. . ."
                    elif Bonus >= 0:
                        call LikeUpdater("Laura",3)
                        ch_l "Eh, I don't know. . ."
                    else:
                        call LauraFace("angry", 1, Eyes="side") 
                        ch_l "Probably not."
                    call LauraFace("smile", 1) 
                    call Statup("Laura", "Love", 80, 2)
                    call Statup("Laura", "Inbt", 70, 5)   
                    call Taboo_Level
                    return
                    
            "You look like you might be into it. . .":             
                    if Approval:
                            call LauraFace("sexy")     
                            call Statup("Laura", "Obed", 90, 4)
                            call Statup("Laura", "Obed", 50, 5)
                            call Statup("Laura", "Inbt", 70, 4) 
                            call Statup("Laura", "Inbt", 40, 4) 
                            $ Line = renpy.random.choice(["Well. . . ok.",                 
                                "I don't mind getting with her. . .",
                                "I kinda needed to blow off some steam. . .",
                                "Sure.", 
                                "I guess. . .",
                                "Heh, ok, fine."]) 
                            ch_l "[Line]"
                            $ Line = 0                   
                            jump L_Les_Partner
                    else:   
                            pass
                    
            "Just get at it already.":                                              
                    # Pressured into it
                    $ Approval = ApprovalCheck("Laura", 550, "OI", TabM = 2) # 55, 70, 85
                    if Approval > 1 or (Approval and L_Forced):
                            call LauraFace("sad")
                            call Statup("Laura", "Love", 70, -5, 1)
                            call Statup("Laura", "Love", 200, -5)                 
                            ch_l "Ok, if you insist."  
                            call Statup("Laura", "Obed", 80, 4)
                            call Statup("Laura", "Inbt", 80, 1) 
                            call Statup("Laura", "Inbt", 60, 3)  
                            $ L_Forced = 1  
                            jump L_Les_Partner
                    else:                              
                            call Statup("Laura", "Love", 200, -20)     
                            $ L_RecentActions.append("angry")
                            $ L_DailyActions.append("angry")
    # end of asking her to do it
    
    if R_Loc == bg_current:
            call R_Les_Response("Laura",1,B2=Bonus)
    elif E_Loc == bg_current:
            call E_Les_Response("Laura",1,B2=Bonus)
    elif K_Loc == bg_current:
            call K_Les_Response("Laura",1,B2=Bonus)
    if _return:
            #if the other girl convinces her
            call LauraFace("smile", 1)
            ch_l "Ok, if {i}you're{/i} into it."
            ch_l "Get over here. . ."
            jump L_Les_Prep
            
            
    #She refused all offers.
    $ Laura_Arms = 1                
    if not Partner:
            ch_l "I don't know if I should feel insulted. . ."
    elif L_Forced:
            call LauraFace("angry", 1)
            ch_l "I'm not into that."
            call Statup("Laura", "Lust", 90, 5)         
            if L_Love > 300:
                call Statup("Laura", "Love", 70, -2)
            call Statup("Laura", "Obed", 50, -2)    
            $ L_RecentActions.append("angry")
            $ L_DailyActions.append("angry")  
    elif Taboo > 20:                            
            # she refuses and this is too public a place for her
            call LauraFace("angry", 1)          
            $ L_DailyActions.append("tabno") 
            ch_l "Not someplace so public."     
            call Statup("Laura", "Lust", 90, 5)  
            call Statup("Laura", "Obed", 50, -3) 
    elif L_Les:
            call LauraFace("sad") 
            if Bonus >= 100:
                ch_l "I'm not up for that."     
            else:    
                ch_l "Not with an audience."     
    else:
            call LauraFace("normal", 1)
            ch_l "Nope."  
    $ L_RecentActions.append("no lesbian")                      
    $ L_DailyActions.append("no lesbian") 
    $ Tempmod = 0 
    call Taboo_Level
    return
    
label L_Les_Partner:
    # This checks to see if the other girl is into it. 
    if R_Loc == bg_current:
            call R_Les_Response("Laura",2)
            if not _return:
                    # If Rogue refused
                    return
    elif E_Loc == bg_current:
            call E_Les_Response("Laura",2)
            if not _return:
                    # If Emma refused
                    return
    elif K_Loc == bg_current:
            call K_Les_Response("Laura",2)
            if not _return:
                    # If Kitty refused
                    return
            
label L_Les_Prep:    
    #sets the scene up   
    
    if R_Loc == bg_current:
            if "noticed Laura" not in R_RecentActions:
                    $ R_RecentActions.append("noticed Laura")  
            if "noticed Rogue" not in L_RecentActions:
                    $ L_RecentActions.append("noticed Rogue")           
            $ Partner = "Rogue"  
    elif E_Loc == bg_current:
            if "noticed Laura" not in E_RecentActions:
                    $ E_RecentActions.append("noticed Laura")  
            if "noticed Emma" not in L_RecentActions:
                    $ L_RecentActions.append("noticed Emma")           
            $ Partner = "Emma"  
    elif K_Loc == bg_current:
            if "noticed Laura" not in K_RecentActions:
                    $ K_RecentActions.append("noticed Laura")  
            if "noticed Kitty" not in L_RecentActions:
                    $ L_RecentActions.append("noticed Kitty")           
            $ Partner = "Kitty" 
            
    if "unseen" not in L_RecentActions:
            #if she knows you're there. . .
            call LauraFace("sexy")
            $ Laura_Arms = 2
            "Laura move's closer to [Partner] and wraps her arms around her neck."
            if not L_LesWatch:
                    #First time        
                    if L_Forced:
                        call Statup("Laura", "Love", 90, -20)
                        call Statup("Laura", "Obed", 70, 55)
                        call Statup("Laura", "Inbt", 80, 55) 
                    else:
                        call Statup("Laura", "Love", 90, 5)
                        call Statup("Laura", "Obed", 70, 20)
                        call Statup("Laura", "Inbt", 80, 60)  
            call L_Les_FirstKiss
            $ Trigger3 == "kiss girl"
            $ Trigger4 == "kiss girl"
        
    $ Trigger = "lesbian"   
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0 
    $ Line = 0
    if Taboo:
        call DrainWord("Laura","tabno")
    call DrainWord("Laura","no lesbian")
    $ L_RecentActions.append("lesbian")                      
    $ L_DailyActions.append("lesbian") 
    
label L_Les_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Laura")
        call Les_Launch("Laura")  
        call LauraLust     

        if  P_Focus < 100:                                                    
                    #Player Command menu
                    menu:
                        "Keep watching. . .":
                                    pass
                                   
                        "\"Ahem. . .\"" if "unseen" in L_RecentActions:  
                                jump L_Les_Interupted   
                                
                        "Start jack'in it." if Trigger2 != "jackin":
                                call L_Jackin                   
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
                                            if L_Action and MultiAction:
                                                call Laura_Offhand_Set
                                                if Trigger2:
                                                     $ L_Action -= 1
                                            else:
                                                ch_l "I need a break, can we wrap on this?"  
                                            
                                    "Threesome actions":   
                                        menu:
                                            "Ask Laura to do something else with [Partner]":
                                                    if "unseen" in L_RecentActions:
                                                            ch_p "Oh yeah, why don't you. . ."
                                                            jump L_Les_Interupted
                                                    else:                        
                                                            call Laura_Les_Change
                                            "Ask [Partner] to do something else":
                                                    if "unseen" in L_RecentActions:
                                                            ch_p "Oh yeah, why don't you. . ."
                                                            jump L_Les_Interupted
                                                    else:                        
                                                        call Partner_Threechange("Laura")  
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                    if "unseen" in L_RecentActions:
                                                            ch_p "Oh, that's good. . ."
                                                            jump L_Les_Interupted
                                                    else:                        
                                                            $ ThreeCount = 0  
                                                            
#                                            "Swap to [Partner]":
#                                                        call Trigger_Swap("Laura")
                                            "Undress [Partner]":
                                                    if "unseen" in L_RecentActions:
                                                            ch_p "Oh, yeah, take it off. . ."
                                                            jump L_Les_Interupted
                                                    else:                        
                                                            call Partner_Undress
                                                            jump L_Les_Cycle 
                                            "Clean up Partner":
                                                    if "unseen" in L_RecentActions:
                                                            ch_p "You've got a little something. . ."
                                                            jump L_Les_Interupted
                                                    else:                        
                                                            call Partner_Cleanup
                                                            jump L_Les_Cycle 
                                            "Never mind":
                                                        jump L_Les_Cycle 
                                    "Undress Laura":
                                            if "unseen" in L_RecentActions:
                                                    ch_p "Oh yeah, why don't you. . ."
                                                    jump L_Les_Interupted
                                            else:                        
                                                    call L_Undress   
                                    "Clean up Laura (locked)" if not L_Spunk:
                                            pass  
                                    "Clean up Laura" if L_Spunk:
                                            if "unseen" in L_RecentActions:
                                                ch_p "You've got a little something. . ."
                                                jump L_Les_Interupted
                                            else:                        
                                                call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump L_Les_Cycle  
                                            
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call L_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump L_Les_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call L_Pos_Reset
                                    $ Line = 0
                                    jump L_Les_After   
        #End menu (if Line)
        
        call Shift_Focus("Laura")  
        call Sex_Dialog("Laura",Partner)
        
        $ Cnt += 1
        $ Round -= 1
             
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or L_Lust >= 100:    
                    #If either of you can cum:
                    if P_Focus >= 100:
                            #If you can cum:  
                            if "unseen" not in L_RecentActions: #if she knows you're there
                                call PL_Cumming
                                if "angry" in L_RecentActions:  
                                    call L_Pos_Reset
                                    return    
                                call Statup("Laura", "Lust", 200, 5) 
                                if 100 > L_Lust >= 70 and L_OCount < 2:             
                                    $ L_RecentActions.append("unsatisfied")                      
                                    $ L_DailyActions.append("unsatisfied") 
                                $ Line = "came"
                            else: #If she wasn't aware you were there
                                "You grunt and try to hold it in."
                                $ P_Focus = 95
                                jump L_Les_Interupted
     
                    if L_Lust >= 100: 
                            #If Laura can cum                                              
                            call L_Cumming
                            jump L_Les_Interupted
                       
                    if Line == "came": 
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."      
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
                            
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if "unseen" in L_RecentActions:
                if Round == 10:
                    "It's getting a bit late, Laura and [Partner] will probably be wrapping up soon."  
                elif Round == 5:
                    "They're definitely going to stop soon."
        else:
                if Round == 10:
                    ch_l "It's getting late, we should wrap this up." 
                elif Round == 5:
                    ch_l "Tic tock, [L_Petname]."   
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    if "unseen" not in L_RecentActions:
        ch_l "Ok, [L_Petname], breaktime."
    

label L_Les_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call L_Pos_Reset
        
    call LauraFace("sexy") 
        
    if Partner == "Emma":
        call Partner_Like("Laura",4)
    else:
        call Partner_Like("Laura",3)
            
    $ L_LesWatch += 1 
    if L_LesWatch == 1:            
            $ L_SEXP += 15    
            if L_Love >= 500 and L_Org:
                    ch_l "I enjoyed the audience. . ." 
    
    if not Situation:
            ch_l "That was fun. . ."
            if R_Loc == bg_current:
                if "les laura" not in R_History:
                        if L_LikeRogue >= 600:
                                ch_l "You've got game there."
                        else:
                                ch_l "That was pretty good. . ."
                        if R_LikeLaura >= 600:
                                ch_r "Um, yeah, you too. . ."
                        else:
                                ch_r "I guess. . ."
                        $ L_History.append("les rogue")   
                        $ R_History.append("les laura")  
                else:
                    #second time
                    ch_r "Mmmm yeah. . ."
            elif E_Loc == bg_current:
                if "les laura" not in E_History:
                        if L_LikeEmma >= 600:
                                ch_l "I liked that thing with the mouth work."
                        else:
                                ch_l "You seem to know your way around. . ."
                        if E_LikeLaura >= 600:
                                ch_e "Practice, dear. . ."
                        else:
                                ch_e "It would be better if you'd had more practice, dear."
                        $ L_History.append("les emma")   
                        $ E_History.append("les laura")  
                else:
                    #second time
                    ch_e "Certainly. . ."
            elif K_Loc == bg_current:
                if "les laura" not in K_History:
                        if L_LikeKitty >= 600:
                                ch_l "Really cute work there."
                        else:
                                ch_l "That was ok. . ."
                        if K_LikeLaura >= 600:
                                ch_k "Yeah, that was really hot. . ."
                        else:
                                ch_k "I guess. . ."
                        $ L_History.append("les kitty")   
                        $ K_History.append("les laura")  
                else:
                    #second time
                    ch_k "Mmmm yeah that was good. . ."
                    
                        
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# End R LesScene


    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

label Laura_Les_Change(D20S=0, Secondary=Partner, Primary = "Laura", PrimaryLust=0, SecondaryLust=0):
        # for Lesbian primary activity: Laura_Threeway_Set("preset", "lesbian", Trigger3, ActiveGirl)
        #this is called when the player wants to change over a lesbian T3 behavior.
        $ Line = 0
        menu:
            "Hey Laura. . ."
            "why don't you kiss her?" if Trigger5 != "kiss girl" and Trigger5 != "kiss both":
                    call Laura_Threeway_Set("kiss girl", "lesbian", Trigger3)
            "why don't you grab her tits?" if Trigger3 != "fondle breasts":
                    call Laura_Threeway_Set("fondle breasts", "lesbian", Trigger3)
            "why don't you suck her breasts?" if Trigger3 != "suck breasts":
                    call Laura_Threeway_Set("suck breasts", "lesbian", Trigger3)
            "why don't you finger her?" if Trigger3 != "fondle pussy":
                    call Laura_Threeway_Set("fondle pussy", "lesbian", Trigger3)
            "why don't you go down on her?" if Trigger3 != "lick pussy":
                    call Laura_Threeway_Set("lick pussy", "lesbian", Trigger3)
            "why don't you grab her ass?" if Trigger3 != "fondle ass":
                    call Laura_Threeway_Set("fondle ass", "lesbian", Trigger3)
            "why don't you lick her ass?" if Trigger3 != "lick ass":
                    call Laura_Threeway_Set("lick ass", "lesbian", Trigger3) 
            "never mind.":
                pass
        if not Line:
            $ Line = "You return to what you were doing." 
        else:
            $ Situation = "skip"
        "[Line]"
        return

label Laura_Three_Change(ActiveGirl = "Rogue", D20S=0, Secondary="Laura", PrimaryLust=0, SecondaryLust=0):
        #this is called when the player wants to change over a threeway behavior.
        # for Threeway secondary activity: Laura_Threeway_Set("preset", 0, Trigger4, "ActiveGirl")        
        menu L_Three_Change:
            ch_p "Hey Laura. . ."
            "about [ActiveGirl]. . .":
                menu:
                    ch_p "about [ActiveGirl]. . ."
                    "why don't you kiss her?" if Trigger5 != "kiss girl" and Trigger5 != "kiss both":
                            call Laura_Threeway_Set("kiss girl", 0, Trigger4, ActiveGirl)                            
                    "why don't you grab her tits?" if Trigger4 != "fondle breasts":
                            call Laura_Threeway_Set("fondle breasts",0, Trigger4, ActiveGirl)                    
                    "why don't you suck her breasts?" if Trigger4 != "suck breasts":
                            call Laura_Threeway_Set("suck breasts",0, Trigger4, ActiveGirl)                            
                    "why don't you finger her?" if Trigger4 != "fondle pussy":
                            call Laura_Threeway_Set("fondle pussy",0, Trigger4, ActiveGirl)                            
                    "why don't you go down on her?" if Trigger4 != "lick pussy":
                            call Laura_Threeway_Set("lick pussy", 0, Trigger4, ActiveGirl)                            
                    "why don't you grab her ass?" if Trigger4 != "fondle ass":
                            call Laura_Threeway_Set("fondle ass", 0, Trigger4, ActiveGirl)                            
                    "why don't you lick her ass?" if Trigger4 != "lick ass":
                            call Laura_Threeway_Set("lick ass", 0, Trigger4, ActiveGirl)
                    "wait, I meant. . .":
                            jump L_Three_Change
                    
            "about me. . .":
                menu:
                    ch_p "about me. . ."
                    "why don't you kiss me?" if Trigger5 != "kiss you" and Trigger5 != "kiss both":
                            call Laura_Threeway_Set("kiss you", 0, Trigger4, ActiveGirl)                            
                    "maybe take me in hand?" if Trigger4 != "hand":
                            call Laura_Threeway_Set("hand", 0, Trigger4, ActiveGirl)                            
                    "maybe give me a lick?" if Trigger4 != "blow":
                            call Laura_Threeway_Set("blow", 0, Trigger4, ActiveGirl)
                    "wait, I meant. . .":
                            jump L_Three_Change
            "never mind.":
                pass
        return

#Start L_Les_Response >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >
label L_Les_Response(Girl="Rogue", Step=1, B=0, B2=0, Tempmod=0, Result=0, Approval = 0):
        #Dialog for responses to Lesbian scenes, Girl is the initial girl in the scene. Step is the phase of the conversation
        # call L_Les_Response("Rogue",1)
        if L_Les:
            $ Tempmod += 10
        if L_SEXP >= 50:
            $ Tempmod += 25
        elif L_SEXP >= 30:
            $ Tempmod += 15
        elif L_SEXP >= 15:
            $ Tempmod += 5
                    
        elif L_Inbt >= 750:
            $ Tempmod += 5
            
        if "exhibitionist" in L_Traits:      
            $ Tempmod += (3*Taboo) 
            
        if "dating" in L_Traits or "sex friend" in L_Petnames:
            $ Tempmod += 10        
        elif "ex" in L_Traits:
            $ Tempmod -= 40  
            
        if Girl == "Rogue":
                #if it's Rogue. . .
                if L_LikeRogue >= 900:
                        $ B += 150
                elif L_LikeRogue >= 800 or "poly Rogue" in L_Traits:
                        $ B += 100
                elif L_LikeRogue >= 700:
                        $ B += 50
                elif L_LikeRogue <= 200:
                        $ B -= 200
                elif L_LikeRogue <= 500:
                        $ B -= 100
        elif Girl == "Emma":
                #if it's Emma. . .
                if L_LikeEmma >= 900:
                        $ B += 150
                elif L_LikeEmma >= 800 or "poly Emma" in L_Traits:
                        $ B += 100
                elif L_LikeEmma >= 700:
                        $ B += 50
                elif L_LikeEmma <= 200:
                        $ B -= 200
                elif L_LikeEmma <= 500:
                        $ B -= 100
        elif Girl == "Kitty":
                #if it's Kitty. . .
                if L_LikeKitty >= 900:
                        $ B += 150
                elif L_LikeKitty >= 800 or "poly Kitty" in L_Traits:
                        $ B += 100
                elif L_LikeKitty >= 700:
                        $ B += 50
                elif L_LikeKitty <= 200:
                        $ B -= 200
                elif L_LikeKitty <= 500:
                        $ B -= 100
                        
        $ Approval = ApprovalCheck("Laura", 1300, TabM = 2, Bonus = B) # 1300, 1450, 1600, Taboo -800
        
        if Step == 1:
            #this is if the first girl's check failed, but Laura likes her.
            if Approval >= 2 or (Approval and B >= 150):
                call LauraFace("sexy", 1)
                ch_l "It's really not bad, give it a shot."
                if B2 >= 100:
                    $ Result = 1
                    if Girl == "Rogue":
                            $ L_LikeRogue += (int(B/10))
                            $ R_LikeLaura += (int(B2/10))
                    elif Girl == "Emma":
                            $ L_LikeEmma += (int(B/10))
                            $ E_LikeLaura += (int(B2/10))
                    elif Girl == "Kitty":
                            $ L_LikeKitty += (int(B/10))
                            $ K_LikeLaura += (int(B2/10))
            else:
                return Result
        
        if Step == 2:
            #this is the second step, usually in the Prep phase
            if Approval >= 2:
                call LauraFace("smile", 1)
                ch_l "I'm in."
                $ Result = 1
            elif Approval:
                call LauraFace("sly", 2)
                if B >= 100:
                        ch_l "You're cute and all. . ."
                if B >= 0:
                        ch_l "I don't know, [Girl]. . ."
                $ L_Blush = 1
                menu:
                    extend ""
                    "Ok, that's fine. . .":
                            if B >= 100:                            
                                ch_l "Oh, no, I'm in."
                                $ Result = 1
                            else:
                                call LauraFace("smile")
                                ch_l "Yeah. . ."
                    "Come on, you might enjoy it. . .":
                            if B >= 50:
                                ch_l "Maybe. .. " 
                                $ Result = 1
                            else:
                                call LauraFace("sad", 2)
                                ch_l "I doubt it." 
                    "Get in there, now.":
                            if ApprovalCheck("Laura", 550, "OI", TabM = 2):
                                call LauraFace("sadside", 1)
                                ch_l "Fine."
                                $ Result = 1
                            else:
                                call LauraFace("angry")
                                ch_l "Don't push me."  
                                $ L_RecentActions.append("angry")
                                $ L_DailyActions.append("angry")
                    "[Girl], what do you think?":
                            if Girl == "Rogue":
                                call RogueFace("sexy", 1)
                                if R_Les and L_Les:
                                        ch_r "Oh, it's not that bad."
                                else:
                                        ch_r "It could be a lot of fun."
                                $ L_LikeRogue += (int(B/10))
                                if B >= 50:
                                        $ R_LikeLaura += 5
                            elif Girl == "Emma":
                                call EmmaFace("sexy", 1)
                                if E_Les and L_Les:
                                        ch_e "What's the matter Laura, too shy around [Playername]?"
                                else:
                                        ch_e "What's the matter Laura, I've seen how you look at me. . ."
                                $ L_LikeEmma += (int(B/10))
                                if B >= 50:
                                        $ E_LikeLaura += 5
                            elif Girl == "Kitty":
                                call KittyFace("sexy", 1)
                                if K_Les and L_Les:
                                        ch_k "We have so much fun together though."
                                else:
                                        ch_k "It could be fun!"
                                $ L_LikeKitty += (int(B/10))
                                if B >= 50:
                                        $ K_LikeLaura += 5
                            if B >= 50:
                                call LauraFace("smile", 1)
                                ch_l "I guess so."
                                $ Result = 1
                            else:
                                call LauraFace("angry", 1, Eyes="side")
                                ch_l "Sorry [Girl], it's not about you."
            if Step == 3:
                    #This is a check if you interrupted them and Primary wants to do it, does Secondary?
                    if Approval:
                            call LauraFace("smile", 1)
                            ch_l "Yeah. . ."
                            $ Result = 1
                    else:
                            call LauraFace("sadside", 1)
                            ch_l "Not right now. . ."
            
            if not Result:      
                #no approval
                $ L_RecentActions.append("no lesbian")                      
                $ L_DailyActions.append("no lesbian") 
                call LauraFace("sadside", 1)
                if B <= 0:
                    ch_l "Sorry, [L_Petname], she's not my type."
                if Taboo > 20:
                    ch_l "Sorry, [L_Petname], this area's a bit exposed."
                if B >= 100:
                    ch_l "Sorry, [L_Petname], I don't want an audience. . ."
                else:
                    ch_l "Sorry, [L_Petname], I'm just not into that."
                
        return Result
#End L_Les_Response >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >


label L_Les_FirstKiss:
    # called when there is a first kiss situation between two girls
    if Partner == "Rogue":
            if "les rogue" in L_History:
                #if they've been together before              
                $ Line = "experienced"
            elif L_Les and R_Les:   
                #if both have kissed girls before
                $ Line = "first both"
            elif L_Les:
                #Laura's had experience              
                $ Line = "first girl"
            elif R_Les:
                #Rogue's had experience                
                $ Line = "first partner"
    elif Partner == "Emma":
            if "les emma" in L_History:
                #if they've been together before              
                $ Line = "experienced"
            elif L_Les and E_Les:   
                #if both have kissed girls before
                $ Line = "first both"
            elif L_Les:
                #Laura's had experience              
                $ Line = "first girl"
            elif E_Les:
                #Emma's had experience                
                $ Line = "first partner"
    elif Partner == "Kitty":
            if "les kitty" in L_History:
                #if they've been together before              
                $ Line = "experienced"
            elif L_Les and K_Les:   
                #if both have kissed girls before
                $ Line = "first both"
            elif L_Les:
                #Laura's had experience              
                $ Line = "first girl"
            elif K_Les:
                #Kitty's had experience                
                $ Line = "first partner"
    
    if Line == "experienced":
            "Laura and [Partner] move together in a passionate kiss."
            "Laura's arms firmly grasp [Partner]'s neck and pull her close."
    else:
            if Line in ("first both", "first girl"):
                # Laura's first time
                "Laura slowly moves in and gives [Partner] a soft kiss."
            else:
                #not Laura's first time
                "Laura casually places a hand on the back of [Partner]'s head and draws their lips together."
            if Line == "first partner":
                #other girl's first time
                "[Partner] pulls back a bit, but slowly leans into the enbrace."
            else:
                #not other girl's first time
                "[Partner]'s lips curl up into a smile and she draws Laura even closer."                    
            "After a few seconds, it begins to grow more passionate."
    return
#End L_Les_Response >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >