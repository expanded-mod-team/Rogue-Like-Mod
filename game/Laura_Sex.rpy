﻿# Laura_SexMenu //////////////////////////////////////////////////////////////////////
label Laura_SexAct(Act = 0):    
        call Shift_Focus(LauraX)    
        if Act == "SkipTo":
            $ renpy.pop_call() #causes it to skip past the Trigger Swap
            $ renpy.pop_call() #causes it to skip past the cycle you were in before
            #$ renpy.pop_call() #causes it to skip past the sex menu you were in before that
            call SkipTo(LauraX)
        elif Act == "switch":
            $ renpy.pop_call() #causes it to skip past call here from Sex_Menu_Threesome
            #$ renpy.pop_call() #causes it to skip past call to Sex_Menu_Threesome
            # drops through to sex menu
        elif Act == "masturbate":         
            call Laura_M_Prep
            if not Situation:
                return    
        elif Act == "lesbian":         
            call Les_Prep(LauraX) #nee call Laura_Les_Prep
            if not Situation:
                return     
        elif Act == "kissing":        
            call KissPrep(LauraX)
            if not Situation:
                return   
        elif Act == "breasts":        
            call Laura_Fondle_Breasts
            if not Situation:
                return  
        elif Act == "blow":        
            call Laura_BJ_Prep
            if not Situation:
                return  
        elif Act == "hand":        
            call Laura_HJ_Prep
            if not Situation:
                return   
        elif Act == "sex":        
            call Laura_SexPrep
            if not Situation:
                return   

label Laura_SexMenu:     
        call Shift_Focus(LauraX)
        $ Trigger = 0    
        $ Trigger2 = 0
        $ Trigger3 = 0
        $ Situation = 0
        call Laura_Hide    
        $ LauraX.ArmPose = 1
        call Set_The_Scene(1,0,0,0,1)
        if not Player.Semen:
                "You're a little out of juice at the moment, you might want to wait a bit." 
        if Player.Focus >= 95:
                "You're practically buzzing, the slightest breeze could set you off."
        if not LauraX.Action:
                "[LauraX.Name]'s looking a bit tired out, maybe let her rest a bit."
        
        if "caught" in LauraX.RecentActions or "angry" in LauraX.RecentActions:  
                if LauraX.Loc == bg_current:                
                        ch_l "You really don't want to try me right now."
                $ LauraX.OutfitChange()        
                $ LauraX.DrainWord("caught",1,0)
                return
            
        if Round < 5:
            ch_l "You're looking a bit worn out, maybe take a break."   
            return
        menu Laura_SMenu:  
            ch_l "What did you want to do?"
            "Do you want to make out?":
                    if LauraX.Action:
                        call Makeout(LauraX)
                    else:
                        ch_l "Maybe in a minute, I need a break." 
            
            "Could I touch you?":
                    if LauraX.Action:
                        $ LauraX.Mouth = "smile"                    
                        menu:
                            ch_l "Yeah? Like where?"                      
                            "Could I give you a massage?":
                                    call Massage(LauraX)                        
                            "Your breasts?":
                                    call Laura_Fondle_Breasts
                            "Suck your breasts?" if LauraX.Action and LauraX.SuckB:
                                    call Laura_Suck_Breasts
                            "Your thighs?" if LauraX.Action:
                                    call Laura_Fondle_Thighs
                            "Your pussy?" if LauraX.Action:
                                    call Laura_Fondle_Pussy
                            "Lick your pussy?" if LauraX.Action and LauraX.LickP:
                                    call Laura_Lick_Pussy
                            "Your Ass?":
                                    call Laura_Fondle_Ass
                            "Never mind [[something else]":
                                    jump Laura_SMenu
                    else:
                        ch_l "Maybe in a minute, I need a break."
                        
            "Could you take care of something for me? [[Your dick, you mean your dick]":        
                    if Player.Semen and LauraX.Action:                
                        menu:
                            ch_l "Oh? Like what?"
                            "Could you give me a handjob?":
                                call Laura_Handjob
                            "Could you give me a titjob?":
                                call Laura_Titjob         
                            "Could you suck my cock?":
                                call Laura_Blowjob 
                            "Could use your feet?":
                                call Laura_Footjob 
                            "Never mind [[something else]":
                                jump Laura_SMenu
                    elif not LauraX.Action:
                                ch_l "Maybe in a minute, I need a break." 
                    else:
                                "You really don't have it in you, maybe take a break." 
                    
            "Could you put on a show for me?":
                        menu:
                            ch_l "What kind of show are you thinking?"
                            "Dance for me?":
                                    if LauraX.Action:
                                        call Group_Strip(LauraX) 
                                    else:
                                        ch_l "Maybe in a minute, I need a break."
                                    
                            "Could you undress for me?": 
                                        call Girl_Undress(LauraX)  
                                                
                            "You've got a little something. . . [[clean-up]" if LauraX.Spunk:
                                        ch_l "What?"
                                        call Girl_Cleanup(LauraX,"ask")
                                        
                            "Could I watch you get yourself off? [[masturbate]":
                                    if LauraX.Action:
                                        call Laura_Masturbate           
                                    else:
                                        ch_l "Maybe in a minute, I need a break."
                            
                            "Maybe make out with [RogueX.Name]?" if RogueX.Loc == bg_current:
                                        call LesScene(LauraX)
                            "Maybe make out with [KittyX.Name]?" if KittyX.Loc == bg_current:
                                        call LesScene(LauraX)
                            "Maybe make out with [EmmaX.Name]?" if EmmaX.Loc == bg_current:
                                        call LesScene(LauraX)

                            "Never mind [[something else]":
                                        jump Laura_SMenu
                              
                    
            "Could we maybe?. . . [[fuck]":
                    if LauraX.Action:
                        menu:
                            "What did you want to do?"
                            "Lean back, I've got something in mind. . .":
                                        if Player.Semen:
                                            call Laura_Sex_H   
                                        else:
                                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                            "Fuck your pussy.":    
                                        if Player.Semen:                    
                                            call Laura_Sex_P  
                                        else:
                                            "The spirit is apparently willing, but the flesh is spongy and bruised."          
                            "Fuck your ass.":     
                                        if Player.Semen:                   
                                            call Laura_Sex_A    
                                        else:
                                            "The spirit is apparently willing, but the flesh is spongy and bruised." 
                            "How about some toys? [[Pussy]":                        
                                        call Laura_Dildo_Pussy     
                            "How about some toys? [[Anal]":                        
                                        call Laura_Dildo_Ass   
                            "Never mind [[something else]":
                                        jump Laura_SMenu
                    else:
                                        ch_l "Maybe in a minute, I need a break."
                            
            "Hey, do you want in on this? [[Threesome]" if not Partner:
                        call Sex_Menu_Threesome(LauraX)
                        jump Laura_SMenu
                        
            "Hey, [Partner.Name]? [[Switch lead]" if Partner:
                        call expression Partner.Tag + "_SexAct" pass ("switch") #call Rogue_SexAct("switch")     
                        return

            "Cheat Menu" if config.developer:
                        call Cheat_Menu(LauraX)
            "Never mind. [[exit]":         
                    if LauraX.Lust >= 50 or LauraX.Addict >= 50:
                            $ LauraX.FaceChange("sad")
                            if LauraX.Action and LauraX.SEXP >= 15 and Round > 20:
                                    if "round2" not in LauraX.RecentActions:  
                                            ch_l "Are you sure, [LauraX.Petname]?"
                                            ch_l "I could go another round. . . or two. . ."                
                                            $ LauraX.Statup("Inbt", 30, 2)
                                            $ LauraX.Statup("Inbt", 50, 1)
                                    elif LauraX.Addict >= 50:                        
                                            ch_l "I need more contact." 
                                    else:
                                            ch_l "Aren't you forgetting something?"                          
                                    menu:
                                        extend ""
                                        "Yeah, I'm done for now." if Player.Semen and "round2" not in LauraX.RecentActions:                 
                                            if "unsatisfied" in LauraX.RecentActions and not LauraX.OCount:                                
                                                $ LauraX.FaceChange("angry")
                                                $ LauraX.Eyes = "side" 
                                                $ LauraX.Statup("Love", 70, -2)
                                                $ LauraX.Statup("Love", 90, -4)
                                                $ LauraX.Statup("Obed", 30, 2)
                                                $ LauraX.Statup("Obed", 70, 1)
                                                ch_l "You'll regret that one."
                                            else:                               
                                                $ LauraX.FaceChange("bemused", 1)
                                                $ LauraX.Statup("Obed", 50, 2)   
                                                ch_l "Selfish. . ."  
                                        "I gave it a shot." if "round2" in LauraX.RecentActions:                 
                                            if "unsatisfied" in LauraX.RecentActions and not LauraX.OCount:                                
                                                $ LauraX.FaceChange("angry")
                                                $ LauraX.Eyes = "side"                                 
                                                ch_l "Not a very good one."
                                            else:                               
                                                $ LauraX.FaceChange("bemused", 1) 
                                                ch_l "Selfish. . ."  
                                        "Hey, I did my part." if LauraX.OCount > 2:      
                                                $ LauraX.FaceChange("sly", 1) 
                                                ch_l "Well. . . yeah, but. . ."  
                                        "I'm tapped out for the moment, let's try again later." if not Player.Semen:
                                                $ LauraX.FaceChange("normal")                        
                                                ch_l "Well, you could always try something else. . ."
                                        "Ok, we can try something else." if MultiAction and "round2" not in LauraX.RecentActions:
                                                $ LauraX.FaceChange("smile")
                                                $ LauraX.Statup("Love", 70, 2)
                                                $ LauraX.Statup("Love", 90, 1) 
                                                ch_l "Good. . ."                            
                                                $ LauraX.RecentActions.append("round2")                      
                                                $ LauraX.DailyActions.append("round2") 
                                                jump Laura_SexMenu
                                        "Again? Ok, fine." if MultiAction and "round2" in LauraX.RecentActions:
                                                $ LauraX.FaceChange("sly")
                                                ch_l "Always. . ."           
                                                jump Laura_SexMenu  
                                    #End "if Laura is still up for more"
                            else:  
                                                $ LauraX.FaceChange("bemused", 1)
                                                ch_l "Yeah, you look like you've had enough. We can take a break. . ."   
                                                ch_l ". . .for now."
                                                $ LauraX.Statup("Inbt", 30, 2)
                                                $ LauraX.Statup("Inbt", 50, 1)    
                            $ LauraX.FaceChange()
                    else:
                                                ch_l "Ok, fine."
                        
                    call Sex_Over  
                    return
        if LauraX.Loc != bg_current:
            call Set_The_Scene
            call Trig_Reset
            return
        if not MultiAction:    
            call Set_The_Scene
            ch_l "That's all. . . for now at least."
            $ LauraX.OCount = 0
            call Trig_Reset
            return
        call GirlsAngry
        jump Laura_SexMenu
# end Laura_SexMenu //////////////////////////////////////////////////////////////////////            



##  LauraX.Masturbating //////////////////////////////////////////////////////////////////////
# Cnt 1 means she's seen you, Cnt 0 means she hasn't.
label Laura_Masturbate: #(Situation = Situation):
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(LauraX)
    if LauraX.Mast:
        $ Tempmod += 10
    if LauraX.SEXP >= 50:
        $ Tempmod += 25
    elif LauraX.SEXP >= 30:
        $ Tempmod += 15
    elif LauraX.SEXP >= 15:
        $ Tempmod += 5
    if LauraX.Lust >= 90:
        $ Tempmod += 20
    elif LauraX.Lust >= 75:
        $ Tempmod += 5
    if "exhibitionist" in LauraX.Traits:      
        $ Tempmod += (3*Taboo) 
    if "dating" in LauraX.Traits or "sex friend" in LauraX.Petnames:
        $ Tempmod += 10
    elif "ex" in LauraX.Traits:
        $ Tempmod -= 40  
    if LauraX.ForcedCount and not LauraX.Forced:        
        $ Tempmod -= 5 * LauraX.ForcedCount   
        
    $ Approval = ApprovalCheck(LauraX, 1300, TabM = 2) # 120, 135, 150, Taboo -80(200)
    
    $ LauraX.DrainWord("unseen",1,0) #She sees you, so remove unseens
    
    if Situation == "join":       # This triggers if you ask to join in        
                if Approval > 1 or (Approval and LauraX.Lust >= 50):
                    menu:        
                        extend ""
                        "Would you like some help? I could lend some helping hands. . ."  if Player.Semen and LauraX.Action:
                                $ LauraX.Statup("Love", 90, 1)
                                $ LauraX.Statup("Obed", 50, 2)
                                $ LauraX.FaceChange("sexy")
                                ch_l "Huh. Well I guess you could work the top?"                  
                                $ LauraX.Statup("Obed", 70, 2)
                                $ LauraX.Statup("Inbt", 70, 1)
                                $ Trigger2 = "fondle breasts"
                                $ LauraX.Mast += 1
                                jump Laura_M_Cycle
                        "Would you like some help? I could. . . up to you, I guess." if Player.Semen and LauraX.Action:
                                $ LauraX.Statup("Love", 70, 2)
                                $ LauraX.Statup("Love", 90, 1)
                                $ LauraX.FaceChange("sexy")
                                ch_l "Yeah, I guess? . ."                
                                $ LauraX.Statup("Obed", 70, 2)
                                $ LauraX.Statup("Inbt", 70, 1)
                                $ D20 = renpy.random.randint(1, 20)
                                if D20 > 10:
                                    $ Trigger2 = "fondle breasts"
                                else:
                                    $ Trigger2 = "suck breasts"
                                $ LauraX.Mast += 1
                                jump Laura_M_Cycle
                        "Why don't we take care of each other?" if Player.Semen and LauraX.Action:
                                $ LauraX.FaceChange("sexy")
                                ch_l "Like what?"                    
                                $ renpy.pop_call()          #removes the call to this label 
                                return                      #returns to sexmenu=
                        "You look like you have things well in hand. . .":
                                if LauraX.Lust >= 50:
                                    $ LauraX.Statup("Love", 70, 2)
                                    $ LauraX.Statup("Love", 90, 1)      
                                    $ LauraX.FaceChange("sexy")
                                    ch_l "I am getting pretty close. . ."                    
                                    $ LauraX.Statup("Obed", 80, 3)
                                    $ LauraX.Statup("Inbt", 80, 5)  
                                    jump Laura_M_Cycle
                                elif ApprovalCheck(LauraX, 1200):
                                    $ LauraX.FaceChange("sly")                        
                                    ch_l "Yeah. . . but I can take a break. . ."
                                else:
                                    $ LauraX.FaceChange("angry")
                                    ch_l "-until you messed it up."
                                    
                #else: You've failed all checks so she kicks you out.
                $ LauraX.ArmPose = 1  
                $ LauraX.OutfitChange()  
                $ LauraX.Action -= 1
                $ Player.Statup("Focus", 50, 30)  
                call Checkout(1)
                $ Line = 0
                $ Situation = 0      
                $ renpy.pop_call()          #removes the call to this label 
                if Approval:     
                        $ LauraX.FaceChange("bemused", 2)
                        if bg_current == "bg laura":
                            ch_l "Why are you in my room?"   
                        else:
                            ch_l "I wasn't expecting company. . ." 
                        $ LauraX.Blush = 1
                else:
                        $ LauraX.Statup("Love", 200, -5)
                        $ LauraX.FaceChange("angry")
                        $ LauraX.RecentActions.append("angry")
                        $ LauraX.DailyActions.append("angry")  
                        if bg_current == "bg laura":
                            ch_l "I was kinda busy, so get out."
                            "[LauraX.Name] kicks you out of her room."
                            $ renpy.pop_call()
                            jump Campus_Map  
                        else:
                            ch_l "I'm getting out of here, but maybe knock next time."
                            call Remove_Girl(LauraX)
                return                      #returns to sexmenu, which returns to original    
    #End of "Join" option
    
    
    
    if Situation == LauraX:                                                                  #Laura auto-starts   
                if Approval > 2:                                                      # fix, add laura auto stuff here
                        if LauraX.PantsNum() == 5:
                            "[LauraX.Name]'s hand snakes down her body, and hikes up her skirt."
                            $ LauraX.Upskirt = 1
                        elif LauraX.PantsNum() >= 6:
                            "[LauraX.Name] slides her hand down her body and into her pants."  
                        elif LauraX.HoseNum() >= 5:
                            "[LauraX.Name]'s hand slides down her body and under her [LauraX.Hose]."
                        elif LauraX.Panties:                
                            "[LauraX.Name]'s hand slides down her body and under her [LauraX.Panties]."
                        else:
                            "[LauraX.Name]'s hand slides down her body and begins to caress her pussy."
                        $ LauraX.SeenPanties = 1
                        call Laura_First_Bottomless(1)
                        "She starts to slowly rub herself."
                        menu:
                            "What do you do?"
                            "Nothing.":                    
                                    $ LauraX.Statup("Inbt", 80, 3) 
                                    $ LauraX.Statup("Inbt", 60, 2)
                                    "[LauraX.Name] begins to masturbate."
                            "Go for it.":       
                                    $ LauraX.FaceChange("sexy, 1")                    
                                    $ LauraX.Statup("Inbt", 80, 3) 
                                    ch_p "That is so sexy, [LauraX.Pet]."
                                    $ LauraX.NameCheck() #checks reaction to petname
                                    "You lean back and enjoy the show."
                                    $ LauraX.Statup("Love", 80, 1)
                                    $ LauraX.Statup("Obed", 90, 1)
                                    $ LauraX.Statup("Obed", 50, 2)
                            "Ask her to stop.":
                                    $ LauraX.FaceChange("surprised")       
                                    $ LauraX.Statup("Inbt", 70, 1) 
                                    ch_p "Let's not do that right now, [LauraX.Pet]."
                                    $ LauraX.NameCheck() #checks reaction to petname
                                    "[LauraX.Name] pulls her hands away from herself."
                                    $ LauraX.OutfitChange()
                                    $ LauraX.Statup("Obed", 90, 1)
                                    $ LauraX.Statup("Obed", 50, 1)
                                    $ LauraX.Statup("Obed", 30, 2)
                                    return            
                        jump Laura_M_Prep
                else:                
                        $ Tempmod = 0                               # fix, add laura auto stuff here
                        $ Trigger2 = 0
                return            
    #End if Laura intitiates this action
    
    #first time
    if not LauraX.Mast:                                                                
            $ LauraX.FaceChange("surprised", 1)
            $ LauraX.Mouth = "kiss"
            ch_l "So you want me to masturbate while you watch?"
            if LauraX.Forced:
                $ LauraX.FaceChange("sad")
                ch_l "And you {i}just{/i} want to watch. . ."
            
            
    #First time dialog             
    if not LauraX.Mast and Approval:                                                      
            if LauraX.Forced: 
                $ LauraX.FaceChange("sad")
                $ LauraX.Statup("Love", 70, -3, 1)
                $ LauraX.Statup("Love", 20, -2, 1)
            elif LauraX.Love >= LauraX.Obed and LauraX.Love >= LauraX.Inbt:
                $ LauraX.FaceChange("sexy")
                $ LauraX.Brows = "sad"
                $ LauraX.Mouth = "smile" 
                ch_l "I don't know, are you sure?"          
            elif LauraX.Obed >= LauraX.Inbt:
                $ LauraX.FaceChange("normal")
                ch_l "If that's what you're into. . ."            
            else: # Uninhibited 
                $ LauraX.FaceChange("sad")
                $ LauraX.Mouth = "smile"             
                ch_l "I do have some free time. . ."     
    
    
    #Second time+ initial dialog
    elif Approval:                                                                       
            if LauraX.Forced: 
                $ LauraX.FaceChange("sad")
                $ LauraX.Statup("Love", 70, -3, 1)
                $ LauraX.Statup("Love", 20, -2, 1)
                ch_l "Hmm, again?"  
            elif Approval and "masturbation" in LauraX.RecentActions:
                $ LauraX.FaceChange("sexy", 1)
                ch_l "I have built up some more tension. . ."    
                jump Laura_M_Prep
            elif Approval and "masturbation" in LauraX.DailyActions:
                $ LauraX.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Did you enjoy that?",       
                    "Didn't get enough earlier?",
                    "I liked having an audience. . ."]) 
                ch_l "[Line]"            
            elif LauraX.Mast < 3:        
                $ LauraX.FaceChange("sexy", 1)
                $ LauraX.Brows = "confused"
                ch_l "Did you. . . like it last time?"       
            else:       
                $ LauraX.FaceChange("sexy", 1)
                $ LauraX.ArmPose = 2
                $ Line = renpy.random.choice(["You like to watch.",                 
                    "Again?",                 
                    "You really like to watch me.",
                    "You want me to masturbate again?"]) 
                ch_l "[Line]"
                $ Line = 0
    #End second time+ initial dialog
    
    #If she's into it. . .  
    if Approval >= 2:                                                                                
            if LauraX.Forced:
                $ LauraX.FaceChange("sad")
                $ LauraX.Statup("Obed", 90, 1)
                $ LauraX.Statup("Inbt", 60, 1)
                ch_l "Whatever. . ." 
            else:
                $ LauraX.FaceChange("sexy", 1)
                $ LauraX.Statup("Love", 90, 1)
                $ LauraX.Statup("Inbt", 50, 3) 
                $ Line = renpy.random.choice(["Huh. Ok.",                 
                    "Couldn't hurt. . .",
                    "Allright.", 
                    "Sure.",
                    "Heh, ok."]) 
                ch_l "[Line]"
                $ Line = 0
            $ LauraX.Statup("Obed", 20, 1)
            $ LauraX.Statup("Obed", 60, 1)
            $ LauraX.Statup("Inbt", 70, 2) 
            jump Laura_M_Prep   
            
    #If she's not into it, but maybe. . .    
    else:                                                                                       
        menu:
            ch_l "I don't know that I want to do that right now."
            "Maybe later?":
                    $ LauraX.FaceChange("sexy", 1)  
                    if LauraX.Lust > 70:                        
                        ch_l "I probably will be, but not with an audience."
                    else:
                        ch_l "Hmm, maybe. . ."
                    $ LauraX.Statup("Love", 80, 2)
                    $ LauraX.Statup("Inbt", 70, 2)               
                    return
            "You look like you could use it. . .":             
                    if Approval:
                        $ LauraX.FaceChange("sexy")     
                        $ LauraX.Statup("Obed", 90, 2)
                        $ LauraX.Statup("Obed", 50, 2)
                        $ LauraX.Statup("Inbt", 70, 3) 
                        $ LauraX.Statup("Inbt", 40, 2) 
                        $ Line = renpy.random.choice(["Huh. Ok.",                 
                                "Couldn't hurt. . .",
                                "Allright.", 
                                "Sure.",
                                "Heh, ok."]) 
                        ch_l "[Line]"
                        $ Line = 0                   
                        jump Laura_M_Prep
                    
            "Just get at it already.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(LauraX, 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                    if Approval > 1 or (Approval and LauraX.Forced):
                        $ LauraX.FaceChange("sad")
                        $ LauraX.Statup("Love", 70, -5, 1)
                        $ LauraX.Statup("Love", 200, -5)                 
                        ch_l "Whatever."  
                        $ LauraX.Statup("Obed", 80, 4)
                        $ LauraX.Statup("Inbt", 80, 1) 
                        $ LauraX.Statup("Inbt", 60, 3)  
                        $ LauraX.Forced = 1  
                        jump Laura_M_Prep
                    else:                              
                        $ LauraX.Statup("Love", 200, -20)     
                        $ LauraX.RecentActions.append("angry")
                        $ LauraX.DailyActions.append("angry")
    # end of asking her to do it
    
    #She refused all offers.
    $ LauraX.ArmPose = 1                
    if LauraX.Forced:
            $ LauraX.FaceChange("angry", 1)
            ch_l "This is just too weird for me."
            $ LauraX.Statup("Lust", 90, 5)         
            if LauraX.Love > 300:
                $ LauraX.Statup("Love", 70, -2)
            $ LauraX.Statup("Obed", 50, -2)    
            $ LauraX.RecentActions.append("angry")
            $ LauraX.DailyActions.append("angry")   
            $ LauraX.RecentActions.append("no masturbation")                      
            $ LauraX.DailyActions.append("no masturbation") 
            return
    elif Taboo:                             # she refuses and this is too public a place for her
            $ LauraX.FaceChange("angry", 1)          
            $ LauraX.DailyActions.append("tabno") 
            ch_l "I couldn't do that in public."     
            $ LauraX.Statup("Lust", 90, 5)  
            $ LauraX.Statup("Obed", 50, -3)    
            return                
    elif LauraX.Mast:
            $ LauraX.FaceChange("sad") 
            ch_l "I'm not into it right now."     
    else:
            $ LauraX.FaceChange("normal", 1)
            ch_l "Um, no."  
    $ LauraX.RecentActions.append("no masturbation")                      
    $ LauraX.DailyActions.append("no masturbation") 
    $ Tempmod = 0 
    return

label Laura_M_Prep: 
    $ LauraX.Upskirt = 1    
    $ LauraX.PantiesDown = 1 
    call Laura_First_Bottomless(1)
    call Set_The_Scene(Dress=0)   
    
    #if she hasn't seen you yet. . .
    if "unseen" in LauraX.RecentActions:
            $ LauraX.FaceChange("sexy")
            $ LauraX.Eyes = "closed"
            $ LauraX.ArmPose = 2
            "You see [LauraX.Name] leaning back, masturbating. You don't think she's noticed you yet."
    else:    
            $ LauraX.FaceChange("sexy")
            $ LauraX.ArmPose = 2
            "[LauraX.Name] lays back and starts to toy with herself."
            if not LauraX.Mast:#First time        
                    if LauraX.Forced:
                        $ LauraX.Statup("Love", 90, -20)
                        $ LauraX.Statup("Obed", 70, 45)
                        $ LauraX.Statup("Inbt", 80, 35) 
                    else:
                        $ LauraX.Statup("Love", 90, 15)
                        $ LauraX.Statup("Obed", 70, 35)
                        $ LauraX.Statup("Inbt", 80, 40)  
        
    
    $ Trigger = "masturbation"   
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0 
    $ Line = 0
    if Taboo:
        $ LauraX.DrainWord("tabno")
    $ LauraX.DrainWord("no masturbation")
    $ LauraX.RecentActions.append("masturbation")                      
    $ LauraX.DailyActions.append("masturbation") 
            
label Laura_M_Cycle:      
    if Situation == "join":
        $ renpy.pop_call() 
        $ Situation = 0 
        
    while Round >=0:  
        call Laura_Pos_Reset("masturbation")
        call Shift_Focus(LauraX) 
        $ LauraX.LustFace()   
        if "unseen" in LauraX.RecentActions and LauraX.Loc == bg_current:  
                $ LauraX.Eyes = "closed"
                if LauraX.ScentTimer >= 3:
                        $ LauraX.ScentTimer = 0
                        "[LauraX.Name]'s nose twitches and she seems to be sniffing the air."
                        jump Laura_M_Interupted
                $ LauraX.ScentTimer += 1
        
        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0
            
        if  Player.Focus < 100:                                                    
                    #Player Command menu                                        
                    menu:
                        "Keep Watching.":
                                pass
                                
                        "[LauraX.Name]. . .[[jump in]" if "unseen" not in LauraX.RecentActions and LauraX.Loc == bg_current:                 
                                "[LauraX.Name] slows what she's doing with a sly grin."
                                ch_l "Are you enjoying this?"
                                $ Situation = "join"
                                call Laura_Masturbate               
                        "\"Ahem. . .\"" if "unseen" in LauraX.RecentActions and LauraX.Loc == bg_current:  
                                jump Laura_M_Interupted    
                                                   
                        "Start jack'in it." if Trigger2 != "jackin":
                                call Jackin(LauraX)                
                        "Stop jack'in it." if Trigger2 == "jackin":
                                $ Trigger2 = 0    
                                            
                        "Slap her ass" if LauraX.Loc == bg_current:    
                                if "unseen" in LauraX.RecentActions:
                                        "You smack [LauraX.Name] firmly on the ass!"
                                        jump Laura_M_Interupted                                          
                                else:
                                        call Slap_Ass(LauraX)                                        
                                        $ Cnt += 1
                                        $ Round -= 1    
                                        jump Laura_M_Cycle  
                           
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
                                    "Offhand action" if LauraX.Loc == bg_current:
                                            if LauraX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ LauraX.Action -= 1
                                            else:
                                                ch_l "Maybe we could finish this up for now?"  
                                                           
                                    "Threesome actions (locked)" if not Partner or "unseen" in LauraX.RecentActions or LauraX.Loc != bg_current: 
                                        pass
                                    "Threesome actions" if Partner and "unseen" not in LauraX.RecentActions and LauraX.Loc == bg_current:   
                                        menu:
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(LauraX)   
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(LauraX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_M_Cycle 
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_M_Cycle 
                                            "Never mind":
                                                        jump Laura_M_Cycle 
                                    "undress [LauraX.Name]":
                                            if "unseen" in LauraX.RecentActions:
                                                    ch_p "Oh, yeah, take it off. . ."
                                                    jump Laura_M_Interupted
                                            else:                                        
                                                    call Girl_Undress(LauraX)   
                                    "Clean up [LauraX.Name] (locked)" if not LauraX.Spunk:
                                            pass  
                                    "Clean up [LauraX.Name]" if LauraX.Spunk:
                                            if "unseen" in LauraX.RecentActions:
                                                    ch_p "You've got a little something on you. . ."
                                                    jump Laura_M_Interupted
                                            else:                      
                                                    call Girl_Cleanup(LauraX,"ask")                                         
                                    "Never mind":
                                                    jump Laura_M_Cycle                               
                         
                        "Back to Sex Menu" if MultiAction and LauraX.Loc == bg_current: 
                                    ch_p "Let's try something else."
                                    call Laura_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Laura_M_Interupted
                        "End Scene" if not MultiAction or LauraX.Loc != bg_current: 
                                    ch_p "Let's stop for now."
                                    call Laura_Pos_Reset
                                    $ Line = 0
                                    jump Laura_M_Interupted
        #End menu (if Line)
        
        call Shift_Focus(LauraX)  
        call Sex_Dialog(LauraX,Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1
    
        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        
        if Player.Focus >= 100 or LauraX.Lust >= 100:   
                    #If you can cum:
                    if Player.Focus >= 100:
                        if "unseen" not in LauraX.RecentActions: 
                            #if she knows you're there
                            call Player_Cumming(LauraX)
                            if "angry" in LauraX.RecentActions:  
                                call Laura_Pos_Reset
                                return    
                            $ LauraX.Statup("Lust", 200, 5) 
                            if 100 > LauraX.Lust >= 70 and LauraX.OCount < 2:             
                                $ LauraX.RecentActions.append("unsatisfied")                      
                                $ LauraX.DailyActions.append("unsatisfied") 
                            $ Line = "came"
                        else: #If she wasn't aware you were there
                            "You grunt and try to hold it in."
                            $ Player.Focus = 95
                            if LauraX.Loc == bg_current:
                                    jump Laura_M_Interupted
     
                    #If Laura can cum
                    if LauraX.Lust >= 100:                                               
                        call Girl_Cumming(LauraX)
                        if LauraX.Loc == bg_current:
                                jump Laura_M_Interupted
                       
                    if Line == "came": 
                        $ Line = 0
                        if not Player.Semen:
                            "You're emptied out, you should probably take a break."
                            $ Trigger2 = 0 if Trigger2 == "jackin" else Trigger2
                            
                            
                        if "unsatisfied" in LauraX.RecentActions:#And Laura is unsatisfied,  
                            "[LauraX.Name] still seems a bit unsatisfied with the experience."
                            menu:
                                "Let her keep going?"
                                "Yes, keep going for a bit.":
                                    $ Line = "You let her get back into it" 
                                    jump Laura_M_Cycle  
                                "No, I'm done.":
                                    "You ask her to stop."
                                    return 
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)                            
        #End orgasm
        
        if "unseen" in LauraX.RecentActions:
                if Round == 10:
                    "It's getting a bit late, [LauraX.Name] will probably be wrapping up soon."  
                elif Round == 5:
                    "She's definitely going to stop soon."
        else:
                if LauraX.Loc == bg_current:
                        call Escalation(LauraX) #sees if she wants to escalate things
        
                if Round == 10:
                    ch_l "We might want to wrap this up, it's getting late."  
                    $ LauraX.Lust += 10
                elif Round == 5:
                    ch_l "Five minutes, maybe."     
                    $ LauraX.Lust += 25   
    
    #Round = 0 loop breaks
    $ LauraX.FaceChange("bemused", 0)
    $ Line = 0
    if "unseen" not in LauraX.RecentActions:
        ch_l "Ok, I'm kinda done for now, I need a break."
    
label Laura_M_Interupted:
    
    # If she hasn't noticed you're there before cumming
    if "unseen" in LauraX.RecentActions:                         
                $ LauraX.FaceChange("surprised", 2)
                "[LauraX.Name] stops what she's doing with a start, eyes wide."
                call Laura_First_Bottomless(1) 
                $ LauraX.FaceChange("surprised", 2)
                
                #If you've been jacking it
                if Trigger2 == "jackin":
                        ch_l "Huh."
                        ch_l "When did you get here?"
                        $ LauraX.Eyes = "down"
                        menu:
                            ch_l "And um. . . you have your penis out. . . "
                            "A while back, it was an excellent show.":   
                                    $ LauraX.FaceChange("sexy",1)
                                    $ LauraX.Statup("Obed", 50, 3)
                                    $ LauraX.Statup("Obed", 70, 2)
                                    ch_l "Really? Weird. . ."
                                    if LauraX.Love >= 800 or LauraX.Obed >= 500 or LauraX.Inbt >= 500:
                                        $ Tempmod += 10
                                        $ LauraX.Statup("Lust", 90, 5)
                                        ch_l "I um. . . you're not so bad yourself. . ."  
                                    
                            "I. . . just got here?":
                                    $ LauraX.FaceChange("angry",1)                   
                                    $ LauraX.Statup("Love", 70, 2)
                                    $ LauraX.Statup("Love", 90, 1)
                                    $ LauraX.Statup("Obed", 50, 2)
                                    $ LauraX.Statup("Obed", 70, 2)
                                    "She looks pointedly at your cock,"
                                    ch_l "Long enough to whip that out?"   
                                    if LauraX.Love >= 800 or LauraX.Obed >= 500 or LauraX.Inbt >= 500:
                                            $ Tempmod += 10
                                            $ LauraX.Statup("Lust", 90, 5)
                                            $ LauraX.FaceChange("bemused", 1)
                                            ch_l "It was really that interesting?"   
                                    else:
                                            $ Tempmod -= 10
                                            $ LauraX.Statup("Lust", 200, -5)
                        call Seen_First_Peen(LauraX,Partner) 
                                    
                #you haven't been jacking it                    
                else:         
                        ch_l "Huh."
                        ch_l "When did you get here?"
                        menu:
                            extend ""
                            "A while back.":   
                                    $ LauraX.FaceChange("sexy", 1)
                                    $ LauraX.Statup("Obed", 50, 3)
                                    $ LauraX.Statup("Obed", 70, 2)
                                    ch_l "I must have put on a show. . ."
                            "I just got here.":
                                    $ LauraX.FaceChange("bemused", 1)
                                    $ LauraX.Statup("Love", 70, 2)
                                    $ LauraX.Statup("Love", 90, 1)                    
                                    ch_l "Uh-huh. . ."   
                                    $ LauraX.Statup("Obed", 50, 2)
                                    $ LauraX.Statup("Obed", 70, 2)    
                                
                $ LauraX.DrainWord("unseen",1,0) #She sees you, so remove unseens
                $ LauraX.Mast += 1
                if Round <= 10:
                    ch_l "I kinda needed a break anyway. . ."
                    return
                $ Situation = "join"        
                call Laura_Masturbate
                "error: report this if you see it."
                return #should be redundant
    #End Unseen
    
    #else, if She's seen you already    
    $ LauraX.Action -= 1
    $ LauraX.Mast += 1    
    call Checkout
    if Situation == "shift":        
        $ Situation = 0
        return
    $ Situation = 0
        
    if Partner == EmmaX:
        call Partner_Like(LauraX,3)
    else:
        call Partner_Like(LauraX,2)
    
    if LauraX.Loc != bg_current:
        return
        
    if Round <= 10:
            ch_l "I need a minute here. . ."
            return
    $ LauraX.FaceChange("sexy", 1)
    if LauraX.Lust < 20:
        ch_l "I guess that worked out, how about you?"
    else:
        ch_l "So, what next?"
    menu:
        extend ""
        "Well, I have something you could take care of. . ." if Player.Semen and LauraX.Action:
                $ Situation = "shift"
                return   
        "You could just keep going. . ." if Player.Semen:
                $ LauraX.FaceChange("sly")
                if LauraX.Action and Round >= 10:
                    ch_l "Ok. . ."
                    jump Laura_M_Cycle
                else:
                    ch_l "I need a minute here. . ."
        "I'm good here. [[Stop]":  
                if LauraX.Love < 800 and LauraX.Inbt < 500 and LauraX.Obed < 500:
                    $ LauraX.OutfitChange()
                $ LauraX.FaceChange("normal")
                $ LauraX.Brows = "confused"
                ch_l "Ok."
                $ LauraX.Brows = "normal" 
        "You should probably stop for now." if LauraX.Lust > 30:
                $ LauraX.FaceChange("angry")
                ch_l "Hrmm."
    return
    
## end LauraX.Masturbating ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

  
            
# Start Laura Sex pose //////////////////////////////////////////////////////////////////////////////////
# LauraX.Sex_P //////////////////////////////////////////////////////////////////////

label Laura_Sex_P:  
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(LauraX)
    if LauraX.Sex >= 7: # She loves it
        $ Tempmod += 15
    elif LauraX.Sex >= 3: #You've done it before several times
        $ Tempmod += 12
    elif LauraX.Sex: #You've done it before
        $ Tempmod += 10    
        
    if LauraX.Addict >= 75 and (LauraX.CreamP + LauraX.CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 20
    elif LauraX.Addict >= 75:
        $ Tempmod += 15
        
    if LauraX.Lust > 85:
        $ Tempmod += 10
    elif LauraX.Lust > 75: #She's really horny
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 10 
    if "exhibitionist" in LauraX.Traits:    
        $ Tempmod += (4*Taboo)      
    if "dating" in LauraX.Traits or "sex friend" in LauraX.Petnames:
        $ Tempmod += 10
    elif "ex" in LauraX.Traits:
        $ Tempmod -= 40
    if LauraX.ForcedCount and not LauraX.Forced:
        $ Tempmod -= 5 * LauraX.ForcedCount
    
    
        
    if Taboo and "tabno" in LauraX.DailyActions:        
        $ Tempmod -= 10 
        
    if "no sex" in LauraX.DailyActions:    
        $ Tempmod -= 15 if "no sex" in LauraX.RecentActions else 5                  
             
        
    $ Approval = ApprovalCheck(LauraX, 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)
        
    if Situation == "auto":   
                call Laura_Sex_Launch("L")   
                if LauraX.PantsNum() == 5:
                    "You push [LauraX.Name] onto her back, sliding her skirt up as you go."
                    $ LauraX.Upskirt = 1                
                elif LauraX.PantsNum() >= 6:
                    "You push [LauraX.Name] onto her back, sliding her pants down as you do."    
                    $ LauraX.Upskirt = 1    
                else:
                    "You push [LauraX.Name] onto her back."
                $ LauraX.SeenPanties = 1
                "You rub the tip of your cock against her moist slit."        
                $ LauraX.FaceChange("surprised", 1)
                
                if (LauraX.Sex and Approval) or (Approval > 1):
                    #this is not the first time you've had sex, or she's into it         
                    "[LauraX.Name] glances down and then breaks into a smile."
                    $ LauraX.FaceChange("sly")
                    $ LauraX.Statup("Obed", 70, 3)
                    $ LauraX.Statup("Inbt", 50, 3) 
                    $ LauraX.Statup("Inbt", 70, 1) 
                    ch_l "Fine by me, [LauraX.Petname]."            
                    jump Laura_SexPrep         
                else:                                                                                                            
                    #she's questioning it
                    $ LauraX.Brows = "angry"                
                    menu:
                        ch_l "Oh, taking it all the way, are we?" 
                        "Sorry, sorry! Never mind.":
                            if Approval:     
                                    $ LauraX.FaceChange("sexy", 1)
                                    $ LauraX.Statup("Obed", 70, 3)
                                    $ LauraX.Statup("Inbt", 50, 3) 
                                    $ LauraX.Statup("Inbt", 70, 1) 
                                    ch_l "No no, not a problem. . ."
                                    jump Laura_SexPrep
                            else:
                                    "You pull back before you really get it in."                    
                                    $ LauraX.FaceChange("bemused", 1)
                                    if LauraX.Sex:
                                        ch_l "Maybe ask first, [LauraX.Petname]?" 
                                    else:
                                        ch_l "Maybe if you'd asked first. . ."
                        "Just fucking.":                    
                            $ LauraX.Statup("Love", 80, -10, 1)  
                            $ LauraX.Statup("Love", 200, -10)
                            "You press inside some more."                              
                            $ LauraX.Statup("Obed", 70, 3)
                            $ LauraX.Statup("Inbt", 50, 3) 
                            if not ApprovalCheck(LauraX, 700, "O", TabM=1):   #Checks if Obed is 700+                          
                                $ LauraX.FaceChange("angry")
                                "[LauraX.Name] shoves you away and backhands you in the face."
                                ch_l "Dick."
                                ch_l "Don't push me."                                                  
                                $ LauraX.Statup("Love", 50, -10, 1)                        
                                $ LauraX.Statup("Obed", 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                call Laura_Sex_Reset
                                $ LauraX.RecentActions.append("angry")
                                $ LauraX.DailyActions.append("angry")                    
                            else:
                                $ LauraX.FaceChange("sad")
                                "[LauraX.Name] doesn't seem to be into this, you're lucky she's so obedient."                        
                                jump Laura_SexPrep
                return   
    #End Auto
    
   
    if not LauraX.Sex and "no sex" not in LauraX.RecentActions:                           
            #first time    
            $ LauraX.FaceChange("surprised", 1)
            $ LauraX.Mouth = "kiss"
            ch_l "Huh, you wanna fuck me? . . "    
            if LauraX.Forced:
                $ LauraX.FaceChange("sad")
                ch_l "Pretty bold of you. . ."
            
            
    if not LauraX.Sex and Approval:                                                  
            #First time dialog        
            if LauraX.Forced: 
                $ LauraX.FaceChange("sad")
                $ LauraX.Statup("Love", 70, -30, 1)
                $ LauraX.Statup("Love", 20, -20, 1)
            elif LauraX.Love >= (LauraX.Obed + LauraX.Inbt):
                $ LauraX.FaceChange("sexy")
                $ LauraX.Brows = "sad"
                $ LauraX.Mouth = "smile" 
                ch_l "Well, you look so cute when you ask. . ."            
            elif LauraX.Obed >= LauraX.Inbt:
                $ LauraX.FaceChange("normal")
                ch_l "Yes, [LauraX.Petname]. . ."            
            elif LauraX.Addict >= 50:
                $ LauraX.FaceChange("manic", 1)
                ch_l "Sounds fun. . ."
            else: # Uninhibited 
                $ LauraX.FaceChange("sad")
                $ LauraX.Mouth = "smile"             
                ch_l "I was hoping you'd ask. . ."   
            #End first time dialog
            
    elif Approval:                                                                      
            #Second time+ dialog        
            $ LauraX.FaceChange("sexy", 1)
            if LauraX.Forced: 
                $ LauraX.FaceChange("sad")
                $ LauraX.Statup("Love", 70, -3, 1)
                $ LauraX.Statup("Love", 20, -2, 1)
                ch_l "I hope I don't wear you out." 
            elif not Taboo and "tabno" in LauraX.DailyActions:        
                ch_l "Yeah, this is more covert."        
            elif "sex" in LauraX.RecentActions:
                ch_l "Again? Your funeral." 
                jump Laura_SexPrep
            elif "sex" in LauraX.DailyActions:
                $ Line = renpy.random.choice(["Back again?",                 
                    "You'd like another round?",                 
                    "I must be better than I thought.", 
                    "Didn't get enough earlier?",
                    "Your funeral, " + LauraX.Petname + "."]) 
                ch_l "[Line]"
            elif LauraX.Sex < 3:        
                $ LauraX.Brows = "confused"
                $ LauraX.Mouth = "kiss"
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
            if LauraX.Forced:
                $ LauraX.FaceChange("sad")
                $ LauraX.Statup("Obed", 90, 1)
                $ LauraX.Statup("Inbt", 60, 1)
                ch_l "Ok, fine. Just make it good."  
            elif "no sex" in LauraX.DailyActions:               
                ch_l "Ok, whatever. . ."
            else:
                $ LauraX.FaceChange("sexy", 1)
                $ LauraX.Statup("Love", 90, 1)
                $ LauraX.Statup("Inbt", 50, 3) 
                $ Line = renpy.random.choice(["Well. . . fine, let's do it.",                 
                    "Sure.", 
                    "We could, I guess.",
                    "Hmmm, sure.",
                    "Sounds fun."]) 
                ch_l "[Line]"
                $ Line = 0
            $ LauraX.Statup("Obed", 20, 1)
            $ LauraX.Statup("Obed", 60, 1)
            $ LauraX.Statup("Inbt", 70, 2) 
            jump Laura_SexPrep   
    
    else:                                                                               
            #She's not into it, but maybe. . .    
            $ LauraX.FaceChange("angry")       
            if "no sex" in LauraX.RecentActions:  
                ch_l "Sorry, [LauraX.Petname] \"no.\""
            elif Taboo and "tabno" in LauraX.DailyActions and "no sex" in LauraX.DailyActions:  
                ch_l "I told you. . . this place is too exposed." 
            elif "no sex" in LauraX.DailyActions:       
                ch_l "I just told you \"no.\""
            elif Taboo and "tabno" in LauraX.DailyActions:  
                ch_l "I already told you this is too public!"     
            elif not LauraX.Sex:
                $ LauraX.FaceChange("bemused")
                ch_l "Oh, you have no idea what you're in for. . ."
            else:
                $ LauraX.FaceChange("bemused")
                ch_l "Maybe later? . ."
            menu:
                extend ""
                "Sorry, never mind." if "no sex" in LauraX.DailyActions:
                        $ LauraX.FaceChange("bemused")
                        ch_l "Well, you are persistant."
                        return
                "Maybe later?" if "no sex" not in LauraX.DailyActions:
                        $ LauraX.FaceChange("sexy")  
                        ch_l "Probably. . ."
                        $ LauraX.Statup("Love", 80, 2)
                        $ LauraX.Statup("Inbt", 70, 2)   
                        if Taboo:                    
                            $ LauraX.RecentActions.append("tabno")                      
                            $ LauraX.DailyActions.append("tabno") 
                        $ LauraX.RecentActions.append("no sex")                      
                        $ LauraX.DailyActions.append("no sex")            
                        return
                "I think you'd enjoy it as much as I would. . .":             
                        if Approval:
                            $ LauraX.FaceChange("sexy")     
                            $ LauraX.Statup("Obed", 90, 2)
                            $ LauraX.Statup("Obed", 50, 2)
                            $ LauraX.Statup("Inbt", 70, 3) 
                            $ LauraX.Statup("Inbt", 40, 2) 
                            $ Line = renpy.random.choice(["Yeah, probably. . .",     
                                "I guess. . .", 
                                "Good point. . ."]) 
                            ch_l "[Line]"
                            $ Line = 0                   
                            jump Laura_SexPrep       
                "Just deal with it.":                                               # Pressured into it
                        $ Approval = ApprovalCheck(LauraX, 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
                        if Approval > 1 or (Approval and LauraX.Forced):
                            $ LauraX.FaceChange("sad")
                            $ LauraX.Statup("Love", 70, -5, 1)
                            $ LauraX.Statup("Love", 200, -5)                 
                            ch_l "Fine, if it'll shut you up."  
                            $ LauraX.Statup("Obed", 80, 4)
                            $ LauraX.Statup("Inbt", 80, 1) 
                            $ LauraX.Statup("Inbt", 60, 3)  
                            $ LauraX.Forced = 1  
                            jump Laura_SexPrep
                        else:                          
                            $ LauraX.Statup("Love", 200, -20)   
                            $ LauraX.RecentActions.append("angry")
                            $ LauraX.DailyActions.append("angry")  
                #end menu
    #end Approval check
    
    #She refused all offers.
    $ LauraX.ArmPose = 1  
    if "no sex" in LauraX.DailyActions:
        ch_l "Don't push me." 
        $ LauraX.RecentActions.append("angry")
        $ LauraX.DailyActions.append("angry")   
    elif LauraX.Forced:
        $ LauraX.FaceChange("angry", 1)
        ch_l "I'm over taking orders."
        $ LauraX.Statup("Lust", 200, 5) 
        if LauraX.Love > 300:   
                $ LauraX.Statup("Love", 70, -2) 
        $ LauraX.Statup("Obed", 50, -2)     
        $ LauraX.RecentActions.append("angry")
        $ LauraX.DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        $ LauraX.FaceChange("angry", 1)
        $ LauraX.RecentActions.append("tabno")                      
        $ LauraX.DailyActions.append("tabno") 
        ch_l "This place is way too exposed."     
        $ LauraX.Statup("Lust", 200, 5)  
        $ LauraX.Statup("Obed", 50, -3)
    elif LauraX.Sex:
        $ LauraX.FaceChange("sad") 
        ch_l "Just jack it or something."       
    else:
        $ LauraX.FaceChange("normal", 1)
        ch_l "Yeah, no."     
    $ LauraX.RecentActions.append("no sex")                      
    $ LauraX.DailyActions.append("no sex") 
    $ Tempmod = 0    
    return

label Laura_SexPrep:
    call Seen_First_Peen(LauraX,Partner,React=Situation)
    call Laura_Sex_Launch("hotdog")
             
    if Situation == LauraX:                                                                 
            #Laura auto-starts   
            $ Situation = 0
            if LauraX.PantsNum() == 5:
                "[LauraX.Name] lays back, sliding her skirt up as she does so."
                $ LauraX.Upskirt = 1
            elif LauraX.PantsNum() >= 6:
                "[LauraX.Name] lays back, sliding her [LauraX.Legs] down as she does so." 
                $ LauraX.Upskirt = 1
            else:
                "[LauraX.Name] rolls back and pulls you toward her."
            $ LauraX.SeenPanties = 1
            "She slides the tip along her pussy and seems to want you to insert it."
            menu:
                "What do you do?"
                "Go with it.":                    
                    $ LauraX.Statup("Inbt", 80, 3) 
                    $ LauraX.Statup("Inbt", 50, 2)
                    "[LauraX.Name] slides it in."
                "Praise her.":       
                    $ LauraX.FaceChange("sexy", 1)                    
                    $ LauraX.Statup("Inbt", 80, 3) 
                    ch_p "Oh yeah, [LauraX.Pet], let's do this."
                    $ LauraX.NameCheck() #checks reaction to petname
                    "Laura slides it in."
                    $ LauraX.Statup("Love", 85, 1)
                    $ LauraX.Statup("Obed", 90, 1)
                    $ LauraX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ LauraX.FaceChange("surprised")       
                    $ LauraX.Statup("Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [LauraX.Pet]."
                    $ LauraX.NameCheck() #checks reaction to petname
                    "[LauraX.Name] pulls back."
                    $ LauraX.Statup("Obed", 90, 1)
                    $ LauraX.Statup("Obed", 50, 1)
                    $ LauraX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")      
                    $ LauraX.AddWord(1,"refused","refused")  
                    return      
            $ LauraX.PantiesDown = 1  
            call Laura_First_Bottomless(1)
            
    elif Situation != "auto":
        call Bottoms_Off(LauraX) 
        
        if (LauraX.Panties and not LauraX.PantiesDown) or (LauraX.Legs and not LauraX.Upskirt) or LauraX.HoseNum() >= 6: #If she refuses to take off her pants but agreed to anal
            ch_l "Huh. . ."
            
            if (LauraX.Panties and not LauraX.PantiesDown) and (LauraX.PantsNum() > 6 and not LauraX.Upskirt):
                "She quickly drops her pants and her [LauraX.Panties]."
            elif (LauraX.Panties and not LauraX.PantiesDown) and (LauraX.PantsNum() == 6 and not LauraX.Upskirt):
                "She quickly drops her shorts and her [LauraX.Panties]."
            elif LauraX.PantsNum() > 6 and not LauraX.Upskirt:
                "She tugs her pants down, exposing her bare pussy."
            elif LauraX.PantsNum() == 6 and not LauraX.Upskirt:
                "She tugs her shorts down, exposing her bare pussy."
            elif LauraX.HoseNum() >= 6 and (LauraX.Panties and not LauraX.PantiesDown):
                "She tugs her [LauraX.Hose] and [LauraX.Panties] off."
                $ LauraX.Hose = 0
            elif LauraX.HoseNum() >= 6:
                "She tugs her [LauraX.Hose] off and drops them to the ground."
                $ LauraX.Hose = 0
            elif (LauraX.Panties and not LauraX.PantiesDown):
                "She tugs her [LauraX.Panties] off and drops them to the ground."  
            
        $ LauraX.Upskirt = 1
        $ LauraX.PantiesDown = 1       
        $ LauraX.SeenPanties = 1
        call Laura_First_Bottomless
        
        if Taboo: # Laura gets started. . .
            "[LauraX.Name] glances around to see if anyone notices what she's doing."
            if "cockout" in Player.RecentActions:
                "Then she lays back and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and lays back."
                "She slowly presses against your rigid member."
            $ LauraX.Inbt += int(Taboo/10)  
            $ LauraX.Lust += int(Taboo/5)
        else:    
            if "cockout" in Player.RecentActions:
                "[LauraX.Name] lays back and slowly presses against your rigid member."
            else:
                "[LauraX.Name] pulls down your pants and lays back."
                "She slowly presses against your rigid member."
        "She leans back a bit and your cock slides in."
                            
    else:  #if Situation == "auto"         
        if (LauraX.PantsNum() >= 6 and not LauraX.Upskirt) and (LauraX.Panties and not LauraX.PantiesDown):
            "You quickly pull down her pants and her [LauraX.Panties] and press against her slit."
        elif (LauraX.Panties and not LauraX.PantiesDown):
            "You quickly pull down her [LauraX.Panties] and press against her slit."  
        $ LauraX.Upskirt = 1
        $ LauraX.PantiesDown = 1       
        $ LauraX.SeenPanties = 1
        call Laura_First_Bottomless(1)
    
    if Player.Focus >= 50:
            ch_l "Nice to see you're ready for business. . ."
    if not LauraX.Sex:        
        if LauraX.Forced:
            $ LauraX.Statup("Love", 90, -150)
            $ LauraX.Statup("Obed", 70, 60)
            $ LauraX.Statup("Inbt", 80, 50) 
        else:
            $ LauraX.Statup("Love", 90, 30)
            $ LauraX.Statup("Obed", 70, 30)
            $ LauraX.Statup("Inbt", 80, 60) 
    
    if Situation:   
        $ renpy.pop_call() 
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ Player.Cock = "in"
    $ Trigger = "sex"
    $ Speed = 1
    if Taboo:
        $ LauraX.DrainWord("tabno")
    $ LauraX.DrainWord("no sex")
    $ LauraX.RecentActions.append("sex")                      
    $ LauraX.DailyActions.append("sex")     

label Laura_Sex_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus(LauraX)
        call Laura_Sex_Launch("sex") 
        if Speed >= 4:     
            $ Speed = 2
#            call Speed_Shift(2) 
        $ LauraX.LustFace()         
        $ Player.Cock = "in"
        $ Trigger = "sex"
        $ LauraX.Upskirt = 1
        $ LauraX.PantiesDown = 1  
        
        if  Player.Focus < 100:                                                    
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
                                    call Slap_Ass(LauraX)  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Laura_Sex_Cycle  
                                    
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
                                            if LauraX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ LauraX.Action -= 1
                                            else:
                                                ch_l "I think we could take a little break." 
                                                
                                    "Shift primary action":
                                            if LauraX.Action and MultiAction:
                                                    menu:
                                                        "How about anal?":
                                                                $ Situation = "shift"
                                                                call Laura_SexAfter
                                                                call Laura_Sex_A
                                                        "Just stick it in her ass [[without asking].":
                                                                $ Situation = "auto"
                                                                call Laura_SexAfter
                                                                call Laura_Sex_A
                                                        "Pull back to hotdog her.":
                                                                $ Situation = "pullback"
                                                                call Laura_SexAfter
                                                                call Laura_Sex_H
                                                        "Never Mind":
                                                                jump Laura_Sex_Cycle
                                            else:
                                                ch_l "I think we could take a little break." 
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask [LauraX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(LauraX)
                                            "Ask [LauraX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(LauraX) 
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0   
                                                        
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(LauraX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_Sex_Cycle 
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_Sex_Cycle 
                                            "Never mind":
                                                        jump Laura_Sex_Cycle 
                                    "undress [LauraX.Name]":
                                            call Girl_Undress(LauraX)   
                                    "Clean up [LauraX.Name] (locked)" if not LauraX.Spunk:
                                            pass  
                                    "Clean up [LauraX.Name]" if LauraX.Spunk:
                                            call Girl_Cleanup(LauraX,"ask")                                         
                                    "Never mind":
                                            jump Laura_Sex_Cycle                                    
                                                        
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Laura_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Laura_SexAfter
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Laura_Sex_Reset
                                    $ Line = 0
                                    jump Laura_SexAfter
        #End menu (if Line)              
        
        call Shift_Focus(LauraX)    
        call Sex_Dialog(LauraX,Partner)
        
        $ Cnt += 1
        $ Round -= 1     
        
        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or LauraX.Lust >= 100:   
                    #If either of you could cum    
                    if Player.Focus >= 100:
                            #If you can cum:                                                
                            call Player_Cumming(LauraX)
                            if "angry" in LauraX.RecentActions:  
                                call Laura_Sex_Reset
                                return    
                            $ LauraX.Statup("Lust", 200, 5) 
                            if 100 > LauraX.Lust >= 70 and LauraX.OCount < 2:             
                                    $ LauraX.RecentActions.append("unsatisfied")                      
                                    $ LauraX.DailyActions.append("unsatisfied") 
                            
                            if Player.Focus > 80:
                                jump Laura_SexAfter 
                            $ Line = "came"

                    if LauraX.Lust >= 100:         
                            #If you're still going at it and Laura can cum
                            call Girl_Cumming(LauraX)
                            if Situation == "shift" or "angry" in LauraX.RecentActions:
                                jump Laura_SexAfter
                       
                    if Line == "came": #ex Player.Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Laura_SexAfter
                            elif "unsatisfied" in LauraX.RecentActions:
                                #And Laura is unsatisfied,  
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ Line = "You get back into it" 
                                        jump Laura_Sex_Cycle  
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Laura_SexAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Laura_SexAfter   
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)            
        #End orgasm
        
        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0
        
        if LauraX.SEXP >= 100 or ApprovalCheck(LauraX, 1200, "LO"):
            pass
        elif Cnt == (5 + LauraX.Sex):
                    $ LauraX.Brows = "confused"
                    ch_l "So are we getting close?"   
        elif Cnt == (10 + LauraX.Sex):
                    $ LauraX.Brows = "angry"        
                    menu:
                        ch_l "Hey. . . could we. . . try something. . . else?"
                        "How about a BJ?" if LauraX.Action and MultiAction:
                                $ Situation = "shift"
                                call Laura_SexAfter
                                call Laura_Blowjob       
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."             
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ Cnt += 1
                                jump Laura_Sex_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Laura_Sex_Reset
                                $ Situation = "shift"
                                jump Laura_SexAfter
                        "No, get back down there.":                                
                                if ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 500, "O"):                        
                                    $ LauraX.Statup("Love", 200, -5)
                                    $ LauraX.Statup("Obed", 50, 3)                    
                                    $ LauraX.Statup("Obed", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    $ LauraX.FaceChange("angry", 1)   
                                    call Laura_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_l "Not with that attitude."
                                    $ LauraX.Statup("Love", 50, -3, 1)
                                    $ LauraX.Statup("Love", 80, -4, 1)
                                    $ LauraX.Statup("Obed", 30, -1, 1)                    
                                    $ LauraX.Statup("Obed", 50, -1, 1)  
                                    $ LauraX.RecentActions.append("angry")
                                    $ LauraX.DailyActions.append("angry")   
                                    jump Laura_SexAfter
        #End Count check
   
        call Escalation(LauraX) #sees if she wants to escalate things
        
        if Round == 10:
            ch_l "It's getting kinda late. . ."  
        elif Round == 5:
            ch_l "We should take a break for a minute."     
    
    #Round = 0 loop breaks
    $ LauraX.FaceChange("bemused", 0)
    $ Line = 0
    ch_l "Ok, that's enough of that for now."
    
label Laura_SexAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ Player.Sprite = 0
        $ Player.Cock = "out"
        call Laura_Sex_Reset
        
    $ LauraX.FaceChange("sexy") 
    
    $ LauraX.Sex += 1  
    $ LauraX.Action -=1
    $ LauraX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ LauraX.Addictionrate += 1        
    $ LauraX.Statup("Inbt", 30, 2) 
    $ LauraX.Statup("Inbt", 70, 1) 
        
    call Partner_Like(LauraX,3,2)
    
    if "Laura Sex Addict" in Achievements:
            pass 
            
    elif LauraX.Sex >= 10:
        $ LauraX.SEXP += 5
        $ Achievements.append("Laura Sex Addict")
        if not Situation:
            $ LauraX.FaceChange("smile", 1)
            ch_l "We're making this a regular thing, huh. . ."               
    elif LauraX.Sex == 1:            
            $LauraX.SEXP += 20        
            if not Situation: 
                if LauraX.Love >= 500 and "unsatisfied" not in LauraX.RecentActions:
                    ch_l "I can tell, I was the best you've had."
                elif LauraX.Obed <= 500 and Player.Focus <= 20:
                    $ LauraX.Mouth = "sad"
                    ch_l "Satisfied?"
    elif LauraX.Sex == 5:
            ch_l "You know, this was a good idea."
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in LauraX.RecentActions:
            $ LauraX.FaceChange("angry")
            $ LauraX.Eyes = "side"
            ch_l "Forgetting someone? . ."
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Did you[LauraX.like]want to try something else?"
    call Checkout
    return   

# End laura sex //////////////////////////////////////////////////////////////////////////////////


# Laura anal //////////////////////////////////////////////////////////////////////

label Laura_Sex_A:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(LauraX)
    if LauraX.Anal >= 7: # She loves it
        $ Tempmod += 20   
    elif LauraX.Anal >= 3: #You've done it before several times
        $ Tempmod += 17
    elif LauraX.Anal: #You've done it before
        $ Tempmod += 15 
        
    if LauraX.Addict >= 75 and (LauraX.CreamP + LauraX.CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 25
    elif LauraX.Addict >= 75: 
        $ Tempmod += 15
    
    if LauraX.Lust > 85:
        $ Tempmod += 10
    elif LauraX.Lust > 75: #She's really horny
        $ Tempmod += 5
        
    $ Tempmod += 10  # she starts out loose    
        
    if Situation == "shift":
        $ Tempmod += 10    
    if "exhibitionist" in LauraX.Traits:
        $ Tempmod += (5*Taboo) 
        
    if "dating" in LauraX.Traits or "sex friend" in LauraX.Petnames:
        $ Tempmod += 10      
    elif "ex" in LauraX.Traits:
        $ Tempmod -= 40  
    if LauraX.ForcedCount and not LauraX.Forced:
        $ Tempmod -= 5 * LauraX.ForcedCount
        
    if Taboo and "tabno" in LauraX.DailyActions:        
        $ Tempmod -= 10 
    if "no anal" in LauraX.DailyActions:               
        $ Tempmod -= 5         
        $ Tempmod -= 10 if "no anal" in LauraX.RecentActions else 0  
            
    $ Approval = ApprovalCheck(LauraX, 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)
    
    if Situation == "auto":   
            call Laura_Sex_Launch("L")   
            if LauraX.PantsNum() == 5:
                "You push [LauraX.Name] onto her back, sliding her skirt up as you go."
                $ LauraX.Upskirt = 1                
            elif LauraX.PantsNum() >= 6:
                "You push [LauraX.Name] onto her back, sliding her pants down as you do."    
                $ LauraX.Legs = 0    
            else:
                "You push [LauraX.Name] onto her back."
            $ LauraX.SeenPanties = 1
            "You press the tip of your cock against her tight rim."        
            $ LauraX.FaceChange("surprised", 1)
            call Laura_First_Bottomless(1)
            
            if (LauraX.Anal and Approval) or (Approval > 1):                                                                      
                #this is not the first time you've had sex, or she's into it    
                $ LauraX.Statup("Obed", 70, 3)
                $ LauraX.Statup("Inbt", 50, 3) 
                $ LauraX.Statup("Inbt", 70, 1) 
                "[LauraX.Name] glances down and then breaks into a smile."
                ch_l "Yeah, ok. . ."          
                jump Laura_AnalPrep         
            else:                                                                                                            
                #she's questioning it
                $ LauraX.Brows = "angry"                
                menu:
                    ch_l "Oh? A backdoor intruder?" 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            $ LauraX.FaceChange("sexy", 1)
                            $ LauraX.Statup("Obed", 70, 3)
                            $ LauraX.Statup("Inbt", 50, 3) 
                            $ LauraX.Statup("Inbt", 70, 1) 
                            ch_l "Hey, whatever floats your boat. . ."
                            ch_l "Get in there."
                            jump Laura_AnalPrep
                        "You pull back before you really get it in."                    
                        $ LauraX.FaceChange("bemused", 1)
                        
                        if LauraX.Anal:
                            ch_l "You coulda warned me. . ." 
                        else:
                            ch_l "Hey, all I expect is a little warning. . ."
                    "Just fucking.":                    
                        $ LauraX.Statup("Love", 80, -10, 1)  
                        $ LauraX.Statup("Love", 200, -8)
                        "You press into her."                              
                        $ LauraX.Statup("Obed", 70, 3)
                        $ LauraX.Statup("Inbt", 50, 3) 
                        if not ApprovalCheck(LauraX, 700, "O", TabM=1):                        
                            $ LauraX.FaceChange("angry")
                            "[LauraX.Name] shoves you away and backhands you in the face."
                            ch_l "Yeah, not like that you won't."                                           
                            $ LauraX.Statup("Love", 50, -10, 1)                        
                            $ LauraX.Statup("Obed", 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            call Laura_Sex_Reset
                            $ LauraX.RecentActions.append("angry")
                            $ LauraX.DailyActions.append("angry")                        
                        else:
                            $ LauraX.FaceChange("sad")
                            "[LauraX.Name] doesn't seem to be into this, you're lucky she's so obedient."                        
                            jump Laura_AnalPrep
            return  
            #end "auto" 
    
   
    if not LauraX.Anal and "no anal" not in LauraX.RecentActions:                                                               
            #first time    
            $ LauraX.FaceChange("surprised", 1)
            $ LauraX.Mouth = "kiss"
            ch_l "Huh, anal?"
      
            if LauraX.Forced:
                $ LauraX.FaceChange("sad")
                ch_l "Anal? That's what you're pushing for?"
        
    if "anal" in LauraX.RecentActions:
            $ LauraX.FaceChange("sexy", 1)
            ch_l "Sure, get in there."
            jump Laura_AnalPrep
        
    
    if not LauraX.Anal and Approval:                                                 
            #First time dialog        
            if LauraX.Forced: 
                $ LauraX.FaceChange("sad")
                $ LauraX.Statup("Love", 70, -3, 1)
                $ LauraX.Statup("Love", 20, -2, 1)
            elif LauraX.Love >= (LauraX.Obed + LauraX.Inbt):
                $ LauraX.FaceChange("sexy")
                $ LauraX.Brows = "sad"
                $ LauraX.Mouth = "smile" 
                ch_l "I was hoping you'd ask. . ."           
            elif LauraX.Obed >= LauraX.Inbt:
                $ LauraX.FaceChange("normal")
                ch_l "I expected that. . ."
            elif LauraX.Addict >= 50:
                $ LauraX.FaceChange("manic", 1)
                ch_l "Hmm, sounds fun. . ."
            else: # Uninhibited 
                $ LauraX.FaceChange("sad")
                $ LauraX.Mouth = "smile"             
                ch_l "I was tired of waiting. . ."  
    
    elif Approval:                                                                       
            #Second time+ dialog
            if LauraX.Forced: 
                $ LauraX.FaceChange("sad")
                $ LauraX.Statup("Love", 70, -3, 1)
                $ LauraX.Statup("Love", 20, -2, 1)
                ch_l "You don't hold back. . ."
            elif not Taboo and "tabno" in LauraX.DailyActions:        
                ch_l "I guess this is secluded enough. . ."   
            elif "anal" in LauraX.DailyActions and not LauraX.Loose:
                pass      
            elif "anal" in LauraX.RecentActions:
                ch_l "I am warmed up. . ."
                jump Laura_AnalPrep
            elif "anal" in LauraX.DailyActions:
                $ LauraX.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Back again so soon?",                 
                    "So you'd like another round?",                 
                    "Again? Sure.", 
                    "Didn't get enough earlier?",
                    "Your funeral, " + LauraX.Petname + "."]) 
                ch_l "[Line]"    
            else:       
                $ LauraX.FaceChange("sexy", 1)
                $ LauraX.ArmPose = 2
                $ Line = renpy.random.choice(["Oooh, you want some of this?",                 
                    "So you'd like another round?",                 
                    "I knew you enjoyed it. . .", 
                    "I hope you don't plan on wearing me out.",
                    "You want to plow me?"]) 
                ch_l "[Line]"
            $ Line = 0
            
    if Approval >= 2:                                                                   
            #She's into it. . .               
            if LauraX.Forced:
                $ LauraX.FaceChange("sad")
                $ LauraX.Statup("Obed", 90, 1)
                $ LauraX.Statup("Inbt", 60, 1)
                ch_l "Whatever."   
            elif "no anal" in LauraX.DailyActions:               
                ch_l "Well, if you're going to keep asking. . ."
                ch_l "Might be fun. . ."
            else:
                $ LauraX.FaceChange("sexy", 1)
                $ LauraX.Statup("Love", 90, 1)
                $ LauraX.Statup("Inbt", 50, 3) 
                $ Line = renpy.random.choice(["Well. . . ok.",                 
                    "Sure.", 
                    "You could, I guess.",
                    "Um, yeah.",
                    "Heh, ok, ok."]) 
                ch_l "[Line]"
                $ Line = 0
            $ LauraX.Statup("Obed", 20, 1)
            $ LauraX.Statup("Obed", 60, 1)
            $ LauraX.Statup("Inbt", 70, 2) 
            jump Laura_AnalPrep   
               
    else:                                                                               
            #She's not into it, but maybe. . .            
            $ LauraX.FaceChange("angry")
            if "no anal" in LauraX.RecentActions:  
                ch_l "Sorry, [LauraX.Petname] \"no.\""
            elif Taboo and "tabno" in LauraX.DailyActions and "no anal" in LauraX.DailyActions:
                ch_l "I told you. . . this place is too exposed." 
            elif "no anal" in LauraX.DailyActions:       
                ch_l "I just told you \"no.\""
            elif Taboo and "tabno" in LauraX.DailyActions:  
                ch_l "I already told you this is too public!"      
            elif not LauraX.Anal:
                $ LauraX.FaceChange("bemused")
                ch_l "I don't know that you're ready for that yet."
            else:
                $ LauraX.FaceChange("bemused")
                ch_l "Maybe eventually. . ."
            menu:
                extend ""
                "Sorry, never mind." if "no anal" in LauraX.DailyActions:
                    $ LauraX.FaceChange("bemused")
                    ch_l "Hey, I can't blame you."              
                    return
                "Maybe later?" if "no anal" not in LauraX.DailyActions:
                    $ LauraX.FaceChange("sexy")  
                    ch_l "Oh, probably. . ."
                    ch_l ". . . often."
                    $ LauraX.Statup("Love", 80, 2)
                    $ LauraX.Statup("Inbt", 70, 2)  
                    if Taboo:                    
                        $ LauraX.RecentActions.append("tabno")                      
                        $ LauraX.DailyActions.append("tabno") 
                    $ LauraX.RecentActions.append("no anal")                      
                    $ LauraX.DailyActions.append("no anal") 
                    return
                "I bet it would feel really good. . .":             
                    if Approval:
                        $ LauraX.FaceChange("sexy")     
                        $ LauraX.Statup("Obed", 90, 2)
                        $ LauraX.Statup("Obed", 50, 2)
                        $ LauraX.Statup("Inbt", 70, 3) 
                        $ LauraX.Statup("Inbt", 40, 2) 
                        $ Line = renpy.random.choice(["Yeah, probably. . .",     
                                "I guess. . .", 
                                "Good point. . ."]) 
                        ch_l "[Line]"
                        $ Line = 0                   
                        jump Laura_AnalPrep
                    else:   
                        pass
                        
                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(LauraX, 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                    if Approval > 1 or (Approval and LauraX.Forced):
                        $ LauraX.FaceChange("sad")
                        $ LauraX.Statup("Love", 70, -5, 1)
                        $ LauraX.Statup("Love", 200, -5)                 
                        ch_l "Oh fine, get it over with."  
                        $ LauraX.Statup("Obed", 80, 4)
                        $ LauraX.Statup("Inbt", 80, 1) 
                        $ LauraX.Statup("Inbt", 60, 3)  
                        $ LauraX.Forced = 1  
                        jump Laura_AnalPrep
                    else:                              
                        $ LauraX.Statup("Love", 200, -20)    
                        $ LauraX.RecentActions.append("angry")
                        $ LauraX.DailyActions.append("angry")   
    
    #She refused all offers.
    $ LauraX.ArmPose = 1  
    if "no anal" in LauraX.DailyActions:
        ch_l "Don't push it."   
        $ LauraX.RecentActions.append("angry")
        $ LauraX.DailyActions.append("angry")   
    elif LauraX.Forced:
        $ LauraX.FaceChange("angry", 1)
        ch_l "You're going too far."
        $ LauraX.Statup("Lust", 200, 5)     
        if LauraX.Love > 300:     
                $ LauraX.Statup("Love", 70, -2)
        $ LauraX.Statup("Obed", 50, -2)    
        $ LauraX.RecentActions.append("angry")
        $ LauraX.DailyActions.append("angry")   
    elif Taboo:                             
        # she refuses and this is too public a place for her
        $ LauraX.FaceChange("angry", 1)
        $ LauraX.RecentActions.append("tabno")                      
        $ LauraX.DailyActions.append("tabno") 
        ch_l "This place is way too exposed."
        $ LauraX.Statup("Lust", 200, 5)  
        $ LauraX.Statup("Obed", 50, -3) 
    elif "anal" in LauraX.DailyActions:
        $ LauraX.FaceChange("bemused")
        ch_l "Not right now."    
    elif LauraX.Anal:
        $ LauraX.FaceChange("sad") 
        ch_l "You'll have to earn it."
    else:
        $ LauraX.FaceChange("normal", 1)
        ch_l "You haven't earned it yet."    
    $ LauraX.RecentActions.append("no anal")                      
    $ LauraX.DailyActions.append("no anal") 
    $ Tempmod = 0    
    return

label Laura_AnalPrep:    
    call Seen_First_Peen(LauraX,Partner,React=Situation)
    call Laura_Sex_Launch("hotdog")
        
    if Situation == LauraX:                                                                 
            #Laura auto-starts   
            $ Situation = 0
            if LauraX.PantsNum() == 5:
                "[LauraX.Name] lays back, sliding her skirt up as she does so."
                $ LauraX.Upskirt = 1
            elif LauraX.PantsNum() >= 6:
                "[LauraX.Name] lays back, sliding her [LauraX.Legs] down as she does so." 
                $ LauraX.Upskirt = 1
            else:
                "[LauraX.Name] rolls back and pulls you toward her."
            $ LauraX.SeenPanties = 1
            "She slides the tip along her asshole, and seems to want you to insert it."
            menu:
                "What do you do?"
                "Go with it.":                    
                    $ LauraX.Statup("Inbt", 80, 3) 
                    $ LauraX.Statup("Inbt", 50, 2)
                    "[LauraX.Name] slides it in."
                "Praise her.":       
                    $ LauraX.FaceChange("sexy", 1)                    
                    $ LauraX.Statup("Inbt", 80, 3) 
                    ch_p "Oh yeah, [LauraX.Pet], let's do this."
                    $ LauraX.NameCheck() #checks reaction to petname
                    "[LauraX.Name] slides it in."
                    $ LauraX.Statup("Love", 85, 1)
                    $ LauraX.Statup("Obed", 90, 1)
                    $ LauraX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ LauraX.FaceChange("surprised")       
                    $ LauraX.Statup("Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [LauraX.Pet]."
                    $ LauraX.NameCheck() #checks reaction to petname
                    "[LauraX.Name] pulls back."
                    $ LauraX.Statup("Obed", 90, 1)
                    $ LauraX.Statup("Obed", 50, 1)
                    $ LauraX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")      
                    $ LauraX.AddWord(1,"refused","refused")  
                    return      
            $ LauraX.PantiesDown = 1  
            call Laura_First_Bottomless(1)
    elif Situation != "auto":
        call Bottoms_Off(LauraX)    
        if (LauraX.Panties and not LauraX.PantiesDown) or (LauraX.Legs and not LauraX.Upskirt) or LauraX.HoseNum() >= 6: #If she refuses to take off her pants but agreed to anal
            ch_l "Huh. . ."
            
            if (LauraX.Panties and not LauraX.PantiesDown) and (LauraX.PantsNum() > 6 and not LauraX.Upskirt):
                "She quickly drops her pants and her [LauraX.Panties]."
            elif (LauraX.Panties and not LauraX.PantiesDown) and (LauraX.PantsNum() == 6 and not LauraX.Upskirt):
                "She quickly drops her shorts and her [LauraX.Panties]."
            elif LauraX.PantsNum() > 6 and not LauraX.Upskirt:
                "She tugs her pants down, exposing her bare pussy."
            elif LauraX.PantsNum() == 6 and not LauraX.Upskirt:
                "She tugs her shorts down, exposing her bare pussy."
            elif LauraX.HoseNum() >= 6 and (LauraX.Panties and not LauraX.PantiesDown):
                "She tugs her [LauraX.Hose] and [LauraX.Panties] off."
                $ LauraX.Hose = 0
            elif LauraX.HoseNum() >= 6:
                "She tugs her [LauraX.Hose] off and drops them to the ground."
                $ LauraX.Hose = 0
            elif (LauraX.Panties and not LauraX.PantiesDown):
                "She tugs her [LauraX.Panties] off and drops them to the ground."  
                
        $ LauraX.Upskirt = 1
        $ LauraX.PantiesDown = 1       
        $ LauraX.SeenPanties = 1
        call Laura_First_Bottomless
        
        if Taboo: # Laura gets started. . .
            "[LauraX.Name] glances around to see if anyone notices what she's doing."
            if "cockout" in Player.RecentActions:
                "Then she lays back and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and lays back."
                "She slowly presses against your rigid member."
            $ LauraX.Inbt += int(Taboo/10)  
            $ LauraX.Lust += int(Taboo/5)
        else:    
            if "cockout" in Player.RecentActions:
                "[LauraX.Name] lays back and slowly presses against your rigid member."
            else:
                "[LauraX.Name] pulls down your pants and lays back."
                "She slowly presses against your rigid member."
        "She leans back a bit and your cock pops in."
                     
    else: #if Situation == "auto"       
        if (LauraX.PantsNum() >= 6 and not LauraX.Upskirt) and (LauraX.Panties and not LauraX.PantiesDown):
            "You quickly pull down her pants and her [LauraX.Panties] and press against her back door."
        elif (LauraX.Panties and not LauraX.PantiesDown):
            "You quickly pull down her [LauraX.Panties] and press against her back door."  
        $ LauraX.Upskirt = 1
        $ LauraX.PantiesDown = 1       
        $ LauraX.SeenPanties = 1
        call Laura_First_Bottomless(1)
            
    if not LauraX.Anal:                                                      #First time stat buffs       
        if LauraX.Forced:
            $ LauraX.Statup("Love", 90, -150)
            $ LauraX.Statup("Obed", 70, 70)
            $ LauraX.Statup("Inbt", 80, 40) 
        else:
            $ LauraX.Statup("Love", 90, 10)
            $ LauraX.Statup("Obed", 70, 30)
            $ LauraX.Statup("Inbt", 80, 70) 
    elif not LauraX.Loose:                                                   #first few times stat buffs       
        if LauraX.Forced:
            $ LauraX.Statup("Love", 90, -20)
            $ LauraX.Statup("Obed", 70, 10)
            $ LauraX.Statup("Inbt", 80, 5) 
        else:
            $ LauraX.Statup("Obed", 70, 7)
            $ LauraX.Statup("Inbt", 80, 5) 
                
    if Situation:    
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ Player.Cock = "anal"
    $ Trigger = "anal"
    $ Speed = 1
    if Taboo:
        $ LauraX.DrainWord("tabno")
    $ LauraX.DrainWord("no anal")
    $ LauraX.RecentActions.append("anal")                      
    $ LauraX.DailyActions.append("anal") 

label Laura_Anal_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus(LauraX)
        call Laura_Sex_Launch("anal") 
        if Speed >= 4:    
            $ Shift = 2
#            call Speed_Shift(2) 
        $ LauraX.LustFace()         
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
                                    call Slap_Ass(LauraX)  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Laura_Anal_Cycle  
                                    
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
                                            if LauraX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ LauraX.Action -= 1
                                            else:
                                                ch_l "I think we could take a little break." 
                                                
                                    "Shift primary action":
                                            if LauraX.Action and MultiAction:
                                                    menu:
                                                        "How about sex?":
                                                                $ Situation = "shift"
                                                                call Laura_AnalAfter
                                                                call Laura_Sex_P
                                                        "Just stick it in her pussy [[without asking].":
                                                                $ Situation = "auto"
                                                                call Laura_AnalAfter
                                                                call Laura_Sex_P
                                                        "Pull back to hotdog her.":
                                                                $ Situation = "pullback"
                                                                call Laura_AnalAfter
                                                                call Laura_Sex_H
                                                        "Never Mind":
                                                                jump Laura_Anal_Cycle
                                            else:
                                                ch_l "I think we could take a little break." 
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask [LauraX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(LauraX)
                                            "Ask [LauraX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(LauraX) 
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0   
                                                        
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(LauraX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_Anal_Cycle 
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_Anal_Cycle 
                                            "Never mind":
                                                        jump Laura_Anal_Cycle 
                                    "undress [LauraX.Name]":
                                            call Girl_Undress(LauraX)   
                                    "Clean up [LauraX.Name] (locked)" if not LauraX.Spunk:
                                            pass  
                                    "Clean up [LauraX.Name]" if LauraX.Spunk:
                                            call Girl_Cleanup(LauraX,"ask")                                         
                                    "Never mind":
                                            jump Laura_Anal_Cycle                                    
                                                        
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Laura_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Laura_AnalAfter
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Laura_Sex_Reset
                                    $ Line = 0
                                    jump Laura_AnalAfter
        #End menu (if Line)              
        
        call Shift_Focus(LauraX)    
        call Sex_Dialog(LauraX,Partner)
        
        $ Cnt += 1
        $ Round -= 1     
        
        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or LauraX.Lust >= 100:   
                    #If either of you could cum    
                    if Player.Focus >= 100:
                            #If you can cum:                                                
                            call Player_Cumming(LauraX)
                            if "angry" in LauraX.RecentActions:  
                                call Laura_Sex_Reset
                                return    
                            $ LauraX.Statup("Lust", 200, 5) 
                            if 100 > LauraX.Lust >= 70 and LauraX.OCount < 2:             
                                    $ LauraX.RecentActions.append("unsatisfied")                      
                                    $ LauraX.DailyActions.append("unsatisfied") 
                            
                            if Player.Focus > 80:
                                jump Laura_AnalAfter 
                            $ Line = "came"

                    if LauraX.Lust >= 100:         
                            #If you're still going at it and Laura can cum
                            call Girl_Cumming(LauraX)
                            if Situation == "shift" or "angry" in LauraX.RecentActions:
                                jump Laura_AnalAfter
                       
                    if Line == "came": #ex Player.Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Laura_AnalAfter
                            elif "unsatisfied" in LauraX.RecentActions:
                                #And Laura is unsatisfied,  
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ Line = "You get back into it" 
                                        jump Laura_Anal_Cycle  
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Laura_AnalAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Laura_AnalAfter   
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)            
        #End orgasm
        
        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0
        
        if LauraX.SEXP >= 100 or ApprovalCheck(LauraX, 1200, "LO"):
            pass
        elif Cnt == (5 + LauraX.Anal):
                    $ LauraX.Brows = "confused"
                    ch_l "We getting close here?"   
        elif Cnt == (10 + LauraX.Anal):
                    $ LauraX.Brows = "angry"        
                    menu:
                        ch_l "Can we. . . do something. . . else?"
                        "How about a BJ?" if LauraX.Action and MultiAction:
                                $ Situation = "shift"
                                call Laura_AnalAfter
                                call Laura_Blowjob  
                        "How about a Handy?" if LauraX.Action and MultiAction:
                                $ Situation = "shift"
                                call Laura_AnalAfter
                                call Laura_Handjob     
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."             
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ Cnt += 1
                                jump Laura_Anal_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Laura_Sex_Reset
                                $ Situation = "shift"
                                jump Laura_AnalAfter
                        "No, get back down there.":                                
                                if ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 500, "O"):                        
                                    $ LauraX.Statup("Love", 200, -5)
                                    $ LauraX.Statup("Obed", 50, 3)                    
                                    $ LauraX.Statup("Obed", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    $ LauraX.FaceChange("angry", 1)   
                                    call Laura_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_l "Not with that attitude."                         
                                    $ LauraX.Statup("Love", 50, -3, 1)
                                    $ LauraX.Statup("Love", 80, -4, 1)
                                    $ LauraX.Statup("Obed", 30, -1, 1)                    
                                    $ LauraX.Statup("Obed", 50, -1, 1)  
                                    $ LauraX.RecentActions.append("angry")
                                    $ LauraX.DailyActions.append("angry")   
                                    jump Laura_AnalAfter
        #End Count check
   
        if Round == 10:
            ch_l "It's getting kinda late. . ."  
        elif Round == 5:
            ch_l "We should take a break for a minute."        
    
    #Round = 0 loop breaks
    $ LauraX.FaceChange("bemused", 0)
    $ Line = 0
    ch_l "Ok, that's enough of that for now."
    
label Laura_AnalAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ Player.Sprite = 0
        $ Player.Cock = "out"
        call Laura_Sex_Reset
        
    $ LauraX.FaceChange("sexy") 
    
    $ LauraX.Anal += 1  
    $ LauraX.Action -=1
    $ LauraX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ LauraX.Addictionrate += 1        
    $ LauraX.Statup("Inbt", 30, 3) 
    $ LauraX.Statup("Inbt", 70, 1) 
    
    if Partner == "Kitty":
        call Partner_Like(LauraX,4,2)
    else:
        call Partner_Like(LauraX,3,2)
    
    if "Laura Anal Addict" in Achievements:
            pass 
            
    elif LauraX.Anal >= 10:
        $ LauraX.SEXP += 7
        $ Achievements.append("Laura Anal Addict")
        if not Situation:
            $ LauraX.FaceChange("bemused", 1)
            ch_l "I think you've got a knack for that."                  
    elif LauraX.Anal == 1:            
            $LauraX.SEXP += 25        
            if not Situation: 
                if LauraX.Love >= 500 and "unsatisfied" not in LauraX.RecentActions:
                    ch_l "You seem to know your way around back there."  
                elif LauraX.Obed <= 500 and Player.Focus <= 20:
                    $ LauraX.Mouth = "sad"
                    ch_l "That was pleasant."
    elif LauraX.Anal == 5:
            ch_l "I'm glad you're into this."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in LauraX.RecentActions:
            $ LauraX.FaceChange("angry")
            $ LauraX.Eyes = "side"
            ch_l  "Forgetting someone? . ."
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Mmm, so what else did you have in mind?"
    call Checkout
    return   


# End Laura Anal //////////////////////////////////////////////////////////////////////////////////
    

  
# Laura hotdog //////////////////////////////////////////////////////////////////////

label Laura_Sex_H: 
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(LauraX)
    if LauraX.Hotdog >= 3: #You've done it before several times
        $ Tempmod += 10
    elif LauraX.Hotdog: #You've done it before
        $ Tempmod += 5    
    
    if LauraX.Lust > 85:
        $ Tempmod += 10
    elif LauraX.Lust > 75: #She's really horny
        $ Tempmod += 5
    if Situation == "shift":
        $ Tempmod += 10   
    if "exhibitionist" in LauraX.Traits:
        $ Tempmod += (3*Taboo)  
    if "dating" in LauraX.Traits or "sex friend" in LauraX.Petnames:
        $ Tempmod += 10
    elif "ex" in LauraX.Traits:
        $ Tempmod -= 40 
    if LauraX.ForcedCount and not LauraX.Forced:
        $ Tempmod -= 5 * LauraX.ForcedCount 
    
    if Taboo and "tabno" in LauraX.DailyActions:        
        $ Tempmod -= 10 
        
    if "no hotdog" in LauraX.DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no hotdog" in LauraX.RecentActions else 0      
        
    $ Approval = ApprovalCheck(LauraX, 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)
    
    if Situation == "auto":   
            call Laura_Sex_Launch("L")   
            "You push [LauraX.Name] down, and press your cock against her."    
            $ LauraX.FaceChange("surprised", 1)
            
            if (LauraX.Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
                "[LauraX.Name] glances down and then breaks into a smile."
                $ LauraX.FaceChange("sly")
                $ LauraX.Statup("Obed", 70, 3)
                $ LauraX.Statup("Inbt", 50, 3) 
                $ LauraX.Statup("Inbt", 70, 1) 
                ch_l "Oh, what did you have in mind with that? . ."            
                jump Laura_HotdogPrep         
            else:                                                                                                            #she's questioning it
                $ LauraX.Brows = "angry"                
                menu:
                    ch_l "You might want to take a step back, [LauraX.Petname]?" 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            $ LauraX.FaceChange("sexy", 1)
                            $ LauraX.Statup("Obed", 70, 3)
                            $ LauraX.Statup("Inbt", 50, 3) 
                            $ LauraX.Statup("Inbt", 70, 1) 
                            ch_l "Or not. . ."
                            jump Laura_HotdogPrep
                        "You pull back from her."                    
                        $ LauraX.FaceChange("bemused", 1)
                        ch_l "Maybe ask first?"                                             
                    "You'll see.":                    
                        $ LauraX.Statup("Love", 80, -10, 1)  
                        $ LauraX.Statup("Love", 200, -8)
                        "You grind against her crotch."                              
                        $ LauraX.Statup("Obed", 70, 3)
                        $ LauraX.Statup("Inbt", 50, 3) 
                        if not ApprovalCheck(LauraX, 500, "O", TabM=1): #Checks if Obed is 700+  
                            $ LauraX.FaceChange("angry")
                            "[LauraX.Name] shoves you away."
                            ch_l "Don't push it, [LauraX.Petname]."                                                  
                            $ LauraX.Statup("Love", 50, -10, 1)                        
                            $ LauraX.Statup("Obed", 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            call Laura_Sex_Reset
                            $ LauraX.RecentActions.append("angry")
                            $ LauraX.DailyActions.append("angry")                       
                        else:
                            $ LauraX.FaceChange("sad")
                            "[LauraX.Name] doesn't seem to be into this, but she knows her place."                        
                            jump Laura_HotdogPrep
            return     
            #end auto
    
   
    if not LauraX.Hotdog and "no hotdog" not in LauraX.RecentActions:                                                               
            #first time    
            $ LauraX.FaceChange("surprised", 1)
            $ LauraX.Mouth = "kiss"
            ch_l "What, just grinding?"
      
            if LauraX.Forced:
                $ LauraX.FaceChange("sad")
                ch_l ". . . nothing more?"
        
        
    if not LauraX.Hotdog and Approval:                                                
            #First time dialog        
            if LauraX.Forced: 
                $ LauraX.FaceChange("sad")
                $ LauraX.Statup("Love", 70, -3, 1)
                $ LauraX.Statup("Love", 20, -2, 1)
            elif LauraX.Love >= (LauraX.Obed + LauraX.Inbt):
                $ LauraX.FaceChange("sexy")
                $ LauraX.Brows = "sad"
                $ LauraX.Mouth = "smile" 
                ch_l "If that's what you're into. . ."           
            elif LauraX.Obed >= LauraX.Inbt:
                $ LauraX.FaceChange("normal")
                ch_l "If that's what works for you. . ."
            elif LauraX.Addict >= 50:
                $ LauraX.FaceChange("manic", 1)
                ch_l "Hrmm. . ."
            else: # Uninhibited 
                $ LauraX.FaceChange("sad")
                $ LauraX.Mouth = "smile"             
                ch_l "Well if that's what gets you off. . ."    
            
    elif Approval:                                                                      
            #Second time+ dialog
            if LauraX.Forced: 
                $ LauraX.FaceChange("sad")
                $ LauraX.Statup("Love", 70, -3, 1)
                $ LauraX.Statup("Love", 20, -2, 1)
                ch_l "That's pushing it. . ."  
            elif not Taboo and "tabno" in LauraX.DailyActions:        
                ch_l "I guess this is a better location . ."   
            elif "hotdog" in LauraX.RecentActions:
                $ LauraX.FaceChange("sexy", 1)
                ch_l "Again? Fine, whatever."
                jump Laura_HotdogPrep
            elif "hotdog" in LauraX.DailyActions:
                $ LauraX.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Back again so soon?",                 
                    "So you'd like another round?",                 
                    "You're really into this. . .", 
                    "Are you sure that's all you want?"]) 
                ch_l "[Line]"    
            else:       
                $ LauraX.FaceChange("sexy", 1)
                $ LauraX.ArmPose = 2
                $ Line = renpy.random.choice(["Oooh, you want some of this?",                 
                    "So you'd like another round?",                       
                    "You're really into this. . .", 
                    "You want another rub?"]) 
                ch_l "[Line]"
            $ Line = 0
            
    if Approval >= 2:                                                                  
            #She's into it. . .               
            if LauraX.Forced:
                $ LauraX.FaceChange("sad")
                $ LauraX.Statup("Obed", 80, 1)
                $ LauraX.Statup("Inbt", 60, 1)
                ch_l "Ok, fine."    
            elif "no hotdog" in LauraX.DailyActions:               
                ch_l "It was rather entertaining. . ."
            else:
                $ LauraX.FaceChange("sexy", 1)
                $ LauraX.Statup("Love", 80, 1)
                $ LauraX.Statup("Inbt", 50, 2) 
                $ Line = renpy.random.choice(["Well, sure, let me give it a rub.",                 
                    "Very well.",                 
                    "Nice!", 
                    "I guess we could do that.",
                    "Ok, let me. . .",
                    "Heh, ok, ok."]) 
                ch_l "[Line]"
                $ Line = 0
            $ LauraX.Statup("Obed", 60, 1)
            $ LauraX.Statup("Inbt", 70, 2) 
            jump Laura_HotdogPrep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            $ LauraX.FaceChange("angry")
            if "no hotdog" in LauraX.RecentActions:  
                ch_l "Sorry, [LauraX.Petname] \"no.\""
            elif Taboo and "tabno" in LauraX.DailyActions and "no hotdog" in LauraX.DailyActions: 
                ch_l "I just told you. . .not in such an exposed location." 
            elif "no hotdog" in LauraX.DailyActions:       
                ch_l "I'm believe I just told you \"no,\" [LauraX.Petname]."
            elif Taboo and "tabno" in LauraX.DailyActions:  
                ch_l "I told you. . . this place is too exposed." 
            elif not LauraX.Hotdog:
                $ LauraX.FaceChange("bemused")
                ch_l "Hmm, that could be amusing, [LauraX.Petname]. . ."
            else:
                $ LauraX.FaceChange("bemused")
                ch_l "I don't think that would be appropriate. . ."
            menu:
                extend ""
                "Sorry, never mind." if "no hotdog" in LauraX.DailyActions:
                    $ LauraX.FaceChange("bemused")
                    ch_l "So long as you don't push it."              
                    return
                "Maybe later?" if "no hotdog" not in LauraX.DailyActions:
                    $ LauraX.FaceChange("sexy")  
                    ch_l "I gues eventually. . ."
                    $ LauraX.Statup("Love", 80, 1)
                    $ LauraX.Statup("Inbt", 50, 1)   
                    if Taboo:                    
                        $ LauraX.RecentActions.append("tabno")                      
                        $ LauraX.DailyActions.append("tabno") 
                    $ LauraX.RecentActions.append("no hotdog")                      
                    $ LauraX.DailyActions.append("no hotdog")                          
                    return
                "You might like it. . .":             
                    if Approval:
                        $ LauraX.FaceChange("sexy")     
                        $ LauraX.Statup("Obed", 60, 2)
                        $ LauraX.Statup("Inbt", 50, 2) 
                        $ Line = renpy.random.choice(["Yeah, probably. . .",     
                                "I guess. . .", 
                                "Good point. . ."]) 
                        ch_l "[Line]"
                        $ Line = 0                   
                        jump Laura_HotdogPrep
                    else:   
                        pass
                        
                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(LauraX, 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                    if Approval > 1 or (Approval and LauraX.Forced):
                        $ LauraX.FaceChange("sad")
                        $ LauraX.Statup("Love", 70, -2, 1)
                        $ LauraX.Statup("Love", 200, -2)                 
                        ch_l "Alright, fine."  
                        $ LauraX.Statup("Obed", 80, 4)
                        $ LauraX.Statup("Inbt", 60, 2)  
                        $ LauraX.Forced = 1  
                        jump Laura_HotdogPrep
                    else:                              
                        $ LauraX.Statup("Love", 200, -10)     
                        $ LauraX.RecentActions.append("angry")
                        $ LauraX.DailyActions.append("angry")   
    
    #She refused all offers.
    $ LauraX.ArmPose = 1      
    
    if "no hotdog" in LauraX.DailyActions:
        ch_l "What did I tell you?"   
        $ LauraX.RecentActions.append("angry")
        $ LauraX.DailyActions.append("angry")   
    if LauraX.Forced:
        $ LauraX.FaceChange("angry", 1)
        ch_l "There's no point trying."
        $ LauraX.Statup("Lust", 200, 5)  
        if LauraX.Love > 300:   
                $ LauraX.Statup("Love", 70, -1)
        $ LauraX.Statup("Obed", 50, -1)  
        $ LauraX.RecentActions.append("angry")
        $ LauraX.DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        $ LauraX.FaceChange("angry", 1)        
        $ LauraX.RecentActions.append("tabno")                      
        $ LauraX.DailyActions.append("tabno") 
        ch_l "This area is a bit too exposed for that sort of thing. . ."  
        $ LauraX.Statup("Lust", 200, 5)  
        $ LauraX.Statup("Obed", 50, -3)  
    elif LauraX.Hotdog:
        $ LauraX.FaceChange("sad") 
        ch_l "Not anymore."
    else:
        $ LauraX.FaceChange("normal", 1)
        ch_l "No thanks."    
    $ LauraX.RecentActions.append("no hotdog")                      
    $ LauraX.DailyActions.append("no hotdog") 
    $ Tempmod = 0    
    return

label Laura_HotdogPrep:  
    call Seen_First_Peen(LauraX,Partner,React=Situation)
    call Laura_Sex_Launch("hotdog")
    
    if Situation == LauraX:                                                                 
            #Laura auto-starts   
            $ Situation = 0
            "[LauraX.Name] rolls back and pulls you toward her, grinding against your cock."
            menu:
                "What do you do?"
                "Go with it.":                    
                    $ LauraX.Statup("Inbt", 80, 3) 
                    $ LauraX.Statup("Inbt", 50, 2)
                    "[LauraX.Name] continues to grind."
                "Praise her.":       
                    $ LauraX.FaceChange("sexy", 1)                    
                    $ LauraX.Statup("Inbt", 80, 3) 
                    ch_p "Oh yeah, [LauraX.Pet], let's do this."
                    $ LauraX.NameCheck() #checks reaction to petname
                    "[LauraX.Name] continues to grind."
                    $ LauraX.Statup("Love", 85, 1)
                    $ LauraX.Statup("Obed", 90, 1)
                    $ LauraX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ LauraX.FaceChange("surprised")       
                    $ LauraX.Statup("Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [LauraX.Pet]."
                    $ LauraX.NameCheck() #checks reaction to petname
                    "[LauraX.Name] pulls back."
                    $ LauraX.Statup("Obed", 90, 1)
                    $ LauraX.Statup("Obed", 50, 1)
                    $ LauraX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")      
                    $ LauraX.AddWord(1,"refused","refused")  
                    return      
    elif Situation != "auto":
#        call Bottoms_Off(LauraX)    
        
        if Taboo: # Laura gets started. . .
            "[LauraX.Name] glances around to see if anyone notices what she's doing."
            if "cockout" in Player.RecentActions:
                "Then she lays back and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and lays back."
                "She slowly presses against your rigid member."
            $ LauraX.Inbt += int(Taboo/10)  
            $ LauraX.Lust += int(Taboo/5)
        else:    
            if "cockout" in Player.RecentActions:
                "[LauraX.Name] lays back and slowly presses against your rigid member."
            else:
                "[LauraX.Name] pulls down your pants and lays back."
                "She slowly presses against your rigid member."
                     
    else: #if Situation == "auto"       
        "She lays back, pulling you against her with your rigid member."
    
    if not LauraX.Hotdog:                                                      #First time stat buffs      
        if LauraX.Forced:
            $ LauraX.Statup("Love", 90, -5)
            $ LauraX.Statup("Obed", 70, 20)
            $ LauraX.Statup("Inbt", 80, 10) 
        else:
            $ LauraX.Statup("Love", 90, 20)
            $ LauraX.Statup("Obed", 70, 20)
            $ LauraX.Statup("Inbt", 80, 20)  
    
            
    if Situation:    
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ Trigger = "hotdog"
    $ Speed = 1
    if Taboo:
        $ LauraX.DrainWord("tabno")
    $ LauraX.DrainWord("no hotdog")
    $ LauraX.RecentActions.append("hotdog")                      
    $ LauraX.DailyActions.append("hotdog") 

label Laura_Hotdog_Cycle: #Repeating strokes 
    while Round >=0:  
        call Shift_Focus(LauraX)
        call Laura_Sex_Launch("hotdog") 
        if Speed >= 4:        
            $ Speed = 2
#            call Speed_Shift(2) 
        $ LauraX.LustFace()         
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
                                    call Slap_Ass(LauraX)  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Laura_Hotdog_Cycle  
                                    
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
                                            if LauraX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ LauraX.Action -= 1
                                            else:
                                                ch_l "I think we could take a little break." 
                                                
                                    "Shift primary action":
                                            if LauraX.Action and MultiAction:
                                                    menu:
                                                        "How about sex?":
                                                            $ Situation = "shift"
                                                            call Laura_HotdogAfter
                                                            call Laura_Sex_P
                                                        "Just stick it in her pussy [[without asking].":
                                                            $ Situation = "auto"
                                                            call Laura_HotdogAfter
                                                            call Laura_Sex_P
                                                        "How about anal?":
                                                            $ Situation = "shift"
                                                            call Laura_HotdogAfter
                                                            call Laura_Sex_A
                                                        "Just stick it in her ass [[without asking].":
                                                            $ Situation = "auto"
                                                            call Laura_HotdogAfter
                                                            call Laura_Sex_A
                                                        "Never Mind":
                                                                jump Laura_Hotdog_Cycle
                                            else:
                                                ch_l "I think we could take a little break." 
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask [LauraX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(LauraX)
                                            "Ask [LauraX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(LauraX) 
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0   
                                                        
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(LauraX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_Hotdog_Cycle 
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_Hotdog_Cycle 
                                            "Never mind":
                                                        jump Laura_Hotdog_Cycle 
                                    "undress [LauraX.Name]":
                                            call Girl_Undress(LauraX)   
                                    "Clean up [LauraX.Name] (locked)" if not LauraX.Spunk:
                                            pass  
                                    "Clean up [LauraX.Name]" if LauraX.Spunk:
                                            call Girl_Cleanup(LauraX,"ask")                                         
                                    "Never mind":
                                            jump Laura_Hotdog_Cycle                                    
                                                        
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Laura_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Laura_HotdogAfter
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Laura_Sex_Reset
                                    $ Line = 0
                                    jump Laura_HotdogAfter
        #End menu (if Line)              
        
        call Shift_Focus(LauraX)    
        call Sex_Dialog(LauraX,Partner)
        
        $ Cnt += 1
        $ Round -= 1     
        
        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or LauraX.Lust >= 100:   
                    #If either of you could cum    
                    if Player.Focus >= 100:
                            #If you can cum:                                                
                            call Player_Cumming(LauraX)
                            if "angry" in LauraX.RecentActions:  
                                call Laura_Sex_Reset
                                return    
                            $ LauraX.Statup("Lust", 200, 5) 
                            if 100 > LauraX.Lust >= 70 and LauraX.OCount < 2:             
                                    $ LauraX.RecentActions.append("unsatisfied")                      
                                    $ LauraX.DailyActions.append("unsatisfied") 
                            
                            if Player.Focus > 80:
                                jump Laura_HotdogAfter 
                            $ Line = "came"

                    if LauraX.Lust >= 100:         
                            #If you're still going at it and Laura can cum
                            call Girl_Cumming(LauraX)
                            if Situation == "shift" or "angry" in LauraX.RecentActions:
                                jump Laura_HotdogAfter
                       
                    if Line == "came": #ex Player.Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Laura_HotdogAfter
                            elif "unsatisfied" in LauraX.RecentActions:
                                #And Laura is unsatisfied,  
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ Line = "You get back into it" 
                                        jump Laura_Hotdog_Cycle  
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Laura_HotdogAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Laura_HotdogAfter   
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)            
        #End orgasm
        
        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0
        
        if LauraX.SEXP >= 100 or ApprovalCheck(LauraX, 1200, "LO"):
            pass
        elif Cnt == (5 + LauraX.Hotdog):
                    $ LauraX.Brows = "confused"
                    ch_l "Are we getting close here?"   
        elif Cnt == (10 + LauraX.Hotdog):
                    $ LauraX.Brows = "angry"        
                    menu:
                        ch_l "I'm kinda bored by this."
                        "How about a BJ?" if LauraX.Action and MultiAction:
                                $ Situation = "shift"
                                call Laura_HotdogAfter
                                call Laura_Blowjob       
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."             
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ Cnt += 1
                                jump Laura_Hotdog_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Laura_Sex_Reset
                                $ Situation = "shift"
                                jump Laura_HotdogAfter
                        "No, get back down there.":                                
                                if ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 500, "O"):                        
                                    $ LauraX.Statup("Love", 200, -5)
                                    $ LauraX.Statup("Obed", 50, 3)                    
                                    $ LauraX.Statup("Obed", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    $ LauraX.FaceChange("angry", 1)   
                                    call Laura_Sex_Reset
                                    "She scowls at you and pulls away."
                                    ch_l "Not with that attitude."                         
                                    $ LauraX.Statup("Love", 50, -3, 1)
                                    $ LauraX.Statup("Love", 80, -4, 1)
                                    $ LauraX.Statup("Obed", 30, -1, 1)                    
                                    $ LauraX.Statup("Obed", 50, -1, 1)  
                                    $ LauraX.RecentActions.append("angry")
                                    $ LauraX.DailyActions.append("angry")   
                                    jump Laura_HotdogAfter
        #End Count check
   
        call Escalation(LauraX) #sees if she wants to escalate things
        
        if Round == 10:
            ch_l "It's getting kinda late. . ."  
        elif Round == 5:
            ch_l "We should take a break for a minute."        
    
    #Round = 0 loop breaks
    $ LauraX.FaceChange("bemused", 0)
    $ Line = 0
    ch_l "Ok, that's enough of that for now."
    
label Laura_HotdogAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ Player.Sprite = 0
        $ Player.Cock = "out"
        call Laura_Sex_Reset
        
    $ LauraX.FaceChange("sexy") 
    
    $ LauraX.Hotdog += 1  
    $ LauraX.Action -=1
    $ LauraX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ LauraX.Addictionrate += 1        
    $ LauraX.Statup("Inbt", 30, 1) 
    $ LauraX.Statup("Inbt", 70, 1) 
    
    call Partner_Like(LauraX,2)
    
    if LauraX.Hotdog == 10:
        $ LauraX.SEXP += 5             
    elif LauraX.Hotdog == 1:            
            $LauraX.SEXP += 10        
            if not Situation: 
                if LauraX.Love >= 500 and "unsatisfied" not in LauraX.RecentActions:
                    ch_l "That was. . . nice."
                elif LauraX.Obed <= 500 and Player.Focus <= 20:
                    $ LauraX.Mouth = "sad"
                    ch_l "Enough for you?" 
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in LauraX.RecentActions:
            $ LauraX.FaceChange("angry")
            $ LauraX.Eyes = "side"
            ch_l "That didn't do much for me. . ."
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# End Laura hotdogging //////////////////////////////////////////////////////////////////////////////////

