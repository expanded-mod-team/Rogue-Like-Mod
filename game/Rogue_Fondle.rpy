# RogueX.Fondle /////////////////////////////////////////////////////////////////////////////
label Rogue_Fondle:    
    $ RogueX.Mouth = "smile"
    if not RogueX.Action:
        ch_r "I'm a bit worn out right now, [RogueX.Petname], maybe later."
        return
    menu:
        ch_r "Well where exactly were you interested in touching, [RogueX.Petname]?"
        "Your breasts?" if RogueX.Action:
                    jump Rogue_Fondle_Breasts
        "Suck your breasts?" if RogueX.Action and RogueX.SuckB:
                    jump Rogue_Suck_Breasts
        "Your thighs?" if RogueX.Action:
                    jump Rogue_Fondle_Thighs
        "Your pussy?" if RogueX.Action:
                    jump Rogue_Fondle_Pussy
        "Lick your pussy?" if RogueX.Action and RogueX.LickP:
                    jump Rogue_Lick_Pussy
        "Your Ass?" if RogueX.Action:
                    jump Rogue_Fondle_Ass
        "Never mind.":
                    return
    return


# RogueX.Fondle Breasts /////////////////////////////////////////////////////////////////////////////
label Rogue_Fondle_Breasts:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(RogueX)
    
    # Will she let you fondle? Modifiers
    if RogueX.FondleB: #You've done it before
        $ Tempmod += 15
    if RogueX.Lust > 75: #She's really horny
        $ Tempmod += 20
    if "exhibitionist" in RogueX.Traits:
        $ Tempmod += (3*Taboo)
    if "dating" in RogueX.Traits or "sex friend" in RogueX.Petnames:
        $ Tempmod += 10
    elif "ex" in RogueX.Traits:
        $ Tempmod -= 20
    if RogueX.ForcedCount and not RogueX.Forced:
        $ Tempmod -= 5 * RogueX.ForcedCount
    
    if Taboo and "tabno" in RogueX.DailyActions:        
        $ Tempmod -= 10 
        
    if "no fondle breasts" in RogueX.DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle breasts" in RogueX.RecentActions else 0        
        
    $ Approval = ApprovalCheck(RogueX, 950, TabM = 3) # 95, 110, 125 -120(215)
    
    if Situation == "auto":  
        if Approval:
            $ RogueX.FaceChange("sexy")       
            $ RogueX.Statup("Obed", 90, 1)
            $ RogueX.Statup("Obed", 70, 2)
            $ RogueX.Statup("Inbt", 70, 3)
            $ RogueX.Statup("Inbt", 30, 2)            
            "As you cup her breast, [RogueX.Name] gently nods."            
            jump Rogue_FB_Prep        
        else:   
            $ RogueX.FaceChange("surprised")
            $ RogueX.Brows = "confused"
            $ RogueX.Statup("Obed", 50, -2)
            ch_r "Ah, ah, Just keep doing what you were doing, [RogueX.Petname]."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
                    
    # fondle yes:    
    
    if Approval:                                                                       #Second time+ dialog        
        $ RogueX.FaceChange("sexy", 1)
        if RogueX.Forced: 
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Love", 70, -3, 1)
            $ RogueX.Statup("Love", 20, -2, 1)           
        elif not Taboo and "tabno" in RogueX.DailyActions:        
            ch_r "I guess this is private enough. . ."   
            
    if "fondle breasts" in RogueX.RecentActions:
        $ RogueX.FaceChange("sexy", 1)
        ch_r "Mmm, again? Ok."
        jump Rogue_FB_Prep
    elif "fondle breasts" in RogueX.DailyActions:
        $ RogueX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so hard this time though.",
            "Mmm. . ."]) 
        ch_r "[Line]"
            
    if Approval >= 2:             
        $ RogueX.FaceChange("bemused", 1)
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Love", 70, -3, 1)
            $ RogueX.Statup("Love", 20, -2, 1)
            $ RogueX.Statup("Obed", 90, 1)
            $ RogueX.Statup("Inbt", 60, 1)
        ch_r "Ok [RogueX.Petname], come and get'em."   
        $ RogueX.Statup("Love", 90, 1)
        $ RogueX.Statup("Inbt", 50, 3) 
        jump Rogue_FB_Prep
        
    else:
        $ RogueX.FaceChange("angry", 1)
        if "no fondle breasts" in RogueX.RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions and "no fondle breasts" in RogueX.DailyActions:  
            ch_r "I told you not to touch me like that in public!" 
        elif "no fondle breasts" in RogueX.DailyActions:       
            ch_r "I already told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions:  
            ch_r "I told you not in public!"  
        elif not RogueX.FondleB:
            $ RogueX.FaceChange("bemused")
            ch_r "I just don't think I'm ready yet, [RogueX.Petname]. . ."
        else:
            $ RogueX.FaceChange("bemused")
            ch_r "I'd really rather not."   
        menu:
            extend ""
            "Sorry, never mind." if "no fondle breasts" in RogueX.DailyActions:
                $ RogueX.FaceChange("bemused")
                ch_r "Ok, no problem, [RogueX.Petname]."              
                return
            "Maybe later?" if "no fondle breasts" not in RogueX.DailyActions:
                $ RogueX.FaceChange("sexy")  
                "She re-adjusts her cleavage."
                ch_r "I'll give it some thought, [RogueX.Petname]."
                $ RogueX.Statup("Love", 80, 1)
                $ RogueX.Statup("Love", 50, 1)
                $ RogueX.Statup("Inbt", 30, 2)    
                if Taboo:                    
                    $ RogueX.AddWord(1,"tabno","tabno")
                $ RogueX.RecentActions.append("no fondle breasts")                      
                $ RogueX.DailyActions.append("no fondle breasts")            
                return                
            "Come on, Please?":             
                if Approval:
                    $ RogueX.FaceChange("sexy")     
                    $ RogueX.Statup("Obed", 90, 1)
                    $ RogueX.Statup("Obed", 50, 2)
                    $ RogueX.Statup("Inbt", 60, 3)
                    $ RogueX.Statup("Inbt", 30, 2)
                    ch_r "Heh, I suppose I can hardly refuse ya when you use the magic words . . ."                
                    jump Rogue_FB_Prep
                else:   
                    $ RogueX.FaceChange("sexy") 
                    ch_r "I'm afraid not this time, sorry [RogueX.Petname]." 
            
            
            "[[Grab her chest anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck(RogueX, 350, "OI", TabM = 3) # 35, 50, 65
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.FaceChange("sad")
                    $ RogueX.Statup("Love", 70, -5, 1)
                    $ RogueX.Statup("Love", 20, -2, 1)                 
                    ch_r "Fine, if that's what you want."                         
                    $ RogueX.Statup("Obed", 90, 2)
                    $ RogueX.Statup("Obed", 50, 4)
                    $ RogueX.Statup("Inbt", 60, 3)   
                    if Approval < 2:                          
                        $ RogueX.Forced = 1
                    jump Rogue_FB_Prep
                else:                              
                    $ RogueX.Statup("Love", 200, -10)  
                    $ RogueX.FaceChange("angry", 1)
                    "She slaps your hand away."   
                    $ RogueX.AddWord(1,"angry","angry")   
    
    if "no fondle breasts" in RogueX.DailyActions:
        ch_r "Learn to take \"no\" for an answer, [RogueX.Petname]."   
        $ RogueX.AddWord(1,"angry","angry")  
    elif RogueX.Forced:
        $ RogueX.FaceChange("angry", 1)
        ch_r "I don't want you touching me."
        $ RogueX.Statup("Lust", 60, 5)    
        $ RogueX.Statup("Obed", 50, -2)   
        $ RogueX.AddWord(1,"angry","angry")    
    elif Taboo:
        $ RogueX.FaceChange("angry", 1)    
        $ RogueX.AddWord(1,"tabno","tabno")  
        ch_r "I really don't think this is the right place for that!"                   
    elif RogueX.FondleB:
        $ RogueX.FaceChange("sad")
        ch_r "Sorry, [RogueX.Petname], you aren't touching these again."        
    else:
        $ RogueX.FaceChange("sexy") 
        $ RogueX.Mouth = "sad"
        ch_r "Not hap'nin."    
    $ RogueX.RecentActions.append("no fondle breasts")                      
    $ RogueX.DailyActions.append("no fondle breasts") 
    $ Tempmod = 0   
    return 
            
   
label Rogue_FB_Prep: #Animation set-up          
    if Trigger == "kiss you": 
        $ Trigger = "fondle breasts" 
        return
        
    if Trigger2 == "fondle breasts": 
        return
    
    call Rogue_Breasts_Launch("fondle breasts")
    
    if Situation == RogueX:                                                                  
            #Rogue auto-starts    
            $ Situation = 0
            if (RogueX.Over or RogueX.Chest) and not RogueX.Uptop:
                #if she has some sort of top on. . .
                if ApprovalCheck(RogueX, 1250, TabM = 1) or (RogueX.SeenChest and ApprovalCheck(RogueX, 500) and not Taboo):
                        $ RogueX.Uptop = 1
                        $ Line = RogueX.Over if RogueX.Over else RogueX.Chest
                        "With a miscevious grin, [RogueX.Name] pulls her [Line] up over her breasts."
                        call Rogue_First_Topless(1)
                        $ Line = 0
                        "She then grabs your arm and shoves your hand against her breast, clearly intending you to get to work."
                else:
                        "[RogueX.Name] grabs your arm and shoves your hand against her covered breast, clearly intending you to get to work."
            else:
                        "[RogueX.Name] grabs your arm and shoves your hand against her breast, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":                    
                    $ RogueX.Statup("Inbt", 80, 3) 
                    $ RogueX.Statup("Inbt", 50, 2)
                    "You start to fondle it."
                "Praise her.":       
                    $ RogueX.FaceChange("sexy", 1)                    
                    $ RogueX.Statup("Inbt", 80, 3) 
                    ch_p "I like the initiative, [RogueX.Pet]."
                    $ RogueX.NameCheck() #checks reaction to petname
                    "You start to fondle it."
                    $ RogueX.Statup("Love", 85, 1)
                    $ RogueX.Statup("Obed", 90, 1)
                    $ RogueX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your hand back."
                    $ RogueX.FaceChange("surprised")       
                    $ RogueX.Statup("Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [RogueX.Pet]."
                    $ RogueX.NameCheck() #checks reaction to petname
                    "[RogueX.Name] pulls back."
                    $ RogueX.Statup("Obed", 90, 1)
                    $ RogueX.Statup("Obed", 50, 1)
                    $ RogueX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")      
                    $ RogueX.AddWord(1,"refused","refused")  
                    return          
            #end auto
        
    if not RogueX.Forced and Situation != "auto":
        $ Tempmod = 0
        call Top_Off(RogueX)
        if "angry" in RogueX.RecentActions:
            return
        
    $ Tempmod = 0  
    if not RogueX.FondleB:        
        if RogueX.Forced:
            $ RogueX.Statup("Love", 90, -20)
            $ RogueX.Statup("Obed", 70, 25)
            $ RogueX.Statup("Inbt", 80, 15) 
        else:
            $ RogueX.Statup("Love", 90, 10)
            $ RogueX.Statup("Obed", 70, 5)
            $ RogueX.Statup("Inbt", 80, 15) 
            
    if Taboo:
        $ RogueX.Inbt += int(Taboo/10)  
        $ RogueX.Lust += int(Taboo/5)        
    
    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0   
    $ Cnt = 0    
    if Taboo:
        $ RogueX.DrainWord("tabno")
    $ RogueX.DrainWord("no fondle breasts")
    $ RogueX.AddWord(0,"fondle breasts","fondle breasts")
    
label Rogue_FB_Cycle: #Repeating strokes    
    while Round >=0:  
        call Shift_Focus(RogueX) 
        call Rogue_Breasts_Launch("fondle breasts")
        $ RogueX.LustFace()   
        
        if Player.Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                         
                        "Slap her ass":                     
                                    call Slap_Ass(RogueX)  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Rogue_FB_Cycle  
                                    
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
                                            if RogueX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ RogueX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(RogueX,"tired")  # "I'm actually getting a little tired,"  
                                                
                                    "Shift primary action":
                                            if RogueX.Action and MultiAction:
                                                    menu:
                                                        "Ask to suck on them.":
                                                                if RogueX.Action and MultiAction:                        
                                                                    $ Situation = "shift"
                                                                    call Rogue_FB_After
                                                                    call Rogue_Suck_Breasts
                                                                else:
                                                                    call Sex_Basic_Dialog(RogueX,"tired") 
                                                        "Just suck on them without asking.":
                                                                if RogueX.Action and MultiAction:                            
                                                                    $ Situation = "auto"
                                                                    call Rogue_FB_After
                                                                    call Rogue_Suck_Breasts
                                                                else:
                                                                    "As you lean in to suck on her breast, she grabs your head and pushes back."
                                                                    call Sex_Basic_Dialog(RogueX,"tired")  # "I'm actually getting a little tired,"                                           
                                                        "Never Mind":
                                                                    jump Rogue_FB_Cycle
                                            else: 
                                                call Sex_Basic_Dialog(RogueX,"tired")  # "I'm actually getting a little tired,"           
                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:  
                                        menu:
                                            "Ask [RogueX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(RogueX)
                                            "Ask [RogueX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(RogueX)  
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0    
                                                        
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(RogueX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Rogue_FB_Cycle 
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Rogue_FB_Cycle 
                                            "Never mind":
                                                        jump Rogue_FB_Cycle 
                                    "Undress [RogueX.Name]":
                                            call Girl_Undress(RogueX)   
                                    "Clean up [RogueX.Name] (locked)" if not RogueX.Spunk:
                                            pass  
                                    "Clean up [RogueX.Name]" if RogueX.Spunk:
                                            call Girl_Cleanup(RogueX,"ask")                                         
                                    "Never mind":
                                            jump Rogue_FB_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Rogue_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Rogue_FB_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Rogue_Pos_Reset
                                    $ Line = 0
                                    jump Rogue_FB_After
        #End menu (if Line)
        
        call Shift_Focus(RogueX)
        call Sex_Dialog(RogueX,Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or RogueX.Lust >= 100: 
                    #If either of you could cum   
                    if Player.Focus >= 100:    
                            #If you can cum:                                                 
                            call Player_Cumming(RogueX)
                            if "angry" in RogueX.RecentActions:  
                                    call Rogue_Pos_Reset
                                    return    
                            $ RogueX.Statup("Lust", 200, 5) 
                            if 100 > RogueX.Lust >= 70 and RogueX.OCount < 2 and RogueX.SEXP >= 20:               
                                    $ RogueX.AddWord(0,"unsatisfied","unsatisfied")
                            if Player.Focus > 80:
                                    jump Rogue_FB_After 
                            $ Line = "came"
     
                    if RogueX.Lust >= 100:  
                            #If Rogue can cum                                             
                            call Girl_Cumming(RogueX)
                            if Situation == "shift" or "angry" in RogueX.RecentActions:
                                    jump Rogue_FB_After
                       
                    if Line == "came": #ex Player.Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not Player.Semen:
                                    "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in RogueX.RecentActions:#And Rogue is unsatisfied,  
                                "[RogueX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Rogue_FB_After    
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)            
        #End orgasm
        
        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0
        
        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
                    pass
        elif Cnt == (5 + RogueX.FondleB):
                    $ RogueX.Brows = "confused"
                    ch_r "You're just going at them, huh?" 
        elif RogueX.Lust >= 85:
                    pass  
        elif Cnt == (15 + RogueX.FondleB) and RogueX.SEXP >= 15 and not ApprovalCheck(RogueX, 1500):
                    $ RogueX.Brows = "confused" 
                    menu:
                        ch_r "I know you're having fun, but maybe we could try something else [RogueX.Petname]."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Rogue_FB_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Rogue_FB_After
                        "No, this is fun.":   
                                if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):                        
                                    $ RogueX.Statup("Love", 200, -5)
                                    $ RogueX.Statup("Obed", 50, 3)                    
                                    $ RogueX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ RogueX.FaceChange("angry", 1)   
                                    call Rogue_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_r "Well if that's your attitude, I don't need your \"help\"."                         
                                    $ RogueX.Statup("Love", 50, -3, 1)
                                    $ RogueX.Statup("Love", 80, -4, 1)
                                    $ RogueX.Statup("Obed", 30, -1, 1)                    
                                    $ RogueX.Statup("Obed", 50, -1, 1)  
                                    $ RogueX.AddWord(1,"angry","angry")    
                                    jump Rogue_FB_After
        #End Count check
           
        call Escalation(RogueX) #sees if she wants to escalate things
        
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
                
        if RogueX.Lust >= 50 and not RogueX.Uptop and (RogueX.Chest or RogueX.Over):
                $ RogueX.Uptop = 1
                "[RogueX.Name] shrugs and pulls her top open."   
                call Rogue_First_Topless
                      
    #Round = 0 loop breaks
    $ RogueX.FaceChange("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.Petname], that's enough of that for now."
    
label Rogue_FB_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Rogue_Pos_Reset
        
    $ RogueX.FaceChange("sexy") 
    
    $ RogueX.FondleB += 1  
    $ RogueX.Action -=1
    $ RogueX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ RogueX.Addictionrate += 1   
        
    call Partner_Like(RogueX,2)
     
    if RogueX.FondleB == 1:            
            $ RogueX.SEXP += 4         
            if not Situation: 
                if RogueX.Love >= 500 and "unsatisfied" not in RogueX.RecentActions:
                    ch_r "That was . . . real pleasant, [RogueX.Petname]."
                elif RogueX.Obed <= 500 and Player.Focus <= 20:
                    $ RogueX.FaceChange("perplexed", 1)
                    ch_r "Did you get your jollies?"
     
    $ Tempmod = 0  
    call Checkout
    return   

# End Fondle Breasts


# R Suck Breasts /////////////////////////////////////////////////////////////////////////////

label Rogue_Suck_Breasts:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(RogueX)
                                                                                        # Will she let you suck? Modifiers
    if RogueX.SuckB: #You've done it before
        $ Tempmod += 15
    if not RogueX.Chest and not RogueX.Over:
        $ Tempmod += 15
    if RogueX.Lust > 75: #She's really horny
        $ Tempmod += 20
    if RogueX.Lust > 75 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in RogueX.Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in RogueX.Traits or "sex friend" in RogueX.Petnames:
        $ Tempmod += 10
    elif "ex" in RogueX.Traits:
        $ Tempmod -= 25  
    if RogueX.ForcedCount and not RogueX.Forced:
        $ Tempmod -= 5 * RogueX.ForcedCount     
    
    if Taboo and "tabno" in RogueX.DailyActions:        
        $ Tempmod -= 10 
        
    if "no suck breasts" in RogueX.DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no suck breasts" in RogueX.RecentActions else 0   
        
    $ Approval = ApprovalCheck(RogueX, 1050, TabM = 4) # 105, 120, 135, Taboo -160(265)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ RogueX.FaceChange("sexy")       
            $ RogueX.Statup("Obed", 90, 1)
            $ RogueX.Statup("Obed", 70, 2)
            $ RogueX.Statup("Inbt", 70, 3)
            $ RogueX.Statup("Inbt", 30, 2)            
            "As you dive in, [RogueX.Name] seems a bit surprised, but just makes a little \"coo.\""              
            jump Rogue_SB_Prep      
        else:               
            $ RogueX.FaceChange("surprised")
            $ RogueX.Statup("Obed", 50, -2)
            ch_r "Hey, just keep doing what you were doing, [RogueX.Petname]."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
    
    if "suck breasts" in RogueX.RecentActions:
        $ RogueX.FaceChange("sexy", 1)
        ch_r "Mmm, again? Ok."
        jump Rogue_SB_Prep
    elif "suck breasts" in RogueX.DailyActions:
        $ RogueX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so hard this time though.",
            "Mmm. . ."]) 
        ch_r "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .
        $ RogueX.FaceChange("bemused", 1)
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Love", 70, -3, 1)
            $ RogueX.Statup("Love", 20, -2, 1)
            $ RogueX.Statup("Obed", 90, 1)
            $ RogueX.Statup("Inbt", 60, 1)
        ch_r "Ok [RogueX.Petname], come and get'em."   
        $ RogueX.Statup("Love", 90, 1)
        $ RogueX.Statup("Inbt", 50, 3) 
        jump Rogue_SB_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        $ RogueX.FaceChange("angry", 1)
        if "no suck breasts" in RogueX.RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions and "no suck breasts" in RogueX.DailyActions:  
            ch_r "I told you we can't do that in public!" 
        elif "no suck breasts" in RogueX.DailyActions:       
            ch_r "I already told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions:  
            ch_r "I told you not in public!"  
        elif not RogueX.SuckB:
            $ RogueX.FaceChange("bemused")
            ch_r "I just don't think I'm ready yet, [RogueX.Petname]. . ."
        else:
            $ RogueX.FaceChange("bemused")
            ch_r "I'd really rather not."  
        menu:
            extend ""
            "Sorry, never mind." if "no suck breasts" in RogueX.DailyActions:
                $ RogueX.FaceChange("bemused")
                ch_r "Yeah, fine, [RogueX.Petname]."              
                return
            "Maybe later?" if "no suck breasts" not in RogueX.DailyActions:
                $ RogueX.FaceChange("sexy")  
                ch_r "I'll give it some thought, [RogueX.Petname]."
                $ RogueX.Statup("Love", 80, 1)
                $ RogueX.Statup("Love", 50, 1)
                $ RogueX.Statup("Inbt", 30, 2)    
                if Taboo:                    
                    $ RogueX.AddWord(1,"tabno","tabno")  
                $ RogueX.RecentActions.append("no suck breasts")                      
                $ RogueX.DailyActions.append("no suck breasts")            
                return
            "Come on, Please?":             
                if Approval:
                    $ RogueX.FaceChange("sexy")     
                    $ RogueX.Statup("Obed", 90, 1)
                    $ RogueX.Statup("Obed", 50, 2)
                    $ RogueX.Statup("Inbt", 60, 3)
                    $ RogueX.Statup("Inbt", 30, 2)
                    ch_r "You better work your mouth that hard on these."                
                    jump Rogue_SB_Prep
                else:   
                    $ RogueX.FaceChange("sexy") 
                    ch_r "I'm afraid not this time, sorry [RogueX.Petname]."     
            
            "[[Start sucking anyway]":                                               # Pressured into licking. 
                $ Approval = ApprovalCheck(RogueX, 450, "OI", TabM = 3) # 45, 60, 75, -120(165)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.FaceChange("sad")
                    $ RogueX.Statup("Love", 70, -5, 1)
                    $ RogueX.Statup("Love", 20, -2, 1)                 
                    ch_r "Hmmph, well I guess you can go to town. . ."                         
                    $ RogueX.Statup("Obed", 90, 2)
                    $ RogueX.Statup("Obed", 50, 4)
                    $ RogueX.Statup("Inbt", 60, 3)  
                    if Approval < 2:                          
                        $ RogueX.Forced = 1
                    jump Rogue_SB_Prep
                else:                              
                    $ RogueX.Statup("Love", 200, -10)  
                    $ RogueX.FaceChange("angry", 1)
                    "She shoves your head back out."   
                    $ RogueX.AddWord(1,"angry","angry")   
                    
    if "no suck breasts" in RogueX.DailyActions:
        ch_r "Learn to take \"no\" for an answer, [RogueX.Petname]." 
        $ RogueX.AddWord(1,"angry","angry")  
    elif RogueX.Forced:
        $ RogueX.FaceChange("angry", 1)
        ch_r "I don't want your lips on me."
        $ RogueX.Statup("Lust", 60, 5)    
        $ RogueX.Statup("Obed", 50, -2)    
        $ RogueX.AddWord(1,"angry","angry")  
    elif Taboo:   
        $ RogueX.FaceChange("angry", 1)      
        $ RogueX.AddWord(1,"tabno","tabno")  
        ch_r "I really don't think this is the right place for that!"                   
    elif RogueX.SuckB:
        $ RogueX.FaceChange("sad")
        ch_r "Sorry, [RogueX.Petname], you aren't getting these in your mouth."            
    else:
        $ RogueX.FaceChange("sexy") 
        $ RogueX.Mouth = "sad"
        ch_r "Not hap'nin, [RogueX.Petname]."
    $ RogueX.RecentActions.append("no suck breasts")                      
    $ RogueX.DailyActions.append("no suck breasts") 
    $ Tempmod = 0    
    return
                      
        
ch_r "Sorry, I don't even know how I got here. . ."
return

label Rogue_SB_Prep:                                                                 #Animation set-up 
            
    if Trigger2 == "suck breasts":
        return
           
    call Rogue_Breasts_Launch("suck breasts")
        
    if Situation == RogueX:                                                        
            #Rogue auto-starts    
            $ Situation = 0
            if (RogueX.Over or RogueX.Chest) and not RogueX.Uptop:
                #if she has some sort of top on. . .
                if ApprovalCheck(RogueX, 1250, TabM = 1) or (RogueX.SeenChest and ApprovalCheck(RogueX, 500) and not Taboo):
                        $ RogueX.Uptop = 1
                        $ Line = RogueX.Over if RogueX.Over else RogueX.Chest
                        "With a miscevious grin, [RogueX.Name] pulls her [Line] up over her breasts."
                        call Rogue_First_Topless(1)
                        $ Line = 0
                        "She then grabs your head and shoves your face into her chest, clearly intending you to get to work."
                else:
                        "[RogueX.Name] grabs your head and shoves your face into her chest, clearly intending you to get to work."
            else:
                        "[RogueX.Name] grabs your head and shoves your face into her chest, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":                    
                        $ RogueX.Statup("Inbt", 80, 3) 
                        $ RogueX.Statup("Inbt", 50, 2)
                        "You start to run your tongue along her nipple."
                "Praise her.":       
                        $ RogueX.FaceChange("sexy", 1)                    
                        $ RogueX.Statup("Inbt", 80, 3) 
                        ch_p "Mmm, I like this, [RogueX.Pet]."
                        $ RogueX.NameCheck() #checks reaction to petname
                        "You start to fondle it."
                        $ RogueX.Statup("Love", 85, 1)
                        $ RogueX.Statup("Obed", 90, 1)
                        $ RogueX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                        "You pull your head back."
                        $ RogueX.FaceChange("surprised")       
                        $ RogueX.Statup("Inbt", 70, 1) 
                        ch_p "Let's not do that right now, [RogueX.Pet]."
                        $ RogueX.NameCheck() #checks reaction to petname
                        "[RogueX.Name] pulls away."
                        $ RogueX.Statup("Obed", 90, 1)
                        $ RogueX.Statup("Obed", 50, 1)
                        $ RogueX.Statup("Obed", 30, 2)
                        $ Player.RecentActions.append("nope")      
                        $ RogueX.AddWord(1,"refused","refused")  
                        return          
            #end auto
            
    if not RogueX.Forced and Situation != "auto":
        $ Tempmod = 0   
        call Top_Off(RogueX)
        if "angry" in RogueX.RecentActions:
            return
    
    $ Tempmod = 0   
    if not RogueX.SuckB:        
        if RogueX.Forced:
            $ RogueX.Statup("Love", 90, -25)
            $ RogueX.Statup("Obed", 70, 25)
            $ RogueX.Statup("Inbt", 80, 17) 
        else:
            $ RogueX.Statup("Love", 90, 10)
            $ RogueX.Statup("Obed", 70, 10)
            $ RogueX.Statup("Inbt", 80, 15) 
    
    if Taboo:
        $ RogueX.Inbt += int(Taboo/10)  
        $ RogueX.Lust += int(Taboo/5)
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0
    $ Line = 0     
    $ Cnt = 0   
    if Taboo:
        $ RogueX.DrainWord("tabno")
    $ RogueX.DrainWord("no suck breasts")
    $ RogueX.AddWord(0,"suck breasts","suck breasts")
    
label Rogue_SB_Cycle: #Repeating strokes   
    if Trigger2 == "kiss you":
            $ Trigger2 = 0
    while Round >=0:  
        call Shift_Focus(RogueX) 
        call Rogue_Breasts_Launch("suck breasts")
        $ RogueX.LustFace()   
        
        if  Player.Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                         
                        "Slap her ass":                     
                                    call Slap_Ass(RogueX)  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Rogue_SB_Cycle  
                                    
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
                                            if RogueX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ RogueX.Action -= 1
                                            else:
                                                    call Sex_Basic_Dialog(RogueX,"tired")  # "I'm actually getting a little tired,"  
                                                
                                    "Shift primary action":
                                            if RogueX.Action and MultiAction:
                                                    menu:
                                                        "Pull back to fondling.":  
                                                            if RogueX.Action and MultiAction:
                                                                $ Situation = "pullback"
                                                                call Rogue_SB_After
                                                                call Rogue_Fondle_Breasts
                                                            else:
                                                                "As you pull back, [RogueX.Name] pushes you back in close."
                                                                call Sex_Basic_Dialog(RogueX,"tired") 
                                                        "Never Mind":
                                                                jump Rogue_SB_Cycle
                                            else: 
                                                                call Sex_Basic_Dialog(RogueX,"tired")  # "I'm actually getting a little tired,"           
                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask [RogueX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(RogueX)
                                            "Ask [RogueX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(RogueX)  
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0    
                                                        
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(RogueX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Rogue_SB_Cycle 
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Rogue_SB_Cycle 
                                            "Never mind":
                                                        jump Rogue_SB_Cycle 
                                    "Undress [RogueX.Name]":
                                            call Girl_Undress(RogueX)   
                                    "Clean up [RogueX.Name] (locked)" if not RogueX.Spunk:
                                            pass  
                                    "Clean up [RogueX.Name]" if RogueX.Spunk:
                                            call Girl_Cleanup(RogueX,"ask")                                         
                                    "Never mind":
                                            jump Rogue_SB_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Rogue_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Rogue_SB_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Rogue_Pos_Reset
                                    $ Line = 0
                                    jump Rogue_SB_After
        #End menu (if Line)
        
        call Shift_Focus(RogueX)
        call Sex_Dialog(RogueX,Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or RogueX.Lust >= 100: 
                    #If either of you could cum   
                    if Player.Focus >= 100:    
                            #If you can cum:                                                 
                            call Player_Cumming(RogueX)
                            if "angry" in RogueX.RecentActions:  
                                call Rogue_Pos_Reset
                                return    
                            $ RogueX.Statup("Lust", 200, 5) 
                            if 100 > RogueX.Lust >= 70 and RogueX.OCount < 2:              
                                $ RogueX.AddWord(0,"unsatisfied","unsatisfied")
                            
                            if Player.Focus > 80:
                                jump Rogue_SB_After 
                            $ Line = "came"
     
                    if RogueX.Lust >= 100:  
                            #If Rogue can cum                                             
                            call Girl_Cumming(RogueX)
                            if Situation == "shift" or "angry" in RogueX.RecentActions:
                                jump Rogue_SB_After
                       
                    if Line == "came": #ex Player.Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."
                                                        
                            if "unsatisfied" in RogueX.RecentActions:#And Rogue is unsatisfied,  
                                "[RogueX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Rogue_SB_After    
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)            
        #End orgasm
        
        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0
        
        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
                    pass
        elif Cnt == (5 + RogueX.SuckB):
                    $ RogueX.Brows = "confused"
                    ch_r "You're just going at them, huh?"   
        elif RogueX.Lust >= 85:
                    pass
        elif Cnt == (15 + RogueX.SuckB) and RogueX.SEXP >= 15 and not ApprovalCheck(RogueX, 1500):
                    $ RogueX.Brows = "confused"        
                    menu:
                        ch_r "I know you're having fun, but maybe we could try something else [RogueX.Petname]."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Rogue_SB_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Rogue_SB_After
                        "No, this is fun.":   
                                if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):                        
                                    $ RogueX.Statup("Love", 200, -5)
                                    $ RogueX.Statup("Obed", 50, 3)                    
                                    $ RogueX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ RogueX.FaceChange("angry", 1)   
                                    call Rogue_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_r "Well if that's your attitude, I don't need your \"help\"."                         
                                    $ RogueX.Statup("Love", 50, -3, 1)
                                    $ RogueX.Statup("Love", 80, -4, 1)
                                    $ RogueX.Statup("Obed", 30, -1, 1)                    
                                    $ RogueX.Statup("Obed", 50, -1, 1)  
                                    $ RogueX.AddWord(1,"angry","angry")   
                                    jump Rogue_SB_After
        #End Count check
           
        call Escalation(RogueX) #sees if she wants to escalate things
        
        if Round == 10:
                ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
                ch_r "Seriously, it'll be time to stop soon."        
    
        if RogueX.Lust >= 50 and not RogueX.Uptop and (RogueX.Chest or RogueX.Over):
                $ RogueX.Uptop = 1
                "Rogue shrugs and pulls her top open."   
                call Rogue_First_Topless 
                      
    #Round = 0 loop breaks
    $ RogueX.FaceChange("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.Petname], that's enough of that for now."
    
    
label Rogue_SB_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Rogue_Pos_Reset
        
    $ RogueX.FaceChange("sexy") 
    
    $ RogueX.SuckB += 1  
    $ RogueX.Action -=1
    $ RogueX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ RogueX.Addictionrate += 1 
        
    call Partner_Like(RogueX,2)
     
    if RogueX.SuckB == 1:            
            $ RogueX.SEXP += 4         
            if not Situation: 
                if RogueX.Love >= 500 and "unsatisfied" not in RogueX.RecentActions:
                    ch_r "I . . . really liked that, [RogueX.Petname]."
                elif RogueX.Obed <= 500 and Player.Focus <= 20:
                    $ RogueX.FaceChange("perplexed", 1)
                    ch_r "Did you like the taste?"
     
    $ Tempmod = 0  
    call Checkout
    return   
    
# End Suck breasts    

# Fondle Thighs start //////////////////////////////////////////

label Rogue_Fondle_Thighs:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(RogueX)
                                                                                        # Will she let you fondle her thighs? Modifiers
    if RogueX.FondleT: #You've done it before
        $ Tempmod += 10
    if RogueX.PantsNum() >= 6 or RogueX.HoseNum() >= 5: # she's got pants on.
        $ Tempmod -= 5    
    if RogueX.Lust > 75: #She's really horny
        $ Tempmod += 10    
    if "exhibitionist" in RogueX.Traits:
        $ Tempmod += Taboo   
    if "dating" in RogueX.Traits or "sex friend" in RogueX.Petnames:
        $ Tempmod += 10
    elif "ex" in RogueX.Traits:
        $ Tempmod -= 25 
    if RogueX.ForcedCount and not RogueX.Forced:
        $ Tempmod -= 5 * RogueX.ForcedCount      
    
    if Taboo and "tabno" in RogueX.DailyActions:        
        $ Tempmod -= 10 
        
    if "no fondle thighs" in RogueX.DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle thighs" in RogueX.RecentActions else 0   
            
    $ Approval = ApprovalCheck(RogueX, 750, TabM=1) # 75, 90, 105, Taboo -40(105)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ RogueX.FaceChange("sexy")       
            $ RogueX.Statup("Obed", 50, 1)
            $ RogueX.Statup("Inbt", 30, 2)            
            "As you caress her thigh, Rogue glances at you, and smiles."             
            jump Rogue_FT_Prep      
        else:               
            $ RogueX.FaceChange("surprised")
            $ RogueX.Statup("Obed", 50, -2)
            ch_r "Hands off the merchandise, [RogueX.Petname]."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        $ RogueX.FaceChange("surprised")    
        $ RogueX.Brows = "sad"
        if RogueX.Lust > 60:
            $ RogueX.Statup("Love", 70, -3)
        $ RogueX.Statup("Obed", 90, 1)
        $ RogueX.Statup("Obed", 70, 2)
        "As you pull back, Rogue looks a little sad."              
        jump Rogue_FT_Prep  
    elif "fondle thighs" in RogueX.RecentActions:
        $ RogueX.FaceChange("sexy", 1)
        ch_r "Mmm, again? Ok."
        jump Rogue_FT_Prep
    elif "fondle thighs" in RogueX.DailyActions:
        $ RogueX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "You do have a smooth touch. . .",
            "Mmm. . ."]) 
        ch_r "[Line]"
    
    if Approval >= 2:                                                                   #She's into it. . .
        $ RogueX.FaceChange("bemused", 1)
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Love", 70, -3, 1)
            $ RogueX.Statup("Obed", 90, 1)
            $ RogueX.Statup("Inbt", 60, 1)
        ch_r "Ok [RogueX.Petname], go ahead."   
        $ RogueX.Statup("Love", 90, 1)
        $ RogueX.Statup("Inbt", 50, 3) 
        jump Rogue_FT_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        $ RogueX.FaceChange("angry", 1)
        if "no fondle thighs" in RogueX.RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions and "no fondle thighs" in RogueX.DailyActions:  
            ch_r "I told you not to touch me like that in public!" 
        elif "no fondle thighs" in RogueX.DailyActions:       
            ch_r "I already told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions:  
            ch_r "I told you not in public!"  
        elif not RogueX.FondleT:
            $ RogueX.FaceChange("bemused")
            ch_r "I just don't think I'm ready yet, [RogueX.Petname]. . ."
        else:
            $ RogueX.FaceChange("bemused")
            ch_r "I'd really rather not."  
        menu:
            extend ""
            "Sorry, never mind." if "no fondle thighs" in RogueX.DailyActions:
                $ RogueX.FaceChange("bemused")
                ch_r "Yeah, ok, [RogueX.Petname]."              
                return
            "Maybe later?" if "no fondle thighs" not in RogueX.DailyActions:
                $ RogueX.FaceChange("sexy")  
                ch_r "Heh, maybe, [RogueX.Petname]."
                $ RogueX.Statup("Love", 80, 1)
                $ RogueX.Statup("Inbt", 30, 2)    
                if Taboo:                    
                    $ RogueX.AddWord(1,"tabno","tabno")  
                $ RogueX.RecentActions.append("no fondle thighs")                      
                $ RogueX.DailyActions.append("no fondle thighs")            
                return
            "Come on, Please?":             
                if Approval:
                    $ RogueX.FaceChange("sexy")     
                    $ RogueX.Statup("Obed", 60, 1)
                    $ RogueX.Statup("Obed", 30, 2)
                    $ RogueX.Statup("Inbt", 50, 1)
                    $ RogueX.Statup("Inbt", 30, 2)
                    ch_r "Heh, I suppose I can hardly refuse ya when you use the magic words . . ."             
                    jump Rogue_FT_Prep
                else:   
                    $ RogueX.FaceChange("sexy") 
                    ch_r "I'm afraid not this time, sorry [RogueX.Petname]."     
            
            "[[Start caressing her thigh anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck(RogueX, 350, "OI", TabM = 2) # 35, 50, 65, -80(105)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.FaceChange("sad")
                    $ RogueX.Statup("Love", 70, -5, 1)
                    $ RogueX.Statup("Love", 20, -2, 1)                 
                    ch_r "Hmmph."                         
                    $ RogueX.Statup("Obed", 50, 3)
                    $ RogueX.Statup("Inbt", 60, 2)  
                    if Approval < 2:                          
                        $ RogueX.Forced = 1
                    jump Rogue_FT_Prep
                else:                              
                    $ RogueX.Statup("Love", 200, -8)  
                    $ RogueX.FaceChange("angry", 1)
                    "She slaps your hand away."   
                    $ RogueX.AddWord(1,"angry","angry")   
                    
    if "no fondle thighs" in RogueX.DailyActions:
        ch_r "Learn to take \"no\" for an answer, [RogueX.Petname]."  
        $ RogueX.AddWord(1,"angry","angry")  
    elif RogueX.Forced:
        $ RogueX.FaceChange("angry", 1)
        ch_r "Not even that much."
        $ RogueX.Statup("Lust", 50, 2)    
        $ RogueX.Statup("Obed", 50, -1)   
        $ RogueX.AddWord(1,"angry","angry")  
    elif Taboo:
        $ RogueX.FaceChange("angry", 1)    
        $ RogueX.AddWord(1,"tabno","tabno")  
        ch_r "I really don't think this is the right place for that!"                   
    elif RogueX.FondleT:
        $ RogueX.FaceChange("sad")
        ch_r "Fresh!"            
    else:
        $ RogueX.FaceChange("sexy") 
        $ RogueX.Mouth = "sad"
        ch_r "No luck, [RogueX.Petname]."
    $ RogueX.RecentActions.append("no fondle thighs")                      
    $ RogueX.DailyActions.append("no fondle thighs") 
    $ Tempmod = 0    
    return
    
label Rogue_FT_Prep:                                                                 #Animation set-up 
    if Trigger == "kiss you": 
        $ Trigger = "fondle thighs" 
        return
        
    if Trigger2 == "fondle thighs": 
        return
        
    if not RogueX.Forced and Situation != "auto":
        $ Tempmod = 0
        call Bottoms_Off(RogueX) 
        if "angry" in RogueX.RecentActions:
            return 
            
    $ Tempmod = 0    
    call Rogue_Pussy_Launch("fondle thighs")
    if not RogueX.FondleT:        
        if RogueX.Forced:
            $ RogueX.Statup("Love", 90, -10)
            $ RogueX.Statup("Obed", 70, 15)
            $ RogueX.Statup("Inbt", 80, 10) 
        else:
            $ RogueX.Statup("Love", 90, 5)
            $ RogueX.Statup("Obed", 70, 10)
            $ RogueX.Statup("Inbt", 80, 15) 
            
    if Taboo:               
        $ RogueX.Statup("Lust", 200, (int(Taboo/5)))                               
        $ RogueX.Statup("Inbt", 200, (2*(int(Taboo/5))))
     
    if Situation:   
        $ renpy.pop_call() 
        $ Situation = 0 
    $ Line = 0 
    $ Cnt = 0
    if Taboo:
        $ RogueX.DrainWord("tabno")
    $ RogueX.DrainWord("no fondle thighs")
    $ RogueX.AddWord(0,"fondle thighs","fondle thighs")
    
label Rogue_FT_Cycle: #Repeating strokes 
    while Round >=0:  
        call Shift_Focus(RogueX) 
        call Rogue_Pussy_Launch("fondle thighs")
        $ RogueX.LustFace()   
        
        if  Player.Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                         
                        "Slap her ass":                     
                                    call Slap_Ass(RogueX)  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Rogue_FT_Cycle  
                                    
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
                                            if RogueX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ RogueX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(RogueX,"tired")  # "I'm actually getting a little tired,"  
                                                
                                    "Shift primary action":
                                            if RogueX.Action and MultiAction:
                                                    menu:                                                             
                                                        "Can I do a little deeper?":
                                                                if RogueX.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Rogue_FT_After
                                                                    call Rogue_Fondle_Pussy                
                                                                else:
                                                                    call Sex_Basic_Dialog(RogueX,"tired")  # "I'm actually getting a little tired,"  
                                                        "Shift your hands a bit higher without asking":
                                                                if RogueX.Action and MultiAction:
                                                                    $ Situation = "auto"
                                                                    call Rogue_FT_After
                                                                    call Rogue_Fondle_Pussy    
                                                                else:
                                                                    "As your hands creep upwards, she grabs your wrists."
                                                                    call Sex_Basic_Dialog(RogueX,"tired")  # "I'm actually getting a little tired," 
                                                        "Never Mind":
                                                                jump Rogue_FT_Cycle
                                            else: 
                                                call Sex_Basic_Dialog(RogueX,"tired")  # "I'm actually getting a little tired,"           
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Rogue_FT_After
                                                call Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask [RogueX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(RogueX)
                                            "Ask [RogueX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(RogueX)  
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0    
                                                        
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(RogueX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Rogue_FT_Cycle 
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Rogue_FT_Cycle 
                                            "Never mind":
                                                        jump Rogue_FT_Cycle 
                                    "Undress [RogueX.Name]":
                                            call Girl_Undress(RogueX)   
                                    "Clean up [RogueX.Name] (locked)" if not RogueX.Spunk:
                                            pass  
                                    "Clean up [RogueX.Name]" if RogueX.Spunk:
                                            call Girl_Cleanup(RogueX,"ask")                                         
                                    "Never mind":
                                            jump Rogue_FT_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Rogue_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Rogue_FT_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Rogue_Pos_Reset
                                    $ Line = 0
                                    jump Rogue_FT_After
        #End menu (if Line)
        
        call Shift_Focus(RogueX)
        call Sex_Dialog(RogueX,Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or RogueX.Lust >= 100: 
                    #If either of you could cum   
                    if Player.Focus >= 100:    
                            #If you can cum:                                                 
                            call Player_Cumming(RogueX)
                            if "angry" in RogueX.RecentActions:  
                                call Rogue_Pos_Reset
                                return    
                            $ RogueX.Statup("Lust", 200, 5) 
                            if 100 > RogueX.Lust >= 70 and RogueX.OCount < 2 and RogueX.SEXP >= 20:             
                                $ RogueX.AddWord(0,"unsatisfied","unsatisfied")    
                            
                            if Player.Focus > 80:
                                jump Rogue_FT_After 
                            $ Line = "came"
     
                    if RogueX.Lust >= 100:  
                            #If Rogue can cum                                             
                            call Girl_Cumming(RogueX)
                            if Situation == "shift" or "angry" in RogueX.RecentActions:
                                jump Rogue_FT_After
                       
                    if Line == "came": #ex Player.Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in RogueX.RecentActions:#And Rogue is unsatisfied,  
                                "[RogueX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Rogue_FT_After   
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)            
        #End orgasm
        
        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0
        
        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif Cnt == (5 + RogueX.FondleT):
                    $ RogueX.Brows = "confused"
                    ch_r "You like how those feel, huh?"   
        elif Cnt == (15 + RogueX.FondleT) and RogueX.SEXP >= 15 and not ApprovalCheck(RogueX, 1500):
                    $ RogueX.Brows = "confused"        
                    menu:
                        ch_r "I know you're having fun, but maybe we could try something else [RogueX.Petname]."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Rogue_FT_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Rogue_FT_After
                        "No, this is fun.":   
                                if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):                        
                                    $ RogueX.Statup("Love", 200, -5)
                                    $ RogueX.Statup("Obed", 50, 3)                    
                                    $ RogueX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ RogueX.FaceChange("angry", 1)   
                                    call Rogue_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_r "Well if that's your attitude, I don't need your \"help\"."                         
                                    $ RogueX.Statup("Love", 50, -3, 1)
                                    $ RogueX.Statup("Love", 80, -4, 1)
                                    $ RogueX.Statup("Obed", 30, -1, 1)                    
                                    $ RogueX.Statup("Obed", 50, -1, 1)  
                                    $ RogueX.AddWord(1,"angry","angry")   
                                    jump Rogue_FT_After
        #End Count check
           
        call Escalation(RogueX) #sees if she wants to escalate things
        
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    $ RogueX.FaceChange("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.Petname], that's enough of that for now."
    
    
label Rogue_FT_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Rogue_Pos_Reset
        
    $ RogueX.FaceChange("sexy") 
    
    $ RogueX.FondleT += 1  
    $ RogueX.Action -=1
    if RogueX.PantsNum() < 6 or RogueX.Upskirt:        
        $ RogueX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ RogueX.Addictionrate += 1
            
        call Partner_Like(RogueX,1,0)
     
    if RogueX.FondleT == 1:            
            $ RogueX.SEXP += 3         
            if not Situation: 
                if RogueX.Love >= 500 and "unsatisfied" not in RogueX.RecentActions:
                    ch_r "That was. . . nice."
                elif RogueX.Obed <= 500 and Player.Focus <= 20:
                    $ RogueX.FaceChange("perplexed", 1)
                    ch_r "Was that enough for you?"
     
    $ Tempmod = 0  
    call Checkout
    return   
    
# ////////////////////////////////////////////////////////////////////////Start Fondle Pussy    
label Rogue_Fondle_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(RogueX)
                                                                                        # Will she let you fondle? Modifiers
    if RogueX.FondleP: #You've done it before
        $ Tempmod += 20
    if RogueX.PantsNum() >= 6 or RogueX.HoseNum() >= 5: # she's got pants on.
        $ Tempmod -= 10    
    if RogueX.Lust > 75: #She's really horny
        $ Tempmod += 15
    if RogueX.Lust > 75 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in RogueX.Traits:
        $ Tempmod += (2*Taboo)
    if "dating" in RogueX.Traits or "sex friend" in RogueX.Petnames:
        $ Tempmod += 10
    elif "ex" in RogueX.Traits:
        $ Tempmod -= 25  
    if RogueX.ForcedCount and not RogueX.Forced:
        $ Tempmod -= 5 * RogueX.ForcedCount     
    
    if Taboo and "tabno" in RogueX.DailyActions:        
        $ Tempmod -= 10 
        
    if "no fondle pussy" in RogueX.DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle pussy" in RogueX.RecentActions else 0   
            
    $ Approval = ApprovalCheck(RogueX, 1050, TabM = 2) # 105, 120, 135, Taboo -80(185)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ RogueX.FaceChange("sexy")       
            $ RogueX.Statup("Obed", 90, 1)
            $ RogueX.Statup("Obed", 70, 2)
            $ RogueX.Statup("Inbt", 70, 3)
            $ RogueX.Statup("Inbt", 30, 2)
            "As your hand creeps up her thigh, [RogueX.Name] seems a bit surprised, but then nods."            
            jump Rogue_FP_Prep      
        else:               
            $ RogueX.FaceChange("surprised")
            $ RogueX.Statup("Obed", 50, -2)
            ch_r "Hey, just keep doing what you were doing, [RogueX.Petname]."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        $ RogueX.FaceChange("surprised")   
        $ RogueX.Brows = "sad"        
        if RogueX.Lust > 80:
            $ RogueX.Statup("Love", 70, -4)
        $ RogueX.Statup("Obed", 90, 1)
        $ RogueX.Statup("Obed", 70, 2)
        "As your hand pulls out, [RogueX.Name] gasps and looks upset."              
        jump Rogue_FP_Prep     
    elif "fondle pussy" in RogueX.RecentActions:
        $ RogueX.FaceChange("sexy", 1)
        ch_r "Mmm, again? Ok."
        jump Rogue_FP_Prep
    elif "fondle pussy" in RogueX.DailyActions:
        $ RogueX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so hard this time though.",
            "Take it a bit gently, I'm still quivering from earlier.",
            "Mmm. . ."]) 
        ch_r "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .
        $ RogueX.FaceChange("bemused", 1)
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Love", 70, -3, 1)
            $ RogueX.Statup("Love", 20, -2, 1)
            $ RogueX.Statup("Obed", 90, 1)
            $ RogueX.Statup("Inbt", 60, 1)
        ch_r "Sure, get in there."   
        $ RogueX.Statup("Love", 90, 1)
        $ RogueX.Statup("Inbt", 50, 3) 
        jump Rogue_FP_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        $ RogueX.FaceChange("angry", 1)
        if "no fondle pussy" in RogueX.RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions and "no fondle pussy" in RogueX.DailyActions:  
            ch_r "I told you not to touch me like that in public!" 
        elif "no fondle pussy" in RogueX.DailyActions:       
            ch_r "I already told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions:  
            ch_r "I told you not in public!"  
        elif not RogueX.FondleP:
            $ RogueX.FaceChange("bemused")
            ch_r "Um, not down there, [RogueX.Petname]. . ."
        else:
            $ RogueX.FaceChange("bemused")
            ch_r "I'd really rather not."  
        menu:
            extend ""
            "Sorry, never mind." if "no fondle pussy" in RogueX.DailyActions:
                $ RogueX.FaceChange("bemused")
                ch_r "Yeah, ok, [RogueX.Petname]."              
                return
            "Maybe later?" if "no fondle pussy" not in RogueX.DailyActions:
                $ RogueX.FaceChange("sexy")  
                ch_r "I'll give it some thought, [RogueX.Petname]."
                $ RogueX.Statup("Love", 80, 2)
                $ RogueX.Statup("Inbt", 70, 2)   
                if Taboo:                    
                    $ RogueX.AddWord(1,"tabno","tabno")  
                $ RogueX.RecentActions.append("no fondle pussy")                      
                $ RogueX.DailyActions.append("no fondle pussy")            
                return
            "Come on, Please?":             
                if Approval:
                    $ RogueX.FaceChange("sexy")     
                    $ RogueX.Statup("Obed", 90, 2)
                    $ RogueX.Statup("Obed", 50, 2)
                    $ RogueX.Statup("Inbt", 70, 3) 
                    $ RogueX.Statup("Inbt", 40, 2) 
                    ch_r "Well, if you're gonna beg. . ."                    
                    jump Rogue_FP_Prep
                else:   
                    $ RogueX.FaceChange("sexy") 
                    ch_r "Tsk, not this time, [RogueX.Petname]." 
            
            "[[Start fondling anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck(RogueX, 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.FaceChange("sad")
                    $ RogueX.Statup("Love", 70, -5, 1)
                    $ RogueX.Statup("Love", 200, -2)                 
                    ch_r "Well, at least make it worth it."
                    $ RogueX.Statup("Obed", 50, 4)
                    $ RogueX.Statup("Inbt", 80, 1) 
                    $ RogueX.Statup("Inbt", 60, 3)  
                    if Approval < 2:                          
                        $ RogueX.Forced = 1
                    jump Rogue_FP_Prep
                else:                              
                    $ RogueX.Statup("Love", 200, -15)  
                    $ RogueX.FaceChange("angry", 1)
                    "She slaps your hand away."   
                    $ RogueX.AddWord(1,"angry","angry")   
                    
    if "no fondle pussy" in RogueX.DailyActions:
        ch_r "Learn to take \"no\" for an answer, [RogueX.Petname]."   
        $ RogueX.AddWord(1,"angry","angry")  
    elif RogueX.Forced:
        $ RogueX.FaceChange("angry", 1)
        ch_r "Stay out of my pants, [RogueX.Petname]."
        $ RogueX.Statup("Lust", 70, 5)    
        $ RogueX.Statup("Obed", 50, -2)    
        $ RogueX.AddWord(1,"angry","angry")  
    elif Taboo:
        $ RogueX.FaceChange("angry", 1)    
        $ RogueX.AddWord(1,"tabno","tabno")  
        ch_r "I really don't think this is the right place for that!"                   
    elif RogueX.FondleP:
        $ RogueX.FaceChange("sad")
        ch_r "Sorry, keep your hands out of there."           
    else:
        $ RogueX.FaceChange("sexy") 
        $ RogueX.Mouth = "sad"
        ch_r "No luck [RogueX.Petname]."
    $ RogueX.RecentActions.append("no fondle pussy")                      
    $ RogueX.DailyActions.append("no fondle pussy") 
    $ Tempmod = 0    
    return
    
ch_r "Sorry, I don't even know how I got here. . ."
return
                
label Rogue_FP_Prep: #Animation set-up 
    if Trigger2 == "fondle pussy":
        return
            
    call Rogue_Pussy_Launch("fondle pussy")
    
    if Situation == RogueX:                                                        
            #Rogue auto-starts    
            $ Situation = 0
            if (RogueX.Legs and not RogueX.Upskirt) or (RogueX.Panties and not RogueX.PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck(RogueX, 1250, TabM = 1) or (RogueX.SeenPussy and ApprovalCheck(RogueX, 500) and not Taboo):
                        $ RogueX.Upskirt = 1
                        $ RogueX.PantiesDown = 1
                        $ Line = 0
                        if RogueX.PantsNum() == 5:
                            $ Line = RogueX.Name+" hikes up her skirt"
                        elif RogueX.PantsNum() > 6:
                            $ Line = RogueX.Name+" pulls down her " + RogueX.Legs
                        else:
                            $ Line = 0                            
                        if RogueX.Panties:
                            if Line:
                                #wearing pants
                                "[Line] and pulls her [RogueX.Panties] out of the way."
                                "She then grabs your arm and shoves your hand into her crotch, clearly intending you to get to work."
                            else:
                                #no pants
                                "She pulls her [RogueX.Panties] out of the way, and then shoves your hand into her crotch."
                                "She clearly intends for you to get to work." 
                        else:
                            #pants but no panties
                            "[Line], and then shoves your hand into her crotch."
                            "She clearly intends for you to get to work."                     
                        call Rogue_First_Bottomless(1)
                else:
                        "[RogueX.Name] grabs your arm and shoves your hand into her crotch, clearly intending you to get to work."
            else:
                        "[RogueX.Name] grabs your arm and shoves your hand into her crotch, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":                    
                    $ RogueX.Statup("Inbt", 80, 3) 
                    $ RogueX.Statup("Inbt", 50, 2)
                    "You start to run your fingers along her pussy."
                "Praise her.":       
                    $ RogueX.FaceChange("sexy", 1)                    
                    $ RogueX.Statup("Inbt", 80, 3) 
                    ch_p "I like the initiative, [RogueX.Pet]."
                    $ RogueX.NameCheck() #checks reaction to petname
                    "You start to run your fingers along her pussy."
                    $ RogueX.Statup("Love", 85, 1)
                    $ RogueX.Statup("Obed", 90, 1)
                    $ RogueX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your hand back."
                    $ RogueX.FaceChange("surprised")       
                    $ RogueX.Statup("Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [RogueX.Pet]."
                    $ RogueX.NameCheck() #checks reaction to petname
                    "[RogueX.Name] pulls back."
                    $ RogueX.Statup("Obed", 90, 1)
                    $ RogueX.Statup("Obed", 50, 1)
                    $ RogueX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")      
                    $ RogueX.AddWord(1,"refused","refused")  
                    return          
            #end auto
            
    if not RogueX.Forced and Situation != "auto":
        $ Tempmod = 0
        call Bottoms_Off(RogueX)   
        if "angry" in RogueX.RecentActions:
            return 
    $ Tempmod = 0
    if not RogueX.FondleP:        
        if RogueX.Forced:
            $ RogueX.Statup("Love", 90, -50)
            $ RogueX.Statup("Obed", 70, 35)
            $ RogueX.Statup("Inbt", 80, 25) 
        else:
            $ RogueX.Statup("Love", 90, 10)
            $ RogueX.Statup("Obed", 70, 10)
            $ RogueX.Statup("Inbt", 80, 15) 
    if Taboo:
        $ RogueX.Inbt += int(Taboo/10)  
        $ RogueX.Lust += int(Taboo/5)
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0   
    $ Line = 0   
    $ Cnt = 0 
    if Taboo:
        $ RogueX.DrainWord("tabno")
    $ RogueX.DrainWord("no fondle pussy")
    $ RogueX.AddWord(0,"fondle pussy","fondle pussy")
    
    $ Speed = 1
    
label Rogue_FP_Cycle: #Repeating strokes 
    while Round >=0:  
        call Shift_Focus(RogueX) 
        call Rogue_Pussy_Launch("fondle pussy")
        $ RogueX.LustFace()    
        
        if  Player.Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                          
                        "I want to stick a finger in. . ." if Speed != 2:
                                if RogueX.InsertP: 
                                    $ Speed = 2
                                else:
                                    menu:                                
                                        "Ask her first":
                                            $ Situation = "shift"
                                        "Don't ask first [[just stick it in]":                                    
                                            $ Situation = "auto"
                                    call Rogue_Insert_Pussy 
                        
                        "Pull back a bit. . ." if Speed == 2:
                                    $ Speed = 0
                                    
                        "Slap her ass":                     
                                    call Slap_Ass(RogueX)  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Rogue_FP_Cycle  
                                    
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
                                            if RogueX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ RogueX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(RogueX,"tired")  # "I'm actually getting a little tired,"  
                                                
                                    "Shift primary action":
                                            if RogueX.Action and MultiAction:
                                                    menu:                                                             
                                                        "I want to lick your pussy.":
                                                                $ Situation = "shift"
                                                                call Rogue_FP_After
                                                                call Rogue_Lick_Pussy                 
                                                        "Just start licking":
                                                                $ Situation = "auto"
                                                                call Rogue_FP_After
                                                                call Rogue_Lick_Pussy         
                                                        "Pull back to the thighs":
                                                                $ Situation = "pullback"
                                                                call Rogue_FP_After
                                                                call Rogue_Fondle_Thighs
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Rogue_FP_After
                                                                call Rogue_Dildo_Pussy  
                                                        "Never Mind":
                                                                jump Rogue_FP_Cycle
                                            else: 
                                                call Sex_Basic_Dialog(RogueX,"tired")  # "I'm actually getting a little tired,"           
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Rogue_FP_After
                                                call Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask [RogueX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(RogueX)
                                            "Ask [RogueX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(RogueX)  
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0    
                                                        
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(RogueX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Rogue_FP_Cycle 
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Rogue_FP_Cycle 
                                            "Never mind":
                                                        jump Rogue_FP_Cycle 
                                    "Undress [RogueX.Name]":
                                            call Girl_Undress(RogueX)   
                                    "Clean up [RogueX.Name] (locked)" if not RogueX.Spunk:
                                            pass  
                                    "Clean up [RogueX.Name]" if RogueX.Spunk:
                                            call Girl_Cleanup(RogueX,"ask")                                         
                                    "Never mind":
                                            jump Rogue_FP_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Rogue_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Rogue_FP_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Rogue_Pos_Reset
                                    $ Line = 0
                                    jump Rogue_FP_After
        #End menu (if Line)
        
        call Shift_Focus(RogueX)
        call Sex_Dialog(RogueX,Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or RogueX.Lust >= 100: 
                    #If either of you could cum   
                    if Player.Focus >= 100:    
                            #If you can cum:                                                 
                            call Player_Cumming(RogueX)
                            if "angry" in RogueX.RecentActions:  
                                call Rogue_Pos_Reset
                                return    
                            $ RogueX.Statup("Lust", 200, 5) 
                            if 100 > RogueX.Lust >= 70 and RogueX.OCount < 2:               
                                $ RogueX.AddWord(0,"unsatisfied","unsatisfied")
                            
                            if Player.Focus > 80:
                                jump Rogue_FP_After 
                            $ Line = "came"
     
                    if RogueX.Lust >= 100:  
                            #If Rogue can cum  
                            call Girl_Cumming(RogueX)
                            if Situation == "shift" or "angry" in RogueX.RecentActions:
                                jump Rogue_FP_After
                       
                    if Line == "came": #ex Player.Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in RogueX.RecentActions:#And Rogue is unsatisfied,  
                                "[RogueX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Rogue_FP_After    
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm                
                call Girl_Cumming(Partner)            
        #End orgasm
        
        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0
        
        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif Cnt == (5 + RogueX.FondleP):
                    $ RogueX.Brows = "confused"
                    ch_r "You like how that feels, huh?"  
        elif RogueX.Lust >= 80:
                    pass
        elif Cnt == (15 + RogueX.FondleP) and RogueX.SEXP >= 15 and not ApprovalCheck(RogueX, 1500):
                    $ RogueX.Brows = "confused"        
                    menu:
                        ch_r "I know you're having fun, but maybe we could try something else [RogueX.Petname]."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Rogue_FP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Rogue_FP_After
                        "No, this is fun.":   
                                if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):                        
                                    $ RogueX.Statup("Love", 200, -5)
                                    $ RogueX.Statup("Obed", 50, 3)                    
                                    $ RogueX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ RogueX.FaceChange("angry", 1)   
                                    call Rogue_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_r "Well if that's your attitude, I don't need your \"help\"."                         
                                    $ RogueX.Statup("Love", 50, -3, 1)
                                    $ RogueX.Statup("Love", 80, -4, 1)
                                    $ RogueX.Statup("Obed", 30, -1, 1)                    
                                    $ RogueX.Statup("Obed", 50, -1, 1)  
                                    $ RogueX.AddWord(1,"angry","angry")    
                                    jump Rogue_FP_After
        #End Count check
           
        call Escalation(RogueX) #sees if she wants to escalate things
        
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    $ RogueX.FaceChange("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.Petname], that's enough of that for now."
    
    
label Rogue_FP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Rogue_Pos_Reset
        
    $ RogueX.FaceChange("sexy") 
    
    $ RogueX.FondleP += 1  
    $ RogueX.Action -=1
    if RogueX.PantsNum() < 6 or RogueX.Upskirt:        
        $ RogueX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ RogueX.Addictionrate += 1
            
    call Partner_Like(RogueX,2)
            
    if RogueX.FondleP == 1:            
            $ RogueX.SEXP += 7         
            if not Situation: 
                if RogueX.Love >= 500 and "unsatisfied" not in RogueX.RecentActions:
                    ch_r "Certainly different with someone else at the wheel."
                elif RogueX.Obed <= 500 and Player.Focus <= 20:
                    $ RogueX.FaceChange("perplexed", 1)
                    ch_r "Was that enough for you?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_r "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# end RogueX.Fondle Pussy /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label Rogue_Insert_Pussy:
    call Shift_Focus(RogueX)
    if Situation == "auto":                                                                  #You auto-start                    
        if ApprovalCheck(RogueX, 1100, TabM = 2):
                $ RogueX.FaceChange("surprised")       
                $ RogueX.Statup("Obed", 90, 1)
                $ RogueX.Statup("Obed", 70, 2)
                $ RogueX.Statup("Inbt", 70, 3) 
                $ RogueX.Statup("Inbt", 30, 2) 
                "As you slide a finger in, [RogueX.Name] seems a bit surprised, but seems into it."              
                jump Rogue_IP_Prep
        else:   
                $ RogueX.FaceChange("surprised")
                $ RogueX.Statup("Love", 80, -2)
                $ RogueX.Statup("Obed", 50, -3)
                ch_r "Keep it outside, [RogueX.Petname]."   
                return            
    
    if ApprovalCheck(RogueX, 1100, TabM = 2):                                                                   #She's into it. . .               
        if RogueX.Forced:
                $ RogueX.FaceChange("sad")
                $ RogueX.Statup("Love", 70, -3, 1)
                $ RogueX.Statup("Love", 20, -2, 1)
                $ RogueX.Statup("Obed", 90, 1)
                $ RogueX.Statup("Inbt", 60, 1)
                ch_r "Sure, get in there."    
        else:
                $ RogueX.FaceChange("sexy", 1)
                $ RogueX.Statup("Love", 90, 1)
                $ RogueX.Statup("Inbt", 50, 3) 
                ch_r "God yes."                
        $ RogueX.Statup("Obed", 20, 1)
        $ RogueX.Statup("Obed", 60, 1)
        $ RogueX.Statup("Inbt", 70, 2) 
        jump Rogue_IP_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .  
        $ RogueX.FaceChange("bemused", 2)
        ch_r "Um, no thanks, [RogueX.Petname]."
        $ RogueX.Blush = 1
    return
    
                   
label Rogue_IP_Prep: #Animation set-up    
    if not RogueX.InsertP:
        $ RogueX.InsertP = 1
        $ RogueX.SEXP += 10          
        if RogueX.Forced:
                $ RogueX.Statup("Love", 90, -60)
                $ RogueX.Statup("Obed", 70, 55)
                $ RogueX.Statup("Inbt", 80, 35) 
        else:
                $ RogueX.Statup("Love", 90, 10)
                $ RogueX.Statup("Obed", 70, 20)
                $ RogueX.Statup("Inbt", 80, 25)
        
    if not RogueX.Forced and Situation != "auto":        
            call Girl_Undress(RogueX,"bottom")
            if "angry" in RogueX.RecentActions:
                return    
            
    if Taboo:
            $ RogueX.Inbt += int(Taboo/10)  
            $ RogueX.Lust += int(Taboo/5)
        
    $ Line = 0   
    $ Speed = 2
    return

# end RogueX.Insert Pussy /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label Rogue_Lick_Pussy: 
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(RogueX)
                                                                                  # Will she let you fondle? Modifiers     
    if RogueX.LickP: #You've done it before
        $ Tempmod += 15
    if RogueX.PantsNum() >= 6 or RogueX.HoseNum() >= 5: # she's got pants on.
        $ Tempmod -= 15  
    if RogueX.Lust > 95:
        $ Tempmod += 20  
    elif RogueX.Lust > 85: #She's really horny
        $ Tempmod += 15
    if Situation == "shift":
        $ Tempmod += 10
    if RogueX.Lust > 85 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in RogueX.Traits:
        $ Tempmod += (4*Taboo) 
    if "dating" in RogueX.Traits or "sex friend" in RogueX.Petnames:
        $ Tempmod += 10
    elif "ex" in RogueX.Traits:
        $ Tempmod -= 25  
    if RogueX.ForcedCount and not RogueX.Forced:
        $ Tempmod -= 5 * RogueX.ForcedCount     
    
    if Taboo and "tabno" in RogueX.DailyActions:        
        $ Tempmod -= 10 
        
    if "no lick pussy" in RogueX.DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no lick pussy" in RogueX.RecentActions else 0   
            
    $ Approval = ApprovalCheck(RogueX, 1250, TabM = 4) # 125, 140, 155, Taboo -160(285)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            $ RogueX.FaceChange("surprised")
            $ RogueX.Statup("Obed", 90, 1)
            $ RogueX.Statup("Obed", 70, 2)
            $ RogueX.Statup("Inbt", 70, 3) 
            $ RogueX.Statup("Inbt", 30, 2) 
            "As you crouch down and start to lick her pussy, [RogueX.Name] startles, but then sinks into the sensation."  
            $ RogueX.FaceChange("sexy")           
            jump Rogue_LP_Prep
        else:   
            $ RogueX.FaceChange("surprised")
            $ RogueX.Statup("Love", 80, -2)
            $ RogueX.Statup("Obed", 50, -3)
            ch_r "Oh! No, no thank you, [RogueX.Petname]."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return            
    
    if "lick pussy" in RogueX.RecentActions:
        $ RogueX.FaceChange("sexy", 1)
        ch_r "Mmm, again? Ok."
        jump Rogue_LP_Prep
    elif "lick pussy" in RogueX.DailyActions:
        $ RogueX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Again? Oh, you're insatiable!",
            "Must be my lucky day!",
            "You sure know how to keep a girl satisfied. . .",
            "Mmm. . ."]) 
        ch_r "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .               
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Love", 70, -3, 1)
            $ RogueX.Statup("Love", 20, -2, 1)
            $ RogueX.Statup("Obed", 90, 1)
            $ RogueX.Statup("Inbt", 60, 1)
            ch_r "Sure, get in there."    
        else:
            $ RogueX.FaceChange("sexy", 1)
            $ RogueX.Eyes = "closed"            
            $ RogueX.Statup("Love", 90, 1)
            $ RogueX.Statup("Inbt", 50, 3)            
            $ RogueX.Statup("Lust", 200, 3)
            ch_r "Oooooooh. . ."                
        $ RogueX.Statup("Obed", 20, 1)
        $ RogueX.Statup("Obed", 60, 1)
        $ RogueX.Statup("Inbt", 70, 2) 
        jump Rogue_LP_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        $ RogueX.FaceChange("angry", 1)
        if "no lick pussy" in RogueX.RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions and "no lick pussy" in RogueX.DailyActions:  
            ch_r "You already got your answer!" 
        elif "no lick pussy" in RogueX.DailyActions:       
            ch_r "I already told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions:  
            ch_r "I told you not in public!"  
        elif not RogueX.LickP:
            $ RogueX.FaceChange("bemused")
            ch_r "That's pretty intimate, [RogueX.Petname]. . ."
        else:
            $ RogueX.FaceChange("bemused")
            ch_r "Oh, um, no, I'm not really comfortable with that. . ." 
        menu:
            extend ""
            "Sorry, never mind." if "no lick pussy" in RogueX.DailyActions:
                $ RogueX.FaceChange("bemused")
                ch_r "Yeah, ok, [RogueX.Petname]."              
                return            
            "I'm sure I can convince you later. . ." if "no lick pussy" not in RogueX.DailyActions:
                $ RogueX.FaceChange("sexy")  
                ch_r "I'll be thinking about it, [RogueX.Petname]."
                $ RogueX.Statup("Love", 80, 2)
                $ RogueX.Statup("Inbt", 70, 2)   
                if Taboo:                    
                    $ RogueX.AddWord(1,"tabno","tabno")  
                $ RogueX.RecentActions.append("no lick pussy")                      
                $ RogueX.DailyActions.append("no lick pussy")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    $ RogueX.FaceChange("sexy")           
                    $ RogueX.Statup("Obed", 90, 2)
                    $ RogueX.Statup("Obed", 50, 2)
                    ch_r "Ok, you're probably right. . ."      
                    $ RogueX.Statup("Inbt", 70, 3) 
                    $ RogueX.Statup("Inbt", 40, 2)
                    jump Rogue_LP_Prep
                else:   
                    $ RogueX.FaceChange("sexy") 
                    ch_r "Tsk, not this time, [RogueX.Petname], that just seems. . . intimate."     
            
            "[[Get in there anyway]":                                               # Pressured into being licked. 
                $ Approval = ApprovalCheck(RogueX, 750, "OI", TabM = 4) # 75, 90, 105, -160(235)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.FaceChange("sad")
                    $ RogueX.Statup("Love", 70, -5, 1)
                    $ RogueX.Statup("Love", 200, -2)                 
                    ch_r "Ok, get in there if you're so determined."  
                    $ RogueX.Statup("Obed", 50, 4)
                    $ RogueX.Statup("Inbt", 80, 1) 
                    $ RogueX.Statup("Inbt", 60, 3)  
                    if Approval < 2:                          
                        $ RogueX.Forced = 1
                    jump Rogue_LP_Prep
                else:                              
                    $ RogueX.Statup("Love", 200, -15)  
                    $ RogueX.FaceChange("angry", 1)
                    "She shoves your head back."   
                    $ RogueX.AddWord(1,"angry","angry")   
                    
    if "no lick pussy" in RogueX.DailyActions:
        ch_r "Learn to take \"no\" for an answer, [RogueX.Petname]."  
        $ RogueX.AddWord(1,"angry","angry")  
    elif RogueX.Forced:
        $ RogueX.FaceChange("angry", 1)
        ch_r "Not even, [RogueX.Petname]."
        $ RogueX.Statup("Lust", 80, 5)    
        $ RogueX.Statup("Obed", 50, -2)     
        $ RogueX.AddWord(1,"angry","angry")   
    elif Taboo:
        $ RogueX.FaceChange("angry", 1)    
        $ RogueX.AddWord(1,"tabno","tabno")  
        ch_r "This just really isn't the time or place, [RogueX.Petname]!"                   
    elif RogueX.LickP:
        $ RogueX.FaceChange("sad") 
        ch_r "Sorry, keep your tongue in your mouth."    
    else:
        $ RogueX.FaceChange("surprised")
        ch_r "Ew!"
        $ RogueX.FaceChange()
    $ RogueX.RecentActions.append("no lick pussy")                      
    $ RogueX.DailyActions.append("no lick pussy") 
    $ Tempmod = 0    
    return
    
label Rogue_LP_Prep: #Animation set-up  
    if Trigger2 == "lick pussy": #fix pull down pants now an option, make it work
        return
             
    call Rogue_Pussy_Launch("lick pussy")
    
    
    if Situation == RogueX:                                                       
            #Rogue auto-starts    
            $ Situation = 0
            if (RogueX.Legs and not RogueX.Upskirt) or (RogueX.Panties and not RogueX.PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck(RogueX, 1250, TabM = 1) or (RogueX.SeenPussy and ApprovalCheck(RogueX, 500) and not Taboo):
                        $ RogueX.Upskirt = 1
                        $ RogueX.PantiesDown = 1
                        $ Line = 0
                        if RogueX.PantsNum() == 5:
                            $ Line = RogueX.Name+" hikes up her skirt"
                        elif RogueX.PantsNum() > 6:
                            $ Line = RogueX.Name+" pulls down her " + RogueX.Legs
                        else:
                            $ Line = 0                            
                        if RogueX.Panties:
                            if Line:
                                #wearing pants
                                "[Line] and pulls her [RogueX.Panties] out of the way."
                                "She then grabs your head and pulls it to her crotch, clearly intending you to get to work."
                            else:
                                #no pants
                                "She pulls her [RogueX.Panties] out of the way, and then shoves your face into her crotch."
                                "She clearly intends for you to get to work." 
                        else:
                                #pants but no panties
                                "[Line], and then shoves your face into her crotch."
                                "She clearly intends for you to get to work."                     
                        call Rogue_First_Bottomless(1)
                else:
                        "[RogueX.Name] grabs your head and pulls it to her crotch, clearly intending you to get to work."
            else:
                        "[RogueX.Name] grabs your head and pulls it to her crotch, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":                    
                    $ RogueX.Statup("Inbt", 80, 3) 
                    $ RogueX.Statup("Inbt", 50, 2)
                    "You start licking."
                "Praise her.":       
                    $ RogueX.FaceChange("sexy", 1)                    
                    $ RogueX.Statup("Inbt", 80, 3) 
                    ch_p "Mmm, I like this idea, [RogueX.Pet]."
                    $ RogueX.NameCheck() #checks reaction to petname
                    "You start licking."
                    $ RogueX.Statup("Love", 85, 1)
                    $ RogueX.Statup("Obed", 90, 1)
                    $ RogueX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your head away."
                    $ RogueX.FaceChange("surprised")       
                    $ RogueX.Statup("Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [RogueX.Pet]."
                    $ RogueX.NameCheck() #checks reaction to petname
                    "[RogueX.Name] pulls back."
                    $ RogueX.Statup("Obed", 90, 1)
                    $ RogueX.Statup("Obed", 50, 1)
                    $ RogueX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")      
                    $ RogueX.AddWord(1,"refused","refused")  
                    return          
            #end auto
            
    if not RogueX.Forced and Situation != "auto":
        $ Tempmod = 0
        if RogueX.PantsNum() >= 6:
            $ Tempmod = 15
        call Bottoms_Off(RogueX)
        if "angry" in RogueX.RecentActions:
            return  
            
    $ Tempmod = 0 
    if not RogueX.LickP:        
        if RogueX.Forced:
            $ RogueX.Statup("Love", 90, -30)
            $ RogueX.Statup("Obed", 70, 35)
            $ RogueX.Statup("Inbt", 80, 75) 
        else:
            $ RogueX.Statup("Love", 90, 35)
            $ RogueX.Statup("Obed", 70, 15)
            $ RogueX.Statup("Inbt", 80, 35)
    if Taboo:
        $ RogueX.Inbt += int(Taboo/10)  
        $ RogueX.Lust += int(Taboo/5)
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
        
    if RogueX.PantsNum() == 5:
        $ RogueX.Upskirt = 1  
        $ RogueX.SeenPanties = 1
    call Rogue_First_Bottomless(1)
    
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ RogueX.DrainWord("tabno")
    $ RogueX.DrainWord("no lick pussy")
    $ RogueX.AddWord(0,"lick pussy","lick pussy")
    
label Rogue_LP_Cycle: #Repeating strokes
    if Trigger2 == "kiss you":
            $ Trigger2 = 0   
    while Round >=0:  
        call Shift_Focus(RogueX) 
        call Rogue_Pussy_Launch("lick pussy")
        $ RogueX.LustFace()   
        
        if  Player.Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                                              
                        "Slap her ass":                     
                                    call Slap_Ass(RogueX)  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Rogue_LP_Cycle  
                                    
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
                                            if RogueX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ RogueX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(RogueX,"tired")  # "I'm actually getting a little tired,"  
                                                
                                    "Shift primary action":
                                            if RogueX.Action and MultiAction:
                                                    menu:                                                             
                                                        "Pull out and start rubbing again.":
                                                                if RogueX.Action and MultiAction:
                                                                    $ Situation = "pullback"
                                                                    call Rogue_LP_After
                                                                    call Rogue_Fondle_Pussy
                                                                else:
                                                                    call Sex_Basic_Dialog(RogueX,"tired")  # "I'm actually getting a little tired,"  
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Rogue_LP_After
                                                                call Rogue_Dildo_Pussy  
                                                        "Never Mind":
                                                                jump Rogue_LP_Cycle
                                            else: 
                                                call Sex_Basic_Dialog(RogueX,"tired")  # "I'm actually getting a little tired,"           
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Rogue_LP_After
                                                call Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask [RogueX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(RogueX)
                                            "Ask [RogueX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(RogueX)  
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0    
                                                        
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(RogueX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Rogue_LP_Cycle 
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk: # (locked)" if not Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Rogue_LP_Cycle 
                                            "Never mind":
                                                        jump Rogue_LP_Cycle 
                                    "Undress [RogueX.Name]":
                                            call Girl_Undress(RogueX)   
                                    "Clean up [RogueX.Name] (locked)" if not RogueX.Spunk:
                                            pass  
                                    "Clean up [RogueX.Name]" if RogueX.Spunk:
                                            call Girl_Cleanup(RogueX,"ask")                                         
                                    "Never mind":
                                            jump Rogue_LP_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Rogue_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Rogue_LP_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Rogue_Pos_Reset
                                    $ Line = 0
                                    jump Rogue_LP_After
        #End menu (if Line)
        
        if RogueX.Panties or RogueX.PantsNum() >= 6 or RogueX.HoseNum() >= 5: #This checks if Rogue wants to strip down.
                call Girl_Undress(RogueX,"auto")
                
        call Shift_Focus(RogueX)
        call Sex_Dialog(RogueX,Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or RogueX.Lust >= 100: 
                    #If either of you could cum   
                    if Player.Focus >= 100:    
                            #If you can cum:                                                 
                            call Player_Cumming(RogueX)
                            if "angry" in RogueX.RecentActions:  
                                call Rogue_Pos_Reset
                                return    
                            $ RogueX.Statup("Lust", 200, 5) 
                            if 100 > RogueX.Lust >= 70 and RogueX.OCount < 2:                  
                                $ RogueX.AddWord(0,"unsatisfied","unsatisfied")
                            
                            if Player.Focus > 80:
                                jump Rogue_LP_After 
                            $ Line = "came"
     
                    if RogueX.Lust >= 100:  
                            #If Rogue can cum                                             
                            call Girl_Cumming(RogueX)
                            if Situation == "shift" or "angry" in RogueX.RecentActions:
                                jump Rogue_LP_After
                       
                    if Line == "came": #ex Player.Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in RogueX.RecentActions:#And Rogue is unsatisfied,  
                                "[RogueX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Rogue_LP_After   
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)            
        #End orgasm
        
        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0
        
        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif Cnt == (5 + RogueX.LickP):
                    $ RogueX.Brows = "confused"
                    ch_r "You like it down there?"  
        elif RogueX.Lust >= 80:
                    pass
        elif Cnt == (15 + RogueX.LickP) and RogueX.SEXP >= 15 and not ApprovalCheck(RogueX, 1500):
                    $ RogueX.Brows = "confused"        
                    menu:
                        ch_r "[RogueX.Petname], I know you're having fun down there, but maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Rogue_LP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Rogue_LP_After
                        "No, this is fun.":   
                                if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):                        
                                    $ RogueX.Statup("Love", 200, -5)
                                    $ RogueX.Statup("Obed", 50, 3)                    
                                    $ RogueX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ RogueX.FaceChange("angry", 1)   
                                    call Rogue_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_r "Well if that's your attitude, I don't need your \"help\"."                         
                                    $ RogueX.Statup("Love", 50, -3, 1)
                                    $ RogueX.Statup("Love", 80, -4, 1)
                                    $ RogueX.Statup("Obed", 30, -1, 1)                    
                                    $ RogueX.Statup("Obed", 50, -1, 1)  
                                    $ RogueX.AddWord(1,"angry","angry")     
                                    jump Rogue_LP_After
        #End Count check
           
        call Escalation(RogueX) #sees if she wants to escalate things
        
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    $ RogueX.FaceChange("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.Petname], that's enough of that for now."
    
    
label Rogue_LP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Rogue_Pos_Reset
        
    $ RogueX.FaceChange("sexy") 
    
    $ RogueX.LickP += 1  
    $ RogueX.Action -=1     
    if RogueX.PantsNum() < 6 or RogueX.Upskirt:        
        $ RogueX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ RogueX.Addictionrate += 1
    
    if Partner == EmmaX:
        call Partner_Like(RogueX,4,3)
    else:
        call Partner_Like(RogueX,3,3)
     
    if RogueX.LickP == 1:            
            $ RogueX.SEXP += 10         
            if not Situation: 
                if RogueX.Love >= 500 and "unsatisfied" not in RogueX.RecentActions:
                    ch_r "I. . . how'd I taste?"
                elif RogueX.Obed <= 500 and Player.Focus <= 20:
                    $ RogueX.FaceChange("perplexed", 1)
                    ch_r "Did you like that?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_r "Mmm, so what else did you have in mind?"
    call Checkout
    return   


# end RogueX.Lick Pussy /////////////////////////////////////////////////////////////////////////////

    
# ////////////////////////////////////////////////////////////////////////Start Fondle Ass    
label Rogue_Fondle_Ass: 
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(RogueX)
                                                                                     # Will she let you fondle? Modifiers
    if RogueX.FondleA: #You've done it before
        $ Tempmod += 10
    if RogueX.PantsNum() >= 6 or RogueX.HoseNum() >= 5: # she's got pants on.
        $ Tempmod -= 5     
    if RogueX.Lust > 75: #She's really horny
        $ Tempmod += 15
    if "exhibitionist" in RogueX.Traits:
        $ Tempmod += Taboo  
    if "dating" in RogueX.Traits or "sex friend" in RogueX.Petnames:
        $ Tempmod += 10
    elif "ex" in RogueX.Traits:
        $ Tempmod -= 25 
    if RogueX.ForcedCount and not RogueX.Forced:
        $ Tempmod -= 5 * RogueX.ForcedCount      
    
    if Taboo and "tabno" in RogueX.DailyActions:        
        $ Tempmod -= 10 
        
    if "no fondle ass" in RogueX.DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle ass" in RogueX.RecentActions else 0   
        
    $ Approval = ApprovalCheck(RogueX, 850, TabM=1) # 85, 100, 115, Taboo -40(125)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:  
            $ RogueX.FaceChange("surprised", 1)  
            $ RogueX.Statup("Obed", 70, 2)
            $ RogueX.Statup("Inbt", 40, 2) 
            "As your hand creeps down her backside, [RogueX.Name] seems a bit surprised, but then nods."              
            $ RogueX.FaceChange("sexy")  
            jump Rogue_FA_Prep  
        else:          
            $ RogueX.FaceChange("surprised")
            $ RogueX.Statup("Obed", 50, -3)
            ch_r "Hands off, [RogueX.Petname]."   
            $ RogueX.FaceChange("bemused")
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        $ RogueX.FaceChange("surprised")   
        $ RogueX.Brows = "sad"        
        if RogueX.Lust > 80:
            $ RogueX.Statup("Love", 70, -4)
        $ RogueX.Statup("Obed", 90, 1)
        $ RogueX.Statup("Obed", 70, 2)
        "As your hand slides out, [RogueX.Name] gasps and looks upset."              
        jump Rogue_FA_Prep     
    elif "fondle ass" in RogueX.RecentActions:
        $ RogueX.FaceChange("sexy", 1)
        ch_r "Mmm, again? Ok."
        jump Rogue_FA_Prep
    elif "fondle ass" in RogueX.DailyActions:
        $ RogueX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so rough this time though.",
            "Mmm. . ."]) 
        ch_r "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .        
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Love", 70, -2, 1)
            $ RogueX.Statup("Obed", 90, 2)
            $ RogueX.Statup("Inbt", 60, 2)
            ch_r "Fine, grab a cheek."   
        else:
            $ RogueX.FaceChange("bemused, 1") 
            ch_r "Sure, grab a cheek."   
        $ RogueX.Statup("Lust", 200, 3)
        $ RogueX.Statup("Obed", 60, 1)
        $ RogueX.Statup("Inbt", 70, 1) 
        jump Rogue_FA_Prep
        
    else:                                                                               #She's not into it, but maybe. . .            
        $ RogueX.FaceChange("angry", 1)
        if "no fondle ass" in RogueX.RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions and "no fondle ass" in RogueX.DailyActions:  
            ch_r "I told you not to touch me like that in public!" 
        elif "no fondle ass" in RogueX.DailyActions:       
            ch_r "I already told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions:  
            ch_r "I told you not in public!"  
        elif not RogueX.FondleA:
            $ RogueX.FaceChange("bemused")
            ch_r "Not yet, [RogueX.Petname]. . ."
        else:
            $ RogueX.FaceChange("bemused")
            ch_r "Let's not, ok [RogueX.Petname]?"
        menu:
            extend ""
            "Sorry, never mind." if "no fondle ass" in RogueX.DailyActions:
                $ RogueX.FaceChange("bemused")
                ch_r "Yeah, ok, [RogueX.Petname]."              
                return
            "Maybe later?" if "no fondle ass" not in RogueX.DailyActions:
                $ RogueX.FaceChange("sexy")  
                ch_r "Heh, maybe, [RogueX.Petname]."
                $ RogueX.Statup("Love", 80, 2)
                $ RogueX.Statup("Inbt", 50, 2)  
                if Taboo:                    
                    $ RogueX.AddWord(1,"tabno","tabno")  
                $ RogueX.RecentActions.append("no fondle ass")                      
                $ RogueX.DailyActions.append("no fondle ass")            
                return
            "Just one good squeeze?":             
                if Approval:
                    $ RogueX.FaceChange("sexy")     
                    $ RogueX.Statup("Obed", 90, 1)
                    $ RogueX.Statup("Obed", 50, 2)
                    ch_r "Well, if you're gonna beg. . ."                           
                    $ RogueX.Statup("Inbt", 70, 1) 
                    $ RogueX.Statup("Inbt", 40, 2) 
                    jump Rogue_FA_Prep
                else:   
                    $ RogueX.FaceChange("sexy") 
                    ch_r "Tsk, not this time, [RogueX.Petname]."      
            
            "[[Start fondling anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck(RogueX, 250, "OI", TabM = 3) # 25, 40, 55, -120(145)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.FaceChange("sad")
                    $ RogueX.Statup("Love", 70, -3, 1)
                    $ RogueX.Statup("Love", 200, -1) 
                    ch_r "Fine, I suppose."                
                    $ RogueX.Statup("Obed", 50, 3)
                    $ RogueX.Statup("Inbt", 60, 3) 
                    if Approval < 2:                          
                        $ RogueX.Forced = 1
                    jump Rogue_FA_Prep
                else:                              
                    $ RogueX.Statup("Love", 200, -10)  
                    $ RogueX.FaceChange("angry", 1)
                    "She slaps your hand away."   
                    $ RogueX.AddWord(1,"angry","angry")     
                        
    if "no fondle ass" in RogueX.DailyActions:
        ch_r "Learn to take \"no\" for an answer, [RogueX.Petname]."   
        $ RogueX.AddWord(1,"angry","angry")  
    elif RogueX.Forced:
        $ RogueX.FaceChange("angry", 1)
        ch_r "Hands off the booty!"
        $ RogueX.Statup("Lust", 60, 5)    
        $ RogueX.Statup("Obed", 50, -2)   
        $ RogueX.AddWord(1,"angry","angry")  
    elif Taboo:
        $ RogueX.FaceChange("angry", 1)    
        $ RogueX.AddWord(1,"tabno","tabno")  
        ch_r "[RogueX.Petname]! Not in public!"                   
    elif RogueX.FondleA:
        $ RogueX.FaceChange("sad")
        ch_r "Sorry, hands off the booty."        
    else:
        $ RogueX.FaceChange("sexy") 
        $ RogueX.Mouth = "sad"
        ch_r "Shoo, [RogueX.Petname]."
    $ RogueX.RecentActions.append("no fondle ass")                      
    $ RogueX.DailyActions.append("no fondle ass") 
    $ Tempmod = 0    
    return
        
ch_r "Sorry, I don't even know how I got here. . ."
return

label Rogue_FA_Prep: #Animation set-up 
    if Trigger2 == "fondle ass":
        return
    if not RogueX.Forced and Situation != "auto":
        $ Tempmod = 0
        call Bottoms_Off(RogueX)
        if "angry" in RogueX.RecentActions:
            return    
    $ Tempmod = 0      
    call Rogue_Pussy_Launch("fondle ass")
    if not RogueX.FondleA:        
        if RogueX.Forced:
            $ RogueX.Statup("Love", 90, -20)
            $ RogueX.Statup("Obed", 70, 20)
            $ RogueX.Statup("Inbt", 80, 15) 
        else:
            $ RogueX.Statup("Love", 90, 10)
            $ RogueX.Statup("Obed", 70, 12)
            $ RogueX.Statup("Inbt", 80, 20)
    if Taboo:
        $ RogueX.Inbt += int(Taboo/10)  
        $ RogueX.Lust += int(Taboo/5)
     
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0   
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ RogueX.DrainWord("tabno")
    $ RogueX.DrainWord("no fondle ass")
    $ RogueX.AddWord(0,"fondle ass","fondle ass")
    
label Rogue_FA_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus(RogueX) 
        call Rogue_Pussy_Launch("fondle ass")
        $ RogueX.LustFace()   
        
        if  Player.Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                                              
                        "Slap her ass":                     
                                    call Slap_Ass(RogueX)  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Rogue_FA_Cycle  
                                    
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
                                            if RogueX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ RogueX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(RogueX,"tired")  # "I'm actually getting a little tired,"  
                                                
                                    "Shift primary action":
                                            if RogueX.Action and MultiAction:
                                                    menu:                                                             
                                                        "I want to stick a finger in.":
                                                                $ Situation = "shift"
                                                                call Rogue_FA_After
                                                                call Rogue_Insert_Ass    
                                                        "Just stick a finger in without asking.":
                                                                $ Situation = "auto"
                                                                call Rogue_FA_After
                                                                call Rogue_Insert_Ass
                                                        "I want to lick your asshole.":
                                                                $ Situation = "shift"
                                                                call Rogue_FA_After
                                                                call Rogue_Lick_Ass                 
                                                        "Just start licking.":
                                                                $ Situation = "auto"
                                                                call Rogue_FA_After
                                                                call Rogue_Lick_Ass    
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Rogue_FA_After
                                                                call Rogue_Dildo_Ass  
                                                        "Never Mind":
                                                                jump Rogue_FA_Cycle
                                            else: 
                                                call Sex_Basic_Dialog(RogueX,"tired")  # "I'm actually getting a little tired,"           
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Rogue_FA_After
                                                call Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask [RogueX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(RogueX)
                                            "Ask [RogueX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(RogueX)  
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0    
                                                        
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(RogueX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Rogue_FA_Cycle 
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Rogue_FA_Cycle 
                                            "Never mind":
                                                        jump Rogue_FA_Cycle 
                                    "Undress [RogueX.Name]":
                                            call Girl_Undress(RogueX)   
                                    "Clean up [RogueX.Name] (locked)" if not RogueX.Spunk:
                                            pass  
                                    "Clean up [RogueX.Name]" if RogueX.Spunk:
                                            call Girl_Cleanup(RogueX,"ask")                                         
                                    "Never mind":
                                            jump Rogue_FA_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Rogue_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Rogue_FA_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Rogue_Pos_Reset
                                    $ Line = 0
                                    jump Rogue_FA_After
        #End menu (if Line)
        
        if RogueX.Panties or RogueX.PantsNum() >= 6 or RogueX.HoseNum() >= 5: #This checks if Rogue wants to strip down.
                call Girl_Undress(RogueX,"auto")
                
        call Shift_Focus(RogueX)
        call Sex_Dialog(RogueX,Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or RogueX.Lust >= 100: 
                    #If either of you could cum   
                    if Player.Focus >= 100:    
                            #If you can cum:                                                 
                            call Player_Cumming(RogueX)
                            if "angry" in RogueX.RecentActions:  
                                call Rogue_Pos_Reset
                                return    
                            $ RogueX.Statup("Lust", 200, 5) 
                            if 100 > RogueX.Lust >= 70 and RogueX.OCount < 2 and RogueX.SEXP >= 20:              
                                $ RogueX.AddWord(0,"unsatisfied","unsatisfied")
                            
                            if Player.Focus > 80:
                                jump Rogue_FA_After 
                            $ Line = "came"
     
                    if RogueX.Lust >= 100:  
                            #If Rogue can cum                                             
                            call Girl_Cumming(RogueX)
                            if Situation == "shift" or "angry" in RogueX.RecentActions:
                                jump Rogue_FA_After
                       
                    if Line == "came": #ex Player.Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in RogueX.RecentActions:#And Rogue is unsatisfied,  
                                "[RogueX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Rogue_FA_After   
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)            
        #End orgasm
        
        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0
                    
        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif Cnt == (5 + RogueX.FondleA):
                    $ RogueX.Brows = "confused"
                    ch_r "Uh, that's nice, but. . ."  
        elif RogueX.Lust >= 80:
                    pass
        elif Cnt == (15 + RogueX.FondleA) and RogueX.SEXP >= 15 and not ApprovalCheck(RogueX, 1500):
                    $ RogueX.Brows = "confused"        
                    menu:
                        ch_r "[RogueX.Petname], this is nice, but could we do something else?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Rogue_FA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Rogue_FA_After
                        "No, this is fun.":   
                                if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):                        
                                    $ RogueX.Statup("Love", 200, -5)
                                    $ RogueX.Statup("Obed", 50, 3)                    
                                    $ RogueX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ RogueX.FaceChange("angry", 1)   
                                    call Rogue_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_r "Well if that's your attitude, I don't need your \"help\"."                         
                                    $ RogueX.Statup("Love", 50, -3, 1)
                                    $ RogueX.Statup("Love", 80, -4, 1)
                                    $ RogueX.Statup("Obed", 30, -1, 1)                    
                                    $ RogueX.Statup("Obed", 50, -1, 1)  
                                    $ RogueX.AddWord(1,"angry","angry")   
                                    jump Rogue_FA_After
        #End Count check
        
        call Escalation(RogueX) #sees if she wants to escalate things
        
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    $ RogueX.FaceChange("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.Petname], that's enough of that for now."
    
    
label Rogue_FA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Rogue_Pos_Reset
        
    $ RogueX.FaceChange("sexy") 
    
    $ RogueX.FondleA += 1  
    $ RogueX.Action -=1            
    if RogueX.PantsNum() < 6 or RogueX.Upskirt:        
        $ RogueX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ RogueX.Addictionrate += 1
    
        call Partner_Like(RogueX,2)
     
    if RogueX.FondleA == 1:            
            $ RogueX.SEXP += 4         
            if not Situation: 
                if RogueX.Love >= 500 and "unsatisfied" not in RogueX.RecentActions:
                    ch_r "That was. . . nice. . ."
                elif RogueX.Obed <= 500 and Player.Focus <= 20:
                    $ RogueX.FaceChange("perplexed", 1)
                    ch_r "Did you like that?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_r "Mmm, so what else did you have in mind?"
    call Checkout    
    return   


# end RogueX.Fondle Ass /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Ass    
label Rogue_Insert_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(RogueX)
    if RogueX.InsertA: #You've done it before
        $ Tempmod += 25
    if RogueX.PantsNum() >= 6 or RogueX.HoseNum() >= 5: # she's got pants on.
        $ Tempmod -= 15    
    if RogueX.Lust > 85 and RogueX.Loose: #She's really horny
        $ Tempmod += 15
    if RogueX.Lust > 95 and RogueX.Loose:
        $ Tempmod += 5
    if Situation == "shift":
        $ Tempmod += 10
    if RogueX.Lust > 85 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in RogueX.Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in RogueX.Traits or "sex friend" in RogueX.Petnames:
        $ Tempmod += 10
    elif "ex" in RogueX.Traits:
        $ Tempmod -= 25 
    if RogueX.ForcedCount and not RogueX.Forced:
        $ Tempmod -= 5 * RogueX.ForcedCount
    
    if Taboo and "tabno" in RogueX.DailyActions:        
        $ Tempmod -= 10 
        
    if "no insert ass" in RogueX.DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no insert ass" in RogueX.RecentActions else 0   
            
    $ Approval = ApprovalCheck(RogueX, 1300, TabM = 3) # 130, 145, 160, Taboo -120(250)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            $ RogueX.FaceChange("surprised")
            $ RogueX.Statup("Obed", 90, 2)
            $ RogueX.Statup("Obed", 70, 2)
            $ RogueX.Statup("Inbt", 80, 2) 
            $ RogueX.Statup("Inbt", 30, 2) 
            "As you slide a finger in, [RogueX.Name] tightens around it in surprise, but seems into it."  
            $ RogueX.FaceChange("sexy")           
            jump Rogue_IA_Prep
        else:   
            $ RogueX.FaceChange("surprised")
            $ RogueX.Statup("Love", 80, -2)
            $ RogueX.Statup("Obed", 50, -3)
            ch_r "Keep it out of there, [RogueX.Petname]."                 
            $ Tempmod = 0
            $ Trigger2 = 0
            return          
    
    if "insert ass" in RogueX.DailyActions and not RogueX.Loose:
        $ RogueX.FaceChange("bemused", 1)
        ch_r "I'm still a little sore from earlier, [RogueX.Petname]."
    elif "insert ass" in RogueX.DailyActions:
        $ RogueX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so hard this time though.",
            "Mmm. . ."]) 
        ch_r "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .               
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Love", 70, -3, 1)
            $ RogueX.Statup("Love", 20, -2, 1)
            $ RogueX.Statup("Obed", 90, 1)
            $ RogueX.Statup("Inbt", 60, 1)
            ch_r "Sure, get in there."    
        else:
            $ RogueX.FaceChange("sexy", 1)
            $ RogueX.Eyes = "closed"            
            $ RogueX.Statup("Love", 90, 1)
            $ RogueX.Statup("Inbt", 50, 3)            
            $ RogueX.Statup("Lust", 200, 3)
            ch_r "Oooooooh. . ."                
        $ RogueX.Statup("Obed", 20, 1)
        $ RogueX.Statup("Obed", 60, 1)
        $ RogueX.Statup("Inbt", 70, 2) 
        jump Rogue_IA_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        $ RogueX.FaceChange("angry", 1)
        if "no insert ass" in RogueX.RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions and "no insert ass" in RogueX.DailyActions:  
            ch_r "I told you that wasn't appropriate!" 
        elif "no insert ass" in RogueX.DailyActions:       
            ch_r "I already told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions:  
            ch_r "I told you not in public!"  
        elif not RogueX.InsertA:
            $ RogueX.FaceChange("perplexed", 1)
            ch_r "I. . . don't think that's. . ."
        else:
            $ RogueX.FaceChange("bemused")
            ch_r "Oh, um, no, I'm not really comfortable with that. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no insert ass" in RogueX.DailyActions:
                $ RogueX.FaceChange("bemused")
                ch_r "Yeah, ok, [RogueX.Petname]."              
                return
            "Maybe later?" if "no insert ass" not in RogueX.DailyActions:
                $ RogueX.FaceChange("sexy")  
                ch_r "It's. . . possible, [RogueX.Petname]."
                $ RogueX.Statup("Love", 80, 2)
                $ RogueX.Statup("Inbt", 70, 2)   
                if Taboo:                    
                    $ RogueX.AddWord(1,"tabno","tabno")  
                $ RogueX.RecentActions.append("no insert ass")                      
                $ RogueX.DailyActions.append("no insert ass")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    $ RogueX.FaceChange("sexy")           
                    $ RogueX.Statup("Obed", 90, 2)
                    $ RogueX.Statup("Obed", 50, 2)
                    ch_r "Ok, you're probably right. . ."      
                    $ RogueX.Statup("Inbt", 70, 3) 
                    $ RogueX.Statup("Inbt", 40, 2)
                    jump Rogue_IA_Prep
                else:   
                    $ RogueX.FaceChange("bemused") 
                    ch_r "I really don't think that I would."     
            
            "[[Slide a finger in anyway]":                                               # Pressured into being fingered. 
                $ Approval = ApprovalCheck(RogueX, 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                if Approval > 1 or (Approval and RogueX.Forced):                    
                    $ RogueX.FaceChange("surprised", 1)
                    $ RogueX.Statup("Love", 70, -5, 1)
                    $ RogueX.Statup("Love", 200, -2)                 
                    ch_r "Oh. . . well, ok then. . ."                     
                    $ RogueX.FaceChange("sad")
                    $ RogueX.Statup("Obed", 50, 4)
                    $ RogueX.Statup("Inbt", 80, 1) 
                    $ RogueX.Statup("Inbt", 60, 3)  
                    if Approval < 2:                          
                        $ RogueX.Forced = 1
                    jump Rogue_IA_Prep
                else:                              
                    $ RogueX.Statup("Love", 200, -15)  
                    $ RogueX.FaceChange("angry", 1)
                    "She slaps your hand away."   
                    $ RogueX.AddWord(1,"angry","angry")   
                    
    if "no insert ass" in RogueX.DailyActions:
        ch_r "Learn to take \"no\" for an answer, [RogueX.Petname]."   
        $ RogueX.AddWord(1,"angry","angry")  
    elif RogueX.Forced:
        $ RogueX.FaceChange("angry", 1)
        ch_r "Um, no way."
        if RogueX.Inbt > 50:
                $ RogueX.Statup("Lust", 80, 10)  
        else:
                $ RogueX.Statup("Lust", 50, 3)
        $ RogueX.Statup("Obed", 50, -2)      
        $ RogueX.AddWord(1,"angry","angry")   
    elif Taboo:
        $ RogueX.FaceChange("angry", 1)    
        $ RogueX.AddWord(1,"tabno","tabno")  
        ch_r "[RogueX.Petname]! This just really isn't the time or place!"                   
    elif RogueX.InsertA:
        $ RogueX.FaceChange("sad") 
        ch_r "I think you should keep your fingers to yourself."    
    else:
        $ RogueX.FaceChange("surprised")
        ch_r "I. . . not there!!"
        $ RogueX.FaceChange()
    $ RogueX.RecentActions.append("no insert ass")                      
    $ RogueX.DailyActions.append("no insert ass") 
    $ Tempmod = 0    
    return
    
        
label Rogue_IA_Prep: #Animation set-up 
    if Trigger2 == "insert ass":
        return
            
    call Rogue_Pussy_Launch("insert ass")
        
    if Situation == RogueX:                                                         
            #Rogue auto-starts    
            $ Situation = 0
            if (RogueX.Legs and not RogueX.Upskirt) or (RogueX.Panties and not RogueX.PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck(RogueX, 1250, TabM = 1) or (RogueX.SeenPussy and ApprovalCheck(RogueX, 500) and not Taboo):
                        $ RogueX.Upskirt = 1
                        $ RogueX.PantiesDown = 1
                        $ Line = 0
                        if RogueX.PantsNum() == 5:
                            $ Line = RogueX.Name+" hikes up her skirt"
                        elif RogueX.PantsNum() > 6:
                            $ Line = RogueX.Name+" pulls down her " + RogueX.Legs
                        else:
                            $ Line = 0                            
                        if RogueX.Panties:
                            if Line:
                                #wearing pants
                                "[Line] and pulls her [RogueX.Panties] out of the way."
                                "She then grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
                            else:
                                #no pants
                                "She pulls her [RogueX.Panties] out of the way, and then presses your hand against her asshole."
                                "She clearly intends for you to get to work." 
                        else:
                            #pants but no panties
                            "[Line], and then presses your hand against her asshole."
                            "She clearly intends for you to get to work."                     
                        call Rogue_First_Bottomless(1)
                else:
                        "[RogueX.Name] grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
            else:
                        "[RogueX.Name] grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":                    
                    $ RogueX.Statup("Inbt", 80, 3) 
                    $ RogueX.Statup("Inbt", 50, 2)
                    "You press your finger into it."
                "Praise her.":       
                    $ RogueX.FaceChange("sexy", 1)                    
                    $ RogueX.Statup("Inbt", 80, 3) 
                    ch_p "Dirty girl, [RogueX.Pet]."
                    $ RogueX.NameCheck() #checks reaction to petname
                    "You press your finger into it."
                    $ RogueX.Statup("Love", 85, 1)
                    $ RogueX.Statup("Obed", 90, 1)
                    $ RogueX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your hand back."
                    $ RogueX.FaceChange("surprised")       
                    $ RogueX.Statup("Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [RogueX.Pet]."
                    $ RogueX.NameCheck() #checks reaction to petname
                    "[RogueX.Name] pulls back."
                    $ RogueX.Statup("Obed", 90, 1)
                    $ RogueX.Statup("Obed", 50, 1)
                    $ RogueX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")      
                    $ RogueX.AddWord(1,"refused","refused")  
                    return          
            #end auto
          
    if not RogueX.Forced and Situation != "auto":
        $ Tempmod = 0
        call Bottoms_Off(RogueX)
        if "angry" in RogueX.RecentActions:
            return    
            
    $ Tempmod = 0    
    if not RogueX.InsertA:        
        if RogueX.Forced:
            $ RogueX.Statup("Love", 90, -50)
            $ RogueX.Statup("Obed", 70, 60)
            $ RogueX.Statup("Inbt", 80, 35) 
        else:
            $ RogueX.Statup("Love", 90, 10)
            $ RogueX.Statup("Obed", 70, 20)
            $ RogueX.Statup("Inbt", 80, 25)
            
    if Taboo:
        $ RogueX.Inbt += int(Taboo/10)  
        $ RogueX.Lust += int(Taboo/5)
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0    
    $ Cnt = 0
    if Taboo:
        $ RogueX.DrainWord("tabno")
    $ RogueX.DrainWord("no insert ass")
    $ RogueX.AddWord(0,"insert ass","insert ass")
    
label Rogue_IA_Cycle: #Repeating strokes 
    while Round >=0:  
        call Shift_Focus(RogueX) 
        call Rogue_Pussy_Launch("insert ass")
        $ RogueX.LustFace()   
        
        if  Player.Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                                              
                        "Slap her ass":                     
                                    call Slap_Ass(RogueX)  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Rogue_IA_Cycle  
                                    
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
                                            if RogueX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ RogueX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(RogueX,"tired")  # "I'm actually getting a little tired,"  
                                                
                                    "Shift primary action":
                                            if RogueX.Action and MultiAction:
                                                    menu:                                                             
                                                        "Pull out and start rubbing again.":
                                                                $ Situation = "pullback"
                                                                call Rogue_IA_After
                                                                call Rogue_Fondle_Ass
                                                        "I want to lick your asshole.":
                                                                $ Situation = "shift"
                                                                call Rogue_IA_After
                                                                call Rogue_Lick_Ass                 
                                                        "Just start licking.":
                                                                $ Situation = "auto"
                                                                call Rogue_IA_After
                                                                call Rogue_Lick_Ass    
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Rogue_IA_After
                                                                call Rogue_Dildo_Ass  
                                                        "Never Mind":
                                                                jump Rogue_IA_Cycle
                                            else: 
                                                call Sex_Basic_Dialog(RogueX,"tired")  # "I'm actually getting a little tired,"           
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Rogue_IA_After
                                                call Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask [RogueX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(RogueX)
                                            "Ask [RogueX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(RogueX)  
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0    
                                                        
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(RogueX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Rogue_IA_Cycle 
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Rogue_IA_Cycle 
                                            "Never mind":
                                                        jump Rogue_IA_Cycle 
                                    "Undress [RogueX.Name]":
                                            call Girl_Undress(RogueX)   
                                    "Clean up [RogueX.Name] (locked)" if not RogueX.Spunk:
                                            pass  
                                    "Clean up [RogueX.Name]" if RogueX.Spunk:
                                            call Girl_Cleanup(RogueX,"ask")                                         
                                    "Never mind":
                                            jump Rogue_IA_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Rogue_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Rogue_IA_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Rogue_Pos_Reset
                                    $ Line = 0
                                    jump Rogue_IA_After
        #End menu (if Line)
        
        if RogueX.Panties or RogueX.PantsNum() >= 6 or RogueX.HoseNum() >= 5: #This checks if Rogue wants to strip down.
                call Girl_Undress(RogueX,"auto")
                
        call Shift_Focus(RogueX)
        call Sex_Dialog(RogueX,Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or RogueX.Lust >= 100: 
                    #If either of you could cum   
                    if Player.Focus >= 100:    
                            #If you can cum:                                                 
                            call Player_Cumming(RogueX)
                            if "angry" in RogueX.RecentActions:  
                                call Rogue_Pos_Reset
                                return    
                            $ RogueX.Statup("Lust", 200, 5) 
                            if 100 > RogueX.Lust >= 70 and RogueX.OCount < 2:                   
                                $ RogueX.AddWord(0,"unsatisfied","unsatisfied")
                            
                            if Player.Focus > 80:
                                jump Rogue_IA_After 
                            $ Line = "came"
     
                    if RogueX.Lust >= 100:  
                            #If Rogue can cum                                             
                            call Girl_Cumming(RogueX)
                            if Situation == "shift" or "angry" in RogueX.RecentActions:
                                jump Rogue_IA_After
                       
                    if Line == "came": #ex Player.Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in RogueX.RecentActions:#And Rogue is unsatisfied,  
                                "[RogueX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Rogue_IA_After    
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)            
        #End orgasm
        
        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0
        
        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif Cnt == (5 + RogueX.InsertA):
                    $ RogueX.Brows = "confused"
                    ch_r "What are you even doing down there?" 
        elif RogueX.Lust >= 80:
                    pass
        elif Cnt == (15 + RogueX.InsertA) and RogueX.SEXP >= 15 and not ApprovalCheck(RogueX, 1500):
                    $ RogueX.Brows = "confused"        
                    menu:
                        ch_r "[RogueX.Petname], this is getting uncomfortable, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Rogue_IA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Rogue_IA_After
                        "No, this is fun.":   
                                if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):                        
                                    $ RogueX.Statup("Love", 200, -5)
                                    $ RogueX.Statup("Obed", 50, 3)                    
                                    $ RogueX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ RogueX.FaceChange("angry", 1)   
                                    call Rogue_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_r "Well if that's your attitude, I don't need your \"help\"."                         
                                    $ RogueX.Statup("Love", 50, -3, 1)
                                    $ RogueX.Statup("Love", 80, -4, 1)
                                    $ RogueX.Statup("Obed", 30, -1, 1)                    
                                    $ RogueX.Statup("Obed", 50, -1, 1)  
                                    $ RogueX.AddWord(1,"angry","angry")    
                                    jump Rogue_IA_After
        #End Count check
           
        call Escalation(RogueX) #sees if she wants to escalate things
        
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    $ RogueX.FaceChange("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.Petname], that's enough of that for now."
    
    
label Rogue_IA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Rogue_Pos_Reset
        
    $ RogueX.FaceChange("sexy") 
    
    $ RogueX.InsertA += 1  
    $ RogueX.Action -=1            
    $ RogueX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ RogueX.Addictionrate += 1
        
    call Partner_Like(RogueX,2)
     
    if RogueX.InsertA == 1:            
            $ RogueX.SEXP += 12         
            if not Situation: 
                if RogueX.Love >= 500 and "unsatisfied" not in RogueX.RecentActions:
                    ch_r "That felt. . . interesting. . ."
                elif RogueX.Obed <= 500 and Player.Focus <= 20:
                    $ RogueX.FaceChange("perplexed", 1)
                    ch_r "Did you like that?"
     
    $ Tempmod = 0  
    call Checkout
    return   


# end RogueX.Insert Ass /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Ass    
label Rogue_Lick_Ass: 
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(RogueX)
                                                                             # Will she let you lick? Modifiers         
    if RogueX.LickA: #You've done it before
        $ Tempmod += 20
    if RogueX.PantsNum() >= 6 or RogueX.HoseNum() >= 5: # she's got pants on.
        $ Tempmod -= 25 
    if RogueX.Lust > 95:
        $ Tempmod += 20  
    elif RogueX.Lust > 85: #She's really horny
        $ Tempmod += 15    
    if RogueX.Lust > 85 and Situation == "auto": #auto
        $ Tempmod += 10 
    if Situation == "shift":
        $ Tempmod += 10
    if "exhibitionist" in RogueX.Traits:
        $ Tempmod += (4*Taboo) 
    if "dating" in RogueX.Traits or "sex friend" in RogueX.Petnames:
        $ Tempmod += 10
    elif "ex" in RogueX.Traits:
        $ Tempmod -= 25  
    if RogueX.ForcedCount and not RogueX.Forced:
        $ Tempmod -= 5 * RogueX.ForcedCount 
    
    if Taboo and "tabno" in RogueX.DailyActions:        
        $ Tempmod -= 10 
        
    if "no lick ass" in RogueX.DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no lick ass" in RogueX.RecentActions else 0   
            
    $ Approval = ApprovalCheck(RogueX, 1550, TabM = 4) # 155, 170, 185, Taboo -160(315)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            $ RogueX.FaceChange("surprised")   
            $ RogueX.Statup("Obed", 90, 1)
            $ RogueX.Statup("Inbt", 80, 3) 
            $ RogueX.Statup("Inbt", 40, 2) 
            "As you crouch down and start to lick her asshole, [RogueX.Name] startles briefly, but then begins to melt."  
            $ RogueX.FaceChange("sexy")  
            jump Rogue_LA_Prep
        else:   
            $ RogueX.FaceChange("surprised")
            $ RogueX.Statup("Love", 80, -2)
            $ RogueX.Statup("Obed", 50, -3)
            ch_r "Um, no, I'm not really. . . don't."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return  
    
    if "lick ass" in RogueX.RecentActions:
        $ RogueX.FaceChange("sexy", 1)
        ch_r "Mmm, again? Ok."
        jump Rogue_LA_Prep
    elif "lick ass" in RogueX.DailyActions:
        $ RogueX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "I'm still tingling a bit from earlier.",
            "Mmm. . ."]) 
        ch_r "[Line]"
    
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Love", 70, -3, 1)
            $ RogueX.Statup("Love", 20, -2, 1)
            $ RogueX.Statup("Obed", 90, 2)
            $ RogueX.Statup("Inbt", 60, 2)
            ch_r "Sure, get in there."    
        else:
            $ RogueX.FaceChange("sexy", 1)
            $ RogueX.Eyes = "closed"            
            $ RogueX.Statup("Love", 90, 1)
            $ RogueX.Statup("Inbt", 60, 2)            
            $ RogueX.Statup("Lust", 200, 3)
            ch_r "Oooooooh. . ."                
        $ RogueX.Statup("Obed", 20, 1)
        $ RogueX.Statup("Obed", 60, 1)
        $ RogueX.Statup("Inbt", 80, 2) 
        jump Rogue_LA_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .           
        $ RogueX.FaceChange("angry", 1)
        if "no lick ass" in RogueX.RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions and "no lick ass" in RogueX.DailyActions:  
            ch_r "I told you not to touch me like that in public!" 
        elif "no lick ass" in RogueX.DailyActions:       
            ch_r "I already told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions:  
            ch_r "I told you not in public!"  
        elif not RogueX.LickA:                    #First time dialog
            $ RogueX.FaceChange("bemused", 1)
            if RogueX.Love >= RogueX.Obed and RogueX.Love >= RogueX.Inbt:            
                ch_r "I'm not really sure I want you lick'in down there. . ."
            elif RogueX.Obed >= RogueX.Inbt:            
                ch_r "You really don't have to if you don't want to."
            else:
                $ RogueX.Eyes = "sexy"
                ch_r "Hmm. . . it's worth a shot. . ."
        else:
            $ RogueX.FaceChange("bemused")
            ch_r "Not now, [RogueX.Petname]."  
        menu:
            extend ""
            "Sorry, never mind." if "no lick ass" in RogueX.DailyActions:
                $ RogueX.FaceChange("bemused")
                ch_r "Yeah, ok, [RogueX.Petname]."              
                return
            "I'm sure I can convince you later. . ." if "no lick ass" not in RogueX.DailyActions:
                $ RogueX.FaceChange("sexy")  
                ch_r "Anything's possible, [RogueX.Petname]."
                $ RogueX.Statup("Love", 80, 2)
                $ RogueX.Statup("Inbt", 70, 2)   
                if Taboo:                    
                    $ RogueX.AddWord(1,"tabno","tabno")   
                $ RogueX.RecentActions.append("no lick ass")                      
                $ RogueX.DailyActions.append("no lick ass")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    $ RogueX.FaceChange("sexy")           
                    $ RogueX.Statup("Obed", 90, 2)
                    $ RogueX.Statup("Obed", 50, 2)
                    ch_r "Ok, you're probably right. . ."      
                    $ RogueX.Statup("Inbt", 70, 3) 
                    $ RogueX.Statup("Inbt", 40, 2)
                    jump Rogue_LA_Prep
                else:   
                    $ RogueX.FaceChange("sexy") 
                    ch_r "Tsk, not this time, [RogueX.Petname], that just seems. . . dirty."        
            
            "[[Start licking anyway]":                                               # Pressured into being licked. 
                $ Approval = ApprovalCheck(RogueX, 1100, "OI", TabM = 4) # 110, 125, 140, -160(270)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.FaceChange("sad")
                    $ RogueX.Statup("Love", 70, -5, 1)
                    $ RogueX.Statup("Love", 200, -2)                 
                    ch_r "Ok, get in there if you're so determined."  
                    $ RogueX.Statup("Obed", 50, 4)
                    $ RogueX.Statup("Inbt", 80, 1) 
                    $ RogueX.Statup("Inbt", 60, 3)  
                    if Approval < 2:                          
                        $ RogueX.Forced = 1
                    jump Rogue_LA_Prep
                else:                              
                    $ RogueX.Statup("Love", 200, -15)  
                    $ RogueX.FaceChange("angry", 1)
                    "She shoves your head back."   
                    $ RogueX.AddWord(1,"angry","angry") 
                    
    if "no lick ass" in RogueX.DailyActions:
        ch_r "Learn to take \"no\" for an answer, [RogueX.Petname]."   
        $ RogueX.AddWord(1,"angry","angry") 
    elif RogueX.Forced:
        $ RogueX.FaceChange("angry", 1)
        ch_r "Ew, no way."
        if RogueX.Inbt > 50:
                $ RogueX.Statup("Lust", 80, 10)  
        else:
                $ RogueX.Statup("Lust", 50, 3)
        $ RogueX.Statup("Obed", 50, -2)   
        $ RogueX.AddWord(1,"angry","angry")  
    elif Taboo:
        $ RogueX.FaceChange("angry", 1)
        $ RogueX.AddWord(1,"tabno","tabno")  
        ch_r "This just really isn't the time or place, [RogueX.Petname]!"                   
    elif RogueX.LickP:
        $ RogueX.FaceChange("sad") 
        ch_r "Sorry, keep your tongue in your mouth."    
    else:
        $ RogueX.FaceChange("surprised")
        ch_r "What?! Gross!"
        $ RogueX.FaceChange()
    $ RogueX.RecentActions.append("no lick ass")                      
    $ RogueX.DailyActions.append("no lick ass") 
    $ Tempmod = 0    
    return
        
label Rogue_LA_Prep: #Animation set-up  
    if Trigger2 == "lick ass":
        return
    if not RogueX.Forced and Situation != "auto":
        $ Tempmod = 0
        if RogueX.PantsNum() >= 6:
            $ Tempmod = 15
        call Bottoms_Off(RogueX)
        if "angry" in RogueX.RecentActions:
            return    
    $ Tempmod = 0  
    call Rogue_Pussy_Launch("lick ass")
    if not RogueX.LickA:        
        if RogueX.Forced:
            $ RogueX.Statup("Love", 90, -30)
            $ RogueX.Statup("Obed", 70, 40)
            $ RogueX.Statup("Inbt", 80, 80) 
        else:
            $ RogueX.Statup("Love", 90, 35)
            $ RogueX.Statup("Obed", 70, 25)
            $ RogueX.Statup("Inbt", 80, 55)
    if Taboo:
        $ RogueX.Inbt += int(Taboo/10)  
        $ RogueX.Lust += int(Taboo/5)
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    
    $ RogueX.Upskirt = 1
    if RogueX.PantsNum() == 5:
        $ RogueX.SeenPanties = 1
    call Rogue_First_Bottomless(1)
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ RogueX.DrainWord("tabno")
    $ RogueX.DrainWord("no lick ass")
    
    $ RogueX.AddWord(1,"lick","lick")
    $ RogueX.AddWord(1,"ass","ass")
    $ RogueX.AddWord(0,"lick ass","lick ass")
label Rogue_LA_Cycle: #Repeating strokes
    if Trigger2 == "kiss you":
            $ Trigger2 = 0
    while Round >=0:  
        call Shift_Focus(RogueX) 
        call Rogue_Pussy_Launch("lick ass")
        $ RogueX.LustFace()   
        
        if  Player.Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                                              
                        "Slap her ass":                     
                                    call Slap_Ass(RogueX)  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Rogue_LA_Cycle  
                                    
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
                                            if RogueX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ RogueX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(RogueX,"tired")  # "I'm actually getting a little tired,"  
                                                
                                    "Shift primary action":
                                            if RogueX.Action and MultiAction:
                                                    menu:                                                             
                                                        "Switch to fondling.":
                                                                $ Situation = "pullback"
                                                                call Rogue_LA_After
                                                                call Rogue_Fondle_Ass
                                                        "I want to stick a finger in.":
                                                                $ Situation = "shift"
                                                                call Rogue_LA_After
                                                                call Rogue_Insert_Ass                 
                                                        "Just stick a finger in [[without asking].":
                                                                $ Situation = "auto"
                                                                call Rogue_LA_After
                                                                call Rogue_Insert_Ass                        
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Rogue_LA_After
                                                                call Rogue_Dildo_Ass  
                                                        "Never Mind":
                                                                jump Rogue_LA_Cycle
                                            else: 
                                                call Sex_Basic_Dialog(RogueX,"tired")  # "I'm actually getting a little tired,"           
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Rogue_LA_After
                                                call Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask [RogueX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(RogueX)
                                            "Ask [RogueX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(RogueX)  
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0    
                                                        
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(RogueX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Rogue_LA_Cycle 
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Rogue_LA_Cycle 
                                            "Never mind":
                                                        jump Rogue_LA_Cycle 
                                    "Undress [RogueX.Name]":
                                            call Girl_Undress(RogueX)   
                                    "Clean up [RogueX.Name] (locked)" if not RogueX.Spunk:
                                            pass  
                                    "Clean up [RogueX.Name]" if RogueX.Spunk:
                                            call Girl_Cleanup(RogueX,"ask")                                         
                                    "Never mind":
                                            jump Rogue_LA_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Rogue_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Rogue_LA_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Rogue_Pos_Reset
                                    $ Line = 0
                                    jump Rogue_LA_After
        #End menu (if Line)
        
        if RogueX.Panties or RogueX.PantsNum() >= 6 or RogueX.HoseNum() >= 5: #This checks if Rogue wants to strip down.
                call Girl_Undress(RogueX,"auto")
                
        call Shift_Focus(RogueX)
        call Sex_Dialog(RogueX,Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or RogueX.Lust >= 100: 
                    #If either of you could cum   
                    if Player.Focus >= 100:    
                            #If you can cum:                                                 
                            call Player_Cumming(RogueX)
                            if "angry" in RogueX.RecentActions:  
                                call Rogue_Pos_Reset
                                return    
                            $ RogueX.Statup("Lust", 200, 5) 
                            if 100 > RogueX.Lust >= 70 and RogueX.OCount < 2:                
                                $ RogueX.AddWord(0,"unsatisfied","unsatisfied")
                            
                            if Player.Focus > 80:
                                jump Rogue_LA_After 
                            $ Line = "came"
     
                    if RogueX.Lust >= 100:  
                            #If Rogue can cum                                             
                            call Girl_Cumming(RogueX)
                            if Situation == "shift" or "angry" in RogueX.RecentActions:
                                jump Rogue_LA_After
                       
                    if Line == "came": #ex Player.Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."
                            
                            if "unsatisfied" in RogueX.RecentActions:#And Rogue is unsatisfied,  
                                "[RogueX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it" 
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Rogue_LA_After     
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)            
        #End orgasm
        
        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0
                    
        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
                    pass
        elif Cnt == (5 + RogueX.LickA):
                    $ RogueX.Brows = "confused"
                    ch_r "What are you even doing down there?"  
        elif RogueX.Lust >= 80:
                    pass
        elif Cnt == (15 + RogueX.LickA) and RogueX.SEXP >= 15 and not ApprovalCheck(RogueX, 1500):
                    $ RogueX.Brows = "confused"        
                    menu:
                        ch_r "[RogueX.Petname], this is getting uncomfortable, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Rogue_LA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Rogue_LA_After
                        "No, this is fun.":   
                                if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):                        
                                    $ RogueX.Statup("Love", 200, -5)
                                    $ RogueX.Statup("Obed", 50, 3)                    
                                    $ RogueX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ RogueX.FaceChange("angry", 1)   
                                    call Rogue_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_r "Well if that's your attitude, I don't need your \"help\"."                         
                                    $ RogueX.Statup("Love", 50, -3, 1)
                                    $ RogueX.Statup("Love", 80, -4, 1)
                                    $ RogueX.Statup("Obed", 30, -1, 1)                    
                                    $ RogueX.Statup("Obed", 50, -1, 1)  
                                    $ RogueX.AddWord(1,"angry","angry")   
                                    jump Rogue_LA_After
        #End Count check
           
        call Escalation(RogueX) #sees if she wants to escalate things
        
        if Round == 10:
                ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
                ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    $ RogueX.FaceChange("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.Petname], that's enough of that for now."
    
    
label Rogue_LA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Rogue_Pos_Reset
        
    $ RogueX.FaceChange("sexy") 
    
    $ RogueX.LickA += 1  
    $ RogueX.Action -=1      
    if RogueX.PantsNum() < 6 or RogueX.Upskirt:        
        $ RogueX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ RogueX.Addictionrate += 1
            
    call Partner_Like(RogueX,2)
                 
    if RogueX.LickA == 1:            
            $ RogueX.SEXP += 15         
            if not Situation: 
                if RogueX.Love >= 500 and "unsatisfied" not in RogueX.RecentActions:
                    ch_r "Was. . . that something you liked?"
                elif RogueX.Obed <= 500 and Player.Focus <= 20:
                    $ RogueX.FaceChange("perplexed", 1)
                    ch_r "Did you like that?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_r "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# end RogueX.Lick Ass /////////////////////////////////////////////////////////////////////////////

