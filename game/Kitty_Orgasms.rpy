# Start You Cumming //////////////////////////////////////////////////////////////////////////////////

label PK_Cumming:
    call Shift_Focus("Kitty")
    if Trigger == "blow":
            $ Tempmod += 5
        
    if K_Addict > 75:
            $ Tempmod += 20
    elif K_Addict > 50:
            $ Tempmod += 5
    
    if K_Swallow >= 10:
            $ Tempmod += 15  
    elif K_Swallow >= 3:
            $ Tempmod += 5
        
    if (K_CreamP + K_CreamA) >= 10:
            $ Tempmod += 15 
    elif (K_CreamP + K_CreamA) >= 3:
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
    
    call KittyFace("sexy") 
    
    menu:
        "[Line]"
        "Warn her":
                $ Situation = "warn"
                jump K_Warn_Her
            
        "Ask to cum in her mouth": 
                $ Situation = "asked"
                jump K_In_Mouth                            
        "Cum in her mouth without asking" if Trigger == "blow" or Trigger == "hand" or Trigger == "titjob":
                $ Situation = "auto"
                jump K_In_Mouth
        
        "Ask to cum inside her" if Trigger == "sex":
                $ Situation = "asked"
                jump K_Creampie_P        
        "Ask to cum inside her" if Trigger == "anal":
                $ Situation = "asked"
                jump K_Creampie_A
                
        "Cum inside her" if Trigger == "sex":
                $ Situation = "auto"
                jump K_Creampie_P        
        "Cum inside her" if Trigger == "anal":
                $ Situation = "auto"
                jump K_Creampie_A
            
        "Cum on her face":
                jump K_Facial 
                
        "Cum on her tits":
                jump K_TitSpunk  
                
#MOD MARKER cum menu choices
        "Cum on her ass" if Trigger in ("sex","anal","hotdog") and renpy.showing("Kitty_Doggy"):
                jump K_SpunkBack
        "Cum on her belly" if Trigger in ("sex","anal","hotdog","foot") and renpy.showing("Kitty_SexSprite"):
                jump K_SpunkBelly
            
        "Pull back":
            if renpy.showing("Kitty_BJ_Animation"):
                    if K_Addict >= 60 and ApprovalCheck("Kitty", 1000, "I", Bonus = ((K_Addict*10)- K_Obed)) and K_Swallow:
                            $ K_Eyes = "manic"
                            $ Speed = 0
                            "You pull out of her mouth with a pop, and her eyes widen in surprise."
                            $ K_Mouth = "sucking"
                            $ K_Spunk.append("mouth")
                            $ Speed = 4
                            "She leaps at your cock and sucks it deep, draining your fluids hungrily." 
                            $ Speed = 0
                            $ K_Mouth = "lipbite"
                            "When she finishes, she licks her lips."
                            call KittyFace("bemused")
                            ch_k "Sorry, [K_Petname], I just couldn't let that go to waste."
                            call Statup("Kitty", "Obed", 200, -5)
                            call Statup("Kitty", "Inbt", 200, 10)
                            jump K_Swallowed                            
                    call Kitty_BJ_Reset                
            elif renpy.showing("Kitty_HJ_Animation"):
                    call Kitty_HJ_Reset                
            elif renpy.showing("Kitty_SexSprite"):
                    call Kitty_Sex_Reset      
            # End reset state
            
            if ApprovalCheck("Kitty", 500, "I", Bonus = ((K_Addict*10)- K_Obed)) and K_Addict > 50 and K_Swallow: #If addict + Inbt is > obedience + 50. . .
                    $ K_Eyes = "manic"
                    $ K_Mouth = "kiss"
                    $ Speed = 0
                    "Her eyes widen in panic."
                    ch_k "Are you sure you won't reconsider, [K_Petname]?" 
                    $ K_Blush = 2
                    menu:
                        extend ""
                        "Ok, if you'll swallow it.":
                                        if not renpy.showing("Kitty_BJ_Animation"):
                                            call Kitty_BJ_Launch("cum")
                                        call KittyFace("sucking") 
                                        $ Speed = 5 
                                        $ K_Spunk.append("mouth")
                                        "She nods and puts the tip into her mouth. As you release she gulps it down hungrily."
                                        call KittyFace("sexy")     
                                        ". . ."
                                        $ Speed = 0
                                        call KittyFace("sad")                       
                                        $ K_Mouth = "lipbite"
                                        ch_k "You know I like my milk."   
                                        call Statup("Kitty", "Obed", 50, 2)
                                        call Statup("Kitty", "Obed", 70, 1)
                                        call Statup("Kitty", "Inbt", 30, 2)
                                        call Statup("Kitty", "Inbt", 50, 3)
                                        jump K_Swallowed                                
                        "No, we're done for now.": #If addict is > obedience + 50. . .
                                if ApprovalCheck("Kitty", 250, "I", Bonus = ((K_Addict*10)- K_Obed)) or K_Addict > 75:                            
                                        call Statup("Kitty", "Obed", 50, -1)
                                        call Statup("Kitty", "Obed", 70, -2)
                                        call Statup("Kitty", "Inbt", 30, 2)
                                        call Statup("Kitty", "Inbt", 70, 3)
                                        if not renpy.showing("Kitty_BJ_Animation"):
                                            call Kitty_BJ_Launch("cum")
                                        $ Speed = 5
                                        "She dives down on you and you can't resist filling her throat."
                                        $ Speed = 0
                                        ch_k "It's. . . compelling."
                                        jump K_Swallowed                                
                                else:                         
                                        call Statup("Kitty", "Obed", 30, 3)
                                        call Statup("Kitty", "Obed", 70, 5)
                                        call KittyFace("sad")
                                        $ K_Brows = "confused"
                                        ch_k "Whatever."
                                        $ Line = 0
                                        $ P_Focus -= 5
                                        return      
                    #manic, wanted to swallow
                    
            call KittyFace("sexy", 1)
            call Statup("Kitty", "Obed", 50, 2)
            "You pull pull back away from her. She looks up at you and licks her lips." 
            ch_k "Oh? So what did you want to do?"
            $ Line = 0
            $ P_Focus = 95
            return
            #end "pull back"
#End Main orgasm menu

#Warn her start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label K_Warn_Her:                                                                                                                       #Warn her start
        "You let her know that you're going to come."
        call Statup("Kitty", "Love", 90, 3)
        if K_Obed >= 500:
                call Statup("Kitty", "Obed", 80, 5)
        if "hungry" in K_Traits and D20 >= 5:
                if renpy.showing("Kitty_SexSprite"):
                    call Kitty_HJ_Launch("cum")   
                    "She grins and pulls out with a pop, and begins to stroke you off."
                $ Speed = 2
                call KittyFace("sucking")       
                ". . ."
                $ Speed = 0
                $ K_Spunk.append("mouth")
                if not renpy.showing("Kitty_BJ_Animation"):
                    "She smiles and then puts your tip in her mouth. When you finish filling her mouth, she quickly gulps it down and wipes her lips."
                else:                    
                    "She makes a little humming sound, but keeps sucking. When you finish filling her mouth, she quickly gulps it down and wipes her lips."        
                call KittyFace("sexy")
                $ K_Mouth = "smile"
                ch_k "Hmmm, thanks for the warning."         
                jump K_Swallowed
        #End Hungy take-over
            
        if Trigger == "sex":
            if K_CreamP and (K_CreamP + D20) >= 10: 
                # She's Creampied a few times
                call KittyFace("sexy")
                $ P_Cock = "in"
                $ K_Spunk.append("in")
                $ P_Spunk = "in"
                $ Speed = 0
                "She smiles and speeds up her actions, causing you to erupt inside her."   
                if K_Lust >= 85: 
                    call K_Cumming  
                jump K_Creampied
                    
        elif Trigger == "anal":
            if K_CreamA >= 5 and (K_CreamA + D20) >= 10:
                # She's Anal Creampied at least once
                call KittyFace("sexy")
                $ P_Cock = "anal"
                $ K_Spunk.append("anal")
                $ P_Spunk = "anal"
                $ Speed = 0
                "She gets a michevious look and speeds up, you burst inside her."    
                if K_Lust >= 85: 
                    call K_Cumming          
                jump K_Creampied
            
        if (K_Swallow + D20) >= 10:        
            if Trigger != "anal" or K_Swallow >= 10 or renpy.showing("Kitty_BJ_Animation"): 
                    # If she's swallowed and decides to swallow              
                    if renpy.showing("Kitty_BJ_Animation"):            
                            call KittyFace("sucking")
                            if K_Blow >= 10 or Speed >= 4:
                                    $ Speed = 6 #deep animation
                            else:
                                    $ Speed = 5 #shallow animation
                            $ K_Spunk.append("mouth")
                            "She makes a little humming sound, but keeps sucking."
                    elif renpy.showing("Kitty_TJ_Animation"):  
                            if K_Blow >= 5 or Speed >= 3:          
                                    call KittyFace("kiss")
                                    $ Speed = 5 #shallow animation
                                    $ K_Spunk.append("mouth")
                                    "She makes a little humming sound, but keeps sucking."
                            else: 
                                    jump K_Facial
                    else:
                            call Kitty_BJ_Launch("cum")
                            $ Speed = 5
                            call KittyFace("sucking")
                            $ K_Spunk.append("mouth")
                            "She smiles and then puts your tip in her mouth."
                    if K_Swallow <= 3:
                            "When you finish filling her mouth, she gags a little, but manages to swallow it."
                    else:
                            "When you finish filling her mouth, she quickly gulps it down and wipes her lips."                
                    $ Speed = 0
                    call KittyFace("sexy")
                    $ K_Mouth = "smile"
                    if K_Swallow < 5:
                            ch_k "Thats. . . thick."
                    else:
                            ch_k "Hmmm, thanks for the warning."  
                    jump K_Swallowed
        #end if she's swallowed
            
            else:
                #She's swallowed before, but not a lot  
                if renpy.showing("Kitty_SexSprite"):
                    call Kitty_HJ_Launch("cum") 
                    "She grins and pulls out with a pop, and begins to stroke you off."
                $ Speed = 2               
                #If she's handying
                jump K_Handy_Finish    
        #end handy finish        
            
        if ApprovalCheck("Kitty", 1000):                    
                #warned but likes you and experienced
                if K_SEXP > 20 and renpy.showing("Kitty_SexSprite"):
                        "She gently pushes you back off of her."
                        jump K_SpunkBelly
                elif K_SEXP > 20:
                        jump K_Facial 
                if renpy.showing("Kitty_HJ_Animation") and K_Hand:
                        jump K_Handy_Finish
                elif renpy.showing("Kitty_BJ_Animation") and K_Blow:
                        jump K_Handy_Finish
                elif renpy.showing("Kitty_TJ_Animation") and K_Tit:
                        jump K_Facial
                elif renpy.showing("Kitty_SexSprite") and K_Sex and Trigger == "sex":
                        "She gently pushes you back off of her."
                        jump K_SpunkBelly
                elif renpy.showing("Kitty_SexSprite") and K_Anal and Trigger == "anal":
                        "She gently pushes you back off of her."
                        jump K_SpunkBelly
        
        
        # Else. . . not experienced or she's not a huge fan, 
        if renpy.showing("Kitty_BJ_Animation"):
            if not K_Blow:
                $ Situation = "auto"
                jump K_In_Mouth
            else:
                jump K_Handy_Finish   
        elif Trigger == "sex" or Trigger == "anal":
                call Kitty_Sex_Reset
                "She pulls off of you and grabs your cock in her hand."
                jump K_Handy_Finish
        elif renpy.showing("Kitty_SexSprite"):#hotdogging
                "She smiles and starts rubbing against you a bit faster."
                jump K_SpunkBelly
        jump K_Facial
    #End "Warn her" / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    
                      
                      
#Cum in mouth start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label K_In_Mouth:      
    if Trigger == "anal":
            $ Tempmod -= 15
    if "hungry" not in K_Traits and K_Addict <= 50 and "full" in K_RecentActions:
            $ Tempmod -= 15                  
            
    $ P_Cock = "out"    
    if Situation == "auto":
                $ Situation = 0                
                if renpy.showing("Kitty_TJ_Animation"):     
                        call KittyFace("kiss")                        
                elif not renpy.showing("Kitty_BJ_Animation"):
                        call Kitty_BJ_Launch("cum")
                $ Speed = 6 if Speed == 4 else 5 #6 if deep throating, 5 if not
                "You grab her head and cum in her mouth"  
                $ K_Eyes = "closed"                 
                $ P_Spunk = 1    
                if renpy.showing("Kitty_TJ_Animation"): 
                        show Kitty_TJ_Animation
                        with vpunch   
                else:
                        show Kitty_BJ_Animation
                        with vpunch   
                if "full" in K_RecentActions:
                        #if she's had enough
                        call KittyFace("bemused")
                        $ K_Spunk.append("mouth")
                        $ Speed = 0
                        "She gags a little, but manages to swallow it."
                        $ K_Spunk.remove("mouth")
                        ch_k "I'm[K_like]totally stuffed here. . ."
                        ch_k ". . . is there anywhere else we could put this?"
                elif K_Swallow >= 5 or "hungry" in K_Traits:
                        #if she likes to swallow
                        call KittyFace("sexy")
                        $ K_Mouth = "smile"
                        $ K_Spunk.append("mouth")
                        "She quickly gulps it down and wipes her mouth."
                        $ K_Spunk.remove("mouth")
                        $ Speed = 0
                        ch_k "Mmmm, Kitty likes her milk."
                        call KittyFace
                elif K_Swallow:
                        call KittyFace("bemused")
                        $ K_Spunk.append("mouth")
                        $ Speed = 0
                        "She gags a little, but manages to swallow it."
                        $ K_Spunk.remove("mouth")
                        ch_k "That[K_like]takes some getting used to."
                        call KittyFace
                elif not K_Swallow and K_Addict >= 50 and K_Inbt < 500 and K_Blow < 10:
                        call KittyFace("bemused", 1)
                        $ K_Spunk.append("mouth")
                        ". . ."            
                        $ K_Spunk.remove("mouth")
                        $ K_Spunk.append("hand")
                        $ Speed = 0
                        "She gags and spits it into her palm. Then she licks her lips, looks down at her dripping hand, blushes, and quickly wipes it off."
                        $ K_Spunk.remove("hand")
                        ch_k "I'm not into that taste."
                        $ K_Addictionrate += 1
                        if "addictive" in P_Traits:
                            $ K_Addictionrate += 1
                        call KittyFace
                        jump K_Orgasm_After
                elif not K_Swallow and K_Addict >= 50:
                        call KittyFace("sexy")
                        $ K_Mouth = "tongue"
                        $ K_Spunk.append("mouth")
                        ". . ."
                        $ K_Spunk.remove("mouth")
                        $ K_Spunk.append("hand")
                        $ Speed = 0
                        "She gags and spits it into her palm. Then she licks her lips, looks down, and drinks up what's in her palm."
                        $ K_Spunk.remove("hand")
                        ch_k "You coulda warned me." 
                        call KittyFace
                        call Statup("Kitty", "Inbt", 30, 2)
                        call Statup("Kitty", "Inbt", 50, 2)
                elif not K_Swallow:
                        if ApprovalCheck("Kitty", 700, "LO") and ApprovalCheck("Kitty", 300, "I"):
                            call KittyFace("angry")
                            $ K_Spunk.append("mouth")
                        else:
                            call KittyFace("bemused")
                            $ K_Mouth = "tongue"
                            $ K_Spunk.append("mouth")
                        ". . ."
                        $ K_Spunk.append("hand")
                        $ Speed = 0
                        "She gags and spits it into her palm."   
                        menu:
                            ch_k "Hey[K_like]what gives?"
                            "Sorry about that.":
                                    call Statup("Kitty", "Love", 80, 1)
                                    $ K_Addictionrate += 1
                                    if "addictive" in P_Traits:
                                        $ K_Addictionrate += 1
                                    call KittyFace("smile", 1)
                                    ch_k "Well, just[K_like]now I know, I guess?"
                                    jump K_Orgasm_After
                                
                            "Why don't you try swallowing it?":
                                    if ApprovalCheck("Kitty", 1300):
                                        "She tentatively licks her hand, and then gulps it down."
                                        $ K_Spunk.remove("hand")
                                        call KittyFace("sexy", 1)
                                        $ K_Spunk.append("mouth")
                                        ch_k "Hmm, creamy. . ."
                                        call Statup("Kitty", "Obed", 50, 12)
                                        $ K_Spunk.remove("mouth")
                                    elif ApprovalCheck("Kitty", 1000, "OI", Bonus = (K_Addict*10)):
                                        call KittyFace("bemused", 1)
                                        $ K_Brows = "normal" 
                                        $ K_Mouth = "sad"
                                        $ K_Spunk.remove("hand")
                                        $ K_Spunk.append("mouth")
                                        "She scowls a bit, but licks her hand clean as she does so, and swallows it down."
                                        $ K_Spunk.remove("mouth")
                                        ch_k "It's. . . not terrible."
                                        call Statup("Kitty", "Obed", 50, 15)
                                    else:
                                        $ K_Spunk.remove("hand")
                                        "She scowls at you and wipes her hand off. Then she licks her lips."
                                        jump K_Orgasm_After
                                    
                            "Swallow it, now.":
                                    call Statup("Kitty", "Love", 30, -1, 1)
                                    call Statup("Kitty", "Love", 50, -1, 1)                    
                                    call Statup("Kitty", "Love", 80, -1, 1)
                                    if ApprovalCheck("Kitty", 1200, "OI") or K_Addict >= 50:                            
                                        call KittyFace("sad", 1)
                                        $ K_Spunk.append("mouth")
                                        $ K_Spunk.remove("hand")
                                        "She scowls a bit, but licks her hand clean as she does so, and swallows it down."
                                        $ K_Spunk.remove("mouth")
                                        ch_k "That's. . . not terrible."
                                        call Statup("Kitty", "Obed", 50, 15)
                                    else:         
                                        $ K_Spunk.remove("hand")               
                                        "She scowls at you and wipes her hand off. Then she licks her lips."                        
                                        jump K_Orgasm_After
                else:                
                            jump K_Orgasm_After
                                
                jump K_Swallowed
                #end if not asked/auto / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
           
    $ Situation = 0
    "You ask if you can cum in her mouth."
    if renpy.showing("Kitty_SexSprite"):
            call Kitty_HJ_Launch("cum")
        
    if "full" in K_RecentActions:
            pass
        
    elif K_Swallow >= 5 or "hungry" in K_Traits:  
            # If she's swallowed 5 times, 
            call KittyFace("sucking")
            if renpy.showing("Kitty_TJ_Animation"):    
                call KittyFace("kiss")
                $ Speed = 5
                "She nods and bends down to put the tip between her lips."
            elif not renpy.showing("Kitty_BJ_Animation"):
                call Kitty_BJ_Launch("cum")            
                $ Speed = 2
                "She nods and bends down to put the tip between her lips."
            else:            
                $ Speed = 2
                "She nods and hums a \"yes\" sound."      
            $ Speed = 6 if Speed == 4 else 5 #6 if deep throating, 5 if not  
            ". . ."    
            $ P_Spunk = 1
            $ K_Spunk.append("mouth")
            "After you cum, she quickly gulps it down and wipes her mouth."
            call KittyFace("sexy")            
            $ Speed = 0
            ch_k "Mmm, creamy."
            $ K_Spunk.remove("mouth")
            jump K_Swallowed
        
    elif K_Addict >= 80 and K_Swallow: 
            #addicted
            $ K_Brows = "confused"
            $ K_Eyes = "manic"
            if renpy.showing("Kitty_TJ_Animation"):    
                call KittyFace("kiss")
                $ Speed = 5
                "She looks a bit quizzical, but gently puts the tip to her lips, just as you blow."
            elif not renpy.showing("Kitty_BJ_Animation"):
                call Kitty_BJ_Launch("cum")            
                $ Speed = 2    
                "She looks a bit quizzical, but gently puts the tip to her lips, just as you blow."
            else:            
                $ Speed = 2
                "She nods and hums a \"yes\" sound."
            $ Speed = 6 if Speed == 4 else 5 #6 if deep throating, 5 if not
            $ K_Mouth = "sucking"
            ". . ."
            $ P_Spunk = 1
            $ K_Spunk.append("mouth")
            $ Speed = 0
            "She gags a little, but quickly swallows it."
            call KittyFace("sexy")
            $ K_Mouth = "smile"
            ch_k "You coulda warned me first."
            $ K_Spunk.remove("mouth")
            call Statup("Kitty", "Inbt", 200, 5)
            jump K_Swallowed
            
    elif K_Swallow:                
            if ApprovalCheck("Kitty", 900):
                $ K_Brows = "confused"
                if renpy.showing("Kitty_TJ_Animation"):    
                    call KittyFace("kiss")
                    $ Speed = 5
                    "She looks a bit confused, but gently puts the tip to her lips."
                    "Just as you blow. She gags a little, but quickly swallows it."
                elif not renpy.showing("Kitty_BJ_Animation"):
                    call Kitty_BJ_Launch("cum")            
                    $ Speed = 2    
                    "She looks a bit confused, but gently puts the tip to her lips."
                    "Just as you blow. She gags a little, but quickly swallows it."
                else:            
                    $ Speed = 2     
                    ch_k "[[mumbled] Huh?"
                $ Speed = 6 if Speed == 4 else 5 #6 if deep throating, 5 if not
                $ K_Mouth = "sucking"
                $ K_Spunk.append("mouth")
                $ K_Brows = "normal"
                $ K_Eyes = "sexy"
                ". . ."
                $ P_Spunk = 1
                $ K_Spunk.append("mouth")
                "She gags a little, but quickly swallows it."
                $ Speed = 0
                call KittyFace("sexy")
                ch_k "Yech, that's still kinda nasty."
                $ K_Spunk.remove("mouth")
                jump K_Swallowed
     
    #If she hasn't swallowed or doesn't automatically want to. . .  
    
    if  ApprovalCheck("Kitty", 500, "LI") or ApprovalCheck("Kitty", 400, "OI"): 
        call KittyFace("bemused")
        $ K_Eyes = "sexy"
    else:
        call KittyFace("angry")
        
    $ Speed = 0    
    
    if "full" in K_RecentActions:
        ch_k "I've kinda had enough for now? . ." 
    else:
        ch_k "That doesn't sound too appetizing. . ."
    
    menu:
        extend ""
        "Sorry about that.":
                call Statup("Kitty", "Love", 80, 3)
                $ K_Addictionrate += 1
                if "addictive" in P_Traits:
                    $ K_Addictionrate += 1
                call KittyFace("smile", 1)
                ch_k "Can't hurt to ask, right?"
                if ApprovalCheck("Kitty", 1200, TabM=1) and "full" not in K_RecentActions:
                    call Statup("Kitty", "Inbt", 30, 3)
                    call Statup("Kitty", "Inbt", 70, 2)  
                    call KittyFace("sexy", 1)
                    ch_k "It's[K_like]worth a shot."
                else:
                    jump K_Handy_Finish                
            
        "Give it a try, you might like it." if "full" not in K_RecentActions:
                if ApprovalCheck("Kitty", 1300, TabM=1):  
                    call Statup("Kitty", "Obed", 50, 5)
                    call Statup("Kitty", "Obed", 70, 3)
                    $ K_Brows = "confused"  
                    $ K_Eyes = "sexy"
                    ch_k "I guess. . ."
                else:     
                    $ K_Addictionrate += 1
                    if "addictive" in P_Traits:
                        $ K_Addictionrate += 1
                    $ K_Blush = 1
                    ch_k "You wish, [K_Petname]."
                    jump K_Handy_Finish
                            
        "Seriously, put it in your mouth.":
                if ApprovalCheck("Kitty", 1500, "LI", TabM=1) or ApprovalCheck("Kitty", 1200, "OI", TabM=1):
                        call KittyFace("sucking", 1)
                elif ApprovalCheck("Kitty", 1000, "OI", Bonus = (K_Addict*10)): #Mild addiction included                
                        call KittyFace("angry", 1)
                else: 
                        #You insisted, she refused. 
                        call KittyFace("angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        call Kitty_HJ_Launch("cum")
                        call Kitty_HJ_Reset                
                        call Statup("Kitty", "Love", 50, -3, 1)
                        call Statup("Kitty", "Love", 80, -4, 1)
                        ch_k "You can handle it yourself then."
                        call Statup("Kitty", "Obed", 30, -1, 1)
                        call Statup("Kitty", "Obed", 50, -1, 1)  
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")   
                        $ Line = 0
                        return  
                call Statup("Kitty", "Obed", 50, 10)
                call Statup("Kitty", "Obed", 70, 5)
        
    if renpy.showing("Kitty_TJ_Animation"):    
        call KittyFace("kiss")
        $ Speed = 5
    elif not renpy.showing("Kitty_BJ_Animation"):
        call Kitty_BJ_Launch("cum")     
    $ Speed = 6 if Speed == 4 else 5 #6 if deep throating, 5 if not
    if ApprovalCheck("Kitty", 1200):            
            "She gently puts the tip to her lips, just as you blow."
    else:
            "She tentatively places the tip in her mouth, and you blast inside it."                   
            call KittyFace("sexy")
            call Statup("Kitty", "Love", 50, -3, 1)
            call Statup("Kitty", "Love", 80, -4, 1)  
            
    $ P_Spunk = 1
    $ K_Spunk.append("mouth")
    $ K_Mouth = "sucking"
    ". . ."   
    "She gags a little, but quickly swallows it." 
    $ Speed = 0            
    call KittyFace("sexy") 
    
    if ApprovalCheck("Kitty", 1000) and K_Swallow >= 3:
            ch_k "I'm starting to get used to that."    
    elif ApprovalCheck("Kitty", 800):                          
            ch_k "I guess that isn't too bad."
    else:
            call KittyFace("sad")
            ch_k "Kinda nasty, [K_Petname]."    
    call Statup("Kitty", "Inbt", 30, 3)
    call Statup("Kitty", "Inbt", 50, 2)            
    $ K_Blow += 1
    jump K_Swallowed     
    #end Kitty in mouth  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Creampie  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label K_Creampie_P:
        if Trigger == "sex" and Situation == "auto":
                $ P_Cock = "in"
                $ K_Spunk.append("in")
                $ P_Spunk = "in"
                $ Speed = 0
                if ApprovalCheck("Kitty", 1300) or K_CreamP:               
                    call KittyFace("surprised")
                    "You come in her pussy. Her eyes widen in surprise, but she takes it in stride."  
                    call KittyFace("sexy")
                    if K_Lust >= 85: 
                        call K_Cumming
                else:
                    if K_Lust >= 85: 
                        "You come in her pussy. Her eyes widen in surprise and she shakes a bit."
                        call K_Cumming                
                    else:
                        "You come in her pussy. Her eyes widen in surprise and she pulls out."
                    $ P_Cock = "out"
                    call KittyFace("angry")
                    ch_k "You coulda[K_like]warned me or something!"
                    call KittyFace("bemused")
                    ch_k "It was pretty warm though. . ."                     
                jump K_Creampied
        
        #else (You ask her if it's ok):
        if ApprovalCheck("Kitty", 1200) or K_CreamP:        
                call KittyFace("sexy")
                if K_CreamP >= 3:
                    "She smiles and speeds up her actions, causing you to erupt inside her."  
                elif K_CreamP:
                    "She gets a michevious look and speeds up, you burst inside her." 
                else:
                    "As you continue to pound her, she nods her head."
                $ P_Cock = "in"
                $ K_Spunk.append("in")
                $ P_Spunk = "in"
                $ Speed = 0
                if K_Lust >= 85: 
                    call K_Cumming  
                call Statup("Kitty", "Love", 90, 1) 
                ch_k "Hmm, cozy. . ."
                jump K_Creampied
        else:
                call KittyFace("sexy")
                call Statup("Kitty", "Love", 80, 2) 
                call Statup("Kitty", "Love", 90, 2) 
                ch_k "Thanks for the warning, but maybe not this time?"
        jump K_SpunkBelly

#Start Anal Creampie  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label K_Creampie_A:                             
        # These need conditionals added    
        if Trigger == "anal" and Situation == "auto":
                $ P_Cock = "anal"
                $ K_Spunk.append("anal")
                $ P_Spunk = "anal"
                $ Speed = 0
                if ApprovalCheck("Kitty", 1200) or K_CreamP:              
                    call KittyFace("surprised", 1)
                    "You come in her ass. Her eyes widen in surprise, but she takes it in stride."  
                    call KittyFace("sexy")
                    if K_Lust >= 85: 
                        call K_Cumming
                else:
                    if K_Lust >= 85: 
                        "You come in her ass. Her eyes widen in surprise and she shakes a bit."
                        call K_Cumming                
                    else:
                        "You come in her ass. Her eyes widen in surprise and she pulls out."
                    $ P_Cock = "out"
                    call KittyFace("angry")
                    ch_k "Maybe a little warning next time?"
                    call KittyFace("bemused")
                    ch_k "that was pretty warm though. . ."
                jump K_Creampied
            
        #else (You ask her if it's ok):
        if ApprovalCheck("Kitty", 1200) or K_CreamP:        
                call KittyFace("sexy")
                if K_CreamP >= 3:
                    "She smiles and speeds up her actions, causing you to erupt inside her."  
                elif K_CreamP:
                    "She gets a michevious look and speeds up, you burst inside her." 
                else:
                    "As you continue to pound her, she nods her head."
                $ P_Cock = "anal"
                $ K_Spunk.append("anal")
                $ P_Spunk = "anal"
                $ Speed = 0
                if K_Lust >= 85: 
                    call K_Cumming  
                call Statup("Kitty", "Love", 90, 1) 
                ch_k "Wow, I feel so full. . ."
                jump K_Creampied
        else:
                call KittyFace("sexy")     
                call Statup("Kitty", "Love", 80, 2) 
                ch_k "Thanks for the warning, but maybe not this time?"
        jump K_SpunkBelly
            
#Start Facial  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    
label K_Facial: 
        if renpy.showing("Kitty_BJ_Animation"):       
                if K_Addict >= 60 and ApprovalCheck("Kitty", 1000, "I", Bonus = ((K_Addict*10)- K_Obed)) and K_Swallow:
                        $ K_Eyes = "manic"
                        $ K_Blush = 1
                        $ Speed = 0
                        "You pull out of her mouth with a pop, and her eyes widen in surprise." 
                        $ Speed = 4
                        $ K_Spunk.append("mouth")
                        "She leaps at your cock and sucks it deep, draining your fluids hungrily."
                        $ K_Mouth = "lipbite"
                        $ Speed = 0
                        "When she finishes, she licks her lips."
                        call KittyFace("bemused")
                        $ K_Spunk.remove("mouth")
                        ch_k "Sorry, that's just[K_like]sooooo good."
                        call Statup("Kitty", "Obed", 80, -5)
                        call Statup("Kitty", "Inbt", 200, 10)
                        jump K_Swallowed
                call Kitty_HJ_Launch("cum")
                $ Speed = 2
                $ K_Spunk.append("facial")
                "You pull out of her mouth with a pop, and she strokes you off. You spray all over her face."
                $ Speed = 0
        
        elif renpy.showing("Kitty_TJ_Animation"):   
                $ K_Spunk.append("facial")
                if not K_Tit:                       
                    "She glances up but continues to rub her breasts up and down on your cock."
                    "When you come, you spray all over her face."
                else:
                    "As you're about to finish, you aim squarely at her face, and spray all over it."  
                $ Speed = 0
                
        elif renpy.showing("Kitty_HJ_Animation"):       
                $ K_Spunk.append("facial")
                if not K_Hand:                       
                    "She looks a bit confused but continues to stroke while staring at it like a live snake. When you finish, you spray all over her face."
                else:
                    "As you're about to finish, you aim squarely at her face, and spray all over it."  
                $ Speed = 0
        else:        
                call Kitty_HJ_Launch("cum")
                $ Speed = 2
                $ K_Spunk.append("facial")
                "As you're about to finish, you pull out, aim squarely at her face, and spray all over it."
                $ Speed = 0
        
        if Situation == "warn":
            ch_k "Whew, thanks for the head's up."  
        else:
            ch_k "Huh, nice warning there, [K_Petname]." 
               
        $ P_Cock = "out"            
        jump K_Orgasm_After


#Start titjob spunk  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    
label K_TitSpunk: 
        if renpy.showing("Kitty_BJ_Animation"):       
                if K_Addict >= 60 and ApprovalCheck("Kitty", 1000, "I", Bonus = ((K_Addict*10)- K_Obed)) and K_Swallow:
                        $ K_Eyes = "manic"
                        $ K_Blush = 1
                        $ Speed = 0
                        "You pull out of her mouth with a pop, and her eyes widen in surprise." 
                        $ Speed = 4
                        $ K_Spunk.append("mouth")
                        "She leaps at your cock and sucks it deep, draining your fluids hungrily."
                        $ K_Mouth = "lipbite"
                        $ Speed = 0
                        "When she finishes, she draws her hand across her lips."
                        call KittyFace("bemused")
                        $ K_Spunk.remove("mouth")
                        ch_k "I'm sorry, [K_Petname], too tasty."
                        call Statup("Kitty", "Obed", 80, -5)
                        call Statup("Kitty", "Inbt", 200, 10)
                        jump K_Swallowed
                   
        if not renpy.showing("Kitty_TJ_Animation") and not renpy.showing("Kitty_HJ_Animation") and not renpy.showing("Kitty_BJ_Animation"):      
                call Kitty_HJ_Launch("cum")
        $ K_Spunk.append("tits")
        $ Speed = 0
        "As you're about to finish, you speed up and spray all over her chest."

        if Situation == "warn":
            ch_k "Whew, thanks for the head's up."  
        else:
            ch_k "Huh, nice warning there, [K_Petname]." 
                    
        jump K_Orgasm_After
        
# Start Spunk belly  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
###ANON MOD CODE BLOCK START #####
#placeholderline1 
label K_SpunkBack: 
        if Trigger != "foot":
            call Kitty_Doggy_Launch("hotdog")
        $ Speed = 0
        if K_Addict >= 60 and ApprovalCheck("Kitty", 1000, "I", Bonus = ((K_Addict*10)- K_Obed))  and K_Swallow:
                $ K_Eyes = "manic"
                $ K_Blush = 1
                call Kitty_BJ_Launch("cum")
                if Trigger == "sex":
                    "You pull out of her pussy with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
                elif Trigger == "anal":                
                    "You pull out of her ass with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
                $ K_Mouth = "lipbite"
                $ K_Spunk.append("mouth")
                "When she finishes, she licks her lips."
                call KittyFace("bemused")
                $ K_Spunk.remove("mouth")
                ch_r "Sorry, [K_Petname], I just couldn't let that go to waste."
                call Statup("Kitty", "Obed", 80, -5)
                call Statup("Kitty", "Inbt", 200, 10)
                jump K_Swallowed
        if Trigger != "foot":
            $ P_Cock = "out"
        $ K_Spunk.append("back")
        if Trigger == "sex":
                "You pull out of her pussy with a pop and spray all over her backside."
        elif Trigger == "anal":
                "You pull out of her ass with a pop and spray all over her backside."
        else:
                "You pick up the pace and with a grunt you spray all over her backside."
            
                      
        if K_Addict >= 60 and ApprovalCheck("Kitty", 800, "I", Bonus = ((K_Addict*10)- K_Obed)) and K_Swallow: 
                #if she's manic and has swallowed
                $ K_Eyes = "manic"
                $ K_Blush = 1        
                "Kitty's eyes widen with desire, and she quickly wipes a bit off with her hand, then licks her fingers clean."
                call KittyFace("manic", 1)
                $ K_Spunk.append("mouth")
                $ K_Mouth = "smile"
                ch_r "Well, [K_Petname], I just couldn't let that go to waste."
                $ K_Spunk.remove("mouth")
                call Statup("Kitty", "Inbt", 50, 3)
                jump K_Swallowed
              
            
        #else . . .
        call KittyFace("sexy", 1)
        ch_r "Thanks for the courtesy, [K_Petname]. Such a mess though. . ." 
#        call Kitty_Doggy_Reset
        jump K_Orgasm_After
###ANON MOD CODE BLOCK STOP ######
###ANON MOD CODE BLOCK STOP ######
label K_SpunkBelly: 
        if P_Cock != "foot":
                call Kitty_Sex_Launch("hotdog")
        $ Speed = 0
        if K_Addict >= 60 and ApprovalCheck("Kitty", 1000, "I", Bonus = ((K_Addict*10)- K_Obed))  and K_Swallow:
                $ K_Eyes = "manic"
                $ K_Blush = 1
                call Kitty_BJ_Launch("cum")
                if Trigger == "sex":
                    "You pull out of her pussy with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
                elif Trigger == "anal":                
                    "You pull out of her ass with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
                $ K_Mouth = "lipbite"
                $ K_Spunk.append("mouth")
                "When she finishes, she licks her lips."
                call KittyFace("bemused")
                $ K_Spunk.remove("mouth")
                ch_k "Sorry, that's just[K_like]sooooo good."
                call Statup("Kitty", "Obed", 80, -5)
                call Statup("Kitty", "Inbt", 200, 10)
                jump K_Swallowed
        if P_Cock != "foot":
            $ P_Cock = "out"
        $ P_Spunk = "out"
        $ K_Spunk.append("belly")
        if Trigger == "sex":
                "You pull out of her pussy with a pop and spray all over her belly."
        elif Trigger == "anal":
                "You pull out of her ass with a pop and spray all over her belly."
        else:
                "You pick up the pace and with a grunt you spray all over her belly."
            
                      
        if K_Addict >= 60 and ApprovalCheck("Kitty", 800, "I", Bonus = ((K_Addict*10)- K_Obed)) and K_Swallow: 
                #if she's manic and has swallowed
                $ K_Eyes = "manic"
                $ K_Blush = 1        
                "Kitty's eyes widen with desire, and she quickly wipes a bit off with her hand, then licks her fingers clean."
                call KittyFace("manic", 1)
                $ K_Spunk.append("mouth")
                $ K_Mouth = "smile"
                ch_k "Sorry, that's just[K_like]sooooo good."
                $ K_Spunk.remove("mouth")
                call Statup("Kitty", "Inbt", 50, 3)
                jump K_Swallowed
              
            
        #else . . .
        call KittyFace("sexy", 1)
        ch_k "Mmmm, all over the place. . ."
#        call Kitty_Sex_Reset
        jump K_Orgasm_After
    
   
#Start Handy finish  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label K_Handy_Finish:
        if renpy.showing("Kitty_SexSprite"):
                call Kitty_HJ_Launch("cum")  
                if Trigger == "hotdog":
                    "She bends down and begins to stroke you off."
                else:
                    "She grins and pulls out with a pop, and begins to stroke you off."
                $ Speed = 2   
        elif renpy.showing("Kitty_BJ_Animation"):         
                call Kitty_HJ_Launch("cum")  
                $ Speed = 2   
                "She slides her lips off your cock, and begins to stroke you off."        
        else:    
                call Kitty_HJ_Launch("cum")
                $ Speed = 2 
        $ K_Spunk.append("hand") 
        "She grins and speeds up her efforts, placing her left hand over your tip. You burst all over her hands." 
        $ Speed = 0
        
        if K_Addict > 80 or "hungry" in K_Traits:
                $ K_Eyes = "manic"
                $ K_Spunk.remove("hand")
                $ K_Spunk.append("mouth")
                $ K_Mouth = "smile"
                "She licks her hands off with a satisfied grin."
                $ K_Spunk.remove("mouth")
                ch_k "Hmmm. . ."
        else:
                call KittyFace("bemused")
                $ K_Spunk.remove("hand")
                "She wipes her hands off, but takes a quick sniff when she's done and smiles."
                ch_k "Hmm, sticky."  
                jump K_Orgasm_After


#Start Swallowed  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label K_Swallowed: 
        $ K_Swallow += 1
        call Statup("Kitty", "Inbt", 50, 3)
        $ K_Addict -= 20    
        if "mouth" in K_Spunk:
                $ K_Spunk.remove("mouth")
        if "full" not in K_RecentActions and Action_Check("Kitty", "recent", "swallowed") >= 5: 
                $ K_RecentActions.append("full")    
                call KittyFace("surprised", 1)
                ch_k "-buurp-"
                call KittyFace("sexy", 1)
                ch_k "I. . . might have to cut back a bit."
        $ K_RecentActions.append("swallowed")                      
        $ K_DailyActions.append("swallowed") 
        $ K_Addictionrate += 2
        if "addictive" in P_Traits:
                $ K_Addictionrate += 2
        if Trigger == "anal":    
                call Statup("Kitty", "Obed", 50, 3)
                call Statup("Kitty", "Obed", 200, 3)
        if K_Swallow == 1:
                $K_SEXP += 12
                call Statup("Kitty", "Inbt", 70, 5)
        jump K_Orgasm_After

#Start Creampied  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label K_Creampied:
        if Trigger == "sex":
                $ K_CreamP += 1
                call Statup("Kitty", "Lust", 200, 10)
                $ K_RecentActions.append("creampie sex")                      
                $ K_DailyActions.append("creampie sex") 
        elif Trigger == "anal":
                $ K_CreamA += 1
                call Statup("Kitty", "Lust", 200, 5)
                $ K_RecentActions.append("creampie anal")                      
                $ K_DailyActions.append("creampie anal") 
        call Statup("Kitty", "Inbt", 50, 3)
        $ K_Addict -= 30
        $ K_Addictionrate += 2
        if "addictive" in P_Traits:
                $ K_Addictionrate += 3
        if K_CreamP == 1:
                $ K_SEXP += 10
                call Statup("Kitty", "Inbt", 70, 5)
#        call Kitty_Sex_Reset

# Clean-up / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label K_Orgasm_After:
        $ Line = "What next?"
        $ Kitty_Arms = 1
        $ P_Semen -= 1
        $ P_Focus = 0
        $ Speed = 0  
        menu:
                "Want her to clean you off?"
                "Yes":
                    call K_CleanCock
                "Actually, let [Partner] do it." if Partner:
                    call AllReset("Kitty") #resets the position of the orignal lead
                    call Partner_Clean
                    call AllReset("Kitty") #resets the position of the orignal lead
                "No":
                    pass
        if K_Spunk:
                call Kitty_Cleanup
        $ Situation = 0
        return
        
        
label K_CleanCock:
        $ Line = "What next?"
        $ Kitty_Arms = 1
        $ P_Cock = "out"
        $ Speed = 0    
        if Trigger == "anal" and not ApprovalCheck("Kitty", 1600, TabM=1) and not K_Addict >= 80:
                "She wipes your cock clean."
        elif K_Blow > 3 or K_Swallow: 
                if ApprovalCheck("Kitty", 1200, TabM=1) or K_Addict >= 60:
                        call Kitty_BJ_Launch("cum")
                        $ Speed = 1
                        call KittyFace("sucking", 1) 
                        if ApprovalCheck("Kitty", 1500, TabM=1):
                            if Partner and ApprovalCheck(Partner, 1500, TabM=1):
                                "Both girls look up at you as they lick your cock clean."
                            elif K_Love > K_Inbt and K_Love > K_Obed:
                                $ K_Eyes = "sly"
                                "She looks up at you lovingly as she licks your cock clean."            
                            elif K_Obed > K_Inbt:
                                $ K_Eyes = "side"
                                "She dutifully licks your cock clean with lowered eyes."
                                call Statup("Kitty", "Obed", 80, 3)                
                            else:
                                "She happily licks your cock clean." 
                        elif K_Addict >= 60:
                                "She hungrily and thoroughly licks your cock clean."   
                        else:
                            "She licks you cock clean." 
                        call KittyFace("sexy")  
                else:
                        if not renpy.showing("Kitty_HJ_Animation"):
                            call Kitty_HJ_Launch("cum") 
                        if Partner and ApprovalCheck(Partner, 1000, TabM=1):
                            "Both girls reach down and wipe your cock clean."
                        else:
                            "She wipes your cock clean."  
        else:
                        if not renpy.showing("Kitty_HJ_Animation"):
                            call Kitty_HJ_Launch("cum") 
                        if Partner and ApprovalCheck(Partner, 1000, TabM=1):
                            "Both girls reach down and wipe your cock clean."
                        else:
                            "She wipes your cock clean."     
        $ P_Spunk = 0
        call KittyFace("sexy") 
        return
                    


    
# End You Cumming //////////////////////////////////////////////////////////////////////////////////


# Kitty Lusty face check ////////////////////////////////////////////////////////////////////////////////
label KittyLust(Extreme = 0, Kissing = 0):
    if K_Lust >= 80:        
        $ K_Blush = 2
    elif K_Lust >= 40:        
        $ K_Blush = 1
        
    if K_Lust >= 80:
            $ K_Wet = 2 
    elif K_Lust >= 50:
            $ K_Wet = 1
    
    if Trigger3 == "kiss both" or Trigger3 == "kiss girl":
            #if the girls are kissing or all three are
            $ Kissing = 1
    elif Trigger4 == "kiss both" or Trigger3 == "kiss girl":
            #if the girls are kissing or all three are
            $ Kissing = 1   
    elif Partner != "Kitty":
            #If Kitty is kissing and is primary
            if Trigger == "kiss you" or Trigger2 == "kiss you":  
                $ Kissing = 1
    elif Trigger4 == "kiss you":   
            #If Kitty is kissing you in a threesome action
            $ Kissing = 1
    
    if Kissing:        
            #If Kitty is kissing and is primary
            $ K_Eyes = "closed"
            if K_Kissed >= 10 and K_Inbt >= 300:
                $ K_Mouth = "sucking"
            elif K_Kissed > 1 and K_Addict >= 50:            
                $ K_Mouth = "sucking"
            else:
                $ K_Mouth = "kiss"                        
    else:       
            #If Kitty is not kissing someone 
            if K_Lust >= 90:
                    $ K_Eyes = "closed"
                    $ K_Brows = "sad"
                    $ K_Mouth = "surprised"
            elif K_Lust >= 70:
                    $ K_Eyes = "sexy"
                    $ K_Brows = "sad"
                    $ K_Mouth = "lipbite"
            elif K_Lust >= 50 and not Extreme:
                    $ K_Eyes = "sexy"
                    $ K_Brows = "sad"
                    $ K_Mouth = "lipbite"
            elif K_Lust >= 30 and not Extreme:
                    $ K_Eyes = "sexy"
                    $ K_Brows = "normal"
                    if renpy.showing("Kitty_SexSprite"):
                            $ K_Mouth = "lipbite"
                    else:
                            $ K_Mouth = "kiss"
            elif not Extreme:
                    $ K_Eyes = "sexy"
                    $ K_Brows = "normal"
                    $ K_Mouth = "normal"
        
    if Partner == "Kitty" and Trigger4 in ("lick pussy", "lick ass", "blow", "suck breasts"):         
                    $ K_Mouth = "tongue"    
    elif Trigger3 in ("lick pussy", "lick ass", "suck breasts"):         
                    $ K_Mouth = "tongue"  
        
    if K_OCount >= 10:  
            #If you've fucked her senseless
            $ K_Eyes = "stunned"
            $ K_Mouth = "tongue"   
            
    if not K_Loose:     
            #if anal hurts. . .
            if Partner != "Kitty" and (Trigger == "anal" or Trigger == "dildo anal" or Trigger3 == "dildo anal"):  
                $ K_Eyes = "closed"
                $ K_Brows = "angry"
                
    return

# End faces  
    
#  Kitty Orgasm //////////////////////////

label K_Cumming(Quick=0):
    $ K_Eyes = "surprised"
    $ K_Brows = "sad"
    $ K_Mouth = "sucking"
    $ K_Blush = 1
    ch_k ". . . !"
    $ Speed = 0
    if renpy.showing("Kitty_SexSprite"):
            show Kitty_SexSprite #fix, test this
            with vpunch
    elif renpy.showing("Kitty_BJ_Animation"):           #fix, make this animation work better when paused for this effect.
            show Kitty_BJ_Animation
            with vpunch
    elif renpy.showing("Kitty_TJ_Animation"):
            show Kitty_TJ_Animation  
            with vpunch
    elif renpy.showing("Kitty_HJ_Animation"):
            show Kitty_HJ_Animation  
            with vpunch
    else:
            show Kitty_Sprite
            with vpunch
    $ Speed = 1
    $ Line = renpy.random.choice(["Kitty is suddenly rocked with spasms, holding back a muffled scream.", 
                "Kitty grabs on tightly as her body shakes with pleasure.", 
                "Kitty stiffens and lets out a low moan.",
                "Kitty's body quivers and suddenly goes still."])
    "[Line]"
    
    if Quick:
            call AnyFace("Kitty","sexy",2)  
            $ K_Lust = 20
            return
            
    $ K_Eyes = "closed"
    $ K_Brows = "sad"
    $ K_Mouth = "tongue"
    $ Line = renpy.random.choice(["Wow. . .  just, wow.", 
                "That was amazing!", 
                "Hmmmm. . . .",
                "I loved that!"])
    ch_k "[Line]"
           
    
    $ K_Lust = 30 if "hotblooded" in K_Traits else 0 
    $ K_Lust += (K_OCount * 5)
    $ K_Lust = 80 if K_Lust >= 80 else K_Lust 
    call Statup("Kitty", "Inbt", 50, 1)
    call Statup("Kitty", "Inbt", 70, 1)
            
    if "unsatisfied" in K_RecentActions:  #If she had been unsatisfied, you satisfied her. . .        
        call Statup("Kitty", "Love", 70, 2)
        call Statup("Kitty", "Love", 90, 1)
        if "unsatisfied" in K_DailyActions:
            ch_k "You know how to take care of me."
        call DrainWord("Kitty","unsatisfied")
    $ K_OCount += 1   
    $ K_Org += 1
    $ Line = 0
      
    if Trigger != "masturbation":
            call Statup("Kitty", "Lust", 40, 1)
            call Statup("Kitty", "Love", 70, 1)
            call Statup("Kitty", "Love", 90, 1)
            call Statup("Kitty", "Obed", 50, 2)
            call Statup("Kitty", "Obed", 70, 2)
            if K_OCount == 1:
                    # if she's angry, but not too angry, then reduce that on the first O of the time block.
                    $ K_ForcedCount -= 1 if 5 > K_ForcedCount > 0 else 0 
            
            #checks to check reaction of other girls
            if R_Loc == bg_current and "noticed Kitty" in R_RecentActions: 
                    $ R_Lust += 15 if R_LikeKitty >= 500 else 10
                    $ R_Lust += 5 if R_Les >= 5 else 0
            elif E_Loc == bg_current and "noticed Kitty" in E_RecentActions: 
                    $ E_Lust += 15 if E_LikeKitty >= 500 else 10
                    $ E_Lust += 5 if E_Les >= 5 else 0 
            elif L_Loc == bg_current and "noticed Kitty" in L_RecentActions: 
                    $ L_Lust += 15 if L_LikeKitty >= 500 else 10
                    $ L_Lust += 5 if L_Les >= 5 else 0 
            if Partner == "Kitty":
                    #If the active girl is someone else
                    call Partner_Cumming("Kitty")  
                            
            #Orgasm count   
            if Trigger != "blow" and Trigger != "hand" and Partner != "Kitty":
                if K_OCount == 2:
                        $ K_Brows = "confused"
                        ch_k "Hmm. . . so. . . good."
                        call Statup("Kitty", "Love", 50, 1)
                        call Statup("Kitty", "Love", 80, 2)
                        call Statup("Kitty", "Obed", 50, 1)
                        call Statup("Kitty", "Obed", 60, 1)            
                elif K_OCount == 3: #5
                        $ K_Brows = "confused"            
                        ch_k "You're. . .wearing. . .me. . .out. . ."
                        call Statup("Kitty", "Love", 50, 2)
                        call Statup("Kitty", "Love", 80, 2)
                        call Statup("Kitty", "Obed", 30, 1)
                        call Statup("Kitty", "Obed", 50, 1)                
                elif K_OCount == 5 and Partner != "Kitty": #10
                        $ K_Mouth = "tongue"    
                        ch_k "I'm . . .really. . . getting. . . tired. . . here. . ."    
                        menu:
                            ch_k "could. . . we. . . take. . . a. . .break?"
                            "Finish up." if P_FocusX:
                                "You release your concentration. . ."                 
                                $ P_FocusX = 0
                                $ P_Focus += 15                    
                            "Let's try something else." if MultiAction:  
                                $ Situation = "shift"
                            "No, I'm not done yet.":
                                if Trigger == "sex" or Trigger == "anal":
                                    if ApprovalCheck("Kitty", 1000, TabM=1) or ApprovalCheck("Kitty", 400, "O", TabM=1):
                                        call Statup("Kitty", "Love", 200, -5)
                                        call Statup("Kitty", "Obed", 50, 2)
                                        call Statup("Kitty", "Obed", 80, 3)
                                        $ K_Eyes = "stunned"
                                        "She drifts off into incoherent moans."
                                    else:
                                        call KittyFace("angry", 1)
                                        "She scowls at you, pulls out with a pop, and wipes herself off."
                                        ch_k "Looks like you're going to have to. . ."
                                        call Statup("Kitty", "Love", 50, -3, 1)
                                        call Statup("Kitty", "Love", 80, -4, 1)
                                        call Statup("Kitty", "Obed", 30, -1, 1)
                                        call Statup("Kitty", "Obed", 50, -1, 1)  
                                        $ K_RecentActions.append("angry")
                                        $ K_DailyActions.append("angry")   
                                else:
                                    call Statup("Kitty", "Obed", 50, 3)
                                    call Statup("Kitty", "Obed", 80, 2)
                                    $ K_Eyes = "stunned"
                                    "She drifts off into incoherent moans."   
                #end Ocount stuff 
    if Trigger == "strip":
            call AllReset("Kitty")
            show Kitty_Sprite at Kitty_Dance1()
            "Kitty begins to dance again."
    return
    
# End Kitty Orgasm /////////////////////////////////////////////////////////////////////////////////////


# Start Kitty Clean-Up /////////////////////////////////////////////////////////////////////////////////////
label Kitty_Cleanup(Choice = "random",Options=[],Cnt=0,Cleaned=0,Original="Kitty"):
    if Choice == "after":
            # This is at the end of a session
            if not K_Spunk:
                $ K_Wet = 0
                return    
            $ Cnt = 1
        
        
    if K_Addict > 80 and K_Swallow:
        #if she likes cum, she prefers to eat it. 
        $ Choice = "eat"            
        $ K_Eyes = "manic"
        $ K_Mouth = "smile" 
    elif Choice == "ask":
        pass
    elif "painted" in K_RecentActions and ApprovalCheck("Kitty", 1000, "OI"):
        return    
    elif ApprovalCheck("Kitty", 1200, "LO"):  
        $ Choice = "ask"   
    elif not ApprovalCheck("Kitty", 400, "I"):
        call KittyFace("bemused") 
        $ Choice = "clean"   
    elif not Cnt:
        $ Choice = "random"  
    else:
        $ Choice = "ask"      
   
    if Ch_Focus != "Kitty":
        # if Kitty isn't the lead, swap to her.
        $ Original = Partner
        call Shift_Focus("Kitty")
        
    $ Cleaned = 1 if "cleaned" in K_DailyActions else 0
    $ K_RecentActions.append("cleaned") 
    $ K_DailyActions.append("cleaned") 
    
    if Choice == "ask":
            $ Choice = "random"
            "She looks down at the spunk covering her."
            menu:
                "What do you suggest Kitty do about cleaning up?"
                "You should leave it where it is.":
                        if not Cnt:
                            # If this isn't the end of the session
                            if ApprovalCheck("Kitty", 300, "I") or ApprovalCheck("Kitty", 1000):
                                    call Statup("Kitty", "Obed", 70, 1)
                                    call Statup("Kitty", "Inbt", 50, 1)
                                    call Statup("Kitty", "Lust", 90, 2) 
                                    $ Choice = "leave"  
                                    call KittyFace("sly") 
                                    ch_k "Oh, ok.."
                            else:
                                    call KittyFace("sly") 
                                    ch_k "Hm, no."                                    
                        elif ApprovalCheck("Kitty", 900, "I") or "exhibitionist" in K_Traits:
                                call Statup("Kitty", "Obed", 70, 2)
                                call Statup("Kitty", "Obed", 90, 1)
                                call Statup("Kitty", "Lust", 90, 5) 
                                $ Choice = "leave"  
                                call KittyFace("sly") 
                                ch_k "Ooh, I like where your head is at. . "
                        elif ApprovalCheck("Kitty", 650, "I") and ApprovalCheck("Kitty", 1200, "LO"):
                                call Statup("Kitty", "Obed", 90, 1)
                                call Statup("Kitty", "Inbt", 80, 1) 
                                call Statup("Kitty", "Lust", 90, 5) 
                                $ Choice = "leave"  
                                call KittyFace("surprised",2) 
                                ch_k "Well, maybe. . ."
                                call KittyFace("sly",1) 
                        
                        else:
                            call KittyFace("angry") 
                            menu:
                                ch_k "Now you're just being ridiculous!" 
                                "Please?":
                                    if ApprovalCheck("Kitty", 1800):
                                        call Statup("Kitty", "Love", 85, 1)
                                        call Statup("Kitty", "Obed", 50, 2)
                                        call Statup("Kitty", "Obed", 80, 1)
                                        call Statup("Kitty", "Inbt", 40, 3) 
                                        call Statup("Kitty", "Inbt", 80, 1) 
                                        ch_k "Oh, fine!"
                                        $ Choice = "leave"  
                                    elif Cleaned:
                                        call KittyFace("angry") 
                                        ch_k "Seriously, quit bugging me about this."
                                    elif ApprovalCheck("Kitty", 800):
                                        call Statup("Kitty", "Inbt", 50, 1) 
                                        ch_k "You're persistant, but no way."
                                    else:
                                        call Statup("Kitty", "Love", 75, -5)
                                        call Statup("Kitty", "Love", 40, -10)
                                        call Statup("Kitty", "Obed", 90, 2)
                                        call KittyFace("angry") 
                                        ch_k "Don't be a dick."
                                "I insist.":
                                    call KittyFace("sad") 
                                    if ApprovalCheck("Kitty", 400, "I") and ApprovalCheck("Kitty", 1200, "LO"):
                                        call Statup("Kitty", "Obed", 40, 3)
                                        call Statup("Kitty", "Obed", 90, 2)
                                        ch_k "Fine, whatever."
                                        $ Choice = "leave"  
                                    elif ApprovalCheck("Kitty", 800, "O"):
                                        call Statup("Kitty", "Love", 50, -10)
                                        call Statup("Kitty", "Love", 200, -5)
                                        call Statup("Kitty", "Obed", 90, 10)
                                        call Statup("Kitty", "Obed", 200, 5)
                                        ch_k "Fine."
                                        $ Choice = "leave"  
                                    elif Cleaned:
                                        call Statup("Kitty", "Love", 50, -5)
                                        call Statup("Kitty", "Love", 200, -1)
                                        call KittyFace("angry") 
                                        ch_k "Seriously, stop bugging me about this."
                                    elif ApprovalCheck("Kitty", 800):
                                        call Statup("Kitty", "Love", 50, -3)
                                        call Statup("Kitty", "Love", 200, -1)
                                        call KittyFace("sad") 
                                        ch_k "That's a bit much." 
                                    else:
                                        call Statup("Kitty", "Love", 50, -10)
                                        call Statup("Kitty", "Love", 200, -5)
                                        call KittyFace("angry") 
                                        ch_k "Well that's too bad!"
                                        
                                "Never mind then.":
                                    ch_k "Right. . ."                            
                        #end "leave it"
                        
                "You should just eat it.":
                        call KittyFace("sly") 
                        if "hungry" in K_Traits or (K_Swallow >= 5 and ApprovalCheck("Kitty", 800)): 
                                #lots of swallows
                                call Statup("Kitty", "Obed", 90, 1)
                                call Statup("Kitty", "Inbt", 50, 3) 
                                call Statup("Kitty", "Inbt", 80, 1) 
                                call Statup("Kitty", "Lust", 90, 5) 
                                $ Choice = "eat"   
                                ch_k "Mmmmm, maybe . ."
                        elif K_Swallow and ApprovalCheck("Kitty", 800): 
                                #few swallows
                                call Statup("Kitty", "Obed", 50, 1)
                                call Statup("Kitty", "Obed", 90, 1)
                                call Statup("Kitty", "Inbt", 50, 2) 
                                call Statup("Kitty", "Inbt", 80, 1) 
                                call Statup("Kitty", "Lust", 90, 5) 
                                $ Choice = "eat"   
                                ch_k "It's not that bad. . ."
                        elif ApprovalCheck("Kitty", 1200): 
                                #no swallows, but likes you
                                call Statup("Kitty", "Obed", 50, 1)
                                call Statup("Kitty", "Obed", 90, 1)
                                call Statup("Kitty", "Inbt", 50, 3) 
                                call Statup("Kitty", "Inbt", 80, 1) 
                                $ Choice = "eat"   
                                ch_k "Huh, I guess. . ."
                        elif ApprovalCheck("Kitty", 400): 
                                #Likes you well enough, but won't
                                call KittyFace("sad") 
                                ch_k "Yeah, not really."
                        else: 
                                #doesn't like you.
                                call Statup("Kitty", "Love", 50, -5)
                                call Statup("Kitty", "Love", 200, -3)
                                call KittyFace("angry") 
                                ch_k "No."
                        #end eat it
                              
                "You should just clean it up.":
                        if ApprovalCheck("Kitty", 600, "I") and not ApprovalCheck("Kitty", 1500, "LO"): #rebellious
                                call KittyFace("sly") 
                                call Statup("Kitty", "Obed", 50, -3)
                                call Statup("Kitty", "Inbt", 70, 10) 
                                call Statup("Kitty", "Inbt", 200, 5) 
                                call Statup("Kitty", "Lust", 60, 5) 
                                ch_k "I don't know, [K_Petname], it doesn't look so bad. . ."
                                $ Choice = "leave"   
                                menu:
                                    extend ""
                                    "Ok, fine.":
                                        call KittyFace("smile") 
                                        call Statup("Kitty", "Love", 70, 5)
                                        call Statup("Kitty", "Obed", 50, 3)
                                    "No, clean it up.": 
                                        if ApprovalCheck("Kitty", 600, "O"):
                                            call KittyFace("sad") 
                                            call Statup("Kitty", "Obed", 50, 10)
                                            ch_k "Oh, fine. . ."
                                            $ Choice = "clean"  
                                        elif ApprovalCheck("Kitty", 1200, "LO"):
                                            call KittyFace("sad") 
                                            call Statup("Kitty", "Love", 70, -3)
                                            call Statup("Kitty", "Obed", 50, 3)
                                            ch_k "Boooo. . ."
                                            $ Choice = "clean"   
                                        else:
                                            call Statup("Kitty", "Love", 70, -5)
                                            call Statup("Kitty", "Obed", 50, -5)
                                            ch_k "No! I like it this way."
                                                                                    
                        else: #agrees
                                call KittyFace("bemused") 
                                $ Choice = "clean"   
                                ch_k "Ok, fine. . ."
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
            call Partner_Cleanup_Check("Kitty")
                
    if Choice == "random":
            $ Options = ["clean"]
            if K_Swallow and ApprovalCheck("Kitty", 800):
                    $ Options.append("eat") 
                    if K_Swallow >=5:                            
                        $ Options.append("eat") 
                    if "hungry" in K_Traits:                
                        $ Options.append("eat") 
            if ApprovalCheck("Kitty", 300, "I"):
                    if not Cnt:
                        $ Options.append("leave") 
                    if not Cnt or ApprovalCheck("Kitty", 600, "I"):
                        $ Options.append("leave") 
                    if not Cnt or ApprovalCheck("Kitty", 800, "I"):
                        $ Options.append("leave") 
                    if "exhibitionist" in K_Traits:
                        $ Options.append("leave") 
                    
            $ renpy.random.shuffle(Options)
            
            $ Choice = Options[0]
            #end "random"            
            
    if Choice == "leave":
            call Statup("Kitty", "Inbt", 80, 2) 
            call Statup("Kitty", "Inbt", 200, 1) 
            "She leaves the jiz right where it is and gives you a wink."
            if "hand" in K_Spunk: 
                    $ K_Spunk.remove("hand")
                    if K_Swallow:
                        "She does lick off her hand though."
                    else:
                        "She does wipe her hand off though."   
            if "mouth" in K_Spunk:                  
                    $ K_Spunk.remove("mouth")
            if Cnt:
                    # if this is final clean-up and left the jiz on   
                    $ K_RecentActions.append("painted")                  
                    $ K_DailyActions.append("painted")   
            #end "leave it"
    
    if K_Spunk and Choice != "leave":
            call Self_Cleanup("Kitty")
               
    if Ch_Focus != Original:
        # if Kitty wasn't the lead, swap that one back
        call Shift_Focus(Original)
    return    
    
# End Kitty Clean-Up /////////////////////////////////////////////////////////////////////////////////////

