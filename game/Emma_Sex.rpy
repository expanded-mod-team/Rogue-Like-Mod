# Emma_SexMenu //////////////////////////////////////////////////////////////////////
label Emma_SexAct(Act = 0):    
        call Shift_Focus(EmmaX)      
        if Taboo > 20 and "taboo" not in EmmaX.History:
                # If she's yet to agree to taboo stuff
                call Emma_Taboo_Talk
                if bg_current == "bg classroom":
                        ch_p "We could just lock the door, right?"
                        ch_e "We certainly could. . ."                
                        "[EmmaX.Name] walks to the door and locks it behind her."
                        $ Taboo = 0
                else:
                        return      
                        
        if Act == "SkipTo":
            $ renpy.pop_call() #causes it to skip past the Trigger Swap
            $ renpy.pop_call() #causes it to skip past the cycle you were in before
            #$ renpy.pop_call() #causes it to skip past the sex menu you were in before that
            call SkipTo(EmmaX)
        elif Act == "switch":
            $ renpy.pop_call() #causes it to skip past call here from Sex_Menu_Threesome
            #$ renpy.pop_call() #causes it to skip past call to Sex_Menu_Threesome
            # drops through to sex menu
        elif Act == "masturbate":         
            call Emma_M_Prep
            if not Situation:
                return        
        elif Act == "lesbian":  
            call Les_Prep(EmmaX)
            if not Situation:
                return   
        elif Act == "kissing":        
            call KissPrep(EmmaX)
            if not Situation:
                return   
        elif Act == "breasts":        
            call Emma_Fondle_Breasts
            if not Situation:
                return  
        elif Act == "blow":        
            call Emma_BJ_Prep
            if not Situation:
                return  
        elif Act == "hand":        
            call Emma_HJ_Prep
            if not Situation:
                return   
        elif Act == "sex":        
            call Emma_SexPrep
            if not Situation:
                return   

label Emma_SexMenu: 
        if "classcaught" not in EmmaX.History:
                ch_e "I can't imagine being a part of something so. . . tawdry." 
                return
        if "three" not in EmmaX.History and not AloneCheck(EmmaX):
                # if there are other girls in the room. . .
                call Emma_ThreeCheck
        if Taboo > 20 and "taboo" not in EmmaX.History:
                # If she's yet to agree to taboo stuff
                call Emma_Taboo_Talk
                if bg_current == "bg classroom" or bg_current in PersonalRooms and AloneCheck(EmmaX):
                        ch_p "We could just lock the door, right?"
                        ch_e "We certainly could. . ."                
                        "[EmmaX.Name] walks to the door and locks it behind her."                        
                        $ Player.Traits.append("locked")   
                        call Taboo_Level
                        
                else:
                        return          
        call Shift_Focus(EmmaX)
        $ Trigger = 0    
        $ Trigger2 = 0
        $ Trigger3 = 0
        $ Situation = 0
        call Emma_Hide    
        $ EmmaX.ArmPose = 1
        if "detention" in EmmaX.RecentActions:
                $ Tempmod = 20 if Tempmod <= 20 else Tempmod
        call Set_The_Scene(1,0,0,0,1)

        if not Player.Semen:
                "You're a little out of juice at the moment, you might want to wait a bit." 
        if Player.Focus >= 95:
                "You're practically buzzing, the slightest breeze could set you off."
        if not EmmaX.Action:
                "[EmmaX.Name]'s looking a bit tired out, maybe let her rest a bit."
        
        if "caught" in EmmaX.RecentActions or "angry" in EmmaX.RecentActions:  
                if EmmaX.Loc == bg_current:                
                            ch_e "I'd rather not deal with you at the moment."
                $ EmmaX.OutfitChange()        
                $ EmmaX.DrainWord("caught",1,0)
                return
            
        if Round < 5:
            ch_e "I think we could both do with a short break."   
            return
        menu Emma_SMenu:  
            ch_e "So, what was it you hoped to do?"
            "Do you want to make out?":
                        if EmmaX.Action:
                                call Makeout(EmmaX)
                        else:
                                ch_e "I'm sorry, [EmmaX.Petname], but I need a break." 
            
            "Could I touch you?":
                    if EmmaX.Action:
                        $ EmmaX.FaceChange("sly")                    
                        menu:
                            ch_e "Um, what did you want to touch, [EmmaX.Petname]?"                      
                            "Could I give you a massage?":
                                    call Massage(EmmaX)                        
                            "Your breasts?":
                                    call Emma_Fondle_Breasts
                            "Suck your breasts?" if EmmaX.Action and EmmaX.SuckB:
                                    call Emma_Suck_Breasts
                            "Your thighs?" if EmmaX.Action:
                                    call Emma_Fondle_Thighs
                            "Your pussy?" if EmmaX.Action:
                                    call Emma_Fondle_Pussy
                            "Lick your pussy?" if EmmaX.Action and EmmaX.LickP:
                                    call Emma_Lick_Pussy
                            "Your Ass?":
                                    call Emma_Fondle_Ass
                            "Never mind [[something else]":
                                    jump Emma_SMenu
                    else:
                        ch_e "I'm sorry, [EmmaX.Petname], but I need a break."
                        
            "Could you take care of something for me? [[Your dick, you mean your dick]":        
                    if Player.Semen and EmmaX.Action:                
                        menu:
                            ch_e "What did you want me to do?"
                            "Could you give me a handjob?":
                                    call Emma_Handjob
                            "Could you give me a titjob?":
                                    call Emma_Titjob         
                            "Could you suck my cock?":
                                    call Emma_Blowjob 
                            "Could use your feet?":
                                    call Emma_Footjob 
                            "Never mind [[something else]":
                                    jump Emma_SMenu
                    elif not EmmaX.Action:
                                "I'm sorry, [EmmaX.Petname], but I need a break."
                    else:
                                "You really don't have it in you, maybe take a break." 
                    
            "Could you put on a show for me?":
                        menu:
                            ch_e "What did you want to see?"
                            "Dance for me?":
                                    if EmmaX.Action:
                                        call Group_Strip(EmmaX)       
                                    else:
                                        "I'm sorry, [EmmaX.Petname], but I need a break."
                                    
                            "Could you undress for me?": 
                                        call Girl_Undress(EmmaX)  
                                                
                            "You've got a little something. . . [[clean-up]" if EmmaX.Spunk:
                                        ch_e "Huh?"
                                        call Girl_Cleanup(EmmaX,"ask")
                                        
                            "Could I watch you get yourself off? [[masturbate]":
                                    if EmmaX.Action:
                                        call Emma_Masturbate           
                                    else:
                                        "I'm sorry, [EmmaX.Petname], but I need a break."
                                                    
                            "Maybe make out with [RogueX.Name]?" if RogueX.Loc == bg_current:
                                        call LesScene(EmmaX)
                            "Maybe make out with [KittyX.Name]?" if KittyX.Loc == bg_current:
                                        call LesScene(EmmaX)
                            "Maybe make out with [LauraX.Name]?" if LauraX.Loc == bg_current:
                                        call LesScene(EmmaX)
                                    
                            "Never mind [[something else]":
                                        jump Emma_SMenu
                              
                    
            "Could we maybe?. . . [[fuck]":
                    if Player.Semen and EmmaX.Action:
                        menu:
                            "What did you want to do?"
                            "Come over here, I've got something in mind. . .":
                                    call Emma_Sex_H           
                            "Fuck your pussy.":                        
                                    call Emma_Sex_P           
                            "Fuck your ass.":                        
                                    call Emma_Sex_A    
                            "How about some toys? [[Pussy]":                        
                                    call Emma_Dildo_Pussy     
                            "How about some toys? [[Anal]":                        
                                    call Emma_Dildo_Ass   
                            "Never mind [[something else]":
                                    jump Emma_SMenu
                    elif not EmmaX.Action:
                                    "I'm sorry, [EmmaX.Petname], but I need a break."
                    else:
                                    "The spirit is apparently willing, but the flesh is spongy and bruised." 
                            
            "Hey, do you want in on this? [[Threesome]":
                                    call Sex_Menu_Threesome(EmmaX)
                                    jump Emma_SMenu
                                    
            "Hey, [Partner.Name]? [[Switch lead]" if Partner:
                        call expression Partner.Tag + "_SexAct" pass ("switch")   
                        return
                                    
            "Cheat Menu" if config.developer:
                                    call Cheat_Menu(EmmaX)
            "Never mind. [[exit]":         
                    if EmmaX.Lust >= 50 or EmmaX.Addict >= 50:
                            $ EmmaX.FaceChange("sad")
                            if EmmaX.Action and EmmaX.SEXP >= 15 and Round > 20:
                                    if "round2" not in EmmaX.RecentActions:  
                                        ch_e "Are you certain, [EmmaX.Petname]? Are you perhaps forgetting something?"                
                                        $ EmmaX.Statup("Inbt", 30, 2)
                                        $ EmmaX.Statup("Inbt", 50, 1)
                                    elif EmmaX.Addict >= 50:                        
                                        ch_e "I need more contact." 
                                    else:
                                        ch_e "I'm afraid that still wasn't enough."                          
                                    menu:
                                        extend ""
                                        "Yeah, I'm done for now." if Player.Semen and "round2" not in EmmaX.RecentActions:                 
                                            if "unsatisfied" in EmmaX.RecentActions and not EmmaX.OCount:                                
                                                $ EmmaX.FaceChange("angry")
                                                $ EmmaX.Eyes = "side" 
                                                $ EmmaX.Statup("Love", 70, -2)
                                                $ EmmaX.Statup("Love", 90, -4)
                                                $ EmmaX.Statup("Obed", 30, 2)
                                                $ EmmaX.Statup("Obed", 70, 1)
                                                ch_e "Well! This might count against you next time."
                                            else:                               
                                                $ EmmaX.FaceChange("bemused", 1)
                                                $ EmmaX.Statup("Obed", 50, 2)   
                                                ch_e "I suppose I'll have to blame myself as an educator."  
                                        "I gave it a shot." if "round2" in EmmaX.RecentActions:                 
                                            if "unsatisfied" in EmmaX.RecentActions and not EmmaX.OCount:                                
                                                $ EmmaX.FaceChange("angry")
                                                $ EmmaX.Eyes = "side"                                 
                                                ch_e "Yes, disappointingly so. . ."
                                            else:                               
                                                $ EmmaX.FaceChange("bemused", 1) 
                                                ch_e "I suppose you did. . .shame you couldn't do better. . ."  
                                        "Hey, I did my part." if EmmaX.OCount > 2:      
                                                $ EmmaX.FaceChange("sly", 1) 
                                                ch_e "Take it as a compliment that I expected more."  
                                        "I'm tapped out for the moment, let's try again later." if not Player.Semen:
                                                $ EmmaX.FaceChange("normal")                        
                                                ch_e "I suppose that can't be helped. . ."
                                        "Ok, we can try something else." if MultiAction and "round2" not in EmmaX.RecentActions:
                                                $ EmmaX.FaceChange("smile")
                                                $ EmmaX.Statup("Love", 70, 2)
                                                $ EmmaX.Statup("Love", 90, 1) 
                                                ch_e "Excellent. . ."                            
                                                $ EmmaX.RecentActions.append("round2")                      
                                                $ EmmaX.DailyActions.append("round2") 
                                                jump Emma_SexMenu
                                        "Again? Ok, fine." if MultiAction and "round2" in EmmaX.RecentActions:
                                                $ EmmaX.FaceChange("sly")
                                                ch_e "Always. . ."           
                                                jump Emma_SexMenu  
                                    #End "if [EmmaX.Name] is still up for more"
                            else:  
                                                $ EmmaX.FaceChange("bemused", 1)
                                                ch_e "I suppose I'm tired as well, [EmmaX.Petname]. We can take a breather. . ."  
                                                $ EmmaX.Statup("Inbt", 30, 2)
                                                $ EmmaX.Statup("Inbt", 50, 1)    
                            $ EmmaX.FaceChange()
                    else:
                                                ch_e "Fine."
                    call Sex_Over  
                    return
        if EmmaX.Loc != bg_current:
                    call Set_The_Scene
                    call Trig_Reset
                    return
        if not MultiAction:    
                    call Set_The_Scene
                    ch_e "That's all you get. . . for now."
                    $ EmmaX.OCount = 0
                    call Trig_Reset
                    return
        call GirlsAngry
        jump Emma_SexMenu
# end Emma_SexMenu //////////////////////////////////////////////////////////////////////            


##  EmmaX.Masturbating //////////////////////////////////////////////////////////////////////
# Cnt 1 means she's seen you, Cnt 0 means she hasn't.
label Emma_Masturbate: #(Situation = Situation):
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(EmmaX)
    if EmmaX.Mast:
        $ Tempmod += 10
    if EmmaX.SEXP >= 50:
        $ Tempmod += 25
    elif EmmaX.SEXP >= 30:
        $ Tempmod += 15
    elif EmmaX.SEXP >= 15:
        $ Tempmod += 5
    if EmmaX.Lust >= 90:
        $ Tempmod += 20
    elif EmmaX.Lust >= 75:
        $ Tempmod += 5
    if "exhibitionist" in EmmaX.Traits:      
        $ Tempmod += (3*Taboo) 
    if "dating" in EmmaX.Traits or "sex friend" in EmmaX.Petnames:
        $ Tempmod += 10
    elif "ex" in EmmaX.Traits:
        $ Tempmod -= 40  
    if EmmaX.ForcedCount and not EmmaX.Forced:        
        $ Tempmod -= 5 * EmmaX.ForcedCount   
        
    $ Approval = ApprovalCheck(EmmaX, 1300, TabM = 2) # 120, 135, 150, Taboo -80(200)
    
    $ EmmaX.DrainWord("unseen",1,0) #She sees you, so remove unseens
    
    if Situation == "join":       # This triggers if you ask to join in        
                if Approval > 1 or (Approval and EmmaX.Lust >= 50):
                    menu:        
                        extend ""
                        "Would you like some help? I could lend some helping hands. . ."  if Player.Semen and EmmaX.Action:
                                $ EmmaX.Statup("Love", 90, 1)
                                $ EmmaX.Statup("Obed", 50, 2)
                                $ EmmaX.FaceChange("sexy")
                                ch_e "Hm, well I do have my hands full with these. . ."                  
                                $ EmmaX.Statup("Obed", 70, 2)
                                $ EmmaX.Statup("Inbt", 70, 1)
                                $ Trigger2 = "fondle breasts"
                                $ EmmaX.Mast += 1
                                jump Emma_M_Cycle
                        "Would you like some help? I could. . . up to you, I guess." if Player.Semen and EmmaX.Action:
                                $ EmmaX.Statup("Love", 70, 2)
                                $ EmmaX.Statup("Love", 90, 1)
                                $ EmmaX.FaceChange("sexy")
                                ch_e "I suppose I could use some added attention. . ."                
                                $ EmmaX.Statup("Obed", 70, 2)
                                $ EmmaX.Statup("Inbt", 70, 1)
                                $ D20 = renpy.random.randint(1, 20)
                                if D20 > 10:
                                    $ Trigger2 = "fondle breasts"
                                else:
                                    $ Trigger2 = "suck breasts"
                                $ EmmaX.Mast += 1
                                jump Emma_M_Cycle
                        "Why don't we take care of each other?" if Player.Semen and EmmaX.Action:
                                $ EmmaX.FaceChange("sexy")
                                ch_e "I suppose I could spare some attention. . ."                    
                                $ renpy.pop_call()          #removes the call to this label 
                                return                      #returns to sexmenu=
                        "You look like you have things well in hand. . .":
                                if EmmaX.Lust >= 50:
                                    $ EmmaX.Statup("Love", 70, 2)
                                    $ EmmaX.Statup("Love", 90, 1)      
                                    $ EmmaX.FaceChange("sexy")
                                    ch_e "So you prefer to watch. . ."                    
                                    $ EmmaX.Statup("Obed", 80, 3)
                                    $ EmmaX.Statup("Inbt", 80, 5)  
                                    jump Emma_M_Cycle
                                elif ApprovalCheck(EmmaX, 1200):
                                    $ EmmaX.FaceChange("sly")                        
                                    ch_e "I did, but I wasn't intending perfomance art."
                                else:
                                    $ EmmaX.FaceChange("angry")
                                    ch_e "I did, but now the mood is ruined. . ."
                                    
                #else: You've failed all checks so she kicks you out.
                $ EmmaX.ArmPose = 1  
                $ EmmaX.OutfitChange()  
                $ EmmaX.Action -= 1
                $ Player.Statup("Focus", 50, 30)
                call Checkout(1)
                $ Line = 0
                $ Situation = 0      
                $ renpy.pop_call()          #removes the call to this label 
                if Approval:     
                        $ EmmaX.FaceChange("bemused", 1)
                        if bg_current == "bg emma":
                            ch_e "Why are you even in my room?"   
                        else:
                            ch_e "I wasn't expecting visitors. . ." 
                        $ EmmaX.Blush = 0
                else:
                        $ EmmaX.Statup("Love", 200, -5)
                        $ EmmaX.FaceChange("angry")
                        $ EmmaX.RecentActions.append("angry")
                        $ EmmaX.DailyActions.append("angry")  
                        if bg_current == "bg emma":
                            ch_e "You may have noticed, I had some work to take care of, so if you'll leave me to it. . ."
                            "[EmmaX.Name] kicks you out of her room."
                            $ renpy.pop_call()
                            jump Campus_Map  
                        else:
                            ch_e "I think I'll be leaving, if you don't mind."    
                            call Remove_Girl(EmmaX)
                return                      #returns to sexmenu, which returns to original    
    #End of "Join" option
    
    
    
    if Situation == EmmaX:                                                                  #Emma auto-starts   
                if Approval > 2:                                                      # fix, add emma auto stuff here
                        if EmmaX.PantsNum() == 5:
                            "[EmmaX.Name]'s hand snakes down her body, and hikes up her skirt."
                            $ EmmaX.Upskirt = 1
                        elif EmmaX.PantsNum() > 6:
                            "[EmmaX.Name] slides her hand down her body and into her pants."  
                        elif EmmaX.HoseNum() >= 5:
                            "[EmmaX.Name]'s hand slides down her body and under her [EmmaX.Hose]."
                        elif EmmaX.Panties:                
                            "[EmmaX.Name]'s hand slides down her body and under her [EmmaX.Panties]."
                        else:
                            "[EmmaX.Name]'s hand slides down her body and begins to caress her pussy."
                        $ EmmaX.SeenPanties = 1
                        "She starts to slowly rub herself."
                        call Emma_First_Bottomless
                        menu:
                            "What do you do?"
                            "Nothing.":                    
                                    $ EmmaX.Statup("Inbt", 80, 3) 
                                    $ EmmaX.Statup("Inbt", 60, 2)
                                    "[EmmaX.Name] begins to masturbate."
                            "Go for it.":       
                                    $ EmmaX.FaceChange("sexy, 1")                    
                                    $ EmmaX.Statup("Inbt", 80, 3) 
                                    ch_p "That is so sexy, [EmmaX.Pet]."
                                    $ EmmaX.NameCheck() #checks reaction to petname
                                    "You lean back and enjoy the show."
                                    $ EmmaX.Statup("Love", 80, 1)
                                    $ EmmaX.Statup("Obed", 90, 1)
                                    $ EmmaX.Statup("Obed", 50, 2)
                            "Ask her to stop.":
                                    $ EmmaX.FaceChange("surprised")       
                                    $ EmmaX.Statup("Inbt", 70, 1) 
                                    ch_p "Let's not do that right now, [EmmaX.Pet]."
                                    $ EmmaX.NameCheck() #checks reaction to petname
                                    "[EmmaX.Name] pulls her hands away from herself."
                                    $ EmmaX.OutfitChange()
                                    $ EmmaX.Statup("Obed", 90, 1)
                                    $ EmmaX.Statup("Obed", 50, 1)
                                    $ EmmaX.Statup("Obed", 30, 2)
                                    return            
                        jump Emma_M_Prep
                else:                
                        $ Tempmod = 0                               # fix, add emma auto stuff here
                        $ Trigger2 = 0
                return            
    #End if [EmmaX.Name] intitiates this action
    
    #first time
    if not EmmaX.Mast:                                                                
            $ EmmaX.FaceChange("surprised", 1)
            $ EmmaX.Mouth = "kiss"
            ch_e "So you enjoy a good show then. . ."
            if EmmaX.Forced:
                $ EmmaX.FaceChange("sad")
                ch_e "but. . . {i}only{/i} a show?"
            
            
    #First time dialog             
    if not EmmaX.Mast and Approval:                                                      
            if EmmaX.Forced: 
                $ EmmaX.FaceChange("sad")
                $ EmmaX.Statup("Love", 70, -3, 1)
                $ EmmaX.Statup("Love", 20, -2, 1)
            elif EmmaX.Love >= EmmaX.Obed and EmmaX.Love >= EmmaX.Inbt:
                $ EmmaX.FaceChange("sexy")
                $ EmmaX.Brows = "sad"
                $ EmmaX.Mouth = "smile" 
                ch_e "I don't usually show this side . . ."          
            elif EmmaX.Obed >= EmmaX.Inbt:
                $ EmmaX.FaceChange("normal")
                ch_e "If that's what you're into, [EmmaX.Petname]. . ."            
            else: # Uninhibited 
                $ EmmaX.FaceChange("sad")
                $ EmmaX.Mouth = "smile"             
                ch_e "I do enjoy a good performance . . ."     
    
    
    #Second time+ initial dialog
    elif Approval:                                                                       
            if EmmaX.Forced: 
                $ EmmaX.FaceChange("sad")
                $ EmmaX.Statup("Love", 70, -3, 1)
                $ EmmaX.Statup("Love", 20, -2, 1)
                ch_e "Again? Just you only want to watch?"  
            elif Approval and "masturbation" in EmmaX.RecentActions:
                $ EmmaX.FaceChange("sexy", 1)
                ch_e "I still have some. . . work I could be doing. . ."    
                jump Emma_M_Prep
            elif Approval and "masturbation" in EmmaX.DailyActions:
                $ EmmaX.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["I was that good?",       
                    "Didn't get enough earlier?",
                    "I did enjoy the audience participation. . ."]) 
                ch_e "[Line]"            
            elif EmmaX.Mast < 3:        
                $ EmmaX.FaceChange("sexy", 1)
                $ EmmaX.Brows = "confused"
                ch_e "You enjoyed the show?"       
            else:       
                $ EmmaX.FaceChange("sexy", 1)
                $ EmmaX.ArmPose = 2
                $ Line = renpy.random.choice(["You really do like to watch.",                 
                    "Once more?",                 
                    "You enjoy watching me.",
                    "You want me to take care of myself?"]) 
                ch_e "[Line]"
                $ Line = 0
    #End second time+ initial dialog
    
    #If she's into it. . .  
    if Approval >= 2:                                                                                
            if EmmaX.Forced:
                $ EmmaX.FaceChange("sad")
                $ EmmaX.Statup("Obed", 90, 1)
                $ EmmaX.Statup("Inbt", 60, 1)
                ch_e "Fine. . ." 
            else:
                $ EmmaX.FaceChange("sexy", 1)
                $ EmmaX.Statup("Love", 90, 1)
                $ EmmaX.Statup("Inbt", 50, 3) 
                $ Line = renpy.random.choice(["Ok.",                 
                    "It couldn't hurt having you around. . .",
                    "Very well.", 
                    "Sure, why not?",
                    "[[chuckles]. . . ok."]) 
                ch_e "[Line]"
                $ Line = 0
            $ EmmaX.Statup("Obed", 20, 1)
            $ EmmaX.Statup("Obed", 60, 1)
            $ EmmaX.Statup("Inbt", 70, 2) 
            jump Emma_M_Prep   
            
    #If she's not into it, but maybe. . .    
    else:                                                                                       
        menu:
            ch_e "I don't know that I want to perform."
            "Maybe later?":
                        $ EmmaX.FaceChange("sexy", 1)  
                        if EmmaX.Lust > 70:                        
                            ch_e "I have plans for. . . later, but perhaps you could take part."
                        else:
                            ch_e "I couldn't say."
                        $ EmmaX.Statup("Love", 80, 2)
                        $ EmmaX.Statup("Inbt", 70, 2)               
                        return
            "You look like you could use it. . .":             
                    if Approval:
                        $ EmmaX.FaceChange("sexy")     
                        $ EmmaX.Statup("Obed", 90, 2)
                        $ EmmaX.Statup("Obed", 50, 2)
                        $ EmmaX.Statup("Inbt", 70, 3) 
                        $ EmmaX.Statup("Inbt", 40, 2) 
                        $ Line = renpy.random.choice(["Ok.",                 
                            "It couldn't hurt having you around. . .",
                            "Very well.", 
                            "Sure, why not?",
                            "[[chuckles]. . . ok."]) 
                        ch_e "[Line]"
                        $ Line = 0                   
                        jump Emma_M_Prep
                    
            "Just get at it already.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(EmmaX, 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                    if Approval > 1 or (Approval and EmmaX.Forced):
                        $ EmmaX.FaceChange("sad")
                        $ EmmaX.Statup("Love", 70, -5, 1)
                        $ EmmaX.Statup("Love", 200, -5)                 
                        ch_e "Oh, if it will shut you up."  
                        $ EmmaX.Statup("Obed", 80, 4)
                        $ EmmaX.Statup("Inbt", 80, 1) 
                        $ EmmaX.Statup("Inbt", 60, 3)  
                        $ EmmaX.Forced = 1  
                        jump Emma_M_Prep
                    else:                              
                        $ EmmaX.Statup("Love", 200, -20)     
                        $ EmmaX.RecentActions.append("angry")
                        $ EmmaX.DailyActions.append("angry")
    # end of asking her to do it
    
    #She refused all offers.
    $ EmmaX.ArmPose = 1                
    if EmmaX.Forced:
            $ EmmaX.FaceChange("angry", 1)
            ch_e "That's something I won't do."
            $ EmmaX.Statup("Lust", 90, 5)         
            if EmmaX.Love > 300:
                $ EmmaX.Statup("Love", 70, -2)
            $ EmmaX.Statup("Obed", 50, -2)    
            $ EmmaX.RecentActions.append("angry")
            $ EmmaX.DailyActions.append("angry")   
            $ EmmaX.RecentActions.append("no masturbation")                      
            $ EmmaX.DailyActions.append("no masturbation") 
            return
    elif Taboo:                             # she refuses and this is too public a place for her
            $ EmmaX.FaceChange("angry", 1)          
            $ EmmaX.DailyActions.append("tabno") 
            ch_e "Obviously not in someplace so exposed."     
            $ EmmaX.Statup("Lust", 90, 5)  
            $ EmmaX.Statup("Obed", 50, -3)    
            return                
    elif EmmaX.Mast:
            $ EmmaX.FaceChange("sad") 
            ch_e "I'm sure you can find something else to watch."     
    else:
            $ EmmaX.FaceChange("normal", 1)
            ch_e "I don't think so, [EmmaX.Petname]."  
    $ EmmaX.RecentActions.append("no masturbation")                      
    $ EmmaX.DailyActions.append("no masturbation") 
    $ Tempmod = 0 
    return

label Emma_M_Prep: 
    $ EmmaX.Upskirt = 1    
    $ EmmaX.PantiesDown = 1 
    call Emma_First_Bottomless(1)
    call Set_The_Scene(Dress=0)  
    
    #if she hasn't seen you yet. . .
    if "unseen" in EmmaX.RecentActions:
            $ EmmaX.FaceChange("sexy")
            $ EmmaX.Eyes = "closed"
            $ EmmaX.ArmPose = 2
            "You see [EmmaX.Name] leaning back, masturbating. You don't think she's noticed you yet."
    else:    
            $ EmmaX.FaceChange("sexy")
            $ EmmaX.ArmPose = 2
            "[EmmaX.Name] lays back and starts to toy with herself."
            if not EmmaX.Mast:#First time        
                    if EmmaX.Forced:
                        $ EmmaX.Statup("Love", 90, -20)
                        $ EmmaX.Statup("Obed", 70, 45)
                        $ EmmaX.Statup("Inbt", 80, 35) 
                    else:
                        $ EmmaX.Statup("Love", 90, 15)
                        $ EmmaX.Statup("Obed", 70, 35)
                        $ EmmaX.Statup("Inbt", 80, 40)  
        
    
    $ Trigger = "masturbation"   
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0 
    $ Line = 0
    if Taboo:
        $ EmmaX.DrainWord("tabno")
    $ EmmaX.DrainWord("no masturbation")
    $ EmmaX.RecentActions.append("masturbation")                      
    $ EmmaX.DailyActions.append("masturbation") 
            
label Emma_M_Cycle:  
    if Situation == "join":
        $ renpy.pop_call() 
        $ Situation = 0 
        
    while Round >=0:  
        call Emma_Pos_Reset("masturbation")
        call Shift_Focus(EmmaX) 
        $ EmmaX.LustFace()  
        if "unseen" in EmmaX.RecentActions:  
                $ EmmaX.Eyes = "closed"
        
        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0
            
        if  Player.Focus < 100:                                                    
                    #Player Command menu                                        
                    menu:
                        "Keep Watching.":
                                pass
                                
                        "[EmmaX.Name]. . .[[jump in]" if "unseen" not in EmmaX.RecentActions and EmmaX.Loc == bg_current:                 
                                "[EmmaX.Name] slows what she's doing with a sly grin."
                                ch_e "Enjoying the show?"
                                $ Situation = "join"
                                call Emma_Masturbate               
                        "\"Ahem. . .\"" if "unseen" in EmmaX.RecentActions and EmmaX.Loc == bg_current:  
                                jump Emma_M_Interupted    
                                                   
                        "Start jack'in it." if Trigger2 != "jackin":
                                call Jackin(EmmaX)                   
                        "Stop jack'in it." if Trigger2 == "jackin":
                                $ Trigger2 = 0    
                                            
                        "Slap her ass" if EmmaX.Loc == bg_current:    
                                if "unseen" in EmmaX.RecentActions:
                                        "You smack [EmmaX.Name] firmly on the ass!"
                                        jump Emma_M_Interupted                                          
                                else:
                                        call Slap_Ass(EmmaX)                                        
                                        $ Cnt += 1
                                        $ Round -= 1    
                                        jump Emma_M_Cycle  
                           
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."                
                                    $ Player.FocusX = 0
                                    
                        "Change what I'm doing":
                                menu:
                                    "Offhand action" if EmmaX.Loc == bg_current:
                                            if EmmaX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ EmmaX.Action -= 1
                                            else:
                                                ch_e "I'm actually getting a little tired, perhaps we could wrap this up?"  
                                                           
                                    "Threesome actions (locked)" if not Partner or "unseen" in EmmaX.RecentActions or EmmaX.Loc != bg_current: 
                                        pass
                                    "Threesome actions" if Partner and "unseen" not in EmmaX.RecentActions and EmmaX.Loc == bg_current:   
                                        menu:
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(EmmaX)  
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(EmmaX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_M_Cycle 
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_M_Cycle 
                                            "Never mind":
                                                        jump Emma_M_Cycle 
                                    "Undress [EmmaX.Name]":
                                            if "unseen" in EmmaX.RecentActions:
                                                    ch_p "Oh, yeah, take it off. . ."
                                                    jump Emma_M_Interupted
                                            else:                                        
                                                    call Girl_Undress(EmmaX)   
                                    "Clean up [EmmaX.Name] (locked)" if not EmmaX.Spunk:
                                            pass  
                                    "Clean up [EmmaX.Name]" if EmmaX.Spunk:
                                            if "unseen" in EmmaX.RecentActions:
                                                    ch_p "You've got a little something on you. . ."
                                                    jump Emma_M_Interupted
                                            else:                      
                                                    call Girl_Cleanup(EmmaX,"ask")                                         
                                    "Never mind":
                                            jump Emma_M_Cycle                               
                         
                        "Back to Sex Menu" if MultiAction and EmmaX.Loc == bg_current: 
                                    ch_p "Let's try something else."
                                    call Emma_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Emma_M_Interupted
                        "End Scene" if not MultiAction or EmmaX.Loc != bg_current: 
                                    ch_p "Let's stop for now."
                                    call Emma_Pos_Reset
                                    $ Line = 0
                                    jump Emma_M_Interupted
        #End menu (if Line)
        
        call Shift_Focus(EmmaX)    
        call Sex_Dialog(EmmaX,Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1
    
        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        
        if Player.Focus >= 100 or EmmaX.Lust >= 100:   
                    #If you can cum:
                    if Player.Focus >= 100:
                        if "unseen" not in EmmaX.RecentActions: 
                            #if she knows you're there
                            call Player_Cumming(EmmaX)
                            if "angry" in EmmaX.RecentActions:  
                                call Emma_Pos_Reset
                                return    
                            $ EmmaX.Statup("Lust", 200, 5) 
                            if 100 > EmmaX.Lust >= 70 and EmmaX.OCount < 2:             
                                $ EmmaX.RecentActions.append("unsatisfied")                      
                                $ EmmaX.DailyActions.append("unsatisfied") 
                            $ Line = "came"
                        else: #If she wasn't aware you were there
                            "You grunt and try to hold it in."
                            $ Player.Focus = 95
                            if EmmaX.Loc == bg_current or EmmaX.Loc == "bg desk":
                                    jump Emma_M_Interupted
     
                    #If [EmmaX.Name] can cum
                    if EmmaX.Lust >= 100:                                               
                        call Girl_Cumming(EmmaX)
                        if EmmaX.Loc == bg_current or EmmaX.Loc == "bg desk":
                                jump Emma_M_Interupted
                       
                    if Line == "came": 
                        $ Line = 0
                        if not Player.Semen:
                            "You're emptied out, you should probably take a break."
                            $ Trigger2 = 0 if Trigger2 == "jackin" else Trigger2
                            
                            
                        if "unsatisfied" in EmmaX.RecentActions:#And [EmmaX.Name] is unsatisfied,  
                            "[EmmaX.Name] still seems a bit unsatisfied with the experience."
                            menu:
                                "Let her keep going?"
                                "Yes, keep going for a bit.":
                                    $ Line = "You let her get back into it" 
                                    jump Emma_M_Cycle  
                                "No, I'm done.":
                                    "You ask her to stop."
                                    return 
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)                          
        #End orgasm
        
        if "unseen" in EmmaX.RecentActions:
                if Round == 10:
                    "It's getting a bit late, [EmmaX.Name] will probably be wrapping up soon."  
                elif Round == 5:
                    "She's definitely going to stop soon."
        else: 
                if EmmaX.Loc == bg_current:
                        call Escalation(EmmaX) #sees if she wants to escalate things
        
                if Round == 10:
                    ch_e "I thnk I'll probably take a break soon."  
                    $ EmmaX.Lust += 10
                elif Round == 5:
                    ch_e "Ung, I'm almost finished. . ."     
                    $ EmmaX.Lust += 25   
    
    #Round = 0 loop breaks
    $ EmmaX.FaceChange("bemused", 0)
    $ Line = 0
    if "unseen" not in EmmaX.RecentActions:
        ch_e "That's probably enough of that."
    
label Emma_M_Interupted:
    
    # If she hasn't noticed you're there before cumming
    if "unseen" in EmmaX.RecentActions:                         
                $ EmmaX.FaceChange("surprised", 2)
                "[EmmaX.Name] stops what she's doing with a start, eyes wide."
                call Emma_First_Bottomless(1) 
                $ EmmaX.FaceChange("confused", 1, Eyes="surprised")
                if EmmaX.Loc == "bg desk":
                        $ EmmaX.Loc = bg_current
                        call Display_Girl(EmmaX)
                        "She approaches you."
                
                #If you've been jacking it
                if Trigger2 == "jackin":
                        ch_e "!"
                        ch_e "How long have you been there?!"
                        $ EmmaX.Eyes = "down"
                        menu:
                            ch_e "And I see you've been busy. . . "
                            "A little while, it was an excellent show.":   
                                    $ EmmaX.FaceChange("sexy",1)
                                    $ EmmaX.Statup("Obed", 50, 3)
                                    $ EmmaX.Statup("Obed", 70, 2)
                                    ch_e "Well, obviously. . ."
                                    if EmmaX.Love >= 800 or EmmaX.Obed >= 500 or EmmaX.Inbt >= 500:
                                        $ Tempmod += 10
                                        $ EmmaX.Statup("Lust", 90, 5)
                                    ch_e "and I suppose you bring a lot to the table as well, don't you. . ."  
                                    
                            "I. . . just got here?":
                                    $ EmmaX.FaceChange("angry",1, Eyes="down")                   
                                    $ EmmaX.Statup("Love", 70, 2)
                                    $ EmmaX.Statup("Love", 90, 1)
                                    $ EmmaX.Statup("Obed", 50, 2)
                                    $ EmmaX.Statup("Obed", 70, 2)
                                    "She looks pointedly at your cock,"
                                    $ EmmaX.Eyes = "squint"
                                    ch_e "Long enough to raise your sails?"   
                                    if EmmaX.Love >= 800 or EmmaX.Obed >= 500 or EmmaX.Inbt >= 500:
                                            $ Tempmod += 10
                                            $ EmmaX.Statup("Lust", 90, 5)
                                            $ EmmaX.FaceChange("bemused", 1)
                                            ch_e "I suppose you couldn't help yourself under the circumstances. . ."   
                                    else:
                                            $ Tempmod -= 10
                                            $ EmmaX.Statup("Lust", 200, -5)
                        
                        if "Historia" not in Player.Traits:
                                    call Seen_First_Peen(EmmaX,Partner)
                                    
                #you haven't been jacking it                    
                else:         
                        ch_e "!"
                        ch_e "How long have you been there?!" 
                        menu:
                            extend ""
                            "A little while.":   
                                    $ EmmaX.FaceChange("sexy", 1)
                                    $ EmmaX.Statup("Obed", 50, 3)
                                    $ EmmaX.Statup("Obed", 70, 2)
                                    ch_e "Enjoying the show?"
                            "I just got here.":
                                    $ EmmaX.FaceChange("bemused", 1)
                                    $ EmmaX.Statup("Love", 70, 2)
                                    $ EmmaX.Statup("Love", 90, 1)                    
                                    ch_e "Yes, I'm sure. . ."   
                                    $ EmmaX.Statup("Obed", 50, 2)
                                    $ EmmaX.Statup("Obed", 70, 2)    
                                
                $ EmmaX.DrainWord("unseen",1,0) #She sees you, so remove unseens
                $ EmmaX.Mast += 1
                if "classcaught" not in EmmaX.History or "Historia" in Player.Traits:
                    # this activates if it's the first time in class
                    return
                if Round <= 10:
                    ch_e "Unfortunately it's getting rather late."
                    return
                $ Situation = "join"        
                call Emma_Masturbate
                "error: report this if you see it."
                return #should be redundant
    #End Unseen
    
    #else, if She's seen you already    
    $ EmmaX.Action -= 1
    $ EmmaX.Mast += 1    
    call Checkout
    if Situation == "shift":        
        $ Situation = 0
        return
    $ Situation = 0
        
    if Partner == "Kitty":
        call Partner_Like(EmmaX,4,2)
    else:
        call Partner_Like(EmmaX,3,2)
    
    if EmmaX.Loc != bg_current and EmmaX.Loc != "bg desk":
            return
        
    if Round <= 10:
            ch_e "Allow me to collect myself. . ."
            return
    $ EmmaX.FaceChange("sexy", 1)
    if EmmaX.Lust < 20:
            ch_e "I suppose that took care of my needs, at least."
    else:
            ch_e "Yes?"
    menu:
        extend ""
        "Well, I have something you could take care of. . ." if Player.Semen and EmmaX.Action and MultiAction:
                $ Situation = "shift"
                return   
        "You could just keep going. . ." if Player.Semen:
                $ EmmaX.FaceChange("sly")
                if EmmaX.Action and Round >= 10:
                    ch_e "I suppose. . ."
                    jump Emma_M_Cycle
                else:
                    ch_e "Gimme a minute, I need to collect myself here. . ."
        "I'm good here. [[Stop]":  
                if EmmaX.Love < 800 and EmmaX.Inbt < 500 and EmmaX.Obed < 500:
                    $ EmmaX.OutfitChange()
                $ EmmaX.FaceChange("normal")
                $ EmmaX.Brows = "confused"
                ch_e "Well. . . yes. . ."
                $ EmmaX.Brows = "normal" 
        "You should probably stop for now." if EmmaX.Lust > 30:
                $ EmmaX.FaceChange("angry")
                ch_e "I . . . yes . ."
    if Trigger2 == "jackin":
        $ Trigger2 = 0
    return
    
## end EmmaX.Masturbating ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Start [EmmaX.Name] Sex pose //////////////////////////////////////////////////////////////////////////////////
# EmmaX.Sex_P //////////////////////////////////////////////////////////////////////

label Emma_Sex_P:  
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(EmmaX)
    if EmmaX.Sex >= 7: # She loves it
        $ Tempmod += 15
    elif EmmaX.Sex >= 3: #You've done it before several times
        $ Tempmod += 12
    elif EmmaX.Sex: #You've done it before
        $ Tempmod += 10    
        
    if EmmaX.Addict >= 75 and (EmmaX.CreamP + EmmaX.CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 20
    elif EmmaX.Addict >= 75:
        $ Tempmod += 15
        
    if EmmaX.Lust > 85:
        $ Tempmod += 10
    elif EmmaX.Lust > 75: #She's really horny
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 10 
    if "exhibitionist" in EmmaX.Traits:    
        $ Tempmod += (4*Taboo)      
    if "dating" in EmmaX.Traits or "sex friend" in EmmaX.Petnames:
        $ Tempmod += 10
    elif "ex" in EmmaX.Traits:
        $ Tempmod -= 40
    if EmmaX.ForcedCount and not EmmaX.Forced:
        $ Tempmod -= 5 * EmmaX.ForcedCount
    
    
        
    if Taboo and "tabno" in EmmaX.DailyActions:        
        $ Tempmod -= 10 
        
    if "no sex" in EmmaX.DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no sex" in EmmaX.RecentActions else 0                  
             
        
    $ Approval = ApprovalCheck(EmmaX, 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)
        
    if Situation == "auto":   
                call Emma_Sex_Launch("L")   
                if EmmaX.PantsNum() == 5:
                    "You roll back, pulling [EmmaX.Name] on top of you, sliding her skirt up as you go."
                    $ EmmaX.Upskirt = 1                
                elif EmmaX.PantsNum() >= 6:
                    "You roll back, pulling [EmmaX.Name] on top of you, sliding her [EmmaX.Legs] down as you do."    
                    $ EmmaX.Legs = 0    
                else:
                    "You roll back, pulling [EmmaX.Name] on top of you."
                $ EmmaX.SeenPanties = 1
                "You rub the tip of your cock against her moist slit."        
                $ EmmaX.FaceChange("surprised", 1)
                
                if (EmmaX.Sex and Approval) or (Approval > 1):
                    #this is not the first time you've had sex, or she's into it         
                    "[EmmaX.Name] is briefly startled, but melts into a sly smile."
                    $ EmmaX.FaceChange("sly")
                    $ EmmaX.Statup("Obed", 70, 3)
                    $ EmmaX.Statup("Inbt", 50, 3) 
                    $ EmmaX.Statup("Inbt", 70, 1) 
                    ch_e "Mmm, if you insist, [EmmaX.Petname]."            
                    jump Emma_SexPrep         
                else:                                                                                                            
                    #she's questioning it
                    $ EmmaX.Brows = "angry"                
                    menu:
                        ch_e "Do you really think you can handle that?" 
                        "Sorry, sorry! Never mind.":
                            if Approval:     
                                    $ EmmaX.FaceChange("sexy", 1)
                                    $ EmmaX.Statup("Obed", 70, 3)
                                    $ EmmaX.Statup("Inbt", 50, 3) 
                                    $ EmmaX.Statup("Inbt", 70, 1) 
                                    ch_e "I am willing to give it a try if you are. . ."
                                    jump Emma_SexPrep
                            else:
                                    "You pull back before you really get it in."                    
                                    $ EmmaX.FaceChange("bemused", 1)
                                    if EmmaX.Sex:
                                        ch_e "Perhaps ask first, [EmmaX.Petname]." 
                                    else:
                                        ch_e "Perhaps some other time, when you ask nicely."
                        "Just fucking.":                    
                            $ EmmaX.Statup("Love", 80, -10, 1)  
                            $ EmmaX.Statup("Love", 200, -10)
                            "You press inside some more."                              
                            $ EmmaX.Statup("Obed", 70, 3)
                            $ EmmaX.Statup("Inbt", 50, 3) 
                            if not ApprovalCheck(EmmaX, 700, "O", TabM=1):   #Checks if Obed is 700+                          
                                $ EmmaX.FaceChange("angry")
                                "[EmmaX.Name] shoves you away and backhands you in the face."
                                ch_e "Impertinent!"
                                ch_e "do not test my patience with you."                                                  
                                $ EmmaX.Statup("Love", 50, -10, 1)                        
                                $ EmmaX.Statup("Obed", 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                call Emma_Sex_Reset
                                $ EmmaX.RecentActions.append("angry")
                                $ EmmaX.DailyActions.append("angry")                    
                            else:
                                $ EmmaX.FaceChange("sad")
                                "[EmmaX.Name] doesn't seem to be into this, you're lucky she's so obedient."                        
                                jump Emma_SexPrep
                return   
    #End Auto
    
   
    if not EmmaX.Sex and "no sex" not in EmmaX.RecentActions:                           
            #first time    
            $ EmmaX.FaceChange("surprised", 1)
            $ EmmaX.Mouth = "kiss"
            ch_e "Hmm, are you sure you're really prepared for this? . . "    
            if EmmaX.Forced:
                $ EmmaX.FaceChange("sad")
                ch_e "Are you sure this is how you'd like to use your. . . influence?"
            
            
    if not EmmaX.Sex and Approval:                                                  
            #First time dialog        
            if EmmaX.Forced: 
                $ EmmaX.FaceChange("sad")
                $ EmmaX.Statup("Love", 70, -30, 1)
                $ EmmaX.Statup("Love", 20, -20, 1)
            elif EmmaX.Love >= (EmmaX.Obed + EmmaX.Inbt):
                $ EmmaX.FaceChange("sexy")
                $ EmmaX.Brows = "sad"
                $ EmmaX.Mouth = "smile" 
                ch_e "I wouldn't want you to get hurt. . ."            
            elif EmmaX.Obed >= EmmaX.Inbt:
                $ EmmaX.FaceChange("normal")
                ch_e "If you insist, [EmmaX.Petname]. . ."            
            elif EmmaX.Addict >= 50:
                $ EmmaX.FaceChange("manic", 1)
                ch_e "I was wondering how it would feel with you. . ."
            else: # Uninhibited 
                $ EmmaX.FaceChange("sad")
                $ EmmaX.Mouth = "smile"             
                ch_e "I was hoping you'd ask. . ."   
            #End first time dialog
            
    elif Approval:                                                                      
            #Second time+ dialog        
            $ EmmaX.FaceChange("sexy", 1)
            if EmmaX.Forced: 
                $ EmmaX.FaceChange("sad")
                $ EmmaX.Statup("Love", 70, -3, 1)
                $ EmmaX.Statup("Love", 20, -2, 1)
                ch_e "Again? You're really wearing out your welcome." 
            elif not Taboo and "tabno" in EmmaX.DailyActions:        
                ch_e "I suppose this is more private."        
            elif "sex" in EmmaX.RecentActions:
                ch_e "Again? [EmmaX.Petname], you're insatiable!" 
                jump Emma_SexPrep
            elif "sex" in EmmaX.DailyActions:
                $ Line = renpy.random.choice(["Back again?",                 
                    "You'd like another round?",                 
                    "I suppose I am irresistible. . .", 
                    "Didn't get enough earlier?",
                    "You're wearing me out, " + EmmaX.Petname + "."]) 
                ch_e "[Line]"
            elif EmmaX.Sex < 3:        
                $ EmmaX.Brows = "confused"
                $ EmmaX.Mouth = "kiss"
                ch_e "Oh? Another round?"      
            else:       
                $ Line = renpy.random.choice(["Oh, you want some of this?",                 
                    "You'd like another round?",                 
                    "I suppose I am irresistible. . .", 
                    "Do you intend to make me melt?",
                    "You want me to ride you?"]) 
                ch_e "[Line]"
            $ Line = 0
            #end Second time+ dialog
            
    if Approval >= 2:                                                                  
            #She's into it. . .               
            if EmmaX.Forced:
                $ EmmaX.FaceChange("sad")
                $ EmmaX.Statup("Obed", 90, 1)
                $ EmmaX.Statup("Inbt", 60, 1)
                ch_e "Oh, fine, if it will shut you up."  
            elif "no sex" in EmmaX.DailyActions:               
                ch_e "Very well, you've convinced me. . ."
            else:
                $ EmmaX.FaceChange("sexy", 1)
                $ EmmaX.Statup("Love", 90, 1)
                $ EmmaX.Statup("Inbt", 50, 3) 
                $ Line = renpy.random.choice(["Well. . . fine, I accept.",                 
                    "Sure!", 
                    "We could, I suppose.",
                    "Hmmm, yes.",
                    "How could I refuse?"]) 
                ch_e "[Line]"
                $ Line = 0
            $ EmmaX.Statup("Obed", 20, 1)
            $ EmmaX.Statup("Obed", 60, 1)
            $ EmmaX.Statup("Inbt", 70, 2) 
            jump Emma_SexPrep   
    
    else:                                                                               
            #She's not into it, but maybe. . .    
            $ EmmaX.FaceChange("angry")       
            if "no sex" in EmmaX.RecentActions:  
                ch_e "I'm afraid that \"no\" is my final answer, [EmmaX.Petname]."
            elif Taboo and "tabno" in EmmaX.DailyActions and "no sex" in EmmaX.DailyActions:  
                ch_e "I already told you. . .not in such an exposed location." 
            elif "no sex" in EmmaX.DailyActions:       
                ch_e "I believe I just told you \"no,\" [EmmaX.Petname]."
            elif Taboo and "tabno" in EmmaX.DailyActions:  
                ch_e "I already told you this is too public!"     
            elif not EmmaX.Sex:
                $ EmmaX.FaceChange("bemused")
                ch_e "I really doubt you understand what you're in for. . ."
            else:
                $ EmmaX.FaceChange("bemused")
                ch_e "Perhaps another time would be better? . ."
            menu:
                extend ""
                "Sorry, never mind." if "no sex" in EmmaX.DailyActions:
                        $ EmmaX.FaceChange("bemused")
                        ch_e "I can appreciate your. . . drive."
                        return
                "Maybe later?" if "no sex" not in EmmaX.DailyActions:
                        $ EmmaX.FaceChange("sexy")  
                        ch_e "Oh, most certainly. . ."
                        $ EmmaX.Statup("Love", 80, 2)
                        $ EmmaX.Statup("Inbt", 70, 2)   
                        if Taboo:                    
                            $ EmmaX.RecentActions.append("tabno")                      
                            $ EmmaX.DailyActions.append("tabno") 
                        $ EmmaX.RecentActions.append("no sex")                      
                        $ EmmaX.DailyActions.append("no sex")            
                        return
                "I think you'd enjoy it as much as I would. . .":             
                        if Approval:
                            $ EmmaX.FaceChange("sexy")     
                            $ EmmaX.Statup("Obed", 90, 2)
                            $ EmmaX.Statup("Obed", 50, 2)
                            $ EmmaX.Statup("Inbt", 70, 3) 
                            $ EmmaX.Statup("Inbt", 40, 2) 
                            $ Line = renpy.random.choice(["I can't exactly argue with that. . .",     
                                "I suppose. . .", 
                                "You raise a good point. . ."]) 
                            ch_e "[Line]"
                            $ Line = 0                   
                            jump Emma_SexPrep       
                "Just deal with it.":                                               # Pressured into it
                        $ Approval = ApprovalCheck(EmmaX, 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
                        if Approval > 1 or (Approval and EmmaX.Forced):
                            $ EmmaX.FaceChange("sad")
                            $ EmmaX.Statup("Love", 70, -5, 1)
                            $ EmmaX.Statup("Love", 200, -5)                 
                            ch_e "Fine, if it'll shut you up."  
                            $ EmmaX.Statup("Obed", 80, 4)
                            $ EmmaX.Statup("Inbt", 80, 1) 
                            $ EmmaX.Statup("Inbt", 60, 3)  
                            $ EmmaX.Forced = 1  
                            jump Emma_SexPrep
                        else:                          
                            $ EmmaX.Statup("Love", 200, -20)   
                            $ EmmaX.RecentActions.append("angry")
                            $ EmmaX.DailyActions.append("angry")  
                #end menu
    #end Approval check
    
    #She refused all offers.
    $ EmmaX.ArmPose = 1  
    if "no sex" in EmmaX.DailyActions:
        ch_e "Don't question me again." 
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")   
    elif EmmaX.Forced:
        $ EmmaX.FaceChange("angry", 1)
        ch_e "Don't overestimate your leverage here."
        $ EmmaX.Statup("Lust", 200, 5) 
        if EmmaX.Love > 300:   
                $ EmmaX.Statup("Love", 70, -2) 
        $ EmmaX.Statup("Obed", 50, -2)     
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        $ EmmaX.FaceChange("angry", 1)
        $ EmmaX.RecentActions.append("tabno")                      
        $ EmmaX.DailyActions.append("tabno") 
        ch_e "How can you imagine this would be an appropriate location?"      
        $ EmmaX.Statup("Lust", 200, 5)  
        $ EmmaX.Statup("Obed", 50, -3)
    elif EmmaX.Sex:
        $ EmmaX.FaceChange("sad") 
        ch_e "I'm sure you can figure out how to take care of that yourself."       
    else:
        $ EmmaX.FaceChange("normal", 1)
        ch_e "I'm afraid not."     
    $ EmmaX.RecentActions.append("no sex")                      
    $ EmmaX.DailyActions.append("no sex") 
    $ Tempmod = 0    
    return

label Emma_SexPrep:
    call Seen_First_Peen(EmmaX,Partner,React=Situation)
    call Emma_Sex_Launch("hotdog")
            
    if Situation == EmmaX:                                                                 
            #Emma auto-starts   
            $ Situation = 0
            if EmmaX.PantsNum() == 5:
                "[EmmaX.Name] pushes you back and climbs on top of you, sliding her skirt up as she does so."
                $ EmmaX.Upskirt = 1                
            elif EmmaX.PantsNum() >= 6:
                "[EmmaX.Name] pushes you down and climbs on top of you, sliding her [EmmaX.Legs] down as she does so." 
                $ EmmaX.Upskirt = 1
            else:
                "[EmmaX.Name] pushes you back and climbs on top of you."
            $ EmmaX.SeenPanties = 1
            "She slides the tip along her pussy and seems to want you to insert it."
            menu:
                "What do you do?"
                "Go with it.":                    
                    $ EmmaX.Statup("Inbt", 80, 3) 
                    $ EmmaX.Statup("Inbt", 50, 2)
                    "[EmmaX.Name] slides it in."
                "Praise her.":       
                    $ EmmaX.FaceChange("sexy", 1)                    
                    $ EmmaX.Statup("Inbt", 80, 3) 
                    ch_p "Oh yeah, [EmmaX.Pet], let's do this."
                    $ EmmaX.NameCheck() #checks reaction to petname
                    "[EmmaX.Name] slides it in."
                    $ EmmaX.Statup("Love", 85, 1)
                    $ EmmaX.Statup("Obed", 90, 1)
                    $ EmmaX.Statup("Obed", 50, 2)
                "Ask her to stop.":
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
            $ EmmaX.PantiesDown = 1  
            call Emma_First_Bottomless(1)
            
    elif Situation != "auto":
        call Bottoms_Off(EmmaX)       
        
        
        if (EmmaX.Panties and not EmmaX.PantiesDown) or (EmmaX.Legs and not EmmaX.Upskirt) or EmmaX.HoseNum() >= 6: #If she refuses to take off her pants but agreed to anal
            ch_e "I suppose we can't do much with all this on."
            
            if (EmmaX.Panties and not EmmaX.PantiesDown) and (EmmaX.PantsNum() > 6 and not EmmaX.Upskirt):
                "She quickly drops her pants and her [EmmaX.Panties]."
            elif (EmmaX.Panties and not EmmaX.PantiesDown) and (EmmaX.PantsNum() == 6 and not EmmaX.Upskirt):
                "She quickly drops her shorts and her [EmmaX.Panties]."
            elif EmmaX.PantsNum() > 6 and not EmmaX.Upskirt:
                "She tugs her pants down, exposing her bare pussy."
            elif EmmaX.PantsNum() == 6 and not EmmaX.Upskirt:
                "She tugs her shorts down, exposing her bare pussy."
            elif EmmaX.HoseNum() >= 6 and (EmmaX.Panties and not EmmaX.PantiesDown):
                "She tugs her [EmmaX.Hose] and [EmmaX.Panties] off."
                $ EmmaX.Hose = 0
            elif EmmaX.HoseNum() >= 6:
                "She tugs her [EmmaX.Hose] off and drops them to the ground."
                $ EmmaX.Hose = 0
            elif (EmmaX.Panties and not EmmaX.PantiesDown):
                "She tugs her [EmmaX.Panties] off and drops them to the ground."  
            
        $ EmmaX.Upskirt = 1
        $ EmmaX.PantiesDown = 1       
        $ EmmaX.SeenPanties = 1
        call Emma_First_Bottomless
        
        if Taboo: # [EmmaX.Name] gets started. . .
            "[EmmaX.Name] glances around to see if anyone notices what she's doing."
            if "cockout" in Player.RecentActions:
                "Then she pushes you back and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and climbs on top of you."
                "She slowly presses against your rigid member."
            $ EmmaX.Inbt += int(Taboo/10)  
            $ EmmaX.Lust += int(Taboo/5)
        else:    
            if "cockout" in Player.RecentActions:
                "[EmmaX.Name] pushes you back and slowly presses against your rigid member."
            else:
                "[EmmaX.Name] pulls down your pants and climbs on top of you."
                "She slowly presses against your rigid member."
        "She leans back a bit and your cock slides in."
                            
    else:  #if Situation == "auto"         
        if (EmmaX.PantsNum() > 6 and not EmmaX.Upskirt) and (EmmaX.Panties and not EmmaX.PantiesDown):
            "You quickly pull down her pants and her [EmmaX.Panties] and press against her slit."
        elif (EmmaX.Panties and not EmmaX.PantiesDown):
            "You quickly pull down her [EmmaX.Panties] and press against her slit."  
        $ EmmaX.Upskirt = 1
        $ EmmaX.PantiesDown = 1       
        $ EmmaX.SeenPanties = 1
        call Emma_First_Bottomless(1)
    
    if Player.Focus >= 50:
            ch_e "My word [EmmaX.Petname], your member is hard enough to crack diamond...and I should know."
    if not EmmaX.Sex:        
        if EmmaX.Forced:
            $ EmmaX.Statup("Love", 90, -150)
            $ EmmaX.Statup("Obed", 70, 60)
            $ EmmaX.Statup("Inbt", 80, 50) 
        else:
            $ EmmaX.Statup("Love", 90, 30)
            $ EmmaX.Statup("Obed", 70, 30)
            $ EmmaX.Statup("Inbt", 80, 60) 
    
    if Situation:   
        $ renpy.pop_call() 
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ Player.Cock = "in"
    $ Trigger = "sex"
    $ Speed = 1
    if Taboo:
        $ EmmaX.DrainWord("tabno")
    $ EmmaX.DrainWord("no sex")
    $ EmmaX.RecentActions.append("sex")                      
    $ EmmaX.DailyActions.append("sex")     

label Emma_Sex_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus(EmmaX)
        call Emma_Sex_Launch("sex") 
        $ Speed = 2 if Speed >= 4 else Speed
        $ EmmaX.LustFace()        
        $ Player.Cock = "in"
        $ Trigger = "sex"
        $ EmmaX.Upskirt = 1
        $ EmmaX.PantiesDown = 1  
        
        if  Player.Focus < 100:                                                    
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
                                    call Slap_Ass(EmmaX)  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Emma_Sex_Cycle  
                                    
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
                                                ch_e "I'm getting a bit tired here, could we take a break?" 
                                                
                                    "Shift primary action":
                                            if EmmaX.Action and MultiAction:
                                                    menu:
                                                        "How about anal?":
                                                                $ Situation = "shift"
                                                                call Emma_SexAfter
                                                                call Emma_Sex_A
                                                        "Just stick it in her ass [[without asking].":
                                                                $ Situation = "auto"
                                                                call Emma_SexAfter
                                                                call Emma_Sex_A
                                                        "Pull back to hotdog her.":
                                                                $ Situation = "pullback"
                                                                call Emma_SexAfter
                                                                call Emma_Sex_H
                                                        "Never Mind":
                                                                jump Emma_Sex_Cycle
                                            else:
                                                ch_e "I'm getting a bit tired here, could we take a break?" 
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
                                                        jump Emma_Sex_Cycle 
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_Sex_Cycle 
                                            "Never mind":
                                                        jump Emma_Sex_Cycle 
                                    "Undress [EmmaX.Name]":
                                            call Girl_Undress(EmmaX)   
                                    "Clean up [EmmaX.Name] (locked)" if not EmmaX.Spunk:
                                            pass  
                                    "Clean up [EmmaX.Name]" if EmmaX.Spunk:
                                            call Girl_Cleanup(EmmaX,"ask")                                         
                                    "Never mind":
                                            jump Emma_Sex_Cycle                                    
                                                        
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Emma_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Emma_SexAfter
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Emma_Sex_Reset
                                    $ Line = 0
                                    jump Emma_SexAfter
        #End menu (if Line)              
        
        call Shift_Focus(EmmaX)    
        call Sex_Dialog(EmmaX,Partner)
        
        $ Cnt += 1
        $ Round -= 1     
        
        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or EmmaX.Lust >= 100:   
                    #If either of you could cum    
                    if Player.Focus >= 100:
                            #If you can cum:                                                
                            call Player_Cumming(EmmaX)
                            if "angry" in EmmaX.RecentActions:  
                                call Emma_Sex_Reset
                                return    
                            $ EmmaX.Statup("Lust", 200, 5) 
                            if 100 > EmmaX.Lust >= 70 and EmmaX.OCount < 2:             
                                    $ EmmaX.RecentActions.append("unsatisfied")                      
                                    $ EmmaX.DailyActions.append("unsatisfied") 
                            
                            if Player.Focus > 80:
                                jump Emma_SexAfter 
                            $ Line = "came"

                    if EmmaX.Lust >= 100:         
                            #If you're still going at it and [EmmaX.Name] can cum
                            call Girl_Cumming(EmmaX)
                            if Situation == "shift" or "angry" in EmmaX.RecentActions:
                                jump Emma_SexAfter
                       
                    if Line == "came": #ex Player.Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Emma_SexAfter
                            elif "unsatisfied" in EmmaX.RecentActions:
                                #And [EmmaX.Name] is unsatisfied,  
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ Line = "You get back into it" 
                                        jump Emma_Sex_Cycle  
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Emma_SexAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Emma_SexAfter   
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)            
        #End orgasm
        
        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0
        
        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif Cnt == (5 + EmmaX.Sex):
                    $ EmmaX.Brows = "confused"
                    ch_e "So are we getting close?"   
        elif Cnt == (10 + EmmaX.Sex):
                    $ EmmaX.Brows = "angry"        
                    ch_e "I'm . . .getting . . a bit. . . tired. . . here. . ."
                    menu:
                        ch_e "Could we. . . do something. . . else?"
                        "How about a BJ?" if EmmaX.Action and MultiAction:
                                $ Situation = "shift"
                                call Emma_SexAfter
                                call Emma_Blowjob       
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."             
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ Cnt += 1
                                jump Emma_Sex_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Emma_Sex_Reset
                                $ Situation = "shift"
                                jump Emma_SexAfter
                        "No, get back down there.":                                
                                if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):                        
                                    $ EmmaX.Statup("Love", 200, -5)
                                    $ EmmaX.Statup("Obed", 50, 3)                    
                                    $ EmmaX.Statup("Obed", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    $ EmmaX.FaceChange("angry", 1)   
                                    call Emma_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_e "No, I think not."
                                    $ EmmaX.Statup("Love", 50, -3, 1)
                                    $ EmmaX.Statup("Love", 80, -4, 1)
                                    $ EmmaX.Statup("Obed", 30, -1, 1)                    
                                    $ EmmaX.Statup("Obed", 50, -1, 1)  
                                    $ EmmaX.RecentActions.append("angry")
                                    $ EmmaX.DailyActions.append("angry")   
                                    jump Emma_SexAfter
        #End Count check
   
        call Escalation(EmmaX) #sees if she wants to escalate things
        
        if Round == 10:
            ch_e "You might want to think about your endgame here. . ."  
        elif Round == 5:
            ch_e "We'll need a break soon."        
    
    #Round = 0 loop breaks
    $ EmmaX.FaceChange("bemused", 0)
    $ Line = 0
    ch_e "Ok, [EmmaX.Petname], that's enough of that for now."
    
label Emma_SexAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ Player.Sprite = 0
        $ Player.Cock = "out"
        call Emma_Sex_Reset
        
    $ EmmaX.FaceChange("sexy") 
    
    $ EmmaX.Sex += 1  
    $ EmmaX.Action -=1
    $ EmmaX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ EmmaX.Addictionrate += 1        
    $ EmmaX.Statup("Inbt", 30, 2) 
    $ EmmaX.Statup("Inbt", 70, 1) 
        
    call Partner_Like(EmmaX,3,2)
    
    if "Emma Sex Addict" in Achievements:
            pass 
            
    elif EmmaX.Sex >= 10:
        $ EmmaX.SEXP += 5
        $ Achievements.append("Emma Sex Addict")
        if not Situation:
            $ EmmaX.FaceChange("smile", 1)
            ch_e "I seem to fit you like a glove. . ."               
    elif EmmaX.Sex == 1:            
            $EmmaX.SEXP += 20        
            if not Situation: 
                if EmmaX.Love >= 500 and "unsatisfied" not in EmmaX.RecentActions:
                    ch_e "I assume I rocked your entire world."
                elif EmmaX.Obed <= 500 and Player.Focus <= 20:
                    $ EmmaX.Mouth = "sad"
                    ch_e "I hope you enjoyed that."
    elif EmmaX.Sex == 5:
            ch_e "We really should have done this sooner."
            ch_e "I can't imagine why I waited so long."
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in EmmaX.RecentActions:
            $ EmmaX.FaceChange("angry")
            $ EmmaX.Eyes = "side"
            ch_e "Could you have perhaps been more attentive? . ."
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_e "Did you[EmmaX.like]want to try something else?"
    call Checkout
    return   

# End emma sex //////////////////////////////////////////////////////////////////////////////////


# [EmmaX.Name] anal //////////////////////////////////////////////////////////////////////

label Emma_Sex_A:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(EmmaX)
    if EmmaX.Anal >= 7: # She loves it
        $ Tempmod += 20   
    elif EmmaX.Anal >= 3: #You've done it before several times
        $ Tempmod += 17
    elif EmmaX.Anal: #You've done it before
        $ Tempmod += 15 
        
    if EmmaX.Addict >= 75 and (EmmaX.CreamP + EmmaX.CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 25
    elif EmmaX.Addict >= 75: 
        $ Tempmod += 15
    
    if EmmaX.Lust > 85:
        $ Tempmod += 10
    elif EmmaX.Lust > 75: #She's really horny
        $ Tempmod += 5
        
    $ Tempmod += 10  # she starts out loose    
        
    if Situation == "shift":
        $ Tempmod += 10    
    if "exhibitionist" in EmmaX.Traits:
        $ Tempmod += (5*Taboo) 
        
    if "dating" in EmmaX.Traits or "sex friend" in EmmaX.Petnames:
        $ Tempmod += 10      
    elif "ex" in EmmaX.Traits:
        $ Tempmod -= 40  
    if EmmaX.ForcedCount and not EmmaX.Forced:
        $ Tempmod -= 5 * EmmaX.ForcedCount
        
    if Taboo and "tabno" in EmmaX.DailyActions:        
        $ Tempmod -= 10 
    if "no anal" in EmmaX.DailyActions:               
        $ Tempmod -= 5         
        $ Tempmod -= 10 if "no anal" in EmmaX.RecentActions else 0  
            
    $ Approval = ApprovalCheck(EmmaX, 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)
    
    if Situation == "auto":   
            call Emma_Sex_Launch("L")   
            if EmmaX.PantsNum() == 5:
                "You roll back, pulling [EmmaX.Name] on top of you, sliding her skirt up as you go."
                $ EmmaX.Upskirt = 1                
            elif EmmaX.PantsNum() >= 6:
                "You roll back, pulling [EmmaX.Name] on top of you, sliding her [EmmaX.Legs] down as you do."    
                $ EmmaX.Legs = 0    
            else:
                "You roll back, pulling [EmmaX.Name] on top of you."
            $ EmmaX.SeenPanties = 1
            "You press the tip of your cock against her tight rim."        
            $ EmmaX.FaceChange("surprised", 1)
            
            if (EmmaX.Anal and Approval) or (Approval > 1):                                                                      
                #this is not the first time you've had sex, or she's into it    
                $ EmmaX.Statup("Obed", 70, 3)
                $ EmmaX.Statup("Inbt", 50, 3) 
                $ EmmaX.Statup("Inbt", 70, 1) 
                "[EmmaX.Name] is briefly startled, but melts into a sly smile."
                ch_e "Oooh, naughty boy. . ."          
                jump Emma_AnalPrep         
            else:                                                                                                            
                #she's questioning it
                $ EmmaX.Brows = "angry"                
                menu:
                    ch_e "Oh? What exactly are you doing back there?" 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            $ EmmaX.FaceChange("sexy", 1)
                            $ EmmaX.Statup("Obed", 70, 3)
                            $ EmmaX.Statup("Inbt", 50, 3) 
                            $ EmmaX.Statup("Inbt", 70, 1) 
                            ch_e "Well, so long as you know what you're doing . ."
                            ch_e "I didn't say I was opposed. . ."
                            jump Emma_AnalPrep
                        "You pull back before you really get it in."                    
                        $ EmmaX.FaceChange("bemused", 1)
                        
                        if EmmaX.Anal:
                            ch_e "I do appreciate a little warning. . ." 
                        else:
                            ch_e "Perhaps we could work up to that. . ."
                    "Just fucking.":                    
                        $ EmmaX.Statup("Love", 80, -10, 1)  
                        $ EmmaX.Statup("Love", 200, -8)
                        "You press into her."                              
                        $ EmmaX.Statup("Obed", 70, 3)
                        $ EmmaX.Statup("Inbt", 50, 3) 
                        if not ApprovalCheck(EmmaX, 700, "O", TabM=1):                        
                            $ EmmaX.FaceChange("angry")
                            "[EmmaX.Name] shoves you away and backhands you in the face."
                            ch_e "Impertinent!"
                            ch_e "You need to ask a lady first."                                                  
                            $ EmmaX.Statup("Love", 50, -10, 1)                        
                            $ EmmaX.Statup("Obed", 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            call Emma_Sex_Reset
                            $ EmmaX.RecentActions.append("angry")
                            $ EmmaX.DailyActions.append("angry")                        
                        else:
                            $ EmmaX.FaceChange("sad")
                            "[EmmaX.Name] doesn't seem to be into this, you're lucky she's so obedient."                        
                            jump Emma_AnalPrep
            return  
            #end "auto" 
    
   
    if not EmmaX.Anal and "no anal" not in EmmaX.RecentActions:                                                               
            #first time    
            $ EmmaX.FaceChange("surprised", 1)
            $ EmmaX.Mouth = "kiss"
            ch_e "Oooh, naughty boy. Anal?"
      
            if EmmaX.Forced:
                $ EmmaX.FaceChange("sad")
                ch_e "Anal? That's your goto?"
        
    if "anal" in EmmaX.RecentActions:
            $ EmmaX.FaceChange("sexy", 1)
            ch_e "Alright."
            jump Emma_AnalPrep
        
    
    if not EmmaX.Anal and Approval:                                                 
            #First time dialog        
            if EmmaX.Forced: 
                $ EmmaX.FaceChange("sad")
                $ EmmaX.Statup("Love", 70, -3, 1)
                $ EmmaX.Statup("Love", 20, -2, 1)
            elif EmmaX.Love >= (EmmaX.Obed + EmmaX.Inbt):
                $ EmmaX.FaceChange("sexy")
                $ EmmaX.Brows = "sad"
                $ EmmaX.Mouth = "smile" 
                ch_e "I was wondering when you'd ask. . ."           
            elif EmmaX.Obed >= EmmaX.Inbt:
                $ EmmaX.FaceChange("normal")
                ch_e "I expected we'd get here at some point. . ."
            elif EmmaX.Addict >= 50:
                $ EmmaX.FaceChange("manic", 1)
                ch_e "Hmm, that would be an interesting experience. . ."
            else: # Uninhibited 
                $ EmmaX.FaceChange("sad")
                $ EmmaX.Mouth = "smile"             
                ch_e "I was getting tired of waiting. . ."  
    
    elif Approval:                                                                       
            #Second time+ dialog
            if EmmaX.Forced: 
                $ EmmaX.FaceChange("sad")
                $ EmmaX.Statup("Love", 70, -3, 1)
                $ EmmaX.Statup("Love", 20, -2, 1)
                ch_e "You don't hold back. . ."
            elif not Taboo and "tabno" in EmmaX.DailyActions:        
                ch_e "I suppose this is secluded enough. . ."   
            elif "anal" in EmmaX.DailyActions and not EmmaX.Loose:
                pass      
            elif "anal" in EmmaX.RecentActions:
                ch_e "I am warmed up. . ."
                jump Emma_AnalPrep
            elif "anal" in EmmaX.DailyActions:
                $ EmmaX.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Back again so soon?",                 
                    "So you'd like another round?",                 
                    "I'm still a little sore from earlier.", 
                    "Didn't get enough earlier?",
                    "You're wearing me out, " + EmmaX.Petname + "."]) 
                ch_e "[Line]"    
            else:       
                $ EmmaX.FaceChange("sexy", 1)
                $ EmmaX.ArmPose = 2
                $ Line = renpy.random.choice(["Oooh, you want some of this?",                 
                    "So you'd like another round?",                 
                    "I knew you enjoyed it. . .", 
                    "Do you intend to make me melt?",
                    "You want me to ride you?"]) 
                ch_e "[Line]"
            $ Line = 0
            
    if Approval >= 2:                                                                   
            #She's into it. . .               
            if EmmaX.Forced:
                $ EmmaX.FaceChange("sad")
                $ EmmaX.Statup("Obed", 90, 1)
                $ EmmaX.Statup("Inbt", 60, 1)
                ch_e "Oh very well."   
            elif "no anal" in EmmaX.DailyActions:               
                ch_e "After some consideration. . ."
                ch_e "It might be entertaining."
            else:
                $ EmmaX.FaceChange("sexy", 1)
                $ EmmaX.Statup("Love", 90, 1)
                $ EmmaX.Statup("Inbt", 50, 3) 
                $ Line = renpy.random.choice(["Well. . . ok.",                 
                    "Sure!", 
                    "You could, I guess.",
                    "Um, yeah.",
                    "Heh, ok, ok."]) 
                ch_e "[Line]"
                $ Line = 0
            $ EmmaX.Statup("Obed", 20, 1)
            $ EmmaX.Statup("Obed", 60, 1)
            $ EmmaX.Statup("Inbt", 70, 2) 
            jump Emma_AnalPrep   
               
    else:                                                                               
            #She's not into it, but maybe. . .            
            $ EmmaX.FaceChange("angry")
            if "no anal" in EmmaX.RecentActions:  
                ch_e "I'm afraid that \"no\" is my final answer, [EmmaX.Petname]."
            elif Taboo and "tabno" in EmmaX.DailyActions and "no anal" in EmmaX.DailyActions:
                ch_e "I already told you. . .not in such an exposed location." 
            elif "no anal" in EmmaX.DailyActions:       
                ch_e "I believe I just told you \"no,\" [EmmaX.Petname]."
            elif Taboo and "tabno" in EmmaX.DailyActions:  
                ch_e "I already told you this is too public!"      
            elif not EmmaX.Anal:
                $ EmmaX.FaceChange("bemused")
                ch_e "I don't know that you're ready for that yet."
            else:
                $ EmmaX.FaceChange("bemused")
                ch_e "Perhaps we can work up to that."
            menu:
                extend ""
                "Sorry, never mind." if "no anal" in EmmaX.DailyActions:
                    $ EmmaX.FaceChange("bemused")
                    ch_e "I don't blame you for your. . . enthusiasm."              
                    return
                "Maybe later?" if "no anal" not in EmmaX.DailyActions:
                    $ EmmaX.FaceChange("sexy")  
                    ch_e "I imagine we will. . ."
                    ch_e ". . . often."
                    $ EmmaX.Statup("Love", 80, 2)
                    $ EmmaX.Statup("Inbt", 70, 2)  
                    if Taboo:                    
                        $ EmmaX.RecentActions.append("tabno")                      
                        $ EmmaX.DailyActions.append("tabno") 
                    $ EmmaX.RecentActions.append("no anal")                      
                    $ EmmaX.DailyActions.append("no anal") 
                    return
                "I bet it would feel really good. . .":             
                    if Approval:
                        $ EmmaX.FaceChange("sexy")     
                        $ EmmaX.Statup("Obed", 90, 2)
                        $ EmmaX.Statup("Obed", 50, 2)
                        $ EmmaX.Statup("Inbt", 70, 3) 
                        $ EmmaX.Statup("Inbt", 40, 2) 
                        $ Line = renpy.random.choice(["I can't exactly argue with that. . .",     
                                "I suppose. . .", 
                                "You raise a good point. . ."]) 
                        ch_e "[Line]"
                        $ Line = 0                   
                        jump Emma_AnalPrep
                    else:   
                        pass
                        
                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(EmmaX, 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                    if Approval > 1 or (Approval and EmmaX.Forced):
                        $ EmmaX.FaceChange("sad")
                        $ EmmaX.Statup("Love", 70, -5, 1)
                        $ EmmaX.Statup("Love", 200, -5)                 
                        ch_e "Oh, very well, get it over with."  
                        $ EmmaX.Statup("Obed", 80, 4)
                        $ EmmaX.Statup("Inbt", 80, 1) 
                        $ EmmaX.Statup("Inbt", 60, 3)  
                        $ EmmaX.Forced = 1  
                        jump Emma_AnalPrep
                    else:                              
                        $ EmmaX.Statup("Love", 200, -20)    
                        $ EmmaX.RecentActions.append("angry")
                        $ EmmaX.DailyActions.append("angry")   
    
    #She refused all offers.
    $ EmmaX.ArmPose = 1  
    if "no anal" in EmmaX.DailyActions:
        ch_e "Don't question me again."   
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")   
    elif EmmaX.Forced:
        $ EmmaX.FaceChange("angry", 1)
        ch_e "You're really shooting for the fences on that one."
        $ EmmaX.Statup("Lust", 200, 5)     
        if EmmaX.Love > 300:     
                $ EmmaX.Statup("Love", 70, -2)
        $ EmmaX.Statup("Obed", 50, -2)    
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")   
    elif Taboo:                             
        # she refuses and this is too public a place for her
        $ EmmaX.FaceChange("angry", 1)
        $ EmmaX.RecentActions.append("tabno")                      
        $ EmmaX.DailyActions.append("tabno") 
        ch_e "How can you imagine this would be an appropriate location?" 
        ch_e "This place, I mean, not anal."
        if ApprovalCheck(EmmaX, 500, "I"):
                ch_e "Anal can be nice, sometimes."
        if not Approval:
                ch_e "Maybe not with you."
        $ EmmaX.Statup("Lust", 200, 5)  
        $ EmmaX.Statup("Obed", 50, -3) 
    elif "anal" in EmmaX.DailyActions:
        $ EmmaX.FaceChange("bemused")
        ch_e "Don't wear me out here."    
    elif EmmaX.Anal:
        $ EmmaX.FaceChange("sad") 
        ch_e "You'll have to show me you're worth it again."
    else:
        $ EmmaX.FaceChange("normal", 1)
        ch_e "I don't think you've earned that yet."    
    $ EmmaX.RecentActions.append("no anal")                      
    $ EmmaX.DailyActions.append("no anal") 
    $ Tempmod = 0    
    return

label Emma_AnalPrep:    
    call Seen_First_Peen(EmmaX,Partner,React=Situation)
    call Emma_Sex_Launch("hotdog")
             
    if Situation == EmmaX:                                                                 
            #Emma auto-starts   
            $ Situation = 0
            if EmmaX.PantsNum() == 5:
                "[EmmaX.Name] pushes you back and climbs on top of you, sliding her skirt up as she does so."
                $ EmmaX.Upskirt = 1           
            elif EmmaX.PantsNum() >= 6:
                "[EmmaX.Name] pushes you down and climbs on top of you, sliding her [EmmaX.Legs] down as she does so." 
                $ EmmaX.Upskirt = 1
            else:
                "[EmmaX.Name] pushes you back and climbs on top of you."
            $ EmmaX.SeenPanties = 1
            "She slides the tip against her ass and seems to want you to insert it."
            menu:
                "What do you do?"
                "Go with it.":                    
                    $ EmmaX.Statup("Inbt", 80, 3) 
                    $ EmmaX.Statup("Inbt", 50, 2)
                    "[EmmaX.Name] slides it in."
                "Praise her.":       
                    $ EmmaX.FaceChange("sexy", 1)                    
                    $ EmmaX.Statup("Inbt", 80, 3) 
                    ch_p "Oh yeah, [EmmaX.Pet], let's do this."
                    $ EmmaX.NameCheck() #checks reaction to petname
                    "[EmmaX.Name] slides it in."
                    $ EmmaX.Statup("Love", 85, 1)
                    $ EmmaX.Statup("Obed", 90, 1)
                    $ EmmaX.Statup("Obed", 50, 2)
                "Ask her to stop.":
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
            $ EmmaX.PantiesDown = 1  
            call Emma_First_Bottomless(1)
            
    elif Situation != "auto":
        call Bottoms_Off(EmmaX)    
        if (EmmaX.Panties and not EmmaX.PantiesDown) or (EmmaX.Legs and not EmmaX.Upskirt) or EmmaX.HoseNum() >= 6: #If she refuses to take off her pants but agreed to anal
            ch_e "I suppose we can't do much with all this on."
            
            if (EmmaX.Panties and not EmmaX.PantiesDown) and (EmmaX.PantsNum() > 6 and not EmmaX.Upskirt):
                "She quickly drops her pants and her [EmmaX.Panties]."
            elif (EmmaX.Panties and not EmmaX.PantiesDown) and (EmmaX.PantsNum() == 6 and not EmmaX.Upskirt):
                "She quickly drops her shorts and her [EmmaX.Panties]."
            elif EmmaX.PantsNum() > 6 and not EmmaX.Upskirt:
                "She tugs her pants down, exposing her bare pussy."
            elif EmmaX.PantsNum() == 6 and not EmmaX.Upskirt:
                "She tugs her shorts down, exposing her bare pussy."
            elif EmmaX.HoseNum() >= 6 and (EmmaX.Panties and not EmmaX.PantiesDown):
                "She tugs her [EmmaX.Hose] and [EmmaX.Panties] off."
                $ EmmaX.Hose = 0
            elif EmmaX.HoseNum() >= 6:
                "She tugs her [EmmaX.Hose] off and drops them to the ground."
                $ EmmaX.Hose = 0
            elif (EmmaX.Panties and not EmmaX.PantiesDown):
                "She tugs her [EmmaX.Panties] off and drops them to the ground."  
                
        $ EmmaX.Upskirt = 1
        $ EmmaX.PantiesDown = 1       
        $ EmmaX.SeenPanties = 1
        call Emma_First_Bottomless
        
        if Taboo: # [EmmaX.Name] gets started. . .
            "[EmmaX.Name] glances around to see if anyone notices what she's doing."
            if "cockout" in Player.RecentActions:
                "Then she pushes you back and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and climbs on top of you."
                "She slowly presses against your rigid member."
            $ EmmaX.Inbt += int(Taboo/10)  
            $ EmmaX.Lust += int(Taboo/5)
        else:    
            if "cockout" in Player.RecentActions:
                "[EmmaX.Name] pushes you back and slowly presses against your rigid member."
            else:
                "[EmmaX.Name] pulls down your pants and climbs on top of you."
                "She slowly presses against your rigid member."
        "She leans back a bit and your cock pops in."
                     
    else: #if Situation == "auto"       
        if (EmmaX.PantsNum() > 6 and not EmmaX.Upskirt) and (EmmaX.Panties and not EmmaX.PantiesDown):
            "You quickly pull down her pants and her [EmmaX.Panties] and press against her back door."
        elif (EmmaX.Panties and not EmmaX.PantiesDown):
            "You quickly pull down her [EmmaX.Panties] and press against her back door."  
        $ EmmaX.Upskirt = 1
        $ EmmaX.PantiesDown = 1       
        $ EmmaX.SeenPanties = 1
        call Emma_First_Bottomless(1)
            
    if not EmmaX.Anal:                                                      #First time stat buffs       
        if EmmaX.Forced:
            $ EmmaX.Statup("Love", 90, -150)
            $ EmmaX.Statup("Obed", 70, 70)
            $ EmmaX.Statup("Inbt", 80, 40) 
        else:
            $ EmmaX.Statup("Love", 90, 10)
            $ EmmaX.Statup("Obed", 70, 30)
            $ EmmaX.Statup("Inbt", 80, 70) 
    elif not EmmaX.Loose:                                                   #first few times stat buffs       
        if EmmaX.Forced:
            $ EmmaX.Statup("Love", 90, -20)
            $ EmmaX.Statup("Obed", 70, 10)
            $ EmmaX.Statup("Inbt", 80, 5) 
        else:
            $ EmmaX.Statup("Obed", 70, 7)
            $ EmmaX.Statup("Inbt", 80, 5) 
                
    if Situation:    
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ Player.Cock = "anal"
    $ Trigger = "anal"
    $ Speed = 1
    if Taboo:
        $ EmmaX.DrainWord("tabno")
    $ EmmaX.DrainWord("no anal")
    $ EmmaX.RecentActions.append("anal")                      
    $ EmmaX.DailyActions.append("anal") 

label Emma_Anal_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus(EmmaX)
        call Emma_Sex_Launch("anal") 
        $ Speed = 2 if Speed >= 4 else Speed
        $ EmmaX.LustFace()        
        $ Player.Cock = "anal"
        $ Trigger = "anal"
        
        if Player.Focus < 100:                                                    
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
                                    call Slap_Ass(EmmaX)  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Emma_Anal_Cycle  
                                    
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
                                                ch_e "I'm getting a bit tired here, could we take a break?" 
                                                
                                    "Shift primary action":
                                            if EmmaX.Action and MultiAction:
                                                    menu:
                                                        "How about sex?":
                                                                $ Situation = "shift"
                                                                call Emma_AnalAfter
                                                                call Emma_Sex_P
                                                        "Just stick it in her pussy [[without asking].":
                                                                $ Situation = "auto"
                                                                call Emma_AnalAfter
                                                                call Emma_Sex_P
                                                        "Pull back to hotdog her.":
                                                                $ Situation = "pullback"
                                                                call Emma_AnalAfter
                                                                call Emma_Sex_H
                                                        "Never Mind":
                                                                jump Emma_Anal_Cycle
                                            else:
                                                ch_e "I'm getting a bit tired here, could we take a break?" 
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
                                                        jump Emma_Anal_Cycle 
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_Anal_Cycle 
                                            "Never mind":
                                                        jump Emma_Anal_Cycle 
                                    "Undress [EmmaX.Name]":
                                            call Girl_Undress(EmmaX)   
                                    "Clean up [EmmaX.Name] (locked)" if not EmmaX.Spunk:
                                            pass  
                                    "Clean up [EmmaX.Name]" if EmmaX.Spunk:
                                            call Girl_Cleanup(EmmaX,"ask")                                         
                                    "Never mind":
                                            jump Emma_Anal_Cycle                                    
                                                        
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Emma_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Emma_AnalAfter
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Emma_Sex_Reset
                                    $ Line = 0
                                    jump Emma_AnalAfter
        #End menu (if Line)              
        
        call Shift_Focus(EmmaX)    
        call Sex_Dialog(EmmaX,Partner)
        
        $ Cnt += 1
        $ Round -= 1     
        
        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or EmmaX.Lust >= 100:   
                    #If either of you could cum    
                    if Player.Focus >= 100:
                            #If you can cum:                                                
                            call Player_Cumming(EmmaX)
                            if "angry" in EmmaX.RecentActions:  
                                call Emma_Sex_Reset
                                return    
                            $ EmmaX.Statup("Lust", 200, 5) 
                            if 100 > EmmaX.Lust >= 70 and EmmaX.OCount < 2:             
                                    $ EmmaX.RecentActions.append("unsatisfied")                      
                                    $ EmmaX.DailyActions.append("unsatisfied") 
                            
                            if Player.Focus > 80:
                                jump Emma_AnalAfter 
                            $ Line = "came"

                    if EmmaX.Lust >= 100:         
                            #If you're still going at it and [EmmaX.Name] can cum
                            call Girl_Cumming(EmmaX)
                            if Situation == "shift" or "angry" in EmmaX.RecentActions:
                                jump Emma_AnalAfter
                       
                    if Line == "came": #ex Player.Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Emma_AnalAfter
                            elif "unsatisfied" in EmmaX.RecentActions:
                                #And [EmmaX.Name] is unsatisfied,  
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ Line = "You get back into it" 
                                        jump Emma_Anal_Cycle  
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Emma_AnalAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Emma_AnalAfter   
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)            
        #End orgasm
        
        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0
        
        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif Cnt == (5 + EmmaX.Anal):
                    $ EmmaX.Brows = "confused"
                    ch_e "So are we getting close here?"   
        elif Cnt == (10 + EmmaX.Anal):
                    $ EmmaX.Brows = "angry"        
                    ch_e "I'm . . .getting . . a bit. . . tired. . . of this. . ."
                    menu:
                        ch_e "Can we. . . do something. . . else?"
                        "How about a BJ?" if EmmaX.Action and MultiAction:
                                $ Situation = "shift"
                                call Emma_AnalAfter
                                call Emma_Blowjob  
                        "How about a Handy?" if EmmaX.Action and MultiAction:
                                $ Situation = "shift"
                                call Emma_AnalAfter
                                call Emma_Handjob     
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."             
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ Cnt += 1
                                jump Emma_Anal_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Emma_Sex_Reset
                                $ Situation = "shift"
                                jump Emma_AnalAfter
                        "No, get back down there.":                                
                                if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):                        
                                    $ EmmaX.Statup("Love", 200, -5)
                                    $ EmmaX.Statup("Obed", 50, 3)                    
                                    $ EmmaX.Statup("Obed", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    $ EmmaX.FaceChange("angry", 1)   
                                    call Emma_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_e "No, I think not."                         
                                    $ EmmaX.Statup("Love", 50, -3, 1)
                                    $ EmmaX.Statup("Love", 80, -4, 1)
                                    $ EmmaX.Statup("Obed", 30, -1, 1)                    
                                    $ EmmaX.Statup("Obed", 50, -1, 1)  
                                    $ EmmaX.RecentActions.append("angry")
                                    $ EmmaX.DailyActions.append("angry")   
                                    jump Emma_AnalAfter
        #End Count check
   
        if Round == 10:
            ch_e "You might want to think about your endgame here. . ."  
        elif Round == 5:
            ch_e "We'll need a break soon."        
    
    #Round = 0 loop breaks
    $ EmmaX.FaceChange("bemused", 0)
    $ Line = 0
    ch_e "Ok, [EmmaX.Petname], that's enough of that for now."
    
label Emma_AnalAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ Player.Sprite = 0
        $ Player.Cock = "out"
        call Emma_Sex_Reset
        
    $ EmmaX.FaceChange("sexy") 
    
    $ EmmaX.Anal += 1  
    $ EmmaX.Action -=1
    $ EmmaX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ EmmaX.Addictionrate += 1        
    $ EmmaX.Statup("Inbt", 30, 3) 
    $ EmmaX.Statup("Inbt", 70, 1) 
    
    if Partner == "Kitty":
        call Partner_Like(EmmaX,4,2)
    else:
        call Partner_Like(EmmaX,3,2)
    
    if "Emma Anal Addict" in Achievements:
            pass 
            
    elif EmmaX.Anal >= 10:
        $ EmmaX.SEXP += 7
        $ Achievements.append("Emma Anal Addict")
        if not Situation:
            $ EmmaX.FaceChange("bemused", 1)
            ch_e "You're one of the better partners I've had at that."                  
    elif EmmaX.Anal == 1:            
            $EmmaX.SEXP += 25        
            if not Situation: 
                if EmmaX.Love >= 500 and "unsatisfied" not in EmmaX.RecentActions:
                    ch_e "You really took to that well."
                elif EmmaX.Obed <= 500 and Player.Focus <= 20:
                    $ EmmaX.Mouth = "sad"
                    ch_e "Oooh."
                    ch_e "It's been a while."
    elif EmmaX.Anal == 5:
            ch_e "You're pretty good at that."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in EmmaX.RecentActions:
            $ EmmaX.FaceChange("angry")
            $ EmmaX.Eyes = "side"
            ch_e  "Hmm, you seemed to get more out of that than I did. . ."
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_e "Mmm, so what else did you have in mind?"
    call Checkout
    return   


# End [EmmaX.Name] Anal //////////////////////////////////////////////////////////////////////////////////
    

  
# [EmmaX.Name] hotdog //////////////////////////////////////////////////////////////////////

label Emma_Sex_H: 
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(EmmaX)
    if EmmaX.Hotdog >= 3: #You've done it before several times
        $ Tempmod += 10
    elif EmmaX.Hotdog: #You've done it before
        $ Tempmod += 5    
    
    if EmmaX.Lust > 85:
        $ Tempmod += 10
    elif EmmaX.Lust > 75: #She's really horny
        $ Tempmod += 5
    if Situation == "shift":
        $ Tempmod += 10   
    if "exhibitionist" in EmmaX.Traits:
        $ Tempmod += (3*Taboo)  
    if "dating" in EmmaX.Traits or "sex friend" in EmmaX.Petnames:
        $ Tempmod += 10
    elif "ex" in EmmaX.Traits:
        $ Tempmod -= 40 
    if EmmaX.ForcedCount and not EmmaX.Forced:
        $ Tempmod -= 5 * EmmaX.ForcedCount 
    
    if Taboo and "tabno" in EmmaX.DailyActions:        
        $ Tempmod -= 10 
        
    if "no hotdog" in EmmaX.DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no hotdog" in EmmaX.RecentActions else 0      
        
    $ Approval = ApprovalCheck(EmmaX, 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)
    
    if Situation == "auto":   
            call Emma_Sex_Launch("L")   
            "You roll back, pulling [EmmaX.Name] on top of you, and press your cock against her."    
            $ EmmaX.FaceChange("surprised", 1)
            
            if (EmmaX.Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
                "[EmmaX.Name] is briefly startled, but melts into a sly smile."
                $ EmmaX.FaceChange("sly")
                $ EmmaX.Statup("Obed", 70, 3)
                $ EmmaX.Statup("Inbt", 50, 3) 
                $ EmmaX.Statup("Inbt", 70, 1) 
                ch_e "Now what shall we do with that . ."            
                jump Emma_HotdogPrep         
            else:                                                                                                            #she's questioning it
                $ EmmaX.Brows = "angry"                
                menu:
                    ch_e "You might want to take a step back, [EmmaX.Petname]?" 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            $ EmmaX.FaceChange("sexy", 1)
                            $ EmmaX.Statup("Obed", 70, 3)
                            $ EmmaX.Statup("Inbt", 50, 3) 
                            $ EmmaX.Statup("Inbt", 70, 1) 
                            ch_e "Or not. . ."
                            jump Emma_HotdogPrep
                        "You pull back from her."                    
                        $ EmmaX.FaceChange("bemused", 1)
                        ch_e "You might get better results if you asked first?"                                             
                    "You'll see.":                    
                        $ EmmaX.Statup("Love", 80, -10, 1)  
                        $ EmmaX.Statup("Love", 200, -8)
                        "You grind against her crotch."                              
                        $ EmmaX.Statup("Obed", 70, 3)
                        $ EmmaX.Statup("Inbt", 50, 3) 
                        if not ApprovalCheck(EmmaX, 500, "O", TabM=1): #Checks if Obed is 700+  
                            $ EmmaX.FaceChange("angry")
                            "[EmmaX.Name] shoves you away."
                            ch_e "Don't push your luck, [EmmaX.Petname]."                                                  
                            $ EmmaX.Statup("Love", 50, -10, 1)                        
                            $ EmmaX.Statup("Obed", 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            call Emma_Sex_Reset
                            $ EmmaX.RecentActions.append("angry")
                            $ EmmaX.DailyActions.append("angry")                       
                        else:
                            $ EmmaX.FaceChange("sad")
                            "[EmmaX.Name] doesn't seem to be into this, but she knows her place."                        
                            jump Emma_HotdogPrep
            return     
            #end auto
    
   
    if not EmmaX.Hotdog and "no hotdog" not in EmmaX.RecentActions:                                                               
            #first time    
            $ EmmaX.FaceChange("surprised", 1)
            $ EmmaX.Mouth = "kiss"
            ch_e "You just want me to grind against you then?"
      
            if EmmaX.Forced:
                $ EmmaX.FaceChange("sad")
                ch_e ". . . nothing more than that?"
        
        
    if not EmmaX.Hotdog and Approval:                                                
            #First time dialog        
            if EmmaX.Forced: 
                $ EmmaX.FaceChange("sad")
                $ EmmaX.Statup("Love", 70, -3, 1)
                $ EmmaX.Statup("Love", 20, -2, 1)
            elif EmmaX.Love >= (EmmaX.Obed + EmmaX.Inbt):
                $ EmmaX.FaceChange("sexy")
                $ EmmaX.Brows = "sad"
                $ EmmaX.Mouth = "smile" 
                ch_e "I wouldn't want to leave you. . . unattended. . ."           
            elif EmmaX.Obed >= EmmaX.Inbt:
                $ EmmaX.FaceChange("normal")
                ch_e "If that's what works for you. . ."
            elif EmmaX.Addict >= 50:
                $ EmmaX.FaceChange("manic", 1)
                ch_e "Hrmm. . ."
            else: # Uninhibited 
                $ EmmaX.FaceChange("sad")
                $ EmmaX.Mouth = "smile"             
                ch_e "Well if that's what gets you off. . ."    
            
    elif Approval:                                                                      
            #Second time+ dialog
            if EmmaX.Forced: 
                $ EmmaX.FaceChange("sad")
                $ EmmaX.Statup("Love", 70, -3, 1)
                $ EmmaX.Statup("Love", 20, -2, 1)
                ch_e "Maybe that's going a bit too far. . ."  
            elif not Taboo and "tabno" in EmmaX.DailyActions:        
                ch_e "I suppose this is a better location . ."   
            elif "hotdog" in EmmaX.RecentActions:
                $ EmmaX.FaceChange("sexy", 1)
                ch_e "Again? Oh, very well."
                jump Emma_HotdogPrep
            elif "hotdog" in EmmaX.DailyActions:
                $ EmmaX.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Back again so soon?",                 
                    "So you'd like another round?",                 
                    "You're really into this. . .", 
                    "Are you sure that's all you want?"]) 
                ch_e "[Line]"    
            else:       
                $ EmmaX.FaceChange("sexy", 1)
                $ EmmaX.ArmPose = 2
                $ Line = renpy.random.choice(["Oooh, you want some of this?",                 
                    "So you'd like another round?",                       
                    "You're really into this. . .", 
                    "You want another rub?"]) 
                ch_e "[Line]"
            $ Line = 0
            
    if Approval >= 2:                                                                  
            #She's into it. . .               
            if EmmaX.Forced:
                $ EmmaX.FaceChange("sad")
                $ EmmaX.Statup("Obed", 80, 1)
                $ EmmaX.Statup("Inbt", 60, 1)
                ch_e "Ok, fine."    
            elif "no hotdog" in EmmaX.DailyActions:               
                ch_e "It was rather entertaining. . ."
            else:
                $ EmmaX.FaceChange("sexy", 1)
                $ EmmaX.Statup("Love", 80, 1)
                $ EmmaX.Statup("Inbt", 50, 2) 
                $ Line = renpy.random.choice(["Well, sure, let me give it a rub.",                 
                    "Very well.",                 
                    "Nice!", 
                    "I suppose we could do that.",
                    "Allow me. . .",
                    "Heh, ok, ok."]) 
                ch_e "[Line]"
                $ Line = 0
            $ EmmaX.Statup("Obed", 60, 1)
            $ EmmaX.Statup("Inbt", 70, 2) 
            jump Emma_HotdogPrep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            $ EmmaX.FaceChange("angry")
            if "no hotdog" in EmmaX.RecentActions:  
                ch_e "I'm afraid that \"no\" is my final answer, [EmmaX.Petname]."
            elif Taboo and "tabno" in EmmaX.DailyActions and "no hotdog" in EmmaX.DailyActions: 
                ch_e "I just told you. . .not in such an exposed location." 
            elif "no hotdog" in EmmaX.DailyActions:       
                ch_e "I'm believe I just told you \"no,\" [EmmaX.Petname]."
            elif Taboo and "tabno" in EmmaX.DailyActions:  
                ch_e "I already told you. . .not in such an exposed location." 
            elif not EmmaX.Hotdog:
                $ EmmaX.FaceChange("bemused")
                ch_e "Hmm, that could be amusing, [EmmaX.Petname]. . ."
            else:
                $ EmmaX.FaceChange("bemused")
                ch_e "I don't think that would be appropriate. . ."
            menu:
                extend ""
                "Sorry, never mind." if "no hotdog" in EmmaX.DailyActions:
                    $ EmmaX.FaceChange("bemused")
                    ch_e "No harm in asking. Once."              
                    return
                "Maybe later?" if "no hotdog" not in EmmaX.DailyActions:
                    $ EmmaX.FaceChange("sexy")  
                    ch_e "I imagine it will happen at some point, [EmmaX.Petname]."
                    $ EmmaX.Statup("Love", 80, 1)
                    $ EmmaX.Statup("Inbt", 50, 1)   
                    if Taboo:                    
                        $ EmmaX.RecentActions.append("tabno")                      
                        $ EmmaX.DailyActions.append("tabno") 
                    $ EmmaX.RecentActions.append("no hotdog")                      
                    $ EmmaX.DailyActions.append("no hotdog")                          
                    return
                "You might like it. . .":             
                    if Approval:
                        $ EmmaX.FaceChange("sexy")     
                        $ EmmaX.Statup("Obed", 60, 2)
                        $ EmmaX.Statup("Inbt", 50, 2) 
                        $ Line = renpy.random.choice(["I can't exactly argue with that. . .",     
                                "I suppose. . .", 
                                "You raise a good point. . ."]) 
                        ch_e "[Line]"
                        $ Line = 0                   
                        jump Emma_HotdogPrep
                    else:   
                        pass
                        
                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(EmmaX, 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                    if Approval > 1 or (Approval and EmmaX.Forced):
                        $ EmmaX.FaceChange("sad")
                        $ EmmaX.Statup("Love", 70, -2, 1)
                        $ EmmaX.Statup("Love", 200, -2)                 
                        ch_e "Alright, fine. Lay back."  
                        $ EmmaX.Statup("Obed", 80, 4)
                        $ EmmaX.Statup("Inbt", 60, 2)  
                        $ EmmaX.Forced = 1  
                        jump Emma_HotdogPrep
                    else:                              
                        $ EmmaX.Statup("Love", 200, -10)     
                        $ EmmaX.RecentActions.append("angry")
                        $ EmmaX.DailyActions.append("angry")   
    
    #She refused all offers.
    $ EmmaX.ArmPose = 1      
    
    if "no hotdog" in EmmaX.DailyActions:
        ch_e "I've made myself clear."   
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")   
    if EmmaX.Forced:
        $ EmmaX.FaceChange("angry", 1)
        ch_e "I just don't see the benefit."
        $ EmmaX.Statup("Lust", 200, 5)  
        if EmmaX.Love > 300:   
                $ EmmaX.Statup("Love", 70, -1)
        $ EmmaX.Statup("Obed", 50, -1)  
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        $ EmmaX.FaceChange("angry", 1)        
        $ EmmaX.RecentActions.append("tabno")                      
        $ EmmaX.DailyActions.append("tabno") 
        ch_e "This area is a bit too exposed for that sort of thing. . ."  
        $ EmmaX.Statup("Lust", 200, 5)  
        $ EmmaX.Statup("Obed", 50, -3)  
    elif EmmaX.Hotdog:
        $ EmmaX.FaceChange("sad") 
        ch_e "Not under the circumstances."
    else:
        $ EmmaX.FaceChange("normal", 1)
        ch_e "No, thank you."    
    $ EmmaX.RecentActions.append("no hotdog")                      
    $ EmmaX.DailyActions.append("no hotdog") 
    $ Tempmod = 0    
    return

label Emma_HotdogPrep:  
    call Seen_First_Peen(EmmaX,Partner,React=Situation)
    call Emma_Sex_Launch("hotdog")
    
         
    if Situation == EmmaX:                                                                 
            #Emma auto-starts   
            $ Situation = 0
            "[EmmaX.Name] pushes you back and climbs on top of you, sliding back and forth along your shaft."
            menu:
                "What do you do?"
                "Go with it.":                    
                    $ EmmaX.Statup("Inbt", 80, 3) 
                    $ EmmaX.Statup("Inbt", 50, 2)
                    "[EmmaX.Name] starts to grind against you."
                "Praise her.":       
                    $ EmmaX.FaceChange("sexy", 1)                    
                    $ EmmaX.Statup("Inbt", 80, 3) 
                    ch_p "Oh yeah, [EmmaX.Pet], let's do this."
                    $ EmmaX.NameCheck() #checks reaction to petname
                    "[EmmaX.Name] starts to grind against you."
                    $ EmmaX.Statup("Love", 85, 1)
                    $ EmmaX.Statup("Obed", 90, 1)
                    $ EmmaX.Statup("Obed", 50, 2)
                "Ask her to stop.":
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
            
    elif Situation != "auto":
#        call Bottoms_Off(EmmaX)    
        
        if Taboo: # [EmmaX.Name] gets started. . .
            "[EmmaX.Name] glances around to see if anyone notices what she's doing."
            if "cockout" in Player.RecentActions:
                "Then she pushes you back and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and climbs on top of you."
                "She slowly presses against your rigid member."
            $ EmmaX.Inbt += int(Taboo/10)  
            $ EmmaX.Lust += int(Taboo/5)
        else:    
            if "cockout" in Player.RecentActions:
                "[EmmaX.Name] pushes you back and slowly presses against your rigid member."
            else:
                "[EmmaX.Name] pulls down your pants and climbs on top of you."
                "She slowly presses against your rigid member."
                     
    else: #if Situation == "auto"       
        "You roll back, pulling her on top of you and your rigid member."
    
    if not EmmaX.Hotdog:                                                      #First time stat buffs      
        if EmmaX.Forced:
            $ EmmaX.Statup("Love", 90, -5)
            $ EmmaX.Statup("Obed", 70, 20)
            $ EmmaX.Statup("Inbt", 80, 10) 
        else:
            $ EmmaX.Statup("Love", 90, 20)
            $ EmmaX.Statup("Obed", 70, 20)
            $ EmmaX.Statup("Inbt", 80, 20)  
    
            
    if Situation:    
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ Trigger = "hotdog"
    $ Speed = 1
    if Taboo:
        $ EmmaX.DrainWord("tabno")
    $ EmmaX.DrainWord("no hotdog")
    $ EmmaX.RecentActions.append("hotdog")                      
    $ EmmaX.DailyActions.append("hotdog") 

label Emma_Hotdog_Cycle: #Repeating strokes 
    while Round >=0:  
        call Shift_Focus(EmmaX)
        call Emma_Sex_Launch("hotdog") 
        $ Speed = 2 if Speed >= 4 else Speed
        $ EmmaX.LustFace()        
        $ Player.Cock = "out"
        $ Trigger = "hotdog"
        
        if  Player.Focus < 100:                                                    
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
                                    call Slap_Ass(EmmaX)  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Emma_Hotdog_Cycle  
                                    
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
                                                ch_e "I'm getting a bit tired here, could we take a break?" 
                                                
                                    "Shift primary action":
                                            if EmmaX.Action and MultiAction:
                                                    menu:
                                                        "How about sex?":
                                                            $ Situation = "shift"
                                                            call Emma_HotdogAfter
                                                            call Emma_Sex_P
                                                        "Just stick it in her pussy [[without asking].":
                                                            $ Situation = "auto"
                                                            call Emma_HotdogAfter
                                                            call Emma_Sex_P
                                                        "How about anal?":
                                                            $ Situation = "shift"
                                                            call Emma_HotdogAfter
                                                            call Emma_Sex_A
                                                        "Just stick it in her ass [[without asking].":
                                                            $ Situation = "auto"
                                                            call Emma_HotdogAfter
                                                            call Emma_Sex_A
                                                        "Never Mind":
                                                                jump Emma_Hotdog_Cycle
                                            else:
                                                ch_e "I'm getting a bit tired here, could we take a break?" 
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
                                                        jump Emma_Hotdog_Cycle 
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_Hotdog_Cycle 
                                            "Never mind":
                                                        jump Emma_Hotdog_Cycle 
                                    "Undress [EmmaX.Name]":
                                            call Girl_Undress(EmmaX)   
                                    "Clean up [EmmaX.Name] (locked)" if not EmmaX.Spunk:
                                            pass  
                                    "Clean up [EmmaX.Name]" if EmmaX.Spunk:
                                            call Girl_Cleanup(EmmaX,"ask")                                         
                                    "Never mind":
                                            jump Emma_Hotdog_Cycle                                    
                                                        
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Emma_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Emma_HotdogAfter
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Emma_Sex_Reset
                                    $ Line = 0
                                    jump Emma_HotdogAfter
        #End menu (if Line)              
        
        call Shift_Focus(EmmaX)    
        call Sex_Dialog(EmmaX,Partner)
        
        $ Cnt += 1
        $ Round -= 1     
        
        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or EmmaX.Lust >= 100:   
                    #If either of you could cum    
                    if Player.Focus >= 100:
                            #If you can cum:                                                
                            call Player_Cumming(EmmaX)
                            if "angry" in EmmaX.RecentActions:  
                                call Emma_Sex_Reset
                                return    
                            $ EmmaX.Statup("Lust", 200, 5) 
                            if 100 > EmmaX.Lust >= 70 and EmmaX.OCount < 2:             
                                    $ EmmaX.RecentActions.append("unsatisfied")                      
                                    $ EmmaX.DailyActions.append("unsatisfied") 
                            
                            if Player.Focus > 80:
                                jump Emma_HotdogAfter 
                            $ Line = "came"

                    if EmmaX.Lust >= 100:         
                            #If you're still going at it and [EmmaX.Name] can cum
                            call Girl_Cumming(EmmaX)
                            if Situation == "shift" or "angry" in EmmaX.RecentActions:
                                jump Emma_HotdogAfter
                       
                    if Line == "came": #ex Player.Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Emma_HotdogAfter
                            elif "unsatisfied" in EmmaX.RecentActions:
                                #And [EmmaX.Name] is unsatisfied,  
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ Line = "You get back into it" 
                                        jump Emma_Hotdog_Cycle  
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Emma_HotdogAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Emma_HotdogAfter      
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)            
        #End orgasm
        
        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0
        
        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif Cnt == (5 + EmmaX.Hotdog):
                    $ EmmaX.Brows = "confused"
                    ch_e "Are we getting close here?"   
        elif Cnt == (10 + EmmaX.Hotdog):
                    $ EmmaX.Brows = "angry"        
                    menu:
                        ch_e "I'm a bit bored by this."
                        "How about a BJ?" if EmmaX.Action and MultiAction:
                                $ Situation = "shift"
                                call Emma_HotdogAfter
                                call Emma_Blowjob       
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."             
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ Cnt += 1
                                jump Emma_Hotdog_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Emma_Sex_Reset
                                $ Situation = "shift"
                                jump Emma_HotdogAfter
                        "No, get back down there.":                                
                                if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):                        
                                    $ EmmaX.Statup("Love", 200, -5)
                                    $ EmmaX.Statup("Obed", 50, 3)                    
                                    $ EmmaX.Statup("Obed", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    $ EmmaX.FaceChange("angry", 1)   
                                    call Emma_Sex_Reset
                                    "She scowls at you and pulls away."
                                    ch_e "No, I think not."                         
                                    $ EmmaX.Statup("Love", 50, -3, 1)
                                    $ EmmaX.Statup("Love", 80, -4, 1)
                                    $ EmmaX.Statup("Obed", 30, -1, 1)                    
                                    $ EmmaX.Statup("Obed", 50, -1, 1)  
                                    $ EmmaX.RecentActions.append("angry")
                                    $ EmmaX.DailyActions.append("angry")   
                                    jump Emma_HotdogAfter
        #End Count check
   
        call Escalation(EmmaX) #sees if she wants to escalate things
        
        if Round == 10:
            ch_e "You might want to think about your endgame here. . ."  
        elif Round == 5:
            ch_e "We'll need a break soon."        
    
    #Round = 0 loop breaks
    $ EmmaX.FaceChange("bemused", 0)
    $ Line = 0
    ch_e "Ok, [EmmaX.Petname], that's enough of that for now."
    
label Emma_HotdogAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ Player.Sprite = 0
        $ Player.Cock = "out"
        call Emma_Sex_Reset
        
    $ EmmaX.FaceChange("sexy") 
    
    $ EmmaX.Hotdog += 1  
    $ EmmaX.Action -=1
    $ EmmaX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ EmmaX.Addictionrate += 1        
    $ EmmaX.Statup("Inbt", 30, 1) 
    $ EmmaX.Statup("Inbt", 70, 1) 
    
    call Partner_Like(EmmaX,2)
    
    if EmmaX.Hotdog == 10:
        $ EmmaX.SEXP += 5             
    elif EmmaX.Hotdog == 1:            
            $EmmaX.SEXP += 10        
            if not Situation: 
                if EmmaX.Love >= 500 and "unsatisfied" not in EmmaX.RecentActions:
                    ch_e "That was. . . pleasant."
                elif EmmaX.Obed <= 500 and Player.Focus <= 20:
                    $ EmmaX.Mouth = "sad"
                    ch_e "Was that enough for you?" 
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in EmmaX.RecentActions:
            $ EmmaX.FaceChange("angry")
            $ EmmaX.Eyes = "side"
            ch_e "I'm afraid that didn't do much for me. . ."
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_e "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# End [EmmaX.Name] hotdogging //////////////////////////////////////////////////////////////////////////////////
