﻿# start Strip Tease /////////////////////////////////////////////////////////////////////////////
#label K_Strip(Tempmod = Tempmod):    
#    call Shift_Focus("Kitty")
#    $ Round -= 5 if Round > 5 else (Round-1)
#    $ K_SpriteLoc = StageCenter 
#    call Set_The_Scene
#    $ Kitty_Arms = 1
#    call KittyFace("sexy")
       
#    if "stripping" in K_DailyActions:
#        call KittyFace("sexy", 1)
#        $ Line = renpy.random.choice(["You liked the show earlier?",       
#            "Didn't get enough earlier?",
#            "You're going to wear me out."]) 
#        ch_k "[Line]" 
#    if not ApprovalCheck("Kitty", 600, TabM = 3):
#        if not ApprovalCheck("Kitty", 400):
#            ch_k "Like I would just dance for you?"
#        elif Taboo:
#            ch_k "I don't know, this really isn't a good place for it?"            
#        else:
#            ch_k "I don't know, I don't really feel like dancing right now."
#        return
    
    
#    call AllReset("Kitty")
#    show Kitty_Sprite at Kitty_Dance1()
#    "She starts to dance."  
    
#    if K_SeenChest or K_SeenPussy:              #You've seen her tits.
#        $ Tempmod += 20
#    if K_SeenPanties:                           #You've seen her panties.
#        $ Tempmod += 5
#    if "exhibitionist" in K_Traits:
#        $ Tempmod += (4*Taboo)
#    if ("dating" in K_Traits or "sex friend" in K_Petnames) and not Taboo:
#        $ Tempmod += 15
#    elif "ex" in K_Traits:
#        $ Tempmod -= 40 
#    elif K_ForcedCount and not K_Forced:
#        $ Tempmod -= 5 * K_ForcedCount
#    $ Trigger = "strip"
#    $ K_RecentActions.append("stripping")                      
#    $ K_DailyActions.append("stripping") 
#    $ K_Strip += 1
#    $ Count = 1
    
#label K_Stripping: 
    
#    while Round >=0:  
#        if Round <= 10:
#            ch_k "It's getting late, we should stop for now."
#            $ Count = 0
#            $ K_Action -= 1    
#            $ K_SpriteLoc = StageRight 
#            return
        
#        $ Round -= 2 if Round > 2 else Round
        
#        call KittyLust(1) #sets her lusty face    
#        if Count != 2:             
#            if K_Over and K_Chest and (K_Panties or K_Legs or HoseNum("Kitty") >= 10):          
#                #will she lose the overshirt when she's dressed under?
#                if ApprovalCheck("Kitty", 750, TabM = 3):
#                    call Statup("Kitty", "Obed", 50, 1)
#                    call Statup("Kitty", "Inbt", 25, 1)                 
#                    call Statup("Player", "Focus", 60, 3)
#                    $ Line = K_Over                
#                    $ K_Over = 0                     
#                    "She drops her shoulders and her [Line] falls to the floor."  
#                else:
#                    jump K_Strip_Ultimatum
            
#            elif K_Legs and (K_Panties or HoseNum("Kitty") >= 10):                              
#                #will she lose the pants/skirt if she has panties on?
#                if ApprovalCheck("Kitty", 1200, TabM = 3) or (K_SeenPanties and not Taboo):
#                    call Statup("Kitty", "Lust", 50, 5)                
#                    call Statup("Kitty", "Obed", 50, 1)
#                    call Statup("Kitty", "Inbt", 30, 1)                
#                    call Statup("Player", "Focus", 60, 5)
#                    $ Line = K_Legs         
#                    $ K_Legs = 0      
#                    "Her [Line] slide through her legs until they're only on her toes, before she kicks them to the floor."   
#                    if not K_SeenPanties:
#                        call Statup("Kitty", "Obed", 50, 2)                              
#                        call Statup("Kitty", "Obed", 200, 3)
#                        call Statup("Kitty", "Inbt", 50, 3)
#                        call Statup("Kitty", "Inbt", 200, 2)
#                        $ K_SeenPanties = 1                
#                else:
#                    jump K_Strip_Ultimatum          
                    
#            elif K_Hose: 
#                # Will she lose the hose?
#                if HoseNum("Kitty") >= 10:
#                    if ApprovalCheck("Kitty", 1200, TabM = 3):
#                        call Statup("Kitty", "Lust", 50, 6)
#                        call Statup("Player", "Focus", 60, 6)
#                    else:    
#                        jump K_Strip_Ultimatum
                        
#                elif HoseNum("Kitty") >= 6 and ApprovalCheck("Kitty", 1200, TabM = 3):
#                    if ApprovalCheck("Kitty", 1200, TabM = 3):
#                        call Statup("Kitty", "Lust", 50, 4)
#                        call Statup("Player", "Focus", 60, 4)
#                    else:    
#                        jump K_Strip_Ultimatum
#                else:
#                    call Statup("Kitty", "Lust", 50, 3)
#                    call Statup("Player", "Focus", 60, 3)
#                $ Line = K_Hose
#                $ K_Hose = 0
#                "Her [Line] slide down off her legs, leaving them in a small pile."     
                
#            elif K_Over and not K_Chest and (K_Panties or HoseNum("Kitty") >= 10):      
#                #will she lose the top when she's topless with panties?        
#                if ApprovalCheck("Kitty", 1250, TabM = 3) or (K_SeenChest and not Taboo):
#                    call Statup("Kitty", "Lust", 60, 5)                
#                    call Statup("Kitty", "Obed", 50, 2)
#                    call Statup("Kitty", "Inbt", 50, 10)   
#                    call Statup("Player", "Focus", 80, 15)    
#                    $ Line = K_Over
#                    $ K_Over = 0                          
#                    if not K_SeenChest:
#                        call KittyFace("bemused", 1)
#                        call Statup("Kitty", "Obed", 50, 3)                              
#                        call Statup("Kitty", "Obed", 200, 4)
#                        call Statup("Kitty", "Inbt", 50, 3)
#                        call Statup("Kitty", "Inbt", 200, 3)  
#                        "She hesitantly glances your way, and then with tug her [Line] passes through her, tossing it to the ground."   
#                        call Kitty_First_Topless(1)        
#                    else: 
#                        "She pulls her [Line] over her head, tossing it to the ground."      
#                else:
#                    jump K_Strip_Ultimatum
                
#            elif K_Chest and not K_Over:                                     
#                # Will she lose the bra?
#                if ApprovalCheck("Kitty", 1250, TabM = 3) or (K_SeenChest and not Taboo):
#                    call Statup("Kitty", "Lust", 60, 5)                
#                    call Statup("Kitty", "Obed", 50, 2)
#                    call Statup("Kitty", "Inbt", 50, 1)
#                    call Statup("Player", "Focus", 80, 15)      
#                    $ Line = K_Chest
#                    $ K_Chest = 0                        
#                    if not K_SeenChest:
#                        call KittyFace("bemused", 1)
#                        call Statup("Kitty", "Obed", 50, 3)                              
#                        call Statup("Kitty", "Obed", 200, 4)
#                        call Statup("Kitty", "Inbt", 50, 3)
#                        call Statup("Kitty", "Inbt", 200, 3)   
#                        "She hesitantly glances your way, and then with a shrug pulls her [Line] through herself, tossing it to the ground."
#                        call Kitty_First_Topless(1)
#                    else:
#                        call KittyFace("sexy")
#                        "She tugs her [Line] off, tossing it to the ground." 
#                else:
#                    jump K_Strip_Ultimatum
            
#            elif K_Legs:                                                        
#                #will she lose the pants/skirt if she has no panties on?
#                if ApprovalCheck("Kitty", 1350, TabM = 3) or (K_SeenPussy and not Taboo):
#                    call Statup("Kitty", "Lust", 75, 10)  
#                    $ Line = K_Legs
#                    $ K_Legs = 0
#                    if not K_SeenPussy:
#                        call Statup("Kitty", "Obed", 60, 3)
#                        call Statup("Kitty", "Obed", 200, 5)
#                        call Statup("Kitty", "Inbt", 50, 4)
#                        call Statup("Kitty", "Inbt", 200, 4)  
#                        "She shyly looks up at you, and then slowly lets her [Line] slide to the floor." 
#                        call Kitty_First_Bottomless(1)  
#                    else:                            
#                        call Statup("Kitty", "Obed", 50, 1)                              
#                        call Statup("Kitty", "Obed", 75, 1)
#                        "She lets her [Line] pass through her legs, dropping them to the floor."   
#                        call Statup("Kitty", "Inbt", 70, 2)    
#                    call Statup("Player", "Focus", 85, 15)
#                else:
#                    jump K_Strip_Ultimatum
                
#            elif K_Over and not K_Panties:                                         
#                #will she lose the overshirt when she's bottomless under?
#                if ApprovalCheck("Kitty", 1350, TabM = 3) or (K_SeenPussy and not Taboo):      
#                    $ Line = K_Over
#                    $ K_Over = 0         
#                    if not K_SeenPussy:                
#                            call Statup("Kitty", "Obed", 60, 3)                              
#                            call Statup("Kitty", "Obed", 200, 5)
#                            call Statup("Kitty", "Inbt", 50, 4)
#                            call Statup("Kitty", "Inbt", 200, 4) 
#                            "She hesitantly glances your way, and then with a tug pulls her [Line] through herself, tossing it to the ground."
#                            call Kitty_First_Bottomless(1)                
#                    else:
#                            "She pulls her [Line] off, tossing it to the ground."     
#                    if not K_Chest:
#                            if not K_SeenChest:                
#                                call Statup("Kitty", "Obed", 50, 3)  
#                                call Statup("Kitty", "Inbt", 50, 3)
#                                call Kitty_First_Topless(1)
#                            else:
#                                call Statup("Kitty", "Lust", 60, 15)                
#                                call Statup("Kitty", "Obed", 50, 3)                              
#                                call Statup("Kitty", "Obed", 75, 1)
#                                call Statup("Kitty", "Inbt", 50, 3)
#                    else:
#                                call Statup("Kitty", "Lust", 75, 10)                
#                                call Statup("Kitty", "Obed", 50, 1)                              
#                                call Statup("Kitty", "Obed", 75, 1)
#                                call Statup("Kitty", "Inbt", 70, 2)                
#                    call Statup("Player", "Focus", 85, 15)    
#                else:
#                    jump K_Strip_Ultimatum
            
#            elif K_Chest:                                                               
#                # Will she go topless?
#                if ApprovalCheck("Kitty", 1250, TabM = 3) or (K_SeenChest and not Taboo):
#                    call Statup("Kitty", "Lust", 60, 5)  
#                    $ Line = K_Chest
#                    $ K_Chest = 0         
#                    if not K_SeenChest:
#                        call Statup("Kitty", "Obed", 50, 3)                              
#                        call Statup("Kitty", "Obed", 200, 4)               
#                        call Statup("Kitty", "Inbt", 50, 3)
#                        call Statup("Kitty", "Inbt", 200, 3)  
#                        "She hesitantly glances your way, and then with a tug pulls her [Line] through herself, tossing it to the ground." 
#                        call Kitty_First_Topless(1)
#                    else:                
#                        call Statup("Kitty", "Obed", 50, 2)
#                        "She pulls her [Line] off, tossing it to the ground."  
#                        call Statup("Kitty", "Inbt", 50, 1)
#                    call Statup("Player", "Focus", 80, 15)   
#                else:
#                    jump K_Strip_Ultimatum
                
#            elif K_Panties:                                                                        
#                # Will she go bottomless?
#                if ApprovalCheck("Kitty", 1350, TabM = 3) or (K_SeenPussy and not Taboo):
#                    call Statup("Kitty", "Lust", 75, 10) 
#                    $ Line = K_Panties
#                    $ K_Panties = 0         
#                    if not K_SeenPussy:
#                        call Statup("Kitty", "Obed", 60, 3)                              
#                        call Statup("Kitty", "Obed", 200, 5)
#                        call Statup("Kitty", "Inbt", 50, 4)
#                        call Statup("Kitty", "Inbt", 200, 4) 
#                        "She shyly looks up at you, and then slowly tugs her [Line] off, flinging them to the side." 
#                        call Kitty_First_Bottomless(1) 
#                    else:                
#                        call Statup("Kitty", "Obed", 50, 1)                              
#                        call Statup("Kitty", "Obed", 75, 1)
#                        "She  looks up at you, and then gently pulls her [Line] off, flicking them to the side."                  
#                        call Statup("Kitty", "Inbt", 70, 2)   
#                    call Statup("Player", "Focus", 85, 15)
#                else:
#                    jump K_Strip_Ultimatum
                
#            else:    
#                call KittyFace("sexy")
#                ch_k "It looks like I've run out of clothes. . ."
#                $ Count = 2
        
#        call Statup("Kitty", "Lust", 70, 2)               #lust/Focus
#        if "exhibitionist" in K_Traits:
#            call Statup("Kitty", "Lust", 200, 2)
#        call Statup("Player", "Focus", 60, 3)
#        if Trigger2 == "jackin":
#            call Statup("Kitty", "Lust", 200, 2)
#            call Statup("Player", "Focus", 200, 5)
        
#        if not P_Semen and P_Focus >= 50:
#            $ P_Focus = 50
    
#        if P_Focus >= 100 or K_Lust >= 100:                                     #If either of you could cum 
            
#            if P_Focus >= 100:                                                  #You cum             
#                call PK_Cumming
#                if "angry" in K_RecentActions:  
#                    return    
#                call Statup("Kitty", "Lust", 200, 5) 
#                if not P_Semen and Trigger2 == "jackin":
#                    "You're spitting dust here, maybe just watch quietly for a while."
#                    $ Trigger2 = 0
            
#                if P_Focus > 80:
#                    jump K_Strip_End   
            
#            if K_Lust >= 100:                                                   #and Kitty cums                    
#                call K_Cumming
#                if Situation == "shift" or "angry" in K_RecentActions:                    
#                    $ Count = 0
#                    jump K_Strip_End 
#            call AllReset("Kitty")
#            show Kitty_Sprite at Kitty_Dance1()
#            "Kitty begins to dance again."
        
#        menu:
#            extend ""
#            "Keep Going. . . (locked)" if Count == 2 or "keepdancing" in K_RecentActions:
#                pass
#            "Keep Going. . ." if Count != 2 and "keepdancing" not in K_RecentActions:
#                $ K_Eyes = "sexy"
#                if K_Love >= 700 or K_Obed >= 500:
#                    if not Tempmod:
#                        $ Tempmod = 10
#                    elif Count == 1 and Tempmod <= 20:
#                        $ Tempmod += 1
#                if Taboo and K_Strip <= 10:
#                    call Statup("Kitty", "Obed", 50, 7)
#                elif Taboo or K_Strip <= 10:
#                    call Statup("Kitty", "Obed", 50, 5)
#                elif K_Strip <= 50:
#                    call Statup("Kitty", "Obed", 50, 3) 
#            "Keep Dancing. . ." if Count == 2:
#                $ K_Eyes = "sexy"              
#            "Just watch silently" if Count != 2:
#                if "watching" not in K_RecentActions:
#                    if Count != 2:
#                        if Taboo and K_Strip <= 10:
#                            call Statup("Kitty", "Inbt", 50, 3) 
#                        elif Taboo or K_Strip <= 10:
#                            call Statup("Kitty", "Inbt", 50, 1) 
#                    elif K_Strip <= 50:
#                            call Statup("Kitty", "Inbt", 50, 2)
#                            call Statup("Kitty", "Lust", 70, 2) 
#                    $ K_RecentActions.append("watching")  
            
#            "Start jack'in it." if Trigger2 != "jackin": #add Kitty reaction here.
#                call K_Jackin                   
#            "Stop jack'in it." if Trigger2 == "jackin":
#                $ Trigger2 = 0
#            "Ok, that's enough.":
#                jump K_Strip_End
                
    
#    jump K_Stripping
    


#label K_Strip_Ultimatum:  
#    if "keepdancing" in K_RecentActions: 
#        jump K_Stripping
        
#    call Set_The_Scene
#    call KittyFace("bemused", 1)        
#    if "stripforced" in K_RecentActions: 
#        call KittyFace("sad", 1)    
#        ch_k "That's all you get."
#    else:
#        ch_k "I don't know, [K_Petname], that's as far as I'll go for now."
#    menu:
#        extend ""
#        "That's ok, you can stop.":                            
#            call Statup("Kitty", "Love", 50, 2)
#            call Statup("Kitty", "Love", 90, 2)
#            call Statup("Kitty", "Inbt", 50, 2)
#        "That's ok, but keep dancing for a bit. . .":                            
#            call Statup("Kitty", "Love", 50, 2)
#            call Statup("Kitty", "Obed", 50, 2)
#            call Statup("Kitty", "Inbt", 50, 2)
#            $ K_RecentActions.append("keepdancing")
#            call K_Pos_Reset        
#            show Kitty_Sprite at Kitty_Dance1()
#            "Kitty begins to dance again."
#            ch_k "Heh, alright."
#            jump K_Stripping
#        "You'd better." if K_Forced:
#            if not ApprovalCheck("Kitty", 500, "O", TabM=5) and not ApprovalCheck("Kitty", 800, "L", TabM=5):                    
#                call KittyFace("angry")
#                ch_k "I'm not just going to do \"whatever\"!"
#                ch_k "I'm done with this."  
#                $ K_RecentActions.append("angry")
#                $ K_DailyActions.append("angry")  
#                $ K_Action -= 1    
#                $ K_SpriteLoc = StageRight 
#                return                                
#            $ Tempmod += 25
#            $ K_Forced = 1
#            call KittyFace("sad")
#            if "stripforced" in K_RecentActions:                    
#                call KittyFace("angry")
#                ch_k ". . ."
#                call Statup("Kitty", "Love", 200, -40)
#            else:
#                ch_k "I. . . could show a bit more. . ."
#                call Statup("Kitty", "Love", 200, -40)
#                $ K_RecentActions.append("stripforced")
#            call K_Pos_Reset        
#            show Kitty_Sprite at Kitty_Dance1()
#            "Kitty begins to dance again."
#            jump K_Stripping
#        "You can do better than that. Keep going." if not K_Forced:
#            if not ApprovalCheck("Kitty", 300, "O", TabM=5) and not ApprovalCheck("Kitty", 700, "L", TabM=5):                   
#                call KittyFace("angry")
#                ch_k "I'm not just going to do \"whatever\"!"
#                ch_k "I'm done with this."  
#                $ K_RecentActions.append("angry")
#                $ K_DailyActions.append("angry")  
#                $ K_Action -= 1    
#                $ K_SpriteLoc = StageRight 
#                return                
#            call Statup("Kitty", "Love", 200, -10)
#            call Statup("Kitty", "Obed", 50, 3)
#            call Statup("Kitty", "Obed", 75, 5)
#            $ Tempmod += 25
#            $ K_Forced = 1
#            call KittyFace("sad")
#            ch_k "I mean, maybe. . ."
#            call K_Pos_Reset        
#            show Kitty_Sprite at Kitty_Dance1()
#            "Kitty begins to dance again."
#            jump K_Stripping
                
#label K_Strip_End:   
#    ch_k "Ok. . . "
#    $ K_Action -= 1    
#    $ Count = 0
#    $ K_SpriteLoc = StageRight 
#    return

# end Strip Tease ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


label K_Strip_Ultimatum:  
    if "keepdancing" in K_RecentActions: 
        return
        
    call K_Pos_Reset        
    call KittyFace("bemused", 1)        
    if "stripforced" in K_RecentActions: 
        call KittyFace("sad", 1)    
        ch_k "That's all you get."
    else:
        ch_k "I don't know, [K_Petname], that's as far as I'll go for now."
        
    menu:
        extend ""
        "That's ok, you can stop.":  
                if "ultimatum" in K_DailyActions:                          
                        call Statup("Kitty", "Love", 50, 2)
                        call Statup("Kitty", "Love", 90, 2)
                        call Statup("Kitty", "Inbt", 50, 2)
                        $ K_DailyActions.append("ultimatum")
                $ K_RecentActions.append("stopdancing")
#                $ Adjacent.remove("Kitty")
                return
        "That's ok, but keep dancing for a bit. . .":     
                if "ultimatum" not in K_DailyActions:                    
                        call Statup("Kitty", "Love", 50, 2)
                        call Statup("Kitty", "Obed", 50, 2)
                        call Statup("Kitty", "Inbt", 50, 2)
                        $ K_DailyActions.append("ultimatum")
                $ K_RecentActions.append("keepdancing")
                if "stripforced" in K_RecentActions: 
                        ch_k ". . ."
                else:
                        ch_k "Heh, alright."
        "You'd better." if K_Forced:
                if not ApprovalCheck("Kitty", 500, "O", TabM=5) and not ApprovalCheck("Kitty", 800, "L", TabM=5):                    
                        call KittyFace("angry")
                        ch_k "I'm not just going to do \"whatever\"!"
                        ch_k "I'm done with this."  
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")  
                        call Remove_Girl("Kitty")
                        return                                
                $ Tempmod += 20
                $ K_Forced += 1
                call KittyFace("sad")
                if "stripforced" in K_RecentActions:                    
                        call KittyFace("angry")
                        ch_k ". . ."
                else:
                        ch_k "I. . . could show a bit more. . ."
                        $ K_RecentActions.append("stripforced")
                call Statup("Kitty", "Love", 200, -40)
        "You can do better than that. Keep going." if not K_Forced:
                if not ApprovalCheck("Kitty", 300, "O", TabM=5) and not ApprovalCheck("Kitty", 700, "L", TabM=5):                   
                        call KittyFace("angry")
                        ch_k "I'm not just going to do \"whatever\"!"
                        ch_k "I'm done with this."  
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")  
                        call Remove_Girl("Kitty")
                        return                
                call Statup("Kitty", "Love", 200, -10)
                call Statup("Kitty", "Obed", 50, 3)
                call Statup("Kitty", "Obed", 75, 5)
                $ Tempmod += 20
                $ K_Forced += 1
                call KittyFace("sad")
                ch_k "I mean, maybe. . ."
    if "ultimatum" not in K_DailyActions:
            $ K_DailyActions.append("ultimatum")
    show Kitty_Sprite at Kitty_Dance1()
    "Kitty begins to dance again."
    return
                 
    
label K_Stripping:   
        #This gets called by Group_Stripping, and returns there at the end. 
        if "stopdancing" in K_RecentActions: 
            #if she's just standing around, cut back to the other girl            
            if "stopdancing" in R_RecentActions: 
                    $ renpy.pop_call()
                    jump Group_Strip_End             
            if "stopdancing" in E_RecentActions: 
                    $ renpy.pop_call()
                    jump Group_Strip_End                  
            if "stopdancing" in L_RecentActions: 
                    $ renpy.pop_call()
                    jump Group_Strip_End                     
            return        
#        if "keepdancing" in K_RecentActions and len(Adjacent) >= 2: 
#            return
        
        $ Kitty_Arms = 1
        call KittyLust(1) #sets her lusty face          
        if "keepdancing" not in K_RecentActions:  
                # if Count isn't 2, it loops. 
                if K_Over and K_Chest and (K_Panties or K_Legs or HoseNum("Kitty") >= 10):          
                    #will she lose the overshirt when she's dressed under?
                    if ApprovalCheck("Kitty", 750, TabM = 3):
                            call Statup("Kitty", "Obed", 50, 1)
                            call Statup("Kitty", "Inbt", 25, 1)                 
                            call Statup("Player", "Focus", 60, 3)
                            $ Line = K_Over                
                            $ K_Over = 0                     
                            "She drops her shoulders and her [Line] falls to the floor."  
                    else:
                            jump K_Strip_Ultimatum
                
                elif K_Legs and (K_Panties or HoseNum("Kitty") >= 10):                              
                    #will she lose the pants/skirt if she has panties on?
                    if ApprovalCheck("Kitty", 1200, TabM = 3) or (K_SeenPanties and not Taboo):
                            call Statup("Kitty", "Lust", 50, 5)                
                            call Statup("Kitty", "Obed", 50, 1)
                            call Statup("Kitty", "Inbt", 30, 1)                
                            call Statup("Player", "Focus", 60, 5)
                            $ Line = K_Legs         
                            $ K_Legs = 0      
                            "Her [Line] slide through her legs until they're only on her toes, before she kicks them to the floor."   
                            if not K_SeenPanties:
                                call Statup("Kitty", "Obed", 50, 2)                              
                                call Statup("Kitty", "Obed", 200, 3)
                                call Statup("Kitty", "Inbt", 50, 3)
                                call Statup("Kitty", "Inbt", 200, 2)
                                $ K_SeenPanties = 1                
                    else:
                            jump K_Strip_Ultimatum          
                        
                elif K_Hose: 
                    # Will she lose the hose?
                    if HoseNum("Kitty") >= 10:
                        if ApprovalCheck("Kitty", 1200, TabM = 3):
                                call Statup("Kitty", "Lust", 50, 6)
                                call Statup("Player", "Focus", 60, 6)
                        else:    
                                jump K_Strip_Ultimatum
                            
                    elif HoseNum("Kitty") >= 6 and ApprovalCheck("Kitty", 1200, TabM = 3):
                        if ApprovalCheck("Kitty", 1200, TabM = 3):
                            call Statup("Kitty", "Lust", 50, 4)
                            call Statup("Player", "Focus", 60, 4)
                        else:    
                            jump K_Strip_Ultimatum
                    else:
                        call Statup("Kitty", "Lust", 50, 3)
                        call Statup("Player", "Focus", 60, 3)
                    $ Line = K_Hose
                    $ K_Hose = 0
                    "Her [Line] slide down off her legs, leaving them in a small pile."     
                    
                elif K_Over and not K_Chest and (K_Panties or HoseNum("Kitty") >= 10):      
                    #will she lose the top when she's topless with panties?        
                    if ApprovalCheck("Kitty", 1250, TabM = 3) or (K_SeenChest and not Taboo):
                            call Statup("Kitty", "Lust", 60, 5)                
                            call Statup("Kitty", "Obed", 50, 2)
                            call Statup("Kitty", "Inbt", 50, 10)   
                            call Statup("Player", "Focus", 80, 15)    
                            $ Line = K_Over
                            $ K_Over = 0                          
                            if not K_SeenChest:
                                call KittyFace("bemused", 1)
                                call Statup("Kitty", "Obed", 50, 3)                              
                                call Statup("Kitty", "Obed", 200, 4)
                                call Statup("Kitty", "Inbt", 50, 3)
                                call Statup("Kitty", "Inbt", 200, 3)  
                                "She hesitantly glances your way, and then with tug her [Line] passes through her, tossing it to the ground."   
                                call Kitty_First_Topless(1)        
                            else: 
                                "She pulls her [Line] over her head, tossing it to the ground."      
                    else:
                            jump K_Strip_Ultimatum
                    
                elif K_Chest and not K_Over:                                     
                    # Will she lose the bra?
                    if ApprovalCheck("Kitty", 1250, TabM = 3) or (K_SeenChest and not Taboo):
                            call Statup("Kitty", "Lust", 60, 5)                
                            call Statup("Kitty", "Obed", 50, 2)
                            call Statup("Kitty", "Inbt", 50, 1)
                            call Statup("Player", "Focus", 80, 15)      
                            $ Line = K_Chest
                            $ K_Chest = 0                        
                            if not K_SeenChest:
                                    call KittyFace("bemused", 1)
                                    call Statup("Kitty", "Obed", 50, 3)                              
                                    call Statup("Kitty", "Obed", 200, 4)
                                    call Statup("Kitty", "Inbt", 50, 3)
                                    call Statup("Kitty", "Inbt", 200, 3)   
                                    "She hesitantly glances your way, and then with a shrug pulls her [Line] through herself, tossing it to the ground."
                                    call Kitty_First_Topless(1)
                            else:
                                    call KittyFace("sexy")
                                    "She tugs her [Line] off, tossing it to the ground." 
                    else:
                            jump K_Strip_Ultimatum
                
                elif K_Legs:                                                        
                    #will she lose the pants/skirt if she has no panties on?
                    if ApprovalCheck("Kitty", 1350, TabM = 3) or (K_SeenPussy and not Taboo):
                            call Statup("Kitty", "Lust", 75, 10)  
                            $ Line = K_Legs
                            $ K_Legs = 0
                            if not K_SeenPussy:
                                    call Statup("Kitty", "Obed", 60, 3)
                                    call Statup("Kitty", "Obed", 200, 5)
                                    call Statup("Kitty", "Inbt", 50, 4)
                                    call Statup("Kitty", "Inbt", 200, 4)  
                                    "She shyly looks up at you, and then slowly lets her [Line] slide to the floor." 
                                    call Kitty_First_Bottomless(1)  
                            else:                            
                                    call Statup("Kitty", "Obed", 50, 1)                              
                                    call Statup("Kitty", "Obed", 75, 1)
                                    "She lets her [Line] pass through her legs, dropping them to the floor."   
                                    call Statup("Kitty", "Inbt", 70, 2)    
                            call Statup("Player", "Focus", 85, 15)
                    else:
                            jump K_Strip_Ultimatum
                    
                elif K_Over and not K_Panties:                                         
                    #will she lose the overshirt when she's bottomless under?
                    if ApprovalCheck("Kitty", 1350, TabM = 3) or (K_SeenPussy and not Taboo):      
                            $ Line = K_Over
                            $ K_Over = 0         
                            if not K_SeenPussy:                
                                    call Statup("Kitty", "Obed", 60, 3)                              
                                    call Statup("Kitty", "Obed", 200, 5)
                                    call Statup("Kitty", "Inbt", 50, 4)
                                    call Statup("Kitty", "Inbt", 200, 4) 
                                    "She hesitantly glances your way, and then with a tug pulls her [Line] through herself, tossing it to the ground."
                                    call Kitty_First_Bottomless(1)                
                            else:
                                    "She pulls her [Line] off, tossing it to the ground."     
                            if not K_Chest:
                                    if not K_SeenChest:                
                                        call Statup("Kitty", "Obed", 50, 3)  
                                        call Statup("Kitty", "Inbt", 50, 3)
                                        call Kitty_First_Topless(1)
                                    else:
                                        call Statup("Kitty", "Lust", 60, 15)                
                                        call Statup("Kitty", "Obed", 50, 3)                              
                                        call Statup("Kitty", "Obed", 75, 1)
                                        call Statup("Kitty", "Inbt", 50, 3)
                            else:
                                        call Statup("Kitty", "Lust", 75, 10)                
                                        call Statup("Kitty", "Obed", 50, 1)                              
                                        call Statup("Kitty", "Obed", 75, 1)
                                        call Statup("Kitty", "Inbt", 70, 2)                
                            call Statup("Player", "Focus", 85, 15)    
                    else:
                        jump K_Strip_Ultimatum
                
                elif K_Chest:                                                               
                    # Will she go topless?
                    if ApprovalCheck("Kitty", 1250, TabM = 3) or (K_SeenChest and not Taboo):
                            call Statup("Kitty", "Lust", 60, 5)  
                            $ Line = K_Chest
                            $ K_Chest = 0         
                            if not K_SeenChest:
                                    call Statup("Kitty", "Obed", 50, 3)                              
                                    call Statup("Kitty", "Obed", 200, 4)               
                                    call Statup("Kitty", "Inbt", 50, 3)
                                    call Statup("Kitty", "Inbt", 200, 3)  
                                    "She hesitantly glances your way, and then with a tug pulls her [Line] through herself, tossing it to the ground." 
                                    call Kitty_First_Topless(1)
                            else:                
                                    call Statup("Kitty", "Obed", 50, 2)
                                    "She pulls her [Line] off, tossing it to the ground."  
                                    call Statup("Kitty", "Inbt", 50, 1)
                            call Statup("Player", "Focus", 80, 15)   
                    else:
                        jump K_Strip_Ultimatum
                    
                elif K_Panties:                                                                        
                    # Will she go bottomless?
                    if ApprovalCheck("Kitty", 1350, TabM = 3) or (K_SeenPussy and not Taboo):
                            call Statup("Kitty", "Lust", 75, 10) 
                            $ Line = K_Panties
                            $ K_Panties = 0         
                            if not K_SeenPussy:
                                    call Statup("Kitty", "Obed", 60, 3)                              
                                    call Statup("Kitty", "Obed", 200, 5)
                                    call Statup("Kitty", "Inbt", 50, 4)
                                    call Statup("Kitty", "Inbt", 200, 4) 
                                    "She shyly looks up at you, and then slowly tugs her [Line] off, flinging them to the side." 
                                    call Kitty_First_Bottomless(1) 
                            else:                
                                    call Statup("Kitty", "Obed", 50, 1)                              
                                    call Statup("Kitty", "Obed", 75, 1)
                                    "She  looks up at you, and then gently pulls her [Line] off, flicking them to the side."                  
                                    call Statup("Kitty", "Inbt", 70, 2)   
                            call Statup("Player", "Focus", 85, 15)
                    else:
                            jump K_Strip_Ultimatum
                    
                else:    
                    call KittyFace("sexy")
                    ch_k "It looks like I've run out of clothes. . ."
                    menu:
                        extend ""
                        "Ok, you can stop":
                                $ K_RecentActions.append("stopdancing")  
                                call K_Pos_Reset        
                        "Keep on dancing":
                                $ K_RecentActions.append("keepdancing")
        # end "nude" not in K_RecentActions loop
        
        call Statup("Kitty", "Lust", 70, 2)               #lust/Focus
        if "exhibitionist" in K_Traits:
                call Statup("Kitty", "Lust", 200, 2)
        call Statup("Player", "Focus", 60, 3)
        if Trigger2 == "jackin":
                call Statup("Kitty", "Lust", 200, 2)
                call Statup("Player", "Focus", 200, 5)
        
        if not P_Semen and P_Focus >= 50:
                $ P_Focus = 50
    
        if P_Focus >= 100 or K_Lust >= 100:                                     
                #If either of you could cum 
                
                if P_Focus >= 100:                                                 
                    #You cum             
                    call PK_Cumming
                    if "angry" in K_RecentActions:  
                        return    
                    call Statup("Kitty", "Lust", 200, 5) 
                    if not P_Semen and Trigger2 == "jackin":
                        "You're spitting dust here, maybe just watch quietly for a while."
                        $ Trigger2 = 0
                
                    if P_Focus > 80:
                        jump Group_Strip_End   
                
                if K_Lust >= 100:                                                   
                    #and Kitty cums                    
                    call K_Cumming
                    if Situation == "shift" or "angry" in K_RecentActions:                    
                        $ Count = 0
                        jump Group_Strip_End 
                     
                call AllReset("Kitty")
                show Kitty_Sprite at Kitty_Dance1()
                "Kitty begins to dance again."
            
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Kitty")
                    
        menu:
            "Kitty should. . ."
            "Keep Going. . ." if "keepdancing" not in K_RecentActions:
                    $ K_Eyes = "sexy"
                    if K_Love >= 700 or K_Obed >= 500:
                        if not Tempmod:
                            $ Tempmod = 10
                        elif Tempmod <= 20:
                            $ Tempmod += 1
                    if Taboo and K_Strip <= 10:
                        call Statup("Kitty", "Obed", 50, 7)
                    elif Taboo or K_Strip <= 10:
                        call Statup("Kitty", "Obed", 50, 5)
                    elif K_Strip <= 50:
                        call Statup("Kitty", "Obed", 50, 3) 
            "Keep Dancing. . ." if "keepdancing" in K_RecentActions:
                    $ K_Eyes = "sexy"    
                                
            "Stop stripping, keep dancing" if "keepdancing" not in K_RecentActions:
                    ch_k "K. . ."
                    $ K_RecentActions.append("keepdancing")
                
            "Start stripping again" if "keepdancing" in K_RecentActions:
                    $ K_RecentActions.remove("keepdancing")
                    if "stripforced" in K_RecentActions: 
                            ch_k ". . ."
                    else:
                            ch_k "Huh?"
                    jump K_Stripping
                    
            "Just watch silently":
                if "watching" not in K_RecentActions:
                    if "keepdancing" not in K_RecentActions:
                        if Taboo and K_Strip <= 10:
                            call Statup("Kitty", "Inbt", 50, 3) 
                        elif Taboo or K_Strip <= 10:
                            call Statup("Kitty", "Inbt", 50, 1) 
                    elif K_Strip <= 50:
                            call Statup("Kitty", "Lust", 70, 2) 
                    $ K_RecentActions.append("watching")  
            
            "Start jack'in it." if Trigger2 != "jackin":
                    call K_Jackin                   
            "Stop jack'in it." if Trigger2 == "jackin":
                    $ Trigger2 = 0
                    
            "Ok, that's enough.":
                    ch_k "Ok. . ."
                    $ renpy.pop_call()
                    jump Group_Strip_End
                
        return
    



# end Strip Tease ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

 
transform Kitty_Dance1():     
    subpixel True 
    pos (K_SpriteLoc, 50)
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

# Start Kitty Undressing  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label K_Undress(Region = "ask", CountStore=0):           
    $ CountStore = Tempmod   
    if Partner == "Kitty":
            $ Tempmod = 0
    call Shift_Focus("Kitty") 
    
    if Region == "auto":
        if K_Upskirt and K_PantiesDown:
            return
        if K_Legs == "pants" and Tempmod < 20:
            $ Tempmod = 20
        if K_Lust >= 90:
            $ Tempmod += 10      
        elif K_Lust >= 80:
            $ Tempmod += 5     
        $ Situation = "auto"
        call Kitty_Bottoms_Off(0)
    
    if Region == "ask":
        menu:
            ch_k "Which parts?"
            "Her top" if K_Over or K_Chest:    
                $ Region = "top"     
            "Her bottoms" if K_Legs or K_Panties or K_Hose:
                $ Region = "bottom"           
            "A little of both. . ." if K_Over or K_Chest or K_Legs or K_Panties or K_Hose: 
                $ Region = "both"    
            "Never mind":
                pass
    
    if Region == "top":
        if K_Over or K_Chest:    
                call Kitty_Top_Off(0)  
    elif Region == "bottom":
        if K_Legs or K_Panties or K_Hose:
                call Kitty_Bottoms_Off(0)    
    elif Region == "both":        
            if K_Over or K_Chest:    
                    call Kitty_Top_Off(0) 
                     
            if Partner == "Kitty":
                    $ Tempmod = 0
            else:
                    $ Tempmod = CountStore 
            
            if "angry" in K_RecentActions: 
                    pass            
            elif not K_Legs and not K_Panties and not K_Hose:
                    pass                
            elif "no topless" in K_RecentActions:
                    menu:
                        ch_k "Don't push it. . ."
                        "And now the bottoms?":
                            call Kitty_Bottoms_Off(0) 
                        "You're probably right, sorry.":
                            pass
            else:
                    ch_p "And now the bottoms?"
                    call Kitty_Bottoms_Off(0) 
                    
    
    $ Tempmod = CountStore
    return


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label Kitty_Top_Off(Intro = 1, Line = 0, Cnt = 0):                                                    # Will she take her top off? Modifiers
    call Shift_Focus("Kitty")
    
    if not K_Over and not K_Chest:                              # If she's already topless. Just skip back.
        $ Tempmod = 0
        return
        
    if "angry" in K_RecentActions:  
        ch_k "No titties for you."
        return
    
    if K_SeenChest and ApprovalCheck("Kitty", 600) and not Taboo:                              #You've seen her tits.
        $ Tempmod += 20
    if "exhibitionist" in K_Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in K_Traits or "sex friend" in K_Petnames and not Taboo:
        $ Tempmod += 10
    elif "ex" in K_Traits:
        $ Tempmod -= 40 
    if "no topless" in K_RecentActions: 
        $ Tempmod -= 10
                     
    if Intro and not K_Uptop:
        if K_Over:
                ch_p "This might be easier without your [K_Over] on."
        elif K_Chest:
                ch_p "This might be easier without your [K_Chest] on."

    $ Approval = ApprovalCheck("Kitty", 1200, TabM = 4) # 110, 125, 140, 300 taboo, -20 if already seen
    
    if Situation == "auto" and  (K_Over or K_Chest) and not K_Uptop:   
            $ Line = 0
            if ApprovalCheck("Kitty", 1300, TabM = 1) or (K_SeenChest and ApprovalCheck("Kitty", 500) and not Taboo):
                    #if she'd go topless
                    call Statup("Kitty", "Inbt", 70, 1)
                    $ K_Uptop = 1
                    $ Line = K_Over if K_Over else K_Chest
                    "Kitty growls slighty, and pulls her [Line] up over her breasts."
                    if Taboo:
                        call Statup("Kitty", "Inbt", 90, (int(Taboo/20)))   
                    call Kitty_First_Topless(1)
                    ch_k "I[K_like]wasn't feeling it that way."  
            elif K_Over and K_Chest and ApprovalCheck("Kitty", 900, TabM = 1):
                    #if she won't go topless, but has a bra on. . .
                    call Statup("Kitty", "Inbt", 40, 1)
                    $ Line = K_Over
                    $ K_Over = 0
                    "Kitty growls slighty, and pulls her [Line] over her head, throwing it aside."
                    ch_k "I[K_like]wasn't feeling it that way."  
            $ Line = 0
            return  
            
    if Situation == "auto":  
        $Line = 0
        if K_Over: # If she's in a top
            if K_Chest and ApprovalCheck("Kitty", 800, TabM = 1):
                call Statup("Kitty", "Inbt", 40, 1)
            elif Approval >= 2 or (K_SeenChest and ApprovalCheck("Kitty", 600) and not Taboo):
                call Statup("Kitty", "Inbt", 70, 1)
            else:
                return
            $ Line = K_Over
            $ K_Over = 0
            "Kitty growls slighty, and lets her [Line] drop to the ground."
            if not K_Chest:
                if Taboo:
                    call Statup("Kitty", "Inbt", 90, (int(Taboo/20)))   
                call Kitty_First_Topless(1)
                
        if K_Chest:
            if Approval >= 2 or (K_SeenChest and ApprovalCheck("Kitty", 600) and not Taboo):
                call Statup("Kitty", "Inbt", 70, 1)
                if Taboo:
                    call Statup("Kitty", "Inbt", 90, (int(Taboo/20)))  
                if Line:
                    $ Line = K_Chest
                    $ K_Chest = 0
                    "As it hits the floor, she lets her [Line] fall through her."  
                else:
                    $ Line = K_Chest
                    $ K_Chest = 0
                    "Kitty growls slightly, and her [Line] falls through her body to the floor."                     
                call Kitty_First_Topless(1) 
                ch_k "I[K_like]wasn't feeling it that way."  
        return
    
    
    if Approval >= 2:                                                                               # Does she assume top off?            
        if "no topless" in K_DailyActions:
            ch_k "Okay, okay!"
        call KittyFace("sexy", 1)
        if K_Forced:
            call KittyFace("sad", 1)
            call Statup("Kitty", "Love", 20, -2, 1)
            call Statup("Kitty", "Love", 70, -3, 1)
            call Statup("Kitty", "Obed", 40, 2)
            call Statup("Kitty", "Obed", 90, 1)
            call Statup("Kitty", "Inbt", 50, 1)
        call Statup("Kitty", "Inbt", 50, 3)  
        $ Cnt = 1
        while (K_Chest or K_Over) and Cnt:
            menu:                                                                                 #Menu All off?
                ch_k "So[K_like]how much did you want me to take off?"  
                "Lose the [K_Over]." if K_Over:                 
                    call KittyFace("bemused", 1)                    
                    $ Line = K_Over
                    $ K_Over = 0
                    "Kitty lets her [Line] pass through her body and fall to the floor."
                "Just lose the [K_Chest]." if K_Over and K_Chest:
                    call KittyFace("bemused", 1)                    
                    $ Line = K_Chest
                    $ K_Chest = 0                 
                    "Kitty reaches through her [K_Over] and grabs, pulling her [Line] from underneath it."   
                "Lose the [K_Chest]." if not K_Over and K_Chest:
                    call KittyFace("bemused", 1)
                    $ Line = K_Chest
                    $ K_Chest = 0                 
                    "Kitty lets her [Line] fall to the ground."   
                "Just pull it up." if (K_Over or K_Chest) and not K_Uptop:
                    call KittyFace("bemused", 1)
                    $ K_Uptop = 1
                    if K_Over and K_Chest:
                            "Kitty smiles and lifts up her tops. . ."   
                    else:
                            "Kitty smiles and lifts up her top. . ."   
                "Lose both tops." if K_Over and K_Chest:
                    call KittyFace("bemused", 1)
                    $ Line = K_Chest
                    $ K_Chest = 0 
                    "Kitty smiles and suddenly her [Line] falls to between her legs. . ."     
                    $ Line = K_Over
                    $ K_Over = 0
                    "quickly followed by her [Line]."              
                "That's enough. [[exit]":               
                    call KittyFace("bemused", 1)
                    ch_k "K."    
                    $ Cnt = 0
        if not K_Chest and not K_Over:             
            call Statup("Kitty", "Obed", 40, 2)
            call Statup("Kitty", "Obed", 90, 1)
            call Kitty_First_Topless  
        call Statup("Kitty", "Lust", 80, 3)        
        $ K_RecentActions.append("ask topless")                      
        $ K_DailyActions.append("ask topless") 
        $ Tempmod = 0        
        return
        
    #Else, Approval < 2, Doesn't want to lose the top//////////////////////////////////  
                 
    call KittyFace("bemused", 1)   
    if Intro == "massage" and not Approval:
        ch_k "A massage is fine, but I'm keeping my top on, ok?"
    elif "no topless" in K_RecentActions: 
        call KittyFace("angry")
        ch_k "I[K_like]already told you, no way!"    
    elif Approval and not K_SeenChest:
        ch_k "I'm[K_like]not really comfortable with that."    
    elif not K_SeenChest:
        ch_k "I'd[K_like]really rather not, ok?"   
    elif "no topless" in K_DailyActions: 
        ch_k "Do you[K_like]think something's changed since earlier?"           
    elif "ask topless" in K_RecentActions: 
        ch_k "Did you[K_like]want something else off?"       
    elif Taboo:
        ch_k "I'm[K_like]not that comfortable out here. . ."          
    elif Approval:
        ch_k "Maybe not?"
    else:
        ch_k "Nu-uh."
        
    menu:
        ch_k "I'll keep my top on, [K_Petname]."
        "Sorry, sorry." if "no topless" in K_RecentActions:  
            call KittyFace("bemused", 1)   
            ch_k "It's cool, I get it, but[K_like]chill out, huh?"
        "Ok, that's fine." if "no topless" not in K_RecentActions: 
            if "ask topless" not in K_DailyActions:
                call Statup("Kitty", "Lust", 80, 3)
                call Statup("Kitty", "Love", 70, 1)
                call Statup("Kitty", "Love", 90, 1)
                call Statup("Kitty", "Inbt", 50, 2)
            if K_Forced:
                $ K_Mouth = "grimace"
                ch_k "That's[K_like]really cool of you."
                if "ask topless" not in K_DailyActions:
                    call Statup("Kitty", "Love", 20, 2)
                    call Statup("Kitty", "Love", 70, 2)
                                                                                                         
        "How about just the [K_Over]?" if K_Over:                                                # asked to go shirtless. 
            if ApprovalCheck("Kitty", 1000, TabM = 3) and K_Chest: #80, 160 taboo 
                call KittyFace("sexy") 
                ch_k "Um, I guess I could. . ."                 
                call KittyFace("bemused", 1)                
                $ Line = K_Over
                $ K_Over = 0
                "Kitty tosses the [Line] over her head."   
                call Statup("Kitty", "Obed", 30, 1)
                call Statup("Kitty", "Obed", 60, 1)
                call Statup("Kitty", "Inbt", 30, 2)
            elif not K_Chest:
                $ K_Eyes = "surprised"
                $ K_Blush = 2
                ch_k "I'd[K_like]be {i}totally{/i} exposed here." 
                call Statup("Kitty", "Inbt", 30, 1)
                menu:
                    extend ""
                    "Ok, you can leave it on.":
                        $ K_Mouth = "smile"
                        call Statup("Kitty", "Love", 70, 2)
                        ch_k "Thanks!"             
                    "That doesn't bother me any.":                                              #fix this
                        if ApprovalCheck("Kitty", 700, "I", TabM=3) or ApprovalCheck("Kitty", 1100, TabM=3):
                            call KittyFace("bemused", 1)
                            ch_k "Why am I not surprised?"                               
                            call Statup("Kitty", "Obed", 20, 2)                                                         
                            call Statup("Kitty", "Obed", 60, 1)
                            call KittyFace("sexy")   
                            $ Line = K_Over
                            $ K_Over = 0
                            "Kitty tosses the [Line] over her head."                            
                            $ K_Over = 0
                            call Statup("Kitty", "Inbt", 30, 1)  
                            call Statup("Kitty", "Inbt", 60, 1)
                            call Kitty_First_Topless   
                        else:   
                            call KittyFace("bemused")
                            call Kitty_Top_Off_Refused  
                            
                    "I know, take it off.":
                        call Kitty_ToplessorNothing
                $ K_Blush = 1        
            else:   
                call KittyFace("sexy")
                call Kitty_Top_Off_Refused  
                                 
        "Come on, Please? [[take it all off]":                                                                      # asked to go topless. 110, 270 Taboo   
            if Approval and ApprovalCheck("Kitty", 600, "L", TabM=1):                 
                call Statup("Kitty", "Obed", 40, 2)
                call KittyFace("sexy")   
                if "no topless" in K_RecentActions:     
                    ch_k "You just don't know when to quit. . . but you got lucky this time. . ."
                else:
                    ch_k "You[K_like]know how to ask nicely . . ." 
                $ K_Uptop = 1
                "Kitty just pulls her top up over her tits."           
                call Statup("Kitty", "Inbt", 30, 1)  
                call Statup("Kitty", "Inbt", 60, 1)
                call Kitty_First_Topless   
            elif "no topless" in K_RecentActions:
                call KittyFace("angry")
                ch_k "Noooope!"
                call Statup("Kitty", "Love", 80, -5)       
                $ K_RecentActions.append("angry")
                $ K_DailyActions.append("angry")   
            else:   
                call KittyFace("sexy")
                call Kitty_Top_Off_Refused
        
        "No, topless or nothing.":                                                              #demanded topless 60, 260 taboo 
            call Kitty_ToplessorNothing
            
        "Never mind.":
            pass
    
    $ K_RecentActions.append("ask topless")                      
    $ K_DailyActions.append("ask topless") 
    $ Tempmod = 0
    return


label Kitty_Top_Off_Refused:                    #When you insist but she refuses    
    call KittyFace("angry")
    if "no topless" in K_RecentActions:  
        ch_k "[K_Like]back off."
    elif "no topless" in K_DailyActions:  
        ch_k "Not today, maybe not ever, [K_Petname]."
    else:
        call KittyFace("sad")
        ch_k "[K_Like], no way, but I don't want to go. . ."
    menu:
        extend ""
        "Sure, never mind." if "no topless" not in K_RecentActions:
            call KittyFace("sexy")
            call Statup("Kitty", "Love", 70, 2)
            ch_k "Great!"  
        "Sorry, I'll drop it." if "no topless" in K_RecentActions:   
            ch_k "Good."  
        "No, let's do something else.":
            $ K_Brows = "angry"
            ch_k "Fine then!"
            call Statup("Kitty", "Lust", 50, 5)
            call Statup("Kitty", "Love", 70, -5, 1)
            if "no topless" not in K_RecentActions:
                call Statup("Kitty", "Lust", 70, 5)
                call Statup("Kitty", "Obed", 60, 5)    
            $ K_RecentActions.append("angry")
            $ K_DailyActions.append("angry")   
    $ K_RecentActions.append("no topless")                      
    $ K_DailyActions.append("no topless") 
    return
              

label Kitty_ToplessorNothing:
    call KittyFace("angry")
    if ApprovalCheck("Kitty", 1000, "OI", TabM = 4) and ApprovalCheck("Kitty", 500, "O", TabM = 3):       #She agrees to your ultimatum 
        call Statup("Kitty", "Love", 20, -2, 1)
        call Statup("Kitty", "Love", 80, -5, 1)
        call Statup("Kitty", "Inbt", 60, 2)
        if "no topless" in K_RecentActions:             
            ch_k "Ok, fine. This time."                 
        else:
            call KittyFace("sad")
            ch_k "Whatever."                
        call Statup("Kitty", "Obed", 60, 5)
        call Statup("Kitty", "Obed", 90, 2)
        $ K_Uptop = 1
        "Kitty slowly pulls her top up over her tits."
        call Kitty_First_Topless                       
    else:                                                                                                #she refuses your ultimatum
        call Statup("Kitty", "Love", 200, -10)                
        call Statup("Kitty", "Obed", 40, -1, 1)
        if "no topless" in K_RecentActions: 
            ch_k "It[K_like]wasn't cute the first time."      
        else:
            $K_Brows = "angry"
            ch_k "[K_Like]no way!"   
        $ K_RecentActions.append("no topless")                      
        $ K_DailyActions.append("no topless")     
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    return              
    
label Kitty_First_Topless(Silent = 0, TempLine = 0):  
    if ChestNum("Kitty") > 1 or OverNum("Kitty") > 2:
        #if she's wearing substantial clothing. . .
        return          
    if K_Loc != bg_current:
            return
    $ K_RecentActions.append("topless")                      
    $ K_DailyActions.append("topless")
    call DrainWord("Kitty","no topless")    
    $ K_SeenChest += 1 
    if K_SeenChest > 1:     
        return                  #ends portion if you've already seen them
    
    
    call Statup("Kitty", "Inbt", 70, 15)  
    if not Silent:
        call KittyFace("bemused", 2)
        "Kitty looks a bit shy, and slowly lowers her hands from her chest."
        ch_k "[K_Like]what do you think?"    
        $ K_Blush = 1
        menu:
            extend ""
            "Lovely.":            
                call Statup("Kitty", "Love", 90, 20)
                call Statup("Kitty", "Inbt", 70, 20)               
                call KittyFace("smile",2)
                ch_k ". . ."
                call Statup("Kitty", "Love", 40, 20)  
                $ K_Blush = 1
                        
            "That's it?":        
                call Statup("Kitty", "Love", 90, -30)
                call Statup("Kitty", "Obed", 60, 25)
                call Statup("Kitty", "Inbt", 70, -15)                          
                call KittyFace("confused",2)
                ch_k "What?"
                menu:      
                    "I, um, no, they're great!":                        
                        call KittyFace("angry",2, Mouth="smile")
                        call Statup("Kitty", "Inbt", 70, 10)   
                        ch_k "Obviously!"            
                    "[EmmaName]'s were bigger, that's all." if E_SeenChest:                            
                        $ TempLine = "Emma"
                    "Rogue's were bigger, that's all." if R_SeenChest:                            
                        $ TempLine = "Rogue"
                        
                if TempLine:
                        call KittyFace("angry")
                        $ K_Mouth = "surprised"                        
                        call Statup("Kitty", "Love", 90, -10)
                        call Statup("Kitty", "Obed", 80, 30)
                        call Statup("Kitty", "Inbt", 70, -25)  
                        ". . ."
                        $ K_Mouth = "sad"
                        if TempLine == "Emma":
                                if K_LikeEmma >= 800:
                                    call KittyFace("sly",2,Eyes="side")
                                    call Statup("Kitty", "Obed", 80, 5)
                                    ch_k "Yeah, like you just wanna shove your head into there. . ."       
                                    $ K_LikeEmma += 20 
                                elif K_LikeEmma >= 700:
                                    $ K_Eyes = "side" 
                                    call Statup("Kitty", "Obed", 80, 5)
                                    ch_k "I mean, I guess, if you like that kind of thing. . ."
                                else:                        
                                    $ K_LikeEmma -= 50
                                    $ Templine = "bad"
                                
                        elif TempLine == "Rogue":
                                if K_LikeRogue >= 800:
                                    call KittyFace("sly",2,Eyes="side")
                                    call Statup("Kitty", "Obed", 80, 5)
                                    ch_k "Yeah, like two ripe apples. . . I mean-"       
                                    $ K_LikeRogue += 20 
                                elif K_LikeRogue >= 700:
                                    $ K_Eyes = "side" 
                                    call Statup("Kitty", "Obed", 80, 5)
                                    ch_k "[K_Like]I guess. . ."
                                else:                        
                                    $ K_LikeRogue -= 50
                                    $ Templine = "bad"
                                                
                        if TempLine == "bad":
                                call Statup("Kitty", "Love", 90, -20)
                                ch_k "Well you sure know how to ruin a mood."     
                                call KittyOutfit
                                $ K_RecentActions.append("no topless")                      
                                $ K_DailyActions.append("no topless")  
                                $ K_RecentActions.append("angry")
                                $ K_DailyActions.append("angry") 
                        
                    
    else:
        if ApprovalCheck("Kitty", 800) and not K_Forced:                #if she's not forced and happy about it
            call Statup("Kitty", "Inbt", 70, 15) 
            call Statup("Kitty", "Obed", 70, 15)              
            call KittyFace("smile")
        else:                                                           #if she's not happy about it
            call Statup("Kitty", "Love", 90, -40)
            call Statup("Kitty", "Inbt", 70, -20)                          
            call KittyFace("angry")
            call Statup("Kitty", "Obed", 70, 40)
    return



# Bottoms ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label Kitty_Bottoms_Off(Intro = 1, Line = 0, Cnt = 0):
    call Shift_Focus("Kitty")
    
    if not K_Legs and not K_Panties and not K_Hose:                                  # If she's already bottomless. Just skip back.     
        $ Tempmod = 0
        return
    
    if "angry" in K_RecentActions:  
        ch_k "The only \"kitty\" you're getting is up here."
        return
    
    # Will she take her bottoms off Modifiers
    if K_SeenPussy and ApprovalCheck("Kitty", 800): #You've seen her Pussy.
        $ Tempmod += 20
    elif not K_Panties:
        $ Tempmod -= 20
    elif K_SeenPanties and ApprovalCheck("Kitty", 600): #You've seen her panties.
        $ Tempmod += 5 
    if Intro == "dildo":
        $ Tempmod += 20
    if "exhibitionist" in K_Traits:
        $ Tempmod += (Taboo * 5)
    if "dating" in K_Traits or "sex friend" in K_Petnames and not Taboo:
        $ Tempmod += 10
    elif "ex" in K_Traits:
        $ Tempmod -= 40 
    if "no bottomless" in K_RecentActions: 
        $ Tempmod -= 20
    
    if Intro:
        if K_Legs and not K_Upskirt:
                ch_p "This might be easier without your [K_Legs] on."
        elif K_Panties and not K_PantiesDown:
                ch_p "This might be easier without your [K_Panties] on."
                
    $ Approval = ApprovalCheck("Kitty", 1300, TabM = 5) # 120, 135, 150, -200(320) taboo, -25 if already seen
    
    if Situation == "auto":
        $ Cnt = 0
            
        if not K_Upskirt and not K_PantiesDown:                  
            if K_Legs == "blue skirt":                                          #If she's in a skirt with panties, hike it up?
                if Approval >= 2 or (K_SeenPussy and ApprovalCheck("Kitty", 700) and not Taboo):
                    call Statup("Kitty", "Inbt", 60, 1)
                    if Taboo:
                        call Statup("Kitty", "Inbt", 90, (int(Taboo/20)))                 
                    $ K_Upskirt = 1
                    "She slides her skirt up."
                    $ Cnt = 1 
                    
            if PantsNum("Kitty") >= 5 or HoseNum("Kitty") >= 6:            
                if K_Panties:                                               #she has pants and panties on
                    if not Approval or (not K_SeenPanties and Taboo):
                        return   
                elif Approval < 2 or (not K_SeenPussy and Taboo):
                    return     
                elif K_Legs == "pants" and K_Upskirt:  
                    return
                call Statup("Kitty", "Inbt", 60, 1)
                $ K_Upskirt = 1
                "Kitty grumbles to herself, and then lets her [Line] fall to the ground." 
                if K_Panties:
                    $ K_SeenPanties = 1
                else:
                    call Kitty_First_Bottomless(1)  
                    
                if Taboo:
                    call Statup("Kitty", "Inbt", 90, (int(Taboo/10)))  
                $ Cnt = 1 
                
        if K_Panties and not K_PantiesDown:                                              # Just wearing panties, lose them?
            if Approval >= 2 or (K_SeenPussy and not Taboo):
                call Statup("Kitty", "Inbt", 70, 2)
                if Taboo:
                    call Statup("Kitty", "Inbt", 90, (int(Taboo/10)))  
                $ K_PantiesDown = 1
                if Cnt:
                    "Kitty tsks in irritation, and her [K_Panties] drop off too."
                else:
                    "Kitty tsks in irritation, and her [K_Panties] phase through her to the floor." 
                call Kitty_First_Bottomless(1) 
                    
                ch_k "It's super annoying not being able to phase you through these."  
        return
            
    
    if Approval >= 2:                 #will she volunteer to strip to underwear?///////////////////////////////////////////////////        
        call KittyFace("sexy", 1)
        if K_Forced:
            call KittyFace("sad", 1)              
            call Statup("Kitty", "Love", 20, -2, 1)
            call Statup("Kitty", "Love", 70, -3, 1)
            call Statup("Kitty", "Obed", 50, 1)
            call Statup("Kitty", "Obed", 90, 1)
            call Statup("Kitty", "Inbt", 60, 1)
            $ Line = "Fine, what'll it be? . ."            
        elif Approval >= 3:
            $ Line = "Heh, what would you like to see? . ."
        else:    
            $ Line = "Ok, maybe, but don't push it. . ." 
        
        call Kitty_Bottoms_Off_Legs
            
        if not K_Panties and Action_Check("Kitty", "recent", "bottomless") < 2: 
            call Statup("Kitty", "Obed", 50, 2)
            call Statup("Kitty", "Obed", 90, 1)
            call Statup("Kitty", "Inbt", 50, 3)
            call Statup("Kitty", "Lust", 80, 3)
    
  
        
    elif K_Legs or K_Panties or K_Hose:                                                      # She'd rather not strip but might        
        call KittyFace("bemused", 1) 
        if "no bottomless" in K_RecentActions: 
            call KittyFace("angry")
            ch_k "Last warning, [K_Petname]. No."   
        elif "no topless" in K_RecentActions: 
            call KittyFace("angry")
            ch_k "Not learning from your mistakes here, [K_Petname]. . ."  
        elif Approval and not K_SeenPussy:
            ch_k "I'm not sure about that. . ."  
        elif not K_SeenPussy and "ask topless" in K_RecentActions:
            ch_k "That's a bit too far."    
        elif not K_SeenPussy:
            ch_k "Maybe later?"   
        elif "no bottomless" in K_DailyActions: 
            ch_k "Short memory, [K_Petname]?"             
        elif Taboo:
            ch_k "This is[K_like]kinda public. . ."  
        elif Approval:
            ch_k "I'm[K_like]not sure about this. . ."   
        elif K_SeenPussy:
            ch_k "Well, you've seen[K_like]it before . . ."            
        elif PantsNum("Kitty") >= 10:
            ch_k "I'm keeping my pants on."   
        elif PantsNum("Kitty") >= 5:
            ch_k "I'm keeping my shorts on."  
        else:
            ch_k "I'm keeping my panties on." 
        menu:            
            extend ""
            "Ok, never mind." if "no bottomless" not in K_RecentActions:  
                if "ask bottomless" not in K_DailyActions:
                    call Statup("Kitty", "Lust", 80, 2)
                    call Statup("Kitty", "Love", 70, 1)
                    call Statup("Kitty", "Love", 90, 1)
                    call Statup("Kitty", "Obed", 50, 2)
                    call Statup("Kitty", "Inbt", 50, 2)
                if K_Forced:
                    $ K_Mouth = "smile"
                    ch_k ". . . thank you."
                    if "ask bottomless" not in K_DailyActions:
                        call Statup("Kitty", "Love", 20, 3)
                        call Statup("Kitty", "Love", 70, 4)
                        call Statup("Kitty", "Inbt", 60, 2)
                    
            "Sorry, sorry." if "no bottomless" in K_RecentActions:  
                ch_k "[K_Like], fine, whatever."
             
            "Come on, Please?": 
                    if "no bottomless" in K_DailyActions:    
                            call KittyFace("angry", 1)
                            ch_k "I already told you \"no.\""
                    else:                  
                        if Approval and ApprovalCheck("Kitty", 600, "L", TabM=1):   
                            call KittyFace("sexy", 1)
                            $ D20 = renpy.random.randint(1, 3)
                            if D20 == 3:
                                $ Line = "I guess. . ."
                                $ Approval += 1
                            else:
                                $ Line = "Maybe. . ."                        
                            call Kitty_Bottoms_Off_Legs  
                        else:    
                            call KittyFace("sexy")
                            call Kitty_Bottoms_Off_Refused
                                    
            "It doesn't have to be everything. . ." if K_Legs or HoseNum("Kitty") >= 10 or K_Panties == "shorts":    
                if Approval and "no bottomless" not in K_DailyActions:                      
                    call KittyFace("bemused", 1)
                    $Line = "Like, how much then?"
                    call Kitty_Bottoms_Off_Legs  
                else:    # She refuses your request. . .
                    call KittyFace("sexy")
                    call Kitty_Bottoms_Off_Refused                       
            "It doesn't have to be everything. . . (locked)" if not K_Legs and HoseNum("Kitty") < 10 and K_Panties != "shorts":   
                    pass
                            
            "No, lose 'em.":            #85 and -200 taboo             
                if (Approval and K_Obed >= 250) or (ApprovalCheck("Kitty", 1000, "OI", TabM = 5) and ApprovalCheck("Kitty", 500, "O", TabM = 3)):                    
                    call Statup("Kitty", "Love", 20, -1, 1)
                    call Statup("Kitty", "Love", 70, -5, 1)
                    call Statup("Kitty", "Obed", 50, 4)
                    call Statup("Kitty", "Obed", 80, 1)
                    call Statup("Kitty", "Inbt", 60, 1)
                    $ Line =  "Like geez, you're serious. . ."  
                    $ Approval = 1 if Approval < 1 else Approval
                    $ K_Forced = 1
                    call Kitty_Bottoms_Off_Legs                     
                else:          
                    call Statup("Kitty", "Love", 200, -10)
                    if ApprovalCheck("Kitty", 400, "O"):
                        ch_k "Sorry[K_like]no way." 
                    else:
                        call KittyFace("angry")
                        ch_k "GTFO."                          
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")   
                    $ K_RecentActions.append("no bottomless")                      
                    $ K_DailyActions.append("no bottomless")   
    
    $ Tempmod = 0
    $ K_RecentActions.append("ask bottomless")                      
    $ K_DailyActions.append("ask bottomless")     
    return           

label Kitty_Bottoms_Off_Legs:    
    
    if K_Forced:        
        call KittyFace("sad", 1)
    elif ApprovalCheck("Kitty", 1100, "OI", TabM = 3):        
        call KittyFace("sly")
    elif ApprovalCheck("Kitty", 1400, TabM = 3):  
        call KittyFace("sexy", 1) 
    else:
        call KittyFace("bemused", 1) 
        
    $ Line = "Well what did you want off?" if not Line else Line
    $ Cnt = 1
    while Cnt and (K_Legs or K_Panties or K_Hose):
        menu:                                       # She's asking what you'd like to see.
            ch_k "[Line]"
            "Everything. . ." if Line != "Like, how much then?": #approval a given
                        
                    if Approval < 2 and not K_Panties and HoseNum("Kitty") < 10:
                        call Kitty_NoPanties
                    
                    if K_Legs:
                        $ Line = K_Legs      
                        $ K_Legs = 0
                        if not K_SeenPanties:
                            "Kitty shyly drops her [Line] to the ground."
                            $ K_SeenPanties = 1
                        else:
                            "Kitty lets her [Line] fall to the ground." 
                    
                    if Approval < 2 and not K_Panties and HoseNum("Kitty") >= 10:
                        call Kitty_NoPanties   
                        
                    if K_Hose:
                        $ Line = K_Hose #HoseName 
                        $ K_Hose = 0
                        "She lets her hose fall off."
                    
                                            
                    if Approval < 2:
                        call Kitty_NoPanties   
                    if K_Panties:                               
                        $ Line = K_Panties   
                        $ K_Panties = 0  
                        "She glances up at you as she lets her [Line] drop." 
                    call Kitty_First_Bottomless   
                    
                    
            "Lose the [K_Legs]." if K_Legs: 
                    if K_Panties and Approval >= 2:
                        call KittyFace("sexy")
                        ch_k "That's. . . doable. . ."
                    elif Approval:          
                        call KittyFace("sexy", 1)    
                        if Approval < 2 and not K_Panties and HoseNum("Kitty") < 10:
                            call Kitty_NoPanties
                    else:    
                        call KittyFace("sexy")
                        call Kitty_Bottoms_Off_Refused
                        return
                        
                    $ Line = K_Legs      
                    $ K_Legs = 0
                    if not K_Panties and HoseNum("Kitty") < 10:
                        call KittyFace("sly", 2)  
                        "She blushes and looks at you slyly before letting her [Line] drop." 
                        call Kitty_First_Bottomless   
                    elif not K_SeenPanties:
                        "Kitty shyly drops her [Line]."
                        $ K_SeenPanties = 1
                    else:
                        "Kitty lets her [Line] fall off." 
                    call KittyFace("bemused", 1)
            
            
            "Lose the [K_Panties]." if K_Panties:
                    if Approval < 2:
                        ch_k "Sorry, no."
                        $ K_RecentActions.append("no bottomless")                      
                        $ K_DailyActions.append("no bottomless")   
                        return                        
                    elif K_Legs == "pants" or HoseNum("Kitty") >= 6:
                        ch_k "[K_Like]I guess. . ."
                    else:
                        ch_k "Ok, sure, [K_Petname]."                                            
                    $ Line = K_Panties   
                    $ K_Panties = 0  
                             
                    if PantsNum("Kitty") >= 10:
                        "She reaches into her pants, then pulls her [Line] through them."    
                    elif PantsNum("Kitty") >= 5:
                        "She reaches into her shorts, then pulls her [Line] through them."
                    else:
                        "She glances up at you as her [Line] drop to the ground."
                    if not K_Legs:
                        call Kitty_First_Bottomless  
            
            "Just give me a clear view. . ." if (K_Panties and not K_PantiesDown) or (K_Legs and not K_Upskirt):
                    if Approval >= 2:
                        ch_k "Fine."
                        $ K_PantiesDown = 1 if K_Panties else 0
                        $ K_Upskirt = 1 if K_Legs else 0
                        "She shifts her [K_Legs] out of the way."
                    elif Approval >= 1 and K_Legs and K_Panties and not K_PantiesDown:
                        ch_k "I guess I could show you something. . ."
                        $ K_Upskirt = 1
                    else:
                        ch_k "No."
                        $ K_RecentActions.append("no bottomless")                      
                        $ K_DailyActions.append("no bottomless")   
                        return   
                    call Kitty_First_Bottomless    
                    
#            "Lose the [K_Hose]." if K_Hose:                                    #make sure to update this mess if I add hose to her
#                    call KittyFace("bemused", 1) 
#                    if K_Legs:
#                        ch_k "Ok, no problem."                         
#                    elif Approval < 2 and not K_Panties and HoseNum("Kitty") >= 10:
#                        call Kitty_NoPanties                            
#                    elif not Approval and HoseNum("Kitty") >= 6:
#                        ch_k "No thanks, [K_Petname]."
#                        return                            
#                    else:
#                        ch_k "Ok, sure, [K_Petname]."                 
                        
#                    $ Line = K_Hose   
#                    $ K_Hose = 0  
#                    if K_Legs:
#                        "She reaches under her [K_Legs] and pulls her [Line] down."
#                    elif HoseNum("Kitty") < 10:
#                        "Kitty pulls her [Line] off." 
#                    elif not K_Panties:
#                        call KittyFace("sly", 2)  
#                        "She blushes and looks at you slyly before removing her [Line]." 
#                        $ K_Blush = 1
#                        call Kitty_First_Bottomless   
#                    elif not K_SeenPanties:
#                        "Kitty shyly removes her [Line]."
#                        $ K_SeenPanties = 1
#                    else:
#                        "Kitty pulls her [Line] off." 
                        
            "Keep it all on for now." if Cnt == 1:
                $ K_Mouth = "smile"
                $ Cnt = 0
                
            "Ok, that's enough for now." if Cnt == 2:
                $ Cnt = 0
                
        $ Cnt = 2 if Cnt else Cnt  
        $ Line = "Ok, is that all?"
    return


label Kitty_NoPanties: #called when asked to remove pants with nothing on under
    if not R_Panties:
        return
    if K_Legs or HoseNum("Kitty") >= 10:
        ch_k "[K_Like]I'm not wearing any panties. . ."  
    else:
        ch_k "Not much else on. . ."  
    menu:
        extend ""
        "Could you do it anyway?":
            if ApprovalCheck("Kitty", 1100, "LI", TabM=1):                                             
                ch_k "I[K_like]guess so. . . "
            else:
                ch_k "No thanks."
                call Kitty_Bottoms_Off_Refused
                $ renpy.pop_call()  
        "Don't care, lose'em.":
            if ApprovalCheck("Kitty", 800, "OI", TabM=1):
                ch_k "Whatev."  
            else:
                call Kitty_Bottoms_Off_Refused
                $ renpy.pop_call()  
                                       
        "Ok, you can leave it on.":
            $ renpy.pop_call()   
    return 
        
label Kitty_Bottoms_Off_Refused:     
    if "no bottomless" in K_RecentActions:  
        ch_k "You're[K_like]on my last nerve here."
    elif "no bottomless" in K_DailyActions:  
        ch_k "Give it a rest."
    else:
        call KittyFace("sad")
        if Cnt == 2:            
            ch_k "What you see is what you get, but[K_like]can't we still have some fun?"   
        else:
            ch_k "The answer's \"no,\" but[K_like]can't we still have some fun?"        
    menu:
        extend ""
        "Sure, never mind." if "no bottomless" not in K_RecentActions:
            $ K_Mouth = "smile"
            call Statup("Kitty", "Love", 70, 2)    
            call Statup("Kitty", "Obed", 60, 2)  
            ch_k "Great!"    
        "Sorry, I'll drop it." if "no bottomless" in K_RecentActions:   
            ch_k "Fine. . ."  
        "No, let's do something else.":
            $K_Brows = "confused"
            ch_k "Ok[K_like]whatever."               
            call Statup("Kitty", "Lust", 50, 5)
            call Statup("Kitty", "Love", 70, -2, 1)
            if "no bottomless" not in K_RecentActions:  
                call Statup("Kitty", "Lust", 70, 5)
                call Statup("Kitty", "Obed", 60, 4)      
            $ K_RecentActions.append("angry")
            $ K_DailyActions.append("angry")   
            
    $ K_RecentActions.append("no bottomless")                      
    $ K_DailyActions.append("no bottomless")
    $ Tempmod = 0
    return   

label Kitty_First_Bottomless(Silent = 0): 
    if PantiesNum("Kitty") > 1 or PantsNum("Kitty") > 2 or HoseNum("Kitty") > 9:
        #if she's wearing substantial clothing. . .
        return     
    if K_Loc != bg_current:
            return
    $ K_RecentActions.append("bottomless")                      
    $ K_DailyActions.append("bottomless")
    call DrainWord("Kitty","no bottomless")
    $ K_SeenPussy += 1 
    if K_SeenPussy > 1:     
        return                  #ends portion if you've already seen them        
    
    
    call Statup("Kitty", "Inbt", 80, 30)  
    call Statup("Kitty", "Obed", 70, 10)   
    if not Silent:
        call KittyFace("bemused", 1)
        "Kitty shyly moves her hands aside, revealing her pussy."        
        menu:        
            extend ""
            "Lovely. . .":            
                call Statup("Kitty", "Love", 90, 20)
                call Statup("Kitty", "Inbt", 60, 25)            
                call KittyFace("smile")          
                ch_k ". . ."
                call Statup("Kitty", "Love", 40, 20)
            "Now {i}that's{/i} the \"Kitty\" I wanted to see.":   
                call Statup("Kitty", "Love", 40, 25) 
                call Statup("Kitty", "Inbt", 60, 30)           
                call KittyFace("perplexed", 2)          
                ch_k "[[snort]"            
                call Statup("Kitty", "Love", 90, 25)
                $ K_Blush = 1
            "Pretty messy down there." if K_Pubes:          
                call KittyFace("surprised",2)  
                ch_k "!"
                if ApprovalCheck("Kitty", 800, "LO"):          
                    call KittyFace("bemused",1)     
                    call Statup("Kitty", "Obed", 50, 30)
                    call Statup("Kitty", "Inbt", 60, 25)        
                    ch_k "I guess I could trim it up a bit. . ."
                    $ K_Todo.append("shave")  
                else:                              
                    call KittyFace("angry",1)  
                    call Statup("Kitty", "Love", 40, -20) 
                    call Statup("Kitty", "Obed", 50, 25)
                    call Statup("Kitty", "Inbt", 60, -5)         
                    ch_k "Well[K_like]sorry I don't keep it baby soft!"
            "I've seen better.":        
                call Statup("Kitty", "Love", 90, -30)
                call Statup("Kitty", "Obed", 50, 25)
                call Statup("Kitty", "Inbt", 70, -30)
                call KittyFace("angry")           
                ch_k ". . ."
                call Statup("Kitty", "Obed", 70, 35)
    else:
        if ApprovalCheck("Kitty", 800) and not K_Forced:
            call Statup("Kitty", "Love", 90, 20)
            call Statup("Kitty", "Inbt", 60, 25)          
            call KittyFace("smile")          
            call Statup("Kitty", "Love", 40, 20)
            call Statup("Kitty", "Obed", 70, 10)
        else:        
            call Statup("Kitty", "Love", 90, -40)
            call Statup("Kitty", "Inbt", 70, -20)
            call KittyFace("angry")          
            call Statup("Kitty", "Obed", 70, 30)
    return
    
# End Kitty Undressing  ///////////////////////////////////////////////////////////////////

    

label Kitty_First_Peen(Silent = 0, Undress = 0, Second = 0, React = 0): 
    #checked each time she sees your cock  ## call Kitty_First_Peen(0,1)
    #if Silent it doesn't say anything
    #if Undress then you get nude
    #if Secondary then this is the second girl to see it.
    # React 0 if other girl didn't comment, 
    # 1 = if the other girl commented, 2 = didn't like it
    
    if K_Loc != bg_current:
                if Partner == "Kitty":
                        $ Partner = 0
                return
    if "cockout" in P_RecentActions and "peen" in K_RecentActions: 
                #If the cock is already out and she's seen it, return
                return
            
    $ K_RecentActions.append("peen")                      
    $ K_DailyActions.append("peen")
    $ K_SeenPeen += 1                      
    call Statup("Kitty", "Inbt", 30, 2) 
    call Statup("Kitty", "Inbt", 80, 1)
    
    if Second:
        #If another girl commented on it first. . .
        if K_SeenPeen == 1: 
                call KittyFace("surprised", 2)  
                ch_k "Oh, wow, you aren't kidding. . ."
                call KittyFace("bemused", 1)  
        elif Second == 1:
                if not ApprovalCheck("Kitty", 800) and not ApprovalCheck("Kitty", 500, "I"):
                    call KittyFace("sad", 1) 
                    ch_k "I mean I guess. . ."
                else:
                    call KittyFace("bemused", 1)  
                    ch_k "I know, right?!"
        elif Second == 2:
                # The other girl didn't like it
                if not ApprovalCheck("Kitty", 800) and not ApprovalCheck("Kitty", 500, "I"):
                    call KittyFace("sad", 1)  
                    ch_k "So over it. . ."
                else:
                    call KittyFace("confused", 1)  
                    ch_k "Come on, it's really cute!"
                    call KittyFace("smile", 1)  
        $ Silent = 1
        
    if Undress:
        $ P_RecentActions.append("naked")    
    if not Silent:        
        if "cockout" in P_RecentActions:
                call KittyFace("down", 2)  
                "Kitty glances down at your exposed cock"
        elif React:
                #If called by a sex dialog
                "Kitty grabs your pants and pulls out your cock."
        elif Undress:
                "You strip nude."
        else:
                "You whip your cock out."
        if "cockout" not in P_RecentActions:
                $ P_RecentActions.append("cockout")   
        if not ApprovalCheck("Kitty", 800) and not ApprovalCheck("Kitty", 500, "I"):
                call KittyFace("surprised", 2)  
                ch_k "Huh?!"
                call KittyFace("angry", 1)  
                $ K_RecentActions.append("angry")
                $ K_DailyActions.append("angry")  
                if K_SeenPeen == 1: 
                    call Statup("Kitty", "Love", 90, -25)                
                    call Statup("Kitty", "Obed", 50, 35)
                    call Statup("Kitty", "Inbt", 60, 20)
                else:                    
                    ch_k "Dude, seriously, you've got a problem!"
                    if Action_Check("Kitty", "daily", "peen") >= 2:
                            #if she's seen more than one peen today         
                            call Statup("Kitty", "Love", 90, -1)     
                            call Statup("Kitty", "Obed", 50, 2)
                            call Statup("Kitty", "Inbt", 60, 2)
                    else:
                            call Statup("Kitty", "Love", 90, -5)                
                            call Statup("Kitty", "Obed", 50, 12)
                            call Statup("Kitty", "Inbt", 60, 10)      
                $ React = 2                       
        elif Taboo > 20 and (not ApprovalCheck("Kitty", 1500) or K_SEXP < 10) and bg_current != "bg showerroom":
                call KittyFace("surprised", 2)  
                ch_k "Um, you should[K_like]put that away in public."
                call KittyFace("bemused", 1)   
                $ React = 2
                if K_SeenPeen == 1: 
                    ch_k "Or[K_like]maybe. . ."
                    call Statup("Kitty", "Love", 90, 15)                
                    call Statup("Kitty", "Obed", 50, 20)
                    call Statup("Kitty", "Inbt", 60, 35)  
                    $ React = 1                  
        elif K_SeenPeen > 10:
                return 0   
        elif ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "L"):
                call KittyFace("sly",1) 
                if K_SeenPeen == 1: 
                    call KittyFace("surprised",2)  
                    ch_k "That's. . . impressive."
                    call KittyFace("bemused",1)  
                    call Statup("Kitty", "Love", 90, 3) 
                elif K_SeenPeen == 2:  
                    ch_k "I can't get over that."               
                    call Statup("Kitty", "Obed", 50, 7) 
                elif K_SeenPeen == 5: 
                    ch_k "There it is."
                    call Statup("Kitty", "Inbt", 60, 5)  
                elif K_SeenPeen == 10: 
                    ch_k "So beautiful."
                    call Statup("Kitty", "Obed", 80, 10)
                    call Statup("Kitty", "Inbt", 60, 3)   
                $ React = 1
        else:
                call KittyFace("sad",1) 
                if K_SeenPeen == 1: 
                    call KittyFace("perplexed",1 ) 
                    ch_k "Well that happened. . ."
                    call Statup("Kitty", "Obed", 50, 7)
                    call Statup("Kitty", "Inbt", 60, 3)  
                elif K_SeenPeen < 5: 
                    call KittyFace("sad",0) 
                    ch_k "Huh."
                    call Statup("Kitty", "Inbt", 60, 2)  
                elif K_SeenPeen == 10: 
                    ch_k "[K_Like]put that away."               
                    call Statup("Kitty", "Obed", 50, 7)
                    call Statup("Kitty", "Inbt", 60, 3) 
                $ React = 2  
    
    else: #Silent mode
                $ P_RecentActions.append("cockout") 
                if K_SeenPeen > 10:
                    return 0
                elif ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "L"):
                        if K_SeenPeen == 1: 
                            call Statup("Kitty", "Love", 90, 3) 
                        elif K_SeenPeen == 2:              
                            call Statup("Kitty", "Obed", 50, 7) 
                        elif K_SeenPeen == 5: 
                            call Statup("Kitty", "Inbt", 60, 5)  
                        elif K_SeenPeen == 10: 
                            call Statup("Kitty", "Love", 90, 10)  
                else:
                        if K_SeenPeen == 1: 
                            call Statup("Kitty", "Obed", 50, 7)
                            call Statup("Kitty", "Inbt", 60, 3)  
                        elif K_SeenPeen < 5: 
                            call Statup("Kitty", "Inbt", 60, 2)  
                        elif K_SeenPeen == 10:              
                            call Statup("Kitty", "Obed", 50, 7)
                            call Statup("Kitty", "Inbt", 60, 3) 
                            
    if K_SeenPeen == 1 and "angry" not in K_RecentActions:           
        call Statup("Kitty", "Love", 90, 10)                
        call Statup("Kitty", "Obed", 90, 25)
        call Statup("Kitty", "Inbt", 60, 20) 
        call Statup("Kitty", "Lust", 200, 5)
    
    call KittyFace("sly",1)  
    return React
    # End Kitty shown peen
    