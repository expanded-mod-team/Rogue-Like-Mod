# L_Massage /////////////////////////////////////////////////////////////////////////////
label L_Massage:
    call Shift_Focus("Laura")
    $ Tempmod = 0    
    
    $ Approval = ApprovalCheck("Laura", 500, TabM = 2) # 95, 110, 125 -120(215)
    
    if Approval >= 2:             
        call LauraFace("bemused", 1)
        if L_Forced:
                call LauraFace("sad")
                call Statup("Laura", "Love", 20, -2, 1)
                call Statup("Laura", "Obed", 90, 1)
                call Statup("Laura", "Inbt", 60, 1)
        ch_l "I guess I could use a rubdown."   
        call Statup("Laura", "Love", 90, 1)
        call Statup("Laura", "Inbt", 50, 3) 
        jump L_Massage_Prep
        
    else:
        call LauraFace("angry", 1)
        if "no massage" in L_RecentActions:  
            ch_l "I only {i}just{/i} refused you, [L_Petname]."
        elif "no massage" in L_DailyActions:       
            ch_l "I told you \"no\" earlier, [L_Petname]."
        else:
            call LauraFace("bemused")
            ch_l "I'm not interested at the moment, [L_Petname]."   
        menu:
            extend ""
            "Sorry, never mind." if "no massage" in L_DailyActions:
                call LauraFace("bemused")
                ch_l "No worries."              
                return
            "Maybe later?" if "no massage" not in L_DailyActions:
                call LauraFace("sexy")  
                ch_l "Maybe?"
                call Statup("Laura", "Love", 80, 1)
                call Statup("Laura", "Inbt", 20, 1)
                call Statup("Laura", "Obed", 20, 1)  
                $ L_RecentActions.append("no massage")                      
                $ L_DailyActions.append("no massage")            
                return                
            "Come on, Please?":             
                if Approval:
                    call LauraFace("sexy")     
                    call Statup("Laura", "Obed", 90, 1)
                    call Statup("Laura", "Obed", 40, 2)
                    call Statup("Laura", "Inbt", 30, 2)
                    ch_l "I do have some tension built up. . ."                
                    jump L_Massage_Prep
                else:   
                    call LauraFace("sly", Brows="confused") 
                    ch_l "No." 
    
    if "no massage" in L_DailyActions:
        ch_l "I've made myself clear on this, [L_Petname]."   
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif L_Forced:
        call LauraFace("angry", 1)
        ch_l "You'll have to keep your hands limber for yourself."
        call Statup("Laura", "Lust", 60, 5)    
        call Statup("Laura", "Obed", 50, -2)   
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif Taboo:
        call LauraFace("angry", 1)    
        ch_l "I try to stay off the radar."                  
    else:
        call LauraFace("sexy") 
        $ L_Mouth = "sad"
        ch_l "I really can't."    
    $ L_RecentActions.append("no massage")                      
    $ L_DailyActions.append("no massage") 
    $ Tempmod = 0    
    return

label L_Massage_Prep:
    call Laura_Top_Off("massage")
    if "angry" in L_RecentActions:
        return    
    
label L_Massage_Cycle: 
    $ L_RecentActions.append("massage")                      
    $ L_DailyActions.append("massage") 
        
    "You massage her back and shoulders."
    if not L_Over:
        $ L_Addict -= D20 if L_Addict > D20 else L_Addict
    
    $ D20 = renpy.random.randint(10, 20)
    $ Round -= D20 if Round > D20 else (Round-1)
            
    ch_l "That was very. . . pleasant, [L_Petname]"
    if "massage" not in L_RecentActions:        
        call Statup("Laura", "Love", 90, 1)
        call Statup("Laura", "Love", 50, 2)
        call Statup("Laura", "Obed", 30, 2)
    return

# end L_Massage /////////////////////////////////////////////////////////////////////////////

# L_Fondle /////////////////////////////////////////////////////////////////////////////
label L_Fondle:
    
    $ L_Mouth = "smile"
    if not L_Action:
        ch_l "I'm rather tired right now, [L_Petname], raincheck?"
        return
    menu:
        ch_l "Well? Where did you want to touch, [L_Petname]?"
        "Your breasts?" if L_Action:
                jump L_Fondle_Breasts
        "Your thighs?" if L_Action:
                jump L_Fondle_Thighs
        "Your pussy?" if L_Action:
                jump L_Fondle_Pussy
        "Your Ass?" if L_Action:
                jump L_Fondle_Ass
        "Never mind.":
                return
    return


# L_Fondle Breasts /////////////////////////////////////////////////////////////////////////////
label L_Fondle_Breasts:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
    
    # Will she let you fondle? Modifiers
    if L_FondleB: #You've done it before
        $ Tempmod += 15
    if L_Lust > 75: #She's really horny
        $ Tempmod += 20
    if "exhibitionist" in L_Traits:
        $ Tempmod += (3*Taboo)
    if "dating" in L_Traits or "sex friend" in L_Petnames:
        $ Tempmod += 10
    elif "ex" in L_Traits:
        $ Tempmod -= 20
    if L_ForcedCount and not L_Forced:
        $ Tempmod -= 5 * L_ForcedCount
    
    if Taboo and "tabno" in L_DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in L_History:                   
        $ Tempmod -= 20 
        
    if "no fondle breasts" in L_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle breasts" in L_RecentActions else 0        
        
    $ Approval = ApprovalCheck("Laura", 950, TabM = 3) # 95, 110, 125 -120(215)
    
    if Situation == "auto":  
        if Approval:
            call LauraFace("sexy")       
            call Statup("Laura", "Obed", 90, 1)
            call Statup("Laura", "Obed", 70, 2)
            call Statup("Laura", "Inbt", 70, 3)
            call Statup("Laura", "Inbt", 30, 2)            
            "As you cup her breast, Laura gently nods."            
            jump L_FB_Prep        
        else:   
            call LauraFace("surprised")
            $ L_Brows = "confused"
            call Statup("Laura", "Obed", 50, -2)
            ch_l "Roll it back, [L_Petname]. . ."
            $ Tempmod = 0
            $ Trigger2 = 0
            return
                    
    # fondle yes:    
    
    if Approval:                                                                       #Second time+ dialog        
        call LauraFace("sexy", 1)
        if L_Forced: 
            call LauraFace("sad")
            call Statup("Laura", "Love", 70, -3, 1)
            call Statup("Laura", "Love", 20, -2, 1)           
        elif not Taboo and "tabno" in L_DailyActions:        
            ch_l "This does seem less. . . exposed."   
            
    if "fondle breasts" in L_RecentActions:
        call LauraFace("sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump L_FB_Prep
    elif "fondle breasts" in L_DailyActions:
        call LauraFace("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Chill. . .",
            "Mmm. . ."]) 
        ch_l "[Line]"
            
    if Approval >= 2:             
        call LauraFace("bemused", 1)
        if L_Forced:
            call LauraFace("sad")
            call Statup("Laura", "Love", 70, -3, 1)
            call Statup("Laura", "Love", 20, -2, 1)
            call Statup("Laura", "Obed", 90, 1)
            call Statup("Laura", "Inbt", 60, 1)
        ch_l "Sure, sounds fun."   
        call Statup("Laura", "Love", 90, 1)
        call Statup("Laura", "Inbt", 50, 3) 
        jump L_FB_Prep
        
    else:
        call LauraFace("angry", 1)
        if "no fondle breasts" in L_RecentActions:  
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "tabno" in L_DailyActions and "no fondle breasts" in L_DailyActions:  
            ch_l "I've had enough of this today." 
        elif "no fondle breasts" in L_DailyActions:       
            ch_l "Don't make me tell you again today."
        elif Taboo and "tabno" in L_DailyActions:  
            ch_l "I told you, not here, [L_Petname]."  
        elif not L_FondleB:
            call LauraFace("bemused")
            ch_l "Look, I don't know if we're ready for that, [L_Petname]. . ."
        else:
            call LauraFace("bemused")
            ch_l "Keep dreaming."   
        menu:
            extend ""
            "Sorry, never mind." if "no fondle breasts" in L_DailyActions:
                call LauraFace("bemused")
                ch_l "No worries."              
                return
            "Maybe later?" if "no fondle breasts" not in L_DailyActions:
                call LauraFace("sexy")  
                ch_l "Eh. Maybe."
                call Statup("Laura", "Love", 80, 1)
                call Statup("Laura", "Love", 50, 1)
                call Statup("Laura", "Inbt", 30, 2)    
                if Taboo:                    
                    $ L_RecentActions.append("tabno")                      
                    $ L_DailyActions.append("tabno") 
                $ L_RecentActions.append("no fondle breasts")                      
                $ L_DailyActions.append("no fondle breasts")            
                return                
            "Come on, Please?":             
                if Approval:
                    call LauraFace("sexy")     
                    call Statup("Laura", "Obed", 50, 2)
                    call Statup("Laura", "Inbt", 60, 3)
                    call Statup("Laura", "Inbt", 30, 2)
                    ch_l "Well if you're going to be a little bitch about it. . ."                
                    jump L_FB_Prep
                else:   
                    call LauraFace("sexy") 
                    ch_l "Well if you're going to be a little bitch about it. . ."
            
            
            "[[Grab her chest anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Laura", 350, "OI", TabM = 3) # 35, 50, 65
                if Approval > 1 or (Approval and L_Forced):
                    call LauraFace("sad")
                    call Statup("Laura", "Love", 70, -5, 1)
                    call Statup("Laura", "Love", 20, -2, 1)                 
                    ch_l "Hey. . ."
                    ch_l "Eh, whatever. . ."
                    call Statup("Laura", "Obed", 90, 2)
                    call Statup("Laura", "Obed", 50, 4)
                    call Statup("Laura", "Inbt", 60, 3)   
                    if Approval < 2:                          
                        $ L_Forced = 1
                    jump L_FB_Prep
                else:                              
                    call Statup("Laura", "Love", 200, -10)  
                    call LauraFace("angry", 1)
                    "She slaps your hand away."   
                    $ L_RecentActions.append("angry")
                    $ L_DailyActions.append("angry")   
    
    if "no fondle breasts" in L_DailyActions:
        ch_l "Listen to the words that are coming out of my mouth."   
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif L_Forced:
        call LauraFace("angry", 1)
        ch_l "No."
        call Statup("Laura", "Lust", 60, 5)    
        call Statup("Laura", "Obed", 50, -2)   
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif Taboo:
        call LauraFace("angry", 1)    
        $ L_RecentActions.append("tabno")                   
        $ L_DailyActions.append("tabno") 
        ch_l "I try to stay off the radar."                   
    elif L_FondleB:
        call LauraFace("sad")
        ch_l "You'll have to earn that back."        
    else:
        call LauraFace("sexy") 
        $ L_Mouth = "sad"
        ch_l "No."    
    $ L_RecentActions.append("no fondle breasts")                      
    $ L_DailyActions.append("no fondle breasts") 
    $ Tempmod = 0   
    return 
            
   
label L_FB_Prep: #Animation set-up 
    if Trigger == "kiss you": 
        $ Trigger = "fondle breasts" 
        return
        
    if Trigger2 == "fondle breasts": 
        return
    
    if not L_Forced and Situation != "auto":
        $ Tempmod = 0
        call Laura_Top_Off
        if "angry" in L_RecentActions:
            return
        
    $ Tempmod = 0  
    call L_Breasts_Launch("fondle breasts")
    if not L_FondleB:        
        if L_Forced:
            call Statup("Laura", "Love", 90, -20)
            call Statup("Laura", "Obed", 70, 25)
            call Statup("Laura", "Inbt", 80, 15) 
        else:
            call Statup("Laura", "Love", 90, 10)
            call Statup("Laura", "Obed", 70, 5)
            call Statup("Laura", "Inbt", 80, 15) 
            
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
    call DrainWord("Laura","no fondle breasts")
    $ L_RecentActions.append("fondle breasts")                      
    $ L_DailyActions.append("fondle breasts") 
    
label L_FB_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Laura") 
        call L_Breasts_Launch("fondle breasts")
        call LauraLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                         
                        "Slap her ass":                     
                                    call L_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump L_FB_Cycle  
                                    
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
                                                        "Ask to suck on them.":
                                                                if L_Action and MultiAction:                        
                                                                    $ Situation = "shift"
                                                                    call L_FB_After
                                                                    call L_Suck_Breasts
                                                                else:
                                                                    ch_l "Maybe we could finish this up for now?"
                                                        "Just suck on them without asking.":
                                                                if L_Action and MultiAction:                            
                                                                    $ Situation = "auto"
                                                                    call L_FB_After
                                                                    call L_Suck_Breasts
                                                                else:
                                                                    "As you lean in to suck on her breast, she grabs your head and pushes back."
                                                                    ch_l "Maybe we could finish this up for now?"
                                                        "Never Mind":
                                                                jump L_FB_Cycle
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
                                                        jump L_FB_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump L_FB_Cycle 
                                            "Never mind":
                                                        jump L_FB_Cycle 
                                    "Undress Laura":
                                            call L_Undress   
                                    "Clean up Laura (locked)" if not L_Spunk:
                                            pass  
                                    "Clean up Laura" if L_Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump L_FB_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call L_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump L_FB_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call L_Pos_Reset
                                    $ Line = 0
                                    jump L_FB_After
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
                                call L_Pos_Reset
                                return    
                            call Statup("Laura", "Lust", 200, 5) 
                            if 100 > L_Lust >= 70 and L_OCount < 2:             
                                $ L_RecentActions.append("unsatisfied")                      
                                $ L_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump L_FB_After 
                            $ Line = "came"
     
                    if L_Lust >= 100:  
                            #If Laura can cum                                             
                            call L_Cumming
                            if Situation == "shift" or "angry" in L_RecentActions:
                                jump L_FB_After
                       
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
                                        jump L_FB_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if L_SEXP >= 100 or ApprovalCheck("Laura", 1200, "LO"):
            pass
        elif Cnt == (5 + L_FondleB):
                    $ L_Brows = "confused"
                    ch_l "Enjoying yourself?" 
        elif L_Lust >= 85:
                    pass  
        elif Cnt == (15 + L_FondleB) and L_SEXP >= 15 and not ApprovalCheck("Laura", 1500):
                    $ L_Brows = "confused" 
                    menu:
                        ch_l "Maybe it's time for something else, [L_Petname]?"
                        "Finish up.":
                                "You let go. . ."   
                                jump L_FB_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump L_FB_After
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
                                    ch_l "Well, I've got better things to be doing."                         
                                    call Statup("Laura", "Love", 50, -3, 1)
                                    call Statup("Laura", "Love", 80, -4, 1)
                                    call Statup("Laura", "Obed", 30, -1, 1)                    
                                    call Statup("Laura", "Obed", 50, -1, 1)  
                                    $ L_RecentActions.append("angry")
                                    $ L_DailyActions.append("angry")   
                                    jump L_FB_After
        #End Count check
           
        if Round == 10:
            ch_l "It's getting late, we should wrap this up."  
        elif Round == 5:
            ch_l "Tic tock, [L_Petname]."    
            
        if L_Lust >= 50 and not L_Uptop and (L_Chest or L_Over):
                $ L_Uptop = 1
                "Laura grunts and pulls her clothes aside."        
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, [L_Petname], breaktime."
    
label L_FB_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call L_Pos_Reset
        
    call LauraFace("sexy") 
    
    $ L_FondleB += 1  
    $ L_Action -=1
    $ L_Addictionrate += 1
    if "addictive" in P_Traits:
        $ L_Addictionrate += 1        
    
    call Partner_Like("Laura",2)
     
    if L_FondleB == 1:            
            $ L_SEXP += 4         
            if not Situation: 
                if L_Love >= 500 and "unsatisfied" not in L_RecentActions:
                    ch_l "Did you enjoy that?"
                elif L_Obed <= 500 and P_Focus <= 20:
                    call LauraFace("perplexed", 1)
                    ch_l "That worked out for you?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Oh? What did you have in mind?"
    call Checkout
    return   

# End Fondle Breasts


# R Suck Breasts /////////////////////////////////////////////////////////////////////////////

label L_Suck_Breasts:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
                                                                                        # Will she let you suck? Modifiers
    if L_SuckB: #You've done it before
        $ Tempmod += 15
    if not L_Chest and not L_Over:
        $ Tempmod += 15
    if L_Lust > 75: #She's really horny
        $ Tempmod += 20
    if L_Lust > 75 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in L_Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in L_Traits or "sex friend" in L_Petnames:
        $ Tempmod += 10
    elif "ex" in L_Traits:
        $ Tempmod -= 25  
    if L_ForcedCount and not L_Forced:
        $ Tempmod -= 5 * L_ForcedCount     
    
    if Taboo and "tabno" in L_DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in L_History:                   
        $ Tempmod -= 20 
        
    if "no suck breasts" in L_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no suck breasts" in L_RecentActions else 0   
        
    $ Approval = ApprovalCheck("Laura", 1050, TabM = 4) # 105, 120, 135, Taboo -160(265)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            call LauraFace("sexy")       
            call Statup("Laura", "Obed", 90, 1)
            call Statup("Laura", "Obed", 70, 2)
            call Statup("Laura", "Inbt", 70, 3)
            call Statup("Laura", "Inbt", 30, 2)            
            "As you dive in, Laura seems a bit surprised, but just makes a little \"grunt.\""              
            jump L_SB_Prep      
        else:               
            call LauraFace("surprised")
            call Statup("Laura", "Obed", 50, -2)
            ch_l "Roll it back, [L_Petname]. . ."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
    
    if "suck breasts" in L_RecentActions:
        call LauraFace("sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump L_SB_Prep
    elif "suck breasts" in L_DailyActions:
        call LauraFace("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Chill. . .",
            "Mmm. . ."]) 
        ch_l "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .
        call LauraFace("bemused", 1)
        if L_Forced:
            call LauraFace("sad")
            call Statup("Laura", "Love", 70, -3, 1)
            call Statup("Laura", "Love", 20, -2, 1)
            call Statup("Laura", "Obed", 90, 1)
            call Statup("Laura", "Inbt", 60, 1)
        ch_l "Sure."   
        call Statup("Laura", "Love", 90, 1)
        call Statup("Laura", "Inbt", 50, 3) 
        jump L_SB_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        call LauraFace("angry", 1)
        if "no suck breasts" in L_RecentActions:  
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "tabno" in L_DailyActions and "no suck breasts" in L_DailyActions:  
            ch_l "I told you, I couldn't be caught like that." 
        elif "no suck breasts" in L_DailyActions:       
            ch_l "Don't make me tell you again today."
        elif Taboo and "tabno" in L_DailyActions:  
            ch_l "I told you, not here, [L_Petname]."  
        elif not L_SuckB:
            call LauraFace("bemused")
            ch_l "Let's work up to that maybe. ."
        else:
            call LauraFace("bemused")
            ch_l "You wish."  
        menu:
            extend ""
            "Sorry, never mind." if "no suck breasts" in L_DailyActions:
                call LauraFace("bemused")
                ch_l "It's cool."              
                return
            "Maybe later?" if "no suck breasts" not in L_DailyActions:
                call LauraFace("sexy")  
                ch_l "Maybe, [L_Petname]."
                call Statup("Laura", "Love", 80, 1)
                call Statup("Laura", "Love", 50, 1)
                call Statup("Laura", "Inbt", 30, 2)    
                if Taboo:                    
                    $ L_RecentActions.append("tabno")                      
                    $ L_DailyActions.append("tabno") 
                $ L_RecentActions.append("no suck breasts")                      
                $ L_DailyActions.append("no suck breasts")            
                return
            "Come on, Please?":             
                if Approval:
                    call LauraFace("sexy")     
                    call Statup("Laura", "Obed", 90, 1)
                    call Statup("Laura", "Obed", 50, 2)
                    call Statup("Laura", "Inbt", 60, 3)
                    call Statup("Laura", "Inbt", 30, 2)
                    ch_l "Ok, fine. . ."                
                    jump L_SB_Prep
                else:   
                    call LauraFace("sexy") 
                    ch_l "Well if you're going to be a little bitch about it. . ."    
            
            "[[Start sucking anyway]":                                               # Pressured into licking. 
                $ Approval = ApprovalCheck("Laura", 450, "OI", TabM = 3) # 45, 60, 75, -120(165)
                if Approval > 1 or (Approval and L_Forced):
                    call LauraFace("sad")
                    call Statup("Laura", "Love", 70, -5, 1)
                    call Statup("Laura", "Love", 20, -2, 1)                 
                    ch_l "Hmm. . . ok. . ."                         
                    call Statup("Laura", "Obed", 90, 2)
                    call Statup("Laura", "Obed", 50, 4)
                    call Statup("Laura", "Inbt", 60, 3)  
                    if Approval < 2:                          
                        $ L_Forced = 1
                    jump L_SB_Prep
                else:                              
                    call Statup("Laura", "Love", 200, -10)  
                    call LauraFace("angry", 1)
                    "She shoves your head back out."   
                    $ L_RecentActions.append("angry")
                    $ L_DailyActions.append("angry")   
                    
    if "no suck breasts" in L_DailyActions:
        ch_l "I don't like to repeat myself, [L_Petname]."   
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif L_Forced:
        call LauraFace("angry", 1)
        ch_l "Not worth it."
        call Statup("Laura", "Lust", 60, 5)    
        call Statup("Laura", "Obed", 50, -2)    
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif Taboo:   
        call LauraFace("angry", 1)      
        $ L_RecentActions.append("tabno")    
        $ L_DailyActions.append("tabno") 
        ch_l "I try to stay off the radar."                   
    elif L_SuckB:
        call LauraFace("sad")
        ch_l "You'll have to earn that back."            
    else:
        call LauraFace("sexy") 
        $ L_Mouth = "sad"
        ch_l "No."
    $ L_RecentActions.append("no suck breasts")                      
    $ L_DailyActions.append("no suck breasts") 
    $ Tempmod = 0    
    return
         

label L_SB_Prep:                                                                 #Animation set-up 
            
    if Trigger2 == "suck breasts":
        return
        
    if not L_Forced and Situation != "auto":
        $ Tempmod = 0   
        call Laura_Top_Off
        if "angry" in L_RecentActions:
            return
    
    $ Tempmod = 0      
    call L_Breasts_Launch("suck breasts")
    if not L_SuckB:        
        if L_Forced:
            call Statup("Laura", "Love", 90, -25)
            call Statup("Laura", "Obed", 70, 25)
            call Statup("Laura", "Inbt", 80, 17) 
        else:
            call Statup("Laura", "Love", 90, 10)
            call Statup("Laura", "Obed", 70, 10)
            call Statup("Laura", "Inbt", 80, 15) 
    
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
    call DrainWord("Laura","no suck breasts")
    $ L_RecentActions.append("suck breasts")                      
    $ L_DailyActions.append("suck breasts") 
    
label L_SB_Cycle: #Repeating strokes  
    if Trigger2 == "kiss you":
            $ Trigger2 = 0
    while Round >=0:  
        call Shift_Focus("Laura") 
        call L_Breasts_Launch("suck breasts")
        call LauraLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                         
                        "Slap her ass":                     
                                    call L_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump L_SB_Cycle  
                                    
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
                                                        "Pull back to fondling.":  
                                                            if L_Action and MultiAction:
                                                                $ Situation = "pullback"
                                                                call L_SB_After
                                                                call L_Fondle_Breasts
                                                            else:
                                                                "As you pull back, Laura pushes you back in close."
                                                                ch_l "Maybe we could finish this up for now?"
                                                        "Never Mind":
                                                                jump L_SB_Cycle
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
                                                        jump L_SB_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump L_SB_Cycle 
                                            "Never mind":
                                                        jump L_SB_Cycle 
                                    "Undress Laura":
                                            call L_Undress   
                                    "Clean up Laura (locked)" if not L_Spunk:
                                            pass  
                                    "Clean up Laura" if L_Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump L_SB_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call L_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump L_SB_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call L_Pos_Reset
                                    $ Line = 0
                                    jump L_SB_After
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
                                call L_Pos_Reset
                                return    
                            call Statup("Laura", "Lust", 200, 5) 
                            if 100 > L_Lust >= 70 and L_OCount < 2:             
                                $ L_RecentActions.append("unsatisfied")                      
                                $ L_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump L_SB_After 
                            $ Line = "came"
     
                    if L_Lust >= 100:  
                            #If Laura can cum                                             
                            call L_Cumming
                            if Situation == "shift" or "angry" in L_RecentActions:
                                jump L_SB_After
                       
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
                                            jump L_SB_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if L_SEXP >= 100 or ApprovalCheck("Laura", 1200, "LO"):
            pass
        elif Cnt == (5 + L_SuckB):
                    $ L_Brows = "sly"
                    ch_l "This is kinda nice. . ."   
        elif L_Lust >= 85:
                    pass
        elif Cnt == (15 + L_SuckB) and L_SEXP >= 15 and not ApprovalCheck("Laura", 1500):
                    $ L_Brows = "confused"        
                    menu:
                        ch_l "Maybe change things up a little?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump L_SB_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump L_SB_After
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
                                    ch_l "I'm kinda bored here."                         
                                    call Statup("Laura", "Love", 50, -3, 1)
                                    call Statup("Laura", "Love", 80, -4, 1)
                                    call Statup("Laura", "Obed", 30, -1, 1)                    
                                    call Statup("Laura", "Obed", 50, -1, 1)  
                                    $ L_RecentActions.append("angry")
                                    $ L_DailyActions.append("angry")   
                                    jump L_SB_After
        #End Count check
           
        if Round == 10:
            ch_l "It's getting late, we should wrap this up."  
        elif Round == 5:
            ch_l "Tic tock, [L_Petname]."        
    
        if L_Lust >= 50 and not L_Uptop and (L_Chest or L_Over):
                $ L_Uptop = 1
                "Laura grunts and pulls her clothes aside."        
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, [L_Petname], breaktime."
    
label L_SB_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call L_Pos_Reset
        
    call LauraFace("sexy") 
    
    $ L_SuckB += 1  
    $ L_Action -=1
    $ L_Addictionrate += 1
    if "addictive" in P_Traits:
        $ L_Addictionrate += 1        
    
    if Partner == "Kitty":
        call Partner_Like("Laura",2,2)
    else:
        call Partner_Like("Laura",2)
     
    if L_SuckB == 1:            
            $ L_SEXP += 4         
            if not Situation: 
                if L_Love >= 500 and "unsatisfied" not in L_RecentActions:
                    ch_l "That was kinda nice."
                elif L_Obed <= 500 and P_Focus <= 20:
                    call LauraFace("perplexed", 1)
                    ch_l "Did you get enough?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Oh? What did you have in mind?"
    call Checkout
    return   
    
# End Suck breasts    

# Fondle Thighs start //////////////////////////////////////////

label L_Fondle_Thighs:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
                                                                                        # Will she let you fondle her thighs? Modifiers
    if L_FondleT: #You've done it before
        $ Tempmod += 10
    if L_Legs == "pants" or HoseNum("Laura") >= 5: # she's got pants on.
        $ Tempmod -= 5    
    if L_Lust > 75: #She's really horny
        $ Tempmod += 10    
    if "exhibitionist" in L_Traits:
        $ Tempmod += Taboo   
    if "dating" in L_Traits or "sex friend" in L_Petnames:
        $ Tempmod += 10
    elif "ex" in L_Traits:
        $ Tempmod -= 25 
    if L_ForcedCount and not L_Forced:
        $ Tempmod -= 5 * L_ForcedCount      
    
    if Taboo and "tabno" in L_DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in L_History:                   
        $ Tempmod -= 20 
        
    if "no fondle thighs" in L_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle thighs" in L_RecentActions else 0   
            
    $ Approval = ApprovalCheck("Laura", 750, TabM=1) # 75, 90, 105, Taboo -40(105)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            call LauraFace("sexy")       
            call Statup("Laura", "Obed", 50, 1)
            call Statup("Laura", "Inbt", 30, 2)            
            "As you caress her thigh, Laura glances at you, and smiles."             
            jump L_FT_Prep      
        else:               
            call LauraFace("surprised")
            call Statup("Laura", "Obed", 50, -2)
            ch_l "Maybe we keep it above the waist, [L_Petname]."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        call LauraFace("surprised")    
        $ L_Brows = "sad"
        if L_Lust > 60:
            call Statup("Laura", "Love", 70, -3)
        call Statup("Laura", "Obed", 90, 1)
        call Statup("Laura", "Obed", 70, 2)
        "As you pull back, Laura looks a little annoyed."              
        jump L_FT_Prep  
    elif "fondle thighs" in L_RecentActions:
        call LauraFace("sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump L_FT_Prep
    elif "fondle thighs" in L_DailyActions:
        call LauraFace("sexy", 1)       
        ch_l "You didn't get enough earlier?"
    
    if Approval >= 2:                                                                   #She's into it. . .
        call LauraFace("bemused", 1)
        if L_Forced:
            call LauraFace("sad")
            call Statup("Laura", "Love", 70, -3, 1)
            call Statup("Laura", "Obed", 90, 1)
            call Statup("Laura", "Inbt", 60, 1)
        ch_l "Ok [L_Petname], go ahead."   
        call Statup("Laura", "Love", 90, 1)
        call Statup("Laura", "Inbt", 50, 3) 
        jump L_FT_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        call LauraFace("angry", 1)
        if "no fondle thighs" in L_RecentActions:  
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "tabno" in L_DailyActions and "no fondle thighs" in L_DailyActions:  
            ch_l "I told you not to touch me like that in public!" 
        elif "no fondle thighs" in L_DailyActions:       
            ch_l "Don't make me tell you again today."
        elif Taboo and "tabno" in L_DailyActions:  
            ch_l "I told you, not here, [L_Petname]."  
        elif not L_FondleT:
            call LauraFace("bemused")
            ch_l "Seems a bit aggressive, [L_Petname]."
        else:
            call LauraFace("bemused")
            ch_l "You wish."  
        menu:
            extend ""
            "Sorry, never mind." if "no fondle thighs" in L_DailyActions:
                call LauraFace("bemused")
                ch_l "It's cool."             
                return
            "Maybe later?" if "no fondle thighs" not in L_DailyActions:
                call LauraFace("sexy")  
                ch_l "Maybe?"
                call Statup("Laura", "Love", 80, 1)
                call Statup("Laura", "Inbt", 30, 2)    
                if Taboo:                    
                    $ L_RecentActions.append("tabno")                      
                    $ L_DailyActions.append("tabno") 
                $ L_RecentActions.append("no fondle thighs")                      
                $ L_DailyActions.append("no fondle thighs")            
                return
            "Come on, Please?":             
                if Approval:
                    call LauraFace("sexy")     
                    call Statup("Laura", "Obed", 60, 1)
                    call Statup("Laura", "Obed", 30, 2)
                    call Statup("Laura", "Inbt", 50, 1)
                    call Statup("Laura", "Inbt", 30, 2)
                    ch_l "Well if you're going to be a little bitch about it. . ."             
                    jump L_FT_Prep
                else:   
                    call LauraFace("sexy") 
                    ch_l "Well if you're going to be a little bitch about it. . ."    
            
            "[[Start caressing her thigh anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Laura", 350, "OI", TabM = 2) # 35, 50, 65, -80(105)
                if Approval > 1 or (Approval and L_Forced):
                    call LauraFace("sad")
                    call Statup("Laura", "Love", 70, -5, 1)
                    call Statup("Laura", "Love", 20, -2, 1)                 
                    ch_l "Hmmph."                         
                    call Statup("Laura", "Obed", 50, 3)
                    call Statup("Laura", "Inbt", 60, 2)  
                    if Approval < 2:                          
                        $ L_Forced = 1
                    jump L_FT_Prep
                else:                              
                    call Statup("Laura", "Love", 200, -8)  
                    call LauraFace("angry", 1)
                    "She slaps your hand away."   
                    $ L_RecentActions.append("angry")
                    $ L_DailyActions.append("angry")   
                    
    if "no fondle thighs" in L_DailyActions:
        ch_l "I don't like to repeat myself, [L_Petname]."   
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif L_Forced:
        call LauraFace("angry", 1)
        ch_l "No."
        call Statup("Laura", "Lust", 50, 2)    
        call Statup("Laura", "Obed", 50, -1)   
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif Taboo:
        call LauraFace("angry", 1)    
        $ L_RecentActions.append("tabno")          
        $ L_DailyActions.append("tabno") 
        ch_l "I try to stay off the radar."                   
    elif L_FondleT:
        call LauraFace("sad")
        ch_l "Keep your hands to yourself."            
    else:
        call LauraFace("sexy") 
        $ L_Mouth = "sad"
        ch_l "No."
    $ L_RecentActions.append("no fondle thighs")                      
    $ L_DailyActions.append("no fondle thighs") 
    $ Tempmod = 0    
    return
    
label L_FT_Prep:                                                                 #Animation set-up 
    if Trigger == "kiss you": 
        $ Trigger = "fondle thighs" 
        return
        
    if Trigger2 == "fondle thighs": 
        return
        
    if not L_Forced and Situation != "auto":
        $ Tempmod = 0
        call Laura_Bottoms_Off 
        if "angry" in L_RecentActions:
            return 
            
    $ Tempmod = 0    
    call L_Pussy_Launch("fondle thighs")
    if not L_FondleT:        
        if L_Forced:
            call Statup("Laura", "Love", 90, -10)
            call Statup("Laura", "Obed", 70, 15)
            call Statup("Laura", "Inbt", 80, 10) 
        else:
            call Statup("Laura", "Love", 90, 5)
            call Statup("Laura", "Obed", 70, 10)
            call Statup("Laura", "Inbt", 80, 15) 
            
    if Taboo:               
        call Statup("Laura", "Lust", 200, (int(Taboo/5)))                               
        call Statup("Laura", "Inbt", 200, (2*(int(Taboo/5))))
     
    if Situation:   
        $ renpy.pop_call() 
        $ Situation = 0 
    $ Line = 0 
    $ Cnt = 0
    if Taboo:
        call DrainWord("Laura","tabno")
    call DrainWord("Laura","no fondle thighs")
    $ L_RecentActions.append("fondle thighs")                      
    $ L_DailyActions.append("fondle thighs")  
    
label L_FT_Cycle:                                                                #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Laura") 
        call L_Pussy_Launch("fondle thighs")
        call LauraLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                         
                        "Slap her ass":                     
                                    call L_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump L_FT_Cycle  
                                    
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
                                                        "Can I do a little deeper?":
                                                                if L_Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call L_FT_After
                                                                    call L_Fondle_Pussy                
                                                                else:
                                                                    ch_l "Maybe we could finish this up for now?"  
                                                        "Shift your hands a bit higher without asking":
                                                                if L_Action and MultiAction:
                                                                    $ Situation = "auto"
                                                                    call L_FT_After
                                                                    call L_Fondle_Pussy    
                                                                else:
                                                                    "As your hands creep upwards, she grabs your wrists."
                                                                    ch_l "Maybe we could finish this up for now?" 
                                                        "Never Mind":
                                                                jump L_FT_Cycle
                                            else: 
                                                ch_l "Maybe we could finish this up for now?"           
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call L_FT_After
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
                                                        jump L_FT_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump L_FT_Cycle 
                                            "Never mind":
                                                        jump L_FT_Cycle 
                                    "Undress Laura":
                                            call L_Undress   
                                    "Clean up Laura (locked)" if not L_Spunk:
                                            pass  
                                    "Clean up Laura" if L_Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump L_FT_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call L_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump L_FT_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call L_Pos_Reset
                                    $ Line = 0
                                    jump L_FT_After
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
                                call L_Pos_Reset
                                return    
                            call Statup("Laura", "Lust", 200, 5) 
                            if 100 > L_Lust >= 70 and L_OCount < 2:             
                                $ L_RecentActions.append("unsatisfied")                      
                                $ L_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump L_FT_After 
                            $ Line = "came"
     
                    if L_Lust >= 100:  
                            #If Laura can cum                                             
                            call L_Cumming
                            if Situation == "shift" or "angry" in L_RecentActions:
                                jump L_FT_After
                       
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
                                            jump L_FT_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if L_SEXP >= 100 or ApprovalCheck("Laura", 1200, "LO"):
            pass
        elif Cnt == (5 + L_FondleT):
                    $ L_Brows = "confused"
                    ch_l "Kinda nice, but. . ."   
        elif Cnt == (15 + L_FondleT) and L_SEXP >= 15 and not ApprovalCheck("Laura", 1500):
                    $ L_Brows = "confused"        
                    menu:
                        ch_l "Maybe change things up a little?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump L_FT_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump L_FT_After
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
                                    ch_l "I'm kinda bored here."                         
                                    call Statup("Laura", "Love", 50, -3, 1)
                                    call Statup("Laura", "Love", 80, -4, 1)
                                    call Statup("Laura", "Obed", 30, -1, 1)                    
                                    call Statup("Laura", "Obed", 50, -1, 1)  
                                    $ L_RecentActions.append("angry")
                                    $ L_DailyActions.append("angry")   
                                    jump L_FT_After
        #End Count check
           
        if Round == 10:
            ch_l "It's getting late, we should wrap this up."  
        elif Round == 5:
            ch_l "Tic tock, [L_Petname]."        
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, [L_Petname], breaktime."
    
    
label L_FT_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call L_Pos_Reset
        
    call LauraFace("sexy") 
    
    $ L_FondleT += 1  
    $ L_Action -=1
    if L_Legs != "pants" or L_Upskirt:        
        $ L_Addictionrate += 1
        if "addictive" in P_Traits:
            $ L_Addictionrate += 1
    
    if Partner == "Kitty":
        call Partner_Like("Laura",2)
    else:
        call Partner_Like("Laura",1)
     
    if L_FondleT == 1:            
            $ L_SEXP += 3         
            if not Situation: 
                if L_Love >= 500 and "unsatisfied" not in L_RecentActions:
                    ch_l "That was. . . interesting."
                elif L_Obed <= 500 and P_Focus <= 20:
                    call LauraFace("perplexed", 1)
                    ch_l "Was that enough?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Oh? What did you have in mind?"
    call Checkout
    return   
    
# ////////////////////////////////////////////////////////////////////////Start Fondle Pussy    
label L_Fondle_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
                                                                                        # Will she let you fondle? Modifiers
    if L_FondleP: #You've done it before
        $ Tempmod += 20
    if L_Legs == "pants" or HoseNum("Laura") >= 5: # she's got pants on.
        $ Tempmod -= 10    
    if L_Lust > 75: #She's really horny
        $ Tempmod += 15
    if L_Lust > 75 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in L_Traits:
        $ Tempmod += (2*Taboo)
    if "dating" in L_Traits or "sex friend" in L_Petnames:
        $ Tempmod += 10
    elif "ex" in L_Traits:
        $ Tempmod -= 25  
    if L_ForcedCount and not L_Forced:
        $ Tempmod -= 5 * L_ForcedCount     
    
    if Taboo and "tabno" in L_DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in L_History:                   
        $ Tempmod -= 20 
        
    if "no fondle pussy" in L_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle pussy" in L_RecentActions else 0   
            
    $ Approval = ApprovalCheck("Laura", 1050, TabM = 2) # 105, 120, 135, Taboo -80(185)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            call LauraFace("sexy")       
            call Statup("Laura", "Obed", 90, 1)
            call Statup("Laura", "Obed", 70, 2)
            call Statup("Laura", "Inbt", 70, 3)
            call Statup("Laura", "Inbt", 30, 2)
            "As your hand creeps up her thigh, Laura seems a bit surprised, but then nods."            
            jump L_FP_Prep      
        else:               
            call LauraFace("surprised")
            call Statup("Laura", "Obed", 50, -2)
            ch_l "Roll it back, [L_Petname]. . ."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        call LauraFace("surprised")   
        $ L_Brows = "sad"        
        if L_Lust > 80:
            call Statup("Laura", "Love", 70, -4)
        call Statup("Laura", "Obed", 90, 1)
        call Statup("Laura", "Obed", 70, 2)
        "As your hand pulls out, Laura gasps and looks upset."              
        jump L_FP_Prep     
    elif "fondle pussy" in L_RecentActions:
        call LauraFace("sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump L_FP_Prep
    elif "fondle pussy" in L_DailyActions:
        call LauraFace("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Chill. . .",
            "Take it slow, I'm still shaking from earlier.",
            "Mmm. . ."]) 
        ch_l "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .
        call LauraFace("bemused", 1)
        if L_Forced:
            call LauraFace("sad")
            call Statup("Laura", "Love", 70, -3, 1)
            call Statup("Laura", "Love", 20, -2, 1)
            call Statup("Laura", "Obed", 90, 1)
            call Statup("Laura", "Inbt", 60, 1)
        ch_l "Mmmm, I couldn't refuse. . ."   
        call Statup("Laura", "Love", 90, 1)
        call Statup("Laura", "Inbt", 50, 3) 
        jump L_FP_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        call LauraFace("angry", 1)
        if "no fondle pussy" in L_RecentActions:  
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "tabno" in L_DailyActions and "no fondle pussy" in L_DailyActions:  
            ch_l "I told you not to touch me like that in public!" 
        elif "no fondle pussy" in L_DailyActions:       
            ch_l "Don't make me tell you again today."
        elif Taboo and "tabno" in L_DailyActions:  
            ch_l "I told you, not here, [L_Petname]."  
        elif not L_FondleP:
            call LauraFace("bemused")
            ch_l "I don't think we're there yet, [L_Petname]. . ."
        else:
            call LauraFace("bemused")
            ch_l "You wish."  
        menu:
            extend ""
            "Sorry, never mind." if "no fondle pussy" in L_DailyActions:
                call LauraFace("bemused")
                ch_l "It's cool, [L_Petname]."              
                return
            "Maybe later?" if "no fondle pussy" not in L_DailyActions:
                call LauraFace("sexy")  
                ch_l "Maybe, [L_Petname]."
                call Statup("Laura", "Love", 80, 2)
                call Statup("Laura", "Inbt", 70, 2)   
                if Taboo:                    
                    $ L_RecentActions.append("tabno")                      
                    $ L_DailyActions.append("tabno") 
                $ L_RecentActions.append("no fondle pussy")                      
                $ L_DailyActions.append("no fondle pussy")            
                return
            "Come on, Please?":             
                if Approval:
                    call LauraFace("sexy")     
                    call Statup("Laura", "Obed", 90, 2)
                    call Statup("Laura", "Obed", 50, 2)
                    call Statup("Laura", "Inbt", 70, 3) 
                    call Statup("Laura", "Inbt", 40, 2) 
                    ch_l "Oooh, beg for me. . ."                    
                    jump L_FP_Prep
                else:   
                    call LauraFace("sexy") 
                    ch_l "No."
            
            "[[Start fondling anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Laura", 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                if Approval > 1 or (Approval and L_Forced):
                    call LauraFace("sad")
                    call Statup("Laura", "Love", 70, -5, 1)
                    call Statup("Laura", "Love", 200, -2)                 
                    ch_l "Ok, fine. . ."
                    call Statup("Laura", "Obed", 50, 4)
                    call Statup("Laura", "Inbt", 80, 1) 
                    call Statup("Laura", "Inbt", 60, 3)  
                    if Approval < 2:                          
                        $ L_Forced = 1
                    jump L_FP_Prep
                else:                              
                    call Statup("Laura", "Love", 200, -15)  
                    call LauraFace("angry", 1)
                    "She slaps your hand away."   
                    $ L_RecentActions.append("angry")
                    $ L_DailyActions.append("angry")   
                    
    if "no fondle pussy" in L_DailyActions:
        ch_l "I don't like to repeat myself, [L_Petname]."   
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif L_Forced:
        call LauraFace("angry", 1)
        ch_l "I don't think so, [L_Petname]."
        call Statup("Laura", "Lust", 70, 5)    
        call Statup("Laura", "Obed", 50, -2)    
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif Taboo:
        call LauraFace("angry", 1)    
        $ L_RecentActions.append("tabno")                   
        $ L_DailyActions.append("tabno")
        ch_l "I try to stay off the radar."                   
    elif L_FondleP:
        call LauraFace("sad")
        ch_l "Sorry, fingers outside."           
    else:
        call LauraFace("sexy") 
        $ L_Mouth = "sad"
        ch_l "No thank you, [L_Petname]."
    $ L_RecentActions.append("no fondle pussy")                      
    $ L_DailyActions.append("no fondle pussy") 
    $ Tempmod = 0    
    return
                    
label L_FP_Prep: #Animation set-up 
    if Trigger2 == "fondle pussy":
        return
        
    if not L_Forced and Situation != "auto":
        $ Tempmod = 0
        call Laura_Bottoms_Off   
        if "angry" in L_RecentActions:
            return 
    $ Tempmod = 0
    
    call L_Pussy_Launch("fondle pussy")
    if not L_FondleP:        
        if L_Forced:
            call Statup("Laura", "Love", 90, -50)
            call Statup("Laura", "Obed", 70, 35)
            call Statup("Laura", "Inbt", 80, 25) 
        else:
            call Statup("Laura", "Love", 90, 10)
            call Statup("Laura", "Obed", 70, 10)
            call Statup("Laura", "Inbt", 80, 15) 
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
    call DrainWord("Laura","no fondle pussy")
    $ L_RecentActions.append("fondle pussy")                      
    $ L_DailyActions.append("fondle pussy") 
    
    $ Speed = 1
    
label L_FP_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Laura") 
        call L_Pussy_Launch("fondle pussy")
        call LauraLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                          
                        "I want to stick a finger in. . ." if Speed != 2:
                                if L_InsertP: 
                                    $ Speed = 2
                                else:
                                    menu:                                
                                        "Ask her first":
                                            $ Situation = "shift"
                                        "Don't ask first [[just stick it in]":                                    
                                            $ Situation = "auto"
                                    call L_Insert_Pussy 
                        
                        "Pull back a bit. . ." if Speed == 2:
                                    $ Speed = 0
                                    
                        "Slap her ass":                     
                                    call L_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump L_FP_Cycle  
                                    
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
                                                        "I want to lick your pussy.":
                                                                $ Situation = "shift"
                                                                call L_FP_After
                                                                call L_Lick_Pussy                 
                                                        "Just start licking":
                                                                $ Situation = "auto"
                                                                call L_FP_After
                                                                call L_Lick_Pussy         
                                                        "Pull back to the thighs":
                                                                $ Situation = "pullback"
                                                                call L_FP_After
                                                                call L_Fondle_Thighs
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call L_FP_After
                                                                call L_Dildo_Pussy  
                                                        "Never Mind":
                                                                jump L_FP_Cycle
                                            else: 
                                                ch_l "Maybe we could finish this up for now?"           
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call L_FP_After
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
                                                        jump L_FP_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump L_FP_Cycle 
                                            "Never mind":
                                                        jump L_FP_Cycle 
                                    "Undress Laura":
                                            call L_Undress   
                                    "Clean up Laura (locked)" if not L_Spunk:
                                            pass  
                                    "Clean up Laura" if L_Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump L_FP_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call L_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump L_FP_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call L_Pos_Reset
                                    $ Line = 0
                                    jump L_FP_After
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
                                call L_Pos_Reset
                                return    
                            call Statup("Laura", "Lust", 200, 5) 
                            if 100 > L_Lust >= 70 and L_OCount < 2:             
                                $ L_RecentActions.append("unsatisfied")                      
                                $ L_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump L_FP_After 
                            $ Line = "came"
     
                    if L_Lust >= 100:  
                            #If Laura can cum                                             
                            call L_Cumming
                            if Situation == "shift" or "angry" in L_RecentActions:
                                jump L_FP_After
                       
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
                                            jump L_FP_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if L_SEXP >= 100 or ApprovalCheck("Laura", 1200, "LO"):
            pass
        elif Cnt == (5 + L_FondleP):
                    $ L_Brows = "confused"
                    ch_l "Mmmm, you're enjoying that, huh?"  
        elif L_Lust >= 80:
                    pass
        elif Cnt == (15 + L_FondleP) and L_SEXP >= 15 and not ApprovalCheck("Laura", 1500):
                    $ L_Brows = "confused"        
                    menu:
                        ch_l "Maybe change things up a little?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump L_FP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump L_FP_After
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
                                    ch_l "I'm kinda bored here."                         
                                    call Statup("Laura", "Love", 50, -3, 1)
                                    call Statup("Laura", "Love", 80, -4, 1)
                                    call Statup("Laura", "Obed", 30, -1, 1)                    
                                    call Statup("Laura", "Obed", 50, -1, 1)  
                                    $ L_RecentActions.append("angry")
                                    $ L_DailyActions.append("angry")   
                                    jump L_FP_After
        #End Count check
           
        if Round == 10:
            ch_l "It's getting late, we should wrap this up."  
        elif Round == 5:
            ch_l "Tic tock, [L_Petname]."        
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, [L_Petname], breaktime."
    
    
label L_FP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call L_Pos_Reset
        
    call LauraFace("sexy") 
    
    $ L_FondleP += 1  
    $ L_Action -=1
    if L_Legs != "pants" or L_Upskirt:        
        $ L_Addictionrate += 1
        if "addictive" in P_Traits:
            $ L_Addictionrate += 1
    
    call Partner_Like("Laura",2)
     
    if L_FondleP == 1:            
            $ L_SEXP += 7         
            if not Situation: 
                if L_Love >= 500 and "unsatisfied" not in L_RecentActions:
                    ch_l "You're really getting into the good stuff."
                elif L_Obed <= 500 and P_Focus <= 20:
                    call LauraFace("perplexed", 1)
                    ch_l "Did you find what you were looking for?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Oh? What did you have in mind?"
    call Checkout
    return   

# end L_Fondle Pussy /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label L_Insert_Pussy:
    call Shift_Focus("Laura")
    if Situation == "auto":                                                                  #You auto-start                    
        if ApprovalCheck("Laura", 1100, TabM = 2):
            call LauraFace("surprised")       
            call Statup("Laura", "Obed", 90, 1)
            call Statup("Laura", "Obed", 70, 2)
            call Statup("Laura", "Inbt", 70, 3) 
            call Statup("Laura", "Inbt", 30, 2) 
            "As you slide a finger in, Laura seems a bit surprised, but seems into it."              
            jump L_IP_Prep
        else:   
            call LauraFace("surprised",2)
            call Statup("Laura", "Love", 80, -2)
            call Statup("Laura", "Obed", 50, -3)
            ch_l "Oooh!"
            "She slaps your hand back."
            call LauraFace("perplexed",1)
            ch_l "Watch your hands, or lose them."
            return            
    
    if ApprovalCheck("Laura", 1100, TabM = 2):                                                                   #She's into it. . .               
        if L_Forced:
            call LauraFace("sad")
            call Statup("Laura", "Love", 70, -3, 1)
            call Statup("Laura", "Love", 20, -2, 1)
            call Statup("Laura", "Obed", 90, 1)
            call Statup("Laura", "Inbt", 60, 1)
            ch_l "Going there, huh. . ."    
        else:
            call LauraFace("sexy", 1)
            call Statup("Laura", "Love", 90, 1)
            call Statup("Laura", "Inbt", 50, 3) 
            ch_l "Mmmmmm. . ."                
        call Statup("Laura", "Obed", 20, 1)
        call Statup("Laura", "Obed", 60, 1)
        call Statup("Laura", "Inbt", 70, 2) 
        jump L_IP_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .  
        call LauraFace("bemused", 1)
        ch_l "Nope."
        $ L_Blush = 0
    return
    
                
label L_IP_Prep: #Animation set-up     
    if not L_InsertP:
        $ L_InsertP = 1
        $ L_SEXP += 10          
        if L_Forced:
            call Statup("Laura", "Love", 90, -60)
            call Statup("Laura", "Obed", 70, 55)
            call Statup("Laura", "Inbt", 80, 35) 
        else:
            call Statup("Laura", "Love", 90, 10)
            call Statup("Laura", "Obed", 70, 20)
            call Statup("Laura", "Inbt", 80, 25)
                
    if not L_Forced and Situation != "auto":        
        call L_Undress("bottom")
        if "angry" in L_RecentActions:
            return    
            
#    call L_Pussy_Launch("insert pussy")
    if Taboo:
        $ L_Inbt += int(Taboo/10)  
        $ L_Lust += int(Taboo/5)
        
    $ Line = 0  
    $ Speed = 2
    return

# end L_Insert Pussy /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label L_Lick_Pussy: 
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
                                                                                  # Will she let you fondle? Modifiers     
    if L_LickP: #You've done it before
        $ Tempmod += 15
    if L_Legs == "pants" or HoseNum("Laura") >= 5: # she's got pants on.
        $ Tempmod -= 15  
    if L_Lust > 95:
        $ Tempmod += 20  
    elif L_Lust > 85: #She's really horny
        $ Tempmod += 15
    if Situation == "shift":
        $ Tempmod += 10
    if L_Lust > 85 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in L_Traits:
        $ Tempmod += (4*Taboo) 
    if "dating" in L_Traits or "sex friend" in L_Petnames:
        $ Tempmod += 10
    elif "ex" in L_Traits:
        $ Tempmod -= 25  
    if L_ForcedCount and not L_Forced:
        $ Tempmod -= 5 * L_ForcedCount     
    
    if Taboo and "tabno" in L_DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in L_History:                   
        $ Tempmod -= 20 
        
    if "no lick pussy" in L_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no lick pussy" in L_RecentActions else 0   
            
    $ Approval = ApprovalCheck("Laura", 1250, TabM = 4) # 125, 140, 155, Taboo -160(285)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            call LauraFace("surprised")
            call Statup("Laura", "Obed", 90, 1)
            call Statup("Laura", "Obed", 70, 2)
            call Statup("Laura", "Inbt", 70, 3) 
            call Statup("Laura", "Inbt", 30, 2) 
            "As you crouch down and start to lick her pussy, Laura starts, but then softens."  
            call LauraFace("sexy")           
            jump L_LP_Prep
        else:   
            call LauraFace("surprised")
            call Statup("Laura", "Love", 80, -2)
            call Statup("Laura", "Obed", 50, -3)
            ch_l "Hey, good instincts, but maybe hold off?" 
            call LauraFace("perplexed",1)
            "She pushes your head back away from her."
            $ Tempmod = 0
            $ Trigger2 = 0
            return            
    
    if "lick pussy" in L_RecentActions:
        call LauraFace("sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump L_LP_Prep
    elif "lick pussy" in L_DailyActions:
        call LauraFace("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right.",
            "I do like this treatment. . .",
            "Mmm. . ."]) 
        ch_l "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .               
        if L_Forced:
            call LauraFace("sad")
            call Statup("Laura", "Love", 70, -3, 1)
            call Statup("Laura", "Love", 20, -2, 1)
            call Statup("Laura", "Obed", 90, 1)
            call Statup("Laura", "Inbt", 60, 1)
            ch_l "If you must. . ."    
        else:
            call LauraFace("sexy", 1)
            $ L_Eyes = "closed"            
            call Statup("Laura", "Love", 90, 1)
            call Statup("Laura", "Inbt", 50, 3)            
            call Statup("Laura", "Lust", 200, 3)
            ch_l "Mmmmmm. . ."                
        call Statup("Laura", "Obed", 20, 1)
        call Statup("Laura", "Obed", 60, 1)
        call Statup("Laura", "Inbt", 70, 2) 
        jump L_LP_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call LauraFace("angry", 1)
        if "no lick pussy" in L_RecentActions:  
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "tabno" in L_DailyActions and "no lick pussy" in L_DailyActions:  
            ch_l "You already got your answer!" 
        elif "no lick pussy" in L_DailyActions:       
            ch_l "Don't make me tell you again today."
        elif Taboo and "tabno" in L_DailyActions:  
            ch_l "I told you, not here, [L_Petname]."  
        elif not L_LickP:
            call LauraFace("bemused")
            ch_l "I'm not sure we're there yet, [L_Petname]. . ."
        else:
            call LauraFace("bemused")
            ch_l "I'm really not cool with that. . ." 
        menu:
            extend ""
            "Sorry, never mind." if "no lick pussy" in L_DailyActions:
                call LauraFace("bemused")
                ch_l "It's cool, [L_Petname]."              
                return            
            "I'm sure I can convince you later. . ." if "no lick pussy" not in L_DailyActions:
                call LauraFace("sexy")  
                ch_l "I'll be thinking about it, [L_Petname]."
                call Statup("Laura", "Love", 80, 2)
                call Statup("Laura", "Inbt", 70, 2)   
                if Taboo:                    
                    $ L_RecentActions.append("tabno")                      
                    $ L_DailyActions.append("tabno") 
                $ L_RecentActions.append("no lick pussy")                      
                $ L_DailyActions.append("no lick pussy")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    call LauraFace("sexy")           
                    call Statup("Laura", "Obed", 90, 2)
                    call Statup("Laura", "Obed", 50, 2)
                    ch_l "You make a good point. . ."      
                    call Statup("Laura", "Inbt", 70, 3) 
                    call Statup("Laura", "Inbt", 40, 2)
                    jump L_LP_Prep
                else:   
                    call LauraFace("sexy") 
                    ch_l "I would, but still no, [L_Petname]."    
            
            "[[Get in there anyway]":                                               # Pressured into being licked. 
                $ Approval = ApprovalCheck("Laura", 750, "OI", TabM = 4) # 75, 90, 105, -160(235)
                if Approval > 1 or (Approval and L_Forced):
                    call LauraFace("sad")
                    call Statup("Laura", "Love", 70, -5, 1)
                    call Statup("Laura", "Love", 200, -2)                 
                    ch_l "If you insist. . ."  
                    call Statup("Laura", "Obed", 50, 4)
                    call Statup("Laura", "Inbt", 80, 1) 
                    call Statup("Laura", "Inbt", 60, 3)  
                    if Approval < 2:                          
                        $ L_Forced = 1
                    jump L_LP_Prep
                else:                              
                    call Statup("Laura", "Love", 200, -15)  
                    call LauraFace("angry", 1)
                    "She shoves your head back."   
                    $ L_RecentActions.append("angry")
                    $ L_DailyActions.append("angry")   
                    
    if "no lick pussy" in L_DailyActions:
        ch_l "I don't like to repeat myself, [L_Petname]."   
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif L_Forced:
        call LauraFace("angry", 1)
        ch_l "I really can't, [L_Petname]."
        call Statup("Laura", "Lust", 80, 5)    
        call Statup("Laura", "Obed", 50, -2)     
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif Taboo:
        call LauraFace("angry", 1)    
        $ L_RecentActions.append("tabno")                   
        $ L_DailyActions.append("tabno") 
        ch_l "I try to stay off the radar."                   
    elif L_LickP:
        call LauraFace("sad") 
        ch_l "Keep your head out of there."    
    else:
        call LauraFace("surprised")
        ch_l "Yeah, sorry."
        call LauraFace
    $ L_RecentActions.append("no lick pussy")                      
    $ L_DailyActions.append("no lick pussy") 
    $ Tempmod = 0    
    return
    
label L_LP_Prep: #Animation set-up  
    if Trigger2 == "lick pussy": #fix pull down pants now an option, make it work
        return
        
    if not L_Forced and Situation != "auto":
        $ Tempmod = 0
        if L_Legs == "pants" and not L_Upskirt:
            $ Tempmod = 15
        call Laura_Bottoms_Off
        if "angry" in L_RecentActions:
            return  
            
    $ Tempmod = 0      
    call L_Pussy_Launch("lick pussy")
    if not L_LickP:        
        if L_Forced:
            call Statup("Laura", "Love", 90, -30)
            call Statup("Laura", "Obed", 70, 35)
            call Statup("Laura", "Inbt", 80, 75) 
        else:
            call Statup("Laura", "Love", 90, 35)
            call Statup("Laura", "Obed", 70, 15)
            call Statup("Laura", "Inbt", 80, 35)
    if Taboo:
        $ L_Inbt += int(Taboo/10)  
        $ L_Lust += int(Taboo/5)
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
        
    if L_Legs == "skirt":
        $ L_Upskirt = 1  
        $ L_SeenPanties = 1
    call Laura_First_Bottomless(1)
    
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Laura","tabno")
    call DrainWord("Laura","no lick pussy")
    $ L_RecentActions.append("lick pussy")                      
    $ L_DailyActions.append("lick pussy") 
    
label L_LP_Cycle: #Repeating strokes
    if Trigger2 == "kiss you":
            $ Trigger2 = 0   
    while Round >=0:  
        call Shift_Focus("Laura") 
        call L_Pussy_Launch("lick pussy")
        call LauraLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                                              
                        "Slap her ass":                     
                                    call L_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump L_LP_Cycle  
                                    
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
                                                        "Pull out and start rubbing again.":
                                                                if L_Action and MultiAction:
                                                                    $ Situation = "pullback"
                                                                    call L_LP_After
                                                                    call L_Fondle_Pussy
                                                                else:
                                                                    ch_l "Maybe we could finish this up for now?"  
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call L_LP_After
                                                                call L_Dildo_Pussy  
                                                        "Never Mind":
                                                                jump L_LP_Cycle
                                            else: 
                                                ch_l "Maybe we could finish this up for now?"           
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call L_LP_After
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
                                                        jump L_LP_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump L_LP_Cycle 
                                            "Never mind":
                                                        jump L_LP_Cycle 
                                    "Undress Laura":
                                            call L_Undress   
                                    "Clean up Laura (locked)" if not L_Spunk:
                                            pass  
                                    "Clean up Laura" if L_Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump L_LP_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call L_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump L_LP_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call L_Pos_Reset
                                    $ Line = 0
                                    jump L_LP_After
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
                                jump L_LP_After 
                            $ Line = "came"
     
                    if L_Lust >= 100:  
                            #If Laura can cum                                             
                            call L_Cumming
                            if Situation == "shift" or "angry" in L_RecentActions:
                                jump L_LP_After
                       
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
                                            jump L_LP_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if L_SEXP >= 100 or ApprovalCheck("Laura", 1200, "LO"):
            pass
        elif Cnt == (5 + L_LickP):
                    $ L_Brows = "confused"
                    ch_l "Isn't it just delicious?"  
        elif L_Lust >= 80:
                    pass
        elif Cnt == (15 + L_LickP) and L_SEXP >= 15 and not ApprovalCheck("Laura", 1500):
                    $ L_Brows = "confused"        
                    menu:
                        ch_l "Maybe change things up a little?"                       
                        "Finish up.":
                                "You let go. . ."   
                                jump L_LP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump L_LP_After
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
                                    ch_l "I'm kinda bored here."                         
                                    call Statup("Laura", "Love", 50, -3, 1)
                                    call Statup("Laura", "Love", 80, -4, 1)
                                    call Statup("Laura", "Obed", 30, -1, 1)                    
                                    call Statup("Laura", "Obed", 50, -1, 1)  
                                    $ L_RecentActions.append("angry")
                                    $ L_DailyActions.append("angry")   
                                    jump L_LP_After
        #End Count check
           
        if Round == 10:
            ch_l "It's getting late, we should wrap this up."  
        elif Round == 5:
            ch_l "Tic tock, [L_Petname]."        
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, [L_Petname], breaktime."
    
    
label L_LP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call L_Pos_Reset
        
    call LauraFace("sexy") 
    
    $ L_LickP += 1  
    $ L_Action -=1     
    if L_Legs != "pants" or L_Upskirt:        
        $ L_Addictionrate += 1
        if "addictive" in P_Traits:
            $ L_Addictionrate += 1
    
    if Partner == "Rogue":
        call Partner_Like("Laura",3,2)
    else:
        call Partner_Like("Laura",2)
     
    if L_LickP == 1:            
            $ L_SEXP += 10         
            if not Situation: 
                if L_Love >= 500 and "unsatisfied" not in L_RecentActions:
                    ch_l "That was a really good use of that tongue of yours."
                elif L_Obed <= 500 and P_Focus <= 20:
                    call LauraFace("perplexed", 1)
                    ch_l "I suppose we both got something out of that. . ."
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Oh? What did you have in mind?"
    call Checkout
    return   


# end L_Lick Pussy /////////////////////////////////////////////////////////////////////////////

    
# ////////////////////////////////////////////////////////////////////////Start Fondle Ass    
label L_Fondle_Ass: 
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
                                                                                     # Will she let you fondle? Modifiers
    if L_FondleA: #You've done it before
        $ Tempmod += 10
    if L_Legs == "pants" or HoseNum("Laura") >= 5: # she's got pants on.
        $ Tempmod -= 5     
    if L_Lust > 75: #She's really horny
        $ Tempmod += 15
    if "exhibitionist" in L_Traits:
        $ Tempmod += Taboo  
    if "dating" in L_Traits or "sex friend" in L_Petnames:
        $ Tempmod += 10
    elif "ex" in L_Traits:
        $ Tempmod -= 25 
    if L_ForcedCount and not L_Forced:
        $ Tempmod -= 5 * L_ForcedCount      
    
    if Taboo and "tabno" in L_DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in L_History:                   
        $ Tempmod -= 20 
        
    if "no fondle ass" in L_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle ass" in L_RecentActions else 0   
        
    $ Approval = ApprovalCheck("Laura", 850, TabM=1) # 85, 100, 115, Taboo -40(125)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:  
            call LauraFace("surprised", 1)  
            call Statup("Laura", "Obed", 70, 2)
            call Statup("Laura", "Inbt", 40, 2) 
            "As your hand creeps down her backside, Laura shivers a bit, and then relaxes."              
            call LauraFace("sexy")  
            jump L_FA_Prep  
        else:          
            call LauraFace("surprised")
            call Statup("Laura", "Obed", 50, -3)
            ch_l "Hands off, [L_Petname]."   
            call LauraFace("bemused")
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        call LauraFace("surprised")   
        $ L_Brows = "sad"        
        if L_Lust > 80:
            call Statup("Laura", "Love", 70, -4)
        call Statup("Laura", "Obed", 90, 1)
        call Statup("Laura", "Obed", 70, 2)
        "As your finger slides out, Laura gasps and looks upset."              
        jump L_FA_Prep     
    elif "fondle ass" in L_RecentActions:
        call LauraFace("sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump L_FA_Prep
    elif "fondle ass" in L_DailyActions:
        call LauraFace("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Mmm, you like that? . .",
            "Mmm. . ."]) 
        ch_l "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .        
        if L_Forced:
            call LauraFace("sad")
            call Statup("Laura", "Love", 70, -2, 1)
            call Statup("Laura", "Obed", 90, 2)
            call Statup("Laura", "Inbt", 60, 2)
            ch_l "If you insist. . ."   
        else:
            call LauraFace("bemused, 1") 
            ch_l "Yeah, ok. . ."   
        call Statup("Laura", "Lust", 200, 3)
        call Statup("Laura", "Obed", 60, 1)
        call Statup("Laura", "Inbt", 70, 1) 
        jump L_FA_Prep
        
    else:                                                                               #She's not into it, but maybe. . .            
        call LauraFace("angry", 1)
        if "no fondle ass" in L_RecentActions:  
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "tabno" in L_DailyActions and "no fondle ass" in L_DailyActions:  
            ch_l "I told you not to touch me like that in public!" 
        elif "no fondle ass" in L_DailyActions:       
            ch_l "Don't make me tell you again today."
        elif Taboo and "tabno" in L_DailyActions:  
            ch_l "I told you, not here, [L_Petname]."  
        elif not L_FondleA:
            call LauraFace("bemused")
            ch_l "Not yet, [L_Petname]. . ."
        else:
            call LauraFace("bemused")
            ch_l "Let's not, ok [L_Petname]?"
        menu:
            extend ""
            "Sorry, never mind." if "no fondle ass" in L_DailyActions:
                call LauraFace("bemused")
                ch_l "It's cool, [L_Petname]."              
                return
            "Maybe later?" if "no fondle ass" not in L_DailyActions:
                call LauraFace("sexy")  
                ch_l "Maybe?"
                call Statup("Laura", "Love", 80, 2)
                call Statup("Laura", "Inbt", 50, 2)  
                if Taboo:                    
                    $ L_RecentActions.append("tabno")                      
                    $ L_DailyActions.append("tabno") 
                $ L_RecentActions.append("no fondle ass")                      
                $ L_DailyActions.append("no fondle ass")            
                return
            "Just one good squeeze?":             
                if Approval:
                    call LauraFace("sexy")     
                    call Statup("Laura", "Obed", 90, 1)
                    call Statup("Laura", "Obed", 50, 2)
                    ch_l "Oooh, beg for me. . ."                           
                    call Statup("Laura", "Inbt", 70, 1) 
                    call Statup("Laura", "Inbt", 40, 2) 
                    jump L_FA_Prep
                else:   
                    call LauraFace("sexy") 
                    ch_l "No."     
            
            "[[Start fondling anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Laura", 250, "OI", TabM = 3) # 25, 40, 55, -120(145)
                if Approval > 1 or (Approval and L_Forced):
                    call LauraFace("sad")
                    call Statup("Laura", "Love", 70, -3, 1)
                    call Statup("Laura", "Love", 200, -1) 
                    ch_l "Fine, I guess."                
                    call Statup("Laura", "Obed", 50, 3)
                    call Statup("Laura", "Inbt", 60, 3) 
                    if Approval < 2:                          
                        $ L_Forced = 1
                    jump L_FA_Prep
                else:                              
                    call Statup("Laura", "Love", 200, -10)  
                    call LauraFace("angry", 1)
                    "She slaps your hand away."   
                    $ L_RecentActions.append("angry")
                    $ L_DailyActions.append("angry")   
                        
    if "no fondle ass" in L_DailyActions:
        ch_l "I don't like to repeat myself, [L_Petname]."   
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif L_Forced:
        call LauraFace("angry", 1)
        ch_l "Do you want to keep those fingers?"
        call Statup("Laura", "Lust", 60, 5)    
        call Statup("Laura", "Obed", 50, -2)   
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif Taboo:
        call LauraFace("angry", 1)    
        $ L_RecentActions.append("tabno")   
        $ L_DailyActions.append("tabno") 
        ch_l "I try to stay off the radar."                   
    elif L_FondleA:
        call LauraFace("sad")
        ch_l "Sorry, keep your hands to yourself."        
    else:
        call LauraFace("sexy") 
        $ L_Mouth = "sad"
        ch_l "No."
    $ L_RecentActions.append("no fondle ass")                      
    $ L_DailyActions.append("no fondle ass") 
    $ Tempmod = 0    
    return
        
ch_l "Sorry, I don't even know how I got here. . ."
return

label L_FA_Prep: #Animation set-up  
    if Trigger2 == "fondle ass":
        return
    if not L_Forced and Situation != "auto":
        $ Tempmod = 0
        call Laura_Bottoms_Off
        if "angry" in L_RecentActions:
            return    
    $ Tempmod = 0      
    call L_Pussy_Launch("fondle ass")
    if not L_FondleA:        
        if L_Forced:
            call Statup("Laura", "Love", 90, -20)
            call Statup("Laura", "Obed", 70, 20)
            call Statup("Laura", "Inbt", 80, 15) 
        else:
            call Statup("Laura", "Love", 90, 10)
            call Statup("Laura", "Obed", 70, 12)
            call Statup("Laura", "Inbt", 80, 20)
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
    call DrainWord("Laura","no fondle ass")
    $ L_RecentActions.append("fondle ass")                      
    $ L_DailyActions.append("fondle ass") 
    
label L_FA_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Laura") 
        call L_Pussy_Launch("fondle ass")
        call LauraLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                                              
                        "Slap her ass":                     
                                    call L_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump L_FA_Cycle  
                                    
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
                                                        "I want to stick a finger in.":
                                                                $ Situation = "shift"
                                                                call L_FA_After
                                                                call L_Insert_Ass    
                                                        "Just stick a finger in without asking.":
                                                                $ Situation = "auto"
                                                                call L_FA_After
                                                                call L_Insert_Ass
                                                        "I want to lick your asshole.":
                                                                $ Situation = "shift"
                                                                call L_FA_After
                                                                call L_Lick_Ass                 
                                                        "Just start licking.":
                                                                $ Situation = "auto"
                                                                call L_FA_After
                                                                call L_Lick_Ass    
                                                        "I want to stick a dildo in.":                                                                
                                                                $ Situation = "shift"
                                                                call L_FA_After
                                                                call L_Dildo_Ass  
                                                        "Never Mind":
                                                                jump L_FA_Cycle
                                            else: 
                                                ch_l "Maybe we could finish this up for now?"           
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call L_FA_After
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
                                                        jump L_FA_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump L_FA_Cycle 
                                            "Never mind":
                                                        jump L_FA_Cycle 
                                    "Undress Laura":
                                            call L_Undress   
                                    "Clean up Laura (locked)" if not L_Spunk:
                                            pass  
                                    "Clean up Laura" if L_Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump L_FA_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call L_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump L_FA_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call L_Pos_Reset
                                    $ Line = 0
                                    jump L_FA_After
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
                                jump L_FA_After 
                            $ Line = "came"
     
                    if L_Lust >= 100:  
                            #If Laura can cum                                             
                            call L_Cumming
                            if Situation == "shift" or "angry" in L_RecentActions:
                                jump L_FA_After
                       
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
                                            jump L_FA_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
                    
        if L_SEXP >= 100 or ApprovalCheck("Laura", 1200, "LO"):
            pass
        elif Cnt == (5 + L_FondleA):
                    $ L_Brows = "confused"
                    ch_l "Mmmm. . ."  
        elif L_Lust >= 80:
                    pass
        elif Cnt == (15 + L_FondleA) and L_SEXP >= 15 and not ApprovalCheck("Laura", 1500):
                    $ L_Brows = "confused"        
                    menu:
                        ch_l "Maybe change things up a little?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump L_FA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump L_FA_After
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
                                    ch_l "I'm kinda bored here."                         
                                    call Statup("Laura", "Love", 50, -3, 1)
                                    call Statup("Laura", "Love", 80, -4, 1)
                                    call Statup("Laura", "Obed", 30, -1, 1)                    
                                    call Statup("Laura", "Obed", 50, -1, 1)  
                                    $ L_RecentActions.append("angry")
                                    $ L_DailyActions.append("angry")   
                                    jump L_FA_After
        #End Count check
        
        if Round == 10:
            ch_l "It's getting late, we should wrap this up."  
        elif Round == 5:
            ch_l "Tic tock, [L_Petname]."        
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, [L_Petname], breaktime."
    
    
label L_FA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call L_Pos_Reset
        
    call LauraFace("sexy") 
    
    $ L_FondleA += 1  
    $ L_Action -=1            
    if L_Legs != "pants" or L_Upskirt:        
        $ L_Addictionrate += 1
        if "addictive" in P_Traits:
            $ L_Addictionrate += 1
    
        call Partner_Like("Laura",2)
     
    if L_FondleA == 1:            
            $ L_SEXP += 4         
            if not Situation: 
                if L_Love >= 500 and "unsatisfied" not in L_RecentActions:
                    ch_l "That was. . . nice. . ."
                elif L_Obed <= 500 and P_Focus <= 20:
                    call LauraFace("perplexed", 1)
                    ch_l "Did you enjoy that?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Oh? What did you have in mind?"
    call Checkout
    return   


# end L_Fondle Ass /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Ass    
label L_Insert_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
    
    if L_InsertA: #You've done it before
        $ Tempmod += 25
    if L_Legs == "pants" or HoseNum("Laura") >= 5: # she's got pants on.
        $ Tempmod -= 15    
    if L_Lust > 85: #She's really horny
        $ Tempmod += 15
    if L_Lust > 95:
        $ Tempmod += 5
    if Situation == "shift":
        $ Tempmod += 10
    if L_Lust > 85 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in L_Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in L_Traits or "sex friend" in L_Petnames:
        $ Tempmod += 10
    elif "ex" in L_Traits:
        $ Tempmod -= 25 
    if L_ForcedCount and not L_Forced:
        $ Tempmod -= 5 * L_ForcedCount
    
    if Taboo and "tabno" in L_DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in L_History:                   
        $ Tempmod -= 20 
        
    if "no insert ass" in L_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no insert ass" in L_RecentActions else 0   
            
    $ Approval = ApprovalCheck("Laura", 1300, TabM = 3) # 130, 145, 160, Taboo -120(250)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            call LauraFace("surprised")
            call Statup("Laura", "Obed", 90, 2)
            call Statup("Laura", "Obed", 70, 2)
            call Statup("Laura", "Inbt", 80, 2) 
            call Statup("Laura", "Inbt", 30, 2) 
            "As you slide a finger in, Laura tightens around it in surprise, but seems into it."  
            call LauraFace("sexy")           
            jump L_IA_Prep
        else:   
            call LauraFace("surprised")
            call Statup("Laura", "Love", 80, -2)
            call Statup("Laura", "Obed", 50, -3)
            ch_l "Whoa, back off, [L_Petname]."                 
            $ Tempmod = 0
            $ Trigger2 = 0
            return          
    
    if "insert ass" in L_DailyActions:
        call LauraFace("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Chill. . .",
            "Mmm. . ."]) 
        ch_l "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .               
        if L_Forced:
            call LauraFace("sad")
            call Statup("Laura", "Love", 70, -3, 1)
            call Statup("Laura", "Love", 20, -2, 1)
            call Statup("Laura", "Obed", 90, 1)
            call Statup("Laura", "Inbt", 60, 1)
            ch_l "If you must. . ."    
        else:
            call LauraFace("sexy", 1)
            $ L_Eyes = "closed"            
            call Statup("Laura", "Love", 90, 1)
            call Statup("Laura", "Inbt", 50, 3)            
            call Statup("Laura", "Lust", 200, 3)
            ch_l "Mmmmm. . ."                
        call Statup("Laura", "Obed", 20, 1)
        call Statup("Laura", "Obed", 60, 1)
        call Statup("Laura", "Inbt", 70, 2) 
        jump L_IA_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call LauraFace("angry", 1)
        if "no insert ass" in L_RecentActions:  
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "tabno" in L_DailyActions and "no insert ass" in L_DailyActions:  
            ch_l "I told you that wasn't appropriate!" 
        elif "no insert ass" in L_DailyActions:       
            ch_l "Don't make me tell you again today."
        elif Taboo and "tabno" in L_DailyActions:  
            ch_l "I told you, not here, [L_Petname]."  
        elif not L_InsertA:
            call LauraFace("perplexed", 1)
            ch_l "That's really not my style. . ."
        else:
            call LauraFace("bemused")
            ch_l "I'd rather not today. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no insert ass" in L_DailyActions:
                call LauraFace("bemused")
                ch_l "It's cool, [L_Petname]."              
                return
            "Maybe later?" if "no insert ass" not in L_DailyActions:
                call LauraFace("sexy")  
                ch_l "It's. . . possible, [L_Petname]."
                call Statup("Laura", "Love", 80, 2)
                call Statup("Laura", "Inbt", 70, 2)   
                if Taboo:                    
                    $ L_RecentActions.append("tabno")                      
                    $ L_DailyActions.append("tabno") 
                $ L_RecentActions.append("no insert ass")                      
                $ L_DailyActions.append("no insert ass")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    call LauraFace("sexy")           
                    call Statup("Laura", "Obed", 90, 2)
                    call Statup("Laura", "Obed", 50, 2)
                    ch_l "You're probably right. . ."      
                    call Statup("Laura", "Inbt", 70, 3) 
                    call Statup("Laura", "Inbt", 40, 2)
                    jump L_IA_Prep
                else:   
                    call LauraFace("bemused") 
                    ch_l "I don't think that I would."     
            
            "[[Slide a finger in anyway]":                                               # Pressured into being fingered. 
                $ Approval = ApprovalCheck("Laura", 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                if Approval > 1 or (Approval and L_Forced):                    
                    call LauraFace("surprised", 1)
                    call Statup("Laura", "Love", 70, -5, 1)
                    call Statup("Laura", "Love", 200, -2)                 
                    ch_l "Well hello there. . ."                     
                    call LauraFace("sad")
                    call Statup("Laura", "Obed", 50, 4)
                    call Statup("Laura", "Inbt", 80, 1) 
                    call Statup("Laura", "Inbt", 60, 3)  
                    if Approval < 2:                          
                        $ L_Forced = 1
                    jump L_IA_Prep
                else:                              
                    call Statup("Laura", "Love", 200, -15)  
                    call LauraFace("angry", 1)
                    "She slaps your hand away."   
                    $ L_RecentActions.append("angry")
                    $ L_DailyActions.append("angry")   
                    
    if "no insert ass" in L_DailyActions:
        ch_l "I don't like to repeat myself, [L_Petname]."   
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif L_Forced:
        call LauraFace("angry", 1)
        ch_l "I'm not going there today."
        if L_Inbt > 50:
                call Statup("Laura", "Lust", 80, 10)  
        else:
                call Statup("Laura", "Lust", 50, 3)
        call Statup("Laura", "Obed", 50, -2)      
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif Taboo:
        call LauraFace("angry", 1)    
        $ L_RecentActions.append("tabno")                   
        $ L_DailyActions.append("tabno") 
        ch_l "I try to stay off the radar."                   
    elif L_InsertA:
        call LauraFace("sad") 
        ch_l "I don't feel like it."    
    else:
        call LauraFace("surprised")
        ch_l "Not today, [L_Petname]."
        call LauraFace
    $ L_RecentActions.append("no insert ass")                      
    $ L_DailyActions.append("no insert ass") 
    $ Tempmod = 0    
    return
    
        
label L_IA_Prep: #Animation set-up 
    if Trigger2 == "insert ass":
        return
        
    if not L_Forced and Situation != "auto":
        $ Tempmod = 0
        call Laura_Bottoms_Off
        if "angry" in L_RecentActions:
            return    
            
    $ Tempmod = 0      
    call L_Pussy_Launch("insert ass")
    if not L_InsertA:        
        if L_Forced:
            call Statup("Laura", "Love", 90, -50)
            call Statup("Laura", "Obed", 70, 60)
            call Statup("Laura", "Inbt", 80, 35) 
        else:
            call Statup("Laura", "Love", 90, 10)
            call Statup("Laura", "Obed", 70, 20)
            call Statup("Laura", "Inbt", 80, 25)
            
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
    call DrainWord("Laura","no insert ass")
    $ L_RecentActions.append("insert ass")                      
    $ L_DailyActions.append("insert ass") 
    
label L_IA_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Laura") 
        call L_Pussy_Launch("insert ass")
        call LauraLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                                              
                        "Slap her ass":                     
                                    call L_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump L_IA_Cycle  
                                    
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
                                                        "Pull out and start rubbing again.":
                                                                $ Situation = "pullback"
                                                                call L_IA_After
                                                                call L_Fondle_Ass
                                                        "I want to lick your asshole.":
                                                                $ Situation = "shift"
                                                                call L_IA_After
                                                                call L_Lick_Ass                 
                                                        "Just start licking.":
                                                                $ Situation = "auto"
                                                                call L_IA_After
                                                                call L_Lick_Ass    
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call L_IA_After
                                                                call L_Dildo_Ass  
                                                        "Never Mind":
                                                                jump L_IA_Cycle
                                            else: 
                                                ch_l "Maybe we could finish this up for now?"           
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call L_IA_After
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
                                                        jump L_IA_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump L_IA_Cycle 
                                            "Never mind":
                                                        jump L_IA_Cycle 
                                    "Undress Laura":
                                            call L_Undress   
                                    "Clean up Laura (locked)" if not L_Spunk:
                                            pass  
                                    "Clean up Laura" if L_Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump L_IA_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call L_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump L_IA_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call L_Pos_Reset
                                    $ Line = 0
                                    jump L_IA_After
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
                                jump L_IA_After 
                            $ Line = "came"
     
                    if L_Lust >= 100:  
                            #If Laura can cum                                             
                            call L_Cumming
                            if Situation == "shift" or "angry" in L_RecentActions:
                                jump L_IA_After
                       
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
                                            jump L_IA_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if L_SEXP >= 100 or ApprovalCheck("Laura", 1200, "LO"):
            pass
        elif Cnt == (5 + L_InsertA):
                    $ L_Brows = "confused"
                    ch_l "Ungh, you're really getting in there. . ."  
        elif L_Lust >= 80:
                    pass
        elif Cnt == (15 + L_InsertA) and L_SEXP >= 15 and not ApprovalCheck("Laura", 1500):
                    $ L_Brows = "confused"        
                    menu:
                        ch_l "Maybe change things up a little?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump L_IA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump L_IA_After
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
                                    ch_l "I'm kinda bored here."                         
                                    call Statup("Laura", "Love", 50, -3, 1)
                                    call Statup("Laura", "Love", 80, -4, 1)
                                    call Statup("Laura", "Obed", 30, -1, 1)                    
                                    call Statup("Laura", "Obed", 50, -1, 1)  
                                    $ L_RecentActions.append("angry")
                                    $ L_DailyActions.append("angry")   
                                    jump L_IA_After
        #End Count check
           
        if Round == 10:
            ch_l "It's getting late, we should wrap this up."  
        elif Round == 5:
            ch_l "Tic tock, [L_Petname]."        
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, [L_Petname], breaktime."
    
label L_IA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call L_Pos_Reset
        
    call LauraFace("sexy") 
    
    $ L_InsertA += 1  
    $ L_Action -=1            
    $ L_Addictionrate += 1
    if "addictive" in P_Traits:
        $ L_Addictionrate += 1
    
    call Partner_Like("Laura",2)
     
    if L_InsertA == 1:            
            $ L_SEXP += 12         
            if not Situation: 
                if L_Love >= 500 and "unsatisfied" not in L_RecentActions:
                    ch_l "That was kinda wild. . ."
                elif L_Obed <= 500 and P_Focus <= 20:
                    call LauraFace("perplexed", 1)
                    ch_l "Did you enjoy that?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Oh? What did you have in mind?"
    call Checkout
    return   


# end L_Insert Ass /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Ass    
label L_Lick_Ass: 
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
                                                                             # Will she let you lick? Modifiers         
    if L_LickA: #You've done it before
        $ Tempmod += 20
    if L_Legs == "pants" or HoseNum("Laura") >= 5: # she's got pants on.
        $ Tempmod -= 25 
    if L_Lust > 95:
        $ Tempmod += 20  
    elif L_Lust > 85: #She's really horny
        $ Tempmod += 15    
    if L_Lust > 85 and Situation == "auto": #auto
        $ Tempmod += 10 
    if Situation == "shift":
        $ Tempmod += 10
    if "exhibitionist" in L_Traits:
        $ Tempmod += (4*Taboo) 
    if "dating" in L_Traits or "sex friend" in L_Petnames:
        $ Tempmod += 10
    elif "ex" in L_Traits:
        $ Tempmod -= 25  
    if L_ForcedCount and not L_Forced:
        $ Tempmod -= 5 * L_ForcedCount 
    
    if Taboo and "tabno" in L_DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in L_History:                   
        $ Tempmod -= 20 
        
    if "no lick ass" in L_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no lick ass" in L_RecentActions else 0   
            
    $ Approval = ApprovalCheck("Laura", 1550, TabM = 4) # 155, 170, 185, Taboo -160(315)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            call LauraFace("surprised")   
            call Statup("Laura", "Obed", 90, 1)
            call Statup("Laura", "Inbt", 80, 3) 
            call Statup("Laura", "Inbt", 40, 2) 
            "As you crouch down and start to lick her asshole, Laura startles briefly, but then begins to melt."  
            call LauraFace("sexy")  
            jump L_LA_Prep
        else:   
            call LauraFace("surprised")
            call Statup("Laura", "Love", 80, -2)
            call Statup("Laura", "Obed", 50, -3)
            ch_l "[L_Petname]! No. . ."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return  
    
    if "lick ass" in L_RecentActions:
        call LauraFace("sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump L_LA_Prep
    elif "lick ass" in L_DailyActions:
        call LauraFace("sexy", 1)
        ch_l "You didn't get enough earlier?"
    
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if L_Forced:
            call LauraFace("sad")
            call Statup("Laura", "Love", 70, -3, 1)
            call Statup("Laura", "Love", 20, -2, 1)
            call Statup("Laura", "Obed", 90, 2)
            call Statup("Laura", "Inbt", 60, 2)
            ch_l "Meh. . ."    
        else:
            call LauraFace("sexy", 1)
            $ L_Eyes = "closed"            
            call Statup("Laura", "Love", 90, 1)
            call Statup("Laura", "Inbt", 60, 2)            
            call Statup("Laura", "Lust", 200, 3)
            ch_l "Mmm. . . naughty."                
        call Statup("Laura", "Obed", 20, 1)
        call Statup("Laura", "Obed", 60, 1)
        call Statup("Laura", "Inbt", 80, 2) 
        jump L_LA_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .           
        call LauraFace("angry", 1)
        if "no lick ass" in L_RecentActions:  
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "tabno" in L_DailyActions and "no lick ass" in L_DailyActions:  
            ch_l "I told you not to touch me like that in public!" 
        elif "no lick ass" in L_DailyActions:       
            ch_l "Don't make me tell you again today."
        elif Taboo and "tabno" in L_DailyActions:  
            ch_l "I told you, not here, [L_Petname]."  
        elif not L_LickA:                    #First time dialog
            call LauraFace("bemused", 1)
            if L_Love >= L_Obed and L_Love >= L_Inbt:            
                ch_l "Oh, we're there now?"
            elif L_Obed >= L_Inbt:            
                ch_l "Is that what gets you off?"
            else:
                $ L_Eyes = "sexy"
                ch_l "Hm, I didn't know that's what you were into."
        else:
            call LauraFace("bemused")
            ch_l "Not now, [L_Petname]."  
        menu:
            extend ""
            "Sorry, never mind." if "no lick ass" in L_DailyActions:
                call LauraFace("bemused")
                ch_l "It's cool, [L_Petname]."              
                return
            "I'm sure I can convince you later. . ." if "no lick ass" not in L_DailyActions:
                call LauraFace("sexy")  
                ch_l "Anything's possible, [L_Petname]."
                call Statup("Laura", "Love", 80, 2)
                call Statup("Laura", "Inbt", 70, 2)   
                if Taboo:                    
                    $ L_RecentActions.append("tabno")                      
                    $ L_DailyActions.append("tabno") 
                $ L_RecentActions.append("no lick ass")                      
                $ L_DailyActions.append("no lick ass")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    call LauraFace("sexy")           
                    call Statup("Laura", "Obed", 90, 2)
                    call Statup("Laura", "Obed", 50, 2)
                    ch_l "Ok, you're probably right. . ."      
                    call Statup("Laura", "Inbt", 70, 3) 
                    call Statup("Laura", "Inbt", 40, 2)
                    jump L_LA_Prep
                else:   
                    call LauraFace("sexy") 
                    ch_l "I really don't think so."        
            
            "[[Start licking anyway]":                                               # Pressured into being licked. 
                $ Approval = ApprovalCheck("Laura", 1100, "OI", TabM = 4) # 110, 125, 140, -160(270)
                if Approval > 1 or (Approval and L_Forced):
                    call LauraFace("sad")
                    call Statup("Laura", "Love", 70, -5, 1)
                    call Statup("Laura", "Love", 200, -2)                 
                    ch_l "Suit yourself."  
                    call Statup("Laura", "Obed", 50, 4)
                    call Statup("Laura", "Inbt", 80, 1) 
                    call Statup("Laura", "Inbt", 60, 3)  
                    if Approval < 2:                          
                        $ L_Forced = 1
                    jump L_LA_Prep
                else:                              
                    call Statup("Laura", "Love", 200, -15)  
                    call LauraFace("angry", 1)
                    "She shoves your head back."   
                    $ L_RecentActions.append("angry")
                    $ L_DailyActions.append("angry")   
                    
    if "no lick ass" in L_DailyActions:
        ch_l "I don't like to repeat myself, [L_Petname]."   
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif L_Forced:
        call LauraFace("angry", 1)
        ch_l "I don't think so."
        if L_Inbt > 50:
                call Statup("Laura", "Lust", 80, 10)  
        else:
                call Statup("Laura", "Lust", 50, 3)
        call Statup("Laura", "Obed", 50, -2)   
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    elif Taboo:
        call LauraFace("angry", 1)    
        $ L_RecentActions.append("tabno")                   
        $ L_DailyActions.append("tabno") 
        ch_l "I try to stay off the radar."                   
    elif L_LickA:
        call LauraFace("sad") 
        ch_l "Sorry, no more of that."    
    else:
        call LauraFace("surprised")
        ch_l "I'm sorry, not now."
        call LauraFace
    $ L_RecentActions.append("no lick ass")                      
    $ L_DailyActions.append("no lick ass") 
    $ Tempmod = 0    
    return
        
label L_LA_Prep: #Animation set-up  
    if Trigger2 == "lick ass":
        return
    if not L_Forced and Situation != "auto":
        $ Tempmod = 0
        if L_Legs == "pants":
            $ Tempmod = 15
        call Laura_Bottoms_Off
        if "angry" in L_RecentActions:
            return    
    $ Tempmod = 0  
    call L_Pussy_Launch("lick ass")
    if not L_LickA:        
        if L_Forced:
            call Statup("Laura", "Love", 90, -30)
            call Statup("Laura", "Obed", 70, 40)
            call Statup("Laura", "Inbt", 80, 80) 
        else:
            call Statup("Laura", "Love", 90, 35)
            call Statup("Laura", "Obed", 70, 25)
            call Statup("Laura", "Inbt", 80, 55)
    if Taboo:
        $ L_Inbt += int(Taboo/10)  
        $ L_Lust += int(Taboo/5)
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    
    $ L_Upskirt = 1
    if L_Legs == "skirt":
        $ L_SeenPanties = 1
    if not L_Panties:
        call Laura_First_Bottomless(1)
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Laura","tabno")
    call DrainWord("Laura","no lick ass")
    
    $ L_RecentActions.append("lick") if "lick" not in L_RecentActions else L_RecentActions
    $ L_RecentActions.append("ass") if "ass" not in L_RecentActions else L_RecentActions
    $ L_RecentActions.append("lick ass")  
    
    $ L_DailyActions.append("lick") if "lick" not in L_DailyActions else L_RecentActions
    $ L_DailyActions.append("ass") if "ass" not in L_DailyActions else L_RecentActions                    
    $ L_DailyActions.append("lick ass")  
label L_LA_Cycle: #Repeating strokes
    if Trigger2 == "kiss you":
            $ Trigger2 = 0
    while Round >=0:  
        call Shift_Focus("Laura") 
        call L_Pussy_Launch("lick ass")
        call LauraLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                                              
                        "Slap her ass":                     
                                    call L_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump L_LA_Cycle  
                                    
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
                                                        "Switch to fondling.":
                                                                $ Situation = "pullback"
                                                                call L_LA_After
                                                                call L_Fondle_Ass
                                                        "I want to stick a finger in.":
                                                                $ Situation = "shift"
                                                                call L_LA_After
                                                                call L_Insert_Ass                 
                                                        "Just stick a finger in [[without asking].":
                                                                $ Situation = "auto"
                                                                call L_LA_After
                                                                call L_Insert_Ass                        
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call L_LA_After
                                                                call L_Dildo_Ass  
                                                        "Never Mind":
                                                                jump L_LA_Cycle
                                            else: 
                                                ch_l "Maybe we could finish this up for now?"           
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call L_LA_After
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
                                                        jump L_LA_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump L_LA_Cycle 
                                            "Never mind":
                                                        jump L_LA_Cycle 
                                    "Undress Laura":
                                            call L_Undress   
                                    "Clean up Laura (locked)" if not L_Spunk:
                                            pass  
                                    "Clean up Laura" if L_Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump L_LA_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call L_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump L_LA_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call L_Pos_Reset
                                    $ Line = 0
                                    jump L_LA_After
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
                                jump L_LA_After 
                            $ Line = "came"
     
                    if L_Lust >= 100:  
                            #If Laura can cum                                             
                            call L_Cumming
                            if Situation == "shift" or "angry" in L_RecentActions:
                                jump L_LA_After
                       
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
                                            jump L_LA_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
                    
        if L_SEXP >= 100 or ApprovalCheck("Laura", 1200, "LO"):
            pass
        elif Cnt == (5 + L_LickA):
                    $ L_Brows = "confused"
                    ch_l "You seem to be enjoying yourself. . ."  
        elif L_Lust >= 80:
                    pass
        elif Cnt == (15 + L_LickA) and L_SEXP >= 15 and not ApprovalCheck("Laura", 1500):
                    $ L_Brows = "confused"        
                    menu:
                        ch_l "[L_Petname], could we try something different?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump L_LA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump L_LA_After
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
                                    ch_l "I'm kinda bored here."                         
                                    call Statup("Laura", "Love", 50, -3, 1)
                                    call Statup("Laura", "Love", 80, -4, 1)
                                    call Statup("Laura", "Obed", 30, -1, 1)                    
                                    call Statup("Laura", "Obed", 50, -1, 1)  
                                    $ L_RecentActions.append("angry")
                                    $ L_DailyActions.append("angry")   
                                    jump L_LA_After
        #End Count check
           
        if Round == 10:
            ch_l "It's getting late, we should wrap this up."  
        elif Round == 5:
            ch_l "Tic tock, [L_Petname]."        
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, [L_Petname], breaktime."
    
label L_LA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call L_Pos_Reset
        
    call LauraFace("sexy") 
    
    $ L_LickA += 1  
    $ L_Action -=1      
    if L_Legs != "pants" or L_Upskirt:        
        $ L_Addictionrate += 1
        if "addictive" in P_Traits:
            $ L_Addictionrate += 1
    
    call Partner_Like("Laura",2)
     
    if L_LickA == 1:            
            $ L_SEXP += 15         
            if not Situation: 
                if L_Love >= 500 and "unsatisfied" not in L_RecentActions:
                    ch_l "That was. . . interesting."
                elif L_Obed <= 500 and P_Focus <= 20:
                    call LauraFace("perplexed", 1)
                    ch_l "Was that good for you?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Oh? What did you have in mind?"
    call Checkout
    return   

# end L_Lick Ass /////////////////////////////////////////////////////////////////////////////

