﻿# Kitty_SexMenu //////////////////////////////////////////////////////////////////////
label Kitty_SexAct(Act = 0):    
    call Shift_Focus("Kitty")    
    if Act == "SkipTo":
        $ renpy.pop_call() #causes it to skip past the Trigger Swap
        $ renpy.pop_call() #causes it to skip past the cycle you were in before
        $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
        call SkipTo("Kitty")
    elif Act == "switch":
        $ renpy.pop_call() #causes it to skip past call here from Sex_Menu_Threesome
        $ renpy.pop_call() #causes it to skip past call to Sex_Menu_Threesome
        # drops through to sex menu
    elif Act == "masturbate":         
        call KM_Prep
        if not Situation:
            return    
    elif Act == "lesbian":         
        call K_Les_Prep
        if not Situation:
            return       
    elif Act == "morningwood":
        # This action is called for by the label Kitty_Morning and returns to there
        $ K_RecentActions.append("blow")           
        $ K_DailyActions.append("blow")                          
        $ K_DailyActions.append("morningwood")  
        call Sleepover_MorningWood
#        call Kitty_MorningWood
        if Situation == "blow": 
            #If you selected to continue the BJ, then it calls the BJ actions
            $ Situation = 0
            call KBJ_Prep
        $ Trigger4 = 0
        call Morning_Partner
        if not Situation:
            return
    elif Act == "kissing":        
        call K_KissPrep
        if not Situation:
            return   
    elif Act == "breasts":        
        call K_Fondle_Breasts
        if not Situation:
            return  
    elif Act == "blow":        
        call KBJ_Prep
        if not Situation:
            return  
    elif Act == "hand":        
        call KHJ_Prep
        if not Situation:
            return   
    elif Act == "sex":        
        call K_SexPrep
        if not Situation:
            return   

label Kitty_SexMenu:     
    call Shift_Focus("Kitty")
    $ Trigger = 0    
    $ Trigger2 = 0
    $ Trigger3 = 0
    $ Situation = 0
    call Kitty_Hide    
    $ Kitty_Arms = 1
    call Set_The_Scene(1,0,0,0,1)
    if not P_Semen:
        "You're a little out of juice at the moment, you might want to wait a bit." 
    if P_Focus >= 95:
        "You're practically buzzing, the slightest breeze could set you off."
    if not K_Action:
        "Kitty's looking a bit tired out, maybe let her rest a bit."
    
    if "caught" in K_RecentActions or "angry" in K_RecentActions:  
        if K_Loc == bg_current:                
                ch_k "I don't want to deal with you right now."
        call KittyOutfit        
        call DrainWord("Kitty","caught",1,0)
        return
        
    if Round < 5:
        ch_k "We've been at it for a while now, let's take a breather."   
        return
    menu Kitty_SMenu:  
        ch_k "So what would you like to do?"
        "Do you want to make out?":
            if K_Action:
                call K_Makeout
            else:
                ch_k "Sorry, [K_Petname], but I'm a bit worn out." 
        
        "Could I touch you?":
                if K_Action:
                    $ K_Mouth = "smile"                    
                    menu:
                        ch_k "Um, what did you want to touch, [K_Petname]?"                      
                        "Could I give you a massage?":
                                call K_Massage                        
                        "Your breasts?":
                                call K_Fondle_Breasts
                        "Your thighs?":
                                call K_Fondle_Thighs
                        "Your pussy?":
                                call K_Fondle_Pussy
                        "Your Ass?":
                                call K_Fondle_Ass
                        "Never mind [[something else]":
                                jump Kitty_SMenu
                else:
                    ch_k "Sorry, [K_Petname], but I'm a bit worn out."
                    
        "Could you take care of something for me? [[Your dick, you mean your dick]":        
                if P_Semen and K_Action:                
                    menu:
                        ch_k "[K_Like]what did you want me to do?"
                        "Could you give me a handjob?":
                            call K_Handjob
                        "Could you give me a titjob?":
                            call K_Titjob         
                        "Could you suck my cock?":
                            call K_Blowjob 
                        "Could use your feet?":
                            call K_Footjob 
                        "Never mind [[something else]":
                            jump Kitty_SMenu
                elif not K_Action:
                        ch_k "Sorry [K_Petname], I'm a bit worn out."
                else:
                        "You really don't have it in you, maybe take a break." 
                
        "Could you put on a show for me?":
                    menu:
                        ch_k "[K_Like]what did you want to see?"
                        "Dance for me?":
                                if K_Action:
                                    call Group_Strip("Kitty") 
                                else:
                                    ch_k "Sorry [K_Petname], I'm a bit worn out."
                                
                        "Could you undress for me?": 
                                    call K_Undress  
                                            
                        "You've got a little something. . . [[clean-up]" if K_Spunk:
                                    ch_k "Huh?"
                                    call Kitty_Cleanup("ask")
                                    
                        "Could I watch you get yourself off? [[masturbate]":
                                if K_Action:
                                    call K_Masturbate           
                                else:
                                    ch_k "Sorry [K_Petname], I'm a bit worn out."
                        
                        "Maybe make out with Rogue?" if R_Loc == bg_current:
                                call K_LesScene
                        "Maybe make out with Emma?" if E_Loc == bg_current:
                                call K_LesScene
                        "Maybe make out with Laura?" if L_Loc == bg_current:
                                call K_LesScene

                        "Never mind [[something else]":
                                jump Kitty_SMenu
                          
                
        "Could we maybe?. . . [[fuck]":
                if K_Action:
                    menu:
                        "What did you want to do?"
                        "Lean back, I've got something in mind. . .":
                                if P_Semen:
                                    call K_Sex_H   
                                else:
                                    "The spirit is apparently willing, but the flesh is spongy and bruised."
                        "Fuck your pussy.":    
                                if P_Semen:                    
                                    call K_Sex_P  
                                else:
                                    "The spirit is apparently willing, but the flesh is spongy and bruised."          
                        "Fuck your ass.":     
                                if P_Semen:                   
                                    call K_Sex_A    
                                else:
                                    "The spirit is apparently willing, but the flesh is spongy and bruised." 
#MOD MARKER doggy position menu choices
                        "Turn around, I've got something in mind. . . \[DoggyStyle\]":
                                if P_Semen:
                                    call K_Doggy_H   
                                else:
                                    "The spirit is apparently willing, but the flesh is spongy and bruised."
                        "Fuck your pussy. \[DoggyStyle\]":    
                                if P_Semen:                    
                                    call K_Doggy_P  
                                else:
                                    "The spirit is apparently willing, but the flesh is spongy and bruised."          
                        "Fuck your ass. \[DoggyStyle\]":     
                                if P_Semen:                   
                                    call K_Doggy_A    
                                else:
                                    "The spirit is apparently willing, but the flesh is spongy and bruised."

                        "How about some toys? [[Pussy]":                        
                                call K_Dildo_Pussy     
                        "How about some toys? [[Anal]":                        
                                call K_Dildo_Ass   
                        "Never mind [[something else]":
                                jump Kitty_SMenu
                else:
                        ch_k "Sorry [K_Petname], I'm a bit worn out."
                        
        "Hey, do you want in on this? [[Threesome]" if not Partner:
                    call Sex_Menu_Threesome("Kitty")
                    jump Kitty_SMenu

        "Cheat Menu" if config.developer:                                                   #Remove
            call Kitty_Cheat_Menu
        "Never mind. [[exit]":         
                if K_Lust >= 50 or K_Addict >= 50:
                        call KittyFace("sad")
                        if K_Action and K_SEXP >= 15 and Round > 20:
                                if "round2" not in K_RecentActions:  
                                    ch_k "Are you sure, [K_Petname]? I wasn't exactly. . . finished."                
                                    call Statup("Kitty", "Inbt", 30, 2)
                                    call Statup("Kitty", "Inbt", 50, 1)
                                elif K_Addict >= 50:                        
                                    ch_k "I need more touching." 
                                else:
                                    ch_k "I still need some more attention."                          
                                menu:
                                    extend ""
                                    "Yeah, I'm done for now." if P_Semen and "round2" not in K_RecentActions:                 
                                        if "unsatisfied" in K_RecentActions and not K_OCount:                                
                                            call KittyFace("angry")
                                            $ K_Eyes = "side" 
                                            call Statup("Kitty", "Love", 70, -2)
                                            call Statup("Kitty", "Love", 90, -4)
                                            call Statup("Kitty", "Obed", 30, 2)
                                            call Statup("Kitty", "Obed", 70, 1)
                                            ch_k "Rude!"
                                        else:                               
                                            call KittyFace("bemused", 1)
                                            call Statup("Kitty", "Obed", 50, 2)   
                                            ch_k "I guess I'll take what I can get. . ."  
                                    "I gave it a shot." if "round2" in K_RecentActions:                 
                                        if "unsatisfied" in K_RecentActions and not K_OCount:                                
                                            call KittyFace("angry")
                                            $ K_Eyes = "side"                                 
                                            ch_k "Rude!"
                                        else:                               
                                            call KittyFace("bemused", 1) 
                                            ch_k "I guess I'll take what I can get. . ."  
                                    "Hey, I did my part." if K_OCount > 2:      
                                        call KittyFace("sly", 1) 
                                        ch_k "Well. . . yeah, but. . ."  
                                    "I'm tapped out for the moment, let's try again later." if not P_Semen:
                                        call KittyFace("normal")                        
                                        ch_k "Yeah, but [K_like]. . ."
                                    "Ok, we can try something else." if MultiAction and "round2" not in K_RecentActions:
                                        call KittyFace("smile")
                                        call Statup("Kitty", "Love", 70, 2)
                                        call Statup("Kitty", "Love", 90, 1) 
                                        ch_k "Hehe. . ."                            
                                        $ K_RecentActions.append("round2")                      
                                        $ K_DailyActions.append("round2") 
                                        jump Kitty_SexMenu
                                    "Again? Ok, fine." if MultiAction and "round2" in K_RecentActions:
                                        call KittyFace("sly")
                                        ch_k "You know it. . ."           
                                        jump Kitty_SexMenu  
                                #End "if Kitty is still up for more"
                        else:  
                                call KittyFace("bemused", 1)
                                ch_k "I guess I'm kinda tired too, [K_Petname]. We can take a break. . ."   
                                ch_k ". . .for now."
                                call Statup("Kitty", "Inbt", 30, 2)
                                call Statup("Kitty", "Inbt", 50, 1)    
                        call KittyFace
                else:
                    ch_k "Ok, fine."
                    
                call Sex_Over  
#                $ K_OCount = 0    
#                call Kitty_Cleanup
#                call KittyOutfit
                return
    if K_Loc != bg_current:
        call Set_The_Scene
        $ Trigger = 0    
        $ Trigger2 = 0
        $ Trigger3 = 0
        $ Trigger4 = 0
        $ Trigger5 = 0
        return
    if not MultiAction:    
        call Set_The_Scene
        ch_k "That's it. . . for now."
        $ K_OCount = 0
        $ Trigger = 0    
        $ Trigger2 = 0
        $ Trigger3 = 0
        $ Trigger4 = 0
        $ Trigger5 = 0
        return
    call GirlsAngry
    jump Kitty_SexMenu
# end Kitty_SexMenu //////////////////////////////////////////////////////////////////////            

label Kitty_Cheat_Menu:
    menu:
        "Level-Up":
            $ K_Hand += 5
            $ K_Blow += 5
            $ K_Swallow += 5
            $ K_Hand += 5
            $ K_Slap += 5
            $ K_Tit += 5
            $ K_Sex += 5
            $ K_Anal += 5
            $ K_Hotdog += 5
            $ K_Mast += 5
            $ K_Org += 5
            $ K_FondleB += 5
            $ K_FondleT += 5
            $ K_FondleP += 5
            $ K_FondleA += 5
            $ K_DildoP += 5
            $ K_DildoA += 5
            $ K_Plug += 5
            $ K_SuckB += 5
            $ K_InsertP += 5
            $ K_InsertA += 5
            $ K_LickP += 5    
            $ K_LickA += 5
            $ K_Blow += 5
            $ K_Swallow += 5
            $ K_CreamP += 5
            $ K_CreamA += 5
            $ K_SeenChest = 1
            $ K_SeenPanties = 1
            $ K_SeenPussy = 1
            "Hand [K_Hand], Blow [K_Blow], Swallow [K_Swallow]"
        "Level Reset":
            $ K_Hand = 0
            $ K_Blow = 0
            $ K_Swallow = 0
            "Hand [K_Hand], Blow [K_Blow], Swallow [K_Swallow]"
        "Toggle Taboo":
            if not Taboo:
                $ Taboo = 40
            else:
                $ Taboo = 0
        "Maxed":
                $ K_Love = 1000
                $ K_Inbt = 1000
                $ K_Obed = 1000
                $ K_Lust = 50
                $ K_Addict = 0 #how addicted she is
                $ K_Addictionrate = 0 #How faster her addiciton rises
                $ K_Kissed = 1 #How many times they've kissed
                $ K_Swallow = 0
        "50\%":
                $ K_Love = 500
                $ K_Inbt = 500
                $ K_Obed = 500
                $ K_Lust = 65
                $ K_Addict = 0 #how addicted she is
                $ K_Addictionrate = 10 #How faster her addiciton rises
                $ K_Kissed = 10 #How many times they've kissed
                $ K_Swallow = 0
        "25\%":
                $ K_Love = 250
                $ K_Inbt = 250
                $ K_Obed = 250
                $ K_Lust = 85
                $ K_Addict = 10 #how addicted she is
                $ K_Addictionrate = 50 #How faster her addiciton rises
                $ K_Kissed = 10 #How many times they've kissed
                $ K_Swallow = 0
        "Juice up":
            $ P_Semen += 5
            $ K_Action = 10
        "Cold Shower":
            $ P_Focus = 0
        "Exit":
            return
    jump Kitty_Cheat_Menu
    return
  
label K_Jackin(Cnt = 0, TempVar = 0):
    if "unseen" in K_RecentActions:
            $ P_RecentActions.append("cockout") 
            $ Trigger2 = "jackin"
            "You whip out your cock and start working it." 
    else:
            if not P_Semen:
                "You don't think that would accomplish much, the poor thing is napping." 
                return
                
            if "cockout" in P_RecentActions:
                    "You start working your cock."
            else:
                    "You whip out your cock and start working it." 
                    $ P_RecentActions.append("cockout")
                    call Seen_First_Peen("Kitty",Partner) 
            
            $ Trigger2 = "jackin"
            if "jackin" in K_RecentActions:
                return            
            $ K_RecentActions.append("jackin")
            $ K_DailyActions.append("jackin") 
            
            if K_SEXP < 10:
                    call KittyFace("surprised", 2) 
                    $ K_Eyes = "down"
                    "Kitty blushes furiously, shocked at your behavior."  
                    call KittyFace("angry", 1) 
                    call Statup("Kitty", "Lust", 50, 5) 
                    if not ApprovalCheck("Kitty", 1200, TabM = 3):
                            $ K_RecentActions.append("angry")
                            $ K_DailyActions.append("angry")  
                            $ renpy.pop_call()
                            return
            elif K_SEXP <= 15:            
                    call KittyFace("surprised", 2) 
                    $ K_Eyes = "down"
                    "Kitty looks down at your cock with surprise."
                    call KittyFace("perplexed", 1) 
                    call Statup("Kitty", "Lust", 60, 8)
                    if not ApprovalCheck("Kitty", 1200, TabM = 3):
                            return
            elif ApprovalCheck("Kitty", 1200, TabM = 3):
                    call KittyFace("surprised", 1) 
                    $ K_Eyes = "down"
                    "Kitty looks down at your cock and smiles."            
                    call KittyFace("sly", 1) 
                    call Statup("Kitty", "Lust", 70, 8)
            elif ApprovalCheck("Kitty", 500, "I", TabM=2):
                    call KittyFace("surprised", 1) 
                    $ K_Eyes = "down"
                    "Kitty glances at it, but just smiles in amusement."        
                    call KittyFace("sly", 1) 
                    call Statup("Kitty", "Lust", 70, 10)
            else:
                    call KittyFace("angry", 1) 
                    $ K_Eyes = "down"
                    "Kitty glances down at your cock with a scowl."        
                    $ K_Eyes = "sexy"                
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")  
                    return
            
            if K_Action and K_Loc == bg_current:
                $ Options = ["none"]
                
                if K_Hand >= 5 and ApprovalCheck("Kitty", 1200, TabM = 3):
                        $ Cnt = K_Hand - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        while Cnt:
                            $ Options.append("hand") 
                            $ Cnt -= 1
                if K_Blow >= 5 and ApprovalCheck("Kitty", 1400, TabM = 3):
                        $ Cnt = K_Blow - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        $ Cnt += 5 if "hungry" in K_Traits else 0
                        while Cnt:
                            $ Options.append("blow") 
                            $ Cnt -= 1
                if K_Tit >= 5 and ApprovalCheck("Kitty", 1300, TabM = 5):
                        $ Cnt = K_Tit - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        while Cnt:
                            $ Options.append("Tit") 
                            $ Cnt -= 1
                if K_Sex >= 5 and ApprovalCheck("Kitty", 1500, TabM = 5):
                        $ Cnt = K_Sex - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        $ Cnt += 5 if K_Lust >= 70 else 0
                        while Cnt:
                            $ Options.append("sex") 
                            $ Cnt -= 1
                if K_Anal >= 5 and ApprovalCheck("Kitty", 1700, TabM = 5):
                        $ Cnt = K_Anal - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        $ Cnt += 5 if K_Lust >= 70 and K_Loose else 0
                        while Cnt:
                            $ Options.append("anal") 
                            $ Cnt -= 1
                    
                $ renpy.random.shuffle(Options) 
                                
                $ TempVar = Options[0]  
                $ del Options[:]  
                
                if TempVar == "hand":
                        ch_k "I could. . . lend you a hand?"
                elif TempVar == "blow":
                        ch_k "I could, get that wet for you. . ."
                elif TempVar == "tit":
                        ch_k "My chest might keep that warm. . ."
                elif TempVar == "sex":
                        ch_k "I'm getting a little wet. . ."
                elif TempVar == "anal":
                        ch_k "Why don't you bring that in through the back. . ."
                else:
                        ch_k "Prrrr. . ."
                        return
                    
                menu:
                    extend ""
                    "No thanks, I've got this in hand.":
                        ch_k "What ev, [K_Petname]."
                        return
                    "Hmm, sounds like a plan.": 
                        $ Situation = "shift"
                
                $ Trigger2 = 0
                    
                #Close out what you were doing 
                if Trigger == "strip":
                        call Group_Strip_End
                elif Trigger == "masturbation":
                        $ K_Action -= 1
                        $ K_Mast += 1    
                        call Checkout
                else:
                        call CloseOut("Kitty")
                
                show blackscreen onlayer black
                hide blackscreen onlayer black
                if TempVar == "hand":                
                        jump KHJ_Prep
                elif TempVar == "blow":
                        jump KBJ_Prep
                elif TempVar == "tit":
                        jump KTJ_Prep
                elif TempVar == "sex":
                        jump K_SexPrep
                elif TempVar == "anal":
                        jump K_AnalPrep
    return
# End Kitty "jackin it" action / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    
label K_TouchCheek:  
    call Shift_Focus("Kitty")
    call KittyFace("surprised", 1) 
    if "no cheek" in K_DailyActions:
        "You reach out to brush Kitty's face with your hand, but she slaps it away."
        call KittyFace("angry")
        ch_k "Hands off, dickbag."
        call Statup("Kitty", "Love", 50, -2)
        return
    else:
        "You reach out and brush Kitty's face with your hand."
    call Statup("Kitty", "Obed", 50, 1)    
    if "addict kitty" in P_Traits:
        $ K_Addict -= 2            
        $ K_Addictionrate += 1 if K_Addictionrate < 5 else K_Addictionrate 
        $ K_Addictionrate = 3 if K_Addictionrate < 3 else K_Addictionrate 
        call Statup("Kitty", "Lust", 70, 5)
    else:
        call Statup("Kitty", "Lust", 40, 5)
        
    if ApprovalCheck("Kitty", 1000):
        call KittyFace("sexy", 1)
        ch_k "Hmmm, what were you thinking, [K_Petname]?"
        call Statup("Kitty", "Love", 80, 1)
    elif ApprovalCheck("Kitty", 800) or ApprovalCheck("Kitty", 700, "L"):
        call KittyFace("smile", 1)
        ch_k "Sweet. . ."      
    elif "cheek" in K_DailyActions:        
        call KittyFace("angry", 1)
        ch_k "Hey, I warned you, [K_Petname]."
        call Statup("Kitty", "Love", 50, -2)
        $ K_DailyActions.append("no cheek")
    elif ApprovalCheck("Kitty", 400):
        $ K_Mouth = "smile"
        $ K_Brows = "normal"
        ch_k "Um, that was weird."
    else:
        call KittyFace("angry", 1)
        ch_k "Back off, weirdo."   
        call Statup("Kitty", "Love", 50, -3)
        call Statup("Kitty", "Obed", 50, 1)
        call Statup("Kitty", "Inbt", 30, 1)
    
    if "no cheek" in K_DailyActions: 
        menu:
            "Sorry, sorry, won't happen again.":
                if ApprovalCheck("Kitty", 300):
                    call KittyFace("sexy", 1)
                    ch_k "Yeah,[K_like]stop being weird."
                    call Statup("Kitty", "Love", 80, 2)
                else:
                    call KittyFace("angry", 1)
                    $ K_Eyes = "side"
                    ch_k "Uh-huh."                 
                    call Statup("Kitty", "Obed", 20, 1)   
                    
            "You know you wanted it.":
                if ApprovalCheck("Kitty", 400, "OI") or ApprovalCheck("Kitty", 800):
                    call KittyFace("normal", 1)
                    $ K_Eyes = "squint"
                    ch_k "Well. . . I didn't[K_like] {i}hate{/i} it. . ."
                    call Statup("Kitty", "Love", 60, -1) 
                    call Statup("Kitty", "Obed", 30, 2)                        
                    call Statup("Kitty", "Inbt", 40, 2)
                else:
                    call KittyFace("angry", 2)
                    $ K_Eyes = "squint"
                    ch_k "You wish."  
                    $ K_Blush = 1
                    call Statup("Kitty", "Love", 60, -3) 
                    call Statup("Kitty", "Obed", 30, 3)                        
                    call Statup("Kitty", "Inbt", 40, 2) 
    else:
        menu:
            "Sorry, you looked so cute there.":
                if ApprovalCheck("Kitty", 850, "LI"):
                    call KittyFace("sexy", 1)
                    ch_k "There better be more where that came from."
                    call Statup("Kitty", "Love", 80, 2)
                elif ApprovalCheck("Kitty", 500, "LI"):
                    call KittyFace("smile", 1)
                    ch_k "I'm not the only one looking cute, [K_Petname]."
                    call Statup("Kitty", "Love", 80, 2)
                else:
                    call KittyFace("angry", 1)
                    $ K_Eyes = "side"
                    ch_k "Too cute for you."                 
                    call Statup("Kitty", "Obed", 20, 1)   
                    
            "You had a fly on you.":
                if ApprovalCheck("Kitty", 700, "LI"):
                    call KittyFace("sexy", 1)
                    ch_k "Oh? [K_Like]sorry. . ."
                    call Statup("Kitty", "Love", 60, 1)                        
                    call Statup("Kitty", "Inbt", 40, 1)
                elif ApprovalCheck("Kitty", 700):
                    call KittyFace("normal")
                    ch_k "A fly, right. . ."
                else:
                    call KittyFace("angry", 1)
                    ch_k "Riiiight, just don't touch me." 
                    call Statup("Kitty", "Obed", 50, 2)    
                    
            "Are you sure you didn't enjoy that?":
                if ApprovalCheck("Kitty", 850):
                    call KittyFace("sexy", 1)
                    $ K_Eyes = "side"
                    ch_k "Maybe if there were more to it. . ."
                    call Statup("Kitty", "Obed", 50, 2)  
                    call Statup("Kitty", "Obed", 30, 1)                        
                    call Statup("Kitty", "Inbt", 40, 1)
                elif ApprovalCheck("Kitty", 500, "OI"):
                    call KittyFace("normal", 1)
                    ch_k "Well. . . I guess, maybe. . . no, quit it."
                    call Statup("Kitty", "Love", 60, -1)
                    call Statup("Kitty", "Obed", 50, 2)  
                    call Statup("Kitty", "Obed", 30, 2)                        
                    call Statup("Kitty", "Inbt", 40, 2)
                else:
                    call KittyFace("angry", 1)
                    $ K_Eyes = "side"
                    ch_k "Not interested."   
                    call Statup("Kitty", "Love", 60, -3)
                    call Statup("Kitty", "Obed", 50, 2)  
                    call Statup("Kitty", "Obed", 30, 3)                        
                    call Statup("Kitty", "Inbt", 40, 2)   
            
    $ K_RecentActions.append("cheek")
    $ K_DailyActions.append("cheek")
    return


label K_Headpat:  
    call Shift_Focus("Kitty")
    call KittyFace("surprised", 1)
    if "no headpat" in K_DailyActions:
        "You reach out to pat Kitty on the head, but she slips away before staring at you with a raised eyebrow."
        call KittyFace("angry")
        ch_k "I told you, weird."
        ch_k "Weirdo."
        call Statup("Kitty", "Love", 50, -2)
        return
    else:
        "You reach out and pat Kitty on the head."
    call Statup("Kitty", "Obed", 50, 2)    

    if ApprovalCheck("Kitty", 1200):
        call KittyFace("sexy", 1)
        ch_k "Mmmmm. . ."
        call Statup("Kitty", "Love", 85, 1)
    elif ApprovalCheck("Kitty", 900) or ApprovalCheck("Kitty", 750, "L"):
        call KittyFace("smile", 1)
        ch_k "Mmmmmm. . ."      
    elif "headpat" in K_DailyActions:        
        call KittyFace("angry", 1)
        ch_k "Hey, cut it out."
        call Statup("Kitty", "Love", 50, -2)
        $ K_DailyActions.append("no headpat")
    elif ApprovalCheck("Kitty", 400):
        $ K_Mouth = "smile"
        $ K_Brows = "normal"
        ch_k "Um, okay..."
    else:
        call KittyFace("angry", 1)
        "She slaps your hand aside and glares at you."
        ch_k "Knock it off!"  
        call Statup("Kitty", "Love", 50, -3)
        call Statup("Kitty", "Obed", 50, 1)
        call Statup("Kitty", "Inbt", 30, 1)
   
    if "no headpat" in K_DailyActions:
        menu:
            "Sorry, sorry, won't happen again.":
                if ApprovalCheck("Kitty", 300):
                    call KittyFace("sexy", 1)
                    call Statup("Kitty", "Love", 80, 2)
                    ch_k "Uh-huh."     
                else:
                    call KittyFace("angry", 1)
                    $ K_Eyes = "side" 
                    call Statup("Kitty", "Obed", 20, 1)  
                    ch_k "It'd better not."          

            "You know you wanted it.":
                if ApprovalCheck("Kitty", 400, "OI") or ApprovalCheck("Kitty", 800):
                    call KittyFace("normal", 1)
                    $ K_Eyes = "squint"
                    ch_k "Maaaaybe..." 
                    call Statup("Kitty", "Love", 60, -1)
                    call Statup("Kitty", "Obed", 30, 2)                        
                    call Statup("Kitty", "Inbt", 40, 2)
                else:
                    call KittyFace("sexy", 2)
                    $ K_Eyes = "squint"
                    ch_k "Um. . ."
                    $ K_Blush = 1
                    call Statup("Kitty", "Love", 60, -3)
                    call Statup("Kitty", "Obed", 30, 3)                        
                    call Statup("Kitty", "Inbt", 40, 2)
       
    else:
        menu:
            "Sorry, you looked so cute there.":
                if ApprovalCheck("Kitty", 850, "LI"):
                    call KittyFace("sexy", 1)
                    "She leans into it."
                    ch_k "Purrrrr. . ."
                    call Statup("Kitty", "Love", 80, 2)  
                    $ Count = 7
                elif ApprovalCheck("Kitty", 500, "LI"):
                    call KittyFace("smile", 1)
                    ch_k "Tell me something I don't know."
                    call Statup("Kitty", "Love", 80, 2)
                    $ Count = 5
                else:
                    call KittyFace("angry", 1)
                    $ K_Eyes = "side"
                    ch_k "Yeah, right. Pull the other one."                
                    call Statup("Kitty", "Obed", 20, 1)
                    $ Count = 1  
                   
            "You had a loose hair going on.":
                if ApprovalCheck("Kitty", 700, "LI"):
                    call KittyFace("sexy", 1)
                    ch_k "Loose hair? Me?"
                    call Statup("Kitty", "Love", 60, 1)                        
                    call Statup("Kitty", "Inbt", 40, 1)
                    $ Count = 4
                elif ApprovalCheck("Kitty", 700):
                    call KittyFace("normal")
                    ch_k "A hair, right. . ."
                    $ Count = 3
                else:
                    call KittyFace("angry", 1)
                    ch_k "Uhuh, just... just watch it, okay?"
                    call Statup("Kitty", "Obed", 50, 2)  
                    $ Count = 1  
                   
            "Are you sure you didn't enjoy that?":
                if ApprovalCheck("Kitty", 850):
                    call KittyFace("sexy", 1)
                    $ K_Eyes = "side"
                    ch_k "Hmmm... maybe, maybe not."
                    call Statup("Kitty", "Obed", 50, 2)  
                    call Statup("Kitty", "Obed", 30, 1)                        
                    call Statup("Kitty", "Inbt", 40, 1)
                    $ Count = 4
                elif ApprovalCheck("Kitty", 500, "OI"):
                    call KittyFace("normal", 1)
                    ch_k "Well. . . I guess, maybe. . . nah, nope."
                    call Statup("Kitty", "Love", 60, -1)
                    call Statup("Kitty", "Obed", 50, 2)  
                    call Statup("Kitty", "Obed", 30, 2)                        
                    call Statup("Kitty", "Inbt", 40, 2)
                    $ Count = 2
                else:
                    call KittyFace("angry", 1)
                    $ K_Eyes = "side"
                    ch_k "Grrrr. . ."  
                    call Statup("Kitty", "Love", 60, -3)
                    call Statup("Kitty", "Obed", 50, 2)  
                    call Statup("Kitty", "Obed", 30, 3)                        
                    call Statup("Kitty", "Inbt", 40, 2)
                    $ Count = 1
        while Count > 0 and Round >= 10:
            $ Count -= 1 if Count != 3 else 0
            $ Round -= 1
            menu:
                "Continue?"
                "Yes":
                    "You continue to hold your hand on top of Kitty's head, rubbing it softly."                    
                    if not Count:
                        if ApprovalCheck("Kitty", 800):
                            call KittyFace("bemused", 2)
                            call Statup("Kitty", "Love", 80, 2)                      
                            call Statup("Kitty", "Inbt", 40, 2)
                            ch_k "Hey, okay, I think that's enough. . ."
                            "She ducks out from under your hand."
                            call KittyFace("bemused", 1)
                        else:
                            call KittyFace("angry", 2)
                            call Statup("Kitty", "Love", 60, -5)                      
                            call Statup("Kitty", "Inbt", 40, 3)
                            ch_k "Ok, I think that's enough now. . ."
                            "She knocks your hand away."
                            call KittyFace("angry", 1)
                    elif Count == 1:
                        if ApprovalCheck("Kitty", 800):
                            call KittyFace("bemused", 1)
                            call Statup("Kitty", "Love", 80, 1)
                            call Statup("Kitty", "Obed", 50, 2)                        
                            call Statup("Kitty", "Inbt", 40, 2)
                            ch_k "We should probably do something else. . ."
                        else:
                            call KittyFace("angry", 2)
                            call Statup("Kitty", "Love", 60, -2)
                            call Statup("Kitty", "Obed", 60, 2)  
                            call Statup("Kitty", "Obed", 30, 2)  
                            ch_k "This Kitty has claws, you know."
                    else:
                        if ApprovalCheck("Kitty", 900):
                            call KittyFace("bemused", 2,Eyes="closed")
                            if Count > 3:
                                call Statup("Kitty", "Love", 90, 1)
                                call Statup("Kitty", "Love", 70, 1)
                                call Statup("Kitty", "Obed", 50, 1)
                                ch_k "Mmmmm. . ."
                                "She's practically purring."
                        else:
                            call KittyFace("angry", 1)
                            call Statup("Kitty", "Love", 60, -1)
                            call Statup("Kitty", "Obed", 50, 2)  
                            call Statup("Kitty", "Obed", 30, 2)                        
                            call Statup("Kitty", "Inbt", 40, 2)
                            ch_k "Um. . ."
                            $ Count -= 1 if Count > 2 else 0
                "No":
                    $ Count = 0
    $ Count = 0                
    $ K_RecentActions.append("headpat")
    $ K_DailyActions.append("headpat")
    return

# Slap Ass

#MOD MARKER SLAP
label K_Slap_Ass:
    call Shift_Focus("Kitty")
    # fix add sound here?
    if renpy.showing("Kitty_SexSprite"):
            show Kitty_SexSprite #fix, test this
            with vpunch
#MOD Kitty Doggy Slap
    elif renpy.showing("Kitty_Doggy"):
            show Kitty_Doggy #fix, test this
            with vpunch
    elif renpy.showing("Kitty_BJ_Animation"):           #fix, make this animation work better when paused for this effect.
            show Kitty_BJ_Animation
            with vpunch
    elif renpy.showing("Kitty_TJ_Animation"):
            show Kitty_TJ_Animation  
            with vpunch
    elif renpy.showing("Kitty_HJ_Animation"):
            show Kitty_HJ_Animation  
            with vpunch
    else:
            show Kitty_Sprite
            with vpunch
    $ K_Slap += 1                               #add in slap-base obedience        
    if ApprovalCheck("Kitty", 300, "O", TabM=1):   
        call KittyFace("sexy", 1)  
        $ K_Mouth = "surprised"
        call Statup("Kitty", "Lust", 51, 3, 1)
        if Action_Check("Kitty", "recent", "slap") < 4:
            call Statup("Kitty", "Lust", 200, 1)
            if K_Slap <= 5:
                    call Statup("Kitty", "Obed", 50, 2)
            if K_Slap <= 10:
                    call Statup("Kitty", "Obed", 80, 1)
        $ Line = "You slap her ass and she jumps with pleasure"
    else:                
        call KittyFace("surprised", 1)        
        if Action_Check("Kitty", "recent", "slap") < 4:
            call Statup("Kitty", "Obed", 70, 2)        
            call Statup("Kitty", "Love", 50, -1)
        $ Line = "You slap her ass and she looks back at you a bit startled"  
    
    if Taboo:    
        $ K_Blush = 2
        "[Line]."
        if not ApprovalCheck("Kitty", 900, TabM=2):
            if K_Slap <= 5:
                call Statup("Kitty", "Obed", 80, 2)  
                call Statup("Kitty", "Obed", 50, 2)      
            call Statup("Kitty", "Love", 70, -2)    
            call Statup("Kitty", "Love", 50, -1)
            $ Line = "She looks pretty mad though"  
        elif not ApprovalCheck("Kitty", 1500, TabM=2):
            if K_Slap <= 5:
                    call Statup("Kitty", "Obed", 80, 2)
            call Statup("Kitty", "Love", 70, -1)
            $ Line = "She looks a bit embarrassed"  
        else:                         #Over 1500
            call KittyFace("sexy")
            $ K_Mouth = "smile"
            if K_Slap <= 5:
                    call Statup("Kitty", "Obed", 80, 1)
            $ Line = "She gives you a naughty grin" 
        $ K_Blush = 1
        
    if not Trigger:
        "[Line]."
        $ Line = 0
        
    $ K_RecentActions.append("slap") if Action_Check("Kitty", "recent", "slap") < 4 else K_RecentActions
    $ K_DailyActions.append("slap") if Action_Check("Kitty", "daily", "slap") < 10 else K_DailyActions
        
    return
    
# Tag end ////////////////////////////////////////////////////////////////////////


# K_Makeout //////////////////////////////////////////////////////////////////////
label K_Makeout:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Kitty")
    
    $ Approval = ApprovalCheck("Kitty", 700, TabM=1) # 50, 65, 80, Taboo -40(90)
    
    if Approval > 1 and not K_Kissed and not K_Forced:        
        call KittyFace("sexy")
        $ K_Eyes = "side"
        ch_k "You are kinda cute. . ."
    if Approval and not K_Kissed:        
        call KittyFace("sexy")
        $ K_Eyes = "side"
        ch_k "I'll give it a go. . ."   
    elif Approval and "kissing" in K_RecentActions:
            call KittyFace("sexy", 1)
            ch_k "Prrr. . ."
            jump K_KissPrep
    elif Approval and "kissing" in K_DailyActions:
        call KittyFace("sexy", 1)
        $ Line = renpy.random.choice(["Meow.",       
            "Didn't get enough earlier?",
            "Come'ere tasty."]) 
        ch_k "[Line]"            
    elif Approval > 1 and K_Love > K_Obed:       
        call KittyFace("sexy")
        ch_k "Smooches!"            
    elif ApprovalCheck("Kitty", 500, "O") and K_Obed > K_Love:
        call KittyFace("normal")
        ch_k "Sure, ok."
        call Statup("Kitty", "Obed", 60, 1)
    elif ApprovalCheck("Kitty", 300, "O") and ApprovalCheck("Kitty", 200, "L"):
        call KittyFace("sexy")
        ch_k "Ok, fine."
        call Statup("Kitty", "Obed", 50, 3)
    elif K_Addict >= 50:
        call KittyFace("sexy")
        $K_Eyes = "manic"
        ch_k "I kinda have to."    
    elif Approval:       
        call KittyFace("bemused")
        ch_k "Yeah, whatever." 
    else:        
        call KittyFace("normal") # Else
        $ K_Mouth = "sad"
        ch_k "Nope."
        $ K_RecentActions.append("no kissing")                      
        $ K_DailyActions.append("no kissing") 
        return    
        
label K_KissPrep:    
    call Statup("Kitty", "Inbt", 10, 1)
    call Statup("Kitty", "Inbt", 20, 1)
    call K_Kissing_Launch("kiss you")
    if K_Kissed >= 10 and K_Inbt >= 300:
        call KittyFace("sucking")
    elif K_Kissed > 1 and K_Addict >= 50:
        call KittyFace("sucking")
    else:
        call KittyFace("kiss")
    if Situation == "Kitty":                                                      
            #Kitty auto-starts   
            $ Situation = 0
            "Kitty presses her body against yours, and kisses you passionately."
            menu:
                "What do you do?"
                "Go with it.":                    
                    call Statup("Kitty", "Inbt", 80, 3) 
                    call Statup("Kitty", "Inbt", 50, 2)
                    "You lean in to the kiss."
                "Praise her.":       
                    call KittyFace("sexy", 1)                    
                    call Statup("Kitty", "Inbt", 80, 3) 
                    ch_p "Mmm, this is a nice surprise, [K_Pet]."
                    call Kitty_Namecheck
                    "You lean in to the kiss."
                    call Statup("Kitty", "Love", 85, 1)
                    call Statup("Kitty", "Obed", 90, 1)
                    call Statup("Kitty", "Obed", 50, 2)
                "Ask her to stop.":
                    "You pull back."
                    call KittyFace("surprised")       
                    call Statup("Kitty", "Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [K_Pet]."
                    call Kitty_Namecheck
                    call Statup("Kitty", "Obed", 90, 1)
                    call Statup("Kitty", "Obed", 50, 1)
                    call Statup("Kitty", "Obed", 30, 2)
                    $ P_RecentActions.append("nope")      
                    call AnyWord("Kitty",1,"refused","refused")  
                    return          
            #end auto
    if K_Kissed >= 10:
        "She's all over you, licking all over your face and grinding against you."  
    elif K_Kissed > 7:
        "She's really sucking face."
    elif K_Kissed > 3:
        "She's really getting into it, her tongue's going at it."
    else:
        "You and Kitty make out for a while."    
    if Taboo:
        call DrainWord("Kitty","tabno")
    call DrainWord("Kitty","no kissing")
    $ K_RecentActions.append("kissing")                      
    $ K_DailyActions.append("kissing") 
    if not K_Kissed: 
        $ K_Addict -= 5       
        call Statup("Kitty", "Lust", 70, 5)
        call Statup("Kitty", "Love", 90, 10)
        call Statup("Kitty", "Love", 60, 25)            
        call Statup("Kitty", "Obed", 30, 20)
        call Statup("Kitty", "Inbt", 30, 20)
        jump K_Kiss_After
    $ Trigger = "kiss you"
    $ Line = 0
    $ Cnt = 0
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
     
label K_KissCycle:
    while Round >=0:
        call Shift_Focus("Kitty")
        call K_Kissing_Launch("kiss you")       
        call KittyLust   
            
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
                  
        if  P_Focus < 100:                                                    
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                pass                
                        "Slap her ass":                     
                                    call K_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump K_KissCycle  
                        
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                        
                        "Start jack'in it." if MultiAction and Trigger2 != "jackin":
                                call K_Jackin                        
                        "Stop jack'in it." if MultiAction and Trigger2 == "jackin":
                                "You stop jack'in it."
                                $ Trigger2 = 0
                                
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
                                                        "Move a hand to her breasts. . ." if K_Kissed >= 5 and MultiAction:
                                                                if K_Action and MultiAction:
                                                                    $ Situation = "auto"
                                                                    call K_Kiss_After
                                                                    call K_Fondle_Breasts                          
                                                                    if Trigger == "fondle breasts": 
                                                                        $ Trigger2 = "kiss you"                                   
                                                                        call KFB_Prep   
                                                                    else: 
                                                                        $ Trigger = "kiss you"     
                                                                else:
                                                                    "As your hands creep upwards, she grabs your wrists."
                                                                    ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"  
                                                        "Move a hand to her thighs. . ." if K_Kissed >= 5 and MultiAction:
                                                                if K_Action and MultiAction:
                                                                    $ Situation = "auto"
                                                                    call K_Kiss_After
                                                                    call K_Fondle_Thighs   
                                                                    if Trigger == "fondle thighs": 
                                                                        $ Trigger2 = "kiss you"      
                                                                        call KFT_Prep 
                                                                    else: 
                                                                        $ Trigger = "kiss you"     
                                                                else:
                                                                    "As your hands creep downwards, she grabs your wrists."
                                                                    ch_k "I'm actually getting a little tired, so maybe we could wrap this up?" 
                                                        "Never Mind":
                                                                jump K_KissCycle
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
                                                        jump K_KissCycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump K_KissCycle 
                                            "Never mind":
                                                        jump K_KissCycle 
                                    "Undress Kitty":
                                            call K_Undress   
                                    "Clean up Kitty (locked)" if not K_Spunk:
                                            pass  
                                    "Clean up Kitty" if K_Spunk:
                                            call Kitty_Cleanup("ask")                                         
                                    "Never mind":
                                            jump K_KissCycle 
                        
                        "Back to Sex Menu" if MultiAction and K_Kissed >= 5:  
                                ch_p "Let's try something else." 
                                $ Situation = "shift"
                                $ Line = 0
                                jump K_Kiss_After
                        "End Scene": 
                                ch_p "Let's stop for now."
                                $ Line = 0
                                jump K_Kiss_After
        #End menu (if Line)
        
        call Shift_Focus("Kitty")  
        call Sex_Dialog("Kitty",Partner)
        
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
                            if 100 > K_Lust >= 70 and K_OCount < 2 and K_SEXP >= 20:             
                                    $ K_RecentActions.append("unsatisfied")                      
                                    $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump K_Kiss_After 
                            $ Line = "came"
     
                    if K_Lust >= 100:       
                            #If you're still going at it and Kitty can cum
                            call K_Cumming
                            if Situation == "shift" or "angry" in K_RecentActions:
                                jump K_Kiss_After            
                    
                    #If you came
                    if Line == "came":
                            if not P_Semen:
                                "You're pretty wiped, better stop for now."
                            $ Line = 0
                            jump K_Kiss_After                 
                
        if Partner:
                call Partner_Cumming("Kitty")            
        #End orgasm
        
        call Escalation("Kitty","K") #sees if she wants to escalate things
        
        if Round == 10:
            ch_k "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_k "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0)
    $ Line = 0
    ch_k "Ok, [K_Petname], that's enough of that for now."
    
label K_Kiss_After:
    call KittyFace("sexy") 
    
    $ K_Kissed += 1
    $ K_Action -=1
    $ K_Addictionrate += 1
    if "addictive" in P_Traits:
        $ K_Addictionrate += 1        
    
    call Partner_Like("Kitty",1)
    
    if "kissing" not in K_RecentActions:
        if K_Love > 300:
            call Statup("Kitty", "Love", 60, 4)
        call Statup("Kitty", "Love", 70, 1)
        $ K_RecentActions.append("kissing")                      
        $ K_DailyActions.append("kissing") 
     
    if K_Kissed > 10: 
            pass        
    elif K_Kissed == 10:
            call KittyFace("smile", 1)        
            ch_k "I could eat you up."
    elif K_Kissed == 5:
            ch_k "You're good at this. . ." 
    elif K_Kissed == 1:    
            $ K_SEXP += 1 
        
    if not Situation and K_Kissed > 5 and K_Lust > 50 and ApprovalCheck("Kitty", 950):
            call KittyFace("sexy", 1)
            $K_Brows = "sad"
            ch_k "Is that it?"  
     
    $ Tempmod = 0  
    if Situation:
        ch_k "Mmm, so what else did you have in mind?"
    else:
        call K_Pos_Reset  
    call Checkout
    return


# end Makeout //////////////////////////////////////////////////////////////////////

            

##  K_Masturbating //////////////////////////////////////////////////////////////////////
# Cnt 1 means she's seen you, Cnt 0 means she hasn't.
label K_Masturbate: #(Situation = Situation):
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Kitty")
    if K_Mast:
        $ Tempmod += 10
    if K_SEXP >= 50:
        $ Tempmod += 25
    elif K_SEXP >= 30:
        $ Tempmod += 15
    elif K_SEXP >= 15:
        $ Tempmod += 5
    if K_Lust >= 90:
        $ Tempmod += 20
    elif K_Lust >= 75:
        $ Tempmod += 5
    if "exhibitionist" in K_Traits:      
        $ Tempmod += (3*Taboo) 
    if "dating" in K_Traits or "sex friend" in K_Petnames:
        $ Tempmod += 10
    elif "ex" in K_Traits:
        $ Tempmod -= 40  
    if K_ForcedCount and not K_Forced:        
        $ Tempmod -= 5 * K_ForcedCount   
        
    $ Approval = ApprovalCheck("Kitty", 1300, TabM = 2) # 120, 135, 150, Taboo -80(200)
    
    call DrainWord("Kitty","unseen",1,0) #She sees you, so remove unseens
    
    if Situation == "join":       # This triggers if you ask to join in        
                if Approval > 1 or (Approval and K_Lust >= 50):
                    menu:        
                        extend ""
                        "Would you like some help? I could lend some helping hands. . ."  if P_Semen and K_Action:
                                call Statup("Kitty", "Love", 90, 1)
                                call Statup("Kitty", "Obed", 50, 2)
                                call KittyFace("sexy")
                                ch_k "Um, you know, maybe start up top?"                  
                                call Statup("Kitty", "Obed", 70, 2)
                                call Statup("Kitty", "Inbt", 70, 1)
                                $ Trigger2 = "fondle breasts"
                                $ K_Mast += 1
                                jump KM_Cycle
                        "Would you like some help? I could. . . up to you, I guess." if P_Semen and K_Action:
                                call Statup("Kitty", "Love", 70, 2)
                                call Statup("Kitty", "Love", 90, 1)
                                call KittyFace("sexy")
                                ch_k "I'd[K_like]love it if you could give me a hand. . ."                
                                call Statup("Kitty", "Obed", 70, 2)
                                call Statup("Kitty", "Inbt", 70, 1)
                                $ D20 = renpy.random.randint(1, 20)
                                if D20 > 10:
                                    $ Trigger2 = "fondle breasts"
                                else:
                                    $ Trigger2 = "suck breasts"
                                $ K_Mast += 1
                                jump KM_Cycle
                        "Why don't we take care of each other?" if P_Semen and K_Action:
                                call KittyFace("sexy")
                                ch_k "I think I could help with that. . ."                    
                                $ renpy.pop_call()          #removes the call to this label 
                                return                      #returns to sexmenu=
                        "You look like you have things well in hand. . .":
                                if K_Lust >= 50:
                                    call Statup("Kitty", "Love", 70, 2)
                                    call Statup("Kitty", "Love", 90, 1)      
                                    call KittyFace("sexy")
                                    ch_k "Well {i}I{/i} think so. . ."                    
                                    call Statup("Kitty", "Obed", 80, 3)
                                    call Statup("Kitty", "Inbt", 80, 5)  
                                    jump KM_Cycle
                                elif ApprovalCheck("Kitty", 1200):
                                    call KittyFace("sly")                        
                                    ch_k "Yeah. . . but I think I'm kinda done. . ."
                                else:
                                    call KittyFace("angry")
                                    ch_k "Hrmph, yeah, I kinda {i}did.{/i}"
                                    
                #else: You've failed all checks so she kicks you out.
                $ Kitty_Arms = 1  
                call KittyOutfit  
                $ K_Action -= 1
                call Statup("Player", "Focus", 50, 30)
                call Checkout(1)
                $ Line = 0
                $ Situation = 0      
                $ renpy.pop_call()          #removes the call to this label 
                if Approval:     
                        call KittyFace("bemused", 2)
                        if bg_current == "bg kitty":
                            ch_k "So what are you[K_like]even doing here?"   
                        else:
                            ch_k "I[K_like]didn't expect to see you here. . ." 
                        $ K_Blush = 1
                else:
                        call Statup("Kitty", "Love", 200, -5)
                        call KittyFace("angry")
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")  
                        if bg_current == "bg kitty":
                            ch_k "So in case you couldn't tell, I was a little {i}busy?{/i} Maybe knock sometime?"
                            "Kitty kicks you out of her room."
                            $ renpy.pop_call()
                            jump Campus_Map  
                        else:
                            ch_k "So. . . I'm getting out of here? Maybe knock sometime?"
                            hide Kitty with easeoutbottom
                            call Remove_Girl("Kitty")
                return                      #returns to sexmenu, which returns to original    
    #End of "Join" option
    
    
    
    if Situation == "Kitty":                                                                  #Kitty auto-starts   
                if Approval > 2:                                                      # fix, add kitty auto stuff here
                        if K_Legs == "blue skirt":
                            "Kitty's hand snakes down her body, and hikes up her skirt."
                            $ K_Upskirt = 1
                        elif K_Legs == "pants":
                            "Kitty slides her hand down her body and into her jeans."  
                        elif HoseNum("Kitty") >= 5:
                            "Kitty's hand slides down her body and under her [K_Hose]."
                        elif K_Panties:                
                            "Kitty's hand slides down her body and under her [K_Panties]."
                        else:
                            "Kitty's hand slides down her body and begins to caress her pussy."
                        $ K_SeenPanties = 1
                        "She starts to slowly rub herself."
                        call Kitty_First_Bottomless
                        menu:
                            "What do you do?"
                            "Nothing.":                    
                                    call Statup("Kitty", "Inbt", 80, 3) 
                                    call Statup("Kitty", "Inbt", 60, 2)
                                    "Kitty begins to masturbate."
                            "Go for it.":       
                                    call KittyFace("sexy, 1")                    
                                    call Statup("Kitty", "Inbt", 80, 3) 
                                    ch_p "That is so sexy, [K_Pet]."
                                    call Kitty_Namecheck
                                    "You lean back and enjoy the show."
                                    call Statup("Kitty", "Love", 80, 1)
                                    call Statup("Kitty", "Obed", 90, 1)
                                    call Statup("Kitty", "Obed", 50, 2)
                            "Ask her to stop.":
                                    call KittyFace("surprised")       
                                    call Statup("Kitty", "Inbt", 70, 1) 
                                    ch_p "Let's not do that right now, [K_Pet]."
                                    call Kitty_Namecheck
                                    "Kitty pulls her hands away from herself."
                                    call KittyOutfit
                                    call Statup("Kitty", "Obed", 90, 1)
                                    call Statup("Kitty", "Obed", 50, 1)
                                    call Statup("Kitty", "Obed", 30, 2)
                                    return            
                        jump KM_Prep
                else:                
                        $ Tempmod = 0                               # fix, add kitty auto stuff here
                        $ Trigger2 = 0
                return            
    #End if Kitty intitiates this action
    
    #first time
    if not K_Mast:                                                                
            call KittyFace("surprised", 1)
            $ K_Mouth = "kiss"
            ch_k "You want me to. . . touch myself?"
            ch_k "And you're going to . . .watch?"
            if K_Forced:
                call KittyFace("sad")
                ch_k "So you {i}just{/i} want to watch. . ."
            
            
    #First time dialog             
    if not K_Mast and Approval:                                                      
            if K_Forced: 
                call KittyFace("sad")
                call Statup("Kitty", "Love", 70, -3, 1)
                call Statup("Kitty", "Love", 20, -2, 1)
            elif K_Love >= K_Obed and K_Love >= K_Inbt:
                call KittyFace("sexy")
                $ K_Brows = "sad"
                $ K_Mouth = "smile" 
                ch_k "This is kind of {i}intimate{/i} . . ."          
            elif K_Obed >= K_Inbt:
                call KittyFace("normal")
                ch_k "Ok by me, [K_Petname]. . ."            
            else: # Uninhibited 
                call KittyFace("sad")
                $ K_Mouth = "smile"             
                ch_k "This could be kinda fun . . ."     
    
    
    #Second time+ initial dialog
    elif Approval:                                                                       
            if K_Forced: 
                call KittyFace("sad")
                call Statup("Kitty", "Love", 70, -3, 1)
                call Statup("Kitty", "Love", 20, -2, 1)
                ch_k "Again? Just looking?"  
            elif Approval and "masturbation" in K_RecentActions:
                call KittyFace("sexy", 1)
                ch_k "I guess I could give it another go. . ."    
                jump KM_Prep
            elif Approval and "masturbation" in K_DailyActions:
                call KittyFace("sexy", 1)
                $ Line = renpy.random.choice(["Was it that good?",       
                    "Didn't get enough earlier?",
                    "I kinda liked the audience. . ."]) 
                ch_k "[Line]"            
            elif K_Mast < 3:        
                call KittyFace("sexy", 1)
                $ K_Brows = "confused"
                ch_k "Did you. . . like it last time?"       
            else:       
                call KittyFace("sexy", 1)
                $ Kitty_Arms = 2
                $ Line = renpy.random.choice(["You really like to watch.",                 
                    "Again?",                 
                    "You like to watch me.",
                    "You want me to get myself off?"]) 
                ch_k "[Line]"
                $ Line = 0
    #End second time+ initial dialog
    
    #If she's into it. . .  
    if Approval >= 2:                                                                                
            if K_Forced:
                call KittyFace("sad")
                call Statup("Kitty", "Obed", 90, 1)
                call Statup("Kitty", "Inbt", 60, 1)
                ch_k "Fine. . ." 
            else:
                call KittyFace("sexy", 1)
                call Statup("Kitty", "Love", 90, 1)
                call Statup("Kitty", "Inbt", 50, 3) 
                $ Line = renpy.random.choice(["Huh. Ok.",                 
                    "Couldn't hurt having you around. . .",
                    "Two birds with one stone. . .",
                    "K.", 
                    "Sure, why not?",
                    "Lol, ok."]) 
                ch_k "[Line]"
                $ Line = 0
            call Statup("Kitty", "Obed", 20, 1)
            call Statup("Kitty", "Obed", 60, 1)
            call Statup("Kitty", "Inbt", 70, 2) 
            jump KM_Prep   
            
    #If she's not into it, but maybe. . .    
    else:                                                                                       
        menu:
            ch_k "That's. . . private? You know?"
            "Maybe later?":
                    call KittyFace("sexy", 1)  
                    if K_Lust > 70:                        
                        ch_k "Well, I know what {i}I'll{/i} be doing later. Not sure if you can come."
                        ch_k "I mean-  you know, be there."                        
                        ch_k "I'm not sure you'll {i}be{/i} there."
                        ch_k ". . .coming."                  
                    else:
                        ch_k "Hmm, maybe. . . I'll text you?"
                    call Statup("Kitty", "Love", 80, 2)
                    call Statup("Kitty", "Inbt", 70, 2)               
                    return
            "You look like you could use it. . .":             
                    if Approval:
                        call KittyFace("sexy")     
                        call Statup("Kitty", "Obed", 90, 2)
                        call Statup("Kitty", "Obed", 50, 2)
                        call Statup("Kitty", "Inbt", 70, 3) 
                        call Statup("Kitty", "Inbt", 40, 2) 
                        $ Line = renpy.random.choice(["Huh. Ok.",                 
                                "Couldn't hurt having you around. . .",
                                "Two birds with one stone. . .",
                                "K.", 
                                "Sure, why not?",
                                "Lol, ok."]) 
                        ch_k "[Line]"
                        $ Line = 0                   
                        jump KM_Prep
                    else:   
                        pass
                    
            "Just get at it already.":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Kitty", 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                    if Approval > 1 or (Approval and K_Forced):
                        call KittyFace("sad")
                        call Statup("Kitty", "Love", 70, -5, 1)
                        call Statup("Kitty", "Love", 200, -5)                 
                        ch_k "Fiiine, geeze."  
                        call Statup("Kitty", "Obed", 80, 4)
                        call Statup("Kitty", "Inbt", 80, 1) 
                        call Statup("Kitty", "Inbt", 60, 3)  
                        $ K_Forced = 1  
                        jump KM_Prep
                    else:                              
                        call Statup("Kitty", "Love", 200, -20)     
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")
    # end of asking her to do it
    
    #She refused all offers.
    $ Kitty_Arms = 1                
    if K_Forced:
            call KittyFace("angry", 1)
            ch_k "I. . . can't, not with you watching."
            call Statup("Kitty", "Lust", 90, 5)         
            if K_Love > 300:
                call Statup("Kitty", "Love", 70, -2)
            call Statup("Kitty", "Obed", 50, -2)    
            $ K_RecentActions.append("angry")
            $ K_DailyActions.append("angry")   
            $ K_RecentActions.append("no masturbation")                      
            $ K_DailyActions.append("no masturbation") 
            return
    elif Taboo:                             # she refuses and this is too public a place for her
            call KittyFace("angry", 1)          
            $ K_DailyActions.append("tabno") 
            ch_k "Certainly not here!"     
            call Statup("Kitty", "Lust", 90, 5)  
            call Statup("Kitty", "Obed", 50, -3)    
            return                
    elif K_Mast:
            call KittyFace("sad") 
            ch_k "Sorry, maybe try a porn game or something."     
    else:
            call KittyFace("normal", 1)
            ch_k "Um, no."  
    $ K_RecentActions.append("no masturbation")                      
    $ K_DailyActions.append("no masturbation") 
    $ Tempmod = 0 
    return

label KM_Prep: 
    $ K_Upskirt = 1    
    $ K_PantiesDown = 1 
    call Kitty_First_Bottomless(1)
    call Set_The_Scene(Dress=0)   
    
    #if she hasn't seen you yet. . .
    if "unseen" in K_RecentActions:
            call KittyFace("sexy")
            $ K_Eyes = "closed"
            $ Kitty_Arms = 2
            "You see Kitty leaning back, masturbating. You don't think she's noticed you yet."
    else:    
            call KittyFace("sexy")
            $ Kitty_Arms = 2
            "Kitty lays back and starts to toy with herself."
            if not K_Mast:#First time        
                    if K_Forced:
                        call Statup("Kitty", "Love", 90, -20)
                        call Statup("Kitty", "Obed", 70, 45)
                        call Statup("Kitty", "Inbt", 80, 35) 
                    else:
                        call Statup("Kitty", "Love", 90, 15)
                        call Statup("Kitty", "Obed", 70, 35)
                        call Statup("Kitty", "Inbt", 80, 40)  
        
    
    $ Trigger = "masturbation"   
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0 
    $ Line = 0
    if Taboo:
        call DrainWord("Kitty","tabno")
    call DrainWord("Kitty","no masturbation")
    $ K_RecentActions.append("masturbation")                      
    $ K_DailyActions.append("masturbation") 
            
label KM_Cycle:      
    if Situation == "join":
        $ renpy.pop_call() 
        $ Situation = 0 
        
    while Round >=0:  
        call K_Pos_Reset("masturbation")
        call Shift_Focus("Kitty") 
        call KittyLust  
        if "unseen" in K_RecentActions:  
                $ K_Eyes = "closed"
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if  P_Focus < 100:                                                    
                    #Player Command menu                                        
                    menu:
                        "Keep Watching.":
                                pass
                                
                        "Kitty. . .[[jump in]" if "unseen" not in K_RecentActions and K_Loc == bg_current:                 
                                "Kitty slows what she's doing with a sly grin."
                                ch_k "Like what you see?"
                                $ Situation = "join"
                                call K_Masturbate               
                        "\"Ahem. . .\"" if "unseen" in K_RecentActions and K_Loc == bg_current:  
                                jump KM_Interupted    
                                                   
                        "Start jack'in it." if Trigger2 != "jackin":
                                call K_Jackin                   
                        "Stop jack'in it." if Trigger2 == "jackin":
                                $ Trigger2 = 0    
                                            
                        "Slap her ass" if K_Loc == bg_current:    
                                if "unseen" in K_RecentActions:
                                        "You smack Kitty firmly on the ass!"
                                        jump KM_Interupted                                          
                                else:
                                        call K_Slap_Ass                                        
                                        $ Cnt += 1
                                        $ Round -= 1    
                                        jump KM_Cycle  
                           
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                    
                        "Change what I'm doing":
                                menu:
                                    "Offhand action" if K_Loc == bg_current:
                                            if K_Action and MultiAction:
                                                call Kitty_Offhand_Set
                                                if Trigger2:
                                                     $ K_Action -= 1
                                            else:
                                                ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"  
                                                           
                                    "Threesome actions (locked)" if not Partner or "unseen" in K_RecentActions or K_Loc != bg_current: 
                                        pass
                                    "Threesome actions" if Partner and "unseen" not in K_RecentActions and K_Loc == bg_current:   
                                        menu:
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Kitty")      
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Kitty")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump KM_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump KM_Cycle 
                                            "Never mind":
                                                        jump KM_Cycle 
                                    "Undress Kitty":
                                            if "unseen" in K_RecentActions:
                                                    ch_p "Oh, yeah, take it off. . ."
                                                    jump KM_Interupted
                                            else:                                        
                                                    call K_Undress   
                                    "Clean up Kitty (locked)" if not K_Spunk:
                                            pass  
                                    "Clean up Kitty" if K_Spunk:
                                            if "unseen" in K_RecentActions:
                                                    ch_p "You've got a little something on you. . ."
                                                    jump KM_Interupted
                                            else:                      
                                                    call Kitty_Cleanup("ask")                                         
                                    "Never mind":
                                            jump KM_Cycle                               
                         
                        "Back to Sex Menu" if MultiAction and K_Loc == bg_current: 
                                    ch_p "Let's try something else."
                                    call K_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump KM_Interupted
                        "End Scene" if not MultiAction or K_Loc != bg_current: 
                                    ch_p "Let's stop for now."
                                    call K_Pos_Reset
                                    $ Line = 0
                                    jump KM_Interupted
        #End menu (if Line)
        
        call Shift_Focus("Kitty")  
        call Sex_Dialog("Kitty",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or K_Lust >= 100:   
                    #If you can cum:
                    if P_Focus >= 100:
                        if "unseen" not in K_RecentActions: 
                            #if she knows you're there
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
                            if K_Loc == bg_current:
                                    jump KM_Interupted
     
                    #If Kitty can cum
                    if K_Lust >= 100:                                               
                        call K_Cumming
                        if K_Loc == bg_current:
                                jump KM_Interupted
                       
                    if Line == "came": 
                        $ Line = 0
                        if not P_Semen:
                            "You're emptied out, you should probably take a break."
                            $ Trigger2 = 0 if Trigger2 == "jackin" else Trigger2
                            
                            
                        if "unsatisfied" in K_RecentActions:#And Kitty is unsatisfied,  
                            "Kitty still seems a bit unsatisfied with the experience."
                            menu:
                                "Let her keep going?"
                                "Yes, keep going for a bit.":
                                    $ Line = "You let her get back into it" 
                                    jump KM_Cycle  
                                "No, I'm done.":
                                    "You ask her to stop."
                                    return
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Kitty")                 
        #End orgasm
        
        if "unseen" in K_RecentActions:
                if Round == 10:
                    "It's getting a bit late, Kitty will probably be wrapping up soon."  
                elif Round == 5:
                    "She's definitely going to stop soon."
        else:
                if K_Loc == bg_current:
                        call Escalation("Kitty","K") #sees if she wants to escalate things
        
                if Round == 10:
                    ch_k "We might want to wrap this up, it's getting late."  
                    $ K_Lust += 10
                elif Round == 5:
                    ch_k "Seriously, it'll be time to stop soon."     
                    $ K_Lust += 25   
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0)
    $ Line = 0
    if "unseen" not in K_RecentActions:
        ch_k "Ok, I'm kinda done for now, I need a break."
    
label KM_Interupted:
    
    # If she hasn't noticed you're there before cumming
    if "unseen" in K_RecentActions:                         
                call KittyFace("surprised", 2)
                "Kitty stops what she's doing with a start, eyes wide."
                call Kitty_First_Bottomless(1) 
                call KittyFace("surprised", 2)
                
                #If you've been jacking it
                if Trigger2 == "jackin":
                        ch_k "Eeep!"
                        ch_k "When did you get here?!"
                        $ K_Eyes = "down"
                        menu:
                            ch_k "And um. . . your cock is out. . . "
                            "A while back, it was an excellent show.":   
                                    call KittyFace("sexy",1)
                                    call Statup("Kitty", "Obed", 50, 3)
                                    call Statup("Kitty", "Obed", 70, 2)
                                    ch_k "Um, I mean. . . yeah. . ."
                                    if K_Love >= 800 or K_Obed >= 500 or K_Inbt >= 500:
                                        $ Tempmod += 10
                                        call Statup("Kitty", "Lust", 90, 5)
                                        ch_k "I um. . . like what I'm seeing too. . ."  
                                    
                            "I. . . just got here?":
                                    call KittyFace("angry",1)                   
                                    call Statup("Kitty", "Love", 70, 2)
                                    call Statup("Kitty", "Love", 90, 1)
                                    call Statup("Kitty", "Obed", 50, 2)
                                    call Statup("Kitty", "Obed", 70, 2)
                                    "She looks pointedly at your cock,"
                                    ch_k "Long enough to whip that out?"   
                                    if K_Love >= 800 or K_Obed >= 500 or K_Inbt >= 500:
                                            $ Tempmod += 10
                                            call Statup("Kitty", "Lust", 90, 5)
                                            call KittyFace("bemused", 1)
                                            ch_k "I, um, guess I should be flattered?"   
                                    else:
                                            $ Tempmod -= 10
                                            call Statup("Kitty", "Lust", 200, -5)
                        call Seen_First_Peen("Kitty",Partner) 
                                    
                #you haven't been jacking it                    
                else:         
                        ch_k "Eeep!"
                        ch_k "When did you get here?!"    
                        menu:
                            extend ""
                            "A while back.":   
                                    call KittyFace("sexy", 1)
                                    call Statup("Kitty", "Obed", 50, 3)
                                    call Statup("Kitty", "Obed", 70, 2)
                                    ch_k "I hope I kept you entertained. . ."
                            "I just got here.":
                                    call KittyFace("bemused", 1)
                                    call Statup("Kitty", "Love", 70, 2)
                                    call Statup("Kitty", "Love", 90, 1)                    
                                    ch_k "Yeah, I just bet. . ."   
                                    call Statup("Kitty", "Obed", 50, 2)
                                    call Statup("Kitty", "Obed", 70, 2)    
                                
                call DrainWord("Kitty","unseen",1,0) #She sees you, so remove unseens
                $ K_Mast += 1
                if Round <= 10:
                    ch_k "It's getting kinda late to do anything about it. . ."
                    return
                $ Situation = "join"        
                call K_Masturbate
                "error: report this if you see it."
                return #should be redundant
    #End Unseen
    
    #else, if She's seen you already    
    $ K_Action -= 1
    $ K_Mast += 1    
    call Checkout
    if Situation == "shift":        
        $ Situation = 0
        return
    $ Situation = 0
        
    call Partner_Like("Kitty",3)
        
    if K_Loc != bg_current:
        return
            
    if Round <= 10:
            ch_k "Gimme a minute, I need to collect myself here. . ."
            return
    call KittyFace("sexy", 1)
    if K_Lust < 20:
        ch_k "Well that worked for me, how 'bout you?"
    else:
        ch_k "Um, yeah?"
    menu:
        extend ""
        "Well, I have something you could take care of. . ." if P_Semen and K_Action:
                $ Situation = "shift"
                return   
        "You could just keep going. . ." if P_Semen:
                call KittyFace("sly")
                if K_Action and Round >= 10:
                    ch_k "Sure. . ."
                    jump KM_Cycle
                else:
                    ch_k "Gimme a minute, I need to collect myself here. . ."
        "I'm good here. [[Stop]":  
                if K_Love < 800 and K_Inbt < 500 and K_Obed < 500:
                    call KittyOutfit
                call KittyFace("normal")
                $ K_Brows = "confused"
                ch_k "Well. . . ok. . ."
                $ K_Brows = "normal" 
        "You should probably stop for now." if K_Lust > 30:
                call KittyFace("angry")
                ch_k "I guess? . ."
    return
    
## end K_Masturbating ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




# Kitty_Offhand function //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


label Kitty_Offhand(TempLine=0):
    #This is the dialog for what you're doing with your other hand while a primary action takes place
    
    $ D20 = renpy.random.randint(1, 20)                                                                 # Taboo caught check
                    
    if not Trigger2: #If there are no offhand options set, return
        return    
    
    if Trigger2 == "kiss you":
                $ Line = renpy.random.choice([" Your lips gently slide across hers.", 
                        " Her lips part as you hold her close.",    
                        " You nibble her neck as she groans in pleasure.",
                        " You squeeze her tightly as your tongues jostle.",
                        " Her tongue dances around yours.",
                        " She nibbles your ear as her hands slide across your back.",
                        " Your hands slide down her body as your lips press hers.",
                        " You kiss her passionately.", 
                        " Your tongues swirl around each other's."])
                if K_Love >= 300:
                        call Statup("Kitty", "Love", 75, 1)
                $ PrimaryLust += 2 if K_Lust < 50 else 1
        
    elif Trigger2 == "fondle breasts":
                $ Line = renpy.random.choice([" You reach out and massage her pert breasts.", 
                        " You pass your hands gently over her warm breasts.", 
                        " Her nipples catch lightly on your fingers as you grasp her warm flesh, you can feel them stiffen.",
                        " She gasps as you lightly thumb her tight nipples."])
                $ PrimaryLust += 3           
                $ TempFocus += 2 if P_Focus < 90 else 0 
        
    elif Trigger2 == "suck breasts":
            if K_Chest:
                $ Line = renpy.random.choice([" You bend down and motor-boat her breasts.",
                    " You tease her nipples with your tongue through her top.",
                    " You slowly lick her nipples through her moist top.", 
                    " you gently place a nipple between your lips, and draw it out until it releases with a *pop*.",
                    " She gasps as you lightly lick her rigid nipples, poking through her top."])            
            else:
                $ Line = renpy.random.choice([" You bend down and motor-boat her breasts.",
                    " You gently nibble at her nipples as you suck on them.",
                    " You tease her nipples with your tongue.",
                    " You slowly lick around, and then blow across her nipples.", 
                    " You gently place a nipple between your lips, and draw it out until it releases with a *pop*.",
                    " She gasps as you lightly lick her rigid nipples."])
            $ PrimaryLust += 4 if 60 < K_Lust < 80 else 2  
            $ TempFocus += 3 if P_Focus < 90 else 0 
        
    elif Trigger2 == "fondle pussy":
            
            $ Line = renpy.random.choice([" You put your hand against her mound and grind against it.", 
                        " You reach into her gap and she gasps as you slide your hand across and stroke her lips.", 
                        " Her legs twitch a bit as you press your thumb against her.",
                        " You slide a hand up her inner thigh, she moans a little as you reach the point where they meet."])
            $ PrimaryLust += 4 if 60 < K_Lust < 90 else 2        
            $ TempFocus += 4 if P_Focus < 90 else 0 
        
    elif Trigger2 == "lick pussy":
            if K_Legs != "pants" and not K_Panties:  
                $ Line = renpy.random.choice([" You slide your tongue into her pussy and flick the roof with deft strokes.", 
                    " You spread the lips back and she gasps as you slide your tongue between them.", 
                    " You can feel her twitching as you grind your tongue against her clit.",
                    " She gasps as you suck on her clit.",
                    " You rub her clit with your thumb as you dive into her pussy with your tongue.",
                    " With a little nibble, you tug on her lower lips.",
                    " You slowly lick into her gap and she gasps as you press the walls aside."])
            else:
                $ Line = renpy.random.choice([" You spread the lips back beneath the thin fabric, and she gasps as you slide your tongue across them.", 
                    " She gasps as you suck on her clit through the fabric.",
                    " You rub her clit with your thumb as you press against her pussy with your tongue.",
                    " You put your hand against her mound and lick the juice that's collected.", 
                    " With a little nibble, you tug back the fabric.",
                    " You slowly lick into her gap and she gasps as you press the walls aside."])
            $ PrimaryLust += 5 if K_Lust > 50 else 2       
            $ TempFocus += 4 if P_Focus < 90 else 0 
            
    elif Trigger2 == "fondle ass":
            if K_Legs != "pants" and not K_Panties: 
                $ Line = renpy.random.choice([" You reach out and brush your hands across her bare ass.", 
                        " You put your hand against her firm rear and grind against it.", 
                        " You reach into her gap and she gasps as you slide your hand across and stroke her puckered hole.", 
                        " Her legs twitch a bit as you press your thumb against her.",
                        " She gasps as you reach under her and lightly stroke her ass.",
                        " You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks."])
            else:
                $ Line = renpy.random.choice([" You reach out and brush your hands across her ass.", 
                        " You put your hand against her firm rear and grind against it.", 
                        " You reach into her gap and she gasps as you slide your hand across and stroke her puckered hole.", 
                        " Her legs twitch a bit as you press your thumb against her.",
                        " She gasps as you reach under her and lightly stroke her ass.",
                        " You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks."])
            $ PrimaryLust += 2 if K_Lust < 50 else 1
            $ TempFocus += 1 if P_Focus < 50 else 0  
            $ TempFocus += 1 if P_Focus < 80 else 0   
        
    elif Trigger2 == "insert ass":
            $ Line = renpy.random.choice([" You reach out and slide a finger into her ass.", 
                    " You slide a finger into her asshole and stroke the roof of it.", 
                    " You can feel her twitching as you press your thumb against her clit.",
                    " She gasps as you rub her asshole with your fingers.",
                    " You rub her pussy with your thumb as you dive into her asshole with your middle finger.",
                    " You reach into her gap and she gasps as you slide your hand across and press against her hole.", 
                    " She gasps as you reach under her warm lips and lightly stroke her ass."])       
            $ PrimaryLust += 3 if K_Lust > 70 and K_Loose else 1
            $ TempFocus += 2 if P_Focus < 90 else 0 
        
    elif Trigger2 == "jackin":
            if Trigger == "masturbation":
                    $ Line = " You stroke your cock as you watch her go."
            elif Trigger == "lesbian":
                    $ Line = " You stroke your cock as you watch them."
            elif Trigger == "hand":
                    $ Line = renpy.random.choice([" You also give it a little rub.", 
                            " As she does so, you polish the knob a bit.", 
                            " You help.",
                            " Your hand bumps into hers occasionally."])     
            elif Trigger == "blow":
                    if Speed >= 3:
                        $ Line = "."
                    else:
                        $ Line = renpy.random.choice([" You also give it a little rub.", 
                            " As she does so, you work the shaft a bit.", 
                            " Your fingers brush her lips.",
                            " Her lips brush your hand occasionally."])    
            else:
                    $ Line = renpy.random.choice([" With your other hand, you stroke your shaft.", 
                            " You stroke your cock with your other hand.", 
                            " As you do, you stoke yourself."])            
            if "unseen" not in K_RecentActions:
                $ PrimaryLust += 3 if 20 < K_Lust < 70 else 2
                $ TempFocus += 1 if P_Focus < 70 else 0            
            $ TempFocus += 5
               
    return                      #End Kitty_Offhand check
    


label Kitty_Offhand_Set(Situation = Situation, TempTrigger = Trigger2):
    
    if Situation == "shift focus":        
            if TempTrigger:      
                $ Trigger2 = 0  
#                $ Situation = 0
                if TempTrigger == "fondle breasts":
                        "You shift your attention to her breasts."
                        jump KFB_Prep
                elif TempTrigger == "suck breasts":
                        "You shift your attention to her breasts."
                        jump KSB_Prep
                elif TempTrigger == "fondle pussy":
                        "You shift your attention to her pussy."
                        jump KFP_Prep
                elif TempTrigger == "lick pussy":
                        "You shift your attention to her pussy."
                        jump KLP_Prep
                elif TempTrigger == "fondle ass":
                        "You shift your attention to her ass."
                        jump KFA_Prep
                elif TempTrigger == "insert ass":
                        "You shift your attention to her ass."
                        jump KIA_Prep
                else: #If Trigger2 is "kiss you"
                        "You go back to kissing her deeply."
                        jump K_KissPrep                
            else: #if there's no Trigger2
                "You aren't doing anything else to shift to."     
            return
    # End "shift" situation    
        
    if Trigger:
        $ Situation = "auto"                 
        menu:  
            "Also kiss her." if Trigger in ("fondle breasts", "fondle pussy", "fondle thighs", "fondle ass", "insert ass", "sex", "anal", "hotdog", "dildo pussy", "dildo anal", "foot"):
                    "You lean in and start kissing her."
                    $ Trigger2 = "kiss you"
                    
            "Also fondle her breasts." if Trigger in ("fondle pussy", "fondle thighs", "fondle ass", "insert ass", "suck breasts", "lick pussy", "lick ass", "sex", "anal", "hotdog", "foot", "dildo pussy", "dildo anal", "foot"):
                    $ Trigger2 = "fondle breasts"
                    call K_Fondle_Breasts
                    
            "Also suck her breasts." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "fondle ass", "insert ass", "sex", "anal", "hotdog", "foot", "dildo pussy", "dildo anal", "foot"):
                    $ Trigger2 = "suck breasts"
                    call K_Suck_Breasts
                    
            "Also fondle her pussy." if Trigger in ("fondle breasts","fondle thighs", "fondle ass", "insert ass", "suck breasts", "lick pussy", "lick ass", "sex", "anal", "hotdog", "foot", "dildo pussy", "dildo anal", "foot"):
                    $ Trigger2 = "fondle pussy"
                    call K_Fondle_Pussy
                    
            "Also fondle her ass." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "insert ass", "suck breasts", "lick pussy", "lick ass", "sex", "anal", "hotdog", "dildo pussy", "dildo anal"):
                    $ Trigger2 = "fondle ass"
                    call K_Fondle_Ass
                    
            "Also finger her ass." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "fondle ass", "suck breasts", "lick pussy", "lick ass", "sex", "hotdog", "dildo pussy", "foot"):
                    $ Trigger2 = "insert ass"
                    call K_Insert_Ass
                    
            "Also jack it." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "fondle ass", "insert ass", "suck breasts", "lick pussy", "lick ass", "dildo pussy", "dildo anal"):
                    call K_Jackin
                    
            "Nevermind":
                pass
    else: #if a Trigger is not found. . .
        "There's some kind of bug here, let Oni know." 
        
    $ Situation = 0
    return

    
# end Kitty_Offhand function ////////////////////////////////////////////////////////////////////////


label Kitty_ShameIndex:   
    $ K_ShameLevel = 0
    
    if Trigger == "kiss you":
        $ K_ShameLevel += 2
        
    elif Trigger in ("fondle breasts", "fondle thighs", "fondle ass"):
        $ K_ShameLevel += 6
        
    elif Trigger in ("fondle pussy", "insert ass", "suck breasts", "hotdog"):
        $ K_ShameLevel += 10
        
    elif Trigger in ("lick pussy", "dildo pussy", "lick ass", "dildo anal", "hand", "blow", "titjob", "masturbation"):
        $ K_ShameLevel += 15
    
    elif Trigger in ("sex",  "anal"):
        $ K_ShameLevel += 20
    
    
    if not Trigger2:
        pass
    if Trigger2 == "kiss you":
        $ K_ShameLevel += 2
        
    elif Trigger2 in ("fondle breasts", "fondle thighs", "fondle ass"):
        $ K_ShameLevel += 6
        
    elif Trigger2 in ("fondle pussy", "insert ass", "suck breasts", "hotdog"):
        $ K_ShameLevel += 10
        
    elif Trigger2 in ("lick pussy", "dildo pussy", "lick ass", "dildo anal", "hand"):
        $ K_ShameLevel += 15    
        
        
    if not Trigger3:
        pass
    elif Trigger3 == "kiss you":
        $ K_ShameLevel += 2
    elif Trigger3 == "kiss girl":
        $ K_ShameLevel += 3
    elif Trigger3 == "kiss both":
        $ K_ShameLevel += 4
        
    elif Trigger3 in ("fondle breasts", "fondle thighs", "fondle ass"):
        $ K_ShameLevel += 6
        
    elif Trigger3 in ("fondle pussy"):
        $ K_ShameLevel += 10
        
    elif Trigger3 in ("dildo pussy", "dildo anal", "hand"):
        $ K_ShameLevel += 15
    
    
    $ K_ShameLevel += K_Shame #adds clothing based shame
    
    return
            
label Kitty_Taboo(Cnt= 1,Choice=0):   
    if "Kitty" not in P_DailyActions:
            $ P_DailyActions.append("Kitty") 
    if "scent" not in P_DailyActions:
            $ P_DailyActions.append("scent") 
            
    $ Cnt = Action_Check("Kitty", "recent", "spotted") if "spotted" in K_RecentActions else 1
    $ Cnt = 4 if Cnt > 4 else Cnt   
    
    $ D20 = renpy.random.randint(1, 20)  
        
    if D20 < 10:               
        #if you're at the point where the girls would notice you. . .  
        if Taboo > 20:
            if (Trigger == "kiss you" and not Trigger2 and not Trigger3):
                pass
            elif "Kitty" not in Rules:
                #if Xavier is looking. . .
                call KittyFace("surprised", 1)
                if Trigger == "blow" or Trigger == "hand" or Trigger == "titjob":
                    "Kitty stops what she's doing with a startled look."                
                else:
                    "You feel a slight buzzing in your head and stop what you're doing."
                ch_x "Cease that behavior at once! Come to my office immediately!" 
                call AllReset("Kitty")
                $ renpy.pop_call()        
                $ renpy.pop_call()
                call Girls_Caught("Kitty") #Kitty_Caught
                return
            else:
                #if you've disabled Xavier's looking
                ch_x "Hmmm. . ."
                call Statup("Kitty", "Inbt", 90, 2) 
                call Statup("Kitty", "Lust", 200, 3) 
                
        if bg_current == "bg classroom" and E_Loc == "bg teacher":
            #If you're in class and emma's there as a teacher. . .
            call Emma_Teacher_Caught("Kitty")
        call Girls_Noticed("Kitty")
            
    if Taboo <= 20:
            #This is a private space with others around.
            call Girls_Noticed("Kitty")
            return        
    elif Cnt < 4:        
            call KittyFace("surprised", 2)                                              
            #if this has happened less than 4 times within the current cycle of events
                  #if this has happened less than 4 times within the current cycle of events
            if "spotted" not in K_RecentActions:
                "Some of the other students notice you and Kitty."
                call Statup("Kitty", "Inbt", 200, 2)               
                $ K_Rep -= 2                         
                $ P_Rep -= 2             
            elif Cnt < 3:
                "A few more students notice you and Kitty."   
                call Statup("Kitty", "Inbt", 200, 2)               
                $ K_Rep -= 1                    
                $ P_Rep -= 1  
            elif Cnt == 3:
                "You've got quite an audience."               
                call Statup("Kitty", "Inbt", 200, 3)               
                $ K_Rep -= 1                    
                $ P_Rep -= 1  
                
            if "exhibitionist" in K_Traits:                
                    call KittyFace("sexy", 0)                     
                    if "spotted" not in K_RecentActions:
                        ch_k "I think we can give'em a show, [K_Petname]."                          
                    call Statup("Kitty", "Lust", 200, 5) 
                    $ Choice = "A"
            elif ApprovalCheck("Kitty", 750, "I", TabM=Cnt):            
                    #not an exhibitionist but very uninhibited       
                    call KittyFace("sexy", 1)                    
                    $ K_Brows = "sad"                           
                    if "spotted" not in K_RecentActions:                        
                        ch_k "What should we do?" 
                    call Statup("Kitty", "Lust", 200, 4)   
                    $ Choice = "B"
            elif ApprovalCheck("Kitty", 1000, "OI", TabM=Cnt):     
                    #not an exhibitionist but obedient/uninhibited          
                    call KittyFace("surprised", 2)
                    "Kitty looks a bit panicked."
                    call Statup("Kitty", "Lust", 200, 4)
                    $ Choice = "C"
            else:  
                    # She fails her inhibition checks
                    call KittyFace("surprised", 2)
                    if "spotted" not in K_RecentActions:    
                        "Kitty bolts up with an embarassed look. She grabs her clothes and flings herself through the nearest wall."  
                        $ K_Rep -= 3 if K_Rep >= 30 else K_Rep            
                    else:
                        "With a sudden embarrassed start, Kitty panics. She dives through the nearest wall."
                        call Statup("Kitty", "Love", 90, -15) 
                    "You head back to your room."                    
                    $ Choice = "stop"
                
            if Choice != "stop":
                menu:
                    "What would you like to do?"
                    "Let them watch. . ." if "spotted" not in K_RecentActions:   
                        if Choice == "A":                
                                call KittyFace("sexy", 0) 
                                ch_k "I'll bring my \"A\" game."             
                        elif Choice == "B":            
                                #not an exhibitionist but very uninhibited       
                                call KittyFace("sexy", 1)
                                $ K_Brows = "sad"               
                                ch_k "Hehe, um, yeah."    
                        elif Choice == "C":     
                                call KittyFace("sexy",2)
                                if K_Obed > K_Inbt:
                                    $ K_Eyes = "side"
                                    ch_k "If you insist, [K_Petname]."
                                else:          
                                    $ K_Mouth = "smile"
                                    $ K_Brows = "sad"
                                    ch_k "Yeah[K_like]sure. . ."                        
                                call Statup("Kitty", "Obed", 200, 5)                       
                        "You get back to it." 
                        $ K_Blush = 1
                    "Continue" if "spotted" in K_RecentActions:
                        if Choice == "C":          
                            call Statup("Kitty", "Obed", 200, 5) 
                    "Ok, let's stop.":   
                        if Choice == "A":                            
                                call KittyFace("sad")
                                ch_k "Booo."                                         
                        elif Choice == "B":            
                                call KittyFace("sad")
                                ch_k "Um, yeah." 
                        elif Choice == "C":     
                                call Statup("Kitty", "Love", 90, 10)          
                                call KittyFace("smile")
                                ch_k "Heh, thanks [K_Petname]." 
                        "You both run back to your rooms."
                        $ Choice = "stop"
                        
            if Choice == "stop":            
                    $ K_RecentActions.append("caught")
                    $ K_DailyActions.append("caught")     
                    show blackscreen onlayer black 
                    call AllReset("Kitty")
                    hide Kitty_Sprite with easeoutright  
                    call Remove_Girl("Kitty")
                    call KittyOutfit
                    hide blackscreen onlayer black 
                    $ renpy.pop_call()          
                    $ renpy.pop_call()       
                    $ renpy.pop_call()                    
                    jump Player_Room             
    elif "exhibitionist" not in K_Traits:     
        call KittyFace("sly")   
        $ K_Traits.append("exhibitionist") 
        "Kitty seems to have become something of an exhibitionist."
    elif D20 > 15:
        call KittyFace("sexy")
        "The crowd cheers."
        
    $ K_RecentActions.append("spotted") if Cnt < 4 else K_RecentActions
    $ K_DailyActions.append("spotted")  if "spotted" not in K_DailyActions else K_DailyActions
    return
    
    
label Kitty_Noticed(Other = "Rogue", Silent=0, B = 0):
    if "threesome" in K_RecentActions:
            return
    if Partner == "Kitty" and "noticed " + Other in K_RecentActions:
            return                
    
    if not Silent and Partner != "Kitty":
            call KittyFace("surprised", 1)           
            "Kitty noticed what you and [Other] are up to."
    
    if "cockout" in P_RecentActions:
                call Kitty_First_Peen            
    $ K_RecentActions.append("noticed " + Other)
    if "poly " + Other in K_Traits or (Other in P_Harem and "Kitty" in P_Harem):
            #if they already have a relationship. . .
            $ B = (1000-(20*Taboo))  
    else:             
            #if they don't have a relationship. . .
            if Other == "Rogue":    
                    $ B = (K_LikeRogue - 500)  
            elif Other == "Laura":    
                    $ B = (K_LikeLaura - 500)  
            elif Other == "Emma":    
                    $ B = (K_LikeEmma - 500)  
            if "dating" in K_Traits or "Kitty" in P_Harem:
                    #if they already have a relationship. . .
                    $ B -= 200
                    
    $ K_SpriteLoc = StageFarRight  
    call Display_Kitty(0,0) 
    $ Partner = "Kitty"
    $ Line = 0
    if ApprovalCheck("Kitty", 2000, TabM=2, Bonus = B) or ApprovalCheck("Kitty", 950, "L", TabM=2, Bonus = (B/3)): 
            #if she's very loose or really likes you
            call KittyFace("sexy", 1)
            if not Silent:
                    "She decides to join you."                                      
            call Statup("Kitty", "Obed", 90, 5)
            call Statup("Kitty", "Inbt", 90, 5) 
            call Statup("Kitty", "Lust", 90, 3) 
            if "poly " + Other not in K_Traits: 
                    $ K_Traits.append("poly " + Other) 
            call Kitty_Threeway_Set(Mode="start",ActiveGirl=Other) 
    elif ApprovalCheck("Kitty", 650, "O", TabM=2) and ApprovalCheck("Kitty", 450, "L", TabM=1) or ApprovalCheck("Kitty", 800, "O", TabM=2, Bonus = (B/3)): 
            #if she likes you, but is very obedient
            call KittyFace("sexy")
            if not Silent:
                    "She sits down patiently off to the side and watches."          
            call Statup("Kitty", "Love", 90, 5) 
            call Statup("Kitty", "Inbt", 90, 5)  
            call Statup("Kitty", "Lust", 90, 2)  
            if "poly " + Other not in K_Traits: 
                    $ K_Traits.append("poly " + Other) 
            call Kitty_Threeway_Set("watch",Mode="start",ActiveGirl=Other) 
    elif ApprovalCheck("Kitty", 650, "I", TabM=2) and ApprovalCheck("Kitty", 450, "L", TabM=1) or ApprovalCheck("Kitty", 800, "I", TabM=2, Bonus = (B/3)):
            #if she likes you, but is very uninhibited
            call KittyFace("sexy")
            if not Silent:
                    "She sits down and watches you with a hungry look."             
            call Statup("Kitty", "Love", 90, 5) 
            call Statup("Kitty", "Obed", 90, 2)
            call Statup("Kitty", "Inbt", 90, 2)     
            call Statup("Kitty", "Lust", 90, 5) 
            if "poly " + Other not in K_Traits: 
                    $ K_Traits.append("poly " + Other) 
            call Kitty_Threeway_Set("watch",Mode="start",ActiveGirl=Other) 
    elif ApprovalCheck("Kitty", 1500, TabM=2, Bonus = B):
            call KittyFace("perplexed", 1)
            if not Silent:
                    "She looks a little confused at what's happening, but she stays put and watches."
            if K_Love >= K_Obed and K_Love >= K_Inbt:
                call Statup("Kitty", "Obed", 90, 2)
                call Statup("Kitty", "Inbt", 90, 2)                     
            elif K_Obed >= K_Inbt:
                call Statup("Kitty", "Love", 90, 2) 
                call Statup("Kitty", "Inbt", 90, 2)   
            else:
                call Statup("Kitty", "Love", 90, 2) 
                call Statup("Kitty", "Obed", 90, 1)
                call Statup("Kitty", "Inbt", 90, 1) 
            call Statup("Kitty", "Lust", 90, 5)
            call Kitty_Threeway_Set("watch",Mode="start",ActiveGirl=Other) 
    elif ApprovalCheck("Kitty", 650, "L", TabM=1) or ApprovalCheck("Kitty", 400, "O", TabM=2):
            #if she likes you or is obedient, but not enough
            call KittyFace("angry", 2)                
            if bg_current == "bg kitty": 
                    "She looks betrayed, and kicks you both out of the room."
            else:
                    "She looks betrayed, and storms out of the room."                   
            call Statup("Kitty", "Love", 200, -5) 
            call Statup("Kitty", "Love", 80, -5) 
            call Statup("Kitty", "Love", 70, -5) 
            call Statup("Kitty", "Obed", 90, -5)
            call Statup("Kitty", "Lust", 89, 10) 
            if "saw with " + Other not in K_Traits: 
                    $ K_Traits.append("saw with " + Other) 
            $ Partner = 0
            if bg_current == "bg kitty": #Kicks you out if in Kitty's room
                    $ K_RecentActions.append("angry")
                    call GirlsAngry
            call Remove_Girl("Kitty")
    else:
            #if she doesn't like you much
            call KittyFace("surprised", 2)
            call Statup("Kitty", "Inbt", 90, 2) 
            call Statup("Kitty", "Lust", 40, 20)
            if Trigger != "kiss you":
                    call Statup("Kitty", "Love", 90, -10) 
                    call Statup("Kitty", "Obed", 90, -5)
                    call Statup("Kitty", "Lust", 80, 10)
            if bg_current == "bg kitty":
                    call Statup("Kitty", "Love", 90, -5) 
                    call Statup("Kitty", "Obed", 90, -5)
                    "She looks embarrassed, and shoves you both out of the room."                 
            elif Trigger != "kiss you":
                    "She looks embarrassed, and bolts from the room." 
            else:
                    "She looks a bit disgusted and walks away."                                  
            $ Partner = 0       
            if bg_current == "bg kitty": #Kicks you out if in Kitty's room
                    $ K_RecentActions.append("angry")
                    call GirlsAngry
            call Remove_Girl("Kitty")
    if Line:
        # This plays a line from a threesome action, if there is one. 
        "[Line]."          
        $ Line = 0
    return
    