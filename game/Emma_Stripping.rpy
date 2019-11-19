# start Strip Tease /////////////////////////////////////////////////////////////////////////////
label E_Strip(Tempmod = Tempmod):    
#    call Shift_Focus("Emma")
#    $ Round -= 5 if Round > 5 else (Round-1)
#    $ E_SpriteLoc = StageCenter 
#    call Set_The_Scene
#    $ Emma_Arms = 2
#    call EmmaFace("sexy")
       
#    if "stripping" in E_DailyActions:
#        call EmmaFace("sexy", 1)
#        $ Line = renpy.random.choice(["You like when I dance for you?",       
#            "Didn't get enough earlier?",
#            "This is quite a workout."]) 
#        ch_e "[Line]" 

#    call AllReset("Emma")
#    show Emma_Sprite at Emma_Dance1()
#    "She starts to dance."  
    
#    if E_SeenChest or E_SeenPussy:              #You've seen her tits.
#        $ Tempmod += 20
#    if E_SeenPanties:                           #You've seen her panties.
#        $ Tempmod += 5
#    if "exhibitionist" in E_Traits:
#        $ Tempmod += (4*Taboo)
#    if ("dating" in E_Traits or "sex friend" in E_Petnames) and not Taboo:
#        $ Tempmod += 15
#    elif "ex" in E_Traits:
#        $ Tempmod -= 40 
#    elif E_ForcedCount and not E_Forced:
#        $ Tempmod -= 5 * E_ForcedCount
#    $ Trigger = "strip"
#    $ E_RecentActions.append("stripping")                      
#    $ E_DailyActions.append("stripping") 
#    $ E_Strip += 1
#    $ Count = 1
    
label E_Stripping: 
        #This gets called by Group_Stripping, and returns there at the end. 
        if "stopdancing" in E_RecentActions: 
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
    
        $ Emma_Arms = 2
        call EmmaLust(1) #sets her lusty face           
        if "keepdancing" not in E_RecentActions:  
                # if Count isn't 2, it loops. 
                if E_Arms and not E_Over:          
                        #will she lose the gloves? Yes, yes she'll lose the gloves. They're gloves. 
                        $ E_Arms = 0
                        "She pulls her gloves off, and tosses them to the ground."  
                   
                elif E_Over and E_Chest and (E_Panties or E_Legs or HoseNum("Emma") >= 10):          
                        #will she lose the overshirt when she's dressed under?
                        if ApprovalCheck("Emma", 750, TabM = 3):
                                call Statup("Emma", "Obed", 50, 1)
                                call Statup("Emma", "Inbt", 25, 1)                 
                                call Statup("Player", "Focus", 60, 3)
                                $ Line = E_Over
                                $ E_Over = 0
                                "She pulls her [Line] over her head and throws it behind her."  
                        else:
                                jump E_Strip_Ultimatum
                                    
                elif E_Legs and (E_Panties or HoseNum("Emma") >= 10):                              
                        #will she lose the pants/skirt if she has panties on?
                        if ApprovalCheck("Emma", 1000, TabM = 3) or (E_SeenPanties and not Taboo):
                                call Statup("Emma", "Lust", 50, 5)                
                                call Statup("Emma", "Obed", 50, 1)
                                call Statup("Emma", "Inbt", 30, 1)                
                                call Statup("Player", "Focus", 60, 5)
                                $ Line = E_Legs         
                                $ E_Legs = 0      
                                "She unzips and pulls down her [Line], dropping them to the floor."   
                                if not E_SeenPanties:
                                        call Statup("Emma", "Obed", 50, 2)                              
                                        call Statup("Emma", "Obed", 200, 3)
                                        call Statup("Emma", "Inbt", 50, 3)
                                        call Statup("Emma", "Inbt", 200, 2)
                                        $ E_SeenPanties = 1                
                        else:
                                jump E_Strip_Ultimatum          
                
                elif E_Boots: 
                        # Will she lose the boots?
                        call Statup("Emma", "Lust", 50, 2)
                        call Statup("Player", "Focus", 60, 2)
                        $ E_Boots = 0
                        "She unzips her boots and tosses them aside."  
                                    
                elif E_Hose: 
                        # Will she lose the hose?
                        if HoseNum("Emma") >= 10:
                                if ApprovalCheck("Emma", 1200, TabM = 3):
                                        call Statup("Emma", "Lust", 50, 6)
                                        call Statup("Player", "Focus", 60, 6)
                                else:    
                                        jump E_Strip_Ultimatum
                                
                        elif HoseNum("Emma") >= 6 and ApprovalCheck("Emma", 1200, TabM = 3):
                                if ApprovalCheck("Emma", 1200, TabM = 3):
                                        call Statup("Emma", "Lust", 50, 4)
                                        call Statup("Player", "Focus", 60, 4)
                                else:    
                                        jump E_Strip_Ultimatum
                        else:
                                call Statup("Emma", "Lust", 50, 3)
                                call Statup("Player", "Focus", 60, 3)
                        $ Line = E_Hose
                        $ E_Hose = 0
                        "She rolls the [Line] down off her legs, leaving them in a small pile."     
                    
                elif E_Over and not E_Chest and (E_Panties or HoseNum("Emma") >= 10):     
                    #will she lose the top when she's topless with panties?        
                    if ApprovalCheck("Emma", 1200, TabM = 3) or (E_SeenChest and not Taboo):
                            call Statup("Emma", "Lust", 60, 5)                
                            call Statup("Emma", "Obed", 50, 2)
                            call Statup("Emma", "Inbt", 50, 10)   
                            call Statup("Player", "Focus", 80, 15)     
                            $ Line = E_Over
                            $ E_Over = 0                       
                            if not E_SeenChest:
                                    call EmmaFace("bemused", 1)
                                    call Statup("Emma", "Obed", 50, 3)                              
                                    call Statup("Emma", "Obed", 200, 4)
                                    call Statup("Emma", "Inbt", 50, 3)
                                    call Statup("Emma", "Inbt", 200, 3)    
                                    "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground." 
                                    call Emma_First_Topless       
                            else:
                                    "She pulls her [Line] over her head, tossing it to the ground."     
                    else:
                            jump E_Strip_Ultimatum
                    
                elif E_Chest and not E_Over:                                     
                    # Will she lose the bra?
                    if ApprovalCheck("Emma", 1200, TabM = 3) or (E_SeenChest and not Taboo):
                            call Statup("Emma", "Lust", 60, 5)                
                            call Statup("Emma", "Obed", 50, 2)
                            call Statup("Emma", "Inbt", 50, 1)
                            call Statup("Player", "Focus", 80, 15)     
                            $ Line = E_Chest
                            $ E_Chest = 0   
                            call Emma_Tits_Up
                            if not E_SeenChest:
                                    call EmmaFace("bemused", 1)
                                    call Statup("Emma", "Obed", 50, 3)                              
                                    call Statup("Emma", "Obed", 200, 4)
                                    call Statup("Emma", "Inbt", 50, 3)
                                    call Statup("Emma", "Inbt", 200, 3)          
                                    "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                                    call Emma_First_Topless
                            else:
                                    call EmmaFace("sexy")
                                    "She pulls her [Line] over her head, tossing it to the ground."      
                    else:
                            jump E_Strip_Ultimatum
            
                elif E_Legs:                                                       
                    #will she lose the pants/skirt if she has no panties on?
                    if ApprovalCheck("Emma", 1350, TabM = 3) or (E_SeenPussy and not Taboo):
                            call Statup("Emma", "Lust", 75, 10)    
                            $ Line = E_Legs
                            $ E_Legs = 0                       
                            if not E_SeenPussy:
                                    call Statup("Emma", "Obed", 60, 3)
                                    call Statup("Emma", "Obed", 200, 5)
                                    call Statup("Emma", "Inbt", 50, 4)
                                    call Statup("Emma", "Inbt", 200, 4)  
                                    "She shyly looks up at you, and then slowly unzips and pulls down her [Line], dropping them to the floor."   
                                    call Emma_First_Bottomless 
                            else:                            
                                    call Statup("Emma", "Obed", 50, 1)                              
                                    call Statup("Emma", "Obed", 75, 1)
                                    "She unzips and pulls down her [Line], dropping them to the floor."   
                                    call Statup("Emma", "Inbt", 70, 2)           
                            call Statup("Player", "Focus", 85, 15)
                    else:
                            jump E_Strip_Ultimatum
                    
                elif E_Over and not E_Panties:                                        
                    #will she lose the overshirt when she's bottomless under?
                    if ApprovalCheck("Emma", 1350, TabM = 3) or (E_SeenPussy and not Taboo):    
                            $ Line = E_Over
                            $ E_Over = 0               
                            if not E_SeenPussy:                
                                    call Statup("Emma", "Obed", 60, 3)                              
                                    call Statup("Emma", "Obed", 200, 5)
                                    call Statup("Emma", "Inbt", 50, 4)
                                    call Statup("Emma", "Inbt", 200, 4) 
                                    "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                                    call Emma_First_Bottomless                
                            else:
                                    "She pulls her [Line] over her head, tossing it to the ground." 
                            if not E_Chest:
                                    if not E_SeenChest:                
                                            call Statup("Emma", "Obed", 50, 3)  
                                            call Statup("Emma", "Inbt", 50, 3)
                                            call Emma_First_Topless
                                    else:
                                            call Statup("Emma", "Lust", 60, 15)                
                                            call Statup("Emma", "Obed", 50, 3)                              
                                            call Statup("Emma", "Obed", 75, 1)
                                            call Statup("Emma", "Inbt", 50, 3)
                            else:
                                    call Statup("Emma", "Lust", 75, 10)                
                                    call Statup("Emma", "Obed", 50, 1)                              
                                    call Statup("Emma", "Obed", 75, 1)
                                    call Statup("Emma", "Inbt", 70, 2)                
                            call Statup("Player", "Focus", 85, 15)    
                    else:
                            jump E_Strip_Ultimatum
                
                elif E_Chest:                                                               
                    # Will she go topless?
                    if ApprovalCheck("Emma", 1200, TabM = 3) or (E_SeenChest and not Taboo):
                            call Statup("Emma", "Lust", 60, 5) 
                            $ Line = E_Chest
                            $ E_Chest = 0   
                            call Emma_Tits_Up            
                            if not E_SeenChest:
                                    call Statup("Emma", "Obed", 50, 3)                              
                                    call Statup("Emma", "Obed", 200, 4)               
                                    call Statup("Emma", "Inbt", 50, 3)
                                    call Statup("Emma", "Inbt", 200, 3)  
                                    "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground." 
                                    call Emma_First_Topless
                            else:                
                                    call Statup("Emma", "Obed", 50, 2)
                                    "She pulls her [Line] over her head, tossing it to the ground."  
                                    call Statup("Emma", "Inbt", 50, 1)
                            call Statup("Player", "Focus", 80, 15)   
                    else:
                            jump E_Strip_Ultimatum
                    
                elif E_Panties:                                                                       
                    # Will she go bottomless?
                    if ApprovalCheck("Emma", 1350, TabM = 3) or (E_SeenPussy and not Taboo):
                            call Statup("Emma", "Lust", 75, 10) 
                            $ Line = E_Panties
                            $ E_Panties = 0               
                            if not E_SeenPussy:
                                    call Statup("Emma", "Obed", 60, 3)                              
                                    call Statup("Emma", "Obed", 200, 5)
                                    call Statup("Emma", "Inbt", 50, 4)
                                    call Statup("Emma", "Inbt", 200, 4) 
                                    "She shyly looks up at you, and then slowly pulls her [Line] down, kicking them off to the side."   
                                    call Emma_First_Bottomless
                            else:                
                                    call Statup("Emma", "Obed", 50, 1)                              
                                    call Statup("Emma", "Obed", 75, 1)
                                    "She  looks up at you, and then gently pulls her [Line] down, kicking them off to the side."                  
                                    call Statup("Emma", "Inbt", 70, 2)   
                            call Statup("Player", "Focus", 85, 15)
                    else:
                            jump E_Strip_Ultimatum
                    
                else:    
                    call EmmaFace("sexy")
                    ch_e "Well, it appears I've run out of clothes, [E_Petname]. . ."
                    menu:
                            extend ""
                            "Ok, you can stop":
                                    $ E_RecentActions.append("stopdancing")  
                                    call E_Pos_Reset        
                            "Keep on dancing":
                                    $ E_RecentActions.append("keepdancing")
        # end "nude" not in E_RecentActions loop
                
        call Statup("Emma", "Lust", 70, 2)               #lust/Focus
        if "exhibitionist" in E_Traits:
                call Statup("Emma", "Lust", 200, 2)
        call Statup("Player", "Focus", 60, 3)
        if Trigger2 == "jackin":
                call Statup("Emma", "Lust", 200, 2)
                call Statup("Player", "Focus", 200, 5)
        
        if not P_Semen and P_Focus >= 50:
                $ P_Focus = 50

        if P_Focus >= 100 or E_Lust >= 100:                                     
                #If either of you could cum 
                
                if P_Focus >= 100:                                                  
                    #You cum             
                    call PE_Cumming
                    if "angry" in E_RecentActions:  
                        return    
                    call Statup("Emma", "Lust", 200, 5) 
                    if not P_Semen and Trigger2 == "jackin":
                        "You're spitting dust here, maybe just watch quietly for a while."
                        $ Trigger2 = 0
                
                    if P_Focus > 80:
                        jump Group_Strip_End   
                    
                if E_Lust >= 100:                                                  
                    #and Emma cums                    
                    call E_Cumming
                    if Situation == "shift" or "angry" in E_RecentActions:                    
                        $ Count = 0
                        jump Group_Strip_End  
                        
                call AllReset("Emma")
                show Emma_Sprite at Emma_Dance1()
                "Emma begins to dance again."
            
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Emma")
        menu:
            "Emma should. . ."
            "Keep Dancing. . ." if "keepdancing" in E_RecentActions:
                    $ E_Eyes = "sexy"      
            "Keep Going. . ." if "keepdancing" not in E_RecentActions:
                    $ E_Eyes = "sexy"
                    if E_Love >= 700 or E_Obed >= 500:
                        if not Tempmod:
                            $ Tempmod = 10
                        elif Tempmod <= 20:
                            $ Tempmod += 1
                    if Taboo and E_Strip <= 10:
                        call Statup("Emma", "Obed", 50, 7)
                    elif Taboo or E_Strip <= 10:
                        call Statup("Emma", "Obed", 50, 5)
                    elif E_Strip <= 50:
                        call Statup("Emma", "Obed", 50, 3) 
                    "She continues to dance."  
                           
            "Stop stripping, keep dancing" if "keepdancing" not in E_RecentActions:
                    ch_e "Oh? Very well."
                    $ E_RecentActions.append("keepdancing")
                
            "Start stripping again" if "keepdancing" in E_RecentActions:
                    $ E_RecentActions.remove("keepdancing")
                    if "stripforced" in E_RecentActions: 
                            ch_e ". . ."
                    else:
                            ch_e "Hmm. . ."
                    jump E_Stripping
                
            "Just watch silently":
                if "watching" not in E_RecentActions:
                    if "keepdancing" not in E_RecentActions:
                        if Taboo and E_Strip <= 10:
                            call Statup("Emma", "Inbt", 50, 3) 
                        elif Taboo or E_Strip <= 10:
                            call Statup("Emma", "Inbt", 50, 1) 
                    elif E_Strip <= 50:
                            call Statup("Emma", "Inbt", 50, 2)
                            call Statup("Emma", "Lust", 70, 2) 
                    $ E_RecentActions.append("watching")  
            
            "Start jack'in it." if Trigger2 != "jackin":
                    call E_Jackin                   
            "Stop jack'in it." if Trigger2 == "jackin":
                    $ Trigger2 = 0
            "Ok, that's enough.":
                    ch_e "Alright, [E_Petname]. . . "
                    $ renpy.pop_call()
                    jump Group_Strip_End
                    
        
        return
    


label E_Strip_Ultimatum:  
    if "keepdancing" in E_RecentActions: 
        return
        
                    
    call E_Pos_Reset
    call EmmaFace("bemused", 1)        
    if "stripforced" in E_RecentActions: 
        call EmmaFace("sad", 1)    
        ch_e "I think that's plenty, [E_Petname]."
    else:
        ch_e "I'm afraid that's as far as I'm ready to go, [E_Petname]. . . for now."
    menu:
        extend ""
        "That's ok, you can stop.":    
                if "ultimatum" not in E_DailyActions:                             
                        call Statup("Emma", "Love", 50, 2)
                        call Statup("Emma", "Love", 90, 2)
                        call Statup("Emma", "Inbt", 50, 2)
                        $ E_DailyActions.append("ultimatum")
                $ E_RecentActions.append("stopdancing")
                return
        "That's ok, but keep dancing for a bit. . .":  
                if "ultimatum" not in E_DailyActions:                          
                        call Statup("Emma", "Love", 50, 2)
                        call Statup("Emma", "Obed", 50, 2)
                        call Statup("Emma", "Inbt", 50, 2)
                        $ E_DailyActions.append("ultimatum")
                $ E_RecentActions.append("keepdancing")
                if "stripforced" in E_RecentActions: 
                        ch_e ". . ."
                else:
                        ch_e "Oh, if I must, [E_Petname]."
        "You'd better." if E_Forced:
            if not ApprovalCheck("Emma", 500, "O", TabM=5) and not ApprovalCheck("Emma", 800, "L", TabM=5):                    
                    call EmmaFace("angry")
                    ch_e "I think you're overstepping your bounds here, [E_Petname]."
                    ch_e "Remember your place."  
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")  
                    call Remove_Girl("Emma")
                    return                                
            $ Tempmod += 20
            $ E_Forced += 1
            call EmmaFace("sad")
            if "stripforced" in E_RecentActions:                    
                    call EmmaFace("angry")
                    ch_e ". . ."
            else:
                    ch_e "Hmm, forceful. . ."
                    $ E_RecentActions.append("stripforced")
            call Statup("Emma", "Love", 200, -40)
        "You can do better than that. Keep going." if not E_Forced:
            if not ApprovalCheck("Emma", 300, "O", TabM=5) and not ApprovalCheck("Emma", 700, "L", TabM=5):                   
                    call EmmaFace("angry")
                    ch_e "I think you're overstepping your bounds here, [E_Petname]."
                    ch_e "Remember your place."  
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")  
                    call Remove_Girl("Emma")
                    return                
            call Statup("Emma", "Love", 200, -10)
            call Statup("Emma", "Obed", 50, 3)
            call Statup("Emma", "Obed", 75, 5)
            $ Tempmod += 20
            $ E_Forced += 1
            call EmmaFace("sad")
            ch_e "I can't imagine doing better than \"perfection\". . ."
            
    if "ultimatum" not in E_DailyActions:
            $ E_DailyActions.append("ultimatum")
    show Emma_Sprite at Emma_Dance1()
    "Emma begins to dance again."
    return
                
#label E_Strip_End:   
#    ch_e "Ok, [E_Petname]. . ."
#    $ E_Action -= 1    
#    $ Count = 0
#    $ E_SpriteLoc = StageCenter    
#    call Set_The_Scene
    return

# end Strip Tease ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

transform Emma_Dance1():     
    subpixel True 
    pos (E_SpriteLoc, 50)
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
    
           

# Start Emma Undressing  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label E_Undress(Region = "ask", CountStore=0):  
    $ CountStore = Tempmod    
    if Partner == "Emma":
            $ Tempmod = 0  
    call Shift_Focus("Emma")           
                    
    if Region == "auto":
        if E_Upskirt and E_PantiesDown:
            return
        if E_Legs == "pants" and Tempmod < 20:
            $ Tempmod = 20
        if E_Lust >= 90:
            $ Tempmod += 10      
        elif E_Lust >= 80:
            $ Tempmod += 5  
        $ Situation = "auto"
        call Emma_Bottoms_Off(0)
        $ Situation = 0
    
    if Region == "ask":
        menu:
            "Which parts?"
            "Her top" if E_Over or E_Chest:    
                $ Region = "top"     
            "Her bottoms" if E_Legs or E_Panties or E_Hose:
                $ Region = "bottom"           
            "A little of both. . ." if (E_Over or E_Chest) and (E_Legs or E_Panties or E_Hose): 
                $ Region = "both"    
            "Never mind":
                pass
    
    if Region == "top":
        if E_Over or E_Chest:    
                call Emma_Top_Off(0)  
    elif Region == "bottom":
        if E_Legs or E_Panties or E_Hose:
                call Emma_Bottoms_Off(0)  
    elif Region == "both":        
            if E_Over or E_Chest:    
                    call Emma_Top_Off(0) 
            
            if Partner == "Emma":
                    $ Tempmod = 0
            else:
                    $ Tempmod = CountStore 
            
            if "angry" in E_RecentActions: 
                    pass            
            elif not E_Legs and not E_Panties and not E_Hose:
                    pass                
            elif "no topless" in E_RecentActions:
                    menu:
                        ch_e "Care to push your luck?"
                        "And now the bottoms?":
                            call Emma_Bottoms_Off(0) 
                        "You're probably right, sorry.":
                            pass
            else:
                    ch_p "And now the bottoms?"
                    call Emma_Bottoms_Off(0) 
                    
    
    $ Tempmod = CountStore
    return


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label Emma_Top_Off(Intro = 1, Line = 0, Cnt = 0):                                                    # Will she take her top off? Modifiers
    call Shift_Focus("Emma")
    
    if not E_Over and not E_Chest:                              # If she's already topless. Just skip back.
        $ Tempmod = 0
        return
        
    if "angry" in E_RecentActions:  
        ch_e "I'm in no mood, [E_Petname]."
        return
    
    if E_SeenChest and ApprovalCheck("Emma", 600) and not Taboo:                              #You've seen her tits.
        $ Tempmod += 20
    if "exhibitionist" in E_Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in E_Traits or "sex friend" in E_Petnames and not Taboo:
        $ Tempmod += 10
    elif "ex" in E_Traits:
        $ Tempmod -= 40 
    if "no topless" in E_RecentActions: 
        $ Tempmod -= 10
                     
    if Intro and not E_Uptop:
        if E_Over:
                ch_p "This might be easier without your [E_Over] on."
        elif E_Chest:
                ch_p "This might be easier without your [E_Chest] on."

    $ Approval = ApprovalCheck("Emma", 1200, TabM = 4) # 110, 125, 140, 300 taboo, -20 if already seen
    
    if Situation == "auto" and  (E_Over or E_Chest) and not E_Uptop:   
            $ Line = 0
            if ApprovalCheck("Emma", 1100, TabM = 1) or (E_SeenChest and ApprovalCheck("Emma", 500) and not Taboo):
                    #if she'd go topless
                    call Statup("Emma", "Inbt", 70, 1)
                    $ E_Uptop = 1
                    $ Line = E_Over if E_Over else E_Chest
                    "Emma scowls in irritation, and pulls her [Line] tits out."
                    ch_e "Sometimes only direct contact will do."  
                    if Taboo:
                        call Statup("Emma", "Inbt", 90, (int(Taboo/20)))   
                    call Emma_First_Topless(1)
            elif E_Over and E_Chest and ApprovalCheck("Emma", 600, TabM = 1):
                    #if she won't go topless, but has a bra on. . .
                    call Statup("Emma", "Inbt", 40, 1)
                    $ Line = E_Over
                    $ E_Over = 0
                    "Emma scowls in irritation, and pulls her [Line] off, throwing it aside."
                    ch_e "I just wasn't getting much out of it that way."   
            $ Line = 0
            return     
    
    if Approval >= 2:                                                                               # Does she assume top off?            
        if "no topless" in E_DailyActions:
            ch_e "{i}Fine,{/i} if that will shut you up."
        call EmmaFace("sexy", 1)
        if E_Forced:
            call EmmaFace("sad", 1)
            call Statup("Emma", "Love", 20, -2, 1)
            call Statup("Emma", "Love", 70, -3, 1)
            call Statup("Emma", "Obed", 40, 2)
            call Statup("Emma", "Obed", 90, 1)
            call Statup("Emma", "Inbt", 50, 1)
        call Statup("Emma", "Inbt", 50, 3)  
        $ Cnt = 1
        while (E_Chest or E_Over) and Cnt:
            menu:                                                                                 #Menu All off?
                ch_e "What was it you were interested in, [E_Petname]?"  
                "Lose the gloves." if E_Arms:
                    call EmmaFace("bemused", 1)                    
                    $ E_Arms = 0               
                    "Emma  pulls off her gloves and drops them to the floor."                     
                "Lose the [E_Over]." if E_Over:                 
                    call EmmaFace("bemused", 1)                    
                    $ Line = E_Over
                    $ E_Over = 0
                    "Emma shrugs off her [Line] and it drops to the floor."
                "Just lose the [E_Chest]." if E_Over and E_Chest:
                    call EmmaFace("bemused", 1)                    
                    $ Line = E_Chest
                    $ E_Chest = 0   
                    call Emma_Tits_Up              
                    "Emma unfastens her [Line] from beneath her [E_Over], and allows it to drop to the floor."   
                "Lose the [E_Chest]." if not E_Over and E_Chest:
                    call EmmaFace("bemused", 1)
                    $ Line = E_Chest
                    $ E_Chest = 0      
                    call Emma_Tits_Up           
                    "Emma unfastens her [Line] and allows it to drop to the floor." 
                "Just pull it up." if (E_Over or E_Chest) and not E_Uptop:
                    call EmmaFace("bemused", 1)
                    $ E_Uptop = 1
                    "Emma smiles and pulls out her tits. . ."   
                "Lose both tops." if E_Over and E_Chest:
                    call EmmaFace("bemused", 1)  
                    $ Line = E_Over
                    $ E_Over = 0
                    call Emma_Tits_Up
                    "Emma shrugs off her [Line]-"      
                    $ Line = E_Chest
                    $ E_Chest = 0 
                    call Emma_Tits_Up
                    "-followed quickly by her [Line]."           
                "That's enough. [[exit]":               
                    call EmmaFace("bemused", 1)
                    ch_e "Very well. . ."    
                    $ Cnt = 0
        if (not E_Chest and not E_Over) or E_Uptop:             
            call Statup("Emma", "Obed", 40, 2)
            call Statup("Emma", "Obed", 90, 1)
            call Emma_First_Topless  
        call Statup("Emma", "Lust", 80, 3)        
        $ E_RecentActions.append("ask topless")                      
        $ E_DailyActions.append("ask topless") 
        $ Tempmod = 0        
        return
        
    #Else, Approval < 2, Doesn't want to lose the top//////////////////////////////////  
                 
    call EmmaFace("bemused", 1)   
    if Intro == "massage" and not Approval:
        ch_e "I welcome a massage, but I'm staying fully dressed."
    elif "no topless" in E_RecentActions: 
        call EmmaFace("angry")
        ch_e "Learn from previous mistakes, [E_Petname]."    
    elif Approval and not E_SeenChest:
        ch_e "I don't know if that would be appropriate."    
    elif not E_SeenChest:
        ch_e "I don't think you're ready for that."   
    elif "no topless" in E_DailyActions: 
        ch_e "Are you still that obsessed?"           
    elif "ask topless" in E_RecentActions: 
        ch_e "You want more?"       
    elif Taboo:
        ch_e "[E_Petname], not around prying eyes."          
    elif Approval:
        ch_e "Are you sure you're prepared?"
    else:
        ch_e "No."
        
    menu:
        extend ""
        "Sorry, sorry." if "no topless" in E_RecentActions:  
            call EmmaFace("bemused", 1)   
            ch_e "I can't blame you for your persistance, but learn from your errors."
        "Ok, that's fine." if "no topless" not in E_RecentActions: 
            if "ask topless" not in E_DailyActions:
                call Statup("Emma", "Lust", 80, 3)
                call Statup("Emma", "Love", 70, 1)
                call Statup("Emma", "Love", 90, 1)
                call Statup("Emma", "Inbt", 50, 2)
            if E_Forced:
                $ E_Mouth = "grimace"
                ch_e "How. . . generous of you."
                if "ask topless" not in E_DailyActions:
                    call Statup("Emma", "Love", 20, 2)
                    call Statup("Emma", "Love", 70, 2)
         
        "Lose the gloves." if E_Arms:
            call EmmaFace("bemused", 1)
            $ E_Arms = 0               
            "Emma  pulls off her gloves and drops them to the floor." 
            
        "How about just the [E_Over]?" if E_Over:                                                # asked to go shirtless. 
            if ApprovalCheck("Emma", 1000, TabM = 3) and E_Chest: #80, 160 taboo 
                call EmmaFace("sexy") 
                ch_e "Well, I suppose that would be fine. . ."                 
                call EmmaFace("bemused", 1)                
                $ Line = E_Over
                $ E_Over = 0
                "Emma shrugs off her [Line]."   
                call Statup("Emma", "Obed", 30, 1)
                call Statup("Emma", "Obed", 60, 1)
                call Statup("Emma", "Inbt", 30, 2)
            elif not E_Chest:
                $ E_Eyes = "surprised"
                $ E_Blush = 2
                ch_e "I don't think you're prepared for what's under there." 
                call Statup("Emma", "Inbt", 30, 1)
                menu:
                    extend ""
                    "Ok, you can leave it on.":
                        $ E_Mouth = "smile"
                        call Statup("Emma", "Love", 70, 2)
                        ch_e "Good."             
                    "I think I could handle it.":
                        if ApprovalCheck("Emma", 700, "I", TabM=3) or ApprovalCheck("Emma", 1100, TabM=3):
                            call EmmaFace("bemused", 1)
                            ch_e "Well, I suppose it couldn't hurt to try."                               
                            call Statup("Emma", "Obed", 20, 2)                                                         
                            call Statup("Emma", "Obed", 60, 1)
                            call EmmaFace("sexy")   
                            $ Line = E_Over
                            $ E_Over = 0
                            "Emma shrugs off her [Line]."   
                            call Statup("Emma", "Inbt", 30, 1)  
                            call Statup("Emma", "Inbt", 60, 1)
                            call Emma_First_Topless   
                        else:   
                            call EmmaFace("bemused")
                            call Emma_Top_Off_Refused  
                            
                    "I know, take it off.":
                        call Emma_ToplessorNothing
                $ E_Blush = 1        
            else:   
                call EmmaFace("sexy")
                call Emma_Top_Off_Refused  
                                 
        "Come on, Please? [[take it all off]":                                                                      # asked to go topless. 110, 270 Taboo   
            if Approval and ApprovalCheck("Emma", 600, "L", TabM=1):                 
                call Statup("Emma", "Obed", 40, 2)
                call EmmaFace("sexy")   
                if "no topless" in E_RecentActions:     
                    ch_e "Fine, I can't take your constant begging."
                else:
                    ch_e "Well, I suppose if you ask nicely . . ."                 
                $ E_Uptop = 1
                "Emma just pulls her tits out."
                call Statup("Emma", "Inbt", 30, 1)  
                call Statup("Emma", "Inbt", 60, 1)
                call Emma_First_Topless 
            elif "no topless" in E_RecentActions:
                call EmmaFace("angry")
                ch_e "Again, no."
                call Statup("Emma", "Love", 90, -5)  
                $ E_RecentActions.append("angry")
                $ E_DailyActions.append("angry")   
            else:   
                call EmmaFace("sexy")
                call Emma_Top_Off_Refused
        
        "No, topless or nothing.":                                                              #demanded topless 60, 260 taboo 
            call Emma_ToplessorNothing
                                
        "Never mind.":
            pass
    
    $ E_RecentActions.append("ask topless")                      
    $ E_DailyActions.append("ask topless") 
    $ Tempmod = 0
    return


label Emma_Top_Off_Refused:                    #When you insist but she refuses    
    call EmmaFace("angry")
    if "no topless" in E_RecentActions:  
        ch_e "You should probably back off now."
    elif "no topless" in E_DailyActions:  
        ch_e "I'm tired of this, [E_Petname]."
    call EmmaFace("sad")
    menu:
        ch_e "Is this a dealbreaker for you?"
        "No, never mind." if "no topless" not in E_RecentActions:
            call EmmaFace("sexy")
            call Statup("Emma", "Love", 70, 2)
            ch_e "Good."  
        "Sorry, I'll drop it." if "no topless" in E_RecentActions:   
            ch_e "Good."  
        "Yes, it is.":
            $ E_Brows = "angry"
            ch_e "Very well."
            call Statup("Emma", "Lust", 50, 5)
            call Statup("Emma", "Love", 70, -5, 1)
            if "no topless" not in E_RecentActions:
                call Statup("Emma", "Lust", 70, 5)
                call Statup("Emma", "Obed", 60, 5)    
            $ E_RecentActions.append("angry")
            $ E_DailyActions.append("angry")   
    $ E_RecentActions.append("no topless")                      
    $ E_DailyActions.append("no topless") 
    return
              

label Emma_ToplessorNothing:
    call EmmaFace("angry")
    if ApprovalCheck("Emma", 700, "OI", TabM = 4) and ApprovalCheck("Emma", 400, "O", TabM = 3):       
        #She agrees to your ultimatum 
        call Statup("Emma", "Love", 20, -2, 1)
        call Statup("Emma", "Love", 80, -5, 1)
        call Statup("Emma", "Inbt", 60, 2)
        if "no topless" in E_RecentActions:             
            ch_e "Oh, very well. . ."                 
        else:
            call EmmaFace("sad")
            ch_e "Fine."                
        call Statup("Emma", "Obed", 60, 5)
        call Statup("Emma", "Obed", 90, 2)
        $ E_Uptop = 1
        "Emma grudgingly pulls her tits out of her top."
        if E_Arms:            
            $ E_Arms = 0    
            "She pulls off her gloves and drops them to the floor."
        call Emma_First_Topless                       
    else:                                                                                                
        #she refuses your ultimatum
        call Statup("Emma", "Love", 200, -10)                
        call Statup("Emma", "Obed", 40, -1, 1)
        if "no topless" in E_RecentActions: 
            $E_Brows = "angry"
            ch_e "Learn to take \"no\" for an answer."  
        else: 
            ch_e "I'm afraid not."      
        $ E_RecentActions.append("no topless")                      
        $ E_DailyActions.append("no topless")     
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    return              
    
label Emma_First_Topless(Silent = 0, TempLine = 0):    
    if ChestNum("Emma") > 1 or OverNum("Emma") > 2:
        #if she's wearing substantial clothing. . .
        return     
    if E_Loc != bg_current:
            return   
    $ E_RecentActions.append("topless")                      
    $ E_DailyActions.append("topless")
    call DrainWord("Emma","no topless")      
    call Emma_Tits_Up 
    $ E_SeenChest += 1 
    if E_SeenChest > 1:     
        return                  #ends portion if you've already seen them
    
    
    call Statup("Emma", "Inbt", 70, 15)  
    if not Silent:
        call EmmaFace("sly")
        "You get your first look at Emma's bare chest."
        ch_e "Well, [E_Petname]? Is it everything you dreamed?"    
        $ E_Blush = 1
        menu:
            extend ""
            "Definitely, and more.":            
                call Statup("Emma", "Love", 90, 20)
                call Statup("Emma", "Inbt", 70, 20)               
                call EmmaFace("smile",1)
                ch_e "I do aim to impress."
                call Statup("Emma", "Love", 40, 20)  
                $ E_Blush = 0
            ". . . [[stunned]":            
                call Statup("Emma", "Love", 90, 20)
                call Statup("Emma", "Inbt", 70, 30)
                ch_e "Yes, that would be the usual reaction."
                call Statup("Emma", "Love", 40, 10)  
            "Huh, not what I was expecting. . .":        
                call Statup("Emma", "Love", 90, -30)
                call Statup("Emma", "Obed", 60, 25)
                call Statup("Emma", "Inbt", 70, -15)                          
                call EmmaFace("confused",2)
                ch_e "What?"
                menu:        
                    "They're even better than I imagined!":    
                        call Statup("Emma", "Love", 90, 20)
                        call Statup("Emma", "Obed", 60, -20)
                        call Statup("Emma", "Inbt", 70, 20)                          
                        call EmmaFace("perplexed",1)
                        ch_e "Well, I suppose you managed to salvage that one. . ."
                    "I, um, no, they're great!":                        
                        call EmmaFace("angry",2, Mouth="smile")
                        call Statup("Emma", "Inbt", 70, 10)   
                        ch_e "Of couse they are!"            
                    "Rogue's were tighter, that's all." if R_SeenChest:                            
                        $ TempLine = "Rogue"
                    "Kitty's were tighter, that's all." if K_SeenChest:                            
                        $ TempLine = "Kitty"
                    "Laura's were tighter, that's all." if K_SeenChest:                            
                        $ TempLine = "Laura"
                        
                if TempLine:
                        call EmmaFace("angry")
                        $ E_Mouth = "surprised"                        
                        call Statup("Emma", "Love", 90, -10)
                        call Statup("Emma", "Obed", 80, 30)
                        call Statup("Emma", "Inbt", 70, -25)  
                        ". . ."
                        $ E_Mouth = "sad"
                        if TempLine == "Rogue":
                                if E_LikeRogue >= 800:
                                    call EmmaFace("sly",2,Eyes="side")
                                    call Statup("Emma", "Obed", 80, 5)
                                    ch_e "They are rather . . . ripe. . ."       
                                    $ E_LikeRogue += 20 
                                elif E_LikeRogue >= 700:
                                    $ E_Eyes = "side" 
                                    call Statup("Emma", "Obed", 80, 5)
                                    ch_e "I suppose that's true. . ."    
                                else:                        
                                    $ E_LikeRogue -= 50
                                    $ Templine = "bad"
                                
                        elif TempLine == "Kitty":
                                if E_LikeKitty >= 800:
                                    call EmmaFace("sly",2,Eyes="side")
                                    call Statup("Emma", "Obed", 80, 5)
                                    ch_e "They are rather . . . pert. . ."       
                                    $ E_LikeKitty += 20 
                                elif E_LikeKitty >= 700:
                                    $ E_Eyes = "side" 
                                    call Statup("Emma", "Obed", 80, 5)
                                    ch_e "Well, for a child. . ."    
                                else:                        
                                    $ E_LikeKitty -= 50
                                    $ Templine = "bad"
                                    
                        elif TempLine == "Laura":
                                if E_LikeLaura >= 800:
                                    call EmmaFace("sly",2,Eyes="side")
                                    call Statup("Emma", "Obed", 80, 5)
                                    ch_e "They are rather . . . pert. . ."       
                                    $ E_LikeKitty += 20 
                                elif E_LikeLaura >= 700:
                                    $ E_Eyes = "side" 
                                    call Statup("Emma", "Obed", 80, 5)
                                    ch_e "Well, for a child. . ."    
                                else:                        
                                    $ E_LikeLaura -= 50
                                    $ Templine = "bad"
                        
                        
                        if TempLine == "bad":
                                call Statup("Emma", "Love", 90, -20)
                                ch_e "I think you've seen enough for now, [E_Petname]."   
                                call EmmaOutfit
                                $ E_RecentActions.append("no topless")                      
                                $ E_DailyActions.append("no topless")  
                                $ E_RecentActions.append("angry")
                                $ E_DailyActions.append("angry")  
                        
                    
    else:
        if ApprovalCheck("Emma", 800) and not E_Forced:                #if she's not forced and happy about it
            call Statup("Emma", "Inbt", 70, 15) 
            call Statup("Emma", "Obed", 70, 15)              
            call EmmaFace("smile")
        else:                                                           #if she's not happy about it
            call Statup("Emma", "Love", 90, -40)
            call Statup("Emma", "Inbt", 70, -20)                          
            call EmmaFace("angry")
            call Statup("Emma", "Obed", 70, 40)
    return



# Bottoms ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label Emma_Bottoms_Off(Intro = 1, Line = 0, Cnt = 0):
    call Shift_Focus("Emma")
    
    if not E_Legs and not E_Panties and not E_Hose:                                  
        # If she's already bottomless. Just skip back.     
        $ Tempmod = 0
        return
    
    if "angry" in E_RecentActions:  
        ch_e "I would give up on that."
        return
    
    # Will she take her bottoms off Modifiers
    if E_SeenPussy and ApprovalCheck("Emma", 800): #You've seen her Pussy.
        $ Tempmod += 20
    elif not E_Panties:
        $ Tempmod -= 20
    elif E_SeenPanties and ApprovalCheck("Emma", 600): #You've seen her panties.
        $ Tempmod += 5 
    if Intro == "dildo":
        $ Tempmod += 20
    if "exhibitionist" in E_Traits:
        $ Tempmod += (Taboo * 5)
    if "dating" in E_Traits or "sex friend" in E_Petnames and not Taboo:
        $ Tempmod += 10
    elif "ex" in E_Traits:
        $ Tempmod -= 40 
    if "no bottomless" in E_RecentActions: 
        $ Tempmod -= 20
    
    if Intro:
        if E_Legs and not E_Upskirt:
                ch_p "This might be easier without your [E_Legs] on."
        elif E_Panties and not E_PantiesDown:
                ch_p "This might be easier without your [E_Panties] on."
                
    $ Approval = ApprovalCheck("Emma", 1300, TabM = 5) # 120, 135, 150, -200(320) taboo, -25 if already seen
    
    if Situation == "auto":
            $ Cnt = 0
            
            if not E_Upskirt and not E_PantiesDown:                      
                if E_Legs == "skirt" and not E_Upskirt:                                          
                    #If she's in a skirt with panties, hike it up?
                    if Approval >= 2 or (E_SeenPussy and ApprovalCheck("Emma", 700) and not Taboo):
                        call Statup("Emma", "Inbt", 60, 1)
                        if Taboo:
                            call Statup("Emma", "Inbt", 90, (int(Taboo/20)))                 
                        $ E_Upskirt = 1
                        "She slides her skirt up."
                        $ Cnt = 1 
                        
                if PantsNum("Emma") >= 5 or HoseNum("Emma") >= 6:            
                    if E_Panties:                                               
                        #she has pants and panties on
                        if not Approval or (not E_SeenPanties and Taboo):
                            return   
                    elif Approval < 2 or (not E_SeenPussy and Taboo):
                        return     
                    elif E_Legs == "pants" and E_Upskirt:  
                        return
                    call Statup("Emma", "Inbt", 60, 1)
                    $ E_Upskirt = 1
                    "Emma shrugs, and then tugs her [Line] down." 
                    call Emma_First_Bottomless(1)  
                        
                    if Taboo:
                        call Statup("Emma", "Inbt", 90, (int(Taboo/10)))  
                    $ Cnt = 1 
                
            if E_Panties and not E_PantiesDown:                                              
                # Just wearing panties, lose them?
                if Approval >= 2 or (E_SeenPussy and not Taboo):
                    call Statup("Emma", "Inbt", 70, 2)
                    if Taboo:
                        call Statup("Emma", "Inbt", 90, (int(Taboo/10)))  
                    $ E_PantiesDown = 1
                    if Cnt:
                        "and pulls her [E_Panties] down too."
                    else:
                        "Emma tsks in irritation, and tugs her [E_Panties] down." 
                    call Emma_First_Bottomless(1) 
                        
                    ch_e "That was just in the way."  
            return
            
    
    if Approval >= 2:                 
            #will she volunteer to strip to underwear?///////////////////////////////////////////////////        
            call EmmaFace("sexy", 1)
            if E_Forced:
                call EmmaFace("sad", 1)              
                call Statup("Emma", "Love", 20, -2, 1)
                call Statup("Emma", "Love", 70, -3, 1)
                call Statup("Emma", "Obed", 50, 1)
                call Statup("Emma", "Obed", 90, 1)
                call Statup("Emma", "Inbt", 60, 1)
                $ Line = "Oh, very well."            
            elif Approval >= 3:
                $ Line = "Mmmm, what would you like?"
            else:    
                $ Line = "What would you have me take off?" 
            
            call Emma_Bottoms_Off_Legs
                
            if not E_Panties and Action_Check("Emma", "recent", "bottomless") < 2: 
                call Statup("Emma", "Obed", 50, 2)
                call Statup("Emma", "Obed", 90, 1)
                call Statup("Emma", "Inbt", 50, 3)
                call Statup("Emma", "Lust", 80, 3)
    
  
        
    elif E_Legs or E_Panties or E_Hose:
            # She'd rather not strip but might        
            call EmmaFace("bemused", 1) 
            if "no bottomless" in E_RecentActions: 
                call EmmaFace("angry")
                ch_e "Stop asking, you're embarrassing yourself."   
            elif "no topless" in E_RecentActions: 
                call EmmaFace("angry")
                ch_e "Do you really think that's likely?"  
            elif Approval and not E_SeenPussy:
                ch_e "I don't know if you're ready for that."  
            elif not E_SeenPussy and "ask topless" in E_RecentActions:
                ch_e "Be careful how far you push it. . ."    
            elif not E_SeenPussy:
                ch_e "Maybe when you've earned it."   
            elif "no bottomless" in E_DailyActions: 
                ch_e "Don't you learn anything, [E_Petname]?"             
            elif Taboo:
                ch_e "Not with so many eyes around, [E_Petname]. . ."  
            elif Approval:
                ch_e "Probably not. . ."   
            elif E_SeenPussy:
                ch_e "I think you've seen enough . . ."            
            elif PantsNum("Emma") >= 10:
                ch_e "I'm keeping my pants on."           
            elif E_Legs == "skirt":
                ch_e "I'm keeping my skirt on."   
            elif PantsNum("Emma") >= 5:
                ch_e "I'm keeping my shorts on."  
            else:
                ch_e "I'm keeping my panties on." 
            menu:            
                extend ""
                "Ok, never mind." if "no bottomless" not in E_RecentActions:  
                    if "ask bottomless" not in E_DailyActions:
                        call Statup("Emma", "Lust", 80, 2)
                        call Statup("Emma", "Love", 70, 1)
                        call Statup("Emma", "Love", 90, 1)
                        call Statup("Emma", "Obed", 50, 2)
                        call Statup("Emma", "Inbt", 50, 2)
                    if E_Forced:
                        $ E_Mouth = "smile"
                        ch_e "Very. . . generous."
                        if "ask bottomless" not in E_DailyActions:
                            call Statup("Emma", "Love", 20, 3)
                            call Statup("Emma", "Love", 70, 4)
                            call Statup("Emma", "Inbt", 60, 2)
                        
                "Sorry, sorry." if "no bottomless" in E_RecentActions:  
                    ch_e "Good."
                 
                "Come on, Please?":       
                    if "no bottomless" in E_DailyActions:  
                            call EmmaFace("angry")
                            ch_e "I believe you've heard my answer on that."
                    else:
                            if Approval and ApprovalCheck("Emma", 600, "L", TabM=2):   
                                call EmmaFace("sexy", 1)
                                $ D20 = renpy.random.randint(1, 3)
                                if D20 == 3:
                                    $ Line = "I suppose. . ."
                                    $ Approval += 1
                                else:
                                    $ Line = "Perhaps. . ."                        
                                call Emma_Bottoms_Off_Legs  
                            else:    
                                call EmmaFace("sexy")
                                call Emma_Bottoms_Off_Refused
                                        
                "It doesn't have to be everything. . ." if E_Legs or HoseNum("Emma") >= 10 or E_Panties == "shorts":    
                    if Approval and "no bottomless" not in E_DailyActions:                    
                        call EmmaFace("bemused", 1)
                        $Line = "Well what did you have in mind then?"
                        call Emma_Bottoms_Off_Legs  
                    else:    # She refuses your request. . .
                        call EmmaFace("sexy")
                        call Emma_Bottoms_Off_Refused                                
                "It doesn't have to be everything. . . (locked)" if not E_Legs and HoseNum("Emma") < 10 and E_Panties != "shorts":   
                    pass
                    
                "No, lose 'em.":            #85 and -200 taboo             
                    if (Approval and E_Obed >= 250) or (ApprovalCheck("Emma", 1000, "OI", TabM = 5) and ApprovalCheck("Emma", 500, "O", TabM = 3)):                    
                        call Statup("Emma", "Love", 20, -1, 1)
                        call Statup("Emma", "Love", 70, -5, 1)
                        call Statup("Emma", "Obed", 50, 4)
                        call Statup("Emma", "Obed", 80, 1)
                        call Statup("Emma", "Inbt", 60, 1)
                        $ Line =  "Don't test me. . ."  
                        $ Approval = 1 if Approval < 1 else Approval
                        $ E_Forced = 1
                        call Emma_Bottoms_Off_Legs                     
                    else:          
                        call Statup("Emma", "Love", 200, -10)
                        if ApprovalCheck("Emma", 400, "O"):
                            ch_e "Definitely not." 
                        else:
                            call EmmaFace("angry")
                            ch_e "Out of my sight, [E_Petname]."                          
                            $ E_RecentActions.append("angry")
                            $ E_DailyActions.append("angry")   
                        $ E_RecentActions.append("no bottomless")                      
                        $ E_DailyActions.append("no bottomless")  
            #end approval
    
    $ Tempmod = 0
    $ E_RecentActions.append("ask bottomless")                      
    $ E_DailyActions.append("ask bottomless")     
    return           

label Emma_Bottoms_Off_Legs:    
    
    if E_Forced:        
        call EmmaFace("sad", 1)
    elif ApprovalCheck("Emma", 1100, "OI", TabM = 3):        
        call EmmaFace("sly")
    elif ApprovalCheck("Emma", 1400, TabM = 3):  
        call EmmaFace("sexy", 1) 
    else:
        call EmmaFace("bemused", 1) 
        
    $ Line = "Well what did you want off?" if not Line else Line
    $ Cnt = 1
    while Cnt and (E_Legs or E_Panties or E_Hose):
        menu:                                       # She's asking what you'd like to see.
            ch_e "[Line]"
            "Everything. . ." if Line != "Well what did you have in mind then?": #approval a given
                        
                    if Approval < 2 and not E_Panties and HoseNum("Emma") < 10:
                        call Emma_NoPanties
                    
                    if E_Legs:
                        $ Line = E_Legs      
                        $ E_Legs = 0
                        "Emma pulls her [Line] down."
                        $ E_SeenPanties = 1 if not E_SeenPanties else E_SeenPanties
                                           
                    if Approval < 2 and not E_Panties and HoseNum("Emma") >= 10:
                        call Emma_NoPanties   
                        
                    if E_Boots:
                        $ E_Boots = 0
                        "She pulls her boots off."   
                        
                    if E_Hose:
                        $ Line = E_Hose #HoseName 
                        $ E_Hose = 0
                        "She rolls her hose off."                    
                                            
                    if Approval < 2:
                        call Emma_NoPanties   
                    if E_Panties:                               
                        $ Line = E_Panties   
                        $ E_Panties = 0  
                        "She reaches down and pulls her [Line] off." 
                    call Emma_First_Bottomless   
                    
                    
            "Lose the [E_Legs]." if E_Legs: 
                    if E_Panties and Approval >= 2:
                        call EmmaFace("sexy")
                        ch_e "I can manage that. . ."
                    elif Approval:          
                        call EmmaFace("sexy", 1)    
                        if Approval < 2 and not E_Panties and HoseNum("Emma") < 10:
                            call Emma_NoPanties
                    else:    
                        call EmmaFace("sexy")
                        call Emma_Bottoms_Off_Refused
                        return
                        
                    $ Line = E_Legs      
                    $ E_Legs = 0
                    if not E_Panties and HoseNum("Emma") < 10:
                        call EmmaFace("sly", 1)  
                        "She looks at you slyly before pulling her [Line] off." 
                        call Emma_First_Bottomless 
                    else:
                        "Emma pulls down her [Line]."                        
                        $ E_SeenPanties = 1 if not E_SeenPanties else E_SeenPanties
                    call EmmaFace("bemused", 1)
                        
            "Lose the [E_Panties]." if E_Panties:
                    if Approval < 2:
                        ch_e "I'm afraid not."
                        $ E_RecentActions.append("no bottomless")                      
                        $ E_DailyActions.append("no bottomless")   
                        return                        
                    elif E_Legs == "pants" or HoseNum("Emma") >= 6:
                        ch_e "I suppose that I could. . ."
                    else:
                        ch_e "Of course."                                            
                    $ Line = E_Panties   
                    $ E_Panties = 0  
                             
                    if PantsNum("Emma") >= 5:
                        "She pulls down her [E_Legs], then pulls her [Line] off and puts them back on."    
                    else:
                        "She reaches down and pulls her [Line] off."
                    call Emma_First_Bottomless 
            
            "Lose the [E_Boots]." if E_Boots:
                    ch_e "Of course."   
                    $ E_Boots = 0                      
                    "She reaches down and pulls her boots off."
            
            "Just give me a clear view. . ." if (E_Panties and not E_PantiesDown) or (E_Legs and not E_Upskirt):
                    if Approval >= 2:
                        ch_e "Fine."
                        $ E_PantiesDown = 1 if E_Panties else 0
                        $ E_Upskirt = 1 if E_Legs else 0
                        "She shifts her [E_Legs] out of the way."
                    elif Approval >= 1 and E_Legs and E_Panties and not E_PantiesDown:
                        ch_e "I'll give at least give a little view. . ."
                        $ E_Upskirt = 1
                    else:
                        ch_e "No."
                        $ E_RecentActions.append("no bottomless")                      
                        $ E_DailyActions.append("no bottomless")   
                        return   
                    call Emma_First_Bottomless                     
            
            "Lose the [E_Hose]." if E_Hose:                                    #make sure to update this mess if I add hose to her
                    call EmmaFace("bemused", 1) 
                    if E_Legs:
                        ch_e "All right, fine."                         
                    elif Approval < 2 and not E_Panties and HoseNum("Emma") >= 10:
                        call Emma_NoPanties                            
                    elif not Approval and HoseNum("Emma") >= 6:
                        ch_e "Sorry, no, [E_Petname]."
                        return                            
                    else:
                        ch_e "Fine, [E_Petname]."                 
                        
                    $ Line = E_Hose   
                    $ E_Hose = 0  
                    if E_Legs:
                        "She reaches under her [E_Legs] and pulls her [Line] down."
                    elif HoseNum("Emma") < 10:
                        "Emma pulls her [Line] off." 
                    elif not E_Panties:
                        call EmmaFace("sly", 2)  
                        "She looks at you slyly before removing her [Line]." 
                        $ E_Blush = 1
                        call Emma_First_Bottomless   
                    elif not E_SeenPanties:
                        "Emma slowly removes her [Line]."
                        $ E_SeenPanties = 1
                    else:
                        "Emma pulls her [Line] off." 
                        
            "Keep it all on for now." if Cnt == 1:
                $ E_Mouth = "smile"
                $ Cnt = 0
                
            "Ok, that's enough for now." if Cnt == 2:
                $ Cnt = 0
                
        $ Cnt = 2 if Cnt else Cnt  
        $ Line = "Ok, is that all?"
    return


label Emma_NoPanties: 
    #called when asked to remove pants with nothing on under
    if not R_Panties:
        return
    if E_Legs or HoseNum("Emma") >= 10:
        ch_e "I don't have anything on under this. . ."  
    else:
        ch_e "This is all I have on. . ."  
    menu:
        extend ""
        "Could you do it anyway?":
            if ApprovalCheck("Emma", 1100, "LI", TabM=1):                                             
                ch_e "I suppose. . . "
            else:
                ch_e "I'm afraid not."
                call Emma_Bottoms_Off_Refused
                $ renpy.pop_call()  
        "Don't care, lose'em.":
            if ApprovalCheck("Emma", 800, "OI", TabM=1):
                ch_e "If you insist."  
            else:
                call Emma_Bottoms_Off_Refused
                $ renpy.pop_call()  
                                       
        "Ok, you can leave it on.":
            $ renpy.pop_call()   
    return 
        
label Emma_Bottoms_Off_Refused:     
    if "no bottomless" in E_RecentActions:  
        ch_e "Try to control your impulses."
    elif "no bottomless" in E_DailyActions:  
        ch_e "Not today."
    else:
        call EmmaFace("sad")
        if Cnt == 2:            
            ch_e "That's all I'm willing to do, is that a deal-breaker?"   
        else:
            ch_e "I'm afraid not, is that a deal-breaker?"        
    menu:
        extend ""
        "No, no, never mind." if "no bottomless" not in E_RecentActions:
            $ E_Mouth = "smile"
            call Statup("Emma", "Love", 70, 2)    
            call Statup("Emma", "Obed", 60, 2)  
            ch_e "Excellent."    
        "Sorry, I'll drop it." if "no bottomless" in E_RecentActions:   
            ch_e "Good. . ."  
        "Yeah, let's do something else.":
            $E_Brows = "confused"
            ch_e "Your loss."               
            call Statup("Emma", "Lust", 50, 5)
            call Statup("Emma", "Love", 70, -2, 1)
            if "no bottomless" not in E_RecentActions:  
                call Statup("Emma", "Lust", 70, 5)
                call Statup("Emma", "Obed", 60, 4)      
            $ E_RecentActions.append("angry")
            $ E_DailyActions.append("angry")   
            
    $ E_RecentActions.append("no bottomless")                      
    $ E_DailyActions.append("no bottomless")
    $ Tempmod = 0
    return   

label Emma_First_Bottomless(Silent = 0): 
    if PantiesNum("Emma") > 1 or PantsNum("Emma") > 2 or HoseNum("Emma") > 9:
        #if she's wearing substantial clothing. . .  
        return     
    if E_Loc != bg_current:
            return   
    $ E_RecentActions.append("bottomless")                      
    $ E_DailyActions.append("bottomless")
    call DrainWord("Emma","no bottomless")
    $ E_SeenPussy += 1 
    if E_SeenPussy > 1:     
        return                  #ends portion if you've already seen them        
    
    
    call Statup("Emma", "Inbt", 80, 30)  
    call Statup("Emma", "Obed", 70, 10)   
    if not Silent:
        call EmmaFace("sly")
        "You find yourself staring at [EmmaName]'s bare pussy."        
        menu:        
            extend ""
            "Niiice. . .":            
                call Statup("Emma", "Love", 90, 20)
                call Statup("Emma", "Inbt", 60, 25)            
                call EmmaFace("smile")          
                ch_e "I'm aware. . . "
                call Statup("Emma", "Love", 40, 20)
            "I see you keep it smooth down there." if not E_Pubes:          
                call EmmaFace("confused",1)  
                ch_e "Yes?"
                if ApprovalCheck("Emma", 700, "LO"):    
                    call EmmaFace("bemused")     
                    menu:
                        ch_e "Do you prefer more fuzz?"
                        "Yes":
                            if ApprovalCheck("Emma", 900, "LO"):
                                call Statup("Emma", "Obed", 50, 30)
                                call Statup("Emma", "Inbt", 60, 25)        
                                ch_e "I suppose I could let it go. . ."
                                $ E_Todo.append("pubes")  
                            else:   
                                call EmmaFace("normal")     
                                ch_e "Well that's a pity."
                        "Up to you, I guess.":
                                call Statup("Emma", "Love", 80, 10)
                                ch_e "I'm glad you agree."
                        "No, leave it that way.":  
                                if ApprovalCheck("Emma", 900, "LO"):
                                    call EmmaFace("sly")    
                                    call Statup("Emma", "Love", 80, 10)
                                else:
                                    call EmmaFace("angry",Mouth="normal")    
                                call Statup("Emma", "Inbt", 60, 25) 
                                ch_e "I'm glad I have your. . . permission."
                                $ E_Brows = "normal"
                else:                              
                    call EmmaFace("angry",1)  
                    call Statup("Emma", "Love", 40, -20) 
                    call Statup("Emma", "Obed", 50, 25)
                    call Statup("Emma", "Inbt", 60, -5)         
                    ch_e "Yes, I'm afraid I don't like an unkept garden."
            "Not bad for someone your age.":        
                call Statup("Emma", "Love", 90, -30)
                call Statup("Emma", "Obed", 50, 25)
                call Statup("Emma", "Inbt", 70, -30)
                call EmmaFace("angry",2)           
                if not E_Forced and not ApprovalCheck("Emma", 900, "LO"):                    
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")  
                        call Statup("Emma", "Obed", 70, 25)
                ch_e "You will regret that remark. . ."
    else:
        
        if ApprovalCheck("Emma", 800) and not E_Forced:
            call Statup("Emma", "Love", 90, 20)
            call Statup("Emma", "Inbt", 60, 25)          
            call EmmaFace("smile")          
            call Statup("Emma", "Love", 40, 20)
            call Statup("Emma", "Obed", 70, 10)
        else:        
            call Statup("Emma", "Love", 90, -40)
            call Statup("Emma", "Inbt", 70, -20)
            call EmmaFace("angry")          
            call Statup("Emma", "Obed", 70, 30)
    return
    
# End Emma Undressing  ///////////////////////////////////////////////////////////////////

    

label Emma_First_Peen(Silent = 0, Undress = 0, Second = 0, React = 0): 
    #checked each time she sees your cock  ## call Emma_First_Peen(0,1)
    #if Silent it doesn't say anything
    #if Undress then you get nude
    #if Secondary then this is the second girl to see it.
    # React 0 if other girl didn't comment, 
    # 1 = if the other girl commented, 2 = didn't like it
    
    if E_Loc != bg_current:
                if Partner == "Emma":
                        $ Partner = 0
                return  
    if "cockout" in P_RecentActions and "peen" in E_RecentActions: 
                #If the cock is already out and she's seen it, return
                return
            
    $ E_RecentActions.append("peen")                      
    $ E_DailyActions.append("peen")
    $ E_SeenPeen += 1                      
    call Statup("Emma", "Inbt", 30, 2) 
    call Statup("Emma", "Inbt", 80, 1)
    
    if Second:
        #If another girl commented on it first. . .
        if E_SeenPeen == 1: 
                call EmmaFace("smirk", 2, Eyes = "down")  
                ch_e "My, that certainly is an impressive specimen. . ."
                call EmmaFace("bemused", 1)  
        elif Second == 1:
                # The other girl liked it
                if not ApprovalCheck("Emma", 800) and not ApprovalCheck("Emma", 500, "I"):
                    call EmmaFace("sad", 1) 
                    ch_e "I suppose you haven't had a lot of experience. . ."
                else:
                    call EmmaFace("bemused", 1)  
                    ch_e "Yes, it caught me off guard as well. . ."
        elif Second == 2:
                # The other girl didn't like it
                if not ApprovalCheck("Emma", 800) and not ApprovalCheck("Emma", 500, "I"):
                    call EmmaFace("sad", 1)  
                    ch_e "A fine judge of quality. . ."
                else:
                    call EmmaFace("confused", 1)  
                    ch_e "You just don't appreciate the finer things. . ."
                    call EmmaFace("sly",0)  
        $ Silent = 1
        
    if Undress:
        $ P_RecentActions.append("naked")    
    if not Silent:        
        if "cockout" in P_RecentActions:
                call EmmaFace("down", 2)  
                "Emma glances down at your exposed cock"
        elif React:
                #If called by a sex dialog
                "Emma unzips your pants and draws out your cock."
        elif Undress:
                "You strip nude."
        else:
                "You whip your cock out."
        if "cockout" not in P_RecentActions:
                $ P_RecentActions.append("cockout")
        if bg_current != "bg showerroom" and not ApprovalCheck("Emma", 800) and not ApprovalCheck("Emma", 400, "I"):
                if "detention" in E_RecentActions or "classcaught" in E_RecentActions:                    
                    call EmmaFace("confused", Eyes="down")  
                    ch_e "Mmm?"                    
                    call EmmaFace("surprised", Eyes="squint") 
                    if E_SeenPeen == 1: 
                        call Statup("Emma", "Love", 30, 10) 
                        call Statup("Emma", "Love", 90, 5)                
                        call Statup("Emma", "Obed", 50, 20)
                        call Statup("Emma", "Inbt", 60, 30)
                    else:                         
                        call Statup("Emma", "Love", 90, 2)                
                        call Statup("Emma", "Obed", 50, 3)
                        call Statup("Emma", "Inbt", 60, 5) 
                    ch_e "Well I suppose I can make an exception in this case."
                    $ React = 1 
                else:
                    call EmmaFace("surprised", Eyes="down")  
                    ch_e "Mmm?"
                    call EmmaFace("angry", 1)  
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")  
                    if E_SeenPeen == 1: 
                        call Statup("Emma", "Love", 90, -10)                
                        call Statup("Emma", "Obed", 50, 35)
                        call Statup("Emma", "Inbt", 60, 20)
                    else:                    
                        ch_e "[E_Petname]! We are going to have to work through this. . . problem of yours."
                        if Action_Check("Emma", "daily", "peen") >= 2:
                                #if she's seen more than one peen today         
                                call Statup("Emma", "Love", 90, -1)     
                                call Statup("Emma", "Obed", 50, 2)
                                call Statup("Emma", "Inbt", 60, 2)
                        else:
                                call Statup("Emma", "Love", 90, -5)                
                                call Statup("Emma", "Obed", 50, 12)
                                call Statup("Emma", "Inbt", 60, 10)  
                    $ React = 2                           
        elif Taboo > 20 and (not ApprovalCheck("Emma", 1500) or E_SEXP < 10) and bg_current != "bg showerroom":
                call EmmaFace("surprised", 2)  
                ch_e "You really should be careful where you display that thing." 
                $ React = 2
                if E_SeenPeen == 1: 
                    call EmmaFace("bemused", 1, Eyes="down")  
                    ch_e ". . . impressive though it may be. . ." 
                    $ React = 1
                    call Statup("Emma", "Love", 30, 15) 
                    call Statup("Emma", "Love", 90, 15)                
                    call Statup("Emma", "Obed", 50, 25)
                    call Statup("Emma", "Inbt", 60, 35)  
                call EmmaFace("bemused",0)   
        elif E_SeenPeen > 10:
                return 0   
        elif ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "L"):
                call EmmaFace("sly",1) 
                if E_SeenPeen == 1: 
                    call EmmaFace("surprised",1, Eyes="down")  
                    ch_e "Well that's certainly an interesting specimen."
                    call EmmaFace("bemused",1)  
                    call Statup("Emma", "Love", 50, 5)
                    call Statup("Emma", "Love", 90, 10) 
                elif E_SeenPeen == 2:  
                    $ E_Eyes = "down"
                    ch_e "Oh, hello again."               
                    call Statup("Emma", "Inbt", 60, 5) 
                elif E_SeenPeen == 5: 
                    ch_e "Yes, we've seen that before." 
                    call Statup("Emma", "Obed", 50, 7) 
                elif E_SeenPeen == 10:  
                    $ E_Eyes = "down"
                    ch_e "I do appreciate some of your features."
                    call Statup("Emma", "Obed", 80, 5)
                    call Statup("Emma", "Inbt", 60, 10)  
                $ E_Eyes = "squint" 
                $ React = 1
        else:
                call EmmaFace("sad",1) 
                if E_SeenPeen == 1: 
                    call EmmaFace("perplexed",1 ) 
                    ch_e "Are you aware that your dick is out?"
                    call Statup("Emma", "Obed", 50, 7)
                    call Statup("Emma", "Inbt", 60, 3)  
                elif E_SeenPeen < 5: 
                    call EmmaFace("sad",0) 
                    ch_e "You might want to put that away, [E_Petname]."
                    call Statup("Emma", "Inbt", 60, 2)  
                elif E_SeenPeen == 10: 
                    ch_e "Yes, we've all seen that before."               
                    call Statup("Emma", "Obed", 50, 7)
                    call Statup("Emma", "Inbt", 60, 5)   
                $ React = 2
    
    else: #Silent mode
                $ P_RecentActions.append("cockout") 
                if E_SeenPeen > 10:
                    return 0
                elif ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "L"):
                        if E_SeenPeen == 1: 
                            call Statup("Emma", "Love", 90, 3) 
                        elif E_SeenPeen == 2:      
                            call Statup("Emma", "Inbt", 60, 5) 
                        elif E_SeenPeen == 5:          
                            call Statup("Emma", "Obed", 50, 7) 
                        elif E_SeenPeen == 10: 
                            call Statup("Emma", "Love", 90, 10)  
                else:
                        if E_SeenPeen == 1: 
                            call Statup("Emma", "Obed", 50, 7)
                            call Statup("Emma", "Inbt", 60, 3)  
                        elif E_SeenPeen < 5: 
                            call Statup("Emma", "Inbt", 60, 2)  
                        elif E_SeenPeen == 10:              
                            call Statup("Emma", "Obed", 50, 7)
                            call Statup("Emma", "Inbt", 60, 3) 
                            
    if E_SeenPeen == 1 and "angry" not in E_RecentActions:         
        call Statup("Emma", "Love", 50, 10)          
        call Statup("Emma", "Love", 90, 10)                
        call Statup("Emma", "Obed", 90, 20)
        call Statup("Emma", "Inbt", 60, 20) 
        call Statup("Emma", "Lust", 80, 10)
    
    return React
    # End Emma shown peen
    
    