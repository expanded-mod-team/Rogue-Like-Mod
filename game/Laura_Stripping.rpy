# start Strip Tease /////////////////////////////////////////////////////////////////////////////

label L_Stripping: 
        #This gets called by Group_Stripping, and returns there at the end. 
        if "stopdancing" in L_RecentActions: 
            #if she's just standing around, cut back to the other girl        
            if "stopdancing" in K_RecentActions: 
                    $ renpy.pop_call()
                    jump Group_Strip_End             
            if "stopdancing" in R_RecentActions: 
                    $ renpy.pop_call()
                    jump Group_Strip_End                  
            if "stopdancing" in L_RecentActions: 
                    $ renpy.pop_call()
                    jump Group_Strip_End    
            return
    
        $ Laura_Arms = 2
        call LauraLust(1) #sets her lusty face           
        if "keepdancing" not in L_RecentActions:  
                # if Count isn't 2, it loops. 
#                if L_Arms and not L_Over:          
#                        #will she lose the wristbands? Yes, yes she'll lose the gloves. They're gloves. 
#                        $ L_Arms = 0
#                        "She pulls her gloves off, and tosses them to the ground."  
                   
                if L_Over and L_Chest and (L_Panties or L_Legs or HoseNum("Laura") >= 10):          
                        #will she lose the overshirt when she's dressed under?
                        if ApprovalCheck("Laura", 750, TabM = 3):
                                call Statup("Laura", "Obed", 50, 1)
                                call Statup("Laura", "Inbt", 25, 1)                 
                                call Statup("Player", "Focus", 60, 3)
                                $ Line = L_Over
                                $ L_Over = 0
                                "She pulls her [Line] off and throws it behind her."  
                        else:
                                jump L_Strip_Ultimatum
                                    
                elif L_Legs and (L_Panties or HoseNum("Laura") >= 10):                              
                        #will she lose the pants/skirt if she has panties on?
                        if ApprovalCheck("Laura", 1000, TabM = 3) or (L_SeenPanties and not Taboo):
                                call Statup("Laura", "Lust", 50, 5)                
                                call Statup("Laura", "Obed", 50, 1)
                                call Statup("Laura", "Inbt", 30, 1)                
                                call Statup("Player", "Focus", 60, 5)
                                $ Line = L_Legs         
                                $ L_Legs = 0      
                                "She unzips and pulls down her [Line], dropping them to the floor."   
                                if not L_SeenPanties:
                                        call Statup("Laura", "Obed", 50, 2)                              
                                        call Statup("Laura", "Obed", 200, 3)
                                        call Statup("Laura", "Inbt", 50, 3)
                                        call Statup("Laura", "Inbt", 200, 2)
                                        $ L_SeenPanties = 1                
                        else:
                                jump L_Strip_Ultimatum          
                
                elif L_Boots: 
                        # Will she lose the boots?
                        call Statup("Laura", "Lust", 50, 2)
                        call Statup("Player", "Focus", 60, 2)
                        $ L_Boots = 0
                        "She unzips her boots and tosses them aside."  
                                    
                elif L_Hose: 
                        # Will she lose the hose?
                        if HoseNum("Laura") >= 10:
                                if ApprovalCheck("Laura", 1200, TabM = 3):
                                        call Statup("Laura", "Lust", 50, 6)
                                        call Statup("Player", "Focus", 60, 6)
                                else:    
                                        jump L_Strip_Ultimatum
                                
                        elif HoseNum("Laura") >= 6 and ApprovalCheck("Laura", 1200, TabM = 3):
                                if ApprovalCheck("Laura", 1200, TabM = 3):
                                        call Statup("Laura", "Lust", 50, 4)
                                        call Statup("Player", "Focus", 60, 4)
                                else:    
                                        jump L_Strip_Ultimatum
                        else:
                                call Statup("Laura", "Lust", 50, 3)
                                call Statup("Player", "Focus", 60, 3)
                        $ Line = L_Hose
                        $ L_Hose = 0
                        "She rolls the [Line] down off her legs, leaving them in a small pile."     
                    
                elif L_Over and not L_Chest and (L_Panties or HoseNum("Laura") >= 10):     
                    #will she lose the top when she's topless with panties?        
                    if ApprovalCheck("Laura", 1200, TabM = 3) or (L_SeenChest and not Taboo):
                            call Statup("Laura", "Lust", 60, 5)                
                            call Statup("Laura", "Obed", 50, 2)
                            call Statup("Laura", "Inbt", 50, 10)   
                            call Statup("Player", "Focus", 80, 15)     
                            $ Line = L_Over
                            $ L_Over = 0                       
                            if not L_SeenChest:
                                    call LauraFace("bemused", 1)
                                    call Statup("Laura", "Obed", 50, 3)                              
                                    call Statup("Laura", "Obed", 200, 4)
                                    call Statup("Laura", "Inbt", 50, 3)
                                    call Statup("Laura", "Inbt", 200, 3)    
                                    "She hesitantly glances down, and then with a shrug pulls her [Line] over her head, tossing it to the ground." 
                                    call Laura_First_Topless       
                            else:
                                    "She pulls her [Line] over her head, tossing it to the ground."     
                    else:
                            jump L_Strip_Ultimatum
                    
                elif L_Chest and not L_Over:                                     
                    # Will she lose the bra?
                    if ApprovalCheck("Laura", 1200, TabM = 3) or (L_SeenChest and not Taboo):
                            call Statup("Laura", "Lust", 60, 5)                
                            call Statup("Laura", "Obed", 50, 2)
                            call Statup("Laura", "Inbt", 50, 1)
                            call Statup("Player", "Focus", 80, 15)     
                            $ Line = L_Chest
                            $ L_Chest = 0   
                            if not L_SeenChest:
                                    call LauraFace("bemused", 1)
                                    call Statup("Laura", "Obed", 50, 3)                              
                                    call Statup("Laura", "Obed", 200, 4)
                                    call Statup("Laura", "Inbt", 50, 3)
                                    call Statup("Laura", "Inbt", 200, 3)          
                                    "She hesitantly glances down, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                                    call Laura_First_Topless
                            else:
                                    call LauraFace("sexy")
                                    "She pulls her [Line] over her head, tossing it to the ground."      
                    else:
                            jump L_Strip_Ultimatum
            
                elif L_Legs:                                                       
                    #will she lose the pants/skirt if she has no panties on?
                    if ApprovalCheck("Laura", 1350, TabM = 3) or (L_SeenPussy and not Taboo):
                            call Statup("Laura", "Lust", 75, 10)    
                            $ Line = L_Legs
                            $ L_Legs = 0                       
                            if not L_SeenPussy:
                                    call Statup("Laura", "Obed", 60, 3)
                                    call Statup("Laura", "Obed", 200, 5)
                                    call Statup("Laura", "Inbt", 50, 4)
                                    call Statup("Laura", "Inbt", 200, 4)  
                                    "She looks up at you, and then slowly unzips and pulls down her [Line], dropping them to the floor."   
                                    call Laura_First_Bottomless 
                            else:                            
                                    call Statup("Laura", "Obed", 50, 1)                              
                                    call Statup("Laura", "Obed", 75, 1)
                                    "She unzips and pulls down her [Line], dropping them to the floor."   
                                    call Statup("Laura", "Inbt", 70, 2)           
                            call Statup("Player", "Focus", 85, 15)
                    else:
                            jump L_Strip_Ultimatum
                    
                elif L_Over and not L_Panties:                                        
                    #will she lose the overshirt when she's bottomless under?
                    if ApprovalCheck("Laura", 1350, TabM = 3) or (L_SeenPussy and not Taboo):    
                            $ Line = L_Over
                            $ L_Over = 0               
                            if not L_SeenPussy:                
                                    call Statup("Laura", "Obed", 60, 3)                              
                                    call Statup("Laura", "Obed", 200, 5)
                                    call Statup("Laura", "Inbt", 50, 4)
                                    call Statup("Laura", "Inbt", 200, 4) 
                                    "She glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                                    call Laura_First_Bottomless                
                            else:
                                    "She pulls her [Line] over her head, tossing it to the ground." 
                            if not L_Chest:
                                    if not L_SeenChest:                
                                            call Statup("Laura", "Obed", 50, 3)  
                                            call Statup("Laura", "Inbt", 50, 3)
                                            call Laura_First_Topless
                                    else:
                                            call Statup("Laura", "Lust", 60, 15)                
                                            call Statup("Laura", "Obed", 50, 3)                              
                                            call Statup("Laura", "Obed", 75, 1)
                                            call Statup("Laura", "Inbt", 50, 3)
                            else:
                                    call Statup("Laura", "Lust", 75, 10)                
                                    call Statup("Laura", "Obed", 50, 1)                              
                                    call Statup("Laura", "Obed", 75, 1)
                                    call Statup("Laura", "Inbt", 70, 2)                
                            call Statup("Player", "Focus", 85, 15)    
                    else:
                            jump L_Strip_Ultimatum
                
                elif L_Chest:                                                               
                    # Will she go topless?
                    if ApprovalCheck("Laura", 1200, TabM = 3) or (L_SeenChest and not Taboo):
                            call Statup("Laura", "Lust", 60, 5) 
                            $ Line = L_Chest
                            $ L_Chest = 0              
                            if not L_SeenChest:
                                    call Statup("Laura", "Obed", 50, 3)                              
                                    call Statup("Laura", "Obed", 200, 4)               
                                    call Statup("Laura", "Inbt", 50, 3)
                                    call Statup("Laura", "Inbt", 200, 3)  
                                    "She glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground." 
                                    call Laura_First_Topless
                            else:                
                                    call Statup("Laura", "Obed", 50, 2)
                                    "She pulls her [Line] over her head, tossing it to the ground."  
                                    call Statup("Laura", "Inbt", 50, 1)
                            call Statup("Player", "Focus", 80, 15)   
                    else:
                            jump L_Strip_Ultimatum
                    
                elif L_Panties:                                                                       
                    # Will she go bottomless?
                    if ApprovalCheck("Laura", 1350, TabM = 3) or (L_SeenPussy and not Taboo):
                            call Statup("Laura", "Lust", 75, 10) 
                            $ Line = L_Panties
                            $ L_Panties = 0               
                            if not L_SeenPussy:
                                    call Statup("Laura", "Obed", 60, 3)                              
                                    call Statup("Laura", "Obed", 200, 5)
                                    call Statup("Laura", "Inbt", 50, 4)
                                    call Statup("Laura", "Inbt", 200, 4) 
                                    "She looks up at you, and then slowly pulls her [Line] down, kicking them off to the side."   
                                    call Laura_First_Bottomless
                            else:                
                                    call Statup("Laura", "Obed", 50, 1)                              
                                    call Statup("Laura", "Obed", 75, 1)
                                    "She looks up at you, and then gently pulls her [Line] down, kicking them off to the side."                  
                                    call Statup("Laura", "Inbt", 70, 2)   
                            call Statup("Player", "Focus", 85, 15)
                    else:
                            jump L_Strip_Ultimatum
                    
                else:    
                    if L_Neck or L_Arms:                        
                        $ L_Neck = 0
                        $ L_Arms = 0
                        "She tosses the rest aside."
                    call LauraFace("sexy")
                    ch_l "Well, that's all I've got, [L_Petname]. . ."
                    menu:
                            extend ""
                            "Ok, you can stop":
                                    $ L_RecentActions.append("stopdancing")  
                                    call L_Pos_Reset        
                            "Keep on dancing":
                                    $ L_RecentActions.append("keepdancing")
        # end "nude" not in L_RecentActions loop
                
        call Statup("Laura", "Lust", 70, 2)               #lust/Focus
        if "exhibitionist" in L_Traits:
                call Statup("Laura", "Lust", 200, 2)
        call Statup("Player", "Focus", 60, 3)
        if Trigger2 == "jackin":
                call Statup("Laura", "Lust", 200, 2)
                call Statup("Player", "Focus", 200, 5)
        
        if not P_Semen and P_Focus >= 50:
                $ P_Focus = 50

        if P_Focus >= 100 or L_Lust >= 100:                                     
                #If either of you could cum 
                
                if P_Focus >= 100:                                                  
                    #You cum             
                    call PL_Cumming
                    if "angry" in L_RecentActions:  
                        return    
                    call Statup("Laura", "Lust", 200, 5) 
                    if not P_Semen and Trigger2 == "jackin":
                        "You're spitting dust here, maybe just watch quietly for a while."
                        $ Trigger2 = 0
                
                    if P_Focus > 80:
                        jump Group_Strip_End   
                    
                if L_Lust >= 100:                                                  
                    #and Laura cums                    
                    call L_Cumming
                    if Situation == "shift" or "angry" in L_RecentActions:                    
                        $ Count = 0
                        jump Group_Strip_End  
                        
                call AllReset("Laura")
                show Laura_Sprite at Laura_Dance1()
                "Laura begins to dance again."
            
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")
        menu:
            "Laura should. . ."
            "Keep Dancing. . ." if "keepdancing" in L_RecentActions:
                    $ L_Eyes = "sexy"      
            "Keep Going. . ." if "keepdancing" not in L_RecentActions:
                    $ L_Eyes = "sexy"
                    if L_Love >= 700 or L_Obed >= 500:
                        if not Tempmod:
                            $ Tempmod = 10
                        elif Tempmod <= 20:
                            $ Tempmod += 1
                    if Taboo and L_Strip <= 10:
                        call Statup("Laura", "Obed", 50, 7)
                    elif Taboo or L_Strip <= 10:
                        call Statup("Laura", "Obed", 50, 5)
                    elif L_Strip <= 50:
                        call Statup("Laura", "Obed", 50, 3) 
                    "She continues to dance."  
                           
            "Stop stripping, keep dancing" if "keepdancing" not in L_RecentActions:
                    ch_l "Huh? I guess. . ."
                    $ L_RecentActions.append("keepdancing")
                
            "Start stripping again" if "keepdancing" in L_RecentActions:
                    $ L_RecentActions.remove("keepdancing")
                    if "stripforced" in L_RecentActions: 
                            ch_l ". . ."
                    else:
                            ch_l "Hmm. . ."
                    jump L_Stripping
                
            "Just watch silently":
                if "watching" not in L_RecentActions:
                    if "keepdancing" not in L_RecentActions:
                        if Taboo and L_Strip <= 10:
                            call Statup("Laura", "Inbt", 50, 3) 
                        elif Taboo or L_Strip <= 10:
                            call Statup("Laura", "Inbt", 50, 1) 
                    elif L_Strip <= 50:
                            call Statup("Laura", "Inbt", 50, 2)
                            call Statup("Laura", "Lust", 70, 2) 
                    $ L_RecentActions.append("watching")  
            
            "Start jack'in it." if Trigger2 != "jackin":
                    call L_Jackin                   
            "Stop jack'in it." if Trigger2 == "jackin":
                    $ Trigger2 = 0
            "Ok, that's enough.":
                    ch_l "Alright, [L_Petname]. . . "
                    $ renpy.pop_call()
                    jump Group_Strip_End
                    
        
        return
    


label L_Strip_Ultimatum:  
    if "keepdancing" in L_RecentActions: 
        return
               
    call L_Pos_Reset
    call LauraFace("bemused", 1)        
    if "stripforced" in L_RecentActions: 
        call LauraFace("sad", 1)    
        ch_l "Last call, [L_Petname]."
    else:
        ch_l "Ok, that's enough, [L_Petname]. . . for now."
    menu:
        extend ""
        "That's ok, you can stop.":    
                if "ultimatum" not in L_DailyActions:                             
                        call Statup("Laura", "Love", 50, 2)
                        call Statup("Laura", "Love", 90, 2)
                        call Statup("Laura", "Inbt", 50, 2)
                        $ L_DailyActions.append("ultimatum")
                $ L_RecentActions.append("stopdancing")
                return
        "That's ok, but keep dancing for a bit. . .":  
                if "ultimatum" not in L_DailyActions:                          
                        call Statup("Laura", "Love", 50, 2)
                        call Statup("Laura", "Obed", 50, 2)
                        call Statup("Laura", "Inbt", 50, 2)
                        $ L_DailyActions.append("ultimatum")
                $ L_RecentActions.append("keepdancing")
                if "stripforced" in L_RecentActions: 
                        ch_l ". . ."
                else:
                        ch_l "Eh? Fine."
        "You'd better." if L_Forced:
            if not ApprovalCheck("Laura", 500, "O", TabM=5) and not ApprovalCheck("Laura", 800, "L", TabM=5):                    
                    call LauraFace("angry")
                    ch_l "You'd better remember who you're talking to, [L_Petname]."
                    $ L_RecentActions.append("angry")
                    $ L_DailyActions.append("angry")  
                    call Remove_Girl("Laura")
                    return                                
            $ Tempmod += 20
            $ L_Forced += 1
            call LauraFace("sad")
            if "stripforced" in L_RecentActions:                    
                    call LauraFace("angry")
                    ch_l ". . ."
            else:
                    ch_l "Grrrr. . ."
                    $ L_RecentActions.append("stripforced")
            call Statup("Laura", "Love", 200, -40)
        "You can do better than that. Keep going." if not L_Forced:
            if not ApprovalCheck("Laura", 300, "O", TabM=5) and not ApprovalCheck("Laura", 700, "L", TabM=5):                   
                    call LauraFace("angry")
                    ch_l "I don't like that tone, [L_Petname]."
                    $ L_RecentActions.append("angry")
                    $ L_DailyActions.append("angry")  
                    call Remove_Girl("Laura")
                    return                
            call Statup("Laura", "Love", 200, -10)
            call Statup("Laura", "Obed", 50, 3)
            call Statup("Laura", "Obed", 75, 5)
            $ Tempmod += 20
            $ L_Forced += 1
            call LauraFace("sad")
            ch_l ". . . Right. . ."
            
    if "ultimatum" not in L_DailyActions:
            $ L_DailyActions.append("ultimatum")
    show Laura_Sprite at Laura_Dance1()
    "Laura begins to dance again."
    return
              
# end Strip Tease ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

transform Laura_Dance1():     
    subpixel True 
    pos (L_SpriteLoc, 50)
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
    
           

# Start Laura Undressing  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label L_Undress(Region = "ask", CountStore=0):  
    $ CountStore = Tempmod    
    if Partner == "Laura":
            $ Tempmod = 0  
    call Shift_Focus("Laura")           
                    
    if Region == "auto":
        if L_Upskirt and L_PantiesDown:
            return
        if L_Legs == "pants" and Tempmod < 20:
            $ Tempmod = 20
        if L_Lust >= 90:
            $ Tempmod += 10      
        elif L_Lust >= 80:
            $ Tempmod += 5  
        $ Situation = "auto"
        call Laura_Bottoms_Off(0)
        $ Situation = 0
    
    if Region == "ask":
        menu:
            "Which parts?"
            "Her top" if L_Over or L_Chest:    
                $ Region = "top"     
            "Her bottoms" if L_Legs or L_Panties or L_Hose:
                $ Region = "bottom"           
            "A little of both. . ." if (L_Over or L_Chest) and (L_Legs or L_Panties or L_Hose): 
                $ Region = "both"    
            "Never mind":
                pass
    
    if Region == "top":
        if L_Over or L_Chest:    
                call Laura_Top_Off(0)  
    elif Region == "bottom":
        if L_Legs or L_Panties or L_Hose:
                call Laura_Bottoms_Off(0)  
    elif Region == "both":        
            if L_Over or L_Chest:    
                    call Laura_Top_Off(0) 
            
            if Partner == "Laura":
                    $ Tempmod = 0
            else:
                    $ Tempmod = CountStore 
            
            if "angry" in L_RecentActions: 
                    pass            
            elif not L_Legs and not L_Panties and not L_Hose:
                    pass                
            elif "no topless" in L_RecentActions:
                    menu:
                        ch_l "Know when to fold'em, [L_Petname]."
                        "And now the bottoms?":
                            call Laura_Bottoms_Off(0) 
                        "You're probably right, sorry.":
                            pass
            else:
                    ch_p "And now the bottoms?"
                    call Laura_Bottoms_Off(0) 
                    
    
    $ Tempmod = CountStore
    return


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label Laura_Top_Off(Intro = 1, Line = 0, Cnt = 0):                                                    # Will she take her top off? Modifiers
    call Shift_Focus("Laura")
    
    if not L_Over and not L_Chest:                              # If she's already topless. Just skip back.
        $ Tempmod = 0
        return
        
    if "angry" in L_RecentActions:  
        ch_l "Don't push it, [L_Petname]."
        return
    
    if L_SeenChest and ApprovalCheck("Laura", 600) and not Taboo:                              #You've seen her tits.
        $ Tempmod += 20
    if "exhibitionist" in L_Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in L_Traits or "sex friend" in L_Petnames and not Taboo:
        $ Tempmod += 10
    elif "ex" in L_Traits:
        $ Tempmod -= 40 
    if "no topless" in L_RecentActions: 
        $ Tempmod -= 10
                     
    if Intro and not L_Uptop:
        if L_Over:
                ch_p "This might be easier without your [L_Over] on."
        elif L_Chest:
                ch_p "This might be easier without your [L_Chest] on."

    $ Approval = ApprovalCheck("Laura", 1200, TabM = 4) # 110, 125, 140, 300 taboo, -20 if already seen
    
    if Situation == "auto" and  (L_Over or L_Chest) and not L_Uptop:   
            $ Line = 0
            if ApprovalCheck("Laura", 1250, TabM = 1) or (L_SeenChest and ApprovalCheck("Laura", 500) and not Taboo):
                    #if she'd go topless
                    call Statup("Laura", "Inbt", 70, 1)
                    $ L_Uptop = 1
                    $ Line = L_Over if L_Over else L_Chest
                    "Laura scowls in irritation, and pulls her [Line] up over her breasts."
                    if Taboo:
                        call Statup("Laura", "Inbt", 90, (int(Taboo/20)))   
                    call Laura_First_Topless(1)
                    ch_l "That wasn't working out."  
            elif L_Over and L_Chest and ApprovalCheck("Laura", 800, TabM = 1):
                    #if she won't go topless, but has a bra on. . .
                    call Statup("Laura", "Inbt", 40, 1)
                    $ Line = L_Over
                    $ L_Over = 0
                    "Laura scowls in irritation, and pulls her [Line] over her head, throwing it aside."
                    ch_l "That wasn't working out."   
            $ Line = 0
            return  
             
    if Approval >= 2:                                                                               # Does she assume top off?            
        if "no topless" in L_DailyActions:
            ch_l "{i}Fine,{/i} but don't think I'm getting soft on you."
        call LauraFace("sexy", 1)
        if L_Forced:
            call LauraFace("sad", 1)
            call Statup("Laura", "Love", 20, -2, 1)
            call Statup("Laura", "Love", 70, -3, 1)
            call Statup("Laura", "Obed", 40, 2)
            call Statup("Laura", "Obed", 90, 1)
            call Statup("Laura", "Inbt", 50, 1)
        call Statup("Laura", "Inbt", 50, 3)  
        $ Cnt = 1
        while (L_Chest or L_Over) and Cnt:
            menu:                                                                                 #Menu All off?
                ch_l "What did you want to see, [L_Petname]?"  
                "Lose the wristbands." if L_Arms:
                    call LauraFace("bemused", 1)                    
                    $ L_Arms = 0               
                    "Laura  pulls off her wristbands and drops them to the floor."                     
                "Lose the [L_Over]." if L_Over:                 
                    call LauraFace("bemused", 1)                    
                    $ Line = L_Over
                    $ L_Over = 0
                    "Laura shrugs off her [Line] and it drops to the floor."
                "Just lose the [L_Chest]." if L_Over and L_Chest:
                    call LauraFace("bemused", 1)                    
                    $ Line = L_Chest
                    $ L_Chest = 0               
                    "Laura unfastens her [Line] beneath her [L_Over], and allows it to drop to the floor."   
                "Lose the [L_Chest]." if not L_Over and L_Chest:
                    call LauraFace("bemused", 1)
                    $ Line = L_Chest
                    $ L_Chest = 0              
                    "Laura pulls off her [Line] and allows it to drop to the floor." 
                "Just pull it up." if (L_Over or L_Chest) and not L_Uptop:
                    call LauraFace("bemused", 1)
                    $ L_Uptop = 1
                    if L_Over and L_Chest:
                            "Laura smiles and lifts up her tops. . ."   
                    else:
                            "Laura smiles and lifts up her top. . ."   
                "Lose both tops." if L_Over and L_Chest:
                    call LauraFace("bemused", 1)  
                    $ Line = L_Over
                    $ L_Over = 0
                    "Laura shrugs off her [Line]-"      
                    $ Line = L_Chest
                    $ L_Chest = 0 
                    "-followed quickly by her [Line]."           
                "That's enough. [[exit]":               
                    call LauraFace("bemused", 1)
                    ch_l "Suit yourself. . ."    
                    $ Cnt = 0
        if not L_Chest and not L_Over or L_Uptop:             
            call Statup("Laura", "Obed", 40, 2)
            call Statup("Laura", "Obed", 90, 1)
            call Laura_First_Topless  
        call Statup("Laura", "Lust", 80, 3)        
        $ L_RecentActions.append("ask topless")                      
        $ L_DailyActions.append("ask topless") 
        $ Tempmod = 0        
        return
        
    #Else, Approval < 2, Doesn't want to lose the top//////////////////////////////////  
                 
    call LauraFace("bemused", 1)   
    if Intro == "massage" and not Approval:
        ch_l "I could use a massage, but I'm keeping my clothes on."
    elif "no topless" in L_RecentActions: 
        call LauraFace("angry")
        ch_l "Don't push it, [L_Petname]."    
    elif Approval and not L_SeenChest:
        ch_l "I don't know, man."    
    elif not L_SeenChest:
        ch_l "I really don't think so."   
    elif "no topless" in L_DailyActions: 
        ch_l "Dude, relax."           
    elif "ask topless" in L_RecentActions: 
        ch_l "Again?"       
    elif Taboo:
        ch_l "[L_Petname], not around here, alright?"          
    elif Approval:
        ch_l "Are you sure?"
    else:
        ch_l "No."
        
    menu:
        extend ""
        "Sorry, sorry." if "no topless" in L_RecentActions:  
            call LauraFace("bemused", 1)   
            ch_l "Right, I get it, stay thirsty."
        "Ok, that's fine." if "no topless" not in L_RecentActions: 
            if "ask topless" not in L_DailyActions:
                call Statup("Laura", "Lust", 80, 3)
                call Statup("Laura", "Love", 70, 1)
                call Statup("Laura", "Love", 90, 1)
                call Statup("Laura", "Inbt", 50, 2)
            if L_Forced:
                $ L_Mouth = "grimace"
                ch_l "Ok."
                if "ask topless" not in L_DailyActions:
                    call Statup("Laura", "Love", 20, 2)
                    call Statup("Laura", "Love", 70, 2)
         
        "Lose the wristbands." if L_Arms:
            call LauraFace("bemused", 1)
            $ L_Arms = 0               
            "Laura  pulls off her wristbands and drops them to the floor." 
            
        "How about just the [L_Over]?" if L_Over:                                                # asked to go shirtless. 
            if ApprovalCheck("Laura", 1000, TabM = 3) and L_Chest: #80, 160 taboo 
                call LauraFace("sexy") 
                ch_l "I mean. . . I guess. . ."                 
                call LauraFace("bemused", 1)                
                $ Line = L_Over
                $ L_Over = 0
                "Laura shrugs off her [Line]."   
                call Statup("Laura", "Obed", 30, 1)
                call Statup("Laura", "Obed", 60, 1)
                call Statup("Laura", "Inbt", 30, 2)
            elif not L_Chest:
                $ L_Eyes = "surprised"
                $ L_Blush = 2
                ch_l "I don't really have anything on under here." 
                call Statup("Laura", "Inbt", 30, 1)
                menu:
                    extend ""
                    "Ok, you can leave it on.":
                        $ L_Mouth = "smile"
                        call Statup("Laura", "Love", 70, 2)
                        ch_l "Right."             
                    "I think I could handle it.":
                        if ApprovalCheck("Laura", 700, "I", TabM=3) or ApprovalCheck("Laura", 1100, TabM=3):
                            call LauraFace("bemused", 1)
                            ch_l "Maybe you could. . ."                               
                            call Statup("Laura", "Obed", 20, 2)                                                         
                            call Statup("Laura", "Obed", 60, 1)
                            call LauraFace("sexy")   
                            $ Line = L_Over
                            $ L_Over = 0
                            "Laura shrugs off her [Line]."   
                            call Statup("Laura", "Inbt", 30, 1)  
                            call Statup("Laura", "Inbt", 60, 1)
                            call Laura_First_Topless   
                        else:   
                            call LauraFace("bemused")
                            call Laura_Top_Off_Refused  
                            
                    "I know, take it off.":
                        call Laura_ToplessorNothing
                $ L_Blush = 1        
            else:   
                call LauraFace("sexy")
                call Laura_Top_Off_Refused  
                                 
        "Come on, Please? [[take it all off]":                                                                      # asked to go topless. 110, 270 Taboo   
            if Approval and ApprovalCheck("Laura", 600, "L", TabM=1):                 
                call Statup("Laura", "Obed", 40, 2)
                call LauraFace("sexy")   
                if "no topless" in L_RecentActions:     
                    ch_l "Fine, you thirsty weirdo."
                $ L_Uptop = 1
                "Laura just pulls her top up over her tits."
                call Statup("Laura", "Inbt", 30, 1)  
                call Statup("Laura", "Inbt", 60, 1)
                call Laura_First_Topless 
            elif "no topless" in L_RecentActions:
                call LauraFace("angry")
                ch_l "Still no."
                call Statup("Laura", "Love", 90, -5)  
                $ L_RecentActions.append("angry")
                $ L_DailyActions.append("angry")   
            else:   
                call LauraFace("sexy")
                call Laura_Top_Off_Refused
        
        "No, topless or nothing.":                                                              #demanded topless 60, 260 taboo 
            call Laura_ToplessorNothing
                                
        "Never mind.":
            pass
    
    $ L_RecentActions.append("ask topless")                      
    $ L_DailyActions.append("ask topless") 
    $ Tempmod = 0
    return


label Laura_Top_Off_Refused:                    #When you insist but she refuses    
    call LauraFace("angry")
    if "no topless" in L_RecentActions:  
        ch_l "You're getting real close to the line, [L_Petname]."
    elif "no topless" in L_DailyActions:  
        ch_l "You keep coming back with this, [L_Petname]."
    call LauraFace("sad")
    menu:
        ch_l "Let it go?"
        "Sure, never mind." if "no topless" not in L_RecentActions:
            call LauraFace("sexy")
            call Statup("Laura", "Love", 70, 2)
            ch_l "Good."  
        "Sorry, I'll drop it." if "no topless" in L_RecentActions:   
            ch_l "Good."  
        "No, I'm serious.":
            $ L_Brows = "angry"
            ch_l "Your funeral."
            call Statup("Laura", "Lust", 50, 5)
            call Statup("Laura", "Love", 70, -5, 1)
            if "no topless" not in L_RecentActions:
                call Statup("Laura", "Lust", 70, 5)
                call Statup("Laura", "Obed", 60, 5)    
            $ L_RecentActions.append("angry")
            $ L_DailyActions.append("angry")   
    $ L_RecentActions.append("no topless")                      
    $ L_DailyActions.append("no topless") 
    return
              

label Laura_ToplessorNothing:
    call LauraFace("angry")
    if ApprovalCheck("Laura", 700, "OI", TabM = 4) and ApprovalCheck("Laura", 400, "O", TabM = 3):       
        #She agrees to your ultimatum 
        call Statup("Laura", "Love", 20, -2, 1)
        call Statup("Laura", "Love", 80, -5, 1)
        call Statup("Laura", "Inbt", 60, 2)
        if "no topless" in L_RecentActions:             
            ch_l "Hrmph, whatever. . ."                 
        else:
            call LauraFace("sad")
            ch_l "Ugh, whatever."                
        call Statup("Laura", "Obed", 60, 5)
        call Statup("Laura", "Obed", 90, 2)
        $ L_Uptop = 1
        "Laura grumpily pulls her top up over her tits."
        if L_Arms:            
            $ L_Arms = 0    
            "She pulls off her wristbands and drops them to the floor."
        call Laura_First_Topless                       
    else:                                                                                                
        #she refuses your ultimatum
        call Statup("Laura", "Love", 200, -10)                
        call Statup("Laura", "Obed", 40, -1, 1)
        if "no topless" in L_RecentActions: 
            $L_Brows = "angry"
            ch_l "You have got to chill."  
        else: 
            ch_l "Nope."      
        $ L_RecentActions.append("no topless")                      
        $ L_DailyActions.append("no topless")     
        $ L_RecentActions.append("angry")
        $ L_DailyActions.append("angry")   
    return              
    
label Laura_First_Topless(Silent = 0, TempLine = 0):     
    if ChestNum("Laura") > 1 or OverNum("Laura") > 2:
        #if she's wearing substantial clothing. . .
        return     
    $ L_RecentActions.append("topless")                      
    $ L_DailyActions.append("topless")
    call DrainWord("Laura","no topless")    
    $ L_SeenChest += 1 
    if L_SeenChest > 1:     
        return                  #ends portion if you've already seen them
    
    
    call Statup("Laura", "Inbt", 70, 15)  
    if not Silent:
        call LauraFace("sly")
        "You get your first look at Laura's bare chest."
        ch_l "So? What are you looking at?"    
        $ L_Blush = 1
        menu:
            extend ""
            "Your tits, they look great.":            
                call Statup("Laura", "Love", 90, 20)
                call Statup("Laura", "Inbt", 70, 20)           
                call LauraFace("sexy",1,Eyes="down")    
                ch_l "Huh. I mean I guess so. . ."           
                call LauraFace("smile",0)
                call Statup("Laura", "Love", 40, 20)
            ". . . [[stunned]":            
                call Statup("Laura", "Love", 90, 10)
                call Statup("Laura", "Inbt", 70, 10)
                ch_l "Cat got your tongue?"
                call Statup("Laura", "Love", 40, 10)  
            "Huh, not what I was expecting. . .":        
                call Statup("Laura", "Love", 90, -30)
                call Statup("Laura", "Obed", 60, 25)
                call Statup("Laura", "Inbt", 70, -15)                          
                call LauraFace("confused",2)
                ch_l "Huh?"
                menu:        
                    "They're really perky!":    
                        call Statup("Laura", "Love", 90, 20)
                        call Statup("Laura", "Obed", 60, -20)
                        call Statup("Laura", "Inbt", 70, 20)                          
                        call LauraFace("perplexed",1)
                        ch_l "Oh. Right. . ."
                    "I, um, no, they're great!":                        
                        call LauraFace("angry",2, Mouth="smile")
                        call Statup("Laura", "Inbt", 70, 10)   
                        ch_l "Why wouldn't they be?"    
                    "Kitty's were tighter, that's all." if K_SeenChest:                            
                        $ TempLine = "Kitty"
                    "Emma's were a lot bigger, that's all." if E_SeenChest:                            
                        $ TempLine = "Kitty"
                        
                if TempLine:
                        call LauraFace("angry")
                        $ L_Mouth = "surprised"                        
                        call Statup("Laura", "Love", 90, -10)
                        call Statup("Laura", "Obed", 80, 30)
                        call Statup("Laura", "Inbt", 70, -25)  
                        ". . ."
                        $ L_Mouth = "sad"
                        if TempLine == "Emma":
                                if L_LikeEmma >= 800:
                                    call LauraFace("sly",2,Eyes="side")
                                    call Statup("Laura", "Obed", 80, 5)
                                    ch_l "They are kinda huge. . ."       
                                    $ L_LikeEmma += 20 
                                elif L_LikeEmma >= 600:
                                    $ L_Eyes = "side" 
                                    call Statup("Laura", "Obed", 80, 5)
                                    ch_l "I guess that's true. . ."    
                                else:                        
                                    $ L_LikeEmma -= 50
                                    $ Templine = "bad"
                                
                        elif TempLine == "Kitty":
                                if L_LikeKitty >= 800:
                                    call LauraFace("sly",2,Eyes="side")
                                    call Statup("Laura", "Obed", 80, 5)
                                    ch_l "She is very. . . streamlined. . ."       
                                    $ L_LikeKitty += 20 
                                elif L_LikeKitty >= 700:
                                    $ L_Eyes = "side" 
                                    call Statup("Laura", "Obed", 80, 5)
                                    ch_l "they are kinda. . . pointy. . ."    
                                else:                        
                                    $ L_LikeKitty -= 50
                                    $ Templine = "bad"
                        
                        
                        if TempLine == "bad":
                                call Statup("Laura", "Love", 90, -20)
                                ch_l "Still kinda rude though."   
                                call LauraOutfit
                                $ L_RecentActions.append("no topless")                      
                                $ L_DailyActions.append("no topless")  
                                $ L_RecentActions.append("angry")
                                $ L_DailyActions.append("angry")  
                        
                    
    else:
        if ApprovalCheck("Laura", 800) and not L_Forced:                #if she's not forced and happy about it
            call Statup("Laura", "Inbt", 70, 15) 
            call Statup("Laura", "Obed", 70, 15)              
            call LauraFace("smile")
        else:                                                           #if she's not happy about it
            call Statup("Laura", "Love", 90, -40)
            call Statup("Laura", "Inbt", 70, -20)                          
            call LauraFace("angry")
            call Statup("Laura", "Obed", 70, 40)
    return



# Bottoms ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label Laura_Bottoms_Off(Intro = 1, Line = 0, Cnt = 0):
    call Shift_Focus("Laura")
    
    if not L_Legs and not L_Panties and not L_Hose:                                  
        # If she's already bottomless. Just skip back.     
        $ Tempmod = 0
        return
    
    if "angry" in L_RecentActions:  
        ch_l "You're barking up the wrong tree."
        return
    
    # Will she take her bottoms off Modifiers
    if L_SeenPussy and ApprovalCheck("Laura", 800): #You've seen her Pussy.
        $ Tempmod += 20
    elif not L_Panties:
        $ Tempmod -= 20
    elif L_SeenPanties and ApprovalCheck("Laura", 600): #You've seen her panties.
        $ Tempmod += 5 
    if Intro == "dildo":
        $ Tempmod += 20
    if "exhibitionist" in L_Traits:
        $ Tempmod += (Taboo * 5)
    if "dating" in L_Traits or "sex friend" in L_Petnames and not Taboo:
        $ Tempmod += 10
    elif "ex" in L_Traits:
        $ Tempmod -= 40 
    if "no bottomless" in L_RecentActions: 
        $ Tempmod -= 20
    
    if Intro:
        if L_Legs and not L_Upskirt:
                ch_p "This might be easier without your [L_Legs] on."
        elif L_Panties and not L_PantiesDown:
                ch_p "This might be easier without your [L_Panties] on."
                
    $ Approval = ApprovalCheck("Laura", 1300, TabM = 5) # 120, 135, 150, -200(320) taboo, -25 if already seen
    
    if Situation == "auto":
            $ Cnt = 0
            
            if not L_Upskirt and not L_PantiesDown:                      
                if L_Legs == "skirt" and not L_Upskirt:                                          
                    #If she's in a skirt with panties, hike it up?
                    if Approval >= 2 or (L_SeenPussy and ApprovalCheck("Laura", 700) and not Taboo):
                        call Statup("Laura", "Inbt", 60, 1)
                        if Taboo:
                            call Statup("Laura", "Inbt", 90, (int(Taboo/20)))                 
                        $ L_Upskirt = 1
                        "She slides her skirt up."
                        $ Cnt = 1 
                        
                if PantsNum("Laura") >= 5 or HoseNum("Laura") >= 6:            
                    if L_Panties:                                               
                        #she has pants and panties on
                        if not Approval or (not L_SeenPanties and Taboo):
                            return   
                    elif Approval < 2 or (not L_SeenPussy and Taboo):
                        return     
                    elif L_Legs == "pants" and L_Upskirt:  
                        return
                    call Statup("Laura", "Inbt", 60, 1)
                    $ L_Upskirt = 1
                    "Laura shrugs, and then tugs her [Line] down." 
                    if L_Panties:
                        $ L_SeenPanties = 1
                    else:
                        call Laura_First_Bottomless(1)  
                        
                    if Taboo:
                        call Statup("Laura", "Inbt", 90, (int(Taboo/10)))  
                    $ Cnt = 1 
                
            if L_Panties and not L_PantiesDown:                                              
                # Just wearing panties, lose them?
                if Approval >= 2 or (L_SeenPussy and not Taboo):
                    call Statup("Laura", "Inbt", 70, 2)
                    if Taboo:
                        call Statup("Laura", "Inbt", 90, (int(Taboo/10)))  
                    $ L_PantiesDown = 1
                    if Cnt:
                        "and pulls her [L_Panties] down too."
                    else:
                        "Laura tsks in irritation, and tugs her [L_Panties] down." 
                    call Laura_First_Bottomless(1) 
                        
                    ch_l "I guess all that was in the way."  
            return
            
    
    if Approval >= 2:                 
            #will she volunteer to strip to underwear?///////////////////////////////////////////////////        
            call LauraFace("sexy", 1)
            if L_Forced:
                call LauraFace("sad", 1)              
                call Statup("Laura", "Love", 20, -2, 1)
                call Statup("Laura", "Love", 70, -3, 1)
                call Statup("Laura", "Obed", 50, 1)
                call Statup("Laura", "Obed", 90, 1)
                call Statup("Laura", "Inbt", 60, 1)
                $ Line = "Hmm, I guess."            
            elif Approval >= 3:
                $ Line = "What did you want off?"
            else:    
                $ Line = "Hm, what did you want me to lose?"
            
            call Laura_Bottoms_Off_Legs
                
            if not L_Panties and Action_Check("Laura", "recent", "bottomless") < 2: 
                call Statup("Laura", "Obed", 50, 2)
                call Statup("Laura", "Obed", 90, 1)
                call Statup("Laura", "Inbt", 50, 3)
                call Statup("Laura", "Lust", 80, 3)
    
  
        
    elif L_Legs or L_Panties or L_Hose:
            # She'd rather not strip but might        
            call LauraFace("bemused", 1) 
            if "no bottomless" in L_RecentActions: 
                call LauraFace("angry")
                ch_l "Now you're just embarrassing yourself."   
            elif "no topless" in L_RecentActions: 
                call LauraFace("angry")
                ch_l "This is really pushing it."  
            elif Approval and not L_SeenPussy:
                ch_l "I don't know if you're earned that yet."  
            elif not L_SeenPussy and "ask topless" in L_RecentActions:
                ch_l "Kinda pushing it, [L_Petname]. . ."    
            elif not L_SeenPussy:
                ch_l "Maybe, after you've earned it. . ."   
            elif "no bottomless" in L_DailyActions: 
                ch_l "So thirsty. . ."             
            elif Taboo:
                ch_l "This is pretty exposed, [L_Petname]. . ."  
            elif Approval:
                ch_l "Probably not. . ."   
            elif L_SeenPussy:
                ch_l "You've probably seen enough . . ."            
            elif PantsNum("Laura") >= 10:
                ch_l "Well, I'm keeping my pants on."           
            elif L_Legs == "skirt":
                ch_l "Well, I'm keeping my skirt on."   
            elif PantsNum("Laura") >= 5:
                ch_l "Well, I'm keeping my shorts on."  
            else:
                ch_l "Well, I'm keeping my panties on." 
            menu:            
                extend ""
                "Ok, never mind." if "no bottomless" not in L_RecentActions:  
                    if "ask bottomless" not in L_DailyActions:
                        call Statup("Laura", "Lust", 80, 2)
                        call Statup("Laura", "Love", 70, 1)
                        call Statup("Laura", "Love", 90, 1)
                        call Statup("Laura", "Obed", 50, 2)
                        call Statup("Laura", "Inbt", 50, 2)
                    if L_Forced:
                        $ L_Mouth = "smile"
                        ch_l "Right."
                        if "ask bottomless" not in L_DailyActions:
                            call Statup("Laura", "Love", 20, 3)
                            call Statup("Laura", "Love", 70, 4)
                            call Statup("Laura", "Inbt", 60, 2)
                        
                "Sorry, sorry." if "no bottomless" in L_RecentActions:  
                    ch_l "Good."
                 
                "Come on, Please?":       
                    if "no bottomless" in L_DailyActions:  
                            call LauraFace("angry")
                            ch_l "You heard me."
                    else:
                            if Approval and ApprovalCheck("Laura", 600, "L", TabM=2):   
                                call LauraFace("sexy", 1)
                                $ D20 = renpy.random.randint(1, 3)
                                if D20 == 3:
                                    $ Line = "Well. . ."
                                    $ Approval += 1
                                else:
                                    $ Line = "Maybe. . ."                        
                                call Laura_Bottoms_Off_Legs  
                            else:    
                                call LauraFace("sexy")
                                call Laura_Bottoms_Off_Refused
                                        
                "It doesn't have to be everything. . ." if L_Legs or HoseNum("Laura") >= 10 or L_Panties == "shorts":    
                    if Approval and "no bottomless" not in L_DailyActions:                    
                        call LauraFace("bemused", 1)
                        $Line = "Well like what were you thinking?"
                        call Laura_Bottoms_Off_Legs  
                    else:    # She refuses your request. . .
                        call LauraFace("sexy")
                        call Laura_Bottoms_Off_Refused                                
                "It doesn't have to be everything. . . (locked)" if not L_Legs and HoseNum("Laura") < 10 and L_Panties != "shorts":   
                    pass
                    
                "No, lose 'em.":            #85 and -200 taboo             
                    if (Approval and L_Obed >= 250) or (ApprovalCheck("Laura", 1000, "OI", TabM = 5) and ApprovalCheck("Laura", 500, "O", TabM = 3)):                    
                        call Statup("Laura", "Love", 20, -1, 1)
                        call Statup("Laura", "Love", 70, -5, 1)
                        call Statup("Laura", "Obed", 50, 4)
                        call Statup("Laura", "Obed", 80, 1)
                        call Statup("Laura", "Inbt", 60, 1)
                        $ Line =  "Don't push me. . ."  
                        $ Approval = 1 if Approval < 1 else Approval
                        $ L_Forced = 1
                        call Laura_Bottoms_Off_Legs                     
                    else:          
                        call Statup("Laura", "Love", 200, -10)
                        if ApprovalCheck("Laura", 400, "O"):
                            ch_l "No way." 
                        else:
                            call LauraFace("angry")
                            ch_l "Fuck off."                          
                            $ L_RecentActions.append("angry")
                            $ L_DailyActions.append("angry")   
                        $ L_RecentActions.append("no bottomless")                      
                        $ L_DailyActions.append("no bottomless")  
            #end approval
    
    $ Tempmod = 0
    $ L_RecentActions.append("ask bottomless")                      
    $ L_DailyActions.append("ask bottomless")     
    return           

label Laura_Bottoms_Off_Legs:    
    
    if L_Forced:        
        call LauraFace("sad", 1)
    elif ApprovalCheck("Laura", 1100, "OI", TabM = 3):        
        call LauraFace("sly")
    elif ApprovalCheck("Laura", 1400, TabM = 3):  
        call LauraFace("sexy", 1) 
    else:
        call LauraFace("bemused", 1) 
        
    $ Line = "What did you have in mind?" if not Line else Line
    $ Cnt = 1
    while Cnt and (L_Legs or L_Panties or L_Hose):
        menu:                                       # She's asking what you'd like to see.
            ch_l "[Line]"
            "Everything. . ." if Line != "Well like what were you thinking?": #approval a given
                        
                    if Approval < 2 and not L_Panties and HoseNum("Laura") < 10:
                        call Laura_NoPanties
                    
                    if L_Legs:
                        $ Line = L_Legs      
                        $ L_Legs = 0
                        "Laura pulls her [Line] down."
                        $ L_SeenPanties = 1 if not L_SeenPanties else L_SeenPanties
                                           
                    if Approval < 2 and not L_Panties and HoseNum("Laura") >= 10:
                        call Laura_NoPanties   
                        
                    if L_Boots:
                        $ L_Boots = 0
                        "She pulls her boots off."   
                        
                    if L_Hose:
                        $ Line = L_Hose #HoseName 
                        $ L_Hose = 0
                        "She rolls her hose off."                    
                                            
                    if Approval < 2:
                        call Laura_NoPanties   
                    if L_Panties:                               
                        $ Line = L_Panties   
                        $ L_Panties = 0  
                        "She reaches down and pulls her [Line] off." 
                    call Laura_First_Bottomless   
                    
                    
            "Lose the [L_Legs]." if L_Legs: 
                    if L_Panties and Approval >= 2:
                        call LauraFace("sexy")
                        ch_l "I guess I could. . ."
                    elif Approval:          
                        call LauraFace("sexy", 1)    
                        if Approval < 2 and not L_Panties and HoseNum("Laura") < 10:
                            call Laura_NoPanties
                    else:    
                        call LauraFace("sexy")
                        call Laura_Bottoms_Off_Refused
                        return
                        
                    $ Line = L_Legs      
                    $ L_Legs = 0
                    if not L_Panties and HoseNum("Laura") < 10:
                        call LauraFace("sly", 1)  
                        "She looks at you slyly before pulling her [Line] off." 
                        call Laura_First_Bottomless 
                    else:
                        "Laura pulls down her [Line]."                        
                        $ L_SeenPanties = 1 if not L_SeenPanties else L_SeenPanties
                    call LauraFace("bemused", 1)
            
            
            "Lose the [L_Panties]." if L_Panties:
                    if Approval < 2:
                        ch_l "I'm afraid not."
                        $ L_RecentActions.append("no bottomless")                      
                        $ L_DailyActions.append("no bottomless")   
                        return                        
                    else:
                        ch_l "Huh, ok. . ."                                    
                    $ Line = L_Panties   
                    $ L_Panties = 0  
                             
                    if PantsNum("Laura") >= 5:
                        "She pulls down her [L_Legs], then pulls her [Line] off and puts them back on."    
                    else:
                        "She reaches down and pulls her [Line] off."
                    if not L_Legs:
                        call Laura_First_Bottomless 
            
            "Lose the [L_Boots]." if L_Boots:
                    ch_l "Hm, if you want."   
                    $ L_Boots = 0                      
                    "She reaches down and pulls her boots off."
                      
            "Just give me a clear view. . ." if (L_Panties and not L_PantiesDown) or (L_Legs and not L_Upskirt):
                    if Approval >= 2:
                        ch_l "Whatever."
                        $ L_PantiesDown = 1 if L_Panties else 0
                        $ L_Upskirt = 1 if L_Legs else 0
                        "She shifts her [L_Legs] out of the way."
                    elif Approval >= 1 and L_Legs and L_Panties and not L_PantiesDown:
                        ch_l "Make do with this. . ."
                        $ L_Upskirt = 1
                    else:
                        ch_l "No."
                        $ L_RecentActions.append("no bottomless")                      
                        $ L_DailyActions.append("no bottomless")   
                        return   
                    call Laura_First_Bottomless    
                    
            
            "Lose the [L_Hose]." if L_Hose:                                    #make sure to update this mess if I add hose to her
                    call LauraFace("bemused", 1) 
                    if L_Legs:
                        ch_l "All right, fine."                         
                    elif Approval < 2 and not L_Panties and HoseNum("Laura") >= 10:
                        call Laura_NoPanties                            
                    elif not Approval and HoseNum("Laura") >= 6:
                        ch_l "Sorry, no, [L_Petname]."
                        return                            
                    else:
                        ch_l "Fine, [L_Petname]."                 
                        
                    $ Line = L_Hose   
                    $ L_Hose = 0  
                    if L_Legs:
                        "She reaches under her [L_Legs] and pulls her [Line] down."
                    elif HoseNum("Laura") < 10:
                        "Laura pulls her [Line] off." 
                    elif not L_Panties:
                        call LauraFace("sly", 2)  
                        "She looks at you before removing her [Line]." 
                        $ L_Blush = 1
                        call Laura_First_Bottomless   
                    elif not L_SeenPanties:
                        "Laura slowly removes her [Line]."
                        $ L_SeenPanties = 1
                    else:
                        "Laura pulls her [Line] off." 
                        
            "Keep it all on for now." if Cnt == 1:
                $ L_Mouth = "smile"
                $ Cnt = 0
                
            "Ok, that's enough for now." if Cnt == 2:
                $ Cnt = 0
                
        $ Cnt = 2 if Cnt else Cnt  
        $ Line = renpy.random.choice(["Is that it?",       
            "You finished?",
            "Anything else?"]) 
    return


label Laura_NoPanties: 
    #called when asked to remove pants with nothing on under
    if not R_Panties:
        return
    if L_Legs or HoseNum("Laura") >= 10:
        ch_l "I don't have anything on under this. . ."  
    else:
        ch_l "These are all I have on. . ."  
    menu:
        extend ""
        "Could you do it anyway?":
            if ApprovalCheck("Laura", 1100, "LI", TabM=1):                                             
                ch_l "I guess. . . "
            else:
                ch_l "Nah, not right now."
                call Laura_Bottoms_Off_Refused
                $ renpy.pop_call()  
        "Don't care, lose'em.":
            if ApprovalCheck("Laura", 800, "OI", TabM=1):
                ch_l "Fine."  
            else:
                call Laura_Bottoms_Off_Refused
                $ renpy.pop_call()  
                                       
        "Ok, you can leave it on.":
            $ renpy.pop_call()   
    return 
        
label Laura_Bottoms_Off_Refused:     
    if "no bottomless" in L_RecentActions:  
        ch_l "Reign it in."
    elif "no bottomless" in L_DailyActions:  
        ch_l "No, not today."
    else:
        call LauraFace("sad")
        if Cnt == 2:            
            ch_l "No more, is that going to be a problem?"   
        else:
            ch_l "Nope, is that going to be a problem?"        
    menu:
        extend ""
        "No, no, never mind." if "no bottomless" not in L_RecentActions:
            $ L_Mouth = "smile"
            call Statup("Laura", "Love", 70, 2)    
            call Statup("Laura", "Obed", 60, 2)  
            ch_l "Right."    
        "Sorry, I'll drop it." if "no bottomless" in L_RecentActions:   
            ch_l "Good. . ."  
        "Yeah, let's do something else.":
            $L_Brows = "confused"
            ch_l "Your loss."               
            call Statup("Laura", "Lust", 50, 5)
            call Statup("Laura", "Love", 70, -2, 1)
            if "no bottomless" not in L_RecentActions:  
                call Statup("Laura", "Lust", 70, 5)
                call Statup("Laura", "Obed", 60, 4)      
            $ L_RecentActions.append("angry")
            $ L_DailyActions.append("angry")   
            
    $ L_RecentActions.append("no bottomless")                      
    $ L_DailyActions.append("no bottomless")
    $ Tempmod = 0
    return   

label Laura_First_Bottomless(Silent = 0): 
    if PantiesNum("Laura") > 1 or PantsNum("Laura") > 2 or HoseNum("Laura") > 9:
        #if she's wearing substantial clothing. . .
        return     
    $ L_RecentActions.append("bottomless")                      
    $ L_DailyActions.append("bottomless")
    call DrainWord("Laura","no bottomless")
    $ L_SeenPussy += 1 
    if L_SeenPussy > 1:     
        return                  #ends portion if you've already seen them        
    
    
    call Statup("Laura", "Inbt", 80, 30)  
    call Statup("Laura", "Obed", 70, 10)   
    if not Silent:
        call LauraFace("sly")
        if L_Pubes:
            "You find yourself staring at [LauraName]'s furry pussy."   
        else:
            "You find yourself staring at [LauraName]'s bare pussy."        
        menu:        
            extend ""
            "Niiice. . .":            
                call Statup("Laura", "Love", 90, 20)
                call Statup("Laura", "Inbt", 60, 25)            
                call LauraFace("smile")          
                ch_l "You think?"
                ch_l "Yeah, I like it too. . . "
                call Statup("Laura", "Love", 40, 20)
            "I see you keep it natural down there." if L_Pubes:          
                call LauraFace("confused",1)  
                ch_l "Well. . . yeah."
                if ApprovalCheck("Laura", 700, "LO"):    
                    call LauraFace("bemused")     
                    menu:
                        ch_l "What, am I supposed to shave it?"
                        "Yes":
                            if ApprovalCheck("Laura", 900, "LO"):
                                call Statup("Laura", "Obed", 50, 30)
                                call Statup("Laura", "Inbt", 60, 25)        
                                ch_l "I guess I could. . ."
                                $ L_Todo.append("pubes")  
                            else:   
                                call LauraFace("normal")     
                                ch_l "Seems like a waste of time."
                                ch_l "Do you know how fast my hair grows?"
                        "Up to you, I guess.":
                                call Statup("Laura", "Love", 80, 10)
                                ch_l "Yeah, I mean, shaving would be a lot of work."
                        "No, leave it that way.":  
                                if ApprovalCheck("Laura", 900, "LO"):
                                    call LauraFace("sly")    
                                    call Statup("Laura", "Love", 80, 10)
                                else:
                                    call LauraFace("angry",Mouth="normal")    
                                call Statup("Laura", "Inbt", 60, 25) 
                                ch_l "Right."
                                $ L_Brows = "normal"
                else:                              
                    call LauraFace("angry",1)  
                    call Statup("Laura", "Love", 40, -20) 
                    call Statup("Laura", "Obed", 50, 25)
                    call Statup("Laura", "Inbt", 60, -5)         
                    ch_l "I mean, what else would I do?"
            "What a mess.":        
                call Statup("Laura", "Love", 90, -30)
                call Statup("Laura", "Obed", 50, 25)
                call Statup("Laura", "Inbt", 70, -30)
                call LauraFace("angry",2)           
                if not L_Forced and not ApprovalCheck("Laura", 900, "LO"):                    
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")  
                        call Statup("Laura", "Obed", 70, 25)
                ch_l "I'll make you a mess. . ."
    else:
        
        if ApprovalCheck("Laura", 800) and not L_Forced:
            call Statup("Laura", "Love", 90, 20)
            call Statup("Laura", "Inbt", 60, 25)          
            call LauraFace("smile")          
            call Statup("Laura", "Love", 40, 20)
            call Statup("Laura", "Obed", 70, 10)
        else:        
            call Statup("Laura", "Love", 90, -40)
            call Statup("Laura", "Inbt", 70, -20)
            call LauraFace("angry")          
            call Statup("Laura", "Obed", 70, 30)
    return
    
# End Laura Undressing  ///////////////////////////////////////////////////////////////////

    

label Laura_First_Peen(Silent = 0, Undress = 0, Second = 0, React = 0): 
    #checked each time she sees your cock  ## call Laura_First_Peen(0,1)
    #if Silent it doesn't say anything
    #if Undress then you get nude
    #if Secondary then this is the second girl to see it.
    # React 0 if other girl didn't comment, 
    # 1 = if the other girl commented, 2 = didn't like it
    
    if L_Loc != bg_current:
                if Partner == "Laura":
                        $ Partner = 0
                return  
    if "cockout" in P_RecentActions and "peen" in L_RecentActions: 
                #If the cock is already out and she's seen it, return
                return
            
    $ L_RecentActions.append("peen")                      
    $ L_DailyActions.append("peen")
    $ L_SeenPeen += 1                      
    call Statup("Laura", "Inbt", 30, 2) 
    call Statup("Laura", "Inbt", 80, 1)
    
    if Second:
        #If another girl commented on it first. . .
        if L_SeenPeen == 1: 
                call LauraFace("smirk", 2, Eyes = "down")  
                ch_l "Huh, that's a pretty good one you got there. . ."
                call LauraFace("bemused", 1)  
        elif Second == 1:
                # The other girl liked it
                if not ApprovalCheck("Laura", 800) and not ApprovalCheck("Laura", 500, "I"):
                    call LauraFace("sad", 1) 
                    ch_l "I guess . ."
                else:
                    call LauraFace("bemused", 1)  
                    ch_l "Yeah, nice, isn't it. . ."
        elif Second == 2:
                # The other girl didn't like it
                if not ApprovalCheck("Laura", 800) and not ApprovalCheck("Laura", 500, "I"):
                    call LauraFace("sad", 1)  
                    ch_l "I guess. . ."
                else:
                    call LauraFace("confused", 1)  
                    ch_l "Aw, come on, it's not that bad. . ."
                    call LauraFace("sly",0)  
        $ Silent = 1
        
    if Undress:
        $ P_RecentActions.append("naked")    
    if not Silent:        
        if "cockout" in P_RecentActions:
                call LauraFace("down", 2)  
                "Laura glances down at your exposed cock"
        elif React:
                #If called by a sex dialog
                "Laura unzips your pants and draws out your cock."
        elif Undress:
                "You strip nude."
        else:
                "You whip your cock out."
        if "cockout" not in P_RecentActions:
                $ P_RecentActions.append("cockout")
        if bg_current != "bg showerroom" and not ApprovalCheck("Laura", 800) and not ApprovalCheck("Laura", 400, "I"):
                    call LauraFace("surprised", Eyes="down")  
                    ch_l "Mmm?"
                    call LauraFace("angry", 1)  
                    $ L_RecentActions.append("angry")
                    $ L_DailyActions.append("angry")  
                    if L_SeenPeen == 1: 
                        call Statup("Laura", "Love", 90, -10)                
                        call Statup("Laura", "Obed", 50, 35)
                        call Statup("Laura", "Inbt", 60, 20)
                    else:                    
                        ch_l "Dude, not cool."
                        if Action_Check("Laura", "daily", "peen") >= 2:
                                #if she's seen more than one peen today         
                                call Statup("Laura", "Love", 90, -1)     
                                call Statup("Laura", "Obed", 50, 2)
                                call Statup("Laura", "Inbt", 60, 2)
                        else:
                                call Statup("Laura", "Love", 90, -5)                
                                call Statup("Laura", "Obed", 50, 12)
                                call Statup("Laura", "Inbt", 60, 10)  
                    $ React = 2                           
        elif Taboo > 20 and (not ApprovalCheck("Laura", 1500) or L_SEXP < 10) and bg_current != "bg showerroom":
                call LauraFace("surprised", 2)  
                ch_l "I think there's a time and place for that sort of thing." 
                $ React = 2
                if L_SeenPeen == 1: 
                    call LauraFace("bemused", 1, Eyes="down")  
                    ch_l ". . . not that I mind, myself. . ." 
                    $ React = 1
                    call Statup("Laura", "Love", 30, 15) 
                    call Statup("Laura", "Love", 90, 15)                
                    call Statup("Laura", "Obed", 50, 25)
                    call Statup("Laura", "Inbt", 60, 35)  
                call LauraFace("bemused",0)   
        elif L_SeenPeen > 10:
                return 0   
        elif ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "L"):
                call LauraFace("sly",1) 
                if L_SeenPeen == 1: 
                    call LauraFace("surprised",1, Eyes="down")  
                    ch_l "Huh, that's a pretty good one you got there. . ."
                    call LauraFace("bemused",1)  
                    call Statup("Laura", "Love", 50, 5)
                    call Statup("Laura", "Love", 90, 10) 
                elif L_SeenPeen == 2:  
                    $ L_Eyes = "down"
                    ch_l "Oh, there it is."               
                    call Statup("Laura", "Inbt", 60, 5) 
                elif L_SeenPeen == 5: 
                    ch_l "Yeah, I've seen that one." 
                    call Statup("Laura", "Obed", 50, 7) 
                elif L_SeenPeen == 10:  
                    $ L_Eyes = "down"
                    ch_l "I don't get tired of that view."
                    call Statup("Laura", "Obed", 80, 5)
                    call Statup("Laura", "Inbt", 60, 10)  
                $ L_Eyes = "squint" 
                $ React = 1
        else:
                call LauraFace("sad",1) 
                if L_SeenPeen == 1: 
                    call LauraFace("perplexed",1 ) 
                    ch_l "Your dick is out."
                    call Statup("Laura", "Obed", 50, 7)
                    call Statup("Laura", "Inbt", 60, 3)  
                elif L_SeenPeen < 5: 
                    call LauraFace("sad",0) 
                    ch_l "Hey. . ."
                    ch_l "You might want to put that away, [L_Petname]."
                    call Statup("Laura", "Inbt", 60, 2)  
                elif L_SeenPeen == 10: 
                    ch_l "Yeah, yeah, waving your cock around again."               
                    call Statup("Laura", "Obed", 50, 7)
                    call Statup("Laura", "Inbt", 60, 5)   
                $ React = 2
    
    else: #Silent mode
                $ P_RecentActions.append("cockout") 
                if L_SeenPeen > 10:
                    return 0
                elif ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "L"):
                        if L_SeenPeen == 1: 
                            call Statup("Laura", "Love", 90, 3) 
                        elif L_SeenPeen == 2:      
                            call Statup("Laura", "Inbt", 60, 5) 
                        elif L_SeenPeen == 5:          
                            call Statup("Laura", "Obed", 50, 7) 
                        elif L_SeenPeen == 10: 
                            call Statup("Laura", "Love", 90, 10)  
                else:
                        if L_SeenPeen == 1: 
                            call Statup("Laura", "Obed", 50, 7)
                            call Statup("Laura", "Inbt", 60, 3)  
                        elif L_SeenPeen < 5: 
                            call Statup("Laura", "Inbt", 60, 2)  
                        elif L_SeenPeen == 10:              
                            call Statup("Laura", "Obed", 50, 7)
                            call Statup("Laura", "Inbt", 60, 3) 
                            
    if L_SeenPeen == 1 and "angry" not in L_RecentActions:         
        call Statup("Laura", "Love", 50, 10)          
        call Statup("Laura", "Love", 90, 10)                
        call Statup("Laura", "Obed", 90, 20)
        call Statup("Laura", "Inbt", 60, 20) 
        call Statup("Laura", "Lust", 80, 10)
    
    return React
    # End Laura shown peen
    
    