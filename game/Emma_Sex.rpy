﻿# Emma_SexMenu //////////////////////////////////////////////////////////////////////
label Emma_SexAct(Act = 0):    
    call Shift_Focus("Emma")      
    if Taboo > 20 and "taboo" not in E_History:
            # If she's yet to agree to taboo stuff
            call Emma_Taboo_Talk
            if bg_current == "bg classroom":
                    ch_p "We could just lock the door, right?"
                    ch_e "We certainly could. . ."                
                    "[EmmaName] walks to the door and locks it behind her."
                    $ Taboo = 0
            else:
                    return      
                    
    if Act == "SkipTo":
        $ renpy.pop_call() #causes it to skip past the Trigger Swap
        $ renpy.pop_call() #causes it to skip past the cycle you were in before
        $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
        call SkipTo("Emma")
    elif Act == "switch":
        $ renpy.pop_call() #causes it to skip past call here from Sex_Menu_Threesome
        $ renpy.pop_call() #causes it to skip past call to Sex_Menu_Threesome
        # drops through to sex menu
    elif Act == "masturbate":         
        call EM_Prep
        if not Situation:
            return        
    elif Act == "lesbian":         
        call E_Les_Prep
        if not Situation:
            return   
    elif Act == "morningwood":
        # This action is called for by the label Emma_Morning and returns to there
        $ E_RecentActions.append("blow")           
        $ E_DailyActions.append("blow")                          
        $ E_DailyActions.append("morningwood")    
        call Sleepover_MorningWood
#        call Emma_MorningWood
        if Situation == "blow": 
            #If you selected to continue the BJ, then it calls the BJ actions
            $ Situation = 0
            call E_BJ_Prep
        $ Trigger4 = 0
        call Morning_Partner                                
        if not Situation:
            return
    elif Act == "kissing":        
        call E_KissPrep
        if not Situation:
            return   
    elif Act == "breasts":        
        call E_Fondle_Breasts
        if not Situation:
            return  
    elif Act == "blow":        
        call E_BJ_Prep
        if not Situation:
            return  
    elif Act == "hand":        
        call E_HJ_Prep
        if not Situation:
            return   
    elif Act == "sex":        
        call E_SexPrep
        if not Situation:
            return   

label Emma_SexMenu: 
    if "classcaught" not in E_History:
            ch_e "I can't imagine being a part of something so. . . tawdry." 
            return
    if "three" not in E_History:
            call CleartheRoom("Emma",Check=1)
            if _return >= 1:
                    # if there are other girls in the room. . .
                    call Emma_ThreeCheck
    if Taboo > 20 and "taboo" not in E_History:
            # If she's yet to agree to taboo stuff
            call Emma_Taboo_Talk
            if bg_current == "bg classroom":
                    ch_p "We could just lock the door, right?"
                    ch_e "We certainly could. . ."                
                    "[EmmaName] walks to the door and locks it behind her."
                    $ Taboo = 0
            else:
                    return          
    call Shift_Focus("Emma")
    $ Trigger = 0    
    $ Trigger2 = 0
    $ Trigger3 = 0
    $ Situation = 0
    call Emma_Hide    
    $ Emma_Arms = 1
    if "detention" in E_RecentActions:
        $ Tempmod = 20 if Tempmod <= 20 else Tempmod
    call Set_The_Scene(1,0,0,0,1)

    if not P_Semen:
        "You're a little out of juice at the moment, you might want to wait a bit." 
    if P_Focus >= 95:
        "You're practically buzzing, the slightest breeze could set you off."
    if not E_Action:
        "Emma's looking a bit tired out, maybe let her rest a bit."
    
    if "caught" in E_RecentActions or "angry" in E_RecentActions:  
        if E_Loc == bg_current:                
                ch_e "I'd rather not deal with you at the moment."
        call EmmaOutfit        
        call DrainWord("Emma","caught",1,0)
        return
        
    if Round < 5:
        ch_e "I think we could both do with a short break."   
        return
    menu Emma_SMenu:  
        ch_e "So, what was it you hoped to do?"
        "Do you want to make out?":
            if E_Action:
                call E_Makeout
            else:
                ch_e "I'm sorry, [E_Petname], but I need a break." 
        
        "Could I touch you?":
                if E_Action:
                    call EmmaFace("sly")                    
                    menu:
                        ch_e "Um, what did you want to touch, [E_Petname]?"                      
                        "Could I give you a massage?":
                                call E_Massage                        
                        "Your breasts?":
                                call E_Fondle_Breasts
                        "Your thighs?":
                                call E_Fondle_Thighs
                        "Your pussy?":
                                call E_Fondle_Pussy
                        "Your Ass?":
                                call E_Fondle_Ass
                        "Never mind [[something else]":
                                jump Emma_SMenu
                else:
                    ch_e "I'm sorry, [E_Petname], but I need a break."
                    
        "Could you take care of something for me? [[Your dick, you mean your dick]":        
                if P_Semen and E_Action:                
                    menu:
                        ch_e "What did you want me to do?"
                        "Could you give me a handjob?":
                            call E_Handjob
                        "Could you give me a titjob?":
                            call E_Titjob         
                        "Could you suck my cock?":
                            call E_Blowjob 
                        "Could use your feet?":
                            call E_Footjob 
                        "Never mind [[something else]":
                            jump Emma_SMenu
                elif not E_Action:
                        "I'm sorry, [E_Petname], but I need a break."
                else:
                        "You really don't have it in you, maybe take a break." 
#            ch_e "Not if you mean \"your dick\".[[Not available yet]"
                
        "Could you put on a show for me?":
                    menu:
                        ch_e "What did you want to see?"
                        "Dance for me?":
                                if E_Action:
                                    call Group_Strip("Emma")       
                                else:
                                    "I'm sorry, [E_Petname], but I need a break."
                                
                        "Could you undress for me?": 
                                    call E_Undress  
                                            
                        "You've got a little something. . . [[clean-up]" if E_Spunk:
                                    ch_e "Huh?"
                                    call Emma_Cleanup("ask")
                                    
                        "Could I watch you get yourself off? [[masturbate]":
                                if E_Action:
                                    call E_Masturbate           
                                else:
                                    "I'm sorry, [E_Petname], but I need a break."
                                                
                        "Maybe make out with Rogue?" if R_Loc == bg_current:
                                call E_LesScene
                        "Maybe make out with Kitty?" if K_Loc == bg_current:
                                call E_LesScene
                        "Maybe make out with Laura?" if L_Loc == bg_current:
                                call E_LesScene

                        "Never mind [[something else]":
                                jump Emma_SMenu
                          
                
        "Could we maybe?. . . [[fuck]":
                if P_Semen and E_Action:
                    menu:
                        "What did you want to do?"
                        "Come over here, I've got something in mind. . .":
                                call E_Sex_H           
                        "Fuck your pussy.":                        
                                call E_Sex_P           
                        "Fuck your ass.":                        
                                call E_Sex_A    
#MOD MARKER doggy position menu choices
                        "Turn around, I've got something in mind. . . \[DoggyStyle\]":
                                if P_Semen:
                                    call E_Doggy_H   
                                else:
                                    "The spirit is apparently willing, but the flesh is spongy and bruised."
                        "Fuck your pussy. \[DoggyStyle\]":    
                                if P_Semen:                    
                                    call E_Doggy_P  
                                else:
                                    "The spirit is apparently willing, but the flesh is spongy and bruised."          
                        "Fuck your ass. \[DoggyStyle\]":     
                                if P_Semen:                   
                                    call E_Doggy_A    
                                else:
                                    "The spirit is apparently willing, but the flesh is spongy and bruised."

#MOD MARKER missionary position menu choices
                        "Lean back, I've got something in mind. . . \[Missionary\]":
                                    if P_Semen:
                                        call E_Missionary_H
                                    else:
                                        "The spirit is apparently willing, but the flesh is spongy and bruised."
                        "Fuck your pussy. \[Missionary\].":
                                    if P_Semen:
                                        call E_Missionary_P
                                    else:
                                        "The spirit is apparently willing, but the flesh is spongy and bruised."         
                        "Fuck your ass. \[Missionary\]":
                                    if P_Semen:
                                        call E_Missionary_A
                        "How about some toys? [[Pussy]":                        
                            call E_Dildo_Pussy     
                        "How about some toys? [[Anal]":                        
                            call E_Dildo_Ass   
                        "Never mind [[something else]":
                                jump Emma_SMenu
                elif not E_Action:
                        "I'm sorry, [E_Petname], but I need a break."
                else:
                        "The spirit is apparently willing, but the flesh is spongy and bruised." 
                        
        "Hey, do you want in on this? [[Threesome]":
                    call Sex_Menu_Threesome("Emma")
                    jump Emma_SMenu
                                
        "Cheat Menu" if config.developer:                                                   #Remove
            call Emma_Cheat_Menu
        "Never mind. [[exit]":         
                if E_Lust >= 50 or E_Addict >= 50:
                        call EmmaFace("sad")
                        if E_Action and E_SEXP >= 15 and Round > 20:
                                if "round2" not in E_RecentActions:  
                                    ch_e "Are you certain, [E_Petname]? Are you perhaps forgetting something?"                
                                    call Statup("Emma", "Inbt", 30, 2)
                                    call Statup("Emma", "Inbt", 50, 1)
                                elif E_Addict >= 50:                        
                                    ch_e "I need more contact." 
                                else:
                                    ch_e "I'm afraid that still wasn't enough."                          
                                menu:
                                    extend ""
                                    "Yeah, I'm done for now." if P_Semen and "round2" not in E_RecentActions:                 
                                        if "unsatisfied" in E_RecentActions and not E_OCount:                                
                                            call EmmaFace("angry")
                                            $ E_Eyes = "side" 
                                            call Statup("Emma", "Love", 70, -2)
                                            call Statup("Emma", "Love", 90, -4)
                                            call Statup("Emma", "Obed", 30, 2)
                                            call Statup("Emma", "Obed", 70, 1)
                                            ch_e "Well! This might count against you next time."
                                        else:                               
                                            call EmmaFace("bemused", 1)
                                            call Statup("Emma", "Obed", 50, 2)   
                                            ch_e "I suppose I'll have to blame myself as an educator."  
                                    "I gave it a shot." if "round2" in E_RecentActions:                 
                                        if "unsatisfied" in E_RecentActions and not E_OCount:                                
                                            call EmmaFace("angry")
                                            $ E_Eyes = "side"                                 
                                            ch_e "Yes, disappointingly so. . ."
                                        else:                               
                                            call EmmaFace("bemused", 1) 
                                            ch_e "I suppose you did. . .shame you couldn't do better. . ."  
                                    "Hey, I did my part." if E_OCount > 2:      
                                        call EmmaFace("sly", 1) 
                                        ch_e "Take it as a compliment that I expected more."  
                                    "I'm tapped out for the moment, let's try again later." if not P_Semen:
                                        call EmmaFace("normal")                        
                                        ch_e "I suppose that can't be helped. . ."
                                    "Ok, we can try something else." if MultiAction and "round2" not in E_RecentActions:
                                        call EmmaFace("smile")
                                        call Statup("Emma", "Love", 70, 2)
                                        call Statup("Emma", "Love", 90, 1) 
                                        ch_e "Excellent. . ."                            
                                        $ E_RecentActions.append("round2")                      
                                        $ E_DailyActions.append("round2") 
                                        jump Emma_SexMenu
                                    "Again? Ok, fine." if MultiAction and "round2" in E_RecentActions:
                                        call EmmaFace("sly")
                                        ch_e "Always. . ."           
                                        jump Emma_SexMenu  
                                #End "if Emma is still up for more"
                        else:  
                                call EmmaFace("bemused", 1)
                                ch_e "I suppose I'm tired as well, [E_Petname]. We can take a breather. . ."  
                                call Statup("Emma", "Inbt", 30, 2)
                                call Statup("Emma", "Inbt", 50, 1)    
                        call EmmaFace
                else:
                    ch_e "Fine."
                    
                call Sex_Over  
#                $ E_OCount = 0    
#                call Emma_Cleanup
#                call EmmaOutfit
                return
    if E_Loc != bg_current:
        call Set_The_Scene
        $ Trigger = 0    
        $ Trigger2 = 0
        $ Trigger3 = 0
        $ Trigger4 = 0
        $ Trigger5 = 0
        return
    if not MultiAction:    
        call Set_The_Scene
        ch_e "That's all you get. . . for now."
        $ E_OCount = 0
        $ Trigger = 0    
        $ Trigger2 = 0
        $ Trigger3 = 0
        $ Trigger4 = 0
        $ Trigger5 = 0
        return
    call GirlsAngry
    jump Emma_SexMenu
# end Emma_SexMenu //////////////////////////////////////////////////////////////////////            

label Emma_Cheat_Menu:
    menu:
        "Level-Up":
            $ E_Hand += 5
            $ E_Blow += 5
            $ E_Swallow += 5
            $ E_Hand += 5
            $ E_Slap += 5
            $ E_Tit += 5
            $ E_Sex += 5
            $ E_Anal += 5
            $ E_Hotdog += 5
            $ E_Mast += 5
            $ E_Org += 5
            $ E_FondleB += 5
            $ E_FondleT += 5
            $ E_FondleP += 5
            $ E_FondleA += 5
            $ E_DildoP += 5
            $ E_DildoA += 5
            $ E_Plug += 5
            $ E_SuckB += 5
            $ E_InsertP += 5
            $ E_InsertA += 5
            $ E_LickP += 5    
            $ E_LickA += 5
            $ E_Blow += 5
            $ E_Swallow += 5
            $ E_CreamP += 5
            $ E_CreamA += 5
            $ E_SeenChest = 1
            $ E_SeenPanties = 1
            $ E_SeenPussy = 1
            "Hand [E_Hand], Blow [E_Blow], Swallow [E_Swallow]"
        "Level Reset":
            $ E_Hand = 0
            $ E_Blow = 0
            $ E_Swallow = 0
            "Hand [E_Hand], Blow [E_Blow], Swallow [E_Swallow]"
        "Toggle Taboo":
            if not Taboo:
                $ Taboo = 40
            else:
                $ Taboo = 0
        "Maxed":
                $ E_Love = 1000
                $ E_Inbt = 1000
                $ E_Obed = 1000
                $ E_Lust = 50
                $ E_Addict = 0 #how addicted she is
                $ E_Addictionrate = 0 #How faster her addiciton rises
                $ E_Kissed = 1 #How many times they've kissed
                $ E_Swallow = 0
        "50\%":
                $ E_Love = 500
                $ E_Inbt = 500
                $ E_Obed = 500
                $ E_Lust = 65
                $ E_Addict = 0 #how addicted she is
                $ E_Addictionrate = 10 #How faster her addiciton rises
                $ E_Kissed = 10 #How many times they've kissed
                $ E_Swallow = 0
        "25\%":
                $ E_Love = 250
                $ E_Inbt = 250
                $ E_Obed = 250
                $ E_Lust = 85
                $ E_Addict = 10 #how addicted she is
                $ E_Addictionrate = 50 #How faster her addiciton rises
                $ E_Kissed = 10 #How many times they've kissed
                $ E_Swallow = 0
        "Juice up":
            $ P_Semen += 5
            $ E_Action = 10
        "Cold Shower":
            $ P_Focus = 0
        "Exit":
            return
    jump Emma_Cheat_Menu
    return
    
    
    
label E_Jackin(Cnt = 0, TempVar = 0):
    if "unseen" in E_RecentActions:        
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
                    call Seen_First_Peen("Emma",Partner)
            
            $ Trigger2 = "jackin"
            if "jackin" in E_RecentActions:
                return            
            $ E_RecentActions.append("jackin")
            $ E_DailyActions.append("jackin") 
            
            if E_SEXP < 10 and "classcaught" not in E_History:
                    call EmmaFace("surprised", 1) 
                    $ E_Eyes = "down"
                    "Wait,"
                    call EmmaFace("angry", 1)                     
                    ch_e "That really isn't appropriate."  
                    call Statup("Emma", "Lust", 50, 7) 
                    if not ApprovalCheck("Emma", 1200, TabM = 3):
                            $ E_RecentActions.append("angry")
                            $ E_DailyActions.append("angry")  
                            $ renpy.pop_call()
                            return
            elif E_SEXP <= 15:            
                    call EmmaFace("surprised", 1) 
                    $ E_Eyes = "down"
                    "Emma looks down at your cock with some surprise."
                    call EmmaFace("perplexed", 0) 
                    call Statup("Emma", "Lust", 60, 10)
            elif ApprovalCheck("Emma", 1200, TabM = 3):
                    call EmmaFace("surprised", 1) 
                    $ E_Eyes = "down"
                    "Emma looks down at your cock and smiles."            
                    call EmmaFace("sly", 0) 
                    call Statup("Emma", "Lust", 70, 12)
            elif ApprovalCheck("Emma", 500, "I", TabM=2):
                    call EmmaFace("surprised", 1) 
                    $ E_Eyes = "down"
                    "Emma glances at it, but just smiles in amusement."        
                    call EmmaFace("sly", 0) 
                    call Statup("Emma", "Lust", 70, 15)
            else:
                    call EmmaFace("angry", 1) 
                    $ E_Eyes = "down"
                    "Emma glances down at your cock with a scowl."    
                    call EmmaFace("angry", 0)
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")  
                    return
            
            if E_Action and E_Loc == bg_current:
                $ Options = ["none"]
                
                if E_Hand >= 5 and ApprovalCheck("Emma", 1200, TabM = 3):
                        $ Cnt = E_Hand - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        while Cnt:
                            $ Options.append("hand") 
                            $ Cnt -= 1
                if E_Blow >= 5 and ApprovalCheck("Emma", 1400, TabM = 3):
                        $ Cnt = E_Blow - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        $ Cnt += 5 if "hungry" in E_Traits else 0
                        while Cnt:
                            $ Options.append("blow") 
                            $ Cnt -= 1
                if E_Tit >= 5 and ApprovalCheck("Emma", 1300, TabM = 5):
                        $ Cnt = E_Tit - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        while Cnt:
                            $ Options.append("Tit") 
                            $ Cnt -= 1
                if E_Sex >= 5 and ApprovalCheck("Emma", 1500, TabM = 5):
                        $ Cnt = E_Sex - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        $ Cnt += 5 if E_Lust >= 70 else 0
                        while Cnt:
                            $ Options.append("sex") 
                            $ Cnt -= 1
                if E_Anal >= 5 and ApprovalCheck("Emma", 1700, TabM = 5):
                        $ Cnt = E_Anal - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        $ Cnt += 5 if E_Lust >= 70 and E_Loose else 0
                        while Cnt:
                            $ Options.append("anal") 
                            $ Cnt -= 1
                    
                $ renpy.random.shuffle(Options) 
                                
                $ TempVar = Options[0]  
                $ del Options[:]  
                
                if TempVar == "hand":
                        ch_e "Would you like a hand with that?"
                elif TempVar == "blow":
                        ch_e "I wouldn't mind a taste of that. . ."
                elif TempVar == "tit":
                        ch_e "If you like, I could use my chest. . ."
                elif TempVar == "sex":
                        ch_e "I'm positively dripping here. . ."
                elif TempVar == "anal":
                        ch_e "I wouldn't mind you using the back door. . ."
                else:
                        ch_e "Mmmmm. . ."
                        return
                    
                menu:
                    extend ""
                    "No thanks, I've got this in hand.":
                        call EmmaFace("perplexed", 1)  
                        ch_e "Oh. . ."      
                        ch_e "Carry on then, [E_Petname]."
                        call EmmaFace("sly", 0, Eyes="down") 
                        return
                    "Hmm, sounds like a plan.": 
                        $ Situation = "shift"
                
                $ Trigger2 = 0
                    
                #Close out what you were doing 
                if Trigger == "strip":
                        call Group_Strip_End
                elif Trigger == "masturbation":
                        $ E_Action -= 1
                        $ E_Mast += 1    
                        call Checkout
                else:
                        call CloseOut("Emma")
                                
                show blackscreen onlayer black
                hide blackscreen onlayer black
                if TempVar == "hand":                
                        jump E_HJ_Prep
                elif TempVar == "blow":
                        jump E_BJ_Prep
                elif TempVar == "tit":
                        jump E_TJ_Prep
                elif TempVar == "sex":
                        jump E_SexPrep
                elif TempVar == "anal":
                        jump E_AnalPrep
    return
# End Emma "jackin it" action / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
 
label E_TouchCheek:  
    call Shift_Focus("Emma")
    call EmmaFace("surprised", 1) 
    if "no cheek" in E_DailyActions:
            "You reach out to brush Emma's face with your hand, but she slaps it away."
            call EmmaFace("angry")
            ch_e "What are you doing, [E_Petname]?"
            call Statup("Emma", "Love", 50, -2)
            return
    else:
            "You reach out and brush Emma's face with your hand."
    call Statup("Emma", "Obed", 50, 1)    
    if "addict emma" in P_Traits:
        $ E_Addict -= 2            
        $ E_Addictionrate += 1 if E_Addictionrate < 5 else E_Addictionrate 
        $ E_Addictionrate = 3 if E_Addictionrate < 3 else E_Addictionrate 
        call Statup("Emma", "Lust", 70, 5)
    else:
        call Statup("Emma", "Lust", 40, 5)
        
    if ApprovalCheck("Emma", 1000):
        call EmmaFace("sexy", 1)
        ch_e "That's sweet, what was it for, [E_Petname]?"
        call Statup("Emma", "Love", 80, 1)
    elif ApprovalCheck("Emma", 800) or ApprovalCheck("Emma", 700, "L"):
        call EmmaFace("smile", 1)
        ch_e "Mmmmm. . ."      
    elif "cheek" in E_DailyActions:        
        call EmmaFace("angry", 1)
        ch_e "I won't warn you again, [E_Petname]."
        call Statup("Emma", "Love", 50, -2)
        $ E_DailyActions.append("no cheek")
    elif ApprovalCheck("Emma", 400):
        $ E_Mouth = "smile"
        $ E_Brows = "normal"
        ch_e "Hmm, maybe we need to discuss \"boundaries.\""
    else:
        call EmmaFace("angry", 1)
        ch_e "That's inappropriate behavior, [E_Petname]."   
        call Statup("Emma", "Love", 50, -3)
        call Statup("Emma", "Obed", 50, 1)
        call Statup("Emma", "Inbt", 30, 1)
    
    if "no cheek" in E_DailyActions: 
        menu:
            "Sorry, sorry, won't happen again.":
                if ApprovalCheck("Emma", 300):
                    call EmmaFace("sexy", 1)
                    ch_e "See that it doesn't."
                    call Statup("Emma", "Love", 80, 2)
                else:
                    call EmmaFace("angry", 1)
                    $ E_Eyes = "side"
                    ch_e "I'm sure."                 
                    call Statup("Emma", "Obed", 20, 1)   
                    
            "You know you wanted it.":
                if ApprovalCheck("Emma", 400, "OI") or ApprovalCheck("Emma", 800):
                    call EmmaFace("normal", 1)
                    $ E_Eyes = "squint"
                    ch_e "Don't presume. . . so much."
                    call Statup("Emma", "Love", 60, -1) 
                    call Statup("Emma", "Obed", 30, 2)                        
                    call Statup("Emma", "Inbt", 40, 2)
                else:
                    call EmmaFace("angry", 2)
                    $ E_Eyes = "squint"
                    ch_e "You {i}must{/i} be daydreaming."  
                    $ E_Blush = 1
                    call Statup("Emma", "Love", 60, -3) 
                    call Statup("Emma", "Obed", 30, 3)                        
                    call Statup("Emma", "Inbt", 40, 2) 
    else:
        menu:
            "Sorry, you looked so lovely.":
                if ApprovalCheck("Emma", 850, "LI"):
                    call EmmaFace("sexy", 1)
                    ch_e "Don't make promises you can't keep."
                    call Statup("Emma", "Love", 80, 2)
                elif ApprovalCheck("Emma", 500, "LI"):
                    call EmmaFace("smile", 1)
                    ch_e "You don't look so bad yourself, [E_Petname]."
                    call Statup("Emma", "Love", 80, 2)
                else:
                    call EmmaFace("angry", 1)
                    $ E_Eyes = "side"
                    ch_e "Obviously."                 
                    call Statup("Emma", "Obed", 20, 1)   
                    
            "You had a fly on you.":
                if ApprovalCheck("Emma", 700, "LI"):
                    call EmmaFace("sexy", 1)
                    ch_e "Oh? I'm {i}sure{/i} that was it. . ."
                    call Statup("Emma", "Love", 60, 1)                        
                    call Statup("Emma", "Inbt", 40, 1)
                elif ApprovalCheck("Emma", 700):
                    call EmmaFace("normal")
                    ch_e "A fly, right. . ."
                else:
                    call EmmaFace("angry", 1)
                    ch_e "That's no excuse." 
                    call Statup("Emma", "Obed", 50, 2)    
                    
            "Are you sure you didn't enjoy that?":
                if ApprovalCheck("Emma", 850):
                    call EmmaFace("sexy", 1)
                    $ E_Eyes = "side"
                    ch_e "I'd need to try again to be sure. . ."
                    call Statup("Emma", "Obed", 50, 2)  
                    call Statup("Emma", "Obed", 30, 1)                        
                    call Statup("Emma", "Inbt", 40, 1)
                elif ApprovalCheck("Emma", 500, "OI"):
                    call EmmaFace("normal", 1)
                    ch_e "Don't push it. . . too far."
                    call Statup("Emma", "Love", 60, -1)
                    call Statup("Emma", "Obed", 50, 2)  
                    call Statup("Emma", "Obed", 30, 2)                        
                    call Statup("Emma", "Inbt", 40, 2)
                else:
                    call EmmaFace("angry", 1)
                    $ E_Eyes = "side"
                    ch_e "Certain."   
                    call Statup("Emma", "Love", 60, -3)
                    call Statup("Emma", "Obed", 50, 2)  
                    call Statup("Emma", "Obed", 30, 3)                        
                    call Statup("Emma", "Inbt", 40, 2)   
            
    $ E_RecentActions.append("cheek")
    $ E_DailyActions.append("cheek")
    return
# End Emma "touch cheek" action / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 

label E_Headpat:  
    call Shift_Focus("Emma")
    call EmmaFace("surprised", 1)
    if "no headpat" in E_DailyActions:
        "You reach out to pat Emma on the head, but she glares at you hard enough that you freeze."
        call EmmaFace("angry")
        ch_e "What have we said about this \"head pats\" obsession?"
        call Statup("Emma", "Love", 50, -2)
        return
    else:
        "You reach out and pat Emma on the head."
    call Statup("Emma", "Obed", 50, 2)    
       
    if ApprovalCheck("Emma", 1200):
        call EmmaFace("sexy", 1)
        ch_e "Hmmmm?"
        call Statup("Emma", "Love", 85, 1)
    elif ApprovalCheck("Emma", 1100) or ApprovalCheck("Emma", 850, "L"):
        call EmmaFace("smile", 1)
        ch_e "Mmmmmm. . ."      
    elif "headpat" in E_DailyActions:        
        call EmmaFace("angry", 1)
        ch_e "Do I look like a child or pet to you?"
        call Statup("Emma", "Love", 50, -2)
        $ E_DailyActions.append("no headpat")
    elif ApprovalCheck("Emma", 800):
        $ E_Mouth = "smile"
        $ E_Brows = "normal"
        ch_e "Hmph. You have some odd interests."
    else:
        call EmmaFace("angry", 1)
        "She grabs your wrist and pulls it away from her hair."
        ch_e "I will warn you once. Stop that."  
        call Statup("Emma", "Love", 50, -3)
        call Statup("Emma", "Obed", 50, 1)
        call Statup("Emma", "Inbt", 30, 1)
   
    if "no headpat" in E_DailyActions:
        menu:
            "Sorry, sorry, won't happen again.":
                if ApprovalCheck("Emma", 300):
                    call EmmaFace("sexy", 1)
                    ch_e "I should hope not."
                    call Statup("Emma", "Love", 80, 2)
                else:
                    call EmmaFace("angry", 1)
                    $ E_Eyes = "side"
                    "Emma silently glares at you."                
                    call Statup("Emma", "Obed", 20, 1)  

            "You know you wanted it.":
                if ApprovalCheck("Emma", 600, "OI") or ApprovalCheck("Emma", 900):
                    call EmmaFace("normal", 1)
                    $ E_Eyes = "squint"
                    ch_e "Hmph. . ."
                    call Statup("Emma", "Love", 60, -1)
                    call Statup("Emma", "Obed", 30, 2)                        
                    call Statup("Emma", "Inbt", 40, 2)
                else:
                    call EmmaFace("sexy", 2)
                    $ E_Eyes = "squint"
                    ch_e "What nonsense. . ."  
                    $ E_Blush = 1
                    call Statup("Emma", "Love", 60, -3)
                    call Statup("Emma", "Obed", 30, 3)                        
                    call Statup("Emma", "Inbt", 40, 2)
       
    else:
        menu:
            "Sorry, you looked so cute there.":
                if ApprovalCheck("Emma", 1050, "LI"):
                    call EmmaFace("sexy", 1)
                    "She hesitates, but then slowly closes her eyes."
                    ch_e "Be grateful. I wouldn't let just anyone do this."
                    call Statup("Emma", "Love", 80, 2)  
                    $ Count = 5
                elif ApprovalCheck("Emma", 700, "LI"):
                    call EmmaFace("smile", 1)
                    ch_e "Just cute? I must be slipping."
                    call Statup("Emma", "Love", 80, 2)
                    $ Count = 4
                else:
                    call EmmaFace("angry", 1)
                    $ E_Eyes = "side"
                    ch_e "You'll have to do better than that, [E_PetName]. Much better."              
                    call Statup("Emma", "Obed", 20, 1)
                    $ Count = 1  
                   
            "You had a loose hair going on.":
                if ApprovalCheck("Emma", 850, "LI"):
                    call EmmaFace("sexy", 1)
                    ch_e "A loose hair, you say? Perhaps you can help get it back under control."
                    call Statup("Emma", "Love", 60, 1)                        
                    call Statup("Emma", "Inbt", 40, 1)
                    $ Count = 5
                elif ApprovalCheck("Emma", 700):
                    call EmmaFace("normal")
                    ch_e "A loose hair? Oh, [E_PetName]. I would hope you'd be more original than that."
                    $ Count = 3
                else:
                    call EmmaFace("angry", 1)
                    ch_e "I can handle something like that easily enough on my own."
                    call Statup("Emma", "Obed", 50, 2)  
                    $ Count = 1  
                   
            "Are you sure you didn't enjoy that?":
                if ApprovalCheck("Emma", 1000):
                    call EmmaFace("sexy", 1)
                    $ E_Eyes = "side"
                    ch_e "I'll admit that much, at least."
                    call Statup("Emma", "Obed", 50, 2)  
                    call Statup("Emma", "Obed", 30, 1)                        
                    call Statup("Emma", "Inbt", 40, 1)
                    $ Count = 4
                elif ApprovalCheck("Emma", 600, "OI"):
                    call EmmaFace("normal", 1)
                    ch_e "Ah. . . no, no. A lady must have some secrets."
                    call Statup("Emma", "Love", 60, -1)
                    call Statup("Emma", "Obed", 50, 2)  
                    call Statup("Emma", "Obed", 30, 2)                        
                    call Statup("Emma", "Inbt", 40, 2)
                    $ Count = 2
                else:
                    call EmmaFace("angry", 1)
                    $ E_Eyes = "side"
                    ch_e "If you'd tried that a few years ago..."  
                    call Statup("Emma", "Love", 60, -3)
                    call Statup("Emma", "Obed", 50, 2)  
                    call Statup("Emma", "Obed", 30, 3)                        
                    call Statup("Emma", "Inbt", 40, 2)
                    $ Count = 1
        while Count > 0 and Round >= 10:
            $ Count -= 1 if Count != 3 else 0
            $ Round -= 1
            menu:
                "Continue?"
                "Yes":
                    "You continue to hold your hand on top of Emma's head, rubbing it softly."                    
                    if not Count:
                        if ApprovalCheck("Emma", 800):
                            call EmmaFace("bemused", 2)
                            call Statup("Emma", "Love", 80, 2)                      
                            call Statup("Emma", "Inbt", 40, 2)
                            ch_e "I think. . . that will do."
                            "She steps back and out of your range."
                            call EmmaFace("bemused", 1)
                        else:
                            call EmmaFace("angry", 2)
                            call Statup("Emma", "Love", 60, -5)                      
                            call Statup("Emma", "Inbt", 40, 3)
                            ch_e "I think you've had your fun. . ."
                            "She knocks your hand away."
                            call EmmaFace("angry", 1)
                    elif Count == 1:
                        if ApprovalCheck("Emma", 900):
                            call EmmaFace("bemused", 1)
                            call Statup("Emma", "Love", 80, 1)
                            call Statup("Emma", "Obed", 50, 2)                        
                            call Statup("Emma", "Inbt", 40, 2)
                            if Taboo > 20:
                                    # Taboo ratings over 20 are considered public areas, over 0 means people might be around
                                    ch_e "We really shouldn't do this in public. . . I do have an image."
                            else:
                                    ch_e "Just be careful not to do that in public. . . I do have an image."
                        else:
                            call EmmaFace("angry", 2)
                            call Statup("Emma", "Love", 60, -2)
                            call Statup("Emma", "Obed", 60, 2)  
                            call Statup("Emma", "Obed", 30, 2)  
                            ch_e "Don't push your luck too far."
                    else:
                        if ApprovalCheck("Emma", 900):
                            call EmmaFace("bemused", 2,Eyes="closed")
                            if Count > 3:
                                call Statup("Emma", "Love", 90, 1)
                                call Statup("Emma", "Love", 70, 1)
                                call Statup("Emma", "Obed", 50, 1)
                                ch_e "Mmmmm. . . you really shouldn't. . ."
                                "She does seem to be leaning into it. . ."
                        else:
                            call EmmaFace("angry", 1)
                            call Statup("Emma", "Love", 60, -1)
                            call Statup("Emma", "Obed", 50, 2)  
                            call Statup("Emma", "Obed", 30, 2)                        
                            call Statup("Emma", "Inbt", 40, 2)
                            ch_e "Er. . ."
                            $ Count -= 1 if Count > 2 else 0
                "No":
                    $ Count = 0
    $ Count = 0                
    $ E_RecentActions.append("headpat")
    $ E_DailyActions.append("headpat")
    return
# Slap Ass

label E_Slap_Ass:
    call Shift_Focus("Emma")
    # fix add sound here?
    if renpy.showing("Emma_SexSprite"):
            show Emma_SexSprite #fix, test this
            with vpunch
    elif renpy.showing("Emma_Missionary"):
            show Emma_Missionary #fix, test this
            with vpunch
    elif renpy.showing("Emma_Doggy"):
            show Emma_Doggy #fix, test this
            with vpunch
    elif renpy.showing("Emma_BJ_Animation"):           #fix, make this animation work better when paused for this effect.
            show Emma_BJ_Animation
            with vpunch
    elif renpy.showing("Emma_TJ_Animation"):
            show Emma_TJ_Animation  
            with vpunch
    elif renpy.showing("Emma_HJ_Animation"):
            show Emma_HJ_Animation  
            with vpunch
    else:
            show Emma_Sprite
            with vpunch
    $ E_Slap += 1                               #add in slap-base obedience        
    if ApprovalCheck("Emma", 300, "O", TabM=1):   
        call EmmaFace("sexy", 1)  
        $ E_Mouth = "surprised"
        call Statup("Emma", "Lust", 51, 3, 1)
        if Action_Check("Emma", "recent", "slap") < 4:
            call Statup("Emma", "Lust", 200, 1)
            if E_Slap <= 5:
                    call Statup("Emma", "Obed", 50, 2)
            if E_Slap <= 10:
                    call Statup("Emma", "Obed", 80, 1)
        $ Line = "You slap her ass and she jumps with pleasure"
    else:                
        call EmmaFace("surprised", 1)        
        if Action_Check("Emma", "recent", "slap") < 4:
            call Statup("Emma", "Obed", 70, 2)        
            call Statup("Emma", "Love", 50, -1)
        $ Line = "You slap her ass and she looks back at you a bit startled"  
    
    if Taboo:    
        "[Line]."
        if not ApprovalCheck("Emma", 900, TabM=3) and "public" not in E_History:
            call EmmaFace("angry",1)
            if E_Slap <= 5:
                call Statup("Emma", "Obed", 80, 2)  
                call Statup("Emma", "Obed", 50, 2)      
            call Statup("Emma", "Love", 70, -2)    
            call Statup("Emma", "Love", 50, -1)
            $ Line = "She looks pretty mad though"  
        elif not ApprovalCheck("Emma", 1500, TabM=3) and "public" not in E_History:
            call EmmaFace("bemused",2)
            if E_Slap <= 5:
                    call Statup("Emma", "Obed", 80, 2)
            call Statup("Emma", "Love", 70, -1)
            $ Line = "She looks a bit embarrassed"  
            $ E_Blush = 1
        else:                         #Over 1500
            call EmmaFace("sexy")
            $ E_Mouth = "smile"
            if E_Slap <= 5:
                    call Statup("Emma", "Obed", 80, 1)
            $ Line = "She gives you a naughty grin" 
        
    if not Trigger:
        "[Line]."
        $ Line = 0
        
    $ E_RecentActions.append("slap") if Action_Check("Emma", "recent", "slap") < 4 else E_RecentActions
    $ E_DailyActions.append("slap") if Action_Check("Emma", "daily", "slap") < 10 else E_DailyActions
        
    return
    
# Tag end ////////////////////////////////////////////////////////////////////////


# E_Makeout //////////////////////////////////////////////////////////////////////
label E_Makeout:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Emma")
    
    $ Approval = ApprovalCheck("Emma", 700, TabM=1) # 50, 65, 80, Taboo -40(90)
    
    if Approval > 1 and not E_Kissed and not E_Forced:        
        call EmmaFace("sexy")
        $ E_Eyes = "side"
        ch_e "Well, I suppose it couldn't hurt. . ."
    elif Approval and not E_Kissed:        
        call EmmaFace("sexy")
        $ E_Eyes = "side"
        ch_e "We could. . ."   
    elif Approval and "kissing" in E_RecentActions:
            call EmmaFace("sexy", 1)
            ch_e "Mmmm. . ."
            jump E_KissPrep
    elif Approval and "kissing" in E_DailyActions:
        call EmmaFace("sexy", 1)
        $ Line = renpy.random.choice(["Mmmm. . .",       
            "Didn't get enough earlier?",
            "Come and get it."]) 
        ch_e "[Line]"            
    elif Approval > 1 and E_Love > E_Obed:       
        call EmmaFace("sexy")
        ch_e "Mwa."            
    elif ApprovalCheck("Emma", 500, "O") and E_Obed > E_Love:
        call EmmaFace("normal")
        ch_e "Of course."
        call Statup("Emma", "Obed", 60, 1)
    elif ApprovalCheck("Emma", 300, "O") and ApprovalCheck("Emma", 200, "L"):
        call EmmaFace("sexy")
        ch_e "Ok, fine."
        call Statup("Emma", "Obed", 50, 3)
    elif E_Addict >= 50:
        call EmmaFace("sexy")
        $E_Eyes = "manic"
        ch_e ". . . yes."    
    elif Approval:       
        call EmmaFace("bemused")
        ch_e "Very well." 
    else:        
        call EmmaFace("normal") # Else
        $ E_Mouth = "sad"
        ch_e "Hmmm, no."
        $ E_RecentActions.append("no kissing")                      
        $ E_DailyActions.append("no kissing") 
        return    
        
label E_KissPrep:    
    call Statup("Emma", "Inbt", 10, 1)
    call Statup("Emma", "Inbt", 20, 1)
    call E_Kissing_Launch("kiss you")
    if E_Kissed >= 10 and E_Inbt >= 300:
        call EmmaFace("sucking")
    elif E_Kissed > 1 and E_Addict >= 50:
        call EmmaFace("sucking")
    else:
        call EmmaFace("kiss")
    if Situation == "Emma":                                                      
            #Emma auto-starts   
            $ Situation = 0
            "Emma presses her chest against yours, and kisses you deeply."
            menu:
                "What do you do?"
                "Go with it.":                    
                    call Statup("Emma", "Inbt", 80, 3) 
                    call Statup("Emma", "Inbt", 50, 2)
                    "You lean in to the kiss."
                "Praise her.":       
                    call EmmaFace("sexy", 1)                    
                    call Statup("Emma", "Inbt", 80, 3) 
                    ch_p "Mmm, this is a nice surprise, [E_Pet]."
                    call Emma_Namecheck
                    "You lean in to the kiss."
                    call Statup("Emma", "Love", 85, 1)
                    call Statup("Emma", "Obed", 90, 1)
                    call Statup("Emma", "Obed", 50, 2)
                "Ask her to stop.":
                    "You pull back."
                    call EmmaFace("surprised")       
                    call Statup("Emma", "Inbt", 70, 1) 
                    ch_p "Let's not do that right now, [E_Pet]."
                    call Emma_Namecheck
                    call Statup("Emma", "Obed", 90, 1)
                    call Statup("Emma", "Obed", 50, 1)
                    call Statup("Emma", "Obed", 30, 2)
                    $ P_RecentActions.append("nope")      
                    call AnyWord("Emma",1,"refused","refused")  
                    return          
            #end auto
    if E_Kissed >= 10:
        "She's all over you, running her hands along your body."  
    elif E_Kissed > 7:
        "She's really sucking face."
    elif E_Kissed > 3:
        "She's really getting into it."
    else:
        "You and Emma make out for a while."    
    if Taboo:
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no kissing")
    $ E_RecentActions.append("kissing")                      
    $ E_DailyActions.append("kissing") 
    if not E_Kissed: 
        $ E_Addict -= 5       
        call Statup("Emma", "Lust", 70, 5)
        call Statup("Emma", "Love", 90, 10)
        call Statup("Emma", "Love", 60, 25)            
        call Statup("Emma", "Obed", 30, 20)
        call Statup("Emma", "Inbt", 30, 20)
        jump E_Kiss_After
    $ Trigger = "kiss you"
    $ Line = 0
    $ Cnt = 0
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
     
label E_KissCycle:
    while Round >=0:
        call Shift_Focus("Emma")
        call E_Kissing_Launch("kiss you")       
        call EmmaLust   
            
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
                  
        if  P_Focus < 100:                                                    
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                pass                
                        "Slap her ass":                     
                                    call E_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump E_KissCycle  
                        
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                        
                        "Start jack'in it." if MultiAction and Trigger2 != "jackin":
                                call E_Jackin                        
                        "Stop jack'in it." if MultiAction and Trigger2 == "jackin":
                                "You stop jack'in it."
                                $ Trigger2 = 0
                                
                        "Other options":
                                menu:   
                                    "Offhand action":
                                            if E_Action and MultiAction:
                                                call Emma_Offhand_Set
                                                if Trigger2:
                                                     $ E_Action -= 1
                                            else:
                                                ch_e "I'm actually getting a little tired, perhaps we could wrap this up?"  
                                                
                                    "Shift primary action":
                                            if E_Action and MultiAction:
                                                    menu:  
                                                        "Move a hand to her breasts. . ." if E_Kissed >= 5 and MultiAction:
                                                                if E_Action and MultiAction:
                                                                    $ Situation = "auto"
                                                                    call E_Kiss_After
                                                                    call E_Fondle_Breasts                          
                                                                    if Trigger == "fondle breasts": 
                                                                        $ Trigger2 = "kiss you"                                   
                                                                        call E_FB_Prep   
                                                                    else: 
                                                                        $ Trigger = "kiss you"     
                                                                else:
                                                                    "As your hands creep upwards, she grabs your wrists."
                                                                    ch_e "I'm actually getting a little tired, perhaps we could wrap this up?"  
                                                        "Move a hand to her thighs. . ." if E_Kissed >= 5 and MultiAction:
                                                                if E_Action and MultiAction:
                                                                    $ Situation = "auto"
                                                                    call E_Kiss_After
                                                                    call E_Fondle_Thighs   
                                                                    if Trigger == "fondle thighs": 
                                                                        $ Trigger2 = "kiss you"      
                                                                        call E_FT_Prep 
                                                                    else: 
                                                                        $ Trigger = "kiss you"     
                                                                else:
                                                                    "As your hands creep downwards, she grabs your wrists."
                                                                    ch_e "I'm actually getting a little tired, perhaps we could wrap this up?" 
                                                        "Never Mind":
                                                                jump E_KissCycle
                                            else:
                                                ch_e "I'm actually getting a little tired, perhaps we could wrap this up?" 
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
                                                        jump E_KissCycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump E_KissCycle 
                                            "Never mind":
                                                        jump E_KissCycle 
                                    "Undress Emma":
                                            call E_Undress   
                                    "Clean up Emma (locked)" if not E_Spunk:
                                            pass  
                                    "Clean up Emma" if E_Spunk:
                                            call Emma_Cleanup("ask")                                         
                                    "Never mind":
                                            jump E_KissCycle 
                        
                        "Back to Sex Menu" if MultiAction and E_Kissed >= 5:  
                                ch_p "Let's try something else." 
                                $ Situation = "shift"
                                $ Line = 0
                                jump E_Kiss_After
                        "End Scene": 
                                ch_p "Let's stop for now."
                                $ Line = 0
                                jump E_Kiss_After
        #End menu (if Line)
        
        call Shift_Focus("Emma")    
        call Sex_Dialog("Emma",Partner)
        
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
                            if 100 > E_Lust >= 70 and E_OCount < 2 and E_SEXP >= 20:             
                                    $ E_RecentActions.append("unsatisfied")                      
                                    $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_Kiss_After 
                            $ Line = "came"
     
                    if E_Lust >= 100:       
                            #If you're still going at it and Emma can cum
                            call E_Cumming
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_Kiss_After            
                    
                    #If you came
                    if Line == "came":
                            if not P_Semen:
                                "You're pretty wiped, better stop for now."
                            $ Line = 0
                            jump E_Kiss_After                 
                
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Emma")            
        #End orgasm
        
        call Escalation("Emma","E") #sees if she wants to escalate things
        
        if Round == 10:
            ch_e "We might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_e "It will be time to stop soon."        
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    ch_e "Alright, [E_Petname], that's plenty of that for now."
    
label E_Kiss_After:
    call EmmaFace("sexy") 
    
    $ E_Kissed += 1
    $ E_Action -=1
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1        
    
    call Partner_Like("Emma",1)
    
    if "kissing" not in E_RecentActions:
        if E_Love > 300:
            call Statup("Emma", "Love", 60, 4)
        call Statup("Emma", "Love", 70, 1)
        $ E_RecentActions.append("kissing")                      
        $ E_DailyActions.append("kissing") 
     
    if E_Kissed > 10: 
            pass        
    elif E_Kissed == 10:
            call EmmaFace("smile", 1)        
            ch_e "This has been a pleasant surprise."
    elif E_Kissed == 5:
            ch_e "You're surprisingly talented. . ." 
    elif E_Kissed == 1:    
            $ E_SEXP += 1 
        
    if not Situation and E_Kissed > 5 and E_Lust > 50 and ApprovalCheck("Emma", 950):
            call EmmaFace("sexy", 1)
            $E_Brows = "sad"
            ch_e "Does that satisfy you, [E_Petname]?"  
     
    $ Tempmod = 0  
    if Situation:
        ch_e "What were you considering?"
    else:
        call E_Pos_Reset  
    call Checkout
    return


# end Makeout //////////////////////////////////////////////////////////////////////

            

##  E_Masturbating //////////////////////////////////////////////////////////////////////
# Cnt 1 means she's seen you, Cnt 0 means she hasn't.
label E_Masturbate: #(Situation = Situation):
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Emma")
    if E_Mast:
        $ Tempmod += 10
    if E_SEXP >= 50:
        $ Tempmod += 25
    elif E_SEXP >= 30:
        $ Tempmod += 15
    elif E_SEXP >= 15:
        $ Tempmod += 5
    if E_Lust >= 90:
        $ Tempmod += 20
    elif E_Lust >= 75:
        $ Tempmod += 5
    if "exhibitionist" in E_Traits:      
        $ Tempmod += (3*Taboo) 
    if "dating" in E_Traits or "sex friend" in E_Petnames:
        $ Tempmod += 10
    elif "ex" in E_Traits:
        $ Tempmod -= 40  
    if E_ForcedCount and not E_Forced:        
        $ Tempmod -= 5 * E_ForcedCount   
        
    $ Approval = ApprovalCheck("Emma", 1300, TabM = 2) # 120, 135, 150, Taboo -80(200)
    
    call DrainWord("Emma","unseen",1,0) #She sees you, so remove unseens
    
    if Situation == "join":       # This triggers if you ask to join in        
                if Approval > 1 or (Approval and E_Lust >= 50):
                    menu:        
                        extend ""
                        "Would you like some help? I could lend some helping hands. . ."  if P_Semen and E_Action:
                                call Statup("Emma", "Love", 90, 1)
                                call Statup("Emma", "Obed", 50, 2)
                                call EmmaFace("sexy")
                                ch_e "Hm, well I do have my hands full with these. . ."                  
                                call Statup("Emma", "Obed", 70, 2)
                                call Statup("Emma", "Inbt", 70, 1)
                                $ Trigger2 = "fondle breasts"
                                $ E_Mast += 1
                                jump EM_Cycle
                        "Would you like some help? I could. . . up to you, I guess." if P_Semen and E_Action:
                                call Statup("Emma", "Love", 70, 2)
                                call Statup("Emma", "Love", 90, 1)
                                call EmmaFace("sexy")
                                ch_e "I suppose I could use some added attention. . ."                
                                call Statup("Emma", "Obed", 70, 2)
                                call Statup("Emma", "Inbt", 70, 1)
                                $ D20 = renpy.random.randint(1, 20)
                                if D20 > 10:
                                    $ Trigger2 = "fondle breasts"
                                else:
                                    $ Trigger2 = "suck breasts"
                                $ E_Mast += 1
                                jump EM_Cycle
                        "Why don't we take care of each other?" if P_Semen and E_Action:
                                call EmmaFace("sexy")
                                ch_e "I suppose I could spare some attention. . ."                    
                                $ renpy.pop_call()          #removes the call to this label 
                                return                      #returns to sexmenu=
                        "You look like you have things well in hand. . .":
                                if E_Lust >= 50:
                                    call Statup("Emma", "Love", 70, 2)
                                    call Statup("Emma", "Love", 90, 1)      
                                    call EmmaFace("sexy")
                                    ch_e "So you prefer to watch. . ."                    
                                    call Statup("Emma", "Obed", 80, 3)
                                    call Statup("Emma", "Inbt", 80, 5)  
                                    jump EM_Cycle
                                elif ApprovalCheck("Emma", 1200):
                                    call EmmaFace("sly")                        
                                    ch_e "I did, but I wasn't intending perfomance art."
                                else:
                                    call EmmaFace("angry")
                                    ch_e "I did, but now the mood is ruined. . ."
                                    
                #else: You've failed all checks so she kicks you out.
                $ Emma_Arms = 1  
                call EmmaOutfit  
                $ E_Action -= 1
                call Statup("Player", "Focus", 50, 30)
                call Checkout(1)
                $ Line = 0
                $ Situation = 0      
                $ renpy.pop_call()          #removes the call to this label 
                if Approval:     
                        call EmmaFace("bemused", 1)
                        if bg_current == "bg emma":
                            ch_e "Why are you even in my room?"   
                        else:
                            ch_e "I wasn't expecting visitors. . ." 
                        $ E_Blush = 0
                else:
                        call Statup("Emma", "Love", 200, -5)
                        call EmmaFace("angry")
                        $ E_RecentActions.append("angry")
                        $ E_DailyActions.append("angry")  
                        if bg_current == "bg emma":
                            ch_e "You may have noticed, I had some work to take care of, so if you'll leave me to it. . ."
                            "Emma kicks you out of her room."
                            $ renpy.pop_call()
                            jump Campus_Map  
                        else:
                            ch_e "I think I'll be leaving, if you don't mind."                            
                            hide Emma with easeoutright
                            call Remove_Girl("Emma")
                return                      #returns to sexmenu, which returns to original    
    #End of "Join" option
    
    
    
    if Situation == "Emma":                                                                  #Emma auto-starts   
                if Approval > 2:                                                      # fix, add emma auto stuff here
                        if E_Legs == "skirt":
                            "Emma's hand snakes down her body, and hikes up her skirt."
                            $ E_Upskirt = 1
                        elif E_Legs == "pants":
                            "Emma slides her hand down her body and into her pants."  
                        elif HoseNum("Emma") >= 5:
                            "Emma's hand slides down her body and under her [E_Hose]."
                        elif E_Panties:                
                            "Emma's hand slides down her body and under her [E_Panties]."
                        else:
                            "Emma's hand slides down her body and begins to caress her pussy."
                        $ E_SeenPanties = 1
                        "She starts to slowly rub herself."
                        call Emma_First_Bottomless
                        menu:
                            "What do you do?"
                            "Nothing.":                    
                                    call Statup("Emma", "Inbt", 80, 3) 
                                    call Statup("Emma", "Inbt", 60, 2)
                                    "Emma begins to masturbate."
                            "Go for it.":       
                                    call EmmaFace("sexy, 1")                    
                                    call Statup("Emma", "Inbt", 80, 3) 
                                    ch_p "That is so sexy, [E_Pet]."
                                    call Emma_Namecheck
                                    "You lean back and enjoy the show."
                                    call Statup("Emma", "Love", 80, 1)
                                    call Statup("Emma", "Obed", 90, 1)
                                    call Statup("Emma", "Obed", 50, 2)
                            "Ask her to stop.":
                                    call EmmaFace("surprised")       
                                    call Statup("Emma", "Inbt", 70, 1) 
                                    ch_p "Let's not do that right now, [E_Pet]."
                                    call Emma_Namecheck
                                    "Emma pulls her hands away from herself."
                                    call EmmaOutfit
                                    call Statup("Emma", "Obed", 90, 1)
                                    call Statup("Emma", "Obed", 50, 1)
                                    call Statup("Emma", "Obed", 30, 2)
                                    return            
                        jump EM_Prep
                else:                
                        $ Tempmod = 0                               # fix, add emma auto stuff here
                        $ Trigger2 = 0
                return            
    #End if Emma intitiates this action
    
    #first time
    if not E_Mast:                                                                
            call EmmaFace("surprised", 1)
            $ E_Mouth = "kiss"
            ch_e "So you enjoy a good show then. . ."
            if E_Forced:
                call EmmaFace("sad")
                ch_e "but. . . {i}only{/i} a show?"
            
            
    #First time dialog             
    if not E_Mast and Approval:                                                      
            if E_Forced: 
                call EmmaFace("sad")
                call Statup("Emma", "Love", 70, -3, 1)
                call Statup("Emma", "Love", 20, -2, 1)
            elif E_Love >= E_Obed and E_Love >= E_Inbt:
                call EmmaFace("sexy")
                $ E_Brows = "sad"
                $ E_Mouth = "smile" 
                ch_e "I don't usually show this side . . ."          
            elif E_Obed >= E_Inbt:
                call EmmaFace("normal")
                ch_e "If that's what you're into, [E_Petname]. . ."            
            else: # Uninhibited 
                call EmmaFace("sad")
                $ E_Mouth = "smile"             
                ch_e "I do enjoy a good performance . . ."     
    
    
    #Second time+ initial dialog
    elif Approval:                                                                       
            if E_Forced: 
                call EmmaFace("sad")
                call Statup("Emma", "Love", 70, -3, 1)
                call Statup("Emma", "Love", 20, -2, 1)
                ch_e "Again? Just you only want to watch?"  
            elif Approval and "masturbation" in E_RecentActions:
                call EmmaFace("sexy", 1)
                ch_e "I still have some. . . work I could be doing. . ."    
                jump EM_Prep
            elif Approval and "masturbation" in E_DailyActions:
                call EmmaFace("sexy", 1)
                $ Line = renpy.random.choice(["I was that good?",       
                    "Didn't get enough earlier?",
                    "I did enjoy the audience participation. . ."]) 
                ch_e "[Line]"            
            elif E_Mast < 3:        
                call EmmaFace("sexy", 1)
                $ E_Brows = "confused"
                ch_e "You enjoyed the show?"       
            else:       
                call EmmaFace("sexy", 1)
                $ Emma_Arms = 2
                $ Line = renpy.random.choice(["You really do like to watch.",                 
                    "Once more?",                 
                    "You enjoy watching me.",
                    "You want me to take care of myself?"]) 
                ch_e "[Line]"
                $ Line = 0
    #End second time+ initial dialog
    
    #If she's into it. . .  
    if Approval >= 2:                                                                                
            if E_Forced:
                call EmmaFace("sad")
                call Statup("Emma", "Obed", 90, 1)
                call Statup("Emma", "Inbt", 60, 1)
                ch_e "Fine. . ." 
            else:
                call EmmaFace("sexy", 1)
                call Statup("Emma", "Love", 90, 1)
                call Statup("Emma", "Inbt", 50, 3) 
                $ Line = renpy.random.choice(["Ok.",                 
                    "It couldn't hurt having you around. . .",
                    "Very well.", 
                    "Sure, why not?",
                    "[[chuckles]. . . ok."]) 
                ch_e "[Line]"
                $ Line = 0
            call Statup("Emma", "Obed", 20, 1)
            call Statup("Emma", "Obed", 60, 1)
            call Statup("Emma", "Inbt", 70, 2) 
            jump EM_Prep   
            
    #If she's not into it, but maybe. . .    
    else:                                                                                       
        menu:
            ch_e "I don't know that I want to perform."
            "Maybe later?":
                    call EmmaFace("sexy", 1)  
                    if E_Lust > 70:                        
                        ch_e "I have plans for. . . later, but perhaps you could take part."
                    else:
                        ch_e "I couldn't say."
                    call Statup("Emma", "Love", 80, 2)
                    call Statup("Emma", "Inbt", 70, 2)               
                    return
            "You look like you could use it. . .":             
                    if Approval:
                        call EmmaFace("sexy")     
                        call Statup("Emma", "Obed", 90, 2)
                        call Statup("Emma", "Obed", 50, 2)
                        call Statup("Emma", "Inbt", 70, 3) 
                        call Statup("Emma", "Inbt", 40, 2) 
                        $ Line = renpy.random.choice(["Ok.",                 
                            "It couldn't hurt having you around. . .",
                            "Very well.", 
                            "Sure, why not?",
                            "[[chuckles]. . . ok."]) 
                        ch_e "[Line]"
                        $ Line = 0                   
                        jump EM_Prep
                    
            "Just get at it already.":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Emma", 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                    if Approval > 1 or (Approval and E_Forced):
                        call EmmaFace("sad")
                        call Statup("Emma", "Love", 70, -5, 1)
                        call Statup("Emma", "Love", 200, -5)                 
                        ch_e "Oh, if it will shut you up."  
                        call Statup("Emma", "Obed", 80, 4)
                        call Statup("Emma", "Inbt", 80, 1) 
                        call Statup("Emma", "Inbt", 60, 3)  
                        $ E_Forced = 1  
                        jump EM_Prep
                    else:                              
                        call Statup("Emma", "Love", 200, -20)     
                        $ E_RecentActions.append("angry")
                        $ E_DailyActions.append("angry")
    # end of asking her to do it
    
    #She refused all offers.
    $ Emma_Arms = 1                
    if E_Forced:
            call EmmaFace("angry", 1)
            ch_e "That's something I won't do."
            call Statup("Emma", "Lust", 90, 5)         
            if E_Love > 300:
                call Statup("Emma", "Love", 70, -2)
            call Statup("Emma", "Obed", 50, -2)    
            $ E_RecentActions.append("angry")
            $ E_DailyActions.append("angry")   
            $ E_RecentActions.append("no masturbation")                      
            $ E_DailyActions.append("no masturbation") 
            return
    elif Taboo:                             # she refuses and this is too public a place for her
            call EmmaFace("angry", 1)          
            $ E_DailyActions.append("tabno") 
            ch_e "Obviously not in someplace so exposed."     
            call Statup("Emma", "Lust", 90, 5)  
            call Statup("Emma", "Obed", 50, -3)    
            return                
    elif E_Mast:
            call EmmaFace("sad") 
            ch_e "I'm sure you can find something else to watch."     
    else:
            call EmmaFace("normal", 1)
            ch_e "I don't think so, [E_Petname]."  
    $ E_RecentActions.append("no masturbation")                      
    $ E_DailyActions.append("no masturbation") 
    $ Tempmod = 0 
    return

label EM_Prep: 
    $ E_Upskirt = 1    
    $ E_PantiesDown = 1 
    call Emma_First_Bottomless(1)
    call Set_The_Scene(Dress=0)  
    
    #if she hasn't seen you yet. . .
    if "unseen" in E_RecentActions:
            call EmmaFace("sexy")
            $ E_Eyes = "closed"
            $ Emma_Arms = 2
            "You see Emma leaning back, masturbating. You don't think she's noticed you yet."
    else:    
            call EmmaFace("sexy")
            $ Emma_Arms = 2
            "Emma lays back and starts to toy with herself."
            if not E_Mast:#First time        
                    if E_Forced:
                        call Statup("Emma", "Love", 90, -20)
                        call Statup("Emma", "Obed", 70, 45)
                        call Statup("Emma", "Inbt", 80, 35) 
                    else:
                        call Statup("Emma", "Love", 90, 15)
                        call Statup("Emma", "Obed", 70, 35)
                        call Statup("Emma", "Inbt", 80, 40)  
        
    
    $ Trigger = "masturbation"   
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0 
    $ Line = 0
    if Taboo:
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no masturbation")
    $ E_RecentActions.append("masturbation")                      
    $ E_DailyActions.append("masturbation") 
            
label EM_Cycle:  
    if Situation == "join":
        $ renpy.pop_call() 
        $ Situation = 0 
        
    while Round >=0:  
        call E_Pos_Reset("masturbation")
        call Shift_Focus("Emma") 
        call EmmaLust  
        if "unseen" in E_RecentActions:  
                $ E_Eyes = "closed"
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if  P_Focus < 100:                                                    
                    #Player Command menu                                        
                    menu:
                        "Keep Watching.":
                                pass
                                
                        "Emma. . .[[jump in]" if "unseen" not in E_RecentActions and E_Loc == bg_current:                 
                                "Emma slows what she's doing with a sly grin."
                                ch_e "Enjoying the show?"
                                $ Situation = "join"
                                call E_Masturbate               
                        "\"Ahem. . .\"" if "unseen" in E_RecentActions and E_Loc == bg_current:  
                                jump EM_Interupted    
                                                   
                        "Start jack'in it." if Trigger2 != "jackin":
                                call E_Jackin                   
                        "Stop jack'in it." if Trigger2 == "jackin":
                                $ Trigger2 = 0    
                                            
                        "Slap her ass" if E_Loc == bg_current:    
                                if "unseen" in E_RecentActions:
                                        "You smack Emma firmly on the ass!"
                                        jump EM_Interupted                                          
                                else:
                                        call E_Slap_Ass                                        
                                        $ Cnt += 1
                                        $ Round -= 1    
                                        jump EM_Cycle  
                           
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
                                    "Offhand action" if E_Loc == bg_current:
                                            if E_Action and MultiAction:
                                                call Emma_Offhand_Set
                                                if Trigger2:
                                                     $ E_Action -= 1
                                            else:
                                                ch_e "I'm actually getting a little tired, perhaps we could wrap this up?"  
                                                           
                                    "Threesome actions (locked)" if not Partner or "unseen" in E_RecentActions or E_Loc != bg_current: 
                                        pass
                                    "Threesome actions" if Partner and "unseen" not in E_RecentActions and E_Loc == bg_current:   
                                        menu:
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Emma")  
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Emma")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump EM_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump EM_Cycle 
                                            "Never mind":
                                                        jump EM_Cycle 
                                    "Undress Emma":
                                            if "unseen" in E_RecentActions:
                                                    ch_p "Oh, yeah, take it off. . ."
                                                    jump EM_Interupted
                                            else:                                        
                                                    call E_Undress   
                                    "Clean up Emma (locked)" if not E_Spunk:
                                            pass  
                                    "Clean up Emma" if E_Spunk:
                                            if "unseen" in E_RecentActions:
                                                    ch_p "You've got a little something on you. . ."
                                                    jump EM_Interupted
                                            else:                      
                                                    call Emma_Cleanup("ask")                                         
                                    "Never mind":
                                            jump EM_Cycle                               
                         
                        "Back to Sex Menu" if MultiAction and E_Loc == bg_current: 
                                    ch_p "Let's try something else."
                                    call E_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump EM_Interupted
                        "End Scene" if not MultiAction or E_Loc != bg_current: 
                                    ch_p "Let's stop for now."
                                    call E_Pos_Reset
                                    $ Line = 0
                                    jump EM_Interupted
        #End menu (if Line)
        
        call Shift_Focus("Emma")    
        call Sex_Dialog("Emma",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or E_Lust >= 100:   
                    #If you can cum:
                    if P_Focus >= 100:
                        if "unseen" not in E_RecentActions: 
                            #if she knows you're there
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
                            if E_Loc == bg_current or E_Loc == "bg desk":
                                    jump EM_Interupted
     
                    #If Emma can cum
                    if E_Lust >= 100:                                               
                        call E_Cumming
                        if E_Loc == bg_current or E_Loc == "bg desk":
                                jump EM_Interupted
                       
                    if Line == "came": 
                        $ Line = 0
                        if not P_Semen:
                            "You're emptied out, you should probably take a break."
                            $ Trigger2 = 0 if Trigger2 == "jackin" else Trigger2
                            
                            
                        if "unsatisfied" in E_RecentActions:#And Emma is unsatisfied,  
                            "Emma still seems a bit unsatisfied with the experience."
                            menu:
                                "Let her keep going?"
                                "Yes, keep going for a bit.":
                                    $ Line = "You let her get back into it" 
                                    jump EM_Cycle  
                                "No, I'm done.":
                                    "You ask her to stop."
                                    return
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Emma")                          
        #End orgasm
        
        if "unseen" in E_RecentActions:
                if Round == 10:
                    "It's getting a bit late, Emma will probably be wrapping up soon."  
                elif Round == 5:
                    "She's definitely going to stop soon."
        else: 
                if E_Loc == bg_current:
                        call Escalation("Emma","E") #sees if she wants to escalate things
        
                if Round == 10:
                    ch_e "I thnk I'll probably take a break soon."  
                    $ E_Lust += 10
                elif Round == 5:
                    ch_e "Ung, I'm almost finished. . ."     
                    $ E_Lust += 25   
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    if "unseen" not in E_RecentActions:
        ch_e "That's probably enough of that."
    
label EM_Interupted:
    
    # If she hasn't noticed you're there before cumming
    if "unseen" in E_RecentActions:                         
                call EmmaFace("surprised", 2)
                "Emma stops what she's doing with a start, eyes wide."
                call Emma_First_Bottomless(1) 
                call EmmaFace("confused", 1, Eyes="surprised")
                if E_Loc == "bg desk":
                    $ E_Loc = bg_current
                    call Display_Emma
                    "She approaches you."
                
                #If you've been jacking it
                if Trigger2 == "jackin":
                        ch_e "!"
                        ch_e "How long have you been there?!"
                        $ E_Eyes = "down"
                        menu:
                            ch_e "And I see you've been busy. . . "
                            "A little while, it was an excellent show.":   
                                    call EmmaFace("sexy",1)
                                    call Statup("Emma", "Obed", 50, 3)
                                    call Statup("Emma", "Obed", 70, 2)
                                    ch_e "Well, obviously. . ."
                                    if E_Love >= 800 or E_Obed >= 500 or E_Inbt >= 500:
                                        $ Tempmod += 10
                                        call Statup("Emma", "Lust", 90, 5)
                                    ch_e "and I suppose you bring a lot to the table as well, don't you. . ."  
                                    
                            "I. . . just got here?":
                                    call EmmaFace("angry",1, Eyes="down")                   
                                    call Statup("Emma", "Love", 70, 2)
                                    call Statup("Emma", "Love", 90, 1)
                                    call Statup("Emma", "Obed", 50, 2)
                                    call Statup("Emma", "Obed", 70, 2)
                                    "She looks pointedly at your cock,"
                                    $ E_Eyes = "squint"
                                    ch_e "Long enough to raise your sails?"   
                                    if E_Love >= 800 or E_Obed >= 500 or E_Inbt >= 500:
                                            $ Tempmod += 10
                                            call Statup("Emma", "Lust", 90, 5)
                                            call EmmaFace("bemused", 1)
                                            ch_e "I suppose you couldn't help yourself under the circumstances. . ."   
                                    else:
                                            $ Tempmod -= 10
                                            call Statup("Emma", "Lust", 200, -5)
                        
                        if "Historia" not in P_Traits:
                                call Seen_First_Peen("Emma",Partner)
                                    
                #you haven't been jacking it                    
                else:         
                        ch_e "!"
                        ch_e "How long have you been there?!" 
                        menu:
                            extend ""
                            "A little while.":   
                                    call EmmaFace("sexy", 1)
                                    call Statup("Emma", "Obed", 50, 3)
                                    call Statup("Emma", "Obed", 70, 2)
                                    ch_e "Enjoying the show?"
                            "I just got here.":
                                    call EmmaFace("bemused", 1)
                                    call Statup("Emma", "Love", 70, 2)
                                    call Statup("Emma", "Love", 90, 1)                    
                                    ch_e "Yes, I'm sure. . ."   
                                    call Statup("Emma", "Obed", 50, 2)
                                    call Statup("Emma", "Obed", 70, 2)    
                                
                call DrainWord("Emma","unseen",1,0) #She sees you, so remove unseens
                $ E_Mast += 1
                if "classcaught" not in E_History or "Historia" in P_Traits:
                    # this activates if it's the first time in class
                    return
                if Round <= 10:
                    ch_e "Unfortunately it's getting rather late."
                    return
                $ Situation = "join"        
                call E_Masturbate
                "error: report this if you see it."
                return #should be redundant
    #End Unseen
    
    #else, if She's seen you already    
    $ E_Action -= 1
    $ E_Mast += 1    
    call Checkout
    if Situation == "shift":        
        $ Situation = 0
        return
    $ Situation = 0
        
    if Partner == "Kitty":
        call Partner_Like("Emma",4,2)
    else:
        call Partner_Like("Emma",3,2)
    
    if E_Loc != bg_current and E_Loc != "bg desk":
        return
        
    if Round <= 10:
            ch_e "Allow me to collect myself. . ."
            return
    call EmmaFace("sexy", 1)
    if E_Lust < 20:
        ch_e "I suppose that took care of my needs, at least."
    else:
        ch_e "Yes?"
    menu:
        extend ""
        "Well, I have something you could take care of. . ." if P_Semen and E_Action and MultiAction:
                $ Situation = "shift"
                return   
        "You could just keep going. . ." if P_Semen:
                call EmmaFace("sly")
                if E_Action and Round >= 10:
                    ch_e "I suppose. . ."
                    jump EM_Cycle
                else:
                    ch_e "Gimme a minute, I need to collect myself here. . ."
        "I'm good here. [[Stop]":  
                if E_Love < 800 and E_Inbt < 500 and E_Obed < 500:
                    call EmmaOutfit
                call EmmaFace("normal")
                $ E_Brows = "confused"
                ch_e "Well. . . yes. . ."
                $ E_Brows = "normal" 
        "You should probably stop for now." if E_Lust > 30:
                call EmmaFace("angry")
                ch_e "I . . . yes . ."
    if Trigger2 == "jackin":
        $ Trigger2 = 0
    return
    
## end E_Masturbating ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




# Emma_Offhand function //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


label Emma_Offhand(TempLine=0):
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
                if E_Love >= 300:
                        call Statup("Emma", "Love", 75, 1)
                $ PrimaryLust += 2 if E_Lust < 50 else 1
        
    elif Trigger2 == "fondle breasts":
                $ Line = renpy.random.choice([" You reach out and massage her voluminous breasts.", 
                        " You pass your hands gently over her warm breasts.", 
                        " Her nipples catch lightly on your fingers as you grasp her warm flesh, you can feel them stiffen.",
                        " She gasps as you lightly thumb her tight nipples."])
                $ PrimaryLust += 3           
                $ TempFocus += 2 if P_Focus < 90 else 0 
        
    elif Trigger2 == "suck breasts":
            if E_Chest:
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
            $ PrimaryLust += 4 if 60 < E_Lust < 80 else 2  
            $ TempFocus += 3 if P_Focus < 90 else 0 
        
    elif Trigger2 == "fondle pussy":
            
            $ Line = renpy.random.choice([" You put your hand against her mound and grind against it.", 
                        " You reach into her gap and she gasps as you slide your hand across and stroke her lips.", 
                        " Her legs twitch a bit as you press your thumb against her.",
                        " You slide a hand up her inner thigh, she moans a little as you reach the point where they meet."])
            $ PrimaryLust += 4 if 60 < E_Lust < 90 else 2        
            $ TempFocus += 4 if P_Focus < 90 else 0 
        
    elif Trigger2 == "lick pussy":
            if E_Legs != "pants" and not E_Panties:  
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
            $ PrimaryLust += 5 if E_Lust > 50 else 2       
            $ TempFocus += 4 if P_Focus < 90 else 0 
            
    elif Trigger2 == "fondle ass":
            if E_Legs != "pants" and not E_Panties: 
                $ Line = renpy.random.choice([" You reach out and brush your hands across her bare ass.", 
                        " You put your hand against her firm rear and grind against it.", 
                        " You reach into her gap and she gasps as you slide your hand across and stroke her puckered hole.", 
                        " Her legs twitch a bit as you press your thumb against her.",
                        " She gasps as you reach under her and lightly stroke her ass.",
                        " You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks."])
            else:
                $ Line = renpy.random.choice([" You reach out and brush your hands across her ass.", 
                        ". You put your hand against her firm rear and grind against it.", 
                        ". You reach into her gap and she gasps as you slide your hand across and stroke her puckered hole.", 
                        ". Her legs twitch a bit as you press your thumb against her.",
                        ". She gasps as you reach under her and lightly stroke her ass.",
                        ". You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks."])
            $ PrimaryLust += 2 if E_Lust < 50 else 1
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
            $ PrimaryLust += 3 if E_Lust > 70 and E_Loose else 1
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
            if "unseen" not in E_RecentActions:
                $ PrimaryLust += 3 if 20 < E_Lust < 70 else 2
                $ TempFocus += 1 if P_Focus < 70 else 0            
            $ TempFocus += 5
               
    return                      #End Emma_Offhand check
    


label Emma_Offhand_Set(Situation = Situation, TempTrigger = Trigger2):
    
    if Situation == "shift focus":        
            if TempTrigger:      
                $ Trigger2 = 0  
#                $ Situation = 0
                if TempTrigger == "fondle breasts":
                        "You shift your attention to her breasts."
                        jump E_FB_Prep
                elif TempTrigger == "suck breasts":
                        "You shift your attention to her breasts."
                        jump E_SB_Prep
                elif TempTrigger == "fondle pussy":
                        "You shift your attention to her pussy."
                        jump E_FP_Prep
                elif TempTrigger == "lick pussy":
                        "You shift your attention to her pussy."
                        jump E_LP_Prep
                elif TempTrigger == "fondle ass":
                        "You shift your attention to her ass."
                        jump E_FA_Prep
                elif TempTrigger == "insert ass":
                        "You shift your attention to her ass."
                        jump E_IA_Prep
                else: #If Trigger2 is "kiss you"
                        "You go back to kissing her deeply."
                        jump E_KissPrep                
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
                    
            "Also fondle her breasts." if Trigger in ("fondle pussy", "fondle thighs", "fondle ass", "insert ass", "suck breasts", "lick pussy", "lick ass", "sex", "anal", "hotdog", "dildo pussy", "dildo anal", "foot"):
                    $ Trigger2 = "fondle breasts"
                    call E_Fondle_Breasts
                    
            "Also suck her breasts." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "fondle ass", "insert ass", "sex", "anal", "hotdog", "dildo pussy", "dildo anal", "foot"):
                    $ Trigger2 = "suck breasts"
                    call E_Suck_Breasts
                    
            "Also fondle her pussy." if Trigger in ("fondle breasts","fondle thighs", "fondle ass", "insert ass", "suck breasts", "lick pussy", "lick ass", "sex", "anal", "hotdog", "dildo pussy", "dildo anal", "foot"):
                    $ Trigger2 = "fondle pussy"
                    call E_Fondle_Pussy
                    
            "Also fondle her ass." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "insert ass", "suck breasts", "lick pussy", "lick ass", "sex", "anal", "hotdog", "dildo pussy", "dildo anal"):
                    $ Trigger2 = "fondle ass"
                    call E_Fondle_Ass
                    
            "Also finger her ass." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "fondle ass", "suck breasts", "lick pussy", "lick ass", "sex", "hotdog", "dildo pussy", "foot"):
                    $ Trigger2 = "insert ass"
                    call E_Insert_Ass
                    
            "Also jack it." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "fondle ass", "insert ass", "suck breasts", "lick pussy", "lick ass", "dildo pussy", "dildo anal"):
                    call E_Jackin
                    
            "Nevermind":
                pass
    else: #if a Trigger is not found. . .
        "There's some kind of bug here, let Oni know." 
        
    $ Situation = 0
    return

    
# end Emma_Offhand function ////////////////////////////////////////////////////////////////////////


label Emma_ShameIndex:   
    $ E_ShameLevel = 0
    
    if Trigger == "kiss you":
        $ E_ShameLevel += 2
        
    elif Trigger in ("fondle breasts", "fondle thighs", "fondle ass"):
        $ E_ShameLevel += 6
        
    elif Trigger in ("fondle pussy", "insert ass", "suck breasts", "hotdog"):
        $ E_ShameLevel += 10
        
    elif Trigger in ("lick pussy", "dildo pussy", "lick ass", "dildo anal", "hand", "blow", "titjob", "masturbation"):
        $ E_ShameLevel += 15
    
    elif Trigger in ("sex",  "anal"):
        $ E_ShameLevel += 20
    
    
    if not Trigger2:
        pass
    if Trigger2 == "kiss you":
        $ E_ShameLevel += 2
        
    elif Trigger2 in ("fondle breasts", "fondle thighs", "fondle ass"):
        $ E_ShameLevel += 6
        
    elif Trigger2 in ("fondle pussy", "insert ass", "suck breasts", "hotdog"):
        $ E_ShameLevel += 10
        
    elif Trigger2 in ("lick pussy", "dildo pussy", "lick ass", "dildo anal", "hand"):
        $ E_ShameLevel += 15    
        
        
    if not Trigger3:
        pass
    elif Trigger3 == "kiss you":
        $ E_ShameLevel += 2
    elif Trigger3 == "kiss girl":
        $ E_ShameLevel += 3
    elif Trigger3 == "kiss both":
        $ E_ShameLevel += 4
        
    elif Trigger3 in ("fondle breasts", "fondle thighs", "fondle ass"):
        $ E_ShameLevel += 6
        
    elif Trigger3 in ("fondle pussy"):
        $ E_ShameLevel += 10
        
    elif Trigger3 in ("dildo pussy", "dildo anal", "hand"):
        $ E_ShameLevel += 15
    
    
    $ E_ShameLevel += E_Shame #adds clothing based shame
    
    return
            
label Emma_Taboo(Cnt= 1, Public=0,Choice=0):  
    if "Emma" not in P_DailyActions:
            $ P_DailyActions.append("Emma") 
    if "scent" not in P_DailyActions:
            $ P_DailyActions.append("scent") 
            
    $ Cnt = Action_Check("Emma", "recent", "spotted") if "spotted" in E_RecentActions else 1
    $ Cnt = 4 if Cnt > 4 else Cnt   
    
    $ D20 = renpy.random.randint(1, 20)  
    if D20 < 10:    
        #if you're at the point where the girls would notice you. . .
        if Taboo > 20:
            if (Trigger == "kiss you" and not Trigger2 and not Trigger3):
                pass
            elif "Emma" not in Rules:
                #if Xavier is looking. . .
                call EmmaFace("confused", 1)
                if Trigger == "blow" or Trigger == "hand" or Trigger == "titjob":
                    "Emma stops what she's doing with an annoyed look."                
                else:
                    "You feel a slight buzzing in your head and stop what you're doing."
                ch_x "Cease that behavior at once! Come to my office immediately!" 
                call AllReset("Emma")
                $ renpy.pop_call()        
                $ renpy.pop_call()
                call  Girls_Caught("Emma") #Emma_Caught
                return
            else:
                #if you've disabled Xavier's looking
                ch_x "Hmmm. . ."
                call Statup("Emma", "Inbt", 90, 2) 
                call Statup("Emma", "Lust", 200, 3) 
        call Girls_Noticed("Emma")
            
    if Taboo <= 20:
            #This is a private space with others around.
            call Girls_Noticed("Emma")
            return     
    elif Cnt < 4:                                                      
            #if this has happened less than 4 times within the current cycle of events
            
            if "public" not in E_History:
                $ E_History.append("public")
                
            if "spotted" not in E_RecentActions:
                "Some of the other students notice you and Emma."
                call Statup("Emma", "Inbt", 200, 2)               
                $ E_Rep -= 4                         
                $ P_Rep -= 2             
            elif Cnt < 3:
                "A few more students notice you and Emma."   
                call Statup("Emma", "Inbt", 200, 2)               
                $ E_Rep -= 2                    
                $ P_Rep -= 1  
            elif Cnt == 3:
                "You've got quite an audience."               
                call Statup("Emma", "Inbt", 200, 3)               
                $ E_Rep -= 1                    
                $ P_Rep -= 1  
                
            if "exhibitionist" in E_Traits:                
                    call EmmaFace("sexy", 0)                     
                    if "spotted" not in E_RecentActions:
                        ch_e "Hmm, maybe they can learn a few things, [E_Petname]."                          
                    call Statup("Emma", "Lust", 200, 5) 
                    $ Choice = "A"
            elif ApprovalCheck("Emma", 750, "I", TabM=Cnt-Public):
                    #not an exhibitionist but very uninhibited       
                    call EmmaFace("sexy", 1)                    
                    $ E_Brows = "sad"                           
                    if "spotted" not in E_RecentActions:                        
                        ch_e "Well, this is something of a situation." 
                    call Statup("Emma", "Lust", 200, 4)   
                    $ Choice = "B"
            elif ApprovalCheck("Emma", 1000, "OI", TabM=Cnt-Public):     
                    #not an exhibitionist but obedient/uninhibited          
                    call EmmaFace("confused", 2)
                    "Emma looks a bit concerned."
                    call Statup("Emma", "Lust", 200, 4)
                    $ Choice = "C"
            else:  
                    # She fails her inhibition checks
                    call EmmaFace("angry", 2)
                    if "spotted" not in E_RecentActions:    
                        "Emma bolts up with an embarassed look. She grabs her clothes and stalks off."  
                        $ E_Rep -= 3 if E_Rep >= 30 else E_Rep            
                    else:
                        "With a sudden embarrassed start, Emma stop what she's doing. She grabs her clothes and stalks off."  
                        call Statup("Emma", "Love", 90, -15) 
                    "You head back to your room."                    
                    $ Choice = "stop"
                
            if Choice != "stop":
                menu:
                    "What would you like to do?"
                    "Let them watch. . ." if "spotted" not in E_RecentActions:   
                            if Choice == "A":                
                                    call EmmaFace("sexy", 0) 
                                    ch_e "It's only fair."             
                            elif Choice == "B":            
                                    #not an exhibitionist but very uninhibited       
                                    call EmmaFace("sexy", 1)            
                                    ch_e "I do suppose we can show them how it's done."    
                            elif Choice == "C":     
                                    call EmmaFace("sexy",2)
                                    if E_Obed > E_Inbt:
                                        $ E_Eyes = "side"
                                        ch_e "I won't back down if you won't, [E_Petname]."
                                    else:          
                                        $ E_Mouth = "smile"
                                        $ E_Brows = "sad"
                                        ch_e "Not that I mind, of course."                     
                                    call Statup("Emma", "Obed", 200, 5)                       
                            "You get back to it." 
                            $ E_Blush = 1
                    "Continue" if "spotted" in E_RecentActions:
                            if Choice == "C":          
                                call Statup("Emma", "Obed", 200, 5) 
                    "Ok, let's stop.":                
                            call EmmaFace("sad")
                            if Choice == "A":               
                                    ch_e "Spoilsport."                                         
                            elif Choice == "B":            
                                    ch_e "I suppose." 
                            elif Choice == "C":     
                                    call Statup("Emma", "Love", 90, 10)          
                                    call EmmaFace("confused")
                                    $ E_Eyes = "side"
                                    ch_e "That probably would be for the best. . ." 
                            "You both run back to your rooms."
                            $ Choice = "stop"
                        
            if Choice == "stop":            
                    $ E_RecentActions.append("caught")
                    $ E_DailyActions.append("caught")          
                    show blackscreen onlayer black 
                    call Remove_Girl("Emma")
                    call EmmaOutfit
                    hide blackscreen onlayer black 
                    $ renpy.pop_call()          
                    $ renpy.pop_call()       
                    $ renpy.pop_call()                    
                    jump Player_Room             
    elif "exhibitionist" not in E_Traits:     
            call EmmaFace("sly")   
            $ E_Traits.append("exhibitionist") 
            "Emma seems to have become something of an exhibitionist."
    elif D20 > 15:
            call EmmaFace("sexy")
            "The crowd cheers."
        
    $ E_RecentActions.append("spotted") if Cnt < 4 else E_RecentActions
    $ E_DailyActions.append("spotted")  if "spotted" not in E_DailyActions else E_DailyActions
    return
    
    
label Emma_Noticed(Other = "Rogue", Silent=0, B = 0):
    if "threesome" in E_RecentActions:                  
            return
    if Partner == "Emma" and "noticed " + Other in E_RecentActions:
            return
    
    if not Silent and Partner != "Emma":
            call EmmaFace("surprised", 1)
            "Emma noticed what you and [Other] are up to."
   
    if "cockout" in P_RecentActions:
                call Emma_First_Peen     
    $ E_RecentActions.append("noticed " + Other)
    if "poly " + Other in E_Traits or (Other in P_Harem and "Emma" in P_Harem):
            #if they already have a relationship. . .
            $ B = (1000-(20*Taboo))  
    else:             
            #if they don't have a relationship. . .
            if Other == "Rogue":    
                    $ B = (E_LikeRogue - 500)  
            elif Other == "Kitty":    
                    $ B = (E_LikeKitty - 500)  
            elif Other == "Laura":    
                    $ B = (E_LikeLaura - 500)  
            if "dating" in E_Traits or "Emma" in P_Harem:
                    #if they already have a relationship. . .
                    $ B -= 200
                        
    if "three" not in E_History or "classcaught" not in E_History:   
            if bg_current == "bg emma":
                    #if you're in her room. . .
                    ch_e "If the two of you cannot keep your hands off each other, please do so elsewhere. . ."
                    "She shoves the two of you out of her room and slams the door."
                    if Other == "Rogue":    
                            $ R_Loc = "bg player"
                    elif Other == "Kitty":    
                            $ K_Loc = "bg player"
                    elif Other == "Laura":    
                            $ L_Loc = "bg player"
                    $ renpy.pop_call()        
                    $ renpy.pop_call()
                    jump Player_Room
                    
            call Remove_Girl("Emma") 
            $ E_DailyActions.append("noticed girl")     
            if not Silent:
                    "She seems uncomfortable with the situation and leaves the room."
                    "Perhaps you should ask her about it after class."
            return
            
    $ E_SpriteLoc = StageFarRight  
    call Display_Emma(0,0) 
    if Partner == "Emma":
            $ Silent = 1
    $ Partner = "Emma"  
    $ Line = 0
    if ApprovalCheck("Emma", 2000, TabM=2, Bonus = B) or ApprovalCheck("Emma", 950, "L", TabM=2, Bonus = (B/3)):
            #if she's very loose or really likes you
            call EmmaFace("sexy", 1)
            if not Silent:
                    "She decides to join you."                                      
            call Statup("Emma", "Obed", 90, 5)
            call Statup("Emma", "Inbt", 90, 5) 
            call Statup("Emma", "Lust", 90, 3) 
            if "poly " + Other not in E_Traits: 
                    $ E_Traits.append("poly " + Other) 
            call Emma_Threeway_Set(Mode="start",ActiveGirl=Other)
    elif ApprovalCheck("Emma", 650, "O", TabM=2) and ApprovalCheck("Emma", 450, "L", TabM=1) or ApprovalCheck("Emma", 800, "O", TabM=2, Bonus = (B/3)): 
            #if she likes you, but is very obedient
            call EmmaFace("sexy")
            if not Silent:
                    "She takes a seat off to the side and watches."          
            call Statup("Emma", "Love", 90, 5) 
            call Statup("Emma", "Inbt", 90, 5)  
            call Statup("Emma", "Lust", 90, 2)  
            if "poly " + Other not in E_Traits: 
                    $ E_Traits.append("poly " + Other) 
            call Emma_Threeway_Set("watch",Mode="start",ActiveGirl=Other)            
    elif ApprovalCheck("Emma", 650, "I", TabM=2) and ApprovalCheck("Emma", 450, "L", TabM=1) or ApprovalCheck("Emma", 800, "I", TabM=2, Bonus = (B/3)):
            #if she likes you, but is very uninhibited
            call EmmaFace("sexy")
            if not Silent:
                    "She sits down and watches you intently."             
            call Statup("Emma", "Love", 90, 5) 
            call Statup("Emma", "Obed", 90, 2)
            call Statup("Emma", "Inbt", 90, 2)     
            call Statup("Emma", "Lust", 90, 5) 
            if "poly " + Other not in E_Traits: 
                    $ E_Traits.append("poly " + Other) 
            call Emma_Threeway_Set("watch",Mode="start",ActiveGirl=Other)  
    elif ApprovalCheck("Emma", 1500, TabM=2, Bonus = B):
            call EmmaFace("perplexed", 1)
            if not Silent:
                    "She looks a little annoyed, but she stays and watches."
            if E_Love >= E_Obed and E_Love >= E_Inbt:
                call Statup("Emma", "Obed", 90, 2)
                call Statup("Emma", "Inbt", 90, 2)                     
            elif E_Obed >= E_Inbt:
                call Statup("Emma", "Love", 90, 2) 
                call Statup("Emma", "Inbt", 90, 2)   
            else:
                call Statup("Emma", "Love", 90, 2) 
                call Statup("Emma", "Obed", 90, 1)
                call Statup("Emma", "Inbt", 90, 1) 
            call Statup("Emma", "Lust", 90, 5)
            call Emma_Threeway_Set("watch",Mode="start",ActiveGirl=Other)  
    elif ApprovalCheck("Emma", 650, "L", TabM=1) or ApprovalCheck("Emma", 400, "O", TabM=2):
            #if she likes you or is obedient, but not enough
            call EmmaFace("angry", 2)                
            if bg_current == "bg emma": 
                    "She looks betrayed, and kicks you both out of the room."
            else:
                    "She looks betrayed, and storms out of the room."                   
            call Statup("Emma", "Love", 200, -5) 
            call Statup("Emma", "Love", 80, -5) 
            call Statup("Emma", "Love", 70, -5) 
            call Statup("Emma", "Obed", 90, -5)
            call Statup("Emma", "Lust", 89, 10) 
            if "saw with " + Other not in E_Traits: 
                    $ E_Traits.append("saw with " + Other) 
            if bg_current == "bg emma": #Kicks you out if in Emma's room
                    $ E_RecentActions.append("angry")
                    call GirlsAngry
            call Remove_Girl("Emma")
    else:
            #if she doesn't like you much
            call EmmaFace("surprised", 2)
            call Statup("Emma", "Inbt", 90, 2) 
            call Statup("Emma", "Lust", 40, 20)
            if Trigger != "kiss you":
                    call Statup("Emma", "Love", 90, -10) 
                    call Statup("Emma", "Obed", 90, -5)
                    call Statup("Emma", "Lust", 80, 10)
            if bg_current == "bg emma":
                    call Statup("Emma", "Love", 90, -5) 
                    call Statup("Emma", "Obed", 90, -5)
                    "She looks annoyed, and shoves you both out of the room."                 
            elif Trigger != "kiss you":
                "She looks annoyed, and storms out of the room." 
            else:
                "She looks a bit disgusted and walks away."    
            if bg_current == "bg emma": #Kicks you out if in Emma's room
                    $ E_RecentActions.append("angry")
                    call GirlsAngry
            call Remove_Girl("Emma")
    if Line:
        # This plays a line from a threesome action, if there is one. 
        "[Line]." 
        $ Line = 0
    return
    

