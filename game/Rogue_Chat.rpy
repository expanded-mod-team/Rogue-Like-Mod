﻿# star Rogue chat interface
label Rogue_Chat_Set(Preset=0):    
    if "Rogue" not in Digits and R_Loc != bg_current and "Rogue" not in Nearby:
            "You don't have her number."
            return
            
    if Preset:   
            ch_p "Hey, Rogue. . ."
            call Shift_Focus("Rogue")
            if R_Loc != bg_current:
                        show Cellphone at SpriteLoc(StageLeft)
            else:
                        hide Cellphone
            if Preset == "chat":
                    $ renpy.pop_call() #removes the call to chat subroutine
                    $ renpy.pop_call() #This removes the callback to the previous chat session
            elif Preset == "settings":
                    $ renpy.pop_call() #This removes the callback to the previous chat session
                    $ renpy.pop_call() #this removes the callback to the previous settings menu
                    call Rogue_Settings   
            elif Preset == "wardrobe":
                    $ renpy.pop_call() #This removes the callback to the previous chat session
                    $ renpy.pop_call() #this removes the callback to the previous settings menu
                    $ renpy.pop_call() #this removes the callback to the previous settings menu testing. . .
                    ch_p "I wanted to talk about your outfit. . ."
                    call Taboo_Level
                    if R_Taboo:
                            if "exhibitionist" in R_Traits:
                                ch_r "Oooh, naughty. . ."  
                            elif ApprovalCheck("Rogue", 900, TabM=4) or ApprovalCheck("Rogue", 400, "I", TabM=3): 
                                ch_r "Well, I mean, it's pretty public here, but I guess I could. . ."
                            else:
                                ch_r "This is a pretty public place for that, don't you think?"
                                ch_r "We can talk about that back in our rooms."
                                jump Rogue_Chat
                            call Rogue_Clothes
                    elif ApprovalCheck("Rogue", 600, "L") or ApprovalCheck("Rogue", 300, "O"):
                        ch_r "Ok, what did you want?"
                        call Rogue_Clothes
                    else:
                        ch_r "Well I'm not really interested in your fashion opinions." 
            #end preset menu
            
label Rogue_Chat:
    call RogueFace      
    call Shift_Focus("Rogue")
    if R_Loc != bg_current:
                show Cellphone at SpriteLoc(StageLeft)
    else:
                hide Cellphone
    
    if "caught" in R_RecentActions:
                ch_r "We should probably keep our distance for now."
                return
    if "angry" in R_RecentActions:
                ch_r "I really don't want to talk to you right now."
                return
    if "les" in R_RecentActions:
            #if she's with a girl. . .
            ch_r "Ooof. . . gimme a minute. . ."
            "You hear some shifting around. . ."
            ch_r "Ok, just um, never mind. . ."
            "You hear some muffled giggles in the background."
    menu:
        ch_r "So what did you want to talk about, [R_Petname]?"
        "Come on over." if R_Loc != bg_current:
                    if "Rogue" in Nearby and bg_current != "bg showerrroom":
                        call Swap_Nearby("Rogue")
                    elif Room_Full():
                        "It's already pretty crowded here."
                        call Dismissed
                    else:
                        call Rogue_Summon  
        "Ask Rogue to leave" if R_Loc == bg_current:
                    call Rogue_Dismissed   
                    return
        "Romance her":      
                menu:
                    "Flirt with her (locked)" if R_Chat[5]:  
                                pass
                    "Flirt with her" if not R_Chat[5]:
                                call Rogue_Flirt    
                        
                    "Sex Menu (locked)" if R_Loc != bg_current:
                                pass
                    "Sex Menu" if R_Loc == bg_current:
                                if R_Love >= R_Obed:
                                    ch_p "Did you want to fool around?"
                                else:
                                    ch_p "I'd like to get naughty."
                                if "angry" in R_RecentActions:  
                                    ch_r "I don't want to deal with you right now."
                                elif ApprovalCheck("Rogue", 600, "LI"):
                                    call RogueFace("sexy")
                                    ch_r "Heh, all right, [R_Petname]."
                                    call Rogue_SexMenu
                                    return
                                elif ApprovalCheck("Rogue", 400, "OI"):
                                    ch_r "If that's what you want, [R_Petname]."
                                    call Rogue_SexMenu
                                    return
                                else:
                                    ch_r "I'm not really interested, [R_Petname]." 
                               
                    "Dirty Talk (locked)" if R_SEXP < 10:
                                pass
                    "Dirty Talk" if R_SEXP >= 10:
                                ch_p "About when we get together. . ."
                                call Rogue_SexChat
                    "Date":
                                ch_p "Do you want to go on a date tonight?"
                                call Rogue_Date_Ask          
                    "Gifts (locked)" if R_Loc != bg_current:
                                pass
                    "Gifts" if R_Loc == bg_current:
                                ch_p "I'd like to give you something."
                                call Rogue_Gifts
                    "Back":
                                pass        
                                          
        "Talk with her": 
                menu:
                    "I just wanted to talk. . .":
                                call Rogue_Chitchat   
                    "Relationship status":
                                ch_p "Could we talk about us?"
                                if R_Loc == bg_current:
                                    call Rogue_Relationship
                                else:
                                    ch_r "That sounds like it might be a little heavy to do over the phone."
                                    ch_r "Maybe later?"
                          
                    "Other girls":
                                menu:
                                    "How do you feel about Kitty?" if "met" in K_History:
                                            call Rogue_About("Kitty")
                                    "How do you feel about Emma?" if "met" in E_History:
                                            call Rogue_About("Emma")
                                    "How do you feel about Laura?" if "met" in L_History:
                                            call Rogue_About("Laura")
                                    "About hooking up with other girls. . .":
                                            call Rogue_Monogamy
                                    "Never mind.":
                                            pass
                                            
                    "Could I get your number?" if "Rogue" not in Digits:
                                if ApprovalCheck("Rogue", 400, "L") or ApprovalCheck("Rogue", 200, "I"):
                                    ch_r "Sure, I suppose."
                                    $ Digits.append("Rogue") 
                                elif ApprovalCheck("Rogue", 200, "O"):
                                    ch_r "If you want it, I guess."             
                                    $ Digits.append("Rogue")
                                else:
                                    ch_r "I don't really want you calling me."                     
                                
                    "Back":
                                pass
                    
        "Change Rogue":
                    call Rogue_Settings   
         
        "Add her to party" if "Rogue" not in Party and R_Loc == bg_current:
                    ch_p "Could you follow me for a bit?"
                    if ApprovalCheck("Rogue", 550):
                        $ Party.append("Rogue")
                        ch_r "Ok, Where did you want to go?"
                        return
                    elif not ApprovalCheck("Rogue", 300):
                        ch_r "Um, no thanks."
                    else:
                        ch_r "I'm fine here, thanks."
        "Disband party" if "Rogue" in Party: 
                    ch_p "Ok, you can leave if you prefer."
                    $ Party.remove("Rogue")       
                    call Rogue_Schedule(0)         
                    if "leaving" in R_RecentActions:
                        call DrainWord("Rogue","leaving")
                    if R_Loc == bg_current:
                        ch_r "Ok, I'll probably stick around for a bit anyway."
                    else:
                        ch_r "Ok, see you later then."
                        call Set_The_Scene   
                    return
                
        "Switch to. . .":
                menu:
                    "Kitty":
                        call Chat("Kitty")          
                    "Emma":
                        call Chat("Emma")       
                    "Laura":
                        call Chat("Laura")
                    "Never mind":
                        pass
                        
        "Never mind.":
                    ch_r "Ok, later then."
                    return
    jump Rogue_Chat


#Rogue Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  

label Rogue_Relationship:
    while True:
        menu:
            ch_r "What did you want to ask me about?"
            
            "Do you want to be my girlfriend?" if "dating" not in R_Traits and "ex" not in R_Traits:
                    if "asked boyfriend" in R_DailyActions and "angry" in R_DailyActions:
                        call RogueFace("angry", 1)
                        ch_r "Seriously, stop bugging me."
                        return
                    elif "asked boyfriend" in R_DailyActions:
                        call RogueFace("angry", 1)
                        ch_r "You already asked about that, the answer's still no."
                        return
                    elif R_Break[0]:                    
                        call RogueFace("angry", 1)                    
                        ch_r "I already told you, not while you're with her."
                        if "dating" in K_Traits:   
                            $ R_DailyActions.append("asked boyfriend")                     
                            return
                        elif "ex" in K_Traits:
                            ch_p "I'm not anymore."
                         
                    $ R_DailyActions.append("asked boyfriend")
                    
                    if P_Harem and "RogueYes" not in P_Traits: 
                        if len(P_Harem) >= 2:
                            ch_r "That wouldn't be fair to the others, [R_Petname]."
                        else:
                            ch_r "That wouldn't be fair to [P_Harem[0]], [R_Petname]."
                        return                    
                    
                    if R_Event[5]:
                        call RogueFace("bemused", 1)
                        ch_r "I mean, I asked you about this before. . ."
                    else:
                        call RogueFace("surprised", 2)
                        ch_r "Wow, this is unexpected, [R_Petname]. . ." 
                        call RogueFace("smile", 1)
                    
                    call Rogue_OtherWoman
                    
                    if R_Love >= 800:
                        call RogueFace("surprised", 1)
                        $ R_Mouth = "grimace"
                        call Statup("Rogue", "Love", 200, 40)
                        ch_r "I'd love to!"
                        if "boyfriend" not in R_Petnames:
                            $ R_Petnames.append("boyfriend")                
                        $ R_Traits.append("dating")
                        if "RogueYes" in P_Traits:       
                                    $ P_Traits.remove("RogueYes")
                                    $ P_Harem.append("Rogue")
                                    call Harem_Initiation
                        "Rogue leaps in and kisses you deeply."
                        call RogueFace("kiss", 1) 
                        $ R_Kissed += 1
                    elif R_Obed >= 500:
                        call RogueFace("perplexed")
                        ch_r "I'm not sure I'd call what we have \"dating.\""
                    elif R_Inbt >= 500:
                        call RogueFace("smile")                
                        ch_r "I don't really want to be tied down like that."
                    else:
                        call RogueFace("perplexed", 1)
                        ch_r "I don't really feel that way about you right now, [R_Petname]."
                
            
            "Do you want to get back together?" if "ex" in R_Traits:
                    if "asked boyfriend" in R_DailyActions and "angry" in R_DailyActions:
                        call RogueFace("angry", 1)
                        ch_r "Seriously, stop bugging me."
                        return
                    elif "asked boyfriend" in R_DailyActions:
                        call RogueFace("angry", 1)
                        ch_r "You already asked about that, the answer's still no."
                        return
                    elif R_Break[0]: 
                        call RogueFace("angry", 1)                    
                        if "dating" in K_Traits:   
                            ch_r "I alredy told you, not while you're with her."
                            return
                        elif "ex" in K_Traits:
                            ch_r "I alredy told you, not while you're with her."
                            ch_p "I'm not anymore."
                            $ R_Break[0] = 0
                        else:    
                            if not ApprovalCheck("Rogue", 1500) or R_Break[1] > 5:
                                ch_r "We are never, ever, ever getting back together."
                            else:
                                call RogueFace("sad", 1)
                                ch_r "Sorry, it's just still too fresh. I can't even think of getting back together yet."
                        $ R_DailyActions.append("asked boyfriend")
                        return
                    
                    $ R_DailyActions.append("asked boyfriend")
                    
                    if P_Harem and "RogueYes" not in P_Traits: 
                        if len(P_Harem) >= 2:
                            ch_r "That wouldn't be fair to the others, [R_Petname]."
                        else:
                            ch_r "That wouldn't be fair to [P_Harem[0]], [R_Petname]."
                        return
                    
                    $ Cnt = 0
                    call Rogue_OtherWoman
                                            
                    if R_Love >= 800:
                        call RogueFace("surprised", 1)
                        $ R_Mouth = "grimace"
                        call Statup("Rogue", "Love", 90, 5)
                        ch_r "If you're in, I'm in!"
                        if "boyfriend" not in R_Petnames:
                            $ R_Petnames.append("boyfriend")                
                        $ R_Traits.append("dating")          
                        $ R_Traits.remove("ex")
                        if "RogueYes" in P_Traits:       
                                    $ P_Traits.remove("RogueYes")
                                    $ P_Harem.append("Rogue")
                                    call Harem_Initiation
                        "Rogue leaps in and kisses you deeply."
                        call RogueFace("kiss", 1) 
                        $ R_Kissed += 1
                    elif R_Love >= 600 and ApprovalCheck("Rogue", 1500):
                        call RogueFace("smile", 1)
                        $ R_Mouth = "grimace"
                        call Statup("Rogue", "Love", 90, 5)
                        ch_r "We can give this another try."
                        if "boyfriend" not in R_Petnames:
                            $ R_Petnames.append("boyfriend")                
                        $ R_Traits.append("dating")             
                        $ R_Traits.remove("ex")
                        if "RogueYes" in P_Traits:       
                                    $ P_Traits.remove("RogueYes")
                                    $ P_Harem.append("Rogue")
                                    call Harem_Initiation
                        "Rogue gives you a quick kiss."
                        call RogueFace("kiss", 1) 
                        $ R_Kissed += 1
                    elif R_Obed >= 500:
                        call RogueFace("sad")
                        ch_r "Whatever we had, whatever we have right now, that's not it."
                    elif R_Inbt >= 500:
                        call RogueFace("perplexed")                
                        ch_r "We tried that, it didn't work out."
                    else:
                        call RogueFace("perplexed", 1)
                        ch_r "I'm not ready for more heartbreak, [R_Petname]."
                    
                    # End Back Together
                        
            "I wanted to ask about [[another girl]" if "Rogue" in P_Harem:
                    menu:
                        "Have you reconsidered letting me date. . ."
                        "Kitty" if "Kitty" not in P_Harem and "met" in K_History:
                                call Poly_Start("Kitty",1)
                        "Emma" if "Emma" not in P_Harem and "met" in E_History:
                                call Poly_Start("Emma",1)
                        "Laura" if "Laura" not in P_Harem and "met" in L_History:
                                call Poly_Start("Laura",1)
                        "Never mind":
                                pass
                                
            "I think we should break up." if "dating" in R_Traits or "Rogue" in P_Harem:
                if "breakup talk" in R_RecentActions:
                    ch_r "We were {i}just{/i} over this, not even funny."
                elif "breakup talk" in R_DailyActions:
                    ch_r "Tired of me again that quick?" 
                    ch_r "We're not having this talk today, [R_Petname]."
                else:
                    call Breakup("Rogue")                
                
                
    #        "I'd like to bring Kitty into this." if "poly Kitty" not in R_Traits and not K_Break[0]:    #fix nonfunctional yet
                
    #            if "asked threesome" in R_RecentActions:
    #                ch_r "Persistence will NOT be rewarded here."
    #                return
    #            elif "asked threesome" in R_DailyActions:
    #                ch_r "I don't think my answer's changing any time soon." 
    #                return
    #            else:
    #                $ R_DailyActions.append("asked threesome")                
    #                $Cnt = int((R_LikeKitty - 500)/2)
    #                menu:
    #                    ch_r "What does she think about this?"
                            
    #                    "She said I can be with you too." if "poly Rogue" in K_Traits:
    #                        if ApprovalCheck("Rogue", 1800, Bonus = Cnt):
    #                            call RogueFace("smile", 1)
    #                            if R_Love >= R_Obed:
    #                                ch_r "Just so long as we can be together, I can share."
    #                            elif R_Obed >= R_Inbt:
    #                                ch_r "I'm ok with that if she is."
    #                            else:
    #                                ch_r "Yeah, I mean I guess so."
    #                                $ R_Traits.append("poly Kitty")
    #                        else:
    #                            call RogueFace("angry", 1)
    #                            ch_r "Well maybe she did, but I don't want to share."  
                        
    #                    "I could ask if she'd be ok with me dating you both." if "poly Rogue" not in K_Traits:
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
    #                        if R_LikeKitty >= 700:
    #                            ch_r "I have to say I've kind of been thinking about it myself."  
    #                            call Statup("Rogue", "Love", 90, 5)
    #                            call Statup("Rogue", "Obed", 70, 1)
    #                            call Statup("Rogue", "Inbt", 80, 5)
    #                        elif R_LikeKitty >= 500:
    #                            ch_r "I guess, if that's what you want. . ." 
    #                        elif R_Obed >= 700:
    #                            ch_r "If that's what you want. . ." 
    #                        else:
    #                            ch_r "I can't really stand her, I don't think so."  
                                
                            
    #                    "You're right, I was dumb to ask.":
    #                        call RogueFace("sad")
    #                        ch_r "Yeah, you were."  
                            
                #end Kitty Threesome
                    
            
            "About that talk we had before. . .":
                menu:
                    "You weren't a virgin?" if R_Sex and not R_Chat[0]:
                        call Rogue_Not_Virgin   
                    
                    "You said you wanted me to be your Master?" if R_Event[8] and "master" not in R_Petnames:
                        menu:
                            ch_r "Yes?"
                            "I'm ok with that now.":
                                if ApprovalCheck("Rogue", 800, "O"):     
                                    call RogueFace("sexy", 1)
                                    ch_r "I hope to serve well, Master."
                                    call Statup("Rogue", "Obed", 200, 100) 
                                    $ R_Petnames.append("master")
                                    $ R_Event[8] = 2
                                else:
                                    ch_r "Well, I'm not really interested in that sort of thing anymore."
                                    ch_r "I mean, maybe later." 
                            "Never mind.":
                                call RogueFace("sad")
                                ch_r "Oh."
                                call Statup("Rogue", "Obed", 200, -5)
                                call Statup("Rogue", "Love", 90, -5)  
                    "Never Mind":
                        pass
                            
            "Never Mind":
                return
                  
        return

#label Rogue_Breakup(Anger = 0):  
#    $ R_RecentActions.append("breakup talk")  
#    $ R_DailyActions.append("breakup talk")
#    if R_Break[1] > 3:       
#            call RogueFace("angry")
#            call Statup("Rogue", "Love", 50, -5, 1)
#            call Statup("Rogue", "Love", 80, -10, 1)
#            call Statup("Rogue", "Obed", 30, -5, 1)
#            call Statup("Rogue", "Obed", 50, -10, 1)
#            call Statup("Rogue", "Inbt", 50, 3)
#            call Statup("Rogue", "Inbt", 80, 1)
#            ch_r "This is getting old, [R_Petname]."       
#            $ Anger += 2
#    elif R_Break[1]:
#            call RogueFace("surprised")
#            call Statup("Rogue", "Love", 50, -5, 1)
#            call Statup("Rogue", "Obed", 30, -5, 1)
#            call Statup("Rogue", "Inbt", 80, 1)
#            ch_r "What, again?"   
#            call RogueFace("angry")
#            $ Anger += 1
#    else:
#            call RogueFace("surprised")
#            ch_r "What?! Why?"    
    
#    $ Line = "denial"
#    menu:
#        "It's not you, it's me.":  
#                call Statup("Rogue", "Love", 200, -5)
#                call Statup("Rogue", "Obed", 80, -5)
#                call Statup("Rogue", "Inbt", 50, 3) 
#                call Statup("Rogue", "Inbt", 70, 1) 
#                call RogueFace("confused")
            
#        "I just think we need a break.":
#                call Statup("Rogue", "Love", 200, -5)
#                call RogueFace("sad")
            
#        "I've found someone else.":      
#                $ Anger += 1
#                call Statup("Rogue", "Love", 200, -10)
#                call Statup("Rogue", "Obed", 50, 3)
#                call Statup("Rogue", "Obed", 80, 3)
#                call Statup("Rogue", "Inbt", 50, -5)  
#                call RogueFace("angry")
#                menu:
#                    ch_r "Who is it?"
#                    "Kitty":           
#                        $ Line = "kitty"
#                    "I won't say.":
#                        call Statup("Rogue", "Love", 200, -5)
#                        ch_r "It's Kitty, isn't it."
#                        $ Line = "kitty"
#                    "I was kidding.":  
#                        call Statup("Rogue", "Love", 200, -5)
#                        call Statup("Rogue", "Obed", 50, 3)
#                        ch_r "That was a pretty rude way to deflect there."
#                        $ Line = "denial"
                    
#        "I'm just done with you.":  
#                call RogueFace("angry")
#                call Statup("Rogue", "Love", 50, 3)
#                call Statup("Rogue", "Love", 200, -15)
#                call Statup("Rogue", "Obed", 50, 5)
#                call Statup("Rogue", "Obed", 80, 5)
#                call Statup("Rogue", "Obed", 200,5)
#                call Statup("Rogue", "Inbt", 50, -5)                
#                $ Anger += 1
            
#    if Line == "denial":
#            call RogueFace("sad")
#            if ApprovalCheck("Rogue", 900, "O"):
#                ch_r "If that's really what you want. . ."           
#            elif ApprovalCheck("Rogue", 900, "L"):
#                ch_r "But I love you so much!"
#            elif ApprovalCheck("Rogue", 900, "I"):
#                ch_r "I guess if that's what you want. . ."    
#            elif ApprovalCheck("Rogue", 1500):
#                ch_r "But we mean so much to each other!"
#            else: 
#                ch_r "Are you sure this is what you want?" 
#            $ Line = "bargaining"
            
#    elif Line == "kitty":
#        $Cnt = int((R_LikeKitty - 500)/2)       
#        if R_LikeKitty >= 800: 
#                call Statup("Rogue", "Lust", 70, 5)
#                call Statup("Rogue", "Obed", 50, 5)
#                call Statup("Rogue", "Obed", 200, 5)
#                call Statup("Rogue", "Inbt", 50, 1)
#                call Statup("Rogue", "Inbt", 200, 5) 
#                $ R_Blush = 1
#                ch_r "Well, you have good tastes, at least."
#        elif R_LikeKitty >= 600:
#                call Statup("Rogue", "Love", 50, -5, 1)
#                call Statup("Rogue", "Love", 80, -10, 1)
#                call Statup("Rogue", "Obed", 50, 5)
#                call Statup("Rogue", "Obed", 200, 3)
#                ch_r "With one of my closest friends?!"
#                $ Anger += 1
#        elif R_LikeKitty >= 400:
#                call Statup("Rogue", "Love", 50, -3, 1)
#                call Statup("Rogue", "Love", 80, -5, 1)
#                call Statup("Rogue", "Obed", 80, 5)
#                call Statup("Rogue", "Inbt", 50, 1)
#                call Statup("Rogue", "Inbt", 80, 3) 
#                ch_r "You know you can do better."
#        else: #R_LikeKitty < 400
#                call Statup("Rogue", "Love", 50, -5, 1)
#                call Statup("Rogue", "Obed", 80, 3)
#                call Statup("Rogue", "Inbt", 50, 2)
#                call Statup("Rogue", "Inbt", 80, 5) 
#                call RogueFace("angry")
#                ch_r "With that skank?!"
#                $ Anger += 2
            
#        if ApprovalCheck("Rogue", 2000, Bonus = Cnt):
#                call Statup("Rogue", "Lust", 70, 5)
#                call RogueFace("sexy")
#                ch_r "Why not both of us?"
#                $ Line = "threeway kitty"
#        else:
#                call RogueFace("sad")
#                menu:
#                    ch_r "You would rather be with her than with me?"
#                    "Yes, I would.":    
#                        call Statup("Rogue", "Love", 50, -3, 1)
#                        call Statup("Rogue", "Love", 80, -5, 1)
#                        call Statup("Rogue", "Obed", 30, 1)
#                        call Statup("Rogue", "Obed", 50, 1)                   
#                        $ Anger += 1
#                        ch_r "Well then I don't think I can help you." 
#                        $ Line = "bargaining"
                        
#                    "I'd rather be with both of you.":      
#                        $ Line = "threeway kitty"
                        
#                    "No, I'm sorry, never mind that.": 
#                        call Statup("Rogue", "Love", 50, -3, 1)
#                        call Statup("Rogue", "Obed", 80, -5)
#                        $ Line = "bargaining"
    
    
#    if Line == "threeway kitty":
#            menu Rogue_Breakup_Kitty:
#                ch_r "Like date us both at once? What does she think about that?"
#                "She said it would be ok with her." if "poly Rogue" in K_Traits:
#                            if ApprovalCheck("Rogue", 1800, Bonus = Cnt):
#                                call RogueFace("smile", 1)
#                                call Statup("Rogue", "Lust", 70, 5)     
#                                call Statup("Rogue", "Obed", 50, 5)
#                                call Statup("Rogue", "Obed", 80, 3)  
#                                call Statup("Rogue", "Inbt", 50, 3)
#                                call Statup("Rogue", "Inbt", 80, 1)
#                                if R_LikeKitty < 400:
#                                    call RogueFace("angry")
#                                    ch_r "I can't stand that bitch, but for you I'll put up with her."     
#                                elif R_LikeKitty >= 700:
#                                    call RogueFace("sexy")
#                                    ch_r "I have to say I've kind of been thinking about it myself."                         
#                                elif R_Love >= R_Obed:
#                                    call RogueFace("sad")
#                                    ch_r "Just so long as we can be together, I can share."
#                                elif R_Obed >= R_Inbt:
#                                    ch_r "I'm ok with that if she is."
#                                else:
#                                    ch_r "Yeah, I mean I guess so."    
#                                $ R_Traits.append("poly Kitty")
                                
#                            else:      
#                                $ Anger += 2
#                                call Statup("Rogue", "Love", 50, -10, 1)
#                                call Statup("Rogue", "Love", 80, -15, 1)
#                                call Statup("Rogue", "Obed", 50, 3)
#                                call Statup("Rogue", "Obed", 80, 3) 
#                                call Statup("Rogue", "Inbt", 50, 5)
#                                call Statup("Rogue", "Inbt", 80, 3)
#                                call RogueFace("angry", 1)
#                                ch_r "Well maybe she did, but I don't want to share."  
#                                $ Line = "bargaining"
#                #End "she said it'd be ok.
                        
#                "I have no idea." if not K_Break[0]:
#                            $ Line = "ask Kitty"
                
#                "She's not into it." if K_Break[0]:
#                            if R_LikeKitty >= 700:
#                                call Statup("Rogue", "Love", 200, -5)
#                            elif R_LikeKitty <= 400:
#                                call Statup("Rogue", "Love", 90, 5)
                                    
#                "She doesn't need to know.": 
#                            $ Line = "ask Kitty"  
#                            if R_LikeKitty >= 700:
#                                call RogueFace("angry")
#                                call Statup("Rogue", "Love", 200, -5)
#                            elif R_LikeKitty <= 400:
#                                call Statup("Rogue", "Love", 90, 5)
            
#            if Line == "ask Kitty" and R_LikeKitty >= 700:
#                            call RogueFace("sexy")
#                            ch_r "I have to say I've kind of been thinking about it myself."  
#                            menu:                         
#                                ch_r "Would you like me to ask her for you?" 
#                                "Yes, that'd be a good idea.":
#                                    call Statup("Rogue", "Love", 90, 5)
#                                    call Statup("Rogue", "Obed", 70, 1)
#                                    call Statup("Rogue", "Inbt", 80, 5)
#                                    $ R_Traits.append("ask Kitty")
#                                "No, let's just keep it under cover.":   
#                                    call Statup("Rogue", "Love", 50, -5, 1)
#                                    call Statup("Rogue", "Love", 80, -5, 1)
#                                    call Statup("Rogue", "Obed", 80, 5)
#                                    call Statup("Rogue", "Inbt", 50, 3)     
                    
        
#            if Line != "bargaining" and "poly Kitty" not in R_Traits:               
                        
#                if "ask Kitty" not in R_Traits and not ApprovalCheck("Rogue", 1800, Bonus = -(int((R_LikeKitty - 600)/2))): #checks if Rogue likes you more than Kitty
#                            call Statup("Rogue", "Love", 50, -5, 1)
#                            call Statup("Rogue", "Obed", 80, -10, 1)
#                            call Statup("Rogue", "Inbt", 50, 5)
#                            call RogueFace("angry", 1)
#                            if not ApprovalCheck("Rogue", 1800):                        
#                                    ch_r "Well I don't like you that much either."
#                            else:
#                                    call Statup("Rogue", "Love", 80, -10, 1)
#                                    call Statup("Rogue", "Obed", 50, -5, 1)
#                                    ch_r "Well then I'm not cool with that, Kitty's a friend of mine."       
#                            $ Anger += 1
#                            $ Line = "bargaining"                                 
#                else:                
#                            call Statup("Rogue", "Obed", 30, 5)
#                            call Statup("Rogue", "Obed", 50, 3)
#                            call Statup("Rogue", "Inbt", 50, 5)
#                            call Statup("Rogue", "Inbt", 80, 1)
#                            call RogueFace("sad")                      
#                            if R_LikeKitty < 400:
#                                    call RogueFace("angry")
#                                    ch_r "I can't stand that bitch, but for you I'll put up with her."    
#                            elif R_Love >= R_Obed:
#                                    ch_r "I really do want to be together with you."
#                            elif R_Obed >= R_Inbt:
#                                    ch_r "If that's how you want it to be."
#                            else:
#                                    ch_r "I suppose that's ok."
#                            $ R_Traits.append("poly Kitty")
#                            if "ask Kitty" in R_Traits:
#                                    ch_r "I'll talk to Kitty about it."
#                            else:
#                                    call RogueFace("sad")
#                                    $ R_Traits.append("downlow")
#                                    ch_r "I guess we can keep this on the downlow, for now at least."
                                
#                                    if R_LikeKitty >= 800:
#                                        ch_r "Please talk to Kitty about sharing you openly though."
#                                    elif R_LikeKitty >= 500:
#                                        ch_r "I really don't like going behind Kitty's back though."
#                                    else:
#                                        ch_r "Might be kind of fun sneaking around behind her back."
#            #End Threeway Kitty
    
#    if Line == "bargaining" and Anger < 3: 
#        call RogueFace("sad")
#        menu Rogue_Breakup_Bargaining:            
#            ch_r "Are you sure there's no way I could convince you to stay?"
#            "My Mind's made up.":
#                    call Statup("Rogue", "Obed", 80, 5)
#                    $ Line = "breakup"
#            "Well, you could do something for me. . .[[sex menu]":
#                    call Statup("Rogue", "Obed", 80, 3)
#                    $ Tempmod = 50
#                    $ MultiAction = 0
#                    call Rogue_SexMenu
#                    $ MultiAction = 1
#                    menu:
#                        "Ok, I guess we can give it another shot.":
#                            call Statup("Rogue", "Love", 80, 3)
#                            call Statup("Rogue", "Obed", 80, 5)
#                            $ Line = "makeup"
#                            call RogueFace("smile")
                        
#                        "That was nice, but we're still over.":
#                            call RogueFace("angry")
#                            call Statup("Rogue", "Love", 50, -5, 1)
#                            call Statup("Rogue", "Love", 80, -10, 1)
#                            call Statup("Rogue", "Obed", 50, 15)
#                            call Statup("Rogue", "Obed", 80, 10)
#                            $ Line = "breakup"                              
#                            $ Anger += 4
                
#            "Maybe if we brought someone else into this relationship?" if "bargainthreeway" not in R_RecentActions:
#                    $ R_RecentActions.append("bargainthreeway")
#                    menu:
#                        ch_r "Who?"
#                        "Kitty?":
#                                call RogueFace("confused")
#                                $ Line = "threeway kitty"
#                                jump Rogue_Breakup_Kitty
#                        #"Your pick.": #add this later when there are more girls
#                        "Never mind, silly question.":                            
#                                call Statup("Rogue", "Love", 200, -10)
#                                call Statup("Rogue", "Obed", 50, -10, 1)
#                                $ Anger += 1
#                                call RogueFace("angry")
#                                jump Rogue_Breakup_Bargaining
                        
#        if Anger < 3 and Line != "breakup" and Line != "makeup":
#                jump Rogue_Breakup_Bargaining
                        
                        
#        # End Bargaining
            
#    if Line == "breakup" or Anger >= 4: #add anger stat to track how mad she's getting.
#        if Anger >= 4:
#                call RogueFace("angry")
#                call Statup("Rogue", "Love", 60, -10, 1)
#                call Statup("Rogue", "Obed", 50, -5)
#                call Statup("Rogue", "Inbt", 70, 5)
#                ch_r "Well fuck you then!"
#                if R_Love >= R_Obed:
#                    ch_r "You broke my fucking heart, asshole."
#                elif R_Obed >= R_Inbt:
#                    call Statup("Rogue", "Obed", 200, -20)
#                    call RogueFace("sad")
#                    ch_r "You're abandoning me."
#                else:
#                    ch_r "Now who'll I fuck?"  
#        else:
#                call Statup("Rogue", "Inbt", 70, 5)
#                call RogueFace("sad")
#                ch_r "I'm sad we couldn't work something out."
#                if R_Love >= R_Obed:
#                    ch_r "I'll really miss you."
#                elif R_Obed >= R_Inbt:
#                    call Statup("Rogue", "Obed", 200, -10)
#                    ch_r "You're abandoning me."
#                else:
#                    ch_r "Now who'll I fuck?"  
            
#        $ R_Traits.remove("dating")
#        $ R_Traits.append("ex")
#        $ R_Break[0] = 5 + R_Break[1] + R_Cheated
        
#    else: #Stay together.
#            call RogueFace("smile")
#            ch_r "I really am glad we could work things out."
#            if R_Love >= R_Obed:
#                call Statup("Rogue", "Love", 200, 3)
#                ch_r "I'd really miss you."
#            elif R_Obed >= R_Inbt:
#                ch_r "I need you with me."
#            else:
#                ch_r "We have fun together."   
        
#    $ Line = 0
    
#    return
#    #End Break-up
                
label Rogue_OtherWoman(Cnt = 0):
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    if not P_Harem:
            return            
            
    if "Kitty" == P_Harem[0]:           
            $Cnt = int((R_LikeKitty - 500)/2)
    elif "Emma" == P_Harem[0]:     
            $Cnt = int((R_LikeEmma - 500)/2)
    elif "Laura" == P_Harem[0]:           
            $Cnt = int((R_LikeLaura - 500)/2)
    else:
            $Cnt = 100     
        
    call RogueFace("perplexed")
    if len(P_Harem) >= 2:
        ch_r "But you're with [P_Harem[0]] right now, and a whole mess'a other girls!"
    else:    
        ch_r "But you're with [P_Harem[0]]!"
    menu: 
        extend ""
        "She said I can be with you too." if "RogueYes" in P_Traits:
                if ApprovalCheck("Rogue", 1800, Bonus = Cnt):
                    call RogueFace("smile", 1)
                    if R_Love >= R_Obed:
                        ch_r "I s'pose I can learn ta share."
                    elif R_Obed >= R_Inbt:
                        ch_r "Well I won't be the one to get in the way a this."
                    else:
                        ch_r "Ok, sure."
                else:
                    call RogueFace("angry", 1)
                    ch_r "Well that harlot!"  
                    $ renpy.pop_call()                                          
                    #This causes it to jump past the previous menu on the return
        
        "I could ask if she'd be ok with me dating you both." if "RogueYes" not in P_Traits:
                if ApprovalCheck("Rogue", 1800, Bonus = Cnt):
                    call RogueFace("smile", 1)
                    if R_Love >= R_Obed:
                        ch_r "I s'pose I can learn ta share."
                    elif R_Obed >= R_Inbt:
                        ch_r "Well I won't be the one to get in the way a this."
                    else:
                        ch_r "Ok, sure."               
                    ch_r "You go ask her if she's inta that, then get back to me tomorrow."
                else:
                    call RogueFace("angry", 1)
                    ch_r "Well that harlot!"     
                $ renpy.pop_call()
        
        "What she doesn't know won't hurt her.":
                if not ApprovalCheck("Rogue", 1800, Bonus = -Cnt): #checks if Rogue likes you more than Rogue
                    call RogueFace("angry", 1)
                    if not ApprovalCheck("Rogue", 1800):
                        ch_r "Well now I don't wantcha."
                    else:
                        ch_r "I ain't in a sharin mood."                    
                    $ renpy.pop_call() 
                
                else:
                    call RogueFace("smile", 1)
                    if R_Love >= R_Obed:
                        ch_r "I s'pose somethin could be arranged. . ."
                    elif R_Obed >= R_Inbt:
                        ch_r "If you insist."
                    else:
                        ch_r "Don't see why not."
                    $ R_Traits.append("downlow")
                
        "I can break it off with her.":
                    call RogueFace("sad")
                    ch_r "Well then talk to me after you have."                                   
                    $ renpy.pop_call()
            
        "You're right, I was dumb to ask.":
                    call RogueFace("sad")
                    ch_r "Yeah. . ."                    
                    $ renpy.pop_call()                   
                
    return
    
# End Rogue Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////    

#Rogue Settings ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label Rogue_Settings:
    menu:
        ch_p "Let's talk about you."
        "Wardrobe":
                    ch_p "I wanted to talk about your style."
                    call Taboo_Level
                    if R_Taboo:
                            if "exhibitionist" in R_Traits:
                                ch_r "Oooh, naughty. . ."  
                            elif ApprovalCheck("Rogue", 900, TabM=4) or ApprovalCheck("Rogue", 400, "I", TabM=3): 
                                ch_r "Well, I mean, it's pretty public here, but I guess I could. . ."
                            else:
                                ch_r "This is a pretty public place for that, don't you think?"
                                ch_r "We can talk about that back in our rooms."
                                return
                            call Rogue_Clothes
                    elif ApprovalCheck("Rogue", 900, TabM=4) or ApprovalCheck("Rogue", 600, "L") or ApprovalCheck("Rogue", 300, "O"):
                        ch_r "Ok, what did you want?"
                        call Rogue_Clothes
                    else:
                        ch_r "I'm not really interested in your fashion opinions."
                                                
        "Shift her Personality" if ApprovalCheck("Rogue", 900, "L", TabM=0) or ApprovalCheck("Rogue", 900, "O", TabM=0)or ApprovalCheck("Rogue", 900, "I", TabM=0):
                    ch_p "Could we talk about us?"
                    call Rogue_Personality
        
        "Pet names":
            menu:       
                "Your Petname":
                            ch_p "Could we talk about my pet name?"
                            if ApprovalCheck("Rogue", 600, "L", TabM=0) or ApprovalCheck("Rogue", 300, "O", TabM=0):
                                call Rogue_Names    
                            else:
                                $ R_Mouth = "smile"
                                ch_r "I'll call you what I like, [R_Petname], and you'll like it."
                        
                "Her Petname":
                            ch_p "I've got a pet name for you, you know?"
                            if ApprovalCheck("Rogue", 600, "L", TabM=0):
                                ch_r "Oh? What is it?" 
                            elif ApprovalCheck("Rogue", 300, "O", TabM=0):
                                ch_r "What did you want to call me?"
                            else:
                                ch_r "Oh, this should be good. . ."            
                            call Rogue_Pet   
                "Back":
                        pass
                                    
        "Follow options" if "follow" in R_Traits:
                    ch_p "You know how you ask if I want to follow you sometimes?"
                    $ Line = 0
                    menu:
                        ch_r "Yes?"
                        "You can go where you want, I'll catch up later." if "freetravels" not in R_Traits:
                            call RogueFace("perplexed")
                            ch_r "Oh, ok, not a problem."
                            if "follow" not in R_DailyActions:
                                call Statup("Rogue", "Love", 90, -2)
                                call Statup("Rogue", "Obed", 30, 5) 
                            $ Line = "free"
                                
                        "You can ask if I want to follow you." if "asktravels" not in R_Traits or "freetravels" in R_Traits:
                            call RogueFace("perplexed")
                            ch_r "Oh, ok, not a problem."
                            if "follow" not in R_DailyActions:
                                call Statup("Rogue", "Love", 70, 2) 
                                call Statup("Rogue", "Inbt", 60, 2) 
                            $ Line = "ask"
                                                    
                        "Don't ever leave when I'm around." if "lockedtravels" not in R_Traits or "freetravels" in R_Traits:
                            if ApprovalCheck("Rogue", 500, "O") or ApprovalCheck("Rogue", 900, "L"):   
                                call RogueFace("sexy")
                                ch_r "Oh, Ok."
                                if "follow" not in R_DailyActions:
                                    if R_Love > 90:
                                        call Statup("Rogue", "Love", 99, 2)
                                    call Statup("Rogue", "Obed", 60, 5)                             
                                call Statup("Rogue", "Inbt", 50, -5, 1) 
                                $ Line = "lock"
                            else:
                                call RogueFace("angry")
                                ch_r "Well, I don't really care what you think on the matter."
                                
                        "Never mind.":
                            ch_r "Oh, ok."
                    
                    if Line:
                        $ R_DailyActions.append("follow")                
                        if "freetravels" in R_Traits:
                            $ R_Traits.remove("freetravels") 
                        if "asktravels" in R_Traits:
                            $ R_Traits.remove("asktravels") 
                        if "lockedtravels" in R_Traits:
                            $ R_Traits.remove("lockedtravels") 
                    
                        if Line == "free":
                            $ R_Traits.append("freetravels")            
                        elif Line == "ask":
                            $ R_Traits.append("asktravels")                
                        elif Line == "lock":
                            $ R_Traits.append("lockedtravels")    
                        $ Line = 0
                                   
#        "Tasks" if "sir" in R_Petnames:
#                    ch_p "I have some tasks for you."
#                    call Rogue_Controls
            
        "Switch to. . .":
                menu:
                    "Kitty":
                        call Kitty_Chat_Set("settings")                    
                    "Emma":
                        call Emma_Chat_Set("settings") 
                    "Laura":
                        call Laura_Chat_Set("settings") 
                    "Never mind":
                        pass
                    
        "Never mind.":
                    return  
    jump Rogue_Settings

# End Rogue Chat

label Rogue_Monogamy:
        #called from Rogue_Settings to ask her not to hook up wiht other girls    
        menu:
            "Could you not hook up with other girls?" if "mono" not in R_Traits:
                    if R_Thirst >= 60 and not ApprovalCheck("Rogue", 1700, "LO", TabM=0):
                            #she's too thirsty
                            call AnyFace("Rogue","sly",1) 
                            if "mono" not in R_DailyActions:                                                         
                                    call Statup("Rogue", "Obed", 90, -2) 
                            ch_r "I might consider that, but you don't exactly make yourself available. . ."
                            return
                    elif ApprovalCheck("Rogue", 1200, "LO", TabM=0) and R_Love >= L_Obed:
                            #she cares
                            call AnyFace("Rogue","sly",1) 
                            if "mono" not in R_DailyActions:                                                         
                                    call Statup("Rogue", "Love", 90, 1) 
                            ch_r "Aw, would that make you jealous?" 
                            ch_r "I suppose I could restain myself. . ."
                    elif ApprovalCheck("Rogue", 700, "O", TabM=0):
                            #she is obedient
                            call AnyFace("Rogue","sly",1,Eyes="side") 
                            ch_r "If that's what you really want. . ."
                    else:   
                            #she doesn't care
                            call AnyFace("Rogue","sly",1,Brows="confused") 
                            ch_r "Who I \"hook up\" with is my own damned business." 
                            return                    
                    if "mono" not in R_DailyActions:                                                         
                            call Statup("Rogue", "Obed", 90, 3) 
                    call AnyWord("Rogue",1,0,"mono") #Daily
                    $ R_Traits.append("mono")   
            "Don't hook up with other girls." if "mono" not in R_Traits:
                    if ApprovalCheck("Rogue", 900, "O", TabM=0):
                            #she is obedient
                            call AnyFace("Rogue","sly",1,Eyes="side") 
                            ch_r "Ok."
                    elif R_Thirst >= 60 and not ApprovalCheck("Rogue", 1700, "LO", TabM=0):
                            #she's too thirsty
                            call AnyFace("Rogue","sly",1) 
                            if "mono" not in R_DailyActions:                                                         
                                    call Statup("Rogue", "Obed", 90, -2) 
                            ch_r "I might consider that, but you don't exactly make yourself available. . ."
                            return
                    elif ApprovalCheck("Rogue", 550, "O", TabM=0):
                            #she is obedient
                            call AnyFace("Rogue","sly",1,Eyes="side") 
                            ch_r "If that's what you really want. . ."
                    elif ApprovalCheck("Rogue", 1400, "LO", TabM=0):
                            #she cares
                            call AnyFace("Rogue","sly",1) 
                            ch_r "Is that any way to ask a girl?" 
                            ch_r "Still, I'll do it for you. . ."
                    else:   
                            #she doesn't care
                            call AnyFace("Rogue","sly",1,Brows="confused") 
                            ch_r "Who I \"hook up\" with is my own damned business." 
                            return                     
                    if "mono" not in R_DailyActions:                                                         
                            call Statup("Rogue", "Obed", 90, 3) 
                    call AnyWord("Rogue",1,0,"mono") #Daily
                    $ R_Traits.append("mono")   
            "It's ok if you hook up with other girls." if "mono" in R_Traits:
                    if ApprovalCheck("Rogue", 700, "O", TabM=0):
                            call AnyFace("Rogue","sly",1,Eyes="side") 
                            ch_r "As you wish."
                    elif ApprovalCheck("Rogue", 800, "L", TabM=0):
                            call AnyFace("Rogue","sly",1) 
                            ch_r "I hope you don't give me any reasons to want to. . ." 
                    else:
                            call AnyFace("Rogue","sly",1,Brows="confused") 
                            if "mono" not in R_DailyActions:                                                         
                                    call Statup("Rogue", "Love", 90, -2)
                            ch_r "Oh? Well, glad I got your permission there." 
                    if "mono" not in R_DailyActions:                                                         
                            call Statup("Rogue", "Obed", 90, 3) 
                    if "mono" in R_Traits:
                            $ R_Traits.remove("mono")  
                    call AnyWord("Rogue",1,0,"mono") #Daily 
            "Never mind.":
                pass
        return
        
# end Rogue monogamy <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
   
   
label Rogue_Jumped:
        #called from Rogue_Settings to ask her not to jump you  
        ch_p "Hey, Remember that time you threw yourself at me?" 
        call AnyFace("Rogue","sly",1,Brows="confused") 
        menu:
            ch_r "Yeah?"
            "Could you maybe just ask instead?" if "chill" not in R_Traits:
                    if R_Thirst >= 60 and not ApprovalCheck("Rogue", 1500, "LO", TabM=0):
                            #she's too thirsty
                            call AnyFace("Rogue","sly",1) 
                            if "chill" not in R_DailyActions:                                                         
                                    call Statup("Rogue", "Obed", 90, -2) 
                            ch_r "Maybe don't keep me waiting then. . ."
                            return
                    elif ApprovalCheck("Rogue", 1000, "LO", TabM=0) and R_Love >= L_Obed:
                            #she cares
                            call AnyFace("Rogue","sly",1) 
                            if "chill" not in R_DailyActions:                                                         
                                    call Statup("Rogue", "Love", 90, 1) 
                            ch_r "Sorry, [R_Petname], I just got a little lonely. . ." 
                            ch_r "I'll be good. . ."
                    elif ApprovalCheck("Rogue", 500, "O", TabM=0):
                            #she is obedient
                            call AnyFace("Rogue","sly",1,Eyes="side") 
                            ch_r "If that's what you really want. . ."
                    else:   
                            #she doesn't care
                            call AnyFace("Rogue","sly",1,Brows="confused") 
                            ch_r "I can't make any promises." 
                            return                    
                    if "chill" not in R_DailyActions:                                                         
                            call Statup("Rogue", "Obed", 90, 3) 
                    call AnyWord("Rogue",1,0,"chill") #Daily
                    $ R_Traits.append("chill")   
            "Don't bother me like that." if "chill" not in R_Traits:
                    if ApprovalCheck("Rogue", 900, "O", TabM=0):
                            #she is obedient
                            call AnyFace("Rogue","sly",1,Eyes="side") 
                            ch_r "Ok."
                    elif R_Thirst >= 60 and not ApprovalCheck("Rogue", 600, "O", TabM=0):
                            #she's too thirsty
                            call AnyFace("Rogue","sly",1) 
                            if "chill" not in R_DailyActions:                                                         
                                    call Statup("Rogue", "Obed", 90, -2) 
                            ch_r "Maybe don't keep me waiting then. . ."
                            return
                    elif ApprovalCheck("Rogue", 450, "O", TabM=0):
                            #she is obedient
                            call AnyFace("Rogue","sly",1,Eyes="side") 
                            ch_r "If that's what you really want. . ."
                    elif ApprovalCheck("Rogue", 500, "LO", TabM=0) and not ApprovalCheck("Rogue", 500, "I", TabM=0):
                            #she cares
                            call AnyFace("Rogue","sly",1) 
                            ch_r "You might want to watch your mouth." 
                            ch_r "Still, I'll try to keep to myself. . ."
                    else:   
                            #she doesn't care
                            call AnyFace("Rogue","sly",1,Brows="confused") 
                            ch_r "No promises." 
                            return                     
                    if "chill" not in R_DailyActions:                                                         
                            call Statup("Rogue", "Obed", 90, 3) 
                    call AnyWord("Rogue",1,0,"chill") #Daily
                    $ R_Traits.append("chill")   
            "Knock yourself out.":
                    if ApprovalCheck("Rogue", 800, "L", TabM=0):
                            call AnyFace("Rogue","sly",1) 
                            ch_r "Will do. . ." 
                    elif ApprovalCheck("Rogue", 700, "O", TabM=0):
                            call AnyFace("Rogue","sly",1,Eyes="side") 
                            ch_r "Yes sir."
                    else:
                            call AnyFace("Rogue","sly",1,Brows="confused") 
                            if "chill" not in R_DailyActions:                                                         
                                    call Statup("Rogue", "Love", 90, -2)
                            ch_r "Maybe. If I've got nothing better to do." 
                    if "chill" not in R_DailyActions:                                                         
                            call Statup("Rogue", "Obed", 90, 3) 
                    if "chill" in R_Traits:
                            $ R_Traits.remove("chill")  
                    call AnyWord("Rogue",1,0,"chill") #Daily 
            "Um, never mind.":
                pass
        return
        
# end Rogue jumped <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Rogue Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label Rogue_SexChat(Line = "Yeah, what did you want to talk about?"):
    while True:
            menu:
                ch_r "[Line]"                
                "My favorite thing to do is. . .":
                    if "setfav" in R_DailyActions:
                        ch_r "Yeah, I know. You just told me earlier."
                    else:
                        menu:
                            "Sex.":
                                        call RogueFace("sly")
                                        if R_PlayerFav == "sex":
                                            call Statup("Rogue", "Lust", 80, 5)
                                            ch_r "Yeah, I know that. . ."                                
                                        elif R_Favorite == "sex":
                                            call Statup("Rogue", "Love", 90, 5)
                                            call Statup("Rogue", "Lust", 80, 10)
                                            ch_r "Oooh, I love a good pipe cleaning too. . ."
                                        elif R_Sex >= 5:
                                            ch_r "Can't say as I mind a good roll in the hay."
                                        elif not R_Sex:
                                            call RogueFace("perplexed")
                                            ch_r "Who {i}exactly{/i} are y'all having sex {i}with?{/i}"
                                        else:
                                            call RogueFace("bemused")
                                            ch_r "Heh, [R_Petname], flithy mouth on you. . ."
                                        $ R_PlayerFav = "sex"
                                        
                            "Anal.":
                                        call RogueFace("sly")
                                        if R_PlayerFav == "anal":
                                            call Statup("Rogue", "Lust", 80, 5)
                                            ch_r "So I hear. . ."                                
                                        elif R_Favorite == "anal":
                                            call Statup("Rogue", "Love", 90, 5)
                                            call Statup("Rogue", "Lust", 80, 10)
                                            ch_r "I can't say as I mind that. . ."
                                        elif R_Anal >= 10:
                                            ch_r "It's not a bad way to spend some time. . ."
                                        elif not R_Anal:
                                            call RogueFace("perplexed")
                                            ch_r "Who {i}exactly{/i} are y'all fucking {i}with?{/i}"
                                        else:
                                            call RogueFace("bemused")
                                            ch_r "Heh, heh, I . . . I don't {i}mind{/i} it. . ."
                                        $ R_PlayerFav = "anal"
                                        
                            "Blowjobs.":   
                                        call RogueFace("sly")
                                        if R_PlayerFav == "blow":
                                            call Statup("Rogue", "Lust", 80, 3)
                                            ch_r "I'm not surprised. . ."                                
                                        elif R_Favorite == "blow":
                                            call Statup("Rogue", "Love", 90, 5)
                                            call Statup("Rogue", "Lust", 80, 5)
                                            ch_r "I guess I have developed a real taste for you. . ."
                                        elif R_Blow >= 10:
                                            ch_r "I'm getting to enjoy it too . . ."
                                        elif not R_Blow:
                                            call RogueFace("perplexed")
                                            ch_r "Who {i}exactly{/i} is sucking you off?"
                                        else:
                                            call RogueFace("bemused")
                                            ch_r "I'm. . . getting used to the taste. . ."
                                        $ R_PlayerFav = "blow"     
                                        
                            "Titjobs.":
                                        call RogueFace("sly")    
                                        if R_PlayerFav == "titjob":
                                            call Statup("Rogue", "Lust", 80, 5)
                                            ch_r "So I hear. . ."                           
                                        elif R_Favorite == "titjob":
                                            call Statup("Rogue", "Love", 90, 5)
                                            call Statup("Rogue", "Lust", 80, 7)
                                            ch_r "I really enjoy it too. . ."
                                        elif R_Tit >= 10:
                                            ch_r "It's certainly an interesting experience . . ."
                                        elif not R_Tit:
                                            call RogueFace("perplexed")
                                            ch_r "Who {i}exactly{/i} is tit fucking you?"
                                        else:
                                            call RogueFace("bemused")
                                            ch_r "I can't say as I blame you. . ."
                                        $ R_PlayerFav = "titjob"   
                                        
                            "Handjobs.":
                                        call RogueFace("sly")
                                        if R_PlayerFav == "hand":
                                            call Statup("Rogue", "Lust", 80, 5)
                                            ch_r "Yeah, you've said that before. . ."                                
                                        elif R_Favorite == "hand":
                                            call Statup("Rogue", "Love", 90, 5)
                                            call Statup("Rogue", "Lust", 80, 7)
                                            ch_r "I love how you feel in my hand. . ."
                                        elif R_Hand >= 10:
                                            ch_r "It is pretty nice to touch someone like that . . ."
                                        elif not R_Hand:
                                            call RogueFace("perplexed")
                                            ch_r "Who {i}exactly{/i} is jerking you off?"
                                        else:
                                            call RogueFace("bemused")
                                            ch_r "I do like the sensation. . ."
                                        $ R_PlayerFav = "hand"  
                                        
                            "Feeling you up.":
                                        $ Cnt = R_FondleB + R_FondleT + R_SuckB + R_Hotdog
                                        call RogueFace("sly")
                                        if R_PlayerFav == "fondle":
                                            call Statup("Rogue", "Lust", 80, 3)
                                            ch_r "Yeah, I think we've established that. . ."                                
                                        elif R_Favorite in ("hotdog","suck breasts","fondle breasts","fondle thighs"):
                                            call Statup("Rogue", "Love", 90, 5)
                                            call Statup("Rogue", "Lust", 80, 5)
                                            ch_r "I love how you touch me. . ."
                                        elif Cnt >= 10:
                                            ch_r "It's nice to have someone who can really touch me . . ."
                                        elif not Cnt:
                                            call RogueFace("perplexed")
                                            ch_r "Who {i}exactly{/i} are you feeling up?"
                                        else:
                                            call RogueFace("bemused")
                                            ch_r "I do like how that feels. . ."
                                        $ R_PlayerFav = "fondle"  
                                        $ Cnt = 0
                                
                            "Kissing you.":
                                        call RogueFace("sly")
                                        if R_PlayerFav == "kiss you":
                                            call Statup("Rogue", "Love", 90, 3)
                                            ch_r "I've heard it before, but don't mind hearing it again. . ."                                
                                        elif R_Favorite == "kiss you":
                                            call Statup("Rogue", "Love", 90, 5)
                                            call Statup("Rogue", "Lust", 80, 5)
                                            ch_r "I can't get over your lips either. . ."
                                        elif R_Kissed >= 10:
                                            ch_r "I love kissing you too . . ."
                                        elif not R_Kissed:
                                            call RogueFace("perplexed")
                                            ch_r "Who {i}exactly{/i} are you smooch'in?"
                                        else:
                                            call RogueFace("bemused")
                                            ch_r "It's nice being able to kiss someone without hurting them. . ."
                                        $ R_PlayerFav = "kiss you" 
                                
                        $ R_DailyActions.append("setfav") 
                            
                "What's your favorite thing to do?":
                                if not ApprovalCheck("Rogue", 800):
                                        call RogueFace("perplexed")
                                        ch_r "I don't think that's any of your business. . ."                                    
                                else:
                                        if R_SEXP >= 50:
                                            call RogueFace("sly")
                                            ch_r "If you can't tell. . ."   
                                        else:                 
                                            call RogueFace("bemused")
                                            $ R_Eyes = "side"
                                            ch_r "I don't know, I guess maybe. . ."
                                            
                                            
                                        if not R_Favorite or R_Favorite == "kiss":
                                            ch_r "I guess I love it when we kiss. . ."  
                                        elif R_Favorite == "anal":
                                            if R_Anal >= 10:
                                                ch_r "I like when you fuck my ass."  
                                            else:
                                                ch_r "I like when you stick it in my. . . butt."  
                                        elif R_Favorite == "lick ass":
                                                ch_r "I like when you lick my. . . asshole." 
                                        elif R_Favorite == "insert ass":
                                                ch_r "I like when you . . . finger my asshole." 
                                        elif R_Favorite == "sex":
                                                ch_r "I like when you fuck me hard." 
                                        elif R_Favorite == "lick pussy":
                                                ch_r "I like when you lick my pussy." 
                                        elif R_Favorite == "fondle pussy":
                                                ch_r "I like when you fingerblast me." 
                                        elif R_Favorite == "blow":
                                                ch_r "I kind of like to suck your cock." 
                                        elif R_Favorite == "tit":
                                                ch_r "I like to work your cock with my tits." 
                                        elif R_Favorite == "hand":
                                                ch_r "I like the feel of your cock in my hand." 
                                        elif R_Favorite == "hotdog":
                                                ch_r "I like it when you grind against me." 
                                        elif R_Favorite == "suck breasts":
                                                ch_r "I like it when you suck on my tits."  
                                        elif R_Favorite == "fondle breasts":
                                                ch_r "I like it when you feel up my tits." 
                                        elif R_Favorite == "fondle thighs":
                                                ch_r "I like it when you massage my thighs."
                                        else:
                                                ch_r "I don't really know. . ."    
                                                
                                # End Rogue's favorite things.
                                        
                "Don't talk as much during sex." if "vocal" in R_Traits:
                        if "setvocal" in R_DailyActions:
                            call RogueFace("perplexed")
                            ch_r "We've been over this already."
                        else:              
                            if ApprovalCheck("Rogue", 1000) and R_Obed <= R_Love:
                                call RogueFace("bemused")
                                call Statup("Rogue", "Obed", 90, 1)
                                ch_r "Heh, ok, if that's what you want. . ."
                                $ R_Traits.remove("vocal")   
                            elif ApprovalCheck("Rogue", 700, "O"):
                                call RogueFace("sadside")
                                call Statup("Rogue", "Obed", 90, 1)
                                ch_r "If that's what you want, [R_Petname]."
                                $ R_Traits.remove("vocal")   
                            elif ApprovalCheck("Rogue", 600):
                                call RogueFace("sly")
                                call Statup("Rogue", "Love", 90, -3)
                                call Statup("Rogue", "Obed", 50, -1)
                                call Statup("Rogue", "Inbt", 90, 5)
                                ch_r "I'll say what I want, and you'll like it, [R_Petname]."
                            else:
                                call RogueFace("angry")
                                call Statup("Rogue", "Love", 90, -5)
                                call Statup("Rogue", "Obed", 60, -3)
                                call Statup("Rogue", "Inbt", 90, 10)
                                ch_r "Fuck you, I'll talk as much as I want."
                                                
                            $ R_DailyActions.append("setvocal")   
                "Talk dirty to me during sex." if "vocal" not in R_Traits:
                        if "setvocal" in R_DailyActions:
                            call RogueFace("perplexed")
                            ch_r "We've been over this already."
                        else:     
                            if ApprovalCheck("Rogue", 1000) and R_Obed <= R_Love:
                                call RogueFace("sly")
                                call Statup("Rogue", "Obed", 90, 2)
                                ch_r "Heh, ok, if that's what you want. . ."
                                $ R_Traits.append("vocal")   
                            elif ApprovalCheck("Rogue", 700, "O"):
                                call RogueFace("sadside")
                                call Statup("Rogue", "Obed", 90, 2)
                                ch_r "If that's what you want, [R_Petname]."
                                $ R_Traits.append("vocal")   
                            elif ApprovalCheck("Rogue", 600):
                                call RogueFace("sly")
                                call Statup("Rogue", "Obed", 90, 3)
                                ch_r "I can give it a shot, [R_Petname]."
                                $ R_Traits.append("vocal")   
                            else:
                                call RogueFace("angry")
                                call Statup("Rogue", "Inbt", 90, 5)
                                ch_r "I'll say what I want, when I want."  
                                
                            $ R_DailyActions.append("setvocal")  
                        # End Rogue Dirty Talk
                                        
                "Don't do your own thing as much during sex." if "passive" not in R_Traits:
                        if "initiative" in R_DailyActions:
                            call RogueFace("perplexed")
                            ch_r "We've been over this already."
                        else:       
                            if ApprovalCheck("Rogue", 1000) and R_Obed <= R_Love:
                                call RogueFace("bemused")
                                call Statup("Rogue", "Obed", 90, 1)
                                ch_r "Heh, ok, lead the way. . ."  
                                $ R_Traits.append("passive")                     
                            elif ApprovalCheck("Rogue", 700, "O"):
                                call RogueFace("sadside")
                                call Statup("Rogue", "Obed", 90, 1)
                                ch_r "I'll restrain myself then, [R_Petname]."
                                $ R_Traits.append("passive")
                            elif ApprovalCheck("Rogue", 600):
                                call RogueFace("sly")
                                call Statup("Rogue", "Love", 90, -3)
                                call Statup("Rogue", "Obed", 50, -1)
                                call Statup("Rogue", "Inbt", 90, 5)
                                ch_r "You know you don't want that, [R_Petname]."
                            else:
                                call RogueFace("angry")
                                call Statup("Rogue", "Love", 90, -5)
                                call Statup("Rogue", "Obed", 60, -3)
                                call Statup("Rogue", "Inbt", 90, 10)
                                ch_r "I'll do what I want, prick."
                                
                            $ R_DailyActions.append("initiative")  
                "Take more initiative during sex." if "passive" in R_Traits:
                        if "initiative" in R_DailyActions:
                            call RogueFace("perplexed")
                            ch_r "We've been over this already."
                        else:   
                            if ApprovalCheck("Rogue", 1000) and R_Obed <= R_Love:
                                call RogueFace("bemused")
                                call Statup("Rogue", "Obed", 90, 1)
                                ch_r "Heh, I think I can handle that. . ."     
                                $ R_Traits.remove("passive")                   
                            elif ApprovalCheck("Rogue", 700, "O"):
                                call RogueFace("sadside")
                                call Statup("Rogue", "Obed", 90, 1)
                                ch_r "I can do that, [R_Petname]."
                                $ R_Traits.remove("passive")   
                            elif ApprovalCheck("Rogue", 600):
                                call RogueFace("sly")
                                call Statup("Rogue", "Obed", 90, 3)
                                ch_r "I can certainly try, [R_Petname]."
                                $ R_Traits.remove("passive")   
                            else:
                                call RogueFace("angry")
                                call Statup("Rogue", "Inbt", 90, 5)
                                ch_r "If I want to, I will, but not because you say so."  
                                
                            $ R_DailyActions.append("initiative")   
                            
                "About getting Jumped" if "jumped" in R_History:
                    call Rogue_Jumped
                "About when you masturbate":
                    call NoFap("Rogue")
                    
                "Never Mind" if Line == "Yeah, what did you want to talk about?":
                    return
                "That's all." if Line != "Yeah, what did you want to talk about?":
                    return
            if Line == "Yeah, what did you want to talk about?":
                $ Line = "Anything else?"
    return
# End Rogue Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



# Rogue Chitchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label Rogue_Chitchat(O=0, Options = ["default","default","default"]):   
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:                                               #adds only a specific option that was sent
        $ Options = [O]
    else:
        
        if "Rogue" not in Digits:
            if ApprovalCheck("Rogue", 500, "L") or ApprovalCheck("Rogue", 250, "I"):
                ch_r "You know, I never got around to giving you my number, here you go."
                $ Digits.append("Rogue")  
                return
            elif ApprovalCheck("Rogue", 250, "O"):
                ch_r "You know, you should probably have my number, here you go."             
                $ Digits.append("Rogue")
                return
                
        if "hungry" not in R_Traits and (R_Swallow + R_Chat[2]) >= 10 and R_Loc == bg_current:  #She's swallowed a lot        
            call Rogue_Hungry
            return  
        
#        $ Options = ["default","default","default","bub"]
        #adds options based on accomplishments
        if ApprovalCheck("Rogue", 1200):
            $ Options.append("dance") 
        if ApprovalCheck("Rogue", 800, "L") and "nametag chat" not in R_DailyActions:
            $ Options.append("close")            
        if R_Blow >= 2:
            $ Options.append("blow")        
        if "steal" in R_Traits:
            $ Options.append("steal")
        if PunishmentX and "caught chat" not in R_DailyActions:
            $ Options.append("caught")
        if R_Event[0] and "key chat" not in R_DailyActions:
            $ Options.append("key")
        if "lover" in R_Petnames and ApprovalCheck("Rogue", 900, "L"): # luvy dovey       
            $ Options.append("luv")
              
        if "mandrill" in P_Traits and "cologne chat" not in R_DailyActions:
            $ Options.append("mandrill")        
        if "purple" in P_Traits and "cologne chat" not in R_DailyActions:
            $ Options.append("purple")        
        if "corruption" in P_Traits and "cologne chat" not in R_DailyActions:
            $ Options.append("corruption")
                    
        if not R_Chat[0] and R_Sex:
            $ Options.append("virgin")    
            
        if (bg_current == "bg rogue" or bg_current == "bg player") and "nametag chat" not in R_DailyActions:
            if "lover" not in R_Petnames and ApprovalCheck("Rogue", 900, "L"): # R_Event[6]        
                $ Options.append("lover?")
            elif "sir" not in R_Petnames and ApprovalCheck("Rogue", 500, "O"): # R_Event[7]
                $ Options.append("sir?")     
            elif "daddy" not in R_Petnames and ApprovalCheck("Rogue", 750, "L") and ApprovalCheck("Rogue", 500, "O") and ApprovalCheck("Rogue", 500, "I"): # R_Event[5]
                $ Options.append("daddy?")
            elif "master" not in R_Petnames and ApprovalCheck("Rogue", 900, "O"): # R_Event[8]
                $ Options.append("master?")
            elif "sex friend" not in R_Petnames and ApprovalCheck("Rogue", 500, "I"): # R_Event[9]
                $ Options.append("sexfriend?")
            elif "fuck buddy" not in R_Petnames and ApprovalCheck("Rogue", 900, "I"): # R_Event[10]
                $ Options.append("fuckbuddy?")  
            
        
        if not ApprovalCheck("Rogue", 300):            #She dislikes you
            $ Options.append("hate") 
    
    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one
    
    if Options[0] == "virgin": # "virgin line" not yet triggered:
        call Rogue_Not_Virgin
    
    elif Options[0] == "mandrill":                             
        $ R_DailyActions.append("cologne chat") 
        call RogueFace("confused")
        ch_r "(sniff, sniff). . . something kind of smells like monkey butt in here. . ."
        call RogueFace("sly", 1)
        ch_r ". . . but you're looking pretty handsome today, [R_Petname]."    
    elif Options[0] == "purple":              
        $ R_DailyActions.append("cologne chat") 
        call RogueFace("sly",1)
        ch_r "(sniff, sniff). . . hmm, you're smelling good today. . ."
        ch_r ". . . was there anything I could do to make you happy?"    
    elif Options[0] == "corruption":              
        $ R_DailyActions.append("cologne chat") 
        call RogueFace("confused")
        ch_r "(sniff, sniff). . . that's a pretty strong scent you've got there. . ."
        call RogueFace("sly")
        ch_r ". . . I'm gettin some pretty naughty thoughts over here, [R_Petname]. . ."
        
    elif Options[0] == "blow":
        $ Line = renpy.random.choice(["You know, you taste better than I thought.", 
                "You're making my jaw a bit sore there.", 
                "Let me know if you want a little mouth attention.",
                "Hmmm. . . [she mimes her tongue knocking against her cheek.]"])
        ch_r "[Line]"
        
    elif Options[0] == "close": # R_Love >= 800
        ch_r "It's always been hard for me to get close to people, since I could never. . ."
        ch_r "get {i}close{/i} to them, you know?"    
        ch_r "It's been real good for me to be able to get close to you like this."
        $ R_DailyActions.append("close chat") 
    elif Options[0] == "caught": # Xavier's caught you
        ch_r "Wow, that was scary getting dragged into the Professor's office."
        if not ApprovalCheck("Rogue", 500, "I"):
            ch_r "Maybe we should be more careful about where we. . . you know."
        else:
            ch_r "Maybe we should be more careful about where we fuck."
        $ R_DailyActions.append("caught chat") 
    elif Options[0] == "key": # you have her key
        if R_SEXP <= 15:
            ch_r "I'm glad you have my key now, just don't use it for any funny business. . ."
        else:
            ch_r "I'm glad you have my key now, maybe you could . . . \"surprise\" me sometime. . ."
        $ R_DailyActions.append("key chat") 
    elif Options[0] == "touch": # "touch" in R_Traits:
        ch_r "It's only because I've been working with you so much that I've been able to learn to control my abilities."
        ch_r "If it weren't for you, I wouldn't have been able to touch anyone!"
    elif Options[0] == "steal": # "steal" in R_Traits:
        ch_r "It's only because of having worked with you and your powers that I've learned to permanently copy other mutant powers."   
    elif Options[0] == "dance": # dancing comes up
        ch_r "Can't wait for the next big party."
        ch_r "I love to dance, and I've got the best partner to grind with-"
        call Rogue_Doggy_Launch("massage")
        if R_Legs == "skirt":
            $ R_Upskirt = 1
            if R_Panties and R_SeenPanties and ApprovalCheck("Rogue", 800, TabM = 3):
                pass
            elif R_Panties and ApprovalCheck("Rogue", 800, TabM = 3):
                $ R_SeenPanties = 1
            elif R_Panties:
                $ R_Upskirt = 0                            
            elif R_SeenPussy and ApprovalCheck("Rogue", 1000, TabM = 4):
                pass
            elif ApprovalCheck("Rogue", 1400, TabM = 3):
                call Rogue_First_Bottomless(1)  
            else:
                $ R_Upskirt = 0            
            pause 0.5  
            $ R_Upskirt = 0      
        ch_r "Y'know what I'm sayin', [R_Petname]?"        
        $ R_Upskirt = 0      
        call Rogue_Doggy_Reset

        
    elif Options[0] == "luv": # love maxed out
        call RogueFace("bemused", 1)
        ch_r ". . ."
        ch_r "You know, time was, I really thought I'd end up alone, unable to touch anyone. . ."        
        call RogueFace("smile")
        ch_r "I'm really glad that I was able to find you."
        ch_r "I love you, [R_Petname]."
        menu:
            extend ""
            "I love you too.":
                call Statup("Rogue", "Love", 200, 10)
                call Statup("Rogue", "Obed", 80, 4)
                call Statup("Rogue", "Inbt", 80, 4)
            "I love you too, [R_Pet].":
                call Rogue_Namecheck
                if _return:                    
                    call RogueFace("angry")
                    call Statup("Rogue", "Love", 90, -1)
                    call Statup("Rogue", "Obed", 80, 10)
                    call Statup("Rogue", "Inbt", 80, 4)
                else:
                    call Statup("Rogue", "Love", 200, 10)
                    call Statup("Rogue", "Obed", 80, 4)
                    call Statup("Rogue", "Inbt", 80, 4)
            "Yeah, same here.":                
                call RogueFace("perplexed")
                call Statup("Rogue", "Love", 90, -1)
                call Statup("Rogue", "Obed", 80, 10)
                call Statup("Rogue", "Inbt", 80, 4)
            "Whatever.":
                call RogueFace("angry")
                call Statup("Rogue", "Love", 200, -10)
                call Statup("Rogue", "Obed", 80, 4)
                call Statup("Rogue", "Inbt", 80, 10)
    
    elif Options[0] == "boyfriend?":
        call Rogue_BF
        $ R_DailyActions.append("nametag chat") 
    elif Options[0] == "lover?":
        call Rogue_Love
        $ R_DailyActions.append("nametag chat") 
    elif Options[0] == "sir?":
        call Rogue_Sub
        $ R_DailyActions.append("nametag chat") 
    elif Options[0] == "master?":
        call Rogue_Slave
        $ R_DailyActions.append("nametag chat") 
    elif Options[0] == "sexfriend?":
        call Rogue_Sexfriend
        $ R_DailyActions.append("nametag chat") 
    elif Options[0] == "fuckbuddy?":
        call Rogue_Fuckbuddy 
        $ R_DailyActions.append("nametag chat")  
    elif Options[0] == "daddy?":
        call Rogue_Daddy  
        $ R_DailyActions.append("nametag chat") 
        
    elif Options[0] == "hate": # trinty lower then 50:
        $ Line = renpy.random.choice(["Get away from me.", 
                "I don't want to see your face.", 
                "Stop bothering me.",
                "Leave me alone."])
        ch_r "[Line]"
        
    else: #all else fell through. . .
        $ D20 = renpy.random.randint(1, 16)
        if D20 == 1:
                call RogueFace("confused")
                ch_r "I'm so nervous about this Genetics test with Professor McCoy. I don't get this stuff at all."
        elif D20 == 2:
                call RogueFace("sad")
                ch_r "Feeling kinda down today, [R_Petname]. Family problems. It's. . .kinda complicated."
        elif D20 == 3:
                call RogueFace("sly")
                ch_r "So, um. . .maybe you heard about the friends I used to hang out with? They're not all as bad as they seem. Mostly."
        elif D20 == 4:
                call RogueFace("smile")
                ch_r "I had the best workout earlier in the Danger Room today! Wish you coulda seen me!"
        elif D20 == 5:
                call RogueFace("smile")
                ch_r "Ever wonder what it would be like to be able to fly? That's gotta be the coolest power, right?"
        elif D20 == 6:
                call RogueFace("smile")
                ch_r "Ever been out to Breakstone Lake, behind the Mansion? It's so nice and peaceful. Kinda reminds me of back home in Mississippi, during the summer. Just a little chillier."
        elif D20 == 7:
                call RogueFace("smile")
                $ R_Eyes = "surprised"
                ch_r "I just saw the coolest thing, when I was walking through the courtyard! A bunch of deer, in the woods, just over by the fence!"
                $ R_Eyes = "side"
                ch_r "Their fur looked so. . .{i}soft{/i}. I wonder what they actually feel like?"
        elif D20 == 8:
                call RogueFace("smile")
                ch_r "Hey, did you see the Avengers on the news this morning?  Those guys make everything look {i}so{/i} easy!"
        elif D20 == 9:
                call RogueFace("smile")
                ch_r "A couple of us are gonna get together and go for a jog around one of the Mansion's sub-basements tomorrow. You should come with us!"
        elif D20 == 10:
                call RogueFace("down")
                ch_r "I have {i}so{/i} much homework this week! And I {i}so{/i} don't feel like doing any of it!"
        elif D20 == 11:
                call RogueFace("startled")
                ch_r "Y'know, I {i}really{/i} hate my powers. But could you imagine having Professor Xavier's?" 
                ch_r "I don't know if I could handle that kind of responsibility."
                ch_r "Might be even worse than mine, in their own way."
        elif D20 == 12:
                call RogueFace("sad")
                ch_r "The Mansion's a great place to live. . .but sometimes I get weirded out when I think how we could get attacked by some super-maniac any given second."
        elif D20 == 13:
                call RogueFace("smile")
                ch_r "I love it when you get a really good night's sleep. Feels amazing!"
        elif D20 == 14:
                call RogueFace("bemused")
                ch_r "I heard they're thinking about maybe having a school dance this year. That could be. . .{i}interesting{/i}."
        elif D20 == 15:
                call RogueFace("smile")
                ch_r "You been outside today? Wow, is it gorgeous!"
        elif D20 == 16:
                call RogueFace("smile")
                ch_r "You know, I tagged Wolverine once,"
                call RogueFace("sadside")  
                $ R_Brows = "confused"
                ch_r "I still catch myself calling people \"bub\" from time to time."  
        else:
                call RogueFace("smile")
                ch_r "I like hanging out with you like this!"
    $ Line = 0
    return

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
label Rogue_Flirt:    
    if R_Loc != bg_current:  
        "Rogue isn't around."
        return
        
    $ R_Chat[5] = 1                                         #can only flirt once per cycle. 
    menu:        
        "Compliment her":
                    call Compliment("Rogue")
                
        "Say you love her":
                    call Love_You("Rogue")
            
        "Touch her cheek":                                                                              
                    call R_TouchCheek
        
        "Hold hands":
                    call Hold_Hands("Rogue")        
                        
        "Kiss her cheek":                                                                          
                    "You lean over, brush her hair aside and kiss her on the cheek."                
                    if ApprovalCheck("Rogue", 650, "L", TabM=1):
                        call RogueFace("sexy", 1) 
                        call Statup("Rogue", "Love", 90, 1)          
                        call Statup("Rogue", "Obed", 40, 2) 
                        ch_r "That was real sweet, [R_Petname]."
                    elif ApprovalCheck("Rogue", 500, "L", TabM=1):
                        call RogueFace("surprised", 1)
                        call Statup("Rogue", "Love", 70, 2)         
                        call Statup("Rogue", "Obed", 40, 2)            
                        call Statup("Rogue", "Inbt", 20, 1) 
                        ch_r "What was that for, [R_Petname]?"
                    elif ApprovalCheck("Rogue", 300, "L", TabM=1):                    
                        call RogueFace("angry", 1)
                        call Statup("Rogue", "Love", 90, -1)          
                        call Statup("Rogue", "Obed", 60, 2)            
                        call Statup("Rogue", "Inbt", 40, 1) 
                        ch_r "Hey, keep your distance, [R_Petname]!"
                    else: 
                        call RogueFace("angry", 1)
                        call Statup("Rogue", "Love", 90, -5)          
                        call Statup("Rogue", "Obed", 90, 5)            
                        call Statup("Rogue", "Inbt", 40, 3) 
                        ch_r "Hey, back off!"
                    $ R_Addict -= 1
                    $ R_Addictionrate += 1
                    $ R_Addictionrate = 3 if R_Addictionrate < 3 else R_Addictionrate 
                       
        "Kiss her lips":                                                                                    #Kiss her
                    if ApprovalCheck("Rogue", 800, TabM=1):        
                        "You lean over, put your hand against her cheek, and plant a kiss on her lips."
                    elif ApprovalCheck("Rogue", 800):        
                        call RogueFace("bemused", 1)
                        $ R_Eyes = "side"                  
                        call Statup("Rogue", "Obed", 50, -1)            
                        call Statup("Rogue", "Inbt", 40, 2) 
                        "You lean close for a kiss, but Rogue plants a hand on your face and pushes you back."
                        ch_r "Isn't this a bit public, [R_Petname]?" 
                        return
                    else:                
                        call RogueFace("angry", 1)
                        call Statup("Rogue", "Love", 90, -5)          
                        call Statup("Rogue", "Obed", 50, -1)            
                        call Statup("Rogue", "Inbt", 40, 5) 
                        "You lean close for a kiss, but Rogue plants a hand on your face and pushes you back."
                        ch_r "What the hell, [R_Petname]?" 
                        return
                    if R_Kissed:
                            if ApprovalCheck("Rogue", 750, "L", TabM=1):
                                call RogueFace("sexy", 1)
                                call Statup("Rogue", "Love", 90, 2)          
                                call Statup("Rogue", "Obed", 50, 2) 
                                ch_r "Hmm we should do that again, [R_Petname]."
                            elif ApprovalCheck("Rogue", 650, "L", TabM=1):
                                call RogueFace("sexy", 1)
                                call Statup("Rogue", "Love", 90, 2)          
                                call Statup("Rogue", "Obed", 50, 2) 
                                ch_r "Hmm, that was a nice surprise, [R_Petname]?"
                            elif ApprovalCheck("Rogue", 500, "L", TabM=1):
                                call RogueFace("surprised", 1)
                                call Statup("Rogue", "Love", 70, 3)          
                                call Statup("Rogue", "Obed", 50, 2) 
                                ch_r "Hey, what do you think you're doing, [R_Petname]?"
                            elif ApprovalCheck("Rogue", 300, "L", TabM=1):
                                call RogueFace("angry", 1)
                                call Statup("Rogue", "Love", 90, -3)          
                                call Statup("Rogue", "Obed", 60, 3)            
                                call Statup("Rogue", "Inbt", 40, 2) 
                                ch_r "That really wasn't appropriate, [R_Petname]!"
                            else: 
                                call RogueFace("angry", 1)
                                call Statup("Rogue", "Love", 90, -8)          
                                call Statup("Rogue", "Obed", 90, 6)            
                                call Statup("Rogue", "Inbt", 40, 3) 
                                ch_r "Not cool, [R_Petname]."
                            
                    else:                   #If this is the first kiss
                            if ApprovalCheck("Rogue", 750, "L", TabM=1):
                                call RogueFace("surprised", 1)
                                call Statup("Rogue", "Love", 70, 45)           
                                call Statup("Rogue", "Obed", 50, 20)
                                call Statup("Rogue", "Inbt", 50, 35)
                                ch_r "Hmmm, that was a pleasant suprise. . ."
                                call RogueFace("sexy")
                                ch_r "Maybe we should do that again, [R_Petname]."
                            elif ApprovalCheck("Rogue", 650, "L", TabM=1):
                                call RogueFace("surprised", 1)
                                call Statup("Rogue", "Love", 80, 30)           
                                call Statup("Rogue", "Obed", 50, 25)
                                call Statup("Rogue", "Inbt", 50, 35)
                                ch_r "Wha, what was that, [R_Petname]?"
                                ch_r "Hmm, not that it was entirely unpleasant. . ."
                            elif ApprovalCheck("Rogue", 500, "L", TabM=1):
                                call RogueFace("surprised", 1)            
                                call Statup("Rogue", "Obed", 70, 30)
                                call Statup("Rogue", "Inbt", 70, 35)
                                ch_r "Hey, what do you think you're doing, [R_Petname]?"
                            elif ApprovalCheck("Rogue", 700, TabM=1):
                                call RogueFace("angry", 1)
                                call Statup("Rogue", "Love", 60, -5) 
                                call Statup("Rogue", "Obed", 70, 40)
                                call Statup("Rogue", "Inbt", 70, 40)
                                ch_r "Wha, what the hell was that about?!"
                            else: 
                                call RogueFace("angry", 1)
                                call Statup("Rogue", "Love", 60, -15) 
                                call Statup("Rogue", "Obed", 70, 50)
                                call Statup("Rogue", "Inbt", 70, 40)
                                ch_r "Not cool, [R_Petname]."
                            
                    $ R_Kissed += 1            
                    $ R_Addict -= 1
                    $ R_Addictionrate += 1
                    $ R_Addictionrate = 3 if R_Addictionrate < 3 else R_Addictionrate 
                        
                    if ApprovalCheck("Rogue", 650, TabM=1):
                        if R_Love > R_Obed and R_Love > R_Inbt:
                            ch_r "Gimme some more sugar, [R_Petname]."
                        elif R_Obed > R_Inbt:
                            ch_r "Did you want to follow up on that?"
                        else:
                            ch_r "You'd best have a follow-up to that, [R_Petname]."
                        menu:
                            "Keep kissing?"
                            "You know it.":
                                call Statup("Rogue", "Lust", 60, 3)  
                                call Statup("Rogue", "Love", 90, 1)
                                call Statup("Rogue", "Love", 60, 3) 
                                call Statup("Rogue", "Inbt", 50, 2)
                                call Rogue_SexAct("kissing")
                                call Trig_Reset(1)
                                return
                            "Just a taste [[no].":
                                call RogueFace("bemused", 1) 
                                call Statup("Rogue", "Lust", 40, 1) 
                                call Statup("Rogue", "Lust", 60, 4) 
                                call Statup("Rogue", "Obed", 70, 2)
                                call Statup("Rogue", "Inbt", 50, 2)
                                ch_r "At some point I'm gonna need the whole mouthful, [R_Petname]."
                            "Nope.":
                                call RogueFace("angry", 1)
                                call Statup("Rogue", "Love", 80, -2) 
                                call Statup("Rogue", "Obed", 70, 3)
                                call Statup("Rogue", "Inbt", 50, 1)
                                ch_r "You're writing checks you can't cash, [R_Petname]."
                    else:
                        ch_r "Don't just plant one on a girl without ask'in first."
                    #end Kiss
                    
        "Hug her":                                                                                          #Hug her
                    if ApprovalCheck("Rogue", 200, TabM=1):        
                        "You lean over and wrap Rogue in a warm hug."
                    else:                
                        call RogueFace("angry", 1)
                        "You lean in with your arms wide, but Rogue grabs your shoulders and shoves you back."
                        ch_r "Hey, what're you doing, [R_Petname]?" 
                        return
                    if R_SEXP >= 30: 
                        call Statup("Rogue", "Lust", 60, 3) 
                        call Statup("Rogue", "Love", 90, 1)          
                        call Statup("Rogue", "Obed", 90, 3)            
                        call Statup("Rogue", "Inbt", 90, 3) 
                        call RogueFace("sexy")
                        ch_r "Hmm, are you hinting at something there, [R_Petname]?"
                    elif ApprovalCheck("Rogue", 600, "L", TabM=1):
                        call RogueFace("sexy")
                        call Statup("Rogue", "Love", 90, 1)          
                        call Statup("Rogue", "Obed", 40, 2)            
                        call Statup("Rogue", "Inbt", 30, 1) 
                        ch_r "Hmm, nice to see you too, [R_Petname]?"
                    elif ApprovalCheck("Rogue", 450, TabM=1):
                        call RogueFace("surprised", 1)
                        call Statup("Rogue", "Love", 90, 1)  
                        call Statup("Rogue", "Love", 70, 1)        
                        call Statup("Rogue", "Obed", 40, 2)            
                        call Statup("Rogue", "Inbt", 30, 1)  
                        ch_r "Hey, [R_Petname]. What's up?"
                    elif ApprovalCheck("Rogue", 350, TabM=1):
                        call RogueFace("angry", 1)  
                        call Statup("Rogue", "Love", 70, 1)        
                        call Statup("Rogue", "Obed", 50, 3)            
                        call Statup("Rogue", "Inbt", 30, 2) 
                        ch_r "I don't really know you that well."
                    else: 
                        call RogueFace("angry", 1)
                        call Statup("Rogue", "Love", 10, -1)  
                        call Statup("Rogue", "Love", 40, -1)         
                        call Statup("Rogue", "Obed", 20, 2)        
                        call Statup("Rogue", "Obed", 50, 2)            
                        call Statup("Rogue", "Inbt", 30, 2) 
                        ch_r "Had enough, [R_Petname]?"   
                        
        "Slap her ass" if R_Loc == bg_current:                                                              #Slap her ass
                    call R_Slap_Ass
            
        "Pinch her ass":                                                                                    #Pinch her ass
                    call RogueFace("surprised", 1)
                    if R_SEXP >= 5 and ApprovalCheck("Rogue", 600, TabM=1):        
                        "You come up to Rogue from behind and quickly pinch her butt."
                    else:                
                        "You come up to Rogue from behind and quickly pinch her butt."
                        call RogueFace("angry")
                        "She slaps your hand away and rounds on you."
                        ch_r "Hey, what're you doing, [R_Petname]?" 
                        return
                    if R_SEXP >= 20: 
                        call Statup("Rogue", "Lust", 60, 3) 
                        call Statup("Rogue", "Love", 90, 1)           
                        call Statup("Rogue", "Obed", 60, 2)          
                        call Statup("Rogue", "Obed", 90, 1)            
                        call Statup("Rogue", "Inbt", 50, 3) 
                        call RogueFace("sexy")
                        ch_r "Ooh! Are you hinting at something there, [R_Petname]?"
                    elif ApprovalCheck("Rogue", 800, "L", TabM=1):
                        call RogueFace("sexy")
                        call Statup("Rogue", "Love", 90, 1)           
                        call Statup("Rogue", "Obed", 60, 2)          
                        call Statup("Rogue", "Obed", 90, 1)            
                        call Statup("Rogue", "Inbt", 50, 2) 
                        ch_r "Hmm, nice to see you too, [R_Petname]?"
                    elif ApprovalCheck("Rogue", 900, TabM=1):
                        call RogueFace("surprised")
                        call Statup("Rogue", "Love", 90, 1)           
                        call Statup("Rogue", "Obed", 60, 3)          
                        call Statup("Rogue", "Obed", 90, 2)            
                        call Statup("Rogue", "Inbt", 50, 2) 
                        ch_r "Ooh! What's up?"
                    elif ApprovalCheck("Rogue", 800, TabM=1):
                        call RogueFace("angry")
                        call Statup("Rogue", "Love", 60, -3) 
                        call Statup("Rogue", "Love", 90, -1)           
                        call Statup("Rogue", "Obed", 60, 4)          
                        call Statup("Rogue", "Obed", 90, 3)            
                        call Statup("Rogue", "Inbt", 50, 2) 
                        ch_r "Hey, not cool."
                    else: 
                        call RogueFace("angry")
                        call Statup("Rogue", "Love", 60, -3) 
                        call Statup("Rogue", "Love", 90, -3)           
                        call Statup("Rogue", "Obed", 60, 5)          
                        call Statup("Rogue", "Obed", 90, 4)            
                        call Statup("Rogue", "Inbt", 50, 3)
                        ch_r "Ow! Lay off."  
                        #End pinch her ass
                    
        "Flip her skirt up" if R_Legs == "skirt" and not R_Upskirt:                                         #Flip her skirt           
                    call RogueFace("surprised", 1)
                    $ R_Upskirt = 1
                    pause 0.5            
                    $ R_Upskirt = 0
                    "You sneak up on Rogue from behind and flip her skirt up quickly!"
                    $ R_Upskirt = 0
                    if R_Panties and not Taboo:
                        if ApprovalCheck("Rogue", 750, "L", TabM=2):
                            call RogueFace("sexy", 1)
                            ch_r "Oh, naughty, [R_Petname]!"
                            call Statup("Rogue", "Love", 90, 3) 
                            ch_r "You could have just asked, you know. . ."
                        elif ApprovalCheck("Rogue", 650, "L", TabM=2):
                            call RogueFace("sexy", 1)
                            ch_r "Naughty naughty, [R_Petname]!"
                        elif ApprovalCheck("Rogue", 300, "I", TabM=1):
                            call RogueFace("sexy", 1)
                            ch_r "Hey, what do you think you're doing, [R_Petname]?"
                        elif ApprovalCheck("Rogue", 300, TabM=1):
                            call RogueFace("angry", 1)
                            call Statup("Rogue", "Love", 90, -3)           
                            call Statup("Rogue", "Obed", 80, 1)  
                            ch_r "Not cool, [R_Petname]!"
                        else: 
                            call RogueFace("angry", 1)
                            ch_r "What the fuck, [R_Petname]!"
                            call Statup("Rogue", "Love", 90, -5)          
                            call Statup("Rogue", "Obed", 80, 2)  
                            ch_r "That is not how you treat a lady!"
                        call Statup("Rogue", "Obed", 80, 5)             
                        call Statup("Rogue", "Inbt", 30, 2)           
                        call Statup("Rogue", "Inbt", 80, 3) 
                        $ R_SeenPanties = 1
                        
                    elif R_Panties: #panties on, but Taboo
                        if ApprovalCheck("Rogue", 750, "L") and ApprovalCheck("Rogue", 1300, TabM=2):
                            call RogueFace("sexy", 1)
                            ch_r "Oh, naughty, [R_Petname]!"
                            call Statup("Rogue", "Love", 90, 3) 
                            ch_r "You could have just asked, you know. . ."
                        elif ApprovalCheck("Rogue", 600, "L") and ApprovalCheck("Rogue", 1200, TabM=2):
                            call RogueFace("sexy", 1)
                            ch_r "[R_Petname]! A little warning!"
                        elif ApprovalCheck("Rogue", 600, "L"):
                            call RogueFace("angry", 1)
                            call Statup("Rogue", "Love", 90, -3)           
                            call Statup("Rogue", "Obed", 80, 3)  
                            ch_r "[R_Petname]! This isn't the time or place for this!"
                        elif ApprovalCheck("Rogue", 800, TabM=2):
                            call RogueFace("angry", 1)
                            call Statup("Rogue", "Love", 90, -5)           
                            call Statup("Rogue", "Obed", 80, 2)  
                            ch_r "Wha! [R_Petname]!"
                        else: 
                            call RogueFace("angry", 1)
                            ch_r "What the fuck, [R_Petname]!"
                            call Statup("Rogue", "Love", 90, -10)          
                            call Statup("Rogue", "Obed", 80, 2)           
                            call Statup("Rogue", "Inbt", 80, 1) 
                            ch_r "Why would you even do that in public?"
                        call Statup("Rogue", "Obed", 80, 7)             
                        call Statup("Rogue", "Inbt", 30, 3)           
                        call Statup("Rogue", "Inbt", 80, 3)
                        $ R_SeenPanties = 1
                        
                    elif not Taboo: #no panties, no taboo
                        if ApprovalCheck("Rogue", 850, "L"):
                            call RogueFace("sexy", 1)
                            ch_r "Oh, naughty, [R_Petname]!"
                            ch_r "You could have just asked, you know. . ."
                        elif ApprovalCheck("Rogue", 700, "L"):
                            call RogueFace("sexy", 1)
                            ch_r "[R_Petname]! A little warning!"
                        elif ApprovalCheck("Rogue", 600, "L"):
                            call RogueFace("bemused", 1)
                            call Statup("Rogue", "Love", 90, -3)           
                            call Statup("Rogue", "Obed", 80, 3)  
                            ch_r "Wha?! [R_Petname]? . . I don't usually. . ."
                        elif ApprovalCheck("Rogue", 500):
                            call RogueFace("angry", 1)
                            call Statup("Rogue", "Love", 90, -5)           
                            call Statup("Rogue", "Obed", 80, 2)  
                            ch_r "Wha! [R_Petname]!"
                        else: 
                            call RogueFace("angry", 1)
                            ch_r "What the fuck, [R_Petname]!"
                            call Statup("Rogue", "Love", 90, -10)          
                            call Statup("Rogue", "Obed", 80, 2)           
                            call Statup("Rogue", "Inbt", 80, 1) 
                            ch_r "I- I don't usually, you know. . ."  
                        call Statup("Rogue", "Obed", 80, 7)             
                        call Statup("Rogue", "Inbt", 30, 3)           
                        call Statup("Rogue", "Inbt", 80, 4)  
                        call Rogue_First_Bottomless 
                        
                    else: #no panties, taboo
                        if ApprovalCheck("Rogue", 850, "L") and ApprovalCheck("Rogue", 1500):
                            call RogueFace("sexy", 1)
                            ch_r "Oh, naughty, [R_Petname]!"
                            ch_r "You could have just asked, you know. . ."
                        elif ApprovalCheck("Rogue", 700, "L") and ApprovalCheck("Rogue", 1500):
                            call RogueFace("sexy", 1)
                            ch_r "[R_Petname]! A little warning!"
                        elif ApprovalCheck("Rogue", 700):
                            call RogueFace("bemused", 1)
                            call Statup("Rogue", "Love", 90, -3)           
                            call Statup("Rogue", "Obed", 80, 3)  
                            ch_r "[R_Petname]! This isn't the time or place for this!"
                        elif ApprovalCheck("Rogue", 1000):
                            call RogueFace("angry", 1)
                            call Statup("Rogue", "Love", 90, -5)           
                            call Statup("Rogue", "Obed", 80, 2)  
                            ch_r "Wha! [R_Petname]!"
                        else: 
                            call RogueFace("angry", 1)
                            ch_r "What the fuck, [R_Petname]!"
                            call Statup("Rogue", "Love", 90, -10)          
                            call Statup("Rogue", "Obed", 80, 2)           
                            call Statup("Rogue", "Inbt", 80, 1) 
                            ch_r "I- I don't usually, you know. . ." 
                        call Statup("Rogue", "Obed", 80, 7)             
                        call Statup("Rogue", "Inbt", 30, 4)           
                        call Statup("Rogue", "Inbt", 80, 4)  
                        call Rogue_First_Bottomless                  
                    call Statup("Rogue", "Lust", 60, 1) 
                    if "exhibitionist" in R_Traits:
                        call Statup("Rogue", "Lust", 200, 4) 
                    #End Flip her Skirt
                    
        "Grab her tit":                                                                                     #Grab her tit
                    call RogueFace("surprised", 1)
                    if R_SEXP >= 5 and ApprovalCheck("Rogue", 600, TabM=2):        
                        "You come up to Rogue and quickly honk her boob."
                    else:             
                        "You come up to Rogue and quickly honk her boob."
                        call RogueFace("angry")
                        show Rogue
                        with vpunch
                        "She slaps your hand away and smacks your face."
                        ch_r "What the fuck, [R_Petname]?" 
                        return
                    if R_SEXP >= 40: 
                        call Statup("Rogue", "Lust", 60, 5) 
                        call Statup("Rogue", "Love", 90, 2) 
                        call RogueFace("sexy")
                        ch_r "Ooh! Are you hinting at something there, [R_Petname]?"
                        $ Count = 10
                    elif ApprovalCheck("Rogue", 800, "L", TabM=1):
                        call RogueFace("sexy")
                        call Statup("Rogue", "Lust", 60, 2) 
                        call Statup("Rogue", "Love", 90, 1) 
                        ch_r "Hmm, hand to my heart, [R_Petname]?"
                        $ Count = 7
                    elif ApprovalCheck("Rogue", 1000, TabM=1):
                        call RogueFace("perplexed")  
                        call Statup("Rogue", "Lust", 60, 1)         
                        ch_r "Oh! A little handsy, eh [R_Petname]?"                    
                        $ Count = 5
                    elif ApprovalCheck("Rogue", 800, TabM=1):
                        call RogueFace("angry")
                        call Statup("Rogue", "Love", 90, -3)          
                        call Statup("Rogue", "Obed", 90, 4)            
                        call Statup("Rogue", "Inbt", 90, 3) 
                        ch_r "You seem to have misplaced something. . ."
                        $ Count = 3
                    else: 
                        call RogueFace("angry")
                        call Statup("Rogue", "Love", 90, -5)          
                        call Statup("Rogue", "Obed", 90, 5)            
                        call Statup("Rogue", "Inbt", 90, 3) 
                        ch_r "Move it or lose it, [R_Petname]." 
                        $ Count = 2
                              
                    call Statup("Rogue", "Obed", 70, 3)            
                    call Statup("Rogue", "Inbt", 70, 2) 
                    ch_r "Um, are you going to let go?"
                    while Count > 0:
                        if Count == 6:
                            call RogueFace("sexy", 1)
                            ch_r "Hmmm, maybe do keep at it. . ."  
                            call Statup("Rogue", "Lust", 90, 2)       
                            call Statup("Rogue", "Inbt", 70, 1)
                        elif Count == 3:
                            call RogueFace("perplexed")
                            call Statup("Rogue", "Lust", 90, 1) 
                            ch_r "That's nice [R_Petname], but maybe cut it out?"
                        elif Count == 2:
                            call RogueFace("angry")
                            call Statup("Rogue", "Love", 90, -1) 
                            ch_r "Ok, stop it right now."
                        elif Count == 1:
                            call RogueFace("angry")
                            ch_r "Back the hell off, [R_Petname]!"
                            call Statup("Rogue", "Love", 90, -5) 
                            show Rogue
                            with vpunch
                            "She slaps your hand away and smacks your face."
                            ch_r "What the fuck, [R_Petname]?" 
                            $ Count = 1                     
                        $ Count -= 1 if Count >= 0 else 0
                            
                        if Count > 0:
                            menu:
                                "Your hand is still on her chest."
                                "Let go immediately":
                                    if Count >= 7:
                                        ch_r "Aw, can't say I'm not a {i}little{/i} disappointed. . ."  
                                        call Statup("Rogue", "Lust", 60, 2)         
                                        call Statup("Rogue", "Inbt", 70, 1) 
                                    elif Count <= 4:
                                        ch_r "Smart move."
                                    $ Count = 0
                                    
                                "Honk it again and let go":
                                    if Count >= 7:
                                        ch_r "Heh, can't say I'm not a {i}little{/i} disappointed. . ."            
                                        call Statup("Rogue", "Lust", 60, 4) 
                                        call Statup("Rogue", "Inbt", 70, 1)
                                    elif Count >= 4:
                                        ch_r "Classy, [R_Petname]."
                                    else:
                                        call RogueFace("angry")
                                        ch_r "Dick move."
                                    call Statup("Rogue", "Obed", 70, 3)            
                                    call Statup("Rogue", "Inbt", 70, 2)
                                    $ Count = 0 
                                        
                                "Fondle it a little":                            
                                    if R_FondleB and ApprovalCheck("Rogue", 1000, TabM=2):                                
                                        call RogueFace("sexy",1)
                                        $ R_Eyes = "closed"
                                        call Statup("Rogue", "Lust", 90, 5) 
                                    else:
                                        call RogueFace("perplexed")
                                        call Statup("Rogue", "Lust", 90, 2) 
                                        $ Count -= 1
                                    call Statup("Rogue", "Obed", 70, 4)            
                                    call Statup("Rogue", "Inbt", 70, 2)
                                    ch_r "Umm. . ."
                                    
                                "Just leave it there.":
                                    if Count == 5:
                                        call RogueFace("perplexed")
                                        call Statup("Rogue", "Lust", 90, 3) 
                                        ch_r "This is a bit odd."                            
                                    elif Count == 2:
                                        call RogueFace("perplexed")
                                        call Statup("Rogue", "Lust", 90, 1) 
                                        ch_r "This is getting a bit uncomfortable."
                                    call Statup("Rogue", "Obed", 70, 2)            
                                    call Statup("Rogue", "Inbt", 70, 1)
                                    
                            
                    
                    if R_FondleB and ApprovalCheck("Rogue", 1100, TabM = 3): 
                        call RogueFace("sexy", 1)
                        ch_r "You know, maybe we could keep this party roll'in. . ."
                        menu:
                            extend ""
                            "Yeah!":
                                call Statup("Rogue", "Lust", 60, 5) 
                                call Statup("Rogue", "Love", 90, 2)          
                                call Statup("Rogue", "Obed", 60, 3)            
                                call Statup("Rogue", "Inbt", 60, 3) 
                                call Rogue_SexAct("breasts")
                                call Trig_Reset(1)
                                return
                            "Nah, that was enough.":
                                call RogueFace("sad", 1)
                                call Statup("Rogue", "Lust", 60, 2) 
                                call Statup("Rogue", "Love", 90, -1)          
                                call Statup("Rogue", "Obed", 60, 4)            
                                call Statup("Rogue", "Inbt", 60, 3) 
                                ch_r "Whatever."
                    elif ApprovalCheck("Rogue", 800, TabM = 3):  
                        $ R_Brows = "confused"
                        $ R_Eyes = "sexy"
                        $ R_Mouth = "smile"
                        ch_r "Was that fun for you?"
                    elif ApprovalCheck("Rogue", 800): 
                        call RogueFace("angry", 1)
                        ch_r "I can't believe you'd do that in public!"
                    else:
                        call RogueFace("angry", 1)
                        ch_r "Just, don't do that sort of thing again!"
                    #End Grab her tit
                        
                
        "Rub her shoulders":                                                                                #Rub her shoulders
                    "You come up to Rogue from behind and gently rub her shoulders."
                    if R_SEXP >= 30:
                        call RogueFace("sexy") 
                        call Statup("Rogue", "Lust", 60, 3) 
                        call Statup("Rogue", "Love", 90, 2)
                        "She leans back into your hands"
                        ch_r "Hmm, are you hinting at something there, [R_Petname]?"
                    elif ApprovalCheck("Rogue", 600, "L"):
                        call RogueFace("sexy")
                        call Statup("Rogue", "Lust", 60, 1) 
                        call Statup("Rogue", "Love", 90, 2)
                        ch_r "Hmm, that feels nice, [R_Petname]."
                    elif ApprovalCheck("Rogue", 450):
                        call RogueFace("surprised", 1)
                        call Statup("Rogue", "Love", 90, 1)
                        ch_r "Oh, hey, [R_Petname]. What's up?"
                    elif ApprovalCheck("Rogue", 350):
                        call RogueFace("angry", 1)
                        call Statup("Rogue", "Love", 90, -1)
                        if Taboo:
                            ch_r "Hey, um, ease up on the PDAs there, [R_Petname]."
                        else:
                            ch_r "Whoa, um, give me some space here."
                    else: 
                        call RogueFace("angry", 1)
                        "She slaps your hands away."
                        ch_r "Not really the time or place, [R_Petname]?"           
                    call Statup("Rogue", "Obed", 30, 3)            
                    call Statup("Rogue", "Inbt", 30, 2) 
        
        "Ask for her panties":
                    call Rogue_AskPanties
                                            
        "Never mind [[exit]":
                    $ R_Chat[5] = 0 
            
    return
    
#End flirt core menu.


label Rogue_AskPanties(Store = 0):
    $ Store = Tempmod  
    $ Line = 0
    if not R_Panties or R_Panties == "shorts":
        if ApprovalCheck("Rogue", 900):
            call RogueFace("sexy", 1)
            call Statup("Rogue", "Lust", 80, 5) 
            call Statup("Rogue", "Lust", 60, 5) 
            call Statup("Rogue", "Lust", 40, 10)            
            call Statup("Rogue", "Inbt", 60, 5)            
            call Statup("Rogue", "Inbt", 30, 10) 
            ch_r "I'm not wearing any."
        elif R_Over == "towel" or not R_Legs:
            call RogueFace("bemused", 2)
            ch_r "I think you can see I can't."            
        else:
            call RogueFace("bemused", 2, Eyes="side")
            call Statup("Rogue", "Lust", 80, 5) 
            call Statup("Rogue", "Lust", 60, 5) 
            call Statup("Rogue", "Lust", 40, 10)            
            call Statup("Rogue", "Inbt", 60, 5)  
            ch_r "I definitely have some on, but you can't have them."  
                        
    else:
        if R_SeenPussy and ApprovalCheck("Rogue", 500): #You've seen her Pussy.
            $ Tempmod += 15
        elif R_SeenPanties and ApprovalCheck("Rogue", 500): #You've seen her panties.
            $ Tempmod += 5 
        if "exhibitionist" in R_Traits:
            $ Tempmod += (Taboo * 5)
        if "dating" in R_Traits or "sex friend" in R_Petnames and not Taboo:
            $ Tempmod += 10
        if "no bottomless" in R_RecentActions: 
            $ Tempmod -= 20
        
        $ Line = 0
        if R_Legs == "pants" or HoseNum("Rogue") >= 10: 
            if ApprovalCheck("Rogue", 1000, "OI", TabM = 5) or "exhibitionist" in R_Traits:   
                $ Line = "here"
            elif ApprovalCheck("Rogue", 900, TabM = 5):
                $ Line = "change"
                
        elif R_Legs == "skirt":
            if ApprovalCheck("Rogue", 600, "OI", TabM = 5) or "exhibitionist" in R_Traits:   
                $ Line = "here"
            elif ApprovalCheck("Rogue", 1100, TabM = 5):
                $ Line = "change"
                
        else:
            if ApprovalCheck("Rogue", 1200, TabM = 5) or "exhibitionist" in R_Traits:
                $ Line = "here"
        
        
        if Line == "here":                              #She's agreed to change and will do it here
                call RogueFace("sly")                          
                if R_Legs == "skirt":      
                    call Statup("Rogue", "Obed", 60, 4)            
                    call Statup("Rogue", "Inbt", 60, 4)
                else: #no pants or skirt         
                    call Statup("Rogue", "Obed", 60, 6)            
                    call Statup("Rogue", "Inbt", 60, 6) 
                
                call Statup("Rogue", "Lust", 60, 5)    
                call Remove_Panties("Rogue")
                    
                if Taboo:
                    call Statup("Rogue", "Lust", 60, 5) 
                    if "exhibitionist" in R_Traits: 
                        call Statup("Rogue", "Lust", 80, 5)
                        call Statup("Rogue", "Lust", 200, 5)    
                    call Statup("Rogue", "Obed", 80, 10)            
                    call Statup("Rogue", "Inbt", 80, 10)        
            
        elif Line:                                      #She's agreed to change, but leaves the room to do it.
                if not Taboo:                           #If it's in one of your rooms                                    
                    call RogueFace("bemused", 1) 
                    menu:
                        ch_r "Could you head out for a 'sec while I change?"
                        "OK.": 
                            call Statup("Rogue", "Love", 90, 5) 
                            call RogueFace("smile", 1)                                             
                            ch_r "I 'preciate it, [R_Petname]."
                            call RogueFace("sly", 1) 
                            call Statup("Rogue", "Lust", 60, 2)         
                            call Statup("Rogue", "Obed", 60, 4)            
                            call Statup("Rogue", "Inbt", 60, 4)
                            show blackscreen onlayer black 
                            "You exit the room for a minute"                                
                            hide blackscreen onlayer black 
                            $ R_DailyActions.append("pantyless")
                            call RogueOutfit
                            if Taboo:              
                                call Quick_Taboo("Rogue")
                            "When you return, she quietly hands you her balled up panties."
                            $ Line = 0
                            
                        "And miss the show?":
                            if ApprovalCheck("Rogue", 1000, "LI"): 
                                call Statup("Rogue", "Lust", 70, 5)          
                                call Statup("Rogue", "Obed", 60, 5)            
                                call Statup("Rogue", "Inbt", 60, 5) 
                                call RogueFace("sly", 1) 
                                ch_r "Ok, fine."
                            else:                 
                                call RogueFace("angry", 1) 
                                call Statup("Rogue", "Love", 90, -5)          
                                call Statup("Rogue", "Obed", 60, -3)            
                                call Statup("Rogue", "Inbt", 60, 5) 
                                ch_r "Then I guess there'll be no show to see, [R_Petname]."
                                $ Line = 0
                                
                        "Nope, I'm staying.":
                            if ApprovalCheck("Rogue", 600, "OI"): 
                                call RogueFace("perplexed", 1) 
                                call Statup("Rogue", "Lust", 70, 5)          
                                call Statup("Rogue", "Obed", 60, 10)            
                                call Statup("Rogue", "Inbt", 60, 5) 
                                ch_r "If you insist."
                                call RogueFace("normal") 
                            else:        
                                call RogueFace("angry", 1) 
                                call Statup("Rogue", "Love", 90, -10)          
                                call Statup("Rogue", "Obed", 60, -5)            
                                call Statup("Rogue", "Inbt", 60, 5) 
                                ch_r "Then I guess I'm not doing anything."
                                $ Line = 0
                                
                    if Line:                                            #She agreed to stay  
                                call RogueFace("sly", 1) 
                                if R_Legs == "pants" or HoseNum("Rogue") >= 10:   
                                        call Statup("Rogue", "Lust", 60, 5)         
                                        call Statup("Rogue", "Obed", 60, 5)            
                                        call Statup("Rogue", "Inbt", 60, 5)   
                                elif R_Legs == "skirt":
                                        call Statup("Rogue", "Lust", 60, 5)         
                                        call Statup("Rogue", "Obed", 60, 4)            
                                        call Statup("Rogue", "Inbt", 60, 4) 
                                        
                                call Remove_Panties("Rogue") 
                                

                else:                                   #if she's not in one of your rooms
                    call RogueFace("sly", 1) 
                    call Statup("Rogue", "Lust", 60, 2)         
                    call Statup("Rogue", "Obed", 60, 4)            
                    call Statup("Rogue", "Inbt", 60, 4)
                    $ R_Loc = "hold"
                    call Set_The_Scene
                    "Rogue nods and leaves for a minute." 
                    $ R_DailyActions.append("pantyless")
                    call RogueOutfit
                    if Taboo:              
                        call Quick_Taboo("Rogue")
                    $ R_Loc = bg_current
                    call Set_The_Scene
                    "She returns and quietly hands you her balled up panties."
                                        
            
        else:                                           #She refuses.    
            call RogueFace("angry", 2)                        
            if not ApprovalCheck("Rogue", 500):
                call Statup("Rogue", "Lust", 60, 5) 
                call Statup("Rogue", "Love", 90, -10)          
                call Statup("Rogue", "Obed", 60, 3)            
                call Statup("Rogue", "Inbt", 60, 3) 
                ch_r "I can't believe you would even ask me something like that!"
                $ R_RecentActions.append("angry")
                $ R_DailyActions.append("angry")   
                
            elif not ApprovalCheck("Rogue", 500, TabM = 5):
                call Statup("Rogue", "Lust", 60, 5) 
                call Statup("Rogue", "Love", 90, -5)          
                call Statup("Rogue", "Obed", 60, 5)            
                call Statup("Rogue", "Inbt", 60, 5) 
                ch_r "I can't believe you would even ask me that here!"                                
                $ R_RecentActions.append("angry")
                $ R_DailyActions.append("angry")   
                
            else:
                call RogueFace("bemused", 2)
                call Statup("Rogue", "Lust", 60, 3)            
                call Statup("Rogue", "Inbt", 60, 1)
                if Taboo:            
                    call Statup("Rogue", "Inbt", 60, 2)
                    if R_Love >= R_Inbt or R_Obed >= R_Inbt:
                        ch_r "I'm sorry, [R_Petname], not around here."
                    else:       
                        call Statup("Rogue", "Obed", 60, -2)    
                        ch_r "Nah, not around here, at least."
                else:
                    if R_Love >= R_Inbt or R_Obed >= R_Inbt:
                        ch_r "I'm sorry, [R_Petname], I'm not ready yet."
                    else:
                        call RogueFace("perplexed")       
                        call Statup("Rogue", "Obed", 60, -2)    
                        ch_r "Nah, not around you, at least."    
            $ R_Blush = 1
                
                    
            
    $ Tempmod = Store       
    $ Line = 0
    return
    
    
    
       
label Remove_Panties(chr = "Rogue", Store = 0, Store2 = 0):
    if chr == "Rogue":
                $ Store = R_Legs
                $ Store2 = R_Hose
                
                if R_Legs == "pants":    
                    $ R_Legs = 0        
                if R_Legs == "skirt": 
                    $ R_Upskirt = 1
                if HoseNum("Rogue") >= 5:
                    $ R_Hose = 0        
                $ R_Panties = 0  
                    
                if Taboo:
                        if Store == "pants":
                            "Rogue looks around, but pulls her pants clean off and her panties with them."
                        elif Store == "skirt" and Store2 != R_Hose:
                            "Rogue looks around, hikes up her skirt, pulls her [Store2] clean off and her panties with them."
                        elif Store == "skirt":               
                            "Rogue looks around, reaches under her skirt, and pulls her panties down."
                        elif Store2 != R_Hose:  
                            "Rogue looks around, but pulls her [Store2] clean off and her panties with them." 
                        else:
                            "Rogue looks around, and pulls her panties down."                             
                else: #Not Taboo
                        if Store == "pants":
                            "Rogue glances at you and pulls her pants clean off and her panties with them."
                        elif Store == "skirt" and Store2 != R_Hose:
                            "Rogue glances at you, hikes up her skirt, pulls her [Store2] clean off and her panties with them."
                        elif Store == "skirt":
                            "Rogue glances at you, reaches under her skirt, and pulls her panties down."
                        elif Store2 != R_Hose:
                            "Rogue glances at you and pulls her [Store2] clean off and her panties with them."
                        else:                            
                            "Rogue glances at you and pulls her panties off."
                        
                $ R_Legs = Store  
                $ R_Hose = Store2      
                if R_Legs == "pants":
                    "She hands you the panties and then pulls her pants back on."
                elif R_Legs == "skirt" and HoseNum("Rogue") >= 5:
                    "She hands you the panties and then pulls her [R_Hose] back on and her skirt back down."  
                    $ R_Upskirt = 0
                elif R_Legs == "skirt":        
                    "She hands you the panties and then pulls her skirt back down."  
                    $ R_Upskirt = 0    
                elif HoseNum("Rogue") >= 5:
                    "She hands you the panties and then pulls her [R_Hose] back on."  
                else:
                    "Rogue hands them to you in a ball." 
                
                call Rogue_First_Bottomless(1) 
                $ R_DailyActions.append("pantyless")
                call RogueOutfit
                if Taboo:              
                    call Quick_Taboo("Rogue")
    # End Rogue's options
    
    elif chr == "Kitty":    
        
                $ Store = K_Legs
                $ Store2 = K_Hose
                
                $ K_Panties = 0  
                    
                call KittyFace("bemused") 
                if Store == "pants":
                    "Kitty looks around, reaches into her pocket, and tugs her panties out."
                elif Store == "skirt":               
                    "Kitty looks around, reaches into her skirt, and pulls her panties out."
                elif Store2 != K_Hose:  
                    "Kitty looks around, reaches through her hose, and pulls her panties out." 
                else:
                    "Kitty looks around and pulls her panties off."
                    
                call KittyFace("sexy") 
                "She hands them to you with a smirk." 
                
                if not K_Legs and HoseNum("Kitty") <= 5:
                        call Kitty_First_Bottomless(1) 
                $ K_DailyActions.append("pantyless")
                call KittyOutfit
                if Taboo:              
                    call Quick_Taboo("Kitty")
                                        
    # End Kitty's options
    
    elif chr == "Emma":
                $ Store = E_Legs
                $ Store2 = E_Hose
                
                if E_Legs == "pants" or E_Legs == "yoga pants":    
                    $ E_Legs = 0        
                if E_Legs == "skirt": 
                    $ E_Upskirt = 1
                if HoseNum("Emma") >= 5:
                    $ E_Hose = 0        
                $ E_Panties = 0  
                    
                if Taboo:
                        if Store == "pants" or E_Legs == "yoga pants":
                            "Emma looks around, but pulls her pants clean off and her panties with them."
                        elif Store == "skirt" and Store2 != E_Hose:
                            "Emma looks around, hikes up her skirt, pulls her [Store2] clean off and her panties with them."
                        elif Store == "skirt":               
                            "Emma looks around, reaches under her skirt, and pulls her panties down."
                        elif Store2 != E_Hose:  
                            "Emma looks around, but pulls her [Store2] clean off and her panties with them." 
                        else:  
                            "Emma looks around, but pulls her panties off." 
                else: #Not Taboo
                        if Store == "pants" or E_Legs == "yoga pants":
                            "Emma glances at you and pulls her pants clean off and her panties with them."
                        elif Store == "skirt" and Store2 != E_Hose:
                            "Emma glances at you, hikes up her skirt, pulls her [Store2] clean off and her panties with them."
                        elif Store == "skirt":
                            "Emma glances at you, reaches under her skirt, and pulls her panties down."
                        elif Store2 != E_Hose:
                            "Emma glances at you and pulls her [Store2] clean off and her panties with them."
                        else:
                            "Emma glances at you and pulls her panties off."
                        
                $ E_Legs = Store  
                $ E_Hose = Store2      
                if E_Legs == "pants" or E_Legs == "yoga pants":
                    "She hands you the panties and then pulls her pants back on."
                elif E_Legs == "skirt" and HoseNum("Emma") >= 5:
                    "She hands you the panties and then pulls her [E_Hose] back on and her skirt back down."  
                    $ E_Upskirt = 0
                elif E_Legs == "skirt":        
                    "She hands you the panties and then pulls her skirt back down."  
                    $ E_Upskirt = 0    
                elif HoseNum("Emma") >= 5:
                    "She hands you the panties and then pulls her [E_Hose] back on."  
                else:
                    "Emma hands them to you in a ball." 
                
                call Emma_First_Bottomless(1) 
                $ E_DailyActions.append("pantyless")
                call EmmaOutfit
                if Taboo:              
                    call Quick_Taboo("Emma")
    # End Emma's options
    elif chr == "Laura":
                $ Store = L_Legs
                $ Store2 = L_Hose
                
                if L_Legs == "pants" or L_Legs == "yoga pants":    
                    $ L_Legs = 0        
                if L_Legs == "skirt": 
                    $ L_Upskirt = 1
                if HoseNum("Laura") >= 5:
                    $ L_Hose = 0        
                $ L_Panties = 0  
                    
                if Taboo:
                        if Store == "pants" or L_Legs == "yoga pants":
                            "Laura looks around, but pulls her pants clean off and her panties with them."
                        elif Store == "skirt" and Store2 != L_Hose:
                            "Laura looks around, hikes up her skirt, pulls her [Store2] clean off and her panties with them."
                        elif Store == "skirt":               
                            "Laura looks around, reaches under her skirt, and pulls her panties down."
                        elif Store2 != L_Hose:  
                            "Laura looks around, but pulls her [Store2] clean off and her panties with them." 
                        else:  
                            "Laura looks around, but pulls her panties off." 
                else: #Not Taboo
                        if Store == "pants" or L_Legs == "yoga pants":
                            "Laura glances at you and pulls her pants clean off and her panties with them."
                        elif Store == "skirt" and Store2 != L_Hose:
                            "Laura glances at you, hikes up her skirt, pulls her [Store2] clean off and her panties with them."
                        elif Store == "skirt":
                            "Laura glances at you, reaches under her skirt, and pulls her panties down."
                        elif Store2 != L_Hose:
                            "Laura glances at you and pulls her [Store2] clean off and her panties with them."
                        else:
                            "Laura glances at you and pulls her panties off."
                        
                $ L_Legs = Store  
                $ L_Hose = Store2      
                if L_Legs == "pants" or L_Legs == "yoga pants":
                    "She hands you the panties and then pulls her pants back on."
                elif L_Legs == "skirt" and HoseNum("Laura") >= 5:
                    "She hands you the panties and then pulls her [L_Hose] back on and her skirt back down."  
                    $ L_Upskirt = 0
                elif L_Legs == "skirt":        
                    "She hands you the panties and then pulls her skirt back down."  
                    $ L_Upskirt = 0    
                elif HoseNum("Laura") >= 5:
                    "She hands you the panties and then pulls her [L_Hose] back on."  
                else:
                    "Laura hands them to you in a ball." 
                
                call Laura_First_Bottomless(1) 
                $ L_DailyActions.append("pantyless")
                call LauraOutfit
                if Taboo:              
                    call Quick_Taboo("Laura")
    # End Laura's options
    
    return
    # End Ask for Panties //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //
    
    
# Rogue Control interface //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //
label Rogue_Controls:
    menu:
        "I'd like you to call me something else":
            call Rogue_Names            
            return
        "I'd like you to come over for some action." if R_Loc != bg_current:
            ch_r "Ok, I'll be right over."
            $ R_Loc = bg_current 
            call Set_The_Scene
            call Rogue_SexMenu
            return
        "I'd like to get busy." if R_Loc == bg_current:
            ch_r "Hmmm, what did you have in mind?"
            call Rogue_SexMenu
            return
        "I want you to stop taking your own initiative." if "sub" not in R_Traits:
            $ R_Traits.append("sub")
            ch_r "Very well, I will only do as ordered from now on."           
        "You can take your own initiative if you like." if "sub" in R_Traits:
            $ R_Traits.remove("sub")
            ch_r "Great, I'll do that."   
        "Exit.":
            return
    jump Rogue_Controls
return

# start Rogue_Gifts//////////////////////////////////////////////////////////
label Rogue_Gifts:  
    if not P_Inventory:
        "You don't have anything to give her."
        return
    menu:
        "What would you like to give her?"
        "Toys and Books":
            menu:
                "Give her a dildo." if "dildo" in P_Inventory: 
                    #If you have a Dildo, you'll give it.
                    $ Count = R_Inventory.count("dildo")
                    if "dildo" not in R_Inventory:                            
                        "You give Rogue the dildo."
                        $ R_Blush = 1
                        $ Rogue_Arms = 2
                        $ R_Held = "dildo"
                        if ApprovalCheck("Rogue", 800):                    
                            call RogueFace("bemused")
                            $ P_Inventory.remove("dildo")
                            $ R_Inventory.append("dildo")
                            call Statup("Rogue", "Love", 200, 30)
                            call Statup("Rogue", "Obed", 200, 30)
                            call Statup("Rogue", "Inbt", 200, 30)
                            ch_r "Well, I've got some ideas in mind for this. . ."
                            call Statup("Rogue", "Lust", 89, 10)
                        elif ApprovalCheck("Rogue", 500):
                            call RogueFace("confused")
                            $ P_Inventory.remove("dildo")
                            $ R_Inventory.append("dildo")
                            call Statup("Rogue", "Love", 200, 10)
                            call Statup("Rogue", "Obed", 200, 10)
                            call Statup("Rogue", "Inbt", 200, 10)
                            ch_r "Huh, well I guess I can find a place for it. . ."  
                            call Statup("Rogue", "Lust", 89, 10)
                            call RogueFace("surprised")
                            ch_r "I- I mean. . . I'll just put it away."
                            call RogueFace("bemused")
                        elif "offered gift" in R_DailyActions:
                            call RogueFace("angry")
                            "She hands it back to you."
                            ch_r "Look, maybe you should just rethink your gift-giving choices?"                    
                        else:
                            call RogueFace("angry")
                            call Statup("Rogue", "Love", 50, -20)
                            call Statup("Rogue", "Obed", 20, 10)
                            call Statup("Rogue", "Inbt", 20, 20)                    
                            ch_r "That's a pretty forward gift to be giving a lady. . ."                     
                            call Statup("Rogue", "Lust", 89, 5)
                            "She hands it back to you."
                            $ R_DailyActions.append("offered gift") 
                    elif Count == 1:
                        ch_r "Well, I suppose I could always use another. . ."
                    else: 
                        ch_r "Honestly, [R_Petname], I already have enough of those."
                    $ R_Held = 0
                    $ Rogue_Arms = 2
                    
                "Give her the vibrator." if "vibrator" in P_Inventory: 
                    #If you have a vibrator, you'll give it.
                    if "vibrator" not in R_Inventory:                            
                        "You give Rogue the Shocker Vibrator."
                        $ R_Blush = 1
                        $ Rogue_Arms = 2
                        $ R_Held = "vibrator"
                        if ApprovalCheck("Rogue", 700):                    
                            call RogueFace("bemused")
                            $ P_Inventory.remove("vibrator")
                            $ R_Inventory.append("vibrator")
                            call Statup("Rogue", "Love", 200, 30)
                            call Statup("Rogue", "Obed", 200, 30)
                            call Statup("Rogue", "Inbt", 200, 30)
                            ch_r "Well, I've got some ideas in mind for this. . ."
                            call Statup("Rogue", "Lust", 89, 10)
                        elif ApprovalCheck("Rogue", 400):
                            call RogueFace("confused")
                            $ P_Inventory.remove("vibrator")
                            $ R_Inventory.append("vibrator")
                            call Statup("Rogue", "Love", 200, 10)
                            call Statup("Rogue", "Obed", 200, 10)
                            call Statup("Rogue", "Inbt", 200, 10)
                            ch_r "I guess I can use this to work the kinks out. . ."  
                            call Statup("Rogue", "Lust", 89, 10)
                            call RogueFace("surprised")
                            ch_r "Muscle knots, I mean!"
                            call RogueFace("bemused", 1)
                        elif "offered gift" in R_DailyActions:
                            call RogueFace("angry")
                            "She hands it back to you."
                            ch_r "Look, maybe you should just rethink your gift-giving choices?"    
                        else:
                            call RogueFace("angry")
                            call Statup("Rogue", "Love", 50, -20)
                            call Statup("Rogue", "Obed", 20, 10)
                            call Statup("Rogue", "Inbt", 20, 20)                    
                            ch_r "I don't think I have much use for that."                     
                            call Statup("Rogue", "Lust", 89, 5)
                            "She hands it back to you."
                            $ R_DailyActions.append("offered gift") 
                    else: 
                        ch_r "[R_Petname], I only need the one."
                    $ R_Held = 0
                    $ Rogue_Arms = 2
                "Give her the \"Dazzler and Longshot\" book." if "Dazzler and Longshot" in P_Inventory: 
                    #If you have a vibrator, you'll give it.
                    if "Dazzler and Longshot" not in R_Inventory:                            
                        "You give Rogue the book."
                        $ R_Blush = 1
                        if ApprovalCheck("Rogue", 600, "L"):                    
                            call RogueFace("smile")
                            ch_r "Oh, I've heard of this one, very romantic!"
                            call Statup("Rogue", "Lust", 89, 10)
                        else:
                            call RogueFace("confused")
                            ch_r "Hmph, well I guess i've heard good things about it, I'll give it a shot."  
                            call RogueFace("bemused")       
                        $ P_Inventory.remove("Dazzler and Longshot")
                        $ R_Inventory.append("Dazzler and Longshot") 
                        call Statup("Rogue", "Love", 200, 150) 
                        if R_Love >= 1000:
                            $ R_Love = 1000
                    else: 
                        ch_r "I already have one of those."                
                    
                "Give her the \"256 Shades of Grey\" book." if "256 Shades of Grey" in P_Inventory: 
                    #If you have a book, you'll give it.
                    if "256 Shades of Grey" not in R_Inventory:                            
                        "You give Rogue the book."
                        $ R_Blush = 1
                        if ApprovalCheck("Rogue", 500, "O"):                    
                            call RogueFace("bemused")
                            ch_r "I'll research it thoroughly."
                            call Statup("Rogue", "Lust", 89, 10)
                        else:
                            call RogueFace("confused") 
                            ch_r "Hmm, I have heard some good things about this one. I'll give it a quick read."  
                            call RogueFace("bemused")             
                        $ P_Inventory.remove("256 Shades of Grey")
                        $ R_Inventory.append("256 Shades of Grey")                    
                        call Statup("Rogue", "Obed", 200, 150)  
                        if R_Obed >= 1000:
                            $ R_Obed = 1000
                    else: 
                        ch_r "I already have one of those."                
                    
                "Give her the \"Avengers Tower Penthouse\" book." if "Avengers Tower Penthouse" in P_Inventory: 
                    #If you have a book, you'll give it.
                    if "Avengers Tower Penthouse" not in R_Inventory:                            
                        "You give Rogue the book."
                        $ R_Blush = 1
                        if ApprovalCheck("Rogue", 500, "I"):                    
                            call RogueFace("bemused")
                            ch_r "Oh. . . I think I can work with this. . ."
                            call Statup("Rogue", "Lust", 89, 10)
                        else:
                            call RogueFace("confused")
                            ch_r "Well. . . this is a bit. . . I think I'll keep this for research."  
                            call RogueFace("bemused")               
                        $ P_Inventory.remove("Avengers Tower Penthouse")
                        $ R_Inventory.append("Avengers Tower Penthouse")                    
                        call Statup("Rogue", "Inbt", 200, 150)  
                        if R_Inbt >= 1000:
                            $ R_Inbt = 1000
                    else: 
                        ch_r "I already have one of those." 
            
                "Never mind":
                    pass
        "Clothing":    
            menu:
                "Give her the green nighty." if "r nighty" in P_Inventory: 
                    #If you have a nighty, you'll give it.
                    if "nighty" not in R_Inventory:                            
                        "You give Rogue the nighty."
                        $ R_Blush = 1
                        if ApprovalCheck("Rogue", 600):                    
                            call RogueFace("bemused")
                            $ P_Inventory.remove("r nighty")
                            $ R_Inventory.append("nighty")
                            call Statup("Rogue", "Love", 200, 40)
                            call Statup("Rogue", "Obed", 200, 20)
                            call Statup("Rogue", "Inbt", 200, 30)
                            ch_r "I bet I'd look good in this. . ."
                            call Statup("Rogue", "Lust", 89, 10)
                        else:
                            call RogueFace("confused")
                            $ P_Inventory.remove("r nighty")
                            $ R_Inventory.append("nighty")
                            call Statup("Rogue", "Love", 200, 30)
                            call Statup("Rogue", "Obed", 200, 20)
                            call Statup("Rogue", "Inbt", 200, 20)
                            ch_r "Well, it's a little revealing, but still pretty cute."  
                            call RogueFace("bemused")
                    else: 
                        ch_r "I already have one of those."                
                    
                "Give her the lace bra." if "r lace bra" in P_Inventory: 
                    #If you have a bra, you'll give it.
                    if "lace bra" not in R_Inventory:                            
                        "You give Rogue the lace bra."
                        $ R_Blush = 1
                        if ApprovalCheck("Rogue", 1000):                    
                            call RogueFace("bemused")
                            $ P_Inventory.remove("r lace bra")
                            $ R_Inventory.append("lace bra")
                            call Statup("Rogue", "Love", 200, 30)
                            call Statup("Rogue", "Obed", 200, 20)
                            call Statup("Rogue", "Inbt", 200, 30)
                            ch_r "Hmm, this really shows off the assets. . ."
                            call Statup("Rogue", "Lust", 89, 10)
                        elif ApprovalCheck("Rogue", 700):
                            call RogueFace("confused")
                            $ P_Inventory.remove("r lace bra")
                            $ R_Inventory.append("lace bra")
                            call Statup("Rogue", "Love", 200, 25)
                            call Statup("Rogue", "Obed", 200, 20)
                            call Statup("Rogue", "Inbt", 200, 20)
                            ch_r "I don't know that I'd wear this out, but maybe in private." 
                        elif "no gift bra" in R_RecentActions:
                            call RogueFace("angry",2)
                            ch_r "I just told you, it's not happening!"
                        elif "no gift bra" in R_DailyActions:
                            call RogueFace("angry",2)
                            ch_r "You can't even give me 24 hours?!"  
                        else:
                            call RogueFace("angry")
                            call Statup("Rogue", "Love", 50, -20)
                            call Statup("Rogue", "Obed", 20, 10)
                            call Statup("Rogue", "Inbt", 20, 20)  
                            if "no gift panties" in R_DailyActions:                    
                                ch_r "I don't want these neither!" 
                            else:                  
                                ch_r "I don't know why you would focus on my rack, [R_Petname]"                     
                            call Statup("Rogue", "Lust", 89, 5)
                            "She hands it back to you."
                            $ R_RecentActions.append("no gift bra")                      
                            $ R_DailyActions.append("no gift bra") 
                        call RogueFace("bemused")
                    else: 
                        ch_r "I already have one of those."                
                    
                "Give her the lace panties." if "r lace panties" in P_Inventory: 
                    #If you have panties, you'll give it.
                    if "lace panties" not in R_Inventory:                            
                        "You give Rogue the lace panties."
                        $ R_Blush = 1
                        if ApprovalCheck("Rogue", 1100):                    
                            call RogueFace("bemused")
                            $ P_Inventory.remove("r lace panties")
                            $ R_Inventory.append("lace panties")
                            call Statup("Rogue", "Love", 200, 30)
                            call Statup("Rogue", "Obed", 200, 20)
                            call Statup("Rogue", "Inbt", 200, 30)
                            ch_r "Hmm, these really put the goods on display. . ."
                            call Statup("Rogue", "Lust", 89, 10)
                        elif ApprovalCheck("Rogue", 800):
                            call RogueFace("confused")
                            $ P_Inventory.remove("r lace panties")
                            $ R_Inventory.append("lace panties")
                            call Statup("Rogue", "Love", 200, 25)
                            call Statup("Rogue", "Obed", 200, 20)
                            call Statup("Rogue", "Inbt", 200, 20)
                            ch_r "These are a bit flimsy. . ."       
                        elif "no gift panties" in R_RecentActions:
                            call RogueFace("angry",2)
                            ch_r "What did I {i}just{/i} tell you?!"
                        elif "no gift panties" in R_DailyActions:
                            call RogueFace("angry",2)
                            ch_r "Not today, [R_Petname]!"  
                        else:
                            call RogueFace("angry")
                            call Statup("Rogue", "Love", 50, -20)
                            call Statup("Rogue", "Obed", 20, 10)
                            call Statup("Rogue", "Inbt", 20, 20)  
                            if "no gift bra" in R_DailyActions:                    
                                ch_r "I don't want these neither!" 
                            else:
                                ch_r "I think I'll pick out my own unmentionables, thank you."                     
                            call Statup("Rogue", "Lust", 89, 5)
                            "She hands them back to you."
                            $ R_RecentActions.append("no gift panties")                      
                            $ R_DailyActions.append("no gift panties") 
                        call RogueFace("bemused")
                    else: 
                        ch_r "I already have one of those."                
                      
                "Give her the stockings and garterbelt." if "stockings and garterbelt" in P_Inventory: 
                    #If you have a stockings, you'll give it.
                    if "stockings and garterbelt" not in R_Inventory:                            
                        "You give Rogue the stockings."
                        $ R_Blush = 1                 
                        call RogueFace("bemused")
                        $ P_Inventory.remove("stockings and garterbelt")
                        $ R_Inventory.append("stockings and garterbelt")
                        call Statup("Rogue", "Love", 200, 5)
                        call Statup("Rogue", "Obed", 200, 5)
                        call Statup("Rogue", "Inbt", 200, 5)
                        ch_r "These are pretty nice. . ."
                        call Statup("Rogue", "Lust", 89, 5)
                    else: 
                        ch_r "I already have one of those."   
                     
                "Give her the bikini top." if "r bikini top" in P_Inventory: 
                    #If you have a bra, you'll give it.
                    if "bikini top" not in R_Inventory:                            
                        "You give Rogue the bikini top."
                        $ R_Blush = 1
                        if ApprovalCheck("Rogue", 1200):                    
                            call RogueFace("bemused")
                            $ P_Inventory.remove("r bikini top")
                            $ R_Inventory.append("bikini top")
                            call Statup("Rogue", "Love", 200, 20)
                            call Statup("Rogue", "Obed", 200, 10)
                            call Statup("Rogue", "Inbt", 200, 10)
                            ch_r "This is a nice color. . ."
                        elif ApprovalCheck("Rogue", 900):
                            call RogueFace("confused",1)
                            $ P_Inventory.remove("r bikini top")
                            $ R_Inventory.append("bikini top")
                            call Statup("Rogue", "Love", 200, 20)
                            call Statup("Rogue", "Obed", 200, 10)
                            call Statup("Rogue", "Inbt", 200, 5)
                            ch_r "A little skimpy. . ."                  
                            call RogueFace("bemused",1)
                        elif ApprovalCheck("Rogue", 700):
                            call RogueFace("confused",2)
                            $ P_Inventory.remove("r bikini top")
                            $ R_Inventory.append("bikini top")
                            call Statup("Rogue", "Love", 200, 10)
                            call Statup("Rogue", "Obed", 200, 5)
                            call Statup("Rogue", "Inbt", 200, 5)
                            ch_r "I was thinking about a tan. . ."                  
                            call RogueFace("bemused",1)
                        elif "no gift bra" in R_RecentActions:
                            call RogueFace("angry",2)
                            ch_r "Don't make me say it again!"
                        elif "no gift bra" in R_DailyActions:
                            call RogueFace("angry",2)
                            ch_r "My answer's still no, stop asking!"                      
                        else:
                            call RogueFace("angry",2)
                            call Statup("Rogue", "Love", 50, -5)
                            call Statup("Rogue", "Obed", 20, 5)
                            call Statup("Rogue", "Inbt", 20, 10)
                            if "no gift bra " in R_DailyActions:                    
                                ch_r "I don't want this either!"                      
                            else:
                                ch_r "Don't you worry about my swimwear."    
                            $ R_Blush = 1
                            "She hands it back to you."
                            $ R_RecentActions.append("no gift bra")                      
                            $ R_DailyActions.append("no gift bra") 
                        if "bikini top" in R_Inventory and "bikini bottoms" in R_Inventory:
                                $ R_Swim[0] = 1
                    else: 
                        ch_r "I already have one of those."
                        
               
                "Give her the bikini bottoms." if "r bikini bottoms" in P_Inventory: 
                    #If you have a bra, you'll give it.
                    if "bikini bottoms" not in R_Inventory:                            
                        "You give Rogue the bikini bottoms."
                        $ R_Blush = 1
                        if ApprovalCheck("Rogue", 1200):                    
                            call RogueFace("bemused")
                            $ P_Inventory.remove("r bikini bottoms")
                            $ R_Inventory.append("bikini bottoms")
                            call Statup("Rogue", "Love", 200, 20)
                            call Statup("Rogue", "Obed", 200, 10)
                            call Statup("Rogue", "Inbt", 200, 10)
                            ch_r "These are pretty nice. . ."
                        elif ApprovalCheck("Rogue", 900):
                            call RogueFace("confused",1)
                            $ P_Inventory.remove("r bikini bottoms")
                            $ R_Inventory.append("bikini bottoms")
                            call Statup("Rogue", "Love", 200, 20)
                            call Statup("Rogue", "Obed", 200, 10)
                            call Statup("Rogue", "Inbt", 200, 5)
                            ch_r "Kinda tiny, aren't they. . ."                  
                            call RogueFace("bemused",1)
                        elif ApprovalCheck("Rogue", 700):
                            call RogueFace("confused",2)
                            $ P_Inventory.remove("r bikini bottoms")
                            $ R_Inventory.append("bikini bottoms")
                            call Statup("Rogue", "Love", 200, 10)
                            call Statup("Rogue", "Obed", 200, 5)
                            call Statup("Rogue", "Inbt", 200, 5)
                            ch_r "I was thinking about a tan. . ."                   
                            call RogueFace("bemused",1)
                        elif "no gift panties" in R_RecentActions:
                            call RogueFace("angry",2)
                            ch_r "Don't make me say it again!"
                        elif "no gift panties" in R_DailyActions:
                            call RogueFace("angry",2)
                            ch_r "My answer's still no, stop asking!"                      
                        else:
                            call RogueFace("angry",2)
                            call Statup("Rogue", "Love", 50, -5)
                            call Statup("Rogue", "Obed", 20, 5)
                            call Statup("Rogue", "Inbt", 20, 10)
                            if "no gift bra" in R_DailyActions:                    
                                ch_r "I don't want these either!"                      
                            else:
                                ch_r "Don't you worry what I've got on down there."    
                            $ R_Blush = 1
                            "She hands them back to you."
                            $ R_RecentActions.append("no gift panties")                      
                            $ R_DailyActions.append("no gift panties") 
                        if "bikini top" in R_Inventory and "bikini bottoms" in R_Inventory:
                                $ R_Swim[0] = 1
                    else: 
                        ch_r "I already have one of those."
                              
                "Never mind":
                    pass 
            
#        "Give her a butt plug." if "buttplug" in P_Inventory:
#            if "buttplug" not in R_Inventory:                            
#                "You give Rogue the butt plug."
#                $ P_Inventory.remove("buttplug")
#                $ R_Inventory.append("buttplug")
#            else: 
#                "She already has enough of those."
#            
        "Exit":
            return
    
    jump Rogue_Gifts
    return


# start Rogue_Names//////////////////////////////////////////////////////////
label Rogue_Names:    
    menu:
        ch_r "Oh? What would you like me to call you?"
        "Sugar's fine.":
            $ R_Petname = "sugar"
            ch_r "You got it, sugar."
        "Call me by my name.":
            $ R_Petname = Playername            
            ch_r "If you'd rather, [R_Petname]."
        "Call me \"boyfriend\"." if "boyfriend" in R_Petnames:
            $ R_Petname = "boyfriend"
            ch_r "Sure thing, [R_Petname]."
        "Call me \"lover\"." if "lover" in R_Petnames:
            $ R_Petname = "lover"
            ch_r "Oooh, love to, [R_Petname]."
        "Call me \"sir\"." if "sir" in R_Petnames:
            $ R_Petname = "sir"
            ch_r "Yes, [R_Petname]."
        "Call me \"master\"." if "master" in R_Petnames:
            $ R_Petname = "master"
            ch_r "As you wish, [R_Petname]."
        "Call me \"sex friend\"." if "sex friend" in R_Petnames:
            $ R_Petname = "sex friend"
            ch_r "Heh, very cheeky, [R_Petname]."
        "Call me \"fuck buddy\"." if "fuck buddy" in R_Petnames:
            $ R_Petname = "fuck buddy"
            ch_r "I'm game if you are, [R_Petname]."        
        "Call me \"daddy\"." if "daddy" in R_Petnames:
            $ R_Petname = "daddy"
            ch_r "Oh! You bet, [R_Petname]."
        "Nevermind.":
            return
    return
# end Rogue_Names//////////////////////////////////////////////////////////

label Rogue_Pet:
    while 1:
        menu:
            extend ""
            "Polite":
                menu:
                    extend ""
                    "I think I'll just call you Rogue.":
                        $ R_Pet = "Rogue"            
                        ch_r "I don't see why not, [R_Petname]."
                        
                    "I think I'll call you \"girl\".":
                        $ R_Pet = "girl"
                        if "boyfriend" in R_Petnames or ApprovalCheck("Rogue", 500, "L"):
                            call RogueFace("sexy", 1) 
                            ch_r "I sure am your girl, [R_Petname]."
                        else:      
                            call RogueFace("angry")           
                            ch_r "I ain't your girl, [R_Petname]." 
                            
                    "I think I'll call you \"boo\".":
                        $ R_Pet = "boo"
                        if "boyfriend" in R_Petnames or ApprovalCheck("Rogue", 500, "L"):
                            call RogueFace("sexy", 1) 
                            ch_r "Aw, I am your boo, [R_Petname]."
                        else:     
                            call RogueFace("angry")            
                            ch_r "I ain't your boo,  [R_Petname]."
                            
                    "I think I'll call you \"bae\".":
                        $ R_Pet = "bae"
                        if "boyfriend" in R_Petnames or ApprovalCheck("Rogue", 500, "L"):
                            call RogueFace("sexy", 1) 
                            ch_r "Aw, I am your bae, [R_Petname]."
                        else:     
                            call RogueFace("angry")            
                            ch_r "I ain't your bae,  [R_Petname]."
                            
                    "I think I'll call you \"baby\".":
                        $ R_Pet = "baby"
                        if "boyfriend" in R_Petnames or ApprovalCheck("Rogue", 500, "L"):
                            call RogueFace("sexy", 1) 
                            ch_r "Aw, cute, [R_Petname]."
                        else:     
                            call RogueFace("angry")            
                            ch_r "I ain't your baby, [R_Petname]." 
                            
                    "I think I'll call you \"chere\".":
                        $ R_Pet = "chere"
                        if "lover" in R_Petnames or ApprovalCheck("Rogue", 600, "L"):
                            call RogueFace("sexy", 1) 
                            ch_r "Oh, tre romantic, [R_Petname]."
                        else:     
                            call RogueFace("angry", 1)  
                            $ R_Eyes = "side"
                            ch_r "That has some. . . bad memories, [R_Petname]." 
                            
                    "I think I'll call you \"sweetie\".":
                        $ R_Pet = "sweetie"
                        if "boyfriend" in R_Petnames or ApprovalCheck("Rogue", 500, "L"):
                            ch_r "Aw, that's sweet, [R_Petname]."
                        else:     
                            call RogueFace("angry", 1)            
                            ch_r "That's a bit much, [R_Petname]."
                            
                    "I think I'll call you \"sexy\".":
                        $ R_Pet = "sexy"
                        if "lover" in R_Petnames or ApprovalCheck("Rogue", 900):
                            call RogueFace("sexy", 1) 
                            ch_r "You're not so bad yourself, [R_Petname]."
                        else:        
                            call RogueFace("angry", 1)         
                            ch_r "Inappropriate, [R_Petname]."  
                            
                    "I think I'll call you \"lover\".":
                        $ R_Pet = "lover"
                        if "lover" in R_Petnames or ApprovalCheck("Rogue", 900):
                            call RogueFace("sexy", 1) 
                            ch_r "Oh, I love you too, [R_Petname]."
                        else:      
                            call RogueFace("angry", 1)           
                            ch_r "Not any time soon, [R_Petname]."   
                        
                    "Back":
                        pass
            
            "Risky":
                menu:                        
                    "I think I'll call you \"slave\".":
                        $ R_Pet = "slave"
                        if "master" in R_Petnames or ApprovalCheck("Rogue", 700, "O"):
                            call RogueFace("bemused", 1) 
                            ch_r "As you wish, [R_Petname]."
                        else:      
                            call RogueFace("angry", 1)           
                            ch_r "I ain't anyone's slave, [R_Petname]."
                                            
                    "I think I'll call you \"pet\".":
                        $ R_Pet = "pet"
                        if "master" in R_Petnames or ApprovalCheck("Rogue", 600, "O"):
                            call RogueFace("bemused", 1) 
                            ch_r "Hmm, make sure to pet me, [R_Petname]."
                        else:             
                            call RogueFace("angry", 1)    
                            ch_r "I ain't your pet, [R_Petname]."
                            
                    "I think I'll call you \"slut\".":
                        $ R_Pet = "slut"
                        if "sex friend" in R_Petnames or ApprovalCheck("Rogue", 1000, "OI"):
                            call RogueFace("sexy") 
                            ch_r "You know me too well, [R_Petname]."
                        else:                
                            call RogueFace("angry", 1) 
                            $ R_Mouth = "surprised"
                            ch_r "Well I never!" 
                            
                    "I think I'll call you \"whore\".":
                        $ R_Pet = "whore"
                        if "fuckbuddy" in R_Petnames or ApprovalCheck("Rogue", 1100, "OI"):
                            call RogueFace("sly") 
                            ch_r "I guess I am. . ."
                        else:        
                            call RogueFace("angry", 1)         
                            ch_r "You look'in to start something, [R_Petname]?" 
                                                   
                    "I think I'll call you \"sugartits\".":
                        $ R_Pet = "sugartits"
                        if "sex friend" in R_Petnames or ApprovalCheck("Rogue", 1500):
                            call RogueFace("sly", 1) 
                            ch_r "Heh."
                        else:     
                            call RogueFace("angry", 1)            
                            ch_r "Better not to my face, [R_Petname]." 
                            
                    "I think I'll call you \"sex friend\".":
                        $ R_Pet = "sex friend"
                        if "sex friend" in R_Petnames or ApprovalCheck("Rogue", 600, "I"):
                            call RogueFace("sly") 
                            ch_r "Rreow. . ."
                        else:                
                            call RogueFace("angry", 1) 
                            ch_r "Hey, no need to advertise, [R_Petname]." 
                            
                    "I think I'll call you \"fuckbuddy\".":
                        $ R_Pet = "fuckbuddy"
                        if "fuckbuddy" in R_Petnames or ApprovalCheck("Rogue", 700, "I"):
                            call RogueFace("sly") 
                            ch_r "That sounds about right, [R_Petname]."
                        else:                
                            call RogueFace("angry", 1)
                            $ R_Mouth = "surprised"
                            ch_r "Inappropriate, [R_Petname]." 
                        
                    "I think I'll call you \"baby girl\".":
                        $ R_Pet = "baby girl"
                        if "daddy" in R_Petnames or ApprovalCheck("Rogue", 1200):
                            call RogueFace("smile", 1) 
                            ch_r "You know it, [R_Petname]."
                        else:                
                            call RogueFace("angry", 1) 
                            ch_r "I ain't your baby girl, [R_Petname]." 
                            
                    "Back":
                        pass
                    
            "Nevermind.":
                return
    return
    
label Rogue_Namecheck(R_Pet = R_Pet, Cnt = 0, Ugh = 0):#R_Pet is the internal pet name, Cnt and Ugh are internal count variable
    if R_Pet == "Rogue":
        return Ugh   
    if Taboo:
        $ Cnt = int(Taboo/10)
    if R_Pet == "girl":                                         #easy options
        if ApprovalCheck("Rogue", 500, "L", TabM=1):            
            call Statup("Rogue", "Love", 80, 1)
        else:
            call Statup("Rogue", "Love", 50, -1)
            $ Ugh = 1
    elif R_Pet == "boo" or R_Pet == "bae":
        if ApprovalCheck("Rogue", 500, "L", TabM=1):
            call Statup("Rogue", "Love", 80, 1)
        else:
            call Statup("Rogue", "Love", 50, -2)
            $ Ugh = 1
    elif R_Pet == "baby":    
        if ApprovalCheck("Rogue", 500, "L", TabM=1):
            call Statup("Rogue", "Love", 90, 1)
        else:
            call Statup("Rogue", "Love", 30, -1)
            $ Ugh = 1
    elif R_Pet == "chere":
        if ApprovalCheck("Rogue", 600, "L", TabM=1):
            call Statup("Rogue", "Love", 80, 2)
        else:
            call Statup("Rogue", "Love", 50, -1)
            $ Ugh = 1
    elif R_Pet == "sweetie":
        if not ApprovalCheck("Rogue", 500, "L", TabM=1):
            call Statup("Rogue", "Love", 80, 1)  
        else:
            call Statup("Rogue", "Love", 40, -1)
            $ Ugh = 1
            
    elif R_Pet == "sexy" or R_Pet == "lover":
        if ApprovalCheck("Rogue", 900, TabM=1):                                                        #over 150
            call Statup("Rogue", "Love", 80, 2)
            call Statup("Rogue", "Obed", 80, 1)
            call Statup("Rogue", "Inbt", 70, 1) 
        else:                                                            
            call Statup("Rogue", "Love", 50, (-1-Cnt))
            call Statup("Rogue", "Obed", 50, 1)
            call Statup("Rogue", "Inbt", 20, -1)
            $ Ugh = 1
            
    elif R_Pet == "slave":                                        #tougher options
        if ApprovalCheck("Rogue", 800, "O", TabM=3):                                            #over 80
            call Statup("Rogue", "Lust", 90, (3+Cnt))
            call Statup("Rogue", "Obed", 95, (2+Cnt))
            call Statup("Rogue", "Inbt", 30, 1)
            call Statup("Rogue", "Inbt", 70, 1)     
        elif ApprovalCheck("Rogue", 500, "O", TabM=3):                                                  #between 50 and 80
            call Statup("Rogue", "Lust", 90, 1)
            call Statup("Rogue", "Love", 200, -1)
            call Statup("Rogue", "Obed", 81, 2)
            call Statup("Rogue", "Inbt", 70, 1)        
        else:                                                                                           # under 50
            call Statup("Rogue", "Love", 200, -2)
            call Statup("Rogue", "Love", 50, -1, 1)
            call Statup("Rogue", "Obed", 50, 1)
            call Statup("Rogue", "Inbt", 50, -1)
            $ Ugh = 1
    
    elif R_Pet == "pet":                                        #tougher options
        if ApprovalCheck("Rogue", 1500, TabM=2):                                            #over 150
            call Statup("Rogue", "Lust", 90, (3+Cnt))
            call Statup("Rogue", "Obed", 95, (2+Cnt))
            call Statup("Rogue", "Inbt", 30, 1)
            call Statup("Rogue", "Inbt", 70, 1)     
        elif ApprovalCheck("Rogue", 1200, TabM=2):                                                  #between 120 and 150
            call Statup("Rogue", "Lust", 60, 1)
            call Statup("Rogue", "Obed", 81, 2)
            call Statup("Rogue", "Inbt", 70, 1)        
        else:                                                                                           # under 120
            call Statup("Rogue", "Love", 200, -2)
            call Statup("Rogue", "Love", 50, -1, 1)
            call Statup("Rogue", "Obed", 50, 1)
            call Statup("Rogue", "Inbt", 50, -1)
            $ Ugh = 1
            
    elif R_Pet == "slut":
        if ApprovalCheck("Rogue", 500, "O", TabM=2) or ApprovalCheck("Rogue", 500, "I", TabM=2):        #over 50
            call Statup("Rogue", "Lust", 90, (4+Cnt))
            call Statup("Rogue", "Obed", 95, (2+Cnt))
            call Statup("Rogue", "Inbt", 40, 2)
            call Statup("Rogue", "Inbt", 80, 1)
        elif ApprovalCheck("Rogue", 300, "O", TabM=2) or ApprovalCheck("Rogue", 300, "I", TabM=2):      #between 30 and 50
            call Statup("Rogue", "Lust", 90, 1)
            call Statup("Rogue", "Love", 200, (-1-Cnt))
            call Statup("Rogue", "Obed", 80, (2+Cnt))
            call Statup("Rogue", "Inbt", 70, 1)        
        else:                                                                                           # under 40
            call Statup("Rogue", "Love", 200, (-2-Cnt))
            call Statup("Rogue", "Love", 50, (-1-Cnt), 1)
            call Statup("Rogue", "Obed", 50, 1)
            call Statup("Rogue", "Inbt", 20, -1)
            $ Ugh = 1
            
    elif R_Pet == "whore":
        if ApprovalCheck("Rogue", 600, "O", TabM=2) or ApprovalCheck("Rogue", 600, "I", TabM=2):        #over 60
            call Statup("Rogue", "Lust", 90, 4)
            call Statup("Rogue", "Obed", 95, 2)
            call Statup("Rogue", "Inbt", 50, 2)
            call Statup("Rogue", "Inbt", 80, 1)
        elif ApprovalCheck("Rogue", 400, "O", TabM=2) or ApprovalCheck("Rogue", 400, "I", TabM=2):      #between 40 and 60
            call Statup("Rogue", "Lust", 90, 1)
            call Statup("Rogue", "Love", 200, (-2-Cnt))
            call Statup("Rogue", "Obed", 80, 2)
            call Statup("Rogue", "Inbt", 70, 1)
        else:                                                                                           # under 40
            call Statup("Rogue", "Love", 200, (-3-Cnt))
            call Statup("Rogue", "Love", 50, (-2-Cnt), 1)
            call Statup("Rogue", "Obed", 50, 1)            
            call Statup("Rogue", "Inbt", 21, 1, 1)
            call Statup("Rogue", "Inbt", 20, -1)
            $ Ugh = 1
            
    elif R_Pet == "sugartits":
        if ApprovalCheck("Rogue", 1500, TabM=1):                                                        #over 150
            call Statup("Rogue", "Obed", 80, 1)
            call Statup("Rogue", "Obed", 50, 2)
            call Statup("Rogue", "Inbt", 70, 1)            
            call Statup("Rogue", "Inbt", 30, 2)
        else:                                                                       
            call Statup("Rogue", "Love", 200, (-2-Cnt))
            call Statup("Rogue", "Love", 50, (-1-Cnt))
            call Statup("Rogue", "Obed", 50, 1)
            call Statup("Rogue", "Inbt", 20, -1)
            $ Ugh = 1
            
    elif R_Pet == "sex friend":    
        if ApprovalCheck("Rogue", 750, "O", TabM=1) or ApprovalCheck("Rogue", 600, "I", TabM=1):        #over 75/60
            call Statup("Rogue", "Lust", 90, 3)
            call Statup("Rogue", "Obed", 95, 2)
            call Statup("Rogue", "Inbt", 40, 2)
            call Statup("Rogue", "Inbt", 80, 1)
        elif ApprovalCheck("Rogue", 600, "O", TabM=1) or ApprovalCheck("Rogue", 400, "I", TabM=1):      #between 60/40 and 75/60
            call Statup("Rogue", "Lust", 90, 2)
            call Statup("Rogue", "Love", 200, (-1-Cnt))
            call Statup("Rogue", "Obed", 80, 1)
            call Statup("Rogue", "Inbt", 70, 1)
            $ R_Blush = 1
        else:                                                                                           # under 60/40
            call Statup("Rogue", "Love", 200, -Cnt)
            call Statup("Rogue", "Love", 50, (-1-Cnt), 1)
            call Statup("Rogue", "Obed", 50, 1)
            call Statup("Rogue", "Inbt", 20, -1)
            $ Ugh = 1
            
    elif R_Pet == "fuckbuddy":
        if ApprovalCheck("Rogue", 700, "O", TabM=2) or ApprovalCheck("Rogue", 700, "I", TabM=1):        #over 70/70
            call Statup("Rogue", "Lust", 90, 3)
            call Statup("Rogue", "Obed", 95, 2)
            call Statup("Rogue", "Inbt", 40, 2)
            call Statup("Rogue", "Inbt", 85, 1)
        elif ApprovalCheck("Rogue", 600, "O", TabM=2) or ApprovalCheck("Rogue", 500, "I", TabM=1):      #between 60/50 and 70/70
            call Statup("Rogue", "Lust", 90, 2)
            call Statup("Rogue", "Love", 200, (-1-Cnt))
            call Statup("Rogue", "Obed", 80, 1)
            call Statup("Rogue", "Inbt", 70, 1)
            $ R_Blush = 1
        else:                                                                                           #under 60/50
            call Statup("Rogue", "Love", 200, -Cnt)
            call Statup("Rogue", "Love", 60, (-2-Cnt), 1)
            call Statup("Rogue", "Obed", 60, 1)
            call Statup("Rogue", "Inbt", 20, -1)
            $ Ugh = 1
            
    elif R_Pet == "baby girl":
        if ApprovalCheck("Rogue", 1200, TabM=1):                                                        #over 150
            call Statup("Rogue", "Obed", 80, 1)
            call Statup("Rogue", "Obed", 50, 2)
            call Statup("Rogue", "Inbt", 70, 1)            
            call Statup("Rogue", "Inbt", 30, 2)
        else:                                                                       
            call Statup("Rogue", "Love", 200, (-2-Cnt))
            call Statup("Rogue", "Love", 50, (-1-Cnt))
            call Statup("Rogue", "Obed", 50, 1)
            call Statup("Rogue", "Inbt", 20, -1)
            $ Ugh = 1
            
    return Ugh


# start Rogue_Personality//////////////////////////////////////////////////////////
label Rogue_Personality(Cnt = 0):   
    if not R_Chat[4] or Cnt:
        "Since you're doing well in one area, you can convince Rogue to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_r "Sure, what's up?"
        "More Obedient. [[Love to Obedience]" if R_Love > 900:
            ch_p "If you really love me, could you please just do what I say?"
            ch_r "Well, I suppose for you I could be a bit more obedient."
            $ R_Chat[4] = 1
        "Less Inhibited. [[Love to Inhibition]" if R_Love > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_r "Well, I suppose for you I could be a bit less inhibited."
            $ R_Chat[4] = 2
        
        "Less Inhibited. [[Obedience to Inhibition]" if R_Obed > 900:
            ch_p "I want you to be less inhibited."
            ch_r "Very well, I'll try to take more initiative."
            $ R_Chat[4] = 3
        "More Loving. [[Obedience to Love]" if R_Obed > 900:
            ch_p "I'd like you to learn to love me."
            ch_r "If I must, I'll try to come around."
            $ R_Chat[4] = 4
            
        "More Obedient. [[Inhibition to Obedience]" if R_Inbt > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_r "Well, I guess it can be fun to try what you want too. . ."
            $ R_Chat[4] = 5
            
        "More Loving. [[Inhibition to Love]" if R_Inbt > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_r "Well, I guess I am getting pretty attached. . ."
            $ R_Chat[4] = 6
            
        "I guess just do what you like. . .[[reset]" if R_Chat[4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_r "Um, ok."
            $ R_Chat[4] = 0
        "Repeat the rules":
            $ Cnt = 1
            jump Rogue_Personality
        "Nevermind.":
            return
    return
# end Rogue_Personality//////////////////////////////////////////////////////////




# Rogue_Summon//////////////////////////////////////////////////////////

label Rogue_Summon(Tempmod = Tempmod):
    call RogueOutfit        
    if "no summon" in R_RecentActions:
            # If she's refused to follow you once recently
            if "angry" in R_RecentActions:
                ch_r "What part of \"no\" don't you understand?"
            elif Action_Check("Rogue", "recent", "no summon") > 1:
                ch_r "I already told you no, take a hint."
                $ R_RecentActions.append("angry") 
            elif Current_Time == "Night": 
                ch_r "I told you it was too late for that tonight."
            else:
                ch_r "I told you I was busy."   
            $ R_RecentActions.append("no summon")
            return
                        
    $ D20 = renpy.random.randint(1, 20) 
    $ Line = 0
    if R_Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = -10
    elif R_Loc == "bg dangerroom":    
        $ Tempmod = -20
    elif R_Loc == "bg showerroom":    
        $ Tempmod = -40
        
    if D20 <= 3:                                                                        
        #unlucky refusal
        $ Line = "no"    
    elif "les" in R_RecentActions:
            #if she's with another girl. . .
            if ApprovalCheck("Rogue", 2000):
                    ch_r "I'm enjoying some company right now, [R_Petname], care to join us?"
                    menu:
                        extend ""
                        "Sure":
                            $ Line = "go to"
                        "No thanks.":
                            ch_r "Suit yourself."
                            return
            else:            
                    ch_r "What? Um, no, um, not right now."   
                    ch_r "Maybe we could touch base later."      
                    $ R_RecentActions.append("no summon") 
                    return  
    elif Current_Time == "Night": 
            if ApprovalCheck("Rogue", 700, "L") or ApprovalCheck("Rogue", 300, "O"):                              
                    #It's night time but she likes you.
                    ch_r "Ok, it's getting late but I can hang out for a bit."
                    $ R_Loc = bg_current 
                    call Set_The_Scene
            else:                                                           
                    #It's night time and she isn't into you
                    ch_r "It's a bit late, [R_Petname], maybe tomorrow."     
                    $ R_RecentActions.append("no summon") 
            return            
    elif not ApprovalCheck("Rogue", 700, "L") or not ApprovalCheck("Rogue", 600, "O"):                       
        #It's not night time, but she's busy 
        if not ApprovalCheck("Rogue", 300):
                ch_r "Not really interested, [R_Petname]."       
                $ R_RecentActions.append("no summon") 
                return    
        
        
        if "summoned" in R_RecentActions:
                pass              
        elif "goto" in R_RecentActions:
                ch_r "You were just over here and then you took off. Why not just head back?"
        elif R_Loc == "bg classroom":
                ch_r "I'm kinda in class right now, [R_Petname], you could join me."
        elif R_Loc == "bg dangerroom": 
                ch_r "I'm training at the moment, [R_Petname], care to join me?"    
        elif R_Loc == "bg campus": 
                ch_r "I'm hanging out on campus, [R_Petname], want to hang with me?" 
        elif R_Loc == "bg rogue": 
                ch_r "I'm in my room, [R_Petname], want to swing by?" 
        elif R_Loc == "bg player": 
                ch_r "I happen to be in your room, [R_Petname], I'm waiting for you. . ."   
        elif R_Loc == "bg showerroom":    
            if ApprovalCheck("Rogue", 1600):
                ch_r "I'm kinda in the shower right now, [R_Petname], care to join me?"
            else:            
                ch_r "I'm kinda in the shower right now, [R_Petname], maybe we could touch base later."      
                $ R_RecentActions.append("no summon") 
                return    
        elif R_Loc == "hold":
                ch_r "I'm not really around right now, see you later?"       
                $ R_RecentActions.append("no summon") 
                return    
        else:
                #Unknown location
                ch_r "Why don't you come over here, [R_Petname]?"    
            
        if "summoned" in R_RecentActions:
            ch_r "Ok, fine, but why are you leading me on a merry chase?"           
            $ Line = "yes"
            
        elif "goto" in R_RecentActions:
            menu:
                extend ""
                "You're right, be right back.":
                                ch_r "See you then!"
                                $ Line = "go to"                    
                "Nah, it's better here.":    
                                ch_r "Fine by me."                    
                "But I'd {i}really{/i} like to see you over here.":
                        if ApprovalCheck("Rogue", 600, "L") or ApprovalCheck("Rogue", 1400):
                                $ Line = "lonely"
                        else: 
                                $ Line = "no"                        
                "I said come over here.":
                        if ApprovalCheck("Rogue", 600, "O"):                                   
                                #she is obedient
                                $ Line = "command"                        
                        elif D20 >= 7 and ApprovalCheck("Rogue", 1400):                         
                                #she is generally favorable 
                                ch_r "I suppose I can, [R_Petname]."              
                                $ Line = "yes"                        
                        elif ApprovalCheck("Rogue", 200, "O"):                                  
                                #she is not obedient  
                                ch_r "I don't think so."    
                                ch_r "If you want to see me, you know where to find me."    
                        else:                                                                   
                                #she is obedient, but you failed to meet the checks                     
                                $ Line = "no" 
        else:
            menu:
                extend ""
                "Sure, I'll be right there.":
                        call Statup("Rogue", "Love", 55, 1) 
                        call Statup("Rogue", "Inbt", 30, 1)
                        ch_r "See you then!"
                        $ Line = "go to"
                    
                "Nah, we can talk later.":
                        call Statup("Rogue", "Obed", 50, 1)                            
                        call Statup("Rogue", "Obed", 30, 2)     
                        ch_r "Oh, ok. Talk to you later then."
                    
                "Could you please come visit me? I'm lonely.":
                        if ApprovalCheck("Rogue", 600, "L") or ApprovalCheck("Rogue", 1400):
                            call Statup("Rogue", "Love", 70, 1)                   
                            call Statup("Rogue", "Obed", 50, 1)
                            $ Line = "lonely"
                        else: 
                            call Statup("Rogue", "Inbt", 30, 1)
                            $ Line = "no"
                            
                "I said come over here.":
                        if ApprovalCheck("Rogue", 600, "O"):                              
                            #she is obedient
                            call Statup("Rogue", "Love", 50, 1, 1)    
                            call Statup("Rogue", "Love", 40, -1)                
                            call Statup("Rogue", "Obed", 90, 1)    
                            $ Line = "command"
                            
                        elif D20 >= 7 and ApprovalCheck("Rogue", 1400):       
                            #she is generally favorable
                            call Statup("Rogue", "Love", 70, -2)  
                            call Statup("Rogue", "Love", 90, -1)  
                            call Statup("Rogue", "Obed", 50, 2)                                
                            call Statup("Rogue", "Obed", 90, 1)  
                            ch_r "I suppose I can, [R_Petname]."              
                            $ Line = "yes"
                            
                        elif ApprovalCheck("Rogue", 200, "O"):                                         
                            #she is not obedient   
                            call Statup("Rogue", "Love", 70, -4)  
                            call Statup("Rogue", "Love", 90, -2)   
                            ch_r "I don't know who you think you are, boss'in me around like that."                             
                            call Statup("Rogue", "Inbt", 40, 2)
                            call Statup("Rogue", "Inbt", 60, 1)    
                            call Statup("Rogue", "Obed", 70, -2)
                            ch_r "If you want to see me, you know where to find me."    
                        else:                                                                   
                            #she is obedient, but you failed to meet the checks
                            call Statup("Rogue", "Inbt", 30, 1)
                            call Statup("Rogue", "Inbt", 50, 1)                                    
                            call Statup("Rogue", "Love", 50, -1, 1)
                            call Statup("Rogue", "Obed", 70, -1)  
                            $ Line = "no" 
                        #end "ordered"
    else:                                                                               
        #automatic acceptance
        if R_Love > R_Obed:
                ch_r "I'd love to, [R_Petname]."
        else:
                ch_r "Ok, I'll be right over, [R_Petname]."
        $ Line = "yes" 
       
    $ Tempmod = 0
    
    if not Line:                                                                        
            #You end the dialog neutrally              
            $ R_RecentActions.append("no summon") 
            return
    
    if Line == "no":                                                                    
            # She's refused, context based dialog
            if R_Loc == "bg classroom":
                ch_r "I seriously can't, [R_Petname], big test coming up." 
            elif R_Loc == "bg dangerroom": 
                ch_r "Wish I could, [R_Petname], but I need to get some hours in."
            else:
                ch_r "I'm sorry, [R_Petname], but I'm kinda busy right now."  
            $ R_RecentActions.append("no summon") 
            return
        
    elif Line == "go to":                                                                 
            #You agreed to go to her instead        
            $ renpy.pop_call()
            $ Tempmod = 0
            $ R_RecentActions.append("goto") 
            $ P_RecentActions.append("goto")  
            if R_Loc == "bg classroom":
                    ch_r "See you then!"
                    jump Class_Room 
            elif R_Loc == "bg dangerroom": 
                    ch_r "I'll be warming up!"
                    jump Danger_Room
            elif R_Loc == "bg rogue": 
                    ch_r "I'll get tidied up."
                    jump Rogue_Room
            elif R_Loc == "bg player": 
                    ch_r "I'll be waiting."
                    jump Player_Room                
            elif R_Loc == "bg showerroom": 
                    ch_r "I guess I'll be here."
                    jump Shower_Room
            elif R_Loc == "bg campus": 
                    ch_r "I'll keep an eye out for you."
                    jump Campus
            elif R_Loc == "bg kitty": 
                    ch_r "I'll see you there."
                    jump Kitty_Room
            elif R_Loc == "bg emma": 
                    ch_r "I'll see you there."
                    jump Emma_Room
            elif R_Loc == "bg laura": 
                    ch_r "I'll see you there."
                    jump Laura_Room
            else:
                    ch_r "You know, I'll just meet you in my room."
                    $ R_Loc = "bg rogue"
                    jump Rogue_Room
            
    #She's agreed to come over    
    elif Line == "lonely":
            ch_r "Oh, how could I say \"no\" to you, [R_Petname]?"
    elif Line == "command": 
            ch_r "Fine, if you insist, [R_Petname]."
    
    $ R_RecentActions.append("summoned") 
    $ Line = 0
    ch_r "I'll be right over."  
    if "locked" in P_Traits:
            call Locked_Door("Rogue")
            return                              
    $ R_Loc = bg_current 
    call Set_The_Scene
    return

# End Rogue Summon / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Rogue Leave / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    
label Rogue_Leave(Tempmod=Tempmod):  
        if "leaving" in R_RecentActions:
            call DrainWord("Rogue","leaving")   
        else:
            return
        
        if bg_current == "bg dangerroom":   
                call Gym_Clothes("exit")
                
        if R_Loc == "hold":   
                # Activates if she's being moved out of play
                ch_r "I'm heading out for a while, see you later." 
                return
                
        if "Rogue" in Party or "lockedtravels" in R_Traits: 
                #If she's in your party or if you've told her not to leave you
                #It resets her to your location
                $ R_Loc = bg_current 
                return
          
        elif "freetravels" in R_Traits or not ApprovalCheck("Rogue", 700):
                #If you've told her to go wherever, or she just doesn't care what you think.
                call RogueOutfit(Changed=0)
                if not ApprovalCheck("Rogue", 600, "LO"):
                                ch_r "I'm headed out, see you later."
                elif R_Loc == "bg classroom":
                                ch_r "I'm headed to class right now, [R_Petname]."
                elif R_Loc == "bg dangerroom": 
                                ch_r "I'm hitting the danger room, [R_Petname]."   
                elif R_Loc == "bg campus": 
                                ch_r "I'm going to hang out on campus, [R_Petname]." 
                elif R_Loc == "bg rogue": 
                                ch_r "I'm heading back to my room, [R_Petname]." 
                elif R_Loc == "bg player": 
                                ch_r "I'll be heading to your room, [R_Petname]."   
                elif R_Loc == "bg showerroom":    
                            if ApprovalCheck("Rogue", 1400):
                                ch_r "I'm hitting the showers, later."
                            else:            
                                ch_r "I'm . . . headed out, see you later."                        
                else:        
                                ch_r "I'm headed out, see you later."
                hide Rogue
                return     
                #End Free Travels
        
        call RogueOutfit(Changed=0)  
        
        if "follow" not in R_Traits:
                # Sets a key to show that she's asked you to follow her at least once
                $ R_Traits.append("follow")   
            
        $ D20 = renpy.random.randint(1, 20) 
        $ Line = 0
        # Sets her preferences
        if R_Loc == "bg classroom": #fix change these if changed function
            $ Tempmod = 10
        elif R_Loc == "bg dangerroom":    
            $ Tempmod = 20
        elif R_Loc == "bg showerroom":    
            $ Tempmod = 40

        
        if R_Loc == "bg classroom":
                        ch_r "I'm headed to class right now, [R_Petname], you could join me."
        elif R_Loc == "bg dangerroom": 
                        ch_r "I'm hitting the danger room, [R_Petname], care to join me?"    
        elif R_Loc == "bg campus": 
                        ch_r "I'm going to hang out on campus, [R_Petname], want to hang with me?" 
        elif R_Loc == "bg rogue": 
                        ch_r "I'm heading back to my room, [R_Petname], want to swing by?" 
        elif R_Loc == "bg player": 
                        ch_r "I'll be heading to your room, [R_Petname]."   
        elif R_Loc == "bg showerroom":    
                    if ApprovalCheck("Rogue", 1600):
                        ch_r "I'm hitting the showers, [R_Petname], care to join me?"
                    else:            
                        ch_r "I'm hitting the showers, [R_Petname], maybe we could touch base later."
                        return           
        else: #Location unknown        
                        ch_r "Why don't you come with me, [R_Petname]?"    
        
        menu:
            extend ""
            "Sure, I'll catch up.":                  
                    if "followed" not in R_RecentActions:
                        call Statup("Rogue", "Love", 55, 1) 
                        call Statup("Rogue", "Inbt", 30, 1)
                    $ Line = "go to"
                
            "Nah, we can talk later.":
                    if "followed" not in R_RecentActions:
                        call Statup("Rogue", "Obed", 50, 1)                            
                        call Statup("Rogue", "Obed", 30, 2)
                    ch_r "Oh, ok. Talk to you later then."
                
            "Could you please stay with me? I'll get lonely.":
                    if ApprovalCheck("Rogue", 600, "L") or ApprovalCheck("Rogue", 1400):
                        if "followed" not in R_RecentActions:
                            call Statup("Rogue", "Love", 70, 1)                   
                            call Statup("Rogue", "Obed", 50, 1)
                        $ Line = "lonely"
                    else: 
                        if "followed" not in R_RecentActions:
                            call Statup("Rogue", "Inbt", 30, 1)
                        $ Line = "no"
                    
            "No, stay here.":
                    if ApprovalCheck("Rogue", 600, "O"):                              
                        #she is obedient
                        if "followed" not in R_RecentActions:
                            call Statup("Rogue", "Love", 50, 1, 1)    
                            call Statup("Rogue", "Love", 40, -1)                
                            call Statup("Rogue", "Obed", 90, 1)    
                        $ Line = "command"
                        
                    elif D20 >= 7 and ApprovalCheck("Rogue", 1400):       
                        #she is generally favorable
                        if "followed" not in R_RecentActions:
                            call Statup("Rogue", "Love", 70, -2)  
                            call Statup("Rogue", "Love", 90, -1)  
                            call Statup("Rogue", "Obed", 50, 2)                                
                            call Statup("Rogue", "Obed", 90, 1)  
                        ch_r "I suppose I can, [R_Petname]."              
                        $ Line = "yes"
                        
                    elif ApprovalCheck("Rogue", 200, "O"):                                         
                        #she is not obedient   
                        if "followed" not in R_RecentActions:
                            call Statup("Rogue", "Love", 70, -4)  
                            call Statup("Rogue", "Love", 90, -2)   
                        ch_r "I don't know who you think you are, boss'in me around like that." 
                        if "followed" not in R_RecentActions:                           
                            call Statup("Rogue", "Inbt", 40, 2)
                            call Statup("Rogue", "Inbt", 60, 1)    
                            call Statup("Rogue", "Obed", 70, -2)
                        ch_r "If you want to see me, you know where to find me."                    
                    else:                                                                   
                        #she is obedient, but you failed to meet the checks
                        if "followed" not in R_RecentActions:
                            call Statup("Rogue", "Inbt", 30, 1)
                            call Statup("Rogue", "Inbt", 50, 1)                                    
                            call Statup("Rogue", "Love", 50, -1, 1)
                            call Statup("Rogue", "Obed", 70, -1)  
                        $ Line = "no" 
                    #End ordered to stay
                    
        $ R_RecentActions.append("followed")
        if not Line:                                                                        
                #You end the dialog neutrally
                hide Rogue
                call Gym_Clothes("auto", "Rogue")
                return
        
        if Line == "no":                                                                    
                # She's refused, context based dialog
                if R_Loc == "bg classroom":
                    ch_r "I seriously can't, [R_Petname], big test coming up." 
                elif R_Loc == "bg dangerroom": 
                    ch_r "Wish I could, [R_Petname], but I need to get some hours in."
                else:
                    ch_r "I'm sorry, [R_Petname], but I'm kinda busy right now."      
                hide Rogue
                call Gym_Clothes("auto", "Rogue")      
                return
            
        elif Line == "go to":                                                                 
                #You agreed to go to her instead  
                $ Tempmod = 0
                call DrainWord("All","leaving")  
                call DrainWord("All","arriving")             
                hide Rogue
                call Gym_Clothes("auto", "Rogue")
                if R_Loc == "bg classroom":
                    ch_r "See you then!"            
                    jump Class_Room_Entry 
                elif R_Loc == "bg dangerroom": 
                    ch_r "I'll be warming up!"         
                    jump Danger_Room_Entry
                elif R_Loc == "bg rogue": 
                    ch_r "I'll meet you there."
                    jump Rogue_Room
                elif R_Loc == "bg player": 
                    ch_r "I'll be waiting."
                    jump Player_Room                
                elif R_Loc == "bg showerroom": 
                    ch_r "I guess I'll see you there."
                    jump Shower_Room_Entry
                elif R_Loc == "bg campus": 
                    ch_r "Let's head over there."
                    jump Campus_Entry
                else:
                    ch_r "You know, I'll just meet you in my room."
                    $ R_Loc = "bg rogue"
                    jump Rogue_Room
                #End "goto" where she's at
                
        #She's agreed to come over    
        elif Line == "lonely":
                ch_r "Oh, how could I say \"no\" to you, [R_Petname]?"
        elif Line == "command": 
                ch_r "Fine, if you insist, [R_Petname]."
        
        $ Line = 0
        ch_r "I can stay for a bit."                                
        $ R_Loc = bg_current 
        return

# End Rogue Leave ///////////////////    

label Rogue_Dismissed(Leaving = 0):
    if "Rogue" in Party:        
            $ Party.remove("Rogue")
    call Rogue_Schedule(0) #if R_Loc == bg_current then it means she wants to stay here
    if "leaving" in R_RecentActions:
            call DrainWord("Rogue","leaving")   
    menu:
        "You can leave if you like.":
                if R_Loc == bg_current and not ApprovalCheck("Rogue", 700, "O"):
                        ch_r "Thanks, but I think I'll stick around."
                else:
                        ch_r "Sure, ok. See you later."
                        $ Leaving = 1           
        "Could you give me the room please?":                            
                if R_Loc == bg_current and not ApprovalCheck("Rogue", 800, "LO"):
                        ch_r "I'd rather stick around."
                elif not ApprovalCheck("Rogue", 500, "LO"):
                        ch_r "I think I should probably stick around."
                else:
                        if "dismissed" not in R_DailyActions:
                                call Statup("Rogue", "Obed", 30, 5)
                                call Statup("Rogue", "Obed", 50, 5)
                        ch_r "Not a problem, see you later then."   
                        $ Leaving = 1                    
        "You can go now.":                         
                if R_Loc == bg_current and not ApprovalCheck("Rogue", 500, "O"):
                        ch_r "I think I'll stay."         
                elif not ApprovalCheck("Rogue", 300, "O"):
                        call RogueFace("confused") 
                        ch_r "Well if you want me to go, then maybe I should stick around."
                else:
                        if "dismissed" not in R_DailyActions:
                                call Statup("Rogue", "Obed", 40, 10)
                                call Statup("Rogue", "Obed", 60, 5)
                        ch_r "If you wish."     
                        $ Leaving = 1                  
        "Nevermind.":
                        return                             
    
    if not Leaving and bg_current in ("bg campus","bg classroom","bg dangerroom"):
            #if there is space nearby. . .
            call Remove_Girl("Rogue",1,1)
    elif not Leaving:     
            menu:
                extend ""
                "I insist, get going.":  
                        if R_Loc != bg_current and (ApprovalCheck("Rogue", 1200, "LO") or ApprovalCheck("Rogue", 500, "O")):
                                #If she has someplace to be and is obedient
                                if "dismissed" not in R_DailyActions:
                                        call Statup("Rogue", "Love", 70, -5, 1)
                                        call Statup("Rogue", "Obed", 50, 10)
                                        call Statup("Rogue", "Obed", 80, 5)
                                ch_r "Ok, if you insist." 
                                $ Leaving = 1           
                        elif R_Loc != bg_current and (ApprovalCheck("Rogue", 1000, "LO") or ApprovalCheck("Rogue", 300, "O")):
                                #If she has someplace to be and is less obedient
                                if "dismissed" not in R_DailyActions:
                                        call Statup("Rogue", "Love", 50, -5, 1)
                                        call Statup("Rogue", "Love", 70, -5, 1)
                                        call Statup("Rogue", "Obed", 50, 10)
                                        call Statup("Rogue", "Obed", 80, 5)
                                call RogueFace("angry") 
                                ch_r "Fine, if you're going to be a dick about it."
                                $ Leaving = 1           
                        elif R_Loc != bg_current:
                                #If she has someplace to be but is not obedient
                                if "dismissed" not in R_DailyActions:
                                        call Statup("Rogue", "Love", 50, -5, 1)
                                        call Statup("Rogue", "Love", 70, -10, 1)
                                        call Statup("Rogue", "Obed", 50, -5)
                                        call Statup("Rogue", "Inbt", 50, 5)
                                        call Statup("Rogue", "Inbt", 80, 3)
                                call RogueFace("angry") 
                                ch_r "Like hell I will."   
                        elif ApprovalCheck("Rogue", 1400, "LO") or ApprovalCheck("Rogue", 400, "O"):
                                #If she has nowhere to be to be but is obedient
                                if "dismissed" not in R_DailyActions:
                                        call Statup("Rogue", "Love", 50, -5, 1)
                                        call Statup("Rogue", "Obed", 50, 10)
                                        call Statup("Rogue", "Obed", 80, 5)
                                call RogueFace("sad") 
                                ch_r "Ok, if that's what you want."
                                $ Leaving = 1           
                        else:
                                #If she has nowhere to be to be and is not obedient
                                if "dismissed" not in R_DailyActions:
                                        call Statup("Rogue", "Love", 50, -5, 1)
                                        call Statup("Rogue", "Love", 70, -10, 1)
                                        call Statup("Rogue", "Obed", 50, -5)
                                        call Statup("Rogue", "Inbt", 50, 3)
                                        call Statup("Rogue", "Inbt", 80, 2)
                                call RogueFace("sad") 
                                ch_r "You wish."           
                "Ok, nevermind.":
                                pass               
                    
    if "dismissed" not in R_DailyActions:
            $ R_DailyActions.append("dismissed")  
    if "Rogue" in Nearby:
        "You shift a bit away from Rogue"
    elif Leaving == 0:
            # Stay
            $ R_Loc = bg_current
    else:
            # Go
            if R_Loc != bg_current: #it stays the same
                pass
            elif bg_current == "bg rogue":
                $ R_Loc = "bg campus"
            else:
                $ R_Loc = "bg rogue"
            hide Rogue
            "Rogue heads out." 
    return
    #end "you can leave"

# Rogue's Clothes  // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // //
label Rogue_Clothes:   
    $ Trigger = 1 # to prevent Focus swapping. . .    
    call RogueFace
    menu:
        ch_r "So what did you want to tell me about my clothes again?"
        "Overshirts":
                jump Rogue_Clothes_Over        
        "Legwear":
                jump Rogue_Clothes_Legs
        "Underwear":
                jump Rogue_Clothes_Under
        "Accessories":
                jump Rogue_Clothes_Misc
        "Outfit Management":
                jump Rogue_Clothes_Outfits  
        "Let's talk about what you wear around.":
                call Rogue_Clothes_Schedule
                           
        "Could I get a look at it?" if R_Loc != bg_current:
                # checks to see if she'll drop the screen
                call Rogue_OutfitShame(0,2) 
                if _return:                    
                    show PhoneSex zorder 150
                    ch_r "How's that? . ."
                hide PhoneSex
        "Could I get a look at it?" if renpy.showing('DressScreen'):
                # checks to see if she'll drop the screen
                call Rogue_OutfitShame(0,2) 
                if _return:
                    hide DressScreen
        "Would you be more comfortable behind a screen? (locked)" if R_Taboo:
                pass
        "Would you be more comfortable behind a screen?" if R_Loc == bg_current and not R_Taboo and not renpy.showing('DressScreen'):
                # checks to see if she'll drop the screen
                if ApprovalCheck("Rogue", 1500) or (R_SeenChest and R_SeenPussy):
                        ch_r "Don't really need that, thanks."
                else:
                        show DressScreen zorder 150
                        ch_r "This is more comfortable, thanks."
                        
        "Switch to. . .":
                if renpy.showing('DressScreen'):
                        call Rogue_OutfitShame(0,2) 
                        if _return:
                            hide DressScreen
                        else:
                            call RogueOutfit 
                $ R_TempClothes[1] = R_Arms  
                $ R_TempClothes[2] = R_Legs 
                $ R_TempClothes[3] = R_Over
                $ R_TempClothes[4] = R_Neck 
                $ R_TempClothes[5] = R_Chest 
                $ R_TempClothes[6] = R_Panties
#                $ R_TempClothes[7] = R_Boots
                $ R_TempClothes[8] = R_Hair
                $ R_TempClothes[9] = R_Hose
                $ R_TempClothes[0] = 1 
                $ R_Outfit = "temporary"
                $ R_OutfitDay = "temporary"  
                $ Trigger = 0
                menu:
                    "Kitty":
                        call Kitty_Chat_Set("wardrobe")                    
                    "Emma":
                        call Emma_Chat_Set("wardrobe") 
                    "Laura":
                        call Laura_Chat_Set("wardrobe") 
                    "Never mind":
                        pass  
                        
        "Never mind, you look good like that. [[return]":            
                if "wardrobe" not in R_RecentActions:  
                        #Apply stat boosts only if it's the first time this turn
                        if R_Chat[1] <= 1:                
                                call Statup("Rogue", "Love", 70, 10)
                                call Statup("Rogue", "Obed", 20, 10)
                                ch_r "Aw, that's sweet."
                        elif R_Chat[1] <= 10:
                                call Statup("Rogue", "Love", 70, 5)
                                call Statup("Rogue", "Obed", 20, 5)
                                ch_r "Thanks." 
                        elif R_Chat[1] <= 50:
                                call Statup("Rogue", "Love", 70, 1)
                                call Statup("Rogue", "Obed", 20, 1) 
                                ch_r "Ok."
                        else:
                                ch_r "Ok."
                        $ R_RecentActions.append("wardrobe")  
                if renpy.showing('DressScreen'):
                        call Rogue_OutfitShame(0,2) 
                        if _return:
                            hide DressScreen
                        else:
                            call RogueOutfit 
                #sets up a temporary outfit
                $ R_TempClothes[1] = R_Arms  
                $ R_TempClothes[2] = R_Legs 
                $ R_TempClothes[3] = R_Over
                $ R_TempClothes[4] = R_Neck 
                $ R_TempClothes[5] = R_Chest 
                $ R_TempClothes[6] = R_Panties
#                $ R_TempClothes[7] = R_Boots
                $ R_TempClothes[8] = R_Hair
                $ R_TempClothes[9] = R_Hose
                $ R_TempClothes[0] = 1 
                $ R_Outfit = "temporary"
                $ R_OutfitDay = "temporary"  
                $ R_Chat[1] += 1
                $ Trigger = 0
                return
                
    jump Rogue_Clothes
    #End of Rogue Wardrobe Main Menu

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Rogue_Clothes_Outfits:                                                                               
        # Outfits
        "That looks really good on you, you should remember that one. [[Set Custom]":
                menu:
                    "Which slot would you like this saved in?"
                    "Custom 1":
                                call Rogue_OutfitShame(3,1)
                    "Custom 2":
                                call Rogue_OutfitShame(5,1)
                    "Custom 3":
                                call Rogue_OutfitShame(6,1)
                    "Gym Clothes":
                                call Rogue_OutfitShame(4,1)                    
                    "Sleepwear":
                                call Rogue_OutfitShame(7,1)                      
                    "Swimwear":
                                call Rogue_OutfitShame(10,1)   
                    "Never mind":
                                pass   
                                
        "I really like that green top and skirt outfit you have.":                  
                #Green
                call RogueOutfit("evo_green")   
                menu:
                    "You should wear this one out. [[set current outfit]":
                        $ R_Outfit = "evo_green"
                        $ R_Shame = R_OutfitShame[1]
                        ch_r "Ok, [R_Petname], I like this one too."
                    "Let's try something else though.":
                        ch_r "Sure."            
                    
        "That pink top and pants look really nice on you.":                        
                #Pink  
                call RogueOutfit("evo_pink")
                menu:
                    "You should wear this one out. [[set current outfit]":
                        $ R_Outfit = "evo_pink"
                        $ R_Shame = R_OutfitShame[2]
                        ch_r "Sure, [R_Petname], that one's nice."
                    "Let's try something else though.":
                        ch_r "Ok."            
                    
        "Remember that outfit we put together? [[Set a custom outfit] (locked)" if not R_Custom[0] and not R_Custom2[0] and not R_Custom3[0]:
                        pass       
                        
        "Remember that outfit we put together?" if R_Custom[0] or R_Custom2[0] or R_Custom3[0]: 
                        $ Cnt = 0
                        while 1:
                            menu:                
                                "Throw on Custom 1 (locked)" if not R_Custom[0]:
                                        pass
                                "Throw on Custom 1" if R_Custom[0]:
                                        call RogueOutfit("custom1")
                                        $ Cnt = 3
                                "Throw on Custom 2 (locked)" if not R_Custom2[0]:
                                        pass
                                "Throw on Custom 2" if R_Custom2[0]:
                                        call RogueOutfit("custom2")
                                        $ Cnt = 5
                                "Throw on Custom 3 (locked)" if not R_Custom3[0]:
                                        pass
                                "Throw on Custom 3" if R_Custom3[0]:
                                        call RogueOutfit("custom3")
                                        $ Cnt = 6
                                
                                "You should wear this one in private. (locked)" if not Cnt:
                                        pass
                                "You should wear this one in private." if Cnt:
                                        if Cnt == 5:
                                            $ R_Schedule[9] = "custom2"
                                        elif Cnt == 6:
                                            $ R_Schedule[9] = "custom3"
                                        else:
                                            $ R_Schedule[9] = "custom"
                                        ch_r "Ok, sure."
                                
                                "On second thought, forget about that one outfit. . .":
                                        menu:
                                            ch_r "Which one did you mean?"
                                            "Custom 1 [[clear custom 1]" if R_Custom[0]:
                                                ch_r "Ok, no problem."
                                                $ R_Custom[0] = 0
                                            "Custom 1 [[clear custom 1] (locked)" if not R_Custom[0]:
                                                pass
                                            "Custom 2 [[clear custom 2]" if R_Custom2[0]:
                                                ch_r "Ok, no problem."
                                                $ R_Custom2[0] = 0
                                            "Custom 2 [[clear custom 2] (locked)" if not R_Custom2[0]:
                                                pass
                                            "Custom 3 [[clear custom 3]" if R_Custom3[0]:
                                                ch_r "Ok, no problem."
                                                $ R_Custom3[0] = 0
                                            "Custom 3 [[clear custom 3] (locked)" if not R_Custom3[0]:
                                                pass
                                            "Never mind, [[back].":
                                                pass            
                                        
                                "You should wear this one out. [[choose outfit first](locked)" if not Cnt:
                                    pass
                                "You should wear this one out." if Cnt:
                                    call Rogue_Custom_Out(Cnt)
                                "Ok, back to what we were talking about. . .":
                                    $ Cnt = 0
                                    jump Rogue_Clothes                               
        
        "Gym Clothes?" if not R_Taboo or bg_current == "bg dangerroom":
                call RogueOutfit("gym")
                
        "Sleepwear?" if not R_Taboo:
                if ApprovalCheck("Rogue", 1200):
                        call RogueOutfit("sleep")
                else:
                        call Display_DressScreen("Rogue")
                        if _return:
                            call RogueOutfit("sleep")
                                        
        "Swimwear?" if not R_Taboo or bg_current == "bg pool":
                call RogueOutfit("swimwear")
                            
        "Your birthday suit looks really great. . .":                                 
                #Nude
                call RogueFace("sexy", 1)
                $ Line = 0                        
                if not R_Chest and not R_Panties and not R_Over and not R_Legs and not R_Hose:                
                    ch_r "Can't get much more naked than this."  
                elif R_SeenChest and R_SeenPussy and ApprovalCheck("Rogue", 1000, TabM=5):
                    ch_r "Naughty boy. . ."  
                    $ Line = 1
                elif ApprovalCheck("Rogue", 2000, TabM=5):
                    ch_r "Hmm. . . you move fast, but I suppose for you. . ."    
                    $ Line = 1
                elif R_SeenChest and R_SeenPussy and ApprovalCheck("Rogue", 1000, TabM=0):
                    ch_r "Well, maybe if it weren't quite so. . . public here."  
                elif ApprovalCheck("Rogue", 2000, TabM=0):
                    ch_r "I might consider it if we had some privacy. . ."  
                elif ApprovalCheck("Rogue", 1000, TabM=0):                
                    call RogueFace("surprised", 1)
                    ch_r "Hmm. . . you're getting a bit ahead of yourself, [R_Petname]."
                else:
                    call RogueFace("angry", 1)
                    ch_r "What sort of common strumpet do you take me for?"  
                    
                if Line:                                                            #If she got nude. . .                            
                    call RogueOutfit("nude")
                    "She pulls all her clothes off and throws them in a heap on the floor."
                    call Rogue_First_Topless
                    call Rogue_First_Bottomless(1)
                    call RogueFace("sexy")
                    menu:
                        "You know, you should wear this one out. [[set current outfit]":
                            if "exhibitionist" in R_Traits:
                                ch_r "You sure know how to rev my engines. . ." 
                                $ R_Outfit = "nude"
                                $ R_Shame = R_OutfitShame[0]
                            elif ApprovalCheck("Rogue", 750, "I") or ApprovalCheck("Rogue", 2500, TabM=0):                    
                                ch_r "Heh, all right [R_Petname]."
                                $ R_Outfit = "nude"
                                $ R_Shame = R_OutfitShame[0]
                            else:
                                call RogueFace("sexy", 1)
                                $ R_Eyes = "surprised"
                                ch_r "I'm afraid not, [R_Petname], this is just for between you and me." 
                        "Let's try something else though.":
                            if "exhibitionist" in R_Traits:
                                ch_r "Hmm, too bad you didn't want me to wear this out. . ."                         
                            elif ApprovalCheck("Rogue", 750, "I") or ApprovalCheck("Rogue", 2500, TabM=0):       
                                call RogueFace("bemused", 1)             
                                ch_r "You know, for a second there I thought you might want me to wear this out. . ."
                                ch_r "Hehe, um. . ."
                            else:
                                call RogueFace("confused", 1)
                                ch_r "Well obviously. It's not like I'd ever go out like this."   
                $ Line = 0
                
        "Never mind":    
                        jump Rogue_Clothes     
            
    jump Rogue_Clothes
    #End of Rogue Outfits

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Rogue_Clothes_Over:                                                                                         
        # Overshirts    
        "Why don't you go with no [R_Over]?" if R_Over:
                call RogueFace("bemused", 1)
                if R_Chest or (R_SeenChest and ApprovalCheck("Rogue", 600)):
                    ch_r "Sure."
                elif ApprovalCheck("Rogue", 600, TabM=0):
                    call Rogue_NoBra
                    if not _return:
                        if not ApprovalCheck("Rogue", 1200):
                            call Display_DressScreen("Rogue")
                            if not _return:
                                jump Rogue_Clothes
                        else:
                                jump Rogue_Clothes
                else:
                    call Display_DressScreen("Rogue")
                    if not _return:
                            ch_r "I'd rather not. . ."
                            if not R_Chest:
                                ch_r "I'm afraid I don't have anything on under this."
                            jump Rogue_Clothes
                $ R_Over = 0
                if not R_Chest and not renpy.showing('DressScreen'):
                        call Rogue_First_Topless
                        
        "Try on the green mesh top." if R_Over != "mesh top":
                call RogueFace("bemused", 1)
                if R_Chest or (R_SeenChest and ApprovalCheck("Rogue", 500, TabM=2)):
                    ch_r "Sure."  
                elif ApprovalCheck("Rogue", 600, TabM=0):
                    call Rogue_NoBra
                    if not _return:
                        if not ApprovalCheck("Rogue", 1200):
                            call Display_DressScreen("Rogue")
                            if not _return:
                                jump Rogue_Clothes
                        else:
                                jump Rogue_Clothes
                else:
                    call Display_DressScreen("Rogue")
                    if not _return:
                            ch_r "I'm afraid that top is a bit sheer to have nothing under it."
                            if not R_Chest:
                                ch_r "I don't have anything on under this."
                            jump Rogue_Clothes
                            
                $ R_Over = "mesh top"    
                menu:
                    ch_r "With the collar?"
                    "Yes":
                        $ R_Neck = "spiked collar"
                    "No":
                        $ R_Neck = 0
                if R_Chest == "buttoned tank":
                    $ R_Chest = "tank"   
                if not R_Chest and not renpy.showing('DressScreen'):
                    call Rogue_First_Topless 
                            
        "How about that pink top?" if R_Over != "pink top":
                $ R_Over = "pink top"  
                $ R_Neck = 0
                        
        "How about that green hoodie?" if R_Over != "hoodie":
                $ R_Over = "hoodie"  
                        
        "Maybe just throw on a towel?" if R_Over != "towel":
                call RogueFace("bemused", 1)
                if R_Chest or R_SeenChest:
                    ch_r "Fresh."
                elif ApprovalCheck("Rogue", 900, TabM=0):
                    call RogueFace("perplexed", 1)
                    ch_r "I suppose? . ."          
                else:
                    call Display_DressScreen("Rogue")
                    if not _return:
                            ch_r "That don't leave much to the imagination. . ."
                            jump Rogue_Clothes
                $ R_Over = "towel"  
            
        "How about that green nighty I got you?" if R_Over != "nighty" and "nighty" in R_Inventory:
                if R_Legs:
                    ch_r "I can't really wear that with my [R_Legs] on."
                elif ApprovalCheck("Rogue", 1100, TabM=3):
                    ch_r "Sure. . ."
                    if "lace bra" in R_Inventory:
                        $ R_Chest = "lace bra"
                    else:
                        $ R_Chest = "bra"
                    if "lace panties" in R_Inventory:
                        $ R_Panties = "lace panties"
                    else:
                        $ R_Panties = "black panties"
                    $ R_Over = "nighty"   
                    menu:
                        extend ""
                        "Nice.":
                            pass
                        "I meant {i}just{/i} the nighty.":
                            if ApprovalCheck("Rogue", 1400, TabM=3):
                                "She shrugs off her bra and then pulls the nighty back up."
                                $ R_Panties = 0
                                $ R_Chest = 0
                                ch_r "Hmmm, alright. . ."
                            elif ApprovalCheck("Rogue", 1200, TabM=3):
                                $ R_Chest = 0
                                ch_r "I'll keep my panties on, thanks."
                            else:
                                ch_r "Be happy with what you get."
                else:
                    call Display_DressScreen("Rogue")
                    if not _return:
                            ch_r "That's a bit . . . revealing."
                            jump Rogue_Clothes
                if not R_Chest and not renpy.showing('DressScreen'):
                    call Rogue_First_Topless
                
        "Never mind":
            pass           
    jump Rogue_Clothes
    #End of Rogue Top
                       
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    label Rogue_NoBra:
        menu:
            ch_r "I don't have anything under this. . ."
            "Then you could slip something on under it. . .":   
                        if R_SeenChest and ApprovalCheck("Rogue", 1000, TabM=3) or ApprovalCheck("Rogue", 1200, TabM=4):
                                $ R_Blush = 2
                                ch_r "'course, I don't exactly need something under it either. . ."
                                $ R_Blush = 1                
                        elif ApprovalCheck("Rogue", 900, TabM=2) and "lace bra" in R_Inventory:
                                ch_r "I suppose this would work. . ."
                                $ R_Chest  = "lace bra"    
                                "She pulls out her lace bra and slips it on under her [R_Over]."
                        elif ApprovalCheck("Rogue", 800, TabM=2):
                                ch_r "Yeah, I guess."
                                $ R_Chest = "bra"
                                "She pulls out her bra and slips it on under her [R_Over]."
                        elif ApprovalCheck("Rogue", 600, TabM=2):
                                ch_r "Yeah, I guess."
                                $ R_Chest = "tank"
                                "She pulls out her tanktop and slips it on under her [R_Over]."
                        else:
                                ch_r "Yeah, I don't think so."
                                return 0
                        
            "You could always just wear nothing at all. . .":
                        if ApprovalCheck("Rogue", 1100, "LI", TabM=2) and R_Love > R_Inbt:               
                                ch_r "I suppose I could. . ."
                        elif ApprovalCheck("Rogue", 700, "OI", TabM=2) and R_Obed > R_Inbt:
                                ch_r "Sure. . ."
                        elif ApprovalCheck("Rogue", 600, "I", TabM=2):
                                ch_r "Yeah. . ."
                        elif ApprovalCheck("Rogue", 1300, TabM=2):
                                ch_r "Okay, fine."
                        else: 
                                call RogueFace("surprised")
                                $ R_Brows = "angry"
                                if R_Taboo > 20:
                                    ch_r "Not in public, [R_Petname]!"
                                else:
                                    ch_r "Don't push it, [R_Petname]."
                                return 0
                                
                    
            "Never mind.":
                        ch_r "Ok. . ."
                        return 0
        return 1
        #End of Rogue bra check
       
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<                      
                       
    menu Rogue_Clothes_Legs:                                                                                                   
        # Leggings   
        "Maybe go without the [R_Legs]." if R_Legs:
                call RogueFace("sexy", 1)
                if R_SeenPanties and R_Panties and ApprovalCheck("Rogue", 500, TabM=5):
                    ch_r "Sure."
                elif R_SeenPussy and ApprovalCheck("Rogue", 900, TabM=4):
                    ch_r "Sure, why not?"             
                elif ApprovalCheck("Rogue", 1300, TabM=2) and R_Panties:
                    ch_r "Well, I suppose if it's for you. . ."                         
                elif ApprovalCheck("Rogue", 700) and not R_Panties:
                    call Rogue_NoPantiesOn
                    if not _return and not R_Panties:
                        if not ApprovalCheck("Rogue", 1500):
                            call Display_DressScreen("Rogue")
                            if not _return:
                                jump Rogue_Clothes
                        else:
                                jump Rogue_Clothes
                else:
                    call Display_DressScreen("Rogue")
                    if not _return:
                        ch_r "Not in front of you, [R_Petname]."
                        if not R_Panties:
                            ch_r "Maybe if I put some panties on first. . ."
                        jump Rogue_Clothes
                if R_Legs == "leather pants" or R_Legs == "mesh pants":
                        $ R_Legs = 0    
                        "She tugs her pants off and drops them to the ground."
                else:
                        $ R_Legs = 0    
                        "She tugs her skirt off and drops it to the ground."
                if renpy.showing('DressScreen'):
                    pass
                elif R_Panties:                
                    $ R_SeenPanties = 1
                else:
                    call Rogue_First_Bottomless
                                                    
        "How about that skirt?" if R_Legs != "skirt":  
                $ R_Legs = "skirt"
                $ R_Upskirt = 0
                                            
        "Your ass looks tight in those jeans." if R_Legs != "pants":
                $ R_Legs = "pants"
                $ R_Hose = 0
                
        "The tights would look good with that." if R_Hose != 'tights' and R_Legs != "pants":     
                $ R_Hose = "tights"                   
        "Your ripped tights would look good with that." if R_Hose != 'ripped tights' and "ripped tights" in R_Inventory and R_Legs != "pants":     
                $ R_Hose = "ripped tights"           
        "You could lose the tights." if R_Hose == 'ripped tights' or R_Hose == 'tights':     
                $ R_Hose = 0  
            
        "What about wearing your shorts?" if R_Panties != "shorts":
                ch_r "Alright."
                $ R_Panties = "shorts"            
        "Why don't you lose the shorts?" if R_Panties == "shorts":
                call RogueFace("sexy", 1)
                if R_SeenPanties and R_Panties and ApprovalCheck("Rogue", 500, TabM=5):
                    ch_r "Sure."
                elif R_SeenPussy and ApprovalCheck("Rogue", 900, TabM=4):
                    ch_r "Sure, why not?"             
                elif ApprovalCheck("Rogue", 1300, TabM=2) and R_Panties:
                    ch_r "Well, I suppose if it's for you. . ."   
                elif ApprovalCheck("Rogue", 700) and not R_Panties:
                    call Rogue_NoPantiesOn
                    if not _return and not R_Panties:
                        if not ApprovalCheck("Rogue", 1500):
                            call Display_DressScreen("Rogue")
                            if not _return:
                                jump Rogue_Clothes
                        else:
                                jump Rogue_Clothes
                else:
                    call Display_DressScreen("Rogue")
                    if not _return:
                        ch_r "Not in front of you, [R_Petname]."
                        if not R_Panties:
                            ch_r "Maybe if I put some panties on first. . ."
                        jump Rogue_Clothes
                if R_Panties == "shorts":
                        $ R_Panties = 0
                "She tugs her shorts off and drops them to the ground."
                if renpy.showing('DressScreen'):
                    pass
                elif R_Panties:                
                    $ R_SeenPanties = 1
                else:
                    call Rogue_First_Bottomless
                    
        "Never mind":
            pass
    jump Rogue_Clothes
    #End of Rogue Pants
   
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
    
    label Rogue_NoPantiesOn:
        menu:
            ch_r "I'm not wearing anything under these, you know. . ."
            "Then you could slip on a pair of panties. . .":   
                        if R_SeenPussy and ApprovalCheck("Rogue", 1100, TabM=4):
                                $ R_Blush = 1
                                ch_r "Alright."       
                                $ R_Blush = 0                        
                        elif ApprovalCheck("Rogue", 1500, TabM=4):
                                $ R_Blush = 1
                                ch_r "Alright."       
                                $ R_Blush = 0                
                        elif ApprovalCheck("Rogue", 800, TabM=4) and "lace panties" in R_Inventory:
                                ch_r "I like how you think."
                                $ R_Panties  = "lace panties"  
                                if ApprovalCheck("Rogue", 1200, TabM=4) and R_Legs:   
                                    $ Line = R_Legs
                                    $ R_Legs = 0
                                    "She pulls off her [R_Legs] and slips on the lace panties."                                    
                                elif R_Legs == "skirt":
                                    "She pulls out her lace panties and pulls them up under her skirt."
                                    $ R_Legs = 0
                                    "Then she drops the skirt to the floor."
                                else:
                                    $ Line = R_Legs
                                    $ R_Legs = 0
                                    "She steps away a moment and then comes back wearing only the lace panties."                                     
                                jump Rogue_Clothes
                        elif ApprovalCheck("Rogue", 700, TabM=4):
                                ch_r "Yeah, I guess."
                                $ R_Panties = "black panties"
                                if ApprovalCheck("Rogue", 1200, TabM=4) and R_Legs:   
                                    $ Line = R_Legs
                                    $ R_Legs = 0
                                    "She pulls off her [R_Legs] and slips on the black panties."                                    
                                elif R_Legs == "skirt":
                                    "She pulls out her black panties and pulls them up under her skirt."
                                    $ R_Legs = 0
                                    "Then she drops the skirt to the floor."
                                else:
                                    $ Line = R_Legs
                                    $ R_Legs = 0
                                    "She steps away a moment and then comes back wearing only the black panties."                                     
                                jump Rogue_Clothes
                        else:
                                ch_r "Nope."
                                return 0
                        
            "You could always just wear nothing at all. . .":
                    if ApprovalCheck("Rogue", 1100, "LI", TabM=3) and R_Love > R_Inbt:               
                            ch_r "Well aren't you cheeky. . . I suppose I could give you a show. . ."
                    elif ApprovalCheck("Rogue", 750, "OI", TabM=3) and R_Obed > R_Inbt:
                            ch_r "If that's what you want."
                    elif ApprovalCheck("Rogue", 500, "I", TabM=3):
                            ch_r "Oooh, naughty."
                    elif ApprovalCheck("Rogue", 1400, TabM=3):
                            ch_r "Oh, fine. You've been a good boy."
                    else: 
                            call RogueFace("surprised")
                            $ R_Brows = "angry"
                            if R_Taboo:
                                ch_r "Not here,[R_Petname]!"
                            else:
                                ch_r "Not with you around,[R_Petname]!"
                            return 0
                                                        
            "Never mind.":
                ch_r "Ok. . ."
                return 0
        return 1
        #End of Rogue Panties check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
    menu Rogue_Clothes_Under:
        "Tops":
            menu:
                "How about you lose the [R_Chest]?" if R_Chest:
                        call RogueFace("bemused", 1)                        
                        if R_SeenChest and ApprovalCheck("Rogue", 1100, TabM=2):
                            ch_r "Sure."    
                        elif ApprovalCheck("Rogue", 1100, TabM=2):
                            ch_r "I guess I don't really mind if you see them. . ."
                        elif R_Over == "hoodie" and ApprovalCheck("Rogue", 500, TabM=2):
                            ch_r "I guess this covers enough. . ."  
                        elif not R_SeenChest and not ApprovalCheck("Rogue", 1100):
                                call Display_DressScreen("Rogue")
                                if not _return:
                                    if R_Over == "pink top" and ApprovalCheck("Rogue", 950, TabM=2):
                                        ch_r "This look is a bit revealing. . ."  
                                    elif R_Over == "mesh top":
                                        ch_r "In this top? That would leave nothing to the imagination!" 
                                    elif not R_Over:
                                        ch_r "Not without a little coverage, for modesty."
                                    else:
                                        ch_r "I don't think so, [R_Petname]."
                                    jump Rogue_Clothes 
                        $ Line = R_Chest
                        $ R_Chest = 0
                        if R_Over:
                            "She reaches into her [R_Over] grabs her [Line], and pulls it out, dropping it to the ground."
                        else:
                            "She lets her [Line] fall to the ground."
                        if (not R_Over or R_Over == "mesh top") and not renpy.showing('DressScreen'):
                            call Rogue_First_Topless

                "Try on that black tank top." if R_Chest != "tank":
                        $ R_Chest = "tank"            
                "I like that buttoned tank top." if R_Chest != "buttoned tank" and R_Over != "mesh top":
                        $ R_Chest = "buttoned tank"  
                    
                "I like that sports bra." if R_Chest != "sports bra":
                        if (R_SeenChest and ApprovalCheck("Rogue", 600)) or ApprovalCheck("Rogue", 900, TabM=2):
                            ch_r "Sure."   
                            $ R_Chest = "sports bra"         
                        else:                
                            call Display_DressScreen("Rogue")
                            if not _return:
                                ch_r "I don't know about wearing it with this. . ." 
                                jump Rogue_Clothes 
                                    
                "I like that black bra." if R_Chest != "bra":
                        if (R_SeenChest and ApprovalCheck("Rogue", 600)) or ApprovalCheck("Rogue", 1100, TabM=2):
                            ch_r "Sure."   
                            $ R_Chest = "bra"         
                        else:          
                            call Display_DressScreen("Rogue")
                            if not _return:
                                ch_r "That's a bit too revealing. . ." 
                                jump Rogue_Clothes      
                                
                "I like that lace bra." if "lace bra" in R_Inventory and R_Chest != "lace bra":
                        if (R_SeenChest and ApprovalCheck("Rogue", 800)) or ApprovalCheck("Rogue", 1100, TabM=2):
                            ch_r "Sure."   
                            $ R_Chest = "lace bra"         
                        else:                
                            call Display_DressScreen("Rogue")
                            if not _return:
                                ch_r "That's a bit too revealing. . ." 
                                jump Rogue_Clothes   
                
                "I like that bikini top." if R_Chest != "bikini top" and "bikini top" in R_Inventory:
                        if bg_current == "bg pool":
                                ch_r "Sure."   
                                $ R_Chest = "bikini top"         
                        else:                
                                if R_SeenChest or ApprovalCheck("Rogue", 1000, TabM=2):
                                    ch_r "Sure."   
                                    $ R_Chest = "bikini top"         
                                else:             
                                    call Display_DressScreen("Rogue")
                                    if not _return:
                                        ch_r "I kinda don't feel right about that. . ." 
                                        jump Rogue_Clothes       
                        
                "Never mind":
                            pass
            jump Rogue_Clothes_Under
                                    
                                    
        "Hose and stockings options":
            menu:          
                "You could lose the hose." if R_Hose and R_Hose != 'ripped tights' and R_Hose != 'tights':     
                        $ R_Hose = 0  
                "The thigh-high hose would look good with that." if R_Hose != "stockings" and R_Legs != "pants":     
                        $ R_Hose = "stockings"  
                "The pantyhose would look good with that." if R_Hose != "pantyhose" and R_Legs != "pants":     
                        $ R_Hose = "pantyhose" 
                "The stockings would look good with that." if R_Hose != "stockings and garterbelt" and "stockings and garterbelt" in R_Inventory and R_Legs != "pants":     
                        $ R_Hose = "stockings and garterbelt"  
                "Maybe just the garterbelt?" if R_Hose != "garterbelt" and "stockings and garterbelt" in R_Inventory and R_Legs != "pants":     
                        $ R_Hose = "garterbelt"  
                "Your ripped pantyhose would look good with that." if R_Hose != "ripped pantyhose" and "ripped pantyhose" in R_Inventory and R_Legs != "pants":     
                        $ R_Hose = "ripped pantyhose"    
                "Never mind":
                        pass  
            jump Rogue_Clothes_Under
        
        "Panties":
            menu:
                
                "You could lose those panties. . ." if R_Panties and R_Panties != "shorts":
                        call RogueFace("bemused", 1)
                        if (R_SeenPussy and ApprovalCheck("Rogue", 900)) and not R_Taboo: # You've seen her pussy
                            if ApprovalCheck("Rogue", 850, "L", TabM=2):               
                                ch_r "Well aren't you cheeky. . ."
                            elif ApprovalCheck("Rogue", 500, "O", TabM=2):
                                ch_r "Fine by me."
                            elif ApprovalCheck("Rogue", 350, "I", TabM=2):
                                ch_r "Oooh, naughty."                            
                            else:
                                ch_r "Oh, I guess I could."         
                        else:                       #You've never seen it
                            if ApprovalCheck("Rogue", 1100, "LI", TabM=2):               
                                ch_r "Well aren't you cheeky. . . I suppose I could give you a show. . ."
                            elif ApprovalCheck("Rogue", 750, "OI", TabM=2):
                                ch_r "If that's what you want."
                            elif ApprovalCheck("Rogue", 500, "I", TabM=2):
                                ch_r "Oooh, naughty."
                            elif ApprovalCheck("Rogue", 1400, TabM=3):
                                ch_r "Oh, fine. You've been a good boy."
                            else: 
                                call Display_DressScreen("Rogue")
                                if not _return:
                                    call RogueFace("surprised")
                                    $ R_Brows = "angry" 
                                    if R_Taboo > 20:
                                        ch_r "Not in public, [R_Petname]!"
                                    else:
                                        ch_r "Not with you around,[R_Petname]!"
                                    jump Rogue_Clothes
                        $ Line = R_Panties
                        $ R_Panties = 0  
                        if R_Legs == "skirt":
                            "She reaches under her skirt and pulls her [Line] out, droping them to the ground." 
                        elif R_Legs:
                            if renpy.showing('DressScreen') or ApprovalCheck("Rogue", 1400, TabM=3):
                                    "She pulls down her [R_Legs], removes her [Line], and then pulls them back on."
                            else:
                                    "She steps away for a moment."
                        else:
                            "She pulls her [Line] off and drops them to the ground."
                        if not R_Legs and not renpy.showing('DressScreen'):
                            call Rogue_First_Bottomless
                            call Statup("Rogue", "Inbt", 50, 2)  
                                
                                        
                "Why don't you wear the green panties instead?" if R_Panties and R_Panties != "green panties":
                        if ApprovalCheck("Rogue", 1000, TabM=3):
                            ch_r "Sure, ok."
                            $ R_Panties = "green panties"  
                        elif R_Panties == "shorts":
                            ch_r "Heh, no, I think I'll stick with these, thanks."
                        else:
                            call Display_DressScreen("Rogue")
                            if not _return:
                                ch_r "I think I'll choose my own underwear, thank you."
                        
                "Why don't you wear the black panties instead?" if R_Panties and R_Panties != "black panties":
                        if ApprovalCheck("Rogue", 1100, TabM=3):
                            ch_r "Sure."
                            $ R_Panties = "black panties"
                        elif R_Panties == "shorts":
                            ch_r "Heh, no, I think I'll stick with these, thanks."
                        else:
                            call Display_DressScreen("Rogue")
                            if not _return:
                                ch_r "I don't see how that's any business of yours, [R_Petname]."
                                    
                "Why don't you wear the lace panties instead?" if "lace panties" in R_Inventory and R_Panties and R_Panties != "lace panties":
                        if ApprovalCheck("Rogue", 1200, TabM=3):
                            ch_r "Sure."
                            $ R_Panties = "lace panties"
                        elif R_Panties == "shorts":
                            ch_r "Heh, no, I think I'll stick with these, thanks."
                        else:
                            call Display_DressScreen("Rogue")
                            if not _return:
                                ch_r "I don't see how that's any business of yours, [R_Petname]."
                                    
                "I like those bikini bottoms." if R_Panties != "bikini bottoms" and "bikini bottoms" in R_Inventory:
                        if bg_current == "bg pool":
                            ch_r "Sure."   
                            $ R_Panties = "bikini bottoms"         
                        else:                
                            if ApprovalCheck("Rogue", 1000, TabM=2):
                                ch_r "Sure."   
                                $ R_Panties = "bikini bottoms"         
                            else:        
                                call Display_DressScreen("Rogue")
                                if not _return:        
                                    ch_r "I kinda don't feel right about that. . ."  
                "You know, you could wear some panties with that. . ." if not R_Panties:
                        call RogueFace("bemused", 1)
                        if (R_Love+R_Obed) <= (1.5 * R_Inbt):
                            $ R_Mouth = "smile"
                            ch_r "No thanks, [R_Petname]."
                            menu:
                                "Fine by me":
                                    jump Rogue_Clothes
                                "I insist, put some on.":
                                    if (R_Love+R_Obed) <= R_Inbt:
                                        call RogueFace("angry")
                                        ch_r "Well too bad."
                                        jump Rogue_Clothes
                                    else:
                                        call RogueFace("sadside")
                                        ch_r "Well! Fine." 
                        menu:
                            extend ""
                            "How about the green ones?":
                                ch_r "Sure, ok."
                                $ R_Panties = "green panties"
                            "How about the black ones?":
                                ch_r "Alright."                
                                $ R_Panties  = "black panties"
                            "How about the lace ones?" if "lace panties" in R_Inventory:
                                ch_r "Alright."                
                                $ R_Panties  = "lace panties"
                                
                "Never mind":
                        pass
            jump Rogue_Clothes_Under
        "Never mind":
                        pass
    jump Rogue_Clothes
    #End of Rogue Underwear
    
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<    
            
    menu Rogue_Clothes_Misc:                                                                                                                    
        #Misc
        
        "Maybe dry out your hair." if R_Hair == "wet":
                if ApprovalCheck("Rogue", 600):
                    ch_r "Ok."
                    $ R_Hair = "evo"
                else:
                    ch_r "I kinda prefer this look."
                
        "You should go for that wet look with your hair." if R_Hair != "wet":
                if ApprovalCheck("Rogue", 800):
                    ch_r "Hmm?"
                    $ R_Hair = "wet"
                    "She wanders off for a minute and comes back."
                    ch_r "Like this?"
                else:
                    ch_r "Not really into that."
                    
        "You know, I like some nice hair down there. Maybe grow it out." if not R_Pubes:
                if "pubes" in R_Todo:
                        call RogueFace("bemused", 1)
                        ch_r "Yeah, I know, [R_Petname]. It doesn't grow out overnight!"
                else:                
                        call RogueFace("bemused", 1)
                        $ Approval = ApprovalCheck("Rogue", 1150, TabM=0)
                        
                        if ApprovalCheck("Rogue", 850, "L", TabM=0) or (Approval and R_Love > R_Obed):               
                            ch_r "Well. . . if that's how you like it. . ."
                        elif ApprovalCheck("Rogue", 500, "O", TabM=0) or (Approval and R_Obed > R_Inbt):
                            ch_r "If that's what you want."
                        elif ApprovalCheck("Rogue", 500, "I", TabM=0) or Approval:
                            ch_r "Heh, I like a man knows what he wants, [R_Petname]."
                        else: 
                            call RogueFace("surprised")
                            $ R_Brows = "angry"
                            ch_r "Well I don't see how that's any of your business, [R_Petname]."
                            jump Rogue_Clothes
                        $ R_Todo.append("pubes")
                        $ R_PubeC = 6
        
        "I like it waxed clean down there." if R_Pubes == 1:
                call RogueFace("bemused", 1)
                if "shave" in R_Todo:
                        ch_r "I know, I'll get on that. Not right this second, obviously."
                else:
                        $ Approval = ApprovalCheck("Rogue", 1150, TabM=0)
                        if ApprovalCheck("Rogue", 850, "L", TabM=0) or (Approval and R_Love > R_Obed):             
                            ch_r "I can keep it tidy if you like. . ."
                        elif ApprovalCheck("Rogue", 500, "O", TabM=0) or (Approval and R_Obed > R_Inbt):
                            ch_r "I'll take care of it."
                        elif ApprovalCheck("Rogue", 500, "I", TabM=0) or Approval:
                            ch_r "You better earn it, [R_Petname]."
                        else: 
                            call RogueFace("surprised")
                            $ R_Brows = "angry"
                            ch_r "I don't see how that's any of your beeswax, [R_Petname]."
                            jump Rogue_Clothes
                        $ R_Todo.append("shave")        
        "Piercings. [[See what she looks like without them first] (locked)" if not R_SeenPussy and not R_SeenChest:
                        pass
            
        "You know, you'd look really nice with some ring body piercings." if R_Pierce != "ring" and (R_SeenPussy or R_SeenChest):             
                if "ring" in R_Todo:
                    ch_r "Yeah, I know, I'll get to it."
                else:                    
                    call RogueFace("bemused", 1)
                    $ Approval = ApprovalCheck("Rogue", 1350, TabM=0)
                    if ApprovalCheck("Rogue", 950, "L", TabM=0) or (Approval and R_Love > R_Obed):   
                        ch_r "You really like those? Well, I suppose. . ."
                    elif ApprovalCheck("Rogue", 600, "O", TabM=0) or (Approval and R_Obed > R_Inbt):
                        ch_r "I'll go get that taken care of."
                    elif ApprovalCheck("Rogue", 600, "I", TabM=0) or Approval:
                        ch_r "I've always kind of liked the look of those. . ."
                    else: 
                        call RogueFace("surprised")
                        $ R_Brows = "angry"
                        ch_r "I don't see how that's any of your beeswax, [R_Petname]."
                        jump Rogue_Clothes            
                    $ R_Todo.append("ring")
        
        "You know, you'd look really nice with some barbell body piercings." if R_Pierce != "barbell" and (R_SeenPussy or R_SeenChest):                
                if "barbell" in R_Todo:
                    ch_r "Yeah, I know, I'll get to it."
                else:                    
                    call RogueFace("bemused", 1)
                    $ Approval = ApprovalCheck("Rogue", 1350, TabM=0)
                    if ApprovalCheck("Rogue", 900, "L", TabM=0) or (Approval and R_Love > R_Obed):   
                        ch_r "You really like those? Well, I suppose. . ."
                    elif ApprovalCheck("Rogue", 600, "O", TabM=0) or (Approval and R_Obed > R_Inbt):
                        ch_r "I'll go get that taken care of."
                    elif ApprovalCheck("Rogue", 600, "I", TabM=0) or Approval:
                        ch_r "I've always kind of liked the look of those. . ."
                    else: 
                        call RogueFace("surprised")
                        $ R_Brows = "angry"
                        ch_r "I don't see how that's any of your beeswax, [R_Petname]."
                        jump Rogue_Clothes                
                    $ R_Todo.append("barbell")
                    $ R_Pierce = "barbell"
                        
        "You know, you'd look better without those piercings." if R_Pierce:
                call RogueFace("bemused", 1)
                $ Approval = ApprovalCheck("Rogue", 1350, TabM=0)
                if ApprovalCheck("Rogue", 950, "L", TabM=0) or (Approval and R_Love > R_Obed):   
                    ch_r "You really think so? I guess I could lose them. . ."
                elif ApprovalCheck("Rogue", 600, "O", TabM=0) or (Approval and R_Obed > R_Inbt):
                    ch_r "I'll take them out then."
                elif ApprovalCheck("Rogue", 600, "I", TabM=0) or Approval:
                    ch_r "I guess I prefered not having them in. . ."                
                else: 
                    call RogueFace("surprised")
                    $ R_Brows = "angry"
                    ch_r "I'll keep them, if you don't mind."
                    jump Rogue_Clothes            
                $ R_Pierce = 0 
                        
        "I like that spiked collar." if R_Neck != "spiked collar":
                        $ R_Neck = "spiked collar"
        "You could lose that spiked collar." if R_Neck == "spiked collar":
                        $ R_Neck = 0
                        
        "Throw the gloves on." if not R_Arms:
                        $ R_Arms = "gloved"
        "Take a little risk, no gloves." if R_Arms:
                        $ R_Arms = 0                        
                        
        "Never mind":
            pass      
    jump Rogue_Clothes
    #End of Rogue Misc Wardrobe
    
return

#End Rogue Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <



# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


label Rogue_Clothes_Schedule(Cnt = 0):
        #Sets clothing for different days, if Cnt is 3 it's all days, 2 is TuThu, 1 is only weekends
        #Schedule 0-6= mon-fri, Schedule 7 is dates, 9 is private
        
        if ApprovalCheck("Rogue", 1500, "LO"):
                ch_r "So, you'd like to choose what I wear for the week? Ok, shoot."
                $ Cnt = 3
        elif ApprovalCheck("Rogue", 1200, "LO"):
                ch_r "I guess I could set aside a few schooldays for you."
                $ Cnt = 2
        elif ApprovalCheck("Rogue", 1000, "LO"):
                ch_r "We can talk about what I wear outside of classes."
                $ Cnt = 1
        else:
                ch_r "You know, I don't really need fashion advice from you."
                return                        
        while True:    
            menu:
                    extend ""
                    "Every Day":
                        "This sets her outfit for every day of the week in one go."
                        "This overwrites the default schedule, and any scheduling you've already made."
                        "Any choices you make later will overwrite this choice."
                        menu:
                            "Pick an outfit to wear":                                
                                call Rogue_Clothes_ScheduleB
                                if Cnt > 1:
                                        $ R_Schedule[0] = _return
                                if Cnt > 2:
                                        $ R_Schedule[1] = _return
                                if Cnt > 1:
                                        $ R_Schedule[2] = _return
                                if Cnt > 2:
                                        $ R_Schedule[3] = _return
                                if Cnt > 1:
                                        $ R_Schedule[4] = _return
                                $ R_Schedule[5] = _return
                                $ R_Schedule[6] = _return
                            "Never mind.":
                                pass
                    "Weekdays":
                        menu:
                            "On Monday you should wear. . ." if Cnt > 1:
                                call Rogue_Clothes_ScheduleB
                                $ R_Schedule[0] = _return
                            "On Monday you should wear. . . (locked)" if Cnt <= 1:
                                pass
                                
                            "On Tuesday you should wear. . ." if Cnt > 2:
                                call Rogue_Clothes_ScheduleB
                                $ R_Schedule[1] = _return        
                            "On Tuesday you should wear. . . (locked)" if Cnt <= 2:
                                pass
                                
                            "On Wednesday you should wear. . ." if Cnt > 1:
                                call Rogue_Clothes_ScheduleB
                                $ R_Schedule[2] = _return
                            "On Wednesday you should wear. . . (locked)" if Cnt <= 1:
                                pass        
                                
                            "On Thursday you should wear. . ." if Cnt > 2:
                                call Rogue_Clothes_ScheduleB
                                $ R_Schedule[3] = _return
                            "On Thursday you should wear. . . (locked)" if Cnt <= 2:
                                pass
                                
                            "On Friday you should wear. . ." if Cnt > 1:
                                call Rogue_Clothes_ScheduleB
                                $ R_Schedule[4] = _return
                            "On Friday you should wear. . . (locked)" if Cnt <= 1:
                                pass
                            "Back":
                                pass 
                    "Other":
                        menu:
                            "On Saturday you should wear. . . (locked)" if Cnt < 1:
                                pass
                            "On Saturday you should wear. . ." if Cnt >= 1:
                                call Rogue_Clothes_ScheduleB
                                $ R_Schedule[5] = _return
                                
                            "On Sunday you should wear. . . (locked)" if Cnt < 1:
                                pass
                            "On Sunday you should wear. . ." if Cnt >= 1:
                                call Rogue_Clothes_ScheduleB
                                $ R_Schedule[6] = _return
                                
                            "In our rooms you should wear. . . (locked)" if Cnt < 1:
                                pass  
                            "In our rooms you should wear. . ." if Cnt >= 1:
                                call Rogue_Clothes_ScheduleB(99)
                                $ R_Schedule[9] = _return   
                                
                            "On dates you should wear. . . (locked)" if Cnt < 1:
                                pass
                            "On dates you should wear. . ." if Cnt >= 1:
                                call Rogue_Clothes_ScheduleB
                                $ R_Schedule[7] = _return  
                            "Back":
                                pass 
                                
                    "About Gym clothes":
                        menu:
                            ch_p "You asked me before about your gym clothes?"
                            "Don't ask before changing into gym clothes" if "no ask gym" not in R_Traits:
                                        ch_r "Sure."
                                        $ R_Traits.append("no ask gym")
                            "Ask me before changing into gym clothes" if "no ask gym" in R_Traits:
                                        ch_r "Sure."
                                        $ R_Traits.remove("no ask gym")    
                            "Never Mind":
                                pass                              
                                
                    "Private outfit" if R_Schedule[9]:
                                #if comfy is in L_Traits, she won't ask before changing
                                ch_p "You know that outfit you wear in private?"
                                menu:
                                    ch_r "Yeah?"
                                    "Just put them on without asking me about it." if "comfy" not in R_Traits:
                                        ch_r "Sure."
                                        $ R_Traits.append("comfy")
                                    "Ask before changing into that." if "comfy" in R_Traits:
                                        ch_r "Sure."
                                        $ R_Traits.remove("comfy")
                                    "Never Mind":
                                        pass       
                            
                    "Never mind [[Done]":
                        return        
        jump Rogue_Clothes_Schedule
        
label Rogue_Clothes_ScheduleB(Count = 0):
#This is called by Rogue_Clothes_Schedule when setting her outfit for a given day
#If Count by the end, yes, if not count, no. If count is 99 then it's an auto-yes

            menu:
                "Your green outfit.":
                    $ Count = 1
                "That pink outfit, with the jeans.":
                    $ Count = 2
                "That outfit we put together [[custom]":
                            menu:
                                ch_r "Which one again?"
                                "The first one. (locked)" if not R_Custom[0]:
                                    pass
                                "The first one." if R_Custom[0]:
                                    if R_Custom[0] == 2 or Count == 99:
                                        $ Count = 3
                                    else:
                                        ch_r "I told you I'm not wearing that outside, [R_Petname]."
                                        
                                "The second one. (locked)" if not R_Custom2[0]:
                                    pass
                                "The second one." if R_Custom2[0]:
                                    if R_Custom2[0] == 2 or Count == 99:
                                        $ Count = 5
                                    else:
                                        ch_r "I told you I'm not wearing that outside, [R_Petname]."
                                        
                                "The third one. (locked)" if not R_Custom3[0]:
                                    pass
                                "The third one." if R_Custom3[0]:
                                    if R_Custom3[0] == 2 or Count == 99:
                                        $ Count = 6
                                    else:
                                        ch_r "I told you I'm not wearing that outside, [R_Petname]."
                                        
                                "Never mind":
                                    pass
                "Your gym clothes.":
                    $ Count = 4
                "Your sleepwear.":
                    if Count != 99:
                        ch_e "I don't know about that, [R_Petname]."
                        $ Count = 0
                    else:
                        $ Count = 7
                "Whatever you like.":
                    pass
                    
            if Count:
                        ch_r "Ok, sure, I'll wear that."
            else:
                        ch_r "I'll just wear whatever then."
            return Count    
#End Rogue Clothes Scheduling Check

label R_AltClothes(Outfit=8):
        #1 = "evo_green", 2 = "evo_pink"
        #3 = "custom1", 5 = "custom2", 6 = "custom3", 7 = "sleep", 4 = "gym", 10 = "swimwear"
        #This selects her outfit when teaching if 8
        #This selects her private outfit if 9
        
        if R_Schedule[Outfit] == 1 or not R_Schedule[Outfit]:
                    $ R_Outfit = "evo_green"
        elif R_Schedule[Outfit] == 2:
                    $ R_Outfit = "evo_pink"
        elif R_Schedule[Outfit] == 3:
                    $ R_Outfit = "custom1"
        elif R_Schedule[Outfit] == 5:
                    $ R_Outfit = "custom2"
        elif R_Schedule[Outfit] == 6:
                    $ R_Outfit = "custom3"
        elif R_Schedule[Outfit] == 7:
                    $ R_Outfit = "sleep"
        elif R_Schedule[Outfit] == 4:
                    $ R_Outfit = "gym"
        elif R_Schedule[Outfit] == 10:
                    $ R_Outfit = "swimwear"
        return
  
label R_Private_Outfit:
    #sets Rogue's private outfit in private
    if R_Break[0] or "angry" in R_DailyActions:
            return
    if R_Outfit == "temporary":
            #if you manually set a different option, keep it
            return
    if "comfy" in R_RecentActions or "comfy" in R_Traits or R_Outfit == R_Schedule[9]:
            call R_AltClothes(9)
            call RogueOutfit(Changed=1)
    elif "no comfy" in R_RecentActions:
            pass        
    elif (2 * R_Inbt) >= (R_Love + R_Obed +100):
            # if her inhibition is much higher than her obedience to you. . .            
            ch_r "Be right there [R_Petname]. . ."
            ch_r "I'm slippin' inta somethin' more comfortable. . ."
            call R_AltClothes(9)
            call RogueOutfit(Changed=1)
            $ R_RecentActions.append("comfy")
    else:
            ch_r "Be right there [R_Petname]. . ."
            menu: 
                ch_r "Should I throw on somethin' more comfortable?"
                "Sure.":
                    ch_r "Love to. . ."
                    call R_AltClothes(9)
                    call RogueOutfit(Changed=1)
                    $ R_RecentActions.append("comfy")
                "No thanks.":
                    ch_r "Suit yourself."       
                    $ R_RecentActions.append("no comfy")             
    return

label Rogue_Custom_Out(Custom = 3, Shame = 0, Agree = 1):
            #If Custom1 = 3, if custom2 = 5, if custom3 = 6
            
            call RogueFace("sexy", 1)
            if "exhibitionist" in R_Traits:  
                        ch_r "Ooo, momma likes."  
                        if Custom == 5 and R_Custom2[0] == 2:
                            $ R_Outfit = "custom2"                    
                            $ R_Shame = R_OutfitShame[5]
                        elif Custom == 6 and R_Custom3[0] == 2:
                            $ R_Outfit = "custom3"                    
                            $ R_Shame = R_OutfitShame[6]
                        else: #if custom 1:
                            $ R_Outfit = "custom1"                    
                            $ R_Shame = R_OutfitShame[3]            
                        return    
            
            if Custom == 5 and R_Custom2[0] == 2:
                        $ R_Outfit = "custom2"   
            elif Custom == 6 and R_Custom3[0] == 2:
                        $ R_Outfit = "custom3"   
            elif R_Custom[0] == 2: #if custom 1:
                        $ R_Outfit = "custom1"   
            else: #no
                        $ Agree = 0
             
            if Agree: 
                        #she's decided to wear this out.
                        $ R_Shame = R_OutfitShame[Custom]          
                        if R_OutfitShame[Custom] >= 50:
                            ch_r "You realize I'm pretty much naked here, right?"
                        elif R_OutfitShame[Custom] >= 25:
                            ch_r "This is pretty shameless. . ."
                        elif R_OutfitShame[Custom] >= 15:
                            call RogueFace("bemused", 1)
                            ch_r "I don't know, I guess I could try it. . ."
                        else:
                            ch_r "Sure, [R_Petname], that one's nice."
            else:
                        #She's decided not to wear this out
                        if R_OutfitShame[Custom] >= 50:
                            call RogueFace("angry", 1)
                            ch_r "Come on, I'd be totally nude!"
                        elif R_OutfitShame[Custom] >= 25:
                            call RogueFace("angry", 1)
                            ch_r "You're lucky I show {i}you{/i} this."
                        else:
                            call RogueFace("bemused", 1)
                            ch_r "It's kind of daring for me, sorry."  
            return
# End Rogue Custom Out
                                
                                
label Rogue_OutfitShame(Custom = 3, Check = 0, Count = 0, Tempshame = 50, Agree = 1):
            #Custom determines which custom outfit is being checked against.    
            #If Custom1 = 3, if custom2 = 5, if custom3 = 6, if gym = 4, if sleepwear 7, if private = 9, if swimsuit = 10
            #if not a check, then it is only applied if it's in a taboo area
            # Tempshame is a throwaway value, 0-50, Agree is whether she will wear it out, 2 if yes, 1 if only around you.
            
            if not Check and not R_Taboo and Custom != 20:
                    #if this is not a custom check and you're in a safe space,
                    if R_Schedule[9]:
                            #if there is a "private outfit" set, ask to change.
                            call R_Private_Outfit
                    return
                            
            #If she's wearing a bra of some kind
            if Custom == 20 and R_Uptop: 
                $ Count = 0
            elif R_Chest == "tank":                                              
                $ Count = 20
            elif R_Chest == "buttoned tank":
                $ Count = 15
            elif R_Chest == "sports bra":
                $ Count = 15
            elif R_Chest == "bikini top":
                $ Count = 15
            elif R_Chest == "bra":
                $ Count = 10    
            else:     #R_Chest == 0 or lace bra:
                if R_Chest == "lace bra":
                    $ Count = 5
                if R_Pierce:
                    $ Count = -5
                else:
                    $ Count = 0
                    
            #If she's wearing an overshirt
            if Custom == 20 and R_Uptop: 
                $ Count = 0
            elif R_Over == "pink top":                                             
                $ Count += 15
            elif R_Over == "hoodie":      
                $ Count += 15
            elif R_Over == "mesh top":      
                $ Count += 5
            elif R_Over == "towel":      
                $ Count += 10
            #else: nothing    
            
            call RogueFace("sexy", 0)
            if Custom == 9 or Custom == 7:
                pass
            elif Count >= 20:
                $ Count = 20
                if Check:
                    ch_r "Oh, I think this top combination works."            
            elif not Check:
                pass
            elif Count >= 10 and (ApprovalCheck("Rogue", 1200, TabM=0) or ApprovalCheck("Rogue", 500, "I", TabM=0)):  
                ch_r "This top is pretty sexy. . ."        
            elif Count >= 10:
                ch_r "This top might be a bit daring to wear outside."
            elif Count >= 5 and (ApprovalCheck("Rogue", 2300, TabM=0) or ApprovalCheck("Rogue", 800, "I", TabM=0)):  
                ch_r "Not leaving much to the imagination. . ."        
            elif Count >= 5:        
                call RogueFace("startled", 1)
                ch_r "I really think this is a bit scandelous to wear out. . ."
            elif (ApprovalCheck("Rogue", 2700, TabM=0) or ApprovalCheck("Rogue", 950, "I", TabM=0)):  
                ch_r "Oooh, I'm getting turned on already. . ."        
            else:
                call RogueFace("bemused", 1)
                ch_r "This is just for in private, right. . ."
             
            $ Tempshame -= Count                  #Set Outfit shame for the upper half    
            $ Count = 0         
            
            if R_Legs and R_Panties: #If wearing both legs and panties   
                        $ Count = 30        
            else: #If she's missing something on her legs   
                        if R_Legs == "pants":                   #If wearing pants commando
                            $ Count = 25
                        elif R_Legs:                            #If wearing a skirt commando
                            $ Count = 20
                        elif R_Panties == "shorts":             #If wearing shorts
                            $ Count = 25  
                        elif R_Panties == "bikini bottoms":      #If wearing only bikini bottoms
                            $ Count = 15
                        elif R_Panties == "green panties":      #If wearing only green panties
                            $ Count = 10
                        elif R_Panties == "lace panties":       #If wearing only lace panties
                            $ Count = 5
                        elif R_Panties:                         #If wearing only any other panties
                            $ Count = 7
                        #else: 0
                        
                        if HoseNum("Rogue") >= 10:              #Factors in tights and hose
                            $ Count = 25 if Count < 25 else Count
                            
                        if R_Over == "towel" and Count:         #If wearing a Towel and anything else
                            $ Count = 25
                        elif R_Over == "towel":                 #If just wearing a Towel
                            $ Count = 15        
            
            if not Check:
                        #If this isn't a custom check, skip this dialog stuff
                        pass      
            elif Custom == 9 or Custom == 7:
                pass
            elif Count >= 20:
                        if R_Legs == "pants":
                            ch_r "Oh, I think these pants will work fine."
                        elif R_Legs:
                            ch_r "Oh, I think this skirt will work fine."
                        elif HoseNum("Rogue") >= 10:
                            ch_r "Oh, these [R_Hose] will work."
                        elif R_Panties == "shorts":
                            ch_r "Oh, I think these shorts will work fine."  
                        elif R_Over == "towel":
                            ch_r "The towel's an odd choice. . ."
                        else:
                            ch_r "Kinda breezy across my nethers, [R_Petname]. . ."
                        if not R_Panties and ApprovalCheck("Rogue", 500, "I", TabM=0):
                            ch_r "I kinda like going commando."           
                        elif not R_Panties:
                            ch_r "Don't know about going commando though."
                    
            elif Count >= 10 and (ApprovalCheck("Rogue", 2000, TabM=0) or ApprovalCheck("Rogue", 700, "I", TabM=0)):
                ch_r "These don't really leave much to the imagination. . ."        
            elif Count >= 10:
                call RogueFace("angry", 1)
                ch_r "I'm warning you, I'm not running around in my panties. . ."
                
            elif (ApprovalCheck("Rogue", 2500, TabM=0) or ApprovalCheck("Rogue", 800, "I", TabM=0)):  
                ch_r "Hmm, Breezy. . ."        
            else:
                ch_r "So long as we stay inside. . ."
                
            $ Tempshame -= Count                  #Set Outfit shame for the lower half
            
            if Check:
                    #if this is a custom outfit check                    
                    if Check == 2:
                        ch_p "So can I see it then?"
                    elif Custom == 4:
                        ch_p "So would you work out in that?"
                    elif Custom == 7:
                        ch_p "So would you sleep in that?"
                    else:
                        ch_p "So would you wear that outside?"  
                    call RogueFace("sexy", 0)
                    if PantsNum("Rogue") > 2:  
                        pass        #if she's wearing pants
                    elif PantiesNum("Rogue") > 2 and (R_SeenPanties or ApprovalCheck("Rogue", 900, TabM=0)):
                        pass        #no pants, but panties
                    elif R_SeenPussy or ApprovalCheck("Rogue", 1200, TabM=0):
                        pass        #no panties, but she's fine with that
                    else:
                        $ Agree = 0 #not fine with it
                        
                    if not Agree:
                        pass
                    elif OverNum("Rogue") > 2:    
                        pass        #if she's wearing a top
                    elif ChestNum("Rogue") > 2 and (R_SeenChest or ApprovalCheck("Rogue", 900, TabM=0)):
                        pass        #no top, but bra
                    elif R_SeenChest or ApprovalCheck("Rogue", 1200, TabM=0):
                        pass        #no bra, but she's fine with that
                    else:
                        $ Agree = 0 #not fine with it
                    
                    if Check == 2 and Agree:
                                #if checking to see if she'll drop the dressing screen. . .                                
                                $ R_Shame = Tempshame
                                call RogueFace("sly")
                                ch_r "This ain't a bad look, I guess. . ."
                                hide DressScreen
                                return 1   
                    if not Agree:
                                #she isn't even comfortable with you seeing it
                                call RogueFace("bemused", 2,Eyes="side")
                                ch_r "I don't really feel comfortable in this. . ."
                                        
                                menu:
                                    extend ""
                                    "Ok then, you can put your normal clothes back on.":
                                                call RogueOutfit(Changed=1)  
                                                hide DressScreen
                                    "Ok, we can keep tweaking it.":
                                                pass
                                call RogueFace("smile", 1)
                                ch_r "Thanks, [R_Petname]."
                                return
                    if R_Taboo >= 40: 
                        call RogueFace("confused",1)
                        $ R_Mouth = "smile"
                        ch_r "It's a little late to worry about that, right?" 
                    elif "exhibitionist" in R_Traits:        
                        ch_r "Hmm. . . yeah, I'd love to. . ."
                        call Statup("Rogue", "Lust", 80, 10)
                    elif Custom == 7: 
                        #Sleepwear
                        call RogueFace("bemused", 1)
                        if Tempshame >= 30:
                                ch_r "A bit scandelous, but yeah."
                        elif Tempshame >= 15:
                                ch_r "Yeah, you're worth it."
                        else:
                                ch_r "Sure, it's cute."                            
                    elif Tempshame <= 5:
                        call RogueFace("smile")
                        ch_r "Yeah, I think I like this style, I'd wear this."
                    elif Tempshame <= 15:
                        if ApprovalCheck("Rogue", 1700, TabM=0, C = 0) or ApprovalCheck("Rogue", 400, "I", TabM=0, C = 0):        
                            ch_r "It's pretty skimpy, but I can make it work."
                        else:
                            call RogueFace("bemused", 1)
                            ch_r "I think this looks is a bit daring to wear."
                            $ Agree = 0
                    elif Custom == 10 and Tempshame <= 20:  
                        #if it's a swimsuit. . .
                        call RogueFace("bemused", 1)
                        ch_r "Sure, I can swim in this. . ."
                    elif Tempshame <= 25:
                        if ApprovalCheck("Rogue", 2300, TabM=0, C = 0) or ApprovalCheck("Rogue", 700, "I", TabM=0, C = 0):
                            ch_r "Kinky, but I can rock this."
                        else:
                            call RogueFace("angry", 1)
                            ch_r "I'm definitely not going out in this."
                            $ Agree = 0
                    elif ApprovalCheck("Rogue", 2500, TabM=0, C = 0) or ApprovalCheck("Rogue", 800, "I", TabM=0, C = 0):
                            call RogueFace("bemused", 1)
                            ch_r "I can't believe it. . . but yeah."
                    else:
                            call RogueFace("angry", 1)
                            ch_r "You have got to be kidding."
                            $ Agree = 0
                    
                    $ R_OutfitShame[Custom] = Tempshame 
                    if Custom == 5:
                        $ R_Custom2[1] = R_Arms  
                        $ R_Custom2[2] = R_Legs 
                        $ R_Custom2[3] = R_Over
                        $ R_Custom2[4] = R_Neck
                        $ R_Custom2[5] = R_Chest 
                        $ R_Custom2[6] = R_Panties
                        $ R_Custom2[8] = R_Hair
                        $ R_Custom2[9] = R_Hose
                        $ R_Custom2[0] = 2 if Agree else 1   
                        call Clothing_Schedule_Check("Rogue",5,1) #checks to make sure it's still SFW     
                    elif Custom == 6:
                        $ R_Custom3[1] = R_Arms  
                        $ R_Custom3[2] = R_Legs 
                        $ R_Custom3[3] = R_Over
                        $ R_Custom3[4] = R_Neck
                        $ R_Custom3[5] = R_Chest 
                        $ R_Custom3[6] = R_Panties
                        $ R_Custom3[8] = R_Hair
                        $ R_Custom3[9] = R_Hose
                        $ R_Custom3[0] = 2 if Agree else 1
                        call Clothing_Schedule_Check("Rogue",6,1)   
                    elif Custom == 4 and Agree:
                        $ R_Gym[1] = R_Arms  
                        $ R_Gym[2] = R_Legs 
                        $ R_Gym[3] = R_Over
                        $ R_Gym[4] = R_Neck
                        $ R_Gym[5] = R_Chest 
                        $ R_Gym[6] = R_Panties
                        $ R_Gym[8] = R_Hair
                        $ R_Gym[9] = R_Hose
                        $ R_Gym[0] = 2     
                        call Clothing_Schedule_Check("Rogue",4,1)   
                    elif Custom == 7:
                        $ R_Sleepwear[1] = R_Arms  
                        $ R_Sleepwear[2] = R_Legs 
                        $ R_Sleepwear[3] = R_Over
                        $ R_Sleepwear[4] = R_Neck 
                        $ R_Sleepwear[5] = R_Chest 
                        $ R_Sleepwear[6] = R_Panties
                        $ R_Sleepwear[8] = R_Hair
                        $ R_Sleepwear[9] = R_Hose
                        $ R_Sleepwear[0] = 2 if Agree else 1    
                    elif Custom == 10:            
                        $ R_Swim[1] = R_Arms  
                        $ R_Swim[2] = R_Legs 
                        $ R_Swim[3] = R_Over
                        $ R_Swim[4] = R_Neck 
                        $ R_Swim[5] = R_Chest 
                        $ R_Swim[6] = R_Panties
                        $ R_Swim[8] = R_Hair
                        $ R_Swim[9] = R_Hose
                        $ R_Swim[0] = 2 if Agree else 1
                    else: #Typically Custom == 3
                        $ R_Custom[1] = R_Arms  
                        $ R_Custom[2] = R_Legs 
                        $ R_Custom[3] = R_Over
                        $ R_Custom[4] = R_Neck
                        $ R_Custom[5] = R_Chest 
                        $ R_Custom[6] = R_Panties
                        $ R_Custom[8] = R_Hair
                        $ R_Custom[9] = R_Hose
                        $ R_Custom[0] = 2 if Agree else 1
                        call Clothing_Schedule_Check("Rogue",3,1)   
            elif R_Taboo <= 20:
                # halves shame level if she's comfortable
                $ Tempshame /= 2
                
            $ R_Shame = Tempshame
                 
            if Custom == 20:
                # This returns the scene if it's a check Shame adjustment
                return
                
            if Check:
                    pass
            elif "exhibitionist" in R_Traits and Tempshame <= 20: 
                    #If she's an exhibitionist
                    pass
            elif Tempshame <= 5:
                    #If the outfit is very tame
                    pass
            elif R_Over == "towel" and R_Loc == "bg showerroom": 
                    #If she's in a towel but it's appropriate
                    pass
            elif Tempshame <= 15 and (ApprovalCheck("Rogue", 1500) or ApprovalCheck("Rogue", 500, "I")):
                    #If the outfit is hot but she's ok     
                    pass
            elif Tempshame <= 20 and (R_Loc == "bg dangerroom" or R_Loc == "bg pool"): 
                    #If the outfit is light but she's in the gym
                    pass
            elif Tempshame <= 20 and (ApprovalCheck("Rogue", 1800) or ApprovalCheck("Rogue", 650, "I")):
                    #If the outfit is sexy but she's cool with that
                    pass
            elif Tempshame <= 25 and (ApprovalCheck("Rogue", 2000) or ApprovalCheck("Rogue", 700, "I")):
                    #If the outfit is sexy but she's cool with that
                    pass
            elif (ApprovalCheck("Rogue", 2500) or ApprovalCheck("Rogue", 800, "I")):
                    #If the outfit is very scandelous but she's ok with that      
                    pass
            elif not R_Taboo:
                    pass
            else:
                    if R_Loc == bg_current:
                            ch_r "I'll be right back, I've got to change out of this."
                    if R_Loc == "bg dangerroom":
                            $ R_Outfit =  "gym"
                    elif R_Loc == "bg pool" and R_Swim[0]:
                            $ R_Outfit =  "swimwear"                        
                    else:
                            $ R_Outfit = renpy.random.choice(["evo_green", "evo_pink"])
                    $ R_Water = 0
                    call RogueOutfit(Changed=1) 
                    ch_r "That wasn't really \"outdoor ready\"."
                    
            return   
#End Rogue Custom clothes check.



# start Rogue not a virgin
label Rogue_Not_Virgin:
    menu:
        "I noticed that when we had sex, you didn't seem to be a virgin."
        "Wasn't I your first time?":
            call RogueFace("bemused", 1)
            call Statup("Rogue", "Love", 60, 5)
            call Statup("Rogue", "Obed", 20, 15)
            ch_r "Oh, no! You definitely were, it's just. . . you know,"
            ch_r "I lead a pretty active lifestyle, so I lost that physical barrier years ago."
        "So you get around?":
            call RogueFace("sexy", 1)
            $ R_Brows = "angry"
            call Statup("Rogue", "Obed", 30, 15)
            call Statup("Rogue", "Obed", 60, 5)
            call Statup("Rogue", "Inbt", 30, 15)
            call Statup("Rogue", "Inbt", 60, 5)
            ch_r "Jerk, not like that. I tore it years ago in combat training."
        "Are you a slut?":
            call RogueFace("angry", 1)          
            call Statup("Rogue", "Love", 30, -20, 1)
            call Statup("Rogue", "Love", 60, -40, 1)
            call Statup("Rogue", "Obed", 30, 30)
            call Statup("Rogue", "Obed", 60, 20)
            ch_r "If you'd like to find that out, you might want to rethink how you talk to me, [R_Petname]."
    $ R_Chat[0] = 1
    return

# end rogue not a virgin //////////////////////////////////////////////////////////

# start rogue hungry //////////////////////////////////////////////////////////
label Rogue_Hungry:
    if R_Chat[3]:
        ch_r "You know, I've really come to enjoy the taste of your. . . cum. I think I'd like some more of that."
    elif R_Chat[2]:
        ch_r "You know, I've really come to enjoy the taste of your, serum. It's like my favorite drink!"
    else:
        ch_r "You know, I've really come to enjoy the taste of your. . . cum. I think I'd like some more of that."
    $ R_Traits.append("hungry")
return


# end rogue hungry //////////////////////////////////////////////////////////


label Rogue_About(Girl="Kitty"):
    ch_r "What do I think about her? Well. . ."
    if Girl == "Kitty":
            if "poly Kitty" in R_Traits:  
                ch_r "I think you know the answer to that one. . ."    
            elif R_LikeKitty >= 900:
                ch_r "I think she's really . . . hot?"
            elif R_LikeKitty >= 800:
                ch_r "I feel really close to her, best friends, maybe more."    
            elif R_LikeKitty >= 700:
                ch_r "She's one of my best friends."
            elif R_LikeKitty >= 600:
                ch_r "We're good friends."
            elif R_LikeKitty >= 500:
                ch_r "I don't know, she's ok."
            elif R_LikeKitty >= 400:
                ch_r "We're. . . kind of off right now."
            elif R_LikeKitty >= 300:
                ch_r "I don't want to talk about it." 
            else:
                ch_r "That ho-bag skank?"
    elif Girl == "Emma":
            if "poly Emma" in R_Traits:  
                ch_r "Well, I sure don't kick her out of bed. . ."    
            elif R_LikeEmma >= 900:
                ch_r "I'm kinda hot for teacher."
            elif R_LikeEmma >= 800:
                ch_r "She's pretty amaz'in, right? Sometimes I wonder. . ."    
            elif R_LikeEmma >= 700:
                ch_r "We hang out sometimes after class, she's fun to talk to."
            elif R_LikeEmma >= 600:
                ch_r "She's a really great teach, I love her lectures."
            elif R_LikeEmma >= 500:
                ch_r "I don't know, she's ok."
            elif R_LikeEmma >= 400:
                ch_r "I don't really like the way she looks at you in class."
            elif R_LikeEmma >= 300:
                ch_r "I hate her  class." 
            else:
                ch_r "Ugh, that WITCH!"    
    elif Girl == "Laura":
            if "poly Laura" in R_Traits:  
                ch_r "We hook up from time to time. . ."    
            elif R_LikeLaura >= 900:
                ch_r "She's got an animal magnetism to her. . ."
            elif R_LikeLaura >= 800:
                ch_r "We really seem to get along. . ."    
            elif R_LikeLaura >= 700:
                ch_r "She's a good friend."
            elif R_LikeLaura >= 600:
                ch_r "She's a good teammate."
            elif R_LikeLaura >= 500:
                ch_r "I don't know, she's ok in a fight."
            elif R_LikeLaura >= 400:
                ch_r "We're. . . not in a good place."
            elif R_LikeLaura >= 300:
                ch_r "I don't want to talk about it." 
            else:
                ch_r "That ho-bag skank?"          
    return