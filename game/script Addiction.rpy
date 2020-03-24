# Event First_Addicted /////////////////////////////////////////////////////
label First_Addicted(Girl=0):
        # Girl.Event[1] starts at zero, +1 each time, jumps to 10 if you agree to help her
        call Set_The_Scene
        call Shift_Focus(Girl)
        $ Girl.Event[1] += 1
        $ MultiAction = 0
        
        call Locked_Door(Girl)
        if not _return:
                #if the door is locked and you refused entry. . .
                return
        if bg_current != "bg player":
                if Girl.Loc == bg_current or Girl in Party:
                        "Out of the blue, [Girl.Name] says she wants to talk to you in your room and drags you over there."
                else:
                        "[Girl.Name] shows up, hurridly says she wants to talk to you in your room and drags you over there."
        else:
                if Girl.Loc == bg_current or Girl in Party:
                        "[Girl.Name] turns to you with a bit of a dazed look."
                else:            
                        "[Girl.Name] barges into your room in a tizzy."
        $ Taboo = 0
        $ Girl.Taboo = 0
        $ bg_current = "bg player"
        $ Girl.Loc = bg_current    
        $ Girl.OutfitChange(Changed=1)
        call Set_The_Scene    
        call CleartheRoom(Girl)
        
        if Girl.Event[1] == 1:
                #first time through. . .
                if Girl == RogueX:
                        $ Girl.FaceChange("bemused")
                        ch_r "Oh, hey there [Girl.Petname]. You seem to be fitting in well. . ."
                        if not Girl.Kissed:
                            ch_r "Look, since the other day when I first. . . touched you,"
                        else:
                            ch_r "Look, since the other day when I first. . . kissed you,"
                        ch_r "I've had this kind of. . . buzz. At first I thought it was just from finally being able to touch someone,"
                        $ Girl.Eyes = "sexy"
                        ch_r "But I think maybe. . . could I touch you again?"
                elif Girl == KittyX:
                        $ Girl.FaceChange("bemused",2)
                        ch_k "Oh. . . hey, [Girl.Petname]. I've been thinking. . ."
                        if not Girl.Kissed:
                            ch_k "Look, since a while back when I first. . . touched you,"
                        else:
                            ch_k "Look, since a while back when I first. . . kissed you,"
                        ch_k "I've kinda been thinking. . . feeling a little odd. . ."
                        $ Girl.Eyes = "side"
                        ch_k "Would you mind if I touched you again real quick?"
                elif Girl == EmmaX:
                        $ Girl.FaceChange("bemused")
                        ch_e "Oh, hello [Girl.Petname]. . ."
                        ch_e "You've been doing well in your studies, it seems. . ."
                        ch_e "Look, since the other day when we first. . . came into contact. . ."
                        $ Girl.FaceChange("sadside",1,Brows="angry")
                        ch_e "I've been. . . struggling with something."
                        ch_e "A feeling. . ."
                        $ Girl.Eyes = "sexy"
                        ch_e "I was thinking perhaps that. . . touching you again might help?"
                elif Girl == LauraX:
                        $ Girl.FaceChange("bemused")
                        ch_l "Oh, hey, [Girl.Petname]."
                        ch_l "You think maybe I could touch you again?"
                        menu:
                            extend ""
                            "Ok?":
                                ch_l "Cool."
                            "Why":
                                ch_l "Oh. . . no reason."
                                ch_l "I just sort of feel a little jumpy, and wanted to try something." 
        #end "first intro"
                    
                    
        elif Girl.Event[1] == 2:
                        jump First_Addicted2
        else:
                        jump First_Addicted3 
        menu:
            extend ""
            "Another kiss?" if Girl.Kissed:
                    if ApprovalCheck(Girl, 660, "LI",Alt=[[RogueX],560]):
                            $ Girl.Statup("Lust", 80, 3)
                            $ Girl.Statup("Love", 80, 6)
                            $ Girl.FaceChange("sexy")
                            if Girl == RogueX:
                                    ch_r "Yeah, sure, pucker up, [Girl.Petname]."
                            elif Girl == KittyX:
                                    ch_k "Um, yeah!"
                            elif Girl == EmmaX:
                                    ch_e "Took the words out of my mouth, [Girl.Petname]."
                            elif Girl == LauraX:
                                    ch_l "Sure, I'm in."
                            "She leans in for another kiss."
                            call KissPrep
                    else:
                            $ Girl.FaceChange("sad",2)
                            if Girl == RogueX:
                                    ch_r "I don't think so, [Girl.Petname]."
                            elif Girl == KittyX:
                                    ch_k "Um, no thanks."
                            elif Girl == EmmaX:
                                    ch_e "I don't think that would be appropriate right now."
                            elif Girl == LauraX:
                                    ch_l "Um, no thanks."
                            jump Addicted_Bad_End   
            "How about a kiss?" if not Girl.Kissed:
                    if ApprovalCheck(Girl, 660, "LI",Alt=[[RogueX],560]):
                            $ Girl.Statup("Lust", 80, 3)
                            $ Girl.Statup("Love", 80, 6)
                            $ Girl.FaceChange("bemused",1)
                            if Girl == RogueX:
                                    ch_r "Yeah, sure, let's do that."  
                            elif Girl == KittyX:
                                    ch_k "What? Oh, um, ok. . ."
                            elif Girl == EmmaX:
                                    ch_e "Oh, well. . . I suppose we could do that. . ."
                            elif Girl == LauraX:
                                    ch_l "Oh. . . I guess, sure."  
                            "She leans in for a kiss."
                            call KissPrep   
                    else:
                            $ Girl.FaceChange("sad",2)
                            if Girl == RogueX:
                                    ch_r "I don't think so, [Girl.Petname]."
                            elif Girl == KittyX:
                                    ch_k "Um, no thanks."
                            elif Girl == EmmaX:
                                    ch_e "I don't think that would be appropriate right now."
                            elif Girl == LauraX:
                                    ch_l "Um, no thanks."
                            jump Addicted_Bad_End   
            "Sure, if it would make you feel better.":
                    if ApprovalCheck(Girl, 700, "LI",Alt=[[RogueX],600]):
                            $ Girl.Statup("Lust", 80, 3)
                            $ Girl.Statup("Love", 90, 1)
                            $ Girl.Statup("Love", 80, 3)
                            $ Girl.Statup("Love", 50, 4)
                            $ Girl.FaceChange("sexy")                            
                            if Girl == RogueX:
                                    ch_r "I've got an idea for that."
                            elif Girl == KittyX:
                                    ch_k "Good, because I have an idea. . ."
                            elif Girl == EmmaX:
                                    ch_e "Well, we may as well enjoy the experience. . ."
                            elif Girl == LauraX:
                                    ch_r "Cool."
                            "She leans in for a kiss."
                            call KissPrep
                    else:
                            $ Girl.Statup("Lust", 80, 3)
                            $ Girl.Statup("Love", 90, 1)
                            $ Girl.Statup("Love", 80, 3)
                            $ Girl.Statup("Love", 50, 4)
                            $ Girl.FaceChange("smile")
                            call Girl_Tag(Girl)
                        
            "What, you just want to touch my face? No thanks.":
                    if ApprovalCheck(Girl, 500, "L",Alt=[[RogueX],400]) or Girl.Kissed:
                            $ Girl.Statup("Love", 200, -3)
                            $ Girl.Statup("Inbt", 50, 3)
                            $ Girl.Brows = "confused"
                            $ Girl.Eyes = "surprised"
                            $ Girl.Mouth = "sad"
                            if Girl == RogueX:
                                    ch_r "Well, how 'bout if I gave you a kiss?"
                            elif Girl == KittyX:
                                    ch_k "Well. . .I could give you a kiss?"
                            elif Girl == EmmaX:
                                    ch_e "Would you be interested in. . . a kiss?"
                            elif Girl == LauraX:
                                    ch_l "Then. . . wanna make out a little?"
                            menu:  
                                extend ""
                                "Sure, that'll do.":                        
                                        $ Girl.Statup("Lust", 80, 3)
                                        $ Girl.Statup("Love", 80, 5)
                                        $ Girl.FaceChange("sexy")
                                        "She leans in for a kiss."
                                        call KissPrep       
                                "Only if we can make out a bit." if Girl != LauraX:
                                        $ Girl.Statup("Love", 80, 3)
                                        $ Girl.Statup("Obed", 40, 5)
                                        $ Girl.FaceChange("sexy")
                                        if Girl == RogueX:
                                                ch_r "Fine, we can do that."
                                        elif Girl == KittyX:
                                                ch_k "Sure, that counds good."
                                        elif Girl == EmmaX:
                                                ch_e "I don't see why not."      
                                        call KissPrep                    
                                "Not good enough.":                        
                                        $ Girl.Statup("Love", 200, -5)                                             
                                        $ Girl.Brows = "angry"
                                        $ Count2 = 3        
                                        call Addicted_Ultimatum
                    else:                       
                                        $ Girl.Brows = "angry"  
                                        $ Count2 = 2                   
                                        call Addicted_Ultimatum
        jump First_Addicted_End
          
# End Event First_Addicted /////////////////////////////////////////////////////

# Event First_Addicted2 /////////////////////////////////////////////////////  
label First_Addicted2:  
        # jump to from First_Addicted       
        $ Girl.FaceChange("manic")
        if Girl == RogueX:
                ch_r "Ok, so remember the other day, when I wanted to touch you, but you refused?"
        elif Girl == KittyX:
                ch_k "Hey, remember when I wanted to touch you, but you were[Girl.like]\"no way?\""
        elif Girl == EmmaX:
                ch_e "Do you recall a while back, I wanted to touch you, and you refused me?"
        elif Girl == LauraX:
                ch_l "Hey, Remember the other day when you wouldn't let me touch you?"
        menu:
            extend ""
            "Yeah. . .":
                pass
            "Not really. . .":
                $ Girl.Brows = "angry"
                $ Girl.Statup("Love", 80, -3)
                $ Girl.Statup("Obed", 80, 3)   
        if Girl == RogueX:
                ch_r "Well I can't take it anymore, I feel this. . . craving to touch you again and it's driving me nuts."
        elif Girl == KittyX:
                ch_k "Well. . . I just toss and turn all night, I'm really uncomfortable."
        elif Girl == EmmaX:
                ch_e "Well it seems to be getting worse."
                ch_e "I just can't seem to keep my mind off of it."
        elif Girl == LauraX:   
                ch_l "I'm really uncomfortable. I really think it would help if I could touch you real quick."
        menu:
            extend ""
            "That's terrible. Have you seen a doctor?":
                    $ Girl.Statup("Love", 80, 5)
                    $ Girl.Statup("Obed", 80, 3)                        
                    if Girl == RogueX:
                            ch_r "That's sweet of you, yes. Doc McCoy said that he couldn't determine a cause. . ."
                            ch_r "but I think it has something to do with your touch."
                    elif Girl == KittyX:
                            ch_k "Aw, that's sweet. Doc McCoy said that he couldn't figure out a cause. . ."
                            ch_k "I do think touching you is important, somehow."
                    elif Girl == EmmaX:
                            ch_e "That's sweet of you to ask, yes. Henry was unable to determine a cause for it. . ."
                            ch_e "I believe it has something to do with your touch."
                    elif Girl == LauraX:
                            ch_l "Oh, yeah. McCoy said he couldn't figure it out. . ."
                            ch_l "I think it has something to do with your touch."
            "Serves you right.":
                    $ Girl.Brows = "angry"
                    $ Girl.Mouth = "sad"
                    $ Girl.Statup("Love", 80, -7)
                    $ Girl.Statup("Obed", 80, 5)
                    if Girl == RogueX:
                            ch_r "Ass!"
                    elif Girl == KittyX:
                            ch_k "Jerk!"
                    elif Girl == EmmaX:
                            ch_e "Boar."
                    elif Girl == LauraX:
                            ch_l "Jackass."
            "Are you a pirate?" if Girl == RogueX: 
                    $ Girl.Brows = "confused"
                    $ Girl.Statup("Love", 80, 3)
                    $ Girl.Statup("Obed", 80, 3)   
                    ch_r "Arrr. Love a guy with a sense of humor."
            "I have that effect on people." if Girl != RogueX: 
                    $ Girl.Brows = "confused"
                    $ Girl.Statup("Love", 80, 3)
                    $ Girl.Statup("Obed", 80, 3)   
                    if Girl == KittyX:
                            ch_k "Hehe, um, yeah. . ."
                    elif Girl == EmmaX:
                            ch_e "I suppose I don't want to know how you know that. . ."
                    elif Girl == LauraX:
                            ch_l "Seriously?" 
                            ch_l "Have -you- looked into that?"                
        $ Girl.FaceChange("bemused")                          
        if Girl == RogueX:
                ch_r "I've just been feeling a bit weird since we last touched, shaky, buzzed. I can't concentrate on anything."    
                ch_r ". . .Anyway, I've reconsidered your. . . offer. I'm willing to be a bit . . . flexible here."
        elif Girl == KittyX:
                ch_k "Anyway, it's a real hassle. . . I haven't been able to concentrate well. . ."
                ch_k "I'd really appreciate if you could help me out here. . ."
        elif Girl == EmmaX:
                ch_e "Yes, well, I haven't been able to get my work done lately, I feel very foggy."
                ch_e "I would certainly be willing to offer some sort of. . . compensation. . ."
        elif Girl == LauraX:
                ch_l "Yeah, so I've been off my game, missing a lot of easy hits." 
                ch_l "Could you throw me a bone here?"
        $ Count2 = 2
        call Addicted_Ultimatum
        jump First_Addicted_End
    
    
# Event First_Addicted3 /////////////////////////////////////////////////////  
label First_Addicted3: 
        # jump to from First_Addicted
        $ Girl.Event[1] += 1
        if Girl == RogueX:
                ch_r "Ok, I've given you plenty of chances here. . . Plenty."    
                ch_r "This is driving me crazy, it's like I have a full body itch that I can't scratch."
        elif Girl == KittyX:
                ch_k "Ok[Girl.like]seriously, this is getting nuts."
                ch_k "I have been SUPER patient so far, and enough is enough."
        elif Girl == EmmaX:
                ch_e "You have to understand, [Girl.Petname], this is incredibly uncomfortable."
                ch_e "I haven't had a full night's sleep in a while now, it's quite unbearable." 
        elif Girl == LauraX:
                ch_l "Hey, I don't know what the deal is here, but I don't like it."
                ch_l "Cut me some slack here, or I'll cut it myself."
        menu:
            extend ""
            "And Dr. McCoy hasn't been able to find a cause?":
                    $ Girl.Statup("Love", 80, 5)
                    $ Girl.Statup("Obed", 50, 3)                        
                    if Girl == RogueX:
                            ch_r "Nothing! He's run all sorts of tests, and nothing's come up!"
                            ch_r "It has to be you, something about your touch, your mutant power."
                    elif Girl == KittyX:
                            ch_k "Nothing! Test after test, and nothing so far!"
                            ch_k "It has to be you, something about your touch, your mutant power."
                    elif Girl == EmmaX:
                            ch_e "No! I am at my whit's end with that man, so many pointless tests."
                            ch_e "I know it's something about you, about your touch, your mutant power."
                    elif Girl == LauraX:
                            ch_l "No! I haven't been poked and prodded so much in years, but nothing so far."
                            ch_l "I figure it has to be your powers or something."
            "Well, I did make some tempting offers. . .":
                    $ Girl.Brows = "angry"
                    $ Girl.Mouth = "sad"
                    $ Girl.Statup("Love", 80, -7)
                    $ Girl.Statup("Obed", 80, 5)
                    if Girl == RogueX:
                            ch_r "Yeah, very tempting."   
                    elif Girl == KittyX:
                            ch_k "Yeah, um. . . sure."
                    elif Girl == EmmaX:
                            ch_e "I suppose I may have reconsidered. . ."
                    elif Girl == LauraX:   
                            ch_l "Yeah, I mean now they might be. . ."
        $ Girl.Brows = "angry"
        $ Girl.Mouth = "sad"
        $ Girl.Blush = 1    
                        
        if Girl == RogueX:
                ch_r "So. . .I need this to end. I need to figure this out. I'll do anything here."
        elif Girl == KittyX:
                ch_k "So[Girl.like]can we do something here or what?"
        elif Girl == EmmaX:
                ch_e "I may be a bit more. . . flexible in my negotiations. . ."
        elif Girl == LauraX:  
                ch_l "I'm open to suggestions here."
        $ Count2 = 2
        call Addicted_Ultimatum
        jump First_Addicted_End
    
# end Event First_Addicted3 /////////////////////////////////////////////////////


label Addicted_Ultimatum(AddictStore=Girl.Addict):
        #Called when you demand something for a touch. . .
        #either returns and then jumps to a good ending, or jumps to bad ending
        $ Girl.AddWord(1,"ultimatum","ultimatum") #adds to recent and daily
        $ Tempmod = int(Girl.Addict/2)
        if Girl.Addict >= 80:
                    $ Count2 += 2
        elif Girl.Addict >= 50:
                    $ Count2 += 1
                            
        if Girl == RogueX:
                if Girl.Event[1] == 1:     
                        ch_r "Fine then, what would work for you?"
                else:
                        ch_r "What do I need to do for another touch?"
        elif Girl == KittyX:
                if Girl.Event[1] == 1:     
                        ch_k "So[Girl.Like]what do you want?"
                else:
                        ch_k "Ok, so what'll it take to get another hit?"
        elif Girl == EmmaX:
                if Girl.Event[1] == 1:     
                        ch_e "Very well, what is it that you want?"
                else:
                        ch_e "What would it take then?"
        elif Girl == LauraX:  
                        ch_l "Ok, fine, what do you want?"  
                            
        while Count2:
            $ CountStore = Tempmod        
            if not ApprovalCheck(Girl, 1200, "LO"):
                    $ Girl.Forced = 1               
            menu Addict_Ultimatum_Menu:
                extend ""
                "Nothing, just touch whatever you like.":
                        $ Girl.Forced = 0   
                        if Girl.Petname in ("master", "sir"):           
                                $ Girl.Statup("Lust", 80, 3)
                                $ Girl.Statup("Love", 70, 1)
                                $ Girl.Statup("Love", 95, 1)
                                $ Girl.FaceChange("sexy")
                                if Girl == RogueX:
                                        ch_r "Thank you, [Girl.Petname]."
                                elif Girl == KittyX:
                                        ch_k "Oh, thank you."
                                elif Girl == EmmaX:
                                        ch_e "Oh, appreciated."
                                elif Girl == LauraX:
                                        ch_l "Thank you, [Girl.Petname]."
                                "She leans in for a kiss."
                                call KissPrep
                        elif ApprovalCheck(Girl, 650, "LI",Alt=[[RogueX],600]):
                                $ Girl.Statup("Lust", 80, 3)
                                $ Girl.Statup("Love", 80, 5)
                                $ Girl.FaceChange("sexy")
                                if Girl == RogueX:
                                        ch_r "I've got an idea for that."
                                elif Girl == KittyX:
                                        ch_k "Oh, cool."
                                elif Girl == EmmaX:
                                        ch_e "Thank you, [Girl.Petname]"                                        
                                elif Girl == LauraX:
                                        ch_l "Ok, cool."                                
                                "She leans in for a kiss."
                                call KissPrep
                        else:
                                $ Girl.Statup("Lust", 80, 3)
                                $ Girl.Statup("Love", 80, 6)
                                $ Girl.FaceChange("smile")
                                call Girl_Tag(Girl)
                        $ Girl.Addict = 20 if Girl.Addict > 20 else Girl.Addict
                    
                "How about a kiss?":
                        if Girl.Kissed or ApprovalCheck(Girl, 600, "LI",Alt=[[RogueX],560]) or Girl.Petname in ("master", "sir"):
                                $ Girl.Forced = 0   
                                $ Girl.Statup("Lust", 80, 3)
                                $ Girl.Statup("Love", 80, 6)
                                $ Girl.FaceChange("sexy")
                                if Girl == RogueX:
                                        ch_r "That all? Yeah, sure, let's do that."  
                                elif Girl == KittyX:
                                        ch_k "Oh, um, ok, sure."
                                elif Girl == EmmaX:
                                        ch_e "I suppose we could. . ."
                                elif Girl == LauraX:
                                        ch_l "Yeah, ok."   
                                "She leans in for a kiss."
                                call KissPrep   
                                $ Girl.Addict = 20 if Girl.Addict > 20 else Girl.Addict
                        else:
                                if Girl == RogueX:
                                        ch_r "That's kinda personal."  
                                elif Girl == KittyX:
                                        ch_k "I don't know. . ."
                                elif Girl == EmmaX:
                                        ch_e "I don't think that would be appropriate. . ."
                                elif Girl == LauraX:
                                        ch_l "Eh. . . nah."  
                
                "How about you let me touch you instead?":
                        if Girl == RogueX:
                                ch_r "That depends, [Girl.Petname]. Where were you thinking?"  
                        elif Girl == KittyX:
                                ch_k "I don't know[Girl.like]what were you thinking, [Girl.Petname]?"
                        elif Girl == EmmaX:
                                ch_e "I'm not sure, [Girl.Petname]. What did you have in mind?"
                        elif Girl == LauraX: 
                                ch_l "So, what were you thinking here?"
                        menu:                   
                            extend ""
                            "How about I give you a full contact back massage?":
                                    $ CountStore = Tempmod
                                    call Top_Off(Girl,0) 
                                    $ Tempmod = CountStore
                                    if not Girl.Over and "no topless" not in Girl.RecentActions:        
                                                    $ Girl.Statup("Obed", 50, 3)
                                                    $ Girl.Statup("Inbt", 50, 3)
                                                    call Massage_Prep(Girl)
                                    elif "no topless" in Girl.RecentActions: 
                                        if Girl == RogueX:
                                                ch_r "Look, we can still do this, so long as I can touch you after."
                                        elif Girl == KittyX:
                                                ch_k "Even with my top on, we can still do this. . ."
                                        elif Girl == EmmaX:
                                                ch_e "I think we can manage with my top left on. . ."
                                        elif Girl == LauraX:
                                                ch_l "We can still do something here. . ."
                                        menu:
                                            extend ""
                                            "Sure, ok.":
                                                    $ Girl.Statup("Obed", 50, 5)
                                                    $ Girl.Statup("Inbt", 50, 5)
                                                    call Massage_Prep(Girl)
                                                    "[Girl.Name] gets back up."
                                                    call Girl_Tag(Girl)       
                                            "Nope, not worth it.":
                                                    if Girl == RogueX:
                                                            ch_r "Fine then! What else?"
                                                    elif Girl == KittyX:
                                                            ch_k "Well!"
                                                    elif Girl == EmmaX:
                                                            ch_e "Pity. Any other ideas?"
                                                    elif Girl == LauraX:
                                                            ch_l "Ok."
                                                    
                                    else:
                                                    $ Girl.Statup("Obed", 50, 5)
                                                    $ Girl.Statup("Inbt", 50, 5)                        
                                                    if Girl == RogueX:
                                                            ch_r "Ok, but after we do this, I get a little touch too."
                                                    elif Girl == KittyX:
                                                            ch_k "Sure, but after this, I'll still need to touch you."
                                                    elif Girl == EmmaX:
                                                            ch_e "Fine, but I will still need some other contact."
                                                    elif Girl == LauraX:
                                                            ch_l "Yeah, but, I'll need to touch you after this."
                                                    call Massage_Prep(Girl)
                                                    "[Girl.Name] gets back up."
                                                    call Girl_Tag(Girl)             
                            #end massage
                            
                            "How about you let me touch your breasts?":
                                    $ CountStore = Tempmod
                                    call Top_Off(Girl,0)   
                                    $ Tempmod = CountStore
                                    call expression Girl.Tag + "_Fondle_Breasts"
                                    if "fondle breasts" in Girl.RecentActions:
                                            $ Girl.Statup("Obed", 80, 10)
                                            $ Girl.Statup("Inbt", 80, 10)
                                            if Girl == RogueX:
                                                    ch_r "I hope that was enough."
                                            elif Girl == KittyX:
                                                    ch_k "Was that good enough for you?"
                                            elif Girl == EmmaX:
                                                    ch_e "I imagine that was plenty."
                                            elif Girl == LauraX:         
                                                    ch_l "That was enough, right?"
                                
                            "How about you just let me touch your thighs?":            
                                    $ CountStore = Tempmod          
                                    call Bottoms_Off(Girl,0)               
                                    $ Tempmod = CountStore
                                    if Girl.PantsNum() > 6 or Girl.HoseNum() >= 5:
                                            if Girl == RogueX:
                                                    ch_r "Ok, but after we do this, I get a little touch too."
                                            elif Girl == KittyX:
                                                    ch_k "Sure, but after this, I'll still need to touch you."
                                            elif Girl == EmmaX:
                                                    ch_e "Fine, but I will still need some other contact."
                                            elif Girl == LauraX:
                                                    ch_l "Yeah, but, I'll need to touch you after this."
                                    call expression Girl.Tag + "_Fondle_Thighs"
                                    if "fondle thighs" in Girl.RecentActions:
                                            $ Girl.Statup("Obed", 50, 5)
                                            $ Girl.Statup("Inbt", 50, 5)
                                            if Girl == RogueX:
                                                    ch_r "I hope that was enough."
                                            elif Girl == KittyX:
                                                    ch_k "Was that good enough for you?"
                                            elif Girl == EmmaX:
                                                    ch_e "I imagine that was plenty."
                                            elif Girl == LauraX:         
                                                    ch_l "That was enough, right?"
                                            if Girl.PantsNum() > 6 or Girl.HoseNum() >= 5:
                                                    call Girl_Tag(Girl)
                            
                            "How about you let me touch your pussy?":             
                                    $ CountStore = Tempmod          
                                    call Bottoms_Off(Girl,0) 
                                    $ Tempmod = CountStore  
                                    call expression Girl.Tag + "_Fondle_Pussy"   
                                    if "fondle pussy" in Girl.RecentActions:
                                            $ Girl.Statup("Obed", 50, 10)
                                            $ Girl.Statup("Obed", 80, 5)
                                            $ Girl.Statup("Inbt", 50, 10)
                                            $ Girl.Statup("Inbt", 80, 5)
                                            if Girl == RogueX:
                                                    ch_r "I hope that was enough."
                                            elif Girl == KittyX:
                                                    ch_k "Was that good enough for you?"
                                            elif Girl == EmmaX:
                                                    ch_e "I imagine that was plenty."
                                            elif Girl == LauraX:         
                                                    ch_l "That was enough, right?"
                            "Never mind, something else":
                                    jump Addict_Ultimatum_Menu
                "You could touch me.":  
                        menu:
                            "How about you give me a handjob?": 
                                    call expression Girl.Tag + "_Handjob"
                            
                            "How about you blow me?":
                                    call expression Girl.Tag + "_Blowjob"
                                    
                            "How about you titfuck me?":
                                    call expression Girl.Tag + "_Titjob"
                                    
                            "Never mind, something else":
                                    jump Addict_Ultimatum_Menu
                                    
                        if "angry" not in Girl.RecentActions:
                                if "blow" in Girl.RecentActions or "hand" in Girl.RecentActions or "titjob" in Girl.RecentActions:
                                            $ Girl.Statup("Obed", 50, 10)
                                            $ Girl.Statup("Obed", 80, 5)
                                            $ Girl.Statup("Inbt", 50, 10)
                                            $ Girl.Statup("Inbt", 80, 5)
                                            if Girl == RogueX:
                                                    ch_r "I hope that was enough."
                                            elif Girl == KittyX:
                                                    ch_k "Was that good enough for you?"
                                            elif Girl == EmmaX:
                                                    ch_e "I imagine that was plenty."
                                            elif Girl == LauraX:         
                                                    ch_l "That was enough, right?"

                                
                "How about you strip for me, and then I let you touch me?":
                        $ CountStore = Girl.ClothingCheck() 
                        call Group_Strip(Girl)  
                        if Girl.Loc != bg_current:
                                    jump Misplaced
                        menu:
                            "Ok, that was enough, you can touch me now.": 
                                    call Girl_Tag(Girl)
                                    $ Girl.Statup("Obed", 50, 10)
                                    $ Girl.Statup("Inbt", 50, 10)
                            "That was pretty weak, I'll need a bit more.":
                                    $ Girl.FaceChange("angry")
                                    if CountStore > Girl.ClothingCheck() and Girl.ClothingCheck() < 3:
                                            #if she is wearing less than before. . .
                                            $ Girl.Statup("Love", 200, -40)
                                            $ Girl.Statup("Inbt", 50, 5)
                                            $ Girl.Statup("Obed", 50, 20) 
                                            if Girl == RogueX:
                                                    ch_r "You're renigging after I went this far?!"
                                            elif Girl == KittyX:
                                                    ch_k "Hey! I. . . took off some stuff."
                                            elif Girl == EmmaX:
                                                    ch_e "I've made far more off far less. . ."
                                            elif Girl == LauraX:
                                                    ch_l "Hey, you get what you get."     
                                            jump Addicted_Bad_End
                                    else:
                                            if Girl == RogueX:
                                                    ch_r "Seriously? What will this take?" 
                                            elif Girl == KittyX:
                                                    ch_k "That wasn't enough?!"
                                            elif Girl == EmmaX:
                                                    ch_e "I think that was -more- than sufficient."
                                            elif Girl == LauraX:
                                                    ch_l "Not cool."                    
                    
                "I have some ideas. . ." if Girl.Event[1] >= 10:
                            call expression Girl.Tag + "_SexMenu"                    
                
                "Have you considered a . . . chemical solution?" if Girl.Event[1] >= 10 and Player.Semen and not Girl.Chat[2]:                      
                            #Serum first time
                            call Addicted_Serum                       
                "Would you like some \"serum?\"" if Girl.Event[1] >= 10 and Player.Semen and Girl.Chat[2]:                                         
                            #Would you like some serum?
                            call Addicted_Serum
                            
                "Nope, you're on your own":
                        if Girl.Event[1] >= 10:
                                #if you've already cleared this event
                                call Addicted_Fix_Beg
                        elif Girl.Addict >= 70:
                                $ Girl.FaceChange("angry",2)         
                                $ Girl.Statup("Love", 80, -2)
                                $ Girl.Statup("Obed", 80, 3)
                                if Girl == RogueX:
                                        ch_r "I ain't tak'in \"no\" for an answer here, figure it out."
                                elif Girl == KittyX:
                                        ch_k "Uhuh, we're figuring this one out."
                                elif Girl == EmmaX:
                                        ch_e "I'm afraid that you'll need a better answer than that."
                                elif Girl == LauraX:
                                        ch_l "Nooope."
                                $ Count2 = 0
                        else:
                                $ Girl.FaceChange("angry",2)         
                                $ Girl.Statup("Love", 200, -30)
                                $ Girl.Statup("Obed", 200, 5)
                                if Girl == RogueX:
                                        ch_r "Well then!"
                                elif Girl == KittyX:
                                        ch_k "Jerk!"
                                elif Girl == EmmaX:
                                        ch_e "Well then!"
                                elif Girl == LauraX:
                                        ch_l "Hmmph!"
                                "[Girl.Name] gives one last look over her shoulder before slamming the door and storming out."  
                                call Remove_Girl(Girl)
                                jump Addicted_Bad_End
            
            if "angry" in Girl.RecentActions:
                    #if you pissed her off. . .
                    if Girl.Addict >= 80:
                            if Girl == RogueX:
                                    ch_r "If I wasn't feeling so buzzed right now. . ." 
                            elif Girl == KittyX:
                                    ch_k "If I could keep my balance well enough to punch you. . ." 
                            elif Girl == EmmaX:
                                    ch_e "If my head wasn't buzzing like a million bees. . ." 
                            elif Girl == LauraX:
                                    ch_l "You're lucky I can barely see straight. . ." 
                    else:
                            if Girl == RogueX:
                                    ch_r "This is just not worth it. I'm out of here." 
                            elif Girl == KittyX:
                                    ch_k "Nope, this is too much, I'm outtie." 
                            elif Girl == EmmaX:
                                    ch_e "I'm afraid you overplayed your hand here, [Girl.Petname]." 
                            elif Girl == LauraX:
                                    ch_l "Nah, you pushed it too far there, [Girl.Petname]." 
                            jump Addicted_Bad_End 
                      
            if Girl.Addict <= 20:
                    # if you've settled her down. . .
                    return
            $ Tempmod = CountStore
            if Count2 and not Girl.Action:
                            if Girl == RogueX:
                                    ch_r "[[pant, pant] Get to the point already, [Player.Name]. . ." 
                                    ch_r "[[pant, pant] I can't keep this up all day."    
                            elif Girl == KittyX:
                                    ch_k "[[pant, pant] Wrap it up, [Player.Name]. . ." 
                                    ch_k "[[pant, pant] I'm worn out. . ."    
                            elif Girl == EmmaX:
                                    ch_e "[[pant, pant] Could we wrap this up, [Player.Name]. . ." 
                                    ch_e "[[pant, pant] I really do have plans later."    
                            elif Girl == LauraX:
                                    ch_l "Hey, um, get to the point already, [Player.Name]. . ." 
                                    ch_l "I've got things to do. . ."    
                            $ Girl.Action = 1  
            if Girl.Addict >= 80:
                    #if she's extra strung out. . .
                    if Count2 > 3:
                            if Girl == RogueX:
                                    ch_r "I'd, I don't want to do that. . ."
                            elif Girl == KittyX:
                                    ch_k "That's not really something I'd enjoy. . ."
                            elif Girl == EmmaX:
                                    ch_e "You'd push things that far. . ."
                            elif Girl == LauraX:
                                    ch_l "Come on, not cool. . ."
                            $ Tempmod += 5
                    elif Count2 > 2:
                            if Girl == RogueX:
                                    ch_r "But. . . I just can't. . ."
                            elif Girl == KittyX:
                                    ch_k "But. . . come on. . ."
                            elif Girl == EmmaX:
                                    ch_e "Surely there must be something we can agree to. . ."
                            elif Girl == LauraX:
                                    ch_l "Seriously,[Girl.Petname]. . ."
                            $ Tempmod += 10
                    elif Count2 > 1:
                            if Girl == RogueX:
                                    ch_r "PLEASE, I'm begging you here, be reasonable!"
                            elif Girl == KittyX:
                                    ch_k "Come on! I'm begging you here. . ."
                            elif Girl == EmmaX:
                                    ch_e "Leave me with a little dignity here. . ."
                            elif Girl == LauraX:
                                    ch_l "You've got to. . . please?"
                            $ Tempmod += 20   
            elif Girl.Addict <= AddictStore:
                            #if you've drained it a bit, but not enough. . .
                            if Girl == RogueX:
                                    ch_r "I'll still need a bit more than that. . ."
                            elif Girl == KittyX:
                                    ch_k "I'm still feeling off. . ."
                            elif Girl == EmmaX:
                                    ch_e "That's not quite enough yet. . ."
                            elif Girl == LauraX:
                                    ch_l "I'm still not feeling right. . ."
            else:
                    if Count2 > 2:
                            if Girl == RogueX:
                                    ch_r "Try something else, I'm not into that."
                            elif Girl == KittyX:
                                    ch_k "Isn't there anything I can do here?"
                            elif Girl == EmmaX:
                                    ch_e "You must be joking, we can come to an arrangement."
                            elif Girl == LauraX:
                                    ch_l "Nah, be serious."
                    elif Count2 > 1:
                            if Girl == RogueX:
                                    ch_r "Come on, isn't there anything I can do here?"
                            elif Girl == KittyX:
                                    ch_k "Gimme a break here."                                   
                            elif Girl == EmmaX:
                                    ch_e "There must be something you'd want. . ."
                            elif Girl == LauraX: 
                                    ch_l "Come on, let's do this." 
                            $ Tempmod += 10                  
            $ Count2 -= 1 if Count2 > 0 else 0 
            $ Round -= 10 if Round >= 21 else Round - 10
        #End While loop
        
        if Girl.Addict >= 80:
                #if you're well over the limits
                $ Girl.FaceChange("angry")
                "[Girl.Name] trembles with rage."
                $ Girl.Statup("Love", 200, -30)
                $ Girl.Statup("Inbt", 200, 40)
                if Girl == RogueX:
                        ch_r "Well then!"
                        ch_r "No way, no how. I'm going to get this taken care of, NOW!"
                elif Girl == KittyX:
                        ch_k "Jerk!"
                        ch_k "We are settling this now."
                elif Girl == EmmaX:
                        ch_e "Well then!"
                        ch_e "Sometimes you have to do it yourself. . ."
                elif Girl == LauraX:
                        ch_l "Hmmph!"
                call Girl_Tag(Girl,1)      
                $ Girl.Addictionrate += 2
                $ Girl.Resistance = 1 if Girl.Resistance < 1 else Girl.Resistance 
                jump Addicted_Bad_End   
            
        $ Girl.FaceChange("sad")
        if Girl == RogueX:
                ch_r "Sorry [Girl.Petname], you've run out of chances. I'm out of here."
        elif Girl == KittyX:
                ch_k "Well, I guess I should get going then. . ."                           
        elif Girl == EmmaX:
                ch_e "Well, I'm afraid we're out of time to mess around, I should be going."
        elif Girl == LauraX: 
                ch_l "Ok, fine, I gotta get going anyway. . ."
        jump Addicted_Bad_End  
    
label First_Addicted_End:    
        # This is the ending sequence if you successfully complete the addiciton innitiation
        $ Girl.DailyActions.append("fixed") 
        $ Girl.Event[1] = 10
        $ Girl.FaceChange("surprised") 
        if Girl == RogueX:
                ch_r "Wow. I feel a lot better now, a lot more centered. I think I really am addicted to you here."  
        elif Girl == KittyX:
                ch_k "Whoa. That felt great. I think maybe a little -too- great. . ."  
        elif Girl == EmmaX:
                ch_e "Amazing. That really did shake out the cobwebs. . . I think this may become an issue."  
        elif Girl == LauraX: 
                ch_l "Huh. That did the trick. Thanks."  
        if "swallowed" in Girl.RecentActions:
                $ Girl.FaceChange("bemused", 1)
                if Girl == RogueX:
                        ch_r "Hmm, there might be something to your. . . fluids too. They felt so warm. . ."
                elif Girl == KittyX:
                        $ Girl.Blush = 2
                        ch_k "And you, um. . . tasted really good too. . "
                elif Girl == EmmaX:
                        ch_e "I suspect there's something to your. . . fluids as well. . ."
                elif Girl == LauraX:
                        ch_l "You tasted pretty good too, real. . . warm? . ."
        $ Girl.FaceChange("normal", 0)
        $ Girl.Mouth = "sad"   
        call Sex_Over  
        if Girl not in Digits:
                if Girl == RogueX:
                        ch_r "I'm going to need to get in touch, you should probably have my number, here you go."    
                elif Girl == KittyX:
                        ch_k "You should[Girl.like]call me sometime, here's my number."    
                elif Girl == EmmaX:
                        ch_e "I'm going to need to get in touch, take down my number. . ."    
                elif Girl == LauraX:
                        ch_l "I'll probably need to get in touch, here's my number."             
                $ Digits.append(Girl)
        if Girl == RogueX:
                ch_r "I may need to do this again sometime. . . I'll see ya later."
        elif Girl == KittyX:
                ch_k "We should. . . um, do this again sometimeokbye."
        elif Girl == EmmaX:
                ch_e "We should. . . hook up some time."
        elif Girl == LauraX:
                ch_l "See ya later, we should hook up."
        $ Girl.Resistance = 1
    
label Addicted_Bad_End:  
        #if an Ultimatum fails. . .
        #also falls through from good ending. . .
        $ Girl.Event[3] = 5
        $ Girl.RecentActions.append("addiction")                      
        $ Girl.DailyActions.append("addiction")   
        $ Girl.DrainWord("ultimatum",0) #removes recent 
        $ Tempmod = 0
        $ Line = 0
        $ Situation = 0  
        $ Girl.Forced = 0   
        $ MultiAction = 1 
        $ Girl.Addictionrate += 2
        call Sex_Over  
        call Checkout
        $ Girl.ArmPose = 1  
        if bg_current == Girl.Home: 
                "You head back to your room."
        elif bg_current == "bg player" and Girl.Loc == bg_current:
                "[Girl.Name] heads out."  
        call Remove_Girl(Girl)     
        $ renpy.pop_call() 
        jump Misplaced
    
# end Event First_Addicted2 /////////////////////////////////////////////////////
  
label Addicted_Fix_Beg:   
        #jumped to if you refuse her anything during the later phase
        $ Girl.FaceChange("angry")
        $ Girl.Forced = 0    
        if "beg" in Girl.RecentActions: 
            $ Girl.Statup("Love", 200, -10)
        $ Girl.Statup("Obed", 50, 2)
        $ Girl.Statup("Obed", 90, 1)            
        if Girl.Petname in ("master", "sir"): 
                #if she is obedient
                $ Girl.FaceChange("sad")
                if Girl.Addict <= 80 or "beg" in Girl.RecentActions: 
                        if Girl == RogueX:
                                ch_r "If you insist, [Girl.Petname]."
                        elif Girl == KittyX:
                                ch_k "Ok, ok, fine. . . [Girl.Petname]"
                        elif Girl == EmmaX:
                                ch_e "I suppose I'll have to make do, [Girl.Petname]."
                        elif Girl == LauraX:
                                ch_l "Ok, fine, [Girl.Petname]."
                        "[Girl.Name] shrugs dejectedly, and then leaves the room."
                        jump Addicted_Bad_End        
                else:
                        $ Girl.Eyes = "manic"
                        "[Girl.Name] shivers slightly."                    
                        if Girl == RogueX:
                                ch_r "Please, [Girl.Petname], please reconsider?"
                        elif Girl == KittyX:
                                ch_k "Please, [Girl.Petname], I'm losing it. . ."
                        elif Girl == EmmaX:
                                ch_e ". . ."
                                ch_e "Please, [Girl.Petname]?"
                        elif Girl == LauraX:
                                ch_l "Come on, [Girl.Petname]?"
                        $ Girl.RecentActions.append("beg")                          
        elif Girl.Addict <= 85:      
                if Girl == RogueX:
                        ch_r "Well then!"
                elif Girl == KittyX:
                        ch_k "Jerk!"
                elif Girl == EmmaX:
                        ch_e "Well then!"
                elif Girl == LauraX:
                        ch_l "Hmmph!"
                "[Girl.Name] trembles with rage and walks out."
                jump Addicted_Bad_End                
        else:                 
                #if you're well over the limits
                $ Girl.FaceChange("angry")
                "[Girl.Name] trembles with rage."
                $ Girl.Statup("Love", 200, -10)
                $ Girl.Statup("Obed", 90, -5)   
                if Girl == RogueX:
                        ch_r "You. . ."
                        ch_r "I just can't take \"no\" for an answer here."  
                elif Girl == KittyX:
                        ch_k "!!!"
                        ch_k "I just can't even!"
                elif Girl == EmmaX:
                        ch_e ". . ."
                        ch_e "Fine."
                        ch_e "Sometimes you have to do it yourself. . ."
                elif Girl == LauraX:
                        ch_l "Grrrrrrrrrrr. . ."       
                call Girl_Tag(Girl,1)
                $ Girl.Statup("Inbt", 50, 10)
                $ Girl.Statup("Inbt", 90, 5)     
                $ Girl.Addictionrate += 2
                if Girl.Addict <= 40:
                        jump Addicted_Fix_End
                else:
                        "[Girl.Name] trembles with rage and walks out."
                        jump Addicted_Bad_End 
        return     
                        
# Event Addiction_Fix /////////////////////////////////////////////////////  
label Addiction_Fix(Girl=0):   
        if Girl not in TotalGirls:
                $ Girl = Ch_Focus
        call Set_The_Scene
        call Shift_Focus(Girl)
        $ Girl.Loc = bg_current
        $ Girl.OutfitChange(Changed=1)
        call Locked_Door(Girl)
        if not _return:
                #if the door is locked and you refused entry. . .
                return
        call Set_The_Scene
        call CleartheRoom(Girl)
        $ Girl.FaceChange("manic")  
        $ MultiAction = 0
        $ Taboo = 0
        $ Girl.Taboo = 0
        if bg_current != "bg player" and bg_current != Girl.Home:
                if Girl.Loc == bg_current or Girl in Party:
                        "[Girl.Name] says she wants to talk to you in your room and drags you over there."
                else:
                        "[Girl.Name] shows up, says she wants to talk to you in your room and drags you over there."
        else:
                if Girl.Loc == bg_current or Girl in Party:
                        "[Girl.Name] turns to you with a hungry look."
                else:            
                        "[Girl.Name] pops into your room in a bit of a tizzy."
        if Girl.Event[1] < 11:             
                if Girl == RogueX:
                        ch_r "Hey, so we figured out what's causing this buzz."
                        ch_r "Since I saw you last, it's been easier to deal with, it builds slower, goes away faster."
                        ch_r "I can almost handle it now, but not quite, you know?"
                elif Girl == KittyX:
                        ch_k "So I got a handle on what's been happening with me."
                        ch_k "With you."
                        ch_k "With this buzzing. . ."
                        ch_k "I think it's a little easier now? Seems to get better more quickly?"  
                        ch_k "But I could still use a little personal time. . ."
                elif Girl == EmmaX:
                        ch_e "You'll be pleased to know that I think I've sorted out our. . . drama."
                        ch_e "This whole \"buzzing\" issue." 
                        ch_e "I think that it's settled into a dull pang, something manageable."
                        ch_e "Not that I want to manage it -all- the time. . ."
                elif Girl == LauraX:
                        ch_l "Hey, I think I've got that buzzing sorted out."
                        ch_l "I don't think it's as strong, I think I can manage it now."
                        ch_l "Still, I like how it feels when it's good. . ."
                menu:
                    extend ""
                    "And still no alternative but touching me?":
                            $ Girl.Statup("Love", 80, 1)
                            $ Girl.Statup("Obed", 50, 1)             
                            if Girl == RogueX:
                                    ch_r "Nothing! McCoy's tried everything he can think of."
                            elif Girl == KittyX:
                                    ch_k "Nothing!"
                            elif Girl == EmmaX:
                                    ch_e "Unfortunately not. Hank's tried everything."
                            elif Girl == LauraX:
                                    ch_l "Doesn't look that way."
                    "Well anything I can do to help. . .":
                            $ Girl.Statup("Love", 90, 1)
                            $ Girl.Statup("Obed", 50, 1)             
                            if Girl == RogueX:
                                    ch_r "I appreciate that, [Girl.Petname]."
                            elif Girl == KittyX:
                                    ch_k "Aw, thanks, [Girl.Petname]."
                            elif Girl == EmmaX:
                                    ch_e "I am quite appreciative of that, [Girl.Petname]."
                            elif Girl == LauraX:
                                    ch_l "Yeah, thanks, [Girl.Petname]."
                    "You could always whore yourself out again.":
                            $ Girl.FaceChange("angry",2)     
                            $ Girl.Statup("Love", 50, -1, 1)
                            $ Girl.Statup("Love", 80, -3, 1)
                            $ Girl.Statup("Obed", 50, 2)
                            $ Girl.Statup("Obed", 90, 1)             
                            if Girl == RogueX:
                                    ch_r "Yeah, I'm aware of my options, thanks for pointing that out."
                            elif Girl == KittyX:
                                    ch_k "Yeah, thanks for that image."
                            elif Girl == EmmaX:
                                    ch_e ". . ."
                            elif Girl == LauraX:
                                    ch_l "Not cool."     
        else:
                    if Girl.Petname in ("master", "sir"):
                            $ Girl.FaceChange("bemused")              
                            if Girl == RogueX:
                                    ch_r "I need another fix, [Girl.Petname]. What can I do about it?"
                            elif Girl == KittyX:
                                    ch_k "I could use another fix, [Girl.Petname]. Could you help me?"
                            elif Girl == EmmaX:
                                    ch_e "I could do with a fix, [Girl.Petname]. Care to help me out?"
                            elif Girl == LauraX:
                                    ch_l "Gimme another fix, [Girl.Petname]. . . Please?"
                    else:             
                            if Girl == RogueX:
                                    ch_r "Hey, I think I need another fix, I'm feeling a bit out of it."
                            elif Girl == KittyX:
                                    ch_k "Hey, um, could I get another fix?"
                            elif Girl == EmmaX:
                                    ch_e "[Girl.Petname]. . . I could do with another fix. . . if you have the time."
                            elif Girl == LauraX:
                                    ch_l "Hey, could I get another fix?"
        $ Girl.Blush = 1            
        $ Count2 = 2
        $ Tempmod = 0
        call Addicted_Ultimatum
        jump Addicted_Fix_End
            
label Addicted_Fix_End:      
        #Event[4] is the number of times you've successfully done this.
        $ Girl.FaceChange("normal", 0)
        $ Girl.Mouth = "sad"  
        if Girl == RogueX:
                if Girl.Event[1] < 11:
                    #if it's the first "fix"
                    if "forced tag" in Girl.RecentActions: 
                            ch_r "I got what I needed. I really wish that I could avoid it, but it looks like I'm stuck with you."
                            ch_r "Just. . . in future maybe try to be less of a dick about it?"
                    elif not Girl.Forced:
                            ch_r "Thanks. I really appreciate this. I can't really explain it, but if I don't get. . . "
                            ch_r "access every now and then, I just feel awful, crawling out of my skin. Being with you, helps calm me down."            
                            if ApprovalCheck(Girl, 750):
                                ch_r "And, you know, we had a lot of fun in the process."
                            else: #not good with you
                                ch_r "And thanks for, you know, not taking advantage of the situation."        
                    else: #forced
                            ch_r "Well, I hope you got what you wanted out of this. I really wish that I could avoid it, but it looks like I'm stuck with you."
                            ch_r "Just. . . in future maybe try to be less of a dick about it?"
                else:        
                    if "forced tag" in Girl.RecentActions: 
                            ch_r "Well, I got what I needed. I guess I'll see you around."            
                    elif not Girl.Forced:
                            ch_r "Hmmmm, that was real nice, [Girl.Petname]."
                            ch_r "I'm looking forward more and more to these . . . \"sessions\" of ours."
                    else: #forced
                            ch_r "Well, looks like we both got what we wanted. I guess I'll see you around."  
        elif Girl == KittyX:
                if Girl.Event[1] < 11:
                    if "forced tag" in Girl.RecentActions: 
                            ch_k "Ok, that should do it. . ."
                            ch_k "Could you maybe not force me into that though?"
                    elif not Girl.Forced:
                            ch_k "Thanks for helping me out. It really feels awful when I let it go too long."
                            if ApprovalCheck(Girl, 850):
                                ch_k "And we got to have some fun with it too. . ."
                            else: #not good with you
                                ch_k "And thanks for[Girl.like]not taking advantage. . . you know?"        
                    else: #forced
                            ch_k "Well, you seemed to have fun. . ."
                            ch_k "Maybe. . . could you be less of a jerk about it. . ."
                            ch_k "Please?"
                else:        
                    if "forced tag" in Girl.RecentActions: 
                            ch_k "Ok, that should do it. . . guess I'll see you around."            
                    elif not Girl.Forced:
                            ch_k "Mmmmm, that was greeeeat, [Girl.Petname]."
                            ch_k "I hope to see you again real soon. . ."
                    else: #forced
                            ch_k "Well, you seemed to have fun. . . I'll see you around."  
        elif Girl == EmmaX:
                if Girl.Event[1] < 11:
                    if "forced tag" in Girl.RecentActions: 
                            ch_e "Well. . . I suppose that will satisfy me."
                            ch_e "You could perhaps catch more flies with honey, you know. . ."
                    elif not Girl.Forced:
                            ch_e "I appreciate your. . . assistance."
                            ch_e "This really is quite inconvenient, but I suppose it could be worse."
                            if ApprovalCheck(Girl, 800):
                                ch_e "You really aren't the worst company out there. . ."
                            else: #not good with you
                                ch_e "I appreciate your. . . restraint in handling our situation."        
                    else: #forced
                            ch_e "Well. . . you seem to have gotten the best of this arrangement. . ."
                            ch_e "You could perhaps catch more flies with honey, you know. . ."
                else:        
                    if "forced tag" in Girl.RecentActions: 
                            ch_e "Well. . . I suppose that will satisfy me. . . at least for the time being"        
                    elif not Girl.Forced:
                            ch_e "Hmmmm, that was quite pleasant, [Girl.Petname]."
                            ch_e "I suppose I am quite anticipating our next rendezvous."
                    else: #forced
                            ch_e "Well. . . you seem to have gotten the best of this arrangement. . ."
                            ch_e "For now, at least. . ."  
        elif Girl == LauraX:
                if Girl.Event[1] < 11:
                    if "forced tag" in Girl.RecentActions: 
                            ch_l "Ok, that should do it."
                            ch_l "Maybe don't be such an asshole though."
                    elif not Girl.Forced:      
                            ch_l "Mmmm, that's a weight off. . ."
                            ch_l "Thanks for helping to sort me out there, [Girl.Petname]."
                            if ApprovalCheck(Girl, 750):
                                ch_l "And hey, not a bad way to spend some time, right?"
                            else: #not good with you
                                ch_l "And thanks for not pushing things, eh?"        
                    else: #forced
                            $ Girl.Statup("Love", 90, -5)
                            ch_l "Ok, I guess you got what you wanted. I seem to be stuck with you here."
                            ch_l "Maybe don't be such an asshole though."
                else:        
                    if "forced tag" in Girl.RecentActions: 
                            ch_l "Ok, that should do it. See you later"          
                    elif not Girl.Forced:
                            ch_l "Good times, [Girl.Petname]."
                            ch_l "See ya later."
                    else: #forced
                            $ Girl.Statup("Love", 90, -5)
                            ch_l "Ok, looks like you got what you wanted. Guess I'll see you around."  
        $ Girl.Event[1] += 1
        $ Girl.DailyActions.append("fixed")
        jump Addicted_Bad_End
    
# end Event Addiction_Fix /////////////////////////////////////////////////////


            
label Addicted_Serum:
        # if Girl.Chat[2], she's tried it before
        # if Girl.Chat[3], she knows it's jiz    
        
        if "no serum" in Girl.RecentActions:           
                if Girl == RogueX:
                        ch_r "No, we tried that and you blew it."
                elif Girl == KittyX:
                        ch_k "Nope, try something else."
                elif Girl == EmmaX:
                        ch_e "I'm afraid you had your shot with that one."
                elif Girl == LauraX:
                        ch_l "Time for plan B, [Girl.Petname]."
                return
        $ CountStore = Girl.Action
        $ Girl.Action = 0                            
                                
        $ Girl.FaceChange("confused")
        if not Girl.Chat[2]:
            #if this is the first time she's tried it. . .  "Have you considered a . . . chemical solution?"   
            $ Girl.FaceChange("confused")         
            if Girl == RogueX:
                    ch_r "What do you mean by that?"
            elif Girl == KittyX:
                    ch_k "Chemical what?"
            elif Girl == EmmaX:
                    ch_e "Oh? In what way?"
            elif Girl == LauraX:
                    ch_l "Huh?"
            menu: 
                extend ""
                "I think I could. . . (trick her)":
                        ch_p "I was just thinking, I've been studying hard in class and could maybe whip up a. . .serum, that would reduce the cravings."                    
                        $ Girl.FaceChange()             
                        if Girl == RogueX:
                                ch_r "Hmm. . . well if you think you can figure out something that would stop this, I'm game."  
                        elif Girl == KittyX:
                                ch_k "Huh, really? Didn't take you for a chemistry whiz, but anything's worth a shot."  
                        elif Girl == EmmaX:
                                ch_e "Consider me a bit skeptical, given your grades, but I'm open to ideas."  
                        elif Girl == LauraX:
                                ch_l "Huh. . . Ok, I guess it's worth a shot."    
                                       
                "My jiz.":
                        $ Girl.Blush = 1             
                        if Girl == RogueX:
                                if Girl.Swallow:
                                        $ Girl.FaceChange("bemused") 
                                        ch_r "Hmm, well it has seemed to work for me in the past. . ."
                                else:
                                        $ Girl.FaceChange("surprised")
                                        ch_r "Your what? . . . You want me to drink your jiz?"
                                if ApprovalCheck(Girl, 750):     #if she likes you, she offers sex instead  
                                        $ Girl.FaceChange("sexy")
                                        ch_r "Well if that's the plan, couldn't I just get some from the source?"
                                else:
                                        ch_r "Well, I guess if touching you works, this could work too. . ."
                        elif Girl == KittyX:
                                if Girl.Swallow:
                                        $ Girl.FaceChange("bemused") 
                                        ch_k "Well. . .  It's not like that doesn't work. . ."
                                else:
                                        $ Girl.FaceChange("surprised",2)
                                        ch_k "Your what? . . . You want me to. . ."
                                        ch_k ". . . drink your jiz?"
                                if ApprovalCheck(Girl, 850):     #if she likes you, she offers sex instead 
                                        $ Girl.FaceChange("sexy") 
                                        ch_k "I mean, I don't -could- drink it from the bottle. . ."
                                else:
                                        ch_k "I guess this might be the simplest way. . ."
                        elif Girl == EmmaX:
                                if Girl.Swallow:
                                        $ Girl.FaceChange("bemused") 
                                        ch_e "I suppose it does have some. . . restorative properties. . ."
                                else:
                                        $ Girl.FaceChange("surprised")
                                        ch_e "Well. . . I suppose it does make a certain amount of sense. . ."
                                if ApprovalCheck(Girl, 950):     #if she likes you, she offers sex instead  
                                        $ Girl.FaceChange("sexy")
                                        ch_e "I might be convinced to drink it from the source, you know. . ."
                                else:
                                        ch_e "I have entertained worse offers. . ."
                        elif Girl == LauraX:
                                if Girl.Swallow:
                                        $ Girl.FaceChange("bemused") 
                                        ch_l "Yeah, makes sense. . ."
                                else:
                                        $ Girl.FaceChange("surprised")
                                        ch_l "Huh? Huh. . . yeah, makes sense."
                                if ApprovalCheck(Girl, 850):     #if she likes you, she offers sex instead  
                                        $ Girl.FaceChange("sexy")
                                        ch_l "Do you want me to just get down there?"
                                else:
                                        ch_l "So, we doing this?"
                        $ Tempmod += 20
                        $ Girl.Chat[3] = 1
                    
                "Never mind.":                
                    $ Girl.Action = CountStore
                    return
        
        elif Girl.Chat[3]:
                #if she knows it's jiz. . .
                $ Girl.FaceChange("bemused", 1)  
                $ Tempmod += 20           
                if Girl == RogueX:
                        ch_r "Hmm, it was good last time. . ."            
                        if ApprovalCheck(Girl, 750):
                                $ Girl.FaceChange("sexy")
                                ch_r "I'd really rather get it straight off the tap. . ."
                        else:
                                $ Girl.FaceChange("sad")
                                $ Girl.Brows = "normal" 
                                ch_r "I guess this is as good a \"treatment\" as any."
                elif Girl == KittyX:
                        ch_k "Well, it was tasty. . ."            
                        if ApprovalCheck(Girl, 850):
                                $ Girl.FaceChange("sexy")
                                ch_k "I take my milk from the bottle. . ."
                        else:
                                $ Girl.FaceChange("sad")
                                $ Girl.Brows = "normal" 
                                ch_k "This'll work out, I guess."
                elif Girl == EmmaX:
                        ch_e "You do possess a unique bouquet. . ."            
                        if ApprovalCheck(Girl, 950):
                                $ Girl.FaceChange("sexy")
                                ch_e "I'd rather take my medicine. . . directly."
                        else:
                                $ Girl.FaceChange("sad")
                                $ Girl.Brows = "normal" 
                                ch_e "I suppose we can make this work."
                elif Girl == LauraX:
                        ch_l "Yeah, i mean it was pretty good. . ."            
                        if ApprovalCheck(Girl, 850):
                                $ Girl.FaceChange("sexy")
                                ch_l "I'd really rather get it straight off the tap. . ."
                        else:
                                $ Girl.FaceChange("sad")
                                $ Girl.Brows = "normal" 
                                ch_l "I guess this works."
        elif Girl.Chat[2]:                
                #if she's tried it before. . .
                ch_p "I was just thinking, I could whip up more of that serum. . ."
                $ Girl.FaceChange("bemused")             
                if Girl == RogueX:
                        ch_r "Well, whatever that stuff is, it worked well enough last time. . ."  
                elif Girl == KittyX:
                        ch_k "Well, it did seem to do the trick. . ."  
                elif Girl == EmmaX:
                        ch_e "Yes. . . it certain was. . . interesting. . ."  
                elif Girl == LauraX:
                        ch_l "Yeah, ok. Kinda tasted like jiz though. . ." 
                $ Tempmod += 10                  
                 
        #pricing                 
        $ Count = 3
        while Count and "has serum" not in Girl.RecentActions:   
            $ Line = 0
            $ Count -= 1
            menu:
                "What do you ask for in exchange?"
                "Give it to her":
                        $ Girl.Forced = 0    
                        $ Girl.Mouth = "smile"
                        $ Girl.Statup("Love", 50, 1)
                        "You hand her the serum."
                        $ Girl.RecentActions.append("has serum")
                    
                "Well, a handy might do the trick. . .":
                        $ Girl.FaceChange("sexy")
                        if ApprovalCheck(Girl, 1100) or (ApprovalCheck(Girl, 800) and Girl.Chat[2]):
                                $ Girl.ArmPose = 2             
                                if Girl == RogueX:
                                        if Girl.Chat[3]: 
                                                ch_r "Heh, I guess I could work the pump for a bit."
                                        else:
                                                ch_r "I guess if that's what you want. . ."
                                elif Girl == KittyX:
                                        if Girl.Chat[3]: 
                                                ch_k "Oh, we're going \"manual\" then. . ."
                                        else:
                                                ch_k "Hmm, yeah, cost of doing business. . ."
                                elif Girl == EmmaX:
                                        if Girl.Chat[3]: 
                                                ch_e "Well, I suppose if you want something done right. . ."
                                        else:
                                                ch_e "I suppose one good turn deserves another. . ."
                                elif Girl == LauraX:
                                                ch_l "Sure, I could lend you a hand. . ."
                                call expression Girl.Tag + "_HJ_Prep"
                                $ Girl.Statup("Obed", 70, 1)
                                $ Girl.Statup("Inbt", 50, 2)
                                $ Girl.Statup("Inbt", 70, 1)
                                $ Girl.RecentActions.append("has serum")
                        else:
                                $ Girl.Brows = "confused"             
                                if Girl == RogueX:
                                        ch_r "Pssht, you wish."
                                elif Girl == KittyX:
                                        ch_k "Heh, as if."
                                elif Girl == EmmaX:
                                        ch_e "Oh, I'm sure you'd enjoy that."
                                elif Girl == LauraX:
                                        ch_l "Heh, yeah right."
                                        
                "How about a blowjob?":                    
                        $ Girl.FaceChange("sexy")
                        if ApprovalCheck(Girl, 1300) or (ApprovalCheck(Girl, 800) and Girl.Chat[3]):             
                                if Girl == RogueX:
                                        if Girl.Chat[3]: 
                                                ch_r "Heh, I guess I could get it straight from the source."
                                        else:
                                                ch_r "I. . . suppose I could. . ."
                                elif Girl == KittyX:
                                        if Girl.Chat[3]: 
                                                ch_k "Oh, I guess straight off the tap. . ."
                                        else:
                                                ch_k "Hmm, yeah, cost of doing business. . ."
                                elif Girl == EmmaX:
                                        if Girl.Chat[3]: 
                                                ch_e "Doesn't hurt to get it from the source. . ."
                                        else:
                                                ch_e "I suppose one good turn deserves another. . ."
                                elif Girl == LauraX:
                                                ch_l "I could give it a taste. . ."                                                
                                call expression Girl.Tag + "_BJ_Prep"
                                $ Girl.RecentActions.append("has serum")
                                $ Girl.Statup("Obed", 70, 1)
                                $ Girl.Statup("Inbt", 50, 2)
                                $ Girl.Statup("Inbt", 70, 1)                    
                        else:
                                $ Girl.Brows = "confused"      
                                if Girl == RogueX:
                                        ch_r "Pssht, you wish."
                                elif Girl == KittyX:
                                        ch_k "Heh, as if."
                                elif Girl == EmmaX:
                                        ch_e "Oh, I'm sure you'd enjoy that."
                                elif Girl == LauraX:
                                        ch_l "Heh, yeah right."
                                             
                "Ask for a favor for it.":
                        $ Girl.FaceChange("sexy")           
                        if Girl == RogueX:
                                ch_r "Oh? What sort of favor were you expecting, [Girl.Petname]?"
                        elif Girl == KittyX:
                                ch_k "Yeah? What'd you want, [Girl.Petname]?"
                        elif Girl == EmmaX:
                                ch_e "What is it you're expecting of me, [Girl.Petname]?"
                        elif Girl == LauraX:
                                ch_l "Ok, what're you thinking, [Girl.Petname]?"
                        $ MultiAction = 0                          
                        $ Girl.Action = 1
                        call expression Girl.Tag + "_SexMenu"   
                        if "angry" not in Girl.RecentActions:
                                $ Girl.Statup("Love", 70, 2)       
                                if Girl == RogueX:
                                        ch_r "I'm glad we could work something out, [Girl.Petname]."
                                elif Girl == KittyX:
                                        ch_k "Ok, what next?"
                                elif Girl == EmmaX:
                                        ch_e "I suppose that was fair."
                                elif Girl == LauraX:
                                        ch_l "Ok, now with that out of the way. . ."
                                $ Girl.Statup("Obed", 50, 1)
                                $ Girl.Statup("Obed", 70, 1)
                                $ Girl.Statup("Inbt", 70, 2)  
                                $ Girl.RecentActions.append("has serum") 
                        else:       
                                if Girl == RogueX:
                                        ch_r "Well that ain't gonna fly, [Girl.Petname]."
                                elif Girl == KittyX:
                                        ch_k "As if, [Girl.Petname]."
                                elif Girl == EmmaX:
                                        ch_e "You must be joking, [Girl.Petname]."
                                elif Girl == LauraX:
                                        ch_l "Nope."
                                $ Count = 0
                            
                "I'm charging for a sip, $5.":
                            $ Line = "Five"
                                        
                "I'm afraid I'll have to charge, $10.":
                            $ Line = "Ten"
                        
                "Never mind.":       
                            if Girl == RogueX:
                                    ch_r "Oh, ok. . ."
                            elif Girl == KittyX:
                                    ch_k "Um, ok. . ."
                            elif Girl == EmmaX:
                                    ch_e "Ok. . ."
                            elif Girl == LauraX:
                                    ch_l "Oh, ok. . ."
                            $ Girl.Action = CountStore
                            return
                            
            if Line == "Five" or Line == "Ten":
                        #you've tried to charge for it. . .
                        $ Girl.FaceChange("angry")
                        $ Girl.Mouth = "surprised"       
                        if Girl == RogueX:
                                if Girl.Chat[3]: 
                                        ch_r "[Line] bucks, just to drink your cum?"
                                elif Girl.Chat[2]:
                                        ch_r "[Line] bucks, just for this supposed \"serum\"?"
                                else:
                                        ch_r "[Line] bucks, just for that serum?"
                        elif Girl == KittyX:
                                if Girl.Chat[3]: 
                                        ch_k "[Line] bucks for a mouthfull of jiz?"
                                elif Girl.Chat[2]:
                                        ch_k "[Line] bucks, just for this supposed \"serum\"?"
                                else:
                                        ch_k "[Line] bucks, just for that serum?"
                        elif Girl == EmmaX:
                                if Girl.Chat[3]: 
                                        ch_e "[Line] dollars? You're charging for warm semen?"
                                elif Girl.Chat[2]:
                                        ch_e "[Line] bucks, just for this supposed \"serum\"?"
                                else:
                                        ch_e "[Line] bucks, just for that suspect liquid?"
                        elif Girl == LauraX:
                                if Girl.Chat[3]: 
                                        ch_l "[Line] bucks for fresh cum?"
                                elif Girl.Chat[2]:
                                        ch_l "[Line] bucks, just for some \"serum\"?"
                                else:
                                        ch_l "[Line] bucks, just for that stuff?"
                        $ Girl.FaceChange()
                        $ Girl.Eyes = "side"
                        $ Girl.Statup("Love", 70, -3, 1)
                        $ Girl.Statup("Love", 200, -4)
                        call AnyLine(Girl,". . .")
                        $ Girl.FaceChange()
                        $ Girl.Brows = "sad"
                        if Line == "Ten": 
                                $ Girl.Statup("Love", 70, -2, 1)
                                $ Girl.Statup("Love", 90, -10)  
                        if Girl.Chat[2] and Line == "Ten" and Girl.Addict >= 75:         
                                if Girl == RogueX:
                                        ch_r "Five was bad enough! Fine, here you go, but not a penny more." 
                                elif Girl == KittyX:
                                        ch_k "Five was bad enough! Ok, whatever, here." 
                                elif Girl == EmmaX:
                                        ch_e "Five wasn't enough for you? Fine." 
                                elif Girl == LauraX:
                                        ch_l "You're busting my balls here. Ok, ten, fine."  
                                $ Girl.Statup("Obed", 50, 2)
                                $ Girl.Statup("Obed", 90, 3)
                                $ Girl.Statup("Inbt", 70, 2)
                                if not ApprovalCheck(Girl, 1200, "LI"):
                                        $ Girl.Forced = 1    
                                $ Player.Cash += 10 
                                $ Girl.RecentActions.append("has serum") 
                        elif Girl.Chat[2] and Line == "Five":         
                                if Girl == RogueX:
                                        ch_r "Ok, here you go."
                                elif Girl == KittyX:
                                        ch_k "Ok, fine."
                                elif Girl == EmmaX:
                                        ch_e "Oh, very well."
                                elif Girl == LauraX:
                                        ch_l "I guess, here."
                                $ Girl.Statup("Obed", 50, 4)
                                $ Girl.Statup("Obed", 70, 2)
                                $ Girl.Statup("Inbt", 70, 4)                    
                                if not ApprovalCheck(Girl, 1200, "LI"):
                                        $ Girl.Forced = 1    
                                $ Player.Cash += 5 
                                $ Girl.RecentActions.append("has serum")
                        else:       
                                if Girl == RogueX:
                                        ch_r "No way, I don't even know if this'll work."
                                elif Girl == KittyX:
                                        ch_k "No way, this might not even work!"
                                elif Girl == EmmaX:
                                        ch_e "I'm not paying for something so suspicious."
                                elif Girl == LauraX:
                                        ch_l "No way."
            #end "charge for it"
                                        
            if "swallowed" in Girl.RecentActions:              
                    if Girl == RogueX:
                            if Girl.Chat[3]: 
                                    ch_r "Well, I think that hit the spot. . ."
                                    return
                            else:
                                    ch_r "That was. . . good actually, now what about this serum?"
                    elif Girl == KittyX:
                            if Girl.Chat[3]: 
                                    ch_k "Hmm, delicious. . ."
                                    return
                            else:
                                    ch_k "That was. . . fine, but what about this serum?"
                    elif Girl == EmmaX:
                            if Girl.Chat[3]: 
                                    ch_e "Quite satisfying. . ."
                                    return
                            else:
                                    ch_e "Now that we've dealt with the payment, what about this \"serum?\""
                    elif Girl == LauraX:
                            if Girl.Chat[3]: 
                                    ch_l "That was good. . ."
                                    return
                            else:
                                    ch_l "Ok, so you mentioned a \"serum?\""
            elif "hand" in Girl.RecentActions or "blow" in Girl.RecentActions: 
                            #not swallowed             
                            if Girl == RogueX:
                                    ch_r "Ok, I think I worked that one off, now how about that serum?"
                            elif Girl == KittyX:
                                    ch_k "Ok, I think I earned it, now what about this serum?"
                            elif Girl == EmmaX:
                                    ch_e "I think that should be sufficient, what about this \"serum?\""
                            elif Girl == LauraX:
                                    ch_l "That worked out, so you mentioned a \"serum?\""
                                
            if "has serum" in Girl.RecentActions:  
                            #if she got the serum, drop out of the loop
                            $ Count = 0
            elif Count == 1:       
                            if Girl == RogueX:
                                    ch_r "I don't have all day, get serious."  
                            elif Girl == KittyX:
                                    ch_k "There's gotta be something else you want?"
                            elif Girl == EmmaX:
                                    ch_e "I need you to make a reasonable offer here. . ."
                            elif Girl == LauraX:      
                                    ch_l "Hey, get serious here."
            elif Count:       
                            if Girl == RogueX:
                                    ch_r "Come on, what else do you want here?"
                            elif Girl == KittyX:
                                    ch_k "Come on, anything else?"
                            elif Girl == EmmaX:
                                    ch_e "I'm trying to be flexible here. . ."
                            elif Girl == LauraX:
                                    ch_l "Hey, give me a better idea."
            #end while loop
                  
                  
        if "has serum" in Girl.RecentActions: 
                #falls through if she got the serum  
                "She opens the serum bottle and gives it a little sniff."
                
                if Girl.Chat[3]:
                        "She glances hesitantly at you, but gulps it down, and wipes her lips."                                 
                        $ Girl.Statup("Inbt", 70, 2)
                elif Girl.Swallow >= 5 or Girl in (EmmaX,LauraX):
                        "She looks a bit confused, but then grins, gulps it down, and wipes her lips."   
                        $ Girl.Statup("Inbt", 50, 1)
                        $ Girl.Statup("Inbt", 70, 2)    
                        if Girl == RogueX:
                                ch_r "That was your jiz, wasn't it. You chould have just told me."  
                                ch_r "I know how well that stuff works."                 
                        elif Girl == KittyX:
                                ch_k "Hey, that was just jiz!" 
                                ch_k "Well, I guess it works."
                        elif Girl == EmmaX:
                                ch_e "I should have realized that you weren't some chemical genius."
                                ch_e "Using your own juices as a cure-all?"
                                ch_e "Still, I suppose this is a convenient alternative."
                        elif Girl == LauraX:
                                ch_l "Oh. That was jiz."  
                                ch_l "Makes sense."
                        $ Girl.Chat[3] = 1
                elif Girl.Swallow or Girl in (EmmaX,LauraX):                                
                        $ Girl.FaceChange("surprised")       
                        if Girl == RogueX:
                                ch_r "Hmmm. . . hey, this is your jiz, isn't it?!"              
                        elif Girl == KittyX:
                                ch_k "Hey, that was just jiz!" 
                        elif Girl == EmmaX:
                                ch_e "I should have realized that you weren't some chemical genius."
                                ch_e "Using your own juices as a cure-all?"
                        elif Girl == LauraX:
                                ch_l "Hey, that was just jiz."  
                        menu:
                            extend ""
                            "Um, yes?":
                                    $ Girl.FaceChange("confused")
                                    $ Girl.Mouth = "lipbite"
                            "Of course not!":
                                    $ Girl.FaceChange("confused")
                                    $ Girl.Mouth = "smile"
                        "She looks sternly at you, but then gulps it down and wipes her lips."   
                        if Girl == RogueX:
                                ch_r "Ugh, I'm still getting used to the taste of that, you should have just told me."
                        elif Girl == KittyX:
                                ch_k "Ew, gross. . . you could have just told me."
                        elif Girl == EmmaX:
                                ch_e "Well, it's not like it's the first time I've taken sperm recreationally."
                        elif Girl == LauraX:
                                ch_l "Well, I guess it works. . ."
                        $ Girl.Chat[3] = 1
                else:       #She doesn't know what it was
                        "She then gulps it down and wipes her lips."
                        if Girl == RogueX:
                                ch_r "Ugh, that stuff goes down hard. . ."
                        elif Girl == KittyX:
                                ch_k "Ew, this stuff is thick. . ."
                $ Girl.Eyes = "closed"
                $ Girl.Brows = "sad"
                $ Girl.Mouth = "smile"
                "[Girl.Name] shudders with ecstasy."
                $ Girl.FaceChange()
                if Girl.Chat[3]:
                        if Girl == RogueX:
                                ch_r "Hmm, even knowing what that stuff is, it does seem to work."  
                        elif Girl == KittyX:
                                ch_k "Still kinda weird, but it works."  
                        elif Girl == EmmaX:
                                ch_e "I'm still stunned at how effective that is."  
                        elif Girl == LauraX:
                                ch_l "Ah, that's better."  
                        $ Girl.RecentActions.append("swallowed") 
                        $ Girl.DailyActions.append("swallowed") 
                else:
                        if Girl == RogueX:
                                ch_r ". . . that does certainly take the edge off. Thank you."  
                        elif Girl == KittyX:
                                ch_k ". . . but it does do the trick. Thanks."                 
                $ Girl.RecentActions.remove("has serum") 
                $ Girl.RecentActions.append("serum") 
                $ Girl.DailyActions.append("serum")            
                $ Girl.Addict = 20 if Girl.Addict >= 20 else 0
                $ Girl.Addictionrate += 2
                if "addictive" in Player.Traits:
                        $ Girl.Addictionrate += 2           
                $ Girl.Chat[2] += 1
        else:
                if Girl == RogueX:
                        ch_r "Too bad we couldn't come to an arrangement here. . ."
                elif Girl == KittyX:
                        ch_k "I wish you'd be more flexible. . ."
                elif Girl == EmmaX:
                        ch_e "You drive too hard a bargain. . ."
                elif Girl == LauraX:
                        ch_l "Well, I guess that's that. . ." 
                $ Girl.RecentActions.append("no serum") 
        $ Girl.Action = CountStore
        return
# End Addiction / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
    
    