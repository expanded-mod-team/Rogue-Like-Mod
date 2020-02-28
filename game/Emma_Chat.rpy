﻿# star Emma chat interface

label Emma_Chat_Minimal:
    $ EmmaX.FaceChange()    
    call Shift_Focus(EmmaX)
    if EmmaX.Loc != bg_current:
                show Cellphone at SpriteLoc(EmmaX.SpriteLoc)
    else:
                hide Cellphone
    if "caught" in EmmaX.RecentActions:
                ch_e "I don't think we should be seen together, if you don't mind."
                return
    if "angry" in EmmaX.RecentActions:
                ch_e "I would not press my luck if I were you."
                return
    menu:
        ch_e "What was it you wished to discuss, [EmmaX.Petname]?"
        "Come on over." if EmmaX.Loc != bg_current:
                    ch_e "I don't think I should be visiting students at their whim."
                    ch_e "You know my office hours."
        "Ask [EmmaX.Name] to leave" if EmmaX.Loc == bg_current:
                    ch_e "I'll come and go as I see fit, thank you."        
        "Romance her":
                menu:
                    "Sex Menu" if EmmaX.Loc == bg_current:
                                ch_p "Did you want to fool around?"                  
                                ch_e "With a student? You should know better than that, [EmmaX.Petname]."   
                    "Date":
                                ch_p "Do you want to go on a date tonight?"
                                ch_e "Well that certainly doesn't seem appropriate."
                    "Gifts" if EmmaX.Loc == bg_current:
                                ch_p "I'd like to give you something."
                                ch_e "I'm not sure that would be appropriate at the moment."                        
                    "Back":
                                pass
        "Talk to her":
                menu:
                    "I just wanted to talk. . .":
                                call Emma_Chitchat
                    "Relationship status":   
                                ch_p "Could we talk about us?"
                                ch_e "I'm not sure that's an appropriate discussion at the moment."                        
                    "Could I get your number?" if EmmaX not in Digits:
                                if ApprovalCheck(EmmaX, 800, "LI"):
                                    ch_e "I don't see why not."
                                    $ Digits.append(EmmaX) 
                                elif ApprovalCheck(EmmaX, 500, "OI"):
                                    ch_e "Hmm. . . fine, hand me your phone."             
                                    $ Digits.append(EmmaX)
                                else:
                                    ch_e "I don't think it's appropriate to give my number out to a student like that."     
                    "Back":
                                pass                        
        "Change [EmmaX.Name]":
                    ch_p "Let's talk about you."
                    ch_e "I doubt that's any of your business."        
        "Party up" if EmmaX not in Party and EmmaX.Loc == bg_current:
                    ch_p "Could you follow me for a bit?"
                    ch_e "I don't think I should."                    
        "Disband party" if EmmaX in Party: 
                    ch_p "Ok, you can leave if you prefer."
                    $ Party.remove(EmmaX)                           
        "Never mind.":
                    if Current_Time == "Evening":
                            ch_e "Now if that will be all, please clear out of here."
                            $ EmmaX.FaceChange("bemused",2)
                            ch_e "I have some. . . business to attend to." 
                    else:
                            "She seems a bit reserved. Maybe you need something to break the ice."
                            "Maybe you should check in on her after classes are over and the students leave."
                    return
    jump Emma_Chat_Minimal


#Emma Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  

label Emma_Relationship:
    while True:
        menu:
            ch_e "What did you want to talk about?"                        
            "Do you want to be my girlfriend?" if "dating" not in EmmaX.Traits and "ex" not in EmmaX.Traits:
                    $ EmmaX.DailyActions.append("relationship")
                    if "asked boyfriend" in EmmaX.DailyActions and "angry" in EmmaX.DailyActions:
                            $ EmmaX.FaceChange("angry", 1)
                            ch_e "Pest."
                            return
                    elif "asked boyfriend" in EmmaX.DailyActions:
                            $ EmmaX.FaceChange("angry", 1)
                            ch_e "Not today, little fly."
                            return
                    elif EmmaX.Break[0]:
                            $ EmmaX.FaceChange("angry", 1)
                            ch_e "I don't share."
                            if Player.Harem:   
                                    $ EmmaX.DailyActions.append("asked boyfriend")
                                    return
                            else:
                                    ch_p "I'm not anymore."
                            
                    $ EmmaX.DailyActions.append("asked boyfriend")
                    
                    if Player.Harem and "EmmaYes" not in Player.Traits: 
                        if len(Player.Harem) >= 2:
                            ch_e "I doubt they would understand, [EmmaX.Petname]."
                        else:
                            ch_e "I doubt [Player.Harem[0].Name] would understand, [EmmaX.Petname]."
                        return
                          
                    if EmmaX.Event[5]:
                            $ EmmaX.FaceChange("bemused", 1)
                            ch_e "I believe I asked you first."
                    else:
                            $ EmmaX.FaceChange("surprised", 2)
                            ch_e "Don't you think that might be inappropriate, [EmmaX.Petname]. . ." 
                            $ EmmaX.FaceChange("smile", 1)
                    
                    call Emma_OtherWoman
                    
                    if EmmaX.Love >= 800:
                            $ EmmaX.FaceChange("surprised", 1)
                            $ EmmaX.Mouth = "smile"
                            $ EmmaX.Statup("Love", 200, 40)
                            ch_e "I suppose I've become accustomed to you. . ."
                            if "boyfriend" not in EmmaX.Petnames:
                                    $ EmmaX.Petnames.append("boyfriend")                
                            $ EmmaX.Traits.append("dating")                        
                            if "EmmaYes" in Player.Traits:       
                                    $ Player.Traits.remove("EmmaYes")
                                    $ Player.Harem.append(EmmaX)
                                    call Harem_Initiation
                            "[EmmaX.Name] draws you in and kisses you deeply."
                            $ EmmaX.FaceChange("kiss", 1) 
                            $ EmmaX.Kissed += 1
                    elif EmmaX.Obed >= 500:
                            $ EmmaX.FaceChange("perplexed")
                            ch_e "I don't believe \"dating\" would be the right term for it."    
                    elif EmmaX.Inbt >= 500:
                            $ EmmaX.FaceChange("smile")                
                            ch_e "I don't think we should be \"exclusive.\""      
                    else:
                            $ EmmaX.FaceChange("perplexed", 1)
                            ch_e "I really couldn't get serious about a student, [EmmaX.Petname]."
                                    
            "Do you want to get back together?" if "ex" in EmmaX.Traits:
                    $ EmmaX.DailyActions.append("relationship")
                    if "asked boyfriend" in EmmaX.DailyActions and "angry" in EmmaX.DailyActions:
                            $ EmmaX.FaceChange("angry", 1)
                            ch_e "Do I have to demonstrate how unlikely that is?"
                            return
                    elif "asked boyfriend" in EmmaX.DailyActions:
                            $ EmmaX.FaceChange("angry", 1)
                            ch_e "Now you're just embarrassing yourself."
                            return
                            
                    $ EmmaX.DailyActions.append("asked boyfriend")
                    
                    if Player.Harem and "EmmaYes" not in Player.Traits:
                            if len(Player.Harem) >= 2:
                                ch_e "I doubt they would understand, [EmmaX.Petname]."
                            else:
                                ch_e "I doubt [Player.Harem[0].Name] would understand, [EmmaX.Petname]."
                            return
                                    
                    $ Cnt = 0
                    call Emma_OtherWoman
                                            
                    if EmmaX.Love >= 800:
                            $ EmmaX.FaceChange("sly", 1)
                            $ EmmaX.Statup("Love", 90, 5)
                            ch_e "Try as I might, I can't stay mad at you."
                            if "boyfriend" not in EmmaX.Petnames:
                                        $ EmmaX.Petnames.append("boyfriend")                
                            $ EmmaX.Traits.append("dating")          
                            $ EmmaX.Traits.remove("ex")                 
                            if "EmmaYes" in Player.Traits:       
                                        $ Player.Traits.remove("EmmaYes")
                                        $ Player.Harem.append(EmmaX)
                                        call Harem_Initiation
                            "[EmmaX.Name] leans in and kisses you deeply."
                            $ EmmaX.FaceChange("kiss", 1) 
                            $ EmmaX.Kissed += 1
                    elif EmmaX.Love >= 600 and ApprovalCheck(EmmaX, 1500):
                            $ EmmaX.FaceChange("smile", 1)
                            $ EmmaX.Statup("Love", 90, 5)
                            ch_e "Hrm, very well."        
                            if "boyfriend" not in EmmaX.Petnames:
                                    $ EmmaX.Petnames.append("boyfriend")                
                            $ EmmaX.Traits.append("dating")             
                            $ EmmaX.Traits.remove("ex")         
                            if "EmmaYes" in Player.Traits:       
                                    $ Player.Traits.remove("EmmaYes")
                                    $ Player.Harem.append(EmmaX)
                                    call Harem_Initiation
                            $ EmmaX.FaceChange("kiss", 1) 
                            "[EmmaX.Name] gives you a quick kiss."
                            $ EmmaX.FaceChange("sly", 1) 
                            $ EmmaX.Kissed += 1
                    elif EmmaX.Obed >= 500:
                            $ EmmaX.FaceChange("sad")
                            ch_e "Let's keep things as they are, for now."   
                    elif EmmaX.Inbt >= 500:
                            $ EmmaX.FaceChange("perplexed")                
                            ch_e "No, \"casual\" works better for the time being."
                    else:
                            $ EmmaX.FaceChange("perplexed", 1)
                            ch_e "I can't be bothered with second chances."
                    
                    # End Back Together
             
            "I wanted to ask about [[another girl]" if EmmaX in Player.Harem:
                    menu:
                        "Have you reconsidered letting me date. . ."
                        "[RogueX.Name]" if RogueX not in Player.Harem:
                                call Poly_Start(RogueX,1)
                        "[KittyX.Name]" if KittyX not in Player.Harem and "met" in KittyX.History:
                                call Poly_Start(KittyX,1)
                        "[LauraX.Name]" if LauraX not in Player.Harem and "met" in LauraX.History:
                                call Poly_Start(LauraX,1)
                        "Never mind":
                                pass          
                                   
            "I think we should break up." if "dating" in EmmaX.Traits or EmmaX in Player.Harem:
                        if "breakup talk" in EmmaX.DailyActions:
                                ch_e "You must be joking. Again?"
                        else:
                                call Breakup(EmmaX)       
                
            "About that talk we had before. . .":
                menu:
                    "When you said you loved me. . ." if "lover" not in EmmaX.Traits and EmmaX.Event[6] >= 20:
                            call Emma_Love_Redux     
                    "You said you wanted me to be more in control?" if "sir" not in EmmaX.Petnames and "sir" in EmmaX.History:
                            if "asked sub" in EmmaX.DailyActions:
                                    ch_e "I did, you didn't."          
                            else:
                                    call Emma_Sub_Asked
                    "You said you wanted me to be your Master?" if "master" not in EmmaX.Petnames and "master" in EmmaX.History:
                            if "asked sub" in EmmaX.DailyActions:
                                    ch_e "I seem to recall something about that. . ."            
                            else:
                                    call Emma_Sub_Asked                      
                    "Never Mind":
                            pass                     
            "Never Mind":
                return
              
    return

label Emma_OtherWoman(Cnt = 0):
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    if not Player.Harem:
            return
    $ Cnt = int((EmmaX.GirlLikeCheck(Player.Harem[0]) - 500)/2)    
        
    $ EmmaX.FaceChange("perplexed")
    if len(Player.Harem) >= 2:
        ch_e "But you're with [Player.Harem[0].Name] right now, among others, apparently."
    else:    
        ch_e "But you're with [Player.Harem[0].Name] right now."
    menu: 
        extend ""
        "She said I can be with you too." if "EmmaYes" in Player.Traits:
                if ApprovalCheck(EmmaX, 1800, Bonus = Cnt):
                    $ EmmaX.FaceChange("smile", 1)
                    if EmmaX.Love >= EmmaX.Obed:
                            ch_e "I suppose you're worth sharing."
                    elif EmmaX.Obed >= EmmaX.Inbt:
                            ch_e "If she can share then I can."
                    else:
                            ch_e "Sure, why not."
                else:
                    $ EmmaX.FaceChange("angry", 1)
                    ch_e "I really don't care what that little slut does."  
                    $ renpy.pop_call()                                          
                    #This causes it to jump past the previous menu on the return
        
        "I could ask if she'd be ok with me dating you both." if "EmmaYes" not in Player.Traits:
                if ApprovalCheck(EmmaX, 1800, Bonus = Cnt):
                        $ EmmaX.FaceChange("smile", 1)
                        if EmmaX.Love >= EmmaX.Obed:
                            ch_e "I suppose you're worth sharing."
                        elif EmmaX.Obed >= EmmaX.Inbt:
                            ch_e "If she can share then I can."
                        else:
                            ch_e "Sure, why not."                       
                        ch_e "Go ask her, give me the night to think about it, and then come back tomorrow with her answer."
                else:
                        $ EmmaX.FaceChange("angry", 1)
                        ch_e "I really don't care what that little slut does."    
                $ renpy.pop_call()
        
        "What she doesn't know won't hurt her.":
                if not ApprovalCheck(EmmaX, 1800, Bonus = -Cnt): #checks if Emma likes you more than Rogue
                        $ EmmaX.FaceChange("angry", 1)
                        if not ApprovalCheck(EmmaX, 1800):
                                ch_e "I don't want you either."
                        else:
                                ch_e "I don't want to share you."                    
                        $ renpy.pop_call()                 
                else:
                        $ EmmaX.FaceChange("smile", 1)
                        if EmmaX.Love >= EmmaX.Obed:
                                ch_e "I suppose we could arrange something."
                        elif EmmaX.Obed >= EmmaX.Inbt:
                                ch_e "If you insist."
                        else:
                                ch_e "I don't see why not."
                        $ EmmaX.Traits.append("downlow")
                
        "I can break it off with her.":
                    $ EmmaX.FaceChange("sad")
                    ch_e "Then we can talk after you have."                                   
                    $ renpy.pop_call()
            
        "You're right, I was dumb to ask.":
                    $ EmmaX.FaceChange("sad")
                    ch_e "Obviously. . ."                    
                    $ renpy.pop_call()   
    return


label Emma_About(Check=0):
    if Check not in TotalGirls:
            ch_e "Who?"
            return
    ch_e "What do I think about her? Well. . ."
    if Check == RogueX:    
            if "poly Rogue" in EmmaX.Traits:  
                ch_e "As you're aware, we've shared a great deal. . ."    
            elif EmmaX.LikeRogue >= 900:
                ch_e "I do find her rather mesmerizing. . ."
            elif EmmaX.LikeRogue >= 800:
                ch_e "That accent certainly did grow on me. . ."    
            elif EmmaX.LikeRogue >= 700:
                ch_e "We've become quite close."
            elif EmmaX.LikeRogue >= 600:
                ch_e "I'm rather fond of her."
            elif EmmaX.LikeRogue >= 500:
                ch_e "She's an adequate student."
            elif EmmaX.LikeRogue >= 400:
                ch_e "She can be a bit of a handful."
            elif EmmaX.LikeRogue >= 300:
                ch_e "I can barely tollerate her disrespectful nature." 
            else:
                ch_e "That swamp rat? What about her?" 
    elif Check == KittyX:    
            if "poly Kitty" in EmmaX.Traits:  
                ch_e "As you're aware, we do get along quite well. . ."    
            elif EmmaX.LikeKitty >= 900:
                ch_e "She is rather. . . flexible. . ."
            elif EmmaX.LikeKitty >= 800:
                ch_e "She is rather adorable. . ."    
            elif EmmaX.LikeKitty >= 700:
                ch_e "She's something of a friend at this point."
            elif EmmaX.LikeKitty >= 600:
                ch_e "Once you get to know her, she's not bad."
            elif EmmaX.LikeKitty >= 500:
                ch_e "She's an adequate student."
            elif EmmaX.LikeKitty >= 400:
                ch_e "She can be a bit of a know it all."
            elif EmmaX.LikeKitty >= 300:
                ch_e "I can't stand her constant questions." 
            else:
                ch_e "That little bitch?"
    elif Check == LauraX:    
            if "poly Laura" in EmmaX.Traits:  
                ch_e "She is quite. . . energetic. . ."    
            elif EmmaX.LikeLaura >= 900:
                ch_e "She's very durable. . ."
            elif EmmaX.LikeLaura >= 800:
                ch_e "She has a rough quality that is quite exciting. . ."    
            elif EmmaX.LikeLaura >= 700:
                ch_e "She's something of a friend at this point."
            elif EmmaX.LikeLaura >= 600:
                ch_e "Once you get to know her, she's not bad."
            elif EmmaX.LikeLaura >= 500:
                ch_e "She's an adequate student."
            elif EmmaX.LikeLaura >= 400:
                ch_e "She is a bit rough around the edges"
            elif EmmaX.LikeLaura >= 300:
                ch_e "Yes, a bit feral, that one." 
            else:
                ch_e "I'd put her down myself if I didn't have responsibilites."          
    return
#End Emma_AboutRogue

label Emma_Monogamy:
        #called from Emma_Settings to ask her not to hook up wiht other girls    
        menu:
            "Could you not hook up with other girls?" if "mono" not in EmmaX.Traits:
                    if EmmaX.Thirst >= 50 and not ApprovalCheck(EmmaX, 1800, "LO", TabM=0):
                            #she's too thirsty
                            $ EmmaX.FaceChange("sly",1) 
                            if "mono" not in EmmaX.DailyActions:                                                         
                                    $ EmmaX.Statup("Obed", 90, -2) 
                            ch_e "You know, it's not like you leave me any alternatives. . ."
                            return
                    elif ApprovalCheck(EmmaX, 1300, "LO", TabM=0) and EmmaX.Love >= EmmaX.Obed:
                            #she cares
                            $ EmmaX.FaceChange("sly",1) 
                            if "mono" not in EmmaX.DailyActions:                                                         
                                    $ EmmaX.Statup("Love", 90, 1) 
                            ch_e "Jealousy is an adorable look on you. . ." 
                            ch_e "I suppose I could restain myself. . ."
                    elif ApprovalCheck(EmmaX, 750, "O", TabM=0):
                            #she is obedient
                            $ EmmaX.FaceChange("sly",1,Eyes="side") 
                            ch_e "If you insist. . ."
                    else:   
                            #she doesn't care
                            $ EmmaX.FaceChange("sly",1,Brows="confused") 
                            ch_e "I'm afraid my affairs are my own business." 
                            ch_e "Don't leave me wanting. . ." 
                            return                    
                    if "mono" not in EmmaX.DailyActions:                                                         
                            $ EmmaX.Statup("Obed", 90, 3) 
                    $ EmmaX.AnyWord(1,0,"mono") #Daily
                    $ EmmaX.Traits.append("mono")   
            "Don't hook up with other girls." if "mono" not in EmmaX.Traits:
                    if ApprovalCheck(EmmaX, 900, "O", TabM=0):
                            #she is obedient
                            $ EmmaX.FaceChange("sly",1,Eyes="side") 
                            ch_e "Oh very well."
                    elif EmmaX.Thirst >= 60 and not ApprovalCheck(EmmaX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ EmmaX.FaceChange("sly",1) 
                            if "mono" not in EmmaX.DailyActions:                                                         
                                    $ EmmaX.Statup("Obed", 90, -2) 
                            ch_e "You know, it's not like you leave me any alternatives. . ."
                            return
                    elif ApprovalCheck(EmmaX, 600, "O", TabM=0):
                            #she is obedient
                            $ EmmaX.FaceChange("sly",1,Eyes="side") 
                            ch_e "If I must. . ."
                    elif ApprovalCheck(EmmaX, 1500, "LO", TabM=0):
                            #she cares
                            $ EmmaX.FaceChange("sly",1) 
                            ch_e "You shouldn't take that tone with me." 
                            ch_e "But I suppose I could let it slide. . ."
                    else:   
                            #she doesn't care
                            $ EmmaX.FaceChange("sly",1,Brows="confused") 
                            ch_e "My affairs are my own business." 
                            return                   
                    if "mono" not in EmmaX.DailyActions:                                                         
                            $ EmmaX.Statup("Obed", 90, 3) 
                    $ EmmaX.AnyWord(1,0,"mono") #Daily
                    $ EmmaX.Traits.append("mono")   
            "It's ok if you hook up with other girls." if "mono" in EmmaX.Traits:
                    if ApprovalCheck(EmmaX, 700, "O", TabM=0):
                            $ EmmaX.FaceChange("sly",1,Eyes="side") 
                            ch_e "Of course."
                    elif ApprovalCheck(EmmaX, 800, "L", TabM=0):
                            $ EmmaX.FaceChange("sly",1) 
                            ch_e "Only if I find myself. . . available. . ." 
                    else:
                            $ EmmaX.FaceChange("sly",1,Brows="confused") 
                            if "mono" not in EmmaX.DailyActions:                                                         
                                    $ EmmaX.Statup("Love", 90, -2)
                            ch_e "I wasn't aware that I needed your permission." 
                    if "mono" not in EmmaX.DailyActions:                                                         
                            $ EmmaX.Statup("Obed", 90, 3)
                    if "mono" in EmmaX.Traits:
                            $ EmmaX.Traits.remove("mono")   
                    $ EmmaX.AnyWord(1,0,"mono") #Daily
            "Never mind.":
                pass
        return
        
# end Emma monogamy <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Emma_Jumped:
        #called from Emma_Settings to ask her not to jump you  
        ch_p "Hey, Remember that time you threw yourself at me?" 
        $ EmmaX.FaceChange("sly",1,Brows="confused") 
        ch_e "I believe I recall something like that."
        menu:
            ch_e "What of it?"
            "Could you maybe just ask instead?" if "chill" not in EmmaX.Traits:
                    if EmmaX.Thirst >= 60 and not ApprovalCheck(EmmaX, 1600, "LO", TabM=0):
                            #she's too thirsty
                            $ EmmaX.FaceChange("sly",1) 
                            if "chill" not in EmmaX.DailyActions:                                                         
                                    $ EmmaX.Statup("Obed", 90, -2) 
                            ch_e "I do have certain. . . needs that must be met."
                            ch_e "Stay on your toes."
                            return
                    elif ApprovalCheck(EmmaX, 1100, "LO", TabM=0) and EmmaX.Love >= EmmaX.Obed:
                            #she cares
                            $ EmmaX.FaceChange("sly",1) 
                            if "chill" not in EmmaX.DailyActions:                                                         
                                    $ EmmaX.Statup("Love", 90, 1) 
                            ch_e "I didn't intend to upset you, [EmmaX.Petname]. . ." 
                            ch_e "I'll try to keep control. . ."
                    elif ApprovalCheck(EmmaX, 600, "O", TabM=0):
                            #she is obedient
                            $ EmmaX.FaceChange("sly",1,Eyes="side") 
                            ch_e "If that's what would make you comfortable. . ."
                    else:   
                            #she doesn't care
                            $ EmmaX.FaceChange("sly",1,Brows="confused") 
                            ch_e "I'll see what I can do about that." 
                            ch_e "Stay on your toes."
                            return                    
                    if "chill" not in EmmaX.DailyActions:                                                         
                            $ EmmaX.Statup("Obed", 90, 3) 
                    $ EmmaX.AnyWord(1,0,"chill") #Daily
                    $ EmmaX.Traits.append("chill")   
            "Don't bother me like that." if "chill" not in EmmaX.Traits:
                    if ApprovalCheck(EmmaX, 900, "O", TabM=0):
                            #she is obedient
                            $ EmmaX.FaceChange("sly",1,Eyes="side") 
                            ch_e "Oh, very well."
                    elif EmmaX.Thirst >= 60 and not ApprovalCheck(EmmaX, 600, "O", TabM=0):
                            #she's too thirsty
                            $ EmmaX.FaceChange("sly",1) 
                            if "chill" not in EmmaX.DailyActions:                                                         
                                    $ EmmaX.Statup("Obed", 90, -2) 
                            ch_e "I do have certain. . . needs that must be met."
                            ch_e "Stay on your toes."
                            return
                    elif ApprovalCheck(EmmaX, 450, "O", TabM=0):
                            #she is obedient
                            $ EmmaX.FaceChange("sly",1,Eyes="side") 
                            ch_e "Well, I wouldn't want to be a \"bother\". . ."
                    elif ApprovalCheck(EmmaX, 500, "LO", TabM=0) and not ApprovalCheck(EmmaX, 500, "I", TabM=0):
                            #she cares
                            $ EmmaX.FaceChange("sly",1) 
                            ch_e "Don't press your luck, [EmmaX.Petname]." 
                            ch_e "I will try to give you some space, however. . ."
                    else:   
                            #she doesn't care
                            $ EmmaX.FaceChange("sly",1,Brows="confused") 
                            ch_e "I'll see what I can do about that." 
                            ch_e "Stay on your toes."
                            return                     
                    if "chill" not in EmmaX.DailyActions:                                                         
                            $ EmmaX.Statup("Obed", 90, 3) 
                    $ EmmaX.AnyWord(1,0,"chill") #Daily
                    $ EmmaX.Traits.append("chill")   
            "Knock yourself out.":
                    if ApprovalCheck(EmmaX, 800, "L", TabM=0):
                            $ EmmaX.FaceChange("sly",1) 
                            ch_e "You can count on it. . ." 
                    elif ApprovalCheck(EmmaX, 700, "O", TabM=0):
                            $ EmmaX.FaceChange("sly",1,Eyes="side") 
                            ch_e "Very well."
                    else:
                            $ EmmaX.FaceChange("sly",1,Brows="confused") 
                            if "chill" not in EmmaX.DailyActions:                                                         
                                    $ EmmaX.Statup("Love", 90, -2)
                            ch_e "We'll see. . ." 
                    if "chill" not in EmmaX.DailyActions:                                                         
                            $ EmmaX.Statup("Obed", 90, 3) 
                    if "chill" in EmmaX.Traits:
                            $ EmmaX.Traits.remove("chill")  
                    $ EmmaX.AnyWord(1,0,"chill") #Daily 
            "Um, never mind.":
                pass
        return
        
# end Emma jumped  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# start emma hungry  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Emma_Hungry:
    if EmmaX.Chat[3]:
        ch_e "I do enjoy your taste. . ."
    elif EmmaX.Chat[2]:
        ch_e "You know, that serum of yours has a rather. . . familiar taste to it."
    else:
        ch_e "I do enjoy your taste. . ."
    $ EmmaX.Traits.append("hungry")
return


# end emma hungry / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Emma Sexchat / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Emma_SexChat:
    $ Line = "Hmm? What did you want to talk about?" if not Line else Line
    while True:
            menu:
                ch_e "[Line]"                
                "My favorite thing to do is. . .":
                    if "setfav" in EmmaX.DailyActions:
                        ch_e "I'm aware. You just told me earlier."
                    else:
                        menu:
                            "Sex.":
                                        $ EmmaX.FaceChange("sly")
                                        if EmmaX.PlayerFav == "sex":
                                            $ EmmaX.Statup("Lust", 80, 5)
                                            ch_e "I'm well aware. . ."                                
                                        elif EmmaX.Favorite == "sex":
                                            $ EmmaX.Statup("Love", 90, 5)
                                            $ EmmaX.Statup("Lust", 80, 10)
                                            ch_e "Oh. . . as chance would have it. . ."
                                        elif EmmaX.Sex:
                                            ch_e "I can see why."
                                        else:
                                            $ EmmaX.FaceChange("perplexed")
                                            ch_e "And exactly {i}who{/i} are you having sex {i}with?{/i}"
                                        $ EmmaX.PlayerFav = "sex"
                                        
                            "Anal.":
                                        $ EmmaX.FaceChange("sly")
                                        if EmmaX.PlayerFav == "anal":
                                            $ EmmaX.Statup("Lust", 80, 5)
                                            ch_e "So you've told me. . ."                                
                                        elif EmmaX.Favorite == "anal":
                                            $ EmmaX.Statup("Love", 90, 5)
                                            $ EmmaX.Statup("Lust", 80, 10)
                                            ch_e "{i}Mine too{/i}. . ."
                                        elif EmmaX.Anal >= 10:
                                            ch_e "It certainly is a workout. . ."
                                        elif not EmmaX.Anal:
                                            $ EmmaX.FaceChange("perplexed")
                                            ch_e "Who's ass {i}are{/i} you fucking?"
                                        else:
                                            $ EmmaX.FaceChange("bemused")
                                            ch_e "Yes, you did seem enthusiastic. . ."
                                        $ EmmaX.PlayerFav = "anal"
                                        
                            "Blowjobs.":   
                                        $ EmmaX.FaceChange("sly")
                                        if EmmaX.PlayerFav == "blow":
                                            $ EmmaX.Statup("Lust", 80, 3)
                                            ch_e "Yes, so you've said. . ."                                
                                        elif EmmaX.Favorite == "blow":
                                            $ EmmaX.Statup("Love", 90, 5)
                                            $ EmmaX.Statup("Lust", 80, 5)
                                            ch_e "Hmm, you are delicious. . ."
                                        elif EmmaX.Blow >= 10:
                                            ch_e "I certainly can't complain . . ."
                                        elif not EmmaX.Blow:
                                            $ EmmaX.FaceChange("perplexed")
                                            ch_e "Oh? Is some little whore sucking you off?"
                                        else:
                                            $ EmmaX.FaceChange("bemused")
                                            ch_e "Yes, I enjoy it as well. . . ."
                                        $ EmmaX.PlayerFav = "blow"     
                                        
                            "Titjobs.":
                                        $ EmmaX.FaceChange("sly")
                                        if EmmaX.PlayerFav == "titjob":
                                            $ EmmaX.Statup("Lust", 80, 5)
                                            ch_e "So you're said. . ."                                
                                        elif EmmaX.Favorite == "titjob":
                                            $ EmmaX.Statup("Love", 90, 5)
                                            $ EmmaX.Statup("Lust", 80, 7)
                                            ch_e "I really enjoy it too. . ."
                                        elif EmmaX.Tit >= 10:
                                            ch_e "I can't imagine why . . ."
                                        elif not EmmaX.Tit:
                                            $ EmmaX.FaceChange("perplexed")
                                            ch_e "Oh, is someone else providing that service?"
                                        else:
                                            $ EmmaX.FaceChange("bemused")
                                            ch_e "I can understand why. . ."
                                        $ EmmaX.PlayerFav = "titjob"   
                                        
                            "Footjobs.":
                                        $ EmmaXX.FaceChange("sly")
                                        if EmmaXX.PlayerFav == "foot":
                                            $ EmmaXX.Statup("Lust", 80, 5)
                                            ch_e "Yes, so you've said. . ."                                
                                        elif EmmaXX.Favorite == "foot":
                                            $ EmmaXX.Statup("Love", 90, 5)
                                            $ EmmaXX.Statup("Lust", 80, 7)
                                            ch_e "It certainly is a diversion. . ."
                                        elif EmmaXX.Foot >= 10:
                                            ch_e "Yes, it certainly is a workout . . ."
                                        elif not EmmaXX.Foot:
                                            $ EmmaXX.FaceChange("perplexed")
                                            ch_e "Oh, is some little skank offering footsies now?"
                                        else:
                                            $ EmmaXX.FaceChange("bemused")
                                            ch_e "It certainly is a diversion. . ."
                                        $ EmmaXX.PlayerFav = "foot"  
                                        
                            "Handjobs.":
                                        $ EmmaX.FaceChange("sly")
                                        if EmmaX.PlayerFav == "hand":
                                            $ EmmaX.Statup("Lust", 80, 5)
                                            ch_e "Yes, so you've said. . ."                                
                                        if EmmaX.Favorite == "hand":
                                            $ EmmaX.Statup("Love", 90, 5)
                                            $ EmmaX.Statup("Lust", 80, 7)
                                            ch_e "It certainly is a diversion. . ."
                                        elif EmmaX.Hand >= 10:
                                            ch_e "Yes, it certainly is a workout . . ."
                                        elif not EmmaX.Hand:
                                            $ EmmaX.FaceChange("perplexed")
                                            ch_e "Oh, is some little skank offering handies now?"
                                        else:
                                            $ EmmaX.FaceChange("bemused")
                                            ch_e "It certainly is a diversion. . ."
                                        $ EmmaX.PlayerFav = "hand"  
                                        
                            "Feeling you up.":
                                        $ Cnt = EmmaX.FondleB + EmmaX.FondleT + EmmaX.SuckB + EmmaX.Hotdog
                                        $ EmmaX.FaceChange("sly")
                                        if EmmaX.PlayerFav == "fondle":
                                            $ EmmaX.Statup("Lust", 80, 3)
                                            ch_e "I've heard that before. . ."                                
                                        elif EmmaX.Favorite in ("hotdog","suck breasts","fondle breasts","fondle thighs"):
                                            $ EmmaX.Statup("Love", 90, 5)
                                            $ EmmaX.Statup("Lust", 80, 5)
                                            ch_e "You do have a way with my body . ."
                                        elif not Cnt:
                                            $ EmmaX.FaceChange("perplexed")
                                            ch_e "I can't imagine who youre feeling up. Yet."
                                        else:
                                            $ EmmaX.FaceChange("bemused")
                                            ch_e "You have a very deft hand . . ."
                                        $ EmmaX.PlayerFav = "fondle"  
                                        $ Cnt = 0
                                
                            "Kissing you.":
                                        $ EmmaX.FaceChange("sly")
                                        if EmmaX.PlayerFav == "kiss you":
                                            $ EmmaX.Statup("Love", 90, 3)
                                            ch_e "I'm well aware. . ."                                
                                        elif EmmaX.Favorite == "kiss you":
                                            $ EmmaX.Statup("Love", 90, 5)
                                            $ EmmaX.Statup("Lust", 80, 5)
                                            ch_e "For some reason, the romantic in me agrees. . ."
                                        elif EmmaX.Kissed >= 10:
                                            ch_e "I love kissing you too . . ."
                                        elif not EmmaX.Kissed:
                                            $ EmmaX.FaceChange("perplexed")
                                            ch_e "Who {i}are{/i} you kissing, [EmmaX.Petname]?"
                                        else:
                                            $ EmmaX.FaceChange("bemused")
                                            ch_e "How romantic."
                                        $ EmmaX.PlayerFav = "kiss you" 
                                
                        $ EmmaX.DailyActions.append("setfav") 
                            
                "What's your favorite thing to do?":
                                if not ApprovalCheck(EmmaX, 800):
                                        $ EmmaX.FaceChange("perplexed")
                                        ch_e "I don't believe that's an appropriate question. . ."                                    
                                else:
                                        if EmmaX.SEXP >= 50:
                                            $ EmmaX.FaceChange("sly")
                                            ch_e "You really should know already . ."   
                                        else:                 
                                            $ EmmaX.FaceChange("bemused")
                                            $ EmmaX.Eyes = "side"
                                            ch_e "Hmm, I suppose I could tell you. . ."
                                            
                                            
                                        if not EmmaX.Favorite or EmmaX.Favorite == "kiss":
                                            ch_e "Call me a romantic, but I enjoy kissing you. . ."  
                                        elif EmmaX.Favorite == "anal":
                                                ch_e "I really enjoy anal."  
                                        elif EmmaX.Favorite == "lick ass":
                                                ch_e "I enjoy it when you lick my asshole." 
                                        elif EmmaX.Favorite == "insert ass":
                                                ch_e "I enjoy it when you stick a finger in my ass." 
                                        elif EmmaX.Favorite == "sex":
                                                ch_e "I like when you fuck me hard." 
                                        elif EmmaX.Favorite == "lick pussy":
                                                ch_e "I like when you lick my pussy." 
                                        elif EmmaX.Favorite == "fondle pussy":
                                                ch_e "I like when you finger me." 
                                        elif EmmaX.Favorite == "blow":
                                                ch_e "I quite enjoy sucking you, is that a problem?" 
                                        elif EmmaX.Favorite == "tit":
                                                ch_e "I enjoy using my tits." 
                                        elif EmmaX.Favorite == "foot":
                                                ch_e "I do enjoy using my feet." 
                                        elif EmmaX.Favorite == "hand":
                                                ch_e "I enjoy stroking you off." 
                                        elif EmmaX.Favorite == "hotdog":
                                                ch_e "I enjoy it when you grind against me." 
                                        elif EmmaX.Favorite == "suck breasts":
                                                ch_e "You are good at sucking my tits."  
                                        elif EmmaX.Favorite == "fondle breasts":
                                                ch_e "You are good at fondling my tits."  
                                        elif EmmaX.Favorite == "fondle thighs":
                                                ch_e "I enjoy when you massage my thighs."
                                        else:
                                                ch_e "I'm really not sure. . ."    
                                                
                                # End Emma's favorite things.
                    
                "Don't talk as much during sex." if "vocal" in EmmaX.Traits:
                        if "setvocal" in EmmaX.DailyActions:
                            $ EmmaX.FaceChange("perplexed")
                            ch_e "You've made yourself clear on the matter."
                        else:              
                            if ApprovalCheck(EmmaX, 1000) and EmmaX.Obed <= EmmaX.Love:
                                $ EmmaX.FaceChange("bemused")
                                $ EmmaX.Statup("Obed", 90, 1)
                                ch_e "Oh, very well. . ."
                                $ EmmaX.Traits.remove("vocal")   
                            elif ApprovalCheck(EmmaX, 700, "O"):
                                $ EmmaX.FaceChange("sadside")
                                $ EmmaX.Statup("Obed", 90, 1)
                                ch_e "I suppose I could, [EmmaX.Petname]."
                                $ EmmaX.Traits.remove("vocal")   
                            elif ApprovalCheck(EmmaX, 600):
                                $ EmmaX.FaceChange("sly")
                                $ EmmaX.Statup("Love", 90, -3)
                                $ EmmaX.Statup("Obed", 50, -1)
                                $ EmmaX.Statup("Inbt", 90, 5)
                                ch_e "Don't presume to tell me what to say, [EmmaX.Petname]."
                            else:
                                $ EmmaX.FaceChange("angry")
                                $ EmmaX.Statup("Love", 90, -5)
                                $ EmmaX.Statup("Obed", 60, -3)
                                $ EmmaX.Statup("Inbt", 90, 10)
                                ch_e "I'll say what I wish, and you'll enjoy it."
                                                
                            $ EmmaX.DailyActions.append("setvocal")   
                "Talk dirty to me during sex." if "vocal" not in EmmaX.Traits:
                        if "setvocal" in EmmaX.DailyActions:
                            $ EmmaX.FaceChange("perplexed")
                            ch_e "We've discussed this already."
                        else:     
                            if ApprovalCheck(EmmaX, 1000) and EmmaX.Obed <= EmmaX.Love:
                                $ EmmaX.FaceChange("sly")
                                $ EmmaX.Statup("Obed", 90, 2)
                                ch_e "Mmmm, I believe I can do that. . ."
                                $ EmmaX.Traits.append("vocal")   
                            elif ApprovalCheck(EmmaX, 700, "O"):
                                $ EmmaX.FaceChange("sadside")
                                $ EmmaX.Statup("Obed", 90, 2)
                                ch_e "If that's what you wish, [EmmaX.Petname]."
                                $ EmmaX.Traits.append("vocal")   
                            elif ApprovalCheck(EmmaX, 600):
                                $ EmmaX.FaceChange("sly")
                                $ EmmaX.Statup("Obed", 90, 3)
                                ch_e "I suppose I could, [EmmaX.Petname]."
                                $ EmmaX.Traits.append("vocal")   
                            else:
                                $ EmmaX.FaceChange("angry")
                                $ EmmaX.Statup("Inbt", 90, 5)
                                ch_e "If I feel like it."  
                                
                            $ EmmaX.DailyActions.append("setvocal")  
                        # End Emma Dirty Talk
                    
                "Don't do your own thing as much during sex." if "passive" not in EmmaX.Traits:
                        if "initiative" in EmmaX.DailyActions:
                            $ EmmaX.FaceChange("perplexed")
                            ch_e "I believe we've discussed this."
                        else:       
                            if ApprovalCheck(EmmaX, 1000) and EmmaX.Obed <= EmmaX.Love:
                                $ EmmaX.FaceChange("bemused")
                                $ EmmaX.Statup("Obed", 90, 1)
                                ch_e "Oh, so you want to take charge? . ."   
                                $ EmmaX.Traits.append("passive")                 
                            elif ApprovalCheck(EmmaX, 700, "O"):
                                $ EmmaX.FaceChange("sadside")
                                $ EmmaX.Statup("Obed", 90, 1)
                                ch_e "I'll await your instruction, [EmmaX.Petname]."
                                $ EmmaX.Traits.append("passive")   
                            elif ApprovalCheck(EmmaX, 600):
                                $ EmmaX.FaceChange("sly")
                                $ EmmaX.Statup("Love", 90, -3)
                                $ EmmaX.Statup("Obed", 50, -1)
                                $ EmmaX.Statup("Inbt", 90, 5)
                                ch_e "Oh, you don't mean that, [EmmaX.Petname]."
                            else:
                                $ EmmaX.FaceChange("angry")
                                $ EmmaX.Statup("Love", 90, -5)
                                $ EmmaX.Statup("Obed", 60, -3)
                                $ EmmaX.Statup("Inbt", 90, 10)
                                ch_e "You wish."
                                
                            $ EmmaX.DailyActions.append("initiative")  
                "Take more initiative during sex." if "passive" in EmmaX.Traits:
                        if "initiative" in EmmaX.DailyActions:
                                $ EmmaX.FaceChange("perplexed")
                                ch_e "I believe we've discussed this."
                        else:   
                            if ApprovalCheck(EmmaX, 1000) and EmmaX.Obed <= EmmaX.Love:
                                $ EmmaX.FaceChange("bemused")
                                $ EmmaX.Statup("Obed", 90, 1)
                                ch_e "Oh, you know that I will. . ."   
                                $ EmmaX.Traits.remove("passive")                     
                            elif ApprovalCheck(EmmaX, 700, "O"):
                                $ EmmaX.FaceChange("sadside")
                                $ EmmaX.Statup("Obed", 90, 1)
                                ch_e "I can do that, [EmmaX.Petname]."
                                $ EmmaX.Traits.remove("passive")   
                            elif ApprovalCheck(EmmaX, 600):
                                $ EmmaX.FaceChange("sly")
                                $ EmmaX.Statup("Obed", 90, 3)
                                ch_e "I suppose I might, [EmmaX.Petname]."
                                $ EmmaX.Traits.remove("passive")   
                            else:
                                $ EmmaX.FaceChange("angry")
                                $ EmmaX.Statup("Inbt", 90, 5)
                                ch_e "We'll see."  
                                
                            $ EmmaX.DailyActions.append("initiative") 
                            
                
                "About getting Jumped" if "jumped" in EmmaX.History:
                        call Emma_Jumped
                "About when you masturbate":
                        call NoFap(EmmaX)
                    
                "Have you considered maybe having some fun in public?" if "taboocheck" not in EmmaX.History and "taboo" not in EmmaX.History:
                        call Emma_Taboo_Talk
                "We talked about maybe having some fun in public?" if "taboocheck" in EmmaX.History and "taboo" not in EmmaX.History:
                        call Emma_Taboo_Talk
                    
                "Have you considered maybe having a threesome?" if "threecheck" not in EmmaX.History and "three" not in EmmaX.History:
                        call Emma_ThreeCheck
                "We talked about maybe having a threesome?" if "threecheck" in EmmaX.History and "three" not in EmmaX.History:
                        call Emma_ThreeCheck
                
                "Never Mind" if Line == "Hmm? What did you want to talk about?":
                        return
                "That's all." if Line != "Hmm? What did you want to talk about?":
                        return
            if Line == "Yeah, what did you want to talk about?":
                $ Line = "Anything else?"
    return
# End Emma Sexchat / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

## Emma Chitchat / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Emma_Chitchat(O=0, Options = ["default","default","default"]):    
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:                                               #adds only a specific option that was sent
        $ Options = [O]
    else:
        if EmmaX not in Digits:
                if ApprovalCheck(EmmaX, 500, "L") or ApprovalCheck(EmmaX, 250, "I"):
                    ch_e "If you'd like to reach me. . . after hours, here's my number."
                    $ Digits.append(EmmaX)  
                    return
                elif ApprovalCheck(EmmaX, 250, "O"):
                    ch_e "I should let you know how to contact me."             
                    $ Digits.append(EmmaX)
                    return
                
        if "hungry" not in EmmaX.Traits and (EmmaX.Swallow + EmmaX.Chat[2]) >= 10 and EmmaX.Loc == bg_current:  #She's swallowed a lot        
                    call Emma_Hungry
                    return  
        if not Taboo or ApprovalCheck(EmmaX, 800, "I"):
                    if EmmaX.Loc == bg_current and EmmaX.Thirst >= 30 and "refused" not in EmmaX.DailyActions and "quicksex" not in EmmaX.DailyActions: 
                            $ Girl.FaceChange("sly",1,Eyes="down")    
                            ch_e "I've got an itch. . . "
                            "[EmmaX.Name] draws her hand down her body and grazes her pussy."      
                            $ Girl.FaceChange("sly",1)    
                            ch_e ". . think you can scratch it?"
                            call Quick_Sex(EmmaX)
                    return
        
#        $ Options = ["default","default","default"]
        #adds options based on accomplishments
        if "classcaught" in EmmaX.Traits:
            if "caught" in EmmaX.DailyActions and "caught chat" not in EmmaX.DailyActions:
                $ Options.append("caught")
            if EmmaX.Event[0] and "key" not in EmmaX.Chat:
                $ Options.append("key")
            if "lover" in EmmaX.Petnames and ApprovalCheck(EmmaX, 900, "L"): # luvy dovey       
                $ Options.append("luv")
                  
            if "mandrill" in Player.Traits and "cologne chat" not in EmmaX.DailyActions:
                $ Options.append("mandrill")        
            if "purple" in Player.Traits and "cologne chat" not in EmmaX.DailyActions:
                $ Options.append("purple")        
            if "corruption" in Player.Traits and "cologne chat" not in EmmaX.DailyActions:
                $ Options.append("corruption")
            
            if EmmaX.Date >= 1:
                #if you've dated before
                $ Options.append("dated")
            if "cheek" in EmmaX.DailyActions and "cheek" not in EmmaX.Chat:
                #If you've touched her cheek today
                $ Options.append("cheek")
            if EmmaX.Kissed >= 5:
                #if you've kissed a few times
                $ Options.append("kissed")
            if "dangerroom" in Player.DailyActions:
                #If you've been in the danger room today
                $ Options.append("dangerroom")
            if "showered" in EmmaX.DailyActions:
                #If you've caught Emma showering today
                $ Options.append("showercaught")
            if "fondle breasts" in EmmaX.DailyActions or "fondle pussy" in EmmaX.DailyActions or "fondle ass" in EmmaX.DailyActions:
                #If you've fondled Emma today
                $ Options.append("fondled")
            if "Dazzler and Longshot" in EmmaX.Inventory and "256 Shades of Grey" in EmmaX.Inventory and "Avengers Tower Penthouse" in EmmaX.Inventory:   
                #If you've given Emma the books
                if "book" not in EmmaX.Chat:
                    $ Options.append("booked")
            if "lace bra" in EmmaX.Inventory or "lace panties" in EmmaX.Inventory:   
                #If you've given Emma the lingerie
                if "lingerie" not in EmmaX.Chat:
                    $ Options.append("lingerie")
            if EmmaX.Hand:   
                #If Emma's given a handjob
                $ Options.append("handy")
            if EmmaX.Swallow:   
                #If Emma's swallowed before
                $ Options.append("swallowed")
            if "cleaned" in EmmaX.DailyActions or "painted" in EmmaX.DailyActions:
                #If Emma's been facialed
                $ Options.append("facial")
            if EmmaX.Sleep:
                #If Emma's slept over
                $ Options.append("sleep")
            if EmmaX.CreamP or EmmaX.CreamA:
                #If Emma's been creampied
                $ Options.append("creampie")
            if EmmaX.Sex or EmmaX.Anal:
                #If Emma's been sexed
                $ Options.append("sexed")
            if EmmaX.Anal:
                #If Emma's been analed
                $ Options.append("anal")
            if "public" in EmmaX.History and "public" not in EmmaX.Chat:
                $ Options.append("public")            
                
            if (bg_current == "bg emma" or bg_current == "bg player") and "relationship" not in EmmaX.DailyActions:
                if "lover" not in EmmaX.Petnames and EmmaX.Love >= 950 and EmmaX.Event[6] != 20: # EmmaX.Event[6]        
                    $ Options.append("lover?")
                elif "sir" not in EmmaX.History and EmmaX.Obed >= 500: # EmmaX.Event[7]
                    $ Options.append("sir?")      
                elif "daddy" not in EmmaX.Petnames and ApprovalCheck(EmmaX, 750, "L") and ApprovalCheck(EmmaX, 500, "O") and ApprovalCheck(EmmaX, 500, "I"): # EmmaX.Event[5]
                    $ Options.append("daddy?")
                elif "master" not in EmmaX.History and EmmaX.Obed >= 800 and "sir" in EmmaX.Petnames: # EmmaX.Event[8]
                    $ Options.append("master?")
                elif "sex friend" not in EmmaX.Petnames and EmmaX.Inbt >= 500 and bg_current == "bg classroom" and Time_Count == 2: # EmmaX.Event[9]
                    $ Options.append("sexfriend?")
                elif "fuck buddy" not in EmmaX.Petnames and EmmaX.Inbt >= 800 and bg_current != EmmaX.Loc: # EmmaX.Event[10]
                    $ Options.append("fuckbuddy?")  
            
        
        if not ApprovalCheck(EmmaX, 300):            #She dislikes you
            $ Options.append("hate") 
    
    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one
    
    if Options[0] == "mandrill":                             
        $ EmmaX.DailyActions.append("cologne chat") 
        $ EmmaX.FaceChange("confused")
        ch_e "(sniff, sniff). . . you aren't using that cheap baboon musk, are you? . ."
        $ EmmaX.FaceChange("perplexed", 1)
        ch_e ". . . though I suppose. . . he wasn't that bad. . ."    
    elif Options[0] == "purple":              
        $ EmmaX.DailyActions.append("cologne chat") 
        $ EmmaX.FaceChange("sly",1)
        ch_e "(sniff, sniff). . . huh, what's that smell? . ."
        ch_e ". . . was there anything I could do for you?"    
    elif Options[0] == "corruption":              
        $ EmmaX.DailyActions.append("cologne chat") 
        $ EmmaX.FaceChange("confused")
        ch_e "(sniff, sniff). . . that's. . . ripe. . ."
        $ EmmaX.FaceChange("sly")
        ch_e ". . . I may have some. . . purpose for you later. . ."
                
    elif Options[0] == "caught": # Xavier's caught you
            $ EmmaX.FaceChange("angry", Eyes="side")
            if "caught chat" in EmmaX.Chat:
                    ch_e "I'm getting rather tired of getting dragged into Charles' office."
                    ch_e "Perhaps we ought to be more. . . discrete." 
                    if not ApprovalCheck(EmmaX, 500, "I"):
                        $ EmmaX.FaceChange("sly", Eyes="side")
                        ch_e "Sometimes. . ."
            else:    
                    ch_e "Well that was certainly unpleasant."
                    ch_e "Xavier talked my ear off for at least an hour."
                    ch_e "Some nonsense about \"the responsibilities of an educator.\""
                    ch_e "I'll have you know, I take my responsibilities to my students. . ."
                    $ EmmaX.FaceChange("sly")
                    ch_e "{i}very{/i} seriously. . ."
                    if not ApprovalCheck(EmmaX, 500, "I"):
                        ch_e "I don't thing we should be so forward in public anymore."
                    else:
                        ch_e "I did enjoy seeing the old buzzard so worked up though. . ."
                    $ EmmaX.Chat.append("caught chat") 
    elif Options[0] == "key": # you have her key
            if EmmaX.SEXP <= 15:
                ch_e "Now just because I gave you my room key, doesn't mean you shouldn't knock. . ."
            else:
                ch_e "I gave you that key for a reason, you might want to use it sometime. . ."
            $ EmmaX.Chat.append("key") 
        
    elif Options[0] == "cheek":
            #Emma's response to having her cheek touched.
            ch_e "Earlier, you brushed my cheek. . ."
            ch_p "Yeah?  Was that okay?"
            if ApprovalCheck(EmmaX, 600, "L"):
                    $ EmmaX.FaceChange("smile",1)
                    ch_e "Yes, it was. . . intimate." 
                    $ EmmaX.Chat.append("cheek") 
            elif ApprovalCheck(EmmaX, 800):
                    $ EmmaX.FaceChange("normal",1,Eyes="side")
                    ch_e "I. . . suppose so, [EmmaX.Petname]." 
            else:
                    $ EmmaX.FaceChange("confused",1,Eyes="side")
                    ch_e "I just found it to be a bit. . . forward." 
            
            
    elif Options[0] == "dated":
            #Emma's response to having gone on a date with the Player.
            ch_e "You should know, I enjoyed our last date.  We should do that again sometime."

    elif Options[0] == "kissed":
            #Emma's response to having been kissed by the Player.
            $ EmmaX.FaceChange("sly",1)
            ch_e "You have some remarkably skilled lips, [EmmaX.Petname]."
            menu:
                extend ""
                "Hey. . .when you're good, you're good.":
                        $ EmmaX.FaceChange("smile",1)
                        ch_e "Oh, don't let it get to your head."
                        ch_e "-unless you're interested in sharing."
                "No. You think?":
                        ch_e "Oh, learn to take a compliment, [EmmaX.Petname]."

    elif Options[0] == "dangerroom":
            #Emma's response to Player working out in the Danger Room while Emma is present
            $ EmmaX.FaceChange("sly",1)
            ch_e "I caught your last Danger Room session,[EmmaX.Petname]."  
            ch_e "You certainly do. . . fill out that uniform."

    elif Options[0] == "showercaught":
            #Emma's response to being caught in the shower.
            if "shower" in EmmaX.Chat: 
                ch_e "Enjoy the show earlier?"                       
            else:
                ch_e "I do hope that my appearance in the shower earlier wasn't too distracting."            
                $ EmmaX.Chat.append("shower") 
                menu:
                    extend ""
                    "It was a total accident!  I promise!":             
                            $ EmmaX.Statup("Love", 50, 5)    
                            $ EmmaX.Statup("Love", 90, 2) 
                            if ApprovalCheck(EmmaX, 1000):
                                $ EmmaX.FaceChange("sly",1)
                                ch_e "Oh? so I can't count on a repeat performance?"
                            else:
                                $ EmmaX.FaceChange("smile")
                                ch_e "It happens, just don't make a habit of it."
                    "I only have eyes for you.":        
                            $ EmmaX.Statup("Obed", 40, 5)   
                            if ApprovalCheck(EmmaX, 1000) or ApprovalCheck(EmmaX, 700, "L"):      
                                    $ EmmaX.Statup("Love", 90, 3)    
                                    $ EmmaX.FaceChange("sly",1)
                                    ch_e "Oh, I'm sure that's true. . ."
                                    ch_e "It is nice to hear though."
                            else:                
                                    $ EmmaX.Statup("Love", 70, -5) 
                                    $ EmmaX.FaceChange("angry", Eyes="side")
                                    ch_e "I suppose it's better than being stalked by one-eye over there."                                                       
                    "Totally on purpose. I regret nothing.":
                            if ApprovalCheck(EmmaX, 1200):                     
                                    $ EmmaX.Statup("Love", 90, 3)          
                                    $ EmmaX.Statup("Obed", 70, 10)            
                                    $ EmmaX.Statup("Inbt", 50, 5) 
                                    $ EmmaX.FaceChange("sly",1)
                                    ch_e "Welll. . . I suppose I can appreciate your honesty."
                                    $ EmmaX.FaceChange("sly",1, Eyes="side")
                                    ch_e ". . .if not for your lack of follow-through."
                            elif ApprovalCheck(EmmaX, 800):                          
                                    $ EmmaX.Statup("Obed", 60, 5)            
                                    $ EmmaX.Statup("Inbt", 50, 5) 
                                    $ EmmaX.FaceChange("perplexed",2)
                                    ch_e "Hmm? I suppose I can't blame you for that."
                            else:                
                                    $ EmmaX.Statup("Love", 50, -10) 
                                    $ EmmaX.Statup("Love", 80, -10)          
                                    $ EmmaX.Statup("Obed", 50, 10)  
                                    $ EmmaX.FaceChange("angry")
                                    ch_e "Unexpectedly honest, but still unacceptable."

    elif Options[0] == "fondled":
            #Emma's response to being felt up.
            if EmmaX.FondleB + EmmaX.FondleP + EmmaX.FondleA >= 10:
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
                        $ EmmaX.FaceChange("sly",2)
                        ch_e "They were a bit simplistic, but certainly inspirational."
                "Good. You looked like you could use to learn a thing or two from them.":                     
                        $ EmmaX.Statup("Love", 90, 3)            
                        $ EmmaX.Statup("Inbt", 50, 10) 
                        $ EmmaX.FaceChange("sly")
                        ch_e "Oh, [EmmaX.Petname], the things I could teach those authors would leave them in the hospital."
            $ EmmaX.Blush = 1
            $ EmmaX.Chat.append("book") 

    elif Options[0] == "lingerie":
            #Emma's response to being given lingerie.
            $ EmmaX.FaceChange("sly")
            ch_e "[EmmaX.Petname], I wanted to thank you again for the. . .{i}clothing{/i} you bought me."
            ch_e "They look wonderful."
            $ EmmaX.Chat.append("lingerie") 

    elif Options[0] == "handy":
            #Emma's response after giving the Player a handjob.
            $ EmmaX.FaceChange("sly", Eyes="side")
            ch_e "You know, I was thinking about my hand," 
            $ EmmaX.FaceChange("sly")
            ch_e "on your cock. . ."
            ch_e "Oh, that expression is priceless. . ."
            ch_e "I suppose I'll have to repeat that service sometime. . ."

    elif Options[0] == "blow":
            if "blow" not in EmmaX.Chat:
                    #Emma's response after giving the Player a blowjob.
                    $ EmmaX.FaceChange("sly",2)
                    ch_e "You know, [EmmaX.Petname], you have a very unique flavor to you."
                    ch_p "Oh?"
                    ch_e "Your cock, I mean."
                    ch_e "Very. . . satisfying."
                    menu:
                        extend ""
                        "Well, there's always more where that came from.":                            
                                    $ EmmaX.Statup("Love", 90, 5)            
                                    $ EmmaX.Statup("Inbt", 60, 10) 
                                    $ EmmaX.FaceChange("sly")
                                    ch_e "I'll have to take you up on that."
                        "I'm glad it measured up to all those other guys.":
                                if ApprovalCheck(EmmaX, 300, "I") or not ApprovalCheck(EmmaX, 800):     
                                    $ EmmaX.Statup("Obed", 60, 10)            
                                    $ EmmaX.Statup("Inbt", 50, 10) 
                                    $ EmmaX.FaceChange("smile",1)
                                    ch_e "Oh, it certainly managed that."
                                else:                            
                                    $ EmmaX.Statup("Love", 80, -2)                            
                                    $ EmmaX.Statup("Obed", 70, 10)            
                                    $ EmmaX.Statup("Inbt", 50, 5) 
                                    $ EmmaX.FaceChange("sly")
                                    ch_e "Are you trying to imply something about my. . . experience?"      
                    $ EmmaX.Blush = 1
                    $ EmmaX.Chat.append("blow") 
            else:
                    $ Line = renpy.random.choice(["You've a taste that's easy to acquire.", 
                            "My jaw is a bit sore lately.", 
                            "If you need some. . . attention, let me know.",
                            "Mmmm. . . [she mimes her tongue knocking against her cheek.]"])
                    ch_e "[Line]"

    elif Options[0] == "swallowed":
            #Emma's response after swallowing the Player's cum.
            if "swallow" in EmmaX.Chat:                
                ch_e "I think I'd like another taste of your. . . essence."
            else:
                ch_e "You certainly have a unique flavor to your semen, [EmmaX.Petname]."
                $ EmmaX.FaceChange("sly",1)
                ch_e "Very. . . envigorating. . ."
                $ EmmaX.Chat.append("swallow") 

    elif Options[0] == "facial":
            #Emma's response after taking a facial from the Player.
            $ EmmaX.FaceChange("sexy")
            ch_e "You know, perhaps you could try to keep it away from my eyes next time?"

    elif Options[0] == "sleepover":
            #Emma's response after sleeping with the Player.
            ch_e "You're so restless in your sleep, it gives me. . . ideas."

    elif Options[0] == "creampie":
            #Another of Emma's responses after having sex with the Player.
            "[EmmaX.Name] draws close to you so she can whisper into your ear."
            ch_e "I can still feel you. . .running down the inside of my thigh."

    elif Options[0] == "sexed":
            #A final response from Emma after having sex with the Player.
            $ EmmaX.FaceChange("sexy",2)
            ch_e "Since being with you, I have a lot more to think about, after class. . ."

    elif Options[0] == "anal":
            #Emma's response after getting anal from the Player.
            $ EmmaX.FaceChange("sly",1)
            ch_e "It's been a while since I've had anyone use the back door."
            $ EmmaX.FaceChange("sexy")
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
                $ EmmaX.FaceChange("sly")    
                ch_e "Hmm, well I suppose the cat's out of the bag now."
                $ EmmaX.FaceChange("sly", Eyes="side",Brows="angry")    
                if "spotted" in EmmaX.DailyActions:
                    ch_e "With that show we put on earlier, I doubt we can keep rumors from spreading."
                else:
                    ch_e "With that show we put on the other day, I doubt we can keep rumors from spreading."
                ch_e ". . ."
                $ EmmaX.FaceChange("sly")                               
                $ EmmaX.Statup("Obed", 70, 10)               
                $ EmmaX.Statup("Inbt", 60, 10)          
                $ EmmaX.Statup("Inbt", 90, 10) 
                ch_e "I suppose we'll just have to spread some more. . ."
                $ EmmaX.Chat.append("public") 
                    
    elif Options[0] == "hate": # trinty lower then 50:
        $ Line = renpy.random.choice(["I'd rather keep this professional.", 
                "If you have something to say, put it in writing.", 
                "Back off.",
                "Leave me alone."])
        ch_e "[Line]"
        
    else: #all else fell through. . .
            $ D20 = renpy.random.randint(1, 15)        
            if D20 == 1:
                    $ EmmaX.FaceChange("smile")
                    ch_e "You did  lovely job on the quiz the other day."
            elif D20 == 2:
                    $ EmmaX.FaceChange("sad")
                    ch_e "I've had a miserable amount of paperwork lately."
                    $ EmmaX.FaceChange("bemused")
                    ch_e "Perhaps come by after class to help?"
            elif D20 == 3:
                    $ EmmaX.FaceChange("surprised")
                    ch_e "You should have seen what Miss Pryde was wearing earlier!"
            elif D20 == 4:
                    $ EmmaX.FaceChange("sad")
                    ch_e "Preparing for next week's test has been exhausting!"
            elif D20 == 5:
                    $ EmmaX.FaceChange("smile")
                    ch_e "It really is a lovely day for a walk. . ."
            elif D20 == 6:
                    $ EmmaX.FaceChange("startled")
                    ch_e "There have been some serious issues lately with Sentinel attacks."
            elif D20 == 7:
                    $ EmmaX.FaceChange("smile")
                    ch_e "I've just had a positive progress report on my work so far."
            elif D20 == 8:
                    $ EmmaX.FaceChange("sad")
                    ch_e "This is a lovely school, but I do miss the amenities of the big city."
            elif D20 == 9:
                    $ EmmaX.FaceChange("confused")
                    ch_e "Do you pick up that weird humming of Xavier's in your head, or is that just me?"
            elif D20 == 10:
                    $ EmmaX.FaceChange("smile")
                    ch_e "I think the class is picking up the recent study sessions."
            elif D20 == 11:
                    $ EmmaX.FaceChange("smile")
                    ch_e "I've been looking forward to my next workout session."
            elif D20 == 12:
                    $ EmmaX.FaceChange("sad")
                    ch_e "I'm not sure what to do with Rogue's grades, they're starting to slip."
            elif D20 == 13:
                    $ EmmaX.FaceChange("smile")
                    ch_e "Not that I'm a lush or anything, but I could really do for a drink."
            elif D20 == 14:
                    $ EmmaX.FaceChange("sad")
                    ch_e "There's been another attack on the news, deplorable."
            elif D20 == 15:
                    $ EmmaX.FaceChange("sadside")
                    ch_e "I think I must have pulled something during my workout yesterday."
                    $ EmmaX.FaceChange("sly",Mouth="normal")
                    ch_e "Perhaps you could work it out for me?"
            else:
                    $ EmmaX.FaceChange("startled")
                    ch_e "As students go, you're not intollerable."
        
    $ Line = 0
    return

# start Emma_Names / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Emma_Names(TempName=0):    
    call LastNamer
    $ TempName = _return
    menu:
        ch_e "Oh? What would you like me to call you?"
        "[TempName]'s fine.":
            # ie "Mr. Zero"
            $ EmmaX.Petname = TempName
            ch_e "I assumed it was, [EmmaX.Petname]."
        "Call me by my name.":
            $ EmmaX.Petname = Player.Name            
            ch_e "If you'd rather, [EmmaX.Petname]."
        "Call me \"dear\"." if "dear" in EmmaX.Petnames:
            $ EmmaX.Petname = "dear"
            ch_e "Certainly, [EmmaX.Petname]."
        "Call me \"darling\"." if "darling" in EmmaX.Petnames:
            $ EmmaX.Petname = "darling"
            ch_e "Certainly, [EmmaX.Petname]."
        "Call me \"boyfriend\"." if "boyfriend" in EmmaX.Petnames:
            $ EmmaX.Petname = "boyfriend"
            ch_e "How pedestrian, but fine, [EmmaX.Petname]."
        "Call me \"lover\"." if "lover" in EmmaX.Petnames:
            $ EmmaX.Petname = "lover"
            ch_e "Certainly, [EmmaX.Petname]."
        "Call me \"sir\"." if "sir" in EmmaX.Petnames:
            $ EmmaX.Petname = "sir"
            ch_e "Yes, [EmmaX.Petname]."
        "Call me \"master\"." if "master" in EmmaX.Petnames:
            $ EmmaX.Petname = "master"
            ch_e "As you wish, [EmmaX.Petname]."
        "Call me \"sex friend\"." if "sex friend" in EmmaX.Petnames:
            $ EmmaX.Petname = "sex friend"
            ch_e "You naughty boy. Very well, [EmmaX.Petname]."
        "Call me \"fuck buddy\"." if "fuck buddy" in EmmaX.Petnames:
            $ EmmaX.Petname = "fuck buddy"
            ch_e "How nasty, \"[EmmaX.Petname]\"."        
        "Call me \"daddy\"." if "daddy" in EmmaX.Petnames:
            $ EmmaX.Petname = "daddy"
            ch_e "Mmm, ok, [EmmaX.Petname]."
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
                        $ EmmaX.Pet = "Ms. Frost"            
                        $ EmmaX.Name = "Ms. Frost"
                        ch_e "I don't see why not, [EmmaX.Petname]."
                        
                    "I think I'll just call you Emma.":
                        if ApprovalCheck(EmmaX, 700) or "classcaught" in EmmaX.History:
                            ch_e "I don't see why not, [EmmaX.Petname]."   
                            $ EmmaX.Pet = EmmaX            
                            $ EmmaX.Name = EmmaX
                        else:
                            ch_e "I'd rather you didn't, [EmmaX.Petname]."
                        
                    "I think I'll call you \"girl\".":
                        $ EmmaX.Pet = "girl"
                        if "boyfriend" in EmmaX.Petnames or ApprovalCheck(EmmaX, 600, "L"):
                            $ EmmaX.FaceChange("sexy", 1) 
                            ch_e "How droll, [EmmaX.Petname]."
                        else:      
                            $ EmmaX.FaceChange("angry")           
                            ch_e "I wouldn't, [EmmaX.Petname]." 
                            
                    "I think I'll call you \"boo\".":
                        $ EmmaX.Pet = "boo"
                        if "boyfriend" in EmmaX.Petnames or ApprovalCheck(EmmaX, 800, "L"):
                            $ EmmaX.FaceChange("bemused", 1) 
                            ch_e "How adorable, [EmmaX.Petname]."
                        else:     
                            $ EmmaX.FaceChange("angry")            
                            ch_e "I'm no such thing,  [EmmaX.Petname]."
                            
                    "I think I'll call you \"bae\".":
                        $ EmmaX.Pet = "bae"
                        if "boyfriend" in EmmaX.Petnames or ApprovalCheck(EmmaX, 800, "L"):
                            $ EmmaX.FaceChange("sexy", 1) 
                            ch_e "I suppose I am your. . . \"bae?\""
                        else:     
                            $ EmmaX.FaceChange("angry")            
                            ch_e "What does that even mean?."
                            
                    "I think I'll call you \"baby\".":
                        $ EmmaX.Pet = "baby"
                        if "boyfriend" in EmmaX.Petnames or ApprovalCheck(EmmaX, 500, "L"):
                            $ EmmaX.FaceChange("sexy", 1) 
                            ch_e "How precious."
                        else:     
                            $ EmmaX.FaceChange("angry")            
                            ch_e "I think I'm a bit. . . mature for that." 
                            
                    "I think I'll call you \"darling\".":
                        $ EmmaX.Pet = "darling"
                        if "boyfriend" in EmmaX.Petnames or ApprovalCheck(EmmaX, 600, "L"):
                            ch_e "I do adore you, [EmmaX.Petname]."
                        else:     
                            $ EmmaX.FaceChange("angry", 1)            
                            ch_e "A bit premature, [EmmaX.Petname]."
                            
                    "I think I'll call you \"sweetie\".":
                        $ EmmaX.Pet = "sweetie"
                        if "boyfriend" in EmmaX.Petnames or ApprovalCheck(EmmaX, 500, "L"):
                            ch_e "Really, [EmmaX.Petname]?"
                        else:     
                            $ EmmaX.FaceChange("angry", 1)            
                            ch_e "Too saccharine, [EmmaX.Petname]."
                            
                    "I think I'll call you \"sexy\".":
                        $ EmmaX.Pet = "sexy"
                        if "lover" in EmmaX.Petnames or ApprovalCheck(EmmaX, 900):
                            $ EmmaX.FaceChange("sexy", 1) 
                            ch_e "I can't argue there, [EmmaX.Petname]."
                        else:        
                            $ EmmaX.FaceChange("angry", 1)         
                            ch_e "That may be a bit much, [EmmaX.Petname]."  
                            
                    "I think I'll call you \"lover\".":
                        $ EmmaX.Pet = "lover"
                        if "lover" in EmmaX.Petnames or ApprovalCheck(EmmaX, 900, "L"):
                            $ EmmaX.FaceChange("sexy", 1) 
                            ch_e "I do love you, [EmmaX.Petname]!"
                        else:      
                            $ EmmaX.FaceChange("angry", 1)           
                            ch_e "Not in this lifetime, [EmmaX.Petname]."  
                        
                    "Back":
                        pass
            
            "Risky":
                menu:                        
                    "I think I'll call you \"slave\".":
                        $ EmmaX.Pet = "slave"
                        if "master" in EmmaX.Petnames or ApprovalCheck(EmmaX, 900, "O"):
                            $ EmmaX.FaceChange("bemused", 1) 
                            ch_e "As you wish, [EmmaX.Petname]."
                        else:      
                            $ EmmaX.FaceChange("angry", 1)           
                            ch_e "I'm no man's slave, [EmmaX.Petname]."
                                            
                    "I think I'll call you \"pet\".":
                        $ EmmaX.Pet = "pet"
                        if "master" in EmmaX.Petnames or ApprovalCheck(EmmaX, 600, "O"):
                            $ EmmaX.FaceChange("bemused", 1) 
                            ch_e "So long as you make sure to pet me, [EmmaX.Petname]."
                        else:             
                            $ EmmaX.FaceChange("angry", 1)    
                            ch_e "I doubt you'd want me for a pet, [EmmaX.Petname]."
                            
                    "I think I'll call you \"slut\".":
                        $ EmmaX.Pet = "slut"
                        if "sex friend" in EmmaX.Petnames or ApprovalCheck(EmmaX, 1000, "OI"):
                            $ EmmaX.FaceChange("sexy") 
                            ch_e "I cant exactly disagree, [EmmaX.Petname]."
                        else:                
                            $ EmmaX.FaceChange("angry", 1) 
                            $ EmmaX.Mouth = "surprised"
                            ch_e "I would strongly reconsider that." 
                            
                    "I think I'll call you \"whore\".":
                        $ EmmaX.Pet = "whore"
                        if "fuckbuddy" in EmmaX.Petnames or ApprovalCheck(EmmaX, 1100, "OI"):
                            $ EmmaX.FaceChange("sly") 
                            ch_e "Only for you though. . ."
                        else:        
                            $ EmmaX.FaceChange("angry", 1)         
                            ch_e "The last man to call me that no longer remembers his own name." 
                                                   
                    "I think I'll call you \"sugartits\".":
                        $ EmmaX.Pet = "sugartits"
                        if "sex friend" in EmmaX.Petnames or ApprovalCheck(EmmaX, 1400):
                            $ EmmaX.FaceChange("sly", 1) 
                            ch_e "They certainly are sweet. . ."
                        else:     
                            $ EmmaX.FaceChange("angry", 1)            
                            ch_e "I expect you're better than that, [EmmaX.Petname]." 
                            
                    "I think I'll call you \"sex friend\".":
                        $ EmmaX.Pet = "sex friend"
                        if "sex friend" in EmmaX.Petnames or ApprovalCheck(EmmaX, 600, "I"):
                            $ EmmaX.FaceChange("sly") 
                            ch_e "Hm?"
                        else:                
                            $ EmmaX.FaceChange("angry", 1) 
                            ch_e "Hopefully not in public, [EmmaX.Petname]." 
                            
                    "I think I'll call you \"fuckbuddy\".":
                        $ EmmaX.Pet = "fuckbuddy"
                        if "fuckbuddy" in EmmaX.Petnames or ApprovalCheck(EmmaX, 700, "I"):
                            $ EmmaX.FaceChange("bemused") 
                            ch_e "Well. . . alright."
                        else:                
                            $ EmmaX.FaceChange("angry", 1)
                            $ EmmaX.Mouth = "surprised"
                            ch_e "How crass." 
                        
                    "I think I'll call you \"baby girl\".":
                        $ EmmaX.Pet = "baby girl"
                        if "daddy" in EmmaX.Petnames or ApprovalCheck(EmmaX, 1200):
                            $ EmmaX.FaceChange("smile", 1) 
                            ch_e "Adorable."
                        else:                
                            $ EmmaX.FaceChange("angry", 1) 
                            ch_e "A bit inappropriate." 
                    
                    "I think I'll call you \"mommy\".":
                        $ EmmaX.Pet = "mommy"
                        if "mommy" in EmmaX.Pets or ApprovalCheck(EmmaX, 1500):
                            $ EmmaX.FaceChange("sly", 1, Mouth="kiss") 
                            ch_e "Oooh, [EmmaX.Petname]."
                        else:     
                            $ EmmaX.FaceChange("angry")            
                            ch_e "That's a bit much, [EmmaX.Petname]" 
                            
                    "Back":
                        pass
                    
            "Nevermind.":
                return
    return
    
#label Emma_Namecheck(EmmaX.Pet = EmmaX.Pet, Cnt = 0, Ugh = 0):#$ Girl.NameCheck() #checks reaction to petname
   
# start Emma_Rename//////////////////////////////////////////////////////////
label Emma_Rename:  
        #Sets alternate names from Emma
        $ EmmaX.Mouth = "smile"
        ch_e "Yes, and?"
        menu:
            extend ""
            "I think \"Emma's\" a pretty name." if EmmaX.Name != "Emma" and "Emma" in EmmaX.Names:
                    $ EmmaX.Name = "Emma"
                    ch_e "I've always been fond of it. . ."
            "I thought \"Ms. Frost\" sounded cool." if EmmaX.Name != "Ms. Frost" and "Ms. Frost" in EmmaX.Names:
                    $ EmmaX.Name = "Ms. Frost"
                    if ApprovalCheck(EmmaX, 1000, "LI"):
                            $ EmmaX.FaceChange("sly", 1) 
                            if "namechange" not in EmmaX.DailyActions:
                                    $ EmmaX.Statup("Obed", 70, 2)
                                    $ EmmaX.Statup("Inbt", 70, 3)   
                            ch_e "Naughty boy. . ."                        
                    else:
                            ch_e "I suppose we could keep things professional. . ."
            "I liked the sound of \"White Queen.\"" if EmmaX.Name != "White Queen" and "White Queen" in EmmaX.Names:   
                    $ EmmaX.Name = "White Queen"                         
                    if not ApprovalCheck(EmmaX, 500, "I"):
                            $ EmmaX.FaceChange("confused") 
                            ch_e "Where have you heard that-"
                            $ EmmaX.FaceChange("sly", 2) 
                            if "namechange" not in EmmaX.DailyActions:
                                    $ EmmaX.Statup("Love", 80, 2)   
                                    $ EmmaX.Statup("Obed", 70, 2)  
                                    $ EmmaX.Statup("Inbt", 80, 3)
                            ch_e "Oh, you dirty, dirty boy. . ."                        
                    else:
                            $ EmmaX.FaceChange("confused") 
                            ch_e "Oh, well, I suppose. . ."
                    $ EmmaX.FaceChange() 
            "Nevermind.":
                    pass
        $ EmmaX.AddWord(1,0,"namechange")
        return
# end Emma_Rename//////////////////////////////////////////////////////////

# start Emma_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Emma_Personality(Cnt = 0):   
    if not EmmaX.Chat[4] or Cnt:
        "Since you're doing well in one area, you can convince Emma to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_e "Sure, what's up?"
        "More Obedient. [[Love to Obedience]" if EmmaX.Love > 900:
            ch_p "If you really love me, could you please just do what I say?"
            ch_e "Anything to humor you, [EmmaX.Petname]."
            $ EmmaX.Chat[4] = 1
        "Less Inhibited. [[Love to Inhibition]" if EmmaX.Love > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_e "I don't see how I could be {i}less{/i} inhibited, but I can certainly try."
            $ EmmaX.Chat[4] = 2
        
        "Less Inhibited. [[Obedience to Inhibition]" if EmmaX.Obed > 900:
            ch_p "I want you to be less inhibited."
            ch_e "If you say so."
            $ EmmaX.Chat[4] = 3
        "More Loving. [[Obedience to Love]" if EmmaX.Obed > 900:
            ch_p "I'd like you to learn to love me."
            ch_e "I'll try to."
            $ EmmaX.Chat[4] = 4
            
        "More Obedient. [[Inhibition to Obedience]" if EmmaX.Inbt > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_e "Does that get you off?"
            $ EmmaX.Chat[4] = 5
            
        "More Loving. [[Inhibition to Love]" if EmmaX.Inbt > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_e "We do have fun. . ."
            $ EmmaX.Chat[4] = 6
            
        "I guess just do what you like. . .[[reset]" if EmmaX.Chat[4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_e "As if I ever do anything else?"
            $ EmmaX.Chat[4] = 0
        "Repeat the rules":
            $ Cnt = 1
            jump Emma_Personality
        "Nevermind.":
            return
    return
# end Emma_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Emma_Summon / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Emma_Summon(Tempmod=Tempmod):
    $ EmmaX.OutfitChange()  
    if "no summon" in EmmaX.RecentActions:
                if "angry" in EmmaX.RecentActions:
                    ch_e "I'm not in the mood for this, [EmmaX.Petname]."
                elif EmmaX.RecentActions.count("no summon") > 1:
                    ch_e "You heard me the first time."
                    $ EmmaX.RecentActions.append("angry") 
                elif Current_Time == "Night": 
                    ch_e "It's past your bedtime."
                else:
                    ch_e "As I said, I've got things to do."   
                $ EmmaX.RecentActions.append("no summon")
                return
                    
    $ D20 = renpy.random.randint(1, 20) 
    $ Line = 0
    if EmmaX.Loc == "bg teacher": #fix change these if changed function
        $ Tempmod = -30
    elif EmmaX.Loc == "bg classroom":
        $ Tempmod = -10
    elif EmmaX.Loc == "bg dangerroom":    
        $ Tempmod = -10
    elif EmmaX.Loc == "bg showerroom":    
        $ Tempmod = -30
        
    if D20 <= 3:                                                                        
        #unlucky refusal
        $ Line = "no"     
    if Current_Time == "Night": 
                if ApprovalCheck(EmmaX, 700, "L") or ApprovalCheck(EmmaX, 300, "O"):                              
                        #It's night time but she likes you.
                        ch_e "It's getting late, but fine, what did you want?"
                        $ EmmaX.Loc = bg_current 
                        call Set_The_Scene
                else:                                                           
                        #It's night time and she isn't into you
                        ch_e "It's late, [EmmaX.Petname], tell me tomorrow."       
                        $ EmmaX.RecentActions.append("no summon")         
                return
    elif "les" in EmmaX.RecentActions:
            #if she's with another girl. . .
            if ApprovalCheck(EmmaX, 2000):
                    ch_e "I'm. . . entertaining at the moment, [EmmaX.Petname], care to join us?"
                    menu:
                        extend ""
                        "Sure":
                            $ Line = "go to"
                        "No thanks.":
                            ch_e "Your loss."
                            return
            else:            
                    ch_e "Oh. . . that might be an issue, we're- I'm. . ."
                    ch_e "indisposed. . ."
                    ch_e "Perhaps we could meet later."      
                    $ EmmaX.RecentActions.append("no summon") 
                    return       
    elif not ApprovalCheck(EmmaX, 700, "L") or not ApprovalCheck(EmmaX, 600, "O"):                       
        #It's not night time, but she's busy 
        if not ApprovalCheck(EmmaX, 300):
                ch_e "I don't really feel up to that, [EmmaX.Petname]."       
                $ EmmaX.RecentActions.append("no summon")         
                return    
            
            
        if "summoned" in EmmaX.RecentActions:
                pass
        elif "goto" in EmmaX.RecentActions:
                ch_e "You only just left, why not return?"
        elif EmmaX.Loc == "bg classroom" or EmmaX.Loc == "bg teacher":
                ch_e "You can find me in the class room, [EmmaX.Petname]."
        elif EmmaX.Loc == "bg dangerroom": 
                ch_e "I'm getting some training in, [EmmaX.Petname], care to join me?"    
        elif EmmaX.Loc == "bg campus": 
                ch_e "I'm relaxing in the square, if you'd care to join me." 
        elif EmmaX.Loc == "bg emma": 
                ch_e "I'm in my room, [EmmaX.Petname]." 
        elif EmmaX.Loc == "bg player": 
                ch_e "I'm waiting in your room, [EmmaX.Petname]. . ."   
        elif EmmaX.Loc == "bg showerroom":    
            if ApprovalCheck(EmmaX, 1600):
                ch_e "I'm in the shower right now, [EmmaX.Petname], do you need an invitation?"
            else:            
                ch_e "I'm in the shower right now, [EmmaX.Petname], perhaps I'll see you later."       
                $ EmmaX.RecentActions.append("no summon")         
                return      
        elif EmmaX.Loc == "hold":
                ch_e "I'm off campus for a bit, I'll be back later."       
                $ EmmaX.RecentActions.append("no summon") 
                return      
        else:        
                ch_e "You could always come over here, [EmmaX.Petname]."    
           
           
        if "summoned" in EmmaX.RecentActions:
            ch_e "Again? Very well."           
            $ Line = "yes"            
        elif "goto" in EmmaX.RecentActions:
            menu:
                extend ""
                "You're right, be right back.":
                                ch_e "I'll be waiting."
                                $ Line = "go to"                    
                "Nah, it's better here.":    
                                ch_e "Very well."                    
                "But I'd {i}really{/i} like to see you over here.":
                        if ApprovalCheck(EmmaX, 600, "L") or ApprovalCheck(EmmaX, 1400):
                                $ Line = "lonely"
                        else: 
                                $ Line = "no"                        
                "I said come over here.":
                        if ApprovalCheck(EmmaX, 600, "O"):                                    
                                #she is obedient
                                $ Line = "command"                        
                        elif D20 >= 7 and ApprovalCheck(EmmaX, 1400):                         
                                #she is generally favorable 
                                ch_e "Hmm, very well."              
                                $ Line = "yes"                        
                        elif ApprovalCheck(EmmaX, 200, "O"):                                  
                                #she is not obedient  
                                ch_e "If you're lucky, I'll still be here when you arrive."    
                        else:                                                                   
                                #she is obedient, but you failed to meet the checks                     
                                $ Line = "no" 
        else:  
            menu:
                extend ""
                "Sure, I'll be right there.":
                    $ EmmaX.Statup("Love", 55, 1) 
                    $ EmmaX.Statup("Inbt", 30, 1)
                    ch_e "I'll be waiting."
                    $ Line = "go to"
                    
                "Nah, we can talk later.":
                    $ EmmaX.Statup("Obed", 50, 1)                            
                    $ EmmaX.Statup("Obed", 30, 2)
                    ch_e "Very well."
                    
                "Could you please come visit me? I'm lonely.":
                    if ApprovalCheck(EmmaX, 600, "L") or ApprovalCheck(EmmaX, 1400):
                        $ EmmaX.Statup("Love", 70, 1)                   
                        $ EmmaX.Statup("Obed", 50, 1)
                        $ Line = "lonely"
                    else: 
                        $ EmmaX.Statup("Inbt", 30, 1)
                        $ Line = "no"
                        
                "I said come over here.":
                    if ApprovalCheck(EmmaX, 600, "O"):                              
                        #she is obedient
                        $ EmmaX.Statup("Love", 50, 1, 1)    
                        $ EmmaX.Statup("Love", 40, -1)                
                        $ EmmaX.Statup("Obed", 90, 1)    
                        $ Line = "command"
                        
                    elif D20 >= 7 and ApprovalCheck(EmmaX, 1400):       
                        #she is generally favorable
                        $ EmmaX.Statup("Love", 70, -2)  
                        $ EmmaX.Statup("Love", 90, -1)  
                        $ EmmaX.Statup("Obed", 50, 2)                                
                        $ EmmaX.Statup("Obed", 90, 1)  
                        ch_e "Ok, fine, [EmmaX.Petname]."              
                        $ Line = "yes"
                        
                    elif ApprovalCheck(EmmaX, 200, "O"):                                         
                        #she is not obedient   
                        $ EmmaX.Statup("Love", 70, -4)  
                        $ EmmaX.Statup("Love", 90, -2)   
                        ch_e "Who do you think is in charge here?!"                             
                        $ EmmaX.Statup("Inbt", 40, 2)
                        $ EmmaX.Statup("Inbt", 60, 1)    
                        $ EmmaX.Statup("Obed", 70, -2)
                        ch_e "You'd better hope you don't find me here."                    
                    else:                                                                   
                        #she is obedient, but you failed to meet the checks
                        $ EmmaX.Statup("Inbt", 30, 1)
                        $ EmmaX.Statup("Inbt", 50, 1)                                    
                        $ EmmaX.Statup("Love", 50, -1, 1)
                        $ EmmaX.Statup("Obed", 70, -1)  
                        $ Line = "no" 
                    #end "ordered"
    else:                                                                               
        #automatic acceptance
        if EmmaX.Love > EmmaX.Obed:
            ch_e "I'd love to."
        else:
            ch_e "I'll be right there, [EmmaX.Petname]."
        $ Line = "yes" 
        
    $ Tempmod = 0
    
    if not Line:                                                                        
            #You end the dialog neutrally               
            $ EmmaX.RecentActions.append("no summon")         
            return
        
    if Line == "no":                                                                    
            # She's refused, context based dialog
            if EmmaX.Loc == "bg teacher":
                ch_e "I can't exactly leave class, [EmmaX.Petname]." 
            elif EmmaX.Loc == "bg classroom":
                ch_e "I have a lot of paperwork, [EmmaX.Petname]." 
            elif EmmaX.Loc == "bg dangerroom": 
                ch_e "I'm just getting warmed up here."
            else:
                ch_e "I have a lot to finish up here."          
            $ EmmaX.RecentActions.append("no summon")         
            return
        
    elif Line == "go to":                                                                 
            #You agreed to go to her instead        
            $ renpy.pop_call()
            $ Tempmod = 0
            $ EmmaX.RecentActions.append("goto")  
            $ Player.RecentActions.append("goto")  
            if EmmaX.Loc == "bg classroom" or EmmaX.Loc == "bg teacher":
                    ch_e "You don't want to miss too much."
                    jump Class_Room 
            elif EmmaX.Loc == "bg dangerroom": 
                    ch_e "I'll try to save some for you."
                    jump Danger_Room
            elif EmmaX.Loc == "bg emma": 
                    ch_e "I'll tidy up a few things."
                    jump Emma_Room
            elif EmmaX.Loc == "bg player": 
                    ch_e "I'll be waiting for you."
                    jump Player_Room                
            elif EmmaX.Loc == "bg showerroom": 
                    ch_e "Don't keep me waiting. . ."
                    jump Shower_Room
            elif EmmaX.Loc == "bg campus": 
                    ch_e "I've got a nice location picked out."
                    jump Campus
            elif EmmaX.Loc == "bg rogue": 
                    ch_e "I'll try to keep occupied."
                    jump Rogue_Room
            elif EmmaX.Loc == "bg kitty": 
                    ch_e "I'll try to keep occupied."
                    jump Kitty_Room
            elif EmmaX.Loc == "bg laura": 
                    ch_e "I'll try to keep occupied."
                    jump Laura_Room
            else:
                    ch_e "You know, I'll just meet you in my room."
                    $ EmmaX.Loc = "bg emma"
                    jump Emma_Room
            
    #She's agreed to come over    
    elif Line == "lonely":
            ch_e "Well, we can't have that now."
    elif Line == "command": 
            ch_e "If I must. . ."
        
    $ EmmaX.RecentActions.append("summoned")  
    $ Line = 0
    ch_e "I'll be there in a minute."   
    if "locked" in Player.Traits:
            call Locked_Door(EmmaX)
            return
    $ EmmaX.Loc = bg_current 
    call Taboo_Level(0)
    $ EmmaX.OutfitChange()
    call Set_The_Scene
    return

# End Emma Summon  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 


label Emma_Leave(Tempmod=Tempmod, GirlsNum = 0):        
    if "leaving" in EmmaX.RecentActions:
        $ EmmaX.DrainWord("leaving")
    else:
        return
    
    if EmmaX.Loc == "hold":   
            # Activates if she's being moved out of play
            ch_e "Sorry, I have some business to attend to." 
            return
            
    if EmmaX in Party or "lockedtravels" in EmmaX.Traits:           
            #If she's in your party or if you've told her not to leave you
            #It resets her to your location
            $ EmmaX.Loc = bg_current 
            return
      
    elif "freetravels" in EmmaX.Traits or not ApprovalCheck(EmmaX, 700):
            #If you've told her to go wherever, or she just doesn't care what you think.   
            $ EmmaX.OutfitChange()           
            if GirlsNum: #if someone left before her
                        ch_e "I have to head out as well."
                        
            if EmmaX.Loc == "bg teacher":
                        ch_e "I have a class to teach."
            elif EmmaX.Loc == "bg classroom":
                        ch_e "I have some paperwork to take care of."
            elif EmmaX.Loc == "bg dangerroom": 
                        ch_e "I have a workout scheduled."   
            elif EmmaX.Loc == "bg campus": 
                        ch_e "I'm going to take in some sun." 
            elif EmmaX.Loc == "bg emma": 
                        ch_e "I'm heading back to my room." 
            elif EmmaX.Loc == "bg player": 
                        ch_e "I'll be heading to your room."   
            elif EmmaX.Loc == "bg showerroom" and ApprovalCheck(EmmaX, 1400):
                        ch_e "I'm going to take a quick shower."  
            elif EmmaX.Loc == "bg pool": 
                        ch_e "I was heading for a swim."               
            else:        
                        ch_e "I'll see you later."                  
            hide Emma_Sprite
            return     
            #End Free Travels
    
    if bg_current == "bg dangerroom":   
            call Gym_Clothes("exit")
            
    $ EmmaX.OutfitChange()
    
    if "follow" not in EmmaX.Traits:
            # Sets a key to show that she's asked you to follow her at least once
            $ EmmaX.Traits.append("follow")   
        
    $ D20 = renpy.random.randint(1, 20) 
    $ Line = 0
    # Sets her preferences
    if EmmaX.Loc == "bg teacher": #fix change these if changed function
        $ Tempmod = -40
    elif EmmaX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = -10
    elif EmmaX.Loc == "bg dangerroom":    
        $ Tempmod = 20
    elif EmmaX.Loc == "bg showerroom":    
        $ Tempmod = 20
    
    
    if GirlsNum: #if someone left before her
                ch_e "I'm leaving as well."
                
    if EmmaX.Loc == "bg teacher":
        ch_e "I've got a class to teach, but you could probably learn a thing or two from it."
    elif EmmaX.Loc == "bg classroom":
        ch_e "I have some paperwork to take care of, but you could keep me company."
    elif EmmaX.Loc == "bg dangerroom": 
        ch_e "I have a workout planned, but there's room for one more."    
    elif EmmaX.Loc == "bg campus": 
        ch_e "I'm planning to get some sunning in, care to join me?" 
    elif EmmaX.Loc == "bg emma": 
        ch_e "I'm heading back to my room, but you can walk me back." 
    elif EmmaX.Loc == "bg player": 
        ch_e "I'm actually heading to your room, [EmmaX.Petname]."   
    elif EmmaX.Loc == "bg showerroom":    
        if ApprovalCheck(EmmaX, 1600):
            ch_e "I'm catching a quick shower, care to join me?"
        else:            
            ch_e "I'm headed for the showers, make sure to keep your distance."
            return      
    elif EmmaX.Loc == "bg pool": 
                ch_e "I was heading for a swim. Care to join me?" 
    else:        
        ch_e "Would you care to come with me?"    
    
    
    menu:
        extend ""
        "Sure, I'll catch up.":
                if "followed" not in EmmaX.RecentActions:
                    $ EmmaX.Statup("Love", 55, 1) 
                    $ EmmaX.Statup("Inbt", 30, 1)
                $ Line = "go to"
            
        "Nah, we can talk later.":
                if "followed" not in EmmaX.RecentActions:
                    $ EmmaX.Statup("Obed", 50, 1)                            
                    $ EmmaX.Statup("Obed", 30, 2)
                ch_e "Very well, I'll talk to you later."
            
        "Could you please stay with me? I'll get lonely.":
                if ApprovalCheck(EmmaX, 600, "L") or ApprovalCheck(EmmaX, 1400):                
                    if "followed" not in EmmaX.RecentActions:
                        $ EmmaX.Statup("Love", 70, 1)                   
                        $ EmmaX.Statup("Obed", 50, 1)
                    $ Line = "lonely"
                else: 
                    if "followed" not in EmmaX.RecentActions:
                        $ EmmaX.Statup("Inbt", 30, 1)
                    $ Line = "no"
                
        "No, stay here.":
                if ApprovalCheck(EmmaX, 600, "O"):                              
                    #she is obedient
                    if "followed" not in EmmaX.RecentActions:
                        if EmmaX.Love >= 50:
                            $ EmmaX.Statup("Love", 90, 1)    
                        $ EmmaX.Statup("Love", 40, -1)                
                        $ EmmaX.Statup("Obed", 90, 1)    
                    $ Line = "command"
                    
                elif D20 >= 7 and ApprovalCheck(EmmaX, 1400):       
                    #she is generally favorable
                    if "followed" not in EmmaX.RecentActions:
                        $ EmmaX.Statup("Love", 70, -2)  
                        $ EmmaX.Statup("Love", 90, -1)  
                        $ EmmaX.Statup("Obed", 50, 2)                                
                        $ EmmaX.Statup("Obed", 90, 1)  
                    ch_e "I guess it wasn't that important. . ."              
                    $ Line = "yes"
                    
                elif ApprovalCheck(EmmaX, 200, "O"):                                         
                    #she is not obedient                   
                    if "followed" not in EmmaX.RecentActions:
                        $ EmmaX.Statup("Love", 70, -4)  
                        $ EmmaX.Statup("Love", 90, -2)   
                    ch_e "Does that work with your little strumpets?"  
                    if "followed" not in EmmaX.RecentActions:                       
                        $ EmmaX.Statup("Inbt", 40, 2)
                        $ EmmaX.Statup("Inbt", 60, 1)    
                        $ EmmaX.Statup("Obed", 70, -2)
                else:                                                                  
                    #she is obedient, but you failed to meet the checks                  
                    if "followed" not in EmmaX.RecentActions:
                        $ EmmaX.Statup("Inbt", 30, 1)
                        $ EmmaX.Statup("Inbt", 50, 1)                                    
                        $ EmmaX.Statup("Love", 50, -1, 1)
                        $ EmmaX.Statup("Obed", 70, -1)  
                    $ Line = "no" 
                #End ordered to stay
                    
    call Taboo_Level(0)
    $ EmmaX.RecentActions.append("followed")     
    if not Line:                                                                        
            #You end the dialog neutrally      
            hide Emma_Sprite
            call Gym_Clothes("change", [EmmaX])
            return
    
    if Line == "no":                                                                    
            # She's refused, context based dialog
            if EmmaX.Loc == "bg teacher":
                ch_e "I'm not \"cutting class,\" [EmmaX.Petname]." 
            elif EmmaX.Loc == "bg classroom":
                ch_e "I'm afraid not, [EmmaX.Petname], I need to get this work done." 
            elif EmmaX.Loc == "bg dangerroom": 
                ch_e "I'm sorry, but how do you think I keep this figure?"
            else:
                ch_e "I'm sorry, I'm just much too busy at the moment."         
            hide Emma_Sprite
            call Gym_Clothes("change", [EmmaX])         
            return
        
    elif Line == "go to":                                                                 
            #You agreed to go to her instead  
            $ Tempmod = 0
            call DrainAll("leaving")
            call DrainAll("arriving")       
            hide Emma_Sprite
            call Gym_Clothes("change", [EmmaX])
            if EmmaX.Loc == "bg teacher":
                ch_e "I'll see you there."            
                jump Class_Room_Entry
            elif EmmaX.Loc == "bg classroom":
                ch_e "Excellent, that should pass the time."            
                jump Class_Room_Entry
            elif EmmaX.Loc == "bg dangerroom": 
                ch_e "I'll try to leave some for you."
                jump Danger_Room_Entry
            elif EmmaX.Loc == "bg emma": 
                ch_e "I'll be waiting."
                jump Emma_Room
            elif EmmaX.Loc == "bg player": 
                ch_e "I'll be waiting."
                jump Player_Room                
            elif EmmaX.Loc == "bg showerroom": 
                ch_e "I'll get started."
                jump Shower_Room_Entry
            elif EmmaX.Loc == "bg campus": 
                ch_e "Ok, let's."
                jump Campus_Entry
            elif EmmaX.Loc == "bg pool": 
                ch_e "Ok, let's."
                jump Pool_Entry
            else:     
                ch_e "You know, I'll just meet you in my room."
                $ EmmaX.Loc = "bg emma"
                jump Emma_Room
            #End "goto" where she's at
            
    #She's agreed to come over    
    elif Line == "lonely":
            ch_e "Well we wouldn't want that. . ."
    elif Line == "command": 
            ch_e "If you insist."
    
    $ Line = 0
    ch_e "I suppose I can stay for a while."                                
    $ EmmaX.Loc = bg_current 
    return

# End Emma Leave / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

   
## Emma's Clothes // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // //
label Emma_Clothes(Public=0,Bonus=0):   
    if EmmaX.Taboo:                        
            if "exhibitionist" in EmmaX.Traits:
                ch_e "Mmmmm. . ."  
            elif ApprovalCheck(EmmaX, 900, TabM=4) or ApprovalCheck(EmmaX, 400, "I", TabM=3): 
                ch_e "This isn't really the appropriate place for it, however. . ."
                return #alter to be conditional
            else:
                ch_e "I'd rather discuss that in private."
                return
    elif ApprovalCheck(EmmaX, 900, TabM=4) or ApprovalCheck(EmmaX, 600, "L") or ApprovalCheck(EmmaX, 300, "O"):
        ch_e "What about my style?"
    else:
        ch_e "I'll let you know when I care what you think."
        return
              
    if Girl != EmmaX:
            #This culls returns if sent from another girl
            $ renpy.pop_call()     
    $ Girl = EmmaX   
    call Shift_Focus(Girl)
    
    if "exhibitionist" in EmmaX.Traits:
            $ Public += 1
    if EmmaX.Rep <= 200:
            $ Public += 2
    elif EmmaX.Rep <= 400:
            $ Public += 1        
    if "public" in EmmaX.History:
            $ Public += 2
    #This is a trait for if she's open to being sexy in public
        
label Emma_Wardrobe_Menu: 
    $ Trigger = 1 # to prevent Focus swapping. . .   
    $ EmmaX.FaceChange()
    while True:
        menu:
            ch_e "You wanted to discuss my clothing choices?"   
            "Overshirts":
                        call Emma_Clothes_Over        
            "Legwear":
                        call Emma_Clothes_Legs
            "Underwear":
                        call Emma_Clothes_Under
            "Accessories":
                        call Emma_Clothes_Misc
            "Outfits":
                        call Emma_Clothes_Outfits    
            "Let's talk about what you wear around.":
                        call Clothes_Schedule(EmmaX)   
                        
            "Could I get a look at it?" if EmmaX.Loc != bg_current:
                    # checks to see if she'll drop the screen
                    call OutfitShame(EmmaX,0,2) 
                    if _return:                    
                        show PhoneSex zorder 150
                        ch_e "Ok, a quick shot for you. . ."
                    hide PhoneSex
                        
            "Could I get a look at it?" if renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    call OutfitShame(EmmaX,0,2) 
                    if _return:
                        hide DressScreen
            "Would you be more comfortable behind a screen? (locked)" if EmmaX.Taboo:
                    pass
            "Would you be more comfortable behind a screen?" if EmmaX.Loc == bg_current and not EmmaX.Taboo and not renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    if ApprovalCheck(EmmaX, 1500) or (EmmaX.SeenChest and EmmaX.SeenPussy):
                            ch_e "Oh, I think we can handle this."
                    else:
                            show DressScreen zorder 150
                            ch_e "Yes, this will be more comfortable."
                            
            "Switch to. . .":   
                    if renpy.showing('DressScreen'):
                            call OutfitShame(EmmaX,0,2) 
                            if _return:
                                hide DressScreen
                            else:
                                $ EmmaX.OutfitChange() 
                    $ EmmaX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ Trigger = 0
                    call Switch_Chat
                    if Girl != EmmaX:
                            ch_p "I wanted to talk about your clothes."
                            call expression Girl.Tag +"_Clothes"
                    $ Girl = EmmaX
                    call Shift_Focus(Girl)                
            "Never mind, you look good like that.":
                    if "wardrobe" not in EmmaX.RecentActions: 
                            #Apply stat boosts only if it's the first time this turn 
                            if EmmaX.Chat[1] <= 1:                
                                    $ EmmaX.Statup("Love", 70, 15)
                                    $ EmmaX.Statup("Obed", 40, 20)
                                    ch_e "I thought so as well."
                            elif EmmaX.Chat[1] <= 10:
                                    $ EmmaX.Statup("Love", 70, 5)
                                    $ EmmaX.Statup("Obed", 40, 7)
                                    ch_e "Isn't it?" 
                            elif EmmaX.Chat[1] <= 50:
                                    $ EmmaX.Statup("Love", 70, 1)
                                    $ EmmaX.Statup("Obed", 40, 1) 
                            $ EmmaX.RecentActions.append("wardrobe") 
                    if renpy.showing('DressScreen'):
                            call OutfitShame(EmmaX,0,2) 
                            if _return:
                                hide DressScreen
                            else:
                                $ EmmaX.OutfitChange() 
                    $ EmmaX.Set_Temp_Outfit() #sets current outfit as temporary          
                    $ EmmaX.Chat[1] += 1              
                    $ Trigger = 0      
                    return
                          
        #Loops back up      
        #return #jump Emma_Clothes
        #End of Emma Wardrobe Main Menu
        
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Emma_Clothes_Outfits:                                                                                 
        # Outfits
        "You should remember that one. [[Set Custom]":
                menu:
                    "Which slot would you like this saved in?"
                    "Custom 1":
                                call OutfitShame(EmmaX,3,1)
                    "Custom 2":
                                call OutfitShame(EmmaX,5,1)
                    "Custom 3":
                                call OutfitShame(EmmaX,6,1)
                    "Gym Clothes":
                                call OutfitShame(EmmaX,4,1)
                    "Sleepwear":
                                call OutfitShame(EmmaX,7,1)
                    "Swimwear":
                                call OutfitShame(EmmaX,10,1)
                    "Never mind":
                                pass       
        "I really like that teacher's look you wear.": 
                $ EmmaX.OutfitChange("casual1")   
                menu:
                    "You should wear this one out. [[set current outfit]":
                        $ EmmaX.Outfit = "casual1"
                        $ EmmaX.Shame = 0
                        ch_e "Yes, a very tasteful look."
                    "Let's try something else though.":
                        ch_e "Very well."            
                    
        "That combat uniform you have looks really nice on you.":
                $ EmmaX.OutfitChange("casual2")
                menu:
                    "You should wear this one out. [[set current outfit]":
                        $ EmmaX.Outfit = "casual2"
                        $ EmmaX.Shame = 0
                        ch_e "I really enjoyed wearing that one."
                    "Let's try something else though.":
                        ch_e "Very well."            
                    
        "Remember that outfit we put together? [[Set a custom outfit] (locked)" if not EmmaX.Custom1[0] and not EmmaX.Custom2[0] and not EmmaX.Custom3[0]:
                        pass       
                        
        "Remember that outfit we put together?" if EmmaX.Custom1[0] or EmmaX.Custom2[0] or EmmaX.Custom3[0]: 
                $ Cnt = 0
                while 1:
                    menu:                
                        "Throw on Custom 1 (locked)" if not EmmaX.Custom1[0]:
                                pass
                        "Throw on Custom 1" if EmmaX.Custom1[0]:
                                $ EmmaX.OutfitChange("custom1")
                                $ Cnt = 3
                        "Throw on Custom 2 (locked)" if not EmmaX.Custom2[0]:
                                pass
                        "Throw on Custom 2" if EmmaX.Custom2[0]:
                                $ EmmaX.OutfitChange("custom2")
                                $ Cnt = 5
                        "Throw on Custom 3 (locked)" if not EmmaX.Custom3[0]:
                                pass
                        "Throw on Custom 3" if EmmaX.Custom3[0]:
                                $ EmmaX.OutfitChange("custom3")
                                $ Cnt = 6
                        
                        "You should wear this one in private. (locked)" if not Cnt:
                                pass
                        "You should wear this one in private." if Cnt:
                                if Cnt == 5:
                                    $ EmmaX.Clothing[9] = "custom2"
                                elif Cnt == 6:
                                    $ EmmaX.Clothing[9] = "custom3"
                                else:
                                    $ EmmaX.Clothing[9] = "custom1"
                                ch_e "Ok, sure."
                                                
                        "On second thought, forget about that one outfit. . .":
                                menu:
                                    "Custom 1 [[clear custom 1]" if EmmaX.Custom1[0]:
                                        ch_e "Very well."
                                        $ EmmaX.Custom1[0] = 0
                                    "Custom 1 [[clear custom 1] (locked)" if not EmmaX.Custom1[0]:
                                        pass
                                    "Custom 2 [[clear custom 2]" if EmmaX.Custom2[0]:
                                        ch_e "Very well."
                                        $ EmmaX.Custom2[0] = 0
                                    "Custom 2 [[clear custom 2] (locked)" if not EmmaX.Custom2[0]:
                                        pass
                                    "Custom 3 [[clear custom 3]" if EmmaX.Custom3[0]:
                                        ch_e "Very well."
                                        $ EmmaX.Custom3[0] = 0
                                    "Custom 3 [[clear custom 3] (locked)" if not EmmaX.Custom3[0]:
                                        pass
                                    "Never mind, [[back].":
                                        pass    
                                                   
                        "You should wear this one out. [[choose outfit first](locked)" if not Cnt:
                                pass
                        "You should wear this one out." if Cnt:
                                call Custom_Out(EmmaX,Cnt)
                        "Ok, back to what we were talking about. . .":
                                $ Cnt = 0
                                return #jump Emma_Clothes                    
        
        "Gym Clothes?" if not EmmaX.Taboo or bg_current == "bg dangerroom":
                $ EmmaX.OutfitChange("gym")
            
    
        "Sleepwear?" if not EmmaX.Taboo:
                if ApprovalCheck(EmmaX, 1200):
                        $ EmmaX.OutfitChange("sleep")
                else:
                        call Display_DressScreen(EmmaX)
                        if _return:
                            $ EmmaX.OutfitChange("sleep")
                            
        "Swimwear? (locked)" if (EmmaX.Taboo and bg_current != "bg pool") or not EmmaX.Swim[0]:
                $ EmmaX.OutfitChange("swimwear")   
        "Swimwear?" if (not EmmaX.Taboo or bg_current == "bg pool") and EmmaX.Swim[0]:
                $ EmmaX.OutfitChange("swimwear")
                            
        "Your birthday suit looks really great. . .":                                     
                #Nude
                $ EmmaX.FaceChange("sly", 1)
                $ Line = 0
                if not EmmaX.Chest and not EmmaX.Panties and not EmmaX.Over and not EmmaX.Legs and not EmmaX.Hose:  
                    # if already naked (yes)
                    ch_e "Apparently so. . ."  
                elif EmmaX.SeenChest and EmmaX.SeenPussy and ApprovalCheck(EmmaX, 1200, TabM=(5-Public)):
                    #if you've seen it all and she likes you well enough (yes)
                    ch_e "I'll take that as an invitation. . ."  
                    $ Line = 1
                elif ApprovalCheck(EmmaX, 2000, TabM=(5-Public)):
                    #if you haven't seen everything but she really likes you (yes)
                    ch_e "I suppose you've earned it. . ."    
                    $ Line = 1
                elif EmmaX.SeenChest and EmmaX.SeenPussy and ApprovalCheck(EmmaX, 1200, TabM=0):
                    # if you've seen it but it's in public (no)
                    ch_e "As you're well aware, but this isn't the appropriate venue. . ."  
                elif ApprovalCheck(EmmaX, 2000, TabM=0):
                    #if you haven't seen everything but she really likes you and it's public (no) 
                    ch_e "I assure you it is, but this isn't the appropriate venue. . ."  
                elif ApprovalCheck(EmmaX, 1000, TabM=0):     
                    #if you haven't seen everything and she kinda likes you but it's public (no)
                    $ EmmaX.FaceChange("surprised", 1)
                    ch_e "I assure you that it is, but that's not the way to ask."
                    $ EmmaX.Blush = 0
                else:
                    # if she refuses. (no) 
                    $ EmmaX.FaceChange("angry", 1)
                    ch_e "Not the worst line I've heard."
                    ch_e ". . . but close."
                    
                if Line:                                                            #If she got nude. . .                            
                    $ EmmaX.OutfitChange("nude")
                    "She strips down."
                    call Emma_First_Topless
                    call Emma_First_Bottomless(1)
                    $ EmmaX.FaceChange("sexy")
                    menu:
                        "You know, you should wear this one out. [[set current outfit]":
                            if "exhibitionist" in EmmaX.Traits:
                                $ EmmaX.FaceChange("sexy",2,Eyes="down")
                                ch_e "Mmmmm. . ." 
                                $ EmmaX.Outfit = "nude"
                                $ EmmaX.Statup("Lust", 50, 10) 
                                $ EmmaX.Statup("Lust", 70, 5) 
                                $ EmmaX.Shame = 50
                                $ EmmaX.FaceChange("sexy",1)
                            elif ApprovalCheck(EmmaX, 800, "I") or ApprovalCheck(EmmaX, 2800, TabM=0): 
                                ch_e "Oooh, that would cause quite a stir. . ." 
                                $ EmmaX.Outfit = "nude"
                                $ EmmaX.Shame = 50
                            elif ApprovalCheck(EmmaX, 400, "I") and ApprovalCheck(EmmaX, 1200, TabM=0): 
                                $ EmmaX.FaceChange("bemused", 1,Eyes="side")
                                ch_e "You shouldn't suggest such things. . ."
                            else:
                                $ EmmaX.FaceChange("sexy", 1,Eyes="surprised")
                                ch_e "Impossible." 
                                
                        "Let's try something else though.":
                            if "exhibitionist" in EmmaX.Traits:
                                ch_e "Too much for you to handle?"                         
                            elif ApprovalCheck(EmmaX, 800, "I") or ApprovalCheck(EmmaX, 2800, TabM=0):       
                                $ EmmaX.FaceChange("bemused", 1)             
                                ch_e "Because obviously I couldn't go around like this. . ."
                            else:
                                $ EmmaX.FaceChange("confused", 1)
                                ch_e "So long as it's just the two of us, I don't mind this."   
                $ Line = 0
                            
        "Never mind":    
            return #jump Emma_Clothes     
            
    return #jump Emma_Clothes
    #End of Emma Outfits
            
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Emma_Clothes_Over:                                                                                        
        # Overshirts
        "Why don't you go with no [EmmaX.Over]?" if EmmaX.Over:
                $ EmmaX.FaceChange("bemused", 1)
                if ApprovalCheck(EmmaX, 800, TabM=(3-Public)) and (EmmaX.Chest or EmmaX.SeenChest):
                    ch_e "Certainly."
                elif ApprovalCheck(EmmaX, 600, TabM=0):
                    call Emma_NoBra
                    if not _return:
                        if not ApprovalCheck(EmmaX, 1200):
                            call Display_DressScreen(EmmaX)
                            if not _return:
                                return #jump Emma_Clothes
                        else:
                                return #jump Emma_Clothes                                 
                else:
                    call Display_DressScreen(EmmaX)
                    if not _return:
                            ch_e "I'm afraid not."
                            if not EmmaX.Chest:
                                ch_e "I'm indecent under this. . ."
                            return #jump Emma_Clothes
                $ Line = EmmaX.Over
                $ EmmaX.Over = 0   
                "She shrugs off her [Line]."
                if not EmmaX.Chest and not renpy.showing('DressScreen'):
                        call Emma_First_Topless
            
        "Try on that white jacket you have." if EmmaX.Over != "jacket":
                $ EmmaX.FaceChange("bemused")
                if EmmaX.Chest or EmmaX.SeenChest or ApprovalCheck(EmmaX, 500, TabM=(3-Public)):
                    ch_e "Yeah, ok."          
                else:
                    call Display_DressScreen(EmmaX)
                    if not _return:
                            $ EmmaX.FaceChange("bemused", 1)
                            ch_e "I'm not sure this is appropriate without something more substantial underneath."
                            return #jump Emma_Clothes
                $ EmmaX.Over = "jacket"   
            
        "Try on that lace nighty." if EmmaX.Over != "nighty":
                $ EmmaX.FaceChange("bemused")
                if EmmaX.Chest or EmmaX.SeenChest or ApprovalCheck(EmmaX, 500, TabM=(3-Public)):
                    ch_e "Yeah, ok."          
                else:
                    call Display_DressScreen(EmmaX)
                    if not _return:
                            $ EmmaX.FaceChange("bemused", 1)
                            ch_e "This is a bit shear for this top."
                            return #jump Emma_Clothes
                $ EmmaX.Over = "nighty"   
                            
        "Maybe just throw on a towel?" if EmmaX.Over != "towel":
                $ EmmaX.FaceChange("bemused", 1)
                $ Bonus = 5 if bg_current == "bg showerroom" else 0
                if EmmaX.Chest or (EmmaX.SeenChest and ApprovalCheck(EmmaX, 500, TabM=(3-Public-Bonus))):
                    ch_e "Oh, you like this?"
                elif ApprovalCheck(EmmaX, 1000, TabM=(3-Public-Bonus)):
                    $ EmmaX.FaceChange("perplexed", 1)
                    ch_e "Fine."          
                else:
                    call Display_DressScreen(EmmaX)
                    if not _return:
                            $ EmmaX.FaceChange("bemused", 1)
                            ch_e "This wouldn't leave much to the imagination."
                            return #jump Emma_Clothes
                call Emma_NoBra
                if not _return:
                    return #jump Emma_Clothes
                $ EmmaX.Over = "towel"    
                            
        "Never mind":
                pass
    return #jump Emma_Clothes
    #End of Emma Top
            
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    label Emma_NoBra: #fix test this
        menu:
            ch_e "I'm not wearing much of anything under this. . ."
            "Then you could slip something on under it. . .":   
                        if (EmmaX.SeenChest and ApprovalCheck(EmmaX, 1000, TabM=(4-Public))) or ApprovalCheck(EmmaX, 1200, TabM=(5-Public)):
                                ch_e "-not that I'm overly concerned about it. . ."
                        elif ApprovalCheck(EmmaX, 900, TabM=(3-Public)) and "lace bra" in EmmaX.Inventory:
                                ch_e "I suppose I could."
                                $ EmmaX.Chest  = "lace bra"  
                                "She pulls out her lace bra and slips it on under her [EmmaX.Over]."
#                        elif ApprovalCheck(EmmaX, 800, TabM=(3-Public)):
#                                ch_e "I suppose I could."
#                                $ EmmaX.Chest = "bra"
#                                "She pulls out her bra and slips it on under her [EmmaX.Over]."
                        elif ApprovalCheck(EmmaX, 700, TabM=(3-Public)):
                                ch_e "I suppose I could."
                                $ EmmaX.Chest = "corset"   
                                "She pulls out her corset and slips it on under her [EmmaX.Over]."
                        elif ApprovalCheck(EmmaX, 600, TabM=(3-Public)):
                                ch_e "I suppose I could."
                                $ EmmaX.Chest = "sports bra"
                                "She pulls out her sports bra and slips it on under her [EmmaX.Over]."
                        else:
                                ch_e "Yes, but I'd rather not."
                                return 0
                        
            "You could always just wear nothing at all. . .":
                        if ApprovalCheck(EmmaX, 1100, "LI", TabM=(3-Public)) and EmmaX.Love > EmmaX.Inbt:               
                                ch_e "The things I do for you. . ."
                        elif ApprovalCheck(EmmaX, 700, "OI", TabM=(3-Public)) and EmmaX.Obed > EmmaX.Inbt:
                                ch_e "If that's what you insist. . ."
                        elif ApprovalCheck(EmmaX, 600, "I", TabM=(3-Public)):
                                ch_e "I suppose I could. . ."
                        elif ApprovalCheck(EmmaX, 1300, TabM=(3-Public)):
                                ch_e "Very well."
                        else: 
                                $ EmmaX.FaceChange("surprised")
                                $ EmmaX.Brows = "angry"
                                if EmmaX.Taboo > 20:
                                    ch_e "I'm afraid I couldn't do that in public."
                                else:
                                    ch_e "I could, but I wouldn't."
                                return 0
                                
                    
            "Never mind.":
                        return 0
        return 1
        #End of Emma bra check
       
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Emma_Clothes_Legs:                                                                                                   
        # Leggings    
        "Maybe go without the [EmmaX.Legs]." if EmmaX.Legs:
                $ EmmaX.FaceChange("sexy", 1)
                if EmmaX.SeenPanties and EmmaX.Panties and ApprovalCheck(EmmaX, 500, TabM=(6-Public)):
                    ch_e "Fine."
                elif EmmaX.SeenPussy and ApprovalCheck(EmmaX, 900, TabM=(5-Public)):
                    ch_e "Fine."
                elif ApprovalCheck(EmmaX, 1300, TabM=(2-Public)) and EmmaX.Panties:
                    ch_e "It's not like I haven't worn this look before. . ."
                elif ApprovalCheck(EmmaX, 700) and not EmmaX.Panties:
                    call Emma_NoPantiesOn                        
                    if not _return and not EmmaX.Panties:
                        if not ApprovalCheck(EmmaX, 1500):
                            call Display_DressScreen(EmmaX)
                            if not _return:
                                return #jump Emma_Clothes
                        else:
                                return #jump Emma_Clothes                                
                else:
                    call Display_DressScreen(EmmaX)
                    if not _return:
                        ch_e "I'm afraid not."
                        if not EmmaX.Panties:
                            ch_e "You understand, it could get. . . drafty. . ."
                        return #jump Emma_Clothes
                $ Line = EmmaX.Legs
                $ EmmaX.Legs = 0    
                "She peels her [Line] off."
                $ Line = 0                
                if renpy.showing('DressScreen'):
                    pass
                elif EmmaX.Panties:                
                    $ EmmaX.SeenPanties = 1
                else:
                    call Emma_First_Bottomless
        
        "You look great in those white pants." if EmmaX.Legs != "pants":
                ch_e "I know."
                $ EmmaX.Legs = "pants"
                
        "You look great in that little skirt." if EmmaX.Legs != "skirt":
                ch_e "I agree."
                $ EmmaX.Legs = "skirt"
            
        "You look great in boots." if EmmaX.Acc != "thigh boots":
                ch_e "They do look nice on me."
                $ EmmaX.Acc = "thigh boots"
        "Maybe lose the boots." if EmmaX.Acc == "thigh boots":
                ch_e "I suppose."
                $ EmmaX.Acc = 0
                
        "You look great in yoga pants." if EmmaX.Legs != "yoga pants":
                ch_e "Yeah, ok."
                $ EmmaX.Legs = "yoga pants"
                               
        "Never mind":
                pass
    return #jump Emma_Clothes
    #End of Emma Pants
    
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
    
    label Emma_NoPantiesOn: #fix test this
        $ EmmaX.FaceChange("sexy",Eyes="side")
        ch_e "You should be aware. . ."
        $ EmmaX.FaceChange("sly")
        menu:
            ch_e "I'm not wearing any panties at the moment. . ."
            "Then you could slip on a pair. . .":   
                        if (EmmaX.SeenPussy and ApprovalCheck(EmmaX, 1100, TabM=(5-Public))) or ApprovalCheck(EmmaX, 1500, TabM=(5-Public)):
                                $ EmmaX.Blush = 1
                                ch_e "I didn't say that bothered me. . ."
                                $ EmmaX.Blush = 0                
                        elif ApprovalCheck(EmmaX, 800, TabM=(5-Public)) and "lace panties" in EmmaX.Inventory:
                                ch_e "I like how you think, turn around."
                                $ EmmaX.Panties  = "lace panties"    
                                "She pulls out her lace panties, and with your back turned she removes her pants, and slips her panties on."
                        elif ApprovalCheck(EmmaX, 700, TabM=(5-Public)):
                                ch_e "Yeah, I guess."
                                $ EmmaX.Panties = "white panties"
                                "She pulls out her white panties, and with your back turned she removes her pants, and slips her panties on."                   
                        elif ApprovalCheck(EmmaX, 500, TabM=(6-Public)):
                                ch_e "Yeah, I guess."
                                $ EmmaX.Panties = "sports panties"
                                "She pulls out her sports panties, and with your back turned she removes her pants, and slips her panties on."                   
                        elif EmmaX.Taboo and ApprovalCheck(EmmaX, 800, TabM=0):
                                ch_e "I like how you think, but not in public like this."
                                return 0
                        else:
                                ch_e "I could, but I'd rather not."
                                return 0
                        
            "You could always just wear nothing at all. . .":
                        if ApprovalCheck(EmmaX, 1100, "LI", TabM=(5-Public)) and EmmaX.Love > EmmaX.Inbt:               
                                ch_e "I suppose I could. . ."
                        elif ApprovalCheck(EmmaX, 700, "OI", TabM=(5-Public)) and EmmaX.Obed > EmmaX.Inbt:
                                ch_e "If you'd like. . ."
                        elif ApprovalCheck(EmmaX, 600, "I", TabM=(5-Public)):
                                ch_e "I certainly could. . ."
                        elif ApprovalCheck(EmmaX, 1300, TabM=(5-Public)):
                                ch_e "Very well."
                        else: 
                                $ EmmaX.FaceChange("surprised")
                                $ EmmaX.Brows = "angry"
                                if EmmaX.Taboo > 20:
                                    ch_e "I'm afraid not out here, [EmmaX.Petname]!"
                                else:
                                    ch_e "You wish, [EmmaX.Petname]!"
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
                "How about you lose the [EmmaX.Chest]?" if EmmaX.Chest:
                    $ EmmaX.FaceChange("bemused", 1)
                    if EmmaX.SeenChest and ApprovalCheck(EmmaX, 900, TabM=(4-Public)):
                        ch_e "Of course."    
                    elif ApprovalCheck(EmmaX, 1100, TabM=2):
                        if EmmaX.Taboo:
                            ch_e "I'd rather not out here. . ."
                        else:
                            ch_e "I suppose for you. . ."
                    elif EmmaX.Over == "jacket" and ApprovalCheck(EmmaX, 700, TabM=(3-Public)):
                        ch_e "This is a bit daring without anything under it. . ."  
                    elif not EmmaX.Over:                                         
                        call Display_DressScreen(EmmaX)
                        if not _return:
                            ch_e "I don't think that would be appropriate."
                            return #jump Emma_Clothes                                 
                    else:
                        call Display_DressScreen(EmmaX)
                        if not _return:
                            ch_e "I'm afraid not, [EmmaX.Petname]."
                            return #jump Emma_Clothes                                 
                    $ Line = EmmaX.Chest
                    $ EmmaX.Chest = 0
                    if EmmaX.Over:
                        "She reaches under her [EmmaX.Over] grabs her [Line], and pulls it out, dropping it to the ground."
                    else:
                        "She lets her [Line] fall to the ground."
                        if not renpy.showing('DressScreen'):
                            call Emma_First_Topless
                  
                "I like that corset you have." if EmmaX.Chest != "corset":
                    if EmmaX.SeenChest or ApprovalCheck(EmmaX, 1000, TabM=(3-Public)):
                        ch_e "So do I."   
                        $ EmmaX.Chest = "corset"  
                        $ EmmaX.TitsUp = 1
                    else:            
                        call Display_DressScreen(EmmaX)
                        if not _return:       
                            ch_e "I don't think that would be appropriate. . ."      
                        
                "I like that lace bra." if "lace bra" in EmmaX.Inventory and EmmaX.Chest != "lace bra":
                    if EmmaX.SeenChest or ApprovalCheck(EmmaX, 1300, TabM=(3-Public)):
                        ch_e "Fine."   
                        $ EmmaX.Chest = "lace bra"         
                    else:                
                        call Display_DressScreen(EmmaX)
                        if not _return:       
                            ch_e "It's a bit revealing. . ."  
                    
                "I like that sports bra." if EmmaX.Chest != "sports bra":
                    if EmmaX.SeenChest or ApprovalCheck(EmmaX, 1000, TabM=(3-Public)):
                        ch_e "Fine."   
                        $ EmmaX.Chest = "sports bra"         
                    else:                
                        call Display_DressScreen(EmmaX)
                        if not _return:       
                            ch_e "I'm not sure about that. . ."  
                          
                "I like that bikini top." if EmmaX.Chest != "bikini top" and "bikini top" in EmmaX.Inventory:
                    if bg_current == "bg pool":
                            ch_e "Fine."   
                            $ EmmaX.Chest = "bikini top"         
                    else:                
                            if EmmaX.SeenChest or ApprovalCheck(EmmaX, 800, TabM=2):
                                ch_e "Fine."   
                                $ EmmaX.Chest = "bikini top"         
                            else:                
                                call Display_DressScreen(EmmaX)
                                if not _return:       
                                    ch_e "I don't know about wearing that here. . ." 
                "Never mind":
                    pass 
            return #jump Emma_Clothes_Under
                  
                                    
        "Hose and stockings options":
            menu:          
                "You could lose the hose." if EmmaX.Hose:     
                                $ EmmaX.Hose = 0  
                "The thigh-high hose would look good with that." if EmmaX.Hose != "stockings" and "stockings and garterbelt" in EmmaX.Inventory:    
                                $ EmmaX.Hose = "stockings"  
                "The pantyhose would look good with that." if EmmaX.Hose != "pantyhose" and "pantyhose" in EmmaX.Inventory:    
                                $ EmmaX.Hose = "pantyhose" 
                "The stockings and garterbelt would look good with that." if EmmaX.Hose != "stockings and garterbelt" and "stockings and garterbelt" in EmmaX.Inventory:     
                                $ EmmaX.Hose = "stockings and garterbelt"  
                "Maybe just the garterbelt?" if EmmaX.Hose != "garterbelt" and "stockings and garterbelt" in EmmaX.Inventory:     
                                $ EmmaX.Hose = "garterbelt"  
                "Never mind":
                        pass  
            return #jump Emma_Clothes_Under
                      
        #Panties   
        "Panties":
            menu:
                "You could lose those panties. . ." if EmmaX.Panties:
                        $ EmmaX.FaceChange("bemused", 1)  
                        if (ApprovalCheck(EmmaX, 900) or EmmaX.SeenPussy) and not EmmaX.Taboo:
                            #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
                            
                            if ApprovalCheck(EmmaX, 850, "L"):               
                                    ch_e "You like the view?"
                            elif ApprovalCheck(EmmaX, 500, "O"):
                                    ch_e "If you'd like."
                            elif ApprovalCheck(EmmaX, 350, "I"):
                                    ch_e "I do enjoy going without them. . ."
                            else:
                                    ch_e "Very well."         
                        else:                       
                            #low approval or not wearing pants or in public 
                            if ApprovalCheck(EmmaX, 1100, "LI", TabM=(4-Public)) and EmmaX.Love > EmmaX.Inbt:               
                                    ch_e "I don't exactly mind you seeing. . ."
                            elif ApprovalCheck(EmmaX, 700, "OI", TabM=(4-Public)) and EmmaX.Obed > EmmaX.Inbt:
                                    ch_e "I suppose I could. . ."
                            elif ApprovalCheck(EmmaX, 600, "I", TabM=(4-Public)):
                                    ch_e "Why not."
                            elif ApprovalCheck(EmmaX, 1300, TabM=(4-Public)):
                                    ch_e "Fine."
                            else: 
                                call Display_DressScreen(EmmaX)
                                if not _return:
                                    $ EmmaX.FaceChange("surprised")
                                    $ EmmaX.Brows = "angry" 
                                    if EmmaX.Taboo > 20:
                                        ch_e "I don't think I could out here, [EmmaX.Petname]!"
                                    else:
                                        ch_e "I could, but I won't, [EmmaX.Petname]!"
                                    return #jump Emma_Clothes
                        $ Line = EmmaX.Panties
                        $ EmmaX.Panties = 0  
                        if EmmaX.Legs:
                            if EmmaX.Taboo or ApprovalCheck(EmmaX, 1100) or EmmaX.SeenPussy:
                                "She pulls off her [EmmaX.Legs] then pulls her [Line] off, droping them to the ground, before putting them back on." 
                                call Emma_First_Bottomless(1)
                            else:
                                "She asks you to turn around. After a few seconds, you turn back to her as she drops the [Line] to the ground."               
                        else:
                            "She pulls off her [Line] and lets them drop to the ground."
                            if not renpy.showing('DressScreen'):
                                call Emma_First_Bottomless
                                $ EmmaX.Statup("Inbt", 50, 2)  
                            
                "Why don't you wear the white panties instead?" if EmmaX.Panties and EmmaX.Panties != "white panties":
                        if ApprovalCheck(EmmaX, 1100, TabM=(4-Public)):
                                ch_e "Ok."
                                $ EmmaX.Panties = "white panties"  
                        else:                
                            call Display_DressScreen(EmmaX)
                            if not _return:
                                ch_e "I really don't see how that's any of your concern."
                  
                "Why don't you wear the sporty panties instead?" if EmmaX.Panties and EmmaX.Panties != "sports panties":
                        if ApprovalCheck(EmmaX, 1200, TabM=(4-Public)):
                                ch_e "Fine."
                                $ EmmaX.Panties = "sports panties"
                        else:    
                            call Display_DressScreen(EmmaX)
                            if not _return:
                                ch_e "I really don't see how that's any of your concern."
                                
                "Why don't you wear the lace panties instead?" if "lace panties" in EmmaX.Inventory and EmmaX.Panties and EmmaX.Panties != "lace panties":
                        if ApprovalCheck(EmmaX, 1300, TabM=(4-Public)):
                                ch_e "Fine."
                                $ EmmaX.Panties = "lace panties"
                        else:
                            call Display_DressScreen(EmmaX)
                            if not _return:
                                ch_e "I really don't see how that's any of your concern."
                                 
                "I like those bikini bottoms." if EmmaX.Panties != "bikini bottoms" and "bikini bottoms" in EmmaX.Inventory:
                        if bg_current == "bg pool":
                                ch_e "Fine."   
                                $ EmmaX.Panties = "bikini bottoms"         
                        else:                
                                if ApprovalCheck(EmmaX, 800, TabM=2):
                                    ch_e "Fine."   
                                    $ EmmaX.Panties = "bikini bottoms"         
                                else:        
                                    call Display_DressScreen(EmmaX)
                                    if not _return:        
                                        ch_e "I don't know about wearing those here. . ." 
                                
                "You know, you could wear some panties with that. . ." if not EmmaX.Panties:
                        $ EmmaX.FaceChange("bemused", 1)
                        if EmmaX.Legs and (EmmaX.Love+EmmaX.Obed) <= (2* EmmaX.Inbt):
                            $ EmmaX.Mouth = "smile"
                            ch_e "I could, but won't."
                            menu:
                                "Fine by me":
                                    return #jump Emma_Clothes
                                "I insist, put some on.":
                                    if (EmmaX.Love+EmmaX.Obed) <= EmmaX.Inbt:
                                        $ EmmaX.FaceChange("angry", Eyes="side")
                                        ch_e "How disappointing that must be for you."
                                        return #jump Emma_Clothes
                                    else:
                                        $ EmmaX.FaceChange("sadside")
                                        ch_e "If you insist."   
                        menu:
                            ch_e "If you insist. . ."
                            "How about the white ones?":
                                ch_e "Fine."
                                $ EmmaX.Panties = "white panties"
                            "How about the sporty ones?":
                                ch_e "Fine."
                                $ EmmaX.Panties = "sports panties"
                            "How about the lace ones?" if "lace panties" in EmmaX.Inventory:
                                ch_e "Fine."                
                                $ EmmaX.Panties  = "lace panties"
                "Never mind":
                    pass
            return #jump Emma_Clothes_Under
        "Never mind":
            pass
    return #jump Emma_Clothes
    #End of Emma Underwear
       
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  
        
    menu Emma_Clothes_Misc:                     
        #Misc        
        "You look good with your hair flowing." if EmmaX.Hair != "wave":
                if ApprovalCheck(EmmaX, 600):
                    ch_e "Like this?"
                    $ EmmaX.Hair = "wave"
                else:
                    ch_e "Yes, I do."
                
        "Maybe keep your hair straight." if EmmaX.Hair != "wet":
                if ApprovalCheck(EmmaX, 600):
                    ch_e "You think?"
                    $ EmmaX.Hair = "wet"
                else:
                    ch_e "I tend to prefer it a bit more loose."
                        
        "You know, I like some nice hair down there. Maybe grow it out." if not EmmaX.Pubes and "pubes" not in EmmaX.Todo: 
                if "pubes" in EmmaX.Todo:
                    $ EmmaX.FaceChange("bemused", 1)
                    ch_e "Rome wasn't built in a day. . ."
                else:                    
                    $ EmmaX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(EmmaX, 1150, TabM=0)
                    if ApprovalCheck(EmmaX, 850, "L", TabM=0) or (Approval and EmmaX.Love > 2 * EmmaX.Obed):               
                        ch_e "If you like that sort of thing. . ."
                    elif ApprovalCheck(EmmaX, 500, "I", TabM=0) or (Approval and EmmaX.Inbt > EmmaX.Obed):
                        ch_e "I could go a bit more. . . wild."
                    elif ApprovalCheck(EmmaX, 400, "O", TabM=0) or Approval:
                        ch_e "If you insist. . ."
                    else: 
                        $ EmmaX.FaceChange("surprised")
                        $ EmmaX.Brows = "angry"
                        ch_e "I don't see how that's your concern, [EmmaX.Petname]."
                        return #jump Emma_Clothes
                    $ EmmaX.Todo.append("pubes")
                    $ EmmaX.PubeC = 6
        
        "I like it waxed clean down there." if EmmaX.Pubes == 1:
                $ EmmaX.FaceChange("bemused", 1)            
                if "shave" in EmmaX.Todo:
                    ch_e "Yes, yes, it's on my schedule."
                else:
                    $ Approval = ApprovalCheck(EmmaX, 1150, TabM=0)
                    
                    if ApprovalCheck(EmmaX, 850, "L", TabM=0) or (Approval and EmmaX.Love > 2 * EmmaX.Obed):               
                        ch_e "I know you love it."
                    elif ApprovalCheck(EmmaX, 500, "I", TabM=0) or (Approval and EmmaX.Inbt > EmmaX.Obed):
                        ch_e "I like it kept tidy."
                    elif ApprovalCheck(EmmaX, 400, "O", TabM=0) or Approval:
                        ch_e "If you insist."
                    else: 
                        $ EmmaX.FaceChange("surprised")
                        $ EmmaX.Brows = "angry"
                        ch_e "I don't see how that's your concern, [EmmaX.Petname]."
                        return #jump Emma_Clothes
                    $ EmmaX.Todo.append("shave")        
        "Piercings. [[See what she looks like without them first] (locked)" if not EmmaX.SeenPussy and not EmmaX.SeenChest:
                pass
            
        "You know, you'd look really nice with some ring body piercings." if EmmaX.Pierce != "ring" and (EmmaX.SeenPussy or EmmaX.SeenChest):    
                if "ring" in EmmaX.Todo:
                        ch_e "Yes, yes, it's on my schedule."
                else:                    
                        $ EmmaX.FaceChange("bemused", 1)
                        $ Approval = ApprovalCheck(EmmaX, 1350, TabM=0)
                        if ApprovalCheck(EmmaX, 900, "L", TabM=0) or (Approval and EmmaX.Love > 2* EmmaX.Obed):   
                                ch_e "A little handhold, I assume?"
                        elif ApprovalCheck(EmmaX, 600, "I", TabM=0) or (Approval and EmmaX.Inbt > EmmaX.Obed):
                                ch_e "I do like a nice ring. . ."
                        elif ApprovalCheck(EmmaX, 500, "O", TabM=0) or Approval:
                                ch_e "I didn't know you were into that sort of thing."
                        else: 
                                $ EmmaX.FaceChange("surprised")
                                $ EmmaX.Brows = "angry"
                                ch_e "Well, I'm just not ready for that sort of thing, [EmmaX.Petname]."
                                return #jump Emma_Clothes            
                        $ EmmaX.Todo.append("ring")
        
        "You know, you'd look really nice with some barbell body piercings." if EmmaX.Pierce != "barbell" and (EmmaX.SeenPussy or EmmaX.SeenChest):    
                if "barbell" in EmmaX.Todo:
                        ch_e "Yes, yes, it's on my schedule."
                else:                    
                        $ EmmaX.FaceChange("bemused", 1)
                        $ Approval = ApprovalCheck(EmmaX, 1350, TabM=0)
                        if ApprovalCheck(EmmaX, 900, "L", TabM=0) or (Approval and EmmaX.Love > 2 * EmmaX.Obed): 
                            ch_e "A little handhold, I assume?"
                        elif ApprovalCheck(EmmaX, 600, "I", TabM=0) or (Approval and EmmaX.Inbt > EmmaX.Obed):
                            ch_e "They might look nice on these. . ."
                        elif ApprovalCheck(EmmaX, 500, "O", TabM=0) or Approval:
                            ch_e "I didn't know you were into that sort of thing."
                        else: 
                            $ EmmaX.FaceChange("surprised")
                            $ EmmaX.Brows = "angry"
                            ch_e "Well, I'm just not ready for that sort of thing, [EmmaX.Petname]."
                            return #jump Emma_Clothes                
                        $ EmmaX.Todo.append("barbell")
                        $ EmmaX.Pierce = "barbell"
            
        "You know, you'd look better without those piercings." if EmmaX.Pierce:
                $ EmmaX.FaceChange("bemused", 1)
                $ Approval = ApprovalCheck(EmmaX, 1350, TabM=0)
                if ApprovalCheck(EmmaX, 950, "L", TabM=0) or (Approval and EmmaX.Love > EmmaX.Obed):   
                    ch_e "If they aren't working for you. . ."
                elif ApprovalCheck(EmmaX, 700, "I", TabM=0) or (Approval and EmmaX.Inbt > EmmaX.Obed):
                    ch_e "They were being a nuisance."
                elif ApprovalCheck(EmmaX, 600, "O", TabM=0) or Approval:
                    ch_e "I'll remove them then."
                else: 
                    $ EmmaX.FaceChange("surprised")
                    $ EmmaX.Brows = "angry"
                    ch_e "Well {i}I{/i} enjoy them."
                    return #jump Emma_Clothes            
                $ EmmaX.Pierce = 0 
                
        "Why don't you try on that white choker." if EmmaX.Neck != "choker":
                ch_e "Ok. . ."         
                $ EmmaX.Neck = "choker"
        "Maybe go without a collar." if EmmaX.Neck:
                ch_e "Ok. . ."         
                $ EmmaX.Neck = 0
            
        "Maybe lose the gloves." if EmmaX.Arms:
                $ EmmaX.Arms = 0
                ch_e "Ok."
        "Put your gloves on." if not EmmaX.Arms:
                $ EmmaX.Arms = "gloves"
                ch_e "Ok."       
        "Never mind":
                pass         
    return #jump Emma_Clothes
    #End of Emma Misc Wardrobe
    
return
#End Emma Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

        
## Start Emma first Les / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#label Emma_First_Les(Silent = 0, Undress = 0, GirlsNum = 0): #checked when she engages in a les scene  ## call Emma_First_Les(0,1)
#    if EmmaX.Les:
#        return
    
#    $ EmmaX.Les += 1
#    $ EmmaX.RecentActions.append("lesbian")        
#    $ EmmaX.Statup("Inbt", 30, 2) 
#    $ EmmaX.Statup("Inbt", 90, 1)
    
#    if not Silent: 
#        #example previous line: Line + " and cups " + Primary + "'s breasts in her delicate hands" 
#        "Emma's head jerks up and she looks at what [Partner] is doing. [Partner] pauses and glances up at her with a mischievous grin." 
#        ch_e "I, um, I haven't done that sort of thing before."
#        if Partner == "Rogue":
#                if R_Les:
#                    ch_r "Neither have I Sugar, but it seemed like fun."
#                else:
#                    ch_r "It's all right Sugar, I'll take care of you."
#        if EmmaX.LikeRogue >= 60 and ApprovalCheck(EmmaX, (1500-(10*EmmaX.Les)-(10*(EmmaX.LikeRogue-60)))): #If she likes both of you a lot, threeway
#                $ State = "threeway"
#        elif ApprovalCheck(EmmaX, 1000): #If she likes you well enough, Hetero
#                $ State = "hetero"            
#        elif EmmaX.LikeRogue >= 70: #if she doesn't like you but likes Rogue, lesbian
#                $ State = "lesbian"
        
        
        
        
        
#        if "cockout" in Player.RecentActions:
#                $ EmmaX.FaceChange("down", 2)  
#                if GirlsNum:
#                    "Emma also glances down at your cock"
#                else:
#                    "Emma glances down at your exposed cock"
#        elif Undress:
#                "You strip nude."
#        else:
#                "You whip your cock out."
#        $ Player.RecentActions.append("cockout") 
        
#        if Taboo and not ApprovalCheck(EmmaX, 1500):
#                $ EmmaX.FaceChange("surprised", 2)  
#                ch_e "Um, you should[EmmaX.like]put that away in public."
#                $ EmmaX.FaceChange("bemused", 1)  
#                if EmmaX.SeenPeen == 1: 
#                    ch_e "Or[EmmaX.like]maybe. . ."
#                    $ EmmaX.Statup("Love", 90, 15)                
#                    $ EmmaX.Statup("Obed", 50, 20)
#                    $ EmmaX.Statup("Inbt", 60, 35)  
                    
#        elif EmmaX.SeenPeen > 10:
#                return    
#        elif ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "L"):
#                $ EmmaX.FaceChange("sly",1) 
#                if EmmaX.SeenPeen == 1: 
#                    $ EmmaX.FaceChange("surprised",2)  
#                    ch_e "That's. . . impressive."
#                    $ EmmaX.FaceChange("bemused",1)  
#                    $ EmmaX.Statup("Love", 90, 3) 
#                elif EmmaX.SeenPeen == 2:  
#                    ch_e "I can't get over that."               
#                    $ EmmaX.Statup("Obed", 50, 7) 
#                elif EmmaX.SeenPeen == 5: 
#                    ch_e "There it is."
#                    $ EmmaX.Statup("Inbt", 60, 5)  
#                elif EmmaX.SeenPeen == 10: 
#                    ch_e "So beautiful."
#                    $ EmmaX.Statup("Obed", 80, 10)
#                    $ EmmaX.Statup("Inbt", 60, 3)  
#        else:
#                $ EmmaX.FaceChange("sad",1) 
#                if EmmaX.SeenPeen == 1: 
#                    $ EmmaX.FaceChange("perplexed",1 ) 
#                    ch_e "Well that happened. . ."
#                    $ EmmaX.Statup("Obed", 50, 7)
#                    $ EmmaX.Statup("Inbt", 60, 3)  
#                elif EmmaX.SeenPeen < 5: 
#                    $ EmmaX.FaceChange("sad",0) 
#                    ch_e "Huh."
#                    $ EmmaX.Statup("Inbt", 60, 2)  
#                elif EmmaX.SeenPeen == 10: 
#                    ch_e "[EmmaX.Like]put that away."               
#                    $ EmmaX.Statup("Obed", 50, 7)
#                    $ EmmaX.Statup("Inbt", 60, 3)  
    
#    else: #Silent mode
#                $ Player.RecentActions.append("cockout") 
#                if EmmaX.SeenPeen > 10:
#                    return
#                elif ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "L"):
#                        if EmmaX.SeenPeen == 1: 
#                            $ EmmaX.Statup("Love", 90, 3) 
#                        elif EmmaX.SeenPeen == 2:              
#                            $ EmmaX.Statup("Obed", 50, 7) 
#                        elif EmmaX.SeenPeen == 5: 
#                            $ EmmaX.Statup("Inbt", 60, 5)  
#                        elif EmmaX.SeenPeen == 10: 
#                            $ EmmaX.Statup("Love", 90, 10)  
#                else:
#                        if EmmaX.SeenPeen == 1: 
#                            $ EmmaX.Statup("Obed", 50, 7)
#                            $ EmmaX.Statup("Inbt", 60, 3)  
#                        elif EmmaX.SeenPeen < 5: 
#                            $ EmmaX.Statup("Inbt", 60, 2)  
#                        elif EmmaX.SeenPeen == 10:              
#                            $ EmmaX.Statup("Obed", 50, 7)
#                            $ EmmaX.Statup("Inbt", 60, 3) 
                            
#    if EmmaX.SeenPeen == 1:            
#        $ EmmaX.Statup("Love", 90, 10)                
#        $ EmmaX.Statup("Obed", 90, 25)
#        $ EmmaX.Statup("Inbt", 60, 20) 
#        $ EmmaX.Statup("Lust", 200, 5)
    
#    return
## End Emma first Les / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /   
    
##label Emma_Tits_Up:
            
            