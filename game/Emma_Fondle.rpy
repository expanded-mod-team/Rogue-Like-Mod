# EmmaX.Fondle /////////////////////////////////////////////////////////////////////////////
label Emma_Fondle:
    
    $ EmmaX.Mouth = "smile"
    if not EmmaX.Action:
        ch_e "I'm rather tired right now, [EmmaX.Petname], raincheck?"
        return
    menu:
        ch_e "Well? Where did you want to touch, [EmmaX.Petname]?"
        "Your breasts?" if EmmaX.Action:
                jump Emma_Fondle_Breasts
        "Your thighs?" if EmmaX.Action:
                jump Emma_Fondle_Thighs
        "Your pussy?" if EmmaX.Action:
                jump Emma_Fondle_Pussy
        "Your Ass?" if EmmaX.Action:
                jump Emma_Fondle_Ass
        "Never mind.":
                return
    return


# EmmaX.Fondle Breasts /////////////////////////////////////////////////////////////////////////////
label Emma_Fondle_Breasts:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(EmmaX)
    
    # Will she let you fondle? Modifiers
    if EmmaX.FondleB: #You've done it before
        $ Tempmod += 15
    if EmmaX.Lust > 75: #She's really horny
        $ Tempmod += 20
    if "exhibitionist" in EmmaX.Traits:
        $ Tempmod += (3*Taboo)
    if "dating" in EmmaX.Traits or "sex friend" in EmmaX.Petnames:
        $ Tempmod += 10
    elif "ex" in EmmaX.Traits:
        $ Tempmod -= 20
    if EmmaX.ForcedCount and not EmmaX.Forced:
        $ Tempmod -= 5 * EmmaX.ForcedCount
    
    if Taboo and "tabno" in EmmaX.DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in EmmaX.History:                   
        $ Tempmod -= 20 
        
    if "no fondle breasts" in EmmaX.DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle breasts" in EmmaX.RecentActions else 0        
        
    $ Approval = ApprovalCheck(EmmaX, 950, TabM = 3) # 95, 110, 125 -120(215)
    
    if Situation == "auto":  
        if Approval:
            $ EmmaX.FaceChange("sexy")       
            $ EmmaX.Statup("Obed", 90, 1)
            $ EmmaX.Statup("Obed", 70, 2)
            $ EmmaX.Statup("Inbt", 70, 3)
            $ EmmaX.Statup("Inbt", 30, 2)            
            "As you cup her breast, [EmmaX.Name] gently nods."            
            jump Emma_FB_Prep        
        else:   
            $ EmmaX.FaceChange("surprised")
            $ EmmaX.Brows = "confused"
            $ EmmaX.Statup("Obed", 50, -2)
            ch_e "Down boy, you were doing so well. . ."
            $ Tempmod = 0
            $ Trigger2 = 0
            return
                    
    # fondle yes:    
    
    if Approval:                                                                       #Second time+ dialog        
        $ EmmaX.FaceChange("sexy", 1)
        if EmmaX.Forced: 
            $ EmmaX.FaceChange("sad")
            $ EmmaX.Statup("Love", 70, -3, 1)
            $ EmmaX.Statup("Love", 20, -2, 1)           
        elif not Taboo and "tabno" in EmmaX.DailyActions:        
            ch_e "This does seem less. . . exposed."   
            
    if "fondle breasts" in EmmaX.RecentActions:
        $ EmmaX.FaceChange("sexy", 1)
        ch_e "Mmmm, again? I suppose. . ."
        jump Emma_FB_Prep
    elif "fondle breasts" in EmmaX.DailyActions:
        $ EmmaX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax, gently. . .",
            "Mmm. . ."]) 
        ch_e "[Line]"
            
    if Approval >= 2:             
        $ EmmaX.FaceChange("bemused", 1)
        if EmmaX.Forced:
            $ EmmaX.FaceChange("sad")
            $ EmmaX.Statup("Love", 70, -3, 1)
            $ EmmaX.Statup("Love", 20, -2, 1)
            $ EmmaX.Statup("Obed", 90, 1)
            $ EmmaX.Statup("Inbt", 60, 1)
        ch_e "That sounds lovely, ravish me."   
        $ EmmaX.Statup("Love", 90, 1)
        $ EmmaX.Statup("Inbt", 50, 3) 
        jump Emma_FB_Prep
        
    else:
        $ EmmaX.FaceChange("angry", 1)
        if "no fondle breasts" in EmmaX.RecentActions:  
            ch_e "Your persistance is doing you no favors, [EmmaX.Petname]."
        elif Taboo and "tabno" in EmmaX.DailyActions and "no fondle breasts" in EmmaX.DailyActions:  
            ch_e "You've been warned." 
        elif "no fondle breasts" in EmmaX.DailyActions:       
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "tabno" in EmmaX.DailyActions:  
            ch_e "As I said, not here, [EmmaX.Petname]."  
        elif not EmmaX.FondleB:
            $ EmmaX.FaceChange("bemused")
            ch_e "I highly doubt you could handle them, [EmmaX.Petname]. . ."
        else:
            $ EmmaX.FaceChange("bemused")
            ch_e "You wish."   
        menu:
            extend ""
            "Sorry, never mind." if "no fondle breasts" in EmmaX.DailyActions:
                $ EmmaX.FaceChange("bemused")
                ch_e "Don't concern yourself, [EmmaX.Petname]."              
                return
            "Maybe later?" if "no fondle breasts" not in EmmaX.DailyActions:
                $ EmmaX.FaceChange("sexy")  
                "She re-adjusts her cleavage."
                ch_e "Well, I can't rule it out. . ."
                $ EmmaX.Statup("Love", 80, 1)
                $ EmmaX.Statup("Love", 50, 1)
                $ EmmaX.Statup("Inbt", 30, 2)    
                if Taboo:                    
                    $ EmmaX.RecentActions.append("tabno")                      
                    $ EmmaX.DailyActions.append("tabno") 
                $ EmmaX.RecentActions.append("no fondle breasts")                      
                $ EmmaX.DailyActions.append("no fondle breasts")            
                return                
            "Come on, Please?":             
                if Approval:
                    $ EmmaX.FaceChange("sexy")     
                    $ EmmaX.Statup("Obed", 90, 1)
                    $ EmmaX.Statup("Obed", 50, 2)
                    $ EmmaX.Statup("Inbt", 60, 3)
                    $ EmmaX.Statup("Inbt", 30, 2)
                    ch_e "Politeness can be rewarded. . ."                
                    jump Emma_FB_Prep
                else:   
                    $ EmmaX.FaceChange("sexy") 
                    ch_e "This wasn't a \"tone\" issue." 
            
            
            "[[Grab her chest anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck(EmmaX, 350, "OI", TabM = 3) # 35, 50, 65
                if Approval > 1 or (Approval and EmmaX.Forced):
                    $ EmmaX.FaceChange("sad")
                    $ EmmaX.Statup("Love", 70, -5, 1)
                    $ EmmaX.Statup("Love", 20, -2, 1)                 
                    ch_e "That is not appropriate. . ."
                    ch_e "but neither is it entirely unwelcome. . ."
                    $ EmmaX.Statup("Obed", 90, 2)
                    $ EmmaX.Statup("Obed", 50, 4)
                    $ EmmaX.Statup("Inbt", 60, 3)   
                    if Approval < 2:                          
                        $ EmmaX.Forced = 1
                    jump Emma_FB_Prep
                else:                              
                    $ EmmaX.Statup("Love", 200, -10)  
                    $ EmmaX.FaceChange("angry", 1)
                    "She slaps your hand away."   
                    $ EmmaX.RecentActions.append("angry")
                    $ EmmaX.DailyActions.append("angry")   
    
    if "no fondle breasts" in EmmaX.DailyActions:
        ch_e "You need to pay attention when I speak to you."   
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")   
    elif EmmaX.Forced:
        $ EmmaX.FaceChange("angry", 1)
        ch_e "Don't push your luck."
        $ EmmaX.Statup("Lust", 60, 5)    
        $ EmmaX.Statup("Obed", 50, -2)   
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")   
    elif Taboo:
        $ EmmaX.FaceChange("angry", 1)    
        $ EmmaX.RecentActions.append("tabno")                   
        $ EmmaX.DailyActions.append("tabno") 
        ch_e "I can't been seen doing that with you."                   
    elif EmmaX.FondleB:
        $ EmmaX.FaceChange("sad")
        ch_e "I'm afraid you haven't earned back my good graces."        
    else:
        $ EmmaX.FaceChange("sexy") 
        $ EmmaX.Mouth = "sad"
        ch_e "No."    
    $ EmmaX.RecentActions.append("no fondle breasts")                      
    $ EmmaX.DailyActions.append("no fondle breasts") 
    $ Tempmod = 0   
    return 
            
   
label Emma_FB_Prep: #Animation set-up 
    if Trigger == "kiss you": 
        $ Trigger = "fondle breasts" 
        return
        
    if Trigger2 == "fondle breasts": 
        return
            
    call Emma_Breasts_Launch("fondle breasts")
    
    if Situation == EmmaX:                                                                  
            #Emma auto-starts    
            $ Situation = 0
            if (EmmaX.Over or EmmaX.Chest) and not EmmaX.Uptop:
                #if she has some sort of top on. . .
                if ApprovalCheck(EmmaX, 1250, TabM = 1) or (EmmaX.SeenChest and ApprovalCheck(EmmaX, 500) and not Taboo):
                        $ EmmaX.Uptop = 1
                        $ Line = EmmaX.Over if EmmaX.Over else EmmaX.Chest
                        "With a devilish grin, [EmmaX.Name] pulls her [Line] up over her breasts."
                        call Emma_First_Topless(1)
                        $ Line = 0
                        "She then grabs your arm and mashes your hand against her breast, clearly intending you to get to work."
                else:
                        "[EmmaX.Name] grabs your arm and mashes your hand against her covered breast, clearly intending you to get to work."
            else:
                        "[EmmaX.Name] grabs your arm and mashes your hand against her breast, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":                    
                    $ EmmaX.Statup("Inbt", 80, 3) 
                    $ EmmaX.Statup("Inbt", 50, 2)
                    "You start to fondle it."
                "Praise her.":       
                    $ EmmaX.FaceChange("sexy", 1)                    
                    $ EmmaX.Statup("Inbt", 80, 3) 
                    ch_p "I like the initiative, [EmmaX.Pet]."
                    $ EmmaX.NameCheck() #checks reaction to petname
                    "You start to fondle it."
                    $ EmmaX.Statup("Love", 85, 1)
                    $ EmmaX.Statup("Obed", 90, 1)
                    $ EmmaX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your hand back."
                    $ EmmaX.FaceChange("surprised")       
                    $ EmmaX.Statup("Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [EmmaX.Pet]."
                    $ EmmaX.NameCheck() #checks reaction to petname
                    "[EmmaX.Name] pulls back."
                    $ EmmaX.Statup("Obed", 90, 1)
                    $ EmmaX.Statup("Obed", 50, 1)
                    $ EmmaX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")      
                    $ EmmaX.AddWord(1,"refused","refused")  
                    return          
            #end auto
            
    if not EmmaX.Forced and Situation != "auto":
        $ Tempmod = 0
        call Top_Off(EmmaX)
        if "angry" in EmmaX.RecentActions:
            return
    $ Tempmod = 0  
    if not EmmaX.FondleB:        
        if EmmaX.Forced:
            $ EmmaX.Statup("Love", 90, -20)
            $ EmmaX.Statup("Obed", 70, 25)
            $ EmmaX.Statup("Inbt", 80, 15) 
        else:
            $ EmmaX.Statup("Love", 90, 10)
            $ EmmaX.Statup("Obed", 70, 5)
            $ EmmaX.Statup("Inbt", 80, 15) 
            
    if Taboo:
        $ EmmaX.Inbt += int(Taboo/10)  
        $ EmmaX.Lust += int(Taboo/5)        
    
    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0  
    $ Cnt = 0     
    if Taboo:
        $ EmmaX.DrainWord("tabno")
    $ EmmaX.DrainWord("no fondle breasts")
    $ EmmaX.RecentActions.append("fondle breasts")                      
    $ EmmaX.DailyActions.append("fondle breasts") 
    
label Emma_FB_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus(EmmaX) 
        call Emma_Breasts_Launch("fondle breasts")
        $ EmmaX.LustFace()   
        
        if  Player.Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                         
                        "Slap her ass":                     
                                    call Slap_Ass(EmmaX)  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Emma_FB_Cycle  
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."                
                                    $ Player.FocusX = 0
                                    
                        "Other options":
                                menu:   
                                    "Offhand action":
                                            if EmmaX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ EmmaX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(EmmaX,"tired")   
                                                
                                    "Shift primary action":
                                            if EmmaX.Action and MultiAction:
                                                    menu:
                                                        "Ask to suck on them.":
                                                                if EmmaX.Action and MultiAction:                        
                                                                    $ Situation = "shift"
                                                                    call Emma_FB_After
                                                                    call Emma_Suck_Breasts
                                                                else:
                                                                    call Sex_Basic_Dialog(EmmaX,"tired") 
                                                        "Just suck on them without asking.":
                                                                if EmmaX.Action and MultiAction:                            
                                                                    $ Situation = "auto"
                                                                    call Emma_FB_After
                                                                    call Emma_Suck_Breasts
                                                                else:
                                                                    "As you lean in to suck on her breast, she grabs your head and pushes back."
                                                                    call Sex_Basic_Dialog(EmmaX,"tired") 
                                                        "Never Mind":
                                                                jump Emma_FB_Cycle
                                            else: 
                                                call Sex_Basic_Dialog(EmmaX,"tired") 
                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(EmmaX)
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(EmmaX) 
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0   
                                                        
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(EmmaX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_FB_Cycle 
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_FB_Cycle 
                                            "Never mind":
                                                        jump Emma_FB_Cycle 
                                    "Undress [EmmaX.Name]":
                                            call Girl_Undress(EmmaX)   
                                    "Clean up [EmmaX.Name] (locked)" if not EmmaX.Spunk:
                                            pass  
                                    "Clean up [EmmaX.Name]" if EmmaX.Spunk:
                                            call Girl_Cleanup(EmmaX,"ask")                                         
                                    "Never mind":
                                            jump Emma_FB_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Emma_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Emma_FB_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Emma_Pos_Reset
                                    $ Line = 0
                                    jump Emma_FB_After
        #End menu (if Line)
        
        call Shift_Focus(EmmaX)    
        call Sex_Dialog(EmmaX,Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or EmmaX.Lust >= 100: 
                    #If either of you could cum   
                    if Player.Focus >= 100:    
                            #If you can cum:                                                 
                            call Player_Cumming(EmmaX)
                            if "angry" in EmmaX.RecentActions:  
                                call Emma_Pos_Reset
                                return    
                            $ EmmaX.Statup("Lust", 200, 5) 
                            if 100 > EmmaX.Lust >= 70 and EmmaX.OCount < 2 and EmmaX.SEXP >= 20:             
                                $ EmmaX.RecentActions.append("unsatisfied")                      
                                $ EmmaX.DailyActions.append("unsatisfied") 
                            
                            if Player.Focus > 80:
                                jump Emma_FB_After 
                            $ Line = "came"
     
                    if EmmaX.Lust >= 100:  
                            #If [EmmaX.Name] can cum                                             
                            call Girl_Cumming(EmmaX)
                            if Situation == "shift" or "angry" in EmmaX.RecentActions:
                                jump Emma_FB_After
                       
                    if Line == "came": #ex Player.Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in EmmaX.RecentActions:#And [EmmaX.Name] is unsatisfied,  
                                "[EmmaX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Emma_FB_After    
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)            
        #End orgasm
        
        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0
        
        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif Cnt == (5 + EmmaX.FondleB):
                    $ EmmaX.Brows = "confused"
                    ch_e "They really are magnificent, aren't they?" 
        elif EmmaX.Lust >= 85:
                    pass  
        elif Cnt == (15 + EmmaX.FondleB) and EmmaX.SEXP >= 15 and not ApprovalCheck(EmmaX, 1500):
                    $ EmmaX.Brows = "confused" 
                    menu:
                        ch_e "Perhaps we could try something else, [EmmaX.Petname]?"
                        "Finish up.":
                                "You let go. . ."   
                                jump Emma_FB_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Emma_FB_After
                        "No, this is fun.":   
                                if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):                        
                                    $ EmmaX.Statup("Love", 200, -5)
                                    $ EmmaX.Statup("Obed", 50, 3)                    
                                    $ EmmaX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ EmmaX.FaceChange("angry", 1)   
                                    call Emma_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_e "You may be enjoying yourself, but I'm getting a bit sore."                         
                                    $ EmmaX.Statup("Love", 50, -3, 1)
                                    $ EmmaX.Statup("Love", 80, -4, 1)
                                    $ EmmaX.Statup("Obed", 30, -1, 1)                    
                                    $ EmmaX.Statup("Obed", 50, -1, 1)  
                                    $ EmmaX.RecentActions.append("angry")
                                    $ EmmaX.DailyActions.append("angry")   
                                    jump Emma_FB_After
        #End Count check
        
        call Escalation(EmmaX) #sees if she wants to escalate things
        
        if Round == 10:
            ch_e "It's getting late. . ."  
        elif Round == 5:
            ch_e "We should take a break soon."     
            
        if EmmaX.Lust >= 50 and not EmmaX.Uptop and (EmmaX.Chest or EmmaX.Over):
                $ EmmaX.Uptop = 1
                "[EmmaX.Name] sighs and tugs her breasts free of her clothes."      
                call Emma_First_Topless            
    
    #Round = 0 loop breaks
    $ EmmaX.FaceChange("bemused", 0)
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."
    
label Emma_FB_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Emma_Pos_Reset
        
    $ EmmaX.FaceChange("sexy") 
    
    $ EmmaX.FondleB += 1  
    $ EmmaX.Action -=1
    $ EmmaX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ EmmaX.Addictionrate += 1        
    
    call Partner_Like(EmmaX,2)
     
    if EmmaX.FondleB == 1:            
            $ EmmaX.SEXP += 4         
            if not Situation: 
                if EmmaX.Love >= 500 and "unsatisfied" not in EmmaX.RecentActions:
                    ch_e "I'm sure it exceeded your expectations. . ."
                elif EmmaX.Obed <= 500 and Player.Focus <= 20:
                    $ EmmaX.FaceChange("perplexed", 1)
                    ch_e "Well you certainly hit the jackpot."
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_e "Oh? What did you have in mind?"
    call Checkout
    return   

# End Fondle Breasts


# R Suck Breasts /////////////////////////////////////////////////////////////////////////////

label Emma_Suck_Breasts:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(EmmaX)
                                                                                        # Will she let you suck? Modifiers
    if EmmaX.SuckB: #You've done it before
        $ Tempmod += 15
    if not EmmaX.Chest and not EmmaX.Over:
        $ Tempmod += 15
    if EmmaX.Lust > 75: #She's really horny
        $ Tempmod += 20
    if EmmaX.Lust > 75 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in EmmaX.Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in EmmaX.Traits or "sex friend" in EmmaX.Petnames:
        $ Tempmod += 10
    elif "ex" in EmmaX.Traits:
        $ Tempmod -= 25  
    if EmmaX.ForcedCount and not EmmaX.Forced:
        $ Tempmod -= 5 * EmmaX.ForcedCount     
    
    if Taboo and "tabno" in EmmaX.DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in EmmaX.History:                   
        $ Tempmod -= 20 
        
    if "no suck breasts" in EmmaX.DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no suck breasts" in EmmaX.RecentActions else 0   
        
    $ Approval = ApprovalCheck(EmmaX, 1050, TabM = 4) # 105, 120, 135, Taboo -160(265)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ EmmaX.FaceChange("sexy")       
            $ EmmaX.Statup("Obed", 90, 1)
            $ EmmaX.Statup("Obed", 70, 2)
            $ EmmaX.Statup("Inbt", 70, 3)
            $ EmmaX.Statup("Inbt", 30, 2)            
            "As you dive in, [EmmaX.Name] seems a bit surprised, but just makes a little \"coo.\""              
            jump Emma_SB_Prep      
        else:               
            $ EmmaX.FaceChange("surprised")
            $ EmmaX.Statup("Obed", 50, -2)
            ch_e "Down boy, you were doing so well. . ."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
    
    if "suck breasts" in EmmaX.RecentActions:
        $ EmmaX.FaceChange("sexy", 1)
        ch_e "Mmmm, again? I suppose. . ."
        jump Emma_SB_Prep
    elif "suck breasts" in EmmaX.DailyActions:
        $ EmmaX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax, gently. . .",
            "Mmm. . ."]) 
        ch_e "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .
        $ EmmaX.FaceChange("bemused", 1)
        if EmmaX.Forced:
            $ EmmaX.FaceChange("sad")
            $ EmmaX.Statup("Love", 70, -3, 1)
            $ EmmaX.Statup("Love", 20, -2, 1)
            $ EmmaX.Statup("Obed", 90, 1)
            $ EmmaX.Statup("Inbt", 60, 1)
        ch_e "Oh very well. . ."   
        $ EmmaX.Statup("Love", 90, 1)
        $ EmmaX.Statup("Inbt", 50, 3) 
        jump Emma_SB_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        $ EmmaX.FaceChange("angry", 1)
        if "no suck breasts" in EmmaX.RecentActions:  
            ch_e "Your persistance is doing you no favors, [EmmaX.Petname]."
        elif Taboo and "tabno" in EmmaX.DailyActions and "no suck breasts" in EmmaX.DailyActions:  
            ch_e "I told you I couldn't be seen like that." 
        elif "no suck breasts" in EmmaX.DailyActions:       
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "tabno" in EmmaX.DailyActions:  
            ch_e "As I said, not here, [EmmaX.Petname]."  
        elif not EmmaX.SuckB:
            $ EmmaX.FaceChange("bemused")
            ch_e "Let's work up to that, perhaps. . ."
        else:
            $ EmmaX.FaceChange("bemused")
            ch_e "You wish."  
        menu:
            extend ""
            "Sorry, never mind." if "no suck breasts" in EmmaX.DailyActions:
                $ EmmaX.FaceChange("bemused")
                ch_e "No offense taken. I get it."              
                return
            "Maybe later?" if "no suck breasts" not in EmmaX.DailyActions:
                $ EmmaX.FaceChange("sexy")  
                ch_e "I'll give it some thought, [EmmaX.Petname]."
                $ EmmaX.Statup("Love", 80, 1)
                $ EmmaX.Statup("Love", 50, 1)
                $ EmmaX.Statup("Inbt", 30, 2)    
                if Taboo:                    
                    $ EmmaX.RecentActions.append("tabno")                      
                    $ EmmaX.DailyActions.append("tabno") 
                $ EmmaX.RecentActions.append("no suck breasts")                      
                $ EmmaX.DailyActions.append("no suck breasts")            
                return
            "Come on, Please?":             
                if Approval:
                    $ EmmaX.FaceChange("sexy")     
                    $ EmmaX.Statup("Obed", 90, 1)
                    $ EmmaX.Statup("Obed", 50, 2)
                    $ EmmaX.Statup("Inbt", 60, 3)
                    $ EmmaX.Statup("Inbt", 30, 2)
                    ch_e "Oh, if you insist. . ."                
                    jump Emma_SB_Prep
                else:   
                    $ EmmaX.FaceChange("sexy") 
                    ch_e "This wasn't a \"tone\" issue."     
            
            "[[Start sucking anyway]":                                               # Pressured into licking. 
                $ Approval = ApprovalCheck(EmmaX, 450, "OI", TabM = 3) # 45, 60, 75, -120(165)
                if Approval > 1 or (Approval and EmmaX.Forced):
                    $ EmmaX.FaceChange("sad")
                    $ EmmaX.Statup("Love", 70, -5, 1)
                    $ EmmaX.Statup("Love", 20, -2, 1)                 
                    ch_e "You'd better shower them with praise. . ."                         
                    $ EmmaX.Statup("Obed", 90, 2)
                    $ EmmaX.Statup("Obed", 50, 4)
                    $ EmmaX.Statup("Inbt", 60, 3)  
                    if Approval < 2:                          
                        $ EmmaX.Forced = 1
                    jump Emma_SB_Prep
                else:                              
                    $ EmmaX.Statup("Love", 200, -10)  
                    $ EmmaX.FaceChange("angry", 1)
                    "She shoves your head back out."   
                    $ EmmaX.RecentActions.append("angry")
                    $ EmmaX.DailyActions.append("angry")   
                    
    if "no suck breasts" in EmmaX.DailyActions:
        ch_e "I don't appreciate having to repeat myself, [EmmaX.Petname]."   
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")   
    elif EmmaX.Forced:
        $ EmmaX.FaceChange("angry", 1)
        ch_e "Not worth it."
        $ EmmaX.Statup("Lust", 60, 5)    
        $ EmmaX.Statup("Obed", 50, -2)    
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")   
    elif Taboo:   
        $ EmmaX.FaceChange("angry", 1)      
        $ EmmaX.RecentActions.append("tabno")    
        $ EmmaX.DailyActions.append("tabno") 
        ch_e "I have a reputation to maintain."                   
    elif EmmaX.SuckB:
        $ EmmaX.FaceChange("sad")
        ch_e "I am sorry about that, but perhaps later?"            
    else:
        $ EmmaX.FaceChange("sexy") 
        $ EmmaX.Mouth = "sad"
        ch_e "No."
    $ EmmaX.RecentActions.append("no suck breasts")                      
    $ EmmaX.DailyActions.append("no suck breasts") 
    $ Tempmod = 0    
    return
         

label Emma_SB_Prep:                                                                 #Animation set-up 
            
    if Trigger2 == "suck breasts":
        return
             
    call Emma_Breasts_Launch("suck breasts")
    
    if Situation == EmmaX:                                                        
            #Emma auto-starts    
            $ Situation = 0
            if (EmmaX.Over or EmmaX.Chest) and not EmmaX.Uptop:
                #if she has some sort of top on. . .
                if ApprovalCheck(EmmaX, 1250, TabM = 1) or (EmmaX.SeenChest and ApprovalCheck(EmmaX, 500) and not Taboo):
                        $ EmmaX.Uptop = 1
                        $ Line = EmmaX.Over if EmmaX.Over else EmmaX.Chest
                        "With a devilish grin, [EmmaX.Name] pulls her [Line] up over her breasts."
                        call Emma_First_Topless(1)
                        $ Line = 0
                        "She then grabs your head and crams your face into her chest, clearly intending you to get to work."
                else:
                        "[EmmaX.Name] grabs your head and crams your face into her chest, clearly intending you to get to work."
            else:
                        "[EmmaX.Name] grabs your head and crams your face into her chest, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":                    
                    $ EmmaX.Statup("Inbt", 80, 3) 
                    $ EmmaX.Statup("Inbt", 50, 2)
                    "You start to run your tongue along her nipple."
                "Praise her.":       
                    $ EmmaX.FaceChange("sexy", 1)                    
                    $ EmmaX.Statup("Inbt", 80, 3) 
                    ch_p "Mmm, I like this, [EmmaX.Pet]."
                    $ EmmaX.NameCheck() #checks reaction to petname
                    "You start to fondle it."
                    $ EmmaX.Statup("Love", 85, 1)
                    $ EmmaX.Statup("Obed", 90, 1)
                    $ EmmaX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your head back."
                    $ EmmaX.FaceChange("surprised")       
                    $ EmmaX.Statup("Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [EmmaX.Pet]."
                    $ EmmaX.NameCheck() #checks reaction to petname
                    "[EmmaX.Name] pulls away."
                    $ EmmaX.Statup("Obed", 90, 1)
                    $ EmmaX.Statup("Obed", 50, 1)
                    $ EmmaX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")      
                    $ EmmaX.AddWord(1,"refused","refused")  
                    return          
            #end auto
    if not EmmaX.Forced and Situation != "auto":
        $ Tempmod = 0   
        call Top_Off(EmmaX)
        if "angry" in EmmaX.RecentActions:
            return
    
    $ Tempmod = 0 
    if not EmmaX.SuckB:        
        if EmmaX.Forced:
            $ EmmaX.Statup("Love", 90, -25)
            $ EmmaX.Statup("Obed", 70, 25)
            $ EmmaX.Statup("Inbt", 80, 17) 
        else:
            $ EmmaX.Statup("Love", 90, 10)
            $ EmmaX.Statup("Obed", 70, 10)
            $ EmmaX.Statup("Inbt", 80, 15) 
    
    if Taboo:
        $ EmmaX.Inbt += int(Taboo/10)  
        $ EmmaX.Lust += int(Taboo/5)
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0
    $ Line = 0  
    $ Cnt = 0      
    if Taboo:
        $ EmmaX.DrainWord("tabno")
    $ EmmaX.DrainWord("no suck breasts")
    $ EmmaX.RecentActions.append("suck breasts")                      
    $ EmmaX.DailyActions.append("suck breasts") 
    
label Emma_SB_Cycle: #Repeating strokes  
    if Trigger2 == "kiss you":
            $ Trigger2 = 0
    while Round >=0:  
        call Shift_Focus(EmmaX) 
        call Emma_Breasts_Launch("suck breasts")
        $ EmmaX.LustFace()   
        
        if  Player.Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                         
                        "Slap her ass":                     
                                    call Slap_Ass(EmmaX)  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Emma_SB_Cycle  
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."                
                                    $ Player.FocusX = 0
                                    
                        "Other options":
                                menu:   
                                    "Offhand action":
                                            if EmmaX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ EmmaX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(EmmaX,"tired")   
                                                
                                    "Shift primary action":
                                            if EmmaX.Action and MultiAction:
                                                    menu:
                                                        "Pull back to fondling.":  
                                                            if EmmaX.Action and MultiAction:
                                                                $ Situation = "pullback"
                                                                call Emma_SB_After
                                                                call Emma_Fondle_Breasts
                                                            else:
                                                                "As you pull back, [EmmaX.Name] pushes you back in close."
                                                                call Sex_Basic_Dialog(EmmaX,"tired") 
                                                        "Never Mind":
                                                                jump Emma_SB_Cycle
                                            else: 
                                                call Sex_Basic_Dialog(EmmaX,"tired")            
                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(EmmaX)
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(EmmaX) 
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0   
                                                        
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(EmmaX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_SB_Cycle 
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_SB_Cycle 
                                            "Never mind":
                                                        jump Emma_SB_Cycle 
                                    "Undress [EmmaX.Name]":
                                            call Girl_Undress(EmmaX)   
                                    "Clean up [EmmaX.Name] (locked)" if not EmmaX.Spunk:
                                            pass  
                                    "Clean up [EmmaX.Name]" if EmmaX.Spunk:
                                            call Girl_Cleanup(EmmaX,"ask")                                         
                                    "Never mind":
                                            jump Emma_SB_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Emma_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Emma_SB_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Emma_Pos_Reset
                                    $ Line = 0
                                    jump Emma_SB_After
        #End menu (if Line)
        
        call Shift_Focus(EmmaX)    
        call Sex_Dialog(EmmaX,Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or EmmaX.Lust >= 100: 
                    #If either of you could cum   
                    if Player.Focus >= 100:    
                            #If you can cum:                                                 
                            call Player_Cumming(EmmaX)
                            if "angry" in EmmaX.RecentActions:  
                                call Emma_Pos_Reset
                                return    
                            $ EmmaX.Statup("Lust", 200, 5) 
                            if 100 > EmmaX.Lust >= 70 and EmmaX.OCount < 2:             
                                $ EmmaX.RecentActions.append("unsatisfied")                      
                                $ EmmaX.DailyActions.append("unsatisfied") 
                            
                            if Player.Focus > 80:
                                jump Emma_SB_After 
                            $ Line = "came"
     
                    if EmmaX.Lust >= 100:  
                            #If [EmmaX.Name] can cum                                             
                            call Girl_Cumming(EmmaX)
                            if Situation == "shift" or "angry" in EmmaX.RecentActions:
                                jump Emma_SB_After
                       
                    if Line == "came": #ex Player.Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in EmmaX.RecentActions:#And [EmmaX.Name] is unsatisfied,  
                                    "[EmmaX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it" 
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Emma_SB_After    
        if Partner:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)            
        #End orgasm
        
        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0
        
        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif Cnt == (5 + EmmaX.SuckB):
                    $ EmmaX.Brows = "sly"
                    ch_e "Lovely, aren't they?"   
        elif EmmaX.Lust >= 85:
                    pass
        elif Cnt == (15 + EmmaX.SuckB) and EmmaX.SEXP >= 15 and not ApprovalCheck(EmmaX, 1500):
                    $ EmmaX.Brows = "confused"        
                    menu:
                        ch_e "You certainly seem to be enjoying yourself, but perhaps we could add some variety?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Emma_SB_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Emma_SB_After
                        "No, this is fun.":   
                                if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):                        
                                    $ EmmaX.Statup("Love", 200, -5)
                                    $ EmmaX.Statup("Obed", 50, 3)                    
                                    $ EmmaX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ EmmaX.FaceChange("angry", 1)   
                                    call Emma_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_e "You may be enjoying yourself, but I'm getting a bit sore."                         
                                    $ EmmaX.Statup("Love", 50, -3, 1)
                                    $ EmmaX.Statup("Love", 80, -4, 1)
                                    $ EmmaX.Statup("Obed", 30, -1, 1)                    
                                    $ EmmaX.Statup("Obed", 50, -1, 1)  
                                    $ EmmaX.RecentActions.append("angry")
                                    $ EmmaX.DailyActions.append("angry")   
                                    jump Emma_SB_After
        #End Count check
           
        if Round == 10:
            ch_e "It's getting late. . ."  
        elif Round == 5:
            ch_e "We should take a break soon."        
    
        if EmmaX.Lust >= 50 and not EmmaX.Uptop and (EmmaX.Chest or EmmaX.Over):
                $ EmmaX.Uptop = 1
                "[EmmaX.Name] sighs and tugs her breasts free of her clothes."    
                call Emma_First_Topless    
                
    #Round = 0 loop breaks
    $ EmmaX.FaceChange("bemused", 0)
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."
    
label Emma_SB_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Emma_Pos_Reset
        
    $ EmmaX.FaceChange("sexy") 
    
    $ EmmaX.SuckB += 1  
    $ EmmaX.Action -=1
    $ EmmaX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ EmmaX.Addictionrate += 1        
    
    if Partner == "Kitty":
        call Partner_Like(EmmaX,2,2)
    else:
        call Partner_Like(EmmaX,2)
     
    if EmmaX.SuckB == 1:            
            $ EmmaX.SEXP += 4         
            if not Situation: 
                if EmmaX.Love >= 500 and "unsatisfied" not in EmmaX.RecentActions:
                    ch_e "Delectable, weren't they."
                elif EmmaX.Obed <= 500 and Player.Focus <= 20:
                    $ EmmaX.FaceChange("perplexed", 1)
                    ch_e "Did you get enough?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_e "Oh? What did you have in mind?"
    call Checkout
    return   
    
# End Suck breasts    

# Fondle Thighs start //////////////////////////////////////////

label Emma_Fondle_Thighs:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(EmmaX)
                                                                                        # Will she let you fondle her thighs? Modifiers
    if EmmaX.FondleT: #You've done it before
        $ Tempmod += 10
    if EmmaX.PantsNum() > 6 or EmmaX.HoseNum() >= 5: # she's got pants on.
        $ Tempmod -= 5    
    if EmmaX.Lust > 75: #She's really horny
        $ Tempmod += 10    
    if "exhibitionist" in EmmaX.Traits:
        $ Tempmod += Taboo   
    if "dating" in EmmaX.Traits or "sex friend" in EmmaX.Petnames:
        $ Tempmod += 10
    elif "ex" in EmmaX.Traits:
        $ Tempmod -= 25 
    if EmmaX.ForcedCount and not EmmaX.Forced:
        $ Tempmod -= 5 * EmmaX.ForcedCount      
    
    if Taboo and "tabno" in EmmaX.DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in EmmaX.History:                   
        $ Tempmod -= 20 
        
    if "no fondle thighs" in EmmaX.DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle thighs" in EmmaX.RecentActions else 0   
            
    $ Approval = ApprovalCheck(EmmaX, 750, TabM=1) # 75, 90, 105, Taboo -40(105)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ EmmaX.FaceChange("sexy")       
            $ EmmaX.Statup("Obed", 50, 1)
            $ EmmaX.Statup("Inbt", 30, 2)            
            "As you caress her thigh, [EmmaX.Name] glances at you, and smiles."             
            jump Emma_FT_Prep      
        else:               
            $ EmmaX.FaceChange("surprised")
            $ EmmaX.Statup("Obed", 50, -2)
            ch_e "Perhaps we keep it above the waist, [EmmaX.Petname]."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        $ EmmaX.FaceChange("surprised")    
        $ EmmaX.Brows = "sad"
        if EmmaX.Lust > 60:
            $ EmmaX.Statup("Love", 70, -3)
        $ EmmaX.Statup("Obed", 90, 1)
        $ EmmaX.Statup("Obed", 70, 2)
        "As you pull back, [EmmaX.Name] looks a little sad."              
        jump Emma_FT_Prep  
    elif "fondle thighs" in EmmaX.RecentActions:
        $ EmmaX.FaceChange("sexy", 1)
        ch_e "Mmmm, again? I suppose. . ."
        jump Emma_FT_Prep
    elif "fondle thighs" in EmmaX.DailyActions:
        $ EmmaX.FaceChange("sexy", 1)       
        ch_e "You didn't get enough earlier?"
    
    if Approval >= 2:                                                                   #She's into it. . .
        $ EmmaX.FaceChange("bemused", 1)
        if EmmaX.Forced:
            $ EmmaX.FaceChange("sad")
            $ EmmaX.Statup("Love", 70, -3, 1)
            $ EmmaX.Statup("Obed", 90, 1)
            $ EmmaX.Statup("Inbt", 60, 1)
        ch_e "Ok [EmmaX.Petname], go ahead."   
        $ EmmaX.Statup("Love", 90, 1)
        $ EmmaX.Statup("Inbt", 50, 3) 
        jump Emma_FT_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        $ EmmaX.FaceChange("angry", 1)
        if "no fondle thighs" in EmmaX.RecentActions:  
            ch_e "Your persistance is doing you no favors, [EmmaX.Petname]."
        elif Taboo and "tabno" in EmmaX.DailyActions and "no fondle thighs" in EmmaX.DailyActions:  
            ch_e "I told you not to touch me like that in public!" 
        elif "no fondle thighs" in EmmaX.DailyActions:       
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "tabno" in EmmaX.DailyActions:  
            ch_e "As I said, not here, [EmmaX.Petname]."  
        elif not EmmaX.FondleT:
            $ EmmaX.FaceChange("bemused")
            ch_e "Seems a bit forward, [EmmaX.Petname]."
        else:
            $ EmmaX.FaceChange("bemused")
            ch_e "You wish."  
        menu:
            extend ""
            "Sorry, never mind." if "no fondle thighs" in EmmaX.DailyActions:
                $ EmmaX.FaceChange("bemused")
                ch_e "I appreciate your restraint."             
                return
            "Maybe later?" if "no fondle thighs" not in EmmaX.DailyActions:
                $ EmmaX.FaceChange("sexy")  
                ch_e "Perhaps."
                $ EmmaX.Statup("Love", 80, 1)
                $ EmmaX.Statup("Inbt", 30, 2)    
                if Taboo:                    
                    $ EmmaX.RecentActions.append("tabno")                      
                    $ EmmaX.DailyActions.append("tabno") 
                $ EmmaX.RecentActions.append("no fondle thighs")                      
                $ EmmaX.DailyActions.append("no fondle thighs")            
                return
            "Come on, Please?":             
                if Approval:
                    $ EmmaX.FaceChange("sexy")     
                    $ EmmaX.Statup("Obed", 60, 1)
                    $ EmmaX.Statup("Obed", 30, 2)
                    $ EmmaX.Statup("Inbt", 50, 1)
                    $ EmmaX.Statup("Inbt", 30, 2)
                    ch_e "Politeness can be rewarded. . ."             
                    jump Emma_FT_Prep
                else:   
                    $ EmmaX.FaceChange("sexy") 
                    ch_e "This wasn't a \"tone\" issue."     
            
            "[[Start caressing her thigh anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck(EmmaX, 350, "OI", TabM = 2) # 35, 50, 65, -80(105)
                if Approval > 1 or (Approval and EmmaX.Forced):
                    $ EmmaX.FaceChange("sad")
                    $ EmmaX.Statup("Love", 70, -5, 1)
                    $ EmmaX.Statup("Love", 20, -2, 1)                 
                    ch_e "Hmmph."                         
                    $ EmmaX.Statup("Obed", 50, 3)
                    $ EmmaX.Statup("Inbt", 60, 2)  
                    if Approval < 2:                          
                        $ EmmaX.Forced = 1
                    jump Emma_FT_Prep
                else:                              
                    $ EmmaX.Statup("Love", 200, -8)  
                    $ EmmaX.FaceChange("angry", 1)
                    "She slaps your hand away."   
                    $ EmmaX.RecentActions.append("angry")
                    $ EmmaX.DailyActions.append("angry")   
                    
    if "no fondle thighs" in EmmaX.DailyActions:
        ch_e "I don't appreciate having to repeat myself, [EmmaX.Petname]."   
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")   
    elif EmmaX.Forced:
        $ EmmaX.FaceChange("angry", 1)
        ch_e "Don't push your luck."
        $ EmmaX.Statup("Lust", 50, 2)    
        $ EmmaX.Statup("Obed", 50, -1)   
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")   
    elif Taboo:
        $ EmmaX.FaceChange("angry", 1)    
        $ EmmaX.RecentActions.append("tabno")          
        $ EmmaX.DailyActions.append("tabno") 
        ch_e "I have a reputation to maintain."                   
    elif EmmaX.FondleT:
        $ EmmaX.FaceChange("sad")
        ch_e "Hands."            
    else:
        $ EmmaX.FaceChange("sexy") 
        $ EmmaX.Mouth = "sad"
        ch_e "No."
    $ EmmaX.RecentActions.append("no fondle thighs")                      
    $ EmmaX.DailyActions.append("no fondle thighs") 
    $ Tempmod = 0    
    return
    
label Emma_FT_Prep:                                                                 #Animation set-up 
    if Trigger == "kiss you": 
        $ Trigger = "fondle thighs" 
        return
        
    if Trigger2 == "fondle thighs": 
        return
        
    if not EmmaX.Forced and Situation != "auto":
        $ Tempmod = 0
        call Bottoms_Off(EmmaX) 
        if "angry" in EmmaX.RecentActions:
            return 
            
    $ Tempmod = 0    
    call Emma_Pussy_Launch("fondle thighs")
    if not EmmaX.FondleT:        
        if EmmaX.Forced:
            $ EmmaX.Statup("Love", 90, -10)
            $ EmmaX.Statup("Obed", 70, 15)
            $ EmmaX.Statup("Inbt", 80, 10) 
        else:
            $ EmmaX.Statup("Love", 90, 5)
            $ EmmaX.Statup("Obed", 70, 10)
            $ EmmaX.Statup("Inbt", 80, 15) 
            
    if Taboo:               
        $ EmmaX.Statup("Lust", 200, (int(Taboo/5)))                               
        $ EmmaX.Statup("Inbt", 200, (2*(int(Taboo/5))))
     
    if Situation:   
        $ renpy.pop_call() 
        $ Situation = 0 
    $ Line = 0 
    $ Cnt = 0
    if Taboo:
        $ EmmaX.DrainWord("tabno")
    $ EmmaX.DrainWord("no fondle thighs")
    $ EmmaX.RecentActions.append("fondle thighs")                      
    $ EmmaX.DailyActions.append("fondle thighs")  
    
label Emma_FT_Cycle:                                                                #Repeating strokes
    while Round >=0:  
        call Shift_Focus(EmmaX) 
        call Emma_Pussy_Launch("fondle thighs")
        $ EmmaX.LustFace()   
        
        if  Player.Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                         
                        "Slap her ass":                     
                                    call Slap_Ass(EmmaX)  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Emma_FT_Cycle  
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."                
                                    $ Player.FocusX = 0
                                    
                        "Other options":
                                menu:   
                                    "Offhand action":
                                            if EmmaX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ EmmaX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(EmmaX,"tired")   
                                                
                                    "Shift primary action":
                                            if EmmaX.Action and MultiAction:
                                                    menu:                                                             
                                                        "Can I do a little deeper?":
                                                                if EmmaX.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Emma_FT_After
                                                                    call Emma_Fondle_Pussy                
                                                                else:
                                                                    call Sex_Basic_Dialog(EmmaX,"tired")   
                                                        "Shift your hands a bit higher without asking":
                                                                if EmmaX.Action and MultiAction:
                                                                    $ Situation = "auto"
                                                                    call Emma_FT_After
                                                                    call Emma_Fondle_Pussy    
                                                                else:
                                                                    "As your hands creep upwards, she grabs your wrists."
                                                                    call Sex_Basic_Dialog(EmmaX,"tired")  
                                                        "Never Mind":
                                                                jump Emma_FT_Cycle
                                            else: 
                                                call Sex_Basic_Dialog(EmmaX,"tired")            
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Emma_FT_After
                                                call Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(EmmaX)
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(EmmaX) 
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0   
                                                        
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(EmmaX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_FT_Cycle 
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_FT_Cycle 
                                            "Never mind":
                                                        jump Emma_FT_Cycle 
                                    "Undress [EmmaX.Name]":
                                            call Girl_Undress(EmmaX)   
                                    "Clean up [EmmaX.Name] (locked)" if not EmmaX.Spunk:
                                            pass  
                                    "Clean up [EmmaX.Name]" if EmmaX.Spunk:
                                            call Girl_Cleanup(EmmaX,"ask")                                         
                                    "Never mind":
                                            jump Emma_FT_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Emma_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Emma_FT_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Emma_Pos_Reset
                                    $ Line = 0
                                    jump Emma_FT_After
        #End menu (if Line)
        
        call Shift_Focus(EmmaX)    
        call Sex_Dialog(EmmaX,Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or EmmaX.Lust >= 100: 
                    #If either of you could cum   
                    if Player.Focus >= 100:    
                            #If you can cum:                                                 
                            call Player_Cumming(EmmaX)
                            if "angry" in EmmaX.RecentActions:  
                                call Emma_Pos_Reset
                                return    
                            $ EmmaX.Statup("Lust", 200, 5) 
                            if 100 > EmmaX.Lust >= 70 and EmmaX.OCount < 2 and EmmaX.SEXP >= 20:             
                                $ EmmaX.RecentActions.append("unsatisfied")                      
                                $ EmmaX.DailyActions.append("unsatisfied") 
                            
                            if Player.Focus > 80:
                                jump Emma_FT_After 
                            $ Line = "came"
     
                    if EmmaX.Lust >= 100:  
                            #If [EmmaX.Name] can cum                                             
                            call Girl_Cumming(EmmaX)
                            if Situation == "shift" or "angry" in EmmaX.RecentActions:
                                jump Emma_FT_After
                       
                    if Line == "came": #ex Player.Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in EmmaX.RecentActions:#And [EmmaX.Name] is unsatisfied,  
                                    "[EmmaX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it" 
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Emma_FT_After    
        if Partner:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)            
        #End orgasm
        
        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0
        
        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif Cnt == (5 + EmmaX.FondleT):
                    $ EmmaX.Brows = "confused"
                    ch_e "Luxurious, yes?"   
        elif Cnt == (15 + EmmaX.FondleT) and EmmaX.SEXP >= 15 and not ApprovalCheck(EmmaX, 1500):
                    $ EmmaX.Brows = "confused"        
                    menu:
                        ch_e "You certainly seem to be enjoying yourself, but perhaps we could add some variety?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Emma_FT_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Emma_FT_After
                        "No, this is fun.":   
                                if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):                        
                                    $ EmmaX.Statup("Love", 200, -5)
                                    $ EmmaX.Statup("Obed", 50, 3)                    
                                    $ EmmaX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ EmmaX.FaceChange("angry", 1)   
                                    call Emma_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_e "Well perhaps you are enjoying yourself, but I'm tired of this."                         
                                    $ EmmaX.Statup("Love", 50, -3, 1)
                                    $ EmmaX.Statup("Love", 80, -4, 1)
                                    $ EmmaX.Statup("Obed", 30, -1, 1)                    
                                    $ EmmaX.Statup("Obed", 50, -1, 1)  
                                    $ EmmaX.RecentActions.append("angry")
                                    $ EmmaX.DailyActions.append("angry")   
                                    jump Emma_FT_After
        #End Count check
           
        if Round == 10:
            ch_e "It's getting late. . ."  
        elif Round == 5:
            ch_e "We should take a break soon."        
    
    #Round = 0 loop breaks
    $ EmmaX.FaceChange("bemused", 0)
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."
    
    
label Emma_FT_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Emma_Pos_Reset
        
    $ EmmaX.FaceChange("sexy") 
    
    $ EmmaX.FondleT += 1  
    $ EmmaX.Action -=1
    if EmmaX.PantsNum() <= 6 or EmmaX.Upskirt:        
        $ EmmaX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ EmmaX.Addictionrate += 1
    
    if Partner == "Kitty":
        call Partner_Like(EmmaX,2)
    else:
        call Partner_Like(EmmaX,1)
     
    if EmmaX.FondleT == 1:            
            $ EmmaX.SEXP += 3         
            if not Situation: 
                if EmmaX.Love >= 500 and "unsatisfied" not in EmmaX.RecentActions:
                    ch_e "That was. . . pleasant."
                elif EmmaX.Obed <= 500 and Player.Focus <= 20:
                    $ EmmaX.FaceChange("perplexed", 1)
                    ch_e "Was that enough?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_e "Oh? What did you have in mind?"
    call Checkout
    return   
    
# ////////////////////////////////////////////////////////////////////////Start Fondle Pussy    
label Emma_Fondle_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(EmmaX)
                                                                                        # Will she let you fondle? Modifiers
    if EmmaX.FondleP: #You've done it before
        $ Tempmod += 20
    if EmmaX.PantsNum() > 6 or EmmaX.HoseNum() >= 5: # she's got pants on.
        $ Tempmod -= 10    
    if EmmaX.Lust > 75: #She's really horny
        $ Tempmod += 15
    if EmmaX.Lust > 75 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in EmmaX.Traits:
        $ Tempmod += (2*Taboo)
    if "dating" in EmmaX.Traits or "sex friend" in EmmaX.Petnames:
        $ Tempmod += 10
    elif "ex" in EmmaX.Traits:
        $ Tempmod -= 25  
    if EmmaX.ForcedCount and not EmmaX.Forced:
        $ Tempmod -= 5 * EmmaX.ForcedCount     
    
    if Taboo and "tabno" in EmmaX.DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in EmmaX.History:                   
        $ Tempmod -= 20 
        
    if "no fondle pussy" in EmmaX.DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle pussy" in EmmaX.RecentActions else 0   
            
    $ Approval = ApprovalCheck(EmmaX, 1050, TabM = 2) # 105, 120, 135, Taboo -80(185)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ EmmaX.FaceChange("sexy")       
            $ EmmaX.Statup("Obed", 90, 1)
            $ EmmaX.Statup("Obed", 70, 2)
            $ EmmaX.Statup("Inbt", 70, 3)
            $ EmmaX.Statup("Inbt", 30, 2)
            "As your hand creeps up her thigh, [EmmaX.Name] seems a bit surprised, but then nods."            
            jump Emma_FP_Prep      
        else:               
            $ EmmaX.FaceChange("surprised")
            $ EmmaX.Statup("Obed", 50, -2)
            ch_e "Down boy, you were doing so well. . ."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        $ EmmaX.FaceChange("surprised")   
        $ EmmaX.Brows = "sad"        
        if EmmaX.Lust > 80:
            $ EmmaX.Statup("Love", 70, -4)
        $ EmmaX.Statup("Obed", 90, 1)
        $ EmmaX.Statup("Obed", 70, 2)
        "As your hand pulls out, [EmmaX.Name] gasps and looks upset."              
        jump Emma_FP_Prep     
    elif "fondle pussy" in EmmaX.RecentActions:
        $ EmmaX.FaceChange("sexy", 1)
        ch_e "Mmmm, again? I suppose. . ."
        jump Emma_FP_Prep
    elif "fondle pussy" in EmmaX.DailyActions:
        $ EmmaX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax, gently. . .",
            "Take it a bit gently, I'm still shaking from earlier.",
            "Mmm. . ."]) 
        ch_e "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .
        $ EmmaX.FaceChange("bemused", 1)
        if EmmaX.Forced:
            $ EmmaX.FaceChange("sad")
            $ EmmaX.Statup("Love", 70, -3, 1)
            $ EmmaX.Statup("Love", 20, -2, 1)
            $ EmmaX.Statup("Obed", 90, 1)
            $ EmmaX.Statup("Inbt", 60, 1)
        ch_e "Mmmm, I couldn't refuse. . ."   
        $ EmmaX.Statup("Love", 90, 1)
        $ EmmaX.Statup("Inbt", 50, 3) 
        jump Emma_FP_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        $ EmmaX.FaceChange("angry", 1)
        if "no fondle pussy" in EmmaX.RecentActions:  
            ch_e "Your persistance is doing you no favors, [EmmaX.Petname]."
        elif Taboo and "tabno" in EmmaX.DailyActions and "no fondle pussy" in EmmaX.DailyActions:  
            ch_e "I told you not to touch me like that in public!" 
        elif "no fondle pussy" in EmmaX.DailyActions:       
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "tabno" in EmmaX.DailyActions:  
            ch_e "As I said, not here, [EmmaX.Petname]."  
        elif not EmmaX.FondleP:
            $ EmmaX.FaceChange("bemused")
            ch_e "I don't think we're there yet, [EmmaX.Petname]. . ."
        else:
            $ EmmaX.FaceChange("bemused")
            ch_e "You wish."  
        menu:
            extend ""
            "Sorry, never mind." if "no fondle pussy" in EmmaX.DailyActions:
                $ EmmaX.FaceChange("bemused")
                ch_e "I appreciate your restraint, [EmmaX.Petname]."              
                return
            "Maybe later?" if "no fondle pussy" not in EmmaX.DailyActions:
                $ EmmaX.FaceChange("sexy")  
                ch_e "I'll give it some thought, [EmmaX.Petname]."
                $ EmmaX.Statup("Love", 80, 2)
                $ EmmaX.Statup("Inbt", 70, 2)   
                if Taboo:                    
                    $ EmmaX.RecentActions.append("tabno")                      
                    $ EmmaX.DailyActions.append("tabno") 
                $ EmmaX.RecentActions.append("no fondle pussy")                      
                $ EmmaX.DailyActions.append("no fondle pussy")            
                return
            "Come on, Please?":             
                if Approval:
                    $ EmmaX.FaceChange("sexy")     
                    $ EmmaX.Statup("Obed", 90, 2)
                    $ EmmaX.Statup("Obed", 50, 2)
                    $ EmmaX.Statup("Inbt", 70, 3) 
                    $ EmmaX.Statup("Inbt", 40, 2) 
                    ch_e "I do enjoy hearing you beg. . ."                    
                    jump Emma_FP_Prep
                else:   
                    $ EmmaX.FaceChange("sexy") 
                    ch_e "No."
            
            "[[Start fondling anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck(EmmaX, 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                if Approval > 1 or (Approval and EmmaX.Forced):
                    $ EmmaX.FaceChange("sad")
                    $ EmmaX.Statup("Love", 70, -5, 1)
                    $ EmmaX.Statup("Love", 200, -2)                 
                    ch_e "Oh, if you insist. . ."
                    $ EmmaX.Statup("Obed", 50, 4)
                    $ EmmaX.Statup("Inbt", 80, 1) 
                    $ EmmaX.Statup("Inbt", 60, 3)  
                    if Approval < 2:                          
                        $ EmmaX.Forced = 1
                    jump Emma_FP_Prep
                else:                              
                    $ EmmaX.Statup("Love", 200, -15)  
                    $ EmmaX.FaceChange("angry", 1)
                    "She slaps your hand away."   
                    $ EmmaX.RecentActions.append("angry")
                    $ EmmaX.DailyActions.append("angry")   
                    
    if "no fondle pussy" in EmmaX.DailyActions:
        ch_e "I don't appreciate having to repeat myself, [EmmaX.Petname]."   
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")   
    elif EmmaX.Forced:
        $ EmmaX.FaceChange("angry", 1)
        ch_e "I don't think so, [EmmaX.Petname]."
        $ EmmaX.Statup("Lust", 70, 5)    
        $ EmmaX.Statup("Obed", 50, -2)    
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")   
    elif Taboo:
        $ EmmaX.FaceChange("angry", 1)    
        $ EmmaX.RecentActions.append("tabno")                   
        $ EmmaX.DailyActions.append("tabno")
        ch_e "I have a reputation to maintain."                   
    elif EmmaX.FondleP:
        $ EmmaX.FaceChange("sad")
        ch_e "Sorry, keep your hands out of there."           
    else:
        $ EmmaX.FaceChange("sexy") 
        $ EmmaX.Mouth = "sad"
        ch_e "No thank you, [EmmaX.Petname]."
    $ EmmaX.RecentActions.append("no fondle pussy")                      
    $ EmmaX.DailyActions.append("no fondle pussy") 
    $ Tempmod = 0    
    return
                    
label Emma_FP_Prep: #Animation set-up 
    if Trigger2 == "fondle pussy":
        return
            
    call Emma_Pussy_Launch("fondle pussy")
    
    if Situation == EmmaX:                                                        
            #Emma auto-starts    
            $ Situation = 0
            if (EmmaX.Legs and not EmmaX.Upskirt) or (EmmaX.Panties and not EmmaX.PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck(EmmaX, 1250, TabM = 1) or (EmmaX.SeenPussy and ApprovalCheck(EmmaX, 500) and not Taboo):
                        $ EmmaX.Upskirt = 1
                        $ EmmaX.PantiesDown = 1
                        $ Line = 0
                        if EmmaX.PantsNum() == 5:
                            $ Line = EmmaX.Name + " hikes up her skirt"
                        elif EmmaX.PantsNum() >= 6:
                            $ Line = EmmaX.Name + " pulls down her " + EmmaX.Legs
                        else:
                            $ Line = 0                            
                        if EmmaX.Panties:
                            if Line:
                                #wearing pants
                                "[Line] and pulls her [EmmaX.Panties] out of the way."
                                "She then grabs your arm and then strokes your hand across her crotch, clearly intending you to get to work."
                            else:
                                #no pants
                                "She pulls her [EmmaX.Panties] out of the way, and then strokes your hand across her crotch."
                                "She clearly intends for you to get to work." 
                        else:
                                #pants but no panties
                                "[Line], and then strokes your hand across her crotch."
                                "She clearly intends for you to get to work."                     
                        call Emma_First_Bottomless(1)
                else:
                        "[EmmaX.Name] grabs your arm and strokes your hand across her crotch, clearly intending you to get to work."
            else:
                        "[EmmaX.Name] grabs your arm and strokes your hand across her crotch, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":                    
                    $ EmmaX.Statup("Inbt", 80, 3) 
                    $ EmmaX.Statup("Inbt", 50, 2)
                    "You start to run your fingers along her pussy."
                "Praise her.":       
                    $ EmmaX.FaceChange("sexy", 1)                    
                    $ EmmaX.Statup("Inbt", 80, 3) 
                    ch_p "I like the initiative, [EmmaX.Pet]."
                    $ EmmaX.NameCheck() #checks reaction to petname
                    "You start to run your fingers along her pussy."
                    $ EmmaX.Statup("Love", 85, 1)
                    $ EmmaX.Statup("Obed", 90, 1)
                    $ EmmaX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your hand back."
                    $ EmmaX.FaceChange("surprised")       
                    $ EmmaX.Statup("Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [EmmaX.Pet]."
                    $ EmmaX.NameCheck() #checks reaction to petname
                    "[EmmaX.Name] pulls back."
                    $ EmmaX.Statup("Obed", 90, 1)
                    $ EmmaX.Statup("Obed", 50, 1)
                    $ EmmaX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")      
                    $ EmmaX.AddWord(1,"refused","refused")  
                    return          
            #end auto
            
    if not EmmaX.Forced and Situation != "auto":
        $ Tempmod = 0
        call Bottoms_Off(EmmaX)   
        if "angry" in EmmaX.RecentActions:
            return 
    $ Tempmod = 0
    
    if not EmmaX.FondleP:        
        if EmmaX.Forced:
            $ EmmaX.Statup("Love", 90, -50)
            $ EmmaX.Statup("Obed", 70, 35)
            $ EmmaX.Statup("Inbt", 80, 25) 
        else:
            $ EmmaX.Statup("Love", 90, 10)
            $ EmmaX.Statup("Obed", 70, 10)
            $ EmmaX.Statup("Inbt", 80, 15) 
    if Taboo:
        $ EmmaX.Inbt += int(Taboo/10)  
        $ EmmaX.Lust += int(Taboo/5)
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0   
    $ Line = 0    
    $ Cnt = 0
    if Taboo:
        $ EmmaX.DrainWord("tabno")
    $ EmmaX.DrainWord("no fondle pussy")
    $ EmmaX.RecentActions.append("fondle pussy")                      
    $ EmmaX.DailyActions.append("fondle pussy") 
    
    $ Speed = 1
    
label Emma_FP_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus(EmmaX) 
        call Emma_Pussy_Launch("fondle pussy")
        $ EmmaX.LustFace()   
        
        if  Player.Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                          
                        "I want to stick a finger in. . ." if Speed != 2:
                                if EmmaX.InsertP: 
                                    $ Speed = 2
                                else:
                                    menu:                                
                                        "Ask her first":
                                            $ Situation = "shift"
                                        "Don't ask first [[just stick it in]":                                    
                                            $ Situation = "auto"
                                    call Emma_Insert_Pussy 
                        
                        "Pull back a bit. . ." if Speed == 2:
                                    $ Speed = 0
                                    
                        "Slap her ass":                     
                                    call Slap_Ass(EmmaX)  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Emma_FP_Cycle  
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."                
                                    $ Player.FocusX = 0
                                    
                        "Other options":
                                menu:   
                                    "Offhand action":
                                            if EmmaX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ EmmaX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(EmmaX,"tired")   
                                                
                                    "Shift primary action":
                                            if EmmaX.Action and MultiAction:
                                                    menu:                                                             
                                                        "I want to lick your pussy.":
                                                                $ Situation = "shift"
                                                                call Emma_FP_After
                                                                call Emma_Lick_Pussy                 
                                                        "Just start licking":
                                                                $ Situation = "auto"
                                                                call Emma_FP_After
                                                                call Emma_Lick_Pussy         
                                                        "Pull back to the thighs":
                                                                $ Situation = "pullback"
                                                                call Emma_FP_After
                                                                call Emma_Fondle_Thighs
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Emma_FP_After
                                                                call Emma_Dildo_Pussy  
                                                        "Never Mind":
                                                                jump Emma_FP_Cycle
                                            else: 
                                                call Sex_Basic_Dialog(EmmaX,"tired")            
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Emma_FP_After
                                                call Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(EmmaX)
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(EmmaX) 
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0   
                                                        
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(EmmaX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_FP_Cycle 
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_FP_Cycle 
                                            "Never mind":
                                                        jump Emma_FP_Cycle 
                                    "Undress [EmmaX.Name]":
                                            call Girl_Undress(EmmaX)   
                                    "Clean up [EmmaX.Name] (locked)" if not EmmaX.Spunk:
                                            pass  
                                    "Clean up [EmmaX.Name]" if EmmaX.Spunk:
                                            call Girl_Cleanup(EmmaX,"ask")                                         
                                    "Never mind":
                                            jump Emma_FP_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Emma_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Emma_FP_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Emma_Pos_Reset
                                    $ Line = 0
                                    jump Emma_FP_After
        #End menu (if Line)
        
        call Shift_Focus(EmmaX)    
        call Sex_Dialog(EmmaX,Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or EmmaX.Lust >= 100: 
                    #If either of you could cum   
                    if Player.Focus >= 100:    
                            #If you can cum:                                                 
                            call Player_Cumming(EmmaX)
                            if "angry" in EmmaX.RecentActions:  
                                call Emma_Pos_Reset
                                return    
                            $ EmmaX.Statup("Lust", 200, 5) 
                            if 100 > EmmaX.Lust >= 70 and EmmaX.OCount < 2:             
                                $ EmmaX.RecentActions.append("unsatisfied")                      
                                $ EmmaX.DailyActions.append("unsatisfied") 
                            
                            if Player.Focus > 80:
                                jump Emma_FP_After 
                            $ Line = "came"
     
                    if EmmaX.Lust >= 100:  
                            #If [EmmaX.Name] can cum                                             
                            call Girl_Cumming(EmmaX)
                            if Situation == "shift" or "angry" in EmmaX.RecentActions:
                                jump Emma_FP_After
                       
                    if Line == "came": #ex Player.Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in EmmaX.RecentActions:#And [EmmaX.Name] is unsatisfied,  
                                    "[EmmaX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it" 
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Emma_FP_After    
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)            
        #End orgasm
        
        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0
        
        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif Cnt == (5 + EmmaX.FondleP):
                    $ EmmaX.Brows = "confused"
                    ch_e "You like how that feels, huh?"  
        elif EmmaX.Lust >= 80:
                    pass
        elif Cnt == (15 + EmmaX.FondleP) and EmmaX.SEXP >= 15 and not ApprovalCheck(EmmaX, 1500):
                    $ EmmaX.Brows = "confused"        
                    menu:
                        ch_e "You certainly seem to be enjoying yourself, but perhaps we could add some variety?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Emma_FP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Emma_FP_After
                        "No, this is fun.":   
                                if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):                        
                                    $ EmmaX.Statup("Love", 200, -5)
                                    $ EmmaX.Statup("Obed", 50, 3)                    
                                    $ EmmaX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ EmmaX.FaceChange("angry", 1)   
                                    call Emma_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_e "Well perhaps you are enjoying yourself, but I'm tired of this."                         
                                    $ EmmaX.Statup("Love", 50, -3, 1)
                                    $ EmmaX.Statup("Love", 80, -4, 1)
                                    $ EmmaX.Statup("Obed", 30, -1, 1)                    
                                    $ EmmaX.Statup("Obed", 50, -1, 1)  
                                    $ EmmaX.RecentActions.append("angry")
                                    $ EmmaX.DailyActions.append("angry")   
                                    jump Emma_FP_After
        #End Count check
           
        if Round == 10:
            ch_e "It's getting late. . ."  
        elif Round == 5:
            ch_e "We should take a break soon."        
    
    #Round = 0 loop breaks
    $ EmmaX.FaceChange("bemused", 0)
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."
    
    
label Emma_FP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Emma_Pos_Reset
        
    $ EmmaX.FaceChange("sexy") 
    
    $ EmmaX.FondleP += 1  
    $ EmmaX.Action -=1
    if EmmaX.PantsNum() <= 6 or EmmaX.Upskirt:        
        $ EmmaX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ EmmaX.Addictionrate += 1
    
    call Partner_Like(EmmaX,2)
     
    if EmmaX.FondleP == 1:            
            $ EmmaX.SEXP += 7         
            if not Situation: 
                if EmmaX.Love >= 500 and "unsatisfied" not in EmmaX.RecentActions:
                    ch_e "I do appreciate some rather. . . aggressive attention down there."
                elif EmmaX.Obed <= 500 and Player.Focus <= 20:
                    $ EmmaX.FaceChange("perplexed", 1)
                    ch_e "Did you find what you were looking for?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_e "Oh? What did you have in mind?"
    call Checkout
    return   

# end EmmaX.Fondle Pussy /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label Emma_Insert_Pussy:
    call Shift_Focus(EmmaX)
    if Situation == "auto":                                                                  #You auto-start                    
        if ApprovalCheck(EmmaX, 1100, TabM = 2):
            $ EmmaX.FaceChange("surprised")       
            $ EmmaX.Statup("Obed", 90, 1)
            $ EmmaX.Statup("Obed", 70, 2)
            $ EmmaX.Statup("Inbt", 70, 3) 
            $ EmmaX.Statup("Inbt", 30, 2) 
            "As you slide a finger in, [EmmaX.Name] seems a bit surprised, but seems into it."              
            jump Emma_IP_Prep
        else:   
            $ EmmaX.FaceChange("surprised",2)
            $ EmmaX.Statup("Love", 80, -2)
            $ EmmaX.Statup("Obed", 50, -3)
            ch_e "Oooh!"
            "She slaps your hand back."
            $ EmmaX.FaceChange("perplexed",1)
            ch_e "Careful what you put in there, you may not get it back."
            return            
    
    if ApprovalCheck(EmmaX, 1100, TabM = 2):                                                                   #She's into it. . .               
        if EmmaX.Forced:
            $ EmmaX.FaceChange("sad")
            $ EmmaX.Statup("Love", 70, -3, 1)
            $ EmmaX.Statup("Love", 20, -2, 1)
            $ EmmaX.Statup("Obed", 90, 1)
            $ EmmaX.Statup("Inbt", 60, 1)
            ch_e "If you must. . ."    
        else:
            $ EmmaX.FaceChange("sexy", 1)
            $ EmmaX.Statup("Love", 90, 1)
            $ EmmaX.Statup("Inbt", 50, 3) 
            ch_e "Mmmmmm. . ."                
        $ EmmaX.Statup("Obed", 20, 1)
        $ EmmaX.Statup("Obed", 60, 1)
        $ EmmaX.Statup("Inbt", 70, 2) 
        jump Emma_IP_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .  
        $ EmmaX.FaceChange("bemused", 2)
        ch_e "No. Thank you."
        $ EmmaX.Blush = 1
    return
    
                
label Emma_IP_Prep: #Animation set-up     
    if not EmmaX.InsertP:
        $ EmmaX.InsertP = 1
        $ EmmaX.SEXP += 10          
        if EmmaX.Forced:
            $ EmmaX.Statup("Love", 90, -60)
            $ EmmaX.Statup("Obed", 70, 55)
            $ EmmaX.Statup("Inbt", 80, 35) 
        else:
            $ EmmaX.Statup("Love", 90, 10)
            $ EmmaX.Statup("Obed", 70, 20)
            $ EmmaX.Statup("Inbt", 80, 25)
                
    if not EmmaX.Forced and Situation != "auto":        
        call Girl_Undress(EmmaX,"bottom")
        if "angry" in EmmaX.RecentActions:
            return    
            
#    call Emma_Pussy_Launch("insert pussy")
    if Taboo:
        $ EmmaX.Inbt += int(Taboo/10)  
        $ EmmaX.Lust += int(Taboo/5)
        
    $ Line = 0  
    $ Speed = 2
    return

# end EmmaX.Insert Pussy /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label Emma_Lick_Pussy: 
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(EmmaX)
                                                                                  # Will she let you fondle? Modifiers     
    if EmmaX.LickP: #You've done it before
        $ Tempmod += 15
    if EmmaX.PantsNum() > 6 or EmmaX.HoseNum() >= 5: # she's got pants on.
        $ Tempmod -= 15  
    if EmmaX.Lust > 95:
        $ Tempmod += 20  
    elif EmmaX.Lust > 85: #She's really horny
        $ Tempmod += 15
    if Situation == "shift":
        $ Tempmod += 10
    if EmmaX.Lust > 85 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in EmmaX.Traits:
        $ Tempmod += (4*Taboo) 
    if "dating" in EmmaX.Traits or "sex friend" in EmmaX.Petnames:
        $ Tempmod += 10
    elif "ex" in EmmaX.Traits:
        $ Tempmod -= 25  
    if EmmaX.ForcedCount and not EmmaX.Forced:
        $ Tempmod -= 5 * EmmaX.ForcedCount     
    
    if Taboo and "tabno" in EmmaX.DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in EmmaX.History:                   
        $ Tempmod -= 20 
        
    if "no lick pussy" in EmmaX.DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no lick pussy" in EmmaX.RecentActions else 0   
            
    $ Approval = ApprovalCheck(EmmaX, 1250, TabM = 4) # 125, 140, 155, Taboo -160(285)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            $ EmmaX.FaceChange("surprised")
            $ EmmaX.Statup("Obed", 90, 1)
            $ EmmaX.Statup("Obed", 70, 2)
            $ EmmaX.Statup("Inbt", 70, 3) 
            $ EmmaX.Statup("Inbt", 30, 2) 
            "As you crouch down and start to lick her pussy, [EmmaX.Name] jumps, but then softens."  
            $ EmmaX.FaceChange("sexy")           
            jump Emma_LP_Prep
        else:   
            $ EmmaX.FaceChange("surprised")
            $ EmmaX.Statup("Love", 80, -2)
            $ EmmaX.Statup("Obed", 50, -3)
            ch_e "I like where your head is at, so to speak, but perhaps hold off on that." 
            $ EmmaX.FaceChange("perplexed",1)
            "She pushes your head back away from her."
            $ Tempmod = 0
            $ Trigger2 = 0
            return            
    
    if "lick pussy" in EmmaX.RecentActions:
        $ EmmaX.FaceChange("sexy", 1)
        ch_e "Mmmm, again? I suppose. . ."
        jump Emma_LP_Prep
    elif "lick pussy" in EmmaX.DailyActions:
        $ EmmaX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right.",
            "What a queen deserves. . .",
            "Mmm. . ."]) 
        ch_e "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .               
        if EmmaX.Forced:
            $ EmmaX.FaceChange("sad")
            $ EmmaX.Statup("Love", 70, -3, 1)
            $ EmmaX.Statup("Love", 20, -2, 1)
            $ EmmaX.Statup("Obed", 90, 1)
            $ EmmaX.Statup("Inbt", 60, 1)
            ch_e "If you must. . ."    
        else:
            $ EmmaX.FaceChange("sexy", 1)
            $ EmmaX.Eyes = "closed"            
            $ EmmaX.Statup("Love", 90, 1)
            $ EmmaX.Statup("Inbt", 50, 3)            
            $ EmmaX.Statup("Lust", 200, 3)
            ch_e "Mmmmmm. . ."                
        $ EmmaX.Statup("Obed", 20, 1)
        $ EmmaX.Statup("Obed", 60, 1)
        $ EmmaX.Statup("Inbt", 70, 2) 
        jump Emma_LP_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        $ EmmaX.FaceChange("angry", 1)
        if "no lick pussy" in EmmaX.RecentActions:  
            ch_e "Your persistance is doing you no favors, [EmmaX.Petname]."
        elif Taboo and "tabno" in EmmaX.DailyActions and "no lick pussy" in EmmaX.DailyActions:  
            ch_e "You already got your answer!" 
        elif "no lick pussy" in EmmaX.DailyActions:       
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "tabno" in EmmaX.DailyActions:  
            ch_e "As I said, not here, [EmmaX.Petname]."  
        elif not EmmaX.LickP:
            $ EmmaX.FaceChange("bemused")
            ch_e "I'm not sure we're at that stage, [EmmaX.Petname]. . ."
        else:
            $ EmmaX.FaceChange("bemused")
            ch_e "I'm really not comfortable with that. . ." 
        menu:
            extend ""
            "Sorry, never mind." if "no lick pussy" in EmmaX.DailyActions:
                $ EmmaX.FaceChange("bemused")
                ch_e "I appreciate your restraint, [EmmaX.Petname]."              
                return            
            "I'm sure I can convince you later. . ." if "no lick pussy" not in EmmaX.DailyActions:
                $ EmmaX.FaceChange("sexy")  
                ch_e "I'll be thinking about it, [EmmaX.Petname]."
                $ EmmaX.Statup("Love", 80, 2)
                $ EmmaX.Statup("Inbt", 70, 2)   
                if Taboo:                    
                    $ EmmaX.RecentActions.append("tabno")                      
                    $ EmmaX.DailyActions.append("tabno") 
                $ EmmaX.RecentActions.append("no lick pussy")                      
                $ EmmaX.DailyActions.append("no lick pussy")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    $ EmmaX.FaceChange("sexy")           
                    $ EmmaX.Statup("Obed", 90, 2)
                    $ EmmaX.Statup("Obed", 50, 2)
                    ch_e "You present a compelling case. . ."      
                    $ EmmaX.Statup("Inbt", 70, 3) 
                    $ EmmaX.Statup("Inbt", 40, 2)
                    jump Emma_LP_Prep
                else:   
                    $ EmmaX.FaceChange("sexy") 
                    ch_e "I would, but still no, [EmmaX.Petname]."    
            
            "[[Get in there anyway]":                                               # Pressured into being licked. 
                $ Approval = ApprovalCheck(EmmaX, 750, "OI", TabM = 4) # 75, 90, 105, -160(235)
                if Approval > 1 or (Approval and EmmaX.Forced):
                    $ EmmaX.FaceChange("sad")
                    $ EmmaX.Statup("Love", 70, -5, 1)
                    $ EmmaX.Statup("Love", 200, -2)                 
                    ch_e "If you insist. . ."  
                    $ EmmaX.Statup("Obed", 50, 4)
                    $ EmmaX.Statup("Inbt", 80, 1) 
                    $ EmmaX.Statup("Inbt", 60, 3)  
                    if Approval < 2:                          
                        $ EmmaX.Forced = 1
                    jump Emma_LP_Prep
                else:                              
                    $ EmmaX.Statup("Love", 200, -15)  
                    $ EmmaX.FaceChange("angry", 1)
                    "She shoves your head back."   
                    $ EmmaX.RecentActions.append("angry")
                    $ EmmaX.DailyActions.append("angry")   
                    
    if "no lick pussy" in EmmaX.DailyActions:
        ch_e "I don't appreciate having to repeat myself, [EmmaX.Petname]."   
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")   
    elif EmmaX.Forced:
        $ EmmaX.FaceChange("angry", 1)
        ch_e "I really can't, [EmmaX.Petname]."
        $ EmmaX.Statup("Lust", 80, 5)    
        $ EmmaX.Statup("Obed", 50, -2)     
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")   
    elif Taboo:
        $ EmmaX.FaceChange("angry", 1)    
        $ EmmaX.RecentActions.append("tabno")                   
        $ EmmaX.DailyActions.append("tabno") 
        ch_e "I have a reputation to maintain."                   
    elif EmmaX.LickP:
        $ EmmaX.FaceChange("sad") 
        ch_e "Keep your head out of there."    
    else:
        $ EmmaX.FaceChange("surprised")
        ch_e "I know, I'm as disappointed as you are."
        $ EmmaX.FaceChange()
    $ EmmaX.RecentActions.append("no lick pussy")                      
    $ EmmaX.DailyActions.append("no lick pussy") 
    $ Tempmod = 0    
    return
    
label Emma_LP_Prep: #Animation set-up  
    if Trigger2 == "lick pussy": #fix pull down pants now an option, make it work
        return
            
    call Emma_Pussy_Launch("lick pussy")
    
    if Situation == EmmaX:                                                       
            #Emma auto-starts    
            $ Situation = 0
            if (EmmaX.Legs and not EmmaX.Upskirt) or (EmmaX.Panties and not EmmaX.PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck(EmmaX, 1250, TabM = 1) or (EmmaX.SeenPussy and ApprovalCheck(EmmaX, 500) and not Taboo):
                        $ EmmaX.Upskirt = 1
                        $ EmmaX.PantiesDown = 1
                        $ Line = 0
                        if EmmaX.PantsNum() == 5:
                            $ Line = EmmaX.Name + " hikes up her skirt"
                        elif EmmaX.PantsNum() >= 6:
                            $ Line = EmmaX.Name + " pulls down her " + EmmaX.Legs
                        else:
                            $ Line = 0                            
                        if EmmaX.Panties:
                            if Line:
                                #wearing pants
                                "[Line] and pulls her [EmmaX.Panties] out of the way."
                                "She then grabs your head and pulls it to her crotch, clearly intending you to get to work."
                            else:
                                #no pants
                                "She pulls her [EmmaX.Panties] out of the way, and then shoves your face into her crotch."
                                "She clearly intends for you to get to work." 
                        else:
                                #pants but no panties
                                "[Line], and then shoves your face into her crotch."
                                "She clearly intends for you to get to work."                     
                        call Emma_First_Bottomless(1)
                else:
                        "[EmmaX.Name] grabs your head and pulls it to her crotch, clearly intending you to get to work."
            else:
                        "[EmmaX.Name] grabs your head and pulls it to her crotch, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":                    
                    $ EmmaX.Statup("Inbt", 80, 3) 
                    $ EmmaX.Statup("Inbt", 50, 2)
                    "You start licking."
                "Praise her.":       
                    $ EmmaX.FaceChange("sexy", 1)                    
                    $ EmmaX.Statup("Inbt", 80, 3) 
                    ch_p "Mmm, I like this idea, [EmmaX.Pet]."
                    $ EmmaX.NameCheck() #checks reaction to petname
                    "You start licking."
                    $ EmmaX.Statup("Love", 85, 1)
                    $ EmmaX.Statup("Obed", 90, 1)
                    $ EmmaX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your head away."
                    $ EmmaX.FaceChange("surprised")       
                    $ EmmaX.Statup("Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [EmmaX.Pet]."
                    $ EmmaX.NameCheck() #checks reaction to petname
                    "[EmmaX.Name] pulls back."
                    $ EmmaX.Statup("Obed", 90, 1)
                    $ EmmaX.Statup("Obed", 50, 1)
                    $ EmmaX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")      
                    $ EmmaX.AddWord(1,"refused","refused")  
                    return          
            #end auto
            
    if not EmmaX.Forced and Situation != "auto":
        $ Tempmod = 0
        if EmmaX.PantsNum() > 6:
            $ Tempmod = 15
        call Bottoms_Off(EmmaX)
        if "angry" in EmmaX.RecentActions:
            return  
            
    $ Tempmod = 0  
    if not EmmaX.LickP:        
        if EmmaX.Forced:
            $ EmmaX.Statup("Love", 90, -30)
            $ EmmaX.Statup("Obed", 70, 35)
            $ EmmaX.Statup("Inbt", 80, 75) 
        else:
            $ EmmaX.Statup("Love", 90, 35)
            $ EmmaX.Statup("Obed", 70, 15)
            $ EmmaX.Statup("Inbt", 80, 35)
    if Taboo:
        $ EmmaX.Inbt += int(Taboo/10)  
        $ EmmaX.Lust += int(Taboo/5)
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
        
    if EmmaX.PantsNum() == 5:
        $ EmmaX.Upskirt = 1  
        $ EmmaX.SeenPanties = 1
    call Emma_First_Bottomless(1)
    
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ EmmaX.DrainWord("tabno")
    $ EmmaX.DrainWord("no lick pussy")
    $ EmmaX.RecentActions.append("lick pussy")                      
    $ EmmaX.DailyActions.append("lick pussy") 
    
label Emma_LP_Cycle: #Repeating strokes
    if Trigger2 == "kiss you":
            $ Trigger2 = 0   
    while Round >=0:  
        call Shift_Focus(EmmaX) 
        call Emma_Pussy_Launch("lick pussy")
        $ EmmaX.LustFace()   
        
        if  Player.Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                                              
                        "Slap her ass":                     
                                    call Slap_Ass(EmmaX)  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Emma_LP_Cycle  
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."                
                                    $ Player.FocusX = 0
                                    
                        "Other options":
                                menu:   
                                    "Offhand action":
                                            if EmmaX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ EmmaX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(EmmaX,"tired")   
                                                
                                    "Shift primary action":
                                            if EmmaX.Action and MultiAction:
                                                    menu:                                                             
                                                        "Pull out and start rubbing again.":
                                                                if EmmaX.Action and MultiAction:
                                                                    $ Situation = "pullback"
                                                                    call Emma_LP_After
                                                                    call Emma_Fondle_Pussy
                                                                else:
                                                                    call Sex_Basic_Dialog(EmmaX,"tired")   
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Emma_LP_After
                                                                call Emma_Dildo_Pussy  
                                                        "Never Mind":
                                                                jump Emma_LP_Cycle
                                            else: 
                                                call Sex_Basic_Dialog(EmmaX,"tired")            
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Emma_LP_After
                                                call Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(EmmaX)
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(EmmaX) 
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0   
                                                        
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(EmmaX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_LP_Cycle 
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_LP_Cycle 
                                            "Never mind":
                                                        jump Emma_LP_Cycle 
                                    "Undress [EmmaX.Name]":
                                            call Girl_Undress(EmmaX)   
                                    "Clean up [EmmaX.Name] (locked)" if not EmmaX.Spunk:
                                            pass  
                                    "Clean up [EmmaX.Name]" if EmmaX.Spunk:
                                            call Girl_Cleanup(EmmaX,"ask")                                         
                                    "Never mind":
                                            jump Emma_LP_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Emma_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Emma_LP_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Emma_Pos_Reset
                                    $ Line = 0
                                    jump Emma_LP_After
        #End menu (if Line)
        
        if EmmaX.Panties or EmmaX.PantsNum() > 6 or EmmaX.HoseNum() >= 5: #This checks if [EmmaX.Name] wants to strip down.
                call Girl_Undress(EmmaX,"auto")
                
        call Shift_Focus(EmmaX)    
        call Sex_Dialog(EmmaX,Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or EmmaX.Lust >= 100: 
                    #If either of you could cum   
                    if Player.Focus >= 100:    
                            #If you can cum:                                                 
                            call Player_Cumming(EmmaX)
                            if "angry" in EmmaX.RecentActions:  
                                call Emma_Pos_Reset
                                return    
                            $ EmmaX.Statup("Lust", 200, 5) 
                            if 100 > EmmaX.Lust >= 70 and EmmaX.OCount < 2:             
                                $ EmmaX.RecentActions.append("unsatisfied")                      
                                $ EmmaX.DailyActions.append("unsatisfied") 
                            
                            if Player.Focus > 80:
                                jump Emma_LP_After 
                            $ Line = "came"
     
                    if EmmaX.Lust >= 100:  
                            #If [EmmaX.Name] can cum                                             
                            call Girl_Cumming(EmmaX)
                            if Situation == "shift" or "angry" in EmmaX.RecentActions:
                                jump Emma_LP_After
                       
                    if Line == "came": #ex Player.Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in EmmaX.RecentActions:#And [EmmaX.Name] is unsatisfied,  
                                    "[EmmaX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it" 
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Emma_LP_After  
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)            
        #End orgasm
        
        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0
        
        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif Cnt == (5 + EmmaX.LickP):
                    $ EmmaX.Brows = "confused"
                    ch_e "Isn't it just delicious?"  
        elif EmmaX.Lust >= 80:
                    pass
        elif Cnt == (15 + EmmaX.LickP) and EmmaX.SEXP >= 15 and not ApprovalCheck(EmmaX, 1500):
                    $ EmmaX.Brows = "confused"        
                    menu:
                        ch_e "[EmmaX.Petname], I know you're having fun down there, but maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Emma_LP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Emma_LP_After
                        "No, this is fun.":   
                                if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):                        
                                    $ EmmaX.Statup("Love", 200, -5)
                                    $ EmmaX.Statup("Obed", 50, 3)                    
                                    $ EmmaX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ EmmaX.FaceChange("angry", 1)   
                                    call Emma_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_e "Well perhaps you are enjoying yourself, but I'm tired of this."                         
                                    $ EmmaX.Statup("Love", 50, -3, 1)
                                    $ EmmaX.Statup("Love", 80, -4, 1)
                                    $ EmmaX.Statup("Obed", 30, -1, 1)                    
                                    $ EmmaX.Statup("Obed", 50, -1, 1)  
                                    $ EmmaX.RecentActions.append("angry")
                                    $ EmmaX.DailyActions.append("angry")   
                                    jump Emma_LP_After
        #End Count check
           
        call Escalation(EmmaX) #sees if she wants to escalate things
        
        if Round == 10:
            ch_e "It's getting late. . ."  
        elif Round == 5:
            ch_e "We should take a break soon."        
    
    #Round = 0 loop breaks
    $ EmmaX.FaceChange("bemused", 0)
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."
    
    
label Emma_LP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Emma_Pos_Reset
        
    $ EmmaX.FaceChange("sexy") 
    
    $ EmmaX.LickP += 1  
    $ EmmaX.Action -=1     
    if EmmaX.PantsNum() <= 6 or EmmaX.Upskirt:        
        $ EmmaX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ EmmaX.Addictionrate += 1
    
    if Partner == "Rogue":
        call Partner_Like(EmmaX,3,2)
    else:
        call Partner_Like(EmmaX,2)
     
    if EmmaX.LickP == 1:            
            $ EmmaX.SEXP += 10         
            if not Situation: 
                if EmmaX.Love >= 500 and "unsatisfied" not in EmmaX.RecentActions:
                    ch_e "I could really take advantage of your services more often. . ."
                elif EmmaX.Obed <= 500 and Player.Focus <= 20:
                    $ EmmaX.FaceChange("perplexed", 1)
                    ch_e "I suppose that worked out for both of us. . ."
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_e "Oh? What did you have in mind?"
    call Checkout
    return   


# end EmmaX.Lick Pussy /////////////////////////////////////////////////////////////////////////////

    
# ////////////////////////////////////////////////////////////////////////Start Fondle Ass    
label Emma_Fondle_Ass: 
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(EmmaX)
                                                                                     # Will she let you fondle? Modifiers
    if EmmaX.FondleA: #You've done it before
        $ Tempmod += 10
    if EmmaX.PantsNum() > 6 or EmmaX.HoseNum() >= 5: # she's got pants on.
        $ Tempmod -= 5     
    if EmmaX.Lust > 75: #She's really horny
        $ Tempmod += 15
    if "exhibitionist" in EmmaX.Traits:
        $ Tempmod += Taboo  
    if "dating" in EmmaX.Traits or "sex friend" in EmmaX.Petnames:
        $ Tempmod += 10
    elif "ex" in EmmaX.Traits:
        $ Tempmod -= 25 
    if EmmaX.ForcedCount and not EmmaX.Forced:
        $ Tempmod -= 5 * EmmaX.ForcedCount      
    
    if Taboo and "tabno" in EmmaX.DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in EmmaX.History:                   
        $ Tempmod -= 20 
        
    if "no fondle ass" in EmmaX.DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle ass" in EmmaX.RecentActions else 0   
        
    $ Approval = ApprovalCheck(EmmaX, 850, TabM=1) # 85, 100, 115, Taboo -40(125)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:  
            $ EmmaX.FaceChange("surprised", 1)  
            $ EmmaX.Statup("Obed", 70, 2)
            $ EmmaX.Statup("Inbt", 40, 2) 
            "As your hand creeps down her backside, [EmmaX.Name] jumps a bit, and then relaxes."              
            $ EmmaX.FaceChange("sexy")  
            jump Emma_FA_Prep  
        else:          
            $ EmmaX.FaceChange("surprised")
            $ EmmaX.Statup("Obed", 50, -3)
            ch_e "Hands off, [EmmaX.Petname]."   
            $ EmmaX.FaceChange("bemused")
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        $ EmmaX.FaceChange("surprised")   
        $ EmmaX.Brows = "sad"        
        if EmmaX.Lust > 80:
            $ EmmaX.Statup("Love", 70, -4)
        $ EmmaX.Statup("Obed", 90, 1)
        $ EmmaX.Statup("Obed", 70, 2)
        "As your finger slides out, [EmmaX.Name] gasps and looks upset."              
        jump Emma_FA_Prep     
    elif "fondle ass" in EmmaX.RecentActions:
        $ EmmaX.FaceChange("sexy", 1)
        ch_e "Mmmm, again? I suppose. . ."
        jump Emma_FA_Prep
    elif "fondle ass" in EmmaX.DailyActions:
        $ EmmaX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Perhaps not so rough this time?",
            "Mmm. . ."]) 
        ch_e "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .        
        if EmmaX.Forced:
            $ EmmaX.FaceChange("sad")
            $ EmmaX.Statup("Love", 70, -2, 1)
            $ EmmaX.Statup("Obed", 90, 2)
            $ EmmaX.Statup("Inbt", 60, 2)
            ch_e "If you insist. . ."   
        else:
            $ EmmaX.FaceChange("bemused, 1") 
            ch_e "I can't exactly refuse. . ."   
        $ EmmaX.Statup("Lust", 200, 3)
        $ EmmaX.Statup("Obed", 60, 1)
        $ EmmaX.Statup("Inbt", 70, 1) 
        jump Emma_FA_Prep
        
    else:                                                                               #She's not into it, but maybe. . .            
        $ EmmaX.FaceChange("angry", 1)
        if "no fondle ass" in EmmaX.RecentActions:  
            ch_e "Your persistance is doing you no favors, [EmmaX.Petname]."
        elif Taboo and "tabno" in EmmaX.DailyActions and "no fondle ass" in EmmaX.DailyActions:  
            ch_e "I told you not to touch me like that in public!" 
        elif "no fondle ass" in EmmaX.DailyActions:       
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "tabno" in EmmaX.DailyActions:  
            ch_e "As I said, not here, [EmmaX.Petname]."  
        elif not EmmaX.FondleA:
            $ EmmaX.FaceChange("bemused")
            ch_e "Not yet, [EmmaX.Petname]. . ."
        else:
            $ EmmaX.FaceChange("bemused")
            ch_e "Let's not, ok [EmmaX.Petname]?"
        menu:
            extend ""
            "Sorry, never mind." if "no fondle ass" in EmmaX.DailyActions:
                $ EmmaX.FaceChange("bemused")
                ch_e "I appreciate your restraint, [EmmaX.Petname]."              
                return
            "Maybe later?" if "no fondle ass" not in EmmaX.DailyActions:
                $ EmmaX.FaceChange("sexy")  
                ch_e "Perhaps."
                $ EmmaX.Statup("Love", 80, 2)
                $ EmmaX.Statup("Inbt", 50, 2)  
                if Taboo:                    
                    $ EmmaX.RecentActions.append("tabno")                      
                    $ EmmaX.DailyActions.append("tabno") 
                $ EmmaX.RecentActions.append("no fondle ass")                      
                $ EmmaX.DailyActions.append("no fondle ass")            
                return
            "Just one good squeeze?":             
                if Approval:
                    $ EmmaX.FaceChange("sexy")     
                    $ EmmaX.Statup("Obed", 90, 1)
                    $ EmmaX.Statup("Obed", 50, 2)
                    ch_e "I do enjoy hearing you beg. . ."                           
                    $ EmmaX.Statup("Inbt", 70, 1) 
                    $ EmmaX.Statup("Inbt", 40, 2) 
                    jump Emma_FA_Prep
                else:   
                    $ EmmaX.FaceChange("sexy") 
                    ch_e "No."     
            
            "[[Start fondling anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck(EmmaX, 250, "OI", TabM = 3) # 25, 40, 55, -120(145)
                if Approval > 1 or (Approval and EmmaX.Forced):
                    $ EmmaX.FaceChange("sad")
                    $ EmmaX.Statup("Love", 70, -3, 1)
                    $ EmmaX.Statup("Love", 200, -1) 
                    ch_e "Fine, I suppose."                
                    $ EmmaX.Statup("Obed", 50, 3)
                    $ EmmaX.Statup("Inbt", 60, 3) 
                    if Approval < 2:                          
                        $ EmmaX.Forced = 1
                    jump Emma_FA_Prep
                else:                              
                    $ EmmaX.Statup("Love", 200, -10)  
                    $ EmmaX.FaceChange("angry", 1)
                    "She slaps your hand away."   
                    $ EmmaX.RecentActions.append("angry")
                    $ EmmaX.DailyActions.append("angry")   
                        
    if "no fondle ass" in EmmaX.DailyActions:
        ch_e "I don't appreciate having to repeat myself, [EmmaX.Petname]."   
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")   
    elif EmmaX.Forced:
        $ EmmaX.FaceChange("angry", 1)
        ch_e "Do you want to keep those fingers?"
        $ EmmaX.Statup("Lust", 60, 5)    
        $ EmmaX.Statup("Obed", 50, -2)   
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")   
    elif Taboo:
        $ EmmaX.FaceChange("angry", 1)    
        $ EmmaX.RecentActions.append("tabno")   
        $ EmmaX.DailyActions.append("tabno") 
        ch_e "I have a reputation to maintain."                   
    elif EmmaX.FondleA:
        $ EmmaX.FaceChange("sad")
        ch_e "I'm sorry, keep your hands to yourself."        
    else:
        $ EmmaX.FaceChange("sexy") 
        $ EmmaX.Mouth = "sad"
        ch_e "No."
    $ EmmaX.RecentActions.append("no fondle ass")                      
    $ EmmaX.DailyActions.append("no fondle ass") 
    $ Tempmod = 0    
    return
        
ch_e "Sorry, I don't even know how I got here. . ."
return

label Emma_FA_Prep: #Animation set-up  
    if Trigger2 == "fondle ass":
        return
    if not EmmaX.Forced and Situation != "auto":
        $ Tempmod = 0
        call Bottoms_Off(EmmaX)
        if "angry" in EmmaX.RecentActions:
            return    
    $ Tempmod = 0      
    call Emma_Pussy_Launch("fondle ass")
    if not EmmaX.FondleA:        
        if EmmaX.Forced:
            $ EmmaX.Statup("Love", 90, -20)
            $ EmmaX.Statup("Obed", 70, 20)
            $ EmmaX.Statup("Inbt", 80, 15) 
        else:
            $ EmmaX.Statup("Love", 90, 10)
            $ EmmaX.Statup("Obed", 70, 12)
            $ EmmaX.Statup("Inbt", 80, 20)
    if Taboo:
        $ EmmaX.Inbt += int(Taboo/10)  
        $ EmmaX.Lust += int(Taboo/5)
     
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0   
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ EmmaX.DrainWord("tabno")
    $ EmmaX.DrainWord("no fondle ass")
    $ EmmaX.RecentActions.append("fondle ass")                      
    $ EmmaX.DailyActions.append("fondle ass") 
    
label Emma_FA_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus(EmmaX) 
        call Emma_Pussy_Launch("fondle ass")
        $ EmmaX.LustFace()   
        
        if  Player.Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                                              
                        "Slap her ass":                     
                                    call Slap_Ass(EmmaX)  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Emma_FA_Cycle  
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."                
                                    $ Player.FocusX = 0
                                    
                        "Other options":
                                menu:   
                                    "Offhand action":
                                            if EmmaX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ EmmaX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(EmmaX,"tired")   
                                                
                                    "Shift primary action":
                                            if EmmaX.Action and MultiAction:
                                                    menu:                                                             
                                                        "I want to stick a finger in.":
                                                                $ Situation = "shift"
                                                                call Emma_FA_After
                                                                call Emma_Insert_Ass    
                                                        "Just stick a finger in without asking.":
                                                                $ Situation = "auto"
                                                                call Emma_FA_After
                                                                call Emma_Insert_Ass
                                                        "I want to lick your asshole.":
                                                                $ Situation = "shift"
                                                                call Emma_FA_After
                                                                call Emma_Lick_Ass                 
                                                        "Just start licking.":
                                                                $ Situation = "auto"
                                                                call Emma_FA_After
                                                                call Emma_Lick_Ass    
                                                        "I want to stick a dildo in.":                                                                
                                                                $ Situation = "shift"
                                                                call Emma_FA_After
                                                                call Emma_Dildo_Ass  
                                                        "Never Mind":
                                                                jump Emma_FA_Cycle
                                            else: 
                                                call Sex_Basic_Dialog(EmmaX,"tired")            
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Emma_FA_After
                                                call Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(EmmaX)
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(EmmaX) 
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0   
                                                        
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(EmmaX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_FA_Cycle 
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_FA_Cycle 
                                            "Never mind":
                                                        jump Emma_FA_Cycle 
                                    "Undress [EmmaX.Name]":
                                            call Girl_Undress(EmmaX)   
                                    "Clean up [EmmaX.Name] (locked)" if not EmmaX.Spunk:
                                            pass  
                                    "Clean up [EmmaX.Name]" if EmmaX.Spunk:
                                            call Girl_Cleanup(EmmaX,"ask")                                         
                                    "Never mind":
                                            jump Emma_FA_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Emma_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Emma_FA_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Emma_Pos_Reset
                                    $ Line = 0
                                    jump Emma_FA_After
        #End menu (if Line)
        
        if EmmaX.Panties or EmmaX.PantsNum() > 6 or EmmaX.HoseNum() >= 5: #This checks if [EmmaX.Name] wants to strip down.
                call Girl_Undress(EmmaX,"auto")
                
        call Shift_Focus(EmmaX)    
        call Sex_Dialog(EmmaX,Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or EmmaX.Lust >= 100: 
                    #If either of you could cum   
                    if Player.Focus >= 100:    
                            #If you can cum:                                                 
                            call Player_Cumming(EmmaX)
                            if "angry" in EmmaX.RecentActions:  
                                call Emma_Pos_Reset
                                return    
                            $ EmmaX.Statup("Lust", 200, 5) 
                            if 100 > EmmaX.Lust >= 70 and EmmaX.OCount < 2 and EmmaX.SEXP >= 20:             
                                $ EmmaX.RecentActions.append("unsatisfied")                      
                                $ EmmaX.DailyActions.append("unsatisfied") 
                            
                            if Player.Focus > 80:
                                jump Emma_FA_After 
                            $ Line = "came"
     
                    if EmmaX.Lust >= 100:  
                            #If [EmmaX.Name] can cum                                             
                            call Girl_Cumming(EmmaX)
                            if Situation == "shift" or "angry" in EmmaX.RecentActions:
                                jump Emma_FA_After
                       
                    if Line == "came": #ex Player.Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in EmmaX.RecentActions:#And [EmmaX.Name] is unsatisfied,  
                                    "[EmmaX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it" 
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Emma_FA_After   
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)            
        #End orgasm
        
        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0
                    
        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif Cnt == (5 + EmmaX.FondleA):
                    $ EmmaX.Brows = "confused"
                    ch_e "Mmmm I do enjoy that. . ."  
        elif EmmaX.Lust >= 80:
                    pass
        elif Cnt == (15 + EmmaX.FondleA) and EmmaX.SEXP >= 15 and not ApprovalCheck(EmmaX, 1500):
                    $ EmmaX.Brows = "confused"        
                    menu:
                        ch_e "[EmmaX.Petname], this is nice, but could we do something else?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Emma_FA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Emma_FA_After
                        "No, this is fun.":   
                                if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):                        
                                    $ EmmaX.Statup("Love", 200, -5)
                                    $ EmmaX.Statup("Obed", 50, 3)                    
                                    $ EmmaX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ EmmaX.FaceChange("angry", 1)   
                                    call Emma_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_e "Well perhaps you are enjoying yourself, but I'm tired of this."                         
                                    $ EmmaX.Statup("Love", 50, -3, 1)
                                    $ EmmaX.Statup("Love", 80, -4, 1)
                                    $ EmmaX.Statup("Obed", 30, -1, 1)                    
                                    $ EmmaX.Statup("Obed", 50, -1, 1)  
                                    $ EmmaX.RecentActions.append("angry")
                                    $ EmmaX.DailyActions.append("angry")   
                                    jump Emma_FA_After
        #End Count check
        
        call Escalation(EmmaX) #sees if she wants to escalate things
        
        if Round == 10:
            ch_e "It's getting late. . ."  
        elif Round == 5:
            ch_e "We should take a break soon."        
    
    #Round = 0 loop breaks
    $ EmmaX.FaceChange("bemused", 0)
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."
    
    
label Emma_FA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Emma_Pos_Reset
        
    $ EmmaX.FaceChange("sexy") 
    
    $ EmmaX.FondleA += 1  
    $ EmmaX.Action -=1            
    if EmmaX.PantsNum() <= 6 or EmmaX.Upskirt:        
        $ EmmaX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ EmmaX.Addictionrate += 1
    
        call Partner_Like(EmmaX,2)
     
    if EmmaX.FondleA == 1:            
            $ EmmaX.SEXP += 4         
            if not Situation: 
                if EmmaX.Love >= 500 and "unsatisfied" not in EmmaX.RecentActions:
                    ch_e "That was. . . nice. . ."
                elif EmmaX.Obed <= 500 and Player.Focus <= 20:
                    $ EmmaX.FaceChange("perplexed", 1)
                    ch_e "Did you enjoy that?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_e "Oh? What did you have in mind?"
    call Checkout
    return   


# end EmmaX.Fondle Ass /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Ass    
label Emma_Insert_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(EmmaX)
    
    if EmmaX.InsertA: #You've done it before
        $ Tempmod += 25
    if EmmaX.PantsNum() > 6 or EmmaX.HoseNum() >= 5: # she's got pants on.
        $ Tempmod -= 15    
    if EmmaX.Lust > 85: #She's really horny
        $ Tempmod += 15
    if EmmaX.Lust > 95:
        $ Tempmod += 5
    if Situation == "shift":
        $ Tempmod += 10
    if EmmaX.Lust > 85 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in EmmaX.Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in EmmaX.Traits or "sex friend" in EmmaX.Petnames:
        $ Tempmod += 10
    elif "ex" in EmmaX.Traits:
        $ Tempmod -= 25 
    if EmmaX.ForcedCount and not EmmaX.Forced:
        $ Tempmod -= 5 * EmmaX.ForcedCount
    
    if Taboo and "tabno" in EmmaX.DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in EmmaX.History:                   
        $ Tempmod -= 20 
        
    if "no insert ass" in EmmaX.DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no insert ass" in EmmaX.RecentActions else 0   
            
    $ Approval = ApprovalCheck(EmmaX, 1300, TabM = 3) # 130, 145, 160, Taboo -120(250)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            $ EmmaX.FaceChange("surprised")
            $ EmmaX.Statup("Obed", 90, 2)
            $ EmmaX.Statup("Obed", 70, 2)
            $ EmmaX.Statup("Inbt", 80, 2) 
            $ EmmaX.Statup("Inbt", 30, 2) 
            "As you slide a finger in, [EmmaX.Name] tightens around it in surprise, but seems into it."  
            $ EmmaX.FaceChange("sexy")           
            jump Emma_IA_Prep
        else:   
            $ EmmaX.FaceChange("surprised")
            $ EmmaX.Statup("Love", 80, -2)
            $ EmmaX.Statup("Obed", 50, -3)
            ch_e "Whoa, back off, [EmmaX.Petname]."                 
            $ Tempmod = 0
            $ Trigger2 = 0
            return          
    
    if "insert ass" in EmmaX.DailyActions:
        $ EmmaX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax, gently. . .",
            "Mmm. . ."]) 
        ch_e "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .               
        if EmmaX.Forced:
            $ EmmaX.FaceChange("sad")
            $ EmmaX.Statup("Love", 70, -3, 1)
            $ EmmaX.Statup("Love", 20, -2, 1)
            $ EmmaX.Statup("Obed", 90, 1)
            $ EmmaX.Statup("Inbt", 60, 1)
            ch_e "If you must. . ."    
        else:
            $ EmmaX.FaceChange("sexy", 1)
            $ EmmaX.Eyes = "closed"            
            $ EmmaX.Statup("Love", 90, 1)
            $ EmmaX.Statup("Inbt", 50, 3)            
            $ EmmaX.Statup("Lust", 200, 3)
            ch_e "Mmmmm. . ."                
        $ EmmaX.Statup("Obed", 20, 1)
        $ EmmaX.Statup("Obed", 60, 1)
        $ EmmaX.Statup("Inbt", 70, 2) 
        jump Emma_IA_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        $ EmmaX.FaceChange("angry", 1)
        if "no insert ass" in EmmaX.RecentActions:  
            ch_e "Your persistance is doing you no favors, [EmmaX.Petname]."
        elif Taboo and "tabno" in EmmaX.DailyActions and "no insert ass" in EmmaX.DailyActions:  
            ch_e "I told you that wasn't appropriate!" 
        elif "no insert ass" in EmmaX.DailyActions:       
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "tabno" in EmmaX.DailyActions:  
            ch_e "As I said, not here, [EmmaX.Petname]."  
        elif not EmmaX.InsertA:
            $ EmmaX.FaceChange("perplexed", 1)
            ch_e "That's really not my usual style. . ."
        else:
            $ EmmaX.FaceChange("bemused")
            ch_e "I'd rather not today. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no insert ass" in EmmaX.DailyActions:
                $ EmmaX.FaceChange("bemused")
                ch_e "I appreciate your restraint, [EmmaX.Petname]."              
                return
            "Maybe later?" if "no insert ass" not in EmmaX.DailyActions:
                $ EmmaX.FaceChange("sexy")  
                ch_e "It's. . . possible, [EmmaX.Petname]."
                $ EmmaX.Statup("Love", 80, 2)
                $ EmmaX.Statup("Inbt", 70, 2)   
                if Taboo:                    
                    $ EmmaX.RecentActions.append("tabno")                      
                    $ EmmaX.DailyActions.append("tabno") 
                $ EmmaX.RecentActions.append("no insert ass")                      
                $ EmmaX.DailyActions.append("no insert ass")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    $ EmmaX.FaceChange("sexy")           
                    $ EmmaX.Statup("Obed", 90, 2)
                    $ EmmaX.Statup("Obed", 50, 2)
                    ch_e "You're probably right. . ."      
                    $ EmmaX.Statup("Inbt", 70, 3) 
                    $ EmmaX.Statup("Inbt", 40, 2)
                    jump Emma_IA_Prep
                else:   
                    $ EmmaX.FaceChange("bemused") 
                    ch_e "I don't think that I would."     
            
            "[[Slide a finger in anyway]":                                               # Pressured into being fingered. 
                $ Approval = ApprovalCheck(EmmaX, 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                if Approval > 1 or (Approval and EmmaX.Forced):                    
                    $ EmmaX.FaceChange("surprised", 1)
                    $ EmmaX.Statup("Love", 70, -5, 1)
                    $ EmmaX.Statup("Love", 200, -2)                 
                    ch_e "Well hello there. . ."                     
                    $ EmmaX.FaceChange("sad")
                    $ EmmaX.Statup("Obed", 50, 4)
                    $ EmmaX.Statup("Inbt", 80, 1) 
                    $ EmmaX.Statup("Inbt", 60, 3)  
                    if Approval < 2:                          
                        $ EmmaX.Forced = 1
                    jump Emma_IA_Prep
                else:                              
                    $ EmmaX.Statup("Love", 200, -15)  
                    $ EmmaX.FaceChange("angry", 1)
                    "She slaps your hand away."   
                    $ EmmaX.RecentActions.append("angry")
                    $ EmmaX.DailyActions.append("angry")   
                    
    if "no insert ass" in EmmaX.DailyActions:
        ch_e "I don't appreciate having to repeat myself, [EmmaX.Petname]."   
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")   
    elif EmmaX.Forced:
        $ EmmaX.FaceChange("angry", 1)
        ch_e "I'm not going that far today."
        if EmmaX.Inbt > 50:
                $ EmmaX.Statup("Lust", 80, 10)  
        else:
                $ EmmaX.Statup("Lust", 50, 3)
        $ EmmaX.Statup("Obed", 50, -2)      
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")   
    elif Taboo:
        $ EmmaX.FaceChange("angry", 1)    
        $ EmmaX.RecentActions.append("tabno")                   
        $ EmmaX.DailyActions.append("tabno") 
        ch_e "I have a reputation to maintain."                   
    elif EmmaX.InsertA:
        $ EmmaX.FaceChange("sad") 
        ch_e "I don't feel like it."    
    else:
        $ EmmaX.FaceChange("surprised")
        ch_e "Not today, [EmmaX.Petname]."
        $ EmmaX.FaceChange()
    $ EmmaX.RecentActions.append("no insert ass")                      
    $ EmmaX.DailyActions.append("no insert ass") 
    $ Tempmod = 0    
    return
    
        
label Emma_IA_Prep: #Animation set-up 
    if Trigger2 == "insert ass":
        return
            
    call Emma_Pussy_Launch("insert ass")
    
    if Situation == EmmaX:                                                         
            #Emma auto-starts    
            $ Situation = 0
            if (EmmaX.Legs and not EmmaX.Upskirt) or (EmmaX.Panties and not EmmaX.PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck(EmmaX, 1250, TabM = 1) or (EmmaX.SeenPussy and ApprovalCheck(EmmaX, 500) and not Taboo):
                        $ EmmaX.Upskirt = 1
                        $ EmmaX.PantiesDown = 1
                        $ Line = 0
                        if EmmaX.PantsNum() == 5:
                            $ Line = EmmaX.Name + " hikes up her skirt"
                        elif EmmaX.PantsNum() >= 6:
                            $ Line = EmmaX.Name + " pulls down her " + EmmaX.Legs
                        else:
                            $ Line = 0                            
                        if EmmaX.Panties:
                            if Line:
                                #wearing pants
                                "[Line] and pulls her [EmmaX.Panties] out of the way."
                                "She then grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
                            else:
                                #no pants
                                "She pulls her [EmmaX.Panties] out of the way, and then presses your hand against her asshole."
                                "She clearly intends for you to get to work." 
                        else:
                                #pants but no panties
                                "[Line], and then presses your hand against her asshole."
                                "She clearly intends for you to get to work."                     
                        call Emma_First_Bottomless(1)
                else:
                        "[EmmaX.Name] grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
            else:
                        "[EmmaX.Name] grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":                    
                    $ EmmaX.Statup("Inbt", 80, 3) 
                    $ EmmaX.Statup("Inbt", 50, 2)
                    "You press your finger into it."
                "Praise her.":       
                    $ EmmaX.FaceChange("sexy", 1)                    
                    $ EmmaX.Statup("Inbt", 80, 3) 
                    ch_p "Dirty girl, [EmmaX.Pet]."
                    $ EmmaX.NameCheck() #checks reaction to petname
                    "You press your finger into it."
                    $ EmmaX.Statup("Love", 85, 1)
                    $ EmmaX.Statup("Obed", 90, 1)
                    $ EmmaX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your hand back."
                    $ EmmaX.FaceChange("surprised")       
                    $ EmmaX.Statup("Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [EmmaX.Pet]."
                    $ EmmaX.NameCheck() #checks reaction to petname
                    "[EmmaX.Name] pulls back."
                    $ EmmaX.Statup("Obed", 90, 1)
                    $ EmmaX.Statup("Obed", 50, 1)
                    $ EmmaX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")      
                    $ EmmaX.AddWord(1,"refused","refused")  
                    return          
            #end auto
           
    if not EmmaX.Forced and Situation != "auto":
        $ Tempmod = 0
        call Bottoms_Off(EmmaX)
        if "angry" in EmmaX.RecentActions:
            return    
            
    $ Tempmod = 0   
    if not EmmaX.InsertA:        
        if EmmaX.Forced:
            $ EmmaX.Statup("Love", 90, -50)
            $ EmmaX.Statup("Obed", 70, 60)
            $ EmmaX.Statup("Inbt", 80, 35) 
        else:
            $ EmmaX.Statup("Love", 90, 10)
            $ EmmaX.Statup("Obed", 70, 20)
            $ EmmaX.Statup("Inbt", 80, 25)
            
    if Taboo:
        $ EmmaX.Inbt += int(Taboo/10)  
        $ EmmaX.Lust += int(Taboo/5)
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0    
    $ Cnt = 0
    if Taboo:
        $ EmmaX.DrainWord("tabno")
    $ EmmaX.DrainWord("no insert ass")
    $ EmmaX.RecentActions.append("insert ass")                      
    $ EmmaX.DailyActions.append("insert ass") 
    
label Emma_IA_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus(EmmaX) 
        call Emma_Pussy_Launch("insert ass")
        $ EmmaX.LustFace()   
        
        if  Player.Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                                              
                        "Slap her ass":                     
                                    call Slap_Ass(EmmaX)  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Emma_IA_Cycle  
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."                
                                    $ Player.FocusX = 0
                                    
                        "Other options":
                                menu:   
                                    "Offhand action":
                                            if EmmaX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ EmmaX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(EmmaX,"tired")   
                                                
                                    "Shift primary action":
                                            if EmmaX.Action and MultiAction:
                                                    menu:                                                             
                                                        "Pull out and start rubbing again.":
                                                                $ Situation = "pullback"
                                                                call Emma_IA_After
                                                                call Emma_Fondle_Ass
                                                        "I want to lick your asshole.":
                                                                $ Situation = "shift"
                                                                call Emma_IA_After
                                                                call Emma_Lick_Ass                 
                                                        "Just start licking.":
                                                                $ Situation = "auto"
                                                                call Emma_IA_After
                                                                call Emma_Lick_Ass    
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Emma_IA_After
                                                                call Emma_Dildo_Ass  
                                                        "Never Mind":
                                                                jump Emma_IA_Cycle
                                            else: 
                                                call Sex_Basic_Dialog(EmmaX,"tired")            
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Emma_IA_After
                                                call Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(EmmaX)
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(EmmaX) 
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0   
                                                        
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(EmmaX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_IA_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass 
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_IA_Cycle 
                                            "Never mind":
                                                        jump Emma_IA_Cycle 
                                    "Undress [EmmaX.Name]":
                                            call Girl_Undress(EmmaX)   
                                    "Clean up [EmmaX.Name] (locked)" if not EmmaX.Spunk:
                                            pass  
                                    "Clean up [EmmaX.Name]" if EmmaX.Spunk:
                                            call Girl_Cleanup(EmmaX,"ask")                                         
                                    "Never mind":
                                            jump Emma_IA_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Emma_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Emma_IA_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Emma_Pos_Reset
                                    $ Line = 0
                                    jump Emma_IA_After
        #End menu (if Line)
        
        if EmmaX.Panties or EmmaX.PantsNum() > 6 or EmmaX.HoseNum() >= 5: #This checks if [EmmaX.Name] wants to strip down.
                call Girl_Undress(EmmaX,"auto")
                
        call Shift_Focus(EmmaX)    
        call Sex_Dialog(EmmaX,Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or EmmaX.Lust >= 100: 
                    #If either of you could cum   
                    if Player.Focus >= 100:    
                            #If you can cum:                                                 
                            call Player_Cumming(EmmaX)
                            if "angry" in EmmaX.RecentActions:  
                                call Emma_Pos_Reset
                                return    
                            $ EmmaX.Statup("Lust", 200, 5) 
                            if 100 > EmmaX.Lust >= 70 and EmmaX.OCount < 2:             
                                $ EmmaX.RecentActions.append("unsatisfied")                      
                                $ EmmaX.DailyActions.append("unsatisfied") 
                            
                            if Player.Focus > 80:
                                jump Emma_IA_After 
                            $ Line = "came"
     
                    if EmmaX.Lust >= 100:  
                            #If [EmmaX.Name] can cum                                             
                            call Girl_Cumming(EmmaX)
                            if Situation == "shift" or "angry" in EmmaX.RecentActions:
                                jump Emma_IA_After
                       
                    if Line == "came": #ex Player.Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in EmmaX.RecentActions:#And [EmmaX.Name] is unsatisfied,  
                                    "[EmmaX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it" 
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Emma_IA_After    
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)            
        #End orgasm
        
        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0
        
        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif Cnt == (5 + EmmaX.InsertA):
                    $ EmmaX.Brows = "confused"
                    ch_e "Ungh, You're getting going there. . ."  
        elif EmmaX.Lust >= 80:
                    pass
        elif Cnt == (15 + EmmaX.InsertA) and EmmaX.SEXP >= 15 and not ApprovalCheck(EmmaX, 1500):
                    $ EmmaX.Brows = "confused"        
                    menu:
                        ch_e "[EmmaX.Petname], this is getting kind sore, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Emma_IA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Emma_IA_After
                        "No, this is fun.":   
                                if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):                        
                                    $ EmmaX.Statup("Love", 200, -5)
                                    $ EmmaX.Statup("Obed", 50, 3)                    
                                    $ EmmaX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ EmmaX.FaceChange("angry", 1)   
                                    call Emma_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_e "Well perhaps you are enjoying yourself, but I'm tired of this."                         
                                    $ EmmaX.Statup("Love", 50, -3, 1)
                                    $ EmmaX.Statup("Love", 80, -4, 1)
                                    $ EmmaX.Statup("Obed", 30, -1, 1)                    
                                    $ EmmaX.Statup("Obed", 50, -1, 1)  
                                    $ EmmaX.RecentActions.append("angry")
                                    $ EmmaX.DailyActions.append("angry")   
                                    jump Emma_IA_After
        #End Count check
           
        call Escalation(EmmaX) #sees if she wants to escalate things
        
        if Round == 10:
            ch_e "It's getting late. . ."  
        elif Round == 5:
            ch_e "We should take a break soon."        
    
    #Round = 0 loop breaks
    $ EmmaX.FaceChange("bemused", 0)
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."
    
label Emma_IA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Emma_Pos_Reset
        
    $ EmmaX.FaceChange("sexy") 
    
    $ EmmaX.InsertA += 1  
    $ EmmaX.Action -=1            
    $ EmmaX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ EmmaX.Addictionrate += 1
    
    call Partner_Like(EmmaX,2)
     
    if EmmaX.InsertA == 1:            
            $ EmmaX.SEXP += 12         
            if not Situation: 
                if EmmaX.Love >= 500 and "unsatisfied" not in EmmaX.RecentActions:
                    ch_e "You certainly surprise me. . ."
                elif EmmaX.Obed <= 500 and Player.Focus <= 20:
                    $ EmmaX.FaceChange("perplexed", 1)
                    ch_e "Was it everything you dreamed?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_e "Oh? What did you have in mind?"
    call Checkout
    return   


# end EmmaX.Insert Ass /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Ass    
label Emma_Lick_Ass: 
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(EmmaX)
                                                                             # Will she let you lick? Modifiers         
    if EmmaX.LickA: #You've done it before
        $ Tempmod += 20
    if EmmaX.PantsNum() > 6 or EmmaX.HoseNum() >= 5: # she's got pants on.
        $ Tempmod -= 25 
    if EmmaX.Lust > 95:
        $ Tempmod += 20  
    elif EmmaX.Lust > 85: #She's really horny
        $ Tempmod += 15    
    if EmmaX.Lust > 85 and Situation == "auto": #auto
        $ Tempmod += 10 
    if Situation == "shift":
        $ Tempmod += 10
    if "exhibitionist" in EmmaX.Traits:
        $ Tempmod += (4*Taboo) 
    if "dating" in EmmaX.Traits or "sex friend" in EmmaX.Petnames:
        $ Tempmod += 10
    elif "ex" in EmmaX.Traits:
        $ Tempmod -= 25  
    if EmmaX.ForcedCount and not EmmaX.Forced:
        $ Tempmod -= 5 * EmmaX.ForcedCount 
    
    if Taboo and "tabno" in EmmaX.DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in EmmaX.History:                   
        $ Tempmod -= 20 
        
    if "no lick ass" in EmmaX.DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no lick ass" in EmmaX.RecentActions else 0   
            
    $ Approval = ApprovalCheck(EmmaX, 1550, TabM = 4) # 155, 170, 185, Taboo -160(315)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            $ EmmaX.FaceChange("surprised")   
            $ EmmaX.Statup("Obed", 90, 1)
            $ EmmaX.Statup("Inbt", 80, 3) 
            $ EmmaX.Statup("Inbt", 40, 2) 
            "As you crouch down and start to lick her asshole, [EmmaX.Name] startles briefly, but then begins to melt."  
            $ EmmaX.FaceChange("sexy")  
            jump Emma_LA_Prep
        else:   
            $ EmmaX.FaceChange("surprised")
            $ EmmaX.Statup("Love", 80, -2)
            $ EmmaX.Statup("Obed", 50, -3)
            ch_e "[EmmaX.Petname]! Not now. . ."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return  
    
    if "lick ass" in EmmaX.RecentActions:
        $ EmmaX.FaceChange("sexy", 1)
        ch_e "Mmmm, again? I suppose. . ."
        jump Emma_LA_Prep
    elif "lick ass" in EmmaX.DailyActions:
        $ EmmaX.FaceChange("sexy", 1)
        ch_e "You didn't get enough earlier?"
    
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if EmmaX.Forced:
            $ EmmaX.FaceChange("sad")
            $ EmmaX.Statup("Love", 70, -3, 1)
            $ EmmaX.Statup("Love", 20, -2, 1)
            $ EmmaX.Statup("Obed", 90, 2)
            $ EmmaX.Statup("Inbt", 60, 2)
            ch_e "If you must. . ."    
        else:
            $ EmmaX.FaceChange("sexy", 1)
            $ EmmaX.Eyes = "closed"            
            $ EmmaX.Statup("Love", 90, 1)
            $ EmmaX.Statup("Inbt", 60, 2)            
            $ EmmaX.Statup("Lust", 200, 3)
            ch_e "Mmm. . . naughty."                
        $ EmmaX.Statup("Obed", 20, 1)
        $ EmmaX.Statup("Obed", 60, 1)
        $ EmmaX.Statup("Inbt", 80, 2) 
        jump Emma_LA_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .           
        $ EmmaX.FaceChange("angry", 1)
        if "no lick ass" in EmmaX.RecentActions:  
            ch_e "Your persistance is doing you no favors, [EmmaX.Petname]."
        elif Taboo and "tabno" in EmmaX.DailyActions and "no lick ass" in EmmaX.DailyActions:  
            ch_e "I told you not to touch me like that in public!" 
        elif "no lick ass" in EmmaX.DailyActions:       
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "tabno" in EmmaX.DailyActions:  
            ch_e "As I said, not here, [EmmaX.Petname]."  
        elif not EmmaX.LickA:                    #First time dialog
            $ EmmaX.FaceChange("bemused", 1)
            if EmmaX.Love >= EmmaX.Obed and EmmaX.Love >= EmmaX.Inbt:            
                ch_e "Oh, are we there now?"
            elif EmmaX.Obed >= EmmaX.Inbt:            
                ch_e "Is that what gets you off?"
            else:
                $ EmmaX.Eyes = "sexy"
                ch_e "Hm, I didn't know that's what you were into."
        else:
            $ EmmaX.FaceChange("bemused")
            ch_e "Not now, [EmmaX.Petname]."  
        menu:
            extend ""
            "Sorry, never mind." if "no lick ass" in EmmaX.DailyActions:
                $ EmmaX.FaceChange("bemused")
                ch_e "I appreciate your restraint, [EmmaX.Petname]."              
                return
            "I'm sure I can convince you later. . ." if "no lick ass" not in EmmaX.DailyActions:
                $ EmmaX.FaceChange("sexy")  
                ch_e "Anything's possible, [EmmaX.Petname]."
                $ EmmaX.Statup("Love", 80, 2)
                $ EmmaX.Statup("Inbt", 70, 2)   
                if Taboo:                    
                    $ EmmaX.RecentActions.append("tabno")                      
                    $ EmmaX.DailyActions.append("tabno") 
                $ EmmaX.RecentActions.append("no lick ass")                      
                $ EmmaX.DailyActions.append("no lick ass")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    $ EmmaX.FaceChange("sexy")           
                    $ EmmaX.Statup("Obed", 90, 2)
                    $ EmmaX.Statup("Obed", 50, 2)
                    ch_e "Ok, you're probably right. . ."      
                    $ EmmaX.Statup("Inbt", 70, 3) 
                    $ EmmaX.Statup("Inbt", 40, 2)
                    jump Emma_LA_Prep
                else:   
                    $ EmmaX.FaceChange("sexy") 
                    ch_e "I really don't think so."        
            
            "[[Start licking anyway]":                                               # Pressured into being licked. 
                $ Approval = ApprovalCheck(EmmaX, 1100, "OI", TabM = 4) # 110, 125, 140, -160(270)
                if Approval > 1 or (Approval and EmmaX.Forced):
                    $ EmmaX.FaceChange("sad")
                    $ EmmaX.Statup("Love", 70, -5, 1)
                    $ EmmaX.Statup("Love", 200, -2)                 
                    ch_e "Suit yourself."  
                    $ EmmaX.Statup("Obed", 50, 4)
                    $ EmmaX.Statup("Inbt", 80, 1) 
                    $ EmmaX.Statup("Inbt", 60, 3)  
                    if Approval < 2:                          
                        $ EmmaX.Forced = 1
                    jump Emma_LA_Prep
                else:                              
                    $ EmmaX.Statup("Love", 200, -15)  
                    $ EmmaX.FaceChange("angry", 1)
                    "She shoves your head back."   
                    $ EmmaX.RecentActions.append("angry")
                    $ EmmaX.DailyActions.append("angry")   
                    
    if "no lick ass" in EmmaX.DailyActions:
        ch_e "I don't appreciate having to repeat myself, [EmmaX.Petname]."   
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")   
    elif EmmaX.Forced:
        $ EmmaX.FaceChange("angry", 1)
        ch_e "I don't think so."
        if EmmaX.Inbt > 50:
                $ EmmaX.Statup("Lust", 80, 10)  
        else:
                $ EmmaX.Statup("Lust", 50, 3)
        $ EmmaX.Statup("Obed", 50, -2)   
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")   
    elif Taboo:
        $ EmmaX.FaceChange("angry", 1)    
        $ EmmaX.RecentActions.append("tabno")                   
        $ EmmaX.DailyActions.append("tabno") 
        ch_e "I have a reputation to maintain."                   
    elif EmmaX.LickA:
        $ EmmaX.FaceChange("sad") 
        ch_e "Sorry, no more of that."    
    else:
        $ EmmaX.FaceChange("surprised")
        ch_e "I'm sorry, not now."
        $ EmmaX.FaceChange()
    $ EmmaX.RecentActions.append("no lick ass")                      
    $ EmmaX.DailyActions.append("no lick ass") 
    $ Tempmod = 0    
    return
        
label Emma_LA_Prep: #Animation set-up  
    if Trigger2 == "lick ass":
        return
    if not EmmaX.Forced and Situation != "auto":
        $ Tempmod = 0
        if EmmaX.PantsNum() > 6:
            $ Tempmod = 15
        call Bottoms_Off(EmmaX)
        if "angry" in EmmaX.RecentActions:
            return    
    $ Tempmod = 0  
    call Emma_Pussy_Launch("lick ass")
    if not EmmaX.LickA:        
        if EmmaX.Forced:
            $ EmmaX.Statup("Love", 90, -30)
            $ EmmaX.Statup("Obed", 70, 40)
            $ EmmaX.Statup("Inbt", 80, 80) 
        else:
            $ EmmaX.Statup("Love", 90, 35)
            $ EmmaX.Statup("Obed", 70, 25)
            $ EmmaX.Statup("Inbt", 80, 55)
    if Taboo:
        $ EmmaX.Inbt += int(Taboo/10)  
        $ EmmaX.Lust += int(Taboo/5)
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    
    $ EmmaX.Upskirt = 1
    if EmmaX.PantsNum() == 5:
        $ EmmaX.SeenPanties = 1
    call Emma_First_Bottomless(1)
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ EmmaX.DrainWord("tabno")
    $ EmmaX.DrainWord("no lick ass")
    
    $ EmmaX.RecentActions.append("lick") if "lick" not in EmmaX.RecentActions else EmmaX.RecentActions
    $ EmmaX.RecentActions.append("ass") if "ass" not in EmmaX.RecentActions else EmmaX.RecentActions
    $ EmmaX.RecentActions.append("lick ass")  
    
    $ EmmaX.DailyActions.append("lick") if "lick" not in EmmaX.DailyActions else EmmaX.RecentActions
    $ EmmaX.DailyActions.append("ass") if "ass" not in EmmaX.DailyActions else EmmaX.RecentActions                    
    $ EmmaX.DailyActions.append("lick ass")  
label Emma_LA_Cycle: #Repeating strokes
    if Trigger2 == "kiss you":
            $ Trigger2 = 0
    while Round >=0:  
        call Shift_Focus(EmmaX) 
        call Emma_Pussy_Launch("lick ass")
        $ EmmaX.LustFace()   
        
        if  Player.Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                                              
                        "Slap her ass":                     
                                    call Slap_Ass(EmmaX)  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Emma_LA_Cycle  
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."                
                                    $ Player.FocusX = 0
                                    
                        "Other options":
                                menu:   
                                    "Offhand action":
                                            if EmmaX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ EmmaX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(EmmaX,"tired")   
                                                
                                    "Shift primary action":
                                            if EmmaX.Action and MultiAction:
                                                    menu:                                                             
                                                        "Switch to fondling.":
                                                                $ Situation = "pullback"
                                                                call Emma_LA_After
                                                                call Emma_Fondle_Ass
                                                        "I want to stick a finger in.":
                                                                $ Situation = "shift"
                                                                call Emma_LA_After
                                                                call Emma_Insert_Ass                 
                                                        "Just stick a finger in [[without asking].":
                                                                $ Situation = "auto"
                                                                call Emma_LA_After
                                                                call Emma_Insert_Ass                        
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Emma_LA_After
                                                                call Emma_Dildo_Ass  
                                                        "Never Mind":
                                                                jump Emma_LA_Cycle
                                            else: 
                                                call Sex_Basic_Dialog(EmmaX,"tired")            
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Emma_LA_After
                                                call Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(EmmaX)
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(EmmaX) 
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0   
                                                        
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(EmmaX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_LA_Cycle 
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_LA_Cycle 
                                            "Never mind":
                                                        jump Emma_LA_Cycle 
                                    "Undress [EmmaX.Name]":
                                            call Girl_Undress(EmmaX)   
                                    "Clean up [EmmaX.Name] (locked)" if not EmmaX.Spunk:
                                            pass  
                                    "Clean up [EmmaX.Name]" if EmmaX.Spunk:
                                            call Girl_Cleanup(EmmaX,"ask")                                         
                                    "Never mind":
                                            jump Emma_LA_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Emma_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Emma_LA_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Emma_Pos_Reset
                                    $ Line = 0
                                    jump Emma_LA_After
        #End menu (if Line)
        
        if EmmaX.Panties or EmmaX.PantsNum() > 6 or EmmaX.HoseNum() >= 5: #This checks if [EmmaX.Name] wants to strip down.
                call Girl_Undress(EmmaX,"auto")
                
        call Shift_Focus(EmmaX)    
        call Sex_Dialog(EmmaX,Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or EmmaX.Lust >= 100: 
                    #If either of you could cum   
                    if Player.Focus >= 100:    
                            #If you can cum:                                                 
                            call Player_Cumming(EmmaX)
                            if "angry" in EmmaX.RecentActions:  
                                call Emma_Pos_Reset
                                return    
                            $ EmmaX.Statup("Lust", 200, 5) 
                            if 100 > EmmaX.Lust >= 70 and EmmaX.OCount < 2:             
                                $ EmmaX.RecentActions.append("unsatisfied")                      
                                $ EmmaX.DailyActions.append("unsatisfied") 
                            
                            if Player.Focus > 80:
                                jump Emma_LA_After 
                            $ Line = "came"
     
                    if EmmaX.Lust >= 100:  
                            #If [EmmaX.Name] can cum                                             
                            call Girl_Cumming(EmmaX)
                            if Situation == "shift" or "angry" in EmmaX.RecentActions:
                                jump Emma_LA_After
                       
                    if Line == "came": #ex Player.Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in EmmaX.RecentActions:#And [EmmaX.Name] is unsatisfied,  
                                    "[EmmaX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it" 
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Emma_LA_After   
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)            
        #End orgasm
        
        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0
                    
        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif Cnt == (5 + EmmaX.LickA):
                    $ EmmaX.Brows = "confused"
                    ch_e "You certainly are enthusiastic. . ."  
        elif EmmaX.Lust >= 80:
                    pass
        elif Cnt == (15 + EmmaX.LickA) and EmmaX.SEXP >= 15 and not ApprovalCheck(EmmaX, 1500):
                    $ EmmaX.Brows = "confused"        
                    menu:
                        ch_e "[EmmaX.Petname], this is getting weird, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Emma_LA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Emma_LA_After
                        "No, this is fun.":   
                                if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):                        
                                    $ EmmaX.Statup("Love", 200, -5)
                                    $ EmmaX.Statup("Obed", 50, 3)                    
                                    $ EmmaX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ EmmaX.FaceChange("angry", 1)   
                                    call Emma_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_e "Well perhaps you are enjoying yourself, but I'm tired of this."                         
                                    $ EmmaX.Statup("Love", 50, -3, 1)
                                    $ EmmaX.Statup("Love", 80, -4, 1)
                                    $ EmmaX.Statup("Obed", 30, -1, 1)                    
                                    $ EmmaX.Statup("Obed", 50, -1, 1)  
                                    $ EmmaX.RecentActions.append("angry")
                                    $ EmmaX.DailyActions.append("angry")   
                                    jump Emma_LA_After
        #End Count check
           
        call Escalation(EmmaX) #sees if she wants to escalate things
        
        if Round == 10:
            ch_e "It's getting late. . ."  
        elif Round == 5:
            ch_e "We should take a break soon."        
    
    #Round = 0 loop breaks
    $ EmmaX.FaceChange("bemused", 0)
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."
    
label Emma_LA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Emma_Pos_Reset
        
    $ EmmaX.FaceChange("sexy") 
    
    $ EmmaX.LickA += 1  
    $ EmmaX.Action -=1      
    if EmmaX.PantsNum() <= 6 or EmmaX.Upskirt:        
        $ EmmaX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ EmmaX.Addictionrate += 1
    
    call Partner_Like(EmmaX,2)
     
    if EmmaX.LickA == 1:            
            $ EmmaX.SEXP += 15         
            if not Situation: 
                if EmmaX.Love >= 500 and "unsatisfied" not in EmmaX.RecentActions:
                    ch_e "That was. . . invigorating."
                elif EmmaX.Obed <= 500 and Player.Focus <= 20:
                    $ EmmaX.FaceChange("perplexed", 1)
                    ch_e "Was it all you dreamed of?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_e "Oh? What did you have in mind?"
    call Checkout
    return   

# end EmmaX.Lick Ass /////////////////////////////////////////////////////////////////////////////

