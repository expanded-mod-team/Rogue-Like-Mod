﻿## R_Handjob //////////////////////////////////////////////////////////////////////
label R_Handjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Rogue")
    if R_Hand >= 7: # She loves it
        $ Tempmod += 10
    elif R_Hand >= 3: #You've done it before several times
        $ Tempmod += 7
    elif R_Hand: #You've done it before
        $ Tempmod += 3
        
    if R_Addict >= 75 and R_Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 15
    if R_Addict >= 75:
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 15
    if "exhibitionist" in R_Traits:
        $ Tempmod += (3*Taboo)    
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 40 
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount    
    
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no hand" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no hand" in R_RecentActions else 0    
        
    $ Approval = ApprovalCheck("Rogue", 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)
    
    if Situation == "Rogue":                                                                  #Rogue auto-starts   
        if Approval > 2:                                                      # fix, add rogue auto stuff here
            if Trigger2 == "jackin":
                "Rogue brushes your hand aside and starts stroking your cock."
            else:
                "Rogue gives you a mischevious smile, and starts to fondle your cock."
            menu:
                "What do you do?"
                "Nothing.":                    
                    call Statup("Rogue", "Inbt", 70, 3) 
                    call Statup("Rogue", "Inbt", 30, 2)                     
                    "Rogue continues her actions."
                "Praise her.":       
                    call RogueFace("sexy", 1)                    
                    call Statup("Rogue", "Inbt", 70, 3) 
                    ch_p "Oooh, that's good, [R_Pet]."
                    call Rogue_Namecheck
                    "Rogue continues her actions."
                    call Statup("Rogue", "Love", 80, 1)
                    call Statup("Rogue", "Obed", 90, 1)
                    call Statup("Rogue", "Obed", 50, 2)
                "Ask her to stop.":
                    call RogueFace("surprised")       
                    call Statup("Rogue", "Inbt", 70, 1) 
                    ch_p "Let's not do that for now, [R_Pet]."
                    call Rogue_Namecheck
                    "Rogue puts it down."
                    call Statup("Rogue", "Obed", 90, 1)
                    call Statup("Rogue", "Obed", 50, 1)
                    call Statup("Rogue", "Obed", 30, 2)
                    return            
            if Trigger:
                $ Trigger3 = "hand"
                return
            jump RHJ_Prep
        else:                
            $ Tempmod = 0                               # fix, add rogue auto stuff here
            $ Trigger2 = 0
            return            
    
    if not R_Hand and "no hand" not in R_RecentActions:        
        call RogueFace("surprised", 1)
        $ R_Mouth = "kiss"
        ch_r "You want me to rub your cock, with my hand?"
            
    if not R_Hand and Approval:                                                 #First time dialog        
        if R_Forced: 
            call RogueFace("sad")
            call Statup("Rogue", "Love", 70, -3, 1)
            call Statup("Rogue", "Love", 20, -2, 1)
        elif R_Love >= (R_Obed + R_Inbt):
            call RogueFace("sexy")
            $ R_Brows = "sad"
            $ R_Mouth = "smile" 
            ch_r "Well, I've never really been able to touch people without draining them, this could be an interesting experience. . ."            
        elif R_Obed >= R_Inbt:
            call RogueFace("normal")
            ch_r "If that's what you want, [R_Petname]. . ."            
        elif R_Addict >= 50:
            call RogueFace("manic", 1)
            ch_r "I think, if I could just touch that. . ."  
        else: # Uninhibited 
            call RogueFace("sad")
            $ R_Mouth = "smile"             
            ch_r "Hmm, could be fun. . ."    
            
    elif Approval:                                                                       #Second time+ dialog
        if R_Forced: 
            call RogueFace("sad")
            call Statup("Rogue", "Love", 70, -3, 1)
            call Statup("Rogue", "Love", 20, -2, 1)
            ch_r "That's really what you want?" 
        elif not Taboo and "tabno" in R_DailyActions:        
            ch_r "Ok, I guess this is private enough. . ."    
        elif "hand" in R_RecentActions:
            call RogueFace("sexy", 1)
            ch_r "Mmm, again? Let me flex my hand a bit. . ."
            jump RHJ_Prep
        elif "hand" in R_DailyActions:
            call RogueFace("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",   
                "You're going to give me calluses.", 
                "Didn't get enough earlier?",
                "My arm's still a bit sore from earlier.",
                "My arm's still a bit sore from earlier."]) 
            ch_r "[Line]"
        elif R_Hand < 3:        
            call RogueFace("sexy", 1)
            $ R_Brows = "confused"
            $ R_Mouth = "kiss"
            ch_r "So you'd like another handy?"        
        else:       
            call RogueFace("sexy", 1)
            $ Rogue_Arms = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                "So you'd like another handy?",                 
                "A little. . . [fist pumping hand gestures]?", 
                "You want me to grease your skids?",
                "A little tender loving care?"]) 
            ch_r "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if R_Forced:
            call RogueFace("sad")
            call Statup("Rogue", "Obed", 90, 1)
            call Statup("Rogue", "Inbt", 60, 1)
            ch_r "Ok, fine." 
        elif "no hand" in R_DailyActions:               
            ch_r "I guess if it'll get you off. . ."   
        else:
            call RogueFace("sexy", 1)
            call Statup("Rogue", "Love", 90, 1)
            call Statup("Rogue", "Inbt", 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, put'im here.",                 
                "Well. . . ok.",                 
                "I suppose, drop trou.", 
                "I guess I could. . . whip it out.",
                "Fine. . . [She gestures for you to come over].",
                "Heh, ok, ok."]) 
            ch_r "[Line]"
            $ Line = 0
        call Statup("Rogue", "Obed", 20, 1)
        call Statup("Rogue", "Obed", 60, 1)
        call Statup("Rogue", "Inbt", 70, 2) 
        jump RHJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call RogueFace("angry")
        if "no hand" in R_RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions and "no hand" in R_DailyActions: 
            ch_r "I already told you that I wouldn't jerk you off in public!"  
        elif "no hand" in R_DailyActions:       
            ch_r "I already told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions:  
            ch_r "I already told you this is too public!"     
        elif not R_Hand:
            call RogueFace("bemused")
            ch_r "I don't really want to touch it, [R_Petname]. . ."
        else:
            call RogueFace("bemused")
            ch_r "Not, right now [R_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no hand" in R_DailyActions:
                call RogueFace("bemused")
                ch_r "Fine."              
                return
            "Maybe later?" if "no hand" not in R_DailyActions:
                call RogueFace("sexy")  
                ch_r "I'll give it some thought, [R_Petname]."
                call Statup("Rogue", "Love", 80, 2)
                call Statup("Rogue", "Inbt", 70, 2)   
                if Taboo:                    
                    $ R_RecentActions.append("tabno")                      
                    $ R_DailyActions.append("tabno") 
                $ R_RecentActions.append("no hand")                      
                $ R_DailyActions.append("no hand")            
                return
            "I'd really appreciate it. . .":             
                if Approval:
                    call RogueFace("sexy")     
                    call Statup("Rogue", "Obed", 90, 2)
                    call Statup("Rogue", "Obed", 50, 2)
                    call Statup("Rogue", "Inbt", 70, 3) 
                    call Statup("Rogue", "Inbt", 40, 2) 
                    $ Line = renpy.random.choice(["Sure, put'im here.",                 
                        "No Problem.",                 
                        "Sure. Drop trou.", 
                        "I suppose, whip it out.",
                        "Ok, [She gestures for you to come over].",
                        "Heh, ok."]) 
                    ch_r "[Line]"
                    $ Line = 0                   
                    jump RHJ_Prep
                else:   
                    pass
                    
            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Rogue", 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and R_Forced):
                    call RogueFace("sad")
                    call Statup("Rogue", "Love", 70, -5, 1)
                    call Statup("Rogue", "Love", 200, -2)                 
                    ch_r "Ok, fine, whip it out."  
                    call Statup("Rogue", "Obed", 50, 4)
                    call Statup("Rogue", "Inbt", 80, 1) 
                    call Statup("Rogue", "Inbt", 60, 3)  
                    $ R_Forced = 1  
                    jump RHJ_Prep
                else:                              
                    call Statup("Rogue", "Love", 200, -15)     
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Rogue_Arms = 1 
    if "no hand" in R_DailyActions:
        call RogueFace("angry", 1)
        ch_r "I just don't want to, [R_Petname]."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1)
        ch_r "I'm not that kind of girl!"
        call Statup("Rogue", "Lust", 200, 5)    
        if R_Love > 300: 
                call Statup("Rogue", "Love", 70, -2)
        call Statup("Rogue", "Obed", 50, -2)    
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call RogueFace("angry", 1)          
        $ R_DailyActions.append("tabno") 
        ch_r "I really don't think this is the right place for that!"
        call Statup("Rogue", "Lust", 200, 5)  
        call Statup("Rogue", "Obed", 50, -3)   
    elif R_Hand:
        call RogueFace("sad") 
        ch_r "I think you can manage it yourself this time. . ."       
    else:
        call RogueFace("normal", 1)
        ch_r "I'd really rather not."  
    $ R_RecentActions.append("no hand")                      
    $ R_DailyActions.append("no hand") 
    $ Tempmod = 0    
    return
    

label RHJ_Prep:
    if Trigger2 == "hand": 
        return
    
    if Taboo:
        $ R_Inbt += int(Taboo/10)  
        $ R_Lust += int(Taboo/5)
                
    call RogueFace("sexy")
    if R_Forced:
        call RogueFace("sad")
    elif R_Hand:
        $ R_Brows = "confused"
        $ R_Eyes = "sexy"
        $ R_Mouth = "smile"
    
    call Seen_First_Peen("Rogue",Partner)
    call Rogue_HJ_Launch("L")
    if not R_Hand:        
        if R_Forced:
            call Statup("Rogue", "Love", 90, -20)
            call Statup("Rogue", "Obed", 70, 25)
            call Statup("Rogue", "Inbt", 80, 30) 
        else:
            call Statup("Rogue", "Love", 90, 5)
            call Statup("Rogue", "Obed", 70, 20)
            call Statup("Rogue", "Inbt", 80, 20)     
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Rogue","tabno")
    call DrainWord("Rogue","no hand")
    $ R_RecentActions.append("hand")                      
    $ R_DailyActions.append("hand") 
  
label RHJ_Cycle: #Repeating strokes    
    while Round >=0:  
        call Shift_Focus("Rogue") 
        call Rogue_HJ_Launch    
        call RogueLust   
        
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
                                            if R_Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ R_Action -= 1
                                            else:
                                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                                         
                                    "Shift primary action":
                                            if R_Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    if R_Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call RHJ_After                
                                                                        call R_Blowjob
                                                                    else:
                                                                        ch_r "Actually I'm getting a bit worn out, let's finish up here. . ."
                                                                        
                                                        "How about a titjob?":
                                                                    if R_Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call RHJ_After
                                                                        call R_Titjob
                                                                    else:
                                                                        ch_r "Actually I'm getting a bit worn out, let's finish up here. . ."
                                                        "Never Mind":
                                                                jump RHJ_Cycle
                                            else: 
                                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"           
                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask Rogue to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Rogue_Les_Change
                                            "Ask Rogue to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Rogue")  
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0    
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Rogue")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump RHJ_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump RHJ_Cycle 
                                            "Never mind":
                                                        jump RHJ_Cycle 
                                    "Undress Rogue":
                                            call R_Undress   
                                    "Clean up Rogue (locked)" if not R_Spunk:
                                            pass  
                                    "Clean up Rogue" if R_Spunk:
                                            call Rogue_Cleanup("ask")                                         
                                    "Never mind":
                                            jump RHJ_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Rogue_HJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump RHJ_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Rogue_HJ_Reset
                                    $ Line = 0
                                    jump RHJ_After
        #End menu (if Line)
        
        call Shift_Focus("Rogue")
        call Sex_Dialog("Rogue",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or R_Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PR_Cumming
                            if "angry" in R_RecentActions:  
                                call Rogue_HJ_Reset
                                return    
                            call Statup("Rogue", "Lust", 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump RHJ_After 
                            $ Line = "came"
     
                    if R_Lust >= 100:  
                            #If Rogue can cum                                             
                            call R_Cumming
                            if Situation == "shift" or "angry" in R_RecentActions:
                                jump RHJ_After
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in R_RecentActions:#And Rogue is unsatisfied,  
                                "Rogue still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump RHJ_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Rogue")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if R_SEXP >= 100 or ApprovalCheck("Rogue", 1200, "LO"):
            pass
        elif Cnt == (5 + R_Hand):
                    $ R_Brows = "confused"
                    ch_r "Are you getting close here? I'm getting a little sore."   
        elif Cnt == (10 + R_Hand):
                    $ R_Brows = "angry"        
                    menu:
                        ch_r "I'm getting rug-burn here [R_Petname]. Can we do something else?"
                        "How about a BJ?" if R_Action and MultiAction:
                                $ Situation = "shift"
                                call RHJ_After
                                call R_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                jump RHJ_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Rogue_HJ_Reset
                                $ Situation = "shift"
                                jump RHJ_After
                        "No, get back down there.":                                
                                if ApprovalCheck("Rogue", 1200) or ApprovalCheck("Rogue", 500, "O"):                        
                                    call Statup("Rogue", "Love", 200, -5)
                                    call Statup("Rogue", "Obed", 50, 3)                    
                                    call Statup("Rogue", "Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    call RogueFace("angry", 1)   
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_r "Well if that's your attitude you can handle your own business."                         
                                    call Statup("Rogue", "Love", 50, -3, 1)
                                    call Statup("Rogue", "Love", 80, -4, 1)
                                    call Statup("Rogue", "Obed", 30, -1, 1)                    
                                    call Statup("Rogue", "Obed", 50, -1, 1)  
                                    $ R_RecentActions.append("angry")
                                    $ R_DailyActions.append("angry")   
                                    jump RHJ_After
        #End Count check
           
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0)
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
label RHJ_After:
    call RogueFace("sexy") 
    
    $ R_Hand += 1  
    $ R_Action -=1
    $ R_Addictionrate += 1
    if "addictive" in P_Traits:
        $ R_Addictionrate += 1        
    call Statup("Rogue", "Lust", 90, 5)
        
    call Partner_Like("Rogue",2)
    
    if "Rogue Handi-Queen" in Achievements:
            pass  
    elif R_Hand >= 10:
            call RogueFace("smile", 1)
            ch_r "I guess you can call me \"Handi-Queen.\""
            $ Achievements.append("Rogue Handi-Queen")
            $R_SEXP += 5          
    elif R_Hand == 1:            
            $R_SEXP += 10
            if R_Love >= 500:
                $ R_Mouth = "smile"
                ch_r "Well, it's really nice to finally be able to reach out and touch someone."
            elif P_Focus <= 20:
                $ R_Mouth = "sad"
                ch_r "Well, I hope that got your rocks off."
    elif R_Hand == 5:
            ch_r "I think I've got this well in hand."                
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_r "Mmm, so what else did you have in mind?"
    else:
        call Rogue_HJ_Reset    
    call Checkout
    return

## end R_Handjob //////////////////////////////////////////////////////////////////////


## R_Titjob //////////////////////////////////////////////////////////////////////
label R_Titjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Rogue")
    if R_Tit >= 7: # She loves it
        $ Tempmod += 10
    elif R_Tit >= 3: #You've done it before several times
        $ Tempmod += 7
    elif R_Tit: #You've done it before
        $ Tempmod += 5
    
    if R_Addict >= 75 and R_Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 15
    elif R_Addict >= 75:
        $ Tempmod += 5
        
    if R_SeenChest and ApprovalCheck("Rogue", 500): # You've seen her tits.
        $ Tempmod += 10    
    if not R_Chest and not R_Over: #She's already topless
        $ Tempmod += 10
    if R_Lust > 75: #She's really horny
        $ Tempmod += 10
    if Situation == "shift":
        $ Tempmod += 15
    if "exhibitionist" in R_Traits:
        $ Tempmod += (5*Taboo)
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 30 
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount    
    
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no titjob" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no titjob" in R_RecentActions else 0    
        
    $ Approval = ApprovalCheck("Rogue", 1200, TabM = 5) # 120, 135, 150, Taboo -200(320)
    
    if Situation == "Rogue":                                                                  #Rogue auto-starts   
        if Approval > 2:                                                      # fix, add rogue auto stuff here
            call Rogue_TJ_Launch("L")            
            "Rogue slides down and sandwiches your dick between her tits."
            menu:
                "What do you do?"
                "Nothing.":                    
                    call Statup("Rogue", "Inbt", 80, 3) 
                    call Statup("Rogue", "Inbt", 40, 2)                     
                    "Rogue starts to slide them up and down."
                "Praise her.":       
                    call RogueFace("sexy", 1)                    
                    call Statup("Rogue", "Inbt", 80, 3) 
                    ch_p "Oh, that sounds like a good idea, [R_Pet]."
                    call Rogue_Namecheck
                    "Rogue continues her actions."
                    call Statup("Rogue", "Love", 85, 1)
                    call Statup("Rogue", "Obed", 90, 1)
                    call Statup("Rogue", "Obed", 50, 2)
                "Ask her to stop.":     
                    call RogueFace("confused")  
                    call Statup("Rogue", "Inbt", 70, 1) 
                    ch_p "Let's not do that for now, [R_Pet]."
                    call Rogue_Namecheck
                    "Rogue lets it drop out from between her breasts."
                    call Statup("Rogue", "Obed", 90, 1)
                    call Statup("Rogue", "Obed", 50, 3)
                    call Rogue_TJ_Reset  
                    return            
            jump RTJ_Cycle
        else:                
            $ Tempmod = 0                               # fix, add rogue auto stuff here
            $ Trigger2 = 0
            return            
    
    if not R_Tit and "no titjob" not in R_RecentActions:        
        call RogueFace("surprised", 1)
        $ R_Mouth = "kiss"
        ch_r "You want me to rub your cock with my breasts?"        
        if R_Blow:          
            $ R_Mouth = "smile"
            ch_r "My mouth wasn't enough?"
        elif R_Hand:          
            $ R_Mouth = "smile"
            ch_r "My hand wasn't enough?"
            
    if not R_Tit and Approval:                                                 #First time dialog    
        if R_Forced: 
            call RogueFace("sad")
            call Statup("Rogue", "Love", 70, -3, 1)
            call Statup("Rogue", "Love", 20, -2, 1)
        elif R_Love >= (R_Obed + R_Inbt):
            call RogueFace("sexy")
            $ R_Brows = "sad"
            $ R_Mouth = "smile" 
            ch_r "Huh, well that's certainly one way to get off."            
        elif R_Obed >= R_Inbt:
            call RogueFace("normal")
            ch_r "If that's what you want. . ."              
        elif R_Addict >= 50:
            call RogueFace("manic", 1)
            ch_r "Hmmmm. . . ."     
        else: # Uninhibited 
            call RogueFace("sad")
            $ R_Mouth = "smile"             
            ch_r "Heh, might be fun."      
    elif Approval:                                                                       #Second time+ dialog
        if R_Forced: 
            call RogueFace("sad")
            call Statup("Rogue", "Love", 70, -3, 1)
            call Statup("Rogue", "Love", 20, -2, 1)
            ch_r "This isn't going to become a habit, will it?"
        elif not Taboo and "tabno" in R_DailyActions:        
            ch_r "Ok, I guess this is private enough. . ."   
        elif "titjob" in R_RecentActions:
            call RogueFace("sexy", 1)
            ch_r "Mmm, again? Ok, let me get the girls ready."
            jump RTJ_Prep
        elif "titjob" in R_DailyActions:
            call RogueFace("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",   
                "You're going to give me calluses.", 
                "Didn't get enough earlier?",
                "My tits are still a bit sore from earlier."]) 
            ch_r "[Line]"
        elif R_Tit < 3:        
            call RogueFace("sexy", 1)
            $ R_Brows = "confused"
            $ R_Mouth = "kiss"
            ch_r "So you'd like another titjob?"        
        else:       
            call RogueFace("sexy", 1)
            $ Rogue_Arms = 2
            $ Line = renpy.random.choice(["You want some of this action [jiggles her tits]?",                 
                "So you'd like another titjob?",                 
                "A little. . . bounce?", 
                "You want me to pillow your crank?",
                "A little soft embrace?"]) 
            ch_r "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if R_Forced:
            call RogueFace("sad")
            call Statup("Rogue", "Obed", 90, 1)
            call Statup("Rogue", "Inbt", 60, 1)
            ch_r "Well, there are worst ways to get you off. . ." 
        elif "no titjob" in R_DailyActions:               
            ch_r "Hmm, I suppose. . ."       
        else:
            call RogueFace("sexy", 1)
            call Statup("Rogue", "Love", 90, 1)
            call Statup("Rogue", "Inbt", 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, put it here.",                 
                "Well. . . ok.",                 
                "Yum.", 
                "Sure, whip it out.",
                "Fine. . . [She drools a bit into her cleavage].",
                "Heh, ok, alright."]) 
            ch_r "[Line]"
            $ Line = 0
        call Statup("Rogue", "Obed", 20, 1) 
        call Statup("Rogue", "Obed", 70, 1)      
        call Statup("Rogue", "Inbt", 80, 2) 
        jump RTJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call RogueFace("angry")
        if "no titjob" in R_RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions and "no titjob" in R_DailyActions:  
            ch_r "This is just way too exposed!"     
        elif "no titjob" in R_DailyActions:       
            ch_r "I already told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions:  
            ch_r "This is just way too exposed!"     
        elif not R_Tit:
            call RogueFace("bemused")
            ch_r "I'm not really up for that, [R_Petname]. . ."
        else:
            call RogueFace("bemused")
            ch_r "Not, right now [R_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no titjob" in R_DailyActions:
                call RogueFace("bemused")
                ch_r "Yeah, ok, [R_Petname]."              
                return
            "Maybe later?" if "no titjob" not in R_DailyActions:
                call RogueFace("sexy")  
                ch_r "We'll have to see."
                call Statup("Rogue", "Love", 80, 2)
                call Statup("Rogue", "Inbt", 70, 2)   
                if Taboo:                    
                    $ R_RecentActions.append("tabno")                      
                    $ R_DailyActions.append("tabno") 
                $ R_RecentActions.append("no titjob")                      
                $ R_DailyActions.append("no titjob")            
                return
            "I think this could be fun for both of us. . .":             
                if Approval:
                    call RogueFace("sexy")     
                    call Statup("Rogue", "Obed", 80, 2)
                    call Statup("Rogue", "Obed", 40, 2)
                    call Statup("Rogue", "Inbt", 70, 3) 
                    call Statup("Rogue", "Inbt", 40, 2) 
                    $ Line = renpy.random.choice(["Well, ok, put it here.",                 
                        "Well. . . ok.",                 
                        "I guess.", 
                        "I guess, whip it out.",
                        "Fine. . . [She drools a bit into her cleavage].",
                        "Heh, ok, alright."])
                    ch_r "[Line]"
                    $ Line = 0                   
                    jump RTJ_Prep
                else:   
                    $ Approval = ApprovalCheck("Rogue", 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)             Handy instead?
                    if Approval >= 2:       
                        call Statup("Rogue", "Inbt", 80, 1) 
                        call Statup("Rogue", "Inbt", 60, 3) 
                        call RogueFace("confused", 1)
                        if R_Blow:
                            ch_r "I could just. . . blow you instead?"
                        else:
                            ch_r "I could maybe. . . you know, [[she pushes her tongue against the side of her cheek]?"
                        menu:
                            extend ""
                            "Ok, get down there.":
                                call Statup("Rogue", "Love", 80, 2)  
                                call Statup("Rogue", "Inbt", 60, 1)                                
                                call Statup("Rogue", "Obed", 50, 1) 
                                jump RBJ_Prep
                            "Nah, it's all about dem titties.":  
                                $ Line = "no BJ"
                    if Approval:       
                        call Statup("Rogue", "Inbt", 80, 1) 
                        call Statup("Rogue", "Inbt", 60, 3) 
                        call RogueFace("confused", 1)
                        if R_Hand:
                            ch_r "Maybe you'd settle for a handy?"
                        else:
                            ch_r "I could maybe. . . [[she makes a jerking motion with her hand]?"
                        menu:
                            extend ""
                            "Sure, that's fine.":
                                call Statup("Rogue", "Love", 80, 2)  
                                call Statup("Rogue", "Inbt", 60, 1)                                
                                call Statup("Rogue", "Obed", 50, 1) 
                                jump RHJ_Prep
                            "Seriously, titties." if Line == "no BJ":  
                                $ Line = 0
                            "Nah, it's all about dem titties." if Line != "no BJ":  
                                pass
                    call Statup("Rogue", "Love", 200, -2)                 
                    ch_r "Ok, whatever."  
                    call Statup("Rogue", "Obed", 70, 2) 
                    
                    
            "Come on, let me fuck those titties, [R_Pet]":                                               # Pressured into it                
                call Rogue_Namecheck
                $ Approval = ApprovalCheck("Rogue", 700, "OI", TabM = 4) # 70, 85, 100, -160(230)
                if Approval > 1 or (Approval and R_Forced):
                    call RogueFace("sad")
                    call Statup("Rogue", "Love", 70, -5, 1)
                    call Statup("Rogue", "Love", 200, -2)                 
                    ch_r "Ok, fine, whip it out."  
                    call Statup("Rogue", "Obed", 50, 4)
                    call Statup("Rogue", "Inbt", 80, 1) 
                    call Statup("Rogue", "Inbt", 60, 3)  
                    $ R_Forced = 1
                    jump RTJ_Prep
                else:                              
                    call Statup("Rogue", "Love", 200, -15)     
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")   
    
    #She refused all offers.   
    if "no titjob" in R_DailyActions:
        call RogueFace("angry", 1)
        ch_r "Look, I already told you no thanks, [R_Petname]."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1)
        ch_r "I'm not that kind of girl."
        call Statup("Rogue", "Lust", 200, 5)      
        if R_Love > 300: 
                call Statup("Rogue", "Love", 70, -2)
        call Statup("Rogue", "Obed", 50, -2)      
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call RogueFace("angry", 1)          
        $ R_DailyActions.append("tabno") 
        ch_r "You really expect me to do that here? You realize how. . . exposed that would be?"
        call Statup("Rogue", "Lust", 200, 5)  
        call Statup("Rogue", "Obed", 50, -3)  
    elif R_Tit:
        call RogueFace("sad") 
        ch_r "I think I'll let you know when I want you touching these again."       
    else:
        call RogueFace("normal", 1)
        ch_r "How about let's not, [R_Petname]."
    $ R_RecentActions.append("no titjob")                      
    $ R_DailyActions.append("no titjob") 
    $ Tempmod = 0    
    return
    
label RTJ_Prep:
      
    if Taboo:
        $ R_Inbt += int(Taboo/10)  
        $ R_Lust += int(Taboo/5)

        
    call RogueFace("sexy")
    if R_Forced:
        call RogueFace("sad")
    elif R_Tit:
        $ R_Brows = "confused"
        $ R_Eyes = "sexy"
        $ R_Mouth = "smile"
    
    call Seen_First_Peen("Rogue",Partner)
    call Rogue_TJ_Launch("L")    
    if not R_Tit:        
        if R_Forced:
            call Statup("Rogue", "Love", 90, -25)
            call Statup("Rogue", "Obed", 70, 30)
            call Statup("Rogue", "Inbt", 80, 35) 
        else:
            call Statup("Rogue", "Love", 90, 5)
            call Statup("Rogue", "Obed", 70, 25)
            call Statup("Rogue", "Inbt", 80, 30)   
            
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0  
    if Taboo:
        call DrainWord("Rogue","tabno")
    call DrainWord("Rogue","no titjob")
    $ R_RecentActions.append("titjob")                      
    $ R_DailyActions.append("titjob") 


label RTJ_Cycle: #Repeating strokes    
    while Round >=0:  
        call Shift_Focus("Rogue") 
        call Rogue_TJ_Launch    
        call RogueLust   
        
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
                                            if R_Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ R_Action -= 1
                                            else:
                                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                                         
                                    "Shift primary action":
                                            if R_Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                if R_Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call RTJ_After                
                                                                    call R_Blowjob
                                                                else:
                                                                    ch_r "Actually I'm getting a bit worn out, let's finish up here. . ."
                                                                    
                                                        "How about a handy?":
                                                                if R_Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call RBJ_After
                                                                    call R_Handjob
                                                                else:
                                                                    ch_r "Actually I'm getting a bit worn out, let's finish up here. . ."                                                            
                                                        "Never Mind":
                                                                jump RTJ_Cycle
                                            else: 
                                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"           
                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask Rogue to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Rogue_Les_Change
                                            "Ask Rogue to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Rogue")  
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0    
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Rogue")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump RTJ_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump RTJ_Cycle 
                                            "Never mind":
                                                        jump RTJ_Cycle 
                                    "Undress Rogue":
                                            call R_Undress   
                                    "Clean up Rogue (locked)" if not R_Spunk:
                                            pass  
                                    "Clean up Rogue" if R_Spunk:
                                            call Rogue_Cleanup("ask")                                         
                                    "Never mind":
                                            jump RTJ_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Rogue_TJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump RTJ_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Rogue_TJ_Reset
                                    $ Line = 0
                                    jump RTJ_After
        #End menu (if Line)
        
        call Shift_Focus("Rogue")
        call Sex_Dialog("Rogue",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or R_Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PR_Cumming
                            if "angry" in R_RecentActions:  
                                call Rogue_TJ_Reset
                                return    
                            call Statup("Rogue", "Lust", 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump RTJ_After 
                            $ Line = "came"
     
                    if R_Lust >= 100:  
                            #If Rogue can cum                                             
                            call R_Cumming
                            if Situation == "shift" or "angry" in R_RecentActions:
                                jump RTJ_After
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in R_RecentActions:#And Rogue is unsatisfied,  
                                "Rogue still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump RTJ_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Rogue")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if R_SEXP >= 100 or ApprovalCheck("Rogue", 1200, "LO"):
            pass
        elif Cnt == (5 + R_Tit):
                    $ R_Brows = "confused"
                    ch_r "Are you getting close here? I'm getting a little sore."   
        elif Cnt == (10 + R_Tit):
                    $ R_Brows = "angry"        
                    menu:
                        ch_r "I'm getting rug-burn here [R_Petname]. Can we do something else?"
                        "How about a BJ?" if R_Action and MultiAction:
                                $ Situation = "shift"
                                call RTJ_After
                                call R_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                jump RTJ_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Rogue_TJ_Reset
                                $ Situation = "shift"
                                jump RTJ_After
                        "No, get back down there.":                                
                                if ApprovalCheck("Rogue", 1200) or ApprovalCheck("Rogue", 500, "O"):                        
                                    call Statup("Rogue", "Love", 200, -5)
                                    call Statup("Rogue", "Obed", 50, 3)                    
                                    call Statup("Rogue", "Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    call RogueFace("angry", 1)   
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_r "Well if that's your attitude you can handle your own business."                         
                                    call Statup("Rogue", "Love", 50, -3, 1)
                                    call Statup("Rogue", "Love", 80, -4, 1)
                                    call Statup("Rogue", "Obed", 30, -1, 1)                    
                                    call Statup("Rogue", "Obed", 50, -1, 1)  
                                    $ R_RecentActions.append("angry")
                                    $ R_DailyActions.append("angry")   
                                    jump RTJ_After
        #End Count check
           
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0)
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
        
label RTJ_After:
    call RogueFace("sexy") 
    
    $ R_Tit += 1
    $ R_Action -=1
    $ R_Addictionrate += 1
    if "addictive" in P_Traits:
        $ R_Addictionrate += 1
        
    call Partner_Like("Rogue",3)
        
    if R_Tit > 5:
            pass
    elif R_Tit == 1:
        $R_SEXP += 12
        if R_Love >= 500:
            $ R_Mouth = "smile"
            ch_r "Well, that was certainly interesting."
        elif P_Focus <= 20:
            $ R_Mouth = "sad"
            ch_r "Well, I hope that was enough for you."        
    elif R_Tit == 5:
            ch_r "I think I've got the goods for this."   
    
    
    $ Tempmod = 0 
    if Situation == "shift":
            ch_r "Mmm, so what else did you have in mind?"
    else:
            call Rogue_TJ_Reset    
    call Checkout
    return

## end R_Titjob //////////////////////////////////////////////////////////////////////

# R_Blowjob //////////////////////////////////////////////////////////////////////

label R_Blowjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Rogue")
    if R_Blow >= 7: # She loves it
        $ Tempmod += 15  
    elif R_Blow >= 3: #You've done it before several times
        $ Tempmod += 10
    elif R_Blow: #You've done it before
        $ Tempmod += 7    
        
    if R_Addict >= 75 and R_Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 25
    elif R_Addict >= 75: #She's really strung out
        $ Tempmod += 15
        
    if Situation == "shift":
        $ Tempmod += 15
    if "exhibitionist" in R_Traits:
        $ Tempmod += (4*Taboo) 
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 40  
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount        
    
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no blow" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no blow" in R_RecentActions else 0    
    
    $ Approval = ApprovalCheck("Rogue", 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)
    
    if Situation == "Rogue":                                                                  #Rogue auto-starts   
        if Approval > 2:                                                      # fix, add rogue auto stuff here
            "Rogue slides down and gives your cock a little lick."
            menu:
                "What do you do?"
                "Nothing.":                    
                    call Statup("Rogue", "Inbt", 80, 3) 
                    call Statup("Rogue", "Inbt", 40, 2)                     
                    "Rogue continues licking at it."
                "Praise her.":       
                    call RogueFace("sexy", 1)                    
                    call Statup("Rogue", "Inbt", 80, 3) 
                    ch_p "Hmmm, keep doing that, [R_Pet]."
                    call Rogue_Namecheck
                    "Rogue continues her actions."
                    call Statup("Rogue", "Love", 85, 1)
                    call Statup("Rogue", "Obed", 90, 1)
                    call Statup("Rogue", "Obed", 50, 2)
                "Ask her to stop.":     
                    call RogueFace("surprised")  
                    call Statup("Rogue", "Inbt", 70, 1) 
                    ch_p "Let's not do that for now, [R_Pet]."
                    call Rogue_Namecheck
                    "Rogue puts it down."
                    call Statup("Rogue", "Obed", 90, 1)
                    call Statup("Rogue", "Obed", 50, 3)
                    return            
            jump RBJ_Prep
        else:                
            $ Tempmod = 0                               # fix, add rogue auto stuff here
            $ Trigger2 = 0
            return            
    
    if not R_Blow and "no blow" not in R_RecentActions:        
        call RogueFace("surprised", 1)
        $ R_Mouth = "kiss"
        ch_r "You want me to put your dick. . . in my mouth?"
        if R_Hand:          
            $ R_Mouth = "smile"
            ch_r "My hand wasn't enough?"
            
    if not R_Blow and Approval:                                                 #First time dialog        
        if R_Forced: 
            call RogueFace("sad")
            call Statup("Rogue", "Love", 70, -3, 1)
            call Statup("Rogue", "Love", 20, -2, 1)
        elif R_Love >= (R_Obed + R_Inbt):
            call RogueFace("sexy")
            $ R_Brows = "sad"
            $ R_Mouth = "smile" 
            ch_r "I've never really put something like that in my mouth. . . might be interesting."            
        elif R_Obed >= R_Inbt:
            call RogueFace("normal")
            ch_r "I suppose, if that's what you want. . ."               
        elif R_Addict >= 50:
            call RogueFace("manic", 1)
            ch_r "I think. . . for some reason I really do want that in my mouth. . ."   
        else: # Uninhibited 
            call RogueFace("sad")
            $ R_Mouth = "smile"             
            ch_r "I guess. . ."       
    elif Approval:                                                                       #Second time+ dialog
        if R_Forced: 
            call RogueFace("sad")
            call Statup("Rogue", "Love", 70, -3, 1)
            call Statup("Rogue", "Love", 20, -2, 1)
            ch_r "You want me to do that again?"
        elif not Taboo and "tabno" in R_DailyActions:        
            ch_r "Ok, I guess this is private enough. . ."    
        elif "blow" in R_RecentActions:
            call RogueFace("sexy", 1)
            ch_r "Mmm, again? [[stretches her jaw]"
            jump RBJ_Prep                
        elif "blow" in R_DailyActions:
            call RogueFace("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",   
                "You're going to give me lockjaw.", 
                "Let me get some saliva going.",
                "Didn't get enough earlier?",
                "My jaw's still a bit sore from earlier.",
                "My jaw's still a bit sore from earlier."]) 
            ch_r "[Line]"
        elif R_Blow < 3:        
            call RogueFace("sexy", 1)
            $ R_Brows = "confused"
            $ R_Mouth = "kiss"
            ch_r "So you'd like another blowjob?"        
        else:       
            call RogueFace("sexy", 1)
            $ Rogue_Arms = 2
            $ Line = renpy.random.choice(["You want some of this action [mimes blowing]?",                 
                "So you'd like another blowjob?",                 
                "A little. . . lick?", 
                "You want me to wet your willy?",
                "A little tender loving care?"]) 
            ch_r "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if R_Forced:
            call RogueFace("sad")
            call Statup("Rogue", "Obed", 90, 1)
            call Statup("Rogue", "Inbt", 60, 1)
            ch_r "Whatever."    
        elif "no blow" in R_DailyActions:               
            ch_r "Oh, I suppose it isn't so bad. . ."  
        else:
            call RogueFace("sexy", 1)
            call Statup("Rogue", "Love", 90, 1)
            call Statup("Rogue", "Inbt", 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, ahhhhhh.",                 
                "Well. . . ok.",                 
                "Yum.", 
                "Sure, whip it out.",
                "Fine. . . [She licks her lips].",
                "Heh, ok, alright."]) 
            ch_r "[Line]"
            $ Line = 0
        call Statup("Rogue", "Obed", 20, 1) 
        call Statup("Rogue", "Obed", 70, 1)      
        call Statup("Rogue", "Inbt", 80, 2) 
        jump RBJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call RogueFace("angry")
        if "no blow" in R_RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions and "no blow" in R_DailyActions:  
            ch_r "I already told you that I wouldn't suck you off in public!"  
        elif "no blow" in R_DailyActions:       
            ch_r "I already told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions:  
            ch_r "I already told you this is too public!"      
        elif not R_Blow:
            call RogueFace("bemused")
            ch_r "I don't think I'd like the taste, [R_Petname]. . ."
        else:
            call RogueFace("bemused")
            ch_r "Not, right now [R_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no blow" in R_DailyActions:
                call RogueFace("bemused")
                ch_r "Yeah, ok, [R_Petname]."              
                return
            "Maybe later?" if "no blow" not in R_DailyActions:
                call RogueFace("sexy")  
                ch_r "I might get hungry, [R_Petname]."
                call Statup("Rogue", "Love", 80, 2)
                call Statup("Rogue", "Inbt", 70, 2)   
                if Taboo:                    
                    $ R_RecentActions.append("tabno")                      
                    $ R_DailyActions.append("tabno") 
                $ R_RecentActions.append("no blow")                      
                $ R_DailyActions.append("no blow")            
                return
            "Come on, please?":             
                if Approval:
                    call RogueFace("sexy")     
                    call Statup("Rogue", "Obed", 90, 2)
                    call Statup("Rogue", "Obed", 50, 2)
                    call Statup("Rogue", "Inbt", 70, 3) 
                    call Statup("Rogue", "Inbt", 40, 2) 
                    $ Line = renpy.random.choice(["Well, sure, ahhhhhh.",                 
                        "Well. . . ok.",                 
                        "I guess a taste couldn't hurt.", 
                        "I guess I could. . . whip it out.",
                        "Fine. . . [She licks her lips].",
                        "Heh, ok, alright."]) 
                    ch_r "[Line]"
                    $ Line = 0                   
                    jump RBJ_Prep
                else:   
                    if ApprovalCheck("Rogue", 1100, TabM = 3): # 110, 125, 140, Taboo -120(230)             Handy instead?    
                        call Statup("Rogue", "Inbt", 80, 1) 
                        call Statup("Rogue", "Inbt", 60, 3) 
                        call RogueFace("confused", 1)
                        if R_Hand:
                            ch_r "Maybe you'd settle for a handy?"
                        else:
                            ch_r "I could maybe. . . [[she makes a jerking motion with her hand]?"
                        menu:
                            ch_r "What do you say?"
                            "Sure, that's fine.":
                                call Statup("Rogue", "Love", 80, 2)  
                                call Statup("Rogue", "Inbt", 60, 1)                                
                                call Statup("Rogue", "Obed", 50, 1) 
                                jump RHJ_Prep
                            "Nah, if it's not a BJ, forget it.":
                                call Statup("Rogue", "Love", 200, -2)                 
                                ch_r "Ok, whatever."  
                                call Statup("Rogue", "Obed", 70, 2) 
                    
                    
            "Suck it, [R_Pet]":                                               # Pressured into it                
                call Rogue_Namecheck
                $ Approval = ApprovalCheck("Rogue", 750, "OI", TabM = 3) # 75, 90, 105, -120(195)
                if Approval > 1 or (Approval and R_Forced):
                    call RogueFace("sad")
                    call Statup("Rogue", "Love", 70, -5, 1)
                    call Statup("Rogue", "Love", 200, -2)                 
                    ch_r "Ok, fine, whip it out."  
                    call Statup("Rogue", "Obed", 50, 4)
                    call Statup("Rogue", "Inbt", 80, 1) 
                    call Statup("Rogue", "Inbt", 60, 3)  
                    $ R_Forced = 1
                    jump RBJ_Prep
                else:                              
                    call Statup("Rogue", "Love", 200, -15)     
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")   
    
    #She refused all offers.   
    if "no blow" in R_DailyActions:
        call RogueFace("angry", 1)
        ch_r "Read my lips, no."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1)
        ch_r "That isn't something I'd want!"
        call Statup("Rogue", "Lust", 200, 5)     
        if R_Love > 300: 
                call Statup("Rogue", "Love", 70, -2)
        call Statup("Rogue", "Obed", 50, -2)      
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
        $ R_RecentActions.append("no blow")                      
        $ R_DailyActions.append("no blow") 
        return
    elif Taboo:                             # she refuses and this is too public a place for her
        call RogueFace("angry", 1)          
        $ R_DailyActions.append("tabno") 
        ch_r "You really expect me to do that here?"
        call Statup("Rogue", "Lust", 200, 5)  
        call Statup("Rogue", "Obed", 50, -3)    
        return                
    elif R_Blow:
        call RogueFace("sad") 
        ch_r "I think I've got the taste out of my mouth, thanks."       
    else:
        call RogueFace("normal", 1)
        ch_r "Not interested."  
    $ R_RecentActions.append("no blow")                      
    $ R_DailyActions.append("no blow") 
    $ Tempmod = 0    
    return
    

label RBJ_Prep:   
    if Taboo:
        $ R_Inbt += int(Taboo/10)  
        $ R_Lust += int(Taboo/5)
                
    call RogueFace("sexy")
    if R_Forced:
        call RogueFace("sad")
    elif R_Hand:
        $ R_Brows = "confused"
        $ R_Eyes = "sexy"
        $ R_Mouth = "smile"
    
    call Seen_First_Peen("Rogue",Partner)
    call Rogue_BJ_Launch("L")
    if not R_Blow:        
        if R_Forced:
            call Statup("Rogue", "Love", 90, -70)
            call Statup("Rogue", "Obed", 70, 45)
            call Statup("Rogue", "Inbt", 80, 60) 
        else:
            call Statup("Rogue", "Love", 90, 5)
            call Statup("Rogue", "Obed", 70, 35)
            call Statup("Rogue", "Inbt", 80, 40)     
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Rogue","tabno")
    call DrainWord("Rogue","no blow")
    $ R_RecentActions.append("blow")                      
    $ R_DailyActions.append("blow")     

label RBJ_Cycle: #Repeating strokes    
    while Round >=0:  
        call Shift_Focus("Rogue") 
        call Rogue_BJ_Launch    
        call RogueLust   
        
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
                                if "pushed" not in R_RecentActions and R_Blow < 5:
                                    call Statup("Rogue", "Love", 80, -(20-(2*R_Blow))) 
                                    call Statup("Rogue", "Obed", 80, (30-(3*R_Blow)))
                                    $ R_RecentActions.append("pushed")
                                if Trigger2 == "jackin" and Speed != 3:
                                    "She takes it to the root, and you move your hand out of the way."
                                $ Speed = 4  
                        "Take it deeper. (locked)" if Speed == 4:
                                pass
                            
                        "Set your own pace. . .":                
                                "Rogue hums contentedly."    
                                if "setpace" not in R_RecentActions:
                                    call Statup("Rogue", "Love", 80, 2)
                                $ D20 = renpy.random.randint(1, 20)     
                                if R_Blow < 5:
                                    $ D20 -= 10
                                elif R_Blow < 10:
                                    $ D20 -= 5
                                    
                                if D20 > 15:
                                    $ Speed = 4              
                                    if "setpace" not in R_RecentActions:      
                                        call Statup("Rogue", "Inbt", 80, 3) 
                                elif D20 > 10:
                                    $ Speed = 3
                                elif D20 > 5:
                                    $ Speed = 2
                                else:
                                    $ Speed = 1
                                $ R_RecentActions.append("setpace")
                                
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
                                            if R_Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ R_Action -= 1
                                            else:
                                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                                         
                                    "Shift primary action":
                                            if R_Action and MultiAction:
                                                    menu:
                                                        "How about a handy?":
                                                                if R_Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call RBJ_After
                                                                    call R_Handjob
                                                                else:
                                                                    ch_r "Actually I'm getting a bit worn out, let's finish up here. . ."
                                                        "How about a titjob?":
                                                                if R_Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call RBJ_After
                                                                    call R_Titjob
                                                                else:
                                                                    ch_r "Actually I'm getting a bit worn out, let's finish up here. . ."
                                                        "Never Mind":
                                                                jump RBJ_Cycle
                                            else: 
                                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"           
                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:  
                                        menu:
                                            "Ask Rogue to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Rogue_Les_Change
                                            "Ask Rogue to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Rogue")  
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0    
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Rogue")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump RBJ_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump RBJ_Cycle 
                                            "Never mind":
                                                        jump RBJ_Cycle 
                                    "Undress Rogue":
                                            call R_Undress   
                                    "Clean up Rogue (locked)" if not R_Spunk:
                                            pass  
                                    "Clean up Rogue" if R_Spunk:
                                            call Rogue_Cleanup("ask")                                         
                                    "Never mind":
                                            jump RBJ_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Rogue_BJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump RBJ_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Rogue_BJ_Reset
                                    $ Line = 0
                                    jump RBJ_After
        #End menu (if Line)
                    
        call Shift_Focus("Rogue")
        call Sex_Dialog("Rogue",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
        if Speed:
            $ P_Wet = 1 #wets penis        
            $ P_Spunk = 0 if P_Spunk else P_Spunk #cleans you off after one cycle
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or R_Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PR_Cumming
                            if "angry" in R_RecentActions:  
                                call Rogue_BJ_Reset
                                return    
                            call Statup("Rogue", "Lust", 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump RBJ_After 
                            $ Line = "came"
     
                    if R_Lust >= 100:  
                            #If Rogue can cum                                             
                            call R_Cumming
                            if Situation == "shift" or "angry" in R_RecentActions:
                                jump RBJ_After
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in R_RecentActions:#And Rogue is unsatisfied,  
                                "Rogue still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump RBJ_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Rogue")            
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if R_SEXP >= 100 or ApprovalCheck("Rogue", 1200, "LO"):
            pass
        elif Cnt == (5 + R_Blow):
                    $ R_Brows = "confused"
                    ch_r "Are you getting close here? My jaw's getting pretty sore." 
        elif Cnt == (10 + R_Blow):
                    $ R_Brows = "angry"     
                    ch_r "I'm getting a little tired, [R_Petname]. Can we do something else?"   
                    menu:
                        ch_r "I'm getting a little tired, [R_Petname]. Can we do something else?"                        
                        "Continue (locked)":
                                pass
                        "How about a Handy?" if R_Action and MultiAction:
                                $ Situation = "shift"
                                call RBJ_After
                                call R_Handjob 
                                return
                        "How about a Handy? (locked)" if not R_Action or not MultiAction:
                                pass
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                jump RBJ_Cycle
                        "Finish up. (locked)" if not P_FocusX:
                                pass
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Rogue_BJ_Reset
                                $ Situation = "shift"
                                jump RBJ_After
                        "Let's try something else. (locked)" if not MultiAction: 
                                pass
                        "No, get back down there.":
                                if ApprovalCheck("Rogue", 1200) or ApprovalCheck("Rogue", 500, "O"):
                                    call Statup("Rogue", "Love", 200, -5)
                                    call Statup("Rogue", "Obed", 50, 3)
                                    call Statup("Rogue", "Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    call RogueFace("angry", 1)  
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_r "Well if that's your attitude you can handle your own business."
                                    call Statup("Rogue", "Love", 50, -3, 1)
                                    call Statup("Rogue", "Love", 80, -4, 1)
                                    call Statup("Rogue", "Obed", 30, -1, 1)
                                    call Statup("Rogue", "Obed", 50, -1, 1)  
                                    $ R_RecentActions.append("angry")
                                    $ R_DailyActions.append("angry")   
                                    jump RBJ_After
        #End Count check
           
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0)
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."

label RBJ_After:    
    call RogueFace("sexy")  
        
    $ R_Blow += 1
    $ R_Action -=1
    $ R_Addictionrate += 1
    if "addictive" in P_Traits:
        $ R_Addictionrate += 1
    
    if Partner == "Emma":
        call Partner_Like("Rogue",3)
    else:
        call Partner_Like("Rogue",2)
            
    if "Rogue Jobber" in Achievements:
        pass
    elif R_Blow >= 10:
        call RogueFace("smile", 1)
        ch_r "I'm really starting to enjoy this."        
        $ Achievements.append("Rogue Jobber")
        $R_SEXP += 5
    elif Situation == "shift":
        pass
    elif R_Blow == 1:
            $R_SEXP += 15
            if R_Love >= 500:
                $ R_Mouth = "smile"
                ch_r "That really wasn't half bad."
            elif P_Focus <= 20:
                $ R_Mouth = "sad"
                ch_r "Well, I hope that got your rocks off."
    elif R_Blow == 5:
        ch_r "I think I've got the hang of this."
    
    $ Tempmod = 0    
    if Situation != "shift":
        call Rogue_BJ_Reset    
    call Checkout
    return
    
return

# end R_Blowjob                                 //////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label R_Dildo_Check:
    if "dildo" in P_Inventory:   
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in R_Inventory:
        "You ask Rogue to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1
            
label R_Dildo_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Rogue")
    call R_Dildo_Check    
    if not _return:
        return 

    if R_DildoP: #You've done it before
        $ Tempmod += 15
    if R_Legs == "pants:": # she's got pants on.
        $ Tempmod -= 20
        
    if R_Lust > 95:
        $ Tempmod += 20    
    elif R_Lust > 85: #She's really horny
        $ Tempmod += 15
        
    if Situation == "shift":
        $ Tempmod += 10
    if "exhibitionist" in R_Traits:        
        $ Tempmod += (5*Taboo) 
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 40
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount     
        
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no dildo" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no dildo" in R_RecentActions else 0       
        
    $ Approval = ApprovalCheck("Rogue", 1250, TabM = 4) # 125, 140, 155, Taboo -160(335)
    
    if Situation == "Rogue":                                                                  #Rogue auto-starts   
                if Approval > 2:                                                      # fix, add rogue auto stuff here
                    if R_Legs == "skirt":
                        "Rogue grabs her dildo, hiking up her skirt as she does."
                        $ R_Upskirt = 1
                    elif R_Legs == "pants":
                        "Rogue grabs her dildo, pulling down her pants as she does."              
                        $ R_Legs = 0
                    else:
                        "Rogue grabs her dildo, rubbing is suggestively against her crotch."
                    $ R_SeenPanties = 1
                    "She slides the tip along her pussy and seems to want you to insert it."
                    menu:
                        "What do you do?"
                        "Nothing.":                    
                            call Statup("Rogue", "Inbt", 80, 3) 
                            call Statup("Rogue", "Inbt", 50, 2)
                            "Rogue slides it in."
                        "Go for it.":       
                            call RogueFace("sexy", 1)                    
                            call Statup("Rogue", "Inbt", 80, 3) 
                            ch_p "Oh yeah, [R_Pet], let's do this."
                            call Rogue_Namecheck
                            "You grab the dildo and slide it in."
                            call Statup("Rogue", "Love", 85, 1)
                            call Statup("Rogue", "Obed", 90, 1)
                            call Statup("Rogue", "Obed", 50, 2)
                        "Ask her to stop.":
                            call RogueFace("surprised")       
                            call Statup("Rogue", "Inbt", 70, 1) 
                            ch_p "Let's not do that right now, [R_Pet]."
                            call Rogue_Namecheck
                            "Rogue sets the dildo down."
                            call Statup("Rogue", "Obed", 90, 1)
                            call Statup("Rogue", "Obed", 50, 1)
                            call Statup("Rogue", "Obed", 30, 2)
                            return            
                    jump RDP_Prep
                else:                
                    $ Tempmod = 0                               # fix, add rogue auto stuff here
                    $ Trigger2 = 0
                return            
    
    if Situation == "auto":    
                "You rub the dildo across her body, and along her moist slit."
                call RogueFace("surprised", 1)
                
                if (R_DildoP and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
                    "Rogue is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                    call RogueFace("sexy")
                    call Statup("Rogue", "Obed", 70, 3)
                    call Statup("Rogue", "Inbt", 50, 3) 
                    call Statup("Rogue", "Inbt", 70, 1) 
                    ch_r "Ok, [R_Petname], let's do this."            
                    jump RDP_Prep         
                else:                                                                                                            #she's questioning it
                    $ R_Brows = "angry"                
                    menu:
                        ch_r "Hey, what do you think you're doing back there?!" 
                        "Sorry, sorry! Never mind.":
                            if Approval:     
                                call RogueFace("sexy", 1)
                                call Statup("Rogue", "Obed", 70, 3)
                                call Statup("Rogue", "Inbt", 50, 3) 
                                call Statup("Rogue", "Inbt", 70, 1) 
                                ch_r "Well, since you're be'in so nice about it, I guess we can give it a go. . ."
                                jump RDP_Prep
                            "You pull back before you really get it in."                    
                            call RogueFace("bemused", 1)
                            if R_DildoP:
                                ch_r "Well ok, [R_Petname], no harm done. Just give me a little warning next time." 
                            else:
                                ch_r "Well ok, [R_Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."                                               
                        "Just playing with my favorite toys.":                    
                            call Statup("Rogue", "Love", 80, -10, 1)  
                            call Statup("Rogue", "Love", 200, -10)
                            "You press it inside some more."                              
                            call Statup("Rogue", "Obed", 70, 3)
                            call Statup("Rogue", "Inbt", 50, 3) 
                            if not ApprovalCheck("Rogue", 700, "O", TabM=1): #Checks if Obed is 700+                             
                                call RogueFace("angry")
                                "Rogue shoves you away and slaps you in the face."
                                ch_r "Jackass!"
                                ch_r "If that's how you want to treat me, we're done here!"                                                  
                                call Statup("Rogue", "Love", 50, -10, 1)                        
                                call Statup("Rogue", "Obed", 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                if renpy.showing("Rogue_Doggy"):
                                    call Rogue_Sex_Reset  
                                $ R_RecentActions.append("angry")
                                $ R_DailyActions.append("angry")                          
                            else:
                                call RogueFace("sad")
                                "Rogue doesn't seem to be into this, you're lucky she's so obedient."                        
                                jump RDP_Prep
                return             
    #end Auto
   
    if not R_DildoP:                                                               
            #first time    
            call RogueFace("surprised", 1)
            $ R_Mouth = "kiss"
            ch_r "Hmmm, so you'd like to try out some toys?"    
            if R_Forced:
                call RogueFace("sad")
                ch_r "I suppose there are worst things you could ask for."
            
    if not R_DildoP and Approval:                                                 
            #First time dialog        
            if R_Forced: 
                call RogueFace("sad")
                call Statup("Rogue", "Love", 70, -3, 1)
                call Statup("Rogue", "Love", 20, -2, 1)
            elif R_Love >= (R_Obed + R_Inbt):
                call RogueFace("sexy")
                $ R_Brows = "sad"
                $ R_Mouth = "smile" 
                ch_r "I've had a reasonable amount of experience with these, you know. . ."            
            elif R_Obed >= R_Inbt:
                call RogueFace("normal")
                ch_r "If that's what you want, [R_Petname]. . ."            
            else: # Uninhibited 
                call RogueFace("sad")
                $ R_Mouth = "smile"             
                ch_r "I guess it could be fun with a partner. . ."    
            
    elif Approval:                                                                       
            #Second time+ dialog
            if R_Forced: 
                call RogueFace("sad")
                call Statup("Rogue", "Love", 70, -3, 1)
                call Statup("Rogue", "Love", 20, -2, 1)
                ch_r "The toys again?" 
            elif not Taboo and "tabno" in R_DailyActions:        
                ch_r "Well, at least you got us some privacy this time. . ."   
            elif "dildo pussy" in R_RecentActions:
                call RogueFace("sexy", 1)
                ch_r "Mmm, again? Ok, let's get to it."
                jump RDP_Prep
            elif "dildo pussy" in R_DailyActions:
                call RogueFace("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "You're going to wear me out."]) 
                ch_r "[Line]"
            elif R_DildoP < 3:        
                call RogueFace("sexy", 1)
                $ R_Brows = "confused"
                $ R_Mouth = "kiss"
                ch_r "You want to stick it in my pussy again?"       
            else:       
                call RogueFace("sexy", 1)
                $ Rogue_Arms = 2
                $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my pussy again?",
                    "You want me ta lube up your toy?"]) 
                ch_r "[Line]"
                $ Line = 0
            
    if Approval >= 2:                                                                   
            #She's into it. . .               
            if R_Forced:
                call RogueFace("sad")
                call Statup("Rogue", "Obed", 90, 1)
                call Statup("Rogue", "Inbt", 60, 1)
                ch_r "Ok, fine."    
            else:
                call RogueFace("sexy", 1)
                call Statup("Rogue", "Love", 90, 1)
                call Statup("Rogue", "Inbt", 50, 3) 
                $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."]) 
                ch_r "[Line]"
                $ Line = 0
            call Statup("Rogue", "Obed", 20, 1)
            call Statup("Rogue", "Obed", 60, 1)
            call Statup("Rogue", "Inbt", 70, 2) 
            jump RDP_Prep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            call RogueFace("angry")
            if "no dildo" in R_RecentActions:  
                ch_r "What part of \"no,\" did you not get, [R_Petname]?"
            elif Taboo and "tabno" in R_DailyActions and "no dildo" in R_DailyActions:
                ch_r "Stop swinging that thing around in public!"   
            elif "no dildo" in R_DailyActions:       
                ch_r "I already told you \"no,\" [R_Petname]."
            elif Taboo and "tabno" in R_DailyActions:  
                ch_r "Stop swinging that thing around in public!"  
            elif not R_DildoP:
                call RogueFace("bemused")
                ch_r "I'm just not into toys, [R_Petname]. . ."
            else:
                call RogueFace("bemused")
                ch_r "I don't think we need any toys, [R_Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in R_DailyActions:
                    call RogueFace("bemused")
                    ch_r "Yeah, ok, [R_Petname]."              
                    return
                "Maybe later?" if "no dildo" not in R_DailyActions:
                    call RogueFace("sexy")  
                    ch_r "Maybe I'll practice on my own time, [R_Petname]."
                    call Statup("Rogue", "Love", 80, 2)
                    call Statup("Rogue", "Inbt", 70, 2)  
                    if Taboo:                    
                        $ R_RecentActions.append("tabno")                      
                        $ R_DailyActions.append("tabno") 
                    $ R_RecentActions.append("no dildo")                      
                    $ R_DailyActions.append("no dildo") 
                    return
                "I think you'd like it. . .":             
                    if Approval:
                        call RogueFace("sexy")     
                        call Statup("Rogue", "Obed", 90, 2)
                        call Statup("Rogue", "Obed", 50, 2)
                        call Statup("Rogue", "Inbt", 70, 3) 
                        call Statup("Rogue", "Inbt", 40, 2) 
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You've got me there."]) 
                        ch_r "[Line]"
                        $ Line = 0                   
                        jump RDP_Prep
                    else:   
                        pass
                        
                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Rogue", 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                    if Approval > 1 or (Approval and R_Forced):
                        call RogueFace("sad")
                        call Statup("Rogue", "Love", 70, -5, 1)
                        call Statup("Rogue", "Love", 200, -5)                 
                        ch_r "Ok, fine. If we're going to do this, stick it in already."  
                        call Statup("Rogue", "Obed", 80, 4)
                        call Statup("Rogue", "Inbt", 80, 1) 
                        call Statup("Rogue", "Inbt", 60, 3)  
                        $ R_Forced = 1  
                        jump RDP_Prep
                    else:                              
                        call Statup("Rogue", "Love", 200, -20)     
                        $ R_RecentActions.append("angry")
                        $ R_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Rogue_Arms = 1  
    if "no dildo" in R_DailyActions:
            ch_r "Learn to take \"no\" for an answer, [R_Petname]."   
            $ R_RecentActions.append("angry")
            $ R_DailyActions.append("angry")   
    elif R_Forced:
            call RogueFace("angry", 1)
            ch_r "I'm not going to let you use that on me."
            call Statup("Rogue", "Lust", 200, 5)   
            if R_Love > 300: 
                    call Statup("Rogue", "Love", 70, -2)
            call Statup("Rogue", "Obed", 50, -2)     
            $ R_RecentActions.append("angry")
            $ R_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
            call RogueFace("angry", 1)         
            $ R_RecentActions.append("tabno")                       
            $ R_DailyActions.append("tabno") 
            ch_r "Not here!"     
            call Statup("Rogue", "Lust", 200, 5)  
            call Statup("Rogue", "Obed", 50, -3)  
    elif R_DildoP:
            call RogueFace("sad") 
            ch_r "Sorry, you can keep your toys to yourself."     
    else:
            call RogueFace("normal", 1)
            ch_r "No way."  
    $ R_RecentActions.append("no dildo")                      
    $ R_DailyActions.append("no dildo")  
    $ Tempmod = 0    
    return
                
label RDP_Prep: #Animation set-up 
    if Trigger2 == "dildo pussy":
        return
        
    if not R_Forced and Situation != "auto":
        $ Tempmod = 15 if R_Legs == "pants" else 0           
        call Rogue_Bottoms_Off
        if "angry" in R_RecentActions:
            return    
            
    $ Tempmod = 0      
    call R_Pussy_Launch("dildo pussy")
    if not R_DildoP:        
        if R_Forced:
            call Statup("Rogue", "Love", 90, -75)
            call Statup("Rogue", "Obed", 70, 60)
            call Statup("Rogue", "Inbt", 80, 35) 
        else:
            call Statup("Rogue", "Love", 90, 10)
            call Statup("Rogue", "Obed", 70, 20)
            call Statup("Rogue", "Inbt", 80, 45)
    if Taboo:
        $ R_Inbt += int(Taboo/10)  
        $ R_Lust += int(Taboo/5)
    
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0    
    $ Cnt = 0
    if Taboo:
        call DrainWord("Rogue","tabno")
    call DrainWord("Rogue","no dildo")
    $ R_RecentActions.append("dildo pussy")                      
    $ R_DailyActions.append("dildo pussy") 
    
label RDP_Cycle: #Repeating strokes    
    while Round >=0:  
        call Shift_Focus("Rogue") 
        call R_Pussy_Launch("dildo pussy")
        call RogueLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                               
                        "Slap her ass":                     
                                call R_Slap_Ass
                                jump RDP_Cycle  
                                
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
                                            if R_Action and MultiAction:
                                                call Rogue_Offhand_Set
                                                if Trigger2:
                                                     $ R_Action -= 1
                                            else:
                                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                                                
                                    "Shift primary action":
                                            if R_Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in her ass.":
                                                                $ Situation = "shift"
                                                                call RDP_After
                                                                call R_Insert_Ass    
                                                        "Just stick a finger in her ass without asking.":
                                                                $ Situation = "auto"
                                                                call RDP_After
                                                                call R_Insert_Ass                                           
                                                        "I want to shift the dildo to her ass.":
                                                                $ Situation = "shift"
                                                                call RDP_After
                                                                call R_Dildo_Ass   
                                                        "Never Mind":
                                                                jump RDP_Cycle
                                            else: 
                                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"           
                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call RDP_After
                                                call Rogue_Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask Rogue to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Rogue_Les_Change
                                            "Ask Rogue to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Rogue")  
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0    
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Rogue")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump RDP_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump RDP_Cycle 
                                            "Never mind":
                                                        jump RDP_Cycle 
                                    "Undress Rogue":
                                            call R_Undress   
                                    "Clean up Rogue (locked)" if not R_Spunk:
                                            pass  
                                    "Clean up Rogue" if R_Spunk:
                                            call Rogue_Cleanup("ask")                                         
                                    "Never mind":
                                            jump RDP_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call R_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump RDP_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call R_Pos_Reset
                                    $ Line = 0
                                    jump RDP_After
        #End menu (if Line)
        
        if R_Panties or R_Legs == "pants" or HoseNum("Rogue") >= 5: #This checks if Rogue wants to strip down.
                call R_Undress("auto")
            
        call Shift_Focus("Rogue")
        call Sex_Dialog("Rogue",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or R_Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PR_Cumming
                            if "angry" in R_RecentActions:  
                                call R_Pos_Reset
                                return    
                            call Statup("Rogue", "Lust", 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump RDP_After 
                            $ Line = "came"
     
                    if R_Lust >= 100:  
                            #If Rogue can cum                                             
                            call R_Cumming
                            if Situation == "shift" or "angry" in R_RecentActions:
                                jump RDP_After
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in R_RecentActions:#And Rogue is unsatisfied,  
                                "Rogue still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump RDP_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Rogue")            
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if R_SEXP >= 100 or ApprovalCheck("Rogue", 1200, "LO"):
            pass
        elif Cnt == (5 + R_DildoA):
                    $ R_Brows = "confused"
                    ch_r "What are you even doing down there?" 
        elif R_Lust >= 80:
                    pass
        elif Cnt == (15 + R_DildoA) and R_SEXP >= 15 and not ApprovalCheck("Rogue", 1500):
                    $ R_Brows = "confused"        
                    menu:
                        ch_r "[R_Petname], this is getting uncomfortable, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump RDP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump RDP_After
                        "No, this is fun.":   
                                if ApprovalCheck("Rogue", 1200) or ApprovalCheck("Rogue", 500, "O"):                        
                                    call Statup("Rogue", "Love", 200, -5)
                                    call Statup("Rogue", "Obed", 50, 3)                    
                                    call Statup("Rogue", "Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call RogueFace("angry", 1)   
                                    call R_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_r "Well if that's your attitude, I don't need your \"help\"."                         
                                    call Statup("Rogue", "Love", 50, -3, 1)
                                    call Statup("Rogue", "Love", 80, -4, 1)
                                    call Statup("Rogue", "Obed", 30, -1, 1)                    
                                    call Statup("Rogue", "Obed", 50, -1, 1)  
                                    $ R_RecentActions.append("angry")
                                    $ R_DailyActions.append("angry")   
                                    jump RDP_After
        #End Count check
           
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0)
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
label RDP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call R_Pos_Reset
        
    call RogueFace("sexy") 
    
    $ R_DildoP += 1  
    $ R_Action -=1   
    
    call Partner_Like("Rogue",2)
     
    if R_DildoP == 1:            
            $ R_SEXP += 10         
            if not Situation: 
                if R_Love >= 500 and "unsatisfied" not in R_RecentActions:
                    ch_r "Well I liked that. . ."
                elif R_Obed <= 500 and P_Focus <= 20:
                    call RogueFace("perplexed", 1)
                    ch_r "Did you like that?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_r "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# end R_Dildo Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Insert Ass    

label R_Dildo_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Rogue")
    call R_Dildo_Check
    if not _return:
        return 
      
    if R_Loose:
        $ Tempmod += 30   
    elif "anal" in R_RecentActions or "dildo anal" in R_RecentActions:
        $ Tempmod -= 20 
    elif "anal" in R_DailyActions or "dildo anal" in R_DailyActions:
        $ Tempmod -= 10
    elif (R_Anal + R_DildoA + R_Plug) > 0: #You've done it before
        $ Tempmod += 20   
        
    if R_Legs == "pants:": # she's got pants on.
        $ Tempmod -= 20   
        
    if R_Lust > 95:
        $ Tempmod += 20
    elif R_Lust > 85: #She's really horny
        $ Tempmod += 15
        
    if Situation == "shift":
        $ Tempmod += 10
    if "exhibitionist" in R_Traits:        
        $ Tempmod += (5*Taboo)
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 40  
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount   
    
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no dildo" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no dildo" in R_RecentActions else 0   
        
    $ Approval = ApprovalCheck("Rogue", 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)
    
    if Situation == "Rogue":                                                                  
            #Rogue auto-starts   
            if Approval > 2:                                                      # fix, add rogue auto stuff here
                if R_Legs == "skirt":
                    "Rogue grabs her dildo, hiking up her skirt as she does."
                    $ R_Upskirt = 1
                elif R_Legs == "pants":
                    "Rogue grabs her dildo, pulling down her pants as she does."              
                    $ R_Legs = 0
                else:
                    "Rogue grabs her dildo, rubbing is suggestively against her ass."
                $ R_SeenPanties = 1
                "She slides the tip against her asshole, and seems to want you to insert it."
                menu:
                    "What do you do?"
                    "Nothing.":                    
                        call Statup("Rogue", "Inbt", 80, 3) 
                        call Statup("Rogue", "Inbt", 50, 2)
                        "Rogue slides it in."
                    "Go for it.":       
                        call RogueFace("sexy", 1)                    
                        call Statup("Rogue", "Inbt", 80, 3) 
                        ch_p "Oh yeah, [R_Pet], let's do this."
                        call Rogue_Namecheck
                        "You grab the dildo and slide it in."
                        call Statup("Rogue", "Love", 85, 1)
                        call Statup("Rogue", "Obed", 90, 1)
                        call Statup("Rogue", "Obed", 50, 2)
                    "Ask her to stop.":
                        call RogueFace("surprised")       
                        call Statup("Rogue", "Inbt", 70, 1) 
                        ch_p "Let's not do that right now, [R_Pet]."
                        call Rogue_Namecheck
                        "Rogue sets the dildo down."
                        call Statup("Rogue", "Obed", 90, 1)
                        call Statup("Rogue", "Obed", 50, 1)
                        call Statup("Rogue", "Obed", 30, 2)
                        return            
                jump RDA_Prep
            else:                
                $ Tempmod = 0                               # fix, add rogue auto stuff here
                $ Trigger2 = 0
            return            
    
    if Situation == "auto":    
            "You rub the dildo across her body, and against her tight anus."
            call RogueFace("surprised", 1)
            
            if (R_DildoA and Approval) or (Approval > 1):                                                                      
                #this is not the first time you've had sex, or she's into it         
                "Rogue is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                call RogueFace("sexy")
                call Statup("Rogue", "Obed", 70, 3)
                call Statup("Rogue", "Inbt", 50, 3) 
                call Statup("Rogue", "Inbt", 70, 1) 
                ch_r "Ok, [R_Petname], let's do this."            
                jump RDA_Prep         
            else:                                                                                                            
                #she's questioning it
                $ R_Brows = "angry"                
                menu:
                    ch_r "Hey, what do you think you're doing back there?!" 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            call RogueFace("sexy", 1)
                            call Statup("Rogue", "Obed", 70, 3)
                            call Statup("Rogue", "Inbt", 50, 3) 
                            call Statup("Rogue", "Inbt", 70, 1) 
                            ch_r "Well, since you're be'in so nice about it, I guess we can give it a go. . ."
                            jump RDA_Prep
                        "You pull back before you really get it in."                    
                        call RogueFace("bemused", 1)
                        if R_DildoA:
                            ch_r "Well ok, [R_Petname], no harm done. Just give me a little warning next time." 
                        else:
                            ch_r "Well ok, [R_Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."                                               
                    "Just playing with my favorite toys.":                    
                        call Statup("Rogue", "Love", 80, -10, 1)  
                        call Statup("Rogue", "Love", 200, -10)
                        "You press it inside some more."                              
                        call Statup("Rogue", "Obed", 70, 3)
                        call Statup("Rogue", "Inbt", 50, 3) 
                        if not ApprovalCheck("Rogue", 700, "O", TabM=1): #Checks if Obed is 700+                           
                            call RogueFace("angry")
                            "Rogue shoves you away and slaps you in the face."
                            ch_r "Jackass!"
                            ch_r "If that's how you want to treat me, we're done here!"                                                  
                            call Statup("Rogue", "Love", 50, -10, 1)                        
                            call Statup("Rogue", "Obed", 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            if renpy.showing("Rogue_Doggy"):
                                call Rogue_Sex_Reset  
                            $ R_RecentActions.append("angry")
                            $ R_DailyActions.append("angry")                         
                        else:
                            call RogueFace("sad")
                            "Rogue doesn't seem to be into this, you're lucky she's so obedient."                        
                            jump RDA_Prep
            return             
    #end auto
   
    if not R_DildoA:                                                               
            #first time    
            call RogueFace("surprised", 1)
            $ R_Mouth = "kiss"
            ch_r "Hmmm, so you'd like to try out some toys?"    
            if R_Forced:
                call RogueFace("sad")
                ch_r "You had to go for the butt, uh?"
    
    if not R_Loose and ("dildo anal" in R_RecentActions or "anal" in R_RecentActions or "dildo anal" in R_DailyActions or "anal" in R_DailyActions):
            call RogueFace("bemused", 1)
            ch_r "I'm still a bit sore from earlier. . ."
            
    if not R_DildoA and Approval:                                                 
            #First time dialog        
            if R_Forced: 
                call RogueFace("sad")
                call Statup("Rogue", "Love", 70, -3, 1)
                call Statup("Rogue", "Love", 20, -2, 1)
            elif R_Love >= (R_Obed + R_Inbt):
                call RogueFace("sexy")
                $ R_Brows = "sad"
                $ R_Mouth = "smile" 
                ch_r "I haven't actually used one of these, back there before. . ."            
            elif R_Obed >= R_Inbt:
                call RogueFace("normal")
                ch_r "If that's what you want, [R_Petname]. . ."            
            else: # Uninhibited 
                call RogueFace("sad")
                $ R_Mouth = "smile"             
                ch_r "I guess it could be fun with a partner. . ."    
            
    elif Approval:                                                                       
            #Second time+ dialog
            if R_Forced: 
                call RogueFace("sad")
                call Statup("Rogue", "Love", 70, -3, 1)
                call Statup("Rogue", "Love", 20, -2, 1)
                ch_r "The toys again?"  
            elif not Taboo and "tabno" in R_DailyActions:        
                ch_r "Well, at least you got us some privacy this time. . ."   
            elif "dildo anal" in R_DailyActions and not R_Loose:
                pass
            elif "dildo anal" in R_DailyActions:
                call RogueFace("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "I'm still a bit sore from earlier.",
                    "You're going to wear me out."]) 
                ch_r "[Line]"
            elif R_DildoA < 3:        
                call RogueFace("sexy", 1)
                $ R_Brows = "confused"
                $ R_Mouth = "kiss"
                ch_r "You want to stick it in my ass again?"       
            else:       
                call RogueFace("sexy", 1)
                $ Rogue_Arms = 2
                $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my ass again?",
                    "You want me ta lube up your toy?"]) 
                ch_r "[Line]"
                $ Line = 0
            
    if Approval >= 2:                                                                  
            #She's into it. . .               
            if R_Forced:
                call RogueFace("sad")
                call Statup("Rogue", "Obed", 90, 1)
                call Statup("Rogue", "Inbt", 60, 1)
                ch_r "Ok, fine."    
            else:
                call RogueFace("sexy", 1)
                call Statup("Rogue", "Love", 90, 1)
                call Statup("Rogue", "Inbt", 50, 3) 
                $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."]) 
                ch_r "[Line]"
                $ Line = 0
            call Statup("Rogue", "Obed", 20, 1)
            call Statup("Rogue", "Obed", 60, 1)
            call Statup("Rogue", "Inbt", 70, 2) 
            jump RDA_Prep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            call RogueFace("angry")
            if "no dildo" in R_RecentActions:  
                ch_r "What part of \"no,\" did you not get, [R_Petname]?"
            elif Taboo and "tabno" in R_DailyActions and "no dildo" in R_DailyActions:
                ch_r "Stop swinging that thing around in public!"  
            elif "no dildo" in R_DailyActions:       
                ch_r "I already told you \"no,\" [R_Petname]."
            elif Taboo and "tabno" in R_DailyActions:  
                ch_r "I already told you that I wouldn't do that out here!"  
            elif not R_DildoA:
                call RogueFace("bemused")
                ch_r "I'm just not into toys, [R_Petname]. . ."
            elif not R_Loose and "dildo anal" not in R_DailyActions:
                call RogueFace("perplexed")
                ch_r "You could have been a bit more gentle last time, [R_Petname]. . ."
            else:
                call RogueFace("bemused")
                ch_r "I don't think we need any toys, [R_Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in R_DailyActions:
                    call RogueFace("bemused")
                    ch_r "Yeah, ok, [R_Petname]."              
                    return
                "Maybe later?" if "no dildo" not in R_DailyActions:
                    call RogueFace("sexy")  
                    ch_r "Maybe I'll practice on my own time, [R_Petname]."
                    call Statup("Rogue", "Love", 80, 2)
                    call Statup("Rogue", "Inbt", 70, 2)  
                    if Taboo:                    
                        $ R_RecentActions.append("tabno")                      
                        $ R_DailyActions.append("tabno") 
                    $ R_RecentActions.append("no dildo")                      
                    $ R_DailyActions.append("no dildo") 
                    return
                "I think you'd like it. . .":             
                    if Approval:
                        call RogueFace("sexy")     
                        call Statup("Rogue", "Obed", 90, 2)
                        call Statup("Rogue", "Obed", 50, 2)
                        call Statup("Rogue", "Inbt", 70, 3) 
                        call Statup("Rogue", "Inbt", 40, 2) 
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You've got me there."]) 
                        ch_r "[Line]"
                        $ Line = 0                   
                        jump RDA_Prep
                    else:   
                        pass
                        
                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Rogue", 1050, "OI", TabM = 3) # 105, 120, 135, -120(225)
                    if Approval > 1 or (Approval and R_Forced):
                        call RogueFace("sad")
                        call Statup("Rogue", "Love", 70, -5, 1)
                        call Statup("Rogue", "Love", 200, -5)                 
                        ch_r "Ok, fine. If we're going to do this, stick it in already."  
                        call Statup("Rogue", "Obed", 80, 4)
                        call Statup("Rogue", "Inbt", 80, 1) 
                        call Statup("Rogue", "Inbt", 60, 3)  
                        $ R_Forced = 1  
                        jump RDA_Prep
                    else:                              
                        call Statup("Rogue", "Love", 200, -20)    
                        $ R_RecentActions.append("angry")
                        $ R_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Rogue_Arms = 1   
    if "no dildo" in R_DailyActions:
            ch_r "Learn to take \"no\" for an answer, [R_Petname]."   
            $ R_RecentActions.append("angry")
            $ R_DailyActions.append("angry")   
    elif R_Forced:
            call RogueFace("angry", 1)
            ch_r "I'm not going to let you use that on me."
            call Statup("Rogue", "Lust", 200, 5)    
            if R_Love > 300: 
                    call Statup("Rogue", "Love", 70, -2)
            call Statup("Rogue", "Obed", 50, -2)   
            $ R_RecentActions.append("angry")
            $ R_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
            call RogueFace("angry", 1)          
            $ R_RecentActions.append("tabno")                       
            $ R_DailyActions.append("tabno") 
            ch_r "Not here!"     
            call Statup("Rogue", "Lust", 200, 5)  
            call Statup("Rogue", "Obed", 50, -3)  
    elif not R_Loose and "dildo anal" in R_DailyActions:
            call RogueFace("bemused")
            ch_r "Sorry, I just need a little break back there, [R_Petname]."    
    elif R_DildoA:
            call RogueFace("sad") 
            ch_r "Sorry, you can keep your toys out of there."     
    else:
            call RogueFace("normal", 1)
            ch_r "No way." 
    $ R_RecentActions.append("no dildo")                      
    $ R_DailyActions.append("no dildo")   
    $ Tempmod = 0    
    return
                
label RDA_Prep: #Animation set-up 
    if Trigger2 == "dildo anal":
        return
        
    if not R_Forced and Situation != "auto":
        $ Tempmod = 20 if R_Legs == "pants" else 0           
        call Rogue_Bottoms_Off
        if "angry" in R_RecentActions:
            return    
            
    $ Tempmod = 0      
    call R_Pussy_Launch("dildo anal")
    if not R_DildoA:        
        if R_Forced:
            call Statup("Rogue", "Love", 90, -75)
            call Statup("Rogue", "Obed", 70, 60)
            call Statup("Rogue", "Inbt", 80, 35) 
        else:
            call Statup("Rogue", "Love", 90, 10)
            call Statup("Rogue", "Obed", 70, 20)
            call Statup("Rogue", "Inbt", 80, 45)
    if Taboo:
        $ R_Inbt += int(Taboo/10)  
        $ R_Lust += int(Taboo/5)
    
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0    
    $ Cnt = 0
    if Taboo:
        call DrainWord("Rogue","tabno")
    call DrainWord("Rogue","no dildo")
    $ R_RecentActions.append("dildo anal")                      
    $ R_DailyActions.append("dildo anal") 
    
label RDA_Cycle: #Repeating strokes    
    while Round >=0:  
        call Shift_Focus("Rogue") 
        call R_Pussy_Launch("dildo anal")
        call RogueLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                               
                        "Slap her ass":                     
                                call R_Slap_Ass
                                jump RDA_Cycle  
                                
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
                                            if R_Action and MultiAction:
                                                call Rogue_Offhand_Set
                                                if Trigger2:
                                                     $ R_Action -= 1
                                            else:
                                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                                                
                                    "Shift primary action":
                                            if R_Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in her pussy.":
                                                                $ Situation = "shift"
                                                                call RDA_After
                                                                call R_Fondle_Pussy    
                                                        "Just stick a finger in her pussy without asking.":
                                                                $ Situation = "auto"
                                                                call RDA_After
                                                                call R_Fondle_Pussy                                           
                                                        "I want to shift the dildo to her pussy.":
                                                                $ Situation = "shift"
                                                                call RDA_After
                                                                call R_Dildo_Pussy 
                                                        "Never Mind":
                                                                jump RDA_Cycle
                                            else: 
                                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"           
                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call RDA_After
                                                call Rogue_Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask Rogue to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Rogue_Les_Change
                                            "Ask Rogue to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Rogue")  
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0    
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Rogue")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump RDA_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump RDA_Cycle 
                                            "Never mind":
                                                        jump RDA_Cycle 
                                    "Undress Rogue":
                                            call R_Undress   
                                    "Clean up Rogue (locked)" if not R_Spunk:
                                            pass  
                                    "Clean up Rogue" if R_Spunk:
                                            call Rogue_Cleanup("ask")                                         
                                    "Never mind":
                                            jump RDA_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call R_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump RDA_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call R_Pos_Reset
                                    $ Line = 0
                                    jump RDA_After
        #End menu (if Line)
        
        if R_Panties or R_Legs == "pants" or HoseNum("Rogue") >= 5: #This checks if Rogue wants to strip down.
                call R_Undress("auto")
            
        call Shift_Focus("Rogue")
        call Sex_Dialog("Rogue",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or R_Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PR_Cumming
                            if "angry" in R_RecentActions:  
                                call R_Pos_Reset
                                return    
                            call Statup("Rogue", "Lust", 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump RDA_After 
                            $ Line = "came"
     
                    if R_Lust >= 100:  
                            #If Rogue can cum                                             
                            call R_Cumming
                            if Situation == "shift" or "angry" in R_RecentActions:
                                jump RDA_After
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in R_RecentActions:#And Rogue is unsatisfied,  
                                "Rogue still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump RDA_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Rogue")            
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if R_SEXP >= 100 or ApprovalCheck("Rogue", 1200, "LO"):
            pass
        elif Cnt == (5 + R_DildoA):
                    $ R_Brows = "confused"
                    ch_r "What are you even doing down there?" 
        elif R_Lust >= 80:
                    pass
        elif Cnt == (15 + R_DildoA) and R_SEXP >= 15 and not ApprovalCheck("Rogue", 1500):
                    $ R_Brows = "confused"        
                    menu:
                        ch_r "[R_Petname], this is getting uncomfortable, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump RDA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump RDA_After
                        "No, this is fun.":   
                                if ApprovalCheck("Rogue", 1200) or ApprovalCheck("Rogue", 500, "O"):                        
                                    call Statup("Rogue", "Love", 200, -5)
                                    call Statup("Rogue", "Obed", 50, 3)                    
                                    call Statup("Rogue", "Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call RogueFace("angry", 1)   
                                    call R_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_r "Well if that's your attitude, I don't need your \"help\"."                         
                                    call Statup("Rogue", "Love", 50, -3, 1)
                                    call Statup("Rogue", "Love", 80, -4, 1)
                                    call Statup("Rogue", "Obed", 30, -1, 1)                    
                                    call Statup("Rogue", "Obed", 50, -1, 1)  
                                    $ R_RecentActions.append("angry")
                                    $ R_DailyActions.append("angry")   
                                    jump RDA_After
        #End Count check
           
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0)
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
    
label RDA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call R_Pos_Reset
        
    call RogueFace("sexy") 
    
    $ R_DildoA += 1  
    $ R_Action -=1            
    
    call Partner_Like("Rogue",2)
     
    if R_DildoA == 1:            
            $ R_SEXP += 10         
            if not Situation: 
                if R_Love >= 500 and "unsatisfied" not in R_RecentActions:
                    if R_Loose:
                        ch_r "Well I liked that. . ."
                    else:
                        ch_r "Well that was a bit rough. . ."
                elif R_Obed <= 500 and P_Focus <= 20:
                    call RogueFace("perplexed", 1)
                    ch_r "Did you like that?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_r "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# end R_Dildo Ass /////////////////////////////////////////////////////////////////////////////

label R_Vibrator_Check:                                                                                 #fix this whole section is copy/paste unfinished
    if "vibrator" in P_Inventory:   
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in R_Inventory:
        "You ask Rogue to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1



## R_Footjob //////////////////////////////////////////////////////////////////////
label R_Footjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Rogue")
    if R_Foot >= 7: # She loves it
        $ Tempmod += 10
    elif R_Foot >= 3: #You've done it before several times
        $ Tempmod += 7
    elif R_Foot: #You've done it before
        $ Tempmod += 3
        
    if R_Addict >= 75 and R_Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 10
    if R_Addict >= 75:
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 15
    if "exhibitionist" in R_Traits:
        $ Tempmod += (3*Taboo)    
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 40 
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount    
    
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no foot" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no foot" in R_RecentActions else 0    
        
    $ Approval = ApprovalCheck("Rogue", 1250, TabM = 3) # 110, 125, 140, Taboo -120(230)
    
    if Situation == "Rogue":                                                                  #Rogue auto-starts   
        if Approval > 2:                                                      # fix, add rogue auto stuff here
            "Rogue leans forward and starts rubbing your cock between her feet."
            menu:
                "What do you do?"
                "Nothing.":                    
                    call Statup("Rogue", "Inbt", 70, 3) 
                    call Statup("Rogue", "Inbt", 30, 2)                     
                    "Rogue continues her actions."
                "Praise her.":       
                    call RogueFace("sexy", 1)                    
                    call Statup("Rogue", "Inbt", 70, 3) 
                    ch_p "Oooh, that's good, [R_Pet]."
                    call Rogue_Namecheck
                    "Rogue continues her actions."
                    call Statup("Rogue", "Love", 80, 1)
                    call Statup("Rogue", "Obed", 90, 1)
                    call Statup("Rogue", "Obed", 50, 2)
                "Ask her to stop.":
                    call RogueFace("surprised")       
                    call Statup("Rogue", "Inbt", 70, 1) 
                    ch_p "Let's not do that for now, [R_Pet]."
                    call Rogue_Namecheck
                    "Rogue puts it down."
                    call Statup("Rogue", "Obed", 90, 1)
                    call Statup("Rogue", "Obed", 50, 1)
                    call Statup("Rogue", "Obed", 30, 2)
                    return            
            if Trigger:
                $ Trigger3 = "foot"
                return
            jump RFJ_Prep
        else:                
            $ Tempmod = 0                               # fix, add rogue auto stuff here
            $ Trigger2 = 0
            return            
    
    if not R_Foot and "no foot" not in R_RecentActions:        
        call RogueFace("confused", 2)
        ch_r "Huh, so like a handy, but with my feet?"
        $ R_Blush = 1
            
    if not R_Foot and Approval:                                                 #First time dialog        
        if R_Forced: 
            call RogueFace("sad",1)
            call Statup("Rogue", "Love", 70, -3, 1)
            call Statup("Rogue", "Love", 20, -2, 1)
        elif R_Love >= (R_Obed + R_Inbt):
            call RogueFace("sexy",1)
            $ R_Brows = "sad"
            $ R_Mouth = "smile" 
            ch_r "If that's what you like. . ."            
        elif R_Obed >= R_Inbt:
            call RogueFace("normal",1)
            ch_r "If that's what you want, [R_Petname]. . ."            
        elif R_Addict >= 50:
            call RogueFace("manic", 1)
            ch_r "I guess. . ."  
        else: # Uninhibited 
            call RogueFace("lipbite",1)    
            ch_r "Sure. . ."    
            
    elif Approval:                                                                       #Second time+ dialog
        if R_Forced: 
            call RogueFace("sad")
            call Statup("Rogue", "Love", 70, -3, 1)
            call Statup("Rogue", "Love", 20, -2, 1)
            ch_r "That's it?" 
        elif not Taboo and "tabno" in R_DailyActions:        
            ch_r "I guess here would be ok. . ."    
        elif "foot" in R_RecentActions:
            call RogueFace("sexy", 1)
            ch_r "I don't want to wear them out. . ."
            jump RFJ_Prep
        elif "foot" in R_DailyActions:
            call RogueFace("sexy", 1)
            $ Line = renpy.random.choice(["Another one?",   
                "You're going to give me calluses.", 
                "Didn't get enough earlier?",
                "My feet are a bit sore from earlier.",
                "My feet are kinda sore from earlier."]) 
            ch_r "[Line]"
        elif R_Foot < 3:        
            call RogueFace("sexy", 1)
            $ R_Brows = "confused"
            $ R_Mouth = "kiss"
            ch_r "Again?"        
        else:       
            call RogueFace("sexy", 1)
            $ Rogue_Arms = 2
            $ Line = renpy.random.choice(["You want me to use my feet?",                 
                "So you'd like another foot rub?",                 
                "So you'd like me to. . . [she rubs her foot along your leg]?", 
                "So you'd like another foot rub?"]) 
            ch_r "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if R_Forced:
            call RogueFace("sad")
            call Statup("Rogue", "Obed", 90, 1)
            call Statup("Rogue", "Inbt", 60, 1)
            ch_r ". . . Ok, if that's what you want." 
        elif "no foot" in R_DailyActions:               
            ch_r "Fine!"   
        else:
            call RogueFace("sexy", 1)
            call Statup("Rogue", "Love", 90, 1)
            call Statup("Rogue", "Inbt", 50, 3) 
            $ Line = renpy.random.choice(["Sure, I guess.",                 
                "Okay.",                 
                "Ok, lemme see it.", 
                "I guess. . .",
                "Ok. . . [She gestures for you to come over].",
                "Heh, ok, fine."]) 
            ch_r "[Line]"
            $ Line = 0
        call Statup("Rogue", "Obed", 20, 1)
        call Statup("Rogue", "Obed", 60, 1)
        call Statup("Rogue", "Inbt", 70, 2) 
        jump RFJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call RogueFace("angry")
        if "no foot" in R_RecentActions:  
            ch_r "I just said \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions and "no foot" in R_DailyActions: 
            ch_r "Not in public!"  
        elif "no foot" in R_DailyActions:       
            ch_r "I told you \"no\" earlier [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions:  
            ch_r "I said not in public!"     
        elif not R_Foot:
            call RogueFace("bemused")
            ch_r "Well I don't know about that, [R_Petname]. . ."
        else:
            call RogueFace("bemused")
            ch_r "Maybe not right now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no foot" in R_DailyActions:
                call RogueFace("bemused")
                ch_r "No problem."              
                return
            "Maybe later?" if "no foot" not in R_DailyActions:
                call RogueFace("sexy")  
                ch_r ". . ."
                ch_r "I guess?"
                call Statup("Rogue", "Love", 80, 2)
                call Statup("Rogue", "Inbt", 70, 2)   
                if Taboo:                    
                    $ R_RecentActions.append("tabno")                      
                    $ R_DailyActions.append("tabno") 
                $ R_RecentActions.append("no foot")                      
                $ R_DailyActions.append("no foot")            
                return
            "I'd really appreciate it. . .":             
                if Approval:
                    call RogueFace("sexy")     
                    call Statup("Rogue", "Obed", 90, 2)
                    call Statup("Rogue", "Obed", 50, 2)
                    call Statup("Rogue", "Inbt", 70, 3) 
                    call Statup("Rogue", "Inbt", 40, 2) 
                    $ Line = renpy.random.choice(["Sure, I guess.",                 
                        "Okay.",                 
                        "Ok, lemme see it.", 
                        "I guess. . .",
                        "Ok. . . [She gestures for you to come over].",
                        "Heh, ok, fine."]) 
                    ch_r "[Line]"
                    $ Line = 0                   
                    jump RFJ_Prep
                else:   
                    pass
                    
            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Rogue", 400, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and R_Forced):
                    call RogueFace("sad")
                    call Statup("Rogue", "Love", 70, -5, 1)
                    call Statup("Rogue", "Love", 200, -2)                 
                    ch_r "Ok, fine."  
                    call Statup("Rogue", "Obed", 50, 4)
                    call Statup("Rogue", "Inbt", 80, 1) 
                    call Statup("Rogue", "Inbt", 60, 3)  
                    $ R_Forced = 1  
                    jump RFJ_Prep
                else:                              
                    call Statup("Rogue", "Love", 200, -15)     
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Rogue_Arms = 1 
    if "no foot" in R_DailyActions:
        call RogueFace("angry", 1)
        ch_r "I'aint tellin you again."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1)
        ch_r "Not even with my feet."
        call Statup("Rogue", "Lust", 200, 5)    
        if R_Love > 300: 
                call Statup("Rogue", "Love", 70, -2)
        call Statup("Rogue", "Obed", 50, -2)    
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call RogueFace("angry", 1)          
        $ R_DailyActions.append("tabno") 
        ch_r "Not in such an exposed place, [R_Petname]."
        call Statup("Rogue", "Lust", 200, 5)  
        call Statup("Rogue", "Obed", 50, -3)   
    elif R_Foot:
        call RogueFace("sad") 
        ch_r "Not right now, [R_Petname]. . ."       
    else:
        call RogueFace("normal", 1)
        ch_r "That isn't really how I planned to use my feet today"  
    $ R_RecentActions.append("no foot")                      
    $ R_DailyActions.append("no foot") 
    $ Tempmod = 0    
    return
    

label RFJ_Prep:
    if Trigger2 == "foot": 
        return
    
    if Taboo:
        $ R_Inbt += int(Taboo/10)  
        $ R_Lust += int(Taboo/5)
                
    call RogueFace("sexy")
    if R_Forced:
        call RogueFace("sad")
    elif R_Foot:
        $ R_Brows = "confused"
        $ R_Eyes = "sexy"
        $ R_Mouth = "smile"
    
    call Seen_First_Peen("Rogue",Partner)
    
    if not R_Foot:        
        if R_Forced:
            call Statup("Rogue", "Love", 90, -20)
            call Statup("Rogue", "Obed", 70, 25)
            call Statup("Rogue", "Inbt", 80, 30) 
        else:
            call Statup("Rogue", "Love", 90, 5)
            call Statup("Rogue", "Obed", 70, 20)
            call Statup("Rogue", "Inbt", 80, 20)     
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Rogue","tabno")
    call DrainWord("Rogue","no foot")
    $ R_RecentActions.append("foot")                      
    $ R_DailyActions.append("foot") 
    
  
label RFJ_Cycle:    
    while Round >=0:  
        call Shift_Focus("Rogue") 
        call Rogue_Doggy_Launch("foot")    
        call RogueLust   
        
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
                                            if R_Action and MultiAction:
                                                call Rogue_Offhand_Set
                                                if Trigger2:
                                                     $ R_Action -= 1
                                            else:
                                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                                                   
                                    "Shift primary action":
                                            if R_Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    if R_Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call RFJ_After                
                                                                        call R_Blowjob
                                                                    else:
                                                                        ch_r "Actually I'm getting a bit worn out, let's finish up here. . ."
                                                        "How about a handjob?":
                                                                    if R_Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call RFJ_After                
                                                                        call R_Handjob
                                                                    else:
                                                                        ch_r "Actually I'm getting a bit worn out, let's finish up here. . ."
                                                                        
                                                        "How about a titjob?":
                                                                    if R_Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call RFJ_After
                                                                        call R_Titjob
                                                                    else:
                                                                        ch_r "Actually I'm getting a bit worn out, let's finish up here. . ."
                                                                
                                                        "Never Mind":
                                                                jump RFJ_Cycle
                                            else: 
                                                ch_r "I'm getting kinda tired, so maybe we could wrap this up?"           
                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask Rogue to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Rogue_Les_Change
                                            "Ask Rogue to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Rogue")  
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0    
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Rogue")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump RFJ_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump RFJ_Cycle 
                                            "Never mind":
                                                        jump RFJ_Cycle 
                                    "Undress Rogue":
                                            call R_Undress   
                                    "Clean up Rogue (locked)" if not R_Spunk:
                                            pass  
                                    "Clean up Rogue" if R_Spunk:
                                            call Rogue_Cleanup("ask")                                         
                                    "Never mind":
                                            jump RFJ_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Rogue_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump RFJ_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Rogue_Sex_Reset
                                    $ Line = 0
                                    jump RFJ_After
        #End menu (if Line)
        
        call Shift_Focus("Rogue")
        call Sex_Dialog("Rogue",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or R_Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PR_Cumming
                            if "angry" in R_RecentActions:  
                                call Rogue_Sex_Reset
                                return    
                            call Statup("Rogue", "Lust", 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump RFJ_After 
                            $ Line = "came"
     
                    if R_Lust >= 100:  
                            #If Rogue can cum                                             
                            call R_Cumming
                            if Situation == "shift" or "angry" in R_RecentActions:
                                jump RFJ_After
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in R_RecentActions:#And Rogue is unsatisfied,  
                                "Rogue still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump RFJ_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Rogue")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if Cnt == 20:
                    $ R_Brows = "angry"        
                    menu:
                        ch_r "Ow, i'm not used to this. Mind if we take a break?"
                        "How about a BJ?" if R_Action and MultiAction:
                                $ Situation = "shift"
                                call RFJ_After
                                call R_Blowjob   
                        "How about a Handy?" if R_Action and MultiAction:
                                $ Situation = "shift"
                                call RFJ_After
                                call R_Handjob  
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump RFJ_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Rogue_Sex_Reset
                                $ Situation = "shift"
                                jump RFJ_After
                        "No, get back down there.":
                                if ApprovalCheck("Rogue", 1200) or ApprovalCheck("Rogue", 500, "O"):
                                    call Statup("Rogue", "Love", 200, -5)
                                    call Statup("Rogue", "Obed", 50, 3)                    
                                    call Statup("Rogue", "Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    call RogueFace("angry", 1)   
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_r "Well if that's your attitude you can handle your own business."
                                    call Statup("Rogue", "Love", 50, -3, 1)
                                    call Statup("Rogue", "Love", 80, -4, 1)
                                    call Statup("Rogue", "Obed", 30, -1, 1)                    
                                    call Statup("Rogue", "Obed", 50, -1, 1)                     
                                    $ R_RecentActions.append("angry")
                                    $ R_DailyActions.append("angry")   
                                    jump RFJ_After
        elif Cnt == 10 and R_SEXP <= 100 and not ApprovalCheck("Rogue", 1200, "LO"):
                    $ R_Brows = "confused"
                    ch_r "Can we be done with this now? I'm getting sore."         
        #End Count check
                   
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0)
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
label RFJ_After:
    call RogueFace("sexy") 
    
    $ R_Foot += 1  
    $ R_Action -=1
    $ R_Addictionrate += 1
    if "addictive" in P_Traits:
        $ R_Addictionrate += 1        
    call Statup("Rogue", "Lust", 90, 5)
    
    call Partner_Like("Rogue",1)
    
    if "Roguepedi" in Achievements:
            pass  
    elif R_Foot >= 10:
            call RogueFace("smile", 1)
            ch_r "I guess I've gotten used to this foot thing."
            $ Achievements.append("Roguepedi")
            $ R_SEXP += 5          
    elif R_Foot == 1:            
            $ R_SEXP += 10
            if R_Love >= 500:
                $ R_Mouth = "smile"
                ch_r "That was a real interesting experience. . ."
            elif P_Focus <= 20:
                $ R_Mouth = "sad"
                ch_r "Did that work for you?"
    elif R_Foot == 5:
                ch_r "I kinda like this sensation." 
                ch_r "Never thought about touching people with my feet."                  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_r "Mmm, so what else did you have in mind?"
    else:
        call Rogue_Sex_Reset    
    call Checkout
    return

## end R_Footjob //////////////////////////////////////////////////////////////////////



# Start R_Lesbian ////////////////////////////////////////////////////////////////////////
label R_Les_Interupted:    
        # Called if you catch them fucking 
        if "unseen" not in R_RecentActions:
                if R_Org < 3 and R_Action:                
                    menu:
                        "Did you want to stop them?"
                        "Yeah.":
                            pass
                        "No, let them keep going.":
                            $ R_Action -= 1 if R_Action > 0 else 0
                            jump R_Les_Cycle 
                else:
                    ch_r "Ok, that's probably enough of that. . ."
                jump R_Les_After
        call DrainWord("Rogue","unseen",1,0) #She sees you, so remove unseens
        call DrainWord(Partner,"unseen",1,0) #She sees you, so remove unseens
        call RogueFace("surprised", 2)
        "Suddenly, Rogue jerks up from what she was doing with a start, and gives [Partner] a nudge."
        ch_r "Um, [Playername], how long have you been watchin?"
        call RogueFace("surprised", 1)
        $ R_Action -= 1 if R_Action > 0 else 0
        call Checkout(1)
        $ Line = 0
    
        #If you've been jacking it
        if Trigger2 == "jackin":
                $ R_Eyes = "down"
                menu:
                    ch_r "And why is your cock out like that?!"
                    "Long enough, it was an excellent show.":   
                            call RogueFace("sexy")
                            call Statup("Rogue", "Obed", 50, 3)
                            call Statup("Rogue", "Obed", 70, 2)
                            "Rogue glances over at [Partner]."
                            ch_r "Well, I imagine it was. . ."
                            if R_Love >= 800 or R_Obed >= 500 or R_Inbt >= 500:
                                $ Tempmod += 10
                                call Statup("Rogue", "Lust", 90, 5)
                                ch_r "And the view from this angle ain't so bad either. . ."  
                            
                    "I. . . just got here?":
                            call RogueFace("angry")                   
                            call Statup("Rogue", "Love", 70, 2)
                            call Statup("Rogue", "Love", 90, 1)
                            call Statup("Rogue", "Obed", 50, 2)
                            call Statup("Rogue", "Obed", 70, 2)
                            "She looks pointedly at your cock,"
                            ch_r "Suuure . . ."   
                            if R_Love >= 800 or R_Obed >= 500 or R_Inbt >= 500:
                                    $ Tempmod += 10
                                    call Statup("Rogue", "Lust", 90, 5)
                                    call RogueFace("bemused", 1)
                                    ch_r "-but I guess we were pretty tempting. . ."   
                            else:
                                    $ Tempmod -= 10
                                    call Statup("Rogue", "Lust", 200, -5)
                call Seen_First_Peen("Rogue",Partner)  
        else:         
                #you haven't been jacking it                            
                menu:
                    ch_r "H- how long you been stand'in there, [R_Petname]?"
                    "Long enough.":   
                            call RogueFace("sexy", 1)
                            call Statup("Rogue", "Obed", 50, 3)
                            call Statup("Rogue", "Obed", 70, 2)
                            ch_r "Well I hope you got a good show out of it. . ."
                    "I just got here.":
                            call RogueFace("bemused", 1)
                            call Statup("Rogue", "Love", 70, 2)
                            call Statup("Rogue", "Love", 90, 1)                    
                            ch_r "A likely story . . ."   
                            call Statup("Rogue", "Obed", 50, 2)
                            call Statup("Rogue", "Obed", 70, 2)    
                                
        if not ApprovalCheck("Rogue", 1350):
                #If she doesn't like you enough to have you around. . .
                call Statup("Rogue", "Love", 200, -5)
                call RogueFace("angry")
                $ R_RecentActions.append("angry")
                $ R_DailyActions.append("angry")
                ch_r "You should get out of here right now, and maybe learn ta knock?"
                $ renpy.pop_call()
                $ renpy.pop_call()
                if bg_current == "bg player":                                        
                    jump Campus_Map  
                else:
                    jump Player_Room  
        
        if Round <= 10:
            ch_r "It's getting too late to do much about it right now though."
            return
        $ Situation = "interrupted"
    
label R_LesScene(Bonus = 0): #Repeating strokes
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Rogue")
    if R_LesWatch:
        $ Tempmod += 10
    elif R_Les:
        $ Tempmod += 5
    if R_SEXP >= 50:
        $ Tempmod += 25
    elif R_SEXP >= 30:
        $ Tempmod += 15
    elif R_SEXP >= 15:
        $ Tempmod += 5
        
    if R_Lust >= 90:
        $ Tempmod += 5
    elif R_Lust >= 75:
        $ Tempmod += 5
        
    elif R_Inbt >= 750:
        $ Tempmod += 5
        
    if "exhibitionist" in R_Traits:      
        $ Tempmod += (3*Taboo) 
        
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10        
    elif "ex" in R_Traits:
        $ Tempmod -= 40  
        
    if K_Loc == bg_current:
            #if it's Kitty. . .
            $ K_RecentActions.append("noticed Rogue")
            $ R_RecentActions.append("noticed Kitty")
            $ Partner = "Kitty"  
            if R_LikeKitty >= 900:
                    $ Bonus += 150
            elif R_LikeKitty >= 800 or "poly Kitty" in R_Traits:
                    $ Bonus += 100
            elif R_LikeKitty >= 700:
                    $ Bonus += 50
            elif R_LikeKitty <= 200:
                    $ Bonus -= 200
            elif R_LikeKitty <= 500:
                    $ Bonus -= 100
            call DrainWord("Kitty","unseen",1,0) #She sees you, so remove unseens
    elif E_Loc == bg_current:
            #if it's Emma. . .
            $ E_RecentActions.append("noticed Rogue")
            $ R_RecentActions.append("noticed Emma")
            $ Partner = "Emma"  
            if R_LikeEmma >= 900:
                    $ Bonus += 150
            elif R_LikeEmma >= 800 or "poly Emma" in R_Traits:
                    $ Bonus += 100
            elif R_LikeEmma >= 700:
                    $ Bonus += 50
            elif R_LikeEmma <= 200:
                    $ Bonus -= 200
            elif R_LikeEmma <= 500:
                    $ Bonus -= 100
            call DrainWord("Emma","unseen",1,0) #She sees you, so remove unseens
    elif L_Loc == bg_current:
            #if it's Laura. . .
            $ L_RecentActions.append("noticed Rogue")
            $ R_RecentActions.append("noticed Laura")
            $ Partner = "Laura"  
            if R_LikeLaura >= 900:
                    $ Bonus += 150
            elif R_LikeLaura >= 800 or "poly Laura" in R_Traits:
                    $ Bonus += 100
            elif R_LikeLaura >= 700:
                    $ Bonus += 50
            elif R_LikeLaura <= 200:
                    $ Bonus -= 200
            elif R_LikeLaura <= 500:
                    $ Bonus -= 100
            call DrainWord("Laura","unseen",1,0) #She sees you, so remove unseens
            
    if bg_current in ("bg player", "bg rogue", "bg kitty", "bg emma"):
        $ Taboo == 0
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount   
        
    $ Approval = ApprovalCheck("Rogue", 1350, TabM = 2, Bonus = Bonus) # 1350, 1500, 1650, Taboo -800
    
    call DrainWord("Rogue","unseen",1,0) #She sees you, so remove unseens
    
    if Situation == "interrupted":    
        menu:
            extend ""
            "I guess I should probably get going then. . .":
                    call Statup("Rogue", "Love", 80, 3)
                    if Approval >= 2:
                            # if Rogue is very much in
                            ch_r "Well, I didn't say you had to leave. . ."
                            if K_Loc == bg_current:
                                    call K_Les_Response("Rogue",3,B2=Bonus)                            
                            elif E_Loc == bg_current:
                                    call E_Les_Response("Rogue",3,B2=Bonus)                        
                            elif L_Loc == bg_current:
                                    call L_Les_Response("Rogue",3,B2=Bonus) 
                            if not _return:
                                    return
                    else:
                            # If Rogue is only so/so, but Kitty is on board, she tries to convince Rogue
                            if K_Loc == bg_current:
                                    call K_Les_Response("Rogue",1,B2=Bonus)                            
                            elif E_Loc == bg_current:
                                    call E_Les_Response("Rogue",1,B2=Bonus)                         
                            elif L_Loc == bg_current:
                                    call L_Les_Response("Rogue",1,B2=Bonus)                            
                            if not _return:
                                    #this is the default reaction if Kitty is not into it either
                                    if Approval:
                                        ch_r "I mean, you can hang out. . ."
                                        return
                                    else:
                                        ch_r "Yeah, that's probably a good idea. . ."  
                                        $ renpy.pop_call()
                                        $ renpy.pop_call()
                                        if bg_current == "bg player":                                        
                                            jump Campus_Map  
                                        else:
                                            jump Player_Room  
                            elif not Approval:
                                    ch_r "I'm sorry [R_Petname], I just am not interested in putting on a show."
                                    return                            
                            elif not R_Action:
                                    ch_r "I'm sorry [R_Petname], I'm just too tuckered out right now. . ."
                                    return        
                            else:
                                    ch_r "Ok, fine."    
                    #if it passed the hurdles. . .
                    jump R_Les_Prep
            "So maybe I could join you girls?" if P_Semen and R_Action:
                    call RogueFace("sexy")
                    ch_r "Well what did you have in mind?"    
                    $ Situation = "join"
                    return                      #returns to sexmenu=
            "So maybe I could watch a bit longer?":
                    call RogueFace("bemused", 1)   
    #End "Interrupted" content.
    
    #first time
    if not R_LesWatch:                                                                
            call RogueFace("surprised", 1)
            $ R_Mouth = "kiss"
            ch_r "You want me and [Partner] to hook up, while you watch?"
            if R_Forced:
                call RogueFace("sad")
                ch_r "And {i}just{/i} watch?"
                
    if Approval and "touch" not in R_Traits:
            ch_r "Well, I wouldn't want to hurt her. Remember my. . . ability?"
            ch_p "Don't worry, I can keep it turned off."
            ch_r "Oh, well I guess. . ."
                     
    if not R_LesWatch and Approval:   
            #First time dialog                                                       
            if R_Forced: 
                call RogueFace("sad")
                call Statup("Rogue", "Love", 70, -3, 1)
                call Statup("Rogue", "Love", 20, -2, 1)
            elif Bonus >= 100:
                call RogueFace("sly", Eyes="side")
                ch_r "Hmm, actually I might enjoy this more than you think. . ."   
            elif R_Love >= (R_Obed + R_Inbt):
                call RogueFace("sexy")
                $ R_Brows = "sad"
                $ R_Mouth = "smile" 
                ch_r "I haven't really given much thought to being with other people lately. . ."          
            elif R_Obed >= R_Inbt:
                call RogueFace("normal")
                ch_r "If that's what you want, [R_Petname]. . ."            
            else: # Uninhibited 
                call RogueFace("sad")
                $ R_Mouth = "smile"             
                ch_r "I guess it could be fun with you watching. . ."    
    
    
    elif Approval:            
                #Second time+ initial dialog                                                           
                if R_Forced: 
                        call RogueFace("sad")
                        call Statup("Rogue", "Love", 70, -3, 1)
                        call Statup("Rogue", "Love", 20, -2, 1)
                        ch_r "So you want to watch me with a girl again?"  
                elif Approval and "lesbian" in R_RecentActions:
                        call RogueFace("sexy", 1)
                        ch_r "I guess we could get a little closer. . ."    
                        jump R_Les_Prep
                elif Approval and "lesbian" in R_DailyActions:
                        call RogueFace("sexy", 1)
                        $ Line = renpy.random.choice(["You enjoyed the show?",       
                            "Didn't get enough earlier?",
                            "It is nice to have an audience. . ."]) 
                        ch_r "[Line]"            
                elif R_Mast < 3:        
                        call RogueFace("sexy", 1)
                        $ R_Brows = "confused"
                        ch_r "You like to watch, huh?"       
                else:       
                        call RogueFace("sexy", 1)
                        $ Rogue_Arms = 2
                        $ Line = renpy.random.choice(["You sure do like to watch.",                 
                            "So you'd like me to go again?",                 
                            "You want to watch some more?",
                            "You want me to get busy with "+Partner+"?"]) 
                        ch_r "[Line]"
                        $ Line = 0                        
    #End second time+ initial dialog
    
    if Approval >= 2:      
                #If she's into it. . .                                                                            
                if R_Forced:
                    call RogueFace("sad")
                    call Statup("Rogue", "Obed", 90, 1)
                    call Statup("Rogue", "Inbt", 60, 1)
                    ch_r "Fine, I'm ok with it if she is. . ." 
                else:
                    call RogueFace("sexy", 1)
                    call Statup("Rogue", "Love", 90, 1)
                    call Statup("Rogue", "Inbt", 50, 3) 
                    $ Line = renpy.random.choice(["Well. . . ok.",                 
                        "I don't mind getting cozy with her. . .",
                        "I've kind of needed this anyways. . .",
                        "Sure!", 
                        "I guess I could. . . give it a go.",
                        "Heh, ok, ok."]) 
                    ch_r "[Line]"
                    $ Line = 0
                call Statup("Rogue", "Obed", 20, 1)
                call Statup("Rogue", "Obed", 60, 1)
                call Statup("Rogue", "Inbt", 70, 2) 
                jump R_Les_Partner   
    #end instant approval
            
    else:       
        #If she's not into it, but maybe. . .                                                                                    
        menu:
            ch_r "I'm not sure about that though, [R_Petname]."
            "Maybe later?":
                    call RogueFace("sexy", 1)  
                    if Bonus >= 100:
                        call Statup("Rogue", "Inbt", 90, 5)  
                        ch_r "Well. . . definitely at some point. . ."
                    elif Bonus >= 0:
                        call LikeUpdater("Rogue",3)
                        ch_r "Um, I don't know. . . maybe?"
                    else:
                        call RogueFace("angry", 1, Eyes="side") 
                        ch_r "Yeah, I really don't see that happening. . ."
                    call RogueFace("smile", 1) 
                    ch_r "But thanks for being ok with that."
                    call Statup("Rogue", "Love", 80, 2)
                    call Statup("Rogue", "Inbt", 70, 5)   
                    call Taboo_Level
                    return
                    
            "You look like you might be into it. . .":             
                    if Approval:
                            call RogueFace("sexy")     
                            call Statup("Rogue", "Obed", 90, 4)
                            call Statup("Rogue", "Obed", 50, 5)
                            call Statup("Rogue", "Inbt", 70, 4) 
                            call Statup("Rogue", "Inbt", 40, 4) 
                            $ Line = renpy.random.choice(["Well. . . ok.",                 
                                    "I don't mind getting cozy with her. . .",
                                    "I've kind of needed this anyways. . .",
                                    "Sure!", 
                                    "I guess I could. . . give it a go.",
                                    "Heh, ok, ok."]) 
                            ch_r "[Line]"
                            $ Line = 0                   
                            jump R_Les_Partner
                    else:   
                            pass
                    
            "Just get at it already.":                                              
                    # Pressured into it
                    $ Approval = ApprovalCheck("Rogue", 550, "OI", TabM = 2) # 55, 70, 85
                    if Approval > 1 or (Approval and R_Forced):
                            call RogueFace("sad")
                            call Statup("Rogue", "Love", 70, -5, 1)
                            call Statup("Rogue", "Love", 200, -5)                 
                            ch_r "Ok, fine. I'll give it a try."  
                            call Statup("Rogue", "Obed", 80, 4)
                            call Statup("Rogue", "Inbt", 80, 1) 
                            call Statup("Rogue", "Inbt", 60, 3)  
                            $ R_Forced = 1  
                            jump R_Les_Partner
                    else:                              
                            call Statup("Rogue", "Love", 200, -20)     
                            $ R_RecentActions.append("angry")
                            $ R_DailyActions.append("angry")
    # end of asking her to do it
    
    if K_Loc == bg_current:
            call K_Les_Response("Rogue",1,B2=Bonus)
    elif E_Loc == bg_current:
            call E_Les_Response("Rogue",1,B2=Bonus)
    elif L_Loc == bg_current:
            call L_Les_Response("Rogue",1,B2=Bonus)
    if _return:
            #if the other girl convinces her
            call RogueFace("smile", 1)
            ch_r "Ok, fine! You've talked me into it."
            ch_r "Get over here. . ."
            jump R_Les_Prep
            
            
    #She refused all offers.
    $ Rogue_Arms = 1                
    if not Partner:
            ch_r "It would take two to tango, so. . ."
    elif R_Forced:
            call RogueFace("angry", 1)
            ch_r "Look, that's just not on the table."
            call Statup("Rogue", "Lust", 90, 5)         
            if R_Love > 300:
                call Statup("Rogue", "Love", 70, -2)
            call Statup("Rogue", "Obed", 50, -2)    
            $ R_RecentActions.append("angry")
            $ R_DailyActions.append("angry")  
    elif Taboo:                            
            # she refuses and this is too public a place for her
            call RogueFace("angry", 1)          
            $ R_DailyActions.append("tabno") 
            ch_r "Definitely not around here."     
            call Statup("Rogue", "Lust", 90, 5)  
            call Statup("Rogue", "Obed", 50, -3) 
    elif R_Les:
            call RogueFace("sad") 
            if Bonus >= 100:
                ch_r "I just don't think I'm ready for that sort of thing."     
            else:    
                ch_r "I just don't think I'm into that sort of thing."     
    else:
            call RogueFace("normal", 1)
            ch_r "Heh, noway, I am {i}not{/i} doing that."  
    $ R_RecentActions.append("no lesbian")                      
    $ R_DailyActions.append("no lesbian") 
    $ Tempmod = 0 
    call Taboo_Level
    return
    
label R_Les_Partner:
    # This checks to see if the other girl is into it. 
    if K_Loc == bg_current:
            call K_Les_Response("Rogue",2)
            if not _return:
                    # If Kitty refused
                    return
    elif E_Loc == bg_current:
            call E_Les_Response("Rogue",2)
            if not _return:
                    # If Emma refused
                    return
    elif L_Loc == bg_current:
            call L_Les_Response("Rogue",2)
            if not _return:
                    # If Laura refused
                    return
            
label R_Les_Prep:    
    #sets the scene up   
    
    if K_Loc == bg_current:
            if "noticed Rogue" not in K_RecentActions:
                    $ K_RecentActions.append("noticed Rogue")  
            if "noticed Kitty" not in R_RecentActions:
                    $ R_RecentActions.append("noticed Kitty")           
            $ Partner = "Kitty"  
    elif E_Loc == bg_current:
            if "noticed Rogue" not in E_RecentActions:
                    $ E_RecentActions.append("noticed Rogue")  
            if "noticed Emma" not in R_RecentActions:
                    $ R_RecentActions.append("noticed Emma")           
            $ Partner = "Emma"  
    elif L_Loc == bg_current:
            if "noticed Rogue" not in L_RecentActions:
                    $ L_RecentActions.append("noticed Rogue")  
            if "noticed Laura" not in R_RecentActions:
                    $ R_RecentActions.append("noticed Laura")           
            $ Partner = "Laura" 
            
    if "unseen" in R_RecentActions:
            pass
        
            #if she hasn't seen you yet. . .    
#            call RogueFace("sexy")
#            $ R_Eyes = "closed"
#            $ Rogue_Arms = 2
#            "You see Rogue leaning back, masturbating. You don't think she's noticed you yet."
    else:   
            #if she knows you're there. . .
            call RogueFace("sexy")
            $ Rogue_Arms = 2
            "Rogue move's closer to [Partner] and wraps her arms around her neck."
            if not R_LesWatch:
                    #First time        
                    if R_Forced:
                        call Statup("Rogue", "Love", 90, -20)
                        call Statup("Rogue", "Obed", 70, 55)
                        call Statup("Rogue", "Inbt", 80, 55) 
                    else:
                        call Statup("Rogue", "Love", 90, 5)
                        call Statup("Rogue", "Obed", 70, 20)
                        call Statup("Rogue", "Inbt", 80, 60)  
            call R_Les_FirstKiss
            $ Trigger3 == "kiss girl"
            $ Trigger4 == "kiss girl"
        
    $ Trigger = "lesbian"   
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0 
    $ Line = 0
    if Taboo:
        call DrainWord("Rogue","tabno")
    call DrainWord("Rogue","no lesbian")
    $ R_RecentActions.append("lesbian")                      
    $ R_DailyActions.append("lesbian") 
    
label R_Les_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Rogue")
        call Les_Launch("Rogue")    
        call RogueLust     

        if  P_Focus < 100:                                                    
                    #Player Command menu
                    menu:
                        "Keep watching. . .":
                                    pass
                                   
                        "\"Ahem. . .\"" if "unseen" in R_RecentActions:  
                                jump R_Les_Interupted   
                                
                        "Start jack'in it." if Trigger2 != "jackin":
                                call R_Jackin                   
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
                                            if R_Action and MultiAction:
                                                call Rogue_Offhand_Set
                                                if Trigger2:
                                                     $ R_Action -= 1
                                            else:
                                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                                            
                                    "Threesome actions":   
                                        menu:
                                            "Ask Rogue to do something else with [Partner]":
                                                    if "unseen" in R_RecentActions:
                                                            ch_p "Oh yeah, why don't you. . ."
                                                            jump R_Les_Interupted
                                                    else:                
                                                            call Rogue_Les_Change
                                            "Ask [Partner] to do something else":
                                                    if "unseen" in R_RecentActions:
                                                            ch_p "Oh yeah, why don't you. . ."
                                                            jump R_Les_Interupted
                                                    else:                        
                                                            call Partner_Threechange("Rogue")  
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        if "unseen" in R_RecentActions:
                                                            ch_p "Oh, that's good. . ."
                                                            jump R_Les_Interupted
                                                        else:        
                                                            $ ThreeCount = 0    
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Rogue")
                                            "Undress [Partner]":
                                                    if "unseen" in R_RecentActions:
                                                        ch_p "Oh, yeah, take it off. . ."
                                                        jump R_Les_Interupted
                                                    else:           
                                                        call Partner_Undress
                                                        jump R_Les_Cycle 
                                            "Clean up Partner":
                                                    if "unseen" in R_RecentActions:
                                                        ch_p "You've got a little something. . ."
                                                        jump R_Les_Interupted
                                                    else:           
                                                        call Partner_Cleanup
                                                        jump R_Les_Cycle 
                                            "Never mind":
                                                        jump R_Les_Cycle 
                                    "Undress Rogue":
                                            if "unseen" in R_RecentActions:
                                                    ch_p "Oh yeah, why don't you. . ."
                                                    jump R_Les_Interupted
                                            else:                        
                                                    call R_Undress   
                                    "Clean up Rogue (locked)" if not R_Spunk:
                                            pass  
                                    "Clean up Rogue" if R_Spunk:
                                            if "unseen" in R_RecentActions:
                                                ch_p "You've got a little something. . ."
                                                jump R_Les_Interupted
                                            else:                        
                                                call Rogue_Cleanup("ask")                                         
                                    "Never mind":
                                            jump R_Les_Cycle  
                                            
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call R_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump R_Les_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call R_Pos_Reset
                                    $ Line = 0
                                    jump R_Les_After   
        #End menu (if Line)
        
        call Shift_Focus("Rogue")
        call Sex_Dialog("Rogue",Partner)
        
        $ Cnt += 1
        $ Round -= 1
             
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or R_Lust >= 100:    
                    #If either of you can cum:
                    if P_Focus >= 100:
                            #If you can cum:  
                            if "unseen" not in R_RecentActions: #if she knows you're there
                                call PR_Cumming
                                if "angry" in R_RecentActions:  
                                    call R_Pos_Reset
                                    return    
                                call Statup("Rogue", "Lust", 200, 5) 
                                if 100 > R_Lust >= 70 and R_OCount < 2:             
                                    $ R_RecentActions.append("unsatisfied")                      
                                    $ R_DailyActions.append("unsatisfied") 
                                $ Line = "came"
                            else: #If she wasn't aware you were there
                                "You grunt and try to hold it in."
                                $ P_Focus = 95
                                jump R_Les_Interupted
     
                    if R_Lust >= 100: 
                            #If Rogue can cum                                              
                            call R_Cumming
                            jump R_Les_Interupted
                       
                    if Line == "came": 
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."      
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Rogue")   
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if "unseen" in R_RecentActions:
                if Round == 10:
                    "It's getting a bit late, Rogue and [Partner] will probably be wrapping up soon."  
                elif Round == 5:
                    "They're definitely going to stop soon."
        else:
                if Round == 10:
                    ch_r "We might want to wrap this up, it's getting late." 
                elif Round == 5:
                    ch_r "Seriously, it'll be time to stop soon."   
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0)
    $ Line = 0
    if "unseen" not in R_RecentActions:
        ch_r "Ok, [R_Petname], that's enough of that for now."
    

label R_Les_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call R_Pos_Reset
        
    call RogueFace("sexy") 
        
    if Partner == "Emma":
        call Partner_Like("Rogue",4)
    else:
        call Partner_Like("Rogue",3)
            
    $ R_LesWatch += 1 
    if R_LesWatch == 1:            
            $ R_SEXP += 15    
            if R_Love >= 500 and R_Org:
                    ch_r "I have to say, I really enjoyed that one. . ." 
    
    if not Situation:
            ch_r "That was nice. . ."
            if K_Loc == bg_current:
                if "les rogue" not in K_History:
                        if R_LikeKitty >= 600:
                                ch_r "You. . . really know what you're doing down there. . ."
                        else:
                                ch_r "That. . . wasn't awful. . ."
                        if K_LikeRogue >= 600:
                                ch_k "Yeah, that was really hot. . ."
                        else:
                                ch_k "I guess. . ."
                        $ R_History.append("les kitty")   
                        $ K_History.append("les rogue")  
                else:
                    #second time
                    ch_k "Mmmm yeah that was good. . ."
            elif E_Loc == bg_current:
                if "les rogue" not in E_History:
                        if R_LikeEmma >= 600:
                                ch_r "You. . . really know what you're doing down there. . ."
                        else:
                                ch_r "That. . . wasn't awful. . ."
                        if E_LikeRogue >= 600:
                                ch_e "Practice, dear. . ."
                        else:
                                ch_e "You could certainly do with more practice. . ."
                        $ R_History.append("les emma")   
                        $ E_History.append("les rogue")  
                else:
                    #second time
                    ch_e "Certainly. . ."
            elif L_Loc == bg_current:
                if "les rogue" not in L_History:
                        if R_LikeLaura >= 600:
                                ch_r "You. . . really know what you're doing down there. . ."
                        else:
                                ch_r "That. . . wasn't awful. . ."
                        if L_LikeRogue >= 600:
                                ch_l "I can read a map."
                        else:
                                ch_l "Uh-huh."
                        $ R_History.append("les laura")   
                        $ L_History.append("les rogue") 
                else:
                    #second time
                    ch_l "Yup. . ."
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_r "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# End R LesScene


    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

label Rogue_Les_Change(D20S=0, Secondary=Partner, Primary = "Rogue", PrimaryLust=0, SecondaryLust=0):
        # for Lesbian primary activity: Rogue_Threeway_Set("preset", "lesbian", Trigger3, ActiveGirl)
        #this is called when the player wants to change over a lesbian T3 behavior.
        $ Line = 0
        menu:
            "Hey Rogue. . ."
            "why don't you kiss her?" if Trigger5 != "kiss girl" and Trigger5 != "kiss both":
                    call Rogue_Threeway_Set("kiss girl", "lesbian", Trigger3)
            "why don't you grab her tits?" if Trigger3 != "fondle breasts":
                    call Rogue_Threeway_Set("fondle breasts", "lesbian", Trigger3)
            "why don't you suck her breasts?" if Trigger3 != "suck breasts":
                    call Rogue_Threeway_Set("suck breasts", "lesbian", Trigger3)
            "why don't you finger her?" if Trigger3 != "fondle pussy":
                    call Rogue_Threeway_Set("fondle pussy", "lesbian", Trigger3)
            "why don't you go down on her?" if Trigger3 != "lick pussy":
                    call Rogue_Threeway_Set("lick pussy", "lesbian", Trigger3)
            "why don't you grab her ass?" if Trigger3 != "fondle ass":
                    call Rogue_Threeway_Set("fondle ass", "lesbian", Trigger3)
            "why don't you lick her ass?" if Trigger3 != "lick ass":
                    call Rogue_Threeway_Set("lick ass", "lesbian", Trigger3) 
            "never mind.":
                pass
        if not Line:
            $ Line = "You return to what you were doing." 
        else:
            $ Situation = "skip"
        "[Line]"
        return

label Rogue_Three_Change(ActiveGirl = "Kitty", D20S=0, Secondary="Rogue", PrimaryLust=0, SecondaryLust=0):
        #this is called when the player wants to change over a threeway behavior.
        # for Threeway secondary activity: Rogue_Threeway_Set("preset", 0, Trigger4, "ActiveGirl")        
        menu R_Three_Change:
            ch_p "Hey Rogue. . ."
            "about [ActiveGirl]. . .":
                menu:
                    ch_p "about [ActiveGirl]. . ."
                    "why don't you kiss her?" if Trigger5 != "kiss girl" and Trigger5 != "kiss both":
                            call Rogue_Threeway_Set("kiss girl", 0, Trigger4, ActiveGirl)                            
                    "why don't you grab her tits?" if Trigger4 != "fondle breasts":
                            call Rogue_Threeway_Set("fondle breasts",0, Trigger4, ActiveGirl)                    
                    "why don't you suck her breasts?" if Trigger4 != "suck breasts":
                            call Rogue_Threeway_Set("suck breasts",0, Trigger4, ActiveGirl)                            
                    "why don't you finger her?" if Trigger4 != "fondle pussy":
                            call Rogue_Threeway_Set("fondle pussy",0, Trigger4, ActiveGirl)                            
                    "why don't you go down on her?" if Trigger4 != "lick pussy":
                            call Rogue_Threeway_Set("lick pussy", 0, Trigger4, ActiveGirl)                            
                    "why don't you grab her ass?" if Trigger4 != "fondle ass":
                            call Rogue_Threeway_Set("fondle ass", 0, Trigger4, ActiveGirl)                            
                    "why don't you lick her ass?" if Trigger4 != "lick ass":
                            call Rogue_Threeway_Set("lick ass", 0, Trigger4, ActiveGirl)
                    "wait, I meant. . .":
                            jump R_Three_Change
                    
            "about me. . .":
                menu:
                    ch_p "about me. . ."
                    "why don't you kiss me?" if Trigger5 != "kiss you" and Trigger5 != "kiss both":
                            call Rogue_Threeway_Set("kiss you", 0, Trigger4, ActiveGirl)                            
                    "maybe take me in hand?" if Trigger4 != "hand":
                            call Rogue_Threeway_Set("hand", 0, Trigger4, ActiveGirl)                            
                    "maybe give me a lick?" if Trigger4 != "blow":
                            call Rogue_Threeway_Set("blow", 0, Trigger4, ActiveGirl)
                    "wait, I meant. . .":
                            jump R_Three_Change
            "never mind.":
                pass
        return

#Start R_Les_Response >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >
label R_Les_Response(Girl="Kitty", Step=1, B=0, B2=0, Tempmod=0, Result=0, Approval = 0):
        #Dialog for responses to Lesbian scenes, Girl is the initial girl in the scene. Step is the phase of the conversation
        # call R_Les_Response("Kitty",1)
        if R_Les:
            $ Tempmod += 10
        if R_SEXP >= 50:
            $ Tempmod += 25
        elif R_SEXP >= 30:
            $ Tempmod += 15
        elif R_SEXP >= 15:
            $ Tempmod += 5
                    
        elif R_Inbt >= 750:
            $ Tempmod += 5
            
        if "exhibitionist" in R_Traits:      
            $ Tempmod += (3*Taboo) 
            
        if "dating" in R_Traits or "sex friend" in R_Petnames:
            $ Tempmod += 10        
        elif "ex" in R_Traits:
            $ Tempmod -= 40  
            
        if Girl == "Kitty":
                #if it's Kitty. . .
                if R_LikeKitty >= 900:
                        $ B += 150
                elif R_LikeKitty >= 800 or "poly Kitty" in R_Traits:
                        $ B += 100
                elif R_LikeKitty >= 700:
                        $ B += 50
                elif R_LikeKitty <= 200:
                        $ B -= 200
                elif R_LikeKitty <= 500:
                        $ B -= 100
        elif Girl == "Emma":
                #if it's Emma. . .
                if R_LikeEmma >= 900:
                        $ B += 150
                elif R_LikeEmma >= 800 or "poly Emma" in R_Traits:
                        $ B += 100
                elif R_LikeEmma >= 700:
                        $ B += 50
                elif R_LikeEmma <= 200:
                        $ B -= 200
                elif R_LikeEmma <= 500:
                        $ B -= 100
        elif Girl == "Laura":
                #if it's Laura. . .
                if R_LikeLaura >= 900:
                        $ B += 150
                elif R_LikeLaura >= 800 or "poly Laura" in R_Traits:
                        $ B += 100
                elif R_LikeLaura >= 700:
                        $ B += 50
                elif R_LikeLaura <= 200:
                        $ B -= 200
                elif R_LikeLaura <= 500:
                        $ B -= 100
                        
        $ Approval = ApprovalCheck("Rogue", 1300, TabM = 2, Bonus = B) # 1300, 1450, 1600, Taboo -800
        
        if Step == 1:
            #this is if the first girl's check failed, but Rogue likes her.
            if Approval >= 2 or (Approval and B >= 150):
                call RogueFace("sexy", 1)
                ch_r "You sure [Girl]? Could be a lot of fun?"
                if B2 >= 100:
                    $ Result = 1
                    if Girl == "Kitty":
                            $ R_LikeKitty += (int(B/10))
                            $ K_LikeRogue += (int(B2/10))
                    elif Girl == "Emma":
                            $ R_LikeEmma += (int(B/10))
                            $ E_LikeRogue += (int(B2/10))
                    elif Girl == "Laura":
                            $ R_LikeLaura += (int(B/10))
                            $ L_LikeRogue += (int(B2/10))
            else:
                return Result
        
        if Step == 2:
            #this is the second step, usually in the Prep phase
            if Approval >= 2:
                call RogueFace("smile", 1)
                ch_r "'Course!"
                $ Result = 1
            elif Approval:
                call RogueFace("sly", 2)
                if B >= 100:
                        ch_r "I don't know, maybe. . ."
                if B >= 0:
                        ch_r "I'm not sure about her though. . ."
                $ R_Blush = 1
                menu:
                    extend ""
                    "Ok, that's fine. . .":
                            if B >= 100:                            
                                ch_r "Never mind, I'm in."
                                $ Result = 1
                            else:
                                call RogueFace("smile")
                                ch_r "Thanks, I appreciate it."
                    "Come on, you might enjoy it. . .":
                            if B >= 50:
                                ch_r "Well, I suppose." 
                                $ Result = 1
                            else:
                                call RogueFace("sad", 2)
                                ch_r "I don't think so." 
                    "Get in there, now.":
                            if ApprovalCheck("Rogue", 550, "OI", TabM = 2):
                                call RogueFace("sadside", 1)
                                ch_r "Fine, whatever."
                                $ Result = 1
                            else:
                                call RogueFace("angry")
                                ch_r "Who do you think you're talk'in to?"  
                                $ R_RecentActions.append("angry")
                                $ R_DailyActions.append("angry")
                    "[Girl], what do you think?":
                            if Girl == "Kitty":
                                call KittyFace("sexy", 1)
                                if K_Les and R_Les:
                                        ch_k "Come on Rogue, you know we have fun."
                                else:
                                        ch_k "Come on Rogue, could be fun."
                                $ R_LikeKitty += (int(B/10))
                                if B >= 50:
                                        $ K_LikeRogue += 5
                            elif Girl == "Emma":
                                call EmmaFace("sexy", 1)
                                if E_Les and R_Les:
                                        ch_e "What's the matter Rogue, shy around [Playername]?"
                                else:
                                        ch_e "What's the matter Rogue, I don't bite. . ."
                                $ R_LikeEmma += (int(B/10))
                                if B >= 50:
                                        $ E_LikeRogue += 5
                            elif Girl == "Laura":
                                call LauraFace("sexy", 1)
                                if L_Les and R_Les:
                                        ch_l "What, you don't want to fuck with [L_Petname] around?"
                                else:
                                        ch_l "Come on, you look like you have it in you."
                                $ R_LikeLaura += (int(B/10))
                                if B >= 50:
                                        $ L_LikeRogue += 5
                            if B >= 50:
                                call RogueFace("smile", 1)
                                ch_r "You know, I can't argue with that, [Girl]."
                                $ Result = 1
                            else:
                                call RogueFace("angry", 1, Eyes="side")
                                ch_r "Sorry [Girl], nothin personal."
            if Step == 3:
                    #This is a check if you interrupted them and Primary wants to do it, does Secondary?
                    if Approval:
                            call RogueFace("smile", 1)
                            ch_r "I mean, I guess so. . ."
                            $ Result = 1
                    else:
                            call RogueFace("sadside", 1)
                            ch_r "I'm really not into that right now. . ."
            
            if not Result:      
                #no approval
                $ R_RecentActions.append("no lesbian")                      
                $ R_DailyActions.append("no lesbian") 
                call RogueFace("sadside", 1)
                if B <= 0:
                    ch_r "Sorry, [R_Petname], it's just not like that with her."
                if Taboo:
                    ch_r "Sorry, [R_Petname], this isn't a good place for it."
                if B >= 100:
                    ch_r "Sorry, [R_Petname], maybe if you weren't around. . ."
                else:
                    ch_r "Sorry, [R_Petname], I'm just not interested."
                
        return Result
#End R_Les_Response >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >


label R_Les_FirstKiss:
    # called when there is a first kiss situation between two girls
    if Partner == "Kitty":
            if "les kitty" in R_History:
                #if they've been together before              
                $ Line = "experienced"
            elif R_Les and K_Les:   
                #if both have kissed girls before
                $ Line = "first both"
            elif R_Les:
                #Rogue's had experience              
                $ Line = "first girl"
            elif K_Les:
                #Kitty's had experience                
                $ Line = "first partner"
    elif Partner == "Emma":
            if "les emma" in R_History:
                #if they've been together before              
                $ Line = "experienced"
            elif R_Les and E_Les:   
                #if both have kissed girls before
                $ Line = "first both"
            elif R_Les:
                #Rogue's had experience              
                $ Line = "first girl"
            elif E_Les:
                #Emma's had experience                
                $ Line = "first partner"
    elif Partner == "Laura":
            if "les laura" in R_History:
                #if they've been together before              
                $ Line = "experienced"
            elif R_Les and L_Les:   
                #if both have kissed girls before
                $ Line = "first both"
            elif R_Les:
                #Rogue's had experience              
                $ Line = "first girl"
            elif L_Les:
                #Laura's had experience                
                $ Line = "first partner"
    
    if Line == "experienced":
            "Rogue and [Partner] move together in a passionate kiss."
            "Rogue's arms firmly grasp [Partner]'s neck and pull her close."
    else:
            if Line in ("first both", "first girl"):
                # Rogue's first time
                "Rogue tentatively moves in and gives [Partner] a soft kiss."
            else:
                #not Rogue's first time
                "Rogue casually places a hand on the back of [Partner]'s head and draws their lips together."
            if Line == "first partner":
                #other girl's first time
                "[Partner] pulls back a bit, but slowly leans into the enbrace."
            else:
                #not other girl's first time
                "[Partner]'s lips curl up into a smile and she draws Rogue even closer."                    
            "After a few seconds, it begins to grow more passionate."
    return