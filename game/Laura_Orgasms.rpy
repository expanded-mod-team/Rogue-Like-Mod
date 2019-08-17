# Start You Cumming //////////////////////////////////////////////////////////////////////////////////

label PL_Cumming:
    call Shift_Focus("Laura")
            
    if Trigger == "blow":
            $ Tempmod += 5
        
    if L_Addict > 75:
            $ Tempmod += 20
    elif L_Addict > 50:
            $ Tempmod += 5
    
    if L_Swallow >= 10:
            $ Tempmod += 15  
    elif L_Swallow >= 3:
            $ Tempmod += 5
        
    if (L_CreamP + L_CreamA) >= 10:
            $ Tempmod += 15 
    elif (L_CreamP + L_CreamA) >= 3:
            $ Tempmod += 5             
       
    $ D20 = renpy.random.randint(1, 20) 
    
# intro lines    
    if Trigger == "hand":
            $ Line = "As she strokes, you're about ready to come. . ."
    elif Trigger == "blow":
            $ Line = "As she sucks at you, you start to feel about to come. . ."
    elif Trigger == "titjob":
            $ Line = "As you rub into her cleavage, you start to feel about to come. . ."
    elif Trigger == "sex" or Trigger == "anal":
            $ Line = "As you thrust into her, you feel about to blow. . ."
    elif Trigger == "hotdog":
            $ Line = "As you grind into her, you feel about to blow. . ."
    else:        
            $ Line = "You start to feel about to come. . ."    
    
    call LauraFace("sexy") 
    
    menu:
        "[Line]"
        "Warn her":
                $ Situation = "warn"
#                jump L_No_Cum           #fix, temporary
                jump L_Warn_Her
            
        "Ask to cum in her mouth": 
                $ Situation = "asked"
#                jump L_No_Cum           #fix, temporary
                jump L_In_Mouth                            
        "Cum in her mouth without asking" if Trigger == "blow" or Trigger == "hand" or Trigger == "titjob":
                $ Situation = "auto"
#                jump L_No_Cum           #fix, temporary
                jump L_In_Mouth
        
        "Ask to cum inside her" if Trigger == "sex":
                $ Situation = "asked"
                jump L_Creampie_P        
        "Ask to cum inside her" if Trigger == "anal":
                $ Situation = "asked"
                jump L_Creampie_A
                
        "Cum inside her" if Trigger == "sex":
                $ Situation = "auto"
                jump L_Creampie_P        
        "Cum inside her" if Trigger == "anal":
                $ Situation = "auto"
                jump L_Creampie_A
            
        "Cum on her face":
#                jump L_No_Cum           #fix, temporary
                jump L_Facial   
                
        "Cum on her tits":
#                jump L_No_Cum           #fix, temporary
                jump L_TitSpunk   
                
        "Cum on her belly" if Trigger == "sex" or Trigger == "anal" or Trigger == "hotdog":
                jump L_SpunkBelly
            
        "Pull back":
            if renpy.showing("Laura_BJ_Animation"):
                    if L_Addict >= 60 and ApprovalCheck("Laura", 1000, "I", Bonus = ((L_Addict*10)- L_Obed)) and L_Swallow:
                            $ L_Eyes = "manic"
                            call Speed_Shift(0)
                            "You pull out of her mouth with a pop, and her eyes widen in surprise."
                            $ L_Mouth = "sucking"
                            $ L_Spunk.append("mouth")
                            $ L_Spunk.append("chin")
                            call Speed_Shift(4)
                            "She leaps at your cock and sucks it deep, draining your fluids hungrily." 
                            call Speed_Shift(0)
                            $ L_Mouth = "lipbite"
                            "When she finishes, she draws her hand across her lips."
                            call LauraFace("bemused")
                            ch_l "Sorry, [L_Petname], but I couldn't let that go to waste."
                            call Statup("Laura", "Obed", 200, -5)
                            call Statup("Laura", "Inbt", 200, 10)
                            jump L_Swallowed                            
                    call Laura_BJ_Reset                
            elif renpy.showing("Laura_HJ_Animation"):
                    call Laura_HJ_Reset                
            elif renpy.showing("Laura_TJ_Animation"):
                    call Laura_TJ_Reset               
            elif renpy.showing("Laura_SexSprite"):
                    call Laura_Sex_Reset  
            if ApprovalCheck("Laura", 500, "I", Bonus = ((L_Addict*10)- L_Obed)) and L_Addict > 50 and L_Swallow: #If addict + Inbt is > obedience + 50. . .
                    $ L_Eyes = "manic"
                    $ L_Mouth = "kiss"
                    call Speed_Shift(0)
                    "Her eyes widen in panic."
                    ch_l "You wouldn't reconsider, [L_Petname]?" 
                    $ L_Blush = 2
                    menu:
                        extend ""
                        "Ok, if you'll swallow it.":
                                if Trigger != "blow": 
                                    call Laura_BJ_Launch("cum")
                                call LauraFace("sucking") 
                                call Speed_Shift(4)
                                "She nods and puts the tip into her mouth. as you release she gulps it down hungrily."
                                call LauraFace("sexy")                      
                                $ L_Mouth = "sucking"
                                $ L_Spunk.append("mouth")
                                $ L_Spunk.append("chin")
                                ". . ."
                                call Speed_Shift(0)
                                call LauraFace("sad")                       
                                $ L_Mouth = "lipbite"
                                ch_l "Yum."  
                                call Statup("Laura", "Obed", 50, 2)
                                call Statup("Laura", "Obed", 70, 1)
                                call Statup("Laura", "Inbt", 30, 2)
                                call Statup("Laura", "Inbt", 50, 3)
                                jump L_Swallowed                                
                        "No, we're done for now.": #If addict is > obedience + 50. . .
                                if ApprovalCheck("Laura", 250, "I", Bonus = ((L_Addict*10)- L_Obed)) or L_Addict > 75:                            
                                        call Statup("Laura", "Obed", 50, -1)
                                        call Statup("Laura", "Obed", 70, -2)
                                        call Statup("Laura", "Inbt", 30, 2)
                                        call Statup("Laura", "Inbt", 70, 3)
                                        if Trigger != "blow":
                                            call Laura_BJ_Launch("cum")
                                            call Speed_Shift(4)
                                        "She dives down on you and you can't resist filling her throat."
                                        call Speed_Shift(0)
                                        ch_l "Now we are."
                                        jump L_Swallowed                                
                                else:                         
                                        call Statup("Laura", "Obed", 30, 3)
                                        call Statup("Laura", "Obed", 70, 5)
                                        call LauraFace("sad")
                                        $ L_Brows = "confused"
                                        ch_l "Dick."
                                        $ Line = 0
                                        $ P_Focus -= 5
                                        return  
                    #manic, wanted to swallow
                    
            call LauraFace("sexy", 1)
            call Statup("Laura", "Obed", 50, 2)
            "You pull pull back away from her. She looks up at you and licks her lips." 
            ch_l "So now what?"
            $ Line = 0
            $ P_Focus = 95
            return
            #end "pull back"
#End Main orgasm menu

label L_No_Cum:
        #this is a temporary thing until this system is complete
        call LauraFace("confused", Mouth="smirk") 
        if Situation == "warn":
            ch_p "I'm about to. . . blow. . ."
            ch_l "Oh? Cool."
        elif Situation == "asked":        
            ch_p "I'm about to. . . blow. . ."
            ch_p "Could I. . . come in your mouth?"
            ch_l "Hmmm, I don't think so."
        else:
            ch_l "Not so fast, [L_Petname]."         
        if not renpy.showing("Laura_HJ_Animation"):
            $ Laura_Arms = 2
        call LauraFace("sly",1) 
        ch_l "For now just come in my hand here. . ."
        $ L_Spunk.append("hand") 
        "She grabs the head of your cock and you gush into it."
        ch_l "Bit of a mess. . ."         
        jump L_Orgasm_After


label L_Warn_Her:            
        "You let her know that you're going to come."
        call Statup("Laura", "Love", 90, 3)
        if L_Obed >= 500:
                call Statup("Laura", "Obed", 80, 5)
        if "hungry" in L_Traits and D20 >= 5:
                if renpy.showing("Laura_SexSprite"):
                    call Laura_BJ_Launch("cum")   
                    "She grins and pulls out with a pop, and begins to suck you off."
                call Speed_Shift(4)
                call LauraFace("sucking")       
                ". . ."
                call Speed_Shift(0)
                $ L_Spunk.append("mouth")
                $ L_Spunk.append("chin")
                if not renpy.showing("Laura_BJ_Animation"):
                    "She smiles and then puts your tip in her mouth. When you finish filling her mouth, she quickly gulps it down and wipes her lips."
                else:                    
                    "She makes a little humming sound, but keeps sucking. When you finish filling her mouth, she quickly gulps it down and wipes her lips."        
                call LauraFace("sexy")
                $ L_Mouth = "smile"
                ch_l "Yum, thanks for the heads up."     
                jump L_Swallowed
        #End Hungy take-over
            
        if Trigger == "sex" and L_CreamP >= 5: 
                # She's Creampied a few times
                call LauraFace("sexy")
                $ P_Cock = "in"
                $ L_Spunk.append("in")
                $ P_Spunk = "in"
                call Speed_Shift(4)
                "She smiles and speeds up her actions, causing you to erupt inside her."   
                if L_Lust >= 85: 
                    call L_Cumming  
                jump L_Creampied
        
        elif Trigger == "sex" and L_CreamP and D20 >= 10:  
                # She's Creampied at least once
                call LauraFace("sly")
                $ P_Cock = "in"
                $ L_Spunk.append("in")
                $ P_Spunk = "in"
                call Speed_Shift(4)
                "She gets a michevious look and speeds up, you burst inside her."          
                if L_Lust >= 85: 
                    call L_Cumming  
                jump L_Creampied
            
        elif Trigger == "anal" and L_CreamA >= 5: 
                # She's Anal Creampied a few times
                call LauraFace("sexy")
                $ P_Cock = "anal"
                $ L_Spunk.append("anal")
                $ P_Spunk = "anal"
                call Speed_Shift(4)
                "She smiles and speeds up her actions, causing you to erupt inside her."         
                if L_Lust >= 85: 
                    call L_Cumming  
                jump L_Creampied
        
        elif Trigger == "anal" and L_CreamA and D20 >= 10: 
                # She's Anal Creampied at least once
                call LauraFace("sly")
                $ P_Cock = "anal"
                $ L_Spunk.append("anal")
                $ P_Spunk = "anal"
                call Speed_Shift(4)
                "She gets a michevious look and speeds up, you burst inside her."    
                if L_Lust >= 85: 
                    call L_Cumming          
                jump L_Creampied
            
        elif Trigger != "anal" and L_Swallow >= 5: 
                #If she's swallowed a lot     
                if renpy.showing("Laura_TJ_Animation"):  
                        if L_Blow >= 5 or Speed >= 3:          
                                call LauraFace("tongue")
                                call Speed_Shift(5) #shallow animation
                                $ L_Spunk.append("mouth")
                                $ L_Spunk.append("chin")
                                "She makes a little humming sound, but keeps sucking."
                        else: 
                                jump L_Facial
                elif renpy.showing("Laura_BJ_Animation"):            
                        call LauraFace("sucking")
                        $ L_Spunk.append("mouth")
                        $ L_Spunk.append("chin")
                        if Speed == 4: #6 if deep throating, 5 if not
                                call Speed_Shift(6)
                        else:
                                call Speed_Shift(5)
                        "She makes a little humming sound, but keeps sucking."
                        call Speed_Shift(0)
                        "When you finish filling her mouth, she quickly gulps it down and wipes her lips."
                else:
                        call Laura_BJ_Launch("cum")
                        call Speed_Shift(2)
                        call LauraFace("sucking")
                        $ L_Spunk.append("mouth")
                        $ L_Spunk.append("chin")
                        "She smiles and then puts your tip in her mouth."
                        call Speed_Shift(5)
                        "When you finish filling her mouth, she quickly gulps it down and wipes her lips."                
                call Speed_Shift(0)
                call LauraFace("sexy")
                $ L_Mouth = "smile"
                ch_l "Yum, thanks for the heads up."  
                jump L_Swallowed
            
        elif L_Swallow and D20 >= 10:  
                #She's swallowed before, but not a lot  
                if renpy.showing("Laura_SexSprite"):
                    call Laura_HJ_Launch("cum") 
                    "She grins and pulls out with a pop, and begins to stroke you off."
                call Speed_Shift(2)
                if renpy.showing("Laura_TJ_Animation") or renpy.showing("Laura_BJ_Animation"): 
                    if renpy.showing("Laura_TJ_Animation"): 
                        if L_Blow >= 5 or Speed >= 3:          
                                call LauraFace("tongue")
                                call Speed_Shift(5) #shallow animation
                                $ L_Spunk.append("mouth")
                                $ L_Spunk.append("chin")
                        else: 
                                jump L_Facial
                    elif renpy.showing("Laura_BJ_Animation"): 
                            #if she's blowing
                            call LauraFace("sucking")
                            $ L_Spunk.append("mouth")
                            $ L_Spunk.append("chin")
                    if Speed == 4: #6 if deep throating, 5 if not
                            call Speed_Shift(6)
                    else:
                            call Speed_Shift(5)
                    "She makes a little humming sound, but keeps sucking."
                    "When you finish filling her mouth, she gags a little, but manages to swallow it."
                    call Speed_Shift(0)
                    call LauraFace("sexy")
                    $ L_Mouth = "smile"
                    if L_Addict > 50:
                            $ L_Eyes = "manic"
                            "She gulps it down hungrily and licks her lips."
                    call LauraFace("bemused")
                    ch_l "Hmm. . . an intense taste, thanks for the heads up."
                    jump L_Swallowed                    
                    #fix, add titjob option here.   
                else:
                        #If she's handying
                        jump L_Handy_Finish    
        #end if she's swallowed        
            
        elif ApprovalCheck("Laura", 1000):                    
                #warned but likes you and experienced
                if L_SEXP > 20 and renpy.showing("Laura_SexSprite"):
                        "She gently pushes you back off of her."
                        jump L_SpunkBelly
                elif L_SEXP > 20:
                        jump L_Facial            
        
                if renpy.showing("Laura_HJ_Animation") and L_Hand:
                        jump L_Handy_Finish
                elif renpy.showing("Laura_BJ_Animation") and L_Blow:
                        jump L_Handy_Finish
                elif renpy.showing("Laura_TJ_Animation") and L_Tit:
                        jump L_TitSpunk
                elif renpy.showing("Laura_SexSprite") and L_Sex and Trigger == "sex":
                        "She gently pushes you back off of her."
                        jump L_SpunkBelly
                elif renpy.showing("Laura_SexSprite") and L_Anal and Trigger == "anal":
                        "She gently pushes you back off of her."
                        jump L_SpunkBelly
                
        # Else. . . not experienced or she's not a huge fan, 
        if Trigger == "sex" or Trigger == "anal":
                call Laura_Sex_Reset
                "She pulls off of you and grabs your cock in her hand."
                jump L_Handy_Finish
        elif renpy.showing("Laura_TJ_Animation"):#hotdogging
                "She smiles and starts rubbing against you a bit faster."
                jump L_TitSpunk
        elif renpy.showing("Laura_SexSprite"):#hotdogging
                "She smiles and starts rubbing against you a bit faster."
                jump L_SpunkBelly
        else:
                jump L_Handy_Finish
    #End "Warn her" / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    
                      
                      
#Cum in mouth start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label L_In_Mouth:      
            
    if Trigger == "anal":
            $ Tempmod -= 15
    if "hungry" not in L_Traits and L_Addict <= 50 and "full" in L_RecentActions:
            $ Tempmod -= 15                  
                
    if Situation == "auto":
                $ Situation = 0
                if renpy.showing("Laura_TJ_Animation"):         
                        call LauraFace("tongue")
                elif not renpy.showing("Laura_BJ_Animation"):
                        call Laura_BJ_Launch("cum")
                $ L_Eyes = "down"
                if Speed == 4: #6 if deep throating, 5 if not
                        call Speed_Shift(6)
                else:
                        call Speed_Shift(5)
                "You grab her head and cum in her mouth"  
                $L_Eyes = "closed"      
                if renpy.showing("Laura_TJ_Animation"): 
                        show Laura_TJ_Animation
                        with vpunch
                else:
                        show Laura_BJ_Animation
                        with vpunch
                if "full" in L_RecentActions:
                        #if she's had enough
                        call LauraFace("bemused")
                        $ L_Spunk.append("mouth")
                        $ L_Spunk.append("chin")
                        call Speed_Shift(0)
                        "She gags a little, but manages to swallow it."
                        $ L_Spunk.remove("mouth")
                        ch_l "Hmm. . . I'm kinda full. . ."
                        ch_l "Maybe keep it outside. . ."
                elif L_Swallow >= 5 or "hungry" in L_Traits:
                        #if she likes to swallow
                        call LauraFace("sexy")
                        $ L_Mouth = "smile"
                        $ L_Spunk.append("mouth")
                        $ L_Spunk.append("chin")
                        "She quickly gulps it down and wipes her mouth."
                        $ L_Spunk.remove("mouth")
                        call Speed_Shift(0)
                        ch_l "Yum."
                        call LauraFace
                elif L_Swallow:
                        call LauraFace("bemused")
                        $ L_Spunk.append("mouth")
                        $ L_Spunk.append("chin")
                        call Speed_Shift(0)
                        "She gags a little, but manages to swallow it."
                        $ L_Spunk.remove("mouth")
                        ch_l "Your. . . flavor is. . . distinct, but maybe a heads up?"
                        call LauraFace
                elif not L_Swallow and L_Addict >= 50 and L_Inbt < 400 and L_Blow < 10:
                        call LauraFace("bemused", 1)
                        $ L_Spunk.append("mouth")
                        $ L_Spunk.append("chin")
                        ". . ."            
                        $ L_Spunk.remove("mouth")
                        $ L_Spunk.append("hand")
                        call Speed_Shift(0)
                        "She gags and spits it into her palm. Then she licks her lips, looks down at her dripping hand, blushes, and quickly wipes it off."
                        $ L_Spunk.remove("hand")
                        ch_l "That certainly is. . . intense. . ."
                        $ L_Addictionrate += 1
                        if "addictive" in P_Traits:
                            $ L_Addictionrate += 1
                        call LauraFace
                        jump L_Orgasm_After
                elif not L_Swallow and L_Addict >= 50:
                        call LauraFace("sexy")
                        $ L_Mouth = "tongue"
                        $ L_Spunk.append("mouth")
                        $ L_Spunk.append("chin")
                        ". . ."
                        $ L_Spunk.remove("mouth")
                        $ L_Spunk.append("hand")
                        call Speed_Shift(0)
                        "She gags and spits it into her palm. Then she licks her lips, looks down, and drinks up what's in her palm."
                        $ L_Spunk.remove("hand")
                        ch_l "I should be mad, but. . ."
                        call LauraFace
                        call Statup("Laura", "Inbt", 30, 2)
                        call Statup("Laura", "Inbt", 50, 2)
                elif not L_Swallow:
                        if ApprovalCheck("Laura", 800, "LI") and ApprovalCheck("Laura", 400, "OI"):
                            call LauraFace("angry")
                        else:
                            call LauraFace("bemused")
                            $ L_Mouth = "tongue"
                        $ L_Spunk.append("mouth")
                        $ L_Spunk.append("chin")
                        ". . ."
                        $ L_Spunk.append("hand")
                        call Speed_Shift(0)
                        "She gags and spits it into her palm."   
                        menu:
                            ch_l "What's the deal just cumming in my mouth like that?"
                            "Sorry about that.":
                                    call Statup("Laura", "Love", 80, 1)
                                    $ L_Addictionrate += 1
                                    if "addictive" in P_Traits:
                                        $ L_Addictionrate += 1
                                    call LauraFace("smile", 1)
                                    ch_l "Fine. . ."
                                    ch_l "Just warn me next time. . ."
                                    jump L_Orgasm_After
                                
                            "Why don't you try swallowing it?":
                                    if ApprovalCheck("Laura", 1200):
                                        "She tentatively licks her hand, and then gulps it down."
                                        $ L_Spunk.remove("hand")
                                        call LauraFace("sexy", 1)
                                        $ L_Spunk.append("mouth")
                                        ch_l "Wasn't that bad. . ."
                                        call Statup("Laura", "Obed", 50, 10)
                                        $ L_Spunk.remove("mouth")
                                    elif ApprovalCheck("Laura", 1200, "OI", Bonus = (L_Addict*10)):
                                        call LauraFace("bemused", 1)
                                        $ L_Brows = "normal" 
                                        $ L_Mouth = "sad"
                                        $ L_Spunk.remove("hand")
                                        $ L_Spunk.append("mouth")
                                        "She scowls a bit, but licks her hand clean as she does so, and swallows it down."
                                        $ L_Spunk.remove("mouth")
                                        ch_l "Not my favorite flavor. . ."
                                        call Statup("Laura", "Obed", 50, 10)
                                    else:
                                        $ L_Spunk.remove("hand")
                                        "She scowls at you and wipes her hand off. Then she licks her lips."
                                        jump L_Orgasm_After
                                    
                            "Swallow it, now.":
                                    call Statup("Laura", "Love", 30, -1, 1)
                                    call Statup("Laura", "Love", 50, -1, 1)                    
                                    call Statup("Laura", "Love", 80, -1, 1)
                                    if ApprovalCheck("Laura", 1200, "OI") or L_Addict >= 50:                            
                                        call LauraFace("sad", 1)
                                        $ L_Spunk.append("mouth")
                                        $ L_Spunk.remove("hand")
                                        "She scowls a bit, but licks her hand clean as she does so, and swallows it down."
                                        $ L_Spunk.remove("mouth")
                                        ch_l "Not my favorite flavor. . ."
                                        call Statup("Laura", "Obed", 50, 10)
                                    else:         
                                        $ L_Spunk.remove("hand")               
                                        "She scowls at you and wipes her hand off. Then she licks her lips."                        
                                        jump L_Orgasm_After
                else:                
                            jump L_Orgasm_After
                                
                jump L_Swallowed
                #end if not asked/auto / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
    
    $ Situation = 0
    "You ask if you can cum in her mouth."
    if renpy.showing("Laura_SexSprite"):
            call Laura_HJ_Launch("cum")
        
    if "full" in L_RecentActions:
            pass
        
    elif L_Swallow >= 5 or "hungry" in L_Traits:  
            # If she's swallowed 5 times, 
            if renpy.showing("Laura_TJ_Animation"):         
                call LauraFace("tongue",Eyes="down")
                call Speed_Shift(5) #shallow animation
                "She nods and bends down to put the tip between her lips."
            elif not renpy.showing("Laura_BJ_Animation"):
                call Laura_BJ_Launch("cum")           
                call LauraFace("tongue",Eyes="down")
                if Speed == 4: #6 if deep throating, 5 if not
                        call Speed_Shift(6)
                else:
                        call Speed_Shift(5)
                "She nods and bends down to put the tip between her lips."
            else:                 
                call LauraFace("tongue",Eyes="down")
                $ L_Brows = "confused"
                if Speed == 4: #6 if deep throating, 5 if not
                        call Speed_Shift(6)
                else:
                        call Speed_Shift(5)
                "She nods and hums a \"yes\" sound."   
            $ L_Spunk.append("mouth")
            $ L_Spunk.append("chin")
            "After you cum, she quickly gulps it down and wipes her mouth."
            ". . ."
            call LauraFace("sexy")            
            call Speed_Shift(0)
            ch_l "Yum."
            $ L_Spunk.remove("mouth")
            jump L_Swallowed
        
    elif L_Addict >= 80 and L_Swallow: 
            #addicted           
            if renpy.showing("Laura_TJ_Animation"):         
                call LauraFace("tongue",Eyes="down")
                call Speed_Shift(5) #shallow animation
                "She gently puts the tip to her lips, just as you blow."
            elif not renpy.showing("Laura_BJ_Animation"):
                call Laura_BJ_Launch("cum")           
                call LauraFace("tongue",Eyes="down")
                if Speed == 4: #6 if deep throating, 5 if not
                        call Speed_Shift(6)
                else:
                        call Speed_Shift(5)
                "She gently puts the tip to her lips, just as you blow."
            else:                 
                call LauraFace("tongue",Eyes="down")
                $ L_Brows = "confused"
                if Speed == 4: #6 if deep throating, 5 if not
                        call Speed_Shift(6)
                else:
                        call Speed_Shift(5)
                "She nods and hums a \"yes\" sound."                    
            $ L_Spunk.append("mouth")
            $ L_Spunk.append("chin")
            "She gags a little, but quickly swallows it."
            ". . ."
            call Speed_Shift(0)
            call LauraFace("sexy")
            $ L_Mouth = "smile"
            ch_l "Can't say I didn't enjoy that . ."
            $ L_Spunk.remove("mouth")
            call Statup("Laura", "Inbt", 200, 5)
            jump L_Swallowed
            
    elif L_Swallow:                
            if ApprovalCheck("Laura", 900):
                if renpy.showing("Laura_TJ_Animation"):         
                    call LauraFace("tongue",Eyes="down")
                    call Speed_Shift(5) #shallow animation
                    "She gently puts the tip to her lips, just as you blow."
                elif not renpy.showing("Laura_BJ_Animation"):
                    call Laura_BJ_Launch("cum")           
                    call LauraFace("tongue",Eyes="down")
                    if Speed == 4: #6 if deep throating, 5 if not
                            call Speed_Shift(6)
                    else:
                            call Speed_Shift(5)
                    "She gently puts the tip to her lips, just as you blow."
                else:                 
                    call LauraFace("tongue",Eyes="down")
                    $ L_Brows = "confused"
                    if Speed == 4: #6 if deep throating, 5 if not
                            call Speed_Shift(6)
                    else:
                            call Speed_Shift(5)
                    "She tilts her head and hums a \"hmm?\" sound."
                $ L_Spunk.append("mouth")
                $ L_Spunk.append("chin")
                $ L_Brows = "normal"
                $ L_Eyes = "sexy"
                ". . ."
                call Speed_Shift(0)
                call LauraFace("sexy")
                $ L_Spunk.append("mouth")
                $ L_Spunk.append("chin")
                ch_l "It grows on you. . ."
                $ L_Spunk.remove("mouth")
                jump L_Swallowed
     
    #If she hasn't swallowed or doesn't automatically want to. . .  
    
    if  ApprovalCheck("Laura", 300, "LI") or ApprovalCheck("Laura", 300, "OI"): 
        call LauraFace("bemused")
        $ L_Eyes = "sexy"
    else:
        call LauraFace("angry")
        
    call Speed_Shift(0)   
    
    if "full" in L_RecentActions:
            ch_l "I'm stuffed, [L_Petname]. . ." 
    else:
            ch_l "I don't know why. . ."
    
    menu:
        extend ""
        "Sorry about that.":
                call Statup("Laura", "Love", 80, 3)
                $ L_Addictionrate += 1
                if "addictive" in P_Traits:
                    $ L_Addictionrate += 1
                call LauraFace("smile", 1)
                ch_l "Hmm. . ."
                if ApprovalCheck("Laura", 1200, TabM=1) and "full" not in L_RecentActions:
                    $ Approval = 2 
                    call Statup("Laura", "Inbt", 30, 3)
                    call Statup("Laura", "Inbt", 70, 2)  
                    call LauraFace("sexy", 1)
                    ch_l "Maybe a little. . ."
                else:
                    jump L_Handy_Finish                
            
        "Give it a try, you might like it." if "full" not in L_RecentActions:
                if ApprovalCheck("Laura", 1200, TabM=1):  
                    $ Approval = 2
                    call Statup("Laura", "Obed", 50, 5)
                    call Statup("Laura", "Obed", 70, 3)
                    $ L_Brows = "confused"  
                    $ L_Eyes = "sexy"
                    ch_l "If you insist. . ."
                else:     
                    $ L_Addictionrate += 1
                    if "addictive" in P_Traits:
                        $ L_Addictionrate += 1
                    $ L_Blush = 1
                    ch_l "You think I don't have a nose, [L_Petname]?"
                    jump L_Handy_Finish
                            
        "Seriously, put it in your mouth.":
                if ApprovalCheck("Laura", 1500, "LI", TabM=1) or ApprovalCheck("Laura", 1200, "OI", TabM=1):
                        call LauraFace("sucking", 1)
                elif ApprovalCheck("Laura", 1000, "OI", Bonus = (L_Addict*10)): #Mild addiction included                
                        call LauraFace("angry", 1)
                else: 
                        #You insisted, she refused. 
                        call LauraFace("angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        call Laura_HJ_Launch("cum")
                        call Laura_HJ_Reset                
                        call Statup("Laura", "Love", 50, -3, 1)
                        call Statup("Laura", "Love", 80, -4, 1)
                        ch_l "Seriously, you eat a dick."
                        call Statup("Laura", "Obed", 30, -1, 1)
                        call Statup("Laura", "Obed", 50, -1, 1)  
                        $ L_RecentActions.append("angry")
                        $ L_DailyActions.append("angry")   
                        $ Line = 0
                        return      
                if renpy.showing("Laura_TJ_Animation"):         
                    call LauraFace("tongue")
                    call Speed_Shift(5) #shallow animation
                else:
                    $ L_Mouth = "sucking"
                    call Laura_BJ_Launch("cum")            
                    call Speed_Shift(5)
                call Statup("Laura", "Obed", 50, 10)
                call Statup("Laura", "Obed", 70, 5)
    
    if renpy.showing("Laura_TJ_Animation"):          
        call LauraFace("tongue")
        call Speed_Shift(5) #shallow animation                         
    elif not renpy.showing("Laura_BJ_Animation"):
        call Laura_BJ_Launch("cum")     
        if Speed == 4: #6 if deep throating, 5 if not
                call Speed_Shift(6)
        else:
                call Speed_Shift(5)
    $ L_Spunk.append("mouth")
    $ L_Spunk.append("chin")
    if ApprovalCheck("Laura", 1200):            
            "She gently puts the tip to her lips, just as you blow."
            "She coughs a little, but quickly swallows it." 
    else:
            "She tentatively places the tip in her mouth, and you blast inside it."
            "She quickly gulps it down."                    
            call LauraFace("sexy")
            call Statup("Laura", "Love", 50, -3, 1)
            call Statup("Laura", "Love", 80, -4, 1)        
    $ L_Mouth = "sucking"
    ". . ."   
    call Speed_Shift(0)         
    call LauraFace("sexy") 
    
    if ApprovalCheck("Laura", 1000) and L_Swallow >= 3:
            ch_l "Mmmmm. . ."    
    elif ApprovalCheck("Laura", 800):                
            ch_l "Takes a little getting used to. . ."
    else:
            call LauraFace("sad")
            ch_l "That's. . . intense. . ."   
    call Statup("Laura", "Inbt", 30, 3)
    call Statup("Laura", "Inbt", 50, 2)            
    $ L_Blow += 1
    jump L_Swallowed     
    #end Laura in mouth  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Creampie  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label L_Creampie_P:
        if Trigger == "sex" and Situation == "auto":
                $ P_Cock = "in"
                $ L_Spunk.append("in")
                $ P_Spunk = "in"
                $ Speed = 4
#                call Speed_Shift(4) 
                if ApprovalCheck("Laura", 1300) or L_CreamP:              
                        call LauraFace("surprised", Eyes="down")
                        "You come in her pussy. Her eyes widen in surprise, but she takes it in stride."  
                        call LauraFace("sexy")
                        if L_Lust >= 85: 
                            call L_Cumming
                else:
                    if L_Lust >= 85: 
                            "You come in her pussy. Her eyes widen in surprise and she shakes a bit."
                            call L_Cumming                
                    else:
                            "You come in her pussy. Her eyes widen in surprise and she pulls out."
                    $ Speed = 0
#                    call Speed_Shift(0) 
                    $ P_Cock = "out"
                    call LauraFace("angry")
                    ch_l "Hey, maybe a heads up?"
                    call LauraFace("bemused")
                    ch_l "Not that it didn't feel good. . ."
                    
                jump L_Creampied
        
        #else (You ask her if it's ok):
        if ApprovalCheck("Laura", 1200) or L_CreamP:        
                call LauraFace("sexy")
                if L_CreamP >= 3:
                    "She smiles and speeds up her actions, causing you to erupt inside her."  
                elif L_CreamP:
                    "She gets a michevious look and speeds up, you burst inside her." 
                else:
                    "As you continue to pound her, she nods her head."
                $ P_Cock = "in"
                $ L_Spunk.append("in")
                $ P_Spunk = "in"
                $ Speed = 4
#                call Speed_Shift(4) 
                if L_Lust >= 85: 
                    call L_Cumming  
                call Statup("Laura", "Love", 90, 1) 
                ch_l "Very. . . filling."
                jump L_Creampied
        else:
                call LauraFace("sexy")
                call Statup("Laura", "Love", 80, 2) 
                call Statup("Laura", "Love", 90, 2) 
                ch_l "Thanks for the heads up *grunt* [L_Petname], but let's not."
        jump L_SpunkBelly

#Start Anal Creampie  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label L_Creampie_A:                             
        # These need conditionals added    
        if Trigger == "anal" and Situation == "auto":
                $ P_Cock = "anal"
                $ L_Spunk.append("anal")
                $ P_Spunk = "anal"
                $ Speed = 4
#                call Speed_Shift(4) 
                if ApprovalCheck("Laura", 1200) or L_CreamP:              
                    call LauraFace("surprised", 1, Eyes="down")
                    "You come in her ass. Her eyes widen in surprise, but she takes it in stride."  
                    call LauraFace("sexy")
                    if L_Lust >= 85: 
                        call L_Cumming
                else:
                    if L_Lust >= 85: 
                        "You come in her ass. Her eyes widen in surprise and she shakes a bit."
                        call L_Cumming                
                    else:
                        "You come in her ass. Her eyes widen in surprise and she pulls out."
                    $ Speed = 0
#                    call Speed_Shift(0) 
                    $ P_Cock = "out"
                    call LauraFace("angry")
                    ch_l "No advanced warning, [L_Petname]?"
                    call LauraFace("bemused")
                    ch_l "That was pretty filling. . ."
                jump L_Creampied
            
        #else (You ask her if it's ok):
        if ApprovalCheck("Laura", 1200) or L_CreamP:        
                call LauraFace("sexy")
                if L_CreamP >= 3:
                    "She smiles and speeds up her actions, causing you to erupt inside her."  
                elif L_CreamP:
                    "She gets a michevious look and speeds up, you burst inside her." 
                else:
                    "As you continue to pound her, she nods her head."
                $ P_Cock = "anal"
                $ L_Spunk.append("anal")
                $ P_Spunk = "anal"
                $ Speed = 4
#                call Speed_Shift(4) 
                if L_Lust >= 85: 
                    call L_Cumming  
                call Statup("Laura", "Love", 90, 1) 
                ch_l "Mmmm, so full. . ."
                jump L_Creampied
        else:
                call LauraFace("sexy")     
                call Statup("Laura", "Love", 80, 2) 
                ch_l "Thanks for warning me *grunt* [L_Petname], but perhaps not."
        jump L_SpunkBelly
            
#Start Facial  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    
label L_Facial: 
    if renpy.showing("Laura_BJ_Animation"):       
            if L_Addict >= 60 and ApprovalCheck("Laura", 1000, "I", Bonus = ((L_Addict*10)- L_Obed)) and L_Swallow:
                    $ L_Eyes = "manic"
                    $ L_Blush = 1
                    call Speed_Shift(0)
                    "You pull out of her mouth with a pop, and her eyes widen in surprise." 
                    call Speed_Shift(4)
                    $ L_Spunk.append("mouth")
                    $ L_Spunk.append("chin")
                    "She leaps at your cock and sucks it deep, draining your fluids hungrily."
                    $ L_Mouth = "lipbite"
                    call Speed_Shift(0)
                    "When she finishes, she draws her hand across her lips."
                    call LauraFace("bemused")
                    $ L_Spunk.remove("mouth")
                    ch_l "I'm sorry, [L_Petname], but waste not want not."
                    call Statup("Laura", "Obed", 80, -5)
                    call Statup("Laura", "Inbt", 200, 10)
                    jump L_Swallowed
            call Laura_HJ_Launch("cum")
            call Speed_Shift(2)
            if "hair" in L_Spunk:
                pass
            elif "facial" in L_Spunk:
                $ L_Spunk.append("hair")
            else:
                $ L_Spunk.append("facial")
            "You pull out of her mouth with a pop, and she strokes you off. You spray all over her face."
            call Speed_Shift(0)
            jump L_Orgasm_After
    
    if not renpy.showing("Laura_TJ_Animation") and not renpy.showing("Laura_HJ_Animation"):      
            call Laura_HJ_Launch("cum")
            call Speed_Shift(2)
    if "hair" in L_Spunk:
        pass
    elif "facial" in L_Spunk:
        $ L_Spunk.append("hair")
    else:
        $ L_Spunk.append("facial")
    "As you're about to finish, you pull out, aim squarely at her face, and spray all over it."
    call Speed_Shift(0)

    if Situation == "warn":
        ch_l "Thanks for the warning. . . maybe not the mess though. . ." 
    else:
        ch_l "What a mess, maybe a heads up next time?" 
                
    jump L_Orgasm_After

#Start titjob spunk  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    
label L_TitSpunk: 
    if renpy.showing("Laura_BJ_Animation"):       
            if L_Addict >= 60 and ApprovalCheck("Laura", 1000, "I", Bonus = ((L_Addict*10)- L_Obed)) and L_Swallow:
                    $ L_Eyes = "manic"
                    $ L_Blush = 1
                    call Speed_Shift(0)
                    "You pull out of her mouth with a pop, and her eyes widen in surprise." 
                    call Speed_Shift(4)
                    $ L_Spunk.append("mouth")
                    $ L_Spunk.append("chin")
                    "She leaps at your cock and sucks it deep, draining your fluids hungrily."
                    $ L_Mouth = "lipbite"
                    call Speed_Shift(0)
                    "When she finishes, she draws her hand across her lips."
                    call LauraFace("bemused")
                    $ L_Spunk.remove("mouth")
                    ch_l "Sorry, [L_Petname], too delicious."
                    call Statup("Laura", "Obed", 80, -5)
                    call Statup("Laura", "Inbt", 200, 10)
                    jump L_Swallowed
    
    if renpy.showing("Laura_SexSprite"):
            $ P_Cock = "out"
            $ P_Spunk = "out"     
            $ Speed = 4
    elif not renpy.showing("Laura_TJ_Animation") and not renpy.showing("Laura_HJ_Animation"): 
            call Laura_HJ_Launch("cum")
            $ Speed = 2
#    if not renpy.showing("Laura_TJ_Animation") and not renpy.showing("Laura_HJ_Animation") and not renpy.showing("Laura_BJ_Animation"):      
#            call Laura_TJ_Launch("cum")

    $ L_Spunk.append("tits")
    $ Speed = 0
    if renpy.showing("Laura_SexSprite"):
            "As you're about to finish, you pull out and spray all over her chest."
    else:
            "As you're about to finish, you speed up and spray all over her chest."

    if Situation == "warn":
        ch_l "That was sloppy." 
    else:
        ch_l "Ugh, a little warning?" 
                
    jump L_Orgasm_After
    
# Start Spunk belly  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label L_SpunkBelly:   
    
    call Laura_Sex_Launch("hotdog")
    if L_Addict >= 60 and ApprovalCheck("Laura", 1000, "I", Bonus = ((L_Addict*10)- L_Obed))  and L_Swallow:
            $ L_Eyes = "manic"
            $ L_Blush = 1
            call Laura_BJ_Launch("cum")
            if Trigger == "sex":
                "You pull out of her pussy with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
            elif Trigger == "anal":                
                "You pull out of her ass with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
            $ L_Mouth = "lipbite"
            $ L_Spunk.append("mouth")
            "When she finishes, she draws her hand across her lips."
            call LauraFace("bemused")
            $ L_Spunk.remove("mouth")
            ch_l "Sorry, [L_Petname], but I couldn't let that go to waste."
            call Statup("Laura", "Obed", 80, -5)
            call Statup("Laura", "Inbt", 200, 10)
            jump L_Swallowed
    $ P_Cock = "out"
    $ P_Spunk = "out"     
    $ Speed = 4
#    call Speed_Shift(4) 
    $ L_Spunk.append("belly")
    if Trigger == "sex":
            "You pull out of her pussy with a pop and spray all over her belly."
    elif Trigger == "anal":
            "You pull out of her ass with a pop and spray all over her belly."
    else:
            "You pick up the pace and with a grunt you spray all over her belly."
        
                  
    if L_Addict >= 60 and ApprovalCheck("Laura", 800, "I", Bonus = ((L_Addict*10)- L_Obed)) and L_Swallow: 
            #if she's manic and has swallowed
            $ L_Eyes = "manic"
            $ L_Blush = 1        
            "Laura's eyes widen with desire, and she quickly wipes a bit off with her hand, then licks her fingers clean."
            call LauraFace("manic", 1)
            $ L_Spunk.append("mouth")
            $ L_Mouth = "smile"
            ch_l "Well, [L_Petname], I just couldn't let that go to waste."
            $ L_Spunk.remove("mouth")
            call Statup("Laura", "Inbt", 50, 3)
            jump L_Swallowed
          
        
    #else . . .
    call LauraFace("sexy", 1)
    ch_l "Hmm. . . what a mess. . ."  
#    call Laura_Sex_Reset
    jump L_Orgasm_After
    
   
#Start Handy finish  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label L_Handy_Finish:
    if renpy.showing("Laura_SexSprite"):
        call Laura_Sex_Reset
    call Laura_HJ_Launch("cum")
    $ Speed = 2
    $ L_Spunk.append("hand")  
    if renpy.showing("Laura_HJ_Animation"):                                  
            "She grins and speeds up her efforts, placing her left hand over your tip. You burst all over her hands." 
    else:
            "She grins and starts jerking you off, placing her left hand over your tip. You burst all over her hands."
    $ Speed = 0
    
    if L_Addict > 80 or "hungry" in L_Traits:
            $ L_Eyes = "manic"
            $ L_Spunk.remove("hand")
            $ L_Spunk.append("mouth")
            $ L_Mouth = "smile"
            "She licks her hands off with a satisfied grin."
            $ L_Spunk.remove("mouth")
            ch_l "Hmmm. . ."
    else:
            call LauraFace("bemused")
            $ L_Spunk.remove("hand")
            "She wipes her hands off, but takes a quick sniff when she's done and smiles."
            ch_l "Thanks for the heads up." 
            jump L_Orgasm_After


#Start Swallowed  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label L_Swallowed: 
        $ L_Swallow += 1
        call Statup("Laura", "Inbt", 50, 3)
        $ L_Addict -= 20    
        if "mouth" in L_Spunk:
                $ L_Spunk.remove("mouth")
        if "full" not in L_RecentActions and Action_Check("Laura", "recent", "swallowed") >= 5: 
                $ L_RecentActions.append("full")    
                call LauraFace("surprised", 1)
                ch_l "-ehem-"
                call LauraFace("sexy", 1)
                ch_l "Excuse me [L_Petname], it must have been something I ate."
        $ L_RecentActions.append("swallowed")                      
        $ L_DailyActions.append("swallowed") 
        $ L_Addictionrate += 2
        if "addictive" in P_Traits:
                $ L_Addictionrate += 2
        if Trigger == "anal":    
                call Statup("Laura", "Obed", 50, 2)
                call Statup("Laura", "Obed", 200, 2)
        if L_Swallow == 1:
                $L_SEXP += 12
                call Statup("Laura", "Inbt", 70, 5)
        jump L_Orgasm_After

#Start Creampied  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label L_Creampied:
    if Trigger == "sex":
            $ L_CreamP += 1
            call Statup("Laura", "Lust", 200, 10)
            $ L_RecentActions.append("creampie sex")                      
            $ L_DailyActions.append("creampie sex") 
    elif Trigger == "anal":
            $ L_CreamA += 1
            call Statup("Laura", "Lust", 200, 5)
            $ L_RecentActions.append("creampie anal")                      
            $ L_DailyActions.append("creampie anal") 
    call Statup("Laura", "Inbt", 50, 3)
    $ L_Addict -= 30
    $ L_Addictionrate += 2
    if "addictive" in P_Traits:
            $ L_Addictionrate += 3
    if L_CreamP == 1:
            $L_SEXP += 10
            call Statup("Laura", "Inbt", 70, 5)
#    call Laura_Sex_Reset

# Clean-up / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label L_Orgasm_After:
        $ Line = "What next?"
        if not renpy.showing("Laura_HJ_Animation"):
            $ Laura_Arms = 1
        $ P_Semen -= 1
        $ P_Focus = 0
        call Speed_Shift(0)
        menu:
                "Want her to clean you off?"
                "Yes":
                    call L_CleanCock
                "Actually, let [Partner] do it." if Partner:
                    call AllReset("Laura") #resets the position of the orignal lead
                    call Partner_Clean #
                    call AllReset("Laura") #resets the position of the orignal lead
                "No":
                    pass
        if L_Spunk:
                call Laura_Cleanup
        $ Situation = 0
        return
        
        
label L_CleanCock:
        $ Line = "What next?"
        if not renpy.showing("Laura_HJ_Animation"):
            $ Laura_Arms = 1
        $ P_Cock = "out"
        call Speed_Shift(0)  
        if Trigger == "anal" and not ApprovalCheck("Laura", 1600, TabM=1) and not L_Addict >= 80:
                "She wipes your cock clean."
        elif "classcaught" in L_RecentActions and bg_current == "bg classroom" and L_SEXP <= 10:
                #this skips this step if you haven't done much yet
                "She wipes your cock clean."
        elif L_Blow > 3 or L_Swallow: 
                if ApprovalCheck("Laura", 1200, TabM=1) or L_Addict >= 60:
                        call Laura_BJ_Launch("cum")
                        call Speed_Shift(1)
                        call LauraFace("sucking", 1) 
                        if ApprovalCheck("Laura", 1500, TabM=1):
                            if Partner and ApprovalCheck(Partner, 1500, TabM=1):
                                "Both girls look up at you as they lick your cock clean."
                            elif L_Love > L_Inbt and L_Love > L_Obed:
                                $ L_Eyes = "sly"
                                "She looks up at you lovingly as she licks your cock clean."            
                            elif L_Obed > L_Inbt:
                                $ L_Eyes = "side"
                                "She dutifully licks your cock clean with lowered eyes."
                                call Statup("Laura", "Obed", 80, 3)                
                            else:
                                "She happily licks your cock clean." 
                        elif L_Addict >= 60:
                                "She hungrily and thoroughly licks your cock clean."   
                        else:
                            "She licks you cock clean." 
                        call LauraFace("sexy")  
                else:
                        if not renpy.showing("Laura_HJ_Animation"):
                            call Laura_HJ_Launch("cum") 
                        if Partner and ApprovalCheck(Partner, 1000, TabM=1):
                            "Both girls reach down and wipe your cock clean."
                        else:
                            "She wipes your cock clean."  
        else:
                        if not renpy.showing("Laura_HJ_Animation"):
                            call Laura_HJ_Launch("cum") 
                        if Partner and ApprovalCheck(Partner, 1000, TabM=1):
                            "Both girls reach down and wipe your cock clean."
                        else:
                            "She wipes your cock clean."       
        $ P_Spunk = 0
        call LauraFace("sexy") 
        return
    
# End You Cumming //////////////////////////////////////////////////////////////////////////////////


# Laura Lusty face check ////////////////////////////////////////////////////////////////////////////////
label LauraLust(Extreme = 0, Kissing = 0):
                
    if L_Lust >= 90:        
            $ L_Blush = 2
    elif L_Lust >= 40:        
            $ L_Blush = 1 
        
    if L_Lust >= 80:
            $ L_Wet = 2 
    elif L_Lust >= 50:
            $ L_Wet = 1
            
    if L_Loc == "bg teacher" and not Extreme:
            #this prevents her face from changing if she's just being a teacher.
            return
       
    if Trigger3 == "kiss both" or Trigger3 == "kiss girl":
            #if the girls are kissing or all three are
            $ Kissing = 1
    elif Trigger4 == "kiss both" or Trigger3 == "kiss girl":
            #if the girls are kissing or all three are
            $ Kissing = 1   
    elif Partner != "Laura":
            #If Laura is kissing and is primary
            if Trigger == "kiss you" or Trigger2 == "kiss you":  
                $ Kissing = 1
    elif Trigger4 == "kiss you":   
            #If Laura is kissing you in a threesome action
            $ Kissing = 1
            
    if Kissing:
            $ L_Eyes = "closed"
            if L_Kissed >= 10 and L_Inbt >= 300:
                $ L_Mouth = "sucking"
            elif L_Kissed > 1 and L_Addict >= 50:            
                $ L_Mouth = "sucking"
            else:
                $ L_Mouth = "kiss"
    else:    
            #If Laura is not kissing someone
            if L_Lust >= 90:
                    $ L_Eyes = "closed"
                    $ L_Brows = "sad"
                    $ L_Mouth = "surprised"
            elif L_Lust >= 70:
                    $ L_Eyes = "sexy"
                    $ L_Brows = "sad"
                    $ L_Mouth = "lipbite"
            elif L_Lust >= 50 and not Extreme:
                    $ L_Eyes = "squint"
                    $ L_Brows = "sad"
                    $ L_Mouth = "lipbite"
            elif L_Lust >= 30 and not Extreme:
                    $ L_Eyes = "sexy"
                    $ L_Brows = "normal"
                    $ L_Mouth = "smirk"
            elif not Extreme:
                    $ L_Eyes = "sexy"
                    $ L_Brows = "normal"
                    $ L_Mouth = "smirk"    
            if L_Lust < 50 and not Extreme and not ApprovalCheck("Laura", 1000):
                $ L_Eyes = "side"
    
    if Partner == "Laura" and Trigger4 in ("lick pussy", "lick ass", "blow", "suck breasts"):         
                    $ L_Mouth = "tongue"  
    elif Trigger3 in ("lick pussy", "lick ass", "suck breasts"):         
                    $ L_Mouth = "tongue"  
                    
    if L_OCount >= 10:   
            #If you've fucked her senseless
            $ L_Eyes = "stunned"
            $ L_Mouth = "tongue"   
                
    return

# End faces

#  Laura Orgasm //////////////////////////

label L_Cumming(Quick=0):
    $ L_Eyes = "surprised"
    $ L_Brows = "sad"
    $ L_Mouth = "tongue"
    $ L_Blush = 1
    ch_l ". . . !"
    call Speed_Shift(0)
    if renpy.showing("Laura_SexSprite"):
            show Laura_SexSprite #fix, test this
            with vpunch
    elif renpy.showing("Laura_BJ_Animation"):           #fix, make this animation work better when paused for this effect.
            show Laura_BJ_Animation
            with vpunch
    elif renpy.showing("Laura_TJ_Animation"):
            show Laura_TJ_Animation  
            with vpunch
    elif renpy.showing("Laura_HJ_Animation"):
            show Laura_HJ_Animation  
            with vpunch
    else:
            show Laura_Sprite
            with vpunch
    call Speed_Shift(1)
    $ Line = renpy.random.choice(["Laura is suddenly rocked with spasms, holding back a muffled scream.", 
                "Laura grabs on tightly as her body shakes with pleasure.", 
                "Laura stiffens and lets out a low moan.",
                "Laura's body quivers and suddenly goes still."])
    "[Line]"    
    if Quick:
            call AnyFace("Laura","sexy",2)  
            $ L_Lust = 20
            return
            
    $ L_Eyes = "closed"
    $ L_Brows = "sad"
    $ L_Mouth = "tongue"
    $ Line = renpy.random.choice(["Oooooh. . .", 
                "That was a good one. . .", 
                "Hmmmm. . . .",
                "That was. . ."])
    ch_l "[Line]"
           
    
    $ L_Lust = 30 if "hotblooded" in L_Traits else 0 
    $ L_Lust += (L_OCount * 5)
    $ L_Lust = 80 if L_Lust >= 80 else L_Lust    
    call Statup("Laura", "Inbt", 50, 1)
    call Statup("Laura", "Inbt", 70, 1)
            
    if "unsatisfied" in L_RecentActions:  #If she had been unsatisfied, you satisfied her. . .        
            call Statup("Laura", "Love", 70, 2)
            call Statup("Laura", "Love", 90, 1)
            if "unsatisfied" in L_DailyActions:
                ch_l "Thanks for evening the score, [L_Petname]?"
            call DrainWord("Laura","unsatisfied")
    $ L_OCount += 1        
    $ L_Org += 1
    $ Line = 0
      
    if Trigger != "masturbation":
            call Statup("Laura", "Lust", 40, 1)
            call Statup("Laura", "Love", 70, 1)
            call Statup("Laura", "Love", 90, 1)
            call Statup("Laura", "Obed", 50, 2)
            call Statup("Laura", "Obed", 70, 2)  
            if L_OCount == 1:
                    # if she's angry, but not too angry, then reduce that on the first O of the time block.
                    $ L_ForcedCount -= 1 if 5 > L_ForcedCount > 0 else 0 
            
            #checks to check reaction of other girls
            if K_Loc == bg_current and "noticed laura" in K_RecentActions:                     
                    $ K_Lust += 15 if K_LikeLaura >= 500 else 10
                    $ K_Lust += 5 if K_Les >= 5 else 0
            elif R_Loc == bg_current and "noticed laura" in R_RecentActions: 
                    $ R_Lust += 15 if R_LikeLaura >= 500 else 10
                    $ R_Lust += 5 if R_Les >= 5 else 0 
            elif E_Loc == bg_current and "noticed laura" in E_RecentActions: 
                    $ E_Lust += 15 if E_LikeLaura >= 500 else 10
                    $ E_Lust += 5 if E_Les >= 5 else 0 
            if Partner == "Laura":
                    #If the active girl is someone else
                    call Partner_Cumming("Laura")
                    
            #Orgasm count
            if Trigger != "blow" and Trigger != "hand" and Partner != "Laura":
                if L_OCount == 2:
                        $ L_Brows = "confused"
                        ch_l "Hey, good job, [L_Petname]. . ."
                        call Statup("Laura", "Love", 50, 1)
                        call Statup("Laura", "Love", 80, 2)
                        call Statup("Laura", "Obed", 50, 1)
                        call Statup("Laura", "Obed", 60, 1)            
                elif L_OCount == 3: #5
                        $ L_Brows = "confused"            
                        ch_l "You can. . . definitely. . . keep up. . ."
                        call Statup("Laura", "Love", 50, 2)
                        call Statup("Laura", "Love", 80, 2)
                        call Statup("Laura", "Obed", 30, 1)
                        call Statup("Laura", "Obed", 50, 1)                    
                elif L_OCount == 6 and Partner != "Laura": #10
                    $ L_Mouth = "tongue"    
                    ch_l "I don't. . . usually. . . wear out. . . this easy. . ."
                    menu:
                        ch_l "could. . . we. . . take. . . a break?"
                        "Finish up." if P_FocusX:
                            "You release your concentration. . ."                 
                            $ P_FocusX = 0
                            $ P_Focus += 15                    
                        "Let's try something else." if MultiAction:  
                            $ Situation = "shift"
                        "No, I'm not done yet.":
                            if Trigger == "sex" or Trigger == "anal":
                                if ApprovalCheck("Laura", 1000, TabM=1) or ApprovalCheck("Laura", 400, "O", TabM=1):
                                    call Statup("Laura", "Love", 200, -5)
                                    call Statup("Laura", "Obed", 50, 2)
                                    call Statup("Laura", "Obed", 80, 3)
                                    $ L_Eyes = "stunned"
                                    "She drifts off into incoherent moans."
                                else:
                                    call LauraFace("angry", 1)
                                    "She scowls at you, pulls out with a pop, and wipes herself off."
                                    ch_l "Learn to take a hint. . ."
                                    call Statup("Laura", "Love", 50, -3, 1)
                                    call Statup("Laura", "Love", 80, -4, 1)
                                    call Statup("Laura", "Obed", 30, -1, 1)
                                    call Statup("Laura", "Obed", 50, -1, 1)  
                                    $ L_RecentActions.append("angry")
                                    $ L_DailyActions.append("angry")   
                            else:
                                call Statup("Laura", "Obed", 50, 3)
                                call Statup("Laura", "Obed", 80, 2)
                                $ L_Eyes = "stunned"
                                "She drifts off into incoherent moans."  
                #end Ocount stuff
    if Trigger == "strip":
            call AllReset("Laura")
            show Laura_Sprite at Laura_Dance1()
            "Laura begins to dance again."
    return
    
# End Laura Orgasm /////////////////////////////////////////////////////////////////////////////////////


# Start Laura Clean-Up /////////////////////////////////////////////////////////////////////////////////////
label Laura_Cleanup(Choice = "random",Options=[],Cnt=0,Cleaned=0,Original="Laura"):
    
    if Choice == "after":
            # This is at the end of a session            
            if not L_Spunk:
                $ L_Wet = 0
                return    
            $ Cnt = 1  
        
    if L_Addict > 80 and L_Swallow:
        #if she likes cum, she prefers to eat it. 
        $ Choice = "eat"            
        $ L_Eyes = "manic"
        $ L_Mouth = "smile"          
    elif Choice == "ask":
        pass
    elif "painted" in L_RecentActions and ApprovalCheck("Laura", 1000, "OI"):
        return
    elif ApprovalCheck("Laura", 1200, "LO"):  
        $ Choice = "ask"            
    elif not ApprovalCheck("Laura", 400, "I"):
        call LauraFace("bemused") 
        $ Choice = "clean"   
    else:
        $ Choice = "ask"      
      
    if Ch_Focus != "Laura":
        # if Laura isn't the lead, swap to her.
        $ Original = Partner
        call Shift_Focus("Laura")
        
    $ Cleaned = 1 if "cleaned" in L_DailyActions else 0
    $ L_RecentActions.append("cleaned") 
    $ L_DailyActions.append("cleaned") 
    
    if Choice == "ask":
            $ Choice = "random"
            "She looks down at the spunk covering her."
            menu:
                "What do you suggest Laura do about cleaning up?"
                "You should leave it where it is.":
                        if not Cnt:
                            # If this isn't the end of the session
                            if ApprovalCheck("Laura", 300, "I") or ApprovalCheck("Laura", 1000):
                                    call Statup("Laura", "Obed", 70, 1)
                                    call Statup("Laura", "Inbt", 50, 1)
                                    call Statup("Laura", "Lust", 90, 2) 
                                    $ Choice = "leave"  
                                    call LauraFace("sly") 
                                    ch_l "Hmm. . ."
                            else:
                                    call LauraFace("sly") 
                                    ch_l "Eh, I'm not a fan of mess, [L_Petname]." 
                        elif ApprovalCheck("Laura", 900, "I") or "exhibitionist" in L_Traits:
                                call Statup("Laura", "Obed", 70, 2)
                                call Statup("Laura", "Obed", 90, 1)
                                call Statup("Laura", "Lust", 90, 5) 
                                $ Choice = "leave"  
                                call LauraFace("sly") 
                                ch_l "Hmm. . . I do like the glow it gives me. . "
                        elif ApprovalCheck("Laura", 600, "I") and ApprovalCheck("Laura", 1200, "LO"):
                                call Statup("Laura", "Obed", 90, 1)
                                call Statup("Laura", "Inbt", 80, 1) 
                                call Statup("Laura", "Lust", 90, 5) 
                                $ Choice = "leave"  
                                call LauraFace("surprised",2) 
                                ch_l "Hmm. . . if you insist. . ."
                                call LauraFace("sly",1) 
                        
                        else:
                            call LauraFace("angry") 
                            menu:
                                ch_l "Excuse me?" 
                                "Please?":
                                    if ApprovalCheck("Laura", 1800):
                                        call Statup("Laura", "Love", 85, 1)
                                        call Statup("Laura", "Obed", 50, 2)
                                        call Statup("Laura", "Obed", 80, 1)
                                        call Statup("Laura", "Inbt", 40, 3) 
                                        call Statup("Laura", "Inbt", 80, 1) 
                                        ch_l "Fine."
                                        $ Choice = "leave"  
                                    elif Cleaned:
                                        call LauraFace("angry") 
                                        ch_l "I'm in no mood for this."
                                    elif ApprovalCheck("Laura", 800):
                                        call Statup("Laura", "Inbt", 50, 1) 
                                        ch_l "You're certainly persistant, but no."
                                    else:
                                        call Statup("Laura", "Love", 75, -5)
                                        call Statup("Laura", "Love", 40, -10)
                                        call Statup("Laura", "Obed", 90, 2)
                                        call LauraFace("angry") 
                                        ch_l "You've gotta be joking."
                                "I insist.":
                                    call LauraFace("sad") 
                                    if ApprovalCheck("Laura", 400, "I") and ApprovalCheck("Laura", 1200, "LO"):
                                        call Statup("Laura", "Obed", 40, 3)
                                        call Statup("Laura", "Obed", 90, 2)
                                        ch_l "Fine."
                                        $ Choice = "leave"  
                                    elif ApprovalCheck("Laura", 800, "O"):
                                        call Statup("Laura", "Love", 50, -10)
                                        call Statup("Laura", "Love", 200, -5)
                                        call Statup("Laura", "Obed", 90, 10)
                                        call Statup("Laura", "Obed", 200, 5)
                                        ch_l "If you insist."
                                        $ Choice = "leave"  
                                    elif Cleaned:
                                        call Statup("Laura", "Love", 50, -5)
                                        call Statup("Laura", "Love", 200, -1)
                                        call LauraFace("angry") 
                                        ch_l "Enough out of you."
                                    elif ApprovalCheck("Laura", 800):
                                        call Statup("Laura", "Love", 50, -3)
                                        call Statup("Laura", "Love", 200, -1)
                                        call LauraFace("sad") 
                                        ch_l "Don't push it." 
                                    else:
                                        call Statup("Laura", "Love", 50, -10)
                                        call Statup("Laura", "Love", 200, -5)
                                        call LauraFace("angry") 
                                        ch_l "Hell no."
                                        
                                "Never mind then.":
                                    ch_l "Ok. . ."                            
                        #end "leave it"
                        
                "You should just eat it.":
                        call LauraFace("sly") 
                        if "hungry" in L_Traits or (L_Swallow >= 5 and ApprovalCheck("Laura", 800)): 
                                #lots of swallows
                                call Statup("Laura", "Obed", 90, 1)
                                call Statup("Laura", "Inbt", 50, 3) 
                                call Statup("Laura", "Inbt", 80, 1) 
                                call Statup("Laura", "Lust", 90, 5) 
                                $ Choice = "eat"   
                                "She licks her lips. . ."
                        elif L_Swallow and ApprovalCheck("Laura", 800): 
                                #few swallows
                                call Statup("Laura", "Obed", 50, 1)
                                call Statup("Laura", "Obed", 90, 1)
                                call Statup("Laura", "Inbt", 50, 2) 
                                call Statup("Laura", "Inbt", 80, 1) 
                                call Statup("Laura", "Lust", 90, 5) 
                                $ Choice = "eat"   
                                ch_l "You do taste pretty good. . ."
                        elif ApprovalCheck("Laura", 1200): 
                                #no swallows, but likes you
                                call Statup("Laura", "Obed", 50, 1)
                                call Statup("Laura", "Obed", 90, 1)
                                call Statup("Laura", "Inbt", 50, 3) 
                                call Statup("Laura", "Inbt", 80, 1) 
                                $ Choice = "eat"   
                                ch_l "I have been thinking about it. . ."
                        elif ApprovalCheck("Laura", 400): 
                                #Likes you well enough, but won't
                                call LauraFace("sad") 
                                ch_l "Yeah, but I won't. . ."
                        else: 
                                #doesn't like you.
                                call Statup("Laura", "Love", 50, -5)
                                call Statup("Laura", "Love", 200, -3)
                                call LauraFace("angry") 
                                ch_l "Nope."
                        #end eat it
                              
                "You should just clean it up.":
                        if ApprovalCheck("Laura", 600, "I") and not ApprovalCheck("Laura", 1500, "LO"): #rebellious
                                call LauraFace("sly") 
                                call Statup("Laura", "Obed", 50, -3)
                                call Statup("Laura", "Inbt", 70, 10) 
                                call Statup("Laura", "Inbt", 200, 5) 
                                call Statup("Laura", "Lust", 60, 5) 
                                ch_l "I could. . ."
                                ch_l "-but I don't want to. . ."
                                $ Choice = "leave"   
                                menu:
                                    extend ""
                                    "Ok, fine.":
                                        call LauraFace("smile") 
                                        call Statup("Laura", "Love", 70, 5)
                                        call Statup("Laura", "Obed", 50, 3)
                                    "No, clean it up.": 
                                        if ApprovalCheck("Laura", 600, "O"):
                                            call LauraFace("sad") 
                                            call Statup("Laura", "Obed", 50, 10)
                                            ch_l "Oh, fine. . ."
                                            $ Choice = "clean"  
                                        elif ApprovalCheck("Laura", 1200, "LO"):
                                            call LauraFace("sad") 
                                            call Statup("Laura", "Love", 70, -3)
                                            call Statup("Laura", "Obed", 50, 3)
                                            ch_l "Booo. . ."
                                            $ Choice = "clean"   
                                        else:
                                            call Statup("Laura", "Love", 70, -5)
                                            call Statup("Laura", "Obed", 50, -5)
                                            ch_l "Too bad."
                                                                                    
                        else: #agrees
                                call LauraFace("bemused") 
                                $ Choice = "clean"   
                                ch_l "Whatever. . ."
                        #end clean it up
                        
                "Hey [Partner], you eat it off her." if Partner:
                            $ Choice = "partner lick"  
                "Hey [Partner], you wipe it off her." if Partner:
                            $ Choice = "partner wipe"  
                                            
                "Say nothing. [[leave it to her]":
                    $ Choice = "random"
            #end "asked"
                
    if Choice == "partner wipe" or Choice == "partner lick":
            #resets to "random" if she refuses        
            call Partner_Cleanup_Check("Laura")
            
    if Choice == "random":
            $ Options = ["clean"]
            if L_Swallow and ApprovalCheck("Laura", 800):
                    $ Options.append("eat") 
                    if L_Swallow >=5:                            
                        $ Options.append("eat") 
                    if "hungry" in L_Traits:                
                        $ Options.append("eat") 
            if ApprovalCheck("Laura", 600, "I"):
                    if not Cnt:
                        $ Options.append("leave") 
                    if not Cnt or ApprovalCheck("Laura", 800, "I"):
                        $ Options.append("leave") 
                    if "exhibitionist" in L_Traits:
                        $ Options.append("leave") 
                                        
            $ renpy.random.shuffle(Options)
            
            $ Choice = Options[0]
            #end "random"
            
            
    if Choice == "leave":
            call Statup("Laura", "Inbt", 80, 2) 
            call Statup("Laura", "Inbt", 200, 1) 
            "She leaves the jiz right where it is and gives you a wink."
            if "hand" in L_Spunk: 
                    $ L_Spunk.remove("hand")
                    if L_Swallow:
                        "She does lick off her hand though."
                    else:
                        "She does wipe her hand off though."   
            if "mouth" in L_Spunk:                  
                    $ L_Spunk.remove("mouth")
            if Cnt:
                    # if this is final clean-up and left the jiz on   
                    $ L_RecentActions.append("painted")                  
                    $ L_DailyActions.append("painted")  
            #end "leave it"
           
    if L_Spunk and Choice != "leave":
            call Self_Cleanup("Laura")
               
    if Ch_Focus != Original:
        # if Laura wasn't the lead, swap that one back
        call Shift_Focus(Original)
    return    
    
# End Laura Clean-Up /////////////////////////////////////////////////////////////////////////////////////

