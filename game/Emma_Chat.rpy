# star Emma chat interface
label Emma_Chat_Set(Preset=0):    
    if "classcaught" not in E_History:        
            if "met" not in E_History:
                    "Who?"
                    return
            "She isn't interested in that."
            return
    elif E_Loc == "bg teacher" and bg_current == "bg classroom": 
            ch_e "We can speak after class, [E_Petname]."      
            return
            
    if "Emma" not in Digits and E_Loc != bg_current and "Emma" not in Nearby:
            "You don't have her number."
            return
    if Preset:   
            ch_p "Hey [EmmaName]. . ."
            call Shift_Focus("Emma")
            if E_Loc != bg_current:
                        show Cellphone at SpriteLoc(StageLeft)
            else:
                        hide Cellphone
            if Preset == "chat":
                    $ renpy.pop_call() #removes the call to chat subroutine
                    $ renpy.pop_call() #This removes the callback to the previous chat session
            elif Preset == "settings":
                    $ renpy.pop_call() #This removes the callback to the previous chat session
                    $ renpy.pop_call() #this removes the callback to the previous settings menu testing. . .
                    call Emma_Settings  
            elif Preset == "wardrobe":
                    $ renpy.pop_call() #This removes the callback to the previous chat session
                    $ renpy.pop_call() #this removes the callback to the previous settings menu
                    $ renpy.pop_call() #this removes the callback to the previous settings menu testing. . .
                    ch_p "I wanted to talk about your outfit. . ."
                    if Taboo:
                            if "exhibitionist" in E_Traits:
                                ch_e "Mmmmm. . ."  
                            elif ApprovalCheck("Emma", 900, TabM=4) or ApprovalCheck("Emma", 400, "I", TabM=3): 
                                ch_e "This isn't really the appropriate place for it, however. . ."
                            else:
                                ch_e "I'd rather discuss that in private."
                                jump Emma_Chat
                            call Emma_Clothes
                    elif ApprovalCheck("Emma", 600, "L") or ApprovalCheck("Emma", 300, "O"):
                            ch_e "What about my style?"
                            call Emma_Clothes
                    else:
                            ch_e "I'll let you know when I care what you think." 
            #end preset menu
                        
label Emma_Chat:
    call EmmaFace    
    call Shift_Focus("Emma")
    if E_Loc != bg_current:
                show Cellphone at SpriteLoc(StageLeft)
    else:
                hide Cellphone
    if "caught" in E_RecentActions:
                ch_e "I don't think we should be seen together, if you don't mind."
                return
    if "angry" in E_RecentActions:
                ch_e "I would not press my luck if I were you."
                return
    menu:
        ch_e "What was it you wanted to discuss, [E_Petname]?"
        "Come on over." if E_Loc != bg_current:
                    if "Emma" in Nearby and bg_current != "bg showerrroom":
                        call Swap_Nearby("Emma")
                    elif Room_Full():
                        "It's already pretty crowded here."
                        call Dismissed
                    else:
                        call Emma_Summon  
        "Ask Emma to leave" if E_Loc == bg_current:
                    call Emma_Dismissed    
                    return
        
        "Flirt with her." if not E_Chat[5]:
                    call Emma_Flirt               
        "Flirt with her. (locked)" if E_Chat[5]:  
                    pass
            
        "Sex Menu" if E_Loc == bg_current:
                    if E_Love >= E_Obed:
                        ch_p "Did you want to fool around?"  
                    else: 
                        ch_p "I want to get naughty."
                    if "angry" in E_RecentActions:  
                        ch_e "You should know better than that."
                    elif ApprovalCheck("Emma", 600, "LI"):
                        call EmmaFace("sexy")
                        ch_e "Perhaps. . ."
                        call Emma_SexMenu
                        return
                    elif ApprovalCheck("Emma", 400, "OI"):
                        ch_e "If that's what you want, [E_Petname]."
                        call Emma_SexMenu
                        return
                    else:
                        ch_e "No thanks, [E_Petname]."          
                                
        "I just wanted to talk. . .":
                    call Emma_Chitchat
                    
        "Emma's settings":                    
                    call Emma_Settings   
        
        "Relationship status":      
                    ch_p "Could we talk about us?"       
                    if "relationship" in E_DailyActions:
                        ch_e "Now you're starting to bore me."
                    elif E_Loc == bg_current:
                        call Emma_Relationship
                    else:
                        ch_e "This seems a bit serious to discuss over the phone."
                        ch_e "Later, perhaps."
                        
        "Could I get your number?" if "Emma" not in Digits:
                    if ApprovalCheck("Emma", 800, "LI"):
                        ch_e "I don't see why not."
                        $ Digits.append("Emma") 
                    elif ApprovalCheck("Emma", 500, "OI"):
                        ch_e "Hmm. . . fine, hand me your phone."             
                        $ Digits.append("Emma")
                    else:
                        ch_e "I don't think it's appropriate to give my number out to a student like that."  
                        
        "Gifts" if E_Loc == bg_current:
                ch_p "I'd like to give you something."
                call Emma_Gifts
                        
        "Add her to party" if "Emma" not in Party and E_Loc == bg_current:
                    ch_p "Could you follow me for a bit?"                                             
                    if ApprovalCheck("Emma", 1250):
                        $ Party.append("Emma")
                        ch_e "Lead away."
                        return
                    elif ApprovalCheck("Emma", 950):
                        $ Party.append("Emma")
                        ch_e "You'd better not bore me."
                        return
                    elif not ApprovalCheck("Emma", 400):
                        ch_e "I can't imagine why I would."
                    else:
                        ch_e "I'd rather not."
        "Disband party" if "Emma" in Party: 
                    ch_p "Ok, you can leave if you prefer."
                    $ Party.remove("Emma")       
                    call Emma_Schedule(0)         
                    if "leaving" in E_RecentActions:
                        call DrainWord("Emma","leaving")
                    if E_Loc == bg_current:
                        ch_e "I'm glad I have your \"permission\" to leave, but I'd rather be here."
                    elif E_Loc == "bg teacher" and bg_current == "bg classroom":
                        ch_e "I'm glad I have your \"permission\" to leave, but I {i}do{/i} have a class to teach."
                    else:
                        ch_e "If that's all then, I'll see you later."
                        call Set_The_Scene   
                    return
                
        "Lock the door" if bg_current == "bg classroom" and "locked" not in P_RecentActions:
                    ch_p "Could you lock the door?"
                    if Current_Time == "Evening" or Weekday >=5:
                            ch_e "Ooh, certainly. . ."
                            $ P_RecentActions.append("locked")
                            call Taboo_Level
                    else:
                            ch_e "I don't really think that would be appropriate in the middle of class."
                            
        "Unlock the door" if bg_current == "bg classroom" and "locked" in P_RecentActions:
                    ch_p "Could you unlock the door?"
                    ch_e "I suppose. . ."
                    $ P_RecentActions.remove("locked")
                    call Taboo_Level
            
        "Date":
                ch_p "Do you want to go on a date tonight?"
                call Emma_Date_Ask
        
        "Switch to. . .":
                menu:
                    "Rogue":
                        call Chat("Rogue")
                    "Kitty":
                        call Chat("Kitty")         
                    "Laura":
                        call Chat("Laura")
                    "Never mind":
                        pass
                        
        "Never mind.":
                    if E_Loc != bg_current:
                        ch_e "We'll talk later then."
                    return
    jump Emma_Chat

label Emma_Chat_Minimal:
    call EmmaFace    
    call Shift_Focus("Emma")
    if E_Loc != bg_current:
                show Cellphone at SpriteLoc(E_SpriteLoc)
    else:
                hide Cellphone
    if "caught" in E_RecentActions:
                ch_e "I don't think we should be seen together, if you don't mind."
                return
    if "angry" in E_RecentActions:
                ch_e "I would not press my luck if I were you."
                return
    menu:
        ch_e "What was it you wanted to discuss, [E_Petname]?"
        "Come on over." if E_Loc != bg_current:
                    ch_e "I don't think I should be visiting students at their whim."
                    ch_e "You know my office hours."
        "Ask Emma to leave" if E_Loc == bg_current:
                    ch_e "I'll come and go as I see fit, thank you."
                    
        "Sex Menu" if E_Loc == bg_current:
                    if E_Love >= E_Obed:
                        ch_p "Did you want to fool around?"  
                    else: 
                        ch_p "I want to get naughty."                        
                    ch_e "With a student? You should know better than that, [E_Petname]."  
                          
        "I just wanted to talk. . .":
                    call Emma_Chitchat
                    
        "Emma's settings":
                    ch_p "Let's talk about you."
                    ch_e "I doubt that's any of your business."
        
        "Relationship status":   
                    ch_p "Could we talk about us?"
                    ch_e "I'm not sure that's an appropriate discussion at the moment."
                        
        "Could I get your number?" if "Emma" not in Digits:
                    if ApprovalCheck("Emma", 800, "LI"):
                        ch_e "I don't see why not."
                        $ Digits.append("Emma") 
                    elif ApprovalCheck("Emma", 500, "OI"):
                        ch_e "Hmm. . . fine, hand me your phone."             
                        $ Digits.append("Emma")
                    else:
                        ch_e "I don't think it's appropriate to give my number out to a student like that."  
                        
        "Gifts" if E_Loc == bg_current:
                    ch_p "I'd like to give you something."
                    ch_e "I'm not sure that would be appropriate at the moment."
                        
        "Party up" if "Emma" not in Party and E_Loc == bg_current:
                    ch_p "Could you follow me for a bit?"
                    ch_e "I don't think I should."
                    
        "Disband party" if "Emma" in Party: 
                    ch_p "Ok, you can leave if you prefer."
                    $ Party.remove("Emma")       
                          
        "Date":
                    ch_p "Do you want to go on a date tonight?"
                    ch_e "Well that certainly doesn't seem appropriate."
                
        "Never mind.":
                    if Current_Time == "Evening":
                            ch_e "Now if that will be all, please clear out of here."
                            call EmmaFace("bemused",2)
                            ch_e "I have some. . . business to attend to." 
                    else:
                            "She seems a bit reserved. Maybe you need something to break the ice."
                            "Maybe you should check in on her after classes are over and the students leave."
                    return
    jump Emma_Chat_Minimal


#Emma Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  

label Emma_Relationship:
    menu:
        ch_e "What did you want to talk about?"
        
        "Have you considered maybe having some fun in public?" if "taboocheck" not in E_History and "taboo" not in E_History:
            call Emma_Taboo_Talk
        "We talked about maybe having some fun in public?" if "taboocheck" in E_History:
            call Emma_Taboo_Talk
            
        "Have you considered maybe having a threesome?" if "threecheck" not in E_History and "three" not in E_History:
            call Emma_ThreeCheck
        "We talked about maybe having a threesome?" if "threecheck" in E_History:
            call Emma_ThreeCheck
        
        "Do you want to be my girlfriend?" if "dating" not in E_Traits and "ex" not in E_Traits:
                $ E_DailyActions.append("relationship")
                if "asked boyfriend" in E_DailyActions and "angry" in E_DailyActions:
                    call EmmaFace("angry", 1)
                    ch_e "Pest."
                    return
                elif "asked boyfriend" in E_DailyActions:
                    call EmmaFace("angry", 1)
                    ch_e "Not today, little fly."
                    return
                elif E_Break[0]:                    
                    call EmmaFace("angry", 1)                    
                    ch_e "I don't share."
                    if "dating" in R_Traits:   
                        $ E_DailyActions.append("asked boyfriend")                     
                        return
                    elif "dating" in K_Traits:   
                        $ E_DailyActions.append("asked boyfriend")                     
                        return
                    elif "ex" in R_Traits:
                        ch_p "I'm not anymore."
                    elif "ex" in K_Traits:
                        ch_p "I'm not anymore."
                        
                $ E_DailyActions.append("asked boyfriend")
                
                if P_Harem and "EmmaYes" not in P_Traits: 
                    if len(P_Harem) >= 2:
                        ch_e "I doubt they would understand, [E_Petname]."
                    else:
                        ch_e "I doubt [P_Harem[0]] would understand, [E_Petname]."
                    return
                                
                
                if E_Event[5]:
                    call EmmaFace("bemused", 1)
                    ch_e "I believe I asked you first."
                else:
                    call EmmaFace("surprised", 2)
                    ch_e "Don't you think that might be inappropriate, [E_Petname]. . ." 
                    call EmmaFace("smile", 1)
                
                call Emma_OtherWoman
                
                if E_Love >= 800:
                        call EmmaFace("surprised", 1)
                        $ E_Mouth = "smile"
                        call Statup("Emma", "Love", 200, 40)
                        ch_e "I suppose I've become accustomed to you. . ."
                        if "boyfriend" not in E_Petnames:
                            $ E_Petnames.append("boyfriend")                
                        $ E_Traits.append("dating")                        
                        if "EmmaYes" in P_Traits:       
                                $ P_Traits.remove("EmmaYes")
                                $ P_Harem.append("Emma")
                                call Harem_Initiation
                        "Emma draws you in and kisses you deeply."
                        call EmmaFace("kiss", 1) 
                        $ E_Kissed += 1
                elif E_Obed >= 500:
                        call EmmaFace("perplexed")
                        ch_e "I don't believe \"dating\" would be the right term for it."    
                elif E_Inbt >= 500:
                        call EmmaFace("smile")                
                        ch_e "I don't think we should be \"exclusive.\""      
                else:
                        call EmmaFace("perplexed", 1)
                        ch_e "I really couldn't get serious about a student, [E_Petname]."
                    
        "When you said you loved me. . ." if "lover" not in E_Traits and E_Event[6] >= 20:
                call Emma_Love_Redux
        
        "Do you want to get back together?" if "ex" in E_Traits:
                $ E_DailyActions.append("relationship")
                if "asked boyfriend" in E_DailyActions and "angry" in E_DailyActions:
                    call EmmaFace("angry", 1)
                    ch_e "Do I have to demonstrate how unlikely that is?"
                    return
                elif "asked boyfriend" in E_DailyActions:
                    call EmmaFace("angry", 1)
                    ch_e "Now you're just embarrassing yourself."
                    return
                elif E_Break[0]: 
                    call EmmaFace("angry", 1)                    
                    if "dating" in (R_Traits,K_Traits):   
                        ch_e "I don't share."
                        return
                    elif "ex" in (R_Traits,K_Traits):
                        ch_e "I don't share."
                        ch_p "I'm not anymore."
                        $ E_Break[0] = 0
                    else:    
                        if not ApprovalCheck("Emma", 1500) or E_Break[1] > 5:
                            ch_e "Persistance will not be rewarded."
                        else:
                            call EmmaFace("sad", 1)
                            ch_e "You couldn't even wait a few days to start sniffing around again?"
                        $ E_DailyActions.append("asked boyfriend")
                        return
                        
                $ E_DailyActions.append("asked boyfriend")
                
                if P_Harem and "EmmaYes" not in P_Traits:
                    if len(P_Harem) >= 2:
                        ch_e "I doubt they would understand, [E_Petname]."
                    else:
                        ch_e "I doubt [P_Harem[0]] would understand, [E_Petname]."
                    return
                                
                $ Cnt = 0
                call Emma_OtherWoman
                                        
                if E_Love >= 800:
                    call EmmaFace("sly", 1)
                    call Statup("Emma", "Love", 90, 5)
                    ch_e "Try as I might, I can't stay mad at you."
                    if "boyfriend" not in E_Petnames:
                        $ E_Petnames.append("boyfriend")                
                    $ E_Traits.append("dating")          
                    $ E_Traits.remove("ex")                 
                    if "EmmaYes" in P_Traits:       
                            $ P_Traits.remove("EmmaYes")
                            $ P_Harem.append("Emma")
                            call Harem_Initiation
                    "Emma leans in and kisses you deeply."
                    call EmmaFace("kiss", 1) 
                    $ E_Kissed += 1
                elif E_Love >= 600 and ApprovalCheck("Emma", 1500):
                    call EmmaFace("smile", 1)
                    call Statup("Emma", "Love", 90, 5)
                    ch_e "Hrm, very well."                 
                    if "EmmaYes" in P_Traits:       
                            $ P_Traits.remove("EmmaYes")
                            $ P_Harem.append("Emma")
                            call Harem_Initiation
                    if "boyfriend" not in E_Petnames:
                        $ E_Petnames.append("boyfriend")                
                    $ E_Traits.append("dating")             
                    $ E_Traits.remove("ex")
                    call EmmaFace("kiss", 1) 
                    "Emma gives you a quick kiss."
                    call EmmaFace("sly", 1) 
                    $ E_Kissed += 1
                elif E_Obed >= 500:
                    call EmmaFace("sad")
                    ch_e "Let's keep things as they are, for now."   
                elif E_Inbt >= 500:
                    call EmmaFace("perplexed")                
                    ch_e "No, \"casual\" works better for the time being."
                else:
                    call EmmaFace("perplexed", 1)
                    ch_e "I can't be bothered with second chances."
                
        # End Back Together
         
        "I wanted to ask about [[another girl]" if "Emma" in P_Harem:
                menu:
                    "Have you reconsidered letting me date. . ."
                    "Rogue" if "Rogue" not in P_Harem:
                            call Poly_Start("Rogue",1)
                    "Kitty" if "Kitty" not in P_Harem:
                            call Poly_Start("Kitty",1)
                    "Laura" if "Laura" not in P_Harem:
                            call Poly_Start("Laura",1)
                    "Never mind":
                            pass           
                               
#        "I think we should break up." if "dating" in E_Traits:
#            if "breakup talk" in E_DailyActions:
#                ch_e "You must be joking. Again?"
#            else:
#                call Emma_Breakup        #breakup not in yet?        
            
            
#        "I'd like to bring Emma into this." if "poly Emma" not in R_Traits and not E_Break[0]:    #fix nonfunctional yet, switch over to Emma stuff
            
#            if "asked threesome" in R_RecentActions:
#                ch_r "Persistence will NOT be rewarded here."
#                return
#            elif "asked threesome" in R_DailyActions:
#                ch_r "I don't think my answer's changing any time soon." 
#                return
#            else:
#                $ R_DailyActions.append("asked threesome")                
#                $Cnt = int((R_LikeEmma - 500)/2)
#                menu:
#                    ch_r "What does she think about this?"
                        
#                    "She said I can be with you too." if "poly Rogue" in E_Traits:
#                        if ApprovalCheck("Rogue", 1800, Bonus = Cnt):
#                            call RogueFace("smile", 1)
#                            if R_Love >= R_Obed:
#                                ch_r "Just so long as we can be together, I can share."
#                            elif R_Obed >= R_Inbt:
#                                ch_r "I'm ok with that if she is."
#                            else:
#                                ch_r "Yeah, I mean I guess so."
#                                $ R_Traits.append("poly Emma")
#                        else:
#                            call RogueFace("angry", 1)
#                            ch_r "Well maybe she did, but I don't want to share."  
                    
#                    "I could ask if she'd be ok with me dating you both." if "poly Rogue" not in E_Traits:
#                        if ApprovalCheck("Rogue", 1800, Bonus = Cnt) or :
#                            call RogueFace("smile", 1)
#                            if R_Love >= R_Obed:
#                                ch_r "Just so long as we can be together, I can share."
#                            elif R_Obed >= R_Inbt:
#                                ch_r "I'm ok with that if she is."
#                            else:
#                                ch_r "Yeah, I mean I guess so."                        
#                            ch_r "Go ask her, give me the night to think about it, and then come back tomorrow with her answer."
#                        else:
#                            call RogueFace("angry", 1)
#                            ch_r "Well maybe she would, but I don't want to share."  
                    
#                    "Could you ask?":
#                        if R_LikeEmma >= 700:
#                            ch_r "I have to say I've kind of been thinking about it myself."  
#                            call Statup("Rogue", "Love", 90, 5)
#                            call Statup("Rogue", "Obed", 70, 1)
#                            call Statup("Rogue", "Inbt", 80, 5)
#                        elif R_LikeEmma >= 500:
#                            ch_r "I guess, if that's what you want. . ." 
#                        elif R_Obed >= 700:
#                            ch_r "If that's what you want. . ." 
#                        else:
#                            ch_r "I can't really stand her, I don't think so."  
                            
                        
#                    "You're right, I was dumb to ask.":
#                        call RogueFace("sad")
#                        ch_r "Yeah, you were."  
                        
            #end Emma Threesome
                
        "You said you wanted me to be more in control?" if "sir" not in E_Petnames and "sir" in E_History:
                if "asked sub" in E_DailyActions:
                        ch_e "I did, you didn't."          
                else:
                        call Emma_Sub_Asked
        "You said you wanted me to be your Master?" if "master" not in E_Petnames and "master" in E_History:
                if "asked sub" in E_DailyActions:
                        ch_e "I seem to recall something about that. . ."            
                else:
                        call Emma_Sub_Asked                        
        "Never Mind":
            return
              
    return

label Emma_OtherWoman(Cnt = 0):
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    if not P_Harem:
            return
    $ Cnt = 0
    if "Rogue" == P_Harem[0]:        
            # $ Other = "Rogue"
            $Cnt = int((E_LikeRogue - 500)/2)
    elif "Kitty" == P_Harem[0]:           
            $Cnt = int((E_LikeKitty - 500)/2)
    elif "Laura" == P_Harem[0]:           
            $Cnt = int((E_LikeLaura - 500)/2)
    else:
            $Cnt = 100     
        
    call EmmaFace("perplexed")
    if len(P_Harem) >= 2:
        ch_e "But you're with [P_Harem[0]] right now, among others, apparently."
    else:    
        ch_e "But you're with [P_Harem[0]] right now."
    menu: 
        extend ""
        "She said I can be with you too." if "EmmaYes" in P_Traits:
                if ApprovalCheck("Emma", 1800, Bonus = Cnt):
                    call EmmaFace("smile", 1)
                    if E_Love >= E_Obed:
                        ch_e "I suppose you're worth sharing."
                    elif E_Obed >= E_Inbt:
                        ch_e "If she can share then I can."
                    else:
                        ch_e "Sure, why not."
                else:
                    call EmmaFace("angry", 1)
                    ch_e "I really don't care what that little slut does."  
                    $ renpy.pop_call()                                          
                    #This causes it to jump past the previous menu on the return
        
        "I could ask if she'd be ok with me dating you both." if "EmmaYes" not in P_Traits:
                if ApprovalCheck("Emma", 1800, Bonus = Cnt):
                    call EmmaFace("smile", 1)
                    if E_Love >= E_Obed:
                        ch_e "I suppose you're worth sharing."
                    elif E_Obed >= E_Inbt:
                        ch_e "If she can share then I can."
                    else:
                        ch_e "Sure, why not."                       
                    ch_e "Go ask her, give me the night to think about it, and then come back tomorrow with her answer."
                else:
                    call EmmaFace("angry", 1)
                    ch_e "I really don't care what that little slut does."    
                $ renpy.pop_call()
        
        "What she doesn't know won't hurt her.":
                if not ApprovalCheck("Emma", 1800, Bonus = -Cnt): #checks if Emma likes you more than Rogue
                    call EmmaFace("angry", 1)
                    if not ApprovalCheck("Emma", 1800):
                        ch_e "I don't want you either."
                    else:
                        ch_e "I don't want to share you."                    
                    $ renpy.pop_call() 
                
                else:
                    call EmmaFace("smile", 1)
                    if E_Love >= E_Obed:
                        ch_e "I suppose we could arrange something."
                    elif E_Obed >= E_Inbt:
                        ch_e "If you insist."
                    else:
                        ch_e "I don't see why not."
                    $ E_Traits.append("downlow")
                
        "I can break it off with her.":
                    call EmmaFace("sad")
                    ch_e "Then we can talk after you have."                                   
                    $ renpy.pop_call()
            
        "You're right, I was dumb to ask.":
                    call EmmaFace("sad")
                    ch_e "Obviously. . ."                    
                    $ renpy.pop_call()   
    return
#End Emma Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////      
    
    
    
#Emma Settings ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  
label Emma_Settings:
    menu:
        ch_p "Let's talk about you."
        "Wardrobe":     
                if E_Loc != "bg player" and E_Loc != "bg emma": 
                    if Taboo:                        
                        ch_p "I wanted to talk about your style."
                        if "exhibitionist" in E_Traits:
                            ch_e "Mmmmm. . ."  
                        elif ApprovalCheck("Emma", 900, TabM=4) or ApprovalCheck("Emma", 400, "I", TabM=3): 
                            ch_e "This isn't really the appropriate place for it, however. . ."
                            return #alter to be conditional
                        else:
                            ch_e "I'd rather discuss that in private."
                            return
                    call Emma_Clothes
                elif ApprovalCheck("Emma", 900, TabM=4) or ApprovalCheck("Emma", 600, "L") or ApprovalCheck("Emma", 300, "O"):
                    ch_e "What about my style?"
                    call Emma_Clothes
                else:
                    ch_e "I'll let you know when I care what you think."
                
        "Shift her Personality" if ApprovalCheck("Emma", 900, "L", TabM=0) or ApprovalCheck("Emma", 900, "O", TabM=0) or ApprovalCheck("Emma", 900, "I", TabM=0):
                ch_p "Could we talk about us?"
                call Emma_Personality
        
        "Dirty Talk":
                    ch_p "About when we have sex. . ."
                    call Emma_SexChat
                    
        "Pet names":
            menu:
                "Your Pet Name":
                        ch_p "Could we talk about my pet name?"
                        if ApprovalCheck("Emma", 600, "L", TabM=0) or ApprovalCheck("Emma", 300, "O", TabM=0):
                            call Emma_Names    
                        else:
                            $ E_Mouth = "smile"
                            ch_e "It's your name, [E_Petname]."
                        
                "Her Pet Name":
                        ch_p "I've got a pet name for you, you know?"
                        if ApprovalCheck("Emma", 600, "L", TabM=0):
                            ch_e "I'm dying to hear it. . ." 
                        elif ApprovalCheck("Emma", 300, "O", TabM=0):
                            ch_e "Do you now."
                        else:
                            ch_e "You've made me curious. . ."          
                        call Emma_Pet   
                        
                "Back":
                        pass
                    
        "Other girls":
            menu:
                ch_p "How do you feel about. . ."
                "Rogue?":
                    call Emma_AboutRogue  
                "Kitty?":
                    call Emma_AboutKitty
                "Laura?":
                    call Emma_AboutLaura
                "Never mind.":
                    pass
        
        "Follow options" if "follow" in E_Traits:
                ch_p "You know how you ask if I want to follow you sometimes?"
                $ Line = 0
                menu:
                    ch_e "Yes?"
                    "You can go where you want, I'll catch up later." if "freetravels" not in E_Traits:
                            call EmmaFace("perplexed")
                            ch_e "Fine, I'll leave some mystery."
                            if "follow" not in E_DailyActions:
                                call Statup("Emma", "Love", 90, -2)
                                call Statup("Emma", "Obed", 30, 5) 
                            $ E_Traits.append("freetravels")
                            $ Line = "free"
                            
                    "You can ask if I want to follow you." if "asktravels" not in E_Traits:
                            call EmmaFace("perplexed")
                            ch_e "Don't want to be left behind?"
                            if "follow" not in E_DailyActions:
                                call Statup("Emma", "Love", 70, 2) 
                                call Statup("Emma", "Inbt", 60, 2) 
                            $ Line = "ask"
                                                
                    "Don't ever leave when I'm around." if "lockedtravels" not in E_Traits:
                            if ApprovalCheck("Emma", 600, "O") or ApprovalCheck("Emma", 900, "L"):   
                                call EmmaFace("angry", Eyes="side")
                                ch_e "I don't know why I put up with your nonsense."
                                call EmmaFace("sexy",1)
                                ch_e "But {i}fine.{/i}"
                                if "follow" not in E_DailyActions:
                                        if E_Love > 90:
                                            call Statup("Emma", "Love", 99, 2)
                                        call Statup("Emma", "Obed", 60, 10)                             
                                call Statup("Emma", "Inbt", 50, -5, 1) 
                                $ Line = "lock"
                            else:
                                call EmmaFace("angry")                        
                                ch_e "Where I go is my own business."
                            
                    "Never mind.":
                            ch_e "Whatever."
                        
                if Line:
                    $ E_DailyActions.append("follow")                
                    if "freetravels" in E_Traits:
                        $ E_Traits.remove("freetravels") 
                    if "asktravels" in E_Traits:
                        $ E_Traits.remove("asktravels") 
                    if "lockedtravels" in E_Traits:
                        $ E_Traits.remove("lockedtravels") 
                
                    if Line == "free":
                        $ E_Traits.append("freetravels")            
                    elif Line == "ask":
                        $ E_Traits.append("asktravels")                
                    elif Line == "lock":
                        $ E_Traits.append("lockedtravels")    
                    $ Line = 0        
                              
        "Gym clothes" if "asked gym" in E_DailyActions and "no ask gym" not in E_Traits:
                    ch_p "You asked me about your gym clothes?"
                    ch_p "Don't worry about that, your gym clothes are cute."   
                    ch_e "I'm glad you approve."
                    $ E_Traits.append("no ask gym")
        "Gym clothes" if "no ask gym" in E_Traits:
                    ch_p "You asked me about your gym clothes?"
                    ch_p "Forget about that, I changed my mind."   
                    ch_e "Ok, I'll keep that in mind."
                    $ E_Traits.remove("no ask gym")
        
        "Private outfit" if E_Schedule[9]:
                    #if comfy is in E_Traits, she won't ask before changing
                    ch_p "You know that outfit you wear in private?"
                    menu:
                        ch_e "Yeah, what about it?"
                        "Just put them on without asking me about it." if "comfy" not in E_Traits:
                            $ E_Traits.append("comfy")
                        "Ask before changing into that." if "comfy" in E_Traits:
                            $ E_Traits.remove("comfy")
                        "Never Mind":
                            pass
            
        "Tasks" if "sir" in E_Petnames:
                    ch_p "I have some tasks for you."
                    call Emma_Controls
            
        "Switch to. . .":
                menu:
                    "Rogue":
                        call Rogue_Chat_Set("settings")
                    "Kitty":
                        call Kitty_Chat_Set("settings")    
                    "Laura":
                        call Laura_Chat_Set("settings") 
                    "Never mind":
                        pass
        "Never mind.":
            return  
    jump Emma_Settings

# End Emma Settings  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  


# Emma Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label Emma_SexChat(Line = "Hmm? What did you want to talk about?"):
    while True:
            menu:
                ch_e "[Line]"                
                "My favorite thing to do is. . .":
                    if "setfav" in E_DailyActions:
                        ch_e "I'm aware. You just told me earlier."
                    else:
                        menu:
                            "Sex.":
                                        call EmmaFace("sly")
                                        if E_PlayerFav == "sex":
                                            call Statup("Emma", "Lust", 80, 5)
                                            ch_e "I'm well aware. . ."                                
                                        elif E_Favorite == "sex":
                                            call Statup("Emma", "Love", 90, 5)
                                            call Statup("Emma", "Lust", 80, 10)
                                            ch_e "Oh. . . as chance would have it. . ."
                                        elif E_Sex:
                                            ch_e "I can see why."
                                        else:
                                            call EmmaFace("perplexed")
                                            ch_e "And exactly {i}who{/i} are you having sex {i}with?{/i}"
                                        $ E_PlayerFav = "sex"
                                        
                            "Anal.":
                                        call EmmaFace("sly")
                                        if E_PlayerFav == "anal":
                                            call Statup("Emma", "Lust", 80, 5)
                                            ch_e "So you've told me. . ."                                
                                        elif E_Favorite == "anal":
                                            call Statup("Emma", "Love", 90, 5)
                                            call Statup("Emma", "Lust", 80, 10)
                                            ch_e "{i}Mine too{/i}. . ."
                                        elif E_Anal >= 10:
                                            ch_e "It certainly is a workout. . ."
                                        elif not E_Anal:
                                            call EmmaFace("perplexed")
                                            ch_e "Who's ass {i}are{/i} you fucking?"
                                        else:
                                            call EmmaFace("bemused")
                                            ch_e "Yes, you did seem enthusiastic. . ."
                                        $ E_PlayerFav = "anal"
                                        
                            "Blowjobs.":   
                                        call EmmaFace("sly")
                                        if E_PlayerFav == "blow":
                                            call Statup("Emma", "Lust", 80, 3)
                                            ch_e "Yes, so you've said. . ."                                
                                        elif E_Favorite == "blow":
                                            call Statup("Emma", "Love", 90, 5)
                                            call Statup("Emma", "Lust", 80, 5)
                                            ch_e "Hmm, you are delicious. . ."
                                        elif E_Blow >= 10:
                                            ch_e "I certainly can't complain . . ."
                                        elif not E_Blow:
                                            call EmmaFace("perplexed")
                                            ch_e "Oh? Is some little whore sucking you off?"
                                        else:
                                            call EmmaFace("bemused")
                                            ch_e "Yes, I enjoy it as well. . . ."
                                        $ E_PlayerFav = "blow"     
                                        
                            "Titjobs.":
                                        call EmmaFace("sly")
                                        if E_PlayerFav == "titjob":
                                            call Statup("Emma", "Lust", 80, 5)
                                            ch_e "So you're said. . ."                                
                                        elif E_Favorite == "titjob":
                                            call Statup("Emma", "Love", 90, 5)
                                            call Statup("Emma", "Lust", 80, 7)
                                            ch_e "I really enjoy it too. . ."
                                        elif E_Tit >= 10:
                                            ch_e "I can't imagine why . . ."
                                        elif not E_Tit:
                                            call EmmaFace("perplexed")
                                            ch_e "Oh, is someone else providing that service?"
                                        else:
                                            call EmmaFace("bemused")
                                            ch_e "I can understand why. . ."
                                        $ E_PlayerFav = "titjob"   
                                        
                            "Handjobs.":
                                        call EmmaFace("sly")
                                        if E_PlayerFav == "hand":
                                            call Statup("Emma", "Lust", 80, 5)
                                            ch_e "Yes, so you've said. . ."                                
                                        if E_Favorite == "hand":
                                            call Statup("Emma", "Love", 90, 5)
                                            call Statup("Emma", "Lust", 80, 7)
                                            ch_e "It certainly is a diversion. . ."
                                        elif E_Hand >= 10:
                                            ch_e "Yes, it certainly is a workout . . ."
                                        elif not E_Hand:
                                            call EmmaFace("perplexed")
                                            ch_e "Oh, is some little skank offering handies now?"
                                        else:
                                            call EmmaFace("bemused")
                                            ch_e "It certainly is a diversion. . ."
                                        $ E_PlayerFav = "hand"  
                                        
                            "Feeling you up.":
                                        $ Cnt = E_FondleB + E_FondleT + E_SuckB + E_Hotdog
                                        call EmmaFace("sly")
                                        if E_PlayerFav == "fondle":
                                            call Statup("Emma", "Lust", 80, 3)
                                            ch_e "I've heard that before. . ."                                
                                        elif E_Favorite in ("hotdog","suck breasts","fondle breasts","fondle thighs"):
                                            call Statup("Emma", "Love", 90, 5)
                                            call Statup("Emma", "Lust", 80, 5)
                                            ch_e "You do have a way with my body . ."
                                        elif not Cnt:
                                            call EmmaFace("perplexed")
                                            ch_e "I can't imagine who youre feeling up. Yet."
                                        else:
                                            call EmmaFace("bemused")
                                            ch_e "You have a very deft hand . . ."
                                        $ E_PlayerFav = "fondle"  
                                        $ Cnt = 0
                                
                            "Kissing you.":
                                        call EmmaFace("sly")
                                        if E_PlayerFav == "kiss you":
                                            call Statup("Emma", "Love", 90, 3)
                                            ch_e "I'm well aware. . ."                                
                                        elif E_Favorite == "kiss you":
                                            call Statup("Emma", "Love", 90, 5)
                                            call Statup("Emma", "Lust", 80, 5)
                                            ch_e "For some reason, the romantic in me agrees. . ."
                                        elif E_Kissed >= 10:
                                            ch_e "I love kissing you too . . ."
                                        elif not E_Kissed:
                                            call EmmaFace("perplexed")
                                            ch_e "Who {i}are{/i} you kissing, [E_Petname]?"
                                        else:
                                            call EmmaFace("bemused")
                                            ch_e "How romantic."
                                        $ E_PlayerFav = "kiss you" 
                                
                        $ E_DailyActions.append("setfav") 
                            
                "What's your favorite thing to do?":
                                if not ApprovalCheck("Emma", 800):
                                        call EmmaFace("perplexed")
                                        ch_e "I don't believe that's an appropriate question. . ."                                    
                                else:
                                        if E_SEXP >= 50:
                                            call EmmaFace("sly")
                                            ch_e "You really should know already . ."   
                                        else:                 
                                            call EmmaFace("bemused")
                                            $ E_Eyes = "side"
                                            ch_e "Hmm, I suppose I could tell you. . ."
                                            
                                            
                                        if not E_Favorite or E_Favorite == "kiss":
                                            ch_e "Call me a romantic, but I enjoy kissing you. . ."  
                                        elif E_Favorite == "anal":
                                                ch_e "I really enjoy anal."  
                                        elif E_Favorite == "lick ass":
                                                ch_e "I enjoy it when you lick my asshole." 
                                        elif E_Favorite == "insert ass":
                                                ch_e "I enjoy it when you stick a finger in my ass." 
                                        elif E_Favorite == "sex":
                                                ch_e "I like when you fuck me hard." 
                                        elif E_Favorite == "lick pussy":
                                                ch_e "I like when you lick my pussy." 
                                        elif E_Favorite == "fondle pussy":
                                                ch_e "I like when you finger me." 
                                        elif E_Favorite == "blow":
                                                ch_e "I quite enjoy sucking you, is that a problem?" 
                                        elif E_Favorite == "tit":
                                                ch_e "I enjoy using my tits." 
                                        elif E_Favorite == "hand":
                                                ch_e "I enjoy stroking you off." 
                                        elif E_Favorite == "hotdog":
                                                ch_e "I enjoy it when you grind against me." 
                                        elif E_Favorite == "suck breasts":
                                                ch_e "You are good at sucking my tits."  
                                        elif E_Favorite == "fondle breasts":
                                                ch_e "You are good at fondling my tits."  
                                        elif E_Favorite == "fondle thighs":
                                                ch_e "I enjoy when you massage my thighs."
                                        else:
                                                ch_e "I'm really not sure. . ."    
                                                
                                # End Emma's favorite things.
                    
                    
                "Don't talk as much during sex." if "vocal" in E_Traits:
                        if "setvocal" in E_DailyActions:
                            call EmmaFace("perplexed")
                            ch_e "You've made yourself clear on the matter."
                        else:              
                            if ApprovalCheck("Emma", 1000) and E_Obed <= E_Love:
                                call EmmaFace("bemused")
                                call Statup("Emma", "Obed", 90, 1)
                                ch_e "Oh, very well. . ."
                                $ E_Traits.remove("vocal")   
                            elif ApprovalCheck("Emma", 700, "O"):
                                call EmmaFace("sadside")
                                call Statup("Emma", "Obed", 90, 1)
                                ch_e "I suppose I could, [E_Petname]."
                                $ E_Traits.remove("vocal")   
                            elif ApprovalCheck("Emma", 600):
                                call EmmaFace("sly")
                                call Statup("Emma", "Love", 90, -3)
                                call Statup("Emma", "Obed", 50, -1)
                                call Statup("Emma", "Inbt", 90, 5)
                                ch_e "Don't presume to tell me what to say, [E_Petname]."
                            else:
                                call EmmaFace("angry")
                                call Statup("Emma", "Love", 90, -5)
                                call Statup("Emma", "Obed", 60, -3)
                                call Statup("Emma", "Inbt", 90, 10)
                                ch_e "I'll say what I wish, and you'll enjoy it."
                                                
                            $ E_DailyActions.append("setvocal")   
                "Talk dirty to me during sex." if "vocal" not in E_Traits:
                        if "setvocal" in E_DailyActions:
                            call EmmaFace("perplexed")
                            ch_e "We've discussed this already."
                        else:     
                            if ApprovalCheck("Emma", 1000) and E_Obed <= E_Love:
                                call EmmaFace("sly")
                                call Statup("Emma", "Obed", 90, 2)
                                ch_e "Mmmm, I believe I can do that. . ."
                                $ E_Traits.append("vocal")   
                            elif ApprovalCheck("Emma", 700, "O"):
                                call EmmaFace("sadside")
                                call Statup("Emma", "Obed", 90, 2)
                                ch_e "If that's what you wish, [E_Petname]."
                                $ E_Traits.append("vocal")   
                            elif ApprovalCheck("Emma", 600):
                                call EmmaFace("sly")
                                call Statup("Emma", "Obed", 90, 3)
                                ch_e "I suppose I could, [E_Petname]."
                                $ E_Traits.append("vocal")   
                            else:
                                call EmmaFace("angry")
                                call Statup("Emma", "Inbt", 90, 5)
                                ch_e "If I feel like it."  
                                
                            $ E_DailyActions.append("setvocal")  
                        # End Emma Dirty Talk
                    
                    
                "Don't do your own thing as much during sex." if "passive" not in E_Traits:
                        if "initiative" in E_DailyActions:
                            call EmmaFace("perplexed")
                            ch_e "I believe we've discussed this."
                        else:       
                            if ApprovalCheck("Emma", 1000) and E_Obed <= E_Love:
                                call EmmaFace("bemused")
                                call Statup("Emma", "Obed", 90, 1)
                                ch_e "Oh, so you want to take charge? . ."   
                                $ E_Traits.append("passive")                 
                            elif ApprovalCheck("Emma", 700, "O"):
                                call EmmaFace("sadside")
                                call Statup("Emma", "Obed", 90, 1)
                                ch_e "I'll await your instruction, [E_Petname]."
                                $ E_Traits.append("passive")   
                            elif ApprovalCheck("Emma", 600):
                                call EmmaFace("sly")
                                call Statup("Emma", "Love", 90, -3)
                                call Statup("Emma", "Obed", 50, -1)
                                call Statup("Emma", "Inbt", 90, 5)
                                ch_e "Oh, you don't mean that, [E_Petname]."
                            else:
                                call EmmaFace("angry")
                                call Statup("Emma", "Love", 90, -5)
                                call Statup("Emma", "Obed", 60, -3)
                                call Statup("Emma", "Inbt", 90, 10)
                                ch_e "You wish."
                                
                            $ E_DailyActions.append("initiative")  
                "Take more initiative during sex." if "passive" in E_Traits:
                        if "initiative" in E_DailyActions:
                            call EmmaFace("perplexed")
                            ch_e "I believe we've discussed this."
                        else:   
                            if ApprovalCheck("Emma", 1000) and E_Obed <= E_Love:
                                call EmmaFace("bemused")
                                call Statup("Emma", "Obed", 90, 1)
                                ch_e "Oh, you know that I will. . ."   
                                $ E_Traits.remove("passive")                     
                            elif ApprovalCheck("Emma", 700, "O"):
                                call EmmaFace("sadside")
                                call Statup("Emma", "Obed", 90, 1)
                                ch_e "I can do that, [E_Petname]."
                                $ E_Traits.remove("passive")   
                            elif ApprovalCheck("Emma", 600):
                                call EmmaFace("sly")
                                call Statup("Emma", "Obed", 90, 3)
                                ch_e "I suppose I might, [E_Petname]."
                                $ E_Traits.remove("passive")   
                            else:
                                call EmmaFace("angry")
                                call Statup("Emma", "Inbt", 90, 5)
                                ch_e "We'll see."  
                                
                            $ E_DailyActions.append("initiative")   
                "Never Mind" if Line == "Hmm? What did you want to talk about?":
                    return
                "That's all." if Line != "Hmm? What did you want to talk about?":
                    return
            if Line == "Hmm? What did you want to talk about?":
                $ Line = "Anything else?"
    return
# End Emma Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


## Emma Chitchat /////////////////// #Work in progress
label Emma_Chitchat(O=0, Options = ["default","default","default"]):    
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:                                               #adds only a specific option that was sent
        $ Options = [O]
    else:
        if "Emma" not in Digits:
                if ApprovalCheck("Emma", 500, "L") or ApprovalCheck("Emma", 250, "I"):
                    ch_e "If you'd like to reach me. . . after hours, here's my number."
                    $ Digits.append("Emma")  
                    return
                elif ApprovalCheck("Emma", 250, "O"):
                    ch_e "I should let you know how to contact me."             
                    $ Digits.append("Emma")
                    return
                
        if "hungry" not in E_Traits and (E_Swallow + E_Chat[2]) >= 10 and E_Loc == bg_current:  #She's swallowed a lot        
                call Emma_Hungry
                return  
        
#        $ Options = ["default","default","default"]
        #adds options based on accomplishments
        if "caught" in E_DailyActions and "caught chat" not in E_DailyActions:
            $ Options.append("caught")
        if E_Event[0] and "key" not in E_Chat:
            $ Options.append("key")
        if "lover" in E_Petnames and ApprovalCheck("Emma", 900, "L"): # luvy dovey       
            $ Options.append("luv")
              
        if "mandrill" in P_Traits and "cologne chat" not in E_DailyActions:
            $ Options.append("mandrill")        
        if "purple" in P_Traits and "cologne chat" not in E_DailyActions:
            $ Options.append("purple")        
        if "corruption" in P_Traits and "cologne chat" not in E_DailyActions:
            $ Options.append("corruption")
        
        if E_Date >= 1:
            #if you've dated before
            $ Options.append("dated")
        if "cheek" in E_DailyActions and "cheek" not in E_Chat:
            #If you've touched her cheek today
            $ Options.append("cheek")
        if E_Kissed >= 5:
            #if you've kissed a few times
            $ Options.append("kissed")
        if "dangerroom" in P_DailyActions:
            #If you've been in the danger room today
            $ Options.append("dangerroom")
        if "showered" in E_DailyActions:
            #If you've caught Emma showering today
            $ Options.append("showercaught")
        if "fondle breasts" in E_DailyActions or "fondle pussy" in E_DailyActions or "fondle ass" in E_DailyActions:
            #If you've fondled Emma today
            $ Options.append("fondled")
        if "Dazzler and Longshot" in E_Inventory and "256 Shades of Grey" in E_Inventory and "Avengers Tower Penthouse" in E_Inventory:   
            #If you've given Emma the books
            if "book" not in E_Chat:
                $ Options.append("booked")
        if "lace bra" in E_Inventory or "lace panties" in E_Inventory:   
            #If you've given Emma the lingerie
            if "lingerie" not in E_Chat:
                $ Options.append("lingerie")
        if E_Hand:   
            #If Emma's given a handjob
            $ Options.append("handy")
        if E_Swallow:   
            #If Emma's swallowed before
            $ Options.append("swallowed")
        if "cleaned" in E_DailyActions or "painted" in E_DailyActions:
            #If Emma's been facialed
            $ Options.append("facial")
        if E_Sleep:
            #If Emma's slept over
            $ Options.append("sleep")
        if E_CreamP or E_CreamA:
            #If Emma's been creampied
            $ Options.append("creampie")
        if E_Sex or E_Anal:
            #If Emma's been sexed
            $ Options.append("sexed")
        if E_Anal:
            #If Emma's been analed
            $ Options.append("anal")
        if "public" in E_History and "public" not in E_Chat:
            $ Options.append("public")            
            
#        if not E_Chat[0] and E_Sex:
#            $ Options.append("virgin")    
            
        if (bg_current == "bg emma" or bg_current == "bg player") and "relationship" not in E_DailyActions:
            if "lover" not in E_Petnames and E_Love >= 950 and E_Event[6] != 20: # E_Event[6]        
                $ Options.append("lover?")
            elif "sir" not in E_History and E_Obed >= 500: # E_Event[7]
                $ Options.append("sir?")      
            elif "daddy" not in E_Petnames and ApprovalCheck("Emma", 750, "L") and ApprovalCheck("Emma", 500, "O") and ApprovalCheck("Emma", 500, "I"): # E_Event[5]
                $ Options.append("daddy?")
            elif "master" not in E_History and E_Obed >= 800 and "sir" in E_Petnames: # E_Event[8]
                $ Options.append("master?")
            elif "sex friend" not in E_Petnames and E_Inbt >= 500 and bg_current == "bg classroom" and Time_Count == 2: # E_Event[9]
                $ Options.append("sexfriend?")
            elif "fuck buddy" not in E_Petnames and E_Inbt >= 800 and bg_current != E_Loc: # E_Event[10]
                $ Options.append("fuckbuddy?")  
            
        
        if not ApprovalCheck("Emma", 300):            #She dislikes you
            $ Options.append("hate") 
    
    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one
    
    if Options[0] == "mandrill":                             
        $ E_DailyActions.append("cologne chat") 
        call EmmaFace("confused")
        ch_e "(sniff, sniff). . . you aren't using that cheap baboon musk, are you? . ."
        call EmmaFace("perplexed", 1)
        ch_e ". . . though I suppose. . . he wasn't that bad. . ."    
    elif Options[0] == "purple":              
        $ E_DailyActions.append("cologne chat") 
        call EmmaFace("sly",1)
        ch_e "(sniff, sniff). . . huh, what's that smell? . ."
        ch_e ". . . was there anything I could do for you?"    
    elif Options[0] == "corruption":              
        $ E_DailyActions.append("cologne chat") 
        call EmmaFace("confused")
        ch_e "(sniff, sniff). . . that's. . . ripe. . ."
        call EmmaFace("sly")
        ch_e ". . . I may have some. . . purpose for you later. . ."
                
    elif Options[0] == "caught": # Xavier's caught you
            call EmmaFace("angry", Eyes="side")
            if "caught chat" in E_Chat:
                    ch_e "I'm getting rather tired of getting dragged into Charles' office."
                    ch_e "Perhaps we ought to be more. . . discrete." 
                    if not ApprovalCheck("Emma", 500, "I"):
                        call EmmaFace("sly", Eyes="side")
                        ch_e "Sometimes. . ."
            else:    
                    ch_e "Well that was certainly unpleasant."
                    ch_e "Xavier talked my ear off for at least an hour."
                    ch_e "Some nonsense about \"the responsibilities of an educator.\""
                    ch_e "I'll have you know, I take my responsibilities to my students. . ."
                    call EmmaFace("sly")
                    ch_e "{i}very{/i} seriously. . ."
                    if not ApprovalCheck("Emma", 500, "I"):
                        ch_e "I don't thing we should be so forward in public anymore."
                    else:
                        ch_e "I did enjoy seeing the old buzzard so worked up though. . ."
                    $ E_Chat.append("caught chat") 
    elif Options[0] == "key": # you have her key
            if E_SEXP <= 15:
                ch_e "Now just because I gave you my room key, doesn't mean you shouldn't knock. . ."
            else:
                ch_e "I gave you that key for a reason, you might want to use it sometime. . ."
            $ E_Chat.append("key") 
        
    elif Options[0] == "cheek":
            #Emma's response to having her cheek touched.
            ch_e "Earlier, you brushed my cheek. . ."
            ch_p "Yeah?  Was that okay?"
            if ApprovalCheck("Emma", 600, "L"):
                    call EmmaFace("smile",1)
                    ch_e "Yes, it was. . . intimate." 
                    $ E_Chat.append("cheek") 
            elif ApprovalCheck("Emma", 800):
                    call EmmaFace("normal",1,Eyes="side")
                    ch_e "I. . . suppose so, [E_Petname]." 
            else:
                    call EmmaFace("confused",1,Eyes="side")
                    ch_e "I just found it to be a bit. . . forward." 
            
            
    elif Options[0] == "dated":
            #Emma's response to having gone on a date with the Player.
            ch_e "You should know, I enjoyed our last date.  We should do that again sometime."

    elif Options[0] == "kissed":
            #Emma's response to having been kissed by the Player.
            call EmmaFace("sly",1)
            ch_e "You have some remarkably skilled lips, [E_Petname]."
            menu:
                extend ""
                "Hey. . .when you're good, you're good.":
                        call EmmaFace("smile",1)
                        ch_e "Oh, don't let it get to your head."
                        ch_e "-unless you're interested in sharing."
                "No. You think?":
                        ch_e "Oh, learn to take a compliment, [E_Petname]."

    elif Options[0] == "dangerroom":
            #Emma's response to Player working out in the Danger Room while Emma is present
            call EmmaFace("sly",1)
            ch_e "I caught your last Danger Room session,[E_Petname]."  
            ch_e "You certainly do. . . fill out that uniform."

    elif Options[0] == "showercaught":
            #Emma's response to being caught in the shower.
            if "shower" in E_Chat: 
                ch_e "Enjoy the show earlier?"                       
            else:
                ch_e "I do hope that my appearance in the shower earlier wasn't too distracting."            
                $ E_Chat.append("shower") 
                menu:
                    extend ""
                    "It was a total accident!  I promise!":             
                            call Statup("Emma", "Love", 50, 5)    
                            call Statup("Emma", "Love", 90, 2) 
                            if ApprovalCheck("Emma", 1000):
                                call EmmaFace("sly",1)
                                ch_e "Oh? so I can't count on a repeat performance?"
                            else:
                                call EmmaFace("smile")
                                ch_e "It happens, just don't make a habit of it."
                    "I only have eyes for you.":        
                            call Statup("Emma", "Obed", 40, 5)   
                            if ApprovalCheck("Emma", 1000) or ApprovalCheck("Emma", 700, "L"):      
                                    call Statup("Emma", "Love", 90, 3)    
                                    call EmmaFace("sly",1)
                                    ch_e "Oh, I'm sure that's true. . ."
                                    ch_e "It is nice to hear though."
                            else:                
                                    call Statup("Emma", "Love", 70, -5) 
                                    call EmmaFace("angry", Eyes="side")
                                    ch_e "I suppose it's better than being stalked by one-eye over there."                                                       
                    "Totally on purpose. I regret nothing.":
                            if ApprovalCheck("Emma", 1200):                     
                                    call Statup("Emma", "Love", 90, 3)          
                                    call Statup("Emma", "Obed", 70, 10)            
                                    call Statup("Emma", "Inbt", 50, 5) 
                                    call EmmaFace("sly",1)
                                    ch_e "Welll. . . I suppose I can appreciate your honesty."
                                    call EmmaFace("sly",1, Eyes="side")
                                    ch_e ". . .if not for your lack of follow-through."
                            elif ApprovalCheck("Emma", 800):                          
                                    call Statup("Emma", "Obed", 60, 5)            
                                    call Statup("Emma", "Inbt", 50, 5) 
                                    call EmmaFace("perplexed",2)
                                    ch_e "Hmm? I suppose I can't blame you for that."
                            else:                
                                    call Statup("Emma", "Love", 50, -10) 
                                    call Statup("Emma", "Love", 80, -10)          
                                    call Statup("Emma", "Obed", 50, 10)  
                                    call EmmaFace("angry")
                                    ch_e "Unexpectedly honest, but still unacceptable."

    elif Options[0] == "fondled":
            #Emma's response to being felt up.
            if E_FondleB + E_FondleP + E_FondleA >= 10:
                ch_e "I'll need a helping hand later." 
            else:                
                ch_e "You've displayed some rather significant talents in. . . massage."
                ch_e "We may need to explore that further. . ."

    elif Options[0] == "booked":
            #Emma's response after a Player gives her the books from the shop.
            ch_e "I read the. . . books you gave me."
            menu:
                extend ""
                "Yeah? Did you like them?":
                        call EmmaFace("sly",2)
                        ch_e "They were a bit simplistic, but certainly inspirational."
                "Good. You looked like you could use to learn a thing or two from them.":                     
                        call Statup("Emma", "Love", 90, 3)            
                        call Statup("Emma", "Inbt", 50, 10) 
                        call EmmaFace("sly")
                        ch_e "Oh, [E_Petname], the things I could teach those authors would leave them in the hospital."
            $ E_Blush = 1
            $ E_Chat.append("book") 

    elif Options[0] == "lingerie":
            #Emma's response to being given lingerie.
            call EmmaFace("sly")
            ch_e "[E_Petname], I wanted to thank you again for the. . .{i}clothing{/i} you bought me."
            ch_e "They look wonderful."
            $ E_Chat.append("lingerie") 

    elif Options[0] == "handy":
            #Emma's response after giving the Player a handjob.
            call EmmaFace("sly", Eyes="side")
            ch_e "You know, I was thinking about my hand," 
            call EmmaFace("sly")
            ch_e "on your cock. . ."
            ch_e "Oh, that expression is priceless. . ."
            ch_e "I suppose I'll have to repeat that service sometime. . ."

    elif Options[0] == "blow":
            if "blow" not in E_Chat:
                    #Emma's response after giving the Player a blowjob.
                    call EmmaFace("sly",2)
                    ch_e "You know, [E_Petname], you have a very unique flavor to you."
                    ch_p "Oh?"
                    ch_e "Your cock, I mean."
                    ch_e "Very. . . satisfying."
                    menu:
                        extend ""
                        "Well, there's always more where that came from.":                            
                                    call Statup("Emma", "Love", 90, 5)            
                                    call Statup("Emma", "Inbt", 60, 10) 
                                    call EmmaFace("sly")
                                    ch_e "I'll have to take you up on that."
                        "I'm glad it measured up to all those other guys.":
                                if ApprovalCheck("Emma", 300, "I") or not ApprovalCheck("Emma", 800):     
                                    call Statup("Emma", "Obed", 60, 10)            
                                    call Statup("Emma", "Inbt", 50, 10) 
                                    call EmmaFace("smile",1)
                                    ch_e "Oh, it certainly managed that."
                                else:                            
                                    call Statup("Emma", "Love", 80, -2)                            
                                    call Statup("Emma", "Obed", 70, 10)            
                                    call Statup("Emma", "Inbt", 50, 5) 
                                    call EmmaFace("sly")
                                    ch_e "Are you trying to imply something about my. . . experience?"      
                    $ E_Blush = 1
                    $ E_Chat.append("blow") 
            else:
                    $ Line = renpy.random.choice(["You've a taste that's easy to acquire.", 
                            "My jaw is a bit sore lately.", 
                            "If you need some. . . attention, let me know.",
                            "Mmmm. . . [she mimes her tongue knocking against her cheek.]"])
                    ch_e "[Line]"

    elif Options[0] == "swallowed":
            #Emma's response after swallowing the Player's cum.
            if "swallow" in E_Chat:                
                ch_e "I think I'd like another taste of your. . . essence."
            else:
                ch_e "You certainly have a unique flavor to your semen, [E_Petname]."
                call EmmaFace("sly",1)
                ch_e "Very. . . envigorating. . ."
                $ E_Chat.append("swallow") 

    elif Options[0] == "facial":
            #Emma's response after taking a facial from the Player.
            call EmmaFace("sexy")
            ch_e "You know, perhaps you could try to keep it away from my eyes next time?"

    elif Options[0] == "sleepover":
            #Emma's response after sleeping with the Player.
            ch_e "You're so restless in your sleep, it gives me. . . ideas."

    elif Options[0] == "creampie":
            #Another of Emma's responses after having sex with the Player.
            "Emma draws close to you so she can whisper into your ear."
            ch_e "I can still feel you. . .running down the inside of my thigh."

    elif Options[0] == "sexed":
            #A final response from Emma after having sex with the Player.
            call EmmaFace("sexy",2)
            ch_e "Since being with you, I have a lot more to think about, after class. . ."

    elif Options[0] == "anal":
            #Emma's response after getting anal from the Player.
            call EmmaFace("sly",1)
            ch_e "It's been a while since I've had anyone use the back door."
            call EmmaFace("sexy")
            ch_e "I'm glad you \"went there.\""
        
    elif Options[0] == "boyfriend?":
        call Emma_BF
    elif Options[0] == "lover?":
        call Emma_Love
    elif Options[0] == "sir?":
        call Emma_Sub
    elif Options[0] == "master?":
        call Emma_Master
    elif Options[0] == "sexfriend?":
        call Emma_Sexfriend
    elif Options[0] == "fuckbuddy?":
        call Emma_Fuckbuddy 
    elif Options[0] == "daddy?":
        call Emma_Daddy  
    
    elif Options[0] == "public": # You had sex in public
                call EmmaFace("sly")    
                ch_e "Hmm, well I suppose the cat's out of the bag now."
                call EmmaFace("sly", Eyes="side",Brows="angry")    
                if "spotted" in E_DailyActions:
                    ch_e "With that show we put on earlier, I doubt we can keep rumors from spreading."
                else:
                    ch_e "With that show we put on the other day, I doubt we can keep rumors from spreading."
                ch_e ". . ."
                call EmmaFace("sly")                               
                call Statup("Emma", "Obed", 70, 10)               
                call Statup("Emma", "Inbt", 60, 10)          
                call Statup("Emma", "Inbt", 90, 10) 
                ch_e "I suppose we'll just have to spread some more. . ."
                $ E_Chat.append("public") 
                    
    elif Options[0] == "hate": # trinty lower then 50:
        $ Line = renpy.random.choice(["I'd rather keep this professional.", 
                "If you have something to say, put it in writing.", 
                "Back off.",
                "Leave me alone."])
        ch_e "[Line]"
        
    else: #all else fell through. . .
            $ D20 = renpy.random.randint(1, 15)        
            if D20 == 1:
                    call EmmaFace("smile")
                    ch_e "You did  lovely job on the quiz the other day."
            elif D20 == 2:
                    call EmmaFace("sad")
                    ch_e "I've had a miserable amount of paperwork lately."
                    call EmmaFace("bemused")
                    ch_e "Perhaps come by after class to help?"
            elif D20 == 3:
                    call EmmaFace("surprised")
                    ch_e "You should have seen what Miss Pryde was wearing earlier!"
            elif D20 == 4:
                    call EmmaFace("sad")
                    ch_e "Preparing for next week's test has been exhausting!"
            elif D20 == 5:
                    call EmmaFace("smile")
                    ch_e "It really is a lovely day for a walk. . ."
            elif D20 == 6:
                    call EmmaFace("startled")
                    ch_e "There have been some serious issues lately with Sentinel attacks."
            elif D20 == 7:
                    call EmmaFace("smile")
                    ch_e "I've just had a positive progress report on my work so far."
            elif D20 == 8:
                    call EmmaFace("sad")
                    ch_e "This is a lovely school, but I do miss the amenities of the big city."
            elif D20 == 9:
                    call EmmaFace("confused")
                    ch_e "Do you pick up that weird humming of Xavier's in your head, or is that just me?"
            elif D20 == 10:
                    call EmmaFace("smile")
                    ch_e "I think the class is picking up the recent study sessions."
            elif D20 == 11:
                    call EmmaFace("smile")
                    ch_e "I've been looking forward to my next workout session."
            elif D20 == 12:
                    call EmmaFace("sad")
                    ch_e "I'm not sure what to do with Rogue's grades, they're starting to slip."
            elif D20 == 13:
                    call EmmaFace("smile")
                    ch_e "Not that I'm a lush or anything, but I could really do for a drink."
            elif D20 == 14:
                    call EmmaFace("sad")
                    ch_e "There's been another attack on the news, deplorable."
            elif D20 == 15:
                    call EmmaFace("sadside")
                    ch_e "I think I must have pulled something during my workout yesterday."
                    call EmmaFace("sly",Mouth="normal")
                    ch_e "Perhaps you could work it out for me?"
            else:
                    call EmmaFace("startled")
                    ch_e "As students go, you're not intollerable."
        
    $ Line = 0
    return

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
label Emma_Flirt:
    
    if E_Loc == bg_current:         
        $ E_Chat[5] = 1                                         #can only flirt once per cycle. 
        menu:        
#            "Compliment her":
                
            "Say you love her":
                        call Love_You("Emma")
                
            "Touch her cheek.":                                                                                 #Touch her cheek 
                    call E_TouchCheek
                            
            "Kiss her cheek":                                                                                   #Kiss her cheek
                    "You lean over, tilt her head back, and kiss her on the cheek."                
                    if ApprovalCheck("Emma", 700, "L", TabM=2):
                        call EmmaFace("sexy", 1) 
                        call Statup("Emma", "Love", 90, 1)          
                        call Statup("Emma", "Obed", 40, 2) 
                        ch_e ". . ."
                        ch_e "Hello. . ."
                    elif ApprovalCheck("Emma", 400, "L", TabM=3):
                        call EmmaFace("surprised", 1)
                        call Statup("Emma", "Love", 70, 2)
                        call Statup("Emma", "Love", 90, 1)          
                        call Statup("Emma", "Obed", 40, 2)            
                        call Statup("Emma", "Inbt", 20, 1) 
                        ch_e ". . . to what do I owe the pleasure?"
                    elif Taboo and ApprovalCheck("Emma", 500, "L"):                    
                        call EmmaFace("angry", 1)
                        call Statup("Emma", "Love", 90, -1)          
                        call Statup("Emma", "Obed", 60, 2)            
                        call Statup("Emma", "Inbt", 40, 1) 
                        ch_e "That's highly inappropriate, [E_Petname]"
                        ch_e "[[mumbles] -in public, at least. . ."
                    else: 
                        call EmmaFace("angry", 1)
                        call Statup("Emma", "Love", 90, -5)          
                        call Statup("Emma", "Obed", 90, 5)            
                        call Statup("Emma", "Inbt", 40, 3) 
                        ch_e "Stop that at once."
                    if "addict emma" in P_Traits:
                        $ E_Addict -= 1
                        $ E_Addictionrate += 1
                        $ E_Addictionrate = 3 if E_Addictionrate < 3 else E_Addictionrate 
                   
            "Kiss her lips":                                                                                    #Kiss her
                    if ApprovalCheck("Emma", 1000, TabM=2) or ApprovalCheck("Emma", 600, "L", TabM=2):        
                        "You lean down, tilt her head back, and plant a kiss on her lips."
                    elif ApprovalCheck("Emma", 1000) or ApprovalCheck("Emma", 600, "L"):     
                        call EmmaFace("bemused", 1)
                        $ E_Eyes = "side"         
                        call Statup("Emma", "Obed", 50, -5)            
                        call Statup("Emma", "Inbt", 40, 2) 
                        "You lean close for a kiss, but Emma gently pushes your face away."
                        ch_e "Not in public, [E_Petname]." 
                        return
                    else:                
                        call EmmaFace("angry", 1)
                        call Statup("Emma", "Love", 90, -10)          
                        call Statup("Emma", "Obed", 50, 5)            
                        call Statup("Emma", "Inbt", 40, 5) 
                        "You lean close for a kiss, but Emma gently pushes your face away."
                        ch_e "No." 
                        return
                    if E_Kissed:
                            if ApprovalCheck("Emma", 800, "L", TabM=2):
                                call EmmaFace("sexy", 1)
                                call Statup("Emma", "Love", 90, 2)          
                                call Statup("Emma", "Obed", 50, 2)
                                ch_e "Mmmmmmm. . ."
                            elif ApprovalCheck("Emma", 700, "L", TabM=2):
                                call EmmaFace("sexy", 1)
                                call Statup("Emma", "Love", 90, 2)          
                                call Statup("Emma", "Obed", 50, 2) 
                                ch_e "Hmm, hello [E_Petname]. . ."
                            elif ApprovalCheck("Emma", 550, "L", TabM=2):
                                call EmmaFace("surprised", 1)
                                call Statup("Emma", "Love", 70, 1) 
                                call Statup("Emma", "Love", 90, 2)          
                                call Statup("Emma", "Obed", 50, 2) 
                                ch_e "You're incorrigible."
                            elif Taboo and ApprovalCheck("Emma", 750):
                                call EmmaFace("angry", 1)
                                call Statup("Emma", "Love", 90, -5)          
                                call Statup("Emma", "Obed", 60, 3)            
                                call Statup("Emma", "Inbt", 40, 2) 
                                ch_e "Highly inappropriate!"
                                call EmmaFace("bemused", Eyes="side")
                                ch_e "-at least while in public. . ."
                            else: 
                                call EmmaFace("angry", 1)
                                call Statup("Emma", "Love", 90, -5)          
                                call Statup("Emma", "Obed", 90, 6)            
                                call Statup("Emma", "Inbt", 40, 3) 
                                ch_e "Down boy."
                            
                    else:                   #If this is the first kiss
                            if ApprovalCheck("Emma", 800, "L", TabM=2) or ApprovalCheck("Emma", 1200, TabM=2):
                                call EmmaFace("surprised", 1)
                                call Statup("Emma", "Love", 95, 30)          
                                call Statup("Emma", "Obed", 50, 15)
                                call Statup("Emma", "Inbt", 50, 15)
                                ch_e ". . ."
                                ch_e "Hmmm, that was a pleasant surprise. . ."
                                call EmmaFace("sexy")
                                ch_e "I could always use some more, [E_Petname]."
                            elif ApprovalCheck("Emma", 650, "L", TabM=2):
                                call EmmaFace("surprised", 1)
                                call Statup("Emma", "Love", 80, 25)            
                                call Statup("Emma", "Obed", 50, 20)
                                call Statup("Emma", "Inbt", 50, 15)
                                ch_e "Hmm?"
                                ch_e "So we're there now, are we? . ."
                            elif ApprovalCheck("Emma", 500, "L", TabM=2):
                                call EmmaFace("surprised", 1)            
                                call Statup("Emma", "Obed", 70, 20)
                                call Statup("Emma", "Inbt", 70, 20)
                                ch_e "I don't think that's really appropriate, [E_Petname]."
                            elif Taboo and ApprovalCheck("Emma", 800):
                                call EmmaFace("angry", 1)
                                call Statup("Emma", "Love", 60, -5) 
                                call Statup("Emma", "Obed", 70, 35)
                                call Statup("Emma", "Inbt", 70, 20)
                                ch_e "We can't be seen doing that, [E_Petname]."
                            else: 
                                call EmmaFace("angry", 1)
                                call Statup("Emma", "Love", 60, -10) 
                                call Statup("Emma", "Obed", 70, 45)
                                call Statup("Emma", "Inbt", 70, 25)
                                ch_e "How dare you?"
                            
                    $ E_Kissed += 1  
                    if "addict emma" in P_Traits:
                        $ E_Addict -= 1
                        $ E_Addictionrate += 1
                        $ E_Addictionrate = 3 if E_Addictionrate < 3 else E_Addictionrate 
                        
                    if ApprovalCheck("Emma", 700, TabM=3) and not Taboo:
                        if "three" not in E_History:
                                call CleartheRoom("Emma",Check=1)
                                if _return >= 1:
                                        # if there are other girls in the room. . .
                                        call Emma_ThreeCheck
                            
                        if E_Love > E_Obed and E_Love > E_Inbt:
                            ch_e "I hope there's more where that came from. . ."
                        elif E_Obed > E_Inbt:
                            ch_e "I wouldn't mind some more of that. . ."
                        else:
                            ch_e "Get over here. . ."
                        menu:
                            "Keep kissing?"
                            "You know it.":
                                call Statup("Emma", "Lust", 60, 3)  
                                call Statup("Emma", "Love", 90, 1)
                                call Statup("Emma", "Love", 60, 3) 
                                call Statup("Emma", "Inbt", 50, 1)
                                call Emma_SexAct("kissing")
                                call Trig_Reset(1)
                                return
                            "Not now [[no].":
                                call EmmaFace("bemused", 1) 
                                call Statup("Emma", "Lust", 40, 1) 
                                call Statup("Emma", "Lust", 60, 4) 
                                call Statup("Emma", "Obed", 70, 3)
                                call Statup("Emma", "Inbt", 50, 1)
                                ch_e "Tease. . ."
                            "Nope.":
                                call EmmaFace("angry", 1)
                                call Statup("Emma", "Lust", 40, 1) 
                                call Statup("Emma", "Love", 80, -2) 
                                call Statup("Emma", "Obed", 70, 4)
                                call Statup("Emma", "Inbt", 50, 1)
                                ch_e "I don't appreciate games, [E_Petname]."
                    elif Taboo:
                        call EmmaFace("sad")
                        ch_e "But we just can't."
                        ch_e "Not here."
                    else:
                        ch_e "Don't try that again."
                    #End Kiss her
                
            "Hug her":                                                                                          #Hug her
                    if ApprovalCheck("Emma", 400, TabM=2):        
                        "You lean over and wrap Emma in a warm hug."
                    else:                
                        call EmmaFace("angry", 1)
                        "You lean in with your arms wide, but Emma shoves you a step back."
                        ch_e "What exactly is that about, [E_Petname]?" 
                        return
                        
                    if E_SEXP >= 30: 
                        call Statup("Emma", "Lust", 60, 3) 
                        call Statup("Emma", "Love", 90, 1)          
                        call Statup("Emma", "Obed", 90, 3)            
                        call Statup("Emma", "Inbt", 90, 2) 
                        call EmmaFace("sexy")
                        ch_e "Hmmm, what did you have in mind, [E_Petname]."
                    elif ApprovalCheck("Emma", 800, "L", TabM=2):
                        call EmmaFace("sexy")
                        call Statup("Emma", "Love", 90, 1)          
                        call Statup("Emma", "Obed", 40, 2)            
                        call Statup("Emma", "Inbt", 30, 1) 
                        ch_e "Hmm, I do enjoy this. . ."
                    elif ApprovalCheck("Emma", 550, TabM=2):
                        call EmmaFace("surprised", 1)
                        call Statup("Emma", "Love", 90, 1)  
                        call Statup("Emma", "Love", 70, 1)        
                        call Statup("Emma", "Obed", 40, 2)            
                        call Statup("Emma", "Inbt", 30, 1)  
                        ch_e "Hm? What was it you wanted?"
                    elif Taboo and ApprovalCheck("Emma", 550):
                        call EmmaFace("angry", 1)  
                        call Statup("Emma", "Love", 70, 1)        
                        call Statup("Emma", "Obed", 50, 3)            
                        call Statup("Emma", "Inbt", 30, 2) 
                        ch_e "We can't be seen like this. . ."
                    else: 
                        call EmmaFace("angry", 1) 
                        call Statup("Emma", "Love", 40, -4)       
                        call Statup("Emma", "Obed", 50, 4)            
                        call Statup("Emma", "Inbt", 30, 2) 
                        ch_e "What was that about, [E_Petname]?"   
                        
            "Slap her ass" if E_Loc == bg_current:                                                              #Slap her ass
                    call E_Slap_Ass
                
            "Pinch her ass":                                                                                    #Pinch her ass
                    call EmmaFace("surprised", 1)
                    if E_SEXP >= 5 and ApprovalCheck("Emma", 700, TabM=2):        
                        "You come up to Emma from behind and quickly pinch her butt."
                    else:                
                        "You come up to Emma from behind and quickly pinch her butt."
                        call EmmaFace("angry")
                        "She slaps your hand away and rounds on you."
                        ch_e "Down boy!" 
                        return
                        
                    if E_SEXP >= 40: 
                        call Statup("Emma", "Lust", 60, 3) 
                        call Statup("Emma", "Love", 90, 1)           
                        call Statup("Emma", "Obed", 60, 2)          
                        call Statup("Emma", "Obed", 90, 1)            
                        call Statup("Emma", "Inbt", 50, 3) 
                        call EmmaFace("sexy")
                        ch_e "Mmm, what was that for?"
                    elif ApprovalCheck("Emma", 8000, TabM=2):
                        call EmmaFace("surprised")
                        call Statup("Emma", "Love", 90, 1)           
                        call Statup("Emma", "Obed", 60, 4)          
                        call Statup("Emma", "Obed", 90, 2)            
                        call Statup("Emma", "Inbt", 50, 2) 
                        ch_e "Mmm, watch it."
                    elif Taboo and ApprovalCheck("Emma", 800):
                        call EmmaFace("angry")
                        call Statup("Emma", "Love", 90, -4)           
                        call Statup("Emma", "Obed", 60, 5)          
                        call Statup("Emma", "Obed", 90, 3)            
                        call Statup("Emma", "Inbt", 50, 1) 
                        ch_e "That is not something you can do in public."
                    else: 
                        call EmmaFace("angry")
                        call Statup("Emma", "Love", 90, -8)           
                        call Statup("Emma", "Obed", 60, 5)          
                        call Statup("Emma", "Obed", 90, 4)            
                        call Statup("Emma", "Inbt", 50, 2)
                        ch_e "Would you like me to break those fingers?"  
                    
                    
            "Grab her tit":                                                                                     #Grab her tit
                    call EmmaFace("surprised", 1)
                    if E_SEXP >= 5 and ApprovalCheck("Emma", 700, TabM=3):        
                        "You come up to Emma and quickly honk her boob."
                    else:             
                        "You come up to Emma and quickly honk her boob."
                        call EmmaFace("angry")
                        show Emma_Sprite
                        with vpunch
                        "She slaps your hand away and elbows you in the ribs."
                        ch_e "You must learn to resist temptations, [E_Petname]." 
                        return
                        
                    if E_SEXP >= 40: 
                        call Statup("Emma", "Lust", 60, 7) 
                        call Statup("Emma", "Love", 90, 2) 
                        call EmmaFace("sly")
                        ch_e "I do enjoy this, [E_Petname]. . ."
                        $ Count = 10
                    elif ApprovalCheck("Emma", 850, "L", TabM=2):
                        call EmmaFace("sexy")
                        call Statup("Emma", "Lust", 60, 3) 
                        call Statup("Emma", "Love", 90, 1) 
                        ch_e "Mmmmmm. . ."
                        $ Count = 7
                    elif ApprovalCheck("Emma", 1200, TabM=2):
                        call EmmaFace("perplexed")  
                        call Statup("Emma", "Lust", 60, 2)         
                        ch_e "Rather forward of you, [E_Petname]."
                        $ Count = 5
                    elif Taboo and ApprovalCheck("Emma", 900):
                        call EmmaFace("angry")
                        call Statup("Emma", "Love", 90, -5)          
                        call Statup("Emma", "Obed", 90, 4)            
                        call Statup("Emma", "Inbt", 90, 1) 
                        ch_e "You should move that, immediately."
                        call Statup("Emma", "Lust", 60, 2)
                        $ Count = 1
                    else: 
                        call EmmaFace("angry")
                        call Statup("Emma", "Love", 90, -8)          
                        call Statup("Emma", "Obed", 90, 5)            
                        call Statup("Emma", "Inbt", 90, 2) 
                        ch_e "Do you want to lose that hand?" 
                        $ Count = 2
                              
                    call Statup("Emma", "Obed", 70, 3)            
                    call Statup("Emma", "Inbt", 70, 2)                     
                    while Count > 0:
                        if Count == 5:
                            call EmmaFace("sexy", 1)
                            ch_e "Mmmmm, I do enjoy that. . ."  
                            call Statup("Emma", "Lust", 90, 2)       
                            call Statup("Emma", "Inbt", 70, 1)
                        elif Count == 3:
                            call EmmaFace("perplexed")
                            call Statup("Emma", "Lust", 90, 2) 
                            ch_e "Not that I don't enjoy that, [E_Petname]. . ."
                        elif Count == 2:
                            call EmmaFace("angry")
                            call Statup("Emma", "Lust", 90, 2) 
                            call Statup("Emma", "Love", 90, -1) 
                            ch_e "Ok, enough of that. . ."
                        elif Count == 1:
                            call EmmaFace("angry")
                            ch_e "Time to stop, [E_Petname]."
                            call Statup("Emma", "Lust", 90, 2) 
                            call Statup("Emma", "Love", 90, -5) 
                            show Emma_Sprite
                            with vpunch
                            "She elbows you in the ribs."
                            ch_e "You should learn from social cues. . ." 
                        $ Count -= 1 if Count >= 0 else 0
                            
                        if Count > 0:
                            menu:
                                "Your hand is still on her chest."
                                "Let go immediately":
                                    if Count >= 7:
                                        ch_e "It's not that I really minded. . ."  
                                        call Statup("Emma", "Lust", 60, 2)         
                                        call Statup("Emma", "Inbt", 70, 1) 
                                    elif Count <= 4:
                                        ch_e "I suppose it's for the best."
                                    $ Count = 0
                                    
                                "Honk it again and let go":
                                    if Count >= 7:
                                        call EmmaFace("bemused")
                                        ch_e "Hmm, so amusing."          
                                        call Statup("Emma", "Lust", 60, 4) 
                                        call Statup("Emma", "Inbt", 70, 1)
                                    elif Count >= 4:
                                        ch_e "How droll."
                                    else:
                                        call EmmaFace("angry")
                                        ch_e "You'd better take more care."
                                    call Statup("Emma", "Obed", 70, 3)            
                                    call Statup("Emma", "Inbt", 70, 2)
                                    $ Count = 0 
                                        
                                "Fondle it a little":                            
                                    if E_FondleB and ApprovalCheck("Emma", 1100, TabM=3):                                
                                        call EmmaFace("sexy",1)
                                        $ E_Eyes = "closed"
                                        call Statup("Emma", "Lust", 90, 5) 
                                    else:
                                        call EmmaFace("perplexed")
                                        call Statup("Emma", "Lust", 90, 3) 
                                        $ Count -= 1
                                    call Statup("Emma", "Obed", 70, 4)            
                                    call Statup("Emma", "Inbt", 70, 2)
                                    ch_e "Mmm. . ."
                                    
                                "Just leave it there.":
                                    call EmmaFace("perplexed", Eyes="down")
                                    if Count == 5:
                                        call Statup("Emma", "Lust", 90, 4) 
                                    elif Count == 2:
                                        call Statup("Emma", "Lust", 90, 2) 
                                    ch_e "Um, [E_Petname]."                     
                                    call Statup("Emma", "Obed", 70, 2)            
                                    call Statup("Emma", "Inbt", 70, 1)
                                    call EmmaFace("perplexed")       
                    if Taboo:
                        ch_e "Show some respect when in public, [E_Petname]."
                    elif E_FondleB and ApprovalCheck("Emma", 1200, TabM = 3): 
                        if "three" not in E_History:
                                call CleartheRoom("Emma",Check=1)
                                if _return >= 1:
                                        # if there are other girls in the room. . .
                                        call Emma_ThreeCheck
                            
                        call EmmaFace("sexy", 1)
                        ch_e "Were you just sampling, or did you want to continue?"
                        menu:
                            extend ""
                            "Yeah!":
                                    call Statup("Emma", "Lust", 60, 5) 
                                    call Statup("Emma", "Love", 90, 2)          
                                    call Statup("Emma", "Obed", 60, 3)            
                                    call Statup("Emma", "Inbt", 60, 3) 
                                    call Emma_SexAct("breasts")
                                    call Trig_Reset(1)
                                    return
                            "Nah, that was enough.":
                                    call EmmaFace("sad", 1)
                                    call Statup("Emma", "Lust", 60, 2) 
                                    call Statup("Emma", "Love", 90, -2)          
                                    call Statup("Emma", "Obed", 60, 4)            
                                    call Statup("Emma", "Inbt", 60, 2) 
                                    ch_e "Oh. Pity."
                    elif ApprovalCheck("Emma", 900, TabM = 3):  
                        $ E_Brows = "confused"
                        $ E_Eyes = "sexy"
                        $ E_Mouth = "smile"
                        ch_e "Did you enjoy that?"
                    elif ApprovalCheck("Emma", 900): 
                        call EmmaFace("angry", 1)
                        ch_e "I can't believe you would do that in public."
                    else:
                        call EmmaFace("angry", 1)
                        ch_e "Just keep your hands to yourself."
                        
                    
            "Rub her shoulders":                                                                                #Rub her shoulders
                    "You come up to Emma from behind and gently rub her shoulders."
                    if E_SEXP >= 30:
                        call EmmaFace("sexy") 
                        call Statup("Emma", "Lust", 60, 3) 
                        call Statup("Emma", "Love", 90, 2)
                        "She sinks back into your hands"
                        ch_e "Hmm, to what do I owe the pleasure, [E_Petname]?"
                    elif ApprovalCheck("Emma", 650, "L", TabM = 2):
                        call EmmaFace("sexy")
                        call Statup("Emma", "Lust", 60, 1) 
                        call Statup("Emma", "Love", 90, 2)
                        ch_e "Well that's lovely, [E_Petname]."
                    elif ApprovalCheck("Emma", 500, TabM = 2):
                        call EmmaFace("surprised", 1)
                        call Statup("Emma", "Love", 90, 1)
                        ch_e "Well hello, [E_Petname]."
                    elif ApprovalCheck("Emma", 400):
                        call EmmaFace("angry", 1)
                        call Statup("Emma", "Love", 90, -1)
                        if Taboo:
                            ch_e "Do I have to explain boundaries to you, [E_Petname]?"
                        else:
                            ch_e "I'd rather you didn't. . ."
                    else: 
                        call EmmaFace("angry", 1)
                        "She slaps your hands away."
                        ch_e "That will be enough of that."           
                    call Statup("Emma", "Obed", 30, 3)            
                    call Statup("Emma", "Inbt", 30, 2) 
                        
            "Ask for her panties":
                    call Emma_AskPanties
                    
            "Never mind [[exit]":
                    $ E_Chat[5] = 0  
                    return
    else:
        "Emma isn't around."
            
    return
# End Emma Flirt //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //


label Emma_AskPanties(Store = 0):
    $ Store = Tempmod  
    $ Line = 0
    if not E_Panties or E_Panties == "shorts":
        if ApprovalCheck("Emma", 900):
            call EmmaFace("sexy", 1)
            call Statup("Emma", "Lust", 80, 5) 
            call Statup("Emma", "Lust", 60, 5) 
            call Statup("Emma", "Lust", 40, 10)            
            call Statup("Emma", "Inbt", 60, 5)            
            call Statup("Emma", "Inbt", 30, 10) 
            ch_e "That. . . isn't exactly an option."
        elif E_Over == "towel" or not E_Legs:
            ch_e "I think you can see that I don't have any. . ."            
        else:
            call EmmaFace("bemused", 2, Eyes="side")
            call Statup("Emma", "Lust", 80, 5) 
            call Statup("Emma", "Lust", 60, 5) 
            call Statup("Emma", "Lust", 40, 10)            
            call Statup("Emma", "Inbt", 60, 5)  
            ch_e "Hrm, I'm afraid not."            
            
    else:
        if E_SeenPussy and ApprovalCheck("Emma", 500): #You've seen her Pussy.
            $ Tempmod += 15
        elif E_SeenPanties and ApprovalCheck("Emma", 500): #You've seen her panties.
            $ Tempmod += 5 
        if "exhibitionist" in E_Traits:
            $ Tempmod += (Taboo * 5)
        if "dating" in E_Traits or "sex friend" in E_Petnames and not Taboo:
            $ Tempmod += 10
        if "no bottomless" in E_RecentActions: 
            $ Tempmod -= 20
        
        $ Line = 0
        if E_Legs == "pants" or HoseNum("Emma") >= 10: 
            if ApprovalCheck("Emma", 1000, "OI", TabM = 5) or "exhibitionist" in E_Traits:   
                $ Line = "here"
            elif ApprovalCheck("Emma", 900, TabM = 5):
                $ Line = "change"
                
        elif E_Legs == "skirt":
            if ApprovalCheck("Emma", 600, "OI", TabM = 5) or "exhibitionist" in E_Traits:   
                $ Line = "here"
            elif ApprovalCheck("Emma", 1100, TabM = 5):
                $ Line = "change"
                
        else:
            if ApprovalCheck("Emma", 1200, TabM = 5) or "exhibitionist" in E_Traits:
                $ Line = "here"
        
        
        if Line == "here":                              #She's agreed to change and will do it here
                call EmmaFace("sly")                          
                if E_Legs == "skirt":      
                    call Statup("Emma", "Obed", 60, 4)            
                    call Statup("Emma", "Inbt", 60, 4)
                else: #no pants or skirt         
                    call Statup("Emma", "Obed", 60, 6)            
                    call Statup("Emma", "Inbt", 60, 6) 
                
                call Statup("Emma", "Lust", 60, 5)    
                call Remove_Panties("Emma")
                    
                if Taboo:
                    call Statup("Emma", "Lust", 60, 5) 
                    if "exhibitionist" in E_Traits: 
                        call Statup("Emma", "Lust", 80, 5)
                        call Statup("Emma", "Lust", 200, 5)    
                    call Statup("Emma", "Obed", 80, 10)            
                    call Statup("Emma", "Inbt", 80, 10)        
            
        elif Line:                                      #She's agreed to change, but leaves the room to do it.
                if not Taboo:                           #If it's in one of your rooms                                    
                    call EmmaFace("bemused", 1) 
                    menu:
                        ch_e "I would appreciate some privacy while I change."
                        "OK.": 
                            call Statup("Emma", "Love", 90, 5) 
                            call EmmaFace("smile", 1)                                             
                            ch_e "Thank you, [E_Petname]."
                            call EmmaFace("sly", 1) 
                            call Statup("Emma", "Lust", 60, 2)         
                            call Statup("Emma", "Obed", 60, 4)            
                            call Statup("Emma", "Inbt", 60, 4)
                            show blackscreen onlayer black 
                            "You exit the room for a minute"   
                            $ E_DailyActions.append("pantyless")
                            call EmmaOutfit                             
                            hide blackscreen onlayer black 
                            if Taboo:              
                                call Quick_Taboo("Emma")
                            "When you return, she quietly hands you her balled up panties."
                            $ Line = 0
                            
                        "And miss the show?":
                            if ApprovalCheck("Emma", 1000, "LI"): 
                                call Statup("Emma", "Lust", 70, 5)          
                                call Statup("Emma", "Obed", 60, 5)            
                                call Statup("Emma", "Inbt", 60, 5) 
                                call EmmaFace("sly", 1) 
                                ch_e "How precious."
                            else:                 
                                call EmmaFace("angry", 1) 
                                call Statup("Emma", "Love", 90, -5)          
                                call Statup("Emma", "Obed", 60, -3)            
                                call Statup("Emma", "Inbt", 60, 5) 
                                ch_e "What show would that be, [Playername]?"
                                $ Line = 0
                                
                        "Nope, I'm staying.":
                            if ApprovalCheck("Emma", 600, "OI"): 
                                call EmmaFace("perplexed", 1) 
                                call Statup("Emma", "Lust", 70, 5)          
                                call Statup("Emma", "Obed", 60, 10)            
                                call Statup("Emma", "Inbt", 60, 5) 
                                ch_e "If you must."
                                call EmmaFace("normal") 
                            else:        
                                call EmmaFace("angry", 1) 
                                call Statup("Emma", "Love", 90, -10)          
                                call Statup("Emma", "Obed", 60, -5)            
                                call Statup("Emma", "Inbt", 60, 5) 
                                ch_e "Then I suppose we're done here."
                                $ Line = 0
                                
                    if Line:                                            #She agreed to stay  
                                call EmmaFace("sly", 1) 
                                if E_Legs == "pants" or HoseNum("Emma") >= 10:   
                                        call Statup("Emma", "Lust", 60, 5)         
                                        call Statup("Emma", "Obed", 60, 5)            
                                        call Statup("Emma", "Inbt", 60, 5)   
                                elif E_Legs == "skirt":
                                        call Statup("Emma", "Lust", 60, 5)         
                                        call Statup("Emma", "Obed", 60, 4)            
                                        call Statup("Emma", "Inbt", 60, 4) 
                                        
                                call Remove_Panties("Emma") 
                                

                else:                                   #if she's not in one of your rooms
                    call EmmaFace("sly", 1) 
                    call Statup("Emma", "Lust", 60, 2)         
                    call Statup("Emma", "Obed", 60, 4)            
                    call Statup("Emma", "Inbt", 60, 4)
                    $ E_Loc = "hold"
                    call Set_The_Scene
                    "Emma nods and leaves for a minute." 
                    $ E_DailyActions.append("pantyless")
                    call EmmaOutfit
                    if Taboo:              
                        call Quick_Taboo("Emma")
                    $ E_Loc = bg_current
                    call Set_The_Scene
                    "She returns and quietly hands you her balled up panties."
                                        
            
        else:                                           #She refuses.    
            call EmmaFace("angry", 2)                        
            if not ApprovalCheck("Emma", 500):
                call Statup("Emma", "Lust", 60, 5) 
                call Statup("Emma", "Love", 90, -10)          
                call Statup("Emma", "Obed", 60, 3)            
                call Statup("Emma", "Inbt", 60, 3) 
                ch_e "Out of the question."
                $ E_RecentActions.append("angry")
                $ E_DailyActions.append("angry")   
                
            elif not ApprovalCheck("Emma", 500, TabM = 5):
                call Statup("Emma", "Lust", 60, 5) 
                call Statup("Emma", "Love", 90, -5)          
                call Statup("Emma", "Obed", 60, 5)            
                call Statup("Emma", "Inbt", 60, 5) 
                ch_e "Look around you and have some sense."                                
                $ E_RecentActions.append("angry")
                $ E_DailyActions.append("angry")   
                
            else:
                call EmmaFace("bemused", 2)
                call Statup("Emma", "Lust", 60, 3)            
                call Statup("Emma", "Inbt", 60, 1)
                if Taboo:            
                    call Statup("Emma", "Inbt", 60, 2)
                    if E_Love >= E_Inbt or E_Obed >= E_Inbt:
                        ch_e "You know I would, [E_Petname], but not here."
                    else:       
                        call Statup("Emma", "Obed", 60, -2)    
                        ch_e "Nah, not around here, at least."
                else:
                    if E_Love >= E_Inbt or E_Obed >= E_Inbt:
                        ch_e "You'll have to work up to that, [E_Petname]."
                    else:
                        call EmmaFace("perplexed")       
                        call Statup("Emma", "Obed", 60, -2)    
                        ch_e "I think you'd need to earn that."    
            $ E_Blush = 1
                
    $ Tempmod = Store       
    $ Line = 0
    return

    # End Ask for Panties   //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //

# Emma Control interface ///////////////////
label Emma_Controls:
    menu:
        "I'd like you to call me something else":
            call Emma_Names            
            return
        "I'd like you to come over for some action." if E_Loc != bg_current:
            ch_e "I was already in the neighborhood."
            $ E_Loc = bg_current 
            call Set_The_Scene
            call Emma_SexMenu
            return
        "I'd like to get busy." if E_Loc == bg_current:
            ch_e "I'm sure. . ."
            call Emma_SexMenu
            return
        "I want you to stop taking your own initiative." if "sub" not in E_Traits:
            $ E_Traits.append("sub")
            ch_e "You do enjoy being in control. . ."                
        "Exit.":
            return
    jump Emma_Controls
return

# start Emma_Gifts//////////////////////////////////////////////////////////
label Emma_Gifts:  
    if P_Inventory == []:
        "You don't have anything to give her."
        return
    menu:
        "What would you like to give her?"
        "Toys and books":
            menu:
                "Give her a dildo." if "dildo" in P_Inventory: #If you have a Dildo, you'll give it.
                    $ Count = E_Inventory.count("dildo")
                    if "dildo" not in E_Inventory:                            
                        "You give Emma the dildo."
                        $ E_Blush = 1
                        $ Emma_Arms = 2
                        $ E_Held = "dildo"
                        if ApprovalCheck("Emma", 1000) or ApprovalCheck("Emma", 400, "I"):                    
                            call EmmaFace("bemused")
                            $ P_Inventory.remove("dildo")
                            $ E_Inventory.append("dildo")
                            call Statup("Emma", "Love", 200, 30)
                            call Statup("Emma", "Obed", 200, 30)
                            call Statup("Emma", "Inbt", 200, 30)
                            ch_e "I'm sure I can find some place to store it. . ."
                            call Statup("Emma", "Lust", 89, 10)
                            call Statup("Emma", "Lust", 89, 10)
                        elif ApprovalCheck("Emma", 800) or ApprovalCheck("Emma", 300, "I"):
                            call EmmaFace("confused")
                            $ P_Inventory.remove("dildo")
                            $ E_Inventory.append("dildo")
                            ch_e "This is not an appropriate gift from a student. . ."  
                            call Statup("Emma", "Lust", 89, 5)
                            call Statup("Emma", "Lust", 89, 10)
                            call EmmaFace("sadside",1)
                            ch_e "Hm. . ."
                            call Statup("Emma", "Love", 200, 10)
                            call Statup("Emma", "Obed", 200, 10)
                            call Statup("Emma", "Inbt", 200, 10)
                            call EmmaFace("sly")
                            ch_e "I suppose I can find {i}some{/i} use for it. . ."
                        elif "offered gift" in E_DailyActions:
                            call EmmaFace("angry")
                            "She hands it back to you."
                            ch_e "I think I have made myself clear about inappropriate gifts?"     
                        else:
                            call EmmaFace("angry")
                            call Statup("Emma", "Love", 50, -20)
                            call Statup("Emma", "Obed", 20, 10)
                            call Statup("Emma", "Inbt", 20, 20)                    
                            ch_e "[E_Petname], I don't believe this is an appropriate gift from a student."                     
                            call Statup("Emma", "Lust", 89, 10)
                            "She hands it back to you."
                            $ E_DailyActions.append("offered gift") 
                    elif Count == 1:
                        ch_e "I suppose I always have room for one more. . ."
                    else: 
                        ch_e "How many places do you think I could put these?"
                    $ E_Held = 0
                    $ Emma_Arms = 2
                                        
                "Give her the vibrator." if "vibrator" in P_Inventory: #If you have a vibrator, you'll give it.
                    if "vibrator" not in E_Inventory:                            
                        "You give Emma the Shocker Vibrator."
                        $ E_Blush = 1
                        $ Emma_Arms = 2
                        $ E_Held = "vibrator"
                        if ApprovalCheck("Emma", 700):                    
                            call EmmaFace("bemused")
                            $ P_Inventory.remove("vibrator")
                            $ E_Inventory.append("vibrator")
                            call Statup("Emma", "Love", 200, 30)
                            call Statup("Emma", "Obed", 200, 30)
                            call Statup("Emma", "Inbt", 200, 30)
                            ch_e "How very thoughtful of you. . ."  
                            call Statup("Emma", "Lust", 89, 10)
                            call EmmaFace("sly")
                            ch_e "I'm sure I can put this to good use. . ."
                        elif ApprovalCheck("Emma", 400):
                            call EmmaFace("confused")
                            $ P_Inventory.remove("vibrator")
                            $ E_Inventory.append("vibrator")
                            call Statup("Emma", "Love", 200, 10)
                            call Statup("Emma", "Obed", 200, 10)
                            call Statup("Emma", "Inbt", 200, 10)
                            ch_e "How very thoughtful of you. . ."  
                            call Statup("Emma", "Lust", 89, 10)
                            call EmmaFace("sly")
                            ch_e "a back massager, I assume. . ."
                        elif "offered gift" in E_DailyActions:
                            call EmmaFace("angry")
                            "She hands it back to you."
                            ch_e "I think I have made myself clear about inappropriate gifts?"   
                        else:
                            call EmmaFace("angry")
                            call Statup("Emma", "Love", 50, -20)
                            call Statup("Emma", "Obed", 20, 10)
                            call Statup("Emma", "Inbt", 20, 20)       
                            ch_e "[E_Petname], I don't believe this is an appropriate gift from a student."   
                            call Statup("Emma", "Lust", 89, 5)
                            "She hands it back to you."
                            $ E_DailyActions.append("offered gift") 
                    else: 
                        ch_e "I already have plenty."
                    $ E_Held = 0
                    $ Emma_Arms = 2
                    
                "Give her the \"Dazzler and Longshot\" book." if "Dazzler and Longshot" in P_Inventory: #If you have a vibrator, you'll give it.
                    if "Dazzler and Longshot" not in E_Inventory:                            
                        "You give Emma the book."
                        $ E_Blush = 1
                        if ApprovalCheck("Emma", 600, "L"):                    
                            call EmmaFace("angry")
                            ch_e "Is this the type of thing you expect from me. . ."
                            call EmmaFace("sadside", Mouth="lipbite")
                            ch_e "we'll have to see. . ."
                            call Statup("Emma", "Lust", 89, 10)
                        else:
                            call EmmaFace("angry")
                            ch_e "I don't exactly read this dime store trash. . ."
                            call EmmaFace("sadside", Mouth="lipbite")
                            ch_e "but I will take it. . ."
                        $ P_Inventory.remove("Dazzler and Longshot")
                        $ E_Inventory.append("Dazzler and Longshot") 
                        call Statup("Emma", "Love", 200, 50) 
                    else: 
                        ch_e "You're repeating yourself."                
                    
                "Give her the \"256 Shades of Grey\" book." if "256 Shades of Grey" in P_Inventory: #If you have a book, you'll give it.
                    if "256 Shades of Grey" not in E_Inventory:                            
                        "You give Emma the book."
                        $ E_Blush = 1
                        if ApprovalCheck("Emma", 500, "O"):                    
                            call EmmaFace("bemused")
                            ch_e "I expect it might be somewhat entertaining."
                            call Statup("Emma", "Lust", 89, 10)
                        else:
                            call EmmaFace("confused") 
                            ch_e "I've heard of that one."  
                            call EmmaFace("bemused")             
                        $ P_Inventory.remove("256 Shades of Grey")
                        $ E_Inventory.append("256 Shades of Grey")                    
                        call Statup("Emma", "Obed", 200, 50)  
                    else: 
                        ch_e "You're repeating yourself."                  
                    
                "Give her the \"Avengers Tower Penthouse\" book." if "Avengers Tower Penthouse" in P_Inventory: #If you have a book, you'll give it.
                    if "Avengers Tower Penthouse" not in E_Inventory:                            
                        "You give Emma the book."
                        $ E_Blush = 1
                        if ApprovalCheck("Emma", 500, "I"):                    
                            call EmmaFace("bemused")
                            ch_e "Perhaps don't visit unannounced. . ."
                            call Statup("Emma", "Lust", 89, 10)
                        else:
                            call EmmaFace("sly")
                            ch_e "I normally confiscate such things. . . I'll just do that now. . ."  
                            call EmmaFace("bemused")               
                        $ P_Inventory.remove("Avengers Tower Penthouse")
                        $ E_Inventory.append("Avengers Tower Penthouse")                    
                        call Statup("Emma", "Inbt", 200, 50)  
                    else: 
                        ch_e "You're repeating yourself." 
                "Never mind":
                    pass
        "Clothing":     
            menu:
                "Give her the lace bra." if "e lace bra" in P_Inventory: #If you have a bra, you'll give it.
                    if "lace bra" not in E_Inventory:                            
                        "You give Emma the lace bra."
                        if ApprovalCheck("Emma", 1200):                    
                            call EmmaFace("bemused")
                            $ P_Inventory.remove("e lace bra")
                            $ E_Inventory.append("lace bra")
                            call Statup("Emma", "Love", 200, 25)
                            call Statup("Emma", "Obed", 200, 30)
                            call Statup("Emma", "Inbt", 200, 20)
                            ch_e "I'm impressed, you got the size correct. . ."
                            call Statup("Emma", "Lust", 89, 10)
                        elif ApprovalCheck("Emma", 800):
                            call EmmaFace("confused",1)
                            $ P_Inventory.remove("e lace bra")
                            $ E_Inventory.append("lace bra")
                            call Statup("Emma", "Love", 200, 20)
                            call Statup("Emma", "Obed", 200, 30)
                            call Statup("Emma", "Inbt", 200, 15)
                            ch_e "I'm not exactly running low on this sort of thing. . ."                    
                            call EmmaFace("bemused",1)
                        elif ApprovalCheck("Emma", 600):
                            call EmmaFace("confused")
                            $ P_Inventory.remove("e lace bra")
                            $ E_Inventory.append("lace bra")
                            call Statup("Emma", "Love", 200, 20)
                            call Statup("Emma", "Obed", 200, 20)
                            call Statup("Emma", "Inbt", 200, 25)
                            ch_e "This is an . . . unusual gift from a student. . ."                     
                            call EmmaFace("bemused",1)
                        elif "no gift bra" in E_DailyActions:
                            call EmmaFace("angry")
                            ch_e "This still isn't an appropriate gift from a student."      
                        else:
                            call EmmaFace("angry")
                            call Statup("Emma", "Love", 50, -10)
                            call Statup("Emma", "Obed", 20, 10)
                            call Statup("Emma", "Inbt", 20, 20)  
                            if "no gift panties" in E_DailyActions:                    
                                ch_e "This isn't any better than the last."                       
                            else:                   
                                ch_e "I don't think it's appropriate for you to be so focused on my breasts."                     
                            call Statup("Emma", "Lust", 89, 5)
                            $ E_Blush = 1
                            "She hands it back to you."
                            $ E_RecentActions.append("no gift bra")                      
                            $ E_DailyActions.append("no gift bra") 
                    else: 
                        ch_e "I already have one of those."                
                    
                "Give her the lace panties." if "e lace panties" in P_Inventory: #If you have a bra, you'll give it.
                    if "lace panties" not in E_Inventory:                            
                        "You give Emma the lace panties."
                        if ApprovalCheck("Emma", 900):
                            call EmmaFace("confused",1)
                            $ P_Inventory.remove("e lace panties")
                            $ E_Inventory.append("lace panties")
                            call Statup("Emma", "Love", 200, 20)
                            call Statup("Emma", "Obed", 200, 25)
                            call Statup("Emma", "Inbt", 200, 20)
                            ch_e "Not entirely out of place in my wardrobe. . ."                  
                            call EmmaFace("bemused",1)
                        elif ApprovalCheck("Emma", 700):
                            call EmmaFace("confused")
                            $ P_Inventory.remove("e lace panties")
                            $ E_Inventory.append("lace panties")
                            call Statup("Emma", "Love", 200, 20)
                            call Statup("Emma", "Obed", 200, 20)
                            call Statup("Emma", "Inbt", 200, 25)
                            ch_e "This is an. . . unsual gift."                  
                            call EmmaFace("sly",1)
                            ch_e "But I'll hold on to them. . ." 
                        elif "no gift panties" in E_DailyActions:
                            call EmmaFace("angry")
                            ch_e "I don't recommend trying again any time soon."                      
                        else:
                            call EmmaFace("angry")
                            call Statup("Emma", "Love", 50, -15)
                            call Statup("Emma", "Obed", 20, 10)
                            call Statup("Emma", "Inbt", 20, 20)
                            if "no gift bra" in E_DailyActions:                    
                                ch_e "These aren't appropriate either." 
                            elif E_SeenPanties:
                                ch_e "Just because you've seen my panties doesn't mean you get to pick them out."                          
                            else:
                                ch_e "I don't believe these are appropriate thoughts for you to be having."                     
                            call Statup("Emma", "Lust", 89, 5)
                            "She hands them back to you."
                            $ E_RecentActions.append("no gift panties")                      
                            $ E_DailyActions.append("no gift panties") 
                    else: 
                        ch_e "I already have one of those."                
                   
                "Give her the stockings and garterbelt." if "e stockings and garterbelt" in P_Inventory: 
                    #If you have a stockings, you'll give it.
                    if "stockings and garterbelt" not in E_Inventory:                            
                        "You give Emma the stockings."
                        call EmmaFace("bemused")
                        $ P_Inventory.remove("e stockings and garterbelt")
                        $ E_Inventory.append("stockings and garterbelt")
                        call Statup("Emma", "Love", 200, 5)
                        call Statup("Emma", "Obed", 200, 5)
                        call Statup("Emma", "Inbt", 200, 5)
                        ch_e "These are lovely. . ."
                        call Statup("Emma", "Lust", 89, 3)
                    else: 
                        ch_e "I already have those."  
                        
                "Give her the pantyhose." if "e pantyhose" in P_Inventory: 
                    #If you have a stockings, you'll give it.
                    if "pantyhose" not in E_Inventory:                            
                        "You give Emma the pantyhose."
                        call EmmaFace("bemused")
                        $ P_Inventory.remove("e pantyhose")
                        $ E_Inventory.append("pantyhose")
                        call Statup("Emma", "Love", 200, 5)
                        call Statup("Emma", "Obed", 200, 5)
                        call Statup("Emma", "Inbt", 200, 5)
                        ch_e "These are lovely. . ."
                    else: 
                        ch_e "I already have those."  
                        
                "Give her the bikini top." if "e bikini top" in P_Inventory: 
                    #If you have a bra, you'll give it.
                    if "bikini top" not in E_Inventory:                            
                        "You give Emma the bikini top."
                        $ E_Blush = 1
                        if ApprovalCheck("Emma", 1200):                    
                            call EmmaFace("bemused")
                            $ P_Inventory.remove("e bikini top")
                            $ E_Inventory.append("bikini top")
                            call Statup("Emma", "Love", 200, 20)
                            call Statup("Emma", "Obed", 200, 10)
                            call Statup("Emma", "Inbt", 200, 10)
                            ch_e "This does show off my assets, doesn't it. . ."
                        elif ApprovalCheck("Emma", 900):
                            call EmmaFace("confused",1)
                            $ P_Inventory.remove("e bikini top")
                            $ E_Inventory.append("bikini top")
                            call Statup("Emma", "Love", 200, 20)
                            call Statup("Emma", "Obed", 200, 10)
                            call Statup("Emma", "Inbt", 200, 5)
                            ch_e "This is my style. . ."                  
                            call EmmaFace("bemused",1)
                        elif ApprovalCheck("Emma", 700):
                            call EmmaFace("confused",2)
                            $ P_Inventory.remove("e bikini top")
                            $ E_Inventory.append("bikini top")
                            call Statup("Emma", "Love", 200, 10)
                            call Statup("Emma", "Obed", 200, 5)
                            call Statup("Emma", "Inbt", 200, 5)
                            ch_e "An interesting. . . gift. . ."                  
                            call EmmaFace("bemused",1)
                        elif "no gift bra" in E_RecentActions:
                            call EmmaFace("angry",2)
                            ch_e "I don't want this either."  
                        elif "no gift bra" in E_DailyActions:
                            call EmmaFace("angry",2)
                            ch_e "I don't recommend trying again any time soon."                    
                        else:
                            call EmmaFace("angry",2)
                            call Statup("Emma", "Love", 50, -5)
                            call Statup("Emma", "Obed", 20, 5)
                            call Statup("Emma", "Inbt", 20, 10)
                            if "no gift bra " in E_DailyActions:                    
                                ch_e "I don't want this either!"                      
                            else:
                                ch_e "I don't think my swimwear is any concern of yours."    
                            $ E_Blush = 1
                            "She hands it back to you."
                            $ E_RecentActions.append("no gift bra")                      
                            $ E_DailyActions.append("no gift bra") 
                    else: 
                        ch_e "I already have one of those."
                        
               
                "Give her the bikini bottoms." if "e bikini bottoms" in P_Inventory: 
                    #If you have a bra, you'll give it.
                    if "bikini bottoms" not in E_Inventory:                            
                        "You give Emma the bikini bottoms."
                        $ E_Blush = 1
                        if ApprovalCheck("Emma", 1200):                    
                            call EmmaFace("bemused")
                            $ P_Inventory.remove("e bikini bottoms")
                            $ E_Inventory.append("bikini bottoms")
                            call Statup("Emma", "Love", 200, 20)
                            call Statup("Emma", "Obed", 200, 10)
                            call Statup("Emma", "Inbt", 200, 10)
                            ch_e "These are quite stylish. . ."
                        elif ApprovalCheck("Emma", 900):
                            call EmmaFace("confused",1)
                            $ P_Inventory.remove("e bikini bottoms")
                            $ E_Inventory.append("bikini bottoms")
                            call Statup("Emma", "Love", 200, 20)
                            call Statup("Emma", "Obed", 200, 10)
                            call Statup("Emma", "Inbt", 200, 5)
                            ch_e "Rather daring. . ."                  
                            call EmmaFace("bemused",1)
                        elif ApprovalCheck("Emma", 700):
                            call EmmaFace("confused",2)
                            $ P_Inventory.remove("e bikini bottoms")
                            $ E_Inventory.append("bikini bottoms")
                            call Statup("Emma", "Love", 200, 10)
                            call Statup("Emma", "Obed", 200, 5)
                            call Statup("Emma", "Inbt", 200, 5)
                            ch_e "I don't know that a student should be buying me swimwear. . ."                  
                            call EmmaFace("bemused",1)
                        elif "no gift panties" in E_RecentActions:
                            call EmmaFace("angry",2)
                            ch_e "I don't want these either."  
                        elif "no gift panties" in E_DailyActions:
                            call EmmaFace("angry",2)
                            ch_e "I don't recommend trying again any time soon."                   
                        else:
                            call EmmaFace("angry",2)
                            call Statup("Emma", "Love", 50, -5)
                            call Statup("Emma", "Obed", 20, 5)
                            call Statup("Emma", "Inbt", 20, 10)
                            if "no gift bra" in E_DailyActions:                    
                                ch_e "I don't want these either!"                      
                            else:
                                ch_e "I don't think my swimwear is any concern of yours."   
                            $ E_Blush = 1
                            "She hands them back to you."
                            $ E_RecentActions.append("no gift panties")                      
                            $ E_DailyActions.append("no gift panties") 
                    else: 
                        ch_e "I already have one of those."
                "Never mind":
                    pass
        "Exit":
            pass
    
    return


# start Emma_Names//////////////////////////////////////////////////////////
label Emma_Names(TempName=0):    
    call LastNamer
    $ TempName = _return
    menu:
        ch_e "Oh? What would you like me to call you?"
        "[TempName]'s fine.":
            # ie "Mr. Zero"
            $ E_Petname = TempName
            ch_e "I assumed it was, [E_Petname]."
        "Call me by my name.":
            $ E_Petname = Playername            
            ch_e "If you'd rather, [E_Petname]."
        "Call me \"dear\"." if "dear" in E_Petnames:
            $ E_Petname = "dear"
            ch_e "Certainly, [E_Petname]."
        "Call me \"darling\"." if "darling" in E_Petnames:
            $ E_Petname = "darling"
            ch_e "Certainly, [E_Petname]."
        "Call me \"boyfriend\"." if "boyfriend" in E_Petnames:
            $ E_Petname = "boyfriend"
            ch_e "How pedestrian, but fine, [E_Petname]."
        "Call me \"lover\"." if "lover" in E_Petnames:
            $ E_Petname = "lover"
            ch_e "Certainly, [E_Petname]."
        "Call me \"sir\"." if "sir" in E_Petnames:
            $ E_Petname = "sir"
            ch_e "Yes, [E_Petname]."
        "Call me \"master\"." if "master" in E_Petnames:
            $ E_Petname = "master"
            ch_e "As you wish, [E_Petname]."
        "Call me \"sex friend\"." if "sex friend" in E_Petnames:
            $ E_Petname = "sex friend"
            ch_e "You naughty boy. Very well, [E_Petname]."
        "Call me \"fuck buddy\"." if "fuck buddy" in E_Petnames:
            $ E_Petname = "fuck buddy"
            ch_e "How nasty, \"[E_Petname]\"."        
        "Call me \"daddy\"." if "daddy" in E_Petnames:
            $ E_Petname = "daddy"
            ch_e "Mmm, ok, [E_Petname]."
        "Nevermind.":
            return
    return
# end Emma_Names//////////////////////////////////////////////////////////

label Emma_Pet:
    while 1:
        menu:
            extend ""
            "Polite":
                menu:
                    extend ""
                    "I think I'll just call you Ms. Frost.":
                        $ E_Pet = "Ms. Frost"            
                        $ EmmaName = "Ms. Frost"
                        ch_e "I don't see why not, [E_Petname]."
                        
                    "I think I'll just call you Emma.":
                        if ApprovalCheck("Emma", 700) or "classcaught" in E_History:
                            ch_e "I don't see why not, [E_Petname]."   
                            $ E_Pet = "Emma"            
                            $ EmmaName = "Emma"
                        else:
                            ch_e "I'd rather you didn't, [E_Petname]."
                        
                    "I think I'll call you \"girl\".":
                        $ E_Pet = "girl"
                        if "boyfriend" in E_Petnames or ApprovalCheck("Emma", 600, "L"):
                            call EmmaFace("sexy", 1) 
                            ch_e "How droll, [E_Petname]."
                        else:      
                            call EmmaFace("angry")           
                            ch_e "I wouldn't, [E_Petname]." 
                            
                    "I think I'll call you \"boo\".":
                        $ E_Pet = "boo"
                        if "boyfriend" in E_Petnames or ApprovalCheck("Emma", 800, "L"):
                            call EmmaFace("bemused", 1) 
                            ch_e "How adorable, [E_Petname]."
                        else:     
                            call EmmaFace("angry")            
                            ch_e "I'm no such thing,  [E_Petname]."
                            
                    "I think I'll call you \"bae\".":
                        $ E_Pet = "bae"
                        if "boyfriend" in E_Petnames or ApprovalCheck("Emma", 800, "L"):
                            call EmmaFace("sexy", 1) 
                            ch_e "I suppose I am your. . . \"bae?\""
                        else:     
                            call EmmaFace("angry")            
                            ch_e "What does that even mean?."
                            
                    "I think I'll call you \"baby\".":
                        $ E_Pet = "baby"
                        if "boyfriend" in E_Petnames or ApprovalCheck("Emma", 500, "L"):
                            call EmmaFace("sexy", 1) 
                            ch_e "How precious."
                        else:     
                            call EmmaFace("angry")            
                            ch_e "I think I'm a bit. . . mature for that." 
                            
                    "I think I'll call you \"darling\".":
                        $ E_Pet = "darling"
                        if "boyfriend" in E_Petnames or ApprovalCheck("Emma", 600, "L"):
                            ch_e "I do adore you, [E_Petname]."
                        else:     
                            call EmmaFace("angry", 1)            
                            ch_e "A bit premature, [E_Petname]."
                            
                    "I think I'll call you \"sweetie\".":
                        $ E_Pet = "sweetie"
                        if "boyfriend" in E_Petnames or ApprovalCheck("Emma", 500, "L"):
                            ch_e "Really, [E_Petname]?"
                        else:     
                            call EmmaFace("angry", 1)            
                            ch_e "Too saccharine, [E_Petname]."
                            
                    "I think I'll call you \"sexy\".":
                        $ E_Pet = "sexy"
                        if "lover" in E_Petnames or ApprovalCheck("Emma", 900):
                            call EmmaFace("sexy", 1) 
                            ch_e "I can't argue there, [E_Petname]."
                        else:        
                            call EmmaFace("angry", 1)         
                            ch_e "That may be a bit much, [E_Petname]."  
                            
                    "I think I'll call you \"lover\".":
                        $ E_Pet = "lover"
                        if "lover" in E_Petnames or ApprovalCheck("Emma", 900, "L"):
                            call EmmaFace("sexy", 1) 
                            ch_e "I do love you, [E_Petname]!"
                        else:      
                            call EmmaFace("angry", 1)           
                            ch_e "Not in this lifetime, [E_Petname]."  
                        
                    "Back":
                        pass
            
            "Risky":
                menu:                        
                    "I think I'll call you \"slave\".":
                        $ E_Pet = "slave"
                        if "master" in E_Petnames or ApprovalCheck("Emma", 900, "O"):
                            call EmmaFace("bemused", 1) 
                            ch_e "As you wish, [E_Petname]."
                        else:      
                            call EmmaFace("angry", 1)           
                            ch_e "I'm no man's slave, [E_Petname]."
                                            
                    "I think I'll call you \"pet\".":
                        $ E_Pet = "pet"
                        if "master" in E_Petnames or ApprovalCheck("Emma", 600, "O"):
                            call EmmaFace("bemused", 1) 
                            ch_e "So long as you make sure to pet me, [E_Petname]."
                        else:             
                            call EmmaFace("angry", 1)    
                            ch_e "I doubt you'd want me for a pet, [E_Petname]."
                            
                    "I think I'll call you \"slut\".":
                        $ E_Pet = "slut"
                        if "sex friend" in E_Petnames or ApprovalCheck("Emma", 1000, "OI"):
                            call EmmaFace("sexy") 
                            ch_e "I cant exactly disagree, [E_Petname]."
                        else:                
                            call EmmaFace("angry", 1) 
                            $ E_Mouth = "surprised"
                            ch_e "I would strongly reconsider that." 
                            
                    "I think I'll call you \"whore\".":
                        $ E_Pet = "whore"
                        if "fuckbuddy" in E_Petnames or ApprovalCheck("Emma", 1100, "OI"):
                            call EmmaFace("sly") 
                            ch_e "Only for you though. . ."
                        else:        
                            call EmmaFace("angry", 1)         
                            ch_e "The last man to call me that no longer remembers his own name." 
                                                   
                    "I think I'll call you \"sugartits\".":
                        $ E_Pet = "sugartits"
                        if "sex friend" in E_Petnames or ApprovalCheck("Emma", 1400):
                            call EmmaFace("sly", 1) 
                            ch_e "They certainly are sweet. . ."
                        else:     
                            call EmmaFace("angry", 1)            
                            ch_e "I expect you're better than that, [E_Petname]." 
                            
                    "I think I'll call you \"sex friend\".":
                        $ E_Pet = "sex friend"
                        if "sex friend" in E_Petnames or ApprovalCheck("Emma", 600, "I"):
                            call EmmaFace("sly") 
                            ch_e "Hm?"
                        else:                
                            call EmmaFace("angry", 1) 
                            ch_e "Hopefully not in public, [E_Petname]." 
                            
                    "I think I'll call you \"fuckbuddy\".":
                        $ E_Pet = "fuckbuddy"
                        if "fuckbuddy" in E_Petnames or ApprovalCheck("Emma", 700, "I"):
                            call EmmaFace("bemused") 
                            ch_e "Well. . . alright."
                        else:                
                            call EmmaFace("angry", 1)
                            $ E_Mouth = "surprised"
                            ch_e "How crass." 
                        
                    "I think I'll call you \"baby girl\".":
                        $ E_Pet = "baby girl"
                        if "daddy" in E_Petnames or ApprovalCheck("Emma", 1200):
                            call EmmaFace("smile", 1) 
                            ch_e "Adorable."
                        else:                
                            call EmmaFace("angry", 1) 
                            ch_e "A bit inappropriate." 
                    
                    "I think I'll call you \"mommy\".":
                        $ E_Pet = "mommy"
                        if "mommy" in E_Pets or ApprovalCheck("Emma", 1500):
                            call EmmaFace("sly", 1, Mouth="kiss") 
                            ch_e "Oooh, [E_Petname]."
                        else:     
                            call EmmaFace("angry")            
                            ch_e "That's a bit much, [E_Petname]" 
                            
                    "Back":
                        pass
                    
            "Nevermind.":
                return
    return
    
label Emma_Namecheck(E_Pet = E_Pet, Cnt = 0, Ugh = 0):#E_Pet is the internal pet name, Cnt and Ugh are internal count variable
    if E_Pet == "Emma":
        return Ugh   
    if E_Pet == "Ms. Frost":
        return Ugh   
    if Taboo:
        $ Cnt = int(Taboo/10)
    if E_Pet == "girl":                                         #easy options
        if ApprovalCheck("Emma", 500, "L", TabM=1):            
            call Statup("Emma", "Love", 80, 1)
        else:
            call Statup("Emma", "Love", 50, -1)
            $ Ugh = 1
    elif E_Pet == "boo" or E_Pet == "bae":
        if ApprovalCheck("Emma", 500, "L", TabM=1):
            call Statup("Emma", "Love", 80, 1)
        else:
            call Statup("Emma", "Love", 50, -2)
            $ Ugh = 1
    elif E_Pet == "baby":    
        if ApprovalCheck("Emma", 500, "L", TabM=1):
            call Statup("Emma", "Love", 90, 1)
        else:
            call Statup("Emma", "Love", 30, -1)
            $ Ugh = 1
    elif E_Pet == "darling":
        if ApprovalCheck("Emma", 600, "L", TabM=1):
            call Statup("Emma", "Love", 80, 2)
        else:
            call Statup("Emma", "Love", 50, -1)
            $ Ugh = 1
    elif E_Pet == "sweetie":
        if not ApprovalCheck("Emma", 500, "L", TabM=1):
            call Statup("Emma", "Love", 80, 1)  
        else:
            call Statup("Emma", "Love", 40, -1)
            $ Ugh = 1
            
    elif E_Pet == "sexy" or E_Pet == "lover":
        if ApprovalCheck("Emma", 900, TabM=1):                                                        #over 150
            call Statup("Emma", "Love", 80, 2)
            call Statup("Emma", "Obed", 80, 1)
            call Statup("Emma", "Inbt", 70, 1) 
        else:                                                            
            call Statup("Emma", "Love", 50, (-1-Cnt))
            call Statup("Emma", "Obed", 50, 1)
            call Statup("Emma", "Inbt", 20, -1)
            $ Ugh = 1
            
    elif E_Pet == "slave":                                        #tougher options
        if ApprovalCheck("Emma", 900, "O", TabM=3):                                            #over 80
            call Statup("Emma", "Lust", 90, (3+Cnt))
            call Statup("Emma", "Obed", 95, (2+Cnt))
            call Statup("Emma", "Inbt", 30, 1)
            call Statup("Emma", "Inbt", 70, 1)     
        elif ApprovalCheck("Emma", 600, "O", TabM=3):                                                  #between 50 and 80
            call Statup("Emma", "Lust", 90, 1)
            call Statup("Emma", "Love", 200, -1)
            call Statup("Emma", "Obed", 81, 2)
            call Statup("Emma", "Inbt", 70, 1)        
        else:                                                                                           # under 50
            call Statup("Emma", "Love", 200, -2)
            call Statup("Emma", "Love", 50, -1, 1)
            call Statup("Emma", "Obed", 50, 1)
            call Statup("Emma", "Inbt", 50, -1)
            $ Ugh = 1
    
    elif E_Pet == "pet":                                        #tougher options
        if ApprovalCheck("Emma", 1500, TabM=2):                                            #over 150
            call Statup("Emma", "Lust", 90, (3+Cnt))
            call Statup("Emma", "Obed", 95, (2+Cnt))
            call Statup("Emma", "Inbt", 30, 1)
            call Statup("Emma", "Inbt", 70, 1)     
        elif ApprovalCheck("Emma", 1200, TabM=2):                                                  #between 120 and 150
            call Statup("Emma", "Lust", 60, 1)
            call Statup("Emma", "Obed", 81, 2)
            call Statup("Emma", "Inbt", 70, 1)        
        else:                                                                                           # under 120
            call Statup("Emma", "Love", 200, -2)
            call Statup("Emma", "Love", 50, -1, 1)
            call Statup("Emma", "Obed", 50, 1)
            call Statup("Emma", "Inbt", 50, -1)
            $ Ugh = 1
            
    elif E_Pet == "slut":
        if ApprovalCheck("Emma", 500, "O", TabM=2) or ApprovalCheck("Emma", 500, "I", TabM=2):        #over 50
            call Statup("Emma", "Lust", 90, (4+Cnt))
            call Statup("Emma", "Obed", 95, (2+Cnt))
            call Statup("Emma", "Inbt", 40, 2)
            call Statup("Emma", "Inbt", 80, 1)
        elif ApprovalCheck("Emma", 300, "O", TabM=2) or ApprovalCheck("Emma", 300, "I", TabM=2):      #between 30 and 50
            call Statup("Emma", "Lust", 90, 1)
            call Statup("Emma", "Love", 200, (-1-Cnt))
            call Statup("Emma", "Obed", 80, (2+Cnt))
            call Statup("Emma", "Inbt", 70, 1)        
        else:                                                                                           # under 40
            call Statup("Emma", "Love", 200, (-2-Cnt))
            call Statup("Emma", "Love", 50, (-1-Cnt), 1)
            call Statup("Emma", "Obed", 50, 1)
            call Statup("Emma", "Inbt", 20, -1)
            $ Ugh = 1
            
    elif E_Pet == "whore":
        if ApprovalCheck("Emma", 700, "O", TabM=2) or ApprovalCheck("Emma", 600, "I", TabM=2):        #over 60
            call Statup("Emma", "Lust", 90, 4)
            call Statup("Emma", "Obed", 95, 2)
            call Statup("Emma", "Inbt", 50, 2)
            call Statup("Emma", "Inbt", 80, 1)
        elif ApprovalCheck("Emma", 500, "O", TabM=2) or ApprovalCheck("Emma", 400, "I", TabM=2):      #between 40 and 60
            call Statup("Emma", "Lust", 90, 1)
            call Statup("Emma", "Love", 200, (-2-Cnt))
            call Statup("Emma", "Obed", 80, 2)
            call Statup("Emma", "Inbt", 70, 1)
        else:                                                                                           # under 40
            call Statup("Emma", "Love", 200, (-3-Cnt))
            call Statup("Emma", "Love", 50, (-2-Cnt), 1)
            call Statup("Emma", "Obed", 50, 1)            
            call Statup("Emma", "Inbt", 21, 1, 1)
            call Statup("Emma", "Inbt", 20, -1)
            $ Ugh = 1
            
    elif E_Pet == "sugartits":
        if ApprovalCheck("Emma", 1500, TabM=1):                                                        #over 150
            call Statup("Emma", "Obed", 80, 1)
            call Statup("Emma", "Obed", 50, 2)
            call Statup("Emma", "Inbt", 70, 1)            
            call Statup("Emma", "Inbt", 30, 2)
        else:                                                                       
            call Statup("Emma", "Love", 200, (-2-Cnt))
            call Statup("Emma", "Love", 50, (-1-Cnt))
            call Statup("Emma", "Obed", 50, 1)
            call Statup("Emma", "Inbt", 20, -1)
            $ Ugh = 1
            
    elif E_Pet == "sex friend":    
        if ApprovalCheck("Emma", 750, "O", TabM=1) or ApprovalCheck("Emma", 600, "I", TabM=1):        #over 75/60
            call Statup("Emma", "Lust", 90, 3)
            call Statup("Emma", "Obed", 95, 2)
            call Statup("Emma", "Inbt", 40, 2)
            call Statup("Emma", "Inbt", 80, 1)
        elif ApprovalCheck("Emma", 600, "O", TabM=1) or ApprovalCheck("Emma", 400, "I", TabM=1):      #between 60/40 and 75/60
            call Statup("Emma", "Lust", 90, 2)
            call Statup("Emma", "Love", 200, (-1-Cnt))
            call Statup("Emma", "Obed", 80, 1)
            call Statup("Emma", "Inbt", 70, 1)
            $ E_Blush = 1
        else:                                                                                           # under 60/40
            call Statup("Emma", "Love", 200, -Cnt)
            call Statup("Emma", "Love", 50, (-1-Cnt), 1)
            call Statup("Emma", "Obed", 50, 1)
            call Statup("Emma", "Inbt", 20, -1)
            $ Ugh = 1
            
    elif E_Pet == "fuckbuddy":
        if ApprovalCheck("Emma", 700, "O", TabM=2) or ApprovalCheck("Emma", 700, "I", TabM=1):        #over 70/70
            call Statup("Emma", "Lust", 90, 3)
            call Statup("Emma", "Obed", 95, 2)
            call Statup("Emma", "Inbt", 40, 2)
            call Statup("Emma", "Inbt", 85, 1)
        elif ApprovalCheck("Emma", 600, "O", TabM=2) or ApprovalCheck("Emma", 500, "I", TabM=1):      #between 60/50 and 70/70
            call Statup("Emma", "Lust", 90, 2)
            call Statup("Emma", "Love", 200, (-1-Cnt))
            call Statup("Emma", "Obed", 80, 1)
            call Statup("Emma", "Inbt", 70, 1)
            $ E_Blush = 1
        else:                                                                                           #under 60/50
            call Statup("Emma", "Love", 200, -Cnt)
            call Statup("Emma", "Love", 60, (-2-Cnt), 1)
            call Statup("Emma", "Obed", 60, 1)
            call Statup("Emma", "Inbt", 20, -1)
            $ Ugh = 1
            
    elif E_Pet == "baby girl" or E_Pet == "mommy":
        if ApprovalCheck("Emma", 1200, TabM=1):                                                        #over 150
            call Statup("Emma", "Obed", 80, 1)
            call Statup("Emma", "Obed", 50, 2)
            call Statup("Emma", "Inbt", 70, 1)            
            call Statup("Emma", "Inbt", 30, 2)
        else:                                                                       
            call Statup("Emma", "Love", 200, (-2-Cnt))
            call Statup("Emma", "Love", 50, (-1-Cnt))
            call Statup("Emma", "Obed", 50, 1)
            call Statup("Emma", "Inbt", 20, -1)
            $ Ugh = 1
    return Ugh


# start Emma_Personality//////////////////////////////////////////////////////////
label Emma_Personality(Cnt = 0):   
    if not E_Chat[4] or Cnt:
        "Since you're doing well in one area, you can convince Emma to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_e "Sure, what's up?"
        "More Obedient. [[Love to Obedience]" if E_Love > 900:
            ch_p "If you really love me, could you please just do what I say?"
            ch_e "Anything to humor you, [E_Petname]."
            $ E_Chat[4] = 1
        "Less Inhibited. [[Love to Inhibition]" if E_Love > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_e "I don't see how I could be {i}less{/i} inhibited, but I can certainly try."
            $ E_Chat[4] = 2
        
        "Less Inhibited. [[Obedience to Inhibition]" if E_Obed > 900:
            ch_p "I want you to be less inhibited."
            ch_e "If you say so."
            $ E_Chat[4] = 3
        "More Loving. [[Obedience to Love]" if E_Obed > 900:
            ch_p "I'd like you to learn to love me."
            ch_e "I'll try to."
            $ E_Chat[4] = 4
            
        "More Obedient. [[Inhibition to Obedience]" if E_Inbt > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_e "Does that get you off?"
            $ E_Chat[4] = 5
            
        "More Loving. [[Inhibition to Love]" if E_Inbt > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_e "We do have fun. . ."
            $ E_Chat[4] = 6
            
        "I guess just do what you like. . .[[reset]" if E_Chat[4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_e "As if I ever do anything else?"
            $ E_Chat[4] = 0
        "Repeat the rules":
            $ Cnt = 1
            jump Emma_Personality
        "Nevermind.":
            return
    return
# end Emma_Personality//////////////////////////////////////////////////////////




# Emma_Summon//////////////////////////////////////////////////////////

label Emma_Summon(Tempmod=Tempmod):
    call EmmaOutfit  
    if "no summon" in E_RecentActions:
                if "angry" in E_RecentActions:
                    ch_e "I'm not in the mood for this, [E_Petname]."
                elif Action_Check("Emma", "recent", "no summon") > 1:
                    ch_e "You heard me the first time."
                    $ E_RecentActions.append("angry") 
                elif Current_Time == "Night": 
                    ch_e "It's past your bedtime."
                else:
                    ch_e "As I said, I've got things to do."   
                $ E_RecentActions.append("no summon")
                return
                              
    if Current_Time == "Night": 
                if ApprovalCheck("Emma", 700, "L") or ApprovalCheck("Emma", 300, "O"):                              
                        #It's night time but she likes you.
                        ch_e "It's getting late, but fine, what did you want?"
                        $ E_Loc = bg_current 
                        call Set_The_Scene
                else:                                                           
                        #It's night time and she isn't into you
                        ch_e "It's late, [E_Petname], tell me tomorrow."       
                        $ E_RecentActions.append("no summon")         
                return
                
    $ D20 = renpy.random.randint(1, 20) 
    $ Line = 0
    if E_Loc == "bg teacher": #fix change these if changed function
        $ Tempmod = -30
    elif E_Loc == "bg classroom":
        $ Tempmod = 10
    elif E_Loc == "bg dangerroom":    
        $ Tempmod = 10
    elif E_Loc == "bg showerroom":    
        $ Tempmod = 30
        
    if D20 <= 3:                                                                        
        #unlucky refusal
        $ Line = "no"       
    elif not ApprovalCheck("Emma", 700, "L") or not ApprovalCheck("Emma", 600, "O"):                       
        #It's not night time, but she's busy 
        if not ApprovalCheck("Emma", 300):
                ch_e "I don't really feel up to that, [E_Petname]."       
                $ E_RecentActions.append("no summon")         
                return    
            
            
        if "summoned" in E_RecentActions:
                pass
        elif "goto" in E_RecentActions:
                ch_e "You only just left, why not return?"
        elif E_Loc == "bg classroom" or E_Loc == "bg teacher":
                ch_e "You can find me in the class room, [E_Petname]."
        elif E_Loc == "bg dangerroom": 
                ch_e "I'm getting some training in, [E_Petname], care to join me?"    
        elif E_Loc == "bg campus": 
                ch_e "I'm relaxing in the square, if you'd care to join me." 
        elif E_Loc == "bg emma": 
                ch_e "I'm in my room, [E_Petname]." 
        elif E_Loc == "bg player": 
                ch_e "I'm waiting in your room, [E_Petname]. . ."   
        elif E_Loc == "bg showerroom":    
            if ApprovalCheck("Emma", 1600):
                ch_e "I'm in the shower right now, [E_Petname], do you need an invitation?"
            else:            
                ch_e "I'm in the shower right now, [E_Petname], perhaps I'll see you later."       
                $ E_RecentActions.append("no summon")         
                return      
        elif E_Loc == "hold":
                ch_e "I'm off campus for a bit, I'll be back later."       
                $ E_RecentActions.append("no summon") 
                return      
        else:        
                ch_e "You could always come over here, [E_Petname]."    
           
           
        if "summoned" in E_RecentActions:
            ch_e "Again? Very well."           
            $ Line = "yes"            
        elif "goto" in E_RecentActions:
            menu:
                extend ""
                "You're right, be right back.":
                                ch_e "I'll be waiting."
                                $ Line = "go to"                    
                "Nah, it's better here.":    
                                ch_e "Very well."                    
                "But I'd {i}really{/i} like to see you over here.":
                        if ApprovalCheck("Emma", 600, "L") or ApprovalCheck("Emma", 1400):
                                $ Line = "lonely"
                        else: 
                                $ Line = "no"                        
                "I said come over here.":
                        if ApprovalCheck("Emma", 600, "O"):                                    
                                #she is obedient
                                $ Line = "command"                        
                        elif D20 >= 7 and ApprovalCheck("Emma", 1400):                         
                                #she is generally favorable 
                                ch_e "Hmm, very well."              
                                $ Line = "yes"                        
                        elif ApprovalCheck("Emma", 200, "O"):                                  
                                #she is not obedient  
                                ch_e "If you're lucky, I'll still be here when you arrive."    
                        else:                                                                   
                                #she is obedient, but you failed to meet the checks                     
                                $ Line = "no" 
        else:  
            menu:
                extend ""
                "Sure, I'll be right there.":
                    call Statup("Emma", "Love", 55, 1) 
                    call Statup("Emma", "Inbt", 30, 1)
                    ch_e "I'll be waiting."
                    $ Line = "go to"
                    
                "Nah, we can talk later.":
                    call Statup("Emma", "Obed", 50, 1)                            
                    call Statup("Emma", "Obed", 30, 2)
                    ch_e "Very well."
                    
                "Could you please come visit me? I'm lonely.":
                    if ApprovalCheck("Emma", 600, "L") or ApprovalCheck("Emma", 1400):
                        call Statup("Emma", "Love", 70, 1)                   
                        call Statup("Emma", "Obed", 50, 1)
                        $ Line = "lonely"
                    else: 
                        call Statup("Emma", "Inbt", 30, 1)
                        $ Line = "no"
                        
                "I said come over here.":
                    if ApprovalCheck("Emma", 600, "O"):                              
                        #she is obedient
                        call Statup("Emma", "Love", 50, 1, 1)    
                        call Statup("Emma", "Love", 40, -1)                
                        call Statup("Emma", "Obed", 90, 1)    
                        $ Line = "command"
                        
                    elif D20 >= 7 and ApprovalCheck("Emma", 1400):       
                        #she is generally favorable
                        call Statup("Emma", "Love", 70, -2)  
                        call Statup("Emma", "Love", 90, -1)  
                        call Statup("Emma", "Obed", 50, 2)                                
                        call Statup("Emma", "Obed", 90, 1)  
                        ch_e "Ok, fine, [E_Petname]."              
                        $ Line = "yes"
                        
                    elif ApprovalCheck("Emma", 200, "O"):                                         
                        #she is not obedient   
                        call Statup("Emma", "Love", 70, -4)  
                        call Statup("Emma", "Love", 90, -2)   
                        ch_e "Who do you think is in charge here?!"                             
                        call Statup("Emma", "Inbt", 40, 2)
                        call Statup("Emma", "Inbt", 60, 1)    
                        call Statup("Emma", "Obed", 70, -2)
                        ch_e "You'd better hope you don't find me here."                    
                    else:                                                                   
                        #she is obedient, but you failed to meet the checks
                        call Statup("Emma", "Inbt", 30, 1)
                        call Statup("Emma", "Inbt", 50, 1)                                    
                        call Statup("Emma", "Love", 50, -1, 1)
                        call Statup("Emma", "Obed", 70, -1)  
                        $ Line = "no" 
                    #end "ordered"
    else:                                                                               
        #automatic acceptance
        if E_Love > E_Obed:
            ch_e "I'd love to."
        else:
            ch_e "I'll be right there, [E_Petname]."
        $ Line = "yes" 
        
    if not Line:                                                                        
            #You end the dialog neutrally               
            $ E_RecentActions.append("no summon")         
            return
        
    if Line == "no":                                                                    
            # She's refused, context based dialog
            if E_Loc == "bg teacher":
                ch_e "I can't exactly leave class, [E_Petname]." 
            elif E_Loc == "bg classroom":
                ch_e "I have a lot of paperwork, [E_Petname]." 
            elif E_Loc == "bg dangerroom": 
                ch_e "I'm just getting warmed up here."
            else:
                ch_e "I have a lot to finish up here."          
            $ E_RecentActions.append("no summon")         
            return
        
    elif Line == "go to":                                                                 
            #You agreed to go to her instead        
            $ renpy.pop_call()
            $ Tempmod = 0
            $ E_RecentActions.append("goto")  
            $ P_RecentActions.append("goto")  
            if E_Loc == "bg classroom" or E_Loc == "bg teacher":
                    ch_e "You don't want to miss too much."
                    jump Class_Room 
            elif E_Loc == "bg dangerroom": 
                    ch_e "I'll try to save some for you."
                    jump Danger_Room
            elif E_Loc == "bg emma": 
                    ch_e "I'll tidy up a few things."
                    jump Emma_Room
            elif E_Loc == "bg player": 
                    ch_e "I'll be waiting for you."
                    jump Player_Room                
            elif E_Loc == "bg showerroom": 
                    ch_e "Don't keep me waiting. . ."
                    jump Shower_Room
            elif E_Loc == "bg campus": 
                    ch_e "I've got a nice location picked out."
                    jump Campus
            else:
                    ch_e "You know, I'll just meet you in my room."
                    $ E_Loc = "bg emma"
                    jump Emma_Room
            
    #She's agreed to come over    
    elif Line == "lonely":
            ch_e "Well, we can't have that now."
    elif Line == "command": 
            ch_e "If I must. . ."
        
    $ E_RecentActions.append("summoned")  
    $ Line = 0
    ch_e "I'll be there in a minute."   
    if "locked" in P_RecentActions:
            call Locked_Door("Emma")
            return
    $ E_Loc = bg_current 
    call EmmaOutfit
    call Set_The_Scene
    return

# End Emma Summon ///////////////////    


label Emma_Leave(Tempmod=Tempmod, GirlsNum = 0):        
    if "leaving" in E_RecentActions:
        call DrainWord("Emma","leaving")
    else:
        return
    
    if E_Loc == "hold":   
            # Activates if she's being moved out of play
            ch_e "Sorry, I have some business to attend to." 
            return
            
    if "Emma" in Party or "lockedtravels" in E_Traits:           
            #If she's in your party or if you've told her not to leave you
            #It resets her to your location
            $ E_Loc = bg_current 
            return
      
    elif "freetravels" in E_Traits or not ApprovalCheck("Emma", 700):
            #If you've told her to go wherever, or she just doesn't care what you think.   
            call EmmaOutfit           
            if GirlsNum: #if someone left before her
                        ch_e "I have to head out as well."
                        
            if E_Loc == "bg teacher":
                        ch_e "I have a class to teach."
            elif E_Loc == "bg classroom":
                        ch_e "I have some paperwork to take care of."
            elif E_Loc == "bg dangerroom": 
                        ch_e "I have a workout scheduled."   
            elif E_Loc == "bg campus": 
                        ch_e "I'm going to take in some sun." 
            elif E_Loc == "bg emma": 
                        ch_e "I'm heading back to my room." 
            elif E_Loc == "bg player": 
                        ch_e "I'll be heading to your room."   
            elif E_Loc == "bg showerroom" and ApprovalCheck("Emma", 1400):
                        ch_e "I'm going to take a quick shower."              
            else:        
                        ch_e "I'll see you later."                  
            hide Emma_Sprite
            return     
            #End Free Travels
    
    if bg_current == "bg dangerroom":   
            call Gym_Clothes("exit")
            
    call EmmaOutfit
    
    if "follow" not in E_Traits:
            # Sets a key to show that she's asked you to follow her at least once
            $ E_Traits.append("follow")   
        
    $ D20 = renpy.random.randint(1, 20) 
    $ Line = 0
    # Sets her preferences
    if E_Loc == "bg teacher": #fix change these if changed function
        $ Tempmod = -40
    elif E_Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = -10
    elif E_Loc == "bg dangerroom":    
        $ Tempmod = 20
    elif E_Loc == "bg showerroom":    
        $ Tempmod = 20
    
    
    if GirlsNum: #if someone left before her
                ch_e "I'm leaving as well."
                
    if E_Loc == "bg teacher":
        ch_e "I've got a class to teach, but you could probably learn a thing or two from it."
    elif E_Loc == "bg classroom":
        ch_e "I have some paperwork to take care of, but you could keep me company."
    elif E_Loc == "bg dangerroom": 
        ch_e "I have a workout planned, but there's room for one more."    
    elif E_Loc == "bg campus": 
        ch_e "I'm planning to get some sunning in, care to join me?" 
    elif E_Loc == "bg emma": 
        ch_e "I'm heading back to my room, but you can walk me back." 
    elif E_Loc == "bg player": 
        ch_e "I'm actually heading to your room, [E_Petname]."   
    elif E_Loc == "bg showerroom":    
        if ApprovalCheck("Emma", 1600):
            ch_e "I'm catching a quick shower, care to join me?"
        else:            
            ch_e "I'm headed for the showers, make sure to keep your distance."
            return      
    else:        
        ch_e "Would you care to come with me?"    
    
    
    menu:
        extend ""
        "Sure, I'll catch up.":
                if "followed" not in E_RecentActions:
                    call Statup("Emma", "Love", 55, 1) 
                    call Statup("Emma", "Inbt", 30, 1)
                $ Line = "go to"
            
        "Nah, we can talk later.":
                if "followed" not in E_RecentActions:
                    call Statup("Emma", "Obed", 50, 1)                            
                    call Statup("Emma", "Obed", 30, 2)
                ch_e "Very well, I'll talk to you later."
            
        "Could you please stay with me? I'll get lonely.":
                if ApprovalCheck("Emma", 600, "L") or ApprovalCheck("Emma", 1400):                
                    if "followed" not in E_RecentActions:
                        call Statup("Emma", "Love", 70, 1)                   
                        call Statup("Emma", "Obed", 50, 1)
                    $ Line = "lonely"
                else: 
                    if "followed" not in E_RecentActions:
                        call Statup("Emma", "Inbt", 30, 1)
                    $ Line = "no"
                
        "No, stay here.":
                if ApprovalCheck("Emma", 600, "O"):                              
                    #she is obedient
                    if "followed" not in E_RecentActions:
                        if E_Love >= 50:
                            call Statup("Emma", "Love", 90, 1)    
                        call Statup("Emma", "Love", 40, -1)                
                        call Statup("Emma", "Obed", 90, 1)    
                    $ Line = "command"
                    
                elif D20 >= 7 and ApprovalCheck("Emma", 1400):       
                    #she is generally favorable
                    if "followed" not in E_RecentActions:
                        call Statup("Emma", "Love", 70, -2)  
                        call Statup("Emma", "Love", 90, -1)  
                        call Statup("Emma", "Obed", 50, 2)                                
                        call Statup("Emma", "Obed", 90, 1)  
                    ch_e "I guess it wasn't that important. . ."              
                    $ Line = "yes"
                    
                elif ApprovalCheck("Emma", 200, "O"):                                         
                    #she is not obedient                   
                    if "followed" not in E_RecentActions:
                        call Statup("Emma", "Love", 70, -4)  
                        call Statup("Emma", "Love", 90, -2)   
                    ch_e "Does that work with your little strumpets?"  
                    if "followed" not in E_RecentActions:                       
                        call Statup("Emma", "Inbt", 40, 2)
                        call Statup("Emma", "Inbt", 60, 1)    
                        call Statup("Emma", "Obed", 70, -2)
                else:                                                                  
                    #she is obedient, but you failed to meet the checks                  
                    if "followed" not in E_RecentActions:
                        call Statup("Emma", "Inbt", 30, 1)
                        call Statup("Emma", "Inbt", 50, 1)                                    
                        call Statup("Emma", "Love", 50, -1, 1)
                        call Statup("Emma", "Obed", 70, -1)  
                    $ Line = "no" 
                #End ordered to stay
                    
    $ E_RecentActions.append("followed")     
    if not Line:                                                                        
            #You end the dialog neutrally      
            hide Emma_Sprite
            call Gym_Clothes("auto", "Emma")
            return
    
    if Line == "no":                                                                    
            # She's refused, context based dialog
            if E_Loc == "bg teacher":
                ch_e "I'm not \"cutting class,\" [E_Petname]." 
            elif E_Loc == "bg classroom":
                ch_e "I'm afraid not, [E_Petname], I need to get this work done." 
            elif E_Loc == "bg dangerroom": 
                ch_e "I'm sorry, but how do you think I keep this figure?"
            else:
                ch_e "I'm sorry, I'm just much too busy at the moment."         
            hide Emma_Sprite
            call Gym_Clothes("auto", "Emma")         
            return
        
    elif Line == "go to":                                                                 
            #You agreed to go to her instead  
            $ Tempmod = 0
            call DrainWord("All","leaving")  
            call DrainWord("All","arriving")        
            hide Emma_Sprite
            call Gym_Clothes("auto", "Emma")
            if E_Loc == "bg teacher":
                ch_e "I'll see you there."            
                jump Class_Room_Entry
            elif E_Loc == "bg classroom":
                ch_e "Excellent, that should pass the time."            
                jump Class_Room_Entry
            elif E_Loc == "bg dangerroom": 
                ch_e "I'll try to leave some for you."
                jump Danger_Room_Entry
            elif E_Loc == "bg emma": 
                ch_e "I'll be waiting."
                jump Emma_Room
            elif E_Loc == "bg player": 
                ch_e "I'll be waiting."
                jump Player_Room                
            elif E_Loc == "bg showerroom": 
                ch_e "I'll get started."
                jump Shower_Room_Entry
            elif E_Loc == "bg campus": 
                ch_e "Ok, let's."
                jump Campus_Entry
            else:     
                ch_e "You know, I'll just meet you in my room."
                $ E_Loc = "bg emma"
                jump Emma_Room
            #End "goto" where she's at
            
    #She's agreed to come over    
    elif Line == "lonely":
            ch_e "Well we wouldn't want that. . ."
    elif Line == "command": 
            ch_e "If you insist."
    
    $ Line = 0
    ch_e "I suppose I can stay for a while."                                
    $ E_Loc = bg_current 
    return

# End Emma Leave ///////////////////   

label Emma_Dismissed(Leaving = 0):
    if "Emma" in Party:        
            $ Party.remove("Emma")
    call Emma_Schedule(0) #if E_Loc == bg_current then it means she wants to stay here
    if "leaving" in E_RecentActions:
            call DrainWord("Emma","leaving")   
    menu:
        "You can leave if you like.":
                if E_Loc == bg_current and not ApprovalCheck("Emma", 600, "O"):
                        ch_e "Be that as it may, I'll stick around for a bit."
                else:
                        ch_e "Very well, [E_Petname]"
                        $ Leaving = 1                   
        "Could you give me the room please?":                            
                if E_Loc == bg_current and not ApprovalCheck("Emma", 800, "LO"):
                        ch_e "As it happens, I don't have any other plans."
                elif not ApprovalCheck("Emma", 500, "LO"):
                        ch_e "I don't think that I can."               
                else:
                        if "dismissed" not in E_DailyActions:
                                call Statup("Emma", "Obed", 30, 7)
                                call Statup("Emma", "Obed", 50, 5)
                        ch_e "Very well. . ." 
                        $ Leaving = 1                              
        "You can go now.":                         
                if E_Loc == bg_current and not ApprovalCheck("Emma", 450, "O"):
                        ch_e "No, I don't believe that I can."
                elif not ApprovalCheck("Emma", 250, "O"):
                        call EmmaFace("confused") 
                        ch_e "Now I am intrigued."
                else:
                        if "dismissed" not in E_DailyActions:
                                call Statup("Emma", "Obed", 40, 10)
                                call Statup("Emma", "Obed", 60, 7)
                        ch_e "Very well. . ."
                        $ Leaving = 1                               
        "Nevermind.":
                        return                                           
                
    if not Leaving and bg_current in ("bg campus","bg classroom","bg dangerroom"):
            #if there is space nearby. . .
            call Remove_Girl("Emma",1,1)            
    elif not Leaving:     
            menu:
                extend ""
                "I insist, get going.":  
                        if E_Loc != bg_current and (ApprovalCheck("Emma", 1200, "LO") or ApprovalCheck("Emma", 400, "O")):
                                #If she has someplace to be and is obedient
                                if "dismissed" not in E_DailyActions:
                                        call Statup("Emma", "Love", 70, -5, 1)
                                        call Statup("Emma", "Obed", 60, 10)
                                        call Statup("Emma", "Obed", 80, 5)
                                ch_e "Very well. . ."  
                                $ Leaving = 1                                  
                        elif E_Loc != bg_current and (ApprovalCheck("Emma", 1000, "LO") or ApprovalCheck("Emma", 250, "O")):
                                #If she has someplace to be and is less obedient
                                if "dismissed" not in E_DailyActions:
                                        call Statup("Emma", "Love", 50, -5, 1)
                                        call Statup("Emma", "Love", 70, -5, 1)
                                        call Statup("Emma", "Obed", 60, 10)
                                        call Statup("Emma", "Obed", 80, 5)
                                call EmmaFace("angry") 
                                ch_e "I'll leave, but do not test me, [E_Petname]"      
                                $ Leaving = 1                         
                        elif E_Loc != bg_current:
                                #If she has someplace to be but is not obedient
                                if "dismissed" not in E_DailyActions:
                                        call Statup("Emma", "Love", 50, -5, 1)
                                        call Statup("Emma", "Love", 70, -10, 1)
                                        call Statup("Emma", "Obed", 50, -3)
                                        call Statup("Emma", "Inbt", 50, 5)
                                        call Statup("Emma", "Inbt", 80, 3)
                                call EmmaFace("angry") 
                                ch_e "Well now I'm definitely not."          
                        elif ApprovalCheck("Emma", 1400, "LO") or ApprovalCheck("Emma", 400, "O"):
                                #If she has nowhere to be to be but is obedient
                                if "dismissed" not in E_DailyActions:
                                        call Statup("Emma", "Love", 50, -5, 1)
                                        call Statup("Emma", "Obed", 50, 10)
                                        call Statup("Emma", "Obed", 80, 5)
                                call EmmaFace("sad") 
                                ch_e "I suppose I could get out of your way."
                                $ Leaving = 1                   
                        else:
                                #If she has nowhere to be to be and is not obedient
                                if "dismissed" not in E_DailyActions:
                                        call Statup("Emma", "Love", 50, -5, 1)
                                        call Statup("Emma", "Love", 70, -10, 1)
                                        call Statup("Emma", "Obed", 50, -5)
                                        call Statup("Emma", "Inbt", 50, 3)
                                        call Statup("Emma", "Inbt", 80, 2)
                                call EmmaFace("sad") 
                                ch_e "That doesn't look like it'll be happening."          
                "Ok, nevermind.":    
                                pass
                    
    if "dismissed" not in E_DailyActions:
            $ E_DailyActions.append("dismissed")        
    if "Emma" in Nearby:
        "You shift a bit away from Emma"
    elif Leaving == 0:
            # Stay
            $ E_Loc = bg_current
    else:
            # Go
            if E_Loc != bg_current: #it stays the same
                pass
            elif bg_current == "bg emma":
                $ E_Loc = "bg campus"
            else:
                $ E_Loc = "bg emma"
            hide Emma_Sprite
            "Emma heads out." 
    return
    #end "you can leave"
    

label Emma_AboutRogue:
    ch_e "What do I think about her? Well. . ."
    
    if "poly Rogue" in E_Traits:  
        ch_e "As you're aware, we've shared a great deal. . ."    
    elif E_LikeRogue >= 900:
        ch_e "I do find her rather mesmerizing. . ."
    elif E_LikeRogue >= 800:
        ch_e "That accent certainly did grow on me. . ."    
    elif E_LikeRogue >= 700:
        ch_e "We've become quite close."
    elif E_LikeRogue >= 600:
        ch_e "I'm rather fond of her."
    elif E_LikeRogue >= 500:
        ch_e "She's an adequate student."
    elif E_LikeRogue >= 400:
        ch_e "She can be a bit of a handful."
    elif E_LikeRogue >= 300:
        ch_e "I can barely tollerate her disrespectful nature." 
    else:
        ch_e "That swamp rat? What about her?"          
    return
label Emma_AboutKitty:
    ch_e "What do I think about her? Well. . ."
    
    if "poly Kitty" in E_Traits:  
        ch_e "As you're aware, we do get along quite well. . ."    
    elif E_LikeKitty >= 900:
        ch_e "She is rather. . . flexible. . ."
    elif E_LikeKitty >= 800:
        ch_e "She is rather adorable. . ."    
    elif E_LikeKitty >= 700:
        ch_e "She's something of a friend at this point."
    elif E_LikeKitty >= 600:
        ch_e "Once you get to know her, she's not bad."
    elif E_LikeKitty >= 500:
        ch_e "She's an adequate student."
    elif E_LikeKitty >= 400:
        ch_e "She can be a bit of a know it all."
    elif E_LikeKitty >= 300:
        ch_e "I can't stand her constant questions." 
    else:
        ch_e "That little bitch?"
          
    return
    
label Emma_AboutLaura:
    ch_e "What do I think about her? Well. . ."
    
    if "poly Laura" in E_Traits:  
        ch_e "She is quite. . . energetic. . ."    
    elif E_LikeLaura >= 900:
        ch_e "She's very durable. . ."
    elif E_LikeLaura >= 800:
        ch_e "She has a rough quality that is quite exciting. . ."    
    elif E_LikeLaura >= 700:
        ch_e "She's something of a friend at this point."
    elif E_LikeLaura >= 600:
        ch_e "Once you get to know her, she's not bad."
    elif E_LikeLaura >= 500:
        ch_e "She's an adequate student."
    elif E_LikeLaura >= 400:
        ch_e "She is a bit rough around the edges"
    elif E_LikeLaura >= 300:
        ch_e "Yes, a bit feral, that one." 
    else:
        ch_e "I'd put her down myself if I didn't have responsibilites."
          
    return
#End Emma_AboutRogue
    

## Emma's Clothes ///////////////////
label Emma_Clothes(Public=0,Bonus=0):   
    if "exhibitionist" in E_Traits:
            $ Public += 1
    if E_Rep <= 200:
            $ Public += 2
    elif E_Rep <= 400:
            $ Public += 1        
    if "public" in E_History:
            $ Public += 2
    #This is a trait for if she's open to being sexy in public
        
    call EmmaFace
    menu:
        ch_e "You wanted to discuss my clothing choices?"
        "Let's talk about your modded clothes.":
                    jump Emma_Modded_Clothes_Menu
        "Let's talk about your outfits.":
                    jump Emma_Clothes_Outfits        
        "Let's talk about your over shirts.":
                    jump Emma_Clothes_Over        
        "Let's talk about your legwear.":
                    jump Emma_Clothes_Legs
        "Let's talk about your underwear.":
                    jump Emma_Clothes_Under
        "Let's talk about the other stuff.":
                    jump Emma_Clothes_Misc
        "That looks really good on you, you should remember that one. [[Set Custom]":
                menu:
                    "Which slot would you like this saved in?"
                    "Custom 1":
                                call Emma_OutfitShame(3,1)
                    "Custom 2":
                                call Emma_OutfitShame(5,1)
                    "Custom 3":
                                call Emma_OutfitShame(6,1)
                    "Custom 4":
                                call Emma_OutfitShame(15,1)
                    "Custom 5":
                                call Emma_OutfitShame(16,1)
                    "Custom 6":
                                call Emma_OutfitShame(17,1)
                    "Custom 7":
                                call Emma_OutfitShame(18,1)
                    "Custom 8":
                                call Emma_OutfitShame(19,1)
                    "Custom 9":
                                call Emma_OutfitShame(20,1)
                    "Gym Clothes":
                                call Emma_OutfitShame(7,1)
                    "Sleepwear":
                                call Emma_OutfitShame(9,1)
                    "Swimwear":
                                call Emma_OutfitShame(10,1)
                    "Never mind":
                                pass        
        "Switch to. . .":   
                menu:              
                    "Rogue":
                        call Rogue_Chat_Set("wardrobe")
                    "Kitty":
                        call Kitty_Chat_Set("wardrobe")   
                    "Laura":
                        call Laura_Chat_Set("wardrobe")  
                    "Never mind":
                        pass                        
        "Never mind, you look good like that.":
                if "wardrobe" not in E_RecentActions: 
                        #Apply stat boosts only if it's the first time this turn 
                        if E_Chat[1] <= 1:                
                                call Statup("Emma", "Love", 70, 15)
                                call Statup("Emma", "Obed", 40, 20)
                                ch_e "I thought so as well."
                        elif E_Chat[1] <= 10:
                                call Statup("Emma", "Love", 70, 5)
                                call Statup("Emma", "Obed", 40, 7)
                                ch_e "Isn't it?" 
                        elif E_Chat[1] <= 50:
                                call Statup("Emma", "Love", 70, 1)
                                call Statup("Emma", "Obed", 40, 1) 
                        $ E_RecentActions.append("wardrobe")  
                #sets up a temporary outfit
                $ E_TempClothes[1] = E_Arms  
                $ E_TempClothes[2] = E_Legs 
                $ E_TempClothes[3] = E_Over
                $ E_TempClothes[4] = E_Neck 
                $ E_TempClothes[5] = E_Chest 
                $ E_TempClothes[6] = E_Panties
                $ E_TempClothes[7] = E_Boots
                $ E_TempClothes[8] = E_Hair
                $ E_TempClothes[9] = E_Hose
                $ E_TempClothes[0] = 1 
                $ E_Outfit = "temporary"
                $ E_OutfitDay = "temporary"           
                $ E_Chat[1] += 1                
                return
                            
    jump Emma_Clothes
    #End of Emma Wardrobe Main Menu
        
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Emma_Clothes_Outfits:                                                                                 # Outfits
        "I really like that teacher's look you wear.": 
            call EmmaOutfit("teacher")   
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ E_Outfit = "teacher"
                    $ E_Shame = E_OutfitShame[1]
                    ch_e "Yes, a very tasteful look."
                "Let's try something else though.":
                    ch_e "Very well."            
                    
        "That combat uniform you have looks really nice on you.":
            call EmmaOutfit("costume")
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ E_Outfit = "costume"
                    $ E_Shame = E_OutfitShame[2]
                    ch_e "I really enjoyed wearing that one."
                "Let's try something else though.":
                    ch_e "Very well."            
                    
        "Remember that outfit we put together? [[Set a custom outfit] (locked)" if not E_Custom[0] and not E_Custom2[0] and not E_Custom3[0] and not E_Custom4[0] and not E_Custom5[0] and not E_Custom6[0] and not E_Custom7[0] and not E_Custom8[0] and not E_Custom9[0]:
                        pass       
                        
        "Remember that outfit we put together?" if E_Custom[0] or E_Custom2[0] or E_Custom3[0] or E_Custom4[0] or E_Custom5[0] or E_Custom6[0] or E_Custom7[0] or E_Custom8[0] or E_Custom9[0]: 
            $ Cnt = 0
            while 1:
                menu:                
                    "Throw on Custom 1 (locked)" if not E_Custom[0]:
                        pass
                    "Throw on Custom 1" if E_Custom[0]:
                        $ E_Outfit = "custom1"
                        call EmmaOutfit
                        $ Cnt = 3
                    "Throw on Custom 2 (locked)" if not E_Custom2[0]:
                        pass
                    "Throw on Custom 2" if E_Custom2[0]:
                        $ E_Outfit = "custom2"
                        call EmmaOutfit
                        $ Cnt = 5
                    "Throw on Custom 3 (locked)" if not E_Custom3[0]:
                        pass
                    "Throw on Custom 3" if E_Custom3[0]:
                        $ E_Outfit = "custom3"
                        call EmmaOutfit
                        $ Cnt = 6
                    
                    "Throw on Custom 4 (locked)" if not E_Custom4[0]:
                        pass
                    "Throw on Custom 4" if E_Custom4[0]:
                        $ E_Outfit = "custom4"
                        call EmmaOutfit
                        $ Cnt = 15
                    "Throw on Custom 5 (locked)" if not E_Custom5[0]:
                        pass
                    "Throw on Custom 5" if E_Custom5[0]:
                        $ E_Outfit = "custom5"
                        call EmmaOutfit
                        $ Cnt = 16
                    "Throw on Custom 6 (locked)" if not E_Custom6[0]:
                        pass
                    "Throw on Custom 6" if E_Custom6[0]:
                        $ E_Outfit = "custom6"
                        call EmmaOutfit
                        $ Cnt = 17
                    "Throw on Custom 7 (locked)" if not E_Custom7[0]:
                        pass
                    "Throw on Custom 7" if E_Custom7[0]:
                        $ E_Outfit = "custom7"
                        call EmmaOutfit
                        $ Cnt = 18
                    "Throw on Custom 8 (locked)" if not E_Custom8[0]:
                        pass
                    "Throw on Custom 8" if E_Custom8[0]:
                        $ E_Outfit = "custom8"
                        call EmmaOutfit
                        $ Cnt = 19
                    "Throw on Custom 9 (locked)" if not E_Custom9[0]:
                        pass
                    "Throw on Custom 9" if E_Custom9[0]:
                        $ E_Outfit = "custom9"
                        call EmmaOutfit
                        $ Cnt = 20
                    "You should wear this one in our rooms. (locked)" if not Cnt:
                        pass
                    "You should wear this one in our rooms." if Cnt:
                        if Cnt == 5:
                            $ E_Schedule[9] = "custom2"
                        elif Cnt == 15:
                            $ E_Schedule[9] = "custom4"
                        elif Cnt == 16:
                            $ E_Schedule[9] = "custom5"
                        elif Cnt == 17:
                            $ E_Schedule[9] = "custom6"
                        elif Cnt == 18:
                            $ E_Schedule[9] = "custom7"
                        elif Cnt == 19:
                            $ E_Schedule[9] = "custom8"
                        elif Cnt == 20:
                            $ E_Schedule[9] = "custom9"
                        elif Cnt == 6:
                            $ E_Schedule[9] = "custom3"
                        else:
                            $ E_Schedule[9] = "custom1"
                        ch_e "Ok, sure."
                    
                    
                    "On second thought, forget about that one outfit. . .":
                        menu:
                            "Custom 1 [[clear custom 1]" if E_Custom[0]:
                                ch_e "Very well."
                                $ E_Custom[0] = 0
                            "Custom 1 [[clear custom 1] (locked)" if not E_Custom[0]:
                                pass
                            "Custom 2 [[clear custom 2]" if E_Custom2[0]:
                                ch_e "Very well."
                                $ E_Custom2[0] = 0
                            "Custom 2 [[clear custom 1] (locked)" if not E_Custom2[0]:
                                pass
                            "Custom 3 [[clear custom 3]" if E_Custom3[0]:
                                ch_e "Very well."
                                $ E_Custom3[0] = 0
                            "Custom 3 [[clear custom 3] (locked)" if not E_Custom3[0]:
                                pass
                            "Custom 4 [[clear custom 4]" if E_Custom4[0]:
                                ch_e "Very well."
                                $ E_Custom4[0] = 0
                            "Custom 4 [[clear custom 4] (locked)" if not E_Custom4[0]:
                                pass
                            "Custom 5 [[clear custom 5]" if E_Custom5[0]:
                                ch_e "Very well."
                                $ E_Custom5[0] = 0
                            "Custom 5 [[clear custom 5] (locked)" if not E_Custom5[0]:
                                pass
                            "Custom 6 [[clear custom 6]" if E_Custom6[0]:
                                ch_e "Very well."
                                $ E_Custom6[0] = 0
                            "Custom 6 [[clear custom 6] (locked)" if not E_Custom6[0]:
                                pass
                            "Custom 7 [[clear custom 7]" if E_Custom7[0]:
                                ch_e "Very well."
                                $ E_Custom7[0] = 0
                            "Custom 7 [[clear custom 7] (locked)" if not E_Custom7[0]:
                                pass
                            "Custom 8 [[clear custom 8]" if E_Custom8[0]:
                                ch_e "Very well."
                                $ E_Custom8[0] = 0
                            "Custom 8 [[clear custom 8] (locked)" if not E_Custom8[0]:
                                pass
                            "Custom 9 [[clear custom 9]" if E_Custom9[0]:
                                ch_e "Very well."
                                $ E_Custom9[0] = 0
                            "Custom 9 [[clear custom 9] (locked)" if not E_Custom9[0]:
                                pass
                            "Never mind, [[back].":
                                pass    
                                            
                                            
                    "You should wear this one out. [[choose outfit first](locked)" if not Cnt:
                        pass
                    "You should wear this one out." if Cnt:
                        call Emma_Custom_Out(Cnt)
                    "Ok, back to what we were talking about. . .":
                        $ Cnt = 0
                        jump Emma_Clothes_Outfits                    
        
        "Your birthday suit looks really great. . .":                                     
            #Nude
            call EmmaFace("sly", 1)
            $ Line = 0
            if not E_Chest and not E_Panties and not E_Over and not E_Legs and not E_Hose:  
                # if already naked (yes)
                ch_e "Apparently so. . ."  
            elif E_SeenChest and E_SeenPussy and ApprovalCheck("Emma", 1200, TabM=(5-Public)):
                #if you've seen it all and she likes you well enough (yes)
                ch_e "I'll take that as an invitation. . ."  
                $ Line = 1
            elif ApprovalCheck("Emma", 2000, TabM=(5-Public)):
                #if you haven't seen everything but she really likes you (yes)
                ch_e "I suppose you've earned it. . ."    
                $ Line = 1
            elif E_SeenChest and E_SeenPussy and ApprovalCheck("Emma", 1200, TabM=0):
                # if you've seen it but it's in public (no)
                ch_e "As you're well aware, but this isn't the appropriate venue. . ."  
            elif ApprovalCheck("Emma", 2000, TabM=0):
                #if you haven't seen everything but she really likes you and it's public (no) 
                ch_e "I assure you it is, but this isn't the appropriate venue. . ."  
            elif ApprovalCheck("Emma", 1000, TabM=0):     
                #if you haven't seen everything and she kinda likes you but it's public (no)
                call EmmaFace("surprised", 1)
                ch_e "I assure you that it is, but that's not the way to ask."
                $ E_Blush = 0
            else:
                # if she refuses. (no) 
                call EmmaFace("angry", 1)
                ch_e "Not the worst line I've heard."
                ch_e ". . . but close."
                
            if Line:                                                            #If she got nude. . .                            
                call EmmaOutfit("nude")
                "She strips down."
                call Emma_First_Topless
                call Emma_First_Bottomless(1)
                call EmmaFace("sexy")
                menu:
                    "You know, you should wear this one out. [[set current outfit]":
                        if "exhibitionist" in E_Traits:
                            call EmmaFace("sexy",2,Eyes="down")
                            ch_e "Mmmmm. . ." 
                            $ E_Outfit = "nude"
                            call Statup("Emma", "Lust", 50, 10) 
                            call Statup("Emma", "Lust", 70, 5) 
                            $ E_Shame = E_OutfitShame[0]
                            call EmmaFace("sexy",1)
                        elif ApprovalCheck("Emma", 800, "I") or ApprovalCheck("Emma", 2800, TabM=0): 
                            ch_e "Oooh, that would cause quite a stir. . ." 
                            $ E_Outfit = "nude"
                            $ E_Shame = E_OutfitShame[0]
                        elif ApprovalCheck("Emma", 400, "I") and ApprovalCheck("Emma", 1200, TabM=0): 
                            call EmmaFace("bemused", 1,Eyes="side")
                            ch_e "You shouldn't suggest such things. . ."
                        else:
                            call EmmaFace("sexy", 1,Eyes="surprised")
                            ch_e "Impossible." 
                            
                    "Let's try something else though.":
                        if "exhibitionist" in E_Traits:
                            ch_e "Too much for you to handle?"                         
                        elif ApprovalCheck("Emma", 800, "I") or ApprovalCheck("Emma", 2800, TabM=0):       
                            call EmmaFace("bemused", 1)             
                            ch_e "Because obviously I couldn't go around like this. . ."
                        else:
                            call EmmaFace("confused", 1)
                            ch_e "So long as it's just the two of us, I don't mind this."   
            $ Line = 0
                
        "How about throwing on your sleepwear?" if not Taboo:
            #fix add conditions
            call EmmaOutfit("sleep")
        "How about throwing on your swimwear?" if not Taboo or bg_current == "bg pool":
            #fix add conditions
            call EmmaOutfit("swimwear")
            
        "Let's talk about what you wear outside.":
            call Emma_Clothes_Schedule
            
        "Never mind":    
            jump Emma_Clothes     
            
    jump Emma_Clothes
    #End of Emma Outfits
            
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Emma_Clothes_Over:                                                                                            # Overshirts
        "Why don't you go with no [E_Over]?" if E_Over:
            call EmmaFace("bemused", 1)
            if ApprovalCheck("Emma", 800, TabM=(3-Public)) and (E_Chest or E_SeenChest):
                ch_e "Certainly."
            elif ApprovalCheck("Emma", 1200, TabM=0):
                call Emma_NoBra
                if not _return:
                    jump Emma_Clothes                    
            $ Line = E_Over
            $ E_Over = 0   
            call Emma_Tits_Up
            "She shrugs off her [Line]."
            if not E_Chest:
                call Emma_First_Topless
            
        "Try on that white jacket you have." if E_Over != "jacket":
            call EmmaFace("bemused")
            if E_Chest or E_SeenChest or ApprovalCheck("Emma", 500, TabM=(3-Public)):
                ch_e "Yeah, ok."          
            else:
                call EmmaFace("bemused", 1)
                ch_e "I'm not sure this is appropriate without something more substantial underneath."
                jump Emma_Clothes    
            $ E_Over = "jacket"   
            
        "Try on that lace nighty." if E_Over != "nighty":
            call EmmaFace("bemused")
            if E_Chest or E_SeenChest or ApprovalCheck("Emma", 500, TabM=(3-Public)):
                ch_e "Yeah, ok."          
            else:
                call EmmaFace("bemused", 1)
                ch_e "This is a bit shear for this top."
                jump Emma_Clothes    
            $ E_Over = "nighty"   
                            
        "Maybe just throw on a towel?" if E_Over != "towel":
            call EmmaFace("bemused", 1)
            $ Bonus = 5 if bg_current == "bg showerroom" else 0
            if E_Chest or (E_SeenChest and ApprovalCheck("Emma", 500, TabM=(3-Public-Bonus))):
                ch_e "Oh, you like this?"
            elif ApprovalCheck("Emma", 1000, TabM=(3-Public-Bonus)):
                call EmmaFace("perplexed", 1)
                ch_e "Fine."          
            else:
                ch_e "This wouldn't leave much to the imagination."
                jump Emma_Clothes  
            call Emma_NoBra
            if not _return:
                jump Emma_Clothes
            $ E_Over = "towel"       
            call Emma_Tits_Up
                            
        "Never mind":
            pass
    jump Emma_Clothes
    #End of Emma Top
            
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    label Emma_NoBra: #fix test this
        menu:
            ch_e "I'm not wearing much of anything under this. . ."
            "Then you could slip something on under it. . .":   
                        if (E_SeenChest and ApprovalCheck("Emma", 1000, TabM=(4-Public))) or ApprovalCheck("Emma", 1200, TabM=(5-Public)):
                                ch_e "-not that I'm overly concerned about it. . ."
                        elif ApprovalCheck("Emma", 900, TabM=(3-Public)) and "lace bra" in E_Inventory:
                                ch_e "I suppose I could."
                                $ E_Chest  = "lace bra"    
                                call Emma_Tits_Up
                                "She pulls out her lace bra and slips it on under her [E_Over]."
#                        elif ApprovalCheck("Emma", 800, TabM=(3-Public)):
#                                ch_e "I suppose I could."
#                                $ E_Chest = "bra"
#                                "She pulls out her bra and slips it on under her [E_Over]."
                        elif ApprovalCheck("Emma", 700, TabM=(3-Public)):
                                ch_e "I suppose I could."
                                $ E_Chest = "corset"   
                                call Emma_Tits_Up
                                "She pulls out her corset and slips it on under her [E_Over]."
                        elif ApprovalCheck("Emma", 600, TabM=(3-Public)):
                                ch_e "I suppose I could."
                                $ E_Chest = "sports bra"
                                "She pulls out her sports bra and slips it on under her [E_Over]."
                        else:
                                ch_e "Yes, but I'd rather not."
                                return 0
                        
            "You could always just wear nothing at all. . .":
                        if ApprovalCheck("Emma", 1100, "LI", TabM=(3-Public)) and E_Love > E_Inbt:               
                                ch_e "The things I do for you. . ."
                        elif ApprovalCheck("Emma", 700, "OI", TabM=(3-Public)) and E_Obed > E_Inbt:
                                ch_e "If that's what you insist. . ."
                        elif ApprovalCheck("Emma", 600, "I", TabM=(3-Public)):
                                ch_e "I suppose I could. . ."
                        elif ApprovalCheck("Emma", 1300, TabM=(3-Public)):
                                ch_e "Very well."
                        else: 
                                call EmmaFace("surprised")
                                $ E_Brows = "angry"
                                if Taboo > 20:
                                    ch_e "I'm afraid I couldn't do that in public."
                                else:
                                    ch_e "I could, but I wouldn't."
                                return 0
                                
                    
            "Never mind.":
                        return 0
        return 1
        #End of Emma bra check
       
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Emma_Clothes_Legs:                                                                                                    # Leggings    
        "Maybe go without the [E_Legs]." if E_Legs:
            call EmmaFace("sexy", 1)
            if E_SeenPanties and E_Panties and ApprovalCheck("Emma", 500, TabM=(6-Public)):
                ch_e "Fine."
            elif E_SeenPussy and ApprovalCheck("Emma", 900, TabM=(5-Public)):
                ch_e "Fine."
            elif ApprovalCheck("Emma", 1300, TabM=(2-Public)) and E_Panties:
                ch_e "It's not like I haven't worn this look before. . ."
            elif ApprovalCheck("Emma", 800) and not E_Panties:
                call Emma_NoPantiesOn
                if not _return:
                    jump Emma_Clothes
            else:
                ch_e "I'm afraid not."
                if not E_Panties:
                    ch_e "You understand, it could get. . . drafty. . ."
                jump Emma_Clothes
            $ Line = E_Legs
            $ E_Legs = 0    
            "She peels her [Line] off."
            $ Line = 0
            call Emma_First_Bottomless
        
        "You look great in those white pants." if E_Legs != "pants":
            ch_e "I know."
            $ E_Legs = "pants"
                
        "You look great in that little skirt." if E_Legs != "skirt":
            ch_e "I agree."
            $ E_Legs = "skirt"
            
        "You look great in boots." if E_Boots != "thigh boots":
            ch_e "They do look nice on me."
            $ E_Boots = "thigh boots"
        "Maybe lose the boots." if E_Boots == "thigh boots":
            ch_e "I suppose."
            $ E_Boots = 0
                
        "You look great in yoga pants." if E_Legs != "yoga pants":
            ch_e "Yeah, ok."
            $ E_Legs = "yoga pants"
            
#        "What about wearing your yellow shorts?" if E_Legs != "shorts":
#            ch_e "K, no problem."
#            $ E_Legs = "shorts"    
                   
        "Never mind":
            pass
    jump Emma_Clothes
    #End of Emma Pants
    
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
    
    label Emma_NoPantiesOn: #fix test this
        call EmmaFace("sexy",Eyes="side")
        ch_e "You should be aware. . ."
        call EmmaFace("sly")
        menu:
            ch_e "I'm not wearing any panties at the moment. . ."
            "Then you could slip on a pair. . .":   
                        if (E_SeenPussy and ApprovalCheck("Emma", 1100, TabM=(5-Public))) or ApprovalCheck("Emma", 1500, TabM=(5-Public)):
                                $ E_Blush = 1
                                ch_e "I didn't say that bothered me. . ."
                                $ E_Blush = 0                
                        elif ApprovalCheck("Emma", 800, TabM=(5-Public)) and "lace panties" in E_Inventory:
                                ch_e "I like how you think, turn around."
                                $ E_Panties  = "lace panties"    
                                "She pulls out her lace panties, and with your back turned she removes her pants, and slips her panties on."
                        elif ApprovalCheck("Emma", 700, TabM=(5-Public)):
                                ch_e "Yeah, I guess."
                                $ E_Panties = "white panties"
                                "She pulls out her white panties, and with your back turned she removes her pants, and slips her panties on."                   
                        elif ApprovalCheck("Emma", 500, TabM=(6-Public)):
                                ch_e "Yeah, I guess."
                                $ E_Panties = "sports panties"
                                "She pulls out her sports panties, and with your back turned she removes her pants, and slips her panties on."                   
                        elif Taboo and ApprovalCheck("Emma", 800, TabM=0):
                                ch_e "I like how you think, but not in public like this."
                                return 0
                        else:
                                ch_e "I could, but I'd rather not."
                                return 0
                        
            "You could always just wear nothing at all. . .":
                        if ApprovalCheck("Emma", 1100, "LI", TabM=(5-Public)) and E_Love > E_Inbt:               
                                ch_e "I suppose I could. . ."
                        elif ApprovalCheck("Emma", 700, "OI", TabM=(5-Public)) and E_Obed > E_Inbt:
                                ch_e "If you'd like. . ."
                        elif ApprovalCheck("Emma", 600, "I", TabM=(5-Public)):
                                ch_e "I certainly could. . ."
                        elif ApprovalCheck("Emma", 1300, TabM=(5-Public)):
                                ch_e "Very well."
                        else: 
                                call EmmaFace("surprised")
                                $ E_Brows = "angry"
                                if Taboo > 20:
                                    ch_e "I'm afraid not out here, [E_Petname]!"
                                else:
                                    ch_e "You wish, [E_Petname]!"
                                return 0
                                
            "Never mind.":
                ch_e "Ok. . ."
                return 0
        return 1
        #End of Emma Panties check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Emma_Clothes_Under:
        "Tops":
            menu:
                "How about you lose the [E_Chest]?" if E_Chest:
                    call EmmaFace("bemused", 1)
                    if E_SeenChest and ApprovalCheck("Emma", 900, TabM=(4-Public)):
                        ch_e "Of course."    
                    elif ApprovalCheck("Emma", 1100, TabM=2):
                        if Taboo:
                            ch_e "I'd rather not out here. . ."
                        else:
                            ch_e "I suppose for you. . ."
                    elif E_Over == "jacket" and ApprovalCheck("Emma", 700, TabM=(3-Public)):
                        ch_e "This is a bit daring without anything under it. . ."  
                    elif not E_Over:
                        ch_e "I don't think that would be appropriate."
                        jump Emma_Clothes 
                    else:
                        ch_e "I'm afraid not, [E_Petname]."
                        jump Emma_Clothes 
                    $ Line = E_Chest
                    $ E_Chest = 0
                    if E_Over:
                        "She reaches under her [E_Over] grabs her [Line], and pulls it out, dropping it to the ground."
                    else:
                        "She lets her [Line] fall to the ground."
                        call Emma_First_Topless
                  
                "I like that corset you have." if E_Chest != "corset":
                    if E_SeenChest or ApprovalCheck("Emma", 1000, TabM=(3-Public)):
                        ch_e "So do I."   
                        $ E_Chest = "corset"  
                        $ E_TitsUp = 1
                    else:                
                        ch_e "I don't think that would be appropriate. . ."      
                        
                "I like that lace bra." if "lace bra" in E_Inventory and E_Chest != "lace bra":
                    if E_SeenChest or ApprovalCheck("Emma", 1300, TabM=(3-Public)):
                        ch_e "Fine."   
                        $ E_Chest = "lace bra"         
                    else:                
                        ch_e "It's a bit revealing. . ."  
                    
                "I like that sports bra." if E_Chest != "sports bra":
                    if E_SeenChest or ApprovalCheck("Emma", 1000, TabM=(3-Public)):
                        ch_e "Fine."   
                        $ E_Chest = "sports bra"         
                    else:                
                        ch_e "I'm not sure about that. . ."  
                          
                "I like that bikini top." if E_Chest != "bikini top" and "bikini top" in E_Inventory:
                    if bg_current == "bg pool":
                            ch_e "Fine."   
                            $ E_Chest = "bikini top"         
                    else:                
                            if E_SeenChest or ApprovalCheck("Emma", 800, TabM=2):
                                ch_e "Fine."   
                                $ E_Chest = "bikini top"         
                            else:                
                                ch_e "I don't know about wearing that here. . ." 
                "Never mind":
                    pass 
                  
                                    
        "Hose and stockings options":
            menu:          
                "You could lose the hose." if E_Hose:     
                                $ E_Hose = 0  
                "The thigh-high hose would look good with that." if E_Hose != "stockings" and "stockings and garterbelt" in E_Inventory:    
                                $ E_Hose = "stockings"  
                "The pantyhose would look good with that." if E_Hose != "pantyhose" and "pantyhose" in E_Inventory:    
                                $ E_Hose = "pantyhose" 
                "The stockings and garterbelt would look good with that." if E_Hose != "stockings and garterbelt" and "stockings and garterbelt" in E_Inventory:     
                                $ E_Hose = "stockings and garterbelt"  
                "Maybe just the garterbelt?" if E_Hose != "garterbelt" and "stockings and garterbelt" in E_Inventory:     
                                $ E_Hose = "garterbelt"  
                "Never mind":
                        pass  
                      
        #Panties   
        "Panties":
            menu:
                "You could lose those panties. . ." if E_Panties:
                    call EmmaFace("bemused", 1)  
                    if (ApprovalCheck("Emma", 900) or E_SeenPussy) and not Taboo:
                        #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
                        
                        if ApprovalCheck("Emma", 850, "L"):               
                                ch_e "You like the view?"
                        elif ApprovalCheck("Emma", 500, "O"):
                                ch_e "If you'd like."
                        elif ApprovalCheck("Emma", 350, "I"):
                                ch_e "I do enjoy going without them. . ."
                        else:
                                ch_e "Very well."         
                    else:                       
                        #low approval or not wearing pants or in public 
                        if ApprovalCheck("Emma", 1100, "LI", TabM=(4-Public)) and E_Love > E_Inbt:               
                                ch_e "I don't exactly mind you seeing. . ."
                        elif ApprovalCheck("Emma", 700, "OI", TabM=(4-Public)) and E_Obed > E_Inbt:
                                ch_e "I suppose I could. . ."
                        elif ApprovalCheck("Emma", 600, "I", TabM=(4-Public)):
                                ch_e "Why not."
                        elif ApprovalCheck("Emma", 1300, TabM=(4-Public)):
                                ch_e "Fine."
                        else: 
                                call EmmaFace("surprised")
                                $ E_Brows = "angry"
                                if Taboo > 20:
                                    ch_e "I don't think I could out here, [E_Petname]!"
                                else:
                                    ch_e "I could, but I won't, [E_Petname]!"
                                jump Emma_Clothes
                                
                                
                    $ Line = E_Panties
                    $ E_Panties = 0  
                    if E_Legs:
                        if Taboo or ApprovalCheck("Emma", 1100) or E_SeenPussy:
                            "She pulls off her [E_Legs] then pulls her [Line] off, droping them to the ground, before putting them back on." 
                            call Emma_First_Bottomless(1)
                        else:
                            "She asks you to turn around. After a few seconds, you turn back to her as she drops the [Line] to the ground."               
                    else:
                        "She pulls off her [Line] and lets them drop to the ground."
                        call Emma_First_Bottomless
                        call Statup("Emma", "Inbt", 50, 2)  
                        
                "Why don't you wear the white panties instead?" if E_Panties and E_Panties != "white panties":
                    if ApprovalCheck("Emma", 1100, TabM=(4-Public)):
                            ch_e "Ok."
                            $ E_Panties = "white panties"  
                    else:                
                            ch_e "I really don't see how that's any of your concern."
                  
                "Why don't you wear the sporty panties instead?" if E_Panties and E_Panties != "sports panties":
                    if ApprovalCheck("Emma", 1200, TabM=(4-Public)):
                            ch_e "Fine."
                            $ E_Panties = "sports panties"
                    else:
                            ch_e "I really don't see how that's any of your concern."
                            
                "Why don't you wear the lace panties instead?" if "lace panties" in E_Inventory and E_Panties and E_Panties != "lace panties":
                    if ApprovalCheck("Emma", 1300, TabM=(4-Public)):
                            ch_e "Fine."
                            $ E_Panties = "lace panties"
                    else:
                            ch_e "I really don't see how that's any of your concern."
                             
                "I like those bikini bottoms." if E_Panties != "bikini bottoms" and "bikini bottoms" in E_Inventory:
                    if bg_current == "bg pool":
                            ch_e "Fine."   
                            $ E_Panties = "bikini bottoms"         
                    else:                
                            if ApprovalCheck("Emma", 800, TabM=2):
                                ch_e "Fine."   
                                $ E_Panties = "bikini bottoms"         
                            else:                
                                ch_e "I don't know about wearing those here. . ." 
                                
                "You know, you could wear some panties with that. . ." if not E_Panties:
                    call EmmaFace("bemused", 1)
                    if (E_Love+E_Obed) <= (2* E_Inbt):
                        $ E_Mouth = "smile"
                        ch_e "I could, but won't."
                        call Statup("Emma", "Inbt", 70, 2)
                        menu:
                            "Fine by me":
                                call Statup("Emma", "Love", 90, 2)
                                call Statup("Emma", "Inbt", 70, 2)
                                jump Emma_Clothes
                            "I insist, put some on.":
                                if (E_Love+E_Obed) <= E_Inbt:
                                    call EmmaFace("angry", Eyes="side")
                                    call Statup("Emma", "Inbt", 99, 5)
                                    call Statup("Emma", "Obed", 80, -5)
                                    ch_e "How disappointing that must be for you."
                                    jump Emma_Clothes
                                else:
                                    call EmmaFace("sadside")
                                    call Statup("Emma", "Inbt", 200, -5)
                                    call Statup("Emma", "Obed", 80, 5)
                                    ch_e "If you insist."   
                    menu:
                        ch_e "If you insist. . ."
                        "How about the white ones?":
                            ch_e "Fine."
                            $ E_Panties = "white panties"
                        "How about the sporty ones?":
                            ch_e "Fine."
                            $ E_Panties = "sports panties"
                        "How about the lace ones?" if "lace panties" in E_Inventory:
                            ch_e "Fine."                
                            $ E_Panties  = "lace panties"
                "Never mind":
                    pass
        "Never mind":
            pass
    jump Emma_Clothes
    #End of Emma Underwear
       
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  
        
    menu Emma_Clothes_Misc:                     
        #Misc
        "Maybe lose the gloves." if E_Arms:
            $ E_Arms = 0
            ch_e "Ok."
        "Put your gloves on." if not E_Arms:
            $ E_Arms = 1
            ch_e "Ok."       
        "You look good with your hair flowing." if E_Hair != "wave":
            if ApprovalCheck("Emma", 600):
                ch_e "Like this?"
                $ E_Hair = "wave"
            else:
                ch_e "Yes, I do."
                
        "Maybe keep your hair straight." if E_Hair != "wet":
            if ApprovalCheck("Emma", 600):
                ch_e "You think?"
                $ E_Hair = "wet"
            else:
                ch_e "I tend to prefer it a bit more loose."
                        
        "You know, I like some nice hair down there. Maybe grow it out." if not E_Pubes and "pubes" in E_Todo:
            call EmmaFace("bemused", 1)
            ch_e "Rome wasn't built in a day. . ."
        "You know, I like some nice hair down there. Maybe grow it out." if not E_Pubes and "pubes" not in E_Todo:
            call EmmaFace("bemused", 1)
            $ Approval = ApprovalCheck("Emma", 1150, TabM=0)
            if ApprovalCheck("Emma", 850, "L", TabM=0) or (Approval and E_Love > 2 * E_Obed):               
                ch_e "If you like that sort of thing. . ."
            elif ApprovalCheck("Emma", 500, "I", TabM=0) or (Approval and E_Inbt > E_Obed):
                ch_e "I could go a bit more. . . wild."
            elif ApprovalCheck("Emma", 400, "O", TabM=0) or Approval:
                ch_e "If you insist. . ."
            else: 
                call EmmaFace("surprised")
                $ E_Brows = "angry"
                ch_e "I don't see how that's your concern, [E_Petname]."
                jump Emma_Clothes
            $ E_Todo.append("pubes")
            $ E_PubeC = 6
        
        "I like it waxed clean down there." if E_Pubes == 1:
            call EmmaFace("bemused", 1)            
            if "shave" in E_Todo:
                ch_e "Yes, yes, it's on my schedule."
            else:
                $ Approval = ApprovalCheck("Emma", 1150, TabM=0)
                
                if ApprovalCheck("Emma", 850, "L", TabM=0) or (Approval and E_Love > 2 * E_Obed):               
                    ch_e "I know you love it."
                elif ApprovalCheck("Emma", 500, "I", TabM=0) or (Approval and E_Inbt > E_Obed):
                    ch_e "I like it kept tidy."
                elif ApprovalCheck("Emma", 400, "O", TabM=0) or Approval:
                    ch_e "If you insist."
                else: 
                    call EmmaFace("surprised")
                    $ E_Brows = "angry"
                    ch_e "I don't see how that's your concern, [E_Petname]."
                    jump Emma_Clothes
                $ E_Todo.append("shave")        
        "Piercings. [[See what she looks like without them first] (locked)" if not E_SeenPussy and not E_SeenChest:
            pass
            
        "You know, you'd look really nice with some ring body piercings." if E_Pierce != "ring" and (E_SeenPussy or E_SeenChest) and "ring" not in E_Todo:
            call EmmaFace("bemused", 1)
            $ Approval = ApprovalCheck("Emma", 1350, TabM=0)
            if ApprovalCheck("Emma", 900, "L", TabM=0) or (Approval and E_Love > 2* E_Obed):   
                    ch_e "A little handhold, I assume?"
            elif ApprovalCheck("Emma", 600, "I", TabM=0) or (Approval and E_Inbt > E_Obed):
                    ch_e "I do like a nice ring. . ."
            elif ApprovalCheck("Emma", 500, "O", TabM=0) or Approval:
                    ch_e "I didn't know you were into that sort of thing."
            else: 
                    call EmmaFace("surprised")
                    $ E_Brows = "angry"
                    ch_e "Well, I'm just not ready for that sort of thing, [E_Petname]."
                    jump Emma_Clothes            
            $ E_Todo.append("ring")
        
        "You know, you'd look really nice with some barbell body piercings." if E_Pierce != "barbell" and (E_SeenPussy or E_SeenChest)and "barbell" not in E_Todo:
            call EmmaFace("bemused", 1)
            $ Approval = ApprovalCheck("Emma", 1350, TabM=0)
            if ApprovalCheck("Emma", 900, "L", TabM=0) or (Approval and E_Love > 2 * E_Obed): 
                ch_e "A little handhold, I assume?"
            elif ApprovalCheck("Emma", 600, "I", TabM=0) or (Approval and E_Inbt > E_Obed):
                ch_e "They might look nice on these. . ."
            elif ApprovalCheck("Emma", 500, "O", TabM=0) or Approval:
                ch_e "I didn't know you were into that sort of thing."
            else: 
                call EmmaFace("surprised")
                $ E_Brows = "angry"
                ch_e "Well, I'm just not ready for that sort of thing, [E_Petname]."
                jump Emma_Clothes                
            $ E_Todo.append("barbell")
            $ E_Pierce = "barbell"
            
        "You know, you'd look better without those piercings." if E_Pierce:
            call EmmaFace("bemused", 1)
            $ Approval = ApprovalCheck("Emma", 1350, TabM=0)
            if ApprovalCheck("Emma", 950, "L", TabM=0) or (Approval and E_Love > E_Obed):   
                ch_e "If they aren't working for you. . ."
            elif ApprovalCheck("Emma", 700, "I", TabM=0) or (Approval and E_Inbt > E_Obed):
                ch_e "They were being a nuisance."
            elif ApprovalCheck("Emma", 600, "O", TabM=0) or Approval:
                ch_e "I'll remove them then."
            else: 
                call EmmaFace("surprised")
                $ E_Brows = "angry"
                ch_e "Well {i}I{/i} enjoy them."
                jump Emma_Clothes            
            $ E_Pierce = 0 
        "Why don't you try on that white choker." if E_Neck != "choker":
            ch_e "Ok. . ."         
            $ E_Neck = "choker"
        "Maybe go without a collar." if E_Neck:
            ch_e "Ok. . ."         
            $ E_Neck = 0
            
        "Never mind":
            pass         
    jump Emma_Clothes
    #End of Emma Misc Wardrobe
    
return
#End Emma Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <



# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

label Emma_Clothes_Schedule(Cnt = 0):
        #Sets clothing for different days, if Cnt is 3 it's all days, 2 is TuThu, 1 is only weekends
        
        if ApprovalCheck("Emma", 1500, "LO"):
                ch_e "I'm open to suggestions."
                $ Cnt = 3
        elif ApprovalCheck("Kitty", 1200, "LO"):
                ch_e "I could let you choose a few days. . ."
                $ Cnt = 2
        elif ApprovalCheck("Emma", 1000, "LO"):
                ch_e "Perhaps when I'm off the clock. . ."
                $ Cnt = 1
        else:
                ch_e "I'd prefer to handle my own wardrobe."
                return
            
        menu:
                extend ""
                "Weekdays":
                    menu:
                        "On Monday you should wear. . ." if Cnt > 1:
                            call Emma_Clothes_ScheduleB
                            $ E_Schedule[0] = _return
                        "On Monday you should wear. . . (locked)" if Cnt <= 1:
                            pass
                            
                        "On Tuesday you should wear. . ." if Cnt > 2:
                            call Emma_Clothes_ScheduleB
                            $ E_Schedule[1] = _return        
                        "On Tuesday you should wear. . . (locked)" if Cnt <= 2:
                            pass
                            
                        "On Wednesday you should wear. . ." if Cnt > 1:
                            call Emma_Clothes_ScheduleB
                            $ E_Schedule[2] = _return
                        "On Wednesday you should wear. . . (locked)" if Cnt <= 1:
                            pass   
                            
                        "On Thursday you should wear. . ." if Cnt > 2:
                            call Emma_Clothes_ScheduleB
                            $ E_Schedule[3] = _return
                        "On Thursday you should wear. . . (locked)" if Cnt <= 2:
                            pass
                            
                        "On Friday you should wear. . ." if Cnt > 1:
                            call Emma_Clothes_ScheduleB
                            $ E_Schedule[4] = _return
                        "On Friday you should wear. . . (locked)" if Cnt <= 1:
                            pass
                        "Back":
                            pass    
                            
                "Other":
                    menu:
                        "On Saturday you should wear. . . (locked)" if Cnt < 1:
                            pass
                        "On Saturday you should wear. . ." if Cnt >= 1:
                            call Emma_Clothes_ScheduleB
                            $ E_Schedule[5] = _return
                            
                        "On Sunday you should wear. . . (locked)" if Cnt < 1:
                            pass
                        "On Sunday you should wear. . ." if Cnt >= 1:
                            call Emma_Clothes_ScheduleB
                            $ E_Schedule[6] = _return
                            
                        "In our rooms you should wear. . . (locked)" if Cnt < 1:
                            pass
                        "In our rooms you should wear. . ." if Cnt >= 1:
                            call Emma_Clothes_ScheduleB(99)
                            $ E_Schedule[9] = _return   
                            
                        "On dates you should wear. . . (locked)" if Cnt < 2:
                            pass
                        "On dates you should wear. . ." if Cnt >= 2:
                            call Emma_Clothes_ScheduleB
                            $ E_Schedule[7] = _return    
                            
                        "When teaching you should wear. . . (locked)" if Cnt < 3:
                            pass
                        "When teaching you should wear. . ." if Cnt >= 3:
                            call Emma_Clothes_ScheduleB(90)
                            $ E_Schedule[8] = _return  
                        "Back":
                            pass         
                    
                "Never mind [[Done]":
                    return        
        jump Emma_Clothes_Schedule
    
    
    
label Emma_Clothes_ScheduleB(Count = 0):
#This is called by Emma_Clothes_Schedule when setting her outfit for a given day
#If Count by the end, yes, if not count, no. If count is 99 then it's an auto-yes
            
            menu:
                "That teacher outfit.":
                    $ Count = 1
                "Your superhero outfit.":
                    $ Count = 2
                "That outfit we put together [[custom]" if E_Custom[0] or E_Custom2[0] or E_Custom3[0] or E_Custom4[0] or E_Custom5[0] or E_Custom6[0] or E_Custom7[0] or E_Custom8[0] or E_Custom9[0]:
                            menu:
                                ch_e "Which were you thinking?"
                                "The first one. (locked)" if not E_Custom[0]:
                                    pass
                                "The first one." if E_Custom[0]:
                                    if E_Custom[0] == 2 or Count == 99:
                                        $ Count = 3
                                    else:
                                        ch_e "I said I'm not wearing that one in public."
                                        
                                "The second one. (locked)" if not E_Custom2[0]:
                                    pass
                                "The second one." if E_Custom2[0]:
                                    if E_Custom2[0] == 2 or Count == 99:
                                        $ Count = 5
                                    else:
                                        ch_e "I said I'm not wearing that one in public."
                                        
                                "The third one. (locked)" if not E_Custom3[0]:
                                    pass
                                "The third one." if E_Custom3[0]:
                                    if E_Custom3[0] == 2 or Count == 99:
                                        $ Count = 6
                                    else:
                                        ch_e "I said I'm not wearing that one in public."
                                        
                                "The fourth one. (locked)" if not E_Custom4[0]:
                                    pass
                                "The fourth one." if E_Custom4[0]:
                                    if E_Custom4[0] == 2 or Count == 99:
                                        $ Count = 15
                                    else:
                                        ch_e "I said I'm not wearing that one in public."
                                        
                                "The fifth one. (locked)" if not E_Custom5[0]:
                                    pass
                                "The fifth one." if E_Custom5[0]:
                                    if E_Custom5[0] == 2 or Count == 99:
                                        $ Count = 16
                                    else:
                                        ch_e "I said I'm not wearing that one in public."
                                        
                                "The sixth one. (locked)" if not E_Custom6[0]:
                                    pass
                                "The sixth one." if E_Custom6[0]:
                                    if E_Custom6[0] == 2 or Count == 99:
                                        $ Count = 17
                                    else:
                                        ch_e "I said I'm not wearing that one in public."
                                        
                                "The seventh one. (locked)" if not E_Custom7[0]:
                                    pass
                                "The seventh one." if E_Custom7[0]:
                                    if E_Custom7[0] == 2 or Count == 99:
                                        $ Count = 18
                                    else:
                                        ch_e "I said I'm not wearing that one in public."
                                        
                                "The eighth one. (locked)" if not E_Custom8[0]:
                                    pass
                                "The eighth one." if E_Custom8[0]:
                                    if E_Custom8[0] == 2 or Count == 99:
                                        $ Count = 19
                                    else:
                                        ch_e "I said I'm not wearing that one in public."
                                        
                                "The ninth one. (locked)" if not E_Custom9[0]:
                                    pass
                                "The ninth one." if E_Custom9[0]:
                                    if E_Custom9[0] == 2 or Count == 99:
                                        $ Count = 20
                                    else:
                                        ch_e "I said I'm not wearing that one in public."
                                        
                                "Never mind":
                                    pass
                "Your gym clothes.":
                    if Count == 90:
                        ch_e "Not in class, [E_Petname]."
                        $ Count = 0
                    else:
                        $ Count = 4
                "Your sleepwear.":
                    if Count != 99:
                        ch_e "I don't think that would be appropriate, [E_Petname]."
                        $ Count = 0
                    else:
                        $ Count = 7
                "Whatever you like.":
                    pass
                    
            if Count:
                        ch_e "Very well."
            else:
                        ch_e "I'll wear something else instead."
            return Count    
#End Emma Clothes Scheduling Check


label E_AltClothes(Outfit=8):
        #1 = "teacher", 2 = "costume"
        #3 = "custom1", 5 = "custom2", 6 = "custom3", 7 = "sleep", 4 = "gym", 10 = "swimwear"
        #This selects her outfit when teaching if 8
        #This selects her private outfit if 9
        
        if E_Schedule[Outfit] == 1 or not E_Schedule[Outfit]:
                    $ E_Outfit = "teacher"
        elif E_Schedule[Outfit] == 2:
                    $ E_Outfit = "costume"
        elif E_Schedule[Outfit] == 15:
                    $ E_Outfit = "custom4"
        elif E_Schedule[Outfit] == 16:
                    $ E_Outfit = "custom5"
        elif E_Schedule[Outfit] == 17:
                    $ E_Outfit = "custom6"
        elif E_Schedule[Outfit] == 18:
                    $ E_Outfit = "custom7"
        elif E_Schedule[Outfit] == 19:
                    $ E_Outfit = "custom8"
        elif E_Schedule[Outfit] == 20:
                    $ E_Outfit = "custom9"
        elif E_Schedule[Outfit] == 3:
                    $ E_Outfit = "custom1"
        elif E_Schedule[Outfit] == 5:
                    $ E_Outfit = "custom2"
        elif E_Schedule[Outfit] == 6:
                    $ E_Outfit = "custom3"
        elif E_Schedule[Outfit] == 7:
                    $ E_Outfit = "sleep"
        elif E_Schedule[Outfit] == 4:
                    $ E_Outfit = "gym"
        elif E_Schedule[Outfit] == 10:
                    $ E_Outfit = "swimwear"
        return
  
label E_Private_Outfit:
    #sets Emma's private outfit in private
    if "comfy" in E_RecentActions or "comfy" in E_Traits or E_Outfit == E_Schedule[9]:
            call E_AltClothes(9)
            call EmmaOutfit(Changed=1)
    elif "no comfy" in E_RecentActions:
            pass        
    elif (2 * E_Inbt) >= (E_Love + E_Obed +100):
            # if her inhibition is much higher than her obedience to you. . .            
            ch_e "I'll be just a moment. . ."
            ch_e "I'll just slip into something more comfortable. . ."
            call E_AltClothes(9)
            call EmmaOutfit(Changed=1)
            $ E_RecentActions.append("comfy")
    else:
            ch_e "I'll be just a moment. . ."
            menu: 
                ch_e "Would you like me to change into something more comfortable?"
                "Sure.":
                    ch_e "Lovely. . ."
                    call E_AltClothes(9)
                    call EmmaOutfit(Changed=1)
                    $ E_RecentActions.append("comfy")
                "No thanks.":
                    ch_e "Very well."       
                    $ E_RecentActions.append("no comfy")             
    return


label Emma_Custom_Out(Custom = 3, Shame = 0, Agree = 1):
            #If Custom1 = 3, if custom2 = 5, if custom3 = 6
            
            call EmmaFace("sexy", 1)
            if "exhibitionist" in E_Traits:  
                        ch_e "Hmm, I'm getting excited. . ."  
                        if Custom == 5 and E_Custom2[0] == 2:
                            $ E_Outfit = "custom2"                    
                            $ E_Shame = E_OutfitShame[5]
                        elif Custom == 15 and E_Custom4[0] == 2:
                                    $ E_Outfit = "custom4"
                                    $ E_Shame = E_OutfitShame[Custom]
                        elif Custom == 16 and E_Custom5[0] == 2:
                                    $ E_Outfit = "custom5"
                                    $ E_Shame = E_OutfitShame[Custom]
                        elif Custom == 17 and E_Custom6[0] == 2:
                                    $ E_Outfit = "custom6"
                                    $ E_Shame = E_OutfitShame[Custom]
                        elif Custom == 18 and E_Custom7[0] == 2:
                                    $ E_Outfit = "custom7"
                                    $ E_Shame = E_OutfitShame[Custom]
                        elif Custom == 19 and E_Custom8[0] == 2:
                                    $ E_Outfit = "custom8"
                                    $ E_Shame = E_OutfitShame[Custom]
                        elif Custom == 20 and E_Custom9[0] == 2:
                                    $ E_Outfit = "custom9"
                                    $ E_Shame = E_OutfitShame[Custom]
                        elif Custom == 6 and E_Custom3[0] == 2:
                            $ E_Outfit = "custom3"                    
                            $ E_Shame = E_OutfitShame[6]
                        else: #if custom 1:
                            $ E_Outfit = "custom1"                    
                            $ E_Shame = E_OutfitShame[3]            
                        return    
            
            if Custom == 5 and E_Custom2[0] == 2:
                        $ E_Outfit = "custom2"   
            elif Custom == 15 and E_Custom4[0] == 2:
                        $ E_Outfit = "custom4"
            elif Custom == 16 and E_Custom5[0] == 2:
                        $ E_Outfit = "custom5"
            elif Custom == 17 and E_Custom6[0] == 2:
                        $ E_Outfit = "custom6"
            elif Custom == 18 and E_Custom7[0] == 2:
                        $ E_Outfit = "custom7"
            elif Custom == 19 and E_Custom8[0] == 2:
                        $ E_Outfit = "custom8"
            elif Custom == 20 and E_Custom9[0] == 2:
                        $ E_Outfit = "custom9"
            elif Custom == 6 and E_Custom3[0] == 2:
                        $ E_Outfit = "custom3"   
            elif E_Custom[0] == 2: #if custom 1:
                        $ E_Outfit = "custom1"   
            else: #no
                        $ Agree = 0
             
            if Agree:                              
                        #she's decided to wear this out.
                        $ E_Shame = E_OutfitShame[Custom]          
                        if E_OutfitShame[Custom] >= 50:
                            ch_e "This is. . . kinda slutty. . ."
                        elif E_OutfitShame[Custom] >= 25:
                            ch_e "I'm not really comfortable with this one. . ."
                        elif E_OutfitShame[Custom] >= 15:
                            call EmmaFace("bemused", 1)
                            ch_e "I'll give it a shot. . ."
                        else:
                            ch_e "Yeah, I like that one too."
            else:
                        #She's decided not to wear this out
                        if E_OutfitShame[Custom] >= 50:
                            call EmmaFace("angry", 1)
                            ch_e "You have GOT to be kidding me here."
                        elif E_OutfitShame[Custom] >= 25:
                            call EmmaFace("angry", 1)
                            ch_e "This is just between us."
                        else:
                            call EmmaFace("surprised", 1)
                            ch_e "I can't wear this out!"  
            return
# End Emma Custom Out
                                
                                
label Emma_OutfitShame(Custom = 3, Check = 0, Count = 0, Tempshame = 50, Agree = 1): 
            #Custom determines which custom outfit is being checked against.    
            #If Custom1 = 3, if custom2 = 5, if custom3 = 6, if gym = 7, if private = 9, if swimsuit = 10, if 20, quickcheck
            #if not a check, then it is only applied if it's in a taboo area
            # Tempshame is a throwaway value, 0-50, Agree is whether she will wear it out, 2 if yes, 1 if only around you.
            
            if not Check and not Taboo and Custom != 20:
                #if this is not a custom check and you're in a safe space,
                if E_Schedule[9]:
                    #if there is a "private outfit" set, ask to change.
                    call E_Private_Outfit
                return
                        
            #If she's wearing a bra of some kind
            if Custom == 20 and E_Uptop: 
                $ Count = 0
            elif E_Chest == "corset":  
                $ Count = 15
            elif IsOutfitModdedEmma("Chest"):
                $ Count = Mod_Emma_OutfitShame("Chest")
            elif E_Chest == "sports bra":
                $ Count = 15
            elif E_Chest == "bikini top":
                $ Count = 15
            elif E_Chest == "bra":
                $ Count = 10   
            elif E_Chest == "lace bra":
                $ Count = 5
            else:     #E_Chest == 0
                if E_Pierce:
                    $ Count = -5
                else:
                    $ Count = 0
                    
            #If she's wearing an overshirt
            if Custom == 20 and E_Uptop: 
                $ Count = 0
            elif IsOutfitModdedEmma("Over"):                                             
                $ Count += Mod_Emma_OutfitShame("Over")                                             
            elif E_Over == "jacket":                                             
                $ Count += 15
            elif E_Over == "towel":      
                $ Count += 5
            elif E_Over == "nighty":      
                $ Count += 5
            #else: nothing    
            
            call EmmaFace("sexy", 0)
            if Custom == 9:
                        #It's for private only
                        pass
            elif Count >= 20:
                        $ Count = 20
                        if Check:
                            ch_e "This is a fashionable top."
            elif not Check:
                        pass
            elif Count >= 10: 
                        if ApprovalCheck("Emma", 1200, TabM=0) or ApprovalCheck("Emma", 500, "I", TabM=0):  
                            ch_e "A bit daring. . ."        
                        else:
                            ch_e "I'm not sure about this top."
            elif Count >= 5:
                        if ApprovalCheck("Emma", 2300, TabM=0) or ApprovalCheck("Emma", 800, "I", TabM=0):  
                            ch_e "I typically cover a {i}bit{/i} more than this."        
                        else:        
                            call EmmaFace("startled", 1)
                            ch_e "This is a bit more cleavage than even I'm comforable with."
            elif (ApprovalCheck("Emma", 2700, TabM=0) or ApprovalCheck("Emma", 950, "I", TabM=0)):  
                        ch_e "Aren't my assets a bit. . . exposed here?"        
            else:
                        call EmmaFace("bemused", 1)
                        ch_e "This is considerably more cleavage than even I'm comforable with."
             
            $ Tempshame -= Count                  #Set Outfit shame for the upper half    
            $ Count = 0         
            
            if E_Legs or E_Panties:          
                if PantsNum("Emma") >= 5:              
                    #If wearing pants
                    if E_Panties:
                            $ Count = 30
                    else:
                            # if commando
                            $ Count = 25                
                elif IsOutfitModdedEmma("Panties"):      #If wearing only sports panties
                    $ Count = Mod_Emma_OutfitShame("Panties")      #If wearing only sports panties
                elif E_Panties == "sports panties":      #If wearing only sports panties
                    $ Count = 20           
                elif E_Panties == "bikini bottoms":      #If wearing only bikini bottoms
                    $ Count = 15       
                elif E_Panties == "white panties":      #If wearing only white panties
                    $ Count = 10
                elif E_Panties == "lace panties":       #If wearing only lace panties
                    $ Count = 5              
                #else: 0
                
                if HoseNum("Emma") >= 10:
                    # if she's wearing full coverage hose, it's at least 25
                    $ Count = 25 if Count < 25 else Count
                    
                if E_Over == "towel":         
                    #If wearing a Towel it's at least 5
                    $ Count = 5 if Count < 5 else Count
                            
            if not Check:
                        #If this isn't a custom check, skip this dialog stuff
                        pass
            elif Custom == 9:
                        #It's for private only
                        pass
            elif Count >= 20:
                        if PantsNum("Emma") > 5:
                            ch_e "and these pants always did suit me."
                        elif PantsNum("Emma") >= 5:
                            ch_e "and this skirt always did suit me."
                        elif HoseNum("Emma") >= 10:
                            ch_e "I guess these [E_Hose] will work fine."
                        elif E_Over == "towel":
                            ch_e "I'm unsure about wearing a towel out, [E_Petname]. . ."
                        else:
                            ch_e "I probably could wear something more downstairs, [E_Petname]. . ."
                        if not E_Panties:
                            if ApprovalCheck("Emma", 500, "I", TabM=0):
                                ch_e "I do enjoy going without panties."
                            else:
                                ch_e "I don't know about going without panties in this situation."
                    
            elif Count >= 10:
                if ApprovalCheck("Emma", 2000, TabM=0) or ApprovalCheck("Emma", 700, "I", TabM=0):
                        ch_e "I hope you don't expect me to wear this out. . ."        
                else:
                        call EmmaFace("angry", 1)
                        ch_e "I don't know about wearing this outside. . ."                
            elif (ApprovalCheck("Emma", 2500, TabM=0) or ApprovalCheck("Emma", 800, "I", TabM=0)):  
                        ch_e "This really tests my limits."        
            else:
                        ch_e "I'll need to put something else on to leave the room though."
                
            $ Tempshame -= Count                  #Set Outfit shame for the lower half
            
            if Check:
                    #if this is a custom outfit check
                    if Custom == 7:
                        ch_p "So would you work out in that?"
                    elif Custom == 9:
                        ch_p "So would you sleep in that?"
                    else:
                        ch_p "So would you wear that outside?"  
                                         
                    call EmmaFace("sexy", 0)
                    if Taboo >= 40: #E_Loc != "bg player" and E_Loc != "bg emma": 
                            call EmmaFace("confused",1)
                            $ E_Mouth = "smile"
                            "She glances around."
                            ch_e "Is that a trick question?" 
                    elif "exhibitionist" in E_Traits and Tempshame <= 20:        
                            ch_e "The thought of it gets me moist. . ."
                            call Statup("Emma", "Lust", 80, 10)
                    elif Tempshame <= 5:
                            call EmmaFace("smile")
                            ch_e "Yes, it's a fine choice."
                    elif Tempshame <= 15 and (ApprovalCheck("Emma", 1700, TabM=0, C = 0) or ApprovalCheck("Emma", 400, "I", TabM=0, C = 0)):        
                            ch_e "Rather daring, how could I resist?"
                    elif Custom == 9:
                            #if it's sleepwear      
                            call EmmaFace("bemused", 1)
                            if Tempshame >= 30:
                                ch_e "You understand I only wear this sort of thing in private."  
                            else:
                                ch_e "It is a comfortable outfit."   
                    elif Tempshame <= 15:  
                            call EmmaFace("bemused", 1)
                            ch_e "Rather too daring, don't you think?."
                            $ Agree = 0
                            
                    elif Tempshame >= 15 and "public" not in E_History:                 #maybe remove later     
                            ch_e "I doubt I could get away with this in public, [E_Petname]."
                            $ Agree = 0
                        
                    elif Custom == 10 and Tempshame <= 20:  
                        #if it's a swimsuit. . .
                        call EmmaFace("bemused", 1)
                        ch_e "Fine, this is decent swimwear. . ."
                    elif Tempshame <= 25 and (ApprovalCheck("Emma", 2300, TabM=0, C = 0) or ApprovalCheck("Emma", 700, "I", TabM=0, C = 0)):
                            ch_e "This is particularly inappropriate. . . in the best ways."
                    elif Tempshame <= 25:
                            call EmmaFace("angry", 1)
                            ch_e "I don't believe even I could pull off this look, [E_Petname]."
                            $ Agree = 0
                    elif (ApprovalCheck("Emma", 2500, TabM=0, C = 0) or ApprovalCheck("Emma", 800, "I", TabM=0, C = 0)):
                            call EmmaFace("bemused", 1)
                            ch_e "This look certainly pushes the boundaries."
                    else:
                            call EmmaFace("angry", 1)
                            ch_e "Even I can't pull this off."
                            $ Agree = 0
                        
                    $ E_OutfitShame[Custom] = Tempshame                     
                    if Custom == 5:
                            $ E_Custom2[1] = E_Arms  
                            $ E_Custom2[2] = E_Legs 
                            $ E_Custom2[3] = E_Over
                            $ E_Custom2[4] = E_Neck 
                            $ E_Custom2[5] = E_Chest 
                            $ E_Custom2[6] = E_Panties
                            $ E_Custom2[7] = E_Boots
                            $ E_Custom2[8] = E_Hair
                            $ E_Custom2[9] = E_Hose
                            $ E_Custom2[0] = 2 if Agree else 1
                            call Clothing_Schedule_Check("Emma",5,1) 
#MOD CUSTOM OUTFITS OUTFITSHAME
                    elif Custom == 20:
                            $ E_Custom9[1] = E_Arms  
                            $ E_Custom9[2] = E_Legs 
                            $ E_Custom9[3] = E_Over
                            $ E_Custom9[4] = E_Neck 
                            $ E_Custom9[5] = E_Chest 
                            $ E_Custom9[6] = E_Panties
                            $ E_Custom9[7] = E_Boots
                            $ E_Custom9[8] = E_Hair
                            $ E_Custom9[9] = E_Hose
                            $ E_Custom9[0] = 2 if Agree else 1
                            call Clothing_Schedule_Check("Emma",Custom,1) 
                    elif Custom == 19:
                            $ E_Custom8[1] = E_Arms  
                            $ E_Custom8[2] = E_Legs 
                            $ E_Custom8[3] = E_Over
                            $ E_Custom8[4] = E_Neck 
                            $ E_Custom8[5] = E_Chest 
                            $ E_Custom8[6] = E_Panties
                            $ E_Custom8[7] = E_Boots
                            $ E_Custom8[8] = E_Hair
                            $ E_Custom8[9] = E_Hose
                            $ E_Custom8[0] = 2 if Agree else 1
                            call Clothing_Schedule_Check("Emma",Custom,1) 
                    elif Custom == 18:
                            $ E_Custom7[1] = E_Arms  
                            $ E_Custom7[2] = E_Legs 
                            $ E_Custom7[3] = E_Over
                            $ E_Custom7[4] = E_Neck 
                            $ E_Custom7[5] = E_Chest 
                            $ E_Custom7[6] = E_Panties
                            $ E_Custom7[7] = E_Boots
                            $ E_Custom7[8] = E_Hair
                            $ E_Custom7[9] = E_Hose
                            $ E_Custom7[0] = 2 if Agree else 1
                            call Clothing_Schedule_Check("Emma",Custom,1) 
                    elif Custom == 17:
                            $ E_Custom6[1] = E_Arms  
                            $ E_Custom6[2] = E_Legs 
                            $ E_Custom6[3] = E_Over
                            $ E_Custom6[4] = E_Neck 
                            $ E_Custom6[5] = E_Chest 
                            $ E_Custom6[6] = E_Panties
                            $ E_Custom6[7] = E_Boots
                            $ E_Custom6[8] = E_Hair
                            $ E_Custom6[9] = E_Hose
                            $ E_Custom6[0] = 2 if Agree else 1
                            call Clothing_Schedule_Check("Emma",Custom,1) 
                    elif Custom == 16:
                            $ E_Custom5[1] = E_Arms  
                            $ E_Custom5[2] = E_Legs 
                            $ E_Custom5[3] = E_Over
                            $ E_Custom5[4] = E_Neck 
                            $ E_Custom5[5] = E_Chest 
                            $ E_Custom5[6] = E_Panties
                            $ E_Custom5[7] = E_Boots
                            $ E_Custom5[8] = E_Hair
                            $ E_Custom5[9] = E_Hose
                            $ E_Custom5[0] = 2 if Agree else 1
                            call Clothing_Schedule_Check("Emma",Custom,1) 
                    elif Custom == 15:
                            $ E_Custom4[1] = E_Arms  
                            $ E_Custom4[2] = E_Legs 
                            $ E_Custom4[3] = E_Over
                            $ E_Custom4[4] = E_Neck 
                            $ E_Custom4[5] = E_Chest 
                            $ E_Custom4[6] = E_Panties
                            $ E_Custom4[7] = E_Boots
                            $ E_Custom4[8] = E_Hair
                            $ E_Custom4[9] = E_Hose
                            $ E_Custom4[0] = 2 if Agree else 1
                            call Clothing_Schedule_Check("Emma",Custom,1) 
                    elif Custom == 6:
                            $ E_Custom3[1] = E_Arms  
                            $ E_Custom3[2] = E_Legs 
                            $ E_Custom3[3] = E_Over
                            $ E_Custom3[4] = E_Neck 
                            $ E_Custom3[5] = E_Chest 
                            $ E_Custom3[6] = E_Panties
                            $ E_Custom3[7] = E_Boots
                            $ E_Custom3[8] = E_Hair
                            $ E_Custom3[9] = E_Hose
                            $ E_Custom3[0] = 2 if Agree else 1
                            call Clothing_Schedule_Check("Emma",6,1) 
                    elif Custom == 7 and Agree:
                            $ E_Gym[1] = E_Arms  
                            $ E_Gym[2] = E_Legs 
                            $ E_Gym[3] = E_Over
                            $ E_Gym[4] = E_Neck 
                            $ E_Gym[5] = E_Chest 
                            $ E_Gym[6] = E_Panties
                            $ E_Gym[7] = E_Boots
                            $ E_Gym[8] = E_Hair
                            $ E_Gym[9] = E_Hose
                            $ E_Gym[0] = 2   
                            call Clothing_Schedule_Check("Emma",4,1) 
                    elif Custom == 9 and Agree:
                            $ E_Sleepwear[1] = E_Arms  
                            $ E_Sleepwear[2] = E_Legs 
                            $ E_Sleepwear[3] = E_Over
                            $ E_Sleepwear[4] = E_Neck 
                            $ E_Sleepwear[5] = E_Chest 
                            $ E_Sleepwear[6] = E_Panties
                            $ E_Sleepwear[7] = E_Boots
                            $ E_Sleepwear[8] = E_Hair
                            $ E_Sleepwear[9] = E_Hose
                            $ E_Sleepwear[0] = 2 if Agree else 1   
                    elif Custom == 10:            
                            $ E_Swim[1] = E_Arms  
                            $ E_Swim[2] = E_Legs 
                            $ E_Swim[3] = E_Over
                            $ E_Swim[4] = E_Neck 
                            $ E_Swim[5] = E_Chest 
                            $ E_Swim[6] = E_Panties
                            $ E_Swim[8] = E_Hair
                            $ E_Swim[9] = E_Hose
                            $ E_Swim[0] = 2 if Agree else 1                          
                    else: #Typically Custom == 3
                            $ E_Custom[1] = E_Arms  
                            $ E_Custom[2] = E_Legs 
                            $ E_Custom[3] = E_Over
                            $ E_Custom[4] = E_Neck 
                            $ E_Custom[5] = E_Chest 
                            $ E_Custom[6] = E_Panties
                            $ E_Custom[7] = E_Boots
                            $ E_Custom[8] = E_Hair
                            $ E_Custom[9] = E_Hose
                            $ E_Custom[0] = 2 if Agree else 1
                            call Clothing_Schedule_Check("Emma",3,1)  
                    #End check  
            elif Taboo <= 20:
                # halves shame level if she's comfortable
                $ Tempshame /= 2  
                
            $ E_Shame = Tempshame
            if Custom == 20:
                # This returns the scene if it's a check Shame adjustment
                return
                
            if Check:
                    pass
            elif "exhibitionist" in E_Traits: 
                    #If she's an exhibitionist
                    pass
            elif Tempshame <= 5:
                    #If the outfit is very tame
                    pass
            elif E_Over == "towel" and E_Loc == "bg showerroom": 
                    #If she's in a towel but it's appropriate
                    pass
            elif Tempshame <= 15 and (ApprovalCheck("Emma", 1600) or ApprovalCheck("Emma", 550, "I")):
                    #If the outfit is hot but she's ok     
                    pass
            elif Tempshame <= 20 and E_Loc == "bg dangerroom": 
                    #If the outfit is light but she's in the gym
                    pass
            elif Tempshame <= 20 and (ApprovalCheck("Emma", 1800) or ApprovalCheck("Emma", 650, "I")):
                    #If the outfit is sexy but she's cool with that
                    pass
            elif Tempshame <= 25 and (ApprovalCheck("Emma", 2200) or ApprovalCheck("Emma", 700, "I")):
                    #If the outfit is sexy but she's cool with that
                    pass
            elif (ApprovalCheck("Emma", 2500) or ApprovalCheck("Emma", 900, "I")):
                    #If the outfit is very scandelous but she's ok with that      
                    pass
            elif Custom == 9 and not Taboo:
                    pass
            else:
                    ch_e "I'm afraid I'll have to change, one moment."
                    $ E_Outfit = "teacher"
                    $ E_Water = 0
                    call EmmaOutfit(Changed = 1) 
                    ch_e "Sorry for the wait."
                    
            return        

#End Emma Custom clothes check.
    
# start emma hungry //////////////////////////////////////////////////////////
label Emma_Hungry:
    if E_Chat[3]:
        ch_e "I do enjoy your taste. . ."
    elif E_Chat[2]:
        ch_e "You know, that serum of yours has a rather. . . familiar taste to it."
    else:
        ch_e "I do enjoy your taste. . ."
    $ E_Traits.append("hungry")
return


# end emma hungry //////////////////////////////////////////////////////////

    
# Start Emma first Les / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Emma_First_Les(Silent = 0, Undress = 0, GirlsNum = 0): #checked when she engages in a les scene  ## call Emma_First_Les(0,1)
    if E_Les:
        return
    
    $ E_Les += 1
    $ E_RecentActions.append("lesbian")        
    call Statup("Emma", "Inbt", 30, 2) 
    call Statup("Emma", "Inbt", 90, 1)
    
    if not Silent: 
        #example previous line: Line + " and cups " + Primary + "'s breasts in her delicate hands" 
        "Emma's head jerks up and she looks at what [Partner] is doing. [Partner] pauses and glances up at her with a mischievous grin." 
        ch_e "I, um, I haven't done that sort of thing before."
        if Partner == "Rogue":
                if R_Les:
                    ch_r "Neither have I Sugar, but it seemed like fun."
                else:
                    ch_r "It's all right Sugar, I'll take care of you."
        if E_LikeRogue >= 60 and ApprovalCheck("Emma", (1500-(10*E_Les)-(10*(E_LikeRogue-60)))): #If she likes both of you a lot, threeway
                $ State = "threeway"
        elif ApprovalCheck("Emma", 1000): #If she likes you well enough, Hetero
                $ State = "hetero"            
        elif E_LikeRogue >= 70: #if she doesn't like you but likes Rogue, lesbian
                $ State = "lesbian"
        
        
        
        
        
        if "cockout" in P_RecentActions:
                call EmmaFace("down", 2)  
                if GirlsNum:
                    "Emma also glances down at your cock"
                else:
                    "Emma glances down at your exposed cock"
        elif Undress:
                "You strip nude."
        else:
                "You whip your cock out."
        $ P_RecentActions.append("cockout") 
        
        if Taboo and not ApprovalCheck("Emma", 1500):
                call EmmaFace("surprised", 2)  
                ch_e "Um, you should[E_like]put that away in public."
                call EmmaFace("bemused", 1)  
                if E_SeenPeen == 1: 
                    ch_e "Or[E_like]maybe. . ."
                    call Statup("Emma", "Love", 90, 15)                
                    call Statup("Emma", "Obed", 50, 20)
                    call Statup("Emma", "Inbt", 60, 35)  
                    
        elif E_SeenPeen > 10:
                return    
        elif ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "L"):
                call EmmaFace("sly",1) 
                if E_SeenPeen == 1: 
                    call EmmaFace("surprised",2)  
                    ch_e "That's. . . impressive."
                    call EmmaFace("bemused",1)  
                    call Statup("Emma", "Love", 90, 3) 
                elif E_SeenPeen == 2:  
                    ch_e "I can't get over that."               
                    call Statup("Emma", "Obed", 50, 7) 
                elif E_SeenPeen == 5: 
                    ch_e "There it is."
                    call Statup("Emma", "Inbt", 60, 5)  
                elif E_SeenPeen == 10: 
                    ch_e "So beautiful."
                    call Statup("Emma", "Obed", 80, 10)
                    call Statup("Emma", "Inbt", 60, 3)  
        else:
                call EmmaFace("sad",1) 
                if E_SeenPeen == 1: 
                    call EmmaFace("perplexed",1 ) 
                    ch_e "Well that happened. . ."
                    call Statup("Emma", "Obed", 50, 7)
                    call Statup("Emma", "Inbt", 60, 3)  
                elif E_SeenPeen < 5: 
                    call EmmaFace("sad",0) 
                    ch_e "Huh."
                    call Statup("Emma", "Inbt", 60, 2)  
                elif E_SeenPeen == 10: 
                    ch_e "[E_Like]put that away."               
                    call Statup("Emma", "Obed", 50, 7)
                    call Statup("Emma", "Inbt", 60, 3)  
    
    else: #Silent mode
                $ P_RecentActions.append("cockout") 
                if E_SeenPeen > 10:
                    return
                elif ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "L"):
                        if E_SeenPeen == 1: 
                            call Statup("Emma", "Love", 90, 3) 
                        elif E_SeenPeen == 2:              
                            call Statup("Emma", "Obed", 50, 7) 
                        elif E_SeenPeen == 5: 
                            call Statup("Emma", "Inbt", 60, 5)  
                        elif E_SeenPeen == 10: 
                            call Statup("Emma", "Love", 90, 10)  
                else:
                        if E_SeenPeen == 1: 
                            call Statup("Emma", "Obed", 50, 7)
                            call Statup("Emma", "Inbt", 60, 3)  
                        elif E_SeenPeen < 5: 
                            call Statup("Emma", "Inbt", 60, 2)  
                        elif E_SeenPeen == 10:              
                            call Statup("Emma", "Obed", 50, 7)
                            call Statup("Emma", "Inbt", 60, 3) 
                            
    if E_SeenPeen == 1:            
        call Statup("Emma", "Love", 90, 10)                
        call Statup("Emma", "Obed", 90, 25)
        call Statup("Emma", "Inbt", 60, 20) 
        call Statup("Emma", "Lust", 200, 5)
    
    return
# End Emma first Les / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /   
    
label Emma_Tits_Up:
    $ E_Tits = 1
    if Emma_Arms == 1:
        pass    
    elif E_Chest == "corset":
        pass
    else:
        #if all checks fail,
        $ E_Tits = 0    
    return