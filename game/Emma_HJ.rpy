## E_Handjob //////////////////////////////////////////////////////////////////////
label E_Handjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Emma")
    if E_Hand >= 7: # She loves it
        $ Tempmod += 10
    elif E_Hand >= 3: #You've done it before several times
        $ Tempmod += 7
    elif E_Hand: #You've done it before
        $ Tempmod += 3
        
    if E_Addict >= 75 and E_Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 15
    if E_Addict >= 75:
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 15
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
        
    if "no hand" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no hand" in E_RecentActions else 0    
        
    $ Approval = ApprovalCheck("Emma", 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)
    
    if Situation == "Emma":                                                                  #Emma auto-starts   
        if Approval > 2:                                                      # fix, add emma auto stuff here
            if Trigger2 == "jackin":
                "Emma brushes your hand aside and starts stroking your cock."
            else:
                "Emma draws her fingers across your cock, and begins to stroke it."
            menu:
                "What do you do?"
                "Nothing.":                    
                    call Statup("Emma", "Inbt", 70, 3) 
                    call Statup("Emma", "Inbt", 30, 1)                     
                    "Emma continues her actions."
                "Praise her.":       
                    call EmmaFace("sexy", 1)                    
                    call Statup("Emma", "Inbt", 70, 2) 
                    ch_p "Oooh, that's good, [E_Pet]."
                    call Emma_Namecheck
                    "Emma continues her actions."
                    call Statup("Emma", "Love", 80, 1)
                    call Statup("Emma", "Obed", 90, 1)
                    call Statup("Emma", "Obed", 50, 2)
                "Ask her to stop.":
                    call EmmaFace("surprised")       
                    call Statup("Emma", "Inbt", 70, 1) 
                    ch_p "Let's not do that for now, [E_Pet]."
                    call Emma_Namecheck
                    "Emma puts it down."
                    call Statup("Emma", "Obed", 90, 1)
                    call Statup("Emma", "Obed", 50, 1)
                    call Statup("Emma", "Obed", 30, 2)
                    return            
            if Trigger:
                $ Trigger3 = "hand"
                return
            jump E_HJ_Prep
        else:                
            $ Tempmod = 0                               # fix, add emma auto stuff here
            $ Trigger2 = 0
            return            
    
    if not E_Hand and "no hand" not in E_RecentActions:        
        call EmmaFace("sly", 2)
        ch_e "You'd like me to take care of that for you?"
            
    if not E_Hand and Approval:                                                 #First time dialog        
        if E_Forced: 
            call EmmaFace("sad",1)
            call Statup("Emma", "Love", 70, -3, 1)
            call Statup("Emma", "Love", 20, -2, 1)
        elif E_Love >= (E_Obed + E_Inbt):
            call EmmaFace("sexy",1)
            $ E_Brows = "sad"
            $ E_Mouth = "smile" 
            ch_e "I suppose you've earned something. . ."            
        elif E_Obed >= E_Inbt:
            call EmmaFace("normal",1)
            ch_e "If that's what you'd like, [E_Petname]. . ."            
        elif E_Addict >= 50:
            call EmmaFace("manic", 1)
            ch_e "Mmmmmmmm. . ."  
        else: # Uninhibited 
            call EmmaFace("lipbite",1,Eyes="side")    
            ch_e "I suppose. . ."    
            
    elif Approval:                                                                       #Second time+ dialog
        if E_Forced: 
            call EmmaFace("sad")
            call Statup("Emma", "Love", 70, -3, 1)
            call Statup("Emma", "Love", 20, -2, 1)
            ch_e "No more than that?" 
        elif not Taboo and "tabno" in E_DailyActions:        
            ch_e "Here, hmm?. . ."    
        elif "hand" in E_RecentActions:
            call EmmaFace("sexy", 1)
            ch_e "I will need to grade papers later, you know. . ."
            jump E_HJ_Prep
        elif "hand" in E_DailyActions:
            call EmmaFace("sexy", 1)
            $ Line = renpy.random.choice(["Another?",   
                "You're going to wear out my arm.", 
                "Didn't get enough earlier?",
                "My hand's a bit sore from earlier.",
                "My hand's rather sore from before."]) 
            ch_e "[Line]"
        elif E_Hand < 3:        
            call EmmaFace("sly", 1)
            ch_e "Enjoyed last time?. . ."        
        else:       
            call EmmaFace("sexy", 1)
            $ Emma_Arms = 2
            $ Line = renpy.random.choice(["You want more?",                 
                "So you'd like another?",                 
                "More of this? [fist pumping hand gestures]", 
                "Oh, did you want some attention?"]) 
            ch_e "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if E_Forced:
            call EmmaFace("sad")
            call Statup("Emma", "Obed", 90, 1)
            call Statup("Emma", "Inbt", 60, 1)
            ch_e "Very well." 
        elif "no hand" in E_DailyActions:               
            ch_e "Oh, fine!"   
        else:
            call EmmaFace("sexy", 1)
            call Statup("Emma", "Love", 90, 1)
            call Statup("Emma", "Inbt", 50, 3) 
            $ Line = renpy.random.choice(["Oh, I suppose.",                 
                "I'll do it.",                 
                "Well, give it here.", 
                "I suppose I could. . .",
                "Fine. . . [She gestures for you to come over].",
                "Ok, ok."]) 
            ch_e "[Line]"
            $ Line = 0
        call Statup("Emma", "Obed", 20, 1)
        call Statup("Emma", "Obed", 60, 1)
        call Statup("Emma", "Inbt", 70, 2) 
        jump E_HJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call EmmaFace("angry")
        if "no hand" in E_RecentActions:  
            ch_e "You need to learn to take\"no\" for an answer, [E_Petname]."
        elif "no hand" in E_DailyActions:       
            ch_e "I told you \"no,\" [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "I told you, this is too public!"     
        elif not E_Hand:
            call EmmaFace("bemused")
            ch_e "Are you sure though, [E_Petname]?. . ."
        else:
            call EmmaFace("bemused")
            ch_e "I'd rather not right now though."
        menu:
            extend ""
            "Sorry, never mind." if "no hand" in E_DailyActions:
                call EmmaFace("bemused")
                ch_e "Quite alright."              
                return
            "Maybe later?" if "no hand" not in E_DailyActions:
                call EmmaFace("sexy")  
                ch_e ". . ."
                ch_e "I couldn't rule it out. . ."
                call Statup("Emma", "Love", 80, 2)
                call Statup("Emma", "Inbt", 70, 2)   
                if Taboo:                    
                    $ E_RecentActions.append("tabno")                      
                    $ E_DailyActions.append("tabno") 
                $ E_RecentActions.append("no hand")                      
                $ E_DailyActions.append("no hand")            
                return
            "I'd really appreciate it. . .":             
                if Approval:
                    call EmmaFace("sexy")     
                    call Statup("Emma", "Obed", 90, 2)
                    call Statup("Emma", "Obed", 50, 2)
                    call Statup("Emma", "Inbt", 70, 3) 
                    call Statup("Emma", "Inbt", 40, 2) 
                    $ Line = renpy.random.choice(["Oh, I suppose.",                 
                        "I'll do it.",                 
                        "Well, give it here.", 
                        "I suppose I could. . .",
                        "Fine. . . [She gestures for you to come over].",
                        "Ok, ok."]) 
                    ch_e "[Line]"
                    $ Line = 0                   
                    jump E_HJ_Prep
                    
            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Emma", 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("angry")
                    call Statup("Emma", "Love", 70, -5, 1)
                    call Statup("Emma", "Love", 200, -2)                 
                    ch_e "Hm. Alright, but don't push your luck, [E_Petname]."  
                    call Statup("Emma", "Obed", 50, 4)
                    call Statup("Emma", "Inbt", 80, 1) 
                    call Statup("Emma", "Inbt", 60, 3)  
                    $ E_Forced = 1  
                    jump E_HJ_Prep
                else:                              
                    call Statup("Emma", "Love", 200, -15)     
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Emma_Arms = 1 
    if "no hand" in E_DailyActions:
        call EmmaFace("angry", 1)
        ch_e "Don't make me repeat myself."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1)
        ch_e "Even that is asking too much."
        call Statup("Emma", "Lust", 200, 5)   
        if E_Love > 300:    
                call Statup("Emma", "Love", 70, -2)
        call Statup("Emma", "Obed", 50, -2)    
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call EmmaFace("angry", 1)          
        $ E_DailyActions.append("tabno") 
        ch_e "I couldn't possibly do that. . . here!"
        call Statup("Emma", "Lust", 200, 5)  
        call Statup("Emma", "Obed", 50, -3)   
    elif E_Hand:
        call EmmaFace("sad") 
        ch_e "I'd really rather not. . ."       
    else:
        call EmmaFace("normal", 1)
        ch_e "No, I don't think so, [E_Petname]."  
    $ E_RecentActions.append("no hand")                      
    $ E_DailyActions.append("no hand") 
    $ Tempmod = 0    
    return
    

label E_HJ_Prep:
    if Trigger2 == "hand": 
        return
    
    if Taboo:
        $ E_Inbt += int(Taboo/10)  
        $ E_Lust += int(Taboo/5)
                
    call EmmaFace("sexy")
    if E_Forced:
        call EmmaFace("sad")
    elif E_Hand:
        $ E_Brows = "confused"
        $ E_Eyes = "sexy"
        $ E_Mouth = "smile"
        
    call Seen_First_Peen("Emma",Partner)
    call Emma_HJ_Launch("L")
    if not E_Hand:        
        if E_Forced:
            call Statup("Emma", "Love", 90, -20)
            call Statup("Emma", "Obed", 70, 25)
            call Statup("Emma", "Inbt", 80, 30) 
        else:
            call Statup("Emma", "Love", 90, 5)
            call Statup("Emma", "Obed", 70, 20)
            call Statup("Emma", "Inbt", 80, 20)     
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no hand")
    $ E_RecentActions.append("hand")                      
    $ E_DailyActions.append("hand") 
  
label E_HJ_Cycle:    
    while Round >=0:  
        call Shift_Focus("Emma") 
        call Emma_HJ_Launch    
        call EmmaLust   
        
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
                                            if E_Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ E_Action -= 1
                                            else:
                                                ch_e "Hmm, I think we've probably done enough for now. . ."  
                                         
                                    "Shift primary action":
                                            if E_Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    if E_Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call E_HJ_After                
                                                                        call E_Blowjob
                                                                    else:
                                                                        ch_e "Hmm, I think we've probably done enough for now. . ."
                                                                        
                                                        "How about a titjob?":
                                                                    if E_Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call E_HJ_After
                                                                        call E_Titjob
                                                                    else:
                                                                        ch_e "Hmm, I think we've probably done enough for now. . ."
                                                        "Never Mind":
                                                                jump E_HJ_Cycle
                                            else: 
                                                ch_e "Hmm, I think we've probably done enough for now. . ."           
                    
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
                                                        jump E_HJ_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump E_HJ_Cycle 
                                            "Never mind":
                                                        jump E_HJ_Cycle 
                                    "Undress Emma":
                                            call E_Undress   
                                    "Clean up Emma (locked)" if not E_Spunk:
                                            pass  
                                    "Clean up Emma" if E_Spunk:
                                            call Emma_Cleanup("ask")                                         
                                    "Never mind":
                                            jump E_HJ_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Emma_HJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_HJ_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Emma_HJ_Reset
                                    $ Line = 0
                                    jump E_HJ_After
        #End menu (if Line)
        
        call Shift_Focus("Emma")    
        call Sex_Dialog("Emma",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or E_Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PE_Cumming
                            if "angry" in E_RecentActions:  
                                call Emma_HJ_Reset
                                return    
                            call Statup("Emma", "Lust", 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_HJ_After 
                            $ Line = "came"
     
                    if E_Lust >= 100:  
                            #If Emma can cum                                             
                            call E_Cumming
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_HJ_After
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in E_RecentActions:#And Emma is unsatisfied,  
                                    "Emma still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it" 
                                        "No, I'm done.":
                                            "You pull back."
                                            jump E_HJ_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Emma")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if Cnt == 20:
                    $ E_Brows = "angry"    
                    ch_e "Hmm, I'm getting a bit of a cramp here."    
                    menu:
                        ch_e "Mind if we take a break?"
                        "How about a BJ?" if E_Action and MultiAction:
                                $ Situation = "shift"
                                call E_HJ_After
                                call E_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump E_HJ_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Emma_HJ_Reset
                                $ Situation = "shift"
                                jump E_HJ_After
                        "No, get back down there.":
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):
                                    call Statup("Emma", "Love", 200, -5)
                                    call Statup("Emma", "Obed", 50, 3)                    
                                    call Statup("Emma", "Obed", 80, 2)
                                    "She scowls but gets back to work."
                                else:
                                    call EmmaFace("angry", 1)   
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_e "You know, I do have better things to do with my time than this."                                               
                                    call Statup("Emma", "Love", 50, -3, 1)
                                    call Statup("Emma", "Love", 80, -4, 1)
                                    call Statup("Emma", "Obed", 30, -1, 1)                    
                                    call Statup("Emma", "Obed", 50, -1, 1)                     
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_HJ_After
        elif Cnt == 10 and E_SEXP <= 100 and not ApprovalCheck("Emma", 1200, "LO"):
                    $ E_Brows = "confused"
                    ch_e "Are you certain you didn't have anything else in mind?"         
        #End Count check
                   
        if Round == 10:
            ch_e "It's about time for a break."     
        elif Round == 5:
            ch_e "Ok, that's enough, for now. . ."    
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    ch_e "Ok, seriously, I'm putting it down for a minute."
    
label E_HJ_After:
    call EmmaFace("sexy") 
    
    $ E_Hand += 1  
    $ E_Action -=1
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1        
    call Statup("Emma", "Lust", 90, 5)
    
    call Partner_Like("Emma",1)
                    
    if "Emma Handi-Queen" in Achievements:
            pass  
    elif E_Hand >= 10:
            call EmmaFace("smile", 1)
            ch_e "I've apparently become the \"queen\" of handjobs as well."
            $ Achievements.append("Emma Handi-Queen")
            $E_SEXP += 5          
    elif E_Hand == 1:            
            $E_SEXP += 10
            if not E_Forced:
                $ E_Mouth = "smile"
                ch_e "What a lovely experience. . ."
            elif P_Focus <= 20:
                $ E_Mouth = "sad"
                ch_e "Was that sufficient?"
    elif E_Hand == 5:
                ch_e "Please do call again. . ."                  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Very well, what did you want to do?"
    else:
        call Emma_HJ_Reset    
    call Checkout
    return

## end E_Handjob //////////////////////////////////////////////////////////////////////




## E_Titjob //////////////////////////////////////////////////////////////////////
label E_Titjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Emma")
    if E_Tit >= 7: # She loves it
        $ Tempmod += 10
    elif E_Tit >= 3: #You've done it before several times
        $ Tempmod += 7
    elif E_Tit: #You've done it before
        $ Tempmod += 5
    
    if E_Addict >= 75 and E_Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 15
    elif E_Addict >= 75:
        $ Tempmod += 5
        
    if E_SeenChest and ApprovalCheck("Emma", 500): # You've seen her tits.
        $ Tempmod += 10    
    if not E_Chest and not E_Over: #She's already topless
        $ Tempmod += 10
    if E_Lust > 75: #She's really horny
        $ Tempmod += 10
    if Situation == "shift":
        $ Tempmod += 15
    if "exhibitionist" in E_Traits:
        $ Tempmod += (5*Taboo)
    if "dating" in E_Traits or "sex friend" in E_Petnames:
        $ Tempmod += 10
    elif "ex" in E_Traits:
        $ Tempmod -= 30 
    if E_ForcedCount and not E_Forced:
        $ Tempmod -= 5 * E_ForcedCount    
    
    if Taboo and "tabno" in E_DailyActions:        
        $ Tempmod -= 10 
        
    if "no titjob" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no titjob" in E_RecentActions else 0    
        
    $ Approval = ApprovalCheck("Emma", 1200, TabM = 5) # 120, 135, 150, Taboo -200(320)
    
    if Situation == "Emma":                                                                  #Emma auto-starts   
        if Approval > 2:                                                      # fix, add emma auto stuff here
            call Emma_TJ_Launch  
            $ Speed = 0
            "Emma slides down and sandwiches your dick between her tits."
            menu:
                "What do you do?"
                "Nothing.":                    
                    call Statup("Emma", "Inbt", 80, 3) 
                    call Statup("Emma", "Inbt", 40, 2)                     
                    "Emma starts to slide them up and down."
                "Praise her.":       
                    call EmmaFace("sexy", 1)                    
                    call Statup("Emma", "Inbt", 80, 3) 
                    ch_p "Oh, that sounds like a good idea, [E_Pet]."
                    call Emma_Namecheck
                    "Emma continues her actions."
                    call Statup("Emma", "Love", 85, 1)
                    call Statup("Emma", "Obed", 90, 1)
                    call Statup("Emma", "Obed", 50, 2)
                "Ask her to stop.":     
                    call EmmaFace("confused")  
                    call Statup("Emma", "Inbt", 70, 1) 
                    ch_p "Let's not do that for now, [E_Pet]."
                    call Emma_Namecheck
                    "Emma lets it drop out from between her breasts."
                    call Statup("Emma", "Obed", 90, 1)
                    call Statup("Emma", "Obed", 50, 3)
                    call Emma_TJ_Reset  
                    return            
            jump E_TJ_Cycle
        else:                
            $ Tempmod = 0                               # fix, add emma auto stuff here
            $ Trigger2 = 0
            return            
    
    if not E_Tit and "no titjob" not in E_RecentActions:        
        call EmmaFace("surprised", 1)
        $ E_Mouth = "kiss"
        ch_e "Hmm, are you sure you can handle that, [E_Petname]?"       
            
    if not E_Tit and Approval:                                                
        #First time dialog    
        if E_Forced: 
            call EmmaFace("sad")
            call Statup("Emma", "Love", 70, -3, 1)
            call Statup("Emma", "Love", 20, -2, 1)
        elif E_Love >= (E_Obed + E_Inbt):
            call EmmaFace("sexy")
            $ E_Brows = "sad"
            $ E_Mouth = "smile" 
            ch_e "I suppose you've earned something special. . ."            
        elif E_Obed >= E_Inbt:
            call EmmaFace("normal")
            ch_e "If that's what you want. . ."              
        elif E_Addict >= 50:
            call EmmaFace("manic", 1)
            ch_e "Hmmmm. . . ."     
        else: # Uninhibited 
            call EmmaFace("sad")
            $ E_Mouth = "smile"             
            ch_e "Hmm, I was wondering when you'd ask. . ."   
            
    elif Approval:                                                                       
        #Second time+ dialog
        if E_Forced: 
            call EmmaFace("sad")
            call Statup("Emma", "Love", 70, -3, 1)
            call Statup("Emma", "Love", 20, -2, 1)
            ch_e "You aren't getting used to this service, are you?"
        elif not Taboo and "tabno" in E_DailyActions:        
            ch_e "I suppose this is secluded enough. . ."   
        elif "titjob" in E_RecentActions:
            call EmmaFace("sexy", 1)
            ch_e "Oh! Back for more?"
            jump E_TJ_Prep
        elif "titjob" in E_DailyActions:
            call EmmaFace("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",   
                "You're going to wear them out.", 
                "Didn't get enough earlier?",
                "I'm still a bit sore from earlier."]) 
            ch_e "[Line]"
        elif E_Tit < 3:        
            call EmmaFace("sly", 1)
            ch_e "Hmm, another titjob?"        
        else:       
            call EmmaFace("sexy", 1)
            $ Emma_Arms = 2
            $ Line = renpy.random.choice(["You want some of these? [jiggles her tits]",                 
                "So you'd like another titjob?",                 
                "A little. . . [bounces tits]?", 
                "A little warm embrace?"]) 
            ch_e "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if E_Forced:
            call EmmaFace("sad")
            call Statup("Emma", "Obed", 90, 1)
            call Statup("Emma", "Inbt", 60, 1)
            ch_e "I suppose there are worst ways to get you off. . ." 
        elif "no titjob" in E_DailyActions:               
            ch_e "Oh, very well then. . ."       
        else:
            call EmmaFace("sexy", 1)
            call Statup("Emma", "Love", 90, 1)
            call Statup("Emma", "Inbt", 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, come over here.",                 
                "Oh, very well.",                 
                "Mmmmm.", 
                "Fine, whip it out.",
                "Fine. . . [She drools a bit into her cleavage].",
                "Oh, all right."]) 
            ch_e "[Line]"
            $ Line = 0
        call Statup("Emma", "Obed", 20, 1) 
        call Statup("Emma", "Obed", 70, 1)      
        call Statup("Emma", "Inbt", 80, 2) 
        jump E_TJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call EmmaFace("angry")
        if "no titjob" in E_RecentActions:  
            ch_e "I {i}just{/i} refused, [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no titjob" in E_DailyActions:  
            ch_e "This is not an appropriate location for that. !"     
        elif "no titjob" in E_DailyActions:       
            ch_e "I already refused, [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "This is not an appropriate place for that."     
        elif not E_Tit:
            call EmmaFace("bemused")
            ch_e "I don't know that you're ready for that, [E_Petname]. . ."
        else:
            call EmmaFace("bemused")
            ch_e "Perhaps later, [E_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no titjob" in E_DailyActions:
                call EmmaFace("bemused")
                ch_e "That's all right, [E_Petname]."              
                return
            "Maybe later?" if "no titjob" not in E_DailyActions:
                call EmmaFace("sexy")  
                ch_e "Perhaps."
                call Statup("Emma", "Love", 80, 2)
                call Statup("Emma", "Inbt", 70, 2)   
                if Taboo:                    
                    $ E_RecentActions.append("tabno")                      
                    $ E_DailyActions.append("tabno") 
                $ E_RecentActions.append("no titjob")                      
                $ E_DailyActions.append("no titjob")            
                return
            "I think this could be fun for both of us. . .":             
                if Approval:
                    call EmmaFace("sexy")     
                    call Statup("Emma", "Obed", 80, 2)
                    call Statup("Emma", "Obed", 40, 2)
                    call Statup("Emma", "Inbt", 70, 3) 
                    call Statup("Emma", "Inbt", 40, 2) 
                    $ Line = renpy.random.choice(["Well, sure, come over here.",                 
                            "Oh, very well.",                 
                            "Mmmmm.", 
                            "Fine, whip it out.",
                            "Fine. . . [She drools a bit into her cleavage].",
                            "Oh, all right."]) 
                    ch_e "[Line]"
                    $ Line = 0                   
                    jump E_TJ_Prep
                else:   
                    $ Approval = ApprovalCheck("Emma", 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)             Handy instead?
                    if Approval >= 2:       
                        call Statup("Emma", "Inbt", 80, 1) 
                        call Statup("Emma", "Inbt", 60, 3) 
                        call EmmaFace("confused", 1)
                        if E_Blow:
                            ch_e "You seemed to enjoy blowjobs, would that work instead?"
                        else:
                            ch_e "Would you perhaps prefer a blowjob?"
                        menu:
                            extend ""
                            "Ok, get down there.":
                                call Statup("Emma", "Love", 80, 2)  
                                call Statup("Emma", "Inbt", 60, 1)                                
                                call Statup("Emma", "Obed", 50, 1) 
                                jump E_BJ_Prep
                            "Nah, it's all about dem titties.":  
                                $ Line = "no BJ"
                    if Approval:       
                        call Statup("Emma", "Inbt", 80, 1) 
                        call Statup("Emma", "Inbt", 60, 3) 
                        call EmmaFace("confused", 1)
                        ch_e "Perhaps a handjob?"
                        menu:
                            ch_e "Perhaps a handjob?"
                            "Sure, that's fine.":
                                call Statup("Emma", "Love", 80, 2)  
                                call Statup("Emma", "Inbt", 60, 1)                                
                                call Statup("Emma", "Obed", 50, 1) 
                                jump E_HJ_Prep
                            "Seriously, titties." if Line == "no BJ":  
                                $ Line = 0
                            "Nah, it's all about dem titties." if Line != "no BJ":  
                                pass
                    call Statup("Emma", "Love", 200, -2)                 
                    ch_e "Your loss."  
                    call Statup("Emma", "Obed", 70, 2) 
                    
                    
            "Come on, let me fuck those titties, [E_Pet]":                                               # Pressured into it                
                call Emma_Namecheck
                $ Approval = ApprovalCheck("Emma", 700, "OI", TabM = 4) # 70, 85, 100, -160(230)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad")
                    call Statup("Emma", "Love", 70, -5, 1)
                    call Statup("Emma", "Love", 200, -2)                 
                    ch_e "Oh, very well."  
                    call Statup("Emma", "Obed", 50, 4)
                    call Statup("Emma", "Inbt", 80, 1) 
                    call Statup("Emma", "Inbt", 60, 3)  
                    $ E_Forced = 1
                    jump E_TJ_Prep
                else:                              
                    call Statup("Emma", "Love", 200, -15)     
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
    
    #She refused all offers.   
    if "no titjob" in E_DailyActions:
        call EmmaFace("angry", 1)
        ch_e "I've refused, end of story."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1)
        ch_e "I couldn't put you through that."
        call Statup("Emma", "Lust", 200, 5)  
        if E_Love > 300:       
                call Statup("Emma", "Love", 70, -2)
        call Statup("Emma", "Obed", 50, -2)      
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call EmmaFace("angry", 1)          
        $ E_DailyActions.append("tabno") 
        ch_e "Can you imagine the scandal? Here?"
        call Statup("Emma", "Lust", 200, 5)  
        call Statup("Emma", "Obed", 50, -3)  
    elif E_Tit:
        call EmmaFace("sad") 
        ch_e "I'm afraid you'll just have to remember the last time."       
    else:
        call EmmaFace("normal", 1)
        ch_e "How about let's not, [E_Petname]."
    $ E_RecentActions.append("no titjob")                      
    $ E_DailyActions.append("no titjob") 
    $ Tempmod = 0    
    return
    
label E_TJ_Prep:
      
    if Taboo:
        $ E_Inbt += int(Taboo/10)  
        $ E_Lust += int(Taboo/5)

        
    call EmmaFace("sexy")
    if E_Forced:
        call EmmaFace("sad")
    elif E_Tit:
        $ E_Brows = "confused"
        $ E_Eyes = "sexy"
        $ E_Mouth = "smile"
    
    call Seen_First_Peen("Emma",Partner)
    call Emma_TJ_Launch("L")    
    if not E_Tit:        
        if E_Forced:
            call Statup("Emma", "Love", 90, -25)
            call Statup("Emma", "Obed", 70, 30)
            call Statup("Emma", "Inbt", 80, 35) 
        else:
            call Statup("Emma", "Love", 90, 5)
            call Statup("Emma", "Obed", 70, 25)
            call Statup("Emma", "Inbt", 80, 30)   
            
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0  
    if Taboo:
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no titjob")
    $ E_RecentActions.append("titjob")                      
    $ E_DailyActions.append("titjob") 


label E_TJ_Cycle: #Repeating strokes    
    while Round >=0:  
        call Shift_Focus("Emma") 
        call Emma_TJ_Launch    
        call EmmaLust   
        
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
                                            if E_Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ E_Action -= 1
                                            else:
                                                ch_e "Actually, could we wrap this up soon?" 
                                         
                                    "Shift primary action":
                                            if E_Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                if E_Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call E_TJ_After                
                                                                    call E_Blowjob
                                                                else:
                                                                    ch_e "Actually, could we wrap this up soon?"
                                                                    
                                                        "How about a handy?":
                                                                if E_Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call E_BJ_After
                                                                    call E_Handjob
                                                                else:
                                                                    ch_e "Actually, could we wrap this up soon?"                                                            
                                                        "Never Mind":
                                                                jump E_TJ_Cycle
                                            else: 
                                                ch_e "Actually, could we wrap this up soon?"          
                    
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
                                                        jump E_TJ_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump E_TJ_Cycle 
                                            "Never mind":
                                                        jump E_TJ_Cycle 
                                    "Undress Emma":
                                            call E_Undress   
                                    "Clean up Emma (locked)" if not E_Spunk:
                                            pass  
                                    "Clean up Emma" if E_Spunk:
                                            call Emma_Cleanup("ask")                                         
                                    "Never mind":
                                            jump E_TJ_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Emma_TJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_TJ_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Emma_TJ_Reset
                                    $ Line = 0
                                    jump E_TJ_After
        #End menu (if Line)
        
        call Shift_Focus("Emma")    
        call Sex_Dialog("Emma",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or E_Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PE_Cumming
                            if "angry" in E_RecentActions:  
                                call Emma_TJ_Reset
                                return    
                            call Statup("Emma", "Lust", 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_TJ_After 
                            $ Line = "came"
     
                    if E_Lust >= 100:  
                            #If Emma can cum                                             
                            call E_Cumming
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_TJ_After
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in E_RecentActions:#And Emma is unsatisfied,  
                                "Emma still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump E_TJ_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Emma")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
        elif Cnt == (5 + E_Tit):
                    $ E_Brows = "confused"
                    ch_e "Are you getting close here? I'm getting a bit sore."   
        elif Cnt == (10 + E_Tit):
                    $ E_Brows = "angry"        
                    menu:
                        ch_e "I'm getting a bit worn out, could we settle this some other way?"
                        "How about a BJ?" if E_Action and MultiAction:
                                $ Situation = "shift"
                                call E_TJ_After
                                call E_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                jump E_TJ_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Emma_TJ_Reset
                                $ Situation = "shift"
                                jump E_TJ_After
                        "No, get back down there.":                                
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    call Statup("Emma", "Love", 200, -5)
                                    call Statup("Emma", "Obed", 50, 3)                    
                                    call Statup("Emma", "Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    call EmmaFace("angry", 1)   
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_e "Then I suppose you can handle this yourself."                         
                                    call Statup("Emma", "Love", 50, -3, 1)
                                    call Statup("Emma", "Love", 80, -4, 1)
                                    call Statup("Emma", "Obed", 30, -1, 1)                    
                                    call Statup("Emma", "Obed", 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_TJ_After
        #End Count check
           
        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    ch_e "All right, [E_Petname], that's plenty for now."
        
label E_TJ_After:
    call EmmaFace("sexy") 
    
    $ E_Tit += 1
    $ E_Action -=1
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1
        
    if Partner == "Kitty":
        call Partner_Like("Emma",4,2)
    else:
        call Partner_Like("Emma",3)
        
    if E_Tit > 5:
            pass
    elif E_Tit == 1:
        $E_SEXP += 12
        if E_Love >= 500:
            $ E_Mouth = "smile"
            ch_e "Mmm, was that as good for you as it was for me?"
        elif P_Focus <= 20:
            $ E_Mouth = "sad"
            ch_e "I hope that lived up to expectations."        
    elif E_Tit == 5:
            ch_e "You certainly get a lot of milage out of these."   
    
    
    $ Tempmod = 0 
    if Situation == "shift":
            ch_e "Mmm, so what else did you have in mind?"
    else:
            call Emma_TJ_Reset    
    call Checkout
    return

## end E_Titjob //////////////////////////////////////////////////////////////////////


# E_Blowjob //////////////////////////////////////////////////////////////////////

label E_Blowjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Emma")
    if E_Blow >= 7: # She loves it
        $ Tempmod += 15  
    elif E_Blow >= 3: #You've done it before several times
        $ Tempmod += 10
    elif E_Blow: #You've done it before
        $ Tempmod += 7    
        
    if E_Addict >= 75 and E_Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 25
    elif E_Addict >= 75: #She's really strung out
        $ Tempmod += 15
        
    if Situation == "shift":
        $ Tempmod += 15
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
        
    if "no blow" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no blow" in E_RecentActions else 0    
    
    $ Approval = ApprovalCheck("Emma", 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)
    
    if Situation == "Emma":                                                                  #Emma auto-starts   
        if Approval > 2:                                                      # fix, add emma auto stuff here
            "Emma slides down and places your cock against her lips."
            menu:
                "What do you do?"
                "Nothing.":                    
                    call Statup("Emma", "Inbt", 80, 3) 
                    call Statup("Emma", "Inbt", 40, 2)                     
                    "Emma starts to lick it."
                "Praise her.":       
                    call EmmaFace("sexy", 1)                    
                    call Statup("Emma", "Inbt", 80, 3) 
                    ch_p "Hmmm, keep doing that, [E_Pet]."
                    call Emma_Namecheck
                    "Emma continues her actions."
                    call Statup("Emma", "Love", 85, 1)
                    call Statup("Emma", "Obed", 90, 1)
                    call Statup("Emma", "Obed", 50, 2)
                "Ask her to stop.":     
                    call EmmaFace("surprised")  
                    call Statup("Emma", "Inbt", 70, 1) 
                    ch_p "Let's not do that for now, [E_Pet]."
                    call Emma_Namecheck
                    "Emma puts it down."
                    call Statup("Emma", "Obed", 90, 1)
                    call Statup("Emma", "Obed", 50, 3)
                    return            
            jump E_BJ_Prep
        else:                
            $ Tempmod = 0                               # fix, add emma auto stuff here
            $ Trigger2 = 0
            return            
    
    if not E_Blow and "no blow" not in E_RecentActions:        
        call EmmaFace("sly")
        ch_e "So you'd like me to suck you off?"
            
    if not E_Blow and Approval:                                                 #First time dialog        
        if E_Forced: 
            call EmmaFace("sad")
            call Statup("Emma", "Love", 70, -3, 1)
            call Statup("Emma", "Love", 20, -2, 1)
        elif E_Love >= (E_Obed + E_Inbt):
            call EmmaFace("sexy")
            $ E_Brows = "sad"
            $ E_Mouth = "smile" 
            ch_e "I am curious if it tastes as good as it looks. . ."            
        elif E_Obed >= E_Inbt:
            call EmmaFace("normal")
            ch_e "If that's what you want. . ."               
        elif E_Addict >= 50:
            call EmmaFace("manic", 1)
            ch_e "I don't know if I could wait. . ."   
        else: # Uninhibited 
            call EmmaFace("sad")
            $ E_Mouth = "smile"             
            ch_e "I suppose. . ."       
    elif Approval:                                                                       #Second time+ dialog
        if E_Forced: 
            call EmmaFace("sad")
            call Statup("Emma", "Love", 70, -3, 1)
            call Statup("Emma", "Love", 20, -2, 1)
            ch_e "Ugh, that again?"
        elif not Taboo and "tabno" in E_DailyActions:        
            ch_e "Ok, I suppose this is secluded enough. . ."    
        elif "blow" in E_RecentActions:
            call EmmaFace("sexy", 1)
            ch_e "Mmm, again? [[yawns]"
            jump E_BJ_Prep                
        elif "blow" in E_DailyActions:
            call EmmaFace("sexy", 1)
            $ Line = renpy.random.choice(["Back so soon?",   
                "Let me get some saliva going.",
                "Didn't get enough earlier?",
                "My jaw's still sore from our prior engagement.",
                "My jaw's still a bit sore from earlier."]) 
            ch_e "[Line]"
        elif E_Blow < 3:        
            call EmmaFace("sexy", 1)
            $ E_Brows = "confused"
            $ E_Mouth = "kiss"
            ch_e "Another blowjob?"        
        else:       
            call EmmaFace("sexy", 1)
            $ Emma_Arms = 2
            $ Line = renpy.random.choice(["You want me to [mimes blowing]?",                 
                "So you want another blowjob?", 
                "You want me to suck you off?",
                "Are you asking if I'm hungry?"]) 
            ch_e "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if E_Forced:
            call EmmaFace("sad")
            call Statup("Emma", "Obed", 90, 1)
            call Statup("Emma", "Inbt", 60, 1)
            ch_e "Fine."    
        elif "no blow" in E_DailyActions:               
            ch_e "Fine, I suppose you've earned it. . ."  
        else:
            call EmmaFace("sexy", 1)
            call Statup("Emma", "Love", 90, 1)
            call Statup("Emma", "Inbt", 50, 3) 
            $ Line = renpy.random.choice(["Well, ok.",                 
                "Well. . . ok.",                 
                "Mmmm.", 
                "Sure, let me have it.",
                "Mmmm. . . [She licks her lips].",
                "Ok, fine."]) 
            ch_e "[Line]"
            $ Line = 0
        call Statup("Emma", "Obed", 20, 1) 
        call Statup("Emma", "Obed", 70, 1)      
        call Statup("Emma", "Inbt", 80, 2) 
        jump E_BJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call EmmaFace("angry")
        if "no blow" in E_RecentActions:  
            ch_e "I believe I just told you, \"no.\""
        elif Taboo and "tabno" in E_DailyActions and "no blow" in E_DailyActions:  
            ch_e "I told you, this is too public!"  
        elif "no blow" in E_DailyActions:       
            ch_e "I told you \"no,\" [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "I told you this is too public!"      
        elif not E_Blow:
            call EmmaFace("bemused")
            ch_e "I'm not sure you're up to my usual tastes, [E_Petname]. . ."
        else:
            call EmmaFace("bemused")
            ch_e "Perhaps later, [E_Petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no blow" in E_DailyActions:
                call EmmaFace("bemused")
                ch_e "No harm done, [E_Petname]."              
                return
            "Maybe later?" if "no blow" not in E_DailyActions:
                call EmmaFace("sexy")  
                ch_e "I wouldn't rule it out, [E_Petname]."
                call Statup("Emma", "Love", 80, 2)
                call Statup("Emma", "Inbt", 70, 2)   
                if Taboo:                    
                    $ E_RecentActions.append("tabno")                      
                    $ E_DailyActions.append("tabno") 
                $ E_RecentActions.append("no blow")                      
                $ E_DailyActions.append("no blow")            
                return
            "Come on, please?":             
                if Approval:
                    call EmmaFace("sexy")     
                    call Statup("Emma", "Obed", 90, 2)
                    call Statup("Emma", "Obed", 50, 2)
                    call Statup("Emma", "Inbt", 70, 3) 
                    call Statup("Emma", "Inbt", 40, 2) 
                    $ Line = renpy.random.choice(["Well, I suppose.",                 
                        "Well. . . ok.",                 
                        "I could perhaps give it a try.", 
                        "I suppose I could. . .",
                        "Fine. . . [She licks her lips].",
                        "Hmph, ok, fine."]) 
                    ch_e "[Line]"
                    $ Line = 0                   
                    jump E_BJ_Prep
                else:   
                    if ApprovalCheck("Emma", 1100, TabM = 3): # 110, 125, 140, Taboo -120(230)             Handy instead?    
                        call Statup("Emma", "Inbt", 80, 1) 
                        call Statup("Emma", "Inbt", 60, 3) 
                        call EmmaFace("confused", 1)
                        $ Emma_Arms = 2
                        if E_Hand:
                            ch_e "I could just stroke you off, perhaps?"
                        else:
                            ch_e "Would my hand be an adequate substitue?"
                        menu:
                            extend ""
                            "Sure, that's fine.":
                                call Statup("Emma", "Love", 80, 2)  
                                call Statup("Emma", "Inbt", 60, 1)                                
                                call Statup("Emma", "Obed", 50, 1) 
                                jump E_HJ_Prep
                            "Nah, if it's not your mouth, forget it.":
                                call Statup("Emma", "Love", 200, -2)                                
                                $ Emma_Arms = 1                
                                ch_e "Pitty."  
                                call Statup("Emma", "Obed", 70, 2)  
                    
                    
            "Suck it, [E_Pet]":                                               # Pressured into it                
                call Emma_Namecheck
                $ Approval = ApprovalCheck("Emma", 750, "OI", TabM = 3) # 75, 90, 105, -120(195)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad")
                    call Statup("Emma", "Love", 70, -5, 1)
                    call Statup("Emma", "Love", 200, -2)                 
                    ch_e "Oh, fine. . ."  
                    call Statup("Emma", "Obed", 50, 4)
                    call Statup("Emma", "Inbt", 80, 1) 
                    call Statup("Emma", "Inbt", 60, 3)  
                    $ E_Forced = 1
                    jump E_BJ_Prep
                else:                              
                    call Statup("Emma", "Love", 200, -15)     
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
    
    #She refused all offers.   
    if "no blow" in E_DailyActions:
        call EmmaFace("angry", 1)
        ch_e "Then I hope you can take care of yourself."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1)
        ch_e "You go too far!"
        call Statup("Emma", "Lust", 200, 5)  
        if E_Love > 300:      
                call Statup("Emma", "Love", 70, -2)
        call Statup("Emma", "Obed", 50, -2)      
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
        $ E_RecentActions.append("no blow")                      
        $ E_DailyActions.append("no blow") 
        return
    elif Taboo:                             # she refuses and this is too public a place for her
        call EmmaFace("angry", 1)          
        $ E_DailyActions.append("tabno") 
        ch_e "This is way too exposed!"
        call Statup("Emma", "Lust", 200, 5)  
        call Statup("Emma", "Obed", 50, -3)    
        return                
    elif E_Blow:
        call EmmaFace("sad") 
        ch_e "I'm just not in the mood, [E_Petname]."       
    else:
        call EmmaFace("normal", 1)
        ch_e "I don't think I will."  
    $ E_RecentActions.append("no blow")                      
    $ E_DailyActions.append("no blow") 
    $ Tempmod = 0    
    return
    

label E_BJ_Prep:   
    if renpy.showing("Emma_HJ_Animation"):
        hide Emma_HJ_Animation with easeoutbottom
    if Taboo:
        $ E_Inbt += int(Taboo/10)  
        $ E_Lust += int(Taboo/5)
                
    call EmmaFace("sexy")
    if E_Forced:
        call EmmaFace("sad")
    
    call Seen_First_Peen("Emma",Partner)
    call Emma_BJ_Launch("L")
    if not E_Blow:        
        if E_Forced:
            call Statup("Emma", "Love", 90, -70)
            call Statup("Emma", "Obed", 70, 45)
            call Statup("Emma", "Inbt", 80, 60) 
        else:
            call Statup("Emma", "Love", 90, 5)
            call Statup("Emma", "Obed", 70, 35)
            call Statup("Emma", "Inbt", 80, 40)     
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no blow")
    $ E_RecentActions.append("blow")                      
    $ E_DailyActions.append("blow")     

label E_BJ_Cycle: #Repeating strokes  
    while Round >=0:  
        call Shift_Focus("Emma") 
        call Emma_BJ_Launch    
        call EmmaLust   
        
        if  P_Focus < 100:                                                   
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
                                if "pushed" not in E_RecentActions and E_Blow < 5:
                                    call Statup("Emma", "Love", 80, -(20-(2*E_Blow))) 
                                    call Statup("Emma", "Obed", 80, (30-(3*E_Blow)))
                                    $ E_RecentActions.append("pushed")
                                if Trigger2 == "jackin" and Speed != 3:
                                    "She takes it to the root, and you move your hand out of the way."
                                $ Speed = 4  
                        "Take it deeper. (locked)" if Speed == 4:
                                pass
                            
                        "Set your own pace. . .":                
                                "Emma hums contentedly."    
                                if "setpace" not in E_RecentActions:
                                    call Statup("Emma", "Love", 80, 2)
                                $ D20 = renpy.random.randint(1, 20)     
                                if E_Blow < 5:
                                    $ D20 -= 10
                                elif E_Blow < 10:
                                    $ D20 -= 5
                                    
                                if D20 > 15:
                                    $ Speed = 4              
                                    if "setpace" not in E_RecentActions:      
                                        call Statup("Emma", "Inbt", 80, 3) 
                                elif D20 > 10:
                                    $ Speed = 3
                                elif D20 > 5:
                                    $ Speed = 2
                                else:
                                    $ Speed = 1
                                $ E_RecentActions.append("setpace")
                                
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
                                            if E_Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ E_Action -= 1
                                            else:
                                                ch_e "Hmm, I think we've probably done enough for now. . ."  
                                         
                                    "Shift primary action":
                                            if E_Action and MultiAction:
                                                    menu:
                                                        "How about a handy?":
                                                                if E_Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call E_BJ_After
                                                                    call E_Handjob
                                                                else:
                                                                    ch_e "I'm kinda tired, could we just wrap this up. . ."
                                                        "How about a titjob?":
                                                                if E_Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call E_BJ_After
                                                                    call E_Titjob
                                                                else:
                                                                    ch_e "I'm kinda tired, could we just wrap this up. . ."                                        
                                                        "Never Mind":
                                                                jump E_BJ_Cycle
                                            else: 
                                                ch_e "Hmm, I think we've probably done enough for now. . ."           
                    
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
                                                        jump E_BJ_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump E_BJ_Cycle 
                                            "Never mind":
                                                        jump E_BJ_Cycle 
                                    "Undress Emma":
                                            call E_Undress   
                                    "Clean up Emma (locked)" if not E_Spunk:
                                            pass  
                                    "Clean up Emma" if E_Spunk:
                                            call Emma_Cleanup("ask")                                         
                                    "Never mind":
                                            jump E_BJ_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Emma_BJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_BJ_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Emma_BJ_Reset
                                    $ Line = 0
                                    jump E_BJ_After
        #End menu (if Line)
        
        call Shift_Focus("Emma")             
        call Sex_Dialog("Emma",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
        if Speed:
            $ P_Wet = 1 #wets penis        
            $ P_Spunk = 0 if P_Spunk else P_Spunk #cleans you off after one cycle
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or E_Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PE_Cumming
                            if "angry" in E_RecentActions:  
                                call Emma_BJ_Reset
                                return    
                            call Statup("Emma", "Lust", 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_BJ_After 
                            $ Line = "came"
     
                    if E_Lust >= 100:  
                            #If Emma can cum                                             
                            call E_Cumming
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_BJ_After
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in E_RecentActions:#And Emma is unsatisfied,  
                                    "Emma still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it" 
                                        "No, I'm done.":
                                            "You pull back."
                                            jump E_BJ_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Emma")            
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
        elif Cnt == (15 + E_Blow):
                $ E_Brows = "angry"        
                menu:
                    ch_e "I'm getting a bit worn out here, could we do something else?"
                    "How about a Handy?" if E_Action and MultiAction:
                            $ Situation = "shift"
                            call E_BJ_After
                            call E_Handjob 
                            return
                    "Finish up." if P_FocusX:
                            "You release your concentration. . ."             
                            $ P_FocusX = 0
                            $ P_Focus += 15
                            $ Cnt += 1
                            "[Line]."
                            jump E_BJ_Cycle
                    "Let's try something else." if MultiAction: 
                            $ Line = 0
                            call Emma_BJ_Reset
                            $ Situation = "shift"
                            jump E_BJ_After
                    "No, get back down there.":
                            if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):
                                call Statup("Emma", "Love", 200, -5)
                                call Statup("Emma", "Obed", 50, 3)
                                call Statup("Emma", "Obed", 80, 2)
                                "She scowls but gets back to work."
                            else:
                                call EmmaFace("angry", 1)  
                                "She scowls at you, drops you cock and pulls back."
                                ch_e "Well then."
                                call Statup("Emma", "Love", 50, -3, 1)
                                call Statup("Emma", "Love", 80, -4, 1)
                                call Statup("Emma", "Obed", 30, -1, 1)
                                call Statup("Emma", "Obed", 50, -1, 1)  
                                $ E_RecentActions.append("angry")
                                $ E_DailyActions.append("angry")   
                                jump E_BJ_After        
        elif Cnt == (10 + E_Blow) and E_SEXP <= 100 and not ApprovalCheck("Emma", 1200, "LO"):
                    $ E_Brows = "confused"
                    ch_e "Are you about done? I'm a little tired of this."  
        #End Count check
        
        if Round == 10:
            ch_e "It's getting a bit late. . ."  
        elif Round == 5:
            ch_e "Do you mind if we take a break?"        
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    ch_e "Ok, I need to rest my jaw for a minute. . ."

label E_BJ_After:    
    call EmmaFace("sexy")  
        
    $ E_Blow += 1
    $ E_Action -=1
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1
                
    call Partner_Like("Emma",2)
        
    if "Emma Jobber" in Achievements:
        pass
    elif E_Blow >= 10:
        call EmmaFace("smile", 1)
        ch_e "You taste positively intoxicating, [E_Petname]."      
        $ Achievements.append("Emma Jobber")
        $E_SEXP += 5
    elif Situation == "shift":
        pass
    elif E_Blow == 1:
            $E_SEXP += 15
            if E_Love >= 500:
                $ E_Mouth = "smile"
                ch_e "Hmm, better than I'd imagined. . ."
            elif P_Focus <= 20:
                $ E_Mouth = "sad"
                ch_e "Was it all you dreamed of?"     
    elif E_Blow == 5:
        ch_e "Best you've had, I'm sure."
        menu:
            "[[nod]":
                call EmmaFace("smile", 1)
                call Statup("Emma", "Love", 90, 10)
                call Statup("Emma", "Obed", 80, 5)
                call Statup("Emma", "Inbt", 90, 10) 
            "[[shake head \"no\"]":        
                if ApprovalCheck("Emma", 500, "O"):
                    call EmmaFace("sad", 2)
                    call Statup("Emma", "Love", 200, -5)
                else:
                    call EmmaFace("angry", 2)
                    call Statup("Emma", "Love", 200, -30)
                call Statup("Emma", "Obed", 80, 20)
                ch_e ". . ."         
                call EmmaFace("sad", 1)
    
    $ Tempmod = 0    
    if Situation != "shift":
        call Emma_BJ_Reset    
    call Checkout
    return
    


# end E_Blowjob                                 //////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label E_Dildo_Check:
    if "dildo" in P_Inventory:   
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in E_Inventory:
        "You ask Emma to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1
            
label E_Dildo_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Emma")
    call E_Dildo_Check    
    if not _return:
        return 

    if E_DildoP: #You've done it before
        $ Tempmod += 15
    if E_Legs == "pants:": # she's got pants on.
        $ Tempmod -= 20
        
    if E_Lust > 95:
        $ Tempmod += 20    
    elif E_Lust > 85: #She's really horny
        $ Tempmod += 15
        
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
        
    if "no dildo" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no dildo" in E_RecentActions else 0       
        
    $ Approval = ApprovalCheck("Emma", 1250, TabM = 4) # 125, 140, 155, Taboo -160(335)
    
    if Situation == "Emma":                                                                  #Emma auto-starts   
                if Approval > 2:                                                      # fix, add emma auto stuff here
                    if E_Legs == "skirt":
                        "Emma grabs her dildo, hiking up her skirt as she does."
                        $ E_Upskirt = 1
                    elif E_Legs == "pants":
                        "Emma grabs her dildo, pulling down her pants as she does."              
                        $ E_Legs = 0
                    else:
                        "Emma grabs her dildo, rubbing is suggestively against her crotch."
                    $ E_SeenPanties = 1
                    "She slides the tip along her pussy and seems to want you to insert it."
                    menu:
                        "What do you do?"
                        "Nothing.":                    
                            call Statup("Emma", "Inbt", 80, 3) 
                            call Statup("Emma", "Inbt", 50, 2)
                            "Emma slides it in."
                        "Go for it.":       
                            call EmmaFace("sexy", 1)                    
                            call Statup("Emma", "Inbt", 80, 3) 
                            ch_p "Oh yeah, [E_Pet], let's do this."
                            call Emma_Namecheck
                            "You grab the dildo and slide it in."
                            call Statup("Emma", "Love", 85, 1)
                            call Statup("Emma", "Obed", 90, 1)
                            call Statup("Emma", "Obed", 50, 2)
                        "Ask her to stop.":
                            call EmmaFace("surprised")       
                            call Statup("Emma", "Inbt", 70, 1) 
                            ch_p "Let's not do that right now, [E_Pet]."
                            call Emma_Namecheck
                            "Emma sets the dildo down."
                            call EmmaOutfit
                            call Statup("Emma", "Obed", 90, 1)
                            call Statup("Emma", "Obed", 50, 1)
                            call Statup("Emma", "Obed", 30, 2)
                            return            
                    jump E_DP_Prep
                else:                
                    $ Tempmod = 0                               # fix, add emma auto stuff here
                    $ Trigger2 = 0
                return            
    
    if Situation == "auto":    
                "You rub the dildo across her body, and along her moist slit."
                call EmmaFace("surprised", 1)
                
                if (E_DildoP and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
                    "Emma is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                    call EmmaFace("sexy")
                    call Statup("Emma", "Obed", 70, 3)
                    call Statup("Emma", "Inbt", 50, 3) 
                    call Statup("Emma", "Inbt", 70, 1) 
                    ch_e "Hmm, [E_Petname], toys!"            
                    jump E_DP_Prep         
                else:                                                                                                            #she's questioning it
                    $ E_Brows = "angry"                
                    menu:
                        ch_e "Excuse yourself, what are you planning to do with that?!" 
                        "Sorry, sorry! Never mind.":
                            if Approval:     
                                call EmmaFace("sexy", 1)
                                call Statup("Emma", "Obed", 70, 3)
                                call Statup("Emma", "Inbt", 50, 3) 
                                call Statup("Emma", "Inbt", 70, 1) 
                                ch_e "Well, now that you mention it. . ."
                                jump E_DP_Prep
                            "You pull back before you really get it in."                    
                            call EmmaFace("bemused", 1)
                            if E_DildoP:
                                ch_e "Well, [E_Petname], maybe warn me next time?" 
                            else:
                                ch_e "Well, [E_Petname], that's a little much. . . for now . . ."                                               
                        "Just playing with my favorite toys.":                    
                            call Statup("Emma", "Love", 80, -10, 1)  
                            call Statup("Emma", "Love", 200, -10)
                            "You press it inside some more."                              
                            call Statup("Emma", "Obed", 70, 3)
                            call Statup("Emma", "Inbt", 50, 3) 
                            if not ApprovalCheck("Emma", 700, "O", TabM=1): #Checks if Obed is 700+                             
                                call EmmaFace("angry")
                                "Emma shoves you away and slaps you in the face."
                                ch_e "Ask nicely before trying anything like that!"                                               
                                call Statup("Emma", "Love", 50, -10, 1)                        
                                call Statup("Emma", "Obed", 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                if renpy.showing("Emma_SexSprite"):
                                    call Emma_Sex_Reset 
                                $ E_RecentActions.append("angry")
                                $ E_DailyActions.append("angry")                          
                            else:
                                call EmmaFace("sad")
                                "Emma doesn't seem to be into this, you're lucky she's so obedient."                        
                                jump E_DP_Prep
                return             
    #end Auto
   
    if not E_DildoP:                                                               
            #first time    
            call EmmaFace("surprised", 1)
            $ E_Mouth = "kiss"
            ch_e "Hmmm, so you'd like to try out some toys?"    
            if E_Forced:
                call EmmaFace("sad")
                ch_e "I suppose there are worst things you could ask for."
            
    if not E_DildoP and Approval:                                                 
            #First time dialog        
            if E_Forced: 
                call EmmaFace("sad")
                call Statup("Emma", "Love", 70, -3, 1)
                call Statup("Emma", "Love", 20, -2, 1)
            elif E_Love >= (E_Obed + E_Inbt):
                call EmmaFace("sexy")
                $ E_Brows = "sad"
                $ E_Mouth = "smile" 
                ch_e "I've had a reasonable amount of experience with these, you know. . ."            
            elif E_Obed >= E_Inbt:
                call EmmaFace("normal")
                ch_e "If that's what you want, [E_Petname]. . ."            
            else: # Uninhibited 
                call EmmaFace("sad")
                $ E_Mouth = "smile"             
                ch_e "I guess it could be fun with a partner. . ."    
            
    elif Approval:                                                                       
            #Second time+ dialog
            if E_Forced: 
                call EmmaFace("sad")
                call Statup("Emma", "Love", 70, -3, 1)
                call Statup("Emma", "Love", 20, -2, 1)
                ch_e "The toys again?" 
            elif not Taboo and "tabno" in E_DailyActions:        
                ch_e "Well, at least you got us some privacy this time. . ."   
            elif "dildo pussy" in E_RecentActions:
                call EmmaFace("sexy", 1)
                ch_e "Mmm, again? Ok, let's get to it."
                jump E_DP_Prep
            elif "dildo pussy" in E_DailyActions:
                call EmmaFace("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "You're going to wear me out."]) 
                ch_e "[Line]"
            elif E_DildoP < 3:        
                call EmmaFace("sexy", 1)
                $ E_Brows = "confused"
                $ E_Mouth = "kiss"
                ch_e "You want to stick it in my pussy again?"       
            else:       
                call EmmaFace("sexy", 1)
                $ Emma_Arms = 2
                $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my pussy again?",
                    "You want me ta lube up your toy?"]) 
                ch_e "[Line]"
                $ Line = 0
            
    if Approval >= 2:                                                                   
            #She's into it. . .               
            if E_Forced:
                call EmmaFace("sad")
                call Statup("Emma", "Obed", 90, 1)
                call Statup("Emma", "Inbt", 60, 1)
                ch_e "Ok, fine."    
            else:
                call EmmaFace("sexy", 1)
                call Statup("Emma", "Love", 90, 1)
                call Statup("Emma", "Inbt", 50, 3) 
                $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess I could. . . stick it in.",
                    "Delightful.",
                    "Hmm, ok, ok."]) 
                ch_e "[Line]"
                $ Line = 0
            call Statup("Emma", "Obed", 20, 1)
            call Statup("Emma", "Obed", 60, 1)
            call Statup("Emma", "Inbt", 70, 2) 
            jump E_DP_Prep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            call EmmaFace("angry")
            if "no dildo" in E_RecentActions:  
                ch_e "What part of \"no,\" did you not get, [E_Petname]?"
            elif Taboo and "tabno" in E_DailyActions and "no dildo" in E_DailyActions:
                ch_e "Stop showing that thing around in public!"   
            elif "no dildo" in E_DailyActions:       
                ch_e "I already told you \"no,\" [E_Petname]."
            elif Taboo and "tabno" in E_DailyActions:  
                ch_e "Stop showing that thing around in public!"  
            elif not E_DildoP:
                call EmmaFace("bemused")
                ch_e "I'm a bit past toys, [E_Petname]. . ."
            else:
                call EmmaFace("bemused")
                ch_e "We don't need any toys, do we, [E_Petname]?"
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in E_DailyActions:
                    call EmmaFace("bemused")
                    ch_e "I thought as much, [E_Petname]."              
                    return
                "Maybe later?" if "no dildo" not in E_DailyActions:
                    call EmmaFace("sexy")  
                    ch_e "Maybe I'll practice on my own time, [E_Petname]."
                    call Statup("Emma", "Love", 80, 2)
                    call Statup("Emma", "Inbt", 70, 2)  
                    if Taboo:                    
                        $ E_RecentActions.append("tabno")                      
                        $ E_DailyActions.append("tabno") 
                    $ E_RecentActions.append("no dildo")                      
                    $ E_DailyActions.append("no dildo") 
                    return
                "I think you'd like it. . .":             
                    if Approval:
                        call EmmaFace("sexy")     
                        call Statup("Emma", "Obed", 90, 2)
                        call Statup("Emma", "Obed", 50, 2)
                        call Statup("Emma", "Inbt", 70, 3) 
                        call Statup("Emma", "Inbt", 40, 2) 
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You make a compelling argument."]) 
                        ch_e "[Line]"
                        $ Line = 0                   
                        jump E_DP_Prep
                    else:   
                        pass
                        
                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Emma", 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                    if Approval > 1 or (Approval and E_Forced):
                        call EmmaFace("sad")
                        call Statup("Emma", "Love", 70, -5, 1)
                        call Statup("Emma", "Love", 200, -5)                 
                        ch_e "Ok, fine. If we're going to do this, stick it in already."  
                        call Statup("Emma", "Obed", 80, 4)
                        call Statup("Emma", "Inbt", 80, 1) 
                        call Statup("Emma", "Inbt", 60, 3)  
                        $ E_Forced = 1  
                        jump E_DP_Prep
                    else:                              
                        call Statup("Emma", "Love", 200, -20)     
                        $ E_RecentActions.append("angry")
                        $ E_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Emma_Arms = 1  
    if "no dildo" in E_DailyActions:
            ch_e "Learn to take \"no\" for an answer, [E_Petname]."   
            $ E_RecentActions.append("angry")
            $ E_DailyActions.append("angry")   
    elif E_Forced:
            call EmmaFace("angry", 1)
            ch_e "I'm not going to let you use that on me."
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
            ch_e "Not here!"     
            call Statup("Emma", "Lust", 200, 5)  
            call Statup("Emma", "Obed", 50, -3)  
    elif E_DildoP:
            call EmmaFace("sad") 
            ch_e "Sorry, you can keep your toys to yourself."     
    else:
            call EmmaFace("normal", 1)
            ch_e "No way."  
    $ E_RecentActions.append("no dildo")                      
    $ E_DailyActions.append("no dildo")  
    $ Tempmod = 0    
    return
                
label E_DP_Prep: #Animation set-up 
    if Trigger2 == "dildo pussy":
        return
        
    if not E_Forced and Situation != "auto":
        $ Tempmod = 15 if E_Legs == "pants" else 0           
        call Emma_Bottoms_Off
        if "angry" in E_RecentActions:
            return    
            
    $ Tempmod = 0      
    call E_Pussy_Launch("dildo pussy")
    if not E_DildoP:        
        if E_Forced:
            call Statup("Emma", "Love", 90, -75)
            call Statup("Emma", "Obed", 70, 60)
            call Statup("Emma", "Inbt", 80, 35) 
        else:
            call Statup("Emma", "Love", 90, 10)
            call Statup("Emma", "Obed", 70, 20)
            call Statup("Emma", "Inbt", 80, 45)
    if Taboo:
        $ E_Inbt += int(Taboo/10)  
        $ E_Lust += int(Taboo/5)
    
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0    
    $ Cnt = 0
    if Taboo:
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no dildo")
    $ E_RecentActions.append("dildo pussy")                      
    $ E_DailyActions.append("dildo pussy") 
    
label E_DP_Cycle: #Repeating strokes    
    while Round >=0:  
        call Shift_Focus("Emma") 
        call E_Pussy_Launch("dildo pussy")
        call EmmaLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                               
                        "Slap her ass":                     
                                call E_Slap_Ass
                                jump E_DP_Cycle  
                                
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
                                                ch_e "Hmm, I think we've probably done enough for now. . ."  
                                                
                                    "Shift primary action":
                                            if E_Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in her ass.":
                                                                $ Situation = "shift"
                                                                call E_DP_After
                                                                call E_Insert_Ass    
                                                        "Just stick a finger in her ass without asking.":
                                                                $ Situation = "auto"
                                                                call E_DP_After
                                                                call E_Insert_Ass                                           
                                                        "I want to shift the dildo to her ass.":
                                                                $ Situation = "shift"
                                                                call E_DP_After
                                                                call E_Dildo_Ass   
                                                        "Never Mind":
                                                                jump E_DP_Cycle
                                            else: 
                                                ch_e "Hmm, I think we've probably done enough for now. . ."           
                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call E_DP_After
                                                call Emma_Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
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
                                                        jump E_DP_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump E_DP_Cycle 
                                            "Never mind":
                                                        jump E_DP_Cycle 
                                    "Undress Emma":
                                            call E_Undress   
                                    "Clean up Emma (locked)" if not E_Spunk:
                                            pass  
                                    "Clean up Emma" if E_Spunk:
                                            call Emma_Cleanup("ask")                                         
                                    "Never mind":
                                            jump E_DP_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call E_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_DP_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call E_Pos_Reset
                                    $ Line = 0
                                    jump E_DP_After
        #End menu (if Line)
        
        if E_Panties or E_Legs == "pants" or HoseNum("Emma") >= 5: #This checks if Emma wants to strip down.
                call E_Undress("auto")
            
        call Shift_Focus("Emma")    
        call Sex_Dialog("Emma",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or E_Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PE_Cumming
                            if "angry" in E_RecentActions:  
                                call E_Pos_Reset
                                return    
                            call Statup("Emma", "Lust", 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_DP_After 
                            $ Line = "came"     
                    if E_Lust >= 100:  
                            #If Emma can cum                                             
                            call E_Cumming
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_DP_After                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break." 
                            if "unsatisfied" in E_RecentActions:#And Emma is unsatisfied,  
                                    "Emma still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it" 
                                        "No, I'm done.":
                                            "You pull back."
                                            jump E_DP_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Emma")            
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
        elif Cnt == (5 + E_DildoP):
                    $ E_Brows = "confused"
                    ch_e "What are you even doing down there?" 
        elif E_Lust >= 80:
                    pass
        elif Cnt == (15 + E_DildoP) and E_SEXP >= 15 and not ApprovalCheck("Emma", 1500):
                    $ E_Brows = "confused"        
                    menu:
                        ch_e "[E_Petname], this is getting uncomfortable, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump E_DP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump E_DP_After
                        "No, this is fun.":   
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    call Statup("Emma", "Love", 200, -5)
                                    call Statup("Emma", "Obed", 50, 3)                    
                                    call Statup("Emma", "Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call EmmaFace("angry", 1)   
                                    call E_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_e "Well if that's your attitude, I don't need your \"help\"."                         
                                    call Statup("Emma", "Love", 50, -3, 1)
                                    call Statup("Emma", "Love", 80, -4, 1)
                                    call Statup("Emma", "Obed", 30, -1, 1)                    
                                    call Statup("Emma", "Obed", 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_DP_After
        #End Count check
           
        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."   
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."      
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    ch_e "Ok, [E_Petname], that's enough of that for now."
    
    
label E_DP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call E_Pos_Reset
        
    call EmmaFace("sexy") 
    
    $ E_DildoP += 1  
    $ E_Action -=1   
    
    call Partner_Like("Emma",1)
     
    if E_DildoP == 1:            
            $ E_SEXP += 10         
            if not Situation: 
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "I appreciate the work you put in. . ."
                elif E_Obed <= 500 and P_Focus <= 20:
                    call EmmaFace("perplexed", 1)
                    ch_e "Did you enjoy that?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_e "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# end E_Dildo Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Insert Ass    

label E_Dildo_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Emma")
    call E_Dildo_Check
    if not _return:
        return 
      
    if E_Loose:
        $ Tempmod += 30   
    elif "anal" in E_RecentActions or "dildo anal" in E_RecentActions:
        $ Tempmod -= 20 
    elif "anal" in E_DailyActions or "dildo anal" in E_DailyActions:
        $ Tempmod -= 10
    elif (E_Anal + E_DildoA + E_Plug) > 0: #You've done it before
        $ Tempmod += 20   
        
    if E_Legs == "pants:": # she's got pants on.
        $ Tempmod -= 20   
        
    if E_Lust > 95:
        $ Tempmod += 20
    elif E_Lust > 85: #She's really horny
        $ Tempmod += 15
        
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
        
    if "no dildo" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no dildo" in E_RecentActions else 0   
        
    $ Approval = ApprovalCheck("Emma", 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)
    
    if Situation == "Emma":                                                                  
            #Emma auto-starts   
            if Approval > 2:                                                      # fix, add emma auto stuff here
                if E_Legs == "skirt":
                    "Emma grabs her dildo, hiking up her skirt as she does."
                    $ E_Upskirt = 1
                elif E_Legs == "pants":
                    "Emma grabs her dildo, pulling down her pants as she does."              
                    $ E_Legs = 0
                else:
                    "Emma grabs her dildo, rubbing is suggestively against her ass."
                $ E_SeenPanties = 1
                "She slides the tip against her asshole, and seems to want you to insert it."
                menu:
                    "What do you do?"
                    "Nothing.":                    
                        call Statup("Emma", "Inbt", 80, 3) 
                        call Statup("Emma", "Inbt", 50, 2)
                        "Emma slides it in."
                    "Go for it.":       
                        call EmmaFace("sexy", 1)                    
                        call Statup("Emma", "Inbt", 80, 3) 
                        ch_p "Oh yeah, [E_Pet], let's do this."
                        call Emma_Namecheck
                        "You grab the dildo and slide it in."
                        call Statup("Emma", "Love", 85, 1)
                        call Statup("Emma", "Obed", 90, 1)
                        call Statup("Emma", "Obed", 50, 2)
                    "Ask her to stop.":
                        call EmmaFace("surprised")       
                        call Statup("Emma", "Inbt", 70, 1) 
                        ch_p "Let's not do that right now, [E_Pet]."
                        call Emma_Namecheck
                        "Emma sets the dildo down."
                        call EmmaOutfit
                        call Statup("Emma", "Obed", 90, 1)
                        call Statup("Emma", "Obed", 50, 1)
                        call Statup("Emma", "Obed", 30, 2)
                        return            
                jump E_DA_Prep
            else:                
                $ Tempmod = 0                               # fix, add emma auto stuff here
                $ Trigger2 = 0
            return            
    
    if Situation == "auto":    
            "You rub the dildo across her body, and against her tight anus."
            call EmmaFace("surprised", 1)
            
            if (E_DildoA and Approval) or (Approval > 1):                                                                      
                #this is not the first time you've had sex, or she's into it         
                "Emma is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                call EmmaFace("sexy")
                call Statup("Emma", "Obed", 70, 3)
                call Statup("Emma", "Inbt", 50, 3) 
                call Statup("Emma", "Inbt", 70, 1)
                ch_e "Mmmm, [E_Petname], toys. . ."                
                jump E_DA_Prep         
            else:                                                                                                            
                #she's questioning it
                $ E_Brows = "angry"                
                menu:
                    ch_e "Excuse yourself, what are you planning to do with that?!" 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            call EmmaFace("sexy", 1)
                            call Statup("Emma", "Obed", 70, 3)
                            call Statup("Emma", "Inbt", 50, 3) 
                            call Statup("Emma", "Inbt", 70, 1) 
                            ch_e "Well, now that you mention it. . ."
                            jump E_DA_Prep
                        "You pull back before you really get it in."                    
                        call EmmaFace("bemused", 1)
                        if E_DildoA:
                            ch_e "Well, [E_Petname], maybe warn me next time?" 
                        else:
                            ch_e "Well, [E_Petname], that's a little much. . . for now . . ."                                                   
                    "Just playing with my favorite toys.":                    
                        call Statup("Emma", "Love", 80, -10, 1)  
                        call Statup("Emma", "Love", 200, -10)
                        "You press it inside some more."                              
                        call Statup("Emma", "Obed", 70, 3)
                        call Statup("Emma", "Inbt", 50, 3) 
                        if not ApprovalCheck("Emma", 700, "O", TabM=1): #Checks if Obed is 700+                           
                            call EmmaFace("angry")
                            "Emma shoves you away and slaps you in the face."
                            ch_e "Ask nicely if you want to stick something in my ass!"                                                  
                            call Statup("Emma", "Love", 50, -10, 1)                        
                            call Statup("Emma", "Obed", 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            if renpy.showing("Emma_SexSprite"):
                                call Emma_Sex_Reset 
                            $ E_RecentActions.append("angry")
                            $ E_DailyActions.append("angry")                         
                        else:
                            call EmmaFace("sad")
                            "Emma doesn't seem to be into this, you're lucky she's so obedient."                        
                            jump E_DA_Prep
            return             
    #end auto
   
    if not E_DildoA:                                                               
            #first time    
            call EmmaFace("surprised", 1)
            $ E_Mouth = "kiss"
            ch_e "Hmm, you don't take half measures. . ."    
            if E_Forced:
                call EmmaFace("sad")
                ch_e "They always go for the butt. . ."
    
    if not E_DildoA and Approval:                                                 
            #First time dialog        
            if E_Forced: 
                call EmmaFace("sad")
                call Statup("Emma", "Love", 70, -3, 1)
                call Statup("Emma", "Love", 20, -2, 1)
            elif E_Love >= (E_Obed + E_Inbt):
                call EmmaFace("sexy")
                $ E_Brows = "sad"
                $ E_Mouth = "smile" 
                ch_e "I suppose you might enjoy that. . ."            
            elif E_Obed >= E_Inbt:
                call EmmaFace("normal")
                ch_e "If that's what you want, [E_Petname]. . ."            
            else: # Uninhibited 
                call EmmaFace("sad")
                $ E_Mouth = "smile"             
                ch_e "I suppose I could enjoy that. . ."    
            
    elif Approval:                                                                       
            #Second time+ dialog
            if E_Forced: 
                call EmmaFace("sad")
                call Statup("Emma", "Love", 70, -3, 1)
                call Statup("Emma", "Love", 20, -2, 1)
                ch_e "The toys again?"  
            elif not Taboo and "tabno" in E_DailyActions:        
                ch_e "Well, at least you got us some privacy this time. . ."   
            elif "dildo anal" in E_DailyActions and not E_Loose:
                pass
            elif E_DildoA < 3:        
                call EmmaFace("sexy", 1)
                $ E_Brows = "confused"
                $ E_Mouth = "kiss"
                ch_e "You want to stick it in my ass again?"       
            else:       
                call EmmaFace("sexy", 1)
                $ Emma_Arms = 2
                $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You'd like to stick it in my ass again?",
                    "You'd like me to lube up your toy?"]) 
                ch_e "[Line]"
                $ Line = 0
            
    if Approval >= 2:                                                                  
            #She's into it. . .               
            if E_Forced:
                call EmmaFace("sad")
                call Statup("Emma", "Obed", 90, 1)
                call Statup("Emma", "Inbt", 60, 1)
                ch_e "Oh, fine."    
            else:
                call EmmaFace("sexy", 1)
                call Statup("Emma", "Love", 90, 1)
                call Statup("Emma", "Inbt", 50, 3) 
                $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                    "Hmm. . . ok.",                 
                    "Sure!", 
                    "I guess I could. . . stick it in.",
                    "Delightful.",
                    "Hmm, ok, ok."]) 
                ch_e "[Line]"
                $ Line = 0
            call Statup("Emma", "Obed", 20, 1)
            call Statup("Emma", "Obed", 60, 1)
            call Statup("Emma", "Inbt", 70, 2) 
            jump E_DA_Prep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            call EmmaFace("angry")
            if "no dildo" in E_RecentActions:  
                ch_e "What part of \"no,\" did you not get, [E_Petname]?"
            elif Taboo and "tabno" in E_DailyActions and "no dildo" in E_DailyActions:
                ch_e "Stop swinging that thing around in public!"  
            elif "no dildo" in E_DailyActions:       
                ch_e "I already told you \"no,\" [E_Petname]."
            elif Taboo and "tabno" in E_DailyActions:  
                ch_e "I already told you that I wouldn't do that out here!"  
            elif not E_DildoA:
                call EmmaFace("bemused")
                ch_e "I'm just not into toys, [E_Petname]. . ."
            else:
                call EmmaFace("bemused")
                ch_e "I don't think we need any toys, [E_Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in E_DailyActions:
                    call EmmaFace("bemused")
                    ch_e "I'm sure, [E_Petname]."              
                    return
                "Maybe later?" if "no dildo" not in E_DailyActions:
                    call EmmaFace("sexy")  
                    ch_e "Perhaps I'll practice on my own time, [E_Petname]."
                    call Statup("Emma", "Love", 80, 2)
                    call Statup("Emma", "Inbt", 70, 2)  
                    if Taboo:                    
                        $ E_RecentActions.append("tabno")                      
                        $ E_DailyActions.append("tabno") 
                    $ E_RecentActions.append("no dildo")                      
                    $ E_DailyActions.append("no dildo") 
                    return
                "I think you'd like it. . .":             
                    if Approval:
                        call EmmaFace("sexy")     
                        call Statup("Emma", "Obed", 90, 2)
                        call Statup("Emma", "Obed", 50, 2)
                        call Statup("Emma", "Inbt", 70, 3) 
                        call Statup("Emma", "Inbt", 40, 2) 
                        $ Line = renpy.random.choice(["Very well, stick it in.",     
                            "I suppose. . .", 
                            "You make a compelling argument."]) 
                        ch_e "[Line]"
                        $ Line = 0                   
                        jump E_DA_Prep
                    else:   
                        pass
                        
                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Emma", 1050, "OI", TabM = 3) # 105, 120, 135, -120(225)
                    if Approval > 1 or (Approval and E_Forced):
                        call EmmaFace("sad")
                        call Statup("Emma", "Love", 70, -5, 1)
                        call Statup("Emma", "Love", 200, -5)                 
                        ch_e "Ok, fine. If we're going to do this, stick it in already."  
                        call Statup("Emma", "Obed", 80, 4)
                        call Statup("Emma", "Inbt", 80, 1) 
                        call Statup("Emma", "Inbt", 60, 3)  
                        $ E_Forced = 1  
                        jump E_DA_Prep
                    else:                              
                        call Statup("Emma", "Love", 200, -20)    
                        $ E_RecentActions.append("angry")
                        $ E_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Emma_Arms = 1   
    if "no dildo" in E_DailyActions:
            ch_e "Learn to take \"no\" for an answer, [E_Petname]."   
            $ E_RecentActions.append("angry")
            $ E_DailyActions.append("angry")   
    elif E_Forced:
            call EmmaFace("angry", 1)
            ch_e "I'm not going to let you use that on me."
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
            ch_e "Not here!"     
            call Statup("Emma", "Lust", 200, 5)  
            call Statup("Emma", "Obed", 50, -3)  
    elif E_DildoA:
            call EmmaFace("sad") 
            ch_e "Sorry, you can keep your toys out of there."     
    else:
            call EmmaFace("normal", 1)
            ch_e "No, thank you." 
    $ E_RecentActions.append("no dildo")                      
    $ E_DailyActions.append("no dildo")   
    $ Tempmod = 0    
    return
                
label E_DA_Prep: #Animation set-up 
    if Trigger2 == "dildo anal":
        return
        
    if not E_Forced and Situation != "auto":
        $ Tempmod = 20 if E_Legs == "pants" else 0           
        call Emma_Bottoms_Off
        if "angry" in E_RecentActions:
            return    
            
    $ Tempmod = 0      
    call E_Pussy_Launch("dildo anal")
    if not E_DildoA:        
        if E_Forced:
            call Statup("Emma", "Love", 90, -75)
            call Statup("Emma", "Obed", 70, 60)
            call Statup("Emma", "Inbt", 80, 35) 
        else:
            call Statup("Emma", "Love", 90, 10)
            call Statup("Emma", "Obed", 70, 20)
            call Statup("Emma", "Inbt", 80, 45)
    if Taboo:
        $ E_Inbt += int(Taboo/10)  
        $ E_Lust += int(Taboo/5)
    
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0    
    $ Cnt = 0
    if Taboo:
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no dildo")
    $ E_RecentActions.append("dildo anal")                      
    $ E_DailyActions.append("dildo anal") 
    
label E_DA_Cycle: #Repeating strokes    
    while Round >=0:  
        call Shift_Focus("Emma") 
        call E_Pussy_Launch("dildo anal")
        call EmmaLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                               
                        "Slap her ass":                     
                                call E_Slap_Ass
                                jump E_DA_Cycle  
                                
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
                                                ch_e "Hmm, I think we've probably done enough for now. . ."  
                                                
                                    "Shift primary action":
                                            if E_Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in her pussy.":
                                                                $ Situation = "shift"
                                                                call E_DA_After
                                                                call E_Fondle_Pussy    
                                                        "Just stick a finger in her pussy without asking.":
                                                                $ Situation = "auto"
                                                                call E_DA_After
                                                                call E_Fondle_Pussy                                           
                                                        "I want to shift the dildo to her pussy.":
                                                                $ Situation = "shift"
                                                                call E_DA_After
                                                                call E_Dildo_Pussy 
                                                        "Never Mind":
                                                                jump E_DA_Cycle
                                            else: 
                                                ch_e "Hmm, I think we've probably done enough for now. . ."           
                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call E_DA_After
                                                call Emma_Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
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
                                                        jump E_DA_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump E_DA_Cycle 
                                            "Never mind":
                                                        jump E_DA_Cycle 
                                    "Undress Emma":
                                            call E_Undress   
                                    "Clean up Emma (locked)" if not E_Spunk:
                                            pass  
                                    "Clean up Emma" if E_Spunk:
                                            call Emma_Cleanup("ask")                                         
                                    "Never mind":
                                            jump E_DA_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call E_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_DA_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call E_Pos_Reset
                                    $ Line = 0
                                    jump E_DA_After
        #End menu (if Line)
        
        if E_Panties or E_Legs == "pants" or HoseNum("Emma") >= 5: #This checks if Emma wants to strip down.
                call E_Undress("auto")
            
        call Shift_Focus("Emma")    
        call Sex_Dialog("Emma",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or E_Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PE_Cumming
                            if "angry" in E_RecentActions:  
                                call E_Pos_Reset
                                return    
                            call Statup("Emma", "Lust", 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_DA_After 
                            $ Line = "came"
     
                    if E_Lust >= 100:  
                            #If Emma can cum                                             
                            call E_Cumming
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_DA_After
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in E_RecentActions:#And Emma is unsatisfied,  
                                    "Emma still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it" 
                                        "No, I'm done.":
                                            "You pull back."
                                            jump E_DA_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Emma")            
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
        elif Cnt == (5 + E_DildoA):
                    $ E_Brows = "confused"
                    ch_e "What are you even doing down there?" 
        elif E_Lust >= 80:
                    pass
        elif Cnt == (15 + E_DildoA) and E_SEXP >= 15 and not ApprovalCheck("Emma", 1500):
                    $ E_Brows = "confused"        
                    menu:
                        ch_e "[E_Petname], this is getting uncomfortable, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump E_DA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump E_DA_After
                        "No, this is fun.":   
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    call Statup("Emma", "Love", 200, -5)
                                    call Statup("Emma", "Obed", 50, 3)                    
                                    call Statup("Emma", "Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call EmmaFace("angry", 1)   
                                    call E_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_e "Well if that's your attitude, I don't need your \"help\"."                         
                                    call Statup("Emma", "Love", 50, -3, 1)
                                    call Statup("Emma", "Love", 80, -4, 1)
                                    call Statup("Emma", "Obed", 30, -1, 1)                    
                                    call Statup("Emma", "Obed", 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_DA_After
        #End Count check
           
        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."   
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."      
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    ch_e "Ok, [E_Petname], that's enough of that for now."
    
    
label E_DA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call E_Pos_Reset
        
    call EmmaFace("sexy") 
    
    $ E_DildoA += 1  
    $ E_Action -=1            
    
    call Partner_Like("Emma",1)
            
    if E_DildoA == 1:            
            $ E_SEXP += 10         
            if not Situation: 
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "That was. . . engaging. . ."
                elif E_Obed <= 500 and P_Focus <= 20:
                    call EmmaFace("perplexed", 1)
                    ch_e "Did you enjoy that?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_e "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# end E_Dildo Ass /////////////////////////////////////////////////////////////////////////////

label E_Vibrator_Check:                                                                                 #fix this whole section is copy/paste unfinished
    if "vibrator" in P_Inventory:   
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in E_Inventory:
        "You ask Emma to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1    
    
## E_Footjob //////////////////////////////////////////////////////////////////////
label E_Footjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Emma")
    if E_Foot >= 7: # She loves it
        $ Tempmod += 10
    elif E_Foot >= 3: #You've done it before several times
        $ Tempmod += 7
    elif E_Foot: #You've done it before
        $ Tempmod += 3
        
    if E_Addict >= 75 and E_Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 10
    if E_Addict >= 75:
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 15
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
        
    if "no foot" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no foot" in E_RecentActions else 0    
        
    $ Approval = ApprovalCheck("Emma", 1250, TabM = 3) # 110, 125, 140, Taboo -120(230)
    
    if Situation == "Emma":                                                                  #Emma auto-starts   
        if Approval > 2:                                                      # fix, add emma auto stuff here
            if Trigger2 == "jackin":
                "Emma sits back and starts rubbing her foot along your cock."
            else:
                "Emma gives you a mischevious smile, and starts to rub her foot along your cock."
            menu:
                "What do you do?"
                "Nothing.":                    
                    call Statup("Emma", "Inbt", 70, 3) 
                    call Statup("Emma", "Inbt", 30, 2)                     
                    "Emma continues her actions."
                "Praise her.":       
                    call EmmaFace("sexy", 1)                    
                    call Statup("Emma", "Inbt", 70, 3) 
                    ch_p "Oooh, that's good, [E_Pet]."
                    call Emma_Namecheck
                    "Emma continues her actions."
                    call Statup("Emma", "Love", 80, 1)
                    call Statup("Emma", "Obed", 90, 1)
                    call Statup("Emma", "Obed", 50, 2)
                "Ask her to stop.":
                    call EmmaFace("surprised")       
                    call Statup("Emma", "Inbt", 70, 1) 
                    ch_p "Let's not do that for now, [E_Pet]."
                    call Emma_Namecheck
                    "Emma puts it down."
                    call Statup("Emma", "Obed", 90, 1)
                    call Statup("Emma", "Obed", 50, 1)
                    call Statup("Emma", "Obed", 30, 2)
                    return            
            if Trigger:
                $ Trigger3 = "foot"
                return
            jump E_FJ_Prep
        else:                
            $ Tempmod = 0                               # fix, add emma auto stuff here
            $ Trigger2 = 0
            return            
    
    if not E_Foot and "no foot" not in E_RecentActions:        
        call EmmaFace("confused", 2)
        ch_e "Mmm, so you're into feet then, [E_Petname]?"
        $ E_Blush = 1
            
    if not E_Foot and Approval:                                                 #First time dialog        
        if E_Forced: 
            call EmmaFace("sad",1)
            call Statup("Emma", "Love", 70, -3, 1)
            call Statup("Emma", "Love", 20, -2, 1)
        elif E_Love >= (E_Obed + E_Inbt):
            call EmmaFace("sexy",1)
            $ E_Brows = "sad"
            $ E_Mouth = "smile" 
            ch_e "I suppose it couldn't hurt. . ."            
        elif E_Obed >= E_Inbt:
            call EmmaFace("normal",1)
            ch_e "If you enjoy that, [E_Petname]. . ."            
        elif E_Addict >= 50:
            call EmmaFace("manic", 1)
            ch_e "Very well. . ."  
        else: # Uninhibited 
            call EmmaFace("lipbite",1)    
            ch_e "Very well. . ."    
            
    elif Approval:                                                                       #Second time+ dialog
        if E_Forced: 
            call EmmaFace("sad")
            call Statup("Emma", "Love", 70, -3, 1)
            call Statup("Emma", "Love", 20, -2, 1)
            ch_e "That's it?" 
        elif not Taboo and "tabno" in E_DailyActions:        
            ch_e "Um, I suppose this is secluded enough. . ."    
        elif "foot" in E_RecentActions:
            call EmmaFace("sexy", 1)
            ch_e "You know, heels are nightmare on the arches. . ."
            jump E_FJ_Prep
        elif "foot" in E_DailyActions:
            call EmmaFace("sexy", 1)
            $ Line = renpy.random.choice(["Another?",   
                "I'd rather not get calluses.", 
                "Didn't get enough earlier?",
                "My feet are rather sore from earlier.",
                "My feet are rather sore from earlier."]) 
            ch_e "[Line]"
        elif E_Foot < 3:        
            call EmmaFace("sexy", 1)
            $ E_Brows = "confused"
            $ E_Mouth = "kiss"
            ch_e "Oh, very well. . ."        
        else:       
            call EmmaFace("sexy", 1)
            $ Emma_Arms = 2
            $ Line = renpy.random.choice(["You'd like me to use my feet again?",                 
                "So you'd like another footjob?",                 
                "Mmmm, some. . . [she rubs her foot along your leg]?", 
                "A little foot rub?"]) 
            ch_e "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if E_Forced:
            call EmmaFace("sad")
            call Statup("Emma", "Obed", 90, 1)
            call Statup("Emma", "Inbt", 60, 1)
            ch_e "Oh, fine." 
        elif "no foot" in E_DailyActions:               
            ch_e "Oh, very well."   
        else:
            call EmmaFace("sexy", 1)
            call Statup("Emma", "Love", 90, 1)
            call Statup("Emma", "Inbt", 50, 3) 
            $ Line = renpy.random.choice(["Sure, I suppose.",                 
                "Fine.",                 
                "Very well, bring it out.", 
                "I suppose I could. . .",
                "Fine. . . [She gestures for you to come over].",
                "Hmm, ok."]) 
            ch_e "[Line]"
            $ Line = 0
        call Statup("Emma", "Obed", 20, 1)
        call Statup("Emma", "Obed", 60, 1)
        call Statup("Emma", "Inbt", 70, 2) 
        jump E_FJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call EmmaFace("angry")
        if "no foot" in E_RecentActions:  
            ch_e "Pay attention, [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no foot" in E_DailyActions: 
            ch_e "I refuse to do this in public."  
        elif "no foot" in E_DailyActions:       
            ch_e "I said \"no,\" [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "I told you, not in public!"     
        elif not E_Foot:
            call EmmaFace("bemused")
            ch_e "I'm unsure, [E_Petname]. . ."
        else:
            call EmmaFace("bemused")
            ch_e "Not now, [E_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no foot" in E_DailyActions:
                call EmmaFace("bemused")
                ch_e "Thank you."              
                return
            "Maybe later?" if "no foot" not in E_DailyActions:
                call EmmaFace("sexy")  
                ch_e ". . ."
                ch_e "Perhaps."
                call Statup("Emma", "Love", 80, 2)
                call Statup("Emma", "Inbt", 70, 2)   
                if Taboo:                    
                    $ E_RecentActions.append("tabno")                      
                    $ E_DailyActions.append("tabno") 
                $ E_RecentActions.append("no foot")                      
                $ E_DailyActions.append("no foot")            
                return
            "I'd really appreciate it. . .":             
                if Approval:
                    call EmmaFace("sexy")     
                    call Statup("Emma", "Obed", 90, 2)
                    call Statup("Emma", "Obed", 50, 2)
                    call Statup("Emma", "Inbt", 70, 3) 
                    call Statup("Emma", "Inbt", 40, 2) 
                    $ Line = renpy.random.choice(["Sure, I suppose.",                 
                            "Fine.",                 
                            "Very well, bring it out.", 
                            "I suppose I could. . .",
                            "Fine. . . [She gestures for you to come over].",
                            "Hmm, ok."]) 
                    ch_e "[Line]"
                    $ Line = 0                   
                    jump E_FJ_Prep
                else:   
                    pass
                    
            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Emma", 400, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad")
                    call Statup("Emma", "Love", 70, -5, 1)
                    call Statup("Emma", "Love", 200, -2)                 
                    ch_e "Oh, very well."  
                    call Statup("Emma", "Obed", 50, 4)
                    call Statup("Emma", "Inbt", 80, 1) 
                    call Statup("Emma", "Inbt", 60, 3)  
                    $ E_Forced = 1  
                    jump E_FJ_Prep
                else:                              
                    call Statup("Emma", "Love", 200, -15)     
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Emma_Arms = 1 
    if "no foot" in E_DailyActions:
        call EmmaFace("angry", 1)
        ch_e "I won't repeat myself."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1)
        ch_e "You really don't want my heels near your manhood."
        call Statup("Emma", "Lust", 200, 5)    
        if E_Love > 300:   
                call Statup("Emma", "Love", 70, -2)
        call Statup("Emma", "Obed", 50, -2)    
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call EmmaFace("angry", 1)          
        $ E_DailyActions.append("tabno") 
        ch_e "This truly isn't an appropriate place for that."
        call Statup("Emma", "Lust", 200, 5)  
        call Statup("Emma", "Obed", 50, -3)   
    elif E_Foot:
        call EmmaFace("sad") 
        ch_e "I'm not in the mood, [E_Petname]. . ."       
    else:
        call EmmaFace("normal", 1)
        ch_e "I'm not in the mood for footplay today. . ."  
    $ E_RecentActions.append("no foot")                      
    $ E_DailyActions.append("no foot") 
    $ Tempmod = 0    
    return
    

label E_FJ_Prep:
    if Trigger2 == "foot": 
        return
    
    if Taboo:
        $ E_Inbt += int(Taboo/10)  
        $ E_Lust += int(Taboo/5)
                
    call EmmaFace("sexy")
    if E_Forced:
        call EmmaFace("sad")
    elif E_Foot:
        $ E_Brows = "confused"
        $ E_Eyes = "sexy"
        $ E_Mouth = "smile"
    
    call Seen_First_Peen("Emma",Partner)
    if not E_Foot:        
        if E_Forced:
            call Statup("Emma", "Love", 90, -20)
            call Statup("Emma", "Obed", 70, 25)
            call Statup("Emma", "Inbt", 80, 30) 
        else:
            call Statup("Emma", "Love", 90, 5)
            call Statup("Emma", "Obed", 70, 20)
            call Statup("Emma", "Inbt", 80, 20)     
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no foot")
    $ E_RecentActions.append("foot")                      
    $ E_DailyActions.append("foot") 
  
label E_FJ_Cycle:    
    while Round >=0:  
        call Shift_Focus("Emma") 
        call Emma_FJ_Launch   
        call EmmaLust   
        
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
                                    "I also want to fondle her thighs." if Trigger2 != "fondle thighs":
                                            if MultiAction:
                                                $ Trigger2 = "fondle thighs"
                                                "You start to fondle her thighs."
                                            else:
                                                ch_e "Hmm, I think we've probably done enough for now. . ."  
                                         
                                    "Shift primary action":
                                            if E_Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    if E_Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call E_FJ_After                
                                                                        call E_Blowjob
                                                                    else:
                                                                        ch_e "Hmm, I think we've probably done enough for now. . ."
                                                        "How about a handjob?":
                                                                    if E_Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call E_FJ_After                
                                                                        call E_Handjob
                                                                    else:
                                                                        ch_e "Hmm, I think we've probably done enough for now. . ."
                                                                        
                                                        "How about a titjob?":
                                                                    if E_Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call E_FJ_After
                                                                        call E_Titjob
                                                                    else:
                                                                        ch_e "Hmm, I think we've probably done enough for now. . ."
                                                                
                                                        "Never Mind":
                                                                jump E_FJ_Cycle
                                            else: 
                                                ch_e "Hmm, I think we've probably done enough for now. . ."           
                    
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
                                                        jump E_FJ_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump E_FJ_Cycle 
                                            "Never mind":
                                                        jump E_FJ_Cycle 
                                    "Undress Emma":
                                            call E_Undress   
                                    "Clean up Emma (locked)" if not E_Spunk:
                                            pass  
                                    "Clean up Emma" if E_Spunk:
                                            call Emma_Cleanup("ask")                                         
                                    "Never mind":
                                            jump E_FJ_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Emma_FJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_FJ_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Emma_FJ_Reset
                                    $ Line = 0
                                    jump E_FJ_After
        #End menu (if Line)
        
        call Shift_Focus("Emma")    
        call Sex_Dialog("Emma",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or E_Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PE_Cumming
                            if "angry" in E_RecentActions:  
                                call Emma_FJ_Reset
                                return    
                            call Statup("Emma", "Lust", 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_FJ_After 
                            $ Line = "came"
     
                    if E_Lust >= 100:  
                            #If Emma can cum                                             
                            call E_Cumming
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_FJ_After
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in E_RecentActions:#And Emma is unsatisfied,  
                                    "Emma still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it" 
                                        "No, I'm done.":
                                            "You pull back."
                                            jump E_FJ_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Emma")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if Cnt == 20:
                    $ E_Brows = "angry"        
                    menu:
                        ch_e "Hmm, foot cramp, could we take a short break?"
                        "How about a BJ?" if E_Action and MultiAction:
                                $ Situation = "shift"
                                call E_FJ_After
                                call E_Blowjob   
                        "How about a Handy?" if E_Action and MultiAction:
                                $ Situation = "shift"
                                call E_FJ_After
                                call E_Handjob  
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump E_FJ_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Emma_Sex_Reset
                                $ Situation = "shift"
                                jump E_FJ_After
                        "No, keep going.":
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):
                                    call Statup("Emma", "Love", 200, -5)
                                    call Statup("Emma", "Obed", 50, 3)                    
                                    call Statup("Emma", "Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    call EmmaFace("angry", 1)   
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_e "I do have better things I could be doing."                                               
                                    call Statup("Emma", "Love", 50, -3, 1)
                                    call Statup("Emma", "Love", 80, -4, 1)
                                    call Statup("Emma", "Obed", 30, -1, 1)                    
                                    call Statup("Emma", "Obed", 50, -1, 1)                     
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_FJ_After
        elif Cnt == 10 and E_SEXP <= 100 and not ApprovalCheck("Emma", 1200, "LO"):
                    $ E_Brows = "confused"
                    ch_e "Could we be done here, my feet are getting sore."         
        #End Count check
                   
        if Round == 10:
            ch_e "Ok, it's getting a bit lake here."   
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."      
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    ch_e "Ok, [E_Petname], that's enough of that for now."
    
label E_FJ_After:
    call EmmaFace("sexy") 
    
    $ E_Foot += 1  
    $ E_Action -=1
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1        
    call Statup("Emma", "Lust", 90, 5)
    
    call Partner_Like("Emma",1)
    
    if "Emmapedi" in Achievements:
            pass  
    elif E_Foot >= 10:
            call EmmaFace("smile", 1)
            ch_e "I'm glad that you enjoy my feet."
            ch_e "They've been trained well over the years."
            $ Achievements.append("Emmapedi")
            $ E_SEXP += 5          
    elif E_Foot == 1:            
            $ E_SEXP += 10
            if E_Love >= 500:
                $ E_Mouth = "smile"
                ch_e "Your cock was so warm . ."
            elif P_Focus <= 20:
                $ E_Mouth = "sad"
                ch_e "Did you enjoy that?"
    elif E_Foot == 5:
                ch_e "I'm enjoying this experience."                  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Ok then, what were you thinking?"
    else:
        call Emma_Sex_Reset    
    call Checkout
    return

## end E_Footjob //////////////////////////////////////////////////////////////////////

 
# Start E_Lesbian ////////////////////////////////////////////////////////////////////////
label E_Les_Interupted:  
        # Called if you catch them fucking 
        if "unseen" not in E_RecentActions:
                if E_Org < 3 and E_Action:                
                    menu:
                        "Did you want to stop them?"
                        "Yeah.":
                            pass
                        "No, let them keep going.":
                            $ E_Action -= 1 if E_Action > 0 else 0
                            jump E_Les_Cycle 
                else:
                    ch_e "Ok, that's probably enough of that. . ."
                jump E_Les_After
        call DrainWord("Emma","unseen",1,0) #She sees you, so remove unseens
        call DrainWord(Partner,"unseen",1,0) #She sees you, so remove unseens
        call EmmaFace("surprised", 2)
        "Suddenly, Emma looks up from what she was doing with a start, and gives [Partner] a nudge."
        call EmmaFace("sly",0)
        ch_e "Hmm? [E_Petname], enjoying the show?"
        $ E_Action -= 1 if E_Action > 0 else 0
        call Checkout(1)
        $ Line = 0
    
        #If you've been jacking it
        if Trigger2 == "jackin":
                $ E_Eyes = "down"
                menu:
                    ch_e "and was. . . that. .  really an appropriate reaction?"
                    "I couldn't help myself, it was an excellent show.":   
                            call EmmaFace("sexy")
                            call Statup("Emma", "Obed", 50, 3)
                            call Statup("Emma", "Obed", 70, 2)
                            "Emma glances over at [Partner]."
                            ch_e "I suppose it was. . ."
                            if E_Love >= 800 or E_Obed >= 500 or E_Inbt >= 500:
                                $ Tempmod += 10
                                call Statup("Emma", "Lust", 90, 5)
                                ch_e "And at least you make good eye candy. . ."  
                            
                    "I. . . just got here?":
                            call EmmaFace("angry")                   
                            call Statup("Emma", "Love", 70, 2)
                            call Statup("Emma", "Love", 90, 1)
                            call Statup("Emma", "Obed", 50, 2)
                            call Statup("Emma", "Obed", 70, 2)
                            "She looks pointedly at your cock,"
                            ch_e "I'm sure. . ."   
                            if E_Love >= 800 or E_Obed >= 500 or E_Inbt >= 500:
                                    $ Tempmod += 10
                                    call Statup("Emma", "Lust", 90, 5)
                                    call EmmaFace("bemused", 1)
                                    ch_e "not that I can blame you. . ."   
                            else:
                                    $ Tempmod -= 10
                                    call Statup("Emma", "Lust", 200, -5)
                call Seen_First_Peen("Emma",Partner) 
        else:         
                #you haven't been jacking it    
                menu:
                    ch_e "Have you been there long?"
                    "Long enough.":   
                            call EmmaFace("sexy", 1)
                            call Statup("Emma", "Obed", 50, 3)
                            call Statup("Emma", "Obed", 70, 2)
                            ch_e "I supppose we did make a show of ourselves. . ."
                    "I just got here.":
                            call EmmaFace("bemused", 1)
                            call Statup("Emma", "Love", 70, 2)
                            call Statup("Emma", "Love", 90, 1)                    
                            ch_e "I'm sure. . ."   
                            call Statup("Emma", "Obed", 50, 2)
                            call Statup("Emma", "Obed", 70, 2)    
                                
        if not ApprovalCheck("Emma", 1350):
                #If she doesn't like you enough to have you around. . .
                call Statup("Emma", "Love", 200, -5)
                call EmmaFace("angry")
                $ E_RecentActions.append("angry")
                $ E_DailyActions.append("angry")
                ch_e "So perhaps you could leave us to it?"
                $ renpy.pop_call()
                $ renpy.pop_call()
                if bg_current == "bg player":                                        
                    jump Campus_Map  
                else:
                    jump Player_Room  
        
        if Round <= 10:
            ch_e "I suppose it was time for a break. . ."
            return
        $ Situation = "interrupted"
    
label E_LesScene(Bonus = 0): #Repeating strokes
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Emma")
    if E_LesWatch:
        $ Tempmod += 10
    elif E_Les:
        $ Tempmod += 5
    if E_SEXP >= 50:
        $ Tempmod += 25
    elif E_SEXP >= 30:
        $ Tempmod += 15
    elif E_SEXP >= 15:
        $ Tempmod += 5
        
    if E_Lust >= 90:
        $ Tempmod += 5
    elif E_Lust >= 75:
        $ Tempmod += 5
        
    elif E_Inbt >= 750:
        $ Tempmod += 5
        
    if "exhibitionist" in E_Traits:      
        $ Tempmod += (3*Taboo) 
        
    if "dating" in E_Traits or "sex friend" in E_Petnames:
        $ Tempmod += 10        
    elif "ex" in E_Traits:
        $ Tempmod -= 40  
        
    if R_Loc == bg_current:
            #if it's Rogue. . .
            $ R_RecentActions.append("noticed Emma")
            $ E_RecentActions.append("noticed Rogue")
            $ Partner = "Rogue"  
            if E_LikeRogue >= 900:
                    $ Bonus += 150
            elif E_LikeRogue >= 800 or "poly Rogue" in E_Traits:
                    $ Bonus += 100
            elif E_LikeRogue >= 700:
                    $ Bonus += 50
            elif E_LikeRogue <= 200:
                    $ Bonus -= 200
            elif E_LikeRogue <= 500:
                    $ Bonus -= 100
            call DrainWord("Rogue","unseen",1,0) #She sees you, so remove unseens
    elif K_Loc == bg_current:
            #if it's Kitty. . .
            $ K_RecentActions.append("noticed Emma")
            $ E_RecentActions.append("noticed Kitty")
            $ Partner = "Kitty"  
            if E_LikeKitty >= 900:
                    $ Bonus += 150
            elif E_LikeKitty >= 800 or "poly Kitty" in E_Traits:
                    $ Bonus += 100
            elif E_LikeKitty >= 700:
                    $ Bonus += 50
            elif E_LikeKitty <= 200:
                    $ Bonus -= 200
            elif E_LikeKitty <= 500:
                    $ Bonus -= 100
            call DrainWord("Kitty","unseen",1,0) #She sees you, so remove unseens
    elif L_Loc == bg_current:
            #if it's Laura. . .
            $ L_RecentActions.append("noticed Emma")
            $ E_RecentActions.append("noticed Laura")
            $ Partner = "Laura"  
            if E_LikeLaura >= 900:
                    $ Bonus += 150
            elif E_LikeLaura >= 800 or "poly Laura" in E_Traits:
                    $ Bonus += 100
            elif E_LikeLaura >= 700:
                    $ Bonus += 50
            elif E_LikeLaura <= 200:
                    $ Bonus -= 200
            elif E_LikeLaura <= 500:
                    $ Bonus -= 100
            call DrainWord("Laura","unseen",1,0) #She sees you, so remove unseens
            
    if bg_current in ("bg player", "bg emma", "bg rogue", "bg kitty"):
        $ Taboo == 0
    if E_ForcedCount and not E_Forced:
        $ Tempmod -= 5 * E_ForcedCount   
        
    $ Approval = ApprovalCheck("Emma", 1350, TabM = 2, Bonus = Bonus) # 1350, 1500, 1650, Taboo -800
    
    call DrainWord("Emma","unseen",1,0) #She sees you, so remove unseens
    
    if Situation == "interrupted":    
        menu:
            extend ""
            "I guess I should probably get going then. . .":
                    call Statup("Emma", "Love", 80, 3)
                    if Approval >= 2:
                            # if Emma is very much in
                            ch_e "Well, if [Partner]'s game. . ."
                            if R_Loc == bg_current:
                                    call R_Les_Response("Emma",3,B2=Bonus)
                            elif K_Loc == bg_current:
                                    call K_Les_Response("Emma",3,B2=Bonus)
                            elif L_Loc == bg_current:
                                    call L_Les_Response("Emma",3,B2=Bonus) 
                            if not _return:
                                    return
                    else:
                            # If Emma is only so/so, but Rogue is on board, she tries to convince Emma
                            if R_Loc == bg_current:
                                    call R_Les_Response("Emma",1,B2=Bonus)  
                            elif K_Loc == bg_current:
                                    call K_Les_Response("Emma",1,B2=Bonus)
                            elif L_Loc == bg_current:
                                    call L_Les_Response("Emma",1,B2=Bonus)                            
                            if not _return:
                                    #this is the default reaction if Rogue is not into it either
                                    if Approval:
                                        ch_e "Well, you could at least stay for a bit. . ."
                                        return
                                    else:
                                        ch_e "I suppose. . ."  
                                        $ renpy.pop_call()
                                        $ renpy.pop_call()
                                        if bg_current == "bg player":                                        
                                            jump Campus_Map  
                                        else:
                                            jump Player_Room  
                            elif not Approval:
                                    ch_e "So sorry [E_Petname], I suppose we'd like to keep this private."
                                    return                            
                            elif not E_Action:
                                    ch_e "So sorry [E_Petname], I needed a break. . ."
                                    return        
                            else:
                                    ch_e "Very well."    
                    #if it passed the hurdles. . .
                    jump E_Les_Prep
            "So maybe I could join you girls?" if P_Semen and E_Action:
                    call EmmaFace("sexy")
                    ch_e "Oh? What do you bring to the table?"    
                    $ Situation = "join"
                    return                      #returns to sexmenu=
            "So maybe I could watch a bit longer?":
                    call EmmaFace("bemused", 1)   
    #End "Interrupted" content.
    
    #first time
    if not E_LesWatch:                                                                
            call EmmaFace("surprised", 1)
            $ E_Mouth = "kiss"
            ch_e "You wanna watch me and [Partner] \"engaged?\""
            if E_Forced:
                call EmmaFace("sad")
                ch_e "nothing more than that though?"
                
    if Approval and Partner == "Rogue" and "touch" not in R_Traits:
            ch_e "I'm not sure, Rogue's touch can be. . . disruptive?"
            ch_p "Don't worry, I can keep it turned off."
            ch_e "Oh, I suppose you can at that. . ."
                     
    if not E_LesWatch and Approval:   
            #First time dialog                                                       
            if E_Forced: 
                call EmmaFace("sad")
                call Statup("Emma", "Love", 70, -3, 1)
                call Statup("Emma", "Love", 20, -2, 1)
            elif Bonus >= 100:
                call EmmaFace("sly", Eyes="side")
                ch_e "This won't be my first time. . ."   
            elif E_Love >= (E_Obed + E_Inbt):
                call EmmaFace("sexy")
                $ E_Brows = "sad"
                $ E_Mouth = "smile" 
                ch_e "I hadn't considered this as one of your kinks. . ."          
            elif E_Obed >= E_Inbt:
                call EmmaFace("normal")
                ch_e "If this is what gets you off, [E_Petname]. . ."            
            else: # Uninhibited 
                call EmmaFace("sad")
                $ E_Mouth = "smile"             
                ch_e "I do enjoy an audience. . ."    
    
    
    elif Approval:            
                #Second time+ initial dialog                                                           
                if E_Forced: 
                        call EmmaFace("sad")
                        call Statup("Emma", "Love", 70, -3, 1)
                        call Statup("Emma", "Love", 20, -2, 1)
                        ch_e "You enjoyed the last show?"  
                elif Approval and "lesbian" in E_RecentActions:
                        call EmmaFace("sexy", 1)
                        ch_e "Hmm, back for more?"    
                        jump E_Les_Prep
                elif Approval and "lesbian" in E_DailyActions:
                        call EmmaFace("sexy", 1)
                        $ Line = renpy.random.choice(["You enjoyed the show?",       
                            "Didn't get enough earlier?",
                            "It is nice to have an audience. . ."]) 
                        ch_e "[Line]"            
                elif E_Mast < 3:        
                        call EmmaFace("sexy", 1)
                        $ E_Brows = "confused"
                        ch_e "You do like to watch."       
                else:       
                        call EmmaFace("sexy", 1)
                        $ Emma_Arms = 2
                        $ Line = renpy.random.choice(["You sure do like to watch.",                 
                            "So you'd like me to go again?",                 
                            "You want to watch some more?",
                            "You want me to engage with "+Partner+"?"]) 
                        ch_e "[Line]"
                        $ Line = 0                        
    #End second time+ initial dialog
    
    if Approval >= 2:      
                #If she's into it. . .                                                                            
                if E_Forced:
                    call EmmaFace("sad")
                    call Statup("Emma", "Obed", 90, 1)
                    call Statup("Emma", "Inbt", 60, 1)
                    ch_e "So long as she's alright it. . ." 
                else:
                    call EmmaFace("sexy", 1)
                    call Statup("Emma", "Love", 90, 1)
                    call Statup("Emma", "Inbt", 50, 3) 
                    $ Line = renpy.random.choice(["Well. . . ok.",                 
                        "I don't mind getting cozy with her. . .",
                        "I kinda needed this anyways. . .",
                        "Sure!", 
                        "I guess. . .",
                        "Heh, ok, fine."]) 
                    ch_e "[Line]"
                    $ Line = 0
                call Statup("Emma", "Obed", 20, 1)
                call Statup("Emma", "Obed", 60, 1)
                call Statup("Emma", "Inbt", 70, 2) 
                jump E_Les_Partner   
    #end instant approval
            
    else:       
        #If she's not into it, but maybe. . .                                                                                    
        menu:
            ch_e "I'm not sure about that, [E_Petname]."
            "Maybe later?":
                    call EmmaFace("sexy", 1)  
                    if Bonus >= 100:
                        call Statup("Emma", "Inbt", 90, 5)  
                        ch_e "Eventually. . ."
                    elif Bonus >= 0:
                        call LikeUpdater("Emma",3)
                        ch_e "One never knows. . ."
                    else:
                        call EmmaFace("angry", 1, Eyes="side") 
                        ch_e "Unlikely."
                    call EmmaFace("smile", 1) 
                    ch_e "I do appreciate your restraint."
                    call Statup("Emma", "Love", 80, 2)
                    call Statup("Emma", "Inbt", 70, 5)   
                    call Taboo_Level
                    return
                    
            "You look like you might be into it. . .":             
                    if Approval:
                            call EmmaFace("sexy")     
                            call Statup("Emma", "Obed", 90, 4)
                            call Statup("Emma", "Obed", 50, 5)
                            call Statup("Emma", "Inbt", 70, 4) 
                            call Statup("Emma", "Inbt", 40, 4) 
                            $ Line = renpy.random.choice(["Well. . . ok.",                 
                                    "I don't mind getting cozy with her. . .",
                                    "I kinda needed this anyways. . .",
                                    "Sure!", 
                                    "I guess. . .",
                                    "Heh, ok, fine."]) 
                            ch_e "[Line]"
                            $ Line = 0                   
                            jump E_Les_Partner
                    else:   
                            pass
                    
            "Just get at it already.":                                              
                    # Pressured into it
                    $ Approval = ApprovalCheck("Emma", 550, "OI", TabM = 2) # 55, 70, 85
                    if Approval > 1 or (Approval and E_Forced):
                            call EmmaFace("sad")
                            call Statup("Emma", "Love", 70, -5, 1)
                            call Statup("Emma", "Love", 200, -5)                 
                            ch_e "Oh, fine."  
                            call Statup("Emma", "Obed", 80, 4)
                            call Statup("Emma", "Inbt", 80, 1) 
                            call Statup("Emma", "Inbt", 60, 3)  
                            $ E_Forced = 1  
                            jump E_Les_Partner
                    else:                              
                            call Statup("Emma", "Love", 200, -20)     
                            $ E_RecentActions.append("angry")
                            $ E_DailyActions.append("angry")
    # end of asking her to do it
    
    if R_Loc == bg_current:
            call R_Les_Response("Emma",1,B2=Bonus)
    elif K_Loc == bg_current:
            call K_Les_Response("Emma",1,B2=Bonus)
    elif L_Loc == bg_current:
            call L_Les_Response("Emma",1,B2=Bonus)
    if _return:
            #if the other girl convinces her
            call EmmaFace("smile", 1)
            ch_e "Well, if you insist, dear."
            call EmmaFace("sly", 1)
            ch_e "Get over here. . ."
            jump E_Les_Prep
            
            
    #She refused all offers.
    $ Emma_Arms = 1  
    if not Partner:
            ch_e "Well, I can't exactly do this alone. . ."
    elif E_Forced:
            call EmmaFace("angry", 1)
            ch_e "I'm just not into that."
            call Statup("Emma", "Lust", 90, 5)         
            if E_Love > 300:
                call Statup("Emma", "Love", 70, -2)
            call Statup("Emma", "Obed", 50, -2)    
            $ E_RecentActions.append("angry")
            $ E_DailyActions.append("angry")  
    elif Taboo:                            
            # she refuses and this is too public a place for her
            call EmmaFace("angry", 1)          
            $ E_DailyActions.append("tabno") 
            ch_e "Totally not around here."     
            call Statup("Emma", "Lust", 90, 5)  
            call Statup("Emma", "Obed", 50, -3) 
    elif E_Les:
            call EmmaFace("sad") 
            if Bonus >= 100:
                ch_e "I'm not really comfortable with that."     
            else:    
                ch_e "I don't think I'm ready for an audience."     
    else:
            call EmmaFace("normal", 1)
            ch_e "No way."  
    $ E_RecentActions.append("no lesbian")                      
    $ E_DailyActions.append("no lesbian") 
    $ Tempmod = 0 
    call Taboo_Level
    return
    
label E_Les_Partner:
    # This checks to see if the other girl is into it. 
    if R_Loc == bg_current:
            call R_Les_Response("Emma",2)
            if not _return:
                    # If Rogue refused
                    return
    elif K_Loc == bg_current:
            call K_Les_Response("Emma",2)
            if not _return:
                    # If Kitty refused
                    return
    elif L_Loc == bg_current:
            call L_Les_Response("Emma",2)
            if not _return:
                    # If Laura refused
                    return
            
label E_Les_Prep:    
    #sets the scene up   
    
    if R_Loc == bg_current:
            if "noticed Emma" not in R_RecentActions:
                    $ R_RecentActions.append("noticed Emma")    
            if "noticed Rogue" not in E_RecentActions:
                    $ E_RecentActions.append("noticed Rogue")           
            $ Partner = "Rogue"  
    elif K_Loc == bg_current:
            if "noticed Emma" not in K_RecentActions:
                    $ K_RecentActions.append("noticed Emma")    
            if "noticed Kitty" not in E_RecentActions:
                    $ E_RecentActions.append("noticed Kitty")         
            $ Partner = "Kitty"  
    elif L_Loc == bg_current:
            if "noticed Emma" not in L_RecentActions:
                    $ L_RecentActions.append("noticed Emma")  
            if "noticed Laura" not in E_RecentActions:
                    $ E_RecentActions.append("noticed Laura")           
            $ Partner = "Laura" 
            
    if "unseen" not in E_RecentActions:
            #if she knows you're there. . .
            call EmmaFace("sexy")
            $ Emma_Arms = 2
            "Emma move's closer to [Partner] and wraps her arms around her neck."
            if not E_LesWatch:
                    #First time        
                    if E_Forced:
                        call Statup("Emma", "Love", 90, -20)
                        call Statup("Emma", "Obed", 70, 55)
                        call Statup("Emma", "Inbt", 80, 55) 
                    else:
                        call Statup("Emma", "Love", 90, 5)
                        call Statup("Emma", "Obed", 70, 20)
                        call Statup("Emma", "Inbt", 80, 60)  
            call E_Les_FirstKiss
            $ Trigger3 == "kiss girl"
            $ Trigger4 == "kiss girl"
        
    $ Trigger = "lesbian"   
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0 
    $ Line = 0
    if Taboo:
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no lesbian")
    $ E_RecentActions.append("lesbian")                      
    $ E_DailyActions.append("lesbian") 
    
label E_Les_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Emma")
        call Les_Launch("Emma")  
        call EmmaLust     

        if  P_Focus < 100:                                                    
                    #Player Command menu
                    menu:
                        "Keep watching. . .":
                                    pass
                                   
                        "\"Ahem. . .\"" if "unseen" in E_RecentActions:  
                                jump E_Les_Interupted   
                                
                        "Start jack'in it." if Trigger2 != "jackin":
                                call E_Jackin                   
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
                                            if E_Action and MultiAction:
                                                call Emma_Offhand_Set
                                                if Trigger2:
                                                     $ E_Action -= 1
                                            else:
                                                ch_e "I'm rather exhausted, so perhaps we could take a break?"  
                                            
                                    "Threesome actions":   
                                        menu:
                                            "Ask Emma to do something else with [Partner]":
                                                    if "unseen" in E_RecentActions:
                                                            ch_p "Oh yeah, why don't you. . ."
                                                            jump E_Les_Interupted
                                                    else:                        
                                                            call Emma_Les_Change
                                            "Ask [Partner] to do something else":
                                                    if "unseen" in E_RecentActions:
                                                            ch_p "Oh yeah, why don't you. . ."
                                                            jump E_Les_Interupted
                                                    else:                        
                                                        call Partner_Threechange("Emma")    
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                    if "unseen" in E_RecentActions:
                                                            ch_p "Oh, that's good. . ."
                                                            jump E_Les_Interupted
                                                    else:                        
                                                            $ ThreeCount = 0     
                                                            
#                                            "Swap to [Partner]":
#                                                        call Trigger_Swap("Emma")
                                            "Undress [Partner]":
                                                    if "unseen" in E_RecentActions:
                                                            ch_p "Oh, yeah, take it off. . ."
                                                            jump E_Les_Interupted
                                                    else:                      
                                                            call Partner_Undress
                                                            jump E_Les_Cycle 
                                            "Clean up Partner":
                                                    if "unseen" in E_RecentActions:
                                                            ch_p "You've got a little something. . ."
                                                            jump E_Les_Interupted
                                                    else:                        
                                                            call Partner_Cleanup
                                                            jump E_Les_Cycle 
                                            "Never mind":
                                                        jump E_Les_Cycle 
                                    "Undress Emma":
                                            if "unseen" in E_RecentActions:
                                                    ch_p "Oh yeah, why don't you. . ."
                                                    jump E_Les_Interupted
                                            else:                        
                                                    call E_Undress   
                                    "Clean up Emma (locked)" if not E_Spunk:
                                            pass  
                                    "Clean up Emma" if E_Spunk:
                                            if "unseen" in E_RecentActions:
                                                ch_p "You've got a little something. . ."
                                                jump E_Les_Interupted
                                            else:                        
                                                call Emma_Cleanup("ask")                                         
                                    "Never mind":
                                            jump E_Les_Cycle  
                                            
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call E_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_Les_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call E_Pos_Reset
                                    $ Line = 0
                                    jump E_Les_After   
        #End menu (if Line)
        
        call Shift_Focus("Emma")    
        call Sex_Dialog("Emma",Partner)
        
        $ Cnt += 1
        $ Round -= 1
             
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or E_Lust >= 100:    
                    #If either of you can cum:
                    if P_Focus >= 100:
                            #If you can cum:  
                            if "unseen" not in E_RecentActions: #if she knows you're there
                                call PE_Cumming
                                if "angry" in E_RecentActions:  
                                    call E_Pos_Reset
                                    return    
                                call Statup("Emma", "Lust", 200, 5) 
                                if 100 > E_Lust >= 70 and E_OCount < 2:             
                                    $ E_RecentActions.append("unsatisfied")                      
                                    $ E_DailyActions.append("unsatisfied") 
                                $ Line = "came"
                            else: #If she wasn't aware you were there
                                "You grunt and try to hold it in."
                                $ P_Focus = 95
                                jump E_Les_Interupted
     
                    if E_Lust >= 100: 
                            #If Emma can cum                                              
                            call E_Cumming
                            jump E_Les_Interupted
                       
                    if Line == "came": 
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."      
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Emma")                                        
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if "unseen" in E_RecentActions:
                if Round == 10:
                    "It's getting a bit late, Emma and [Partner] will probably be wrapping up soon."  
                elif Round == 5:
                    "They're definitely going to stop soon."
        else:
                if Round == 10:
                    ch_e "We should wrap this up, it's getting late." 
                elif Round == 5:
                    ch_e "It will be time to stop soon."   
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    if "unseen" not in E_RecentActions:
        ch_e "Ok, [E_Petname], that's enough for now."
    

label E_Les_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call E_Pos_Reset
        
    call EmmaFace("sexy") 
        
    if Partner == "Kitty":
        call Partner_Like("Emma",4,2)
    else:
        call Partner_Like("Emma",3)
            
    $ E_LesWatch += 1 
    if E_LesWatch == 1:            
            $ E_SEXP += 15    
            if E_Love >= 500 and E_Org:
                    ch_e "I do enjoy an audience. . ." 
                    call EmmaFace("sly",1) 
                    ch_e "something to keep in mind?"
    
    if not Situation:
            ch_e "That was enjoyable. . ."
            if R_Loc == bg_current:
                if "les emma" not in R_History:
                        if E_LikeRogue >= 600:
                                ch_e "You were delightful dear!"
                        else:
                                ch_e "At least you could keep up. . ."
                        if R_LikeEmma >= 600:
                                ch_r "Um, yeah, you too. . ."
                        else:
                                ch_r "I guess. . ."
                        $ E_History.append("les rogue")   
                        $ R_History.append("les emma")  
                else:
                    #second time
                    ch_r "Mmmm yeah. . ."
            elif K_Loc == bg_current:
                if "les emma" not in K_History:
                        if E_LikeKitty >= 600:
                                ch_e "You were delightful dear!"
                        else:
                                ch_e "At least you could keep up. . ."
                        if K_LikeEmma >= 600:
                                ch_r "Yeah, that was. . . wow."
                        else:
                                ch_k "Sure, whatever. . ."
                        $ E_History.append("les kitty")   
                        $ K_History.append("les emma")  
                else:
                    #second time
                    ch_k "Oh yeah. . ."
            elif L_Loc == bg_current:
                if "les kitty" not in L_History:
                        if E_LikeLaura >= 600:
                                ch_e "You were delightful dear!"
                        else:
                                ch_e "At least you could keep up. . ."
                        if L_LikeEmma >= 600:
                                ch_l "Yeah, I try. . ."
                        else:
                                ch_l "Uh-huh."
                        $ K_History.append("les laura")   
                        $ L_History.append("les kitty") 
                else:
                    #second time
                    ch_l "Yup. . ."
                    
                        
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_e "So what else did you have in mind?"
    call Checkout
    return   

# End R LesScene


    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

label Emma_Les_Change(D20S=0, Secondary=Partner, Primary = "Emma", PrimaryLust=0, SecondaryLust=0):
        # for Lesbian primary activity: Emma_Threeway_Set("preset", "lesbian", Trigger3, ActiveGirl)
        #this is called when the player wants to change over a lesbian T3 behavior.
        $ Line = 0
        menu:
            "Hey Emma. . ."
            "why don't you kiss her?" if Trigger5 != "kiss girl" and Trigger5 != "kiss both":
                    call Emma_Threeway_Set("kiss girl", "lesbian", Trigger3)
            "why don't you grab her tits?" if Trigger3 != "fondle breasts":
                    call Emma_Threeway_Set("fondle breasts", "lesbian", Trigger3)
            "why don't you suck her breasts?" if Trigger3 != "suck breasts":
                    call Emma_Threeway_Set("suck breasts", "lesbian", Trigger3)
            "why don't you finger her?" if Trigger3 != "fondle pussy":
                    call Emma_Threeway_Set("fondle pussy", "lesbian", Trigger3)
            "why don't you go down on her?" if Trigger3 != "lick pussy":
                    call Emma_Threeway_Set("lick pussy", "lesbian", Trigger3)
            "why don't you grab her ass?" if Trigger3 != "fondle ass":
                    call Emma_Threeway_Set("fondle ass", "lesbian", Trigger3)
            "why don't you lick her ass?" if Trigger3 != "lick ass":
                    call Emma_Threeway_Set("lick ass", "lesbian", Trigger3) 
            "never mind.":
                pass
        if not Line:
            $ Line = "You return to what you were doing." 
        else:
            $ Situation = "skip"
        "[Line]"
        return

label Emma_Three_Change(ActiveGirl = "Rogue", D20S=0, Secondary="Emma", PrimaryLust=0, SecondaryLust=0):
        #this is called when the player wants to change over a threeway behavior.
        # for Threeway secondary activity: Emma_Threeway_Set("preset", 0, Trigger4, "ActiveGirl")        
        menu E_Three_Change:
            ch_p "Hey Emma. . ."
            "about [ActiveGirl]. . .":
                menu:
                    ch_p "about [ActiveGirl]. . ."
                    "why don't you kiss her?" if Trigger5 != "kiss girl" and Trigger5 != "kiss both":
                            call Emma_Threeway_Set("kiss girl", 0, Trigger4, ActiveGirl)                            
                    "why don't you grab her tits?" if Trigger4 != "fondle breasts":
                            call Emma_Threeway_Set("fondle breasts",0, Trigger4, ActiveGirl)                    
                    "why don't you suck her breasts?" if Trigger4 != "suck breasts":
                            call Emma_Threeway_Set("suck breasts",0, Trigger4, ActiveGirl)                            
                    "why don't you finger her?" if Trigger4 != "fondle pussy":
                            call Emma_Threeway_Set("fondle pussy",0, Trigger4, ActiveGirl)                            
                    "why don't you go down on her?" if Trigger4 != "lick pussy":
                            call Emma_Threeway_Set("lick pussy", 0, Trigger4, ActiveGirl)                            
                    "why don't you grab her ass?" if Trigger4 != "fondle ass":
                            call Emma_Threeway_Set("fondle ass", 0, Trigger4, ActiveGirl)                            
                    "why don't you lick her ass?" if Trigger4 != "lick ass":
                            call Emma_Threeway_Set("lick ass", 0, Trigger4, ActiveGirl)
                    "wait, I meant. . .":
                            jump E_Three_Change
                    
            "about me. . .":
                menu:
                    ch_p "about me. . ."
                    "why don't you kiss me?" if Trigger5 != "kiss you" and Trigger5 != "kiss both":
                            call Emma_Threeway_Set("kiss you", 0, Trigger4, ActiveGirl)                            
                    "maybe take me in hand?" if Trigger4 != "hand":
                            call Emma_Threeway_Set("hand", 0, Trigger4, ActiveGirl)                            
                    "maybe give me a lick?" if Trigger4 != "blow":
                            call Emma_Threeway_Set("blow", 0, Trigger4, ActiveGirl)
                    "wait, I meant. . .":
                            jump E_Three_Change
            "never mind.":
                pass
        return

#Start E_Les_Response >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >
label E_Les_Response(Girl="Rogue", Step=1, B=0, B2=0, Tempmod=0, Result=0, Approval = 0):
        #Dialog for responses to Lesbian scenes, Girl is the initial girl in the scene. Step is the phase of the conversation
        # call E_Les_Response("Rogue",1)
        
        
        if "three" not in E_History or "classcaught" not in E_History or (Taboo > 20 and "taboo" not in E_History): 
                #if she's not open to public sex yet, bailout
                $ E_RecentActions.append("no lesbian")                      
                $ E_DailyActions.append("no lesbian") 
                call Statup("Emma", "Obed", 70, 5)
                call Statup("Emma", "Inbt", 80, 5)  
                call Statup("Emma", "Lust", 50, 10)  
                call EmmaFace("sadside", 1)
                "Emma looks around furtively."
                ch_e "I can't imagine why you would think I would engage in such behavior with a student!"            
                call Remove_Girl("Emma")
                "She quickly leaves the room."
                return 0
        
        if E_Les:
            $ Tempmod += 10
        if E_SEXP >= 50:
            $ Tempmod += 25
        elif E_SEXP >= 30:
            $ Tempmod += 15
        elif E_SEXP >= 15:
            $ Tempmod += 5
                    
        elif E_Inbt >= 750:
            $ Tempmod += 5
            
        if "exhibitionist" in E_Traits:      
            $ Tempmod += (3*Taboo) 
            
        if "dating" in E_Traits or "sex friend" in E_Petnames:
            $ Tempmod += 10        
        elif "ex" in E_Traits:
            $ Tempmod -= 40  
            
        if Girl == "Rogue":
                #if it's Rogue. . .
                if E_LikeRogue >= 900:
                        $ B += 150
                elif E_LikeRogue >= 800 or "poly Rogue" in E_Traits:
                        $ B += 100
                elif E_LikeRogue >= 700:
                        $ B += 50
                elif E_LikeRogue <= 200:
                        $ B -= 200
                elif E_LikeRogue <= 500:
                        $ B -= 100
        elif Girl == "Kitty":
                #if it's Kitty. . .
                if E_LikeKitty >= 900:
                        $ B += 150
                elif E_LikeKitty >= 800 or "poly Kitty" in E_Traits:
                        $ B += 100
                elif E_LikeKitty >= 700:
                        $ B += 50
                elif E_LikeKitty <= 200:
                        $ B -= 200
                elif E_LikeKitty <= 500:
                        $ B -= 100
        elif Girl == "Laura":
                #if it's Laura. . .
                if E_LikeLaura >= 900:
                        $ B += 150
                elif E_LikeLaura >= 800 or "poly Laura" in E_Traits:
                        $ B += 100
                elif E_LikeLaura >= 700:
                        $ B += 50
                elif E_LikeLaura <= 200:
                        $ B -= 200
                elif E_LikeLaura <= 500:
                        $ B -= 100
                        
        $ Approval = ApprovalCheck("Emma", 1300, TabM = 2, Bonus = B) # 1300, 1450, 1600, Taboo -800
        
        if Step == 1:
            #this is if the first girl's check failed, but Emma likes her.
            if Approval >= 2 or (Approval and B >= 150):
                call EmmaFace("sexy", 1)
                ch_e "Oh come on [Girl], I could show you a few things."
                if B2 >= 100:
                    $ Result = 1
                    if Girl == "Rogue":
                            $ E_LikeRogue += (int(B/10))
                            $ R_LikeEmma += (int(B2/10))
                    elif Girl == "Kitty":
                            $ E_LikeKitty += (int(B/10))
                            $ K_LikeEmma += (int(B2/10))
                    elif Girl == "Laura":
                            $ E_LikeLaura += (int(B/10))
                            $ L_LikeEmma += (int(B2/10))
            else:
                return Result
        
        if Step == 2:
            #this is the second step, usually in the Prep phase
            if Approval >= 2:
                call EmmaFace("smile", 1)
                ch_e "Of course, [E_Petname]."
                $ Result = 1
            elif Approval:
                call EmmaFace("sly", 2)
                if B >= 100:
                        ch_e "Mmmmm, certainly. . ."
                if B >= 0:
                        ch_e "[Girl], dear, I don't really think so. . ."
                $ E_Blush = 1
                menu:
                    extend ""
                    "Ok, that's fine. . .":
                            if B >= 100:                            
                                ch_e "Oh, don't back out now. . ."
                                $ Result = 1
                            else:
                                call EmmaFace("smile")
                                ch_e "I appreciate your restraint."
                    "Come on, you might enjoy it. . .":
                            if B >= 50:
                                ch_e "I'm sure I would. . ." 
                                $ Result = 1
                            else:
                                call EmmaFace("sad", 2)
                                ch_e "Probably not." 
                    "Get in there, now.":
                            if ApprovalCheck("Emma", 550, "OI", TabM = 2):
                                call EmmaFace("sadside", 1)
                                ch_e "Oh, fine."
                                $ Result = 1
                            else:
                                call EmmaFace("angry")
                                ch_e "Don't forget who's in charge here, [E_Petname]"  
                                $ E_RecentActions.append("angry")
                                $ E_DailyActions.append("angry")
                    "[Girl], what do you think?":
                            if Girl == "Rogue":
                                call RogueFace("sexy", 1)
                                if R_Les and E_Les:
                                        ch_r "You could do that thing from last time. . ."
                                else:
                                        ch_r "I was hoping you could give me some after class lessons. . ."
                                $ E_LikeRogue += (int(B/10))
                                if B >= 50:
                                        $ R_LikeEmma += 5
                            elif Girl == "Kitty":
                                call KittyFace("sexy", 1)
                                if K_Les and E_Les:
                                        ch_k "I mean, it might be nice to show [K_Petname] what you've taught me. . ."
                                else:
                                        ch_k "I've seen you watching me in class. . ."
                                $ E_LikeKitty += (int(B/10))
                                if B >= 50:
                                        $ K_LikeEmma += 5
                            elif Girl == "Laura":
                                call LauraFace("sexy", 1)
                                if L_Les and E_Les:
                                        ch_l "Wow, you aren't this shy when [L_Petname]'s not around."
                                else:
                                        ch_l "Come on, you look really squishy."
                                $ E_LikeLaura += (int(B/10))
                                if B >= 50:
                                        $ L_LikeEmma += 5
                            if B >= 50:
                                call EmmaFace("smile", 1)
                                ch_e "If we must, [Girl]."
                                $ Result = 1
                            else:
                                call EmmaFace("angry", 1, Eyes="side")
                                ch_e "I'm sorry [Girl], it's really not you."
            if Step == 3:
                    #This is a check if you interrupted them and Primary wants to do it, does Secondary?
                    if Approval:
                            call EmmaFace("smile", 1)
                            ch_e "How could I back out now?"
                            $ Result = 1
                    else:
                            call EmmaFace("sadside", 1)
                            ch_e "I'm afraid not. . ."
            
            if not Result:      
                #no approval
                $ E_RecentActions.append("no lesbian")                      
                $ E_DailyActions.append("no lesbian") 
                call EmmaFace("sadside", 1)
                if B <= 0:
                    ch_e "I'm sorry, [E_Petname], she's just not my type."
                if Taboo:
                    ch_e "I'm sorry, [E_Petname], this would cause a scandal."
                if B >= 100:
                    ch_e "I'm sorry, [E_Petname], not with an audience. . ."
                else:
                    ch_e "I'm sorry, [E_Petname], I'm just not interested in that."
                
        return Result
#End E_Les_Response >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >


label E_Les_FirstKiss:
    # called when there is a first kiss situation between two girls
    if Partner == "Rogue":
            if "les rogue" in E_History:
                #if they've been together before              
                $ Line = "experienced"
            elif E_Les and R_Les:   
                #if both have kissed girls before
                $ Line = "first both"
            elif E_Les:
                #Emma's had experience              
                $ Line = "first girl"
            elif R_Les:
                #Rogue's had experience                
                $ Line = "first partner"
    elif Partner == "Kitty":
            if "les kitty" in E_History:
                #if they've been together before              
                $ Line = "experienced"
            elif E_Les and K_Les:   
                #if both have kissed girls before
                $ Line = "first both"
            elif E_Les:
                #Emma's had experience              
                $ Line = "first girl"
            elif K_Les:
                #Kitty's had experience                
                $ Line = "first partner"
    elif Partner == "Laura":
            if "les laura" in E_History:
                #if they've been together before              
                $ Line = "experienced"
            elif E_Les and L_Les:   
                #if both have kissed girls before
                $ Line = "first both"
            elif E_Les:
                #Emma's had experience              
                $ Line = "first girl"
            elif L_Les:
                #Laura's had experience                
                $ Line = "first partner"
    
    if Line == "experienced":
            "Emma and [Partner] move together in a passionate kiss."
            "Emma's arms firmly grasp [Partner]'s neck and pull her close."
    else:
            if Line in ("first both", "first girl"):
                # Emma's first time
                "Emma tentatively moves in and gives [Partner] a soft kiss."
            else:
                #not Emma's first time
                "Emma casually places a hand on the back of [Partner]'s head and draws their lips together."
            if Line == "first partner":
                #other girl's first time
                "[Partner] pulls back a bit, but slowly leans into the enbrace."
            else:
                #not other girl's first time
                "[Partner]'s lips curl up into a smile and she draws Emma even closer."                    
            "After a few seconds, it begins to grow more passionate."
    return