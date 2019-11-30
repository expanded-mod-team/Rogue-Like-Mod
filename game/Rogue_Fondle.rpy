﻿# R_Massage /////////////////////////////////////////////////////////////////////////////
label R_Massage:
    call Shift_Focus("Rogue")
    $ Tempmod = 0    
    if "angry" in R_RecentActions:
        return    
        
    $ Approval = ApprovalCheck("Rogue", 500, TabM = 1) # 95, 110, 125 -120(215)
    
    if Approval >= 2:             
        call RogueFace("bemused", 1)
        if R_Forced:
                call RogueFace("sad")
                call Statup("Rogue", "Love", 20, -2, 1)
                call Statup("Rogue", "Obed", 90, 1)
                call Statup("Rogue", "Inbt", 60, 1)
        ch_r "Ok [R_Petname], sure."   
        call Statup("Rogue", "Love", 90, 1)
        call Statup("Rogue", "Inbt", 50, 3) 
        jump R_Massage_Prep
        
    else:
        call RogueFace("angry", 1)
        if "no massage" in R_RecentActions:  
            ch_r "Heh, I {i}just{/i} told you \"no,\" [R_Petname]."
        elif "no massage" in R_DailyActions:       
            ch_r "I told you \"no,\" earlier [R_Petname]."
        else:
            call RogueFace("bemused")
            ch_r "I don't know, not right now."   
        menu:
            extend ""
            "Sorry, never mind." if "no massage" in R_DailyActions:
                call RogueFace("bemused")
                ch_r "Ok, no problem, [R_Petname]."              
                return
            "Maybe later?" if "no massage" not in R_DailyActions:
                call RogueFace("sexy")  
                ch_r "Sure, maybe."
                call Statup("Rogue", "Love", 80, 1)
                call Statup("Rogue", "Inbt", 20, 1)
                call Statup("Rogue", "Obed", 20, 1)  
                $ R_RecentActions.append("no massage")                      
                $ R_DailyActions.append("no massage")            
                return                
            "Come on, Please?":             
                if Approval:
                    call RogueFace("sexy")     
                    call Statup("Rogue", "Obed", 90, 1)
                    call Statup("Rogue", "Obed", 40, 2)
                    call Statup("Rogue", "Inbt", 30, 2)
                    ch_r "Well, if you're that desperate. . ."                
                    jump R_Massage_Prep
                else:   
                    call RogueFace("sexy") 
                    ch_r "Heh, no thanks, [R_Petname]." 
    
    if "no massage" in R_DailyActions:
        ch_r "You're starting to skeeve me out, [R_Petname]."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1)
        ch_r "I don't even want you touching me."
        call Statup("Rogue", "Lust", 60, 5)    
        call Statup("Rogue", "Obed", 50, -2)   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:
        call RogueFace("angry", 1)    
        ch_r "I don't want you touching me in public."                   
    else:
        call RogueFace("sexy") 
        $ R_Mouth = "sad"
        ch_r "Seriously, no thanks, [R_Petname]."    
    $ R_RecentActions.append("no massage")                      
    $ R_DailyActions.append("no massage") 
    $ Tempmod = 0    
    return
 
label R_Massage_Prep:
    call Rogue_Top_Off("massage")
    if "angry" in R_RecentActions:
        return    
        
label R_Massage_Cycle:    
    $ R_RecentActions.append("massage")                      
    $ R_DailyActions.append("massage") 
    
    call Rogue_Doggy_Launch("massage")
    
    "You massage her back and shoulders."
    if not R_Over:
        $ R_Addict -= D20 if R_Addict > D20 else R_Addict
        
    $ D20 = renpy.random.randint(10, 20)
    $ Round -= D20 if Round > D20 else (Round-1)
        
    call Rogue_Sex_Reset
    
    ch_r "That was very relaxing, [R_Petname]"
    if "massage" not in R_RecentActions:        
        call Statup("Rogue", "Love", 90, 1)
        call Statup("Rogue", "Love", 50, 2)
        call Statup("Rogue", "Obed", 30, 2)
    return

# end R_Massage /////////////////////////////////////////////////////////////////////////////

# R_Fondle /////////////////////////////////////////////////////////////////////////////
label R_Fondle:
    
    $ R_Mouth = "smile"
    if not R_Action:
        ch_r "I'm a bit worn out right now, [R_Petname], maybe later."
        return
    menu:
        ch_r "Well where exactly were you interested in touching, [R_Petname]?"
        "Your breasts?" if R_Action:
            jump R_Fondle_Breasts
        "Your thighs?" if R_Action:
            jump R_Fondle_Thighs
        "Your pussy?" if R_Action:
            jump R_Fondle_Pussy
        "Your Ass?" if R_Action:
            jump R_Fondle_Ass
        "Never mind.":
            return
    return


# R_Fondle Breasts /////////////////////////////////////////////////////////////////////////////
label R_Fondle_Breasts:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Rogue")
    
    # Will she let you fondle? Modifiers
    if R_FondleB: #You've done it before
        $ Tempmod += 15
    if R_Lust > 75: #She's really horny
        $ Tempmod += 20
    if "exhibitionist" in R_Traits:
        $ Tempmod += (3*Taboo)
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 20
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount
    
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no fondle breasts" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle breasts" in R_RecentActions else 0        
        
    $ Approval = ApprovalCheck("Rogue", 950, TabM = 3) # 95, 110, 125 -120(215)
    
    if Situation == "auto":  
        if Approval:
            call RogueFace("sexy")       
            call Statup("Rogue", "Obed", 90, 1)
            call Statup("Rogue", "Obed", 70, 2)
            call Statup("Rogue", "Inbt", 70, 3)
            call Statup("Rogue", "Inbt", 30, 2)            
            "As you cup her breast, Rogue gently nods."            
            jump RFB_Prep        
        else:   
            call RogueFace("surprised")
            $ R_Brows = "confused"
            call Statup("Rogue", "Obed", 50, -2)
            ch_r "Ah, ah, Just keep doing what you were doing, [R_Petname]."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
                    
    # fondle yes:    
    
    if Approval:                                                                       #Second time+ dialog        
        call RogueFace("sexy", 1)
        if R_Forced: 
            call RogueFace("sad")
            call Statup("Rogue", "Love", 70, -3, 1)
            call Statup("Rogue", "Love", 20, -2, 1)           
        elif not Taboo and "tabno" in R_DailyActions:        
            ch_r "I guess this is private enough. . ."   
            
    if "fondle breasts" in R_RecentActions:
        call RogueFace("sexy", 1)
        ch_r "Mmm, again? Ok."
        jump RFB_Prep
    elif "fondle breasts" in R_DailyActions:
        call RogueFace("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so hard this time though.",
            "Mmm. . ."]) 
        ch_r "[Line]"
            
    if Approval >= 2:             
        call RogueFace("bemused", 1)
        if R_Forced:
            call RogueFace("sad")
            call Statup("Rogue", "Love", 70, -3, 1)
            call Statup("Rogue", "Love", 20, -2, 1)
            call Statup("Rogue", "Obed", 90, 1)
            call Statup("Rogue", "Inbt", 60, 1)
        ch_r "Ok [R_Petname], come and get'em."   
        call Statup("Rogue", "Love", 90, 1)
        call Statup("Rogue", "Inbt", 50, 3) 
        jump RFB_Prep
        
    else:
        call RogueFace("angry", 1)
        if "no fondle breasts" in R_RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions and "no fondle breasts" in R_DailyActions:  
            ch_r "I told you not to touch me like that in public!" 
        elif "no fondle breasts" in R_DailyActions:       
            ch_r "I already told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions:  
            ch_r "I told you not in public!"  
        elif not R_FondleB:
            call RogueFace("bemused")
            ch_r "I just don't think I'm ready yet, [R_Petname]. . ."
        else:
            call RogueFace("bemused")
            ch_r "I'd really rather not."   
        menu:
            extend ""
            "Sorry, never mind." if "no fondle breasts" in R_DailyActions:
                call RogueFace("bemused")
                ch_r "Ok, no problem, [R_Petname]."              
                return
            "Maybe later?" if "no fondle breasts" not in R_DailyActions:
                call RogueFace("sexy")  
                "She re-adjusts her cleavage."
                ch_r "I'll give it some thought, [R_Petname]."
                call Statup("Rogue", "Love", 80, 1)
                call Statup("Rogue", "Love", 50, 1)
                call Statup("Rogue", "Inbt", 30, 2)    
                if Taboo:                    
                    $ R_RecentActions.append("tabno")                      
                    $ R_DailyActions.append("tabno") 
                $ R_RecentActions.append("no fondle breasts")                      
                $ R_DailyActions.append("no fondle breasts")            
                return                
            "Come on, Please?":             
                if Approval:
                    call RogueFace("sexy")     
                    call Statup("Rogue", "Obed", 90, 1)
                    call Statup("Rogue", "Obed", 50, 2)
                    call Statup("Rogue", "Inbt", 60, 3)
                    call Statup("Rogue", "Inbt", 30, 2)
                    ch_r "Heh, I suppose I can hardly refuse ya when you use the magic words . . ."                
                    jump RFB_Prep
                else:   
                    call RogueFace("sexy") 
                    ch_r "I'm afraid not this time, sorry [R_Petname]." 
            
            
            "[[Grab her chest anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Rogue", 350, "OI", TabM = 3) # 35, 50, 65
                if Approval > 1 or (Approval and R_Forced):
                    call RogueFace("sad")
                    call Statup("Rogue", "Love", 70, -5, 1)
                    call Statup("Rogue", "Love", 20, -2, 1)                 
                    ch_r "Fine, if that's what you want."                         
                    call Statup("Rogue", "Obed", 90, 2)
                    call Statup("Rogue", "Obed", 50, 4)
                    call Statup("Rogue", "Inbt", 60, 3)   
                    if Approval < 2:                          
                        $ R_Forced = 1
                    jump RFB_Prep
                else:                              
                    call Statup("Rogue", "Love", 200, -10)  
                    call RogueFace("angry", 1)
                    "She slaps your hand away."   
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")   
    
    if "no fondle breasts" in R_DailyActions:
        ch_r "Learn to take \"no\" for an answer, [R_Petname]."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1)
        ch_r "I don't want you touching me."
        call Statup("Rogue", "Lust", 60, 5)    
        call Statup("Rogue", "Obed", 50, -2)   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:
        call RogueFace("angry", 1)    
        $ R_RecentActions.append("tabno")                   
        $ R_DailyActions.append("tabno") 
        ch_r "I really don't think this is the right place for that!"                   
    elif R_FondleB:
        call RogueFace("sad")
        ch_r "Sorry, [R_Petname], you aren't touching these again."        
    else:
        call RogueFace("sexy") 
        $ R_Mouth = "sad"
        ch_r "Not hap'nin."    
    $ R_RecentActions.append("no fondle breasts")                      
    $ R_DailyActions.append("no fondle breasts") 
    $ Tempmod = 0   
    return 
            
   
label RFB_Prep: #Animation set-up   
label R_FB_Prep: #Animation set-up           
    if Trigger == "kiss you": 
        $ Trigger = "fondle breasts" 
        return
        
    if Trigger2 == "fondle breasts": 
        return
    
    call R_Breasts_Launch("fondle breasts")
    
    if Situation == "Rogue":                                                                  
            #Rogue auto-starts    
            $ Situation = 0
            if (R_Over or R_Chest) and not R_Uptop:
                #if she has some sort of top on. . .
                if ApprovalCheck("Rogue", 1250, TabM = 1) or (R_SeenChest and ApprovalCheck("Rogue", 500) and not Taboo):
                        $ R_Uptop = 1
                        $ Line = R_Over if R_Over else R_Chest
                        "With a miscevious grin, Rogue pulls her [Line] up over her breasts."
                        call Rogue_First_Topless(1)
                        $ Line = 0
                        "She then grabs your arm and shoves your hand against her breast, clearly intending you to get to work."
                else:
                    "Rogue grabs your arm and shoves your hand against her covered breast, clearly intending you to get to work."
            else:
                "Rogue grabs your arm and shoves your hand against her breast, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":                    
                    call Statup("Rogue", "Inbt", 80, 3) 
                    call Statup("Rogue", "Inbt", 50, 2)
                    "You start to fondle it."
                "Praise her.":       
                    call RogueFace("sexy", 1)                    
                    call Statup("Rogue", "Inbt", 80, 3) 
                    ch_p "I like the initiative, [R_Pet]."
                    call Rogue_Namecheck
                    "You start to fondle it."
                    call Statup("Rogue", "Love", 85, 1)
                    call Statup("Rogue", "Obed", 90, 1)
                    call Statup("Rogue", "Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your hand back."
                    call RogueFace("surprised")       
                    call Statup("Rogue", "Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [R_Pet]."
                    call Rogue_Namecheck
                    "Rogue pulls back."
                    call Statup("Rogue", "Obed", 90, 1)
                    call Statup("Rogue", "Obed", 50, 1)
                    call Statup("Rogue", "Obed", 30, 2)
                    $ P_RecentActions.append("nope")      
                    call AnyWord("Rogue",1,"refused","refused")  
                    return          
            #end auto
        
    if not R_Forced and Situation != "auto":
        $ Tempmod = 0
        call Rogue_Top_Off
        if "angry" in R_RecentActions:
            return
        
    $ Tempmod = 0  
    if not R_FondleB:        
        if R_Forced:
            call Statup("Rogue", "Love", 90, -20)
            call Statup("Rogue", "Obed", 70, 25)
            call Statup("Rogue", "Inbt", 80, 15) 
        else:
            call Statup("Rogue", "Love", 90, 10)
            call Statup("Rogue", "Obed", 70, 5)
            call Statup("Rogue", "Inbt", 80, 15) 
            
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
    call DrainWord("Rogue","no fondle breasts")
    $ R_RecentActions.append("fondle breasts")                      
    $ R_DailyActions.append("fondle breasts") 
    
label RFB_Cycle: #Repeating strokes    
    while Round >=0:  
        call Shift_Focus("Rogue") 
        call R_Breasts_Launch("fondle breasts")
        call RogueLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                         
                        "Slap her ass":                     
                                    call R_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump RFB_Cycle  
                                    
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
                                                        "Ask to suck on them.":
                                                                if R_Action and MultiAction:                        
                                                                    $ Situation = "shift"
                                                                    call RFB_After
                                                                    call R_Suck_Breasts
                                                                else:
                                                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"
                                                        "Just suck on them without asking.":
                                                                if R_Action and MultiAction:                            
                                                                    $ Situation = "auto"
                                                                    call RFB_After
                                                                    call R_Suck_Breasts
                                                                else:
                                                                    "As you lean in to suck on her breast, she grabs your head and pushes back."
                                                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"                                           
                                                        "Never Mind":
                                                                jump RFB_Cycle
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
                                                        jump RFB_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump RFB_Cycle 
                                            "Never mind":
                                                        jump RFB_Cycle 
                                    "Undress Rogue":
                                            call R_Undress   
                                    "Clean up Rogue (locked)" if not R_Spunk:
                                            pass  
                                    "Clean up Rogue" if R_Spunk:
                                            call Rogue_Cleanup("ask")                                         
                                    "Never mind":
                                            jump RFB_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call R_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump RFB_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call R_Pos_Reset
                                    $ Line = 0
                                    jump RFB_After
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
                                call R_Pos_Reset
                                return    
                            call Statup("Rogue", "Lust", 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2 and R_SEXP >= 20:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump RFB_After 
                            $ Line = "came"
     
                    if R_Lust >= 100:  
                            #If Rogue can cum                                             
                            call R_Cumming
                            if Situation == "shift" or "angry" in R_RecentActions:
                                jump RFB_After
                       
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
                                        jump RFB_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Rogue")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if R_SEXP >= 100 or ApprovalCheck("Rogue", 1200, "LO"):
            pass
        elif Cnt == (5 + R_FondleB):
                    $ R_Brows = "confused"
                    ch_r "You're just going at them, huh?" 
        elif R_Lust >= 85:
                    pass  
        elif Cnt == (15 + R_FondleB) and R_SEXP >= 15 and not ApprovalCheck("Rogue", 1500):
                    $ R_Brows = "confused" 
                    menu:
                        ch_r "I know you're having fun, but maybe we could try something else [R_Petname]."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump RFB_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump RFB_After
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
                                    jump RFB_After
        #End Count check
           
        call Escalation("Rogue","R") #sees if she wants to escalate things
        
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
                
        if R_Lust >= 50 and not R_Uptop and (R_Chest or R_Over):
                $ R_Uptop = 1
                "Rogue shrugs and pulls her top open."   
                call Rogue_First_Topless
                      
    #Round = 0 loop breaks
    call RogueFace("bemused", 0)
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
    
label RFB_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call R_Pos_Reset
        
    call RogueFace("sexy") 
    
    $ R_FondleB += 1  
    $ R_Action -=1
    $ R_Addictionrate += 1
    if "addictive" in P_Traits:
        $ R_Addictionrate += 1   
        
    call Partner_Like("Rogue",2)
     
    if R_FondleB == 1:            
            $ R_SEXP += 4         
            if not Situation: 
                if R_Love >= 500 and "unsatisfied" not in R_RecentActions:
                    ch_r "That was . . . real pleasant, [R_Petname]."
                elif R_Obed <= 500 and P_Focus <= 20:
                    call RogueFace("perplexed", 1)
                    ch_r "Did you get your jollies?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_r "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# End Fondle Breasts


# R Suck Breasts /////////////////////////////////////////////////////////////////////////////

label R_Suck_Breasts:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Rogue")
                                                                                        # Will she let you suck? Modifiers
    if R_SuckB: #You've done it before
        $ Tempmod += 15
    if not R_Chest and not R_Over:
        $ Tempmod += 15
    if R_Lust > 75: #She's really horny
        $ Tempmod += 20
    if R_Lust > 75 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in R_Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 25  
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount     
    
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no suck breasts" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no suck breasts" in R_RecentActions else 0   
        
    $ Approval = ApprovalCheck("Rogue", 1050, TabM = 4) # 105, 120, 135, Taboo -160(265)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            call RogueFace("sexy")       
            call Statup("Rogue", "Obed", 90, 1)
            call Statup("Rogue", "Obed", 70, 2)
            call Statup("Rogue", "Inbt", 70, 3)
            call Statup("Rogue", "Inbt", 30, 2)            
            "As you dive in, Rogue seems a bit surprised, but just makes a little \"coo.\""              
            jump RSB_Prep      
        else:               
            call RogueFace("surprised")
            call Statup("Rogue", "Obed", 50, -2)
            ch_r "Hey, just keep doing what you were doing, [R_Petname]."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
    
    if "suck breasts" in R_RecentActions:
        call RogueFace("sexy", 1)
        ch_r "Mmm, again? Ok."
        jump RSB_Prep
    elif "suck breasts" in R_DailyActions:
        call RogueFace("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so hard this time though.",
            "Mmm. . ."]) 
        ch_r "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .
        call RogueFace("bemused", 1)
        if R_Forced:
            call RogueFace("sad")
            call Statup("Rogue", "Love", 70, -3, 1)
            call Statup("Rogue", "Love", 20, -2, 1)
            call Statup("Rogue", "Obed", 90, 1)
            call Statup("Rogue", "Inbt", 60, 1)
        ch_r "Ok [R_Petname], come and get'em."   
        call Statup("Rogue", "Love", 90, 1)
        call Statup("Rogue", "Inbt", 50, 3) 
        jump RSB_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        call RogueFace("angry", 1)
        if "no suck breasts" in R_RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions and "no suck breasts" in R_DailyActions:  
            ch_r "I told you we can't do that in public!" 
        elif "no suck breasts" in R_DailyActions:       
            ch_r "I already told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions:  
            ch_r "I told you not in public!"  
        elif not R_SuckB:
            call RogueFace("bemused")
            ch_r "I just don't think I'm ready yet, [R_Petname]. . ."
        else:
            call RogueFace("bemused")
            ch_r "I'd really rather not."  
        menu:
            extend ""
            "Sorry, never mind." if "no suck breasts" in R_DailyActions:
                call RogueFace("bemused")
                ch_r "Yeah, fine, [R_Petname]."              
                return
            "Maybe later?" if "no suck breasts" not in R_DailyActions:
                call RogueFace("sexy")  
                ch_r "I'll give it some thought, [R_Petname]."
                call Statup("Rogue", "Love", 80, 1)
                call Statup("Rogue", "Love", 50, 1)
                call Statup("Rogue", "Inbt", 30, 2)    
                if Taboo:                    
                    $ R_RecentActions.append("tabno")                      
                    $ R_DailyActions.append("tabno") 
                $ R_RecentActions.append("no suck breasts")                      
                $ R_DailyActions.append("no suck breasts")            
                return
            "Come on, Please?":             
                if Approval:
                    call RogueFace("sexy")     
                    call Statup("Rogue", "Obed", 90, 1)
                    call Statup("Rogue", "Obed", 50, 2)
                    call Statup("Rogue", "Inbt", 60, 3)
                    call Statup("Rogue", "Inbt", 30, 2)
                    ch_r "You better work your mouth that hard on these."                
                    jump RSB_Prep
                else:   
                    call RogueFace("sexy") 
                    ch_r "I'm afraid not this time, sorry [R_Petname]."     
            
            "[[Start sucking anyway]":                                               # Pressured into licking. 
                $ Approval = ApprovalCheck("Rogue", 450, "OI", TabM = 3) # 45, 60, 75, -120(165)
                if Approval > 1 or (Approval and R_Forced):
                    call RogueFace("sad")
                    call Statup("Rogue", "Love", 70, -5, 1)
                    call Statup("Rogue", "Love", 20, -2, 1)                 
                    ch_r "Hmmph, well I guess you can go to town. . ."                         
                    call Statup("Rogue", "Obed", 90, 2)
                    call Statup("Rogue", "Obed", 50, 4)
                    call Statup("Rogue", "Inbt", 60, 3)  
                    if Approval < 2:                          
                        $ R_Forced = 1
                    jump RSB_Prep
                else:                              
                    call Statup("Rogue", "Love", 200, -10)  
                    call RogueFace("angry", 1)
                    "She shoves your head back out."   
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")   
                    
    if "no suck breasts" in R_DailyActions:
        ch_r "Learn to take \"no\" for an answer, [R_Petname]."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1)
        ch_r "I don't want your lips on me."
        call Statup("Rogue", "Lust", 60, 5)    
        call Statup("Rogue", "Obed", 50, -2)    
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:   
        call RogueFace("angry", 1)      
        $ R_RecentActions.append("tabno")    
        $ R_DailyActions.append("tabno") 
        ch_r "I really don't think this is the right place for that!"                   
    elif R_SuckB:
        call RogueFace("sad")
        ch_r "Sorry, [R_Petname], you aren't getting these in your mouth."            
    else:
        call RogueFace("sexy") 
        $ R_Mouth = "sad"
        ch_r "Not hap'nin, [R_Petname]."
    $ R_RecentActions.append("no suck breasts")                      
    $ R_DailyActions.append("no suck breasts") 
    $ Tempmod = 0    
    return
                      
        
ch_r "Sorry, I don't even know how I got here. . ."
return

label RSB_Prep:                                                                 #Animation set-up 
label R_SB_Prep:                                                                 #Animation set-up 
            
    if Trigger2 == "suck breasts":
        return
           
    call R_Breasts_Launch("suck breasts")
        
    if Situation == "Rogue":                                                        
            #Rogue auto-starts    
            $ Situation = 0
            if (R_Over or R_Chest) and not R_Uptop:
                #if she has some sort of top on. . .
                if ApprovalCheck("Rogue", 1250, TabM = 1) or (R_SeenChest and ApprovalCheck("Rogue", 500) and not Taboo):
                        $ R_Uptop = 1
                        $ Line = R_Over if R_Over else R_Chest
                        "With a miscevious grin, Rogue pulls her [Line] up over her breasts."
                        call Rogue_First_Topless(1)
                        $ Line = 0
                        "She then grabs your head and shoves your face into her chest, clearly intending you to get to work."
                else:
                    "Rogue grabs your head and shoves your face into her chest, clearly intending you to get to work."
            else:
                "Rogue grabs your head and shoves your face into her chest, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":                    
                    call Statup("Rogue", "Inbt", 80, 3) 
                    call Statup("Rogue", "Inbt", 50, 2)
                    "You start to run your tongue along her nipple."
                "Praise her.":       
                    call RogueFace("sexy", 1)                    
                    call Statup("Rogue", "Inbt", 80, 3) 
                    ch_p "Mmm, I like this, [R_Pet]."
                    call Rogue_Namecheck
                    "You start to fondle it."
                    call Statup("Rogue", "Love", 85, 1)
                    call Statup("Rogue", "Obed", 90, 1)
                    call Statup("Rogue", "Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your head back."
                    call RogueFace("surprised")       
                    call Statup("Rogue", "Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [R_Pet]."
                    call Rogue_Namecheck
                    "Rogue pulls away."
                    call Statup("Rogue", "Obed", 90, 1)
                    call Statup("Rogue", "Obed", 50, 1)
                    call Statup("Rogue", "Obed", 30, 2)
                    $ P_RecentActions.append("nope")      
                    call AnyWord("Rogue",1,"refused","refused")  
                    return          
            #end auto
            
    if not R_Forced and Situation != "auto":
        $ Tempmod = 0   
        call Rogue_Top_Off
        if "angry" in R_RecentActions:
            return
    
    $ Tempmod = 0   
    if not R_SuckB:        
        if R_Forced:
            call Statup("Rogue", "Love", 90, -25)
            call Statup("Rogue", "Obed", 70, 25)
            call Statup("Rogue", "Inbt", 80, 17) 
        else:
            call Statup("Rogue", "Love", 90, 10)
            call Statup("Rogue", "Obed", 70, 10)
            call Statup("Rogue", "Inbt", 80, 15) 
    
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
    call DrainWord("Rogue","no suck breasts")
    $ R_RecentActions.append("suck breasts")                      
    $ R_DailyActions.append("suck breasts") 
    
label RSB_Cycle: #Repeating strokes   
    if Trigger2 == "kiss you":
            $ Trigger2 = 0
    while Round >=0:  
        call Shift_Focus("Rogue") 
        call R_Breasts_Launch("suck breasts")
        call RogueLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                         
                        "Slap her ass":                     
                                    call R_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump RSB_Cycle  
                                    
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
                                                        "Pull back to fondling.":  
                                                            if R_Action and MultiAction:
                                                                $ Situation = "pullback"
                                                                call RSB_After
                                                                call R_Fondle_Breasts
                                                            else:
                                                                "As you pull back, Rogue pushes you back in close."
                                                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up"
                                                        "Never Mind":
                                                                jump RSB_Cycle
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
                                                        jump RSB_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump RSB_Cycle 
                                            "Never mind":
                                                        jump RSB_Cycle 
                                    "Undress Rogue":
                                            call R_Undress   
                                    "Clean up Rogue (locked)" if not R_Spunk:
                                            pass  
                                    "Clean up Rogue" if R_Spunk:
                                            call Rogue_Cleanup("ask")                                         
                                    "Never mind":
                                            jump RSB_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call R_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump RSB_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call R_Pos_Reset
                                    $ Line = 0
                                    jump RSB_After
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
                                call R_Pos_Reset
                                return    
                            call Statup("Rogue", "Lust", 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump RSB_After 
                            $ Line = "came"
     
                    if R_Lust >= 100:  
                            #If Rogue can cum                                             
                            call R_Cumming
                            if Situation == "shift" or "angry" in R_RecentActions:
                                jump RSB_After
                       
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
                                        jump RSB_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Rogue")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if R_SEXP >= 100 or ApprovalCheck("Rogue", 1200, "LO"):
            pass
        elif Cnt == (5 + R_SuckB):
                    $ R_Brows = "confused"
                    ch_r "You're just going at them, huh?"   
        elif R_Lust >= 85:
                    pass
        elif Cnt == (15 + R_SuckB) and R_SEXP >= 15 and not ApprovalCheck("Rogue", 1500):
                    $ R_Brows = "confused"        
                    menu:
                        ch_r "I know you're having fun, but maybe we could try something else [R_Petname]."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump RSB_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump RSB_After
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
                                    jump RSB_After
        #End Count check
           
        call Escalation("Rogue","R") #sees if she wants to escalate things
        
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
        if R_Lust >= 50 and not R_Uptop and (R_Chest or R_Over):
                $ R_Uptop = 1
                "Rogue shrugs and pulls her top open."   
                call Rogue_First_Topless 
                      
    #Round = 0 loop breaks
    call RogueFace("bemused", 0)
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
    
label RSB_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call R_Pos_Reset
        
    call RogueFace("sexy") 
    
    $ R_SuckB += 1  
    $ R_Action -=1
    $ R_Addictionrate += 1
    if "addictive" in P_Traits:
        $ R_Addictionrate += 1 
        
    call Partner_Like("Rogue",2)
     
    if R_SuckB == 1:            
            $ R_SEXP += 4         
            if not Situation: 
                if R_Love >= 500 and "unsatisfied" not in R_RecentActions:
                    ch_r "I . . . really liked that, [R_Petname]."
                elif R_Obed <= 500 and P_Focus <= 20:
                    call RogueFace("perplexed", 1)
                    ch_r "Did you like the taste?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_r "Mmm, so what else did you have in mind?"
    call Checkout
    return   
    
# End Suck breasts    

# Fondle Thighs start //////////////////////////////////////////

label R_Fondle_Thighs:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Rogue")
                                                                                        # Will she let you fondle her thighs? Modifiers
    if R_FondleT: #You've done it before
        $ Tempmod += 10
    if R_Legs == "pants" or HoseNum("Rogue") >= 5: # she's got pants on.
        $ Tempmod -= 5    
    if R_Lust > 75: #She's really horny
        $ Tempmod += 10    
    if "exhibitionist" in R_Traits:
        $ Tempmod += Taboo   
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 25 
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount      
    
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no fondle thighs" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle thighs" in R_RecentActions else 0   
            
    $ Approval = ApprovalCheck("Rogue", 750, TabM=1) # 75, 90, 105, Taboo -40(105)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            call RogueFace("sexy")       
            call Statup("Rogue", "Obed", 50, 1)
            call Statup("Rogue", "Inbt", 30, 2)            
            "As you caress her thigh, Rogue glances at you, and smiles."             
            jump RFT_Prep      
        else:               
            call RogueFace("surprised")
            call Statup("Rogue", "Obed", 50, -2)
            ch_r "Hands off the merchandise, [R_Petname]."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        call RogueFace("surprised")    
        $ R_Brows = "sad"
        if R_Lust > 60:
            call Statup("Rogue", "Love", 70, -3)
        call Statup("Rogue", "Obed", 90, 1)
        call Statup("Rogue", "Obed", 70, 2)
        "As you pull back, Rogue looks a little sad."              
        jump RFT_Prep  
    elif "fondle thighs" in R_RecentActions:
        call RogueFace("sexy", 1)
        ch_r "Mmm, again? Ok."
        jump RFT_Prep
    elif "fondle thighs" in R_DailyActions:
        call RogueFace("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "You do have a smooth touch. . .",
            "Mmm. . ."]) 
        ch_r "[Line]"
    
    if Approval >= 2:                                                                   #She's into it. . .
        call RogueFace("bemused", 1)
        if R_Forced:
            call RogueFace("sad")
            call Statup("Rogue", "Love", 70, -3, 1)
            call Statup("Rogue", "Obed", 90, 1)
            call Statup("Rogue", "Inbt", 60, 1)
        ch_r "Ok [R_Petname], go ahead."   
        call Statup("Rogue", "Love", 90, 1)
        call Statup("Rogue", "Inbt", 50, 3) 
        jump RFT_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        call RogueFace("angry", 1)
        if "no fondle thighs" in R_RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions and "no fondle thighs" in R_DailyActions:  
            ch_r "I told you not to touch me like that in public!" 
        elif "no fondle thighs" in R_DailyActions:       
            ch_r "I already told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions:  
            ch_r "I told you not in public!"  
        elif not R_FondleT:
            call RogueFace("bemused")
            ch_r "I just don't think I'm ready yet, [R_Petname]. . ."
        else:
            call RogueFace("bemused")
            ch_r "I'd really rather not."  
        menu:
            extend ""
            "Sorry, never mind." if "no fondle thighs" in R_DailyActions:
                call RogueFace("bemused")
                ch_r "Yeah, ok, [R_Petname]."              
                return
            "Maybe later?" if "no fondle thighs" not in R_DailyActions:
                call RogueFace("sexy")  
                ch_r "Heh, maybe, [R_Petname]."
                call Statup("Rogue", "Love", 80, 1)
                call Statup("Rogue", "Inbt", 30, 2)    
                if Taboo:                    
                    $ R_RecentActions.append("tabno")                      
                    $ R_DailyActions.append("tabno") 
                $ R_RecentActions.append("no fondle thighs")                      
                $ R_DailyActions.append("no fondle thighs")            
                return
            "Come on, Please?":             
                if Approval:
                    call RogueFace("sexy")     
                    call Statup("Rogue", "Obed", 60, 1)
                    call Statup("Rogue", "Obed", 30, 2)
                    call Statup("Rogue", "Inbt", 50, 1)
                    call Statup("Rogue", "Inbt", 30, 2)
                    ch_r "Heh, I suppose I can hardly refuse ya when you use the magic words . . ."             
                    jump RFT_Prep
                else:   
                    call RogueFace("sexy") 
                    ch_r "I'm afraid not this time, sorry [R_Petname]."     
            
            "[[Start caressing her thigh anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Rogue", 350, "OI", TabM = 2) # 35, 50, 65, -80(105)
                if Approval > 1 or (Approval and R_Forced):
                    call RogueFace("sad")
                    call Statup("Rogue", "Love", 70, -5, 1)
                    call Statup("Rogue", "Love", 20, -2, 1)                 
                    ch_r "Hmmph."                         
                    call Statup("Rogue", "Obed", 50, 3)
                    call Statup("Rogue", "Inbt", 60, 2)  
                    if Approval < 2:                          
                        $ R_Forced = 1
                    jump RFT_Prep
                else:                              
                    call Statup("Rogue", "Love", 200, -8)  
                    call RogueFace("angry", 1)
                    "She slaps your hand away."   
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")   
                    
    if "no fondle thighs" in R_DailyActions:
        ch_r "Learn to take \"no\" for an answer, [R_Petname]."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1)
        ch_r "Not even that much."
        call Statup("Rogue", "Lust", 50, 2)    
        call Statup("Rogue", "Obed", 50, -1)   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:
        call RogueFace("angry", 1)    
        $ R_RecentActions.append("tabno")          
        $ R_DailyActions.append("tabno") 
        ch_r "I really don't think this is the right place for that!"                   
    elif R_FondleT:
        call RogueFace("sad")
        ch_r "Fresh!"            
    else:
        call RogueFace("sexy") 
        $ R_Mouth = "sad"
        ch_r "No luck, [R_Petname]."
    $ R_RecentActions.append("no fondle thighs")                      
    $ R_DailyActions.append("no fondle thighs") 
    $ Tempmod = 0    
    return
    
label RFT_Prep:                                                                 #Animation set-up 
label R_FT_Prep:                                                                 #Animation set-up 
    if Trigger == "kiss you": 
        $ Trigger = "fondle thighs" 
        return
        
    if Trigger2 == "fondle thighs": 
        return
        
    if not R_Forced and Situation != "auto":
        $ Tempmod = 0
        call Rogue_Bottoms_Off 
        if "angry" in R_RecentActions:
            return 
            
    $ Tempmod = 0    
    call R_Pussy_Launch("fondle thighs")
    if not R_FondleT:        
        if R_Forced:
            call Statup("Rogue", "Love", 90, -10)
            call Statup("Rogue", "Obed", 70, 15)
            call Statup("Rogue", "Inbt", 80, 10) 
        else:
            call Statup("Rogue", "Love", 90, 5)
            call Statup("Rogue", "Obed", 70, 10)
            call Statup("Rogue", "Inbt", 80, 15) 
            
    if Taboo:               
        call Statup("Rogue", "Lust", 200, (int(Taboo/5)))                               
        call Statup("Rogue", "Inbt", 200, (2*(int(Taboo/5))))
     
    if Situation:   
        $ renpy.pop_call() 
        $ Situation = 0 
    $ Line = 0 
    $ Cnt = 0
    if Taboo:
        call DrainWord("Rogue","tabno")
    call DrainWord("Rogue","no fondle thighs")
    $ R_RecentActions.append("fondle thighs")                      
    $ R_DailyActions.append("fondle thighs")  
    
label RFT_Cycle: #Repeating strokes 
    while Round >=0:  
        call Shift_Focus("Rogue") 
        call R_Pussy_Launch("fondle thighs")
        call RogueLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                         
                        "Slap her ass":                     
                                    call R_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump RFT_Cycle  
                                    
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
                                                        "Can I do a little deeper?":
                                                                if R_Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call RFT_After
                                                                    call R_Fondle_Pussy                
                                                                else:
                                                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                                                        "Shift your hands a bit higher without asking":
                                                                if R_Action and MultiAction:
                                                                    $ Situation = "auto"
                                                                    call RFT_After
                                                                    call R_Fondle_Pussy    
                                                                else:
                                                                    "As your hands creep upwards, she grabs your wrists."
                                                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?" 
                                                        "Never Mind":
                                                                jump RFT_Cycle
                                            else: 
                                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"           
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call RFT_After
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
                                                        jump RFT_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump RFT_Cycle 
                                            "Never mind":
                                                        jump RFT_Cycle 
                                    "Undress Rogue":
                                            call R_Undress   
                                    "Clean up Rogue (locked)" if not R_Spunk:
                                            pass  
                                    "Clean up Rogue" if R_Spunk:
                                            call Rogue_Cleanup("ask")                                         
                                    "Never mind":
                                            jump RFT_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call R_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump RFT_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call R_Pos_Reset
                                    $ Line = 0
                                    jump RFT_After
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
                                call R_Pos_Reset
                                return    
                            call Statup("Rogue", "Lust", 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2 and R_SEXP >= 20:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump RFT_After 
                            $ Line = "came"
     
                    if R_Lust >= 100:  
                            #If Rogue can cum                                             
                            call R_Cumming
                            if Situation == "shift" or "angry" in R_RecentActions:
                                jump RFT_After
                       
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
                                        jump RFT_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Rogue")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if R_SEXP >= 100 or ApprovalCheck("Rogue", 1200, "LO"):
            pass
        elif Cnt == (5 + R_FondleT):
                    $ R_Brows = "confused"
                    ch_r "You like how those feel, huh?"   
        elif Cnt == (15 + R_FondleT) and R_SEXP >= 15 and not ApprovalCheck("Rogue", 1500):
                    $ R_Brows = "confused"        
                    menu:
                        ch_r "I know you're having fun, but maybe we could try something else [R_Petname]."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump RFT_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump RFT_After
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
                                    jump RFT_After
        #End Count check
           
        call Escalation("Rogue","R") #sees if she wants to escalate things
        
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0)
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
    
label RFT_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call R_Pos_Reset
        
    call RogueFace("sexy") 
    
    $ R_FondleT += 1  
    $ R_Action -=1
    if R_Legs != "pants" or R_Upskirt:        
        $ R_Addictionrate += 1
        if "addictive" in P_Traits:
            $ R_Addictionrate += 1
            
        call Partner_Like("Rogue",1,0)
     
    if R_FondleT == 1:            
            $ R_SEXP += 3         
            if not Situation: 
                if R_Love >= 500 and "unsatisfied" not in R_RecentActions:
                    ch_r "That was. . . nice."
                elif R_Obed <= 500 and P_Focus <= 20:
                    call RogueFace("perplexed", 1)
                    ch_r "Was that enough for you?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_r "Mmm, so what else did you have in mind?"
    call Checkout
    return   
    
# ////////////////////////////////////////////////////////////////////////Start Fondle Pussy    
label R_Fondle_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Rogue")
                                                                                        # Will she let you fondle? Modifiers
    if R_FondleP: #You've done it before
        $ Tempmod += 20
    if R_Legs == "pants" or HoseNum("Rogue") >= 5: # she's got pants on.
        $ Tempmod -= 10    
    if R_Lust > 75: #She's really horny
        $ Tempmod += 15
    if R_Lust > 75 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in R_Traits:
        $ Tempmod += (2*Taboo)
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 25  
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount     
    
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no fondle pussy" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle pussy" in R_RecentActions else 0   
            
    $ Approval = ApprovalCheck("Rogue", 1050, TabM = 2) # 105, 120, 135, Taboo -80(185)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            call RogueFace("sexy")       
            call Statup("Rogue", "Obed", 90, 1)
            call Statup("Rogue", "Obed", 70, 2)
            call Statup("Rogue", "Inbt", 70, 3)
            call Statup("Rogue", "Inbt", 30, 2)
            "As your hand creeps up her thigh, Rogue seems a bit surprised, but then nods."            
            jump RFP_Prep      
        else:               
            call RogueFace("surprised")
            call Statup("Rogue", "Obed", 50, -2)
            ch_r "Hey, just keep doing what you were doing, [R_Petname]."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        call RogueFace("surprised")   
        $ R_Brows = "sad"        
        if R_Lust > 80:
            call Statup("Rogue", "Love", 70, -4)
        call Statup("Rogue", "Obed", 90, 1)
        call Statup("Rogue", "Obed", 70, 2)
        "As your hand pulls out, Rogue gasps and looks upset."              
        jump RFP_Prep     
    elif "fondle pussy" in R_RecentActions:
        call RogueFace("sexy", 1)
        ch_r "Mmm, again? Ok."
        jump RFP_Prep
    elif "fondle pussy" in R_DailyActions:
        call RogueFace("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so hard this time though.",
            "Take it a bit gently, I'm still quivering from earlier.",
            "Mmm. . ."]) 
        ch_r "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .
        call RogueFace("bemused", 1)
        if R_Forced:
            call RogueFace("sad")
            call Statup("Rogue", "Love", 70, -3, 1)
            call Statup("Rogue", "Love", 20, -2, 1)
            call Statup("Rogue", "Obed", 90, 1)
            call Statup("Rogue", "Inbt", 60, 1)
        ch_r "Sure, get in there."   
        call Statup("Rogue", "Love", 90, 1)
        call Statup("Rogue", "Inbt", 50, 3) 
        jump RFP_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        call RogueFace("angry", 1)
        if "no fondle pussy" in R_RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions and "no fondle pussy" in R_DailyActions:  
            ch_r "I told you not to touch me like that in public!" 
        elif "no fondle pussy" in R_DailyActions:       
            ch_r "I already told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions:  
            ch_r "I told you not in public!"  
        elif not R_FondleP:
            call RogueFace("bemused")
            ch_r "Um, not down there, [R_Petname]. . ."
        else:
            call RogueFace("bemused")
            ch_r "I'd really rather not."  
        menu:
            extend ""
            "Sorry, never mind." if "no fondle pussy" in R_DailyActions:
                call RogueFace("bemused")
                ch_r "Yeah, ok, [R_Petname]."              
                return
            "Maybe later?" if "no fondle pussy" not in R_DailyActions:
                call RogueFace("sexy")  
                ch_r "I'll give it some thought, [R_Petname]."
                call Statup("Rogue", "Love", 80, 2)
                call Statup("Rogue", "Inbt", 70, 2)   
                if Taboo:                    
                    $ R_RecentActions.append("tabno")                      
                    $ R_DailyActions.append("tabno") 
                $ R_RecentActions.append("no fondle pussy")                      
                $ R_DailyActions.append("no fondle pussy")            
                return
            "Come on, Please?":             
                if Approval:
                    call RogueFace("sexy")     
                    call Statup("Rogue", "Obed", 90, 2)
                    call Statup("Rogue", "Obed", 50, 2)
                    call Statup("Rogue", "Inbt", 70, 3) 
                    call Statup("Rogue", "Inbt", 40, 2) 
                    ch_r "Well, if you're gonna beg. . ."                    
                    jump RFP_Prep
                else:   
                    call RogueFace("sexy") 
                    ch_r "Tsk, not this time, [R_Petname]." 
            
            "[[Start fondling anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Rogue", 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                if Approval > 1 or (Approval and R_Forced):
                    call RogueFace("sad")
                    call Statup("Rogue", "Love", 70, -5, 1)
                    call Statup("Rogue", "Love", 200, -2)                 
                    ch_r "Well, at least make it worth it."
                    call Statup("Rogue", "Obed", 50, 4)
                    call Statup("Rogue", "Inbt", 80, 1) 
                    call Statup("Rogue", "Inbt", 60, 3)  
                    if Approval < 2:                          
                        $ R_Forced = 1
                    jump RFP_Prep
                else:                              
                    call Statup("Rogue", "Love", 200, -15)  
                    call RogueFace("angry", 1)
                    "She slaps your hand away."   
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")   
                    
    if "no fondle pussy" in R_DailyActions:
        ch_r "Learn to take \"no\" for an answer, [R_Petname]."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1)
        ch_r "Stay out of my pants, [R_Petname]."
        call Statup("Rogue", "Lust", 70, 5)    
        call Statup("Rogue", "Obed", 50, -2)    
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:
        call RogueFace("angry", 1)    
        $ R_RecentActions.append("tabno")                   
        $ R_DailyActions.append("tabno")
        ch_r "I really don't think this is the right place for that!"                   
    elif R_FondleP:
        call RogueFace("sad")
        ch_r "Sorry, keep your hands out of there."           
    else:
        call RogueFace("sexy") 
        $ R_Mouth = "sad"
        ch_r "No luck [R_Petname]."
    $ R_RecentActions.append("no fondle pussy")                      
    $ R_DailyActions.append("no fondle pussy") 
    $ Tempmod = 0    
    return
    
ch_r "Sorry, I don't even know how I got here. . ."
return
                
label RFP_Prep: #Animation set-up 
label R_FP_Prep: #Animation set-up 
    if Trigger2 == "fondle pussy":
        return
            
    call R_Pussy_Launch("fondle pussy")
    
    if Situation == "Rogue":                                                        
            #Rogue auto-starts    
            $ Situation = 0
            if (R_Legs and not R_Upskirt) or (R_Panties and not R_PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck("Rogue", 1250, TabM = 1) or (R_SeenPussy and ApprovalCheck("Rogue", 500) and not Taboo):
                        $ R_Upskirt = 1
                        $ R_PantiesDown = 1
                        $ Line = 0
                        if R_Legs == "skirt":
                            $ Line = "Rogue hikes up her skirt"
                        elif PantsNum("Rogue") >= 5:
                            $ Line = "Rogue pulls down her " + R_Legs
                        else:
                            $ Line = 0                            
                        if R_Panties:
                            if Line:
                                #wearing pants
                                "[Line] and pulls her [R_Panties] out of the way."
                                "She then grabs your arm and shoves your hand into her crotch, clearly intending you to get to work."
                            else:
                                #no pants
                                "She pulls her [R_Panties] out of the way, and then shoves your hand into her crotch."
                                "She clearly intends for you to get to work." 
                        else:
                            #pants but no panties
                            "[Line], and then shoves your hand into her crotch."
                            "She clearly intends for you to get to work."                     
                        call Rogue_First_Bottomless(1)
                else:
                    "Rogue grabs your arm and shoves your hand into her crotch, clearly intending you to get to work."
            else:
                "Rogue grabs your arm and shoves your hand into her crotch, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":                    
                    call Statup("Rogue", "Inbt", 80, 3) 
                    call Statup("Rogue", "Inbt", 50, 2)
                    "You start to run your fingers along her pussy."
                "Praise her.":       
                    call RogueFace("sexy", 1)                    
                    call Statup("Rogue", "Inbt", 80, 3) 
                    ch_p "I like the initiative, [R_Pet]."
                    call Rogue_Namecheck
                    "You start to run your fingers along her pussy."
                    call Statup("Rogue", "Love", 85, 1)
                    call Statup("Rogue", "Obed", 90, 1)
                    call Statup("Rogue", "Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your hand back."
                    call RogueFace("surprised")       
                    call Statup("Rogue", "Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [R_Pet]."
                    call Rogue_Namecheck
                    "Rogue pulls back."
                    call Statup("Rogue", "Obed", 90, 1)
                    call Statup("Rogue", "Obed", 50, 1)
                    call Statup("Rogue", "Obed", 30, 2)
                    $ P_RecentActions.append("nope")      
                    call AnyWord("Rogue",1,"refused","refused")  
                    return          
            #end auto
            
    if not R_Forced and Situation != "auto":
        $ Tempmod = 0
        call Rogue_Bottoms_Off   
        if "angry" in R_RecentActions:
            return 
    $ Tempmod = 0
    if not R_FondleP:        
        if R_Forced:
            call Statup("Rogue", "Love", 90, -50)
            call Statup("Rogue", "Obed", 70, 35)
            call Statup("Rogue", "Inbt", 80, 25) 
        else:
            call Statup("Rogue", "Love", 90, 10)
            call Statup("Rogue", "Obed", 70, 10)
            call Statup("Rogue", "Inbt", 80, 15) 
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
    call DrainWord("Rogue","no fondle pussy")
    $ R_RecentActions.append("fondle pussy")                      
    $ R_DailyActions.append("fondle pussy") 
    
    $ Speed = 1
    
label RFP_Cycle: #Repeating strokes 
    while Round >=0:  
        call Shift_Focus("Rogue") 
        call R_Pussy_Launch("fondle pussy")
        call RogueLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                          
                        "I want to stick a finger in. . ." if Speed != 2:
                                if R_InsertP: 
                                    $ Speed = 2
                                else:
                                    menu:                                
                                        "Ask her first":
                                            $ Situation = "shift"
                                        "Don't ask first [[just stick it in]":                                    
                                            $ Situation = "auto"
                                    call R_Insert_Pussy 
                        
                        "Pull back a bit. . ." if Speed == 2:
                                    $ Speed = 0
                                    
                        "Slap her ass":                     
                                    call R_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump RFP_Cycle  
                                    
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
                                                        "I want to lick your pussy.":
                                                                $ Situation = "shift"
                                                                call RFP_After
                                                                call R_Lick_Pussy                 
                                                        "Just start licking":
                                                                $ Situation = "auto"
                                                                call RFP_After
                                                                call R_Lick_Pussy         
                                                        "Pull back to the thighs":
                                                                $ Situation = "pullback"
                                                                call RFP_After
                                                                call R_Fondle_Thighs
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call RFP_After
                                                                call R_Dildo_Pussy  
                                                        "Never Mind":
                                                                jump RFP_Cycle
                                            else: 
                                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"           
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call RFP_After
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
                                                        jump RFP_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump RFP_Cycle 
                                            "Never mind":
                                                        jump RFP_Cycle 
                                    "Undress Rogue":
                                            call R_Undress   
                                    "Clean up Rogue (locked)" if not R_Spunk:
                                            pass  
                                    "Clean up Rogue" if R_Spunk:
                                            call Rogue_Cleanup("ask")                                         
                                    "Never mind":
                                            jump RFP_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call R_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump RFP_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call R_Pos_Reset
                                    $ Line = 0
                                    jump RFP_After
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
                                call R_Pos_Reset
                                return    
                            call Statup("Rogue", "Lust", 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump RFP_After 
                            $ Line = "came"
     
                    if R_Lust >= 100:  
                            #If Rogue can cum                                             
                            call R_Cumming
                            if Situation == "shift" or "angry" in R_RecentActions:
                                jump RFP_After
                       
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
                                        jump RFP_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Rogue")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if R_SEXP >= 100 or ApprovalCheck("Rogue", 1200, "LO"):
            pass
        elif Cnt == (5 + R_FondleP):
                    $ R_Brows = "confused"
                    ch_r "You like how that feels, huh?"  
        elif R_Lust >= 80:
                    pass
        elif Cnt == (15 + R_FondleP) and R_SEXP >= 15 and not ApprovalCheck("Rogue", 1500):
                    $ R_Brows = "confused"        
                    menu:
                        ch_r "I know you're having fun, but maybe we could try something else [R_Petname]."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump RFP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump RFP_After
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
                                    jump RFP_After
        #End Count check
           
        call Escalation("Rogue","R") #sees if she wants to escalate things
        
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0)
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
    
label RFP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call R_Pos_Reset
        
    call RogueFace("sexy") 
    
    $ R_FondleP += 1  
    $ R_Action -=1
    if R_Legs != "pants" or R_Upskirt:        
        $ R_Addictionrate += 1
        if "addictive" in P_Traits:
            $ R_Addictionrate += 1
            
    call Partner_Like("Rogue",2)
            
    if R_FondleP == 1:            
            $ R_SEXP += 7         
            if not Situation: 
                if R_Love >= 500 and "unsatisfied" not in R_RecentActions:
                    ch_r "Certainly different with someone else at the wheel."
                elif R_Obed <= 500 and P_Focus <= 20:
                    call RogueFace("perplexed", 1)
                    ch_r "Was that enough for you?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_r "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# end R_Fondle Pussy /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label R_Insert_Pussy:
    call Shift_Focus("Rogue")
    if Situation == "auto":                                                                  #You auto-start                    
        if ApprovalCheck("Rogue", 1100, TabM = 2):
            call RogueFace("surprised")       
            call Statup("Rogue", "Obed", 90, 1)
            call Statup("Rogue", "Obed", 70, 2)
            call Statup("Rogue", "Inbt", 70, 3) 
            call Statup("Rogue", "Inbt", 30, 2) 
            "As you slide a finger in, Rogue seems a bit surprised, but seems into it."              
            jump RIP_Prep
        else:   
            call RogueFace("surprised")
            call Statup("Rogue", "Love", 80, -2)
            call Statup("Rogue", "Obed", 50, -3)
            ch_r "Keep it outside, [R_Petname]."   
            return            
    
    if ApprovalCheck("Rogue", 1100, TabM = 2):                                                                   #She's into it. . .               
        if R_Forced:
            call RogueFace("sad")
            call Statup("Rogue", "Love", 70, -3, 1)
            call Statup("Rogue", "Love", 20, -2, 1)
            call Statup("Rogue", "Obed", 90, 1)
            call Statup("Rogue", "Inbt", 60, 1)
            ch_r "Sure, get in there."    
        else:
            call RogueFace("sexy", 1)
            call Statup("Rogue", "Love", 90, 1)
            call Statup("Rogue", "Inbt", 50, 3) 
            ch_r "God yes."                
        call Statup("Rogue", "Obed", 20, 1)
        call Statup("Rogue", "Obed", 60, 1)
        call Statup("Rogue", "Inbt", 70, 2) 
        jump RIP_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .  
        call RogueFace("bemused", 2)
        ch_r "Um, no thanks, [R_Petname]."
        $ R_Blush = 1
    return
    
                
label RIP_Prep: #Animation set-up     
label R_IP_Prep: #Animation set-up    
    if not R_InsertP:
        $ R_InsertP = 1
        $ R_SEXP += 10          
        if R_Forced:
            call Statup("Rogue", "Love", 90, -60)
            call Statup("Rogue", "Obed", 70, 55)
            call Statup("Rogue", "Inbt", 80, 35) 
        else:
            call Statup("Rogue", "Love", 90, 10)
            call Statup("Rogue", "Obed", 70, 20)
            call Statup("Rogue", "Inbt", 80, 25)
        
    if not R_Forced and Situation != "auto":        
        call R_Undress("bottom")
        if "angry" in R_RecentActions:
            return    
            
#    call R_Pussy_Launch("insert pussy")
    if Taboo:
        $ R_Inbt += int(Taboo/10)  
        $ R_Lust += int(Taboo/5)
        
    $ Line = 0   
    $ Speed = 2
    return

# end R_Insert Pussy /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label R_Lick_Pussy: 
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Rogue")
                                                                                  # Will she let you fondle? Modifiers     
    if R_LickP: #You've done it before
        $ Tempmod += 15
    if R_Legs == "pants" or HoseNum("Rogue") >= 5: # she's got pants on.
        $ Tempmod -= 15  
    if R_Lust > 95:
        $ Tempmod += 20  
    elif R_Lust > 85: #She's really horny
        $ Tempmod += 15
    if Situation == "shift":
        $ Tempmod += 10
    if R_Lust > 85 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in R_Traits:
        $ Tempmod += (4*Taboo) 
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 25  
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount     
    
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no lick pussy" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no lick pussy" in R_RecentActions else 0   
            
    $ Approval = ApprovalCheck("Rogue", 1250, TabM = 4) # 125, 140, 155, Taboo -160(285)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            call RogueFace("surprised")
            call Statup("Rogue", "Obed", 90, 1)
            call Statup("Rogue", "Obed", 70, 2)
            call Statup("Rogue", "Inbt", 70, 3) 
            call Statup("Rogue", "Inbt", 30, 2) 
            "As you crouch down and start to lick her pussy, Rogue startles, but then sinks into the sensation."  
            call RogueFace("sexy")           
            jump RLP_Prep
        else:   
            call RogueFace("surprised")
            call Statup("Rogue", "Love", 80, -2)
            call Statup("Rogue", "Obed", 50, -3)
            ch_r "Oh! No, no thank you, [R_Petname]."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return            
    
    if "lick pussy" in R_RecentActions:
        call RogueFace("sexy", 1)
        ch_r "Mmm, again? Ok."
        jump RLP_Prep
    elif "lick pussy" in R_DailyActions:
        call RogueFace("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Again? Oh, you're insatiable!",
            "Must be my lucky day!",
            "You sure know how to keep a girl satisfied. . .",
            "Mmm. . ."]) 
        ch_r "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .               
        if R_Forced:
            call RogueFace("sad")
            call Statup("Rogue", "Love", 70, -3, 1)
            call Statup("Rogue", "Love", 20, -2, 1)
            call Statup("Rogue", "Obed", 90, 1)
            call Statup("Rogue", "Inbt", 60, 1)
            ch_r "Sure, get in there."    
        else:
            call RogueFace("sexy", 1)
            $ R_Eyes = "closed"            
            call Statup("Rogue", "Love", 90, 1)
            call Statup("Rogue", "Inbt", 50, 3)            
            call Statup("Rogue", "Lust", 200, 3)
            ch_r "Oooooooh. . ."                
        call Statup("Rogue", "Obed", 20, 1)
        call Statup("Rogue", "Obed", 60, 1)
        call Statup("Rogue", "Inbt", 70, 2) 
        jump RLP_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call RogueFace("angry", 1)
        if "no lick pussy" in R_RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions and "no lick pussy" in R_DailyActions:  
            ch_r "You already got your answer!" 
        elif "no lick pussy" in R_DailyActions:       
            ch_r "I already told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions:  
            ch_r "I told you not in public!"  
        elif not R_LickP:
            call RogueFace("bemused")
            ch_r "That's pretty intimate, [R_Petname]. . ."
        else:
            call RogueFace("bemused")
            ch_r "Oh, um, no, I'm not really comfortable with that. . ." 
        menu:
            extend ""
            "Sorry, never mind." if "no lick pussy" in R_DailyActions:
                call RogueFace("bemused")
                ch_r "Yeah, ok, [R_Petname]."              
                return            
            "I'm sure I can convince you later. . ." if "no lick pussy" not in R_DailyActions:
                call RogueFace("sexy")  
                ch_r "I'll be thinking about it, [R_Petname]."
                call Statup("Rogue", "Love", 80, 2)
                call Statup("Rogue", "Inbt", 70, 2)   
                if Taboo:                    
                    $ R_RecentActions.append("tabno")                      
                    $ R_DailyActions.append("tabno") 
                $ R_RecentActions.append("no lick pussy")                      
                $ R_DailyActions.append("no lick pussy")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    call RogueFace("sexy")           
                    call Statup("Rogue", "Obed", 90, 2)
                    call Statup("Rogue", "Obed", 50, 2)
                    ch_r "Ok, you're probably right. . ."      
                    call Statup("Rogue", "Inbt", 70, 3) 
                    call Statup("Rogue", "Inbt", 40, 2)
                    jump RLP_Prep
                else:   
                    call RogueFace("sexy") 
                    ch_r "Tsk, not this time, [R_Petname], that just seems. . . intimate."     
            
            "[[Get in there anyway]":                                               # Pressured into being licked. 
                $ Approval = ApprovalCheck("Rogue", 750, "OI", TabM = 4) # 75, 90, 105, -160(235)
                if Approval > 1 or (Approval and R_Forced):
                    call RogueFace("sad")
                    call Statup("Rogue", "Love", 70, -5, 1)
                    call Statup("Rogue", "Love", 200, -2)                 
                    ch_r "Ok, get in there if you're so determined."  
                    call Statup("Rogue", "Obed", 50, 4)
                    call Statup("Rogue", "Inbt", 80, 1) 
                    call Statup("Rogue", "Inbt", 60, 3)  
                    if Approval < 2:                          
                        $ R_Forced = 1
                    jump RLP_Prep
                else:                              
                    call Statup("Rogue", "Love", 200, -15)  
                    call RogueFace("angry", 1)
                    "She shoves your head back."   
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")   
                    
    if "no lick pussy" in R_DailyActions:
        ch_r "Learn to take \"no\" for an answer, [R_Petname]."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1)
        ch_r "Not even, [R_Petname]."
        call Statup("Rogue", "Lust", 80, 5)    
        call Statup("Rogue", "Obed", 50, -2)     
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:
        call RogueFace("angry", 1)    
        $ R_RecentActions.append("tabno")                   
        $ R_DailyActions.append("tabno") 
        ch_r "This just really isn't the time or place, [R_Petname]!"                   
    elif R_LickP:
        call RogueFace("sad") 
        ch_r "Sorry, keep your tongue in your mouth."    
    else:
        call RogueFace("surprised")
        ch_r "Ew!"
        call RogueFace
    $ R_RecentActions.append("no lick pussy")                      
    $ R_DailyActions.append("no lick pussy") 
    $ Tempmod = 0    
    return
    
label RLP_Prep: #Animation set-up  
label R_LP_Prep: #Animation set-up  
    if Trigger2 == "lick pussy": #fix pull down pants now an option, make it work
        return
             
    call R_Pussy_Launch("lick pussy")
    
    
    if Situation == "Rogue":                                                       
            #Rogue auto-starts    
            $ Situation = 0
            if (R_Legs and not R_Upskirt) or (R_Panties and not R_PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck("Rogue", 1250, TabM = 1) or (R_SeenPussy and ApprovalCheck("Rogue", 500) and not Taboo):
                        $ R_Upskirt = 1
                        $ R_PantiesDown = 1
                        $ Line = 0
                        if R_Legs == "skirt":
                            $ Line = "Rogue hikes up her skirt"
                        elif PantsNum("Rogue") >= 5:
                            $ Line = "Rogue pulls down her " + R_Legs
                        else:
                            $ Line = 0                            
                        if R_Panties:
                            if Line:
                                #wearing pants
                                "[Line] and pulls her [R_Panties] out of the way."
                                "She then grabs your head and pulls it to her crotch, clearly intending you to get to work."
                            else:
                                #no pants
                                "She pulls her [R_Panties] out of the way, and then shoves your face into her crotch."
                                "She clearly intends for you to get to work." 
                        else:
                            #pants but no panties
                            "[Line], and then shoves your face into her crotch."
                            "She clearly intends for you to get to work."                     
                        call Rogue_First_Bottomless(1)
                else:
                    "Rogue grabs your head and pulls it to her crotch, clearly intending you to get to work."
            else:
                "Rogue grabs your head and pulls it to her crotch, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":                    
                    call Statup("Rogue", "Inbt", 80, 3) 
                    call Statup("Rogue", "Inbt", 50, 2)
                    "You start licking."
                "Praise her.":       
                    call RogueFace("sexy", 1)                    
                    call Statup("Rogue", "Inbt", 80, 3) 
                    ch_p "Mmm, I like this idea, [R_Pet]."
                    call Rogue_Namecheck
                    "You start licking."
                    call Statup("Rogue", "Love", 85, 1)
                    call Statup("Rogue", "Obed", 90, 1)
                    call Statup("Rogue", "Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your head away."
                    call RogueFace("surprised")       
                    call Statup("Rogue", "Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [R_Pet]."
                    call Rogue_Namecheck
                    "Rogue pulls back."
                    call Statup("Rogue", "Obed", 90, 1)
                    call Statup("Rogue", "Obed", 50, 1)
                    call Statup("Rogue", "Obed", 30, 2)
                    $ P_RecentActions.append("nope")      
                    call AnyWord("Rogue",1,"refused","refused")  
                    return          
            #end auto
            
    if not R_Forced and Situation != "auto":
        $ Tempmod = 0
        if R_Legs == "pants":
            $ Tempmod = 15
        call Rogue_Bottoms_Off
        if "angry" in R_RecentActions:
            return  
            
    $ Tempmod = 0 
    if not R_LickP:        
        if R_Forced:
            call Statup("Rogue", "Love", 90, -30)
            call Statup("Rogue", "Obed", 70, 35)
            call Statup("Rogue", "Inbt", 80, 75) 
        else:
            call Statup("Rogue", "Love", 90, 35)
            call Statup("Rogue", "Obed", 70, 15)
            call Statup("Rogue", "Inbt", 80, 35)
    if Taboo:
        $ R_Inbt += int(Taboo/10)  
        $ R_Lust += int(Taboo/5)
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
        
    if R_Legs == "skirt":
        $ R_Upskirt = 1  
        $ R_SeenPanties = 1
    call Rogue_First_Bottomless(1)
    
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Rogue","tabno")
    call DrainWord("Rogue","no lick pussy")
    $ R_RecentActions.append("lick pussy")                      
    $ R_DailyActions.append("lick pussy") 
    
label RLP_Cycle: #Repeating strokes
    if Trigger2 == "kiss you":
            $ Trigger2 = 0   
    while Round >=0:  
        call Shift_Focus("Rogue") 
        call R_Pussy_Launch("lick pussy")
        call RogueLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                                              
                        "Slap her ass":                     
                                    call R_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump RLP_Cycle  
                                    
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
                                                        "Pull out and start rubbing again.":
                                                                if R_Action and MultiAction:
                                                                    $ Situation = "pullback"
                                                                    call RLP_After
                                                                    call R_Fondle_Pussy
                                                                else:
                                                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call RLP_After
                                                                call R_Dildo_Pussy  
                                                        "Never Mind":
                                                                jump RLP_Cycle
                                            else: 
                                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"           
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call RLP_After
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
                                                        jump RLP_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump RLP_Cycle 
                                            "Never mind":
                                                        jump RLP_Cycle 
                                    "Undress Rogue":
                                            call R_Undress   
                                    "Clean up Rogue (locked)" if not R_Spunk:
                                            pass  
                                    "Clean up Rogue" if R_Spunk:
                                            call Rogue_Cleanup("ask")                                         
                                    "Never mind":
                                            jump RLP_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call R_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump RLP_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call R_Pos_Reset
                                    $ Line = 0
                                    jump RLP_After
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
                                jump RLP_After 
                            $ Line = "came"
     
                    if R_Lust >= 100:  
                            #If Rogue can cum                                             
                            call R_Cumming
                            if Situation == "shift" or "angry" in R_RecentActions:
                                jump RLP_After
                       
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
                                        jump RLP_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Rogue")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if R_SEXP >= 100 or ApprovalCheck("Rogue", 1200, "LO"):
            pass
        elif Cnt == (5 + R_LickP):
                    $ R_Brows = "confused"
                    ch_r "You like it down there?"  
        elif R_Lust >= 80:
                    pass
        elif Cnt == (15 + R_LickP) and R_SEXP >= 15 and not ApprovalCheck("Rogue", 1500):
                    $ R_Brows = "confused"        
                    menu:
                        ch_r "[R_Petname], I know you're having fun down there, but maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump RLP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump RLP_After
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
                                    jump RLP_After
        #End Count check
           
        call Escalation("Rogue","R") #sees if she wants to escalate things
        
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0)
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
    
label RLP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call R_Pos_Reset
        
    call RogueFace("sexy") 
    
    $ R_LickP += 1  
    $ R_Action -=1     
    if R_Legs != "pants" or R_Upskirt:        
        $ R_Addictionrate += 1
        if "addictive" in P_Traits:
            $ R_Addictionrate += 1
    
    if Partner == "Emma":
        call Partner_Like("Rogue",4,3)
    else:
        call Partner_Like("Rogue",3,3)
     
    if R_LickP == 1:            
            $ R_SEXP += 10         
            if not Situation: 
                if R_Love >= 500 and "unsatisfied" not in R_RecentActions:
                    ch_r "I. . . how'd I taste?"
                elif R_Obed <= 500 and P_Focus <= 20:
                    call RogueFace("perplexed", 1)
                    ch_r "Did you like that?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_r "Mmm, so what else did you have in mind?"
    call Checkout
    return   


# end R_Lick Pussy /////////////////////////////////////////////////////////////////////////////

    
# ////////////////////////////////////////////////////////////////////////Start Fondle Ass    
label R_Fondle_Ass: 
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Rogue")
                                                                                     # Will she let you fondle? Modifiers
    if R_FondleA: #You've done it before
        $ Tempmod += 10
    if R_Legs == "pants" or HoseNum("Rogue") >= 5: # she's got pants on.
        $ Tempmod -= 5     
    if R_Lust > 75: #She's really horny
        $ Tempmod += 15
    if "exhibitionist" in R_Traits:
        $ Tempmod += Taboo  
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 25 
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount      
    
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no fondle ass" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle ass" in R_RecentActions else 0   
        
    $ Approval = ApprovalCheck("Rogue", 850, TabM=1) # 85, 100, 115, Taboo -40(125)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:  
            call RogueFace("surprised", 1)  
            call Statup("Rogue", "Obed", 70, 2)
            call Statup("Rogue", "Inbt", 40, 2) 
            "As your hand creeps down her backside, Rogue seems a bit surprised, but then nods."              
            call RogueFace("sexy")  
            jump RFA_Prep  
        else:          
            call RogueFace("surprised")
            call Statup("Rogue", "Obed", 50, -3)
            ch_r "Hands off, [R_Petname]."   
            call RogueFace("bemused")
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        call RogueFace("surprised")   
        $ R_Brows = "sad"        
        if R_Lust > 80:
            call Statup("Rogue", "Love", 70, -4)
        call Statup("Rogue", "Obed", 90, 1)
        call Statup("Rogue", "Obed", 70, 2)
        "As your hand slides out, Rogue gasps and looks upset."              
        jump RFA_Prep     
    elif "fondle ass" in R_RecentActions:
        call RogueFace("sexy", 1)
        ch_r "Mmm, again? Ok."
        jump RFA_Prep
    elif "fondle ass" in R_DailyActions:
        call RogueFace("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so rough this time though.",
            "Mmm. . ."]) 
        ch_r "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .        
        if R_Forced:
            call RogueFace("sad")
            call Statup("Rogue", "Love", 70, -2, 1)
            call Statup("Rogue", "Obed", 90, 2)
            call Statup("Rogue", "Inbt", 60, 2)
            ch_r "Fine, grab a cheek."   
        else:
            call RogueFace("bemused, 1") 
            ch_r "Sure, grab a cheek."   
        call Statup("Rogue", "Lust", 200, 3)
        call Statup("Rogue", "Obed", 60, 1)
        call Statup("Rogue", "Inbt", 70, 1) 
        jump RFA_Prep
        
    else:                                                                               #She's not into it, but maybe. . .            
        call RogueFace("angry", 1)
        if "no fondle ass" in R_RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions and "no fondle ass" in R_DailyActions:  
            ch_r "I told you not to touch me like that in public!" 
        elif "no fondle ass" in R_DailyActions:       
            ch_r "I already told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions:  
            ch_r "I told you not in public!"  
        elif not R_FondleA:
            call RogueFace("bemused")
            ch_r "Not yet, [R_Petname]. . ."
        else:
            call RogueFace("bemused")
            ch_r "Let's not, ok [R_Petname]?"
        menu:
            extend ""
            "Sorry, never mind." if "no fondle ass" in R_DailyActions:
                call RogueFace("bemused")
                ch_r "Yeah, ok, [R_Petname]."              
                return
            "Maybe later?" if "no fondle ass" not in R_DailyActions:
                call RogueFace("sexy")  
                ch_r "Heh, maybe, [R_Petname]."
                call Statup("Rogue", "Love", 80, 2)
                call Statup("Rogue", "Inbt", 50, 2)  
                if Taboo:                    
                    $ R_RecentActions.append("tabno")                      
                    $ R_DailyActions.append("tabno") 
                $ R_RecentActions.append("no fondle ass")                      
                $ R_DailyActions.append("no fondle ass")            
                return
            "Just one good squeeze?":             
                if Approval:
                    call RogueFace("sexy")     
                    call Statup("Rogue", "Obed", 90, 1)
                    call Statup("Rogue", "Obed", 50, 2)
                    ch_r "Well, if you're gonna beg. . ."                           
                    call Statup("Rogue", "Inbt", 70, 1) 
                    call Statup("Rogue", "Inbt", 40, 2) 
                    jump RFA_Prep
                else:   
                    call RogueFace("sexy") 
                    ch_r "Tsk, not this time, [R_Petname]."      
            
            "[[Start fondling anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Rogue", 250, "OI", TabM = 3) # 25, 40, 55, -120(145)
                if Approval > 1 or (Approval and R_Forced):
                    call RogueFace("sad")
                    call Statup("Rogue", "Love", 70, -3, 1)
                    call Statup("Rogue", "Love", 200, -1) 
                    ch_r "Fine, I suppose."                
                    call Statup("Rogue", "Obed", 50, 3)
                    call Statup("Rogue", "Inbt", 60, 3) 
                    if Approval < 2:                          
                        $ R_Forced = 1
                    jump RFA_Prep
                else:                              
                    call Statup("Rogue", "Love", 200, -10)  
                    call RogueFace("angry", 1)
                    "She slaps your hand away."   
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")   
                        
    if "no fondle ass" in R_DailyActions:
        ch_r "Learn to take \"no\" for an answer, [R_Petname]."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1)
        ch_r "Hands off the booty!"
        call Statup("Rogue", "Lust", 60, 5)    
        call Statup("Rogue", "Obed", 50, -2)   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:
        call RogueFace("angry", 1)    
        $ R_RecentActions.append("tabno")   
        $ R_DailyActions.append("tabno") 
        ch_r "[R_Petname]! Not in public!"                   
    elif R_FondleA:
        call RogueFace("sad")
        ch_r "Sorry, hands off the booty."        
    else:
        call RogueFace("sexy") 
        $ R_Mouth = "sad"
        ch_r "Shoo, [R_Petname]."
    $ R_RecentActions.append("no fondle ass")                      
    $ R_DailyActions.append("no fondle ass") 
    $ Tempmod = 0    
    return
        
ch_r "Sorry, I don't even know how I got here. . ."
return

label RFA_Prep: #Animation set-up  
label R_FA_Prep: #Animation set-up 
    if Trigger2 == "fondle ass":
        return
    if not R_Forced and Situation != "auto":
        $ Tempmod = 0
        call Rogue_Bottoms_Off
        if "angry" in R_RecentActions:
            return    
    $ Tempmod = 0      
    call R_Pussy_Launch("fondle ass")
    if not R_FondleA:        
        if R_Forced:
            call Statup("Rogue", "Love", 90, -20)
            call Statup("Rogue", "Obed", 70, 20)
            call Statup("Rogue", "Inbt", 80, 15) 
        else:
            call Statup("Rogue", "Love", 90, 10)
            call Statup("Rogue", "Obed", 70, 12)
            call Statup("Rogue", "Inbt", 80, 20)
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
    call DrainWord("Rogue","no fondle ass")
    $ R_RecentActions.append("fondle ass")                      
    $ R_DailyActions.append("fondle ass") 
    
label RFA_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Rogue") 
        call R_Pussy_Launch("fondle ass")
        call RogueLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                                              
                        "Slap her ass":                     
                                    call R_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump RFA_Cycle  
                                    
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
                                                        "I want to stick a finger in.":
                                                                $ Situation = "shift"
                                                                call RFA_After
                                                                call R_Insert_Ass    
                                                        "Just stick a finger in without asking.":
                                                                $ Situation = "auto"
                                                                call RFA_After
                                                                call R_Insert_Ass
                                                        "I want to lick your asshole.":
                                                                $ Situation = "shift"
                                                                call RFA_After
                                                                call R_Lick_Ass                 
                                                        "Just start licking.":
                                                                $ Situation = "auto"
                                                                call RFA_After
                                                                call R_Lick_Ass    
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call RFA_After
                                                                call R_Dildo_Ass  
                                                        "Never Mind":
                                                                jump RFA_Cycle
                                            else: 
                                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"           
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call RFA_After
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
                                                        jump RFA_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump RFA_Cycle 
                                            "Never mind":
                                                        jump RFA_Cycle 
                                    "Undress Rogue":
                                            call R_Undress   
                                    "Clean up Rogue (locked)" if not R_Spunk:
                                            pass  
                                    "Clean up Rogue" if R_Spunk:
                                            call Rogue_Cleanup("ask")                                         
                                    "Never mind":
                                            jump RFA_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call R_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump RFA_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call R_Pos_Reset
                                    $ Line = 0
                                    jump RFA_After
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
                            if 100 > R_Lust >= 70 and R_OCount < 2 and R_SEXP >= 20:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump RFA_After 
                            $ Line = "came"
     
                    if R_Lust >= 100:  
                            #If Rogue can cum                                             
                            call R_Cumming
                            if Situation == "shift" or "angry" in R_RecentActions:
                                jump RFA_After
                       
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
                                        jump RFA_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Rogue")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
                    
        if R_SEXP >= 100 or ApprovalCheck("Rogue", 1200, "LO"):
            pass
        elif Cnt == (5 + R_FondleA):
                    $ R_Brows = "confused"
                    ch_r "Uh, that's nice, but. . ."  
        elif R_Lust >= 80:
                    pass
        elif Cnt == (15 + R_FondleA) and R_SEXP >= 15 and not ApprovalCheck("Rogue", 1500):
                    $ R_Brows = "confused"        
                    menu:
                        ch_r "[R_Petname], this is nice, but could we do something else?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump RFA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump RFA_After
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
                                    jump RFA_After
        #End Count check
        
        call Escalation("Rogue","R") #sees if she wants to escalate things
        
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0)
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
    
label RFA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call R_Pos_Reset
        
    call RogueFace("sexy") 
    
    $ R_FondleA += 1  
    $ R_Action -=1            
    if R_Legs != "pants" or R_Upskirt:        
        $ R_Addictionrate += 1
        if "addictive" in P_Traits:
            $ R_Addictionrate += 1
    
        call Partner_Like("Rogue",2)
     
    if R_FondleA == 1:            
            $ R_SEXP += 4         
            if not Situation: 
                if R_Love >= 500 and "unsatisfied" not in R_RecentActions:
                    ch_r "That was. . . nice. . ."
                elif R_Obed <= 500 and P_Focus <= 20:
                    call RogueFace("perplexed", 1)
                    ch_r "Did you like that?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_r "Mmm, so what else did you have in mind?"
    call Checkout    
    return   


# end R_Fondle Ass /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Ass    
label R_Insert_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Rogue")
    if R_InsertA: #You've done it before
        $ Tempmod += 25
    if R_Legs == "pants" or HoseNum("Rogue") >= 5: # she's got pants on.
        $ Tempmod -= 15    
    if R_Lust > 85 and R_Loose: #She's really horny
        $ Tempmod += 15
    if R_Lust > 95 and R_Loose:
        $ Tempmod += 5
    if Situation == "shift":
        $ Tempmod += 10
    if R_Lust > 85 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in R_Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 25 
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount
    
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no insert ass" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no insert ass" in R_RecentActions else 0   
            
    $ Approval = ApprovalCheck("Rogue", 1300, TabM = 3) # 130, 145, 160, Taboo -120(250)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            call RogueFace("surprised")
            call Statup("Rogue", "Obed", 90, 2)
            call Statup("Rogue", "Obed", 70, 2)
            call Statup("Rogue", "Inbt", 80, 2) 
            call Statup("Rogue", "Inbt", 30, 2) 
            "As you slide a finger in, Rogue tightens around it in surprise, but seems into it."  
            call RogueFace("sexy")           
            jump RIA_Prep
        else:   
            call RogueFace("surprised")
            call Statup("Rogue", "Love", 80, -2)
            call Statup("Rogue", "Obed", 50, -3)
            ch_r "Keep it out of there, [R_Petname]."                 
            $ Tempmod = 0
            $ Trigger2 = 0
            return          
    
    if "insert ass" in R_DailyActions and not R_Loose:
        call RogueFace("bemused", 1)
        ch_r "I'm still a little sore from earlier, [R_Petname]."
    elif "insert ass" in R_DailyActions:
        call RogueFace("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so hard this time though.",
            "Mmm. . ."]) 
        ch_r "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .               
        if R_Forced:
            call RogueFace("sad")
            call Statup("Rogue", "Love", 70, -3, 1)
            call Statup("Rogue", "Love", 20, -2, 1)
            call Statup("Rogue", "Obed", 90, 1)
            call Statup("Rogue", "Inbt", 60, 1)
            ch_r "Sure, get in there."    
        else:
            call RogueFace("sexy", 1)
            $ R_Eyes = "closed"            
            call Statup("Rogue", "Love", 90, 1)
            call Statup("Rogue", "Inbt", 50, 3)            
            call Statup("Rogue", "Lust", 200, 3)
            ch_r "Oooooooh. . ."                
        call Statup("Rogue", "Obed", 20, 1)
        call Statup("Rogue", "Obed", 60, 1)
        call Statup("Rogue", "Inbt", 70, 2) 
        jump RIA_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call RogueFace("angry", 1)
        if "no insert ass" in R_RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions and "no insert ass" in R_DailyActions:  
            ch_r "I told you that wasn't appropriate!" 
        elif "no insert ass" in R_DailyActions:       
            ch_r "I already told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions:  
            ch_r "I told you not in public!"  
        elif not R_InsertA:
            call RogueFace("perplexed", 1)
            ch_r "I. . . don't think that's. . ."
        else:
            call RogueFace("bemused")
            ch_r "Oh, um, no, I'm not really comfortable with that. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no insert ass" in R_DailyActions:
                call RogueFace("bemused")
                ch_r "Yeah, ok, [R_Petname]."              
                return
            "Maybe later?" if "no insert ass" not in R_DailyActions:
                call RogueFace("sexy")  
                ch_r "It's. . . possible, [R_Petname]."
                call Statup("Rogue", "Love", 80, 2)
                call Statup("Rogue", "Inbt", 70, 2)   
                if Taboo:                    
                    $ R_RecentActions.append("tabno")                      
                    $ R_DailyActions.append("tabno") 
                $ R_RecentActions.append("no insert ass")                      
                $ R_DailyActions.append("no insert ass")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    call RogueFace("sexy")           
                    call Statup("Rogue", "Obed", 90, 2)
                    call Statup("Rogue", "Obed", 50, 2)
                    ch_r "Ok, you're probably right. . ."      
                    call Statup("Rogue", "Inbt", 70, 3) 
                    call Statup("Rogue", "Inbt", 40, 2)
                    jump RIA_Prep
                else:   
                    call RogueFace("bemused") 
                    ch_r "I really don't think that I would."     
            
            "[[Slide a finger in anyway]":                                               # Pressured into being fingered. 
                $ Approval = ApprovalCheck("Rogue", 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                if Approval > 1 or (Approval and R_Forced):                    
                    call RogueFace("surprised", 1)
                    call Statup("Rogue", "Love", 70, -5, 1)
                    call Statup("Rogue", "Love", 200, -2)                 
                    ch_r "Oh. . . well, ok then. . ."                     
                    call RogueFace("sad")
                    call Statup("Rogue", "Obed", 50, 4)
                    call Statup("Rogue", "Inbt", 80, 1) 
                    call Statup("Rogue", "Inbt", 60, 3)  
                    if Approval < 2:                          
                        $ R_Forced = 1
                    jump RIA_Prep
                else:                              
                    call Statup("Rogue", "Love", 200, -15)  
                    call RogueFace("angry", 1)
                    "She slaps your hand away."   
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")   
                    
    if "no insert ass" in R_DailyActions:
        ch_r "Learn to take \"no\" for an answer, [R_Petname]."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1)
        ch_r "Um, no way."
        if R_Inbt > 50:
                call Statup("Rogue", "Lust", 80, 10)  
        else:
                call Statup("Rogue", "Lust", 50, 3)
        call Statup("Rogue", "Obed", 50, -2)      
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:
        call RogueFace("angry", 1)    
        $ R_RecentActions.append("tabno")                   
        $ R_DailyActions.append("tabno") 
        ch_r "[R_Petname]! This just really isn't the time or place!"                   
    elif R_InsertA:
        call RogueFace("sad") 
        ch_r "I think you should keep your fingers to yourself."    
    else:
        call RogueFace("surprised")
        ch_r "I. . . not there!!"
        call RogueFace
    $ R_RecentActions.append("no insert ass")                      
    $ R_DailyActions.append("no insert ass") 
    $ Tempmod = 0    
    return
    
        
label RIA_Prep: #Animation set-up 
label R_IA_Prep: #Animation set-up 
    if Trigger2 == "insert ass":
        return
            
    call R_Pussy_Launch("insert ass")
        
    if Situation == "Rogue":                                                         
            #Rogue auto-starts    
            $ Situation = 0
            if (R_Legs and not R_Upskirt) or (R_Panties and not R_PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck("Rogue", 1250, TabM = 1) or (R_SeenPussy and ApprovalCheck("Rogue", 500) and not Taboo):
                        $ R_Upskirt = 1
                        $ R_PantiesDown = 1
                        $ Line = 0
                        if R_Legs == "skirt":
                            $ Line = "Rogue hikes up her skirt"
                        elif PantsNum("Rogue") >= 5:
                            $ Line = "Rogue pulls down her " + R_Legs
                        else:
                            $ Line = 0                            
                        if R_Panties:
                            if Line:
                                #wearing pants
                                "[Line] and pulls her [R_Panties] out of the way."
                                "She then grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
                            else:
                                #no pants
                                "She pulls her [R_Panties] out of the way, and then presses your hand against her asshole."
                                "She clearly intends for you to get to work." 
                        else:
                            #pants but no panties
                            "[Line], and then presses your hand against her asshole."
                            "She clearly intends for you to get to work."                     
                        call Rogue_First_Bottomless(1)
                else:
                    "Rogue grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
            else:
                "Rogue grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":                    
                    call Statup("Rogue", "Inbt", 80, 3) 
                    call Statup("Rogue", "Inbt", 50, 2)
                    "You press your finger into it."
                "Praise her.":       
                    call RogueFace("sexy", 1)                    
                    call Statup("Rogue", "Inbt", 80, 3) 
                    ch_p "Dirty girl, [R_Pet]."
                    call Rogue_Namecheck
                    "You press your finger into it."
                    call Statup("Rogue", "Love", 85, 1)
                    call Statup("Rogue", "Obed", 90, 1)
                    call Statup("Rogue", "Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your hand back."
                    call RogueFace("surprised")       
                    call Statup("Rogue", "Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [R_Pet]."
                    call Rogue_Namecheck
                    "Rogue pulls back."
                    call Statup("Rogue", "Obed", 90, 1)
                    call Statup("Rogue", "Obed", 50, 1)
                    call Statup("Rogue", "Obed", 30, 2)
                    $ P_RecentActions.append("nope")      
                    call AnyWord("Rogue",1,"refused","refused")  
                    return          
            #end auto
          
    if not R_Forced and Situation != "auto":
        $ Tempmod = 0
        call Rogue_Bottoms_Off
        if "angry" in R_RecentActions:
            return    
            
    $ Tempmod = 0    
    if not R_InsertA:        
        if R_Forced:
            call Statup("Rogue", "Love", 90, -50)
            call Statup("Rogue", "Obed", 70, 60)
            call Statup("Rogue", "Inbt", 80, 35) 
        else:
            call Statup("Rogue", "Love", 90, 10)
            call Statup("Rogue", "Obed", 70, 20)
            call Statup("Rogue", "Inbt", 80, 25)
            
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
    call DrainWord("Rogue","no insert ass")
    $ R_RecentActions.append("insert ass")                      
    $ R_DailyActions.append("insert ass") 
    
label RIA_Cycle: #Repeating strokes 
    while Round >=0:  
        call Shift_Focus("Rogue") 
        call R_Pussy_Launch("insert ass")
        call RogueLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                                              
                        "Slap her ass":                     
                                    call R_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump RIA_Cycle  
                                    
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
                                                        "Pull out and start rubbing again.":
                                                                $ Situation = "pullback"
                                                                call RIA_After
                                                                call R_Fondle_Ass
                                                        "I want to lick your asshole.":
                                                                $ Situation = "shift"
                                                                call RIA_After
                                                                call R_Lick_Ass                 
                                                        "Just start licking.":
                                                                $ Situation = "auto"
                                                                call RIA_After
                                                                call R_Lick_Ass    
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call RIA_After
                                                                call R_Dildo_Ass  
                                                        "Never Mind":
                                                                jump RIA_Cycle
                                            else: 
                                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"           
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call RIA_After
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
                                                        jump RIA_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump RIA_Cycle 
                                            "Never mind":
                                                        jump RIA_Cycle 
                                    "Undress Rogue":
                                            call R_Undress   
                                    "Clean up Rogue (locked)" if not R_Spunk:
                                            pass  
                                    "Clean up Rogue" if R_Spunk:
                                            call Rogue_Cleanup("ask")                                         
                                    "Never mind":
                                            jump RIA_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call R_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump RIA_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call R_Pos_Reset
                                    $ Line = 0
                                    jump RIA_After
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
                                jump RIA_After 
                            $ Line = "came"
     
                    if R_Lust >= 100:  
                            #If Rogue can cum                                             
                            call R_Cumming
                            if Situation == "shift" or "angry" in R_RecentActions:
                                jump RIA_After
                       
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
                                        jump RIA_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Rogue")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if R_SEXP >= 100 or ApprovalCheck("Rogue", 1200, "LO"):
            pass
        elif Cnt == (5 + R_InsertA):
                    $ R_Brows = "confused"
                    ch_r "What are you even doing down there?" 
        elif R_Lust >= 80:
                    pass
        elif Cnt == (15 + R_InsertA) and R_SEXP >= 15 and not ApprovalCheck("Rogue", 1500):
                    $ R_Brows = "confused"        
                    menu:
                        ch_r "[R_Petname], this is getting uncomfortable, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump RIA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump RIA_After
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
                                    jump RIA_After
        #End Count check
           
        call Escalation("Rogue","R") #sees if she wants to escalate things
        
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0)
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
    
label RIA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call R_Pos_Reset
        
    call RogueFace("sexy") 
    
    $ R_InsertA += 1  
    $ R_Action -=1            
    $ R_Addictionrate += 1
    if "addictive" in P_Traits:
        $ R_Addictionrate += 1
        
    call Partner_Like("Rogue",2)
     
    if R_InsertA == 1:            
            $ R_SEXP += 12         
            if not Situation: 
                if R_Love >= 500 and "unsatisfied" not in R_RecentActions:
                    ch_r "That felt. . . interesting. . ."
                elif R_Obed <= 500 and P_Focus <= 20:
                    call RogueFace("perplexed", 1)
                    ch_r "Did you like that?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_r "Mmm, so what else did you have in mind?"
    call Checkout
    return   


# end R_Insert Ass /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Ass    
label R_Lick_Ass: 
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Rogue")
                                                                             # Will she let you lick? Modifiers         
    if R_LickA: #You've done it before
        $ Tempmod += 20
    if R_Legs == "pants" or HoseNum("Rogue") >= 5: # she's got pants on.
        $ Tempmod -= 25 
    if R_Lust > 95:
        $ Tempmod += 20  
    elif R_Lust > 85: #She's really horny
        $ Tempmod += 15    
    if R_Lust > 85 and Situation == "auto": #auto
        $ Tempmod += 10 
    if Situation == "shift":
        $ Tempmod += 10
    if "exhibitionist" in R_Traits:
        $ Tempmod += (4*Taboo) 
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 25  
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount 
    
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no lick ass" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no lick ass" in R_RecentActions else 0   
            
    $ Approval = ApprovalCheck("Rogue", 1550, TabM = 4) # 155, 170, 185, Taboo -160(315)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            call RogueFace("surprised")   
            call Statup("Rogue", "Obed", 90, 1)
            call Statup("Rogue", "Inbt", 80, 3) 
            call Statup("Rogue", "Inbt", 40, 2) 
            "As you crouch down and start to lick her asshole, Rogue startles briefly, but then begins to melt."  
            call RogueFace("sexy")  
            jump RLA_Prep
        else:   
            call RogueFace("surprised")
            call Statup("Rogue", "Love", 80, -2)
            call Statup("Rogue", "Obed", 50, -3)
            ch_r "Um, no, I'm not really. . . don't."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return  
    
    if "lick ass" in R_RecentActions:
        call RogueFace("sexy", 1)
        ch_r "Mmm, again? Ok."
        jump RLA_Prep
    elif "lick ass" in R_DailyActions:
        call RogueFace("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "I'm still tingling a bit from earlier.",
            "Mmm. . ."]) 
        ch_r "[Line]"
    
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if R_Forced:
            call RogueFace("sad")
            call Statup("Rogue", "Love", 70, -3, 1)
            call Statup("Rogue", "Love", 20, -2, 1)
            call Statup("Rogue", "Obed", 90, 2)
            call Statup("Rogue", "Inbt", 60, 2)
            ch_r "Sure, get in there."    
        else:
            call RogueFace("sexy", 1)
            $ R_Eyes = "closed"            
            call Statup("Rogue", "Love", 90, 1)
            call Statup("Rogue", "Inbt", 60, 2)            
            call Statup("Rogue", "Lust", 200, 3)
            ch_r "Oooooooh. . ."                
        call Statup("Rogue", "Obed", 20, 1)
        call Statup("Rogue", "Obed", 60, 1)
        call Statup("Rogue", "Inbt", 80, 2) 
        jump RLA_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .           
        call RogueFace("angry", 1)
        if "no lick ass" in R_RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions and "no lick ass" in R_DailyActions:  
            ch_r "I told you not to touch me like that in public!" 
        elif "no lick ass" in R_DailyActions:       
            ch_r "I already told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions:  
            ch_r "I told you not in public!"  
        elif not R_LickA:                    #First time dialog
            call RogueFace("bemused", 1)
            if R_Love >= R_Obed and R_Love >= R_Inbt:            
                ch_r "I'm not really sure I want you lick'in down there. . ."
            elif R_Obed >= R_Inbt:            
                ch_r "You really don't have to if you don't want to."
            else:
                $ R_Eyes = "sexy"
                ch_r "Hmm. . . it's worth a shot. . ."
        else:
            call RogueFace("bemused")
            ch_r "Not now, [R_Petname]."  
        menu:
            extend ""
            "Sorry, never mind." if "no lick ass" in R_DailyActions:
                call RogueFace("bemused")
                ch_r "Yeah, ok, [R_Petname]."              
                return
            "I'm sure I can convince you later. . ." if "no lick ass" not in R_DailyActions:
                call RogueFace("sexy")  
                ch_r "Anything's possible, [R_Petname]."
                call Statup("Rogue", "Love", 80, 2)
                call Statup("Rogue", "Inbt", 70, 2)   
                if Taboo:                    
                    $ R_RecentActions.append("tabno")                      
                    $ R_DailyActions.append("tabno") 
                $ R_RecentActions.append("no lick ass")                      
                $ R_DailyActions.append("no lick ass")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    call RogueFace("sexy")           
                    call Statup("Rogue", "Obed", 90, 2)
                    call Statup("Rogue", "Obed", 50, 2)
                    ch_r "Ok, you're probably right. . ."      
                    call Statup("Rogue", "Inbt", 70, 3) 
                    call Statup("Rogue", "Inbt", 40, 2)
                    jump RLA_Prep
                else:   
                    call RogueFace("sexy") 
                    ch_r "Tsk, not this time, [R_Petname], that just seems. . . dirty."        
            
            "[[Start licking anyway]":                                               # Pressured into being licked. 
                $ Approval = ApprovalCheck("Rogue", 1100, "OI", TabM = 4) # 110, 125, 140, -160(270)
                if Approval > 1 or (Approval and R_Forced):
                    call RogueFace("sad")
                    call Statup("Rogue", "Love", 70, -5, 1)
                    call Statup("Rogue", "Love", 200, -2)                 
                    ch_r "Ok, get in there if you're so determined."  
                    call Statup("Rogue", "Obed", 50, 4)
                    call Statup("Rogue", "Inbt", 80, 1) 
                    call Statup("Rogue", "Inbt", 60, 3)  
                    if Approval < 2:                          
                        $ R_Forced = 1
                    jump RLA_Prep
                else:                              
                    call Statup("Rogue", "Love", 200, -15)  
                    call RogueFace("angry", 1)
                    "She shoves your head back."   
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")   
                    
    if "no lick ass" in R_DailyActions:
        ch_r "Learn to take \"no\" for an answer, [R_Petname]."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1)
        ch_r "Ew, no way."
        if R_Inbt > 50:
                call Statup("Rogue", "Lust", 80, 10)  
        else:
                call Statup("Rogue", "Lust", 50, 3)
        call Statup("Rogue", "Obed", 50, -2)   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:
        call RogueFace("angry", 1)    
        $ R_RecentActions.append("tabno")                   
        $ R_DailyActions.append("tabno") 
        ch_r "This just really isn't the time or place, [R_Petname]!"                   
    elif R_LickP:
        call RogueFace("sad") 
        ch_r "Sorry, keep your tongue in your mouth."    
    else:
        call RogueFace("surprised")
        ch_r "What?! Gross!"
        call RogueFace
    $ R_RecentActions.append("no lick ass")                      
    $ R_DailyActions.append("no lick ass") 
    $ Tempmod = 0    
    return
        
label RLA_Prep: #Animation set-up  
    if Trigger2 == "lick ass":
        return
    if not R_Forced and Situation != "auto":
        $ Tempmod = 0
        if R_Legs == "pants":
            $ Tempmod = 15
        call Rogue_Bottoms_Off
        if "angry" in R_RecentActions:
            return    
    $ Tempmod = 0  
    call R_Pussy_Launch("lick ass")
    if not R_LickA:        
        if R_Forced:
            call Statup("Rogue", "Love", 90, -30)
            call Statup("Rogue", "Obed", 70, 40)
            call Statup("Rogue", "Inbt", 80, 80) 
        else:
            call Statup("Rogue", "Love", 90, 35)
            call Statup("Rogue", "Obed", 70, 25)
            call Statup("Rogue", "Inbt", 80, 55)
    if Taboo:
        $ R_Inbt += int(Taboo/10)  
        $ R_Lust += int(Taboo/5)
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    
    $ R_Upskirt = 1
    if R_Legs == "skirt":
        $ R_SeenPanties = 1
    call Rogue_First_Bottomless(1)
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Rogue","tabno")
    call DrainWord("Rogue","no lick ass")
    
    $ R_RecentActions.append("lick") if "lick" not in R_RecentActions else R_RecentActions
    $ R_RecentActions.append("ass") if "ass" not in R_RecentActions else R_RecentActions
    $ R_RecentActions.append("lick ass")  
    
    $ R_DailyActions.append("lick") if "lick" not in R_DailyActions else R_RecentActions
    $ R_DailyActions.append("ass") if "ass" not in R_DailyActions else R_RecentActions                    
    $ R_DailyActions.append("lick ass")  
label RLA_Cycle: #Repeating strokes
    if Trigger2 == "kiss you":
            $ Trigger2 = 0
    while Round >=0:  
        call Shift_Focus("Rogue") 
        call R_Pussy_Launch("lick ass")
        call RogueLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                                              
                        "Slap her ass":                     
                                    call R_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump RLA_Cycle  
                                    
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
                                                        "Switch to fondling.":
                                                                $ Situation = "pullback"
                                                                call RLA_After
                                                                call R_Fondle_Ass
                                                        "I want to stick a finger in.":
                                                                $ Situation = "shift"
                                                                call RLA_After
                                                                call R_Insert_Ass                 
                                                        "Just stick a finger in [[without asking].":
                                                                $ Situation = "auto"
                                                                call RLA_After
                                                                call R_Insert_Ass                        
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call RLA_After
                                                                call R_Dildo_Ass  
                                                        "Never Mind":
                                                                jump RLA_Cycle
                                            else: 
                                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"           
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call RLA_After
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
                                                        jump RLA_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump RLA_Cycle 
                                            "Never mind":
                                                        jump RLA_Cycle 
                                    "Undress Rogue":
                                            call R_Undress   
                                    "Clean up Rogue (locked)" if not R_Spunk:
                                            pass  
                                    "Clean up Rogue" if R_Spunk:
                                            call Rogue_Cleanup("ask")                                         
                                    "Never mind":
                                            jump RLA_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call R_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump RLA_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call R_Pos_Reset
                                    $ Line = 0
                                    jump RLA_After
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
                                jump RLA_After 
                            $ Line = "came"
     
                    if R_Lust >= 100:  
                            #If Rogue can cum                                             
                            call R_Cumming
                            if Situation == "shift" or "angry" in R_RecentActions:
                                jump RLA_After
                       
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
                                        jump RLA_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Rogue")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
                    
        if R_SEXP >= 100 or ApprovalCheck("Rogue", 1200, "LO"):
            pass
        elif Cnt == (5 + R_LickA):
                    $ R_Brows = "confused"
                    ch_r "What are you even doing down there?"  
        elif R_Lust >= 80:
                    pass
        elif Cnt == (15 + R_LickA) and R_SEXP >= 15 and not ApprovalCheck("Rogue", 1500):
                    $ R_Brows = "confused"        
                    menu:
                        ch_r "[R_Petname], this is getting uncomfortable, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump RLA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump RLA_After
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
                                    jump RLA_After
        #End Count check
           
        call Escalation("Rogue","R") #sees if she wants to escalate things
        
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0)
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
    
label RLA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call R_Pos_Reset
        
    call RogueFace("sexy") 
    
    $ R_LickA += 1  
    $ R_Action -=1      
    if R_Legs != "pants" or R_Upskirt:        
        $ R_Addictionrate += 1
        if "addictive" in P_Traits:
            $ R_Addictionrate += 1
            
    call Partner_Like("Rogue",2)
                 
    if R_LickA == 1:            
            $ R_SEXP += 15         
            if not Situation: 
                if R_Love >= 500 and "unsatisfied" not in R_RecentActions:
                    ch_r "Was. . . that something you liked?"
                elif R_Obed <= 500 and P_Focus <= 20:
                    call RogueFace("perplexed", 1)
                    ch_r "Did you like that?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_r "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# end R_Lick Ass /////////////////////////////////////////////////////////////////////////////

