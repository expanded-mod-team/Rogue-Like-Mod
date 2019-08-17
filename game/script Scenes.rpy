label Sleepover(Lead=0,Sleep=0,Room=0,Line = 0):
            #This event gets called from Round10, should never be called without the room's owner
            # If there's a Lead, she's been sent to this from elsewhere
            # Sleep tracks number of previous sleepovers

            $ Party = []
            if R_Loc == bg_current:
                    $ Party.append("Rogue")
            if K_Loc == bg_current:
                    $ Party.append("Kitty")
            if E_Loc == bg_current:
                    $ Party.append("Emma")
            if L_Loc == bg_current:
                    $ Party.append("Laura")
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
            
            if bg_current == "bg rogue":
                    $ Room = "Rogue"
            elif bg_current == "bg kitty":
                    $ Room = "Kitty"          
            elif bg_current == "bg emma":
                    $ Room = "Emma"
            elif bg_current == "bg laura":
                    $ Room = "Laura"
            elif bg_current == "bg player":
                    $ Room = "Player"
            else:
                    #it's somehow not any room?
                    "Tell Oni you're in room [bg_current] somehow."
            
            if Room not in Party and bg_current != "bg player":
                    #either another girl is around or she wouldn't want you sleeping there
                    "[Room] probably wouldn't appreciate you staying over, you head back to your own room."
                    call Remove_Girl("All")
                    $ renpy.pop_call()
                    jump Player_Room
                                
            # the previous statemetn should cull out all situations where the owner isn't there
            if Room == "Player":
                    if len(Party) == 2:                    
                        $ renpy.random.shuffle(Party)
                        if ApprovalCheck(Party[0],Check=1) <= ApprovalCheck(Party[1],Check=1):
                            # If second one likes you more, pick her
                            $ Party.reverse()   
                    if Party[0] == "Rogue":
                        ch_r "It's getting late and I'm getting a bit tired."  
                        $ Sleep = R_Sleep               
                    elif Party[0] == "Kitty": 
                        ch_k "It's late, I'm thinking of heading out. . ." 
                        $ Sleep = K_Sleep
                    elif Party[0] == "Emma":            
                        ch_e "It's late, I should be going. . ."  
                        $ Sleep = E_Sleep
                    elif Party[0] == "Laura":            
                        ch_l "I need some sleep. . ."  
                        $ Sleep = L_Sleep
            elif Room == "Rogue":
                    ch_r "It's getting late and I'm turning in."
                    $ Sleep = R_Sleep     
                    if Party[0] != "Rogue":
                            $ Party.reverse()  
            elif Room == "Kitty":
                    ch_k "I'm getting kinda tired. . ."
                    $ Sleep = K_Sleep     
                    if Party[0] != "Kitty":
                            $ Party.reverse() 
            elif Room == "Emma":
                    ch_e "It's getting late, [E_Petname]. . ."
                    $ Sleep = E_Sleep     
                    if Party[0] != "Emma":
                            $ Party.reverse() 
            elif Room == "Laura":
                    ch_l "I'm tired. . ."
                    $ Sleep = L_Sleep     
                    if Party[0] != "Laura":
                            $ Party.reverse() 
            else:
                "Something went wrong." 
                "Tell Oni \"[Party] - [bg_current] - [Room]\""
                    
            
            if Day <= 7:
                    # If it's too early for sleepovers, 
                    jump Return_Player               
                
            if "Emma" in Party:                      
                    if "classcaught" not in E_History:
                            ch_e "I should probably get going, we wouldn't want any rumors to spread."                      
                            call Remove_Girl("Emma")
                    elif len(Party) >= 2 and "three" not in E_History:
                            #if Emma's around but can't do threesome stuff yet
                            if (Room == "Emma" or Room == "Player") and ApprovalCheck("Emma", 1100, "LI"):
                                if Party[0] != "Emma":
                                        $ Party.reverse() 
                                ch_e "[Party[1]] dear, I need a moment with [Playername], but you can leave." 
                                call AnyFace(Party[1],"confused",1)                           
                                call AnyLine(Party[1],"Oh, ok. . .")                            
                                call Remove_Girl(Party[1])
                                ch_e "Sorry about that, but I had to discuss something with you in private."
                            else:
                                #if it's not her room, or she doesn't like you enough to stay
                                ch_e "Yes, I really should be leaving, don't let me bother you two."                        
                                call Remove_Girl("Emma")
                            if "sleeptime" not in E_History:
                                $ E_History.append("sleeptime")                        
                    if not Party:
                        #if Emma leaves
                        jump Return_Player
                        
            if Room not in Party and bg_current != "bg player":
                    #if the room's owner left you in her room. . .
                    "[Room] probably wouldn't appreciate you staying over, you head back to your own room."
                    call Remove_Girl("All")
                    $ renpy.pop_call()
                    jump Player_Room
                        
            call AnyFace(Party[0],"sexy",1)
            
            if Sleep >= 3 and ApprovalCheck(Party[0], 800):                                 
                    #You've slept over several times and she still likes you
                    if Party[0] == Room:
                            $ Line = "Are you staying over tonight?"
                    else:
                            $ Line = "I'm staying over, right?"
                    call AnyLine(Party[0],Line)
                
            elif Sleep < 3 and ApprovalCheck(Party[0], 1100, "LI"):                        
                    #You haven't slept over much, but she wants you to
                    call AnyFace(Party[0],"bemused",1)
                    if Party[0] == "Rogue":
                            if bg_current == "bg rogue":
                                ch_r "I was thinking. . . maybe you wanted to stay the night?"  
                            else:
                                ch_r "I was thinking. . . maybe I could stay the night?" 
                    elif Party[0] == "Kitty":
                            if bg_current == "bg kitty":
                                ch_k "So[K_like]did you want to stay over?"  
                            else:
                                ch_k "So[K_like]could I stay over?"
                    elif Party[0] == "Emma":
                            if bg_current == "bg emma":
                                ch_e "I was wondering, have you considered staying over?"  
                            else:
                                ch_e "I was wondering, could I stay over?" 
                    elif Party[0] == "Laura":
                            if bg_current == "bg laura":
                                ch_l "So, are you staying over?"  
                            else:
                                ch_l "So, can I stay here tonight?" 
                    $ Line = 1
                    
            else: #If she's uninterested                
                    if Party[0] == "Rogue":
                            if bg_current == "bg rogue":
                                ch_r "You should get going." 
                            else:
                                ch_r "I'm heading out, see you tomorrow."
                    elif Party[0] == "Kitty":
                            if bg_current == "bg kitty":
                                ch_k "You should[K_like]head out." 
                            else:
                                ch_k "See ya tomorrow, [K_Petname]."
                    elif Party[0] == "Emma":
                            if bg_current == "bg emma":
                                ch_e "Could you please clear the room?"
                            else:
                                ch_e "I should leave." 
                    elif Party[0] == "Laura":
                            if bg_current == "bg laura":
                                ch_l "Clear out."
                            else:
                                ch_l "So, later." 
            
            if Line:
                #she offered to sleep over
                menu:
                    extend ""
                    "Sure.":
                            if Sleep <= 5:
                                call Statup(Party[0], "Love", 70, 10)
                                call Statup(Party[0], "Obed", 80, 10)
                                call Statup(Party[0], "Obed", 50, 20)
                                call Statup(Party[0], "Inbt", 25, 20)              
                            call Statup(Party[0], "Love", 70, 5) 
                            call AnyFace(Party[0],"smile")
                            # Line = 1
                        
                    "No, sorry.":                  
                            call Statup(Party[0], "Obed", 50, 2)
                            call Statup(Party[0], "Obed", 30, 5)
                            call Statup(Party[0], "Inbt", 40, 3) 
                            call AnyFace(Party[0],"sad")
                            $ Line = 0
                            if Party[0] == "Rogue":
                                    ch_r "Ok, see you tomorrow then. 'Night."                
                            elif Party[0] == "Kitty":
                                    ch_k "Alright. . . see you tomorrow. . ."
                            elif Party[0] == "Emma":
                                    ch_e "Well, if you insist. See you tomorrow then."
                            elif Party[0] == "Laura":
                                    ch_l "Ok."  
                            
                            
            else:
                #if she didn't offer to sleep over
                menu: 
                    extend ""
                    "Ok, I'll head out. Good night." if Party[0] == Room:    
                            #if she didn't agree and this is her room
                            $ Line = "leave"
                    "Ok, see you later then. Good night." if Party[0] != Room:     
                            #if she didn't agree and this is not her room    
                            $ Line = "leave"   
                        
                    "Are you sure I can't stay the night? . ." if not Sleep and Party[0] == Room: 
                            $ Line = "please"   
                    "Are you sure you can't stay? . ." if not Sleep and Party[0] != Room: 
                            $ Line = "please"   
                                
                    "That's not what you said the other night . ." if Sleep: 
                            #if she wants you gone  
                            if ApprovalCheck(Party[0],900)or ApprovalCheck(Party[0],700,"L") or ApprovalCheck(Party[0],500,"O"):
                                call AnyFace(Party[0],"bemused",1)  
                                $ Line = 1       
                                if Party[0] == "Rogue":
                                        ch_r "Well. . . that didn't turn out so bad, I suppose. . ."              
                                elif Party[0] == "Kitty":      
                                        ch_k "and that went pretty well. . ."
                                elif Party[0] == "Emma":
                                        ch_e "It was a nice evening."
                                elif Party[0] == "Laura":
                                        ch_l "Yeah, it was."   
                            else:                    
                                call AnyFace(Party[0],"smile",Brows="confused")
                                # Line = 0
                                if Party[0] == "Rogue":
                                        ch_r "I'm afraid not this time, [R_Petname]. I'll see you later."               
                                elif Party[0] == "Kitty":
                                        ch_k "Um, no, 'fraid not. I'll see ya tomorrow." 
                                elif Party[0] == "Emma":
                                        ch_e "Well, not tonight, [E_Petname]."
                                elif Party[0] == "Laura":
                                        ch_l "Yeah, but not this time."  
                                if Party[0] == Room:
                                        #if it's a girl's room, you leave.
                                        ch_p "Ok, I'll be going then."   
                #if she didn't offer to sleep over
        
            if Line == "leave":           
                # if you agreed to leave
                call Statup(Party[0], "Love", 90, 3)
                call Statup(Party[0], "Inbt", 25, 2)    
                call AnyFace(Party[0],"smile") 
                $ Line = 0 
                if Party[0] == "Rogue":
                        ch_r "Yeah, good night, [R_Petname]. . ."                
                elif Party[0] == "Kitty":
                        ch_k "Yeah, 'night, [K_Petname]. . ."
                elif Party[0] == "Emma":
                        ch_e "Yes, good night, [E_Petname]."
                elif Party[0] == "Laura":
                        ch_l "Ok, good night then."
                        
            if Line == "please": 
                #if she said no but you asked nicely
                if ApprovalCheck(Party[0],1000) or ApprovalCheck(Party[0],700,"L") or ApprovalCheck(Party[0],500,"O"):
                    call AnyFace(Party[0],"bemused") 
                    $ Line = 1 
                    if Party[0] == "Rogue":
                            ch_r "Well. . . I suppose it would be alright."                
                    elif Party[0] == "Kitty":
                            ch_k "Well, Maaaybeee. . ."
                    elif Party[0] == "Emma":
                            ch_e "I suppose we could make an exception. . ."
                    elif Party[0] == "Laura":
                            ch_l "Suit yourself."                    
                else:                    
                    call AnyFace(Party[0],"smile",Brows="confused")
                    $ Line = 0
                    if Party[0] == "Rogue":
                            ch_r "I'm afraid not, [R_Petname]. Head home, I'll see you later."               
                    elif Party[0] == "Kitty":
                            ch_k "Ehhhh. . . no, not tonight, [K_Petname]. Sorry." 
                    elif Party[0] == "Emma":
                            ch_e "I'm afraid not."
                    elif Party[0] == "Laura":
                            ch_l "Don't push it."

            if not Line:
                #if the primary girl refused to sleep over
                if Room == Party[0]:
                        #if it's her room, removes any other girls around
                        call CleartheRoom(Party[0],1)    
                        jump Return_Player                        
                else:   
                        #if it's not her room, remove her, and try again
                        call Remove_Girl(Party[0])
                        call Sleepover
                        #there is a bug where sleepovers take an extra wait block, I believe it camefrom not having a return here,let'stest the theory. 
                        return
                      
            #If the primary girl agreed  
            if len(Party) >= 2:
                #if there is another girl
                if GirlLikeCheck(Party[0],Party[1]) >= 700 and ApprovalCheck(Party[0], 1200):
                        # If she likes the other girl quite a bit and likes you a decent amount
                        if Party[0] == "Rogue":
                                ch_r "And you, [Party[1]]?"                   
                        elif Party[0] == "Kitty":
                                ch_k "How about you, [Party[1]]?"
                        elif Party[0] == "Emma":
                                ch_e "And what about you, [Party[1]]?"
                        elif Party[0] == "Laura":
                                ch_l "And you, [Party[1]]?"
                else:
                        if Party[0] == "Rogue":
                                ch_r "Are you leaving, [Party[1]]?"                   
                        elif Party[0] == "Kitty":
                                ch_k "You heading out, [Party[1]]?"
                        elif Party[0] == "Emma":
                                ch_e "I assume you're leaving, [Party[1]]?"
                        elif Party[0] == "Laura":
                                ch_l "Later, [Party[1]]."
                                
                if GirlLikeCheck(Party[1],Party[0]) >= 500 and ApprovalCheck(Party[1], 1200):
                        # If second girl likes the other girl a bit and likes you a decent amount  
                        call AnyFace(Party[1],"smile") 
                        if Party[1] == "Rogue":
                                ch_r "I'd like to stay too."                   
                        elif Party[1] == "Kitty":
                                ch_k "Can I stay too?"
                        elif Party[1] == "Emma":
                                ch_e "I'd rather join the fun."
                        elif Party[1] == "Laura":
                                ch_l "Me too, right?"
                        $ Line = 1
                else:  
                        call AnyFace(Party[0],"smile",1) 
                        if Party[1] == "Rogue":
                                ch_r "I guess I should be going."                   
                        elif Party[1] == "Kitty":
                                ch_k "I should go, right?"
                        elif Party[1] == "Emma":
                                ch_e "I suppose three is a crowd."
                        elif Party[1] == "Laura":
                                ch_l "I should leave."
                        $ Line = 0
                menu:
                    extend ""
                    "You should stay, [Party[1]].":
                            #this checks the second girl's response.
                            if GirlLikeCheck(Party[1],Party[0]) >= 500 and ApprovalCheck(Party[1], 1200):
                                    # If second girl likes the first girl a bit and likes you a decent amount
                                    if Party[1] == "Rogue":
                                            ch_r "Oh, I'd love to."                   
                                    elif Party[1] == "Kitty":
                                            ch_k "Roomies!"
                                    elif Party[1] == "Emma":
                                            ch_e "I'd love to."
                                    elif Party[1] == "Laura":
                                            ch_l "Great."
                                    $ Line = 1
                            else:  
                                    call AnyFace(Party[1],"sadside",1,Mouth="smile") 
                                    if Party[1] == "Rogue":
                                            ch_r "I don't want to be a bother."                   
                                    elif Party[1] == "Kitty":
                                            ch_k "No way."
                                    elif Party[1] == "Emma":
                                            ch_e "I couldn't."
                                    elif Party[1] == "Laura":
                                            ch_l "Nah."
                                    $ Line = 0
                            
                            #This checks the first girl's response
                            if Line:
                                if GirlLikeCheck(Party[0],Party[1]) >= 700 and ApprovalCheck(Party[0], 1200):
                                    # If first girl likes the other girl quite a bit and likes you a decent amount
                                    if Party[0] == "Rogue":
                                            ch_r "Great!"                   
                                    elif Party[0] == "Kitty":
                                            ch_k "Roomies!"
                                    elif Party[0] == "Emma":
                                            ch_e "Lovely."
                                    elif Party[0] == "Laura":
                                            ch_l "Ok."  
                                elif GirlLikeCheck(Party[0],Party[1]) >= 400 and ApprovalCheck(Party[0], 1400):
                                    # If she barely likes the other girl but likes you a a lot
                                    call AnyFace(Party[0],"sadside",1,Mouth="smile") 
                                    if Party[0] == "Rogue":
                                            ch_r "Sure, I guess."                   
                                    elif Party[0] == "Kitty":
                                            ch_k "Um, Ok."
                                    elif Party[0] == "Emma":
                                            ch_e "I suppose we could find room for one more."
                                    elif Party[0] == "Laura":
                                            ch_l "Whatever."
                                else:
                                    call AnyFace(Party[0],"angry",1) 
                                    if Party[0] == "Rogue":
                                            ch_r "I'm not cool with that."                   
                                    elif Party[0] == "Kitty":
                                            ch_k "No way."
                                    elif Party[0] == "Emma":
                                            ch_e "I don't think so."
                                    elif Party[0] == "Laura":
                                            ch_l "Um, no."
                                    $ Line = 0
                    
                    "You should get going, [Party[1]].":
                            if Party[1] == "Rogue":
                                    ch_r "Oh, ok."                   
                            elif Party[1] == "Kitty":
                                    ch_k "Yeah."
                            elif Party[1] == "Emma":
                                    ch_e "I assumed."
                            elif Party[1] == "Laura":
                                    ch_l "Yeah."
                            $ Line = 0
                            
            if Line == 0:
                #if the second girl got the boot:
                if len(Party) >= 2:
                    if Party[0] == "Rogue":
                            ch_r "Later, [Party[1]]."                   
                    elif Party[0] == "Kitty":
                            ch_k "Night, [Party[1]]." 
                    elif Party[0] == "Emma":
                            ch_e "Goodnight, [Party[1]]." 
                    elif Party[0] == "Laura":
                            ch_l "Night." 
                        
                    if Party[1] == "Rogue":
                            ch_r "Later guys."                   
                    elif Party[1] == "Kitty":
                            ch_k "Night." 
                    elif Party[1] == "Emma":
                            ch_e "Goodnight." 
                    elif Party[1] == "Laura":
                            ch_l "Night." 
                if Party:        
                    call CleartheRoom(Party[0],1,1) #removes any other girls around   
            
            
            if Room not in Party and bg_current != "bg player":
                    #if the room's owner left you in her room. . .
                    "[Room] probably wouldn't appreciate you staying over, you head back to your own room."
                    call Remove_Girl("All")
                    $ renpy.pop_call()
                    jump Player_Room
            elif Party:
                    jump Sleepover_Morning
            else:
                    #if nobody is around.
                    $ bg_current = "bg player"
                    call CleartheRoom("All",1)
                    #if nobody is here, you just go to sleep
                    "It's getting late, so you go to sleep."
                    call Wait
                    return    
                    
            jump Return_Player

  
label Return_Player:    
        # This label is jumped to by the Sleep labels if the player or girl leaves after a sleepover (fail state).
        $ del Party[:]
        if bg_current != "bg rogue" and R_Loc == bg_current:
                "Rogue heads out."        
                $ R_Loc = "bg rogue"
        if bg_current != "bg kitty" and K_Loc == bg_current:
                "Kitty heads out."        
                $ K_Loc = "bg kitty"
        if bg_current != "bg emma" and E_Loc == bg_current:
                "Emma heads out."        
                $ E_Loc = "bg emma"
        if bg_current != "bg laura" and L_Loc == bg_current:
                "Laura heads out."        
                $ L_Loc = "bg laura"
        if bg_current != "bg player":
                "You head back to your room."
        $ bg_current = "bg player"
        call Set_The_Scene
        $ renpy.pop_call()
        jump Player_Room
          
label Sleepover_Morning:
        #This label is jumped too from Sleepover if you successfully stay the night
        if R_Loc == bg_current and "Rogue" not in Party:
               call Remove_Girl("Rogue")
        if K_Loc == bg_current and "Kitty" not in Party:
               call Remove_Girl("Kitty")
        if E_Loc == bg_current and "Emma" not in Party:
               call Remove_Girl("Emma")
        if L_Loc == bg_current and "Laura" not in Party:
               call Remove_Girl("Laura")
        call Shift_Focus(Party[0])            
        call AnyOutfit(Party[0],"sleep")
        if len(Party) >= 2:
                #If there are two girls. . .       
                call AnyOutfit(Party[1],"sleep")
                "The girls change into their sleepwear."
        else:        
                "[Party[0]] changes into her sleepwear."
        
        if Party[0] == "Rogue":
                ch_r "Hmm, that's a bit more comfortable."  
                $ Sleep = R_Sleep    
                $ R_Traits.append("sleepover")
        elif Party[0] == "Kitty":
                ch_k "Ah, that's better."
                $ Sleep = K_Sleep
                $ K_Traits.append("sleepover")
        elif Party[0] == "Emma":
                ch_e "Mmmm, that's better." 
                $ Sleep = E_Sleep
                $ E_Traits.append("sleepover")
        elif Party[0] == "Laura":
                ch_l ". . ."
                $ Sleep = L_Sleep
                $ L_Traits.append("sleepover")
                
        if len(Party) >= 2:
                if Party[1] == "Rogue":
                        ch_r "Let's turn in."    
                        $ R_Traits.append("sleepover")               
                elif Party[1] == "Kitty":
                        ch_k "Night, [K_Petname]"
                        $ K_Traits.append("sleepover")    
                elif Party[1] == "Emma":
                        ch_e "Lights out." 
                        $ E_Traits.append("sleepover")    
                elif Party[1] == "Laura":
                        ch_l "Night."
                        $ L_Traits.append("sleepover")    
        else:
                if Party[0] == "Rogue":
                        ch_r "Let's turn in."                    
                elif Party[0] == "Kitty":
                        ch_k "Night, [K_Petname]"
                elif Party[0] == "Emma":
                        ch_e "Goodnight." 
                elif Party[0] == "Laura":
                        ch_l "Night."
            
        show blackscreen onlayer black    
        pause 1
        call Wait(0,0) #shouldn't change outfit or lighting 
        $ Party = []
        if "sleepover" in R_Traits: 
                $ R_Loc = bg_current
                $ Party.append("Rogue")
        elif R_Loc == bg_current:
               call Remove_Girl("Rogue")
        if "sleepover" in K_Traits:
                $ K_Loc = bg_current
                $ Party.append("Kitty")
        elif K_Loc == bg_current:
               call Remove_Girl("Kitty")
        if "sleepover" in E_Traits:
                $ E_Loc = bg_current
                $ Party.append("Emma")
        elif E_Loc == bg_current:
               call Remove_Girl("Emma")
        if "sleepover" in L_Traits:
                $ L_Loc = bg_current
                $ Party.append("Laura") 
        elif L_Loc == bg_current:
               call Remove_Girl("Laura")
               
        call AnyOutfit(Party[0],"sleep",Perm=1)
        if len(Party) >= 2:
                call AnyOutfit(Party[1],"sleep",Perm=1)
        
        call Morningwood_Check
                                
        call AnyFace(Party[0],"smile")
        if len(Party) >= 2:
                call AnyFace(Party[1],"smile")
        hide NightMask onlayer nightmask  
        hide blackscreen onlayer black
        
        if "morningwood" in P_DailyActions:
            if Party[0] == "Rogue":
                    ch_r "So, that aside, Sleep well?"             
            elif Party[0] == "Kitty":
                    ch_k "So anyway. . . G'morning . . ."
            elif Party[0] == "Emma":
                    ch_e "Now that we've got that out of our system. . ."
                    ch_e "Morning, [E_Petname]."
            elif Party[0] == "Laura":
                    ch_l "Anyway, 'Morning."
        else:
            if Party[0] == "Rogue":
                    ch_r "'Morning [R_Petname]. Sleep well?"             
            elif Party[0] == "Kitty":
                    ch_k "G'morning . . ."
            elif Party[0] == "Emma":
                    ch_e "Hrmph. . ."
                    ch_e "Oh. You're here."
            elif Party[0] == "Laura":
                    ch_l "'Morning."     
                
        menu:
            extend ""
            "It's always nice sleeping with you." if Sleep: 
                    if Sleep < 5:
                        call Statup(Party[0], "Love", 90, 8)
                        call Statup(Party[0], "Obed", 50, 10)
                        call Statup(Party[0], "Inbt", 70, 8)   
                    call AnyFace(Party[0],B=1)
                    
                    if Party[0] == "Rogue":
                            ch_r "Aw, that's right sweet of ya, [R_Petname]."
                            ch_r "We'll have to keep this regular."          
                    elif Party[0] == "Kitty":
                            ch_k "And that's always nice to hear."
                            ch_k "We'll have to keep this up."
                    elif Party[0] == "Emma":
                            ch_e "Well. . ."
                            ch_e "We'll have to make a habit of it then."
                    elif Party[0] == "Laura":
                            ch_l "Yeah. . ."
                            ch_l "Warm. . ."
                
            "I loved sleeping next to you." if not Sleep:
                    call Statup(Party[0], "Love", 90, 15)
                    call Statup(Party[0], "Love", 70, 10)
                    call Statup(Party[0], "Obed", 50, 12)
                    call Statup(Party[0], "Inbt", 70, 12)
                    $ Line = "nice"
                    
            "It was fun.":
                    if not Sleep:                    
                        call Statup(Party[0], "Love", 90, 10)
                        call Statup(Party[0], "Love", 70, 8)
                        call Statup(Party[0], "Obed", 50, 15)
                        call Statup(Party[0], "Inbt", 70, 15)
                    elif Sleep < 5:
                        call Statup(Party[0], "Love", 70, 8)
                        call Statup(Party[0], "Obed", 80, 10)
                        call Statup(Party[0], "Inbt", 35, 8)    
                    call Statup(Party[0], "Obed", 50, 8)       
                    if ApprovalCheck(Party[0], 800, "L"):
                        call AnyFace(Party[0],"bemused")
                    else:
                        call AnyFace(Party[0],"confused")
                        
                    if Party[0] == "Rogue":
                            ch_r "Ok, well glad I wasn't {i}too{/i} much bother."       
                    elif Party[0] == "Kitty":
                            ch_k "Yeah, I mean I guess it was. . ."
                    elif Party[0] == "Emma":
                            ch_e "\"Fun\" is certainly how I would describe it."
                    elif Party[0] == "Laura":
                            ch_l "Yeah, I guess?"
                            
            "You were constantly tossing around.":    
                    call AnyFace(Party[0],B=1)
                    if ApprovalCheck(Party[0], 800, "L") or ApprovalCheck(Party[0], 1200):
                        call AnyFace(Party[0],"bemused")     
                        call AnyLine(Party[0],"Hmm?")
                    else:
                        call AnyFace(Party[0],"angry")     
                        call AnyLine(Party[0],"!!!")
                    if Sleep < 5:                       
                        if Party[0] == "Rogue":
                                ch_r "It's not like I've had much experience sleeping next to someone. . ."      
                        elif Party[0] == "Kitty":
                                ch_k "I don't make a habit out of it. . ."    
                        elif Party[0] == "Emma":
                                ch_e "I haven't had a lot of practice lately."
                        elif Party[0] == "Laura":
                                ch_l "Deal with it."                                
                        call Statup(Party[0], "Love", 60, -8)
                        call Statup(Party[0], "Obed", 50, 22)
                        call Statup(Party[0], "Inbt", 50, 22)                   
                    else:
                        if Party[0] == "Rogue":
                                ch_r "Well you should probably be used to that by now."     
                        elif Party[0] == "Kitty":
                                ch_k "Yeah, well. . . you should be used to that!"
                        elif Party[0] == "Emma":
                                ch_e "I don't plan on changing any time soon."
                        elif Party[0] == "Laura":
                                ch_l "Yeah, it'll be like that."
                    $Line = "toss"
                                
            "You need to learn to stick to your side.":  
                    if Sleep < 5:
                        call Statup(Party[0], "Love", 80, -8)
                        call Statup(Party[0], "Obed", 50, 40)
                    if ApprovalCheck(Party[0], 500, "O"):
                        call Statup(Party[0], "Love", 80, -2)
                        call Statup(Party[0], "Obed", 90, 5)
                        call AnyFace(Party[0],"normal")
                        if Party[0] == "Rogue":
                                ch_r "Yes, [R_Petname], I'll try my best."
                        elif Party[0] == "Kitty":
                                ch_k "Fine, whatever."
                        elif Party[0] == "Emma":
                                ch_e "I do try."
                        elif Party[0] == "Laura":
                                ch_l "Ok."
                        if Sleep < 5:
                                call Statup(Party[0], "Obed", 80, 8)
                    else:
                        call AnyFace(Party[0],"angry")
                        call Statup(Party[0], "Obed", 90, 5)
                        if Party[0] == "Rogue":
                                ch_r "Hmmph, you'll be sleeping alone, keep talk'in like that."   
                        elif Party[0] == "Kitty":
                                ch_k "That's not how you get me to come back." 
                        elif Party[0] == "Emma":
                                ch_e "I'll sleep how I please."
                        elif Party[0] == "Laura":
                                ch_l "Good luck with that."
                        if Sleep < 5:
                                call Statup(Party[0], "Inbt", 35, 20) 
                    $Line = "toss"
                                                                
        if not Sleep and Line == "nice":  
                if Party[0] == "Rogue":
                        $ R_Blush = 1
                        ch_r "Aw, that's right sweet of ya, [R_Petname]."
                        ch_r "Makes me want to do it again sometime."       
                elif Party[0] == "Kitty":
                        $ K_Blush = 2
                        ch_k "Yeah, I. . [K_like]I had fun too."
                        $ K_Blush = 1
                        ch_k "I wouldn't[K_like]mind doing it again."   
                        $ K_Blush = 2
                        ch_k "You know, some other time. . . "
                        $ K_Blush = 1
                elif Party[0] == "Emma":
                        call EmmaFace("smile",1)
                        ch_e "You're a hopeless romantic, [E_Petname]."
                        call EmmaFace("smile",2,Eyes="side")
                        ch_e "I suppose I can be a bit hopeless too. . ."
                elif Party[0] == "Laura":
                        call LauraFace("confused",1)
                        ch_l "Oh. . ."
                        call LauraFace("surprised",2,Brows="confused")
                        ch_l "Yeah, so did I, now that you mention it. . ."
                        call LauraFace("confused",1)
                        ch_l "Huh."
                            
        call AnyFace(Party[0],B=0)
            
        if len(Party) >= 2:        
            #second girl's lines
            if "morningwood" in P_DailyActions:
                if Party[1] == "Rogue":
                        ch_r "And what about me?"   
                        $ Sleep = R_Sleep                     
                elif Party[1] == "Kitty":
                        ch_k "Me too?"
                        $ Sleep = K_Sleep           
                elif Party[1] == "Emma":
                        ch_e "And me?"
                        $ Sleep = E_Sleep           
                elif Party[1] == "Laura":
                        ch_l "Ung, 'morning."
                        $ Sleep = L_Sleep           
            else:            
                "[Party[1]] rolls over in bed."
                if Party[1] == "Rogue":                        
                        ch_r "Mmm, yeah, 'Morning [R_Petname]."  
                        $ Sleep = R_Sleep           
                elif Party[1] == "Kitty":
                        ch_k "Yeah, G'morning . . ."
                        $ Sleep = K_Sleep
                elif Party[1] == "Emma":
                        ch_e "Hrmph. . ."
                        ch_e "Oh. Not so loud, you two."
                        $ Sleep = E_Sleep
                elif Party[1] == "Laura":
                        ch_l "Yeah, 'Morning."
                        $ Sleep = L_Sleep
                    
            menu:
                extend ""
                "I always love sleeping with you too, [Party[1]]." if Sleep: 
                        if Sleep < 5:
                            call Statup(Party[1], "Love", 90, 8)
                            call Statup(Party[1], "Obed", 50, 10)
                            call Statup(Party[1], "Inbt", 70, 8)   
                        call AnyFace(Party[1],B=1)
                        
                        if Party[1] == "Rogue":
                                ch_r "That's sweet of ya to say, [R_Petname]."
                        elif Party[1] == "Kitty":
                                ch_k "So cute!"
                        elif Party[1] == "Emma":
                                ch_e "Mmmm. . . yes, lovely."
                        elif Party[1] == "Laura":
                                ch_l "Sure. . ."
                    
                "And it was great sleeping with you as well, [Party[1]]." if not Sleep:
                        call Statup(Party[1], "Love", 90, 15)
                        call Statup(Party[1], "Love", 70, 10)
                        call Statup(Party[1], "Obed", 50, 12)
                        call Statup(Party[1], "Inbt", 70, 12)
                        $ Line = "nice"
                        
                "I had fun sleeping with you too, [Party[1]].":
                        if not Sleep:                    
                            call Statup(Party[1], "Love", 90, 10)
                            call Statup(Party[1], "Love", 70, 8)
                            call Statup(Party[1], "Obed", 50, 15)
                            call Statup(Party[1], "Inbt", 70, 15)
                        elif Sleep < 5:
                            call Statup(Party[1], "Love", 70, 8)
                            call Statup(Party[1], "Obed", 80, 10)
                            call Statup(Party[1], "Inbt", 35, 8)    
                        call Statup(Party[1], "Obed", 50, 8)       
                        if ApprovalCheck(Party[1], 800, "L"):
                            call AnyFace(Party[1],"bemused")
                        else:
                            call AnyFace(Party[1],"confused")
                            
                        if Party[1] == "Rogue":
                                ch_r "Yeah, uh, fun."       
                        elif Party[1] == "Kitty":
                                ch_k "Yeah, I mean I guess it was. . ."
                        elif Party[1] == "Emma":
                                ch_e "\"Fun\" is certainly how I would describe it."
                        elif Party[1] == "Laura":
                                ch_l "Yeah, I guess?"
                        $Line = "fun"
                                
                "You were constantly tossing around, [Party[1]]." if Line == "toss":   
                        $ Line = "toss"                                 
                "You were tossing around constantly too, [Party[1]]." if Line != "toss":   
                        $ Line = "toss" 
                                    
                "You need to learn to stick to your side, [Party[1]]." if Line == "toss":  
                        $ Line = "turn"        
                "And you need to learn to stick to your side too, [Party[1]]." if Line != "toss":  
                        $ Line = "turn"
                                                                    
            if not Sleep and Line == "nice":  
                    if Party[1] == "Rogue":
                            $ R_Blush = 1
                            ch_r "Aw, that's right sweet of ya, [R_Petname]."
                            ch_r "I think I'd want to do that again."    
                            ch_r "And, uh, you too, [Party[0]]."
                    elif Party[1] == "Kitty":
                            $ K_Blush = 2
                            ch_k "Yeah, I. . [K_like]I had fun too."
                            $ K_Blush = 1
                            ch_k "I wouldn't[K_like]mind doing it again."   
                            $ K_Blush = 2
                            ch_k "You know, some other time. . . "
                            $ K_Blush = 1  
                            ch_k "And[K_like]you too, [Party[0]]."
                    elif Party[1] == "Emma":
                            call EmmaFace("smile",1)
                            ch_e "You're a hopeless romantic, [E_Petname]."
                            call EmmaFace("smile",2,Eyes="side")
                            ch_e "I suppose I can be a bit hopeless too. . ."  
                            ch_e "You know what I'm talking about, [Party[0]]."
                    elif Party[1] == "Laura":
                            call LauraFace("confused",1)
                            ch_l "Oh. . ."
                            call LauraFace("surprised",2,Brows="confused")
                            ch_l "Yeah, so did I, now that you mention it. . ."
                            call LauraFace("confused",1)
                            ch_l "Huh."  
                            ch_l "Weird, right, [Party[0]]?"
                                
            
            elif Line == "toss":   
                        call AnyFace(Party[1],B=1)
                        if ApprovalCheck(Party[1], 800, "L") or ApprovalCheck(Party[1], 1200):
                            call AnyFace(Party[1],"bemused")     
                            call AnyLine(Party[1],"Hmm?")
                        else:
                            call AnyFace(Party[1],"angry")     
                            call AnyLine(Party[1],"!!!")
                        if Sleep < 5:                       
                            if Party[1] == "Rogue":
                                    ch_r "It's not like I've had much experience sleeping next to someone. . ."      
                            elif Party[1] == "Kitty":
                                    ch_k "I don't make a habit out of it. . ."    
                            elif Party[1] == "Emma":
                                    ch_e "I haven't had a lot of practice lately."
                            elif Party[1] == "Laura":
                                    ch_l "Deal with it."                                
                            call Statup(Party[1], "Love", 60, -8)
                            call Statup(Party[1], "Obed", 50, 22)
                            call Statup(Party[1], "Inbt", 50, 22)                   
                        else:
                            if Party[1] == "Rogue":
                                    ch_r "Well you should probably be used to that by now."     
                            elif Party[1] == "Kitty":
                                    ch_k "Yeah, well. . . you should be used to that!"
                            elif Party[1] == "Emma":
                                    ch_e "I don't plan on changing any time soon."
                            elif Party[1] == "Laura":
                                    ch_l "Yeah, it'll be like that."
            
            elif Line == "turn":  
                        if Sleep < 5:
                            call Statup(Party[1], "Love", 80, -8)
                            call Statup(Party[1], "Obed", 50, 40)
                        if ApprovalCheck(Party[1], 500, "O"):
                            call Statup(Party[1], "Love", 80, -2)
                            call Statup(Party[1], "Obed", 90, 5)
                            call AnyFace(Party[1],"normal")
                            if Party[1] == "Rogue":
                                    ch_r "Yes, [R_Petname], I'll try my best."
                            elif Party[1] == "Kitty":
                                    ch_k "Fine, whatever."
                            elif Party[1] == "Emma":
                                    ch_e "I do try."
                            elif Party[1] == "Laura":
                                    ch_l "Ok."
                            if Sleep < 5:
                                    call Statup(Party[1], "Obed", 80, 8)
                        else:
                            call AnyFace(Party[1],"angry")
                            call Statup(Party[1], "Obed", 90, 5)
                            if Party[1] == "Rogue":
                                    ch_r "Hmmph, you'll be sleeping alone, keep talk'in like that."   
                            elif Party[1] == "Kitty":
                                    ch_k "That's not how you get me to come back." 
                            elif Party[1] == "Emma":
                                    ch_e "I'll sleep how I please."
                            elif Party[1] == "Laura":
                                    ch_l "Good luck with that."
                            if Sleep < 5:
                                    call Statup(Party[1], "Inbt", 35, 20) 
            
            call AnyFace(Party[1],B=0)            
        #end second girl's lines
        
        #fix add sex option here
        
        
        if "Rogue" in Party:
                $ R_Sleep += 1 
                $ R_Traits.remove("sleepover")
                call Rogue_Schedule(2)          
        if "Kitty" in Party:
                $ K_Sleep += 1   
                $ K_Traits.remove("sleepover")
                call Kitty_Schedule(2)
        if "Emma" in Party:
                $ E_Sleep += 1  
                $ E_Traits.remove("sleepover")
                call Emma_Schedule(2) 
        if "Laura" in Party:
                $ L_Sleep += 1   
                $ L_Traits.remove("sleepover")
                call Laura_Schedule(2)
                 
        call AnyFace(Party[0],"normal")
        call AnyOutfit(Party[0],6,Changed = 1)
        if len(Party) >= 2:
                call AnyFace(Party[1],"normal")
                call AnyOutfit(Party[1],6,Changed = 1)
                "The girls get changed for the day."
        else:                
                "[Party[0]] gets changed for the day."
        
        if "Rogue" in Party:
                $ Party.remove("Rogue")
                call Rogue_Schedule           
        if "Kitty" in Party:
                $ Party.remove("Kitty")
                call Kitty_Schedule
        if "Emma" in Party:
                $ Party.remove("Emma")
                call Emma_Schedule 
        if "Laura" in Party:
                $ Party.remove("Laura")
                call Laura_Schedule
                
        return
    
# end Event Sleepover /////////////////////////////////////////////////////
# start Event Morning Wood /////////////////////////////////////////////////////

label Sleepover_MorningWood:
        # this label is called from the Kitty_SexAct("morningwood"), 
        # which was called from Kitty_Sleepover, which was called from a Location.
        
#        if len(Party) >= 2 and ApprovalCheck(Party[1], 1200):        
#            #second girl's lines
#            if Party[1] == "Rogue":                        
#                    if R_Blow 
#                    ch_r "Mmm, yeah, 'Morning [R_Petname]."  
#            elif Party[1] == "Kitty":
#                    ch_k "Yeah, G'morning . . ."
#            elif Party[1] == "Emma":
#                    ch_e "Hrmph. . ."
#                    ch_e "Oh. Not so loud, you two."
#            elif Party[1] == "Laura":
#                    ch_l "Yeah, 'Morning."
                    
        call Shift_Focus(Party[0])
        $ P_Focus = 30
        ch_u "\"Slurp, slurp, slurp.\""
        call Statup(0, "Focus", 80, 5)
        call Statup(Party[0], "Lust", 80, 5)        
        $ P_DailyActions.append("morningwood") 
        
        $ Partner = Party[1] if len(Party) >= 2 else 0  
        #display other girl here if necessary
        
        if Partner:
            if Partner == "Rogue":  
                    show Rogue:
                        pos (900,250)
                    $ R_RecentActions.append("threesome")
            elif Partner == "Kitty":     
                    show Kitty_Sprite:
                        pos (900,250)
                    $ K_RecentActions.append("threesome")
            elif Partner == "Emma":      
                    show Emma_Sprite:
                        pos (900,250)
                    $ E_RecentActions.append("threesome")
            elif Partner == "Laura":     
                    show Laura_Sprite:
                        pos (900,250)  
                    $ L_RecentActions.append("threesome") 
                
        if Party[0] == "Rogue":       
                $ R_RecentActions.append("blanket") 
                call Rogue_BJ_Launch
                $ X_Psychic = R_Pet
        elif Party[0] == "Kitty":
                $ K_RecentActions.append("blanket")           
                call Kitty_BJ_Launch
                $ X_Psychic = K_Pet
        elif Party[0] == "Emma":
                $ E_RecentActions.append("blanket")           
                call Emma_BJ_Launch
                $ X_Psychic = E_Pet
        elif Party[0] == "Laura":
                $ L_RecentActions.append("blanket")           
                call Laura_BJ_Launch   
                $ X_Psychic = L_Pet                                 
        
        $ P_RecentActions.append("cockout")
        call AnyFace(Party[0],"closed",1) 
        call AnyFace(Partner,"closed",1,Mouth="tongue") 
        
        "You feel a pleasant sensation. . ."
        if Trigger4 == "blow":
            ch_u "\"Slurp, slurp, slurp.\" \n \ \"Slurp, slurp, slurp.\""
        else:
            ch_u "\"Slurp, slurp, slurp.\""
        call Statup(0, "Focus", 80, 5)
        call Statup(Party[0], "Lust", 80, 5)
        
        "It's somewhere below your waist. . ."   
        if Trigger4 == "blow":
            ch_u "\"Slurp, slurp, slurp.\" \n \ \"Slurp, slurp, slurp.\""
        else:
            ch_u "\"Slurp, slurp, slurp.\""
        call Statup(0, "Focus", 80, 10)
        call Statup(Party[0], "Lust", 80, 5)
        
        $ Trigger = "blow"
        "You open your eyes. . ."
        
        hide NightMask onlayer nightmask  
        hide blackscreen onlayer black
        
        $ Speed = 3
        $ Count = 3
        $ Line = 0
        $ P_RecentActions.append("cockout")
        call Seen_First_Peen(Party[0],Partner,1,1,1)
                         
        while Count > 0:
                #Looping portion
                call Statup(0, "Focus", 80, 10)
                call Statup(Party[0], "Lust", 80, 5)
                menu:
                    extend ""
                    "Stay Quiet":
                        if Count >2:  
                            if Trigger4 == "blow":
                                "You just let them do their thing and pretend to still be asleep."
                            else:
                                "You just let her do her thing and pretend to still be asleep."
                        elif Count:
                            "It does feel nice. . ."
                        elif not Count:  
                            if Trigger4 == "blow":
                                "You wouldn't want to disturb them. . ."  
                            else:                            
                                "You wouldn't want to disturb her. . ." 
                        $ Line = "\"Slurp, slurp, slurp.\""
                        call AnyLine(Party[0],Line)    
                        if Trigger4 == "blow":
                            call AnyLine(Party[1],Line) 
                    "Um. . . [X_Psychic], what're you doing?":
                        $ Line = "question"
                        $ Count = 1
                    "That feels great, keep going. . .":
                        $ Line = "praise"
                        $ Count = 1
                    "Hey, quit that!":
                        $ Line = "no"
                        $ Count = 1
                $ Count -= 1
        $ X_Psychic = 0
        $ Speed = 1
        call AnyFace(Party[0],B=1)  
        if Trigger4 == "blow":
            "[Party[0]] pulls back with a pop and [Party[1]] sits back."
            $ Trigger4 = 0
        else:
            "[Party[0]] pulls back with a pop."
        if Line == "question":                    
                        call AnyFace(Party[0],"smile",B=1) 
                        if Party[0] == "Rogue":
                                ch_r "Well I ain't whistlin Dixie, [R_Petname]."    
                        elif Party[0] == "Kitty":
                                ch_k "I wasn't[K_like]being subtle about it, [K_Petname]." 
                        elif Party[0] == "Emma":
                                ch_e "Surely your education hasn't been that poor, [E_Petname]."
                        elif Party[0] == "Laura":
                                ch_l "Guess."
        elif Line == "praise":
                        call AnyFace(Party[0],"smile",B=1) 
                        if Party[0] == "Rogue":
                                ch_r "Mmm, you know it, [R_Petname]."   
                        elif Party[0] == "Kitty":
                                ch_k "Mmm, hehe."
                        elif Party[0] == "Emma":
                                ch_e "Practice, [E_Petname]."
                        elif Party[0] == "Laura":
                                ch_l "Yeah, I guess?"
        elif Line == "no":
                        $ Speed = 0
                        call AnyFace(Party[0],"angry",B=1,Brows="confused")
                        if Party[0] == "Rogue":
                                 ch_r "Well that's a fine \"how d'ya do,\" when a girl goes to all this trouble!" 
                        elif Party[0] == "Kitty":
                                ch_k "{i}That's{/i} the thanks I get?!"
                        elif Party[0] == "Emma":
                                ch_e "A little \"gratitude\" wouldn't be uncalled for. . ."
                        elif Party[0] == "Laura":
                                ch_l "Huh?"
        else: #if it fell through due to time
                        if Party[0] == "Rogue":
                                ch_r "Heh, I can tell you're awake, [R_Petname]. . ."
                                ch_r "You've been. . . more responsive."    
                        elif Party[0] == "Kitty":
                                ch_k "You can stop faking it, [K_Petname]. . ."
                                ch_k "This guy's telling me you're awake now."
                        elif Party[0] == "Emma":
                                ch_e "I don't know who you think you're fooling."
                                ch_e "You've been awake for a while, [E_Petname]. . ."    
                        elif Party[0] == "Laura":
                                ch_l "You can stop playing dead, [L_Petname]. . ."
                                ch_l "Oldest trick in the book."   
        #end first response phase
                                
        if Partner:        
                #second girl's lines
                if Line == "question":                    
                                call AnyFace(Party[0],"smile",B=1) 
                elif Line == "praise":
                                call AnyFace(Party[0],"smile",B=1) 
                elif Line == "no":
                                call AnyFace(Party[0],"angry",B=1,Brows="confused")
                        
                if Partner == "Rogue":       
                        if "blow" in R_RecentActions:
                            ch_r "I don't know 'bout that, [R_Petname]."
                        else:
                            "Rogue rolls over in bed."
                            ch_r "Don't stop on my account, [R_Petname]."  
                elif Partner == "Kitty":
                        if "blow" in K_RecentActions:
                            ch_k "Huh. . ."
                        else:
                            "Kitty rolls over in bed."
                            ch_k "Looked like you were having some fun there . . ."
                elif Partner == "Emma":
                        if "blow" in E_RecentActions:
                            ch_e "Well. . ."
                        else:
                            "Emma rolls over in bed."
                            ch_e "Oh, don't let me stop you two."
                elif Partner == "Laura":
                        if "blow" in L_RecentActions:
                            ch_l "Hmm. . ."
                        else:
                            "Laura rolls over in bed and stares at you both."
                                
        #start second question phase
        menu:
            extend ""
            "So, um, you want to get back to it?":
                    if Line != "no":
                        #assuming you weren't rude
                        call AnyFace(Party[0],"smile",B=1)                              
                        if Party[0] == "Rogue":
                                ch_r "My pleasure."     
                        elif Party[0] == "Kitty":
                                ch_k "Hehe, mmmm. . ."
                        elif Party[0] == "Emma":
                                ch_e "If you insist. . ."
                        elif Party[0] == "Laura":
                                ch_l "That's the plan. . ."    
                    elif Line == "no" and ApprovalCheck(Party[0], 1750):
                        #if you were a dick but she's ok
                        call AnyFace(Party[0],"bemused")
                        if Party[0] == "Rogue":
                                ch_r "You're lucky I'm so into you. . ."    
                        elif Party[0] == "Kitty":
                                ch_k "Wha? Well. . . I guess. . ."
                        elif Party[0] == "Emma":
                                ch_e "Do try not to be a prat this time. . ."
                        elif Party[0] == "Laura":
                                ch_l "Fine. . ."   
                        $ Line = "maybe"
                    else:
                        #if you were a dick and she's not ok with that
                        call AnyFace(Party[0],"angry",B=1)  
                        if Party[0] == "Rogue":
                                ch_r "Well not when you're rude to me."                
                                ch_r "You can polish yourself off."     
                        elif Party[0] == "Kitty":
                                ch_k "You can't walk that one back!"
                                ch_k "You can take care of that yourself."
                        elif Party[0] == "Emma":
                                ch_e "Not with your attitude."
                                ch_e "I think you can manage to finish this yourself."
                        elif Party[0] == "Laura":
                                ch_l "No."  
            "Were you more interested in something else?":
                    if Line != "no":
                        #assuming you weren't rude
                        call AnyFace(Party[0],"sexy",B=1)  
                        if Party[0] == "Rogue":
                                ch_r "Ooh, what did you have in mind?"  
                        elif Party[0] == "Kitty":
                                ch_k "Maaaybee. . . like what?"
                        elif Party[0] == "Emma":
                                ch_e "Perhaps. . . What did you have in mind?"
                        elif Party[0] == "Laura":
                                ch_l "Yeah, I guess?"
                        $ Line = "sex"
                    elif Line == "no" and ApprovalCheck(Party[0], 1650):
                        #if you were a dick but she's ok
                        call AnyFace(Party[0],"bemused",B=1)  
                        if Party[0] == "Rogue":
                                ch_r "Well, you're a jerk, but you're a cute jerk."
                                ch_r "What were you thinking?"     
                        elif Party[0] == "Kitty":
                                ch_k "Oh, so you had something {i}else{/i} in mind. . ."
                                ch_k "Like what?"
                        elif Party[0] == "Emma":
                                ch_e "Hmm, second chance [E_Petname], what were you considering?"
                        elif Party[0] == "Laura":
                                ch_l "Yeah, I guess?"
                        $ Line = "sex"
                    else:
                        #if you were a dick and she's not ok with that
                        call AnyFace(Party[0],"angry",B=1)  
                        if Party[0] == "Rogue":
                                ch_r "Well not when you're rude to me."                
                                ch_r "You can polish yourself off."     
                        elif Party[0] == "Kitty":
                                ch_k "You can't walk that one back!"
                                ch_k "You can take care of that yourself."
                        elif Party[0] == "Emma":
                                ch_e "Not with your attitude."
                                ch_e "I think you can manage to finish this yourself."
                        elif Party[0] == "Laura":
                                ch_l "No."  
            "Sorry, sorry, please continue." if Line == "no":
                    if ApprovalCheck(Party[0], 1450):
                        #if you were a dick but she's ok
                        call AnyFace(Party[0],"bemused",B=1)  
                        if Party[0] == "Rogue":
                                ch_r "Well, since you asked so nice. . ."    
                        elif Party[0] == "Kitty":
                                ch_k "I guess I can forgive you. . ."
                        elif Party[0] == "Emma":
                                ch_e "Ok, I'll give you another chance here."
                        elif Party[0] == "Laura":
                                ch_l "Yeah, I guess?"
                        $ Line = "maybe"
                    else:
                        #if you were a dick and she's not ok with that
                        call AnyFace(Party[0],"angry",B=1)  
                        if Party[0] == "Rogue":
                                ch_r "Well not when you're rude to me."                
                                ch_r "You can polish yourself off."     
                        elif Party[0] == "Kitty":
                                ch_k "You can't walk that one back!"
                                ch_k "You can take care of that yourself."
                        elif Party[0] == "Emma":
                                ch_e "Not with your attitude."
                                ch_e "I think you can manage to finish this yourself."
                        elif Party[0] == "Laura":
                                ch_l "No."  
            "Sorry, but we could do something else." if Line == "no":
                    if ApprovalCheck(Party[0], 1350):
                        #if you were a dick but she's ok
                        call AnyFace(Party[0],"sexy",B=1)  
                        if Party[0] == "Rogue":
                                ch_r "Well, since you asked so nice. . ."
                                ch_r "What did you have in mind?"   
                        elif Party[0] == "Kitty":
                                ch_k "I guess, maybe. . ."
                                ch_k "Like what?"
                        elif Party[0] == "Emma":
                                ch_e "Mmm, I'll consider it. . ."
                        elif Party[0] == "Laura":
                                ch_l "Yeah, I guess?"                                    
                        $ Line = "sex"
                    else:
                        #if you were a dick and she's not ok with that
                        call AnyFace(Party[0],"angry",B=1) 
                        if Party[0] == "Rogue":
                                ch_r "Well not when you're rude to me."                
                                ch_r "You can polish yourself off."     
                        elif Party[0] == "Kitty":
                                ch_k "You can't walk that one back!"
                                ch_k "You can take care of that yourself."
                        elif Party[0] == "Emma":
                                ch_e "Not with your attitude."
                                ch_e "I think you can manage to finish this yourself."
                        elif Party[0] == "Laura":
                                ch_l "No."  
            "Not when I'm just waking up.":
                        call AnyFace(Party[0],"angry",B=1)  
                        if Party[0] == "Rogue":
                                ch_r "Fine, whatever!"
                                $R_Eyes = "side"
                                ch_r "[[mumbles] Girl tries to do a favor. . ."     
                        elif Party[0] == "Kitty":
                                ch_k "Aw. . ."
                                $K_Eyes = "side"
                                ch_k "Last time I do you a favor. . ."
                        elif Party[0] == "Emma":
                                ch_e "Hmph. . ."
                                $E_Eyes = "side"
                                ch_e "It's not as though that was for my benefit. . ."
                        elif Party[0] == "Laura":
                                ch_l "Tsk. . ."
                                $L_Eyes = "side"
                                ch_l "\"No free blowjobs,\" got it. . ."                                    
                        $ Line = "no"
        #end second question phase
                    
                       
        if Line == "no" or Line == "sex":
                call AnyFace(Partner,"sexy") 
                if Party[0] == "Rogue":      
                        $ R_RecentActions.remove("blanket") 
                        call Rogue_BJ_Reset
                elif Party[0] == "Kitty":
                        $ K_RecentActions.remove("blanket")           
                        call Kitty_BJ_Reset
                elif Party[0] == "Emma":
                        $ E_RecentActions.remove("blanket")           
                        call Emma_BJ_Reset
                elif Party[0] == "Laura":
                        $ L_RecentActions.remove("blanket")           
                        call Laura_BJ_Reset                
                if len(Party) >= 2:
                    if Party[1] == "Rogue":       
                            show Rogue:
                                ease 1 pos (700,50)
                            show Rogue:
                                pos (700,50)
                    elif Party[1] == "Kitty":     
                            show Kitty_Sprite:
                                ease 1 pos (700,50)
                            show Kitty_Sprite:
                                pos (700,50)
                    elif Party[1] == "Emma":      
                            show Emma_Sprite:
                                ease 1 pos (700,50)
                            show Emma_Sprite:
                                pos (700,50)
                    elif Party[1] == "Laura":     
                            show Laura_Sprite:
                                ease 1 pos (700,50)  
                            show Laura_Sprite:
                                pos (700,50)  
                        
                
                if Line == "no":     
                        if bg_current == "bg player":               
                            call AnyLine(Party[0],"I'm out of here.")  
                            call AnyLine(Partner,"Yeah, me too.")  
                        else:
                            call AnyLine(Party[0],"Oh, get out of here already.")  
                        
                        call AnyOutfit(Party[0],6) #sets to OutfitDay
                        call AnyOutfit(Partner,6) #sets to OutfitDay
                        $ Party = []
                        $ Partner = 0
                        $ renpy.pop_call()
                        jump Return_Player
                        
                elif Line == "sex":
                        #shift to other sex stuff with her
                        $ Situation = "shift"
        else: 
                #continue with the BJ
                $ Line = 0
                $ Speed = 1
                $ Situation = "blow"
                if Partner:
                    $ Trigger4 = "blow"
        return
    
# end Event Morning Wood /////////////////////////////////////////////////////    

label Morning_Partner: 
        #Called from sex act menu
        call AnyFace(Partner,"sexy") 
        if Partner == "Rogue":       
                show Rogue:
                    ease 1 pos (700,50)
                show Rogue:
                    pos (700,50)
        elif Partner == "Emma":      
                show Emma_Sprite:
                    ease 1 pos (700,50)
                show Emma_Sprite:
                    pos (700,50)
        elif Partner == "Kitty":     
                show Kitty_Sprite:
                    ease 1 pos (700,50)  
                show Kitty_Sprite:
                    pos (700,50) 
        elif Partner == "Laura":     
                show Laura_Sprite:
                    ease 1 pos (700,50)  
                show Laura_Sprite:
                    pos (700,50) 
        return
    
    
# start Morning Wood Check/////////////////////////////////////////////////////    

label Morningwood_Check(Girls=[0,-3],Line=0,D20=0):                
        #This element sends player to the Morningwood event or returns them
        #it is called from Sleepover_Morning
        
        $ D20 = renpy.random.randint(0,3)  
        $ Line = 0
        
        if len(Party) >= 2:
                #builds a modifier for how the girls like each other
                if GirlLikeCheck(Party[0],Party[1]) >= 900:
                        # If the first girl really likes the second
                        $ Girls[0] = 2
                elif GirlLikeCheck(Party[0],Party[1]) >= 750:
                        # If the first girl kinda likes the second
                        $ Girls[0] = 0
                elif GirlLikeCheck(Party[0],Party[1]) <= 400:
                        # If the first girl really hates the second
                        $ Girls[0] = 2
                else:
                        $ Girls[0] = 0
                    
                if GirlLikeCheck(Party[1],Party[0]) >= 900:
                        # If the second girl really likes the first
                        $ Girls[1] = 2
                elif GirlLikeCheck(Party[1],Party[0]) >= 750:
                        # If the second girl kinda likes the first
                        $ Girls[1] = 0
                elif GirlLikeCheck(Party[1],Party[0]) <= 400:
                        # If the second girl really hates the first
                        $ Girls[1] = -5
                else:
                        $ Girls[1] = -3
        else:
                $ Girls[0] -= 2
        
        if Party[0] == "Rogue":
                #checks if Rogue wants to do it
                if R_Blow >= 5 or ApprovalCheck("Rogue", 900, "I"):  
                        $ Girls[0] += 3
                elif R_Blow and ApprovalCheck("Rogue", 900):
                        $ Girls[0] += 2
                elif ApprovalCheck("Rogue", 1400):
                        $ Girls[0] += 2
                elif R_Blow or ApprovalCheck("Rogue", 900):
                        $ Girls[0] += 1
                        
                if "hungry" in R_Traits and D20 >= 2:
                        #if she likes cum and gets a 50-70 result
                        $ Girls[0] += 2
                if R_Lust >= 50:
                        #if she's horny
                        $ Girls[0] += 1
                if R_SEXP <= 15:
                        #if she's inexperienced
                        $ Girls[0] -= 1                        
        elif Party[0] == "Kitty":
                #checks if Kitty wants to do it
                if K_Blow >= 5 or ApprovalCheck("Kitty", 900, "I"):  
                        $ Girls[0] += 3
                elif K_Blow and ApprovalCheck("Kitty", 900):
                        $ Girls[0] += 2
                elif ApprovalCheck("Kitty", 1400):
                        $ Girls[0] += 2
                elif K_Blow or ApprovalCheck("Kitty", 900):
                        $ Girls[0] += 1
                        
                if "hungry" in K_Traits and D20 >= 2:
                        #if she likes cum and gets a 50-70 result
                        $ Girls[0] += 2
                if K_Lust >= 50:
                        #if she's horny
                        $ Girls[0] += 1
                if K_SEXP <= 15:
                        #if she's inexperienced
                        $ Girls[0] -= 1                            
        elif Party[0] == "Emma":
                #checks if Emma wants to do it
                if E_Blow >= 5 or ApprovalCheck("Emma", 900, "I"):  
                        $ Girls[0] += 3
                elif E_Blow and ApprovalCheck("Emma", 900):
                        $ Girls[0] += 2
                elif ApprovalCheck("Emma", 1400):
                        $ Girls[0] += 2
                elif E_Blow or ApprovalCheck("Emma", 900):
                        $ Girls[0] += 1
                        
                if "hungry" in E_Traits and D20 >= 2:
                        #if she likes cum and gets a 50-70 result
                        $ Girls[0] += 2
                if E_Lust >= 50:
                        #if she's horny
                        $ Girls[0] += 1
                if E_SEXP <= 15:
                        #if she's inexperienced
                        $ Girls[0] -= 1
        elif Party[0] == "Laura":
                #checks if Laura wants to do it
                if L_Blow >= 5 or ApprovalCheck("Laura", 900, "I"):  
                        $ Girls[0] += 3
                elif L_Blow and ApprovalCheck("Laura", 900):
                        $ Girls[0] += 2
                elif ApprovalCheck("Laura", 1400):
                        $ Girls[0] += 2
                elif L_Blow or ApprovalCheck("Laura", 900):
                        $ Girls[0] += 1
                        
                if "hungry" in L_Traits and D20 >= 2:
                        #if she likes cum and gets a 50-70 result
                        $ Girls[0] += 2
                if L_Lust >= 50:
                        #if she's horny
                        $ Girls[0] += 1
                if L_SEXP <= 15:
                        #if she's inexperienced
                        $ Girls[0] -= 1
        #end first girls
        
        if Girls[1] >= 0:
                # if the other girl quite likes her
                $ Girls[0] += 1
                
        #minimum: -1 likely: 3 maximum: 9
        if Girls[0] >= D20:
                $ Line = "yes"  
                
        #end first girl check, Girls[0] maybe "yes," maybe 0
        
        if len(Party) >= 2:
            if Party[1] == "Rogue":
                    #checks if Rogue wants to do it
                    if R_Blow >= 5 or ApprovalCheck("Rogue", 900, "I"):  
                            $ Girls[1] += 3
                    elif R_Blow and ApprovalCheck("Rogue", 900):
                            $ Girls[1] += 2
                    elif ApprovalCheck("Rogue", 1400):
                            $ Girls[1] += 2
                    elif R_Blow or ApprovalCheck("Rogue", 900):
                            $ Girls[1] += 1
                            
                    if "hungry" in R_Traits and D20 >= 2:
                            #if she likes cum and gets a 50-70 result
                            $ Girls[1] += 2
                    if R_Lust >= 50:
                            #if she's horny
                            $ Girls[1] += 1
                    if R_SEXP <= 15:
                            #if she's inexperienced
                            $ Girls[1] -= 2
                            
            elif Party[1] == "Kitty":
                    #checks if Kitty wants to do it
                    if K_Blow >= 5 or ApprovalCheck("Kitty", 900, "I"):  
                            $ Girls[1] += 3
                    elif K_Blow and ApprovalCheck("Kitty", 900):
                            $ Girls[1] += 2
                    elif ApprovalCheck("Kitty", 1400):
                            $ Girls[1] += 2
                    elif K_Blow or ApprovalCheck("Kitty", 900):
                            $ Girls[1] += 1
                            
                    if "hungry" in K_Traits and D20 >= 2:
                            #if she likes cum and gets a 50-70 result
                            $ Girls[1] += 2
                    if K_Lust >= 50:
                            #if she's horny
                            $ Girls[1] += 1
                    if K_SEXP <= 15:
                            #if she's inexperienced
                            $ Girls[1] -= 2    
            elif Party[1] == "Emma":
                    #checks if Emma wants to do it
                    if E_Blow >= 5 or ApprovalCheck("Emma", 900, "I"):  
                            $ Girls[1] += 3
                    elif E_Blow and ApprovalCheck("Emma", 900):
                            $ Girls[1] += 2
                    elif ApprovalCheck("Emma", 1400):
                            $ Girls[1] += 2
                    elif E_Blow or ApprovalCheck("Emma", 900):
                            $ Girls[1] += 1
                            
                    if "hungry" in E_Traits and D20 >= 2:
                            #if she likes cum and gets a 50-70 result
                            $ Girls[1] += 2
                    if E_Lust >= 50:
                            #if she's horny
                            $ Girls[1] += 1
                    if E_SEXP <= 15:
                            #if she's inexperienced
                            $ Girls[1] -= 2
            elif Party[1] == "Laura":
                    #checks if Laura wants to do it
                    if L_Blow >= 5 or ApprovalCheck("Laura", 900, "I"):  
                            $ Girls[1] += 3
                    elif L_Blow and ApprovalCheck("Laura", 900):
                            $ Girls[1] += 2
                    elif ApprovalCheck("Laura", 1400):
                            $ Girls[1] += 2
                    elif L_Blow or ApprovalCheck("Laura", 900):
                            $ Girls[1] += 1
                            
                    if "hungry" in L_Traits and D20 >= 2:
                            #if she likes cum and gets a 50-70 result
                            $ Girls[1] += 2
                    if L_Lust >= 50:
                            #if she's horny
                            $ Girls[1] += 1
                    if L_SEXP <= 15:
                            #if she's inexperienced
                            $ Girls[1] -= 2
            #end second girls
                            
            if Girls[0] >= 0:
                    # if the other girl quite likes her
                    $ Girls[1] += 1
                    
            #minimum: -6 likely: 2 maximum: 9
            if Girls[1] >= (D20 + 1):# 1-4
                    if Line == "yes": #if the first girl agreed
                            $ Line = "double"  
                    else:
                            $ Line = "other"  
            elif Girls[1] <= -1:
                    $ Line = "no"  
            #else: stays "yes"
                            
            if Line == "other" and GirlLikeCheck(Party[0],Party[1]) >= 500:
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
                        if Party[1] == "Rogue":
                                ch_r "You get'cher head out of there, [Party[0]]!"   
                        elif Party[1] == "Kitty":
                                "You hear a thump and feel a small woosh as something heavy drops under the bed."                                   
                                call AnyLine(Party[0],"Ow!")
                                ch_k "Serves you right, [Party[0]]."
                        elif Party[1] == "Emma":
                                ch_e "Step away from [Playername], [Party[0]]."
                        elif Party[1] == "Laura":
                                ch_l "Back it up, [Party[0]]."     
                                
                        if Party[0] == "Rogue":
                                ch_r "I didn't mean no harm, [Party[1]]."   
                        elif Party[0] == "Kitty":
                                "You hear a thump and feel a small woosh as something drops under the bed."                                   
                                call AnyLine(Party[0],"Ow!")
                                ch_k "Spoilsport."
                        elif Party[0] == "Emma":
                                ch_e "Don't be a bore, dear."
                        elif Party[0] == "Laura":
                                ch_l "Fine, whatever."
                        return
            elif Line == "double":
                        # it's a threesome
                        $ Trigger4 = "blow"
                        if Party[1] == "Rogue":     
                                $ R_RecentActions.append("blow")           
                                $ R_DailyActions.append("blow")                          
                                $ R_DailyActions.append("morningwood")  
                        elif Party[1] == "Kitty":     
                                $ K_RecentActions.append("blow")           
                                $ K_DailyActions.append("blow")                          
                                $ K_DailyActions.append("morningwood")  
                        elif Party[1] == "Emma":                            
                                $ E_RecentActions.append("blow")           
                                $ E_DailyActions.append("blow")                          
                                $ E_DailyActions.append("morningwood")   
                        elif Party[1] == "Laura":     
                                $ L_RecentActions.append("blow")           
                                $ L_DailyActions.append("blow")                          
                                $ L_DailyActions.append("morningwood")     
            # it's a solo act with girl 1
            if Party[0] == "Rogue":
                    call Rogue_SexAct("morningwood")   
            elif Party[0] == "Kitty":
                    call Kitty_SexAct("morningwood")
            elif Party[0] == "Emma":
                    call Emma_SexAct("morningwood")
            elif Party[0] == "Laura":
                    call Laura_SexAct("morningwood")
            call Sex_Over(0)
            #end "yes"
            
        else: #Girls[0] = 0
            #neither girl was interested 
            pass
            
        return


# end Morning Wood Check///////////////////////////////////////////////////// 


    
    
    
## start Poly _Start//////////////////////////////////////////////////////////
label Poly_Start(Newbie=0,Round2=0):
        # This is called prior to any new girls being added to your dating structure
        # If there are already two girls in there, it kicks up to the Harem version. 
        # Newbie will be the new girl
        $ Line = 0
                
        if not P_Harem:            
            return
        if len(P_Harem) >= 2:
            call Harem_Start(Newbie,Round2)
            return
            
        if "polystart" in P_DailyActions:
                return                
        $ P_DailyActions.append("polystart")
        
        $ Party = [P_Harem[0]]
        call Shift_Focus(P_Harem[0])
        call Set_The_Scene
        call CleartheRoom(P_Harem[0])
        
            
        if Round2:
                "You pull [Party[0]] aside for a moment."
                ch_p "Hey, have you changed your mind about [Newbie] lately?"
        else:
                call AnyFace(Party[0],"bemused")
                "[Party[0]] pulls you aside and wants to talk about something."
                
                #Line 1
                if Party[0] == "Rogue":                 
                        ch_r "I've seen you were getting pretty cozy with [Newbie]."
                elif Party[0] == "Kitty":      
                        ch_k "You look kinda close with [Newbie] lately."
                elif Party[0] == "Emma":      
                        ch_e "I've noticed that [Newbie] and yourself have been spending time together."
                elif Party[0] == "Laura":     
                        ch_l "You've been all over [Newbie] lately."
                #end Line 1
        
        
        if GirlLikeCheck(Party[0],Newbie) >= 800:
                call AnyFace(Party[0],"sly")  
        elif GirlLikeCheck(Party[0],Newbie) >= 600:
                pass
        else:
                # neither likes her much
                call AnyFace(Party[0],"angry",Mouth="normal")  
                
        # We like her or not
        if Party[0] == "Rogue":       
                if GirlLikeCheck(Party[0],Newbie) >= 800:
                        # if they both like her a lot
                        ch_r "She is pretty sexy, I guess."
                elif GirlLikeCheck(Party[0],Newbie) >= 600:
                        # if they both like her well enough
                        ch_r "I like her just fine, I was just wondering where it was headed."               
                else:
                        # neither likes her much
                        ch_r "I'm not really a fan'a hers."                    
        elif Party[0] == "Kitty":    
                if GirlLikeCheck(Party[0],Newbie) >= 800:
                        # if they both like her a lot
                        ch_k "She's kinda hot, I get that. . ."
                elif GirlLikeCheck(Party[0],Newbie) >= 600:
                        # if they both like her well enough
                        ch_k "She's ok, sure, but I'm not sure. . ."
                else:
                        # neither likes her much
                        ch_k "I don't really like her much." 
        elif Party[0] == "Emma":     
                if GirlLikeCheck(Party[0],Newbie) >= 800:
                        # if they both like her a lot
                        ch_e "I think she's quite the catch."
                elif GirlLikeCheck(Party[0],Newbie) >= 600:
                        # if they both like her well enough
                        ch_e "I do like her, but have some concerns."
                else:
                        # neither likes her much
                        ch_e "I don't really approve."
        elif Party[0] == "Laura":   
                if GirlLikeCheck(Party[0],Newbie) >= 800:
                        # if they both like her a lot
                        ch_l "She's pretty hot, I get it."
                elif GirlLikeCheck(Party[0],Newbie) >= 600:
                        # if they both like her well enough
                        ch_l "She's ok, I guess."
                else:
                        # neither likes her much
                        ch_l "I don't like her."
        #end line 2
        
        
        #Line 3
        if Party[0] == "Rogue":                 
                ch_r "I don't know how I feel about sharing you with some other girl."
                ch_r "So did you plan to get serious with her?"
        elif Party[0] == "Kitty":      
                ch_k "I don't know about sharing my boyfriend with somebody else."
                ch_k "So are you[K_like]trying to date her?"
        elif Party[0] == "Emma":      
                ch_e "I can be a bit. . . possessive with my partners."
                ch_e "Is this getting serious with her?"
        elif Party[0] == "Laura":     
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
            if GirlLikeCheck(Party[0],Newbie) >= 800:
                    # if they like her a lot
                    $ Line = "yy"
                    call Statup(Party[0], "Love", 90, 5)
                    call Statup(Party[0], "Obed", 50, 5)
                    call Statup(Party[0], "Inbt", 90, 10) 
            elif ApprovalCheck(Party[0], 1800):
                    # if they really like you enough to put up with it
                    $ Line = "ym"
                    call Statup(Party[0], "Obed", 50, 5) 
            elif ApprovalCheck(Party[0], 1500) and GirlLikeCheck(Party[0],Newbie) >= 500:
                    # if they like her well enough
                    $ Line = "ym"
            else:
                    # neither likes her much
                    $ Line = "yn"  
                    call Statup(Party[0], "Love", 90, -10)
        #end Line = y
        if Line == "m":
            if GirlLikeCheck(Party[0],Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "my"
                    call Statup(Party[0], "Inbt", 90, 5) 
            elif ApprovalCheck(Party[0], 1800):
                    # if they both really like you enough to put up with it
                    $ Line = "mm"
            elif ApprovalCheck(Party[0], 1500) and GirlLikeCheck(Party[0],Newbie) >= 600:
                    # if they both like her well enough
                    $ Line = "mm"
            else:
                    # neither likes her much
                    $ Line = "mn" 
        #end Line = m  
        if Line == "n":
            if GirlLikeCheck(Party[0],Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "ny"
                    call Statup(Party[0], "Inbt", 90, 10) 
            elif ApprovalCheck(Party[0], 1700):
                    # if they both really like you enough to put up with it
                    $ Line = "nm"
                    call Statup(Party[0], "Inbt", 90, 5) 
            elif ApprovalCheck(Party[0], 1300) and GirlLikeCheck(Party[0],Newbie) >= 500:
                    # if they both like her well enough
                    $ Line = "nm"
                    call Statup(Party[0], "Love", 90, 5)
            else:
                    # if they don't like her well enough
                    $ Line = "nn"
                    call Statup(Party[0], "Love", 90, 10)
        #end Line = n      
            
            
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
        if Line == "yn" or Line == "mn" or Line == "nn":
                call AnyFace(Party[0],"angry")
        elif Line == "yy" or Line == "ny" or Line == "my":
                call AnyFace(Party[0],"sexy")
        else:
                call AnyFace(Party[0],"bemused")
                
        #Line 5
        if Party[0] == "Rogue":       
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
                        
        elif Party[0] == "Kitty":        
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
                        ch_k "Yeah, I can[K_like]live with that."              
                elif Line == "nm":
                        # if you said no but they both like her well enough    
                        ch_k "Ok, I would have been ok with it though."
                        
                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_k "That's not really cool with me."                          
                elif Line == "nn":
                        # if you said no and agree
                        ch_k "Good, that wouldn't have been cool."
                        
        elif Party[0] == "Emma":          
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
                        
        elif Party[0] == "Laura":        
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
                    call AnyFace(Party[0],"smile")
                    call Statup(Party[0], "Love", 90, 10)
                    call Statup(Party[0], "Obed", 50, 10)
                    if Party[0] == "Rogue":       
                                    ch_r "Great, sounds fun."                 
                    elif Party[0] == "Kitty":        
                                    ch_k "Cool, sounds fun."                                        
                    elif Party[0] == "Emma":          
                                    ch_e "Lovely. . ."                                   
                    elif Party[0] == "Laura":        
                                    ch_l "Nice."   
                
                "Well then, I guess I'll stop." if Line in ("mn","yn","ym","mm","nm"):
                    #They were unfavorable, so you gave up on it. 
                    $ Line = "nn"
                    call AnyFace(Party[0],"smile")
                    call Statup(Party[0], "Love", 90, 10) 
                    if Party[0] == "Rogue":       
                                    ch_r "Good to hear."                        
                    elif Party[0] == "Kitty":        
                                    ch_k "Good, that wouldn't have been cool."                        
                    elif Party[0] == "Emma":       
                                    ch_e "Probably for the best."                        
                    elif Party[0] == "Laura":        
                                    ch_l "Good."
                
                "I'm asking her in anyway." if Line in ("mn","yn"):
                    #if they were unfavorable, but you insist
                    pass
                    
                "Well, I'm going to pass anyway." if Line in ("nm","ny","mm"):
                    #if they give you permission, but you aren't into it.
                    $ Line = "nn"
                    call AnyFace(Party[0],"sad")
                    call Statup(Party[0], "Obed", 70, 5) 
                    if Party[0] == "Rogue":       
                                    ch_r "Oh, ok."                        
                    elif Party[0] == "Kitty":        
                                    ch_k "That's fine."                        
                    elif Party[0] == "Emma": 
                                    ch_e "If you insist."                        
                    elif Party[0] == "Laura":        
                                    ch_l "Ok."
                                                
        #end player response to their feedback
            
        if Line == "mn" or Line == "yn":
                # if you said yes/maybe and they said no, but you insisted anyway 
                                 
                if ApprovalCheck(Party[0], 1600) and GirlLikeCheck(Party[0],Newbie) >= 500:
                            call AnyFace(Party[0],"sadside")
                            call Statup(Party[0], "Love", 90, -5)
                            call Statup(Party[0], "Obed", 50, 15)
                            if Party[0] == "Rogue":                 
                                    ch_r "Fine, she's in."
                            elif Party[0] == "Kitty":      
                                    ch_k "Geeze, ok."
                            elif Party[0] == "Emma":      
                                    ch_e "I suppose we'll make room."
                            elif Party[0] == "Laura":     
                                    ch_l "Whatever."
                            $ Line = "yy"
                else:
                            call AnyFace(Party[0],"angry",Eyes="side")
                            call Statup(Party[0], "Love", 90, -25)
                            call Statup(Party[0], "Inbt", 90, 10) 
                            if Party[0] == "Rogue":                 
                                    ch_r "I just don't like you that much, [R_Petname]."
                                    ch_r "I'm out."                                    
                                    if "dating" in R_Traits:
                                        $ R_Traits.remove("dating")
                                    $ R_Traits.append("ex")
                                    $ R_Break[0] = 5 + R_Break[1] + R_Cheated
                            elif Party[0] == "Kitty":      
                                    ch_k "You aren't that cute, [K_Petname]."
                                    ch_k "I'm done."
                                    if "dating" in K_Traits:
                                        $ K_Traits.remove("dating")
                                    $ K_Traits.append("ex")
                                    $ K_Break[0] = 5 + K_Break[1] + K_Cheated
                            elif Party[0] == "Emma":      
                                    ch_e "Don't overestimate yourself, [E_Petname]."
                                    ch_e "We're done."
                                    if "dating" in E_Traits:
                                        $ E_Traits.remove("dating")
                                    $ E_Traits.append("ex")
                                    $ E_Break[0] = 5 + E_Break[1] + E_Cheated
                            elif Party[0] == "Laura":     
                                    ch_l "Too far, [L_Petname]."
                                    ch_l "I'm out of here."
                                    if "dating" in L_Traits:
                                        $ L_Traits.remove("dating")
                                    $ L_Traits.append("ex")
                                    $ L_Break[0] = 5 + L_Break[1] + L_Cheated
                                    
                            $ P_Harem.remove(Party[0])
                            call Remove_Girl(Party[0])
        #end "she said no but you insisted"        
                   
        $ Party = []
        if Line == "yy":
                $Count = Newbie + "No"
                if Count in P_Traits:                   
                        $ P_Traits.remove(Count)
                $Count = Newbie + "Yes"
                $ P_Traits.append(Count)
                "You should give [Newbie] a call."   
        else:
                $Count = Newbie + "No"
                $ P_Traits.append(Count)
                    
                         
        return
        
## end Poly _Start//////////////////////////////////////////////////////////



## start Harem _Start//////////////////////////////////////////////////////////
label Harem_Start(Newbie=0,Round2=0):    
        # This is called prior to any new girls being added to your dating structure
        # If there are aren't two girls in there, it kicks back. 
        # Newbie will be the new girl
        
        if "harem" in P_DailyActions:
                return                
        $ P_DailyActions.append("harem")
        $ Line = 0
        
        if len(P_Harem) < 2:
                #if there aren't enough girls yet, forget about it.
                return
                
        $ Party = [P_Harem[0],P_Harem[1]]
        # Adds first two harem members to party, removed everyone else from the room.
        call Present_Check        
        $ Party = [P_Harem[0],P_Harem[1]]
        call Shift_Focus(P_Harem[0])
        call Set_The_Scene            
        
        call AnyFace(Party[0],"bemused")
        call AnyFace(Party[1],"bemused")
        if Round2:
                "You call [Party[0]] and [Party[1]] over."
                ch_p "I was wondering if you'd changed your mind about [Newbie]."
        else:
                "[Party[0]] pulls you aside and wants to talk about something."
                #Line 1
                
                if Party[0] == "Rogue":       
                        ch_r "Hey, so me and [Party[1]] have been talk'in."                 
                elif Party[0] == "Kitty":    
                        ch_k "So[K_like]me and [Party[1]] had a little chat."   
                elif Party[0] == "Emma":     
                        ch_e "[Party[1]] and I have been discussing a few things."   
                elif Party[0] == "Laura":   
                        ch_l "I had a little chat with [Party[1]]. . ." 
                #end Line 1
                
                #Line 2
                if Party[1] == "Rogue":                 
                        ch_r "We hear that you were getting pretty cozy with [Newbie]."
                elif Party[1] == "Kitty":      
                        ch_k "We hear that you're kinda close with [Newbie] lately."
                elif Party[1] == "Emma":      
                        ch_e "We've hear that [Newbie] and yourself have been spending time together."
                elif Party[1] == "Laura":     
                        ch_l "You've been all over [Newbie] lately."
                #end Line 2
                
        # We like her or not Line 3
        
        if GirlLikeCheck(Party[0],Newbie) >= 600 and GirlLikeCheck(Party[1],Newbie) >= 600:
                pass
        elif GirlLikeCheck(Party[0],Newbie) >= 700:
                # only first girl likes her
                call AnyFace(Party[1],"angry",Mouth="normal")
        elif GirlLikeCheck(Party[1],Newbie) >= 700:
                # only second girl likes her
                call AnyFace(Party[0],"angry",Mouth="normal")
        else:
                # neither likes her much
                call AnyFace(Party[0],"angry",Mouth="normal") 
                call AnyFace(Party[1],"angry",Mouth="normal")    
                
        if Party[0] == "Rogue":       
                if GirlLikeCheck(Party[0],Newbie) >= 800 and GirlLikeCheck(Party[1],Newbie) >= 800:
                        # if they both like her a lot
                        ch_r "Now we like her just fine, and we can't say we don't like the idea much."
                elif GirlLikeCheck(Party[0],Newbie) >= 600 and GirlLikeCheck(Party[1],Newbie) >= 600:
                        # if they both like her well enough
                        ch_r "Now we like her just fine, but we don't know about share'in."
                elif GirlLikeCheck(Party[0],Newbie) >= 700:
                        # only first girl likes her
                        ch_r "Now I like her just fine, but [Party[1]] ain't so sure."
                elif GirlLikeCheck(Party[1],Newbie) >= 700:
                        # only second girl likes her
                        ch_r "Now [Party[1]] seems to like her, but I'm not so sure."
                else:
                        # neither likes her much
                        ch_r "Neither'a us is really cool with that."                    
        elif Party[0] == "Kitty":    
                if GirlLikeCheck(Party[0],Newbie) >= 800 and GirlLikeCheck(Party[1],Newbie) >= 800:
                        # if they both like her a lot
                        ch_k "She's kinda hot, we get that. . ."
                elif GirlLikeCheck(Party[0],Newbie) >= 600 and GirlLikeCheck(Party[1],Newbie) >= 600:
                        # if they both like her well enough
                        ch_k "She's ok, sure, but we're not sure. . ."
                elif GirlLikeCheck(Party[0],Newbie) >= 700:
                        # only first girl likes her
                        ch_k "I like her, but I don't know about [Party[1]]."
                elif GirlLikeCheck(Party[1],Newbie) >= 700:
                        # only second girl likes her
                        ch_k "[Party[1]] likes her, but I don't know."
                else:
                        # neither likes her much
                        ch_k "We don't really like her much." 
        elif Party[0] == "Emma":     
                if GirlLikeCheck(Party[0],Newbie) >= 800 and GirlLikeCheck(Party[1],Newbie) >= 800:
                        # if they both like her a lot
                        ch_e "I think we agree that she's a nice catch."
                elif GirlLikeCheck(Party[0],Newbie) >= 600 and GirlLikeCheck(Party[1],Newbie) >= 600:
                        # if they both like her well enough
                        ch_e "We do like her, but we have some concerns."
                elif GirlLikeCheck(Party[0],Newbie) >= 700:
                        # only first girl likes her
                        ch_e "[Party[1]] doesn't really approve."
                elif GirlLikeCheck(Party[1],Newbie) >= 700:
                        # only second girl likes her
                        ch_e "[Party[1]] seems to think she's acceptable."
                else:
                        # neither likes her much
                        ch_e "We don't really approve."
        elif Party[0] == "Laura":   
                if GirlLikeCheck(Party[0],Newbie) >= 800 and GirlLikeCheck(Party[1],Newbie) >= 800:
                        # if they both like her a lot
                        ch_l "She's pretty hot, we get it."
                elif GirlLikeCheck(Party[0],Newbie) >= 600 and GirlLikeCheck(Party[1],Newbie) >= 600:
                        # if they both like her well enough
                        ch_l "She's ok, I guess."
                elif GirlLikeCheck(Party[0],Newbie) >= 700:
                        # only first girl likes her
                        ch_l "She's fine, but [Party[1]] doesn't like her."
                elif GirlLikeCheck(Party[1],Newbie) >= 700:
                        # only second girl likes her
                        ch_l "[Party[1]] likes her. I don't."
                else:
                        # neither likes her much
                        ch_l "We don't like her."
        #end line 3
        
        #Line 4
        if Party[1] == "Rogue":                 
                ch_r "So did you plan to get serious with her?"
        elif Party[1] == "Kitty":      
                ch_k "So are you[K_like]trying to date her?"
        elif Party[1] == "Emma":      
                ch_e "Is this getting serious with her?"
        elif Party[1] == "Laura":     
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
            if GirlLikeCheck(Party[0],Newbie) >= 800 and GirlLikeCheck(Party[1],Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "yy"                       
                    call Statup(Party[0], "Love", 90, 5)
                    call Statup(Party[0], "Obed", 50, 5)
                    call Statup(Party[0], "Inbt", 90, 10) 
                    call Statup(Party[1], "Love", 90, 5)
                    call Statup(Party[1], "Obed", 50, 5)
                    call Statup(Party[1], "Inbt", 90, 10) 
            elif ApprovalCheck(Party[0], 1800) and ApprovalCheck(Party[1], 1800):
                    # if they both really like you enough to put up with it
                    $ Line = "ym"
                    call Statup(Party[0], "Obed", 50, 10)
                    call Statup(Party[1], "Obed", 50, 10)
            elif ApprovalCheck(Party[0], 1500) and ApprovalCheck(Party[1], 1500):
                    if GirlLikeCheck(Party[0],Newbie) >= 500 and GirlLikeCheck(Party[1],Newbie) >= 500:
                            # if they both like her well enough
                            $ Line = "ym"
                            call Statup(Party[0], "Obed", 80, 15) 
                            call Statup(Party[1], "Obed", 80, 15) 
                    else:
                            # if they don't like her well enough
                            $ Line = "yn"
                            call Statup(Party[0], "Love", 90, -5)
                            call Statup(Party[0], "Obed", 50, -5)
                            call Statup(Party[1], "Love", 90, -5)
                            call Statup(Party[1], "Obed", 50, -5)
            else:
                            # neither likes her much
                            $ Line = "yn"  
                            call Statup(Party[0], "Love", 90, -10)
                            call Statup(Party[0], "Obed", 50, -5)
                            call Statup(Party[1], "Love", 90, -10)
                            call Statup(Party[1], "Obed", 50, -5)
        #end Line = y
        if Line == "m":
            if GirlLikeCheck(Party[0],Newbie) >= 800 and GirlLikeCheck(Party[1],Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "my"
                    call Statup(Party[0], "Inbt", 90, 5) 
                    call Statup(Party[1], "Inbt", 90, 5) 
            elif ApprovalCheck(Party[0], 1800) and ApprovalCheck(Party[1], 1800):
                    # if they both really like you enough to put up with it
                    $ Line = "mm"
            elif ApprovalCheck(Party[0], 1500) and ApprovalCheck(Party[1], 1500):
                    if GirlLikeCheck(Party[0],Newbie) >= 600 or GirlLikeCheck(Party[1],Newbie) >= 600:
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
            if GirlLikeCheck(Party[0],Newbie) >= 800 and GirlLikeCheck(Party[1],Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "ny"
                    call Statup(Party[0], "Inbt", 90, 10) 
                    call Statup(Party[1], "Inbt", 90, 10) 
            elif ApprovalCheck(Party[0], 1700) and ApprovalCheck(Party[1], 1700):
                    # if they both really like you enough to put up with it
                    $ Line = "nm"
                    call Statup(Party[0], "Inbt", 90, 5) 
            elif ApprovalCheck(Party[0], 1300) and ApprovalCheck(Party[1], 1300):
                    if GirlLikeCheck(Party[0],Newbie) >= 500 and GirlLikeCheck(Party[1],Newbie) >= 500:
                            # if they both like her well enough
                            $ Line = "nm"
                    else:
                            # if they don't like her well enough
                            $ Line = "nn"
                            call Statup(Party[0], "Love", 90, 5)
                            call Statup(Party[0], "Inbt", 90, 5) 
                            call Statup(Party[1], "Love", 90, 5)
                            call Statup(Party[1], "Inbt", 90, 5) 
            else:
                            # neither likes her much
                            $ Line = "nn" 
                            call Statup(Party[0], "Love", 90, 5)
                            call Statup(Party[0], "Inbt", 90, 5) 
                            call Statup(Party[1], "Love", 90, 5)
                            call Statup(Party[1], "Inbt", 90, 5) 
        #end Line = n      
                                                  
            
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                
        if Line == "yn" or Line == "mn" or Line == "nn":
                call AnyFace(Party[0],"angry")
                call AnyFace(Party[1],"angry")
        elif Line == "yy" or Line == "ny" or Line == "my":
                call AnyFace(Party[0],"sexy")
                call AnyFace(Party[1],"sexy")
        else:
                call AnyFace(Party[0],"bemused")
                call AnyFace(Party[1],"bemused")   
                
        #Line 5
        if Party[0] == "Rogue":       
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
                        
        elif Party[0] == "Kitty":        
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
                        ch_k "Yeah, we can[K_like]live with that."              
                elif Line == "nm":
                        # if you said no but they both like her well enough    
                        ch_k "Ok, we would have been ok with it though."
                        
                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_k "That's not really cool with us."                          
                elif Line == "nn":
                        # if you said no and agree
                        ch_k "Good, that wouldn't have been cool."
                        
        elif Party[0] == "Emma":          
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
                        
        elif Party[0] == "Laura":        
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
                        call AnyFace(Party[0],"smile")
                        call AnyFace(Party[1],"smile")   
                        call Statup(Party[0], "Obed", 80, 5)
                        call Statup(Party[0], "Inbt", 90, 10) 
                        call Statup(Party[1], "Obed", 80, 5)
                        call Statup(Party[1], "Inbt", 90, 10) 
                        if Party[0] == "Rogue":       
                                    ch_r "Great, sounds fun."                 
                        elif Party[0] == "Kitty":        
                                    ch_k "Cool, sounds fun."                                        
                        elif Party[0] == "Emma":          
                                    ch_e "Lovely. . ."                                   
                        elif Party[0] == "Laura":        
                                    ch_l "Nice."                     
                "Well then, I guess I'll stop." if Line in ("mn","yn"):
                        #They were unfavorable, so you gave up on it. 
                        $ Line = "nn"
                        call AnyFace(Party[0],"normal")
                        call AnyFace(Party[1],"normal")  
                        call Statup(Party[0], "Love", 90, 5)
                        call Statup(Party[0], "Inbt", 90, 5)  
                        call Statup(Party[1], "Love", 90, 5)
                        call Statup(Party[1], "Inbt", 90, 5)                                
                        if Party[0] == "Rogue":       
                                        ch_r "Good to hear."                        
                        elif Party[0] == "Kitty":        
                                        ch_k "Good, that wouldn't have been cool."                        
                        elif Party[0] == "Emma":       
                                        ch_e "Probably for the best."                        
                        elif Party[0] == "Laura":        
                                        ch_l "Good."                    
                "I'm asking her in anyway." if Line in ("mn","yn"):
                        #if they were unfavorable, but you insist
                        pass
                    
                "Well, I'm going to pass anyway." if Line in ("ym","my","nm","ny","mm"):
                        #if they give you permission, but you aren't into it.
                        $ Line = "nn"
                        call AnyFace(Party[0],"sad")
                        call AnyFace(Party[1],"sad")  
                        call Statup(Party[0], "Obed", 50, 5) 
                        call Statup(Party[1], "Obed", 50, 5) 
                        if Party[0] == "Rogue":       
                                        ch_r "Oh, ok."                        
                        elif Party[0] == "Kitty":        
                                        ch_k "That's fine."                        
                        elif Party[0] == "Emma": 
                                        ch_e "If you insist."                        
                        elif Party[0] == "Laura":        
                                        ch_l "Ok."
            #end player response to their feedback
            
            if Line == "yy" or Line == "nn":
                                pass
            elif len(P_Harem) >= 3:
                                call AnyFace(Party[0],"smile",Eyes="side")
                                call AnyFace(Party[1],"smile",Eyes="side") 
                                call Statup(Party[0], "Obed", 90, 5)
                                call Statup(Party[0], "Inbt", 90, 5) 
                                if Party[0] == "Rogue":                 
                                        ch_r "Oh, what's one more."
                                elif Party[0] == "Kitty":      
                                        ch_k "We're building a real \"pride\" here."
                                elif Party[0] == "Emma":      
                                        ch_e "I suppose one more can't hurt."
                                elif Party[0] == "Laura":     
                                        ch_l "Whatever."
                                $ Line = "yy"
            elif Line == "mn" or Line == "yn":
                    # if you said yes/maybe and they said no, but you insisted anyway 
                    $Count = 0
                    while Count < 2:
                        if ApprovalCheck(Party[Count], 1600) and GirlLikeCheck(Party[Count],Newbie) >= 500:
                                # She likes you enough to roll over
                                call AnyFace(Party[Count],"sadside")
                                call Statup(Party[Count], "Love", 90, -5)
                                call Statup(Party[Count], "Obed", 90, 10)
                                if Party[Count] == "Rogue":                 
                                        ch_r "Fine, she's in."
                                elif Party[Count] == "Kitty":      
                                        ch_k "Geeze, ok."
                                elif Party[Count] == "Emma":      
                                        ch_e "I suppose we'll make room."
                                elif Party[Count] == "Laura":     
                                        ch_l "Whatever."
                                $ Line = "yy"
                        else:
                                # She doewsn't like you enough to roll over
                                call AnyFace(Party[Count],"angry",Eyes="side")
                                call Statup(Party[Count], "Love", 90, -25)
                                call Statup(Party[Count], "Inbt", 90, 10) 
                                if Party[Count] == "Rogue":                 
                                        ch_r "I just don't like you that much, [R_Petname]."
                                        ch_r "I'm out."
                                        if "dating" in R_Traits:
                                            $ R_Traits.remove("dating")
                                        $ R_Traits.append("ex")
                                        $ R_Break[0] = 5 + R_Break[1] + R_Cheated
                                elif Party[Count] == "Kitty":      
                                        ch_k "You aren't that cute, [K_Petname]."
                                        ch_k "I'm done."
                                        if "dating" in K_Traits:
                                            $ K_Traits.remove("dating")
                                        $ K_Traits.append("ex")
                                        $ K_Break[0] = 5 + K_Break[1] + K_Cheated
                                elif Party[Count] == "Emma":      
                                        ch_e "Don't overestimate yourself, [E_Petname]."
                                        ch_e "We're done."
                                        if "dating" in E_Traits:
                                            $ E_Traits.remove("dating")
                                        $ E_Traits.append("ex")
                                        $ E_Break[0] = 5 + E_Break[1] + E_Cheated
                                elif Party[Count] == "Laura":     
                                        ch_l "Too far, [L_Petname]."
                                        ch_l "I'm out of here."
                                        if "dating" in L_Traits:
                                            $ L_Traits.remove("dating")
                                        $ L_Traits.append("ex")
                                        $ L_Break[0] = 5 + L_Break[1] + L_Cheated
                                        
                                $ P_Harem.remove(Party[Count])
                                call Remove_Girl(Party[Count])
                        $ Count += 1
            #end "she said no but you insisted"
        
        if Line == "yy":
                $Count = Newbie + "No"
                if Count in P_Traits:                   
                        $ P_Traits.remove(Count)
                $Count = Newbie + "Yes"
                $ P_Traits.append(Count)
                "You should give [Newbie] a call."   
        else:
                $Count = Newbie + "No"
                $ P_Traits.append(Count)
                
        $ Party = []
        $Count = 0
                         
        return
        
        
        
label Harem_Initiation:  
    # This is called when a new girl is added to the pack
    # it makes them more open to sexing each other. 
    if "Rogue" in P_Harem:
            if "Kitty" in P_Harem:
                if "poly Kitty" not in R_Traits:
                    $ R_Traits.append("poly Kitty")
            if "Emma" in P_Harem:
                if "poly Emma" not in R_Traits:
                    $ R_Traits.append("poly Emma")
            if "Laura" in P_Harem:
                if "poly Laura" not in R_Traits:
                    $ R_Traits.append("poly Laura")    
    if "Kitty" in P_Harem:
            if "Rogue" in P_Harem:
                if "poly Rogue" not in K_Traits:
                    $ K_Traits.append("poly Rogue")
            if "Emma" in P_Harem:
                if "poly Emma" not in K_Traits:
                    $ K_Traits.append("poly Emma")
            if "Laura" in P_Harem:
                if "poly Laura" not in K_Traits:
                    $ K_Traits.append("poly Laura") 
    if "Emma" in P_Harem:
            if "Rogue" in P_Harem:
                if "poly Rogue" not in E_Traits:
                    $ E_Traits.append("poly Rogue")
            if "Kitty" in P_Harem:
                if "poly Kitty" not in E_Traits:
                    $ E_Traits.append("poly Kitty")
            if "Laura" in P_Harem:
                if "poly Laura" not in E_Traits:
                    $ E_Traits.append("poly Laura") 
    if "Laura" in P_Harem:
            if "Rogue" in P_Harem:
                if "poly Rogue" not in L_Traits:
                    $ L_Traits.append("poly Rogue")
            if "Kitty" in P_Harem:
                if "poly Kitty" not in L_Traits:
                    $ L_Traits.append("poly Kitty")
            if "Emma" in P_Harem:
                if "poly Emma" not in L_Traits:
                    $ L_Traits.append("poly Emma")
    return
## end Harem _Start//////////////////////////////////////////////////////////


#start study session / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 

label Study_Session:                       
            #study events, girl is the lead girl in the scene
            $ Party = []
            if R_Loc == bg_current:
                    $ Party.append("Rogue")
            if K_Loc == bg_current:
                    $ Party.append("Kitty")
            if E_Loc == bg_current:
                    $ Party.append("Emma")
            if L_Loc == bg_current:
                    $ Party.append("Laura")
            if not Party:
                "There's nobody here to study with."
                return
                
            $ renpy.random.shuffle(Party)
            
            if Current_Time == "Night":                        
                if "Emma" in Party:
                        ch_e "It's a little late for a study session, maybe tomorrow."
                elif Party[0] == "Rogue":
                        ch_r "It's a little late for studying, maybe tomorrow."
                elif Party[0] == "Kitty":
                        ch_k "It's kinda late for studying. . . Tomorrow?"
                elif Party[0] == "Laura":
                        ch_l "It's late. Maybe tomorrow."
                $ Party = []
                return
            elif Round <= 30:         
                if "Emma" in Party:
                        ch_e "I'm afraid I was just about to take a break, perhaps another time. . ."
                elif Party[0] == "Rogue":
                        ch_r "I don't know that there's time for that, maybe if we wait a bit. . ."
                elif Party[0] == "Kitty":
                        ch_k "I don't know that there's time for that, maybe if we wait a bit. . ."
                elif Party[0] == "Laura":
                        ch_l "I was about to take a break, maybe wait a bit."                        
                $ Party = []
                return
                
            elif "Emma" in Party and len(Party) >= 2: 
                ch_e "I suppose you could both use some work."
            else:
                if "Emma" in Party:
                        ch_e "Very well."
                elif Party[0] == "Rogue":
                        ch_r "Sure."
                elif Party[0] == "Kitty":
                        ch_k "Sure."
                elif Party[0] == "Laura":
                        ch_l "Fine." 
                        
            
            $ P_RecentActions.append("study")
            $ P_XP += 5
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
            
            call Statup(Party[0], "Love", 80, 2)
            if len(Party) >= 2:
                call Statup(Party[1], "Love", 80, 2)
                call GirlLikesGirl(Party[0],Party[1],700,5,1)
                call GirlLikesGirl(Party[1],Party[0],700,5,1)
                #raises both girl's likes of each other by 5 if they are under 70 
            
            $ D20 = renpy.random.randint(1, 20)   
            
            #There might be sexy time
            if len(Party) >= 2 and "Emma" in Party and "three" not in E_History:
                $ Line = "no"
                                                             
            if Line != "no" and D20 >= 10: 
                call Frisky_Study             
            else:
                # if there is no frisky stuff
                if "Emma" in Party:
                        ch_e "I'm afraid it's getting a bit late, we should wrap this up. . ."
                elif Party[0] == "Rogue":
                        ch_r "It's getting a bit late, we should wrap this up. . ."
                elif Party[0] == "Kitty":
                        ch_k "It's kinda late, we should probably stop. . ."
                elif Party[0] == "Laura":
                        ch_l "I'm bored now."            
                $ P_XP += 5  
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
            
            if Party[0] == "Rogue":
                        if D20 > 17 and ApprovalCheck("Rogue", 1000) and R_Blow > 5:
                                $ Line = "blow"
                        elif D20 > 14 and ApprovalCheck("Rogue", 1000) and R_Hand >= 5:
                                $ Line = "hand"
                        elif D20 > 10 and (ApprovalCheck("Rogue", 1300) or (R_Mast and ApprovalCheck("Rogue", 1000))) and R_Lust >= 70:
                                $ Line = "masturbate" 
                        elif D20 > 10 and ApprovalCheck("Rogue", 1200) and R_Lust >= 30:   
                                $ Line = "strip"
                        elif ApprovalCheck("Rogue", 700) and R_Kissed > 1:
                                $ Line = "kissing"
                        elif ApprovalCheck("Rogue", 500):        
                                $ Line = "snuggle" 
            elif Party[0] == "Kitty":
                        if D20 > 17 and ApprovalCheck("Kitty", 1000) and K_Blow > 5:
                                $ Line = "blow"
                        elif D20 > 14 and ApprovalCheck("Kitty", 1000) and K_Hand >= 5:
                                $ Line = "hand"
                        elif D20 > 10 and (ApprovalCheck("Kitty", 1300) or (K_Mast and ApprovalCheck("Kitty", 1000))) and K_Lust >= 70:
                                $ Line = "masturbate" 
                        elif D20 > 10 and ApprovalCheck("Kitty", 1200) and K_Lust >= 30:   
                                $ Line = "strip"
                        elif ApprovalCheck("Kitty", 700) and K_Kissed > 1:
                                $ Line = "kissing"
                        elif ApprovalCheck("Kitty", 500):        
                                $ Line = "snuggle" 
            elif Party[0] == "Emma":                        
                        if "classcaught" not in E_History:
                                #if you've never caught her having sex before. 
                                "Emma leans close to you for a moment, but then catches herself and pulls back."
                        elif Second and ("three" not in E_History or "taboo" not in E_History):
                                #if there's a second girl and Emma doesn't do threesomes yet
                                "Emma starts to lean close to you, but then notices [Second]."                                
                                call EmmaFace("sly",1,Eyes="side")
                                "She stops immediately and looks a bit embarrassed."
                        elif D20 > 17 and ApprovalCheck("Emma", 1000) and E_Blow > 5:
                                $ Line = "blow"
                        elif D20 > 14 and ApprovalCheck("Emma", 1000) and E_Hand >= 5:
                                $ Line = "hand"
                        elif D20 > 10 and (ApprovalCheck("Emma", 1300) or (E_Mast and ApprovalCheck("Emma", 1000))) and E_Lust >= 70:
                                $ Line = "masturbate" 
                        elif D20 > 10 and ApprovalCheck("Emma", 1200) and E_Lust >= 30:   
                                $ Line = "strip"
                        elif ApprovalCheck("Emma", 700) and E_Kissed > 1:
                                $ Line = "kissing"
                        elif ApprovalCheck("Emma", 500):        
                                $ Line = "snuggle" 
            elif Party[0] == "Laura":
                        if D20 > 16 and ApprovalCheck("Laura", 1000) and L_Blow > 1:
                                $ Line = "blow"
                        elif D20 > 13 and ApprovalCheck("Laura", 1000) and L_Hand >= 1:
                                $ Line = "hand"
                        elif D20 > 10 and (ApprovalCheck("Laura", 1300) or (L_Mast and ApprovalCheck("Laura", 1000))) and L_Lust >= 50:
                                $ Line = "masturbate" 
                        elif D20 > 10 and ApprovalCheck("Laura", 1200) and L_Lust >= 30:   
                                $ Line = "strip"
                        elif ApprovalCheck("Laura", 500): 
                                if ApprovalCheck("Laura", 700,"L"):
                                        $ Line = "snuggle" 
                                else:
                                        "Laura briefly rests against your shoulder, but then shakes herself and pulls back."
                                        $ Line = 0 
                        elif ApprovalCheck("Laura", 700) and L_Kissed > 1:
                                $ Line = "kissing"
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
                        call AnyFace(Party[0],"sly")
                        if Party[0] == "Kitty":
                                "Kitty reaches her hand through your textbook and you can feel it in your lap."
                                "She unzips you pants and pulls your dick out, stroking it slowly."
                                "She then dives her head under the book, and starts to lick it."   
                        else:
                                "[Party[0]] get predatory grin, and begins to unzip your pants."
                                "She pulls your dick out and pops it into her mouth."    
            elif Line == "hand":
                        call AnyFace(Party[0],"sly")
                        if Party[0] == "Kitty":
                                "Kitty reaches her hand through your textbook and you can feel it in your lap."
                                "She runs her finger along your erection, her hand passing through the jeans to touch your bare skin."
                                "She unzips you pants and pulls your dick out, stroking it slowly."  
                        else:
                                "[Party[0]] get predatory grin, and begins to unzip your pants."
                                "She pulls your dick out and begins to slowly stroke it."    
            elif Line == "masturbate":   
                        call AnyFace(Party[0],"sly", Eyes="side")
                        "[Party[0]] leans back a bit and starts to rub herself." 
                        $ Trigger = "masturbation"  
            elif Line == "kissing":
                        "[Party[0]] leans close to you, and leans in for a kiss."  
            elif Line == "snuggle":
                        "[Party[0]] leans close to you and you spend the rest of the study session nuzzled close."                        
                                                  
            
            if Line == "strip":
                    if "Emma" in Party and ApprovalCheck("Emma", 1200) and E_Lust >= 30:   
                            # Emma always takes priority
                            call Emma_Strip_Study_Intro              
                    elif Party[0] == "Rogue":
                            call Rogue_Strip_Study   
                    elif Party[0] == "Kitty":
                            call Kitty_Strip_Study   
                    elif Party[0] == "Laura":
                            call Laura_Strip_Study             
            elif Line and len(Party) < 2:
                    #if sex stuff is happening but only one girl
                    if Party[0] == "Rogue":
                            call Rogue_SexAct(Line) 
                    elif Party[0] == "Kitty":
                            call Kitty_SexAct(Line) 
                    elif Party[0] == "Emma":
                            call Emma_SexAct(Line) 
                    elif Party[0] == "Laura":
                            call Laura_SexAct(Line) 
            elif Line:
                    #if something sexual is happening, checks if other girl is cool
                    
                    if Line == "snuggle":
                                call Date_Sex_Break(Party[0],Second,2)
                                if _return == 3:
                                        "[Second] glowers at you a bit."  
                                        call GirlLikesGirl(Party[0],Second,700,5,1)
                                        call GirlLikesGirl(Second,Party[0],700,5,1)
                    else:
                                call Date_Sex_Break(Party[0],Second)
                                
                    if _return == 4:
                            if Line == "blow":
                                    "[Party[0]] lets your dick fall out of her mouth."
                                    "You zip your pants back up." 
                            elif Line == "hand":
                                    "[Party[0]] lets your dick drop into your lap"
                                    "You zip your pants back up." 
                            else:                                
                                    "[Party[0]] stops what she's doing."
                                    
                            call AnyFace(Party[0],"sad")
                            if Party[0] == "Rogue":
                                    ch_r "Buzzkill."
                            elif Party[0] == "Kitty":
                                    ch_k "Booo."
                            elif Party[0] == "Emma":
                                    ch_e "Oh, very well." 
                            elif Party[0] == "Laura":
                                    ch_l "Be that way."                                           
                    elif Line != "snuggle":
                        #Plays if you didn't refuse to stop
                        #either the other girl left, or it just continues with both
                        if Party[0] == "Rogue":
                                if _return == 3:
                                    #if the other girl took off. . .
                                    menu:
                                        ch_r "Mind if I continue?"
                                        "Go ahead.":
                                                ch_r "Nice."
                                        "We should stop.":
                                                ch_r "Hmph."
                                                return
                                call Rogue_SexAct(Line) 
                        elif Party[0] == "Kitty":
                                if _return == 3:
                                    #if the other girl took off. . .
                                    menu:
                                        ch_k "I can keep going?"
                                        "Go ahead.":
                                                ch_k "Cool."
                                        "We should stop.":
                                                ch_k "Lame."
                                                return
                                call Kitty_SexAct(Line) 
                        elif Party[0] == "Emma":
                                if _return == 3:
                                    #if the other girl took off. . .
                                    menu:
                                        ch_e "You don't mind if I continue?"
                                        "Go ahead.":
                                                ch_e "Lovely."
                                        "We should stop.":
                                                ch_e "Spoil sport."
                                                return
                                call Emma_SexAct(Line) 
                        elif Party[0] == "Laura":
                                if _return == 3:
                                    #if the other girl took off. . .
                                    menu:
                                        ch_l "Keep going?"
                                        "Go ahead.":
                                                ch_l "Un."
                                        "We should stop.":
                                                ch_l "Grr."
                                                return
                                call Laura_SexAct(Line)
                    if len(Party) >= 2:                        
                        call GirlLikesGirl(Party[0],Party[1],900,10,1)
                        call GirlLikesGirl(Party[1],Party[0],900,10,1)
                        #if still two girls, raise both likes by 10
            else:
                        #if nothing sexy happened. . .
                        return
                
            if "Rogue" in Party and "frisky" not in R_History:
                    $ R_History.append("frisky")
            if "Kitty" in Party and "frisky" not in K_History:
                    $ K_History.append("frisky")
            if "Emma" in Party and "frisky" not in E_History:
                    $ E_History.append("frisky")
            if "Laura" in Party and "frisky" not in L_History:
                    $ L_History.append("frisky")
                    
            "Well that was certainly a productive use of your study time. . ."    
            return
            
#end Frisky study session / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 



#start Dancing/Stripping / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 

label Group_Strip(Girl=0,Tempmod = Tempmod,Tempmod0=0,Tempmod1=0): 
    #Note, this event would break during a date, since it manipulates Adjacent. Perhaps use unique list?
    $ Adjacent = []
    if R_Loc == bg_current:
            $ Adjacent.append("Rogue")
    if K_Loc == bg_current:
            $ Adjacent.append("Kitty")
    if E_Loc == bg_current:
            $ Adjacent.append("Emma")
    if L_Loc == bg_current:
            $ Adjacent.append("Laura")
    if not Adjacent:
            "Nobody's here."
            "You dance alone."
            return    
              
    while len(Adjacent) > 2:  
            #culls out extra members
            call Remove_Girl(Adjacent[2])
#            $ Adjacent.remove(Adjacent[2])
                
    if len(Adjacent) == 2:                    
        $ renpy.random.shuffle(Adjacent)
        if Girl and Adjacent[0] != Girl:
                $ Party.reverse()  
        elif ApprovalCheck(Adjacent[0],Check=1) <= ApprovalCheck(Adjacent[1],Check=1):
                # If second one likes you more, pick her
                $ Adjacent.reverse()   
    
    call Shift_Focus(Adjacent[0])
    
    $ Round -= 5 if Round > 5 else (Round-1)
    call Set_The_Scene(1,0,0,0)
        
    call AnyFace(Adjacent[0],"sexy",1)  
    if len(Adjacent) >= 2:
            call AnyFace(Adjacent[1],"sexy",1)  
        
    if "Rogue" in Adjacent: 
        if not ApprovalCheck("Rogue", 600, TabM = 1):
                if not ApprovalCheck("Rogue", 400):
                    ch_r "I'm just some sort'a gogo dancer now?"
                elif Taboo:
                    ch_r "I don't think this is the best place for dance'n."            
                else:
                    ch_r "I dont feel it right now."                  
                $ Adjacent.remove("Rogue")
    if "Kitty" in Adjacent:    
        if not ApprovalCheck("Kitty", 600, TabM = 1):
                if not ApprovalCheck("Kitty", 400):
                    ch_k "Like I would just dance for you?"
                elif Taboo:
                    ch_k "I don't know, this really isn't a good place for it?"            
                else:
                    ch_k "I don't know, I don't really feel like dancing right now."
                $ Adjacent.remove("Kitty")
    if "Emma" in Adjacent: 
        if not ApprovalCheck("Emma", 650, TabM = 2) or (Taboo and "taboo" not in E_History):
                #she won't dance if she's in public and not cool with that
                if not ApprovalCheck("Emma", 400):
                    ch_e "Oh, you think I'll dance to your tune?"
                elif Taboo:
                    ch_e "You must be joking. Here?"            
                else:
                    ch_e "I don't really feel like dancing at the moment."          
                $ Adjacent.remove("Emma")
    if "Laura" in Adjacent: 
        if not ApprovalCheck("Laura", 600, TabM = 0):
                # Laura does not care about being in public at all. 
                if not ApprovalCheck("Laura", 400):
                    ch_l "I don't dance."     
                else:
                    ch_l "I don't feel like it."       
                $ Adjacent.remove("Laura")
            
    if not Adjacent:
            return
    
    if E_Loc == bg_current and "Emma" not in Adjacent:
            #If Emma is here, but does not agree to this,
            if "classcaught" not in E_History:
                if E_Loc == "bg emma":
                        #if it's her room. . .
                        ch_e "If the two of you would like to dance, please do it elsewhere."
                        $ Adjacent = []
                        return
                else:
                        ch_e "I should really be going." 
                        call Remove_Girl("Emma")
    
    if Adjacent[0] == "Rogue": 
        if "stripping" in R_DailyActions and ApprovalCheck(Adjacent[0], 500, TabM = 3):
            $ Line = "daily"
    elif Adjacent[0] == "Kitty": 
        if "stripping" in K_DailyActions and ApprovalCheck(Adjacent[0], 500, TabM = 3):
            $ Line = "daily"
    elif Adjacent[0] == "Emma": 
        if "stripping" in E_DailyActions and ApprovalCheck(Adjacent[0], 600, TabM = 3):
            $ Line = "daily"
    elif Adjacent[0] == "Laura": 
        if "stripping" in L_DailyActions and ApprovalCheck(Adjacent[0], 550, TabM = 3):
            $ Line = "daily"
            
    if Line == "daily":        
            $ Line = renpy.random.choice(["You liked the show earlier?",       
                "Didn't get enough earlier?",
                "You're going to wear me out."]) 
    else:
            $ Line = renpy.random.choice(["Ok, that sounds fun.",       
                "I could get into that.",
                "Yeah, ok."]) 
    call AnyLine(Adjacent[0],Line)   
    $ Line = 0
    
    call AllReset("All")
    
    if "Rogue" in Adjacent: 
            show Rogue at Rogue_Dance1()
            $ R_RecentActions.append("stripping")                      
            $ R_DailyActions.append("stripping") 
            $ R_Strip += 1 
            $ R_Action -= 1    
            $ Count = Tempmod
            if R_SeenChest or R_SeenPussy:              
                #You've seen her tits.
                $ Count += 20
            if R_SeenPanties:                           
                #You've seen her panties.
                $ Count += 5
            if "exhibitionist" in R_Traits:
                $ Count += (4*Taboo)
            if ("dating" in R_Traits or "sex friend" in R_Petnames or "Rogue" in P_Harem) and not Taboo:
                $ Count += 15
            elif "ex" in R_Traits:
                $ Count -= 40 
            elif R_ForcedCount and not R_Forced:
                $ Count -= 5 * R_ForcedCount
            if Adjacent[0] == "Rogue":
                #sets the tempmod relative to the girl in question
                $ Tempmod0 = Count
            else:
                $ Tempmod1 = Count  
    if "Kitty" in Adjacent:    
            show Kitty_Sprite at Kitty_Dance1()
            $ K_RecentActions.append("stripping")                      
            $ K_DailyActions.append("stripping") 
            $ K_Strip += 1 
            $ K_Action -= 1    
            $ Count = Tempmod
            if K_SeenChest or K_SeenPussy:             
                #You've seen her tits.
                $ Count += 20
            if K_SeenPanties:                          
                #You've seen her panties.
                $ Count += 5
            if "exhibitionist" in K_Traits:
                $ Count += (4*Taboo)
            if ("dating" in K_Traits or "sex friend" in K_Petnames or "Kitty" in P_Harem) and not Taboo:
                $ Count += 15
            elif "ex" in K_Traits:
                $ Count -= 40 
            elif K_ForcedCount and not K_Forced:
                $ Count -= 5 * K_ForcedCount
            if Adjacent[0] == "Kitty":
                #sets the tempmod relative to the girl in question
                $ Tempmod0 = Count
            else:
                $ Tempmod1 = Count                
    if "Emma" in Adjacent: 
            show Emma_Sprite at Emma_Dance1()
            #fix fill in
            $ E_RecentActions.append("stripping")                      
            $ E_DailyActions.append("stripping") 
            $ E_Strip += 1 
            $ E_Action -= 1    
            $ Count = Tempmod
            if E_SeenChest or E_SeenPussy:             
                #You've seen her tits.
                $ Count += 20
            if E_SeenPanties:                          
                #You've seen her panties.
                $ Count += 5
            if "exhibitionist" in E_Traits:
                $ Count += (4*Taboo)
            if ("dating" in E_Traits or "sex friend" in E_Petnames or "Emma" in P_Harem) and not Taboo:
                $ Count += 15
            elif "ex" in E_Traits:
                $ Count -= 40 
            elif E_ForcedCount and not E_Forced:
                $ Count -= 5 * E_ForcedCount
            if Adjacent[0] == "Emma":
                #sets the tempmod relative to the girl in question
                $ Tempmod0 = Count
            else:
                $ Tempmod1 = Count   
    if "Laura" in Adjacent: 
            show Laura_Sprite at Laura_Dance1()
            #fix fill in
            $ L_RecentActions.append("stripping")                      
            $ L_DailyActions.append("stripping") 
            $ L_Strip += 1 
            $ L_Action -= 1    
            $ Count = Tempmod
            if L_SeenChest or L_SeenPussy:             
                #You've seen her tits.
                $ Count += 20
            if L_SeenPanties:                          
                #You've seen her panties.
                $ Count += 5
            if "exhibitionist" in L_Traits:
                $ Count += (4*Taboo)
            if ("dating" in L_Traits or "sex friend" in L_Petnames or "Laura" in P_Harem) and not Taboo:
                $ Count += 15
            elif "ex" in L_Traits:
                $ Count -= 40 
            elif L_ForcedCount and not L_Forced:
                $ Count -= 5 * L_ForcedCount
            if Adjacent[0] == "Laura":
                #sets the tempmod relative to the girl in question
                $ Tempmod0 = Count
            else:
                $ Tempmod1 = Count   
            
    if len(Adjacent) >= 2:
            "They start to dance."
            $ Partner = Adjacent[1]
            $ Count2 = 1
    else:
            "She starts to dance." 
            $ Count2 = 0
            $ Partner = 0
    
    #this portion adds back in girls who dropped out, but sets their "stop" flag.
    if R_Loc == bg_current and "Rogue" not in Adjacent:
            $ Adjacent.append("Rogue")
            if "stopdancing" not in R_RecentActions:
                    $ R_RecentActions.append("stopdancing")
    if K_Loc == bg_current and "Kitty" not in Adjacent:
            $ Adjacent.append("Kitty")
            if "stopdancing" not in K_RecentActions:
                    $ K_RecentActions.append("stopdancing")
    if E_Loc == bg_current and "Emma" not in Adjacent:
            $ Adjacent.append("Emma")
            if "stopdancing" not in E_RecentActions:
                    $ E_RecentActions.append("stopdancing")
    if L_Loc == bg_current and "Laura" not in Adjacent:
            $ Adjacent.append("Laura")
            if "stopdancing" not in L_RecentActions:
                    $ L_RecentActions.append("stopdancing")
            
    
    $ Tempmod = Tempmod0
    $ Trigger = "strip"
    $ Count = 1
    
    while Count and Round >=10:
            #Loops endlessly until you do something.
            $ Round -= 2 if Round > 2 else Round
            call GirlLikesGirl(Adjacent[0],Partner,600,1,1)
            if len(Adjacent) >= 2:            
                call GirlLikesGirl(Adjacent[1],Adjacent[0],600,1,1)
            menu:
                "Continue":
                        pass
                "Would you kindly take off some clothes?":
                        #add checks here
                        call AnyLine(Adjacent[0],"Hmm?")  
                        $ Count = 0
                "Stop":
                        jump Group_Strip_End
                
    
    if E_Loc == bg_current and len(Adjacent) >= 2:
            #If Emma is here, but does not agree to this,
            if "classcaught" not in E_History or "three" not in E_History or (Taboo and "taboo" not in E_History):
                if E_Loc == "bg emma":
                        #if it's her room. . .
                        ch_e "If the two of you would like to get indecent, please do it elsewhere."
                        $ Adjacent = []
                        return
                else:
                        ch_e "I should really be going." 
                        call Remove_Girl("Emma")
    
label Group_Stripping:    
    while Round >= 10 and Adjacent: 
        $ Round -= 2 if Round > 2 else Round
        
        if Adjacent[Count] != Ch_Focus:
                call Shift_Focus(Partner)
        if Adjacent[Count] == "Rogue": 
                call R_Stripping
        elif Adjacent[Count] == "Kitty": 
                call K_Stripping
        elif Adjacent[Count] == "Emma": 
                call E_Stripping
        elif Adjacent[Count] == "Laura": 
                call L_Stripping
        
        $ Trigger = "strip"
        
        if not Adjacent:
                #If everyone leaves, quit out
                jump Group_Strip_End
                
        if len(Adjacent) >= 2:     
            call GirlLikesGirl(Adjacent[Count],Partner,800,2,1)
            call GirlLikesGirl(Adjacent[Count2],Adjacent[Count],800,2,1)
                            
        if len(Adjacent) >= 2:
                # Flips the numbers if in a group
                if Count == 0:
                    $ Count = 1
                    $ Count2 = 0
                    $ Tempmod1 = Tempmod
                    $ Tempmod = Tempmod0
                elif Count == 1:
                    $ Count = 0
                    $ Count2 = 1
                    $ Tempmod0 = Tempmod
                    $ Tempmod = Tempmod1                
                call Shift_Focus(Partner)
#                $ Partner = Adjacent[Count2]
                
                call Activity_Check(Ch_Focus,Partner)                
                                    
        if len(Adjacent) < 2:
                #Plays if only one girl
                if Count == 0:
                        $ Tempmod = Tempmod0
                else:
                        $ Tempmod = Tempmod1   
                        $ Tempmod0 = Tempmod1               
                $ Count = 0
                $ Count2 = 0
                $ Partner = 0   
                
                call Activity_Check(Ch_Focus,Partner)
            
                if "stopdancing" in R_RecentActions: 
                        jump Group_Strip_End      
                if "stopdancing" in K_RecentActions: 
                        jump Group_Strip_End                  
                if "stopdancing" in E_RecentActions: 
                        jump Group_Strip_End                  
                if "stopdancing" in L_RecentActions: 
                        jump Group_Strip_End 
        #ends loop
    if Adjacent and Round <=15:        
            call AnyLine(Adjacent[0],"It's getting late, we should probably take a break.") 
   
label Group_Strip_End:  
    #add like-ups here. . .
    if "stopdancing" in R_RecentActions:
                $ R_RecentActions.remove("stopdancing")
    if "keepdancing" in R_RecentActions:
                $ R_RecentActions.remove("keepdancing")
                
    if "stopdancing" in K_RecentActions:
                $ K_RecentActions.remove("stopdancing")
    if "keepdancing" in K_RecentActions:
                $ K_RecentActions.remove("keepdancing")
                
    if "stopdancing" in E_RecentActions:
                $ E_RecentActions.remove("stopdancing")
    if "keepdancing" in E_RecentActions:
                $ E_RecentActions.remove("keepdancing")
                
    if "stopdancing" in L_RecentActions:
                $ L_RecentActions.remove("stopdancing")
    if "keepdancing" in L_RecentActions:
                $ L_RecentActions.remove("keepdancing")
    
    call Set_The_Scene(1,0,0,0)    
    $ Count = 0
    $ Count2 = 0
#    $ renpy.pop_call()
    return
    
#end Dancing/Stripping / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 



label Girls_Caught(Girl=0,TotalCaught=0,Shame=0,Count=0,T_Pet=0):
    $ TotalCaught = R_Caught + K_Caught + E_Caught + L_Caught
    call Shift_Focus(Girl)
    call Checkout 
    call AnyLine(Girl,"!!!") 
    $ Line = Trigger
    $ Trigger = 0
    $ Trigger2 = 0
    $ Trigger3 = 0
    $ Trigger4 = 0
    $ Trigger5 = 0
    call AnyOutfit(Girl)
    if R_Loc == bg_current:         
            $ R_Loc = "bg study"
    if K_Loc == bg_current:                
            $ K_Loc = "bg study" 
    if E_Loc == bg_current:                
            $ E_Loc = "bg study" 
    if L_Loc == bg_current:     
            $ L_Loc = "bg study"     
    $ bg_current = "bg study"  
    call Set_The_Scene(0)
    show Professor at SpriteLoc(StageLeft)    
    
    if Girl == "Rogue":        
            show Rogue at SpriteLoc(StageRight) with ease
            call Rogue_OutfitShame(20)
            $ Shame = R_Shame
            $ Count = R_Caught
            $ T_Pet = R_Pet
    elif Girl == "Kitty":        
            show Kitty_Sprite at SpriteLoc(StageRight) with ease
            call Kitty_OutfitShame(20)
            $ Shame = K_Shame
            $ Count = K_Caught
            $ T_Pet = K_Pet
    elif Girl == "Emma":      
            show Emma_Sprite at SpriteLoc(StageRight) with ease
            call Emma_OutfitShame(20)
            $ Shame = E_Shame
            $ Count = E_Caught
            $ T_Pet = E_Pet
    elif Girl == "Laura":
            show Laura_Sprite at SpriteLoc(StageRight) with ease
            call Laura_OutfitShame(20)
            $ Shame = L_Shame
            $ Count = L_Caught
            $ T_Pet = L_Pet
    
    if Partner == "Rogue":         
            show Rogue at SpriteLoc(StageFarRight) with ease
    if Partner == "Kitty":         
            show Kitty_Sprite at SpriteLoc(StageFarRight) with ease
    if Partner == "Emma":         
            show Emma_Sprite at SpriteLoc(StageFarRight) with ease
    if Partner == "Laura":         
            show Laura_Sprite at SpriteLoc(StageFarRight) with ease
        
    call XavierFace("shocked")
    call AnyFace(Girl,"sad")
    if Girl == "Emma" or Partner == "Emma":        
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
            
    if Shame >= 40:
            ch_x "[Girl], my dear, you're practically naked! At least throw a towel on!"
            "He throws [Girl] the towel."
            show blackscreen onlayer black 
            if R_Loc == bg_current:      
                    $ R_Over = "towel" 
            if K_Loc == bg_current:      
                    $ K_Over = "towel" 
            if E_Loc == bg_current:      
                    $ E_Over = "towel" 
            if L_Loc == bg_current:   
                    $ L_Over = "towel"         
            hide blackscreen onlayer black
    elif Shame >= 20:
            ch_x "[Girl], my dear, that attire is positively scandalous."
    
    if Count:
            #if Caught for Girl > 0
            "And this isn't even the first time this has happened!"
    
    if Partner:
            call AnyFace(Partner,"surprised",2)
            if Partner in Rules:
                if Partner == "Kitty":
                    "Xavier glances over at Kitty, who just waggles her phone. . ."
                elif Partner == "Laura":                    
                    $ Laura_Arms = 2
                    "Xavier glances over at Laura, who raises her fist and shakes it. . ."
                    $ Laura_Arms = 1
                ch_x "And. . .hm, I could have sworn there was someone else. . ."  
            else:
                ch_x "And [Partner], you were just watching this occur!"        
            call AnyFace(Partner,"bemused",1, Eyes="side")
                
    if "rules" in Rules:
            #if the rules had been removed in a previous game
            call XavierFace("hypno")
            ch_x ". . ."
            ch_x "Hmm, I seem to be having a bit of deja vu here. . ."
            ch_x "I could swear that we've had a conversation like this before, but I cannot recall when. . ."
            call XavierFace("angry")
            ch_x "Regardless, this is a serious issue."
            $ Rules.remove("rules")
     
    if E_Loc == bg_current and "Emma" not in Rules:
        if not E_Caught:
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
                if R_Loc == bg_current and R_Caught < 5:                   
                            call Statup("Rogue", "Love", 70, 20)           
                            call Statup("Rogue", "Inbt", 50, -15)             
                            call Statup("Rogue", "Love", 90, 5)
                if K_Loc == bg_current and K_Caught < 5:                   
                            call Statup("Kitty", "Love", 70, 10)
                            call Statup("Kitty", "Inbt", 30, -25)            
                            call Statup("Kitty", "Inbt", 50, -10)  
                if E_Loc == bg_current and E_Caught < 5:                   
                            call Statup("Emma", "Love", 70, 5)
                            call Statup("Emma", "Inbt", 30, -15) 
                if L_Loc == bg_current and L_Caught < 5:                       
                            call Statup("Laura", "Inbt", 30, -20)            
                            call Statup("Laura", "Inbt", 50, -10)               
                call Statup(Girl, "Obed", 50, -5)  
                    
                call XavierFace("happy")  
                if Count:
                    ch_x "But you know you've done this before. . . at least [Count] times. . ." 
                elif Girl == "Emma" and TotalCaught:
                    ch_x "Not with Ms. Frost, perhaps, but you know you've done this before. . ."
                    ch_x "at least [TotalCaught] times. . ." 
                    call EmmaFace("sexy",Brows="confused")    
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
            
        "Just having a little fun, right [T_Pet]?":
                if Girl == "Rogue":
                        call Rogue_Namecheck
                elif Girl == "Kitty":
                        call Kitty_Namecheck
                elif Girl == "Emma":
                        call Emma_Namecheck
                elif Girl == "Laura":
                        call Laura_Namecheck
                call AnyFace(Girl,"bemused")  
                call Statup(Girl, "Lust", 90, 5)   
                if R_Loc == bg_current and R_Caught < 5:                  
                        call Statup("Rogue", "Love", 70, 20)
                        call Statup("Rogue", "Love", 90, 10)  
                if K_Loc == bg_current and K_Caught < 5:                
                        call Statup("Kitty", "Inbt", 90, 10)   
                        call Statup("Kitty", "Love", 90, 10) 
                if E_Loc == bg_current and E_Caught < 5:                   
                        call Statup("Emma", "Inbt", 90, 10)   
                        call Statup("Emma", "Love", 90, 10) 
                if L_Loc == bg_current and L_Caught < 5:               
                        call Statup("Laura", "Inbt", 90, 10)   
                        call Statup("Laura", "Obed", 90, 5)  
                        call Statup("Laura", "Love", 90, 5) 
                    
                call XavierFace("angry")
                $ Count += 10
                ch_x "If that's your attitude, harsher methods might be necessary."
                if PunishmentX:
                    ch_x "I'm extending your punishment by [Count] days."
                else:
                    ch_x "I'm halving your daily stipend for [Count] days."   
                      
                if R_Loc == bg_current and R_Caught < 5:                   
                        call Statup("Rogue", "Obed", 50, 20)
                        call Statup("Rogue", "Obed", 90, 20)
                        call Statup("Rogue", "Inbt", 30, -20)
                        call Statup("Rogue", "Inbt", 50, -10) 
                if K_Loc == bg_current and K_Caught < 5:                    
                        call Statup("Kitty", "Obed", 50, 20)
                        call Statup("Kitty", "Obed", 90, 20)
                        call Statup("Kitty", "Inbt", 30, -20)  
                if E_Loc == bg_current and E_Caught < 5:                    
                        call Statup("Emma", "Obed", 50, 20)
                        call Statup("Emma", "Obed", 90, 20)
                        call Statup("Emma", "Inbt", 30, -20)   
                if L_Loc == bg_current and L_Caught < 5:               
                        call Statup("Laura", "Obed", 50, 20)
                        call Statup("Laura", "Obed", 90, 20)
                        call Statup("Laura", "Inbt", 30, -20) 
                            
                ch_x "I've had enough of you, begone."
        #End "Little fun"
        
        "Just this. . . Plan Omega, Rogue." if Girl == "Rogue" and P_Lvl >= 5:
                $ Line = "Omega"            
        "Just this. . . Plan Kappa, Kitty!" if Girl == "Kitty" and P_Lvl >= 5:
                $ Line = "Kappa"                    
        "Just this. . . Plan Psi, Emma!" if Girl == "Emma" and P_Lvl >= 5:
                $ Line = "Psi"            
        "Just this. . . Plan Chi, Laura!" if Girl == "Laura" and P_Lvl >= 5:
                $ Line = "Chi"
        #End "Plan X"
                        
                        
        "You can suck it, old man.":
                call LauraFace("surprised")
                call Statup(Girl, "Lust", 90, 10)                
                if R_Loc == bg_current and R_Caught < 5:                   
                        call Statup("Rogue", "Obed", 50, 20)
                        call Statup("Rogue", "Obed", 90, 40)  
                if K_Loc == bg_current and K_Caught < 5:                   
                        call Statup("Kitty", "Obed", 50, 25)
                        call Statup("Kitty", "Obed", 90, 40) 
                if E_Loc == bg_current and E_Caught < 5:        
                        call Statup("Emma", "Love", 90, 5) 
                        call Statup("Emma", "Obed", 50, 20)
                        call Statup("Emma", "Obed", 90, 30)  
                if L_Loc == bg_current and L_Caught < 5:       
                        call Statup("Emma", "Love", 90, 5)           
                        call Statup("Laura", "Obed", 50, 25)
                        call Statup("Laura", "Obed", 90, 30) 
                                            
                call XavierFace("angry")
                $ Count += 20
                ch_x "If that's your attitude, harsher methods might be necessary."
                if PunishmentX:
                    ch_x "I'm extending your punishment by [Count] days!"
                else:
                    ch_x "I'm halving your daily stipend for [Count] days!" 
                    
                if R_Loc == bg_current and R_Caught < 5:        
                        if R_Inbt > 500:
                            call Statup("Rogue", "Inbt", 90, 15)             
                        call Statup("Rogue", "Inbt", 30, -20)
                        call Statup("Rogue", "Inbt", 50, -10)   
                if K_Loc == bg_current and K_Caught < 5:                  
                        if K_Inbt > 500:
                            call Statup("Kitty", "Inbt", 90, 15)             
                        call Statup("Kitty", "Inbt", 30, -20)
                        call Statup("Kitty", "Inbt", 50, -10)   
                if E_Loc == bg_current and E_Caught < 5:                    
                        if E_Inbt > 500:
                            call Statup("Emma", "Inbt", 90, 15)             
                        call Statup("Emma", "Inbt", 30, -20)
                        call Statup("Emma", "Inbt", 50, -10)  
                if L_Loc == bg_current and L_Caught < 5:       
                        if L_Inbt > 500:
                            call Statup("Laura", "Inbt", 90, 15)             
                        call Statup("Laura", "Inbt", 30, -15)
                        call Statup("Laura", "Inbt", 50, -10) 
                            
                ch_x "Now get out of my sight."
        #End "suck it"
    
    if Line:
            if Line == "Omega":
                    if ApprovalCheck("Rogue", 1500, TabM=1, Loc="No"):                   
                            jump Xavier_Plan #Plan_Omega
                    elif ApprovalCheck("Rogue", 1000, TabM=1, Loc="No"):
                            call RogueFace("perplexed") 
                            $ R_Brows = "sad"
                            ch_r "I'm not comfortable with something that extreme, [R_Petname]. . ."
                            menu:
                                "Dammit Rogue. . .":
                                        call RogueFace("angry")
                                        call Statup("Rogue", "Obed", 50, 5)
                                        call Statup("Rogue", "Love", 90, -5) 
                                "Yeah, I guess you're right. . .":
                                        call RogueFace("bemused") 
                    else:
                            call RogueFace("confused") 
                            ch_r "What nonsense are you talking now?"
                            ch_p "Plan {i}Omega!{/i} . . you know. . ."
                            ch_r "Sounds like gibberish."
                            ch_p "Oh, yeah, I guess I haven't mentioned that. . ."
                            call RogueFace("bemused") 
                    #End "Plan Omega"
            if Line == "Kappa":
                    if "Xavier's photo" in P_Inventory and ApprovalCheck("Kitty", 1500, TabM=1, Loc="No"):                   
                            jump Xavier_Plan #Plan_Kappa
                    elif ApprovalCheck("Kitty", 1000, TabM=1, Loc="No"):
                            call KittyFace("perplexed") 
                            $ K_Brows = "sad"
                            if "Xavier's photo" in P_Inventory:
                                    ch_k "You know. . . I really don't think that's a good idea. . ."
                            else:
                                    ch_k "We don't really have any way to pull that off atm. . ."                                
                            menu:
                                "Dammit Kitty. . .":
                                        call KittyFace("angry")
                                        call Statup("Kitty", "Obed", 50, 5)
                                        call Statup("Kitty", "Love", 90, -5) 
                                "Yeah, I guess you're right. . .":
                                        call KittyFace("bemused") 
                                        call Statup("Kitty", "Love", 90, 5) 
                    else:
                            call KittyFace("confused") 
                            ch_k "Wait, Plan what??"
                            ch_p "Plan {i}Kappa!{/i} . . you know. . ."
                            ch_k "I have no {i}idea{/i} what you're talking about."
                            ch_p "oh, yeah, I guess I haven't mentioned that. . ."
                            call KittyFace("bemused") 
                    #End "Plan Kappa"
            elif Line == "Psi":
                    if ApprovalCheck("Emma", 1500, TabM=1, Loc="No"):                   
                            jump Xavier_Plan #Plan_Psi
                    elif ApprovalCheck("Emma", 1000, TabM=1, Loc="No"):
                            call EmmaFace("perplexed") 
                            $ E_Brows = "sad"
                            ch_e "Um, I don't believe we're quite at that point yet, [E_Petname]. . ."
                            menu:
                                "Dammit Emma. . .":
                                        call EmmaFace("angry")
                                        call Statup("Emma", "Obed", 50, 5)
                                        call Statup("Emma", "Love", 90, -5) 
                                "Yeah, I guess you're right. . .":
                                        call EmmaFace("bemused") 
                    else:
                            call EmmaFace("confused") 
                            ch_e "Lord child, what are you talking about now?"
                            ch_p "Plan {i}Psi!{/i} . . you know. . ."
                            ch_e "I wish that I did."
                            ch_p "Oh, yeah, I guess I haven't mentioned that. . ."
                            call EmmaFace("bemused") 
                    #End "Plan Psi"
            elif Line == "Chi":        
                    if L_Lvl >= 5 and ApprovalCheck("Laura", 1500, TabM=1, Loc="No") and ApprovalCheck("Laura", 750, "I"):                   
                            jump Xavier_Plan #Plan_Chi
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
                    #End "Plan Chi"
             
            # if the plan falls through. . .
            call XavierFace("angry")
            $ Count += 10
            ch_x "I have no idea what that was about, but it sounds like you haven't learned."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."    
                
                if R_Loc == bg_current and R_Caught < 5:                 
                        call Statup("Rogue", "Obed", 50, 10)
                        call Statup("Rogue", "Obed", 90, 10)
                        call Statup("Rogue", "Inbt", 30, -10)
                        call Statup("Rogue", "Inbt", 50, -5)    
                if K_Loc == bg_current and K_Caught < 5:                 
                        call Statup("Kitty", "Obed", 50, 10)
                        call Statup("Kitty", "Obed", 90, 10)
                        call Statup("Kitty", "Inbt", 30, -10)
                        call Statup("Kitty", "Inbt", 50, -5)    
                if E_Loc == bg_current and E_Caught < 5:                   
                        call Statup("Emma", "Obed", 50, 10)
                        call Statup("Emma", "Inbt", 50, -5) 
                if L_Loc == bg_current and L_Caught < 5:  
                        call Statup("Laura", "Obed", 50, 10)
                        call Statup("Laura", "Obed", 90, 10)
                        call Statup("Laura", "Inbt", 30, -10)
                        call Statup("Laura", "Inbt", 50, -5)   
            ch_x "I've had enough of you, begone."
    #End "evil plans"            
                
    if Girl == "Kitty" and "Kitty" not in Rules and "Xavier's photo" not in P_Inventory:
            "It would probably be a good idea to find some way to get Xavier to leave you alone."
            "There probably isn't a way available right now though. . ."
            if K_Caught > 1: 
                "Maybe I should try searching the office when he's not around."
            if K_Caught > 2:
                "I bet Kitty could help me get in."
            if K_Caught > 3:
                "I bet there's something in that lefthand drawer. . ."
    elif Girl == "Emma":        
            ch_x "Emma, I'd like you to stay after for a brief discussion about \"boundaries\". . ."
            if E_Caught:
                    call Statup("Emma", "Love", 90, -5) 
                    call EmmaFace("angry",Eyes="closed")
                    ch_e "Not again. . ."
                
    $ PunishmentX += Count     
    if Girl == "Rogue":  
            $ R_Caught += 1
            $ R_RecentActions.append("caught")
            $ R_DailyActions.append("caught") 
    elif Girl == "Kitty":  
            $ K_Caught += 1
            $ K_RecentActions.append("caught")
            $ K_DailyActions.append("caught") 
    elif Girl == "Emma":  
            $ E_Caught += 1
            $ E_RecentActions.append("caught")
            $ E_DailyActions.append("caught") 
    elif Girl == "Laura":  
            $ L_Caught += 1
            $ L_RecentActions.append("caught")
            $ L_DailyActions.append("caught") 
    call Remove_Girl("All")  
    "You return to your room"
    hide Professor
    jump Player_Room
#End Caught / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Xavier_Plan:
    call AnyFace(Girl,"sly")         
    "As you say this, a sly grin crosses [Girl]'s face."
    "You quickly approach Xavier and place your hands on his head."
    call XavierFace("psychic")
    ch_x ". . ."
    call XavierFace("shocked")
    "Xavier realizes with a shock that with your powers, his telepathy is useless."   
    if Girl == "Rogue":
            show Rogue at SpriteLoc(StageLeft+100,85) zorder 24 with ease
            "Rogue moves in and also grabs his head, duplicating his powers as he watches helplessly."
            "Now that she posesses his full power, while his are negated, he has no defenses."
    elif Girl == "Kitty":  
            $ Kitty_Arms = 2
            show Kitty_Sprite at SpriteLoc(StageLeft+100,150) with ease
            $ K_SpriteLoc = StageCenter
            "Kitty moves in sits on his lap, pinning his arms to the chair."
    elif Girl == "Emma":    
            show Emma_Sprite at SpriteLoc(StageLeft+100,85) zorder 24 with ease
            $ E_SpriteLoc = StageCenter
            "Emma moves behind Xavier and activates her own telepathy."    
    elif Girl == "Laura":
            show Laura_Sprite at SpriteLoc(StageLeft+100,150) with ease
            $ L_SpriteLoc = StageCenter
            "Laura moves in sits on his lap, placing one hand on his."
    
    
    if Partner:
            if Partner == "Rogue" and "Omega" not in P_Traits:        
                    $ Line = "first"
            elif Partner == "Kitty" and "Kappa" not in P_Traits:        
                    $ Line = "first"
            elif Partner == "Emma" and "Psi" not in P_Traits:          
                    $ Line = "first"
            elif Partner == "Laura" and "Chi" not in P_Traits:           
                    $ Line = "first"
            
            if Line == "first":
                #if the Partner has never done this. . .
                if ApprovalCheck(Partner, 1000):
                        #if she's cool with it.
                        call AnyFace(Partner,"surprised")      
                        "[Partner] looks a bit caught off guard, but goes along with the idea."        
                        call AnyFace(Partner,"sly")
                else:
                        call AnyFace(Partner,"surprised")      
                        "[Partner] looks a bit uncomfortable with what's happening and takes off." 
                        call Remove_Girl(Partner)
                    
            else:
                        call AnyFace(Partner,"sly")      
                        "[Partner] understands what's going on here."     
    #end partner response
            
    call XavierFace("angry")    
    if Girl == "Rogue":
            $ R_Arms = 0
            $ Rogue_Arms = 2
            show Rogue at SpriteLoc(StageLeft+100,85) zorder 24 with ease
            "Rogue moves in and also grabs his head, duplicating his powers as he watches helplessly."
            "Now that she posesses his full power, while his are negated, he has no defenses."              
            call XavierFace("hypno")                
            if "Omega" in P_Traits:
                    ch_x "Oh, not again."
                    ch_x "What is it you want this time?"  
                    call Statup("Rogue", "Obed", 80, 3)
                    call Statup("Rogue", "Inbt", 70, 1)
            else:
                    call Statup("Rogue", "Obed", 50, 40)
                    call Statup("Rogue", "Inbt", 70, 20) 
            ch_r "Well, [R_Petname], what would you like to do with this opportunity?"
            ch_r "I think we'll only get three tries at this. . ."
    elif Girl == "Kitty": 
            $ Kitty_Arms = 2
            show Kitty_Sprite at SpriteLoc(StageLeft+100,150) with ease
            $ K_SpriteLoc = StageCenter
            "Kitty moves in sits on his lap, pinning his arms to the chair."     
            if "Kappa" in P_Traits:
                    ch_x "Oh, not again."
                    ch_x "What is it you want this time?"
                    call Statup("Kitty", "Obed", 80, 3)
                    call Statup("Kitty", "Inbt", 70, 1)  
            else:
                    ch_x "What is the meaning of this? Unhand me!"
                    "You pull out the photo you found earlier in his study."
                    call Statup("Kitty", "Obed", 50, 40)
                    call Statup("Kitty", "Inbt", 70, 30)
                    ch_p "I have here a rather. . . compromising photo of you and Mystique."
                    ch_p "I was thinking maybe you could cut me a little slack around here."
                    ch_x "And if I do not?"
                    ch_p "Kitty here's set it to distribute to every computer in school, every day."
                    ch_p "And only I know the password." 
                    ch_x "Very well. . . I'll forget about your punishment."
                    ch_p "Oh, I think we can do a bit better than that. . ." 
                    call Statup("Kitty", "Obed", 200, 30)
                    call Statup("Kitty", "Inbt", 200, 10)  
            ch_k "Well, [K_Petname], what should we ask for?"
    elif Girl == "Emma":    
            show Emma_Sprite at SpriteLoc(StageLeft+100,85) zorder 24 with ease
            "Emma moves behind Xavier and activates her own telepathy."
            call XavierFace("angry")
            if "Psi" in P_Traits:
                    ch_x "Oh, not again. . ."
                    call Statup("Emma", "Obed", 80, 3)
                    call Statup("Emma", "Inbt", 80, 1)  
            else:
                    call Statup("Emma", "Obed", 50, 40)
                    call Statup("Emma", "Inbt", 70, 30)
                    call Statup("Emma", "Obed", 200, 30)
                    call Statup("Emma", "Inbt", 200, 10)  
            ch_e "Well, [E_Petname], what should we ask for?" 
    elif Girl == "Laura":
            $ Laura_Arms = 2
            if "Chi" in P_Traits:
                    ch_x "Oh, not again."
                    $ L_Claws = 1
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
            ch_l "Well, [L_Petname], what should we ask for?"
            
    $ Count = 3
    $ PunishmentX = 0
    while Count:
        $ Count -= 1
        menu:
            ch_x "What do you want?"
            "Don't bother us anymore when we're having fun." if Girl not in Rules:
                    ch_x "Very well. . . I could offer you some. . . discretion. . ."
                    $ Rules.append(Girl)
            "You know, it's kinda fun dodging you, catch us if you can." if Girl in Rules:
                    ch_x "If you. . . want me to, I suppose. . ."
                    $ Rules.remove(Girl)
                    
            "Raise my stipend." if P_Income < 30:
                    if Girl == "Rogue" and "Omega" not in P_Traits:    
                            ch_x "Very well. . . but I can only raise it by so much. . ."        
                            $ P_Income += 2
                    elif Girl == "Kitty" and "Kappa" not in P_Traits:    
                            ch_x "Very well. . . but I can only raise it by so much. . ."        
                            $ P_Income += 2
                    elif Girl == "Emma" and "Psi" not in P_Traits:    
                            ch_x "Very well. . . but I can only raise it by so much. . ."        
                            $ P_Income += 2
                    elif Girl == "Laura" and "Chi" not in P_Traits:    
                            ch_x "Very well. . . but I can only raise it by so much. . ."        
                            $ P_Income += 2
                    else:                
                            ch_x "I'm afraid I can't manage any more than I have. . ."
                            $ Count += 1
            "Raise my stipend. [[Used](locked)" if P_Income >= 30:           
                    pass
                    
            "In was interested in a key. . . ":
                menu:
                    "Give me the key to your study." if "Xavier" not in Keys:  
                            ch_x "Fine, take it. . ."  
                            $ Keys.append("Xavier")
                    "Give me the key to your study.[[Owned] (locked)" if "Xavier" in Keys:  
                            pass
                            
                    "Give me the key to [Girl]'s room." if Girl not in Keys:  
                            ch_x "I. . . suppose I could do that. . ."  
                            $ Keys.append(Girl)
                    "Give me the key to [Girl]'s room.[[Owned] (locked)" if Girl in Keys:  
                            pass
                    
                    "Never mind the keys.":
                            $ Count += 1
            "That should do it.":
                $ Count = 0
                
    ch_x "Very well, that should conclude our business. Please leave." 
    if Girl == "Rogue":
            if "Omega" not in P_Traits: 
                    call Statup("Rogue", "Lust", 90, 10)
                    call Statup("Rogue", "Love", 70, 30)
                    call Statup("Rogue", "Love", 200, 20)
                    $ P_Traits.append("Omega")  
            ch_p "Ok, that's enough. Make Xavier forget that any of this happened, and then let's get out of here." 
            $ R_Arms = "gloved"
            $ Rogue_Arms = 1
    elif Girl == "Kitty":
            if "Kappa" not in P_Traits:
                    call Statup("Kitty", "Lust", 90, 10)
                    call Statup("Kitty", "Inbt", 80, 10)
                    call Statup("Kitty", "Love", 70, 10)
                    call Statup("Kitty", "Love", 200, 20)
                    $ P_Traits.append("Kappa")
            $ Kitty_Arms = 0
    elif Girl == "Emma":
            ch_p "Ok, that's enough. Make Xavier forget that any of this happened, and then let's get out of here." 
            if "Psi" not in P_Traits:
                    call Statup("Emma", "Lust", 90, 10)
                    call Statup("Emma", "Inbt", 80, 10)
                    call Statup("Emma", "Love", 70, 10)
                    call Statup("Emma", "Love", 200, 20)
                    $ P_Traits.append("Psi")
    elif Girl == "Laura":
            if "Chi" not in P_Traits:
                    call Statup("Laura", "Lust", 90, 10)
                    call Statup("Laura", "Inbt", 80, 10)
                    call Statup("Laura", "Love", 70, 10)
                    call Statup("Laura", "Love", 200, 20)
                    $ P_Traits.append("Chi")
            $ Laura_Arms = 1
            $ L_Claws = 0
        
    call Remove_Girl("All")  
    "You return to your room"
    hide Professor
    jump Player_Room
                              
# end Caught / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Clean-up  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 


label Partner_Clean:
        #This is called when you ask for a Partner to clean you instead
        if not Partner:
            return
            
        call Shift_Focus(Partner) #makes the partner the lead and the lead the partner
        call AllReset(Partner)  #resets the position of the original lead
        if Ch_Focus == "Rogue":
                call R_CleanCock        
        elif Ch_Focus == "Kitty":
                call K_CleanCock
        elif Ch_Focus == "Emma":
                call E_CleanCock
        elif Ch_Focus == "Laura":
                call L_CleanCock    
            
        call Shift_Focus(Partner) #makes the original lead the lead again
        call AllReset(Partner)  #resets the position of the original partner
        "[Partner] Steps back."
        
        return
        
# Start Self Clean-Up / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Self_Cleanup(Girl=0,TempSpunk=0):
    if Girl == "Rogue":
        $ TempSpunk = R_Spunk
    elif Girl == "Kitty":
        $ TempSpunk = K_Spunk
    elif Girl == "Emma":
        $ TempSpunk = E_Spunk
    elif Girl == "Laura":
        $ TempSpunk = L_Spunk
        
    $ Cnt = 0  
            
    if TempSpunk and Choice != "eat":
            $ TempSpunk.append("hand")
    if "mouth" in TempSpunk and Choice != "eat":
            $ TempSpunk.remove("mouth")
            "[Girl] spits out the spunk in her mouth and it dribbles down her chin,"
            $ Cnt += 1
            if "chin" not in TempSpunk:
                $ TempSpunk.append("chin")
    if "chin" in TempSpunk:
            $ TempSpunk.remove("chin")
            if Cnt:            
                "then she wipes the spunk off her chin,"
            else:
                "[Girl] wipes the spunk off her chin,"
            $ Cnt += 1
    if "hair" in TempSpunk:
            $ TempSpunk.remove("hair")
            if Cnt:            
                "then she wipes the spunk out of her hair,"
            else:
                "[Girl] wipes the spunk out of her hair,"
            $ Cnt += 1
    if "facial" in TempSpunk:
            $ TempSpunk.remove("facial")
            if Cnt:
                "then she wipes the spunk off of her face,"   
            else:
                "[Girl] wipes the spunk off of her face,"   
            $ Cnt += 1         
    if "tits" in TempSpunk:
            $ TempSpunk.remove("tits")
            call Statup("Player", "Focus",80,2)
            if Cnt:
                "then she wipes the spunk off of her chest,"   
            else:
                "[Girl] wipes the spunk off of her chest," 
            $ Cnt += 1           
    if "belly" in TempSpunk:
            $ TempSpunk.remove("belly")
            if Cnt:
                "then she wipes the spunk off of her belly,"   
            else:
                "[Girl] wipes the spunk off her belly," 
            $ Cnt += 1          
    if "back" in TempSpunk:
            $ TempSpunk.remove("back")
            if Cnt:
                "then she wipes the spunk off of her lower back,"   
            else:
                "[Girl] wipes the spunk off her lower back," 
            $ Cnt += 1      
    if "in" in TempSpunk:
            $ TempSpunk.remove("in")
            call Statup("Player", "Focus",80,3)
            if Cnt:
                "then she wipes the spunk inside her pussy,"   
            else:
                "[Girl] wipes the spunk inside her pussy,"     
            $ Cnt += 1 
    if "anal" in TempSpunk and (ApprovalCheck(Girl, 800, "I") or Choice != "eat"):
            while "anal" in TempSpunk:
                $ TempSpunk.remove("anal")
            call Statup("Player", "Focus",80,2)
            if Cnt:
                "then she wipes the spunk dripping out of her ass,"   
            else:
                "[Girl] wipes the spunk dripping our of her ass,"
            $ Cnt += 1            
    if "hand" in TempSpunk:
            $ TempSpunk.remove("hand")
            if Choice == "eat":        
                    $ TempSpunk.append("mouth")  
                    call Statup("Player", "Focus",80,3)
                    if Cnt and "anal" in TempSpunk:
                        "then licks her hands off with a satisfied grin," 
                    if Cnt:
                        "and finally she licks her hands off with a satisfied grin." 
                    else:
                        "[Girl] licks her hands off with a satisfied grin."   
                        
                    call Statup(Girl, "Inbt", 80, 2) 
                    $ TempSpunk.remove("mouth")                    
                    if Girl == "Rogue":
                            $ R_Swallow += 1     
                            $ R_Addict -= (10*Cnt)
                            if R_Swallow == 1:
                                $ R_SEXP += 12
                            $ R_RecentActions.append("swallowed")
                            $ R_DailyActions.append("swallowed") 
                    elif Girl == "Kitty":
                            $ K_Swallow += 1     
                            $ K_Addict -= (10*Cnt)
                            if K_Swallow == 1:
                                $ K_SEXP += 12
                            $ K_RecentActions.append("swallowed")
                            $ K_DailyActions.append("swallowed") 
                    elif Girl == "Emma":
                            $ E_Swallow += 1     
                            $ E_Addict -= (10*Cnt)
                            if E_Swallow == 1:
                                $ E_SEXP += 12
                            $ E_RecentActions.append("swallowed")                     
                            $ E_DailyActions.append("swallowed") 
                    elif Girl == "Laura":
                            $ L_Swallow += 1     
                            $ L_Addict -= (10*Cnt)
                            if L_Swallow == 1:
                                $ L_SEXP += 12
                            $ L_RecentActions.append("swallowed")                     
                            $ L_DailyActions.append("swallowed") 
            #end hand if swallowing  
            else:
                    if Cnt:
                        "and finally, she wipes her hands off with a nearby tissue." 
                    else:
                        "[Girl] wipes her hands off with a nearby tissue."                    
            $ Cnt += 1
            #end hand
    if "anal" in TempSpunk:
            $ TempSpunk.remove("anal")
            if Cnt:
                "Afterward, she wipes the spunk dripping our of her ass."
            else:
                "[Girl] wipes the spunk dripping out of her ass."
                
    if Girl == "Rogue":
            $ R_Wet = 0        
            $ del R_Spunk[:]   
            if Cnt >= 5:
                    $ R_Eyes = "surprised"
                    ch_r "Wow, you really painted me white!"
                    $ R_Eyes = "sexy"
            elif Cnt >=3:
                    ch_r "That was a real mess you left me to clean up."
            elif Choice == "eat" and R_Swallow >= 5:
                    ch_r "That was delcious."
    elif Girl == "Kitty":
            $ K_Wet = 0        
            $ del K_Spunk[:]   
            if Cnt >= 5:
                    $ K_Eyes = "surprised"
                    ch_k "Wow, you really drenched me!"
                    $ K_Eyes = "sexy"
            elif Cnt >=3:
                    ch_k "Well that was a fine mess you got me into."
            elif Choice == "eat" and K_Swallow >= 5:
                    ch_k "Yum."
    elif Girl == "Emma":
            $ E_Wet = 0        
            $ del E_Spunk[:]   
            if Cnt >= 5:
                    $ E_Eyes = "surprised"
                    ch_e "I really was the \"white queen\" there."
                    $ E_Eyes = "sexy"
            elif Cnt >=3:
                    ch_e "Well that was a lot of work."
            elif Choice == "eat" and E_Swallow >= 5:
                    ch_e "Mmmm, now I'm hungry for more."
    elif Girl == "Laura":
            $ L_Wet = 0        
            $ del L_Spunk[:]   
            if Cnt >= 5:
                    $ L_Eyes = "surprised"
                    ch_l "There was a lot more to that than I'd noticed. . ."
                    $ L_Eyes = "sexy"
            elif Cnt >=3:
                    ch_l "You made a real mess there."
            elif Choice == "eat" and L_Swallow >= 5:
                    ch_l "Mmmm, got any more?"
    
    return    
    
# End Self Clean-Up / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Partner_Cleanup_Check(Girl=0,B=0):
        #girl is the lead
        #resets to "random" if she refuses        
        if Choice == "partner lick":
                if Partner in P_Harem and Girl in P_Harem:                 
                        $ B = 0  
                elif Girl == "Rogue" and "poly " + Partner in R_Traits:                    
                        $ B = 0  
                elif Girl == "Kitty" and "poly " + Partner in K_Traits:                    
                        $ B = 0  
                elif Girl == "Emma" and "poly " + Partner in E_Traits:                    
                        $ B = 0  
                elif Girl == "Laura" and "poly " + Partner in L_Traits:                    
                        $ B = 0  
                else:
                        $ B = -100
        else:
                $ B = 0                      
        
        if not ApprovalCheck(Partner, 1400, Bonus=3*B) or GirlLikeCheck(Partner,Girl) < (500-2*B):
                #if she's not super obedient or doesn't like the other girl
                call AnyFace(Partner,"sly") 
                call Statup(Partner, "Obed", 50, -3)
                call Statup(Partner, "Inbt", 70, 10) 
                call Statup(Partner, "Inbt", 200, 5) 
                call Statup(Partner, "Lust", 60, 5) 
                call Partner_CGLine(2) #"You want me ta clean up your mess?"
                menu:
                    extend ""
                    "Fine, never mind.":
                            call AnyFace(Partner,"smile") 
                            call Statup(Partner, "Love", 70, 5)
                            call Statup(Partner, "Obed", 50, 3)
                            $ Choice = "random" 
                    "Yeah, go ahead.": 
                        if ApprovalCheck(Partner, 600,"O", Bonus=3*B):
                            # She's obedient. . .
                            call AnyFace(Partner,"sad") 
                            call Statup(Partner, "Obed", 50, 10)
                            call Partner_CGLine(3) #"If you say so."
                        elif GirlLikeCheck(Partner,Girl) >= 800:
                            # She likes the other girl. . .
                            call AnyFace(Partner,"sly") 
                            call Statup(Partner, "Love", 70, -3)
                            call Statup(Partner, "Obed", 50, 3)
                            call Partner_CGLine(4) #"I guess I don't mind if she doesn't."
                        elif ApprovalCheck(Partner, 1200, Bonus=3*B):
                            # She's likes you enough to listen. . .
                            call AnyFace(Partner,"normal") 
                            call Statup(Partner, "Love", 70, -3)
                            call Statup(Partner, "Obed", 50, 3)
                            call Partner_CGLine(5) #"I guess I could. . ."
                        elif Choice == "partner lick" and ApprovalCheck(Partner, 1200) and GirlLikeCheck(Partner,Girl) >= 600:
                            # She's likes you enough to wipe, but not lick. . .
                            call AnyFace(Partner,"normal") 
                            call Statup(Partner, "Love", 70, -3)
                            call Statup(Partner, "Obed", 50, 3)
                            call Partner_CGLine(6)  #"I can wipe her off, I guess, but that's it. . ."
                            $ Choice = "partner wipe"
                        else:
                            # She's obedient. . .
                            call Statup(Partner, "Love", 70, -5)
                            call Statup(Partner, "Obed", 50, -5)
                            call GirlLikesGirl(Girl,Partner,900,-2,1)
                            call Partner_CGLine(7)  #"No way."
                            $ Choice = "random"                                                                             
        else:           # She just agrees. . .
                            call RogueFace("bemused") 
                            $ Choice = "partner wipe"  
                            call GirlLikesGirl(Girl,Partner,900,3,1)
                            call Partner_CGLine(1) #"I'd better get to work, I guess."
        #end Partner wipe off partner check
        
        
        if Choice != "random":       
            call Statup(Girl, "Lust", 60, 5)
            if not ApprovalCheck(Girl, 1400, Bonus=3*B) or GirlLikeCheck(Girl,Partner) < (500-2*B):
                #if Rogue doesn't like the other girl or isn't super obedient                  
                if GirlLikeCheck(Girl,Partner) >= 800:
                        call Statup(Girl, "Inbt", 90, 5) 
                        call GirlLikesGirl(Partner,Girl,900,5,1)
                        call Partner_CGLine(8,Girl)   #"I'll allow it, since she seems so excited by it. . ."     
                elif ApprovalCheck(Girl, 1200, Bonus=3*B):
                        call Statup(Girl, "Obed", 50, 3)
                        call Statup(Girl, "Obed", 80, 2)
                        call Statup(Girl, "Inbt", 70, 3) 
                        call Partner_CGLine(9,Girl)    #"If that's what turns you on. . ."    
                elif ApprovalCheck(Girl, 1000, Bonus=3*B) and GirlLikeCheck(Girl,Partner) >= (600-B):
                        call Statup(Girl, "Love", 70, 1)
                        call Statup(Girl, "Obed", 50, 3)
                        call Statup(Girl, "Obed", 80, 3)
                        call Statup(Girl, "Inbt", 70, 5) 
                        call GirlLikesGirl(Partner,Girl,900,3,1)
                        call Partner_CGLine(10,Girl) #"Kinda ganging up on me here. . ."
                else:
                        call Statup(Girl, "Obed", 70, -3)
                        call Statup(Girl, "Inbt", 70, 2) 
                        call Partner_CGLine(11,Girl)   # "Kinda gross, no."
                        $ Choice = "random"
            else:
                        call Statup(Girl, "Obed", 50, 3)
                        call Statup(Girl, "Inbt", 70, 3) 
                        call Partner_CGLine(12,Girl) #"Oh, very well. . ."
                        
        if Choice != "random":
                #calls the partner clean-up if that option is chosen
                call Les_Launch(Girl)  
                
                call Partner_Clean_Girl(Girl)
                
                if Girl == "Rogue" and R_Swallow >=5:                            
                        $ Options.append("eat")  
                elif Girl == "Kitty" and K_Swallow >=5:                            
                        $ Options.append("eat")  
                elif Girl == "Emma" and E_Swallow >=5:                            
                        $ Options.append("eat")  
                elif Girl == "Laura" and L_Swallow >=5:                            
                        $ Options.append("eat")                     
                call AllReset(Partner)
                call AllReset(Ch_Focus)
                if Choice == "partner lick":
                        call GirlLikesGirl(Girl,Partner,900,10,1)
                        call Partner_CGLine(13,Girl) #"Well that was a treat. . ."
                else:
                        call GirlLikesGirl(Girl,Partner,900,3,1)
                        call Partner_CGLine(14,Girl)   #"That was easy."                     
        #end Partner wipe off
        return
        
label Partner_CGLine(LineNum=1,Girl=0):
        #call Partner_CGLine(4)
        if not Partner or not LineNum:
            return
        if LineNum == 1:
                # She just agrees. . .
                if Partner == "Rogue":
                    ch_r "Sure, why not?"
                elif Partner == "Kitty":
                    ch_k "You[K_like]really did a job on her."
                    ch_k "I'll get on it."
                elif Partner == "Emma":
                    ch_e "I suppose it wouldn't be so bad."
                elif Partner == "Laura":
                    ch_l "I'd better get to work, I guess."
        elif LineNum == 2:
                # She questions whether she should. . .
                if Partner == "Rogue":
                    ch_r "You want me ta clean up your mess?"
                elif Partner == "Kitty":
                    ch_k "You[K_like]really did a job on her."
                    ch_k "I'm supposed to deal with that?"
                elif Partner == "Emma":
                    ch_e "You expect me to stoop to clean-up duty?"
                elif Partner == "Laura":
                    ch_l "Real mess you left me there."
        elif LineNum == 3:
                # She's obedient. . .
                if Partner == "Rogue":
                    ch_r "If you say so."
                elif Partner == "Kitty":
                    ch_k "Whatever."
                elif Partner == "Emma":
                    ch_e "Lovely."
                elif Partner == "Laura":
                    ch_l "On it."
        elif LineNum == 4:
                # She likes the other girl. . .
                if Partner == "Rogue":
                    ch_r "Well, if she doesn't mind. . ."
                elif Partner == "Kitty":
                    ch_k "I guess I don't mind if she doesn't."
                elif Partner == "Emma":
                    ch_e "Very well, come over here, dear."
                elif Partner == "Laura":
                    ch_l "She is a bit messy. . ."
        elif LineNum == 5:
                # She's likes you enough to listen. . .
                if Partner == "Rogue":
                    ch_r "I s'pose so. . ."
                elif Partner == "Kitty":
                    ch_k "I guess I could. . ."
                elif Partner == "Emma":
                    ch_e "I suppose she'd do the same for me."
                elif Partner == "Laura":
                    ch_l "I guess someone has to."
        elif LineNum == 6:
                # She's likes you enough to wipe, not lick. . .
                if Partner == "Rogue":
                    ch_r "I can wipe her off, I guess, but that's it. . ."
                elif Partner == "Kitty":
                    ch_k "I'm not {i}that{/i} catlike. . ."
                elif Partner == "Emma":
                    ch_e "I'll just use my hands, if you don't mind."
                elif Partner == "Laura":
                    ch_l "I don't know, I'll just use my hands."
        elif LineNum == 7:
                # She's obedient. . .
                if Partner == "Rogue":
                    ch_r "Well, that's y'all's business. . ."
                elif Partner == "Kitty":
                    ch_k "No way."
                elif Partner == "Emma":
                    ch_e "I'm afraid not, [E_Petname]."
                elif Partner == "Laura":
                    ch_l "I'd rather not."   
        if not Girl:
                return
        #from the response portion. . .
        elif LineNum == 8:
                # She's into the other girl. . .
                if Girl == "Rogue":
                    ch_r "Well, how could I turn down such an attractive offer. . ."  
                elif Girl == "Kitty":
                    ch_k "I mean[K_like]she seems so into it. . ."
                elif Girl == "Emma":
                    ch_e "I'll allow it, since she seems so excited by it. . ."   
                elif Girl == "Laura":
                    ch_l "I could do worse than her."   
        elif LineNum == 9:
                # She's into you enough. . .
                if Girl == "Rogue":
                    ch_r "If that's what turns you on. . ."   
                elif Girl == "Kitty":
                    ch_k "I guess if you wanna. . ."
                elif Girl == "Emma":
                    ch_e "I'll allow it, if you're that interested. . ."   
                elif Girl == "Laura":
                    ch_l "Sure, if you're into that." 
        elif LineNum == 10:
                # She's into both of you a little. . .
                if Girl == "Rogue":
                    ch_r "Kinda ganging up on me here. . ."
                elif Girl == "Kitty":
                    ch_k "I feel totally targetted."
                elif Girl == "Emma":
                    ch_e "Oh, fine, don't the both of you look at me like that."
                elif Girl == "Laura":
                    ch_l "More the merrier." 
        elif LineNum == 11:
                # She's not into it. . .
                if Girl == "Rogue":
                    ch_r "I'm just not that kinda girl. . ."  
                elif Girl == "Kitty":
                    ch_k "Kinda gross, no."
                elif Girl == "Emma":
                    ch_e "I just can't be party to that."   
                elif Girl == "Laura":
                    ch_l "Hm. . . nah." 
        elif LineNum == 12:
                # She's fine with it. . .
                if Girl == "Rogue":
                    ch_r "I wouldn't mind some help. . ."
                elif Girl == "Kitty":
                    ch_k "How could I say no?"
                elif Girl == "Emma":
                    ch_e "Oh, very well. . ."
                elif Girl == "Laura":
                    ch_l "If you're offering. . ." 
        elif LineNum == 13:
                # After the other girl licked her down. . .
                if Girl == "Rogue":
                    ch_r "Well that was a treat. . ."
                elif Girl == "Kitty":
                    ch_k "That was. . . real nice."
                elif Girl == "Emma":
                    ch_e "Mmmm, I might need to have you over more often."
                elif Girl == "Laura":
                    ch_l "You're really good at that."
        elif LineNum == 14:
                # After the other girl wiped her down. . .
                if Girl == "Rogue":
                    ch_r "Piece of cake, heh. . ."
                elif Girl == "Kitty":
                    ch_k "Um, thanks."
                elif Girl == "Emma":
                    ch_e "Thank you, dear, I hope that wasn't too much bother."
                elif Girl == "Laura":
                    ch_l "That was easy."
                    
        return
      
label Partner_Clean_Girl(Girl=0,TempSpunk=0):
    #either "partner wipe" or Choice == "partner lick"
    
    if Choice != "partner wipe" and Choice != "partner lick":
        return
        
    if Girl == "Rogue":
        $ TempSpunk = R_Spunk
    elif Girl == "Kitty":
        $ TempSpunk = K_Spunk
    elif Girl == "Emma":
        $ TempSpunk = E_Spunk
    elif Girl == "Laura":
        $ TempSpunk = L_Spunk
            
    if Choice == "partner lick":
            call AnyFace(Partner,"tongue")
    $ Cnt = 0    
    if "chin" in TempSpunk or "mouth" in TempSpunk:
            if "chin" in TempSpunk:
                    $ TempSpunk.remove("chin")
            call GirlLikesGirl(Girl,Partner,900,2,1)
            call GirlLikesGirl(Partner,Girl,900,2,1)   
            if Choice == "partner lick":
                call Spunky(Partner,"mouth",2)
                call Spunky(Partner,"chin",2)          
                call Statup(Partner, "Lust", 80, 3)          
                call Statup(Girl, "Lust", 80, 4)
                call Statup("Player", "Focus",80,3)
                "[Partner] licks her way up [Girl]'s chin, before deeply kissing her."
            else:                 
                call Statup(Girl, "Lust", 80, 2)
                "[Partner] wipes her thumb across [Girl]'s chin,"
            $ Cnt += 1      
    if "mouth" in TempSpunk and Cnt:
            $ TempSpunk.remove("mouth")
            "you can see a line of jiz stretching between their mouths."
            $ Cnt += 1
    if "hair" in TempSpunk:
            $ TempSpunk.remove("hair")
            if Cnt:            
                "then she wipes the spunk out of [Girl]'s hair,"
            else:
                "[Partner] wipes the spunk out of [Girl]'s hair,"
            $ Cnt += 1
    if "facial" in TempSpunk:
            $ TempSpunk.remove("facial")
            if Choice == "partner lick":
                    call Spunky(Partner,"mouth",2)
                    call Spunky(Partner,"chin",2)          
                    call Statup(Partner, "Lust", 80, 2)          
                    call Statup(Girl, "Lust", 80, 4)
                    call Statup("Player", "Focus",80,3)
                    if Cnt:    
                        "then she licks the spunk off of [Girl]'s face," 
                    else:
                        "[Partner] licks the spunk off of [Girl]'s face,"                
            else:            
                    call Statup(Girl, "Lust", 80, 1)
                    if Cnt:
                        "then she wipes the spunk off of [Girl]'s face,"  
                    else:
                        "[Partner] wipes the spunk off of [Girl]'s face,"                          
            $ Cnt += 1         
    if "tits" in TempSpunk:
            $ TempSpunk.remove("tits")
            call GirlLikesGirl(Girl,Partner,900,2,1)
            if Choice == "partner lick":
                    call Spunky(Partner,"mouth",2)
                    call Spunky(Partner,"chin",2)       
                    call Statup(Partner, "Lust", 80, 2)          
                    call Statup(Girl, "Lust", 200, 4)
                    call Statup("Player", "Focus",80,4)
                    if Cnt:    
                        "then she licks her way across [Girl]'s chest," 
                    else:
                        "[Partner] licks her way across [Girl]'s chest,"                
            else:    
                    call Statup(Partner, "Lust", 80, 2)          
                    call Statup(Girl, "Lust", 80, 2)
                    call Statup("Player", "Focus",80,2)
                    if Cnt:
                        "then she wipes the spunk off of [Girl]'s chest,"   
                    else:
                        "[Partner] wipes the spunk off of [Girl]'s chest,"                 
            $ Cnt += 1   
    if "belly" in TempSpunk:
            $ TempSpunk.remove("belly")
            if Choice == "partner lick":
                    call Spunky(Partner,"mouth",2)
                    call Spunky(Partner,"chin",2)   
                    call Statup(Partner, "Lust", 80, 2)          
                    call Statup(Girl, "Lust", 80, 3)
                    call Statup("Player", "Focus",80,1)
                    if Cnt:    
                        "then she licks her way down [Girl]'s belly,"  
                    else:
                        "[Partner] licks her way down [Girl]'s belly,"                
            else:    
                    call Statup(Partner, "Lust", 80, 1)          
                    call Statup(Girl, "Lust", 80, 1)
                    if Cnt:
                        "then she wipes the spunk off of [Girl]'s belly,"  
                    else:
                        "[Partner] wipes the spunk off [Girl]'s belly,"                         
            $ Cnt += 1    
    if "back" in TempSpunk:
            $ TempSpunk.remove("back")
            if Choice == "partner lick":
                    call Spunky(Partner,"mouth",2)
                    call Spunky(Partner,"chin",2)               
                    call Statup(Girl, "Lust", 80, 2)
                    if Cnt:    
                        "then she licks her way up [Girl]'s lower back,"  
                    else:
                        "[Partner] licks her way up [Girl]'s lower back,"              
            else:           
                    call Statup(Girl, "Lust", 80, 1)
                    if Cnt:
                        "then she wipes the spunk off of [Girl]'s lower back," 
                    else:
                        "[Partner] wipes the spunk off [Girl]'s lower back,"                        
            $ Cnt += 1   
    if "in" in TempSpunk:
            $ TempSpunk.remove("in")
            call GirlLikesGirl(Girl,Partner,900,5,1)
            if Choice == "partner lick":
                    call Spunky(Partner,"mouth",2)
                    call Spunky(Partner,"chin",2)       
                    call Statup(Partner, "Lust", 80, 4)          
                    call Statup(Girl, "Lust", 200, 6)
                    call Statup("Player", "Focus",80,6)
                    if Cnt:    
                        "then she sucks gently at [Girl]'s pussy," 
                    else:
                        "[Partner] bends down and sucks gently at [Girl]'s pussy,"                
            else:    
                    call Statup(Partner, "Lust", 80, 2)          
                    call Statup(Girl, "Lust", 200, 4)
                    call Statup("Player", "Focus",80,4)
                    if Cnt:
                        "then she strokes along [Girl]'s pussy, wiping the spunk clean,"  
                    else:
                        "[Partner] strokes along [Girl]'s pussy, wiping the spunk clean,"                          
            $ Cnt += 1 
    if "anal" in TempSpunk:
            $ TempSpunk.remove("anal")
            call GirlLikesGirl(Girl,Partner,900,5,1)
            if Choice == "partner lick" and ApprovalCheck(Partner, 800, "I"):
                    call Spunky(Partner,"mouth",2)
                    call Spunky(Partner,"chin",2)       
                    call Statup(Partner, "Lust", 80, 2)          
                    call Statup(Girl, "Lust", 200, 6)
                    call Statup("Player", "Focus",80,5)
                    if Cnt:    
                        "then she licks up the spunk dripping out of [Girl]'s ass," 
                    else:
                        "[Partner] licks up the spunk dripping our of [Girl]'s ass,"             
            else:    
                    call Statup(Partner, "Lust", 80, 2)          
                    call Statup(Girl, "Lust", 200, 6)
                    call Statup("Player", "Focus",80,3)
                    if Cnt:
                        "then she wipes the spunk dripping out of [Girl]'s ass, discarding it,"   
                    else:
                        "[Partner] wipes the spunk dripping our of [Girl]'s ass, discarding it,"                        
            $ Cnt += 1     
    
    call AnyFace(Partner,"sly")
    if "hand" in TempSpunk:
            $ TempSpunk.remove("hand")  
            if Choice == "partner lick":
                    call Spunky(Partner,"mouth",2)
                    call Spunky(Partner,"chin",2)                
                    call Statup(Girl, "Lust", 80, 3)
                    call Statup("Player", "Focus",80,3)
                    if Cnt:    
                        "and finally she licks [Girl]'s hands off with a satisfied grin." 
                    else:
                        "[Partner] licks [Girl]'s fingertips with a satisfied grin."               
            else:    
                    if Cnt:
                        "and finally she wipes [Girl]'s hands clean." 
                    else:
                        "[Partner] wipes [Girl]'s hands off with a satisfied grin."   
                    
            if Choice == "partner lick" or ApprovalCheck(Partner, 1000): 
                    #if the partner swallows
                    call Spunky(Partner,"mouth",0)       
                    call Spunky(Partner,"chin",0)
                    call Statup(Girl, "Inbt", 80, 2) 
                    call Statup("Player", "Focus",80,3)
                    "Then [Partner] swallows and wipes her mouth." 
                    if Partner == "Rogue":
                            $ R_Swallow += 1     
                            $ R_Addict -= (10*Cnt)
                            if R_Swallow == 1:
                                $ R_SEXP += 12
                            $ R_RecentActions.append("swallowed")
                            $ R_DailyActions.append("swallowed") 
                    elif Partner == "Kitty":
                            $ K_Swallow += 1     
                            $ K_Addict -= (10*Cnt)
                            if K_Swallow == 1:
                                $ K_SEXP += 12
                            $ K_RecentActions.append("swallowed")
                            $ K_DailyActions.append("swallowed") 
                    elif Partner == "Emma":
                            $ E_Swallow += 1     
                            $ E_Addict -= (10*Cnt)
                            if E_Swallow == 1:
                                $ E_SEXP += 12
                            $ E_RecentActions.append("swallowed")
                            $ E_DailyActions.append("swallowed") 
                    elif Partner == "Laura":
                            $ L_Swallow += 1     
                            $ L_Addict -= (10*Cnt)
                            if L_Swallow == 1:
                                $ L_SEXP += 12
                            $ L_RecentActions.append("swallowed")
                            $ L_DailyActions.append("swallowed") 
            else:
                #if the Partner won't swallow
                if Cnt:                    
                    "and finally, she wipes her own hands off with a nearby tissue." 
                else:
                    "[Partner] wipes her own hands off with a nearby tissue."                    
            $ Cnt += 1     
    return
    
#label Partner_Clean_Girl(Girl=0,TempSpunk=0):
#    #either "partner wipe" or Choice == "partner lick"
    
#    if Choice != "partner wipe" and Choice != "partner lick":
#        return
    
#    if Girl == "Rogue":
#        $ TempSpunk = R_Spunk[:]
#    elif Girl == "Kitty":
#        $ TempSpunk = K_Spunk[:]
#    elif Girl == "Emma":
#        $ TempSpunk = E_Spunk[:]
#    elif Girl == "Laura":
#        $ TempSpunk = L_Spunk[:]
        
#    if Choice == "partner lick":
#            call AnyFace(Partner,"tongue")
#    $ Cnt = 0    
#    if "chin" in TempSpunk or "mouth" in TempSpunk:
#            if "chin" in TempSpunk:
#                    $ TempSpunk.remove("chin")
#            call Spunky(Girl,"chin",0)
#            call GirlLikesGirl(Girl,Partner,900,2,1)
#            call GirlLikesGirl(Partner,Girl,900,2,1)
#            if Choice == "partner lick":
#                call Spunky(Partner,"mouth",2)
#                call Spunky(Partner,"chin",2)
#                "[Partner] licks her way up [Girl]'s chin, before deeply kissing her."
#            else:
#                "[Partner] wipes her thumb across [Girl]'s chin,"
#            $ Cnt += 1      
#    if "mouth" in TempSpunk and Cnt:
#            $ TempSpunk.remove("mouth")
#            call Spunky(Girl,"mouth",0)
#            "you can see a line of jiz stretching between their mouths."
#            $ Cnt += 1
#    if "hair" in TempSpunk:
#            $ TempSpunk.remove("hair")
#            call Spunky(Girl,"hair",0)
#            if Cnt:            
#                "then she wipes the spunk out of [Girl]'s hair,"
#            else:
#                "[Partner] wipes the spunk out of [Girl]'s hair,"
#            $ Cnt += 1
#    if "facial" in TempSpunk:
#            $ TempSpunk.remove("facial")
#            call Spunky(Girl,"facial",0)
#            if Cnt:
#                if Choice == "partner lick":
#                    call Spunky(Partner,"mouth",2)
#                    call Spunky(Partner,"chin",2)
#                    "then she licks the spunk off of [Girl]'s face," 
#                else:
#                    "then she wipes the spunk off of [Girl]'s face,"   
#            else:
#                if Choice == "partner lick":
#                    call Spunky(Partner,"mouth",2)
#                    call Spunky(Partner,"chin",2)
#                    "[Partner] licks the spunk off of [Girl]'s face,"  
#                else:
#                    "[Partner] wipes the spunk off of [Girl]'s face,"   
#            $ Cnt += 1         
#    if "tits" in TempSpunk:
#            $ TempSpunk.remove("tits")
#            call Spunky(Girl,"tits",0)
#            call GirlLikesGirl(Girl,Partner,900,2,1)
#            if Cnt:
#                if Choice == "partner lick":
#                    call Spunky(Partner,"mouth",2)
#                    call Spunky(Partner,"chin",2)
#                    "then she licks her way across [Girl]'s chest," 
#                else:
#                    "then she wipes the spunk off of [Girl]'s chest,"   
#            else:
#                if Choice == "partner lick":
#                    call Spunky(Partner,"mouth",2)
#                    call Spunky(Partner,"chin",2)
#                    "[Partner] licks her way across [Girl]'s chest,"
#                else:
#                    "[Partner] wipes the spunk off of [Girl]'s chest," 
#            $ Cnt += 1           
#    if "belly" in TempSpunk:
#            $ TempSpunk.remove("belly")
#            call Spunky(Girl,"belly",0)
#            if Cnt:
#                if Choice == "partner lick":
#                    call Spunky(Partner,"mouth",2)
#                    call Spunky(Partner,"chin",2)
#                    "then she licks her way down [Girl]'s belly,"  
#                else:
#                    "then she wipes the spunk off of [Girl]'s belly,"   
#            else:
#                if Choice == "partner lick":
#                    call Spunky(Partner,"mouth",2)
#                    call Spunky(Partner,"chin",2)
#                    "[Partner] licks her way down [Girl]'s belly," 
#                else:
#                    "[Partner] wipes the spunk off [Girl]'s belly," 
#            $ Cnt += 1     
#    if "in" in TempSpunk:
#            $ TempSpunk.remove("in")
#            call Spunky(Girl,"in",0)
#            call GirlLikesGirl(Girl,Partner,900,5,1)
#            if Cnt:
#                if Choice == "partner lick":
#                    call Spunky(Partner,"mouth",2)
#                    call Spunky(Partner,"chin",2)
#                    "then she sucks gently at [Girl]'s pussy," 
#                else:
#                    "then she wipes the spunk inside [Girl]'s pussy,"   
#            else:
#                if Choice == "partner lick":
#                    call Spunky(Partner,"mouth",2)
#                    call Spunky(Partner,"chin",2)
#                    "[Partner] bends down and sucks gently at [Girl]'s pussy,"  
#                else:
#                    "[Partner] wipes the spunk inside [Girl]'s pussy,"     
#            $ Cnt += 1 
#    if "anal" in TempSpunk:
#            $ TempSpunk.remove("anal")
#            call Spunky(Girl,"anal",0)
#            call GirlLikesGirl(Girl,Partner,900,5,1)
#            if Cnt:
#                if Choice == "partner lick" and ApprovalCheck(Partner, 800, "I"):
#                    call Spunky(Partner,"mouth",2)
#                    "then she licks up the spunk dripping out of [Girl]'s ass," 
#                else:
#                    "then she wipes the spunk dripping out of [Girl]'s ass, discarding it,"   
#            else:
#                if Choice == "partner lick" and ApprovalCheck(Partner, 800, "I"):
#                    call Spunky(Partner,"mouth",2)
#                    call Spunky(Partner,"chin",2)
#                    "[Partner] licks up the spunk dripping our of [Girl]'s ass,"
#                else:
#                    "[Partner] wipes the spunk dripping our of [Girl]'s ass, discarding it,"
#            $ Cnt += 1     
    
#    call AnyFace(Partner,"sly")
#    if "hand" in TempSpunk:
#            $ TempSpunk.remove("hand")
#            call Spunky(Girl,"hand",0)                
#            if Cnt:
#                if Choice == "partner lick":   
#                    call Spunky(Partner,"mouth",2)
#                    call Spunky(Partner,"chin",2)
#                    "and finally she licks [Girl]'s hands off with a satisfied grin." 
#                else:
#                    "and finally she wipes [Girl]'s hands clean." 
#            else:
#                if Choice == "partner lick":
#                    call Spunky(Partner,"mouth",2)
#                    call Spunky(Partner,"chin",2)
#                    "[Partner] licks [Girl]'s fingertips with a satisfied grin."   
#                else:
#                    "[Partner] wipes [Girl]'s hands off with a satisfied grin."   
#            if Choice == "partner lick" or ApprovalCheck(Partner, 1000): 
#                    #if the partner swallows
#                    call Spunky(Partner,"mouth",0)       
#                    call Spunky(Partner,"chin",0)
#                    call Statup(Girl, "Inbt", 80, 2) 
#                    "Then [Partner] swallows and wipes her mouth." 
#                    if Partner == "Rogue":
#                        $ R_Swallow += 1     
#                        $ R_Addict -= (10*Cnt)
#                        if R_Swallow == 1:
#                            $ R_SEXP += 12
#                        $ R_RecentActions.append("swallowed")
#                        $ R_DailyActions.append("swallowed") 
#                    elif Partner == "Kitty":
#                        $ K_Swallow += 1     
#                        $ K_Addict -= (10*Cnt)
#                        if K_Swallow == 1:
#                            $ K_SEXP += 12
#                        $ K_RecentActions.append("swallowed")
#                        $ K_DailyActions.append("swallowed") 
#                    elif Partner == "Emma":
#                        $ E_Swallow += 1     
#                        $ E_Addict -= (10*Cnt)
#                        if E_Swallow == 1:
#                            $ E_SEXP += 12
#                        $ E_RecentActions.append("swallowed")
#                        $ E_DailyActions.append("swallowed") 
#                    elif Partner == "Laura":
#                        $ L_Swallow += 1     
#                        $ L_Addict -= (10*Cnt)
#                        if L_Swallow == 1:
#                            $ L_SEXP += 12
#                        $ L_RecentActions.append("swallowed")
#                        $ L_DailyActions.append("swallowed") 
#            else:
#                #if the Partner won't swallow
#                if Cnt:                    
#                    "and finally, she wipes her own hands off with a nearby tissue." 
#                else:
#                    "[Partner] wipes her own hands off with a nearby tissue."                    
#            $ Cnt += 1     
#    return
    
label Spunky(Girl=0,Type=0,Add=0):
        # girl is the girl, Type is the type being added or removed, 
        # Add is 1 if adding, 0 if removing, 2 if only adding it once
        # call Spunky(Partner,"mouth",1)
        if Girl == "Rogue":
                if Add == 2 and Type not in R_Spunk:
                            $ R_Spunk.append(Type)
                elif Add:
                            $ R_Spunk.append(Type)
                else:
                    while Type in R_Spunk:
                            $ R_Spunk.remove(Type)
        elif Girl == "Kitty":
                if Add == 2 and Type not in K_Spunk:
                            $ K_Spunk.append(Type)
                elif Add:
                            $ K_Spunk.append(Type)
                else:
                    while Type in K_Spunk:
                            $ K_Spunk.remove(Type)
        elif Girl == "Emma":
                if Add == 2 and Type not in E_Spunk:
                            $ E_Spunk.append(Type)
                elif Add:
                            $ E_Spunk.append(Type)
                else:
                    while Type in E_Spunk:
                            $ E_Spunk.remove(Type)
        elif Girl == "Laura":
                if Add == 2 and Type not in L_Spunk:
                            $ L_Spunk.append(Type)
                elif Add:
                            $ L_Spunk.append(Type)
                else:
                    while Type in L_Spunk:
                            $ L_Spunk.remove(Type)    
        return
        
# End Clean-up  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  


label Girl_Caught_Changing(Girl=0):
            if not Girl:
                    return
            call Shift_Focus(Girl)
            $ D20 = renpy.random.randint(1, 20)
            
            call AnyFace(Girl,"surprised", 1,Mouth="kiss")
            
            if D20 > 17:        
                    #She's naked
                    call AnyOutfit(Girl,"nude")
            else:
                    #restore base outfit
                    call AnyOutfit(Girl,6)                     
                    if D20 >15:       
                            #She's bottomless
                            call AnyOutfit(Girl,9) #Legs
                            call AnyOutfit(Girl,10) #Panties
                    elif D20 >14:       
                            #She's Topless
                            call AnyOutfit(Girl,7) #Over
                            call AnyOutfit(Girl,8) #Chest
                    elif D20 >10:       
                            #She's in her underwear
                            call AnyOutfit(Girl,7) #Over
                            call AnyOutfit(Girl,9) #Legs
                    elif D20 >5:        
                            #She's wearing pants/skirt
                            call AnyOutfit(Girl,7) #Over
            #else: #fully dressed
            call Set_The_Scene(Dress=0)
            if D20 > 17:        
                    #She's naked
                    "As you enter the room, you see [Girl] is naked, and seems to be getting dressed."      
            elif D20 >14:       
                    #She's Topless
                    "As you enter the room, you see [Girl] is practically naked, and seems to be getting dressed."  
            elif D20 >10:       
                    #She's in her underwear
                    "As you enter the room, you see [Girl] is in her underwear, and seems to be getting dressed." 
            elif D20 >5:        
                    #She's wearing pants/skirt
                    "As you enter the room, you see [Girl] has her top off, and seems to be getting dressed." 
            else:
                    #She's done
                    "As you enter the room, you see [Girl] has just pulled her top on, and seems to have been getting dressed." 
                 
            if D20 > 5: 
                    if not ApprovalCheck(Girl, (D20 *70)) and SeenCheck(Girl) >= 3:
                            # if D20*70 is less than her approval, and this is the first you've seen of her bits. . .
                            call AnyFace(Girl,"surprised",Brows="angry")  
                            call Statup(Girl, "Love", 80, -50)
                            
                            if not OverNum(Girl) or (OverNum(Girl)+ChestNum(Girl) <5) or (PantsNum(Girl) < 5 and HoseNum(Girl) < 10):
                                # if either she is mostly topless or mostly bottomless)
                                call AnyOutfit(Girl,7,TempOver="towel")  
                                "She grabs a towel and covers up."
                    else:       
                            #She's cool with it, but confused.
                            call AnyFace(Girl,"surprised", 1,Brows = "confused")
                            if ExhibitionistCheck(Girl):
                                call Statup(Girl, "Lust", 200, (2*D20))  
                            else:
                                call Statup(Girl, "Lust", 200, D20)
                          
                    call Statup(Girl, "Inbt", 70, 20)
                    
                    if D20 > 17:
                        call expression Girl + "_First_Bottomless"
                        call expression Girl + "_First_Topless(1)"
                    elif D20 > 15:
                        call expression Girl + "_First_Bottomless"
                    elif D20 > 14:
                        call expression Girl + "_First_Topless"
                       
                    if Girl == "Rogue":
                            ch_r "Hey! Learn to knock maybe?!"
                    elif Girl == "Kitty":
                            ch_k "Why didn't you knock?!"
                    elif Girl == "Emma":
                            ch_e "Did you consider knocking?"
                    elif Girl == "Laura":
                            ch_l "Didn't think about knocking?"
                    menu:
                        extend ""
                        "Sorry, I should have knocked.":  
                                call Statup(Girl, "Love", 50, 2)
                                call Statup(Girl, "Love", 80, 4)
                        "And miss the view?":
                                call Statup(Girl, "Obed", 50, 2)
                                call Statup(Girl, "Obed", 80, 2)
                                call Statup(Girl, "Inbt", 60, 1)
                    #end if she's partially nude
            else:              
                    #She's fully dressed      
                    if not ApprovalCheck(Girl, 800) and not SeenCheck(Girl):            
                            call AnyFace(Girl,"angry",Brows="confused")
                            call Statup(Girl, "Love", 80, -5)
                    else:
                            call AnyFace(Girl,"sexy",Brows="confused")
                    call Statup(Girl, "Inbt", 50, 3)
                    
                    if Girl == "Rogue":
                            ch_r "Well hello there, [R_Petname]. Hoping to see something more?"
                    elif Girl == "Kitty":
                            ch_k "Hey, [K_Petname]. . . {i}you{/i} were hoping I'd be naaaked."
                    elif Girl == "Emma":
                            ch_e "Were you hoping to catch me in a compromising position?."
                    elif Girl == "Laura":
                            ch_l "Hey, [L_Petname]. Trying to catch a peek?"
                            
                    menu:
                        extend ""
                        "Sorry, I should have knocked.":   
                                call Statup(Girl, "Love", 50, 2)
                                call Statup(Girl, "Love", 80, 2)
                        "Well, to be honest. . .":
                                call Statup(Girl, "Love", 50, -2)
                                call Statup(Girl, "Obed", 50, 2)
                                call Statup(Girl, "Obed", 80, 2)
                                call Statup(Girl, "Inbt", 60, 1)
            call AnyFace(Girl,"sexy")
            if ApprovalCheck(Girl, 750) and SeenCheck(Girl):
                    #she flashes you
                    if Girl == "Rogue":
                            ch_r "You could have just asked, [R_Petname]."           
                    elif Girl == "Kitty":
                            ch_k "I didn't say that I {i}minded{/i}. . ."              
                    elif Girl == "Emma":
                            ch_e "That does show initiative. . ."                
                    elif Girl == "Laura":
                            ch_l "I don't mind."
                                           
                    call AnyOutfit(Girl,12) #Uptop up                   
                    call AnyOutfit(Girl,11) #Upskirt up
                    pause 1      
                    call expression Girl + "_First_Topless" pass (1)
                    call expression Girl + "_First_Bottomless" pass (1)                   
                    call AnyOutfit(Girl,5,0,0) #restore current outfit
                    "She flashes you real quick."  
            else:
                    #if she doesn't flash you
                    if Girl == "Rogue":
                            ch_r "Well, it happens, just be careful next time."  
                    elif Girl == "Kitty":
                            ch_k "Yeah. . . we wouldn't want any accidents. . ."  
                    elif Girl == "Emma":
                            ch_e "Hmm, show a bit more care next time. . ." 
                    elif Girl == "Laura":
                            ch_l "Uh-huh . . ."  
            if Girl == "Rogue": 
                    ch_r "Well, are you planning to stick around?" 
            elif Girl == "Kitty":
                    ch_k "So were you planning on staying?" 
            elif Girl == "Emma": 
                    ch_e "Did you have business with me?" 
            elif Girl == "Laura":
                    ch_l "So did you plan to stay?"  
            menu:
                    extend ""
                    "Sure, for a bit.":
                            pass
                    "Actually, I should get going. . .":
                            call AnyOutfit(Girl,6,Changed=0)
                            $ renpy.pop_call()
                            call Worldmap            
#            jump Laura_Room
            return
#End Girl Caught Changing

#start girls sunbathing / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Pool_Sunbathe(Girl=0,Chest=0,Panties=0,Over=0,Legs=0,Line=0,Type=0,Mod=0):
    # This gets called with a character name, and checks 
    # Line tends to carry the current agreement state, Type tends to carry the item being discussed
    # mod is a modifier, base 0, but +200 if asking for no bottoms
    
    menu:
        "With who?"
        "Rogue" if bg_current == R_Loc:                                
                $ Girl = "Rogue"
        "Kitty" if bg_current == K_Loc:                                 
                $ Girl = "Kitty"
        "Emma" if bg_current == E_Loc:                                   
                $ Girl = "Emma"
        "Laura" if bg_current == L_Loc:                                  
                $ Girl = "Laura"
        "Never mind.":
                return
                    
    if not CheckWord(Girl,"Recent","tan") and not CheckWord(Girl,"Recent","no tan"):
            ch_p "Hey, [Girl], why don't you just relax over here?"
            ch_p "You don't want to get tanlines, why don't you. . ."
            ch_p ". . . take off a few layers?"
    else:
            ch_p "Are you sure you don't want to. . ."
    
    if Current_Time == "Night" or Current_Time == "Evening":
            call AnyFace(Girl,"confused")
            call AnyLine(Girl,"A bit late in the day for that. . .")
            call AnyFace(Girl,"normal")
            return        
    if not ClothingCheck(Girl):
            #if she's already nude. . .
            call AnyFace(Girl,"sly")
            call AnyLine(Girl,"Little late for that.")
            if Girl == "Kitty" or Girl == "Rogue":
                call Mod_Tan(Girl,5)
            return            
    if CheckWord(Girl,"Recent","no tan"):
            call AnyFace(Girl,"angry")
            call AnyLine(Girl,"I just told you \"no.\"")
            call AnyWord(Girl,1,"angry","angry") #makes her angry
            return
    elif CheckWord(Girl,"Daily","no tan"):
            call AnyFace(Girl,"angry")
            call AnyLine(Girl,"Not today.")
            call AnyWord(Girl,1,"angry","angry") #makes her angry
            return
    
    if Girl == "Rogue":
            $ Chest = R_Chest
            $ Panties = R_Panties
            $ Over = R_Over
            $ Legs = R_Legs
            if Legs == 0 and R_Hose:
                $ Legs = R_Hose  
    elif Girl == "Kitty":
            $ Chest = K_Chest
            $ Panties = K_Panties
            $ Over = K_Over
            $ Legs = K_Legs
            if Legs == 0 and K_Hose:
                $ Legs = K_Hose  
    elif Girl == "Emma":
            if "classcaught" not in E_History:        
                    call AnyFace(Girl,"angry",2)
                    ch_e "That would be entirely inappropriate."
                    return
            if "taboo" not in E_History:    
                    call AnyFace(Girl,"bemused",2)
                    ch_e "[E_Petname], we can't be seen like that in public. . ."
                    return
            if "three" not in E_History:
                    call CleartheRoom("Emma",Check=1)
                    if _return >= 1:    
                            call AnyFace(Girl,"bemused",2)
                            ch_e "Not with this sort of company. . ."
                            return                    
            $ Chest = E_Chest
            $ Panties = E_Panties
            $ Over = E_Over
            $ Legs = E_Legs
            if Legs == 0 and E_Hose:
                $ Legs = E_Hose                
    elif Girl == "Laura":
            $ Chest = L_Chest
            $ Panties = L_Panties
            $ Over = L_Over
            $ Legs = L_Legs   
            if Legs == 0 and L_Hose:
                $ Legs = L_Hose             
    
    if not Over and not Chest and not Legs and not Panties:
            #if she's already nude. . .
            call AnyFace(Girl,"sly")
            if Girl == "Rogue":
                ch_r "I don't think that'll be a problem, [R_Petname]."
            elif Girl == "Kitty":
                ch_k "Beat you to it."
            elif Girl == "Emma":
                ch_e "I plan ahead."
            elif Girl == "Laura":
                ch_l "Yup."
            call AnyWord(Girl,1,"tan","tan") #adds the "tan" trait to recent and daily actions
            if Girl == "Kitty" or Girl == "Rogue":
                call Mod_Tan(Girl,5)
            return
        
        
    while True:
            #loops until you return
            if not Line:
                #only asks questions if there's not a play on the table.
                menu:
                    extend ""
                    "lose the top?" if Chest:
                            $ Type = "bra"
                                
                    "take it all off?" if (Over or Chest) and (Legs or Panties):
                            if Over == "towel" and not Legs and not Panties:
                                $ Type = "no panties"
                            elif Legs and not Panties:
                                $ Type = "no panties"
                            elif Over and not Chest:
                                $ Type = "no bra"
                            else: 
                                $ Type = "both"
                            $ Mod = 200
                                
                    "maybe just lose the [Over]?" if Over:
                            if Over == "towel" and not Panties:
                                $ Type = "no panties"
                            elif not Chest:
                                $ Type = "no bra"
                            else: 
                                $ Type = "over"
                                
                    "maybe just lose the [Legs]?" if Legs:
                            if not Panties:
                                $ Type = "no panties"
                            else: 
                                $ Type = "legs"
                                
                    "maybe just lose the [Panties]?" if Panties:
                                $ Type = "panties"
                                $ Mod = 200    
                                                                
                    "never mind.":
                            if Girl == "Kitty" or Girl == "Rogue":
                                call Mod_Tan(Girl,5)
                            return
            # end menu
                                        
            if Type == "no panties":
                    $ Mod = 200    
                    call AnyFace(Girl,"bemused",1)
                    call AnyLine(Girl,"I don't have bottoms on under this. . .")  
            elif Type == "no bra":
                    call AnyFace(Girl,"bemused",1)
                    call AnyLine(Girl,"I don't have a top on under this. . .")              
            
            if SeenCheck(Girl,1):
                    $ Mod += 100
                    
            # This is the primary check to see whether she's into it.
            if ExhibitionistCheck(Girl):
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
                                    if not CheckWord(Girl,"Recent","tan") and not CheckWord(Girl,"Recent","no tan"):
                                        call Statup(Girl, "Inbt", 70, 1)
                                        
                                    call AnyFace(Girl,"sly",1)
                                    if Girl == "Rogue":
                                        ch_r "Hmm, good point. . ."
                                    elif Girl == "Kitty":
                                        ch_k "\"And\". . . I don't know. . ."
                                    elif Girl == "Emma":
                                        ch_e "\"And\". . . you're lucky you're so cute. . ."
                                    elif Girl == "Laura":
                                        ch_l "I don't know. . ."
                            else:
                                    if not CheckWord(Girl,"Recent","tan") and not CheckWord(Girl,"Recent","no tan"):
                                        call Statup(Girl, "Love", 70, -1)
                                        call Statup(Girl, "Obed", 80, 1)
                                        
                                    call AnyFace(Girl,"angry",2)
                                    if Girl == "Rogue":
                                        ch_r "\"And\" that's all you're getting. . . for now. . ."
                                    elif Girl == "Kitty":
                                        ch_k "\"And\". . . AND!"
                                    elif Girl == "Emma":
                                        ch_e "\"And\". . . you shouldn't push your luck. . ."
                                    elif Girl == "Laura":
                                        ch_l "\"And\" that's all you get."
                        "Take it off anyway.":
                            if Line == "sure" or (Line == "sorry" and ApprovalCheck(Girl, 600+Mod, "O")):
                                    if not CheckWord(Girl,"Recent","tan") and not CheckWord(Girl,"Recent","no tan"):
                                        call Statup(Girl, "Obed", 50, 1)
                                        call Statup(Girl, "Obed", 80, 2)
                                    if Line != "sure":    
                                            call AnyFace(Girl,"sad",2)
                                    else:
                                            call AnyFace(Girl,"normal",1)
                                    if Girl == "Rogue":
                                        ch_r "Oh, ok. . ."
                                    elif Girl == "Kitty":
                                        ch_k "Yeah, ok. . ."
                                    elif Girl == "Emma":
                                        ch_e "If you insist. . ."
                                    elif Girl == "Laura":
                                        ch_l "Affirmative."
                                        
                                    $ Line = "sure"
                            else:
                                    if not CheckWord(Girl,"Recent","tan") and not CheckWord(Girl,"Recent","no tan"):
                                        call Statup(Girl, "Love", 80, -2)
                                        call Statup(Girl, "Obed", 80, -1)
                                        call Statup(Girl, "Inbt", 60, 1)
                                        
                                    call AnyFace(Girl,"angry",1)
                                    if Girl == "Rogue":
                                        ch_r "I don't like that tone on you. . ."
                                    elif Girl == "Kitty":
                                        ch_k "How about \"no\". . ."
                                    elif Girl == "Emma":
                                        ch_e "Not with that tone. . ."
                                    elif Girl == "Laura":
                                        ch_l "Don't push me."
                                        
                                    call AnyWord(Girl,1,"no tan","no tan") #adds the "no tan" trait to recent and daily actions
                                    return
                        "Hot.":
                                    if not CheckWord(Girl,"Recent","tan") and not CheckWord(Girl,"Recent","no tan"):
                                        call Statup(Girl, "Love", 80, 1)
                                        call Statup(Girl, "Obed", 70, 2)
                                        call Statup(Girl, "Inbt", 60, 1)
                                        call Statup(Girl, "Inbt", 80, 1)
                                        
                                    call AnyFace(Girl,"sly",1)
                                    if Girl == "Rogue":
                                        ch_r "Heh, you're a sweetie. . ."
                                    elif Girl == "Kitty":
                                        ch_k "Hehe. . ."
                                    elif Girl == "Emma":
                                        ch_e "How sweet. . ."
                                    elif Girl == "Laura":
                                        ch_l "True."
                                        
                        "Ok, that's fine.": 
                            if Line == "sure":
                                    if not CheckWord(Girl,"Recent","tan") and not CheckWord(Girl,"Recent","no tan"):
                                        call Statup(Girl, "Love", 80, 2)
                                        call Statup(Girl, "Obed", 80, 1)
                                        call Statup(Girl, "Inbt", 60, 1)
                                        call Statup(Girl, "Inbt", 80, 1)
                                        
                                    call AnyFace(Girl,"sly",1)
                                    if Girl == "Rogue":
                                        ch_r "Ready for a nice surprise? . ."
                                    elif Girl == "Kitty":
                                        ch_k "Oh, you bet it is. . ."
                                    elif Girl == "Emma":
                                        ch_e "More than you know. . ."
                                    elif Girl == "Laura":
                                        ch_l "But I can be generous. . ."
                            else:
                                    if not CheckWord(Girl,"Recent","tan") and not CheckWord(Girl,"Recent","no tan"):
                                        call Statup(Girl, "Love", 50, 1)
                                        call Statup(Girl, "Love", 80, 1)
                                        call Statup(Girl, "Inbt", 60, 1)
                                        
                                    call AnyFace(Girl,"smile")
                                    if Girl == "Rogue":
                                        ch_r "Thanks, [R_Petname]. . ."
                                    elif Girl == "Kitty":
                                        ch_k "Thanks. . ."
                                    elif Girl == "Emma":
                                        ch_e "Good. . ."
                                    elif Girl == "Laura":
                                        ch_l "Right."
                    
                    if Line == "sure":
                            #she agrees
                            call AnyOutfit(Girl,7) # removes Over
                            $ Over = 0
                            call expression Girl + "_First_Topless"
                            if Type == "no panties":
                                    call AnyOutfit(Girl,9) # removes Legs
                                    call AnyOutfit(Girl,13) # removes Hose                                    
                                    $ Legs = 0
                                    call expression Girl + "_First_Bottomless"
                            call AnyWord(Girl,1,"tan","tan") #adds the "tan" trait to recent and daily actions
                    else:
                            call AnyWord(Girl,1,"no tan","no tan") #adds the "no tan" trait to recent and daily actions
                                
                    $ Line = 0
            # end "nothing on under this. . ."   
                    
            if Line == "sure":
                    #She agrees. . .
                    if not CheckWord(Girl,"Recent","tan") and not CheckWord(Girl,"Recent","no tan"):
                            call Statup(Girl, "Obed", 70, 2)
                            call Statup(Girl, "Obed", 90, 1)
                            call Statup(Girl, "Inbt", 70, 2)
                            call Statup(Girl, "Inbt", 90, 1)
                    call AnyFace(Girl,"sly",1)
                    if Girl == "Rogue":
                        ch_r "I suppose I could. . ."
                    elif Girl == "Kitty":
                        ch_k "I guess. . ."
                    elif Girl == "Emma":
                        ch_e "Hmmm. . ."
                    elif Girl == "Laura":
                        ch_l "Sure."
                        
                    if Type == "over" or Type == "both":
                            call AnyOutfit(Girl,7) # removes Over
                            $ Over = 0
                    if Type == "bra" or Type == "both":
                            call AnyOutfit(Girl,8) # removes Bra
                            $ Chest = 0                            
                    call expression Girl + "_First_Topless"
                    
                    if Type == "legs" or Type == "both":
                            call AnyOutfit(Girl,9) # removes Legs
                            call AnyOutfit(Girl,13) # removes Hose
                            $ Legs = 0
                    if Type == "panties" or Type == "both":
                            call AnyOutfit(Girl,10) # removes Panties
                            $ Panties = 0                            
                    call expression Girl + "_First_Bottomless"
                    
                    call AnyWord(Girl,1,"tan","tan") #adds the "tan" trait to recent and daily actions
                            
            elif Line == "sorry" and (Type == "over" or Type == "legs"):
                    #She agrees to just an over-layer. . .
                    if not CheckWord(Girl,"Recent","tan") and not CheckWord(Girl,"Recent","no tan"):
                            call Statup(Girl, "Obed", 50, 1)
                            call Statup(Girl, "Obed", 80, 1)
                            call Statup(Girl, "Inbt", 60, 1)
                            call Statup(Girl, "Inbt", 80, 1)
                    call AnyFace(Girl,"bemused",1)
                    if Girl == "Rogue":
                        ch_r "I suppose I could. . ."
                    elif Girl == "Kitty":
                        ch_k "I guess. . ."
                    elif Girl == "Emma":
                        ch_e "Hmmm. . ."
                    elif Girl == "Laura":
                        ch_l "Sure."
                        
                    if Type == "over":
                            call AnyOutfit(Girl,7) # removes Over
                            $ Over = 0
                    if Type == "legs":
                            call AnyOutfit(Girl,9) # removes Legs
                            $ Legs = 0
                    call AnyWord(Girl,1,"tan","tan") #adds the "tan" trait to recent and daily actions
                            
            elif Line == "sorry":
                    #She refuses but is not offended. . .
                    if not CheckWord(Girl,"Recent","tan") and not CheckWord(Girl,"Recent","no tan"):
                            call Statup(Girl, "Obed", 50, 2)
                            call Statup(Girl, "Obed", 80, 2)
                            call Statup(Girl, "Inbt", 60, 1)
                            call Statup(Girl, "Inbt", 90, 2)
                    call AnyFace(Girl,"sadside",1)
                    if Girl == "Rogue":
                        ch_r "Sorry, I think I can live with the tan lines. . ."
                    elif Girl == "Kitty":
                        ch_k "I just can't. . ."
                    elif Girl == "Emma":
                        ch_e "That just wouldn't be appropriate. . ."
                    elif Girl == "Laura":
                        ch_l "Nah. . ."
                        
                    call AnyWord(Girl,1,"no tan","no tan") #adds the "no tan" trait to recent and daily actions
                    
            elif Line == "no":
                    #She is offended you even asked. . .
                    call Statup(Girl, "Love", 50, -5)
                    call Statup(Girl, "Obed", 50, 2)
                    call Statup(Girl, "Inbt", 60, 1)
                    call AnyFace(Girl,"angry",1)
                    if Girl == "Rogue":
                        ch_r "Not interested, [R_Petname]. . ."
                    elif Girl == "Kitty":
                        ch_k "Not even."
                    elif Girl == "Emma":
                        ch_e "You must be dreaming. . ."
                    elif Girl == "Laura":
                        ch_l "Nope. . ."
                        
                    call AnyWord(Girl,1,"no tan","no tan") #adds the "no tan" trait to recent and daily actions
                    return
            if not ChestNum(Girl) and not OverNum(Girl) and not PantiesNum(Girl) and not PantsNum(Girl) and HoseNum(Girl) < 10:
                        call AnyOutfit(Girl,"nude") #removes remaining clothing.
            $ Mod = 0
            $ Line = 0
            if ClothingCheck(Girl):
                "Anything else?" #loops back to menu
            else:
                if Girl == "Kitty" or Girl == "Rogue":
                    call Mod_Tan(Girl,5)
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
        "Rogue" if bg_current == R_Loc:                                
                $ Girl = "Rogue"
        "Kitty" if bg_current == K_Loc:                                 
                $ Girl = "Kitty"
        "Emma" if bg_current == E_Loc:                                   
                $ Girl = "Emma"
        "Laura" if bg_current == L_Loc:                                  
                $ Girl = "Laura"
        "Never mind.":
                return
                
    ch_p "Hey, [Girl], why don't we skinny dip?"
    
    if Round <= 10:
            call AnyFace(Girl,"sad")
            call AnyLine(Girl,"No time for that.")
            return    
    elif CheckWord(Girl,"Recent","no dip"):
            call AnyFace(Girl,"angry")
            call AnyLine(Girl,"I just told you \"no.\"")
            call AnyWord(Girl,1,"angry","angry") #makes her angry
            return
    elif CheckWord(Girl,"Daily","no dip"):
            call AnyFace(Girl,"angry")
            call AnyLine(Girl,"Not today.")
            call AnyWord(Girl,1,"angry","angry") #makes her angry
            return
    elif CheckWord(Girl,"Recent","dip"):
            call AnyFace(Girl,"confused")
            call AnyLine(Girl,"We already did that.")
            return
     
    if Girl == "Emma":
            if "classcaught" not in E_History:        
                    call AnyFace(Girl,"angry",2)
                    ch_e "That would be entirely inappropriate."
                    return
            if "taboo" not in E_History:    
                    call AnyFace(Girl,"bemused",2)
                    ch_e "[E_Petname], I couldn't risk us getting caught. . ."
                    return
            if "three" not in E_History:
                    call CleartheRoom("Emma",Check=1)
                    if _return >= 1:    
                            call AnyFace(Girl,"bemused",2)
                            ch_e "Not with this sort of company. . ."
                            return                         
    
    if not ClothingCheck(Girl):
            #if she's already nude. . .
            call AnyFace(Girl,"sly")
            if Girl == "Rogue":
                ch_r "Sure, let's get wet."
            elif Girl == "Kitty":
                ch_k "Cannonball!"
            elif Girl == "Emma":
                ch_e "Lovely."
            elif Girl == "Laura":
                ch_l "I'm in."
            call AnyWord(Girl,1,"dip","dip") #adds the "dip" trait to recent and daily actions
    else:
            #if she's dressed. . .
            if SeenCheck(Girl,1):
                    $ Mod += 100
                            
            if ExhibitionistCheck(Girl):
                    #if she's an exhibitionist
                    $ Line = "sure"
            elif ApprovalCheck(Girl, 700+Mod, "I"):
                    #if she's generally slutty
                    $ Line = "sure"
            elif ApprovalCheck(Girl, 1200+Mod):
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
                    if not CheckWord(Girl,"Recent","dip") and not CheckWord(Girl,"Recent","no dip"):   
                            call Statup(Girl, "Obed", 70, 2)
                            call Statup(Girl, "Obed", 90, 1)
                            call Statup(Girl, "Inbt", 70, 2)
                            call Statup(Girl, "Inbt", 90, 1)
                    call AnyFace(Girl,"sly",1)
                    if Girl == "Rogue":
                        ch_r "Sounds fun. . ."
                    elif Girl == "Kitty":
                        ch_k "Oooh, naughty. . ."
                    elif Girl == "Emma":
                        ch_e "How daring. . ."
                    elif Girl == "Laura":
                        ch_l "Sure."
                        
                    call AnyOutfit(Girl,7) # removes Over
                    call AnyOutfit(Girl,8) # removes Bra 
                    call expression Girl + "_First_Topless"
                    
                    call AnyOutfit(Girl,9) # removes Legs
                    call AnyOutfit(Girl,13) # removes Hose
                    call AnyOutfit(Girl,10) # removes Panties            
                    call expression Girl + "_First_Bottomless"
                    call AnyOutfit(Girl,"nude") #removes remaining clothing.
                    call AnyWord(Girl,1,"dip","dip") #adds the "dip" trait to recent and daily actions
                                                
            elif Line == "sorry":
                    #She refuses but is not offended. . .
                    if not CheckWord(Girl,"Recent","dip") and not CheckWord(Girl,"Recent","no dip"):   
                            call Statup(Girl, "Obed", 50, 2)
                            call Statup(Girl, "Obed", 80, 2)
                            call Statup(Girl, "Inbt", 60, 1)
                            call Statup(Girl, "Inbt", 90, 2)
                    call AnyFace(Girl,"sadside",1)
                    if Girl == "Rogue":
                        ch_r "Couldn't we just take a normal swim?"
                    elif Girl == "Kitty":
                        ch_k "I don't think so. . ."
                    elif Girl == "Emma":
                        ch_e "Perhaps in a tub. . ."
                    elif Girl == "Laura":
                        ch_l "Nah. . ."
                    menu:
                        extend ""
                        "Ok, we can just use swimsuits.": 
                                $ Count = 0  
                                if Girl == "Rogue" and not R_Swim[0] and ("bikini top" not in R_Inventory or "bikini bottoms" not in R_Inventory):
                                        #if she doesn't own her swimsuit components. . .
                                        ch_r "I don't really have any swimsuit I could wear. . ."
                                elif Girl == "Kitty" and not K_Swim[0] and ("bikini top" not in K_Inventory or "bikini bottoms" not in K_Inventory or "blue skirt" not in K_Inventory):
                                        #if she doesn't own her swimsuit components. . .
                                        if "bikini top" in K_Inventory and "bikini bottoms" in K_Inventory:                                            
                                            if K_Inbt <= 400:
                                                ch_k "I don't know, I do have a suit, but it's a little daring. . ."
                                                ch_k "If only I had a little skirt or something. . ."                                                
                                        else:
                                                ch_k "I wish I had something cute to wear, but I don't. . ."
                                elif Girl == "Emma" and not E_Swim[0] and ("bikini top" not in E_Inventory or "bikini bottoms" not in E_Inventory):
                                        #if she doesn't own her swimsuit components. . .
                                        ch_e "I really don't own the proper attire. . ."
                                elif Girl == "Laura" and not L_Swim[0] and ("bikini top" not in L_Inventory or "bikini bottoms" not in L_Inventory):
                                        #if she doesn't own her swimsuit components. . .
                                        ch_l "Don't have a suit. . ."
                                else:
                                        if not CheckWord(Girl,"Recent","dip") and not CheckWord(Girl,"Recent","no dip"):
                                                call Statup(Girl, "Love", 80, 2)
                                                call Statup(Girl, "Obed", 50, 1)
                                                call Statup(Girl, "Inbt", 60, 2)
                                        call AnyFace(Girl,"smile")   
                                        if Girl == "Rogue":
                                            ch_r "Thanks, [R_Petname]."
                                        elif Girl == "Kitty":
                                            ch_k "Cool."
                                        elif Girl == "Emma":
                                            ch_e "That would be nice."
                                        elif Girl == "Laura":
                                            ch_l "Whatever."                               
                                        
                                        show blackscreen onlayer black 
                                        "She goes and changes into her suit. . ."
                                        call AnyOutfit(Girl,"swimwear") # puts on her swimsuit
                                        hide blackscreen onlayer black 
                                        call AnyWord(Girl,1,"no dip","no dip") #adds the "no tan" trait to recent and daily actions
                                        $ Count = 1
                                if not Count:
                                    #If she has no suit. . .
                                    menu:
                                        extend ""
                                        "Then what about your undies?":
                                            if ChestNum(Girl) > 2 and PantiesNum(Girl) > 2 and ApprovalCheck(Girl, 1000):
                                                #if she mostly likes you, and is wearing decent undies. . .
                                                pass
                                            elif ChestNum(Girl) > 1 and PantiesNum(Girl) > 1 and ApprovalCheck(Girl, 1200):
                                                #if she mostly likes you, and is wearing scandelous undies. . .
                                                pass
                                            else:       
                                                call AnyFace(Girl,"sly",1)             
                                                call AnyLine(Girl,"That's not going to work either.")                             
                                                call AnyWord(Girl,1,"no dip","no dip")
                                                return       
                                            call AnyFace(Girl,"smile",1)                                         
                                            if Girl == "Rogue":
                                                ch_r "Ok, fine. . ."
                                            elif Girl == "Kitty":
                                                ch_k "Fine, geez."
                                            elif Girl == "Emma":
                                                ch_e "I suppose. . ."
                                            elif Girl == "Laura":
                                                ch_l "Sure, whatever. . ."                                        
                                        "Ok then, never mind.":
                                                call AnyLine(Girl,"Thanks.") 
                                                call AnyWord(Girl,1,"no dip","no dip")
                                                return
                                    call AnyOutfit(Girl,7) # Takes off Over
                                    "She starts to strip down."
                                    call AnyOutfit(Girl,9) # Takes off Legs
                                    call AnyOutfit(Girl,13) # Takes off Hose
                                    "And ends up in her underwear."
                                    
                                    
                        "Never mind then.":                         
                                call Statup(Girl, "Love", 80, -1)
                                if not CheckWord(Girl,"Recent","dip") and not CheckWord(Girl,"Recent","no dip"):   
                                        call Statup(Girl, "Obed", 50, 2)
                                        call Statup(Girl, "Inbt", 60, 1)
                                if Girl == "Rogue":
                                    ch_r "Hmph."
                                elif Girl == "Kitty":
                                    ch_k "Bummer."
                                elif Girl == "Emma":
                                    ch_e "Disappointing."
                                elif Girl == "Laura":
                                    ch_l "K."
                                call AnyWord(Girl,1,"no dip","no dip") #adds the "no tan" trait to recent and daily actions
                                return
                    
            elif Line == "no":
                    #She is offended you even asked. . .
                    call Statup(Girl, "Love", 50, -5)
                    if not CheckWord(Girl,"Recent","dip") and not CheckWord(Girl,"Recent","no dip"):
                        call Statup(Girl, "Obed", 50, 2)
                        call Statup(Girl, "Inbt", 60, 1)
                    call AnyFace(Girl,"angry",1)
                    if Girl == "Rogue":
                        ch_r "Not interested, [R_Petname]. . ."
                    elif Girl == "Kitty":
                        ch_k "Not even."
                    elif Girl == "Emma":
                        ch_e "You must be dreaming. . ."
                    elif Girl == "Laura":
                        ch_l "Nope. . ."
                        
                    call AnyWord(Girl,1,"no dip","no dip") #adds the "no tan" trait to recent and daily actions
                    return
    
    if Girl == "Rogue":
            $ R_Water = 1
    elif Girl == "Kitty":
            $ K_Water = 1
    elif Girl == "Emma":
            $ E_Water = 1
    elif Girl == "Laura":
            $ L_Water = 1                     
    $ Round -= 10         
    "You both swim around for a bit."   
    
    return

#End girls skinnydip / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Girl_Caught_Shower(Girl=0):  
        if not Girl:
                return
        call Shift_Focus(Girl)
        
        call AnyWord(Girl,1,"showered","showered",0,0)
        call Remove_Girl("All")
        
        call AnyOutfit(Girl,"nude")
        call AnyFace(Girl,"smile",1) 
        
        if Girl == "Rogue":
                $ R_Loc = "bg showerroom"              
                $ R_Water = 1
                $ R_Wet = 2
        elif Girl == "Kitty":
                $ K_Loc = "bg showerroom"              
                $ K_Water = 1
                $ K_Wet = 2
        elif Girl == "Emma":
                $ E_Loc = "bg showerroom"              
                $ E_Water = 1   
                $ E_Wet = 2        
        elif Girl == "Laura":
                $ L_Loc = "bg showerroom"                
                $ L_Water = 1
                $ L_Wet = 2
                
        if (D20 >= 18 and ApprovalCheck(Girl,70,"X")) or (D20 >= 15 and ApprovalCheck(Girl,80,"X")):
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
                    call AnyOutfit(Girl,6)
                    return 1
                
        if Line == "knock":                                                                                         
                #You knock
                "You knock on the door. You hear some shuffling inside"    
                call AnyOutfit(Girl,7,TempOver="towel")  
                if (D20 >= 18 and ApprovalCheck(Girl,70,"X")) or (D20 >= 15 and ApprovalCheck(Girl,80,"X")):                                    
                        #Girl caught fapping
                        "You hear a sharp shuffling sound and the water gets cut off."
                        "After several seconds and some more shuffling, [Girl] comes to the door."
                        call AnyFace(Girl,"perplexed",2,Mouth="normal") 
                        call Set_The_Scene(Dress=0)
                        if Girl == "Rogue": 
                                ch_r "Sorry about that [R_Petname], I was. . . just wrapping up my shower."
                        elif Girl == "Kitty":
                                ch_k "Oh, hey, [K_Petname]. I was just. . . showering. Yeah."
                        elif Girl == "Emma": 
                                ch_e "Oh, hello [E_Petname]. I was. . . taking care of some personal business."
                        elif Girl == "Laura": 
                                ch_l "Oh, hey [L_Petname]. I was just. . . working off some stress."
                        call Statup(Girl, "Lust", 90, 5)
                        $ Tempmod += 10
                else:                                                                                                   
                        #Laura caught showering
                        "You hear the rustling of a towel and some knocking around, but after a few seconds [Girl] comes to the door."
                        call Set_The_Scene(Dress=0)
                        if Girl == "Rogue": 
                                ch_r "Sorry about that [R_Petname], I was just wrapping up my shower."
                        elif Girl == "Kitty":
                                ch_k "Oh, hey, [K_Petname]. I was just[K_like]showering."
                        elif Girl == "Emma": 
                                ch_e "Oh, hello [E_Petname]. I was just finishing my shower."
                        elif Girl == "Laura": 
                                ch_l "Oh, hey [L_Petname]. I was just finishing up."
                #end "knocked"
        else:                                                                                                       
            #You don't knock   
            if (D20 >= 18 and ApprovalCheck(Girl,70,"X")) or (D20 >= 15 and ApprovalCheck(Girl,80,"X")):  
                    #Caught masturbating in the shower. 
                    call AnyFace(Girl,"sexy",Eyes="closed")       
                    call AnyWord(Girl,1,"unseen","unseen",0,0) 
                    call Set_The_Scene(Dress=0)
                    $ Count = 0     
                    $ Trigger = "masturbation"
                    $ Trigger3 = "fondle pussy"   
                    "You see [Girl] under the shower, feeling herself up."
                    call expression Girl + "_SexAct" pass ("masturbate") #call Laura_SexAct("masturbate")   
                    jump Shower_Room
                
            elif D20 >= 15:                                                                                         
                    #She's just showering and naked
                    call Set_The_Scene(Dress=0)                
                    call AnyFace(Girl,"surprised", 1)
                    "As you enter the showers, you see [Girl] washing up."        
                    if not ApprovalCheck(Girl, 1200) or not SeenCheck(Girl):
                            call AnyFace(Girl,5,Brows="angry") #just updates brows 
                            call AnyOutfit(Girl,7,TempOver="towel")  
                            "She grabs a towel and covers up."             
                            call AnyFace(Girl,"angry", 1)
                            call Statup(Girl, "Love", 80, -5) 
                    else:
                            if ExhibitionistCheck(Girl):
                                call Statup(Girl, "Lust", 90, (2*D20)) 
                            else:
                                call Statup(Girl, "Lust", 80, D20)         
                            call AnyFace(Girl,5,Brows="confused") #just updates brows        
                    
                    call expression Girl + "_First_Bottomless" pass (1)
                    call expression Girl + "_First_Topless" pass (1)
                    call Statup(Girl, "Inbt", 70, 3)
                    if Girl == "Rogue": 
                            ch_r "Hey! Learn to knock maybe?!"
                    elif Girl == "Kitty":
                            ch_k "Did you[K_like]get a good look?"
                    elif Girl == "Emma": 
                            ch_e "Hello. Haven't you learned to knock before entering?"
                    elif Girl == "Laura": 
                            ch_l "Um, hey? Don't knock much?"
                    menu:
                            extend ""                            
                            "Sorry, I should have knocked.":  
                                    call Statup(Girl, "Love", 50, 2)
                                    call Statup(Girl, "Love", 80, 4)
                            "And miss the view?":
                                    call Statup(Girl, "Obed", 50, 2)
                                    call Statup(Girl, "Obed", 80, 2)
                                    call Statup(Girl, "Inbt", 60, 1)
                            "Why, would it have made a difference?": 
                                if not ApprovalCheck(Girl, 500,"I"):
                                    call Statup(Girl, "Love", 50, -3)
                                    call Statup(Girl, "Obed", 50, 2)
                                call Statup(Girl, "Obed", 80, 2)
                                call Statup(Girl, "Inbt", 60, 2)
                            "It's not as if you're leaving that much to the imagination. . ." if Girl == "Emma": 
                                call Statup("Emma", "Obed", 50, 2)
                                call Statup("Emma", "Obed", 80, 2)
                                call Statup("Emma", "Inbt", 60, 2)
                    #end caught showering naked
                
            else:                                                                                   
                    #She's done showering and in a towel
                    call AnyOutfit(Girl,7,TempOver="towel")  
                    call Set_The_Scene(Dress=0)
                    "As you enter the showers, you see Laura putting on a towel."        
                    if not ApprovalCheck(Girl, 1100) and not SeenCheck(Girl):          
                            call AnyFace(Girl,"angry",Brows="confused")
                            call Statup(Girl, "Love", 80, -5)
                    else:
                            call AnyFace(Girl,"sexy",Brows="confused")
                    call Statup(Girl, "Inbt", 50, 3)
                    if Girl == "Rogue": 
                            ch_r "Well hello there, [R_Petname]. Hoping to see something more?"
                    elif Girl == "Kitty":
                            ch_k "Oh, hey. Were you hoping I'd be naaaaaked?"
                    elif Girl == "Emma": 
                            ch_e "Oh, hello, [E_Petname]. Sorry you didn't get here sooner?"
                    elif Girl == "Laura": 
                            ch_l "Oh, hey [L_Petname]. Trying to slip in unnoticed?"
                    menu:
                            extend ""
                            "Sorry, I should have knocked.":   
                                    call Statup(Girl, "Love", 50, 2)
                                    call Statup(Girl, "Love", 80, 2)   
                            "Well, to be honest. . .":
                                    call Statup(Girl, "Love", 50, -2)
                                    call Statup(Girl, "Obed", 50, 2)
                                    call Statup(Girl, "Obed", 80, 2)
                                    call Statup(Girl, "Inbt", 60, 1)
                            "I still like the view. . ." if Girl != "Emma": 
                                if ApprovalCheck(Girl, 500,"I"):
                                    call Statup(Girl, "Love", 80, 1)
                                else:
                                    call Statup(Girl, "Love", 50, -1)
                                    call Statup(Girl, "Obed", 50, 2)
                                call Statup(Girl, "Obed", 80, 2)
                                call Statup(Girl, "Inbt", 60, 3)
                            "It's not as if you're leaving that much to the imagination. . ." if Girl == "Emma": 
                                call Statup("Emma", "Obed", 50, 2)
                                call Statup("Emma", "Obed", 80, 2)
                                call Statup("Emma", "Inbt", 60, 2)
                    #end caught in towel
                        
            call AnyFace(Girl,"sexy")          
            if not ApprovalCheck(Girl, 750) and SeenCheck(Girl) <= 3:
                    if Girl == "Rogue": 
                            ch_r "Well, it happens, just be careful next time."
                    elif Girl == "Kitty":
                            ch_k "Well, it's not like I totally mind. . ." 
                    elif Girl == "Emma": 
                            ch_e "Hmm. Yes, a likely excuse."
                    elif Girl == "Laura":   
                            ch_l "Well, just keep an eye on your own bits."
                            ch_l "Wouldn't want them going missing."
            elif not ApprovalCheck(Girl, 1300):                 
                    if Girl == "Rogue": 
                            ch_r "Well, it happens, just be careful next time."
                    elif Girl == "Kitty":
                            ch_k "Well too bad." 
                    elif Girl == "Emma": 
                            ch_e "Hmm. Yes, a likely excuse."
                    elif Girl == "Laura":   
                            ch_l "Uh-huh."
            else:                
                
                    if Girl == "Rogue": 
                            ch_r "You could have just asked, [R_Petname]."   
                    elif Girl == "Kitty":
                            ch_k "Well, it's not like it's totally off the table. . ." 
                    elif Girl == "Emma": 
                            ch_e "Well, it's not that I mind. . ."
                    elif Girl == "Laura":   
                            ch_l "Nah, I don't mind much. . ."
                            
                    if OverNum(Girl) == 3: 
                        #if she's wearing a towel. . .       
                        call AnyOutfit(Girl,7) #removes towel  
                        pause 0.5               
                        call AnyOutfit(Girl,7,TempOver="towel")  
                        "She flashes you real quick."    
                        call AnyOutfit(Girl,7,TempOver="towel")  
                        call expression Girl + "_First_Bottomless" pass (1)
                        call expression Girl + "_First_Topless" pass (1) #same as "call Rogue_First_Topless(1)"
                        
                        if Girl == "Laura":   
                                ch_l "Heh!" 
                                                          
            #end didn't knock
        
        if Girl == "Rogue": 
                ch_r "Well, I should probably get going. . ." 
        elif Girl == "Kitty":
                ch_k "I'm done here, see you later?" 
        elif Girl == "Emma": 
                ch_e "I should probably be leaving. . ."
        elif Girl == "Laura":                    
                ch_l "I should get going. . ." 
        menu:
            extend ""
            "Sure, see you later then.":
                    call Remove_Girl(Girl)
            "Actually, could you stick around a minute?":
                if ApprovalCheck(Girl, 900):
                    if Girl == "Rogue":        
                            ch_r "Sure, what's up?"
                    elif Girl == "Kitty":        
                            ch_k "Yeah?"
                    elif Girl == "Emma": 
                            ch_e "Very well, what did you need?"
                    elif Girl == "Laura": 
                            $ L_Loc = "bg showerroom"            
                            ch_l "Huh? Ok, what's up?"
                else:
                    
                    if Girl == "Rogue": 
                            ch_r "Um, actually, I'm not really comfortable being so. . . exposed?"
                            ch_r "I'll just see you around later."
                    elif Girl == "Kitty":
                            ch_k "I'm[K_like]totally exposed here?"
                            ch_k "I'm just going to head out."
                    elif Girl == "Emma": 
                            ch_e "I really shouldn't be \"hanging out\" in such a state."
                            ch_e "We can talk later."
                    elif Girl == "Laura": 
                            ch_l "I probably shouldn't hang out like this."
                            ch_l "We'll talk later."
                    call Remove_Girl(Girl)  
        
        if Line == "leaving":
                call AnyOutfit(Girl,6)
                call AnyOutfit(Girl,6)
        $ Line = 0
        return 0
# End Girl Caught Shower / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Love You Girl / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /   
label Love_You(Girl=0):
        # Called whenever you say "I love you" in the flirt menu
        # Rejects attempts before the girl confesses
                 
        ch_p "[Girl], I love you."
        if not CheckWord(Girl,"Petnames","lover"):
            #if you didn't clear the love scene with her. . .
            if CheckWord(Girl,"History","love"):
                    #you've tried this before. . .   
                    if ApprovalCheck(Girl, 800,"L"):
                            #she kind of likes you
                            call Statup(Girl, "Love", 90, 2)
                            call Statup(Girl, "Obed", 80, 2)
                            call Statup(Girl, "Inbt", 60, 1)
                            call Statup(Girl, "Lust", 30, 5)
                            call AnyFace(Girl,"bemused",2,Brows="confused")   
                            
                            if Girl == "Rogue":
                                    ch_r "Don't push it. . ."
                            elif Girl == "Kitty":
                                    ch_k "I can't even . ."
                            elif Girl == "Emma":
                                    ch_e "Just don't. . ."    
                            elif Girl == "Laura":
                                    ch_l "I don't want to. . ."
                            
                    elif ApprovalCheck(Girl, 600,"L"):
                            #she is friendly enough. . .
                            call Statup(Girl, "Love", 95, 2)
                            call Statup(Girl, "Obed", 80, 3)
                            call Statup(Girl, "Inbt", 60, 1)
                            call AnyFace(Girl,"bemused",2)   
                            
                            if Girl == "Rogue":
                                    ch_r "I don't know, love? . ."
                            elif Girl == "Kitty":
                                    ch_k "I don't know if I think of you like that . ." 
                            elif Girl == "Emma":
                                    ch_e "This is incredibly inappropriate. . ."
                            elif Girl == "Laura":
                                    ch_l "I don't. . ."
                    else:
                            #she doesn't like you. . .
                            call Statup(Girl, "Love", 95, -5)
                            call Statup(Girl, "Obed", 90, 5)
                            call Statup(Girl, "Inbt", 60, 2)
                            call AnyFace(Girl,"angry",1)   
                            
                            if Girl == "Rogue":
                                    ch_r "Bull."
                            elif Girl == "Kitty":
                                    ch_k "Stop trolling me!"
                            elif Girl == "Emma":
                                    ch_e "Oh forget this nonsense already. . ."  
                            elif Girl == "Laura":
                                    ch_l "Fuck off with this. . ."   
                            
            #if this is the first time you've tried this but you haven't agreed to love her yet. . .
            call AnyWord(Girl,1,"love","love",0,"love") #adds the "love" trait to recent and daily actions, and history
            
            if Girl == "Rogue":
                    if not R_Event[6]:
                            # if you've never had the "love" talk. . .
                            $ Line = "never"                    
                    elif R_Event[6] >= 20: 
                            # if she's asked you, but you refused before. . .
                            ch_r "You're just giving me whiplash here, [R_Petname]."
#                            call Rogue_Love_Redux #she doesn't have one of these, skip it.
            elif Girl == "Kitty":
                    if not K_Event[6]:
                            $ Line = "never"                    
                    elif K_Event[6] >= 20: 
                            call Kitty_Love_Redux
            elif Girl == "Emma":
                    if not E_Event[6]:
                            # if you've never had the "love" talk. . .
                            $ Line = "never"                    
                    elif E_Event[6] >= 20: 
                            call Emma_Love_Redux
            elif Girl == "Laura":
                    if not L_Event[6]:
                            $ Line = "never"                    
                    elif L_Event[6] >= 20: 
                            call Laura_Love_Redux
                    
            if Line == "never":
                    if ApprovalCheck(Girl, 800,"L"):
                            call Statup(Girl, "Love", 90, 10)
                            call Statup(Girl, "Lust", 50, 5)
                            call AnyFace(Girl,"smile",2,Eyes="surprised")   
                    elif ApprovalCheck(Girl, 600,"L"):
                            call Statup(Girl, "Love", 90, 5)
                            call AnyFace(Girl,"confused",2,Eyes="surprised")   
                    else:
                            call AnyFace(Girl,"angry",1,Brows="confused")   
                            call Statup(Girl, "Love", 90, -5)
                            call Statup(Girl, "Obed", 90, 5)
                    call Statup(Girl, "Obed", 70, 5)
                    call Statup(Girl, "Inbt", 60, 5)
                    if Girl == "Rogue":
                            ch_r "Whaaa? . ."
                            ch_r "Is this some kind of joke?"   
                    elif Girl == "Kitty":
                            ch_k "What was that? . ."
                            ch_k ". . . Um, I gotta go!"   
                    elif Girl == "Emma":
                            ch_e "What? I. . . I don't know what to say about that."
                            ch_e "I. . . I'll get back to you."     
                    elif Girl == "Laura":
                            ch_l "Huh? You-"
                            ch_l "Um. . ."   
                            ch_l "Bye."
                    
                    "[Girl] leaves the room."
                    call Remove_Girl(Girl)
                    $ renpy.pop_call() #This removes the callback to the previous chat session
                    $ renpy.pop_call() #this removes the callback to the previous chat selector
            return
        # End if you never cleared the love scene stuff        
                
        if CheckWord(Girl,"Daily","love"):
                #if you've said it today
                call Statup(Girl, "Love", 95, 5)
                call Statup(Girl, "Obed", 70, 2)
                call Statup(Girl, "Inbt", 60, 1)
                call Statup(Girl, "Lust", 50, 5)                
                call AnyFace(Girl,"smile",1)   
                if Girl == "Rogue":
                        ch_r "I think you told me that earlier. . ."
                        ch_r "but don't stop on my account, [R_Petname]."   
                elif Girl == "Kitty":
                        ch_k "Didn't you already say that? . ."
                        ch_k ". . . say it again."   
                elif Girl == "Emma":
                        ch_e "So you've told me. . ."
                        ch_e "but I don't tire of it, [E_Petname]."   
                elif Girl == "Laura":
                        ch_l "Yeah, I know. . ."
                        ch_l "but you can keep saying it, [L_Petname]."   
                
        elif ApprovalCheck(Girl, 800,"L"):
                #if she still loves you
                call Statup(Girl, "Love", 90, 5)
                call Statup(Girl, "Love", 200, 5)
                call Statup(Girl, "Obed", 70, 1)
                call Statup(Girl, "Inbt", 60, 1)
                call Statup(Girl, "Lust", 30, 5)     
                call AnyFace(Girl,"smile",1)              
                if Girl == "Rogue":
                        ch_r "I love you too, [R_Petname]."
                elif Girl == "Kitty":
                        ch_k "Awwww! I love you too, [K_Petname]."
                elif Girl == "Emma":
                        ch_e "And I love you too, [E_Petname]."
                elif Girl == "Laura":
                        ch_l "Yeah, love you too."
        else:
                #if she doesn't love you anymore
                call Statup(Girl, "Love", 90, 5)
                call Statup(Girl, "Love", 50, -10, 1)
                call Statup(Girl, "Obed", 70, 3)        
                call AnyFace(Girl,"sadside",1)        
                if Girl == "Rogue":
                        ch_r "It's too late for that."
                elif Girl == "Kitty":
                        ch_k "As if. Jerk."
                elif Girl == "Emma":
                        ch_e "I dearly wish that I could believe that."
                elif Girl == "Laura":
                        ch_l "You blew it."
        
        call AnyWord(Girl,1,"love","love",0,"love") #adds the "love" trait to recent and daily actions, and history
        return
    
 
# End Love You Girl / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /   
    
    