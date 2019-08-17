# star Laura chat interface
label Laura_Chat_Set(Preset=0):
    if "met" not in L_History:
            "Who?"
            return    
    if "Laura" not in Digits and L_Loc != bg_current and "Laura" not in Nearby:
            "You don't have her number."
            return
    if Preset:   
            ch_p "Hey [LauraName]. . ."
            call Shift_Focus("Laura")
            if L_Loc != bg_current:
                        show Cellphone at SpriteLoc(StageLeft)
            else:
                        hide Cellphone            
            if Preset == "chat":
                    $ renpy.pop_call() #removes the call to chat subroutine
                    $ renpy.pop_call() #This removes the callback to the previous chat session
            elif Preset == "settings":
                    $ renpy.pop_call() #This removes the callback to the previous chat session
                    $ renpy.pop_call() #this removes the callback to the previous settings menu testing. . .
                    call Laura_Settings  
            elif Preset == "wardrobe":
                    $ renpy.pop_call() #This removes the callback to the previous chat session
                    $ renpy.pop_call() #this removes the callback to the previous settings menu
                    $ renpy.pop_call() #this removes the callback to the previous settings menu testing. . .
                    ch_p "I wanted to talk about your outfit. . ."
                    if Taboo:
                            if "exhibitionist" in L_Traits:
                                ch_l "Yes? . ."  
                            elif ApprovalCheck("Laura", 900, TabM=4) or ApprovalCheck("Laura", 400, "I", TabM=3): 
                                ch_l "I don't think I'm supposed to undress around here. . ."
                            else:
                                ch_l "I don't think I'm supposed to undress around here. . ."
                                ch_l "Can we talk about this in our rooms?"
                                jump Laura_Chat
                            call Laura_Clothes
                    elif ApprovalCheck("Laura", 600, "L") or ApprovalCheck("Laura", 300, "O"):
                                ch_l "Oh? What about them?"
                                call Laura_Clothes
                    else:
                                ch_l "I don't think about my clothes much."
                                ch_l "You shouldn't either."   
            #end preset menu
                 
                        
label Laura_Chat:
    call LauraFace    
    call Shift_Focus("Laura")
    if L_Loc != bg_current:
                show Cellphone at SpriteLoc(StageLeft)
    else:
                hide Cellphone
    if "caught" in L_RecentActions:
                ch_l "I think we should lie low for a bit."
                return
    if "angry" in L_RecentActions:
                ch_l "You don't want to be around me right now."
                return
    menu:
        ch_l "Yeah?"
        "Come on over." if L_Loc != bg_current:
                    if "Laura" in Nearby and bg_current != "bg showerrroom":
                        call Swap_Nearby("Laura")            
                    elif Room_Full():
                        "I don't think there would be room."
                        call Dismissed
                    else:
                            call Laura_Summon    
        "Ask Laura to leave" if L_Loc == bg_current:
                    call Laura_Dismissed    
                    return
        
        "Flirt with her." if not L_Chat[5]:
                    call Laura_Flirt               
        "Flirt with her. (locked)" if L_Chat[5]:  
                    pass
            
        "Sex Menu" if L_Loc == bg_current:
                    if L_Love >= L_Obed:   
                        ch_p "Did you want to fool around?"  
                    else: 
                        ch_p "I want to get naughty."
                    if "angry" in L_RecentActions:  
                        ch_l "Bad idea right now."
                    elif ApprovalCheck("Laura", 600, "LI"):
                        call LauraFace("sexy")
                        ch_l "Cool."
                        call Laura_SexMenu
                        return
                    elif ApprovalCheck("Laura", 400, "OI"):
                        ch_l "Yes, [L_Petname]."
                        call Laura_SexMenu
                        return
                    else:
                        ch_l "No thanks, [L_Petname]."          
                          
        "I just wanted to talk. . .":
                    call Laura_Chitchat   
                    
        "Laura's settings":
                    ch_p "Let's talk about you."
                    call Laura_Settings   
        
        "Relationship status":
                    ch_p "Could we talk about us?"  
                    if "relationship" in L_DailyActions:
                        ch_l "I need some time to. . .  process."
                    elif L_Loc == bg_current:
                        call Laura_Relationship
                    else:
                        ch_l "Sounds heavy."
                        ch_l "Maybe later when we're face to face?"
                        
        "Could I get your number?" if "Laura" not in Digits:
                    if ApprovalCheck("Laura", 400, "L") or ApprovalCheck("Laura", 200, "I"):
                        ch_l "Oh, sure."
                        $ Digits.append("Laura") 
                    elif ApprovalCheck("Laura", 200, "O"):
                        ch_l "I guess."             
                        $ Digits.append("Laura")
                    else:
                        ch_l "Um, probably not."  
                        
        "Gifts" if L_Loc == bg_current:
                    ch_p "I'd like to give you something."
                    call Laura_Gifts
                        
        "Add her to party" if "Laura" not in Party and L_Loc == bg_current:
                    ch_p "Could you follow me for a bit?"
                    if ApprovalCheck("Laura", 650):
                        $ Party.append("Laura")
                        ch_l "Where to?"
                        return
                    elif not ApprovalCheck("Laura", 400):
                        ch_l "No."
                    else:
                        ch_l "I'd rather not."
        "Disband party" if "Laura" in Party: 
                    ch_p "Ok, you can leave if you prefer."
                    $ Party.remove("Laura")       
                    call Laura_Schedule(0)                        
                    if "leaving" in L_RecentActions:
                        call DrainWord("Laura","leaving")
                    if L_Loc == bg_current:
                        ch_l "I think i'm fine here."
                    else:
                        ch_l "Ok, see ya then."
                        call Set_The_Scene   
                    return
                
        
        "Date":
                    ch_p "Do you want to go on a date tonight?"
                    call Laura_Date_Ask

        "Switch to. . .":
                menu:
                    "Rogue":
                        call Chat("Rogue")       
                    "Kitty":
                        call Chat("Kitty")        
                    "Emma":
                        call Chat("Emma")
                    "Never mind":
                        pass
                            
        "Never mind.":
                    if L_Loc != bg_current:
                        ch_l "Ok."
                    return
    jump Laura_Chat


#Laura Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  

label Laura_Relationship:
    menu:
        ch_l "What did you want to talk about?"
        
#        "Do you want to be my girlfriend?" if "dating" not in L_Traits and "ex" not in L_Traits:
#                $ L_DailyActions.append("relationship")
#                if "asked boyfriend" in L_DailyActions and "angry" in L_DailyActions:
#                    call LauraFace("angry", 1)
#                    ch_l "Like I said, not interested."
#                    return
#                elif "asked boyfriend" in L_DailyActions:
#                    call LauraFace("angry", 1)
#                    ch_l "Still a no."
#                    return
                
#                $ L_DailyActions.append("asked boyfriend")
                
#                if P_Harem and "LauraYes" not in P_Traits:  
#                    if len(P_Harem) >= 2:
#                        ch_l "You'd need to clear it with the others first, [L_Petname]."
#                    else:
#                        ch_l "You'd need to clear it with [P_Harem[0]] first, [L_Petname]."
#                    return
                                    
#                if L_Event[5]:
#                    call LauraFace("bemused", 1)
#                    ch_l "I asked, you said \"no\". . ."
#                else:
#                    call LauraFace("surprised", 2)
#                    ch_l "Huh? . ." 
#                    call LauraFace("smile", 1)
                    
#                call Laura_OtherWoman
                
#                if L_Love >= 800:
#                    call LauraFace("surprised", 1)
#                    $ L_Mouth = "smile"
#                    call Statup("Laura", "Love", 200, 40)
#                    ch_l "Sure!"
#                    if "boyfriend" not in L_Petnames:
#                        $ L_Petnames.append("boyfriend")                
#                    $ L_Traits.append("dating") 
#                    if "LauraYes" in P_Traits:       
#                                $ P_Traits.remove("LauraYes")
#                                $ P_Harem.append("Laura")
#                                call Harem_Initiation
#                    "Laura tackles you and kisses you deeply."
#                    call LauraFace("kiss", 1) 
#                    $ L_Kissed += 1
#                elif L_Obed >= 500:
#                    call LauraFace("perplexed")
#                    ch_l "I don't know, \"dating\". . ."
#                elif L_Inbt >= 500:
#                    call LauraFace("smile")                
#                    ch_l "Nah, this is more fun."
#                else:
#                    call LauraFace("perplexed", 1)
#                    ch_l "Whoa, slow down, [L_Petname]."
                    
        "When you said you loved me. . ." if "lover" not in L_Traits and L_Event[6] >= 20 and L_Event[6] != 23:
                call Laura_Love_Redux
                
        "When you were telling me all that stuff about yourself. . ." if "lover" not in L_Traits and L_Event[6] == 23:
                call Laura_Love_Redux
        
#        "Do you want to get back together?" if "ex" in L_Traits:
#                $ L_DailyActions.append("relationship")
#                if "asked boyfriend" in L_DailyActions and "angry" in L_DailyActions:
#                    call LauraFace("angry", 1)
#                    ch_l "Like I said, not interested."
#                    return
#                elif "asked boyfriend" in L_DailyActions:
#                    call LauraFace("angry", 1)
#                    ch_l "Still a no."
#                    return
                
#                $ L_DailyActions.append("asked boyfriend")
                
#                if P_Harem and "LauraYes" not in P_Traits:
#                    $ L_DailyActions.append("asked boyfriend")   
#                    if len(P_Harem) >= 2:
#                        ch_l "You'd need to clear it with the others first, [L_Petname]."
#                    else:
#                        ch_l "You'd need to clear it with [P_Harem[0]] first, [L_Petname]."
#                    return
                    
#                $ Cnt = 0
#                call Laura_OtherWoman
                                        
#                if L_Love >= 800:
#                    call LauraFace("surprised", 1)
#                    $ L_Mouth = "smile"
#                    call Statup("Laura", "Love", 90, 5)
#                    ch_l "Ok, you've earned another shot!"
#                    if "boyfriend" not in L_Petnames:
#                        $ L_Petnames.append("boyfriend")                
#                    $ L_Traits.append("dating")          
#                    $ L_Traits.remove("ex")
#                    if "LauraYes" in P_Traits:       
#                                $ P_Traits.remove("LauraYes")
#                                $ P_Harem.append("Laura")
#                                call Harem_Initiation
#                    "Laura pulls you in and kisses you deeply."
#                    call LauraFace("kiss", 1) 
#                    $ L_Kissed += 1
#                elif L_Love >= 600 and ApprovalCheck("Laura", 1500):
#                    call LauraFace("smile", 1)
#                    $ L_Mouth = "smile"
#                    call Statup("Laura", "Love", 90, 5)
#                    ch_l "Um, ok, I guess."
#                    if "boyfriend" not in L_Petnames:
#                        $ L_Petnames.append("boyfriend")                
#                    $ L_Traits.append("dating")             
#                    $ L_Traits.remove("ex")
#                    "Laura gives you a quick kiss."
#                    call LauraFace("kiss", 1) 
#                    $ L_Kissed += 1
#                elif L_Obed >= 500:
#                    call LauraFace("sad")
#                    ch_l "I think it's best we keep things simple."   
#                elif L_Inbt >= 500:
#                    call LauraFace("perplexed")                
#                    ch_l "That ruined the fun."
#                else:
#                    call LauraFace("perplexed", 1)
#                    ch_l "I can't trust you like that."
                
#        # End Back Together
             
        "I wanted to ask about [[another girl]" if "Laura" in P_Harem:
                menu:
                    "Have you reconsidered letting me date. . ."
                    "Rogue" if "Rogue" not in P_Harem:
                            call Poly_Start("Rogue",1)
                    "Kitty" if "Kitty" not in P_Harem:
                            call Poly_Start("Kitty",1)
                    "Emma" if "Emma" not in P_Harem:
                            call Poly_Start("Emma",1)
                    "Never mind":
                            pass       
                               
#        "I think we should break up." if "dating" in R_Traits: #ApprovalCheck("Rogue", 950, "L", Bonus = (B/3)):
#            if "breakup talk" in R_RecentActions:
#                ch_r "We were {i}just{/i} over this, not even funny."
#            elif "breakup talk" in R_DailyActions:
#                ch_r "Tired of me again that quick?" 
#                ch_r "We're not having this talk today, [R_Petname]."
#            else:
#                call Rogue_Breakup                
            
            
#        "I'd like to bring Laura into this." if "poly Laura" not in R_Traits and not L_Break[0]:    #fix nonfunctional yet, switch over to Laura stuff
            
#            if "asked threesome" in R_RecentActions:
#                ch_r "Persistence will NOT be rewarded here."
#                return
#            elif "asked threesome" in R_DailyActions:
#                ch_r "I don't think my answer's changing any time soon." 
#                return
#            else:
#                $ R_DailyActions.append("asked threesome")                
#                $Cnt = int((R_LikeLaura - 500)/2)
#                menu:
#                    ch_r "What does she think about this?"
                        
#                    "She said I can be with you too." if "poly Rogue" in L_Traits:
#                        if ApprovalCheck("Rogue", 1800, Bonus = Cnt):
#                            call RogueFace("smile", 1)
#                            if R_Love >= R_Obed:
#                                ch_r "Just so long as we can be together, I can share."
#                            elif R_Obed >= R_Inbt:
#                                ch_r "I'm ok with that if she is."
#                            else:
#                                ch_r "Yeah, I mean I guess so."
#                                $ R_Traits.append("poly Laura")
#                        else:
#                            call RogueFace("angry", 1)
#                            ch_r "Well maybe she did, but I don't want to share."  
                    
#                    "I could ask if she'd be ok with me dating you both." if "poly Rogue" not in L_Traits:
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
#                        if R_LikeLaura >= 700:
#                            ch_r "I have to say I've kind of been thinking about it myself."  
#                            call Statup("Rogue", "Love", 90, 5)
#                            call Statup("Rogue", "Obed", 70, 1)
#                            call Statup("Rogue", "Inbt", 80, 5)
#                        elif R_LikeLaura >= 500:
#                            ch_r "I guess, if that's what you want. . ." 
#                        elif R_Obed >= 700:
#                            ch_r "If that's what you want. . ." 
#                        else:
#                            ch_r "I can't really stand her, I don't think so."  
                            
                        
#                    "You're right, I was dumb to ask.":
#                        call RogueFace("sad")
#                        ch_r "Yeah, you were."  
                        
            #end Laura Threesome
                
        "You said you wanted me to be more in control?" if "sir" not in L_Petnames and "sir" in L_History:
                if "asked sub" in L_RecentActions:
                        ch_l "We just had this conversation."
                elif "asked sub" in L_DailyActions:
                        ch_l "Enough of that talk for one day. . ."            
                else:
                        call Laura_Sub_Asked
        "You said you wanted me to be your Master?" if "master" not in L_Petnames and "master" in L_History:
                if "asked sub" in L_RecentActions:
                        ch_l "We just had this conversation."
                elif "asked sub" in L_DailyActions:
                        ch_l "Enough of that talk for one day. . ."          
                else:
                        call Laura_Sub_Asked
                        
        "Never Mind":
            return
              
    return

label Laura_OtherWoman:
    return                      #fix, remove this once this portion works.
    $ Cnt = 0
    if "dating" in R_Traits:
        call LauraFace("perplexed")
        menu: 
            ch_l "But you're with Rogue right now."
            "She said I can be with you too." if "poly Laura" in R_Traits:
                $Cnt = int((L_LikeRogue - 500)/2)
                if ApprovalCheck("Laura", 1800, Bonus = Cnt):
                    call LauraFace("smile", 1)
                    if L_Love >= L_Obed:
                        ch_l "Just so long as we can be together, I can share."
                    elif L_Obed >= L_Inbt:
                        ch_l "I'm ok with that if she is."
                    else:
                        ch_l "Yeah, I mean I guess so."
                        $ L_Traits.append("poly Rogue")
                else:
                    call LauraFace("angry", 1)
                    ch_l "Well maybe she did, but I don't want to share."  
                    $ renpy.pop_call()                                          #This causes it to jump past the previous menu on the return
            
            "I could ask if she'd be ok with me dating you both." if "poly Laura" not in R_Traits:
                $Cnt = int((L_LikeRogue - 500)/2)
                if ApprovalCheck("Laura", 1800, Bonus = Cnt):
                    call LauraFace("smile", 1)
                    if L_Love >= L_Obed:
                        ch_l "Just so long as we can be together, I can share."
                    elif L_Obed >= L_Inbt:
                        ch_l "I'm ok with that if she is."
                    else:
                        ch_l "Yeah, I mean I guess so."                        
                    ch_l "Go ask her, give me the night to think about it, and then come back tomorrow with her answer."
                else:
                    call LauraFace("angry", 1)
                    ch_l "Well maybe she would, but I don't want to share."      
                $ renpy.pop_call()
            
            "What she doesn't know won't hurt her.":
                $Cnt = int((L_LikeRogue - 500)/2)
                if not ApprovalCheck("Laura", 1800, Bonus = -(int((L_LikeRogue - 600)/2))): #checks if Rogue likes you more than Laura
                    call LauraFace("angry", 1)
                    if not ApprovalCheck("Laura", 1800):
                        ch_l "Well I don't like you that much either."
                    else:
                        ch_l "Well I'm not cool with that, Rogue's a friend of mine."                    
                    $ renpy.pop_call() 
                    
                else:
                    call LauraFace("smile", 1)
                    if L_Love >= L_Obed:
                        ch_l "I really do want to be together with you."
                    elif L_Obed >= L_Inbt:
                        ch_l "If that's how you want it to be."
                    else:
                        ch_l "I suppose that's true."
                    $ L_Traits.append("poly Rogue")
                    $ L_Traits.append("downlow")
                
            "I can break it off with her.":
                call LauraFace("sad")
                ch_l "Well then maybe I'll see you tomorrow after you have."                                   
                $ renpy.pop_call()
                
            "You're right, I was dumb to ask.":
                call LauraFace("sad")
                ch_l "We had a good thing there. Maybe some day. . ."                    
                $ renpy.pop_call()                     
                
    return
    
label Laura_Settings:
    menu:
        ch_p "Let's talk about you."
        "Wardrobe": 
                ch_p "I wanted to talk about your style."
                if L_Loc != "bg player" and L_Loc != "bg laura":  
                    if Taboo:
                        if "exhibitionist" in L_Traits:
                            ch_l "Yes? . ."  
                        elif ApprovalCheck("Laura", 900, TabM=4) or ApprovalCheck("Laura", 400, "I", TabM=3): 
                            ch_l "I don't think I'm supposed to undress around here. . ."
                        else:
                            ch_l "I don't think I'm supposed to undress around here. . ."
                            ch_l "Can we talk about this in our rooms?"
                            return
                    call Laura_Clothes
                elif ApprovalCheck("Laura", 900, TabM=4) or ApprovalCheck("Laura", 600, "L") or ApprovalCheck("Laura", 300, "O"):
                            ch_l "Oh? What about them?"
                            call Laura_Clothes
                else:
                            ch_l "I don't think about my clothes much."
                            ch_l "You shouldn't either."    
                
        "Shift her Personality" if ApprovalCheck("Laura", 900, "L", TabM=0) or ApprovalCheck("Laura", 900, "O", TabM=0) or ApprovalCheck("Laura", 900, "I", TabM=0):
                ch_p "Could we talk about us?"
                call Laura_Personality
        
        
        "Dirty Talk":
                    ch_p "About when we have sex. . ."
                    call Laura_SexChat
          
        "Pet names":
            menu:  
                "About that X-23 name. . .":
                    menu:
                        "Could I call you Laura?" if LauraName == "X-23":  
                            if "Laura" not in L_History:     
                                    if L_Love >= 500:        
                                        call Statup("Laura", "Love", 90, 15)
                                    call Statup("Laura", "Inbt", 50, 5)      
                                    $ L_History.append("Laura")             
                            if "namechange" in L_DailyActions: 
                                    call Statup("Laura", "Love", 90, -1)
                                    ch_l "Make up your mind!" 
                            else:
                                    call Statup("Laura", "Love", 90, -2)
                                    call Statup("Laura", "Obed", 30, 5) 
                                    ch_l "Sure, whatever."                    
                            $ LauraName = "Laura" 
                            $ L_DailyActions.append("namechange") 
                        "Could I call you X-23?" if LauraName == "Laura":   
                            if "X-23" not in L_History:     
                                    if L_Love >= 500: 
                                        call Statup("Laura", "Love", 90, -10)
                                    call Statup("Laura", "Obed", 50, 5)    
                                    call Statup("Laura", "Obed", 90, 10)          
                                    $ L_History.append("X-23")                                     
                            if "namechange" in L_DailyActions: 
                                    call Statup("Laura", "Love", 90, -1)
                                    ch_l "Make up your mind!" 
                            else: 
                                    ch_l "Sure, whatever."                    
                            $ LauraName = "X-23" 
                            $ L_DailyActions.append("namechange") 
                        "Never mind":
                            pass
                            
                            
                "Your Pet Name":
                    ch_p "Could we talk about my pet name?"
                    if ApprovalCheck("Laura", 600, "L", TabM=0) or ApprovalCheck("Laura", 300, "O", TabM=0):
                        call Laura_Names    
                    else:
                        $ L_Mouth = "smile"
                        ch_l "Oh?"
                        
                "Her Pet Name":
                        ch_p "I've got a pet name for you, you know?"
                        if ApprovalCheck("Laura", 600, "L", TabM=0):
                            ch_l "Do you?" 
                        elif ApprovalCheck("Laura", 300, "O", TabM=0):
                            ch_l "What did you want to call me?"
                        else:
                            ch_l "Yeah?"            
                        call Laura_Pet   
        
                "Back":
                        pass
                        
        "About other girls":
                menu:
                    ch_p "How do you feel about. . ."
                    "Rogue?":
                        call Laura_AboutRogue  
                    "Kitty?":
                        call Laura_AboutKitty
                    "Emma?":
                        call Laura_AboutEmma  
                    "Never mind.":
                        pass
            
        "Follow options" if "follow" in L_Traits:
                ch_p "You know how you ask if I want to follow you sometimes?"
                $ Line = 0
                menu:
                    ch_l "Yeah?"
                    "You can go where you want, I'll catch up later." if "freetravels" not in L_Traits:
                        call LauraFace("perplexed")
                        ch_l "Oh. . . okay."
                        if "follow" not in L_DailyActions:
                            call Statup("Laura", "Love", 90, -2)
                            call Statup("Laura", "Obed", 30, 5) 
                        $ L_Traits.append("freetravels")
                        $ Line = "free"
                            
                    "You can ask if I want to follow you." if "asktravels" not in L_Traits:
                        call LauraFace("perplexed")
                        ch_l "Right. . ."
                        if "follow" not in L_DailyActions:
                            call Statup("Laura", "Love", 70, 2) 
                            call Statup("Laura", "Inbt", 60, 2) 
                        $ Line = "ask"
                                                
                    "Don't ever leave when I'm around." if "lockedtravels" not in L_Traits:
                        if ApprovalCheck("Laura", 500, "O") or ApprovalCheck("Laura", 900, "L"):   
                            call LauraFace("smile")
                            ch_l "That's sweet."
                            if "follow" not in L_DailyActions:
                                if L_Love > 90:
                                    call Statup("Laura", "Love", 99, 2)
                                call Statup("Laura", "Obed", 60, 5)                             
                            call Statup("Laura", "Inbt", 50, -5, 1) 
                            $ Line = "lock"
                        else:
                            call LauraFace("angry")                        
                            ch_l "Well, who cares what you think?"
                            
                    "Never mind.":
                        ch_l "Right. . ."
                        
                if Line:
                    $ L_DailyActions.append("follow")                
                    if "freetravels" in L_Traits:
                        $ L_Traits.remove("freetravels") 
                    if "asktravels" in L_Traits:
                        $ L_Traits.remove("asktravels") 
                    if "lockedtravels" in L_Traits:
                        $ L_Traits.remove("lockedtravels") 
                
                    if Line == "free":
                        $ L_Traits.append("freetravels")            
                    elif Line == "ask":
                        $ L_Traits.append("asktravels")                
                    elif Line == "lock":
                        $ L_Traits.append("lockedtravels")    
                    $ Line = 0        
                              
        "Gym clothes" if "asked gym" in L_DailyActions and "no ask gym" not in L_Traits:
                    ch_p "You asked me about your gym clothes?"
                    ch_p "Don't worry about that, your gym clothes are cute."   
                    ch_l "Oh. . . ok."
                    $ L_Traits.append("no ask gym")
        "Gym clothes" if "no ask gym" in L_Traits:
                    ch_p "You asked me about your gym clothes?"
                    ch_p "Forget about that, I changed my mind."      
                    ch_l "Oh. . . ok."
                    $ L_Traits.remove("no ask gym")
                    
        "Private outfit" if L_Schedule[9]:
                    #if comfy is in L_Traits, she won't ask before changing
                    ch_p "You know that outfit you wear in private?"
                    menu:
                        ch_l "Yeah?"
                        "Just put them on without asking me about it." if "comfy" not in L_Traits:
                            $ L_Traits.append("comfy")
                        "Ask before changing into that." if "comfy" in L_Traits:
                            $ L_Traits.remove("comfy")
                        "Never Mind":
                            pass     
                            
        "Tasks" if "sir" in L_Petnames:
                ch_p "I have some tasks for you."
                call Laura_Controls
        
        "Switch to. . .":
                menu:
                    "Rogue":
                        call Rogue_Chat_Set("settings")                    
                    "Kitty":
                        call Kitty_Chat_Set("settings")                 
                    "Emma":
                        call Emma_Chat_Set("settings")
                    "Never mind":
                        pass
        "Never mind.":
            return 
    jump Laura_Settings

# End Laura Chat


# Laura Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label Laura_SexChat(Line = "Yeah, what did you want to talk about?"):
    while True:
            menu:
                ch_l "[Line]"                
                "My favorite thing to do is. . .":
                    if "setfav" in L_DailyActions:
                        ch_l "I remember."
                    else:
                        menu:
                            "Sex.":
                                        call LauraFace("sly")
                                        if L_PlayerFav == "sex":
                                            call Statup("Laura", "Lust", 80, 5)
                                            ch_l "Yeah, I know that. . ."                                
                                        elif L_Favorite == "sex":
                                            call Statup("Laura", "Love", 90, 5)
                                            call Statup("Laura", "Lust", 80, 10)
                                            ch_l "I really like it too!"
                                        elif L_Sex >= 5:
                                            ch_l "Well I don't mind that."
                                        elif not L_Sex:
                                            call LauraFace("perplexed")
                                            ch_l "Who's fucking you? Is it Ms. Frost?!"
                                        else:
                                            call LauraFace("bemused")
                                            ch_l "Heh, um, yeah, it's nice. . ."
                                        $ L_PlayerFav = "sex"
                                        
                            "Anal.":
                                        call LauraFace("sly")
                                        if L_PlayerFav == "anal":
                                            call Statup("Laura", "Lust", 80, 5)
                                            ch_l "So you've said. . ."                                
                                        elif L_Favorite == "anal":
                                            call Statup("Laura", "Love", 90, 5)
                                            call Statup("Laura", "Lust", 80, 10)
                                            ch_l "I love it too!"
                                        elif L_Anal >= 10:
                                            ch_l "Yeah, it's. . . nice. . ."
                                        elif not L_Anal:
                                            call LauraFace("perplexed")
                                            ch_l "Who's fucking you? Is it Ms. Frost?!"
                                        else:
                                            call LauraFace("bemused",Eyes="side")
                                            ch_l "Heh, heh, yeah, um, it's ok. . ."
                                        $ L_PlayerFav = "anal"
                                        
                            "Blowjobs.":   
                                        call LauraFace("sly")
                                        if L_PlayerFav == "blow":
                                            call Statup("Laura", "Lust", 80, 3)
                                            ch_l "Yeah, I know."                                
                                        elif L_Favorite == "blow":
                                            call Statup("Laura", "Love", 90, 5)
                                            call Statup("Laura", "Lust", 80, 5)
                                            ch_l "I love your dick!"
                                        elif L_Blow >= 10:
                                            ch_l "Yeah, you're pretty tasty."
                                        elif not L_Blow:
                                            call LauraFace("perplexed")
                                            ch_l "Who's sucking your dick?! Is it Ms. Frost?!"
                                        else:
                                            call LauraFace("bemused")
                                            ch_l "I'm. . . getting used to the taste. . ."
                                        $ L_PlayerFav = "blow"     
                                        
                            "Titjobs.":
                                        call LauraFace("sly")   
                                        if L_PlayerFav == "titjob":
                                            call Statup("Laura", "Lust", 80, 5)
                                            ch_l "Yeah, you've said that before. . ."                           
                                        elif L_Favorite == "titjob":
                                            call Statup("Laura", "Love", 90, 5)
                                            call Statup("Laura", "Lust", 80, 7)
                                            ch_l "Yeah, I enjoy that too. . ."
                                        elif L_Tit >= 10:
                                            ch_l "It's certainly an interesting experience . . ."
                                        elif not L_Tit:
                                            call LauraFace("perplexed")
                                            ch_l "Who's titfucking you? It's Ms. Frost, isn't it!"
                                        else:
                                            call LauraFace("bemused")
                                            ch_l "That's nice of you to say. . ."
                                            call Statup("Laura", "Love", 80, 5)
                                            call Statup("Laura", "Inbt", 50, 10)
                                        $ L_PlayerFav = "titjob"   
                                        
                            "Handjobs.":
                                        call LauraFace("sly")
                                        if L_PlayerFav == "hand":
                                            call Statup("Laura", "Lust", 80, 5)
                                            ch_l "Yeah, you've said that. . ."                                
                                        elif L_Favorite == "hand":
                                            call Statup("Laura", "Love", 90, 5)
                                            call Statup("Laura", "Lust", 80, 7)
                                            ch_l "You do feel pretty comfy. . ."
                                        elif L_Hand >= 10:
                                            ch_l "I like it too . . ."
                                        elif not L_Hand:
                                            call LauraFace("perplexed")
                                            ch_l "Who's jerking you off? Is it Ms. Frost?!"
                                        else:
                                            call LauraFace("bemused")
                                            ch_l "Yeah, it's nice. . ."
                                        $ L_PlayerFav = "hand"  
                                        
                            "Feeling you up.":
                                        $ Cnt = L_FondleB + L_FondleT + L_SuckB + L_Hotdog
                                        call LauraFace("sly")
                                        if L_PlayerFav == "fondle":
                                            call Statup("Laura", "Lust", 80, 3)
                                            ch_l "Yeah, I think we're clear on that. . ."                                
                                        elif L_Favorite in ("hotdog","suck breasts","fondle breasts","fondle thighs"):
                                            call Statup("Laura", "Love", 90, 5)
                                            call Statup("Laura", "Lust", 80, 5)
                                            ch_l "I love when you touch me. . ."
                                        elif Cnt >= 10:
                                            ch_l "Yeah, it's really nice . . ."
                                        elif not Cnt:
                                            call LauraFace("perplexed")
                                            ch_l "Who's letting you feel her up? Is it Ms. Frost?!"
                                        else:
                                            call LauraFace("bemused")
                                            ch_l "I do like how that feels. . ."
                                        $ L_PlayerFav = "fondle"  
                                        $ Cnt = 0
                                
                            "Kissing you.":
                                        call LauraFace("sly")
                                        if L_PlayerFav == "kiss you":
                                            call Statup("Laura", "Love", 90, 3)
                                            ch_l "Such a romantic. . ."                                
                                        elif L_Favorite == "kiss you":
                                            call Statup("Laura", "Love", 90, 5)
                                            call Statup("Laura", "Lust", 80, 5)
                                            ch_l "Hmm, the taste of you on my lips. . ."
                                        elif L_Kissed >= 10:
                                            ch_l "I love kissing you too . . ."
                                        elif not L_Kissed:
                                            call LauraFace("perplexed")
                                            ch_l "Who are you kissing? Is it Ms. Frost?!"
                                        else:
                                            call LauraFace("bemused")
                                            ch_l "I like kissing you too. . ."
                                        $ L_PlayerFav = "kiss you" 
                                
                        $ L_DailyActions.append("setfav") 
                            
                "What's your favorite thing to do?":
                                if not ApprovalCheck("Laura", 800):
                                        call LauraFace("perplexed")
                                        ch_l ". . ."                                    
                                else:
                                        if L_SEXP >= 50:
                                            call LauraFace("sly")
                                            ch_l "You should know. . ."   
                                        else:                 
                                            call LauraFace("bemused")
                                            $ L_Eyes = "side"
                                            ch_l "Hmm. . ."
                                            
                                            
                                        if not L_Favorite or L_Favorite == "kiss":
                                            ch_l "Kissing?"  
                                        elif L_Favorite == "anal":
                                                ch_l "Probably anal."  
                                        elif L_Favorite == "lick ass":
                                                ch_l "When you lick my ass." 
                                        elif L_Favorite == "insert ass":
                                                ch_l "Fingering my asshole, probably." 
                                        elif L_Favorite == "sex":
                                                ch_l "Just the usual pounding." 
                                        elif L_Favorite == "lick pussy":
                                                ch_l "When you lick my pussy." 
                                        elif L_Favorite == "fondle pussy":
                                                ch_l "When you finger me." 
                                        elif L_Favorite == "blow":
                                                ch_l "I like how your cock tastes." 
                                        elif L_Favorite == "tit":
                                                ch_l "when I use my tits." 
                                        elif L_Favorite == "hand":
                                                ch_l "I like jerking you off." 
                                        elif L_Favorite == "hotdog":
                                                ch_l "When you grind against me." 
                                        elif L_Favorite == "suck breasts":
                                                ch_l "When you suck my tits."  
                                        elif L_Favorite == "fondle breasts":
                                                ch_l "When you grab my tits." 
                                        elif L_Favorite == "fondle thighs":
                                                ch_l "When you rub my thighs."
                                        else:
                                                ch_l "How should I know?"    
                                                
                                # End Laura's favorite things.
                    
                    
                "Don't talk as much during sex." if "vocal" in L_Traits:
                        if "setvocal" in L_DailyActions:
                            call LauraFace("perplexed")
                            ch_l "I heard you the first time."
                        else:              
                            if ApprovalCheck("Laura", 1000) and L_Obed <= L_Love:
                                call LauraFace("bemused")
                                call Statup("Laura", "Obed", 90, 1)
                                ch_l "Stay quiet, got it."
                                $ L_Traits.remove("vocal")   
                            elif ApprovalCheck("Laura", 700, "O"):
                                call LauraFace("sadside")
                                call Statup("Laura", "Obed", 90, 1)
                                ch_l ". . ."
                                $ L_Traits.remove("vocal")   
                            elif ApprovalCheck("Laura", 600):
                                call LauraFace("sly")
                                call Statup("Laura", "Love", 90, -3)
                                call Statup("Laura", "Obed", 50, -1)
                                call Statup("Laura", "Inbt", 90, 5)
                                ch_l "Don't push it, [L_Petname]."
                            else:
                                call LauraFace("angry")
                                call Statup("Laura", "Love", 90, -5)
                                call Statup("Laura", "Obed", 60, -3)
                                call Statup("Laura", "Inbt", 90, 10)
                                ch_l "I don't take orders from you, [L_Petname]."
                                                
                            $ L_DailyActions.append("setvocal")   
                "Talk dirty to me during sex." if "vocal" not in L_Traits:
                        if "setvocal" in L_DailyActions:
                            call LauraFace("perplexed")
                            ch_l "I heard you the first time."
                        else:     
                            if ApprovalCheck("Laura", 1000) and L_Obed <= L_Love:
                                call LauraFace("sly")
                                call Statup("Laura", "Obed", 90, 2)
                                ch_l "Louder? Ok. . ."
                                $ L_Traits.append("vocal")   
                            elif ApprovalCheck("Laura", 700, "O"):
                                call LauraFace("sadside")
                                call Statup("Laura", "Obed", 90, 2)
                                ch_l "If you want, [L_Petname]."
                                $ L_Traits.append("vocal")   
                            elif ApprovalCheck("Laura", 600):
                                call LauraFace("sly")
                                call Statup("Laura", "Obed", 90, 3)
                                ch_l "I guess?"
                                $ L_Traits.append("vocal")   
                            else:
                                call LauraFace("angry")
                                call Statup("Laura", "Inbt", 90, 5)
                                ch_l ". . ."  
                                
                            $ L_DailyActions.append("setvocal")  
                        # End Laura Dirty Talk
                    
                    
                "Don't do your own thing as much during sex." if "passive" not in L_Traits:
                        if "initiative" in L_DailyActions:
                            call LauraFace("perplexed")
                            ch_l "I heard you the first time."
                        else:       
                            if ApprovalCheck("Laura", 1200) and L_Obed <= L_Love:
                                call LauraFace("bemused")
                                call Statup("Laura", "Obed", 90, 1)
                                ch_l "Passive, eh?"     
                                $ L_Traits.append("passive")                  
                            elif ApprovalCheck("Laura", 700, "O"):
                                call LauraFace("sadside")
                                call Statup("Laura", "Obed", 90, 1)
                                ch_l "I'll try to hold back."
                                $ L_Traits.append("passive")
                            elif ApprovalCheck("Laura", 600):
                                call LauraFace("sly")
                                call Statup("Laura", "Love", 90, -3)
                                call Statup("Laura", "Obed", 50, -1)
                                call Statup("Laura", "Inbt", 90, 5)
                                ch_l "Hm, no."
                            else:
                                call LauraFace("angry")
                                call Statup("Laura", "Love", 90, -5)
                                call Statup("Laura", "Obed", 60, -3)
                                call Statup("Laura", "Inbt", 90, 10)
                                ch_l "We'll see."
                                
                            $ L_DailyActions.append("initiative")  
                "Take more initiative during sex." if "passive" in L_Traits:
                        if "initiative" in L_DailyActions:
                            call LauraFace("perplexed")
                            ch_l "I heard you the first time."
                        else:   
                            if ApprovalCheck("Laura", 1000) and L_Obed <= L_Love:
                                call LauraFace("bemused")
                                call Statup("Laura", "Obed", 90, 1)
                                ch_l "More active, got it."    
                                $ L_Traits.remove("passive")                   
                            elif ApprovalCheck("Laura", 700, "O"):
                                call LauraFace("sadside")
                                call Statup("Laura", "Obed", 90, 1)
                                ch_l "If you insist."
                                $ L_Traits.remove("passive")    
                            elif ApprovalCheck("Laura", 600):
                                call LauraFace("sly")
                                call Statup("Laura", "Obed", 90, 3)
                                ch_l "We'll see."
                                $ L_Traits.remove("passive")  
                            else:
                                call LauraFace("angry")
                                call Statup("Laura", "Inbt", 90, 5)
                                ch_l "Too much work."  
                                
                            $ L_DailyActions.append("initiative")   
                "Never Mind" if Line == "Yeah, what did you want to talk about?":
                    return
                "That's all." if Line != "Yeah, what did you want to talk about?":
                    return
            if Line == "Yeah, what did you want to talk about?":
                $ Line = "Anything else?"
    return
# End Laura Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


## Laura Chitchat /////////////////// #Work in progress
label Laura_Chitchat(O=0, Options = ["default","default","default"]):
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:                                               #adds only a specific option that was sent
        $ Options = [O]
    else:
        
        if "Laura" not in Digits:
                if ApprovalCheck("Laura", 500, "L") or ApprovalCheck("Laura", 250, "I"):
                    ch_l "Oh, here's my number, in case you need back-up."
                    $ Digits.append("Laura")  
                    return
                elif ApprovalCheck("Laura", 250, "O"):
                    ch_l "If you need to contact me, here's my number."             
                    $ Digits.append("Laura")
                    return
                
        if "hungry" not in L_Traits and (L_Swallow + L_Chat[2]) >= 10 and L_Loc == bg_current:  #She's swallowed a lot        
                call Laura_Hungry
                return  
        
#        $ Options = ["default","default","default"]
        #adds options based on accomplishments
#        if PunishmentX and "caught chat" not in L_DailyActions:
#            $ Options.append("caught")
        if L_Event[0] and "key" not in L_Chat:
            $ Options.append("key")
        if "lover" in L_Petnames and ApprovalCheck("Laura", 900, "L"): # luvy dovey       
            $ Options.append("luv")
              
        if "mandrill" in P_Traits and "cologne chat" not in L_DailyActions:
            $ Options.append("mandrill")        
        if "purple" in P_Traits and "cologne chat" not in L_DailyActions:
            $ Options.append("purple")        
        if "corruption" in P_Traits and "cologne chat" not in L_DailyActions:
            $ Options.append("corruption")
        
        if LauraName == "X-23" and "X-23" not in L_History: 
            $ Options.append("laura")
            
        if L_Date >= 1:
            #if you've dated before
            $ Options.append("dated")
#        if "cheek" in L_DailyActions and "cheek" not in L_Chat:
#            #If you've touched her cheek today
#            $ Options.append("cheek")
        if L_Kissed >= 5:
            #if you've kissed a few times
            $ Options.append("kissed")
        if "dangerroom" in P_DailyActions:
            #If you've been in the danger room today
            $ Options.append("dangerroom")
        if "showered" in L_DailyActions:
            #If you've caught Laura showering today
            $ Options.append("showercaught")
        if "fondle breasts" in L_DailyActions or "fondle pussy" in L_DailyActions or "fondle ass" in L_DailyActions:
            #If you've fondled Laura today
            $ Options.append("fondled")
        if "Dazzler and Longshot" in L_Inventory and "256 Shades of Grey" in L_Inventory and "Avengers Tower Penthouse" in L_Inventory:   
            #If you've given Laura the books
            if "book" not in L_Chat:
                $ Options.append("booked")
        if "lace bra" in L_Inventory or "lace panties" in L_Inventory:   
            #If you've given Laura the lingerie
            if "lingerie" not in L_Chat:
                $ Options.append("lingerie")
        if L_Hand:   
            #If Laura's given a handjob
            $ Options.append("handy")
        if L_Swallow:   
            #If Laura's swallowed before
            $ Options.append("swallowed")
        if "cleaned" in L_DailyActions or "painted" in L_DailyActions:
            #If Laura's been facialed
            $ Options.append("facial")
        if L_Sleep:
            #If Laura's slept over
            $ Options.append("sleep")
        if L_CreamP or L_CreamA:
            #If Laura's been creampied
            $ Options.append("creampie")
        if L_Sex or L_Anal:
            #If Laura's been sexed
            $ Options.append("sexed")
        if L_Anal:
            #If Laura's been analed
            $ Options.append("anal")
            
#        if not L_Chat[0] and L_Sex:
#            $ Options.append("virgin")    
            
#        if (bg_current == "bg laura" or bg_current == "bg player") and "relationship" not in L_DailyActions:
#            if "lover" not in L_Petnames and ApprovalCheck("Laura", 900, "L"): # L_Event[6]        
#                $ Options.append("lover?")
#            elif "sir" not in L_Petnames and ApprovalCheck("Laura", 500, "O"): # L_Event[7]
#                $ Options.append("sir?")      
#            elif "daddy" not in L_Petnames and ApprovalCheck("Laura", 750, "L") and ApprovalCheck("Laura", 500, "O") and ApprovalCheck("Laura", 500, "I"): # L_Event[5]
#                $ Options.append("daddy?")
#            elif "master" not in L_Petnames and ApprovalCheck("Laura", 900, "O"): # L_Event[8]
#                $ Options.append("master?")
#            elif "sex friend" not in L_Petnames and ApprovalCheck("Laura", 500, "I"): # L_Event[9]
#                $ Options.append("sexfriend?")
#            elif "fuck buddy" not in L_Petnames and ApprovalCheck("Laura", 900, "I"): # L_Event[10]
#                $ Options.append("fuckbuddy?")  
            
        
        if not ApprovalCheck("Laura", 300):            #She dislikes you
            $ Options.append("hate") 
    
    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one
    
    if Options[0] == "mandrill":                             
        $ L_DailyActions.append("cologne chat") 
        call LauraFace("confused")
        ch_l "(sniff, sniff). . . smalls like. . . ape . . ."
        call LauraFace("sexy", 2)
        ch_l ". . . did you want to do something later?"    
    elif Options[0] == "purple":              
        $ L_DailyActions.append("cologne chat") 
        call LauraFace("sly",1)
        ch_l "(sniff, sniff). . . what is that? . ."
        call LauraFace("normal",0)
        ch_l ". . . what was it you wanted?"    
    elif Options[0] == "corruption":              
        $ L_DailyActions.append("cologne chat") 
        call LauraFace("confused")
        ch_l "(sniff, sniff). . . that's a strong scent. . ."
        call LauraFace("angry")
        ch_l ". . . a dangerous scent. . ."
        call LauraFace("sly")
                
    elif Options[0] == "caught": # Xavier's caught you
            if "caught chat" in L_Chat:
                    ch_l "We should be more careful about getting caught."
                    if not ApprovalCheck("Laura", 500, "I"):
                         ch_l "Unless. . ."
            else:    
                    ch_l "Sorry we got dragged into the Professor's office like that."
                    if not ApprovalCheck("Laura", 500, "I"):
                        ch_l "I guess you wouldn't want to get it on in public anymore."
                    else:
                        ch_l "I kind of enjoyed it though. . ."
                    $ L_Chat.append("caught chat") 
    elif Options[0] == "key": # you have her key
            if L_SEXP <= 15:
                ch_l "I gave you the key for convenience, don't abuse it . ."
            else:
                ch_l "I gave you a key, but you don't visit. . ."
            $ L_Chat.append("key") 
        
#    elif Options[0] == "cheek":
#            #Laura's response to having her cheek touched.
#            ch_l "So,[L_Petname]. . .y'know how you[L_like]kinda just brushed my cheek before?"
#            ch_p "Yeah?  Was that okay?"
#            call LauraFace("smile",1)
#            ch_l "More than just {i}okay{/i}."
#            $ L_Chat.append("cheek") 
    
     
    elif Options[0] == "laura":    
            #if she never told you her name. . .
            ch_l "Oh, by the way, I also go by \"Laura.\" Laura Kinney."
            menu:
                "Oh, that's nice, I think I'll call you that.":   
                        call Statup("Laura", "Love", 70, 5) # Love              
                        $ LauraName = "Laura" 
                "Ok, but X-23 sounds cooler.":    
                        call Statup("Laura", "Love", 70, -2) # Love   
                        call Statup("Laura", "Obed", 70, 5) # Obed             
                        $ LauraName = "X-23" 
                                            
    elif Options[0] == "dated":
            #Laura's response to having gone on a date with the Player.
            ch_l "That was fun last night, we should do that again some time."

    elif Options[0] == "kissed":
            #Laura's response to having been kissed by the Player.
            call LauraFace("normal",1)
            ch_l "You're pretty good at kissing, [L_Petname]."
            menu:
                extend ""
                "Hey. . .I'm the best there is at what I do.":
                        call LauraFace("smile",1)
                        ch_l "You'll have to back that claim up."
                "No. You think?":
                        ch_l "Do I look like a kidder?"

    elif Options[0] == "dangerroom":
            #Laura's response to Player working out in the Danger Room while Laura is present
            call LauraFace("sly",1)
            ch_l "Hey,[L_Petname].  I saw you in the Danger Room, earlier."
            ch_l "You should probably keep your left up, you were taking too many shots to the head."

    elif Options[0] == "showercaught":
            #Laura's response to being caught in the shower.
            if "shower" in L_Chat: 
                ch_l "You saw me taking a shower again. . ."                       
            else:
                ch_l "Do you make a habit of bursting into the showers?"            
                $ L_Chat.append("shower") 
                menu:
                    extend ""
                    "It was a total accident!  I promise!":             
                            call Statup("Laura", "Love", 50, 5)    
                            call Statup("Laura", "Love", 90, 2) 
                            if ApprovalCheck("Laura", 1200):
                                call LauraFace("sly",1)
                                ch_l "I didn't mind."
                            call LauraFace("smile")
                            ch_l "We all make mistakes."
                    "Just with you.":        
                            call Statup("Laura", "Obed", 40, 5)   
                            if ApprovalCheck("Laura", 1000) or ApprovalCheck("Laura", 700, "L"):      
                                    call Statup("Laura", "Love", 90, 3)    
                                    call LauraFace("sly",1)
                                    ch_l "Hmm, I guess that's a compliment."
                            else:                
                                    call Statup("Laura", "Love", 70, -5) 
                                    call LauraFace("angry")
                                    ch_l "I think I should be insulted."                                                       
                    "Totally on purpose. I regret nothing.":
                            if ApprovalCheck("Laura", 1200):                     
                                    call Statup("Laura", "Love", 90, 3)          
                                    call Statup("Laura", "Obed", 70, 10)            
                                    call Statup("Laura", "Inbt", 50, 5) 
                                    call LauraFace("sly",1)
                                    ch_l "You seem to know what you want."
                            elif ApprovalCheck("Laura", 800):                          
                                    call Statup("Laura", "Obed", 60, 5)            
                                    call Statup("Laura", "Inbt", 50, 5) 
                                    call LauraFace("perplexed",2)
                                    ch_l "I guess you show initiative."
                                    $ L_Blush = 1
                            else:                
                                    call Statup("Laura", "Love", 50, -10) 
                                    call Statup("Laura", "Love", 80, -10)          
                                    call Statup("Laura", "Obed", 50, 10)  
                                    call LauraFace("angry")
                                    ch_l "That's a bit disturbing."

    elif Options[0] == "fondled":
            #Laura's response to being felt up.
            if L_FondleB + L_FondleP + L_FondleA >= 15:
                ch_l "I need your hands on me." 
            else:                
                ch_l "You could feel me up, if you wanted."

    elif Options[0] == "booked":
            #Laura's response after a Player gives her the books from the shop.
            ch_l "Hey, I read those books you gave me."
            menu:
                extend ""
                "Yeah?  Did you like them?":
                        call LauraFace("sly",2)
                        ch_l "They were. . .{i}interesting{/i}."
                "Good.  You looked like you could use to learn a thing or two from them.":                     
                        call Statup("Laura", "Love", 90, -3)          
                        call Statup("Laura", "Obed", 70, 5)            
                        call Statup("Laura", "Inbt", 50, 5) 
                        call LauraFace("angry")
                        ch_l "I don't see how."                
            $ L_Blush = 1
            $ L_Chat.append("book") 

    elif Options[0] == "lingerie":
            #Laura's response to being given lingerie.
            call LauraFace("sly",2)
            ch_l "That underwear ou got me was kind of uncomfortable, but I do like the look."
            $ L_Blush = 1
            $ L_Chat.append("lingerie") 

    elif Options[0] == "handy":
            #Laura's response after giving the Player a handjob.
            call LauraFace("sly",1)
            ch_l "I was thinking about having your cock in my hand the other day. . ."
            ch_l "You seemed to enjoy it."
            $ L_Blush = 0

    elif Options[0] == "blow":
            if "blow" not in L_Chat:
                    #Laura's response after giving the Player a blowjob.
                    call LauraFace("sly",2)
                    ch_l "Hey, so did you like that blowjob?"
                    menu:
                        extend ""
                        "You were totally amazing.":                            
                                    call Statup("Laura", "Love", 90, 5)            
                                    call Statup("Laura", "Inbt", 60, 10) 
                                    call LauraFace("normal",1)
                                    ch_l "Cool. Cool. . . "
                                    call LauraFace("sexy",1)
                                    ch_l "I'd like another taste sometime."
                        "Honestly? It was good. . .but you could use a little practice, I think.":
                                if ApprovalCheck("Laura", 300, "I") or not ApprovalCheck("Laura", 800):                     
                                    call Statup("Laura", "Love", 90, -5)          
                                    call Statup("Laura", "Obed", 60, 10)            
                                    call Statup("Laura", "Inbt", 50, 10) 
                                    call LauraFace("perplexed",1)
                                    ch_l "Yeah? Sorry to disappoint."
                                else:                              
                                    call Statup("Laura", "Obed", 70, 15)            
                                    call Statup("Laura", "Inbt", 50, 5) 
                                    call LauraFace("sexy",1)
                                    ch_l "Yeah? I suppose we could keep trying until I get it right."                                  
                        "I guess. If you're into weird sounds and too much teeth. Spoiler, I'm not.":                     
                                call Statup("Laura", "Love", 90, -10)          
                                call Statup("Laura", "Obed", 60, 10)   
                                call LauraFace("angry",2)
                                ch_l "Well, good luck with that then."
                    $ L_Blush = 1
                    $ L_Chat.append("blow") 
            else:
                    $ Line = renpy.random.choice(["I gotta tell you, your dick tastes great.", 
                            "I think I nearly dislocated my jaw last time.", 
                            "Let me know if you'd like another blowjob sometime.",
                            "Hmmm. . . [she mimes her tongue knocking against her cheek.]"])
                    ch_l "[Line]"

    elif Options[0] == "swallowed":
            #Laura's response after swallowing the Player's cum.
            if "swallow" in L_Chat:                
                ch_l "Hey, I wouldn't mind another taste of you some time."
            else:
                ch_l "So. . . the other day. . ."
                ch_l "That was the first time I'd really enjoyed the taste of jiz."
                call LauraFace("sly",1)
                ch_l "Good job!"
                $ L_Chat.append("swallow") 

    elif Options[0] == "facial":
            #Laura's response after taking a facial from the Player.
            ch_l "Hey. . .I know this is kind of odd. . ."
            call LauraFace("sexy",2)
            ch_l "I feel so {i}good{/i} with your jiz on my face."
            $ L_Blush = 1

    elif Options[0] == "sleepover":
            #Laura's response after sleeping with the Player.
            ch_l "I really enjoyed the other night."
            ch_l "It felt so safe sleeping next to someone else."

    elif Options[0] == "creampie":
            #Another of Laura's responses after having sex with the Player.
            "Laura draws close to you so she can whisper into your ear."
            ch_l "I can still feel you. . .running down the inside of my thigh."

    elif Options[0] == "sexed":
            #A final response from Laura after having sex with the Player.
            ch_l "So. . . you should know. . ."
            call LauraFace("sexy",2)
            ch_l ". . .lately when I've been flicking the bean. . ."
            ch_l "I've been thinking about you inside of me."
            $ L_Blush = 1

    elif Options[0] == "anal":
            #Laura's response after getting anal from the Player.
            call LauraFace("sly")
            ch_l "I did't really enjoy anal much."
            call LauraFace("sexy",1)
            ch_l "Until you, at least."
        
#    elif Options[0] == "boyfriend?":
#        call Laura_BF
#    elif Options[0] == "lover?":
#        call Laura_Love
#    elif Options[0] == "sir?":
#        call Laura_Sub
#    elif Options[0] == "master?":
#        call Laura_Master
#    elif Options[0] == "sexfriend?":
#        call Laura_Sexfriend
#    elif Options[0] == "fuckbuddy?":
#        call Laura_Fuckbuddy 
#    elif Options[0] == "daddy?":
#        call Laura_Daddy  
        
    elif Options[0] == "hate": # trinty lower then 50:
        $ Line = renpy.random.choice(["Get away from me.", 
                "I don't want to smell you near me.", 
                "Back off.",
                "Buzz off."])
        ch_l "[Line]"
        
    else: #all else fell through. . .
            $ D20 = renpy.random.randint(1, 15)        
            if D20 == 1:
                    call LauraFace("smile")
                    ch_l "I got a good grade on that bio test."
            elif D20 == 2:
                    call LauraFace("annoyed")
                    ch_l "If I have to hear him say \"I'm the best there is\" one more time, I swear I'm going ..."
            elif D20 == 3:
                    call LauraFace("surprised")
                    ch_l "Huh? Oh, sorry. I sort of spaced out. That's not like me."
            elif D20 == 4:
                    call LauraFace("sad")
                    ch_l "Oh, [L_Petname]. I was just remembering something. Don't worry about it."
            elif D20 == 5:
                    call LauraFace("smile")
                    ch_l "I had a good nap. It's nice to be somewhere I can just doze off without worry."
            elif D20 == 6:
                    call LauraFace("perplexed")
                    ch_l "Oh, [L_Petname]. I think I just saw Emma Frost staring at Cyclops. That's... wierd."
            elif D20 == 7:
                    call LauraFace("smile")
                    ch_l "I just got a new personal best time in the Danger Room."
            elif D20 == 8:
                    call LauraFace("sad")
                    ch_l "I like being here, but sometimes there's just so much noise..."
            elif D20 == 9:
                    call LauraFace("confused")
                    ch_l "I'm still trying to figure out what the mystery meat in the cafeteria was today."
                    ch_l "I have enhanced senses, this shouldn't be so difficult!"
            elif D20 == 10:
                    call LauraFace("smile")
                    ch_l "Kitty, Rogue and some of the others asked me if I wanted to go grab some ice cream with them tomorrow."
            elif D20 == 11:
                    call LauraFace("smile")
                    ch_l "I tried out a dance class like Kitty said. Apparently I'm good at it."
            elif D20 == 12:
                    call LauraFace("sad")
                    ch_l "I like talking to Kitty and the others. It makes me feel, I don't know. . ."
                    ch_l "{i}not{/i} like a really dangerous mutant who could kill everyone around me if I flipped out."
            elif D20 == 13:
                    call LauraFace("smile")
                    ch_l "Kitty and Rogue dared me to call Logan \"Dad\". I think we might've given him a heart attack."
            elif D20 == 14:
                    call LauraFace("sad")
                    ch_l "I like going out on missions, but catching up with what's been going on while I'm gone is always a pain."
            elif D20 == 15:
                    call LauraFace("perplexed")
                    ch_l "So they're called the \"Avengers\", but do they ever do any avenging?"
                    ch_l "At least the Fantastic Four really do things that are strange and fantastic."
            elif D20 == 16:
                    call LauraFace("perplexed")
                    ch_l "Have you ever been to New York? Sometimes I'm surprised anyone still wants to live there."
            elif D20 == 17:
                    call LauraFace("perplexed")
                    ch_l "Logan just walked up and told me that if I ever meet someone called. . ."
                    ch_l "\"Dead...Poole?\"...I should just go ahead and stab him in the face."
                    ch_l "What's up with that?"
            elif D20 == 18:
                    call LauraFace("smile")
                    ch_l "Don't tell anyone this, but I think Cyclops is kind of wound up tight."
            elif D20 == 19:
                    call LauraFace("confused")
                    ch_l "Do you smell something? Is that... nachos and... chocolate syrup?!"
            elif D20 == 20:
                    call LauraFace("smile")
                    ch_l "I like being able to just talk about nothing in particular. It's... nice."
            else:
                    call LauraFace("smile")
                    ch_l "You're fun to hang with."
        
    $ Line = 0
    return

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
label Laura_Flirt:
    
    if L_Loc == bg_current:         
        $ L_Chat[5] = 1                                         #can only flirt once per cycle. 
        menu:        
#            "Compliment her":
                
            "Say you love her":
                        call Love_You("Laura")
                        
            "Touch her cheek":                                                                              
                    call L_TouchCheek
            "Pat her head":
                    call L_Headpat
            "Kiss her cheek":                                                                            
                    "You lean over, tilt her head back, and kiss her on the cheek."                
                    if ApprovalCheck("Laura", 700, "L", TabM=1):
                        call LauraFace("perplexed", 2) 
                        call Statup("Laura", "Love", 90, 1)          
                        call Statup("Laura", "Obed", 40, 2) 
                        ch_l ". . ."
                        call LauraFace("sexy", 1, Eyes="side") 
                        ch_l "Huh."
                    elif ApprovalCheck("Laura", 500, "L", TabM=1):
                        call LauraFace("surprised", 1)
                        call Statup("Laura", "Love", 70, 2)
                        call Statup("Laura", "Love", 90, 1)          
                        call Statup("Laura", "Obed", 40, 2)            
                        call Statup("Laura", "Inbt", 20, 1) 
                        ch_l ". . . hey!"
                        ch_l "What's that about?"
                    elif ApprovalCheck("Laura", 300, "L", TabM=1):                    
                        call LauraFace("angry", 1)
                        call Statup("Laura", "Love", 90, -1)          
                        call Statup("Laura", "Obed", 60, 2)            
                        call Statup("Laura", "Inbt", 40, 1) 
                        ch_l "That's a bit forward."
                    else: 
                        call LauraFace("angry", 1)
                        call Statup("Laura", "Love", 90, -5)          
                        call Statup("Laura", "Obed", 90, 5)            
                        call Statup("Laura", "Inbt", 40, 3) 
                        ch_l "Keep back!"
                    if "addict laura" in P_Traits:
                        $ L_Addict -= 1
                        $ L_Addictionrate += 1
                        $ L_Addictionrate = 3 if L_Addictionrate < 3 else L_Addictionrate 
                   
            "Kiss her lips":                                                                                    #Kiss her
                    if ApprovalCheck("Laura", 1000, TabM=1) or ApprovalCheck("Laura", 600, "L", TabM=1):        
                        "You lean down, tilt her head back, and plant a kiss on her lips."
                    elif ApprovalCheck("Laura", 1000) or ApprovalCheck("Laura", 600, "L"):  
                        call LauraFace("bemused", 1)
                        $ L_Eyes = "side"         
                        call Statup("Laura", "Obed", 50, -5)            
                        call Statup("Laura", "Inbt", 40, 2) 
                        "You lean close for a kiss, but Laura gently elbows your ribs."
                        ch_l "Not here, [L_Petname]." 
                        return
                    else:                
                        call LauraFace("angry", 1)
                        call Statup("Laura", "Love", 90, -15)          
                        call Statup("Laura", "Obed", 50, -5)            
                        call Statup("Laura", "Inbt", 40, 5) 
                        "You lean close for a kiss, but Laura checks you onto your butt."
                        ch_l "Keep to yourself, [L_Petname]." 
                        return
                    if L_Kissed:
                            if ApprovalCheck("Laura", 800, "L", TabM=1):
                                call LauraFace("sexy", 1)
                                call Statup("Laura", "Love", 90, 2)          
                                call Statup("Laura", "Obed", 50, 2)
                                ch_l "Mmmmmmm. . ."
                            elif ApprovalCheck("Laura", 700, "L", TabM=1):
                                call LauraFace("sexy", 1)
                                call Statup("Laura", "Love", 90, 2)          
                                call Statup("Laura", "Obed", 50, 2) 
                                ch_l "Hmm, that's nice. . ."
                            elif ApprovalCheck("Laura", 550, "L", TabM=1):
                                call LauraFace("surprised", 1)
                                call Statup("Laura", "Love", 70, 1) 
                                call Statup("Laura", "Love", 90, 2)          
                                call Statup("Laura", "Obed", 50, 2) 
                                ch_l "I don't know about that."
                            elif ApprovalCheck("Laura", 300, "L", TabM=1):
                                call LauraFace("angry", 1)
                                call Statup("Laura", "Love", 90, -8)          
                                call Statup("Laura", "Obed", 60, 3)            
                                call Statup("Laura", "Inbt", 40, 2) 
                                ch_l "Back it off, [L_Petname]."
                            else: 
                                call LauraFace("angry", 1)
                                call Statup("Laura", "Love", 90, -15)          
                                call Statup("Laura", "Obed", 90, 6)            
                                call Statup("Laura", "Inbt", 40, 3) 
                                ch_l "Fuck off."
                            
                    else:                   #If this is the first kiss
                            if ApprovalCheck("Laura", 800, "L", TabM=1):
                                call LauraFace("surprised", 2)
                                call Statup("Laura", "Love", 95, 30)          
                                call Statup("Laura", "Obed", 50, 15)
                                call Statup("Laura", "Inbt", 50, 15)
                                call LauraFace("normal",Eyes="side")
                                ch_l ". . ."
                                call LauraFace("sexy",Eyes="side")
                                ch_l "Hmmm, that was nice. . ."
                                call LauraFace("sexy")
                            elif ApprovalCheck("Laura", 650, "L", TabM=1):
                                call LauraFace("surprised", 1)
                                call Statup("Laura", "Love", 80, 25)            
                                call Statup("Laura", "Obed", 50, 20)
                                call Statup("Laura", "Inbt", 50, 15)
                                ch_l " ! "
                                ch_l "I'm not sure what to do with that. . ."
                            elif ApprovalCheck("Laura", 500, "L", TabM=1):
                                call LauraFace("surprised", 1)            
                                call Statup("Laura", "Obed", 70, 20)
                                call Statup("Laura", "Inbt", 70, 20)
                                ch_l "What are you thinking, [L_Petname]?!"
                            elif ApprovalCheck("Laura", 800, TabM=1):
                                call LauraFace("angry", 1)
                                call Statup("Laura", "Love", 60, -10) 
                                call Statup("Laura", "Obed", 70, 30)
                                call Statup("Laura", "Inbt", 70, 20)
                                ch_l "What the hell, [L_Petname]?!"
                            else: 
                                call LauraFace("angry", 1)
                                call Statup("Laura", "Love", 60, -15) 
                                call Statup("Laura", "Obed", 70, 40)
                                call Statup("Laura", "Inbt", 70, 25)
                                ch_l "Fuck off."
                            
                    $ L_Kissed += 1  
                    if "addict laura" in P_Traits:
                        $ L_Addict -= 1
                        $ L_Addictionrate += 1
                        $ L_Addictionrate = 3 if L_Addictionrate < 3 else L_Addictionrate 
                        
                    if ApprovalCheck("Laura", 700, TabM=1):
                        if L_Love > L_Obed and L_Love > L_Inbt:
                            ch_l "I think I'd like some more."
                        elif L_Obed > L_Inbt:
                            ch_l "Did you want to continue?"
                        else:
                            ch_l "We could keep going, [L_Petname]."
                        menu:
                            "Keep kissing?"
                            "You know it.":
                                call Statup("Laura", "Lust", 60, 3)  
                                call Statup("Laura", "Love", 90, 1)
                                call Statup("Laura", "Love", 60, 3) 
                                call Statup("Laura", "Inbt", 50, 1)
                                call Laura_SexAct("kissing")
                                call Trig_Reset(1)
                                return
                            "Not now [[no].":
                                call LauraFace("bemused", 1) 
                                call Statup("Laura", "Lust", 40, 1) 
                                call Statup("Laura", "Lust", 60, 4) 
                                call Statup("Laura", "Obed", 70, 2)
                                call Statup("Laura", "Inbt", 50, 1)
                                ch_l "Ah, you were kidding."
                            "Nope.":
                                call LauraFace("sadside", 1)
                                call Statup("Laura", "Love", 80, -2) 
                                call Statup("Laura", "Obed", 70, 4)
                                call Statup("Laura", "Inbt", 50, 1)
                                ch_l "Ah, you were kidding."
                    else:
                        ch_l "Don't push me."
                    #End Kiss her
                
            "Hug her":                                                                                          #Hug her
                    if ApprovalCheck("Laura", 300, TabM=1):        
                        "You lean over and wrap Laura in a warm hug."
                    else:                
                        call LauraFace("angry", 1)
                        "You lean in with your arms wide, but Laura slips under you and takes a step back."
                        ch_l "What's was that, [L_Petname]?" 
                        return
                        
                    if L_SEXP >= 30: 
                        call Statup("Laura", "Lust", 60, 3) 
                        call Statup("Laura", "Love", 90, 1)          
                        call Statup("Laura", "Obed", 90, 3)            
                        call Statup("Laura", "Inbt", 90, 2) 
                        call LauraFace("sexy")
                        ch_l "I think you're flipping my switch, [L_Petname]."
                    elif ApprovalCheck("Laura", 800, "L", TabM=1):
                        call LauraFace("sexy")
                        call Statup("Laura", "Love", 90, 1)          
                        call Statup("Laura", "Obed", 40, 2)            
                        call Statup("Laura", "Inbt", 30, 1) 
                        ch_l "Hmmmmm. . ."
                    elif ApprovalCheck("Laura", 550, TabM=1):
                        call LauraFace("surprised", 1)
                        call Statup("Laura", "Love", 90, 1)  
                        call Statup("Laura", "Love", 70, 1)        
                        call Statup("Laura", "Obed", 40, 2)            
                        call Statup("Laura", "Inbt", 30, 1)  
                        ch_l "Um, [L_Petname]? What is this?"
                    elif ApprovalCheck("Laura", 450, TabM=1):
                        call LauraFace("angry", 1)  
                        call Statup("Laura", "Love", 70, 1)        
                        call Statup("Laura", "Obed", 50, 3)            
                        call Statup("Laura", "Inbt", 30, 2) 
                        ch_l "This is making me uncomfortable. . ."
                    else: 
                        call LauraFace("angry", 1) 
                        call Statup("Laura", "Love", 40, -4)       
                        call Statup("Laura", "Obed", 50, 4)            
                        call Statup("Laura", "Inbt", 30, 2) 
                        ch_l "Hey, back off."   
                        
            "Slap her ass" if L_Loc == bg_current:                                                              #Slap her ass
                    call L_Slap_Ass
                
            "Pinch her ass":                                                                                    #Pinch her ass
                    call LauraFace("surprised", 1)
                    if L_SEXP >= 5 and ApprovalCheck("Laura", 700, TabM=1):        
                        "You come up to Laura from behind and quickly pinch her butt."
                    else:                
                        "You come up to Laura from behind and quickly pinch her butt."
                        call LauraFace("angry")
                        "She slaps your hand away and rounds on you."
                        ch_l "What are you thinking?" 
                        return
                        
                    if L_SEXP >= 40: 
                        call Statup("Laura", "Lust", 60, 3) 
                        call Statup("Laura", "Love", 90, 1)           
                        call Statup("Laura", "Obed", 60, 2)          
                        call Statup("Laura", "Obed", 90, 1)            
                        call Statup("Laura", "Inbt", 50, 3) 
                        call LauraFace("sexy")
                        ch_l "Oooh! Getting rough?"
                    elif ApprovalCheck("Laura", 800, "L", TabM=1):
                        call LauraFace("sexy")
                        call Statup("Laura", "Love", 90, 1)           
                        call Statup("Laura", "Obed", 60, 2)          
                        call Statup("Laura", "Obed", 90, 1)            
                        call Statup("Laura", "Inbt", 50, 2) 
                        ch_l "You like the way that feels, [L_Petname]?"
                    elif ApprovalCheck("Laura", 1000, TabM=1):
                        call LauraFace("surprised")
                        call Statup("Laura", "Love", 90, 1)           
                        call Statup("Laura", "Obed", 60, 3)          
                        call Statup("Laura", "Obed", 90, 2)            
                        call Statup("Laura", "Inbt", 50, 2) 
                        ch_l "Wha?!"
                    elif ApprovalCheck("Laura", 800, TabM=1):
                        call LauraFace("angry")
                        call Statup("Laura", "Love", 90, -4)           
                        call Statup("Laura", "Obed", 60, 4)          
                        call Statup("Laura", "Obed", 90, 3)            
                        call Statup("Laura", "Inbt", 50, 1) 
                        ch_l "Hey!"
                    else: 
                        call LauraFace("angry")
                        call Statup("Laura", "Love", 90, -8)           
                        call Statup("Laura", "Obed", 60, 5)          
                        call Statup("Laura", "Obed", 90, 4)            
                        call Statup("Laura", "Inbt", 50, 2)
                        ch_l "Ouch! What the fuck?!"  
                    
                    
            "Grab her tit":                                                                                     #Grab her tit
                    call LauraFace("surprised", 1)
                    if L_SEXP >= 5 and ApprovalCheck("Laura", 700, TabM=2):        
                        "You come up to Laura and quickly honk her boob."
                    else:             
                        "You come up to Laura and quickly honk her boob."
                        call LauraFace("angry")
                        show Laura_Sprite
                        with vpunch
                        "She flips you onto your back."
                        ch_l "What the fuck?!" 
                        return
                        
                    if L_SEXP >= 40: 
                        call Statup("Laura", "Lust", 60, 5) 
                        call Statup("Laura", "Love", 90, 2) 
                        call LauraFace("sexy")
                        ch_l "Hmm, that's pleasant."
                        $ Count = 10
                    elif ApprovalCheck("Laura", 850, "L", TabM=1):
                        call LauraFace("sexy")
                        call Statup("Laura", "Lust", 60, 2) 
                        call Statup("Laura", "Love", 90, 1) 
                        ch_l "Hmm, are you enjoying that as much as I am?"
                        $ Count = 7
                    elif ApprovalCheck("Laura", 1200, TabM=1):
                        call LauraFace("perplexed")  
                        call Statup("Laura", "Lust", 60, 1)         
                        ch_l "That's a bit inappropriate, [L_Petname]."
                        $ Count = 5
                    elif ApprovalCheck("Laura", 900, TabM=1):
                        call LauraFace("angry",Eyes="down")
                        call Statup("Laura", "Love", 90, -5)          
                        call Statup("Laura", "Obed", 90, 4)            
                        call Statup("Laura", "Inbt", 90, 1) 
                        ch_l "Are you going to move that hand or will I have to?"
                        call LauraFace("angry")
                        $ Count = 3
                    else: 
                        call LauraFace("angry")
                        call Statup("Laura", "Love", 90, -8)          
                        call Statup("Laura", "Obed", 90, 5)            
                        call Statup("Laura", "Inbt", 90, 2) 
                        $ Laura_Arms = 2
                        $ L_Claws = 1
                        ch_l "You wanna lose that hand?" 
                        $ Count = 2
                              
                    call Statup("Laura", "Obed", 70, 3)            
                    call Statup("Laura", "Inbt", 70, 2) 
                    ch_l "Are you satisfied?"
                    while Count > 0:
                        if Count == 6:
                            call LauraFace("sexy", 1)
                            ch_l "That's pretty comforting. . ."  
                            call Statup("Laura", "Lust", 90, 2)       
                            call Statup("Laura", "Inbt", 70, 1)
                        elif Count == 3:
                            call LauraFace("perplexed")
                            call Statup("Laura", "Lust", 90, 1) 
                            ch_l "I like it, but maybe stop for now?"
                        elif Count == 2:
                            call LauraFace("angry")
                            call Statup("Laura", "Love", 90, -1) 
                            ch_l "Ok, that's enough now."
                        elif Count == 1:
                            call LauraFace("angry")
                            ch_l "Take a step back, [L_Petname]!"
                            call Statup("Laura", "Love", 90, -5) 
                            show Laura_Sprite
                            with vpunch
                            "She gives you a quick shove."
                            $ Count = 1                     
                        $ Count -= 1 if Count >= 0 else 0
                            
                        if Count > 0:
                            menu:
                                "Your hand is still on her chest."
                                "Let go immediately":
                                    if Count >= 7:
                                        ch_l "I didn't really mind it. . ."  
                                        call Statup("Laura", "Lust", 60, 2)         
                                        call Statup("Laura", "Inbt", 70, 1) 
                                    elif Count <= 4:
                                        ch_l "Probably for the best."
                                    $ Count = 0
                                    
                                "Honk it again and let go":
                                    if Count >= 7:
                                        ch_l "I didn't mind it so much. . ."          
                                        call Statup("Laura", "Lust", 60, 4) 
                                        call Statup("Laura", "Inbt", 70, 1)
                                    elif Count >= 4:
                                        ch_l "Heh."
                                    else:
                                        call LauraFace("angry")
                                        ch_l "Asshole."
                                    call Statup("Laura", "Obed", 70, 3)            
                                    call Statup("Laura", "Inbt", 70, 2)
                                    $ Count = 0 
                                        
                                "Fondle it a little":                            
                                    if L_FondleB and ApprovalCheck("Laura", 1100, TabM=2):                                
                                        call LauraFace("sexy",1)
                                        $ L_Eyes = "closed"
                                        call Statup("Laura", "Lust", 90, 5) 
                                    else:
                                        call LauraFace("perplexed")
                                        call Statup("Laura", "Lust", 90, 2) 
                                        $ Count -= 1
                                    call Statup("Laura", "Obed", 70, 4)            
                                    call Statup("Laura", "Inbt", 70, 2)
                                    ch_l "Hmm. . ."
                                    
                                "Just leave it there.":
                                    if Count == 5:
                                        call LauraFace("perplexed")
                                        call Statup("Laura", "Lust", 90, 3) 
                                        ch_l "Huh."                            
                                    elif Count == 2:
                                        call LauraFace("perplexed")
                                        call Statup("Laura", "Lust", 90, 1) 
                                        ch_l "This is getting uncomfortable."
                                    call Statup("Laura", "Obed", 70, 2)            
                                    call Statup("Laura", "Inbt", 70, 1)
                                    
                            
                    $ Laura_Arms = 1
                    $ L_Claws = 0 
                    if L_FondleB and ApprovalCheck("Laura", 1200, TabM = 3): 
                        call LauraFace("sexy", 1)
                        ch_l "We could keep going. . ."
                        menu:
                            extend ""
                            "Yeah!":
                                call Statup("Laura", "Lust", 60, 5) 
                                call Statup("Laura", "Love", 90, 2)          
                                call Statup("Laura", "Obed", 60, 3)            
                                call Statup("Laura", "Inbt", 60, 3) 
                                call Laura_SexAct("breasts")
                                call Trig_Reset(1)
                                return
                            "Nah, that was enough.":
                                call LauraFace("sad", 1)
                                call Statup("Laura", "Lust", 60, 2) 
                                call Statup("Laura", "Love", 90, -2)          
                                call Statup("Laura", "Obed", 60, 4)            
                                call Statup("Laura", "Inbt", 60, 2) 
                                ch_l "Fine."
                    elif ApprovalCheck("Laura", 900, TabM = 3):  
                        $ L_Brows = "confused"
                        $ L_Eyes = "sexy"
                        $ L_Mouth = "smile"
                        ch_l "You enjoyed that?"
                    elif ApprovalCheck("Laura", 900): 
                        call LauraFace("angry", 1)
                        ch_l "You do that in public?"
                    else:
                        call LauraFace("angry", 1)
                        ch_l "Keep your hands to yourself!"
                        
                    
            "Rub her shoulders":                                                                                #Rub her shoulders
                    "You come up to Laura from behind and gently rub her shoulders."
                    if L_SEXP >= 30:
                        call LauraFace("sexy") 
                        call Statup("Laura", "Lust", 60, 3) 
                        call Statup("Laura", "Love", 90, 2)
                        "She sinks back into your hands"
                        ch_l "Hmm, are you thinking what I'm thinking, [L_Petname]?"
                    elif ApprovalCheck("Laura", 650, "L"):
                        call LauraFace("sexy")
                        call Statup("Laura", "Lust", 60, 1) 
                        call Statup("Laura", "Love", 90, 2)
                        ch_l "Hmmm, that's nice, [L_Petname]."
                    elif ApprovalCheck("Laura", 500):
                        call LauraFace("surprised", 1)
                        call Statup("Laura", "Love", 90, 1)
                        ch_l "Oh, hey there, [L_Petname]."
                    elif ApprovalCheck("Laura", 400):
                        call LauraFace("angry", 1)
                        call Statup("Laura", "Love", 90, -1)
                        if Taboo:
                            ch_l "Maybe take a step back, [L_Petname]?"
                        else:
                            ch_l "Whoa, back it up."
                    else: 
                        call LauraFace("angry", 1)
                        "She slaps your hands away."
                        ch_l "No hands or you lose them."           
                    call Statup("Laura", "Obed", 30, 3)            
                    call Statup("Laura", "Inbt", 30, 2) 
              
            "Ask for her panties":
                    call Laura_AskPanties
                                        
            "Never mind [[exit]":
                    $ L_Chat[5] = 0  
                    return
    else:
        "Laura isn't around."
            
    return



label Laura_AskPanties(Store = 0):
    $ Store = Tempmod  
    $ Line = 0
    if not L_Panties or L_Panties == "shorts":
        if ApprovalCheck("Laura", 900):
            call LauraFace("sexy", 1)
            call Statup("Laura", "Lust", 80, 5) 
            call Statup("Laura", "Lust", 60, 5) 
            call Statup("Laura", "Lust", 40, 10)            
            call Statup("Laura", "Inbt", 60, 5)            
            call Statup("Laura", "Inbt", 30, 10) 
            ch_l "I'm not wearing any."
        elif L_Over == "towel" or not L_Legs:
            call LauraFace("bemused", 2)
            ch_l "Did you think I was wearing any?"            
        else:
            call LauraFace("bemused", 2, Eyes="side")
            call Statup("Laura", "Lust", 80, 5) 
            call Statup("Laura", "Lust", 60, 5) 
            call Statup("Laura", "Lust", 40, 10)            
            call Statup("Laura", "Inbt", 60, 5)   
            ch_l "I'm not wearing any at the moment."         
       
    else:
        if L_SeenPussy and ApprovalCheck("Laura", 500): #You've seen her Pussy.
            $ Tempmod += 15
        elif L_SeenPanties and ApprovalCheck("Laura", 500): #You've seen her panties.
            $ Tempmod += 5 
        if "exhibitionist" in L_Traits:
            $ Tempmod += (Taboo * 5)
        if "dating" in L_Traits or "sex friend" in L_Petnames and not Taboo:
            $ Tempmod += 10
        if "no bottomless" in L_RecentActions: 
            $ Tempmod -= 20
        
        $ Line = 0
        if L_Legs == "pants" or HoseNum("Laura") >= 10: 
            if ApprovalCheck("Laura", 1000, "OI", TabM = 2) or "exhibitionist" in L_Traits:   
                $ Line = "here"
            elif ApprovalCheck("Laura", 900, TabM = 2):
                $ Line = "change"
                
        elif L_Legs == "skirt":
            if ApprovalCheck("Laura", 600, "OI", TabM = 2) or "exhibitionist" in L_Traits:   
                $ Line = "here"
            elif ApprovalCheck("Laura", 1100, TabM = 2):
                $ Line = "change"
                
        else:
            if ApprovalCheck("Laura", 1200, TabM = 2) or "exhibitionist" in L_Traits:
                $ Line = "here"
        
        
        if Line == "here":                              
                #She's agreed to change and will do it here
                call LauraFace("sly")                          
                if L_Legs == "skirt":      
                    call Statup("Laura", "Obed", 60, 4)            
                    call Statup("Laura", "Inbt", 60, 4)
                else: #no pants or skirt         
                    call Statup("Laura", "Obed", 60, 6)            
                    call Statup("Laura", "Inbt", 60, 6) 
                
                call Statup("Laura", "Lust", 60, 5)    
                call Remove_Panties("Laura")
                    
                if Taboo:
                    call Statup("Laura", "Lust", 60, 5) 
                    if "exhibitionist" in L_Traits: 
                        call Statup("Laura", "Lust", 80, 5)
                        call Statup("Laura", "Lust", 200, 5)    
                    call Statup("Laura", "Obed", 80, 10)            
                    call Statup("Laura", "Inbt", 80, 10)        
            
        elif Line:                                      
                    #She's agreed to change, but leaves the room to do it.       
                    call LauraFace("bemused", 1) 
                    menu:
                        ch_l "Could you turn around?"
                        "OK.": 
                            call Statup("Laura", "Love", 90, 5) 
                            call LauraFace("smile", 1)                                             
                            ch_l "Thanks."
                            call LauraFace("sly", 1) 
                            call Statup("Laura", "Lust", 60, 2)         
                            call Statup("Laura", "Obed", 60, 4)            
                            call Statup("Laura", "Inbt", 60, 4)
                            show blackscreen onlayer black 
                            "You turn around"   
                            $ L_DailyActions.append("pantyless")
                            call LauraOutfit                             
                            hide blackscreen onlayer black 
                            if Taboo:              
                                call Quick_Taboo("Laura")
                            "When you turn back, she quietly hands you her balled up panties."
                            $ Line = 0
                            
                        "And miss the show?":
                            if ApprovalCheck("Laura", 1000, "LI"): 
                                call Statup("Laura", "Lust", 70, 5)          
                                call Statup("Laura", "Obed", 60, 5)            
                                call Statup("Laura", "Inbt", 60, 5) 
                                call LauraFace("sly", 1) 
                                ch_l "Oh, you'd like to watch?"
                            else:                 
                                call LauraFace("angry", 1) 
                                call Statup("Laura", "Love", 90, -5)          
                                call Statup("Laura", "Obed", 60, -3)            
                                call Statup("Laura", "Inbt", 60, 5) 
                                ch_l "Yes."
                                $ Line = 0
                                
                        "Nope, I'm staying.":
                            if ApprovalCheck("Laura", 600, "OI"): 
                                call LauraFace("bemused", 1) 
                                call Statup("Laura", "Lust", 70, 5)          
                                call Statup("Laura", "Obed", 60, 10)            
                                call Statup("Laura", "Inbt", 60, 5) 
                                ch_l "Ok."
                                call LauraFace("sexy") 
                            else:        
                                call LauraFace("angry", 1) 
                                call Statup("Laura", "Love", 90, -10)          
                                call Statup("Laura", "Obed", 60, -5)            
                                call Statup("Laura", "Inbt", 60, 5) 
                                ch_l "I think that's rude under the circumstances."
                                $ Line = 0
                                
                    if Line:                                            #She agreed to stay  
                                call LauraFace("sly", 1) 
                                if L_Legs or HoseNum("Laura") >= 10:   
                                        call Statup("Laura", "Lust", 60, 5)         
                                        call Statup("Laura", "Obed", 60, 3)            
                                        call Statup("Laura", "Inbt", 60, 5)  
                                        
                                call Remove_Panties("Laura") 
                                
        else:                                           #She refuses.    
            call LauraFace("angry", 2)                        
            if not ApprovalCheck("Laura", 500):
                call Statup("Laura", "Lust", 60, 5) 
                call Statup("Laura", "Love", 90, -10)          
                call Statup("Laura", "Obed", 60, 3)            
                call Statup("Laura", "Inbt", 60, 3) 
                ch_l "Why do you think I would?"
                $ L_RecentActions.append("angry")
                $ L_DailyActions.append("angry")   
                
            elif not ApprovalCheck("Laura", 500, TabM = 5):
                call Statup("Laura", "Lust", 60, 5) 
                call Statup("Laura", "Love", 90, -5)          
                call Statup("Laura", "Obed", 60, 5)            
                call Statup("Laura", "Inbt", 60, 5) 
                ch_l "In public?"                                
                $ L_RecentActions.append("angry")
                $ L_DailyActions.append("angry")   
                
            else:
                call LauraFace("bemused", 2)
                call Statup("Laura", "Lust", 60, 3)            
                call Statup("Laura", "Inbt", 60, 1)
                if Taboo:            
                    call Statup("Laura", "Inbt", 60, 2)
                    
                if L_Love >= L_Inbt or L_Obed >= L_Inbt:
                    ch_l "Maybe someday, [L_Petname]."
                else:
                    call LauraFace("perplexed")       
                    call Statup("Laura", "Obed", 60, -2)    
                    ch_l "Why would you want that?"
            $ L_Blush = 0
                
    $ Tempmod = Store       
    $ Line = 0
    return

    # End Ask for Panties   //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //


# Laura Control interface ///////////////////
label Laura_Controls:
    menu:
        "I'd like you to call me something else":
            call Laura_Names            
            return
        "I'd like you to come over for some action." if L_Loc != bg_current:
            ch_l "Ok, I'll be right over."
            $ L_Loc = bg_current 
            call Set_The_Scene
            call Laura_SexMenu
            return
        "I'd like to get busy." if L_Loc == bg_current:
            ch_l "How do you mean?"
            call Laura_SexMenu
            return
        "I want you to stop taking your own initiative." if "sub" not in L_Traits:
            $ L_Traits.append("sub")
            ch_l "Ok."                
        "Exit.":
            return
    jump Laura_Controls
return

# start Laura_Gifts//////////////////////////////////////////////////////////
label Laura_Gifts:  
    if P_Inventory == []:
        "You don't have anything to give her."
        return
    menu:
        "What would you like to give her?"
        "Toys and books":
            menu:
                "Give her a dildo." if "dildo" in P_Inventory: 
                    #If you have a Dildo, you'll give it.
                    $ Count = L_Inventory.count("dildo")
                    if "dildo" not in L_Inventory:                            
                        "You give Laura the dildo."
                        $ L_Blush = 1
                        $ Laura_Arms = 2
                        $ L_Held = "dildo"
                        if ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "I"):                    
                            call LauraFace("smile")
                            $ P_Inventory.remove("dildo")
                            $ L_Inventory.append("dildo")
                            call Statup("Laura", "Love", 200, 30)
                            call Statup("Laura", "Obed", 200, 30)
                            call Statup("Laura", "Inbt", 200, 30)
                            ch_l "Oh, cool, I've wanted one of these. . ."
                            call Statup("Laura", "Lust", 89, 10)
                            call Statup("Laura", "Lust", 89, 10)
                        elif ApprovalCheck("Laura", 800) or ApprovalCheck("Laura", 300, "I"):
                            call LauraFace("confused")
                            $ P_Inventory.remove("dildo")
                            $ L_Inventory.append("dildo")
                            call Statup("Laura", "Love", 200, 10)
                            call Statup("Laura", "Obed", 200, 10)
                            call Statup("Laura", "Inbt", 200, 10)
                            ch_l "Huh, you're a weird gift giver."  
                            call Statup("Laura", "Lust", 89, 5)
                            call Statup("Laura", "Lust", 89, 10)
                            call LauraFace("smile")
                            ch_l "It's very thoughtful though."
                        elif "offered gift" in L_DailyActions:
                            call LauraFace("angry")
                            "She hands it back to you."
                            ch_l "I said I can't take something like this."     
                        else:
                            call LauraFace("angry")
                            call Statup("Laura", "Love", 50, -20)
                            call Statup("Laura", "Obed", 20, 10)
                            call Statup("Laura", "Inbt", 20, 20)                    
                            ch_l "I don't think you should just be handing these out to random chicks."                     
                            call Statup("Laura", "Lust", 89, 10)
                            "She hands it back to you."
                            $ L_DailyActions.append("offered gift") 
                    elif Count == 1:
                        ch_l "I don't know if I need another. . ."
                    else: 
                        ch_l "I'm running out of space at this point."
                    $ L_Held = 0
                    $ Laura_Arms = 1
                    
                    
                "Give her the vibrator." if "vibrator" in P_Inventory: 
                    #If you have a vibrator, you'll give it.
                    if "vibrator" not in L_Inventory:                            
                        "You give Laura the Shocker Vibrator."
                        $ L_Blush = 1
                        $ Laura_Arms = 2
                        $ L_Held = "vibrator"
                        if ApprovalCheck("Laura", 700):                    
                            call LauraFace("confused")
                            $ P_Inventory.remove("vibrator")
                            $ L_Inventory.append("vibrator")
                            call Statup("Laura", "Love", 200, 30)
                            call Statup("Laura", "Obed", 200, 30)
                            call Statup("Laura", "Inbt", 200, 30)
                            ch_l "This is. . . [[bzzzt]- "                  
                            call LauraFace("sly")
                            call Statup("Laura", "Lust", 89, 10)
                            ch_l "-some kind of sex thing, huh. . ."
                        elif ApprovalCheck("Laura", 400):
                            call LauraFace("confused")
                            $ P_Inventory.remove("vibrator")
                            $ L_Inventory.append("vibrator")
                            call Statup("Laura", "Love", 200, 10)
                            call Statup("Laura", "Obed", 200, 10)
                            call Statup("Laura", "Inbt", 200, 10)
                            ch_l "This is. . . [[bzzzt]- "                  
                            call LauraFace("sly")
                            call Statup("Laura", "Lust", 89, 10)
                            ch_l "-oooh. . ."
                        elif "offered gift" in L_DailyActions:
                            call LauraFace("angry")
                            "She hands it back to you."
                            ch_l "I don't want it."  
                        else:
                            call LauraFace("angry")
                            call Statup("Laura", "Love", 50, -20)
                            call Statup("Laura", "Obed", 20, 10)
                            call Statup("Laura", "Inbt", 20, 20)                    
                            ch_l "I don't need it."                     
                            call Statup("Laura", "Lust", 89, 5)
                            "She hands it back to you."
                            $ L_DailyActions.append("offered gift") 
                    else: 
                        ch_l "I already have one of these."
                    $ L_Held = 0
                    $ Laura_Arms = 1
                    
                "Give her the \"Dazzler and Longshot\" book." if "Dazzler and Longshot" in P_Inventory: 
                    #If you have a vibrator, you'll give it.
                    if "Dazzler and Longshot" not in L_Inventory:                            
                        "You give Laura the book."
                        $ L_Blush = 1
                        if ApprovalCheck("Laura", 600, "L"):                    
                            call LauraFace("smile")
                            ch_l "A love story?"
                            call Statup("Laura", "Lust", 89, 10)
                        else:
                            call LauraFace("confused")
                            ch_l "Huh. Is there a movie?"  
                            call LauraFace("bemused")       
                        $ P_Inventory.remove("Dazzler and Longshot")
                        $ L_Inventory.append("Dazzler and Longshot") 
                        call Statup("Laura", "Love", 200, 50) 
                    else: 
                        ch_l "I already have one of those."                
                    
                "Give her the \"256 Shades of Grey\" book." if "256 Shades of Grey" in P_Inventory: 
                    #If you have a book, you'll give it.
                    if "256 Shades of Grey" not in L_Inventory:                            
                        "You give Laura the book."
                        $ L_Blush = 1
                        if ApprovalCheck("Laura", 500, "O"):                    
                            call LauraFace("bemused")
                            ch_l "Looks dirty."
                            call Statup("Laura", "Lust", 89, 10)
                        else:
                            call LauraFace("confused") 
                            ch_l "I'll give it a look."  
                            call LauraFace("bemused")             
                        $ P_Inventory.remove("256 Shades of Grey")
                        $ L_Inventory.append("256 Shades of Grey")                    
                        call Statup("Laura", "Obed", 200, 50)  
                    else: 
                        ch_l "I already have one of those."                
                    
                "Give her the \"Avengers Tower Penthouse\" book." if "Avengers Tower Penthouse" in P_Inventory: 
                    #If you have a book, you'll give it.
                    if "Avengers Tower Penthouse" not in L_Inventory:                            
                        "You give Laura the book."
                        $ L_Blush = 1
                        if ApprovalCheck("Laura", 500, "I"):                    
                            call LauraFace("bemused")
                            ch_l "This is pretty hot. . ."
                            call Statup("Laura", "Lust", 89, 10)
                        else:
                            call LauraFace("confused")
                            ch_l "Huh. . . ok."  
                            call LauraFace("bemused")               
                        $ P_Inventory.remove("Avengers Tower Penthouse")
                        $ L_Inventory.append("Avengers Tower Penthouse")                    
                        call Statup("Laura", "Inbt", 200, 50)  
                    else: 
                        ch_l "I already have one of those." 
            
                "Never mind":
                    pass
        "Clothing":    
            menu:
                "Give her the corset." if "l corset" in P_Inventory: 
                    #If you have a bra, you'll give it.
                    if "corset" not in L_Inventory:                            
                        "You give Laura the corset."
                        if ApprovalCheck("Laura", 1000):                    
                            call LauraFace("bemused")
                            $ P_Inventory.remove("l corset")
                            $ L_Inventory.append("corset")
                            call Statup("Laura", "Love", 200, 20)
                            call Statup("Laura", "Obed", 200, 20)
                            call Statup("Laura", "Inbt", 200, 10)
                            ch_l "I'd look good in this, right?"
                            call Statup("Laura", "Lust", 89, 10)
                        elif ApprovalCheck("Laura", 700):
                            call LauraFace("confused",1)
                            $ P_Inventory.remove("l corset")
                            $ L_Inventory.append("corset")
                            call Statup("Laura", "Love", 200, 15)
                            call Statup("Laura", "Obed", 200, 20)
                            call Statup("Laura", "Inbt", 200, 10)
                            ch_l "This is. . . kinda cool. . ."                    
                            call LauraFace("bemused",1)
                        elif ApprovalCheck("Laura", 600):
                            call LauraFace("confused",2)
                            $ P_Inventory.remove("l corset")
                            $ L_Inventory.append("corset")
                            call Statup("Laura", "Love", 200, 10)
                            call Statup("Laura", "Obed", 200, 15)
                            call Statup("Laura", "Inbt", 200, 15)
                            ch_l "I don't know why you'd give me this, it's not like I'd wear it. . ."                     
                            call LauraFace("bemused",1)
                        elif "no gift bra" in L_DailyActions:
                            call LauraFace("angry",2)
                            ch_l "I just told you no."   
                        else:
                            call LauraFace("angry",2)
                            call Statup("Laura", "Love", 50, -10)
                            call Statup("Laura", "Obed", 20, 10)
                            call Statup("Laura", "Inbt", 20, 20)  
                            if "no gift panties" in L_DailyActions:                    
                                ch_l "I don't want this either."                       
                            else:                   
                                ch_l "You have too much time on your hands."                     
                            call Statup("Laura", "Lust", 89, 5)
                            $ L_Blush = 1
                            "She hands it back to you."
                            $ L_RecentActions.append("no gift bra")                      
                            $ L_DailyActions.append("no gift bra") 
                    else: 
                        ch_l "I already have one of those."                
                  
                "Give her the lace corset." if "l lace corset" in P_Inventory: 
                    #If you have a bra, you'll give it.
                    if "lace corset" not in L_Inventory:                            
                        "You give Laura the lace corset."
                        if ApprovalCheck("Laura", 1200):                    
                            call LauraFace("bemused")
                            $ P_Inventory.remove("l lace corset")
                            $ L_Inventory.append("lace corset")
                            call Statup("Laura", "Love", 200, 25)
                            call Statup("Laura", "Obed", 200, 30)
                            call Statup("Laura", "Inbt", 200, 20)
                            ch_l "You think this'd look good on me?"
                            call Statup("Laura", "Lust", 89, 10)
                        elif ApprovalCheck("Laura", 1000):
                            call LauraFace("confused",1)
                            $ P_Inventory.remove("l lace corset")
                            $ L_Inventory.append("lace corset")
                            call Statup("Laura", "Love", 200, 20)
                            call Statup("Laura", "Obed", 200, 30)
                            call Statup("Laura", "Inbt", 200, 15)
                            ch_l "This is. . . kinda flimsy. . ."                    
                            call LauraFace("bemused",1)
                        elif ApprovalCheck("Laura", 800):
                            call LauraFace("confused",2)
                            $ P_Inventory.remove("l lace corset")
                            $ L_Inventory.append("lace corset")
                            call Statup("Laura", "Love", 200, 20)
                            call Statup("Laura", "Obed", 200, 20)
                            call Statup("Laura", "Inbt", 200, 25)
                            ch_l "I don't know why you'd give me this, it's not like I'd wear it. . ."                     
                            call LauraFace("bemused",1)
                        elif "no gift bra" in L_DailyActions:
                            call LauraFace("angry",2)
                            ch_l "I just told you no."   
                        else:
                            call LauraFace("angry",2)
                            call Statup("Laura", "Love", 50, -10)
                            call Statup("Laura", "Obed", 20, 10)
                            call Statup("Laura", "Inbt", 20, 20)  
                            if "no gift panties" in L_DailyActions:                    
                                ch_l "I don't want this either."                       
                            else:                   
                                ch_l "You have too much time on your hands."                     
                            call Statup("Laura", "Lust", 89, 5)
                            $ L_Blush = 1
                            "She hands it back to you."
                            $ L_RecentActions.append("no gift bra")                      
                            $ L_DailyActions.append("no gift bra") 
                    else: 
                        ch_l "I already have one of those."       
                        
                "Give her the lace panties." if "l lace panties" in P_Inventory: 
                    #If you have a bra, you'll give it.
                    if "lace panties" not in L_Inventory:                            
                        "You give Laura the lace panties."
                        $ L_Blush = 1
                        if ApprovalCheck("Laura", 1200):                    
                            call LauraFace("bemused")
                            $ P_Inventory.remove("l lace panties")
                            $ L_Inventory.append("lace panties")
                            call Statup("Laura", "Love", 200, 20)
                            call Statup("Laura", "Obed", 200, 30)
                            call Statup("Laura", "Inbt", 200, 30)
                            ch_l "These are pretty hot. . ."
                            call Statup("Laura", "Lust", 89, 10)
                        elif ApprovalCheck("Laura", 900):
                            call LauraFace("confused",1)
                            $ P_Inventory.remove("l lace panties")
                            $ L_Inventory.append("lace panties")
                            call Statup("Laura", "Love", 200, 20)
                            call Statup("Laura", "Obed", 200, 25)
                            call Statup("Laura", "Inbt", 200, 20)
                            ch_l "These are kinda flimsy. . ."                  
                            call LauraFace("bemused",1)
                        elif ApprovalCheck("Laura", 700):
                            call LauraFace("confused",2)
                            $ P_Inventory.remove("l lace panties")
                            $ L_Inventory.append("lace panties")
                            call Statup("Laura", "Love", 200, 20)
                            call Statup("Laura", "Obed", 200, 20)
                            call Statup("Laura", "Inbt", 200, 25)
                            ch_l "I don't think I'd wear these. . ."                  
                            call LauraFace("bemused",1)
                            ch_l "But I might need to do laundry. . ." 
                        elif "no gift panties" in L_DailyActions:
                            call LauraFace("angry",2)
                            ch_l "My answer's still no, stop asking!"                      
                        else:
                            call LauraFace("angry",2)
                            call Statup("Laura", "Love", 50, -15)
                            call Statup("Laura", "Obed", 20, 10)
                            call Statup("Laura", "Inbt", 20, 20)
                            if "no gift bra" in L_DailyActions:                    
                                ch_l "I don't want these either!" 
                            elif L_SeenPanties:
                                ch_l "Did you not like the ones I had?"                          
                            else:
                                ch_l "You don't need to worry about my underwear."                     
                            call Statup("Laura", "Lust", 89, 5)
                            $ L_Blush = 1
                            "She hands them back to you."
                            $ L_RecentActions.append("no gift panties")                      
                            $ L_DailyActions.append("no gift panties") 
                    else: 
                        ch_l "I already have one of those."                
                              
                "Give her the bikini top." if "l bikini top" in P_Inventory: 
                    #If you have a bra, you'll give it.
                    if "bikini top" not in L_Inventory:                            
                        "You give Laura the bikini top."
                        $ L_Blush = 1
                        if ApprovalCheck("Laura", 1000):                    
                            call LauraFace("bemused")
                            $ P_Inventory.remove("l bikini top")
                            $ L_Inventory.append("bikini top")
                            call Statup("Laura", "Love", 200, 20)
                            call Statup("Laura", "Obed", 200, 10)
                            call Statup("Laura", "Inbt", 200, 10)
                            ch_l "\"X\", cute. . ."
                        elif ApprovalCheck("Laura", 800):
                            call LauraFace("confused",1)
                            $ P_Inventory.remove("l bikini top")
                            $ L_Inventory.append("bikini top")
                            call Statup("Laura", "Love", 200, 20)
                            call Statup("Laura", "Obed", 200, 15)
                            call Statup("Laura", "Inbt", 200, 5)
                            ch_l "Ok, cool. . ."                  
                            call LauraFace("bemused",1)
                        elif ApprovalCheck("Laura", 600):
                            call LauraFace("confused",2)
                            $ P_Inventory.remove("l bikini top")
                            $ L_Inventory.append("bikini top")
                            call Statup("Laura", "Love", 200, 5)
                            call Statup("Laura", "Obed", 200, 10)
                            call Statup("Laura", "Inbt", 200, 5)
                            ch_l "I could use one of these. . ."                  
                            call LauraFace("bemused",1)
                        elif "no gift bra" in L_DailyActions:
                            call LauraFace("angry",2)
                            ch_l "My answer's still no, stop asking!"                      
                        else:
                            call LauraFace("angry",2)
                            call Statup("Laura", "Love", 50, -5)
                            call Statup("Laura", "Obed", 20, 5)
                            call Statup("Laura", "Inbt", 20, 5)
                            if "no gift panties" in L_DailyActions:                    
                                ch_l "I don't want this either!"                       
                            else:
                                ch_l "Don't worry about what I wear."    
                            $ L_Blush = 1
                            "She hands it back to you."
                            $ L_RecentActions.append("no gift bra")                      
                            $ L_DailyActions.append("no gift bra") 
                    else: 
                        ch_l "I already have one of those."     
                        
                "Give her the bikini bottoms." if "l bikini bottoms" in P_Inventory: 
                    #If you have a bra, you'll give it.
                    if "bikini bottoms" not in L_Inventory:                            
                        "You give Laura the bikini bottoms."
                        $ L_Blush = 1
                        if ApprovalCheck("Laura", 1000):                    
                            call LauraFace("bemused")
                            $ P_Inventory.remove("l bikini bottoms")
                            $ L_Inventory.append("bikini bottoms")
                            call Statup("Laura", "Love", 200, 20)
                            call Statup("Laura", "Obed", 200, 10)
                            call Statup("Laura", "Inbt", 200, 10)
                            ch_l "Huh, nice cut. . ."
                        elif ApprovalCheck("Laura", 800):
                            call LauraFace("confused",1)
                            $ P_Inventory.remove("l bikini bottoms")
                            $ L_Inventory.append("bikini bottoms")
                            call Statup("Laura", "Love", 200, 20)
                            call Statup("Laura", "Obed", 200, 15)
                            call Statup("Laura", "Inbt", 200, 5)
                            ch_l "Ok, cool. . ."                  
                            call LauraFace("bemused",1)
                        elif ApprovalCheck("Laura", 600):
                            call LauraFace("confused",2)
                            $ P_Inventory.remove("l bikini bottoms")
                            $ L_Inventory.append("bikini bottoms")
                            call Statup("Laura", "Love", 200, 5)
                            call Statup("Laura", "Obed", 200, 10)
                            call Statup("Laura", "Inbt", 200, 5)
                            ch_l "Weird gift, but is it warm out. . ."                  
                            call LauraFace("bemused",1)
                        elif "no gift panties" in L_DailyActions:
                            call LauraFace("angry",2)
                            ch_l "My answer's still no, stop asking!"                      
                        else:
                            call LauraFace("angry",2)
                            call Statup("Laura", "Love", 50, -5)
                            call Statup("Laura", "Obed", 20, 5)
                            call Statup("Laura", "Inbt", 20, 5)
                            if "no gift bra" in L_DailyActions:                    
                                ch_l "I don't want these either!"                       
                            else:
                                ch_l "Don't worry about what I wear."    
                            $ L_Blush = 1
                            "She hands them back to you."
                            $ L_RecentActions.append("no gift panties")                      
                            $ L_DailyActions.append("no gift panties") 
                    else: 
                        ch_l "I already have one of those."      
                        
                "Never mind":
                    pass
        "Exit":
            pass
    
    return


# start Laura_Names//////////////////////////////////////////////////////////
label Laura_Names:    
    menu:
        ch_l "Oh? What would you like me to call you?"
        "My initial's fine.":            
            $ L_Petname = Playername[:1]  #fix test this
            ch_l "You got it, [L_Petname]."
        "Call me by my name.":
            $ L_Petname = Playername            
            ch_l "If you'd rather, [L_Petname]."
        "Call me \"boyfriend\"." if "boyfriend" in L_Petnames:
            $ L_Petname = "boyfriend"
            ch_l "Sure thing, [L_Petname]."
        "Call me \"lover\"." if "lover" in L_Petnames:
            $ L_Petname = "lover"
            ch_l "Oooh, love to, [L_Petname]."
        "Call me \"sir\"." if "sir" in L_Petnames:
            $ L_Petname = "sir"
            ch_l "Yes, [L_Petname]."
        "Call me \"master\"." if "master" in L_Petnames:
            $ L_Petname = "master"
            ch_l "As you wish, [L_Petname]."
        "Call me \"sex friend\"." if "sex friend" in L_Petnames:
            $ L_Petname = "sex friend"
            ch_l "Heh, very cheeky, [L_Petname]."
        "Call me \"fuck buddy\"." if "fuck buddy" in L_Petnames:
            $ L_Petname = "fuck buddy"
            ch_l "I'm game if you are, [L_Petname]."        
        "Call me \"daddy\"." if "daddy" in L_Petnames:
            $ L_Petname = "daddy"
            ch_l "Oh! You bet, [L_Petname]."        
        "Bub works.":
            $ L_Petname = "bub"
            ch_l "You got it, bub."
        "Nevermind.":
            return
    return
# end Laura_Names//////////////////////////////////////////////////////////

label Laura_Pet:
    while 1:
        menu:
            extend ""
            "Polite":
                menu:
                    extend ""
                    "I think I'll just call you Laura.":
                        $ L_Pet = "Laura"            
                        ch_l "I don't see why not, [L_Petname]."
                        
                    "I think I'll just call you X-23.":
                        $ L_Pet = "X-23"            
                        if ApprovalCheck("Laura", 700, "L") and not ApprovalCheck("Laura", 500, "O"):
                                ch_l "Oh, if you say so, [L_Petname]."
                        else:
                                ch_l "I don't see why not, [L_Petname]."
                        
                    "I think I'll call you \"girl\".":
                        $ L_Pet = "girl"
                        if "boyfriend" in L_Petnames or ApprovalCheck("Laura", 600, "L"):
                            call LauraFace("sexy", 1) 
                            ch_l "I'm totally your girl, [L_Petname]."
                        else:      
                            call LauraFace("angry")           
                            ch_l "I'm NOT your girl, [L_Petname]." 
                            
                    "I think I'll call you \"boo\".":
                        $ L_Pet = "boo"
                        if "boyfriend" in L_Petnames or ApprovalCheck("Laura", 700, "L"):
                            call LauraFace("sexy", 1) 
                            ch_l "I am your boo, [L_Petname]."
                        else:     
                            call LauraFace("angry")            
                            ch_l "I'm NOT your boo,  [L_Petname]."
                            
                    "I think I'll call you \"bae\".":
                        $ L_Pet = "bae"
                        if "boyfriend" in L_Petnames or ApprovalCheck("Laura", 600, "L"):
                            call LauraFace("sexy", 1) 
                            ch_l "I am your bae, [L_Petname]."
                        else:     
                            call LauraFace("angry")            
                            ch_l "I'm NOT your bae,  [L_Petname]."
                            
                    "I think I'll call you \"baby\".":
                        $ L_Pet = "baby"
                        if "boyfriend" in L_Petnames or ApprovalCheck("Laura", 500, "L"):
                            call LauraFace("sexy", 1) 
                            ch_l "Cute, [L_Petname]."
                        else:     
                            call LauraFace("angry")            
                            ch_l "I am not a baby." 
                            
                            
                    "I think I'll call you \"sweetie\".":
                        $ L_Pet = "sweetie"
                        if "boyfriend" in L_Petnames or ApprovalCheck("Laura", 600, "L"):
                            ch_l "Aw, that's sweet, [L_Petname]."
                        else:     
                            call LauraFace("angry", 1)            
                            ch_l "Too sweet, [L_Petname]."
                            
                    "I think I'll call you \"sexy\".":
                        $ L_Pet = "sexy"
                        if "lover" in L_Petnames or ApprovalCheck("Laura", 800):
                            call LauraFace("sexy", 1) 
                            ch_l "You know it, [L_Petname]."
                        else:        
                            call LauraFace("angry", 1)         
                            ch_l "Pushing a line there, [L_Petname]."  
                            
                    "I think I'll call you \"lover\".":
                        $ L_Pet = "lover"
                        if "lover" in L_Petnames or ApprovalCheck("Laura", 1200):
                            call LauraFace("sexy", 1) 
                            ch_l "I know."
                        else:      
                            call LauraFace("angry", 1)           
                            ch_l "I don't think so, [L_Petname]."  
                    
                    "I think I'll call you \"Wolvie\".":
                        $ L_Pet = "Wolvie"
                        if ApprovalCheck("Laura", 500, "I"):
                            call LauraFace("sexy", 1) 
                            ch_l "Heh, ok, [L_Petname]."
                        else:     
                            call LauraFace("angry")            
                            ch_l "Not really that cute, [L_Petname]" 
                        
                    "Back":
                        pass
            
            "Risky":
                menu:                        
                    "I think I'll call you \"slave\".":
                        $ L_Pet = "slave"
                        if "master" in L_Petnames or ApprovalCheck("Laura", 800, "O"):
                            call LauraFace("bemused", 1) 
                            ch_l "As you wish, [L_Petname]."
                        else:      
                            call LauraFace("angry", 1)           
                            ch_l "I am not your slave, [L_Petname]."
                                            
                    "I think I'll call you \"pet\".":
                        $ L_Pet = "pet"
                        if "master" in L_Petnames or ApprovalCheck("Laura", 650, "O"):
                            call LauraFace("bemused", 1) 
                            ch_l "You can pet me if you want, [L_Petname]."
                        else:             
                            call LauraFace("angry", 1)    
                            ch_l "I am no one's pet, [L_Petname]."
                            
                    "I think I'll call you \"slut\".":
                        $ L_Pet = "slut"
                        if "sex friend" in L_Petnames or ApprovalCheck("Laura", 900, "OI"):
                            call LauraFace("sexy") 
                            ch_l "Fair enough."
                        else:                
                            call LauraFace("angry", 1) 
                            $ L_Mouth = "surprised"
                            ch_l "I'm like to see you try it with a busted jaw." 
                            
                    "I think I'll call you \"whore\".":
                        $ L_Pet = "whore"
                        if "fuckbuddy" in L_Petnames or ApprovalCheck("Laura", 1000, "OI"):
                            call LauraFace("sly") 
                            ch_l "I mean. . ."
                        else:        
                            call LauraFace("angry", 1)         
                            ch_l "If either of us is going to be turning tricks. . ." 
                                                   
                    "I think I'll call you \"sugartits\".":
                        $ L_Pet = "sugartits"
                        if "sex friend" in L_Petnames or ApprovalCheck("Laura", 1400):
                            call LauraFace("sly", 1) 
                            ch_l "That doesn't even make sense."
                        else:     
                            call LauraFace("angry", 1)            
                            ch_l "Not cool." 
                            
                    "I think I'll call you \"sex friend\".":
                        $ L_Pet = "sex friend"
                        if "sex friend" in L_Petnames or ApprovalCheck("Laura", 600, "I"):
                            call LauraFace("sly") 
                            ch_l "Yeah. . ."
                        else:                
                            call LauraFace("angry", 1) 
                            ch_l "Keep it down, [L_Petname]." 
                            
                    "I think I'll call you \"fuckbuddy\".":
                        $ L_Pet = "fuckbuddy"
                        if "fuckbuddy" in L_Petnames or ApprovalCheck("Laura", 700, "I"):
                            call LauraFace("sly") 
                            ch_l "Yup."
                        else:                
                            call LauraFace("angry", 1)
                            $ L_Mouth = "surprised"
                            ch_l "Don't even joke, [L_Petname]." 
                        
                    "I think I'll call you \"baby girl\".":
                        $ L_Pet = "baby girl"
                        if "daddy" in L_Petnames or ApprovalCheck("Laura", 1200):
                            call LauraFace("smile", 1) 
                            ch_l "I guess?"
                        else:                
                            call LauraFace("angry", 1) 
                            ch_l "Weirdo." 
                            
                    "Back":
                        pass
                    
            "Nevermind.":
                return
    return
    
label Laura_Namecheck(L_Pet = L_Pet, Cnt = 0, Ugh = 0):
    #L_Pet is the internal pet name, Cnt and Ugh are internal count variable
    if L_Pet == "Laura":
        return Ugh   
    if Taboo:
        $ Cnt = int(Taboo/10)
    if L_Pet == "girl":                                         #easy options
        if ApprovalCheck("Laura", 600, "L", TabM=1):            
            call Statup("Laura", "Love", 80, 1)
        else:
            call Statup("Laura", "Love", 50, -1)
            $ Ugh = 1
    elif L_Pet == "boo" or L_Pet == "bae":
        if ApprovalCheck("Laura", 600, "L", TabM=1):
            call Statup("Laura", "Love", 80, 1)
        else:
            call Statup("Laura", "Love", 50, -2)
            $ Ugh = 1
    elif L_Pet == "baby":    
        if ApprovalCheck("Laura", 500, "L", TabM=1):
            call Statup("Laura", "Love", 90, 1)
        else:
            call Statup("Laura", "Love", 30, -1)
            $ Ugh = 1
    elif L_Pet == "Wolvie":
        if ApprovalCheck("Laura", 500, "I", TabM=1):
            call Statup("Laura", "Love", 80, 1)
        else:
            call Statup("Laura", "Love", 50, -1)
            $ Ugh = 1
    elif L_Pet == "sweetie":
        if not ApprovalCheck("Laura", 600, "L", TabM=1):
            call Statup("Laura", "Love", 80, 1)  
        else:
            call Statup("Laura", "Love", 40, -1)
            $ Ugh = 1
            
    elif L_Pet == "sexy":
        if ApprovalCheck("Laura", 800, TabM=1):                                                        #over 150
            call Statup("Laura", "Love", 80, 2)
            call Statup("Laura", "Obed", 80, 1)
            call Statup("Laura", "Inbt", 70, 1) 
        else:                                                            
            call Statup("Laura", "Love", 50, (-1-Cnt))
            call Statup("Laura", "Obed", 50, 1)
            call Statup("Laura", "Inbt", 20, -1)
            $ Ugh = 1            
    elif L_Pet == "lover":
        if ApprovalCheck("Laura", 1200, TabM=1):                                                        #over 150
            call Statup("Laura", "Love", 80, 2)
            call Statup("Laura", "Obed", 80, 1)
            call Statup("Laura", "Inbt", 70, 1) 
        else:                                                            
            call Statup("Laura", "Love", 50, (-1-Cnt))
            call Statup("Laura", "Obed", 50, 1)
            call Statup("Laura", "Inbt", 20, -1)
            $ Ugh = 1
    #tougher options
    elif L_Pet == "X-23":   
        if ApprovalCheck("Laura", 800, "O"):
            call Statup("Laura", "Lust", 90, 3) 
            call Statup("Laura", "Love", 90, -1)  
            call Statup("Laura", "Obed", 95, 2)                                   
        elif ApprovalCheck("Laura", 700, "L") and not ApprovalCheck("Laura", 500, "O"):
            call Statup("Laura", "Love", 200, -2)
            call Statup("Laura", "Love", 50, -1, 1)
            call Statup("Laura", "Obed", 30, 2)
            call Statup("Laura", "Obed", 50, 2)
            call Statup("Laura", "Inbt", 50, -1)
            $ Ugh = 1
        else:
            call Statup("Laura", "Obed", 95, 1)
            
    elif L_Pet == "slave":                             
        if ApprovalCheck("Laura", 800, "O", TabM=3):                                            #over 80
            call Statup("Laura", "Lust", 90, (3+Cnt))
            call Statup("Laura", "Obed", 95, (2+Cnt))
            call Statup("Laura", "Inbt", 30, 1)  
        elif ApprovalCheck("Laura", 500, "O", TabM=3):                                                  #between 50 and 80
            call Statup("Laura", "Lust", 90, 1)
            call Statup("Laura", "Love", 200, -2)
            call Statup("Laura", "Obed", 81, 2)     
        else:                                                                                           # under 50
            call Statup("Laura", "Love", 200, -2)
            call Statup("Laura", "Love", 50, -1, 1)
            call Statup("Laura", "Obed", 50, 1)
            call Statup("Laura", "Inbt", 50, -1)
            $ Ugh = 1
    
    elif L_Pet == "pet":                                        #tougher options
        if ApprovalCheck("Laura", 800, "O", TabM=2):
            call Statup("Laura", "Lust", 90, (3+Cnt))
            call Statup("Laura", "Obed", 95, (2+Cnt))
            call Statup("Laura", "Inbt", 30, 1)
            call Statup("Laura", "Inbt", 70, 1)     
        elif ApprovalCheck("Laura", 650, "O", TabM=2):
            call Statup("Laura", "Lust", 60, 1)
            call Statup("Laura", "Obed", 81, 2)
            call Statup("Laura", "Inbt", 70, 1)        
        else:
            call Statup("Laura", "Love", 200, -2)
            call Statup("Laura", "Love", 50, -2, 1)
            call Statup("Laura", "Obed", 50, 2)
            call Statup("Laura", "Inbt", 50, -1)
            $ Ugh = 1
            
    elif L_Pet == "slut":
        if ApprovalCheck("Laura", 500, "O", TabM=2) or ApprovalCheck("Laura", 400, "I", TabM=2):        #over 50
            call Statup("Laura", "Lust", 90, (4+Cnt))
            call Statup("Laura", "Obed", 95, (2+Cnt))
            call Statup("Laura", "Inbt", 40, 2)
            call Statup("Laura", "Inbt", 80, 1)
        elif ApprovalCheck("Laura", 300, "O", TabM=2) or ApprovalCheck("Laura", 200, "I", TabM=2):      #between 30 and 50
            call Statup("Laura", "Lust", 90, 1)
            call Statup("Laura", "Love", 200, (-1-Cnt))
            call Statup("Laura", "Obed", 80, (2+Cnt))
            call Statup("Laura", "Inbt", 70, 1)        
        else:                                                                                           # under 40
            call Statup("Laura", "Love", 200, (-2-Cnt))
            call Statup("Laura", "Love", 50, (-1-Cnt), 1)
            call Statup("Laura", "Obed", 50, 1)
            call Statup("Laura", "Inbt", 20, -1)
            $ Ugh = 1
            
    elif L_Pet == "whore":
        if ApprovalCheck("Laura", 500, "O", TabM=2) or ApprovalCheck("Laura", 500, "I", TabM=2):        #over 60
            call Statup("Laura", "Lust", 90, 4)
            call Statup("Laura", "Obed", 95, 2)
            call Statup("Laura", "Inbt", 50, 2)
            call Statup("Laura", "Inbt", 80, 1)
        elif ApprovalCheck("Laura", 400, "O", TabM=2) or ApprovalCheck("Laura", 400, "I", TabM=2):      #between 40 and 60
            call Statup("Laura", "Lust", 90, 1)
            call Statup("Laura", "Love", 200, (-2-Cnt))
            call Statup("Laura", "Obed", 80, 2)
            call Statup("Laura", "Inbt", 70, 1)
        else:                                                                                           # under 40
            call Statup("Laura", "Love", 200, (-3-Cnt))
            call Statup("Laura", "Love", 50, (-2-Cnt), 1)
            call Statup("Laura", "Obed", 50, 1)            
            call Statup("Laura", "Inbt", 21, 1, 1)
            call Statup("Laura", "Inbt", 20, -1)
            $ Ugh = 1
            
    elif L_Pet == "sugartits":
        if ApprovalCheck("Laura", 1500, TabM=1):                                                        #over 150
            call Statup("Laura", "Obed", 80, 1)
            call Statup("Laura", "Obed", 50, 2)
            call Statup("Laura", "Inbt", 70, 1)            
            call Statup("Laura", "Inbt", 30, 2)
        else:                                                                       
            call Statup("Laura", "Love", 200, (-2-Cnt))
            call Statup("Laura", "Love", 50, (-1-Cnt))
            call Statup("Laura", "Obed", 50, 1)
            call Statup("Laura", "Inbt", 20, -1)
            $ Ugh = 1
            
    elif L_Pet == "sex friend":    
        if ApprovalCheck("Laura", 750, "O", TabM=1) or ApprovalCheck("Laura", 600, "I", TabM=1):        #over 75/60
            call Statup("Laura", "Lust", 90, 3)
            call Statup("Laura", "Obed", 95, 2)
            call Statup("Laura", "Inbt", 40, 2)
            call Statup("Laura", "Inbt", 80, 1)
        elif ApprovalCheck("Laura", 600, "O", TabM=1) or ApprovalCheck("Laura", 400, "I", TabM=1):      #between 60/40 and 75/60
            call Statup("Laura", "Lust", 90, 2)
            call Statup("Laura", "Love", 200, (-1-Cnt))
            call Statup("Laura", "Obed", 80, 1)
            call Statup("Laura", "Inbt", 70, 1)
            $ L_Blush = 1
        else:                                                                                           # under 60/40
            call Statup("Laura", "Love", 200, -Cnt)
            call Statup("Laura", "Love", 50, (-1-Cnt), 1)
            call Statup("Laura", "Obed", 50, 1)
            call Statup("Laura", "Inbt", 20, -1)
            $ Ugh = 1
            
    elif L_Pet == "fuckbuddy":
        if ApprovalCheck("Laura", 700, "O", TabM=2) or ApprovalCheck("Laura", 700, "I", TabM=1):        #over 70/70
            call Statup("Laura", "Lust", 90, 3)
            call Statup("Laura", "Obed", 95, 2)
            call Statup("Laura", "Inbt", 40, 2)
            call Statup("Laura", "Inbt", 85, 1)
        elif ApprovalCheck("Laura", 600, "O", TabM=2) or ApprovalCheck("Laura", 500, "I", TabM=1):      #between 60/50 and 70/70
            call Statup("Laura", "Lust", 90, 2)
            call Statup("Laura", "Love", 200, (-1-Cnt))
            call Statup("Laura", "Obed", 80, 1)
            call Statup("Laura", "Inbt", 70, 1)
            $ L_Blush = 1
        else:                                                                                           #under 60/50
            call Statup("Laura", "Love", 200, -Cnt)
            call Statup("Laura", "Love", 60, (-2-Cnt), 1)
            call Statup("Laura", "Obed", 60, 1)
            call Statup("Laura", "Inbt", 20, -1)
            $ Ugh = 1
            
    elif L_Pet == "baby girl":
        if ApprovalCheck("Laura", 1200, TabM=1):                                                        #over 150
            call Statup("Laura", "Obed", 80, 1)
            call Statup("Laura", "Obed", 50, 2)
            call Statup("Laura", "Inbt", 70, 1)            
            call Statup("Laura", "Inbt", 30, 2)
        else:                                                                       
            call Statup("Laura", "Love", 200, (-2-Cnt))
            call Statup("Laura", "Love", 50, (-1-Cnt))
            call Statup("Laura", "Obed", 50, 1)
            call Statup("Laura", "Inbt", 20, -1)
            $ Ugh = 1
            
    return Ugh


# start Laura_Personality//////////////////////////////////////////////////////////
label Laura_Personality(Cnt = 0):   
    if not L_Chat[4] or Cnt:
        "Since you're doing well in one area, you can convince Laura to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_l "Yeah? What's up?"
        "More Obedient. [[Love to Obedience]" if L_Love > 900:
            ch_p "If you really love me, could you please just do what I say?"
            ch_l "If you really care about that, sure."
            $ L_Chat[4] = 1
        "Less Inhibited. [[Love to Inhibition]" if L_Love > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_l "I could always be a bit more wild if that's what you want."
            $ L_Chat[4] = 2
        
        "Less Inhibited. [[Obedience to Inhibition]" if L_Obed > 900:
            ch_p "I want you to be less inhibited."
            ch_l "I guess I could go all-out."
            $ L_Chat[4] = 3
        "More Loving. [[Obedience to Love]" if L_Obed > 900:
            ch_p "I'd like you to learn to love me."
            ch_l "I can try."
            $ L_Chat[4] = 4
            
        "More Obedient. [[Inhibition to Obedience]" if L_Inbt > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_l "I can give it a shot. . ."
            $ L_Chat[4] = 5
            
        "More Loving. [[Inhibition to Love]" if L_Inbt > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_l "If that's somethign you need out of this. . ."
            $ L_Chat[4] = 6
            
        "I guess just do what you like. . .[[reset]" if L_Chat[4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_l "Um, ok."
            $ L_Chat[4] = 0
        "Repeat the rules":
            $ Cnt = 1
            jump Laura_Personality
        "Nevermind.":
            return
    return
# end Laura_Personality//////////////////////////////////////////////////////////




# Laura_Summon//////////////////////////////////////////////////////////

label Laura_Summon(Tempmod=Tempmod):
    call LauraOutfit  
    if "no summon" in L_RecentActions:
                if "angry" in L_RecentActions:
                    ch_l "Grrrrrrrrr."
                elif Action_Check("Laura", "recent", "no summon") > 1:
                    ch_l "Back off!"
                    $ L_RecentActions.append("angry") 
#                elif Current_Time == "Night": 
#                    ch_l "Like I said, it's too late for that."
                else:
                    ch_l "Like I said, I'm busy."   
                $ L_RecentActions.append("no summon")
                return
                              
    if Current_Time == "Night": 
                if ApprovalCheck("Laura", 500, "L") or ApprovalCheck("Laura", 400, "O"):                              #It's night time but she likes you.
                        ch_l "You're up too? Sure, we can hang."
                        $ L_Loc = bg_current 
                        call Set_The_Scene
                else:                                                           #It's night time and she isn't into you
                        ch_l "Nah."       
                        $ L_RecentActions.append("no summon")         
                return
                
    $ D20 = renpy.random.randint(1, 20) 
    $ Line = 0
    if L_Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = 10
    elif L_Loc == "bg dangerroom":    
        $ Tempmod = 10
    elif L_Loc == "bg showerroom":    
        $ Tempmod = 30
        
    if D20 <= 3:                                                                        
        #unlucky refusal
        $ Line = "no"       
    elif not ApprovalCheck("Laura", 700, "L") or not ApprovalCheck("Laura", 600, "O"):                       
        #It's not night time, but she's busy 
        if not ApprovalCheck("Laura", 300):
                ch_l "I'm busy, [L_Petname]."       
                $ L_RecentActions.append("no summon")         
                return    
            
            
        if "summoned" in L_RecentActions:
                pass
        elif "goto" in L_RecentActions:
                ch_l "You were just over here."
        elif L_Loc == "bg classroom":
                ch_l "I'm in class, did you want to come too?"
        elif L_Loc == "bg dangerroom": 
                ch_l "I'm in the Danger Room, [L_Petname], want in?"    
        elif L_Loc == "bg campus": 
                ch_l "I'm napping under a tree here, want to come?" 
        elif L_Loc == "bg laura": 
                ch_l "I'm in my room, [L_Petname], want to hang?" 
        elif L_Loc == "bg player": 
                ch_l "I'm in your room, [L_Petname], why aren't you?"   
        elif L_Loc == "bg showerroom":    
            if ApprovalCheck("Laura", 1600):
                ch_l "I'm in the shower right now. Join me?"
            else:            
                ch_l "I'm in the shower right now, [L_Petname]. We can connect later."       
                $ L_RecentActions.append("no summon")         
                return      
        elif L_Loc == "hold":
                ch_l "I'm on task right now. Sorry?"       
                $ L_RecentActions.append("no summon") 
                return      
        else:        
                ch_l "Why don't you come to me?"    
           
           
        if "summoned" in L_RecentActions:
            ch_l "Again? Ok, fine."           
            $ Line = "yes"            
        elif "goto" in L_RecentActions:
            menu:
                extend ""
                "You're right, be right back.":
                                ch_l "See you when you get here."
                                $ Line = "go to"                    
                "Nah, it's better here.":    
                                ch_l "If you say so."                    
                "But I'd {i}really{/i} like to see you over here.":
                        if ApprovalCheck("Laura", 600, "L") or ApprovalCheck("Laura", 1400):
                                $ Line = "lonely"
                        else: 
                                $ Line = "no"                        
                "I said come over here.":
                        if ApprovalCheck("Laura", 600, "O"):                                    
                                #she is obedient
                                $ Line = "command"                        
                        elif D20 >= 7 and ApprovalCheck("Laura", 1400):                         
                                #she is generally favorable 
                                ch_l "Hmph."              
                                $ Line = "yes"                        
                        elif ApprovalCheck("Laura", 200, "O"):                                  
                                #she is not obedient  
                                ch_l "Whatever."    
                                ch_l "I'll be here if you change your mind."    
                        else:                                                                   
                                #she is obedient, but you failed to meet the checks                     
                                $ Line = "no" 
        else:  
            menu:
                extend ""
                "Sure, I'll be right there.":
                    call Statup("Laura", "Love", 55, 1) 
                    call Statup("Laura", "Inbt", 30, 1)
                    ch_l "See you when you get here."
                    $ Line = "go to"
                    
                "Nah, we can talk later.":
                    call Statup("Laura", "Obed", 50, 1)                            
                    call Statup("Laura", "Obed", 30, 2)
                    ch_l "Ok. Later then."
                    
                "Could you please come visit me? I'm lonely.":
                    if ApprovalCheck("Laura", 650, "L") or ApprovalCheck("Laura", 1500):
                        call Statup("Laura", "Love", 70, 1)                   
                        call Statup("Laura", "Obed", 50, 1)
                        $ Line = "lonely"
                    else: 
                        call Statup("Laura", "Inbt", 30, 1)
                        $ Line = "no"
                        ch_l "Man, you are such a sap."
                        
                "Come on, it'll be fun.":
                    if ApprovalCheck("Laura", 400, "L") and ApprovalCheck("Laura", 800):
                        call Statup("Laura", "Love", 70, 1)                   
                        call Statup("Laura", "Obed", 50, 1)
                        $ Line = "fun"
                    else: 
                        call Statup("Laura", "Inbt", 30, 1)
                        $ Line = "no"
                        
                "I said come over here.":
                    if ApprovalCheck("Laura", 600, "O"):                              
                        #she is obedient
                        call Statup("Laura", "Love", 50, 1, 1)    
                        call Statup("Laura", "Love", 40, -1)                
                        call Statup("Laura", "Obed", 90, 1)    
                        $ Line = "command"
                        
                    elif D20 >= 7 and ApprovalCheck("Laura", 1500):       
                        #she is generally favorable
                        call Statup("Laura", "Love", 70, -2)  
                        call Statup("Laura", "Love", 90, -1)  
                        call Statup("Laura", "Obed", 50, 2)                                
                        call Statup("Laura", "Obed", 90, 1)  
                        ch_l "Ok, fine."              
                        $ Line = "yes"
                        
                    elif ApprovalCheck("Laura", 200, "O"):                                         
                        #she is not obedient   
                        call Statup("Laura", "Love", 60, -4)  
                        call Statup("Laura", "Love", 90, -3)   
                        ch_l "Don't even try it."                             
                        call Statup("Laura", "Inbt", 40, 2)
                        call Statup("Laura", "Inbt", 60, 1)    
                        call Statup("Laura", "Obed", 70, -3)
                        ch_l "I'm staying put."                    
                    else:                                                                   
                        #she is obedient, but you failed to meet the checks
                        call Statup("Laura", "Inbt", 30, 1)
                        call Statup("Laura", "Inbt", 50, 1)                                    
                        call Statup("Laura", "Love", 50, -1, 1)
                        call Statup("Laura", "Obed", 70, -1)  
                        $ Line = "no" 
                    #end "ordered"
    else:                                                                               
        #automatic acceptance
        if L_Love > L_Obed:
            ch_l "Sure!"
        else:
            ch_l "Ok, I'm in route."
        $ Line = "yes" 
        
    if not Line:                                                                        
            #You end the dialog neutrally               
            $ L_RecentActions.append("no summon")         
            return
        
    if Line == "no":                                                                    
            # She's refused, context based dialog
            if L_Loc == "bg classroom":
                ch_l "I can't skip this lecture." 
            elif L_Loc == "bg dangerroom": 
                ch_l "I'm just getting warmed up though!"
            else:
                ch_l "Sorry, [L_Petname], I'm kinda busy."          
            $ L_RecentActions.append("no summon")         
            return
        
    elif Line == "go to":                                                                 
            #You agreed to go to her instead        
            $ renpy.pop_call()
            $ L_RecentActions.append("goto")  
            $ P_RecentActions.append("goto")  
            if L_Loc == "bg classroom":
                    ch_l "K, there's room next to me."
                    jump Class_Room 
            elif L_Loc == "bg dangerroom": 
                    ch_l "I'll try to leave some bots for 'ya."
                    jump Danger_Room
            elif L_Loc == "bg laura":    
                    ch_l "I'll. . . make some space."
                    jump Laura_Room
            elif L_Loc == "bg player": 
                    ch_l "I'll be waiting."
                    jump Player_Room                
            elif L_Loc == "bg showerroom": 
                    ch_l "I'll leave you some hot water."
                    jump Shower_Room
            elif L_Loc == "bg campus": 
                    ch_l "Look for the biggest tree."
                    jump Campus
            else:
                    ch_l "Um, I'll just meet you in my room."
                    $ L_Loc = "bg laura"
                    jump Laura_Room
            
    #She's agreed to come over    
    elif Line == "lonely":
            ch_l "You are such a dork!"
    elif Line == "command": 
            ch_l "Yes, [L_Petname]."
        
    $ L_RecentActions.append("summoned")  
    $ Line = 0
    ch_l "I'll be right there."      
    if "locked" in P_RecentActions:
            call Locked_Door("Laura")
            return                          
    $ L_Loc = bg_current 
    call LauraOutfit
    call Set_The_Scene
    return

# End Laura Summon ///////////////////    


label Laura_Leave(Tempmod=Tempmod, GirlsNum = 0):        
    if "leaving" in L_RecentActions:
        call DrainWord("Laura","leaving")
    else:
        return
    
    if L_Loc == "hold":   
            # Activates if she's being moved out of play
            ch_l "I'm taking off for a bit, later." 
            return
            
    if "Laura" in Party or "lockedtravels" in L_Traits:           
            #If she's in your party or if you've told her not to leave you
            #It resets her to your location
            $ L_Loc = bg_current 
            return
      
    elif "freetravels" in L_Traits or not ApprovalCheck("Laura", 700):
            #If you've told her to go wherever, or she just doesn't care what you think.   
            call LauraOutfit           
            if GirlsNum: #if someone left before her
                        ch_l "Yeah, I'm leaving too."
                        
            if L_Loc == "bg classroom":
                        ch_l "I've got class."
            elif L_Loc == "bg dangerroom": 
                        ch_l "I'm hitting the Danger Room."   
            elif L_Loc == "bg campus": 
                        ch_l "I'm taking a nap in the quad." 
            elif L_Loc == "bg laura": 
                        ch_l "I'm headed back to my room." 
            elif L_Loc == "bg player": 
                        ch_l "I'm gonna hang out in your room for a bit."   
            elif L_Loc == "bg showerroom":    
                if ApprovalCheck("Laura", 1400):
                        ch_l "I'm hitting the showers, later."
                else:            
                        ch_l "I'm headed out."
            else:        
                        ch_l "I'm headed out, later."                  
            hide Laura_Sprite
            return     
            #End Free Travels
    
    if bg_current == "bg dangerroom":   
            call Gym_Clothes("exit")
            
    call LauraOutfit  
    
    if "follow" not in L_Traits:
            # Sets a key to show that she's asked you to follow her at least once
            $ L_Traits.append("follow")   
        
    $ D20 = renpy.random.randint(1, 20) 
    $ Line = 0
    # Sets her preferences
    if L_Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = 10
    elif L_Loc == "bg dangerroom":    
        $ Tempmod = 20
    elif L_Loc == "bg showerroom":    
        $ Tempmod = 40
    
    
    if GirlsNum: #if someone left before her
                ch_l "Yeah, I'm headed out too."
                
    if L_Loc == "bg classroom":
        ch_l "I've got class, want in?"
    elif L_Loc == "bg dangerroom": 
        ch_l "I've got some Danger Room time, want in?"    
    elif L_Loc == "bg campus": 
        ch_l "I'm taking a nap on the quad, you want in?" 
    elif L_Loc == "bg laura": 
        ch_l "I'm headed back to my room, you want in?" 
    elif L_Loc == "bg player": 
        ch_l "I'm going to hang out in your room for a bit, you coming?"   
    elif L_Loc == "bg showerroom":    
        if ApprovalCheck("Laura", 1600):
            ch_l "I'm hitting the showers, you could use one too."
        else:            
            ch_l "I'm hitting the showers, see you later."
            return        
    else:        
        ch_l "Wanna join me?"    
    
    
    menu:
        extend ""
        "Sure, I'll catch up.":
                if "followed" not in L_RecentActions:
                    call Statup("Laura", "Love", 55, 1) 
                    call Statup("Laura", "Inbt", 30, 1)
                $ Line = "go to"
            
        "Nah, we can talk later.":
                if "followed" not in L_RecentActions:
                    call Statup("Laura", "Obed", 50, 1)                            
                    call Statup("Laura", "Obed", 30, 2)
                ch_l "Sure, whatever."
            
        "Could you please stay with me? I'll get lonely.":
                if ApprovalCheck("Laura", 650, "L") or ApprovalCheck("Laura", 1500):                
                    if "followed" not in L_RecentActions:
                        call Statup("Laura", "Love", 70, 1)                   
                        call Statup("Laura", "Obed", 50, 1)
                    $ Line = "lonely"
                else: 
                    if "followed" not in L_RecentActions:
                        call Statup("Laura", "Inbt", 30, 1)
                    $ Line = "no"
                    ch_l "Man, you are such a sap."
                
        "Come on, it'll be fun.":
                if ApprovalCheck("Laura", 400, "L") and ApprovalCheck("Laura", 800):
                    call Statup("Laura", "Love", 70, 1)                   
                    call Statup("Laura", "Obed", 50, 1)
                    $ Line = "fun"
                else: 
                    call Statup("Laura", "Inbt", 30, 1)
                    $ Line = "no"
                        
        "No, stay here.":
                if ApprovalCheck("Laura", 600, "O"):                              
                    #she is obedient
                    if "followed" not in L_RecentActions: 
                        call Statup("Laura", "Love", 40, -2)                
                        call Statup("Laura", "Obed", 90, 1)    
                    $ Line = "command"
                    
                elif D20 >= 7 and ApprovalCheck("Laura", 1400):       
                    #she is generally favorable
                    if "followed" not in L_RecentActions:
                        call Statup("Laura", "Love", 70, -2)  
                        call Statup("Laura", "Love", 90, -1)  
                        call Statup("Laura", "Obed", 50, 2)                                
                        call Statup("Laura", "Obed", 90, 1)  
                    ch_l "I guess if you need me here."              
                    $ Line = "yes"
                    
                elif ApprovalCheck("Laura", 200, "O"):                                         
                    #she is not obedient                   
                    if "followed" not in L_RecentActions:
                        call Statup("Laura", "Love", 70, -4)  
                        call Statup("Laura", "Love", 90, -2)   
                    ch_l "Don't tell me what to do."  
                    if "followed" not in L_RecentActions:                       
                        call Statup("Laura", "Inbt", 40, 2)
                        call Statup("Laura", "Inbt", 60, 1)    
                        call Statup("Laura", "Obed", 70, -2)
                    ch_l "I'm out of here."                    
                else:                                                                  
                    #she is obedient, but you failed to meet the checks                  
                    if "followed" not in L_RecentActions:
                        call Statup("Laura", "Inbt", 30, 1)
                        call Statup("Laura", "Inbt", 50, 1)                                    
                        call Statup("Laura", "Love", 50, -1, 1)                               
                        call Statup("Laura", "Love", 90, -2)
                        call Statup("Laura", "Obed", 70, -1)  
                    $ Line = "no" 
                #End ordered to stay
                    
    $ L_RecentActions.append("followed")     
    if not Line:                                                                        
            #You end the dialog neutrally      
            hide Laura_Sprite
            call Gym_Clothes("auto", "Laura")
            return
    
    if Line == "no":                                                                    
            # She's refused, context based dialog
            if L_Loc == "bg classroom":
                ch_l "I really can't miss this one." 
            elif L_Loc == "bg dangerroom": 
                ch_l "Sorry [L_Petname], but I'm going a little stir crazy."
            else:
                ch_l "Sorry, I have stuff to do."         
            hide Laura_Sprite
            call Gym_Clothes("auto", "Laura")         
            return
        
    elif Line == "go to":                                                                 
            #You agreed to go to her instead  
            $ Tempmod = 0
            call DrainWord("All","leaving")  
            call DrainWord("All","arriving")        
            hide Laura_Sprite
            call Gym_Clothes("auto", "Laura")
            if L_Loc == "bg classroom":
                ch_l "Ok, get a move on then."            
                jump Class_Room_Entry
            elif L_Loc == "bg dangerroom": 
                ch_l "I'll get warmed up."
                jump Danger_Room_Entry
            elif L_Loc == "bg laura": 
                ch_l "Ok."
                jump Laura_Room
            elif L_Loc == "bg player": 
                ch_l "Good."
                jump Player_Room                
            elif L_Loc == "bg showerroom": 
                ch_l "Ok, nice."
                jump Shower_Room_Entry
            elif L_Loc == "bg campus": 
                ch_l "Ok, nice."
                jump Campus_Entry
            else:            
                ch_l "I'll just meet you in your room."
                $ L_Loc = "bg player"
                jump Player_Room
            #End "goto" where she's at
            
    #She's agreed to come over    
    elif Line == "lonely":
            ch_l "Well, I guess you should never go alone. . ."
    elif Line == "command": 
            ch_l "Yes [L_Petname]."
    
    $ Line = 0
    ch_l "I'll stick around."                                
    $ L_Loc = bg_current 
    return

# End Laura Leave ///////////////////   

label Laura_Dismissed(Leaving = 0):
    if "Laura" in Party:        
            $ Party.remove("Laura")
    call Laura_Schedule(0) #if L_Loc == bg_current then it means she wants to stay here
    if "leaving" in L_RecentActions:
            call DrainWord("Laura","leaving")   
    menu:
        "You can leave if you like.":
                if L_Loc == bg_current and not ApprovalCheck("Laura", 600, "O"):
                        ch_l "Ok. [[she does not seem to be moving. . .]"
                else:
                        ch_l "Ok."
                        $ Leaving = 1                   
        "Could you give me the room please?":                            
                if L_Loc == bg_current and not ApprovalCheck("Laura", 800, "LO"):
                        ch_l "Nobody's kicking you out [[She doesn't move]."
                elif not ApprovalCheck("Laura", 500, "LO"):
                        ch_l "Nope."               
                else:
                        if "dismissed" not in L_DailyActions:
                                call Statup("Laura", "Obed", 30, 7)
                                call Statup("Laura", "Obed", 50, 5)
                        ch_l "Sure, ok." 
                        $ Leaving = 1                              
        "You can go now.":                         
                if L_Loc == bg_current and not ApprovalCheck("Laura", 450, "O"):
                        ch_l "But I won't."
                elif not ApprovalCheck("Laura", 250, "O"):
                        call LauraFace("confused") 
                        ch_l "Why?"
                else:
                        if "dismissed" not in L_DailyActions:
                                call Statup("Laura", "Obed", 40, 10)
                                call Statup("Laura", "Obed", 60, 7)
                        ch_l "Ok."
                        $ Leaving = 1                               
        "Nevermind.":
                        return                                           
    
    if not Leaving and bg_current in ("bg campus","bg classroom","bg dangerroom"):
            #if there is space nearby. . .
            call Remove_Girl("Laura",1,1)            
    elif not Leaving:     
            menu:
                extend ""
                "I insist, get going.":  
                        if L_Loc != bg_current and (ApprovalCheck("Laura", 1200, "LO") or ApprovalCheck("Laura", 400, "O")):
                                #If she has someplace to be and is obedient
                                if "dismissed" not in L_DailyActions:
                                        call Statup("Laura", "Love", 70, -5, 1)
                                        call Statup("Laura", "Obed", 60, 10)
                                        call Statup("Laura", "Obed", 80, 5)
                                ch_l "Ok, fine."  
                                $ Leaving = 1                                  
                        elif L_Loc != bg_current and (ApprovalCheck("Laura", 1000, "LO") or ApprovalCheck("Laura", 250, "O")):
                                #If she has someplace to be and is less obedient
                                if "dismissed" not in L_DailyActions:
                                        call Statup("Laura", "Love", 50, -5, 1)
                                        call Statup("Laura", "Love", 70, -5, 1)
                                        call Statup("Laura", "Obed", 60, 10)
                                        call Statup("Laura", "Obed", 80, 5)
                                call LauraFace("angry") 
                                ch_l "I've got stuff to do anyway."      
                                $ Leaving = 1                         
                        elif L_Loc != bg_current:
                                #If she has someplace to be but is not obedient
                                if "dismissed" not in L_DailyActions:
                                        call Statup("Laura", "Love", 50, -5, 1)
                                        call Statup("Laura", "Love", 70, -10, 1)
                                        call Statup("Laura", "Obed", 50, -3)
                                        call Statup("Laura", "Inbt", 50, 5)
                                        call Statup("Laura", "Inbt", 80, 3)
                                call LauraFace("angry") 
                                ch_l "Not until I see what you have planned here."          
                        elif ApprovalCheck("Laura", 1400, "LO") or ApprovalCheck("Laura", 400, "O"):
                                #If she has nowhere to be to be but is obedient
                                if "dismissed" not in L_DailyActions:
                                        call Statup("Laura", "Love", 50, -5, 1)
                                        call Statup("Laura", "Obed", 50, 10)
                                        call Statup("Laura", "Obed", 80, 5)
                                call LauraFace("sad") 
                                ch_l "Ok."
                                $ Leaving = 1                   
                        else:
                                #If she has nowhere to be to be and is not obedient
                                if "dismissed" not in L_DailyActions:
                                        call Statup("Laura", "Love", 50, -5, 1)
                                        call Statup("Laura", "Love", 70, -10, 1)
                                        call Statup("Laura", "Obed", 50, -5)
                                        call Statup("Laura", "Inbt", 50, 3)
                                        call Statup("Laura", "Inbt", 80, 2)
                                call LauraFace("sad") 
                                ch_l "Nope."          
                "Ok, nevermind.":    
                                pass
                    
    if "dismissed" not in L_DailyActions:
            $ L_DailyActions.append("dismissed")        
    if "Laura" in Nearby:
        "You shift a bit away from Laura"
    elif Leaving == 0:
            # Stay
            $ L_Loc = bg_current
    else:
            # Go
            if L_Loc != bg_current: #it stays the same
                pass
            elif bg_current == "bg laura":
                $ L_Loc = "bg campus"
            else:
                $ L_Loc = "bg laura"
            hide Laura_Sprite
            "Laura heads out." 
    return
    #end "you can leave"
    

label Laura_AboutRogue:
    ch_l "What do I think about her? Well. . ."
    
    if "poly Rogue" in L_Traits:  
        ch_l "Yeah, we hook up, so. . ."    
    elif L_LikeRogue >= 900:
        ch_l "She's got a great ass. . ."
    elif L_LikeRogue >= 800:
        ch_l "She's got a nice shape on her. . ."    
    elif L_LikeRogue >= 700:
        ch_l "She's good in a fight."
    elif L_LikeRogue >= 600:
        ch_l "We get along ok."
    elif L_LikeRogue >= 500:
        ch_l "I guess I've seen her around."
    elif L_LikeRogue >= 400:
        ch_l "I don't want to talk about it."
    elif L_LikeRogue >= 300:
        ch_l "Hate her." 
    else:
        ch_l "Bitch."
          
    return
    
label Laura_AboutKitty:
    ch_l "What do I think about her? Well. . ."
    
    if "poly Kitty" in L_Traits:  
        ch_l "Yeah, we hook up, so. . ."    
    elif L_LikeKitty >= 900:
        ch_l "I do like her little tits. . ."
    elif L_LikeKitty >= 800:
        ch_l "She keeps in shape. . ."  
    elif L_LikeKitty >= 700:
        ch_l "Tough to hold down."
    elif L_LikeKitty >= 600:
        ch_l "She's cool."
    elif L_LikeKitty >= 500:
        ch_l "I guess I've seen her around."
    elif L_LikeKitty >= 400:
        ch_l "I don't want to talk about it."
    elif L_LikeKitty >= 300:
        ch_l "Hate her." 
    else:
        ch_l "Bitch."
          
    return
#End Laura_AboutEmma
label Laura_AboutEmma:
    ch_l "What do I think about her? Well. . ."
    
    if "poly Emma" in L_Traits:  
        ch_l "Yeah, we hook up, so. . ." 
    elif L_LikeEmma >= 900:
        ch_l "Really great rack on her. . ."
    elif L_LikeEmma >= 800:
        ch_l "She smells really nice. . ."    
    elif L_LikeEmma >= 700:
        ch_l "She's nice to me after class."
    elif L_LikeEmma >= 600:
        ch_l "She's a good teacher."
    elif L_LikeEmma >= 500:
        ch_l "She's fine."
    elif L_LikeEmma >= 400:
        ch_l "I could do with less of her attitude."
    elif L_LikeEmma >= 300:
        ch_l "She needs to stay out of my head." 
    else:
        ch_l "Grrrrr."
          
    return
    
#End Laura_AboutEmma   

## Laura's Clothes ///////////////////
label Laura_Clothes:    
    call LauraFace
    menu:
        ch_l "what about my clothes?"
        "Let's talk about your hair color.":
                    jump Laura_Modded_Clothes_Misc_Hair
        "Let's talk about your outfits.":
                    jump Laura_Clothes_Outfits        
        "Let's talk about your over shirts.":
                    jump Laura_Clothes_Over        
        "Let's talk about your legwear.":
                    jump Laura_Clothes_Legs
        "Let's talk about your underwear.":
                    jump Laura_Clothes_Under
        "Let's talk about the other stuff.":
                    jump Laura_Clothes_Misc
        "That looks really good on you, you should remember that one. [[Set Custom]":
                menu:
                    "Which slot would you like this saved in?"
                    "Custom 1":
                                call Laura_OutfitShame(3,1)
                    "Custom 2":
                                call Laura_OutfitShame(5,1)
                    "Custom 3":
                                call Laura_OutfitShame(6,1)
                    "Custom 4":
                                call Laura_OutfitShame(15,1)
                    "Custom 5":
                                call Laura_OutfitShame(16,1)
                    "Custom 6":
                                call Laura_OutfitShame(17,1)
                    "Custom 7":
                                call Laura_OutfitShame(18,1)
                    "Custom 8":
                                call Laura_OutfitShame(19,1)
                    "Custom 9":
                                call Laura_OutfitShame(20,1)
                    "Gym Clothes":
                                call Laura_OutfitShame(7,1)
                    "Sleepwear":
                                call Laura_OutfitShame(9,1)
                    "Swimwear":
                                call Laura_OutfitShame(10,1)
                    "Never mind":
                                pass
        "Switch to. . .":
                menu:
                    "Rogue":
                        call Rogue_Chat_Set("wardrobe")                  
                    "Kitty":
                        call Kitty_Chat_Set("wardrobe")                 
                    "Emma":
                        call Emma_Chat_Set("wardrobe")
                    "Never mind":
                        pass
        "Never mind, you look good like that.":
                if "wardrobe" not in L_RecentActions: 
                        #Apply stat boosts only if it's the first time this turn 
                        if L_Chat[1] <= 1:                
                                call Statup("Laura", "Love", 70, 15)
                                call Statup("Laura", "Obed", 40, 20)
                                ch_l "Oh! Thank you."
                        elif L_Chat[1] <= 10:
                                call Statup("Laura", "Love", 70, 5)
                                call Statup("Laura", "Obed", 40, 7)
                                ch_l "Right?" 
                        elif L_Chat[1] <= 50:
                                call Statup("Laura", "Love", 70, 1)
                                call Statup("Laura", "Obed", 40, 1)  
                                ch_l "Uhhuh."
                        else:
                                ch_l "Sure."                    
                        $ L_RecentActions.append("wardrobe")  
                #sets up a temporary outfit
                $ L_TempClothes[1] = L_Arms  
                $ L_TempClothes[2] = L_Legs 
                $ L_TempClothes[3] = L_Over
                $ L_TempClothes[4] = L_Neck 
                $ L_TempClothes[5] = L_Chest 
                $ L_TempClothes[6] = L_Panties
#                $ L_TempClothes[7] = L_Boots
                $ L_TempClothes[8] = L_Hair
                $ L_TempClothes[9] = L_Hose
                $ L_TempClothes[0] = 1 
                $ L_Outfit = "temporary"
                $ L_OutfitDay = "temporary"        
                $ L_Chat[1] += 1                
                return
            
    jump Laura_Clothes
    #End of Laura Wardrobe Main Menu
        
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Laura_Clothes_Outfits:                                                                                 # Outfits
        "I really like that leather combat outfit you wear.": 
            call LauraOutfit("mission")   
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ L_Outfit = "mission"
                    $ L_Shame = L_OutfitShame[1]
                    ch_l "Yeah, I love wearing this one in the field."
                "Let's try something else though.":
                    ch_l "Ok."            
                    
        "That leather jacket and skirt really nice on you.":  
            call LauraOutfit("streets")
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ L_Outfit = "streets"
                    $ L_Shame = L_OutfitShame[2]
                    ch_l "Yeah, I mean, my cousin got it for me."
                "Let's try something else though.":
                    ch_l "Ok."            
                    
        "Remember that outfit we put together? [[Set a custom outfit] (locked)" if not L_Custom[0] and not L_Custom2[0] and not L_Custom3[0] and not L_Custom4[0] and not L_Custom5[0] and not L_Custom6[0] and not L_Custom7[0] and not L_Custom8[0] and not L_Custom9[0]:
                        pass       
                        
        "Remember that outfit we put together?" if L_Custom[0] or L_Custom2[0] or L_Custom3[0] or L_Custom4[0] or L_Custom5[0] or L_Custom6[0] or L_Custom7[0] or L_Custom8[0] or L_Custom9[0]: 
            $ Cnt = 0
            while 1:
                menu:                
                    "Throw on Custom 1 (locked)" if not L_Custom[0]:
                        pass
                    "Throw on Custom 1" if L_Custom[0]:
                        call LauraOutfit("custom1")
                        $ Cnt = 3
                    "Throw on Custom 2 (locked)" if not L_Custom2[0]:
                        pass
                    "Throw on Custom 2" if L_Custom2[0]:
                        call LauraOutfit("custom2")
                        $ Cnt = 5
                    "Throw on Custom 3 (locked)" if not L_Custom3[0]:
                        pass
                    "Throw on Custom 3" if L_Custom3[0]:
                        call LauraOutfit("custom3")
                        $ Cnt = 6
                    
                    "Throw on Custom 4 (locked)" if not L_Custom4[0]:
                        pass
                    "Throw on Custom 4" if L_Custom4[0]:
                        call LauraOutfit("custom4")
                        $ Cnt = 15
                    "Throw on Custom 5 (locked)" if not L_Custom5[0]:
                        pass
                    "Throw on Custom 5" if L_Custom5[0]:
                        call LauraOutfit("custom5")
                        $ Cnt = 16
                    "Throw on Custom 6 (locked)" if not L_Custom6[0]:
                        pass
                    "Throw on Custom 6" if L_Custom6[0]:
                        call LauraOutfit("custom6")
                        $ Cnt = 17
                    "Throw on Custom 7 (locked)" if not L_Custom7[0]:
                        pass
                    "Throw on Custom 7" if L_Custom7[0]:
                        call LauraOutfit("custom7")
                        $ Cnt = 18
                    "Throw on Custom 8 (locked)" if not L_Custom8[0]:
                        pass
                    "Throw on Custom 8" if L_Custom8[0]:
                        call LauraOutfit("custom8")
                        $ Cnt = 19
                    "Throw on Custom 9 (locked)" if not L_Custom9[0]:
                        pass
                    "Throw on Custom 9" if L_Custom9[0]:
                        call LauraOutfit("custom9")
                        $ Cnt = 20
                    "You should wear this one in our rooms. (locked)" if not Cnt:
                        pass
                    "You should wear this one in our rooms." if Cnt:
                        if Cnt == 5:
                            $ L_Schedule[9] = "custom2"
                        elif Cnt == 15:
                            $ L_Schedule[9] = "custom4"
                        elif Cnt == 16:
                            $ L_Schedule[9] = "custom5"
                        elif Cnt == 17:
                            $ L_Schedule[9] = "custom6"
                        elif Cnt == 18:
                            $ L_Schedule[9] = "custom7"
                        elif Cnt == 19:
                            $ L_Schedule[9] = "custom8"
                        elif Cnt == 20:
                            $ L_Schedule[9] = "custom9"
                        elif Cnt == 6:
                            $ L_Schedule[9] = "custom3"
                        else:
                            $ L_Schedule[9] = "custom"
                        ch_l "Ok, sure."
                    
                    
                    "On second thought, forget about that one outfit. . .":
                        menu:
                            "Custom 1 [[clear custom 1]" if L_Custom[0]:
                                ch_l "Ok."
                                $ L_Custom[0] = 0
                            "Custom 1 [[clear custom 1] (locked)" if not L_Custom[0]:
                                pass
                            "Custom 2 [[clear custom 2]" if L_Custom2[0]:
                                ch_l "Ok."
                                $ L_Custom2[0] = 0
                            "Custom 2 [[clear custom 1] (locked)" if not L_Custom2[0]:
                                pass
                            "Custom 3 [[clear custom 3]" if L_Custom3[0]:
                                ch_l "Ok."
                                $ L_Custom3[0] = 0
                            "Custom 3 [[clear custom 3] (locked)" if not L_Custom3[0]:
                                pass
                            "Custom 4 [[clear custom 4]" if L_Custom4[0]:
                                ch_l "Ok."
                                $ L_Custom4[0] = 0
                            "Custom 4 [[clear custom 4] (locked)" if not L_Custom4[0]:
                                pass
                            "Custom 5 [[clear custom 5]" if L_Custom5[0]:
                                ch_l "Ok."
                                $ L_Custom5[0] = 0
                            "Custom 5 [[clear custom 5] (locked)" if not L_Custom5[0]:
                                pass
                            "Custom 6 [[clear custom 6]" if L_Custom6[0]:
                                ch_l "Ok."
                                $ L_Custom6[0] = 0
                            "Custom 6 [[clear custom 6] (locked)" if not L_Custom6[0]:
                                pass
                            "Custom 7 [[clear custom 7]" if L_Custom7[0]:
                                ch_l "Ok."
                                $ L_Custom7[0] = 0
                            "Custom 7 [[clear custom 7] (locked)" if not L_Custom7[0]:
                                pass
                            "Custom 8 [[clear custom 8]" if L_Custom8[0]:
                                ch_l "Ok."
                                $ L_Custom8[0] = 0
                            "Custom 8 [[clear custom 8] (locked)" if not L_Custom8[0]:
                                pass
                            "Custom 9 [[clear custom 9]" if L_Custom9[0]:
                                ch_l "Ok."
                                $ L_Custom9[0] = 0
                            "Custom 9 [[clear custom 9] (locked)" if not L_Custom9[0]:
                                pass
                            "Never mind, [[back].":
                                pass    
                                            
                                            
                    "You should wear this one out. [[choose outfit first](locked)" if not Cnt:
                        pass
                    "You should wear this one out." if Cnt:
                        call Laura_Custom_Out(Cnt)
                    "Ok, back to what we were talking about. . .":
                        $ Cnt = 0
                        jump Laura_Clothes_Outfits                    
        
        "Your birthday suit looks really great. . .":                                     #Nude
            call LauraFace("sexy", 1)
            $ Line = 0
            if not L_Chest and not L_Panties and not L_Over and not L_Legs and not L_Hose:                
                ch_l "Yeah. . . wait, how would you know?"  
            elif L_SeenChest and L_SeenPussy and ApprovalCheck("Laura", 1200, TabM=4):
                ch_l "You know it. . ."  
                $ Line = 1
            elif ApprovalCheck("Laura", 2000, TabM=4):
                ch_l "Skipping straight to that?"    
                $ Line = 1
            elif L_SeenChest and L_SeenPussy and ApprovalCheck("Laura", 1200, TabM=0):
                ch_l "Maybe, but not here. . ."  
            elif ApprovalCheck("Laura", 2000, TabM=0):
                ch_l "Maybe, but not here. . ."  
            elif ApprovalCheck("Laura", 1000, TabM=0):                
                call LauraFace("confused", 1,Mouth="smirk")
                ch_l "Yeah, but I'm not exactly showing it off."
                call LauraFace("bemused", 0)
            else:
                call LauraFace("angry", 1)
                ch_l "What's it to you?"    
                
            if Line:                                                            #If she got nude. . .                            
                call LauraOutfit("nude")
                "She throws her clothes off at her feet."
                call Laura_First_Topless
                call Laura_First_Bottomless(1)
                call LauraFace("sexy")
                menu:
                    "You know, you should wear this one out. [[set current outfit]":
                        if "exhibitionist" in L_Traits:
                            ch_l "mmmm. . ." 
                            $ L_Outfit = "nude"
                            call Statup("Laura", "Lust", 50, 10) 
                            call Statup("Laura", "Lust", 70, 5) 
                            $ L_Shame = L_OutfitShame[0]
                        elif ApprovalCheck("Laura", 800, "I") or ApprovalCheck("Laura", 2800, TabM=0):                    
                            ch_l "Exciting. . ."
                            $ L_Outfit = "nude"
                            $ L_Shame = L_OutfitShame[0]
                        else:
                            call LauraFace("sexy", 1)
                            $ L_Eyes = "surprised"
                            ch_l "I probably shouldn't. Sorry." 
                            
                    "Let's try something else though.":
                        if "exhibitionist" in L_Traits:
                            ch_l "Are you sure?"                         
                        elif ApprovalCheck("Laura", 800, "I") or ApprovalCheck("Laura", 2800, TabM=0):       
                            call LauraFace("bemused", 1)             
                            ch_l "I was worried you expected me to wear this out."
                            ch_l ". . ."
                        else:
                            call LauraFace("confused", 1)
                            ch_l "I don't mind you seeing my body, but. . ."   
            $ Line = 0
                
        "How about throwing on your sleepwear?" if not Taboo:
            #fix add conditions
            call LauraOutfit("sleep")
            
        "How about throwing on your swimwear?" if not Taboo or bg_current == "bg pool":
            #fix add conditions
            call LauraOutfit("swimwear")
                        
        "Let's talk about what you wear outside.":
            call Laura_Clothes_Schedule
            
        "Never mind":    
            jump Laura_Clothes     
            
    jump Laura_Clothes
    #End of Laura Outfits
            
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Laura_Clothes_Over:                                                                                            # Overshirts
        "Why don't you go with no [L_Over]?" if L_Over:
            call LauraFace("bemused", 1)
            if ApprovalCheck("Laura", 800, TabM=3) and (L_Chest or L_SeenChest):
                ch_l "Ok."
            elif ApprovalCheck("Laura", 1200, TabM=0):
                call Laura_NoBra
                if not _return:
                    jump Laura_Clothes
            $ Line = L_Over
            $ L_Over = 0
            "She throws her [Line] at her feet."
            if not L_Chest:
                    call Laura_First_Topless
            
        "Try on that leather jacket." if L_Over != "jacket":
            call LauraFace("bemused")
            if not L_Over or L_Chest == "leather bra":
                #if she's not already wearing a top, or has the leather bra on
                ch_l "Sure."
            elif ApprovalCheck("Laura", 800, TabM=0):
                ch_l "Yeah, ok."          
            else:
                call LauraFace("bemused", 1)
                ch_l "I don't really want to take this [L_Over] off at the moment."
                jump Laura_Clothes    
            $ L_Over = "jacket"   
                
#        "How about that red t-shirt you have?" if L_Over != "red shirt":
#            $ L_Over = "red shirt"  
#            ch_l "This one?"
            
        "Maybe just throw on a towel?" if L_Over != "towel":
            call LauraFace("bemused", 1)
            if L_Chest or L_SeenChest:
                ch_l "Weird."
            elif ApprovalCheck("Laura", 1000, TabM=0):
                call LauraFace("perplexed", 1)
                ch_l "Huh, ok . ."          
            else:
                ch_l "That wouldn't look right."
                jump Laura_Clothes    
            $ L_Over = "towel"    
                            
        "Never mind":
            pass
    jump Laura_Clothes
    #End of Laura Top
            
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    label Laura_NoBra: #fix test this
        menu:
            ch_l "I don't exactly have anything on under this. . ."
            "Then you could slip something on under it. . .":   
                        if L_SeenChest and ApprovalCheck("Laura", 1000, TabM=3):
                                $ L_Blush = 1
                                ch_l "-I didn't say that I minded. . ."
                                $ L_Blush = 0                        
                        elif ApprovalCheck("Laura", 1200, TabM=4):
                                $ L_Blush = 1
                                ch_l "-I didn't say that I minded. . ."
                                $ L_Blush = 0                
                        elif ApprovalCheck("Laura", 900, TabM=2) and "lace corset" in L_Inventory:
                                ch_l "I guess I could find something."
                                $ L_Chest  = "lace corset"    
                                "She pulls out her lace corset and slips it under her [L_Over]."
                        elif ApprovalCheck("Laura", 700, TabM=2) and "corset" in L_Inventory:
                                ch_l "I guess I could find something."
                                $ L_Chest  = "corset"    
                                "She pulls out her corset and slips it under her [L_Over]."
                        elif ApprovalCheck("Laura", 600, TabM=2):
                                ch_l "Yeah, I guess."
                                $ L_Chest = "leather bra"
                                "She pulls out her leather bra and slips it on under her [L_Over]."
#                        elif ApprovalCheck("Laura", 600, TabM=2):
#                                ch_l "Yeah, I guess."
#                                $ L_Chest = "sports bra"
#                                "She pulls out her sports bra and passes it through her [L_Over]."
                        else:
                                ch_l "Yeah, I don't think so."
                                return 0
                        
            "You could always just wear nothing at all. . .":
                        if ApprovalCheck("Laura", 1100, "LI", TabM=2) and L_Love > L_Inbt:               
                                ch_l "For you? I guess. . ."
                        elif ApprovalCheck("Laura", 700, "OI", TabM=2) and L_Obed > L_Inbt:
                                ch_l "Sure. . ."
                        elif ApprovalCheck("Laura", 600, "I", TabM=2):
                                ch_l "Yeah. . ."
                        elif ApprovalCheck("Laura", 1300, TabM=2):
                                ch_l "Okay, fine."
                        else: 
                                call LauraFace("surprised")
                                $ L_Brows = "angry"
                                if Taboo > 20:
                                    ch_l "Not in public, I won't!"
                                else:
                                    ch_l "You're not that cute, [L_Petname]!"
                                return 0
                                
                    
            "Never mind.":
                        ch_l "Ok. . ."
                        return 0
        return 1
        #End of Laura bra check
       
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Laura_Clothes_Legs:                                                                                                    # Leggings    
        "Maybe go without the [L_Legs]." if L_Legs:
            call LauraFace("sexy", 1)
            if L_SeenPanties and L_Panties and ApprovalCheck("Laura", 500, TabM=5):
                ch_l "Ok, sure."
            elif L_SeenPussy and ApprovalCheck("Laura", 900, TabM=4):
                ch_l "Yeah, ok."
            elif ApprovalCheck("Laura", 1300, TabM=2) and L_Panties:
                ch_l "For you, fine. . ."
            elif ApprovalCheck("Laura", 800) and not L_Panties:
                call Laura_NoPantiesOn
                if not _return:
                    jump Laura_Clothes
            else:
                ch_l "Um, not with you around."
                if not L_Panties:
                    ch_l "I'm going commando today. . ."
                jump Laura_Clothes
            if L_Legs == "leather pants" or L_Legs == "mesh pants":
                    $ L_Legs = 0    
                    "She tugs her pants off and drops them to the ground."
            else:
                    $ L_Legs = 0    
                    "She tugs her skirt off and drops it to the ground."
            if L_Panties:                
                $ L_SeenPanties = 1
            else:
                call Laura_First_Bottomless
        
        "You look great in those leather pants." if L_Legs != "leather pants":
            ch_l "Yeah, ok."
            $ L_Legs = "leather pants"
                
        "You look great in those mesh pants." if L_Legs != "mesh pants":
            if ApprovalCheck("Laura", 1000, TabM=4):
                    ch_l "Yeah, ok."
                    $ L_Legs = "mesh pants"
            else:
                    ch_l "Sorry, those are kind of. . . breezy."
        
#        "You look great in yoga pants." if L_Legs != "yoga pants":
#            ch_l "Yeah, ok."
#            $ L_Legs = "yoga pants"
            
        "What about wearing your leather skirt?" if L_Legs != "skirt":
            ch_l "Sure, why not."
            $ L_Legs = "skirt"    
            
                   
                                
        "Never mind":
            pass
    jump Laura_Clothes
    #End of Laura Pants
    
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
    
    label Laura_NoPantiesOn: #fix test this
        menu:
            ch_l "I'm going commando today."
            "Then you could slip on a pair of panties. . .":   
                        if L_SeenPussy and ApprovalCheck("Laura", 1100, TabM=4):
                                $ L_Blush = 1
                                ch_l "No, commando's fine. . ."
                                $ L_Blush = 0                        
                        elif ApprovalCheck("Laura", 1500, TabM=4):
                                $ L_Blush = 1
                                ch_l "No, commando's fine. . ."
                                $ L_Blush = 0                
                        elif ApprovalCheck("Laura", 800, TabM=4) and "lace panties" in L_Inventory:
                                ch_l "I like how you think."
                                $ L_Panties  = "lace panties"  
                                if ApprovalCheck("Laura", 1200, TabM=4):   
                                    $ Line = L_Legs
                                    $ L_Legs = 0
                                    "She pulls off her [L_Legs] and slips on the lace panties."                                    
                                elif L_Legs == "skirt":
                                    "She pulls out her lace panties and pulls them up under her skirt."
                                    $ L_Legs = 0
                                    "Then she drops the skirt to the floor."
                                else:
                                    $ Line = L_Legs
                                    $ L_Legs = 0
                                    "She steps away a moment and then comes back wearing only the lace panties."                                     
                                jump Laura_Clothes
                        elif ApprovalCheck("Laura", 700, TabM=4):
                                ch_l "Yeah, I guess."
                                $ L_Panties = "black panties"
                                if ApprovalCheck("Laura", 1200, TabM=4):   
                                    $ Line = L_Legs
                                    $ L_Legs = 0
                                    "She pulls off her [L_Legs] and slips on the black panties."                                    
                                elif L_Legs == "skirt":
                                    "She pulls out her black panties and pulls them up under her skirt."
                                    $ L_Legs = 0
                                    "Then she drops the skirt to the floor."
                                else:
                                    $ Line = L_Legs
                                    $ L_Legs = 0
                                    "She steps away a moment and then comes back wearing only the black panties."                                     
                                jump Laura_Clothes
                        else:
                                ch_l "Nope."
                                return 0
                        
            "You could always just wear nothing at all. . .":
                        if ApprovalCheck("Laura", 1100, "LI", TabM=3) and L_Love > L_Inbt:               
                                ch_l "True. . ."
                        elif ApprovalCheck("Laura", 700, "OI", TabM=3) and L_Obed > L_Inbt:
                                ch_l "Yes. . ."
                        elif ApprovalCheck("Laura", 600, "I", TabM=3):
                                ch_l "Hrmm. . ."
                        elif ApprovalCheck("Laura", 1300, TabM=3):
                                ch_l "Fine."
                        else: 
                                call LauraFace("surprised")
                                $ L_Brows = "angry"
                                if Taboo > 20:
                                    ch_l "Yeah, but not in public, [L_Petname]!"
                                else:
                                    ch_l "You aren't that cute, [L_Petname]!"
                                return 0
                                
            "Never mind.":
                ch_l "Ok. . ."
                return 0
        return 1
        #End of Laura Panties check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Laura_Clothes_Under:   
        "Tops":
            menu:
                # Tops    
                "How about you lose the [L_Chest]?" if L_Chest:
                    call LauraFace("bemused", 1)
                    if L_SeenChest and ApprovalCheck("Laura", 900, TabM=2.7):
                        ch_l "Ok."    
                    elif ApprovalCheck("Laura", 1100, TabM=2):
                        if Taboo:
                            ch_l "I don't know, here. . ."
                        else:
                            ch_l "Maybe. . ."
                    elif L_Over == "jacket" and ApprovalCheck("Laura", 600, TabM=2):
                        ch_l "This jacket is a bit revealing. . ."  
                    elif L_Over and ApprovalCheck("Laura", 500, TabM=2):
                        ch_l "I guess I could. . ."  
                    elif not L_Over:
                        ch_l "Not without some other top."
                        jump Laura_Clothes 
                    else:
                        ch_l "Nah."
                        jump Laura_Clothes 
                    $ Line = L_Chest
                    $ L_Chest = 0
                    if L_Over:
                        "She reaches under her [L_Over] grabs her [Line], and pulls it off, dropping it to the ground."
                    else:
                        "She pulls off her [Line] and drops it to the ground."
                        call Laura_First_Topless
                    
                    
                "Try on that leather bra." if L_Chest != "leather bra":
                    ch_l "Ok."
                    $ L_Chest = "leather bra"           
                    
                "I like that red corset." if L_Chest != "corset" and "corset" in L_Inventory :
                    if L_SeenChest or ApprovalCheck("Laura", 1000, TabM=1):
                        ch_l "K."   
                        $ L_Chest = "corset"         
                    else:                
                        ch_l "It's a bit revealing. . ."  
                        
                "I like that lace corset." if L_Chest != "lace corset" and "lace corset" in L_Inventory :
                    if L_SeenChest or ApprovalCheck("Laura", 1300, TabM=2):
                        ch_l "K."   
                        $ L_Chest = "lace corset"         
                    else:                
                        ch_l "It's a bit transparent. . ."  
                                    
                "I like that wolverine tanktop." if L_Chest != "wolvie top" and "wolvie top" in L_Inventory:
                    if L_SeenChest or ApprovalCheck("Laura", 1000, TabM=2):
                        ch_l "K."   
                        $ L_Chest = "wolvie top"         
                    else:                
                        ch_l "It's a {i}little{/i} embarrassing. . ."  
               
                "I like that bikini top." if L_Chest != "bikini top" and "bikini top" in L_Inventory:
                    if bg_current == "bg pool":
                            ch_l "K."   
                            $ L_Chest = "bikini top"         
                    else:                
                            if L_SeenChest or ApprovalCheck("Laura", 1000, TabM=2):
                                ch_l "K."   
                                $ L_Chest = "bikini top"         
                            else:                
                                ch_l "This is not really a \"bikini\" sort of place. . ." 
                "Never mind":
                    pass 
              
        "Hose and stockings options":
            menu:          
                "You could lose the hose." if L_Hose and L_Hose != 'ripped tights' and L_Hose != 'tights':     
                                $ L_Hose = 0  
                "The thigh-high hose would look good with that." if L_Hose != "stockings":     
                                $ L_Hose = "stockings"  
                "The stockings and garterbelt would look good with that." if L_Hose != "stockings and garterbelt" and "lace panties" in L_Inventory:     
                                $ L_Hose = "stockings and garterbelt"  
                "Just the garterbelt would look good with that." if L_Hose != "garterbelt" and "lace panties" in L_Inventory:     
                                $ L_Hose = "garterbelt"  
#                "The pantyhose would look good with that." if L_Hose != "pantyhose":     
#                                $ L_Hose = "pantyhose" 
#                "Your ripped pantyhose would look good with that." if L_Hose != "ripped pantyhose" and "ripped pantyhose" in L_Inventory:     
#                                $ L_Hose = "ripped pantyhose"    
                "Never mind":
                        pass  
                        
        #Panties    
        "Panties":
            menu:
                "You could lose those panties. . ." if L_Panties:
                    call LauraFace("bemused", 1)  
                    if ApprovalCheck("Laura", 900) and (L_Legs or (L_SeenPussy and not Taboo)):
                        #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
                        
                        if ApprovalCheck("Laura", 850, "L"):               
                                ch_l "True. . ."
                        elif ApprovalCheck("Laura", 500, "O"):
                                ch_l "Agreed."
                        elif ApprovalCheck("Laura", 350, "I"):
                                ch_l "Heh."
                        else:
                                ch_l "Sure, I guess."         
                    else:                       #low approval or not wearing pants or in public 
                        if ApprovalCheck("Laura", 1100, "LI", TabM=3) and L_Love > L_Inbt:               
                                ch_l "Well look, it's not about you, but. . ."
                        elif ApprovalCheck("Laura", 700, "OI", TabM=3) and L_Obed > L_Inbt:
                                ch_l "Well. . ."
                        elif ApprovalCheck("Laura", 600, "I", TabM=3):
                                ch_l "Hrmm. . ."
                        elif ApprovalCheck("Laura", 1300, TabM=3):
                                ch_l "Okay, okay."
                        else: 
                                call LauraFace("surprised")
                                $ L_Brows = "angry"
                                if Taboo > 20:
                                    ch_l "This is too public."
                                else:
                                    ch_l "You're not that cute, [L_Petname]!"
                                jump Laura_Clothes
                                
                    $ L_Panties = 0
                    if not L_Legs:
                        "She pulls off her panties, then drops them to the ground." 
                        call Laura_First_Bottomless  
                    if ApprovalCheck("Laura", 1200, TabM=4):   
                        $ Line = L_Legs
                        $ L_Legs = 0
                        "She pulls off her [L_Legs] and panties, then pulls the [L_Legs] back on."  
                        $ L_Legs = Line       
                        call Laura_First_Bottomless(1)                             
                    elif L_Legs == "skirt":
                        "She reaches under her skirt and pulls her panties off."
                    else:
                        $ L_Blush = 1
                        "She steps away a moment and then comes back."  
                        $ L_Blush = 0                                    
                        
                "Why don't you wear the black panties instead?" if L_Panties and L_Panties != "black panties":
                    if ApprovalCheck("Laura", 1100, TabM=3):
                            ch_l "Ok."
                            $ L_Panties = "black panties"  
                    else:                
                            ch_l "That's none of your busines."
                        
                "Why don't you wear the wolverine panties instead?" if "wolvie panties" in L_Inventory and L_Panties and L_Panties != "wolvie panties":
                    if ApprovalCheck("Laura", 1000, TabM=3):
                            ch_l "I guess."
                            $ L_Panties = "wolvie panties"
                    else:
                            ch_l "That's none of your busines."
                            
                "Why don't you wear the lace panties instead?" if "lace panties" in L_Inventory and L_Panties and L_Panties != "lace panties":
                    if ApprovalCheck("Laura", 1300, TabM=3):
                            ch_l "I guess."
                            $ L_Panties = "lace panties"
                    else:
                            ch_l "That's none of your busines."
                            
                "I like those bikini bottoms." if "bikini bottoms" in L_Inventory and L_Panties != "bikini bottoms":                            
                    if bg_current == "bg pool":
                            ch_l "K."   
                            $ L_Panties = "bikini bottoms"         
                    else:                
                            if ApprovalCheck("Laura", 1000, TabM=2):
                                ch_l "K."   
                                $ L_Panties = "bikini bottoms"         
                            else:                
                                ch_l "This is not really a \"bikini\" sort of place. . ." 
                        
                "You know, you could wear some panties with that. . ." if not L_Panties:
                    call LauraFace("bemused", 1)
                    if (L_Love+L_Obed) <= (2 * L_Inbt):
                        $ L_Mouth = "smile"
                        ch_l "I don't know about that."
                        call Statup("Laura", "Inbt", 70, 2)
                        menu:
                            "Fine by me":
                                call Statup("Laura", "Love", 90, 2)
                                call Statup("Laura", "Inbt", 70, 2)
                                jump Laura_Clothes
                            "I insist, put some on.":
                                if (L_Love+L_Obed) <= (1.5 * L_Inbt):
                                    call LauraFace("angry", Eyes="side")
                                    call Statup("Laura", "Inbt", 99, 5)
                                    call Statup("Laura", "Obed", 80, -5)
                                    ch_l "Well I insist otherwise."
                                    jump Laura_Clothes
                                else:
                                    call LauraFace("sadside")
                                    call Statup("Laura", "Inbt", 200, -5)
                                    call Statup("Laura", "Obed", 80, 5)
                                    ch_l "Oh, fine."    
                    else:                
                        ch_l "I guess. . ."
                    menu:
                        extend ""
                        "How about the black ones?":
                            ch_l "Sure, ok."
                            $ L_Panties = "black panties"
                        "How about the wolvie ones?" if "wolvie panties" in L_Inventory:
                            ch_l "Sure."                
                            $ L_Panties  = "wolvie panties"
                        "How about the lace ones?" if "lace panties" in L_Inventory:
                            ch_l "Alright."                
                            $ L_Panties  = "lace panties"
                "Never mind":
                    pass
        "Never mind":
            pass
    jump Laura_Clothes
    #End of Laura Underwear
       
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  
        
    menu Laura_Clothes_Misc:                                                                                                                    #Misc
#        "You look good with your hair up." if L_Hair != "evo":
#            if ApprovalCheck("Laura", 600):
#                ch_l "Like this?"
#                $ L_Hair = "evo"
#            else:
#                ch_l "Yeah, I know that."
                
        "Maybe dry out your hair." if L_Hair == "wet":
            if ApprovalCheck("Laura", 600):
                ch_l "Ok."
                $ L_Hair = "long"
            else:
                ch_l "I don't know, it's fine like this."
                
        "You should go for that wet look with your hair." if L_Hair != "wet":
            if ApprovalCheck("Laura", 800):
                ch_l "Hmm?"
                "She wanders off for a minute and comes back."
                ch_l "Like this?"
                $ L_Hair = "wet"
            else:
                ch_l "Ugh, too much work."
        
        "You know, I like some nice hair down there. Maybe grow it out." if not L_Pubes and "pubes" in L_Todo:
            call LauraFace("bemused", 1)
            ch_l "Even I can't grow it out instantly."
        "You know, I like some nice hair down there. Maybe grow it out." if not L_Pubes and "pubes" not in L_Todo:
            call LauraFace("bemused", 1)
            if ApprovalCheck("Laura", 1000, TabM=0):               
                ch_l "Sure, that's easier. . ."           
            else: 
                call LauraFace("surprised")
                $ L_Brows = "angry"
                ch_l "I think I'll do what I want down there."
                jump Laura_Clothes
            $ L_Todo.append("pubes")
            $ L_PubeC = 6
        
        "I like it waxed clean down there." if L_Pubes == 1:
            call LauraFace("bemused", 1)            
            if "shave" in L_Todo:
                ch_l "Yeah, I know, I'll get to it."
            else:
                if ApprovalCheck("Laura", 1100, TabM=0):               
                    ch_l "Really? I guess I could give it a shave. . ."        
                else: 
                    call LauraFace("surprised")
                    $ L_Brows = "angry"
                    ch_l "I think I'll do what I want down there."
                    jump Laura_Clothes
                $ L_Todo.append("shave")        
        "Piercings. [[See what she looks like without them first] (locked)" if not L_SeenPussy and not L_SeenChest:
            pass
            
        "You know, you'd look really nice with some ring body piercings." if L_Pierce != "ring" and (L_SeenPussy or L_SeenChest) and "ring" not in L_Todo:
            call LauraFace("bemused", 1)
            $ Approval = ApprovalCheck("Laura", 1150, TabM=0)
            if ApprovalCheck("Laura", 900, "L", TabM=0) or (Approval and L_Love > 2* L_Obed):   
                ch_l "You think I'd look good with them?"
            elif ApprovalCheck("Laura", 600, "I", TabM=0) or (Approval and L_Inbt > L_Obed):
                ch_l "I've been thinking about that for a while."
            elif ApprovalCheck("Laura", 500, "O", TabM=0) or Approval:
                ch_l "Yes, [L_Petname]."
            else: 
                call LauraFace("surprised")
                $ L_Brows = "angry"
                ch_l "Not interested, [L_Petname]."
                jump Laura_Clothes            
            $ L_Todo.append("ring")
        
        "You know, you'd look really nice with some barbell body piercings." if L_Pierce != "barbell" and (L_SeenPussy or L_SeenChest)and "barbell" not in L_Todo:
            call LauraFace("bemused", 1)
            $ Approval = ApprovalCheck("Laura", 1150, TabM=0)
            if ApprovalCheck("Laura", 900, "L", TabM=0) or (Approval and L_Love > 2 * L_Obed):   
                ch_l "You think I'd look good with them?"
            elif ApprovalCheck("Laura", 600, "I", TabM=0) or (Approval and L_Inbt > L_Obed):
                ch_l "I've been thinking about that for a while."
            elif ApprovalCheck("Laura", 500, "O", TabM=0) or Approval:
                ch_l "Yes, [L_Petname]."
            else: 
                call LauraFace("surprised")
                $ L_Brows = "angry"
                ch_l "Not interested, [L_Petname]."
                jump Laura_Clothes                
            $ L_Todo.append("barbell")
            $ L_Pierce = "barbell"
            
        "You know, you'd look better without those piercings." if L_Pierce:
            call LauraFace("bemused", 1)
            $ Approval = ApprovalCheck("Laura", 1350, TabM=0)
            if ApprovalCheck("Laura", 950, "L", TabM=0) or (Approval and L_Love > L_Obed):   
                ch_l "Make up your mind . ."
            elif ApprovalCheck("Laura", 700, "I", TabM=0) or (Approval and L_Inbt > L_Obed):
                ch_l "In, out, snickt."
            elif ApprovalCheck("Laura", 600, "O", TabM=0) or Approval:
                ch_l "Fine."
            else: 
                call LauraFace("surprised")
                $ L_Brows = "angry"
                ch_l "I've sort of grown attached."
                jump Laura_Clothes            
            $ L_Pierce = 0 
        "Why don't you try on that medallion choker." if L_Neck != "leash choker":
            ch_l "Ok. . ."         
            $ L_Neck = "leash choker"
        "Maybe go without a necklace." if L_Neck:
            ch_l "Ok. . ."         
            $ L_Neck = 0
            
        "Why don't you put those wristbands on." if L_Arms != "wrists":
            ch_l "Ok. . ."         
            $ L_Arms = "wrists"
        "Maybe go without the wristbands." if L_Arms:
            ch_l "Ok. . ."         
            $ L_Arms = 0
            
        "Never mind":
            pass         
    jump Laura_Clothes
    #End of Laura Misc Wardrobe
    
return
#End Laura Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <



# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

label Laura_Clothes_Schedule(Cnt = 0):
        #Sets clothing for different days, if Cnt is 3 it's all days, 2 is TuThu, 1 is only weekends
        
        if ApprovalCheck("Laura", 1500, "LO"):
                ch_l "Fine, you pick, whatever."
                $ Cnt = 3
        elif ApprovalCheck("Laura", 1200, "LO"):
                ch_l "I don't know, you could pick a few days. . ."
                $ Cnt = 2
        elif ApprovalCheck("Laura", 1000, "LO"):
                ch_l "Maybe on weekends. . ."
                $ Cnt = 1
        else:
                ch_l "Nah, I got it covered."
                return
            
        
        menu:
                extend ""
                "Weekdays":
                    menu:
                        "On Monday you should wear. . ." if Cnt > 1:
                            call Laura_Clothes_ScheduleB
                            $ L_Schedule[0] = _return
                        "On Monday you should wear. . . (locked)" if Cnt <= 1:
                            pass
                            
                        "On Tuesday you should wear. . ." if Cnt > 2:
                            call Laura_Clothes_ScheduleB
                            $ L_Schedule[1] = _return        
                        "On Tuesday you should wear. . . (locked)" if Cnt <= 2:
                            pass
                            
                        "On Wednesday you should wear. . ." if Cnt > 1:
                            call Laura_Clothes_ScheduleB
                            $ L_Schedule[2] = _return
                        "On Wednesday you should wear. . . (locked)" if Cnt <= 1:
                            pass   
                            
                        "On Thursday you should wear. . ." if Cnt > 2:
                            call Laura_Clothes_ScheduleB
                            $ L_Schedule[3] = _return
                        "On Thursday you should wear. . . (locked)" if Cnt <= 2:
                            pass
                            
                        "On Friday you should wear. . ." if Cnt > 1:
                            call Laura_Clothes_ScheduleB
                            $ L_Schedule[4] = _return
                        "On Friday you should wear. . . (locked)" if Cnt <= 1:
                            pass 
                        "Back":
                            pass         
               
                "Other":
                    menu:       
                        "On Saturday you should wear. . . (locked)" if Cnt < 1:
                            pass
                        "On Saturday you should wear. . ." if Cnt >= 1:
                            call Laura_Clothes_ScheduleB
                            $ L_Schedule[5] = _return
                            
                        "On Sunday you should wear. . . (locked)" if Cnt < 1:
                            pass                          
                        "On Sunday you should wear. . ." if Cnt >= 1:
                            call Laura_Clothes_ScheduleB
                            $ L_Schedule[6] = _return
                            
                        "In our rooms you should wear. . . (locked)" if Cnt < 1:
                            pass
                        "In our rooms you should wear. . ." if Cnt >= 1:
                            call Laura_Clothes_ScheduleB(99)
                            $ L_Schedule[9] = _return   
                            
                        "On dates you should wear. . . (locked)" if Cnt < 2:
                            pass  
                        "On dates you should wear. . ." if Cnt >= 2:
                            call Laura_Clothes_ScheduleB
                            $ L_Schedule[7] = _return     
                        "Back":
                            pass         
                    
                "Never mind":
                    return        
        jump Laura_Clothes_Schedule
    
    
    
label Laura_Clothes_ScheduleB(Count = 0):
#This is called by Laura_Clothes_Schedule when setting her outfit for a given day
#If Count by the end, yes, if not count, no. If count is 99 then it's an auto-yes
            
            menu:
                "That leather combat look.":
                    $ Count = 1
                "Your jacket and skirt.":
                    $ Count = 2
                "That outfit we put together [[custom]" if L_Custom[0] or L_Custom2[0] or L_Custom3[0] or L_Custom4[0] or L_Custom5[0] or L_Custom6[0] or L_Custom7[0] or L_Custom8[0] or L_Custom9[0]:
                            menu:
                                ch_l "Which one?"
                                "The first one. (locked)" if not L_Custom[0]:
                                    pass
                                "The first one." if L_Custom[0]:
                                    if L_Custom[0] == 2 or Count == 99:
                                        $ Count = 3
                                    else:
                                        ch_l "I told you I wouldn't wear that out."
                                        
                                "The second one. (locked)" if not L_Custom2[0]:
                                    pass
                                "The second one." if L_Custom2[0]:
                                    if L_Custom2[0] == 2 or Count == 99:
                                        $ Count = 5
                                    else:
                                        ch_l "I told you I wouldn't wear that out."
                                        
                                "The third one. (locked)" if not L_Custom3[0]:
                                    pass
                                "The third one." if L_Custom3[0]:
                                    if L_Custom3[0] == 2 or Count == 99:
                                        $ Count = 6
                                    else:
                                        ch_l "I told you I wouldn't wear that out."
                                        
                                "The fourth one. (locked)" if not L_Custom4[0]:
                                    pass
                                "The fourth one." if L_Custom4[0]:
                                    if L_Custom4[0] == 2 or Count == 99:
                                        $ Count = 15
                                    else:
                                        ch_l "I told you I wouldn't wear that out."
                                        
                                "The fifth one. (locked)" if not L_Custom5[0]:
                                    pass
                                "The fifth one." if L_Custom5[0]:
                                    if L_Custom5[0] == 2 or Count == 99:
                                        $ Count = 16
                                    else:
                                        ch_l "I told you I wouldn't wear that out."
                                        
                                "The sixth one. (locked)" if not L_Custom6[0]:
                                    pass
                                "The sixth one." if L_Custom6[0]:
                                    if L_Custom6[0] == 2 or Count == 99:
                                        $ Count = 17
                                    else:
                                        ch_l "I told you I wouldn't wear that out."
                                        
                                "The seventh one. (locked)" if not L_Custom7[0]:
                                    pass
                                "The seventh one." if L_Custom7[0]:
                                    if L_Custom7[0] == 2 or Count == 99:
                                        $ Count = 18
                                    else:
                                        ch_l "I told you I wouldn't wear that out."
                                        
                                "The eighth one. (locked)" if not L_Custom8[0]:
                                    pass
                                "The eighth one." if L_Custom8[0]:
                                    if L_Custom8[0] == 2 or Count == 99:
                                        $ Count = 19
                                    else:
                                        ch_l "I told you I wouldn't wear that out."
                                        
                                "The ninth one. (locked)" if not L_Custom9[0]:
                                    pass
                                "The ninth one." if L_Custom9[0]:
                                    if L_Custom9[0] == 2 or Count == 99:
                                        $ Count = 20
                                    else:
                                        ch_l "I told you I wouldn't wear that out."
                                        
                                "Never mind":
                                    pass
                "Your gym clothes.":
                    $ Count = 4                
                "Your sleepwear.":
                    if Count != 99:
                        ch_l "That's kinda skimpy, [L_Petname]."
                        $ Count = 0
                    else:
                        $ Count = 7
                "Whatever you like.":
                    pass
                    
            if Count:
                        ch_l "Ok, sure."
            else:
                        ch_l "I'll figure something else out."
            return Count    
#End Laura Clothes Scheduling Check


label L_AltClothes(Outfit=8):
        #1 = "mission", 2 = "streets"
        #3 = "custom1", 5 = "custom2", 6 = "custom3", 7 = "sleep", 4 = "gym", 10 = "swimwear"
        #This selects her outfit when teaching if 8
        #This selects her private outfit if 9
        
        if L_Schedule[Outfit] == 1 or not L_Schedule[Outfit]:
                    $ L_Outfit = "mission"
        elif L_Schedule[Outfit] == 2:
                    $ L_Outfit = "streets"
        elif L_Schedule[Outfit] == 15:
                    $ L_Outfit = "custom4"
        elif L_Schedule[Outfit] == 16:
                    $ L_Outfit = "custom5"
        elif L_Schedule[Outfit] == 17:
                    $ L_Outfit = "custom6"
        elif L_Schedule[Outfit] == 18:
                    $ L_Outfit = "custom7"
        elif L_Schedule[Outfit] == 19:
                    $ L_Outfit = "custom8"
        elif L_Schedule[Outfit] == 20:
                    $ L_Outfit = "custom9"
        elif L_Schedule[Outfit] == 3:
                    $ L_Outfit = "custom1"
        elif L_Schedule[Outfit] == 5:
                    $ L_Outfit = "custom2"
        elif L_Schedule[Outfit] == 6:
                    $ L_Outfit = "custom3"
        elif L_Schedule[Outfit] == 7:
                    $ L_Outfit = "sleep"
        elif L_Schedule[Outfit] == 4:
                    $ L_Outfit = "gym"
        elif L_Schedule[Outfit] == 10:
                    $ L_Outfit = "swimwear"
        return
  
label L_Private_Outfit:
    #sets Laura's private outfit in private
    if "comfy" in L_RecentActions or "comfy" in L_Traits or L_Outfit == L_Schedule[9]:
            call L_AltClothes(9)
            call LauraOutfit(Changed=1)
    elif "no comfy" in L_RecentActions:
            pass        
    elif (2 * L_Inbt) >= (L_Love + L_Obed +100):
            # if her inhibition is much higher than her obedience to you. . .            
            ch_l "One minute. . ."
            ch_l "I'm getting a bit more comfortable."
            call L_AltClothes(9)
            call LauraOutfit(Changed=1)
            $ L_RecentActions.append("comfy")
    else:           
            ch_l "One minute. . ."
            menu: 
                ch_l "I could throw on something a bit more fun. . ."
                "Sure.":
                    ch_l "Cool. . ."
                    call L_AltClothes(9)
                    call LauraOutfit(Changed=1)
                    $ L_RecentActions.append("comfy")
                "No thanks.":
                    ch_l "Oh, ok."       
                    $ L_RecentActions.append("no comfy")             
    return

label Laura_Custom_Out(Custom = 3, Shame = 0, Agree = 1):
            #If Custom1 = 3, if custom2 = 5, if custom3 = 6
            
            call LauraFace("sexy", 1)
            if "exhibitionist" in L_Traits:  
                        ch_l "Mmmmmm. . ."  
                        if Custom == 5 and L_Custom2[0] == 2:
                            $ L_Outfit = "custom2"                    
                            $ L_Shame = L_OutfitShame[5]
                        elif Custom == 15 and L_Custom4[0] == 2:
                                    $ L_Outfit = "custom4"
                                    $ L_Shame = L_OutfitShame[Custom]
                        elif Custom == 16 and L_Custom5[0] == 2:
                                    $ L_Outfit = "custom5"
                                    $ L_Shame = L_OutfitShame[Custom]
                        elif Custom == 17 and L_Custom6[0] == 2:
                                    $ L_Outfit = "custom6"
                                    $ L_Shame = L_OutfitShame[Custom]
                        elif Custom == 18 and L_Custom7[0] == 2:
                                    $ L_Outfit = "custom7"
                                    $ L_Shame = L_OutfitShame[Custom]
                        elif Custom == 19 and L_Custom8[0] == 2:
                                    $ L_Outfit = "custom8"
                                    $ L_Shame = L_OutfitShame[Custom]
                        elif Custom == 20 and L_Custom9[0] == 2:
                                    $ L_Outfit = "custom9"
                                    $ L_Shame = L_OutfitShame[Custom]
                        elif Custom == 6 and L_Custom3[0] == 2:
                            $ L_Outfit = "custom3"                    
                            $ L_Shame = L_OutfitShame[6]
                        else: #if custom 1:
                            $ L_Outfit = "custom1"                    
                            $ L_Shame = L_OutfitShame[3]            
                        return    
            
            if Custom == 5 and L_Custom2[0] == 2:
                        $ L_Outfit = "custom2"   
            elif Custom == 15 and L_Custom4[0] == 2:
                        $ L_Outfit = "custom4"
            elif Custom == 16 and L_Custom5[0] == 2:
                        $ L_Outfit = "custom5"
            elif Custom == 17 and L_Custom6[0] == 2:
                        $ L_Outfit = "custom6"
            elif Custom == 18 and L_Custom7[0] == 2:
                        $ L_Outfit = "custom7"
            elif Custom == 19 and L_Custom8[0] == 2:
                        $ L_Outfit = "custom8"
            elif Custom == 20 and L_Custom9[0] == 2:
                        $ L_Outfit = "custom9"
            elif Custom == 6 and L_Custom3[0] == 2:
                        $ L_Outfit = "custom3"   
            elif L_Custom[0] == 2: #if custom 1:
                        $ L_Outfit = "custom1"   
            else: #no
                        $ Agree = 0
             
            if Agree:                              
                        #she's decided to wear this out.
                        $ L_Shame = L_OutfitShame[Custom]          
                        if L_OutfitShame[Custom] >= 50:
                            ch_l "This is. . . really brave. . ."
                        elif L_OutfitShame[Custom] >= 25:
                            ch_l "This one's pretty skimpy. . ."
                        elif L_OutfitShame[Custom] >= 15:
                            call LauraFace("bemused", 1)
                            ch_l "Yeah, ok. . ."
                        else:
                            ch_l "Yup."
            else:
                        #She's decided not to wear this out
                        if L_OutfitShame[Custom] >= 50:
                            call LauraFace("angry", 1)
                            ch_l "Perv."
                        elif L_OutfitShame[Custom] >= 25:
                            call LauraFace("angry", 1)
                            ch_l "Yeah, not in public."
                        else:
                            call LauraFace("surprised", 1)
                            ch_l "Nah."  
            return
# End Laura Custom Out
                                
                                
label Laura_OutfitShame(Custom = 3, Check = 0, Count = 0, Tempshame = 50, Agree = 1):                                                                             #sets custom outfit    
            #Custom determines which custom outfit is being checked against.    
            #If Custom1 = 3, if custom2 = 5, if custom3 = 6, if gym = 7, if private = 9, if swimsuit = 10
            #if not a check, then it is only applied if it's in a taboo area
            # Tempshame is a throwaway value, 0-50, Agree is whether she will wear it out, 2 if yes, 1 if only around you.
            
            if not Check and not Taboo and Custom != 20:
                #if this is not a custom check and you're in a safe space,
                if L_Schedule[9]:
                    #if there is a "private outfit" set, ask to change.
                    call L_Private_Outfit
                return
                        
            #If she's wearing a bra of some kind
            if Custom == 20 and L_Uptop: 
                $ Count = 0
            elif L_Chest == "leather bra":  
                $ Count = 20
#            elif L_Chest == "sports bra":
#                $ Count = 15
            elif L_Chest == "bikini top":
                $ Count = 15
            elif L_Chest == "wolvie top":
                $ Count = 10   
            elif L_Chest == "corset":
                $ Count = 5
            else:     #L_Chest == 0
                if L_Pierce:
                    $ Count = -5
                else:
                    $ Count = 0
                    
            #If she's wearing an overshirt
            if Custom == 20 and L_Uptop: 
                $ Count = 0
            elif L_Over == "jacket":                                             
                $ Count += 10
#            elif L_Over == "red shirt":      
#                $ Count += 20
            elif L_Over == "towel":      
                $ Count += 10
            #else: nothing    
            
            call LauraFace("sexy", 0)
            if Custom == 9:
                pass
            elif Count >= 20:
                $ Count = 20
                if Check:
                    ch_l "This top works."
            elif not Check:
                pass
            elif Count >= 10 and (ApprovalCheck("Laura", 1200, TabM=0) or ApprovalCheck("Laura", 500, "I", TabM=0)):  
                ch_l "This top works."     
            elif Count >= 10:
                ch_l "The top's not really a good look."
            elif Count >= 5 and (ApprovalCheck("Laura", 2300, TabM=0) or ApprovalCheck("Laura", 800, "I", TabM=0)):  
                ch_l "I don't know, the top's a little light."
            elif Count >= 5:        
                call LauraFace("startled", 1)
                ch_l "I can't really wear this top out."
            elif (ApprovalCheck("Laura", 2700, TabM=0) or ApprovalCheck("Laura", 950, "I", TabM=0)):  
                ch_l ". . ."        
            else:
                call LauraFace("bemused", 1)
                ch_l "I wouldn't go out with my tits out."
             
            $ Tempshame -= Count                  #Set Outfit shame for the upper half    
            $ Count = 0         
            
            if L_Legs and L_Panties and L_Legs != "mesh pants": 
                        $ Count = 30               
            else: #If she's missing something on her legs    
                        if PantsNum("Laura") >= 5:               #If wearing pants commando
                            $ Count = 25                            
#                        elif L_Legs == "shorts":                #If wearing shorts
#                            $ Count = 20  
                        elif L_Legs == "skirt":                 #If wearing a skirt commando
                            $ Count = 20     
                        elif L_Panties == "bikini bottoms":       #If wearing only bikini bottoms
                            $ Count = 15   
                        elif L_Panties == "wolvie panties":      #If wearing only wolvie panties
                            $ Count = 10
                        elif L_Panties == "lace panties":       #If wearing only lace panties
                            $ Count = 5
                        elif L_Panties:                         #If wearing only any other panties
                            $ Count = 7
                        #else: 0
                        
                        if L_Legs == "mesh pants":
                            $ Count += 5
                        
                        if HoseNum("Laura") >= 10:
                            $ Count = 25 if Count < 25 else Count
                            
                        if L_Over == "towel" and Count:         #If wearing a Towel and anything else
                            $ Count = 25
                        elif L_Over == "towel":                 #If just wearing a Towel
                            $ Count = 15   
                            
            if not Check:
                        #If this isn't a custom check, skip this dialog stuff
                        pass
            elif Custom == 9:
                        pass
            elif Count >= 20:
                        if PantsNum("Laura") >= 5:
                            ch_l "and these pants work."
                        elif HoseNum("Laura") >= 10:
                            ch_l "and these [L_Hose] will work fine."
                        elif L_Over == "towel":
                            ch_l "The towel's an odd choice. . ."
                        else:
                            ch_l "but there's a draft."
                        if not L_Panties and ApprovalCheck("Laura", 500, "I", TabM=0):
                            ch_l "Commando's cool."           
                        elif not L_Panties:
                            ch_l "I might accidentally flash some people like this though."
                    
            elif Count >= 10 and (ApprovalCheck("Laura", 2000, TabM=0) or ApprovalCheck("Laura", 700, "I", TabM=0)):
                    ch_l "I don't think I'm fully covered. . ."        
            elif Count >= 10:
                    call LauraFace("angry", 1)
                    ch_l "I'm not covered like this. . ."                
            elif (ApprovalCheck("Laura", 2500, TabM=0) or ApprovalCheck("Laura", 800, "I", TabM=0)):  
                    ch_l "It's pretty minimal. . ."        
            else:
                    ch_l "I wouldn't show off my cooch either. . ."
                
            $ Tempshame -= Count                  #Set Outfit shame for the lower half
            
            if Check:
                    #if this is a custom outfit check
                    if Custom == 7:
                        ch_p "So would you work out in that?"
                    elif Custom == 9:
                        ch_p "So would you sleep in that?"
                    else:
                        ch_p "So would you wear that outside?"  
                        
                    call LauraFace("sexy", 0)
                    if Taboo >= 40: #L_Loc != "bg player" and L_Loc != "bg laura": 
                        call LauraFace("confused",1)
                        $ L_Mouth = "smile"
                        ch_l "Well a bit late for that, I guess." 
                    elif "exhibitionist" in L_Traits and Tempshame <= 20: 
                        call Statup("Laura", "Lust", 80, 10) 
                        call LauraFace("sexy", 2)      
                        ch_l ". . ."
                        call LauraFace("sexy", 1)      
                    elif Tempshame <= 5:
                        call LauraFace("smile")
                        ch_l "I don't see why not."
                    elif Tempshame <= 15 and (ApprovalCheck("Laura", 1700, TabM=0, C = 0) or ApprovalCheck("Laura", 400, "I", TabM=0, C = 0)):        
                        ch_l "It looks good, right?"
                    elif Custom == 9:
                        #if it's sleepwear      
                        call LauraFace("bemused", 1)
                        if Tempshame >= 30:
                            ch_l "Sure, perv."   
                        elif Tempshame >= 15:
                            ch_l "Sure, why not."  
                        else:
                            ch_l "Yeah, I guess."                       
                    elif Tempshame <= 15:  
                        call LauraFace("bemused", 1)
                        ch_l "I can't move freely in this without showing off the goods."
                        $ Agree = 0
                    elif Custom == 10 and Tempshame <= 20:  
                        #if it's a swimsuit. . .
                        call LauraFace("bemused", 1)
                        ch_l "Yeah, I can swim in this. . ."
                    elif Tempshame <= 25 and (ApprovalCheck("Laura", 2300, TabM=0, C = 0) or ApprovalCheck("Laura", 700, "I", TabM=0, C = 0)):
                        ch_l "I can handle this."
                    elif Tempshame <= 25:
                        call LauraFace("angry", 1)
                        ch_l "Nah, too slutty."
                        $ Agree = 0
                    elif (ApprovalCheck("Laura", 2500, TabM=0, C = 0) or ApprovalCheck("Laura", 800, "I", TabM=0, C = 0)):
                        call LauraFace("bemused", 1)
                        ch_l "Pretty daring, eh?"
                    else:
                        call LauraFace("angry", 1)
                        ch_l "As if."
                        $ Agree = 0
                        
                    $ L_OutfitShame[Custom] = Tempshame                     
                    if Custom == 5:
                            $ L_Custom2[1] = L_Arms  
                            $ L_Custom2[2] = L_Legs 
                            $ L_Custom2[3] = L_Over
                            $ L_Custom2[4] = L_Neck 
                            $ L_Custom2[5] = L_Chest 
                            $ L_Custom2[6] = L_Panties
                            $ L_Custom2[8] = L_Hair
                            $ L_Custom2[9] = L_Hose
                            $ L_Custom2[0] = 2 if Agree else 1  
                            call Clothing_Schedule_Check("Laura",5,1)           
#MOD CUSTOM OUTFITS OUTFITSHAME
                    elif Custom == 20:
                            $ L_Custom9[1] = L_Arms  
                            $ L_Custom9[2] = L_Legs 
                            $ L_Custom9[3] = L_Over
                            $ L_Custom9[4] = L_Neck 
                            $ L_Custom9[5] = L_Chest 
                            $ L_Custom9[6] = L_Panties
                            $ L_Custom9[8] = L_Hair
                            $ L_Custom9[9] = L_Hose
                            $ L_Custom9[0] = 2 if Agree else 1
                            call Clothing_Schedule_Check("Laura",Custom,1)  
                    elif Custom == 19:
                            $ L_Custom8[1] = L_Arms  
                            $ L_Custom8[2] = L_Legs 
                            $ L_Custom8[3] = L_Over
                            $ L_Custom8[4] = L_Neck 
                            $ L_Custom8[5] = L_Chest 
                            $ L_Custom8[6] = L_Panties
                            $ L_Custom8[8] = L_Hair
                            $ L_Custom8[9] = L_Hose
                            $ L_Custom8[0] = 2 if Agree else 1
                            call Clothing_Schedule_Check("Laura",Custom,1)  
                    elif Custom == 18:
                            $ L_Custom7[1] = L_Arms  
                            $ L_Custom7[2] = L_Legs 
                            $ L_Custom7[3] = L_Over
                            $ L_Custom7[4] = L_Neck 
                            $ L_Custom7[5] = L_Chest 
                            $ L_Custom7[6] = L_Panties
                            $ L_Custom7[8] = L_Hair
                            $ L_Custom7[9] = L_Hose
                            $ L_Custom7[0] = 2 if Agree else 1
                            call Clothing_Schedule_Check("Laura",Custom,1)  
                    elif Custom == 17:
                            $ L_Custom6[1] = L_Arms  
                            $ L_Custom6[2] = L_Legs 
                            $ L_Custom6[3] = L_Over
                            $ L_Custom6[4] = L_Neck 
                            $ L_Custom6[5] = L_Chest 
                            $ L_Custom6[6] = L_Panties
                            $ L_Custom6[8] = L_Hair
                            $ L_Custom6[9] = L_Hose
                            $ L_Custom6[0] = 2 if Agree else 1
                            call Clothing_Schedule_Check("Laura",Custom,1)  
                    elif Custom == 16:
                            $ L_Custom5[1] = L_Arms  
                            $ L_Custom5[2] = L_Legs 
                            $ L_Custom5[3] = L_Over
                            $ L_Custom5[4] = L_Neck 
                            $ L_Custom5[5] = L_Chest 
                            $ L_Custom5[6] = L_Panties
                            $ L_Custom5[8] = L_Hair
                            $ L_Custom5[9] = L_Hose
                            $ L_Custom5[0] = 2 if Agree else 1
                            call Clothing_Schedule_Check("Laura",Custom,1)  
                    elif Custom == 15:
                            $ L_Custom4[1] = L_Arms  
                            $ L_Custom4[2] = L_Legs 
                            $ L_Custom4[3] = L_Over
                            $ L_Custom4[4] = L_Neck 
                            $ L_Custom4[5] = L_Chest 
                            $ L_Custom4[6] = L_Panties
                            $ L_Custom4[8] = L_Hair
                            $ L_Custom4[9] = L_Hose
                            $ L_Custom4[0] = 2 if Agree else 1
                            call Clothing_Schedule_Check("Laura",Custom,1)  
                    elif Custom == 6:
                            $ L_Custom3[1] = L_Arms  
                            $ L_Custom3[2] = L_Legs 
                            $ L_Custom3[3] = L_Over
                            $ L_Custom3[4] = L_Neck 
                            $ L_Custom3[5] = L_Chest 
                            $ L_Custom3[6] = L_Panties
                            $ L_Custom3[8] = L_Hair
                            $ L_Custom3[9] = L_Hose
                            $ L_Custom3[0] = 2 if Agree else 1
                            call Clothing_Schedule_Check("Laura",6,1)  
                    elif Custom == 7 and Agree:
                            $ L_Gym[1] = L_Arms  
                            $ L_Gym[2] = L_Legs 
                            $ L_Gym[3] = L_Over
                            $ L_Gym[4] = L_Neck 
                            $ L_Gym[5] = L_Chest 
                            $ L_Gym[6] = L_Panties
                            $ L_Gym[8] = L_Hair
                            $ L_Gym[9] = L_Hose
                            $ L_Gym[0] = 2   
                            call Clothing_Schedule_Check("Laura",4,1)  
                    elif Custom == 9:                            
                            $ L_Sleepwear[1] = L_Arms  
                            $ L_Sleepwear[2] = L_Legs 
                            $ L_Sleepwear[3] = L_Over
                            $ L_Sleepwear[4] = L_Neck 
                            $ L_Sleepwear[5] = L_Chest 
                            $ L_Sleepwear[6] = L_Panties
                            $ L_Sleepwear[8] = L_Hair
                            $ L_Sleepwear[9] = L_Hose
                            $ L_Sleepwear[0] = 2 if Agree else 1   
                    elif Custom == 10:            
                            $ L_Swim[1] = L_Arms  
                            $ L_Swim[2] = L_Legs 
                            $ L_Swim[3] = L_Over
                            $ L_Swim[4] = L_Neck 
                            $ L_Swim[5] = L_Chest 
                            $ L_Swim[6] = L_Panties
                            $ L_Swim[8] = L_Hair
                            $ L_Swim[9] = L_Hose
                            $ L_Swim[0] = 2 if Agree else 1
                    else: #Typically Custom == 3
                            $ L_Custom[1] = L_Arms  
                            $ L_Custom[2] = L_Legs 
                            $ L_Custom[3] = L_Over
                            $ L_Custom[4] = L_Neck 
                            $ L_Custom[5] = L_Chest 
                            $ L_Custom[6] = L_Panties
                            $ L_Custom[8] = L_Hair
                            $ L_Custom[9] = L_Hose
                            $ L_Custom[0] = 2 if Agree else 1
                            call Clothing_Schedule_Check("Laura",3,1)   
                    #End check                       
            elif Taboo <= 20:
                # halves shame level if she's comfortable
                $ Tempshame /= 2
                
            $ L_Shame = Tempshame
            
            if Custom == 20:
                # This returns the scene if it's a check Shame adjustment
                return
                
            if Check:
                    pass
            elif "exhibitionist" in L_Traits: 
                    #If she's an exhibitionist
                    pass
            elif Tempshame <= 5:
                    #If the outfit is very tame
                    pass
            elif L_Over == "towel" and L_Loc == "bg showerroom": 
                    #If she's in a towel but it's appropriate
                    pass
            elif Tempshame <= 15 and (ApprovalCheck("Laura", 1700) or ApprovalCheck("Laura", 600, "I")):
                    #If the outfit is hot but she's ok     
                    pass
            elif Tempshame <= 20 and L_Loc == "bg dangerroom": 
                    #If the outfit is light but she's in the gym
                    pass
            elif Tempshame <= 20 and (ApprovalCheck("Laura", 1800) or ApprovalCheck("Laura", 650, "I")):
                    #If the outfit is sexy but she's cool with that
                    pass
            elif Tempshame <= 25 and (ApprovalCheck("Laura", 2300) or ApprovalCheck("Laura", 800, "I")):
                    #If the outfit is sexy but she's cool with that
                    pass
            elif (ApprovalCheck("Laura", 2600) or ApprovalCheck("Laura", 950, "I")):
                    #If the outfit is very scandelous but she's ok with that      
                    pass
            elif Custom == 9 and not Taboo:
                    pass
            else:
                    ch_l "One sec, I gotta change real quick."
                    $ L_Outfit = renpy.random.choice(["mission", "streets"])
                    $ L_Water = 0
                    call LauraOutfit(Changed = 1) 
                    ch_l "That's not really outdoors wear."
                    
            return        

#End Laura Custom clothes check.
    
# start laura hungry //////////////////////////////////////////////////////////
label Laura_Hungry:
    if L_Chat[3]:
        ch_l "[[licks her lips] I'm a little thirsty. . ."
    elif L_Chat[2]:
        ch_l "I really enjoy that serum you whipped up."
    else:
        ch_l "[[licks her lips] I'm a little thirsty. . ."
    $ L_Traits.append("hungry")
return


# end laura hungry //////////////////////////////////////////////////////////

    
# Start Laura first Les / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Laura_First_Les(Silent = 0, Undress = 0, GirlsNum = 0): #checked when she engages in a les scene  ## call Laura_First_Les(0,1)
    if L_Les:
        return
    
    $ L_Les += 1
    $ L_RecentActions.append("lesbian")        
    call Statup("Laura", "Inbt", 30, 2) 
    call Statup("Laura", "Inbt", 90, 1)
    
    if not Silent: 
        #example previous line: Line + " and cups " + Primary + "'s breasts in her delicate hands" 
        "Laura's head jerks up and she looks at what [Partner] is doing. [Partner] pauses and glances up at her with a mischievous grin." 
        ch_l "I, um, I haven't done that sort of thing before."
        if Partner == "Rogue":
                if R_Les:
                    ch_r "Neither have I Sugar, but it seemed like fun."
                else:
                    ch_r "It's all right Sugar, I'll take care of you."
        if L_LikeRogue >= 60 and ApprovalCheck("Laura", (1500-(10*L_Les)-(10*(L_LikeRogue-60)))): #If she likes both of you a lot, threeway
                $ State = "threeway"
        elif ApprovalCheck("Laura", 1000): #If she likes you well enough, Hetero
                $ State = "hetero"            
        elif L_LikeRogue >= 70: #if she doesn't like you but likes Rogue, lesbian
                $ State = "lesbian"
        
        
        
        
        
        if "cockout" in P_RecentActions:
                call LauraFace("down", 2)  
                if GirlsNum:
                    "Laura also glances down at your cock"
                else:
                    "Laura glances down at your exposed cock"
        elif Undress:
                "You strip nude."
        else:
                "You whip your cock out."
        $ P_RecentActions.append("cockout") 
        
        if Taboo and not ApprovalCheck("Laura", 1500):
                call LauraFace("surprised", 2)  
                ch_l "Um, you should[L_like]put that away in public."
                call LauraFace("bemused", 1)  
                if L_SeenPeen == 1: 
                    ch_l "Or[L_like]maybe. . ."
                    call Statup("Laura", "Love", 90, 15)                
                    call Statup("Laura", "Obed", 50, 20)
                    call Statup("Laura", "Inbt", 60, 35)  
                    
        elif L_SeenPeen > 10:
                return    
        elif ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "L"):
                call LauraFace("sly",1) 
                if L_SeenPeen == 1: 
                    call LauraFace("surprised",2)  
                    ch_l "That's. . . impressive."
                    call LauraFace("bemused",1)  
                    call Statup("Laura", "Love", 90, 3) 
                elif L_SeenPeen == 2:  
                    ch_l "I can't get over that."               
                    call Statup("Laura", "Obed", 50, 7) 
                elif L_SeenPeen == 5: 
                    ch_l "There it is."
                    call Statup("Laura", "Inbt", 60, 5)  
                elif L_SeenPeen == 10: 
                    ch_l "So beautiful."
                    call Statup("Laura", "Obed", 80, 10)
                    call Statup("Laura", "Inbt", 60, 3)  
        else:
                call LauraFace("sad",1) 
                if L_SeenPeen == 1: 
                    call LauraFace("perplexed",1 ) 
                    ch_l "Well that happened. . ."
                    call Statup("Laura", "Obed", 50, 7)
                    call Statup("Laura", "Inbt", 60, 3)  
                elif L_SeenPeen < 5: 
                    call LauraFace("sad",0) 
                    ch_l "Huh."
                    call Statup("Laura", "Inbt", 60, 2)  
                elif L_SeenPeen == 10: 
                    ch_l "[L_Like]put that away."               
                    call Statup("Laura", "Obed", 50, 7)
                    call Statup("Laura", "Inbt", 60, 3)  
    
    else: #Silent mode
                $ P_RecentActions.append("cockout") 
                if L_SeenPeen > 10:
                    return
                elif ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "L"):
                        if L_SeenPeen == 1: 
                            call Statup("Laura", "Love", 90, 3) 
                        elif L_SeenPeen == 2:              
                            call Statup("Laura", "Obed", 50, 7) 
                        elif L_SeenPeen == 5: 
                            call Statup("Laura", "Inbt", 60, 5)  
                        elif L_SeenPeen == 10: 
                            call Statup("Laura", "Love", 90, 10)  
                else:
                        if L_SeenPeen == 1: 
                            call Statup("Laura", "Obed", 50, 7)
                            call Statup("Laura", "Inbt", 60, 3)  
                        elif L_SeenPeen < 5: 
                            call Statup("Laura", "Inbt", 60, 2)  
                        elif L_SeenPeen == 10:              
                            call Statup("Laura", "Obed", 50, 7)
                            call Statup("Laura", "Inbt", 60, 3) 
                            
    if L_SeenPeen == 1:            
        call Statup("Laura", "Love", 90, 10)                
        call Statup("Laura", "Obed", 90, 25)
        call Statup("Laura", "Inbt", 60, 20) 
        call Statup("Laura", "Lust", 200, 5)
    
    return
# End Laura first Les / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /   
    