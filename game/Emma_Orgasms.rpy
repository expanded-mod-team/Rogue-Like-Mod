# Start You Cumming //////////////////////////////////////////////////////////////////////////////////

label PE_Cumming:
    call Shift_Focus("Emma")
    if "classcaught" in E_RecentActions and bg_current == "bg classroom":
            #if you're in the classcaught scenario
            $ Tempmod -= 50 if Tempmod >= 50 else Tempmod 
            
    if Trigger == "blow":
            $ Tempmod += 5
        
    if E_Addict > 75:
            $ Tempmod += 20
    elif E_Addict > 50:
            $ Tempmod += 5
    
    if E_Swallow >= 10:
            $ Tempmod += 15  
    elif E_Swallow >= 3:
            $ Tempmod += 5
        
    if (E_CreamP + E_CreamA) >= 10:
            $ Tempmod += 15 
    elif (E_CreamP + E_CreamA) >= 3:
            $ Tempmod += 5             
       
    $ D20 = renpy.random.randint(1, 20) 
    
# intro lines    
    if Trigger == "hand" or Trigger == "foot":
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
    
    call EmmaFace("sexy") 
    
    menu:
        "[Line]"
        "Warn her":
                $ Situation = "warn"
                jump E_Warn_Her
            
        "Ask to cum in her mouth": 
                $ Situation = "asked"
                jump E_In_Mouth                            
        "Cum in her mouth without asking" if Trigger == "blow" or Trigger == "hand" or Trigger == "titjob":
                $ Situation = "auto"
                jump E_In_Mouth
        
        "Ask to cum inside her" if Trigger == "sex":
                $ Situation = "asked"
                jump E_Creampie_P        
        "Ask to cum inside her" if Trigger == "anal":
                $ Situation = "asked"
                jump E_Creampie_A
                
        "Cum inside her" if Trigger == "sex":
                $ Situation = "auto"
                jump E_Creampie_P        
        "Cum inside her" if Trigger == "anal":
                $ Situation = "auto"
                jump E_Creampie_A
            
        "Cum on her face":
                jump E_Facial   
                
        "Cum on her tits":
                jump E_TitSpunk   
                
#MOD MARKER cum menu choices
        "Cum on her ass" if Trigger in ("sex","anal","hotdog") and renpy.showing("Emma_Doggy"):
                jump E_SpunkBack
        "Cum on her belly" if Trigger in ("sex","anal","hotdog","foot") and renpy.showing("Emma_Missionary"):
                jump E_SpunkBellyMissionary
        "Cum on her belly" if Trigger in ("sex","anal","hotdog","foot") and renpy.showing("Emma_SexSprite"):
                jump E_SpunkBelly
            
        "Pull back":
            if renpy.showing("Emma_BJ_Animation"):
                    if E_Addict >= 60 and ApprovalCheck("Emma", 1000, "I", Bonus = ((E_Addict*10)- E_Obed)) and E_Swallow:
                            $ E_Eyes = "manic"
                            $ Speed = 0
                            "You pull out of her mouth with a pop, and her eyes widen in surprise."
                            $ E_Mouth = "sucking"
                            $ E_Spunk.append("mouth")
                            $ Speed = 4
                            "She leaps at your cock and sucks it deep, draining your fluids hungrily." 
                            $ Speed = 0
                            $ E_Mouth = "lipbite"
                            "When she finishes, she draws her hand across her lips."
                            call EmmaFace("bemused")
                            ch_e "I'm sorry, [E_Petname], but that would have been a waste."
                            call Statup("Emma", "Obed", 200, -5)
                            call Statup("Emma", "Inbt", 200, 10)
                            jump E_Swallowed                            
                    call Emma_BJ_Reset                
            elif renpy.showing("Emma_HJ_Animation"):
                    call Emma_HJ_Reset                
            elif renpy.showing("Emma_TJ_Animation"):
                    call Emma_TJ_Reset                   
            elif renpy.showing("Emma_FJ_Animation"):
                    call Emma_FJ_Reset            
            elif renpy.showing("Emma_SexSprite"):
                    call Emma_Sex_Reset                    
            if ApprovalCheck("Emma", 500, "I", Bonus = ((E_Addict*10)- E_Obed)) and E_Addict > 50 and E_Swallow: #If addict + Inbt is > obedience + 50. . .
                    $ E_Eyes = "manic"
                    $ E_Mouth = "kiss"
                    $ Speed = 0
                    "Her eyes widen in panic."
                    ch_e "You wouldn't reconsider, [E_Petname]?" 
                    $ E_Blush = 2
                    menu:
                        extend ""
                        "Ok, if you'll swallow it.":
                                if Trigger != "blow": 
                                    call Emma_BJ_Launch("cum")
                                call EmmaFace("sucking") 
                                $ Speed = 2
                                "She nods and puts the tip into her mouth. as you release she gulps it down hungrily."
                                call EmmaFace("sexy")                      
                                $ E_Mouth = "sucking"
                                $ E_Spunk.append("mouth")
                                ". . ."
                                $ Speed = 0
                                call EmmaFace("sad")                       
                                $ E_Mouth = "lipbite"
                                ch_e "Waste not, want not."  
                                call Statup("Emma", "Obed", 50, 2)
                                call Statup("Emma", "Obed", 70, 1)
                                call Statup("Emma", "Inbt", 30, 2)
                                call Statup("Emma", "Inbt", 50, 3)
                                jump E_Swallowed                                
                        "No, we're done for now.": #If addict is > obedience + 50. . .
                                if ApprovalCheck("Emma", 250, "I", Bonus = ((E_Addict*10)- E_Obed)) or E_Addict > 75:                            
                                        call Statup("Emma", "Obed", 50, -1)
                                        call Statup("Emma", "Obed", 70, -2)
                                        call Statup("Emma", "Inbt", 30, 2)
                                        call Statup("Emma", "Inbt", 70, 3)
                                        if Trigger != "blow":
                                            call Emma_BJ_Launch("cum")
                                            $ Speed = 4
                                        "She dives down on you and you can't resist filling her throat."
                                        $ Speed = 0
                                        ch_e "Well, I'm afraid I wasn't."
                                        jump E_Swallowed                                
                                else:                         
                                        call Statup("Emma", "Obed", 30, 3)
                                        call Statup("Emma", "Obed", 70, 5)
                                        call EmmaFace("sad")
                                        $ E_Brows = "confused"
                                        ch_e "If you insist."
                                        $ Line = 0
                                        $ P_Focus -= 5
                                        return  
                    #manic, wanted to swallow
                    
            call EmmaFace("sexy", 1)
            call Statup("Emma", "Obed", 50, 2)
            "You pull pull back away from her. She looks up at you and licks her lips." 
            ch_e "Well [E_Petname], what next then?"
            $ Line = 0
            $ P_Focus = 95
            return
            #end "pull back"
#End Main orgasm menu

label E_No_Cum:
        #this is a temporary thing until this system is complete
        call EmmaFace("confused", Mouth="smirk") 
        if Situation == "warn":
            ch_p "I'm about to. . . blow. . ."
            ch_e "Oh? How thoughtful."
        elif Situation == "asked":        
            ch_p "I'm about to. . . blow. . ."
            ch_p "Could I. . . come in your mouth?"
            ch_e "Hmmm, I don't think so."
        else:
            ch_e "Oh, I know that look, [E_Petname]. You're about to make a mess, aren't you."         
        if not renpy.showing("Emma_HJ_Animation"):
            $ Emma_Arms = 2
        call EmmaFace("sly",1) 
        ch_e "For now why don't you just come in my hand here. . ."
        $ E_Spunk.append("hand") 
        "She grabs the head of your cock and you gush into it."
        ch_e "See? That wasn't so hard."         
        jump E_Orgasm_After


label E_Warn_Her:
        if E_SEXP <= 10:
            #this skips this step if you haven't done much yet
            jump E_No_Cum
            
        "You let her know that you're going to come."
        call Statup("Emma", "Love", 90, 3)
        if E_Obed >= 500:   
                call Statup("Emma", "Obed", 80, 5) 
        if "hungry" in E_Traits and D20 >= 5:
                if renpy.showing("Emma_SexSprite"):
                    call Emma_HJ_Launch("cum")   
                    "She grins and pulls out with a pop, and begins to stroke you off."
                $ Speed = 2
                call EmmaFace("sucking")       
                ". . ."
                $ Speed = 0
                $ E_Spunk.append("mouth")
                if not renpy.showing("Emma_BJ_Animation"):
                    "She smiles and then puts your tip in her mouth. When you finish filling her mouth, she quickly gulps it down and wipes her lips."
                else:                    
                    "She makes a little humming sound, but keeps sucking. When you finish filling her mouth, she quickly gulps it down and wipes her lips."        
                call EmmaFace("sexy")
                $ E_Mouth = "smile"
                ch_e "Delectable, [E_Petname], I appreciate the warning."        
                jump E_Swallowed
        #End Hungy take-over
            
        if Trigger == "sex" and E_CreamP >= 5: 
                # She's Creampied a few times
                call EmmaFace("sexy")
                $ P_Cock = "in"
                $ E_Spunk.append("in")
                $ P_Spunk = "in"
                $ Speed = 0
                "She smiles and speeds up her actions, causing you to erupt inside her."   
                if E_Lust >= 85: 
                    call E_Cumming  
                jump E_Creampied
        
        elif Trigger == "sex" and E_CreamP and D20 >= 10:  
                # She's Creampied at least once
                call EmmaFace("sly")
                $ P_Cock = "in"
                $ E_Spunk.append("in")
                $ P_Spunk = "in"
                $ Speed = 0
                "She gets a michevious look and speeds up, you burst inside her."          
                if E_Lust >= 85: 
                    call E_Cumming  
                jump E_Creampied
            
        elif Trigger == "anal" and E_CreamA >= 5: 
                # She's Anal Creampied a few times
                call EmmaFace("sexy")
                $ P_Cock = "anal"
                $ E_Spunk.append("anal")
                $ P_Spunk = "anal"
                $ Speed = 0
                "She smiles and speeds up her actions, causing you to erupt inside her."         
                if E_Lust >= 85: 
                    call E_Cumming  
                jump E_Creampied
        
        elif Trigger == "anal" and E_CreamA and D20 >= 10: 
                # She's Anal Creampied at least once
                call EmmaFace("sly")
                $ P_Cock = "anal"
                $ E_Spunk.append("anal")
                $ P_Spunk = "anal"
                $ Speed = 0
                "She gets a michevious look and speeds up, you burst inside her."    
                if E_Lust >= 85: 
                    call E_Cumming          
                jump E_Creampied
            
        elif Trigger != "anal" and E_Swallow >= 5: 
                #If she's swallowed a lot     
                if renpy.showing("Emma_TJ_Animation"):  
                        if E_Blow >= 5 or Speed >= 3:          
                                call EmmaFace("tongue")
                                $ Speed = 5 #shallow animation
                                $ E_Spunk.append("mouth")
                                "She makes a little humming sound, but keeps sucking."
                        else: 
                                jump E_Facial
                elif renpy.showing("Emma_BJ_Animation"):            
                        call EmmaFace("sucking")
                        $ E_Spunk.append("mouth")
                        $ Speed = 6 if Speed == 4 else 5 #6 if deep throating, 5 if not
                        "She makes a little humming sound, but keeps sucking."
                        $ Speed = 0
                        "When you finish filling her mouth, she quickly gulps it down and wipes her lips."
                else:
                        call Emma_BJ_Launch("cum")
                        $ Speed = 2
                        call EmmaFace("sucking")
                        $ E_Spunk.append("mouth")
                        "She smiles and then puts your tip in her mouth."
                        $ Speed = 5
                        "When you finish filling her mouth, she quickly gulps it down and wipes her lips."                
                $ Speed = 0
                call EmmaFace("sexy")
                $ E_Mouth = "smile"
                ch_e "Delectable, [E_Petname], I appreciate the warning."  
                jump E_Swallowed
            
        elif E_Swallow and D20 >= 10:  
                #She's swallowed before, but not a lot  
                if renpy.showing("Emma_SexSprite"):
                    call Emma_HJ_Launch("cum") 
                    "She grins and pulls out with a pop, and begins to stroke you off."
                $ Speed = 2
                if renpy.showing("Emma_TJ_Animation") or renpy.showing("Emma_BJ_Animation"): 
                    if renpy.showing("Emma_TJ_Animation"): 
                        if E_Blow >= 5 or Speed >= 3:          
                                call EmmaFace("tongue")
                                $ Speed = 5 #shallow animation
                                $ E_Spunk.append("mouth")
                        else: 
                                jump E_Facial
                    elif renpy.showing("Emma_BJ_Animation"): 
                            #if she's blowing
                            call EmmaFace("sucking")
                            $ E_Spunk.append("mouth")
                    $ Speed = 6 if Speed == 4 else 5 #6 if deep throating, 5 if not
                    "She makes a little humming sound, but keeps sucking."
                    "When you finish filling her mouth, she gags a little, but manages to swallow it."
                    $ Speed = 0
                    call EmmaFace("sexy")
                    $ E_Mouth = "smile"
                    if E_Addict > 50:
                            $ E_Eyes = "manic"
                            "She gulps it down hungrily and licks her lips."
                    call EmmaFace("bemused")
                    ch_e "Hmm. . . an acquired taste, I appreciate the warning."
                    jump E_Swallowed                    
                    #fix, add titjob option here.   
                else:
                        #If she's handying
                        jump E_Handy_Finish    
        #end if she's swallowed        
            
        elif ApprovalCheck("Emma", 1000):                    
                #warned but likes you and experienced
                if E_SEXP > 20 and renpy.showing("Emma_SexSprite"):
                        "She gently pushes you back off of her."
                        jump E_SpunkBelly
                elif E_SEXP > 20:
                        jump E_Facial            
        
                if renpy.showing("Emma_HJ_Animation") and E_Hand:
                        jump E_Handy_Finish
                elif renpy.showing("Emma_BJ_Animation") and E_Blow:
                        jump E_Handy_Finish
                elif renpy.showing("Emma_TJ_Animation") and E_Tit:
                        jump E_TitSpunk
                elif renpy.showing("Emma_SexSprite") and E_Sex and Trigger == "sex":
                        "She gently pushes you back off of her."
                        jump E_SpunkBelly
                elif renpy.showing("Emma_SexSprite") and E_Anal and Trigger == "anal":
                        "She gently pushes you back off of her."
                        jump E_SpunkBelly
                
        # Else. . . not experienced or she's not a huge fan, 
        if Trigger == "sex" or Trigger == "anal":
                call Emma_Sex_Reset
                "She pulls off of you and grabs your cock in her hand."
                jump E_Handy_Finish
        elif renpy.showing("Emma_TJ_Animation"):#hotdogging
                "She smiles and starts rubbing against you a bit faster."
                jump E_TitSpunk
        elif renpy.showing("Emma_SexSprite"):#hotdogging
                "She smiles and starts rubbing against you a bit faster."
                jump E_SpunkBelly
        else:
                jump E_Handy_Finish
    #End "Warn her" / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    
                      
                      
#Cum in mouth start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label E_In_Mouth:      
    if "classcaught" in E_RecentActions and bg_current == "bg classroom" and E_SEXP <= 10:
            #this skips this step if you haven't done much yet
            jump E_No_Cum
            
    if Trigger == "anal":
            $ Tempmod -= 15
    if "hungry" not in E_Traits and E_Addict <= 50 and "full" in E_RecentActions:
            $ Tempmod -= 15                  
                
    if Situation == "auto":
                $ Situation = 0
                if renpy.showing("Emma_TJ_Animation"):         
                        call EmmaFace("tongue")
                elif not renpy.showing("Emma_BJ_Animation"):
                        call Emma_BJ_Launch("cum")
                $ Speed = 5
                "You grab her head and cum in her mouth"  
                $E_Eyes = "closed"      
                if renpy.showing("Emma_TJ_Animation"): 
                        show Emma_TJ_Animation
                        with vpunch
                else:
                        show Emma_BJ_Animation
                        with vpunch
                if "full" in E_RecentActions:
                        #if she's had enough
                        call EmmaFace("bemused")
                        $ E_Spunk.append("mouth")
                        $ Speed = 0
                        "She gags a little, but manages to swallow it."
                        $ E_Spunk.remove("mouth")
                        ch_e "Hmm. . . that, may be a bit much for right now. . ."
                        ch_e "Perhaps we could find someplace else for you to. . . release. . ."
                elif E_Swallow >= 5 or "hungry" in E_Traits:
                        #if she likes to swallow
                        call EmmaFace("sexy")
                        $ E_Mouth = "smile"
                        $ E_Spunk.append("mouth")
                        "She quickly gulps it down and wipes her mouth."
                        $ E_Spunk.remove("mouth")
                        $ Speed = 0
                        ch_e "Delectable, [E_Petname]."
                        call EmmaFace
                elif E_Swallow:
                        call EmmaFace("bemused")
                        $ E_Spunk.append("mouth")
                        $ Speed = 0
                        "She gags a little, but manages to swallow it."
                        $ E_Spunk.remove("mouth")
                        ch_e "Your. . . flavor is growing on me, but perhaps some warning?"
                        call EmmaFace
                elif not E_Swallow and E_Addict >= 50 and E_Inbt < 400 and E_Blow < 10:
                        call EmmaFace("bemused", 1)
                        $ E_Spunk.append("mouth")
                        ". . ."            
                        $ E_Spunk.remove("mouth")
                        $ E_Spunk.append("hand")
                        $ Speed = 0
                        "She gags and spits it into her palm. Then she licks her lips, looks down at her dripping hand, blushes, and quickly wipes it off."
                        $ E_Spunk.remove("hand")
                        ch_e "That certainly is. . . rich. . ."
                        $ E_Addictionrate += 1
                        if "addictive" in P_Traits:
                            $ E_Addictionrate += 1
                        call EmmaFace
                        jump E_Orgasm_After
                elif not E_Swallow and E_Addict >= 50:
                        call EmmaFace("sexy")
                        $ E_Mouth = "tongue"
                        $ E_Spunk.append("mouth")
                        ". . ."
                        $ E_Spunk.remove("mouth")
                        $ E_Spunk.append("hand")
                        $ Speed = 0
                        "She gags and spits it into her palm. Then she licks her lips, looks down, and drinks up what's in her palm."
                        $ E_Spunk.remove("hand")
                        ch_e "I shouldn't reward such rude behavior. . . but it was nourishing."
                        call EmmaFace
                        call Statup("Emma", "Inbt", 30, 2)
                        call Statup("Emma", "Inbt", 50, 2)
                elif not E_Swallow:
                        if ApprovalCheck("Emma", 800, "LI") and ApprovalCheck("Emma", 400, "OI"):
                            call EmmaFace("angry")
                            $ E_Spunk.append("mouth")
                        else:
                            call EmmaFace("bemused")
                            $ E_Mouth = "tongue"
                            $ E_Spunk.append("mouth")
                        ". . ."
                        $ E_Spunk.append("hand")
                        $ Speed = 0
                        "She gags and spits it into her palm."   
                        menu:
                            ch_e "Did I say you could come in my mouth, [E_Petname]?"
                            "Sorry about that.":
                                    call Statup("Emma", "Love", 80, 1)
                                    $ E_Addictionrate += 1
                                    if "addictive" in P_Traits:
                                        $ E_Addictionrate += 1
                                    call EmmaFace("smile", 1)
                                    ch_e "Very well. . ."
                                    ch_e "Just warn me next time. . ."
                                    jump E_Orgasm_After
                                
                            "Why don't you try swallowing it?":
                                    if ApprovalCheck("Emma", 1200):
                                        "She tentatively licks her hand, and then gulps it down."
                                        $ E_Spunk.remove("hand")
                                        call EmmaFace("sexy", 1)
                                        $ E_Spunk.append("mouth")
                                        ch_e "Well, that was a bit of an acquired taste. . ."
                                        call Statup("Emma", "Obed", 50, 10)
                                        $ E_Spunk.remove("mouth")
                                    elif ApprovalCheck("Emma", 1200, "OI", Bonus = (E_Addict*10)):
                                        call EmmaFace("bemused", 1)
                                        $ E_Brows = "normal" 
                                        $ E_Mouth = "sad"
                                        $ E_Spunk.remove("hand")
                                        $ E_Spunk.append("mouth")
                                        "She scowls a bit, but licks her hand clean as she does so, and swallows it down."
                                        $ E_Spunk.remove("mouth")
                                        ch_e "I can't say that it would be my favorite flavor. . ."
                                        call Statup("Emma", "Obed", 50, 10)
                                    else:
                                        $ E_Spunk.remove("hand")
                                        "She scowls at you and wipes her hand off. Then she licks her lips."
                                        jump E_Orgasm_After
                                    
                            "Swallow it, now.":
                                    call Statup("Emma", "Love", 30, -1, 1)
                                    call Statup("Emma", "Love", 50, -1, 1)                    
                                    call Statup("Emma", "Love", 80, -1, 1)
                                    if ApprovalCheck("Emma", 1200, "OI") or E_Addict >= 50:                            
                                        call EmmaFace("sad", 1)
                                        $ E_Spunk.append("mouth")
                                        $ E_Spunk.remove("hand")
                                        "She scowls a bit, but licks her hand clean as she does so, and swallows it down."
                                        $ E_Spunk.remove("mouth")
                                        ch_e "I can't say that it would be my favorite flavor. . ."
                                        call Statup("Emma", "Obed", 50, 10)
                                    else:         
                                        $ E_Spunk.remove("hand")               
                                        "She scowls at you and wipes her hand off. Then she licks her lips."                        
                                        jump E_Orgasm_After
                else:                
                            jump E_Orgasm_After
                                
                jump E_Swallowed
                #end if not asked/auto / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
    
    $ Situation = 0
    "You ask if you can cum in her mouth."
    if renpy.showing("Emma_SexSprite"):
            call Emma_HJ_Launch("cum")
        
    if "full" in E_RecentActions:
            pass
        
    elif E_Swallow >= 5 or "hungry" in E_Traits:  
            # If she's swallowed 5 times, 
            call EmmaFace("sucking")
            if renpy.showing("Emma_TJ_Animation"):     
                call EmmaFace("tongue")
                $ Speed = 5 #shallow animation
                "She nods and bends down to put the tip between her lips."
            elif not renpy.showing("Emma_BJ_Animation"):
                call Emma_BJ_Launch("cum")     
                $ Speed = 6 if Speed == 4 else 5 #6 if deep throating, 5 if not
                "She nods and bends down to put the tip between her lips."
            else:            
                $ Speed = 2
                "She nods and hums a \"yes\" sound."
            $ E_Spunk.append("mouth")
            "After you cum, she quickly gulps it down and wipes her mouth."
            ". . ."
            call EmmaFace("sexy")            
            $ Speed = 0
            ch_e "Delectable, [E_Petname]."
            $ E_Spunk.remove("mouth")
            jump E_Swallowed
        
    elif E_Addict >= 80 and E_Swallow: 
            #addicted
            $ E_Brows = "confused"
            $ E_Eyes = "manic"
            if renpy.showing("Emma_TJ_Animation"):          
                call EmmaFace("tongue")
                $ Speed = 5 #shallow animation
                "She gently puts the tip to her lips, just as you blow."
            elif not renpy.showing("Emma_BJ_Animation"):
                call Emma_BJ_Launch("cum")    
                $ Speed = 6 if Speed == 4 else 5 #6 if deep throating, 5 if not
                "She gently puts the tip to her lips, just as you blow."
                $ E_Mouth = "sucking"
            else:            
                $ Speed = 2
                "She nods and hums a \"yes\" sound."
                $ E_Mouth = "sucking"
            $ E_Spunk.append("mouth")
            "She gags a little, but quickly swallows it."
            ". . ."
            $ Speed = 0
            call EmmaFace("sexy")
            $ E_Mouth = "smile"
            ch_e "I should be upset, but I can't say I didn't enjoy that. . ."
            $ E_Spunk.remove("mouth")
            call Statup("Emma", "Inbt", 200, 5)
            jump E_Swallowed
            
    elif E_Swallow:                
            if ApprovalCheck("Emma", 900):
                $ E_Brows = "confused"
                if renpy.showing("Emma_TJ_Animation"):         
                    call EmmaFace("tongue")
                    $ Speed = 5 #shallow animation
                    "She gently puts the tip to her lips, just as you blow."
                elif not renpy.showing("Emma_BJ_Animation"):
                    call Emma_BJ_Launch("cum")      
                    $ Speed = 6 if Speed == 4 else 5 #6 if deep throating, 5 if not
                    "She gently puts the tip to her lips, just as you blow."
                    $ E_Mouth = "sucking"
                else:            
                    $ Speed = 2
                    "She tilts her head and hums a \"hmm?\" sound."
                    $ E_Mouth = "sucking"
                $ E_Spunk.append("mouth")
                $ E_Brows = "normal"
                $ E_Eyes = "sexy"
                ". . ."
                $ Speed = 0
                call EmmaFace("sexy")
                $ E_Spunk.append("mouth")
                ch_e "It does grow on you. . ."
                $ E_Spunk.remove("mouth")
                jump E_Swallowed
     
    #If she hasn't swallowed or doesn't automatically want to. . .  
    
    if  ApprovalCheck("Emma", 300, "LI") or ApprovalCheck("Emma", 300, "OI"): 
        call EmmaFace("bemused")
        $ E_Eyes = "sexy"
    else:
        call EmmaFace("angry")
        
    $ Speed = 0    
    
    if "full" in E_RecentActions:
            ch_e "I couldn't finish another drop, [E_Petname]. . ." 
    else:
            ch_e "I can't imagine why I would. . ."
    
    menu:
        extend ""
        "Sorry about that.":
                call Statup("Emma", "Love", 80, 3)
                $ E_Addictionrate += 1
                if "addictive" in P_Traits:
                    $ E_Addictionrate += 1
                call EmmaFace("smile", 1)
                ch_e "It is a tempting offer. . ."
                if ApprovalCheck("Emma", 1200, TabM=1) and "full" not in E_RecentActions:
                    $ Approval = 2 
                    call Statup("Emma", "Inbt", 30, 3)
                    call Statup("Emma", "Inbt", 70, 2)  
                    call EmmaFace("sexy", 1)
                    ch_e "Perhaps a little bit. . ."
                else:
                    jump E_Handy_Finish                
            
        "Give it a try, you might like it." if "full" not in E_RecentActions:
                if ApprovalCheck("Emma", 1200, TabM=1):  
                    $ Approval = 2
                    call Statup("Emma", "Obed", 50, 5)
                    call Statup("Emma", "Obed", 70, 3)
                    $ E_Brows = "confused"  
                    $ E_Eyes = "sexy"
                    ch_e "If you insist. . ."
                else:     
                    $ E_Addictionrate += 1
                    if "addictive" in P_Traits:
                        $ E_Addictionrate += 1
                    $ E_Blush = 1
                    ch_e "I highly doubt that, [E_Petname]."
                    jump E_Handy_Finish
                            
        "Seriously, put it in your mouth.":
                if ApprovalCheck("Emma", 1500, "LI", TabM=1) or ApprovalCheck("Emma", 1200, "OI", TabM=1):
                        call EmmaFace("sucking", 1)
                elif ApprovalCheck("Emma", 1000, "OI", Bonus = (E_Addict*10)): #Mild addiction included                
                        call EmmaFace("angry", 1)
                else: 
                        #You insisted, she refused. 
                        call EmmaFace("angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        call Emma_HJ_Launch("cum")
                        call Emma_HJ_Reset                
                        call Statup("Emma", "Love", 50, -3, 1)
                        call Statup("Emma", "Love", 80, -4, 1)
                        ch_e "I think you overestimate your charms."
                        call Statup("Emma", "Obed", 30, -1, 1)
                        call Statup("Emma", "Obed", 50, -1, 1)  
                        $ E_RecentActions.append("angry")
                        $ E_DailyActions.append("angry")   
                        $ Line = 0
                        return      
                if renpy.showing("Emma_TJ_Animation"):         
                    call EmmaFace("tongue")
                    $ Speed = 5 #shallow animation
                else:
                    $ E_Mouth = "sucking"
                    call Emma_BJ_Launch("cum")            
                    $ Speed = 5 
                call Statup("Emma", "Obed", 50, 10)
                call Statup("Emma", "Obed", 70, 5)
    
    if renpy.showing("Emma_TJ_Animation"):          
        call EmmaFace("tongue")
        $ Speed = 5 #shallow animation                         
    elif not renpy.showing("Emma_BJ_Animation"):
        call Emma_BJ_Launch("cum")     
        $ Speed = 6 if Speed == 4 else 5 #6 if deep throating, 5 if not
    $ E_Spunk.append("mouth")
    if ApprovalCheck("Emma", 1200):            
            "She gently puts the tip to her lips, just as you blow."
            "She coughs a little, but quickly swallows it." 
    else:
            "She tentatively places the tip in her mouth, and you blast inside it."
            "She quickly gulps it down."                    
            call EmmaFace("sexy")
            call Statup("Emma", "Love", 50, -3, 1)
            call Statup("Emma", "Love", 80, -4, 1)        
    $ E_Mouth = "sucking"
    ". . ."   
    $ Speed = 0            
    call EmmaFace("sexy") 
    
    if ApprovalCheck("Emma", 1000) and E_Swallow >= 3:
            ch_e "It does grow on you. . ."    
    elif ApprovalCheck("Emma", 800):                
            ch_e "Well, that was a bit of an acquired taste. . ."
    else:
            call EmmaFace("sad")
            ch_e "I can't say that it would be my favorite flavor. . ."   
    call Statup("Emma", "Inbt", 30, 3)
    call Statup("Emma", "Inbt", 50, 2)            
    $ E_Blow += 1
    jump E_Swallowed     
    #end Emma in mouth  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Creampie  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label E_Creampie_P:
        if Trigger == "sex" and Situation == "auto":
                $ P_Cock = "in"
                $ E_Spunk.append("in")
                $ P_Spunk = "in"
                $ Speed = 4
                if ApprovalCheck("Emma", 1300) or E_CreamP:              
                        call EmmaFace("surprised", Eyes="down")
                        "You come in her pussy. Her eyes widen in surprise, but she takes it in stride."  
                        call EmmaFace("sexy")
                        if E_Lust >= 85: 
                            call E_Cumming
                else:
                    if E_Lust >= 85: 
                            "You come in her pussy. Her eyes widen in surprise and she shakes a bit."
                            call E_Cumming                
                    else:
                            "You come in her pussy. Her eyes widen in surprise and she pulls out."
                    $ P_Cock = "out"
                    call EmmaFace("angry")
                    ch_e "Perhaps some warning next time?"
                    call EmmaFace("bemused")
                    ch_e "Not that it didn't feel good at the time. . ."
                    
                jump E_Creampied
        
        #else (You ask her if it's ok):
        if ApprovalCheck("Emma", 1200) or E_CreamP:        
                call EmmaFace("sexy")
                if E_CreamP >= 3:
                    "She smiles and speeds up her actions, causing you to erupt inside her."  
                elif E_CreamP:
                    "She gets a michevious look and speeds up, you burst inside her." 
                else:
                    "As you continue to pound her, she nods her head."
                $ P_Cock = "in"
                $ E_Spunk.append("in")
                $ P_Spunk = "in"
                $ Speed = 4
                if E_Lust >= 85: 
                    call E_Cumming  
                call Statup("Emma", "Love", 90, 1) 
                ch_e "How very. . . filling."
                jump E_Creampied
        else:
                call EmmaFace("sexy")
                call Statup("Emma", "Love", 80, 2) 
                call Statup("Emma", "Love", 90, 2) 
                ch_e "Thanks for warning me *grunt* [E_Petname], but perhaps not."
        jump E_SpunkBelly

#Start Anal Creampie  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label E_Creampie_A:                             
        # These need conditionals added    
        if Trigger == "anal" and Situation == "auto":
                $ P_Cock = "anal"
                $ E_Spunk.append("anal")
                $ P_Spunk = "anal"
                $ Speed = 4
                if ApprovalCheck("Emma", 1200) or E_CreamP:              
                    call EmmaFace("surprised", 1, Eyes="down")
                    "You come in her ass. Her eyes widen in surprise, but she takes it in stride."  
                    call EmmaFace("sexy")
                    if E_Lust >= 85: 
                        call E_Cumming
                else:
                    if E_Lust >= 85: 
                        "You come in her ass. Her eyes widen in surprise and she shakes a bit."
                        call E_Cumming                
                    else:
                        "You come in her ass. Her eyes widen in surprise and she pulls out."
                    $ P_Cock = "out"
                    call EmmaFace("angry")
                    ch_e "No advanced warning, [E_Petname]?"
                    call EmmaFace("bemused")
                    ch_e "I suppose it was rather. . . filling though."
                jump E_Creampied
            
        #else (You ask her if it's ok):
        if ApprovalCheck("Emma", 1200) or E_CreamP:        
                call EmmaFace("sexy")
                if E_CreamP >= 3:
                    "She smiles and speeds up her actions, causing you to erupt inside her."  
                elif E_CreamP:
                    "She gets a michevious look and speeds up, you burst inside her." 
                else:
                    "As you continue to pound her, she nods her head."
                $ P_Cock = "anal"
                $ E_Spunk.append("anal")
                $ P_Spunk = "anal"
                $ Speed = 4
                if E_Lust >= 85: 
                    call E_Cumming  
                call Statup("Emma", "Love", 90, 1) 
                ch_e "Mmmm, I feel so full. . ."
                jump E_Creampied
        else:
                call EmmaFace("sexy")     
                call Statup("Emma", "Love", 80, 2) 
                ch_e "Thanks for warning me *grunt* [E_Petname], but perhaps not."
        jump E_SpunkBelly
            
#Start Facial  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    
label E_Facial: 
    if renpy.showing("Emma_BJ_Animation"):       
            if E_Addict >= 60 and ApprovalCheck("Emma", 1000, "I", Bonus = ((E_Addict*10)- E_Obed)) and E_Swallow:
                    $ E_Eyes = "manic"
                    $ E_Blush = 1
                    $ Speed = 0
                    "You pull out of her mouth with a pop, and her eyes widen in surprise." 
                    $ Speed = 4
                    $ E_Spunk.append("mouth")
                    "She leaps at your cock and sucks it deep, draining your fluids hungrily."
                    $ E_Mouth = "lipbite"
                    $ Speed = 0
                    "When she finishes, she draws her hand across her lips."
                    call EmmaFace("bemused")
                    $ E_Spunk.remove("mouth")
                    ch_e "I'm sorry, [E_Petname], but waste not want not."
                    call Statup("Emma", "Obed", 80, -5)
                    call Statup("Emma", "Inbt", 200, 10)
                    jump E_Swallowed
            call Emma_HJ_Launch("cum")
            $ Speed = 2
            $ E_Spunk.append("facial")
            "You pull out of her mouth with a pop, and she strokes you off. You spray all over her face."
            $ Speed = 0
            jump E_Orgasm_After
    
    if not renpy.showing("Emma_TJ_Animation") and not renpy.showing("Emma_HJ_Animation"):      
            call Emma_HJ_Launch("cum")
            $ Speed = 2
    $ E_Spunk.append("facial")
    "As you're about to finish, you pull out, aim squarely at her face, and spray all over it."
    $ Speed = 0

    if Situation == "warn":
        ch_e "I appreciate the warning. . . perhaps not the mess though. . ." 
    else:
        ch_e "What a mess, a warning would have been appreciated." 
                
    jump E_Orgasm_After

#Start titjob spunk  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    
label E_TitSpunk: 
    if renpy.showing("Emma_BJ_Animation"):       
            if E_Addict >= 60 and ApprovalCheck("Emma", 1000, "I", Bonus = ((E_Addict*10)- E_Obed)) and E_Swallow:
                    $ E_Eyes = "manic"
                    $ E_Blush = 1
                    $ Speed = 0
                    "You pull out of her mouth with a pop, and her eyes widen in surprise." 
                    $ Speed = 4
                    $ E_Spunk.append("mouth")
                    "She leaps at your cock and sucks it deep, draining your fluids hungrily."
                    $ E_Mouth = "lipbite"
                    $ Speed = 0
                    "When she finishes, she draws her hand across her lips."
                    call EmmaFace("bemused")
                    $ E_Spunk.remove("mouth")
                    ch_e "I'm sorry, [E_Petname], but waste not want not."
                    call Statup("Emma", "Obed", 80, -5)
                    call Statup("Emma", "Inbt", 200, 10)
                    jump E_Swallowed
               
    if not renpy.showing("Emma_TJ_Animation") and not renpy.showing("Emma_HJ_Animation") and not renpy.showing("Emma_BJ_Animation"):      
            call Emma_TJ_Launch("cum")
    $ E_Spunk.append("tits")
    $ Speed = 0
    "As you're about to finish, you speed up and spray all over her chest."

    if Situation == "warn":
        ch_e "I appreciate the warning. . . perhaps not the mess though. . ." 
    else:
        ch_e "What a mess, a warning would have been appreciated." 
                
    jump E_Orgasm_After
    
# Start Spunk back  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
###ANON MOD CODE BLOCK START #####
#placeholderline1 
label E_SpunkBellyMissionary: 
        if P_Cock != "foot":
                call Emma_Missionary_Launch("hotdog")
        $ Speed = 0
        if E_Addict >= 60 and ApprovalCheck("Emma", 1000, "I", Bonus = ((E_Addict*10)- E_Obed))  and E_Swallow:
                $ E_Eyes = "manic"
                $ E_Blush = 1
                call Emma_BJ_Launch("cum")
                if Trigger == "sex":
                    "You pull out of her pussy with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
                elif Trigger == "anal":                
                    "You pull out of her ass with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
                $ E_Mouth = "lipbite"
                $ E_Spunk.append("mouth")
                "When she finishes, she licks her lips."
                call EmmaFace("bemused")
                $ E_Spunk.remove("mouth")
                ch_k "Sorry, that's just[E_like]sooooo good."
                call Statup("Emma", "Obed", 80, -5)
                call Statup("Emma", "Inbt", 200, 10)
                jump E_Swallowed
        if P_Cock != "foot":
            $ P_Cock = "out"
        $ P_Spunk = "out"
        $ E_Spunk.append("belly")
        if Trigger == "sex":
                "You pull out of her pussy with a pop and spray all over her belly."
        elif Trigger == "anal":
                "You pull out of her ass with a pop and spray all over her belly."
        else:
                "You pick up the pace and with a grunt you spray all over her belly."
            
                      
        if E_Addict >= 60 and ApprovalCheck("Emma", 800, "I", Bonus = ((E_Addict*10)- E_Obed)) and E_Swallow: 
                #if she's manic and has swallowed
                $ E_Eyes = "manic"
                $ E_Blush = 1        
                "Emma's eyes widen with desire, and she quickly wipes a bit off with her hand, then licks her fingers clean."
                call EmmaFace("manic", 1)
                $ E_Spunk.append("mouth")
                $ E_Mouth = "smile"
                ch_k "Sorry, that's just[E_like]sooooo good."
                $ E_Spunk.remove("mouth")
                call Statup("Emma", "Inbt", 50, 3)
                jump E_Swallowed
              
            
        #else . . .
        call EmmaFace("sexy", 1)
        ch_k "Mmmm, all over the place. . ."
#        call Emma_Sex_Reset
        jump E_Orgasm_After
###ANON MOD CODE MISSIONARY BLOCK STOP ######
label E_SpunkBack: 
        if Trigger != "foot":
            call Emma_Doggy_Launch("hotdog")
        $ Speed = 0
        if E_Addict >= 60 and ApprovalCheck("Emma", 1000, "I", Bonus = ((E_Addict*10)- E_Obed))  and E_Swallow:
                $ E_Eyes = "manic"
                $ E_Blush = 1
                call Emma_BJ_Launch("cum")
                if Trigger == "sex":
                    "You pull out of her pussy with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
                elif Trigger == "anal":                
                    "You pull out of her ass with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
                $ E_Mouth = "lipbite"
                $ E_Spunk.append("mouth")
                "When she finishes, she licks her lips."
                call EmmaFace("bemused")
                $ E_Spunk.remove("mouth")
                ch_r "Sorry, [E_Petname], I just couldn't let that go to waste."
                call Statup("Emma", "Obed", 80, -5)
                call Statup("Emma", "Inbt", 200, 10)
                jump E_Swallowed
        if Trigger != "foot":
            $ P_Cock = "out"
        $ E_Spunk.append("back")
        if Trigger == "sex":
                "You pull out of her pussy with a pop and spray all over her backside."
        elif Trigger == "anal":
                "You pull out of her ass with a pop and spray all over her backside."
        else:
                "You pick up the pace and with a grunt you spray all over her backside."
            
                      
        if E_Addict >= 60 and ApprovalCheck("Emma", 800, "I", Bonus = ((E_Addict*10)- E_Obed)) and E_Swallow: 
                #if she's manic and has swallowed
                $ E_Eyes = "manic"
                $ E_Blush = 1        
                "Emma's eyes widen with desire, and she quickly wipes a bit off with her hand, then licks her fingers clean."
                call EmmaFace("manic", 1)
                $ E_Spunk.append("mouth")
                $ E_Mouth = "smile"
                ch_r "Well, [E_Petname], I just couldn't let that go to waste."
                $ E_Spunk.remove("mouth")
                call Statup("Emma", "Inbt", 50, 3)
                jump E_Swallowed
              
            
        #else . . .
        call EmmaFace("sexy", 1)
        ch_r "Thanks for the courtesy, [E_Petname]. Such a mess though. . ." 
#        call Emma_Sex_Reset
        jump E_Orgasm_After
###ANON MOD CODE BLOCK STOP ######
###ANON MOD CODE BLOCK STOP ######
label E_SpunkBelly:   
    
    call Emma_Sex_Launch("hotdog")
    if E_Addict >= 60 and ApprovalCheck("Emma", 1000, "I", Bonus = ((E_Addict*10)- E_Obed))  and E_Swallow:
            $ E_Eyes = "manic"
            $ E_Blush = 1
            call Emma_BJ_Launch("cum")
            if Trigger == "sex":
                "You pull out of her pussy with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
            elif Trigger == "anal":                
                "You pull out of her ass with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
            $ E_Mouth = "lipbite"
            $ E_Spunk.append("mouth")
            "When she finishes, she draws her hand across her lips."
            call EmmaFace("bemused")
            $ E_Spunk.remove("mouth")
            ch_e "I'm sorry, [E_Petname], but that would have been a waste."
            call Statup("Emma", "Obed", 80, -5)
            call Statup("Emma", "Inbt", 200, 10)
            jump E_Swallowed
    $ P_Cock = "out"
    $ P_Spunk = "out"    
    $ Speed = 4
    $ E_Spunk.append("belly")
    if Trigger == "sex":
            "You pull out of her pussy with a pop and spray all over her belly."
    elif Trigger == "anal":
            "You pull out of her ass with a pop and spray all over her belly."
    else:
            "You pick up the pace and with a grunt you spray all over her belly."
        
                  
    if E_Addict >= 60 and ApprovalCheck("Emma", 800, "I", Bonus = ((E_Addict*10)- E_Obed)) and E_Swallow: 
            #if she's manic and has swallowed
            $ E_Eyes = "manic"
            $ E_Blush = 1        
            "Emma's eyes widen with desire, and she quickly wipes a bit off with her hand, then licks her fingers clean."
            call EmmaFace("manic", 1)
            $ E_Spunk.append("mouth")
            $ E_Mouth = "smile"
            ch_e "Well, [E_Petname], I just couldn't let that go to waste."
            $ E_Spunk.remove("mouth")
            call Statup("Emma", "Inbt", 50, 3)
            jump E_Swallowed
          
        
    #else . . .
    call EmmaFace("sexy", 1)
    ch_e "Hmm. . . you do make a mess. . ."  
#    call Emma_Sex_Reset
    jump E_Orgasm_After
    
   
#Start Handy finish  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label E_Handy_Finish:
    if renpy.showing("Emma_SexSprite"):
        call Emma_Sex_Reset
    if renpy.showing("Emma_FJ_Animation"): 
        jump E_Foot_Finish
    call Emma_HJ_Launch("cum")
    $ Speed = 2        
    $ E_Spunk.append("hand")  
    if renpy.showing("Emma_HJ_Animation"):                                  
            "She grins and speeds up her efforts, placing her left hand over your tip. You burst all over her hands." 
    else:
            "She grins and starts jerking you off, placing her left hand over your tip. You burst all over her hands." 
    $ Speed = 0
    
    if E_Addict > 80 or "hungry" in E_Traits:
            $ E_Eyes = "manic"
            $ E_Spunk.remove("hand")
            $ E_Spunk.append("mouth")
            $ E_Mouth = "smile"
            "She licks her hands off with a satisfied grin."
            $ E_Spunk.remove("mouth")
            ch_e "Hmmm. . ."
    else:
            call EmmaFace("bemused")
            $ E_Spunk.remove("hand")
            "She wipes her hands off, but takes a quick sniff when she's done and smiles."
            ch_e "I appreciate the warning." 
            jump E_Orgasm_After

 
#Start Foot finish  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label E_Foot_Finish:
    if renpy.showing("Emma_SexSprite"):
        call Emma_Sex_Reset
    call Emma_FJ_Launch
    $ Speed = 4        
    $ E_Spunk.append("belly")  
    if renpy.showing("Emma_FJ_Animation"):                                  
            "She grins and speeds up her efforts, sliding her foot along your cock. You burst all over her belly." 
    else:
            "She grins and starts jerking you off with her foot, sliding her foot along your cock. You burst all over her belly." 
    $ P_Spunk = 1  
    $ Speed = 0
    
    if E_Addict > 80 or "hungry" in E_Traits:
            $ E_Eyes = "manic"
            $ E_Spunk.remove("belly")
            $ E_Spunk.append("mouth")
            $ E_Mouth = "smile"
            "She wipes the cum into her mouth with a satisfied grin."
            $ E_Spunk.remove("mouth")
            ch_e "Hmmm. . ."
    else:
            call EmmaFace("bemused")
            ch_e "I appreciate the warning." 
            jump E_Orgasm_After
            
#Start Swallowed  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label E_Swallowed: 
        $ E_Swallow += 1
        call Statup("Emma", "Inbt", 50, 3)
        $ E_Addict -= 20    
        if "mouth" in E_Spunk:
                $ E_Spunk.remove("mouth")
        if "full" not in E_RecentActions and Action_Check("Emma", "recent", "swallowed") >= 5: 
                $ E_RecentActions.append("full")    
                call EmmaFace("surprised", 1)
                ch_e "-ehem-"
                call EmmaFace("sexy", 1)
                ch_e "Excuse me [E_Petname], it must have been something I ate."
        $ E_RecentActions.append("swallowed")                      
        $ E_DailyActions.append("swallowed") 
        $ E_Addictionrate += 2
        if "addictive" in P_Traits:
                $ E_Addictionrate += 2
        if Trigger == "anal":    
                call Statup("Emma", "Obed", 50, 2)
                call Statup("Emma", "Obed", 200, 2)
        if E_Swallow == 1:
                $E_SEXP += 12
                call Statup("Emma", "Inbt", 70, 5)
        jump E_Orgasm_After

#Start Creampied  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label E_Creampied:
    if Trigger == "sex":
            $ E_CreamP += 1
            call Statup("Emma", "Lust", 200, 10)
            $ E_RecentActions.append("creampie sex")                      
            $ E_DailyActions.append("creampie sex") 
    elif Trigger == "anal":
            $ E_CreamA += 1
            call Statup("Emma", "Lust", 200, 5)
            $ E_RecentActions.append("creampie anal")                      
            $ E_DailyActions.append("creampie anal") 
    call Statup("Emma", "Inbt", 50, 3)
    $ E_Addict -= 30
    $ E_Addictionrate += 2
    if "addictive" in P_Traits:
            $ E_Addictionrate += 3
    if E_CreamP == 1:
            $E_SEXP += 10
            call Statup("Emma", "Inbt", 70, 5)
#    call Emma_Sex_Reset

# Clean-up / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label E_Orgasm_After:
        $ Line = "What next?"
        if not renpy.showing("Emma_HJ_Animation"):
            $ Emma_Arms = 1
        $ P_Semen -= 1
        $ P_Focus = 0
        $ Speed = 0  
        menu:
                "Want her to clean you off?"
                "Yes":
                    call E_CleanCock
                "Actually, let [Partner] do it." if Partner:
                    call AllReset("Emma") #resets the position of the orignal lead
                    call Partner_Clean
                    call AllReset("Emma") #resets the position of the orignal lead
                "No":
                    pass
        if E_Spunk:
                call Emma_Cleanup
        $ Situation = 0
        return
        
    
label E_CleanCock:
        $ Line = "What next?"
        if not renpy.showing("Emma_HJ_Animation"):
            $ Emma_Arms = 1
        $ P_Cock = "out"
        $ Speed = 0    
        if Trigger == "anal" and not ApprovalCheck("Emma", 1600, TabM=1) and not E_Addict >= 80:
                "She wipes your cock clean."
        elif "classcaught" in E_RecentActions and bg_current == "bg classroom" and E_SEXP <= 10:
                #this skips this step if you haven't done much yet
                "She wipes your cock clean."
        elif E_Blow > 3 or E_Swallow: 
                if ApprovalCheck("Emma", 1200, TabM=1) or E_Addict >= 60:
                        call Emma_BJ_Launch("cum")
                        $ Speed = 1
                        call EmmaFace("sucking", 1) 
                        if ApprovalCheck("Emma", 1500, TabM=1):
                            if Partner and ApprovalCheck(Partner, 1500, TabM=1):
                                "Both girls look up at you as they lick your cock clean."
                            elif E_Love > E_Inbt and E_Love > E_Obed:
                                $ E_Eyes = "sly"
                                "She looks up at you lovingly as she licks your cock clean."            
                            elif E_Obed > E_Inbt:
                                $ E_Eyes = "side"
                                "She dutifully licks your cock clean with lowered eyes."
                                call Statup("Emma", "Obed", 80, 3)                
                            else:
                                "She happily licks your cock clean." 
                        elif E_Addict >= 60:
                                "She hungrily and thoroughly licks your cock clean."   
                        else:
                            "She licks you cock clean." 
                        call EmmaFace("sexy")  
                else:
                        if not renpy.showing("Emma_HJ_Animation"):
                            call Emma_HJ_Launch("cum") 
                        if Partner and ApprovalCheck(Partner, 1000, TabM=1):
                            "Both girls reach down and wipe your cock clean."
                        else:
                            "She wipes your cock clean."  
        else:
                        if not renpy.showing("Emma_HJ_Animation"):
                            call Emma_HJ_Launch("cum") 
                        if Partner and ApprovalCheck(Partner, 1000, TabM=1):
                            "Both girls reach down and wipe your cock clean."
                        else:
                            "She wipes your cock clean."         
        $ P_Spunk = 0
        call EmmaFace("sexy") 
        return
    
# End You Cumming //////////////////////////////////////////////////////////////////////////////////


# Emma Lusty face check ////////////////////////////////////////////////////////////////////////////////
label EmmaLust(Extreme = 0, Kissing = 0):
                
    if E_Lust >= 90:        
            $ E_Blush = 2
    elif E_Lust >= 40:        
            $ E_Blush = 1 
        
    if E_Lust >= 80:
            $ E_Wet = 2 
    elif E_Lust >= 50:
            $ E_Wet = 1
            
    if E_Loc == "bg teacher" and not Extreme:
            #this prevents her face from changing if she's just being a teacher.
            return
       
    if Trigger3 == "kiss both" or Trigger3 == "kiss girl":
            #if the girls are kissing or all three are
            $ Kissing = 1
    elif Trigger4 == "kiss both" or Trigger3 == "kiss girl":
            #if the girls are kissing or all three are
            $ Kissing = 1   
    elif Partner != "Emma":
            #If Emma is kissing and is primary
            if Trigger == "kiss you" or Trigger2 == "kiss you":  
                $ Kissing = 1
    elif Trigger4 == "kiss you":   
            #If Emma is kissing you in a threesome action
            $ Kissing = 1
            
    if Kissing:
            $ E_Eyes = "closed"
            if E_Kissed >= 10 and E_Inbt >= 300:
                $ E_Mouth = "sucking"
            elif E_Kissed > 1 and E_Addict >= 50:            
                $ E_Mouth = "sucking"
            else:
                $ E_Mouth = "kiss"
                
    else:    
            #If Emma is not kissing someone
            if E_Lust >= 90:
                    $ E_Eyes = "closed"
                    $ E_Brows = "sad"
                    $ E_Mouth = "surprised"
            elif E_Lust >= 70:
                    $ E_Eyes = "sexy"
                    $ E_Brows = "sad"
                    $ E_Mouth = "lipbite"
            elif E_Lust >= 50 and not Extreme:
                    $ E_Eyes = "squint"
                    $ E_Brows = "sad"
                    $ E_Mouth = "lipbite"
            elif E_Lust >= 30 and not Extreme:
                    $ E_Eyes = "sexy"
                    $ E_Brows = "normal"
                    $ E_Mouth = "smirk"
            elif not Extreme:
                    $ E_Eyes = "sexy"
                    $ E_Brows = "normal"
                    $ E_Mouth = "smirk"    
    
    if Partner == "Emma" and Trigger4 in ("lick pussy", "lick ass", "blow", "suck breasts"):         
                    $ E_Mouth = "tongue"  
    elif Trigger3 in ("lick pussy", "lick ass", "suck breasts"):         
                    $ E_Mouth = "tongue"  
                    
    if E_OCount >= 10:   
            #If you've fucked her senseless
            $ E_Eyes = "stunned"
            $ E_Mouth = "tongue"   
                
    return

# End faces

#  Emma Orgasm //////////////////////////

label E_Cumming(Quick=0):
    $ E_Eyes = "surprised"
    $ E_Brows = "sad"
    $ E_Mouth = "tongue"
    $ E_Blush = 1
    ch_e ". . . !"
    $ Speed = 0
    if renpy.showing("Emma_SexSprite"):
            show Emma_SexSprite #fix, test this
            with vpunch
    elif renpy.showing("Emma_BJ_Animation"):           #fix, make this animation work better when paused for this effect.
            show Emma_BJ_Animation
            with vpunch
    elif renpy.showing("Emma_TJ_Animation"):
            show Emma_TJ_Animation  
            with vpunch
    elif renpy.showing("Emma_HJ_Animation"):
            show Emma_HJ_Animation  
            with vpunch
    else:
            show Emma_Sprite
            with vpunch
    $ Speed = 1
    $ Line = renpy.random.choice(["Emma is suddenly rocked with spasms, holding back a muffled scream.", 
                "Emma grabs on tightly as her body shakes with pleasure.", 
                "Emma stiffens and lets out a low moan.",
                "Emma's body quivers and suddenly goes still."])
    "[Line]"    
    if Quick:
            call AnyFace("Emma","sexy",2)  
            $ E_Lust = 20
            return
    $ E_Eyes = "closed"
    $ E_Brows = "sad"
    $ E_Mouth = "tongue"
    $ Line = renpy.random.choice(["Oooooh. . . lovely.", 
                "I really enjoyed that one. . .", 
                "Hmmmm. . . .",
                "That was. . . greaaaaat. . ."])
    ch_e "[Line]"
           
    
    $ E_Lust = 30 if "hotblooded" in E_Traits else 0 
    $ E_Lust += (E_OCount * 5)
    $ E_Lust = 80 if E_Lust >= 80 else E_Lust    
    call Statup("Emma", "Inbt", 50, 1)
    call Statup("Emma", "Inbt", 70, 1)
            
    if "unsatisfied" in E_RecentActions:  #If she had been unsatisfied, you satisfied her. . .        
            call Statup("Emma", "Love", 70, 2)
            call Statup("Emma", "Love", 90, 1)
            if "unsatisfied" in E_DailyActions:
                ch_e "Making up for past mistakes, [E_Petname]?"
            call DrainWord("Emma","unsatisfied")
    $ E_OCount += 1        
    $ E_Org += 1
    $ Line = 0
      
    if Trigger != "masturbation":
            call Statup("Emma", "Lust", 40, 1)
            call Statup("Emma", "Love", 70, 1)
            call Statup("Emma", "Love", 90, 1)
            call Statup("Emma", "Obed", 50, 2)
            call Statup("Emma", "Obed", 70, 2)  
            if E_OCount == 1:
                    # if she's angry, but not too angry, then reduce that on the first O of the time block.
                    $ E_ForcedCount -= 1 if 5 > E_ForcedCount > 0 else 0 
            
            #checks to check reaction of other girls
            if K_Loc == bg_current and "noticed Emma" in K_RecentActions: 
                    $ K_Lust += 15 if K_LikeEmma >= 500 else 10
                    $ K_Lust += 5 if K_Les >= 5 else 0
            elif R_Loc == bg_current and "noticed Emma" in R_RecentActions: 
                    $ R_Lust += 15 if R_LikeEmma >= 500 else 10
                    $ R_Lust += 5 if R_Les >= 5 else 0 
            elif L_Loc == bg_current and "noticed Emma" in L_RecentActions: 
                    $ L_Lust += 15 if L_LikeEmma >= 500 else 10
                    $ L_Lust += 5 if L_Les >= 5 else 0 
            if Partner == "Emma":
                    #If the active girl is someone else
                    call Partner_Cumming("Emma")  
            #Orgasm count
            if Trigger != "blow" and Trigger != "hand" and Partner != "Emma":
                if E_OCount == 2:
                        $ E_Brows = "confused"
                        ch_e "Excellent job, [E_Petname]. . ."
                        call Statup("Emma", "Love", 50, 1)
                        call Statup("Emma", "Love", 80, 2)
                        call Statup("Emma", "Obed", 50, 1)
                        call Statup("Emma", "Obed", 60, 1)            
                elif E_OCount == 3: #5
                        $ E_Brows = "confused"            
                        ch_e "You . . .certainly. . . have some. . . stamina. . ."
                        call Statup("Emma", "Love", 50, 2)
                        call Statup("Emma", "Love", 80, 2)
                        call Statup("Emma", "Obed", 30, 1)
                        call Statup("Emma", "Obed", 50, 1)                    
                elif E_OCount == 5 and Partner != "Emma": #10
                    $ E_Mouth = "tongue"    
                    ch_e "You're . . .practically. . . exhausting. . ."
                    menu:
                        ch_e "would. . . you. . . mind. . . a break?"
                        "Finish up." if P_FocusX:
                            "You release your concentration. . ."                 
                            $ P_FocusX = 0
                            $ P_Focus += 15                    
                        "Let's try something else." if MultiAction:  
                            $ Situation = "shift"
                        "No, I'm not done yet.":
                            if Trigger == "sex" or Trigger == "anal":
                                if ApprovalCheck("Emma", 1000, TabM=1) or ApprovalCheck("Emma", 400, "O", TabM=1):
                                    call Statup("Emma", "Love", 200, -5)
                                    call Statup("Emma", "Obed", 50, 2)
                                    call Statup("Emma", "Obed", 80, 3)
                                    $ E_Eyes = "stunned"
                                    "She drifts off into incoherent moans."
                                else:
                                    call EmmaFace("angry", 1)
                                    "She scowls at you, pulls out with a pop, and wipes herself off."
                                    ch_e "Learn to take a hint. . ."
                                    call Statup("Emma", "Love", 50, -3, 1)
                                    call Statup("Emma", "Love", 80, -4, 1)
                                    call Statup("Emma", "Obed", 30, -1, 1)
                                    call Statup("Emma", "Obed", 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                            else:
                                call Statup("Emma", "Obed", 50, 3)
                                call Statup("Emma", "Obed", 80, 2)
                                $ E_Eyes = "stunned"
                                "She drifts off into incoherent moans."  
                #end Ocount stuff
    if Trigger == "strip":
            call AllReset("Emma")
            show Emma_Sprite at Emma_Dance1()
            "Emma begins to dance again."
    return
    
# End Emma Orgasm /////////////////////////////////////////////////////////////////////////////////////


# Start Emma Clean-Up /////////////////////////////////////////////////////////////////////////////////////
label Emma_Cleanup(Choice = "random",Options=[],Cnt=0,Cleaned=0,Original="Emma"):
    
    if Choice == "after":
            # This is at the end of a session            
            if not E_Spunk:
                $ E_Wet = 0
                return    
            $ Cnt = 1  
        
    if E_Addict > 80 and E_Swallow:
        #if she likes cum, she prefers to eat it. 
        $ Choice = "eat"            
        $ E_Eyes = "manic"
        $ E_Mouth = "smile" 
    elif Cnt and "taboo" not in E_History:
        $ Choice = "clean"           
    elif Choice == "ask":
        pass
    elif "painted" in E_RecentActions and ApprovalCheck("Emma", 1000, "OI"):
        return
    elif ApprovalCheck("Emma", 1200, "LO"):  
        $ Choice = "ask"            
    elif not ApprovalCheck("Emma", 400, "I"):
        call EmmaFace("bemused") 
        $ Choice = "clean"   
    else:
        $ Choice = "ask"      
   
    if Ch_Focus != "Emma":
        # if Emma isn't the lead, swap to her.
        $ Original = Partner
        call Shift_Focus("Emma")
        
    $ Cleaned = 1 if "cleaned" in E_DailyActions else 0
    $ E_RecentActions.append("cleaned") 
    $ E_DailyActions.append("cleaned") 
    
    if Choice == "ask":
            $ Choice = "random"
            "Emma looks down at the spunk covering her."
            menu:
                "What do you suggest Emma do about cleaning up?"
                "You should leave it where it is.":
                        if not Cnt:
                            # If this isn't the end of the session
                            if ApprovalCheck("Emma", 300, "I") or ApprovalCheck("Emma", 1000):
                                    call Statup("Emma", "Obed", 70, 1)
                                    call Statup("Emma", "Inbt", 50, 1)
                                    call Statup("Emma", "Lust", 90, 2) 
                                    $ Choice = "leave"  
                                    call EmmaFace("sly") 
                                    ch_e "Hmm. . ."
                            else:
                                    call EmmaFace("sly") 
                                    ch_e "Too undignified, [E_Petname]." 
                        elif ApprovalCheck("Emma", 900, "I") or "exhibitionist" in E_Traits:
                                call Statup("Emma", "Obed", 70, 2)
                                call Statup("Emma", "Obed", 90, 1)
                                call Statup("Emma", "Lust", 90, 5) 
                                $ Choice = "leave"  
                                call EmmaFace("sly") 
                                ch_e "Hmm. . . I suppose I could use some accessories. . "
                        elif ApprovalCheck("Emma", 600, "I") and ApprovalCheck("Emma", 1200, "LO"):
                                call Statup("Emma", "Obed", 90, 1)
                                call Statup("Emma", "Inbt", 80, 1) 
                                call Statup("Emma", "Lust", 90, 5) 
                                $ Choice = "leave"  
                                call EmmaFace("surprised",2) 
                                ch_e "Hmm. . . if you insist. . ."
                                call EmmaFace("sly",1) 
                        
                        else:
                            call EmmaFace("angry") 
                            menu:
                                ch_e "Excuse me?" 
                                "Please?":
                                    if ApprovalCheck("Emma", 1800):
                                        call Statup("Emma", "Love", 85, 1)
                                        call Statup("Emma", "Obed", 50, 2)
                                        call Statup("Emma", "Obed", 80, 1)
                                        call Statup("Emma", "Inbt", 40, 3) 
                                        call Statup("Emma", "Inbt", 80, 1) 
                                        ch_e "Well. Ok."
                                        $ Choice = "leave"  
                                    elif Cleaned:
                                        call EmmaFace("angry") 
                                        ch_e "I believe I've made myself clear."
                                    elif ApprovalCheck("Emma", 800):
                                        call Statup("Emma", "Inbt", 50, 1) 
                                        ch_e "You're persistant, but no."
                                    else:
                                        call Statup("Emma", "Love", 75, -5)
                                        call Statup("Emma", "Love", 40, -10)
                                        call Statup("Emma", "Obed", 90, 2)
                                        call EmmaFace("angry") 
                                        ch_e "Of course not."
                                "I insist.":
                                    call EmmaFace("sad") 
                                    if ApprovalCheck("Emma", 400, "I") and ApprovalCheck("Emma", 1200, "LO"):
                                        call Statup("Emma", "Obed", 40, 3)
                                        call Statup("Emma", "Obed", 90, 2)
                                        ch_e "Well then."
                                        $ Choice = "leave"  
                                    elif ApprovalCheck("Emma", 800, "O"):
                                        call Statup("Emma", "Love", 50, -10)
                                        call Statup("Emma", "Love", 200, -5)
                                        call Statup("Emma", "Obed", 90, 10)
                                        call Statup("Emma", "Obed", 200, 5)
                                        ch_e "If I must."
                                        $ Choice = "leave"  
                                    elif Cleaned:
                                        call Statup("Emma", "Love", 50, -5)
                                        call Statup("Emma", "Love", 200, -1)
                                        call EmmaFace("angry") 
                                        ch_e "That's enough of that."
                                    elif ApprovalCheck("Emma", 800):
                                        call Statup("Emma", "Love", 50, -3)
                                        call Statup("Emma", "Love", 200, -1)
                                        call EmmaFace("sad") 
                                        ch_e "Don't push me." 
                                    else:
                                        call Statup("Emma", "Love", 50, -10)
                                        call Statup("Emma", "Love", 200, -5)
                                        call EmmaFace("angry") 
                                        ch_e "Obviously not."
                                        
                                "Never mind then.":
                                    ch_e "Ok. . ."                            
                        #end "leave it"
                        
                "You should just eat it.":
                        call EmmaFace("sly") 
                        if "hungry" in E_Traits or (E_Swallow >= 5 and ApprovalCheck("Emma", 800)): 
                                #lots of swallows
                                call Statup("Emma", "Obed", 90, 1)
                                call Statup("Emma", "Inbt", 50, 3) 
                                call Statup("Emma", "Inbt", 80, 1) 
                                call Statup("Emma", "Lust", 90, 5) 
                                $ Choice = "eat"   
                                ch_e "Well, I suppose I could. . ."
                        elif E_Swallow and ApprovalCheck("Emma", 800): 
                                #few swallows
                                call Statup("Emma", "Obed", 50, 1)
                                call Statup("Emma", "Obed", 90, 1)
                                call Statup("Emma", "Inbt", 50, 2) 
                                call Statup("Emma", "Inbt", 80, 1) 
                                call Statup("Emma", "Lust", 90, 5) 
                                $ Choice = "eat"   
                                ch_e "You do have a unique flavor. . ."
                        elif ApprovalCheck("Emma", 1200): 
                                #no swallows, but likes you
                                call Statup("Emma", "Obed", 50, 1)
                                call Statup("Emma", "Obed", 90, 1)
                                call Statup("Emma", "Inbt", 50, 3) 
                                call Statup("Emma", "Inbt", 80, 1) 
                                $ Choice = "eat"   
                                ch_e "I have been a bit curious. . ."
                        elif ApprovalCheck("Emma", 400): 
                                #Likes you well enough, but won't
                                call EmmaFace("sad") 
                                ch_e "I doubt that."
                        else: 
                                #doesn't like you.
                                call Statup("Emma", "Love", 50, -5)
                                call Statup("Emma", "Love", 200, -3)
                                call EmmaFace("angry") 
                                ch_e "No."
                        #end eat it
                              
                "You should just clean it up.":
                        if ApprovalCheck("Emma", 600, "I") and not ApprovalCheck("Emma", 1500, "LO"): #rebellious
                                call EmmaFace("sly") 
                                call Statup("Emma", "Obed", 50, -3)
                                call Statup("Emma", "Inbt", 70, 10) 
                                call Statup("Emma", "Inbt", 200, 5) 
                                call Statup("Emma", "Lust", 60, 5) 
                                ch_e "Hmmm. . . don't I look good like this? . ."
                                $ Choice = "leave"   
                                menu:
                                    extend ""
                                    "Ok, fine.":
                                        call EmmaFace("smile") 
                                        call Statup("Emma", "Love", 70, 5)
                                        call Statup("Emma", "Obed", 50, 3)
                                    "No, clean it up.": 
                                        if ApprovalCheck("Emma", 600, "O"):
                                            call EmmaFace("sad") 
                                            call Statup("Emma", "Obed", 50, 10)
                                            ch_e "Oh, if I must. . ."
                                            $ Choice = "clean"  
                                        elif ApprovalCheck("Emma", 1200, "LO"):
                                            call EmmaFace("sad") 
                                            call Statup("Emma", "Love", 70, -3)
                                            call Statup("Emma", "Obed", 50, 3)
                                            ch_e "Spoilsport. . ."
                                            $ Choice = "clean"   
                                        else:
                                            call Statup("Emma", "Love", 70, -5)
                                            call Statup("Emma", "Obed", 50, -5)
                                            ch_e "I'm afraid you don't have any say in the matter."
                                                                                    
                        else: #agrees
                                call EmmaFace("bemused") 
                                $ Choice = "clean"   
                                ch_e "If I must. . ."
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
            call Partner_Cleanup_Check("Emma")
            
    if Choice == "random":
            $ Options = ["clean"]
            if E_Swallow and ApprovalCheck("Emma", 800):
                    $ Options.append("eat") 
                    if E_Swallow >=5:                            
                        $ Options.append("eat") 
                    if "hungry" in E_Traits:                
                        $ Options.append("eat") 
            if ApprovalCheck("Emma", 600, "I"):
                    if not Cnt:
                        $ Options.append("leave") 
                    if not Cnt or ApprovalCheck("Emma", 800, "I"):
                        $ Options.append("leave") 
                    if "exhibitionist" in E_Traits:
                        $ Options.append("leave") 
                                        
            $ renpy.random.shuffle(Options)
            
            $ Choice = Options[0]
            #end "random"
            
            
    if Choice == "leave":
            call Statup("Emma", "Inbt", 80, 2) 
            call Statup("Emma", "Inbt", 200, 1) 
            "She leaves the jiz right where it is and gives you a wink."
            if "hand" in E_Spunk: 
                    $ E_Spunk.remove("hand")
                    if E_Swallow:
                        "She does lick off her hand though."
                    else:
                        "She does wipe her hand off though."   
            if "mouth" in E_Spunk:                  
                    $ E_Spunk.remove("mouth")
            if Cnt:
                    # if this is final clean-up and left the jiz on   
                    $ E_RecentActions.append("painted")                  
                    $ E_DailyActions.append("painted")     
            #end "leave it"
        
    if E_Spunk and Choice != "leave":
            call Self_Cleanup("Emma")
               
    if Ch_Focus != Original:
        # if Emma wasn't the lead, swap that one back
        call Shift_Focus(Original)
    return    
    
# End Emma Clean-Up /////////////////////////////////////////////////////////////////////////////////////
