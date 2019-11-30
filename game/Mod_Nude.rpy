label  Mod_Nude(Girl = "Kitty"):
   
    if Day <= 3:
        return
    $ Roll = renpy.random.randint(1, 3)
    if Roll != 2: # 1/3 chance of getting a nude from this girl
        return

    if Girl == "Kitty" and K_SEXP:
        # Current_Time #morning, midday, evening or night
        if K_NudeCurrent_Time != Current_Time:  #checks if a nude event for this girl already happened  at this time of day
            $ K_NudeCurrent_Time = Current_Time
        else:
            return
        if K_NudeDay != Day:  #checks if a nude event for this girl already happened today
            $ K_NudeDay = Day
        else:
            return
    
        $ Roll_ = renpy.random.randint(1,2)
        $ K_Nude_Overlay = renpy.random.randint(0,1)
        $ K_OverTemp = K_Over
        $ K_ChestTemp = K_Chest
        $ K_LegsTemp = K_Legs
        $ K_PantiesTemp = K_Panties
        $ P_SpriteTemp = P_Sprite
        $ P_CockTemp = P_Cock
        $ P_Sprite = 0
        $ P_Cock = 0
        
        if ApprovalCheck("Kitty", 1300) or (K_SeenChest and K_SeenPussy and not Taboo):
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 5)                
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 10)   
            $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 80, 15)    
            #$ Line = K_Over
            $ K_Over = 0
            $ K_Chest = 0
            $ K_Legs = 0
            $ K_Panties = 0
            if not K_SeenChest and Roll_:
                call KittyFace("bemused", 1)
                # $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                              
                # $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 4)
                # $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3)
                # $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 3)  
                #"She hesitantly glances your way, and then with tug her [Line] passes through her, tossing it to the ground."   
                call Kitty_First_Topless(1)
            if not K_SeenPussy:
                call KittyFace("bemused", 1)
                # $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                              
                # $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 4)
                # $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3)
                # $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 3)  
                #"She hesitantly glances your way, and then with tug her [Line] passes through her, tossing it to the ground."   
                call Kitty_First_Bottomless(1)
            #else: 
            #    "She pulls her [Line] over her head, tossing it to the ground." 
            if Roll_ == 1:    
                show Nude_Kitty zorder 200
            else:
                show Nude_Kitty_Doggy zorder 200

            "Kitty sent you a picture"
            ch_k "It's hot huh, [K_Petname]?" 
        elif (ApprovalCheck("Kitty", 1000) or (K_SeenChest and not Taboo)) and K_Chest != 0:
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 5)                
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 1)
            $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 80, 15)      
            #$ Line = K_Chest
            $ K_Over = 0   
            if not K_SeenChest and Roll_:
                call KittyFace("bemused", 1)
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                              
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 4)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 3)   
                #"She hesitantly glances your way, and then with a shrug pulls her [Line] through herself, tossing it to the ground."
                #call Kitty_First_Topless(1)
            if Roll_ == 1:    
                show Nude_Kitty zorder 200
            else:
                show Nude_Kitty_Doggy zorder 200

            "Kitty sent you a picture" 
    
        elif ApprovalCheck("Kitty", 600):
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 5)                
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 1)
            $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 80, 15)
            if Roll_ == 1:    
                show Nude_Kitty zorder 200
            else:
                show Nude_Kitty_Doggy zorder 200

            "Kitty sent you a picture" 
            ch_k "What do you think of this look, [K_Petname]?" 
        
    
        if Roll_ == 1:
            hide Nude_Kitty
        else:
            hide Nude_Kitty_Doggy
        $ K_Over = K_OverTemp
        $ K_Chest = K_ChestTemp
        $ K_Legs = K_LegsTemp
        $ K_Panties = K_PantiesTemp
        $ P_Sprite = P_SpriteTemp
        $ P_Cock = P_CockTemp

    elif Girl == "Rogue" and R_SEXP:
        # Current_Time #morning, evening or night
        if R_NudeCurrent_Time != Current_Time:  #checks if a nude event for this girl already happened  at this time of day
            $ R_NudeCurrent_Time = Current_Time
        else:
            return
        if R_NudeDay != Day:  #checks if a nude event for this girl already happened today
            $ R_NudeDay = Day
        else:
            return
    
        $ Roll_ = renpy.random.randint(1,2)
        $ R_Nude_Overlay = renpy.random.randint(0,1)
        $ R_OverTemp = R_Over
        $ R_ChestTemp = R_Chest
        $ R_LegsTemp = R_Legs
        $ R_HoseTemp = R_Hose
        $ R_PantiesTemp = R_Panties
        $ P_SpriteTemp = P_Sprite
        $ P_CockTemp = P_Cock
        $ P_Sprite = 0
        $ P_Cock = 0
        
        if ApprovalCheck("Rogue", 1400) or (R_SeenChest and R_SeenPussy and not Taboo):
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 60, 5)                
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 10)   
            $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 80, 15)    
            #$ Line = R_Over
            $ R_Over = 0
            $ R_Chest = 0
            $ R_Legs = 0
            $ R_Hose = 0
            $ R_Panties = 0
            if not R_SeenChest and Roll_:
                call RogueFace("bemused", 1)
                call Rogue_First_Topless(1)
            if not R_SeenPussy:
                call RogueFace("bemused", 1)
                call Rogue_First_Bottomless(1)
            if Roll_ == 1:    
                show Nude_Rogue zorder 200
            else:
                show Nude_Rogue_Doggy zorder 200

            "Rogue sent you a picture"
            ch_r "It's hot huh, [R_Petname]?" 
        elif (ApprovalCheck("Rogue", 1100) or (R_SeenChest and not Taboo)) and R_Chest != 0:
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 60, 5)                
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 1)
            $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 80, 15)      
            $ R_Over = 0                        
            if not R_SeenChest and Roll_:
                call RogueFace("bemused", 1)
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)                              
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 4)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 3)   
            if Roll_ == 1:    
                show Nude_Rogue zorder 200
            else:
                show Nude_Rogue_Doggy zorder 200

            "Rogue sent you a picture" 
    
        elif ApprovalCheck("Rogue", 600):
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 60, 5)                
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 1)
            $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 80, 15)
            if Roll_ == 1:    
                show Nude_Rogue zorder 200
            else:
                show Nude_Rogue_Doggy zorder 200

            "Rogue sent you a picture" 
            ch_r "What do you think of this look, [R_Petname]?" 
        
    
    
        if Roll_ == 1:
            hide Nude_Rogue
        else:
            hide Nude_Rogue_Doggy
        $ R_Over = R_OverTemp
        $ R_Chest = R_ChestTemp
        $ R_Legs = R_LegsTemp
        $ R_Hose = R_HoseTemp
        $ R_Panties = R_PantiesTemp
        $ P_Sprite = P_SpriteTemp
        $ P_Cock = P_CockTemp

    elif Girl == "Emma" and E_SEXP:
        # Current_Time #morning, evening or night
        if E_NudeCurrent_Time != Current_Time:  #checks if a nude event for this girl already happened  at this time of day
            $ E_NudeCurrent_Time = Current_Time
        else:
            return
        if E_NudeDay != Day:  #checks if a nude event for this girl already happened today
            $ E_NudeDay = Day
        else:
            return
    
        $ Roll_ = renpy.random.randint(1,2)
        $ E_Nude_Overlay = renpy.random.randint(0,1)
        $ E_OverTemp = E_Over
        $ E_ChestTemp = E_Chest
        $ E_LegsTemp = E_Legs
        $ E_HoseTemp = E_Hose
        $ E_PantiesTemp = E_Panties
        $ P_SpriteTemp = P_Sprite
        $ P_CockTemp = P_Cock
        $ P_Sprite = 0
        $ P_Cock = 0
        
        if ApprovalCheck("Emma", 1400) or (E_SeenChest and E_SeenPussy and not Taboo):
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5)                
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 10)   
            $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 80, 15)    
            #$ Line = E_Over
            $ E_Over = 0
            $ E_Chest = 0
            $ E_Legs = 0
            $ E_Hose = 0
            $ E_Panties = 0
            if not E_SeenChest and Roll_:
                call EmmaFace("bemused", 1)
                call Emma_First_Topless(1)
            if not E_SeenPussy:
                call EmmaFace("bemused", 1)
                call Emma_First_Bottomless(1)
            if Roll_ == 1:    
                show Nude_Emma zorder 200
            else:
                show Nude_Emma_Doggy zorder 200

            "Emma sent you a picture"
            ch_e "It's hot huh, [E_Petname]?" 
        elif (ApprovalCheck("Emma", 1100) or (E_SeenChest and not Taboo)) and E_Chest != 0:
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5)                
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 1)
            $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 80, 15)      
            $ E_Over = 0                        
            if not E_SeenChest and Roll_:
                call EmmaFace("bemused", 1)
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                              
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 4)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 3)   
            if Roll_ == 1:    
                show Nude_Emma zorder 200
            else:
                show Nude_Emma_Doggy zorder 200

            "Emma sent you a picture" 
    
        elif ApprovalCheck("Emma", 600):
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5)                
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 1)
            $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 80, 15)
            if Roll_ == 1:    
                show Nude_Emma zorder 200
            else:
                show Nude_Emma_Doggy zorder 200

            "Emma sent you a picture" 
            ch_e "What do you think of this look, [E_Petname]?" 
        
    
    
        if Roll_ == 1:
            hide Nude_Emma
        else:
            hide Nude_Emma_Doggy
        $ E_Over = E_OverTemp
        $ E_Chest = E_ChestTemp
        $ E_Legs = E_LegsTemp
        $ E_Hose = E_HoseTemp
        $ E_Panties = E_PantiesTemp
        $ P_Sprite = P_SpriteTemp
        $ P_Cock = P_CockTemp

    elif Girl == "Laura" and L_SEXP:
        # Current_Time #morning, evening or night
        if L_NudeCurrent_Time != Current_Time:  #checks if a nude event for this girl already happened  at this time of day
            $ L_NudeCurrent_Time = Current_Time
        else:
            return
        if L_NudeDay != Day:  #checks if a nude event for this girl already happened today
            $ L_NudeDay = Day
        else:
            return
    
    
        $ L_OverTemp = L_Over
        $ L_ChestTemp = L_Chest
        $ L_LegsTemp = L_Legs
        $ L_HoseTemp = L_Hose
        $ L_PantiesTemp = L_Panties
        $ P_SpriteTemp = P_Sprite
        $ P_CockTemp = P_Cock
        $ SpeedTemp = Speed
        $ Speed = 0
        $ P_Sprite = 0
        $ P_Cock = 0
        
        if ApprovalCheck("Laura", 1400) or (L_SeenChest and L_SeenPussy and not Taboo):
            $ L_Lust = Statupdate("Laura", "Lust", L_Lust, 60, 5)                
            $ L_Obed = Statupdate("Laura", "Obed", L_Obed, 50, 2)
            $ L_Inbt = Statupdate("Laura", "Inbt", L_Inbt, 50, 10)   
            $ P_Focus = Statupdate("Laura", "Focus", P_Focus, 80, 15)    
            #$ Line = L_Over
            $ L_Over = 0
            $ L_Chest = 0
            $ L_Legs = 0
            $ L_Hose = 0
            $ L_Panties = 0
            if not L_SeenChest:
                call LauraFace("bemused", 1)
                call Laura_First_Topless(1)
            if not L_SeenPussy:
                call LauraFace("bemused", 1)
                call Laura_First_Bottomless(1)
            show Nude_Laura zorder 200
            "Laura sent you a picture"
            ch_l "It's hot huh, [L_Petname]?" 
        elif (ApprovalCheck("Laura", 1100) or (L_SeenChest and not Taboo)) and L_Chest != 0:
            $ L_Lust = Statupdate("Laura", "Lust", L_Lust, 60, 5)                
            $ L_Obed = Statupdate("Laura", "Obed", L_Obed, 50, 2)
            $ L_Inbt = Statupdate("Laura", "Inbt", L_Inbt, 50, 1)
            $ P_Focus = Statupdate("Laura", "Focus", P_Focus, 80, 15)      
            $ L_Over = 0                        
            if not L_SeenChest:
                call LauraFace("bemused", 1)
                $ L_Obed = Statupdate("Laura", "Obed", L_Obed, 50, 3)                              
                $ L_Obed = Statupdate("Laura", "Obed", L_Obed, 200, 4)
                $ L_Inbt = Statupdate("Laura", "Inbt", L_Inbt, 50, 3)
                $ L_Inbt = Statupdate("Laura", "Inbt", L_Inbt, 200, 3)   
            show Nude_Laura zorder 200
            "Laura sent you a picture" 
    
        elif ApprovalCheck("Laura", 600):
            $ L_Lust = Statupdate("Laura", "Lust", L_Lust, 60, 5)                
            $ L_Obed = Statupdate("Laura", "Obed", L_Obed, 50, 2)
            $ L_Inbt = Statupdate("Laura", "Inbt", L_Inbt, 50, 1)
            $ P_Focus = Statupdate("Laura", "Focus", P_Focus, 80, 15)
            show Nude_Laura zorder 200
            "Laura sent you a picture" 
            ch_l "What do you think of this look, [L_Petname]?" 
        
    
    
        hide Nude_Laura
        $ L_Over = L_OverTemp
        $ L_Chest = L_ChestTemp
        $ L_Legs = L_LegsTemp
        $ L_Hose = L_HoseTemp
        $ L_Panties = L_PantiesTemp
        $ P_Sprite = P_SpriteTemp
        $ P_Cock = P_CockTemp
        $ Speed = SpeedTemp

    return

#front nude

image Nude_Kitty_Body:
    contains:
        "Kitty_SexSprite"
        ypos 150
        zoom 1.1

image Nude_Kitty:
    contains:
        "images/Nude/Nude_Sex_Background.png"
    contains:
        AlphaMask("Nude_Kitty_Body","images/Nude/Nude_Sex_Mask.png")
    contains:
        "images/Nude/Nude_Sex.png"
    xpos 450

image Nude_Rogue_Body:
    contains:
        "Rogue_SexSprite"
        ypos 150
        zoom 1.1

image Nude_Rogue:
    contains:
        "images/Nude/Nude_Sex_Background.png"
    contains:
        AlphaMask("Nude_Rogue_Body","images/Nude/Nude_Sex_Mask.png")
    contains:
        "images/Nude/Nude_Sex.png"
    xpos 450

image Nude_Emma_Body:
    contains:
        "Emma_Missionary"
        ypos 150
        zoom 1.1

image Nude_Emma:
    contains:
        "images/Nude/Nude_Sex_Background.png"
    contains:
        AlphaMask("Nude_Emma_Body","images/Nude/Nude_Sex_Mask.png")
    contains:
        "images/Nude/Nude_Sex.png"
    xpos 450


image Nude_Laura_Body:
    contains:
        "Nude_Laura_Body_"
        xpos 400
        ypos 300
        zoom 1.2

image Nude_Laura_Body_:
    contains:
        "Nude_Laura_Body__"
        # xpos 350
        # ypos 300
        # zoom 1.1
    contains:
        "Nude_Laura_Legs__"
        # xpos 350
        # ypos 300
        # zoom 1.1
    zoom .6 #0.6
    transform_anchor True
    anchor (.5,.5)

image Nude_Laura_Body__:
    contains:
        "Laura_Sex_Body"      
        subpixel True       
        pos (0,0) #top (0,-10)

image Nude_Laura_Legs__:
    contains:
        "Laura_Sex_Legs"
        subpixel True
        pos (0,0) #top

image Nude_Laura:
    contains:
        "images/Nude/Nude_Sex_Background.png"
    contains:
        AlphaMask("Nude_Laura_Body","images/Nude/Nude_Sex_Mask.png")
    contains:
        "images/Nude/Nude_Sex.png"
    xpos 450



#doggy nude
image Nude_Kitty_Body_Doggy:
    contains:
        "Kitty_Doggy_Body"
        xpos -40
        ypos -150
        zoom 1.2
    contains:
        "Kitty_Doggy_Ass"
        xpos -40
        ypos -150
        zoom 1.2

image Nude_Kitty_Doggy:
    contains:
        "images/Nude/Nude_Doggy_Background.png"
    contains:
        AlphaMask("Nude_Kitty_Body_Doggy","images/Nude/Nude_Doggy_Mask.png")
        # "Nude_Kitty_Body_Doggy"
    contains:
        "images/Nude/Nude_Doggy_Overlay" + str(K_Nude_Overlay) + ".png"
    contains:
        "images/Nude/Nude_Doggy.png"
    xpos 850
    ypos 800

image Nude_Rogue_Body_Doggy:
    contains:
        "Rogue_Doggy_Body"
        xpos -40
        ypos -150
        zoom 1.2
    contains:
        "Rogue_Doggy_Ass"
        xpos -40
        ypos -150
        zoom 1.2

image Nude_Rogue_Doggy:
    contains:
        "images/Nude/Nude_Doggy_Background.png"
    contains:
        AlphaMask("Nude_Rogue_Body_Doggy","images/Nude/Nude_Doggy_Mask.png")
        # "Nude_Kitty_Body_Doggy"
    contains:
        "images/Nude/Nude_Doggy_Overlay" + str(R_Nude_Overlay) + ".png"
    contains:
        "images/Nude/Nude_Doggy.png"
    xpos 850
    ypos 800


image Nude_Emma_Body_Doggy:
    contains:
        "Emma_Doggy_Body"
        xpos -40
        ypos -150
        zoom 1.2
    contains:
        "Emma_Doggy_Ass"
        xpos -40
        ypos -150
        zoom 1.2

image Nude_Emma_Doggy:
    contains:
        "images/Nude/Nude_Doggy_Background.png"
    contains:
        AlphaMask("Nude_Emma_Body_Doggy","images/Nude/Nude_Doggy_Mask.png")
        # "Nude_Kitty_Body_Doggy"
    contains:
        "images/Nude/Nude_Doggy_Overlay" + str(E_Nude_Overlay) + ".png"
    contains:
        "images/Nude/Nude_Doggy.png"
    xpos 850
    ypos 800
