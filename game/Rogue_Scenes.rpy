# Prologue //////////////////////////////////////////////////////////////////////

label Prologue: 
    $ bg_current = "bg study"  
    $ Current_Time = "Evening"
    call Display_Background
    if "Historia" in Player.Traits: #Simulation haze
                show BlueScreen onlayer black   
    "You recently discovered that you were a mutant when a Sentinel attacked your home.\nYou were rescued by a squad of X-Men and given this address."
    "You've arrived in the early evening at the Xavier Institute, where you've been promised a new home."
    "Things have been tough for mutants in the years since Apocalypse's fall, but this sounds like it might be a good deal."
    if "Historia" not in Player.Traits:
            python:
                Player.Name  = renpy.input("What is your name?", default="Zero", length = 10)
                Player.Name  = Player.Name .strip()        
                if not Player.Name :
                    Player.Name  = "Zero"
                if Player.Name in ("master", "sir", "lover", "boyfriend", "sex friend", "fuck buddy"):
                    Line = "Nice try, smartass."
                    Player.Name  = "Zero"    
            if Line:
                "[Line]"        
            menu:
                "What is your skin color?"        
                "Green":
                    $ Player.Color = "green"
                "White":
                    $ Player.Color = "pink"
                "Black":
                    $ Player.Color = "brown"
    show Professor at SpriteLoc(StageLeft)
    with dissolve
    ch_x "Welcome to the Xavier Institute for Higher Learning. This is a home for all mutants to learn and grow."
    ch_x "My name is Charles Xavier, and I have dedicated my life to helping other mutants such as yourself."
    ch_x "I know that you've had a difficult time, but you will be safe here."
    ch_x "You'll have classes in the day to teach you the skills you'll need, and training in the danger room for self defense."
    ch_x "Since you're on your own, we'll provide a small stipend for your day-to-day needs."
    ch_x "Did you have any questions for me young man?"    
    ch_p "Why did you even bring me here, I don't have any \"super powers.\""
    ch_x "Nonsense, my boy. You have an incredibly useful ability. . ."
    ch_x "the power to negate other powers, even including my own."
    $ RogueX.Loc = bg_current
    $ RogueX.FaceChange("surprised")
    $ RogueX.SpriteLoc = StageFarRight
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc)
    with easeinright
    ch_r "What's that Prof? This new kid can negate mutant powers?" 
    $ RogueX.Mouth = "normal"
    $ RogueX.SpriteLoc = StageRight
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) with ease
    ch_r "Maybe even my own?"
    ch_x "That is correct, [RogueX.Name], though currently, his powers are weak and uncontrolled."
    ch_x "One day, however, he may even be able to help you turn your powers off permanently."
    ch_r "! . . ."
    $ RogueX.FaceChange("smile")
    ch_x "Since you're here, why don't you show our new guest around the mansion?"
    
    ch_x "This young lady is named [RogueX.Name], one of our veteran students."
    ch_x "And [RogueX.Name], this young man goes by the name \"[Player.Name]\"."
    
    hide Professor
    with easeoutright
    
    $ RogueX.SpriteLoc = StageCenter
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc)  
    with ease
    $ ActiveGirls.append(RogueX) if RogueX not in ActiveGirls else ActiveGirls
    
    menu:
        ch_r "A pleasure ta meet ya, [RogueX.Petname]. Let me give ya the lay of the place." 
        "It's nice to meet you too.":
                $ RogueX.Statup("Love", 200, 20)
                $ RogueX.FaceChange("smile", 1)
                ch_r "Oh, a gentleman. I think we'll really get along."                          
                $ RogueX.Blush = 0
                ch_r "Ok, so let me show ya around. . ."
        "The \"lay\" of the place, eh?":
                $ RogueX.Statup("Love", 200, 10)
                $ RogueX.Brows = "normal"     
                $ RogueX.Eyes = "surprised"
                $ RogueX.Mouth = "smile"
                $ RogueX.Blush = 1
                ch_r "Wha- what? N, no, that's not what I meant! I'm just giving you the campus tour!"
                $ RogueX.FaceChange("bemused")
                $ RogueX.Statup("Inbt", 200, 20)
                $ RogueX.Statup("Obed", 200, 20)
                ch_r "Hmm. . ."           
                $ RogueX.Statup("Lust", 90, 3)
                $ RogueX.FaceChange("normal")
                $ RogueX.Eyes = "surprised"
                ch_r "Anyways, let's get this back on track. . ."
                $ RogueX.FaceChange("smile", 0)
        "Whatever.":            
                $ RogueX.Statup("Obed", 200, 20)
                $ RogueX.FaceChange("sad")
                $ RogueX.Brows = "normal"
                ch_r "Tsk, well ok, let's get started."
        "Screw off.":
                $ RogueX.Statup("Love", 200, -30)
                $ RogueX.Statup("Obed", 200, 30)
                $ RogueX.FaceChange("angry")
                show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc)  
                with vpunch
                ch_r "Well I never!"
                ch_r "Hmph, I have to give the tour anyways, so get mov'in. . ."
          
        
# End Prologue //////////////////////////////////////////////////////////////////////

# Tour //////////////////////////////////////////////////////////////////////
label tour_start:
    $ bg_current = "bg campus"    
    $ RogueX.Loc = bg_current
    call Set_The_Scene(0)
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc)  
    ch_r "This is the campus square. It links up to all the major locations on campus and you'll probably pass through here a lot."


# Player's room
    $ bg_current = "bg player" 
    $ RogueX.Loc = bg_current   
    call Set_The_Scene(0)
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc)  
    ch_r "This will be your room, we each get private rooms now that the campus has been expanded."
    menu:
        ch_r "Pretty nice, right?"
        "It is with you in it.":            
                $ RogueX.Blush = 1
                $ RogueX.Statup("Love", 200, 20)
                $ RogueX.Statup("Lust", 90, 5)
        "It'll do.":
                $ RogueX.Statup("Obed", 200, 10)
    ch_p "And where do you live?"
    $ RogueX.Blush = 0
    ch_r "Oh, right down the hall, all the doors are labeled."
    if RogueX.Love <= 500:
            ch_r "I wouldn't recommend bothering me though."
    else:
            ch_r "You can stop by sometime, but not after curfew."
    
# Classrooms
    $ bg_current = "bg classroom"  
    $ RogueX.Loc = bg_current 
    call CleartheRoom("All",0,1)
    call Set_The_Scene(0)
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc)  
    ch_r "And this is one of our state-of-the-art classrooms." 
    ch_r "They're multi-purpose so they can teach almost anything in them."
    ch_r "This used to just be an after school training facility, but over the past few years it's grown into a full service university."


# Danger Room
    $ bg_current = "bg dangerroom"   
    $ RogueX.Loc = bg_current
    call Set_The_Scene(0)
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc)  
    ch_r "And this is the Danger Room. It's been upgraded to a fully holographic experience, allowing realistic battlefield simulations."
    $ Count = 0
    while Count < 3:
        menu:
            extend ""
            "Why would you need battlefield simulations?" if Count != 1:
                    ch_r "The world is a dangerous place, [RogueX.Petname], especially for us mutants."
                    ch_r "This place helps us train to use our powers. Coming here can help you to get a grasp on yours as well."
                    $ Count = 3 if Count == 2 else 1
            "So can this place make some more. . . erotic simulations?" if Count != 2:
                    $ RogueX.Eyes = "side"
                    $ RogueX.Mouth = "lipbite"
                    $ RogueX.Blush = 1
                    $ RogueX.Statup("Inbt", 200, 30)
                    $ RogueX.Statup("Lust", 200, 5)
                    ch_r "Well. . . I suppose it could. . . if one were into such things."
                    $ RogueX.FaceChange(B=0)
                    $ Count = 3 if Count == 1 else 2
            "Ok, let's move on.":
                    $ Count = 3        
    $ Count = 0
    ch_r "Moving on then. . ."

label tour_end: 
    $ bg_current = "bg campus"  
    $ RogueX.Loc = bg_current 
    call Set_The_Scene(0)
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc)  
    ch_r "Well, that's the nickel tour, now you know where everything is. . ."
    $ RogueX.Mouth = "normal"
    $ RogueX.Eyes = "normal"
    $ RogueX.Brows = "confused"
    menu:
        ch_r "I was curious about your ability. Is it true that other mutant powers don't work on you?"
        "Sure.":
                ch_p "That's what they tell me, but to be honest, I don't know much about it."
        "What's it to you?":
                ch_p "What do you care?"
                $ RogueX.Eyes = "sexy"
                ch_r ". . ."
                $ RogueX.Statup("Love", 200, -30)
    ch_r "Well, you see, my power is the ability to absorb the mutant powers and memories of those I touch."
    $ Head = 0
    ch_r "Only, I still can't really control it. I can't touch people without hurting them, and I might even put them into a coma if I'm not careful."
    ch_r "So I was hoping that maybe with your power. . ."
    $ RogueX.FaceChange("sexy")
    $ RogueX.Brows = "sad"    
    menu:
        ch_r "So I was hoping that maybe with your power. . . I could touch you?"
        "Like, a Kiss?":
            if RogueX.Love >= 500:    
                    $ RogueX.Statup("Love", 200, 20)
                    $ RogueX.Statup("Obed", 200, 30)
                    $ RogueX.Statup("Inbt", 20, 20)
                    $ RogueX.FaceChange("surprised", 1)
                    ch_r "Well, aren't you fresh." 
                    $ RogueX.FaceChange("sexy")
                    $ RogueX.Mouth = "smile"
                    ch_r "Just this once."
                    $ RogueX.FaceChange("kiss") 
                    call Rogue_Kissing_Smooch
                    "She gives you a little peck on the cheek."
                    $ RogueX.FaceChange("smile")
            else:
                    $ RogueX.Statup("Love", 200, 30)
                    $ RogueX.FaceChange("bemused")
                    ch_r "Heh, You'll have to earn that [RogueX.Petname]."                
                    $ RogueX.Arms = 0
                    $ RogueX.ArmPose = 2          
                    $ RogueX.FaceChange("sexy")
                    $ RogueX.Brows = "sad"
                    "She pulls off her glove and touches your face."      
        "Ok, be my guest.":        
                $ RogueX.Statup("Love", 200, 30)
                $ RogueX.FaceChange("smile")
                $ RogueX.Arms = 0
                $ RogueX.ArmPose = 2
                $ RogueX.FaceChange("sexy")
                $ RogueX.Brows = "sad"
                "She pulls off her glove and touches your face."
        "No, that's weird.":       
                $ RogueX.Statup("Love", 200, -30)
                $ RogueX.Statup("Inbt", 200, 30)
                $ RogueX.FaceChange("sad")
                $ RogueX.Brows = "normal"
                ch_r "Well I'm just too damned curious, sorry."
                $ RogueX.Arms = 0
                $ RogueX.ArmPose = 2
                "She pulls off her glove and touches your face."
    
    $ RogueX.FaceChange("surprised")
    ch_r "Wow."
    ch_r "This is amazing! With anyone else I would have drained their powers and they'd be out by now."
    $ RogueX.FaceChange("sexy")    
    menu:
        ch_r "Do you know how long it's been since I've felt human contact without hurting them?"
        "Glad I could help.":
                $ RogueX.Statup("Love", 200, 10)
        "I'm guessing it's been quite a while.":
                $ RogueX.Statup("Lust", 200, 5)
                $ RogueX.FaceChange("bemused", 1)
                ch_r ". . ."
    $ RogueX.FaceChange("smile")   
    ch_r "What a rush. I guess that's it then, I'm heading back to my room, you can head to yours."
    $ RogueX.Blush = 0
    if RogueX.Love >= 500:
        ch_r "Maybe I'll see you around though. Here's my number, you can give me a call."        
        if "Historia" not in Player.Traits:
                $ Digits.append(RogueX)
    $ RogueX.Arms = "gloves"
    $ RogueX.ArmPose = 1
    $ RogueX.Addictionrate = 5
    
label tour_parting:
    $ RogueX.Emote = "normal"
    $ RogueX.Blush = 0
    $ RogueX.Loc = "bg rogue"
    if not RogueX.Kissed:
            $ Line = "Want to make out a little?"
    else:
            $ Line = "Want to make out a little more?"
    menu:
        extend ""
        "Ok, See you later.":
            "You head back to your room."
        "[Line]":
            if RogueX.Love >= 560:
                $ RogueX.FaceChange("bemused", 1)
                $ RogueX.Statup("Inbt", 10, 20)
                $ RogueX.Statup("Inbt", 50, 10)                
                if "Historia" in Player.Traits:
                        return 1
                call Makeout(RogueX)
                if "angry" in RogueX.RecentActions:                    
                        $ RogueX.Statup("Love", 200, -10)
                        $ RogueX.Statup("Obed", 200, 30)
                        ch_r "What the hell, [Player.Name]?!"
                        ch_r "Way to take advantage of a girl's feelings there!"             
                        hide Rogue_Sprite with easeoutright
                        "[RogueX.Name] tears off and you head back to your room."
                else:
                        $ RogueX.FaceChange("bemused", 1)
                        ch_r "That was real nice, [RogueX.Petname]. I'll definitely be seeing you later."                
                        hide Rogue_Sprite with easeoutright
                        "You head back to your room."
                        $ RogueX.Emote = "normal"
            else:
                if RogueX.Love >= 530 or RogueX.Obed > 50 and not RogueX.Kissed:
                        $ RogueX.Addictionrate += 1
                        $ RogueX.Statup("Lust", 200, 5)
                        $ RogueX.Statup("Love", 200, 10)
                        $ RogueX.Kissed += 1
                        $ RogueX.FaceChange("bemused", 1)
                        ch_r "Well, maybe one kiss."
                        $ RogueX.FaceChange("kiss")
                        "She gives you a quick kiss. No tongue."                    
                        jump tour_parting
                else: 
                        $ RogueX.FaceChange("bemused")
                        ch_r "Nah, I think you've had enough for today, [RogueX.Petname]."
                        "You head back to your room."
                        hide Rogue_Sprite
                        $ RogueX.Emote = "normal"
    
    if "Historia" in Player.Traits:
            return 0        
    call Wait            
    $ bg_current = "bg player"  
    call Set_The_Scene
    "This is a short tutorial on the game's features. Feel free to skip it, you can always view it later in this room."
    call Tutorial    
    jump Player_Room    
return

# End Tour //////////////////////////////////////////////////////////////////////

            
# Event Rogue_Caught_Masturbating  /////////////////////////////////////////////////////  
#label Rogue_Caught_Masturbating: #redirect to Girl_Caught_Mastubating(RogueX) 
       

# Event Rogue_Key /////////////////////////////////////////////////////  
label Rogue_Key:
            call Shift_Focus(RogueX)
            call Set_The_Scene
            $ RogueX.FaceChange("bemused")
            $ RogueX.ArmPose = 2
            ch_r "Hey, you've been sleeping over a lot, I figured you might want a key?"
            ch_p "Thanks."
            $ RogueX.ArmPose = 1    
            $ Keys.append(RogueX)
            $ RogueX.Event[0] = 1
            return
# end Event Rogue_Key /////////////////////////////////////////////////////

# start Rogue_BF//////////////////////////////////////////////////////////
label Rogue_BF:
    call Shift_Focus(RogueX)
    
    if RogueX.Loc != bg_current and RogueX not in Party:
        "Suddenly, [RogueX.Name] shows up and says she needs to talk to you."    
                
    $ RogueX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(RogueX)
    call CleartheRoom(RogueX)
    call Taboo_Level
    $ RogueX.DailyActions.append("relationship")
    $ RogueX.FaceChange("bemused", 1)
    ch_r "So, [RogueX.Petname], we've been hanging out for a while now."
    ch_r ". . ."
    $ RogueX.Eyes = "sexy"
    menu:
        ch_r "Right?"
        "Yeah, it's been great.":
            $ RogueX.Statup("Love", 200, 20)
        "Yeah, I guess":
            $ RogueX.Statup("Love", 200, 10)
        "Um, maybe?":
            $ RogueX.Statup("Love", 200, -10)
            $ RogueX.Statup("Obed", 200, 30)
    if RogueX.SEXP >= 10:
            ch_r "I mean, we've done some stuff. . ."
    if RogueX.SEXP >= 15:
            ch_r "Like {i}sex{/i} stuff. . ."        
    
    if len(Player.Harem) >= 2:
            ch_r "I know you've been going with those other girls for a while now, but we got talking and . . ."
    elif Player.Harem:        
            ch_r "I know you've been going with [Player.Harem[0]] for a while now, but we got talking and . . ."
                    
    if not RogueX.Event[5]:
            ch_r "Right, so I was thinking. . ."
            ch_r "I haven't really been able to have a stable relationship, since I couldn't touch anyone."
            ch_r "This is all very new to me, but I'm feeling my way through it as best I can."
            ch_r "Let's make it official, you want to be my boyfriend?"
    elif Player.Harem: 
            ch_r "I'd still like to be your girlfriend too."
    else:        
            ch_r "You can be a real jerk sometimes, but still. . . I'm serious about this."
            ch_r "I think I want to be your girlfriend. . . officially"
    $ RogueX.Event[5] += 1
    menu: 
        extend ""
        "I'd love to!":
                $ RogueX.Statup("Love", 200, 30)
                "Rogue leaps in and kisses you deeply."
                $ RogueX.FaceChange("kiss") 
                $ RogueX.Kissed += 1
        "Um, ok.":
                $ RogueX.Brows = "confused"
                "[RogueX.Name] is a bit put off by your casual acceptence of reality, but takes it as a positive sign and hugs you."               
            
        "I'm with someone now." if Player.Harem:             
                $ RogueX.FaceChange("sad",1)    
                ch_r "I know, I know, I just thought maybe you could go out with me too?"
                menu:
                    extend ""
                    "Sure":
                            $ RogueX.Statup("Love", 200, 30)
                            "Rogue leaps in and kisses you deeply."
                            $ RogueX.FaceChange("kiss") 
                            $ RogueX.Kissed += 1                
                    "She wouldn't understand." if len(Player.Harem) == 1:
                            $ Line = "no."
                    "They wouldn't be cool with that." if len(Player.Harem) > 1:
                            $ Line = "no."
                    "I'm sorry, but. . . no." if RogueX.Event[5] != 20:
                            $ Line = "no."
                    "No way.":
                            jump Rogue_BF_Jerk
                if Line == "no": 
                            $ RogueX.Statup("Love", 200, -10)
                            ch_r "I get it. That's fine." 
                            $ RogueX.Event[5] = 20 
                            call Remove_Girl(RogueX) 
                            $ Line = 0
                            return           
        "Not really.":
                jump Rogue_BF_Jerk
    $ RogueX.Petnames.append("boyfriend")
    $ RogueX.Traits.append("dating")
    if "Historia" not in Player.Traits:
            $ Player.Harem.append(RogueX)
            if "RogueYes" in Player.Traits:       
                    $ Player.Traits.remove("RogueYes")
    $ RogueX.FaceChange("sexy")    
    ch_r "Now, . . . boyfriend. . . how would you like to celebrate?"
    if "Historia" in Player.Traits:
        return 1
    $ Tempmod = 10
    call Rogue_SexMenu
    $ Tempmod = 0
    return
    
label Rogue_BF_Jerk:
    $ RogueX.FaceChange("angry", 1)
    ch_r "Well fine!" 
    $ Count = (20* RogueX.Event[5])
    $ RogueX.Statup("Obed", 50, 40)
    if RogueX.Event[5] != 20:
            $ RogueX.Statup("Obed", 200, (20* RogueX.Event[5]))
    if 20 > RogueX.Event[5] >= 3:
            $ RogueX.FaceChange("sad")
            ch_r "Hrmph. I don't care what you want, we're dating. Deal with it."   
            ch_r "Now I need some alone time though."          
            if "Historia" in Player.Traits:
                return 1
            $ RogueX.Petnames.append("boyfriend")
            $ RogueX.Traits.append("dating")
            $ Achievements.append("I am not your Boyfriend!")
            $ bg_current = "bg player"          
            call Remove_Girl(RogueX)
            call Set_The_Scene
            return     
    if 1 <  RogueX.Event[5] < 20:
            ch_r "I don't know why I keep asking, I should know you haven't changed."  
            $ RogueX.Statup("Love", 200, -(50* RogueX.Event[5]))
    else:
            $ RogueX.Statup("Love", 200, -50)
            
    ch_r "Jerk! Out!"   
    if "Historia" in Player.Traits:
        return 1
    $ RogueX.Loc = "bg rogue"
    $ bg_current = "bg player"         
    call Remove_Girl(RogueX) 
    call Set_The_Scene    
    $ renpy.pop_call()
    jump Player_Room     

# end Rogue_BF//////////////////////////////////////////////////////////

# start Rogue_Love//////////////////////////////////////////////////////////
label Rogue_Love:
    call Shift_Focus(RogueX)
    
    if bg_current != "bg rogue":
        if RogueX.Loc == bg_current or RogueX in Party:
            "Suddenly, [RogueX.Name] says she wants to talk to you in her room and drags you over there."
        else:
            "[RogueX.Name] shows up, hurridly says she wants to talk to you in her room and drags you over there."
    else:
        "[RogueX.Name] suddenly stares at you very intently."
    
    $ bg_current = "bg rogue"
    $ RogueX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(RogueX)
    call CleartheRoom(RogueX)
    call Taboo_Level
    $ RogueX.DailyActions.append("relationship")
    $ RogueX.FaceChange("bemused", 1)       
    if "dating" in RogueX.Traits or RogueX in Player.Harem:
            ch_r "We've been dating for a while now, and I'm really feeling close to you."
    else:
            ch_r "We've been hanging out for a while now, and I'm really feeling close to you."
    ch_r ". . ."
    $ RogueX.Eyes = "sexy"
    menu:
        ch_r "Right?"
        "I love you, [RogueX.Name].":
                $ RogueX.Statup("Love", 200, 50)
                $ RogueX.Event[6] = 10
        "Yeah, it's been great.":
                $ RogueX.Statup("Love", 200, 20)
        "Yeah, I guess":
                $ RogueX.Statup("Love", 200, 10)
        "Um, maybe?":
                $ RogueX.Statup("Love", 200, -10)
                $ RogueX.Statup("Obed", 200, 30)
    if not RogueX.Event[6]:
            ch_r "Right, so I was thinking. . ."
            ch_r "I love you."
    elif RogueX.Event[6] == 10:        
            $ RogueX.FaceChange("confused")
            ch_r "So. . . wait, what?"
            $ RogueX.FaceChange("smile",2)
            $RogueX.Brows = "surprised"        
            ch_r "I love you too!"
            $ RogueX.FaceChange("kiss")
            "Rogue leaps into your arms and gives you a kiss." 
            $ RogueX.FaceChange("sexy",1)
            $ RogueX.Kissed += 1
    else:        
            ch_r "Even though we've had our rough patches from time to time. . ."
            ch_r "I still love you."
    $ RogueX.Event[6] += 1
    if RogueX.Event[6] < 10:
        menu:
            extend ""
            "I love you too.":
                    $ RogueX.Statup("Love", 200, 50)
                    "[RogueX.Name] collapses into your arms."
            "That's great!":
                    $ RogueX.Brows = "confused"
                    "[RogueX.Name] seems a bit perplexed, but takes it as a positive sign and hugs you."   
            "I know.":
                    $ RogueX.FaceChange("smile")
                    $ RogueX.Brows = "confused"                
                    "[RogueX.Name] punches you in the arm and then gives you a huge hug."                         
            "So?":
                    jump Rogue_Love_Jerk
            "Well I don't think of you like that.":
                    $ RogueX.Statup("Love", 200, -50)
                    $ RogueX.Statup("Obed", 200, 50)
                    jump Rogue_Love_Jerk
    $ RogueX.FaceChange("bemused",1,Eyes="side")
    $ RogueX.Petnames.append("lover")
    call Rogue_AnnaMarie        #plays new name dialog    
    ch_r "Anyway, I am glad I've been able to share this with you."
    $ RogueX.FaceChange("sly")
    ch_r "I'm hoping to share a lot more with you if I can. . ."
    if not RogueX.Sex:
        $ RogueX.Statup("Obed", 70, 10)
        ch_r "So. . . did you want to . . . consumate this?"
        menu:
            extend ""
            "Yeah. . . [[have sex]":      
                    $ RogueX.Statup("Inbt", 30, 30) 
                    ch_r "Hmm. . ."  
                    if "Historia" in Player.Traits:
                        return 1
                    call Rogue_SexAct("sex")
                    return
            "I have something else in mind. . .[[choose another activity]":
                    $ RogueX.Brows = "confused"
                    $ RogueX.Statup("Obed", 70, 20)
                    ch_r "Well now you've got me curious. . ."
                    pass
            "Ew. [[do nothing]":                
                    $ RogueX.Statup("Love", 200, -10)
                    $ RogueX.Statup("Obed", 70, 40)                
                    $ RogueX.FaceChange("perplexed",1)
                    ch_r "Um, ok?"
                    ch_r "{size=-5}What the fuck was that?{/size}"          #fix test this      
                    return
    else:
            ch_r "Now, lover. . . was there anything else you felt like doing to celebrate?"  
    if "Historia" in Player.Traits:
            return 1
    if "stockings and garterbelt" not in RogueX.Inventory:
            $ RogueX.Inventory.append("stockings and garterbelt")
    $ Tempmod = 20
    call Rogue_SexMenu
    $ Tempmod = 0
    return
    
label Rogue_Love_Jerk:    
    if "Historia" not in Player.Traits:
            $ renpy.pop_call()
    $ RogueX.FaceChange("angry", 1)
    ch_r "Well fine!" 
    $ Count = (20* RogueX.Event[6])
    $ RogueX.Statup("Obed", 50, 40)
    $ RogueX.Statup("Obed", 200, Count)
    if RogueX.Event[6] == 3:
            $ RogueX.FaceChange("sad")
            ch_r "I. . . I don't care, I love you too much anyways."   
            ch_r "I need some time to myself though."
            if "Historia" in Player.Traits:
                    return 1            
            $ RogueX.Petnames.append("lover")
            $ Achievements.append("One Sided Love")
            $ RogueX.Loc = "bg rogue"
            $ bg_current = "bg player"
            call Remove_Girl(RogueX)
            jump Player_Room  
    if RogueX.Event[6] > 1:
            ch_r "Fool me once, shame on you. . . I thought you'd grown." 
    ch_r "If that's how you want to be, you can get the hell out of here!"
    $ Count = (100* RogueX.Event[6])
    $ RogueX.Statup("Love", 200, -Count)    
    if "Historia" in Player.Traits:
            return 0
    $ RogueX.Loc = "bg rogue"
    $ bg_current = "bg player"
    call Remove_Girl(RogueX)
    jump Player_Room  

label Rogue_AnnaMarie:
    ch_r "I should probably tell you, I wasn't exactly born with the name \"Rogue.\""
    ch_r ". . ."
    $ RogueX.FaceChange("bemused",1)
    ch_r "Grow'in up, I went by \"Anna-Marie.\""
    $ RogueX.Names.append("Anna-Marie")
    $ RogueX.Names.append("Anna")
    $ RogueX.Names.append("Marie")
    menu:
        extend ""
        "That's a lovely name.":
                $ RogueX.Statup("Love", 200, 10)
                $ RogueX.Statup("Obed", 50, 5)
                $ RogueX.Statup("Inbt", 70, 5)
                $ RogueX.FaceChange("smile",2)
                ch_r "Oh, thank you so much for say'in. . ."
        "Huh, ok.":
                $ RogueX.Statup("Obed", 80, 5)
                $ RogueX.FaceChange("confused",1)
                ch_r "Um. . . yeah."
        "Don't like it.":
                $ RogueX.Statup("Love", 200, -5)
                $ RogueX.Statup("Obed", 200, 10)
                $ RogueX.Statup("Inbt", 200, -5)
                $ RogueX.FaceChange("angry",1)
                ch_r "Oh. . . Ok. . ."
    menu:
        extend ""
        "I think \"Rogue\" suits you though.":
                $ RogueX.Name = "Rogue"
                $ RogueX.FaceChange("smile")
                ch_r "Yeah, I'm used to it buy this point."    
        "I liked the sound of \"Anna-Marie.\"":
                $ RogueX.Name = "Anna-Marie"
                $ RogueX.FaceChange("smile")
                ch_r "It might be fun to go back like that again. . ."
        "\"Marie\" would be a cute name for you.":
                $ RogueX.Name = "Marie"
                $ RogueX.FaceChange("smile")
                ch_r "You think? I suppose. . ."
        "\"Anna\" sounds nice.":
                $ RogueX.Name = "Anna"
                $ RogueX.FaceChange("smile")
                ch_r "I suppose it does. . ."
    return
# end Rogue_Love//////////////////////////////////////////////////////////


# start Rogue_Sub//////////////////////////////////////////////////////////
label Rogue_Sub:  
    call Shift_Focus(RogueX)
    if RogueX.Loc != bg_current and RogueX not in Party:
            "Suddenly, [RogueX.Name] shows up and says she needs to talk to you."
    
    $ RogueX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(RogueX)
    call CleartheRoom(RogueX)
    call Taboo_Level
    $ RogueX.DailyActions.append("relationship")
    $ RogueX.FaceChange("bemused", 1)
    ch_r ". . ."
    if "dating" in RogueX.Traits or RogueX in Player.Harem:
            ch_r "We've been dating for a bit now."  
    else:    
            ch_r "We've been hanging out for a while now."   
    if RogueX.FondleB or RogueX.FondleP or RogueX.FondleA: 
            ch_r "I've let you touch me. . ."
    if RogueX.Hand or RogueX.Blow:
            ch_r "I've touched you. . ."
    if RogueX.Love >= 900 and ("dating" in RogueX.Traits or RogueX in Player.Harem):
            ch_r "I love you so much. . ."
    elif RogueX.Love >= 800:
            ch_r "I really care about you."
    elif RogueX.Love >= 500:
            ch_r "We don't exactly get along, but. . . we work, right?"
    else:
            $ RogueX.Brows = "angry" 
            ch_r "I really don't like you much, but something about you just. . ."
            ch_r "works for me."
    menu:
        extend ""
        "Yeah, it's been great.":
                $ RogueX.Statup("Love", 200, 20)
        "Yeah, I guess":
                $ RogueX.Statup("Love", 200, 10)
        "Um, maybe?":
                $ RogueX.Statup("Love", 200, -10)
                $ RogueX.Statup("Obed", 200, 30)
    if not RogueX.Event[7]:
            ch_r "Right, so I was thinking. . ."
            $ RogueX.Eyes = "sexy"
            ch_r "I'd like you to provide some . . .structure to my life."
    else:        
            ch_r "I'd like you to reconsider the offer I made. . ."
            ch_r "the one about giving me some . . .structure."
    $ RogueX.Event[7] += 1
    menu:
        extend ""
        "Sounds interesting, yes.":
                $ RogueX.Statup("Obed", 200, 100)
                $ RogueX.Petnames.append("sir")
                "[RogueX.Name] nods obediently."            
        "What do you mean by that?": 
                $ RogueX.FaceChange("bemused") 
                ch_r "When you. . . encourage me to try new things, it really turns me on."
                ch_r "I'd like you to continue to. . . encourage me."
                menu:
                    ch_r "I mean that I would like you to give me orders, and I will follow them as best I can."
                    "Sounds interesting, ok.":
                            $ RogueX.Statup("Obed", 200, 100)
                            "[RogueX.Name] nods obediently."  
                    "Oh, ok, sure.":
                            "[RogueX.Name] seems a bit put out, but takes it as a positive sign and nods."  
                    "Oh, no thanks. Take care of things yourself.":
                            jump Rogue_Sub_Jerk 
                $ RogueX.Petnames.append("sir")         
        "Nah, you can handle things yourself.":
                jump Rogue_Sub_Jerk
    $ RogueX.FaceChange("sexy") 
    ch_r "Now, sir. . . was there anything else you wished me to do to celebrate?"
    if "Historia" in Player.Traits:
            return 1
    if "stockings and garterbelt" not in RogueX.Inventory:
            $ RogueX.Inventory.append("stockings and garterbelt")
    $ Tempmod = 10
    call Rogue_SexMenu
    $ Tempmod = 0
    return
    
label Rogue_Sub_Jerk:
    $ RogueX.FaceChange("sad", 1)
    ch_r "Hrmph!"
    $ Count = (20* RogueX.Event[7])
    $ RogueX.Statup("Inbt", 50, 30)
    $ RogueX.Statup("Inbt", 200, Count)    
    if "Historia" not in Player.Traits:
            $ renpy.pop_call()
    if RogueX.Event[7] == 2:
            $ RogueX.FaceChange("sad")
            ch_r "I need some time to myself though."      
            if "Historia" in Player.Traits:
                    return  
            $ RogueX.Petnames.append("sir")
            $ Achievements.append("Nosiree")
            $ bg_current = "bg player"        
            $ RogueX.Loc = "bg rogue"
            call Remove_Girl(RogueX)
            jump Player_Room  
    if RogueX.Event[7] > 1:
            ch_r "I thought you may have learned to respect my needs by now." 
    ch_r "If that's how it is, I would appreciate some time alone."           
    $ Count = (20* RogueX.Event[7])
    $ RogueX.Statup("Obed", 200, -Count)    
    if "Historia" in Player.Traits:
            return 
    $ RogueX.Loc = "bg rogue"
    $ bg_current = "bg player"
    call Remove_Girl(RogueX)
    jump Player_Room  

# end Rogue_Sub//////////////////////////////////////////////////////////


# start Rogue_Master//////////////////////////////////////////////////////////
label Rogue_Master:    
    call Shift_Focus(RogueX)
    if RogueX.Loc != bg_current and RogueX not in Party:
            "Suddenly, [RogueX.Name] shows up and says she needs to talk to you."
    
    $ RogueX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(RogueX)
    call CleartheRoom(RogueX)
    call Taboo_Level
    $ RogueX.DailyActions.append("relationship")
    $ RogueX.FaceChange("bemused", 1)
    ch_r ". . ."
    
    if "dating" in RogueX.Traits or RogueX in Player.Harem:
            ch_r "This situation we have has really added some . . . spice to our relationship." 
    else:     
            ch_r "This situation we have has been very. . . interesting."
    if RogueX.Anal or RogueX.DildoA:
            ch_r "We've even done some butt stuff."  
    if RogueX.Love >= 900 and ("dating" in RogueX.Traits or RogueX in Player.Harem):
            ch_r "I'm devoted to you. . ."
    elif RogueX.Love >= 800:
            ch_r "I really care about you."
    elif RogueX.Love >= 500:
            ch_r "I can't be without you."
    else:
            $ RogueX.Brows = "angry" 
            ch_r "I can't stand being with you, but can't stand being without you either."
    menu:
        ch_r "Have I been pleasing you, [RogueX.Petname]?"
        "Certainly.":
                $ RogueX.Statup("Love", 200, 20)
                $ RogueX.Statup("Obed", 200, 20)
        "Yeah, I guess.":
                $ RogueX.Statup("Love", 200, 10)
                $ RogueX.Statup("Obed", 200, 20)
        "Not especially.":
                $ RogueX.Statup("Love", 200, -10)            
                $ RogueX.Statup("Obed", 200, 30)        
    if not RogueX.Event[8]:
                ch_r "Yes, well, given that. . ."
                ch_r "I think that I would like you to be my master, formally."
    else:        
                ch_r "I'd like you to reconsider the offer I made. . ."
                ch_r "please be my master."
    $ RogueX.Event[8] += 1
    menu:
        extend ""
        "Very well.":
                $ RogueX.Statup("Obed", 200, 100)
                $ RogueX.Petnames.append("master")
                "[RogueX.Name] bows obediently."
        "What do you mean by that?":            
                $RogueX.Brows = "confused"
                ch_r "Well, when you tell me what to do. . ."            
                $ RogueX.FaceChange("bemused", 1)     
                ch_r "I get really horny." 
                ch_r "I just really need for you to tell me what to do."
                menu:
                    ch_r "I mean that I would follow your orders to the letter, so long as I am able."
                    "Oh, ok, sure.":
                            "[RogueX.Name] seems a bit put out, but takes it as a positive sign and nods."  
                            $ RogueX.Petnames.append("master")
                    "You should do your own thing, you don't need me telling you what to do.":                                            
                            $RogueX.Brows = "confused" 
                            ch_r "Ok, if that's what you want. . ."
                            $ RogueX.Statup("Inbt", 50, 100)  
                            $ RogueX.Statup("Inbt", 90, 50)  
                            ch_r "For now at least. . ."
                            $ RogueX.Statup("Obed", 200, -200)
                            $ RogueX.Event[8] = 3
                    "Oh, no, sounds like too much work.":
                            jump Rogue_Obed_Jerk                
        "Nah, take care of yourself.":
                jump Rogue_Obed_Jerk
    $ RogueX.FaceChange("sexy")       
    ch_r "Now, master. . . was there anything else you wished me to do to celebrate?"
    if "Historia" in Player.Traits:
            return 1
    $ Tempmod = 20
    call Rogue_SexMenu
    $ Tempmod = 0
    return
    
label Rogue_Obed_Jerk:
    $ RogueX.FaceChange("sad", 1)
    ch_r "Well fine!"
    $ Count = (20* RogueX.Event[8])
    $ RogueX.Statup("Inbt", 50, 30)
    $ RogueX.Statup("Inbt", 200, Count) 
    if "Historia" not in Player.Traits:
            $ renpy.pop_call()   
    if RogueX.Event[8] == 2:
            $ RogueX.FaceChange("sad")
            ch_r "I don't care what you say, this is something I need. MASTER."  
            ch_r "I need some time to myself though."   
            if "Historia" in Player.Traits:
                    return  
            $ RogueX.Petnames.append("master")
            $ Achievements.append("Heavy is the Head")
            $ bg_current = "bg player"        
            $ RogueX.Loc = "bg rogue"       
            call Remove_Girl(RogueX)
            jump Player_Room  
    if RogueX.Event[8] > 1:
            ch_r "I thought you may have learned to respect my needs by now." 
    ch_r "If that's how it is, I would appreciate some time alone."          
    $ Count = (50* RogueX.Event[8])
    $ RogueX.Statup("Obed", 200, -Count)
    if "Historia" in Player.Traits:
        return 
    $ RogueX.Loc = "bg rogue"
    $ bg_current = "bg player"       
    call Remove_Girl(RogueX)
    jump Player_Room  

# end Rogue_Slave//////////////////////////////////////////////////////////


# start Rogue_Sexfriend//////////////////////////////////////////////////////////
label Rogue_Sexfriend:  
    call Shift_Focus(RogueX)
    $ RogueX.DailyActions.append("relationship")
    if ("dating" in RogueX.Traits or RogueX in Player.Harem):       
            if RogueX.Loc != bg_current and RogueX not in Party:
                    return
            $ RogueX.Petnames.append("sex friend") 
            $ RogueX.Statup("Inbt", 200, 50) 
            "[RogueX.Name] suddenly gives your butt a little squeeze."
            return
        
    if RogueX.Loc != bg_current and RogueX not in Party:
        "Suddenly, [RogueX.Name] shows up and says she needs to talk to you."
    
    $ RogueX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(RogueX)
    call CleartheRoom(RogueX)
    call Taboo_Level
    $ RogueX.FaceChange("smile", 1)
    ch_r ". . ."
    ch_r "We've been having fun, right?"   
    if RogueX.SEXP >= 40:
            ch_r "I mean, we've been getting up to some pretty wild stuff."
    if "ex" in RogueX.Traits:
            ch_r "And we were actually dating for a while. . ."
    else:
            ch_r "And I know we're not \"dating\" dating, but you know. . ."
    menu:
        ch_r "Haven't I been fun to have around?"
        "Yeah, you've been great.":
                $ RogueX.Statup("Love", 200, 20)
                $ RogueX.Statup("Inbt", 200, 20)
        "Hmmm. . . yes?":
                $ RogueX.Statup("Inbt", 200, 20)
        "Maybe. . .":
                $ RogueX.Statup("Love", 200, -10)
                $ RogueX.Statup("Obed", 200, 30)    
    if RogueX in Player.Harem:
        ch_r "I'd like to have a -lot- more sex. . ."
    if not RogueX.Event[9]:
        ch_r "Ok, so since we've been having so much fun. . ."
        if "ex" in RogueX.Traits:
                ch_r "I think that even though we aren't dating, I still want to be sex friends."
        else:
                ch_r "I think I'm ready to accept just being casual sex friends."
    else:        
        ch_r "I'd like you to reconsider my generous offer. . ."
        ch_r "come on, sex friend? Eh?"
    $ RogueX.Petnames.append("sex friend") 
    $ RogueX.Event[9] += 1    
    if RogueX not in Player.Harem:
            menu:
                extend ""
                "Sounds fun!":
                        $ RogueX.Statup("Inbt", 200, 100) 
                        $ RogueX.Petnames.append("sex friend")
                        "[RogueX.Name] nods obediently."            
                "What do you mean by that?":            
                        $RogueX.Brows = "confused"              
                        ch_r "You know, casual sex, no real strings, for now at least."
                        menu:
                            ch_r "Well?"
                            "Oh, ok, sure.":
                                    "[RogueX.Name] is a bit put off, but grabs you in a big hug anyway."  
                            "Oh, no thanks. Not interested.":
                                    jump Rogue_Sexfriend_Jerk                
                "Nah, you're on your own.":
                        jump Rogue_Sexfriend_Jerk
            $ RogueX.FaceChange("sexy")  
            ch_r "Now, sex friend. . . how would you like to celebrate?"
            if "Historia" in Player.Traits:
                    return 1
    if "stockings and garterbelt" not in RogueX.Inventory:
            $ RogueX.Inventory.append("stockings and garterbelt")
    $ Tempmod = 25
    call Rogue_SexMenu
    $ Tempmod = 0
    return
    
label Rogue_Sexfriend_Jerk:    
    $ RogueX.FaceChange("sad", 1)
    $ RogueX.DailyActions.append("relationship")
    ch_r "Your loss." 
    $ RogueX.Statup("Obed", 50, 30) 
    if "Historia" not in Player.Traits:
            $ renpy.pop_call()   
    if RogueX.Event[9] == 3:
            ch_r "Well, it's not really up to you anyways."
            ch_r "Just let me know if you want a roll in the hay."
            ch_r "I need some alone time though."   
            if "Historia" in Player.Traits:
                    return     
            $ RogueX.Petnames.append("sex friend")
            $ Achievements.append("Man of Virtue")
            $ bg_current = "bg player"        
            $ RogueX.Loc = "bg rogue"
            call Remove_Girl(RogueX)
            jump Player_Room  
    $ Count = (10 * RogueX.Event[9])
    $ RogueX.Statup("Inbt", 200, -Count)
    if bg_current == "bg rogue":
            ch_r "Ok, you can go now."
            $ bg_current = "bg player"
    else:
            ch_r "Ok, I'm out."   
            $ RogueX.Loc = "bg rogue"
    if "Historia" in Player.Traits:
            return 
    call Remove_Girl(RogueX)
    jump Player_Room  

# end Rogue_Sexfriend//////////////////////////////////////////////////////////


# start Rogue_Fuckbuddy//////////////////////////////////////////////////////////
label Rogue_Fuckbuddy:    
    call Shift_Focus(RogueX)
    if "dating" in RogueX.Traits or RogueX in Player.Harem:
            if RogueX.Loc != bg_current and RogueX not in Party:
                    return
            $ RogueX.Petnames.append("fuck buddy") 
            $ RogueX.Statup("Inbt", 200, 50) 
            "[RogueX.Name] suddenly reaches down and gives your package a little squeeze."
            return
        
    if RogueX.Loc != bg_current and RogueX not in Party:
            "Suddenly, [RogueX.Name] shows up and says she needs to talk to you."
    
    $ RogueX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(RogueX)
    call CleartheRoom(RogueX)
    call Taboo_Level
    $ RogueX.FaceChange("bemused", 1)
    ch_r ". . ."
    ch_r "I've been having a lot of fun with this \"sex friend\" thing."       
    if "exhibitionist" in RogueX.Traits:
            ch_r "And I've really been getting off on all the stuff we've been doing."
    menu:
        extend ""       
        "You bet!":
                $ RogueX.Statup("Love", 200, 20)          
                $ RogueX.Statup("Obed", 200, 20)            
                $ RogueX.Statup("Inbt", 200, 30)  
        "Yeah?":
                $ RogueX.Statup("Love", 200, 10)
                $ RogueX.Statup("Obed", 200, 20)
        "Whatever.":
                $ RogueX.Statup("Love", 200, -10)
                $ RogueX.Statup("Obed", 200, 30)    
    ch_r "So, since it's worked so far. . ."
    $ RogueX.Event[10] += 1
    $ RogueX.Petnames.append("fuck buddy")  
    if RogueX not in Player.Harem:
            ch_r "I'd like to be full on casual fuck buddies."
            menu:
                extend ""
                "Heh, ok, fuck buddy.":
                        $ RogueX.Statup("Inbt", 200, 100) 
                        $ RogueX.Petnames.append("fuck buddy")
                        $ RogueX.ArmPose = 2
                        ch_r "Whoo hoo!"
                        $ RogueX.Over = 0
                        $ RogueX.Chest = 0  
                        if "Historia" in Player.Traits:
                                    return 1
                        call Rogue_First_Topless(1)
                        call Rogue_Breasts_Launch
                        "Rogue, throws her top off, grabs you and shoves your head into her cleavage."
                        call Rogue_Pos_Reset
                "What do you mean by that?":            
                    $RogueX.Brows = "confused"
                    menu:
                        ch_r "I mean, you know, we'd fuck. And be buddies. Both of those."
                        "Oh, ok, sure.":
                                call Rogue_Kissing_Launch
                                "Rogue laughs and tackles you into a hug." 
                                call Rogue_Pos_Reset
                        "Oh, no, not my style.":
                                jump Rogue_Fuckbuddy_Jerk                
                "No thanks.":
                    jump Rogue_Fuckbuddy_Jerk
            $ RogueX.FaceChange("sexy")      
            ch_r "Now, -heh-, fuck buddy. . . let's make this official!"
    if "Historia" in Player.Traits:
            return 1
    $ Tempmod = 30
    call Rogue_SexMenu
    $ Tempmod = 0
    return
    
label Rogue_Fuckbuddy_Jerk:
    $ RogueX.Statup("Obed", 50, 30)   
    $ RogueX.FaceChange("bemused", 1)
    if RogueX.Event[10] > 1:
            $ RogueX.ArmPose = 2
            $ RogueX.Over = 0
            $ RogueX.Chest = 0
            ch_r "I offer these things on a silver platter, and nothing!" 
            $ RogueX.OutfitChange()
            ch_r "Look, I don't care what you call it. Just let me know if you want a tumble."   
            if "Historia" in Player.Traits:
                    return 1
            call Rogue_First_Topless(1)
            $ RogueX.Petnames.append("fuck buddy")
            $ Achievements.append("Stalwart as the mount")
            return      
    else:
            ch_r "Too bad."
    if "Historia" in Player.Traits:
            return
    $ renpy.pop_call()
    $ Count = (10*RogueX.Event[10])
    $ RogueX.Statup("Inbt", 200, -Count)
    if bg_current == "bg rogue":
            ch_r "Ok, you can go now."
            $ bg_current = "bg player"
    else:
            ch_r "Ok, I'm out."   
            $ RogueX.Loc = "bg rogue"    
    call Remove_Girl(RogueX)
    jump Player_Room  
# end Rogue_Fuckbuddy//////////////////////////////////////////////////////////

# start Rogue_Daddy//////////////////////////////////////////////////////////
label Rogue_Daddy:      
    $ RogueX.DailyActions.append("relationship")
    call Shift_Focus(RogueX)
    call Set_The_Scene
    ch_r ". . ."
    if "dating" in RogueX.Traits or RogueX in Player.Harem:
            ch_r "You know, even though we've been dating,"  
    else:    
            ch_r "Even though we've been hanging out," 
    if RogueX.Love > RogueX.Obed and RogueX.Love > RogueX.Inbt:
            ch_r "and you're really sweet to me. . ."
    elif RogueX.Obed > RogueX.Inbt:
            ch_r "and you know what I need. . ."
    else:
            ch_r "and I've really been spreading my wings. . ."        
    ch_r "So I was thinking, could I call you \"daddy?\""  
    menu:
        extend ""
        "Ok, go right ahead?":            
                $ RogueX.FaceChange("smile") 
                $ RogueX.Statup("Love", 90, 20)          
                $ RogueX.Statup("Obed", 60, 10)            
                $ RogueX.Statup("Inbt", 80, 30) 
                ch_r "Squee!"   
                $ RogueX.Petname = "daddy"
        "What do you mean by that?": 
                $ RogueX.FaceChange("bemused") 
                ch_r "I just sort of get turned on by it, you know, being your baby girl. . ."
                ch_r "I'd like to call you that."
                menu:
                    extend ""
                    "Sounds interesting, fine by me.":     
                            $ RogueX.FaceChange("smile") 
                            $ RogueX.Statup("Love", 90, 15)          
                            $ RogueX.Statup("Obed", 60, 20)            
                            $ RogueX.Statup("Inbt", 80, 25) 
                            ch_r "Great! . . daddy."  
                            $ RogueX.Petname = "daddy"
                    "Could you not, please?":             
                            $ RogueX.Statup("Love", 90, 5)
                            $ RogueX.Statup("Obed", 80, 40)            
                            $ RogueX.Statup("Inbt", 80, 20)  
                            $ RogueX.FaceChange("sad") 
                            ch_r "   . . .   "
                            ch_r "Well, ok."
                    "No, that creeps me out.":    
                            $ RogueX.Statup("Love", 90, -10)          
                            $ RogueX.Statup("Obed", 80, 45)            
                            $ RogueX.Statup("Inbt", 70, 5)  
                            $ RogueX.FaceChange("angry") 
                            ch_r "Hrmph." 
        "No, that creeps me out.":
                $ RogueX.Statup("Love", 90, -5)          
                $ RogueX.Statup("Obed", 80, 40)            
                $ RogueX.Statup("Inbt", 70, 10) 
                $ RogueX.FaceChange("angry") 
                ch_r "Hrmph."  
    $ RogueX.Petnames.append("daddy")
    return

# end Rogue_Daddy//////////////////////////////////////////////////////////


label Rogue_Frisky_Class:
        $ Line = 0        
        if EmmaX.Loc == "bg teacher":   
            "[EmmaX.Name] is giving a lecture on mutant relations. In her seat next to you, you notice [RogueX.Name] shifting uncomfortably in her seat."
        else:
            "Professor McCoy is giving a lecture on the X-Gene. In her seat next to you, you notice [RogueX.Name] shifting uncomfortably in her seat."
        "Occasionally, you catch her glancing over your way."
        if not ApprovalCheck(RogueX, 600):
                jump Rogue_Frisky_Class_End
            
        "[RogueX.Name] opens her notebook and begins scratching out a note. She detaches the slip of paper from the binder, carefully folding it before sliding it in front of you."
        "She watches you as you unfold the note. In looping penstrokes, it reads: {i}You like biology?{/i}"
        "You look back and see that she's blushing slightly. She slides her pen over to you so you can reply."
        menu:
            "You reply. . ."
            "What are you talking about?":
                    pass
                
            "Naah. Not so much.":
                    $ RogueX.Statup("Love", 80, -3)
                    $ RogueX.Statup("Inbt", 60, -3)   
                    $ RogueX.FaceChange("confused")    

            "It's my favorite subject.":
                    $ RogueX.Statup("Love", 80, 5)   
                    $ RogueX.FaceChange("smile")    
                    "[RogueX.Name] reads your note and starts to smile. She quickly dashes off another note, sliding it in front of you again."
                    "You unfold the note, trying not to let the teacher see you. {i}\"Then maybe we could study together tonight?\"{/i}." 
                    $ Line = "continue"
            
            "I do when it's about you.":
                if ApprovalCheck(RogueX, 500, "I") or RogueX.SEXP >= 30:  
                        $ RogueX.FaceChange("sly")    
                        "[RogueX.Name] reads your note and smiles at you suggestively."
                        $ Line = "flirt"
                elif ApprovalCheck(RogueX, 900):  
                        $ RogueX.FaceChange("confused",2)    
                        "[RogueX.Name] reads your note and blushes furiously, looking down at her notes."
                        $ RogueX.Blush = 1
                        $ Line = "flirt"                
                else: 
                        $ RogueX.FaceChange("perplexed",2)  
                        "[RogueX.Name] reads your note and blushes furiously. She quickly dashes off another note, sliding it in front of you again."
                        "You unfold the note, trying not to let the teacher see you. {i}\"I meant the class! Maybe we could study tonight?\"{/i}." 
                        $ RogueX.Blush = 1
                        $ Line = "continue"
            
            
        if Line == "continue":
                "[RogueX.Name]'s drawn a little heart as the period at the bottom of the question mark." 
                "She's trying to act like she's paying attention to the lecture, but she can't hide the big smile on her face."
                menu:
                    "You respond. . ."
                    "Maybe later.":                     
                            $ RogueX.Statup("Love", 80, -3)
                            $ RogueX.Statup("Obed", 70, 5)
                            $ RogueX.Statup("Inbt", 60, -3)  
                            $ RogueX.FaceChange("confused")
                            $ Line = 0
                    "Naah. I've got better things to do.":
                            $ RogueX.Statup("Love", 200, -15)
                            $ RogueX.Statup("Obed", 70, 5)
                            $ RogueX.Statup("Inbt", 60, -3) 
                            $ Line = 0    
                            $ RogueX.FaceChange("angry")
                            $ RogueX.DailyActions.append("angry")                          
                    "Count on it.":
                            "She smiles when she reads your reply, and throws you a wink."
                            $ RogueX.DailyActions.append("studydate")  
                            $ RogueX.FaceChange("smile")
                            jump Rogue_Frisky_Class_End
                    "We could get some \"studying\" done right now.":
                            if ApprovalCheck(RogueX, 1200):
                                    $ RogueX.FaceChange("sly",1)
                                    $ RogueX.Statup("Love", 80, 3)
                                    $ RogueX.Statup("Inbt", 60, 3) 
                                    "[RogueX.Name] gets a mischevious grin on her face and leans towards you."
                                    $ Line = "flirt"
                            elif ApprovalCheck(RogueX, 700):
                                    $ RogueX.FaceChange("smile",1)
                                    $ RogueX.Statup("Inbt", 60, 2) 
                                    "[RogueX.Name] blushes and smiles your way."
                                    $ Line = "flirt"
                            else:
                                    $ RogueX.FaceChange("confused",1)
                                    "[RogueX.Name] looks a bit surprised, then scowls at you."
                                    jump Rogue_Frisky_Class_End
                            
        #End if Line == "continue"
        
        if Line == "flirt":
                $ D20 = renpy.random.randint(1, 20)
                $ RogueX.FaceChange("sly")                
                "You notice one of [RogueX.Name]'s shoes slip from her foot beneath the desk. She tosses you a sly grin." 
                if RogueX.Hose:
                        "You feel the smooth texture of her stockinged foot begin to slowly slide back and forth along the length of your calf."
                else:
                        "You feel the smooth skin of her bare foot begin to slowly slide back and forth along the length of your calf."
                    
                while D20 <= 21:
                    menu:
                        extend ""                        
                        "Pull away from her.":
                                if Line == "fondle pussy":
                                        "You slowly slide your hand from her lap and start taking notes again."
                                        $ Line = "tease"                                
                                elif Line == "fondle breast":
                                        "With a final squeeze, you move your hand back to the desktop."
                                        $ Line = "tease"
                                else:
                                        $ Line = "rejected"
                                        $ RogueX.Statup("Love", 200, -15)
                                        $ RogueX.Statup("Obed", 70, 2)
                                        $ RogueX.Statup("Inbt", 60, -2) 
                                jump Rogue_Frisky_Class_End
                                    
                        "Look into her eyes and smile slightly." if Line == "flirt": 
                                $ RogueX.FaceChange("smile")                
                                $ RogueX.Statup("Love", 200, 5)
                                "[RogueX.Name] smiles back." 
                                "She looks back towards the front of the class, but her hand drifts across the top of the desk until she's holding yours."
                                $ Line = "handholding"                            
                        "Grasp her hand gently, stroking the top of it." if Line == "handholding":                         
                                $ RogueX.Statup("Love", 200, 5)
                                $ RogueX.FaceChange("smile")                
                                "[RogueX.Name] sighs contentedly and holds your hand for the remainder of class." 
                                jump Rogue_Frisky_Class_End
                                                
                        "Try and slip your hand to her lap." if Line != "fondle pussy":
                                $ Line = "fondle pussy"
                                if ApprovalCheck(RogueX, 1500) and RogueX.FondleP and RogueX.SEXP >= 40:
                                        $ RogueX.FaceChange("sly")           
                                        $ RogueX.Statup("Love", 90, 5)
                                        $ RogueX.Statup("Obed", 70, 5)
                                        $ RogueX.Statup("Inbt", 60, 5)      
                                        "[RogueX.Name] gets a mischievous grin and places her hand on your arm."
                                elif ApprovalCheck(RogueX, 1800) and RogueX.FondleP:
                                        $ RogueX.FaceChange("smile")                
                                        $ RogueX.Statup("Love", 80, 3)
                                        $ RogueX.Statup("Obed", 70, 7)
                                        $ RogueX.Statup("Inbt", 60, 3)  
                                        "[RogueX.Name] starts slightly as your hand travels up her thigh, but then she lets out a slight grin."
                                elif ApprovalCheck(RogueX, 2000):
                                        $ RogueX.FaceChange("perplexed",2)     
                                        $ RogueX.Statup("Obed", 70, 10)
                                        $ RogueX.Statup("Inbt", 60, 3)             
                                        "[RogueX.Name] glances at you in alarm, but then slowly calms down." 
                                        $ RogueX.FaceChange("smile",1)                                           
                                        $ D20 += 2
                                else:
                                        $ Line = "too far"
                                        
                                if Line == "fondle pussy":
                                        $ RogueX.FaceChange("sly")    
                                        if RogueX.Legs == "skirt":
                                            "[RogueX.Name]'s sly smile turns sultry as she feels your fingers sneak under the hem of her skirt, slowly tracing the soft contours of her mound." 
                                        elif RogueX.Legs == "pants":
                                            "[RogueX.Name]'s sly smile turns sultry as she feels your fingers sneak down her pants, slowly tracing the soft contours of her mound." 
                                        else: #No pants
                                            "[RogueX.Name]'s sly smile turns sultry as she feels your fingers sneak between her legs, slowly tracing the soft contours of her mound." 
                                            
                                        if RogueX.Panties == "shorts":
                                            "You think her shorts are becoming damp as you stroke the thin material. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                                        elif RogueX.Panties:
                                            "You think her panties are becoming damp as you stroke the thin material. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                                        elif RogueX.Pubes:
                                            "You feel her soft fur moisten as you stroke the soft flesh below. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                                        else:
                                            "You feel her lips moisten as you stroke the soft flesh. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                                        $ D20 += 5

                        "Keep fondling her pussy." if Line == "fondle pussy":
                                $ RogueX.Statup("Obed", 70, 5)
                                $ RogueX.Statup("Inbt", 60, 3)  
                                "As the class drones on, you continue to slowly massage her warm delta."
                                $ D20 += 5
                                
                        "Start fondling her tits." if Line != "fondle breasts":
                                $ Line = "fondle breasts"
                                if ApprovalCheck(RogueX, 1500) and RogueX.FondleB and RogueX.SEXP >= 40:
                                        $ RogueX.Statup("Love", 80, 5)
                                        $ RogueX.Statup("Obed", 70, 5)
                                        $ RogueX.Statup("Inbt", 60, 3)  
                                        $ RogueX.FaceChange("sly")                
                                        "[RogueX.Name] closes her eyes and caresses your arm."
                                elif ApprovalCheck(RogueX, 1800) and RogueX.FondleB:
                                        $ RogueX.Statup("Love", 80, 3)
                                        $ RogueX.Statup("Obed", 70, 7)
                                        $ RogueX.Statup("Inbt", 60, 3)  
                                        $ RogueX.FaceChange("smile",1)                
                                        "[RogueX.Name] flinches as your hand travels up her ribcage, but she grins as you reach her breast."
                                elif ApprovalCheck(RogueX, 2000):
                                        $ RogueX.Statup("Obed", 70, 10)
                                        $ RogueX.Statup("Inbt", 60, 3)  
                                        $ RogueX.FaceChange("perplexed",2) 
                                        "[RogueX.Name] glances at you in alarm, but then slowly calms down." 
                                        $ RogueX.FaceChange("smile",2) 
                                        $ D20 += 5
                                else:
                                        $ Line = "too far"
                                        
                                if Line == "fondle breasts":  
                                        $ RogueX.FaceChange("sly")                
                                        "[RogueX.Name]'s sly eyes spakle as your hand cups her breast, giving it a casual caress." 
                                        "her nipples begin to firm up and she lets out a small moan of pleasure."
                                        $ D20 += 7
                        "Keep fondling her tits." if Line == "fondle breasts":
                                $ RogueX.Statup("Obed", 70, 5)
                                $ RogueX.Statup("Inbt", 60, 2)  
                                "Barely paying attention to the lecture, you continue to pulse her breast in your palm."
                                $ D20 += 7
                                        
                    if Line == "too far":
                            $ RogueX.FaceChange("surprised",2)   
                            $ RogueX.Statup("Love", 80, -5)
                            $ RogueX.Statup("Obed", 70, 7)
                            $ RogueX.Statup("Inbt", 50, -3)               
                            "[RogueX.Name] sits up straight in her seat and makes a little yelping noise." 
                            $ RogueX.FaceChange("angry",1)                
                            "Between that and the icy glare she shoots you, it's enough to draw the attention of your fellow students in your direction."
                            $ D20 += 10
                    
                #After D20:
                if Line not in ("rejected", "handholding", "tease"):                
                    $ RogueX.Statup("Love", 80, -10)
                    $ RogueX.Statup("Obed", 70, -5)
                    $ RogueX.Statup("Inbt", 50, -10)  
                    $ RogueX.FaceChange("surprised")      
                    if EmmaX.Loc == "bg teacher":                   
                            "[EmmaX.Name] stops her lecture in mid-sentence when she notices that the whole class is looking at you and [RogueX.Name]." 
                            ch_e "[EmmaX.Petname], [RogueX.Name], if you could perhaps pay more attention to the lecture, and less to each other's bodies?"                
                            ch_e "Perhaps it would be best if you visited the headmaster's office and cool off?"
                    else:
                            "Dr. McCoy stops his lecture in mid-sentence when he notices that the whole class is looking at you and [RogueX.Name]." 
                            ch_b "Oh, my stars and garters!"                
                            ch_b "[Player.Name]!?! {b}WHAT ARE YOU DOING? BOTH OF YOU, TO THE PROFESSOR'S OFFICE, IMMEDIATELY!{/b}"
                    if RogueX not in Rules:
                            call Girls_Caught(RogueX)                            
                    else:
                            "Since Xavier isn't concerned with your activities, you both head back to your room instead."
                            $ RogueX.Loc = "bg player"
                            call CleartheRoom(RogueX,0,1)
                            jump Player_Room
        # end if Line == "flirt"
                    
    
label Rogue_Frisky_Class_End:  
        if not Line:        
                $ RogueX.FaceChange("confused")
                "She unfolds the note and quickly reads it over." 
                $ RogueX.FaceChange("sad")
                "As she does, you immediately see disappointment come over her features." 
                "She scratches out a reply and slides it back in front of you." 
                "When you open it up, it reads: {i}Never mind.{/i}"   
        elif Line == "tease":        
                $ RogueX.FaceChange("sly",1)
                "[RogueX.Name] takes in a deep breath and exhales it in a sigh, leaning in to whisper." 
                ch_r "Tonight's \"study session\" just got a whole lot more interesting." # attempt smaller text?
        elif Line == "rejected":
                $ RogueX.FaceChange("sadside")
                "[RogueX.Name] looks surprised and hurt. For the rest of the class, she says nothing." 
                "It seems like she has a hard time looking you in the eye."
        
        "Eventually, [RogueX.Name] seems to settle down and pay attention to the course material. You manage to do the same without falling asleep."
        return
    
    
