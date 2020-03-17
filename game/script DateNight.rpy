label Date_Ask(Girl=0):
        #From the chat menu, you ask Rogue to meet you
        if Girl not in TotalGirls:
            $ Girl = Ch_Focus
        call Shift_Focus(Girl)
        if "yesdate" in Girl.DailyActions:  
                $ Girl.FaceChange("bemused")
                if Girl == RogueX:      
                        ch_r "Come on, I already said \"yes.\""         
                elif Girl == KittyX:
                        ch_k "Lol, I already said \"yes.\""  
                elif Girl == EmmaX:
                        ch_e "Learn to take \"yes\" for an answer, [Girl.Petname]."  
                elif Girl == LauraX:
                        ch_l "I already told you \"ok.\""  
                return         
        if "askeddate" in Girl.DailyActions:  
                $ Girl.FaceChange("angry")        
                if Girl == RogueX:         
                        ch_r "I think you got your answer already."    
                elif Girl == KittyX:
                        ch_k "Geez, stop bothering me already!" 
                elif Girl == EmmaX:
                        ch_e "Persistance will not be rewarded, [Girl.Petname]."  
                elif Girl == LauraX: 
                        ch_l "Back off."          
                return 
        if "stoodup" in Girl.Traits:  
                call Date_Stood_Up(Girl)
                #$ Girl.AddWord(1,"askeddate","askeddate")#recent and daily
                return 
        $ Girl.AddWord(1,"askeddate","askeddate")  #recent and daily
        
        if Girl == EmmaX:
                if "classcaught" not in EmmaX.History:  
                        #if you haven't caught her yet
                        ch_e "I don't really think it would be appropriate for the two of us to be seen together."
                        return
                if "taboo" not in EmmaX.History:
                        #if she hasn't agreed to go public yet
                        call Emma_Taboo_Talk
                        if "taboo" not in EmmaX.History:
                            return
        if Girl.Break[0] and "ex" in Girl.Traits:
                $ Girl.FaceChange("angry")        
                if Girl == RogueX:         
                        ch_r "Seriously? You're asking me that after what you just did?"     
                elif Girl == KittyX:
                        ch_k "You can't just pretend that nothing happened!"  
                elif Girl == EmmaX:
                        ch_e "I think you have some work to do before you're ready to ask that question." 
                elif Girl == LauraX:
                        ch_l "You don't want to be hassling me right now."              
                return     
        if "ex" in Girl.Traits:
            if ApprovalCheck(Girl, 1200):
                    $ Girl.FaceChange("bemused",Brows = "sad" ) 
                    if Girl == RogueX:   
                            ch_r "We had some fun, I guess we could go out, as friends maybe."            
                    elif Girl == KittyX:
                            ch_k "I don't know, we used to have fun. Maybe. . ." 
                    elif Girl == EmmaX:
                            ch_e "You were an entertaining date, I suppose, this once."    
                    elif Girl == LauraX:        
                            ch_l "Well, we did have some fun. . ."          
            else:
                    $ Girl.FaceChange("angry",Eyes = "side")
                    if Girl == RogueX:        
                            ch_r "I don't think we really worked out, [Girl.Petname]."      
                    elif Girl == KittyX:
                            ch_k "I[Girl.like]don't think so." 
                    elif Girl == EmmaX:
                            ch_e "I don't think we really worked out, [Girl.Petname]." 
                    elif Girl == LauraX:
                            ch_l "Nah, pass." 
                    return 
           
        if "stoodup" in Girl.History or "deadbeat" in Girl.History: 
            if "stoodup" in Girl.History:
                    $ Girl.FaceChange("angry",Eyes = "side")  
                    if Girl == RogueX:       
                            ch_r "Don't you be leav'in me behind this time."      
                    elif Girl == KittyX: 
                            ch_k "I don't want to be left in the quad again." 
                    elif Girl == EmmaX:
                            ch_e "I believe you know better than to leave me waiting again."
                    elif Girl == LauraX:             
                            ch_l "Just don't keep me waiting again."             
            if "deadbeat" in Girl.History:  
                    $ Girl.FaceChange("angry")  
                    if Girl == RogueX:   
                            if "stoodup" in Girl.History:
                                ch_r "And last time, you even made me pay for your broke ass?"          
                            else:
                                ch_r "Remember last time, when you made me pay for your broke ass?"               
                    elif Girl == KittyX:
                            if "stoodup" in Girl.History:
                                ch_k "And last time we went out, you[Girl.like]left me with the check!"  
                            else:
                                ch_k "Last time we went out, you[Girl.like]left me with the check!"   
                    elif Girl == EmmaX:
                            if "stoodup" in Girl.History:
                                ch_e "Nor do I expect to be picking up the check again."          
                            else:
                                ch_e "I don't I expect to be picking up the check again."    
                    elif Girl == LauraX:    
                            if "stoodup" in Girl.History:
                                ch_l "And last time you just ditched me with the check."   
                            else:
                                ch_l "Last time you just ditched me with the check."
            menu:
                extend ""
                "Sorry about that, I'll take care of it this time.":
                        if ApprovalCheck(Girl, 650):
                                $ Girl.FaceChange("sad")
                                if Girl == RogueX:       
                                        ch_r "Ok, [Girl.Petname], you'd better."      
                                elif Girl == KittyX:
                                        ch_k "Well, I guess I can give you another chance, just don't disappoint me again."
                                elif Girl == EmmaX:
                                        ch_e "I'll take you at your word, [Girl.Petname]."
                                elif Girl == LauraX:
                                        ch_l "Ok, you get another shot, don't screw it up."
                        else:
                                $ Girl.FaceChange("angry")
                                if Girl == RogueX:            
                                        ch_r "Yeah, I'aint buy'in that hogwash, [Girl.Petname]."  
                                elif Girl == KittyX:
                                        ch_k "Yeah[Girl.like]fool me once. . . no thanks, [Girl.Petname]." 
                                elif Girl == EmmaX:
                                        ch_e "A likely story." 
                                elif Girl == LauraX:
                                        ch_l "You had your chance, you blew it." 
                                return
                "Yeah, so?":
                        if ApprovalCheck(Girl, 1400,Alt=[[EmmaX],1500]):
                                $ Girl.FaceChange("angry", Mouth = "grimace")
                                if Girl == RogueX:     
                                        ch_r "It's a good thing you're so pretty."        
                                elif Girl == KittyX:
                                        ch_k "Why do I[Girl.like]put up with you?"
                                elif Girl == EmmaX:
                                        ch_e "I suppose I can appreciate confidence."
                                        $ EmmaX.FaceChange("bemused")     
                                        ch_e "Just don't get {i}too{/i} confident."  
                                elif Girl == LauraX:
                                        ch_l "Hmm. Ok."
                                return 
                                $ Girl.FaceChange("bemused")        
                        elif ApprovalCheck(Girl, 500, "O",Alt=[[EmmaX],700]):
                                $ Girl.FaceChange("surprised")
                                call AnyLine(Girl,". . .")
                                $ Girl.FaceChange("sad")
                                $ Girl.Statup("Obed", 80, 3)
                                if Girl == RogueX:     
                                        ch_r "I. . . guess I can give you another shot. . ."        
                                elif Girl == KittyX:
                                        ch_k "Well, I guess we can still have fun. . ."
                                elif Girl == EmmaX:
                                        ch_e "Well, I suppose I could join you for a bit. . ."
                                elif Girl == LauraX:
                                        ch_l "If you insist. . ."
                        elif ApprovalCheck(Girl, 650):
                                $ Girl.FaceChange("angry")
                                $ Girl.Statup("Love", 80, -5)
                                $ Girl.Statup("Inbt", 60, 2) 
                                if Girl == RogueX:       
                                        ch_r "\"So\" it looks like we won't be going out again."         
                                elif Girl == KittyX:
                                        ch_k "Yeah[Girl.like]I'm going out with {i}you,{/i} dick."  
                                elif Girl == EmmaX:
                                        ch_e "Then I believe you can figure out the answer to your own question."  
                                elif Girl == LauraX: 
                                        ch_l "So I'm not going out with you again." 
                                return 
                        else:
                                $ Girl.FaceChange("angry")
                                $ Girl.Statup("Love", 80, -10)
                                $ Girl.Statup("Obed", 80, -3)
                                $ Girl.Statup("Inbt", 60, 2) 
                                if Girl == RogueX:  
                                        ch_r "Fuck off."             
                                elif Girl == KittyX:
                                        ch_k "Asshole."  
                                elif Girl == EmmaX:
                                        ch_e "You don't want to stick around." 
                                elif Girl == LauraX:
                                        ch_l "Dick."  
                                return             
            $ Girl.Statup("Obed", 30, 3)
            $ Girl.Statup("Obed", 80, 2)
        #end "if stoodup or deadbeat". . .
        elif ApprovalCheck(Girl, 650):
                $ Girl.FaceChange("smile")
                if Girl == RogueX:  
                        ch_r "Yeah, sounds good. See ya in a bit, [Girl.Petname]."           
                elif Girl == KittyX:
                        ch_k "Sure, see you then."
                elif Girl == EmmaX:
                        ch_e "Sounds lovely, I'll see you later then, [Girl.Petname]."
                elif Girl == LauraX:
                        ch_l "Sure, see you there."
        elif ApprovalCheck(Girl, 400):                
                $ Girl.FaceChange("angry",Eyes = "side")
                if Girl == RogueX:      
                        ch_r "I think I'm washing my hair tonight. . ."       
                elif Girl == KittyX:
                        ch_k "I've[Girl.like]got better things to do. . ."
                elif Girl == EmmaX:
                        ch_e "I have some papers to take care of tonight. . ."
                elif Girl == LauraX:
                        ch_l "I've got some other stuff to do. . ."
                return
        else:
                $ Girl.FaceChange("angry")
                if Girl == RogueX:    
                        ch_r "Yeah, you wish."         
                elif Girl == KittyX:
                        ch_k "[Girl.Like]no way."
                elif Girl == EmmaX:
                        ch_e "I can't imagine why I would."
                elif Girl == LauraX:
                        ch_l "Nah."
                return 
        
        $ Count = 0
        #She mostly agreed, do you ask for a double date?
        menu:
            "Good, I'll meet you in the campus square." if bg_current != "bg campus" or Current_Time != "Evening": 
                            $ Girl.FaceChange("smile")
            "Good, let's get going then." if bg_current == "bg campus" and Current_Time == "Evening": 
                            $ Girl.FaceChange("smile")
            "And I was thinking of asking. . .": 
                        menu:
                            ch_p "And I was thinking of asking. . ."
                            "[RogueX.Name] along too." if Girl != RogueX:
                                        $ Count = Girl.LikeRogue
                            "[KittyX.Name] along too." if Girl != KittyX:
                                        $ Count = Girl.LikeKitty
                            "[EmmaX.Name] along too." if Girl != EmmaX:
                                        $ Count = Girl.LikeEmma
                            "[LauraX.Name] along too." if Girl != LauraX:
                                        $ Count = Girl.LikeLaura
                            "Never mind, probably a bad idea.":  
                                        $ Girl.FaceChange("confused")
                                        if Girl == RogueX:  
                                                ch_r "Okay. . ."           
                                        elif Girl == KittyX:
                                                ch_k "Um. . ."
                                        elif Girl == EmmaX:
                                                ch_e "I see. . ."
                                        elif Girl == LauraX:
                                                ch_l "Um. . ."
                                        if bg_current != "bg campus": 
                                                ch_p "I'll meet you in the campus square then."
        if Count:
            #If you asked about another girl. . .
            if Count >= 600 and ApprovalCheck(Girl, 800, "OI"): #Count is "Girl.LikeX"
                    $ Girl.FaceChange("smile")
                    if Girl == RogueX:          
                            ch_r "Oh, yeah, sounds good."    
                    elif Girl == KittyX:
                            ch_k "Sure, sounds fun."   
                    elif Girl == EmmaX:
                            ch_e "She'd be lovely company."    
                    elif Girl == LauraX:                   
                            ch_l "Sure, more's the merrier, I guess."             
            elif Count >= 750:
                    $ Girl.FaceChange("bemused")
                    if Girl == RogueX:  
                            ch_r "Oh, nice. . ."               
                    elif Girl == KittyX:
                            ch_k "Hm, yeah. . ."      
                    elif Girl == EmmaX:
                            ch_e "Hmmm, you have good taste. . ."
                    elif Girl == LauraX:                    
                            ch_l "Ok. . ."                              
            elif ApprovalCheck(Girl, 1300, "LO"): 
                    $ Girl.FaceChange("sad")
                    if Girl == RogueX:         
                            ch_r "If that's what you're into. . ."      
                    elif Girl == KittyX:
                            ch_k "I guess if that's what you want. . ."     
                    elif Girl == EmmaX:
                            ch_e "Oh, if that's what you'd like. . ." 
                    elif Girl == LauraX:           
                            ch_l "If you insist. . ."     
            else:
                    $ Girl.FaceChange("angry")
                    if Girl == RogueX:     
                            ch_r "Keep tryin, polecat."          
                    elif Girl == KittyX:
                            ch_k "You wish, player!"  
                    elif Girl == EmmaX:
                            ch_e "No, I don't think I would be up for that." 
                    elif Girl == LauraX:
                            ch_l "I'm out."  
                    $ Count = 0
                    return
            $ Girl.DailyActions.append("yesdouble") 
            if bg_current != "bg campus": 
                    ch_p "I'll meet you in the campus square then." 
            $ Count = 0
        
        if bg_current != "bg campus" or Current_Time != "Evening": 
                if Girl == RogueX:      
                        ch_r "Yeah, see you then!"       
                elif Girl == KittyX:
                        ch_k "K', see you then!"
                elif Girl == EmmaX:
                        ch_e "Yes, see you then."
                elif Girl == LauraX:
                        ch_l "Right."
        $ Girl.DailyActions.append("yesdate")                  
        $ Player.DailyActions.append("yesdate") 
        return
#end AskDate / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    
label Date_Stood_Up(Girl=0):
    # if "stoodup" in Girl.Traits    
    if Girl.Loc != bg_current:
            "[Girl.Name] storms into the room." 
            $ Girl.Loc = bg_current            
            call Display_Girl(Girl)            
    else:
            "[Girl.Name] turns to you." 
    $ Girl.FaceChange("confused")
    $ Girl.Statup("Love", 80, -10)
    if Girl == RogueX:           
            ch_r "What're you thinkin not showin up for our date?" 
    elif Girl == KittyX:
            ch_k "Hey, what gives? You didn't show up for our date!"
    elif Girl == EmmaX:
            ch_e "Can you explain where you were the other night?"
    elif Girl == LauraX:
            ch_l "We had plans, you didn't show."
    if "stoodup" in Girl.History:
        $ Girl.FaceChange("angry")
        $ Girl.Statup("Love", 80, -5)
    if Girl == RogueX:    
            ch_r "Again!"        
    elif Girl == KittyX:
            ch_k "Again!"
    elif Girl == EmmaX:
            ch_e "And not for the first time!"
    elif Girl == LauraX:
            ch_l "Again!"
    menu:
            extend ""
            "Oh, sorry about that, slipped my mind.":
                if ApprovalCheck(Girl, 800, "LO") or ApprovalCheck(Girl, 1200):
                        $ Girl.FaceChange("angry")
                        $ Girl.Statup("Love", 80, 5)
                        if Girl == RogueX:        
                                ch_r "Well, 'least you own up ta your mistakes."    
                        elif Girl == KittyX:
                                ch_k "I guess it can happen, but don't make a habit of it."
                        elif Girl == EmmaX:
                                ch_e "Hmph. Well at least you can be honest."
                        elif Girl == LauraX:
                                ch_l "I'll cut you a break, but don't make me cut you."
                        if "stoodup" in Girl.History:
                                $ Girl.FaceChange("sad",Eyes="side")
                                $ Girl.Statup("Obed", 80, 5)
                                if Girl == RogueX:  
                                        ch_r "You need ta shape up."           
                                elif Girl == KittyX:
                                        ch_k "You really need to get your priorities in order."   
                                elif Girl == EmmaX:
                                        ch_e "You need to do better than that, however."   
                                elif Girl == LauraX:  
                                        ch_l "Sort out your plans."  
                elif "stoodup" in Girl.History:
                        $ Girl.FaceChange("sad",Eyes="side")
                        $ Girl.Statup("Love", 80, -5)
                        $ Girl.Statup("Obed", 80, 5)
                        if Girl == RogueX:      
                                ch_r "You need ta shape up!"         
                        elif Girl == KittyX:
                                ch_k "You really need to get your priorities in order."  
                        elif Girl == EmmaX:
                                ch_e "Well you need to stop slipping up."  
                        elif Girl == LauraX:     
                                ch_l "Sort out your plans."                     
                else:
                        $ Girl.FaceChange("angry")
                        $ Girl.Statup("Obed", 80, -2)
                        $ Girl.Statup("Inbt", 60, 2) 
                        if Girl == RogueX:     
                                ch_r "\"Sorry\" ain't gonna cut it next time."       
                        elif Girl == KittyX:
                                ch_k "You'll really have to make it up to me next time."
                        elif Girl == EmmaX:
                                ch_e "The next time, an apology may not be enough."
                                ch_e "If there is a next time."
                        elif Girl == LauraX:
                                ch_l "You're in the hole on this one."
            # end "sorry"   
            
            "I can't imagine that happening, maybe you got the date wrong?":
                if "stoodup" in Girl.History and ApprovalCheck(Girl, 800, "O",Alt=[[EmmaX],900]):                       
                        $ Girl.FaceChange("confused")
                        $ Girl.Statup("Obed", 90, 15)
                        if Girl == RogueX: 
                                ch_r "What? . . No, we definitely. . ."
                                $ Girl.FaceChange("confused",Eyes="side")
                                ch_r "Hm."                                    
                        elif Girl == KittyX:
                                ch_k "Are you. . . I was sure that I. . ."  
                                $ Girl.FaceChange("confused",Eyes="side")
                                ch_k "Huh."                              
                        elif Girl == EmmaX:
                                ch_e "What? . . No, we definitely. . ."  
                                $ Girl.FaceChange("confused",Eyes="side")
                                ch_e "Hm."                            
                        elif Girl == LauraX:  
                                ch_l "i don't think. . . I pretty sure. . ."  
                                $ Girl.FaceChange("confused",Eyes="side")
                                ch_l "Eh."                                   
                elif ApprovalCheck(Girl, 700, "O",Alt=[[EmmaX],800]):
                        $ Girl.FaceChange("angry")
                        $ Girl.Statup("Obed", 80, 5)
                        $ Girl.Statup("Obed", 90, 10)
                        if Girl == RogueX:          
                                ch_r "No. . . we definitely. . ."      
                        elif Girl == KittyX:
                                ch_k "Um. . . I don't think so, but I guess it's possible. . ."    
                        elif Girl == EmmaX:
                                ch_e "No. . . we definitely. . ."     
                        elif Girl == LauraX: 
                                ch_l ". . . I don't think so, but it's possible. . ." 
                elif Girl == EmmaX and not ApprovalCheck(Girl, 700, "L"):
                        $ Girl.FaceChange("angry")
                        $ Girl.RecentActions.append("angry") 
                        $ Girl.DailyActions.append("angry")  
                        $ Girl.Statup("Love", 80, -10)
                        $ Girl.Statup("Obed", 80, -5)
                        $ Girl.Statup("Inbt", 70, 10) 
                        ch_e "Don't even try that nonsense on me, [Girl.Petname]!"
                        ch_e "I INVENTED gaslighting."
                elif Girl != EmmaX and ApprovalCheck(Girl, 500, "I"):
                        $ Girl.FaceChange("angry")
                        $ Girl.RecentActions.append("angry") 
                        $ Girl.DailyActions.append("angry")  
                        $ Girl.Statup("Love", 80, -10)
                        $ Girl.Statup("Inbt", 70, 10) 
                        if Girl == RogueX:            
                                ch_r "Don't you try and twist that around on me!"
                        elif Girl == KittyX:
                                ch_k "Pull the other one, jerk."
                        elif Girl == LauraX:
                                ch_l "Yeah right."
                else:
                        $ Girl.FaceChange("sad",Eyes="side")
                        $ Girl.RecentActions.append("angry") 
                        $ Girl.DailyActions.append("angry")  
                        $ Girl.Statup("Love", 80, -5)
                        $ Girl.Statup("Obed", 80, -5)
                        $ Girl.Statup("Inbt", 60, 5) 
                        if Girl == RogueX:       
                                ch_r "Doubt it, maybe think about a better apology."     
                        elif Girl == KittyX:
                                ch_k "Well. . . I don't think so, stop bothering me."
                        elif Girl == EmmaX:
                                ch_e "Oh, [Girl.Petname], surely you can do better than that."
                        elif Girl == LauraX:
                                ch_l "Nope, not buying it."
            #end "gaslight"
            
            "Yeah, I found something better to do.": 
                if ApprovalCheck(Girl, 1200, "LO"):
                        $ Girl.FaceChange("sad",Eyes="side")
                        $ Girl.Statup("Love", 80, -5)
                        $ Girl.Statup("Obed", 80, 5)
                        if Girl == RogueX:    
                                if "stoodup" in Girl.History:
                                        ch_r "Oh. . . "
                                        ch_r "Well, I guess you have your way. . ."                            
                                else:
                                        $ Girl.Statup("Obed", 80, 10)
                                        ch_r "Oh. . . "
                                        ch_r "just, don't do it again."        
                        elif Girl == KittyX:
                                if "stoodup" in Girl.History:
                                        ch_k "Yeah. . . "
                                        ch_k "You always seem to. . ."                            
                                else:
                                        $ Girl.Statup("Obed", 80, 10)
                                        ch_k "Well. . . "
                                        ch_k "well don't let it happen again."
                        elif Girl == EmmaX:
                                if "stoodup" in Girl.History:
                                        ch_e "Oh. . . "
                                        ch_e "This independent streaks of yours is growing tiresome. . ."                            
                                else:
                                        $ Girl.Statup("Obed", 80, 10)
                                        ch_e "Oh. . . "
                                        ch_e "don't push your luck."
                        elif Girl == LauraX:
                                if "stoodup" in Girl.History:
                                        ch_l "Yeah. . . "
                                        ch_l "That sounds like you. . ."                            
                                else:
                                        $ Girl.Statup("Obed", 80, 10)
                                        ch_l "Huh. . . "
                                        ch_l "well don't do it again."
                elif ApprovalCheck(Girl, 800, "LO"):
                        $ Girl.FaceChange("angry",Eyes="side")
                        $ Girl.Statup("Love", 80, -10)
                        $ Girl.Statup("Obed", 80, 20) 
                        if Girl == RogueX:         
                                ch_r "You can do better than that."   
                        elif Girl == KittyX:
                                ch_k "Well that's rude."
                        elif Girl == EmmaX:
                                ch_e "Surely you can do better than that."
                        elif Girl == LauraX:
                                ch_l "Maybe I did too."
                else:
                        $ Girl.FaceChange("angry")
                        $ Girl.Statup("Love", 80, -15)
                        $ Girl.Statup("Inbt", 60, 5) 
                        if Girl == RogueX:    
                                ch_r "Oh, fuck off."        
                        elif Girl == KittyX:
                                ch_k "Asshole."
                        elif Girl == EmmaX:
                                ch_e "Well then I suppose I have as well."
                        elif Girl == LauraX:
                                ch_l "Asshole."
                        $ Girl.RecentActions.append("angry") 
                        $ Girl.DailyActions.append("angry")  
            #end "something better to do"
                        
    $ Girl.Traits.remove("stoodup") 
    if "stoodup" not in Girl.History:  
            $ Girl.History.append("stoodup") 
    
#    call CleartheRoom("All",Check=1)
#    if _return >= 3:            #fix, maybe reduce this to 2 if CtR is sending returns back properly
#        #if the room is full,
#        call Remove_Girl(Girl)
#        "[Girl.Name] wanders off."        
    return
    
# End Ask Girl / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Readytogo(R=0):    
    #checks to see if you want to go on a date
    if RogueX.Loc == bg_current and "yesdate" in RogueX.DailyActions:  
            ch_r "Ready to head out?"
            $ R=1
    elif KittyX.Loc == bg_current and "yesdate" in KittyX.DailyActions:  
            ch_k "Wanna get going?"
            $ R=1
    elif EmmaX.Loc == bg_current and "yesdate" in EmmaX.DailyActions: 
            ch_e "We should be off."
            $ R=1
    elif LauraX.Loc == bg_current and "yesdate" in LauraX.DailyActions: 
            ch_l "Ready?"
            $ R=1
    menu:
        "Head out on your date?"
        "Yes":
                $ renpy.pop_call() #removes call to ReadytoGo
                $ renpy.pop_call() #removes call to Chat
                jump Campus_Entry
        "Not yet":
                if RogueX.Loc == bg_current and "yesdate" in RogueX.DailyActions:  
                        ch_r "Ok, it's getting late though."
                elif KittyX.Loc == bg_current and "yesdate" in KittyX.DailyActions:  
                        ch_k "Fine."
                elif EmmaX.Loc == bg_current and "yesdate" in EmmaX.DailyActions: 
                        ch_e "Fine, but we don't want to be late."
                elif LauraX.Loc == bg_current and "yesdate" in LauraX.DailyActions: 
                        ch_l "Ok, but we need to get going."
                else:
                        "Suit yourself."
        "Let's cancel that date, just hang out." if R:
                if RogueX.Loc == bg_current and "yesdate" in RogueX.DailyActions:  #Checks if Rogue is in
                        ch_r "Yeah, ok, that's fine."
                        $ RogueX.DailyActions.remove("yesdate")
                if KittyX.Loc == bg_current and "yesdate" in KittyX.DailyActions:  #Checks if Kitty is in
                        ch_k "Yeah, ok."
                        $ KittyX.DailyActions.remove("yesdate")    
                if EmmaX.Loc == bg_current and "yesdate" in EmmaX.DailyActions:  #Checks if Emma is in
                        ch_e "Suit yourself."
                        $ EmmaX.DailyActions.remove("yesdate")
                if LauraX.Loc == bg_current and "yesdate" in LauraX.DailyActions:  #Checks if Laura is in
                        ch_l "Ok, whatever."
                        $ LauraX.DailyActions.remove("yesdate")
    return


# Date Night //////////////////////////////////////////////////////////////////////
# Gets called from the Events whenever "yesdate" in Player.DailyActions
# Checks to see which girls show up, if more than one, they decide whether they are cool with that.
# If they are, you choose location. You can go to dinner first, or skip to movies.
# During dinner there is a check to menu, then a check to whether sexy stuff occurs
# During sexy stuff, the other girl can join in, ignore it, ot cockblock it. 
# Then you pay, during which you can cause offense by being cheap.
# Then you can pick a movie, and pay for that too, similar to dinner. 
# Then you watch the movie and potentially have sex, and again the other girl can object. 
# Then you return to campus, and can pick a girl to take home first, the other will follow. 

label DateNight(Date_Bonus=[0,0],Play_Cost=0,Date_Cost=[0,0],BO=[]): #(nee Prime_Bonus=0,Second_Bonus=0,Play_Cost=0,Prime_Cost=0,Second_Cost=0,BO=[]):
    # Called from the event menu    
    # Party[0] is the lead girl Party[1] the other. 
    # Primary_Bonus and Secondary_Bonus track the girl's love bonuses, Cost is cost of the date
    
    $ Party = [] #clears Party if there is one
    
    $ BO = ActiveGirls[:]
    while BO:
        if "yesdate" in BO[0].DailyActions:  #Checks if which girls are in
                $ Party.append(BO[0])
                $ BO[0].DailyActions.remove("yesdate")
        $ BO.remove(BO[0])
                       
    if not Party:
            "Nobody showed up, weird."
            return
       
    $ renpy.random.shuffle(Party)
    
    while len(Party) > 2:        
            # If two or more members in the party    
            #Culls down party size to two
            $ Party.remove(Party[2])
            
        
    # This portion sets the girls' clothing and mood for the date
    
    $ BO = Party[:]
    while BO:
            if "stoodup" in BO[0].History:
                        $ BO[0].History.remove("stoodup") 
            call Date_Prep(BO[0])#Rogue_Date_Prep
            $ BO.remove(BO[0])
                                       
    $ bg_current = "date" 
    call Shift_Focus(Party[0])
    call Set_The_Scene     
        
    if len(Party) >= 2:
        "As you arrive, you see [Party[0].Name] and [Party[1].Name] waiting for you."
        call Date_Crossed
        if not Party: 
                # both left
                return
        elif len(Party) < 2:
                # One stayed, but not both
                ch_p "Ok then, I guess we're ready to get going. . ."      
    else:
                "As you arrive, you see [Party[0].Name] waiting for you."  
                    
    if Party[0] == RogueX:
        ch_r "Where are we going?"
    elif Party[0] == KittyX:
        ch_k "So[KittyX.like]where would you like to go?"
    elif Party[0] == EmmaX:
        ch_e "Did you have a place in mind?"
    elif Party[0] == LauraX:
        ch_l "Where we headed?"
    
    menu:
        extend ""
        "To a restaurant.":
                $ Player.RecentActions.append("dinner")                      
                $ Player.DailyActions.append("dinner") 
        "To the movies.":
                $ Player.RecentActions.append("movie")                      
                $ Player.DailyActions.append("movie") 
        "Dinner and a movie.": 
                $ Player.RecentActions.append("dinner")                      
                $ Player.DailyActions.append("dinner") 
                $ Player.RecentActions.append("movie")                      
                $ Player.DailyActions.append("movie")
                    
    if len(Party) >= 2:
            if Party[1] == RogueX:
                    ch_r "Sounds fun."
            elif Party[1] == KittyX:
                    ch_k "K, let's get going then."
            elif Party[1] == EmmaX:
                    ch_e "Oh, lovely, shall we?"
            elif Party[1] == LauraX:
                    ch_l "Cool."
    else:
            if RogueX in Party:
                    ch_r "Sounds fun."
            elif KittyX in Party:
                    ch_k "K, let's get going then."
            elif EmmaX in Party:
                    ch_e "Oh, lovely, shall we?"
            elif LauraX in Party:
                    ch_l "Cool."
            
    show blackscreen onlayer black with dissolve
            
    if "dinner" not in Player.RecentActions:
            "You head to the local theater and check out the film listings."
            jump Date_Movies
    else:
            "You go to one of the nicer restaurants in town. The food is quality but reasonably affordable." 
            jump Date_Dinner

#End Date Start   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    
    
    
#Start Crossed Wires Sequence   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    
label Date_Crossed(Girls=[],Check=0,Count=0,Cnt=0):
    #this checks to make sure both girls are on the same page. 
    #"girls" is the girls that are not cool with a double date. 
    
    if Party[0] == RogueX and "yesdouble" not in RogueX.DailyActions:
            ch_r "What's [Party[1].Name] doing here?"
            $ Girls.append(RogueX)
    elif Party[0] == KittyX and "yesdouble" not in KittyX.DailyActions:
            ch_k "Huh? What's [Party[1].Name] doing here?"
            $ Girls.append(KittyX)
    elif Party[0] == EmmaX and "yesdouble" not in EmmaX.DailyActions:
            ch_e "Oh, hello, why is [Party[1].Name] here?"
            $ Girls.append(EmmaX)
    elif Party[0] == LauraX and "yesdouble" not in LauraX.DailyActions:
            ch_l "Hey."
            ch_l "Why's [Party[1].Name] here?"
            $ Girls.append(LauraX)
        
    if Party[1] == RogueX and "yesdouble" not in RogueX.DailyActions:
            if Girls:
                ch_r "Yeah, why's [Party[0].Name] here?"
            else:
                ch_r "What's [Party[0].Name] doing here?"
            $ Girls.append(RogueX)
    elif Party[1] == KittyX and "yesdouble" not in KittyX.DailyActions:
            if Girls:
                ch_k "Yeah, what gives?"
            else:
                ch_k "Huh? What's [Party[0].Name] doing here?"
            $ Girls.append(KittyX)
    elif Party[1] == EmmaX and "yesdouble" not in EmmaX.DailyActions:
            if Girls:
                ch_e "Yes, care to explain?"
            else:
                ch_e "Oh, hello, why is [Party[0].Name] here?"
            $ Girls.append(EmmaX)
    elif Party[1] == LauraX and "yesdouble" not in LauraX.DailyActions:
            if Girls:
                ch_l "Yeah, what's up?"
            else:
                ch_l "Hey."
                ch_l "Why's [Party[0].Name] here?"
            $ Girls.append(LauraX)
            
    if not Girls:
            #if both are fine with it, just return
            return
        
    menu:
        "I thought we could have fun together.":
                $ Check = "fun"
        "Oh, I forgot to tell you?":
                $ Check = "cute"  
        "You're both coming with me.":
                $ Check = "order"
            
        "Never mind [[ditch one or both]":
                menu:
                    "[RogueX.Name], you can go" if RogueX in Party:
                            if ApprovalCheck(RogueX, 1400, "LO"):
                                    $ RogueX.FaceChange("sad", 1)
                                    ch_r "Oh, ok, I guess. Later then?"
                                    "[RogueX.Name] heads off."
                                    call Girl_Date_Over(RogueX,0)
                            else:
                                    call Girl_Date_Over(RogueX)                
                    "[KittyX.Name], you can go" if KittyX in Party:
                            if ApprovalCheck(KittyX, 1400, "LO"):
                                    $ KittyX.FaceChange("sad", 1)
                                    ch_k "Huh? Well, ok, I guess?"
                                    "[KittyX.Name] heads off."
                                    call Girl_Date_Over(KittyX,0)
                            else:
                                    call Girl_Date_Over(KittyX)        
                    "[EmmaX.Name], you can go" if EmmaX in Party:
                            if ApprovalCheck(EmmaX, 1500, "LO"):
                                    $ EmmaX.FaceChange("sad", 1)
                                    ch_e "Hm. You'll have to make this up to me later."
                                    "[EmmaX.Name] walks off."
                                    call Girl_Date_Over(EmmaX,0)
                            else:
                                    call Girl_Date_Over(EmmaX)    
                    "[LauraX.Name], you can go" if LauraX in Party:
                            if ApprovalCheck(LauraX, 1500, "LO"):
                                    $ LauraX.FaceChange("sad", 1)
                                    ch_l "This choice will have consequences."
                                    "[LauraX.Name] walks off."
                                    call Girl_Date_Over(LauraX,0)
                            else:
                                    call Girl_Date_Over(LauraX)  
                    "Never mind. [[Go home]": 
                            if RogueX in Party:
                                    if ApprovalCheck(RogueX, 1400, "LO"):
                                        $ RogueX.FaceChange("sad", 1)
                                        ch_r "Oh, ok, I guess. Later then?"
                                        call Girl_Date_Over(RogueX,0)
                                    else:
                                        call Girl_Date_Over(RogueX)                
                            if KittyX in Party:
                                    if ApprovalCheck(KittyX, 1400, "LO"):
                                        $ KittyX.FaceChange("sad", 1)
                                        ch_k "Huh? Well, ok, I guess?"
                                        call Girl_Date_Over(KittyX,0)
                                    else:
                                        call Girl_Date_Over(KittyX)        
                            if EmmaX in Party:
                                    if ApprovalCheck(EmmaX, 1500, "LO"):
                                        $ EmmaX.FaceChange("sad", 1)
                                        ch_e "Hm. You'll have to make this up to me later."
                                        call Girl_Date_Over(EmmaX,0)
                                    else:
                                        call Girl_Date_Over(EmmaX)     
                            if LauraX in Party:
                                    if ApprovalCheck(LauraX, 1500, "LO"):
                                        $ LauraX.FaceChange("sad", 1)
                                        ch_l "This choice will have consequences."
                                        call Girl_Date_Over(LauraX,0)
                                    else:
                                        call Girl_Date_Over(LauraX) 
                            "You head back to your room."
                            if "yesdate" in Player.DailyActions:
                                    $ Player.DailyActions.remove("yesdate")
                            $ bg_current = "bg player"
                            jump Misplaced                                
                return
    #end question menu
        
    $ Cnt = 2
    while Cnt:    
            #checks to see whether each girls stays or goes
            #assumes that this process starts with two girls, Party[0] and [1]
            $ Cnt -= 1 #first time through is 1, second time through is 0, then out
            if len(Party) < 2:
                    #if the other girl's dropped out
                    if not ApprovalCheck(Party[0], 1000,Alt=[[EmmaX,LauraX],800]):
                            #if the remaining girl isn't interested, this quits out.
                            if Party[0] == RogueX: 
                                    ch_r "So. . . I'm going to get going too?"
                            elif Party[0] == KittyX:         
                                    ch_k "Yeah, this is kind of a weird scene, maybe I'll see you later?"      
                            elif Party[0] == EmmaX:      
                                    ch_e "Unprofessional, but I do give you points for trying."           
                            elif Party[0] == LauraX:
                                    ch_l "You need to plan better."
                                    ch_l "Almost seems like you did that on purpose."
                            call Girl_Date_Over(Party[0],0)
                    return                
                                   
            if Check == "fun":
                    if ApprovalCheck(Party[Cnt],1000):
                        $ Check = 0
                    else:
                        $ Check = -200
            elif Check == "cute":  
                    if ApprovalCheck(Party[Cnt],1000,"LI"):
                        $ Check = 200
                    else:
                        $ Check = -100
            elif Check == "order":
                    if ApprovalCheck(Party[Cnt],1200,"LO"):
                        $ Check = 100
                    else:
                        $ Check = -300
            else:
                        $ Check = 0
            
            if Cnt == 1:
                    $ Count = 0
            else:
                    $ Count = 1
                
            if ApprovalCheck(Party[Cnt], 800, "OI", Bonus = Check) and Party[Cnt].GirlLikeCheck(Party[Count]) >= 600: 
                    # if the current iteration is 1, then it's Party[1].LikesParty[0]
                    # if the current iteration is 0, then it's Party[0].LikesParty[1]
                    $ Party[Cnt].FaceChange("smile")
                    if Party[Cnt] == RogueX: 
                            ch_r "Sure, why not."   
                    elif Party[Cnt] == KittyX: 
                            ch_k "Sure, sounds fun."               
                    elif Party[Cnt] == EmmaX:   
                            ch_e "Alright, I'm in"                 
                    elif Party[Cnt] == LauraX:   
                            ch_l "This could be fun. . ."     
            elif Party[Cnt].GirlLikeCheck(Party[Count]) >= 750:
                    $ Party[Cnt].FaceChange("bemused")                
                    if Party[Cnt] == RogueX:
                            ch_r "Oh, I guess. . ."  
                    elif Party[Cnt] == KittyX:   
                            ch_k "Hm, yeah. . ."               
                    elif Party[Cnt] == EmmaX:   
                            ch_e "This could be interesting. . ."               
                    elif Party[Cnt] == LauraX:
                            ch_l "Nice"    
            elif ApprovalCheck(Party[Cnt], 1300, "LO", Bonus = Check): 
                    $ Party[Cnt].FaceChange("sad")                
                    if Party[Cnt] == RogueX: 
                            ch_r "If you insist. . ."  
                    elif Party[Cnt] == KittyX:          
                            ch_k "I guess if that's what you want. . ."     
                    else:      
                            call AnyLine(Party[Cnt],"If you insist.")
            else:
                    $ Party[Cnt].FaceChange("angry")                
                    if Party[Cnt] == RogueX: 
                            ch_r "In your dreams!"  
                    elif Party[Cnt] == KittyX:   
                            ch_k "You wish, player!"             
                    elif Party[Cnt] == EmmaX:   
                            $ Party[Cnt].FaceChange("surprised",Mouth="smirk")
                            ch_e "Oh, you do aim high."
                            $ Party[Cnt].FaceChange("angry")
                            ch_e "Too high."              
                    elif Party[Cnt] == LauraX:
                            $ Party[Cnt].FaceChange("surprised",Mouth="smirk")
                            ch_l "Really?"
                            $ Party[Cnt].FaceChange("angry")
                            ch_l "That's your play here."
                    call Girl_Date_Over(Party[Cnt],0)
    #end check to see if they're cool with this. . .                
    return
#End Crossed Wires Sequence   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    

label Date_Prep(Girl=0):
    #This gets rthe girl Dressed and ready for Dinner, called by Date_Night
    if Girl not in TotalGirls:
            "Tell Oni this girl called without a target girl."
            return
    $ Taboo = 40
    $ Girl.Taboo = 40
    if Girl.Clothing[7]:
            # if she has a date outfit set
            if Girl.Clothing[7] == 2:
                    $ Girl.Outfit = "casual2"
            elif Girl.Clothing[7] == 3:
                    $ Girl.Outfit = "custom1"
            elif Girl.Clothing[7] == 4:
                    $ Girl.Outfit = "gym"
            elif Girl.Clothing[7] == 5:
                    $ Girl.Outfit = "custom2"
            elif Girl.Clothing[7] == 6:
                    $ Girl.Outfit = "custom3"
            else:
                    $ Girl.Outfit = "casual1"
    else:
            $ Options = ["casual2", "casual1"]
            $ Options.append("custom1") if Girl.Custom1[0] == 2 else Options
            $ Options.append("custom2") if Girl.Custom2[0] == 2 else Options
            $ Options.append("custom3") if Girl.Custom3[0] == 2 else Options
            $ renpy.random.shuffle(Options) 
            $ Girl.Outfit = Options[0]
            $ del Options[:]  
    $ Girl.Loc = "date"
    $ Girl.OutfitChange(Changed=1)
    $ Girl.FaceChange("smile")
    return

# End Rogue Prep / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

    
#Start Dinner Sequence   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Date_Dinner:    
    $ bg_current = "bg restaurant"
    $ BO = Party[:]
    while BO:
        $ BO[0].Loc = "bg restaurant"
        $ BO.remove(BO[0])
        
    call Set_The_Scene
    
    "The waitress comes to the table."
    
    $ BO = Party[:]
    while BO:
        call expression BO[0].Tag + "_Dinner"
        $ BO.remove(BO[0])
    call Player_Dinner
               
    "After a bit, the waitress brings you your meals."
    
    $ Line = "You eat your " + Line
    
    if KittyX in Party and "surfturf" in KittyX.RecentActions: 
            $ Line = Line + ", "+KittyX.Name+" eats the steak but pushes the lobster to the side."
    else:
            $ Line = Line + ", and have a pleasant conversation over the meal."
             
    "[Line]"    
    $ Player.RecentActions.append("dinner") 
    
    call Dinner_Sex
    
    call Date_Paying("dinner") 
    
    if not Party:
            "You decide to head back to your room."
            jump Date_Over

    if "movie" not in Player.RecentActions:
            jump Date_End
            
    #else:    
    "After dinner, you head to the local theater and check out the film listings."   
    jump Date_Movies
    
    
# End Primary Dinner Sequence / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Player_Dinner:
    # This is the player's menu choices
    menu:
        "For yourself, you order. . ."
        "Surf and turf. ($20)":
            $ Play_Cost = 20
            $ Line = "steak and a juicy lobster"
        "Steak. ($15)":  
            $ Play_Cost = 15
            $ Line = "medium rare ribeye"
        "Chicken. ($10)":
            $ Play_Cost = 10
            $ Line = "pangrilled chicken thighs"
        "Just a salad. ($5)":
            $ Play_Cost = 5
            $ Line = "fresh garden salad"
    return


# Start Rogue Dinner Menu/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /       
label Rogue_Dinner(GirlCost=0):
    #Called by Date Dinner, picked Rogue's food
    menu:
        "For [RogueX.Name] you order. . ."
        "Surf and turf. ($20)":
                $ RogueX.FaceChange("smile", Brows = "surprised")
                ch_r "Ooh, you're really pulling out the stops here."  
                $ RogueX.FaceChange()
                $ RogueX.Statup("Love", 80, 5)
                $ RogueX.Statup("Love", 200, 2)
                $ GirlCost = 20
                $ RogueX.RecentActions.append("surfturf")
        "Steak. ($15)":  
                $ RogueX.FaceChange("smile")
                ch_r "I love a big, juicy steak."
                $ RogueX.Statup("Love", 80, 5)
                $ GirlCost = 15
                $ RogueX.RecentActions.append("ribeye")
        "Chicken. ($10)":
                $ RogueX.FaceChange("smile")
                ch_r "I could always go for some chicken."
                $ RogueX.Statup("Love", 50, 1)
                $ RogueX.Statup("Love", 80, 3)
                $ GirlCost = 10
                $ RogueX.RecentActions.append("chicken")
        "Just a salad. ($5)":
                $ RogueX.Mouth = "sad"
                $ RogueX.Eyes = "sexy"
                $ RogueX.Brows = "confused"            
                ch_r "Well, I guess salad isn't that bad. . ."  
                $ RogueX.Statup("Love", 60, -5)
                $ RogueX.Statup("Obed", 50, 2)
                $ GirlCost = 5
                $ RogueX.RecentActions.append("salad")
        "Why don't you choose, [RogueX.Name]?":
                call Date_Bonus(RogueX,2)
                $ RogueX.FaceChange("smile")
                ch_r "Well thanks, [RogueX.Petname]. I think I'll have the chicken."            
                $ RogueX.Statup("Love", 80, 5)        
                $ RogueX.Statup("Inbt", 50, 3)
                $ RogueX.Statup("Obed", 50, -2)
                $ GirlCost = 10
                $ RogueX.RecentActions.append("chicken")
                
    if Party[0] == RogueX:
            $ Date_Cost[0] = GirlCost
    else:
            $ Date_Cost[1] = GirlCost
    call Date_Bonus(RogueX,GirlCost)
    return
# End Rogue Menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /          

# Start Kitty Dinner Menu/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /       
label Kitty_Dinner(GirlCost=0):
    #Called by Date Dinner, picked Kitty's food
    menu:
        "For [KittyX.Name] you order. . ."
        "Surf and turf. ($20)":
                $ KittyX.FaceChange("sad",Brows = "surprised")
                ch_k "Um, I[KittyX.like]don't really eat shellfish. . ."  
                $ KittyX.FaceChange()
                $ KittyX.Statup("Love", 80, -5)
                $ KittyX.Statup("Love", 200, -2)
                $ GirlCost = 20
                call Date_Bonus(KittyX,-11)
                $ KittyX.RecentActions.append("surfturf")
        "Steak. ($15)":  
                $ KittyX.FaceChange("smile")
                ch_k "Sounds delish."
                $ KittyX.Statup("Love", 80, 5)
                $ KittyX.Statup("Love", 200, 2)
                $ GirlCost = 15
                $ KittyX.RecentActions.append("ribeye")
        "Chicken. ($10)":
                $ KittyX.FaceChange("smile")
                ch_k "Chicken's fine."
                $ KittyX.Statup("Love", 50, 1)
                $ KittyX.Statup("Love", 80, 3)
                $ GirlCost = 10
                $ KittyX.RecentActions.append("chicken")
        "Just a salad. ($5)":
                $ KittyX.Mouth = "sad"
                $ KittyX.Eyes = "sexy"
                $ KittyX.Brows = "confused"            
                ch_k "I do enjoy a nice salad."  
                $ KittyX.Statup("Love", 60, -3)
                $ KittyX.Statup("Obed", 50, 2)
                $ GirlCost = 5
                $ KittyX.RecentActions.append("salad")
        "Why don't you choose, [KittyX.Name]?":
                call Date_Bonus(KittyX,2)
                $ KittyX.FaceChange("smile")
                ch_k "Well thanks, [KittyX.Petname]. I think I'll have the steak."            
                $ KittyX.Statup("Love", 80, 7)   
                $ KittyX.Statup("Love", 200, 2) 
                $ GirlCost = 15
                $ KittyX.RecentActions.append("ribeye")
    if Party[0] == KittyX:
        $ Date_Cost[0] = GirlCost
    else:
        $ Date_Cost[1] = GirlCost
    call Date_Bonus(KittyX,GirlCost)
    return
# End Kitty Menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /      

# Start Emma Dinner Menu/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /       
label Emma_Dinner(GirlCost=0):
    #Called by Date Dinner, picked Emma's food
    menu:
        "For [EmmaX.Name] you order. . ."
        "Surf and turf. ($20)":
                $ EmmaX.FaceChange("sly")
                ch_e "Hmm, a refined choice."  
                $ EmmaX.FaceChange()
                $ EmmaX.Statup("Love", 80, 7)
                $ EmmaX.Statup("Love", 200, 3)
                $ GirlCost = 20
                $ EmmaX.RecentActions.append("surfturf")
        "Steak. ($15)":  
                $ EmmaX.FaceChange("smile")
                ch_e "I do enjoy tender meat."
                $ EmmaX.Statup("Love", 80, 5)
                $ GirlCost = 15
                $ EmmaX.RecentActions.append("ribeye")
        "Chicken. ($10)":
                $ EmmaX.FaceChange("smile")
                ch_e "Chicken is fine."
                $ EmmaX.Statup("Love", 50, 1)
                $ EmmaX.Statup("Love", 80, 3)
                $ GirlCost = 10
                $ EmmaX.RecentActions.append("chicken")
        "Just a salad. ($5)":
                $ EmmaX.Mouth = "sad"
                $ EmmaX.Eyes = "sexy"
                $ EmmaX.Brows = "confused"            
                ch_e "I suppose I could go for a salad. . ."  
                $ EmmaX.Statup("Love", 60, -3)
                $ EmmaX.Statup("Obed", 50, -2)
                $ GirlCost = 5
                $ EmmaX.RecentActions.append("salad")
        "Why don't you choose, [EmmaX.Name]?":
                call Date_Bonus(EmmaX,2)
                $ EmmaX.FaceChange("smile")
                ch_e "Thank you, [EmmaX.Petname]. I believe I'll have the steak."     
                $ EmmaX.FaceChange("sly")  
                ch_e ". . .and the lobster, of course." 
                $ EmmaX.Statup("Love", 80, 5)        
                $ EmmaX.Statup("Inbt", 50, 3)
                $ EmmaX.Statup("Obed", 50, -2)
                $ GirlCost = 20
                $ EmmaX.RecentActions.append("surfturf")
                
    if Party[0] == EmmaX:
        $ Date_Cost[0] = GirlCost
    else:
        $ Date_Cost[1] = GirlCost
    call Date_Bonus(EmmaX,GirlCost)
    return
# End Emma Menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /     

# Start Laura Dinner Menu/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /       
label Laura_Dinner(GirlCost=0):
    #Called by Date Dinner, picked Laura's food
    menu:
        "For [LauraX.Name] you order. . ."
        "Surf and turf. ($20)":
                $ LauraX.FaceChange("sad",Brows = "surprised")
                ch_l "Nice. . ."  
                $ LauraX.FaceChange()
                $ LauraX.Statup("Love", 80, 5)
                $ LauraX.Statup("Love", 90, 2)
                $ GirlCost = 20
                $ LauraX.RecentActions.append("surfturf")
        "Steak. ($15)":  
                $ LauraX.FaceChange("smile")
                ch_l "Rare."
                $ LauraX.Statup("Love", 80, 5)
                $ LauraX.Statup("Love", 90, 2)
                $ GirlCost = 15
                $ LauraX.RecentActions.append("ribeye")
        "Chicken. ($10)":
                $ LauraX.FaceChange("smile")
                ch_l "Yeah, ok."
                $ LauraX.Statup("Love", 50, 1)
                $ LauraX.Statup("Love", 80, 3)
                $ GirlCost = 10
                $ LauraX.RecentActions.append("chicken")
        "Just a salad. ($5)":
                $ LauraX.Mouth = "sad"
                $ LauraX.Eyes = "sexy"
                $ LauraX.Brows = "confused"            
                ch_l "Um. no."  
                $ LauraX.Statup("Love", 60, -5)
                $ LauraX.Statup("Obed", 50, -2)
                $ LauraX.Statup("Inbt", 60, 2) 
                ch_l "Steak, rare."
                $ GirlCost = 15
                $ LauraX.RecentActions.append("ribeye")
        "Why don't you choose, [LauraX.Name]?":
                call Date_Bonus(LauraX,2)
                $ LauraX.FaceChange("smile")
                ch_l "Thanks. I think I'll have the steak."            
                $ LauraX.Statup("Love", 80, 7)   
                $ LauraX.Statup("Obed", 60, 2)
                $ LauraX.Statup("Love", 200, 2) 
                $ GirlCost = 15
                $ LauraX.RecentActions.append("ribeye")
                
    if Party[0] == LauraX:
        $ Date_Cost[0] = GirlCost
    else:
        $ Date_Cost[1] = GirlCost
    call Date_Bonus(LauraX,GirlCost)
    return
# End Laura Menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    

# Start Dinner Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Dinner_Sex(Girl=0,Previous=0,GirlBonus=0,OptionsDS=[],BO=[]):
    #Called by Dinner Sex
    
    $ BO = Party[:]
    if 0 in BO:
        $ BO.remove(0)
    while BO:
            if ApprovalCheck(BO[0], 1000):  #Checks if BO[0] is in
                    $ OptionsDS.append(BO[0])   
                    if Party[0] == BO[0] and Date_Bonus[0] > 10:
                            $ OptionsDS.append(BO[0])
                    elif BO[0] in Party and Date_Bonus[1] > 10:
                            $ OptionsDS.append(BO[0])              
            $ BO.remove(BO[0])
            
    if len(OptionsDS) == 0:
            #if nobody is in, return
            return
        
    $ renpy.random.shuffle(OptionsDS)
    
    $ Girl = OptionsDS[0]               #picks lead
    while Girl in OptionsDS:            #culls list down to other girl, if there is one
            $ OptionsDS.remove(Girl)            
        
    if OptionsDS:                       #if anyone's left, make her Previous
            $ Previous = OptionsDS[0]
    
    $ OptionsDS =["nothing"]
            
    if Party[0] == Girl:
        $ GirlBonus = Date_Bonus[0] + Date_Cost[0]
    else:
        $ GirlBonus = Date_Bonus[1] + Date_Cost[1]
        
    if Girl.Anal and ApprovalCheck(Girl, 1500) and GirlBonus >=15: 
            $ OptionsDS.append("anal")        
    if Girl.Sex and ApprovalCheck(Girl, 1500) and GirlBonus >=10:
            $ OptionsDS.append("sex")
    if Girl.Blow and ApprovalCheck(Girl, 1300) and GirlBonus >=10:
            $ OptionsDS.append("blow")      
    if Girl.Hand and ApprovalCheck(Girl, 1000) and GirlBonus >=10:
            $ OptionsDS.append("hand")
    if Girl.FondleP and ApprovalCheck(Girl, 1000) and GirlBonus >=10:
            $ OptionsDS.append("pussy")
    if ApprovalCheck(Girl, 1000) and GirlBonus >=10:
            $ OptionsDS.append("foot")
            
    $ renpy.random.shuffle(OptionsDS) 
    
    $ Girl.FaceChange("sexy")
    if OptionsDS[0] == "nothing":
        pass
    elif OptionsDS[0] == "anal":        
        "Halfway through the meal, [Girl.Name] gets a sly look on her face." 
        "She nods her head suggestively towards the restrooms, and then excuses herself."
        call Date_Sex_Break(Girl,Previous)
        if _return == 4: #you refused
                $ Girl.FaceChange("sadside", 2)
                "You wait a few minutes until she returns, seemingly a bit annoyed at you."
                $ Girl.Statup("Love", 90, -5)
                $ Girl.Statup("Inbt", 80, -10)
                call Date_Bonus(Girl,-5)
        else:
                if _return == 1: #other girl is fine
                        "A few seconds later, you and [Previous.Name] follow her and she drags you both inside, locking the door behind you." 
                        "She spends the next several minutes taking it up the ass while [Previous.Name] feels you both up."
                        $ Girl.GLG(Previous,1000,3,1)
                        $ Previous.GLG(Girl,1000,2,1)
                else:
                        "A few seconds later, you follow her and she drags you inside, locking the door behind you." 
                        "She spends the next several minutes taking it up the ass."
                if _return == 3:
                        "[Previous.Name] stares daggers at you both as you return to the table."
                        call Date_Bonus(Previous,-10)
                if Girl == RogueX:         
                        ch_r "I hope I'll still be able to sit down later."  
                elif Girl == KittyX:
                        ch_k "That was {i}so{/i} worth it."  
                elif Girl == EmmaX:
                        ch_e "Thank you for helping with the stuffing, [Girl.Petname]."  
                elif Girl == LauraX:   
                        ch_l "Worth it."                  
                $ Girl.Statup("Inbt", 50, 9)
                $ Girl.Statup("Inbt", 80, 3)
                $ Girl.SeenPeen += 1
                $ Girl.Anal += 1
                $ Player.Semen -= 1
                $ Girl.RecentActions.append("anal")    
                $ Girl.RecentActions.append("dinnersex")                    
                $ Girl.DailyActions.append("anal") 
    elif OptionsDS[0] == "sex":        
        "Halfway through the meal, [Girl.Name] gets a sly look on her face." 
        "She nods her head suggestively towards the restrooms, and then excuses herself."
        call Date_Sex_Break(Girl,Previous)
        if _return == 4: #you refused
                $ Girl.FaceChange("sadside", 2)
                "You wait a few minutes until she returns, seemingly a bit annoyed at you."
                $ Girl.Statup("Love", 90, -5)
                $ Girl.Statup("Inbt", 80, -10)
                call Date_Bonus(Girl,-5)
        else:
                if _return == 1: #other girl is fine
                        "A few seconds later, you and [Previous.Name] follow her and she drags you both inside, locking the door behind you." 
                        "She spends the next several minutes fucking you raw while [Previous.Name] feels you both up." 
                        $ Girl.GLG(Previous,1000,3,1)
                        $ Previous.GLG(Girl,1000,2,1) 
                else:
                        "A few seconds later, you follow her and she drags you inside, locking the door behind you." 
                        "She spends the next several minutes fucking you raw."
                if _return == 3:
                        "[Previous.Name] stares daggers at you both as you return to the table."
                        call Date_Bonus(Previous,-10)
                if Girl == RogueX:       
                        ch_r "I needed to work off that meal a bit."  
                elif Girl == KittyX:
                        ch_k "That was a workout."
                elif Girl == EmmaX:
                        ch_e "A little after dinner workout never hurt."
                elif Girl == LauraX: 
                        ch_l "Sorry about the scratches."
                $ Girl.Statup("Inbt", 50, 8)
                $ Girl.Statup("Inbt", 80, 2)
                $ Girl.SeenPeen += 1
                $ Girl.Sex += 1
                $ Player.Semen -= 1            
                $ Girl.RecentActions.append("sex")   
                $ Girl.RecentActions.append("dinnersex")                    
                $ Girl.DailyActions.append("sex") 
    elif OptionsDS[0] == "blow":
        "Halfway through the meal, [Girl.Name] gets a sly look on her face, then knocks her fork off the table."
        "She ducks under the table after it, and unzips your pants." 
        call Date_Sex_Break(Girl,Previous)
        if _return == 4: #you refused
                $ Girl.FaceChange("sadside", 2)
                "You zip them back up and shoo her away. She gets back up from under the table."
                $ Girl.Statup("Love", 90, -5)
                $ Girl.Statup("Inbt", 80, -5)
                call Date_Bonus(Girl,-3)
                if Girl == EmmaX:
                        $ Girl.Statup("Obed", 70, 5)
                        ch_e "Found it. . ."
        else:
                if _return == 1: 
                        #other girl is fine
                        "[Previous.Name] shifts closer and wraps one arm around you, the other hand caressing [Girl.Name]'s cheek."
                        "[Girl.Name] then procedes to blow you for several minutes until you cum."
                        $ Girl.GLG(Previous,1000,2,1)
                        $ Previous.GLG(Girl,1000,1,1)
                elif _return == 2: #other girl is fine
                        "She then procedes to blow you for several minutes until you cum, while [Previous.Name] pretends to be occupied."
                else: 
                        "She then procedes to blow you for several minutes until you cum."
                $ Girl.Statup("Inbt", 50, 6)
                $ Girl.Statup("Inbt", 80, 2)
                $ Girl.RecentActions.append("blow")   
                $ Girl.RecentActions.append("dinnersex")                    
                $ Girl.DailyActions.append("blow") 
                if Girl.Swallow:
                    "[Girl.Name] wipes her mouth as she climbs out from under the table."
                    if Girl == RogueX:      
                            ch_r "I don't think we need desert, [Girl.Petname]."     
                    elif Girl == KittyX:
                            ch_k "That hit the spot. . ."            
                    elif Girl == EmmaX:
                            ch_e "Hmm, a creamy aperitif."          
                    elif Girl == LauraX:   
                            ch_l "Yum. . ."    
                    $ Girl.Addict -= 20
                    $ Girl.Swallow += 1  
                    $ Girl.RecentActions.append("swallow")                      
                    $ Girl.DailyActions.append("swallow")       
                else:
                    "[Girl.Name] grabs the napkin off your lap and uses it to collect the jiz."
                    if Girl == RogueX:     
                            ch_r "I bet the cleaning crew will enjoy that."    
                    elif Girl == KittyX:
                            ch_k "I feel kinda sorry for the busboys."
                    elif Girl == EmmaX:
                            ch_e "I suppose that is a bit rude to the help."
                    elif Girl == LauraX:
                            ch_l "Sorry about the mess."
                $ Girl.Statup("Inbt", 30, 4)
                $ Girl.Statup("Inbt", 80, 2)
                $ Girl.SeenPeen += 1
                $ Girl.Blow += 1
                $ Player.Semen -= 1
                if _return == 3:
                    "[Previous.Name] stares daggers at you both as [Girl.Name] crawls out from under the table."  
                    call Date_Bonus(Previous,-10)
    elif OptionsDS[0] == "hand":
        "Halfway through the meal, [Girl.Name] gets a sly look on her face, then shifts her chair around next to yours."
        call Date_Sex_Break(Girl,Previous)
        if _return == 4: 
                #you refused
                $ Girl.FaceChange("sadside", 2)
                "She tries to unzip your pants under the table, but you shoo her away."
                $ Girl.Statup("Love", 90, -5)
                $ Girl.Statup("Inbt", 80, -5)
                call Date_Bonus(Girl,-2)
        else:
                if _return == 1: #other girl is fine
                        "She unzips your pants under the table, and proceeds to caress your cock."
                        "On the other side, [Previous.Name] also reaches down and gets into the action."
                        $ Line = "They"
                        $ Previous.Hand += 1
                        $ Previous.RecentActions.append("hand")                     
                        $ Previous.DailyActions.append("hand") 
                        $ Girl.GLG(Previous,600,3,1)
                        $ Previous.GLG(Girl,600,2,1)
                        $ Girl.GLG(Previous,1000,2,1)
                        $ Previous.GLG(Girl,1000,1,1)
                elif _return == 2: #other girl is fine
                        "She unzips your pants under the table, and proceeds to caress your cock, while [Previous.Name] pretends to be occupied."
                        $ Line = "She"
                else: 
                        "She unzips your pants under the table, and proceeds to caress your cock."
                        $ Line = "She"
                if Girl.Blow and ApprovalCheck(Girl, 1200):
                        "Just as you're about to cum, [Girl.Name] ducks her head under the table and comes up with a mouth full."
                        $ Girl.SeenPeen += 1
                        $ Girl.Blow += 1
                        $ Girl.Addict -= 20
                        $ Girl.Swallow += 1  
                        $ Girl.RecentActions.append("swallow")                      
                        $ Girl.DailyActions.append("swallow")   
                else:
                        "[Line] continues stroking it until you cum into the napkin."
                $ Line = 0
                if Girl == RogueX:       
                        ch_r "I bet the cleaning crew will enjoy that."  
                elif Girl == KittyX:
                        ch_k "I feel kinda sorry for the busboys."
                elif Girl == EmmaX:
                        ch_e "I bet the cleaning crew will enjoy that."
                elif Girl == LauraX:
                        ch_l "Sorry about the mess."
                $ Girl.Statup("Inbt", 30, 4)
                $ Girl.Statup("Inbt", 80, 2)
                $ Girl.Hand += 1
                $ Player.Semen -= 1
                $ Girl.RecentActions.append("hand")                     
                $ Girl.DailyActions.append("hand") 
                if _return == 3:
                    "[Previous.Name] stares daggers at you both from across the table."
                    call Date_Bonus(Previous,-5)
    elif OptionsDS[0] == "pussy":
        "Halfway through the meal, [Girl.Name] gets a sly look on her face, then shifts her chair around next to yours."
        call Date_Sex_Break(Girl,Previous)
        if _return == 4: 
                #you refused
                if Girl.Legs:
                    "She takes your hand and pulls it over to her crotch, shoving it under her [Girl.Legs]."
                else:
                    "She takes your hand and shoves it into her crotch."
                $ Girl.FaceChange("sadside", 2)
                "With a glance at [Previous.Name], you jerk your hand away."
                $ Girl.Statup("Love", 90, -5)
                $ Girl.Statup("Inbt", 80, -5)
                call Date_Bonus(Girl,-3)
        else:
                if Girl.Legs:
                        "She takes your hand and pulls it over to her crotch, shoving it under her [Girl.Legs]."
                else:
                        "She takes your hand and shoves it into her crotch."
                "You can feel that she's warm as a furnace."
                if _return == 1:
                        #other girl is in on it
                        "On the other side, [Previous.Name] also reaches down and gets into the action."
                        "You both stroke her pussy for several minutes, until finally she shudders in orgasm." 
                        "You slowly pulls your hands free with a sly smile."
                        $ Girl.GLG(Previous,700,6,1)
                        $ Girl.GLG(Previous,1000,6,1)
                        $ Previous.GLG(Girl,1000,2,1)
                else: 
                        "You stroke her pussy for several minutes, until finally she shudders in orgasm." 
                        "You slowly pulls your hand free with a sly smile."
                if _return == 3:
                    call Date_Bonus(Previous,-3)
                if Girl == RogueX:         
                        ch_r "I needed to take a bit of the edge off, [Girl.Petname]."
                elif Girl == KittyX:
                        ch_k "Thanks, [Girl.Petname], I needed that."
                elif Girl == EmmaX:
                        ch_e "Ah, that was lovely, [Girl.Petname]."
                elif Girl == LauraX:
                        ch_l "Oof, that was nice."
                if _return == 1:
                        #if the other girl joined in. . .
                        if Girl == RogueX:   
                                ch_r "Thanks to you too, [Previous.Name]."      
                        elif Girl == KittyX:
                                ch_k "You too, [Previous.Name]."
                        elif Girl == EmmaX:
                                ch_e "And thank you as well, [Previous.Name]."
                        elif Girl == LauraX:       
                                ch_l "You too, [Previous.Name]." 
                        $ Girl.Les += 1
                        $ Previous.Les += 1     
                $ Girl.Statup("Love", 90, 3)
                $ Girl.Statup("Inbt", 30, 5)            
                $ Girl.Statup("Inbt", 90, 2)
                $ Girl.FondleP += 1
                $ Girl.Org += 1
                $ Girl.RecentActions.append("fondle pussy") 
                $ Girl.RecentActions.append("dinnersex")                      
                $ Girl.DailyActions.append("fondle pussy") 
    elif OptionsDS[0] == "foot":
        "Halfway through the meal, [Girl.Name] gets a sly look on her face, then shifts a bit lower in her seat."
        "You suddenly feel her foot in your lap, gently caressing your cock."
        call Date_Sex_Break(Girl,Previous)
        if _return == 4: #you refused
                $ Girl.FaceChange("sadside", 2)
                "You shift uncomfortably and push her foot away."
                $ Girl.Statup("Love", 90, -5)
                $ Girl.Statup("Inbt", 80, -3)
                call Date_Bonus(Girl,-1)
        else:
                $ Player.Statup("Focus", 60, 10)
                if _return == 1: #other girl is fine
                        "[Previous.Name] decides to join in the fun and adds her foot to the mix."
                        $ Player.Statup("Focus", 60, 5)
                        $ Girl.GLG(Previous,1000,2,1)
                        $ Previous.GLG(Girl,1000,1,1)
                if _return == 3:
                        call Date_Bonus(Previous,-3)
                "After several minutes of this, she pulls back."
                if Girl == RogueX:      
                        ch_r "Just a little downpayment on later, [Girl.Petname]."   
                elif Girl == KittyX:
                        ch_k "Just a taste of things to come, [Girl.Petname]."
                elif Girl == EmmaX:
                        ch_e "Patience. . . [Girl.Petname]."
                elif Girl == LauraX:
                        ch_l "I've got plans for tonight, [Girl.Petname]."
                $ Girl.Statup("Inbt", 80, 3)
                $ Girl.RecentActions.append("dinnersex") 
    
    $ Girl.Blush = 0
    return    
# End Dinner Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    

    
    
        
#Start Movie Sequence   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /        
label Date_Movies:  
    #This picks and watches a movie
    $ bg_current = "bg movies"
    $ BO = Party[:]
    while BO:
        $ BO[0].Loc = "bg movies"
        $ BO.remove(BO[0])
        
    call Set_The_Scene 
    
    menu:
        "What would you like to see?"
        "A romantic comedy.":
            $ Line = "romcom"
            $ Player.RecentActions.append("romcom")
        "An action movie.":
            $ Line = "action"
            $ Player.RecentActions.append("action")
        "A horror movie.":
            $ Line = "horror"
            $ Player.RecentActions.append("horror")
        "An acclaimed drama.":
            $ Line = "drama" 
            $ Player.RecentActions.append("drama")
        "Let [RogueX.Name] pick." if RogueX in Party:
            $ Line = "pick"
            $ Trigger = RogueX
        "Let [KittyX.Name] pick." if KittyX in Party:
            $ Line = "pick"
            $ Trigger = KittyX
        "Let [EmmaX.Name] pick." if EmmaX in Party:
            $ Line = "pick"
            $ Trigger = EmmaX
        "Let [LauraX.Name] pick." if LauraX in Party:
            $ Line = "pick"
            $ Trigger = LauraX
    
    
    if Line == "pick":
            #if you let one of the girls pick the movie
            $ Trigger.FaceChange("smile")  
            if Trigger == RogueX:         
                    $ RogueX.Statup("Love", 80, 4)
                    $ RogueX.Statup("Obed", 50, -2)
                    $ RogueX.Statup("Inbt", 50, 2)  
                    ch_r "How sweet, [RogueX.Petname]. Let's see the romantic comedy." 
                    $ Line = "romcom" 
            elif Trigger == KittyX:
                    $ KittyX.Statup("Love", 80, 4)
                    $ KittyX.Statup("Obed", 50, -2)
                    $ KittyX.Statup("Inbt", 50, 2) 
                    ch_k "Aw, [KittyX.Petname]. Let's see the drama."  
                    $ Line = "drama" 
            elif Trigger == EmmaX:
                    $ EmmaX.Statup("Love", 80, 5)
                    $ EmmaX.Statup("Obed", 50, -3)
                    $ EmmaX.Statup("Inbt", 50, 3) 
                    ch_e "Oh, lovely. Let's see the horror film."     
                    $ Line = "horror" 
            elif Trigger == LauraX:  
                    $ LauraX.Statup("Love", 90, 5)
                    $ LauraX.Statup("Obed", 50, 2)
                    $ LauraX.Statup("Inbt", 50, 2) 
                    ch_e "Cool. Let's go with some action."     
                    $ Line = "action" 
            $ Player.RecentActions.append(Line)     
            call Date_Bonus(Trigger,20)
    
    if Line == "romcom":
            if RogueX in Party and Trigger != RogueX:
                    $ RogueX.FaceChange("smile", Eyes="surprised")
                    $ RogueX.Statup("Love", 50, 2)
                    $ RogueX.Statup("Love", 95, 4)
                    $ RogueX.Statup("Inbt", 50, 2)
                    ch_r "Oooh, I love a good rom-com, [RogueX.Petname]. This should be great!"  
                    call Date_Bonus(RogueX,15)
            if KittyX in Party and Trigger != KittyX:
                    $ KittyX.FaceChange("smile", Eyes="surprised")
                    $ KittyX.Statup("Love", 50, 2)
                    $ KittyX.Statup("Love", 95, 3)
                    ch_k "Aw, how cuuuute!"   
                    call Date_Bonus(KittyX,5)
            if EmmaX in Party and Trigger != EmmaX:
                    $ EmmaX.FaceChange("confused", Mouth="sad")
                    $ EmmaX.Statup("Love", 70, 2)
                    $ EmmaX.Statup("Obed", 50, 5)
                    $ EmmaX.Statup("Inbt", 70, -3)
                    ch_e "How. . . pedestrian."   
                    call Date_Bonus(EmmaX,-5)
            if LauraX in Party and Trigger != LauraX:
                    $ LauraX.FaceChange("smile", 2)
                    $ LauraX.Statup("Love", 80, 3)
                    $ LauraX.Statup("Obed", 50, 3)
                    $ LauraX.Statup("Inbt", 60, 3)
                    ch_l "This one looks. . . ok."   
                    call Date_Bonus(LauraX,10)
    elif Line == "action":
            if RogueX in Party and Trigger != RogueX:
                    $ RogueX.FaceChange("sexy")
                    ch_r "Hmm, you know I'm always up for some action." 
                    $ RogueX.Statup("Love", 95, 3)
                    call Date_Bonus(RogueX,5)
            if KittyX in Party and Trigger != KittyX:
                    $ KittyX.FaceChange("sexy")
                    $ KittyX.Statup("Love", 95, 4)
                    $ KittyX.Statup("Inbt", 50, 2)
                    ch_k "Action movies are kind of fun." 
                    call Date_Bonus(KittyX,5)
            if EmmaX in Party and Trigger != EmmaX:
                    $ EmmaX.FaceChange("sadside", Brows="angry")
                    $ EmmaX.Statup("Love", 70, -2)
                    $ EmmaX.Statup("Obed", 50, 5)
                    ch_e "I suppose it will at least keep me occupied."          
                    # call Date_Bonus(EmmaX,0)
            if LauraX in Party and Trigger != LauraX:
                    $ LauraX.FaceChange("sadside", Brows="angry")
                    $ LauraX.Statup("Love", 70, 5)
                    $ LauraX.Statup("Obed", 50, 5)
                    ch_l "This one sounds exciting!"          
                    call Date_Bonus(LauraX,10)
    elif Line == "horror":
            if RogueX in Party and Trigger != RogueX:
                    $ RogueX.FaceChange("sad", Eyes="surprised")
                    $ RogueX.Statup("Love", 90, -3)
                    $ RogueX.Statup("Obed", 50, 3)
                    $ RogueX.Statup("Obed", 80, 2)
                    ch_r "I'm not really into the spooky stuff, [RogueX.Petname]."   
                    # call Date_Bonus(RogueX,0)
            if KittyX in Party and Trigger != KittyX:
                    $ KittyX.FaceChange("sad", Eyes="surprised")      
                    $ KittyX.Statup("Love", 90, -5)
                    $ KittyX.Statup("Obed", 50, 4)
                    $ KittyX.Statup("Obed", 80, 2)
                    ch_k "It won't be {i}too{/i} scary, right?"          
                    call Date_Bonus(KittyX,-5)
            if EmmaX in Party and Trigger != EmmaX:
                    $ EmmaX.FaceChange("sly")
                    $ EmmaX.Statup("Love", 70, 3)
                    $ EmmaX.Statup("Obed", 50, 3)
                    $ EmmaX.Statup("Inbt", 70, 2)
                    $ EmmaX.Statup("Lust", 60, 5)
                    ch_e "I do love to get a good chill up the spine."          
                    call Date_Bonus(EmmaX,15)
            if LauraX in Party and Trigger != LauraX:
                    $ LauraX.FaceChange("normal")
                    $ LauraX.Statup("Obed", 50, 3)
                    ch_l "I'm sure it'll be terrifying."          
#                    call Date_Bonus(LauraX,0)
    elif Line == "drama":
            if RogueX in Party and Trigger != RogueX:
                    $ RogueX.FaceChange("bemused")
                    $ RogueX.Statup("Love", 95, 1)
                    $ RogueX.Statup("Obed", 50, 3)
                    ch_r "Hmmm, I have heard some good things about this one, could be interesting."   
                    call Date_Bonus(RogueX,5)
            if KittyX in Party and Trigger != KittyX:
                    $ KittyX.FaceChange("bemused")
                    $ KittyX.Statup("Love", 95, 3)
                    $ KittyX.Statup("Obed", 50, 2)
                    ch_k "I heard this was a good one!"   
                    call Date_Bonus(KittyX,15)
            if EmmaX in Party and Trigger != EmmaX:
                    $ EmmaX.FaceChange("normal")
                    $ EmmaX.Statup("Love", 70, 2)
                    $ EmmaX.Statup("Obed", 50, 3)
                    ch_e "Ah, this does sound like an interesting one."          
                    call Date_Bonus(EmmaX,5)    
            if LauraX in Party and Trigger != LauraX:
                    $ LauraX.FaceChange("normal")
                    $ LauraX.Statup("Obed", 50, 3)
                    ch_l "Meh."          
#                    call Date_Bonus(LauraX,0)   
    $ Trigger = 0
    
    call Date_Paying("movie")   
    
    if not Party:
            #if you're ditched,
            "You decide to watch the movie anyway, but it was pretty boring."
            "Afterwards you just head back to your room."
            jump Date_Over
    
    $ Player.RecentActions.append("movie") 
    #The movie plays.
    if len(Party) >= 2:
        "You take your seat in between the other two."
    else:
        "You take your seats in the theater."
        
    if "romcom" in Player.RecentActions:    
        $ Line = renpy.random.choice(["You watch the movie, which is about an adorkable girl who can't choose between two hunky guys. She picks the other one.", 
                    "You watch the movie, which is about a girl who is mercilessly stalked by some weird guy, until she eventually decides she loves him. They live hapily ever after.", 
                    "In this movie, the lead goes to all her friend's weddings, but can't get it together herself. She dies alone. Just kidding, she gets married at the end.", 
                    "You watch the movie, in which a bunch of college girls go on a wild adventure and have lots of random sex.",
                    "This movie is about a girl who's convinced to live in a sex dungeon, and really seems to enjoy it.",
                    "This movie is about a girl who works for a fashion house and is bullied by her boss, until they become friends."])        
    elif "action" in Player.RecentActions: 
        $ Line = renpy.random.choice(["You watch the movie, which is about an ex marine fighting aliens.", 
                    "You watch the movie, which is about a girl who is mercilessly stalked by some weird guy, until she eventually decides she loves him. They live hapily ever after. There are also a lot of explosions.", 
                    "In this movie, giant robots are fighting animal mash-ups, with the fate of the world in the balance.", 
                    "You watch the movie, in which a team of non-mutant superhumans are apparently fighting some sort of silvery robots in Eastern Europe.",
                    "This movie is about a superhuman powerhouse that nearly wrecks a town, and yet is not arrested for it by the humans. Must be the hammer.",
                    "This movie is about 90 minutes of constant explosions and lensflares."])
    elif "horror" in Player.RecentActions: 
        $ Line = renpy.random.choice(["You watch the movie, which is about an adorkable girl who can't choose between two hunky guys. She picks the other one. The guys are a fishman and a skeleton.", 
                    "You watch the movie, which is about a girl who is mercilessly stalked by some weird guy, until she eventually gives in and marries him. Her life is an endless hell.", 
                    "In this movie, a group of teens are trapped in a wilderness cabin. They have a lot of random sex as some shadowy monster kills them one by one.", 
                    "In this movie, a group of teens are trapped in an abandoned motel. They have a lot of random sex as some shadowy monster kills them one by one.", 
                    "This movie is about a girl who's convinced to live in a sex dungeon, and she's eventually murdered.",
                    "In this movie, a group of teens are trapped in a spaceship. They have a lot of random sex as some shadowy monster kills them one by one."])
    elif "drama" in Player.RecentActions: 
        $ Line = renpy.random.choice(["You watch the movie, which is about a mature woman who can't choose between two eligible widowers. She picks the other one.", 
                    "You watch the movie, which is a documentary about a girl who is mercilessly stalked by some weird guy, until she eventually decides she gets a restraining order.", 
                    "In this movie, which is a biopic about a great historical leader.", 
                    "You watch the movie, in which a disabled person struggles with his various disabilities, and eventually overcomes them, and/or dies.",
                    "This movie is about a lot of yelling and crying as some very serious issues are explored by an ensemble cast."])
   
    "[Line]" #You watch the movie. . .
    
    call Movie_Sex
                
    jump Date_End
        
#end Movie Sequence  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
        

# Start Movie Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Movie_Sex(Girl=0,Previous=0,GirlBonus=0, OptionsDS=[],BO=[]):
    # Called by Date_Sex    
    $ BO = Party[:]
    if 0 in BO:
        $ BO.remove(0)
    while BO:
            if ApprovalCheck(BO[0], 1000):  #Checks if BO[0] is in
                    $ OptionsDS.append(BO[0])   
                    if Party[0] == BO[0] and Date_Bonus[0] > 10:
                            $ OptionsDS.append(BO[0])
                    elif BO[0] in Party and Date_Bonus[1] > 10:
                            $ OptionsDS.append(BO[0])           
                    if "horror" in Player.RecentActions: 
                            $ OptionsDS.append(BO[0])                     
                    elif "drama" in Player.RecentActions:
                            $ OptionsDS.append(BO[0])                        
                    elif BO[0] == LauraX and "action" in Player.RecentActions:
                            $ OptionsDS.append(BO[0])              
            $ BO.remove(BO[0])
            
    if len(OptionsDS) == 0:
            #if nobody is in, return
            return
        
    $ renpy.random.shuffle(OptionsDS)
    
    $ Girl = OptionsDS[0]
    if len(Options) >= 2:
            $ Previous = OptionsDS[1]
    
    $ OptionsDS =["nothing"]
            
    if Party[0] == Girl:
        $ GirlBonus = Date_Bonus[0] + Date_Cost[0]
    else:
        $ GirlBonus = Date_Bonus[1] + Date_Cost[1]
                
    if ApprovalCheck(Girl, 500, Bonus=(10*GirlBonus)):
        $ Girl.FaceChange("kiss", 1)
        if "romcom" in Player.RecentActions: 
                "Halfway through the movie, inspired by the action on screen, [Girl.Name] turns to you and starts to make out with you."
        elif "action" in Player.RecentActions:        
                "Halfway through the movie, adrenaline pumping from the action on screen, [Girl.Name] turns to you and starts to make out with you."
        elif "horror" in Player.RecentActions:  
                if Girl == EmmaX:
                        "Halfway through the movie, slightly bored by it, [Girl.Name] shrugs and starts to make out with you."
                elif Girl == LauraX:
                        "Halfway through the movie, bored by the \"tension\" on screen, [Girl.Name] turns to you and starts to make out with you."
                else:  
                        "Halfway through the movie, freaked out by the tension on screen, [Girl.Name] huddles in your arms, and then starts to make out with you."   
        elif "drama" in Player.RecentActions:  
                if Girl in (RogueX,EmmaX):    
                        "Halfway through the movie, profoundly bored by the movie, [Girl.Name] turns to you with a shrug and starts to make out with you."     
                else: 
                        "Halfway through the movie, [Girl.Name] turns to you with a shrug and starts to make out with you."
        $ Girl.RecentActions.append("kissing") 
        $ Girl.RecentActions.append("moviesex")                       
        $ Girl.DailyActions.append("kissing")      
        call Date_Sex_Break(Girl,Previous)   
        if _return == 4:
                #the other girl stops you
                "You settle back into your seats and watch the rest of the film."
                return
        elif _return == 1:
                #the other girl joins in. . .
                "[Previous.Name] also leans in and begins kissing the both of you."
        elif _return == 3:
                #the other girl is mad. . .
                "You get back to it, [Previous.Name] settles back into her seat with a glare."
        
        if Girl.Anal and ApprovalCheck(Girl, 2000, Bonus=(10*GirlBonus)) and Girl.PantsNum() <= 5:
                $ OptionsDS.append("anal")        
        if Girl.Sex and ApprovalCheck(Girl, 2000, Bonus=(10*GirlBonus)) and Girl.PantsNum() <= 5:
                $ OptionsDS.append("sex")
        if Girl.Blow and ApprovalCheck(Girl, 1300, Bonus=(10*GirlBonus)):
                $ OptionsDS.append("blow")      
        if Girl.Hand and ApprovalCheck(Girl, 1000, Bonus=(10*Count2)):
                $ OptionsDS.append("hand")
        if Girl.FondleP and ApprovalCheck(Girl, 900, Bonus=(10*GirlBonus)):
                $ OptionsDS.append("pussy")
        elif ApprovalCheck(Girl, 1200, Bonus=(5*GirlBonus)) and Girl.Panties:
                $ OptionsDS.append("panties")
        elif ApprovalCheck(Girl, 1200, Bonus=(5*GirlBonus)):
                $ OptionsDS.append("flash")
                       
        $ renpy.random.shuffle(OptionsDS) 
    
    
        if OptionsDS[0] == "anal":
                    $ Girl.FaceChange("sexy", 1)
                    if Girl.Panties:
                        "As you make out, [Girl.Name] reaches down and undoes your fly. She pulls her panties aside and shifts into your lap."
                    else:
                        "As you make out, [Girl.Name] reaches down and undoes your fly. She hikes her skirt up a bit and shifts into your lap."
                    call Date_Sex_Break(Girl,Previous,1)
                    if _return == 3:
                            #the other girl stormed out. . .
                            if Girl == RogueX:        
                                    ch_r "Sorry about that."                    
                            elif Girl == KittyX:
                                    ch_k "Well that was awkward."    
                            elif Girl == EmmaX:
                                    ch_e "Hmm, that was uncomfortable."      
                            elif Girl == LauraX:
                                    ch_l "I wonder if she's coming back."          
                    "She gingerly squeezes your cock into her ass and begins to grind up and down, quietly enough that the other patrons don't seem to notice."
                    if _return == 1:
                            #the other girl joins you. . .
                            "[Previous.Name] also leans over and toys with [Girl.Name]'s pussy."
                            $ Girl.GLG(Previous,700,3,1)
                            $ Girl.GLG(Previous,1000,3,1)
                            $ Previous.GLG(Girl,1000,2,1)
                    if Girl.CreamA:
                            if Girl.Panties:
                                "After several minutes of this, you can't take it anymore and come inside her."
                                "She pulls her panties back up and returns to her seat."
                            else:
                                "After several minutes of this, you can't take it anymore and come inside her."
                                "She wipes off as best she can and shifts back into her seat."
                            $ Girl.CreamA += 1
                            $ Girl.RecentActions.append("creampie anal")                      
                            $ Girl.DailyActions.append("creampie anal") 
                    else:
                            "After several minutes of this, she pulls out and shifts back into her seat, finishing you off with her hand."
                            if Girl.Swallow:
                                if 0 < _return < 3: #if 1 or 2
                                    "You cum into the popcorn bucket, which she and [Previous.Name] then finish off together."
                                else:
                                    "You cum into the popcorn bucket, which she then finishes off."
                                $ Girl.Addict -= 20
                                $ Girl.Swallow += 1
                                $ Girl.Spunk.append("mouth")                          
                                $ Girl.RecentActions.append("swallowed")                      
                                $ Girl.DailyActions.append("swallowed") 
                            else:
                                if Girl == KittyX:
                                    "You cum into the popcorn bucket, which she phases into the floor."
                                else:
                                    "You cum into the popcorn bucket, which she sets in the seat next to her."
                    if Girl == RogueX:   
                            ch_r "This makes for a better ride than a movie."      
                    elif Girl == KittyX:
                            ch_k "Talk about a \"4D\" movie."
                    elif Girl == EmmaX:
                            ch_e "Well, that was exciting."
                    elif Girl == LauraX:
                            ch_l "Hmm, I'm stuffed."
                    $ Girl.Statup("Inbt", 50, 4)
                    $ Girl.Statup("Inbt", 90, 3)
                    $ Girl.SeenPeen += 1
                    $ Girl.Anal += 1
                    $ Player.Semen -= 1
                    $ Girl.RecentActions.append("anal")                      
                    $ Girl.DailyActions.append("anal")  
        elif OptionsDS[0] == "sex":
                    $ Girl.FaceChange("sexy", 1)
                    if Girl.Panties:
                        "As you make out, [Girl.Name] reaches down and undoes your fly. She pulls her panties aside and shifts into your lap."
                    else:
                        "As you make out, [Girl.Name] reaches down and undoes your fly. She hikes her skirt up a bit and shifts into your lap."
                    call Date_Sex_Break(Girl,Previous,1)                    
                    if _return == 3:
                            #the other girl stormed out. . .
                            if Girl == RogueX:        
                                    ch_r "Sorry about that."                    
                            elif Girl == KittyX:
                                    ch_k "Well that was awkward."    
                            elif Girl == EmmaX:
                                    ch_e "Hmm, that was uncomfortable."      
                            elif Girl == LauraX:
                                    ch_l "I wonder if she's coming back."         
                    "Seconds later, she's slowly rocking on your cock, quietly enough that the other patrons don't seem to notice."
                    if _return == 1:
                            #the other girl joins you. . .
                            "[Previous.Name] also leans over and toys with [Girl.Name]'s pussy."
                            $ Girl.GLG(Previous,700,3,1)
                            $ Girl.GLG(Previous,1000,3,1)
                            $ Previous.GLG(Girl,1000,2,1)
                    if Girl.CreamP:
                        if Girl.Panties:
                            "After several minutes of this, you can't take it anymore and come inside her."
                            "She pulls her panties up over her dripping slit and returns to her seat."
                        else:
                            "After several minutes of this, you can't take it anymore and come inside her."
                            "She wipes up as best she can and returns to her seat."
                        $ Girl.CreamP += 1
                        $ Girl.RecentActions.append("creampie sex")                      
                        $ Girl.DailyActions.append("creampie sex") 
                    else:
                        "After several minutes of this, she pulls out and shifts back into her seat, finishing you off with her hand."
                        if Girl.Swallow:
                                if 0 < _return < 3: #if 1 or 2
                                    "You cum into the popcorn bucket, which she and [Previous.Name] then finish off together."
                                else:                                    
                                    "You cum into the popcorn bucket, which she then finishes off."   
                                $ Girl.Spunk.append("mouth")   
                                $ Girl.Addict -= 20
                                $ Girl.Swallow += 1
                                $ Girl.RecentActions.append("swallowed")                      
                                $ Girl.DailyActions.append("swallowed") 
                        else:
                            if Girl == KittyX:
                                "You cum into the popcorn bucket, which she phases into the floor."
                            else:
                                "You cum into the popcorn bucket, which she sets in the seat next to her."
                    if Girl == RogueX:   
                            ch_r "This makes for a better ride than a movie."      
                    elif Girl == KittyX:
                            ch_k "Talk about a \"4D\" movie."
                    elif Girl == EmmaX:
                            ch_e "Well, that was exciting."
                    elif Girl == LauraX:
                            ch_l "Hmm, I'm stuffed."
                    $ Girl.Statup("Inbt", 50, 4)
                    $ Girl.Statup("Inbt", 90, 3)
                    $ Girl.SeenPeen += 1
                    $ Girl.Sex += 1
                    $ Player.Semen -= 1
                    $ Girl.RecentActions.append("sex")                      
                    $ Girl.DailyActions.append("sex")             
        elif OptionsDS[0] == "blow":
                    $ Girl.FaceChange("sucking", 1)
                    "As you make out, [Girl.Name] reaches down and undoes your fly. She then bends down and wraps her lips around it."
                    call Date_Sex_Break(Girl,Previous,1)                
                    if _return == 3:
                            #the other girl stormed out. . .
                            if Girl == RogueX:        
                                    ch_r "Sorry about that."                    
                            elif Girl == KittyX:
                                    ch_k "Well that was awkward."    
                            elif Girl == EmmaX:
                                    ch_e "Hmm, that was uncomfortable."      
                            elif Girl == LauraX:
                                    ch_l "I wonder if she's coming back."              
                    if _return == 1:
                            #the other girl joins you. . .
                            "[Previous.Name] also leans over joins [Girl.Name] at licking your cock."
                            "They take turns sucking on it contentedly for several minutes before you finally cum."   
                            $ Girl.GLG(Previous,1000,2,1)
                            $ Previous.GLG(Girl,1000,2,1)
                    else:
                            "She sucks on it contentedly for several minutes before you finally cum."            
                    $ Girl.Spunk.append("mouth")  
                    if Girl.Swallow:
                            "[Girl.Name] wipes her mouth as she shifts back into her seat and washes it down with some soda."
                            $ Girl.FaceChange("sexy")
                            if Girl == RogueX:     
                                    ch_r "Mmmm, refreshing. . ."    
                            elif Girl == KittyX:
                                    ch_k "Mmmm, that hit the spot. . ."
                            elif Girl == EmmaX:
                                    ch_e "Mmmm, refreshing. . ."
                            elif Girl == LauraX:
                                    ch_l "Mmmm, that hit the spot. . ."
                            $ Girl.Addict -= 20
                            $ Girl.Swallow += 1
                            $ Girl.RecentActions.append("swallowed")                      
                            $ Girl.DailyActions.append("swallowed") 
                    else:
                        if Girl == KittyX:
                            "You cum into the popcorn bucket, which she phases into the floor."
                        else:
                            "You cum into the popcorn bucket, which she sets in the seat next to her."
                        if Girl == RogueX:         
                                ch_r "I bet the cleaning crew will enjoy that."
                        elif Girl == KittyX:
                                ch_k "That should give archeolgists a surprise."
                        elif Girl == EmmaX:
                                ch_e "That is a bit of a mess for the help."
                        elif Girl == LauraX:
                                ch_l "Kinda left a mess there."
                    $ Girl.Statup("Inbt", 40, 3)
                    $ Girl.Statup("Inbt", 80, 2)
                    $ Girl.SeenPeen += 1
                    $ Girl.Blow += 1
                    $ Player.Semen -= 1
                    $ Girl.RecentActions.append("blow")                      
                    $ Girl.DailyActions.append("blow") 
        elif OptionsDS[0] == "hand":
                    $ Girl.FaceChange("sexy")
                    "As you make out, [Girl.Name] reaches down and pulls out your cock." 
                    call Date_Sex_Break(Girl,Previous,1)             
                    if _return == 3:
                            #the other girl stormed out. . .
                            if Girl == RogueX:        
                                    ch_r "Sorry about that."                    
                            elif Girl == KittyX:
                                    ch_k "Well that was awkward."    
                            elif Girl == EmmaX:
                                    ch_e "Hmm, that was uncomfortable."      
                            elif Girl == LauraX:
                                    ch_l "I wonder if she's coming back."    
                            "She then leans over and begins to stroke your cock." 
                    elif _return == 1: 
                            #the other girl joins in. . .
                            "She then leans over and begins to stroke your cock."
                            "[Previous.Name] leans in and joins her, and they share a smile."
                            $ Girl.GLG(Previous,1000,2,1)
                            $ Previous.GLG(Girl,1000,2,1)
                    else:
                            "She then leans over and begins to stroke it." 
                    $ Girl.FaceChange("surprised")
                    if Girl.FondleP:
                        if _return == 1: 
                                #the other girl joins in. . .
                                "You also reach down and begin stroking their pussies."
                        else:
                            if Girl.Legs:
                                    "You also lean over, reach into her [Girl.Legs], and begin to stroke her pussy."
                            elif Girl.Hose:
                                    "You also lean in, reach under her [Girl.Hose], and begin to stroke her pussy."
                            elif Girl.Panties:
                                    "You also lean in, reach under her panties, and begin to stroke her pussy."
                            else:
                                    "You also lean over, notice she isn't wearing anything down there, and begin to stroke her pussy."
                    $ Girl.FaceChange("sexy", 1, Eyes = "closed")
                    if Girl.FondleP:
                            if _return == 1: 
                                "After several minutes of this, [Girl.Name] and [Previous.Name] shudder in orgasm, which sets you off as well."
                            else:
                                "After several minutes of this, she shudders in orgasm, which sets you off as well."
                            "[Girl.Name] catches the jiz in the popcorn bucket."
                    $ Girl.Eyes = "sexy"
                    if Girl.Swallow:
                            if 0 < _return < 3: #if 1 or 2
                                "The girls finish off the remaining popcorn with a grin."    
                            else:
                                "She finishes off the remaining popcorn with a grin."                    
                            $ Girl.Spunk.append("mouth")  
                            if Girl == RogueX:   
                                    ch_r "Best topping they got here, [Girl.Petname]."         
                            elif Girl == KittyX:
                                    ch_k "Best topping they got here, [Girl.Petname]."    
                            elif Girl == EmmaX:
                                    ch_e "I do enjoy this new flavor they have, [Girl.Petname]."   
                            elif Girl == LauraX:  
                                    ch_l "I should order that topping next time."  
                            $ Girl.Addict -= 20
                            $ Girl.Swallow += 1
                            $ Girl.RecentActions.append("swallowed")                      
                            $ Girl.DailyActions.append("swallowed") 
                    else:
                            if Girl == KittyX:
                                "You cum into the popcorn bucket, which she phases into the floor."
                            else:
                                "You cum into the popcorn bucket, which she sets in the seat next to her."
                            if Girl == RogueX:         
                                    ch_r "I bet the cleaning crew will enjoy that."
                            elif Girl == KittyX:
                                    ch_k "That should give archeolgists a surprise."
                            elif Girl == EmmaX:
                                    ch_e "That is a bit of a mess for the help."
                            elif Girl == LauraX:
                                    ch_l "Kinda left a mess there."
                    $ Girl.Statup("Love", 90, 2)
                    $ Girl.Statup("Inbt", 40, 3)
                    $ Girl.Statup("Inbt", 80, 2)
                    $ Girl.FondleP += 1
                    $ Girl.Org += 1        
                    $ Girl.Hand += 1
                    $ Player.Semen -= 1
                    $ Girl.RecentActions.append("hand")                      
                    $ Girl.DailyActions.append("hand") 
        elif OptionsDS[0] == "pussy":
                    $ Girl.FaceChange("sexy")                    
                    if Girl.Legs:
                            "As you make out, [Girl.Name] grabs your hand and shoves it down her [Girl.Legs]."
                    elif Girl.Hose:
                            "As you make out, [Girl.Name] grabs your hand and shoves it down her [Girl.Hose]."
                    elif Girl.Panties:
                            "As you make out, [Girl.Name] grabs your hand and shoves it down her panties."
                    else:
                            "As you make out, [Girl.Name] grabs your hand and shoves it between her legs."
                    call Date_Sex_Break(Girl,Previous,1)
                    $ Girl.Eyes = "closed"
                    if _return == 3:
                            #the other girl stormed out. . .
                            if Girl == RogueX:        
                                    ch_r "Sorry about that."                    
                            elif Girl == KittyX:
                                    ch_k "Well that was awkward."    
                            elif Girl == EmmaX:
                                    ch_e "Hmm, that was uncomfortable."      
                            elif Girl == LauraX:
                                    ch_l "I wonder if she's coming back."            
                            "You get back to work."
                    elif _return == 1: 
                            #the other girl joins in. . .
                            "[Previous.Name] leans in and begins to fondle her breasts as well."   
                            $ Girl.GLG(Previous,700,6,1)
                            $ Girl.GLG(Previous,1000,3,1)
                            $ Previous.GLG(Girl,1000,2,1)
                    "After several minutes of this, she shudders in orgasm and leans back with a contented sigh."
                    $ Girl.Eyes = "sexy"
                    if Girl == RogueX:   
                            ch_r "Thanks [Girl.Petname]. I needed that. . . distraction."      
                    elif Girl == KittyX:
                            ch_k "Hmm, that felt great, [Girl.Petname]."
                    elif Girl == EmmaX:
                            ch_e "Very. . . kind of you, [Girl.Petname]. I needed that."
                    elif Girl == LauraX:
                            ch_l "Hmm, that was great, [Girl.Petname]."
                    $ Girl.Statup("Love", 90, 2)
                    $ Girl.Statup("Inbt", 40, 2)
                    $ Girl.Statup("Inbt", 80, 2)
                    $ Girl.FondleP += 1
                    $ Girl.Org += 1    
                    $ Girl.RecentActions.append("fondle pussy")                      
                    $ Girl.DailyActions.append("fondle pussy") 
        elif OptionsDS[0] == "panties":
                    $ Girl.FaceChange("sexy")
                    "After making out for a few minutes, [Girl.Name] gets a sly look on her face and reaches into her pocket."
                    "After a second, she hands you a cloth lump, apparently her panties." 
                    $ Girl.DailyActions.append("pantyless") 
                    $ Girl.Statup("Inbt", 60, 2)
                    $ Girl.Panties = 0
                    if Girl == RogueX:    
                            ch_r "Just a little downpayment on later, [Girl.Petname]."     
                    elif Girl == KittyX:
                            ch_k "[Girl.Like]hold on to those for me, uh?"
                    elif Girl == EmmaX:
                            ch_e "Just a hint at later, [Girl.Petname]."
                    elif Girl == LauraX:
                            ch_l "Could you hold onto those for later?"
        elif OptionsDS[0] == "flash":
                    $ Girl.FaceChange("sexy")
                    "After making out for a few minutes, [Girl.Name] gets a sly look on her face, then shifts a bit lower in her seat."
                    if Girl.PantsNum() > 6:
                        "Looking down, you notice she's pulled down her pants enough that you can see her bare pussy, lit by the movie screen."  
                    elif Girl.PantsNum() == 6:
                        "Looking down, you notice she's pulled down her shorts enough that you can see her bare pussy, lit by the movie screen."   
                    else:
                        "Looking down, you notice she's hiked up her skirt enough that you can see her bare pussy, lit by the movie screen."            
                    $ Girl.Statup("Inbt", 60, 2)
                    call expression Girl.Tag + "_First_Bottomless" pass (1)
                    if Girl == RogueX:         
                            ch_r "Just a little downpayment on later, [Girl.Petname]."
                    elif Girl == KittyX:
                            ch_k "Just giving you a little taste. . ."
                    elif Girl == EmmaX:
                            ch_e "Just a hint at later, [Girl.Petname]."
                    elif Girl == LauraX:
                            ch_l "Just a heads up. . ."
    #End Rogue movie sex options
    $ Girl.OutfitChange(Changed=0)
    return
# End Movie Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  

#Start Date_Sex_Break   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Date_Sex_Break(Girl=0,Previous=0,Repeat=0):
        #Girl is the lead girl
        #Previous is the other girl
        # if it returns 0, it continues normally.
        # if it returns 1, the other girl joins in
        # if it returns 2, the other girl watches
        # if it returns 3, the other girl is mad, but it goes on
        # if it returns 4, the other girl is mad, so you cancel out
        # if Repeat, it's the second scene like this of the night. 
                
        if not Previous:
                if len(Party) >= 2:
                    if Girl == Party[0]:
                            $ Previous = Party[1]
                    else:
                            $ Previous = Party[0]
        if Previous not in TotalGirls:
                return 0
            
        if Girl.GirlLikeCheck(Previous) >= 700 and Previous.GirlLikeCheck(Girl) >= 700:
                #They like each other and will share
                $ Previous.RecentActions.append("noticed " + Girl.Tag)
                return 1
        elif ApprovalCheck(Previous, 1400) and Previous.GirlLikeCheck(Girl) >= 500:
                #girl2 likes you, and likes girl1 enough to be chill
                $ Previous.FaceChange("sly")
                "[Previous.Name] winks at you, but doesn't move to get involved."
                $ Previous.RecentActions.append("noticed " + Girl.Tag)
                $ Girl.GLG(Previous,600,5,1)
                $ Girl.GLG(Previous,900,3,1)
                $ Previous.GLG(Girl,900,2,1)
                return 2
        elif ApprovalCheck(Previous, 1400) and Previous.GirlLikeCheck(Girl) < 500:
                pass
        
        
        #If they asked you to stop
        
        #She likes you, but hates the girl
        if Repeat == 2:
                #if it's a good night kiss
                $ Previous.FaceChange("angry",Eyes="side")
                $ Previous.Statup("Love", 80, -5)
                $ Previous.Statup("Obed", 80, 5)
                $ Previous.GLG(Girl,800,-3,1)
                return 3                       
        elif Repeat:
                $ Previous.FaceChange("angry")
                $ Previous.Statup("Love", 80, -15)
                $ Previous.Statup("Obed", 80, 15)
                if Previous == RogueX:
                        ch_r "Get a room you two!"
                elif Previous == KittyX:
                        ch_k "Geeze, right in front of me?!"
                elif Previous == EmmaX:
                        ch_e "Oh do grow up, you two!"
                elif Previous == LauraX:
                        ch_l "Seriously, get a room!"
                $ Previous.GLG(Girl,800,-3,1)
                call Girl_Date_Over(Previous)
                # You do it anyway
                return 3     
        if Previous == RogueX:
                ch_r "I know what she's up to, cut it out." 
        elif Previous == KittyX:
                ch_k "I see you there, cut it out."
        elif Previous == EmmaX:
                ch_e "Oh, I see what's going on, stop it."
        elif Previous == LauraX: 
                ch_l "You think I wouldn't notice? Cut it out."   
        $ Previous.GLG(Girl,800,-1,1)  
        $ Girl.GLG(Previous,800,-3,1)           
        menu:
            extend ""
            "Ok, I'll stop.":
                $ Previous.Statup("Love", 80, 10)
                $ Previous.Statup("Obed", 80, -5)
                $ Previous.Statup("Inbt", 60, 5)
                $ Girl.GLG(Previous,800,-3,1)
                if "study" not in Player.RecentActions:
                        call Date_Bonus(Previous,5)
                # You stop
                return 4 
            "I don't think so.":
                $ Previous.FaceChange("angry")
                $ Previous.Statup("Love", 80, -10)
                $ Previous.Statup("Obed", 80, 10)
                $ Previous.Statup("Inbt", 60, -5)
                $ Previous.GLG(Girl,800,-3,1)
                if "study" in Player.RecentActions:
                        call Girl_Date_Over(Previous)
                else:
                        call Date_Bonus(Previous,-5) 
                # You do it anyway
                return 3 
        return 0 #Yes
    
#end Date_Sex_Break   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
        
#Start Payment system   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /         
label Date_Paying(Activity="dinner", Total_Cost=0):  
    # Activity is which thing you're doing, total cost is the combined meal costs. 
    if Activity == "dinner":
                $ Total_Cost = Play_Cost + Date_Cost[0] + Date_Cost[1]
                "The Waitress brings you the check, it comes to $[Total_Cost]."
    else:
        if len(Party) >= 2:
                $ Total_Cost = 30
                "You go to the ticket window, three tickets would be $30."
        else:
                $ Total_Cost = 20
                "You go to the ticket window, two tickets would be $20."
                
    menu:
        "Who's paying?"
        "I've got it." if Player.Cash >= Total_Cost:
            $ Line = "you"         
                        
        "[RogueX.Name], you pay." if RogueX in Party:    
            $ Line = RogueX                 
        "[KittyX.Name], you pay." if KittyX in Party:    
            $ Line = KittyX  
        "[EmmaX.Name], you pay." if EmmaX in Party:    
            $ Line = EmmaX     
        "[LauraX.Name], you pay." if LauraX in Party:    
            $ Line = LauraX                                        
                
        "Let's split it." if Player.Cash >= Play_Cost:   
            $ Line = "split"                             
                        
        "I really can't afford it. . ." if Player.Cash < Total_Cost: 
            $ Line = "deadbeat"    
    
    if Line == "you":
            #If you offer to cover the meal
            if RogueX in Party:
                    if "deadbeat" in RogueX.History:  
                        $ RogueX.History.remove("deadbeat") 
                    $ RogueX.FaceChange("sexy", 1)
                    ch_r "Oh, and such a gentleman."
                    $ RogueX.Statup("Love", 50, 2)
                    $ RogueX.Statup("Love", 80, 2) 
                    if Total_Cost >= 15: 
                        $ RogueX.Statup("Love", 200, 2)
                    call Date_Bonus(RogueX,Total_Cost)
                    
            if KittyX in Party:
                    if "deadbeat" in KittyX.History:  
                        $ KittyX.History.remove("deadbeat") 
                    $ KittyX.FaceChange("sexy", 1)
                    ch_k "[KittyX.Like]that's really nice of you."
                    $ KittyX.Statup("Love", 50, 2)
                    $ KittyX.Statup("Love", 80, 2) 
                    if Total_Cost >= 15: 
                        $ KittyX.Statup("Love", 200, 2)
                    call Date_Bonus(KittyX,Total_Cost)
                    
            if EmmaX in Party:
                    if "deadbeat" in EmmaX.History:  
                        $ EmmaX.History.remove("deadbeat") 
                    $ EmmaX.FaceChange("sly", 1)
                    ch_e "Oh, how very mature of you."
                    $ EmmaX.Statup("Obed", 50, 3)
                    $ EmmaX.Statup("Love", 50, 2) 
                    $ EmmaX.Statup("Love", 80, 2) 
                    if Total_Cost >= 15: 
                        $ EmmaX.Statup("Love", 200, 2)
                    call Date_Bonus(EmmaX,Total_Cost)
                    
            if LauraX in Party:
                    if "deadbeat" in LauraX.History:  
                        $ LauraX.History.remove("deadbeat") 
                    $ LauraX.FaceChange("sly", 1)
                    ch_l "Oh, that's nice of you."
                    $ LauraX.Statup("Obed", 50, 4)
                    $ LauraX.Statup("Love", 50, 2) 
                    $ LauraX.Statup("Love", 80, 1) 
                    if Total_Cost >= 15: 
                        $ LauraX.Statup("Love", 90, 2)
                        $ LauraX.Statup("Obed", 50, 1)
                    call Date_Bonus(LauraX,Total_Cost)
            $ Player.Cash -= Total_Cost                    
                   
    elif Line == RogueX:  
            #If you ask Rogue to pay
            $ RogueX.Statup("Love", 90, -7)
            if Total_Cost >= 15:
                    $ RogueX.Statup("Love", 200, -6)
                    if Party[0] == RogueX and Play_Cost > Date_Cost[0]:
                        $ RogueX.Statup("Love", 200, -10)
                        $ RogueX.Statup("Obed", 80, 4)
                    elif RogueX in Party and Play_Cost > Date_Cost[1]:
                        $ RogueX.Statup("Love", 200, -10)
                        $ RogueX.Statup("Obed", 80, 4)
            if ApprovalCheck(RogueX, 1100) and len(Party) < 2:
                    $ RogueX.FaceChange("sad")
                    ch_r "Well, ok, I guess I can cover it this time."
                    $ RogueX.Statup("Obed", 30, 3)
                    $ RogueX.Statup("Obed", 80, 2)   
                    if bg_current != "bg movies" and "dinnersex" in RogueX.RecentActions:
                            call Date_Bonus(RogueX, -Total_Cost)
            elif ApprovalCheck(RogueX, 1300) and len(Party) >= 2:
                    $ RogueX.FaceChange("sad")
                    ch_r "Hm, ok, I guess I can cover it this time."
                    $ RogueX.Statup("Love", 80, -5)
                    $ RogueX.Statup("Obed", 30, 4)
                    $ RogueX.Statup("Obed", 80, 3)    
                    if bg_current != "bg movies" and "dinnersex" in RogueX.RecentActions:
                            call Date_Bonus(RogueX, -Total_Cost)
            else:                    
                    $ RogueX.FaceChange("angry")
                    if len(Party) >= 2:
                        $ RogueX.Statup("Love", 80, -5)
                        ch_r "Oh, bullshit, I am NOT payin for her."
                    else:
                        ch_r "No way, you're coverin your own bills, [RogueX.Petname]." 
                    if Player.Cash >= Play_Cost: 
                        $ Line = "split"
                    else:
                        $ Line = "deadbeat" 
            #end asked Rogue to pay
                        
    elif Line == KittyX:  
            #If you ask Kitty to pay
            $ KittyX.Statup("Love", 90, -7)
            if Total_Cost >= 15:
                    $ KittyX.Statup("Love", 200, -6)
                    if Party[0] == KittyX and Play_Cost > Date_Cost[0]:
                        $ KittyX.Statup("Love", 200, -10)
                        $ KittyX.Statup("Obed", 80, 4)
                    elif KittyX in Party and Play_Cost > Date_Cost[1]:
                        $ KittyX.Statup("Love", 200, -10)
                        $ KittyX.Statup("Obed", 80, 4)
            if ApprovalCheck(KittyX, 1000) and not len(Party) < 2:
                    $ KittyX.FaceChange("sad")
                    ch_k "Huh? I mean I guess I can. . ."
                    $ KittyX.Statup("Obed", 30, 3)
                    $ KittyX.Statup("Obed", 80, 2)  
                    if bg_current != "bg movies" and "dinnersex" in KittyX.RecentActions:
                            call Date_Bonus(KittyX, -Total_Cost)
            elif ApprovalCheck(KittyX, 1300) and len(Party) >= 2:
                    $ KittyX.FaceChange("sad")
                    ch_k "Huh? I mean I guess I can. . ."
                    $ KittyX.Statup("Love", 80, -5)
                    $ KittyX.Statup("Obed", 30, 4)
                    $ KittyX.Statup("Obed", 80, 3)  
                    if bg_current != "bg movies" and "dinnersex" in KittyX.RecentActions:
                            call Date_Bonus(KittyX, -Total_Cost)
            else:                    
                    $ KittyX.FaceChange("angry")
                    if len(Party) >= 2:
                        $ KittyX.Statup("Love", 80, -5)
                        ch_k "You have GOT to be kidding! I'm not paying for her too!"
                    else:
                        ch_k "As if! You're paying for yourself, [KittyX.Petname]." 
                    if Player.Cash >= Play_Cost: 
                        $ Line = "split"
                    else:
                        $ Line = "deadbeat" 
            #end asked Kitty to pay                   
    
    elif Line == EmmaX:  
            #If you ask Emma to pay
            $ EmmaX.Statup("Love", 90, -3)
            if Total_Cost >= 15:
                    $ EmmaX.Statup("Love", 200, -6)
                    if Party[0] == EmmaX and Play_Cost > Date_Cost[0]:
                        $ EmmaX.Statup("Love", 200, -5)
                        $ EmmaX.Statup("Obed", 80, 4)
                    elif EmmaX in Party and Play_Cost > Date_Cost[1]:
                        $ EmmaX.Statup("Love", 200, -5)
                        $ EmmaX.Statup("Obed", 80, 4)
            if ApprovalCheck(EmmaX, 900) and len(Party) < 2:
                    $ EmmaX.FaceChange("sad")
                    ch_e "I suppose you a student, after all. . ."
                    $ EmmaX.Statup("Obed", 30, 3)
                    $ EmmaX.Statup("Obed", 80, 2)     
                    if bg_current != "bg movies" and "dinnersex" in EmmaX.RecentActions:
                            call Date_Bonus(EmmaX, -Play_Cost)         
            elif ApprovalCheck(EmmaX, 1100) and len(Party) >= 2:
                    $ EmmaX.FaceChange("sad")
                    ch_e "I suppose you are students, after all. . ."
                    $ EmmaX.Statup("Love", 80, -5)
                    $ EmmaX.Statup("Obed", 30, 4)
                    $ EmmaX.Statup("Obed", 80, 3)    
                    if bg_current != "bg movies" and "dinnersex" in EmmaX.RecentActions:
                            call Date_Bonus(EmmaX, -Play_Cost)           
            else:                    
                    $ EmmaX.FaceChange("angry")
                    if len(Party) >= 2:
                        $ EmmaX.Statup("Love", 80, -5)
                        ch_e "I'm certainly not paying {i}her{/i} tab."
                    else:
                        ch_e "Student or not, I'm not paying your bills, [EmmaX.Petname]." 
                    if Player.Cash >= Play_Cost: 
                        $ Line = "split"
                    else:
                        $ Line = "deadbeat"   
            #end asked Emma to pay         
    
    
    elif Line == LauraX:  
            #If you ask Laura to pay
            $ LauraX.Statup("Love", 90, -2)
            if Total_Cost >= 15:
                    $ LauraX.Statup("Love", 200, -6)
                    if Party[0] == LauraX and Play_Cost > Date_Cost[0]:
                        $ LauraX.Statup("Love", 200, -5)
                        $ LauraX.Statup("Obed", 80, 4)
                    elif LauraX in Party and Play_Cost > Date_Cost[1]:
                        $ LauraX.Statup("Love", 200, -5)
                        $ LauraX.Statup("Obed", 80, 4)
            if ApprovalCheck(LauraX, 900) and len(Party) < 2:
                    $ LauraX.FaceChange("sad")
                    ch_l "Down on your luck? . ."
                    $ LauraX.Statup("Obed", 30, 3)
                    $ LauraX.Statup("Obed", 80, 2)     
                    if bg_current != "bg movies" and "dinnersex" in LauraX.RecentActions:
                            call Date_Bonus(LauraX, -Play_Cost)         
            elif ApprovalCheck(LauraX, 1100) and len(Party) >= 2:
                    $ LauraX.FaceChange("sad")
                    ch_l "Down on your luck? . ."
                    $ LauraX.Statup("Love", 80, -5)
                    $ LauraX.Statup("Obed", 30, 4)
                    $ LauraX.Statup("Obed", 80, 3)    
                    if bg_current != "bg movies" and "dinnersex" in LauraX.RecentActions:
                            call Date_Bonus(LauraX, -Play_Cost)           
            else:                    
                    $ LauraX.FaceChange("angry")
                    if len(Party) >= 2:
                        $ LauraX.Statup("Love", 80, -5)
                        ch_l "I'm not covering her though."
                    else:
                        ch_l "Too bad, I'm not covering you." 
                    if Player.Cash >= Play_Cost: 
                        $ Line = "split"
                    else:
                        $ Line = "deadbeat"   
            #end asked Laura to pay    
            
    if Line == "split": 
            #If you ask to split it evenly
            $ Count = len(Party)
            while Count > 0:
                    $ Count -= 1
                    if ApprovalCheck(Party[Count], 600):
                        $ Party[Count].FaceChange("sad",Mouth="normal")
                        $ Party[Count].Statup("Obed", 50, 2)
                        if Party[Count] == RogueX:
                                ch_r "Fine, I guess that's fair."
                        elif Party[Count] == KittyX:
                                ch_k "Yeah[KittyX.like]ok."
                        elif Party[Count] == EmmaX:
                                ch_e "I suppose you are still on a student's budget."
                        elif Party[Count] == LauraX:
                                $ LauraX.FaceChange("sad",Eyes="side")
                                $ LauraX.Statup("Love", 70, 2)
                                $ LauraX.Statup("Obed", 50, 3)
                                ch_l "Kinda cheap."
                    else:
                        if Date_Cost[Count] >=15:    
                                # if it cost more than 15, they like you less.
                                $ Party[Count].Statup("Love", 200, -5,Alt=[[LauraX],200,3])
                        else:
                                $ Party[Count].Statup("Love", 200, -3,Alt=[[LauraX],200,0])  
                        if Party[Count] == RogueX:
                                $ RogueX.FaceChange("angry",Eyes="side")
                                ch_r "Tch. Cheapskate."   
                        elif Party[Count] == KittyX:
                                $ KittyX.FaceChange("angry",Eyes="side")
                                ch_k "Jerk."       
                        elif Party[Count] == EmmaX:
                                $ EmmaX.FaceChange("sad",Eyes="side")
                                ch_e "You should learn not to ask a woman out if you can't afford it." 
                        elif Party[Count] == LauraX:
                                $ Party[Count].Statup("Love", 70, 2)
                                ch_l "Sure."
                    $ Date_Bonus[Count] -= 10 if Date_Cost[Count] >= 15 else 0
            $ Player.Cash -= Play_Cost
            
    if Line == "deadbeat":  
            #If you cannot pay.
            $ Date_Bonus[0] -= Play_Cost
            $ Date_Bonus[1] -= Play_Cost
            $ Date_Bonus[0] -= (Date_Cost[0] - 10) if Date_Cost[0] > 10 else 0
            $ Date_Bonus[1] -= (Date_Cost[1] - 10) if Date_Cost[1] > 10 else 0
            $ Count = len(Party)
            while Count:
                    $ Count -1
                    if Total_Cost >=15:          
                            $ Party[Count].Statup("Love", 200, -4)
                            if Play_Cost > Date_Cost[Count]:
                                    $ Party[Count].Statup("Love", 200, -10,Alt=[[EmmaX,LauraX],200,-5])
                                    $ Party[Count].Statup("Obed", 200, 0,Alt=[[EmmaX,LauraX],500,-2])
                    if bg_current != "bg movies" and "dinnersex" in Party[Count].RecentActions:
                                    call Date_Bonus(Party[Count], -Total_Cost)
                    $ Party[Count].Statup("Obed", 50, -2,Alt=[[LauraX],500,-3])
                    $ Party[Count].FaceChange("sad")
                    if ApprovalCheck(Party[Count], 800):
                            #pity
                            if Party[Count] == RogueX:
                                    ch_r "Aw, poor baby."   
                            elif Party[Count] == KittyX:
                                    ch_k "That's so[KittyX.like]sad."   
                            elif Party[Count] == EmmaX:
                                    ch_e "Well that's just irresponsible."     
                            elif Party[Count] == LauraX:   
                                    ch_l "You gotta cover your own tab, [LauraX.Petname]."  
                    else:
                            #anger
                            $ Party[Count].Brows = "angry"
                            if Party[Count] == RogueX:
                                    ch_r "Well that's pretty weak, asking a girl out when you can't even afford it."
                            elif Party[Count] == KittyX:
                                    ch_k "I wouldn't have gone out with you if I'd known you were such a bum." 
                            elif Party[Count] == EmmaX:
                                    ch_e "You really should learn not to shop outside your class, [EmmaX.Petname]." 
                            elif Party[Count] == LauraX:
                                    ch_l "Get your act together." 
                                    $ Party[Count].Statup("Love", 200, -1)
                            $ Party[Count].Statup("Love", 200, -3)
                            if "deadbeat" not in Party[Count].History:  
                                $ Party[Count].History.append("deadbeat") 
                            else:
                                call Girl_Date_Over(Party[Count])
    #end choice consequences
    
    #Boosts lust based on price spent
    $ Count = int(Date_Bonus[0]/2)
    $ Count = 10 if Count >= 10 else Count
    
    $ Party[0].Statup("Lust", 60, Count,Alt=[[EmmaX],75,Count])
                
    $ Count = int(Date_Bonus[1]/2)
    $ Count = 10 if Count >= 10 else Count   
    if len(Party) >= 2:
            $ Party[1].Statup("Lust", 60, Count,Alt=[[EmmaX],75,Count])
                           
    $ Count = 0
    $ Play_Cost = 0
    $ Date_Cost[0] = 0
    $ Date_Cost[1] = 0
    return
#end payment   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
 
label Date_Bonus(Girl=0, Amount=0):
    #This updates the prime value if the girl is prime, second if not.
    # call Date_Bonus(RogueX,5)
    if Party[0] == Girl:
                $ Date_Bonus[0] += Amount
    elif Girl in Party:
                $ Date_Bonus[1] += Amount
    return       
        
        
#Start Date End  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Date_End:
    #The end of the date jumped to from any end of date
    if Current_Time == "Evening":
            #makes it night time
            call Wait(Outfit = 0)        
            
            $ bg_current = "bg date"    
            call Set_The_Scene(Dress=0) 
            if "movie" in Player.DailyActions:
                "After the movie, you head back to the dorms."
            else:
                "After dinner, you head back to the dorms."   
    else:
            $ bg_current = "bg player"  
            call Set_The_Scene(Entry=1,Dress=0)  
    
    if len(Party) >= 2:
            #if there are two girls
            menu:
                "Who's room do you visit first?"
                "[RogueX.Name]" if RogueX in Party:  
                        call Girl_Date_End(RogueX)
                "[KittyX.Name]" if KittyX in Party:
                        call Girl_Date_End(KittyX)
                "[EmmaX.Name]" if EmmaX in Party:
                        call Girl_Date_End(EmmaX)
                "[LauraX.Name]" if LauraX in Party:
                        call Girl_Date_End(LauraX)
                "Bring them both back to your room" if len(Party) >= 2:
                        jump Player_Date_End
                "Neither, just head home alone": #disable     
                        call Date_Ditched
            jump Date_Over           
    if Party and Party[0]:
            call Girl_Date_End(Party[0])
    else:
            $ Party = []
            "You head back to your room." 

label Date_Over:    
    if Current_Time == "Evening":
            #makes it night time
            call Wait(Outfit = 0)
    $ Player.DailyActions.append("post date") 
    $ bg_current = "bg player"
    call CleartheRoom("All",0,1)
    jump Misplaced

label Player_Date_End:   
    #Called if you call them back to your room    
    $ bg_current = "bg player"
    $ BO = Party[:]
    while BO:
            $ BO[0].Loc = "bg player"
            $ BO.remove(BO[0])
    call Set_The_Scene(Dress=0)
    call Taboo_Level  
    if len(Party) >= 2:        
            "You bring the girls to your own door."
            menu:
                "Who do you want to talk to?"
                "[RogueX.Name]" if RogueX in Party:  
                        call Girl_Date_End(RogueX)
                "[KittyX.Name]" if KittyX in Party:
                        call Girl_Date_End(KittyX)
                "[EmmaX.Name]" if EmmaX in Party:
                        call Girl_Date_End(EmmaX)
                "[LauraX.Name]" if LauraX in Party:
                        call Girl_Date_End(LauraX)
                "Go to Sleep":
                        pass
    elif Party and Party[0]:        
            "You bring [Party[0].Name] to your own door."
            call Girl_Date_End(Party[0])
    jump Player_Room
    

# Start Girl Date End / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label Girl_Date_End(Girl=0): #nee R_Date_End  
    #Called if you end up with girl at the end of the date
    if Girl not in TotalGirls:
            $ Party = []
            jump Date_End
    if bg_current != "bg player":  
            #skips this portion if you are in the player's room already
            menu:
                "Take [Girl.Name] back to her room?":
                    pass
                "Just leave and head back to yours.":
                    call Date_Ditched
                    jump Date_Over    
                    
            $ bg_current = Girl.Home
            $ Girl.Loc = Girl.Home
            if len(Party) >= 2 and Party[1] != Girl:
                    $ Party[1].Loc = Girl.Home
            call Set_The_Scene(Dress=0)
            call Taboo_Level    
    
    if len(Party) >= 2 and Party[0] != Girl:
            # If you picked the secondary girl, it flips them       
            $ Party.reverse()  
            $ Date_Bonus.reverse()
                        
    if bg_current != "bg player":    
        "You walk [Girl.Name] back to her room."
    if Date_Bonus[0] < 0:  
            #if it was a bad date, no bonus
            $ Girl.FaceChange("angry", 0,Eyes = "side")
            if Girl == RogueX:      
                    ch_r "Well that was a waste of an evening. I'll see you around, [Player.Name]."        
            elif Girl == KittyX:
                    ch_k "You[Girl.like]really need to get your shit together, [Player.Name]."
            elif Girl == EmmaX:
                    ch_e "It's possible I could have had a worse evening, [Player.Name]."
            elif Girl == LauraX:
                    ch_l "That was a real shitshow, [Player.Name]."
            if bg_current == "bg player":
                if Girl == KittyX:
                    "She phases through the wall toward her room."
                else:
                    "She storms off down the hall."
            else:
                    "She slams the door on you."
            call Set_The_Scene(Entry=1,Dress=0)
            $ Date_Bonus[0] = 0
            call Girl_Date_Over(Girl,0)
            jump Date_End
    else: 
        if Date_Bonus[0] > 20:
            #if it was a very good date
            $ Girl.FaceChange("sexy", 1)
            if Girl == RogueX:    
                            ch_r "Well that was a lot of fun, [Girl.Petname]. I don't want the night to end . . ."          
            elif Girl == KittyX:
                    if bg_current == "bg player":
                            ch_k "That was fun, [Girl.Petname]. Do I have to go . . ."    
                    else:
                            ch_k "That was fun, [Girl.Petname]. Do you have to go . . ." 
            elif Girl == EmmaX:
                    if bg_current == "bg player":
                            ch_e "That was a lovely evening, [Girl.Petname]. Could I come in for a nightcap?"
                    else:
                            ch_e "That was a lovely evening, [Girl.Petname]. Care for a nightcap? . ."  
            elif Girl == LauraX:
                    if bg_current == "bg player":
                            ch_l "I had fun, [Girl.Petname]. We done, or. . ."    
                    else:
                            ch_l "I had fun, [Girl.Petname]. We done, or . . ."  
        else:
            #if it was a mediocre date
            $ Girl.FaceChange("smile", 1)
            if Girl == RogueX:              
                    ch_r "Well that was a lot of fun, [Girl.Petname]. We'll have to do it again."
            elif Girl == KittyX:
                    ch_k "Well that was fun, [Girl.Petname]. Text me later."
            elif Girl == EmmaX:
                    ch_e "That was a lovely evening, [Girl.Petname]. We'll have to do it again."
            elif Girl == LauraX:
                    ch_l "I had fun, [Girl.Petname]. Talk to you later."
        $ Girl.Date += 1
        menu:
            extend ""
            "Could I get a good night kiss?":
                    if ApprovalCheck(Girl, 600, Bonus=(10*Date_Bonus[0])):
                        $ Girl.Mouth = "smile"
                        if Girl == RogueX:       
                                ch_r "Ok, [Girl.Petname]. I suppose you've earned it."       
                        elif Girl == KittyX:
                                ch_k "Heh, I guess so. . ."
                        elif Girl == EmmaX:
                                ch_e "[Girl.Petname], I suppose I could indulge you."
                        elif Girl == LauraX:
                                ch_l "Well if you insist. . ."
                        call Date_Sex_Break(Girl,0,2)
                        $ MultiAction = 0
                        call KissPrep 
                        $ MultiAction = 1
                    if ApprovalCheck(Girl, 900, Bonus=(10*Date_Bonus[0])):
                        $ Girl.FaceChange("sexy", 1)
                        if Girl == RogueX:    
                                if bg_current == "bg player":
                                        ch_r "That was real nice, how about I come inside for a minute. . ."  
                                else:
                                        ch_r "That was real nice, how about you come inside for a minute. . ."           
                        elif Girl == KittyX:
                                ch_k "Hmmm . . ."   
                                if bg_current == "bg player":
                                        ch_k "Could I. . . maybe come inside for a minute?"
                                else:
                                        ch_k "Maybe. . . come inside for a minute?"
                        elif Girl == EmmaX:
                                if bg_current == "bg player":
                                        ch_e "Hmm, are you sure I couldn't come in? . ."
                                else:
                                        ch_e "Hmm, are you sure you couldn't come in? . ."
                        elif Girl == LauraX:
                                ch_l "Hmmm . . ."   
                                if bg_current == "bg player":
                                        ch_l "Could I. . . borrow you for a minute?"
                                else:
                                        ch_l "Could I. . . borrow you for a minute?"
                        call Date_Sex_Break(Girl)
                        if _return == 4:
                                if bg_current == "bg player":
                                        ch_p "You should probably get going, sorry."
                                else:
                                        ch_p "I should probably get going, sorry."
                                call Girl_Date_Over(Girl,0)
                                jump Date_End 
                    else:
                        $ Girl.FaceChange("smile", 1)
                        if Girl == RogueX:     
                                ch_r "That was real nice, I'll see you later, [Girl.Petname]."          
                        elif Girl == KittyX:
                                ch_k "That was nice, text you later!"
                        elif Girl == EmmaX:
                                ch_e "And now, I'll see you tomorrow, [Girl.Petname]." 
                        elif Girl == LauraX:
                                ch_l "That was nice, talk to you later."
                        $ Date_Bonus[0] = 0
                        call Girl_Date_Over(Girl,0)
                        jump Date_End
                    
            "Want to have a little fun first?" if bg_current != "bg player":
                    if ApprovalCheck(Girl, 800, Bonus=(10*Date_Bonus[0])):
                        $ Girl.FaceChange("sexy", 1)
                        if Girl == RogueX:     
                                ch_r "Alright, [Girl.Petname]. I think you've earned it."         
                        elif Girl == KittyX:
                                ch_k "Heh, I guess so. . ."
                        elif Girl == EmmaX:
                                ch_e "Oh, fine, [Girl.Petname]. I'll indulge you."
                        elif Girl == LauraX:
                                ch_l "I guess, sure."
                        call Date_Sex_Break(Girl)
                        if _return == 4:
                                ch_p "I should probably get going, sorry."  
                                call Girl_Date_Over(Girl,0)
                                jump Date_End  
            "Could you come in for a bit?" if bg_current == "bg player":
                    if ApprovalCheck(Girl, 800, Bonus=(10*Date_Bonus[0])):
                        $ Girl.FaceChange("sexy", 1)
                        if Girl == RogueX:   
                                ch_r "Alright, [Girl.Petname]. I think you've earned it."           
                        elif Girl == KittyX:
                                ch_k "Heh, I guess so. . ."
                        elif Girl == EmmaX:
                                ch_e "Oh, fine, [Girl.Petname]. I'll indulge you."
                        elif Girl == LauraX:
                                ch_l "I guess, sure."
                        call Date_Sex_Break(Girl)
                        if _return == 4:
                                ch_p "You should probably get going, sorry."  
                                call Girl_Date_Over(Girl,0)
                                jump Date_End                  
                    
            "Ok, good night then.":
                    $ Girl.FaceChange("confused", 1)
                    if Girl == EmmaX:   
                            $ Girl.Mouth = "smirk"
                            if bg_current == "bg player":
                                    "[Girl.Name] looks a little annoyed, but heads out."
                            else:
                                    "[Girl.Name] looks a little annoyed, but you head out."
                    else:
                            if bg_current == "bg player":
                                    "[Girl.Name] looks a little confused, but she heads out."
                            else:
                                    "[Girl.Name] looks a little confused, but you head out."
                    call Girl_Date_Over(Girl,0)
                    jump Date_End
                
    # Rogue lets you into her room:
    if bg_current != "bg player":
            $ bg_current = Girl.Home 
    call Set_The_Scene(Dress=0)
    call Taboo_Level 
    $ Girl.FaceChange("sexy", 1)
    if Girl == RogueX:           
            if len(Party) < 2:#not Party[1]:
                            ch_r "So, [Girl.Petname], you've got me all alone, what are your intentions? . ."
            else:
                    if bg_current == "bg player":
                            ch_r "So, [Girl.Petname], we're in your room together, what are your intentions? . ."
                    else:
                            ch_r "So, [Girl.Petname], we're in my room together, what are your intentions? . ."   
    elif Girl == KittyX:
                            ch_k "So[Girl.like]here we are. . . "
    elif Girl == EmmaX:
            if len(Party) < 2: #not Party[1]:
                            ch_e "Now, [Girl.Petname], we're alone together, what would you like to do next? . ."
            else:
                    if bg_current == "bg player":           
                            ch_e "Now, [Girl.Petname], we're in your room together, what would you like to do next? . ."
                    else:
                            ch_e "Now, [Girl.Petname], we're in my room together, what would you like to do next? . ."
    elif Girl == LauraX:
                            ch_l "So. . . after a date like that. . . "
    $ Player.DailyActions.append("post date") 
#    $ renpy.pop_call() #removes call to date
#    $ renpy.pop_call() #removes call to Events
    call expression Girl.Tag + "_SexMenu"  # You have what sex you can get away with
    
    if "angry" in Girl.RecentActions:       
            if bg_current == "bg player": 
                if Girl == KittyX:
                    "[KittyX.Name] storms off through the nearest wall."
                elif Girl == EmmaX:
                    "[EmmaX.Name] stalks through the door and back to her room." 
                else:
                    "[Girl.Name] storms off down the hall." 
            else:
                    "[Girl.Name] shoves you out into the hall. You head back to your room."
                    $ bg_current = "bg player"
            call Remove_Girl("All")
            $ Player.DailyActions.append("post date") 
            jump Player_Room
                                        
    call Sleepover(Girl)  
    jump Misplaced

# End Girl Date End / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    


label Date_Ditched(Girls=0):  
    #if you ditch out on a date, called by Date End
    #Girls tracks the number fo people who have already answered.
    while Party:
        if Party[0] in TotalGirls:
                if ApprovalCheck(Party[0], 1200):
                    $ Party[0].FaceChange("confused")
                    if Party[0] == RogueX:
                            if Girls:
                                    ch_r "Yeah, bye?"
                            else:
                                    ch_r "Huh? Ok, bye, I guess."
                    elif Party[0] == KittyX: 
                            if Girls:
                                    ch_k "Yeah, um, bye?"
                            else:
                                    ch_k "Um, bye?" 
                    elif Party[0] == EmmaX:   
                            if Girls:
                                    ch_e "Yes, a pity."
                            else:
                                    ch_e "Oh? Pity."
                    elif Party[0] == LauraX:   
                            if Girls:
                                    ch_l "Yeah, bye."
                            else:
                                    ch_l "Um, ok, bye."
                elif ApprovalCheck(Party[0], 400):
                    $ Party[0].FaceChange("smile")
                    if Party[0] == RogueX:
                            if Girls:
                                    ch_r "Yeah, see ya later."
                            else:
                                    ch_r "Oh, bye then."
                    elif Party[0] == KittyX:  
                            if Girls:
                                    ch_k "Yeah, Bye!"
                            else:
                                    ch_k "Bye!"
                    elif Party[0] == EmmaX:   
                            if Girls:
                                    ch_e "Oh, yes, good night."
                            else:
                                    ch_e "Good night then."
                    elif Party[0] == LauraX:   
                            if Girls:
                                    ch_l "Yeah, bye."
                            else:
                                    ch_l "Um, ok, bye."
                else:
                    $ Party[0].FaceChange("angry")
                    if Party[0] == RogueX:
                            if Girls:
                                    ch_r "Right, \"bye.\""
                            else:
                                    ch_r "Good riddance."
                    elif Party[0] == KittyX:  
                            if Girls:
                                    ch_k "Yeah, later, asshole."
                            else:
                                    ch_k "Later, asshole."
                    elif Party[0] == EmmaX:  
                            if Girls:
                                    ch_e "I'm not surprised."
                            else:
                                    ch_e "You're excused!" 
                    elif Party[0] == LauraX:   
                            if Girls:
                                    ch_l "Wow, yeah, bye."
                            else:
                                    ch_l "Screw you."
                $ Party[0].Loc = Party[0].Home
                $ Girls += 1
        $ Party.remove(Party[0])
    return
        
# Start Girl Date Over / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Date_Over(Girl=0,Angry=1):
        # Called if Girl is pissed and leaves
        if Angry:
                $ Girl.RecentActions.append("angry") 
                $ Girl.DailyActions.append("angry")  
                $ Girl.FaceChange("angry")
                if Girl == RogueX:   
                        ch_r "I think I'm done here, [Girl.Petname]."             
                elif Girl == KittyX:
                        ch_k "You know what?" 
                        ch_k "[Player.Name]'s a Jerk!" 
                elif Girl == EmmaX:
                        ch_e "I think that's enough of that, [Girl.Petname]." 
                elif Girl == LauraX:
                        ch_l "What was that?" 
                        ch_l "Eat a dick." 
                "[Girl.Name] storms out." 
        if "study" in Player.RecentActions:        
                call Remove_Girl(Girl)
                return
        if Party[0] == Girl:
                $ Date_Bonus[0] = Date_Bonus[1]
                $ Date_Cost[0] = Date_Cost[1]
                $ Date_Cost[1] = 0         
        elif Girl in Party:
                # If this person was in the second slot, flip them. 
                $ Date_Bonus.reverse
                $ Date_Cost.reverse
                
        $ Date_Bonus[1] = 0
        $ Date_Cost[1] = 0
        call Remove_Girl(Girl)
        if not Party:
                #if nobody is left, quit the date
                jump Date_End
        call Shift_Focus(Party[0])      
        return
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>