# start KittyMeet //////////////////////////////////////////////////////////

        
label KittyMeet:   
        $ bg_current = "bg campus"    
        $ KittyX.OutfitDay = "casual1" 
        $ KittyX.Outfit = "casual1"     
        $ KittyX.OutfitChange()
        call CleartheRoom("All",0,1)
        $ KittyX.Loc = "bg kitty"  
        $ KittyX.Love = 400        
        $ KittyX.Obed = 100            
        $ KittyX.Inbt = 0  
        call Shift_Focus(KittyX)    
        call Set_The_Scene(0)
        $ KittyX.SpriteLoc = StageCenter
        $ KittyX.Petname = Player.Name[:1]     
            
        "As you rush to class, you see another student running straight at you."
        "You try to move aside, but aren't fast enough to get out of her way,"
        "She crashes into you at a full jog, and you both fall to the ground."
        "You scramble to your feet and offer the girl a hand up."
        show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) with vpunch       
        $ KittyX.Loc = "bg campus" 
        $ KittyX.Statup("Love", 90, -25) 
        $ KittyX.FaceChange("surprised")
        $ KittyX.ArmPose = 1
        ch_u "Hey!"
        $ KittyX.Brows = "angry"
        ch_u "What the hell was that?"
        $ Cnt = 1
        
        menu:
            extend ""
            "You crashed into me!":
                    $ KittyX.FaceChange("confused", 2)   
                    $ KittyX.Statup("Love", 90, 5)          
                    $ KittyX.Statup("Obed", 80, 20)         
                    ch_u "Wha! Well, yeah. . ."
                    $ KittyX.Blush = 1
                    $ Cnt = 0
            "Sorry about that.":
                    $ KittyX.FaceChange("bemused", 1) 
                    $ KittyX.Eyes = "side"
                    $ KittyX.Statup("Love", 90, 25) 
                    ch_u "Well, I guess it[KittyX.like]wasn't entirely your fault. . ."
            "A meet-cute?":
                    $ KittyX.FaceChange("surprised", 2) 
                    $ KittyX.Statup("Love", 90, 15)           
                    $ KittyX.Statup("Inbt", 70, 10) 
                    ch_u "  !  "
                    $ KittyX.FaceChange("bemused", 1) 
                    ch_u "Hmm. . . maybe. . ."        
        
        ch_p "My name's [Player.Name], by the way." 
        if Cnt:
                $ KittyX.FaceChange("smile", 1)
                ch_k "Mine's Kitty! Kitty Pryde. Nice to meet you!"
        else:
                $ KittyX.FaceChange("sadside", 1)
                ch_k "Um, mine's Kitty." 
        $ KittyX.FaceChange("normal", 1)
        $ KittyX.Mouth = "sad"
        ch_k "I just[KittyX.like]didn't expect to bounce off you like that. Normally I can phase through things." 
        
        menu:                                                               # + 5-10
            extend ""
            "Losing your touch?":
                    $ KittyX.FaceChange("confused", 0)           
                    $ KittyX.Statup("Obed", 80, 5) 
                    ch_k "I don't {i}think{/i} that's it. . ." 
                    ch_p "Just kidding. . ."
                    $ KittyX.Statup("Love", 90, 5) 
            "Was I too distracting?":
                    $ KittyX.FaceChange("angry", 1, Brows = "normal")
                    $ KittyX.Statup("Love", 90, -2)          
                    $ KittyX.Statup("Obed", 80, 8)            
                    $ KittyX.Statup("Inbt", 70, 4) 
                    ch_k "Like, no."
                    ch_p "Heh, I guess not."
            "It must be my powers." :
                    $ KittyX.FaceChange("confused", 0) 
                    $ KittyX.Statup("Love", 90, 5) 
                    ch_k "Oh?"
                
        ch_p "I have the ability to negate mutant powers, so you can't phase through me." 
        $ KittyX.FaceChange("perplexed", 0)    
        ch_k "Oh! Wow, that's an interesting power. So if you grab me, I can't get away?"
        
        menu:                                                               # +10
            extend ""
            "Want to give it a try?":
                    $ KittyX.FaceChange("perplexed", 0) 
                    $ KittyX.Statup("Love", 90, 5)            
                    $ KittyX.Statup("Inbt", 70, 5) 
                    ch_k "I'm definitely curious."
            "I guess so.":
                    $ KittyX.FaceChange("sadside", 0, Mouth = "lipbite")         
                    $ KittyX.Statup("Obed", 80, 3)            
                    $ KittyX.Statup("Inbt", 70, 7) 
                    ch_k "I'd like to give it a try."
            "Does that turn you on?":            
                    $ KittyX.FaceChange("surprised", 2)         
                    $ KittyX.Statup("Obed", 80, 5) 
                    ch_k "What?! No! . ."   
                    $ KittyX.FaceChange("bemused", 1)          
                    $ KittyX.Statup("Inbt", 70, 5) 
                    $ KittyX.Eyes = "side"
                    ch_k ". . . no."
                    $ KittyX.Eyes = "sexy"            
                    ch_k "But it is[KittyX.like]worth testing."
                
        ch_p "Ok, let's give it a shot."
        "You reach out and grab her wrist."
        $ KittyX.FaceChange("angry", 1, Eyes = "down")
        $ KittyX.Addictionrate += 2
        "She struggles for a few moments to shake you free, but you hold firm."
        $ Cnt = 0
        while Cnt < 3:
            menu:
                extend ""
                "Let her go.":  
                        if not Cnt:                                     #you let go instantly
                                $ KittyX.Statup("Love", 90, 7)            
                                $ KittyX.Statup("Inbt", 70, -2)    
                        elif Cnt == 1:                                  #she just asked you to let go
                                $ KittyX.Statup("Love", 90, 10) 
                        else:                                           #you let go after a pause
                                $ KittyX.Statup("Love", 90, 5)            
                        "You release her arm and step back."
                        $ Cnt = 4
                "Hold on.":
                        "You continue to hold onto her arm and she fidgets uncomfortably."
                        if not Cnt:
                                $ KittyX.Eyes = "sexy"                      
                                ch_k "Are you[KittyX.like]going to let go of my arm any time soon?"
                        elif Cnt == 2:
                                ch_k "Ok, that's enough!"
                                $ KittyX.Eyes = "sexy"  
                                $ KittyX.Statup("Love", 90, -10)          
                                $ KittyX.Statup("Obed", 80, -5)            
                                $ KittyX.Statup("Inbt", 70, 10) 
                                "She reaches over and pries your hand loose."
                                $ Cnt = 4
                        else: 
                                $ KittyX.Statup("Love", 90, -1)          
                                $ KittyX.Statup("Obed", 80, 2) 
                                "Um. . ." 
                        $ Cnt += 1
                        $ KittyX.Addictionrate += 1

                "Pull her in for a hug.":
                        $ KittyX.Statup("Love", 90, -5) 
                        $ KittyX.FaceChange("surprised", 2)
                        ch_k "Hey! Like, not cool!"                
                        $ KittyX.FaceChange("angry", 1)
                        show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) with vpunch   
                        "She elbows you in the ribs and shoves herself back a few steps."          
                        $ KittyX.Statup("Inbt", 70, 10) 
                        ch_k "My powers may not work on you, but I have[KittyX.like]a few years of combat experience on you."
                        ch_k "And don't you forget it!"
                        $ Cnt = 10
                
        if Cnt > 3:       
            $ KittyX.Eyes = "side"  
            ch_k "Still though, that was an interesting experience. . ."
        else:
            $ KittyX.FaceChange("bemused", 1, Eyes = "side")
            ch_k "That was an interesting experience. . ."   
        $ KittyX.Eyes = "sexy"  
        $ KittyX.Mouth = "lipbite"
        ch_k "Kinda tingly. . ."
        
        $ Cnt = 0
        $ KittyX.FaceChange("surprised", Mouth = "kiss")
        ch_k "Oh! I[KittyX.like]totally forgot, I have to get to a briefing!"
        if Cnt < 5:
                $ KittyX.FaceChange("smile")
                ch_k "I'll see you later though! Like, bye!"
        else:
                $ KittyX.FaceChange("normal")
                ch_k "I'll see you around I guess. Like, bye!"        
        
        $ KittyX.Loc = "bg kitty"         
        call Set_The_Scene
        
        "She jogs off down the path, and you continue on to class."
        $ KittyX.History.append("met")
        $ ActiveGirls.append(KittyX) if KittyX not in ActiveGirls else ActiveGirls  
        $ bg_current = "bg classroom"            
        $ Round -= 10      
        call Shift_Focus(RogueX)
        return
            
# end KittyMeet //////////////////////////////////////////////////////////            
           
# Event Kitty_Key /////////////////////////////////////////////////////  

#Not updated

label Kitty_Key:
            call Shift_Focus(KittyX)
            call Set_The_Scene
            $ KittyX.FaceChange("bemused")
            $ KittyX.ArmPose = 2
            ch_k "So you've[KittyX.like]been dropping by a lot lately, I figured you might want a key. . ."
            ch_p "Thanks."
            $ KittyX.ArmPose = 1    
            $ Keys.append(KittyX)
            $ KittyX.Event[0] = 1
            return
# end Event Kitty_Key /////////////////////////////////////////////////////

# start Kitty_BF//////////////////////////////////////////////////////////

#Not updated
label Kitty_BF:
    call Shift_Focus(KittyX)    
    if KittyX.Loc != bg_current:
            $ KittyX.Loc = bg_current
            if KittyX not in Party:
                    "[KittyX.Name] approaches you and asks if the two of you can talk."
            else:   
                    "[KittyX.Name] turns towards you and asks if the two of you can talk."
                
    call Set_The_Scene(0)
    call Display_Girl(KittyX)
    "A little blush on her cheeks, you can tell she's a bit anxious about whatever she has to say." 
    call Taboo_Level
    call CleartheRoom(KittyX)
    $ KittyX.DailyActions.append("relationship")
    $ KittyX.FaceChange("bemused", 1)
    
    ch_k "So, [KittyX.Petname], we've[KittyX.like]been hanging for a while, right?"
    ch_k ". . ."
    $ KittyX.Eyes = "sexy"
    menu:
        ch_k "Right?"
        "Yeah. And it's been amazing.":
                $ KittyX.Statup("Love", 200, 20)
        "Yeah, I guess":
                $ KittyX.Statup("Love", 200, 10)
        "Uhm. . .maybe?":
                $ KittyX.Statup("Love", 200, -10)
                $ KittyX.Statup("Obed", 200, 30)
    if KittyX.SEXP >= 10:
            ch_k "I mean, I've gone further with you than I've ever been with anybody before. . ."
    if KittyX.SEXP >= 15:
            ch_k "You know[KittyX.like]. . .in the {i}bedroom{/i}. . ."
    if len(Player.Harem) >= 2:
            ch_k "I know you[KittyX.like]really get around and all. . ."
    elif RogueX in Player.Harem: 
        if "dating?" in KittyX.Traits:    
                ch_k "I know you're kinda[KittyX.like][RogueX.Name]'s boyfriend and all. . . but she and I were talking and[KittyX.like]. . ."
        else:
                ch_k "I know you're kinda[KittyX.like][RogueX.Name]'s boyfriend and all. . ."
    elif Player.Harem:
                ch_k "I know you're kinda[KittyX.like]dating [Player.Harem[0].Name] and all. . ."
        
    if not KittyX.Event[5]:
            ch_k "So, uhm. . ."
            ch_k "It’s not like I[KittyX.like]haven’t gone out with guys before."
            ch_k "I just[KittyX.like]..wow, this is so awkward.  I really like you a lot and. . ."
            ch_k "I mean. . . do you wanna[KittyX.like]be my boyfriend?"
            ch_k "[KittyX.Like]maybe we could make it official?"
    elif "dating?" in KittyX.Traits: 
            ch_k "[RogueX.Name] said it’d totally be cool if we were[KittyX.like]dating, too." 
    elif Player.Harem: 
            ch_k "If you were okay with it. . . I’d still like to be your girlfriend, too."
    else:        
            ch_k "I wish you weren’t[KittyX.like]such a jerk sometimes, but still. . . I’m totally serious about this."
            ch_k "I wanna be your girlfriend[KittyX.like]officially."
    $ KittyX.Event[5] += 1
    menu: 
        extend ""
        "Are you kidding? I'd love to!":
                $ KittyX.Statup("Love", 200, 30)
                "[KittyX.Name] wraps her arms around you and starts kissing you passionately."
                $ KittyX.FaceChange("kiss") 
                call Kitty_Kissing_Launch("kiss you")
                $ KittyX.Kissed += 1
        "Uhm[KittyX.like]okay.":
                $ KittyX.Brows = "confused"
                "[KittyX.Name] seems a little put off by how casually you’re taking all this."
                "Still, she must think it’s a good first step, at least, because she leans into you and gives you a hug."    
        "I'm with someone else now." if Player.Harem:             
            $ KittyX.FaceChange("sad",1)    
            ch_k "I know.  I just[KittyX.like]. . . I thought maybe you could go out with me, too, maybe?"
            menu:
                extend ""
                "Yes. Absolutely." if "KittyYes" in Player.Traits:
                        $ KittyX.Statup("Love", 200, 30)
                        "[KittyX.Name] wraps her arms around you and starts kissing you passionately."
                        $ KittyX.FaceChange("kiss") 
                        call Kitty_Kissing_Launch("kiss you")
                        $ KittyX.Kissed += 1
                "She wouldn't understand." if len(Player.Harem) == 1:
                        $ Line = "no"
                "They wouldn't be cool with that." if len(Player.Harem) > 1:
                        $ Line = "no"
                "I'm sorry, but. . . no." if KittyX.Event[5] != 20:
                        $ Line = "no"
                "No way.":
                        jump Kitty_BF_Jerk
            if Line == "no":                
                        $ KittyX.Statup("Love", 200, -10)
                        ch_k "Well. . . okay. I get it." 
                        $ KittyX.Event[5] = 20 
                        call Remove_Girl(KittyX)  
                        $ Line = 0
                        return
        "Not really.":
                        jump Kitty_BF_Jerk
    
    if "Historia" not in Player.Traits:
            $ Player.Harem.append(KittyX)
            if "KittyYes" in Player.Traits:       
                    $ Player.Traits.remove("KittyYes")
    $ KittyX.Petnames.append("boyfriend")
    $ KittyX.Traits.append("dating")
    $ KittyX.FaceChange("sexy")    
    ch_k "Now. . . boyfriend. . . how about you and I[KittyX.like]celebrate, huh?"
    if "Historia" in Player.Traits:
            return 1
    $ Tempmod = 10
    call Kitty_SexMenu
    $ Tempmod = 0
    return
    
label Kitty_BF_Jerk:
    $ KittyX.FaceChange("angry", 1)
    ch_k "Fine![KittyX.Like]. . .be that way!" 
    $ KittyX.Statup("Obed", 50, 40)
    if KittyX.Event[5] != 20:
            $ KittyX.Statup("Obed", 200, (20* KittyX.Event[5]))
    if 20 > KittyX.Event[5] >= 3:
            $ KittyX.FaceChange("sad")
            ch_k "Yeah? Well. . .[KittyX.like]I don’t care what you want! We’re dating! Deal." 
            ch_k "I. . .uhm. . .think I need to[KittyX.like]be alone for a little while."        
            if "Historia" in Player.Traits:
                    return 1  
            $ KittyX.Petnames.append("boyfriend")
            $ KittyX.Traits.append("dating")
            $ Achievements.append("I am not your Boyfriend!")
            $ bg_current = "bg player"  
            call Remove_Girl(KittyX)   
            call Set_The_Scene
            $ renpy.pop_call()
            jump Player_Room
    if KittyX.Event[5] > 1:
            ch_k "It was such a mistake asking you again.  You’re[KittyX.like]still such a jerk!"
    if KittyX.Event[5] != 20:
            $ KittyX.Statup("Love", 200, -(50* KittyX.Event[5]))
    else:
            $ KittyX.Statup("Love", 200, -50)
    ch_k "Get out, you big jerk!"
    if "Historia" in Player.Traits:
            return
    $ bg_current = "bg player"  
    call Remove_Girl(KittyX)  
    $ renpy.pop_call()
    jump Player_Room
        
## end Kitty_BF//////////////////////////////////////////////////////////

## start Kitty_Love//////////////////////////////////////////////////////////
label Kitty_Love:
    #First time through, KittyX.Event[6] is 0, each time adds 1, automatically ends at 5,
    # it gets set at 20 if you refuse her advances, if it's 25 it means you've asked for a second chance and been refused
    call Shift_Focus(KittyX)  
    if KittyX.Event[6]:
            #on repeat attempts
            "[KittyX.Name] seems kind of shy and shuffles up to you, as if working up her nerve."
    elif bg_current != "bg kitty":
        if KittyX.Loc == bg_current or KittyX in Party:
            "Suddenly, [KittyX.Name] says she wants to talk to you in her room and drags you over there."
        else:
            "[KittyX.Name] shows up, hurridly says she wants to talk to you in her room and drags you over there."
        $ bg_current = "bg kitty"
    else:
            "[KittyX.Name] suddenly stares at you very intently."
        
    $ KittyX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(KittyX)
    call CleartheRoom(KittyX)
    call Taboo_Level
    $ KittyX.DailyActions.append("relationship")
    $ KittyX.FaceChange("bemused", 1)
    $ KittyX.Eyes = "side"    
    $ Line = 0
    $ KittyX.Event[6] += 1
    if KittyX.Event[6] == 1:
            if "dating" in KittyX.Traits:
                ch_k "We've[KittyX.like]been together for a while now, and I've been thinking. . ."
            else:
                ch_k "We've[KittyX.like]know each other for a while now, and I've been thinking. . ."
            ch_k "It's been[KittyX.like]kinda hard for me to really get invested in anyone. . ."
            $ KittyX.Eyes = "down"
            ch_k ". . . to[KittyX.like]be comfortable with who they are and be myself. . ."
            $ KittyX.Eyes = "sly"
            ch_k "I just feel like sometimes you. . ."
            $ KittyX.Eyes = "side"
            ch_k "and me[KittyX.like] . ."
            $ KittyX.FaceChange("perplexed", 2)
            $ KittyX.Eyes = "surprised"
            ch_k "Never mind!"
            "Kitty dashes off and phases through the nearest wall."
            hide Kitty_Sprite with easeoutright
            call Remove_Girl(KittyX)
            return
    if KittyX.Event[6] == 2:
        ch_k "Sorry about before, I don't think I was ready maybe. . ."
        ch_k ". . . but I was kind of thinking-"   
    elif KittyX.Event[6] >= 5:
        ch_k "Um. . ."
        $ KittyX.Eyes = "sly"
        ch_k "You know, it's time to stop running. I think I love you."
        $ KittyX.Eyes = "side"
        ch_k "You don't have to say it back, but I do."
        $ KittyX.Petnames.append("lover")
        ch_k "Um, that's all."
    else:
        ch_k "Um. . ."
    if "lover" not in KittyX.Petnames: 
            menu:
                "She turns and makes a break for the nearest wall."
                "Catch her":
                    $ KittyX.FaceChange("perplexed", 2)
                    $ KittyX.Eyes = "surprised"
                    $ KittyX.Statup("Love", 95, 10) 
                    $ KittyX.Statup("Obed", 95, 15) 
                    "As she spins, you grab on to her wrist. She's slightly startled to have been caught."
                "Let her go":
                    "She dashes through the nearest wall and vanishes from view."
                    jump Kitty_Love_End    
            $ KittyX.Blush = 1
            menu:
                extend ""
                "Pull her close":
                    $ KittyX.FaceChange("smile", 1)
                    $ KittyX.Statup("Love", 95, 20) 
                    "You draw her into an embrace, arms wrapped tightly around her waist."
                    $ Line = "hug"
                "Stay like this":
                    $ KittyX.Eyes = "down"
                    $ KittyX.Statup("Obed", 95, 10) 
                    "You keep hold of her wrist."
                    $ Line = "wrist"
                "Let her go":
                    if 1 < KittyX.Event[6] < 4:
                        "You immediately release her wrist."
                        $ KittyX.Eyes = "down"
                        "She dashes through the nearest wall and vanishes from view."
                        jump Kitty_Love_End
                    else:
                        $ KittyX.Statup("Love", 95, 10) 
                        $ KittyX.Statup("Obed", 95, 20)
                        $ KittyX.Statup("Inbt", 80, 20)  
                        "You release her wrist and she takes a step back."
                        
            ch_k "I'm. . . I'm sorry, I just kind of panicked."
    if "lover" not in KittyX.Petnames:        
            # If she hasn't confessed yet
            ch_k "I thought maybe if I let myself get too close. . ."
            ch_k "I'd fall. . ."
            menu:
                extend ""
                "I'll never let go." if Line:
                        $ KittyX.Statup("Love", 95, 20) 
                        $ KittyX.Statup("Inbt", 80, 10)  
                        "She melts into your arms."
                "I'd always catch you.":
                        $ KittyX.FaceChange("smile")
                        $ KittyX.Statup("Love", 95, 20) 
                        $ KittyX.Statup("Obed", 80, 15)
                        "She smiles and shifts a bit uncomfortably."
                "Yeah, you should watch out for that.":
                        $ KittyX.FaceChange("angry", 1)
                        $ KittyX.RecentActions.append("angry")
                        $ KittyX.Statup("Love", 200, -20) 
                        $ KittyX.Statup("Obed", 80, 10)
                        $ KittyX.Statup("Inbt", 80, 10)  
                        "She shoves you away and then stomps through the nearest wall."                        
                        jump Kitty_Love_End
                    
                "So get going. [[Give her a shove]":
                        $ KittyX.FaceChange("surprised", 1)
                        $ KittyX.Statup("Love", 200, -50) 
                        $ KittyX.Statup("Obed", 80, 10)
                        $ KittyX.Statup("Inbt", 80, 10)  
                        "You shove her through the nearest wall and then continue on you way."
                        $ KittyX.RecentActions.append("angry")
                        hide Kitty_Sprite with easeoutbottom
                        jump Kitty_Love_End
                    
    if "lover" in KittyX.Petnames: 
        #if she made the first move
        menu:
            extend "" #"I love you."
            "I love you too.":
                            $ KittyX.Statup("Love", 200, 40) 
                            $ KittyX.Statup("Inbt", 200, 50)  
                            $ KittyX.FaceChange("smile")
            "You love me?":
                $ KittyX.FaceChange("confused", 2)
                menu:
                    ch_k "But you don't love me?"
                    "Yeah, of course I do!":
                            $ KittyX.Statup("Love", 200, 30)
                            $ KittyX.Statup("Inbt", 200, 60)  
                            $ KittyX.FaceChange("smile")
                    "I mean, a little?": 
                            $ KittyX.Statup("Obed", 80, 20)
                            $ KittyX.Statup("Inbt", 80, -10)  
                            ch_k "That's not a \"yes.\" . ."
                            $ Line = "awkward"
                    "Not really.":
                            $ KittyX.Statup("Love", 200, -30) 
                            $ KittyX.Statup("Obed", 80, 30)
                            $ KittyX.Statup("Inbt", 80, -30)  
                            $ KittyX.FaceChange("angry", 2)
                            ch_k "Huh?!"
                            $ Line = "awkward"
            "Huh.":
                $ KittyX.Statup("Love", 200, -10) 
                $ KittyX.Statup("Obed", 80, 10)
                $ KittyX.Statup("Inbt", 80, -20)  
                menu:
                    ch_k "Huh?!"
                    "I mean, I love you too!":
                            $ KittyX.Statup("Love", 200, 30) 
                            $ KittyX.Statup("Inbt", 80, 10)  
                            $ KittyX.FaceChange("smile")
                            ch_k "Way to pull out a last minute save there. . ."
                    "Well that's awkward.":
                            $ KittyX.Statup("Love", 200, -20) 
                            $ KittyX.Statup("Obed", 80, 30)
                            $ KittyX.Statup("Inbt", 80, -20)  
                            $ KittyX.FaceChange("angry", 2)
                            $ Line = "awkward"
            "Well that's awkward.":
                            $ KittyX.Statup("Love", 200, -30) 
                            $ KittyX.Statup("Obed", 80, 40)
                            $ KittyX.Statup("Inbt", 80, -20)  
                            $ KittyX.FaceChange("perplexed", 2)
                            $ Line = "awkward"
    else:
        menu:
            extend ""
            "I love you, [KittyX.Name].":
                        $ KittyX.Statup("Love", 200, 50) 
                        $ KittyX.Statup("Inbt", 80, 30)  
                        $ KittyX.FaceChange("smile")
                        $ Line = "love"
            "I think you're pretty great.":
                $ KittyX.FaceChange("confused")
                menu:
                    ch_k "But you don't love me?"
                    "Yeah, of course I do!":
                                $ KittyX.Statup("Love", 200, 30) 
                                $ KittyX.Statup("Obed", 50, 10)
                                $ KittyX.Statup("Inbt", 80, 20)  
                                $ KittyX.FaceChange("smile")
                    "I mean, a little?":
                        if ApprovalCheck(KittyX, 1200, "OI"):
                                $ KittyX.FaceChange("sad")
                                $ KittyX.Statup("Love", 200, -30) 
                                $ KittyX.Statup("Obed", 90, 20)
                                $ KittyX.Statup("Inbt", 80, 10)  
                                ch_k "But[KittyX.like]not \"nothing\". . ."
                        else:
                                $ Line = "awkward"
                    "Not really.":     
                        $ KittyX.FaceChange("sad")                   
                        if ApprovalCheck(KittyX, 1500, "OI"):
                                $ KittyX.Statup("Love", 200, -30) 
                                $ KittyX.Statup("Obed", 50, 30)
                                ch_k "Ouch. . ."
                        else:
                                $ Line = "awkward"
            "I was thinking something more casual. . .":
                        $ KittyX.FaceChange("sad")
                        if ApprovalCheck(KittyX, 1200, "OI") or ApprovalCheck(KittyX, 700, "I"):
                                $ KittyX.Statup("Love", 200, -30) 
                                $ KittyX.Statup("Obed", 90, 20)
                                $ KittyX.Statup("Inbt", 90, 30)  
                                ch_k "Close enough."
                        else:  
                                $ Line = "awkward"
                            
    if Line == "awkward":   
        if ApprovalCheck(KittyX, 700, "O"):   
                ch_k "Fine, this doesn't have to be love."
        elif ApprovalCheck(KittyX, 700, "I"):
                ch_k "Fine, just sex it is."            
        elif ApprovalCheck(KittyX, 1200, "OI"):
                ch_k "Fine, I can work with that."
        else:
                $ KittyX.Statup("Love", 200, -50) 
                $ KittyX.Statup("Obed", 95, 50)
                $ KittyX.Statup("Inbt", 80, -50)  
                ch_k "Oh, well I mean if you don't love me-"
                ch_k "You don't have to love me, that's ok."
                ch_k "I'll, um. . . never mind."            
                if "Historia" not in Player.Traits:
                        $ KittyX.RecentActions.append("angry")
        $ KittyX.Event[6] = 20 #this means it shuts down future attempts
    else:
        if Line:
                # If you're holding her
                "She squeezes you even tighter and makes a little whimper."
        else:
                "She dives into your arms with a little squeek."
        if "lover" not in KittyX.Petnames:
                ch_k "I love you too. . ."
                ch_k "I think I have for a while now."
                $ KittyX.Petnames.append("lover")
    
label Kitty_Love_End:    
    if Line == "awkward" or "lover" not in KittyX.Petnames:
            hide Kitty_Sprite with easeoutright
            call Remove_Girl(KittyX)
            return
    ch_k "So I was thinking. . . did you want to . . ."
    if bg_current != "bg player" and bg_current != "bg kitty":
            ch_k "Wait, let's take this someplace more private. . ."
            $ bg_current = "bg kitty"
            $ KittyX.Loc = bg_current
            call Set_The_Scene
            call CleartheRoom(KittyX)
            call Taboo_Level
            ch_k "Ok, so like I was saying. . ."
    $ KittyX.Statup("Obed", 70, 10)
    menu:
        extend ""
        "Yeah, let's do this. . . [[have sex]":      
                $ KittyX.Statup("Inbt", 30, 30) 
                ch_k "Hmm. . ."                  
                if "Historia" in Player.Traits:
                        return 1
                call Kitty_SexAct("sex")
        "I have something else in mind. . .[[choose another activity]":
                $ KittyX.Brows = "confused"
                $ KittyX.Statup("Obed", 70, 20)
                ch_k "Something like. . ."  
                if "Historia" in Player.Traits:
                        return 1  
                $ Tempmod = 20     
                call Kitty_SexMenu     
    return
    
label Kitty_Love_Redux:
    #this is for if you rejected her but want a second chance
    $ Line = 0
    $ KittyX.DailyActions.append("relationship")
    if KittyX.Event[6] >= 25:
            #if this is the second time through
            ch_p "I hope you've forgiven me, I still love you."
            $ KittyX.Statup("Love", 95, 10) 
            if ApprovalCheck(KittyX, 950, "L"):
                    $ Line = "love"
            else:
                    $ KittyX.FaceChange("sad")   
                    ch_k "You've dug too deep a hole, [KittyX.Petname]."
                    ch_k "Keep trying though." 
    else:
            ch_p "Remember when I told you that I didn't love you?"
            $ KittyX.FaceChange("perplexed",1)   
            ch_k "Um, YEAH?!"
            menu:
                "I'm sorry, I didn't mean it.":
                        $ KittyX.Eyes = "surprised"
                        ch_k "Well, if you. . . so wait, you {i}do{/i} love me?"
                        ch_p "Yeah. I mean, yes, I love you, Kitty."
                        $ KittyX.Statup("Love", 200, 10) 
                        if ApprovalCheck(KittyX, 950, "L"):
                                $ Line = "love"
                        else:
                                $ KittyX.FaceChange("sadside")   
                                ch_k "Well, I don't know how I feel at this point. . ."                        
                "I've changed my mind, so. . .":
                    if ApprovalCheck(KittyX, 950, "L"):
                            $ Line = "love"
                            $ KittyX.Eyes = "surprised"
                            ch_k "Really?!"
                    else:
                            $ KittyX.Mouth = "sad"
                            ch_k "Oh, you've changed your mind. Wonderful."
                            $ KittyX.Statup("Inbt", 90, 10) 
                            $ KittyX.FaceChange("sadside")    
                            ch_k "Maybe I have too. . ."
                "Um, never mind.":
                            $ KittyX.Statup("Love", 200, -30) 
                            $ KittyX.Statup("Obed", 50, 10)  
                            $ KittyX.FaceChange("angry")   
                            ch_k "Seriously?"
                            $ KittyX.RecentActions.append("angry")
    if Line == "love":
            $ KittyX.Statup("Love", 200, 40) 
            $ KittyX.Statup("Obed", 90, 10)
            $ KittyX.Statup("Inbt", 90, 10) 
            $ KittyX.FaceChange("smile")    
            ch_k "I[KittyX.like]love you too!"
            if KittyX.Event[6] < 25:             
                    $ KittyX.FaceChange("sly")   
                    "She slugs you in the arm"
                    ch_k "Took you long enough."
            $ KittyX.Petnames.append("lover")                
    $ KittyX.Event[6] = 25
    return
## end Kitty_Love//////////////////////////////////////////////////////////


# start Kitty_Sub//////////////////////////////////////////////////////////

label Kitty_Sub:    
    call Shift_Focus(KittyX)
    if KittyX.Loc != bg_current and KittyX not in Party:
        "Suddenly, [KittyX.Name] shows up and says she needs to talk to you."
    
    $ KittyX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(KittyX)
    call CleartheRoom(KittyX)
    call Taboo_Level
    $ KittyX.DailyActions.append("relationship")
    $ KittyX.FaceChange("bemused", 1)
    
    $ Line = 0
    ch_k "So, uhm. . .you've really kinda[KittyX.like]taken control in our relationship lately."
    menu:    
        extend ""        
        "I guess. That's just kind of what comes naturally for me.":   
                $ KittyX.Statup("Obed", 200, 10)
                $ KittyX.Statup("Inbt", 50, 5)
        "Sorry. I didn't mean to come off like that.":
                $ KittyX.FaceChange("startled", 2)
                $ KittyX.Statup("Love", 80, 5)
                $ KittyX.Statup("Obed", 200, -5)
                $ KittyX.Statup("Inbt", 50, -5)
                ch_k "No!  Don't get the wrong idea!  I just. . ." 
        "Yup. Deal with it.": 
                if ApprovalCheck(KittyX, 1000, "LO"):
                        $ KittyX.Statup("Obed", 200, 20)
                        $ KittyX.Statup("Inbt", 50, 10)
                        ch_k "Um, yeah. . ."
                else:
                        $ KittyX.Statup("Love", 200, -10)
                        $ KittyX.Statup("Obed", 200, 10)
                        $ KittyX.Statup("Inbt", 50, 5)
                        $ KittyX.FaceChange("angry")
                        ch_k "I {i}was{/i} going to tell you I kinda liked it.  But I didn't think you'd be[KittyX.like]a {i}jerk{/i} about it!" #(Loss of points)
                        menu:        
                            extend ""
                            "Guess you don't know me so well, huh?":
                                    ch_k "I guess not."
                                    $ Line = "rude"
                            "Sorry.  I kind of thought you were getting into me being like that.": 
                                    $ KittyX.FaceChange("sexy", 2)
                                    $ KittyX.Eyes = "side"
                                    $ KittyX.Statup("Love", 95, 5)
                                    $ KittyX.Statup("Obed", 200, 5)
                                    $ KittyX.Statup("Inbt", 50, 5)
                                    ch_k ". . ."
     
    $ KittyX.Blush = 1       
    if not Line:
            # She's advancing to the next stage            
            ch_k "Well, I've, uhm. . . never had a guy be like that with me before. . ."
            $ KittyX.FaceChange("sly", 2)
            ch_k "I think I kinda like it."
            $ KittyX.FaceChange("smile", 1)
            menu:
                extend ""
                "Good. If you wanna be with me, that's how it'll be.":
                        if ApprovalCheck(KittyX, 1000, "LO"):
                            $ KittyX.Statup("Obed", 200, 15)
                            $ KittyX.Statup("Inbt", 50, 10)
                            ch_k "I guess I walked into that one. . ."                        
                        else:
                            $ KittyX.FaceChange("sadside", 1)
                            $ KittyX.Statup("Love", 200, -5)
                            $ KittyX.Statup("Obed", 200, 10)                      
                            ch_k "You don't have to do it[KittyX.like]{i}all{/i} the time.  You could still be nice once in a while."
                            menu:      
                                extend ""
                                "Whatever.  That's how it is.  Take it or leave it.":
                                        $ KittyX.FaceChange("angry")
                                        $ KittyX.Statup("Love", 200, -10)
                                        $ KittyX.Statup("Obed", 200, 5)
                                        ch_k "Y'know, you're such a jerk, [Player.Name]!" 
                                        $ Line = "rude"
                                "I think I could maybe do that." : 
                                        $ KittyX.FaceChange("bemused", 2)
                                        $ KittyX.Eyes = "side"
                                        $ KittyX.Statup("Love", 95, 5)
                                        $ KittyX.Statup("Obed", 200, 3)
                                        $ KittyX.Statup("Inbt", 50, 5)
                                        ch_k "Uhm. . .yeah.  It's[KittyX.like]. . kinda hot."
                                
                "Yeah?  You think it's sexy?":
                                        $ KittyX.FaceChange("bemused", 2)
                                        $ KittyX.Eyes = "side"
                                        $ KittyX.Statup("Obed", 200, 5)
                                        $ KittyX.Statup("Inbt", 50, 10)
                                        ch_k "Uhm. . .yeah.  It's[KittyX.like]. . kinda hot."
                        
                "You sure you don't want me to back off a little?":  
                        $ KittyX.FaceChange("startled", 1)
                        $ KittyX.Statup("Obed", 200, -5)
                        menu:
                            ch_k "Only if you think it might be[KittyX.like]weird. But I think it's kinda hot."
                            "Only if you're okay with it.":
                                    $ KittyX.FaceChange("bemused", 2)
                                    $ KittyX.Statup("Love", 95, 10)
                                    $ KittyX.Statup("Inbt", 50, 10)
                                    $ Line = 0
                            "Uhm. . .yeah.  I {i}do{/i} think it's weird.  Sorry.":                                
                                    $ KittyX.Statup("Love", 200, -15)
                                    $ KittyX.Statup("Obed", 200, -5)
                                    $ KittyX.Statup("Inbt", 50, -10)
                                    $ Line = "embarrassed"
                        
                "I don't really care what you like.  I do what I want.":
                            $ KittyX.Statup("Love", 200, -10)
                            $ KittyX.Statup("Obed", 200, 15)
                            $ KittyX.FaceChange("angry")
                            ch_k "Y'know, you're such a jerk, [Player.Name]!" 
                            $ Line = "rude"
                                        
    if not Line:
        $ KittyX.FaceChange("bemused", 1)
        $ KittyX.Eyes = "down"
        ch_k "Cool.  So. . .just so you know. . .I don't mind[KittyX.like]you being in control."
        if "256 Shades of Grey" in KittyX.Inventory:
                    ch_k "Like in that '256 Shades of Grey' book."
        menu Kitty_Sub_Choice:
            extend ""
            "Don't you think that relationship's kinda. . .weird?":
                    $ KittyX.Statup("Love", 200, -5)
                    $ KittyX.Statup("Inbt", 50, -15)
                    $ Line = "embarrassed"
            "I think I could get used to that kinda thing.":
                    $ KittyX.Statup("Obed", 200, 5)
                    $ KittyX.Statup("Inbt", 50, 5)
                    $ KittyX.FaceChange("smile", 1)
                    $ Line = 0
            "You actually {i}read{/i} that?" if "256 Shades of Grey" in KittyX.Inventory and Line != "grey":
                    $ KittyX.Statup("Love", 95, 5)
                    $ KittyX.FaceChange("sly", 1)
                    ch_k "You think I wouldn't read something you bought me?  I think you {i}maybe{/i} don't realize how much I like you."
                    $ KittyX.Statup("Inbt", 50, 5)
                    ch_k "Well, I {i}did{/i} read it.  And. . .it turns out it kinda[KittyX.like]. . {i}really{/i} turned me on."
                    ch_k "So. . .what d'you think?  Think[KittyX.like]maybe you'd like that?"
                    $ Line = "grey"
                    jump Kitty_Sub_Choice

    if not Line:
        $ KittyX.FaceChange("smile", 1)
        ch_k "Awesome.  So. . .if you wanted me to, I could[KittyX.like]call you {i}sir{/i} or something."
        $ KittyX.FaceChange("sly", 2)
        ch_k "Think you'd like that?"        
        $ KittyX.Blush = 1  
        menu:
            extend ""
            "That has a nice ring to it.":
                    $ KittyX.Statup("Love", 95, 5)
                    $ KittyX.Statup("Obed", 200, 15)
                    $ KittyX.Statup("Inbt", 50, 5)
                    ch_k "Okay, then. . .{i}sir{/i}."              
                    $ KittyX.Petname = "sir"
            "I think I'd rather stick with what we've got going.":
                $ KittyX.FaceChange("startled", 2)
                ch_k "Oh!"
                $ KittyX.Statup("Inbt", 50, -5)
                $ KittyX.FaceChange("sadside", 1)
                menu:
                    ch_k ". . . Well. . . maybe you can still kinda[KittyX.like]be in control, anyway?"
                    "I like that idea.":
                            $ KittyX.Statup("Obed", 200, 10)
                            $ KittyX.FaceChange("smile", 1)
                            ch_k "You're so awesome, [KittyX.Petname]."
                    "This is getting really weird.":
                            $ KittyX.Statup("Love", 200, -10)
                            $ KittyX.Statup("Obed", 200, -50)
                            $ KittyX.Statup("Inbt", 50, -15)
                            $ Line = "embarrassed"
        
#Kitty_Sub_Bad_End:
    $ KittyX.History.append("sir")
    if not Line:
            $ KittyX.Blush = 1  
            $ KittyX.Petnames.append("sir")
            #put in stuff that happens if this succeeds
    elif Line == "rude":        
            hide Kitty_Sprite with easeoutbottom                     
            call Remove_Girl(KittyX)            
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[KittyX.Name] phases through the floor in a huff, leaving you alone."
    elif Line == "embarrassed":
            $ KittyX.FaceChange("sadside", 2)
            ch_k "Oh!  Uhm, yeah! [KittyX.Like]I mean. . .."
            $ KittyX.Mouth = "smile"
            ch_k "I was just kidding.  I[KittyX.like]. . yeah.  That's kinda weird."
            ch_k "I should go.  I think I hear Professor Xavier calling me."
            $ KittyX.Blush = 1            
            hide Kitty_Sprite with easeoutbottom                     
            call Remove_Girl(KittyX)
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[KittyX.Name] phases through the floor, leaving you alone. It didn't look like she could get away fast enough."
    return

label Kitty_Sub_Asked:
    $ Line = 0
    $ KittyX.FaceChange("sadside", 1)
    ch_k "Yeah.  And I also[KittyX.like]remember what a {i}jerk{/i} you were to me about it."
    menu:
        extend ""
        "Well, I wanted to say I was sorry. And I was hoping maybe we could give it another shot.":
                if "sir" in KittyX.Petnames and ApprovalCheck(KittyX, 850, "O"): 
                        #if this is asking about the "master" name, and her Obedience is higher than 700
                        pass
                elif ApprovalCheck(KittyX, 550, "O"): 
                        #if it's instead about earning the "sir" title, and her approval is over 500 
                        pass
                else: #if it failed both those things,    
                        ch_k "Well maybe {i}I'm{/i}[KittyX.like]over that. . ." #Failed again. :(       
                        $ Line = "rude"
                        
                if Line != "rude":    
                        $ KittyX.Statup("Love", 90, 10)
                        $ KittyX.FaceChange("sly", 1)
                        ch_k "Well. . .okay.  I {i}did{/i} think that was pretty hot.  Also, you're super-cute when you apologize." 
                        #Blushing expression.  Kitty kisses player and big addition of points
                        ch_k "Okay.  We can[KittyX.like]try again." 

        "Listen. . . I know it's what you want. Do you want to try again, or not?":
                $ KittyX.FaceChange("bemused", 1)
                if "sir" in KittyX.Petnames:
                    if ApprovalCheck(KittyX, 850, "O"): 
                        ch_k "Ok, fine."
                    else: 
                        ch_k "Um, not really."
                        $ Line = "rude"
                elif ApprovalCheck(KittyX, 600, "O"): 
                        #if it's instead about earning the "sir" title, and her approval is over 500
                        $ KittyX.FaceChange("sadside", 1) 
                        ch_k "You're[KittyX.like]totally impossible."
                        $ KittyX.Eyes = "squint"
                        ch_k "Maybe you're right."
                        ch_k "But I still think you should[KittyX.like] apologize for being a jerk to me."
                        menu:
                            extend ""
                            "Okay, I'm sorry I was mean about it.":
                                            $ KittyX.Statup("Love", 90, 15)
                                            $ KittyX.Statup("Inbt", 50, 10)
                                            $ KittyX.FaceChange("bemused", 1)
                                            $ KittyX.Eyes = "side"
                                            ch_k "That's all you had to say."
                            "Not gonna happen.":
                                    if "sir" in KittyX.Petnames and ApprovalCheck(KittyX, 900, "O"): 
                                            $ KittyX.Statup("Love", 200, -5)
                                            $ KittyX.Statup("Obed", 200, 10)
                                            ch_k ". . ."
                                    elif ApprovalCheck(KittyX,650, "O"):  
                                            $ KittyX.Statup("Love", 200, -5)
                                            $ KittyX.Statup("Obed", 200, 10)
                                            ch_k "I, um. . ."    
                                    else: #if it failed both those things,     
                                            $ KittyX.Statup("Love", 200, -10)
                                            $ KittyX.Statup("Obed", 90, -10)
                                            $ KittyX.Statup("Obed", 200, -10)
                                            $ KittyX.Statup("Inbt", 50, -15)                       
                                            "Kitty sighs and rolls her eyes."
                                            $ KittyX.FaceChange("angry", 1)
                                            $ KittyX.Eyes = "side"
                                            ch_k "You really don't learn, do you?"    
                                            $ Line = "rude"
                            "Ok, never mind then.":    
                                            $ KittyX.FaceChange("angry", 1)
                                            $ KittyX.Statup("Love", 200, -10)
                                            $ KittyX.Statup("Obed", 90, -10)
                                            $ KittyX.Statup("Obed", 200, -10)
                                            $ KittyX.Statup("Inbt", 50, -15)
                                            ch_k "Y'know, if you're gonna throw that in my face, forget it."
                                            ch_k "I should've[KittyX.like]expected you'd be like that."
                                            $ Line = "rude"
    
    $ KittyX.RecentActions.append("asked sub")   
    $ KittyX.DailyActions.append("asked sub")     
    if Line == "rude":            
            #If line hasn't been set to "rude" by something above, then it skips right past this
            hide Kitty_Sprite with easeoutbottom                     
            call Remove_Girl(KittyX)
            $ KittyX.RecentActions.append("angry")
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[KittyX.Name] phases through the floor, leaving you alone.  She looked pretty upset."
    elif "sir" in KittyX.Petnames:
            #it didn't fail and "sir" was covered
            $ KittyX.Statup("Obed", 200, 50)
            $ KittyX.Petnames.append("master")  
            $ KittyX.Petname = "master"
            $ KittyX.Eyes = "sly"
            ch_k ". . . master. . ."
    else:
            #it didn't fail
            $ KittyX.Statup("Obed", 200, 30)
            $ KittyX.Petnames.append("sir")  
            $ KittyX.Petname = "sir"
            $ KittyX.Eyes = "sly"
            ch_k ". . . sir."
    return

# end Kitty_Sub//////////////////////////////////////////////////////////


# start Kitty_Master//////////////////////////////////////////////////////////

label Kitty_Master: 
    call Shift_Focus(KittyX)
    if KittyX.Loc != bg_current and KittyX not in Party:
        "Suddenly, [KittyX.Name] shows up and says she needs to talk to you."
    
    $ KittyX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(KittyX)
    call CleartheRoom(KittyX)
    $ KittyX.DailyActions.append("relationship")
    call Taboo_Level
    $ Line = 0
    $ KittyX.FaceChange("bemused", 1)
    ch_k "[KittyX.Petname], if you don't mind me saying so. . ."
    ch_k "I think having you be[KittyX.like]in control of our relationship is working out pretty awesome."
    menu:
        extend ""
        "I like it too.":
                $ KittyX.FaceChange("sly", 1)
                ch_k "Cool.  Maybe we could[KittyX.like]kick it up a notch?"
                menu:
                    extend ""
                    "Nah.  This is just about perfect.":
                            $ KittyX.FaceChange("sad", 1)
                            $ KittyX.Statup("Obed", 200, -15)
                            $ KittyX.Statup("Inbt", 50, 10)
                            ch_k "Oh.  Well, okay, I guess."     
                            $ Line = "fail"                      
                    "What'd you have in mind?":
                            $ KittyX.Eyes = "side"
                            ch_k "I dunno. I was thinking[KittyX.like]maybe I could start calling you. . . {i}master{/i}?"
                            $ KittyX.Eyes = "squint"
                            ch_k "Would you like that?  I think that'd be kinda[KittyX.like]hot."
                            menu:
                                extend ""
                                "Oh, yeah.  I'd like that.":
                                        ch_k "Cool. . ."
                                "Uhm. . .nah.  That's too much.":
                                        $ KittyX.FaceChange("sad", 1)
                                        $ KittyX.Statup("Obed", 200, -15)
                                        $ KittyX.Statup("Inbt", 50, 5)
                                        ch_k "Oh.  Well, okay, I guess."
                                        $ Line = "fail"

                    "Actually, I'd prefer we stopped doing it. I don't want to be too controlling.":
                            $ KittyX.FaceChange("sly", 1)
                            $ KittyX.Statup("Love", 200, 15)
                            $ KittyX.Statup("Obed", 200, -10)
                            $ KittyX.Statup("Inbt", 50, 10)
                            ch_k "Aw, I guess I can't get mad about that. . ."
                            $ Line = "fail"
                            
                    "Actually, let's stop that. It's creeping me out.":
                            $ KittyX.FaceChange("perplexed", 2)
                            $ KittyX.Statup("Love", 200, -10)
                            $ KittyX.Statup("Obed", 200, -50)
                            $ KittyX.Statup("Inbt", 50, -15)
                            ch_k "Oh.  Sorry.  I guess I got[KittyX.like]carried away with it."
                            $ KittyX.Blush = 1
                            $ Line = "embarrassed"
                            
        "As if I care what you think, slut.":
                $ KittyX.FaceChange("sad", 1)
                $ KittyX.Statup("Love", 200, -20)
                $ KittyX.Statup("Obed", 200, 10)
                $ KittyX.Statup("Inbt", 50, -10)
                menu:
                    ch_k "Excuse me?"
                    "Sorry. I just don't care what you want.":
                            if ApprovalCheck(KittyX, 1400, "LO"): 
                                    $ KittyX.Statup("Obed", 200, 10)
                                    ch_k "That's so. . ." 
                                    $ KittyX.FaceChange("sly", 1)
                                    $ KittyX.Statup("Love", 200, 20)
                                    $ KittyX.Statup("Inbt", 50, 15)
                                    ch_k ". . .{i}mean!{/i}" 
                            else:
                                    $ KittyX.Statup("Love", 200, -15)
                                    $ KittyX.Statup("Obed", 200, -10)
                                    $ KittyX.Statup("Inbt", 50, 5)
                                    $ KittyX.FaceChange("angry", 1)
                                    ch_k "!!!"
                                    $ Line = "rude"

                    "Sorry. I'm just trying to do the \"control\" thing.  I thought you'd like it. Too much?":
                                    $ KittyX.Statup("Love", 200, 10)
                                    $ KittyX.Statup("Obed", 200, 10)
                                    $ KittyX.Statup("Inbt", 50, 5)
                                    ch_k "Oh, okay.  Just. . .try not to be so[KittyX.like]mean about it, 'kay?" 

        "Not me.  It's kind of creepy.":
                                    $ KittyX.FaceChange("sad", 2)
                                    $ KittyX.Statup("Love", 200, -10)
                                    $ KittyX.Statup("Obed", 200, -20)
                                    $ KittyX.Statup("Inbt", 50, -25)
                                    ch_k "Oh.  Uhm. . .never mind, then."
                                    $ Line = "embarrassed"
    
    $ KittyX.History.append("master")
    if Line == "rude":
            $ KittyX.RecentActions.append("angry")
            hide Kitty_Sprite with easeoutbottom                     
            call Remove_Girl(KittyX)
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[KittyX.Name] phases through the floor in a huff.  She might have been crying."
    elif Line == "embarrassed":    
            hide Kitty_Sprite with easeoutbottom                     
            call Remove_Girl(KittyX)
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[KittyX.Name] phases through the floor, leaving you alone.  She looked really embarrassed."
    elif Line != "fail":
            $ KittyX.Statup("Obed", 200, 50)
            $ KittyX.Petnames.append("master")
            $ KittyX.Petname = "master"
            ch_k ". . .master."
    return

# end Kitty_Master//////////////////////////////////////////////////////////


# start Kitty_Sexfriend//////////////////////////////////////////////////////////

label Kitty_Sexfriend:  
    $ KittyX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(KittyX)
    call CleartheRoom(KittyX)
    $ KittyX.DailyActions.append("relationship")
    call Taboo_Level
    $ Line = 0
    $ KittyX.FaceChange("bemused", 1)
    ch_k "So, [KittyX.Petname]. . .you[KittyX.like]got a second?" #blushing expression
    menu:
            extend ""
            "Not really.":
                $ KittyX.FaceChange("angry", 1)
                ch_k "You're such a jerk, [Player.Name]!" #Angry expression.  Loss of points                
                $ KittyX.Statup("Love", 200, -20) 
                $ KittyX.Statup("Obed", 50, 3)           
                $ Line = "rude"

            "This doesn't sound good.":
                $ KittyX.FaceChange("perplexed", 1)
                ch_k "I promise.  It's nothing[KittyX.like]bad." 
                    
            "Yeah.  What's up?":
                pass
                
    if not Line: #all this gets skipped if the "rude" response was procced above
            if ApprovalCheck(KittyX, 850, "L"):                  
                    $ KittyX.FaceChange("bemused", 1)
                    ch_k "Well. . . I really like you.  You know that, right?" #Sexy expression.  This is Kitty's "High Like" response
                    menu:
                        extend ""
                        "I was kinda hoping.":
                            $ KittyX.FaceChange("sexy", 1)
                            $ KittyX.Statup("Love", 90, 10) 
                            $ KittyX.Statup("Inbt", 80, 5)    
                            ch_k "I was {i}really{/i} hoping you'd say that [KittyX.Petname]." #Blushing expression
                
                        "Really?":
                            ch_k "Uhm. . . [KittyX.like]yeah.  I really do." #Blushing expression

                        "Ugh.  Gross":
                            $ KittyX.FaceChange("angry", 1)
                            $ KittyX.Statup("Love", 200, -10) 
                            $ KittyX.Statup("Obed", 50, 5)
                            $ KittyX.Statup("Inbt", 80, -5)   
                            ch_k "Y'know, you're such an ass, [Player.Name]!" #Angry expression.  Big loss of points
                            $ Line = "rude"
                            
            elif ApprovalCheck(KittyX, 1000, "LI"): 
                    $ KittyX.FaceChange("sexy", 1)
                    ch_k "I just wanted to tell you. . .I think you're[KittyX.like]kinda cute." 
                    menu:
                        extend ""
                        "That's really nice of you to say.":
                            $ KittyX.Statup("Love", 80, 5) 
                            $ KittyX.Statup("Inbt", 80, 5)   
                            ch_k "Well, I really mean it." #Blushing expression

                        "Me?  You really think so?":
                            ch_k "Yeah.  I {i}really{/i} do." #Blushing expression
                
                        "Are you going somewhere with this?":
                            $ KittyX.FaceChange("angry")
                            ch_k "Well not anymore, I'm not!" #Angry expression.  Loss of points
                            $ Line = "rude"
                            
            else: #if it reaches this block, it's because it failed the "like" check above.                    
                    $ KittyX.Mouth = "smile"
                    $ KittyX.Brows = "sad"
                    $ KittyX.Eyes = "side"
                    ch_k "This is gonna sound[KittyX.like]really weird."
                    menu:
                        extend ""
                        "Well, you've got me intrigued.  Now you {i}have{/i} to tell me.":
                            ch_k "Promise you won't think[KittyX.like]{i}badly{/i}of me?"  #Nervous expression
                            menu:
                                extend ""
                                "[KittyX.Name]. . . I really like you.  I promise.":
                                    $ KittyX.FaceChange("smile")
                                    $ KittyX.Statup("Love", 80, 10) 
                                    $ KittyX.Statup("Inbt", 80, 5)    
                                    ch_k "Well. . . okay."  #Blushing expression.  Gain of points.

                                "Uhm. . . okay?":
                                    ch_k "Well. .  ." #Nervous expression

                                "No promises.":
                                    $ KittyX.FaceChange("perplexed",2)
                                    $ KittyX.Statup("Inbt", 80, -5)  
                                    ch_k "Uhm. . . never mind, then."  #Embarrassed expression.  Minor loss of points
                                    $ Line = "embarrassed"

                        "Uhm, I think I've had my fill of {i}weird{/i}, thanks":
                            $ KittyX.FaceChange("angry",1)
                            ch_k "Fine. [KittyX.like]whatever."
                            $ Line = "rude"
    if KittyX in Player.Harem:
            $ Line = "harem"
    if not Line: #again, if the Line has been changed to "rude" or "embarrassed" then it skips past here.                          
            ch_k "Anyway. . . I was[KittyX.like]kinda thinking. . . we get along pretty well, right?"
            menu:
                extend ""
                "Right. . . ":
                        pass
                "Okay.  Just stop.  You're creeping me out.":
                        $ KittyX.FaceChange("perplexed",2)
                        $ KittyX.Statup("Love", 200, -10) 
                        $ KittyX.Statup("Inbt", 80, -10)  
                        ch_k "Sorry.  I knew this was a mistake." #Embarrassed expression.  Minor loss of points
                        $ Line = "embarrassed"
                    
    if not Line:                
            ch_k "And we've[KittyX.like]known each other for a little while, right?"
            menu:
                extend ""
                "Right. . . ":
                        pass
                "Okay.  Just stop.  You're creeping me out.":
                        $ KittyX.FaceChange("perplexed",2)
                        $ KittyX.Statup("Love", 200, -10) 
                        $ KittyX.Statup("Inbt", 80, -10)  
                        ch_k "Sorry.  I knew this was a mistake." 
                        $ Line = "embarrassed"
    if not Line:            
            ch_k "Well. . . I was just kinda thinking. . . "
            ch_k "[KittyX.like]we could take our relationship a little further, if you wanted to."
            menu:
                extend ""
                "You mean. . . like, being {i}friends with benefits{/i}?":
                        ch_k "Kinda, yeah.  Whaddya think?" #Blushing expression
                        menu:
                            extend ""
                            "Sounds amazing!  Count me in.":
                                    $ KittyX.FaceChange("smile",1)
                                    $ KittyX.Statup("Love", 80, 10) 
                                    $ KittyX.Statup("Obed", 50, 10)
                                    $ KittyX.Statup("Inbt", 200, 50)             
                                    $ KittyX.Statup("Lust", 200, 5) 
                                    "Kitty leans in and gives you a gentle kiss on the cheek."
                                    ch_k "I can't wait to get started, [KittyX.Petname]."

                            "That may be the sluttiest thing I've ever heard in my life.":
                                    $ KittyX.FaceChange("angry",1)
                                    $ KittyX.Statup("Love", 200, -30) 
                                    $ KittyX.Statup("Obed", 50, 10)
                                    $ KittyX.Statup("Inbt", 80, -40)  
                                    ch_k "You're the biggest asshole[KittyX.like]ever, [KittyX.Petname]!" #Angry expression.  HUGE loss of points
                                    $ Line = "rude"

                "Uhm, to be honest, I'd rather not.":
                        $ KittyX.FaceChange("sadside",2)
                        $ KittyX.Statup("Obed", 50, 15)
                        $ KittyX.Statup("Inbt", 80, -15)  
                        ch_k "Oh.  Okay."  #Sad expression
                        ch_k "I[KittyX.like]think I should go now.  I've got[KittyX.like]stuff to do."
                        $ Line = "sad"
    if Line == "harem":
            ch_k "I am -totally- addicted to this dick. . ."
            $ Line = 0
    if Line == "rude":    
            $ KittyX.FaceChange("angry",1)
            $ KittyX.RecentActions.append("angry")
            $ KittyX.Statup("Love", 200, -20) 
            $ KittyX.Statup("Obed", 50, 5)
            $ KittyX.Statup("Inbt", 80, -10) 
            hide Kitty_Sprite with easeoutleft   
            $ KittyX.RecentActions.append("angry")
            "[KittyX.Name] storms off in a huff.  She seemed pretty mad at you."
    elif Line == "embarrassed":
            $ KittyX.FaceChange("perplexed",1)
            $ KittyX.Statup("Love", 200, -10) 
            $ KittyX.Statup("Obed", 50, 5)
            $ KittyX.Statup("Inbt", 80, -20)   
            hide Kitty_Sprite with easeoutbottom
            "[KittyX.Name] phases through the floor leaving you alone.  That was very strange."
    elif Line == "sad":    
            hide Kitty_Sprite with easeoutbottom
            "[KittyX.Name] phases through the floor leaving you alone.  You think you may have hurt her feelings."
    else: #if you kept Line unused throughout, then you passed all the checks, so. . .
            $ KittyX.Petnames.append("sex friend")             
            $ KittyX.FaceChange("sly",2)
            $ KittyX.Statup("Inbt", 80, 10)             
            $ KittyX.Statup("Lust", 80, 10)   
            "[KittyX.Name] leans in and passes her hand across your body."
            "As she does so, she phases her hand through your jeans, so her fingers slide along your bare skin."
            $ KittyX.Blush = 1
            ch_k "I'll definitely be seeing {i}you{/i} later, [KittyX.Petname]."  
            hide Kitty_Sprite with easeoutright
            "She passes through a nearby wall. "            
    call Remove_Girl(KittyX)
    return
    
# end Kitty_Sexfriend//////////////////////////////////////////////////////////


# start Kitty_Fuckbuddy//////////////////////////////////////////////////////////

#Not updated

label Kitty_Fuckbuddy:  
    $ KittyX.DailyActions.append("relationship")
    "Out of nowhere, you feel a hand stroking across your cock."
    "Even though you're fully dressed, it definitely feels like soft skin touching your own."
    "You glance down and see a slender arm snaked around your waist, before vanishing into your pants."
    "As you try to control your rising erection, a voice whispers into your ear,"
    ch_k "Any time, just let me know. . ."
    "-and suddenly the pressure is gone." 
    "Looking around, you don't see anyone nearby, and it doesn't look like anyone else noticed what happened."
    "Maybe you'll check up on [KittyX.Name] later. . ."
    $ KittyX.Petnames.append("fuck buddy")  
    $ KittyX.Event[10] += 1
    return
# end Kitty_Fuckbuddy//////////////////////////////////////////////////////////

# start Kitty_Daddy//////////////////////////////////////////////////////////

#Not updated

label Kitty_Daddy:      
    $ KittyX.DailyActions.append("relationship")
    call Shift_Focus(KittyX)
    call Set_The_Scene
    ch_k ". . ."
    if "dating" in KittyX.Traits or KittyX in Player.Harem:
        ch_k "Hey, so[KittyX.like]we've been dating,"  
    else:    
        ch_k "Hey, so[KittyX.like]we've been hanging out," 
    if KittyX.Love > KittyX.Obed and KittyX.Love > KittyX.Inbt:
        ch_k "and you're so sweet. . ."
    elif KittyX.Obed > KittyX.Inbt:
        ch_k "and you give me what I need. . ."
    else:
        ch_k "and I've been trying out new things. . ."        
    ch_k "So[KittyX.like]I was thinking, could I call you. . . \"daddy?\""  
    menu:
        extend ""
        "Ok, go right ahead?":            
                $ KittyX.FaceChange("smile") 
                $ KittyX.Statup("Love", 90, 25)          
                $ KittyX.Statup("Obed", 60, 10)            
                $ KittyX.Statup("Inbt", 80, 30) 
                ch_k "Great!"            
        "What do you mean by that?": 
            $ KittyX.FaceChange("bemused") 
            ch_k "I don't know, it'd kinda be hot, being your baby girl. . ."
            ch_k "Could'ya call me that?"
            menu:
                extend ""
                "Sounds interesting, fine by me.":     
                        $ KittyX.FaceChange("smile") 
                        $ KittyX.Statup("Love", 90, 17)          
                        $ KittyX.Statup("Obed", 60, 20)            
                        $ KittyX.Statup("Inbt", 80, 25) 
                        ch_k "Nice! . . daddy."  
                        $ KittyX.Petname = "daddy"
                "Could you not, please?":             
                        $ KittyX.Statup("Obed", 80, 40)            
                        $ KittyX.Statup("Inbt", 80, 20)  
                        $ KittyX.FaceChange("sad") 
                        ch_k "   . . .   "
                        ch_k "Huh. K."
                "No, that creeps me out.":    
                        $ KittyX.Statup("Love", 90, -15)          
                        $ KittyX.Statup("Obed", 80, 45)            
                        $ KittyX.Statup("Inbt", 70, 5)  
                        $ KittyX.FaceChange("angry") 
                        ch_k "Booo." 
        "No, that creeps me out.":
                        $ KittyX.Statup("Love", 90, -10)          
                        $ KittyX.Statup("Obed", 80, 40)            
                        $ KittyX.Statup("Inbt", 70, 10) 
                        $ KittyX.FaceChange("angry") 
                        ch_k "Hrmph."  
    $ KittyX.Petnames.append("daddy")
    return

# end Kitty_Daddy//////////////////////////////////////////////////////////
  

#label Kitty_Sub_SecondChance:
#    $ Line = 0
#    ch_k "So, [KittyX.Petname], I was remembering. . .[KittyX.like]how much I liked the way things used to be.  Y'know[KittyX.like]when you were really in control in our relationship.  I miss that."
#    ch_k "The way it ended. . .kinda hurt my feelings.  But I was thinking, maybe, we could try that again?  Whaddya think?"
#    menu:
#        extend ""
#        "I think you should learn how to take a hint.":
#                ch_k "You could've just[KittyX.like]said {i}no{/i}.  But instead, you had to be a jerk!" #Angry expression.  Big loss of points
#                "Kitty phases through the floor, leaving you alone.  She looked super pissed off!"
#                $ Line = "rude"

#        "Yeah, I suppose we could see how it works out.":
#                ch_k "Awesome.  I was hoping you'd say that." #Blushing expression and sir petname opened again
#                ch_k "Y'know, though. . .you were[KittyX.like]really mean about it before.  Maybe there's something you should say?"
#                menu:
#                    extend ""
#                    "You're right.  I was out of line before and I'm sorry I was a jerk.":
#                            ch_k "It's okay.  It takes guts to say that.  I totally[KittyX.like]accept your apology."  #this ends sequence
#                            $ Line = 0
                            
#                    "Not exactly.  You told me I should be more in control.  So I was.  You just took it all wrong.":
#                            ch_k "Oh!  I, uhm. . .maybe I should be the one saying they're[KittyX.like]sorry?" #Blushing expression
#                            menu:
#                                extend ""
#                                "Yeah, I think you should.":
#                                    ch_k "I'm really[KittyX.like]sorry.  Like you said, I wanted you to be more in control.  I guess I should[KittyX.like]expect you to be that way, huh?" #Sad expression
#                                    menu:
#                                        extend ""
#                                        "It's cool, [KittyX.Pet].  I understand.":
#                                                ch_k "You're[KittyX.like]amazing, [KittyX.Petname]" #Sexy expression leading to Kitty giving Player a kiss
#                                        "Uncool, [KittyX.Pet].":
#                                                "Kitty phases through the floor, leaving you by yourself.  She looked totally embarrassed."
#                                                $ Line = "embarrassed"

#                                "Naah, it's cool.  I understand.":
#                                        ch_k "You're[KittyX.like]amazing, [KittyX.Petname]" #Sexy expression leading to Kitty giving Player a kiss #I'm unsure here what code to use here to transition to a new scene.  Also I'm not sure how to "call back" to the place in this scene where I used this same response before

#                                "To tell you the truth, it kind of pissed me off.":
#                                        "I'm really sorry, [KittyX.Petname].  I would never[KittyX.like]do anything to hurt you."
#                                        "Kitty phases through the floor, leaving you by yourself.  She looked totally embarrassed." #See my earlier note about "calling back"
#                                        $ Line = "embarrassed"

#                    "You're right. . .there is.  How about:  {i}Fuck you, I'm not apologizing for shit{/i}?":
#                            ch_k "You're[KittyX.like]the biggest asshole ever!" #Angry expression.  Super-big loss of points
#                            "Kitty phases through the floor, leaving you alone.  She looked super pissed off!"
#                            $ Line = "rude"


#    return


#label Combine_BroachThreesome1:
#	$ Line = 0
#        if RogueX.LikeKitty >= 850 and KittyX.LikeRogue >= 850:
#                #Kitty and Rogue Approach Player Wanting Approval Section
#                call RogueFace("manic",1)
#                $ KittyX.FaceChange("sly")
#                "Both Rogue and Kitty approach you. It's clear from their expressions that they have something important to say to you."
#                "Though Kitty seems at ease, Rogue looks nervous. Even though it's obvious you're alone, she looks around to make sure of it."
#                ch_r "Uhm. . .Kitten, how about you do most of the talking, here? You always seem to know just what to say."
#                menu:
#                        extend ""
#                        "I'm not gonna like this, am I?":
#                                $ KittyX.FaceChange("bemused")
#                                ch_k "Relax, [KittyX.Petname]. This is[KittyX.like]totally a good thing."
#                                pass
#                        "If this is more drama, I really don't have time for it.":
#                                $ Line = "ScrewedThePooch1"
            
#                if not Line:
#                        $ KittyX.FaceChange("sly",1)
#                        ch_k "So . . . Rogue and I were[KittyX.like]talking the other night, right?"
#                        $ KittyX.FaceChange("sly",2)
#                        ch_k "We were talking about how we both like you."
#                        call RogueFace("sly",2)
#                        ch_r "{i}Really{/i} like you."
#                        $ KittyX.FaceChange("smile",1)
#                        ch_k "[KittyX.Like]{i}really{/i} really like you."
#                        "The two girls laugh between each other for a moment before composing themselves again."
#                        $ KittyX.FaceChange("sly")
#                        ch_k "Anyway . . . ever since Rogue came to the Mansion, we've been[KittyX.like]total besties."
#                        ch_k "We basically do[KittyX.like]just about everything together."
#                        ch_k "There's basically nobody in the world I feel more comfortable around."
#                        call RogueFace("smile",1)
#                        ch_r "And I feel exactly the same way about Kitty."
#                        $ KittyX.FaceChange("smile",1)
#                        ch_k "So, like I said, we were talking . . . and we started talking about how we both have[KittyX.like]something going on with you."
#                        ch_k "I told Rogue how happy you made me."
#                        ch_r "And I said almost exactly the same thing about you, [RogueX.Petname]."
#                        $ KittyX.FaceChange("down")
#                        ch_k "And we basically came to the conclusion that[KittyX.like]for one of us, it was gonna have to end."
#                        ch_k "And, even though we're really close, neither of us wanted to give you up. Even[KittyX.like]for our bestie."
#                        call RogueFace("sly",2)
#                        ch_r "So . . . Kitty came up with this crazy idea."
#                        $ KittyX.FaceChange("startled")
#                        ch_k "Huh?"
#                        $ KittyX.FaceChange("smile",1)
#                        ch_k "We[KittyX.like]{b}both{/b} came up with it."
#                        ch_k "Anyway, I'll spare you the[KittyX.like]girl talk, but we had a long discussion about the whole thing."
#                        ch_k "When we were done, we both admitted that[KittyX.like]the only person either of us were attracted to as much as you was . . ."
#                        "Kitty looks over at Rogue, waiting for her to finish her sentence."
#                        call RogueFace("sly",2)
#                        ch_r " . . . Was each other."
#                        $ KittyX.FaceChange("smile",2)
#                        ch_k "So[KittyX.like]we talked it over and decided that, if you were cool with it, we {i}both{/i} want you."
#                        ch_r ". . . At the same time."
#                        menu:
#                                extend ""
#                                "You mean, like, a threesome?":
#                                        call RogueFace("sly",2)
#                                        $ KittyX.FaceChange("sly",1)
#                                        ch_k "Basically . . . yeah."
#                                        "Kitty shrugs slightly."
#                                        ch_k "We're both a little . . . {i}curious{/i}. It's[KittyX.like]a great compromise. So we'd like to see how it would work out."
#                                        call RogueFace("surprised")
#                                        ch_r "We're not, like, lezzies or anything."
#                                        call RogueFace("sly",2)
#                                        ch_r "We're just . . . close. And comfortable. And we think this could be amazing, if it works out."
#                                        call RogueFace ("confused")
#                                        ch_r "What do {i}you{/i} think? This we could maybe try it?"
#                                        menu:
#                                                extend ""
#                                                "I think that sounds amazing! Let's do it!":
#                                                        call RogueFace("smile")
#                                                        $ KittyX.FaceChange("smile")
#                                                        "Both girls look like they could walk on air."
#                                                        "(In Kitty's case, she actually {i}{b}is{/b}{/i})"
#                                                        #Both girls kiss the Player
#                                                        $ KittyX.FaceChange("sly",1)
#                                                        "Kitty looks at Rogue and smirks."
#                                                        ch_k "See? Toldja he'd be[KittyX.like]totally cool with it."
#                                                        call RogueFace("smile",1)
#                                                        ch_r "You were right. I should have doubted {i}either{/i} of you."
#                                                        $ Line = "ItsAMagicNumber1"
#                                                "That sounds really . . . {i}awkward{/i}. I don't think so.":
#                                                        $ Line = "Threejected1"
#                                "You said all that just to tell me you're lesbians?":
#                                        $ Line = "ScrewedThePooch1"
                                    
#        elif RogueX.LikeKitty >= 850 and 849 >= KittyX.LikeRogue >= 500:
#                #Rogue Likes Kitty, Wants Player to Give Nudge Section
#                call RogueFace("sly",1)
#                $ KittyX.FaceChange("smile")
#                "Rogue and Kitty approach you. Both are clearly happy to see you."
#                "You notice that while Kitty looks totally at ease, Rogue has a wry grin on her face."
#                "It's not hard to tell that she has something on her mind -- something Kitty isn't privy to."
#                ch_k "Heya, [KittyX.Petname]!"
#                "Kitty looks at Rogue and arches a curious brow."
#                ch_k "Okay, here he is. So[KittyX.like]what's this all about now?"
#                "You have absolutely no idea what she's talking about."
#                call RogueFace("sly",2)
#                "Rogue looks around to make sure you're alone. Only when she's convinced you have some privacy does she speak."
#                ch_r "Uhm, so . . . I was telling Kitty I wanted to find you so maybe we could all have a little talk, [RogueX.Petname]."
#                $ KittyX.FaceChange("perplexed")
#                ch_k "Right . . ."
#                call RogueFace("smile",1)
#                ch_r "Well, [RogueX.Petname], you know how I told you Kitty and I were best friends, right?"
#                ch_r "Ever since I first came to the Mansion, my powers all out of control, she's stood by me."
#                ch_r "She's always been there when I needed a friend or a shoulder to cry on . . . or basically anything."
#                ch_r "Honestly . . . there's nobody in the world I feel more comfortable around."
#                $ KittyX.FaceChange("smile",2)
#                ch_k "Aww . . ."
#                ch_k "That's[KittyX.like]{i}so{/i} sweet, Rogue!"
#                $ KittyX.FaceChange("smile")
#                ch_k "I love you, too! You're[KittyX.like]the {i}best{/i} bestie!"
#                ch_r "Well . . . maybe I am, but [RogueX.Petname] is the best boyfriend ever."
#                call RogueFace("sly",2)
#                ch_r "And that's why I was . . . well . . ."
#                ch_r ". . . I was hoping we could share him, Kitten."
#                $ KittyX.FaceChange("startled",1)
#                ch_r "C'mon, Kitty. You {i}{b}told{/b}{/i} me you thought [RogueX.Petname] was hot."
#                ch_r "And I {i}know{/i} you check out Kitty, [RogueX.Petname]. I've caught you doing it, now and again."
#                $ KittyX.FaceChange("sly",1)
#                ch_r "I just thought . . . well . . . I've always kind of been curious, Kitty."
#                ch_r "And since we all get along really well . . . I thought if we could {i}all{/i} be together, it could be really amazing."
#                $ KittyX.FaceChange("sly",2)
#                ch_k "Well[KittyX.like]I dunno . . ."
#                ch_k "[KittyX.Petname] {i}is{/i} kinda cute. And I guess we do kinda get along . . ."
#                $ KittyX.FaceChange("sly",1)
#                ch_k "I dunno. [KittyX.Like]what's your thoughts on it?"
#                menu:
#                        extend ""
#                        "A threesome with the two of you? HELL, YES.":
#                                call RogueFace("smile",1)
#                                $ KittyX.FaceChange("sly",1)
#                                ch_k "Pretty enthusiastic about the idea, huh, [KittyX.Petname]?"
#                                call RogueFace("perplexed")
#                                ch_r "Well, what about you, Kitten? Do . . . you want to try?"
#                                ch_k "Are you kidding me?"
#                                $ KittyX.FaceChange("sly",2)
#                                ch_k "You're not the only one that's been {i}kinda curious{/i}."
#                                ch_k "And I've been[KittyX.like]checking out [KittyX.Petname] just as much as he's been checking me out."
#                                ch_k "So, yeah. I'm[KittyX.Like]totally in."
#                                $ Line = "ItsAMagicNumber1"
#                        "I'm not sure. I wouldn't want it to wreck what we have, [RogueX.Pet].":
#                                call RogueFace("smile")
#                                $ KittyX.FaceChange("smile")
#                                ch_k "You're right, Rogue. [KittyX.Like]best boyfriend ever."
#                                ch_k "Well . . . it'd be[KittyX.like]different, I'm sure. But I promise, I'd never get between the two of you."
#                                $ KittyX.FaceChange("sly",2)
#                                ch_k "Not unless you[KittyX.like]asked really nicely."
#                                call RogueFace("smile",1)
#                                ch_r "So . . . good enough for you, [RogueX.Petname]?"
#                                menu:
#                                        extend ""
#                                        "Good enough for me.":
#                                                #Have Kitty and Rogue kiss the Player.
#                                                call RogueFace("smile")
#                                                $ KittyX.FaceChange("smile")
#                                                ch_k "I promise not to make you[KittyX.like]regret this, [KittyX.Petname]."
#                                                $ Line = "ItsAMagicNumber1"
#                                        "I'm sorry. I just don't want to risk it.":
#                                                $ Line = "Threejected1"
#                        "Count me out. That's just too awkward for me.":
#                                $ Line = "Threejected1"
                                
#        elif KittyX.LikeRogue >= 850 and 849 >= RogueX.LikeKitty >= 500:
#                #Kitty Likes Rogue, Wants Player to Give Nudge Section
#                call RogueFace("smile")
#                $ KittyX.FaceChange("sly",1)
#                "Rogue and Kitty approach you. Both are clearly happy to see you."
#                "You notice that while Rogue looks totally at ease, Kitty has a wry grin on her face."
#                "It's not hard to tell that she has something on her mind -- something Rogue isn't privy to."
#                ch_k "Heya, [KittyX.Petname]! {i}Just{/i} who we've been looking for!"
#                call RogueFace("perplexed")
#                ch_r "Okay . . . he's here. Now, what's this all about, Kitty?"
#                ch_k "What this is about is[KittyX.like]about me and [KittyX.Petname] . . ."
#                $ KittyX.FaceChange("sexy",1)
#                ch_k ". . . And {i}you{/i}."
#                call RogueFace("startled")
#                ch_r "Wha -- ?"
#                $ KittyX.FaceChange("smile")
#                "Kitty interrupts her before she can finish the thought."
#                ch_k "[KittyX.Petname], be[KittyX.like]totally honest with me for a second, okay?"
#                ch_k "You think Rogue's[KittyX.like]kinda hot, right?"
#                menu:
#                        extend ""
#                        "Of course . . . but not as hot as you.":
#                                call RogueFace("sly",1)
#                                $ KittyX.FaceChange("smile",1)
#                                ch_r "I can see why you keep him around, Kitten."
#                                ch_k "Yeah, he can be pretty damn adorable."
#                                $ KittyX.FaceChange("smile")
#                                pass
#                        "Well, yeah!":
#                                call RogueFace("sly",1)
#                                $ KittyX.FaceChange("smile")
#                                ch_k "I {i}thought{/i} I saw you checking her out before!"
#                                $ KittyX.FaceChange("sly",1)
#                                ch_k "You're[KittyX.like]lucky that in this case -- that's a {b}good{/b} thing."
#                                pass
#                        "Uhm, to be honest . . . not so much.":
#                                call RogueFace("down")
#                                $ KittyX.FaceChange("down")
#                                ch_k "Oh. Well . . . that kind of shoots {i}that{/i} down, huh?"
#                                "You're not really sure what she means by that, but you get the impression a big opportunity might have just passed you by."
#                                $ Line = "Threejected1"

#            if not Line:
#                    call RogueFace("sly",1)
#                    $ KittyX.FaceChange("smile")
#                    ch_k "Anyway, we've established that[KittyX.like]you think Rogue's pretty hot."
#                    $ KittyX.FaceChange("sly",1)
#                    ch_k "Well . . . you're not the {i}{b}only{/b}{/i} one."
#                    call RogueFace("startled")
#                    ch_k "C'mon, Rogue . . . we're besties, right?"
#                    ch_k "We've been through so much together."
#                    ch_k "And you're absolutely {i}gorgeous{/i}."
#                    ch_k "I'm not going to lie: I'm kinda . . . {i}curious{/i} about you."
#                    ch_k "And I'm lucky enough to have[KittyX.like]the best boyfriend in the world."
#                    ch_k "[KittyX.Petname], so . . . would you be cool with bringing Rogue into what we have?"
#                    ch_k "I mean, I'm totally in love with you. But I think this might even make it better."
#                    ch_k "What d'you think?"
#                    menu:
#                            extend ""
#                            "I'm down . . . but shouldn't we ask Rogue, first?":
#                                    pass
#                            "I'm not sure. I wouldn't want it to wreck what we have, [KittyX.Pet].":
#                                    ch_k "It's[KittyX.like]totally sweet of you to think that way . . . but I think this could only be a good thing -- if we give it a chance."
#                                    ch_k "Are you[KittyX.like]willing to give it a try?"
#                                    menu:
#                                            extend ""
#                                            "If you're sure . . .":
#                                                    $ KittyX.FaceChange("smile")
#                                                    ch_k "I'm sure."
#                                                    pass
#                                            "No. I'm sorry. This is too . . . odd for me.":
#                                                    $ Line = "Threejected1"
#                            "That's just . . . ugh.  No.  No way.":
#                                    $ Line = "Threejected1"
                                    
#        if not Line:
#                ch_k "Rogue? What d'you think? You're always telling me how cute you think [KittyX.Petname] is."
#                call RogueFace("sly",2)
#                ch_r "Well . . . yeah.  That's true, I guess."
#                ch_k "And you know how happy he makes me. You could have a chance at that, too!"
#                "Rogue seems to think about it for a moment, biting her lower lip."
#                "Finally, she takes a deep breath and lets in out in a sigh."
#                ch_r "If y'all don't think I'd get in the way . . . yeah. I'd . . . I'd love to be a part of it."
#                $ KittyX.FaceChange("smile",2)
#                ch_k "So it's settled! We're not a couple anymore! We're[KittyX.like]a trio!"
#                $ Line = "ItsAMagicNumber1"
        
#        else:
#                #Girls Giggle Implication Section
#                call RogueFace("sly",1)
#                $ KittyX.FaceChange("sly",1)
#                "Both Rogue and Kitty approach you. The two of them are whispering between one other as they do."
#                "Once they're within clear earshot, they stop their conversation abruptly."
#                "You have a feeling that you're definitely the subject of the conversation."
#                "You also have a feeling that, whatever they're talking about, they're not going to let you in on it."
#                "It's definitely something for you to file away in your memory."

#	elif Line == "ScrewedThePooch1":
#		call RogueFace("smile")
#		$ KittyX.FaceChange("smile")
#		"Both girls look absolutely furious with your response."
#		"Neither one of them says anything as they turn and storm away from you."
#		"You think you might have heard them mutter something between each other, but they're too far gone to hear exactly what it was."
#		"Given their reaction, you can only imagine."
#		#Major loss of Love & Lust points from both girls

#	elif Line == "ItsAMagicNumber1":
#		call RogueFace("smile")
#		$ KittyX.FaceChange("smile")
#		"Both girls seem really happy with the way things worked out."
#		"For your part, you have a good feeling about the whole arrangement."
#		"In any case . . . it seems like coming to the Institute was the best thing that ever happened to you!"
#		#Major gain of Love & Lust points from both girls

#	elif Line == "Threejected1":
#		call RogueFace("down")
#		$ KittyX.FaceChange("down")
#		"Both girls seem pretty disappointed by your response."
#		ch_k "I guess it was[KittyX.like]too much to ask for, huh?"
#		ch_r "I'm really sorry we made things . . . {i}weird{/i} for you, [RogueX.Petname]."
#		ch_k "Maybe we can just[KittyX.like]forget it ever happened, huh?"
#		"The three of you just kind of stand there in awkward silence until, at last, both girls sort of slink away."
#		"{i}Weird{/i}.  That was about the perfect word for it."
#		#Minor loss of Love & Lust points from both girls
#        return
        

label Kitty_Yoink(Girl=0,TempBonus=0,Shy=0):  
    #this is for if Kitty is asked to steal clothing from another girl in the scene. 
    # Girl is the target, most of the variables are her starting outfit
    # Temp Bonus is 0 if Kitty thinks she'd be ok with it, high if Kitty hates her, low if Kitty doesn't hate her
    # Shy is the Taboo modifier, how embarssaing the trick will be.
    # it can be 2.5 for nudity, 2 for underwear, 1 for no exposure
    
    if "yoink" in KittyX.DailyActions:
            ch_k "We've had enough fun with that."
            return
    
    if RogueX.Loc == bg_current:
            $ Girl = RogueX
    elif EmmaX.Loc == bg_current:
            $ Girl = EmmaX
    elif LauraX.Loc == bg_current:
            $ Girl = LauraX    
            
    if EmmaX.Loc == "bg teacher" and bg_current == "bg classroom":
            #if Emma is teaching. . .
            menu:
                "About who?"
                "[Girl.Name]?" if Girl:
                        pass
                "[EmmaX.Name]":        
                        $ Girl = EmmaX
                "Never mind":
                        return
    elif not Girl:
            "I don't know who you think you could yoink from."
            return
    #end if Emma is teaching
    
    if KittyX.GirlLikeCheck(Girl) <= 200:
            $ TempBonus = 400
    elif KittyX.GirlLikeCheck(Girl) <= 400:
            $ TempBonus = 200
    elif KittyX.GirlLikeCheck(Girl) >= 800 or ApprovalCheck(Girl, 500, "I", TabM=3):
            #if she think's the girl's hot and the girl is pretty open minded. . .
            $ TempBonus = 0
    else: 
            #if she's fairly average on the girl and the girl isn't uninhibited. . .
            $ TempBonus = -400 
    
    menu:
        "Hey [KittyX.Name], why don't you snag [Girl.Name]'s. . ."
        ". . . [Girl.Over]?" if Girl.Over:
                if Girl.Chest:
                        #if she has a bra on under it
                        $ Shy = 2
                        if ApprovalCheck(KittyX, 800, TabM=2, Bonus=TempBonus): 
                            #+800 check in standard taboo
                            #she's in
                            $ Line = "over"
                        elif ApprovalCheck(KittyX, 600, TabM=2, Bonus=TempBonus):
                            #she says no, but not mad
                            $ Line = "no"
                        else:
                            #she's mad
                            $ Line = "noway"
                else:
                        #if she has no bra on under it
                        $ Shy = 3
                        if ApprovalCheck(KittyX, 800, TabM=2.5, Bonus=(TempBonus*1.5)):
                            $ Line = "over"
                        elif ApprovalCheck(KittyX, 600, TabM=1.5, Bonus=TempBonus):
                            $ Line = "no"
                        else:
                            $ Line = "noway"
                
        ". . . [Girl.Chest]?" if Girl.Chest:
                if Girl.Over:
                        #if she has a shirt on over it
                        $ Shy = 1
                        if ApprovalCheck(KittyX, 1200, TabM=1, Bonus=TempBonus): 
                            #+800 check in standard taboo
                            #she's in
                            $ Line = "chest"
                        elif ApprovalCheck(KittyX, 600, TabM=0.5, Bonus=TempBonus):
                            #she says no, but not mad
                            $ Line = "no"
                        else:
                            #she's mad
                            $ Line = "noway"
                else:
                        #if she has no shirt on over it
                        $ Shy = 3
                        if ApprovalCheck(KittyX, 800, TabM=2.5, Bonus=(TempBonus*1.5)):
                            $ Line = "chest"
                        elif ApprovalCheck(KittyX, 600, TabM=1.5, Bonus=TempBonus):
                            $ Line = "no"
                        else:
                            $ Line = "noway"
                
        ". . . [Girl.Legs]?" if Girl.Legs:
                if Girl.Panties or Girl.HoseNum() >= 10:
                        #if she has panties or tights on under it
                        $ Shy = 2
                        if ApprovalCheck(KittyX, 1000, TabM=2, Bonus=TempBonus): 
                            #+800 check in standard taboo
                            #she's in
                            $ Line = "legs"
                        elif ApprovalCheck(KittyX, 800, TabM=2, Bonus=TempBonus):
                            #she says no, but not mad
                            $ Line = "no"
                        else:
                            #she's mad
                            $ Line = "noway"
                else:
                        #if she has no panties or tights on under it
                        $ Shy = 3
                        if ApprovalCheck(KittyX, 1000, TabM=2.5, Bonus=(TempBonus*1.5)):
                            $ Line = "legs"
                        elif ApprovalCheck(KittyX, 800, TabM=1.5, Bonus=TempBonus):
                            $ Line = "no"
                        else:
                            $ Line = "noway"
                            
        ". . . [Girl.Panties]?" if Girl.Panties:
                if Girl.Legs or Girl.HoseNum() >= 10:
                        #if she has legs or tights on over it
                        $ Shy = 1
                        if ApprovalCheck(KittyX, 1000, TabM=1, Bonus=TempBonus): 
                            #+800 check in standard taboo
                            #she's in
                            $ Line = "panties"
                        elif ApprovalCheck(KittyX, 800, TabM=0.5, Bonus=TempBonus):
                            #she says no, but not mad
                            $ Line = "no"
                        else:
                            #she's mad
                            $ Line = "noway"
                else:
                        #if she has no legs or tights on over it
                        $ Shy = 3
                        if ApprovalCheck(KittyX, 1000, TabM=2.5, Bonus=(TempBonus*1.5)):
                            $ Line = "panties"
                        elif ApprovalCheck(KittyX, 800, TabM=1.5, Bonus=TempBonus):
                            $ Line = "no"
                        else:
                            $ Line = "noway"
                
        ". . . [Girl.Hose]?" if Girl.Hose:
                if Girl.Legs:
                        #if she has legs on over it
                        $ Shy = 1
                        if ApprovalCheck(KittyX, 800, TabM=1, Bonus=TempBonus): 
                            #+800 check in standard taboo
                            #she's in
                            $ Line = "hose"
                        elif ApprovalCheck(KittyX, 800, TabM=0.5, Bonus=TempBonus):
                            #she says no, but not mad
                            $ Line = "no"
                        else:
                            #she's mad
                            $ Line = "noway"
                elif Girl.Panties or Girl.HoseNum() < 10:
                        #if she has panties on under it 
                        $ Shy = 2
                        if ApprovalCheck(KittyX, 1000, TabM=2, Bonus=TempBonus): 
                            #+800 check in standard taboo
                            #she's in
                            $ Line = "hose"
                        elif ApprovalCheck(KittyX, 800, TabM=2, Bonus=TempBonus):
                            #she says no, but not mad
                            $ Line = "no"
                        else:
                            #she's mad
                            $ Line = "noway"
                else:
                        #if she has no legs or panties on over it
                        $ Shy = 3
                        if ApprovalCheck(KittyX, 1000, TabM=2.5, Bonus=(TempBonus*1.5)):
                            $ Line = "hose"
                        elif ApprovalCheck(KittyX, 800, TabM=1.5, Bonus=TempBonus):
                            $ Line = "no"
                        else:
                            $ Line = "noway"
                        
        "Never mind.":
                return
    
    if Line == "no":
            $ KittyX.FaceChange("sadside",1)            
            $ KittyX.Statup("Love", 90, -(Shy))   
            ch_k "I really couldn't do that to her."
            return
    if Line == "noway":
            $ KittyX.FaceChange("angry",1)      
            $ KittyX.Statup("Love", 90, -(2*Shy))        
            $ KittyX.Statup("Obed", 60, -(Shy))    
            ch_k "How could you[KittyX.like]even {i}consider{/i} something like that?"
            return
    #else, she agrees. . .
               
    $ KittyX.Statup("Obed", 70, Shy) 
    $ KittyX.Statup("Inbt", 80, Shy)     
    "[KittyX.Name] sneaks up behind [Girl.Name]. . ."
    
    $ Girl.FaceChange("surprised",2)
    if Line == "over":
                $ Line = Girl.Over
                $ Girl.Over = 0
                call expression Girl.Tag + "_First_Topless" pass (1)
                "She reaches out and snags [Girl.Name]'s [Line], tugging it through her body."
        
    elif Line == "chest":
                $ Line = Girl.Chest
                $ Girl.Chest = 0
                call expression Girl.Tag + "_First_Topless" pass (1)
                if Girl.Over:
                    "She reaches through [Girl.Name]'s [Girl.Over] and snags her [Line]."
                else:
                    "She reaches out and snags [Girl.Name]'s [Line], tugging it free."
            
    elif Line == "legs":
                $ Line = Girl.Legs
                $ Girl.Legs = 0
                call expression Girl.Tag + "_First_Bottomless" pass (1)
                "She reaches down and snags [Girl.Name]'s [Line], tugging them through her body."
            
    elif Line == "panties":
                $ Line = Girl.Panties
                $ Girl.Panties = 0
                call expression Girl.Tag + "_First_Bottomless" pass (1)
                if Girl.Legs:
                    "She reaches down through [Girl.Name]'s [Girl.Legs] and snags her [Line]."
                elif Girl.Hose:
                    "She reaches down through [Girl.Name]'s [Girl.Hose] and snags her [Line]."
                else:
                    "She reaches out and snags [Girl.Name]'s [Line], tugging them free."
    elif Line == "hose":
                $ Line = Girl.Hose
                $ Girl.Hose = 0    
                call expression Girl.Tag + "_First_Bottomless" pass (1)
                if Girl.Legs:
                    "She reaches down through [Girl.Name]'s [Girl.Legs] and snags her [Line]."
                else:
                    "She reaches out and snags [Girl.Name]'s [Line], tugging them free."
    
    "She then dashes back a few steps, slipping the [Line] behind her back."
    
    call Activity_Check(Girl,KittyX,1,0,2) #Girl=Girl,Girl2=KittyX,Silent=1,Removal=0,ClothesCheck=2)    
    $ Approval = _return
    
    $ KittyX.DailyActions.append("yoink")
    if "yoink" not in KittyX.History:
            $ KittyX.History.append("yoink")
            
    if "exhibitionist" in Girl.Traits:   
            $ Approval = 2
    $ Girl.DailyActions.append("yoink")
                    
    if Shy <= 1:
            #if you remove a bra, hose, or panties without exposing anything
            if Approval >= 2:  
                    #this girl's amused by this
                    $ Girl.FaceChange("sly")
                    $ Girl.Statup("Inbt", 80, Shy)  
                    $ Girl.Statup("Lust", 80, 2) 
                    "[Girl.Name] glances back in surprise, but then breaks into a quick smile."
            elif Approval: 
                    #this girl's annoyed
                    $ Girl.FaceChange("angry",1)
                    $ Girl.Statup("Love", 90, -(Shy)) 
                    "[Girl.Name] glances back in surprise, and then glances over at you with a glare."
            else:
                    $ Girl.FaceChange("angry",2)
                    $ Girl.Statup("Love", 90, -(Shy)) 
                    "[Girl.Name] glances back in surprise, and then glances over at you with a glare."
                    "She storms away in disgust."
            
    elif Shy <= 2:
            #if you expose bra or panties, but no nudity
            if Approval >= 2: 
                    #this girl's amused by this
                    $ Girl.FaceChange("sly")
                    $ Girl.Statup("Inbt", 80, Shy) 
                    $ Girl.Statup("Lust", 80, Shy) 
                    "[Girl.Name] glances back in surprise, but then breaks into a quick smile."
                    "She then just leans back, unconcerned."
            elif Approval: 
                    #this girl's annoyed
                    $ Girl.FaceChange("angry",1)
                    $ Girl.Statup("Love", 90, -(Shy)) 
                    $ Girl.Statup("Inbt", 80, -(Shy))  
                    $ Girl.Statup("Lust", 80, Shy) 
                    "[Girl.Name] glances back in surprise, and then glances over at you with a glare."
                    $ Girl.FaceChange("sadside",2)
                    "She settles back down with a little embarassment."
            else:
                    $ Girl.FaceChange("angry",2)
                    $ Girl.Statup("Love", 90, -(Shy)) 
                    $ Girl.Statup("Inbt", 80, -(Shy)) 
                    "[Girl.Name] glances back in surprise, and then glances over at you with a glare."
                    "She dashes away in embarassment."
    else:
            #if you strip part of her nude
            if Approval >= 2: 
                    #this girl's amused by this
                    $ Girl.FaceChange("sly")
                    $ Girl.Statup("Love", 90, 1) 
                    $ Girl.Statup("Inbt", 80, Shy)  
                    $ Girl.Statup("Lust", 80, 2*Shy) 
                    "[Girl.Name] glances back in surprise, but then breaks into a quick smile."
                    "She looks around, daring anyone to comment." 
            elif Approval: 
                    #this girl's annoyed
                    $ Girl.FaceChange("angry",2)
                    $ Girl.Statup("Love", 90, -(Shy)) 
                    $ Girl.Statup("Inbt", 80, -(Shy)) 
                    "[Girl.Name] glances back in surprise, and then glances over at you with a glare."
                    "She seems really mortified, but stands her ground."
            else:
                    $ Girl.FaceChange("angry",2)
                    $ Girl.Statup("Love", 90, -(Shy)) 
                    $ Girl.Statup("Inbt", 80, -(Shy)) 
                    "[Girl.Name] glances back in surprise, and then glances over at you with a glare."
                    "She dashes away in embarassment."
        
        
    #if the girl is embarassed
    if Approval:
            $ Girl.GLG(KittyX,900,(2*Shy),1)
            $ KittyX.GLG(Girl,900,(2*Shy),1)
    else:
            call Remove_Girl(Girl)
            $ Girl.GLG(KittyX,900,-(2*Shy),1)
               
    if TempBonus > 0:
            if Approval < 2: 
                #she didn't like the girl, and drove her off.
                $ KittyX.FaceChange("sly")
                $ KittyX.Statup("Love", 80, 1) 
                "[KittyX.Name] smiles triumphantly."
            else:
                #she didn't like the girl, but the girl was fine
                $ KittyX.FaceChange("angry",Eyes="side")
                "[KittyX.Name] seems a bit annoyed at [Girl.Name]'s attitude."
            
    elif not Approval:
                #she liked the girl well enough, but drove her off
                $ KittyX.FaceChange("sly")
                $ KittyX.Statup("Lust", 80, Shy) 
                "[KittyX.Name] seems a bit uncertain about the whole thing."
    else:
                #she liked the girl well enough, and the girl was fine
                $ KittyX.FaceChange("sly")
                $ KittyX.Statup("Love", 80, 1) 
                $ KittyX.Statup("Lust", 80, Shy) 
                "[KittyX.Name] laughs under her breath and waggles the [Line] at you."
    return
            

# start Kitty_Sexfriend//////////////////////////////////////////////////////////

label Kitty_Kate:  
        $ KittyX.Loc = bg_current
        call Set_The_Scene(0)
        call Display_Girl(KittyX)
        call Taboo_Level
        $ Line = 0
        $ KittyX.FaceChange("bemused", 1)    
        ch_k "Hey, [KittyX.Petname]. . .you[KittyX.like]got a second?"
        menu:
                extend ""
                "Not really.":
                    $ KittyX.FaceChange("angry", 1)
                    ch_k "You're such a jerk, [Player.Name]!"                
                    $ KittyX.Statup("Love", 200, -10) 
                    $ KittyX.Statup("Obed", 50, 3)   
                        
                "Yeah.  What's up?":
                    pass
        $ KittyX.Names.append("Kate")
        ch_k "I just wanted to let you know, I'm going by \"Kate\" now!"
        $ KittyX.Name = "Kate"
        menu:
            extend ""
            "Oh no you aren't.":
                    $ KittyX.Statup("Love", 90, -10) 
                    $ KittyX.Statup("Obed", 50, 10)
                    $ KittyX.Statup("Inbt", 80, -10)  
                    $ KittyX.FaceChange("angry", 2)
                    ch_k "!!!"
                    if ApprovalCheck(KittyX, 1200, "LO") or ApprovalCheck(KittyX, 500, "O"):
                            $ KittyX.Name = "Kitty"
                            $ KittyX.FaceChange("sadside", 1)
                            $ KittyX.Statup("Obed", 90, 10)
                            $ KittyX.Statup("Inbt", 80, -5)  
                            ch_k "Well. . . ok. . ."
                    else:
                            ch_k "You're not my supervisor!"                    
            "That's a good fit for you.":
                    $ KittyX.FaceChange("smile", 1)
                    $ KittyX.Statup("Love", 60, 5) 
                    $ KittyX.Statup("Love", 90, 5) 
                    $ KittyX.Statup("Inbt", 60, 5)  
                    ch_k "Thanks!"
            "I always thought \"Kitty\" sounded pretty.":
                    $ KittyX.Name = "Kitty"
                    $ KittyX.Statup("Love", 90, 5) 
                    $ KittyX.Statup("Obed", 70, 5)
                    $ KittyX.Statup("Inbt", 50, 5)  
                    ch_k "Oh, well I guess if you really like \"Kitty,\" I can understand that. . ."
            "Why?":
                    $ KittyX.Names.append("Katherine")
                    ch_k "Well, my full name is \"Katherine Pryde\", and I thought \"Kate\" sounded more grown-up."
                    menu:
                        extend ""
                        "Oh, ok then.":
                                $ KittyX.FaceChange("smile", 1)
                                $ KittyX.Statup("Love", 60, 5) 
                                $ KittyX.Statup("Love", 90, 5) 
                                $ KittyX.Statup("Inbt", 60, 5)   
                                ch_k ". . ."
                        "No, it sounds silly.":
                                $ KittyX.Statup("Love", 90, -10) 
                                $ KittyX.Statup("Obed", 50, 10)
                                $ KittyX.Statup("Inbt", 80, -10)  
                                $ KittyX.FaceChange("angry", 2)
                                ch_k "!!!"
                                if ApprovalCheck(KittyX, 1200, "LO") or ApprovalCheck(KittyX, 500, "O"):
                                        $ KittyX.Name = "Kitty"
                                        $ KittyX.FaceChange("sadside", 1)
                                        $ KittyX.Statup("Obed", 90, 10)
                                        $ KittyX.Statup("Inbt", 80, -5)  
                                        ch_k "Well. . . ok. . ."
                                else:
                                        ch_k "You're not my supervisor!"    
                        "I suppose, but \"Kitty\" is such a pretty name.":
                                $ KittyX.Statup("Love", 90, 5) 
                                $ KittyX.Statup("Inbt", 50, 5)  
                                if ApprovalCheck(KittyX, 800, "LO"):
                                        $ KittyX.Name = "Kitty"
                                        $ KittyX.Statup("Obed", 70, 5)
                                        ch_k "Well, I guess if you prefer it. . ."
                                else:
                                        ch_k "Well. . . too bad."
                        "Why not \"Katherine\" then?":
                                $ KittyX.Statup("Obed", 70, 5)
                                if ApprovalCheck(KittyX, 1200, "LO") or ApprovalCheck(KittyX, 500, "0"):
                                        $ KittyX.Name = "Katherine"
                                        $ KittyX.Statup("Obed", 90, 5)
                                        ch_k "I suppose I could. . ."
                                else:
                                        ch_k "I don't really like it that much. . ."
                                        menu:
                                            extend ""
                                            "Ok, \"Kate\" it is then.":
                                                    $ KittyX.Name = "Kate"
                                                    $ KittyX.FaceChange("smile", 1)
                                                    $ KittyX.Statup("Love", 60, 5) 
                                                    $ KittyX.Statup("Love", 90, 5) 
                                                    $ KittyX.Statup("Inbt", 60, 5)  
                                                    ch_k ". . ."
                                            "Ok, then back to \"Kitty?\"":
                                                    $ KittyX.Statup("Love", 90, 5) 
                                                    $ KittyX.Statup("Inbt", 50, 5)  
                                                    if ApprovalCheck(KittyX, 800, "LO"):
                                                            $ KittyX.Name = "Kitty"
                                                            $ KittyX.Statup("Obed", 70, 5)
                                                            ch_k "I suppose, if you prefer it that way. . ."
                                                    else:
                                                            ch_k "Well. . . too bad."
                                #end "why not Katherine"
                    #end "why?"
        #end menu
        return
    
# end Kate//////////////////////////////////////////////////////////
