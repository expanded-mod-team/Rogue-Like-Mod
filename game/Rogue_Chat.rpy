# star Rogue chat interface
#label Rogue_Chat_Set(Preset=0):    
#    if RogueX not in Digits and RogueX.Loc != bg_current and RogueX not in Nearby:
#            "You don't have her number."
#            return
            
#    if Preset:   
#            ch_p "Hey, [RogueX.Name]. . ."
#            call Shift_Focus(RogueX)
#            if RogueX.Loc != bg_current:
#                        show Cellphone at SpriteLoc(StageLeft)
#            else:
#                        hide Cellphone
#            if Preset == "chat":
#                    $ renpy.pop_call() #removes the call to chat subroutine
#                    $ renpy.pop_call() #This removes the callback to the previous chat session
#            elif Preset == "settings":
#                    $ renpy.pop_call() #This removes the callback to the previous chat session
#                    $ renpy.pop_call() #this removes the callback to the previous settings menu
#                    call Rogue_Settings   
#            elif Preset == "wardrobe":
#                    $ renpy.pop_call() #This removes the callback to the previous chat session
#                    $ renpy.pop_call() #this removes the callback to the previous settings menu
#                    $ renpy.pop_call() #this removes the callback to the previous settings menu testing. . .
#                    ch_p "I wanted to talk about your outfit. . ."
#                    call Taboo_Level
#                    if RogueX.Taboo:
#                            if "exhibitionist" in RogueX.Traits:
#                                ch_r "Oooh, naughty. . ."  
#                            elif ApprovalCheck(RogueX, 900, TabM=4) or ApprovalCheck(RogueX, 400, "I", TabM=3): 
#                                ch_r "Well, I mean, it's pretty public here, but I guess I could. . ."
#                            else:
#                                ch_r "This is a pretty public place for that, don't you think?"
#                                ch_r "We can talk about that back in our rooms."
#                                jump Rogue_Chat
#                            call Rogue_Clothes
#                    elif ApprovalCheck(RogueX, 600, "L") or ApprovalCheck(RogueX, 300, "O"):
#                        ch_r "Ok, what did you want?"
#                        call Rogue_Clothes
#                    else:
#                        ch_r "Well I'm not really interested in your fashion opinions." 
#            #end preset menu
            
#label Rogue_Chat:
#    $ RogueX.FaceChange()      
#    call Shift_Focus(RogueX)
#    if RogueX.Loc != bg_current:
#                show Cellphone at SpriteLoc(StageLeft)
#    else:
#                hide Cellphone
    
#    if "caught" in RogueX.RecentActions:
#                ch_r "We should probably keep our distance for now."
#                return
#    if "angry" in RogueX.RecentActions:
#                ch_r "I really don't want to talk to you right now."
#                return
#    if "les" in RogueX.RecentActions:
#                #if she's with a girl. . .
#                ch_r "Ooof. . . gimme a minute. . ."
#                "You hear some shifting around. . ."
#                ch_r "Ok, just um, never mind. . ."
#                "You hear some muffled giggles in the background."
#    menu:
#        ch_r "So what did you want to talk about, [RogueX.Petname]?"
#        "Come on over." if RogueX.Loc != bg_current:
#                    if RogueX in Nearby and bg_current != "bg showerrroom":
#                        call Swap_Nearby(RogueX)
#                    elif Room_Full():
#                        "It's already pretty crowded here."
#                        call Dismissed
#                    else:
#                        call Rogue_Summon  
#        "Ask [RogueX.Name] to leave" if RogueX.Loc == bg_current:
#                    call Rogue_Dismissed   
#                    return
#        "Romance her":      
#                menu:
#                    "Flirt with her (locked)" if RogueX.Chat[5]:  
#                                pass
#                    "Flirt with her" if not RogueX.Chat[5]:
#                                call Flirt(RogueX)    
                        
#                    "Sex Menu (locked)" if RogueX.Loc != bg_current:
#                                pass
#                    "Sex Menu" if RogueX.Loc == bg_current:
#                                if RogueX.Love >= RogueX.Obed:
#                                    ch_p "Did you want to fool around?"
#                                else:
#                                    ch_p "I'd like to get naughty."
#                                if "angry" in RogueX.RecentActions:  
#                                    ch_r "I don't want to deal with you right now."
#                                elif ApprovalCheck(RogueX, 600, "LI"):
#                                    $ RogueX.FaceChange("sexy")
#                                    ch_r "Heh, all right, [RogueX.Petname]."
#                                    call Rogue_SexMenu
#                                    return
#                                elif ApprovalCheck(RogueX, 400, "OI"):
#                                    ch_r "If that's what you want, [RogueX.Petname]."
#                                    call Rogue_SexMenu
#                                    return
#                                else:
#                                    ch_r "I'm not really interested, [RogueX.Petname]." 
                               
#                    "Dirty Talk (locked)" if RogueX.SEXP < 10:
#                                    pass
#                    "Dirty Talk" if RogueX.SEXP >= 10:
#                                    ch_p "About when we get together. . ."
#                                    call Rogue_SexChat
                                    
#                    "Date":
#                                    ch_p "Do you want to go on a date tonight?"
#                                    call Date_Ask(RogueX)
                                    
#                    "Gifts (locked)" if RogueX.Loc != bg_current:
#                                    pass
#                    "Gifts" if RogueX.Loc == bg_current:
#                                    ch_p "I'd like to give you something."
#                                    call Gifts(RogueX)
#                    "Back":
#                                    pass        
                                          
#        "Talk with her": 
#                menu:
#                    "I just wanted to talk. . .":
#                                call Rogue_Chitchat   
#                    "Relationship status":
#                                ch_p "Could we talk about us?"
#                                if RogueX.Loc == bg_current:
#                                    call Rogue_Relationship
#                                else:
#                                    ch_r "That sounds like it might be a little heavy to do over the phone."
#                                    ch_r "Maybe later?"
                          
#                    "Other girls":
#                                menu:
#                                    "How do you feel about [KittyX.Name]?" if "met" in KittyX.History:
#                                            call Rogue_About(KittyX)
#                                    "How do you feel about [EmmaX.Name]?" if "met" in EmmaX.History:
#                                            call Rogue_About(EmmaX)
#                                    "How do you feel about [LauraX.Name]?" if "met" in LauraX.History:
#                                            call Rogue_About(LauraX)
#                                    "About hooking up with other girls. . .":
#                                            call Rogue_Monogamy
#                                    "Never mind.":
#                                            pass
                                            
#                    "Could I get your number?" if RogueX not in Digits:
#                                if ApprovalCheck(RogueX, 400, "L") or ApprovalCheck(RogueX, 200, "I"):
#                                    ch_r "Sure, I suppose."
#                                    $ Digits.append(RogueX) 
#                                elif ApprovalCheck(RogueX, 200, "O"):
#                                    ch_r "If you want it, I guess."             
#                                    $ Digits.append(RogueX)
#                                else:
#                                    ch_r "I don't really want you calling me."      
#                    "Back":
#                                pass
                    
#        "Change [RogueX.Name]":
#                    call Rogue_Settings   
         
#        "Add her to party" if RogueX not in Party and RogueX.Loc == bg_current:
#                    ch_p "Could you follow me for a bit?"
#                    if ApprovalCheck(RogueX, 550):
#                            $ Party.append(RogueX)
#                            ch_r "Ok, Where did you want to go?"
#                            return
#                    elif not ApprovalCheck(RogueX, 300):
#                            ch_r "Um, no thanks."
#                    else:
#                            ch_r "I'm fine here, thanks."
#        "Disband party" if RogueX in Party: 
#                    ch_p "Ok, you can leave if you prefer."
#                    $ Party.remove(RogueX)       
#                    call Schedule(RogueX,0)         
#                    if "leaving" in RogueX.RecentActions:
#                        call DrainWord(RogueX,"leaving")
#                    if RogueX.Loc == bg_current:
#                        ch_r "Ok, I'll probably stick around for a bit anyway."
#                    else:
#                        ch_r "Ok, see you later then."
#                        call Set_The_Scene   
#                    return
                
#        "Switch to. . .":
#                menu:
#                    "[KittyX.Name]":
#                        call Chat(KittyX)          
#                    "[EmmaX.Name]":
#                        call Chat(EmmaX)       
#                    "[LauraX.Name]":
#                        call Chat(LauraX)
#                    "Never mind":
#                        pass
                        
#        "Never mind.":
#                    ch_r "Ok, later then."
#                    return
#    jump Rogue_Chat

## Rogue Control interface //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //
#label Rogue_Controls:
#    menu:
#        "I'd like you to call me something else":
#                call Rogue_Names            
#                return
#        "I'd like you to come over for some action." if RogueX.Loc != bg_current:
#                ch_r "Ok, I'll be right over."
#                $ RogueX.Loc = bg_current 
#                call Set_The_Scene
#                call Rogue_SexMenu
#                return
#        "I'd like to get busy." if RogueX.Loc == bg_current:
#                ch_r "Hmmm, what did you have in mind?"
#                call Rogue_SexMenu
#                return
#        "I want you to stop taking your own initiative." if "sub" not in RogueX.Traits:
#                $ RogueX.Traits.append("sub")
#                ch_r "Very well, I will only do as ordered from now on."           
#        "You can take your own initiative if you like." if "sub" in RogueX.Traits:
#                $ RogueX.Traits.remove("sub")
#                ch_r "Great, I'll do that."   
#        "Exit.":
#                return
#    jump Rogue_Controls
#return


##Rogue Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  

label Rogue_Relationship:
    while True:
        menu:
            ch_r "What did you want to ask me about?"            
            "Do you want to be my girlfriend?" if "dating" not in RogueX.Traits and "ex" not in RogueX.Traits:
                    $ RogueX.DailyActions.append("relationship")
                    if "asked boyfriend" in RogueX.DailyActions and "angry" in RogueX.DailyActions:
                            $ RogueX.FaceChange("angry", 1)
                            ch_r "Seriously, stop bugging me."
                            return
                    elif "asked boyfriend" in RogueX.DailyActions:
                            $ RogueX.FaceChange("angry", 1)
                            ch_r "You already asked about that, the answer's still no."
                            return
                    elif RogueX.Break[0]:                    
                            $ RogueX.FaceChange("angry", 1)                    
                            ch_r "I already told you, not while you're with her."
                            if Player.Harem:   
                                    $ RogueX.DailyActions.append("asked boyfriend")                     
                                    return
                            else:
                                    ch_p "I'm not anymore."
                         
                    $ RogueX.DailyActions.append("asked boyfriend")
                    
                    if Player.Harem and "RogueYes" not in Player.Traits: 
                        if len(Player.Harem) >= 2:
                            ch_r "That wouldn't be fair to the others, [RogueX.Petname]."
                        else:
                            ch_r "That wouldn't be fair to [Player.Harem[0].Name], [RogueX.Petname]."
                        return                    
                    
                    if RogueX.Event[5]:
                            $ RogueX.FaceChange("bemused", 1)
                            ch_r "I mean, I asked you about this before. . ."
                    else:
                            $ RogueX.FaceChange("surprised", 2)
                            ch_r "Wow, this is unexpected, [RogueX.Petname]. . ." 
                            $ RogueX.FaceChange("smile", 1)
                    
                    call Rogue_OtherWoman
                    
                    if RogueX.Love >= 800:
                            $ RogueX.FaceChange("surprised", 1)
                            $ RogueX.Mouth = "grimace"
                            $ RogueX.Statup("Love", 200, 40)
                            ch_r "I'd love to!"
                            if "boyfriend" not in RogueX.Petnames:
                                        $ RogueX.Petnames.append("boyfriend")                
                            $ RogueX.Traits.append("dating")
                            if "RogueYes" in Player.Traits:       
                                        $ Player.Traits.remove("RogueYes")
                                        $ Player.Harem.append(RogueX)
                                        call Harem_Initiation
                            "[RogueX.Name] leaps in and kisses you deeply."
                            $ RogueX.FaceChange("kiss", 1) 
                            $ RogueX.Kissed += 1
                    elif RogueX.Obed >= 500:
                            $ RogueX.FaceChange("perplexed")
                            ch_r "I'm not sure I'd call what we have \"dating.\""
                    elif RogueX.Inbt >= 500:
                            $ RogueX.FaceChange("smile")                
                            ch_r "I don't really want to be tied down like that."
                    else:
                            $ RogueX.FaceChange("perplexed", 1)
                            ch_r "I don't really feel that way about you right now, [RogueX.Petname]."
                            
            "Do you want to get back together?" if "ex" in RogueX.Traits:
                    $ RogueX.DailyActions.append("relationship")
                    if "asked boyfriend" in RogueX.DailyActions and "angry" in RogueX.DailyActions:
                            $ RogueX.FaceChange("angry", 1)
                            ch_r "Seriously, stop bugging me."
                            return
                    elif "asked boyfriend" in RogueX.DailyActions:
                            $ RogueX.FaceChange("angry", 1)
                            ch_r "You already asked about that, the answer's still no."
                            return
                                        
                    $ RogueX.DailyActions.append("asked boyfriend")
                    
                    if Player.Harem and "RogueYes" not in Player.Traits: 
                            if len(Player.Harem) >= 2:
                                ch_r "That wouldn't be fair to the others, [RogueX.Petname]."
                            else:
                                ch_r "That wouldn't be fair to [Player.Harem[0].Name], [RogueX.Petname]."
                            return
                    
                    $ Cnt = 0
                    call Rogue_OtherWoman
                                            
                    if RogueX.Love >= 800:
                            $ RogueX.FaceChange("surprised", 1)
                            $ RogueX.Mouth = "grimace"
                            $ RogueX.Statup("Love", 90, 5)
                            ch_r "If you're in, I'm in!"
                            if "boyfriend" not in RogueX.Petnames:
                                        $ RogueX.Petnames.append("boyfriend")                
                            $ RogueX.Traits.append("dating")          
                            $ RogueX.Traits.remove("ex")
                            if "RogueYes" in Player.Traits:       
                                        $ Player.Traits.remove("RogueYes")
                                        $ Player.Harem.append(RogueX)
                                        call Harem_Initiation
                            "[RogueX.Name] leaps in and kisses you deeply."
                            $ RogueX.FaceChange("kiss", 1) 
                            $ RogueX.Kissed += 1
                    elif RogueX.Love >= 600 and ApprovalCheck(RogueX, 1500):
                            $ RogueX.FaceChange("smile", 1)
                            $ RogueX.Mouth = "grimace"
                            $ RogueX.Statup("Love", 90, 5)
                            ch_r "We can give this another try."
                            if "boyfriend" not in RogueX.Petnames:
                                        $ RogueX.Petnames.append("boyfriend")                
                            $ RogueX.Traits.append("dating")             
                            $ RogueX.Traits.remove("ex")
                            if "RogueYes" in Player.Traits:       
                                        $ Player.Traits.remove("RogueYes")
                                        $ Player.Harem.append(RogueX)
                                        call Harem_Initiation
                            "[RogueX.Name] gives you a quick kiss."
                            $ RogueX.FaceChange("kiss", 1) 
                            $ RogueX.Kissed += 1
                    elif RogueX.Obed >= 500:
                            $ RogueX.FaceChange("sad")
                            ch_r "Whatever we had, whatever we have right now, that's not it."
                    elif RogueX.Inbt >= 500:
                            $ RogueX.FaceChange("perplexed")                
                            ch_r "We tried that, it didn't work out."
                    else:
                            $ RogueX.FaceChange("perplexed", 1)
                            ch_r "I'm not ready for more heartbreak, [RogueX.Petname]."
                    
                    # End Back Together
                        
            "I wanted to ask about [[another girl]" if RogueX in Player.Harem:
                    menu:
                        "Have you reconsidered letting me date. . ."
                        "[KittyX.Name]" if KittyX not in Player.Harem and "met" in KittyX.History:
                                call Poly_Start(KittyX,1)
                        "[EmmaX.Name]" if EmmaX not in Player.Harem and "met" in EmmaX.History:
                                call Poly_Start(EmmaX,1)
                        "[LauraX.Name]" if LauraX not in Player.Harem and "met" in LauraX.History:
                                call Poly_Start(LauraX,1)
                        "Never mind":
                                pass
                                
            "I think we should break up." if "dating" in RogueX.Traits or RogueX in Player.Harem:
                        if "breakup talk" in RogueX.RecentActions:
                                ch_r "We were {i}just{/i} over this, not even funny."
                        elif "breakup talk" in RogueX.DailyActions:
                                ch_r "Tired of me again that quick?" 
                                ch_r "We're not having this talk today, [RogueX.Petname]."
                        else:
                                call Breakup(RogueX)                
                            
            "About that talk we had before. . .":
                menu:
                    "You weren't a virgin?" if RogueX.Sex and not RogueX.Chat[0]:
                        call Rogue_Not_Virgin   
                    
                    "You said you wanted me to be your Master?" if RogueX.Event[8] and "master" not in RogueX.Petnames:
                        menu:
                            ch_r "Yes?"
                            "I'm ok with that now.":
                                        if ApprovalCheck(RogueX, 800, "O"):     
                                            $ RogueX.FaceChange("sexy", 1)
                                            ch_r "I hope to serve well, Master."
                                            $ RogueX.Statup("Obed", 200, 100) 
                                            $ RogueX.Petnames.append("master")
                                            $ RogueX.Event[8] = 2
                                        else:
                                            ch_r "Well, I'm not really interested in that sort of thing anymore."
                                            ch_r "I mean, maybe later." 
                            "Never mind.":
                                        $ RogueX.FaceChange("sad")
                                        ch_r "Oh."
                                        $ RogueX.Statup("Obed", 200, -5)
                                        $ RogueX.Statup("Love", 90, -5)  
                    "Never Mind":
                        pass                            
            "Never Mind":
                return
        return


label Rogue_OtherWoman(Cnt = 0):
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    if not Player.Harem:
            return            
    $ Cnt = int((RogueX.GirlLikeCheck(Player.Harem[0]) - 500)/2)  
        
    $ RogueX.FaceChange("perplexed")
    if len(Player.Harem) >= 2:
        ch_r "But you're with [Player.Harem[0].Name] right now, and a whole mess'a other girls!"
    else:    
        ch_r "But you're with [Player.Harem[0].Name]!"
    menu: 
        extend ""
        "She said I can be with you too." if "RogueYes" in Player.Traits:
                if ApprovalCheck(RogueX, 1800, Bonus = Cnt):
                    $ RogueX.FaceChange("smile", 1)
                    if RogueX.Love >= RogueX.Obed:
                            ch_r "I s'pose I can learn ta share."
                    elif RogueX.Obed >= RogueX.Inbt:
                            ch_r "Well I won't be the one to get in the way a this."
                    else:
                            ch_r "Ok, sure."
                else:
                    $ RogueX.FaceChange("angry", 1)
                    ch_r "Well that harlot!"  
                    $ renpy.pop_call()                                          
                    #This causes it to jump past the previous menu on the return
        
        "I could ask if she'd be ok with me dating you both." if "RogueYes" not in Player.Traits:
                if ApprovalCheck(RogueX, 1800, Bonus = Cnt):
                        $ RogueX.FaceChange("smile", 1)
                        if RogueX.Love >= RogueX.Obed:
                            ch_r "I s'pose I can learn ta share."
                        elif RogueX.Obed >= RogueX.Inbt:
                            ch_r "Well I won't be the one to get in the way a this."
                        else:
                            ch_r "Ok, sure."               
                        ch_r "You go ask her if she's inta that, then get back to me tomorrow."
                else:
                        $ RogueX.FaceChange("angry", 1)
                        ch_r "Well that harlot!"     
                $ renpy.pop_call()
        
        "What she doesn't know won't hurt her.":
                if not ApprovalCheck(RogueX, 1800, Bonus = -Cnt): #checks if She likes you more than the other girl
                        $ RogueX.FaceChange("angry", 1)
                        if not ApprovalCheck(RogueX, 1800):
                                ch_r "Well now I don't wantcha."
                        else:
                                ch_r "I ain't in a sharin mood."                    
                        $ renpy.pop_call() 
                else:
                        $ RogueX.FaceChange("smile", 1)
                        if RogueX.Love >= RogueX.Obed:
                                ch_r "I s'pose somethin could be arranged. . ."
                        elif RogueX.Obed >= RogueX.Inbt:
                                ch_r "If you insist."
                        else:
                                ch_r "Don't see why not."
                        $ RogueX.AddWord(1,0,0,"downlow")
                
        "I can break it off with her.":
                    $ RogueX.FaceChange("sad")
                    ch_r "Well then talk to me after you have."                                   
                    $ renpy.pop_call()
            
        "You're right, I was dumb to ask.":
                    $ RogueX.FaceChange("sad")
                    ch_r "Yeah. . ."                    
                    $ renpy.pop_call()                   
                
    return
    
    
label Rogue_About(Check=0):
    if Check not in TotalGirls:
            ch_r "Who?"
            return
    ch_r "What do I think about her? Well. . ."
    if Check == KittyX:
            if "poly Kitty" in RogueX.Traits:  
                ch_r "I think you know the answer to that one. . ."    
            elif RogueX.LikeKitty >= 900:
                ch_r "I think she's really . . . hot?"
            elif RogueX.LikeKitty >= 800:
                ch_r "I feel really close to her, best friends, maybe more."    
            elif RogueX.LikeKitty >= 700:
                ch_r "She's one of my best friends."
            elif RogueX.LikeKitty >= 600:
                ch_r "We're good friends."
            elif RogueX.LikeKitty >= 500:
                ch_r "I don't know, she's ok."
            elif RogueX.LikeKitty >= 400:
                ch_r "We're. . . kind of off right now."
            elif RogueX.LikeKitty >= 300:
                ch_r "I don't want to talk about it." 
            else:
                ch_r "That ho-bag skank?"
    elif Check == EmmaX:
            if "poly Emma" in RogueX.Traits:  
                ch_r "Well, I sure don't kick her out of bed. . ."    
            elif RogueX.LikeEmma >= 900:
                ch_r "I'm kinda hot for teacher."
            elif RogueX.LikeEmma >= 800:
                ch_r "She's pretty amaz'in, right? Sometimes I wonder. . ."    
            elif RogueX.LikeEmma >= 700:
                ch_r "We hang out sometimes after class, she's fun to talk to."
            elif RogueX.LikeEmma >= 600:
                ch_r "She's a really great teach, I love her lectures."
            elif RogueX.LikeEmma >= 500:
                ch_r "I don't know, she's ok."
            elif RogueX.LikeEmma >= 400:
                ch_r "I don't really like the way she looks at you in class."
            elif RogueX.LikeEmma >= 300:
                ch_r "I hate her  class." 
            else:
                ch_r "Ugh, that WITCH!"    
    elif Check == LauraX:
            if "poly Laura" in RogueX.Traits:  
                ch_r "We hook up from time to time. . ."    
            elif RogueX.LikeLaura >= 900:
                ch_r "She's got an animal magnetism to her. . ."
            elif RogueX.LikeLaura >= 800:
                ch_r "We really seem to get along. . ."    
            elif RogueX.LikeLaura >= 700:
                ch_r "She's a good friend."
            elif RogueX.LikeLaura >= 600:
                ch_r "She's a good teammate."
            elif RogueX.LikeLaura >= 500:
                ch_r "I don't know, she's ok in a fight."
            elif RogueX.LikeLaura >= 400:
                ch_r "We're. . . not in a good place."
            elif RogueX.LikeLaura >= 300:
                ch_r "I don't want to talk about it." 
            else:
                ch_r "That ho-bag skank?"          
    return
# End Rogue Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////    

label Rogue_Monogamy:
        #called from Rogue_Settings to ask her not to hook up wiht other girls    
        menu:
            "Could you not hook up with other girls?" if "mono" not in RogueX.Traits:
                    if RogueX.Thirst >= 60 and not ApprovalCheck(RogueX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ RogueX.FaceChange("sly",1) 
                            if "mono" not in RogueX.DailyActions:                                                         
                                    $ RogueX.Statup("Obed", 90, -2) 
                            ch_r "I might consider that, but you don't exactly make yourself available. . ."
                            return
                    elif ApprovalCheck(RogueX, 1200, "LO", TabM=0) and RogueX.Love >= RogueX.Obed:
                            #she cares
                            $ RogueX.FaceChange("sly",1) 
                            if "mono" not in RogueX.DailyActions:                                                         
                                    $ RogueX.Statup("Love", 90, 1) 
                            ch_r "Aw, would that make you jealous?" 
                            ch_r "I suppose I could restain myself. . ."
                    elif ApprovalCheck(RogueX, 700, "O", TabM=0):
                            #she is obedient
                            $ RogueX.FaceChange("sly",1,Eyes="side") 
                            ch_r "If that's what you really want. . ."
                    else:   
                            #she doesn't care
                            $ RogueX.FaceChange("sly",1,Brows="confused") 
                            ch_r "Who I \"hook up\" with is my own damned business." 
                            return                    
                    if "mono" not in RogueX.DailyActions:                                                         
                            $ RogueX.Statup("Obed", 90, 3) 
                    $ RogueX.AddWord(1,0,"mono","mono") #Daily
            "Don't hook up with other girls." if "mono" not in RogueX.Traits:
                    if ApprovalCheck(RogueX, 900, "O", TabM=0):
                            #she is obedient
                            $ RogueX.FaceChange("sly",1,Eyes="side") 
                            ch_r "Ok."
                    elif RogueX.Thirst >= 60 and not ApprovalCheck(RogueX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ RogueX.FaceChange("sly",1) 
                            if "mono" not in RogueX.DailyActions:                                                         
                                    $ RogueX.Statup("Obed", 90, -2) 
                            ch_r "I might consider that, but you don't exactly make yourself available. . ."
                            return
                    elif ApprovalCheck(RogueX, 550, "O", TabM=0):
                            #she is obedient
                            $ RogueX.FaceChange("sly",1,Eyes="side") 
                            ch_r "If that's what you really want. . ."
                    elif ApprovalCheck(RogueX, 1400, "LO", TabM=0):
                            #she cares
                            $ RogueX.FaceChange("sly",1) 
                            ch_r "Is that any way to ask a girl?" 
                            ch_r "Still, I'll do it for you. . ."
                    else:   
                            #she doesn't care
                            $ RogueX.FaceChange("sly",1,Brows="confused") 
                            ch_r "Who I \"hook up\" with is my own damned business." 
                            return                     
                    if "mono" not in RogueX.DailyActions:                                                         
                            $ RogueX.Statup("Obed", 90, 3) 
                    $ RogueX.AddWord(1,0,"mono","mono") #Daily
            "It's ok if you hook up with other girls." if "mono" in RogueX.Traits:
                    if ApprovalCheck(RogueX, 700, "O", TabM=0):
                            $ RogueX.FaceChange("sly",1,Eyes="side") 
                            ch_r "As you wish."
                    elif ApprovalCheck(RogueX, 800, "L", TabM=0):
                            $ RogueX.FaceChange("sly",1) 
                            ch_r "I hope you don't give me any reasons to want to. . ." 
                    else:
                            $ RogueX.FaceChange("sly",1,Brows="confused") 
                            if "mono" not in RogueX.DailyActions:                                                         
                                    $ RogueX.Statup("Love", 90, -2)
                            ch_r "Oh? Well, glad I got your permission there." 
                    if "mono" not in RogueX.DailyActions:                                                         
                            $ RogueX.Statup("Obed", 90, 3) 
                    if "mono" in RogueX.Traits:
                            $ RogueX.Traits.remove("mono")  
                    $ RogueX.AddWord(1,0,"mono") #Daily 
            "Never mind.":
                pass
        return
        
# end Rogue monogamy <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
   
   
label Rogue_Jumped:
        #called from Rogue_Settings to ask her not to jump you  
        ch_p "Hey, Remember that time you threw yourself at me?" 
        $ RogueX.FaceChange("sly",1,Brows="confused") 
        menu:
            ch_r "Yeah?"
            "Could you maybe just ask instead?" if "chill" not in RogueX.Traits:
                    if RogueX.Thirst >= 60 and not ApprovalCheck(RogueX, 1500, "LO", TabM=0):
                            #she's too thirsty
                            $ RogueX.FaceChange("sly",1) 
                            if "chill" not in RogueX.DailyActions:                                                         
                                    $ RogueX.Statup("Obed", 90, -2) 
                            ch_r "Maybe don't keep me waiting then. . ."
                            return
                    elif ApprovalCheck(RogueX, 1000, "LO", TabM=0) and RogueX.Love >= RogueX.Obed:
                            #she cares
                            $ RogueX.FaceChange("sly",1) 
                            if "chill" not in RogueX.DailyActions:                                                         
                                    $ RogueX.Statup("Love", 90, 1) 
                            ch_r "Sorry, [RogueX.Petname], I just got a little lonely. . ." 
                            ch_r "I'll be good. . ."
                    elif ApprovalCheck(RogueX, 500, "O", TabM=0):
                            #she is obedient
                            $ RogueX.FaceChange("sly",1,Eyes="side") 
                            ch_r "If that's what you really want. . ."
                    else:   
                            #she doesn't care
                            $ RogueX.FaceChange("sly",1,Brows="confused") 
                            ch_r "I can't make any promises." 
                            return                    
                    if "chill" not in RogueX.DailyActions:                                                         
                            $ RogueX.Statup("Obed", 90, 3) 
                    $ RogueX.AddWord(1,0,"chill","chill") #Daily
            "Don't bother me like that." if "chill" not in RogueX.Traits:
                    if ApprovalCheck(RogueX, 900, "O", TabM=0):
                            #she is obedient
                            $ RogueX.FaceChange("sly",1,Eyes="side") 
                            ch_r "Ok."
                    elif RogueX.Thirst >= 60 and not ApprovalCheck(RogueX, 600, "O", TabM=0):
                            #she's too thirsty
                            $ RogueX.FaceChange("sly",1) 
                            if "chill" not in RogueX.DailyActions:                                                         
                                    $ RogueX.Statup("Obed", 90, -2) 
                            ch_r "Maybe don't keep me waiting then. . ."
                            return
                    elif ApprovalCheck(RogueX, 450, "O", TabM=0):
                            #she is obedient
                            $ RogueX.FaceChange("sly",1,Eyes="side") 
                            ch_r "If that's what you really want. . ."
                    elif ApprovalCheck(RogueX, 500, "LO", TabM=0) and not ApprovalCheck(RogueX, 500, "I", TabM=0):
                            #she cares
                            $ RogueX.FaceChange("sly",1) 
                            ch_r "You might want to watch your mouth." 
                            ch_r "Still, I'll try to keep to myself. . ."
                    else:   
                            #she doesn't care
                            $ RogueX.FaceChange("sly",1,Brows="confused") 
                            ch_r "No promises." 
                            return                     
                    if "chill" not in RogueX.DailyActions:                                                         
                            $ RogueX.Statup("Obed", 90, 3) 
                    $ RogueX.AddWord(1,0,"chill","chill") #Daily
            "Knock yourself out.":
                    if ApprovalCheck(RogueX, 800, "L", TabM=0):
                            $ RogueX.FaceChange("sly",1) 
                            ch_r "Will do. . ." 
                    elif ApprovalCheck(RogueX, 700, "O", TabM=0):
                            $ RogueX.FaceChange("sly",1,Eyes="side") 
                            ch_r "Yes sir."
                    else:
                            $ RogueX.FaceChange("sly",1,Brows="confused") 
                            if "chill" not in RogueX.DailyActions:                                                         
                                    $ RogueX.Statup("Love", 90, -2)
                            ch_r "Maybe. If I've got nothing better to do." 
                    if "chill" not in RogueX.DailyActions:                                                         
                            $ RogueX.Statup("Obed", 90, 3) 
                    if "chill" in RogueX.Traits:
                            $ RogueX.Traits.remove("chill")  
                    $ RogueX.AddWord(1,0,"chill") #Daily 
            "Um, never mind.":
                pass
        return
        
# end Rogue jumped <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# start Rogue not a virgin
label Rogue_Not_Virgin:
    menu:
        "I noticed that when we had sex, you didn't seem to be a virgin."
        "Wasn't I your first time?":
            $ RogueX.FaceChange("bemused", 1)
            $ RogueX.Statup("Love", 60, 5)
            $ RogueX.Statup("Obed", 20, 15)
            ch_r "Oh, no! You definitely were, it's just. . . you know,"
            ch_r "I lead a pretty active lifestyle, so I lost that physical barrier years ago."
        "So you get around?":
            $ RogueX.FaceChange("sexy", 1)
            $ RogueX.Brows = "angry"
            $ RogueX.Statup("Obed", 30, 15)
            $ RogueX.Statup("Obed", 60, 5)
            $ RogueX.Statup("Inbt", 30, 15)
            $ RogueX.Statup("Inbt", 60, 5)
            ch_r "Jerk, not like that. I tore it years ago in combat training."
        "Are you a slut?":
            $ RogueX.FaceChange("angry", 1)          
            $ RogueX.Statup("Love", 30, -20, 1)
            $ RogueX.Statup("Love", 60, -40, 1)
            $ RogueX.Statup("Obed", 30, 30)
            $ RogueX.Statup("Obed", 60, 20)
            ch_r "If you'd like to find that out, you might want to rethink how you talk to me, [RogueX.Petname]."
    $ RogueX.Chat[0] = 1
    return

# end rogue not a virgin //////////////////////////////////////////////////////////

# start rogue hungry //////////////////////////////////////////////////////////
label Rogue_Hungry:
    if RogueX.Chat[3]:
        ch_r "You know, I've really come to enjoy the taste of your. . . cum. I think I'd like some more of that."
    elif RogueX.Chat[2]:
        ch_r "You know, I've really come to enjoy the taste of your, serum. It's like my favorite drink!"
    else:
        ch_r "You know, I've really come to enjoy the taste of your. . . cum. I think I'd like some more of that."
    $ RogueX.Traits.append("hungry")
return


# end rogue hungry //////////////////////////////////////////////////////////

# Rogue Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label Rogue_SexChat:
    $ Line = "Yeah, what did you want to talk about?" if not Line else Line
    while True:
            menu:
                ch_r "[Line]"                
                "My favorite thing to do is. . .":
                    if "setfav" in RogueX.DailyActions:
                        ch_r "Yeah, I know. You just told me earlier."
                    else:
                        menu:
                            "Sex.":
                                        $ RogueX.FaceChange("sly")
                                        if RogueX.PlayerFav == "sex":
                                            $ RogueX.Statup("Lust", 80, 5)
                                            ch_r "Yeah, I know that. . ."                                
                                        elif RogueX.Favorite == "sex":
                                            $ RogueX.Statup("Love", 90, 5)
                                            $ RogueX.Statup("Lust", 80, 10)
                                            ch_r "Oooh, I love a good pipe cleaning too. . ."
                                        elif RogueX.Sex >= 5:
                                            ch_r "Can't say as I mind a good roll in the hay."
                                        elif not RogueX.Sex:
                                            $ RogueX.FaceChange("perplexed")
                                            ch_r "Who {i}exactly{/i} are y'all having sex {i}with?{/i}"
                                        else:
                                            $ RogueX.FaceChange("bemused")
                                            ch_r "Heh, [RogueX.Petname], flithy mouth on you. . ."
                                        $ RogueX.PlayerFav = "sex"
                                        
                            "Anal.":
                                        $ RogueX.FaceChange("sly")
                                        if RogueX.PlayerFav == "anal":
                                            $ RogueX.Statup("Lust", 80, 5)
                                            ch_r "So I hear. . ."                                
                                        elif RogueX.Favorite == "anal":
                                            $ RogueX.Statup("Love", 90, 5)
                                            $ RogueX.Statup("Lust", 80, 10)
                                            ch_r "I can't say as I mind that. . ."
                                        elif RogueX.Anal >= 10:
                                            ch_r "It's not a bad way to spend some time. . ."
                                        elif not RogueX.Anal:
                                            $ RogueX.FaceChange("perplexed")
                                            ch_r "Who {i}exactly{/i} are y'all fucking {i}with?{/i}"
                                        else:
                                            $ RogueX.FaceChange("bemused")
                                            ch_r "Heh, heh, I . . . I don't {i}mind{/i} it. . ."
                                        $ RogueX.PlayerFav = "anal"
                                        
                            "Blowjobs.":   
                                        $ RogueX.FaceChange("sly")
                                        if RogueX.PlayerFav == "blow":
                                            $ RogueX.Statup("Lust", 80, 3)
                                            ch_r "I'm not surprised. . ."                                
                                        elif RogueX.Favorite == "blow":
                                            $ RogueX.Statup("Love", 90, 5)
                                            $ RogueX.Statup("Lust", 80, 5)
                                            ch_r "I guess I have developed a real taste for you. . ."
                                        elif RogueX.Blow >= 10:
                                            ch_r "I'm getting to enjoy it too . . ."
                                        elif not RogueX.Blow:
                                            $ RogueX.FaceChange("perplexed")
                                            ch_r "Who {i}exactly{/i} is sucking you off?"
                                        else:
                                            $ RogueX.FaceChange("bemused")
                                            ch_r "I'm. . . getting used to the taste. . ."
                                        $ RogueX.PlayerFav = "blow"     
                                        
                            "Titjobs.":
                                        $ RogueX.FaceChange("sly")    
                                        if RogueX.PlayerFav == "titjob":
                                            $ RogueX.Statup("Lust", 80, 5)
                                            ch_r "So I hear. . ."                           
                                        elif RogueX.Favorite == "titjob":
                                            $ RogueX.Statup("Love", 90, 5)
                                            $ RogueX.Statup("Lust", 80, 7)
                                            ch_r "I really enjoy it too. . ."
                                        elif RogueX.Tit >= 10:
                                            ch_r "It's certainly an interesting experience . . ."
                                        elif not RogueX.Tit:
                                            $ RogueX.FaceChange("perplexed")
                                            ch_r "Who {i}exactly{/i} is tit fucking you?"
                                        else:
                                            $ RogueX.FaceChange("bemused")
                                            ch_r "I can't say as I blame you. . ."
                                        $ RogueX.PlayerFav = "titjob"   
                                        
                            "Footjobs.":
                                        $ RogueX.FaceChange("sly")
                                        if RogueX.PlayerFav == "foot":
                                            $ RogueX.Statup("Lust", 80, 5)
                                            ch_r "Yeah, you've said that before. . ."                                
                                        elif RogueX.Favorite == "foot":
                                            $ RogueX.Statup("Love", 90, 5)
                                            $ RogueX.Statup("Lust", 80, 7)
                                            ch_r "I do enjoy that sensation. . ."
                                        elif RogueX.Foot >= 10:
                                            ch_r "It is pretty nice to touch someone like that . . ."
                                        elif not RogueX.Foot:
                                            $ RogueX.FaceChange("perplexed")
                                            ch_r "Who {i}exactly{/i} is jerking you off?"
                                        else:
                                            $ RogueX.FaceChange("bemused")
                                            ch_r "I do like the sensation. . ."
                                        $ RogueX.PlayerFav = "foot"  
                                        
                            "Handjobs.":
                                        $ RogueX.FaceChange("sly")
                                        if RogueX.PlayerFav == "hand":
                                            $ RogueX.Statup("Lust", 80, 5)
                                            ch_r "Yeah, you've said that before. . ."                                
                                        elif RogueX.Favorite == "hand":
                                            $ RogueX.Statup("Love", 90, 5)
                                            $ RogueX.Statup("Lust", 80, 7)
                                            ch_r "I love how you feel in my hand. . ."
                                        elif RogueX.Hand >= 10:
                                            ch_r "It is pretty nice to touch someone like that . . ."
                                        elif not RogueX.Hand:
                                            $ RogueX.FaceChange("perplexed")
                                            ch_r "Who {i}exactly{/i} is jerking you off?"
                                        else:
                                            $ RogueX.FaceChange("bemused")
                                            ch_r "I do like the sensation. . ."
                                        $ RogueX.PlayerFav = "hand"  
                                        
                            "Feeling you up.":
                                        $ Cnt = RogueX.FondleB + RogueX.FondleT + RogueX.SuckB + RogueX.Hotdog
                                        $ RogueX.FaceChange("sly")
                                        if RogueX.PlayerFav == "fondle":
                                            $ RogueX.Statup("Lust", 80, 3)
                                            ch_r "Yeah, I think we've established that. . ."                                
                                        elif RogueX.Favorite in ("hotdog","suck breasts","fondle breasts","fondle thighs"):
                                            $ RogueX.Statup("Love", 90, 5)
                                            $ RogueX.Statup("Lust", 80, 5)
                                            ch_r "I love how you touch me. . ."
                                        elif Cnt >= 10:
                                            ch_r "It's nice to have someone who can really touch me . . ."
                                        elif not Cnt:
                                            $ RogueX.FaceChange("perplexed")
                                            ch_r "Who {i}exactly{/i} are you feeling up?"
                                        else:
                                            $ RogueX.FaceChange("bemused")
                                            ch_r "I do like how that feels. . ."
                                        $ RogueX.PlayerFav = "fondle"  
                                        $ Cnt = 0
                                
                            "Kissing you.":
                                        $ RogueX.FaceChange("sly")
                                        if RogueX.PlayerFav == "kiss you":
                                            $ RogueX.Statup("Love", 90, 3)
                                            ch_r "I've heard it before, but don't mind hearing it again. . ."                                
                                        elif RogueX.Favorite == "kiss you":
                                            $ RogueX.Statup("Love", 90, 5)
                                            $ RogueX.Statup("Lust", 80, 5)
                                            ch_r "I can't get over your lips either. . ."
                                        elif RogueX.Kissed >= 10:
                                            ch_r "I love kissing you too . . ."
                                        elif not RogueX.Kissed:
                                            $ RogueX.FaceChange("perplexed")
                                            ch_r "Who {i}exactly{/i} are you smooch'in?"
                                        else:
                                            $ RogueX.FaceChange("bemused")
                                            ch_r "It's nice being able to kiss someone without hurting them. . ."
                                        $ RogueX.PlayerFav = "kiss you" 
                                
                        $ RogueX.DailyActions.append("setfav") 
                            
                "What's your favorite thing to do?":
                                if not ApprovalCheck(RogueX, 800):
                                        $ RogueX.FaceChange("perplexed")
                                        ch_r "I don't think that's any of your business. . ."                                    
                                else:
                                        if RogueX.SEXP >= 50:
                                            $ RogueX.FaceChange("sly")
                                            ch_r "If you can't tell. . ."   
                                        else:                 
                                            $ RogueX.FaceChange("bemused")
                                            $ RogueX.Eyes = "side"
                                            ch_r "I don't know, I guess maybe. . ."
                                            
                                            
                                        if not RogueX.Favorite or RogueX.Favorite == "kiss":
                                            ch_r "I guess I love it when we kiss. . ."  
                                        elif RogueX.Favorite == "anal":
                                            if RogueX.Anal >= 10:
                                                ch_r "I like when you fuck my ass."  
                                            else:
                                                ch_r "I like when you stick it in my. . . butt."  
                                        elif RogueX.Favorite == "lick ass":
                                                ch_r "I like when you lick my. . . asshole." 
                                        elif RogueX.Favorite == "insert ass":
                                                ch_r "I like when you . . . finger my asshole." 
                                        elif RogueX.Favorite == "sex":
                                                ch_r "I like when you fuck me hard." 
                                        elif RogueX.Favorite == "lick pussy":
                                                ch_r "I like when you lick my pussy." 
                                        elif RogueX.Favorite == "fondle pussy":
                                                ch_r "I like when you fingerblast me." 
                                        elif RogueX.Favorite == "blow":
                                                ch_r "I kind of like to suck your cock." 
                                        elif RogueX.Favorite == "tit":
                                                ch_r "I like to work your cock with my tits." 
                                        elif RogueX.Favorite == "hand":
                                                ch_r "I like the feel of your cock in my hand." 
                                        elif RogueX.Favorite == "foot":
                                                ch_r "I kinda like to use my feet." 
                                        elif RogueX.Favorite == "hotdog":
                                                ch_r "I like it when you grind against me." 
                                        elif RogueX.Favorite == "suck breasts":
                                                ch_r "I like it when you suck on my tits."  
                                        elif RogueX.Favorite == "fondle breasts":
                                                ch_r "I like it when you feel up my tits." 
                                        elif RogueX.Favorite == "fondle thighs":
                                                ch_r "I like it when you massage my thighs."
                                        else:
                                                ch_r "I don't really know. . ."    
                                                
                                # End Rogue's favorite things.
                                        
                "Don't talk as much during sex." if "vocal" in RogueX.Traits:
                        if "setvocal" in RogueX.DailyActions:
                            $ RogueX.FaceChange("perplexed")
                            ch_r "We've been over this already."
                        else:              
                            if ApprovalCheck(RogueX, 1000) and RogueX.Obed <= RogueX.Love:
                                $ RogueX.FaceChange("bemused")
                                $ RogueX.Statup("Obed", 90, 1)
                                ch_r "Heh, ok, if that's what you want. . ."
                                $ RogueX.Traits.remove("vocal")   
                            elif ApprovalCheck(RogueX, 700, "O"):
                                $ RogueX.FaceChange("sadside")
                                $ RogueX.Statup("Obed", 90, 1)
                                ch_r "If that's what you want, [RogueX.Petname]."
                                $ RogueX.Traits.remove("vocal")   
                            elif ApprovalCheck(RogueX, 600):
                                $ RogueX.FaceChange("sly")
                                $ RogueX.Statup("Love", 90, -3)
                                $ RogueX.Statup("Obed", 50, -1)
                                $ RogueX.Statup("Inbt", 90, 5)
                                ch_r "I'll say what I want, and you'll like it, [RogueX.Petname]."
                            else:
                                $ RogueX.FaceChange("angry")
                                $ RogueX.Statup("Love", 90, -5)
                                $ RogueX.Statup("Obed", 60, -3)
                                $ RogueX.Statup("Inbt", 90, 10)
                                ch_r "Fuck you, I'll talk as much as I want."
                                                
                            $ RogueX.DailyActions.append("setvocal")   
                "Talk dirty to me during sex." if "vocal" not in RogueX.Traits:
                        if "setvocal" in RogueX.DailyActions:
                            $ RogueX.FaceChange("perplexed")
                            ch_r "We've been over this already."
                        else:     
                            if ApprovalCheck(RogueX, 1000) and RogueX.Obed <= RogueX.Love:
                                $ RogueX.FaceChange("sly")
                                $ RogueX.Statup("Obed", 90, 2)
                                ch_r "Heh, ok, if that's what you want. . ."
                                $ RogueX.Traits.append("vocal")   
                            elif ApprovalCheck(RogueX, 700, "O"):
                                $ RogueX.FaceChange("sadside")
                                $ RogueX.Statup("Obed", 90, 2)
                                ch_r "If that's what you want, [RogueX.Petname]."
                                $ RogueX.Traits.append("vocal")   
                            elif ApprovalCheck(RogueX, 600):
                                $ RogueX.FaceChange("sly")
                                $ RogueX.Statup("Obed", 90, 3)
                                ch_r "I can give it a shot, [RogueX.Petname]."
                                $ RogueX.Traits.append("vocal")   
                            else:
                                $ RogueX.FaceChange("angry")
                                $ RogueX.Statup("Inbt", 90, 5)
                                ch_r "I'll say what I want, when I want."  
                                
                            $ RogueX.DailyActions.append("setvocal")  
                        # End Rogue Dirty Talk
                                        
                "Don't do your own thing as much during sex." if "passive" not in RogueX.Traits:
                        if "initiative" in RogueX.DailyActions:
                                $ RogueX.FaceChange("perplexed")
                                ch_r "We've been over this already."
                        else:       
                            if ApprovalCheck(RogueX, 1000) and RogueX.Obed <= RogueX.Love:
                                $ RogueX.FaceChange("bemused")
                                $ RogueX.Statup("Obed", 90, 1)
                                ch_r "Heh, ok, lead the way. . ."  
                                $ RogueX.Traits.append("passive")                     
                            elif ApprovalCheck(RogueX, 700, "O"):
                                $ RogueX.FaceChange("sadside")
                                $ RogueX.Statup("Obed", 90, 1)
                                ch_r "I'll restrain myself then, [RogueX.Petname]."
                                $ RogueX.Traits.append("passive")
                            elif ApprovalCheck(RogueX, 600):
                                $ RogueX.FaceChange("sly")
                                $ RogueX.Statup("Love", 90, -3)
                                $ RogueX.Statup("Obed", 50, -1)
                                $ RogueX.Statup("Inbt", 90, 5)
                                ch_r "You know you don't want that, [RogueX.Petname]."
                            else:
                                $ RogueX.FaceChange("angry")
                                $ RogueX.Statup("Love", 90, -5)
                                $ RogueX.Statup("Obed", 60, -3)
                                $ RogueX.Statup("Inbt", 90, 10)
                                ch_r "I'll do what I want, prick."
                                
                            $ RogueX.DailyActions.append("initiative")  
                "Take more initiative during sex." if "passive" in RogueX.Traits:
                        if "initiative" in RogueX.DailyActions:
                                $ RogueX.FaceChange("perplexed")
                                ch_r "We've been over this already."
                        else:   
                            if ApprovalCheck(RogueX, 1000) and RogueX.Obed <= RogueX.Love:
                                $ RogueX.FaceChange("bemused")
                                $ RogueX.Statup("Obed", 90, 1)
                                ch_r "Heh, I think I can handle that. . ."     
                                $ RogueX.Traits.remove("passive")                   
                            elif ApprovalCheck(RogueX, 700, "O"):
                                $ RogueX.FaceChange("sadside")
                                $ RogueX.Statup("Obed", 90, 1)
                                ch_r "I can do that, [RogueX.Petname]."
                                $ RogueX.Traits.remove("passive")   
                            elif ApprovalCheck(RogueX, 600):
                                $ RogueX.FaceChange("sly")
                                $ RogueX.Statup("Obed", 90, 3)
                                ch_r "I can certainly try, [RogueX.Petname]."
                                $ RogueX.Traits.remove("passive")   
                            else:
                                $ RogueX.FaceChange("angry")
                                $ RogueX.Statup("Inbt", 90, 5)
                                ch_r "If I want to, I will, but not because you say so."  
                                
                            $ RogueX.DailyActions.append("initiative")   
                            
                "About getting Jumped" if "jumped" in RogueX.History:
                        call Rogue_Jumped
                "About when you masturbate":
                        call NoFap(RogueX)
                    
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
        if RogueX not in Digits:
            if ApprovalCheck(RogueX, 500, "L") or ApprovalCheck(RogueX, 250, "I"):
                    ch_r "You know, I never got around to giving you my number, here you go."
                    $ Digits.append(RogueX)  
                    return
            elif ApprovalCheck(RogueX, 250, "O"):
                    ch_r "You know, you should probably have my number, here you go."             
                    $ Digits.append(RogueX)
                    return
        if "hungry" not in RogueX.Traits and (RogueX.Swallow + RogueX.Chat[2]) >= 10 and RogueX.Loc == bg_current:  #She's swallowed a lot        
                    call Rogue_Hungry
                    return  
        if not Taboo or ApprovalCheck(RogueX, 800, "I"):
                    if RogueX.Loc == bg_current and RogueX.Thirst >= 30 and "refused" not in RogueX.DailyActions and "quicksex" not in RogueX.DailyActions: 
                            $ RogueX.FaceChange("sly",1)    
                            ch_r "Hey, do you want to get a little frisky?"
                            call Quick_Sex(RogueX)
                    return
        
        #adds options based on accomplishments
        if ApprovalCheck(RogueX, 1200):
            $ Options.append("dance") 
        if ApprovalCheck(RogueX, 800, "L") and "nametag chat" not in RogueX.DailyActions:
            $ Options.append("close")            
        if RogueX.Blow >= 2:
            $ Options.append("blow")        
        if "steal" in RogueX.Traits:
            $ Options.append("steal")
        if PunishmentX and "caught chat" not in RogueX.DailyActions:
            $ Options.append("caught")
        if RogueX.Event[0] and "key chat" not in RogueX.DailyActions:
            $ Options.append("key")
        if "lover" in RogueX.Petnames and ApprovalCheck(RogueX, 900, "L"): # luvy dovey       
            $ Options.append("luv")
              
        if "mandrill" in Player.Traits and "cologne chat" not in RogueX.DailyActions:
            $ Options.append("mandrill")        
        if "purple" in Player.Traits and "cologne chat" not in RogueX.DailyActions:
            $ Options.append("purple")        
        if "corruption" in Player.Traits and "cologne chat" not in RogueX.DailyActions:
            $ Options.append("corruption")
                    
        if not RogueX.Chat[0] and RogueX.Sex:
            $ Options.append("virgin")    
            
        if (bg_current == "bg rogue" or bg_current == "bg player") and "nametag chat" not in RogueX.DailyActions:
            if "lover" not in RogueX.Petnames and ApprovalCheck(RogueX, 900, "L"): # RogueX.Event[6]        
                $ Options.append("lover?")
            elif "sir" not in RogueX.Petnames and ApprovalCheck(RogueX, 500, "O"): # RogueX.Event[7]
                $ Options.append("sir?")     
            elif "daddy" not in RogueX.Petnames and ApprovalCheck(RogueX, 750, "L") and ApprovalCheck(RogueX, 500, "O") and ApprovalCheck(RogueX, 500, "I"): # RogueX.Event[5]
                $ Options.append("daddy?")
            elif "master" not in RogueX.Petnames and ApprovalCheck(RogueX, 900, "O"): # RogueX.Event[8]
                $ Options.append("master?")
            elif "sex friend" not in RogueX.Petnames and ApprovalCheck(RogueX, 500, "I"): # RogueX.Event[9]
                $ Options.append("sexfriend?")
            elif "fuck buddy" not in RogueX.Petnames and ApprovalCheck(RogueX, 900, "I"): # RogueX.Event[10]
                $ Options.append("fuckbuddy?")  
        
        if not ApprovalCheck(RogueX, 300):            #She dislikes you
            $ Options.append("hate") 
    
    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one
    
    if Options[0] == "virgin": # "virgin line" not yet triggered:
        call Rogue_Not_Virgin
    
    elif Options[0] == "mandrill":                             
        $ RogueX.DailyActions.append("cologne chat") 
        $ RogueX.FaceChange("confused")
        ch_r "(sniff, sniff). . . something kind of smells like monkey butt in here. . ."
        $ RogueX.FaceChange("sly", 1)
        ch_r ". . . but you're looking pretty handsome today, [RogueX.Petname]."    
    elif Options[0] == "purple":              
        $ RogueX.DailyActions.append("cologne chat") 
        $ RogueX.FaceChange("sly",1)
        ch_r "(sniff, sniff). . . hmm, you're smelling good today. . ."
        ch_r ". . . was there anything I could do to make you happy?"    
    elif Options[0] == "corruption":              
        $ RogueX.DailyActions.append("cologne chat") 
        $ RogueX.FaceChange("confused")
        ch_r "(sniff, sniff). . . that's a pretty strong scent you've got there. . ."
        $ RogueX.FaceChange("sly")
        ch_r ". . . I'm gettin some pretty naughty thoughts over here, [RogueX.Petname]. . ."
        
    elif Options[0] == "blow":
        $ Line = renpy.random.choice(["You know, you taste better than I thought.", 
                "You're making my jaw a bit sore there.", 
                "Let me know if you want a little mouth attention.",
                "Hmmm. . . [she mimes her tongue knocking against her cheek.]"])
        ch_r "[Line]"
        
    elif Options[0] == "close": # RogueX.Love >= 800
        ch_r "It's always been hard for me to get close to people, since I could never. . ."
        ch_r "get {i}close{/i} to them, you know?"    
        ch_r "It's been real good for me to be able to get close to you like this."
        $ RogueX.DailyActions.append("close chat") 
    elif Options[0] == "caught": # Xavier's caught you
        ch_r "Wow, that was scary getting dragged into the Professor's office."
        if not ApprovalCheck(RogueX, 500, "I"):
            ch_r "Maybe we should be more careful about where we. . . you know."
        else:
            ch_r "Maybe we should be more careful about where we fuck."
        $ RogueX.DailyActions.append("caught chat") 
    elif Options[0] == "key": # you have her key
        if RogueX.SEXP <= 15:
            ch_r "I'm glad you have my key now, just don't use it for any funny business. . ."
        else:
            ch_r "I'm glad you have my key now, maybe you could . . . \"surprise\" me sometime. . ."
        $ RogueX.DailyActions.append("key chat") 
    elif Options[0] == "touch": # "touch" in RogueX.Traits:
        ch_r "It's only because I've been working with you so much that I've been able to learn to control my abilities."
        ch_r "If it weren't for you, I wouldn't have been able to touch anyone!"
    elif Options[0] == "steal": # "steal" in RogueX.Traits:
        ch_r "It's only because of having worked with you and your powers that I've learned to permanently copy other mutant powers."   
    elif Options[0] == "dance": # dancing comes up
        ch_r "Can't wait for the next big party."
        ch_r "I love to dance, and I've got the best partner to grind with-"
        call Rogue_Doggy_Launch("massage")
        if RogueX.Legs == "skirt":
            $ RogueX.Upskirt = 1
            if RogueX.Panties and RogueX.SeenPanties and ApprovalCheck(RogueX, 800, TabM = 3):
                pass
            elif RogueX.Panties and ApprovalCheck(RogueX, 800, TabM = 3):
                $ RogueX.SeenPanties = 1
            elif RogueX.Panties:
                $ RogueX.Upskirt = 0                            
            elif RogueX.SeenPussy and ApprovalCheck(RogueX, 1000, TabM = 4):
                pass
            elif ApprovalCheck(RogueX, 1400, TabM = 3):
                call Rogue_First_Bottomless(1)  
            else:
                $ RogueX.Upskirt = 0            
            pause 0.5  
            $ RogueX.Upskirt = 0      
        ch_r "Y'know what I'm sayin', [RogueX.Petname]?"        
        $ RogueX.Upskirt = 0      
        call Rogue_Doggy_Reset

        
    elif Options[0] == "luv": # love maxed out
        $ RogueX.FaceChange("bemused", 1)
        ch_r ". . ."
        ch_r "You know, time was, I really thought I'd end up alone, unable to touch anyone. . ."        
        $ RogueX.FaceChange("smile")
        ch_r "I'm really glad that I was able to find you."
        ch_r "I love you, [RogueX.Petname]."
        menu:
            extend ""
            "I love you too.":
                $ RogueX.Statup("Love", 200, 10)
                $ RogueX.Statup("Obed", 80, 4)
                $ RogueX.Statup("Inbt", 80, 4)
            "I love you too, [RogueX.Pet].":
                $ RogueX.NameCheck()
                if _return:                    
                    $ RogueX.FaceChange("angry")
                    $ RogueX.Statup("Love", 90, -1)
                    $ RogueX.Statup("Obed", 80, 10)
                    $ RogueX.Statup("Inbt", 80, 4)
                else:
                    $ RogueX.Statup("Love", 200, 10)
                    $ RogueX.Statup("Obed", 80, 4)
                    $ RogueX.Statup("Inbt", 80, 4)
            "Yeah, same here.":                
                $ RogueX.FaceChange("perplexed")
                $ RogueX.Statup("Love", 90, -1)
                $ RogueX.Statup("Obed", 80, 10)
                $ RogueX.Statup("Inbt", 80, 4)
            "Whatever.":
                $ RogueX.FaceChange("angry")
                $ RogueX.Statup("Love", 200, -10)
                $ RogueX.Statup("Obed", 80, 4)
                $ RogueX.Statup("Inbt", 80, 10)
    
    elif Options[0] == "boyfriend?":
        call Rogue_BF
        $ RogueX.DailyActions.append("nametag chat") 
    elif Options[0] == "lover?":
        call Rogue_Love
        $ RogueX.DailyActions.append("nametag chat") 
    elif Options[0] == "sir?":
        call Rogue_Sub
        $ RogueX.DailyActions.append("nametag chat") 
    elif Options[0] == "master?":
        call Rogue_Master
        $ RogueX.DailyActions.append("nametag chat") 
    elif Options[0] == "sexfriend?":
        call Rogue_Sexfriend
        $ RogueX.DailyActions.append("nametag chat") 
    elif Options[0] == "fuckbuddy?":
        call Rogue_Fuckbuddy 
        $ RogueX.DailyActions.append("nametag chat")  
    elif Options[0] == "daddy?":
        call Rogue_Daddy  
        $ RogueX.DailyActions.append("nametag chat") 
        
    elif Options[0] == "hate": # trinty lower then 50:
        $ Line = renpy.random.choice(["Get away from me.", 
                "I don't want to see your face.", 
                "Stop bothering me.",
                "Leave me alone."])
        ch_r "[Line]"
        
    else: #all else fell through. . .
        $ D20 = renpy.random.randint(1, 16)
        if D20 == 1:
                $ RogueX.FaceChange("confused")
                ch_r "I'm so nervous about this Genetics test with Professor McCoy. I don't get this stuff at all."
        elif D20 == 2:
                $ RogueX.FaceChange("sad")
                ch_r "Feeling kinda down today, [RogueX.Petname]. Family problems. It's. . .kinda complicated."
        elif D20 == 3:
                $ RogueX.FaceChange("sly")
                ch_r "So, um. . .maybe you heard about the friends I used to hang out with? They're not all as bad as they seem. Mostly."
        elif D20 == 4:
                $ RogueX.FaceChange("smile")
                ch_r "I had the best workout earlier in the Danger Room today! Wish you coulda seen me!"
        elif D20 == 5:
                $ RogueX.FaceChange("smile")
                ch_r "Ever wonder what it would be like to be able to fly? That's gotta be the coolest power, right?"
        elif D20 == 6:
                $ RogueX.FaceChange("smile")
                ch_r "Ever been out to Breakstone Lake, behind the Mansion? It's so nice and peaceful. Kinda reminds me of back home in Mississippi, during the summer. Just a little chillier."
        elif D20 == 7:
                $ RogueX.FaceChange("smile")
                $ RogueX.Eyes = "surprised"
                ch_r "I just saw the coolest thing, when I was walking through the courtyard! A bunch of deer, in the woods, just over by the fence!"
                $ RogueX.Eyes = "side"
                ch_r "Their fur looked so. . .{i}soft{/i}. I wonder what they actually feel like?"
        elif D20 == 8:
                $ RogueX.FaceChange("smile")
                ch_r "Hey, did you see the Avengers on the news this morning?  Those guys make everything look {i}so{/i} easy!"
        elif D20 == 9:
                $ RogueX.FaceChange("smile")
                ch_r "A couple of us are gonna get together and go for a jog around one of the Mansion's sub-basements tomorrow. You should come with us!"
        elif D20 == 10:
                $ RogueX.FaceChange("down")
                ch_r "I have {i}so{/i} much homework this week! And I {i}so{/i} don't feel like doing any of it!"
        elif D20 == 11:
                $ RogueX.FaceChange("startled")
                ch_r "Y'know, I {i}really{/i} hate my powers. But could you imagine having Professor Xavier's?" 
                ch_r "I don't know if I could handle that kind of responsibility."
                ch_r "Might be even worse than mine, in their own way."
        elif D20 == 12:
                $ RogueX.FaceChange("sad")
                ch_r "The Mansion's a great place to live. . .but sometimes I get weirded out when I think how we could get attacked by some super-maniac any given second."
        elif D20 == 13:
                $ RogueX.FaceChange("smile")
                ch_r "I love it when you get a really good night's sleep. Feels amazing!"
        elif D20 == 14:
                $ RogueX.FaceChange("bemused")
                ch_r "I heard they're thinking about maybe having a school dance this year. That could be. . .{i}interesting{/i}."
        elif D20 == 15:
                $ RogueX.FaceChange("smile")
                ch_r "You been outside today? Wow, is it gorgeous!"
        elif D20 == 16:
                $ RogueX.FaceChange("smile")
                ch_r "You know, I tagged Wolverine once,"
                $ RogueX.FaceChange("sadside")  
                $ RogueX.Brows = "confused"
                ch_r "I still catch myself calling people \"bub\" from time to time."  
        else:
                $ RogueX.FaceChange("smile")
                ch_r "I like hanging out with you like this!"
    $ Line = 0
    return

# start Rogue_Names//////////////////////////////////////////////////////////
label Rogue_Names:  
        #Sets pet names from Rogue
        if ApprovalCheck(RogueX, 600, "L", TabM=0) or ApprovalCheck(RogueX, 300, "O", TabM=0):
            pass   
        else:
            $ RogueX.Mouth = "smile"
            ch_r "I'll call you what I like, [RogueX.Petname], and you'll like it."
            return
        menu:
            ch_r "Oh? What would you like me to call you?"
            "Sugar's fine.":
                    $ RogueX.Petname = "sugar"
                    ch_r "You got it, sugar."
            "Call me by my name.":
                    $ RogueX.Petname = Player.Name            
                    ch_r "If you'd rather, [RogueX.Petname]."
            "Call me \"boyfriend\"." if "boyfriend" in RogueX.Petnames:
                    $ RogueX.Petname = "boyfriend"
                    ch_r "Sure thing, [RogueX.Petname]."
            "Call me \"lover\"." if "lover" in RogueX.Petnames:
                    $ RogueX.Petname = "lover"
                    ch_r "Oooh, love to, [RogueX.Petname]."
            "Call me \"sir\"." if "sir" in RogueX.Petnames:
                    $ RogueX.Petname = "sir"
                    ch_r "Yes, [RogueX.Petname]."
            "Call me \"master\"." if "master" in RogueX.Petnames:
                    $ RogueX.Petname = "master"
                    ch_r "As you wish, [RogueX.Petname]."
            "Call me \"sex friend\"." if "sex friend" in RogueX.Petnames:
                    $ RogueX.Petname = "sex friend"
                    ch_r "Heh, very cheeky, [RogueX.Petname]."
            "Call me \"fuck buddy\"." if "fuck buddy" in RogueX.Petnames:
                    $ RogueX.Petname = "fuck buddy"
                    ch_r "I'm game if you are, [RogueX.Petname]."        
            "Call me \"daddy\"." if "daddy" in RogueX.Petnames:
                    $ RogueX.Petname = "daddy"
                    ch_r "Oh! You bet, [RogueX.Petname]."
            "Nevermind.":
                return
        return
# end Rogue_Names//////////////////////////////////////////////////////////

label Rogue_Pet:  
        #sets what you call Rogue
        if ApprovalCheck(RogueX, 600, "L", TabM=0):
            ch_r "Oh? What is it?" 
        elif ApprovalCheck(RogueX, 300, "O", TabM=0):
            ch_r "What did you want to call me?"
        else:
            ch_r "Oh, this should be good. . ."   
        while 1:
            menu:
                extend ""
                "Polite":
                    menu:
                        extend ""
                        "I think I'll just call you Rogue.":
                            $ RogueX.Pet = "Rogue"            
                            ch_r "I don't see why not, [RogueX.Petname]."
                            
                        "I think I'll call you \"girl\".":
                            $ RogueX.Pet = "girl"
                            if "boyfriend" in RogueX.Petnames or ApprovalCheck(RogueX, 500, "L"):
                                $ RogueX.FaceChange("sexy", 1) 
                                ch_r "I sure am your girl, [RogueX.Petname]."
                            else:      
                                $ RogueX.FaceChange("angry")           
                                ch_r "I ain't your girl, [RogueX.Petname]." 
                                
                        "I think I'll call you \"boo\".":
                            $ RogueX.Pet = "boo"
                            if "boyfriend" in RogueX.Petnames or ApprovalCheck(RogueX, 500, "L"):
                                $ RogueX.FaceChange("sexy", 1) 
                                ch_r "Aw, I am your boo, [RogueX.Petname]."
                            else:     
                                $ RogueX.FaceChange("angry")            
                                ch_r "I ain't your boo,  [RogueX.Petname]."
                                
                        "I think I'll call you \"bae\".":
                            $ RogueX.Pet = "bae"
                            if "boyfriend" in RogueX.Petnames or ApprovalCheck(RogueX, 500, "L"):
                                $ RogueX.FaceChange("sexy", 1) 
                                ch_r "Aw, I am your bae, [RogueX.Petname]."
                            else:     
                                $ RogueX.FaceChange("angry")            
                                ch_r "I ain't your bae,  [RogueX.Petname]."
                                
                        "I think I'll call you \"baby\".":
                            $ RogueX.Pet = "baby"
                            if "boyfriend" in RogueX.Petnames or ApprovalCheck(RogueX, 500, "L"):
                                $ RogueX.FaceChange("sexy", 1) 
                                ch_r "Aw, cute, [RogueX.Petname]."
                            else:     
                                $ RogueX.FaceChange("angry")            
                                ch_r "I ain't your baby, [RogueX.Petname]." 
                                
                        "I think I'll call you \"chere\".":
                            $ RogueX.Pet = "chere"
                            if "lover" in RogueX.Petnames or ApprovalCheck(RogueX, 600, "L"):
                                $ RogueX.FaceChange("sexy", 1) 
                                ch_r "Oh, tre romantic, [RogueX.Petname]."
                            else:     
                                $ RogueX.FaceChange("angry", 1)  
                                $ RogueX.Eyes = "side"
                                ch_r "That has some. . . bad memories, [RogueX.Petname]." 
                                
                        "I think I'll call you \"sweetie\".":
                            $ RogueX.Pet = "sweetie"
                            if "boyfriend" in RogueX.Petnames or ApprovalCheck(RogueX, 500, "L"):
                                ch_r "Aw, that's sweet, [RogueX.Petname]."
                            else:     
                                $ RogueX.FaceChange("angry", 1)            
                                ch_r "That's a bit much, [RogueX.Petname]."
                                
                        "I think I'll call you \"sexy\".":
                            $ RogueX.Pet = "sexy"
                            if "lover" in RogueX.Petnames or ApprovalCheck(RogueX, 900):
                                $ RogueX.FaceChange("sexy", 1) 
                                ch_r "You're not so bad yourself, [RogueX.Petname]."
                            else:        
                                $ RogueX.FaceChange("angry", 1)         
                                ch_r "Inappropriate, [RogueX.Petname]."  
                                
                        "I think I'll call you \"lover\".":
                            $ RogueX.Pet = "lover"
                            if "lover" in RogueX.Petnames or ApprovalCheck(RogueX, 900):
                                $ RogueX.FaceChange("sexy", 1) 
                                ch_r "Oh, I love you too, [RogueX.Petname]."
                            else:      
                                $ RogueX.FaceChange("angry", 1)           
                                ch_r "Not any time soon, [RogueX.Petname]."   
                            
                        "Back":
                            pass
                
                "Risky":
                    menu:                        
                        "I think I'll call you \"slave\".":
                            $ RogueX.Pet = "slave"
                            if "master" in RogueX.Petnames or ApprovalCheck(RogueX, 700, "O"):
                                $ RogueX.FaceChange("bemused", 1) 
                                ch_r "As you wish, [RogueX.Petname]."
                            else:      
                                $ RogueX.FaceChange("angry", 1)           
                                ch_r "I ain't anyone's slave, [RogueX.Petname]."
                                                
                        "I think I'll call you \"pet\".":
                            $ RogueX.Pet = "pet"
                            if "master" in RogueX.Petnames or ApprovalCheck(RogueX, 600, "O"):
                                $ RogueX.FaceChange("bemused", 1) 
                                ch_r "Hmm, make sure to pet me, [RogueX.Petname]."
                            else:             
                                $ RogueX.FaceChange("angry", 1)    
                                ch_r "I ain't your pet, [RogueX.Petname]."
                                
                        "I think I'll call you \"slut\".":
                            $ RogueX.Pet = "slut"
                            if "sex friend" in RogueX.Petnames or ApprovalCheck(RogueX, 1000, "OI"):
                                $ RogueX.FaceChange("sexy") 
                                ch_r "You know me too well, [RogueX.Petname]."
                            else:                
                                $ RogueX.FaceChange("angry", 1) 
                                $ RogueX.Mouth = "surprised"
                                ch_r "Well I never!" 
                                
                        "I think I'll call you \"whore\".":
                            $ RogueX.Pet = "whore"
                            if "fuckbuddy" in RogueX.Petnames or ApprovalCheck(RogueX, 1100, "OI"):
                                $ RogueX.FaceChange("sly") 
                                ch_r "I guess I am. . ."
                            else:        
                                $ RogueX.FaceChange("angry", 1)         
                                ch_r "You look'in to start something, [RogueX.Petname]?" 
                                                       
                        "I think I'll call you \"sugartits\".":
                            $ RogueX.Pet = "sugartits"
                            if "sex friend" in RogueX.Petnames or ApprovalCheck(RogueX, 1500):
                                $ RogueX.FaceChange("sly", 1) 
                                ch_r "Heh."
                            else:     
                                $ RogueX.FaceChange("angry", 1)            
                                ch_r "Better not to my face, [RogueX.Petname]." 
                                
                        "I think I'll call you \"sex friend\".":
                            $ RogueX.Pet = "sex friend"
                            if "sex friend" in RogueX.Petnames or ApprovalCheck(RogueX, 600, "I"):
                                $ RogueX.FaceChange("sly") 
                                ch_r "Rreow. . ."
                            else:                
                                $ RogueX.FaceChange("angry", 1) 
                                ch_r "Hey, no need to advertise, [RogueX.Petname]." 
                                
                        "I think I'll call you \"fuckbuddy\".":
                            $ RogueX.Pet = "fuckbuddy"
                            if "fuckbuddy" in RogueX.Petnames or ApprovalCheck(RogueX, 700, "I"):
                                $ RogueX.FaceChange("sly") 
                                ch_r "That sounds about right, [RogueX.Petname]."
                            else:                
                                $ RogueX.FaceChange("angry", 1)
                                $ RogueX.Mouth = "surprised"
                                ch_r "Inappropriate, [RogueX.Petname]." 
                            
                        "I think I'll call you \"baby girl\".":
                            $ RogueX.Pet = "baby girl"
                            if "daddy" in RogueX.Petnames or ApprovalCheck(RogueX, 1200):
                                $ RogueX.FaceChange("smile", 1) 
                                ch_r "You know it, [RogueX.Petname]."
                            else:                
                                $ RogueX.FaceChange("angry", 1) 
                                ch_r "I ain't your baby girl, [RogueX.Petname]." 
                                
                        "Back":
                            pass
                        
                "Nevermind.":
                    return
        return
    
#label Rogue_Namecheck(Cnt = 0, Ugh = 0):#RogueX.Pet is the internal pet name, Cnt and Ugh are internal count variable defunct, remove, replaced with $ RogueX.NameCheck()
      
# start Rogue_Names//////////////////////////////////////////////////////////
label Rogue_Rename:  
        #Sets alternate names from Rogue
        $ RogueX.Mouth = "smile"
        ch_r "Yeah? What of it?"
        menu:
            extend ""
            "I guess \"Rogue\" suits you." if RogueX.Name != "Rogue":
                    $ RogueX.Name = "Rogue"
                    ch_r "You bet."
            "I liked the sound of \"Marie.\"" if RogueX.Name != "Marie" and "Marie" in RogueX.Names:
                    $ RogueX.Name = "Marie"
                    ch_r "Yeah, I could go by that again. . ."
            "I liked the sound of \"Anna.\"" if RogueX.Name != "Anna" and "Anna" in RogueX.Names:
                    $ RogueX.Name = "Anna"
                    ch_r "Yeah, I could go by that again. . ."
            "I liked the sound of \"Anna-Marie.\"" if RogueX.Name != "Anna-Marie" and "Anna-Marie" in RogueX.Names:
                    $ RogueX.Name = "Anna-Marie"
                    ch_r "Yeah, I could go by that again. . ."
            "Nevermind.":
                return
        return
# end Rogue_Names//////////////////////////////////////////////////////////

# start Rogue_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Rogue_Personality(Cnt = 0):   
        if not RogueX.Chat[4] or Cnt:
            "Since you're doing well in one area, you can convince [RogueX.Name] to focus on one of the others."
            "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
            "This will also impact which personality trait takes priority in dialog."
        menu:
            ch_r "Sure, what's up?"
            "More Obedient. [[Love to Obedience]" if RogueX.Love > 900:
                ch_p "If you really love me, could you please just do what I say?"
                ch_r "Well, I suppose for you I could be a bit more obedient."
                $ RogueX.Chat[4] = 1
            "Less Inhibited. [[Love to Inhibition]" if RogueX.Love > 900:
                ch_p "If you really love me, could lighten up a bit, just have some fun?"
                ch_r "Well, I suppose for you I could be a bit less inhibited."
                $ RogueX.Chat[4] = 2
            
            "Less Inhibited. [[Obedience to Inhibition]" if RogueX.Obed > 900:
                ch_p "I want you to be less inhibited."
                ch_r "Very well, I'll try to take more initiative."
                $ RogueX.Chat[4] = 3
            "More Loving. [[Obedience to Love]" if RogueX.Obed > 900:
                ch_p "I'd like you to learn to love me."
                ch_r "If I must, I'll try to come around."
                $ RogueX.Chat[4] = 4
                
            "More Obedient. [[Inhibition to Obedience]" if RogueX.Inbt > 900:
                ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
                ch_r "Well, I guess it can be fun to try what you want too. . ."
                $ RogueX.Chat[4] = 5
                
            "More Loving. [[Inhibition to Love]" if RogueX.Inbt > 900:
                ch_p "I know we're having fun, but do you even care about me?"
                ch_r "Well, I guess I am getting pretty attached. . ."
                $ RogueX.Chat[4] = 6
                
            "I guess just do what you like. . .[[reset]" if RogueX.Chat[4]:
                ch_p "You know what we talked about before? Nevermind that stuff."
                ch_r "Um, ok."
                $ RogueX.Chat[4] = 0
            "Repeat the rules":
                $ Cnt = 1
                jump Rogue_Personality
            "Nevermind.":
                return
        return
# end Rogue_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Rogue_Summon / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Rogue_Summon(Tempmod = Tempmod):
    $ RogueX.OutfitChange()        
    if "no summon" in RogueX.RecentActions:
            # If she's refused to follow you once recently
            if "angry" in RogueX.RecentActions:
                ch_r "What part of \"no\" don't you understand?"
            elif RogueX.RecentActions.count("no summon") > 1:
                ch_r "I already told you no, take a hint."
                $ RogueX.RecentActions.append("angry") 
            elif Current_Time == "Night": 
                ch_r "I told you it was too late for that tonight."
            else:
                ch_r "I told you I was busy."   
            $ RogueX.RecentActions.append("no summon")
            return
                        
    $ D20 = renpy.random.randint(1, 20) 
    $ Line = 0
    if RogueX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = -10
    elif RogueX.Loc == "bg dangerroom":    
        $ Tempmod = -20
    elif RogueX.Loc == "bg showerroom":    
        $ Tempmod = -40
        
    if D20 <= 3:                                                                        
        #unlucky refusal
        $ Line = "no"    
    elif "les" in RogueX.RecentActions:
            #if she's with another girl. . .
            if ApprovalCheck(RogueX, 2000):
                    ch_r "I'm enjoying some company right now, [RogueX.Petname], care to join us?"
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
                    $ RogueX.RecentActions.append("no summon") 
                    return  
    elif Current_Time == "Night": 
            if ApprovalCheck(RogueX, 700, "L") or ApprovalCheck(RogueX, 300, "O"):                              
                    #It's night time but she likes you.
                    ch_r "Ok, it's getting late but I can hang out for a bit."
                    $ RogueX.Loc = bg_current 
                    call Set_The_Scene
            else:                                                           
                    #It's night time and she isn't into you
                    ch_r "It's a bit late, [RogueX.Petname], maybe tomorrow."     
                    $ RogueX.RecentActions.append("no summon") 
            return            
    elif not ApprovalCheck(RogueX, 700, "L") or not ApprovalCheck(RogueX, 600, "O"):                       
        #It's not night time, but she's busy 
        if not ApprovalCheck(RogueX, 300):
                ch_r "Not really interested, [RogueX.Petname]."       
                $ RogueX.RecentActions.append("no summon") 
                return    
        
        
        if "summoned" in RogueX.RecentActions:
                pass              
        elif "goto" in RogueX.RecentActions:
                ch_r "You were just over here and then you took off. Why not just head back?"
        elif RogueX.Loc == "bg classroom":
                ch_r "I'm kinda in class right now, [RogueX.Petname], you could join me."
        elif RogueX.Loc == "bg dangerroom": 
                ch_r "I'm training at the moment, [RogueX.Petname], care to join me?"    
        elif RogueX.Loc == "bg campus": 
                ch_r "I'm hanging out on campus, [RogueX.Petname], want to hang with me?" 
        elif RogueX.Loc == "bg rogue": 
                ch_r "I'm in my room, [RogueX.Petname], want to swing by?" 
        elif RogueX.Loc == "bg player": 
                ch_r "I happen to be in your room, [RogueX.Petname], I'm waiting for you. . ."   
        elif RogueX.Loc == "bg showerroom":    
            if ApprovalCheck(RogueX, 1600):
                ch_r "I'm kinda in the shower right now, [RogueX.Petname], care to join me?"
            else:            
                ch_r "I'm kinda in the shower right now, [RogueX.Petname], maybe we could touch base later."      
                $ RogueX.RecentActions.append("no summon") 
                return    
        elif RogueX.Loc == "hold":
                ch_r "I'm not really around right now, see you later?"       
                $ RogueX.RecentActions.append("no summon") 
                return    
        else:
                #Unknown location
                ch_r "Why don't you come over here, [RogueX.Petname]?"    
            
        if "summoned" in RogueX.RecentActions:
            ch_r "Ok, fine, but why are you leading me on a merry chase?"           
            $ Line = "yes"
            
        elif "goto" in RogueX.RecentActions:
            menu:
                extend ""
                "You're right, be right back.":
                                ch_r "See you then!"
                                $ Line = "go to"                    
                "Nah, it's better here.":    
                                ch_r "Fine by me."                    
                "But I'd {i}really{/i} like to see you over here.":
                        if ApprovalCheck(RogueX, 600, "L") or ApprovalCheck(RogueX, 1400):
                                $ Line = "lonely"
                        else: 
                                $ Line = "no"                        
                "I said come over here.":
                        if ApprovalCheck(RogueX, 600, "O"):                                   
                                #she is obedient
                                $ Line = "command"                        
                        elif D20 >= 7 and ApprovalCheck(RogueX, 1400):                         
                                #she is generally favorable 
                                ch_r "I suppose I can, [RogueX.Petname]."              
                                $ Line = "yes"                        
                        elif ApprovalCheck(RogueX, 200, "O"):                                  
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
                        $ RogueX.Statup("Love", 55, 1) 
                        $ RogueX.Statup("Inbt", 30, 1)
                        ch_r "See you then!"
                        $ Line = "go to"
                    
                "Nah, we can talk later.":
                        $ RogueX.Statup("Obed", 50, 1)                            
                        $ RogueX.Statup("Obed", 30, 2)     
                        ch_r "Oh, ok. Talk to you later then."
                    
                "Could you please come visit me? I'm lonely.":
                        if ApprovalCheck(RogueX, 600, "L") or ApprovalCheck(RogueX, 1400):
                            $ RogueX.Statup("Love", 70, 1)                   
                            $ RogueX.Statup("Obed", 50, 1)
                            $ Line = "lonely"
                        else: 
                            $ RogueX.Statup("Inbt", 30, 1)
                            $ Line = "no"
                            
                "I said come over here.":
                        if ApprovalCheck(RogueX, 600, "O"):                              
                            #she is obedient
                            $ RogueX.Statup("Love", 50, 1, 1)    
                            $ RogueX.Statup("Love", 40, -1)                
                            $ RogueX.Statup("Obed", 90, 1)    
                            $ Line = "command"
                            
                        elif D20 >= 7 and ApprovalCheck(RogueX, 1400):       
                            #she is generally favorable
                            $ RogueX.Statup("Love", 70, -2)  
                            $ RogueX.Statup("Love", 90, -1)  
                            $ RogueX.Statup("Obed", 50, 2)                                
                            $ RogueX.Statup("Obed", 90, 1)  
                            ch_r "I suppose I can, [RogueX.Petname]."              
                            $ Line = "yes"
                            
                        elif ApprovalCheck(RogueX, 200, "O"):                                         
                            #she is not obedient   
                            $ RogueX.Statup("Love", 70, -4)  
                            $ RogueX.Statup("Love", 90, -2)   
                            ch_r "I don't know who you think you are, boss'in me around like that."                             
                            $ RogueX.Statup("Inbt", 40, 2)
                            $ RogueX.Statup("Inbt", 60, 1)    
                            $ RogueX.Statup("Obed", 70, -2)
                            ch_r "If you want to see me, you know where to find me."    
                        else:                                                                   
                            #she is obedient, but you failed to meet the checks
                            $ RogueX.Statup("Inbt", 30, 1)
                            $ RogueX.Statup("Inbt", 50, 1)                                    
                            $ RogueX.Statup("Love", 50, -1, 1)
                            $ RogueX.Statup("Obed", 70, -1)  
                            $ Line = "no" 
                        #end "ordered"
    else:                                                                               
        #automatic acceptance
        if RogueX.Love > RogueX.Obed:
                ch_r "I'd love to, [RogueX.Petname]."
        else:
                ch_r "Ok, I'll be right over, [RogueX.Petname]."
        $ Line = "yes" 
       
    $ Tempmod = 0
    
    if not Line:                                                                        
            #You end the dialog neutrally              
            $ RogueX.RecentActions.append("no summon") 
            return
    
    if Line == "no":                                                                    
            # She's refused, context based dialog
            if RogueX.Loc == "bg classroom":
                ch_r "I seriously can't, [RogueX.Petname], big test coming up." 
            elif RogueX.Loc == "bg dangerroom": 
                ch_r "Wish I could, [RogueX.Petname], but I need to get some hours in."
            else:
                ch_r "I'm sorry, [RogueX.Petname], but I'm kinda busy right now."  
            $ RogueX.RecentActions.append("no summon") 
            return
        
    elif Line == "go to":                                                                 
            #You agreed to go to her instead        
            $ renpy.pop_call()
            $ Tempmod = 0
            $ RogueX.RecentActions.append("goto") 
            $ Player.RecentActions.append("goto")  
            if RogueX.Loc == "bg classroom":
                    ch_r "See you then!"
                    jump Class_Room 
            elif RogueX.Loc == "bg dangerroom": 
                    ch_r "I'll be warming up!"
                    jump Danger_Room
            elif RogueX.Loc == "bg rogue": 
                    ch_r "I'll get tidied up."
                    jump Rogue_Room
            elif RogueX.Loc == "bg player": 
                    ch_r "I'll be waiting."
                    jump Player_Room                
            elif RogueX.Loc == "bg showerroom": 
                    ch_r "I guess I'll be here."
                    jump Shower_Room
            elif RogueX.Loc == "bg campus": 
                    ch_r "I'll keep an eye out for you."
                    jump Campus
            elif RogueX.Loc == "bg kitty": 
                    ch_r "I'll see you there."
                    jump Kitty_Room
            elif RogueX.Loc == "bg emma": 
                    ch_r "I'll see you there."
                    jump Emma_Room
            elif RogueX.Loc == "bg laura": 
                    ch_r "I'll see you there."
                    jump Laura_Room
            else:
                    ch_r "You know, I'll just meet you in my room."
                    $ RogueX.Loc = "bg rogue"
                    jump Rogue_Room
            
    #She's agreed to come over    
    elif Line == "lonely":
            ch_r "Oh, how could I say \"no\" to you, [RogueX.Petname]?"
    elif Line == "command": 
            ch_r "Fine, if you insist, [RogueX.Petname]."
    
    $ RogueX.RecentActions.append("summoned") 
    $ Line = 0
    ch_r "I'll be right over."  
    if "locked" in Player.Traits:
            call Locked_Door(RogueX)
            return           
    call Taboo_Level(0)                   
    $ RogueX.Loc = bg_current 
    call Set_The_Scene
    return

# End Rogue Summon / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Rogue Leave / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /   
label Rogue_Leave(Tempmod=Tempmod):  
        if "leaving" in RogueX.RecentActions:
            $ RogueX.DrainWord("leaving")   
        else:
            return
        
        if bg_current == "bg dangerroom":   
                call Gym_Clothes("exit")
                
        if RogueX.Loc == "hold":   
                # Activates if she's being moved out of play
                ch_r "I'm heading out for a while, see you later." 
                return
                
        if RogueX in Party or "lockedtravels" in RogueX.Traits: 
                #If she's in your party or if you've told her not to leave you
                #It resets her to your location
                $ RogueX.Loc = bg_current 
                return
          
        elif "freetravels" in RogueX.Traits or not ApprovalCheck(RogueX, 700):
                #If you've told her to go wherever, or she just doesn't care what you think.
                $ RogueX.OutfitChange(Changed=0)
                if not ApprovalCheck(RogueX, 600, "LO"):
                                ch_r "I'm headed out, see you later."
                elif RogueX.Loc == "bg classroom":
                                ch_r "I'm headed to class right now, [RogueX.Petname]."
                elif RogueX.Loc == "bg dangerroom": 
                                ch_r "I'm hitting the danger room, [RogueX.Petname]."   
                elif RogueX.Loc == "bg campus": 
                                ch_r "I'm going to hang out on campus, [RogueX.Petname]." 
                elif RogueX.Loc == "bg rogue": 
                                ch_r "I'm heading back to my room, [RogueX.Petname]." 
                elif RogueX.Loc == "bg player": 
                                ch_r "I'll be heading to your room, [RogueX.Petname]."   
                elif RogueX.Loc == "bg pool": 
                                ch_r "I'm headed for the pool."  
                elif RogueX.Loc == "bg showerroom":    
                            if ApprovalCheck(RogueX, 1400):
                                ch_r "I'm hitting the showers, later."
                            else:            
                                ch_r "I'm . . . headed out, see you later."                        
                else:        
                                ch_r "I'm headed out, see you later."
                hide Rogue_Sprite
                return     
                #End Free Travels
        
        $ RogueX.OutfitChange(Changed=0)  
        
        if "follow" not in RogueX.Traits:
                # Sets a key to show that she's asked you to follow her at least once
                $ RogueX.Traits.append("follow")   
            
        $ D20 = renpy.random.randint(1, 20) 
        $ Line = 0
        # Sets her preferences
        if RogueX.Loc == "bg classroom": #fix change these if changed function
            $ Tempmod = 10
        elif RogueX.Loc == "bg dangerroom":    
            $ Tempmod = 20
        elif RogueX.Loc == "bg showerroom":    
            $ Tempmod = 40

        
        if RogueX.Loc == "bg classroom":
                        ch_r "I'm headed to class right now, [RogueX.Petname], you could join me."
        elif RogueX.Loc == "bg dangerroom": 
                        ch_r "I'm hitting the danger room, [RogueX.Petname], care to join me?"    
        elif RogueX.Loc == "bg campus": 
                        ch_r "I'm going to hang out on campus, [RogueX.Petname], want to hang with me?" 
        elif RogueX.Loc == "bg rogue": 
                        ch_r "I'm heading back to my room, [RogueX.Petname], want to swing by?" 
        elif RogueX.Loc == "bg player": 
                        ch_r "I'll be heading to your room, [RogueX.Petname]."   
        elif RogueX.Loc == "bg showerroom":    
                    if ApprovalCheck(RogueX, 1600):
                        ch_r "I'm hitting the showers, [RogueX.Petname], care to join me?"
                    else:            
                        ch_r "I'm hitting the showers, [RogueX.Petname], maybe we could touch base later."
                        return                      
        elif RogueX.Loc == "bg pool": 
                        ch_r "I'm headed for the pool. Wanna come?"   
        else: #Location unknown        
                        ch_r "Why don't you come with me, [RogueX.Petname]?"    
        
        menu:
            extend ""
            "Sure, I'll catch up.":                  
                    if "followed" not in RogueX.RecentActions:
                        $ RogueX.Statup("Love", 55, 1) 
                        $ RogueX.Statup("Inbt", 30, 1)
                    $ Line = "go to"
                
            "Nah, we can talk later.":
                    if "followed" not in RogueX.RecentActions:
                        $ RogueX.Statup("Obed", 50, 1)                            
                        $ RogueX.Statup("Obed", 30, 2)
                    ch_r "Oh, ok. Talk to you later then."
                
            "Could you please stay with me? I'll get lonely.":
                    if ApprovalCheck(RogueX, 600, "L") or ApprovalCheck(RogueX, 1400):
                        if "followed" not in RogueX.RecentActions:
                            $ RogueX.Statup("Love", 70, 1)                   
                            $ RogueX.Statup("Obed", 50, 1)
                        $ Line = "lonely"
                    else: 
                        if "followed" not in RogueX.RecentActions:
                            $ RogueX.Statup("Inbt", 30, 1)
                        $ Line = "no"
                    
            "No, stay here.":
                    if ApprovalCheck(RogueX, 600, "O"):                              
                        #she is obedient
                        if "followed" not in RogueX.RecentActions:
                            $ RogueX.Statup("Love", 50, 1, 1)    
                            $ RogueX.Statup("Love", 40, -1)                
                            $ RogueX.Statup("Obed", 90, 1)    
                        $ Line = "command"
                        
                    elif D20 >= 7 and ApprovalCheck(RogueX, 1400):       
                        #she is generally favorable
                        if "followed" not in RogueX.RecentActions:
                            $ RogueX.Statup("Love", 70, -2)  
                            $ RogueX.Statup("Love", 90, -1)  
                            $ RogueX.Statup("Obed", 50, 2)                                
                            $ RogueX.Statup("Obed", 90, 1)  
                        ch_r "I suppose I can, [RogueX.Petname]."              
                        $ Line = "yes"
                        
                    elif ApprovalCheck(RogueX, 200, "O"):                                         
                        #she is not obedient   
                        if "followed" not in RogueX.RecentActions:
                            $ RogueX.Statup("Love", 70, -4)  
                            $ RogueX.Statup("Love", 90, -2)   
                        ch_r "I don't know who you think you are, boss'in me around like that." 
                        if "followed" not in RogueX.RecentActions:                           
                            $ RogueX.Statup("Inbt", 40, 2)
                            $ RogueX.Statup("Inbt", 60, 1)    
                            $ RogueX.Statup("Obed", 70, -2)
                        ch_r "If you want to see me, you know where to find me."                    
                    else:                                                                   
                        #she is obedient, but you failed to meet the checks
                        if "followed" not in RogueX.RecentActions:
                            $ RogueX.Statup("Inbt", 30, 1)
                            $ RogueX.Statup("Inbt", 50, 1)                                    
                            $ RogueX.Statup("Love", 50, -1, 1)
                            $ RogueX.Statup("Obed", 70, -1)  
                        $ Line = "no" 
                    #End ordered to stay
                    
        $ RogueX.RecentActions.append("followed")
        if not Line:                                                                        
                #You end the dialog neutrally
                hide Rogue_Sprite
                call Gym_Clothes("change", [RogueX])
                return
        
        if Line == "no":                                                                    
                # She's refused, context based dialog
                if RogueX.Loc == "bg classroom":
                    ch_r "I seriously can't, [RogueX.Petname], big test coming up." 
                elif RogueX.Loc == "bg dangerroom": 
                    ch_r "Wish I could, [RogueX.Petname], but I need to get some hours in."
                else:
                    ch_r "I'm sorry, [RogueX.Petname], but I'm kinda busy right now."      
                hide Rogue_Sprite
                call Gym_Clothes("change", [RogueX])      
                return
            
        elif Line == "go to":                                                                 
                #You agreed to go to her instead  
                $ Tempmod = 0
                call DrainAll("leaving")
                call DrainAll("arriving")            
                hide Rogue_Sprite
                call Gym_Clothes("change", [RogueX])
                if RogueX.Loc == "bg classroom":
                    ch_r "See you then!"            
                    jump Class_Room_Entry 
                elif RogueX.Loc == "bg dangerroom": 
                    ch_r "I'll be warming up!"         
                    jump Danger_Room_Entry
                elif RogueX.Loc == "bg rogue": 
                    ch_r "I'll meet you there."
                    jump Rogue_Room
                elif RogueX.Loc == "bg player": 
                    ch_r "I'll be waiting."
                    jump Player_Room                
                elif RogueX.Loc == "bg showerroom": 
                    ch_r "I guess I'll see you there."
                    jump Shower_Room_Entry
                elif RogueX.Loc == "bg campus": 
                    ch_r "Let's head over there."
                    jump Campus_Entry
                elif RogueX.Loc == "bg pool": 
                    ch_r "Let's head over there."
                    jump Pool_Entry
                else:
                    ch_r "You know, I'll just meet you in my room."
                    $ RogueX.Loc = "bg rogue"
                    jump Rogue_Room
                #End "goto" where she's at
                
        #She's agreed to come over    
        elif Line == "lonely":
                ch_r "Oh, how could I say \"no\" to you, [RogueX.Petname]?"
        elif Line == "command": 
                ch_r "Fine, if you insist, [RogueX.Petname]."
        
        $ Line = 0
        ch_r "I can stay for a bit."                                
        $ RogueX.Loc = bg_current 
        call Taboo_Level(0)
        return

# End Rogue Leave / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /   

#label Rogue_Dismissed(Leaving = 0):
#    if RogueX in Party:        
#            $ Party.remove(RogueX)
#    call Girls_Schedule(RogueX,0) #if RogueX.Loc == bg_current then it means she wants to stay here
#    if "leaving" in RogueX.RecentActions:
#            $ RogueX.DrainWord("leaving")   
#    menu:
#        "You can leave if you like.":
#                if RogueX.Loc == bg_current and not ApprovalCheck(RogueX, 700, "O"):
#                        ch_r "Thanks, but I think I'll stick around."
#                else:
#                        ch_r "Sure, ok. See you later."
#                        $ Leaving = 1           
#        "Could you give me the room please?":                            
#                if RogueX.Loc == bg_current and not ApprovalCheck(RogueX, 800, "LO"):
#                        ch_r "I'd rather stick around."
#                elif not ApprovalCheck(RogueX, 500, "LO"):
#                        ch_r "I think I should probably stick around."
#                else:
#                        if "dismissed" not in RogueX.DailyActions:
#                                $ RogueX.Statup("Obed", 30, 5)
#                                $ RogueX.Statup("Obed", 50, 5)
#                        ch_r "Not a problem, see you later then."   
#                        $ Leaving = 1                    
#        "You can go now.":                         
#                if RogueX.Loc == bg_current and not ApprovalCheck(RogueX, 500, "O"):
#                        ch_r "I think I'll stay."         
#                elif not ApprovalCheck(RogueX, 300, "O"):
#                        $ RogueX.FaceChange("confused") 
#                        ch_r "Well if you want me to go, then maybe I should stick around."
#                else:
#                        if "dismissed" not in RogueX.DailyActions:
#                                $ RogueX.Statup("Obed", 40, 10)
#                                $ RogueX.Statup("Obed", 60, 5)
#                        ch_r "If you wish."     
#                        $ Leaving = 1                  
#        "Nevermind.":
#                        return                             
    
#    if not Leaving and bg_current in ("bg campus","bg classroom","bg dangerroom"):
#            #if there is space nearby. . .
#            call Remove_Girl(RogueX,1,1)
#    elif not Leaving:     
#            menu:
#                extend ""
#                "I insist, get going.":  
#                        if RogueX.Loc != bg_current and (ApprovalCheck(RogueX, 1200, "LO") or ApprovalCheck(RogueX, 500, "O")):
#                                #If she has someplace to be and is obedient
#                                if "dismissed" not in RogueX.DailyActions:
#                                        $ RogueX.Statup("Love", 70, -5, 1)
#                                        $ RogueX.Statup("Obed", 50, 10)
#                                        $ RogueX.Statup("Obed", 80, 5)
#                                ch_r "Ok, if you insist." 
#                                $ Leaving = 1           
#                        elif RogueX.Loc != bg_current and (ApprovalCheck(RogueX, 1000, "LO") or ApprovalCheck(RogueX, 300, "O")):
#                                #If she has someplace to be and is less obedient
#                                if "dismissed" not in RogueX.DailyActions:
#                                        $ RogueX.Statup("Love", 50, -5, 1)
#                                        $ RogueX.Statup("Love", 70, -5, 1)
#                                        $ RogueX.Statup("Obed", 50, 10)
#                                        $ RogueX.Statup("Obed", 80, 5)
#                                $ RogueX.FaceChange("angry") 
#                                ch_r "Fine, if you're going to be a dick about it."
#                                $ Leaving = 1           
#                        elif RogueX.Loc != bg_current:
#                                #If she has someplace to be but is not obedient
#                                if "dismissed" not in RogueX.DailyActions:
#                                        $ RogueX.Statup("Love", 50, -5, 1)
#                                        $ RogueX.Statup("Love", 70, -10, 1)
#                                        $ RogueX.Statup("Obed", 50, -5)
#                                        $ RogueX.Statup("Inbt", 50, 5)
#                                        $ RogueX.Statup("Inbt", 80, 3)
#                                $ RogueX.FaceChange("angry") 
#                                ch_r "Like hell I will."   
#                        elif ApprovalCheck(RogueX, 1400, "LO") or ApprovalCheck(RogueX, 400, "O"):
#                                #If she has nowhere to be to be but is obedient
#                                if "dismissed" not in RogueX.DailyActions:
#                                        $ RogueX.Statup("Love", 50, -5, 1)
#                                        $ RogueX.Statup("Obed", 50, 10)
#                                        $ RogueX.Statup("Obed", 80, 5)
#                                $ RogueX.FaceChange("sad") 
#                                ch_r "Ok, if that's what you want."
#                                $ Leaving = 1           
#                        else:
#                                #If she has nowhere to be to be and is not obedient
#                                if "dismissed" not in RogueX.DailyActions:
#                                        $ RogueX.Statup("Love", 50, -5, 1)
#                                        $ RogueX.Statup("Love", 70, -10, 1)
#                                        $ RogueX.Statup("Obed", 50, -5)
#                                        $ RogueX.Statup("Inbt", 50, 3)
#                                        $ RogueX.Statup("Inbt", 80, 2)
#                                $ RogueX.FaceChange("sad") 
#                                ch_r "You wish."           
#                "Ok, nevermind.":
#                                pass               
                    
#    if "dismissed" not in RogueX.DailyActions:
#            $ RogueX.DailyActions.append("dismissed")  
#    if RogueX in Nearby:
#            "You shift a bit away from [RogueX.Name]"
#    elif Leaving == 0:
#            # Stay
#            $ RogueX.Loc = bg_current
#    else:
#            # Go
#            if RogueX.Loc != bg_current: #it stays the same
#                pass
#            elif bg_current == "bg rogue":
#                $ RogueX.Loc = "bg campus"
#            else:
#                $ RogueX.Loc = "bg rogue"
#            hide Rogue_Sprite
#            "[RogueX.Name] heads out." 
#    return
#    #end "you can leave"

# Rogue's Clothes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Rogue_Clothes:
    if RogueX.Taboo:
            if "exhibitionist" in RogueX.Traits:
                ch_r "Oooh, naughty. . ."  
            elif ApprovalCheck(RogueX, 900, TabM=4) or ApprovalCheck(RogueX, 400, "I", TabM=3): 
                ch_r "Well, I mean, it's pretty public here, but I guess I could. . ."
            else:
                ch_r "This is a pretty public place for that, don't you think?"
                ch_r "We can talk about that back in our rooms."
                return
    elif ApprovalCheck(RogueX, 900, TabM=4) or ApprovalCheck(RogueX, 600, "L") or ApprovalCheck(RogueX, 300, "O"):
                ch_r "Ok, what did you want?"
    else:
                ch_r "I'm not really interested in your fashion opinions."
                return
    if Girl != RogueX:
            #This culls returns if sent from another girl
            $ renpy.pop_call()     
    $ Girl = RogueX   
    call Shift_Focus(Girl)

label Rogue_Wardrobe_Menu: 
    while True:
        $ Trigger = 1 # to prevent Focus swapping. . .    
        $ RogueX.FaceChange()
        menu:
            ch_r "So what did you want to tell me about my clothes again?"
            "Overshirts":
                    call Rogue_Clothes_Over        
            "Legwear":
                    call Rogue_Clothes_Legs
            "Underwear":
                    call Rogue_Clothes_Under
            "Accessories":
                    call Rogue_Clothes_Misc
            "Outfit Management":
                    call Rogue_Clothes_Outfits  
            "Let's talk about what you wear around.":
                    call Clothes_Schedule(RogueX)
                               
            "Could I get a look at it?" if RogueX.Loc != bg_current:
                    # checks to see if she'll drop the screen
                    call OutfitShame(RogueX,0,2) 
                    if _return:                    
                        show PhoneSex zorder 150
                        ch_r "How's that? . ."
                    hide PhoneSex
            "Could I get a look at it?" if renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    call OutfitShame(RogueX,0,2) 
                    if _return:
                        hide DressScreen
                        
            "Would you be more comfortable behind a screen? (locked)" if RogueX.Taboo:
                    pass
            "Would you be more comfortable behind a screen?" if RogueX.Loc == bg_current and not RogueX.Taboo and not renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    if ApprovalCheck(RogueX, 1500) or (RogueX.SeenChest and RogueX.SeenPussy):
                            ch_r "Don't really need that, thanks."
                    else:
                            show DressScreen zorder 150
                            ch_r "This is more comfortable, thanks."
                            
            "Switch to. . .":
                    if renpy.showing('DressScreen'):
                            call OutfitShame(RogueX,0,2) 
                            if _return:
                                hide DressScreen
                            else:
                                $ RogueX.OutfitChange() 
                    $ RogueX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ Trigger = 0
                    call Switch_Chat
                    if Girl != RogueX:
                            ch_p "I wanted to talk about your clothes."
                            call expression Girl.Tag +"_Clothes"
                    $ Girl = RogueX
                    call Shift_Focus(Girl)
                            
            "Never mind, you look good like that. [[return]":            
                    if "wardrobe" not in RogueX.RecentActions:  
                            #Apply stat boosts only if it's the first time this turn
                            if RogueX.Chat[1] <= 1:                
                                    $ RogueX.Statup("Love", 70, 10)
                                    $ RogueX.Statup("Obed", 20, 10)
                                    ch_r "Aw, that's sweet."
                            elif RogueX.Chat[1] <= 10:
                                    $ RogueX.Statup("Love", 70, 5)
                                    $ RogueX.Statup("Obed", 20, 5)
                                    ch_r "Thanks." 
                            elif RogueX.Chat[1] <= 50:
                                    $ RogueX.Statup("Love", 70, 1)
                                    $ RogueX.Statup("Obed", 20, 1) 
                                    ch_r "Ok."
                            else:
                                    ch_r "Ok."
                            $ RogueX.RecentActions.append("wardrobe")  
                    if renpy.showing('DressScreen'):
                            call OutfitShame(RogueX,0,2) 
                            if _return:
                                hide DressScreen
                            else:
                                $ RogueX.OutfitChange() 
                    #sets up a temporary outfit
                    $ RogueX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ RogueX.Chat[1] += 1
                    $ Trigger = 0
                    return
        #Loops back up
#    jump Rogue_Wardrobe_Menu
    #End of Rogue Wardrobe Main Menu

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Rogue_Clothes_Outfits:                                                                               
        # Outfits
        "That looks really good on you, you should remember that one. [[Set Custom]":
                menu:
                    "Which slot would you like this saved in?"
                    "Custom 1":
                                call OutfitShame(RogueX,3,1)
                    "Custom 2":
                                call OutfitShame(RogueX,5,1)
                    "Custom 3":
                                call OutfitShame(RogueX,6,1)
                    "Gym Clothes":
                                call OutfitShame(RogueX,4,1)                    
                    "Sleepwear":
                                call OutfitShame(RogueX,7,1)                      
                    "Swimwear":
                                call OutfitShame(RogueX,10,1)   
                    "Never mind":
                                pass   
                                
        "I really like that green top and skirt outfit you have.":                  
                #Green
                $ RogueX.OutfitChange("casual1")   
                menu:
                    "You should wear this one out. [[set current outfit]":
                        $ RogueX.Outfit = "casual1"
                        $ RogueX.Shame = 0
                        ch_r "Ok, [RogueX.Petname], I like this one too."
                    "Let's try something else though.":
                        ch_r "Sure."            
                    
        "That pink top and pants look really nice on you.":                        
                #Pink  
                $ RogueX.OutfitChange("casual2")
                menu:
                    "You should wear this one out. [[set current outfit]":
                        $ RogueX.Outfit = "casual2"
                        $ RogueX.Shame = 0
                        ch_r "Sure, [RogueX.Petname], that one's nice."
                    "Let's try something else though.":
                        ch_r "Ok."            
                    
        "Remember that outfit we put together? [[Set a custom outfit] (locked)" if not RogueX.Custom1[0] and not RogueX.Custom2[0] and not RogueX.Custom3[0]:
                        pass       
                        
        "Remember that outfit we put together?" if RogueX.Custom1[0] or RogueX.Custom2[0] or RogueX.Custom3[0]: 
                        $ Cnt = 0
                        while 1:
                            menu:                
                                "Throw on Custom 1 (locked)" if not RogueX.Custom1[0]:
                                        pass
                                "Throw on Custom 1" if RogueX.Custom1[0]:
                                        $ RogueX.OutfitChange("custom1")
                                        $ Cnt = 3
                                "Throw on Custom 2 (locked)" if not RogueX.Custom2[0]:
                                        pass
                                "Throw on Custom 2" if RogueX.Custom2[0]:
                                        $ RogueX.OutfitChange("custom2")
                                        $ Cnt = 5
                                "Throw on Custom 3 (locked)" if not RogueX.Custom3[0]:
                                        pass
                                "Throw on Custom 3" if RogueX.Custom3[0]:
                                        $ RogueX.OutfitChange("custom3")
                                        $ Cnt = 6
                                
                                "You should wear this one in private. (locked)" if not Cnt:
                                        pass
                                "You should wear this one in private." if Cnt:
                                        if Cnt == 5:
                                            $ RogueX.Clothing[9] = "custom2"
                                        elif Cnt == 6:
                                            $ RogueX.Clothing[9] = "custom3"
                                        else:
                                            $ RogueX.Clothing[9] = "custom1"
                                        ch_r "Ok, sure."
                                
                                "On second thought, forget about that one outfit. . .":
                                        menu:
                                            ch_r "Which one did you mean?"
                                            "Custom 1 [[clear custom 1]" if RogueX.Custom1[0]:
                                                ch_r "Ok, no problem."
                                                $ RogueX.Custom1[0] = 0
                                            "Custom 1 [[clear custom 1] (locked)" if not RogueX.Custom1[0]:
                                                pass
                                            "Custom 2 [[clear custom 2]" if RogueX.Custom2[0]:
                                                ch_r "Ok, no problem."
                                                $ RogueX.Custom2[0] = 0
                                            "Custom 2 [[clear custom 2] (locked)" if not RogueX.Custom2[0]:
                                                pass
                                            "Custom 3 [[clear custom 3]" if RogueX.Custom3[0]:
                                                ch_r "Ok, no problem."
                                                $ RogueX.Custom3[0] = 0
                                            "Custom 3 [[clear custom 3] (locked)" if not RogueX.Custom3[0]:
                                                pass
                                            "Never mind, [[back].":
                                                pass            
                                        
                                "You should wear this one out. [[choose outfit first](locked)" if not Cnt:
                                                pass
                                "You should wear this one out." if Cnt:
                                                call Custom_Out(RogueX,Cnt)
                                "Ok, back to what we were talking about. . .":
                                                $ Cnt = 0
                                                return
                                                #jump Rogue_Clothes                               
        
        "Gym Clothes?" if not RogueX.Taboo or bg_current == "bg dangerroom":
                $ RogueX.OutfitChange("gym")
                
        "Sleepwear?" if not RogueX.Taboo:
                if ApprovalCheck(RogueX, 1200):
                        $ RogueX.OutfitChange("sleep")
                else:
                        call Display_DressScreen(RogueX)
                        if _return:
                            $ RogueX.OutfitChange("sleep")
                                     
        "Swimwear? (locked)" if (RogueX.Taboo and bg_current != "bg pool") or not RogueX.Swim[0]:
                $ RogueX.OutfitChange("swimwear")   
        "Swimwear?" if (not RogueX.Taboo or bg_current == "bg pool") and RogueX.Swim[0]:
                $ RogueX.OutfitChange("swimwear")
                            
        "Your birthday suit looks really great. . .":                                 
                #Nude
                $ RogueX.FaceChange("sexy", 1)
                $ Line = 0                        
                if not RogueX.Chest and not RogueX.Panties and not RogueX.Over and not RogueX.Legs and not RogueX.Hose:                
                        ch_r "Can't get much more naked than this."  
                elif RogueX.SeenChest and RogueX.SeenPussy and ApprovalCheck(RogueX, 1000, TabM=5):
                        ch_r "Naughty boy. . ."  
                        $ Line = 1
                elif ApprovalCheck(RogueX, 2000, TabM=5):
                        ch_r "Hmm. . . you move fast, but I suppose for you. . ."    
                        $ Line = 1
                elif RogueX.SeenChest and RogueX.SeenPussy and ApprovalCheck(RogueX, 1000, TabM=0):
                        ch_r "Well, maybe if it weren't quite so. . . public here."  
                elif ApprovalCheck(RogueX, 2000, TabM=0):
                        ch_r "I might consider it if we had some privacy. . ."  
                elif ApprovalCheck(RogueX, 1000, TabM=0):                
                        $ RogueX.FaceChange("surprised", 1)
                        ch_r "Hmm. . . you're getting a bit ahead of yourself, [RogueX.Petname]."
                else:
                        $ RogueX.FaceChange("angry", 1)
                        ch_r "What sort of common strumpet do you take me for?"  
                    
                if Line:                                                            #If she got nude. . .                            
                        $ RogueX.OutfitChange("nude")
                        "She pulls all her clothes off and throws them in a heap on the floor."
                        call Rogue_First_Topless
                        call Rogue_First_Bottomless(1)
                        $ RogueX.FaceChange("sexy")
                        menu:
                            "You know, you should wear this one out. [[set current outfit]":
                                if "exhibitionist" in RogueX.Traits:
                                        ch_r "You sure know how to rev my engines. . ." 
                                        $ RogueX.Outfit = "nude"
                                        $ RogueX.Shame = 50
                                elif ApprovalCheck(RogueX, 750, "I") or ApprovalCheck(RogueX, 2500, TabM=0):                    
                                        ch_r "Heh, all right [RogueX.Petname]."
                                        $ RogueX.Outfit = "nude"
                                        $ RogueX.Shame = 50
                                else:
                                        $ RogueX.FaceChange("sexy", 1)
                                        $ RogueX.Eyes = "surprised"
                                        ch_r "I'm afraid not, [RogueX.Petname], this is just for between you and me." 
                            "Let's try something else though.":
                                if "exhibitionist" in RogueX.Traits:
                                        ch_r "Hmm, too bad you didn't want me to wear this out. . ."                         
                                elif ApprovalCheck(RogueX, 750, "I") or ApprovalCheck(RogueX, 2500, TabM=0):       
                                        $ RogueX.FaceChange("bemused", 1)             
                                        ch_r "You know, for a second there I thought you might want me to wear this out. . ."
                                        ch_r "Hehe, um. . ."
                                else:
                                        $ RogueX.FaceChange("confused", 1)
                                        ch_r "Well obviously. It's not like I'd ever go out like this."   
                $ Line = 0
                
        "Never mind":    
                        return
                        #jump Rogue_Clothes     
    return        
    #jump Rogue_Clothes
    #End of Rogue Outfits

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Rogue_Clothes_Over:                                                                                         
        # Overshirts    
        "Why don't you go with no [RogueX.Over]?" if RogueX.Over:
                $ RogueX.FaceChange("bemused", 1)
                if RogueX.Chest or (RogueX.SeenChest and ApprovalCheck(RogueX, 600)):
                    ch_r "Sure."
                elif ApprovalCheck(RogueX, 600, TabM=0):
                    call Rogue_NoBra
                    if not _return:
                            if not ApprovalCheck(RogueX, 1200):
                                call Display_DressScreen(RogueX)
                                if not _return:
                                    return
                                    #jump Rogue_Clothes
                            else:
                                    return
                                    #jump Rogue_Clothes
                else:
                    call Display_DressScreen(RogueX)
                    if not _return:
                            ch_r "I'd rather not. . ."
                            if not RogueX.Chest:
                                    ch_r "I'm afraid I don't have anything on under this."
                            return
                            #jump Rogue_Clothes
                $ RogueX.Over = 0
                if not RogueX.Chest and not renpy.showing('DressScreen'):
                            call Rogue_First_Topless
                        
        "Try on the green mesh top." if RogueX.Over != "mesh top":
                $ RogueX.FaceChange("bemused", 1)
                if RogueX.Chest or (RogueX.SeenChest and ApprovalCheck(RogueX, 500, TabM=2)):
                    ch_r "Sure."  
                elif ApprovalCheck(RogueX, 600, TabM=0):
                    call Rogue_NoBra
                    if not _return:
                        if not ApprovalCheck(RogueX, 1200):
                            call Display_DressScreen(RogueX)
                            if not _return:
                                return  #jump Rogue_Clothes
                        else:
                                return  #jump Rogue_Clothes
                else:
                    call Display_DressScreen(RogueX)
                    if not _return:
                            ch_r "I'm afraid that top is a bit sheer to have nothing under it."
                            if not RogueX.Chest:
                                ch_r "I don't have anything on under this."
                            return  #jump Rogue_Clothes
                            
                $ RogueX.Over = "mesh top"    
                menu:
                    ch_r "With the collar?"
                    "Yes":
                        $ RogueX.Neck = "spiked collar"
                    "No":
                        $ RogueX.Neck = 0
                if RogueX.Chest == "buttoned tank":
                    $ RogueX.Chest = "tank"   
                if not RogueX.Chest and not renpy.showing('DressScreen'):
                    call Rogue_First_Topless 
                            
        "How about that pink top?" if RogueX.Over != "pink top":
                $ RogueX.Over = "pink top"  
                $ RogueX.Neck = 0
                        
        "How about that green hoodie?" if RogueX.Over != "hoodie":
                $ RogueX.Over = "hoodie"  
                        
        "Maybe just throw on a towel?" if RogueX.Over != "towel":
                $ RogueX.FaceChange("bemused", 1)
                if RogueX.Chest or RogueX.SeenChest:
                    ch_r "Fresh."
                elif ApprovalCheck(RogueX, 900, TabM=0):
                    $ RogueX.FaceChange("perplexed", 1)
                    ch_r "I suppose? . ."          
                else:
                    call Display_DressScreen(RogueX)
                    if not _return:
                            ch_r "That don't leave much to the imagination. . ."
                            return  #jump Rogue_Clothes
                $ RogueX.Over = "towel"  
            
        "How about that green nighty I got you?" if RogueX.Over != "nighty" and "nighty" in RogueX.Inventory:
                if RogueX.Legs:
                        ch_r "I can't really wear that with my [RogueX.Legs] on."
                elif not ApprovalCheck(RogueX, 1100, TabM=3):                    
                        call Display_DressScreen(RogueX)
                        if not _return:
                                ch_r "That's a bit . . . revealing."
                                return  #jump Rogue_Clothes      
                else:
                        ch_r "Sure. . ."
                if "lace bra" in RogueX.Inventory:
                    $ RogueX.Chest = "lace bra"
                else:
                    $ RogueX.Chest = "bra"
                if "lace panties" in RogueX.Inventory:
                    $ RogueX.Panties = "lace panties"
                else:
                    $ RogueX.Panties = "black panties"
                $ RogueX.Over = "nighty"   
                menu:
                    extend ""
                    "Nice.":
                        pass
                    "I meant {i}just{/i} the nighty.":
                        if ApprovalCheck(RogueX, 1400, TabM=3):
                            "She shrugs off her bra and then pulls the nighty back up."
                            $ RogueX.Panties = 0
                            $ RogueX.Chest = 0
                            ch_r "Hmmm, alright. . ."
                        elif ApprovalCheck(RogueX, 1200, TabM=3):
                            $ RogueX.Chest = 0
                            ch_r "I'll keep my panties on, thanks."
                        else:
                            ch_r "Be happy with what you get."
                if not RogueX.Chest and not renpy.showing('DressScreen'):
                    call Rogue_First_Topless
                
        "Never mind":
            pass           
    return  #jump Rogue_Clothes
    #End of Rogue Top
                       
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    label Rogue_NoBra:
        menu:
            ch_r "I don't have anything under this. . ."
            "Then you could slip something on under it. . .":   
                        if RogueX.SeenChest and ApprovalCheck(RogueX, 1000, TabM=3) or ApprovalCheck(RogueX, 1200, TabM=4):
                                $ RogueX.Blush = 2
                                ch_r "'course, I don't exactly need something under it either. . ."
                                $ RogueX.Blush = 1                
                        elif ApprovalCheck(RogueX, 900, TabM=2) and "lace bra" in RogueX.Inventory:
                                ch_r "I suppose this would work. . ."
                                $ RogueX.Chest  = "lace bra"    
                                "She pulls out her lace bra and slips it on under her [RogueX.Over]."
                        elif ApprovalCheck(RogueX, 800, TabM=2):
                                ch_r "Yeah, I guess."
                                $ RogueX.Chest = "bra"
                                "She pulls out her bra and slips it on under her [RogueX.Over]."
                        elif ApprovalCheck(RogueX, 600, TabM=2):
                                ch_r "Yeah, I guess."
                                $ RogueX.Chest = "tank"
                                "She pulls out her tanktop and slips it on under her [RogueX.Over]."
                        else:
                                ch_r "Yeah, I don't think so."
                                return 0
                        
            "You could always just wear nothing at all. . .":
                        if ApprovalCheck(RogueX, 1100, "LI", TabM=2) and RogueX.Love > RogueX.Inbt:               
                                ch_r "I suppose I could. . ."
                        elif ApprovalCheck(RogueX, 700, "OI", TabM=2) and RogueX.Obed > RogueX.Inbt:
                                ch_r "Sure. . ."
                        elif ApprovalCheck(RogueX, 600, "I", TabM=2):
                                ch_r "Yeah. . ."
                        elif ApprovalCheck(RogueX, 1300, TabM=2):
                                ch_r "Okay, fine."
                        else: 
                                $ RogueX.FaceChange("surprised")
                                $ RogueX.Brows = "angry"
                                if RogueX.Taboo > 20:
                                    ch_r "Not in public, [RogueX.Petname]!"
                                else:
                                    ch_r "Don't push it, [RogueX.Petname]."
                                return 0
                    
            "Never mind.":
                        ch_r "Ok. . ."
                        return 0
        return 1
        #End of Rogue bra check
       
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<                      
                       
    menu Rogue_Clothes_Legs:                                                                                                   
        # Leggings   
        "Maybe go without the [RogueX.Legs]." if RogueX.Legs:
                $ RogueX.FaceChange("sexy", 1)
                if RogueX.SeenPanties and RogueX.Panties and ApprovalCheck(RogueX, 500, TabM=5):
                        ch_r "Sure."
                elif RogueX.SeenPussy and ApprovalCheck(RogueX, 900, TabM=4):
                        ch_r "Sure, why not?"             
                elif ApprovalCheck(RogueX, 1300, TabM=2) and RogueX.Panties:
                        ch_r "Well, I suppose if it's for you. . ."                         
                elif ApprovalCheck(RogueX, 700) and not RogueX.Panties:
                        call Rogue_NoPantiesOn
                        if not _return and not RogueX.Panties:
                            if not ApprovalCheck(RogueX, 1500):
                                call Display_DressScreen(RogueX)
                                if not _return:
                                    return  #jump Rogue_Clothes
                            else:
                                    return  #jump Rogue_Clothes
                else:
                        call Display_DressScreen(RogueX)
                        if not _return:
                            ch_r "Not in front of you, [RogueX.Petname]."
                            if not RogueX.Panties:
                                ch_r "Maybe if I put some panties on first. . ."
                            return  #jump Rogue_Clothes
                if RogueX.PantsNum() > 6:
                        $ RogueX.Legs = 0    
                        "She tugs her pants off and drops them to the ground."
                else:
                        $ RogueX.Legs = 0    
                        "She tugs her skirt off and drops it to the ground."
                if renpy.showing('DressScreen'):
                    pass
                elif RogueX.Panties:                
                    $ RogueX.SeenPanties = 1
                else:
                    call Rogue_First_Bottomless
                                                    
        "How about that skirt?" if RogueX.Legs != "skirt":  
                $ RogueX.Legs = "skirt"
                $ RogueX.Upskirt = 0
                                            
        "Your ass looks tight in those jeans." if RogueX.Legs != "pants":
                $ RogueX.Legs = "pants"
                $ RogueX.Hose = 0
                
        "The tights would look good with that." if RogueX.Hose != 'tights' and RogueX.Legs != "pants":     
                $ RogueX.Hose = "tights"                   
        "Your ripped tights would look good with that." if RogueX.Hose != 'ripped tights' and "ripped tights" in RogueX.Inventory and RogueX.Legs != "pants":     
                $ RogueX.Hose = "ripped tights"           
        "You could lose the tights." if RogueX.Hose == 'ripped tights' or RogueX.Hose == 'tights':     
                $ RogueX.Hose = 0  
            
        "What about wearing your shorts?" if RogueX.Panties != "shorts":
                ch_r "Alright."
                $ RogueX.Panties = "shorts"            
        "Why don't you lose the shorts?" if RogueX.Panties == "shorts":
                $ RogueX.FaceChange("sexy", 1)
                if RogueX.SeenPanties and RogueX.Panties and ApprovalCheck(RogueX, 500, TabM=5):
                    ch_r "Sure."
                elif RogueX.SeenPussy and ApprovalCheck(RogueX, 900, TabM=4):
                    ch_r "Sure, why not?"             
                elif ApprovalCheck(RogueX, 1300, TabM=2) and RogueX.Panties:
                    ch_r "Well, I suppose if it's for you. . ."   
                elif ApprovalCheck(RogueX, 700) and not RogueX.Panties:
                    call Rogue_NoPantiesOn
                    if not _return and not RogueX.Panties:
                        if not ApprovalCheck(RogueX, 1500):
                            call Display_DressScreen(RogueX)
                            if not _return:
                                return  #jump Rogue_Clothes
                        else:
                                return  #jump Rogue_Clothes
                else:
                    call Display_DressScreen(RogueX)
                    if not _return:
                        ch_r "Not in front of you, [RogueX.Petname]."
                        if not RogueX.Panties:
                            ch_r "Maybe if I put some panties on first. . ."
                        return  #jump Rogue_Clothes
                if RogueX.Panties == "shorts":
                        $ RogueX.Panties = 0
                "She tugs her shorts off and drops them to the ground."
                if renpy.showing('DressScreen'):
                    pass
                elif RogueX.Panties:                
                    $ RogueX.SeenPanties = 1
                else:
                    call Rogue_First_Bottomless
                    
        "Never mind":
            pass
    return  #jump Rogue_Clothes
    #End of Rogue Pants
   
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
    
    label Rogue_NoPantiesOn:
        menu:
            ch_r "I'm not wearing anything under these, you know. . ."
            "Then you could slip on a pair of panties. . .":   
                        if RogueX.SeenPussy and ApprovalCheck(RogueX, 1100, TabM=4):
                                $ RogueX.Blush = 1
                                ch_r "Alright."       
                                $ RogueX.Blush = 0                        
                        elif ApprovalCheck(RogueX, 1500, TabM=4):
                                $ RogueX.Blush = 1
                                ch_r "Alright."       
                                $ RogueX.Blush = 0                
                        elif ApprovalCheck(RogueX, 800, TabM=4) and "lace panties" in RogueX.Inventory:
                                ch_r "I like how you think."
                                $ RogueX.Panties  = "lace panties"  
                                if ApprovalCheck(RogueX, 1200, TabM=4) and RogueX.Legs:   
                                        $ Line = RogueX.Legs
                                        $ RogueX.Legs = 0
                                        "She pulls off her [Line] and slips on the lace panties."                                    
                                elif RogueX.Legs == "skirt":
                                        "She pulls out her lace panties and pulls them up under her skirt."
                                        $ RogueX.Legs = 0
                                        "Then she drops the skirt to the floor."
                                else:
                                        $ Line = RogueX.Legs
                                        $ RogueX.Legs = 0
                                        "She steps away a moment and then comes back wearing only the lace panties."                                     
                                return  #jump Rogue_Clothes
                        elif ApprovalCheck(RogueX, 700, TabM=4):
                                ch_r "Yeah, I guess."
                                $ RogueX.Panties = "black panties"
                                if ApprovalCheck(RogueX, 1200, TabM=4) and RogueX.Legs:   
                                        $ Line = RogueX.Legs
                                        $ RogueX.Legs = 0
                                        "She pulls off her [Line] and slips on the black panties."                                    
                                elif RogueX.Legs == "skirt":
                                        "She pulls out her black panties and pulls them up under her skirt."
                                        $ RogueX.Legs = 0
                                        "Then she drops the skirt to the floor."
                                else:
                                        $ Line = RogueX.Legs
                                        $ RogueX.Legs = 0
                                        "She steps away a moment and then comes back wearing only the black panties."                                     
                                return  #jump Rogue_Clothes
                        else:
                                ch_r "Nope."
                                return 0
                        
            "You could always just wear nothing at all. . .":
                    if ApprovalCheck(RogueX, 1100, "LI", TabM=3) and RogueX.Love > RogueX.Inbt:               
                            ch_r "Well aren't you cheeky. . . I suppose I could give you a show. . ."
                    elif ApprovalCheck(RogueX, 750, "OI", TabM=3) and RogueX.Obed > RogueX.Inbt:
                            ch_r "If that's what you want."
                    elif ApprovalCheck(RogueX, 500, "I", TabM=3):
                            ch_r "Oooh, naughty."
                    elif ApprovalCheck(RogueX, 1400, TabM=3):
                            ch_r "Oh, fine. You've been a good boy."
                    else: 
                            $ RogueX.FaceChange("surprised")
                            $ RogueX.Brows = "angry"
                            if RogueX.Taboo:
                                ch_r "Not here,[RogueX.Petname]!"
                            else:
                                ch_r "Not with you around,[RogueX.Petname]!"
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
                    "How about you lose the [RogueX.Chest]?" if RogueX.Chest:
                            $ RogueX.FaceChange("bemused", 1)                        
                            if RogueX.SeenChest and ApprovalCheck(RogueX, 1100, TabM=2):
                                ch_r "Sure."    
                            elif ApprovalCheck(RogueX, 1100, TabM=2):
                                ch_r "I guess I don't really mind if you see them. . ."
                            elif RogueX.Over == "hoodie" and ApprovalCheck(RogueX, 500, TabM=2):
                                ch_r "I guess this covers enough. . ."  
                            elif not RogueX.SeenChest and not ApprovalCheck(RogueX, 1100):
                                    call Display_DressScreen(RogueX)
                                    if not _return:
                                        if RogueX.Over == "pink top" and ApprovalCheck(RogueX, 950, TabM=2):
                                                ch_r "This look is a bit revealing. . ."  
                                        elif RogueX.Over == "mesh top":
                                                ch_r "In this top? That would leave nothing to the imagination!" 
                                        elif not RogueX.Over:
                                                ch_r "Not without a little coverage, for modesty."
                                        else:
                                                ch_r "I don't think so, [RogueX.Petname]."
                                        return  #jump Rogue_Clothes 
                            $ Line = RogueX.Chest
                            $ RogueX.Chest = 0
                            if RogueX.Over:
                                "She reaches into her [RogueX.Over] grabs her [Line], and pulls it out, dropping it to the ground."
                            else:
                                "She lets her [Line] fall to the ground."
                            if (not RogueX.Over or RogueX.Over == "mesh top") and not renpy.showing('DressScreen'):
                                call Rogue_First_Topless

                    "Try on that black tank top." if RogueX.Chest != "tank":
                            $ RogueX.Chest = "tank"            
                    "I like that buttoned tank top." if RogueX.Chest != "buttoned tank" and RogueX.Over != "mesh top":
                            $ RogueX.Chest = "buttoned tank"  
                        
                    "I like that sports bra." if RogueX.Chest != "sports bra":
                            if (RogueX.SeenChest and ApprovalCheck(RogueX, 600)) or ApprovalCheck(RogueX, 900, TabM=2):
                                ch_r "Sure."   
                                $ RogueX.Chest = "sports bra"         
                            else:                
                                call Display_DressScreen(RogueX)
                                if not _return:
                                    ch_r "I don't know about wearing it with this. . ." 
                                    return  #jump Rogue_Clothes 
                                        
                    "I like that black bra." if RogueX.Chest != "bra":
                            if (RogueX.SeenChest and ApprovalCheck(RogueX, 600)) or ApprovalCheck(RogueX, 1100, TabM=2):
                                ch_r "Sure."   
                                $ RogueX.Chest = "bra"         
                            else:          
                                call Display_DressScreen(RogueX)
                                if not _return:
                                    ch_r "That's a bit too revealing. . ." 
                                    return  #jump Rogue_Clothes      
                                    
                    "I like that lace bra." if "lace bra" in RogueX.Inventory and RogueX.Chest != "lace bra":
                            if (RogueX.SeenChest and ApprovalCheck(RogueX, 800)) or ApprovalCheck(RogueX, 1100, TabM=2):
                                ch_r "Sure."   
                                $ RogueX.Chest = "lace bra"         
                            else:                
                                call Display_DressScreen(RogueX)
                                if not _return:
                                    ch_r "That's a bit too revealing. . ." 
                                    return  #jump Rogue_Clothes   
                    
                    "I like that bikini top." if RogueX.Chest != "bikini top" and "bikini top" in RogueX.Inventory:
                            if bg_current == "bg pool":
                                    ch_r "Sure."   
                                    $ RogueX.Chest = "bikini top"         
                            else:                
                                    if RogueX.SeenChest or ApprovalCheck(RogueX, 1000, TabM=2):
                                        ch_r "Sure."   
                                        $ RogueX.Chest = "bikini top"         
                                    else:             
                                        call Display_DressScreen(RogueX)
                                        if not _return:
                                            ch_r "I kinda don't feel right about that. . ." 
                                            return  #jump Rogue_Clothes       
                            
                    "Never mind":
                                pass
                jump Rogue_Clothes_Under
                                        
                                        
            "Hose and stockings options":
                menu:          
                    "You could lose the hose." if RogueX.Hose and RogueX.Hose != 'ripped tights' and RogueX.Hose != 'tights':     
                            $ RogueX.Hose = 0  
                    "The thigh-high hose would look good with that." if RogueX.Hose != "stockings" and RogueX.Legs != "pants":     
                            $ RogueX.Hose = "stockings"  
                    "The pantyhose would look good with that." if RogueX.Hose != "pantyhose" and RogueX.Legs != "pants":     
                            $ RogueX.Hose = "pantyhose" 
                    "The stockings would look good with that." if RogueX.Hose != "stockings and garterbelt" and "stockings and garterbelt" in RogueX.Inventory and RogueX.Legs != "pants":     
                            $ RogueX.Hose = "stockings and garterbelt"  
                    "Maybe just the garterbelt?" if RogueX.Hose != "garterbelt" and "stockings and garterbelt" in RogueX.Inventory and RogueX.Legs != "pants":     
                            $ RogueX.Hose = "garterbelt"  
                    "Your ripped pantyhose would look good with that." if RogueX.Hose != "ripped pantyhose" and "ripped pantyhose" in RogueX.Inventory and RogueX.Legs != "pants":     
                            $ RogueX.Hose = "ripped pantyhose"    
                    "Never mind":
                            pass  
                jump Rogue_Clothes_Under
            
            "Panties":
                menu:
                    
                    "You could lose those panties. . ." if RogueX.Panties and RogueX.Panties != "shorts":
                            $ RogueX.FaceChange("bemused", 1)
                            if (RogueX.SeenPussy and ApprovalCheck(RogueX, 900)) and not RogueX.Taboo: # You've seen her pussy
                                if ApprovalCheck(RogueX, 850, "L", TabM=2):               
                                    ch_r "Well aren't you cheeky. . ."
                                elif ApprovalCheck(RogueX, 500, "O", TabM=2):
                                    ch_r "Fine by me."
                                elif ApprovalCheck(RogueX, 350, "I", TabM=2):
                                    ch_r "Oooh, naughty."                            
                                else:
                                    ch_r "Oh, I guess I could."         
                            else:                       #You've never seen it
                                if ApprovalCheck(RogueX, 1100, "LI", TabM=2):               
                                    ch_r "Well aren't you cheeky. . . I suppose I could give you a show. . ."
                                elif ApprovalCheck(RogueX, 750, "OI", TabM=2):
                                    ch_r "If that's what you want."
                                elif ApprovalCheck(RogueX, 500, "I", TabM=2):
                                    ch_r "Oooh, naughty."
                                elif ApprovalCheck(RogueX, 1400, TabM=3):
                                    ch_r "Oh, fine. You've been a good boy."
                                else: 
                                    call Display_DressScreen(RogueX)
                                    if not _return:
                                        $ RogueX.FaceChange("surprised")
                                        $ RogueX.Brows = "angry" 
                                        if RogueX.Taboo > 20:
                                            ch_r "Not in public, [RogueX.Petname]!"
                                        else:
                                            ch_r "Not with you around,[RogueX.Petname]!"
                                        jump Rogue_Clothes
                            $ Line = RogueX.Panties
                            $ RogueX.Panties = 0  
                            if RogueX.Legs == "skirt":
                                "She reaches under her skirt and pulls her [Line] out, droping them to the ground." 
                            elif RogueX.Legs:
                                if renpy.showing('DressScreen') or ApprovalCheck(RogueX, 1400, TabM=3):
                                        "She pulls down her [RogueX.Legs], removes her [Line], and then pulls them back on."
                                else:
                                        "She steps away for a moment."
                            else:
                                "She pulls her [Line] off and drops them to the ground."
                            if not RogueX.Legs and not renpy.showing('DressScreen'):
                                call Rogue_First_Bottomless
                                $ RogueX.Statup("Inbt", 50, 2)  
                                    
                    "Why don't you wear the green panties instead?" if RogueX.Panties and RogueX.Panties != "green panties":
                            if ApprovalCheck(RogueX, 1000, TabM=3):
                                ch_r "Sure, ok."
                                $ RogueX.Panties = "green panties"  
                            elif RogueX.Panties == "shorts":
                                ch_r "Heh, no, I think I'll stick with these, thanks."
                            else:
                                call Display_DressScreen(RogueX)
                                if not _return:
                                    ch_r "I think I'll choose my own underwear, thank you."
                            
                    "Why don't you wear the black panties instead?" if RogueX.Panties and RogueX.Panties != "black panties":
                            if ApprovalCheck(RogueX, 1100, TabM=3):
                                ch_r "Sure."
                                $ RogueX.Panties = "black panties"
                            elif RogueX.Panties == "shorts":
                                ch_r "Heh, no, I think I'll stick with these, thanks."
                            else:
                                call Display_DressScreen(RogueX)
                                if not _return:
                                    ch_r "I don't see how that's any business of yours, [RogueX.Petname]."
                                        
                    "Why don't you wear the lace panties instead?" if "lace panties" in RogueX.Inventory and RogueX.Panties and RogueX.Panties != "lace panties":
                            if ApprovalCheck(RogueX, 1200, TabM=3):
                                ch_r "Sure."
                                $ RogueX.Panties = "lace panties"
                            elif RogueX.Panties == "shorts":
                                ch_r "Heh, no, I think I'll stick with these, thanks."
                            else:
                                call Display_DressScreen(RogueX)
                                if not _return:
                                    ch_r "I don't see how that's any business of yours, [RogueX.Petname]."
                                        
                    "I like those bikini bottoms." if RogueX.Panties != "bikini bottoms" and "bikini bottoms" in RogueX.Inventory:
                            if bg_current == "bg pool":
                                ch_r "Sure."   
                                $ RogueX.Panties = "bikini bottoms"         
                            else:                
                                if ApprovalCheck(RogueX, 1000, TabM=2):
                                    ch_r "Sure."   
                                    $ RogueX.Panties = "bikini bottoms"         
                                else:        
                                    call Display_DressScreen(RogueX)
                                    if not _return:        
                                        ch_r "I kinda don't feel right about that. . ."  
                    "You know, you could wear some panties with that. . ." if not RogueX.Panties:
                            $ RogueX.FaceChange("bemused", 1)
                            if RogueX.Legs and (RogueX.Love+RogueX.Obed) <= (1.5 * RogueX.Inbt):
                                $ RogueX.Mouth = "smile"
                                ch_r "No thanks, [RogueX.Petname]."
                                menu:
                                    "Fine by me":
                                        jump Rogue_Clothes
                                    "I insist, put some on.":
                                        if (RogueX.Love+RogueX.Obed) <= RogueX.Inbt:
                                            $ RogueX.FaceChange("angry")
                                            ch_r "Well too bad."
                                            jump Rogue_Clothes
                                        else:
                                            $ RogueX.FaceChange("sadside")
                                            ch_r "Well! Fine." 
                            menu:
                                extend ""
                                "How about the green ones?":
                                    ch_r "Sure, ok."
                                    $ RogueX.Panties = "green panties"
                                "How about the black ones?":
                                    ch_r "Alright."                
                                    $ RogueX.Panties  = "black panties"
                                "How about the lace ones?" if "lace panties" in RogueX.Inventory:
                                    ch_r "Alright."                
                                    $ RogueX.Panties  = "lace panties"
                                    
                    "Never mind":
                            pass
                jump Rogue_Clothes_Under
            "Never mind":
                            return
    return
    #end loop    
    #jump Rogue_Clothes
    #End of Rogue Underwear
    
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<    
            
    menu Rogue_Clothes_Misc:                                                                                                                    
        #Misc
        "Maybe dry out your hair." if RogueX.Hair == "wet":
                if ApprovalCheck(RogueX, 600):
                        ch_r "Ok."
                        $ RogueX.Hair = "evo"
                else:
                        ch_r "I kinda prefer this look."
                
        "You should go for that wet look with your hair." if RogueX.Hair != "wet":
                if ApprovalCheck(RogueX, 800):
                        ch_r "Hmm?"
                        $ RogueX.Hair = "wet"
                        "She wanders off for a minute and comes back."
                        ch_r "Like this?"
                else:
                        ch_r "Not really into that."
                    
        "You know, I like some nice hair down there. Maybe grow it out." if not RogueX.Pubes:
                if "pubes" in RogueX.Todo:
                        $ RogueX.FaceChange("bemused", 1)
                        ch_r "Yeah, I know, [RogueX.Petname]. It doesn't grow out overnight!"
                else:                
                        $ RogueX.FaceChange("bemused", 1)
                        $ Approval = ApprovalCheck(RogueX, 1150, TabM=0)
                        
                        if ApprovalCheck(RogueX, 850, "L", TabM=0) or (Approval and RogueX.Love > RogueX.Obed):               
                            ch_r "Well. . . if that's how you like it. . ."
                        elif ApprovalCheck(RogueX, 500, "O", TabM=0) or (Approval and RogueX.Obed > RogueX.Inbt):
                            ch_r "If that's what you want."
                        elif ApprovalCheck(RogueX, 500, "I", TabM=0) or Approval:
                            ch_r "Heh, I like a man knows what he wants, [RogueX.Petname]."
                        else: 
                            $ RogueX.FaceChange("surprised")
                            $ RogueX.Brows = "angry"
                            ch_r "Well I don't see how that's any of your business, [RogueX.Petname]."
                            return  #jump Rogue_Clothes
                        $ RogueX.Todo.append("pubes")
                        $ RogueX.PubeC = 6
        
        "I like it waxed clean down there." if RogueX.Pubes == 1:
                $ RogueX.FaceChange("bemused", 1)
                if "shave" in RogueX.Todo:
                        ch_r "I know, I'll get on that. Not right this second, obviously."
                else:
                        $ Approval = ApprovalCheck(RogueX, 1150, TabM=0)
                        if ApprovalCheck(RogueX, 850, "L", TabM=0) or (Approval and RogueX.Love > RogueX.Obed):             
                            ch_r "I can keep it tidy if you like. . ."
                        elif ApprovalCheck(RogueX, 500, "O", TabM=0) or (Approval and RogueX.Obed > RogueX.Inbt):
                            ch_r "I'll take care of it."
                        elif ApprovalCheck(RogueX, 500, "I", TabM=0) or Approval:
                            ch_r "You better earn it, [RogueX.Petname]."
                        else: 
                            $ RogueX.FaceChange("surprised")
                            $ RogueX.Brows = "angry"
                            ch_r "I don't see how that's any of your beeswax, [RogueX.Petname]."
                            return  #jump Rogue_Clothes
                        $ RogueX.Todo.append("shave")        
        "Piercings. [[See what she looks like without them first] (locked)" if not RogueX.SeenPussy and not RogueX.SeenChest:
                        pass
            
        "You know, you'd look really nice with some ring body piercings." if RogueX.Pierce != "ring" and (RogueX.SeenPussy or RogueX.SeenChest):             
                if "ring" in RogueX.Todo:
                    ch_r "Yeah, I know, I'll get to it."
                else:                    
                    $ RogueX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(RogueX, 1350, TabM=0)
                    if ApprovalCheck(RogueX, 950, "L", TabM=0) or (Approval and RogueX.Love > RogueX.Obed):   
                        ch_r "You really like those? Well, I suppose. . ."
                    elif ApprovalCheck(RogueX, 600, "O", TabM=0) or (Approval and RogueX.Obed > RogueX.Inbt):
                        ch_r "I'll go get that taken care of."
                    elif ApprovalCheck(RogueX, 600, "I", TabM=0) or Approval:
                        ch_r "I've always kind of liked the look of those. . ."
                    else: 
                        $ RogueX.FaceChange("surprised")
                        $ RogueX.Brows = "angry"
                        ch_r "I don't see how that's any of your beeswax, [RogueX.Petname]."
                        return  #jump Rogue_Clothes            
                    $ RogueX.Todo.append("ring")
        
        "You know, you'd look really nice with some barbell body piercings." if RogueX.Pierce != "barbell" and (RogueX.SeenPussy or RogueX.SeenChest):                
                if "barbell" in RogueX.Todo:
                    ch_r "Yeah, I know, I'll get to it."
                else:                    
                    $ RogueX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(RogueX, 1350, TabM=0)
                    if ApprovalCheck(RogueX, 900, "L", TabM=0) or (Approval and RogueX.Love > RogueX.Obed):   
                        ch_r "You really like those? Well, I suppose. . ."
                    elif ApprovalCheck(RogueX, 600, "O", TabM=0) or (Approval and RogueX.Obed > RogueX.Inbt):
                        ch_r "I'll go get that taken care of."
                    elif ApprovalCheck(RogueX, 600, "I", TabM=0) or Approval:
                        ch_r "I've always kind of liked the look of those. . ."
                    else: 
                        $ RogueX.FaceChange("surprised")
                        $ RogueX.Brows = "angry"
                        ch_r "I don't see how that's any of your beeswax, [RogueX.Petname]."
                        return  #jump Rogue_Clothes                
                    $ RogueX.Todo.append("barbell")
                    $ RogueX.Pierce = "barbell"
                        
        "You know, you'd look better without those piercings." if RogueX.Pierce:
                $ RogueX.FaceChange("bemused", 1)
                $ Approval = ApprovalCheck(RogueX, 1350, TabM=0)
                if ApprovalCheck(RogueX, 950, "L", TabM=0) or (Approval and RogueX.Love > RogueX.Obed):   
                    ch_r "You really think so? I guess I could lose them. . ."
                elif ApprovalCheck(RogueX, 600, "O", TabM=0) or (Approval and RogueX.Obed > RogueX.Inbt):
                    ch_r "I'll take them out then."
                elif ApprovalCheck(RogueX, 600, "I", TabM=0) or Approval:
                    ch_r "I guess I prefered not having them in. . ."                
                else: 
                    $ RogueX.FaceChange("surprised")
                    $ RogueX.Brows = "angry"
                    ch_r "I'll keep them, if you don't mind."
                    return  #jump Rogue_Clothes            
                $ RogueX.Pierce = 0 
                        
        "I like that spiked collar." if RogueX.Neck != "spiked collar":
                        $ RogueX.Neck = "spiked collar"
        "You could lose that spiked collar." if RogueX.Neck == "spiked collar":
                        $ RogueX.Neck = 0
                        
        "Throw the gloves on." if not RogueX.Arms:
                        $ RogueX.Arms = "gloves"
        "Take a little risk, no gloves." if RogueX.Arms:
                        $ RogueX.Arms = 0                        
                        
        "Never mind":
                pass    
    return
    #jump Rogue_Clothes
    #End of Rogue Misc Wardrobe
    
return

#End Rogue Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <