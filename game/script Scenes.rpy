label Sleepover(Line = 0,BO=[]):
            # This event gets called from Round10
            # If there's a Lead, she's been sent to this from elsewhere
            # Sleep tracks number of previous sleepovers

            $ Party = []
            
            $ BO = TotalGirls[:]                
            while BO:                     
                    if BO[0].Loc == bg_current:
                            $ Party.append(BO[0])
                    $ BO.remove(BO[0])
                    
            if not Party and bg_current == "bg player":
                    #if nobody is around.
                    call CleartheRoom("All",1)
                    #if nobody is here, you just go to sleep
                    "It's getting late, so you go to sleep."
                    call Wait
                    return    
                      
            while len(Party) > 2:  
                    #culls out extra members
                    $ Party.remove(Party[2])
                            
            if Day <= 7:
                    # prevents anyone agreeing before day 7.
                    $ Party = [0]   
            elif Party and Party[0]:            
                    call Shift_Focus(Party[0])
            
            if bg_current != "bg player":
                    #if this isn't your room, sets "room" to the name of the room's owner
                    $ BO = TotalGirls[:]                
                    while BO:                     
                            if BO[0].Home == bg_current:
                                    if BO[0] not in Party:
                                            #either another girl is around
                                            "[BO[0].Name] probably wouldn't appreciate you staying over, you head back to your own room."
                                            call Remove_Girl("All")
                                            jump Return_Player
                                    if BO[0] != Party[0]:
                                            $ Party.reverse() #makes sure the room's owner is first
                                    $ BO = [1]
                            $ BO.remove(BO[0])
                                                    
            # the previous statement should cull out all situations where the owner isn't there
            if bg_current == "bg player":
                    if len(Party) == 2:                    
                        $ renpy.random.shuffle(Party)
                        if ApprovalCheck(Party[0],Check=1) <= ApprovalCheck(Party[1],Check=1):
                            # If second one likes you more, pick her
                            $ Party.reverse()   
                    if Party[0] == RogueX:
                        ch_r "It's getting late and I'm getting a bit tired."  
                    elif Party[0] == KittyX: 
                        ch_k "It's late, I'm thinking of heading out. . ."
                    elif Party[0] == EmmaX:            
                        ch_e "It's late, I should be going. . ."  
                    elif Party[0] == LauraX:            
                        ch_l "I need some sleep. . ." 
            elif bg_current == Party[0].Home:
                    if Party[0] == RogueX:#Room == RogueX.Name:
                            ch_r "It's getting late and I'm turning in."
                    elif Party[0] == KittyX:
                            ch_k "I'm getting kinda tired. . ."
                    elif Party[0] == EmmaX:
                            ch_e "It's getting late, [EmmaX.Petname]. . ."
                    elif Party[0] == LauraX:
                            ch_l "I'm tired. . ."
            else:
                "Something went wrong." 
                "Tell Oni \"[Party] - [bg_current]\""
                    
            
            if Day <= 7:
                    # If it's too early for sleepovers, 
                    jump Return_Player               
                
            if EmmaX in Party:                      
                    if "classcaught" not in EmmaX.History:
                            if bg_current == EmmaX.Home:
                                    ch_e "You should probably get going, we wouldn't want any rumors to spread."
                                    jump Return_Player
                            else:
                                    ch_e "I should probably get going, we wouldn't want any rumors to spread." 
                                    call Remove_Girl(EmmaX)   
                    elif len(Party) >= 2 and "three" not in EmmaX.History:
                            #if Emma's around but can't do threesome stuff yet
                            if (bg_current == EmmaX.Home or bg_current == "bg player") and ApprovalCheck(EmmaX, 1100, "LI"):
                                if Party[0] != EmmaX:
                                        $ Party.reverse() 
                                ch_e "[Party[1].Name] dear, I need a moment with [Player.Name], but you can leave." 
                                $ Party[1].FaceChange("confused",1)                           
                                call AnyLine(Party[1],"Oh, ok. . .")                            
                                call Remove_Girl(Party[1])
                                ch_e "Sorry about that, but I had to discuss something with you in private."
                            else:
                                #if it's not her room, or she doesn't like you enough to stay
                                ch_e "Yes, I really should be leaving, don't let me bother you two."                        
                                call Remove_Girl(EmmaX)
                            if "sleeptime" not in EmmaX.History:
                                $ EmmaX.History.append("sleeptime")                        
                    if not Party or (EmmaX not in Party and bg_current == EmmaX.Home):
                                #if Emma leaves
                                jump Return_Player
                                                
            $ Party[0].FaceChange("sexy",1)
            
            $ Line = 0
            if Party[0].Sleep >= 3 and ApprovalCheck(Party[0], 800):                                 
                    #You've slept over several times and she still likes you
                    if Party[0].Home == bg_current:
                            call AnyLine(Party[0],"Are you staying over tonight?")
                    else:
                            call AnyLine(Party[0],"I'm staying over, right?")
                    $ Line = 1
                
            elif Party[0].Sleep < 3 and ApprovalCheck(Party[0], 1100, "LI"):                        
                    #You haven't slept over much, but she wants you to
                    $ Party[0].FaceChange("bemused",1)
                    if Party[0] == RogueX:
                            if bg_current == Party[0].Home:
                                ch_r "I was thinking. . . maybe you wanted to stay the night?"  
                            else:
                                ch_r "I was thinking. . . maybe I could stay the night?" 
                    elif Party[0] == KittyX:
                            if bg_current == Party[0].Home:
                                ch_k "So[KittyX.like]did you want to stay over?"  
                            else:
                                ch_k "So[KittyX.like]could I stay over?"
                    elif Party[0] == EmmaX:
                            if bg_current == Party[0].Home:
                                ch_e "I was wondering, have you considered staying over?"  
                            else:
                                ch_e "I was wondering, could I stay over?" 
                    elif Party[0] == LauraX:
                            if bg_current == Party[0].Home:
                                ch_l "So, are you staying over?"  
                            else:
                                ch_l "So, can I stay here tonight?" 
                    $ Line = 1
                    
            else: #If she's uninterested                
                    if Party[0] == RogueX:
                            if bg_current == Party[0].Home:
                                ch_r "You should get going." 
                            else:
                                ch_r "I'm heading out, see you tomorrow."
                    elif Party[0] == KittyX:
                            if bg_current == Party[0].Home:
                                ch_k "You should[KittyX.like]head out." 
                            else:
                                ch_k "See ya tomorrow, [KittyX.Petname]."
                    elif Party[0] == EmmaX:
                            if bg_current == Party[0].Home:
                                ch_e "Could you please clear the room?"
                            else:
                                ch_e "I should leave." 
                    elif Party[0] == LauraX:
                            if bg_current == Party[0].Home:
                                ch_l "Clear out."
                            else:
                                ch_l "So, later." 
            
            if Line:
                    #she offered to sleep over
                    menu:
                        extend ""
                        "Sure.":
                                if Party[0].Sleep <= 5:
                                        $ Party[0].Statup("Love", 70, 10)
                                        $ Party[0].Statup("Obed", 80, 10)
                                        $ Party[0].Statup("Obed", 50, 20)
                                        $ Party[0].Statup("Inbt", 25, 20)              
                                $ Party[0].Statup("Love", 70, 5) 
                                $ Party[0].FaceChange("smile")
                                # Line = 1
                            
                        "No, sorry.":                  
                                $ Party[0].Statup("Obed", 50, 2)
                                $ Party[0].Statup("Obed", 30, 5)
                                $ Party[0].Statup("Inbt", 40, 3) 
                                $ Party[0].FaceChange("sad")
                                $ Line = 0
                                if Party[0] == RogueX:
                                        ch_r "Ok, see you tomorrow then. 'Night."                
                                elif Party[0] == KittyX:
                                        ch_k "Alright. . . see you tomorrow. . ."
                                elif Party[0] == EmmaX:
                                        ch_e "Well, if you insist. See you tomorrow then."
                                elif Party[0] == LauraX:
                                        ch_l "Ok."  
            else:
                    #if she didn't offer to sleep over
                    menu: 
                        extend ""
                        "Ok, I'll head out. Good night." if Party[0].Home == bg_current:    
                                #if she didn't agree and this is her room
                                $ Line = "leave"
                        "Ok, see you later then. Good night." if Party[0].Home != bg_current:     
                                #if she didn't agree and this is not her room    
                                $ Line = "leave"   
                            
                        "Are you sure I can't stay the night? . ." if not Party[0].Sleep and Party[0].Home == bg_current: 
                                $ Line = "please"   
                        "Are you sure you can't stay? . ." if not Party[0].Sleep and Party[0].Home != bg_current: 
                                $ Line = "please"   
                                    
                        "That's not what you said the other night . ." if Party[0].Sleep: 
                                #if she wants you gone  
                                if ApprovalCheck(Party[0],900)or ApprovalCheck(Party[0],700,"L") or ApprovalCheck(Party[0],500,"O"):
                                    $ Party[0].FaceChange("bemused",1)  
                                    $ Line = 1       
                                    if Party[0] == RogueX:
                                            ch_r "Well. . . that didn't turn out so bad, I suppose. . ."              
                                    elif Party[0] == KittyX:      
                                            ch_k "and that went pretty well. . ."
                                    elif Party[0] == EmmaX:
                                            ch_e "It was a nice evening."
                                    elif Party[0] == LauraX:
                                            ch_l "Yeah, it was."   
                                else:                    
                                    $ Party[0].FaceChange("smile",Brows="confused")
                                    # Line = 0
                                    if Party[0] == RogueX:
                                            ch_r "I'm afraid not this time, [RogueX.Petname]. I'll see you later."               
                                    elif Party[0] == KittyX:
                                            ch_k "Um, no, 'fraid not. I'll see ya tomorrow." 
                                    elif Party[0] == EmmaX:
                                            ch_e "Well, not tonight, [EmmaX.Petname]."
                                    elif Party[0] == LauraX:
                                            ch_l "Yeah, but not this time."  
                                    if bg_current != "bg player":
                                            #if it's a girl's room, you leave.
                                            ch_p "Ok, I'll be going then."   
                    #if she didn't offer to sleep over
        
            if Line == "leave":           
                    # if you agreed to leave
                    $ Party[0].Statup("Love", 90, 3)
                    $ Party[0].Statup("Inbt", 25, 2)    
                    $ Party[0].FaceChange("smile") 
                    $ Line = 0 
                    if Party[0] == RogueX:
                            ch_r "Yeah, good night, [RogueX.Petname]. . ."                
                    elif Party[0] == KittyX:
                            ch_k "Yeah, 'night, [KittyX.Petname]. . ."
                    elif Party[0] == EmmaX:
                            ch_e "Yes, good night, [EmmaX.Petname]."
                    elif Party[0] == LauraX:
                            ch_l "Ok, good night then."
                        
            if Line == "please": 
                    #if she said no but you asked nicely
                    if ApprovalCheck(Party[0],1000) or ApprovalCheck(Party[0],700,"L") or ApprovalCheck(Party[0],500,"O"):
                        $ Party[0].FaceChange("bemused") 
                        $ Line = 1 
                        if Party[0] == RogueX:
                                ch_r "Well. . . I suppose it would be alright."                
                        elif Party[0] == KittyX:
                                ch_k "Well, Maaaybeee. . ."
                        elif Party[0] == EmmaX:
                                ch_e "I suppose we could make an exception. . ."
                        elif Party[0] == LauraX:
                                ch_l "Suit yourself."                    
                    else:                    
                        $ Party[0].FaceChange("smile",Brows="confused")
                        $ Line = 0
                        if Party[0] == RogueX:
                                ch_r "I'm afraid not, [RogueX.Petname]. Head home, I'll see you later."               
                        elif Party[0] == KittyX:
                                ch_k "Ehhhh. . . no, not tonight, [KittyX.Petname]. Sorry." 
                        elif Party[0] == EmmaX:
                                ch_e "I'm afraid not."
                        elif Party[0] == LauraX:
                                ch_l "Don't push it."

            if not Line:
                    #if the primary girl refused to sleep over
                    if Party[0].Home == bg_current:
                            #if it's her room, removes any other girls around
                            call CleartheRoom(Party[0],1)    
                            jump Return_Player                        
                    else:   
                            #if it's not her room, remove her, and try again
                            call Remove_Girl(Party[0])
                            call Sleepover
                            return
                      
            #If the primary girl agreed  
            if len(Party) >= 2:
                #if there is another girl
                if Party[0].GirlLikeCheck(Party[1]) >= 700 and ApprovalCheck(Party[0], 1200):
                        # If she likes the other girl quite a bit and likes you a decent amount
                        if Party[0] == RogueX:
                                ch_r "And you, [Party[1].Name]?"                   
                        elif Party[0] == KittyX:
                                ch_k "How about you, [Party[1].Name]?"
                        elif Party[0] == EmmaX:
                                ch_e "And what about you, [Party[1].Name]?"
                        elif Party[0] == LauraX:
                                ch_l "And you, [Party[1].Name]?"
                else:
                        if Party[0] == RogueX:
                                ch_r "Are you leaving, [Party[1].Name]?"                   
                        elif Party[0] == KittyX:
                                ch_k "You heading out, [Party[1].Name]?"
                        elif Party[0] == EmmaX:
                                ch_e "I assume you're leaving, [Party[1].Name]?"
                        elif Party[0] == LauraX:
                                ch_l "Later, [Party[1].Name]."
                                
                if Party[1].GirlLikeCheck(Party[0]) >= 500 and ApprovalCheck(Party[1], 1200):
                        # If second girl likes the other girl a bit and likes you a decent amount  
                        $ Party[1].FaceChange("smile") 
                        if Party[1] == RogueX:
                                ch_r "I'd like to stay too."                   
                        elif Party[1] == KittyX:
                                ch_k "Can I stay too?"
                        elif Party[1] == EmmaX:
                                ch_e "I'd rather join the fun."
                        elif Party[1] == LauraX:
                                ch_l "Me too, right?"
                        $ Line = 1
                else:  
                        $ Party[0].FaceChange("smile",1) 
                        if Party[1] == RogueX:
                                ch_r "I guess I should be going."                   
                        elif Party[1] == KittyX:
                                ch_k "I should go, right?"
                        elif Party[1] == EmmaX:
                                ch_e "I suppose three is a crowd."
                        elif Party[1] == LauraX:
                                ch_l "I should leave."
                        $ Line = 0
                menu:
                    extend ""
                    "You should stay, [Party[1].Name].":
                            #this checks the second girl's response.
                            if Party[1].GirlLikeCheck(Party[0]) >= 500 and ApprovalCheck(Party[1], 1200):
                                    # If second girl likes the first girl a bit and likes you a decent amount
                                    if Party[1] == RogueX:
                                            ch_r "Oh, I'd love to."                   
                                    elif Party[1] == KittyX:
                                            ch_k "Roomies!"
                                    elif Party[1] == EmmaX:
                                            ch_e "I'd love to."
                                    elif Party[1] == LauraX:
                                            ch_l "Great."
                                    $ Line = 1
                                    $ Party[0].GLG(Party[1],800,3,1)
                            else:  
                                    $ Party[1].FaceChange("sadside",1,Mouth="smile") 
                                    if Party[1] == RogueX:
                                            ch_r "I don't want to be a bother."                   
                                    elif Party[1] == KittyX:
                                            ch_k "No way."
                                    elif Party[1] == EmmaX:
                                            ch_e "I couldn't."
                                    elif Party[1] == LauraX:
                                            ch_l "Nah."
                                    $ Line = 0
                                    $ Party[0].GLG(Party[1],700,-5,1)
                            
                            #This checks the first girl's response
                            if Line:
                                if Party[0].GirlLikeCheck(Party[1]) >= 700 and ApprovalCheck(Party[0], 1200):
                                    # If first girl likes the other girl quite a bit and likes you a decent amount
                                    if Party[0] == RogueX:
                                            ch_r "Great!"                   
                                    elif Party[0] == KittyX:
                                            ch_k "Roomies!"
                                    elif Party[0] == EmmaX:
                                            ch_e "Lovely."
                                    elif Party[0] == LauraX:
                                            ch_l "Ok."  
                                    $ Party[1].GLG(Party[0],800,5,1)
                                elif Party[0].GirlLikeCheck(Party[1]) >= 400 and ApprovalCheck(Party[0], 1400):
                                    # If she barely likes the other girl but likes you a a lot
                                    $ Party[0].FaceChange("sadside",1,Mouth="smile") 
                                    if Party[0] == RogueX:
                                            ch_r "Sure, I guess."                   
                                    elif Party[0] == KittyX:
                                            ch_k "Um, Ok."
                                    elif Party[0] == EmmaX:
                                            ch_e "I suppose we could find room for one more."
                                    elif Party[0] == LauraX:
                                            ch_l "Whatever."
                                else:
                                    $ Party[0].FaceChange("angry",1) 
                                    if Party[0] == RogueX:
                                            ch_r "I'm not cool with that."                   
                                    elif Party[0] == KittyX:
                                            ch_k "No way."
                                    elif Party[0] == EmmaX:
                                            ch_e "I don't think so."
                                    elif Party[0] == LauraX:
                                            ch_l "Um, no."
                                    $ Party[0].GLG(Party[1],700,-5,1)
                                    $ Party[1].GLG(Party[0],700,-5,1)
                                    $ Line = 0
                    
                    "You should get going, [Party[1].Name].":
                            if Party[1] == RogueX:
                                    ch_r "Oh, ok."                   
                            elif Party[1] == KittyX:
                                    ch_k "Yeah."
                            elif Party[1] == EmmaX:
                                    ch_e "I assumed."
                            elif Party[1] == LauraX:
                                    ch_l "Yeah."
                            $ Line = 0
                            
            if Line == 0:
                    #if the second girl got the boot:
                    if len(Party) >= 2:
                        if Party[0] == RogueX:
                                ch_r "Later, [Party[1].Name]."                   
                        elif Party[0] == KittyX:
                                ch_k "Night, [Party[1].Name]." 
                        elif Party[0] == EmmaX:
                                ch_e "Goodnight, [Party[1].Name]." 
                        elif Party[0] == LauraX:
                                ch_l "Night." 
                            
                        if Party[1] == RogueX:
                                ch_r "Later guys."                   
                        elif Party[1] == KittyX:
                                ch_k "Night." 
                        elif Party[1] == EmmaX:
                                ch_e "Goodnight." 
                        elif Party[1] == LauraX:
                                ch_l "Night." 
                    if Party:        
                        call CleartheRoom(Party[0],1,1) #removes any other girls around   
            
            if not Party:                
                    #if nobody is around.
                    if bg_current != "bg player":
                            jump Return_Player
                    call CleartheRoom("All",1)
                    #if nobody is here, you just go to sleep
                    "It's getting late, so you go to sleep."
                    call Wait
                    return  
                    
            if bg_current != "bg player" and bg_current != Party[0].Home:
                    #if the room's owner left you in her room. . .
                    "You probably shouldn't sleep here, you head back to your own room."
                    call Remove_Girl("All")
                    $ renpy.pop_call()
                    jump Player_Room
                    
            jump Sleepover_Morning

  
label Return_Player:    
        # This label is jumped to by the Sleep labels if the player or girl leaves after a sleepover (fail state).
        $ del Party[:]                
        $ BO = TotalGirls[:]   
        $ renpy.random.shuffle(BO)
        while BO:                              
                if bg_current != BO[0].Home and BO[0].Loc == bg_current:
                        "[BO[0].Name] heads out."        
                        $ BO[0].Loc = BO[0].Home
                $ BO.remove(BO[0])
        if bg_current != "bg player":
                "You head back to your room."
        $ bg_current = "bg player"
        jump Misplaced
#        call Set_The_Scene
#        $ renpy.pop_call()
#        jump Player_Room
          
label Sleepover_Morning:
        #This label is jumped too from Sleepover if you successfully stay the night               
        $ BO = TotalGirls[:]                
        while BO:                     
                if BO[0].Loc == bg_current and BO[0] not in Party:
                        call Remove_Girl(BO[0])
                $ BO.remove(BO[0])
                    
        call Shift_Focus(Party[0])            
        $ Party[0].OutfitChange("sleep")
        if len(Party) >= 2:
                #If there are two girls. . .       
                $ Party[1].OutfitChange("sleep")
                "The girls change into their sleepwear."
        else:        
                "[Party[0].Name] changes into her sleepwear."
        
        if Party[0] == RogueX:
                ch_r "Hmm, that's a bit more comfortable."
        elif Party[0] == KittyX:
                ch_k "Ah, that's better."
        elif Party[0] == EmmaX:
                ch_e "Mmmm, that's better." 
        elif Party[0] == LauraX:
                ch_l ". . ."
        $ Party[0].Traits.append("sleepover") #this is temporary, removed in the morning
                
        if len(Party) >= 2:
                if Party[1] == RogueX:
                        ch_r "Let's turn in."                   
                elif Party[1] == KittyX:
                        ch_k "Night, [KittyX.Petname]"    
                elif Party[1] == EmmaX:
                        ch_e "Lights out."     
                elif Party[1] == LauraX:
                        ch_l "Night."
                $ Party[1].Traits.append("sleepover") #this is temporary, removed in the morning  
        else:
                if Party[0] == RogueX:
                        ch_r "Let's turn in."                    
                elif Party[0] == KittyX:
                        ch_k "Night, [KittyX.Petname]"
                elif Party[0] == EmmaX:
                        ch_e "Goodnight." 
                elif Party[0] == LauraX:
                        ch_l "Night."
            
        show blackscreen onlayer black    
        pause 1
        call Wait(0,0) #shouldn't change outfit or lighting 
        $ Party = []
        
        $ BO = TotalGirls[:]                
        while BO:                     
                if "sleepover" in BO[0].Traits:
                        $ Party.append(BO[0])    
                        $ BO[0].Loc = bg_current
                        $ BO[0].Outfit = "sleep"
                        $ BO[0].OutfitChange()
                elif BO[0].Loc == bg_current:
                        call Remove_Girl(BO[0])
                $ BO.remove(BO[0])
                             
        call Morningwood_Check
                                
        $ Party[0].FaceChange("smile")
        if len(Party) >= 2:
                $ Party[1].FaceChange("smile")
        hide NightMask onlayer nightmask  
        hide blackscreen onlayer black
        
        if "morningwood" in Player.DailyActions:
                #if you got some
                if Party[0] == RogueX:
                        ch_r "So, that aside, Sleep well?"             
                elif Party[0] == KittyX:
                        ch_k "So anyway. . . G'morning . . ."
                elif Party[0] == EmmaX:
                        ch_e "Now that we've got that out of our system. . ."
                        ch_e "Morning, [EmmaX.Petname]."
                elif Party[0] == LauraX:
                        ch_l "Anyway, 'Morning."
        else:
                if Party[0] == RogueX:
                        ch_r "'Morning [RogueX.Petname]. Sleep well?"             
                elif Party[0] == KittyX:
                        ch_k "G'morning . . ."
                elif Party[0] == EmmaX:
                        ch_e "Hrmph. . ."
                        ch_e "Oh. You're here."
                elif Party[0] == LauraX:
                        ch_l "'Morning."     
                
        menu:
            extend ""
            "It's always nice sleeping with you." if Party[0].Sleep: 
                    if Party[0].Sleep < 5:
                            $ Party[0].Statup("Love", 90, 8)
                            $ Party[0].Statup("Obed", 50, 10)
                            $ Party[0].Statup("Inbt", 70, 8)   
                    $ Party[0].Blush = 1
                    
                    if Party[0] == RogueX:
                            ch_r "Aw, that's right sweet of ya, [RogueX.Petname]."
                            ch_r "We'll have to keep this regular."          
                    elif Party[0] == KittyX:
                            ch_k "And that's always nice to hear."
                            ch_k "We'll have to keep this up."
                    elif Party[0] == EmmaX:
                            ch_e "Well. . ."
                            ch_e "We'll have to make a habit of it then."
                    elif Party[0] == LauraX:
                            ch_l "Yeah. . ."
                            ch_l "Warm. . ."
                
            "I loved sleeping next to you." if not Party[0].Sleep:
                    $ Party[0].Statup("Love", 90, 15)
                    $ Party[0].Statup("Love", 70, 10)
                    $ Party[0].Statup("Obed", 50, 12)
                    $ Party[0].Statup("Inbt", 70, 12)
                    $ Line = "nice"
                    
            "It was fun.":
                    if not Party[0].Sleep:                    
                            $ Party[0].Statup("Love", 90, 10)
                            $ Party[0].Statup("Love", 70, 8)
                            $ Party[0].Statup("Obed", 50, 15)
                            $ Party[0].Statup("Inbt", 70, 15)
                    elif Party[0].Sleep < 5:
                            $ Party[0].Statup("Love", 70, 8)
                            $ Party[0].Statup("Obed", 80, 10)
                            $ Party[0].Statup("Inbt", 35, 8)    
                    $ Party[0].Statup("Obed", 50, 8)       
                    if ApprovalCheck(Party[0], 800, "L"):
                            $ Party[0].FaceChange("bemused")
                    else:
                            $ Party[0].FaceChange("confused")
                        
                    if Party[0] == RogueX:
                            ch_r "Ok, well glad I wasn't {i}too{/i} much bother."       
                    elif Party[0] == KittyX:
                            ch_k "Yeah, I mean I guess it was. . ."
                    elif Party[0] == EmmaX:
                            ch_e "\"Fun\" is certainly how I would describe it."
                    elif Party[0] == LauraX:
                            ch_l "Yeah, I guess?"
                            
            "You were constantly tossing around.":    
                    $ Party[0].Blush = 1
                    if ApprovalCheck(Party[0], 800, "L") or ApprovalCheck(Party[0], 1200):
                            $ Party[0].FaceChange("bemused")     
                            call AnyLine(Party[0],"Hmm?")
                    else:
                            $ Party[0].FaceChange("angry")     
                            call AnyLine(Party[0],"!!!")
                    if Party[0].Sleep < 5:                       
                            if Party[0] == RogueX:
                                    ch_r "It's not like I've had much experience sleeping next to someone. . ."      
                            elif Party[0] == KittyX:
                                    ch_k "I don't make a habit out of it. . ."    
                            elif Party[0] == EmmaX:
                                    ch_e "I haven't had a lot of practice lately."
                            elif Party[0] == LauraX:
                                    ch_l "Deal with it."                                
                            $ Party[0].Statup("Love", 60, -8)
                            $ Party[0].Statup("Obed", 50, 22)
                            $ Party[0].Statup("Inbt", 50, 22)                   
                    else:
                            if Party[0] == RogueX:
                                    ch_r "Well you should probably be used to that by now."     
                            elif Party[0] == KittyX:
                                    ch_k "Yeah, well. . . you should be used to that!"
                            elif Party[0] == EmmaX:
                                    ch_e "I don't plan on changing any time soon."
                            elif Party[0] == LauraX:
                                    ch_l "Yeah, it'll be like that."
                    $Line = "toss"
                                
            "You need to learn to stick to your side.":  
                    if Party[0].Sleep < 5:
                            $ Party[0].Statup("Love", 80, -8)
                            $ Party[0].Statup("Obed", 50, 40)
                    if ApprovalCheck(Party[0], 500, "O"):
                            $ Party[0].Statup("Love", 80, -2)
                            $ Party[0].Statup("Obed", 90, 5)
                            $ Party[0].FaceChange("normal")
                            if Party[0] == RogueX:
                                    ch_r "Yes, [RogueX.Petname], I'll try my best."
                            elif Party[0] == KittyX:
                                    ch_k "Fine, whatever."
                            elif Party[0] == EmmaX:
                                    ch_e "I do try."
                            elif Party[0] == LauraX:
                                    ch_l "Ok."
                            if Party[0].Sleep < 5:
                                    $ Party[0].Statup("Obed", 80, 8)
                    else:
                            $ Party[0].FaceChange("angry")
                            $ Party[0].Statup("Obed", 90, 5)
                            if Party[0] == RogueX:
                                    ch_r "Hmmph, you'll be sleeping alone, keep talk'in like that."   
                            elif Party[0] == KittyX:
                                    ch_k "That's not how you get me to come back." 
                            elif Party[0] == EmmaX:
                                    ch_e "I'll sleep how I please."
                            elif Party[0] == LauraX:
                                    ch_l "Good luck with that."
                            if Party[0].Sleep < 5:
                                    $ Party[0].Statup("Inbt", 35, 20) 
                    $Line = "toss"
                                                                
        if not Party[0].Sleep and Line == "nice":  
                if Party[0] == RogueX:
                        $ Party[0].Blush = 1
                        ch_r "Aw, that's right sweet of ya, [RogueX.Petname]."
                        ch_r "Makes me want to do it again sometime."       
                elif Party[0] == KittyX:
                        $ Party[0].Blush = 2
                        ch_k "Yeah, I. . [KittyX.like]I had fun too."
                        $ Party[0].Blush = 1
                        ch_k "I wouldn't[KittyX.like]mind doing it again."   
                        $ Party[0].Blush = 2
                        ch_k "You know, some other time. . . "
                        $ Party[0].Blush = 1
                elif Party[0] == EmmaX:
                        $ Party[0].FaceChange("smile",1)
                        ch_e "You're a hopeless romantic, [EmmaX.Petname]."
                        $ Party[0].FaceChange("smile",2,Eyes="side")
                        ch_e "I suppose I can be a bit hopeless too. . ."
                elif Party[0] == LauraX:
                        $ Party[0].FaceChange("confused",1)
                        ch_l "Oh. . ."
                        $ Party[0].FaceChange("surprised",2,Brows="confused")
                        ch_l "Yeah, so did I, now that you mention it. . ."
                        $ Party[0].FaceChange("confused",1)
                        ch_l "Huh."
                            
        $ Party[0].Blush = 0
            
        if len(Party) >= 2:        
            #second girl's lines
            if "morningwood" in Player.DailyActions:
                    if Party[1] == RogueX:
                            ch_r "And what about me?"                  
                    elif Party[1] == KittyX:
                            ch_k "Me too?"         
                    elif Party[1] == EmmaX:
                            ch_e "And me?"          
                    elif Party[1] == LauraX:
                            ch_l "Ung, 'morning."         
            else:            
                    "[Party[1].Name] rolls over in bed."
                    if Party[1] == RogueX:                        
                            ch_r "Mmm, yeah, 'Morning [RogueX.Petname]."  
                    elif Party[1] == KittyX:
                            ch_k "Yeah, G'morning . . ."
                    elif Party[1] == EmmaX:
                            ch_e "Hrmph. . ."
                            ch_e "Oh. Not so loud, you two."
                    elif Party[1] == LauraX:
                            ch_l "Yeah, 'Morning."
                    
            menu:
                extend ""
                "I always love sleeping with you too, [Party[1].Name]." if Party[1].Sleep: 
                        if Party[1].Sleep < 5:
                            $ Party[1].Statup("Love", 90, 8)
                            $ Party[1].Statup("Obed", 50, 10)
                            $ Party[1].Statup("Inbt", 70, 8)   
                        $ Party[1].Blush = 1
                        
                        if Party[1] == RogueX:
                                ch_r "That's sweet of ya to say, [RogueX.Petname]."
                        elif Party[1] == KittyX:
                                ch_k "So cute!"
                        elif Party[1] == EmmaX:
                                ch_e "Mmmm. . . yes, lovely."
                        elif Party[1] == LauraX:
                                ch_l "Sure. . ."
                    
                "And it was great sleeping with you as well, [Party[1].Name]." if not Party[1].Sleep:
                        $ Party[1].Statup("Love", 90, 15)
                        $ Party[1].Statup("Love", 70, 10)
                        $ Party[1].Statup("Obed", 50, 12)
                        $ Party[1].Statup("Inbt", 70, 12)
                        $ Line = "nice"
                        
                "I had fun sleeping with you too, [Party[1].Name].":
                        if not Party[1].Sleep:                    
                                $ Party[1].Statup("Love", 90, 10)
                                $ Party[1].Statup("Love", 70, 8)
                                $ Party[1].Statup("Obed", 50, 15)
                                $ Party[1].Statup("Inbt", 70, 15)
                        elif Party[1].Sleep < 5:
                                $ Party[1].Statup("Love", 70, 8)
                                $ Party[1].Statup("Obed", 80, 10)
                                $ Party[1].Statup("Inbt", 35, 8)    
                        $ Party[1].Statup("Obed", 50, 8)       
                        if ApprovalCheck(Party[1], 800, "L"):
                                $ Party[1].FaceChange("bemused")
                        else:
                                $ Party[1].FaceChange("confused")
                            
                        if Party[1] == RogueX:
                                ch_r "Yeah, uh, fun."       
                        elif Party[1] == KittyX:
                                ch_k "Yeah, I mean I guess it was. . ."
                        elif Party[1] == EmmaX:
                                ch_e "\"Fun\" is certainly how I would describe it."
                        elif Party[1] == LauraX:
                                ch_l "Yeah, I guess?"
                        $ Line = "fun"
                                
                "You were constantly tossing around, [Party[1].Name]." if Line == "toss":   
                        $ Line = "toss"                                 
                "You were tossing around constantly too, [Party[1].Name]." if Line != "toss":   
                        $ Line = "toss" 
                                    
                "You need to learn to stick to your side, [Party[1].Name]." if Line == "toss":  
                        $ Line = "turn"        
                "And you need to learn to stick to your side too, [Party[1].Name]." if Line != "toss":  
                        $ Line = "turn"
                                                                    
            if not Party[1].Sleep and Line == "nice":  
                    if Party[1] == RogueX:
                            $ Party[1].Blush = 1
                            ch_r "Aw, that's right sweet of ya, [RogueX.Petname]."
                            ch_r "I think I'd want to do that again."    
                            ch_r "And, uh, you too, [Party[0].Name]."
                    elif Party[1] == KittyX:
                            $ Party[1].Blush = 2
                            ch_k "Yeah, I. . [KittyX.like]I had fun too."
                            $ Party[1].Blush = 1
                            ch_k "I wouldn't[KittyX.like]mind doing it again."   
                            $ Party[1].Blush = 2
                            ch_k "You know, some other time. . . "
                            $ Party[1].Blush = 1  
                            ch_k "And[KittyX.like]you too, [Party[0].Name]."
                    elif Party[1] == EmmaX:
                            $ Party[1].FaceChange("smile",1)
                            ch_e "You're a hopeless romantic, [EmmaX.Petname]."
                            $ Party[1].FaceChange("smile",2,Eyes="side")
                            ch_e "I suppose I can be a bit hopeless too. . ."  
                            ch_e "You know what I'm talking about, [Party[0].Name]."
                    elif Party[1] == LauraX:
                            $ LauraX.FaceChange("confused",1)
                            ch_l "Oh. . ."
                            $ Party[1].FaceChange("surprised",2,Brows="confused")
                            ch_l "Yeah, so did I, now that you mention it. . ."
                            $ Party[1].FaceChange("confused",1)
                            ch_l "Huh."  
                            ch_l "Weird, right, [Party[0].Name]?"
                                
            
            elif Line == "toss":   
                        $ Party[1].Blush = 1
                        if ApprovalCheck(Party[1], 800, "L") or ApprovalCheck(Party[1], 1200):
                                $ Party[1].FaceChange("bemused")     
                                call AnyLine(Party[1],"Hmm?")
                        else:
                                $ Party[1].FaceChange("angry")     
                                call AnyLine(Party[1],"!!!")
                        if Party[1].Sleep < 5:                       
                                if Party[1] == RogueX:
                                        ch_r "It's not like I've had much experience sleeping next to someone. . ."      
                                elif Party[1] == KittyX:
                                        ch_k "I don't make a habit out of it. . ."    
                                elif Party[1] == EmmaX:
                                        ch_e "I haven't had a lot of practice lately."
                                elif Party[1] == LauraX:
                                        ch_l "Deal with it."                                
                                $ Party[1].Statup("Love", 60, -8)
                                $ Party[1].Statup("Obed", 50, 22)
                                $ Party[1].Statup("Inbt", 50, 22)                   
                        else:
                                if Party[1] == RogueX:
                                        ch_r "Well you should probably be used to that by now."     
                                elif Party[1] == KittyX:
                                        ch_k "Yeah, well. . . you should be used to that!"
                                elif Party[1] == EmmaX:
                                        ch_e "I don't plan on changing any time soon."
                                elif Party[1] == LauraX:
                                        ch_l "Yeah, it'll be like that."
            
            elif Line == "turn":  
                        if Party[1].Sleep < 5:
                                $ Party[1].Statup("Love", 80, -8)
                                $ Party[1].Statup("Obed", 50, 40)
                        if ApprovalCheck(Party[1], 500, "O"):
                                $ Party[1].Statup("Love", 80, -2)
                                $ Party[1].Statup("Obed", 90, 5)
                                $ Party[1].FaceChange("normal")
                                if Party[1] == RogueX:
                                        ch_r "Yes, [RogueX.Petname], I'll try my best."
                                elif Party[1] == KittyX:
                                        ch_k "Fine, whatever."
                                elif Party[1] == EmmaX:
                                        ch_e "I do try."
                                elif Party[1] == LauraX:
                                        ch_l "Ok."
                                if Party[1].Sleep < 5:
                                        $ Party[1].Statup("Obed", 80, 8)
                        else:
                                $ Party[1].FaceChange("angry")
                                $ Party[1].Statup("Obed", 90, 5)
                                if Party[1] == RogueX:
                                        ch_r "Hmmph, you'll be sleeping alone, keep talk'in like that."   
                                elif Party[1] == KittyX:
                                        ch_k "That's not how you get me to come back." 
                                elif Party[1] == EmmaX:
                                        ch_e "I'll sleep how I please."
                                elif Party[1] == LauraX:
                                        ch_l "Good luck with that."
                                if Party[1].Sleep < 5:
                                        $ Party[1].Statup("Inbt", 35, 20) 
            
            $ Party[1].Blush = 0           
        #end second girl's lines
        
        #fix add sex option here
        
        if len(Party) >= 2:
                $ Party[1].Sleep += 1 
                $ Party[1].DrainWord("sleepover",1,1,1)
                call Girls_Schedule([Party[1]],2) #forces clothing pick
        $ Party[0].Sleep += 1 
        $ Party[0].DrainWord("sleepover",1,1,1)
        call Girls_Schedule([Party[0]],2) #forces clothing pick
                         
        $ Party[0].FaceChange("normal")
        $ Party[0].OutfitChange(6,Changed = 1)
        if len(Party) >= 2:
                $ Party[1].FaceChange("normal")
                $ Party[1].OutfitChange(6,Changed = 1)
                "The girls get changed for the day."
        else:                
                "[Party[0].Name] gets changed for the day."
                
        $ BO = TotalGirls[:]                
        while BO:
                #loops through and makes choices.                
                $ BO[0].OutfitChange(BO[0].OutfitDay)
                $ BO.remove(BO[0])
                    
        $ BO = Party[:]
        while BO:  
                $ Party.remove(BO[0])
                call Girls_Schedule([BO[0]])
                $ BO.remove(BO[0])
        call Girls_Location
        return
    
# end Event Sleepover /////////////////////////////////////////////////////

# start Event Morning Wood /////////////////////////////////////////////////////


# start Morning Wood Check/////////////////////////////////////////////////////    

label Morningwood_Check(Girls=[0,-3],D20=0):                
        #This element sends player to the Morningwood event or returns them
        #it is called from Sleepover_Morning
        
        $ D20 = renpy.random.randint(0,3)  
        $ Line = 0
        
        if len(Party) >= 2:
                #builds a modifier for how the girls like each other
                if Party[0].GirlLikeCheck(Party[1]) >= 900:
                        # If the first girl really likes the second
                        $ Girls[0] = 2
                elif Party[0].GirlLikeCheck(Party[1]) >= 750:
                        # If the first girl kinda likes the second
                        $ Girls[0] = 0
                elif Party[0].GirlLikeCheck(Party[1]) <= 400:
                        # If the first girl really hates the second
                        $ Girls[0] = 2
                else:
                        $ Girls[0] = 0
                    
                if Party[1].GirlLikeCheck(Party[0]) >= 900:
                        # If the second girl really likes the first
                        $ Girls[1] = 2
                elif Party[1].GirlLikeCheck(Party[0]) >= 750:
                        # If the second girl kinda likes the first
                        $ Girls[1] = 0
                elif Party[1].GirlLikeCheck(Party[0]) <= 400:
                        # If the second girl really hates the first
                        $ Girls[1] = -5
                else:
                        $ Girls[1] = -3
        else:
                $ Girls[0] -= 2
        
        
        #checks if Primary girl wants to do it
        if Party[0].Blow >= 5 or ApprovalCheck(Party[0], 900, "I"):  
                $ Girls[0] += 3
        elif Party[0].Blow and ApprovalCheck(Party[0], 900):
                $ Girls[0] += 2
        elif ApprovalCheck(Party[0], 1400):
                $ Girls[0] += 2
        elif Party[0].Blow or ApprovalCheck(Party[0], 900):
                $ Girls[0] += 1
                
        if "hungry" in Party[0].Traits and D20 >= 2:
                #if she likes cum and gets a 50-70 result
                $ Girls[0] += 2
        if Party[0].Thirst >= 60:
                #if she's horny
                $ Girls[0] += 2
        elif Party[0].Thirst >= 30:
                #if she's horny
                $ Girls[0] += 1
        if Party[0].Lust >= 50:
                #if she's horny
                $ Girls[0] += 1
        if Party[0].SEXP <= 15:
                #if she's inexperienced
                $ Girls[0] -= 1 
        #end first girls
        
        if Girls[1] >= 0:
                # if the other girl quite likes her
                $ Girls[0] += 1
                
        #minimum: -1 likely: 3 maximum: 11
        if Girls[0] >= D20:
                $ Line = "yes"  
                
        #end first girl check, Girls[0] maybe "yes," maybe 0
        
        if len(Party) >= 2:
                if Party[1].Blow >= 5 or ApprovalCheck(Party[1], 900, "I"):  
                        $ Girls[1] += 3
                elif Party[1].Blow and ApprovalCheck(Party[1], 900):
                        $ Girls[1] += 2
                elif ApprovalCheck(Party[1], 1400):
                        $ Girls[1] += 2
                elif Party[1].Blow or ApprovalCheck(Party[1], 900):
                        $ Girls[1] += 1
                        
                if "hungry" in Party[1].Traits and D20 >= 2:
                        #if she likes cum and gets a 50-70 result
                        $ Girls[1] += 2
                if Party[1].Thirst >= 60:
                        #if she's horny
                        $ Girls[1] += 2
                elif Party[1].Thirst >= 30:
                        #if she's horny
                        $ Girls[1] += 1
                if Party[1].Lust >= 50:
                        #if she's horny
                        $ Girls[1] += 1
                if Party[1].SEXP <= 15:
                        #if she's inexperienced
                        $ Girls[1] -= 1 
                #end second girls
                                
                if Girls[0] >= 0:
                        # if the other girl quite likes her
                        $ Girls[1] += 1
                        
                #minimum: -6 likely: 2 maximum: 11
                if Girls[1] >= (D20 + 1):# 1-4
                        if Line == "yes": #if the first girl agreed
                                $ Line = "double"  
                        else:
                                $ Line = "other"  
                elif Girls[1] <= -1:
                        $ Line = "no"  
                #else: stays "yes"
                                
                if Line == "other" and Party[0].GirlLikeCheck(Party[1]) >= 500:
                    # If Girl 1 wasn't into it, but liked girl 2 and girl 2 was, swap them                            
                    $ Party.reverse() 
                    $ Girls[0] = "yes"
                    $ Girls[1] = 0
                        
        #End second girl check, Girls[1] maybe "double," maybe "no", maybe 0
        
        if Line:
            # if Line has changed from 0
            if Line == "no":
                        # second girl ruins it
                        "You hear a little commotion as you start to wake up."
                        if Party[1] == RogueX:
                                ch_r "You get'cher head out of there, [Party[0].Name]!"   
                        elif Party[1] == KittyX:
                                "You hear a thump and feel a small woosh as something heavy drops under the bed."                                   
                                call AnyLine(Party[0],"Ow!")
                                ch_k "Serves you right, [Party[0].Name]."
                        elif Party[1] == EmmaX:
                                ch_e "Step away from [Player.Name], [Party[0].Name]."
                        elif Party[1] == LauraX:
                                ch_l "Back it up, [Party[0].Name]."     
                                
                        if Party[0] == RogueX:
                                ch_r "I didn't mean no harm, [Party[1].Name]."   
                        elif Party[0] == KittyX:
                                "You hear a thump and feel a small woosh as something drops under the bed."                                   
                                call AnyLine(Party[0],"Ow!")
                                ch_k "Spoilsport."
                        elif Party[0] == EmmaX:
                                ch_e "Don't be a bore, dear."
                        elif Party[0] == LauraX:
                                ch_l "Fine, whatever."
                        return
            elif Line == "double":
                        # it's a threesome
                        $ Trigger4 = "blow"    
                        $ Party[1].RecentActions.append("blow")           
                        $ Party[1].DailyActions.append("blow")                          
                        $ Party[1].DailyActions.append("morningwood")  
            # it's a solo act with girl 1    
            $ Trigger = "blow"
            $ Party[0].RecentActions.append("blow")           
            $ Party[0].DailyActions.append("blow")                          
            $ Party[0].DailyActions.append("morningwood")  
            call Sleepover_MorningWood
            #call expression Party[0].Tag + "_SexAct" pass ("morningwood") 
            call Sex_Over(0)
            #end "yes"
            
        else: #Girls[0] = 0
            #neither girl was interested 
            pass
            
        return


# end Morning Wood Check///////////////////////////////////////////////////// 



label Sleepover_MorningWood:
        # this label is called from Morningwood_Check, which was called from Sleepover_Morning
                            
        call Shift_Focus(Party[0])
        $ Player.Focus = 30      
        if Trigger == "blow":
                    ch_u "\"Slurp, slurp, slurp.\""
        else:
                    ch_u "\"Squish, squish, squish.\""
                    
        $ Player.Statup("Focus", 80, 5)
        $ Party[0].Statup("Lust", 80, 5)        
        $ Player.DailyActions.append("morningwood") 
        
        $ Partner = Party[1] if len(Party) >= 2 else 0  
        #display other girl here if necessary
        
        $ Player.RecentActions.append("cockout")
        
        if Partner:
                if Partner == RogueX:  
                        show Rogue_Sprite:
                            pos (900,250)
                elif Partner == KittyX:     
                        show Kitty_Sprite:
                            pos (900,250)
                elif Partner == EmmaX:      
                        show Emma_Sprite:
                            pos (900,250)
                elif Partner == LauraX:     
                        show Laura_Sprite:
                            pos (900,250)                  
                $ Partner.RecentActions.append("threesome")
                
        $ Party[0].RecentActions.append("blanket")   
        call expression Party[0].Tag + "_BJ_Launch"  
        
        $ Party[0].FaceChange("closed",1) 
        if Partner:
                $ Partner.FaceChange("closed",1,Mouth="tongue") 
        
        "You feel a pleasant sensation. . ."
        if Trigger == "blow":
                if Trigger4:
                    ch_u "\"Slurp, slurp, slurp.\" \n \ \"Slurp, slurp, slurp.\""
                else:
                    ch_u "\"Slurp, slurp, slurp.\""
        else:
                if Trigger4:
                    ch_u "\"Squish, squish, squish.\" \n \ \"Slurp, slurp, slurp.\""
                else:
                    ch_u "\"Squish, squish, squish.\""
        $ Player.Statup("Focus", 80, 5)
        $ Party[0].Statup("Lust", 80, 5)
        
        "It's somewhere below your waist. . ."  
        if Trigger == "blow":
                if Trigger4:
                    ch_u "\"Slurp, slurp, slurp.\" \n \ \"Slurp, slurp, slurp.\""
                else:
                    ch_u "\"Slurp, slurp, slurp.\""
        else:
                if Trigger4:
                    ch_u "\"Squish, squish, squish.\" \n \ \"Slurp, slurp, slurp.\""
                else:
                    ch_u "\"Squish, squish, squish.\""
        $ Player.Statup("Focus", 80, 10)
        $ Party[0].Statup("Lust", 80, 5)
        
        "You open your eyes. . ."
        
        hide NightMask onlayer nightmask  
        hide blackscreen onlayer black
        
        $ Speed = 3
        $ Count = 3
        $ Line = 0
        call Seen_First_Peen(Party[0],Partner,1,1,1)
        while Count > 0:
                #Looping portion
                $ Player.Statup("Focus", 80, 10)
                $ Party[0].Statup("Lust", 80, 5)
                if Partner:
                        $ Partner.Statup("Lust", 80, 5)
                menu:
                    "Stay Quiet":
                        if Count >2:  
                            if Trigger4:
                                "You just let them do their thing and pretend to still be asleep."
                            else:
                                "You just let her do her thing and pretend to still be asleep."
                        elif Count:
                            "It does feel nice. . ."
                        elif not Count:  
                            if Trigger4:
                                "You wouldn't want to disturb them. . ."  
                            else:                            
                                "You wouldn't want to disturb her. . ." 
                        if Trigger == "blow":
                                call AnyLine(Party[0],"\"Slurp, slurp, slurp.\"")
                        else:
                                call AnyLine(Party[0],"\"Squish, squish, squish.\"")
                        if Trigger4:
                                call AnyLine(Party[1],"\"Slurp, slurp, slurp.\"") 
                        ". . ."
                    "Um. . . [Party[0].Pet], what're you doing?":
                        $ Line = "question"
                        $ Count = 1
                    "That feels great, keep going. . .":
                        $ Line = "praise"
                        $ Count = 1
                    "Hey, quit that!":
                        $ Line = "no"
                        $ Count = 1
                $ Count -= 1
        $ Speed = 1
        $ Party[0].Blush = 1  
        if Trigger4:
                "[Party[0].Name] pulls back with a pop and [Party[1].Name] sits back."
                $ Trigger4 = 0
        else:
                "[Party[0].Name] pulls back with a pop."
        if Line == "question":                    
                        $ Party[0].FaceChange("smile",1) 
                        if Party[0] == RogueX:
                                ch_r "Well I ain't whistlin Dixie, [RogueX.Petname]."    
                        elif Party[0] == KittyX:
                                ch_k "I wasn't[KittyX.like]being subtle about it, [KittyX.Petname]." 
                        elif Party[0] == EmmaX:
                                ch_e "Surely your education hasn't been that poor, [EmmaX.Petname]."
                        elif Party[0] == LauraX:
                                ch_l "Guess."
        elif Line == "praise":
                        $ Party[0].FaceChange("smile",1) 
                        if Party[0] == RogueX:
                                ch_r "Mmm, you know it, [RogueX.Petname]."   
                        elif Party[0] == KittyX:
                                ch_k "Mmm, hehe."
                        elif Party[0] == EmmaX:
                                ch_e "Practice, [EmmaX.Petname]."
                        elif Party[0] == LauraX:
                                ch_l "Yeah, I guess?"
        elif Line == "no":
                        $ Speed = 0
                        $ Party[0].FaceChange("angry",1,Brows="confused")
                        if Party[0] == RogueX:
                                 ch_r "Well that's a fine \"how d'ya do,\" when a girl goes to all this trouble!" 
                        elif Party[0] == KittyX:
                                ch_k "{i}That's{/i} the thanks I get?!"
                        elif Party[0] == EmmaX:
                                ch_e "A little \"gratitude\" wouldn't be uncalled for. . ."
                        elif Party[0] == LauraX:
                                ch_l "Huh?"
        else: #if it fell through due to time
                        if Party[0] == RogueX:
                                ch_r "Heh, I can tell you're awake, [RogueX.Petname]. . ."
                                ch_r "You've been. . . more responsive."    
                        elif Party[0] == KittyX:
                                ch_k "You can stop faking it, [KittyX.Petname]. . ."
                                ch_k "This guy's telling me you're awake now."
                        elif Party[0] == EmmaX:
                                ch_e "I don't know who you think you're fooling."
                                ch_e "You've been awake for a while, [EmmaX.Petname]. . ."    
                        elif Party[0] == LauraX:
                                ch_l "You can stop playing dead, [LauraX.Petname]. . ."
                                ch_l "Oldest trick in the book."   
        #end first response phase
                                
        if Partner:        
                #second girl's lines
                if Line == "question":                    
                                $ Party[1].FaceChange("smile",1) 
                elif Line == "praise":
                                $ Party[1].FaceChange("smile",1) 
                elif Line == "no":
                                $ Party[1].FaceChange("angry",1,Brows="confused")
                        
                if Partner == RogueX:       
                        if "blow" in RogueX.RecentActions:
                            ch_r "I don't know 'bout that, [RogueX.Petname]."
                        else:
                            "[RogueX.Name] rolls over in bed."
                            ch_r "Don't stop on my account, [RogueX.Petname]."  
                elif Partner == KittyX:
                        if "blow" in KittyX.RecentActions:
                            ch_k "Huh. . ."
                        else:
                            "[KittyX.Name] rolls over in bed."
                            ch_k "Looked like you were having some fun there . . ."
                elif Partner == EmmaX:
                        if "blow" in EmmaX.RecentActions:
                            ch_e "Well. . ."
                        else:
                            "[EmmaX.Name] rolls over in bed."
                            ch_e "Oh, don't let me stop you two."
                elif Partner == LauraX:
                        if "blow" in LauraX.RecentActions:
                            ch_l "Hmm. . ."
                        else:
                            "[LauraX.Name] rolls over in bed and stares at you both."
                                
        #start second question phase
        menu:
            "So, um, you want to get back to it?":
                    if Line != "no":
                            #assuming you weren't rude
                            $ Party[0].FaceChange("smile",1)                              
                            if Party[0] == RogueX:
                                    ch_r "My pleasure."     
                            elif Party[0] == KittyX:
                                    ch_k "Hehe, mmmm. . ."
                            elif Party[0] == EmmaX:
                                    ch_e "If you insist. . ."
                            elif Party[0] == LauraX:
                                    ch_l "That's the plan. . ."    
                    elif Line == "no" and ApprovalCheck(Party[0], 1750):
                            #if you were a dick but she's ok
                            $ Party[0].FaceChange("bemused")
                            if Party[0] == RogueX:
                                    ch_r "You're lucky I'm so into you. . ."    
                            elif Party[0] == KittyX:
                                    ch_k "Wha? Well. . . I guess. . ."
                            elif Party[0] == EmmaX:
                                    ch_e "Do try not to be a prat this time. . ."
                            elif Party[0] == LauraX:
                                    ch_l "Fine. . ."   
                            $ Line = "maybe"
                    else:
                            #if you were a dick and she's not ok with that
                            $ Party[0].FaceChange("angry",1)  
                            if Party[0] == RogueX:
                                    ch_r "Well not when you're rude to me."                
                                    ch_r "You can polish yourself off."     
                            elif Party[0] == KittyX:
                                    ch_k "You can't walk that one back!"
                                    ch_k "You can take care of that yourself."
                            elif Party[0] == EmmaX:
                                    ch_e "Not with your attitude."
                                    ch_e "I think you can manage to finish this yourself."
                            elif Party[0] == LauraX:
                                    ch_l "No."  
            "Were you more interested in something else?":
                    if Line != "no":
                            #assuming you weren't rude
                            $ Party[0].FaceChange("sexy",1)  
                            if Party[0] == RogueX:
                                    ch_r "Ooh, what did you have in mind?"  
                            elif Party[0] == KittyX:
                                    ch_k "Maaaybee. . . like what?"
                            elif Party[0] == EmmaX:
                                    ch_e "Perhaps. . . What did you have in mind?"
                            elif Party[0] == LauraX:
                                    ch_l "Yeah, I guess?"
                            $ Line = "sex"
                    elif Line == "no" and ApprovalCheck(Party[0], 1650):
                            #if you were a dick but she's ok
                            $ Party[0].FaceChange("bemused",1)  
                            if Party[0] == RogueX:
                                    ch_r "Well, you're a jerk, but you're a cute jerk."
                                    ch_r "What were you thinking?"     
                            elif Party[0] == KittyX:
                                    ch_k "Oh, so you had something {i}else{/i} in mind. . ."
                                    ch_k "Like what?"
                            elif Party[0] == EmmaX:
                                    ch_e "Hmm, second chance [EmmaX.Petname], what were you considering?"
                            elif Party[0] == LauraX:
                                    ch_l "Yeah, I guess?"
                            $ Line = "sex"
                    else:
                            #if you were a dick and she's not ok with that
                            $ Party[0].FaceChange("angry",1)  
                            if Party[0] == RogueX:
                                    ch_r "Well not when you're rude to me."                
                                    ch_r "You can polish yourself off."     
                            elif Party[0] == KittyX:
                                    ch_k "You can't walk that one back!"
                                    ch_k "You can take care of that yourself."
                            elif Party[0] == EmmaX:
                                    ch_e "Not with your attitude."
                                    ch_e "I think you can manage to finish this yourself."
                            elif Party[0] == LauraX:
                                    ch_l "No."  
            "Sorry, sorry, please continue." if Line == "no":
                    if ApprovalCheck(Party[0], 1450):
                            #if you were a dick but she's ok
                            $ Party[0].FaceChange("bemused",1)  
                            if Party[0] == RogueX:
                                    ch_r "Well, since you asked so nice. . ."    
                            elif Party[0] == KittyX:
                                    ch_k "I guess I can forgive you. . ."
                            elif Party[0] == EmmaX:
                                    ch_e "Ok, I'll give you another chance here."
                            elif Party[0] == LauraX:
                                    ch_l "Yeah, I guess?"
                            $ Line = "maybe"
                    else:
                            #if you were a dick and she's not ok with that
                            $ Party[0].FaceChange("angry",1)  
                            if Party[0] == RogueX:
                                    ch_r "Well not when you're rude to me."                
                                    ch_r "You can polish yourself off."     
                            elif Party[0] == KittyX:
                                    ch_k "You can't walk that one back!"
                                    ch_k "You can take care of that yourself."
                            elif Party[0] == EmmaX:
                                    ch_e "Not with your attitude."
                                    ch_e "I think you can manage to finish this yourself."
                            elif Party[0] == LauraX:
                                    ch_l "No."  
            "Sorry, but we could do something else." if Line == "no":
                    if ApprovalCheck(Party[0], 1350):
                            #if you were a dick but she's ok
                            $ Party[0].FaceChange("sexy",1)  
                            if Party[0] == RogueX:
                                    ch_r "Well, since you asked so nice. . ."
                                    ch_r "What did you have in mind?"   
                            elif Party[0] == KittyX:
                                    ch_k "I guess, maybe. . ."
                                    ch_k "Like what?"
                            elif Party[0] == EmmaX:
                                    ch_e "Mmm, I'll consider it. . ."
                            elif Party[0] == LauraX:
                                    ch_l "Yeah, I guess?"                                    
                            $ Line = "sex"
                    else:
                            #if you were a dick and she's not ok with that
                            $ Party[0].FaceChange("angry",1) 
                            if Party[0] == RogueX:
                                    ch_r "Well not when you're rude to me."                
                                    ch_r "You can polish yourself off."     
                            elif Party[0] == KittyX:
                                    ch_k "You can't walk that one back!"
                                    ch_k "You can take care of that yourself."
                            elif Party[0] == EmmaX:
                                    ch_e "Not with your attitude."
                                    ch_e "I think you can manage to finish this yourself."
                            elif Party[0] == LauraX:
                                    ch_l "No."  
            "Not when I'm just waking up.":
                            $ Party[0].FaceChange("angry",1)  
                            if Party[0] == RogueX:
                                    ch_r "Fine, whatever!"
                                    $RogueX.Eyes = "side"
                                    ch_r "[[mumbles] Girl tries to do a favor. . ."     
                            elif Party[0] == KittyX:
                                    ch_k "Aw. . ."
                                    $KittyX.Eyes = "side"
                                    ch_k "Last time I do you a favor. . ."
                            elif Party[0] == EmmaX:
                                    ch_e "Hmph. . ."
                                    $EmmaX.Eyes = "side"
                                    ch_e "It's not as though that was for my benefit. . ."
                            elif Party[0] == LauraX:
                                    ch_l "Tsk. . ."
                                    $LauraX.Eyes = "side"
                                    ch_l "\"No free blowjobs,\" got it. . ."                                    
                            $ Line = "no"
        #end second question phase
                    
                       
        if Line == "no" or Line == "sex":
                if Partner:
                        $ Partner.FaceChange("sexy")  
                $ Party[0].RecentActions.remove("blanket") 
                call expression Party[0].Tag + "_BJ_Reset"
                
                if len(Party) >= 2:
                    if Party[1] == RogueX:       
                            show Rogue_Sprite:
                                ease 1 pos (700,50)
                            show Rogue_Sprite:
                                pos (700,50)
                    elif Party[1] == KittyX:     
                            show Kitty_Sprite:
                                ease 1 pos (700,50)
                            show Kitty_Sprite:
                                pos (700,50)
                    elif Party[1] == EmmaX:      
                            show Emma_Sprite:
                                ease 1 pos (700,50)
                            show Emma_Sprite:
                                pos (700,50)
                    elif Party[1] == LauraX:     
                            show Laura_Sprite:
                                ease 1 pos (700,50)  
                            show Laura_Sprite:
                                pos (700,50)  
                        
                if Line == "no":     
                        if bg_current == "bg player":
                            if Partner:
                                    call AnyLine(Partner,"I'm out of here.")           
                            call AnyLine(Party[0],"Yeah, me too.")
                        else:
                            call AnyLine(Party[0],"Oh, get out of here already.") 
                        
                        $ Party[0].OutfitChange(6) #sets to OutfitDay
                        if Partner:
                                $ Partner.OutfitChange(6)
                        $ Party = []
                        $ Partner = 0
                        jump Return_Player
                        
                elif Line == "sex":
                        #shift to other sex stuff with her
                        call expression Party[0].Tag + "_SexMenu"
        else: 
                        #continue with the BJ
                        $ Line = 0
                        $ Speed = 1
                        $ Situation = 0
                        if Partner:
                                $ Trigger4 = "blow"
                        call Morning_Partner
                        call expression Party[0].Tag + "_SexAct" pass ("blow")
        return
    
# end Event Morning Wood /////////////////////////////////////////////////////    

label Morning_Partner: 
        #Called from sex act menu
        if not Partner:
                return
        $ Partner.FaceChange("sexy") 
        if Partner == RogueX:       
                show Rogue_Sprite:
                    ease 1 pos (700,50)
                show Rogue_Sprite:
                    pos (700,50)
        elif Partner == EmmaX:      
                show Emma_Sprite:
                    ease 1 pos (700,50)
                show Emma_Sprite:
                    pos (700,50)
        elif Partner == KittyX:     
                show Kitty_Sprite:
                    ease 1 pos (700,50)  
                show Kitty_Sprite:
                    pos (700,50) 
        elif Partner == LauraX:     
                show Laura_Sprite:
                    ease 1 pos (700,50)  
                show Laura_Sprite:
                    pos (700,50) 
        return
    
    
## start Poly _Start//////////////////////////////////////////////////////////
label Poly_Start(Newbie=0,Round2=0):
        # This is called prior to any new girls being added to your dating structure
        # If there are already two girls in there, it kicks up to the Harem version. 
        # Newbie will be the new girl
        $ Line = 0
                
        if not Player.Harem:            
            return
        if len(Player.Harem) >= 2:
            call Harem_Start(Newbie,Round2)
            return
            
        if "polystart" in Player.DailyActions:
                return                
        $ Player.DailyActions.append("polystart")
        
        $ Party = [Player.Harem[0]]
        call Shift_Focus(Player.Harem[0])
        call Set_The_Scene
        call CleartheRoom(Player.Harem[0])
        
            
        if Round2:
                "You pull [Party[0].Name] aside for a moment."
                ch_p "Hey, have you changed your mind about [Newbie.Name] lately?"
        else:
                $ Party[0].FaceChange("bemused")
                "[Party[0].Name] pulls you aside and wants to talk about something."
                
                #Line 1
                if Party[0] == RogueX:                 
                        ch_r "I've seen you were getting pretty cozy with [Newbie.Name]."
                elif Party[0] == KittyX:      
                        ch_k "You look kinda close with [Newbie.Name] lately."
                elif Party[0] == EmmaX:      
                        ch_e "I've noticed that [Newbie.Name] and yourself have been spending time together."
                elif Party[0] == LauraX:     
                        ch_l "You've been all over [Newbie.Name] lately."
                #end Line 1
        
        
        if Party[0].GirlLikeCheck(Newbie) >= 800:
                $ Party[0].FaceChange("sly")  
        elif Party[0].GirlLikeCheck(Newbie) >= 600:
                pass
        else:
                # neither likes her much
                $ Party[0].FaceChange("angry",Mouth="normal")  
                
        # We like her or not
        if Party[0] == RogueX:       
                if Party[0].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_r "She is pretty sexy, I guess."
                elif Party[0].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_r "I like her just fine, I was just wondering where it was headed."               
                else:
                        # neither likes her much
                        ch_r "I'm not really a fan'a hers."                    
        elif Party[0] == KittyX:    
                if Party[0].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_k "She's kinda hot, I get that. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_k "She's ok, sure, but I'm not sure. . ."
                else:
                        # neither likes her much
                        ch_k "I don't really like her much." 
        elif Party[0] == EmmaX:     
                if Party[0].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_e "I think she's quite the catch."
                elif Party[0].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_e "I do like her, but have some concerns."
                else:
                        # neither likes her much
                        ch_e "I don't really approve."
        elif Party[0] == LauraX:   
                if Party[0].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_l "She's pretty hot, I get it."
                elif Party[0].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_l "She's ok, I guess."
                else:
                        # neither likes her much
                        ch_l "I don't like her."
        #end line 2
        
        
        #Line 3
        if Party[0] == RogueX:                 
                ch_r "I don't know how I feel about sharing you with some other girl."
                ch_r "So did you plan to get serious with her?"
        elif Party[0] == KittyX:      
                ch_k "I don't know about sharing my boyfriend with somebody else."
                ch_k "So are you[KittyX.like]trying to date her?"
        elif Party[0] == EmmaX:      
                ch_e "I can be a bit. . . possessive with my partners."
                ch_e "Is this getting serious with her?"
        elif Party[0] == LauraX:     
                ch_l "I don't play well with others."
                ch_l "Are you two getting serious?"
        #end Line 3
                
        menu:
            extend ""
            "Yeah, I'd like to date her too.":
                $ Line = "y"
            "Maybe, what do you think?":
                $ Line = "m"
            "No, not really.":
                $ Line = "n"
            
        if Line == "y":     
            if Party[0].GirlLikeCheck(Newbie) >= 800:
                    # if they like her a lot
                    $ Line = "yy"
                    $ Party[0].Statup("Love", 90, 5)
                    $ Party[0].Statup("Obed", 50, 5)
                    $ Party[0].Statup("Inbt", 90, 10) 
            elif ApprovalCheck(Party[0], 1800):
                    # if they really like you enough to put up with it
                    $ Line = "ym"
                    $ Party[0].Statup("Obed", 50, 5) 
            elif ApprovalCheck(Party[0], 1500) and Party[0].GirlLikeCheck(Newbie) >= 500:
                    # if they like her well enough
                    $ Line = "ym"
            else:
                    # neither likes her much
                    $ Line = "yn"  
                    $ Party[0].Statup("Love", 90, -10)
        #end Line = y
        if Line == "m":
            if Party[0].GirlLikeCheck(Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "my"
                    $ Party[0].Statup("Inbt", 90, 5) 
            elif ApprovalCheck(Party[0], 1800):
                    # if they both really like you enough to put up with it
                    $ Line = "mm"
            elif ApprovalCheck(Party[0], 1500) and Party[0].GirlLikeCheck(Newbie) >= 600:
                    # if they both like her well enough
                    $ Line = "mm"
            else:
                    # neither likes her much
                    $ Line = "mn" 
        #end Line = m  
        if Line == "n":
            if Party[0].GirlLikeCheck(Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "ny"
                    $ Party[0].Statup("Inbt", 90, 10) 
            elif ApprovalCheck(Party[0], 1700):
                    # if they both really like you enough to put up with it
                    $ Line = "nm"
                    $ Party[0].Statup("Inbt", 90, 5) 
            elif ApprovalCheck(Party[0], 1300) and Party[0].GirlLikeCheck(Newbie) >= 500:
                    # if they both like her well enough
                    $ Line = "nm"
                    $ Party[0].Statup("Love", 90, 5)
            else:
                    # if they don't like her well enough
                    $ Line = "nn"
                    $ Party[0].Statup("Love", 90, 10)
        #end Line = n      
            
            
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
        if Line == "yn" or Line == "mn" or Line == "nn":
                $ Party[0].FaceChange("angry")
        elif Line == "yy" or Line == "ny" or Line == "my":
                $ Party[0].FaceChange("sexy")
        else:
                $ Party[0].FaceChange("bemused")
                
        #Line 5
        if Party[0] == RogueX:       
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_r "Great, sounds fun."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_r "Oh, don't let me stop you."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_r "Oh. Well maybe you should!"
                        
                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_r "Yeah, I guess I can live with that."                        
                elif Line == "nm":
                        # if you said no but they both like her well enough                      
                        ch_r "Hmm, not that I would have minded."
                                
                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_r "I don't think I'm really cool with that."
                elif Line == "nn":
                        # if you said no and agree
                        ch_r "Good to hear."
                        
        elif Party[0] == KittyX:        
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_k "Cool, sounds fun."     
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_k "Oh, seriously, it's fine with me!"
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_k "You might want to, she's hot!"                        
                        
                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_k "Yeah, I can[KittyX.like]live with that."              
                elif Line == "nm":
                        # if you said no but they both like her well enough    
                        ch_k "Ok, I would have been ok with it though."
                        
                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_k "That's not really cool with me."                          
                elif Line == "nn":
                        # if you said no and agree
                        ch_k "Good, that wouldn't have been cool."
                        
        elif Party[0] == EmmaX:          
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_e "Lovely. . ."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_e "Oh, please do, she's lovely."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_e "Pity, I rather like her."
                        
                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_e "I suppose I can make do then."            
                elif Line == "nm":
                        # if you said no but they both like her well enough    
                        ch_e "You could do a lot worse."
                        
                elif Line == "yn" or Line == "mn":
                        # neither likes her much
                        ch_e "I don't think that will be acceptable."
                elif Line == "nn":
                        # if you said no and agree
                        ch_e "Probably for the best."
                        
        elif Party[0] == LauraX:        
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_l "Nice."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_l "Come on, she's pretty great."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_l "You sure? She's hot."
                        
                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_l "Fine, I can work with that."            
                elif Line == "nm":
                        # if you said no but they both like her well enough   
                        ch_l "Ok. I'm cool with it if you do though." 
                        
                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_l "Nope."
                elif Line == "nn":
                        # if you said no and agree
                        ch_l "Good."
        #end Line 5
        
        if Line != "yy" and Line != "nn":
            #if there was some doubt to it
            menu:
                extend ""
                "Ok, then I guess I will ask her to join us." if Line in ("my","ny","ym","mm","nm"):
                    #They were generally favorable, so you agreed
                    $ Line = "yy"
                    $ Party[0].FaceChange("smile")
                    $ Party[0].Statup("Love", 90, 10)
                    $ Party[0].Statup("Obed", 50, 10)
                    if Party[0] == RogueX:       
                                    ch_r "Great, sounds fun."                 
                    elif Party[0] == KittyX:        
                                    ch_k "Cool, sounds fun."                                        
                    elif Party[0] == EmmaX:          
                                    ch_e "Lovely. . ."                                   
                    elif Party[0] == LauraX:        
                                    ch_l "Nice."   
                
                "Well then, I guess I'll stop." if Line in ("mn","yn","ym","mm","nm"):
                    #They were unfavorable, so you gave up on it. 
                    $ Line = "nn"
                    $ Party[0].FaceChange("smile")
                    $ Party[0].Statup("Love", 90, 10) 
                    if Party[0] == RogueX:       
                                    ch_r "Good to hear."                        
                    elif Party[0] == KittyX:        
                                    ch_k "Good, that wouldn't have been cool."                        
                    elif Party[0] == EmmaX:       
                                    ch_e "Probably for the best."                        
                    elif Party[0] == LauraX:        
                                    ch_l "Good."
                
                "I'm asking her in anyway." if Line in ("mn","yn"):
                    #if they were unfavorable, but you insist
                    pass
                    
                "Well, I'm going to pass anyway." if Line in ("nm","ny","mm"):
                    #if they give you permission, but you aren't into it.
                    $ Line = "nn"
                    $ Party[0].FaceChange("sad")
                    $ Party[0].Statup("Obed", 70, 5) 
                    if Party[0] == RogueX:       
                                    ch_r "Oh, ok."                        
                    elif Party[0] == KittyX:        
                                    ch_k "That's fine."                        
                    elif Party[0] == EmmaX: 
                                    ch_e "If you insist."                        
                    elif Party[0] == LauraX:        
                                    ch_l "Ok."
                                                
        #end player response to their feedback
            
        if Line == "mn" or Line == "yn":
                # if you said yes/maybe and they said no, but you insisted anyway 
                                 
                if ApprovalCheck(Party[0], 1600) and Party[0].GirlLikeCheck(Newbie) >= 500:
                            $ Party[0].FaceChange("sadside")
                            $ Party[0].Statup("Love", 90, -5)
                            $ Party[0].Statup("Obed", 50, 15)
                            if Party[0] == RogueX:                 
                                    ch_r "Fine, she's in."
                            elif Party[0] == KittyX:      
                                    ch_k "Geeze, ok."
                            elif Party[0] == EmmaX:      
                                    ch_e "I suppose we'll make room."
                            elif Party[0] == LauraX:     
                                    ch_l "Whatever."
                            $ Line = "yy"
                else:
                            $ Party[0].FaceChange("angry",Eyes="side")
                            $ Party[0].Statup("Love", 90, -25)
                            $ Party[0].Statup("Inbt", 90, 10) 
                            if Party[0] == RogueX:                 
                                    ch_r "I just don't like you that much, [RogueX.Petname]."
                                    ch_r "I'm out."                                    
                            elif Party[0] == KittyX:      
                                    ch_k "You aren't that cute, [KittyX.Petname]."
                                    ch_k "I'm done."
                            elif Party[0] == EmmaX:      
                                    ch_e "Don't overestimate yourself, [EmmaX.Petname]."
                                    ch_e "We're done."
                            elif Party[0] == LauraX:     
                                    ch_l "Too far, [LauraX.Petname]."
                                    ch_l "I'm out of here."
                            if "dating" in Party[0].Traits:
                                $ Party[0].Traits.remove("dating")
                            $ Party[0].Traits.append("ex")
                            $ Party[0].Break[0] = 5 + Party[0].Break[1] + Party[0].Cheated                                    
                            $ Player.Harem.remove(Party[0])
                            call Remove_Girl(Party[0])
        #end "she said no but you insisted"        
                   
        $ Party = []
        if Line == "yy":
                if Newbie.Tag + "No" in Player.Traits:                   
                        $ Player.Traits.remove(Newbie.Tag + "No")
                $ Player.DrainWord(Newbie.Tag + "No",0,0,1)
                $ Player.Traits.append(Newbie.Tag + "Yes")
                "You should give [Newbie.Name] a call."   
        else:     
                $ Player.Traits.append(Newbie.Tag + "No")
        return
        
## end Poly _Start//////////////////////////////////////////////////////////



## start Harem _Start//////////////////////////////////////////////////////////
label Harem_Start(Newbie=0,Round2=0):    
        # This is called prior to any new girls being added to your dating structure
        # If there are aren't two girls in there, it kicks back. 
        # Newbie will be the new girl
        
        if "harem" in Player.DailyActions:
                return                
        $ Player.DailyActions.append("harem")
        $ Line = 0
        
        if len(Player.Harem) < 2:
                #if there aren't enough girls yet, forget about it.
                return
                
        $ Party = [Player.Harem[0],Player.Harem[1]]
        # Adds first two harem members to party, removed everyone else from the room.
        call Present_Check        
        $ Party = [Player.Harem[0],Player.Harem[1]]
        call Shift_Focus(Player.Harem[0])
        call Set_The_Scene            
        
        $ Party[0].FaceChange("bemused")
        $ Party[1].FaceChange("bemused")
        if Round2:
                "You call [Party[0].Name] and [Party[1].Name] over."
                ch_p "I was wondering if you'd changed your mind about [Newbie.Name]."
        else:
                "[Party[0].Name] pulls you aside and wants to talk about something."
                #Line 1
                
                if Party[0] == RogueX:       
                        ch_r "Hey, so me and [Party[1].Name] have been talk'in."                 
                elif Party[0] == KittyX:    
                        ch_k "So[KittyX.like]me and [Party[1].Name] had a little chat."   
                elif Party[0] == EmmaX:     
                        ch_e "[Party[1].Name] and I have been discussing a few things."   
                elif Party[0] == LauraX:   
                        ch_l "I had a little chat with [Party[1].Name]. . ." 
                #end Line 1
                
                #Line 2
                if Party[1] == RogueX:                 
                        ch_r "We hear that you were getting pretty cozy with [Newbie.Name]."
                elif Party[1] == KittyX:      
                        ch_k "We hear that you're kinda close with [Newbie.Name] lately."
                elif Party[1] == EmmaX:      
                        ch_e "We've hear that [Newbie.Name] and yourself have been spending time together."
                elif Party[1] == LauraX:     
                        ch_l "You've been all over [Newbie.Name] lately."
                #end Line 2
                
        # We like her or not Line 3
        
        if Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                pass
        elif Party[0].GirlLikeCheck(Newbie) >= 700:
                # only first girl likes her
                $ Party[1].FaceChange("angry",Mouth="normal")
        elif Party[1].GirlLikeCheck(Newbie) >= 700:
                # only second girl likes her
                $ Party[0].FaceChange("angry",Mouth="normal")
        else:
                # neither likes her much
                $ Party[0].FaceChange("angry",Mouth="normal") 
                $ Party[1].FaceChange("angry",Mouth="normal")    
                
        if Party[0] == RogueX:       
                if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_r "Now we like her just fine, and we can't say we don't like the idea much."
                elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_r "Now we like her just fine, but we don't know about share'in."
                elif Party[0].GirlLikeCheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_r "Now I like her just fine, but [Party[1].Name] ain't so sure."
                elif Party[1].GirlLikeCheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_r "Now [Party[1].Name] seems to like her, but I'm not so sure."
                else:
                        # neither likes her much
                        ch_r "Neither'a us is really cool with that."                    
        elif Party[0] == KittyX:    
                if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_k "She's kinda hot, we get that. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_k "She's ok, sure, but we're not sure. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_k "I like her, but I don't know about [Party[1].Name]."
                elif Party[1].GirlLikeCheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_k "[Party[1].Name] likes her, but I don't know."
                else:
                        # neither likes her much
                        ch_k "We don't really like her much." 
        elif Party[0] == EmmaX:     
                if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_e "I think we agree that she's a nice catch."
                elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_e "We do like her, but we have some concerns."
                elif Party[0].GirlLikeCheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_e "[Party[1].Name] doesn't really approve."
                elif Party[1].GirlLikeCheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_e "[Party[1].Name] seems to think she's acceptable."
                else:
                        # neither likes her much
                        ch_e "We don't really approve."
        elif Party[0] == LauraX:   
                if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_l "She's pretty hot, we get it."
                elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_l "She's ok, I guess."
                elif Party[0].GirlLikeCheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_l "She's fine, but [Party[1].Name] doesn't like her."
                elif Party[1].GirlLikeCheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_l "[Party[1].Name] likes her. I don't."
                else:
                        # neither likes her much
                        ch_l "We don't like her."
        #end line 3
        
        #Line 4
        if Party[1] == RogueX:                 
                ch_r "So did you plan to get serious with her?"
        elif Party[1] == KittyX:      
                ch_k "So are you[KittyX.like]trying to date her?"
        elif Party[1] == EmmaX:      
                ch_e "Is this getting serious with her?"
        elif Party[1] == LauraX:     
                ch_l "Are you two getting serious?"
        #end Line 4
        
        menu:
            extend ""
            "Yeah, I'd like to date her too.":
                $ Line = "y"
            "Maybe, what do you think?":
                $ Line = "m"
            "No, not really.":
                $ Line = "n"
            
        if Line == "y":     
            if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "yy"                       
                    $ Party[0].Statup("Love", 90, 5)
                    $ Party[0].Statup("Obed", 50, 5)
                    $ Party[0].Statup("Inbt", 90, 10) 
                    $ Party[1].Statup("Love", 90, 5)
                    $ Party[1].Statup("Obed", 50, 5)
                    $ Party[1].Statup("Inbt", 90, 10) 
            elif ApprovalCheck(Party[0], 1800) and ApprovalCheck(Party[1], 1800):
                    # if they both really like you enough to put up with it
                    $ Line = "ym"
                    $ Party[0].Statup("Obed", 50, 10)
                    $ Party[1].Statup("Obed", 50, 10)
            elif ApprovalCheck(Party[0], 1500) and ApprovalCheck(Party[1], 1500):
                    if Party[0].GirlLikeCheck(Newbie) >= 500 and Party[1].GirlLikeCheck(Newbie) >= 500:
                            # if they both like her well enough
                            $ Line = "ym"
                            $ Party[0].Statup("Obed", 80, 15) 
                            $ Party[1].Statup("Obed", 80, 15) 
                    else:
                            # if they don't like her well enough
                            $ Line = "yn"
                            $ Party[0].Statup("Love", 90, -5)
                            $ Party[0].Statup("Obed", 50, -5)
                            $ Party[1].Statup("Love", 90, -5)
                            $ Party[1].Statup("Obed", 50, -5)
            else:
                            # neither likes her much
                            $ Line = "yn"  
                            $ Party[0].Statup("Love", 90, -10)
                            $ Party[0].Statup("Obed", 50, -5)
                            $ Party[1].Statup("Love", 90, -10)
                            $ Party[1].Statup("Obed", 50, -5)
        #end Line = y
        if Line == "m":
            if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "my"
                    $ Party[0].Statup("Inbt", 90, 5) 
                    $ Party[1].Statup("Inbt", 90, 5) 
            elif ApprovalCheck(Party[0], 1800) and ApprovalCheck(Party[1], 1800):
                    # if they both really like you enough to put up with it
                    $ Line = "mm"
            elif ApprovalCheck(Party[0], 1500) and ApprovalCheck(Party[1], 1500):
                    if Party[0].GirlLikeCheck(Newbie) >= 600 or Party[1].GirlLikeCheck(Newbie) >= 600:
                            # if they both like her well enough
                            $ Line = "mm"
                    else:
                            # if they don't like her well enough
                            $ Line = "mn"
            else:
                            # neither likes her much
                            $ Line = "mn" 
        #end Line = m  
        if Line == "n":
            if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "ny"
                    $ Party[0].Statup("Inbt", 90, 10) 
                    $ Party[1].Statup("Inbt", 90, 10) 
            elif ApprovalCheck(Party[0], 1700) and ApprovalCheck(Party[1], 1700):
                    # if they both really like you enough to put up with it
                    $ Line = "nm"
                    $ Party[0].Statup("Inbt", 90, 5) 
            elif ApprovalCheck(Party[0], 1300) and ApprovalCheck(Party[1], 1300):
                    if Party[0].GirlLikeCheck(Newbie) >= 500 and Party[1].GirlLikeCheck(Newbie) >= 500:
                            # if they both like her well enough
                            $ Line = "nm"
                    else:
                            # if they don't like her well enough
                            $ Line = "nn"
                            $ Party[0].Statup("Love", 90, 5)
                            $ Party[0].Statup("Inbt", 90, 5) 
                            $ Party[1].Statup("Love", 90, 5)
                            $ Party[1].Statup("Inbt", 90, 5) 
            else:
                            # neither likes her much
                            $ Line = "nn" 
                            $ Party[0].Statup("Love", 90, 5)
                            $ Party[0].Statup("Inbt", 90, 5) 
                            $ Party[1].Statup("Love", 90, 5)
                            $ Party[1].Statup("Inbt", 90, 5) 
        #end Line = n      
                                                  
            
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                
        if Line == "yn" or Line == "mn" or Line == "nn":
                $ Party[0].FaceChange("angry")
                $ Party[1].FaceChange("angry")
        elif Line == "yy" or Line == "ny" or Line == "my":
                $ Party[0].FaceChange("sexy")
                $ Party[1].FaceChange("sexy")
        else:
                $ Party[0].FaceChange("bemused")
                $ Party[1].FaceChange("bemused")   
                
        #Line 5
        if Party[0] == RogueX:       
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_r "Great, sounds fun."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_r "Oh, don't let me stop you."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_r "Oh. Well maybe you should!"
                        
                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_r "Yeah, I guess we can live with that."                        
                elif Line == "nm":
                        # if you said no but they both like her well enough                      
                        ch_r "Hmm, not that we would have minded."
                                
                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_r "I don't think we're really cool with that."
                elif Line == "nn":
                        # if you said no and agree
                        ch_r "Good to hear."
                        
        elif Party[0] == KittyX:        
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_k "Cool, sounds fun."     
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_k "Oh, seriously, it's fine with us!"
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_k "You might want to, she's hot!"                        
                        
                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_k "Yeah, we can[KittyX.like]live with that."              
                elif Line == "nm":
                        # if you said no but they both like her well enough    
                        ch_k "Ok, we would have been ok with it though."
                        
                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_k "That's not really cool with us."                          
                elif Line == "nn":
                        # if you said no and agree
                        ch_k "Good, that wouldn't have been cool."
                        
        elif Party[0] == EmmaX:          
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_e "Lovely. . ."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_e "Oh, please do, she's lovely."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_e "Pity, I rather like her."
                        
                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_e "I suppose we can make do then."            
                elif Line == "nm":
                        # if you said no but they both like her well enough    
                        ch_e "You could do a lot worse."
                        
                elif Line == "yn" or Line == "mn":
                        # neither likes her much
                        ch_e "I don't think that will be acceptable."
                elif Line == "nn":
                        # if you said no and agree
                        ch_e "Probably for the best."
                        
        elif Party[0] == LauraX:        
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_l "Nice."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_l "Come on, she's pretty great."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_l "You sure? She's hot."
                        
                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_l "Fine, we can work with that."            
                elif Line == "nm":
                        # if you said no but they both like her well enough   
                        ch_l "Ok. We're cool with it if you do though." 
                        
                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_l "Nope."
                elif Line == "nn":
                        # if you said no and agree
                        ch_l "Good."
        #end Line 5
        
        if Line != "yy" and Line != "nn":
            #if there was some doubt to it
            menu:
                extend ""
                "Ok, then I guess I will ask her to join us." if Line in ("my","ny","ym","mm","nm"):
                        #They were generally favorable, so you agreed
                        $ Line = "yy"
                        $ Party[0].FaceChange("smile")
                        $ Party[1].FaceChange("smile")   
                        $ Party[0].Statup("Obed", 80, 5)
                        $ Party[0].Statup("Inbt", 90, 10) 
                        $ Party[1].Statup("Obed", 80, 5)
                        $ Party[1].Statup("Inbt", 90, 10) 
                        if Party[0] == RogueX:       
                                    ch_r "Great, sounds fun."                 
                        elif Party[0] == KittyX:        
                                    ch_k "Cool, sounds fun."                                        
                        elif Party[0] == EmmaX:          
                                    ch_e "Lovely. . ."                                   
                        elif Party[0] == LauraX:        
                                    ch_l "Nice."                     
                "Well then, I guess I'll stop." if Line in ("mn","yn"):
                        #They were unfavorable, so you gave up on it. 
                        $ Line = "nn"
                        $ Party[0].FaceChange("normal")
                        $ Party[1].FaceChange("normal")  
                        $ Party[0].Statup("Love", 90, 5)
                        $ Party[0].Statup("Inbt", 90, 5)  
                        $ Party[1].Statup("Love", 90, 5)
                        $ Party[1].Statup("Inbt", 90, 5)                                
                        if Party[0] == RogueX:       
                                        ch_r "Good to hear."                        
                        elif Party[0] == KittyX:        
                                        ch_k "Good, that wouldn't have been cool."                        
                        elif Party[0] == EmmaX:       
                                        ch_e "Probably for the best."                        
                        elif Party[0] == LauraX:        
                                        ch_l "Good."                    
                "I'm asking her in anyway." if Line in ("mn","yn"):
                        #if they were unfavorable, but you insist
                        pass
                    
                "Well, I'm going to pass anyway." if Line in ("ym","my","nm","ny","mm"):
                        #if they give you permission, but you aren't into it.
                        $ Line = "nn"
                        $ Party[0].FaceChange("sad")
                        $ Party[1].FaceChange("sad")  
                        $ Party[0].Statup("Obed", 50, 5) 
                        $ Party[1].Statup("Obed", 50, 5) 
                        if Party[0] == RogueX:       
                                        ch_r "Oh, ok."                        
                        elif Party[0] == KittyX:        
                                        ch_k "That's fine."                        
                        elif Party[0] == EmmaX: 
                                        ch_e "If you insist."                        
                        elif Party[0] == LauraX:        
                                        ch_l "Ok."
            #end player response to their feedback
            
            if Line == "yy" or Line == "nn":
                                pass
            elif len(Player.Harem) >= 3:
                                $ Party[0].FaceChange("smile",Eyes="side")
                                $ Party[1].FaceChange("smile",Eyes="side") 
                                $ Party[0].Statup("Obed", 90, 5)
                                $ Party[0].Statup("Inbt", 90, 5) 
                                if Party[0] == RogueX:                 
                                        ch_r "Oh, what's one more."
                                elif Party[0] == KittyX:      
                                        ch_k "We're building a real \"pride\" here."
                                elif Party[0] == EmmaX:      
                                        ch_e "I suppose one more can't hurt."
                                elif Party[0] == LauraX:     
                                        ch_l "Whatever."
                                $ Line = "yy"
            elif Line == "mn" or Line == "yn":
                    # if you said yes/maybe and they said no, but you insisted anyway 
                    $Count = 0
                    while Count < 2:
                        if ApprovalCheck(Party[Count], 1600) and Party[Count].GirlLikeCheck(Newbie) >= 500:
                                # She likes you enough to roll over
                                $ Party[Count].FaceChange("sadside")
                                $ Party[Count].Statup("Love", 90, -5)
                                $ Party[Count].Statup("Obed", 90, 10)
                                if Party[Count] == RogueX:                 
                                        ch_r "Fine, she's in."
                                elif Party[Count] == KittyX:      
                                        ch_k "Geeze, ok."
                                elif Party[Count] == EmmaX:      
                                        ch_e "I suppose we'll make room."
                                elif Party[Count] == LauraX:     
                                        ch_l "Whatever."
                                $ Line = "yy"
                        else:
                                # She doewsn't like you enough to roll over
                                $ Party[Count].FaceChange("angry",Eyes="side")
                                $ Party[Count].Statup("Love", 90, -25)
                                $ Party[Count].Statup("Inbt", 90, 10) 
                                if Party[Count] == RogueX:                 
                                        ch_r "I just don't like you that much, [RogueX.Petname]."
                                        ch_r "I'm out."
                                elif Party[Count] == KittyX:      
                                        ch_k "You aren't that cute, [KittyX.Petname]."
                                        ch_k "I'm done."
                                elif Party[Count] == EmmaX:      
                                        ch_e "Don't overestimate yourself, [EmmaX.Petname]."
                                        ch_e "We're done."
                                elif Party[Count] == LauraX:     
                                        ch_l "Too far, [LauraX.Petname]."
                                        ch_l "I'm out of here."
                                $ Party[Count].DrainWord("dating",0,0,1) #if "dating" in Party[Count].Traits:
                                $ Party[Count].Traits.append("ex")
                                $ Party[Count].Break[0] = 5 + Party[Count].Break[1] + Party[Count].Cheated
                                        
                                $ Player.Harem.remove(Party[Count])
                                call Remove_Girl(Party[Count])
                        $ Count += 1
            #end "she said no but you insisted"
        
        
        if Line == "yy":
                if Newbie.Tag + "No" in Player.Traits:                   
                        $ Player.Traits.remove(Newbie.Tag + "No")
                $ Player.DrainWord(Newbie.Tag + "No",0,0,1)
                $ Player.Traits.append(Newbie.Tag + "Yes")
                "You should give [Newbie.Name] a call."   
        else:     
                $ Player.Traits.append(Newbie.Tag + "No")
                                
        $ Party = []
        $Count = 0
        return
        
label Harem_Initiation(BO=[],BO2=[]):  
    # This is called when a new girl is added to the pack
    # it makes them more open to sexing each other. 
    $ BO = TotalGirls[:]  
    while BO:   
            $ BO2 = Player.Harem[:]  
            while BO2: 
                    if "poly " + BO2[0].Tag not in BO[0].Traits:
                                $ BO[0].Traits.append("poly " + BO2[0].Tag)
                    $ BO2.remove(BO2[0])
            $ BO.remove(BO[0])
    return
## end Harem _Start//////////////////////////////////////////////////////////


#start study session / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 

label Study_Session(BO=[]):                       
            #study events, girl is the lead girl in the scene
            $ Party = []
            
            $ BO = TotalGirls[:]  
            while BO:  
                    if BO[0].Loc == bg_current:
                            $ Party.append(BO[0])
                    $ BO.remove(BO[0])
            
            if not Party:
                "There's nobody here to study with."
                menu:
                    "Study anyway?"
                    "Yes":
                        $ Player.XP += 5
                        $ Round -= 30 if Round >= 30 else Round
                    "Never mind.":
                        pass
                return
                
            $ renpy.random.shuffle(Party)
            
            if Current_Time == "Night":                        
                    if EmmaX in Party:
                            ch_e "It's a little late for a study session, maybe tomorrow."
                    elif Party[0] == RogueX:
                            ch_r "It's a little late for studying, maybe tomorrow."
                    elif Party[0] == KittyX:
                            ch_k "It's kinda late for studying. . . Tomorrow?"
                    elif Party[0] == LauraX:
                            ch_l "It's late. Maybe tomorrow."
                    $ Party = []
                    return
            elif Round <= 30:         
                    if EmmaX in Party:
                            ch_e "I'm afraid I was just about to take a break, perhaps another time. . ."
                    elif Party[0] == RogueX:
                            ch_r "I don't know that there's time for that, maybe if we wait a bit. . ."
                    elif Party[0] == KittyX:
                            ch_k "I don't know that there's time for that, maybe if we wait a bit. . ."
                    elif Party[0] == LauraX:
                            ch_l "I was about to take a break, maybe wait a bit."                        
                    $ Party = []
                    return
                
            elif EmmaX in Party and len(Party) >= 2: 
                    ch_e "I suppose you could both use some work."
            else:
                    if EmmaX in Party:
                            ch_e "Very well."
                    elif Party[0] == RogueX:
                            ch_r "Sure."
                    elif Party[0] == KittyX:
                            ch_k "Sure."
                    elif Party[0] == LauraX:
                            ch_l "Fine." 
                        
            
            $ Player.RecentActions.append("study")
            $ Player.XP += 5
            $ Trigger = 0
            $ Line = renpy.random.choice(["you run you through some basic routines, it's fairly uneventful.", 
                    "You study up for the mutant biology test.", 
                    "You study for the math quiz.",
                    "You get bored and discuss student gossip instead.",
                    "You study for a few hours, that was fun.",
                    "You spend the next few hours studying the lit test.",
                    "You study for the game design course."]) 
            "[Line]"       
            $ Line = 0
            
            $ Party[0].Statup("Love", 80, 2)
            $ Party[0].XP += 5
            if len(Party) >= 2:
                    $ Party[1].Statup("Love", 80, 2)
                    $ Party[0].GLG(Party[1],700,5,1)
                    $ Party[1].GLG(Party[0],700,5,1)
                    $ Party[1].XP += 5
                    #raises both girl's likes of each other by 5 if they are under 70 
            
            $ D20 = renpy.random.randint(1, 20)   
            
            #There might be sexy time
            if len(Party) >= 2 and EmmaX in Party and "three" not in EmmaX.History:
                $ Line = "no"
                                                             
            if Line != "no" and D20 >= 10: 
                call Frisky_Study             
            else:
                # if there is no frisky stuff
                if EmmaX in Party:
                        ch_e "I'm afraid it's getting a bit late, we should wrap this up. . ."
                elif Party[0] == RogueX:
                        ch_r "It's getting a bit late, we should wrap this up. . ."
                elif Party[0] == KittyX:
                        ch_k "It's kinda late, we should probably stop. . ."
                elif Party[0] == LauraX:
                        ch_l "I'm bored now."            
                $ Player.XP += 5  
            $ Round -= 30 if Round >= 30 else Round
            $ Line = 0
            $ Party = []
            call Wait 
            call Girls_Location
            return
#End Study session  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 


#Start Frisky study session / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label Frisky_Study(Prime_Bonus=0,Second=0,Line=0,Second_Bonus=0):
            # Second is a potential second girl, (make sure to set if no second girl)
            # Prime_Bonus,Second_Bonus=0 is needed by the Datebreak code but does nothing   
            # Prime_Bonus is reappropriated to denote a second pass through
            
            call Shift_Focus(Party[0])
            
            if len(Party) >= 2:
                    $ Second = Party[1]                  
            
            if Party[0] == EmmaX and "classcaught" not in EmmaX.History:
                    #if you've never caught her having sex before. 
                    "[EmmaX.Name] leans close to you for a moment, but then catches herself and pulls back."
            elif Party[0] == EmmaX and Second and ("three" not in EmmaX.History or "taboo" not in EmmaX.History):
                    #if there's a second girl and Emma doesn't do threesomes yet
                    "[EmmaX.Name] starts to lean close to you, but then notices [Second.Name]."                                
                    $ Party[0].FaceChange("sly",1,Eyes="side")
                    "She stops immediately and looks a bit embarrassed."
            elif D20 > 17 and ApprovalCheck(Party[0], 1000) and Party[0].Blow > 5:
                    $ Line = "blow"
            elif D20 > 14 and ApprovalCheck(Party[0], 1000) and Party[0].Hand >= 5:
                    $ Line = "hand"
            elif D20 > 10 and (ApprovalCheck(Party[0], 1300) or (Party[0].Mast and ApprovalCheck(Party[0], 1000))) and Party[0].Lust >= 70:
                    $ Line = "masturbate" 
            elif D20 > 10 and ApprovalCheck(Party[0], 1200) and Party[0].Lust >= 30:   
                    $ Line = "strip"
            elif ApprovalCheck(Party[0], 700) and Party[0].Kissed > 1:
                    $ Line = "kissing"
            elif ApprovalCheck(Party[0], 500):        
                    $ Line = "snuggle" 
                    if Party[0] != LauraX or ApprovalCheck(Party[0], 700,"L"):
                            $ Line = "snuggle" 
                    else:
                            "[Party[0].Name] briefly rests against your shoulder, but then shakes herself and pulls back."
                            $ Line = 0 
            # End first phase
                                                
            if not Line and len(Party) >= 2 and not Prime_Bonus:
                        # this sends it back to the start if there is a second girl
                        # it swaps their order to give the second girl a chance
                        $ Party.reverse()
                        call Frisky_Study(1)               
                        return
            elif not Line or Line == "strip":    
                        pass
            elif Line == "blow":
                        $ Party[0].FaceChange("sly")
                        if Party[0] == KittyX:
                                "[KittyX.Name] reaches her hand through your textbook and you can feel it in your lap."
                                "She unzips you pants and pulls your dick out, stroking it slowly."
                                "She then dives her head under the book, and starts to lick it."   
                        else:
                                "[Party[0].Name] get predatory grin, and begins to unzip your pants."
                                "She pulls your dick out and pops it into her mouth."    
            elif Line == "hand":
                        $ Party[0].FaceChange("sly")
                        if Party[0] == KittyX:
                                "[KittyX.Name] reaches her hand through your textbook and you can feel it in your lap."
                                "She runs her finger along your erection, her hand passing through the jeans to touch your bare skin."
                                "She unzips you pants and pulls your dick out, stroking it slowly."  
                        else:
                                "[Party[0].Name] get predatory grin, and begins to unzip your pants."
                                "She pulls your dick out and begins to slowly stroke it."    
            elif Line == "masturbate":   
                        $ Party[0].FaceChange("sly", Eyes="side")
                        "[Party[0].Name] leans back a bit and starts to rub herself." 
                        $ Trigger = "masturbation"  
            elif Line == "kissing":
                        "[Party[0].Name] leans close to you, and leans in for a kiss."  
            elif Line == "snuggle":
                        "[Party[0].Name] leans close to you and you spend the rest of the study session nuzzled close."                        
                                                  
            
            if Line == "strip":
                    if Party[0] != EmmaX and EmmaX in Party and ApprovalCheck(EmmaX, 1200) and EmmaX.Lust >= 30:                        
                            $ Party.reverse()
                            # Emma always takes priority
                    call Group_Strip_Study 
            elif Line and len(Party) < 2:
                    #if sex stuff is happening but only one girl
                    call expression Party[0].Tag + "_SexAct" pass (Line) 
            elif Line:
                    #if something sexual is happening, checks if other girl is cool
                    if Line == "snuggle":
                                call Date_Sex_Break(Party[0],Second,2)
                                if _return == 3:
                                        "[Second] glowers at you a bit."  
                                        $ Party[0].GLG(Second,700,5,1)
                                        $ Second.GLG(Party[0],700,5,1)
                    else:
                                call Date_Sex_Break(Party[0],Second)
                                
                    if _return == 4:
                            if Line == "blow":
                                    "[Party[0].Name] lets your dick fall out of her mouth."
                                    "You zip your pants back up." 
                            elif Line == "hand":
                                    "[Party[0].Name] lets your dick drop into your lap"
                                    "You zip your pants back up." 
                            else:                                
                                    "[Party[0].Name] stops what she's doing."
                                    
                            $ Party[0].FaceChange("sad")
                            if Party[0] == RogueX:
                                    ch_r "Buzzkill."
                            elif Party[0] == KittyX:
                                    ch_k "Booo."
                            elif Party[0] == EmmaX:
                                    ch_e "Oh, very well." 
                            elif Party[0] == LauraX:
                                    ch_l "Be that way."                                           
                    elif Line != "snuggle":
                        #Plays if you didn't refuse to stop
                        #either the other girl left, or it just continues with both
                        if _return == 3:
                                #if the other girl took off. . .
                                if Party[0] == RogueX:
                                    menu:
                                        ch_r "Mind if I continue?"
                                        "Go ahead.":
                                                ch_r "Nice."
                                        "We should stop.":
                                                ch_r "Hmph."
                                                return
                                elif Party[0] == KittyX:
                                    menu:
                                        ch_k "I can keep going?"
                                        "Go ahead.":
                                                ch_k "Cool."
                                        "We should stop.":
                                                ch_k "Lame."
                                                return
                                elif Party[0] == EmmaX:
                                    menu:
                                        ch_e "You don't mind if I continue?"
                                        "Go ahead.":
                                                ch_e "Lovely."
                                        "We should stop.":
                                                ch_e "Spoil sport."
                                                return
                                elif Party[0] == LauraX:
                                    menu:
                                        ch_l "Keep going?"
                                        "Go ahead.":
                                                ch_l "Un."
                                        "We should stop.":
                                                ch_l "Grr."
                                                return
                        call expression Party[0].Tag + "_SexAct" pass (Line) 
                    if len(Party) >= 2:                        
                        $ Party[0].GLG(Party[1],900,10,1)
                        $ Party[1].GLG(Party[0],900,10,1)
                        #if still two girls, raise both likes by 10
            else:
                        #if nothing sexy happened. . .
                        return
            $ Party[0].AddWord(1,0,0,0,"frisky")
            if len(Party) >= 2: 
                    $ Party[1].AddWord(1,0,0,0,"frisky")
                    
            "Well that was certainly a productive use of your study time. . ."    
            return
            
#end Frisky study session / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 


label Girls_Caught(Girl=0,TotalCaught=0,Shame=0,Count=0,T_Pet=0,BO=[]):
    $ TotalCaught = RogueX.Caught + KittyX.Caught + EmmaX.Caught + LauraX.Caught
    call Shift_Focus(Girl)
    call Checkout 
    call AnyLine(Girl,"!!!") 
    $ Line = Trigger
    $ Trigger = 0
    $ Trigger2 = 0
    $ Trigger3 = 0
    $ Trigger4 = 0
    $ Trigger5 = 0
    $ Girl.OutfitChange()
    $ BO = TotalGirls[:]  
    while BO:   
            if BO[0].Loc == bg_current:
                    $ BO[0].Loc = "bg study"
            $ BO.remove(BO[0])
    $ bg_current = "bg study"  
    call Set_The_Scene(0)
    show Professor at SpriteLoc(StageLeft)    
    
    if Girl == RogueX:        
            show Rogue_Sprite at SpriteLoc(StageRight) with ease
    elif Girl == KittyX:        
            show Kitty_Sprite at SpriteLoc(StageRight) with ease
    elif Girl == EmmaX:      
            show Emma_Sprite at SpriteLoc(StageRight) with ease
    elif Girl == LauraX:
            show Laura_Sprite at SpriteLoc(StageRight) with ease
    call OutfitShame(Girl,20)
            
    $ Count = Girl.Caught
    
    if Partner == RogueX:         
            show Rogue_Sprite at SpriteLoc(StageFarRight) with ease
    if Partner == KittyX:         
            show Kitty_Sprite at SpriteLoc(StageFarRight) with ease
    if Partner == EmmaX:         
            show Emma_Sprite at SpriteLoc(StageFarRight) with ease
    if Partner == LauraX:         
            show Laura_Sprite at SpriteLoc(StageFarRight) with ease
        
    call XavierFace("shocked")
    $ Girl.FaceChange("sad")
    if Girl == EmmaX or Partner == EmmaX:        
            ch_x "I'm very disappointed in your behavior, particularly yours, Emma."
    else:
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
            
    if Girl.Shame >= 40:
            ch_x "[Girl.Name], my dear, you're practically naked! At least throw a towel on!"
            "He throws [Girl.Name] the towel."
            show blackscreen onlayer black 
            $ BO = TotalGirls[:]  
            while BO:   
                    if BO[0].Loc == bg_current:
                            $ BO[0].Over = "towel"  
                    $ BO.remove(BO[0])
            hide blackscreen onlayer black
    elif Girl.Shame >= 20:
            ch_x "[Girl.Name], my dear, that attire is positively scandalous."
    
    if Girl.Caught:
            #if Caught for Girl > 0
            "And this isn't even the first time this has happened!"
    
    if Partner:
            $ Partner.FaceChange("surprised",2)
            if Partner in Rules:
                    if Partner == KittyX:
                        "Xavier glances over at [KittyX.Name], who just waggles her phone. . ."
                    elif Partner == LauraX:                    
                        $ Laura_Arms = 2
                        "Xavier glances over at [LauraX.Name], who raises her fist and shakes it. . ."
                        $ Laura_Arms = 1
                    ch_x "And. . .hm, I could have sworn there was someone else. . ."  
            else:
                    ch_x "And [Partner.Name], you were just watching this occur!"        
            $ Partner.FaceChange("bemused",1, Eyes="side")
                     
    if EmmaX.Loc == bg_current and EmmaX not in Rules:
        if not EmmaX.Caught:
                ch_x "Emma, you are entrusted as a teacher here, I can't have you fraternizing with the students."
                ch_x "This is especially true in the school's public spaces!"
                ch_x "What sort of message does that send?"
                ch_x "How appropriate would it be if I were to just wander the halls with Miss Grey on my lap?"
                call XavierFace("hypno")
                ch_x "Just. . . running my hands along her firm little body without a care in the world. . ."
                call XavierFace("happy")
                ch_x ". . ."
                call XavierFace("shocked")
                ch_x "Yes, well, as I was saying! . ."
        else:
                ch_x "Emma, I don't believe this is the first time we've had this talk."
                ch_x "I should hope it will be the last."    
            
    $ Line = 0        
    menu:
        ch_x "Well what have you to say for yourselves?"
        "Sorry sir, won't do it again.":
                if RogueX.Loc == bg_current and RogueX.Caught < 3:                   
                            $ RogueX.Statup("Love", 70, 20)           
                            $ RogueX.Statup("Inbt", 50, -15)             
                            $ RogueX.Statup("Love", 90, 5)
                if KittyX.Loc == bg_current and KittyX.Caught < 3:                   
                            $ KittyX.Statup("Love", 70, 10)
                            $ KittyX.Statup("Inbt", 30, -25)            
                            $ KittyX.Statup("Inbt", 50, -10)  
                if EmmaX.Loc == bg_current and EmmaX.Caught < 3:                   
                            $ EmmaX.Statup("Love", 70, 5)
                            $ EmmaX.Statup("Inbt", 30, -15) 
                if LauraX.Loc == bg_current and LauraX.Caught < 3:                       
                            $ LauraX.Statup("Inbt", 30, -20)            
                            $ LauraX.Statup("Inbt", 50, -10)               
                $ Girl.Statup("Obed", 50, -5)  
                    
                call XavierFace("happy")  
                if Girl.Caught:
                    ch_x "But you know you've done this before. . . at least [Girl.Caught] times. . ." 
                elif Girl == EmmaX and TotalCaught:
                    ch_x "Not with Ms. Frost, perhaps, but you know you've done this before. . ."
                    ch_x "at least [TotalCaught] times. . ." 
                    $ Girl.FaceChange("sexy",Brows="confused")    
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
        #End "sorry"
            
        "Just having a little fun, right [Girl.Pet]?":
                $ Girl.NameCheck() #checks reaction to petname
                $ Girl.FaceChange("bemused")  
                $ Girl.Statup("Lust", 90, 5)   
                if RogueX.Loc == bg_current and RogueX.Caught < 5:                  
                        $ RogueX.Statup("Love", 70, 20)
                        $ RogueX.Statup("Love", 90, 10)  
                if KittyX.Loc == bg_current and KittyX.Caught < 5:                
                        $ KittyX.Statup("Inbt", 90, 10)   
                        $ KittyX.Statup("Love", 90, 10) 
                if EmmaX.Loc == bg_current and EmmaX.Caught < 5:                   
                        $ EmmaX.Statup("Inbt", 90, 10)   
                        $ EmmaX.Statup("Love", 90, 10) 
                if LauraX.Loc == bg_current and LauraX.Caught < 5:               
                        $ LauraX.Statup("Inbt", 90, 10)   
                        $ LauraX.Statup("Obed", 90, 5)  
                        $ LauraX.Statup("Love", 90, 5) 
                    
                call XavierFace("angry")
                $ Count += 10
                ch_x "If that's your attitude, harsher methods might be necessary."
                if PunishmentX:
                    ch_x "I'm extending your punishment by [Count] days."
                else:
                    ch_x "I'm halving your daily stipend for [Count] days."   
                      
                if RogueX.Loc == bg_current and RogueX.Caught < 3:                   
                        $ RogueX.Statup("Obed", 50, 20)
                        $ RogueX.Statup("Obed", 90, 20)
                        $ RogueX.Statup("Inbt", 30, -20)
                        $ RogueX.Statup("Inbt", 50, -10) 
                if KittyX.Loc == bg_current and KittyX.Caught < 3:                    
                        $ KittyX.Statup("Obed", 50, 20)
                        $ KittyX.Statup("Obed", 90, 20)
                        $ KittyX.Statup("Inbt", 30, -20)  
                if EmmaX.Loc == bg_current and EmmaX.Caught < 3:                    
                        $ EmmaX.Statup("Obed", 50, 20)
                        $ EmmaX.Statup("Obed", 90, 20)
                        $ EmmaX.Statup("Inbt", 30, -20)   
                if LauraX.Loc == bg_current and LauraX.Caught < 3:               
                        $ LauraX.Statup("Obed", 50, 20)
                        $ LauraX.Statup("Obed", 90, 20)
                        $ LauraX.Statup("Inbt", 30, -20) 
                            
                ch_x "I've had enough of you, begone."
        #End "Little fun"
        
        "Just this. . . Plan Omega, [RogueX.Name]." if Girl == RogueX and Player.Lvl >= 5:
                $ Line = "Omega"            
        "Just this. . . Plan Kappa, [KittyX.Name]!" if Girl == KittyX and Player.Lvl >= 5:
                $ Line = "Kappa"                    
        "Just this. . . Plan Psi, [EmmaX.Name]!" if Girl == EmmaX and Player.Lvl >= 5:
                $ Line = "Psi"            
        "Just this. . . Plan Chi, [LauraX.Name]!" if Girl == LauraX and Player.Lvl >= 5:
                $ Line = "Chi"
        #End "Plan X"
                        
                        
        "You can suck it, old man.":
                $ Girl.FaceChange("surprised")
                $ Girl.Statup("Lust", 90, 10)                
                if RogueX.Loc == bg_current and RogueX.Caught < 3:                   
                        $ RogueX.Statup("Obed", 50, 20)
                        $ RogueX.Statup("Obed", 90, 40)  
                if KittyX.Loc == bg_current and KittyX.Caught < 3:                   
                        $ KittyX.Statup("Obed", 50, 25)
                        $ KittyX.Statup("Obed", 90, 40) 
                if EmmaX.Loc == bg_current and EmmaX.Caught < 3:        
                        $ EmmaX.Statup("Love", 90, 5) 
                        $ EmmaX.Statup("Obed", 50, 20)
                        $ EmmaX.Statup("Obed", 90, 30)  
                if LauraX.Loc == bg_current and LauraX.Caught < 3:       
                        $ EmmaX.Statup("Love", 90, 5)           
                        $ LauraX.Statup("Obed", 50, 25)
                        $ LauraX.Statup("Obed", 90, 30) 
                                            
                call XavierFace("angry")
                $ Count += 20
                ch_x "If that's your attitude, harsher methods might be necessary."
                if PunishmentX:
                    ch_x "I'm extending your punishment by [Count] days!"
                else:
                    ch_x "I'm halving your daily stipend for [Count] days!" 
                    
                if RogueX.Loc == bg_current and RogueX.Caught < 3:        
                        if RogueX.Inbt > 500:
                            $ RogueX.Statup("Inbt", 90, 15)             
                        $ RogueX.Statup("Inbt", 30, -20)
                        $ RogueX.Statup("Inbt", 50, -10)   
                if KittyX.Loc == bg_current and KittyX.Caught < 3:                  
                        if KittyX.Inbt > 500:
                            $ KittyX.Statup("Inbt", 90, 15)             
                        $ KittyX.Statup("Inbt", 30, -20)
                        $ KittyX.Statup("Inbt", 50, -10)   
                if EmmaX.Loc == bg_current and EmmaX.Caught < 3:                    
                        if EmmaX.Inbt > 500:
                            $ EmmaX.Statup("Inbt", 90, 15)             
                        $ EmmaX.Statup("Inbt", 30, -20)
                        $ EmmaX.Statup("Inbt", 50, -10)  
                if LauraX.Loc == bg_current and LauraX.Caught < 3:       
                        if LauraX.Inbt > 500:
                            $ LauraX.Statup("Inbt", 90, 15)             
                        $ LauraX.Statup("Inbt", 30, -15)
                        $ LauraX.Statup("Inbt", 50, -10) 
                            
                ch_x "Now get out of my sight."
        #End "suck it"
    
    if Line:
            if Line == "Omega":
                    if ApprovalCheck(RogueX, 1500, TabM=1, Loc="No"):                   
                            jump Xavier_Plan #Plan_Omega
                    elif ApprovalCheck(RogueX, 1000, TabM=1, Loc="No"):
                            $ Girl.FaceChange("perplexed",Brows = "sad")
                            ch_r "I'm not comfortable with something that extreme, [RogueX.Petname]. . ."
                            menu:
                                "Dammit [RogueX.Name]. . .":
                                        $ Girl.FaceChange("angry")
                                        $ RogueX.Statup("Obed", 50, 5)
                                        $ RogueX.Statup("Love", 90, -5) 
                                "Yeah, I guess you're right. . .":
                                        $ Girl.FaceChange("bemused") 
                    else:
                            $ Girl.FaceChange("confused") 
                            ch_r "What nonsense are you talking now?"
                            ch_p "Plan {i}Omega!{/i} . . you know. . ."
                            ch_r "Sounds like gibberish."
                            ch_p "Oh, yeah, I guess I haven't mentioned that. . ."
                            $ Girl.FaceChange("bemused") 
                    #End "Plan Omega"
            elif Line == "Kappa":
                    if "Xavier's photo" in Player.Inventory and ApprovalCheck(KittyX, 1500, TabM=1, Loc="No"):                   
                            jump Xavier_Plan #Plan_Kappa
                    elif ApprovalCheck(KittyX, 1000, TabM=1, Loc="No"):
                            $ Girl.FaceChange("perplexed",Brows = "sad")
                            if "Xavier's photo" in Player.Inventory:
                                    ch_k "You know. . . I really don't think that's a good idea. . ."
                            elif "kappa" in Player.History:
                                    ch_k "Maybe if we came back later we could find something. . ." 
                            else:
                                    ch_k "We don't really have any way to pull that off atm. . ."      
                                    $ Player.History.append("kappa")
                            menu:
                                "Dammit [KittyX.Name]. . .":
                                        $ Girl.FaceChange("angry")
                                        $ KittyX.Statup("Obed", 50, 5)
                                        $ KittyX.Statup("Love", 90, -5) 
                                "Yeah, I guess you're right. . .":
                                        $ Girl.FaceChange("bemused") 
                                        $ KittyX.Statup("Love", 90, 5) 
                    else:
                            $ Girl.FaceChange("confused") 
                            ch_k "Wait, Plan what??"
                            ch_p "Plan {i}Kappa!{/i} . . you know. . ."
                            ch_k "I have no {i}idea{/i} what you're talking about."
                            ch_p "oh, yeah, I guess I haven't mentioned that. . ."
                            $ Girl.FaceChange("bemused") 
                    #End "Plan Kappa"
            elif Line == "Psi":
                    if ApprovalCheck(EmmaX, 1500, TabM=1, Loc="No"):                   
                            jump Xavier_Plan #Plan_Psi
                    elif ApprovalCheck(EmmaX, 1000, TabM=1, Loc="No"):
                            $ Girl.FaceChange("perplexed",Brows = "sad")
                            ch_e "Um, I don't believe we're quite at that point yet, [EmmaX.Petname]. . ."
                            menu:
                                "Dammit [EmmaX.Name]. . .":
                                        $ Girl.FaceChange("angry")
                                        $ EmmaX.Statup("Obed", 50, 5)
                                        $ EmmaX.Statup("Love", 90, -5) 
                                "Yeah, I guess you're right. . .":
                                        $ Girl.FaceChange("bemused") 
                    else:
                            $ Girl.FaceChange("confused") 
                            ch_e "Lord child, what are you talking about now?"
                            ch_p "Plan {i}Psi!{/i} . . you know. . ."
                            ch_e "I wish that I did."
                            ch_p "Oh, yeah, I guess I haven't mentioned that. . ."
                            $ Girl.FaceChange("bemused") 
                    #End "Plan Psi"
            elif Line == "Chi":        
                    if LauraX.Lvl >= 2 and ApprovalCheck(LauraX, 1500, TabM=1, Loc="No") and ApprovalCheck(LauraX, 750, "I"):                   
                            jump Xavier_Plan #Plan_Chi
                    elif ApprovalCheck(LauraX, 1000, TabM=1, Loc="No"):
                            $ Girl.FaceChange("angry",Eyes="side",Brows = "angry")
                            ch_l "I told you that was a stupid idea. . ."
                            menu:
                                "Dammit [LauraX.Name]. . .":
                                        $ Girl.FaceChange("angry")
                                        $ LauraX.Statup("Obed", 50, 5)
                                        $ LauraX.Statup("Love", 90, -5) 
                                "Yeah, I guess you're right. . .":
                                        $ Girl.FaceChange("bemused") 
                                        $ LauraX.Statup("Love", 90, 5) 
                    else:
                            $ Girl.FaceChange("confused") 
                            ch_l "Yeah!"
                            ch_l ". . ."
                            ch_l "Wait, plan \"key,\" what??"
                            ch_p "Plan {i}Chi!{/i} . . you know. . ."
                            ch_l "Um. No?"
                            ch_p "oh, yeah, I guess I haven't mentioned that. . ."
                            $ Girl.FaceChange("bemused") 
                    #End "Plan Chi"
             
            # if the plan falls through. . .
            call XavierFace("angry")
            $ Count += 10
            ch_x "I have no idea what that was about, but it sounds like you haven't learned."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."    
                
                if RogueX.Loc == bg_current and RogueX.Caught < 3:                 
                        $ RogueX.Statup("Obed", 50, 10)
                        $ RogueX.Statup("Obed", 90, 10)
                        $ RogueX.Statup("Inbt", 30, -10)
                        $ RogueX.Statup("Inbt", 50, -5)    
                if KittyX.Loc == bg_current and KittyX.Caught < 3:                 
                        $ KittyX.Statup("Obed", 50, 10)
                        $ KittyX.Statup("Obed", 90, 10)
                        $ KittyX.Statup("Inbt", 30, -10)
                        $ KittyX.Statup("Inbt", 50, -5)    
                if EmmaX.Loc == bg_current and EmmaX.Caught < 3:                   
                        $ EmmaX.Statup("Obed", 50, 10)
                        $ EmmaX.Statup("Inbt", 50, -5) 
                if LauraX.Loc == bg_current and LauraX.Caught < 3:  
                        $ LauraX.Statup("Obed", 50, 10)
                        $ LauraX.Statup("Obed", 90, 10)
                        $ LauraX.Statup("Inbt", 30, -10)
                        $ LauraX.Statup("Inbt", 50, -5)   
            ch_x "I've had enough of you, begone."
    #End "evil plans"            
                
    if Girl == KittyX and KittyX not in Rules and "Xavier's photo" not in Player.Inventory:
            "It would probably be a good idea to find some way to get Xavier to leave you alone."
            "There probably isn't a way available right now though. . ."
            if KittyX.Caught > 1: 
                "Maybe I should try searching the office when he's not around."
            if KittyX.Caught > 2:
                "I bet [KittyX.Name] could help me get in."
            if KittyX.Caught > 3:
                "I bet there's something in that lefthand drawer. . ."
    elif Girl == EmmaX:        
            ch_x "Emma, I'd like you to stay after for a brief discussion about \"boundaries\". . ."
            if EmmaX.Caught:
                    $ EmmaX.Statup("Love", 90, -5) 
                    $ Girl.FaceChange("angry",Eyes="closed")
                    ch_e "Not again. . ."
                
    $ PunishmentX += Count     
    
    $ Girl.Caught += 1
    $ Girl.AddWord(0,"caught","caught") #recent and daily            
    call Remove_Girl("All")  
    "You return to your room"
    hide Professor
    $ bg_current == "bg player"
    jump Misplaced
#End Caught / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Xavier_Plan(Girl=0):    
    if "Xavier" in Player.DailyActions:
            "The Professor seems pretty out of it."
            "You don't think you'll be able to get anything more out of him today."
            "You leave him to it."
            $ bg_current = "bg player"   
            jump Misplaced
    
    if Girl not in TotalGirls:
        $ Girl = Ch_Focus
    call Shift_Focus(Girl)
    $ Girl.FaceChange("sly")         
    "As you say this, a sly grin crosses [Girl.Name]'s face."
    "You quickly approach Xavier and place your hands on his head."
    call XavierFace("psychic")
    ch_x ". . ."
    call XavierFace("shocked")
    "Xavier realizes with a shock that with your powers, his telepathy is useless."  
    
    if Partner:
            if Partner == RogueX and "Omega" not in Player.Traits:        
                    $ Line = "first"
            elif Partner == KittyX and "Kappa" not in Player.Traits:        
                    $ Line = "first"
            elif Partner == EmmaX and "Psi" not in Player.Traits:          
                    $ Line = "first"
            elif Partner == LauraX and "Chi" not in Player.Traits:           
                    $ Line = "first"
            
            if Line == "first":
                #if the Partner has never done this. . .
                if ApprovalCheck(Partner, 1000):
                        #if she's cool with it.
                        $ Partner.FaceChange("surprised")      
                        "[Partner.Name] looks a bit caught off guard, but goes along with the idea."        
                        $ Partner.FaceChange("sly")
                else:
                        $ Partner.FaceChange("surprised")      
                        "[Partner.Name] looks a bit uncomfortable with what's happening and takes off." 
                        call Remove_Girl(Partner)
                    
            else:
                        $ Partner.FaceChange("sly")      
                        "[Partner.Name] understands what's going on here."     
    #end partner response
            
    call XavierFace("angry")    
    if Girl == RogueX:
            $ RogueX.Arms = 0
            $ RogueX.ArmPose = 2
            show Rogue_Sprite at SpriteLoc(StageLeft+100,85) zorder 24 with ease
            "[RogueX.Name] moves in and also grabs his head, duplicating his powers as he watches helplessly."
            "Now that she posesses his full power, while his are negated, he has no defenses."              
            call XavierFace("hypno")                
            if "Omega" in Player.Traits:
                    ch_x "Oh, not again."
                    ch_x "What is it you want this time?"  
                    $ RogueX.Statup("Obed", 80, 3)
                    $ RogueX.Statup("Inbt", 70, 1)
            else:
                    $ RogueX.Statup("Obed", 50, 40)
                    $ RogueX.Statup("Inbt", 70, 20) 
            ch_r "Well, [RogueX.Petname], what would you like to do with this opportunity?"
            ch_r "I think we'll only get three tries at this. . ."
    elif Girl == KittyX: 
            $ KittyX.ArmPose = 2
            show Kitty_Sprite at SpriteLoc(StageLeft+100,150) with ease
            $ KittyX.SpriteLoc = StageCenter
            "[KittyX.Name] moves in sits on his lap, pinning his arms to the chair."     
            if "Kappa" in Player.Traits:
                    ch_x "Oh, not again."
                    ch_x "What is it you want this time?"
                    $ KittyX.Statup("Obed", 80, 3)
                    $ KittyX.Statup("Inbt", 70, 1)  
            else:
                    ch_x "What is the meaning of this? Unhand me!"
                    "You pull out the photo you found earlier in his study."
                    $ KittyX.Statup("Obed", 50, 40)
                    $ KittyX.Statup("Inbt", 70, 30)
                    ch_p "I have here a rather. . . compromising photo of you and Mystique."
                    ch_p "I was thinking maybe you could cut me a little slack around here."
                    ch_x "And if I do not?"
                    ch_p "[KittyX.Name] here's set it to distribute to every computer in school, every day."
                    ch_p "And only I know the password." 
                    ch_x "Very well. . . I'll forget about your punishment."
                    ch_p "Oh, I think we can do a bit better than that. . ." 
                    $ KittyX.Statup("Obed", 200, 30)
                    $ KittyX.Statup("Inbt", 200, 10)  
            ch_k "Well, [KittyX.Petname], what should we ask for?"
    elif Girl == EmmaX:    
            show Emma_Sprite at SpriteLoc(StageLeft+100,85) zorder 24 with ease
            "[EmmaX.Name] moves behind Xavier and activates her own telepathy."
            call XavierFace("angry")
            if "Psi" in Player.Traits:
                    ch_x "Oh, not again. . ."
                    $ EmmaX.Statup("Obed", 80, 3)
                    $ EmmaX.Statup("Inbt", 80, 1)  
            else:
                    $ EmmaX.Statup("Obed", 50, 40)
                    $ EmmaX.Statup("Inbt", 70, 30)
                    $ EmmaX.Statup("Obed", 200, 30)
                    $ EmmaX.Statup("Inbt", 200, 10)  
            ch_e "Well, [EmmaX.Petname], what should we ask for?" 
    elif Girl == LauraX:
            $ LauraX.ArmPose = 2
            if "Chi" in Player.Traits:
                    ch_x "Oh, not again."
                    $ LauraX.Claws = 1
                    ch_x "What is it you want this time?"
                    $ LauraX.Statup("Obed", 80, 3)
                    $ LauraX.Statup("Inbt", 80, 1)   
            else:        
                    ch_x "What is the meaning of this? Unhand me!"
                    ch_p "[LauraX.Name] and I were talking, and it seems like neither of us appreciates you bothering us."
                    ch_x "And if I continue?"
                    ch_p "My little [LauraX.Pet] here has a very particular set of skills, you know. . ."
                    $ Girl.NameCheck() #checks reaction to petname
                    $ LauraX.Claws = 1
                    $ Girl.FaceChange("sly")     
                    ch_p "She could cause a lot of trouble if she keeps getting called down here. . ."
                    "[LauraX.Name] draws her claws along the arm of the Professor's chair, tracing fine lines into the metal." 
                    ch_x "Very well. . . I'll forget about your punishment."
                    ch_p "Oh, I think we can do a bit better than that. . ." 
                    $ LauraX.Statup("Obed", 50, 40)
                    $ LauraX.Statup("Inbt", 80, 30)
                    $ LauraX.Statup("Obed", 200, 30)
                    $ LauraX.Statup("Inbt", 200, 10)  
            ch_l "Well, [LauraX.Petname], what should we ask for?"
            
    $ Count = 3
    $ PunishmentX = 0
    while Count > 0:
        $ Count -= 1
        menu:
            ch_x "What do you want?"
            "Don't bother us anymore when we're having fun." if Girl not in Rules:
                    ch_x "Very well. . . I could offer you some. . . discretion. . ."
                    $ Rules.append(Girl)
            "You know, it's kinda fun dodging you, catch us if you can." if Girl in Rules:
                    ch_x "If you. . . want me to, I suppose. . ."
                    $ Rules.remove(Girl)
                    
            "Raise my stipend." if Player.Income < 30:
                    if Girl == RogueX and "Omega" not in Player.Traits:    
                            ch_x "Very well. . . but I can only raise it by so much. . ."        
                            $ Player.Income += 2
                    elif Girl == KittyX and "Kappa" not in Player.Traits:    
                            ch_x "Very well. . . but I can only raise it by so much. . ."        
                            $ Player.Income += 2
                    elif Girl == EmmaX and "Psi" not in Player.Traits:    
                            ch_x "Very well. . . but I can only raise it by so much. . ."        
                            $ Player.Income += 2
                    elif Girl == LauraX and "Chi" not in Player.Traits:    
                            ch_x "Very well. . . but I can only raise it by so much. . ."        
                            $ Player.Income += 2
                    else:                
                            ch_x "I'm afraid I can't manage any more than I have. . ."
                            $ Count += 1
            "Raise my stipend. [[Used](locked)" if Player.Income >= 30:           
                    pass
            
            "There's this girl that's been bothering me. . .":
                    "This will send a girl away, temporarily removing her from the game."
                    "You can always ask to bring her back later."
                    $ Line = 0
                    menu:
                        ch_p "Could you get rid of. . ."
                        "[RogueX.Name]" if RogueX in ActiveGirls:
                                $ Line = RogueX
                        "[KittyX.Name]" if KittyX in ActiveGirls:
                                $ Line = KittyX
                        "[EmmaX.Name]" if EmmaX in ActiveGirls:
                                $ Line = EmmaX
                        "[LauraX.Name]" if LauraX in ActiveGirls and "dress0" not in LauraX.History:
                                $ Line = LauraX
                        "Never mind. . .":
                                $ Count += 1
                    if Line:
                            #if you picked someone. . .
                            ch_x "Very well, I suppose I can keep her occupied with various tasks around the campus. . ."
                            ch_x "She should be out of your hair for the time being."
                            if Line.Loc == bg_current:
                                    #if she's in the room
                                    $ Line.Statup("Love", 90, -10) 
                                    $ Line.Statup("Obed", 50, 3) 
                                    if Line == RogueX:
                                            ch_r "What do you mean, I'm \"bothering\" you?"
                                    elif Line == KittyX:
                                            ch_k "Hey, what gives?!"
                                    elif Line == EmmaX:
                                            ch_e "Excuse me? I must not have heard that right."
                                    elif Line == LauraX:
                                            ch_l "Explain."
                                    menu:
                                        extend ""
                                        "Oh, sorry, never mind.":
                                                $ Line = 0
                                                if ApprovalCheck(Line, 2000):
                                                        #if she accepts it
                                                        $ Line.FaceChange("confused")
                                                        $ Line.Statup("Love", 90, 3) 
                                                        $ Line.Statup("Obed", 50, 2) 
                                                        if Line == RogueX:
                                                                ch_r "Right. . ."
                                                        elif Line == KittyX:
                                                                ch_k "Uh-huh?"
                                                        elif Line == EmmaX:
                                                                ch_e ". . . right. . ."
                                                        elif Line == LauraX:
                                                                ch_l "If you say so."
                                                else:
                                                        #if she's mad
                                                        $ Line.FaceChange("angry")
                                                        $ Line.Statup("Obed", 50, -2) 
                                                        $ Line.Statup("Inbt", 60, 3) 
                                                        if Line == RogueX:
                                                                ch_r "Damned right you are."
                                                        elif Line == KittyX:
                                                                ch_k "Yeah, right."
                                                        elif Line == EmmaX:
                                                                ch_e "I don't know what you were thinking."
                                                        elif Line == LauraX:
                                                                ch_l "Uh. . . huh."
                                        "Sorry, but I just need some \"me\" time.":
                                                $ ActiveGirls.remove(Line)
                                                $ Line.Statup("Obed", 50, 5) 
                                                $ Line.Statup("Obed", 90, 2) 
                                                $ Line.Statup("Inbt", 60, 2) 
                                                if ApprovalCheck(Line, 900, "L") or ApprovalCheck(Line, 2000):
                                                        #if she accepts it
                                                        $ Line.FaceChange("sadside")
                                                        if Line == RogueX:
                                                                ch_r "I suppose if you do, I can give you some space."
                                                        elif Line == KittyX:
                                                                ch_k "I guess we both could. . ."
                                                        elif Line == EmmaX:
                                                                ch_e "I wouldn't want to be a bother. . ."
                                                        elif Line == LauraX:
                                                                ch_l "I can make myself scarce. . ."
                                                else:
                                                        #if she's mad
                                                        $ Line.Statup("Love", 90, -5) 
                                                        $ Line.FaceChange("angry")
                                                        $ Line.AddWord(1,"angry","angry")
                                                        if Line == RogueX:
                                                                ch_r "Oh, I think you'll be getting it."
                                                        elif Line == KittyX:
                                                                ch_k "Yeah, \"me\" too, I guess!"
                                                        elif Line == EmmaX:
                                                                ch_e "I do have other things with which to occupy myself."
                                                        elif Line == LauraX:
                                                                ch_l "I'm busy too."
                                        "You heard me.": 
                                                $ ActiveGirls.remove(Line)
                                                $ Line.Statup("Love", 80, -5) 
                                                $ Line.Statup("Love", 90, -5)
                                                $ Line.Statup("Obed", 80, 5) 
                                                if ApprovalCheck(Line, 850, "O") or ApprovalCheck(Line, 1500, "LO"):
                                                        #if she accepts it
                                                        $ Line.FaceChange("sadside")
                                                        $ Line.Statup("Obed", 200, 10) 
                                                else:
                                                        #if she's mad
                                                        $ Line.FaceChange("angry")
                                                        $ Line.Statup("Love", 90, -5) 
                                                        $ Line.Statup("Inbt", 60, 5) 
                                                        $ Line.AddWord(1,"angry","angry")
                                                if Line == RogueX:
                                                        ch_r "Loud and clear."
                                                elif Line == KittyX:
                                                        ch_k ". . ."
                                                elif Line == EmmaX:
                                                        ch_e "I suppose I did."
                                                elif Line == LauraX:
                                                        ch_l "If you say so."
                                    #end "picked same girl
                    if Line == Girl:
                        call AnyLine(Girl,"Did you forget that I'm your escape plan?")
                        menu:
                            "Oh. . .":
                                    ch_x "I'll forget you asked."
                                    $ Count = 0
                    $ Line = 0
            #end "remove girl"       
                   
            "I wanted to bring a girl back in. . ." if len(TotalGirls) > len (ActiveGirls):
                    "This will bring the girl back into active play."
                    "You can always ask to send her away again later."
                    $ Line = 0
                    menu:
                        ch_p "Could you bring back. . ."
                        "[RogueX.Name]" if RogueX not in ActiveGirls and RogueX in TotalGirls:
                                $ Line = RogueX
                        "[KittyX.Name]" if KittyX not in ActiveGirls and KittyX in TotalGirls:
                                $ Line = KittyX
                        "[EmmaX.Name]" if EmmaX not in ActiveGirls and EmmaX in TotalGirls:
                                $ Line = EmmaX
                        "[LauraX.Name]" if LauraX not in ActiveGirls and LauraX in TotalGirls and "dress0" not in LauraX.History:
                                #Laura has a special condition because of her introduction story
                                $ Line = LauraX
                        "Never mind. . .":
                                $ Count += 1
                    if Line:
                            #if you picked someone. . .
                            ch_x "Certainly. I've kept her busy, but I can let her off the hook. . ."
                            ch_x "She should have more free time now. . ."
                            $ ActiveGirls.append(Line)                                
                    $ Line = 0
            "In was interested in a key. . . ":
                menu:
                    "Give me the key to your study." if "Xavier" not in Keys:  
                            ch_x "Fine, take it. . ."  
                            $ Keys.append("Xavier")
                    "Give me the key to your study.[[Owned] (locked)" if "Xavier" in Keys:  
                            pass
                            
                    "Give me the key to [Girl.Name]'s room." if Girl not in Keys:  
                            ch_x "I. . . suppose I could do that. . ."  
                            $ Keys.append(Girl)
                    "Give me the key to [Girl.Name]'s room.[[Owned] (locked)" if Girl in Keys:  
                            pass
                    
                    "Never mind the keys.":
                            $ Count += 1
            "That should do it.":
                $ Count = 0
                
    ch_x "Very well, that should conclude our business. Please leave." 
    if Girl == RogueX:
            if "Omega" not in Player.Traits: 
                    $ RogueX.Statup("Lust", 90, 10)
                    $ RogueX.Statup("Love", 70, 30)
                    $ RogueX.Statup("Love", 200, 20)
                    $ Player.Traits.append("Omega")  
            ch_p "Ok, that's enough. Make Xavier forget that any of this happened, and then let's get out of here." 
            $ RogueX.Arms = "gloves"
            $ RogueX.ArmPose = 1
    elif Girl == KittyX:
            if "Kappa" not in Player.Traits:
                    $ KittyX.Statup("Lust", 90, 10)
                    $ KittyX.Statup("Inbt", 80, 10)
                    $ KittyX.Statup("Love", 70, 10)
                    $ KittyX.Statup("Love", 200, 20)
                    $ Player.Traits.append("Kappa")
            $ KittyX.ArmPose = 0
    elif Girl == EmmaX:
            ch_p "Ok, that's enough. Make Xavier forget that any of this happened, and then let's get out of here." 
            if "Psi" not in Player.Traits:
                    $ EmmaX.Statup("Lust", 90, 10)
                    $ EmmaX.Statup("Inbt", 80, 10)
                    $ EmmaX.Statup("Love", 70, 10)
                    $ EmmaX.Statup("Love", 200, 20)
                    $ Player.Traits.append("Psi")
    elif Girl == LauraX:
            if "Chi" not in Player.Traits:
                    $ LauraX.Statup("Lust", 90, 10)
                    $ LauraX.Statup("Inbt", 80, 10)
                    $ LauraX.Statup("Love", 70, 10)
                    $ LauraX.Statup("Love", 200, 20)
                    $ Player.Traits.append("Chi")
            $ LauraX.ArmPose = 1
            $ LauraX.Claws = 0
            
    $ Player.DailyActions.append("Xavier")
    call Remove_Girl("All")  
    hide Professor
    $ bg_current = "bg player"   
    call Set_The_Scene
    "You return to your room"
    jump Misplaced
                              
# end Caught / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Start Caught Changing/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Caught_Changing(Girl=0):
        if not Girl:
                return
        call Shift_Focus(Girl)
        $ D20 = renpy.random.randint(1, 20)
        
        $ Girl.FaceChange("surprised", 1,Mouth="kiss")
        
        if D20 > 17:        
                #She's naked
                $ Girl.OutfitChange("nude")
        else:
                #restore base outfit
                $ Girl.OutfitChange(6)                     
                if D20 >15:       
                        #She's bottomless
                        $ Girl.Legs = 0 #Legs
                        $ Girl.Panties = 0 #Panties
                elif D20 >14:       
                        #She's Topless
                        $ Girl.Chest = 0 #Over
                        $ Girl.Over = 0 #Chest
                elif D20 >10:       
                        #She's in her underwear
                        $ Girl.Over = 0 #Over
                        $ Girl.Legs = 0 #Legs
                elif D20 >5:        
                        #She's wearing pants/skirt but no shirt
                        $ Girl.Over = 0 #Over
        #else: #fully dressed
        call Set_The_Scene(Dress=0)
        if D20 > 17:        
                #She's naked
                "As you enter the room, you see [Girl.Name] is naked, and seems to be getting dressed."      
        elif D20 >14:       
                #She's Topless
                "As you enter the room, you see [Girl.Name] is practically naked, and seems to be getting dressed."  
        elif D20 >10:       
                #She's in her underwear
                "As you enter the room, you see [Girl.Name] is in her underwear, and seems to be getting dressed." 
        elif D20 >5:        
                #She's wearing pants/skirt
                "As you enter the room, you see [Girl.Name] has her top off, and seems to be getting dressed." 
        else:
                #She's done
                "As you enter the room, you see [Girl.Name] has just pulled her top on, and seems to have been getting dressed." 
             
        if D20 > 5: 
                if not ApprovalCheck(Girl, (D20 *70)) and Girl.SeenCheck() >= 3:
                        # if D20*70 is less than her approval, and this is the first you've seen of her bits. . .
                        $ Girl.FaceChange("surprised",Brows="angry")  
                        $ Girl.Statup("Love", 80, -50)
                        
                        if not Girl.OverNum() or (Girl.OverNum()+Girl.ChestNum() <5) or (Girl.PantsNum() < 5 and Girl.HoseNum() < 10):
                            # if either she is mostly topless or mostly bottomless)
                            $ Girl.Over = "towel"
                            "She grabs a towel and covers up."
                else:       
                        #She's cool with it, but confused.
                        $ Girl.FaceChange("surprised", 1,Brows = "confused")
                        if "exhibitionist" in Girl.Traits:
                            $ Girl.Statup("Lust", 200, (2*D20))  
                        else:
                            $ Girl.Statup("Lust", 200, D20)
                      
                $ Girl.Statup("Inbt", 70, 20)
                
                if D20 > 17:
                        call expression Girl.Tag + "_First_Bottomless"
                        call expression Girl.Tag + "_First_Topless" pass (1)
                elif D20 > 15:
                        call expression Girl.Tag + "_First_Bottomless"
                elif D20 > 14:
                        call expression Girl.Tag + "_First_Topless"
                   
                if Girl == RogueX:
                        ch_r "Hey! Learn to knock maybe?!"
                elif Girl == KittyX:
                        ch_k "Why didn't you knock?!"
                elif Girl == EmmaX:
                        ch_e "Did you consider knocking?"
                elif Girl == LauraX:
                        ch_l "Didn't think about knocking?"
                menu:
                    extend ""
                    "Sorry, I should have knocked.":  
                            $ Girl.Statup("Love", 50, 2)
                            $ Girl.Statup("Love", 80, 4)
                    "And miss the view?":
                            $ Girl.Statup("Obed", 50, 2)
                            $ Girl.Statup("Obed", 80, 2)
                            $ Girl.Statup("Inbt", 60, 1)
                #end if she's partially nude
        else:              
                #She's fully dressed      
                if not ApprovalCheck(Girl, 800) and not Girl.SeenCheck():            
                        $ Girl.FaceChange("angry",Brows="confused")
                        $ Girl.Statup("Love", 80, -5)
                else:
                        $ Girl.FaceChange("sexy",Brows="confused")
                $ Girl.Statup("Inbt", 50, 3)
                
                if Girl == RogueX:
                        ch_r "Well hello there, [RogueX.Petname]. Hoping to see something more?"
                elif Girl == KittyX:
                        ch_k "Hey, [KittyX.Petname]. . . {i}you{/i} were hoping I'd be naaaked."
                elif Girl == EmmaX:
                        ch_e "Were you hoping to catch me in a compromising position?."
                elif Girl == LauraX:
                        ch_l "Hey, [LauraX.Petname]. Trying to catch a peek?"
                        
                menu:
                    extend ""
                    "Sorry, I should have knocked.":   
                            $ Girl.Statup("Love", 50, 2)
                            $ Girl.Statup("Love", 80, 2)
                    "Well, to be honest. . .":
                            $ Girl.Statup("Love", 50, -2)
                            $ Girl.Statup("Obed", 50, 2)
                            $ Girl.Statup("Obed", 80, 2)
                            $ Girl.Statup("Inbt", 60, 1)
        $ Girl.FaceChange("sexy")
        if ApprovalCheck(Girl, 750) and Girl.SeenCheck():
                #she flashes you
                if Girl == RogueX:
                        ch_r "You could have just asked, [RogueX.Petname]."           
                elif Girl == KittyX:
                        ch_k "I didn't say that I {i}minded{/i}. . ."              
                elif Girl == EmmaX:
                        ch_e "That does show initiative. . ."                
                elif Girl == LauraX:
                        ch_l "I don't mind."
                                       
                $ Girl.Uptop = 1 #Uptop up                   
                $ Girl.Upskirt = 1 #Upskirt up
                pause 1      
                call expression Girl.Tag + "_First_Topless" pass (1)
                call expression Girl.Tag + "_First_Bottomless" pass (1)                   
                $ Girl.OutfitChange() #restore current outfit
                "She flashes you real quick."  
        else:
                #if she doesn't flash you
                if Girl == RogueX:
                        ch_r "Well, it happens, just be careful next time."  
                elif Girl == KittyX:
                        ch_k "Yeah. . . we wouldn't want any accidents. . ."  
                elif Girl == EmmaX:
                        ch_e "Hmm, show a bit more care next time. . ." 
                elif Girl == LauraX:
                        ch_l "Uh-huh . . ."  
        if Girl == RogueX: 
                ch_r "Well, are you planning to stick around?" 
        elif Girl == KittyX:
                ch_k "So were you planning on staying?" 
        elif Girl == EmmaX: 
                ch_e "Did you have business with me?" 
        elif Girl == LauraX:
                ch_l "So did you plan to stay?"  
        menu:
                extend ""
                "Sure, for a bit.":
                        pass
                "Actually, I should get going. . .":
                        $ Girl.OutfitChange(6,Changed=0)
                        $ renpy.pop_call()
                        call Worldmap      
        return
#End Girl Caught Changing


label Girl_Caught_Mastubating(Girl=0):
        #called by room entry dialog if the girl was masturbating
        if not Girl:
            return
        "As you approach her room, you hear soft moans from inside, and notice that the door is slightly ajar."
        menu:
            extend ""
            "Knock politely":
                $ Line = "knock"
            "Peek inside":
                call Set_The_Scene
                $ Girl.FaceChange("kiss",1,Eyes = "closed") 
                $ Trigger = "masturbation"
                $ Trigger3 = "fondle pussy"
                "You see [Girl.Name], eyes closed and stroking herself vigorously."
                menu:
                    extend ""
                    "Enter Quietly":
                            $ Line = "enter"
                    "Pull back and knock":                        
                            $ Line = "knock"
                    "Leave quietly":
                            $ Line = "leave"
            "Enter quietly":
                    $ Line = "enter"
            "Leave quietly":
                    $ Line = "leave"
        
        if Line == "leave":      
                $ Girl.Statup("Lust", 80, 20)
                "You leave [Girl.Name] to her business and slip out."
                $ renpy.pop_call()  
                jump Campus_Map 
        elif Line == "knock":
                "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
                "After several seconds and some more shuffling of clothing, [Girl.Name] comes to the door."
                $ Girl.FaceChange("confused",1,Eyes = "surprised",Mouth = "smile") 
                $ Trigger = 0
                $ Trigger3 = 0
                call Set_The_Scene            
                if Girl == RogueX:
                        ch_r "Sorry about that [RogueX.Petname], I was. . . working out."
                elif Girl == KittyX:
                        ch_k "Oh, hey, [KittyX.Petname], I was. . . never mind."
                elif Girl == EmmaX:
                        ch_e "Well, I suppose you could tell I was a bit. . . occupied."
                elif Girl == LauraX:                
                        ch_l "Um, hey [LauraX.Petname], just working off some stress."
                $ Tempmod += 10
        elif Line == "enter":
                call Shift_Focus(Girl)
                "You hear some odd noises coming from [Girl.Name]'s room as you enter."
                show blackscreen onlayer black 
                $ Girl.Upskirt = 1
                $ Girl.PantiesDown = 1 
                $ Girl.Loc = bg_current
                call CleartheRoom(Girl,1,1)
                call Set_The_Scene
                $ Girl.FaceChange("sexy")
                $ Girl.Eyes = "closed"
                $ Girl.ArmPose = 2
                $ Count = 0    
                $ Trigger = "masturbation"
                hide blackscreen onlayer black
                $ Girl.DailyActions.append("unseen") 
                $ Girl.RecentActions.append("unseen")    
                call expression Girl.Tag + "_SexAct" pass ("masturbate")
                if "angry" in Girl.RecentActions:
                        return
            
                #After caught masturbating. . .
                $ Girl.Eyes = "sexy"
                $ Girl.Brows = "confused"
                $ Girl.Mouth = "smile"
                if Girl.Mast == 1:        
                        if Girl == RogueX:
                                $ Girl.Mouth = "kiss"
                                ch_r "Well that was a bit unexpected. . ."
                                $ Girl.Eyes = "side"
                                $ Girl.Mouth = "lipbite"        
                                ch_r "but not exactly unpleasant. . ."
                                $ Girl.Eyes = "sexy"
                                $ Girl.Brows = "normal"         
                                $ Girl.Mouth = "smile"
                                ch_r "Maybe next time I'll give you a heads up first." 
                        elif Girl == KittyX:
                                $ Girl.Mouth = "kiss"
                                ch_k "So[KittyX.like]I wasn't expecting company. . ."
                                $ Girl.Eyes = "side"
                                $ Girl.Mouth = "lipbite"        
                                ch_k "but I didn't exactly mind it either. . ."
                                $ Girl.Eyes = "sexy"
                                $ Girl.Brows = "normal"         
                                $ Girl.Mouth = "smile"
                                ch_k "Maybe knock next time?" 
                        elif Girl == EmmaX:
                                $ Girl.Mouth = "kiss"
                                ch_e "I wasn't expecting visitors. . ."
                                $ Girl.Eyes = "side"
                                $ Girl.Mouth = "lipbite"        
                                ch_e "although for you I could make an exception. . ."
                                $ Girl.Eyes = "sexy"
                                $ Girl.Brows = "normal"         
                                $ Girl.Mouth = "smile"
                                ch_e "Perhaps next time you could knock?" 
                        elif Girl == LauraX:
                                $ Girl.Mouth = "kiss"
                                ch_l "So what are you doing here? . ."
                                $ Girl.Eyes = "side"
                                $ Girl.Mouth = "lipbite"        
                                ch_l "not that I mind the company. . ."
                                $ Girl.Eyes = "sexy"
                                $ Girl.Brows = "normal"         
                                $ Girl.Mouth = "smile"
                                ch_l "But you know, give me a heads up first." 
                else:         
                        if Girl == RogueX:
                                ch_r "Fancy seeing you here again, [Girl.Petname]. Almost like it was intentional. . ."
                        elif Girl == KittyX:
                                ch_k "You seem to be making a habit of dropping in."  
                        elif Girl == EmmaX:
                                ch_e "I notice you make a habit of dropping in." 
                        elif Girl == LauraX:
                                ch_l "You're around a lot. . ."  
                        
                $ Girl.ArmPose = 1  
                $ Girl.OutfitChange(Changed=0)
                #end "if you entered"
        return
    
#start girls caught lesing / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

        
label Girls_Caught_Lesing(Girl=0,Girl2=0,BO=[]):
        #called by room entry dialog if the girls were lesing
        
        $ BO = ActiveGirls[:]   
        if Girl:
                $ BO.remove(Girl)
        while BO and not Girl:      
                if BO[0] not in Party and BO[0].Loc == bg_current and "les" in BO[0].RecentActions:
                        # if this girl is not already the focal girl, is at the current location but not in a party, 
                        # and was queued for a les action, set her up as girl 1.
                        $ Girl = BO[0]
                        $ BO = [1]
                $ BO.remove(BO[0])
        if Girl and not Girl2:     
                #if a Girl was either offered or produced by first loop. . .
                $ BO = ActiveGirls[:]  
                $ BO.remove(Girl)
                while BO:      
                        if BO[0] not in Party and BO[0].Loc == bg_current and "les" in BO[0].RecentActions:
                                # if this girl is not already the focal girl, is at the current location but not in a party, 
                                # and was queued for a les action, set her up as girl 2.
                                $ Girl2 = BO[0]
                                $ BO = [1]
                        $ BO.remove(BO[0])
                                    
        if not Girl or not Girl2:
            return 1
            
        $ Girl.DrainWord("les",1,0) #removes general "les" tag from recent actions
        $ Girl2.DrainWord("les",1,0) #removes general "les" tag from recent actions
        
        $ Girl.AddWord(0,"lesbian","lesbian")  #adds "lesbian" tag to recent and daily actions 
        $ Girl2.AddWord(0,"lesbian","lesbian")  #adds "lesbian" tag to recent and daily actions    
        $ Girl.AddWord(1,0,0,0,"les "+Girl2.Tag)  #adds "les Rogue" tag to recent actions
        $ Girl2.AddWord(1,0,0,0,"les "+Girl.Tag)  #adds "les Kitty" tag to recent actions 
        
        "As you approach her room, you hear soft moans from inside, and notice that the door is slightly ajar."
        menu:
            extend ""
            "Knock politely":
                $ Line = "knock"
            "Peek inside":
                call Set_The_Scene
                $ Girl.FaceChange("kiss",1,Eyes = "closed") 
                $ Girl2.FaceChange("kiss",1,Eyes = "closed") 
                $ Trigger = "lesbian"
                $ Trigger3 = "fondle pussy"
                $ Trigger4 = "fondle pussy"
                "You see [Girl.Name] and [Girl2.Name], eyes closed and stroking each other vigorously."
                menu:
                    extend ""
                    "Enter Quietly":
                            $ Line = "enter"
                    "Pull back and knock":                        
                            $ Line = "knock"
                    "Leave quietly":
                            $ Line = "leave"
            "Enter quietly":
                    $ Line = "enter"
            "Leave quietly":
                    $ Line = "leave"
        
        if Line == "leave":      
                "You leave the girls to their business and slip out."
                $ Girl.Thirst -= 30 
                $ Girl.Lust = 20 
                $ Girl2.Thirst -= 30 
                $ Girl2.Lust = 20 
                $ renpy.pop_call()  
                jump Campus_Map 
        elif Line == "knock":
                "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
                "After several seconds and some more shuffling of clothing, [Girl.Name] comes to the door."
                $ Girl.FaceChange("confused",2,Eyes = "surprised",Mouth = "smile") 
                $ Girl2.FaceChange("confused",2,Eyes = "surprised",Mouth = "smile") 
                $ Trigger = 0
                $ Trigger3 = 0
                $ Trigger4 = 0
                $ Trigger5 = 0
                call Set_The_Scene            
                if Girl == RogueX:
                        ch_r "Sorry about that [RogueX.Petname], we were, um. . . working out."
                elif Girl == KittyX:
                        ch_k "Oh, hey, [KittyX.Petname], hi, we were. . . never mind."
                elif Girl == EmmaX:
                        ch_e "Well, I hope you have a good reason for interrupting us."
                        ch_e "I was. . . teaching her a few things. . ."
                elif Girl == LauraX:                
                        ch_l "Um, hey [LauraX.Petname], we were a bit busy."            
                $ Girl.FaceChange("smile",1) 
                $ Girl2.FaceChange("smile",1) 
                $ Tempmod += 10
        elif Line == "enter":
                call Set_The_Scene(Quiet=1)
                $ Girl.FaceChange("kiss",1,Eyes = "closed") 
                $ Girl2.FaceChange("kiss",1,Eyes = "closed") 
                $ Trigger = "lesbian"
                $ Trigger3 = "fondle pussy"
                $ Trigger4 = "fondle pussy"
                $ Girl.AddWord(1,"unseen","unseen") 
                $ Girl2.AddWord(1,"unseen","unseen")
                $ Partner = Girl2
                call expression Girl.Tag + "_SexAct" pass ("lesbian") #call Rogue_SexAct("lesbian")
        return
    
#end girls caught lesing / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


   
    
label Girl_Caught_Shower(Girl=0):  
        if not Girl:
                return
        call Shift_Focus(Girl)
        
        $ Girl.AddWord(1,"showered","showered",0,0)
        call Remove_Girl("All")
        
        $ Girl.OutfitChange("nude")
        $ Girl.FaceChange("smile",1) 
        
        $ Girl.Loc = "bg showerroom"              
        $ Girl.Water = 1
        $ Girl.Wet = 2
                        
        if "gonnafap" in Girl.DailyActions:
                "As you approach the showers, you hear some shallow moans from inside."
        else:
                "As you approach the showers, you hear some humming noises from inside." 
        menu:
                "What do you do?"
                "Enter":     
                    pass              
                "Knock":
                    $ Line = "knock"
                "Come back later": 
                    call Remove_Girl(Girl)
                    $ Girl.OutfitChange(6) #dresses her
                    $ Girl.DrainWord("gonnafap",0,1) #removes "gonnafap" tag from daily                    
                    $ Girl.Lust = 25
                    $ Girl.Thirst -= int(Girl.Thirst/2) if Girl.Thirst >= 50 else int(Girl.Thirst/4) 
                    return 1
                
        if Line == "knock":                                                                                         
                #You knock
                "You knock on the door. You hear some shuffling inside"    
                $ Girl.Over = "towel" 
                if "gonnafap" in Girl.DailyActions:                                    
                        #Girl caught fapping
                        "You hear a sharp shuffling sound and the water gets cut off."
                        "After several seconds and some more shuffling, [Girl.Name] comes to the door."
                        $ Girl.FaceChange("perplexed",2,Mouth="normal") 
                        call Set_The_Scene(Dress=0)
                        if Girl == RogueX: 
                                ch_r "Sorry about that [RogueX.Petname], I was. . . just wrapping up my shower."
                        elif Girl == KittyX:
                                ch_k "Oh, hey, [KittyX.Petname]. I was just. . . showering. Yeah."
                        elif Girl == EmmaX: 
                                ch_e "Oh, hello [EmmaX.Petname]. I was. . . taking care of some personal business."
                        elif Girl == LauraX: 
                                ch_l "Oh, hey [LauraX.Petname]. I was just. . . working off some stress."
                        $ Girl.Statup("Lust", 90, 5)
                        $ Tempmod += 10
                else:                                                                                                   
                        #Laura caught showering
                        "You hear the rustling of a towel and some knocking around, but after a few seconds [Girl.Name] comes to the door."
                        call Set_The_Scene(Dress=0)
                        if Girl == RogueX: 
                                ch_r "Sorry about that [RogueX.Petname], I was just wrapping up my shower."
                        elif Girl == KittyX:
                                ch_k "Oh, hey, [KittyX.Petname]. I was just[KittyX.like]showering."
                        elif Girl == EmmaX: 
                                ch_e "Oh, hello [EmmaX.Petname]. I was just finishing my shower."
                        elif Girl == LauraX: 
                                ch_l "Oh, hey [LauraX.Petname]. I was just finishing up."
                #end "knocked"
        else:                                                                                                       
            #You don't knock   
            if "gonnafap" in Girl.DailyActions:  
                    #Caught masturbating in the shower. 
                    $ Girl.DrainWord("gonnafap",0,1) #removes "gonnafap" tag from daily 
                    $ Girl.FaceChange("sexy",Eyes="closed")       
                    $ Girl.AddWord(1,"unseen","unseen",0,0) 
                    call Set_The_Scene(Dress=0)
                    $ Count = 0     
                    $ Trigger = "masturbation"
                    $ Trigger3 = "fondle pussy"   
                    "You see [Girl.Name] under the shower, feeling herself up."
                    call expression Girl.Tag + "_SexAct" pass ("masturbate") #call Laura_SexAct("masturbate")   
                    jump Shower_Room
                
            elif D20 >= 15:                                                                                         
                    #She's just showering and naked
                    call Set_The_Scene(Dress=0)                
                    $ Girl.FaceChange("surprised", 1)
                    "As you enter the showers, you see [Girl.Name] washing up."        
                    if not ApprovalCheck(Girl, 1200) or not Girl.SeenCheck():
                            $ Girl.Brows="angry"
                            $ Girl.Over = "towel"
                            "She grabs a towel and covers up."             
                            $ Girl.FaceChange("angry", 1)
                            $ Girl.Statup("Love", 80, -5) 
                    else:
                            if "exhibitionist" in Girl.Traits:
                                $ Girl.Statup("Lust", 90, (2*D20)) 
                            else:
                                $ Girl.Statup("Lust", 80, D20)         
                            $ Girl.Brows="confused"       
                    
                    call expression Girl.Tag + "_First_Bottomless" pass (1)
                    call expression Girl.Tag + "_First_Topless" pass (1)
                    $ Girl.Statup("Inbt", 70, 3)
                    if Girl == RogueX: 
                            ch_r "Hey! Learn to knock maybe?!"
                    elif Girl == KittyX:
                            ch_k "Did you[KittyX.like]get a good look?"
                    elif Girl == EmmaX: 
                            ch_e "Hello. Haven't you learned to knock before entering?"
                    elif Girl == LauraX: 
                            ch_l "Um, hey? Don't knock much?"
                    menu:
                            extend ""                            
                            "Sorry, I should have knocked.":  
                                    $ Girl.Statup("Love", 50, 2)
                                    $ Girl.Statup("Love", 80, 4)
                            "And miss the view?":
                                    $ Girl.Statup("Obed", 50, 2)
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 1)
                            "Why, would it have made a difference?": 
                                if not ApprovalCheck(Girl, 500,"I"):
                                    $ Girl.Statup("Love", 50, -3)
                                    $ Girl.Statup("Obed", 50, 2)
                                $ Girl.Statup("Obed", 80, 2)
                                $ Girl.Statup("Inbt", 60, 2)
                            "It's not as if you're leaving that much to the imagination. . ." if Girl == EmmaX: 
                                $ EmmaX.Statup("Obed", 50, 2)
                                $ EmmaX.Statup("Obed", 80, 2)
                                $ EmmaX.Statup("Inbt", 60, 2)
                    #end caught showering naked
                
            else:                                                                                   
                    #She's done showering and in a towel
                    $ Girl.Over = "towel"
                    call Set_The_Scene(Dress=0)
                    "As you enter the showers, you see [Girl.Name] putting on a towel."        
                    if not ApprovalCheck(Girl, 1100) and not Girl.SeenCheck():          
                            $ Girl.FaceChange("angry",Brows="confused")
                            $ Girl.Statup("Love", 80, -5)
                    else:
                            $ Girl.FaceChange("sexy",Brows="confused")
                    $ Girl.Statup("Inbt", 50, 3)
                    if Girl == RogueX: 
                            ch_r "Well hello there, [RogueX.Petname]. Hoping to see something more?"
                    elif Girl == KittyX:
                            ch_k "Oh, hey. Were you hoping I'd be naaaaaked?"
                    elif Girl == EmmaX: 
                            ch_e "Oh, hello, [EmmaX.Petname]. Sorry you didn't get here sooner?"
                    elif Girl == LauraX: 
                            ch_l "Oh, hey [LauraX.Petname]. Trying to slip in unnoticed?"
                    menu:
                            extend ""
                            "Sorry, I should have knocked.":   
                                    $ Girl.Statup("Love", 50, 2)
                                    $ Girl.Statup("Love", 80, 2)   
                            "Well, to be honest. . .":
                                    $ Girl.Statup("Love", 50, -2)
                                    $ Girl.Statup("Obed", 50, 2)
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 1)
                            "I still like the view. . ." if Girl != EmmaX: 
                                if ApprovalCheck(Girl, 500,"I"):
                                    $ Girl.Statup("Love", 80, 1)
                                else:
                                    $ Girl.Statup("Love", 50, -1)
                                    $ Girl.Statup("Obed", 50, 2)
                                $ Girl.Statup("Obed", 80, 2)
                                $ Girl.Statup("Inbt", 60, 3)
                            "It's not as if you're leaving that much to the imagination. . ." if Girl == EmmaX: 
                                $ EmmaX.Statup("Obed", 50, 2)
                                $ EmmaX.Statup("Obed", 80, 2)
                                $ EmmaX.Statup("Inbt", 60, 2)
                    #end caught in towel
                        
            $ Girl.FaceChange("sexy")          
            if not ApprovalCheck(Girl, 750) and Girl.SeenCheck(3):
                    if Girl == RogueX: 
                            ch_r "Well, it happens, just be careful next time."
                    elif Girl == KittyX:
                            ch_k "Well, it's not like I totally mind. . ." 
                    elif Girl == EmmaX: 
                            ch_e "Hmm. Yes, a likely excuse."
                    elif Girl == LauraX:   
                            ch_l "Well, just keep an eye on your own bits."
                            ch_l "Wouldn't want them going missing."
            elif not ApprovalCheck(Girl, 1300):                 
                    if Girl == RogueX: 
                            ch_r "Well, it happens, just be careful next time."
                    elif Girl == KittyX:
                            ch_k "Well too bad." 
                    elif Girl == EmmaX: 
                            ch_e "Hmm. Yes, a likely excuse."
                    elif Girl == LauraX:   
                            ch_l "Uh-huh."
            else:       
                    if Girl == RogueX: 
                            ch_r "You could have just asked, [RogueX.Petname]."   
                    elif Girl == KittyX:
                            ch_k "Well, it's not like it's totally off the table. . ." 
                    elif Girl == EmmaX: 
                            ch_e "Well, it's not that I mind. . ."
                    elif Girl == LauraX:   
                            ch_l "Nah, I don't mind much. . ."
                            
                    if Girl.Over == "towel": 
                            #if she's wearing a towel. . .       
                            $ Girl.Over = 0 #removes towel  
                            pause 0.5               
                            $ Girl.Over = "towel"
                            "She flashes you real quick."     
                            $ Girl.Over = "towel" 
                            call expression Girl.Tag + "_First_Bottomless" pass (1)
                            call expression Girl.Tag + "_First_Topless" pass (1) #same as "call Rogue_First_Topless(1)"
                            
                            if Girl == LauraX:   
                                    ch_l "Heh!" 
                                                          
            #end didn't knock
        
        if Girl == RogueX: 
                ch_r "Well, I should probably get going. . ." 
        elif Girl == KittyX:
                ch_k "I'm done here, see you later?" 
        elif Girl == EmmaX: 
                ch_e "I should probably be leaving. . ."
        elif Girl == LauraX:                    
                ch_l "I should get going. . ." 
        menu:
            extend ""
            "Sure, see you later then.":
                    call Remove_Girl(Girl)
            "Actually, could you stick around a minute?":
                if ApprovalCheck(Girl, 900):
                    if Girl == RogueX:        
                            ch_r "Sure, what's up?"
                    elif Girl == KittyX:        
                            ch_k "Yeah?"
                    elif Girl == EmmaX: 
                            ch_e "Very well, what did you need?"
                    elif Girl == LauraX: 
                            $ LauraX.Loc = "bg showerroom"            
                            ch_l "Huh? Ok, what's up?"
                else:
                    
                    if Girl == RogueX: 
                            ch_r "Um, actually, I'm not really comfortable being so. . . exposed?"
                            ch_r "I'll just see you around later."
                    elif Girl == KittyX:
                            ch_k "I'm[KittyX.like]totally exposed here?"
                            ch_k "I'm just going to head out."
                    elif Girl == EmmaX: 
                            ch_e "I really shouldn't be \"hanging out\" in such a state."
                            ch_e "We can talk later."
                    elif Girl == LauraX: 
                            ch_l "I probably shouldn't hang out like this."
                            ch_l "We'll talk later."
                    call Remove_Girl(Girl)  
        
        if Line == "leaving":
                $ Girl.OutfitChange(6)
        $ Line = 0
        return 0
# End Girl Caught Shower / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




#start girls sunbathing / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Pool_Sunbathe(Girl=0,Type=0,Mod=0):
    # This gets called with a character name, and checks 
    # Line tends to carry the current agreement state, Type tends to carry the item being discussed
    # mod is a modifier, base 0, but +200 if asking for no bottoms
    
    menu:
        "With who?"
        "[RogueX.Name]" if bg_current == RogueX.Loc:                                
                $ Girl = RogueX
        "[KittyX.Name]" if bg_current == KittyX.Loc:                                 
                $ Girl = KittyX
        "[EmmaX.Name]" if bg_current == EmmaX.Loc:                                   
                $ Girl = EmmaX
        "[LauraX.Name]" if bg_current == LauraX.Loc:                                  
                $ Girl = LauraX
        "Never mind.":
                return
                    
    if "tan" not in Girl.RecentActions and "no tan" not in Girl.RecentActions:
            ch_p "Hey, [Girl.Name], why don't you just relax over here?"
            ch_p "You don't want to get tanlines, why don't you. . ."
            ch_p ". . . take off a few layers?"
    else:
            ch_p "Are you sure you don't want to. . ."
    
    if Current_Time == "Night" or Current_Time == "Evening":
            $ Girl.FaceChange("confused")
            call AnyLine(Girl,"A bit late in the day for that. . .")
            $ Girl.FaceChange("normal")
            return        
    if not Girl.ClothingCheck():
            #if she's already nude. . .
            $ Girl.FaceChange("sly")
            call AnyLine(Girl,"Little late for that.")
            return            
    if "no tan" in Girl.RecentActions:
            $ Girl.FaceChange("angry")
            call AnyLine(Girl,"I just told you \"no.\"")
            $ Girl.AddWord(1,"angry","angry") #makes her angry
            return
    elif "no tan" in Girl.DailyActions :
            $ Girl.FaceChange("angry")
            call AnyLine(Girl,"Not today.")
            $ Girl.AddWord(1,"angry","angry") #makes her angry
            return
    
    if Girl == EmmaX:
            if "classcaught" not in EmmaX.History:        
                    $ Girl.FaceChange("angry",2)
                    ch_e "That would be entirely inappropriate."
                    return
            if "taboo" not in EmmaX.History:    
                    $ Girl.FaceChange("bemused",2)
                    ch_e "[EmmaX.Petname], we can't be seen like that in public. . ."
                    return
            if "three" not in EmmaX.History:
                    if not AloneCheck(EmmaX):    
                            $ Girl.FaceChange("bemused",2)
                            ch_e "Not with this sort of company. . ."
                            return     
                         
    if not Girl.Over and not Girl.Chest and not Girl.Legs and not Girl.Panties:
            #if she's already nude. . .
            $ Girl.FaceChange("sly")
            if Girl == RogueX:
                ch_r "I don't think that'll be a problem, [RogueX.Petname]."
            elif Girl == KittyX:
                ch_k "Beat you to it."
            elif Girl == EmmaX:
                ch_e "I plan ahead."
            elif Girl == LauraX:
                ch_l "Yup."
            $ Girl.AddWord(1,"tan","tan") #adds the "tan" trait to recent and daily actions
            return
        
    $ Line = 0    
    while True:
            #loops until you return
            if not Line:
                #only asks questions if there's not a play on the table.
                menu:
                    extend ""                                
                    "take it all off?" if (Girl.Over or Girl.Chest) and (Girl.Legs or Girl.Panties or Girl.Hose):
                            if Girl.Over == "towel" and not Girl.Legs and not Girl.Hose and not Girl.Panties:
                                $ Type = "no panties"
                            elif (Girl.Legs or Girl.Hose) and not Girl.Panties:
                                $ Type = "no panties"
                            elif Girl.Over and not Girl.Chest:
                                $ Type = "no bra"
                            else: 
                                $ Type = "both"
                            $ Mod = 200
                                
                    "lose the top?" if Girl.Chest and not Girl.Over:
                            $ Type = "bra"
                            
                    "maybe just lose the [Girl.Over]?" if Girl.Over:
                            if Girl.Over == "towel" and not Girl.Legs and not Girl.Hose and not Girl.Panties:
                                $ Type = "no panties"
                            elif not Girl.Chest:
                                $ Type = "no bra"
                            else: 
                                $ Type = "over"
                                
                    "maybe just lose the [Girl.Legs]?" if Girl.Legs:
                            if not Girl.Panties:
                                $ Type = "no panties"
                            else: 
                                $ Type = "legs"
                                
                    "maybe just lose the [Girl.Hose]?" if Girl.Hose and not Girl.Legs:
                            if not Girl.Panties:
                                $ Type = "no panties"
                            else: 
                                $ Type = "legs"
                                
                    "maybe just lose the [Girl.Panties]?" if Girl.Panties:
                                $ Type = "panties"
                                $ Mod = 200    
                                                                
                    "never mind.":
                            return
            # end menu
                                        
            if Type == "no panties":
                    $ Mod = 200    
                    $ Girl.FaceChange("bemused",1)
                    call AnyLine(Girl,"I don't have bottoms on under this. . .")
            elif Type == "no bra":
                    $ Girl.FaceChange("bemused",1)
                    call AnyLine(Girl,"I don't have a top on under this. . .")
            
            if Girl.SeenCheck(1): #makes it easier if you've already seen her
                    $ Mod -= 100
                    
            # This is the primary check to see whether she's into it.
            if "exhibitionist" in Girl.Traits:
                    #if she's an exhibitionist
                    $ Line = "sure"
            elif ApprovalCheck(Girl, 700+Mod, "I"):
                    #if she's generally slutty
                    $ Line = "sure"
            elif ApprovalCheck(Girl, 1400+Mod):
                    # if she really likes you.
                    $ Line = "sure"
            elif ApprovalCheck(Girl, 900):
                    # if she is fairly casual, not not enough
                    $ Line = "sorry"
            else:       
                    # if she refuses
                    $ Line = "no"
            
            if Type == "no bra" or Type == "no panties":
                    #checks to see if she'd lose her jacket/pants if nothing on under
                    menu:
                        extend ""
                        "And?":
                            if Line == "sure": 
                                    if "tan" not in Girl.RecentActions and "no tan" not in Girl.RecentActions:
                                        $ Girl.Statup("Inbt", 70, 1)
                                        
                                    $ Girl.FaceChange("sly",1)
                                    if Girl == RogueX:
                                        ch_r "Hmm, good point. . ."
                                    elif Girl == KittyX:
                                        ch_k "\"And\". . . I don't know. . ."
                                    elif Girl == EmmaX:
                                        ch_e "\"And\". . . you're lucky you're so cute. . ."
                                    elif Girl == LauraX:
                                        ch_l "I don't know. . ."
                            else:
                                    if "tan" not in Girl.RecentActions and "no tan" not in Girl.RecentActions:
                                        $ Girl.Statup("Love", 70, -1)
                                        $ Girl.Statup("Obed", 80, 1)
                                        
                                    $ Girl.FaceChange("angry",2)
                                    if Girl == RogueX:
                                        ch_r "\"And\" that's all you're getting. . . for now. . ."
                                    elif Girl == KittyX:
                                        ch_k "\"And\". . . AND!"
                                    elif Girl == EmmaX:
                                        ch_e "\"And\". . . you shouldn't push your luck. . ."
                                    elif Girl == LauraX:
                                        ch_l "\"And\" that's all you get."
                        "Take it off anyway.":
                            if Line == "sure" or (Line == "sorry" and ApprovalCheck(Girl, 600+Mod, "O")):
                                    if "tan" not in Girl.RecentActions and "no tan" not in Girl.RecentActions:
                                        $ Girl.Statup("Obed", 50, 1)
                                        $ Girl.Statup("Obed", 80, 2)
                                    if Line != "sure":    
                                            $ Girl.FaceChange("sad",2)
                                    else:
                                            $ Girl.FaceChange("normal",1)
                                    if Girl == RogueX:
                                        ch_r "Oh, ok. . ."
                                    elif Girl == KittyX:
                                        ch_k "Yeah, ok. . ."
                                    elif Girl == EmmaX:
                                        ch_e "If you insist. . ."
                                    elif Girl == LauraX:
                                        ch_l "Affirmative."
                                        
                                    $ Line = "sure"
                            else:
                                    if "tan" not in Girl.RecentActions and "no tan" not in Girl.RecentActions:
                                        $ Girl.Statup("Love", 80, -2)
                                        $ Girl.Statup("Obed", 80, -1)
                                        $ Girl.Statup("Inbt", 60, 1)
                                        
                                    $ Girl.FaceChange("angry",1)
                                    if Girl == RogueX:
                                        ch_r "I don't like that tone on you. . ."
                                    elif Girl == KittyX:
                                        ch_k "How about \"no\". . ."
                                    elif Girl == EmmaX:
                                        ch_e "Not with that tone. . ."
                                    elif Girl == LauraX:
                                        ch_l "Don't push me."
                                        
                                    $ Girl.AddWord(1,"no tan","no tan") #adds the "no tan" trait to recent and daily actions
                                    return
                        "Hot.":
                                    if "tan" not in Girl.RecentActions and "no tan" not in Girl.RecentActions:
                                        $ Girl.Statup("Love", 80, 1)
                                        $ Girl.Statup("Obed", 70, 2)
                                        $ Girl.Statup("Inbt", 60, 1)
                                        $ Girl.Statup("Inbt", 80, 1)
                                        
                                    $ Girl.FaceChange("sly",1)
                                    if Girl == RogueX:
                                        ch_r "Heh, you're a sweetie. . ."
                                    elif Girl == KittyX:
                                        ch_k "Hehe. . ."
                                    elif Girl == EmmaX:
                                        ch_e "How sweet. . ."
                                    elif Girl == LauraX:
                                        ch_l "True."
                                        
                        "Ok, that's fine.": 
                            if Line == "sure":
                                    if "tan" not in Girl.RecentActions and "no tan" not in Girl.RecentActions:
                                        $ Girl.Statup("Love", 80, 2)
                                        $ Girl.Statup("Obed", 80, 1)
                                        $ Girl.Statup("Inbt", 60, 1)
                                        $ Girl.Statup("Inbt", 80, 1)
                                        
                                    $ Girl.FaceChange("sly",1)
                                    if Girl == RogueX:
                                        ch_r "Ready for a nice surprise? . ."
                                    elif Girl == KittyX:
                                        ch_k "Oh, you bet it is. . ."
                                    elif Girl == EmmaX:
                                        ch_e "More than you know. . ."
                                    elif Girl == LauraX:
                                        ch_l "But I can be generous. . ."
                            else:
                                    if "tan" not in Girl.RecentActions and "no tan" not in Girl.RecentActions:
                                        $ Girl.Statup("Love", 50, 1)
                                        $ Girl.Statup("Love", 80, 1)
                                        $ Girl.Statup("Inbt", 60, 1)
                                        
                                    $ Girl.FaceChange("smile")
                                    if Girl == RogueX:
                                        ch_r "Thanks, [RogueX.Petname]. . ."
                                    elif Girl == KittyX:
                                        ch_k "Thanks. . ."
                                    elif Girl == EmmaX:
                                        ch_e "Good. . ."
                                    elif Girl == LauraX:
                                        ch_l "Right."
                    
                    if Line == "sure":
                            #she agrees
                            $ Girl.Over = 0 # removes Over
                            call expression Girl.Tag + "_First_Topless"
                            if Type == "no panties":
                                    $ Girl.Legs = 0 # removes Legs
                                    $ Girl.Hose = 0 # removes Hose    
                                    call expression Girl.Tag + "_First_Bottomless"
                            $ Girl.AddWord(1,"tan","tan") #adds the "tan" trait to recent and daily actions
                    else:
                            $ Girl.AddWord(1,"no tan","no tan") #adds the "no tan" trait to recent and daily actions
                                
                    $ Line = 0
            # end "nothing on under this. . ."   
                    
            if Line == "sure":
                    #She agrees. . .
                    if "tan" not in Girl.RecentActions and "no tan" not in Girl.RecentActions:
                            $ Girl.Statup("Obed", 70, 2)
                            $ Girl.Statup("Obed", 90, 1)
                            $ Girl.Statup("Inbt", 70, 2)
                            $ Girl.Statup("Inbt", 90, 1)
                    $ Girl.FaceChange("sly",1)
                    if Girl == RogueX:
                        ch_r "I suppose I could. . ."
                    elif Girl == KittyX:
                        ch_k "I guess. . ."
                    elif Girl == EmmaX:
                        ch_e "Hmmm. . ."
                    elif Girl == LauraX:
                        ch_l "Sure."
                        
                    if Type == "over" or Type == "both":
                            $ Girl.Over = 0
                    if Type == "bra" or Type == "both":
                            $ Girl.Chest = 0                            
                    call expression Girl.Tag + "_First_Topless"
                    
                    if Type == "legs" or Type == "both":
                            $ Girl.Legs = 0 # removes Legs
                            $ Girl.Hose = 0 # removes Hose
                    if Type == "panties" or Type == "both":
                            $ Girl.Panties = 0                            
                    call expression Girl.Tag + "_First_Bottomless"
                    
                    $ Girl.AddWord(1,"tan","tan") #adds the "tan" trait to recent and daily actions
                            
            elif Line == "sorry" and (Type == "over" or Type == "legs"):
                    #She agrees to just an over-layer. . .
                    if "tan" not in Girl.RecentActions and "no tan" not in Girl.RecentActions:
                            $ Girl.Statup("Obed", 50, 1)
                            $ Girl.Statup("Obed", 80, 1)
                            $ Girl.Statup("Inbt", 60, 1)
                            $ Girl.Statup("Inbt", 80, 1)
                    $ Girl.FaceChange("bemused",1)
                    if Girl == RogueX:
                        ch_r "I suppose I could. . ."
                    elif Girl == KittyX:
                        ch_k "I guess. . ."
                    elif Girl == EmmaX:
                        ch_e "Hmmm. . ."
                    elif Girl == LauraX:
                        ch_l "Sure."
                        
                    if Type == "over":
                            $ Girl.Over = 0
                    if Type == "legs":
                            $ Girl.Legs = 0
                            $ Girl.Hose = 0
                    $ Girl.AddWord(1,"tan","tan") #adds the "tan" trait to recent and daily actions
                            
            elif Line == "sorry":
                    #She refuses but is not offended. . .
                    if "tan" not in Girl.RecentActions and "no tan" not in Girl.RecentActions:
                            $ Girl.Statup("Obed", 50, 2)
                            $ Girl.Statup("Obed", 80, 2)
                            $ Girl.Statup("Inbt", 60, 1)
                            $ Girl.Statup("Inbt", 90, 2)
                    $ Girl.FaceChange("sadside",1)
                    if Girl == RogueX:
                        ch_r "Sorry, I think I can live with the tan lines. . ."
                    elif Girl == KittyX:
                        ch_k "I just can't. . ."
                    elif Girl == EmmaX:
                        ch_e "That just wouldn't be appropriate. . ."
                    elif Girl == LauraX:
                        ch_l "Nah. . ."
                    $ Girl.AddWord(1,"no tan","no tan") #adds the "no tan" trait to recent and daily actions
                    
            elif Line == "no":
                    #She is offended you even asked. . .
                    $ Girl.Statup("Love", 50, -5)
                    $ Girl.Statup("Obed", 50, 2)
                    $ Girl.Statup("Inbt", 60, 1)
                    $ Girl.FaceChange("angry",1)
                    if Girl == RogueX:
                        ch_r "Not interested, [RogueX.Petname]. . ."
                    elif Girl == KittyX:
                        ch_k "Not even."
                    elif Girl == EmmaX:
                        ch_e "You must be dreaming. . ."
                    elif Girl == LauraX:
                        ch_l "Nope. . ."
                        
                    $ Girl.AddWord(1,"no tan","no tan") #adds the "no tan" trait to recent and daily actions
                    return
            if not Girl.Chest and not Girl.Over and not Girl.Panties and not Girl.Legs and Girl.HoseNum() < 10:
                        $ Girl.OutfitChange("nude") #removes remaining clothing.
            $ Mod = 0
            $ Line = 0
            if Girl.ClothingCheck():
                "Anything else?" #loops back to menu
            else:
                return                
    return

#End girls sunbathing / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#start girls skinnydip / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Pool_Skinnydip(Girl=0,Line=0,Type=0,Mod=0):
    # This gets called with a character name, and checks 
    # Line tends to carry the current agreement state, Type tends to carry the item being discussed
    # mod is a modifier, base 0, but +200 if asking for no bottoms
    
    menu:
        "With who?"
        "[RogueX.Name]" if bg_current == RogueX.Loc:                                
                $ Girl = RogueX
        "[KittyX.Name]" if bg_current == KittyX.Loc:                                 
                $ Girl = KittyX
        "[EmmaX.Name]" if bg_current == EmmaX.Loc:                                   
                $ Girl = EmmaX
        "[LauraX.Name]" if bg_current == LauraX.Loc:                                  
                $ Girl = LauraX
        "Never mind.":
                return
                
    ch_p "Hey, [Girl.Name], why don't we skinny dip?"
    
    if Round <= 10:
            $ Girl.FaceChange("sad")
            call AnyLine(Girl,"No time for that.")
            return    
    elif "no dip" in Girl.RecentActions:
            $ Girl.FaceChange("angry")
            call AnyLine(Girl,"I just told you \"no.\"")
            $ Girl.AddWord(1,"angry","angry") #makes her angry
            return
    elif "no dip" in Girl.DailyActions:
            $ Girl.FaceChange("angry")
            call AnyLine(Girl,"Not today.")
            $ Girl.AddWord(1,"angry","angry") #makes her angry
            return
    elif "dip" in Girl.RecentActions:
            $ Girl.FaceChange("confused")
            call AnyLine(Girl,"We already did that.")
            return
     
    if Girl == EmmaX:
            if "classcaught" not in EmmaX.History:        
                    $ Girl.FaceChange("angry",2)
                    ch_e "That would be entirely inappropriate."
                    return
            if "taboo" not in EmmaX.History:    
                    $ Girl.FaceChange("bemused",2)
                    ch_e "[EmmaX.Petname], I couldn't risk us getting caught. . ."
                    return
            if "three" not in EmmaX.History:
                    if not AloneCheck(EmmaX):
                            $ Girl.FaceChange("bemused",2)
                            ch_e "Not with this sort of company. . ."
                            return                         
    
    if not Girl.ClothingCheck():
            #if she's already nude. . .
            $ Girl.FaceChange("sly")
            if Girl == RogueX:
                ch_r "Sure, let's get wet."
            elif Girl == KittyX:
                ch_k "Cannonball!"
            elif Girl == EmmaX:
                ch_e "Lovely."
            elif Girl == LauraX:
                ch_l "I'm in."
            $ Girl.AddWord(1,"dip","dip") #adds the "dip" trait to recent and daily actions
    else:
            #if she's dressed. . .
            if Girl.SeenCheck(1):
                    $ Mod += 100
                            
            if "exhibitionist" in Girl.Traits:
                    #if she's an exhibitionist
                    $ Line = "sure"
            elif ApprovalCheck(Girl, 700-Mod, "I"):
                    #if she's generally slutty
                    $ Line = "sure"
            elif ApprovalCheck(Girl, 1200-Mod):
                    # if she really likes you.
                    $ Line = "sure"
            elif ApprovalCheck(Girl, 800):
                    # if she is fairly casual, not not enough
                    $ Line = "sorry"
            else:       
                    # if she refuses
                    $ Line = "no"
            
            if Line == "sure":
                    #She agrees. . .
                    if "dip" not in Girl.RecentActions and "no dip" not in Girl.RecentActions:   
                            $ Girl.Statup("Obed", 70, 2)
                            $ Girl.Statup("Obed", 90, 1)
                            $ Girl.Statup("Inbt", 70, 2)
                            $ Girl.Statup("Inbt", 90, 1)
                    $ Girl.FaceChange("sly",1)
                    if Girl == RogueX:
                        ch_r "Sounds fun. . ."
                    elif Girl == KittyX:
                        ch_k "Oooh, naughty. . ."
                    elif Girl == EmmaX:
                        ch_e "How daring. . ."
                    elif Girl == LauraX:
                        ch_l "Sure."
                        
                    $ Girl.Over = 0 # removes Over
                    $ Girl.Chest = 0 # removes Bra 
                    call expression Girl.Tag + "_First_Topless"
                    
                    $ Girl.Legs = 0 # removes Legs
                    $ Girl.Hose = 0 # removes Hose
                    $ Girl.Panties = 0 # removes Panties            
                    call expression Girl.Tag + "_First_Bottomless"
                    $ Girl.OutfitChange("nude") #removes remaining clothing.
                    $ Girl.AddWord(1,"dip","dip") #adds the "dip" trait to recent and daily actions
                                                
            elif Line == "sorry":
                    #She refuses but is not offended. . .
                    if "dip" not in Girl.RecentActions and "no dip" not in Girl.RecentActions:   
                            $ Girl.Statup("Obed", 50, 2)
                            $ Girl.Statup("Obed", 80, 2)
                            $ Girl.Statup("Inbt", 60, 1)
                            $ Girl.Statup("Inbt", 90, 2)
                    $ Girl.FaceChange("sadside",1)
                    if Girl == RogueX:
                        ch_r "Couldn't we just take a normal swim?"
                    elif Girl == KittyX:
                        ch_k "I don't think so. . ."
                    elif Girl == EmmaX:
                        ch_e "Perhaps in a tub. . ."
                    elif Girl == LauraX:
                        ch_l "Nah. . ."
                    menu:
                        extend ""
                        "Ok, we can just use swimsuits.": 
                                if Girl.Swim[0]:
                                        #if she has a suit to put on. . .
                                        if "dip" not in Girl.RecentActions and "no dip" not in Girl.RecentActions:
                                                $ Girl.Statup("Love", 80, 2)
                                                $ Girl.Statup("Obed", 50, 1)
                                                $ Girl.Statup("Inbt", 60, 2)
                                        $ Girl.FaceChange("smile")   
                                        if Girl == RogueX:
                                            ch_r "Thanks, [RogueX.Petname]."
                                        elif Girl == KittyX:
                                            ch_k "Cool."
                                        elif Girl == EmmaX:
                                            ch_e "That would be nice."
                                        elif Girl == LauraX:
                                            ch_l "Whatever."                               
                                        
                                        show blackscreen onlayer black 
                                        "She goes and changes into her suit. . ."
                                        $ Girl.OutfitChange("swimwear") # puts on her swimsuit
                                        hide blackscreen onlayer black 
                                        $ Girl.AddWord(1,"no dip","no dip") #adds the "no tan" trait to recent and daily actions
                                        $ Count = 1
                                else:
                                        if not Girl.OutfitChange("swimwear"):
                                                $ Count = 0  
                                if not Count:
                                    #If she has no suit. . .
                                    menu:
                                        extend ""
                                        "Then what about your undies?":
                                            if Girl.ChestNum() > 2 and Girl.PantiesNum() > 2 and ApprovalCheck(Girl, 1000):
                                                #if she mostly likes you, and is wearing decent undies. . .
                                                pass
                                            elif Girl.ChestNum() > 1 and Girl.PantiesNum() > 1 and ApprovalCheck(Girl, 1200):
                                                #if she mostly likes you, and is wearing scandelous undies. . .
                                                pass
                                            else:       
                                                $ Girl.FaceChange("sly",1)             
                                                call AnyLine(Girl,"That's not going to work either.")                             
                                                $ Girl.AddWord(1,"no dip","no dip")
                                                return       
                                            $ Girl.FaceChange("smile",1)                                         
                                            if Girl == RogueX:
                                                ch_r "Ok, fine. . ."
                                            elif Girl == KittyX:
                                                ch_k "Fine, geez."
                                            elif Girl == EmmaX:
                                                ch_e "I suppose. . ."
                                            elif Girl == LauraX:
                                                ch_l "Sure, whatever. . ."                                        
                                        "Ok then, never mind.":
                                                call AnyLine(Girl,"Thanks.") 
                                                $ Girl.AddWord(1,"no dip","no dip")
                                                return
                                    $ Girl.Over = 0 # Takes off Over
                                    "She starts to strip down."
                                    $ Girl.Legs = 0 # Takes off Legs
                                    $ Girl.Hose = 0 # Takes off Hose
                                    "And ends up in her underwear."
                                    $ Girl.SeenPanties = 1
                                    
                                    
                        "Never mind then.":                         
                                $ Girl.Statup("Love", 80, -1)
                                if "dip" not in Girl.RecentActions and "no dip" not in Girl.RecentActions:   
                                        $ Girl.Statup("Obed", 50, 2)
                                        $ Girl.Statup("Inbt", 60, 1)
                                if Girl == RogueX:
                                    ch_r "Hmph."
                                elif Girl == KittyX:
                                    ch_k "Bummer."
                                elif Girl == EmmaX:
                                    ch_e "Disappointing."
                                elif Girl == LauraX:
                                    ch_l "K."
                                $ Girl.AddWord(1,"no dip","no dip") #adds the "no tan" trait to recent and daily actions
                                return
                    
            elif Line == "no":
                    #She is offended you even asked. . .
                    $ Girl.Statup("Love", 50, -5)
                    if "dip" not in Girl.RecentActions and "no dip" not in Girl.RecentActions:
                        $ Girl.Statup("Obed", 50, 2)
                        $ Girl.Statup("Inbt", 60, 1)
                    $ Girl.FaceChange("angry",1)
                    if Girl == RogueX:
                        ch_r "Not interested, [RogueX.Petname]. . ."
                    elif Girl == KittyX:
                        ch_k "Not even."
                    elif Girl == EmmaX:
                        ch_e "You must be dreaming. . ."
                    elif Girl == LauraX:
                        ch_l "Nope. . ."
                        
                    $ Girl.AddWord(1,"no dip","no dip") #adds the "no tan" trait to recent and daily actions
                    return
    $ Girl.Water = 1               
    $ Round -= 20 if Round >= 20 else Round         
    "You both swim around for a bit."   
    
    return

#End girls skinnydip / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Pool Topless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Pool_Topless(Girl=Ch_Focus,BO=[]):    
        #the girl is swimming, but ends up topless temporarily
        if Girl.Loc != bg_current:
                    #if the lead girl isn't in the room for some reason. . .
                    $ BO = TotalGirls[:]  
                    $ renpy.random.shuffle(BO)
                    while BO:        
                            if BO[0].Loc == bg_current:                  
                                    call Shift_Focus(BO[0])
                                    $ BO = [1]
                            $ BO.remove(BO[0])
                
        $ Girl = Ch_Focus
        if (Girl.ChestNum() <= 1 and Girl.OverNum() <= 1) or Girl.Loc != bg_current:
                #if *no* girls are present, ditch or no point, already topless
                $ D20 = renpy.random.randint(1, 14)
                return
        call AllReset(Girl)
        "[Girl.Name] dives into the pool"         
        call ShowPool #displays pool graphics
        $ Girl.Uptop = 1 #sets uptop
        menu:
            "It appears she's had a wardrobe malfunction."
            "Hey, [Girl.Name]. . .":
                    ch_p "Looks like you might be missing something there. . ."                
                    $ Girl.FaceChange("confused")         
                    call AnyLine(Girl,". . .")
                    $ Girl.FaceChange("surprised",2,Eyes="down")
                    $ Girl.Statup("Love", 80, 3)
                    $ Girl.Statup("Love", 90, 1)
                    $ Girl.Statup("Obed", 60, 2)
                    $ Girl.Statup("Inbt", 50, -2)
                    $ Girl.Statup("Lust", 50, 2)
                    $ Count = 100
            "Say nothing":
                    $ Girl.FaceChange("surprised",2,Eyes="down") 
                    "After a few moments, [Girl.Name] seems to notice that her top rode up."
                    if ApprovalCheck(Girl, 1200):
                            $ Count = 0
                    else:
                            $ Count = -100
                        
        if ApprovalCheck(Girl, 800-Count,"I") or ApprovalCheck(Girl, 1600-Count):
                $ Girl.FaceChange("sly")   
                $ Girl.Chest = 0 #loses top
                $ Girl.Over = 0 #loses top
                $ Girl.Statup("Obed", 60, 2)
                $ Girl.Statup("Inbt", 50, 4)
                $ Girl.Statup("Inbt", 90, 2)
                $ Girl.Statup("Lust", 50, 5)
                "She smiles and tosses her top over her head."       
                call expression Girl.Tag + "_First_Topless"
        elif ApprovalCheck(Girl, 500-Count,"I") or ApprovalCheck(Girl, 1200-Count):
                $ Girl.FaceChange("sly",1)   
                $ Girl.Statup("Obed", 60, 2)
                $ Girl.Statup("Inbt", 50, 3)
                $ Girl.Statup("Inbt", 80, 2)
                $ Girl.Statup("Lust", 50, 3)
                "She smiles, and leaves the top how it is."
                call expression Girl.Tag + "_First_Topless"
        else:
                if ApprovalCheck(Girl, 800-Count):
                        #she's ok with it
                        $ Girl.Statup("Obed", 60, 2)
                        $ Girl.Statup("Inbt", 70, 2)
                        $ Girl.Statup("Lust", 50, 1)
                        $ Girl.FaceChange("bemused",2) 
                else:
                        #she's mad
                        $ Girl.Statup("Love", 70, -2)
                        $ Girl.Statup("Inbt", 50, 1)
                        $ Girl.FaceChange("angry",2) 
                call expression Girl.Tag + "_First_Topless" pass (1)
                $ Girl.Uptop = 0 #resets uptop
                "She tugs her top back into place."
                if Count <= 0:
                        $ Girl.Statup("Love", 70, -5)
                        $ Girl.Statup("Obed", 60, -2)
                        $ Girl.Statup("Inbt", 60, 2)
                        call AnyLine(Girl,"You could have told me.")
                    
        $ Count = 0
        return
# End Pool Topless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start break-up dialog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Breakup(Girl=0,Other=0,Anger = 0,BO=[]): 
        # call Breakup(RogueX) from Chat
        # Repeats is number of times you've broken up, Other is a potential other woman, Anger is a meter that ends things at 4+
        
        $ Girl.AddWord(1,"breakup talk","breakup talk",0,0)
                
        if Girl.Break[1] > 3:       
                $ Girl.FaceChange("angry")
                $ Girl.Statup("Love", 50, -5, 1)
                $ Girl.Statup("Love", 80, -10, 1)
                $ Girl.Statup("Obed", 30, -5, 1)
                $ Girl.Statup("Obed", 50, -10, 1)
                $ Girl.Statup("Inbt", 50, 3)
                $ Girl.Statup("Inbt", 80, 1)
                call AnyLine(Girl,"This is getting old.")       
                $ Anger -= 1
        elif Girl.Break[1]:
                $ Girl.FaceChange("surprised")
                $ Girl.Statup("Love", 50, -5, 1)
                $ Girl.Statup("Obed", 30, -5, 1)
                $ Girl.Statup("Inbt", 80, 1) 
                call AnyLine(Girl,"What, again?")
                $ Girl.FaceChange("angry")
                $ Anger += 1
        else:
                $ Girl.FaceChange("surprised")  
                call AnyLine(Girl,"What?! Why?")
        
        $ Line = 0
        menu:
            "It's not you, it's me.":  
                    $ Girl.Statup("Love", 200, -5)
                    $ Girl.Statup("Obed", 80, -5)
                    $ Girl.Statup("Inbt", 50, 3) 
                    $ Girl.Statup("Inbt", 70, 1) 
                    $ Girl.FaceChange("confused")
                
            "I just think we need a break.":
                    $ Girl.Statup("Love", 200, -5)
                    $ Girl.FaceChange("sad")
                
            "I've found someone else.":      
                    $ Anger += 1
                    $ Girl.Statup("Love", 200, -10)
                    $ Girl.Statup("Obed", 50, 3)
                    $ Girl.Statup("Obed", 80, 3)
                    $ Girl.Statup("Inbt", 50, -5)  
                    $ Girl.FaceChange("angry")
                    call AnyLine(Girl,"Who is it?")
                    menu:
                        extend ""
                        "[RogueX.Name]" if Girl != RogueX:           
                                $ Other = RogueX
                        "[KittyX.Name]" if Girl != KittyX and "met" in KittyX.History:           
                                $ Other = KittyX
                        "[EmmaX.Name]" if Girl != EmmaX and "met" in EmmaX.History:           
                                $ Other = EmmaX
                        "[LauraX.Name]" if Girl != LauraX and "met" in LauraX.History:           
                                $ Other = LauraX
                        "I won't say.":
                                $ Girl.Statup("Love", 200, -5)   
                                $ BO = ActiveGirls[:]  
                                $ BO.remove(Girl)
                                $ Count = 0
                                while BO:        
                                        if BO[0].SEXP > Count: 
                                                # if you've boned this girl more than the last, she's the boss
                                                $ Other = BO[0]
                                                $ Count = BO[0].SEXP
                                        $ BO.remove(BO[0])
                                $ Count = 0
                                if not Other:
                                        call AnyLine(Girl,"Well it's got to be someone. . .")
                                else:    
                                        call AnyLine(Girl,"It's "+Other.Name+", isn't it.")
                        "I was kidding.":  
                                $ Girl.Statup("Love", 200, -5)
                                $ Girl.Statup("Obed", 50, 3)  
                                $ Girl.FaceChange("angry")
                                if Girl == RogueX:
                                        ch_r "That was a pretty rude way to deflect there." 
                                elif Girl == KittyX:
                                        ch_k "I'll[KittyX.like]kid you!"
                                elif Girl == EmmaX:
                                        ch_e "Oh, you do *not* want to \"kid\" me about that."
                                elif Girl == LauraX:
                                        ch_l ". . ." 
                                $ Girl.FaceChange("normal")
                                $ Anger += 1
                                    
            "I'm just done with you.":  
                    $ Girl.FaceChange("angry")
                    $ Girl.Statup("Love", 50, 3)
                    $ Girl.Statup("Love", 200, -15)
                    $ Girl.Statup("Obed", 50, 5)
                    $ Girl.Statup("Obed", 80, 5)
                    $ Girl.Statup("Obed", 200,5)
                    $ Girl.Statup("Inbt", 50, -5)                
                    $ Anger += 1
        #end first question
        
        if not Other: 
                #"denial":
                $ Girl.FaceChange("sad")
                if ApprovalCheck(Girl, 900, "O"):
                        #high obedience
                        call AnyLine(Girl,"If that's really what you want. . .")
                elif ApprovalCheck(Girl, 900, "L"):
                        #high love
                        call AnyLine(Girl,"But I love you so much!")
                elif ApprovalCheck(Girl, 900, "I"):
                        #super casual
                        call AnyLine(Girl,"If that's how you feel. . .")
                elif ApprovalCheck(Girl, 1500):
                        #general mix
                        call AnyLine(Girl,"But we mean so much to each other!")
                else: 
                        #doesn't care too much
                        call AnyLine(Girl,"Are you sure this is what you want?")
                $ Line = "bargaining"
                
        else:
            #if there's another girl. . .
            #GirlLikeCheck(RogueX,KittyX) if Rogue is the girl talking and Kitty is the "other girl"
            $ Cnt = int((Girl.GirlLikeCheck(Other) - 500)/2) 
                        
            if Girl.GirlLikeCheck(Other) >= 800: 
                    $ Girl.Statup("Lust", 70, 5)
                    $ Girl.Statup("Obed", 50, 5)
                    $ Girl.Statup("Obed", 200, 5)
                    $ Girl.Statup("Inbt", 50, 1)
                    $ Girl.Statup("Inbt", 200, 5) 
                    $ Girl.FaceChange(5,2) #blush2
                    call AnyLine(Girl,"Well, you have good tastes, at least.")
                    $ Girl.FaceChange(5,1) #blush1
            elif Girl.GirlLikeCheck(Other) >= 600:
                    $ Girl.Statup("Love", 50, -5, 1)
                    $ Girl.Statup("Love", 80, -10, 1)
                    $ Girl.Statup("Obed", 50, 5)
                    $ Girl.Statup("Obed", 200, 3)
                    if Other == EmmaX:                            
                            call AnyLine(Girl,"With our teacher?!")
                    elif Girl == EmmaX:
                            ch_e "And I always did like her in class. . ."
                    elif Girl == LauraX:
                            ch_l "I do kinda like her." 
                    else:
                            call AnyLine(Girl,"With one of my friends?!")
                    $ Girl.FaceChange("normal")
                    $ Anger += 1
            elif Girl.GirlLikeCheck(Other) >= 400:
                    $ Girl.Statup("Love", 50, -3, 1)
                    $ Girl.Statup("Love", 80, -5, 1)
                    $ Girl.Statup("Obed", 80, 5)
                    $ Girl.Statup("Inbt", 50, 1)
                    $ Girl.Statup("Inbt", 80, 3) 
                    call AnyLine(Girl,"You know you can do better.")
            else: #Girl.GirlLikeCheck(Other) < 400
                    $ Girl.Statup("Love", 50, -5, 1)
                    $ Girl.Statup("Obed", 80, 3)
                    $ Girl.Statup("Inbt", 50, 2)
                    $ Girl.Statup("Inbt", 80, 5) 
                    $ Girl.FaceChange("angry")
                    call AnyLine(Girl,"With that skank?!")
                    $ Anger += 2
                
            if ApprovalCheck(Girl, 2000, Bonus = Cnt):
                    $ Girl.Statup("Lust", 70, 5)
                    $ Girl.FaceChange("sexy")
                    call AnyLine(Girl,"Why not both of us?")
                    $ Line = "threeway"
            else:
                    $ Girl.FaceChange("sad")
                    call AnyLine(Girl,"You would rather be with her than with me?")
                    menu:
                        extend ""
                        "Yes, I would.":    
                                $ Girl.Statup("Love", 50, -3, 1)
                                $ Girl.Statup("Love", 80, -5, 1)
                                $ Girl.Statup("Obed", 30, 1)
                                $ Girl.Statup("Obed", 50, 1)                   
                                $ Anger += 1
                                if Girl == RogueX:
                                        ch_r "Well then I don't think I can help you." 
                                elif Girl == KittyX:
                                        ch_k "!!!"
                                elif Girl == EmmaX:
                                        ch_e "I suppose you've made your choice then."
                                elif Girl == LauraX:
                                        ch_l "Your loss." 
                                $ Line = "bargaining"
                            
                        "I'd rather be with both of you.":      
                                $ Line = "threeway"
                            
                        "No, I'm sorry, never mind that.": 
                                $ Girl.Statup("Love", 50, -3, 1)
                                $ Girl.Statup("Obed", 80, -5)
                                call AnyLine(Girl,"Not doing yourself any favors there. . .")
                                $ Line = "bargaining"
        #end "if there's another" or not
        
        if Line == "threeway" and Anger < 4: 
                call AnyLine(Girl,"Date us both at once? What does she think about that?")
                menu Breakup_Threeway_Offer:
                        extend ""
                        "She said it would be ok with her." if "poly "+ Girl.Tag in Other.Traits or Girl.Tag+"Yes" in Player.Traits: 
                                #"poly Rogue" in KittyX.Traits, or "KittyYes" in Player.Traits
                                if ApprovalCheck(Girl, 1800, Bonus = Cnt):
                                        $ Girl.FaceChange("smile", 1)
                                        $ Girl.Statup("Lust", 70, 5)     
                                        $ Girl.Statup("Obed", 50, 5)
                                        $ Girl.Statup("Obed", 80, 3)  
                                        $ Girl.Statup("Inbt", 50, 3)
                                        $ Girl.Statup("Inbt", 80, 1)
                                        if Girl.GirlLikeCheck(Other) < 400:
                                                $ Girl.FaceChange("angry") 
                                                if Girl == RogueX:
                                                        ch_r "I can't stand that bitch, but for you I'll put up with her." 
                                                elif Girl == KittyX:
                                                        ch_k "That bitch! Fine, I'll put up with her."
                                                elif Girl == EmmaX:
                                                        ch_e "I suppose I can be the better woman here. . ."
                                                        ch_e "Not that it's hard to accomplish."
                                                elif Girl == LauraX:
                                                        ch_l "I can keep my claws in. . . for you."   
                                        elif Girl.GirlLikeCheck(Other) >= 700:
                                                $ Girl.FaceChange("sexy")   
                                                call AnyLine(Girl,"I have to say I've kind of been thinking about it myself.")                     
                                        elif Girl.Love >= Girl.Obed:
                                                $ Girl.FaceChange("sad")
                                                call AnyLine(Girl,"Just so long as we can be together, I can share.") 
                                        else:
                                                #Inbt highest
                                                call AnyLine(Girl,"If she's in, I am.")  
                                                
                                        $ Girl.AddWord(1,0,0,"poly "+Other.Tag,0) #adds "poly Other" to traits                                    
                                else:      
                                        $ Anger += 2
                                        $ Girl.Statup("Love", 50, -10, 1)
                                        $ Girl.Statup("Love", 80, -15, 1)
                                        $ Girl.Statup("Obed", 50, 3)
                                        $ Girl.Statup("Obed", 80, 3) 
                                        $ Girl.Statup("Inbt", 50, 5)
                                        $ Girl.Statup("Inbt", 80, 3)
                                        $ Girl.FaceChange("angry", 1)
                                        call AnyLine(Girl,"Well maybe she did, but I don't want to share." )
                                        $ Line = "bargaining"
                        #End "she said it'd be ok.
                            
                        "I have no idea.": #if not KittyX.Break[0]:
                                $ Line = "ask " + Other #"ask Kitty"
                    
                        "She's not into it.": #if KittyX.Break[0]:
                                if Girl.GirlLikeCheck(Other) >= 700:
                                        $ Girl.Statup("Love", 200, -5)
                                elif Girl.GirlLikeCheck(Other) <= 400:
                                        $ Girl.Statup("Love", 90, 5)
                                call AnyLine(Girl,"Well then why even bring it up?")
                                
                                        
                        "Well, even if she doesn't agree. . .": 
                                $ Line = "ask " + Other #"ask Kitty"  
                                if Girl.GirlLikeCheck(Other) >= 700:
                                        $ Girl.FaceChange("angry")
                                        $ Girl.Statup("Love", 200, -5)
                                elif Girl.GirlLikeCheck(Other) <= 400:
                                        $ Girl.Statup("Love", 90, 5)
                
                if Line == "ask " + Other.Tag and Girl.GirlLikeCheck(Other) >= 700:
                                #if previous responses had her wanting to ask the other girl about it
                                call AnyLine(Girl,"You want me to ask her for you?")
                                menu:                         
                                    extend ""
                                    "Yes, that'd be a good idea.":
                                            $ Girl.Statup("Love", 90, 5)
                                            $ Girl.Statup("Obed", 70, 1)
                                            $ Girl.Statup("Inbt", 80, 5)
                                            $ Girl.FaceChange("sexy")   
                                            call AnyLine(Girl,"I guess I could.")
                                            $ Girl.AddWord(1,0,0,"ask "+Other.Tag,0) #adds "ask Other" to traits
                                            $ Girl.AddWord(1,0,0,"poly "+Other.Tag,0) #adds "poly Other" to traits     
                                    "No, let's just keep it under cover.":   
                                            $ Girl.Statup("Love", 50, -5, 1)
                                            $ Girl.Statup("Love", 80, -5, 1)
                                            $ Girl.Statup("Obed", 80, 5)
                                            $ Girl.Statup("Inbt", 50, 3)   
                                            call AnyLine(Girl,"I don't know. . .")
                        
                if Line != "bargaining" and "poly "+ Other.Tag not in Girl.Traits:
                        #if the answer is not "bargaining," but also the girl has not agreed yet. . .
                        #"poly Kitty" not in RogueX.Traits:    
                        if "ask "+ Other.Tag not in Girl.Traits and not ApprovalCheck(Girl, 1800, Bonus = -(int((Girl.GirlLikeCheck(Other) - 600)/2))): 
                                #"ask Kitty" not in RogueX.Traits
                                #checks if Girl likes you more than Other
                                $ Girl.Statup("Love", 50, -5, 1)
                                $ Girl.Statup("Obed", 80, -10, 1)
                                $ Girl.Statup("Inbt", 50, 5)
                                $ Girl.FaceChange("angry", 1)
                                if not ApprovalCheck(Girl, 1800):         
                                        call AnyLine(Girl,"Maybe I don't like you that much either.")  
                                else:
                                        $ Girl.Statup("Love", 80, -10, 1)
                                        $ Girl.Statup("Obed", 50, -5, 1)
                                        if Girl == EmmaX:
                                                ch_e "I'd rather not be dallying with a student's boyfriend. . ."
                                        elif Other == EmmaX:                            
                                                call AnyLine(Girl,"I don't want to get caught with the teacher's boyfriend!")
                                        else:
                                                call AnyLine(Girl,"I'm not really cool with that, "+Other.Name+"'s a friend of mine." ) 
                                $ Anger += 1
                                $ Line = "bargaining"                                 
                        else:   
                                #if she agrees to polygamy        
                                $ Girl.Statup("Obed", 30, 5)
                                $ Girl.Statup("Obed", 50, 3)
                                $ Girl.Statup("Inbt", 50, 5)
                                $ Girl.Statup("Inbt", 80, 1)
                                $ Girl.FaceChange("sad")           
                                if Girl.GirlLikeCheck(Other) < 400:
                                        $ Girl.FaceChange("angry")
                                        if Girl == RogueX:
                                                ch_r "I can't stand that bitch, but for you I'll put up with her." 
                                        elif Girl == KittyX:
                                                ch_k "That bitch! Fine, I'll put up with her."
                                        elif Girl == EmmaX:
                                                ch_e "I suppose I can be the better woman here. . ."
                                                ch_e "Not that it's hard to accomplish."
                                        elif Girl == LauraX:
                                                ch_l "I can keep my claws in. . . for you."   
                                elif Girl.GirlLikeCheck(Other) >= 700:
                                        $ Girl.FaceChange("sexy")   
                                        call AnyLine(Girl,"I have to say I've kind of been thinking about it myself.")                     
                                elif Girl.Love >= Girl.Obed:
                                        #RogueX.Love >= RogueX.Obed:
                                        $ Girl.FaceChange("sad")
                                        call AnyLine(Girl,"Just so long as we can be together, I can share.") 
                                else:
                                        #Inbt highest
                                        call AnyLine(Girl,"If she's in, I am.")                                                  
                                $ Girl.AddWord(1,0,0,"poly "+Other.Tag,0) #adds "poly Other" to traits   
                                if "ask "+ Other.Tag in Girl.Traits:
                                        #"ask Kitty" in RogueX.Traits:
                                        call AnyLine(Girl,"I'll talk to "+Other.Name+" about it.")
                                else:
                                        $ Girl.FaceChange("sad")                                        
                                        $ Girl.AddWord(1,0,0,"downlow",0) #adds "downlow" to traits 
                                        if Girl == RogueX:
                                                ch_r "I guess we can keep this on the downlow, for now at least." 
                                        elif Girl == KittyX:
                                                ch_k "Oooh, our little secret. . ."
                                        elif Girl == EmmaX:
                                                ch_e "I suppose I can be discreet."
                                        elif Girl == LauraX:
                                                ch_l "I can keep a secret."  
                                    
                                        if Girl.GirlLikeCheck(Other) >= 800:
                                            call AnyLine(Girl, "Please talk to "+Other.Name+" about sharing you openly though.")
                                        elif Girl.GirlLikeCheck(Other) >= 500:
                                            call AnyLine(Girl,"I really don't like going behind "+Other.Name+"'s back though.")
                                        else:
                                            call AnyLine(Girl,"Might be fun, sneaking around behind her back.")
                #End Threeway
        
        if Line == "bargaining" and Anger < 4: 
                $ Girl.FaceChange("sad")
                call AnyLine(Girl,"You're sure there's no way I could convince you to stay?")
                menu Breakup_Bargaining:            
                    extend ""
                    "Sorry, I've changed my mind.":
                            $ Girl.Statup("Obed", 80, 5)
                            if ApprovalCheck(Girl, 1500):   
                                    $ Line = "makeup"
                                    $ Girl.Statup("Love", 80, 5)
                                    if Girl == RogueX:
                                            ch_r "That's wonderful!"
                                    elif Girl == KittyX:
                                            ch_k "Ok!"
                                    elif Girl == EmmaX:
                                            ch_e "I can accept that as an apology. . ."
                                    elif Girl == LauraX:
                                            ch_l "Huh? Ok. . ."  
                            else:
                                    $ Line = "breakup"
                                    $ Girl.Statup("Love", 90, -5)
                                    $ Girl.Statup("Obed", 80, -5)
                                    $ Girl.Statup("Inbt", 80, 10)
                                    if Girl == RogueX:
                                            ch_r "You know what? Save it. We're done."
                                    elif Girl == KittyX:
                                            ch_k "Too little, too late. . ."
                                    elif Girl == EmmaX:
                                            ch_e "I'm afraid it's too late for apologies."
                                    elif Girl == LauraX:
                                            ch_l "Uh-huh. Too late for that."  
                    "My mind's made up.":
                            $ Girl.Statup("Obed", 80, 5)
                            $ Line = "breakup"
                    "Well, you could do something for me. . .[[sex menu]":                           
                            $ Girl.AddWord(1,"bargainsex",0,0,0) #adds "bargainsex" to recent                            
                            $ Girl.Statup("Obed", 80, 3)
                            $ Tempmod = 50
                            $ MultiAction = 0
                            call expression Girl.Tag + "_SexMenu" #call Rogue_SexMenu 
                            $ MultiAction = 1
                            menu:
                                "Ok, I guess we can give it another shot.":
                                        $ Girl.Statup("Love", 80, 3)
                                        $ Girl.Statup("Obed", 80, 5)
                                        $ Line = "makeup"
                                        $ Girl.FaceChange("smile")
                                
                                "That was nice, but we're still over.":
                                        $ Girl.FaceChange("angry")
                                        $ Girl.Statup("Love", 50, -5, 1)
                                        $ Girl.Statup("Love", 80, -10, 1)
                                        $ Girl.Statup("Obed", 50, 15)
                                        $ Girl.Statup("Obed", 80, 10)
                                        $ Line = "breakup"                              
                                        $ Anger += 4
                                        
                    "Maybe if we brought someone else into this relationship?" if not Other and "bargainthreeway" not in Girl.RecentActions: 
                            # if you haven't just tried this
                            $ Girl.AddWord(1,"bargainthreeway",0,0,0) #adds "bargainthreeway" to recent
                            call AnyLine(Girl,"Who?")
                            menu:
                                extend ""
                                "[RogueX.Name]?" if Girl != RogueX:
                                        $ Other = RogueX
                                "[KittyX.Name]?" if Girl != KittyX and "met" in KittyX.History:
                                        $ Other = KittyX
                                "[EmmaX.Name]?" if Girl != EmmaX and "met" in EmmaX.History:
                                        $ Other = EmmaX
                                "[LauraX.Name]?" if Girl != LauraX and "met" in LauraX.History:
                                        $ Other = LauraX
                                        
                                "Up to you?":
                                        $ Girl.FaceChange("confused")
                                        #picks her favorite girl. . .                                        
                                        $ BO = ActiveGirls[:]  
                                        $ BO.remove(Girl)
                                        $ Count = 0
                                        while BO:        
                                                if Girl.GirlLikeCheck(BO[0]) > Count: 
                                                        # if she likes this girl more than the last, she's the pick                                                        
                                                        $ Other = BO[0]
                                                        $ Count = Girl.GirlLikeCheck(BO[0])
                                                $ BO.remove(BO[0])
                                        $ Count = 0
                                        call AnyLine(Girl,Other.Name+"?")
                                        
                                "Never mind, silly question.":                            
                                        $ Girl.Statup("Love", 200, -10)
                                        $ Girl.Statup("Obed", 50, -10, 1)
                                        $ Anger += 1
                                        $ Girl.FaceChange("angry")
                                        jump Breakup_Bargaining
                                                     
                            if Other:
                                    $ Girl.FaceChange("confused")
                                    jump Breakup_Threeway_Offer 
                               
                if Anger < 3 and Line != "breakup" and Line != "makeup":
                        #if no decision and she's not pissed yet, loop   
                        jump Breakup_Bargaining
        # End Bargaining
        
        
                
        if Line == "breakup" or Anger >= 4:
                if Anger >= 4:
                        #if she's pissed
                        $ Girl.FaceChange("angry")
                        $ Girl.Statup("Love", 60, -10, 1)
                        $ Girl.Statup("Obed", 50, -5)
                        $ Girl.Statup("Inbt", 70, 5)
                        if Girl == RogueX:
                                ch_r "Well fuck you then!"
                        elif Girl == KittyX:
                                ch_k "Jerk!!"
                        elif Girl == EmmaX:
                                ch_e "Scum."
                        elif Girl == LauraX:
                                ch_l "You're gonna want to back up a few steps." 
                else:
                        #if she's just sad
                        $ Girl.Statup("Inbt", 70, 5)
                        $ Girl.FaceChange("sad")
                        
                        if Girl.Love >= Girl.Obed:
                                #RogueX.Love >= RogueX.Obed:
                                if Girl == RogueX:
                                        ch_r "I'll really miss you."
                                elif Girl == KittyX:
                                        ch_k "I was[KittyX.like]totally all-in on this!"
                                elif Girl == EmmaX:
                                        ch_e "I'll be devastated."
                                        ch_e "For at least five minutes."
                                elif Girl == LauraX:
                                        ch_l ". . ." 
                                $ Girl.AddWord(1,0,0,"ex",0) #adds "ex" to traits
                        elif Girl.Obed >= Girl.Inbt:
                                #RogueX.Obed >= RogueX.Inbt:
                                $ Girl.Statup("Obed", 200, -10)
                                if Girl == RogueX:
                                        ch_r "You're abandoning me."
                                elif Girl == KittyX:
                                        ch_k "I'm[KittyX.like]not sure what to do next."
                                elif Girl == EmmaX:
                                        ch_e "I suppose I'll have to make do."
                                elif Girl == LauraX:
                                        ch_l "I'll need some new options." 
                                $ Girl.AddWord(1,0,0,"ex",0) #adds "ex" to traits
                        else:
                                #inbt highest
                                if Girl == RogueX:
                                        ch_r "Now who'll I fuck?" 
                                elif Girl == KittyX:
                                        ch_k "I guess I'll[KittyX.like]have to find someone else to bang?"
                                elif Girl == EmmaX:
                                        ch_e "I suppose I'll have other options."
                                elif Girl == LauraX:
                                        ch_l "Ok, later." 
                                #does not add "ex" to traits because she doesn't care that much
            
                $ Girl.DrainWord("dating",0,0,1) #removes "dating" from traits
                if Girl in Player.Harem:
                        $ Player.Harem.remove(Girl)
                
                $ Girl.Break[0] = 5 + Girl.Break[1] + Girl.Cheated
                $ Girl.Break[1] += 1
        #end "if you break up"
                
            
        else: #Stay together.
                $ Girl.FaceChange("smile")       
                call AnyLine(Girl,"I'm glad we could work things out. . .")         
                if Girl.Love >= Girl.Obed:
                        #RogueX.Love >= RogueX.Obed:
                        $ Girl.Statup("Love", 200, 3)
                        if Girl == RogueX:
                                ch_r "I'd really miss you."
                        elif Girl == KittyX:
                                ch_k "I'd[KittyX.like]totes miss you!"
                        elif Girl == EmmaX:
                                ch_e "I'm in too deep, [EmmaX.Petname]."
                        elif Girl == LauraX:
                                ch_l "I. . . care about you."
                elif Girl.Obed >= Girl.Inbt:
                        #RogueX.Obed >= RogueX.Inbt:
                        if Girl == RogueX:
                                ch_r "I need you with me."
                        elif Girl == KittyX:
                                ch_k "I'm[KittyX.like]totally all-in on this."
                        elif Girl == EmmaX:
                                ch_e "I don't think I could do without you."
                        elif Girl == LauraX:
                                ch_l "I need you too much."
                else:
                        #inbt highest, still a break-up, but friendly
                        if Girl == RogueX:
                                ch_r "We have fun together. Let's keep it at that." 
                        elif Girl == KittyX:
                                ch_k "You[KittyX.like]really dodged a bullet on that one."
                        elif Girl == EmmaX:
                                ch_e "It's too much trouble finding another toy."
                        elif Girl == LauraX:
                                ch_l "Ok, fine."
        $ Line = 0
        return
        #End Break-up
        
        
# End Break-up/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start checks for cheating and sharing / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label CheatCheck(BO=[],BO2=[]):
        # This checks whether any girl saw you with any other girl today. 
        # Called by EventCalls
        # If you're in the room with that girl, it launches the cheated scene, otherwise, it has her ask you about it later. 
        # Roster[Counter] is the first girl, Roster[Counter2] is the second girl
        # loops through girl 2 options until finished, then next girl 1 option, until done        
        
        # add an aspect to account for hooking up with multiple girls that have not yet been accounted for. . .        
        $ BO = TotalGirls[:]          
        $ renpy.random.shuffle(BO)
        while BO:       
                if "locked" in Player.Traits and BO[0].Loc != bg_current:
                        #exits if the door is locked and she is not in the room with you    
                        pass
                else:
                        $ BO2 = TotalGirls[:]  
                        while BO2:  
                            if "meet girl" in Player.DailyActions:
                                                #skips if you already have an appointment 
                                                return                                  
                            elif "dating" in BO[0].Traits or BO[0] in Player.Harem:
                                    #if "dating" in RogueX.Traits or RogueX in Player.Harem: 
                                    if "saw with " + BO2[0].Tag in BO[0].Traits:
                                                #if "saw with Kitty" in RogueX.Traits:      
                                                if BO[0] in Player.Harem and BO2[0] in Player.Harem:                
                                                        #if both girls were in the harem, this shouldn't happen 
                                                        $ BO[0].DrainWord("saw with "+BO2[0].Tag,0,0,1)      #removes "saw with Kitty" from traits  
                                                elif bg_current == "bg player" or bg_current == BO[0].Home:
                                                        call Cheated(BO[0],BO2[0])  
                                                        $ renpy.pop_call()
                                                        return       
                            $ BO2.remove(BO2[0])
                $ BO.remove(BO[0])
        return
        
        
#        $ Counter = 4 #len(Roster)-1   
#        while Counter:
#                $ Counter2 = 4 #len(Roster)-1 #resets Counter 2
#                while Counter2:
#                    if "meet girl" in Player.DailyActions:
#                                        #skips if you already have an appointment 
#                                        $ Counter = 1
#                                        $ Counter2 = 1                                    
#                    elif CheckWord(Roster[Counter],"Traits","dating") or Roster[Counter] in Player.Harem:
#                            #if "dating" in RogueX.Traits or RogueX in Player.Harem: 
#                            if CheckWord(Roster[Counter],"Traits","saw with "+Roster[Counter2]):
#                                        #if "saw with Kitty" in RogueX.Traits:      
#                                        if Roster[Counter] in Player.Harem and Roster[Counter2] in Player.Harem:                
#                                                #if both girls were in the harem, this shouldn't happen 
#                                                $ Roster[Counter].DrainWord("saw with "+Roster[Counter2],0,0,1)      #removes "saw with Kitty" from traits  
#                                        elif bg_current in  ("bg player","bg rogue","bg kitty","bg emma","bg laura"):
#                                                call Cheated(Roster[Counter],Roster[Counter2])  
#                                                $ renpy.pop_call()
#                                                return
#                                        else:
#                                                call AskedMeet(Roster[Counter],"angry")    
#                                                $ Counter = 1
#                                                $ Counter2 = 1             
#                    $ Counter2 -= 1
#                $ Counter -= 1
#        return

label ShareCheck(BO=[],BO2=[]):
        # This checks whether one of the girls is supposed to ask the other about joining the harem
        # Called by EventCalls
        # Roster[Counter] is the first girl, Roster[Counter2] is the second girl
        # loops through girl 2 options until finished, then next girl 1 option, until done        
                 
        $ BO = TotalGirls[:]  
        while BO: 
                if "dating" in BO[0].Traits or BO[0] in Player.Harem:
                        #if "dating" in RogueX.Traits or RogueX in Player.Harem: 
                        $ BO2 = TotalGirls[:]  
                        while BO2:     
                                if "ask " + BO2[0].Tag in BO[0].Traits:
                                        #if "ask Kitty" in RogueX.Traits:      
                                        if BO[0] in Player.Harem and BO2[0] in Player.Harem:                
                                                #if both girls were in the harem, this shouldn't happen 
                                                $ BO[0].DrainWord("ask "+BO2[0].Tag,0,0,1)      #removes "askKitty" from traits  
                                        else:
                                                call Share(BO[0],BO2[0])  
                                                $ renpy.pop_call()
                                                return  
                                $ BO2.remove(BO2[0])
                $ BO.remove(BO[0])
        return
        
label AddictCheck(BO=[]):
        # Called to see if the girl is in an addiction spiral
        # Called by EventCalls 
        $ BO = ActiveGirls[:]  
        $ renpy.random.shuffle(BO)
        while BO:   
                if "locked" in Player.Traits and BO[0].Loc != bg_current:
                        #if the door's locked and she's not in the room, skip it
                        pass
                elif "asked fix" in Player.DailyActions and "asked meet" not in BO[0].DailyActions:
                        #this skips any new girls if you've agreed to meet another one
                        pass
                elif BO[0].Event[3]:
                        #this skips if you've already dealt with her once recently
                        pass
                elif "angry" not in BO[0].RecentActions and "addiction" not in BO[0].DailyActions and BO[0].Action >= 1:                    
                        #Activates if she needs her fix
                        if BO[0].Addict >= 60 and BO[0].Resistance and BO[0].Event[1] >= 10:
                                #if addict over 60, and she's completed the event chain
                                if bg_current == BO[0].Home or bg_current == "bg player":
                                            call Addiction_Fix(BO[0])
                                else:
                                    if "asked meet" in BO[0].RecentActions:
                                            pass
                                    elif "asked meet" in BO[0].DailyActions and BO[0].Addict >= 80:
                                            "[BO[0].Name] texts you. . ."
                                            call AnyLine(BO[0],"I know I asked to meet you in your room earlier, but I'm serious, this is important.")
                                            $ Player.AddWord(1,"asked fix",0,0,0)
                                            $ BO[0].AddWord(1,"asked meet",0,0,0)
                                            return
                                    else:
                                            "[BO[0].Name] texts and asks if you could meet her in your room later."
                                            $ BO[0].AddWord(1,"asked meet","asked meet",0,0)
                                            return
                        #Activates if you don't need a fix but already have resistance                    
                        elif BO[0].Resistance:
                                pass                            
                        #These are the "first time addict" event chains
                        elif BO[0].Addict >= 35 and not BO[0].Event[1]:
                                #"I'm addicted" event
                                call First_Addicted(BO[0])            
                        elif BO[0].Addict >= 60 and BO[0].Event[1] <= 2:
                                #"I'm super-addicted" event
                                call First_Addicted(BO[0])            
                        elif BO[0].Addict >= 90:                   
                                #"I'm crazy-addicted" event
                                call First_Addicted(BO[0])  
                $ BO.remove(BO[0])
        return
        
        
label Share(Girl=0,Other=0): 
        # This checks when one girl asks another to share you.
        # it is called by Sharecheck 
                
        $ Girl.DrainWord("ask "+Other.Tag,0,0,1) #removes "ask Kitty" from RogueX.Traits 
                
        if Girl.Break[0]:
                #if the girl was only recently broken up with. . .
                "[Girl.Name] sends you a text."                
                $ Other.Statup("Love", 90, -10) 
                $ Other.Statup("Obed", 80, 10)
                $ Other.Statup("Inbt", 80, 5)   
                
                if Other == RogueX:
                        call AnyLine(Girl,"She said to \"stop bother'in her?\"") 
                elif Other == KittyX:
                        call AnyLine(Girl,"She said to \"give it a rest?\"") 
                elif Other == EmmaX:
                        call AnyLine(Girl,"She said \"when hell freezes over?\"") 
                elif Other == LauraX:
                        call AnyLine(Girl,"She said to \"fuck off?\"") 
                call AnyLine(Girl,"I guess we can see if she comes around on the idea.") 
                
        else:                                 
                if Other.GirlLikeCheck(Girl) >= 800 or ApprovalCheck(Other, 1800) or (ApprovalCheck(Other, 1500) and Other.GirlLikeCheck(Girl) >= 500):
                        # if she likes the other girl a lot, or likes you a lot, or sort of likes you both. . .                     
                        $ Other.AddWord(1,0,0,"poly "+Girl.Tag,0) #adds "dating" to KittyX.Traits
                        #$ Other.AddWord(1,0,0,"dating?",0) #adds "dating" to KittyX.Traits      
                                
                        $ Other.Statup("Obed", 80, 10)
                        $ Other.Statup("Inbt", 80, 15)  
                        
                        if Girl.Event[5]:
                                # if you've already done her BF event before. . .
                                $ Player.Harem.append(Other)             
                                $ Girl.AddWord(1,0,0,"dating",0)     #adds "dating" to traits                   
                        elif bg_current in ("bg rogue","bg kitty","bg emma","bg laura"):     
                                #if you're in a character room, launch their boyfriend speech
                                if Other.Tag+"Yes" not in Player.Traits: 
                                        $ Player.Traits.append(Other.Tag+"Yes")
                                call expression Other.Tag + "_BF" #call Rogue_BF 
                                $ renpy.pop_call() #skips return to ShareCheck
                                $ renpy.pop_call() #skips return to EventCalls
                        else:
                                # if not in a character room, ask later
                                if Other.Tag+"Yes" not in Player.Traits: 
                                        $ Player.Traits.append(Other.Tag+"Yes")
                                call AskedMeet(Other,"bemused")  
                else:                    
                        #If Kitty refuses to share you
                        "[Girl.Name] sends you a text."        
                        call AnyLine(Girl,"I talked to "+Other.Name+" about sharing you, and she said she wasn't into that sort of thing,") 
                        if not ApprovalCheck(Other, 2000):
                                $ Other.Statup("Love", 200, -15)
                                $ Other.Statup("Obed", 50, -5)
                                $ Other.Statup("Inbt", 50, 5)
                                call AnyLine(Girl,"She's just not into you like that.") 
                        else:
                                $ Other.Statup("Love", 200, -5)
                                call AnyLine(Girl,"She doesn't really like me that much. . .") 
                                
                        #means that she won't be available to ask again for another 7 days   
                        $ Other.Break[0] = 7
                        
        return
        
# Start Cheated on the girl / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Cheated(Girl=0,Other=0, Resolution = 0, B = 0):  
        # Called by EventCalls->CheatCheck if you got caught cheating
        #Resolution is Resolution count, you want this over 2 at least. B is the bonus modifier
        $ Girl.AddWord(1,0,"relationship",0,0)
        call Shift_Focus(Girl)
        
        $ Girl.FaceChange("angry") 
        if Girl.Loc != bg_current and Girl not in Party:
                "Suddenly, [Girl.Name] shows up and says she needs to talk to you." 
        $ Girl.Loc = bg_current
        
        $ Girl.DrainWord("asked meet",0,1) #removes "asked meet" from daily                
        if "meet girl" in Player.DailyActions:
                $ Player.DailyActions.remove("meet girl")
        
        call Set_The_Scene
        call CleartheRoom(Girl)
        call Taboo_Level(1)
        
        if Girl.GirlLikeCheck(Other) >= 900:
                $ Resolution += 2
        elif Girl.GirlLikeCheck(Other) >= 800:
                $ Resolution += 1
        $ B = int((Girl.GirlLikeCheck(Other) - 500)/2)    
       
        $ Resolution -= Girl.Cheated if Girl.Cheated <= 3 else 3 #Adds to Resolution 3 or less based on cheating
                
        if Girl.Cheated:
                $ Girl.Statup("Love", 200, -50) 
                $ Girl.Statup("Obed", 80, -20)
                $ Girl.Statup("Inbt", 50, -50)    
                if Girl == RogueX:
                        ch_r "Why're you screw'in around on me again?"
                elif Girl == KittyX:
                        ch_k "Again with this?!"
                elif Girl == EmmaX:
                        ch_e "I noticed you're back to jumping anything that moves. . ."
                elif Girl == LauraX:
                        ch_l "You were screwing someone else again." 
        else:
                $ Girl.Statup("Love", 200, -100) 
                $ Girl.Statup("Obed", 80, -30)
                $ Girl.Statup("Inbt", 50, -20) 
                if Girl == RogueX:
                        ch_r "What the hell was that about earlier?"  
                elif Girl == KittyX:
                        ch_k "Hello?! What was that?"
                elif Girl == EmmaX:
                        ch_e "Do you mind explaining what I saw earlier?"
                elif Girl == LauraX:
                        ch_l "You were with someone else earlier." 
            
        menu:
                extend ""
                "I'm sorry.":
                        $ Girl.Statup("Love", 90, 30) 
                        $ Girl.Statup("Obed", 80, -10)
                        $ Line = "sorry"     
                        $ Resolution += 1
                    
                "What do you mean?":
                        $ Girl.Statup("Love", 200, -10) 
                        $ Girl.Statup("Obed", 80, 15)
                        $ Girl.Statup("Inbt", 80, 5)   
                        
                        call AnyLine(Girl,"I mean you screwing around with "+Other.Name+"!")                          
                        menu:
                                extend ""
                                "Oh! I'm sorry!":         
                                    $ Girl.Statup("Love", 90, 20) 
                                    $ Girl.Statup("Obed", 80, -10)           
                                    $ Line = "sorry"
                                "Oh, that. Yeah.":
                                    $ Girl.Statup("Love", 200, -20) 
                                    $ Girl.Statup("Obed", 80, 10)  
                                    $ Line = "yeah"
                                    $ Resolution -= 1
                            
                "You mean with [Other.Name]?":
                        $ Girl.Statup("Love", 200, -15) 
                        $ Girl.Statup("Obed", 80, 20)
                        $ Girl.Statup("Inbt", 80, 10)  
                        call AnyLine(Girl,"Yes, \"I mean with "+Other.Name+".\"")                      
                        
                        if Girl == RogueX:
                                $ Line = "Y'all were screwing around behind my back!"
                        elif Girl == KittyX:
                                $ Line = "Why were you all over her like that?!"
                        elif Girl == EmmaX:
                                $ Line = "Or didn't you notice who you were fucking?"
                        elif Girl == LauraX:                                
                                $ Line = "I can smell her on you." 
                        
                        if Girl.Cheated:
                            $ Line = Line+" again!"
                        call AnyLine(Girl,Line)
                        menu: 
                                extend ""
                                "Oh! I'm sorry!":
                                    $ Girl.Statup("Love", 90, 15) 
                                    $ Girl.Statup("Obed", 80, -10)                            
                                    $ Line = "sorry"
                                "Oh, yeah.":
                                    $ Girl.Statup("Love", 200, -20) 
                                    $ Girl.Statup("Obed", 80, 10)  
                                    $ Line = "yeah"
                                    $ Resolution -= 2
                
        if Line == "sorry":  
                    $ Girl.FaceChange("sadside")
                    if Girl == RogueX:
                            ch_r "Well 'course you are, but that don't make it right."
                            ch_r "Screwing around with [Other.Name] like that. . ."   
                    elif Girl == KittyX:
                            ch_k "Don't you tell me you're sorry, I'll tell you when you're sorry!"
                    elif Girl == EmmaX:
                            ch_e "Very sorry indeed. . ."
                    elif Girl == LauraX:
                            ch_l "You will be."                             
                    $ Girl.FaceChange("sad")
        else:                         
                    $ Girl.FaceChange("confused")
                    if Girl == RogueX:
                            ch_r "Oh? So what do you have to say for yourself?"
                    elif Girl == KittyX:
                            ch_k "Yeah? Yeah?! What does that even mean?!"
                    elif Girl == EmmaX:
                            ch_e "I'm not sure you understand what trouble you're in here. . ."
                    elif Girl == LauraX:
                            ch_l "So did you have an explanation, or. . ."        
                    $ Girl.FaceChange("angry")
        
        menu:
                extend ""
                "I really hurt you, and I'm sorry.":
                        $ Girl.Statup("Love", 90, 25) 
                        $ Girl.Statup("Obed", 80, -5)
                        call AnyLine(Girl,"Well at least you're owning up to it.")
                        $ Resolution += 2
                    
                "We were just messing around, nothing serious.":
                        $ Girl.Statup("Love", 200, -25) 
                        $ Girl.Statup("Obed", 80, 30)
                        $ Girl.Statup("Inbt", 80, 10)  
                        if Girl == RogueX:
                                ch_r "\"Nothing serious?\" You did {i}not{/i} just tell me that."
                        elif Girl == KittyX:
                                ch_k "I'll \"nothing serious\" you!"
                        elif Girl == EmmaX:
                                ch_e "I'll be the judge of what is or is not \"serious.\""
                        elif Girl == LauraX:
                                if ApprovalCheck(Girl, 1500):
                                        ch_l "Ok, that's fair." 
                                else:
                                        ch_l "Do you want to try that one again?"   
                                
                        if not ApprovalCheck(Girl, 700, "O", Bonus = (B/3)):
                            $ Resolution -= 2
                    
                "I think she's really cute.":
                    if B >= 100 or ApprovalCheck(Girl, 500, "I", Bonus = (B/3)):  
                            # if Like trait is 700 or more. . .
                            $ Girl.FaceChange("confused",Eyes="side")
                            if Other == KittyX:
                                    call AnyLine(Girl,"Well. . . yeah, she is cute, but so what?")  
                            else:
                                    call AnyLine(Girl,"Well. . . yeah, she is hot, but so what?")                  
                            $ Girl.Statup("Lust", 90, 5)
                            $ Line = "threeway"  
                    else:
                            $ Girl.Statup("Love", 200, -20) 
                            $ Girl.Statup("Obed", 80, 30)
                            if Girl == RogueX:
                                    ch_r "Well that don't mean shit, [Player.Name], you're with me!"
                            elif Girl == KittyX:
                                    ch_k "What does that have to do with anything?!"
                            elif Girl == EmmaX:
                                    ch_e "But I am here. [[gestures to encompass her body]"
                            elif Girl == LauraX:
                                    ch_l "That doesn't make her fair game."   
                            $ Resolution -= 2
                    
                "Don't you like her?":
                    $ Girl.Statup("Obed", 80, 30)
                    if B >= 100 or ApprovalCheck(Girl,500,"I"):        
                            # if Like trait is 700 or more. . .    
                            $ Girl.FaceChange("confused",Eyes="side")
                            $ Girl.Statup("Inbt", 90, 25)                  
                            $ Girl.Statup("Lust", 90, 5)
                            if Girl == RogueX:
                                    ch_r "I mean, sorta. Not like that really though. . ." 
                            elif Girl == KittyX:
                                    ch_k "What, like. . . \"like\" like? Um. . ."
                            elif Girl == EmmaX:
                                    ch_e "She is attractive, yes, but I don't think that's relevant."
                            elif Girl == LauraX:
                                    ch_l "Yeah, but I like you too."    
                            $ Line = "threeway" 
                    elif B >= 50:    
                            # if Like trait is 600 or more. . .  
                            $ Girl.FaceChange("confused")
                            $ Girl.Statup("Love", 200, -10)
                            if Girl == EmmaX:
                                    ch_e "She's a good student, but that doesn't mean I'm interested in sharing."
                            else:
                                    call AnyLine(Girl,"We're friends, but so what?")    
                    else:
                            $ Girl.Statup("Love", 200, -20) 
                            if Girl == RogueX:
                                    ch_r "Whether I like her or not, don't give you rights to hook up with her."
                            elif Girl == KittyX:
                                    ch_k "What does that have to do with anything?!"
                            elif Girl == EmmaX:
                                    ch_e "That's entirely irrelevant!"
                            elif Girl == LauraX:
                                    ch_l "Not enough to share."   
                            $ Resolution -= 1
                  
        menu:
                "I won't do it again.":
                    if Girl.Cheated:        
                            $ Girl.Statup("Love", 90, 5)  
                            call AnyLine(Girl,"Like the last time you told me that, you mean?")                    
                            $ Resolution -= 1
                    else:
                            $ Girl.Statup("Love", 90, 20) 
                            $ Girl.FaceChange("angry")
                            $ Resolution += 2 if Resolution < 3 else 0
                            call AnyLine(Girl,"I'll hold you to that.")
                    $ Line = 0
                        
                "I can't make any promises, she's pretty hot.":
                            $ Girl.FaceChange("angry")
                            $ Girl.Statup("Love", 200, -40) 
                            $ Girl.Statup("Obed", 90, 40)
                            $ Girl.Statup("Inbt", 90, 10)  
                            call AnyLine(Girl,"Then I don't know what you tell you, I think we're through.")
                            $ Resolution -= 2
                            $ Line = 0
                    
                "Have you considered maybe letting her join us?":
                        $ Girl.FaceChange("confused",Mouth="smile")
                        if ApprovalCheck(Girl, 2200, Bonus = B) or ApprovalCheck(Girl, 950, "L", Bonus = (B/3)):
                                $ Girl.Statup("Inbt", 90, 30)                  
                                $ Girl.Statup("Lust", 89, 10)
                                $ Resolution += 2
                        elif ApprovalCheck(Girl, 1500, Bonus = B) or Girl.GirlLikeCheck(Other) >= 700:
                                $ Girl.Statup("Inbt", 90, 10)                  
                                $ Girl.Statup("Lust", 90, 5)
                        else:
                                $ Resolution -= 3
                                $ Girl.Statup("Love", 200, -25) 
                                $ Girl.Statup("Inbt", 90, 10) 
                            
                        $ Girl.Statup("Obed", 90, 40) 
                        if Girl == RogueX:
                                ch_r "I don't know what to do with that, you talk'in a three-way?"
                        elif Girl == KittyX:
                                ch_k "What, like a threeway?"
                        elif Girl == EmmaX:
                                ch_e "I'm not sure how to process that."
                                ch_e "Are you suggesting a threeway?"
                        elif Girl == LauraX:
                                ch_l "You wanna fuck both of us?"   
                        $ Line = "threeway"
        
        if Resolution >= 5 and Line == "threeway": #she agrees to a threeway
                        if Girl.Cheated:
                                $ Girl.Statup("Love", 90, 25) 
                                $ Girl.Statup("Obed", 90, 30)
                                $ Girl.Statup("Inbt", 90, 60)   
                        else:
                                $ Girl.Statup("Love", 90, 50) 
                                $ Girl.Statup("Obed", 90, 40)
                                $ Girl.Statup("Inbt", 90, 40)
                        if Girl == RogueX:
                                ch_r "So I catch you fool'in around on me, and you want to make it official?"
                        elif Girl == KittyX:
                                ch_k "So you cheat on me, and then ask for a threeway?"
                        elif Girl == EmmaX:
                                ch_e "Bold move. Boldness should be rewarded. . ."
                        elif Girl == LauraX:
                                ch_l "Cheat on me, and then Ask for a threeway?"
                                ch_l "Risky gamble there."   
                        call AnyLine(Girl,"Maybe I could live with that, I'll talk to "+Other.Name+".")
                                
                        $ Line = "poly"
                            
        elif Resolution >= 5: #she suggests a threeway
                        if Girl.Cheated:
                                $ Girl.Statup("Love", 90, 20) 
                                $ Girl.Statup("Obed", 90, 10)
                                $ Girl.Statup("Inbt", 90, 100)   
                        else:
                                $ Girl.Statup("Love", 90, 40) 
                                $ Girl.Statup("Obed", 90, 10)
                                $ Girl.Statup("Inbt", 90, 60) 
                        if Girl == RogueX:
                                ch_r "You're just a regular polecat in heat. I guess I can't tame you."
                                ch_r "Not alone, at least."
                        elif Girl == KittyX:
                                ch_k "What a mess. I guess maybe I could share though. . ."
                        elif Girl == EmmaX:
                                ch_e "Bold move. Boldness should be rewarded. . ."
                        elif Girl == LauraX:
                                ch_l "You're a piece of work, but maybe I could share . . ."
                                
                        if Girl == EmmaX:
                                call AnyLine(Girl,"Perhaps "+Other.Name+" and I could work something out.")
                        else:
                                call AnyLine(Girl,"Maybe me and "+Other.Name+" can work something out.")
                        $ Line = "poly"
                            
        elif Resolution >= 2: #she agrees to forgive you   
                    if Line == "threeway":
                            #you've asked for a threeway, btu she knocked it down
                            $ Girl.Statup("Obed", 80, 10)       
                            if Girl == RogueX:
                                    ch_r "Don't try to play cards ya just don't have."
                            elif Girl == KittyX:
                                    ch_k "Way to read the room. . ."
                            elif Girl == EmmaX:
                                    ch_e "I appreciate the initiative, if not the common sense. . ."
                            elif Girl == LauraX:
                                    ch_l "Like that'll happen . . ."
                    $ Girl.FaceChange("sadside")
                    if Girl.Cheated:     
                            $ Girl.Statup("Obed", 80, 15)       
                            if Girl == RogueX:
                                    ch_r "I've given you a chance to do right by me, and you keep screwing it up."
                                    ch_r "I don't know how many more chances I can give you here."
                            elif Girl == KittyX:
                                    ch_k "Too many times, [KittyX.Petname]. . ."
                            elif Girl == EmmaX:
                                    ch_e "At some point I'll have to stop putting up with you. . ."
                            elif Girl == LauraX:
                                    ch_l "This is getting tired . . ."
                    else:
                            $ Girl.Statup("Obed", 80, 30) 
                            if Girl == RogueX:
                                    ch_r "You betrayed my trust, [RogueX.Petname]."
                                    ch_r "Don't let it happen again." 
                            elif Girl == KittyX:
                                    ch_k "You hurt me here, [KittyX.Petname]. . ."
                                    ch_k "Don't hurt me like this again."
                            elif Girl == EmmaX:
                                    ch_e "I'll let you off with a warning this time, but don't let it happen again."
                            elif Girl == LauraX:
                                    ch_l "I'll let you off this time, but don't push it."
                        
        else: 
                    #she doesn't agree to forgive you
                    $ Girl.FaceChange("angry")
                    if Line == "threeway":
                        $ Girl.Statup("Obed", 80, 10)       
                        if Girl == RogueX:
                                ch_r "I can't even believe you would suggest a fucking {i}threeway!{/i}"
                        elif Girl == KittyX:
                                ch_k "Seriously? A threeway?!"
                        elif Girl == EmmaX:
                                ch_e "Bold move. Sometimes boldness will get you hurt. . ."
                        elif Girl == LauraX:
                                ch_l "A threeway?"
                    if Girl.Cheated:         
                        $ Girl.Statup("Obed", 90, -50)
                        $ Girl.Statup("Inbt", 90, 20)  
                        if Girl == RogueX:
                                ch_r "You done this too many times for me to keep let'in you back."
                                ch_r "Sorry, [RogueX.Petname], this is the end."
                        elif Girl == KittyX:
                                ch_k "You aren't even that cute. . ."
                                ch_k "We're over."
                        elif Girl == EmmaX:
                                ch_e "I don't think I'm in the mode for these games."
                                ch_e "We're done." 
                        elif Girl == LauraX:
                                ch_l "I hoped I could trust you, but you blew it again. . ."
                    else:
                        $ Girl.Statup("Obed", 90, -50)
                        $ Girl.Statup("Inbt", 90, 10)  
                        if Girl == RogueX:
                                ch_r "I just don't think I can trust you anymore, [RogueX.Petname]."
                                ch_r "This is it for us." 
                        elif Girl == KittyX:
                                ch_k "You hurt me. I just can't even."
                        elif Girl == EmmaX:
                                ch_e "You've lost my trust. We're done here."
                        elif Girl == LauraX:
                                ch_l "I can't trust you. I'm through."
                        
                    $ Girl.AddWord(1,0,0,"ex",0) #adds "ex" to traits
                    $ Girl.DrainWord("dating",0,0,1) #removes "dating" from traits
                    if Girl in Player.Harem:
                            $ Player.Harem.remove(Girl)
                    $ Girl.AddWord(1,0,"angry",0,0)                    
                  
#        $ Girl.DrainWord("saw with " + Other,0,0,1)      #removes "saw with Kitty" from traits    
        
        $ BO = TotalGirls[:]  
        while BO:        
                #removes "saw with Rogue" from traits  
                $ Girl.DrainWord("saw with "+BO[0].Tag,0,0,1)  
                $ BO.remove(BO[0])
                        
        if Line == "poly":       
                $ Girl.AddWord(1,0,0,"poly "+Other.Tag,0)    #adds "poly Kitty" to traits
                $ Girl.AddWord(1,0,0,"ask "+Other.Tag,0)     #adds "ask Kitty" to traits
        else:
                $ Girl.GLG(Other,1000,-50,1)   #$ RogueX.LikeKitty -= 50
                    
        if "ex" in Girl.Traits:
            $ Girl.Break[0] = 5 + Girl.Break[1] + Girl.Cheated
        $ Girl.Cheated += 1
        
        #aftermath
        menu:
                "I'm glad we could work this out." if "dating" in Girl.Traits or Girl in Player.Harem:
                        $ Girl.FaceChange("sad") 
                        if Resolution >= 3:            
                                $ Girl.Statup("Love", 90, 10) 
                                $ Girl.Statup("Obed", 90, 5) 
                                if Girl == RogueX:
                                        ch_r "I am too, [RogueX.Petname]."
                                elif Girl == KittyX:
                                        ch_k "Me too, [KittyX.Petname]. . ."
                        else:
                                $ Girl.Statup("Love", 90, 5) 
                                if Girl == RogueX:
                                        ch_r "Yeah, we'll see, [RogueX.Petname]."
                                elif Girl == KittyX:
                                        ch_k "Sure, [KittyX.Petname]. . ."
                        if Girl == EmmaX:
                                ch_e "Yes, delightful."
                        elif Girl == LauraX:
                                ch_l "Yeah, sure."
                        
                "Want to fool around a bit?" if ("dating" in Girl.Traits or Girl in Player.Harem) and not Taboo:
                        if Girl.Obed + Girl.Inbt >= (1.5 * Girl.Love) or ApprovalCheck(Girl,70,"X"): 
                            #(Obed + Inbt) >= (1.5 * Love) or Lust >= 70
                            $ Girl.FaceChange("sly",Eyes="side")
                            $ Girl.Statup("Love", 90, 20) 
                            $ Girl.Statup("Obed", 90, 10)
                            $ Girl.Statup("Inbt", 90, 10)
                            call AnyLine(Girl,"Sure, whatever.")
                            call expression Girl.Tag + "_SexMenu" #call Rogue_SexMenu 
                        else:        
                            $ Girl.FaceChange("sad")             
                            $ Girl.Statup("Love", 90, -10) 
                            $ Girl.Statup("Obed", 90, -10)
                            if Girl == RogueX:
                                    ch_r "It's still too raw, [RogueX.Petname]."
                            elif Girl == KittyX:
                                    ch_k "Don't even, [KittyX.Petname]. . ."
                            elif Girl == EmmaX:
                                    ch_e "Oh, this is rich."
                            elif Girl == LauraX:
                                    ch_l "Yeah, not now."
                        
                "I'm sorry it didn't work out." if "dating" not in Girl.Traits and Girl not in Player.Harem: 
                            $ Girl.FaceChange("sad") 
                            $ Girl.Statup("Love", 90, 10) 
                            if Girl == RogueX:
                                    ch_r "I am too, [RogueX.Petname]."
                            elif Girl == KittyX:
                                    ch_k "Yeah, me too, [KittyX.Petname]. . ."
                            elif Girl == EmmaX:
                                    ch_e "Yes, you;ll get over it. . . eventually."
                            elif Girl == LauraX:
                                    ch_l "Yeah."
                        
                "Want to have some break-up sex?" if ("dating" not in Girl.Traits and Girl not in Player.Harem) and not Taboo:
                        if Girl.Obed + Girl.Inbt >= (1.5 * Girl.Love) or ApprovalCheck(Girl,70,"X"): 
                            #(Obed + Inbt) >= (1.5 * Love) or Lust >= 70
                            $ Girl.FaceChange("angry",Eyes="side")
                            $ Girl.Statup("Obed", 90, 10)
                            $ Girl.Statup("Inbt", 90, 10)
                            call AnyLine(Girl,"Sure, whatever.")
                            $ Girl.DrainWord("angry",0,1)
                            call expression Girl.Tag + "_SexMenu" #call Rogue_SexMenu 
                            $ Girl.AddWord(1,0,"angry",0,0) #adds "angry" to daily
                        else:
                            $ Girl.FaceChange("angry")
                            $ Girl.Statup("Love", 90, -20) 
                            $ Girl.Statup("Obed", 90, -10)
                            if Girl == RogueX:
                                    ch_r "You have got to be kidding me."
                            elif Girl == KittyX:
                                    ch_k "Don't even, [KittyX.Petname]. . ."
                            elif Girl == EmmaX:
                                    ch_e "Oh, this is rich."
                            elif Girl == LauraX:
                                    ch_l "Yeah, not now."
                        
                "Let me know if you change your mind." if"dating" not in Girl.Traits and Girl not in Player.Harem:
                            $ Girl.FaceChange("angry",Eyes="side")
                            $ Girl.Statup("Love", 90, -5) 
                            $ Girl.Statup("Obed", 90, 10)
                            if Girl == RogueX:
                                    ch_r "Yeah, I'll get right on that."
                            elif Girl == KittyX:
                                    ch_k "Oh, sure, right."
                            elif Girl == EmmaX:
                                    ch_e "Oh, I'm sure you'll be the first I tell."
                            elif Girl == LauraX:
                                    ch_l "Uh-huh."
                    
                "Ok, see you later then.":
                            $ Girl.FaceChange("confused")
        
        if Girl == RogueX:
                ch_r "I need some time alone, [RogueX.Petname]. I'll see you later."
        elif Girl == KittyX:
                ch_k "I need some \"me\" time, I'll see you around."
        elif Girl == EmmaX:
                ch_e "Now, I need to be alone for a bit."
        elif Girl == LauraX:
                ch_l "Ok, well, bye."                  
                
        $ Round -= 10 if Round > 10 else Round
        
        if bg_current in ("bg rogue","bg kitty","bg emma","bg laura"):
                #remove Rogue from the scene (or the player)
                $ bg_current = "bg player"
#                $ renpy.pop_call() #removes call to Events
                $ renpy.pop_call() #removes call to Asked
                $ renpy.pop_call() #removes call to Cheated
                jump Player_Room
        else:
                call Remove_Girl(Girl)
        return

# end Cheated on the Girl / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start No Fapping / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    

label NoFap(Girl=0,TabStore=Taboo,Cnt=0):
        # called when you ask them not to fap from the romance menu
        # call NoFap(Girl)
        
        $ Taboo = 0
        ch_p "About when you masturbate on your own time. . ." 
        
        if "askedfap" in Girl.DailyActions:
                #if it's not the first time you've asked today. . .
                if "nofap" in Girl.Traits:
                        call AnyLine(Girl,"I understand already.")
                else:
                        call AnyLine(Girl,"Stop bothering me with this.")
            
        elif "askedfap" in Girl.History:
                #if it's not the first time you asked. . .
                if not ApprovalCheck(Girl, 800):
                        #rude response
                        $ Girl.FaceChange("angry",2,Eyes="surprised")  
                        $ Girl.Statup("Love", 80, -1) 
                        $ Girl.Statup("Obed", 50, 1)
                        $ Girl.Statup("Obed", 80, 1)
                        $ Girl.Statup("Inbt", 30, -1)
                        $ Girl.Statup("Inbt", 30, 3, 1)
                        if Girl == RogueX:
                                ch_r "I really don't want to go over this again. . ."
                        elif Girl == KittyX:
                                ch_k "This isn't really appropriate. . . "
                        elif Girl == EmmaX:
                                ch_e "I'd rather not discuss this again. . ."
                        elif Girl == LauraX:                
                                ch_l "Hmm, I don't want to have this conversation again."  
                        $ Girl.FaceChange("angry",1)             
                else:
                        #neutral response
                        $ Girl.Statup("Obed", 60, 2)
                        $ Girl.Statup("Obed", 90, 1)
                        $ Girl.Statup("Inbt", 60, 1)
                        $ Girl.Statup("Lust", 50, 1)
                        $ Girl.FaceChange("confused",1)  
                        if Girl == EmmaX:
                                ch_e "Oh? This again?"
                        elif Girl == LauraX:                
                                ch_l "Yeah?"       
                        else: #Rogue, Kitty
                                $ Girl.FaceChange("confused",2)  
                                call AnyLine(Girl,"Um, yeah, what about it?")  
                                
        else:            
                #if this is the first time you've asked her. . .
                if not ApprovalCheck(Girl, 800):
                        #rude response
                        $ Girl.FaceChange("angry",2,Eyes="surprised")  
                        $ Girl.Statup("Love", 90, -5) 
                        $ Girl.Statup("Obed", 50, 3)
                        $ Girl.Statup("Obed", 80, 1)
                        $ Girl.Statup("Inbt", 30, -1)
                        $ Girl.Statup("Inbt", 30, 3, 1)
                        if Girl == RogueX:
                                ch_r "Don't go talk'in about a girl's personal time like that."
                        elif Girl == KittyX:
                                ch_k "I, um. . . "
                                extend "hey! That's not any of your business!"
                        elif Girl == EmmaX:
                                ch_e "What I do in the privacy of my own class-"
                                ch_e "Never mind."
                        elif Girl == LauraX:                
                                ch_l "Hmm, I don't want to have this conversation."  
                        $ Girl.FaceChange("angry",1) 
                elif not ApprovalCheck(Girl, 500, "I"): # or RogueX.SEXP <= 30?
                        #shy response        
                        $ Girl.Statup("Love", 90, -5) 
                        $ Girl.Statup("Obed", 50, 3)
                        $ Girl.Statup("Obed", 80, 1)
                        $ Girl.Statup("Inbt", 30, -1)
                        $ Girl.Statup("Inbt", 30, 3, 1)
                        $ Girl.Statup("Lust", 50, 3)
                        if Girl == RogueX:
                                $ Girl.FaceChange("surprised",2) 
                                ch_r "I. .  um. . I don't really do that. . ."
                        elif Girl == KittyX:
                                $ Girl.FaceChange("surprised",2) 
                                ch_k "Oh, um, that's not really something I. . ."
                        elif Girl == EmmaX:
                                $ Girl.FaceChange("confused",1) 
                                ch_e "I'm not sure why what I do in private is your business. . ."
                        elif Girl == LauraX:    
                                $ Girl.FaceChange("surprised",2)             
                                ch_l "Um. . . yeah?"            
                elif ApprovalCheck(Girl, 500, "O"):
                        #submissive response 
                        $ Girl.Statup("Obed", 90, 5)
                        $ Girl.Statup("Inbt", 50, 2)
                        $ Girl.Statup("Inbt", 80, 1)
                        $ Girl.Statup("Lust", 50, 5)
                        $ Girl.FaceChange("confused",1)  
                        if Girl == EmmaX:
                                ch_e "What of it?"
                        else: #Rogue, Kitty, Laura
                                call AnyLine(Girl,"What about it?")
                else:
                        #neutral response
                        $ Girl.Statup("Obed", 90, 4)
                        $ Girl.Statup("Inbt", 90, 3)
                        $ Girl.Statup("Lust", 50, 3)
                        $ Girl.FaceChange("confused",1)  
                        if Girl == EmmaX:
                                ch_e "Oh? What about it?"
                        elif Girl == LauraX:                
                                ch_l "Yeah?"       
                        else: #Rogue, Kitty
                                $ Girl.FaceChange("confused",2)  
                                call AnyLine(Girl,"Um, yeah, what about it?")  
        #end intro check. . .
        
        menu:
            extend ""
            "I'd rather you not do that." if "nofap" not in Girl.Traits:
                    if "askedfap" not in Girl.DailyActions:
                            $ Girl.Statup("Obed", 200, 2)
                            $ Girl.Statup("Inbt", 90, 1)
                    if ApprovalCheck(Girl, 1400, "LO"):
                            #loving response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, 4) 
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Inbt", 90, 3)
                            $ Girl.FaceChange("bemused",2) 
                            if Girl == RogueX:
                                    ch_r "Well, only because it seems to matter to you. . ."
                            elif Girl == KittyX:
                                    ch_k "You really care about something like that?"
                                    ch_k "Ok, fine."
                            elif Girl == EmmaX:
                                    ch_e "[EmmaX.Petname], the idea of it really bothers you?"
                                    ch_e "Fine, I can make do. . ."
                            elif Girl == LauraX:                
                                    ch_l "So, that'd really bother you? . ."
                                    ch_l "I guess I could stop. . ."
                            $ Girl.FaceChange("bemused",1) 
                    elif ApprovalCheck(Girl, 1600) and not ApprovalCheck(Girl, 500, "I"):
                            #shy response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Inbt", 90, 5)
                                    $ Girl.Statup("Lust", 50, 5)
                            $ Girl.FaceChange("bemused",2,Eyes="side") 
                            if Girl == RogueX:
                                    ch_r "Not that I was, but. . . sure."
                            elif Girl == KittyX:
                                    ch_k "I don't. . . right, I don't."
                            elif Girl == EmmaX:
                                    ch_e "I suppose if it matters to you. . ."
                            elif Girl == LauraX:                
                                    ch_l "I guess if it matters to you. . ." 
                            $ Girl.FaceChange("bemused",1)   
                    elif ApprovalCheck(Girl, 700, "O"):
                            #submissive response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, 3) 
                                    $ Girl.Statup("Obed", 200, 4)
                                    $ Girl.Statup("Inbt", 90, 5)
                                    $ Girl.Statup("Lust", 70, 5)
                            $ Girl.FaceChange("sly",1) 
                            if Girl == RogueX:
                                    ch_r "Yes, [RogueX.Petname]."
                            elif Girl == KittyX:
                                    ch_k "Yes, [KittyX.Petname]."
                            elif Girl == EmmaX:
                                    ch_e "Yes, [EmmaX.Petname]."
                            elif Girl == LauraX:                
                                    ch_l "Yes, [LauraX.Petname]." 
                    elif not ApprovalCheck(Girl, 800):
                            #rude response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, -5) 
                                    $ Girl.Statup("Obed", 90, -3)
                                    $ Girl.Statup("Inbt", 90, 3)
                            $ Girl.FaceChange("angry",2) 
                            if Girl == KittyX:
                                    ch_k "I- this whole conversation is inappropriate!"
                            elif Girl == EmmaX:
                                    ch_e "I really don't care what \"you'd rather.\""
                            else: #Rogue, Laura
                                    call AnyLine(Girl,"I'd rather you stay out my business.")
                            $ Girl.FaceChange("angry",1) 
                            $ Cnt = 1
                    else:
                            #no
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, -1) 
                                    $ Girl.Statup("Obed", 70, 2)
                                    $ Girl.Statup("Inbt", 60, 2)
                            $ Girl.FaceChange("sly",1) 
                            if Girl == RogueX:
                                    ch_r "'Fraid not, [RogueX.Petname]."
                            elif Girl == KittyX:
                                    ch_k "Sorry, no. I try to keep busy."
                            elif Girl == EmmaX:
                                    ch_e "No, I think I shall. . . often."
                            elif Girl == LauraX:                
                                    ch_l "Sorry, [LauraX.Petname], I've got needs."   
                            $ Cnt = 1
                    if not Cnt:
                            $ Girl.AddWord(1,0,0,"nofap")  #adds "nofap" tag to traits 
            # end "ask nicely"
                            
            "Don't do that without permission." if "nofap" not in Girl.Traits:
                    if "askedfap" not in Girl.DailyActions:
                            $ Girl.Statup("Obed", 200, 3)
                    if ApprovalCheck(Girl, 600, "O"):
                            #submissive response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, 3) 
                                    $ Girl.Statup("Obed", 80, 3)
                                    $ Girl.Statup("Obed", 200, 4)
                                    $ Girl.Statup("Inbt", 90, 5)
                                    $ Girl.Statup("Lust", 50, 5)
                                    $ Girl.Statup("Lust", 70, 5)
                            $ Girl.FaceChange("sly") 
                            if Girl == RogueX:
                                    ch_r "Yes, [RogueX.Petname]."
                            elif Girl == KittyX:
                                    ch_k "Yes, [KittyX.Petname]."
                            elif Girl == EmmaX:
                                    ch_e "Yes, [EmmaX.Petname]."
                            elif Girl == LauraX:                
                                    ch_l "Yes, [LauraX.Petname]."  
                    elif ApprovalCheck(Girl, 1200, "LO"):
                            #positive response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, 4) 
                                    $ Girl.Statup("Obed", 80, 3)
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Inbt", 90, 3)
                                    $ Girl.Statup("Lust", 50, 5)
                            $ Girl.FaceChange("bemused",1) 
                            if Girl == RogueX:
                                    ch_r "I guess if it means so much to you. . ."
                            elif Girl == KittyX:
                                    ch_k "I guess I could do \"no fap no-\" what month even is this? . ."
                            elif Girl == EmmaX:
                                    ch_e "Well, aren't you being dominant. . ."
                                    ch_e "I suppose I could restrain myself. . ."
                            elif Girl == LauraX:                
                                    ch_l "I guess I could."   
                    elif not ApprovalCheck(Girl, 500, "I"):
                            #shy response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Inbt", 90, 5)
                                    $ Girl.Statup("Lust", 50, 5)
                            $ Girl.FaceChange("bemused",2,Eyes="side") 
                            if Girl == RogueX:
                                    ch_r "It's not like I even do. . ."
                            elif Girl == KittyX:
                                    ch_k "Girls don't do that. But even if I did, you're being rude."
                            elif Girl == EmmaX:
                                    ch_e "I really don't think it's any of your business."
                            elif Girl == LauraX:                
                                    ch_l "Not interested."   
                            $ Girl.FaceChange("normal",1) 
                            $ Cnt = 1
                    elif not ApprovalCheck(Girl, 800):
                            #rude response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 70, -5) 
                                    $ Girl.Statup("Love", 90, -5) 
                                    $ Girl.Statup("Obed", 60, -3)
                                    $ Girl.Statup("Obed", 90, -3)
                                    $ Girl.Statup("Inbt", 90, 3)
                            $ Girl.FaceChange("angry",2) 
                            if Girl == RogueX:
                                    ch_r "Fuck you I won't."
                            elif Girl == KittyX:
                                    ch_k "I- this whole conversation is inappropriate!"
                            elif Girl == EmmaX:
                                    ch_e "I really don't think it's any of your business."
                            elif Girl == LauraX:                
                                    ch_l "Don't tell me what to do."   
                            $ Girl.FaceChange("angry",1) 
                            $ Cnt = 1
                    else:
                            #no
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, -2) 
                                    $ Girl.Statup("Obed", 70, -2)
                                    $ Girl.Statup("Inbt", 60, 2)
                            $ Girl.FaceChange("bemused",2) 
                            if Girl == RogueX:
                                    ch_r "'Fraid not, [RogueX.Petname]."
                            elif Girl == KittyX:
                                    ch_k "Sorry, no. I try to keep busy."
                            elif Girl == EmmaX:
                                    ch_e "No, I think I shall. . . often."
                            elif Girl == LauraX:                
                                    ch_l "Sorry, [LauraX.Petname], I've got needs."   
                            $ Girl.FaceChange("bemused",1) 
                            $ Cnt = 1
                    if not Cnt:
                            $ Girl.AddWord(1,0,0,"nofap")  #adds "nofap" tag to traits 
            # end "obedience order"
            
            "You can do that if you need to." if "nofap" in Girl.Traits:
                    if "askedfap" not in Girl.DailyActions:
                            $ Girl.Statup("Love", 90, 1) 
                            $ Girl.Statup("Obed", 90, 1)
                            $ Girl.Statup("Inbt", 90, 1)
                    if not ApprovalCheck(Girl, 500, "I"):
                            #shy response
                            if "okfap" not in Girl.History:
                                    $ Girl.Statup("Love", 60, 1) 
                                    $ Girl.Statup("Love", 90, 5) 
                                    $ Girl.Statup("Obed", 60, 3)
                                    $ Girl.Statup("Inbt", 70, 5)
                                    $ Girl.Statup("Lust", 90, 10)
                            $ Girl.FaceChange("confused",2) 
                            if Girl == RogueX:
                                    ch_r "Right! Not that I ever do that anyway, of course. . ."
                            elif Girl == KittyX:
                                    ch_k "Oh? Um, thanks?"
                            elif Girl == EmmaX:
                                    ch_e "I'm glad that I have your permission. . ."
                            elif Girl == LauraX:                
                                    ch_l "Good to know."   
                            $ Girl.FaceChange("smile",1) 
                    elif ApprovalCheck(Girl, 750, "O"):
                            #submissive response
                            if "okfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, 20) 
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Obed", 90, 10)
                                    $ Girl.Statup("Inbt", 90, 10)
                                    $ Girl.Statup("Lust", 90, 10)
                            $ Girl.FaceChange("sly",1) 
                            if Girl == RogueX:
                                    ch_r "Ok, [RogueX.Petname]."
                            elif Girl == KittyX:
                                    ch_k "Ok, [KittyX.Petname]."
                            elif Girl == EmmaX:
                                    ch_e "Yes, [EmmaX.Petname]."
                            elif Girl == LauraX:                
                                    ch_l "Ok, [LauraX.Petname]."
                    else:
                            #positive response
                            if "okfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, 5) 
                                    $ Girl.Statup("Obed", 60, 3)
                                    $ Girl.Statup("Inbt", 70, 3)
                                    $ Girl.Statup("Lust", 50, 5)
                            $ Girl.FaceChange("surprised",2) 
                            if Girl == RogueX:
                                    ch_r "Great! I mean, that's cool."
                            elif Girl == KittyX:
                                    ch_k "Nice! I'll, um, yeah."
                            elif Girl == EmmaX:
                                    ch_e "Oh, what a relief. . ."
                            elif Girl == LauraX:                
                                    ch_l "Finally."    
                            $ Girl.FaceChange("smile",1) 
                    $ Girl.DrainWord("nofap",0,0,1) #removes "nofap" tag from traits
                    $ Girl.AddWord(1,0,0,0,"okfap")  #adds "okfap" tag to History 
                    
                    #fix add a potential for the girl to run out now. . .
            #end "return permission"
            
            "Nevermind":
                    if not ApprovalCheck(Girl, 500, "I"):
                            #shy response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 80, 10) 
                                    $ Girl.Statup("Inbt", 50, 5)
                            $ Girl.FaceChange("bemused",1) 
                            if Girl == EmmaX:
                                    ch_e "Back to more appropriate topics, I hope?"
                            elif Girl == LauraX:                
                                    ch_l "Glad we're off this one. . ."  
                            else: #Rogue, Kitty
                                    $ Girl.FaceChange("surprised",2) 
                                    call AnyLine(Girl,"Right! What were we even talking about?")
                                    $ Girl.FaceChange("smile",1) 
                    elif ApprovalCheck(Girl, 500, "O"):
                            #submissive response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Obed", 60, 5)
                                    $ Girl.Statup("Inbt", 80, 5)
                                    $ Girl.Statup("Lust", 50, 5)
                            $ Girl.FaceChange("sly",1) 
                            if Girl == EmmaX:
                                    ch_e "Very well. . ."
                            else:#Rogue, Kitty, Laura
                                    call AnyLine(Girl,"Ok.")
                    elif not ApprovalCheck(Girl, 800):
                            #rude response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 80, 5) 
                                    $ Girl.Statup("Obed", 50, 5)
                            $ Girl.FaceChange("angry",2,Eyes="side") 
                            if Girl == RogueX:
                                    ch_r "Damned straight, \"never mind.\""
                            elif Girl == EmmaX:
                                    ch_e "I should hope so . . ."
                            else: #Kitty, Laura
                                    call AnyLine(Girl,"Damned right, \"never mind.\"") 
                            $ Girl.FaceChange("angry",1) 
                    else:
                            #neutral response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Obed", 50, 3)
                                    $ Girl.Statup("Inbt", 50, 2)
                            $ Girl.FaceChange("sly",1) 
                            if Girl == EmmaX:
                                    ch_e "Very well. . ."
                            else:#Rogue, Kitty, Laura
                                    call AnyLine(Girl,"Ok.") 
            #end "nevermind"
            
        $ Girl.AddWord(1,0,"askedfap",0,"askedfap")  #adds "askedfap" tag to Daily and History 
        $ Taboo = TabStore    
        return
       
# End No Fapping / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  



# Start Call to Fap / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
label CalltoFap(Girl=0,Fap=0):
        #called from EventCalls
        #The girl calls you for permission to fap, 1 is "yes," 2 is "i'll watch," 3 is "i'll visit."
        
        if "nofap" not in Girl.Traits:
                #if she's allowed to fap, she will
                $ Girl.DrainWord("wannafap",0,1) #removes "wannafap" tag from daily                
                $ Girl.AddWord(1,0,"gonnafap",0,0)  #adds "gonnafap" tag to daily 
                return           
                
        if Girl.Loc == bg_current:
                #if she's in the room with you, this won't come up.
                return
        
        #first girl to pass the above check. . .
        $ EGirls.remove(EGirls[0]) #remove her from the list
        while EGirls:
                #clears out remaining options, if applicable
                if "wannafap" in EGirls[0].DailyActions and "nofap" not in EGirls[0].DailyActions:
                        #if she's wants to fap and is allowed to, she will                   
                        $ EGirls[0].AddWord(1,0,"gonnafap",0,0)  #adds "gonnafap" tag to daily 
                $ EGirls.remove(EGirls[0])
                #any girls who are under "nofap" orders are out of luck this turn. . .
                    
        $ Player.DailyActions.append("fapcall")
        
#        call Shift_Focus(Girl)                 #fix later
        show Cellphone at SpriteLoc(StageLeft)
                
        "[Girl.Name] calls you up. . ."
        if Girl == RogueX:
                ch_r "So. . . I was wondering. . ."
                ch_r "I know you didn't want me to. . . um. . . "
                ch_r "take care of my needs?"
                ch_r ". . ."
                ch_r ". . .but would you mind if I were to do that?"
                ch_r "Right now?" 
        elif Girl == KittyX:               
                ch_k "Hey, so[KittyX.like]I know you were all like. . ."
                ch_k "\"don't touch yourself, Kitty,\" and[KittyX.like],"
                ch_k "I know I agreed and all, but. . ."
                ch_k "Would you mind if[KittyX.like]maybe I did anyway?"
        elif Girl == EmmaX:
                ch_e "I'm aware that we had something of an arrangement going on. . ."
                ch_e "One relating to me. . . gratifying myself. . ."
                ch_e "or the lack thereof. . ."
                ch_e "And I was just curious, would you mind if we perhaps suspended that rule. . ."
                ch_e "Just for tonight, perhaps?"
        elif Girl == LauraX:                
                ch_l "Hey, remember when you told me I couldn't schlick off?"
                ch_l "I want to schlick off."
                ch_l ". . ."
                ch_l "That cool? or. . ."
                        
        menu:
            "Sure, no problem.":
                            $ Girl.Statup("Love", 90, 5)
                            $ Girl.Statup("Love", 80, 5) 
                            $ Girl.Statup("Love", 200, 1) 
                            $ Girl.Statup("Obed", 80, 2)
                            $ Girl.Statup("Inbt", 80, 3)
                            $ Girl.Statup("Lust", 50, 5)
                            if Girl == RogueX:
                                    ch_r "Thanks, I really appreciate that."
                            elif Girl == KittyX:
                                    ch_k "Cool!"
                            elif Girl == EmmaX:
                                    ch_e "Oh, thank you, [EmmaX.Petname]."
                            elif Girl == LauraX: 
                                    ch_l "Nice."
                            $ Fap = 1
            "If you really have to. . .":
                    if Girl.Love >= 2*Girl.Obed:
                            #if she agrees to not do it (Love+Obed >= double Inbt)
                            $ Girl.Statup("Love", 80, 2) 
                            $ Girl.Statup("Obed", 60, 3)
                            $ Girl.Statup("Obed", 80, 1)
                            $ Girl.Statup("Lust", 80, 5)
                            if Girl == RogueX:
                                    ch_r "Oh, well. . .."
                                    ch_r "I suppose I could restrain myself. . ." 
                            elif Girl == KittyX:
                                    ch_k "Well, if it really bothers you. . ."
                            elif Girl == EmmaX:
                                    ch_e "I imagine I can find other distractions, [EmmaX.Petname]."
                            elif Girl == LauraX: 
                                    ch_l "Hmm. Yeah, whatever. Nevermind."
                            $ Girl.Thirst += 10                               
                            
                    else:
                            #if she insists on doing it
                            $ Girl.Statup("Love", 80, 3) 
                            $ Girl.Statup("Love", 200, 1)
                            $ Girl.Statup("Obed", 50, -4)
                            $ Girl.Statup("Obed", 90, -1)
                            $ Girl.Statup("Inbt", 50, 2)
                            $ Girl.Statup("Inbt", 80, 5)
                            $ Girl.Statup("Lust", 50, 5)
                            if Girl == RogueX:
                                    ch_r "I would REALLY appreciate that."
                                    ch_r "Thank you." 
                            elif Girl == KittyX:
                                    ch_k "I kinda. . . yeah."
                            elif Girl == EmmaX:
                                    ch_e "It would really just take the edge off of a long day."
                            elif Girl == LauraX: 
                                    ch_l "Yeah, I probably do."                                    
                            $ Fap = 1
            "No, you may not.":
                    if ApprovalCheck(Girl,600,"O") and (Girl.Obed >= Girl.Inbt):
                            #if she agrees to not do it (Obed >= Inbt)
                            $ Girl.Statup("Love", 50, -5) 
                            $ Girl.Statup("Obed", 60, 5)
                            $ Girl.Statup("Obed", 200, 2)
                            $ Girl.Statup("Lust", 80, 5)
                            if ApprovalCheck(Girl,800,"O"):
                                    $ Girl.Statup("Lust", 200, 5)                                
                            if Girl == RogueX:
                                    ch_r "Oh, well. . .."
                                    ch_r "I suppose I could restrain myself. . ." 
                            elif Girl == KittyX:
                                    ch_k "Well, if it really bothers you. . ."
                            elif Girl == EmmaX:
                                    ch_e "I imagine I can find other distractions, [EmmaX.Petname]."
                            elif Girl == LauraX: 
                                    ch_l "Hmm. Yeah, whatever. Nevermind."
                            $ Girl.Thirst += 10                               
                    elif ApprovalCheck(Girl,1000,"LO"):
                            #she is apologetic about it
                            $ Girl.Statup("Love", 70, -5) 
                            $ Girl.Statup("Obed", 50, -3)
                            $ Girl.Statup("Obed", 80, -2)
                            $ Girl.Statup("Inbt", 50, 3)
                            $ Girl.Statup("Inbt", 80, 2)
                            $ Girl.Statup("Lust", 80, 5)
                            if Girl == RogueX:
                                    ch_r "Well, I mean, I kind of started. . ."
                            elif Girl == KittyX:
                                    ch_k "Um, sorry, but I[KittyX.like]have to?"
                            elif Girl == EmmaX:
                                    ch_e "I think I'll just have to do it anyway. . ."
                            elif Girl == LauraX: 
                                    ch_l "Um, sure, I will NOT be doing just that. . ."   
                            $ Girl.Thirst += 10                               
                            $ Fap = 1
                    else:
                            #if she is mad at you
                            $ Girl.Statup("Love", 70, -5) 
                            $ Girl.Statup("Love", 90, -5) 
                            $ Girl.Statup("Obed", 80, -5)
                            $ Girl.Statup("Inbt", 50, 4)
                            $ Girl.Statup("Inbt", 80, 3)
                            if Girl == RogueX:
                                    ch_r "You know what? Screw it, and screw you!"
                            elif Girl == KittyX:
                                    ch_k "Well. . . I'm doing it anyway!"
                            elif Girl == EmmaX:
                                    ch_e "I think I can be the judge of that."
                            elif Girl == LauraX: 
                                    ch_l "Sure, keep thinking I care."    
                            $ Girl.Thirst += 10                                         
                            $ Fap = 1               
            "I could come over and take care of that. . .":
                            $ Girl.Statup("Love", 80, 4) 
                            $ Girl.Statup("Love", 200, 1) 
                            $ Girl.Statup("Obed", 80, 2)
                            $ Girl.Statup("Inbt", 80, 2)
                            $ Girl.Statup("Lust", 80, 5)
                            if Girl == EmmaX:
                                    ch_e "I think you could at that, [EmmaX.Petname]."
                            elif Girl == LauraX: 
                                    ch_l "Cool."
                            else: #Rogue, Kitty
                                    call AnyLine(Girl,"Oh, you would, would you. . .")
                            $ Fap = 3
            "Only if I can watch." if AloneCheck(): #only works if you're alone
                    if ApprovalCheck(Girl, 1200):
                            #She agrees
                            $ Girl.Statup("Love", 80, 4) 
                            $ Girl.Statup("Obed", 60, 2)
                            $ Girl.Statup("Obed", 80, 2)
                            $ Girl.Statup("Inbt", 50, 2)
                            $ Girl.Statup("Inbt", 80, 3)
                            $ Girl.Statup("Lust", 80, 5)
                            if Girl == RogueX: #R_Mast
                                    ch_r "Hmm. . . that sounds like fun. . ."
                            elif Girl == KittyX:
                                    ch_k "Heh, you looking for a show? . ."
                            elif Girl == EmmaX:
                                    ch_e "I think we could arrange that. . ."
                            elif Girl == LauraX: 
                                    ch_l "Yeah, I could do that, gimme a sec. . ."
                            $ Fap = 2
                    else:
                            #she's not into it.
                            $ Girl.Statup("Love", 60, -3) 
                            $ Girl.Statup("Obed", 60, -2)
                            $ Girl.Statup("Inbt", 80, 3)
                            $ Girl.Statup("Lust", 50, 5)
                            if Girl == RogueX: #R_Mast
                                    ch_r "I, um, I don't know about that. . ."
                            elif Girl == KittyX:
                                    ch_k "Heh, heh, um, I don't think I could. . ."
                            elif Girl == EmmaX:
                                    ch_e "I'd rather avoid putting on a show like that. . ."
                            elif Girl == LauraX: 
                                    ch_l "Nah, had enough of surveillance . . ."
                            $ Girl.Thirst += 15
                                    
        $ Girl.DrainWord("wannafap",0,1) #removes "wannafap" tag from daily         
        hide Cellphone
        
        if Fap == 3:
                #if you decide to come over. . .
                $ del Options[:]  
#                if Girl == "Rogue":                    
#                        $ renpy.pop_call() #skips past EventCall
#                        $ renpy.pop_call() #skips past this label
#                        $ R_Loc = "bg rogue"
#                        call Taboo_Level
#                        jump Rogue_Room
#                elif Girl == "Kitty":
#                        $ renpy.pop_call() #skips past EventCall
#                        $ renpy.pop_call() #skips past this label
#                        $ K_Loc = "bg kitty"
#                        call Taboo_Level
#                        jump Kitty_Room
#                elif Girl == "Emma":
#                        $ renpy.pop_call() #skips past EventCall
#                        $ renpy.pop_call() #skips past this label
#                        $ E_Loc = "bg emma"
#                        call Taboo_Level
#                        jump Emma_Room
#                elif Girl == "Laura": 
#                        $ renpy.pop_call() #skips past EventCall
#                        $ renpy.pop_call() #skips past this label
#                        $ L_Loc = "bg laura"
#                        call Taboo_Level
#                        jump Laura_Room
                        
                #maybe this will work, maybe not, but. . .
                
                $ Girl.Loc = Girl.Home
                $ bg_current = Girl.Home
                call Taboo_Level(1)
#                $ renpy.pop_call() #skips past EventCall
#                $ renpy.pop_call() #skips past this label
                
                jump Misplaced
                #jump expression Girl.Tag + "_Room"
                
        elif Fap == 2:
                #if you agree to watch her. . .
                $ del Options[:]  
                if Girl == EmmaX and Girl.Loc == "bg classroom" and Time_Count >= 2:
                        pass             #if it's Emma and she's in class and it's a good time, stay
                else:
                        $ Girl.Loc = Girl.Home             
                call Taboo_Level(0)        
                call PhoneSex(Girl)            
                $ renpy.pop_call() #skips past EventCall
        elif Fap:
                #if you agree at some point. . .           
                $ Girl.AddWord(1,0,"gonnafap",0,0)  #adds "gonnafap" tag to daily 
            
        $ Options = ["empty"] #sets token entry to prevent a removal failure. . .
        return

            #add history elements
            #add "if girl is watching, "join us." to basic sex menus          
# End Call to Fap / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    
          

# Start Phone Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
label PhoneSex(Girl=0):
        # called by Eventcalls->CalltoFap
        # make sure to adjust orgasm options to work when you aren't in the room.
        
        $ Player.RecentActions.append("phonesex")
            
        #display the phone sex graphics
        
        call Shift_Focus(Girl)
        show PhoneSex zorder 150
                        
        $ Girl.AddWord(1,"phonesex","phonesex",0,"phonesex")  #adds "phonesex" tag to recent and daily actions, and history 
        $ Trigger = 1
        if Girl == RogueX:
                ch_r "Ok, I think that should get the video running, right?"
                call Rogue_M_Prep
                ch_r "Hmm, that was a satisfying phone call. . ."
                ch_r "I gotta go."                
        elif Girl == KittyX:
                ch_k "Ok, that's got it up."
                ch_k "[KittyX.Like]how do I look?"
                call Kitty_M_Prep
                ch_k "Mmmmm. . . call any time, [KittyX.Petname]."
                ch_k "[KittyX.Like]ANY time."
        elif Girl == EmmaX:
                ch_e "Now, set it up like so. . ."
                ch_e "There, you should have video up."
                call Emma_M_Prep
                ch_e "I do enjoy these little chats. . ."
                ch_e "I need to be going though."
        elif Girl == LauraX: 
                ch_l "Ok, video up. . ."
                call Laura_M_Prep
                ch_l "That was fun. Call you later?"        
        #hide the phone sex graphics
        
        hide PhoneSex
                 
        call Get_Dressed
        $ Girl.OutfitChange(5) #resets her clothes
        call Checkout(1)
        $ Player.RecentActions.remove("phonesex")
        return
#add option for girl to strip herself. . .
# End Phone Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  


    
    