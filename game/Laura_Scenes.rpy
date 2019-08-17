
# start LauraMeet//////////////////////////////////////////////////////////

default L_ScentTimer = 0

label LauraMeet(Topics=[],Loop=1):
    $ LauraName = "???"
    
    $ bg_current = "bg dangerroom"   
    call CleartheRoom("All",0,1)
    $ L_Loc = "bg dangerroom"  
    $ L_Love = 400        
    $ L_Obed = 0            
    $ L_Inbt = 200  
    call Shift_Focus("Laura")    
    $ L_SpriteLoc = StageCenter
    call Set_The_Scene(0)
    $ L_Petname = Playername   
    
    "As you approach the Danger Room, you hear a ferocious clanging of metal."
    "Just as you pass through the door, a robotic arm smashes into your face."
    ". . ."   
    call LauraFace("normal", 0) 
    show Laura_Sprite at SpriteLoc(L_SpriteLoc)
    "When you come to, a girl pulls you up by your arm."     
    call LauraFace("surprised", 0, Eyes="squint",Brows="sad") 
    ch_u "Oh, good, you don't look too damaged." 
    call LauraFace("smile", 0, Brows="sad") 
    ch_u "Sorry about that, I was getting a work-out in, and must have forgotten to lock the door." 
    call LauraFace("smile", 0) 
    while Loop:
        menu:
            extend ""
            "Who are you?" if LauraName == "???":
                    call LauraFace("normal", 0) 
                    ch_l "I go by \"X-23\" in the field."
                    $ LauraName = "X-23"        
            "X-23? Is that your real name?" if LauraName == "X-23" and "X23" not in Topics:
                    call LauraFace("confused", 0) 
                    ch_l "It's the one I was born with."
                    $ Topics.append("X23")
            "Is there anything else I could call you?" if "X23" in Topics and "Laura" not in Topics:
                    call Statup("Laura", "Love", 70, 5) # Love
                    call LauraFace("normal", 0) 
                    ch_l "I also go by Laura. Laura Kinney."
                    call LauraFace("confused", 0, Mouth="normal") 
                    $ LauraName = "Laura"       
                    $ Topics.append("Laura")    
                    menu:
                        extend ""
                        "Nice to meet you Laura.": 
                            call Statup("Laura", "Love", 70, 5) # Love  
                            call LauraFace("normal", 0)                
                            ch_l "Yeah, ok."
                        "Hello Laura Laura Kinney.":
                            call LauraFace("confused", 0,Mouth="sucking")   
                            ch_l "It's just-"
                            call LauraFace("smile", 0,Brows="surprised")   
                            call Statup("Laura", "Love", 70, 3) # Love   
                            call Statup("Laura", "Inbt", 70, 2) # Inbt   
                            ch_l "Oh, get it."
                        "Ok, how did you get that name?":
                            call LauraFace("angry", 1,Eyes="side") 
                            call Statup("Laura", "Love", 70, -2) # Love   
                            call Statup("Laura", "Obed", 70, 2) # Obed 
                            ch_l "You're getting too personal."
            "I think I'd prefer calling you X-23." if LauraName == "Laura" and "Laura" in Topics:
                            call Statup("Laura", "Love", 70, -2) # Love   
                            call Statup("Laura", "Obed", 70, 5) # Obed 
                            call LauraFace("sadside", 0,Brows="normal") 
                            ch_l "Suit yourself."        
                            $ L_History.append("X-23")   
                            $ LauraName = "X-23"     
            "My name is [Playername]" if LauraName != "???" and "player" not in Topics:
                    call LauraFace("normal", 0) 
                    ch_l "Ok."     
                    $ Topics.append("player")
                    menu:
                        extend ""
                        ". . .and it's nice to meet you?":
                            call Statup("Laura", "Love", 70, 1) # Love 
                            call LauraFace("confused", 0,Mouth="normal")   
                            ch_l "Yeah, you too." 
                        "So. . .[[moving on]":
                            call Statup("Laura", "Love", 70, 3) # Love   
                            call Statup("Laura", "Obed", 70, 1) # Obed
                            call Statup("Laura", "Inbt", 70, 1) # Inbt  
                            
            "What are you doing here?" if "Training" not in Topics:
                    call Statup("Laura", "Obed", 70, -2) # Obed
                    call LauraFace("confused", 0) 
                    ch_l "Training. That's the point of this place."
                    $ Topics.append("Training")
                    menu:
                        extend ""
                        "I meant in the school, I haven't seen you around before.":
                                call Statup("Laura", "Obed", 70, 2) # Obed 
                        "Ok, that's fair.":
                                call LauraFace("normal", 0) 
                                ch_p "But are you new to this school?"
                                call Statup("Laura", "Love", 70, 3) # Love   
                                call Statup("Laura", "Obed", 70, 4) # Obed
                    ch_l "I've been here since before your time."
                    ch_l "Mostly out in the field though."   
            "So you don't stay here long?" if "Training" in Topics and "Stay" not in Topics:  
                    call Statup("Laura", "Love", 70, 2) # Love   
                    call LauraFace("normal", 0,Eyes="side") 
                    ch_l "I'll be heading out again soon." 
                    call LauraFace("normal", 0) 
                    ch_l "But I am planning to stick around after I get back from this mission."
                    $ Topics.append("Stay")
                
                        
            "What the hell was that?" if len(Topics) <= 1 and "WTF" not in Topics:
                    call Statup("Laura", "Love", 70, -2) # Love   
                    call Statup("Laura", "Obed", 70, 8) # Obed  
                    call LauraFace("confused", 0) 
                    ch_l "It was a robot arm." 
                    call LauraFace("sad", 1,Eyes="leftside") 
                    ch_l "Like I said, sorry."                   
                    call Statup("Laura", "Obed", 70, -3) # Obed
                    call Statup("Laura", "Inbt", 70, 3) # Inbt  
                    call LauraFace("smile", 0,Brows="confused") 
                    ch_l "You probably should have ducked though."
                    $ Topics.append("WTF")
                
            "So what's your mutant power?" if LauraName != "???" and "claws" not in Topics:
                    call Statup("Laura", "Love", 70, 1) # Love   
                    call Statup("Laura", "Obed", 70, 1) # Obed                    
                    call LauraFace("normal", 0) 
                    ch_l "I can heal fast."
                    $ Laura_Arms = 2
                    ch_l "Also I have claws."
                    $ L_Claws = 1
                    call LauraFace("smile", 0,Brows="confused") 
                    "snikt"
                    $ Topics.append("claws")
                    menu:                        
                        "Those claws look pretty sharp.":
                                call Statup("Laura", "Inbt", 70, 3) # Inbt   
                                ch_l "Yeah, indestructible too." 
                        "Cool.":
                                call Statup("Laura", "Love", 70, 3) # Love   
                                call Statup("Laura", "Obed", 70, 2) # Obed
                                call Statup("Laura", "Inbt", 70, 1) # Inbt   
                                call LauraFace("smile", 0,Brows="surprised") 
                                ch_l "Yeah, indestructible too." 
                        "Ouch.": 
                                $ L_Claws = 0
                                call LauraFace("confused", 0) 
                                call Statup("Laura", "Love", 70, -2) # Love   
                                call Statup("Laura", "Obed", 70, -5) # Obed  
                                ch_l "Don't worry, I won't stab you." 
                                call LauraFace("confused", 0,Mouth="normal")      
                                call Statup("Laura", "Inbt", 70, 7) # Inbt   
                                ch_l "Probably."  
                    $ L_Claws = 0
                    $ Laura_Arms = 1
                            
            "Don't you want to know my power?" if "claws" in Topics and "powers" not in Topics:
                    if L_Love >= 405: 
                            call LauraFace("smile", 0,Brows="confused") 
                            ch_l "Yeah, I guess."
                    else:
                            call LauraFace("normal", 0) 
                            ch_l "Not really."
                    call Statup("Laura", "Inbt", 70, 3) # Inbt   
                    $ Topics.append("powers")
                    ch_p "I'm immune to mutant powers and can shut them off." 
                    call LauraFace("smile", 0,Brows="confused") 
                    call Statup("Laura", "Love", 70, 3) # Love   
                    call Statup("Laura", "Obed", 70, 3) # Obed  
                    ch_l "Huh. Interesting. So you can stop me from healing?"
                    ch_p "Yeah. If I touch you, temporarily."  
                    call Statup("Laura", "Obed", 70, 2) # Obed 
                    call Statup("Laura", "Lust", 70, 3) # Lust   
                    ch_l "Give it a try."
                    "She holds out her arm, and you grab it."
                    call Statup("Laura", "Love", 70, 1) # Love   
                    call Statup("Laura", "Obed", 70, 2) # Obed 
                    call Statup("Laura", "Lust", 70, 5) # Lust  
                    call LauraFace("confused", 0) 
                    ch_l "Huh." 
                    call LauraFace("sexy", 1,Eyes="closed") 
                    "You can feel her shudder a little." 
                    call LauraFace("sexy", 1) 
                    call Statup("Laura", "Love", 70, 1) # Love   
                    call Statup("Laura", "Obed", 70, 3) # Obed
                    call Statup("Laura", "Lust", 70, 5) # Lust  
                    ch_l "That feels weird."  
                    call LauraFace("sexy", 1,Eyes="leftside") 
                    call Statup("Laura", "Obed", 70, 1) # Obed 
                    call Statup("Laura", "Lust", 70, 3) # Lust  
                    ch_l "-a little more \"alive\" than usual." 
                    call Statup("Laura", "Inbt", 70, 5) # Inbt  
                    call Statup("Laura", "Lust", 70, 5) # Lust 
                    call LauraFace("sexy", 1,Brows="confused")   
                    ch_l "Almost. . . dangerous."
                
            "Never mind that. . . [[moving on]" if LauraName != "???":
                    $ Loop = 0
            
        if len(Topics) >= 3 and LauraName == "???":
                call Statup("Laura", "Love", 70, -2) # Love   
                call Statup("Laura", "Obed", 70, 5) # Obed
                call Statup("Laura", "Inbt", 70, 5) # Inbt   
                ch_l "Oh, by the way, you can call me \"X-23\"."
                $ LauraName = "X-23"  
        if len(Topics) >= 8:
                $ Loop = 0
        
        
    #close while loop
    ch_l "Ok, I've got a plane to catch."
    if "player" in Topics:
            call Statup("Laura", "Love", 70, 2) # Love   
            call Statup("Laura", "Lust", 70, 1) # Lust  
            call LauraFace("smile",0) 
            ch_l "Maybe I'll see you when I get back, [Playername]."
    else:
            call LauraFace("normal", 0) 
            ch_l "Maybe I'll see you when I get back, stranger."
    if "powers" in Topics:
            call Statup("Laura", "Obed", 70, 2) # Obed
            call Statup("Laura", "Inbt", 70, 2) # Inbt  
            call Statup("Laura", "Lust", 70, 3) # Lust   
            call LauraFace("smile", 1, Brows="confused") 
            ch_l "We should. . . spar."
         
    $ L_Loc = "bg laura"         
    call Set_The_Scene
    
    "She dashes out of the room, headed for the hanger."
    
    $ L_History.append("met")
    $ bg_current = "bg dangerroom"            
    $ Round -= 10      
    call Shift_Focus("Rogue")
    return

# end LauraMeet//////////////////////////////////////////////////////////

                       
label Laura_Key:
        call Set_The_Scene
        call LauraFace("bemused")
        ch_l "Hey, so... this isn't something I usually do but..."
        ch_l "Look, you've been sleeping over a lot and I was thinking..."
        ch_l "Just take it already."
        "She takes your hand and practically forces a key onto your palm before making your fingers close on it."
        $ Keys.append("Laura")
        $ L_Event[0] = 1
        ch_p "Thanks."
        return
        


# Event Laura_Caught_Masturbating  /////////////////////////////////////////////////////  

#Not updated

label Laura_Caught_Masturbating:
            #This label is called from a Location
            call Shift_Focus("Laura")
            "You hear some odd noises coming from Laura's room as you enter."                           #fix this scene, pants option    
            show blackscreen onlayer black
            call LauraOutfit(Changed=1)    
            $ L_Upskirt = 1
            $ L_PantiesDown = 1
            $ L_Loc = bg_current
            call Set_The_Scene(0)
            call Display_Laura(0)
            call LauraFace("sexy")
            $ L_Eyes = "closed"
            $ Laura_Arms = 2
            $ Count = 0   
            hide blackscreen onlayer black
            $ Trigger = "masturbation"
            $ L_DailyActions.append("unseen")
            $ L_RecentActions.append("unseen")    
            call Laura_SexAct("masturbate")
            if "angry" in L_RecentActions:
                return
        
#After caught masturbating. . .
            $ L_Eyes = "sexy"
            $ L_Brows = "confused"
            $ L_Mouth = "smile"
            if L_Mast == 1:        
                    $ L_Mouth = "kiss"
                    ch_l "So what are you doing here? . ."
                    $ L_Eyes = "side"
                    $ L_Mouth = "lipbite"        
                    ch_l "not that I mind the company. . ."
                    $ L_Eyes = "sexy"
                    $ L_Brows = "normal"         
                    $ L_Mouth = "smile"
                    ch_l "But you know, give me a heads up first." 
            else:
                    ch_l "You're around a lot. . ."            
            $ Laura_Arms = 1  
            call LauraOutfit      
            return
    
# end Laura_Caught_Masturbating/////////////////////////////////////////////////////


# Event Laura_Caught /////////////////////////////////////////////////////  


label Laura_Caught(TotalCaught=0):
    $ TotalCaught = R_Caught + K_Caught + E_Caught + L_Caught
    call Shift_Focus("Laura")
    call Checkout
    ch_l "!!!"        
    $ Line = Trigger
    $ Trigger = 0
    $ Trigger2 = 0
    $ Trigger3 = 0
    $ Trigger4 = 0
    $ Trigger5 = 0
    call LauraOutfit
    if R_Loc == bg_current:         
        $ R_Loc = "bg study"
    if K_Loc == bg_current:                
        $ K_Loc = "bg study" 
    if E_Loc == bg_current:                
        $ E_Loc = "bg study"        
    $ bg_current = "bg study"  
    $ L_Loc = "bg study"
    call Set_The_Scene(0)
    show Professor at SpriteLoc(StageLeft)    
    show Laura_Sprite at SpriteLoc(StageRight) with ease
    if R_Loc == bg_current:         
        show Rogue at SpriteLoc(StageFarRight) with ease
    if K_Loc == bg_current:         
        show Kitty_Sprite at SpriteLoc(StageFarRight) with ease
    if E_Loc == bg_current:         
        show Emma_Sprite at SpriteLoc(StageFarRight) with ease
    call XavierFace("shocked")
    call LauraFace("sad")
    ch_x "I'm very disappointed in your behavior, the both of you."
    
    if Line == "fondle thighs" or Line == "fondle breasts" or Line == "fondle pussy" or Line == "hotdog" or Line == "hand":
        ch_x "The two of you, feeling each other up like animals!"
    elif Line == "dildo pussy" or Line == "dildo anal":
        ch_x "Using those. . . devices on each other, unsanitary!"
    elif Line == "lick pussy":
        ch_x "Engaging in. . . cunnilingus. . . dripping everywhere. . ."
    elif Line == "blow":
        ch_x "Right there in public with his {i}penis{/i} in your mouth. . ."
    else:
        ch_x "Having sexual relations in such a public location, it shows very poor character of you!"
    
    if L_Shame >= 40:
        ch_x "Laura, my dear, you're practically naked! At least throw a towel on!"
        "He throws Laura the towel."
        show blackscreen onlayer black 
        $ L_Over = "towel"         
        hide blackscreen onlayer black
    elif L_Shame >= 20:
        ch_x "Laura, my dear, that attire is positively scandalous."
    
    if L_Caught:
        "And this isn't even the first time this has happened!"
    
    if R_Loc == bg_current:             #fix, might not currently work?
        call RogueFace("surprised",2)
        if "Rogue" not in Rules:
            ch_x "And. . .hm, I could have sworn there was someone else. . ."  
        else:
            ch_x "And Rogue, you were just watching this occur!"        
        call RogueFace("bemused",1, Eyes="side")
    elif K_Loc == bg_current:             #fix, might not currently work?
        call KittyFace("surprised",2)
        if "Kitty" not in Rules:
            ch_x "And. . .hm, I could have sworn there was someone else. . ."  
        else:
            ch_x "And Kitty, you were just watching this occur!"        
        call KittyFace("bemused",1,Eyes="side")
    elif E_Loc == bg_current:             #fix, might not currently work?
        call EmmaFace("surprised",2)
        if "Emma" not in Rules:
            ch_x "And. . .hm, I could have sworn there was someone else. . ."  
        else:
            ch_x "And Emma, you were just watching this occur!" 
            ch_x "Unacceptable. . ."        
        call EmmaFace("bemused",1, Eyes="side")
        
    if "rules" in Rules: #if the rules had been removed in a previous game
            call XavierFace("hypno")
            ch_x ". . ."
            ch_x "Hmm, I seem to be having a bit of deja vu here. . ."
            ch_x "I could swear that we've had a conversation like this before, but I cannot recall when. . ."
            call XavierFace("angry")
            ch_x "Regardless, this is a serious issue."
            $ Rules.remove("rules")
            
    $ Count = L_Caught
    menu:
        "Well what have you to say for yourselves?"
        "Sorry sir, won't do it again.":
            if L_Caught < 5:
                call Statup("Laura", "Inbt", 30, -20)            
                call Statup("Laura", "Inbt", 50, -10) 
            call XavierFace("happy")  
            if L_Caught:
                ch_x "But you know you've done this before. . . at least [L_Caught] times. . ." 
            elif TotalCaught:
                ch_x "Not with this young lady, perhaps, but you know you've done this before. . ."
                ch_x "at least [TotalCaught] times. . ." 
            else:
                ch_x "Very well, just don't let it happen again. "
            $ Count += 5
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."
            ch_x "Now return to your rooms and reflect on what you've done."
            
        "Just having a little fun, right [L_Pet]?":
            call Laura_Namecheck
            call LauraFace("bemused")         
            call Statup("Laura", "Lust", 90, 5) 
            if L_Caught < 5:            
                call Statup("Laura", "Inbt", 90, 10)   
                call Statup("Laura", "Love", 90, 10) 
            call XavierFace("angry")
            $ Count += 10
            ch_x "If that's your attitude, harsher methods might be necessary."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."    
            if L_Caught < 5:            
                call Statup("Laura", "Obed", 50, 20)
                call Statup("Laura", "Obed", 90, 20)
                call Statup("Laura", "Inbt", 30, -20)   
            ch_x "I've had enough of you, begone."
            
        "Just this. . . Plan Chi, Laura!" if P_Lvl >= 5:
            if L_Lvl >= 5 and ApprovalCheck("Laura", 1500, TabM=1, Loc="No") and ApprovalCheck("Laura", 750, "I"):                   
                    jump Plan_Chi
            elif ApprovalCheck("Laura", 1000, TabM=1, Loc="No"):
                    call LauraFace("angry",Eyes="side") 
                    $ L_Brows = "angry"
                    ch_l "I told you that was a stupid idea. . ."
                    menu:
                        "Dammit Laura. . .":
                                call LauraFace("angry")
                                call Statup("Laura", "Obed", 50, 5)
                                call Statup("Laura", "Love", 90, -5) 
                        "Yeah, I guess you're right. . .":
                                call LauraFace("bemused") 
                                call Statup("Laura", "Love", 90, 5) 
            else:
                    call LauraFace("confused") 
                    ch_l "Yeah!"
                    ch_l ". . ."
                    ch_l "Wait, plan \"key,\" what??"
                    ch_p "Plan {i}Chi!{/i} . . you know. . ."
                    ch_l "Um. No?"
                    ch_p "oh, yeah, I guess I haven't mentioned that. . ."
                    call LauraFace("bemused") 
            call XavierFace("angry")
            $ Count += 10
            ch_x "I have no idea what that was about, but it sounds like you haven't learned."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."  
            if L_Caught < 5:              
                call Statup("Laura", "Obed", 50, 10)
                call Statup("Laura", "Obed", 90, 10)
                call Statup("Laura", "Inbt", 30, -10)
                call Statup("Laura", "Inbt", 50, -5)   
            ch_x "I've had enough of you, begone."
                        
            
        "You can suck it, old man.":
            call LauraFace("surprised")
            call Statup("Laura", "Lust", 90, 10)
            if L_Caught < 5:
                call Statup("Laura", "Obed", 50, 25)
                call Statup("Laura", "Obed", 90, 40)  
            call XavierFace("angry")
            $ Count += 20
            ch_x "If that's your attitude, harsher methods might be necessary."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days!"
            else:
                ch_x "I'm halving your daily stipend for [Count] days!" 
            if L_Caught < 5:
                if L_Inbt > 50:
                    call Statup("Laura", "Inbt", 90, 15)             
                call Statup("Laura", "Inbt", 30, -15)
                call Statup("Laura", "Inbt", 50, -10)    
            ch_x "Now get out of my sight."
    
    if "Xavier's photo" not in P_Inventory:
            "It would probably be a good idea to find some way to get Xavier to leave you alone."
            "There probably isn't a way available right now though. . ."
#            if L_Caught > 1: 
#                "Maybe I should try searching the office when he's not around."
#            if L_Caught > 2:
#                "I bet Laura could help me get in."
    $ PunishmentX += Count            
    $ L_Caught += 1
    $ L_RecentActions.append("caught")
    $ L_DailyActions.append("caught") 
    call Remove_Girl("All")  
    "You return to your room"
    jump Player_Room
#    $ bg_current = "bg player"
#    return
    
label Plan_Chi:
    call LauraFace("sly")         
    "As you say this, a sly grin crosses Laura's face."
    $ Laura_Arms = 2
    "You quickly approach Xavier and place your hands on his head."
    call XavierFace("psychic")
    ch_x ". . ."
    call XavierFace("shocked")
    "Xavier realizes with a shock that with your powers, his telepathy is useless."   
    show Laura_Sprite at SpriteLoc(StageLeft+100,150) with ease
    $ L_SpriteLoc = StageCenter
    "Laura moves in sits on his lap, placing one hand on his."
    if R_Loc == bg_current and "Omega" not in P_Traits:        
        call RogueFace("surprised")      
        "Rogue looks a bit caught off guard, but goes along with the idea."        
        call RogueFace("sly")
    elif K_Loc == bg_current and "Kappa" not in P_Traits:        
        call KittyFace("surprised")      
        "Kitty looks a bit caught off guard, but goes along with the idea."        
        call KittyFace("sly")
    elif E_Loc == bg_current and "Psi" not in P_Traits:        
        call EmmaFace("surprised")      
        "Emma looks a bit caught off guard, but goes along with the idea."        
        call EmmaFace("sly")
    call XavierFace("angry")
    
    if "Chi" in P_Traits:
            ch_x "Oh, not again."
            ch_x "What is it you want this time?"
            call Statup("Laura", "Obed", 80, 3)
            call Statup("Laura", "Inbt", 80, 1)   
    else:
            ch_x "What is the meaning of this? Unhand me!"
            ch_p "Laura and I were talking, and it seems like neither of us appreciates you bothering us."
            ch_x "And if I continue?"
            ch_p "My little [L_Pet] here has a very particular set of skills, you know. . ."
            call Laura_Namecheck
            $ L_Claws = 1
            call LauraFace("sly")     
            ch_p "She could cause a lot of trouble if she keeps getting called down here. . ."
            "Laura draws her claws along the arm of the Professor's chair, tracing fine lines into the metal." 
            ch_x "Very well. . . I'll forget about your punishment."
            ch_p "Oh, I think we can do a bit better than that. . ." 
            call Statup("Laura", "Obed", 50, 40)
            call Statup("Laura", "Inbt", 80, 30)
            call Statup("Laura", "Obed", 200, 30)
            call Statup("Laura", "Inbt", 200, 10)   
    $ Count = 3
    $ PunishmentX = 0
    while Count:
        $ Count -= 1
        menu:
            ch_l "Well, [L_Petname], what should we ask for?"
            "Don't bother us anymore when we're having fun." if "Laura" not in Rules:
                    ch_x "Very well. . . I could offer you some. . . discretion. . ."
                    $ Rules.append("Laura")
            "You know, it's kinda fun dodging you, catch us if you can." if "Laura" in Rules:
                    ch_x "If you. . . want me to, I suppose. . ."
                    $ Rules.remove("Laura")
            "Raise my stipend." if P_Income < 30 and "Chi" not in P_Traits:    
                    ch_x "Very well. . . but I can only raise it by so much. . ."        
                    $ P_Income += 2
            "Raise my stipend. [[Used](locked)" if P_Income >= 30 or "Chi" in P_Traits:           
                    pass
            "In was interested in a key. . . ":
                menu:
                    "Give me the key to your study." if "Xavier" not in Keys:  
                            ch_x "Fine, take it. . ."  
                            $ Keys.append("Xavier")
                    "Give me the key to your study.[[Owned] (locked)" if "Xavier" in Keys:  
                            pass
                            
                    "Give me the key to Rogue's room." if "Rogue" not in Keys:  
                            ch_x "I. . . suppose I could do that. . ."  
                            $ Keys.append("Rogue")
                    "Give me the key to Rogue's room.[[Owned] (locked)" if "Rogue" in Keys:  
                            pass
                    
                    "Give me the key to Laura's room." if "Laura" not in Keys:  
                            ch_x "Couldn't she provide it? Oh, never mind, here. . ."  
                            $ Keys.append("Laura")
                    "Give me the key to Laura's room.[[Owned] (locked)" if "Laura" in Keys:  
                            pass
                    
                    "Never mind the keys.":
                            $ Count += 1
            "That should do it.":
                $ Count = 0
    ch_x "Very well, that should conclude our business. Please leave." 
    if "Chi" not in P_Traits:
        call Statup("Laura", "Lust", 90, 10)
        call Statup("Laura", "Inbt", 80, 10)
        call Statup("Laura", "Love", 70, 10)
        call Statup("Laura", "Love", 200, 20)
        $ P_Traits.append("Chi")
    $ Laura_Arms = 1
    $ L_Claws = 0
    "You return to your room"
    jump Player_Room
                              
# end Laura_Caught/////////////////////////////////////////////////////

label Laura_BF:
        call Shift_Focus("Laura")
        
        if L_Loc != bg_current:
            $ L_Loc = bg_current
            if "Laura" not in Party:
                "Laura approaches you and motions that she wants to speak to you alone."
            else:   
                "Laura turns towards you and motions that she wants to speak to you alone."
                    
        call Set_The_Scene(0)
        call Display_Laura
        "She looks a bit concerned and you can tell she's a bit anxious about whatever she has to say." 
        call Taboo_Level
        call CleartheRoom("Laura")
        $ L_DailyActions.append("relationship")
        call AnyFace("Laura","angry",1,Eyes="side")        
        $ Line = 0
        ch_l "Hey. So. [L_Petname]. . ."
        call AnyFace("Laura","confused",1,Mouth="lipbite")
        ch_l "I don't know- . . . you're pretty fun to hang out with, ya know?"
        menu:
            extend ""
            "I really love hanging out with you too!":
                call AnyFace("Laura","surprised",2)     
                ch_l "Right, so-"  
                call Statup("Laura", "Obed", 50, -3)
                call Statup("Laura", "Inbt", 80, 1)   
                ch_l ". . ."
                call Statup("Laura", "Love", 200, 5)
                call AnyFace("Laura","bemused",1,Eyes="side")     
                ch_l "\"Love\" is kind of a strong word, [L_Petname]."
            "Yeah, sure, it's a lot of fun.":
                call Statup("Laura", "Love", 200, 10)
                call Statup("Laura", "Inbt", 80, 2)    
                call AnyFace("Laura","smile",0)  
                ch_l "Right?" 
            "I mean, it beats math class. . .":
                call Statup("Laura", "Love", 200, 3)
                call Statup("Laura", "Obed", 80, 3)
                call Statup("Laura", "Inbt", 80, -3) 
                call AnyFace("Laura","angry",1)  
                ch_l "Um, less enthusiasm than I was expecting. . ."
            "If you say so.":
                call Statup("Laura", "Obed", 80, 6)
                call Statup("Laura", "Inbt", 80, -8)    
                call AnyFace("Laura","confused",1)  
                ch_l ". . ."
                
        ch_l "So like I was saying, I don't exactly have a ton of friends."
        call AnyFace("Laura","sadside",1)  
        ch_l "I kind of grew up in a rough place, and then spent a lot of time on the road."
        ch_l "I had a life before coming here."
        menu:
            extend ""
            "What was it like?":
                call Statup("Laura", "Love", 200, 7)
                call Statup("Laura", "Obed", 80, 2)
                call Statup("Laura", "Inbt", 80, 3)   
                call AnyFace("Laura","sad",1,Mouth="lipbite")  
            "Yeah? I know.":
                call Statup("Laura", "Love", 200, 3)
                call Statup("Laura", "Obed", 80, 4)
                call Statup("Laura", "Inbt", 80, 1)   
                call AnyFace("Laura","confused",1,Mouth="lipbite")  
            "I don't need a lot of backstory drama.":
                call Statup("Laura", "Love", 200, -5)
                call Statup("Laura", "Obed", 80, 10)
                call Statup("Laura", "Inbt", 80, -5)   
                call AnyFace("Laura","angry",1)  
                $ Line = "bad"
                ch_l "Fine!"
                ch_l "\"Keep it simple\" it is then."
                ch_l "I don't hate hanging out with you, is all."
        if Line != "bad":
                call AnyFace("Laura","normal",1,Eyes="side")  
                ch_l "Well, you may have guessed I'm related to Wolverine."
                menu:
                    extend ""
                    "Kinda obvious, yeah.":
                            call Statup("Laura", "Love", 200, 4)
                    "I had no idea!":
                            call Statup("Laura", "Love", 200, 3)
                            call Statup("Laura", "Inbt", 80, 1)  
                            call AnyFace("Laura","confused",1)  
                    "Duh.":
                            call Statup("Laura", "Love", 200, 1)
                            call Statup("Laura", "Obed", 80, 2)
                            call AnyFace("Laura","angry",1)  
                ch_l "Well I'm actually his partial clone."
                call AnyFace("Laura","angry",1,Eyes="side")  
                ch_l "I was created to be some sort of biological weapon, an assassin."
                ch_l "I did a lot of work for them as a kid, until eventually I escaped."
                call AnyFace("Laura","sadside",1)  
                ch_l "After that, I had to do a lot of stuff. . . to stay alive."
                ch_l "Stuff I'm not proud of."
                call AnyFace("Laura","sad",1)  
                ch_l "But I don't know. . . being around you, I think it helps."
                call AnyFace("Laura","sad",1,Mouth="smile")  
                ch_l "I kind of feel. . . better."
        if L_SEXP >= 20:
                call Statup("Laura", "Obed", 80, 3)
                call Statup("Laura", "Inbt", 80, 2)   
                call Statup("Laura", "Lust", 80, 5)   
                call AnyFace("Laura","sly",1)  
                ch_l "You really are good in bed, after all." 
        if len(P_Harem) >= 2:
            ch_l "And I know that you have your share of other girls. . ."
            ch_l ". . . but I'd still like to be a part of your life."    
        elif P_Harem:
            ch_l "And I know you're with someone else. . ."
            ch_l ". . . but I'd still like to be a part of your life."   
        else:
            ch_l "I'd just like to be a part of your life."
        call AnyFace("Laura","sad",1,Mouth="smile")  
        ch_l "That's it."
        $ L_Event[5] += 1
        menu:
            extend ""
            "Yeah! I really love you.":
                    call Statup("Laura", "Love", 200, -3)
                    call Statup("Laura", "Obed", 80, -3)
                    call Statup("Laura", "Inbt", 80, 3)   
                    call AnyFace("Laura","surprised",1)  
                    ch_l "Whoa!"
                    call AnyFace("Laura","perplexed")  
                    ch_l "Maybe cool your jets there, [L_Petname]."
                    call AnyFace("Laura","smile",Eyes="side")  
                    ch_l "I wasn't. . ."
                    ch_l "I don't think we're there. . ."
                    call AnyFace("Laura","perplexed",1)  
                    ch_l "Right?"
                    menu:
                        extend ""
                        "Maybe you aren't.":
                                call Statup("Laura", "Love", 200, 10)
                                call Statup("Laura", "Obed", 80, 5)
                                call Statup("Laura", "Inbt", 80, 5)   
                                call Statup("Laura", "Lust", 80, 2)   
                                call AnyFace("Laura","smile",1,Eyes="side")  
                                ch_l "Hehe. . . um."                        
                        "I guess, sure.":
                                call Statup("Laura", "Love", 200, 6)
                                call Statup("Laura", "Obed", 80, 3)
                                call Statup("Laura", "Inbt", 80, 2)  
                                call AnyFace("Laura","angry",1,Eyes="side",Mouth="lipbite")  
                                ch_l "Right, so. . ."
                    #end "I love you"
            "Yeah, I think that'd be great.":
                    call Statup("Laura", "Love", 200, 6)
                    call Statup("Laura", "Obed", 80, 2)
                    call Statup("Laura", "Inbt", 80, 3)   
                    call AnyFace("Laura","smile",1,Eyes="side")  
                    ch_l "Cool."
            "Hmm? Ok.":
                    call Statup("Laura", "Love", 80, 3)
                    call Statup("Laura", "Obed", 80, 5)
                    call Statup("Laura", "Inbt", 80, 3)    
                    call AnyFace("Laura","confused",1,Eyes="side")  
                    ch_l "Yeah. . . cool."
            "I'm not really into that.":
                    call Statup("Laura", "Love", 200, -5)
                    call Statup("Laura", "Obed", 80, 5)
                    call Statup("Laura", "Inbt", 80, -5)   
                    call AnyFace("Laura","sad",1)  
                    if len(P_Harem) >= 2:
                            ch_l "Is it because of [P_Harem[0]] and the rest?"
                    elif P_Harem:
                            ch_l "Is it because of [P_Harem[0]]?"
                    else:
                            ch_l "Why not? What's the deal?"
                    menu:
                        extend ""
                        "Yeah, I don't think she'd understand." if len(P_Harem) == 1: 
                                call Statup("Laura", "Love", 200, -5)
                                call Statup("Laura", "Obed", 80, 7)  
                                call AnyFace("Laura","angry",1,Eyes="side")  
                                call GirlLikesGirl("Laura",P_Harem[0],800,-20,1)
                                ch_l "That bitch."
                        "They wouldn't be cool with that." if len(P_Harem) > 1:
                                call Statup("Laura", "Love", 200, -5)
                                call Statup("Laura", "Obed", 80, 7)  
                                call AnyFace("Laura","angry",1,Eyes="side")  
                                call GirlLikesGirl("Laura",P_Harem[1],800,-20,1)
                                call GirlLikesGirl("Laura",P_Harem[0],800,-20,1)
                                ch_l "Bitches."
                        "It's. . . complicated.":
                                call Statup("Laura", "Love", 200, -20)
                                call Statup("Laura", "Obed", 80, 8)
                                call Statup("Laura", "Inbt", 80, -5)  
                                call AnyFace("Laura","angry",1)  
                                ch_l "Complicated. Sure. Whatever."
                                call AnyFace("Laura","angry",1,Eyes="side")  
                                if len(P_Harem) >= 2:
                                    ch_l "Probably those bitches." 
                                    call GirlLikesGirl("Laura",P_Harem[1],800,-20,1)
                                    call GirlLikesGirl("Laura",P_Harem[0],800,-20,1)
                                elif P_Harem:
                                    ch_l "Probably because of her." 
                                    call GirlLikesGirl("Laura",P_Harem[0],800,-20,1)
                                $ Line = "no"                                
                        "I'm just not into you like that.":
                                call Statup("Laura", "Love", 200, -10)
                                call AnyFace("Laura","surprised",1)  
                                ch_l "Oh."
                                call Statup("Laura", "Obed", 80, 10)
                                call Statup("Laura", "Inbt", 80, 5)   
                                call AnyFace("Laura","sadside",1)  
                                ch_l "Ok, I guess I can respect that."
                    #end "why not?"
                    
                    call AnyFace("Laura","sad",1)  
                    if Line != "no":
                            ch_l "We're still cool though."
                    ch_l "I should. . . leave."
                    "Laura wanders off in a bit of a daze."
                    $ L_Event[5] = 20 
                    call Remove_Girl("Laura")  
                    $ Line = 0
                    return
                            
        if P_Harem:   
                if not ApprovalCheck("Laura", 1400):                    
                        if len(P_Harem) >= 2:
                            ch_l "So you'll break up with the others?" 
                        else:
                            ch_l "So you'll break up with [P_Harem[0]]?"
                        menu:
                            extend ""
                            "Yes, you're worth it.": 
                                    call Statup("Laura", "Love", 200, 20)
                                    call Statup("Laura", "Obed", 80, 5)
                                    call Statup("Laura", "Inbt", 80, 5) 
                                    call AnyFace("Laura","surprised",2,Mouth="smile")  
                                    ch_l ". . ."  
                                    call AnyFace("Laura","smile",1)  
                                    
                                    # fix, I need to add code here to initiate breakups with the rest. . .
                                    
                            "I'd rather you join us.": 
                                    if ApprovalCheck("Laura", 1200):
                                        if GirlLikeCheck("Laura",P_Harem[0]) >= 500:
                                            #if she likes the first girl
                                            if len(P_Harem) >= 2 and GirlLikeCheck("Laura",P_Harem[1]) >= 500:
                                                #if she likes the second girl
                                                if len(P_Harem) >= 3 and GirlLikeCheck("Laura",P_Harem[2]) >= 500:
                                                    #if she likes the third girl
                                                    pass
                                                else:
                                                    $ Line = "no"
                                            else:
                                                $ Line = "no"
                                        else:
                                            $ Line = "no"
                                    else:
                                        $ Line = "no"
                                    if Line == "no":
                                        call Statup("Laura", "Love", 200, -10)
                                        call Statup("Laura", "Obed", 80, 10)
                                        call AnyFace("Laura","angry",1)  
                                        if len(P_Harem) >= 3:
                                            call GirlLikesGirl("Laura",P_Harem[2],800,-10,1)
                                        if len(P_Harem) >= 2:
                                            call GirlLikesGirl("Laura",P_Harem[1],800,-10,1)          
                                        if len(P_Harem) >= 1:
                                            call GirlLikesGirl("Laura",P_Harem[0],800,-10,1)
                                        ch_l "Eh, I'll pass."
                                    else:
                                        call Statup("Laura", "Love", 200,5)
                                        call Statup("Laura", "Obed", 80, 15)
                                        call Statup("Laura", "Inbt", 80, 10) 
                                        call AnyFace("Laura","bemused",1)  
                                        ch_l "Well, I s'pose that wouldn't be so terrible."
                            "What? Of course not.": 
                                        call Statup("Laura", "Love", 200, -25)
                                        call Statup("Laura", "Obed", 80, 5)
                                        if len(P_Harem) >= 3:
                                            call GirlLikesGirl("Laura",P_Harem[2],800,-20,1)
                                        if len(P_Harem) >= 2:
                                            call GirlLikesGirl("Laura",P_Harem[1],800,-20,1)          
                                        if len(P_Harem) >= 1:
                                            call GirlLikesGirl("Laura",P_Harem[0],800,-20,1)
                                        call AnyFace("Laura","angry",1)  
                                        ch_l "Well, fine then."
                                        $ Line = "no"
                        if Line == "no":
                                $ L_Event[5] = 20 
                                call Remove_Girl("Laura")  
                                $ Line = 0
                                return
                #end "she tries to get you to break up with the rest. . .
                
                #if you agreed, but have other girls. . .
                if len(P_Harem) >= 2:
                    ch_l "And you don't think the others would mind?" 
                else:
                    ch_l "And you don't think [P_Harem[0]] would mind?" 
                menu:
                    extend ""
                    "No, actually they're fine with it." if "LauraYes" in P_Traits:
                            call Statup("Laura", "Love", 200, 5)
                            call Statup("Laura", "Obed", 80, 10)
                            call Statup("Laura", "Inbt", 80, 5)   
                            call AnyFace("Laura","surprised",1)  
                            ch_l "Oh, cool."                        
                    "Actually. . . I guess we'll need to work on that one." if "LauraYes" not in P_Traits:
                            call Statup("Laura", "Love", 200, 3)
                            call Statup("Laura", "Obed", 80, 3)
                            call Statup("Laura", "Inbt", 80, 1)   
                            call Statup("Laura", "Lust", 80, 1)   
                            call AnyFace("Laura","confused",1)  
                            ch_l "Hmm, get back to me, I guess?"
                            $ L_Event[5] = 20 
                            call Remove_Girl("Laura")  
                            $ Line = 0
                            return      
                if len(P_Harem) >= 3:
                    call GirlLikesGirl("Laura",P_Harem[2],900,20,1)
                if len(P_Harem) >= 2:
                    call GirlLikesGirl("Laura",P_Harem[1],900,20,1)          
                if len(P_Harem) >= 1:
                    call GirlLikesGirl("Laura",P_Harem[0],900,20,1)
        # end harem stuff
        
        if "Historia" not in P_Traits:
            $ P_Harem.append("Laura")
            if "LauraYes" in P_Traits:       
                    $ P_Traits.remove("LauraYes")
            $ L_Petnames.append("boyfriend")
            $ L_Traits.append("dating")
            call Harem_Initiation
        call Statup("Laura", "Love", 200, 3)
        call Statup("Laura", "Obed", 80, 3)
        call Statup("Laura", "Inbt", 80, 1)   
        call Statup("Laura", "Lust", 80, 1) 
        call AnyFace("Laura","sly",1)    
        ch_l "So, did you have any plans for the next few minutes? . ."
        if "Historia" in P_Traits:
                return 1
        $ Tempmod = 10
        call Laura_SexMenu
        $ Tempmod = 0
            
        return

  
## start Laura_Love//////////////////////////////////////////////////////////
label Laura_Love(Shipping=[],Shipshape=0,Topics=[]):   
    # SHipping is used to track who else you're involved with
    # if L_Event[6] = 5, then it cleared
    # if L_Event[6] = 20, then it broke because you didn't love her
    # if L_Event[6] = 23, then it broke because you pissed her off
    # if L_Event[6] = 25, then it broke and you already went through the redux
    
    if ApprovalCheck("Rogue", 1200, "LO"):
            $ Shipping.append("Rogue") 
    if ApprovalCheck("Kitty", 1200, "LO"):
            $ Shipping.append("Kitty")
    if ApprovalCheck("Emma", 1200, "LO"):
            $ Shipping.append("Emma")
    $ Shipshape = len(Shipping)
        
    if L_Loc == bg_current or "Laura" in Party:
            "Laura glances over at you with a concerned look."
    else:
            "Laura turns a corner and notices you."
    if bg_current != "bg laura" and bg_current != "bg player":           
            "With little word, she moves behind you and pushes you towards her room."
            $ bg_current = "bg laura"
    $ L_Loc = bg_current
    call Set_The_Scene
    call CleartheRoom("Laura")
    call Taboo_Level
    $ L_DailyActions.append("relationship")           
    call AnyFace("Laura","sad",1)        
    ch_l "Hey, so, I like what this is. . ."
    ch_l "-what we have. . ."
    call AnyFace("Laura","sadside",1)  
    ch_l "It's been kind of hard for me to open up to people. . ."
    ch_l "I've been betrayed a lot out there."
    menu:
        extend ""
        "I would never betray you.":
                call AnyFace("Laura","bemused",1)  
                call Statup("Laura", "Love", 200, 10)
                call Statup("Laura", "Obed", 70, 5)
                call Statup("Laura", "Inbt", 60, 5)  
                ch_l "I. . . know that now." 
        "I'm sorry to hear that.":            
                call AnyFace("Laura","sadside",1,Mouth="smile")  
                call Statup("Laura", "Love", 200, 5)
                call Statup("Laura", "Obed", 90, -5)
                call Statup("Laura", "Inbt", 60, 10) 
                ch_l ". . ."
                call AnyFace("Laura","smile",1)  
                ch_l "Thank you. . ."
        "That must be rough.":
                call AnyFace("Laura","sadside",1,Mouth="normal")  
                call Statup("Laura", "Love", 200, 5)
                ch_l ". . ."
                call AnyFace("Laura","smile",1)  
                ch_l "It was. . ."
        "Wow, that sucks.":
                call AnyFace("Laura","confused",1)  
                call Statup("Laura", "Love", 200, -5)
                call Statup("Laura", "Obed", 90, 10)
                call Statup("Laura", "Inbt", 90, -5)
                ch_l ". . ."
                call AnyFace("Laura","angry",1,Eyes="side")  
                ch_l "Right, so. . ."
    ch_l "I didn't always have it as easy as I've had it here."
    $ L_Eyes = "normal"
    ch_l "I only thought it fair to tell you a little about that history."
    $ Line = 0
    while len(Topics) < 9 and "exit" not in Topics:
            #Lines are topics of current discussion. "Topics" catalogues things alrewady discussed
                    
            if Line == "facility":
                    menu:
                        extend ""
                        "How many people did you kill?" if "kills" not in Topics:
                                call AnyFace("Laura","angry",0,Eyes="side")  
                                ch_l "Dozens. Maybe more. At least 13 primary targets."
                                ch_l "Too many \"collaterals.\""
                                $ Topics.append("kills")
                        "Did you ever fail a mission?" if "fail" not in Topics:
                                call AnyFace("Laura","angry",0,Eyes="side",Brows="normal")  
                                ch_l "Once or twice." 
                                ch_l "Sometimes they managed to get away." 
                                ch_l "I'm not proud of who I was back then, but even then. . ."
                                $ L_Mouth = "smile"
                                ch_l ". . . a part of me was happy when they did."
                                $ Topics.append("fail")
                        "Did anyone take care of you?" if "mother" not in Topics:
                                call AnyFace("Laura","smile",0)  
                                ch_l "My mother, Sarah Kinney."
                                ch_l "She's the one who birthed me, and was also one of the scientists that helped create me."                                
                                call AnyFace("Laura","sadside",0)  
                                ch_l "She tried to help me, until I killed her."
                                $ Topics.append("mother")          
                                $ Line = "mother"                
                        "How did you escape?" if "escape" not in Topics:
                                call AnyFace("Laura","sadside",0)  
                                ch_l "Mother."
                                ch_l "She got me out, found me an escape route." 
                                ch_l "It was the last thing she did." 
                                $ Topics.append("escape")       
                                $ Line = "mother"     
                        "I'd like to know more about what came after.":     
                                $ Line = "NYX"     
                        "Enough about that though. . .":  
                                $ Line = 0     
                                
            # end facility questions
            
            if Line == "mother":
                    menu:
                        extend ""
                        "Who was your mother?" if "mother" not in Topics:
                                call AnyFace("Laura","smile",0)  
                                ch_l "Her name was Sarah Kinney."
                                ch_l "She's the one who birthed me, and was also one of the scientists that helped create me."                              
                                call AnyFace("Laura","sadside",0)  
                                ch_l "She tried to help me, until I killed her."
                                $ Topics.append("mother")          
                                $ Line = "mother"       
                        "Why would you kill her?" if "killed" not in Topics and "mother" in Topics:                              
                                call AnyFace("Laura","sad",0,Eyes="surprised")  
                                ch_l "I didn't want to, but the Trigger scent made me. . ."                              
                                call AnyFace("Laura","sadside",0)  
                                if "trigger" in L_History:                 
                                        ch_l "I've mentioned that to you before. . ."
                                else:
                                        $ L_History.append("trigger")
                                ch_l ". . . it can make me kill, even if I don't want to." 
                                $ Topics.append("killed")
                        "It wasn't your fault." if "killed" in Topics:
                                call Statup("Laura", "Love", 200, 5)
                                call Statup("Laura", "Obed", 70, 5)
                                call Statup("Laura", "Inbt", 70, 5)                              
                                call AnyFace("Laura","sad",0)  
                                ch_l "Not completely, no."                              
                                call AnyFace("Laura","sadside",0)  
                                ch_l "But my hands aren't clean."
                                $ Line = "facility"
                        "That must have been horrible." if "killed" in Topics:                              
                                call AnyFace("Laura","sadside",0)  
                                call Statup("Laura", "Love", 200, 5)
                                call Statup("Laura", "Obed", 90, 5)
                                ch_l "It's taken me some time. . ."                              
                                call AnyFace("Laura","normal",0)  
                                ch_l "but I think I'm ok with it now." 
                                $ Line = "facility"
                        "Bummer." if "killed" in Topics:                              
                                call AnyFace("Laura","angry",1) 
                                call Statup("Laura", "Love", 200, -10)
                                call Statup("Laura", "Obed", 90, 5) 
                                ch_l "Are you seriously making fun of my mother's death?!"
                                $ Topics.append("exit")
                                $ Line = "angry"
            # end questions about mother
            
            if Line == "NYX":
                    menu:
                        extend ""                
                        "What did you do for a living?" if "living" not in Topics:                              
                                call AnyFace("Laura","sadside",0)  
                                ch_l "There wasn't much I could do at the time, I mostly just scrounged for food."
                                ch_l "You can get by on some pretty awful stuff if you have a healing factor."                              
                                call AnyFace("Laura","bemused",1,Brows="sad")  
                                ch_l "I also did some. . . shady stuff."
                                $ Topics.append("living")
                                
                        "Was it sexual?" if "work" not in Topics and "living" in Topics:                              
                                call AnyFace("Laura","sadside",2)  
                                call Statup("Laura", "Obed", 90, 5)
                                call Statup("Laura", "Inbt", 90, 10)
                                ch_l ". . ."
                                $ L_Blush = 1
                                ch_l "A little."
                                $ Line = "work"
                                $ Topics.append("work")
                        
                        "Did you hurt people?" if "work" not in Topics and "living" in Topics:                              
                                call AnyFace("Laura","surprised",0,Eyes="normal")  
                                ch_l "No, definitely not."
                                ch_l "After the facility, I just couldn't take that sort of work anymore."                              
                                call AnyFace("Laura","bemused",0)  
                                ch_l "I avoided hurting anyone."                              
                                call AnyFace("Laura","sadside",2)  
                                ch_l "It tended to be more. . . sexual work."
                                $ Line = "work"
                                $ Topics.append("work")                            
                            
                        "And then you eventually made it here? [[exit]" if "xaviers" not in Topics:                              
                                call AnyFace("Laura","bemused",0)  
                                ch_l "Yeah, eventually."
                                ch_l "I'd seen Wolverine on the news, and thought maybe he had some answers."
                                ch_l "He's not around much though."
                                $ Topics.append("xaviers")      
                                $ Line = 0
                        "Good thing you made it here. [[exit]" if "xaviers" in Topics:                               
                                call AnyFace("Laura","smile",0)  
                                ch_l "Yeah."
                                $ Line = 0
            
            if Line == "work":                                
                    call AnyFace("Laura","sadside",0,Mouth="normal")  
                    ch_l "It was mostly the rougher customers."
                    ch_l "The ones who couldn't control their tempers."                              
                    call AnyFace("Laura","angry",0,Mouth="smile")  
                    ch_l "Better for the girl who can heal to take the hits, right?"                      
                    menu:
                            extend ""  
                            "That's terrible. I wish I could have protected you.":                              
                                    call AnyFace("Laura","smile",1)  
                                    call Statup("Laura", "Love", 200, 5)
                                    call Statup("Laura", "Obed", 90, 5)
                                    call Statup("Laura", "Inbt", 90, -5)
                                    ch_l "Thanks, but I was ok."                              
                                    call AnyFace("Laura","sadside",0)  
                                    ch_l "I didn't deserve it, but I felt like I did at the time."
                            "You're strong to have made it out of there.":                              
                                    call AnyFace("Laura","smile",0)  
                                    call Statup("Laura", "Love", 200, 5)
                                    call Statup("Laura", "Obed", 90, 10)
                                    call Statup("Laura", "Inbt", 90, 5)
                                    ch_l "Thanks." 
                                    ch_l "I didn't really think of it like that. . ."                              
                                    call AnyFace("Laura","sadside",0)  
                                    ch_l "I just felt like I'd deserved it."
                                    ch_l "But I realized how wrong that was."
                            "Yeah, that makes sense.":                              
                                    call AnyFace("Laura","confused",1)  
                                    call Statup("Laura", "Love", 200, -5)
                                    call Statup("Laura", "Obed", 90, 15)
                                    call Statup("Laura", "Inbt", 90, -5)
                                    ch_l "Don't think before you speak, do you?"                              
                                    call AnyFace("Laura","sadside",0)  
                                    ch_l "It wasn't right, I just didn't realize it at the time." 
                    ch_l "Eventually I got past it and decided to get out of there."
                    ch_l "Not like they could stop me." 
                    $ Line = "NYX"
                                    
            if not Line:
                    # Primary menu, falls through to this
                    menu:
                        extend ""
                        "What did you do back at the facility?" if "facility" not in Topics:                              
                                call AnyFace("Laura","sadside",0)  
                                ch_l "After they tested what I could do, they put me to work."        
                                ch_l "Mainly, I killed people for them."   
                                $ Topics.append("facility")
                                $ Line = "facility"
                        "More about that facility. . ." if "facility" in Topics:
                                $ Line = "facility"
                                
                        "Where did you go after you escaped?" if "NYX" not in Topics:                              
                                call AnyFace("Laura","sadside",0)  
                                ch_l "I wandered in the wilderness for weeks." 
                                ch_l "Eventually I found my way to New York."
                                ch_l "I lived on the streets for a few years."
                                $ Topics.append("NYX")
                                $ Line = "NYX"  
                        "More about after the escape. . ." if "NYX" in Topics:
                                $ Line = "NYX"
                            
                        "I'm glad you shared that with me. [[exit]" if len(Topics) >= 5:                              
                                call AnyFace("Laura","smile",0)  
                                call Statup("Laura", "Love", 200, 10)
                                call Statup("Laura", "Obed", 90, 3)
                                call Statup("Laura", "Inbt", 90, 3)
                                ch_l "Thanks for listening to me ramble."
                                $ Topics.append("exit")
                        "I think that's probably enough. [[exit]" if "facility" in Topics and "NYX" in Topics:                              
                                call AnyFace("Laura","sadside",0, Mouth="smile")  
                                call Statup("Laura", "Obed", 90, 10)
                                ch_l "Yeah, you get the idea."
                                $ Topics.append("exit")
                        "I don't really care about that. [[exit]":                              
                                call AnyFace("Laura","angry",0)  
                                call Statup("Laura", "Love", 200, -15)
                                call Statup("Laura", "Obed", 50, 5)
                                call Statup("Laura", "Obed", 90, 10)
                                call Statup("Laura", "Inbt", 90, -5)
                                ch_l "Oh, I'm sorry if I was boring you with my life story."
                                $ Line = "angry"
                                $ Topics.append("exit")
    
    #end while loop
        
    if Line == "angry":                              
            call AnyFace("Laura","angry",0)  
            ch_l "And here I was thinking that I meant something to you."
            ch_l "Well forget that!" 
            $ Line = 0
            $ L_Event[6] = 23
            $ L_RecentActions.append("angry")
            $ L_DailyActions.append("angry")
            hide Laura_Sprite with easeoutright
            call Remove_Girl("Laura")
            $ L_Loc = "hold" #puts her off the board for the day
            return
                                  
    call AnyFace("Laura","bemused",0,Eyes="down")  
    ch_l "I just thought you should know,"                              
    call AnyFace("Laura","smile",2)  
    ch_l "I love you."
    menu:
            extend ""
            "I love you too!":                              
                call AnyFace("Laura","smile",1)  
                call Statup("Laura", "Love", 200, 20)
                call Statup("Laura", "Inbt", 90, 5)
                ch_l "For a second there you had me worried."
                $ L_Petnames.append("lover")
                jump Laura_Love_End
            "I know.":            
                call AnyFace("Laura","smile",1) 
                call Statup("Laura", "Love", 200, 10)
                call Statup("Laura", "Obed", 90, 5)
                call Statup("Laura", "Inbt", 90, 10)
                call Statup("Laura", "Lust", 90, 5) 
                ch_l "Smooth one. Seriously though, how about you?"
            "Neat?":            
                call AnyFace("Laura","confused",1) 
                call Statup("Laura", "Obed", 90, 5)
                ch_l "I'm gonna need a bit more there, [L_Petname]."
            "Huh.":            
                call AnyFace("Laura","confused",1) 
                call Statup("Laura", "Love", 200, -5)
                call Statup("Laura", "Obed", 90, 10)
                ch_l "I'm not sure how to take that one."
    
    
    menu:
            extend ""
            "Oh, I love you too!":            
                call AnyFace("Laura","smile",1) 
                call Statup("Laura", "Love", 200, 15)
                call Statup("Laura", "Obed", 90, 5)
                call Statup("Laura", "Inbt", 90, 5)
                ch_l "For a second there you had me worried."
                $ L_Petnames.append("lover")
                jump Laura_Love_End
            "I. . . love you back?":            
                call AnyFace("Laura","confused",1) 
                call Statup("Laura", "Love", 200, 5)
                call Statup("Laura", "Obed", 90, 10)
                ch_l "Ok, I'll take it."
                $ L_Petnames.append("lover")
                jump Laura_Love_End
            "I mean, that's cool and all. . .":            
                call AnyFace("Laura","sadside",1) 
                call Statup("Laura", "Love", 200, -5)
                call Statup("Laura", "Obed", 90, 10)
                call Statup("Laura", "Inbt", 90, -5)
                ch_l ". . . but you don't love me back. Got it."
            "That's. . . uncomfortable.":            
                call AnyFace("Laura","angry",1) 
                call Statup("Laura", "Love", 200, -10)
                call Statup("Laura", "Obed", 90, 15)
                call Statup("Laura", "Inbt", 90, -5)
                ch_l "I don't like where this is heading."
    
    ch_l "What's your problem?"
    ch_l "Is it someone else?"
    $ Line = 0
    menu:
            extend ""
            "Yes, it's Rogue." if "Rogue" in Shipping and Shipshape < 3:
                $ Line = "Rogue"
            "Yes, it's Kitty." if "Kitty" in Shipping and Shipshape < 3:
                $ Line = "Kitty"
            "Yes, it's Emma." if "Emma" in Shipping and Shipshape < 3:
                $ Line = "Emma"
            "Yes, it's the others" if Shipshape > 1:
                call Statup("Laura", "Obed", 90, 15)
                call Statup("Laura", "Inbt", 90, 5)
                call Statup("Laura", "Lust", 90, 5)            
                call AnyFace("Laura","sadside",1) 
                ch_l "Well, you do have your pick."
            "There's nobody else.":
                call Statup("Laura", "Love", 200, -15)
                call Statup("Laura", "Obed", 90, 15)
                call Statup("Laura", "Inbt", 90, 5)            
                call AnyFace("Laura","sad",1) 
                if ApprovalCheck("Laura", 1000, "OI"):
                    ch_l "I guess that's something."
                else:
                    ch_l ". . ."
            "It's a \"you\" problem.":
                call LauraFace("angry")
                call Statup("Laura", "Love", 200, -25)
                call Statup("Laura", "Obed", 90, 15)
                ch_l "You're seriously messing with me?" 
                call Statup("Laura", "Love", 200, -10)
                ch_l "You don't want to see me when I'm angry."
                $ L_RecentActions.append("angry")
                $ L_DailyActions.append("angry")
   
   
    if Line:        
            #If you called out a girl,
            if GirlLikeCheck("Laura",Line) >= 800:
                    call Statup("Laura", "Love", 200, 5)
                    call Statup("Laura", "Obed", 90, 20)
                    call Statup("Laura", "Inbt", 90, 5)
                    call Statup("Laura", "Lust", 90, 5)            
                    call AnyFace("Laura","sadside",1) 
                    ch_l "Yeah, I guess she's great."
            else:
                    call LauraFace("angry",Eyes="side") 
                    call Statup("Laura", "Love", 200, -5)
                    call Statup("Laura", "Obed", 90, 20)          
                    ch_l "Bitch."
                    $ L_RecentActions.append("angry")
                    call GirlLikesGirl("Laura",Line,800,-50,1)                    
    ch_l "Well, if that's the way you feel about it. . ."
    ch_l "I'll. . . see you later."
    ch_l "This. . . hurt."
        
label Laura_Love_End:
    if "lover" not in L_Petnames:     
            $ L_Event[6] = 20 
            hide Laura_Sprite with easeoutright
            call Remove_Girl("Laura")
            $ L_Loc = "hold" #puts her off the board for the day
            return
        
    $ L_Event[6] = 5
    "Laura grabs you in a crushing hug."
    call Statup("Laura", "Love", 200, 25)
    call Statup("Laura", "Lust", 90, 5)            
    call AnyFace("Laura","sly",1) 
    ch_l "So. . . now that we have some free time. . ."
    call Statup("Laura", "Lust", 90, 10)
    
    if not L_Sex:            
        call AnyFace("Laura","bemused",2) 
        ch_l "I think I'm ready. . ."
    else:
        ch_l "Would you like to have some fun?"        
    menu:
            extend ""
            "Yeah, let's do this. . . [[have sex]":      
                call Statup("Laura", "Inbt", 30, 20) 
                call Statup("Laura", "Obed", 70, 10)
                ch_l "Hmm. . ."  
                call Laura_SexAct("sex")
            "I have something else in mind. . .[[choose another activity]":
                $ L_Brows = "confused"
                call Statup("Laura", "Obed", 70, 25)
                ch_l "Like what? . ."    
                $ Tempmod = 20
                call Laura_SexMenu   
    return
        
label Laura_Love_Redux:  
     #this is for if you rejected her but want a second chance
    $ Line = 0
    $ L_DailyActions.append("relationship")
    
    if L_Event[6] >= 25:
            #if this is the second time through
            ch_p "I hope you've forgiven me, I still love you."
            call Statup("Laura", "Love", 95, 10) 
            if ApprovalCheck("Laura", 950, "L"):
                $ Line = "love"
            else:
                call LauraFace("angry")   
                ch_l "You're still working your way out of the hole, [L_Petname]."
                $ L_Eyes="side"
                ch_l ". . ."                
                call LauraFace("angry",Mouth="lipbite") 
                ch_l "But let me hear your pitch." 
    elif L_Event[6] >= 23:
            #if you pissed her off the first time
            ch_p "I was rude when you opened up to me before."
            call Statup("Laura", "Love", 95, 10) 
            if ApprovalCheck("Laura", 950, "L"):
                ch_l "And. . ."
            else:
                call LauraFace("angry")   
                ch_l "You're still working your way out of the hole, [L_Petname]."
                $ L_Eyes="side"
                ch_l ". . ."                
                call LauraFace("angry",Mouth="lipbite") 
                ch_l "But let me hear your pitch." 
    else:
            ch_p "Remember when I told you that I didn't love you?"
            call LauraFace("perplexed",1)   
            ch_l ". . ."
            call LauraFace("angry", Eyes="side")               
            ch_l "How could I forget?"
            
    if Line != "love":
            menu:
                extend ""
                "I'm sorry, I didn't mean it.":
                    $ L_Eyes = "surprised"
                    ch_l "Oh really?"
                    ch_l "That's awfully convenient." 
                    ch_p "Yeah. I mean, yes, I love you, Laura."
                    call Statup("Laura", "Love", 200, 10) 
                    if ApprovalCheck("Laura", 950, "L"):
                        $ Line = "love"
                    else:
                        call LauraFace("sadside")   
                        ch_l "Well, maybe I don't, anymore. . ."                        
                "I've changed my mind, I do love you, so. . .":
                    if ApprovalCheck("Laura", 950, "L"):
                        $ Line = "love"
                        ch_l "Well that's great."
                    else:
                        $ L_Mouth = "sad"
                        ch_l "Good for you."
                        call Statup("Laura", "Inbt", 90, 10) 
                        call LauraFace("sadside")    
                        ch_l "I don't exactly have the same mind either. . ."
                "Um, never mind.":
                    call Statup("Laura", "Love", 200, -30) 
                    call Statup("Laura", "Obed", 50, 10)  
                    call LauraFace("angry")   
                    ch_l "Oh, fuck you."
                    $ L_RecentActions.append("angry")
                    $ L_DailyActions.append("angry")
    if Line == "love":
            call Statup("Laura", "Love", 200, 40) 
            call Statup("Laura", "Obed", 90, 10)
            call Statup("Laura", "Inbt", 90, 10) 
            call LauraFace("smile")    
            ch_l "I'm glad you came around."
            ch_l "I love you too, [L_Petname]!"
            if L_Event[6] < 25:             
                call LauraFace("sly")   
                "She grabs the back of your head and pulls you close."
                ch_l "Next time, don't keep me waiting."
            $ L_Petnames.append("lover")       
    $ L_Event[6] = 25
    return

# end Laura_Love//////////////////////////////////////////////////////////


# start Laura_Sub//////////////////////////////////////////////////////////

label Laura_Sub:    
    call Shift_Focus("Laura")
    if L_Loc != bg_current and "Laura" not in Party:
        "Suddenly, Laura shows up and says she needs to talk to you."
    
    $ L_Loc = bg_current
    call Set_The_Scene(0)
    call Display_Laura
    call CleartheRoom("Laura")
    call Taboo_Level
    $ L_DailyActions.append("relationship")
    call LauraFace("bemused", 1)
    
    $ Line = 0
    ch_l "I've noticed something."    
    ch_l "You've been trying to boss me around lately."
    menu:
        ch_l "I've noticed you trying to boss me around.{w=2.8}{nw}"
        "I guess. That's just kind of what comes naturally for me.":   
                pass
        "Sorry. I didn't mean to come off like that.":
                pass
        "Yup. Deal with it.": 
                pass
    "Before you can speak, she puts her hand over your mouth."   
    call LauraFace("sly", 1,Eyes="side")
    ch_l "I don't know how I feel about that."
    if L_Event[6]: #if you've done the Love route
            call LauraFace("sadside", 1)
            ch_l "You know the past I've had, with the facility, with the. . . "
            ch_l ". . . work I had to do for them."
            call LauraFace("sad", 1)
            ch_l "I don't know if I want to let anyone tell me what to do like that again."     
    menu Laura_Sub_Question:    
        extend ""        
        "I guess I can be demanding.":   
                call LauraFace("sly", 1)
                call Statup("Laura", "Obed", 200, 10)
                call Statup("Laura", "Inbt", 50, 5)
        "Sorry. I didn't mean to come off like that.":
                call LauraFace("sly", 1)
                call Statup("Laura", "Love", 80, 5)
                call Statup("Laura", "Obed", 200, -5)
                call Statup("Laura", "Inbt", 50, -5)
                ch_l "I get it, you're assertive. . ." 
        "Remind me about the facility?" if L_Event[6]:
                call LauraFace("sadside", 1)
                call Statup("Laura", "Love", 99, -10)
                call Statup("Laura", "Inbt", 50, -5)
                ch_l "I told you, I was raised in an underground government lab."
                ch_l "They ordered me to kill people for them."
                call LauraFace("sly", 0, Brows= "angry")
                ch_l ". . . until I got tired of taking orders."
                jump Laura_Sub_Question
        "What bothers you about being told to do things?" if not L_Event[6]:
                call LauraFace("sadside", 1)
                call Statup("Laura", "Love", 80, 5)
                ch_l "I've just had some rough experiences."
                ch_l "You don't need to know about them."
                ch_l ". . ."
                call LauraFace("sad", 0)
                ch_l "Let's just say I was ordered to do some things I regret."
                jump Laura_Sub_Question
        "Get with the program.": 
                if ApprovalCheck("Laura", 1000, "LO"):
                        call LauraFace("sly", 1)
                        call Statup("Laura", "Obed", 200, 20)
                        call Statup("Laura", "Inbt", 50, 10)
                        ch_l "Hmmm. . ."
                else:
                        call Statup("Laura", "Love", 200, -10)
                        call Statup("Laura", "Inbt", 50, -5)
                        call LauraFace("angry",0)
                        ch_l "You're not off to a good start here. You might want to rethink your attitude."
                        menu:        
                            extend ""
                            "Sorry.  I thought that's what you were into.": 
                                    call LauraFace("perplexed", 1,Eyes="side")
                                    $ L_Eyes = "side"
                                    call Statup("Laura", "Love", 75, 10)
                                    call Statup("Laura", "Obed", 200, 5)
                                    call Statup("Laura", "Inbt", 50, 5)
                                    ch_l ". . . after I just said. . ."
                                    call LauraFace("sly", 1)
                                    ch_l "Ok, whatever."
                            "I don't care.":
                                    call Statup("Laura", "Love", 95, -10)
                                    ch_l "I guess not."
                                    $ Line = "rude"
      
    if not Line:
            # She's advancing to the next stage    
            call LauraFace("sly", 1)        
            ch_l "Look, it's not like. . ."
            call LauraFace("sly", 2)
            ch_l ". . . it's not like I hate it."
            call LauraFace("smile", 1, Eyes="side")
            ch_l ". . . I actually think it might make me. . ."
            menu:
                extend ""
                "-excited?":
                    call Statup("Laura", "Obed", 200, 5)
                    call Statup("Laura", "Inbt", 50, 5)
                    ch_l ". . ."
                    call LauraFace("sly", 1)
                    call Statup("Laura", "Lust", 50, 10)
                    ch_l "a little, yeah."
                "-digusted?":
                    call Statup("Laura", "Love", 75, -5)
                    call Statup("Laura", "Obed", 200, -5)
                    call LauraFace("sadside", 1)
                    ch_l ". . . kind of,"
                    call LauraFace("sly", 1)
                    call Statup("Laura", "Inbt", 70, 5)
                    call Statup("Laura", "Lust", 50, 5)
                    ch_l "but also kind of excited by it."
                "-hungry?":
                    call LauraFace("confused", 1,Eyes="surprised",Mouth="smile")
                    call Statup("Laura", "Obed", 200, -5)
                    call Statup("Laura", "Inbt", 50, -5)
                    ch_l "?!"
                    call LauraFace("confused", 1,Eyes="normal",Mouth="smile")
                    ch_l "Well. . . yeah? But not for-"
                    call LauraFace("sly", 1)
                    call Statup("Laura", "Lust", 50, 5)
                    ch_l "I mean, it makes me kind of. . . excited."
                "-horny?":
                    call Statup("Laura", "Obed", 200, 10)
                    call Statup("Laura", "Inbt", 50, 5)
                    call LauraFace("startled", 2,Mouth="lipbite")
                    ch_l "!"
                    call LauraFace("sly", 1, Eyes="side")
                    call Statup("Laura", "Inbt", 50, 5)
                    call Statup("Laura", "Lust", 50, 10)
                    call Statup("Laura", "Lust", 70, 5)
                    ch_l "Yes."
            menu:
                extend ""
                "Good. If you wanna be with me, then you follow my orders.":
                        if ApprovalCheck("Laura", 1000, "LO"):
                            call LauraFace("sly", 1)
                            call Statup("Laura", "Obed", 200, 15)
                            call Statup("Laura", "Inbt", 50, 10)
                            ch_l "Hmmm. . ."                        
                        else:
                            call LauraFace("sadside", 1,Mouth="normal")
                            call Statup("Laura", "Love", 200, -5)
                            call Statup("Laura", "Obed", 200, 10)                      
                            ch_l "You might want to slow your roll there, [L_Petname]."
                            menu:      
                                extend ""
                                "Whatever. That's how it is. Take it or leave it.":
                                        call LauraFace("angry")
                                        call Statup("Laura", "Love", 200, -10)
                                        call Statup("Laura", "Obed", 200, 5)
                                        ch_l "I think you're pushing it too far there, [L_Petname]." 
                                        $ Line = "rude"
                                "Ok, just a little." : 
                                        call LauraFace("bemused", 1)
                                        call Statup("Laura", "Love", 95, 5)
                                        call Statup("Laura", "Inbt", 50, 5)
                                        ch_l "-but not too much."
                                
                "Yeah? You think it's sexy?":
                            call LauraFace("bemused", 2,Eyes="side")
                            call Statup("Laura", "Obed", 200, 5)
                            call Statup("Laura", "Inbt", 50, 10)
                            ch_l ". . ."
                            call Statup("Laura", "Lust", 50, 5)
                            ch_l "Yeah."
                        
                "You sure you don't want me to back off a little?":  
                        call LauraFace("startled", 1,Eyes="squint")
                        call Statup("Laura", "Obed", 200, -5)
                        menu:
                            ch_l "Well if you have to ask. . ."
                            "Only if you're okay with it.":
                                call LauraFace("bemused", 1)
                                call Statup("Laura", "Love", 95, 10)
                                call Statup("Laura", "Inbt", 50, 10)
                                $ Line = 0
                            "Uhm. . .yeah. I think it's weird.  Sorry.":  
                                call LauraFace("sad", 1, Eyes="surprised")                              
                                call Statup("Laura", "Love", 200, -15)
                                call Statup("Laura", "Obed", 200, -5)
                                call Statup("Laura", "Inbt", 50, -10)
                                $ Line = "embarrassed"
                        
                "I couldn't care less.":
                            call Statup("Laura", "Love", 200, -10)
                            call Statup("Laura", "Obed", 200, 15)
                            call LauraFace("angry")
                            ch_l "I think you're pushing it too far there, [L_Petname]." 
                            $ Line = "rude"
                                        
    if not Line:
        call LauraFace("bemused", 1,Eyes = "down")
        ch_l "So, I'm willing to give this a shot."
        ch_l "Just a trial period, to see how it goes."
        ch_l "Just tell me what you want, and. . . I'll see about doing it."
        menu Laura_Sub_Choice:
            extend ""
            "I think I could get used to that kinda thing.":
                    call Statup("Laura", "Obed", 200, 5)
                    call Statup("Laura", "Inbt", 50, 5)
                    call LauraFace("sly", 1)
                    $ Line = 0
            "Don't you think that relationship's kinda. . .weird?":
                    call LauraFace("sad", 1, Eyes="surprised")         
                    call Statup("Laura", "Love", 200, -5)
                    call Statup("Laura", "Inbt", 50, -15)
                    $ Line = "embarrassed"

    if not Line:
        call LauraFace("smile", 1)
        ch_l "Cool. so is there anything you need. . . sir?"
        menu:
            extend ""
            "That has a nice ring to it.":
                    call Statup("Laura", "Love", 95, 5)
                    call Statup("Laura", "Obed", 200, 15)
                    call Statup("Laura", "Inbt", 50, 5)
                    ch_l "Yes, sir."              
                    $ L_Petname = "sir"
            "That's kind of formal, isn't it?":
                call LauraFace("perplexed", 1)
                ch_l "Huh. ok, no problem"
                call Statup("Laura", "Inbt", 50, -5)
                call LauraFace("sly", 1,Eyes="side")
                menu:
                    ch_l "You'll still give me some orders, right?"
                    "Yeah, no problem.":
                            call Statup("Laura", "Obed", 200, 10)
                            call LauraFace("smile", 1)
                            ch_l "Good."
                    "I don't feel comfortable with that. . .":
                            call LauraFace("sad", 1, Eyes="side")         
                            call Statup("Laura", "Love", 200, -10)
                            call Statup("Laura", "Obed", 200, -30)
                            call Statup("Laura", "Inbt", 50, -15)
                            $Line = "embarrassed"
        
#Laura_Sub_Bad_End:
    $ L_History.append("sir")
    if not Line:
            $ L_Petnames.append("sir")
            #put in stuff that happens if this succeeds
    elif Line == "rude":                       
            call Remove_Girl("Laura")            
            if "Historia" not in P_Traits:
                    $ renpy.pop_call()
            "Laura knocks her way past you and storms off."
    elif Line == "embarrassed":
            call LauraFace("sadside", 2)
            ch_l "Huh, ok, if you're not interested. . .."
            hide Laura_Sprite with easeoutright                    
            call Remove_Girl("Laura")
            if "Historia" not in P_Traits:
                    $ renpy.pop_call()
            "Laura heads out of the room."
    return

label Laura_Sub_Asked:
    $ Line = 0
    call LauraFace("sadside", 1)
    ch_l "Yeah. You didn't seem into the idea."
    menu:
        extend ""
        "Well, I wanted to say I was sorry.  And I was hoping maybe we could give it another shot.":
                if "sir" in L_Petnames and ApprovalCheck("Laura", 850, "O"): 
                        #if this is asking about the "master" name, and her Obedience is higher than 700
                        pass
                elif ApprovalCheck("Laura", 550, "O"): 
                        #if it's instead about earning the "sir" title, and her approval is over 500 
                        pass
                else: #if it failed both those things,    
                        call LauraFace("angry", 1)         
                        ch_l "It was a bad idea, don't worry about it." #Failed again. :(       
                        $ Line = "rude"
                        
                if Line != "rude":    
                        call Statup("Laura", "Love", 90, 10)
                        call LauraFace("sly", 1)
                        ch_l "Well, it's not like you stopped ordering me around anyway." 
                        #Blushing expression.  Laura kisses player and big addition of points
                        ch_l "Ok, let's give it a shot." 

        "I know it's what you want. Do you want to try again, or not?":
                call LauraFace("bemused", 1)
                if "sir" in L_Petnames:
                    if ApprovalCheck("Laura", 850, "O"): 
                        ch_l "Ok, fine."
                    else: 
                        ch_l "Nah, I'm good."
                        $ Line = "rude"
                elif ApprovalCheck("Laura", 600, "O"): 
                        #if it's instead about earning the "sir" title, and her approval is over 500
                        call LauraFace("confused", 1) 
                        ch_l "Kinda wishy-washy there."
                        call LauraFace("sly", 1)         
                        ch_l "but maybe you're right."
                        ch_l "Are you sure you're into this?"
                        menu:
                            extend ""
                            "Yes, I'm sorry I was mean about it.":
                                    call Statup("Laura", "Love", 90, 15)
                                    call Statup("Laura", "Inbt", 50, 10)
                                    call LauraFace("bemused", 1)
                                    $ L_Eyes = "side"
                                    ch_l "Ok then."
                            "You're damned right I am, bitch.":
                                    if "sir" in L_Petnames and ApprovalCheck("Laura", 900, "O"): 
                                            call Statup("Laura", "Love", 200, -5)
                                            call Statup("Laura", "Obed", 200, 10)       
                                            ch_l ". . ."
                                    elif ApprovalCheck("Laura",700, "O"):  
                                            call Statup("Laura", "Love", 200, -5)
                                            call Statup("Laura", "Obed", 200, 10)
                                            ch_l "Hmmm. . ."    
                                    else: #if it failed both those things,     
                                            call Statup("Laura", "Love", 200, -10)
                                            call Statup("Laura", "Obed", 90, -10)
                                            call Statup("Laura", "Obed", 200, -10)
                                            call Statup("Laura", "Inbt", 50, -15)      
                                            call LauraFace("angry", 1)
                                            ch_l "Wow, that's pushing it."    
                                            $ Line = "rude"
                            "Ok, never mind then.":    
                                    call LauraFace("angry", 1)
                                    call Statup("Laura", "Love", 200, -10)
                                    call Statup("Laura", "Obed", 90, -10)
                                    call Statup("Laura", "Obed", 200, -10)
                                    call Statup("Laura", "Inbt", 50, -15)
                                    ch_l "I was thinking of taking orders from you, not mindgames."
                                    ch_l "I should've known you'd be like this."
                                    $ Line = "rude"
    
    $ L_RecentActions.append("asked sub")   
    $ L_DailyActions.append("asked sub")     
    if Line == "rude":            
            #If line hasn't been set to "rude" by something above, then it skips right past this
            hide Laura_Sprite with easeoutright                     
            call Remove_Girl("Laura")
            $ L_RecentActions.append("angry")
            if "Historia" not in P_Traits:
                    $ renpy.pop_call()
            "Laura checks you as she stomps out of the room."
    elif "sir" in L_Petnames:
            #it didn't fail and "sir" was covered
            call Statup("Laura", "Obed", 200, 50)
            $ L_Petnames.append("master")  
            $ L_Petname = "master"
            $ L_Eyes = "sly"
            ch_l ". . . master. . ."
    else:
            #it didn't fail
            call Statup("Laura", "Obed", 200, 30)
            $ L_Petnames.append("sir")  
            $ L_Petname = "sir"
            call LauraFace("sly", 1)
            ch_l ". . . sir."
    return

# end Laura_Sub//////////////////////////////////////////////////////////


# start Laura_Master//////////////////////////////////////////////////////////

label Laura_Master: 
    call Shift_Focus("Laura")
    if L_Loc != bg_current and "Laura" not in Party:
        "Suddenly, Laura shows up and says she needs to talk to you."
    
    $ L_Loc = bg_current
    call Set_The_Scene(0)
    call Display_Laura
    call CleartheRoom("Laura")
    $ L_DailyActions.append("relationship")
    call Taboo_Level
    $ Line = 0
    call LauraFace("sly", 1)
    ch_l "[L_Petname]. . ."
    ch_l ". . . permission to speak freely. . ."
    menu:
        extend ""
        "Granted.":
            call Statup("Laura", "Obed", 200, 5)
            call Statup("Laura", "Inbt", 50, 5)
        "What?":
            ch_l "I was asking if I could talk to you about something. . ."
            $ L_Eyes = "side"
            ch_l ". . . personal."
            $ L_Eyes = "squint"
            menu:
                extend ""
                "Oh, go ahead.":
                    call Statup("Laura", "Love", 80, 5)
                    call Statup("Laura", "Obed", 200, 5)
                    ch_l "Right. . ."
                "Oh, then no.":
                    call LauraFace("sad", 1)
                    call Statup("Laura", "Love", 80, -5)
                    call Statup("Laura", "Obed", 200, -10)
                    $ Line = "embarrassed"                   
        "No.":
            call LauraFace("perplexed", 1,Brows="confused")
            call Statup("Laura", "Love", 80, -5)
            call Statup("Laura", "Obed", 200, -5)
            call Statup("Laura", "Inbt", 50, -5)
            ch_l "- are you sure about that?"
            menu:
                extend ""
                "Oh, go ahead.":
                    call LauraFace("confused", 1)
                    call Statup("Laura", "Obed", 200, 10)
                    call Statup("Laura", "Inbt", 60, 10)
                    ch_l "Right. . ."
                "Yes, not interested.":
                    call LauraFace("sad", 1)
                    call Statup("Laura", "Love", 80, -5)
                    call Statup("Laura", "Inbt", 50, -10)
                    $ Line = "embarrassed"
                    
                    
    if not Line:
        call LauraFace("sly", 1)
        ch_l "I think I enjoy having you in charge."
        ch_l "It gives me. . . structure. . ."
        menu:
            extend ""
            "I like it too.":
                    call LauraFace("sly", 1)
                    call Statup("Laura", "Obed", 200, 5)
                    ch_l "Good. Maybe we could take this a bit more seriously?"
                    menu:
                        extend ""
                        "Nah. This is just about perfect.":
                                call LauraFace("sad", 1)
                                call Statup("Laura", "Obed", 200, -15)
                                call Statup("Laura", "Love", 80, 10)
                                $ Line = "fail"                      
                        "What'd you have in mind?":
                                $ L_Eyes = "side"
                                ch_l "I was thinking I could start calling you. . . {i}master{/i}?"
                                $ L_Eyes = "squint"
                                menu:
                                    extend ""
                                    "Oh, yeah.  I'd like that.":
                                            call Statup("Laura", "Obed", 200, 5)
                                            ch_l "Good. . ."
                                    "Um. . .nah.  That's too much.":
                                            call LauraFace("sadside", 1)
                                            call Statup("Laura", "Obed", 200, -15)
                                            call Statup("Laura", "Inbt", 50, 5)
                                            $ Line = "fail"

                        "Actually, I'd prefer we stopped doing it. Too much pressure.":
                                call LauraFace("sad", 1)
                                call Statup("Laura", "Love", 200, -5)
                                call Statup("Laura", "Obed", 200, -10)
                                call Statup("Laura", "Inbt", 50, 15)
                                $ Line = "fail"
                                
                        "Actually, let's stop that. It's creeping me out.":
                                call LauraFace("angry", 2, Eyes="surprised")
                                call Statup("Laura", "Love", 200, -10)
                                call Statup("Laura", "Obed", 200, -50)
                                call Statup("Laura", "Inbt", 50, -15)
                                ch_l "Say no more, I wouldn't want to CREEP YOU OUT."
                                $ Line = "embarrassed"
                                
            "As if I care what you think, slut.":
                    call LauraFace("angry", 1, Mouth="smile")
                    call Statup("Laura", "Love", 90, -20)
                    call Statup("Laura", "Obed", 200, 10)
                    call Statup("Laura", "Inbt", 50, -10)
                    ch_l ". . ."
                    menu:
                        ch_l "Excuse me?"
                        "Sorry. I just don't care what you want.":
                                if ApprovalCheck("Laura", 1400, "LO"): 
                                        call Statup("Laura", "Obed", 200, 10)
                                        ch_l ". . ." 
                                        call LauraFace("sly", 1)
                                        call Statup("Laura", "Love", 200, 20)
                                        call Statup("Laura", "Inbt", 50, 15)
                                        ch_l ". . .{i}go on. . .{/i}" 
                                else:
                                        call Statup("Laura", "Love", 200, -15)
                                        call Statup("Laura", "Obed", 200, -10)
                                        call Statup("Laura", "Inbt", 50, 5)
                                        call LauraFace("angry", 1)
                                        ch_l "!!!"
                                        $ Line = "rude"

                        "Sorry. I'm just trying to do the \"control\" thing.  I thought you'd like it. Too much?":
                                call Statup("Laura", "Love", 200, 10)
                                call Statup("Laura", "Obed", 200, 10)
                                call Statup("Laura", "Inbt", 50, 5)
                                if ApprovalCheck("Laura", 1400, "LO"): 
                                        call Statup("Laura", "Obed", 200, 10)
                                        ch_l ". . ." 
                                        call LauraFace("sly", 1)
                                        call Statup("Laura", "Love", 200, 20)
                                        call Statup("Laura", "Inbt", 50, 15)
                                        ch_l ". . .{i}no, about right. . .{/i}" 
                                else:
                                        call Statup("Laura", "Love", 200, 5)
                                        call Statup("Laura", "Obed", 200, -5)
                                        call Statup("Laura", "Inbt", 50, 5)
                                        call LauraFace("angry", 1, Eyes="side")
                                        ch_l ". . ."
                                        ch_l "We'll work on it. . ."

            "I don't really like it. Too much pressure.":
                        call LauraFace("sad", 2)
                        call Statup("Laura", "Love", 200, -20)
                        call Statup("Laura", "Obed", 200, -20)
                        call Statup("Laura", "Inbt", 50, -10)
                        $ Line = "embarrassed"
    
    $ L_History.append("master")
    if Line == "rude":
            $ L_RecentActions.append("angry")
            hide Laura_Sprite with easeoutright                    
            call Remove_Girl("Laura")
            if "Historia" not in P_Traits:
                    $ renpy.pop_call()
            "Laura stomps out of the room."
    elif Line == "embarrassed":    
            ch_l "Ok, fine then."
            ch_l "And here I was, about to \"elevate your clearance.\""
            hide Laura_Sprite with easeoutright                   
            call Remove_Girl("Laura")
            if "Historia" not in P_Traits:
                    $ renpy.pop_call()
            "Laura brushes past you on her way out."
    elif Line == "fail":
            ch_l "Oh. . ."
            ch_l "I guess that's fine."
    else:
            call Statup("Laura", "Obed", 200, 50)
            $ L_Petnames.append("master")
            $ L_Petname = "master"
            ch_l ". . .master."
    return

# end Laura_Master//////////////////////////////////////////////////////////

label Gwentro:
        if Taboo > 5 or R_Loc == bg_current or K_Loc == bg_current or E_Loc == bg_current:
            #returns if other girls are present, this is a one on one thing. 
            return
        $ L_History.append("Gwentro")
        $ GwenName = "???"
        ch_g "Where is the exit to this place?!" 
        call GwenFace("angry")
        show Gwen_Sprite at SpriteLoc(1500) zorder 25:
                xzoom -1 
        show Gwen_Sprite at SpriteLoc(100) zorder 25 with easeinright #call Display_Gwen
        pause .1
        call GwenFace("surprised")
        $ Speed = 0
        call LauraFace("surprised",2,Eyes="side")
        show Gwen_Sprite at SpriteLoc(200) zorder 25 with vpunch #call Display_Gwen
        ch_g "Ouch!" 
        call GwenFace("angry")
        ch_g "Ok, that's a wall. . . apparently." 
        call GwenFace("surprised")
        ch_g "Oh, hey you tw-"
        call GwenFace("surprised",1,Mouth="kiss")
        ch_g "Um. . ."
        call GwenFace("shocked",1)
        ch_g "Sorry! My bad, I was just. . ." 
        call LauraFace("confused",2,Eyes="side")
        call GwenFace("surprised",1,Mouth="kiss")
        extend "\n looking for an exit. . ." 
        call GwenFace("smile",1)
        extend "\n but you two. . . seem to be working on something. . ." 
        call GwenFace("sad",1)
        extend "\n and now I can't see because of this stupid word balloon. . ." 
        show Gwen_Sprite:
            ease 1 ypos 150 
        call GwenFace("smile",1)
        extend ""
        ch_g "Better. . ."
        show Gwen_Sprite:
            ease 1 ypos 50 
        ch_g "So now that we've got that taken care of, what's your name?"
        call LauraFace("angry",1,Eyes="side")
        show Gwen_Sprite:
            ypos 50
        ch_g "So now that we've got that taken care of, what's your name?{w=0.2}{nw}"                            
        call GwenFace("shocked",0)
        menu:
            ch_g "So now that we've got that taken care of, what's your name?{nw}"
            "[Playername]":
                pass
            "Zero":
                pass
            "None of your buisiness":
                pass
            "Who are you?":
                pass
        ch_g "Whoa!" with vpunch
        menu:
            ch_g "Whoa!"
            "What?":
                pass                            
        call GwenFace("surprised")
        ch_g "Sorry, it's just that menu popping up caught me by surprise."                            
        call GwenFace("smile")
        ch_g "That's how you talk around here? Menus?"
        menu:
            extend ""
            "Yes?":
                    ch_g "That's ok, no judgement. . ."
                    ch_g "I guess that's not the most important thing at the moment. . ."
            "What are you talking about?":
                    ch_g "The floating blocks from earlier? I guess you can't see those. . ."
                    ch_g "Unless you're roleplaying right now." 
        ch_g "Anyway, back to you, what's your name?"
        menu:
            extend ""
            "[Playername]":
                ch_p "It's [Playername]."
                ch_g "Hi, [Playername], my name's Gwen!"
                $ GwenName = "Gwen"
            "None of your buisiness":
                ch_p "It's none of your business."
                ch_g "Well, it looks like your name is [Playername]."
                ch_g "I could tell from the menu."
                ch_g "Mine's Gwen, b-t-dubs."
            "Who are you?":
                ch_p "Never mind me, who are you?!" 
                ch_g "Oh! That's fair, I'm new around here. My name's Gwen!"
                ch_g "And it looks like your name is [Playername]."
                ch_g "I could tell from the menu."
        if GwenName != "Gwen":
            $ GwenName = "Gwen"
            menu:
                extend ""
                "What menu?!":
                    ch_g "Don't worry about it."                                
                "Riiiight. . .":
                    pass
        ch_g "It is kinda crowded over here though, so if you don't mind. . ."
        show Gwen_Sprite:
            easeout 1 xpos 300 
            xzoom 1
            easein .5 xpos 900 
        ch_g "Ah, yes, room to breathe!"
        call LauraFace("angry",Eyes="leftside")
        ch_g "Sorry, I should have said hello earlier, hey Laura!"
        call LauraFace("confused",Eyes="leftside")
        ch_l "How do you know my name!"
        ch_g "I've read all about you! Or do you prefer \"X-23?\""
        ch_g "Or \"Wolverine?\""                            
        call GwenFace("surprised",Mouth="kiss")
        ch_g "God, it's not \"Talon,\" is it?"                       
        call GwenFace("smile")
        ch_l "[LauraName] - is - fine."                            
        call GwenFace("smile",Mouth="kiss")
        ch_g "Cool, so. . ."
        menu:
            "What are you doing here?":
                ch_p "What are you doing here?" 
                ch_g "I had a feeling you would ask that."
            "Some other irrelvant option.":
                ch_p "What are you doing here?" 
                ch_g "Man, determinism, am I right?"
        call LauraFace("confused",Eyes="leftside")
        ch_g "Why are any of us here, really?"
        ch_g "Oh! You mean \"why am I {i}here{/i}\" in this game?"                            
        call GwenFace("sad")
        ch_g "Honestly? No idea. One minute I had an ongoing, then I was on a team book, guess that's cancelled now?"                            
        call GwenFace("smile")
        ch_g "Yeah, your guess is as good as mine. Maybe whoever made it's a fan?"
        call GwenFace("smile",1)
        ch_g "Judging by what you two have cooking over there, looks like some kind of hentai game."
        ch_g "Well, \"When in Rome. . .\""
        show Gwen_Sprite:
            easeout .2 xpos 890 
            easeout .2 xpos 900 
            pause .5
            easeout .15 xpos 880 
            easeout .15 xpos 910 
            easeout .15 xpos 880 
            easeout .15 xpos 900 
        ch_g "Well, \"When in Rome. . .\"{w=1.8}{nw}"                            
        call GwenFace("angry",1)
        ch_g "Huh."
        ch_g "Apparently I can't get my clothes off here."                            
        call GwenFace("sad",1)
        ch_g "That's unfortunate."                             
        call GwenFace("angry",1,Mouth="smile")
        ch_g "I could just stay and watch for a bit. . ."
        call LauraFace("angry",Eyes="leftside")                            
        call GwenFace("surprised",1)
        ch_l "NO!"
        ch_g "Right, right. Don't poke the wolverine. . ."                            
        call GwenFace("smile",1)
        ch_g "Except you, of course -wink-."       
        call GwenFace("sad",0)
        show Gwen_Sprite:
            ease .5 xpos 950                      
        ch_g "I should probably get going then. . ."
        show Gwen_Sprite:
            ease .5 xpos 1050 
        ch_g "Don't know when I'll be back. . ."
        show Gwen_Sprite:
            ease .5 xpos 1200 
        ch_g "If ever. . ."
        show Gwen_Sprite:
            ease .5 xpos 1000        
        call GwenFace("sad",1,Eyes="surprised")
        ch_g "Maybe never, we won't know."
        show Gwen_Sprite:
            ease .2 xpos 1500                                    
        call GwenFace("surprised")
        ch_l "Get out!"
        ch_g "Right! I'm gone, sorry!"
        hide Gwen_Sprite                        
        call LauraFace("bemused",Eyes="sexy")
        ch_l "Now, what were were doing. . ."
        
        return
                    
#Start Laura new clothes content/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Laura_Dressup:
    #(Condition: X23 has returned to school) 
    #(location: campus square) 
    call Shift_Focus("Laura")
    $ L_Loc = bg_current
    call Set_The_Scene(0)
    show Laura_Sprite at SpriteLoc(L_SpriteLoc) with vpunch
#    call Display_Laura
    call CleartheRoom("Laura")
    $ Round -= 10 if Round >= 11 else Round
    $ L_History.append("dress1")
    "As you're heading across the square, you bump into Laura."
    call AnyFace("Laura","normal") 
    ch_l "Oh, hey."
    menu:
        extend ""
        "Ah, [LauraName]. You're back!":
                call Statup("Laura", "Love", 50, 3)
                call Statup("Laura", "Obed", 50, 1)   
                ch_l "Yeah, just got back."
        "Hey.":
                ch_l "Yeah, just got back."
        "Who are you again?":
                call Statup("Laura", "Love", 70, -3)
                call Statup("Laura", "Obed", 80, 5)  
                call AnyFace("Laura","confused") 
                ch_l "Laura."
                ch_l "We met a while back."
                             
    "She stretches and pops her neck." 
    ch_l "I'll be sticking around for a while this time."
    ch_l "I'll see you around, I could use a hot shower." 
        
    menu:
        extend ""
        "Sure, no problem. See you later!":
                pass
        "Ok, later.":
                pass
        "Want some company?":
                call Statup("Laura", "Love", 70, -1)
                call Statup("Laura", "Obed", 80, 5)  
                call Statup("Laura", "Inbt", 80, 5)  
                call AnyFace("Laura","bemused") 
                ch_l "Not really."
    
    hide Laura_Sprite with easeoutright
    call Remove_Girl("Laura")
    "[LauraName] walks away, and as you watch her go you feel a tap on your shoulder." 
        
    call Shift_Focus("Kitty")
    $ K_Loc = bg_current
    call Set_The_Scene(0)
    call Display_Kitty
    call CleartheRoom("Kitty")
    
    call AnyFace("Kitty","smile") 
    ch_k "Hey, [K_Petname], what're you staring at?" 
    #add Kitty arrving here
    
    menu:
        extend ""
        "Hey, Kitty. I was just talking to [LauraName].":
                ch_k "Oh, she's back?" 
        "Oh, nothing.":
                ch_k "Oh, I see, Laura."
                ch_k "She's back?" 
        "I was checking out that fine piece over there.":
            if ApprovalCheck("Kitty",1200,"LO") or K_Les >= 10: 
                    call Statup("Kitty", "Obed", 80, 5)  
                    call Statup("Kitty", "Inbt", 80, 5)  
                    call AnyFace("Kitty","bemused",1) 
                    ch_k "I guess I can't blame you. . ."
            else:
                    call Statup("Kitty", "Love", 70, -5)
                    call Statup("Kitty", "Obed", 80, 10)  
                    call Statup("Kitty", "Inbt", 80, 5)  
                    call AnyFace("Kitty","angry") 
                    ch_k "Rude much?"
                
    call AnyFace("Kitty","smile",Eyes="side") 
    ch_k "She's never around very much, you know."
    ch_k "Must get it from Logan."
    
    menu:
        extend ""
        "Oh, they're related?":
                ch_k "Yeah, she's his daughter or something? I'm not too sure."
        "She's his clone, right?":
                ch_k "I guess? I'm not too sure."                 
    "She shrugs, but then grins mischieviously." 
              
    call AnyFace("Kitty","sly")                                      
    ch_k "Actually, we were thinking of giving her a \"welcome home\" present."     
    ch_k "You wanna chip in?" 
    
    menu:
        extend ""
        "Sure, why not?":
                call Statup("Kitty", "Love", 50, 5)
                call Statup("Kitty", "Obed", 40, 5)  
                ch_p "Here you go. What're you planning to get her?" 
        "Nah, I don't really know her.":
                ch_k "Yeah, maybe you've got a point. She's kinda prickly sometimes." 
                return
        "That could be kind creepy.": 
                ch_k "Yeah, maybe you've got a point. She's kinda prickly sometimes." 
                return
    
    #"Kitty grins."
    ch_k "Well, she doesn't really have much of a wardrobe, so we were going to get her some new clothes."
    
    menu:
        extend ""
        "You're really stylish, so you'll probably pick out something great.":
                call Statup("Kitty", "Love", 80, 5)  
                call Statup("Kitty", "Inbt", 40, 3)  
                call AnyFace("Kitty","smile",1)  
                ch_k "Sweet talker."
        "That sounds good.":
                call Statup("Kitty", "Love", 60, 2)
        "With your fashion sense? That'll end well.": 
                call Statup("Kitty", "Love", 70, -5)
                call Statup("Kitty", "Obed", 80, 5)  
                call Statup("Kitty", "Inbt", 80, -3)  
                call AnyFace("Kitty","angry")  
    ch_k "Anyway, we were thinking around $10 each."
    
    menu:
        extend ""
        "Here you go." if P_Cash >= 10:
                call Statup("Kitty", "Love", 70, 1) 
                call Statup("Kitty", "Obed", 40, 2)   
                ch_k "Nice."
                $ P_Cash -= 10
                $ L_History.append("dress2")
        "I don't have enough. . ." if P_Cash < 10:
                call Statup("Kitty", "Love", 70, 1) 
                call Statup("Kitty", "Obed", 40, 2) 
                call AnyFace("Kitty","normal",1,Brows="surprised",Mouth="sad")  
                ch_k "Oh."
                ch_k "We aren't in a rush or anything. If you still want to, just hit me up." 
        "You know what, never mind.": 
                call Statup("Kitty", "Love", 70, -2)
                call Statup("Kitty", "Obed", 40, -1)   
                call AnyFace("Kitty","normal",1,Brows="surprised",Mouth="sad") 
                ch_k "Oh, ok." 
    
    return
   
label Laura_Dressup2:
    #plays if you blew Kitty off earlier. State should be "dress1"
    ch_p "Hey, remember that gift you wanted to give Laura earlier?"
    call AnyFace("Kitty","smile")  
    ch_k "Yeah?" 
    menu:
        extend ""
        "Here you go, $10.":
                call Statup("Kitty", "Love", 70, 1) 
                call Statup("Kitty", "Obed", 40, 2) 
                ch_k "Cool."
                $ L_History.append("dress2")
        "Never mind.":
                ch_k "Oh, ok."    
    return  

    
label Laura_Dressup3:
    #(Condition: Laura_Dressup has already played), State should be "dress2"
    #(location: Kitty's room door)
    $ L_History.remove("dress1")
    $ L_History.remove("dress2")
    $ L_History.append("dress3")
    $ L_Inventory.append("wolvie top")
    $ L_Inventory.append("wolvie panties")

    "You're walking past Kitty's door when you hear her laughing at something."
    "You hear someone else's voice, there's clearly someone else in her room with her."
    
    ch_l "Kitty, you shouldn't have."
    ch_l "No, seriously. . ."
    ch_l "you shouldn't have."
    ch_k "Aww, c'mon. You look great."

    "You remember Kitty talking about getting Laura some new clothes. She must've gotten Laura to try them on."
    "You can't help but feel curious..."
    
    call AnyOutfit("Laura","nude")
    $ L_Chest = "wolvie top"
    $ L_Panties = "wolvie panties"
    menu:
        extend ""
        "Sneak a peek [[no key] (locked)" if "Kitty" not in Keys:
                pass
        "Sneak a peek" if "Kitty" in Keys:
                "You use your key and unlock the door, opening it and sticking your head in."
                ch_p "Hey, Kitty, what's going on?"
                ch_k "Hey, [K_Petname]! Come on in!"
                
                call CleartheRoom("All",0,1)
                call Shift_Focus("Laura")
                $ K_Loc = "bg kitty"
                $ L_Loc = "bg kitty"
                call Set_The_Scene(Dress=0)
                
                call AnyFace("Laura","sad",2,Eyes="squint",Brows="confused")  
                "Laura stares at you, her eyes narrowed. She's clearly on edge."
                call AnyFace("Laura","sad",2,Brows="confused",Eyes="leftside")  
                ch_l "Didn't you lock the door?"
                call AnyFace("Kitty","smile",Eyes="side")  
                ch_k "Yeah, but I gave him a key."
                call AnyFace("Laura","sad",1,Brows="confused",Eyes="leftside")  
                ch_l "You... gave him a key?"
                call AnyFace("Kitty","smile",1)  
                ch_k "Uh-huh. I mean, he's my [K_Petname]."
                ch_l "Your... [K_Petname]."    
        "Knock":
                "You knock on the door."
                ch_k "Who is it?"
                ch_p "It's [Playername], mind if I come in?"
                if not ApprovalCheck("Kitty", 1000):
                        ch_k "Um, sorry [K_Petname], we're a little busy in here."
                        ch_k "[K_Like]maybe check back later?"
                        ch_p "Sure, no problem."
                        "You head back out."
                        return
                ch_k "Sure, [K_Petname]! Gimme a sec!"
                "Kitty unlocks the door and it swings open."
                
                call CleartheRoom("All",0,1)
                call Shift_Focus("Laura")
                $ K_Loc = "bg kitty"
                $ L_Loc = "bg kitty"
                call Set_The_Scene(Dress=0)
    
                call AnyFace("Laura","sad",2,Brows="surprised")  
                "Laura stares at you, as if she's not sure what she's seeing."
                call AnyFace("Laura","sad",2,Brows="confused",Eyes="leftside")  
                ch_l "So you just let him come into your room whenever?"
    
        "Walk away":
            "Nah, I should let them have their girl time."
            return
    $ L_SeenPanties = 1            
    call AnyFace("Laura","angry",1,Eyes="closed")  
    "She shakes her head, trying to absorb all this new information."
    "She mutters to herself."
    ch_l "I've been gone longer than I thought..."
    call AnyFace("Laura","sad",1,Brows="confused",Eyes="leftside")  
    ch_l "So why's he here?"
    call AnyFace("Kitty","smile",Eyes="side")  
    ch_k "Well, he kind of pitched in to get you this stuff, so why not see what he thinks?"
    "Kitty walks over and poses like she's presenting X23 as a model."
    $ Kitty_Arms = 2
    call AnyFace("Kitty","smile")  
    ch_k "So, what do you think?"

    menu:
        extend ""
        "Her outfit looks familiar...":
                ch_k "I call it the Logan Look."
                call AnyFace("Laura","sad",2,Eyes="stunned")    
                call Statup("Laura", "Inbt", 40, -2)
                ch_l "Please don't call it that."
        "Looking good, [LauraName]!":           
                call Statup("Laura", "Love", 70, 5) 
                call Statup("Laura", "Obed", 40, 3) 
                call Statup("Laura", "Inbt", 40, 5)  
                call GirlLikesGirl("Laura","Kitty",700,5,1)
                call AnyFace("Laura","sadside",1)             
                ch_l "Yeah, well. . . Kitty knows her stuff." 
                call Statup("Kitty", "Love", 70, 1) 
                call Statup("Kitty", "Obed", 40, 3) 
                call GirlLikesGirl("Kitty","Laura",700,3,1)
                ch_k "Heh, thanks."
        "Great ensemble, Kitty! It looks great on her!":
                call Statup("Kitty", "Love", 70, 5) 
                call Statup("Kitty", "Obed", 40, 3)  
                ch_k "Hey, I know my stuff, y'know?"  
                call Statup("Laura", "Love", 70, 3) 
                call Statup("Laura", "Obed", 40, 2) 
                call Statup("Laura", "Inbt", 40, 5) 
                call AnyFace("Laura","bemused",1)   
                call GirlLikesGirl("Laura","Kitty",700,3,1)       
                ch_l "Yeah, I guess she does. . ."
        "Can I get a refund?":
                call Statup("Kitty", "Love", 70, -5) 
                call Statup("Kitty", "Obed", 40, -3)  
                call AnyFace("Kitty","angry")    
                ch_k "Way to bring down the mood."
                call Statup("Laura", "Love", 70, -5) 
                call Statup("Laura", "Obed", 40, 5) 
                call Statup("Laura", "Inbt", 40, -5) 
                call AnyFace("Laura","angry")     
                ch_l "Seriously."

    call AnyFace("Laura","smile",Eyes="leftside",0)  
    call GirlLikesGirl("Laura","Kitty",700,5,1)  
    call GirlLikesGirl("Kitty","Laura",700,5,1)  
    ch_l "But really, Kitty, thanks for this."
    call AnyFace("Kitty","smile",Eyes="side") 
    ch_k "No problem! Like, what're friends for?"
    ch_l "Pretty sure friends don't normally use their friends as dressup dolls."
    ch_k "Oh, Laura, you have sooooo much to learn."

    call AnyFace("Laura","smile",Eyes="down")  
    "Laura smiles just a little bit and looks down at herself."
    ch_l "I think wearing the whole outfit is a bit much."
    call AnyFace("Laura","smile",Eyes="leftside")  
    ch_l "You know that Logan's going to have a few words if he sees me like this."
    call AnyFace("Kitty","smile",Eyes="side") 
    ch_k "Hey, it's your outfit now. Mix-and-match, girl!"
    ch_l "Yeah. Yeah, I think I'll do that."
    
    call AnyFace("Kitty","smile") 
    call AnyFace("Laura","sly",1)  
    "Laura fixes you with a steely gaze."

    ch_l "So. . . I'd like to change now."

    menu:
        extend ""
        "Go right ahead!":
                call Statup("Laura", "Obed", 40, 3) 
                call Statup("Laura", "Inbt", 40, 3) 
                if (not L_SeenChest or not L_SeenPussy) and not ApprovalCheck("Laura",1400):
                        call Statup("Laura", "Love", 70, -5) 
                        call AnyFace("Laura","angry",1)  
                        ch_l "I don't think so."
                        ch_k "Yeah, I think you'd better get going, [K_Petname]. . ." 
                        ch_k ". . .Before she does to you what Logan does to people who make him mad."
                        "Kitty firmly escorts you to the door."
                else:
                    if L_SeenChest and L_SeenPussy:
                        ch_l "Fair enough. . ."
                    elif ApprovalCheck("Laura",1400):
                        ch_l "Bold choice. . ."
                    call AnyFace("Kitty","surprised",2,Eyes="side")  
                    $ L_Chest = 0
                    "Laura starts stripping out of the new clothes. . ."
                    if ApprovalCheck("Kitty",1200):
                        call AnyFace("Kitty","sly",1)  
                    else:
                        call AnyFace("Kitty","angry",1,Eyes="side")  
                        
                    $ L_Panties = 0
                    call Laura_First_Topless
                    call Laura_First_Bottomless(1)
                    pause 1
                    call AnyOutfit("Laura",L_OutfitDay,Changed=1)
                    "And then puts on her usual outfit."
                    
                    if ApprovalCheck("Kitty",1200):
                        call AnyFace("Kitty","sly",1)  
                    else:
                        call AnyFace("Kitty","angry",1)  
                    ch_k "Well, I guess you got your show for the day."
                    ch_k "Now give us some girl time."
                    "Kitty shoos you out of the room and you head to the Campus square."
                    
        "Message received. See you girls later!":
                ch_k "Later, [K_Petname]!"
                ch_l "See ya."
    
    $ Round -= 20 if Round >= 21 else Round
    return
    #End scene
#End Laura new clothes content/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
