# Start Jackin it check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Jackin(Girl=0,Cnt=0,BO=[]):
        #Called when you try to jack it from inside a sex action
        #should include a girl's name, if not, one is randomly picked from the room.
        if not Girl or Girl not in TotalGirls:        
                $ BO = TotalGirls[:]  
                while BO:                   
                        if BO[0].Loc == bg_current:
                                $ Girl = BO[0]
                                $ BO = [1]
                        $ BO.remove(BO[0])
                                
        if "unseen" in Girl.RecentActions:
                $ Player.RecentActions.append("cockout") 
                $ Trigger2 = "jackin"
                "You whip out your cock and start working it." 
        else:
                if not Player.Semen:
                        "You don't think that would accomplish much, the poor thing is napping." 
                        return
                
                if "cockout" in Player.RecentActions:
                        "You start working your cock."
                else:
                        "You whip out your cock and start working it." 
                        $ Player.RecentActions.append("cockout")
                        call Seen_First_Peen(Girl,Partner)
                
                $ Trigger2 = "jackin"
                if "jackin" in Girl.RecentActions:
                    return            
                $ Girl.AddWord(0,"jackin","jackin",0,0)
                
                if Girl == EmmaX and "classcaught" not in Girl.History:
                        $ Girl.FaceChange("surprised", 1) 
                        $ Girl.Eyes = "down"
                        ch_e "Wait. . ."
                        $ Girl.FaceChange("angry", 1)                    
                        ch_e "That really isn't appropriate."  
                        $ Girl.Statup("Lust", 50, 7) 
                        if not ApprovalCheck(EmmaX, 1200, TabM = 3):
                                $ Girl.AddWord(0,"angry","angry",0,0)
                                $ renpy.pop_call()
                                return
                                
                if Girl.SEXP < 10:
                        $ Girl.FaceChange("surprised", 2) 
                        $ Girl.Eyes = "down"
                        if Girl == LauraX:
                                $ Girl.Brows = "confused"
                                "[Girl.Name] seems perplexed that you would do something like that."  
                        else:
                                "[Girl.Name] blushes furiously, shocked at your behavior."  
                        $ Girl.FaceChange("angry", 1) 
                        $ Girl.Statup("Lust", 50, 5) 
                        if not ApprovalCheck(Girl, 1200, TabM = 3):
                                $ Girl.AddWord(0,"angry","angry",0,0)
                                $ renpy.pop_call()
                                return
                elif Girl.SEXP <= 15:            
                        $ Girl.FaceChange("surprised", 2) 
                        $ Girl.Eyes = "down"
                        if Girl == EmmaX:
                                $ Girl.Blush = 1
                                "[Girl.Name] looks down at your cock with some surprise."
                                $ Girl.Statup("Lust", 60, 2)
                        else:
                                "[Girl.Name] looks down at your cock with surprise."
                        $ Girl.FaceChange("perplexed", 1) 
                        $ Girl.Statup("Lust", 60, 8)
                        if not ApprovalCheck(Girl, 1200, TabM = 3):
                                return
                elif ApprovalCheck(Girl, 1100, TabM = 3):
                        $ Girl.FaceChange("surprised", 1) 
                        $ Girl.Eyes = "down"
                        "[Girl.Name] looks down at your cock and smiles."            
                        $ Girl.FaceChange("sly", 1) 
                        $ Girl.Statup("Lust", 70, 8,Alt=[[EmmaX],60,12])
                elif ApprovalCheck(Girl, 500, "I", TabM=2):
                        $ Girl.FaceChange("surprised", 1) 
                        $ Girl.Eyes = "down"
                        "[Girl.Name] glances at it, but just smiles in amusement."        
                        $ Girl.FaceChange("sly", 1) 
                        $ Girl.Statup("Lust", 70, 10,Alt=[[EmmaX],60,15])
                else:
                        $ Girl.FaceChange("angry", 1) 
                        $ Girl.Eyes = "down"
                        "[Girl.Name] glances down at your cock with a scowl."        
                        $ Girl.Eyes = "sexy"                
                        $ Girl.AddWord(0,"angry","angry",0,0)
                        return
                
                if Girl.Action and Girl.Loc == bg_current:
                    $ BO = ["none"]
                    
                    if Girl.Hand >= 5 and ApprovalCheck(Girl, 1100, TabM = 3):
                            $ Cnt = Girl.Hand - 4
                            $ Cnt = 10 if Cnt > 10 else Cnt
                            while Cnt:
                                $ BO.append("hand") 
                                $ Cnt -= 1
                    if Girl.Blow >= 5 and ApprovalCheck(Girl, 1300, TabM = 3):
                            $ Cnt = Girl.Blow - 4
                            $ Cnt = 10 if Cnt > 10 else Cnt
                            $ Cnt += 5 if "hungry" in Girl.Traits else 0
                            while Cnt:
                                $ BO.append("blow") 
                                $ Cnt -= 1
                    if Girl.Tit >= 5 and ApprovalCheck(Girl, 1200, TabM = 5):
                            $ Cnt = Girl.Tit - 4
                            $ Cnt = 10 if Cnt > 10 else Cnt
                            while Cnt:
                                $ BO.append("Tit") 
                                $ Cnt -= 1
                    if Girl.Sex >= 5 and ApprovalCheck(Girl, 1400, TabM = 5):
                            $ Cnt = Girl.Sex - 4
                            $ Cnt = 10 if Cnt > 10 else Cnt
                            $ Cnt += 5 if Girl.Lust >= 70 else 0
                            while Cnt:
                                $ BO.append("sex") 
                                $ Cnt -= 1
                    if Girl.Anal >= 5 and ApprovalCheck(Girl, 1550, TabM = 5):
                            $ Cnt = Girl.Anal - 4
                            $ Cnt = 10 if Cnt > 10 else Cnt
                            $ Cnt += 5 if Girl.Lust >= 70 and Girl.Loose else 0
                            while Cnt:
                                $ BO.append("anal") 
                                $ Cnt -= 1
                        
                    $ renpy.random.shuffle(BO) 
                    
                    if BO[0] == "hand":
                            if Girl == RogueX:
                                    ch_r "Sure you don't want me to handle that for you?"
                            elif Girl == KittyX:
                                    ch_k "I could. . . lend you a hand?"
                            elif Girl == EmmaX:  
                                    ch_e "Would you care for a hand with that?"
                            elif Girl == LauraX:
                                    ch_l "Did you want some help with that?"
                    elif BO[0] == "blow":
                            if Girl == RogueX:
                                    ch_r "Sure my mouth wouldn't do better?"
                            elif Girl == KittyX:
                                    ch_k "I could, get that wet for you. . ."
                            elif Girl == EmmaX:   
                                    ch_e "I wouldn't mind a taste of that. . ."
                            elif Girl == LauraX:
                                    ch_l "Well that looks tasty. . ."
                    elif BO[0] == "tit":
                            if Girl == RogueX:
                                    ch_r "Sure you wouldn't prefer using these?"
                            elif Girl == KittyX:
                                    ch_k "My chest might keep that warm. . ."
                            elif Girl == EmmaX:   
                                    ch_e "If you like, I could use my chest. . ."
                            elif Girl == LauraX:
                                    ch_l "I could use my tits. . ."
                    elif BO[0] == "sex":
                            if Girl == RogueX:
                                    ch_r "Oh, you're making me pretty wet here. . ."
                            elif Girl == KittyX:
                                    ch_k "I'm getting a little wet. . ."
                            elif Girl == EmmaX:    
                                    ch_e "I'm positively dripping, you know. . ."
                            elif Girl == LauraX:
                                    ch_l "Well that's getting me wet. . ."
                    elif BO[0] == "anal":
                            if Girl == RogueX:
                                    ch_r "You've really got my ass tingling. . ."
                            elif Girl == KittyX:
                                    ch_k "Why don't you bring that in through the back. . ."
                            elif Girl == EmmaX:       
                                    ch_e "I wouldn't mind you using the back door. . ."                          
                            elif Girl == LauraX:
                                    ch_l "Why don't you stick that in me. . ."
                    else:
                            if Girl == RogueX:
                                    ch_r "I like what I'm seeing here. . ."
                            elif Girl == KittyX:
                                    ch_k "Prrrr. . ."
                            elif Girl == EmmaX:                            
                                    ch_e "Mmmmm. . ."    
                            elif Girl == LauraX:
                                    ch_l "Prrrr. . ."
                            return
                        
                    menu:
                        extend ""
                        "No thanks, I've got this in hand.":
                                if Girl == RogueX:
                                        ch_r "Your loss, [Girl.Petname]."
                                elif Girl == KittyX:
                                        ch_k "What ev, [Girl.Petname]."
                                elif Girl == EmmaX:  
                                        $ Girl.FaceChange("perplexed", 1) 
                                        ch_e "Oh. . ."      
                                        ch_e "Carry on then, [Girl.Petname]."
                                        $ Girl.FaceChange("sly", 0,Eyes="down") 
                                elif Girl == LauraX:
                                        ch_l "Can't say I didn't offer."
                                return
                        "Hmm, sounds like a plan.": 
                                $ Situation = "shift"
                    
                    $ Trigger2 = 0
                    #Close out what you were doing    
                    if Trigger == "strip":
                            call Group_Strip_End
                    elif Trigger == "masturbation":
                            $ Girl.Action -= 1
                            $ Girl.Mast += 1    
                            call Checkout          
                    elif Trigger:
                            call CloseOut(Girl)
                                    
                    show blackscreen onlayer black
                    hide blackscreen onlayer black
                    if BO[0] == "hand":
                            jump expression Girl.Tag + "_HJ_Prep"
                    elif BO[0] == "blow":
                            jump expression Girl.Tag + "_BJ_Prep"
                    elif BO[0] == "tit":
                            jump expression Girl.Tag + "_TJ_Prep"
                    elif BO[0] == "sex":
                            jump expression Girl.Tag + "_SexPrep"
                    elif BO[0] == "anal":
                            jump expression Girl.Tag + "_AnalPrep"
        return
# end Jackin it check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# For when she tags you to drain you start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Tag(Girl=0,Forced = 0,Gloves=0):
        #Called mostly by Addiction
        if Girl not in TotalGirls:
                $ Girl = Ch_Focus
        call Shift_Focus(Girl)
        $ Gloves = Girl.Arms
        $ Girl.ArmPose = 2
        if not Forced:
                $ Girl.Eyes = "closed"
                $ Girl.Brows = "sad"
        
        if Forced and Player.Lvl >= 5:
            if Gloves == "gloves":
                    $ Girl.Arms = 0
                    "She pulls off her gloves and reaches for your face."     
            else:
                    "She reaches out towards your face."                          
            menu:
                extend ""
                "Catch her arm [[refuse].":
                        $ Girl.FaceChange("surprised", 1) 
                        "As she reaches out, you bat her arm away. The brief contact isn't enough for her."
                        $ Girl.FaceChange("angry") 
                        $ Girl.Statup("Love", 80, -10)
                        if Girl.Addict >= 80 and not ApprovalCheck(Girl, 400, "O",Alt=[[RogueX],600]): 
                                #if she's strung out and not obedient
                                $ Girl.Eyes = "manic"                        
                                "She lashes out and leaps at you, grabbing you by the chin."
                                $ Girl.Eyes = "sly"   
                                if "no tag" not in Girl.RecentActions:
                                        $ Girl.Statup("Obed", 50, -5)
                                        $ Girl.Statup("Inbt", 30, 5)
                                        $ Girl.Statup("Inbt", 90, 1)  
                                $ Forced = 1
                        else:
                                if Girl == RogueX:
                                        ch_r "Not cool, [Girl.Petname]."
                                elif Girl == KittyX:
                                        ch_k "[Girl.Like]so not cool, [Girl.Petname]."
                                elif Girl == EmmaX:
                                        ch_e "You don't want me as an enemy, [Player.Name]."
                                elif Girl == LauraX:
                                        ch_l "Don't push me, [Girl.Petname]."
                                if "no tag" not in Girl.RecentActions:
                                        $ Girl.Statup("Obed", 50, 5)
                                        $ Girl.Statup("Obed", 80, 5)                    
                                $ Girl.RecentActions.append("no tag")
                                $ Girl.DailyActions.append("no tag")
                                $ Girl.Arms = Gloves
                                $ Girl.ArmPose = 1
                                return                        
                "Let her.":
                        "She touches your face."
        else:
                $ Girl.Addict -= 10          
                $ Girl.Addictionrate += 1 if Girl.Addictionrate < 5 else 0 
                $ Girl.Statup("Lust", 90, 5)
                if Gloves == "gloves":
                        $ Girl.Arms = 0
                        $ Line = "She pulls off her gloves and"    
                else:
                        $ Line = "She reaches out and"
                if Girl == RogueX:
                            "[Line] touches your face for a moment."
                elif Girl == KittyX:
                            "[Line] grabs both sides of your face, looking intently into your eyes."
                elif Girl == EmmaX:
                            "[Line] rubs the back of her hand against your cheek."
                elif Girl == LauraX:  
                            "[Line] grabs your face in one hand, firmly smooshing your cheeks together."
        $ Girl.Blush = 2
        while Girl.Addict > 20:     
                $ Girl.Addictionrate += 1 if Girl.Addictionrate < 5 else 0 
                $ Girl.Addict -= 15  
                $ Girl.Statup("Lust", 90, 5)
                if Girl == RogueX:
                        $ Girl.Statup("Lust", 90, 5)
                elif Forced:
                        $ Girl.Statup("Obed", 50, 1)
                "She continues to touch you, and a slight shiver passes through her."
        if Gloves and not Girl.Arms:
                "Appearing sated, she puts her gloves back on."  
        $ Girl.Blush = 1
        $ Girl.Arms = Gloves
        $ Girl.ArmPose = 1
        $ Girl.FaceChange()    
        if Forced:
                $ Girl.RecentActions.append("forced tag")
                $ Girl.DailyActions.append("forced tag")
        $ Girl.RecentActions.append("tag")
        $ Girl.DailyActions.append("tag")
        return
# End "tag" action / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Slap Ass / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Slap_Ass(Girl=0):
        if Girl not in TotalGirls:
                return
        call Shift_Focus(Girl)
        # fix add sound here?
        call Punch
                
        $ Girl.Slap += 1 #add in slap-base obedience  
            
        $ Girl.Blush = 2 if Taboo else 1
        if ApprovalCheck(Girl, 200, "O", TabM=1):   
                $ Girl.FaceChange("sexy", 1)  
                $ Girl.Mouth = "surprised"
                $ Girl.Statup("Lust", 51, 3, 1)
                if Girl.RecentActions.count("slap") < 4:
                        $ Girl.Statup("Lust", 200, 1)
                        if Girl.Slap <= 5:
                                $ Girl.Statup("Obed", 50, 2)
                        if Girl.Slap <= 10:
                                $ Girl.Statup("Obed", 80, 1)
                "You slap her ass and she jumps with pleasure."
        else:                
                $ Girl.FaceChange("surprised", 1)        
                if Girl.RecentActions.count("slap") < 4:
                        $ Girl.Statup("Obed", 70, 2)        
                        $ Girl.Statup("Love", 50, -1)
                "You slap her ass and she looks back at you a bit startled."  
            
        if Trigger and Girl.Lust >= 100:         
                #If you're still going at it and Rogue can cum
                call Girl_Cumming(Girl)
                                
        if Taboo:    
                if not ApprovalCheck(Girl, 800, TabM=2):
                        if Girl.Slap <= 5:
                                $ Girl.Statup("Obed", 80, 2)  
                                $ Girl.Statup("Obed", 50, 2)      
                        $ Girl.Statup("Love", 70, -2)    
                        $ Girl.Statup("Love", 50, -1)
                        "She looks pretty mad though."  
                elif not ApprovalCheck(Girl, 1500, TabM=2):
                        if Girl.Slap <= 5:
                                $ Girl.Statup("Obed", 80, 2)
                        $ Girl.Statup("Love", 70, -1)
                        "She looks a bit embarrassed."  
                else:                         #Over 1500
                        $ Girl.FaceChange("sexy")
                        $ Girl.Mouth = "smile"
                        if Girl.Slap <= 5:
                                $ Girl.Statup("Obed", 80, 1)
                        "She gives you a naughty grin." 
                $ Girl.Blush = 1
                    
        $ Girl.RecentActions.append("slap") if Girl.RecentActions.count("slap") < 4 else Girl.RecentActions
        $ Girl.DailyActions.append("slap") if Girl.DailyActions.count("slap") < 10 else Girl.DailyActions
        return
        
# End Slap Ass / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        
# Start Makeout / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Makeout(Girl=0):    
        if Girl not in TotalGirls:
                return
        $ Round -= 5 if Round > 5 else (Round-1)
        call Shift_Focus(Girl)
        
        $ Approval = ApprovalCheck(Girl, 700, TabM=1,Alt=[[RogueX],500]) #reduced check for Rogue
        
        if Girl == EmmaX and not ApprovalCheck(Girl, 1000):
                #if it's Emma, and she doesn't like you all that much. . .        
                $ Girl.FaceChange("sadside") 
                ch_e "Not when we barely know each other. . ."   
                $ Girl.RecentActions.append("no kissing")                      
                $ Girl.DailyActions.append("no kissing")
                return
        if Approval > 1 and not Girl.Kissed and not Girl.Forced:   
                #first time and she's into it
                $ Girl.FaceChange("sexy")
                $ Girl.Eyes = "side"
                if Girl == RogueX: 
                        ch_r "I've never really been able to do this, so I'm a bit excited to try. . ."   
                elif Girl == KittyX:   
                        ch_k "You are kinda cute. . ."            
                elif Girl == EmmaX:                     
                        ch_e "Well, I suppose it couldn't hurt. . ."                    
                elif Girl == LauraX:
                        ch_l "Worth a shot. . ."
        elif Approval and not Girl.Kissed:     
                #first time, lower enthusiasm
                $ Girl.FaceChange("sexy")
                $ Girl.Eyes = "side"
                if Girl == RogueX: 
                        ch_r "I guess it's worth a shot. . ."   
                elif Girl == KittyX:    
                        ch_k "I'll give it a go. . ."             
                elif Girl == EmmaX:      
                        ch_e "We could. . ."               
                elif Girl == LauraX:
                        ch_l "If you insist. . ."   
        elif Approval and "kissing" in Girl.RecentActions:
                # you were just kissing earlier
                $ Girl.FaceChange("sexy", 1)
                if Girl == KittyX: 
                        ch_k "Prrr. . ."                      
                else:
                        call AnyLine(Girl,"Mmmm. . .")
                jump KissPrep
        elif Approval and "kissing" in Girl.DailyActions:
                #you'd been kissing earlier in the day
                $ Girl.FaceChange("sexy", 1)
                
                $ Line = renpy.random.choice(["A","B","C"])  
                if Line == "A":
                    call AnyLine(Girl,"Didn't get enough earlier?")
                elif Girl == RogueX: 
                    if Line == "B":
                            ch_r "{i}I'm{/i} used to being the one sucking people dry. . ."
                    else: 
                            ch_r "Gimme some sugar, sugar."
                elif Girl == KittyX:   
                    if Line == "B":
                            ch_k "Meow."
                    else: 
                            ch_k "Come'ere tasty."           
                elif Girl == EmmaX:    
                    if Line == "B":
                            ch_e "Mmmm. . ."
                    else: 
                            ch_e "Come and get it."              
                elif Girl == LauraX:
                    if Line == "B":
                            ch_l "Mmmmmm."
                    else: 
                            ch_l "Get over here."
                $ Line = 0
        elif Approval > 1 and Girl.Love > Girl.Obed:   
                # love is higher than obedience
                $ Girl.FaceChange("sexy")
                if Girl == RogueX: 
                        ch_r "Sure, why not?" 
                elif Girl == KittyX:    
                        ch_k "Smooches!"            
                elif Girl == EmmaX:   
                        ch_e "Mwa."                     
                elif Girl == LauraX:  
                        ch_l "Mmmmm. . ."    
        elif ApprovalCheck(Girl, 500, "O") and Girl.Obed > Girl.Love:
                # if Obedience is higher
                $ Girl.FaceChange("normal")
                if Girl == RogueX: 
                        ch_r "If you wish." 
                elif Girl == KittyX:
                        ch_k "Sure, ok."                  
                elif Girl == EmmaX:      
                        ch_e "Of course."             
                elif Girl == LauraX:   
                        ch_l "If you want."
                $ Girl.Statup("Obed", 60, 1)        
        elif ApprovalCheck(Girl, 250, "O") and ApprovalCheck(Girl, 250, "L"): # ApprovalCheck("Laura", 300, "O") and ApprovalCheck("Laura", 200, "L"): kitty too
                #if not that into it
                $ Girl.FaceChange("bemused")
                call AnyLine(Girl,"Ok, fine.")
                $ Girl.Statup("Obed", 50, 3)
        elif Girl.Addict >= 50:
                #high addiction
                $ Girl.FaceChange("sexy")
                $ Girl.Eyes = "manic"
                if Girl == RogueX: 
                        ch_r "Hm. . . ok, let's do this."  
                elif Girl == KittyX:   
                        ch_k "I kinda have to."            
                elif Girl == EmmaX:     
                        ch_e ". . . yes."                
                elif Girl == LauraX:
                        ch_l "I have to."   
        elif Approval:   
                #she's barely into it
                $ Girl.FaceChange("bemused")
                if Girl == RogueX: 
                        ch_r "hmm, ok."   
                elif Girl == KittyX:  
                        ch_k "Yeah, whatever."              
                elif Girl == EmmaX: 
                        ch_e "Very well."                   
                elif Girl == LauraX: 
                        ch_l "Sure." 
        else:        
                #she's out
                $ Girl.FaceChange("normal") # Else
                $ Girl.Mouth = "sad"
                if Girl == RogueX: 
                        ch_r "Nah, I don't think I'm interested."
                elif Girl == KittyX:   
                        ch_k "Nope."              
                elif Girl == EmmaX:     
                        ch_e "Hmmm, no."              
                elif Girl == LauraX:
                        ch_l "No."
                $ Girl.RecentActions.append("no kissing")                      
                $ Girl.DailyActions.append("no kissing") 
                return    
        
label KissPrep(Girl=Ch_Focus):    
        if Girl not in TotalGirls:
            $ Girl = Ch_Focus
        $ Girl.Statup("Inbt", 10, 1)
        $ Girl.Statup("Inbt", 20, 1)
        
        call expression Girl.Tag + "_Kissing_Launch" pass ("kiss you")
        
        if Girl.Kissed >= 10 and Girl.Inbt >= 300:
                $ Girl.FaceChange("sucking")
        elif Girl.Kissed > 1 and Girl.Addict >= 50:
                $ Girl.FaceChange("sucking")
        else:
                $ Girl.FaceChange("kiss",2) 
        if Taboo:
                $ Girl.DrainWord("tabno")
        $ Girl.DrainWord("no kissing")
        
        if Girl == RogueX and not Girl.Kissed:                 
                #If it's Rogue's first time, it's only a simple kiss and then ends
                "You lean in and your lips meet [Girl.Name]'s." 
                $ Girl.Eyes = "surprised"
                $ Girl.Statup("Love", 90, 15)
                $ Girl.Statup("Love", 60, 30) 
                "A slight spark passes between you and her eyes widen with surprise."
                $ Girl.Statup("Lust", 70, 5) 
                ch_r "Wow, [Girl.Petname], that was really something. . ."
                $ Girl.FaceChange("bemused",1) 
                ch_r "Not the kind of zap I'm used to."
                $ Girl.Addict -= 5                 
                $ Girl.Statup("Obed", 30, 20)
                $ Girl.Statup("Inbt", 30, 30)
                jump Kiss_After
        
        if Situation == Girl:                                                      
                #Girl auto-starts   
                $ Situation = 0
                "[Girl.Name] presses her body against yours, and kisses you deeply."
                menu:
                    "What do you do?"
                    "Go with it.":                    
                            $ Girl.Statup("Inbt", 80, 3) 
                            $ Girl.Statup("Inbt", 50, 2)
                            "You lean in to the kiss."
                    "Praise her.":       
                            $ Girl.FaceChange("sexy", 1)                    
                            $ Girl.Statup("Inbt", 80, 3) 
                            ch_p "Mmm, this is a nice surprise, [Girl.Pet]."
                            $ Girl.NameCheck() #checks reaction to petname
                            "You lean in to the kiss."
                            $ Girl.Statup("Love", 85, 1)
                            $ Girl.Statup("Obed", 90, 1)
                            $ Girl.Statup("Obed", 50, 2)
                    "Ask her to stop.":
                            "You pull back."
                            $ Girl.FaceChange("surprised")       
                            $ Girl.Statup("Inbt", 70, 1) 
                            ch_p "Let's not do that right now, [Girl.Pet]."
                            $ Girl.NameCheck() #checks reaction to petname
                            $ Girl.Statup("Obed", 90, 1)
                            $ Girl.Statup("Obed", 50, 1)
                            $ Girl.Statup("Obed", 30, 2)
                            $ Player.RecentActions.append("nope")   
                            $ Girl.AddWord(1,"refused","refused")  
                            return          
                #end auto
        
        if Girl.Kissed >= 10 and Girl.Lust >= 80:
                $ Line = renpy.random.choice(["She's all over you, running her hands along your body.",  
                        "She's all over you, licking all over your face and neck.",  
                        "She's all over you, kissing all over your face and grinding against you."])   
        elif Girl.Kissed > 7:
                $ Line = renpy.random.choice(["She's really sucking face.",
                        "You kiss deeply and passionately.",
                        "You kiss deeply and passionately.",
                        "You kiss deeply and passionately."]) 
        elif Girl.Kissed > 3:
                $ Line = renpy.random.choice(["She's really getting into it.",
                        "She's really getting into it, her tongue's going at it.",
                        "She's really getting into it, there's some heavy tongue action."]) 
        else:
                $ Line = "You and "+ Girl.Name +" make out for a while." 
        "[Line]"    
        $ Cnt = 0
        $ Trigger = "kiss you"
        $ Line = 0
        if Situation:     
            $ renpy.pop_call() 
            $ Situation = 0  
     
label KissCycle(Girl=0):
        if not Girl:
                $ Girl = Ch_Focus
        while Round >=0:
            call Shift_Focus(Girl)
            call expression Girl.Tag + "_Kissing_Launch" pass ("kiss you")   
            $ Girl.LustFace()   
            $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0
            if  Player.Focus < 100:                                                    
                        #Player Command menu
                        menu:
                            "Keep going. . .":
                                        pass         
                                                            
                            "Slap her ass":                     
                                        call Slap_Ass(Girl)  
                                        $ Cnt += 1
                                        $ Round -= 1                                      
                                        jump KissCycle  
                            
                            "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                        pass
                            "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                        "You concentrate on not burning out too quickly."                
                                        $ Player.FocusX = 1
                            "Release your focus." if Player.FocusX:
                                        "You release your concentration. . ."                
                                        $ Player.FocusX = 0
                                            
                            "Start jack'in it." if MultiAction and Trigger2 != "jackin":
                                        call Jackin(Girl)                        
                            "Stop jack'in it." if MultiAction and Trigger2 == "jackin":
                                        "You stop jack'in it."
                                        $ Trigger2 = 0
                                    
                            "Other options":
                                    menu:   
                                        "Offhand action":
                                                if Girl.Action and MultiAction:
                                                        call Offhand_Set
                                                        if Trigger2:
                                                             $ Girl.Action -= 1
                                                else:
                                                        call Sex_Basic_Dialog(Girl,"tired") 
                                                        #"I'm actually getting a little tired, so maybe we could wrap this up?"
                                                    
                                        "Shift primary action":
                                                if Girl.Action and MultiAction:
                                                        menu:  
                                                            "Move a hand to her breasts. . ." if Girl.Kissed >= 1 and MultiAction:
                                                                    if Girl.Action and MultiAction:
                                                                        $ Situation = "auto"
                                                                        call Kiss_After   
                                                                        call expression Girl.Tag + "_Fondle_Breasts" 
                                                                        if Trigger == "fondle breasts": 
                                                                            $ Trigger2 = "kiss you"   
                                                                            call expression Girl.Tag + "_FB_Prep" 
                                                                        else: 
                                                                            $ Trigger = "kiss you"     
                                                                    else:
                                                                        "As your hands creep upwards, she grabs your wrists."
                                                                        call Sex_Basic_Dialog(Girl,"tired") 
                                                                        #"I'm actually getting a little tired, so maybe we could wrap this up?"
                                                            "Move a hand to her thighs. . ." if Girl.Kissed >= 1 and MultiAction:
                                                                    if Girl.Action and MultiAction:
                                                                        $ Situation = "auto"
                                                                        call Kiss_After
                                                                        call expression Girl.Tag + "_Fondle_Thighs" 
                                                                        if Trigger == "fondle thighs": 
                                                                                $ Trigger2 = "kiss you"     
                                                                                call expression Girl.Tag + "_FT_Prep" 
                                                                        else: 
                                                                                $ Trigger = "kiss you"     
                                                                    else:
                                                                        "As your hands creep downwards, she grabs your wrists."
                                                                        call Sex_Basic_Dialog(Girl,"tired") 
                                                                        #"I'm actually getting a little tired, so maybe we could wrap this up?"
                                                            "Never Mind":
                                                                        jump KissCycle
                                                else:
                                                                        call Sex_Basic_Dialog(Girl,"tired") 
                                                                        #"I'm actually getting a little tired, so maybe we could wrap this up?"
                                        "Threesome actions (locked)" if not Partner: 
                                            pass
                                        "Threesome actions" if Partner:  
                                            menu:
                                                "Ask [Girl.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                            call Les_Change(Girl)
                                                            
                                                "Ask [Girl.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                            pass
                                                "Ask [Partner.Name] to do something else":
                                                            call Three_Change(Girl)  
                                                            
                                                "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                            $ ThreeCount = 0                                                            
                                                "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                            $ ThreeCount = 0    
                                                            
                                                "Swap to [Partner.Name]":
                                                            call Trigger_Swap(Girl)
                                                "Undress [Partner.Name]":
                                                            call Girl_Undress(Partner) 
                                                            call Shift_Focus(Partner)
                                                            jump KissCycle 
                                                "Clean up Partner":
                                                            call Girl_Cleanup(Partner,"ask")   
                                                            call Shift_Focus(Partner)
                                                            jump KissCycle 
                                                "Never mind":
                                                            jump KissCycle 
                                        "Undress [Girl.Name]":
                                                call Girl_Undress(Girl) 
                                        "Clean up [Girl.Name] (locked)" if not Girl.Spunk:
                                                pass  
                                        "Clean up [Girl.Name]" if Girl.Spunk:
                                                call Girl_Cleanup(Girl,"ask")                                            
                                        "Never mind":
                                                jump KissCycle 
                            
                            "Back to Sex Menu" if MultiAction and Girl.Kissed >= 5:  
                                    ch_p "Let's try something else." 
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Kiss_After
                            "End Scene": 
                                    ch_p "Let's stop for now."
                                    $ Line = 0
                                    jump Kiss_After
            #End menu (if Line)
            
            call Shift_Focus(Girl)
            call Sex_Dialog(Girl,Partner)
            
            $ Cnt += 1
            $ Round -= 1  
            
            $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up     
            if Player.Focus >= 100 or Girl.Lust >= 100:      
                        #If either of you could cum   
                        if Player.Focus >= 100: 
                                #If you can cum:
                                call Player_Cumming(Girl)
                                if "angry" in Girl.RecentActions:  
                                        call expression Girl.Tag + "_Pos_Reset" 
                                        return    
                                $ Girl.Statup("Lust", 200, 5) 
                                if 100 > Girl.Lust >= 70 and Girl.OCount < 2 and Girl.SEXP >= 20:             
                                        $ Girl.RecentActions.append("unsatisfied")                      
                                        $ Girl.DailyActions.append("unsatisfied")                             
                                if Player.Focus > 80:
                                        jump Kiss_After 
                                $ Line = "came"
         
                        if Girl.Lust >= 100:       
                                #If you're still going at it and Rogue can cum
                                call Girl_Cumming(Girl)
                                if Situation == "shift" or "angry" in Girl.RecentActions:
                                        jump Kiss_After            
                        
                        #If you came
                        if Line == "came":
                                        if not Player.Semen:
                                                "You're pretty wiped, better stop for now."
                                        $ Line = 0
                                        jump Kiss_After                 
                     
            if Partner and Partner.Lust >= 100:
                    #Checks if partner could orgasm
                    call Girl_Cumming(Partner)            
            #End orgasm
               
            call Escalation(Girl) #sees if she wants to escalate things
            
            if Round == 10:        
                    call Sex_Basic_Dialog(Girl,10) #"You might want to wrap this up, it's getting late." 
            elif Round == 5:
                    call Sex_Basic_Dialog(Girl,5)   #"Seriously, it'll be time to stop soon."     
        
        #Round = 0 loop breaks
        $ Girl.FaceChange("bemused", 0)
        $ Line = 0    
        call Sex_Basic_Dialog(Girl,"done") #"Ok, [Girl.Petname], that's enough of that for now."
    
label Kiss_After:
        if Girl not in TotalGirls:
                $ Girl = Ch_Focus
        $ Girl.FaceChange("sexy") 
        
        $ Girl.Kissed += 1
        $ Girl.Action -=1
        $ Girl.Addictionrate += 2 if Girl.Addictionrate < 5 else 1 
        $ Girl.Addictionrate += 1 if "addictive" in Player.Traits else 0
        
        call Partner_Like(Girl,1) #raises other girl's like levels if watching
        
        if "kissing" not in Girl.RecentActions:
                if Girl.Love > 300:
                        $ Girl.Statup("Love", 60, 4)
                $ Girl.Statup("Love", 70, 1)
                $ Girl.RecentActions.append("kissing")                      
                $ Girl.DailyActions.append("kissing") 
         
        if Girl.Kissed > 10: 
                pass        
        elif Girl.Kissed == 10:
                $ Girl.FaceChange("smile", 1)    
                if Girl == RogueX: 
                        ch_r "You must really like my lips, huh?"  
                elif Girl == KittyX:      
                        ch_k "I could eat you up."         
                elif Girl == EmmaX:       
                        ch_e "This has been a pleasant surprise."            
                elif Girl == LauraX:
                        ch_l "I could do this every day."            
        elif Girl.Kissed == 5:
                if Girl == RogueX: 
                        ch_r "We're really making this a regular thing." 
                elif Girl == KittyX: 
                        ch_k "You're good at this. . ."               
                elif Girl == EmmaX:   
                        ch_e "You're surprisingly talented. . ."                 
                elif Girl == LauraX:
                        ch_l "You're really talented. . ." 
        elif Girl.Kissed == 1:    
            $ Girl.SEXP += 1 
            
        if not Situation and Girl.Kissed > 5 and Girl.Lust > 50 and ApprovalCheck(Girl, 950):
                $ Girl.FaceChange("sexy", 1)
                $ Girl.Brows = "sad"
                if Girl == RogueX: 
                        ch_r "You maybe want to try something more?"  
                elif Girl == KittyX:    
                        ch_k "Is that it?"             
                elif Girl == EmmaX:   
                        ch_e "You wouldn't be interested in something more? . ."                
                elif Girl == LauraX:
                        ch_l "Huh, that's all there is to it?"       
        $ Tempmod = 0  
        if Situation:
                call Sex_Basic_Dialog(Girl,"sitch") #"Mmm, so what else did you have in mind?"
        else:
                call expression Girl.Tag + "_Pos_Reset" 
        call Checkout
        return
# End Makeout / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Massage / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Massage(Girl=0,Current=0,Past=0,MCount=0):
        if Girl not in TotalGirls:
            $ Girl = Ch_Focus
        call Shift_Focus(Girl)
        $ Tempmod = 0    
        if "angry" in Girl.RecentActions:
            return    
            
        $ Approval = ApprovalCheck(Girl, 500, TabM = 1) # 95, 110, 125 -120(215)
        
        if Approval >= 2:             
                    $ Girl.FaceChange("bemused", 1)
                    if Girl.Forced:
                            $ Girl.FaceChange("sad")
                            $ Girl.Statup("Love", 20, -2, 1)
                            $ Girl.Statup("Obed", 90, 1)
                            $ Girl.Statup("Inbt", 60, 1)                
                    if Girl == RogueX:
                            ch_r "Ok [Girl.Petname], sure."   
                    elif Girl == KittyX:
                            ch_k "Sure, why not."   
                    elif Girl == EmmaX:
                            ch_e "I could use it, [Girl.Petname]."   
                    elif Girl == LauraX:        
                            ch_l "I guess I could use a rubdown."               
                    $ Girl.Statup("Love", 90, 1)
                    $ Girl.Statup("Inbt", 50, 3) 
                    jump Massage_Prep
            
        else:
            $ Girl.FaceChange("angry", 1)
            if "no massage" in Girl.RecentActions:  
                    if Girl == RogueX:
                            ch_r "Heh, I {i}just{/i} told you \"no,\" [Girl.Petname]."
                    elif Girl == KittyX:
                            ch_k "Come on, I {i}just{/i} told you \"no,\" [Girl.Petname]." 
                    elif Girl == EmmaX:
                            ch_e "I only {i}just{/i} refused you, [Girl.Petname]."
                    elif Girl == LauraX:
                            ch_l "I only {i}just{/i} refused you, [Girl.Petname]."
            elif "no massage" in Girl.DailyActions:   
                    if Girl == RogueX:
                            ch_r "I told you \"no,\" earlier [Girl.Petname]."
                    elif Girl == KittyX:  
                            ch_k "I already told you \"no.\""
                    elif Girl == EmmaX:
                            ch_e "I told you \"no\" earlier, [Girl.Petname]."
                    elif Girl == LauraX:    
                            ch_l "I told you \"no\" earlier, [Girl.Petname]."
            else:
                    $ Girl.FaceChange("bemused")
                    if Girl == RogueX:
                            ch_r "I don't know, not right now."   
                    elif Girl == KittyX:
                            ch_k "I don't know, not right now."  
                    elif Girl == EmmaX:
                            ch_e "I'm not interested at the moment, [Girl.Petname]."   
                    elif Girl == LauraX:
                            ch_l "I'm not interested at the moment, [Girl.Petname]."   
            menu:
                extend ""
                "Sorry, never mind." if "no massage" in Girl.DailyActions:
                        $ Girl.FaceChange("bemused")
                        if Girl == RogueX:
                                ch_r "Ok, no problem, [Girl.Petname]."
                        elif Girl == KittyX:
                                ch_k "It's cool, [Girl.Petname]." 
                        elif Girl == EmmaX:
                                ch_e "Don't concern yourself, [Girl.Petname]."  
                        elif Girl == LauraX:
                                ch_l "No worries."                
                        return
                "Maybe later?" if "no massage" not in Girl.DailyActions:
                        $ Girl.FaceChange("sexy")  
                        $ Girl.Statup("Love", 80, 1)
                        $ Girl.Statup("Inbt", 20, 1)
                        $ Girl.Statup("Obed", 20, 1)  
                        if Girl == RogueX:
                                ch_r "Sure, maybe."
                        elif Girl == KittyX:
                                ch_k "Yeah, maybe."
                        elif Girl == EmmaX:
                                ch_e "Perhaps."
                        elif Girl == LauraX:        
                                ch_l "Maybe?"
                        $ Girl.RecentActions.append("no massage")                      
                        $ Girl.DailyActions.append("no massage")            
                        return                
                "Come on, Please?":             
                    if Approval:
                        $ Girl.FaceChange("sexy")     
                        $ Girl.Statup("Obed", 90, 1)
                        $ Girl.Statup("Obed", 40, 2)
                        $ Girl.Statup("Inbt", 30, 2)
                        if Girl == RogueX:
                                ch_r "Well, if you're that desperate. . ."  
                        elif Girl == KittyX:
                                ch_k "I guess I could use some relaxation. . ."  
                        elif Girl == EmmaX:
                                ch_e "I do have some tension built up. . ."  
                        elif Girl == LauraX:           
                                ch_l "Ok, ok, I do have some knots. . ."
                        jump Massage_Prep
                    else:   
                        $ Girl.FaceChange("sexy") 
                        if Girl == RogueX:
                                ch_r "Heh, no thanks, [Girl.Petname]." 
                        elif Girl == KittyX: 
                                ch_k "Heh, sorry, [Girl.Petname]." 
                        else:
                                $ Girl.FaceChange("sly", Brows="confused") 
                                call AnyLine(Girl,"No.")
        
        if "no massage" in Girl.DailyActions:
                if Girl == RogueX:
                        ch_r "You're starting to skeeve me out, [Girl.Petname]."   
                elif Girl == KittyX:
                        ch_k "Um, get a clue, [Girl.Petname]."  
                elif Girl == EmmaX:
                        ch_e "I've made myself clear on this, [Girl.Petname]."
                elif Girl == LauraX:
                        ch_l "I've made myself clear on this, [Girl.Petname]."  
                $ Girl.RecentActions.append("angry")
                $ Girl.DailyActions.append("angry")   
        elif Girl.Forced:
                $ Girl.FaceChange("angry", 1)
                $ Girl.Statup("Lust", 60, 5)    
                $ Girl.Statup("Obed", 50, -2)   
                if Girl == RogueX:
                        ch_r "I don't even want you touching me."
                elif Girl == KittyX:        
                        ch_k "Even that's too much."
                elif Girl == EmmaX:   
                        ch_e "You'll have to keep your hands limber for yourself." 
                elif Girl == LauraX:
                        ch_l "You'll have to keep your hands limber for yourself."  
                $ Girl.RecentActions.append("angry")
                $ Girl.DailyActions.append("angry")   
        elif Taboo:
                $ Girl.FaceChange("angry", 1)    
                if Girl == RogueX:
                        ch_r "I don't want you touching me in public."  
                elif Girl == KittyX:
                        ch_k "Not[Girl.like]in public."  
                elif Girl == EmmaX:
                        ch_e "I can't been seen doing that with you."  
                elif Girl == LauraX: 
                        ch_l "I try to stay off the radar."     
        else:
                $ Girl.FaceChange("sexy") 
                $ Girl.Mouth = "sad"
                if Girl == RogueX:
                        ch_r "Seriously, no thanks, [Girl.Petname]."    
                elif Girl == KittyX:
                        ch_k "Seriously, no thank you!" 
                elif Girl == EmmaX:
                        ch_e "I really can't."    
                elif Girl == LauraX:  
                        ch_l "So not into it."                
        $ Girl.RecentActions.append("no massage")                      
        $ Girl.DailyActions.append("no massage") 
        $ Tempmod = 0    
        return
 
label Massage_Prep(Girl=Ch_Focus,Current=0,Past=0,MCount=0):
        call Top_Off(Girl,"massage")
        if "angry" in Girl.RecentActions:
                return    
        
label Massage_Cycle:    
        #Current is the current action, past is the previous action, MCount is progress along the character track
        
        $ Girl.RecentActions.append("massage")                      
        $ Girl.DailyActions.append("massage") 
        
        if Girl == RogueX:
                call Rogue_Doggy_Launch("massage")
                
        $ Trigger = "massage"
        
        while Round >= 10 and MCount < 10:  
                call Shift_Focus(Girl) 
                $ Girl.LustFace() 
                menu Massage_Choices:
                    "Where do you touch?"                
                    "Her Upper Body":
                        menu:
                            "Her Neck":
                                    $ Past = Current
                                    $ Current = "neck"
                            "Her Shoulders":
                                    $ Past = Current
                                    $ Current = "shoulders"
                            "Her Back":
                                    $ Past = Current
                                    $ Current = "back"
                            "Her Breasts":
                                    $ Past = Current
                                    $ Current = "breasts"
                            "Her Arms":
                                    $ Past = Current
                                    $ Current = "arms"
                            "Her Hands":
                                    $ Past = Current
                                    $ Current = "hands"
                            "Back":
                                    jump Massage_Choices
                    "Her Legs":     
                        menu:
                            "Her Hips":
                                    $ Past = Current
                                    $ Current = "hips"
                            "Her Ass":
                                    $ Past = Current
                                    $ Current = "ass"
                            "Her Pussy":
                                    $ Past = Current
                                    $ Current = "pussy"
                            "Her Thighs":
                                    $ Past = Current
                                    $ Current = "thighs"
                            "Her Calves":
                                    $ Past = Current
                                    $ Current = "calves"
                            "Her Feet":
                                    $ Past = Current
                                    $ Current = "feet"
                            "Back":
                                    jump Massage_Choices
                    "Her Neck" if Current in ("neck","shoulders","back"):
                            $ Past = Current
                            $ Current = "neck"
                    "Her Shoulders" if Current in ("neck","shoulders","back","arms"):
                            $ Past = Current
                            $ Current = "shoulders"
                    "Her Back" if Current in ("neck","shoulders","back","breasts","hips"):
                            $ Past = Current
                            $ Current = "back"
                    "Her Breasts" if Current in ("breasts","back"):
                            $ Past = Current
                            $ Current = "breasts"
                    "Her Arms" if Current in ("shoulders","arms","hands"):
                            $ Past = Current
                            $ Current = "arms"
                    "Her Hands" if Current in ("arms","hands"):     
                            $ Past = Current
                            $ Current = "hands"                  
                    "Her Hips" if Current in ("back","hips","ass","pussy","thighs"):
                            $ Past = Current
                            $ Current = "hips"
                    "Her Ass" if Current in ("back","hips","ass","pussy","thighs"):
                            $ Past = Current
                            $ Current = "ass"
                    "Her Pussy" if Current in ("hips","ass","pussy","thighs"):
                            $ Past = Current
                            $ Current = "pussy"
                    "Her Thighs" if Current in ("hips","ass","pussy","thighs","calves"):
                            $ Past = Current
                            $ Current = "thighs"
                    "Her Calves" if Current in ("thighs","calves","feet"):
                            $ Past = Current
                            $ Current = "calves"
                    "Her Feet" if Current in ("calves","feet"):
                            $ Past = Current
                            $ Current = "feet"       
                    "Her clothes":
                            call Girl_Undress(Girl)
                            jump Massage_Choices
                    "Stop":
                        jump Massage_After
                #end menu
                
                if Current == "neck":            
                        call expression Girl.Tag + "_Breasts_Launch" pass (0)
                        if Past in ("shoulders","back"):
                                $ Line = "You slide your hands toward " +Girl.Name+ "'s " +Current 
                                $ Check = 400
                        else:
                                $ Line = "You begin to massage " +Girl.Name+ "'s " +Current
                                $ Check = 500
                    
                        if Girl.MassageChart[MCount] == Current and ApprovalCheck(Girl, Check):
                                # really likes it     
                                $ Girl.Statup("Lust", 60, 2)
                                $ Girl.Statup("Lust", 90, 1)
                                if Past == Current:
                                        $ Girl.Statup("Lust", 90, 2)
                                        "You really dig into her neck muscles, and she lets out a long groan of pleasure."
                                else:
                                        "[Line]. She stretches out in obvious pleasure as the knots release."
                        #end neck
                        $ Girl.Addict -= 1
                elif Current == "shoulders":
                        call expression Girl.Tag + "_Breasts_Launch" pass (0)
                        if Past in ("back","neck","arms"):
                                $ Line = "You slide your hands toward " +Girl.Name+ "'s " +Current 
                                $ Check = 400
                        else:
                                $ Line = "You begin to massage " +Girl.Name+ "'s " +Current
                                $ Check = 500
                    
                        if Girl.MassageChart[MCount] == Current and ApprovalCheck(Girl, Check):
                                # really likes it     
                                $ Girl.Statup("Lust", 60, 2)
                                $ Girl.Statup("Lust", 90, 2)
                                if Past == Current:                                
                                        $ Girl.Statup("Lust", 90, 2)
                                        "You really dig into her shoulders, and she wriggles them and moans."
                                else:
                                        "[Line]. She stretches out in obvious pleasure as the knots release."
                        elif Past == Current:
                                $ Check = 600
                                $ Line = "You continue to massage " +Girl.Name+ "'s " +Current
                        #end shoulders   
                        if not Girl.Over:
                                $ Girl.Addict -= 2                 
                elif Current == "back":
                        call expression Girl.Tag + "_Breasts_Launch" pass (0)
                        if Past in ("neck","shoulders","breasts","hips"):
                                $ Line = "You slide your hands toward " +Girl.Name+ "'s " +Current 
                                $ Check = 400
                        else:
                                $ Line = "You begin to massage " +Girl.Name+ "'s " +Current
                                $ Check = 500
                    
                        if Girl.MassageChart[MCount] == Current and ApprovalCheck(Girl, Check):
                                # really likes it     
                                $ Girl.Statup("Lust", 60, 2)
                                $ Girl.Statup("Lust", 90, 2)
                                if Past == Current:
                                        $ Girl.Statup("Lust", 90, 2)
                                        "You really put the pressure into her spine, and she lets out a long groan of pleasure."
                                else:
                                        "[Line]. She moans as you hear her vertebrae stretch."
                        elif Past == Current:
                                $ Check = 600
                                $ Line = "You continue to massage " +Girl.Name+ "'s " +Current
                        #end back
                        if not Girl.Over:
                                $ Girl.Addict -= 1 
                        if not Girl.Chest:
                                $ Girl.Addict -= 1 
                elif Current == "breasts":
                        call expression Girl.Tag + "_Breasts_Launch" pass (0)
                        if Past == "back":
                                $ Line = "You slide your hands around and grasp " +Girl.Name+ "'s " +Current 
                                $ Check = 1000
                        else:
                                $ Line = "You move your hands to grab " +Girl.Name+ "'s " +Current
                                $ Check = 1050
                    
                        if Girl.MassageChart[MCount] == Current and ApprovalCheck(Girl, Check):
                                # really likes it     
                                $ Girl.Statup("Lust", 60, 1)
                                $ Girl.Statup("Lust", 90, 2)
                                $ Girl.Statup("Lust", 200, 3)
                                if Past == Current:
                                        $ Girl.Statup("Lust", 200, 2)
                                        "You knead her breasts firmly and she lets out a low moan."
                                else:
                                        "[Line]. Her nipples grow sharp in your palms."
                        elif Past == Current:
                                $ Check = 1050
                                $ Girl.Statup("Lust", 200, 2)
                                $ Line = "You continue to rub " +Girl.Name+ "'s " +Current
                        #end breasts
                        if not Girl.Over and not Girl.Chest:
                                $ Girl.Addict -= 2 
                elif Current == "arms":
                        call expression Girl.Tag + "_Breasts_Launch" pass (0)
                        if Past == "shoulders":
                                $ Line = "You slide your hands down " +Girl.Name+ "'s " +Current 
                                $ Check = 400
                        elif Past == "hands":
                                $ Line = "You slide your hands up " +Girl.Name+ "'s " +Current 
                                $ Check = 400
                        else:
                                $ Line = "You begin to massage " +Girl.Name+ "'s " +Current
                                $ Check = 500
                    
                        if Girl.MassageChart[MCount] == Current and ApprovalCheck(Girl, Check):
                                # really likes it     
                                $ Girl.Statup("Lust", 60, 2)
                                $ Girl.Statup("Lust", 90, 1)
                                if Past == Current:
                                        $ Girl.Statup("Lust", 90, 2)
                                        "You really dig into her triceps, and she seemed really knotted up."
                                else:
                                        "[Line]. Her hands flex involuntarily and she coos in pleasure."
                        elif Past == Current:
                                $ Check = 600
                                $ Line = "You continue to massage " +Girl.Name+ "'s " +Current
                        #end arms
                        if Girl.Over not in ("mesh top","pink top","jacket"):
                                $ Girl.Addict -= 1 
                elif Current == "hands": 
                        call expression Girl.Tag + "_Breasts_Launch" pass (0) 
                        if Past == "arms":
                                $ Line = "You slide your hands down and grasp " +Girl.Name+ "'s " +Current 
                                $ Check = 400
                        else:
                                $ Line = "You pick up " +Girl.Name+ "'s " +Current+ " and begin to massage them"
                                $ Check = 500
                    
                        if Girl.MassageChart[MCount] == Current and ApprovalCheck(Girl, Check):
                                # really likes it     
                                $ Girl.Statup("Lust", 70, 2)
                                if Past == Current:
                                        $ Girl.Statup("Lust", 70, 2)
                                        "You stretch each finger and rub along the joints. She lets out a small gasp."
                                else:
                                        "[Line]. Her fingers flex with pleasure."
                        elif Past == Current:
                                $ Check = 600
                                $ Line = "You continue to massage " +Girl.Name+ "'s " +Current
                        #end hands
                        $ Girl.Addict -= 1 
                elif Current == "hips":
                        call expression Girl.Tag + "_Pussy_Launch" pass (0)
                        if Past == "back":
                                $ Line = "You slide your hands down toward " +Girl.Name+ "'s " +Current 
                                $ Check = 400
                        elif Past in ("ass","pussy","thighs"):
                                $ Line = "You slide your hands up toward " +Girl.Name+ "'s " +Current 
                                $ Check = 400
                        else:
                                $ Line = "You begin to massage " +Girl.Name+ "'s " +Current
                                $ Check = 500
                    
                        if Girl.MassageChart[MCount] == Current and ApprovalCheck(Girl, Check):
                                # really likes it     
                                $ Girl.Statup("Lust", 60, 2)
                                $ Girl.Statup("Lust", 90, 1)
                                if Past == Current:
                                        "You really dig into her hips, and she lets out a long groan of pleasure."
                                else:
                                        "[Line]. Her back arches out in obvious pleasure as the knots release."
                        elif Past == Current:
                                $ Check = 600
                                $ Line = "You continue to massage " +Girl.Name+ "'s " +Current
                        #end hips
                        if not Girl.Legs and Girl.HoseNum() < 10:
                                $ Girl.Addict -= 1 
                elif Current == "ass":
                        call expression Girl.Tag + "_Pussy_Launch" pass (0)
                        if Past in ("back","hips"):
                                $ Line = "You slide your hands down toward " +Girl.Name+ "'s " +Current 
                                $ Check = 900
                        elif Past in ("pussy","thighs"):
                                $ Line = "You slide your hands up to " +Girl.Name+ "'s " +Current 
                                $ Check = 900
                        else:
                                $ Line = "You begin to massage " +Girl.Name+ "'s " +Current
                                $ Check = 950
                    
                        if Girl.MassageChart[MCount] == Current and ApprovalCheck(Girl, Check):
                                # really likes it     
                                $ Girl.Statup("Lust", 60, 2)
                                $ Girl.Statup("Lust", 90, 1)
                                $ Girl.Statup("Lust", 200, 3)
                                if Past == Current:
                                        $ Girl.Statup("Lust", 200, 2)
                                        "You move across her ass in a wavelike pattern as her back wriggles in pleasure."
                                else:
                                        "[Line]. Her muscles tighten and release as you squeeze them."
                        elif Past == Current:
                                $ Check = 950
                                $ Girl.Statup("Lust", 90, 2)
                                $ Line = "You continue to massage " +Girl.Name+ "'s " +Current
                        #end ass
                        if not Girl.Legs and not Girl.Panties and Girl.HoseNum() < 10:
                                $ Girl.Addict -= 2 
                elif Current == "pussy":
                        call expression Girl.Tag + "_Pussy_Launch" pass (0)
                        if Past in ("hips","ass"):
                                $ Line = "You slide your hands around toward " +Girl.Name+ "'s " +Current 
                                $ Check = 1200
                        elif Past == "thighs":
                                $ Line = "You slide your hands up and into " +Girl.Name+ "'s groin"
                                $ Check = 1100
                        else:
                                $ Line = "You begin to massage " +Girl.Name+ "'s " +Current
                                $ Check = 1200
                    
                        if Girl.MassageChart[MCount] == Current and ApprovalCheck(Girl, Check):
                                # really likes it     
                                $ Girl.Statup("Lust", 60, 2)
                                $ Girl.Statup("Lust", 90, 2)
                                $ Girl.Statup("Lust", 200, 3)
                                if Past == Current:
                                        $ Girl.Statup("Lust", 200, 5)
                                        "You draw your thumbs across her clit and she shudders with pleasure."
                                else:
                                        "[Line]. Her back arches with pleasure and she releases a soft moan."
                        elif Past == Current:
                                $ Check = 1200
                                $ Girl.Statup("Lust", 200, 3)
                                $ Line = "You continue to rub " +Girl.Name+ "'s " +Current
                        #end pussy
                        if not Girl.Legs and not Girl.Panties and Girl.HoseNum() < 10:
                                $ Girl.Addict -= 3 
                elif Current == "thighs":
                        call expression Girl.Tag + "_Pussy_Launch" pass (0)
                        if Past == "calves":
                                $ Line = "You slide your hands up toward " +Girl.Name+ "'s " +Current 
                                $ Check = 500
                        elif Past in ("hips","ass","pussy"):
                                $ Line = "You slide your hands down toward " +Girl.Name+ "'s " +Current 
                                $ Check = 400
                        else:
                                $ Line = "You begin to massage " +Girl.Name+ "'s " +Current
                                $ Check = 600
                    
                        if Girl.MassageChart[MCount] == Current and ApprovalCheck(Girl, Check):
                                # really likes it     
                                $ Girl.Statup("Lust", 60, 2)
                                $ Girl.Statup("Lust", 90, 1)
                                if Past == Current:
                                        $ Girl.Statup("Lust", 60, 1)
                                        "You really put some pressure into stretching out her quads, and she groans in pleasure."
                                else:
                                        "[Line]. Her legs stretch out with clear satisfaction."
                        elif Past == Current:
                                $ Check = 600
                                $ Line = "You continue to massage " +Girl.Name+ "'s " +Current
                        #end thighs
                        if not Girl.PantsNum() <= 6 and Girl.HoseNum() < 10:
                                $ Girl.Addict -= 1 
                elif Current == "calves":
                        call expression Girl.Tag + "_Pos_Reset" pass (0)
                        if Past == "feet":
                                $ Line = "You slide your hands up and stroke " +Girl.Name+ "'s " +Current 
                                $ Check = 400
                        elif Past == "thighs":
                                $ Line = "You slide your hands up to grab " +Girl.Name+ "'s " +Current 
                                $ Check = 400
                        else:
                                $ Line = "You begin to massage " +Girl.Name+ "'s " +Current
                                $ Check = 500
                    
                        if Girl.MassageChart[MCount] == Current and ApprovalCheck(Girl, Check):
                                # really likes it     
                                $ Girl.Statup("Lust", 60, 2)
                                $ Girl.Statup("Lust", 90, 1)
                                if Past == Current:
                                        $ Girl.Statup("Lust", 60, 1)
                                        "You stretch her ankles back and forth, as you work out her tensed calves."
                                else:
                                        "[Line]. She flexes her toes in satisfaction as her muscles stretch out."
                        elif Past == Current:
                                $ Check = 600
                                $ Line = "You continue to massage " +Girl.Name+ "'s " +Current
                        #end calves
                        if not Girl.PantsNum() <= 6 and Girl.HoseNum() < 10:
                                $ Girl.Addict -= 1 
                elif Current == "feet":    
                        call expression Girl.Tag + "_Pos_Reset" pass (0)
                        if Past == "calves":
                                $ Line = "You slide your hands down and grasp " +Girl.Name+ "'s " +Current 
                                $ Check = 400
                        else:
                                $ Line = "You begin to rub " +Girl.Name+ "'s " +Current
                                $ Check = 600
                    
                        if Girl.MassageChart[MCount] == Current and ApprovalCheck(Girl, Check):
                                # really likes it     
                                $ Girl.Statup("Lust", 60, 2)
                                $ Girl.Statup("Lust", 90, 1)
                                if Past == Current:
                                        $ Girl.Statup("Lust", 90, 2)
                                        "You press your thumbs deeply into her arches, and her toes curl around them."
                                else:
                                        "[Line]. She stretches her toes and lets out a soft moan."
                        elif Past == Current:
                                $ Check = 600
                                $ Line = "You continue to rub " +Girl.Name+ "'s " +Current
                        #end feet   
                        if Girl.Acc != "boots" and Girl.HoseNum() < 10:
                                $ Girl.Addict -= 2 
                # end primary checks
                
                # reaction checks
                if Girl.MassageChart[MCount] == Current and ApprovalCheck(Girl, Check):
                        # really likes it, we've covered this above
                        pass
                elif ApprovalCheck(Girl, Check):
                        #kinda likes it
                        $ Line = Line + renpy.random.choice([". She wriggles a little in contentment.", 
                                ". She lets out a little hum.",
                                ". She really seems to enjoy it.",
                                ". She seems comfortable with this.",
                                ". She lets out a small purr of pleasure."])  
                        $ Girl.Statup("Lust", 60, 2)
                        $ Girl.Statup("Lust", 90, 1)
                        "[Line]"
                        if Current == Past and Current in ("breasts","ass","pussy"):
                                #want to get a better grip on that?
                                #jump to the fondling activity
                                if Current == "breasts":                                
                                        call expression Girl.Tag + "_FB_Prep"
                                elif Current == "ass":        
                                        call expression Girl.Tag + "_FA_Prep"
                                elif Current == "pussy":        
                                        call expression Girl.Tag + "_FP_Prep"
                                return
                elif ApprovalCheck(Girl, Check-200) or "massagefail" in Girl.RecentActions:
                        # dislikes it                            
                        $ Line = Line + renpy.random.choice([". She stiffens a bit, but settles back into it.", 
                                ". She doesn't seem to enjoy it.",
                                ". She doesn't seem comfortable with this.",
                                ". She lets out a small tsk of irritation."]) 
                        $ Girl.Statup("Lust", 60, -1)
                        $ Girl.Statup("Lust", 90, -2)
                        "[Line]"            
                        if Current == Past and Current in ("breasts","ass","pussy"):
                                #could you cut that out?
                                call Massage_BadEnd
                                menu:
                                    extend ""
                                    "Sorry, yeah":
                                            "You pull your hands back."
                                            $ Past = Current
                                            $ Current = 0
                                    "I'm enjoying this":
                                            $ Girl.AddWord(1,"massagefail")
                                            jump Massage_BadEnd
                        $ Girl.AddWord(1,"massagefail")
                else:
                        # hates it
                        "[Line]. She stiffens and sits up."
                        $ Girl.AddWord(1,"massagefail")
                        jump Massage_BadEnd
                        
                $ Round -= 6                
                if Girl.MassageChart[MCount] == Current:
                        # advances progress along the track so long as you've hit the target
                        if MCount == 2:
                                "You feel like you're on to something here, whatever you're doing seems to be working."
                        elif MCount == 7:
                                "She really seems to be getting into it, she's practically vibrating."
                        $ MCount += 1           
                #End loop
label Massage_After:                    
        call expression Girl.Tag + "_Pos_Reset" pass (0)
        if MCount >= 3:
                $ Girl.Statup("Love", 90, 1)
                $ Girl.Statup("Love", 50, 2)
                $ Girl.Statup("Obed", 30, 2)
                
        $ Girl.Massage += 1  
        $ Girl.Action -=1
        $ Girl.Addictionrate += 2 if Girl.Addictionrate < 5 else Girl.Addictionrate
        if "addictive" in Player.Traits:
                $ Girl.Addictionrate += 1   
            
        if MCount == 10 and not Girl.Forced:
                #you bowled her over
                if Girl == RogueX:
                        ch_r "Hnnnng, that was ama-zing, [Girl.Petname]!" 
                        ch_r "Did you have anything else in mind?"
                elif Girl == KittyX:    
                        ch_k "Wowwww, [Girl.Petname], that was fantastic!"
                        ch_k "What do you have for round two?"
                elif Girl == EmmaX:
                        ch_e ". . ."
                        ch_e "Incredible, [Girl.Petname]." 
                        ch_e "Did you want to. . . continue?"
                elif Girl == LauraX: 
                        ch_l "Nnnnn, [Girl.Petname], that was great!" 
                        ch_l "That felt amazing, did you have anything else in mind?"
        elif Girl.Massage == 1:
                #first time
                if Girl == RogueX:
                        ch_r "That was very relaxing, [Girl.Petname]." 
                elif Girl == KittyX:    
                        ch_k "That was niiiiice, [Girl.Petname]." 
                elif Girl == EmmaX:
                        ch_e "That was very. . . pleasant, [Girl.Petname]."  
                elif Girl == LauraX: 
                        ch_l "Think that worked out some. . . kinks, [Girl.Petname]."   
        else:
                #any other time
                if Girl == RogueX:
                        ch_r "I do enjoy a nice massage, [Girl.Petname]." 
                elif Girl == KittyX:    
                        ch_k "Hmm, I enjoyed that one, [Girl.Petname]." 
                elif Girl == EmmaX:
                        ch_e "That was very. . . pleasant, [Girl.Petname]."  
                elif Girl == LauraX: 
                        ch_l "Thanks for that one, [Girl.Petname]."   
        $ Girl.Statup("Love", 90, int(MCount/2)) #raises love by half your track progress
        $ Tempmod = 0  
        call Checkout
        return

label Massage_BadEnd: 
        #if you fucked up. . .
        if "massagefail" in Girl.RecentActions:
                #bad finale
                $ Girl.Massage += 1  
                $ Girl.Action -=1
                $ Girl.Addictionrate += 2 if Girl.Addictionrate < 5 else Girl.Addictionrate
                if "addictive" in Player.Traits:
                        $ Girl.Addictionrate += 1   
                if Girl == RogueX:
                        ch_r "Ok, enough out of you, [Girl.Petname]." 
                elif Girl == KittyX:    
                        ch_k "Bad touch!"
                elif Girl == EmmaX:
                        ch_e "That will be enough of that."
                elif Girl == LauraX:
                        ch_l "Ok, you're benched." 
                $ Tempmod = 0  
                call Checkout
        elif Current == "breasts":
                if Girl == RogueX:
                        ch_r "I think you should probably watch your hands there, [Girl.Petname]." 
                elif Girl == KittyX:    
                        ch_k "Hey! Um, stay away from my. . . breasts."
                elif Girl == EmmaX:
                        ch_e "[Girl.Petname]! I contain your enthusiasm!"
                elif Girl == LauraX:
                        ch_l "Hey. I thought this was about me, not you."
        elif Current == "ass":
                if Girl == RogueX:
                        ch_r "You might want to keep things above the belt, [Girl.Petname]." 
                elif Girl == KittyX:  
                        ch_k "Hey[Girl.like]keep your hands off my butt!"
                elif Girl == EmmaX:
                        ch_e "[Girl.Petname]! I'd appreciate you not fondling my rear?"
                elif Girl == LauraX:
                        ch_l "I don't really need my ass worked on right now."
        elif Current == "pussy":
                if Girl == RogueX:
                        ch_r "Whoa there, [Girl.Petname]! Keep your hands out of there!" 
                elif Girl == KittyX:    
                        ch_r "Whoa! I know my name is \"Kitty\" and all, but that's not an invitation!"
                elif Girl == EmmaX:
                        ch_e "[Girl.Petname]! Buy a girl a drink first. Or another, at least."
                elif Girl == LauraX:
                        ch_l "I'll let you know when I need -that- massaged."
        else:
                if Girl == RogueX:
                        ch_r "I think you should probably watch your hands there, [Girl.Petname]." 
                elif Girl == KittyX:    
                        ch_k "Ooh, not there."
                elif Girl == EmmaX:
                        ch_e "[Girl.Petname]! I expect you to remain more professional than that."
                elif Girl == LauraX:
                        ch_l "You should probably avoid that area right now." 
        return
                                

# end Massage / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# start Strip Tease / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#start Dancing/Stripping / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 

label Group_Strip(Girl=0,Tempmod = Tempmod,TempmodP=[0,0],BO=[]): #@nee Tempmod0=0,Tempmod1=0
        #Note, this event would break during a date, since it manipulates Adjacent. Perhaps use unique list?
        $ Present = []
        $ BO = TotalGirls[:]  
        while BO:   
                if BO[0].Loc == bg_current:
                        $ Present.append(BO[0])  
                $ BO.remove(BO[0])
                    
        if not Present:
                "Nobody's here."
                "You dance alone."
                return    
                  
        while len(Present) > 2:  
                #culls out extra members
                call Remove_Girl(Present[2])
    #            $ Present.remove(Present[2])
                    
        if len(Present) == 2:                    
            $ renpy.random.shuffle(Present)
            if Girl and Present[0] != Girl:
                    $ Party.reverse()  
            elif ApprovalCheck(Present[0],Check=1) <= ApprovalCheck(Present[1],Check=1):
                    # If second one likes you more, pick her
                    $ Present.reverse()   
        
        call Shift_Focus(Present[0])
        
        $ Round -= 5 if Round > 5 else (Round-1)
        call Set_The_Scene(1,0,0,0)
            
        $ Present[0].FaceChange("sexy",1)  
        if len(Present) >= 2:
                if Present[1] in TotalGirls:
                        $ Present[1].FaceChange("sexy",1)  
                else:
                        $ Present.remove(Present[1]) 
        
        $ Cnt = len(Present) #max 2
        while Cnt:
            $ Cnt -= 1 #max 1
            if Girl == EmmaX and "classcaught" in EmmaX.RecentActions and AloneCheck(EmmaX):
                        #skip this step if during classcaught sequence
                        pass
            elif not ApprovalCheck(Present[Cnt], 600, TabM = 1,Alt=[[EmmaX],(650+Taboo*10)]) or (Present[Cnt] == EmmaX and Taboo and "taboo" not in EmmaX.History):
                    if not ApprovalCheck(Present[Cnt], 400):
                        if Present[Cnt] == RogueX:
                                ch_r "I'm just some sort'a gogo dancer now?"
                        elif Present[Cnt] == KittyX:
                                ch_k "Like I would just dance for you?"
                        elif Present[Cnt] == EmmaX:
                                ch_e "Oh, you think I'll dance to your tune?"
                        elif Present[Cnt] == LauraX:
                                ch_l "I don't dance."                        
                    elif Taboo:
                        if Present[Cnt] == RogueX:
                                ch_r "I don't think this is the best place for dance'n."
                        elif Present[Cnt] == KittyX:
                                ch_k "I don't know, this really isn't a good place for it?"   
                        elif Present[Cnt] == EmmaX:
                                ch_e "You must be joking. Here?"   
                        elif Present[Cnt] == LauraX:
                                if ApprovalCheck(LauraX, 600, TabM = 0):    #should add a second Laura, then the first gets removed.
                                        $ Present.append(LauraX)            #This restores the "taboo is irrelevant to her" state
                                else:
                                        ch_l "I don't feel like it." 
                    else:
                        if Present[Cnt] == RogueX:
                                ch_r "I dont feel it right now."  
                        elif Present[Cnt] == KittyX:
                                ch_k "I don't know, I don't really feel like dancing right now."
                        elif Present[Cnt] == EmmaX:
                                ch_e "I don't really feel like dancing at the moment."  
                        elif Present[Cnt] == LauraX:
                                ch_l "I don't feel like it."  
                    $ Present.remove(Present[Cnt])
                                      
        if not Present:
                return
        
        if EmmaX.Loc == bg_current and EmmaX not in Present:
                #If Emma is here, but does not agree to this,
                if "classcaught" not in EmmaX.History:
                        if EmmaX.Loc == EmmaX.Home:
                                #if it's her room. . .
                                ch_e "If the two of you would like to dance, please do it elsewhere."
                                $ Present = []
                                return
                        else:
                                ch_e "I should really be going." 
                                call Remove_Girl(EmmaX)
        
        if "stripping" in Present[0].DailyActions and ApprovalCheck(Present[0], 500, TabM = 3):
                $ Line = renpy.random.choice(["You liked the show earlier?",       
                    "Didn't get enough earlier?",
                    "You're going to wear me out."]) 
        else:
                $ Line = renpy.random.choice(["Ok, that sounds fun.",       
                    "I could get into that.",
                    "Yeah, ok."]) 
                
        call AnyLine(Present[0],Line)   
        $ Line = 0
        
        call AllReset("All")
        
        
        $ Cnt = len(Present) #max 2
        while Cnt:
                $ Cnt -= 1 #max 1
                if Present[Cnt] == RogueX:
                            show Rogue_Sprite at Girl_Dance1(RogueX)
                elif Present[Cnt] == KittyX:
                            show Kitty_Sprite at Girl_Dance1(KittyX)
                elif Present[Cnt] == EmmaX:
                            show Emma_Sprite at Girl_Dance1(EmmaX)
                elif Present[Cnt] == LauraX:
                            show Laura_Sprite at Girl_Dance1(LauraX)
                $ Present[Cnt].RecentActions.append("stripping")                      
                $ Present[Cnt].DailyActions.append("stripping") 
                $ Present[Cnt].Strip += 1 
                $ Present[Cnt].Action -= 1    
                $ TempmodP[Cnt] = Tempmod
                if Present[Cnt].SeenChest or Present[Cnt].SeenPussy:              
                    #You've seen her tits.
                    $ TempmodP[Cnt] += 20
                if Present[Cnt].SeenPanties:                           
                    #You've seen her panties.
                    $ TempmodP[Cnt] += 5
                if "exhibitionist" in Present[Cnt].Traits:
                    $ TempmodP[Cnt] += (4*Taboo)
                if ("dating" in Present[Cnt].Traits or "sex friend" in Present[Cnt].Petnames or Present[Cnt] in Player.Harem) and not Taboo:
                    $ TempmodP[Cnt] += 15
                elif "ex" in Present[Cnt].Traits:
                    $ TempmodP[Cnt] -= 40 
                elif Present[Cnt].ForcedCount and not Present[Cnt].Forced:
                    $ TempmodP[Cnt] -= 5 * Present[Cnt].ForcedCount  
                        
        if len(Present) >= 2:
                "They start to dance."
                $ Partner = Present[1]
                $ Count2 = 1
        else:
                "She starts to dance." 
                $ Count2 = 0
                $ Partner = 0
        
                      
        if Girl == EmmaX and "classcaught" in EmmaX.RecentActions and AloneCheck(EmmaX):
                #skip this step if during classcaught sequence
                $ Count = 0
                jump Group_Stripping
                
        #this portion adds back in girls who dropped out, but sets their "stop" flag.
        $ BO = TotalGirls[:]  
        while BO:   
                if BO[0].Loc == bg_current and BO[0] not in Present:
                        $ Present.append(BO[0])
                        if "stopdancing" not in BO[0].RecentActions:
                                $ BO[0].RecentActions.append("stopdancing")
                $ BO.remove(BO[0])
                
        $ Tempmod = TempmodP[0]
        $ Trigger = "strip"
        $ Count = 1
        
        while Count and Round >=10:
                #Loops endlessly until you do something.
                $ Round -= 2 if Round > 2 else Round
                if len(Present) >= 2:      
                    $ Present[0].GLG(Present[1],600,1,1)      
                    $ Present[1].GLG(Present[0],600,1,1)
                menu:
                    "Continue":
                            pass
                    "Would you kindly take off some clothes?":
                            #add checks here
                            call AnyLine(Present[0],"Hmm?")  
                            $ Count = 0
                    "Stop":
                            jump Group_Strip_End
                    
        
        if EmmaX.Loc == bg_current and len(Present) >= 2:
                #If Emma is here, but does not agree to this,
                if "classcaught" not in EmmaX.History or "three" not in EmmaX.History or (Taboo and "taboo" not in EmmaX.History):
                    if EmmaX.Loc == "bg emma":
                            #if it's her room. . .
                            ch_e "If the two of you would like to get indecent, please do it elsewhere."
                            $ Present = []
                            return
                    else:
                            ch_e "I should really be going." 
                            call Remove_Girl(EmmaX)
        
label Group_Stripping:    
        while Round >= 10 and Present: 
            $ Round -= 2 if Round > 2 else Round
            
            if Present[Count] != Ch_Focus:
                    call Shift_Focus(Present[Count])
                    
            call Girl_Stripping(Present[Count])
            
            if not Present or not Present[Count]:
                    jump Group_Strip_End
            if "stopdancing" in Present[Count].RecentActions: 
                    #if she's just standing around, cut back to the other girl 
                    if len(Present) >= 2 and "stopdancing" in Present[0].RecentActions and "stopdancing" in Present[1].RecentActions:
                            jump Group_Strip_End  
                    
            $ Trigger = "strip"
            
            if not Present:
                    #If everyone leaves, quit out
                    jump Group_Strip_End
                    
            if len(Present) >= 2:     
                $ Present[Count].GLG(Partner,800,2,1) 
                $ Present[Count2].GLG(Present[Count],800,2,1) 
                                
            if len(Present) >= 2:
                    # Flips the numbers if in a group
                    # Count starts at 0
                    if Count == 0:
                        $ Count = 1
                        $ Count2 = 0
                        $ TempmodP[1] = Tempmod
                        $ Tempmod = TempmodP[0]
                    elif Count == 1:
                        $ Count = 0
                        $ Count2 = 1
                        $ TempmodP[0] = Tempmod
                        $ Tempmod = TempmodP[1]                
                    call Shift_Focus(Partner)
    #                $ Partner = Present[Count2]
                    
                    call Activity_Check(Ch_Focus,Partner)                
                                        
            if len(Present) < 2:
                    #Plays if only one girl is dancing
                    $ Tempmod = TempmodP[Count]           
                    $ Count = 0
                    $ Count2 = 0
                    $ Partner = 0   
                    
                    call Activity_Check(Ch_Focus,Partner)
                     
                    if not Present or "stopdancing" in Present[0].RecentActions: 
                            jump Group_Strip_End   
            #ends loop
        if Present and Round <=15:        
                call AnyLine(Present[0],"It's getting late, we should probably take a break.") 
       
label Group_Strip_End:  
        #add like-ups here. . .
        if Present:
                $ Present[0].DrainWord("stopdancing",1,0,0) 
                $ Present[0].DrainWord("keepdancing",1,0,0)        
        if len(Present) >= 2:
                $ Present[1].DrainWord("stopdancing",1,0,0) 
                $ Present[1].DrainWord("keepdancing",1,0,0)
                    
        call Set_The_Scene(1,0,0,0)    
        $ Count = 0
        $ Count2 = 0
    #    $ renpy.pop_call()
        return
    
#end Dancing/Stripping / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 


label Girl_Stripping(Girl=0): 
        #This gets called by Group_Stripping, and returns there at the end. 
        if "stopdancing" in Girl.RecentActions: 
                #if she's just standing around, cut back to the other girl 
                return
        
        $ Girl.ArmPose = 2
        $ Girl.LustFace(1) #sets her lusty face          
        if "keepdancing" not in Girl.RecentActions:  
                # if Count isn't 2, it loops. 
                if Girl.Over and Girl.Chest and (Girl.Panties or Girl.Legs or Girl.HoseNum() >= 10):          
                    #will she lose the overshirt when she's dressed under?
                    if ApprovalCheck(Girl, 750, TabM = 3):
                            $ Girl.Statup("Obed", 50, 1)
                            $ Girl.Statup("Inbt", 25, 1)                 
                            $ Player.Statup("Focus", 60, 3)
                            $ Line = Girl.Over                
                            $ Girl.Over = 0  
                            if Girl == KittyX:                   
                                    "She drops her shoulders and her [Line] falls to the floor." 
                            else:
                                    "She pulls her [Line] over her head and throws it behind her."  
                    else:
                            jump Strip_Ultimatum
                
                elif Girl.Legs and (Girl.Panties or Girl.HoseNum() >= 10):                            
                    #will she lose the pants/skirt if she has panties on?
                    if ApprovalCheck(Girl, 1200, TabM = 3) or (Girl.SeenPanties and ApprovalCheck(Girl, 900, TabM = 3) and not Taboo):
                            $ Girl.Statup("Lust", 50, 5)                
                            $ Girl.Statup("Obed", 50, 1)
                            $ Girl.Statup("Inbt", 30, 1)                
                            $ Player.Statup("Focus", 60, 5)
                            $ Line = Girl.Legs         
                            $ Girl.Legs = 0      
                            if Girl == KittyX:                   
                                    "Her [Line] slide through her legs until they're only on her toes, before she kicks them to the floor." 
                            else:
                                    "She unzips and pulls down her [Line], dropping them to the floor."   
                            if not Girl.SeenPanties:
                                    $ Girl.Statup("Obed", 50, 2)                              
                                    $ Girl.Statup("Obed", 200, 3)
                                    $ Girl.Statup("Inbt", 50, 3)
                                    $ Girl.Statup("Inbt", 200, 2)
                                    $ Girl.SeenPanties = 1                
                    else:
                            jump Strip_Ultimatum          
                        
                elif Girl.Hose:  
                    # Will she lose the hose?
                    if Girl.HoseNum() >= 10:
                            if ApprovalCheck(Girl, 1200, TabM = 3):
                                    $ Girl.Statup("Lust", 50, 6)
                                    $ Player.Statup("Focus", 60, 6)
                            else:    
                                    jump Strip_Ultimatum
                                
                    elif Girl.HoseNum() >= 6 and ApprovalCheck(Girl, 1200, TabM = 3):
                            if ApprovalCheck(Girl, 1200, TabM = 3):
                                $ Girl.Statup("Lust", 50, 4)
                                $ Player.Statup("Focus", 60, 4)
                            else:    
                                jump Strip_Ultimatum
                    else:
                            $ Player.Statup("Focus", 60, 3)
                    $ Line = Girl.Hose
                    $ Girl.Hose = 0
                    if Girl == KittyX:                   
                            "Her [Line] slide down off her legs, leaving them in a small pile."   
                    else:
                            "She rolls the [Line] down off her legs, leaving them in a small pile." 
                    call expression Girl.Tag + "_First_Bottomless" pass (1)     
                    
                elif Girl.Over and not Girl.Chest and (Girl.Panties or Girl.HoseNum() >= 10):      
                    #will she lose the top when she's topless with panties?        
                    if ApprovalCheck(Girl, 1250, TabM = 3) or (Girl.SeenChest and ApprovalCheck(Girl, 1000, TabM = 3) and not Taboo):
                            $ Girl.Statup("Lust", 60, 5)                
                            $ Girl.Statup("Obed", 50, 2)
                            $ Girl.Statup("Inbt", 50, 10)   
                            $ Player.Statup("Focus", 80, 15)                     
                            $ Line = Girl.Over                
                            $ Girl.Over = 0                     
                            if not Girl.SeenChest:
                                    $ Girl.FaceChange("bemused", 1)
                                    $ Girl.Statup("Obed", 50, 3)                              
                                    $ Girl.Statup("Obed", 200, 4)
                                    $ Girl.Statup("Inbt", 50, 3)
                                    $ Girl.Statup("Inbt", 200, 3) 
                                    if Girl == KittyX:                   
                                            "She hesitantly glances your way, and then with tug her [Line] passes through her, tossing it to the ground." 
                                    else:
                                            "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."   
                                    call expression Girl.Tag + "_First_Topless" pass (1)       
                            else:      
                                if Girl == KittyX:                   
                                        "She drops her shoulders and her [Line] falls to the floor." 
                                else:          
                                        "She pulls her [Line] over her head, tossing it to the ground."   
                    else:
                            jump Strip_Ultimatum
                    
                elif Girl.Chest and not Girl.Over:                                    
                    # Will she lose the bra?
                    if ApprovalCheck(Girl, 1250, TabM = 3) or (Girl.SeenChest and ApprovalCheck(Girl, 1000, TabM = 3) and not Taboo):
                            $ Girl.Statup("Lust", 60, 5)                
                            $ Girl.Statup("Obed", 50, 2)
                            $ Girl.Statup("Inbt", 50, 1)
                            $ Player.Statup("Focus", 80, 15) 
                            $ Line = Girl.Chest                
                            $ Girl.Chest = 0                     
                            if not Girl.SeenChest:
                                    $ Girl.FaceChange("bemused", 1)
                                    if Girl == KittyX:                   
                                            "She hesitantly glances your way, and then with a shrug pulls her [Line] through herself, tossing it to the ground."
                                    else:
                                            "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                                    $ Girl.Statup("Obed", 50, 3)                              
                                    $ Girl.Statup("Obed", 200, 4)
                                    $ Girl.Statup("Inbt", 50, 3)
                                    $ Girl.Statup("Inbt", 200, 3)    
                                    call expression Girl.Tag + "_First_Topless" pass (1) 
                            else:
                                    $ Girl.FaceChange("sexy")
                                    if Girl == KittyX:                   
                                            "She pulls her [Line] through herself, tossing it to the ground."
                                    else:
                                            "She pulls her [Line] over her head, tossing it to the ground."  
                    else:
                            jump Strip_Ultimatum
                
                elif Girl.Legs:                                                       
                    #will she lose the pants/skirt if she has no panties on?
                    if ApprovalCheck(Girl, 1350, TabM = 3) or (Girl.SeenPussy and ApprovalCheck(Girl, 1100, TabM = 3) and not Taboo):
                            $ Girl.Statup("Lust", 75, 10)  
                            $ Line = Girl.Legs                
                            $ Girl.Legs = 0       
                            if not Girl.SeenPussy:
                                    $ Girl.Statup("Obed", 60, 3)
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Inbt", 50, 4)
                                    $ Girl.Statup("Inbt", 200, 4)  
                                    if Girl == KittyX:                   
                                            "She shyly looks up at you, and then slowly lets her [Line] slide to the floor." 
                                    elif Girl in (EmmaX,LauraX):
                                            "She hesitantly looks up at you, and then slowly unzips and pulls down her [Line], dropping them to the floor."    
                                    else:
                                            "She shyly looks up at you, and then slowly unzips and pulls down her [Line], dropping them to the floor."    
                                    call expression Girl.Tag + "_First_Bottomless" pass (1) 
                            else:                            
                                    $ Girl.Statup("Obed", 50, 1)                              
                                    $ Girl.Statup("Obed", 75, 1)
                                    if Girl == KittyX:                   
                                            "She lets her [Line] pass through her legs, dropping them to the floor."  
                                    else:
                                            "She unzips and pulls down her [Line], dropping them to the floor."   
                                    $ Girl.Statup("Inbt", 70, 2)       
                            $ Player.Statup("Focus", 85, 15)
                    else:
                            jump Strip_Ultimatum
                    
                elif Girl.Over and not Girl.Panties:                                        
                    #will she lose the overshirt when she's bottomless under?
                    if ApprovalCheck(Girl, 1350, TabM = 3) or (Girl.SeenPussy and ApprovalCheck(Girl, 1100, TabM = 3) and not Taboo):                  
                            $ Line = Girl.Over                
                            $ Girl.Over = 0                                 
                            if not Girl.SeenPussy:                
                                    $ Girl.Statup("Obed", 60, 3)                              
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Inbt", 50, 4)
                                    $ Girl.Statup("Inbt", 200, 4) 
                                    if Girl == KittyX:                   
                                            "She hesitantly glances your way, and then with a tug pulls her [Line] through herself, tossing it to the ground."
                                    else:
                                            "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                                    call expression Girl.Tag + "_First_Bottomless" pass (1) 
                            else:
                                if Girl == KittyX:                   
                                        "She drops her shoulders and her [Line] falls to the floor." 
                                else:
                                        "She pulls her [Line] over her head, tossing it to the ground."  
                                
                            if not Girl.Chest or Girl.Uptop:
                                if not Girl.SeenChest:                
                                        $ Girl.Statup("Obed", 50, 3)  
                                        $ Girl.Statup("Inbt", 50, 3)
                                        call expression Girl.Tag + "_First_Topless" pass (1)
                                else:
                                        $ Girl.Statup("Lust", 60, 15)                
                                        $ Girl.Statup("Obed", 50, 3)                              
                                        $ Girl.Statup("Obed", 75, 1)
                                        $ Girl.Statup("Inbt", 50, 3)
                            else:
                                    $ Girl.Statup("Lust", 75, 10)                
                                    $ Girl.Statup("Obed", 50, 1)                              
                                    $ Girl.Statup("Obed", 75, 1)
                                    $ Girl.Statup("Inbt", 70, 2)                
                            $ Player.Statup("Focus", 85, 15)    
                    else:
                            jump Strip_Ultimatum
                
                elif Girl.Chest:                                                               
                    # Will she go topless?
                    if ApprovalCheck(Girl, 1250, TabM = 3) or (Girl.SeenChest and ApprovalCheck(Girl, 1100, TabM = 3) and not Taboo):
                            $ Girl.Statup("Lust", 60, 5) 
                            $ Line = Girl.Chest                
                            $ Girl.Chest = 0                     
                            if not Girl.SeenChest:
                                    $ Girl.Statup("Obed", 50, 3)                              
                                    $ Girl.Statup("Obed", 200, 4)               
                                    $ Girl.Statup("Inbt", 50, 3)
                                    $ Girl.Statup("Inbt", 200, 3)  
                                    if Girl == KittyX:                   
                                            "She hesitantly glances your way, and then with a tug pulls her [Line] through herself, tossing it to the ground." 
                                    else:
                                            "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."   
                                    call expression Girl.Tag + "_First_Topless" pass (1)
                            else:                
                                    $ Girl.Statup("Obed", 50, 2)
                                    if Girl == KittyX:                   
                                            "She drops her shoulders and her [Line] falls to the floor." 
                                    else:
                                            "She pulls her [Line] over her head, tossing it to the ground."  
                                    $ Girl.Statup("Inbt", 50, 1)
                            $ Player.Statup("Focus", 80, 15)   
                    else:
                            jump Strip_Ultimatum
                    
                elif Girl.Panties:                                                                        
                    # Will she go bottomless?
                    if ApprovalCheck(Girl, 1350, TabM = 3) or (Girl.SeenPussy and ApprovalCheck(Girl, 1100, TabM = 3) and not Taboo):
                            $ Girl.Statup("Lust", 75, 10) 
                            $ Line = Girl.Panties                
                            $ Girl.Panties = 0                     
                            if not Girl.SeenPussy:
                                    $ Girl.Statup("Obed", 60, 3)                              
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Inbt", 50, 4)
                                    $ Girl.Statup("Inbt", 200, 4) 
                                    if Girl == KittyX:                   
                                            "She shyly looks up at you, and then slowly tugs her [Line] off, flinging them to the side."
                                    elif Girl in (EmmaX,LauraX):
                                            "She hesitantly looks up at you, and then slowly pulls her [Line] down, kicking them off to the side."  
                                    else:
                                            "She shyly looks up at you, and then slowly pulls her [Line] down, kicking them off to the side."  
                                    call expression Girl.Tag + "_First_Bottomless" pass (1)
                            else:                
                                    $ Girl.Statup("Obed", 50, 1)                              
                                    $ Girl.Statup("Obed", 75, 1)
                                    if Girl == KittyX:                   
                                            "She  looks up at you, and then gently pulls her [Line] off, flicking them to the side."   
                                    else:
                                            "She  looks up at you, and then gently pulls her [Line] down, kicking them off to the side."                  
                                    $ Girl.Statup("Inbt", 70, 2)   
                            $ Player.Statup("Focus", 85, 15)
                    else:
                            jump Strip_Ultimatum
                    
                else:    
                    $ Girl.FaceChange("sexy")
                    if Girl == RogueX:
                            ch_r "I'm afraid that's all I have on, [Girl.Petname]. . ."
                    elif Girl == KittyX:    
                            ch_k "It looks like I've run out of clothes. . ."
                    elif Girl == EmmaX:
                            ch_e "Well, it appears I've run out of clothes, [Girl.Petname]. . ."
                    elif Girl == LauraX: 
                            ch_l "Well, that's all I've got, [Girl.Petname]. . ."
                    menu:
                            extend ""
                            "Ok, you can stop":
                                    $ Girl.RecentActions.append("stopdancing") 
                                    call expression Girl.Tag + "_Pos_Reset"
                            "Keep on dancing":
                                    $ Girl.RecentActions.append("keepdancing")
        # end "nude" not in Girl.RecentActions loop
        
        $ Girl.Statup("Lust", 70, 2)               #lust/Focus
        if "exhibitionist" in Girl.Traits:
                $ Girl.Statup("Lust", 200, 2)
        $ Player.Statup("Focus", 60, 3)
        if Trigger2 == "jackin":
                $ Girl.Statup("Lust", 200, 2)
                $ Player.Statup("Focus", 200, 5)
        
        if not Player.Semen and Player.Focus >= 50:
                $ Player.Focus = 50
    
        if Player.Focus >= 100 or Girl.Lust >= 100:                                     
                #If either of you could cum 
                
                if Player.Focus >= 100:                                                  
                    #You cum      
                    call Player_Cumming(Girl)
                    if "angry" in Girl.RecentActions:  
                            return    
                    $ Girl.Statup("Lust", 200, 5) 
                    if not Player.Semen and Trigger2 == "jackin":
                            "You're spitting dust here, maybe just watch quietly for a while."
                            $ Trigger2 = 0
                    if Player.Focus > 80:
                            jump Group_Strip_End   
                
                if Girl.Lust >= 100:                                                   
                    #and girl cums                    
                    call Girl_Cumming(Girl)
                    if Situation == "shift" or "angry" in Girl.RecentActions:                    
                            $ Count = 0
                            jump Group_Strip_End  
                        
                call AllReset(Girl)    
                
                if Girl == RogueX:
                            show Rogue_Sprite at Girl_Dance1(Girl)
                elif Girl == KittyX:
                            show Kitty_Sprite at Girl_Dance1(Girl)
                elif Girl == EmmaX:
                            show Emma_Sprite at Girl_Dance1(Girl)
                elif Girl == LauraX:
                            show Laura_Sprite at Girl_Dance1(Girl)
                        
                "[Girl.Name] begins to dance again."
         
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm           
                call Girl_Cumming(Partner)
                    
        menu:
            "[Girl.Name] should. . ."
            "Keep Going. . ." if "keepdancing" not in Girl.RecentActions:
                    $ Girl.Eyes = "sexy"
                    if Girl.Love >= 700 or Girl.Obed >= 500:
                        if not Tempmod:
                            $ Tempmod = 10
                        elif Tempmod <= 20:
                            $ Tempmod += 1
                    if Taboo and Girl.Strip <= 10:
                        $ Girl.Statup("Obed", 50, 7)
                    elif Taboo or Girl.Strip <= 10:
                        $ Girl.Statup("Obed", 50, 5)
                    elif Girl.Strip <= 50:
                        $ Girl.Statup("Obed", 50, 3) 
            "Keep Dancing. . ." if "keepdancing" in Girl.RecentActions:
                    $ Girl.Eyes = "sexy"    
                    
            "Stop stripping, keep dancing" if "keepdancing" not in Girl.RecentActions:
                    if Girl == RogueX:
                            ch_r "Ok. . ."
                    elif Girl == KittyX:  
                            ch_k "K. . ."  
                    elif Girl == EmmaX:
                            ch_e "Oh? Very well."
                    elif Girl == LauraX: 
                            ch_l "Huh? I guess. . ."
                    $ Girl.RecentActions.append("keepdancing")
                
            "Start stripping again" if "keepdancing" in Girl.RecentActions:
                    $ Girl.RecentActions.remove("keepdancing")
                    if "stripforced" in Girl.RecentActions: 
                            call AnyLine(Girl,". . .") 
                    else:
                            if Girl == RogueX:
                                    ch_r "Hmm. . ."
                            elif Girl == KittyX:  
                                    ch_k "Huh?"  
                            else:
                                    call AnyLine(Girl,"Hmm. . .") 
                    
            "Just watch silently":
                if "watching" not in Girl.RecentActions:
                    if "keepdancing" not in Girl.RecentActions:
                        if Taboo and Girl.Strip <= 10:
                            $ Girl.Statup("Inbt", 50, 3) 
                        elif Taboo or Girl.Strip <= 10:
                            $ Girl.Statup("Inbt", 50, 1) 
                    elif Girl.Strip <= 50:
                            $ Girl.Statup("Inbt", 50, 2)
                            $ Girl.Statup("Lust", 70, 2) 
                    $ Girl.RecentActions.append("watching")  
            
            "Start jack'in it." if Trigger2 != "jackin":
                    call Jackin(Girl)                   
            "Stop jack'in it." if Trigger2 == "jackin":
                    $ Trigger2 = 0
                    
            "Lose the [Girl.Arms]. . ." if Girl.Arms:
                    $ Girl.FaceChange("surprised")
                    $ Girl.Mouth = "kiss"
                    call AnyLine(Girl,"All right, "+Girl.Petname+".") 
                    $ Girl.FaceChange("sexy")
                    $ Girl.Arms = 0          
            "Lose the gloves. . . (locked)" if not Girl.Arms:
                    pass
                    
            "Ok, that's enough.":
                    if Girl == RogueX:
                            ch_r "Ok, [Girl.Petname]. . . "
                    elif Girl == KittyX:  
                            ch_k "Ok. . ."  
                    else:
                            call AnyLine(Girl,"Alright, "+Girl.Petname+".")                     
                    $ renpy.pop_call()
                    jump Group_Strip_End
                
        return    


label Strip_Ultimatum:  
        if "keepdancing" in Girl.RecentActions: 
            return
            
        call expression Girl.Tag + "_Pos_Reset"
        
        $ Girl.FaceChange("bemused", 1)        
        if "stripforced" in Girl.RecentActions: 
                    $ Girl.FaceChange("sad", 1)  
                    if Girl == RogueX:
                            ch_r "That's as far as I care to go, [Girl.Petname]."
                    elif Girl == KittyX:   
                            ch_k "That's all you get." 
                    elif Girl == EmmaX:
                            ch_e "I think that's plenty, [Girl.Petname]."
                    elif Girl == LauraX: 
                            ch_l "Last call, [Girl.Petname]."
        else:
                    if Girl == RogueX:
                            ch_r "I'm sorry, [Girl.Petname], I'm not ready to show you more. . . Yet."
                    elif Girl == KittyX:   
                            ch_k "I don't know, [Girl.Petname], that's as far as I'll go for now." 
                    elif Girl == EmmaX:
                            ch_e "I'm afraid that's as far as I'm ready to go, [Girl.Petname]. . . for now."
                    elif Girl == LauraX: 
                            ch_l "Ok, that's enough, [Girl.Petname]. . . for now."
        menu:
            extend ""
            "That's ok, you can stop.":          
                    if "ultimatum" not in Girl.DailyActions:                  
                            $ Girl.Statup("Love", 50, 2)
                            $ Girl.Statup("Love", 90, 2)
                            $ Girl.Statup("Inbt", 50, 2)
                            $ Girl.DailyActions.append("ultimatum")
                    $ Girl.RecentActions.append("stopdancing")
                    return
            "That's ok, but keep dancing for a bit. . .":  
                    if "ultimatum" not in Girl.DailyActions:                          
                            $ Girl.Statup("Love", 50, 2)
                            $ Girl.Statup("Obed", 50, 2)
                            $ Girl.Statup("Inbt", 50, 2)
                            $ Girl.DailyActions.append("ultimatum")
                    $ Girl.RecentActions.append("keepdancing")
                    if "stripforced" in Girl.RecentActions: 
                            call AnyLine(Girl,". . .") 
                    else:
                            if Girl == RogueX:
                                    ch_r "Heh, ok [Girl.Petname]."
                            elif Girl == KittyX: 
                                    ch_k "Heh, alright."   
                            elif Girl == EmmaX:
                                    ch_e "Oh, if I must, [Girl.Petname]."
                            elif Girl == LauraX: 
                                    ch_l "Eh? Fine."
            "You'd better." if Girl.Forced:
                    if not ApprovalCheck(Girl, 500, "O", TabM=5) and not ApprovalCheck(Girl, 800, "L", TabM=5):                    
                            $ Girl.FaceChange("angry")                        
                            if Girl == RogueX:
                                    ch_r "I don't know who you think I am, but I ain't gonna just jump when you say \"toad\"."
                                    ch_r "I think we're done here for now." 
                            elif Girl == KittyX:    
                                    ch_k "I'm not just going to do \"whatever\"!"
                                    ch_k "I'm done with this."  
                            elif Girl == EmmaX:
                                    ch_e "I think you're overstepping your bounds here, [Girl.Petname]."
                                    ch_e "Remember your place."  
                            elif Girl == LauraX:       
                                    ch_l "I don't like that tone, [Girl.Petname]."
                            $ Girl.RecentActions.append("angry")
                            $ Girl.DailyActions.append("angry")  
                            call Remove_Girl(Girl)
                            return                                
                    $ Tempmod += 20
                    $ Girl.Forced += 1
                    $ Girl.FaceChange("sad")
                    if "stripforced" in Girl.RecentActions:                    
                            $ Girl.FaceChange("angry")
                            call AnyLine(Girl,". . .") 
                    else:
                            if Girl == RogueX:
                                    ch_r "I. . . guess I could. . ."
                            elif Girl == KittyX:  
                                    ch_k "I. . . could show a bit more. . ."  
                            elif Girl == EmmaX:
                                    ch_e "Hmm, forceful. . ."
                            elif Girl == LauraX: 
                                    ch_l "Grrrr. . ."
                            $ Girl.RecentActions.append("stripforced")
                    $ Girl.Statup("Love", 200, -40)
            "You can do better than that. Keep going." if not Girl.Forced:
                    if not ApprovalCheck(Girl, 300, "O", TabM=5) and not ApprovalCheck(Girl, 700, "L", TabM=5):                   
                            $ Girl.FaceChange("angry")
                            if Girl == RogueX:
                                    ch_r "I don't know who you think I am, but I ain't gonna just jump when you say \"toad\"."
                                    ch_r "I think we're done here for now." 
                            elif Girl == KittyX:    
                                    ch_k "I'm not just going to do \"whatever\"!"
                                    ch_k "I'm done with this."  
                            elif Girl == EmmaX:
                                    ch_e "I think you're overstepping your bounds here, [Girl.Petname]."
                                    ch_e "Remember your place."  
                            elif Girl == LauraX:       
                                    ch_l "I don't like that tone, [Girl.Petname]."
                            $ Girl.RecentActions.append("angry")
                            $ Girl.DailyActions.append("angry")  
                            call Remove_Girl(Girl)
                            return                
                    $ Girl.Statup("Love", 200, -10)
                    $ Girl.Statup("Obed", 50, 3)
                    $ Girl.Statup("Obed", 75, 5)
                    $ Tempmod += 20
                    $ Girl.Forced += 1
                    $ Girl.FaceChange("sad")
                    if Girl == RogueX:
                            ch_r "Well, if you insist. . ."
                    elif Girl == KittyX:    
                            ch_k "I mean, maybe. . ."
                    elif Girl == EmmaX:
                            ch_e "I can't imagine doing better than \"perfection\". . ."
                    elif Girl == LauraX: 
                            ch_l ". . . Right. . ."
        if "ultimatum" not in Girl.DailyActions:
                    $ Girl.DailyActions.append("ultimatum")
                
        if Girl == RogueX:
                    show Rogue_Sprite at Girl_Dance1(Girl)
        elif Girl == KittyX:
                    show Kitty_Sprite at Girl_Dance1(Girl)
        elif Girl == EmmaX:
                    show Emma_Sprite at Girl_Dance1(Girl)
        elif Girl == LauraX:
                    show Laura_Sprite at Girl_Dance1(Girl)
        "[Girl.Name] begins to dance again."
        return
        
transform Girl_Dance1(Chr=Ch_Focus):     
        subpixel True 
        pos (Chr.SpriteLoc, 50)
        xoffset 0
        yoffset 0
        choice:
            parallel:              
                ease 2.5 xoffset -40
                ease 2.5 xoffset 0
            parallel:                  
                easeout 1.0 yoffset 30 # 70 and 80
                linear 0.5 yoffset 40
                easein 1.0 yoffset 0 
                easeout 1.0 yoffset 40
                linear 0.5 yoffset 50 #1.35
                easein 1.0 yoffset 0  
        choice:
            parallel:              
                ease 2.5 xoffset 40
                ease 2.5 xoffset 0
            parallel:                  
                easeout 1.0 yoffset 30 #1.3
                linear 0.5 yoffset 40
                easein 1.0 yoffset 0 
                easeout 1.0 yoffset 40
                linear 0.5 yoffset 50 #1.35
                easein 1.0 yoffset 0  
        choice(0.3):
            parallel:             
                ease 2.5 xoffset -30
                ease 2.5 xoffset 0
            parallel:     
                ease 1.5 yoffset 150 
                ease 3.5 yoffset 0 
        repeat
# End Strip Dancing / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Girl_Lesbian / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Les_Interupted(Girl=0,BO=[]):  
        if Girl not in TotalGirls:
                $ Girl = Ch_Focus
        # Called if you catch them fucking 
        if "unseen" not in Girl.RecentActions:
                if Girl.Org < 3 and Girl.Action:                
                    menu:
                        "Did you want to stop them?"
                        "Yeah.":
                            pass
                        "No, let them keep going.":
                            $ Girl.Action -= 1 if Girl.Action > 0 else 0
                            jump Les_Cycle 
                else:
                    if Girl == LauraX:
                            ch_l "Ahhh, that hit the spot. . ."
                    else:
                            call AnyLine(Girl,"Ok, that's probably enough of that. . .")
                jump Les_After
        $ Girl.DrainWord("unseen",1,0) #She sees you, so remove unseens
        $ Partner.DrainWord("unseen",1,0) #She sees you, so remove unseens
        
        $ Girl.FaceChange("surprised", 1) 
        $ Partner.FaceChange("surprised",2) 
        
        "Suddenly, [Girl.Name] jerks up from what she was doing with a start, and gives [Partner.Name] a nudge."
        $ Girl.FaceChange("bemused", 0) 
        $ Partner.FaceChange("perplexed",1) 
                    
        if Girl == RogueX:
                ch_r "Um, [Player.Name], how long have you been watchin?"
        elif Girl == KittyX:
                ch_k "Eep! [Player.Name], how long have you been there?!"
        elif Girl == EmmaX:
                ch_e "Hmm? [Girl.Petname], enjoying the show?"
        elif Girl == LauraX:
                ch_l "Oh! Hey [Player.Name], how long have you been there?"
        $ Girl.Action -= 1 if Girl.Action > 0 else 0
        call Checkout(1)
        $ Line = 0
    
        #If you've been jacking it
        if Trigger2 == "jackin":
                $ Girl.Eyes = "down"                    
                if Girl == RogueX:
                        ch_r "And why is your cock out like that?!"
                elif Girl == KittyX:
                        ch_k "and why are you fapping?!"
                elif Girl == EmmaX:
                        ch_e "and was. . . that. .  really an appropriate reaction?"
                elif Girl == LauraX:
                        ch_l "Looks like you're taking care of yourself."
                menu:
                    extend ""
                    "Yeah, it was an excellent show.":   
                            $ Girl.FaceChange("sexy")
                            $ Girl.Statup("Obed", 50, 3)
                            $ Girl.Statup("Obed", 70, 2)
                            "[Girl.Name] glances over at [Partner.Name]."                    
                            if Girl == RogueX:
                                    ch_r "Well, I imagine it was. . ."
                            elif Girl == KittyX:
                                    ch_k "I mean, I guess. . ."
                            elif Girl == EmmaX:
                                    ch_e "I suppose it was. . ."
                            elif Girl == LauraX:
                                    ch_l "I get that. . ."
                            if Girl.Love >= 800 or Girl.Obed >= 500 or Girl.Inbt >= 500:
                                    $ Tempmod += 10
                                    $ Girl.Statup("Lust", 90, 5)                    
                                    if Girl == RogueX:
                                            ch_r "And the view from this angle ain't so bad either. . ."  
                                    elif Girl == KittyX:
                                            ch_k "And[Girl.like]you're not so bad yourself. . ."  
                                    elif Girl == EmmaX:
                                            ch_e "And at least you make good eye candy. . ."  
                                    elif Girl == LauraX:
                                            ch_l "You're not so bad to look at either. . ."  
                    #end "Yeah, it was an excellent show."
                    
                    "I. . . just got here?":
                            $ Girl.FaceChange("angry")                   
                            $ Girl.Statup("Love", 70, 2)
                            $ Girl.Statup("Love", 90, 1)
                            $ Girl.Statup("Obed", 50, 2)
                            $ Girl.Statup("Obed", 70, 2)
                            "She looks pointedly at your cock,"                    
                            if Girl == RogueX:
                                    ch_r "Suuure . . ."   
                            elif Girl == KittyX:
                                    ch_k "Riiight. . ."   
                            elif Girl == EmmaX:
                                    ch_e "I'm sure. . ."   
                            elif Girl == LauraX:
                                    ch_l "Uh HUH. . ."   
                            if Girl.Love >= 800 or Girl.Obed >= 500 or Girl.Inbt >= 500:
                                    $ Tempmod += 10
                                    $ Girl.Statup("Lust", 90, 5)
                                    $ Girl.FaceChange("bemused", 1)                    
                                    if Girl == RogueX:
                                            ch_r "-but I guess we were pretty tempting. . ." 
                                    elif Girl == KittyX:
                                            ch_k "-I can't exactly blame you though. . ."   
                                    elif Girl == EmmaX:
                                            ch_e "not that I can blame you. . ."   
                                    elif Girl == LauraX:
                                            ch_l "-can't blame you though."   
                            else:
                                    $ Tempmod -= 10
                                    $ Girl.Statup("Lust", 200, -5)
                    #end "I. . . just got here?"
                call Seen_First_Peen(Girl,Partner)
        #end "noticed you were jackin"
        else:         
                #you haven't been jacking it 
                if Girl == RogueX:
                        ch_r "H- how long you been stand'in there, [Girl.Petname]?"
                elif Girl == KittyX:
                        ch_k "Eep! [Player.Name], how long have you been there?!"  
                elif Girl == EmmaX:
                        ch_e "Have you been there long?"
                elif Girl == LauraX:                    
                        ch_l "Oh! Hey [Player.Name], how long have you been there?"
                menu:  
                    extend ""
                    "Long enough.":   
                            $ Girl.FaceChange("sexy", 1)
                            $ Girl.Statup("Obed", 50, 3)
                            $ Girl.Statup("Obed", 70, 2)                    
                            if Girl == RogueX:
                                    ch_r "Well I hope you got a good show out of it. . ."   
                            elif Girl == KittyX:
                                    ch_k "I guess we[Girl.like]really put on a show, huh. . ."   
                            elif Girl == EmmaX:
                                    ch_e "I supppose we did make a show of ourselves. . ."  
                            elif Girl == LauraX:
                                    ch_l "Didn't intend to put on a show. . ."
                    "I just got here.":
                            $ Girl.FaceChange("bemused", 1)
                            $ Girl.Statup("Love", 70, 2)
                            $ Girl.Statup("Love", 90, 1)                       
                            if Girl == RogueX:               
                                    ch_r "A likely story . . ."   
                            elif Girl == KittyX:                
                                    ch_k "Uh HUH. . ."   
                            elif Girl == EmmaX:               
                                    ch_e "I'm sure. . ."   
                            elif Girl == LauraX:                 
                                    ch_l "Uh HUH. . ."   
                            $ Girl.Statup("Obed", 50, 2)
                            $ Girl.Statup("Obed", 70, 2)    
                                
        if not ApprovalCheck(Girl, 1350):
                #If she doesn't like you enough to have you around. . .
                $ Girl.Statup("Love", 200, -5)
                $ Girl.FaceChange("angry")
                $ Girl.RecentActions.append("angry")
                $ Girl.DailyActions.append("angry")                    
                if Girl == RogueX:
                        ch_r "You should get out of here right now, and maybe learn ta knock?"
                elif Girl == KittyX:
                        ch_k "So maybe you could[Girl.like]leave us to it?"
                elif Girl == EmmaX:
                        ch_e "So perhaps you could leave us to it?"
                elif Girl == LauraX:
                        ch_l "So maybe just leave us to it?"
                $ renpy.pop_call()
                $ renpy.pop_call()
                if bg_current == "bg player":                                        
                        jump Campus_Map  
                else:
                        jump Player_Room  
        
        if Round <= 10:
                #if there's no time, return                    
                if Girl == RogueX:
                        ch_r "It's getting too late to do much about it right now though."
                elif Girl == KittyX:
                        ch_k "We were just about to take a break though."
                elif Girl == EmmaX:
                        ch_e "I suppose it was time for a break. . ."
                elif Girl == LauraX:
                        ch_l "I guess we could take a break though."
                return
        $ Situation = "interrupted"
    
label LesScene(Girl=0,Bonus = 0,BO=[]): #Repeating strokes
        if Girl not in TotalGirls:
                $ Girl = Ch_Focus
        call Shift_Focus(Girl)
        
        if Girl.LesWatch:
                $ Tempmod += 10
        elif Girl.Les:
                $ Tempmod += 5
        if Girl.SEXP >= 50:
                $ Tempmod += 25
        elif Girl.SEXP >= 30:
                $ Tempmod += 15
        elif Girl.SEXP >= 15:
                $ Tempmod += 5
            
        if Girl.Lust >= 90:
                $ Tempmod += 5
        elif Girl.Lust >= 75:
                $ Tempmod += 5
            
        elif Girl.Inbt >= 750:
                $ Tempmod += 5
            
        if "exhibitionist" in Girl.Traits:      
                $ Tempmod += (3*Taboo) 
            
        if "dating" in Girl.Traits or "sex friend" in Girl.Petnames:
                $ Tempmod += 10        
        elif "ex" in Girl.Traits:
                $ Tempmod -= 40  
                    
        if Partner:
                pass
        elif RogueX.Loc == bg_current and Girl != RogueX:         
                $ Partner = RogueX 
        elif KittyX.Loc == bg_current and Girl != KittyX:        
                $ Partner = KittyX 
        elif EmmaX.Loc == bg_current and Girl != EmmaX:          
                $ Partner = EmmaX  
        elif LauraX.Loc == bg_current and Girl != LauraX:        
                $ Partner = LauraX 
                           
        $ Line = Girl.GirlLikeCheck(Partner)   
        if Line >= 900:
                $ Bonus += 150
        elif Line >= 800 or "poly "+Partner.Tag in Girl.Traits:
                $ Bonus += 100
        elif Line >= 700:
                $ Bonus += 50
        elif Line <= 200:
                $ Bonus -= 200
        elif Line <= 500:
                $ Bonus -= 100
        $ Partner.DrainWord("unseen",1,0) #She sees you, so remove unseens    
        $ Line = 0
        
        $ Girl.AddWord(1,"noticed "+Partner.Tag,"noticed "+Partner.Tag) #ie $ Girl.RecentActions.append("noticed Partner") 
        $ Partner.AddWord(1,"noticed "+Girl.Tag,"noticed "+Girl.Tag) #ie $ Partner.RecentActions.append("noticed Girl") 
                
        if bg_current in ("bg player", "bg laura", "bg rogue", "bg emma"):
                $ Taboo = 0
                $ Girl.Taboo = 0
                $ Partner.Taboo = 0
        if Girl.ForcedCount and not Girl.Forced:
                $ Tempmod -= 5 * Girl.ForcedCount   
            
        $ Approval = ApprovalCheck(Girl, 1350, TabM = 2, Bonus = Bonus) # 1350, 1500, 1650, Taboo -800
        
        $ Girl.DrainWord("unseen",1,0) #She sees you, so remove unseens
        
        if Situation == "interrupted":    
            menu:
                extend ""
                "I guess I should probably get going then. . .":
                        $ Girl.Statup("Love", 80, 3)
                        if Approval >= 2:
                                # if lead girl is very much in                    
                                if Girl == RogueX:
                                        ch_r "Well, I didn't say you had to leave. . ."
                                elif Girl == KittyX:
                                        ch_k "Hmmmm, I don't know about that. . ."
                                elif Girl == EmmaX:
                                        ch_e "Well, if [Partner.Tag]'s game. . ."
                                elif Girl == LauraX:
                                        ch_l "Hmmmm, I don't know about that. . ."
                                call Les_Response(Partner,Girl,3,B2=Bonus) 
                                if not _return:
                                        return
                        else:
                                # If lead girl is only so/so, but Partner is on board, she tries to convince lead girl
                                call Les_Response(Partner,Girl,1,B2=Bonus)              
                                if not _return:
                                        #this is the default reaction if Partner is not into it either
                                        if Approval:                    
                                                if Girl == RogueX:
                                                        ch_r "I mean, you can hang out. . ."
                                                elif Girl == KittyX:
                                                        ch_k "You could at least stick around. . ."
                                                elif Girl == EmmaX:
                                                        ch_e "Well, you could at least stay for a bit. . ."
                                                elif Girl == LauraX:
                                                        ch_l "You could chill here."
                                                return
                                        else:                    
                                                if Girl == RogueX:
                                                        ch_r "Yeah, that's probably a good idea. . ."  
                                                elif Girl == KittyX:
                                                        ch_k "I guess so. . ."  
                                                elif Girl == EmmaX:
                                                        ch_e "I suppose. . ."  
                                                elif Girl == LauraX:
                                                        ch_l "Yeah. . ."  
                                                $ renpy.pop_call()
                                                $ renpy.pop_call()
                                                if bg_current == "bg player":                                        
                                                        jump Campus_Map  
                                                else:
                                                        jump Player_Room  
                                elif not Approval:
                                        #if Partner is in, but not lead girl                    
                                        if Girl == RogueX:
                                                ch_r "I'm sorry [Girl.Petname], I just am not interested in putting on a show."
                                        elif Girl == KittyX:
                                                ch_k "Sorry [Girl.Petname], I guess we'd like to keep this private."
                                        elif Girl == EmmaX:
                                                ch_e "So sorry [Girl.Petname], I suppose we'd like to keep this private."
                                        elif Girl == LauraX:
                                                ch_l "Sorry [Girl.Petname], maybe come back later."
                                        return                            
                                elif not Girl.Action:    
                                        #if she's tired out. . .
                                        if Girl == RogueX:
                                                ch_r "I'm sorry [Girl.Petname], I'm just too tuckered out right now. . ."
                                        elif Girl == KittyX:
                                                ch_k "Sorry [Girl.Petname], I'm kinda worn out already. . ."
                                        elif Girl == EmmaX:
                                                ch_e "So sorry [Girl.Petname], I needed a break. . ."
                                        elif Girl == LauraX:
                                                ch_l "Sorry [Girl.Petname], looks like we're taking a break. . ."
                                        return        
                                else:          
                                        #if it all worked out. . .
                                        if Girl == RogueX:
                                                ch_r "Ok, fine."  
                                        elif Girl == KittyX:
                                                ch_k "Sure."  
                                        elif Girl == EmmaX:
                                                ch_e "Very well."   
                                        elif Girl == LauraX:
                                                ch_l "Sure."    
                        #if it passed the hurdles. . .
                        $ Ch_Focus = Girl
                        jump Les_Prep
                        
                "So maybe I could join you girls?" if Player.Semen and Girl.Action:
                        $ Girl.FaceChange("sexy")                    
                        if Girl == RogueX:
                                ch_r "Well what did you have in mind?"    
                        elif Girl == KittyX:
                                ch_k "Mmmm, what would you like?"    
                        elif Girl == EmmaX:
                                ch_e "Oh? What do you bring to the table?"    
                        elif Girl == LauraX:
                                ch_l "Oh, you have something to add here?"    
                        $ Situation = "join"
                        return                      #returns to sexmenu=
                "So maybe I could watch a bit longer?":
                        $ Girl.FaceChange("bemused", 1)   
            #End "Interrupted" content.
        
        #first time
        if not Girl.LesWatch:                                                                
                $ Girl.FaceChange("surprised", 1,Mouth="kiss")                    
                if Girl == RogueX:
                        ch_r "You want me and [Partner.Name] to hook up, while you watch?"
                elif Girl == KittyX:
                        ch_k "You wanna watch me and [Partner.Name] hook up?"
                elif Girl == EmmaX:
                        ch_e "You wanna watch me and [Partner.Name] \"engaged?\""
                elif Girl == LauraX:
                        ch_l "You want to watch me and [Partner.Name] hook up?"
                if Girl.Forced:
                        $ Girl.FaceChange("sad")                    
                        if Girl == RogueX:
                                ch_r "And {i}just{/i} watch?"
                        elif Girl == KittyX:
                                ch_k "but {i}just{/i} watch, right?"
                        elif Girl == EmmaX:
                                ch_e "nothing more than that though?"
                        elif Girl == LauraX:
                                ch_l "{i}Just{/i} watching, right?"
        #end if first time. . .
                    
        if Approval and (Partner == RogueX or Girl == RogueX) and "touch" not in RogueX.Traits:    
                if Girl == RogueX:
                        ch_r "I don't know, isn't my touch. . . dangerous?"
                        ch_p "Don't worry, I can keep it turned off."
                        ch_r "I suppose you can. . ."      
                elif Girl == KittyX:
                        ch_k "I don't know, isn't it kinda. . . dangerous to touch Rogue?"
                        ch_p "Don't worry, I can keep it turned off."
                        ch_k "Oh, well I guess. . ."
                elif Girl == EmmaX:
                        ch_e "I'm not sure, Rogue's touch can be. . . disruptive?"
                        ch_p "Don't worry, I can keep it turned off."
                        ch_e "Oh, I suppose you can at that. . ."
                elif Girl == LauraX:
                        ch_l "I don't know, Rogue's touch can be. . . intense. . ."
                        ch_p "Don't worry, I can keep it turned off."
                        ch_l "Oh, well I guess. . ."
        #end "can Rogue touch" check
                         
        if not Girl.LesWatch and Approval:   
                #First time dialog                                                       
                if Girl.Forced: 
                        $ Girl.FaceChange("sad")
                        $ Girl.Statup("Love", 70, -3, 1)
                        $ Girl.Statup("Love", 20, -2, 1)
                elif Bonus >= 100:
                        $ Girl.FaceChange("sly", Eyes="side")
                        if Girl == RogueX:
                                ch_r "Hmm, actually I might enjoy this more than you think. . ."   
                        elif Girl == KittyX:
                                ch_k "Heh, you don't know what you're asking for. . ."    
                        elif Girl == EmmaX:
                                ch_e "This won't be my first time. . ."   
                        elif Girl == LauraX:      
                                ch_l "Well you'd be in for a treat. . ."   
                elif Girl.Love >= (Girl.Obed + Girl.Inbt):
                        $ Girl.FaceChange("sexy")
                        $ Girl.Brows = "sad"
                        $ Girl.Mouth = "smile" 
                        if Girl == RogueX:
                                ch_r "I haven't really given much thought to being with other people lately. . ." 
                        elif Girl == KittyX:
                                ch_k "I hadn't really considered putting on a show like this. . ."  
                        elif Girl == EmmaX:
                                ch_e "I hadn't considered this as one of your kinks. . ." 
                        elif Girl == LauraX:      
                                ch_l "I hadn't really considered putting on a show like this. . ."          
                elif Girl.Obed >= Girl.Inbt:
                        $ Girl.FaceChange("normal")
                        if Girl == RogueX:  
                                ch_r "If that's what you want, [Girl.Petname]. . ."   
                        elif Girl == KittyX:
                                ch_k "If that's what you want, [Girl.Petname]. . ."   
                        elif Girl == EmmaX:   
                                ch_e "If this is what gets you off, [Girl.Petname]. . ."  
                        elif Girl == LauraX:      
                                ch_l "I'm ok with that, [Girl.Petname]. . ."            
                else: # Uninhibited 
                        $ Girl.FaceChange("sad")
                        $ Girl.Mouth = "smile"                               
                        if Girl == RogueX:
                                ch_r "I guess it could be fun with you watching. . ."   
                        elif Girl == KittyX:
                                ch_k "I guess it could be fun with you watching. . ."   
                        elif Girl == EmmaX:
                                ch_e "I do enjoy an audience. . ."   
                        elif Girl == LauraX:      
                                ch_l "Not that I mind. . ."   
                #End first time with approval dialogs    
        
        elif Approval:            
                    #Second time+ initial dialog                                                           
                    if Girl.Forced: 
                            $ Girl.FaceChange("sad")
                            $ Girl.Statup("Love", 70, -3, 1)
                            $ Girl.Statup("Love", 20, -2, 1)
                            if Girl == RogueX:
                                    ch_r "So you want to watch me with a girl again?"  
                            elif Girl == KittyX:
                                    ch_k "You really like this girl-on-girl stuff, huh?"  
                            elif Girl == EmmaX:
                                    ch_e "You enjoyed the last show?"  
                            elif Girl == LauraX:      
                                    ch_l "This is what gets you off?"  
                    elif Approval and "lesbian" in Girl.RecentActions:
                            $ Girl.FaceChange("sexy", 1)
                            if Girl == RogueX:
                                    ch_r "I guess we could get a little closer. . ."
                            elif Girl == KittyX:
                                    ch_k "A little more wouldn't hurt. . ."   
                            elif Girl == EmmaX:
                                    ch_e "Hmm, back for more?"                                              
                            elif Girl == LauraX:      
                                    ch_l "I wouldn't mind a little more. . ."  
                            $ Ch_Focus = Girl  
                            jump Les_Prep
                    elif Approval and "lesbian" in Girl.DailyActions:
                            $ Girl.FaceChange("sexy", 1)
                            $ Line = renpy.random.choice(["Enjoyed the show?",       
                                    "Didn't get enough earlier?",
                                    "I don't mind having an audience. . ."]) 
                            call AnyLine(Girl,Line)
                    elif Girl.Mast < 3:        
                            $ Girl.FaceChange("sexy", 1)
                            $ Girl.Brows = "confused"
                            if Girl == RogueX:
                                    ch_r "You like to watch, huh?"  
                            elif Girl == KittyX: 
                                    ch_k "You really do like to watch."    
                            elif Girl == EmmaX:
                                    ch_e "You do like to watch."   
                            elif Girl == LauraX:      
                                    ch_l "You do like to watch."       
                    else:       
                            $ Girl.FaceChange("sexy", 1)
                            $ Girl.ArmPose = 2
                            $ Line = renpy.random.choice(["You do like to watch.",                 
                                    "So you'd like us to go again?",                 
                                    "You want to watch some more?",
                                    "You want me to get it on with "+Partner.Tag+"?"]) 
                            call AnyLine(Girl,Line)  
                    $ Line = 0                        
                    #End second time+ initial dialog
        
        if Approval >= 2:      
                    #If she's into it. . .                                                                            
                    if Girl.Forced:
                            $ Girl.FaceChange("sad")
                            $ Girl.Statup("Obed", 90, 1)
                            $ Girl.Statup("Inbt", 60, 1)
                            if Girl == RogueX:
                                    ch_r "Fine, I'm ok with it if she is. . ." 
                            elif Girl == KittyX:
                                    ch_k "Well, I guess if she's fine with it. . ." 
                            elif Girl == EmmaX:
                                    ch_e "So long as she finds it acceptable. . ." 
                            elif Girl == LauraX:      
                                    ch_l "Not the worst way to spend some time. . ." 
                    else:
                            $ Girl.FaceChange("sexy", 1)
                            $ Girl.Statup("Love", 90, 1)
                            $ Girl.Statup("Inbt", 50, 3) 
                            if Situation == "interrupted":
                                    if Girl == RogueX:
                                                ch_r "Well I could do some more. . ."
                                    elif Girl == KittyX:
                                                ch_k "Well I guess we could get back to it. . ."
                                    elif Girl == EmmaX:
                                                ch_e "Well I suppose we could continue. . ."
                                    elif Girl == LauraX:      
                                                ch_l "Well I could get back in there. . ."
                            else:
                                    $ Line = renpy.random.choice(["Well. . . ok.",                 
                                        "I don't mind getting with her. . .",
                                        "A",    
                                        "Sure.", 
                                        "I guess. . .",
                                        "Heh, ok, fine."]) 
                                    if Line == "A":
                                            if Girl == RogueX:
                                                    ch_r "I may have needed this anyway. . ."
                                            elif Girl == KittyX:
                                                    ch_k "I kinda needed this anyways. . ."
                                            elif Girl == EmmaX:
                                                    ch_e "I don't mind getting intimate with her. . ."
                                            elif Girl == LauraX:      
                                                    ch_l "I kinda needed to blow off some steam. . ."                                    
                                    else:           
                                            call AnyLine(Girl,Line)  
                                    $ Line = 0
                    $ Girl.Statup("Obed", 20, 1)
                    $ Girl.Statup("Obed", 60, 1)
                    $ Girl.Statup("Inbt", 70, 2) 
                    jump Les_Partner   
                    #end instant approval
        else:       
            #If she's not into it, but maybe. . .  
            if Girl == RogueX:
                    ch_r "I'm not sure about that though, [Girl.Petname]."
            elif Girl == KittyX:
                    ch_k "I don't know about that, [Girl.Petname]."
            elif Girl == EmmaX:
                    ch_e "I'm not sure about that, [Girl.Petname]."
            elif Girl == LauraX:        
                    ch_l "I don't know, [Girl.Petname]."                                                                                
            menu:
                "Maybe later?":
                        $ Girl.FaceChange("sexy", 1)  
                        if Bonus >= 100:
                                $ Girl.Statup("Inbt", 90, 5)  
                                if Girl == RogueX:
                                        ch_r "Well. . . definitely at some point. . ."
                                elif Girl == KittyX:
                                        ch_k "I mean, eventually. . ."
                                elif Girl == EmmaX:
                                        ch_e "Eventually. . ."
                                elif Girl == LauraX:      
                                        ch_l "Maybe some other time. . ."
                        elif Bonus >= 0:
                                $ Girl.GLG(Partner,800,3,1)
                                if Girl == RogueX:
                                        ch_r "Um, I don't know. . . maybe?"
                                elif Girl == KittyX:
                                        ch_k "Um, I don't know. . . maybe?"
                                elif Girl == EmmaX:
                                        ch_e "One never knows. . ."
                                elif Girl == LauraX:      
                                        ch_l "Eh, I don't know. . ."
                        else:
                                $ Girl.FaceChange("angry", 1, Eyes="side") 
                                if Girl == RogueX:
                                        ch_r "Yeah, I really don't see that happening. . ."
                                elif Girl == KittyX:
                                        ch_k "Not likely."
                                elif Girl == EmmaX:
                                        ch_e "Unlikely."
                                elif Girl == LauraX:      
                                        ch_l "Probably not."
                        if Girl == RogueX:
                                ch_r "But thanks for being ok with that."
                        elif Girl == KittyX:
                                ch_k "Thanks for being cool though. . ."
                        elif Girl == EmmaX:
                                ch_e "I do appreciate your restraint."
                        $ Girl.FaceChange("smile", 1) 
                        $ Girl.Statup("Love", 80, 2)
                        $ Girl.Statup("Inbt", 70, 5)   
                        call Taboo_Level
                        return
                        # end "Maybe later?"
                        
                "You look like you might be into it. . .":             
                        if Approval:
                                $ Girl.FaceChange("sexy")     
                                $ Girl.Statup("Obed", 90, 4)
                                $ Girl.Statup("Obed", 50, 5)
                                $ Girl.Statup("Inbt", 70, 4) 
                                $ Girl.Statup("Inbt", 40, 4) 
                                $ Line = renpy.random.choice(["Well. . . ok.",                 
                                        "I don't mind getting with her. . .",
                                        "A",    
                                        "Sure.", 
                                        "I guess. . .",
                                        "Heh, ok, fine."]) 
                                if Line == "A":
                                        if Girl == RogueX:
                                                ch_r "I may have needed this anyway. . ."
                                        elif Girl == KittyX:
                                                ch_k "I kinda needed this anyways. . ."
                                        elif Girl == EmmaX:
                                                ch_e "I don't mind getting intimate with her. . ."
                                        elif Girl == LauraX:      
                                                ch_l "I kinda needed to blow off some steam. . ."                                    
                                else:           
                                        call AnyLine(Girl,Line)  
                                call AnyLine(Girl,Line)  
                                $ Line = 0                   
                                jump Les_Partner
                        
                "Just get at it already.":                                              
                        # Pressured into it
                        $ Approval = ApprovalCheck(Girl, 550, "OI", TabM = 2) # 55, 70, 85
                        if Approval > 1 or (Approval and Girl.Forced):
                                $ Girl.FaceChange("sad")
                                $ Girl.Statup("Love", 70, -5, 1)
                                $ Girl.Statup("Love", 200, -5)   
                                if Girl == RogueX:                
                                        ch_r "Ok, fine. I'll give it a try."  
                                elif Girl == KittyX:               
                                        ch_k "Ok, whatever."  
                                elif Girl == EmmaX:                
                                        ch_e "Oh, fine."  
                                elif Girl == LauraX:                    
                                        ch_l "Ok, if you insist."  
                                $ Girl.Statup("Obed", 80, 4)
                                $ Girl.Statup("Inbt", 80, 1) 
                                $ Girl.Statup("Inbt", 60, 3)  
                                $ Girl.Forced = 1  
                                jump Les_Partner
                        else:                              
                                $ Girl.Statup("Love", 200, -20)     
                                $ Girl.RecentActions.append("angry")
                                $ Girl.DailyActions.append("angry")
        # end of asking her to do it
        
        call Les_Response(Partner,Girl,1,B2=Bonus) 
        if _return:
                #if the other girl convinces her
                $ Girl.FaceChange("smile", 1)
                if Girl == RogueX:
                        ch_r "Ok, fine! You've talked me into it."
                        ch_r "Get over here. . ."
                elif Girl == KittyX:
                        ch_k "Ok, if {i}you{/i} want to."
                        ch_k "Commere. . ."
                elif Girl == EmmaX:
                        ch_e "Well, if you insist, dear."
                        $ Girl.FaceChange("sly", 1)
                        ch_e "Get over here. . ."
                elif Girl == LauraX:      
                        ch_l "Ok, if {i}you're{/i} into it."
                        ch_l "Get over here. . ."
                $ Ch_Focus = Girl
                jump Les_Prep
                
                
        #She refused all offers.
        $ Girl.ArmPose = 1                
        if not Partner:
                if Girl == RogueX:
                        ch_r "It would take two to tango, so. . ."
                elif Girl == KittyX:
                        ch_k "Seems like she wasn't into it. . ."
                elif Girl == EmmaX:
                        ch_e "Well, I can't exactly do this alone. . ."
                elif Girl == LauraX:      
                        ch_l "I don't know if I should feel insulted. . ."
        elif Girl.Forced:
                $ Girl.FaceChange("angry", 1)
                if Girl == RogueX:
                        ch_r "Look, that's just not on the table."
                elif Girl == KittyX:
                        ch_k "I'm just not into that."
                elif Girl == EmmaX:
                        ch_e "I'm just not into that."
                elif Girl == LauraX:      
                        ch_l "I'm not into that."
                $ Girl.Statup("Lust", 90, 5)         
                if Girl.Love > 300:
                        $ Girl.Statup("Love", 70, -2)
                $ Girl.Statup("Obed", 50, -2)    
                $ Girl.RecentActions.append("angry")
                $ Girl.DailyActions.append("angry")  
        elif Taboo > 20:                            
                # she refuses and this is too public a place for her
                $ Girl.FaceChange("angry", 1)          
                $ Girl.DailyActions.append("tabno") 
                if Girl == RogueX:
                        ch_r "Definitely not around here."  
                elif Girl == KittyX:
                        ch_k "Totally not around here." 
                elif Girl == EmmaX:
                        ch_e "Totally not around here."  
                elif Girl == LauraX:      
                        ch_l "Not someplace so public."     
                $ Girl.Statup("Lust", 90, 5)  
                $ Girl.Statup("Obed", 50, -3) 
        elif Girl.Les:
                $ Girl.FaceChange("sad") 
                if Girl == RogueX: 
                        if Bonus >= 100:
                            ch_r "I just don't think I'm ready for that sort of thing."     
                        else:    
                            ch_r "I just don't think I'm into that sort of thing."   
                elif Girl == KittyX:    
                        if Bonus >= 100:
                            ch_k "I'm not really comfortable with that."     
                        else:    
                            ch_k "I don't think I'm ready for an audience."  
                elif Girl == EmmaX:   
                        if Bonus >= 100:
                            ch_e "I'm not really comfortable with that."     
                        else:    
                            ch_e "I don't think I'm ready for an audience."    
                elif Girl == LauraX:      
                        if Bonus >= 100:
                            ch_l "I'm not up for that."     
                        else:    
                            ch_l "Not with an audience."     
        else:
                $ Girl.FaceChange("normal", 1)
                if Girl == RogueX:  
                        ch_r "Heh, noway, I am {i}not{/i} doing that."  
                elif Girl == KittyX:
                        ch_k "No way."  
                elif Girl == EmmaX: 
                        ch_e "No way."                      
                elif Girl == LauraX:      
                        ch_l "Nope."  
        $ Girl.RecentActions.append("no lesbian")                      
        $ Girl.DailyActions.append("no lesbian") 
        $ Tempmod = 0 
        call Taboo_Level
        return
    
label Les_Partner:
        # This checks to see if the other girl is into it. 
        # Girl and BO are passed from previous label
        
        $ BO = TotalGirls[:]  
        $ BO.remove(Girl)
        while BO:                   
                if BO[0].Loc == bg_current:
                        call Les_Response(BO[0],Girl,2) 
                        if not _return:
                                # If she refused
                                return
                $ BO.remove(BO[0])
        #if nobody refuses, it passes through to the next label
                                
label Les_Prep(Girl=Ch_Focus,BO=[]):    
        #sets the scene up
        $ Line = 0
        if Girl not in TotalGirls or Girl == Partner:
                $ Girl = Ch_Focus    
                if Girl == Partner:
                    $ Partner = 0
                    $ Line = 1
        if Partner in TotalGirls:
                pass
        elif RogueX.Loc == bg_current and Girl != RogueX:         
                $ Partner = RogueX 
        elif KittyX.Loc == bg_current and Girl != KittyX:        
                $ Partner = KittyX 
        elif EmmaX.Loc == bg_current and Girl != EmmaX:          
                $ Partner = EmmaX  
        elif LauraX.Loc == bg_current and Girl != LauraX:        
                $ Partner = LauraX 
                
        if Line:
                #if for some reason the Partner and lead were jumbled, swap them. 
                call Shift_Focus(Partner)
                
        $ Line = 0
                
        $ Girl.AddWord(1,"noticed "+Partner.Tag,"noticed "+Partner.Tag) #ie $ Girl.RecentActions.append("noticed Partner") 
        $ Partner.AddWord(1,"noticed "+Girl.Tag,"noticed "+Girl.Tag) #ie $ Partner.RecentActions.append("noticed Girl") 
                
        if "unseen" not in Girl.RecentActions:
                #if she knows you're there. . .
                $ Girl.FaceChange("sexy")
                $ Girl.ArmPose = 2
                "[Girl.Name] move's closer to [Partner.Name] and wraps her arms around her neck."
                if not Girl.LesWatch:
                        #First time        
                        if Girl.Forced:
                            $ Girl.Statup("Love", 90, -20)
                            $ Girl.Statup("Obed", 70, 55)
                            $ Girl.Statup("Inbt", 80, 55) 
                        else:
                            $ Girl.Statup("Love", 90, 5)
                            $ Girl.Statup("Obed", 70, 20)
                            $ Girl.Statup("Inbt", 80, 60)  
                call Les_FirstKiss
                $ Trigger3 == "kiss girl"
                $ Trigger4 == "kiss girl"
            
        $ Trigger = "lesbian"   
        if Situation:     
            $ renpy.pop_call() 
            $ Situation = 0 
        $ Line = 0
        if Taboo:
            $ Girl.DrainWord("tabno")
        $ Girl.DrainWord("no lesbian")
        $ Girl.AddWord(0,"lesbian","lesbian") #adds "lesbian" to daily and recent
        $ Partner.AddWord(0,"lesbian","lesbian") #adds "lesbian" to daily and recent
    
label Les_Cycle(Girl=Ch_Focus): #Repeating strokes
        if Girl not in TotalGirls:
            $ Girl = Ch_Focus
            
        while Round >=0:  
            call Shift_Focus(Girl)
            call Les_Launch(Girl)  
            $ Girl.LustFace()      

            if  Player.Focus < 100:                                                    
                        #Player Command menu
                        menu:
                            "Keep watching. . .":
                                        pass
                                       
                            "\"Ahem. . .\"" if "unseen" in Girl.RecentActions:  
                                        jump Les_Interupted   
                                        
                            "Start jack'in it." if Trigger2 != "jackin":
                                        call Jackin(Girl)                  
                            "Stop jack'in it." if Trigger2 == "jackin":
                                        $ Trigger2 = 0
                                            
                            "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                        pass
                            "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                        "You concentrate on not burning out too quickly."                
                                        $ Player.FocusX = 1
                            "Release your focus." if Player.FocusX:
                                        "You release your concentration. . ."                
                                        $ Player.FocusX = 0
                                                                
                            "Other options":
                                    menu:   
                                        "Offhand action":
                                                if Girl.Action and MultiAction:
                                                        call Offhand_Set
                                                        if Trigger2:
                                                             $ Girl.Action -= 1
                                                else:
                                                        call Sex_Basic_Dialog(Girl,"tired")  # "I'm actually getting a little tired,"  
                                                
                                        "Threesome actions":   
                                            menu:
                                                "Ask [Girl.Name] to do something else with [Partner.Name]":
                                                        if "unseen" in Girl.RecentActions:
                                                                ch_p "Oh yeah, why don't you. . ."
                                                                jump Les_Interupted
                                                        else:                        
                                                                call Les_Change(Girl)
                                                "Ask [Partner.Name] to do something else":
                                                        if "unseen" in Girl.RecentActions:
                                                                ch_p "Oh yeah, why don't you. . ."
                                                                jump Les_Interupted
                                                        else:                        
                                                                call Three_Change(Girl)  
                                                            
                                                "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                            $ ThreeCount = 0                                                            
                                                "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        if "unseen" in Girl.RecentActions:
                                                                ch_p "Oh, that's good. . ."
                                                                jump Les_Interupted
                                                        else:                        
                                                                $ ThreeCount = 0  
                                                                
                                                #"Swap to [Partner.Name]":
                                                            #call Trigger_Swap(Girl)
                                                "Undress [Partner.Name]":
                                                        if "unseen" in Girl.RecentActions:
                                                                ch_p "Oh, yeah, take it off. . ."
                                                                jump Les_Interupted
                                                        else:                        
                                                                call Girl_Undress(Partner)
                                                                call Shift_Focus(Partner)
                                                                jump Les_Cycle 
                                                "Clean up Partner":
                                                        if "unseen" in Girl.RecentActions:
                                                                ch_p "You've got a little something. . ."
                                                                jump Les_Interupted
                                                        else:                        
                                                                call Girl_Cleanup(Partner,"ask")
                                                                call Shift_Focus(Partner)
                                                                jump Les_Cycle 
                                                "Never mind":
                                                                jump Les_Cycle 
                                        "undress [Girl.Name]":
                                                        if "unseen" in Girl.RecentActions:
                                                                ch_p "Oh yeah, why don't you. . ."
                                                                jump Les_Interupted
                                                        else:                        
                                                                call Girl_Undress(Girl)   
                                        "Clean up [Girl.Name] (locked)" if not Girl.Spunk:
                                                                pass  
                                        "Clean up [Girl.Name]" if Girl.Spunk:
                                                if "unseen" in Girl.RecentActions:
                                                                ch_p "You've got a little something. . ."
                                                                jump Les_Interupted
                                                else:                        
                                                                call Girl_Cleanup(Girl,"ask")                                         
                                        "Never mind":
                                                                jump Les_Cycle  
                                                
                            "Back to Sex Menu" if MultiAction: 
                                        ch_p "Let's try something else."
                                        call expression Girl.Tag + "_Pos_Reset"
                                        call expression Partner.Tag + "_Pos_Reset"
                                        $ Situation = "shift"
                                        $ Line = 0
                                        jump Les_After
                            "End Scene" if not MultiAction: 
                                        ch_p "Let's stop for now."
                                        call expression Girl.Tag + "_Pos_Reset"
                                        call expression Partner.Tag + "_Pos_Reset"
                                        $ Line = 0
                                        jump Les_After   
            #End menu (if Line)
            
            call Shift_Focus(Girl)  
            call Sex_Dialog(Girl,Partner)
            
            $ Cnt += 1
            $ Round -= 1
                 
            $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
            
            if Player.Focus >= 100 or Girl.Lust >= 100:    
                        #If either of you can cum:
                        if Player.Focus >= 100:
                                #If you can cum:  
                                if "unseen" not in Girl.RecentActions: #if she knows you're there
                                        call Player_Cumming(Girl)
                                        if "angry" in Girl.RecentActions:  
                                                call expression Girl.Tag + "_Pos_Reset"
                                                call expression Partner.Tag + "_Pos_Reset"
                                                return    
                                        $ Girl.Statup("Lust", 200, 5) 
                                        if 100 > Girl.Lust >= 70 and Girl.OCount < 2:             
                                                $ Girl.RecentActions.append("unsatisfied")                      
                                                $ Girl.DailyActions.append("unsatisfied") 
                                        $ Line = "came"
                                else: #If she wasn't aware you were there
                                        "You grunt and try to hold it in."
                                        $ Player.Focus = 95
                                        jump Les_Interupted
         
                        if Girl.Lust >= 100: 
                                        #If the lead Girl can cum                                              
                                        call Girl_Cumming(Girl)
                                        jump Les_Interupted
                           
                        if Line == "came": 
                                        $ Line = 0
                                        if not Player.Semen:
                                                "You're emptied out, you should probably take a break."       
            if Partner and Partner.Lust >= 100:
                    #Checks if partner could orgasm
                    call Girl_Cumming(Partner)            
                                
            #End orgasm
            
            $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0
            
            if "unseen" in Girl.RecentActions:
                    if Round == 10:
                            "It's getting a bit late, [Girl.Name] and [Partner.Name] will probably be wrapping up soon."  
                    elif Round == 5:
                            "They're definitely going to stop soon."
            else:
                    if Round == 10:
                            call Sex_Basic_Dialog(Girl,10) #"You might want to wrap this up, it's getting late." 
                    elif Round == 5:
                            call Sex_Basic_Dialog(Girl,5)   #"Seriously, it'll be time to stop soon."     
        #Round = 0 loop breaks
        $ Girl.FaceChange("bemused", 0)
        $ Line = 0
        if "unseen" not in Girl.RecentActions:
                call Sex_Basic_Dialog(Girl,"done")   #"Ok, [Girl.Petname], that's enough of that for now."  
    

label Les_After:            
        call expression Girl.Tag + "_Pos_Reset"
        if not Partner:
                $ Tempmod = 0  
                call Checkout
                return   
        call expression Partner.Tag + "_Pos_Reset"
        $ Girl.FaceChange("sexy") 
        if Partner == EmmaX:
                call Partner_Like(Girl,4)
        else:
                call Partner_Like(Girl,3)
        $ Girl.LesWatch += 1 
        $ Partner.LesWatch += 1 
        if Girl.LesWatch == 1:            
                $ Girl.SEXP += 15    
                if Girl.Love >= 500 and Girl.Org:
                        if Girl == RogueX:
                                ch_r "I have to say, I really enjoyed that one. . ." 
                        elif Girl == KittyX:
                                ch_k "Hmm, that's kinda fun with an audience. . ." 
                        elif Girl == EmmaX:
                                ch_e "I do enjoy an audience. . ." 
                                $ Girl.FaceChange("sly",1) 
                                ch_e "something to keep in mind?"
                        elif Girl == LauraX:      
                                ch_l "I enjoyed the audience. . ."         
        if Partner.LesWatch == 1:            
                $ Partner.SEXP += 15    
                if Partner.Love >= 500 and Partner.Org:
                        if Partner == RogueX:
                                ch_r "I have to say, I really enjoyed that one. . ." 
                        elif Partner == KittyX:
                                ch_k "Hmm, that's kinda fun with an audience. . ." 
                        elif Partner == EmmaX:
                                ch_e "I do enjoy an audience. . ." 
                                $ Partner.FaceChange("sly",1) 
                                ch_e "something to keep in mind?"
                        elif Partner == LauraX:      
                                ch_l "I enjoyed the audience. . ." 
        if not Situation:
                call Post_Les_Dialog
        $ Girl.AddWord(1,0,0,0,"les "+Partner.Tag) #ie $ Girl.RecentActions.append("noticed Partner") 
        $ Partner.AddWord(1,0,0,0,"les "+Girl.Tag) #ie $ Partner.RecentActions.append("noticed Girl")         
        $ Tempmod = 0  
        call Checkout
        return   
    # End LesScene


label Post_Les_Dialog:
        # called from Les_After if they have dialog for each other.         
        if Girl == RogueX:
                ch_r "That was nice. . ."
        elif Girl == KittyX:
                ch_k "That was fun. . ."
        elif Girl == EmmaX:
                ch_e "That was enjoyable. . ."
        elif Girl == LauraX:
                ch_l "That was fun. . ."
                
        if "les "+Partner.Tag in Girl.History:
                #if this wasn't the first time. . .
                if Partner == RogueX:
                        ch_r "Mmmm yeah. . ."
                elif Partner == KittyX:
                        ch_k "Mmmm yeah that was good. . ."
                elif Partner == EmmaX:
                        ch_e "Certainly. . ."
                elif Partner == LauraX:
                        ch_l "Yup. . ."
        else:
                # If this is the first time they've done this. . .
                # "les Kitty" not in RogueX.History. . .
                if Girl.GirlLikeCheck(Partner) >= 600:
                        #if the Lead girl likes the Partner. . .
                        if Girl == RogueX:
                                ch_r "You. . . really know what you're doing down there. . ."
                        elif Girl == KittyX:
                                ch_k "You're really good at that!"
                        elif Girl == EmmaX:
                                ch_e "You were delightful dear!"
                        elif Girl == LauraX:
                                ch_l "I liked that thing with the mouth work."
                else:
                        #if the Lead girl doesn't like the Partner. . .
                        if Girl == RogueX:
                                ch_r "That. . . wasn't awful. . ."
                        elif Girl == KittyX:
                                ch_k "That was. . . interesting. . ."
                        elif Girl == EmmaX:
                                ch_e "At least you could keep up. . ."
                        elif Girl == LauraX:
                                ch_l "That was ok. . ."
                        
                #second girl response. . .        
                if Partner.GirlLikeCheck(Girl) >= 600:
                        #if the Partner girl likes the Lead. . .
                        if Partner == RogueX:
                                ch_r "Um, yeah, you too. . ."
                        elif Partner == KittyX:
                                ch_k "Yeah, that was really hot. . ."
                        elif Partner == EmmaX:
                                ch_e "Practice, dear. . ."
                        elif Partner == LauraX:
                                ch_l "I can read a map."
                else:
                        #if the Partner girl doesn't like the Lead. . .
                        if Partner == RogueX:
                                ch_r "I guess. . ."
                        elif Partner == KittyX:
                                ch_k "I guess. . ."
                        elif Partner == EmmaX:
                                ch_e "You could certainly do with more practice. . ."
                        elif Partner == LauraX:
                                ch_l "Uh-huh."
        return
    
    
#Start Les_Response >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >
label Les_Response(Speaker=0,Subject=0, Step=1, B=0, B2=0, Tempmod=0, Result=0, Approval = 0):
        #Dialog for responses to Lesbian scenes, Speaker is typically Partner to the lead girl. Step is the phase of the conversation
        # call Les_Response(RogueX,1)
        # call Les_Response(KittyX,RogueX,1) 
        if Speaker not in TotalGirls:
                $ Speaker = Partner
        if Subject not in TotalGirls:
                $ Subject = Ch_Focus
            
        if Speaker == EmmaX:
                #if Emma's not open to public sex yet, bailout
                if "three" not in EmmaX.History or "classcaught" not in EmmaX.History or (Taboo > 20 and "taboo" not in EmmaX.History): 
                    $ EmmaX.RecentActions.append("no lesbian")                      
                    $ EmmaX.DailyActions.append("no lesbian") 
                    $ EmmaX.Statup("Obed", 70, 5)
                    $ EmmaX.Statup("Inbt", 80, 5) 
                    $ EmmaX.Statup("Lust", 50, 10)
                    $ Speaker.FaceChange("sadside", 1)
                    "[EmmaX.Name] looks around furtively."
                    ch_e "I can't imagine why you would think I would engage in such behavior with a student!"            
                    call Remove_Girl(EmmaX)
                    "She quickly leaves the room."
                    return 0                
                
        if Speaker.Les:
                $ Tempmod += 10
        if Speaker.SEXP >= 50:
                $ Tempmod += 25
        elif Speaker.SEXP >= 30:
                $ Tempmod += 15
        elif Speaker.SEXP >= 15:
                $ Tempmod += 5
                    
        elif Speaker.Inbt >= 750:
                $ Tempmod += 5
            
        if "exhibitionist" in Speaker.Traits:      
                $ Tempmod += (3*Taboo) 
            
        if "dating" in Speaker.Traits or "sex friend" in Speaker.Petnames:
                $ Tempmod += 10        
        elif "ex" in Speaker.Traits:
                $ Tempmod -= 40  
            
        # Provides a bonus based on how much the speaker likes the subject girl
        if Speaker.GirlLikeCheck(Subject) >= 900:                    
                $ B += 150
        elif Speaker.GirlLikeCheck(Subject) >= 800 or "poly " + Subject.Tag in Speaker.Traits:
                $ B += 100
        elif Speaker.GirlLikeCheck(Subject) >= 700:
                $ B += 50
        elif Speaker.GirlLikeCheck(Subject) <= 200:
                $ B -= 200
        elif Speaker.GirlLikeCheck(Subject) <= 500:
                $ B -= 100
                
        $ Approval = ApprovalCheck(Speaker, 1300, TabM = 2, Bonus = B) # 1300, 1450, 1600, Taboo -800
        
        if not Approval:
                #if there's no chance, skip to the end
                pass
        elif Step == 1:
                #this is if the first girl's check failed, but the speaking girl likes her.
                if Approval >= 2 or B >= 150:
                        $ Speaker.FaceChange("sexy", 1)
                        if Speaker == RogueX:
                                ch_r "You sure [Subject.Tag]? Could be a lot of fun?"
                        elif Speaker == KittyX:
                                ch_k "Come on [Subject.Tag], it could be kinda fun."
                        elif Speaker == EmmaX:
                                ch_e "Oh come on [Subject.Tag], I could show you a few things."
                        elif Speaker == LauraX:       
                                ch_l "It's really not bad, give it a shot."
                        if B2 >= 100:
                                $ Result = 1                        
                                $ Speaker.GirlLikeUp(Subject,(int(B/10)))
                                $ Subject.GirlLikeUp(Speaker,(int(B2/10))) #B2 sent by the call. . .
                else:
                        return Result
        
        elif Step == 2:
            #this is the second step, usually in the Prep phase
            if Approval >= 2:
                    $ Speaker.FaceChange("smile", 1)
                    if Speaker == RogueX:
                            ch_r "'Course!"
                    elif Speaker == KittyX:
                            ch_k "'Course!"
                    elif Speaker == EmmaX:
                            ch_e "Of course, [Speaker.Petname]."
                    elif Speaker == LauraX:       
                            ch_l "I'm in."
                    $ Result = 1
                    return Result
            #if Approval, but not 2
            $ Speaker.FaceChange("sly", 2)
            if Speaker == RogueX:
                    if B >= 100:
                            ch_r "I don't know, maybe. . ."
                    if B >= 0:
                            ch_r "I'm not sure about her though. . ."
            elif Speaker == KittyX:
                    if B >= 100:
                            ch_k "Yeah, I mean I guess. . ."
                    if B >= 0:
                            ch_k "No offense [Subject.Tag], but. . ."
            elif Speaker == EmmaX:
                    if B >= 100:
                            ch_e "Mmmmm, certainly. . ."
                    if B >= 0:
                            ch_e "[Subject.Tag], dear, I don't really think so. . ."
            elif Speaker == LauraX:        
                    if B >= 100:
                            ch_l "You're cute and all. . ."
                    if B >= 0:
                            ch_l "I don't know, [Subject.Tag]. . ."
            $ Speaker.Blush = 1
            menu:
                extend ""
                "Ok, that's fine. . .":
                        if B >= 100:     
                                if Speaker == RogueX:   
                                        ch_r "Never mind, I'm in."
                                elif Speaker == KittyX:      
                                        ch_k "No, no, let's do this."
                                elif Speaker == EmmaX:                       
                                        ch_e "Oh, don't back out now. . ."
                                elif Speaker == LauraX:                                
                                        ch_l "Oh, no, I'm in."
                                $ Result = 1
                        else:      
                                $ Speaker.FaceChange("smile")
                                if Speaker == RogueX:
                                        ch_r "Thanks, I appreciate it."
                                elif Speaker == KittyX:
                                        ch_k "Thanks, I appreciate it."
                                elif Speaker == EmmaX:
                                        ch_e "I appreciate your restraint."
                                elif Speaker == LauraX:        
                                        ch_l "Yeah. . ."
                "Come on, you might enjoy it. . .":
                        if B >= 50:
                                if Speaker == RogueX:
                                        ch_r "Well, I suppose." 
                                elif Speaker == KittyX:
                                        ch_k "I mean, maybe?" 
                                elif Speaker == EmmaX:
                                        ch_e "I'm sure I would. . ." 
                                elif Speaker == LauraX:      
                                        ch_l "Maybe. .. " 
                                $ Result = 1
                        else:
                                $ Speaker.FaceChange("sad", 2)
                                if Speaker == RogueX:
                                        ch_r "I don't think so." 
                                elif Speaker == KittyX:
                                        ch_k "Probably not." 
                                elif Speaker == EmmaX:
                                        ch_e "Probably not." 
                                elif Speaker == LauraX:      
                                        ch_l "I doubt it." 
                "Get in there, now.":
                        if ApprovalCheck(Speaker, 550, "OI", TabM = 2):
                                $ Speaker.FaceChange("sadside", 1)
                                if Speaker == RogueX:
                                        ch_r "Fine, whatever."
                                elif Speaker == KittyX:
                                        ch_k "Fiiine." 
                                elif Speaker == EmmaX:
                                        ch_e "Oh, fine."
                                elif Speaker == LauraX:        
                                        ch_l "Fine."
                                $ Result = 1
                        else:
                                $ Speaker.FaceChange("angry")
                                if Speaker == RogueX:
                                        ch_r "Who do you think you're talk'in to?"  
                                elif Speaker == KittyX:
                                        ch_k "You're not the boss of me!"
                                elif Speaker == EmmaX:
                                        ch_e "Don't forget who's in charge here, [Speaker.Petname]"  
                                elif Speaker == LauraX:    
                                        ch_l "Don't push me."  
                                $ Speaker.AddWord(1,"angry","angry") # adds to daily and recent
                "[Subject.Name], what do you think?":
                        $ Subject.FaceChange("sexy", 1)                                    
                        $ Speaker.GirlLikeUp(Subject,(int(B/10)))
                        if B >= 50:
                                $ Subject.GirlLikeUp(Speaker,5)                                    
                        if Subject == RogueX:                                        
                                if Speaker == KittyX:
                                    if Subject.Les and Speaker.Les:
                                            ch_r "You know that we work well together."
                                    else:
                                            ch_r "It could be a lot of fun."
                                elif Speaker == EmmaX:
                                    if Subject.Les and Speaker.Les:
                                            ch_r "You could do that thing from last time. . ."
                                    else:
                                            ch_r "I was hoping you could give me some after class lessons. . ."
                                else:
                                    if Subject.Les and Speaker.Les:
                                            ch_r "Oh, it's not that bad."
                                    else:
                                            ch_r "It could be a lot of fun."                                        
                        elif Subject == KittyX:
                                if Speaker == RogueX:
                                    if Subject.Les and Speaker.Les:
                                            ch_k "Come on [Speaker.Tag], you know we have fun."
                                    else:
                                            ch_k "Come on [Speaker.Tag], could be fun."                                        
                                elif Speaker == EmmaX:
                                    if Subject.Les and Speaker.Les:
                                            ch_k "I mean, it might be nice to show [Subject.Petname] what you've taught me. . ."
                                    else:
                                            ch_k "I've seen you watching me in class. . ."
                                else:
                                    if Subject.Les and Speaker.Les:
                                            ch_k "We have so much fun together though."
                                    else:
                                            ch_k "It could be fun!"                                        
                        elif Subject == EmmaX:
                                if Subject.Les and Speaker.Les:
                                    ch_e "What's the matter [Speaker.Name], too shy around [Player.Name]?"
                                else:
                                    ch_e "What's the matter [Speaker.Name], I've seen how you look at me. . ."                                     
                        elif Subject == LauraX:                                        
                                if Speaker == EmmaX:
                                    if Subject.Les and Speaker.Les:
                                            ch_l "Wow, you aren't this shy when [Subject.Petname]'s not around."
                                    else:
                                            ch_l "Come on, you look really squishy."
                                else:
                                    if Subject.Les and Speaker.Les:
                                            ch_l "What, you don't want to fuck with [Player.Name] around?"
                                    else:
                                            ch_l "Come on, you look like you have it in you."
                        #end dialogs from if you asked the other girl waht she thought. . .
                        #then the speaker responds. . .
                        if B >= 50:
                                #Yes
                                $ Speaker.FaceChange("smile", 1)                                
                                if Speaker == RogueX:
                                        ch_r "You know, I can't argue with that, [Subject.Tag]."
                                elif Speaker == KittyX:
                                        ch_k "Heh, I guess so, [Subject.Tag]."
                                elif Speaker == EmmaX:
                                        ch_e "If we must, [Subject.Tag]."
                                elif Speaker == LauraX:    
                                        ch_l "I guess so."
                                $ Result = 1
                        else:
                                #No
                                $ Speaker.FaceChange("angry", 1, Eyes="side")
                                if Speaker == RogueX:
                                        ch_r "Sorry [Subject.Tag], nothin personal."
                                elif Speaker == KittyX:
                                        ch_k "Sorry [Subject.Tag], I don't mean anything personal."
                                elif Speaker == EmmaX:
                                        ch_e "I'm sorry [Subject.Tag], it's really not you."
                                elif Speaker == LauraX:    
                                        ch_l "Sorry [Subject.Tag], it's not about you."
                #end dialogs from if you asked the other girl waht she thought. . .
        if Step == 3:
                #This is a check if you interrupted them and Primary wants to do it, does Secondary?
                if Approval:
                        $ Speaker.FaceChange("smile", 1)
                        if Speaker == RogueX:
                                ch_r "I mean, I guess so. . ."
                        elif Speaker == KittyX:
                                ch_k "I mean, I guess. . ."
                        elif Speaker == EmmaX:
                                ch_e "How could I back out now?"
                        elif Speaker == LauraX:    
                                ch_l "Yeah. . ."
                        $ Result = 1
                else:
                        $ Speaker.FaceChange("sadside", 1)
                        if Speaker == RogueX:
                                ch_r "I'm really not into that right now. . ."
                        elif Speaker == KittyX:
                                ch_k "I'm really not into it atm. . ."
                        elif Speaker == EmmaX:
                                ch_e "I'm afraid not. . ."
                        elif Speaker == LauraX:    
                                ch_l "Not right now. . ."
        if not Result:        
                #response if all falls through and it fails. . .
                $ Speaker.RecentActions.append("no lesbian")                      
                $ Speaker.DailyActions.append("no lesbian") 
                $ Speaker.FaceChange("sadside", 1)    
                $ Partner = 0
                if Speaker == RogueX:
                        if B <= 0:
                                ch_r "Sorry, [Speaker.Petname], it's just not like that with her."
                        if Taboo:
                                ch_r "Sorry, [Speaker.Petname], this isn't a good place for it."
                        if B >= 100:
                                ch_r "Sorry, [Speaker.Petname], maybe if you weren't around. . ."
                        else:
                                ch_r "Sorry, [Speaker.Petname], I'm just not interested."
                elif Speaker == KittyX:
                        if B <= 0:
                                ch_k "Sorry, [Speaker.Petname], I'm just not into her."
                        if Taboo:
                                ch_k "Sorry, [Speaker.Petname], this isn't exactly the right place for that."
                        if B >= 100:
                                ch_k "Sorry, [Speaker.Petname], not with you watching. . ."
                        else:
                                ch_k "Sorry, [Speaker.Petname], I'm just not into it."
                elif Speaker == EmmaX:
                        if B <= 0:
                                ch_e "I'm sorry, [Speaker.Petname], she's just not my type."
                        if Taboo:
                                ch_e "I'm sorry, [Speaker.Petname], this would cause a scandal."
                        if B >= 100:
                                ch_e "I'm sorry, [Speaker.Petname], not with an audience. . ."
                        else:
                                ch_e "I'm sorry, [Speaker.Petname], I'm just not interested in that."
                elif Speaker == LauraX:    
                        if B <= 0:
                                ch_l "Sorry, [Speaker.Petname], she's not my type."
                        if Taboo > 20:
                                ch_l "Sorry, [Speaker.Petname], this area's a bit exposed."
                        if B >= 100:
                                ch_l "Sorry, [Speaker.Petname], I don't want an audience. . ."
                        else:
                                ch_l "Sorry, [Speaker.Petname], I'm just not into that."
        # end failure text
                
        return Result
        
#End Girl.Les_Response >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >

label Les_FirstKiss:
        # called when there is a first kiss situation between two girls
        if "les " + Partner.Tag in Girl.History:
                #if they've been together before              
                $ Line = "experienced"
        elif Girl.Les and Partner.Les:   
                #if both have kissed girls before
                $ Line = "first both"
        elif Girl.Les:
                # Girl's had experience              
                $ Line = "first girl"
        elif Partner.Les:
                #Partner's had experience                
                $ Line = "first partner"
                   
        if Line == "experienced":
                "[Girl.Name] and [Partner.Name] move together in a passionate kiss."
                "[Girl.Name]'s arms firmly grasp [Partner.Name]'s neck and pull her close."
        else:
                if Line in ("first both", "first girl"):
                        # Girl's first time
                        "[Girl.Name] slowly moves in and gives [Partner.Name] a soft kiss."
                else:
                        #not Girl's first time
                        "[Girl.Name] casually places a hand on the back of [Partner.Name]'s head and draws their lips together."
                if Line == "first partner":
                        #other girl's first time
                        "[Partner.Name] pulls back a bit, but slowly leans into the enbrace."
                else:
                        #not other girl's first time
                        "[Partner.Name]'s lips curl up into a smile and she draws [Girl.Name] even closer."                    
                "After a few seconds, it begins to grow more passionate."
        return
#End Girl.Les_Response >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >


# Start Les activity change  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Les_Change(Primary = 0, Secondary=Partner, D20S=0, PrimaryLust=0, SecondaryLust=0): #nee (D20S=0, Secondary=Partner, Primary = "Rogue", PrimaryLust=0, SecondaryLust=0):
        # for Lesbian primary activity: Threeway_Set(Primary,"preset", "lesbian", Trigger3, ActiveGirl)
        #this is called when the player wants to change over a lesbian T3 behavior.
        # call Les_Change(RogueX)
        if Primary not in TotalGirls:
                return
        $ Line = 0
        menu:
            "Hey [Primary.Name]. . ."
            "why don't you kiss her?" if Trigger5 != "kiss girl" and Trigger5 != "kiss both":
                        call Threeway_Set(Primary,"kiss girl", "lesbian", Trigger3,Secondary)
            "why don't you grab her tits?" if Trigger3 != "fondle breasts":
                        call Threeway_Set(Primary,"fondle breasts", "lesbian", Trigger3,Secondary)
            "why don't you suck her breasts?" if Trigger3 != "suck breasts":
                        call Threeway_Set(Primary,"suck breasts", "lesbian", Trigger3,Secondary)
            "why don't you finger her?" if Trigger3 != "fondle pussy":
                        call Threeway_Set(Primary,"fondle pussy", "lesbian", Trigger3,Secondary)
            "why don't you go down on her?" if Trigger3 != "lick pussy":
                        call Threeway_Set(Primary,"lick pussy", "lesbian", Trigger3,Secondary)
            "why don't you grab her ass?" if Trigger3 != "fondle ass":
                        call Threeway_Set(Primary,"fondle ass", "lesbian", Trigger3,Secondary)
            "why don't you lick her ass?" if Trigger3 != "lick ass":
                        call Threeway_Set(Primary,"lick ass", "lesbian", Trigger3,Secondary) 
            "never mind.":
                pass
        if not Line:
            $ Line = "You return to what you were doing." 
        else:
            $ Situation = "skip"
        "[Line]"
        return
# End Les activity change  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /