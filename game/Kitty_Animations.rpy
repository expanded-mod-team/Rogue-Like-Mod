﻿# Basic Kitty Sprites
       
image Kitty_Sprite:        
    LiveComposite(
        (480,960),                                                                    
        (124,0), ConditionSwitch(
            "renpy.showing('Kitty_BJ_Animation')", Null(),
            "True", "Kitty_HairBack",   
            ),         
        (0,0), ConditionSwitch(                                                                         
            #Arms1               
            "not Kitty_Arms and K_DynamicTan[0]", "images/KittySprite/Kitty_Sprite_T3Arms1.png",
            "not Kitty_Arms", "images/KittySprite/Kitty_Sprite_Arms1.png",
            "True", Null(),               
            ), 
        (0,0), ConditionSwitch(                                                                        
            "not K_DynamicTan[3] or Kitty_Arms or not K_DynamicTan[0]", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", GetModdedStringTanKitty("3", "1.png")),
            ),
        
        (0,0), ConditionSwitch(   
            "not K_DynamicTan[1] or Kitty_Arms or not K_DynamicTan[0]", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", GetModdedStringTanKitty("1", "1.png")),
            ),
        (0,0), ConditionSwitch(               #back of the shirt
            "not K_Over", Null(),
            "Kitty_Arms and 'modded' in K_Over and 'top' in K_Over", GetModdedString("images/KittySprite/Kitty_Sprite_Under_", K_Over, "2.png"),
            "'modded' in K_Over and 'top' in K_Over", GetModdedString("images/KittySprite/Kitty_Sprite_Under_", K_Over, "1.png"),
            "K_Over == 'pink top' and Kitty_Arms", "images/KittySprite/Kitty_Sprite_Under_Pink2.png",       #2
            "K_Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Under_Pink1.png",                  #1
            "True", Null(),               
            ),
        (0,0), ConditionSwitch(                                                                         
            #body
            "Kitty_Arms and K_DynamicTan[0]", "images/KittySprite/Kitty_Sprite_T3Body_Bare2.png",               
            "Kitty_Arms", "images/KittySprite/Kitty_Sprite_Body_Bare2.png",               
            "True and K_DynamicTan[0]", "images/KittySprite/Kitty_Sprite_T3Body_Bare1.png",    
            "True", "images/KittySprite/Kitty_Sprite_Body_Bare1.png",    
            ),
        (0,0), ConditionSwitch(                                                                     #body
            "not K_DynamicTan[3] or not K_DynamicTan[0]", Null(),
            "Kitty_Arms", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", GetModdedStringTanKitty("3", "2.png")),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", GetModdedStringTanKitty("3", "1.png")),
            ),

        (0,0), ConditionSwitch(                                                                     #body
            "not K_DynamicTan[4] or not K_DynamicTan[0]", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", GetModdedStringTanKitty("4", ".png")),
            ),

        (0,0), ConditionSwitch(                                                                     #body
            "not K_DynamicTan[5] or not K_DynamicTan[0]", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", GetModdedStringTanKitty("5", ".png")),
            ),

        (0,0), ConditionSwitch(                                                                     #body
            "not K_DynamicTan[2] or not K_DynamicTan[0]", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", GetModdedStringTanKitty("2", ".png")),
            ),

        (0,0), ConditionSwitch(   
            "not K_DynamicTan[1] or not K_DynamicTan[0]", Null(),
            "Kitty_Arms", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", GetModdedStringTanKitty("1", "2.png")),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", GetModdedStringTanKitty("1", "1.png")),
            ),

        (0,0), ConditionSwitch(                                                                         #body
   
            "K_Pubes and K_HairColor == 'black'", "images/KittySprite/Kitty_Sprite_Body_Hair_PubesBlack.png",               
            "K_Pubes", "images/KittySprite/Kitty_Sprite_Body_Hair_Pubes.png",               
            "True", Null(),  
            ),#            #wet look
        (0,0), ConditionSwitch(                                                                         
            #piercings bottom
            "not K_Pierce or (K_Panties and not K_PantiesDown)", Null(),                       
            "K_Pierce == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingB.png",      
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallB.png",   
            ),    
        (0,0), ConditionSwitch(                                                                         
            #full hose/tights              
            "K_Panties and not K_PantiesDown", Null(), 
            "not K_Hose", Null(),
            "'modded' in K_Hose", "images/KittySprite/Kitty_Sprite_hose_[K_Hose].png",
            "True", Null(), 
            ), 
        (0,0), ConditionSwitch(                                                                         
            #panties layer           
            "not K_Panties", Null(),               
            "K_Legs and not K_Upskirt and PantsNum('Kitty') != 5", Null(),
            "'modded' in K_Panties", "images/KittySprite/Kitty_Sprite_Panties_[K_Panties]_[K_PantiesDown]_[K_Wet].png",
            
            "not K_PantiesDown or (K_Legs and K_Legs != 'blue skirt' and not K_Upskirt)", ConditionSwitch( 
                    # if the panties aren't down. . .
                    # and she's not wearing pants that are up
                    "K_Wet", ConditionSwitch( 
                            # if they're up and wet. . .
                            # "'modded' in K_Panties", GetModdedString("images/KittySprite/Kitty_Sprite_Panties_", K_Panties, "_Wet.png"),
                            "K_Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Wet.png",
                            "K_Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Wet.png",     
                            "K_Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_Wet.png", 
                            "True", Null(),     
                            ),
                    "True", ConditionSwitch( 
                            #if they're just up. . .       
                            # "'modded' in K_Panties", GetModdedString("images/KittySprite/Kitty_Sprite_Panties_", K_Panties, ".png"),
                            "K_Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green.png",
                            "K_Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace.png",
                            "K_Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini.png", 
                            "True", Null(),     
                            ),    
                    ),                    
            "K_Wet", ConditionSwitch( 
                    #if wet and down. . .
                    # "'modded' in K_Panties", GetModdedString("images/KittySprite/Kitty_Sprite_Panties_", K_Panties, "_Down_Wet.png"),
                    "K_Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Down_Wet.png",
                    "K_Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Down_Wet.png",
                    "K_Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_DownW.png", 
                    "True", Null(),     
                    ),
            "True", ConditionSwitch(
                    # if not wet, but down
                    # "'modded' in K_Panties", GetModdedString("images/KittySprite/Kitty_Sprite_Panties_", K_Panties, "_Down.png"),
                    "K_Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Down.png",
                    "K_Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Down.png",
                    "K_Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_Down.png", 
                    "True", Null(),     
                    ),
            ),
        
        (225,560), ConditionSwitch(                                                                         
            #Personal Wetness            
            "not K_Wet", Null(),
            "K_Legs and not K_Upskirt", Null(),   
            "K_Panties and not K_PantiesDown and K_Wet <= 1", Null(),                   
            "K_Wet == 1", ConditionSwitch( #Wet = 1
                    "K_Panties and K_PantiesDown", AlphaMask("Wet_Drip","Kitty_Drip_MaskP"),  
                    "K_Legs", AlphaMask("Wet_Drip","Kitty_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip","Kitty_Drip_Mask"), #only plays if nothing is in the way
                    ),
            "True", ConditionSwitch( #Wet = 2+
                    "K_Panties and K_PantiesDown", AlphaMask("Wet_Drip2","Kitty_Drip_MaskP"), #"Wet_Drip2",# 
                    "K_Legs", AlphaMask("Wet_Drip2","Kitty_Drip_MaskP"),
                    "K_Panties", AlphaMask("Wet_Drip","Kitty_Drip_Mask"), #"Wet_Drip2",# 
                    "True", AlphaMask("Wet_Drip2","Kitty_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (0,0), ConditionSwitch(                                                                         
            #wetness                    
            "K_Legs or not K_Wet", Null(),             
            "K_Panties and not K_PantiesDown and K_Wet < 2", Null(),
            "K_Panties and not K_PantiesDown", "images/KittySprite/Kitty_Sprite_Wet1.png",
            "K_Wet == 2", "images/KittySprite/Kitty_Sprite_Wet2.png",
            "True", "images/KittySprite/Kitty_Sprite_Wet1.png",
            ),  
        (225,560), ConditionSwitch(                                                                         
            #Spunk nethers        
            "'in' not in K_Spunk and 'anal' not in K_Spunk", Null(),
            "K_Legs and not K_Upskirt", Null(),   
            "True", ConditionSwitch( #Wet = 2+
                    "K_Panties and K_PantiesDown", AlphaMask("Spunk_Drip2","Kitty_Drip_MaskP"), #"Wet_Drip2",# 
                    "K_Legs", AlphaMask("Spunk_Drip2","Kitty_Drip_MaskP"),
                    "True", AlphaMask("Spunk_Drip2","Kitty_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (0,0), ConditionSwitch(                                                                         
            #full hose/tights              
            "K_Panties and K_PantiesDown", Null(), 
            "not K_Hose", Null(),
            "'modded' in K_Hose", "images/KittySprite/Kitty_Sprite_Hose_[K_Hose].png",
            # "'modded' in K_Hose", GetModdedString("images/KittySprite/Kitty_Sprite_hose_", K_Hose, ".png"),
            "True", Null(), 
            ),     
        (0,0), ConditionSwitch(                                                                        
            #pants         
            "not K_Legs", Null(),
            "'modded' in K_Legs", "images/KittySprite/Kitty_Sprite_Legs_[K_Legs]_[K_Upskirt]_[K_Wet].png",

            "K_Legs == 'blue skirt' and K_Upskirt", "images/KittySprite/Kitty_Sprite_Skirt_Up.png",       
            "K_Legs == 'blue skirt'", "images/KittySprite/Kitty_Sprite_Skirt.png",          
            "not K_Legs", Null(),
            # "K_Upskirt and 'modded' in K_Legs", GetModdedString("images/KittySprite/Kitty_Sprite_Legs_", K_Legs, "_Down.png"),
            # "K_Wet and 'modded' in K_Legs", GetModdedString("images/KittySprite/Kitty_Sprite_Legs_", K_Legs, "_Wet.png"),
            # "'modded' in K_Legs", GetModdedString("images/KittySprite/Kitty_Sprite_Legs_", K_Legs, ".png"),
            "not K_Legs or K_Upskirt", Null(),
            #"'modded' in K_Legs and K_Upskirt", GetModdedString("images/KittySprite/Kitty_Sprite_Legs", K_Legs, ".png"),
            "K_Legs == 'capris'", "images/KittySprite/Kitty_Sprite_Pants_Blue.png",
            "K_Legs == 'black jeans'", "images/KittySprite/Kitty_Sprite_Pants_Black.png",
            "K_Wet and K_Legs == 'yoga pants'", "images/KittySprite/Kitty_Sprite_Pants_Yoga_Wet.png",   
            "K_Legs == 'yoga pants'", "images/KittySprite/Kitty_Sprite_Pants_Yoga.png",   
            "K_Wet and K_Legs == 'shorts'", "images/KittySprite/Kitty_Sprite_Shorts_Wet.png",    
            "K_Legs == 'shorts'", "images/KittySprite/Kitty_Sprite_Shorts.png",            
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(                                                                         
            #Arms2               
            "Kitty_Arms and K_DynamicTan[0]", "images/KittySprite/Kitty_Sprite_T3Arms2.png",
            "Kitty_Arms", "images/KittySprite/Kitty_Sprite_Arms2.png",
            "True", Null(),               
            ), 

        (0,0), ConditionSwitch(                                                                         #Arms2               
            "not K_DynamicTan[3] or not K_DynamicTan[0] or not Kitty_Arms", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Arms2.png", GetModdedStringTanKitty("3", "2.png")),
            ),

        (0,0), ConditionSwitch(   
            "not K_DynamicTan[1] or not K_DynamicTan[0] or not Kitty_Arms", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Arms2.png", GetModdedStringTanKitty("1", "2.png")),
            ),

        (0,0), ConditionSwitch(                                                                         #chest
            "True and K_DynamicTan[0]", "images/KittySprite/Kitty_Sprite_T3chest_bare.png",
            "True", "images/KittySprite/Kitty_Sprite_Chest_Bare.png",
            ),  
        (0,0), ConditionSwitch(                                                                     #body
            "not K_DynamicTan[3] or not K_DynamicTan[0]", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Chest_Bare.png", GetModdedStringTanKitty("3", "1.png")),
            ),

        (0,0), ConditionSwitch(   
            "not K_DynamicTan[1] or not K_DynamicTan[0]", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Chest_Bare.png", GetModdedStringTanKitty("1", "1.png")),
            ),#            #chest
        (0,0), ConditionSwitch(   
            #piercings top
            "not K_Pierce", Null(),                       
            "K_Pierce == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingT.png",      
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallT.png",   
            ),    
        (0,0), ConditionSwitch(                                                                        
            #necklace
            "K_Neck == 'gold necklace'", "images/KittySprite/Kitty_Sprite_Necklace1.png",
            "K_Neck == 'star necklace'", "images/KittySprite/Kitty_Sprite_Necklace2.png",
            "True", Null(),
            ),   
        (0,0), ConditionSwitch(                                                                         
            #bra layer           
            "not K_Chest", Null(),                  
            "not K_Uptop", ConditionSwitch( 
                    #if the top's down. . .
                    "Kitty_Arms and 'modded' in K_Chest", GetModdedString("images/KittySprite/Kitty_Sprite_Chest_", K_Chest, "2.png"),
                    "'modded' in K_Chest", GetModdedString("images/KittySprite/Kitty_Sprite_Chest_", K_Chest, "1.png"),
                    "Kitty_Arms and K_Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami2.png",
                    "Kitty_Arms and K_Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini2.png",
                    "K_Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini1.png",
                    "K_Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace.png",
                    "K_Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport.png",
                    "K_Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic.png",
                    "K_Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1.png",
                    "True", Null(),     
                    ),
            "K_Over", ConditionSwitch(
                    # If she's wearing a shirt over the bra                        
                    "K_Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini1_Up.png",
                    "K_Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace1_UpS.png",
                    "K_Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport1_UpS.png",
                    "K_Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic1_Up.png",
                    "K_Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1_UpS.png",    
                    "True", Null(),     
                    ),
            "True", ConditionSwitch(
                    # if she's not wearing a shirt
                    "Kitty_Arms", ConditionSwitch(
                            # if Arms 2
                            "K_Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini2_Up.png",
                            "K_Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace2_Up.png",
                            "K_Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport2_Up.png",
                            "K_Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic2_Up.png",
                            "K_Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami2_Up.png",            
                            "True", Null(),     
                            ),                    
                    "True", ConditionSwitch(
                            # if Arms 1
                            "K_Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini1_Up.png",
                            "K_Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace1_Up.png",
                            "K_Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport1_Up.png",
                            "K_Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic1_Up.png",
                            "K_Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1_Up.png",            
                            "True", Null(),     
                            ),            
                    "True", Null(),     
                    ),
            ),
            
        (0,0), ConditionSwitch(                                                                        
            #piercings over shirt
            "not K_Pierce or not K_Chest or K_Uptop", Null(),                       
            "K_Pierce == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingOver.png",      
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallOver.png",   
            ),    
        (0,0), ConditionSwitch(                                                                        
            #wet look
            "K_Water and Kitty_Arms", "images/KittySprite/Kitty_Sprite_Water2.png",
            "K_Water", "images/KittySprite/Kitty_Sprite_Water1.png",
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                         
            #shirt layer           
            "not K_Over", Null(),                  
            "not K_Uptop", ConditionSwitch( 
                    #if the top's down. . .
                    "Kitty_Arms and 'modded' in K_Over", GetModdedString("images/KittySprite/Kitty_Sprite_Over_", K_Over, "2.png"),
                    "'modded' in K_Over", GetModdedString("images/KittySprite/Kitty_Sprite_Over_", K_Over, "1.png"),
                    "Kitty_Arms and K_Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink2.png",
                    "Kitty_Arms and K_Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew2.png",
                    "Kitty_Arms and K_Over == 'towel'", "images/KittySprite/Kitty_Sprite_Over_Towel2.png",
                    "K_Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink1.png",
                    "K_Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew1.png",
                    "K_Over == 'towel'", "images/KittySprite/Kitty_Sprite_Over_Towel1.png",
                    "True", Null(),     
                    ),            
            "True", ConditionSwitch(
                    # if she's not wearing a shirt                    
                    "Kitty_Arms and K_Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink2_Up.png",
                    "Kitty_Arms and K_Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew2_Up.png",
                    "K_Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink1_Up.png",
                    "K_Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew1_Up.png",            
                    "True", Null(),     
                    ),
            ),
            
        (0,0), ConditionSwitch(                                                                         
            #bra over shirt layer           
            "not K_Over or not K_Chest or not K_Uptop", Null(),   
            "K_Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami_Over.png", 
            "K_Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace_Over.png",
            "K_Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport_Over.png",
            "K_Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic_Over.png",
            "K_Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini_Over.png",
            "True", Null(),  
            ),
            
        (124,0), ConditionSwitch(
            "renpy.showing('Kitty_BJ_Animation')", Null(),
            "True", "Kitty_Head",   
            ), 
        
        (0,0), ConditionSwitch(                                                                        
            #anal spunk
            "K_Legs and not K_Upskirt", Null(), 
            "K_Panties and not K_PantiesDown", Null(), 
            "'anal' in K_Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Anal.png",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(                                                                        
            #pussy spunk
            "K_Legs and not K_Upskirt", Null(), 
            "K_Panties and not K_PantiesDown", Null(), 
            "'in' in K_Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Pussy.png",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(                                                                         
            #belly spunk
            "'belly' in K_Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Belly.png",
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(                                                                         
            #tits spunk
            "'tits' in K_Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Tits.png",
            "True", Null(), 
            ),   
            
        (0,0), ConditionSwitch(
            #UI tool for When Kitty is masturbating using Trigger3 actions
            "Trigger == 'lesbian' or not Trigger3 or Ch_Focus != 'Kitty'", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and K_Lust >= 70", "GirlFingerPussy_K",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_K",            
            "Trigger3 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeLeftBreast_K",    #When zero is working the right breast, fondle left
            "Trigger3 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeRightBreast_K", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts'", "GirlGropeRightBreast_K",
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast_K",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy_K",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy_K",
            "Trigger3 == 'vibrator anal'", "VibratorAnal_K",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy_K",            
            "True", Null(),             
            ),                        
        (0,0), ConditionSwitch(  
            #UI tool for Trigger5(Threesome masutrbation) actions
            "not Trigger5 or Trigger4 != 'masturbation' or Ch_Focus == 'Kitty'", Null(), 
            #this doesn't activate unless Kitty is not primary, and actively masturbating
            "Trigger5 == 'fondle pussy' and Trigger != 'sex' and K_Lust >= 70", "GirlFingerPussy_K",
            "Trigger5 == 'fondle pussy'", "GirlGropePussy_K",
            "Trigger5 == 'fondle breasts'", "GirlGropeRightBreast_K",
            "Trigger5 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger5 == 'vibrator pussy'", "VibratorPussy",
            "Trigger5 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger5 == 'vibrator anal'", "VibratorAnal",
            "Trigger5 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(), 
            ),               
        (0,0), ConditionSwitch(                
            #UI tool for Trigger1(primary) actions
            "not Trigger or Ch_Focus != 'Kitty'", Null(),
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast_K",
            "Trigger == 'fondle thighs'", "GropeThigh_K",
            "Trigger == 'fondle breasts'", "GropeLeftBreast_K",
            "Trigger == 'suck breasts'", "LickRightBreast_K",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_K",
            "Trigger == 'fondle pussy'", "GropePussy_K",
            "Trigger == 'lick pussy'", "Lickpussy_K",
            "Trigger == 'vibrator pussy'", "VibratorPussy_K",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy_K",
            "Trigger == 'vibrator anal'", "VibratorAnal_K",
            "Trigger == 'vibrator anal insert'", "VibratorPussy_K",
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                
            #UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus != 'Kitty'", Null(),
            "not Trigger2 and not Trigger4 and Trigger == 'fondle breasts'", "GropeRightBreast_K",        
            #When doing nothing offhand, use both hands on breasts.
            "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast_K",            
            #When sucking right breast, fondle left
            "Trigger2 == 'fondle breasts'", "GropeRightBreast_K",
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast_K",       
            #When sucking right breast, vibrator left
            "Trigger2 == Trigger", Null(),
            #When both triggers are the same, do nothing              
            "Trigger2 == 'suck breasts'", "LickLeftBreast_K",        
            "Trigger2 == 'fondle pussy'", "GropePussy_K",
            "Trigger2 == 'lick pussy'", "Lickpussy_K",       
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast_K",
            "Trigger2 == 'vibrator pussy'", "VibratorPussy_K",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy_K",
            "Trigger2 == 'vibrator anal'", "VibratorAnal_K",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy_K",
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(  
            #UI tool for Trigger4(Threesome) actions (ie Rogue's hand on her)
            "not Trigger4 or Ch_Focus != 'Kitty'", Null(),
            "Trigger4 == 'fondle pussy' and Trigger != 'sex' and K_Lust >= 70", "GirlFingerPussy_K",
            "Trigger4 == 'fondle pussy'", "GirlGropePussy_K",            
            "Trigger4 == 'lick pussy'", "Lickpussy_K",
            "Trigger4 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_K", 
            "Trigger4 == 'suck breasts'", "LickRightBreast_K",  
            "Trigger4 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_K",    #When zero is working the right breast, fondle left
            "Trigger4 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_K", #When zero is working the left breast, fondle right  
            "Trigger4 == 'fondle breasts' and (Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts')", "GirlGropeLeftBreast_K", #When zero is working the left breast, fondle right  
            "Trigger4 == 'fondle breasts'", "GirlGropeRightBreast_K",
            "Trigger4 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger4 == 'vibrator pussy'", "VibratorPussy",
            "Trigger4 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger4 == 'vibrator anal'", "VibratorAnal",
            "Trigger4 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),             
            ),    
        (0,0), ConditionSwitch(  
            #UI tool for Trigger3(lesbian) actions (ie Rogue's hand on her when Kitty is secondary)
            "Trigger != 'lesbian' or not Trigger3 or Ch_Focus == 'Kitty'", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and K_Lust >= 70", "GirlFingerPussy_K",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_K",            
            "Trigger3 == 'lick pussy'", "Lickpussy_K",
            "Trigger3 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_K", 
            "Trigger3 == 'suck breasts'", "LickRightBreast_K",  
            "Trigger3 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_K",    #When zero is working the right breast, fondle left
            "Trigger3 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_K", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts' and (Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts')", "GirlGropeLeftBreast_K", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts'", "GirlGropeRightBreast_K",
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger3 == 'vibrator anal'", "VibratorAnal",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),             
            ),         
        )
    anchor (0.6, 0.0)
    zoom .75                      

image Kitty_Sprite_Desu:        
    LiveComposite(
        (480,960),                                                                    
        (124,0), ConditionSwitch(
            "renpy.showing('Kitty_BJ_Animation')", Null(),
            "True", "Kitty_HairBack",   
            ),         
        (0,0), ConditionSwitch(                                                                         
            #Arms1               
            "not Kitty_Arms and K_DynamicTan[0]", "images/KittySprite/Kitty_Sprite_T3Arms1.png",
            "not Kitty_Arms", "images/KittySprite/Kitty_Sprite_Arms1.png",
            "True", Null(),               
            ), 
        (0,0), ConditionSwitch(                                                                        
            "not K_DynamicTan[3] or Kitty_Arms or not K_DynamicTan[0]", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", GetModdedStringTanKitty("3", "1.png")),
            # "'modded' in K_DynamicTan[3]", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", GetModdedString("images/KittySprite/Kitty_Sprite_Chest_", K_DynamicTan[3], "1.png")),
            # "K_DynamicTan[3] == 'bikini top'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Bikini1.png"),
            # "K_DynamicTan[3] == 'lace bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Bra_Lace.png"),
            # "K_DynamicTan[3] == 'sports bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Bra_Sport.png"),
            # "K_DynamicTan[3] == 'bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Bra_Basic.png"),
            # "K_DynamicTan[3] == 'cami'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Cami1.png"),
            #"True", Null(),
            ),
        
        (0,0), ConditionSwitch(   
            "not K_DynamicTan[1] or Kitty_Arms or not K_DynamicTan[0]", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", GetModdedStringTanKitty("1", "1.png")),
            # "'modded' in K_DynamicTan[1]", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", GetModdedString("images/KittySprite/Kitty_Sprite_Over_", K_DynamicTan[1], "1.png")),
            # "K_DynamicTan[1] == 'pink top'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Over_Pink1.png"),
            # "K_DynamicTan[1] == 'red shirt'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Over_Crew1.png"),
            # "K_DynamicTan[1] == 'towel'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Over_Towel1.png"),
            # "True", Null(),
            ),
        (0,0), ConditionSwitch(               #back of the shirt
            "not K_Over", Null(),
            "Kitty_Arms and 'modded' in K_Over and 'top' in K_Over", GetModdedString("images/KittySprite/Kitty_Sprite_Under_", K_Over, "2.png"),
            "'modded' in K_Over and 'top' in K_Over", GetModdedString("images/KittySprite/Kitty_Sprite_Under_", K_Over, "1.png"),
            "K_Over == 'pink top' and Kitty_Arms", "images/KittySprite/Kitty_Sprite_Under_Pink2.png",       #2
            "K_Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Under_Pink1.png",                  #1
            "True", Null(),               
            ),
        (0,0), ConditionSwitch(                                                                         
            #body
            "Kitty_Arms and K_DynamicTan[0]", "images/KittySprite/Kitty_Sprite_T3Body_Bare2.png",               
            "Kitty_Arms", "images/KittySprite/Kitty_Sprite_Body_Bare2.png",               
            "True and K_DynamicTan[0]", "images/KittySprite/Kitty_Sprite_T3Body_Bare1.png",    
            "True", "images/KittySprite/Kitty_Sprite_Body_Bare1.png",    
            ),
        (0,0), ConditionSwitch(                                                                     #body
            "not K_DynamicTan[3] or not K_DynamicTan[0]", Null(),
            "Kitty_Arms", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", GetModdedStringTanKitty("3", "2.png")),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", GetModdedStringTanKitty("3", "1.png")),
            
            # "K_DynamicTan[0] and Kitty_Arms and 'modded' in K_DynamicTan[3]", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", GetModdedString("images/KittySprite/Kitty_Sprite_Chest_", K_DynamicTan[3], "2.png")),
            # "K_DynamicTan[0] and Kitty_Arms and K_DynamicTan[3] == 'bikini top'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_Bikini2.png"),
            # "K_DynamicTan[0] and Kitty_Arms and K_DynamicTan[3] == 'cami'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_Cami2.png"),
            
            # "K_DynamicTan[0] and 'modded' in K_DynamicTan[3]", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", GetModdedString("images/KittySprite/Kitty_Sprite_Chest_", K_DynamicTan[3], "1.png")),
            # "K_DynamicTan[0] and K_DynamicTan[3] == 'lace bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Bra_Lace.png"),
            # "K_DynamicTan[0] and K_DynamicTan[3] == 'sports bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Bra_Sport.png"),
            # "K_DynamicTan[0] and K_DynamicTan[3] == 'bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Bra_Basic.png"),
            # "K_DynamicTan[0] and K_DynamicTan[3] == 'cami'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Cami1.png"),
            # "True", Null(),
            ),

        (0,0), ConditionSwitch(                                                                     #body
            "not K_DynamicTan[4] or not K_DynamicTan[0]", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", GetModdedStringTanKitty("4", ".png")),
            # "K_DynamicTan[0] and 'modded' in K_DynamicTan[4]", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", GetModdedString("images/KittySprite/Kitty_Sprite_Chest_", K_DynamicTan[4], ".png")),
            # "K_DynamicTan[0] and K_DynamicTan[4] == 'bikini bottoms'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Panties_Bikini.png"),
            # "K_DynamicTan[0] and K_DynamicTan[4] == 'green panties'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Panties_Green.png"),
            # "K_DynamicTan[0] and K_DynamicTan[4] == 'lace panties'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Panties_Lace.png"),
            # "True", Null(),             
            ),

        (0,0), ConditionSwitch(                                                                     #body
            "not K_DynamicTan[5] or not K_DynamicTan[0]", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", GetModdedStringTanKitty("5", ".png")),
            ),

        (0,0), ConditionSwitch(                                                                     #body
            "not K_DynamicTan[2] or not K_DynamicTan[0]", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", GetModdedStringTanKitty("2", ".png")),
            # "K_DynamicTan[0] and 'modded' in K_DynamicTan[2]", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", GetModdedString("images/KittySprite/Kitty_Sprite_Legs_", K_DynamicTan[2], ".png")),
            # "K_DynamicTan[0] and K_DynamicTan[2] == 'blue skirt'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Skirt.png"),
            # "K_DynamicTan[0] and K_DynamicTan[2] == 'capris'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Pants_Blue.png"),
            # "K_DynamicTan[0] and K_DynamicTan[2] == 'black jeans'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Pants_Black.png"),
            # "K_DynamicTan[0] and K_DynamicTan[2] == 'yoga pants'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Pants_Yoga.png"),  
            # "K_DynamicTan[0] and K_DynamicTan[2] == 'shorts'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Shorts.png"),            
            # "True", Null(),             
            ),

        (0,0), ConditionSwitch(   
            "not K_DynamicTan[1] or not K_DynamicTan[0]", Null(),
            "Kitty_Arms", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", GetModdedStringTanKitty("1", "2.png")),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", GetModdedStringTanKitty("1", "1.png")),
            # "Kitty_Arms and K_DynamicTan[0] and 'modded' in K_DynamicTan[1]", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", GetModdedString("images/KittySprite/Kitty_Sprite_Over_", K_DynamicTan[1], "2.png")),
            # "Kitty_Arms and K_DynamicTan[0] and K_DynamicTan[1] == 'pink top'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_Over_Pink2.png"),
            # "Kitty_Arms and K_DynamicTan[0] and K_DynamicTan[1] == 'red shirt'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_Over_Crew2.png"),
            # "Kitty_Arms and K_DynamicTan[0] and K_DynamicTan[1] == 'towel'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_Over_Towel2.png"),
            # "K_DynamicTan[0] and 'modded' in K_DynamicTan[1]", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", GetModdedString("images/KittySprite/Kitty_Sprite_Over_", K_DynamicTan[1], "1.png")),
            # "K_DynamicTan[0] and K_DynamicTan[1] == 'pink top'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Over_Pink1.png"),
            # "K_DynamicTan[0] and K_DynamicTan[1] == 'red shirt'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Over_Crew1.png"),
            # "K_DynamicTan[0] and K_DynamicTan[1] == 'towel'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Over_Towel1.png"),
            # "True", Null(),
            ),

        (0,0), ConditionSwitch(                                                                         #body
   
            "K_Pubes and K_HairColor == 'black'", "images/KittySprite/Kitty_Sprite_Body_Hair_PubesBlack.png",               
            "K_Pubes", "images/KittySprite/Kitty_Sprite_Body_Hair_Pubes.png",               
            "True", Null(),  
            ),#            #wet look
#            "K_Water and Kitty_Arms", "images/KittySprite/Kitty_Sprite_Water2.png",
#            "K_Water", "images/KittySprite/Kitty_Sprite_Water1.png",
#            "True", Null(),
#            ),  
        (0,0), ConditionSwitch(                                                                         
            #piercings bottom
            "not K_Pierce or (K_Panties and not K_PantiesDown)", Null(),                       
            "K_Pierce == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingB.png",      
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallB.png",   
            ),    
        
#        (0,0), ConditionSwitch(                                                                         
#            #panties
#            "not K_Panties or K_PantiesDown", Null(),
#            "K_Legs or K_Upskirt", Null(), #If panties are down, and pants are either off or down, skip this
            
#            "not K_Panties or not K_PantiesDown", Null(), #If panties are not down or if  pants are on and up, skip this
#            "K_Legs and K_Legs != 'blue skirt' and not K_Upskirt", Null(), #If panties are not down or if  pants are on and up, skip this
            
#            "K_Wet and K_Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Wet.png",
#            "K_Wet and K_Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Wet.png",     
#            "K_Wet and K_Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_Wet.png",          
#            "K_Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green.png",
#            "K_Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace.png",
#            "K_Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini.png", 
#            "True", Null(),
#            ),  
#        (0,0), ConditionSwitch(                                                                         
#            #panties down
#            "not K_Panties or not K_PantiesDown", Null(), #If panties are not down or if  pants are on and up, skip this
#            "K_Legs and K_Legs != 'blue skirt' and not K_Upskirt", Null(), #If panties are not down or if  pants are on and up, skip this
#            "K_Wet and K_Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Down_Wet.png",
#            "K_Wet and K_Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Down_Wet.png",
#            "K_Wet and K_Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_DownW.png", 
#            "K_Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Down.png",
#            "K_Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Down.png",
#            "K_Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_Down.png", 
#            "True", Null(),
#            ),  
        (0,0), ConditionSwitch(                                                                         
            #full hose/tights              
            "K_Panties and not K_PantiesDown", Null(), 
            "not K_Hose", Null(),
            "'modded' in K_Hose", GetModdedString("images/KittySprite/Kitty_Sprite_hose_", K_Hose, ".png"),
            "True", Null(), 
            ), 
        (0,0), ConditionSwitch(                                                                         
            #panties layer           
            "not K_Panties", Null(),               
            "not K_PantiesDown or (K_Legs and K_Legs != 'blue skirt' and not K_Upskirt)", ConditionSwitch( 
                    # if the panties aren't down. . .
                    # and she's not wearing pants that are up
                    "K_Wet", ConditionSwitch( 
                            # if they're up and wet. . .
                            "'modded' in K_Panties", GetModdedString("images/KittySprite/Kitty_Sprite_Panties_", K_Panties, "_Wet.png"),
                            "K_Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Wet.png",
                            "K_Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Wet.png",     
                            "K_Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_Wet.png", 
                            "True", Null(),     
                            ),
                    "True", ConditionSwitch( 
                            #if they're just up. . .       
                            "'modded' in K_Panties", GetModdedString("images/KittySprite/Kitty_Sprite_Panties_", K_Panties, ".png"),
                            "K_Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green.png",
                            "K_Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace.png",
                            "K_Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini.png", 
                            "True", Null(),     
                            ),    
                    ),                    
            "K_Wet", ConditionSwitch( 
                    #if wet and down. . .
#                    "K_Legs and K_Legs != 'blue skirt' and not K_Upskirt", Null(), #If nor wearing a skirt, they would be invisible 
                    "'modded' in K_Panties", GetModdedString("images/KittySprite/Kitty_Sprite_Panties_", K_Panties, "_Down_Wet.png"),
                    "K_Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Down_Wet.png",
                    "K_Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Down_Wet.png",
                    "K_Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_DownW.png", 
                    "True", Null(),     
                    ),
            "True", ConditionSwitch(
                    # if not wet, but down
#                    "K_Legs and K_Legs != 'blue skirt' and not K_Upskirt", Null(), #If nor wearing a skirt, they would be invisible                     
                    "'modded' in K_Panties", GetModdedString("images/KittySprite/Kitty_Sprite_Panties_", K_Panties, "_Down.png"),
                    "K_Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Down.png",
                    "K_Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Down.png",
                    "K_Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_Down.png", 
                    "True", Null(),     
                    ),
            ),
        
        (225,560), ConditionSwitch(                                                                         
            #Personal Wetness            
            "not K_Wet", Null(),
            "K_Legs and not K_Upskirt", Null(),   
            "K_Panties and not K_PantiesDown and K_Wet <= 1", Null(),                   
            "K_Wet == 1", ConditionSwitch( #Wet = 1
                    "K_Panties and K_PantiesDown", AlphaMask("Wet_Drip","Kitty_Drip_MaskP"),  
                    "K_Legs", AlphaMask("Wet_Drip","Kitty_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip","Kitty_Drip_Mask"), #only plays if nothing is in the way
                    ),
            "True", ConditionSwitch( #Wet = 2+
                    "K_Panties and K_PantiesDown", AlphaMask("Wet_Drip2","Kitty_Drip_MaskP"), #"Wet_Drip2",# 
                    "K_Legs", AlphaMask("Wet_Drip2","Kitty_Drip_MaskP"),
                    "K_Panties", AlphaMask("Wet_Drip","Kitty_Drip_Mask"), #"Wet_Drip2",# 
                    "True", AlphaMask("Wet_Drip2","Kitty_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (0,0), ConditionSwitch(                                                                         
            #wetness                    
            "K_Legs or not K_Wet", Null(),             
            "K_Panties and not K_PantiesDown and K_Wet < 2", Null(),
            "K_Panties and not K_PantiesDown", "images/KittySprite/Kitty_Sprite_Wet1.png",
            "K_Wet == 2", "images/KittySprite/Kitty_Sprite_Wet2.png",
            "True", "images/KittySprite/Kitty_Sprite_Wet1.png",
            ),  
        (225,560), ConditionSwitch(                                                                         
            #Spunk nethers        
            "'in' not in K_Spunk and 'anal' not in K_Spunk", Null(),
            "K_Legs and not K_Upskirt", Null(),   
            "True", ConditionSwitch( #Wet = 2+
                    "K_Panties and K_PantiesDown", AlphaMask("Spunk_Drip2","Kitty_Drip_MaskP"), #"Wet_Drip2",# 
                    "K_Legs", AlphaMask("Spunk_Drip2","Kitty_Drip_MaskP"),
                    "True", AlphaMask("Spunk_Drip2","Kitty_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (0,0), ConditionSwitch(                                                                         
            #full hose/tights              
            "K_Panties and K_PantiesDown", Null(), 
            "not K_Hose", Null(),
            "'modded' in K_Hose", GetModdedString("images/KittySprite/Kitty_Sprite_hose_", K_Hose, ".png"),
            "True", Null(), 
            ),     
        (0,0), ConditionSwitch(                                                                        
            #pants         
            "K_Legs == 'blue skirt' and K_Upskirt", "images/KittySprite/Kitty_Sprite_Skirt_Up.png",       
            "K_Legs == 'blue skirt'", "images/KittySprite/Kitty_Sprite_Skirt.png",          
            "not K_Legs", Null(),
            "K_Upskirt and 'modded' in K_Legs", GetModdedString("images/KittySprite/Kitty_Sprite_Legs_", K_Legs, "_Down.png"),
            "K_Wet and 'modded' in K_Legs", GetModdedString("images/KittySprite/Kitty_Sprite_Legs_", K_Legs, "_Wet.png"),
            "'modded' in K_Legs", GetModdedString("images/KittySprite/Kitty_Sprite_Legs_", K_Legs, ".png"),
            "not K_Legs or K_Upskirt", Null(),
            #"'modded' in K_Legs and K_Upskirt", GetModdedString("images/KittySprite/Kitty_Sprite_Legs", K_Legs, ".png"),
            "K_Legs == 'capris'", "images/KittySprite/Kitty_Sprite_Pants_Blue.png",
            "K_Legs == 'black jeans'", "images/KittySprite/Kitty_Sprite_Pants_Black.png",
            "K_Wet and K_Legs == 'yoga pants'", "images/KittySprite/Kitty_Sprite_Pants_Yoga_Wet.png",   
            "K_Legs == 'yoga pants'", "images/KittySprite/Kitty_Sprite_Pants_Yoga.png",   
            "K_Wet and K_Legs == 'shorts'", "images/KittySprite/Kitty_Sprite_Shorts_Wet.png",    
            "K_Legs == 'shorts'", "images/KittySprite/Kitty_Sprite_Shorts.png",            
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(                                                                         
            #Arms2               
            "Kitty_Arms and K_DynamicTan[0]", "images/KittySprite/Kitty_Sprite_T3Arms2.png",
            "Kitty_Arms", "images/KittySprite/Kitty_Sprite_Arms2.png",
            "True", Null(),               
            ), 

        (0,0), ConditionSwitch(                                                                         #Arms2               
            "not K_DynamicTan[3] or not K_DynamicTan[0] or not Kitty_Arms", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Arms2.png", GetModdedStringTanKitty("3", "2.png")),
            ),

        (0,0), ConditionSwitch(   
            "not K_DynamicTan[1] or not K_DynamicTan[0] or not Kitty_Arms", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Arms2.png", GetModdedStringTanKitty("1", "2.png")),
            ),

        (0,0), ConditionSwitch(                                                                         #chest
            "True and K_DynamicTan[0]", "images/KittySprite/Kitty_Sprite_T3chest_bare.png",
            "True", "images/KittySprite/Kitty_Sprite_Chest_Bare.png",
            ),  
        (0,0), ConditionSwitch(                                                                     #body
            "not K_DynamicTan[3] or not K_DynamicTan[0]", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Chest_Bare.png", GetModdedStringTanKitty("3", "1.png")),
            ),

        (0,0), ConditionSwitch(   
            "not K_DynamicTan[1] or not K_DynamicTan[0]", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Chest_Bare.png", GetModdedStringTanKitty("1", "1.png")),
            ),#            #chest
#            "not K_Chest and not K_Over", "images/KittySprite/Kitty_Sprite_Chest_Bare.png",
#            "True", "images/KittySprite/Kitty_Sprite_Chest_Bare.png",
#            ),  
        (0,0), ConditionSwitch(   
            #piercings top
            "not K_Pierce", Null(),                       
            "K_Pierce == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingT.png",      
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallT.png",   
            ),    
#        (0,0), ConditionSwitch(                                                                         
#            #Bra
#            "not K_Chest", Null(),
#            "Kitty_Arms and K_Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami2.png",
#            "Kitty_Arms and K_Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini2.png",
#            "K_Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini1.png",
#            "K_Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace.png",
#            "K_Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport.png",
#            "K_Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic.png",
#            "K_Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1.png",
#            "K_Chest == 0 and K_Over == 'pink top'", Null(),   #use for when bra and top clash  
#            "True", Null(),       
#            ),  
        
        (0,0), ConditionSwitch(                                                                        
            #necklace
            "K_Neck == 'gold necklace'", "images/KittySprite/Kitty_Sprite_Necklace1.png",
            "K_Neck == 'star necklace'", "images/KittySprite/Kitty_Sprite_Necklace2.png",
            "True", Null(),
            ),   
        (0,0), ConditionSwitch(                                                                         
            #bra layer           
            "not K_Chest", Null(),                  
            "not K_Uptop", ConditionSwitch( 
                    #if the top's down. . .
                    "Kitty_Arms and 'modded' in K_Chest", GetModdedString("images/KittySprite/Kitty_Sprite_Chest_", K_Chest, "2.png"),
                    "'modded' in K_Chest", GetModdedString("images/KittySprite/Kitty_Sprite_Chest_", K_Chest, "1.png"),
                    "Kitty_Arms and K_Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami2.png",
                    "Kitty_Arms and K_Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini2.png",
                    "K_Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini1.png",
                    "K_Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace.png",
                    "K_Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport.png",
                    "K_Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic.png",
                    "K_Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1.png",
                    "True", Null(),     
                    ),
            "K_Over", ConditionSwitch(
                    # If she's wearing a shirt over the bra                        
#                    "Kitty_Arms and K_Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1_UpS.png",
#                    "Kitty_Arms and K_Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini2_UpS.png",
                    "K_Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini1_Up.png",
                    "K_Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace1_UpS.png",
                    "K_Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport1_UpS.png",
                    "K_Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic1_Up.png",
                    "K_Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1_UpS.png",    
                    "True", Null(),     
                    ),
            "True", ConditionSwitch(
                    # if she's not wearing a shirt
                    "Kitty_Arms", ConditionSwitch(
                            # if Arms 2
                            "K_Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini2_Up.png",
                            "K_Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace2_Up.png",
                            "K_Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport2_Up.png",
                            "K_Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic2_Up.png",
                            "K_Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami2_Up.png",            
                            "True", Null(),     
                            ),                    
                    "True", ConditionSwitch(
                            # if Arms 1
                            "K_Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini1_Up.png",
                            "K_Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace1_Up.png",
                            "K_Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport1_Up.png",
                            "K_Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic1_Up.png",
                            "K_Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1_Up.png",            
                            "True", Null(),     
                            ),            
                    "True", Null(),     
                    ),
            ),
            
        (0,0), ConditionSwitch(                                                                        
            #piercings over shirt
            "not K_Pierce or not K_Chest or K_Uptop", Null(),                       
            "K_Pierce == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingOver.png",      
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallOver.png",   
            ),    
        (0,0), ConditionSwitch(                                                                        
            #wet look
            "K_Water and Kitty_Arms", "images/KittySprite/Kitty_Sprite_Water2.png",
            "K_Water", "images/KittySprite/Kitty_Sprite_Water1.png",
            "True", Null(),
            ),  
        
#        (0,0), ConditionSwitch(                                                                         
#            #shirt
#            "not K_Over", Null(),
#            "Kitty_Arms and K_Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink2.png",
#            "Kitty_Arms and K_Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew2.png",
#            "Kitty_Arms and K_Over == 'towel'", "images/KittySprite/Kitty_Sprite_Over_Towel2.png",
#            "K_Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink1.png",
#            "K_Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew1.png",
#            "K_Over == 'towel'", "images/KittySprite/Kitty_Sprite_Over_Towel1.png",
#            "True", Null(),
#            ),   
                    
        (0,0), ConditionSwitch(                                                                         
            #shirt layer           
            "not K_Over", Null(),                  
            "not K_Uptop", ConditionSwitch( 
                    #if the top's down. . .
                    "Kitty_Arms and 'modded' in K_Over", GetModdedString("images/KittySprite/Kitty_Sprite_Over_", K_Over, "2.png"),
                    "'modded' in K_Over", GetModdedString("images/KittySprite/Kitty_Sprite_Over_", K_Over, "1.png"),
                    "Kitty_Arms and K_Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink2.png",
                    "Kitty_Arms and K_Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew2.png",
                    "Kitty_Arms and K_Over == 'towel'", "images/KittySprite/Kitty_Sprite_Over_Towel2.png",
                    "K_Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink1.png",
                    "K_Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew1.png",
                    "K_Over == 'towel'", "images/KittySprite/Kitty_Sprite_Over_Towel1.png",
                    "True", Null(),     
                    ),            
            "True", ConditionSwitch(
                    # if she's not wearing a shirt                    
                    "Kitty_Arms and K_Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink2_Up.png",
                    "Kitty_Arms and K_Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew2_Up.png",
#                    "Kitty_Arms and K_Over == 'towel'", "images/KittySprite/Kitty_Sprite_Over_Towel2.png",
                    "K_Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink1_Up.png",
                    "K_Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew1_Up.png",            
#                    "K_Over == 'towel'", "images/KittySprite/Kitty_Sex_Over_Towel.png",   
                    "True", Null(),     
                    ),
            ),
            
        (0,0), ConditionSwitch(                                                                         
            #bra over shirt layer           
            "not K_Over or not K_Chest or not K_Uptop", Null(),   
            "K_Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami_Over.png", 
            "K_Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace_Over.png",
            "K_Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport_Over.png",
            "K_Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic_Over.png",
            "K_Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini_Over.png",
            "True", Null(),  
            ),
            
        (124,0), ConditionSwitch(
            "renpy.showing('Kitty_BJ_Animation')", Null(),
            "True", "Kitty_Head",   
            ), 
        
        (0,0), ConditionSwitch(                                                                        
            #anal spunk
            "K_Legs and not K_Upskirt", Null(), 
            "K_Panties and not K_PantiesDown", Null(), 
            "'anal' in K_Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Anal.png",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(                                                                        
            #pussy spunk
            "K_Legs and not K_Upskirt", Null(), 
            "K_Panties and not K_PantiesDown", Null(), 
            "'in' in K_Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Pussy.png",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(                                                                         
            #belly spunk
            "'belly' in K_Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Belly.png",
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(                                                                         
            #tits spunk
            "'tits' in K_Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Tits.png",
            "True", Null(), 
            ),   
            
        (0,0), ConditionSwitch(
            #UI tool for When Kitty is masturbating using Trigger3 actions
            "Trigger == 'lesbian' or not Trigger3 or Ch_Focus != 'Kitty'", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and K_Lust >= 70", "GirlFingerPussy_K",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_K",            
            "Trigger3 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeLeftBreast_K",    #When zero is working the right breast, fondle left
            "Trigger3 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeRightBreast_K", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts'", "GirlGropeRightBreast_K",
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast_K",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy_K",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy_K",
            "Trigger3 == 'vibrator anal'", "VibratorAnal_K",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy_K",            
            "True", Null(),             
            ),                        
        (0,0), ConditionSwitch(  
            #UI tool for Trigger5(Threesome masutrbation) actions
            "not Trigger5 or Trigger4 != 'masturbation' or Ch_Focus == 'Kitty'", Null(), 
            #this doesn't activate unless Kitty is not primary, and actively masturbating
            "Trigger5 == 'fondle pussy' and Trigger != 'sex' and K_Lust >= 70", "GirlFingerPussy_K",
            "Trigger5 == 'fondle pussy'", "GirlGropePussy_K",
            "Trigger5 == 'fondle breasts'", "GirlGropeRightBreast_K",
            "Trigger5 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger5 == 'vibrator pussy'", "VibratorPussy",
            "Trigger5 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger5 == 'vibrator anal'", "VibratorAnal",
            "Trigger5 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(), 
            ),               
        (0,0), ConditionSwitch(                
            #UI tool for Trigger1(primary) actions
            "not Trigger or Ch_Focus != 'Kitty'", Null(),
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast_K",
            "Trigger == 'fondle thighs'", "GropeThigh_K",
            "Trigger == 'fondle breasts'", "GropeLeftBreast_K",
            "Trigger == 'suck breasts'", "LickRightBreast_K",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_K",
            "Trigger == 'fondle pussy'", "GropePussy_K",
            "Trigger == 'lick pussy'", "Lickpussy_K",
            "Trigger == 'vibrator pussy'", "VibratorPussy_K",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy_K",
            "Trigger == 'vibrator anal'", "VibratorAnal_K",
            "Trigger == 'vibrator anal insert'", "VibratorPussy_K",
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                
            #UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus != 'Kitty'", Null(),
            "not Trigger2 and not Trigger4 and Trigger == 'fondle breasts'", "GropeRightBreast_K",        
            #When doing nothing offhand, use both hands on breasts.
            "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast_K",            
            #When sucking right breast, fondle left
            "Trigger2 == 'fondle breasts'", "GropeRightBreast_K",
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast_K",       
            #When sucking right breast, vibrator left
            "Trigger2 == Trigger", Null(),
            #When both triggers are the same, do nothing              
            "Trigger2 == 'suck breasts'", "LickLeftBreast_K",        
            "Trigger2 == 'fondle pussy'", "GropePussy_K",
            "Trigger2 == 'lick pussy'", "Lickpussy_K",       
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast_K",
            "Trigger2 == 'vibrator pussy'", "VibratorPussy_K",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy_K",
            "Trigger2 == 'vibrator anal'", "VibratorAnal_K",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy_K",
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(  
            #UI tool for Trigger4(Threesome) actions (ie Rogue's hand on her)
            "not Trigger4 or Ch_Focus != 'Kitty'", Null(),
            "Trigger4 == 'fondle pussy' and Trigger != 'sex' and K_Lust >= 70", "GirlFingerPussy_K",
            "Trigger4 == 'fondle pussy'", "GirlGropePussy_K",            
            "Trigger4 == 'lick pussy'", "Lickpussy_K",
            "Trigger4 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_K", 
            "Trigger4 == 'suck breasts'", "LickRightBreast_K",  
            "Trigger4 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_K",    #When zero is working the right breast, fondle left
            "Trigger4 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_K", #When zero is working the left breast, fondle right  
            "Trigger4 == 'fondle breasts' and (Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts')", "GirlGropeLeftBreast_K", #When zero is working the left breast, fondle right  
            "Trigger4 == 'fondle breasts'", "GirlGropeRightBreast_K",
            "Trigger4 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger4 == 'vibrator pussy'", "VibratorPussy",
            "Trigger4 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger4 == 'vibrator anal'", "VibratorAnal",
            "Trigger4 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),             
            ),    
        (0,0), ConditionSwitch(  
            #UI tool for Trigger3(lesbian) actions (ie Rogue's hand on her when Kitty is secondary)
            "Trigger != 'lesbian' or not Trigger3 or Ch_Focus == 'Kitty'", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and K_Lust >= 70", "GirlFingerPussy_K",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_K",            
            "Trigger3 == 'lick pussy'", "Lickpussy_K",
            "Trigger3 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_K", 
            "Trigger3 == 'suck breasts'", "LickRightBreast_K",  
            "Trigger3 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_K",    #When zero is working the right breast, fondle left
            "Trigger3 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_K", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts' and (Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts')", "GirlGropeLeftBreast_K", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts'", "GirlGropeRightBreast_K",
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger3 == 'vibrator anal'", "VibratorAnal",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),             
            ),         
        )
    anchor (0.6, 0.0)
    zoom .75

image Kitty_Head:               
    LiveComposite(
        (416,610),    
#        (0,0), ConditionSwitch(
#            "K_Water", "images/KittySprite/Kitty_Sprite_Hair_Wet_Back.png",
#            "K_Hair == 'long'", "images/KittySprite/Kitty_Sprite_Hair_Long_Back.png",
#            "True", Null(),
#            ),    
        (0,0), ConditionSwitch(
            "K_DynamicTan[0] and K_Water and K_Blush == 1", "images/KittySprite/Kitty_Sprite_THead_Wet_Blush1.png",
            "K_Water and K_Blush == 1", "images/KittySprite/Kitty_Sprite_Head_Wet_Blush1.png",
            "K_DynamicTan[0] and K_Water and K_Blush == 2", "images/KittySprite/Kitty_Sprite_THead_Wet_Blush2.png",
            "K_Water and K_Blush == 2", "images/KittySprite/Kitty_Sprite_Head_Wet_Blush2.png",
            "K_DynamicTan[0] and K_Water", "images/KittySprite/Kitty_Sprite_THead_Wet_Base.png",
            "K_Water", "images/KittySprite/Kitty_Sprite_Head_Wet_Base.png",
            "K_DynamicTan[0] and K_Blush == 1", "images/KittySprite/Kitty_Sprite_THead_Evo_Blush1.png",
            "K_Blush == 1", "images/KittySprite/Kitty_Sprite_Head_Evo_Blush1.png",
            "K_DynamicTan[0] and K_Blush == 2", "images/KittySprite/Kitty_Sprite_THead_Evo_Blush2.png",
            "K_Blush == 2", "images/KittySprite/Kitty_Sprite_Head_Evo_Blush2.png",
            "K_DynamicTan[0]", "images/KittySprite/Kitty_Sprite_THead_Evo_Base.png",
            "True", "images/KittySprite/Kitty_Sprite_Head_Evo_Base.png",
            ),     
        (0,0), ConditionSwitch(
            "K_Brows == 'normal'", "images/KittySprite/Kitty_Sprite_Brows_Normal.png",
            "K_Brows == 'angry'", "images/KittySprite/Kitty_Sprite_Brows_Angry.png",
            "K_Brows == 'sad'", "images/KittySprite/Kitty_Sprite_Brows_Sad.png",
            "K_Brows == 'surprised'", "images/KittySprite/Kitty_Sprite_Brows_Surprised.png",
            "K_Brows == 'confused'", "images/KittySprite/Kitty_Sprite_Brows_Confused.png",
            "True", "images/KittySprite/Kitty_Sprite_Brows_Normal.png",
            ),
        (0,0), ConditionSwitch(
            "K_DynamicTan[0] and K_Mouth == 'normal'", "images/KittySprite/Kitty_Sprite_TMouth_Normal.png",
            "K_Mouth == 'normal'", "images/KittySprite/Kitty_Sprite_Mouth_Normal.png",
            "K_DynamicTan[0] and K_Mouth == 'lipbite'", "images/KittySprite/Kitty_Sprite_TMouth_Lipbite.png",
            "K_Mouth == 'lipbite'", "images/KittySprite/Kitty_Sprite_Mouth_Lipbite.png",
            "K_DynamicTan[0] and K_Mouth == 'kiss'", "images/KittySprite/Kitty_Sprite_TMouth_Kiss.png",
            "K_Mouth == 'kiss'", "images/KittySprite/Kitty_Sprite_Mouth_Kiss.png",
            "K_DynamicTan[0] and K_Mouth == 'sad'", "images/KittySprite/Kitty_Sprite_TMouth_Sad.png",
            "K_Mouth == 'sad'", "images/KittySprite/Kitty_Sprite_Mouth_Sad.png",
            "K_DynamicTan[0] and K_Mouth == 'smile'", "images/KittySprite/Kitty_Sprite_TMouth_Smile.png",
            "K_Mouth == 'smile'", "images/KittySprite/Kitty_Sprite_Mouth_Smile.png",
            "K_Mouth == 'surprised'", "images/KittySprite/Kitty_Sprite_Mouth_Surprised.png",
            "K_Mouth == 'tongue'", "images/KittySprite/Kitty_Sprite_Mouth_Tongue.png",
            "K_Mouth == 'sucking'", "images/KittySprite/Kitty_Sprite_Mouth_Tongue.png", #fix add
            "True", "images/KittySprite/Kitty_Sprite_Mouth_Normal.png",
            "True", "images/KittySprite/Kitty_Sprite_Mouth_Normal.png",
            ),      
        (0,0), ConditionSwitch(
            "'mouth' not in K_Spunk", Null(),            
            "K_Mouth == 'normal'", "images/KittySprite/Kitty_Sprite_Spunk_Normal.png",
            "K_Mouth == 'lipbite'", "images/KittySprite/Kitty_Sprite_Spunk_Normal.png",
            "K_Mouth == 'kiss'", "images/KittySprite/Kitty_Sprite_Spunk_Kiss.png",
            "K_Mouth == 'sad'", "images/KittySprite/Kitty_Sprite_Spunk_Sad.png",
            "K_Mouth == 'smile'", "images/KittySprite/Kitty_Sprite_Spunk_Smile.png",
            "K_Mouth == 'surprised'", "images/KittySprite/Kitty_Sprite_Spunk_Surprised.png",
            "K_Mouth == 'tongue'", "images/KittySprite/Kitty_Sprite_Spunk_Tongue.png",
            "K_Mouth == 'sucking'", "images/KittySprite/Kitty_Sprite_Spunk_Sucking.png", #fix add
            "True", Null(),
            ),       
        (0,0), ConditionSwitch(
            "'facial' in K_Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Facial.png",
            "True", Null(),
            ),     
        (0,0), "Kitty Blink",
        (0,0), ConditionSwitch(
            "K_Water", im.MatrixColor("images/KittySprite/Kitty_Sprite_Hair" + GetHairColor(K_HairColor) + "_Wet.png",im.matrix.tint(float(K_HairCustomColor.red)/255.0, float(K_HairCustomColor.green)/255.0, float(K_HairCustomColor.blue)/255.0)),
            "K_Hair == 'evo'", im.MatrixColor("images/KittySprite/Kitty_Sprite_Hair" + GetHairColor(K_HairColor) + "_Evo.png",im.matrix.tint(float(K_HairCustomColor.red)/255.0, float(K_HairCustomColor.green)/255.0, float(K_HairCustomColor.blue)/255.0)),
            "K_Hair == 'long'", im.MatrixColor("images/KittySprite/Kitty_Sprite_Hair" + GetHairColor(K_HairColor) + "_Long.png",im.matrix.tint(float(K_HairCustomColor.red)/255.0, float(K_HairCustomColor.green)/255.0, float(K_HairCustomColor.blue)/255.0)),
            "K_Hair == 'wet'", im.MatrixColor("images/KittySprite/Kitty_Sprite_Hair" + GetHairColor(K_HairColor) + "_Wet.png",im.matrix.tint(float(K_HairCustomColor.red)/255.0, float(K_HairCustomColor.green)/255.0, float(K_HairCustomColor.blue)/255.0)),
            "True", im.MatrixColor("images/KittySprite/Kitty_Sprite_Hair" + GetHairColor(K_HairColor) + "_Evo.png",im.matrix.tint(float(K_HairCustomColor.red)/255.0, float(K_HairCustomColor.green)/255.0, float(K_HairCustomColor.blue)/255.0)),
            ),     
        (0,0), ConditionSwitch(
            "K_Water", "images/KittySprite/Kitty_Sprite_Wet_Head.png",
            "True", Null(),
            ),     
        (0,0), ConditionSwitch(
            "K_Hair == 'evo' and 'hair' in K_Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Evohair.png",
            "K_Hair == 'long' and 'hair' in K_Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Evohair.png",
#            "K_Hair == 'evo' and 'hair' in K_Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Evohair.png",
            "True", Null(),
            ),     
        )
#    anchor (0.6, 0.0)
    zoom .5

image Kitty_HairBack:
    LiveComposite(
        (416,610),    
        (0,0), ConditionSwitch(
            "K_Water or K_Hair == 'wet'", im.MatrixColor("images/KittySprite/Kitty_Sprite_Hair" + GetHairColor(K_HairColor) + "_Wet_Back.png",im.matrix.tint(float(K_HairCustomColor.red)/255.0, float(K_HairCustomColor.green)/255.0, float(K_HairCustomColor.blue)/255.0)),
            "K_Hair == 'long'", im.MatrixColor("images/KittySprite/Kitty_Sprite_Hair" + GetHairColor(K_HairColor) + "_Long_Back.png",im.matrix.tint(float(K_HairCustomColor.red)/255.0, float(K_HairCustomColor.green)/255.0, float(K_HairCustomColor.blue)/255.0)),
            "True", Null(),
            ),    
        )
#    anchor (0.6, 0.0)
    zoom .5
    
image Kitty Blink:
    ConditionSwitch( 
    "K_Eyes == 'sexy'", "images/KittySprite/Kitty_Sprite_Eyes_Sexy.png", 
    "K_Eyes == 'side'", "images/KittySprite/Kitty_Sprite_Eyes_Side.png",  
    "K_Eyes == 'surprised'", "images/KittySprite/Kitty_Sprite_Eyes_Surprised.png",  
    "K_Eyes == 'manic'", "images/KittySprite/Kitty_Sprite_Eyes_Surprised.png",  
    "K_Eyes == 'normal'", "images/KittySprite/Kitty_Sprite_Eyes_Normal.png",  
    "K_Eyes == 'down'", "images/KittySprite/Kitty_Sprite_Eyes_Down.png",  
    "K_Eyes == 'stunned'", "images/KittySprite/Kitty_Sprite_Eyes_Down.png",  
    "K_Eyes == 'squint'", "Kitty_Squint",  
    "K_Eyes == 'leftside'", "images/KittySprite/Kitty_Sprite_Eyes_SideLeft.png",
    "K_Eyes == 'closed'", "images/KittySprite/Kitty_Sprite_Eyes_Closed.png",    
    "True", "images/KittySprite/Kitty_Sprite_Eyes_Normal.png", 
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    # This randomizes the time between blinking.
    "images/KittySprite/Kitty_Sprite_Eyes_Closed.png"
    .25
    repeat 
    
image Kitty_Squint:
    "images/KittySprite/Kitty_Sprite_Eyes_Sexy.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/KittySprite/Kitty_Sprite_Eyes_Squint.png"
    .25
    repeat    
            
            
image Kitty_Drip_Mask:
    #This is the mask for her drip pattern
    contains:
        "images/KittySprite/Kitty_Sprite_WetMask.png"      
        offset (-225,-560)

image Kitty_Drip_MaskP:
    #This is the mask for her drip pattern in panties down mode
    contains:
        "images/KittySprite/Kitty_Sprite_WetMaskP.png"      
        offset (-225,-560)
            
# End Kitty Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
  
  











# Kitty Sex Sprite ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


image Kitty_SexSprite:            
    LiveComposite(                                                                                 #Base body
        (1120,840),  
        (0,0), ConditionSwitch(                                                        
                #Shows different upper body motion depending on events  
                "not P_Sprite", "Kitty_Sex_Body_Static", 
                "P_Cock == 'anal'", ConditionSwitch( 
                        #if the top's down. . .
                        "Speed >= 3", "Kitty_Sex_Body_Anim3",
                        "Speed >= 2", "Kitty_Sex_Body_Anim2",
                        "Speed", "Kitty_Sex_Body_Anim1",
                        "True", "Kitty_Sex_Body_Static",   
                        ),            
                "P_Cock == 'in'", ConditionSwitch( 
                        #if the top's down. . .
                        "Speed >= 3", "Kitty_Sex_Body_Anim3",
                        "Speed >= 2", "Kitty_Sex_Body_Anim2",
                        "Speed", "Kitty_Sex_Body_Anim1",
                        "True", "Kitty_Sex_Body_Static",   
                        ),             
                "P_Cock == 'foot'", ConditionSwitch( 
                        #if the top's down. . .
                        "Speed >= 2", "Kitty_Sex_Body_FootAnim2",
                        "Speed", "Kitty_Sex_Body_FootAnim1",
                        "True", "Kitty_Sex_Body_FootAnimStatic",   
                        ),            
                "P_Cock == 'out' and Speed >= 2","Kitty_Hotdog_Body_Anim2",                                    
                "True", "Kitty_Sex_Body_Static",           
                ),              
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events            
                "not P_Sprite", "Kitty_Sex_Legs_Static", 
                "P_Cock == 'anal'", ConditionSwitch( 
                        #if the top's down. . .
                        "Speed >= 3", "Kitty_Sex_Legs_Anim3",
                        "Speed >= 2", "Kitty_Sex_Legs_Anim2",
                        "Speed", "Kitty_Sex_Legs_Anim1",
                        "True", "Kitty_Sex_Legs_Static",   
                        ),            
                "P_Cock == 'in'", ConditionSwitch( 
                        #if the top's down. . .
                        "Speed >= 3", "Kitty_Sex_Legs_Anim3",
                        "Speed >= 2", "Kitty_Sex_Legs_Anim2",
                        "Speed", "Kitty_Sex_Legs_Anim1",
                        "True", "Kitty_Sex_Legs_Static",   
                        ),             
                "P_Cock == 'foot'", ConditionSwitch( 
                        #if the top's down. . .
                        "Speed >= 2", "Kitty_Sex_Legs_FootAnim2",
                        "Speed", "Kitty_Sex_Legs_FootAnim1",
                        "True", "Kitty_Sex_Legs_FootAnimStatic",   
                        ),            
                "P_Cock == 'out' and Speed >= 2","Kitty_Hotdog_Legs_Anim2",                                    
                "True", "Kitty_Sex_Legs_Static",           
                ),
        ) 
    align (0.6,0.0)
    pos (650,230)#(750,230)
    zoom 0.7

image Kitty_Sex_Body_Static:
    contains:
            "Kitty_Sex_Body"
    pos (650,230)
            
image Kitty_Sex_Legs_Static:
    contains:
            "Kitty_Sex_Legs"
    pos (650,230)

image Kitty_Sex_Body:
    LiveComposite(                                                                                
        #the torso/head used in the sex pose, referenced by Kitty_SexSprite
        (1120,840),
#        (0,0), ConditionSwitch(                                                                                 #Hair underlayer, delete once this is working
#            "K_Water", Null(), 
#            "K_Hair == 'evo'", "images/KittySex/Kitty_Sex_HairB.png",   
#            "True", Null(),                   
#            ),   
        (260,-350), "Kitty_HairBack_Sex",                                                                                      #Hair underlayer
        (0,0), ConditionSwitch(                                                                                 #Body Base
            "K_DynamicTan[0]", "images/KittySex/Kitty_Sex_T3Body.png",
            "True", "images/KittySex/Kitty_Sex_Body.png",             
            ), 
        (0,0), ConditionSwitch(   
            "not K_DynamicTan[0] or not K_DynamicTan[3]", Null(),
            "True", AlphaMask("images/KittySex/Kitty_Sex_Body.png", GetModdedStringTanKitty("3", ".png", "Sex")),
            # "K_DynamicTan[0] and K_DynamicTan[3] == 'cami'", AlphaMask("images/KittySex/Kitty_Sex_Body.png", "images/KittySex/Kitty_Sex_Under_Cami.png"),
            # "K_DynamicTan[0] and K_DynamicTan[3] == 'sports bra'", AlphaMask("images/KittySex/Kitty_Sex_Body.png", "images/KittySex/Kitty_Sex_Under_SportsBra.png"),
            # "K_DynamicTan[0] and K_DynamicTan[3] == 'bra'", AlphaMask("images/KittySex/Kitty_Sex_Body.png", "images/KittySex/Kitty_Sex_Under_Bra.png"),
            # "K_DynamicTan[0] and K_DynamicTan[3] == 'lace bra'", AlphaMask("images/KittySex/Kitty_Sex_Body.png", "images/KittySex/Kitty_Sex_Under_LaceBra.png"),
            # "True", Null(),
            ),
        (0,0), ConditionSwitch(   
            "not K_DynamicTan[0] or not K_DynamicTan[2]", Null(),
            "K_DynamicTan[2] == 'modded black blue pants'", AlphaMask("images/KittySex/Kitty_Sex_Body.png", "images/KittySex/Kitty_Sex_Legs_Chest_modded black blue pants.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(   
            "not K_DynamicTan[0] or not K_DynamicTan[1]", Null(),
            "True", AlphaMask("images/KittySex/Kitty_Sex_Body.png", GetModdedStringTanKitty("1", ".png", "Sex")),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #Body Base
            "not K_Pierce", Null(),             
            "K_Pierce == 'barbell'", "images/KittySex/Kitty_Sex_Body_Tits_Barbell.png",   
            "K_Pierce == 'ring'", "images/KittySex/Kitty_Sex_Body_Tits_Ring.png",   
            "True", Null(),             
            ),             
        (260,-350), "Kitty_Head_Sex",  #check positioning (400,-300)
        #Eyes
        (0,0), ConditionSwitch(                                                                                 #necklace
            "K_Neck == 'gold necklace'", "images/KittySex/Kitty_Sex_Neck_Gold.png",
            "K_Neck == 'star necklace'", "images/KittySex/Kitty_Sex_Neck_Star.png",
            "True", Null(),
            ),  
#        (0,0), ConditionSwitch(                                                                                 #tanktop
#            "not K_Chest", Null(),        
#            "K_Chest == 'cami'", "images/KittySex/Kitty_Sex_Under_Cami.png",
#            "K_Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Under_SportsBra.png",
#            "K_Chest == 'bra'", "images/KittySex/Kitty_Sex_Under_Bra.png",
#            "K_Chest == 'lace bra'", "images/KittySex/Kitty_Sex_Under_LaceBra.png",
#            "True", Null(),            
#            ), 
        (0,0), ConditionSwitch( 
            #if she's wearing legs that affects the chest (black blue pants). . .
            "not K_Legs or K_Upskirt", Null(),
            "'modded' in K_Legs", GetModdedString("images/KittySex/Kitty_Sex_Legs_Chest_", K_Legs, ".png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                         
            #bra layer           
            "not K_Chest", Null(),                  
            "not K_Uptop", ConditionSwitch( 
                    #if the top's down. . .
                    "'modded' in K_Chest", GetModdedString("images/KittySex/Kitty_Sex_Chest_", K_Chest, ".png"),
                    "K_Chest == 'cami'", "images/KittySex/Kitty_Sex_Under_Cami.png",
                    "K_Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Under_SportsBra.png",
                    "K_Chest == 'bra'", "images/KittySex/Kitty_Sex_Under_Bra.png",
                    "K_Chest == 'bikini top'", "images/KittySex/Kitty_Sex_Under_Bikini.png",
                    "K_Chest == 'lace bra'", "images/KittySex/Kitty_Sex_Under_LaceBra.png",
                    "True", Null(),     
                    ),
            "K_Over", ConditionSwitch(
                    # If she's wearing a shirt over the bra
                    "K_Chest == 'cami'", "images/KittySex/Kitty_Sex_Under_Cami_UpS.png",
                    "K_Chest == 'bikini top'", "images/KittySex/Kitty_Sex_Under_Bikini_Up.png",
                    "K_Chest == 'sports bra' and K_Over == 'red shirt'", "images/KittySex/Kitty_Sex_Under_SportsBra_UpS.png",
                    "K_Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Under_SportsBra_Up.png",
                    "True", Null(),     
                    ),
            "True", ConditionSwitch(
                    # if she's not wearing a shirt
                    "K_Chest == 'cami'", "images/KittySex/Kitty_Sex_Under_Cami_Up.png",
                    "K_Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Under_SportsBra_Up.png",
                    "K_Chest == 'bra'", "images/KittySex/Kitty_Sex_Under_Bra_Up.png",
                    "K_Chest == 'bikini top'", "images/KittySex/Kitty_Sex_Under_Bikini_Up.png",
                    "K_Chest == 'lace bra'", "images/KittySex/Kitty_Sex_Under_LaceBra_Up.png",
                    "True", Null(),     
                    ),
            ),
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "K_Water", "images/KittySex/Kitty_Sex_Water_Body.png",   
            "True", Null(),              
            ), 
#        (0,0), ConditionSwitch(                                                                                 #Wet look
#            "K_Pierce == 'barbell'", "images/KittySex/Kitty_Sex_Body_Barbell.png",   
#            "K_Pierce == 'ring'", "images/KittySex/Kitty_Sex_Body_Ring.png",   
#            "True", Null(),              
#            ), 
        
#        (0,0), ConditionSwitch(                                                                                 #Overshirt
#            "not K_Over", Null(),
#            "K_Over == 'pink top'", "images/KittySex/Kitty_Sex_Over_PinkShirt.png",           
#            "K_Over == 'red shirt'", "images/KittySex/Kitty_Sex_Over_RedShirt.png",   
#            "K_Over == 'towel'", "images/KittySex/Kitty_Sex_Over_Towel.png",       
#            "True", Null(), 
#            ), 
        
        (0,0), ConditionSwitch(                                                                         
            #shirt layer           
            "not K_Over", Null(),                  
            "not K_Uptop", ConditionSwitch( 
                    #if the top's down. . .
                    "'modded' in K_Over", GetModdedString("images/KittySex/Kitty_Sex_Over_", K_Over, ".png"),
                    "K_Over == 'pink top'", "images/KittySex/Kitty_Sex_Over_PinkShirt.png",           
                    "K_Over == 'red shirt'", "images/KittySex/Kitty_Sex_Over_RedShirt.png",   
                    "K_Over == 'towel'", "images/KittySex/Kitty_Sex_Over_Towel.png",   
                    "True", Null(),     
                    ),            
            "True", ConditionSwitch(
                    # if she's not wearing a shirt
                    "K_Over == 'pink top' and K_Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Over_PinkShirt_UpS.png", 
                    "K_Over == 'pink top'", "images/KittySex/Kitty_Sex_Over_PinkShirt_Up.png",           
                    "K_Over == 'red shirt'", "images/KittySex/Kitty_Sex_Over_RedShirt_Up.png",   
#                    "K_Over == 'towel'", "images/KittySex/Kitty_Sex_Over_Towel.png",   
                    "True", Null(),     
                    ),
            ),
        (0,0), ConditionSwitch(                                                                         
            #bra layer over the shirt          
            "not K_Chest or not K_Over or not K_Uptop", Null(),    
            # if she's not wearing a shirt
            "K_Chest == 'bra'", "images/KittySex/Kitty_Sex_Under_Bra_Up.png",
            "K_Chest == 'lace bra'", "images/KittySex/Kitty_Sex_Under_LaceBra_UpS.png",
            "True", Null(),    
            ),
        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'belly' in K_Spunk", "images/KittySex/Kitty_Sex_Spunk_Body.png",   
            "True", Null(),  
            ),  
        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'tits' in K_Spunk", "images/KittySex/Kitty_Sex_Spunk_Tits.png",   
            "True", Null(),  
            ),  
        )

image Kitty_Head_Sex:
    # The head used for the sex pose, referenced by Kitty_Sex_Body
    "Kitty_Head"
    zoom 1.5
    anchor (0.5,0.5)
    rotate -10
    
image Kitty_HairBack_Sex:
    # The hair behind the head for the sex pose, referenced by Kitty_Sex_Body            
    "Kitty_HairBack"
    zoom 1.5
    anchor (0.5,0.5)   
    rotate -10         

#image Kitty_Sex_Legs = LiveComposite(  
image Kitty_Sex_Legs:
    LiveComposite(  
        #the legs used in the sex pose, referenced by Kitty_SexSprite
        (1120,840), 
        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            "not K_Legs", Null(),   
            "K_Legs == 'blue skirt'", "images/KittySex/Kitty_Sex_Skirt_Back.png",   
            "'modded' in K_Legs and 'skirt' in K_Legs", GetModdedString("images/KittySex/Kitty_Sex_Legs_", K_Legs, "_Back.png"),
            "True", Null(),                      
            ),  
        (0,0), ConditionSwitch(
            "K_DynamicTan[0]", "images/KittySex/Kitty_Sex_T3Legs.png",
            "True", "images/KittySex/Kitty_Sex_Legs.png",
            ),
        (0,0), ConditionSwitch(   
            "not K_DynamicTan[0] or not K_DynamicTan[4]", Null(),
            "True", AlphaMask("images/KittySex/Kitty_Sex_Legs.png", GetModdedStringTanKitty("4", ".png", "Sex")),
            # "K_DynamicTan[0] and K_DynamicTan[4] == 'green panties'", AlphaMask("images/KittySex/Kitty_Sex_Legs.png", "images/KittySex/Kitty_Sex_Panties_Green.png"),
            # "K_DynamicTan[0] and K_DynamicTan[4] == 'lace panties'", AlphaMask("images/KittySex/Kitty_Sex_Legs.png", "images/KittySex/Kitty_Sex_Panties_Lace.png"),   
            # "True", Null(),
            ),
        (0,0), ConditionSwitch(  
            "not K_DynamicTan[0] or not K_DynamicTan[5]", Null(), #hose
            "True", AlphaMask("images/KittySex/Kitty_Sex_Legs.png", GetModdedStringTanKitty("5", "_Legs.png", "Sex")),
            ),
        (0,0), ConditionSwitch(  
            "not K_DynamicTan[0] or not K_DynamicTan[2]", Null(),
            "True", AlphaMask("images/KittySex/Kitty_Sex_Legs.png", GetModdedStringTanKitty("2", ".png", "Sex")),
            # "K_DynamicTan[0] and K_DynamicTan[2] == 'shorts'", AlphaMask("images/KittySex/Kitty_Sex_Legs.png", "images/KittySex/Kitty_Sex_Shorts.png"),
            # "K_DynamicTan[0] and K_DynamicTan[2] == 'capris'", AlphaMask("images/KittySex/Kitty_Sex_Legs.png", "images/KittySex/Kitty_Sex_Pants_Blue.png"),
            # "K_DynamicTan[0] and K_DynamicTan[2] == 'black jeans'", AlphaMask("images/KittySex/Kitty_Sex_Legs.png", "images/KittySex/Kitty_Sex_Pants_Black.png"),
            # "True", Null(),   
            ),
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "K_Water", "images/KittySex/Kitty_Sex_Water_Legs.png",   
            "True", Null(),              
            ),  
        (0,0), "Kitty_Sex_Anus",                                                                          #Anus Composite 

        (0,0), "Kitty_Sex_Pussy",                                                                         #Pussy Composite

        (0,0), ConditionSwitch(                                                                                 #Panties if up
            "K_PantiesDown", Null(),     
            "not K_Panties", Null(),
            "'modded' in K_Panties and K_Wet", GetModdedString("images/KittySex/Kitty_Sex_Panties_", K_Panties, "_Wet.png"),
            "'modded' in K_Panties", GetModdedString("images/KittySex/Kitty_Sex_Panties_", K_Panties, ".png"),
            "K_Panties == 'green panties' and K_Wet", "images/KittySex/Kitty_Sex_Panties_Green_Wet.png",          
            "K_Panties == 'green panties'", "images/KittySex/Kitty_Sex_Panties_Green.png",    
            "K_Panties == 'lace panties' and K_Wet", "images/KittySex/Kitty_Sex_Panties_Lace_Wet.png",       
            "K_Panties == 'lace panties'", "images/KittySex/Kitty_Sex_Panties_Lace.png",    
            "K_Panties == 'bikini bottoms' and K_Wet", "images/KittySex/Kitty_Sex_Panties_Bikini_Wet.png",       
            "K_Panties == 'bikini bottoms'", "images/KittySex/Kitty_Sex_Panties_Bikini.png",    
            "True", Null(),                     
            ),
        (0,0), ConditionSwitch(        
            "not K_Hose", Null(),     
            "True", GetOutfitString("images/KittySex/Kitty_Sex_Hose_", K_Hose, "_Legs.png"),
            ), 
        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            "K_Legs == 'blue skirt'", "images/KittySex/Kitty_Sex_Skirt.png",   
            "not K_Legs", Null(),
            "not K_Upskirt and 'modded' in K_Legs and K_Wet > 1", GetModdedString("images/KittySex/Kitty_Sex_Legs_", K_Legs, "_Wet.png"),
            "K_Upskirt and 'modded' in K_Legs and 'skirt' in K_Legs", GetModdedString("images/KittySex/Kitty_Sex_Legs_", K_Legs, ".png"),
            "not K_Upskirt and'modded' in K_Legs", GetModdedString("images/KittySex/Kitty_Sex_Legs_", K_Legs, ".png"),
            "K_Upskirt", Null(),                            
            "K_Legs == 'capris' and K_Wet > 1", "images/KittySex/Kitty_Sex_Pants_Blue_Wet.png",
            "K_Legs == 'capris'", "images/KittySex/Kitty_Sex_Pants_Blue.png",
            "K_Legs == 'black jeans' and K_Wet > 1", "images/KittySex/Kitty_Sex_Pants_Black_Wet.png",
            "K_Legs == 'black jeans'", "images/KittySex/Kitty_Sex_Pants_Black.png",
            "K_Legs == 'shorts' and K_Wet > 1", "images/KittySex/Kitty_Sex_Shorts_Wet.png",
            "K_Legs == 'shorts'", "images/KittySex/Kitty_Sex_Shorts.png",
            "K_Legs == 'yoga pants' and K_Wet > 1", "images/KittySex/Kitty_Sex_Pants_Yoga_Wet.png",
            "K_Legs == 'yoga pants'", "images/KittySex/Kitty_Sex_Pants_Yoga.png",
            "True", Null(),                      
            ),   
        (0,0), ConditionSwitch(                                                                                 #Over Layer
            "K_Over == 'towel'", "images/KittySex/Kitty_Sex_Towel_Legs.png",
            "True", Null(),                    
            ),   
        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'belly' in K_Spunk", "images/KittySex/Kitty_Sex_Spunk_Pelvis.png",   
            "True", Null(),  
            ),  
        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer  
            "not P_Sprite or P_Cock != 'out'", Null(),                    
            "Speed >= 2", "Kitty_Hotdog_Zero_Anim2",
            "Speed", "Kitty_Hotdog_Zero_Anim1",
            "True", "Kitty_Hotdog_Zero_Anim0",   
            ), 
        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer  
            "not P_Sprite or P_Cock != 'foot'", Null(),                    
            "Speed >= 2", "Kitty_Footcock_Zero_Anim2",
            "Speed", "Kitty_Footcock_Zero_Anim1",
            "True", "Kitty_Footcock_Static",   
            ),
#        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer  
#            "not P_Sprite or P_Cock != 'foot'", Null(),                    
#            "Speed >= 2", At("Kitty_Footcock", Kitty_Footcock_Zero_Anim2A()),
#            "Speed", At("Kitty_Footcock", Kitty_Footcock_Zero_Anim1A()),
#            "True", At("Kitty_Footcock", Kitty_Footcock_StaticA()), 
#            ),   
#        (0,0), ConditionSwitch(                                                                                 #UI tool layer
#            "not UI_Tool", Null(),   
#            "UI_Tool", "Slap_Ass",  
#            "True", Null(),   
#            ),   
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "not Speed", "Kitty_Sex_Feet",  
            "P_Cock == 'anal' or P_Cock == 'in' or P_Cock == 'out'", AlphaMask("Kitty_Sex_Feet", "images/KittySex/Kitty_Sex_FeetMask.png"), 
            "True", "Kitty_Sex_Feet",            
            ),
        )
    
image Kitty_Sex_Feet:
    LiveComposite(                                                                                          
        #the lower legs used in the sex pose, referenced by Kitty_Sex_Legs
        (1120,840), 
        (0,0), ConditionSwitch(
            "K_DynamicTan[0]", "images/KittySex/Kitty_Sex_TFeet.png",                                                         #Legs Base
            "True", "images/KittySex/Kitty_Sex_Feet.png",
            ),
        (0,0), ConditionSwitch(  
            "not K_DynamicTan[0] or not K_DynamicTan[5]", Null(), #hose
            "True", AlphaMask("images/KittySex/Kitty_Sex_Feet.png", GetModdedStringTanKitty("5", "_Feet.png", "Sex")),
            ),
        (0,0), ConditionSwitch(  
            "not K_DynamicTan[0] or not K_DynamicTan[2]", Null(),
            "True", AlphaMask("images/KittySex/Kitty_Sex_Feet.png", GetModdedStringTanKitty("2", ".png", "SexFeet")),
            ),
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "K_Water", "images/KittySex/Kitty_Sex_Water_Feet.png",   
            "True", Null(),              
            ),
        (0,0), ConditionSwitch(
            "not K_Hose", Null(),     
            "True", GetOutfitString("images/KittySex/Kitty_Sex_Hose_", K_Hose, "_Feet.png"),
            ),
        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            "K_Upskirt", Null(),                               
            "not K_Legs", Null(),
            "'modded' in K_Legs", GetModdedString("images/KittySex/Kitty_Sex_Feet_", K_Legs, ".png"),
            "K_Legs == 'capris'", "images/KittySex/Kitty_Sex_Feet_Blue.png",
            "K_Legs == 'black jeans'", "images/KittySex/Kitty_Sex_Feet_Black.png",
            "K_Legs == 'yoga pants'", "images/KittySex/Kitty_Sex_Feet_Yoga.png",
            "True", Null(),                      
            ),   
        )
           
image TestingSolid:
        #this is a blank solid I use to test things.
        contains:
            Solid("#75d7ec", xysize=(1500,1500))
            alpha 0.2
            
#Start Animations for Kitty's Pussy during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_Pussy_Fucking0:
    # This is the visual for her pussy during the Speed 0 mode (static). 
    contains:
            # The background plate of her pussy
            "images/KittySex/Kitty_Sex_Pussy_Open.png"
    contains:
            # pubes
            ConditionSwitch(             
                "not K_Pubes", Null(),         
                "True", "images/KittySex/Kitty_Sex_Pubes_Open.png",  
                ),  
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Sex_Zero_Anim0", "Kitty_Pussy_Open_Mask") 
            
image Kitty_Pussy_Fucking1:
    # This is the visual for her pussy during the Speed 1 mode (heading). 
    contains:
            # The background plate of her pussy
            "images/KittySex/Kitty_Sex_Pussy_Open.png"
    contains:
            # pubes
            ConditionSwitch(             
                "not K_Pubes", Null(),         
                "True", "images/KittySex/Kitty_Sex_Pubes_Open.png",  
                ),  
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Sex_Zero_Anim1", "Kitty_Pussy_Open_Mask") 

image Kitty_Pussy_Fucking2:
    # This is the visual for her pussy during the Speed 2 mode (slow). 
    contains:
            # The background plate of her pussy
            "images/KittySex/Kitty_Sex_Pussy_Fucking.png"
    contains:
            # pubes
            ConditionSwitch(             
                "not K_Pubes", Null(),         
                "True", "images/KittySex/Kitty_Sex_Pubes_Fucking.png",  
                ),  
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Sex_Zero_Anim2", "Kitty_Pussy_Fucking_Mask") 
image Kitty_Pussy_Fucking3:  #rename this to 3
    # This is the visual for her pussy during the Speed 3 mode (fast). 
    contains:
            # The background plate of her pussy
            "images/KittySex/Kitty_Sex_Pussy_Fucking.png"
    contains:
            # pubes
            ConditionSwitch(             
                "not K_Pubes", Null(),         
                "True", "images/KittySex/Kitty_Sex_Pubes_Fucking.png",  
                ),  
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Sex_Zero_Anim3", "Kitty_Pussy_Fucking_Mask") 
            
image Kitty_Pussy_Fucking_Mask:
        #This is the mask image for Kitty's wide open pussy
        contains:
            "images/KittySex/Kitty_Sex_Pussy_Mask.png"   

image Kitty_Pussy_Open_Mask:                
        #This is the mask image for Kitty's wide open pussy
        contains:
            "images/KittySex/Kitty_Sex_Pussy_Mask.png"  
            yoffset 3            
            
#image TestMask:
#        #This involves a working, shrinking and growing mask for the pussy
#        contains:
#            "images/KittySex/Kitty_Sex_Pussy_Mask.png"
#            subpixel True
#            anchor (0.5,0.63)
#            pos (0.5,0.63)
#            zoom 1
#            block:
#                ease 1 zoom .5
#                pause 1
#                ease 3 zoom 1
#                repeat 

image Kitty_Pussy_Spunk_Heading:                
    "images/KittySex/Kitty_Sex_Spunk_Puss_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8
            
image Kitty_Sex_Pussy:            
    # This is the visual for her pussy during the Speed 0 mode (static).     
    contains:
            # The background plate of her pussy            
            ConditionSwitch(    
                "P_Sprite and P_Cock == 'in' and Speed >= 2", "images/KittySex/Kitty_Sex_Pussy_Fucking.png",
                "P_Sprite and P_Cock == 'in' and Speed", "images/KittySex/Kitty_Sex_Pussy_Open.png",
                "P_Sprite and P_Cock == 'in'", "images/KittySex/Kitty_Sex_Pussy_Closed.png",    
                "Trigger == 'lick pussy'", "images/KittySex/Kitty_Sex_Pussy_Open.png",   
                "True", "images/KittySex/Kitty_Sex_Pussy_Closed.png",
                )
    contains:
            # The background plate of her pussy            
            ConditionSwitch(    
                "not K_Wet", Null(),  
                "P_Sprite and P_Cock == 'in' and Speed >= 2", "images/KittySex/Kitty_Sex_WetPussy_F.png",
                "True", "images/KittySex/Kitty_Sex_WetPussy_C.png",
                )
    contains: 
            #ring piercing
            ConditionSwitch(  
                "K_Pierce != 'ring'", Null(),
                "not P_Sprite or P_Cock != 'in' or Speed <= 1", "images/KittySex/Kitty_Sex_Pussy_Ring.png",
                "True", "images/KittySex/Kitty_Sex_Pussy_RingF.png",
                ) 
    contains: 
            #barbell piercing
            ConditionSwitch(  
                "K_Pierce != 'barbell'", Null(),
                "not P_Sprite or P_Cock != 'in' or Speed <= 1", "images/KittySex/Kitty_Sex_Pussy_Barbell.png",
                "True", "images/KittySex/Kitty_Sex_Pussy_BarbellF.png",
                )             
    contains:
            # pubes
            ConditionSwitch(    
                "not K_Pubes", Null(),         
                "P_Sprite and P_Cock == 'in' and Speed >= 2", "images/KittySex/Kitty_Sex_Pubes_Fucking.png",
                "P_Sprite and P_Cock == 'in' and Speed", "images/KittySex/Kitty_Sex_Pubes_Open.png",
                "P_Sprite and P_Cock == 'in'", "images/KittySex/Kitty_Sex_Pubes_Closed.png", 
                "Trigger == 'lick pussy'", "images/KittySex/Kitty_Sex_Pubes_Open.png", 
                "True", "images/KittySex/Kitty_Sex_Pubes_Closed.png",
                )
    contains:
            #Spunk under penis
            ConditionSwitch(    
                "'in' in K_Spunk", "images/KittySex/Kitty_Sex_Spunk_Puss_Under.png",   
                "True", Null(),  
                )  
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            ConditionSwitch(    
                "not P_Sprite", Null(),  
                "P_Sprite and P_Cock == 'in' and Speed >= 3", AlphaMask("Kitty_Sex_Zero_Anim3", "Kitty_Pussy_Fucking_Mask"),
                "P_Sprite and P_Cock == 'in' and Speed >= 2", AlphaMask("Kitty_Sex_Zero_Anim2", "Kitty_Pussy_Fucking_Mask"),
                "P_Sprite and P_Cock == 'in' and Speed", AlphaMask("Kitty_Sex_Zero_Anim1", "Kitty_Pussy_Open_Mask"),
                "P_Sprite and P_Cock == 'in'", AlphaMask("Kitty_Sex_Zero_Anim0", "Kitty_Pussy_Open_Mask"),  
                "True", Null(),  
                )  
    contains:
            #Spunk over penis
            ConditionSwitch(    
                "'in' not in K_Spunk or not P_Sprite or P_Cock != 'in' or not Speed", Null(), 
                "Speed <= 1", "Kitty_Pussy_Spunk_Heading",   
                "True", "images/KittySex/Kitty_Sex_Spunk_Puss_Over.png",  
                )  
            
    #End Kitty Pussy composite
            
#End Animations for Kitty's Pussy during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Zero's Cock during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_Sex_Zero_Anim0:
        #this is Kitty's sex animation, Speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (498,530) #X less is left, Y less is up (498,520)
            zoom 1.4
            
image Kitty_Sex_Zero_Anim1:
        #this is Kitty's sex animation, Speed 1 (heading)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (498,525) #X less is left, Y less is up(498,520)
            zoom 1.4
            block:
                ease 1 pos (498,510) #(498,500)
                pause 1
                ease 3 pos (498,525)
                repeat 
            
image Kitty_Sex_Zero_Anim2:
        #this is Kitty's sex animation, Speed 2 (slow)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,490) #X less is left, Y less is up
            zoom 1.4
            block:
                ease 1 pos (500,380) #(500,470)
                pause 1
                ease 3 pos (500,490)
                repeat 
            
image Kitty_Sex_Zero_Anim3:
        #this is Kitty's sex animation, Speed 3 (fast)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,490) #X less is left, Y less is up
            zoom 1.4
            block:
                ease .25 pos (500,380) #(500,470)
                pause .25
                ease 1.5 pos (500,490)
                repeat 
#End Animations for Zero's Cock during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Kitty's Legs during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_Sex_Legs_Anim1:
        #this is the animation for Kitty's lower body during sex, Speed 1 (heading)
        contains:
            subpixel True
            "Kitty_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .25
                easein 1 pos (0,-5)
                pause 1
                ease 2.75 pos (0,0)
                repeat 
            
image Kitty_Sex_Legs_Anim2:            
        #this is the animation for Kitty's lower body during sex, Speed 2 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .5 pos (0,-15)
                ease .25 pos (0,-10)
                pause 1
                ease 2.75 pos (0,0)
                repeat 
            
image Kitty_Sex_Legs_Anim3:
        #this is the animation for Kitty's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Kitty_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds   
                pause .15
                easein .15 pos (0,-20)
                ease .10 pos (0,-15) 
                pause .20
                ease 1.4 pos (0,0)
                repeat 
#End Animations for Kitty's Legs during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Kitty's Body during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_Sex_Body_Anim1:
        #this is the animation for Kitty's upper body during sex, Speed 1 (heading)
        contains:
            subpixel True
            "Kitty_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 pos (0,-5)
                pause 1.25
                ease 2.5 pos (0,0)
                repeat 
            
image Kitty_Sex_Body_Anim2:            
        #this is the animation for Kitty's upper body during sex, Speed 2 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .6
                easein .4 pos (0,-10)
                ease .25 pos (0,-5)
                pause 1
                ease 2.75 pos (0,10)
                repeat 
            
image Kitty_Sex_Body_Anim3:
        #this is the animation for Kitty's upper body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Kitty_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds   
                pause .17
                easein .13 pos (0,-20)
                ease .10 pos (0,-15) 
                pause .20
                ease 1.4 pos (0,10)
                repeat 
#End Animations for Kitty's Body during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /            





#Start Animations for Kitty's Pussy during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Kitty_Sex_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(                                                                                             
            "P_Sprite and P_Cock == 'anal' and Speed >= 3", "images/KittySex/Kitty_Sex_Hole_Open.png",         
            "P_Sprite and P_Cock == 'anal' and Speed >= 2", "images/KittySex/Kitty_Sex_Hole_Open.png",
            "P_Sprite and P_Cock == 'anal' and Speed", "Kitty_Anal_Heading",
            "P_Sprite and P_Cock == 'anal'", "Kitty_Anal_Tip", 
            "K_Loose", "images/KittySex/Kitty_Sex_Hole_Loose.png",   
            "True", "images/KittySex/Kitty_Sex_Hole_Tight.png", 
            )    
    contains:
            #Spunk under penis
            ConditionSwitch(    
                "'anal' not in K_Spunk", Null(),  
                "P_Sprite and P_Cock != 'anal' and Speed >= 1", "images/KittySex/Kitty_Sex_Spunk_Anal_Under.png",  
                "P_Sprite and P_Cock != 'anal' and Speed == 1", "Kitty_Anal_Spunk_Heading_Under",
                "True", "images/KittySex/Kitty_Sex_Spunk_Anal_Closed.png",  
                )  
    contains:
            # The animation of Zero's moving penis, masked by her anus shape
            ConditionSwitch(               
            "not P_Sprite or P_Cock != 'anal'", Null(),                                                                                    
            "Speed >= 3",  AlphaMask("Kitty_Anal_Zero_Anim3", "Kitty_Anal_Fucking_Mask"),        
            "Speed >= 2", AlphaMask("Kitty_Anal_Zero_Anim2", "Kitty_Anal_Fucking_Mask"),
            "Speed", AlphaMask("Kitty_Anal_Zero_Anim1", "Kitty_Anal_Fucking_Mask"),
            "True", AlphaMask("Kitty_Anal_Zero_Anim0", "Kitty_Anal_Fucking_Mask"), 
            )    
    contains:
            #Spunk over penis
            ConditionSwitch(    
                "'anal' not in K_Spunk or not P_Sprite or P_Cock != 'anal' or not Speed", Null(),  
                "Speed == 1", "Kitty_Anal_Spunk_Heading_Over",
                "True", "images/KittySex/Kitty_Sex_Spunk_Anal_Over.png",  
                )  
            
                
image Kitty_Anal_Fucking0:
    # This is the visual for her pussy during the Speed 0 mode (static). 
    contains:
            # The background plate of her pussy
            "Kitty_Anal_Tip"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Anal_Zero_Anim0", "Kitty_Anal_Fucking_Mask") 
            
image Kitty_Anal_Fucking1:
    # This is the visual for her pussy during the Speed 1 mode (heading). 
    contains:
            # The background plate of her pussy
            "Kitty_Anal_Heading"
#            "images/KittySex/Kitty_Sex_Hole_Open.png"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Anal_Zero_Anim1", "Kitty_Anal_Fucking_Mask") 

image Kitty_Anal_Fucking2:
    # This is the visual for her pussy during the Speed 2 mode (slow). 
    contains:
            # The background plate of her pussy
            "images/KittySex/Kitty_Sex_Hole_Open.png"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Anal_Zero_Anim2", "Kitty_Anal_Fucking_Mask") 
            
image Kitty_Anal_Fucking3:  
    # This is the visual for her pussy during the Speed 3 mode (fast). 
    contains:
            # The background plate of her pussy
            "images/KittySex/Kitty_Sex_Hole_Open.png"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Anal_Zero_Anim3", "Kitty_Anal_Fucking_Mask") 
            
image Kitty_Anal_Fucking_Mask:
        #This is the mask image for Kitty's wide open pussy
        contains:
            "images/KittySex/Kitty_Sex_Hole_Mask.png"               

image Kitty_Anal_Open_Mask:            
        #This is the mask image for Kitty's wide open pussy
        contains:
            "images/KittySex/Kitty_Sex_Hole_Mask.png"  
            yoffset 3

image Kitty_Anal_Heading:                
    "images/KittySex/Kitty_Sex_Hole_Open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
    block:
        #total 5 second
        ease .75 xzoom 1.0        
        ease .25 xzoom 0.9
        pause 1.50      
        ease .25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat 

image Kitty_Anal_Spunk_Heading_Over:                
    "images/KittySex/Kitty_Sex_Spunk_Anal_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8
    block:
        #total 5 second
        ease .75 xzoom 1.0   #(1.0)     
        pause 1.75      
        ease .25 xzoom 1.0  #(1.0) 
        ease 2.25 xzoom 0.8   #(0.6)
        repeat 
image Kitty_Anal_Spunk_Heading_Under:                
    "images/KittySex/Kitty_Sex_Spunk_Anal_Under.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
    block:
        #total 5 second
        ease .75 xzoom 1.0        
        ease .25 xzoom 0.95
        pause 1.50      
        ease .25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat 

image Kitty_Anal_Tip:                
    "images/KittySex/Kitty_Sex_Hole_Open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
            
#End Animations for Kitty's Pussy during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Zero's Cock during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_Anal_Zero_Anim0:
        #this is Kitty's sex animation, Speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,600) #X less is left, Y less is up (498,520)
            zoom 1.4
            
image Kitty_Anal_Zero_Anim1:
        #this is Kitty's sex animation, Speed 1 (heading)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,600) #X less is left, Y less is up
            zoom 1.4
            block:
                ease 1 pos (500,570) #(500,470)
                pause 1
                ease 3 pos (500,600)
                repeat 
            
image Kitty_Anal_Zero_Anim2:
        #this is Kitty's sex animation, Speed 2 (slow)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,570) #X less is left, Y less is up
            zoom 1.4
            block:
                ease 1 pos (500,450) #(500,470)
                pause 1
                ease 3 pos (500,570)
                repeat 
            
image Kitty_Anal_Zero_Anim3:
        #this is Kitty's sex animation, Speed 3 (fast)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,570) #X less is left, Y less is up
            zoom 1.4
            block:
                ease .25 pos (500,450) #(500,470)
                pause .25
                ease 1.5 pos (500,570)
                repeat 
#End Animations for Zero's Cock during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Zero's Cock during Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_Hotdog_Zero_Anim0:
        #this is Kitty's sex animation, Speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (498,570) #X less is left, Y less is up
            zoom 1.4
            
image Kitty_Hotdog_Zero_Anim1:
        #this is Kitty's sex animation, Speed 1 (heading)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (498,500) #X less is left, Y less is up
            zoom 1.4
            block:
                ease 1 pos (498,560) #(500,500)
                pause .5
                ease 1.5 pos (498,500)
                repeat 

image Kitty_Hotdog_Zero_Anim2:
        #this is Kitty's sex animation, Speed 3 (fast)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,510) #X less is left, Y less is up
            zoom 1.4
            block:
                ease .5 pos (500,400) #(500,470)
                pause .5
                ease 1 pos (500,510)
                repeat 

image Kitty_Hotdog_Body_Anim2:
        #this is the animation for Kitty's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Kitty_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds   
                pause .30
                ease .50 pos (0,-10)
                pause .20
                ease 1 pos (0,0)
                repeat 
                
image Kitty_Hotdog_Legs_Anim2:
        #this is the animation for Kitty's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Kitty_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds   
                pause .20
                ease .50 pos (0,-10)
                pause .20
                ease 1.1 pos (0,0)
                repeat 
                
#End Animations for Zero's Cock during Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Kitty's Legs during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Kitty_Footcock:   
    contains:
            subpixel True
            "Blowcock"
            alpha 0.8
            zoom 0.7
            anchor (0.5,0.5)
            offset (465,70)
            pos (0,0)
    pos (750,230)

image Kitty_Footcock_Static:    
    contains:
            subpixel True
            "Kitty_Footcock"
            pos (392,295)
    pos (750,230)
                
image Kitty_Footcock_Zero_Anim1:
    contains:
            subpixel True
            "Kitty_Footcock"
            pos (392,295)
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 ypos 360#65
                ease .25 ypos 355#60
                pause 1
                ease 2.50 ypos 270#285
                repeat 
    pos (750,230)
              
image Kitty_Footcock_Zero_Anim2:
    contains:
            subpixel True
            "Kitty_Footcock"
            pos (392,295)
            block:
                #Total time, 4 seconds
                pause .2
                easein .4 ypos 360
                ease .2 ypos 355
                pause .2
                ease 1.00 ypos 270
                repeat
    pos (750,230)

transform Kitty_Footcock_Zero_Anim1A():
            subpixel True
            offset (0,0)
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 yoffset 60#65
                ease .25 yoffset 55#60
                pause 1
                ease 1.50 yoffset -30#285
                repeat 
                
transform Kitty_Footcock_Zero_Anim2A():
            subpixel True
            offset (0,0)
            block:
                #Total time, 2 seconds
                pause .2
                easein .4 yoffset 60
                ease .2 yoffset 55
                pause .2
                ease 1.00 yoffset -30
                pause .2
                easein .4 yoffset 60
                ease .2 yoffset 55
                pause .2
                ease 1.00 yoffset -30
                repeat 
                
transform Kitty_Footcock_StaticA():  
            subpixel True
            offset (0,-5)
            block:
                #Total time, 4 seconds
                pause .5
                ease 1 yoffset 0
                pause 1
                ease 1.50 yoffset -5
                repeat 
            
image Kitty_Sex_Legs_FootAnim1:            
        #this is the animation for Kitty's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (0,-65)
                ease .25 pos (0,-60)
                pause 1
                ease 2.50 pos (0,25)#(0,10)
                repeat 
        pos (750,230)
                
image Kitty_Sex_Legs_FootAnim2:            
        #this is the animation for Kitty's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .2
                easein .4 pos (0,-65)
                ease .2 pos (0,-60)
                pause .2
                ease 1.0 pos (0,25)#(0,10)
                repeat 
        pos (750,230)
                
image Kitty_Sex_Legs_FootAnimStatic:            
        #this is the animation for Kitty's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
        pos (750,230)
           
transform Kitty_Sex_Legs_FootAnim1A():            
        #this is the animation for Kitty's lower body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 yoffset -65
                ease .25 yoffset -60
                pause 1
                ease 1.50 yoffset 25
                repeat 
                
transform Kitty_Sex_Legs_FootAnim2A():            
        #this is the animation for Kitty's lower body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .2
                easein .4 yoffset -65
                ease .2 yoffset -60
                pause .2
                ease 1.0 yoffset 25
                pause .2
                easein .4 yoffset -65
                ease .2 yoffset -60
                pause .2
                ease 1.0 yoffset 25
                repeat 
                
transform Kitty_Sex_Legs_FootAnimStaticA():            
        #this is the animation for Kitty's lower body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                ease 1 yoffset -5
                pause 1
                ease 1.50 yoffset 0
                repeat 
                
#End Animations for Kitty's Legs during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Kitty's Body during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
            
image Kitty_Sex_Body_FootAnim1:            
        #this is the animation for Kitty's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 pos (0,-25)#(0,-5)
                ease .25 pos (0,-15)#(0,0)
                pause 1
                ease 2.50 pos (0,15)#(0,5)
                repeat 
        pos (750,230)
  
image Kitty_Sex_Body_FootAnim2:            
        #this is the animation for Kitty's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .2
                easein .4 pos (0,-25)#(0,-5)
                ease .2 pos (0,-15)#(0,0)
                pause .2
                ease 1.0 pos (0,15)#(0,5)
                repeat 
        pos (750,230)
                
image Kitty_Sex_Body_FootAnimStatic:            
        #this is the animation for Kitty's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Body"
            pos (0,0) #X less is left, Y less is up
        pos (750,230)
 
transform Kitty_Sex_Body_FootAnim1A():            
        #this is the animation for Kitty's upper body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 yoffset -25
                ease .25 yoffset -15
                pause 1
                ease 1.50 yoffset 15
                repeat 
  
transform Kitty_Sex_Body_FootAnim2A():            
        #this is the animation for Kitty's upper body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .2
                easein .4 yoffset -25
                ease .2 yoffset -15
                pause .2
                ease 1.0 yoffset 15
                pause .2
                easein .4 yoffset -25
                ease .2 yoffset -15
                pause .2
                ease 1.0 yoffset 15
                repeat 
                
transform Kitty_Sex_Body_FootAnimStaticA():            
        #this is the animation for Kitty's upper body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                ease 1 yoffset -5
                pause 1
                ease 1.50 yoffset 0
                repeat 
#End Animations for Kitty's Body during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     Sex Launch/Reset
label Kitty_Sex_Launch(Line = "solo"): 
    if Line == "sex":        
        $ P_Cock = "in"
    elif Line == "anal":
        $ P_Cock = "anal"
    elif Line == "solo":   
        $ P_Sprite = 0
        $ P_Cock = "out"
    elif Line == "hotdog":          
        $ P_Cock = "out"
    elif Line == "foot":          
        $ P_Cock = "foot"
    if not Trigger:
        $ Trigger = Line
    if renpy.showing("Kitty_SexSprite"):
        return 
    $ P_Sprite = 1
    $ Speed = 0
    hide Kitty_Sprite    
    if renpy.showing("Kitty_BJ_Animation"):
        hide Kitty_BJ_Animation
    if renpy.showing("Kitty_HJ_Animation"):
        hide Kitty_HJ_Animation
    if renpy.showing("Kitty_TJ_Animation"):
        hide Kitty_TJ_Animation
    show Kitty_SexSprite zorder 150
#    show Kitty_SexSprite zorder 150:
#        pos (750,230)

    with dissolve
    return
    
#MOD MARKER RESET
label Kitty_Sex_Reset:
    if not renpy.showing("Kitty_SexSprite") and not renpy.showing("Kitty_Doggy"):
        return
    $ Kitty_Arms = 2     
    call mod_hide_Kitty_SexSprite
    call Kitty_Hide 
#    call Set_The_Scene(Dress = 0)    
    show Kitty_Sprite at SpriteLoc(K_SpriteLoc) zorder KittyLayer:
        alpha 1
        zoom 1 offset (0,0) 
        anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return
    
# End Kitty Sex pose Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    
    







# Start Kitty Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Kitty BJ element ///////////////////////////////////////////////////////////////////////////                                     Core Kitty BJ element
#Kitty BJ Over Sprite Compositing


image Kitty_BJ_Animation:#BJ_NewTest:                                                                #core BJ animation   
    LiveComposite(    
        (858,928),      
        (0,0), ConditionSwitch(                                                                 
            # Kitty's body, everything below the chin
            "Speed == 0", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_0()),           #Static
            "Speed == 1", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_1()),           #Licking
            "Speed == 2", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_2()),           #Heading
            "Speed == 3", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_3()),           #Sucking
            "Speed == 4", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_4()),           #Deepthroat
            "Speed == 5", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_5()),           #Cumming High
            "Speed == 6", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_6()),           #Cumming Deep
            "True", Null(),
            ),    
        (-270,-160), ConditionSwitch(                                                                 
            # Kitty's head Underlay
            "Speed == 0", At("Kitty_BJ_Head", Kitty_BJ_Head_0()),               #Static
            "Speed == 1", At("Kitty_BJ_Head", Kitty_BJ_Head_1()),               #Licking
            "Speed == 2", At("Kitty_BJ_Head", Kitty_BJ_Head_2()),               #Heading
            "Speed == 3", At("Kitty_BJ_Head", Kitty_BJ_Head_3()),               #Sucking
            "Speed == 4", At("Kitty_BJ_Head", Kitty_BJ_Head_4()),               #Deepthroat
            "Speed == 5", At("Kitty_BJ_Head", Kitty_BJ_Head_5()),               #Cumming High
            "Speed == 6", At("Kitty_BJ_Head", Kitty_BJ_Head_6()),               #Cumming Deep
            "True", Null(),
            ),   
        (0,0), ConditionSwitch(                                                                 
            # Cock
            "Speed == 0", At("Blowcock", Kitty_BJ_Cock_0()),                    #Static
            "Speed == 1", At("Blowcock", Kitty_BJ_Cock_1()),                    #Licking                        
            "Speed >= 2", At("Blowcock", Kitty_BJ_Cock_2()),                    #Heading+                        
#            "Speed == 2", At("Blowcock", Kitty_BJ_Cock_2()),                    #Heading
#            "Speed == 3", At("Blowcock", Kitty_BJ_Cock_2()),                    #Sucking                     
#            "Speed == 4", At("Blowcock", Kitty_BJ_Cock_2()),                    #Deepthroat
            "True", Null(),
            ),    
        (-270,-160), ConditionSwitch(                                                                 
            # the masked overlay for when her head overlaps the cock
            "Speed < 3", Null(), 
            "Speed == 3", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MouthSuckingMask"), Kitty_BJ_Head_3()), #Sucking
            "Speed == 4", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MouthSuckingMask"), Kitty_BJ_Head_4()), #Deepthroat
            "Speed == 6", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MouthSuckingMask"), Kitty_BJ_Head_6()), #Cumming Deep
            "True", Null(),
            ),    
        (-270,-160), ConditionSwitch(                                                                 
            # same as above, but for the heading animation
            "Speed == 2", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MaskHeadingComposite"), Kitty_BJ_Head_2()), #Heading
            "Speed == 5", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MaskHeadingComposite"), Kitty_BJ_Head_5()), #Cumming High
            "True", Null(),
            ),            
        (325,490), ConditionSwitch(                                                                
            # the over part of spunk
            "Speed < 3 or 'mouth' not in K_Spunk", Null(),
            "Speed == 3", At("KittySuckingSpunk", Kitty_BJ_Head_3()), #Sucking
            "Speed == 4", At("KittySuckingSpunk", Kitty_BJ_Head_4()), #Deepthroat
            "Speed == 6", At("KittySuckingSpunk", Kitty_BJ_Head_6()), #Cumming Deep
            "True", Null(),
            ),    
        (325,490), ConditionSwitch(                                                                 
            # same as above, but for the heading animation
            "Speed == 2 and 'mouth' in K_Spunk", At("Kitty_BJ_MaskHeadingSpunk", Kitty_BJ_Head_2()), #Heading
            "Speed == 5 and 'mouth' in K_Spunk", At("Kitty_BJ_MaskHeadingSpunk", Kitty_BJ_Head_5()), #Cumming High
            "True", Null(),
            ),   
        )
    zoom .55
    anchor (.5,.5)
    
image Kitty_BJ_HairBack:
    #Hair underlay
    ConditionSwitch(                                                                            
            "K_Water and K_Hair == 'evo'", im.MatrixColor("images/KittyBJFace/Kitty_BJ_Hair" + GetHairColor(K_HairColor) + "BackWet.png",im.matrix.tint(float(K_HairCustomColor.red)/255.0, float(K_HairCustomColor.green)/255.0, float(K_HairCustomColor.blue)/255.0)),
            "K_Hair == 'long'", im.MatrixColor("images/KittyBJFace/Kitty_BJ_Hair" + GetHairColor(K_HairColor) + "BackWet.png",im.matrix.tint(float(K_HairCustomColor.red)/255.0, float(K_HairCustomColor.green)/255.0, float(K_HairCustomColor.blue)/255.0)),
            "True", Null(),
            ),
    zoom 1.4
    anchor (0.5, 0.5)
    yoffset 50
    
#image Kitty_BJ_Backdrop:                                                                        #Her Body under the head
#    "Kitty_Sprite"
#    zoom 4.8 #4.5
#    pos (175,-110)
#    offset (-500,-280)#(-450,-200) #(-615, -125)
    
image Kitty_BJ_Backdrop:                                                                        
    #Her Body under the head
    LiveComposite(    
        (858,928),  
        (-375,250), ConditionSwitch(                                                                         
            #blanket
            "'blanket' in K_RecentActions", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                         
            #red shirt under
            "K_Over == 'red shirt'", "images/KittyBJFace/Kitty_BJ_Over_RedUnder.png",
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                         
            #body
            "K_DynamicTan[0]", "images/KittyBJFace/Kitty_BJ_T3Body.png",
            "True", "images/KittyBJFace/Kitty_BJ_Body.png", 
            ),
        (0,0), ConditionSwitch(                                                                         
            #chest tan body
            "not K_DynamicTan[3] or not K_DynamicTan[0]", Null(),
            "True", AlphaMask("images/KittyBJFace/Kitty_BJ_Body.png", GetModdedStringTanKitty("3", ".png", "BJFace")),
            ), 
        (0,0), ConditionSwitch(                                                                         
            #over tan body
            "not K_DynamicTan[1] or not K_DynamicTan[0]", Null(),
            "True", AlphaMask("images/KittyBJFace/Kitty_BJ_Body.png", GetModdedStringTanKitty("1", ".png", "BJFace")),
            ),     
        (0,0), ConditionSwitch(                                                                         
            #necklace
            "K_Neck == 'gold necklace'", "images/KittyBJFace/Kitty_BJ_Neck_Gold.png",
            "K_Neck == 'star necklace'", "images/KittyBJFace/Kitty_BJ_Neck_Star.png",
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                  
            # piercings
            "not K_Pierce", Null(),                       
            "K_Pierce == 'ring'", "images/KittyBJFace/Kitty_BJ_PierceRing.png",      
            "True", "images/KittyBJFace/Kitty_BJ_PierceBall.png",   
            ),   
        (0,0), ConditionSwitch(                                                                         
            # wet body
            "not K_Water", Null(),
            "True", "images/KittyBJFace/Kitty_BJ_Wet_Body.png",
            ),  
            
        (0,0), ConditionSwitch(                                                                        
            #Bra
            "not K_Chest", Null(),
            "'modded' in K_Chest", GetModdedString("images/KittyBJFace/Kitty_BJFace_", K_Chest, ".png"),
            "K_Chest == 'lace bra'", "images/KittyBJFace/Kitty_BJ_Bra_Lace.png",
            "K_Chest == 'sports bra'", "images/KittyBJFace/Kitty_BJ_Bra_Sport.png",
            "K_Chest == 'bra'", "images/KittyBJFace/Kitty_BJ_Bra.png",
            "K_Chest == 'cami'", "images/KittyBJFace/Kitty_BJ_Bra_Cami.png",
            "True", Null(),       
            ),  
            
        (0,0), ConditionSwitch(                                                                         
            #Shirt
            "not K_Over", Null(),
            "'modded' in K_Over", GetModdedString("images/KittyBJFace/Kitty_BJFace_", K_Over, ".png"),
            "K_Over == 'pink top'", "images/KittyBJFace/Kitty_BJ_Over_PinkShirt.png",
            "K_Over == 'red shirt'", "images/KittyBJFace/Kitty_BJ_Over_RedShirt.png",
            "K_Over == 'towel'", "images/KittyBJFace/Kitty_BJ_Over_Towel.png",
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                         
            #Spunk
            "'tits' not in K_Spunk", Null(),
            "True", "images/KittyBJFace/Kitty_BJ_Spunk_Body.png",
            ),  
        )
    zoom 1.5 
    offset (-300,-200)
    
image Kitty_BJ_Head:                                                                            #These are all the details of the face
    LiveComposite(    
        (858,928), 
        (0,0), ConditionSwitch(                                                                 
            #Hair back
            "K_Water or K_Hair == 'wet'", im.MatrixColor("images/KittyBJFace/Kitty_BJ_Hair" + GetHairColor(K_HairColor) + "BackWet.png",im.matrix.tint(float(K_HairCustomColor.red)/255.0, float(K_HairCustomColor.green)/255.0, float(K_HairCustomColor.blue)/255.0)), #AlphaMask("images/KittyBJFace/Kitty_BJ_HairBackWet.png", "Kitty_BJ_Backdrop"),
            "True", Null(),
            ),   
#        (0,0), ConditionSwitch(       #Legacy, the bellow version should do the same role                                                          
#            # Underface for sucking 
#            "Speed > 2 and Speed != 5", Null(),            
#            "K_Water and K_Blush", "images/KittyBJFace/Kitty_BJ_FaceClosed_Wet_Blush.png",    
#            "K_Water", "images/KittyBJFace/Kitty_BJ_FaceClosed_Wet.png", 
#            "K_Blush", "images/KittyBJFace/Kitty_BJ_FaceClosed_Blush.png",              
#            "True", "images/KittyBJFace/Kitty_BJ_FaceClosed.png"
#            ),   
#        (0,0), ConditionSwitch(                                                                 
#            # Underface for not sucking 
#            "Speed <= 2 or Speed == 5", Null(),   #"Speed <= 2 or Trigger != 'blow' or Speed == 5", Null(), 
#            "K_Water and K_Blush", "images/KittyBJFace/Kitty_BJ_FaceOpen_Wet_Blush.png",    
#            "K_Water", "images/KittyBJFace/Kitty_BJ_FaceOpen_Wet.png", 
#            "K_Blush", "images/KittyBJFace/Kitty_BJ_FaceOpen_Blush.png",              
#            "True", "images/KittyBJFace/Kitty_BJ_FaceOpen.png"
#            ),          
        (0,0), ConditionSwitch(
            # Basic Face layer
            "Speed <= 2 or Speed == 5 or not renpy.showing('Kitty_BJ_Animation')", ConditionSwitch( 
                    # If the animation isn't sucking, or if not in BJ pose                    
                    "K_Water", ConditionSwitch( 
                            # If she's wet
                            "K_Blush and K_DynamicTan[0]", "images/KittyBJFace/Kitty_BJ_TFaceClosed_Wet_Blush.png",             
                            "K_Blush", "images/KittyBJFace/Kitty_BJ_FaceClosed_Wet_Blush.png",             
                            "True and K_DynamicTan[0]", "images/KittyBJFace/Kitty_BJ_TFaceClosed_Wet.png", 
                            "True", "images/KittyBJFace/Kitty_BJ_FaceClosed_Wet.png", 
                            ),  
                    "K_Blush and K_DynamicTan[0]", "images/KittyBJFace/Kitty_BJ_TFaceClosed_Blush.png",              
                    "K_Blush", "images/KittyBJFace/Kitty_BJ_FaceClosed_Blush.png",              
                    "True and K_DynamicTan[0]", "images/KittyBJFace/Kitty_BJ_TFaceClosed.png",
                    "True", "images/KittyBJFace/Kitty_BJ_FaceClosed.png",
                    ), 
            #if it is in the open, sucking position
            "K_Water", ConditionSwitch( 
                    # If she's wet
                    "K_Blush and K_DynamicTan[0]", "images/KittyBJFace/Kitty_BJ_TFaceOpen_Wet_Blush.png",              
                    "K_Blush", "images/KittyBJFace/Kitty_BJ_FaceOpen_Wet_Blush.png",              
                    "True and K_DynamicTan[0]", "images/KittyBJFace/Kitty_BJ_TFaceOpen_Wet.png", 
                    "True", "images/KittyBJFace/Kitty_BJ_FaceOpen_Wet.png", 
                    ),  
            "K_Blush and K_DynamicTan[0]", "images/KittyBJFace/Kitty_BJ_TFaceOpen_Blush.png",             
            "K_Blush", "images/KittyBJFace/Kitty_BJ_FaceOpen_Blush.png",             
            "True and K_DynamicTan[0]",  "images/KittyBJFace/Kitty_BJ_TFaceOpen.png",
            "True",  "images/KittyBJFace/Kitty_BJ_FaceOpen.png",
            ),    
        (0,0), ConditionSwitch(                                                                         
            #Mouth
            "Speed and renpy.showing('Kitty_BJ_Animation')", ConditionSwitch( 
                  "Speed == 1", "images/KittyBJFace/Kitty_BJ_Mouth_Tongue.png",  #licking
                  "(Speed == 2 or Speed == 5)", Null(),                          #heading
                  "Speed == 3", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png", #sucking
                  "Speed == 4", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png", #deepthroat     
                  "Speed == 6", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png", #cumming        
                  "True", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png", #cumming     
                  ), 
            "Speed == 3 and renpy.showing('Kitty_TJ_Animation')", "images/KittyBJFace/Kitty_BJ_Mouth_Tongue.png",                        
            "Speed >= 5 and renpy.showing('Kitty_TJ_Animation')", "images/KittyBJFace/Kitty_BJ_Mouth_Kiss.png",
            "K_Mouth == 'normal' and K_DynamicTan[0]", "images/KittyBJFace/Kitty_BJ_TMouth_Smile.png",
            "K_Mouth == 'normal'", "images/KittyBJFace/Kitty_BJ_Mouth_Smile.png",
            "K_Mouth == 'lipbite' and K_DynamicTan[0]", "images/KittyBJFace/Kitty_BJ_TMouth_Lipbite.png",
            "K_Mouth == 'lipbite'", "images/KittyBJFace/Kitty_BJ_Mouth_Lipbite.png",
            "K_Mouth == 'sucking'", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png",            
            "K_Mouth == 'kiss' and K_DynamicTan[0]", "images/KittyBJFace/Kitty_BJ_TMouth_Kiss.png",
            "K_Mouth == 'kiss'", "images/KittyBJFace/Kitty_BJ_Mouth_Kiss.png",
            "K_Mouth == 'sad' and K_DynamicTan[0]", "images/KittyBJFace/Kitty_BJ_TMouth_Sad.png",
            "K_Mouth == 'sad'", "images/KittyBJFace/Kitty_BJ_Mouth_Sad.png",
            "K_Mouth == 'smile' and K_DynamicTan[0]", "images/KittyBJFace/Kitty_BJ_TMouth_Smile.png",
            "K_Mouth == 'smile'", "images/KittyBJFace/Kitty_BJ_Mouth_Smile.png",
            "K_Mouth == 'grimace' and K_DynamicTan[0]", "images/KittyBJFace/Kitty_BJ_TMouth_Smile.png",
            "K_Mouth == 'grimace'", "images/KittyBJFace/Kitty_BJ_Mouth_Smile.png",
            "K_Mouth == 'surprised'", "images/KittyBJFace/Kitty_BJ_Mouth_Surprised.png",          
            "K_Mouth == 'tongue'", "images/KittyBJFace/Kitty_BJ_Mouth_Tongue.png",    
            "True", "images/KittyBJFace/Kitty_BJ_Mouth_Smile.png",
            ),        
        (428,605), ConditionSwitch(   
            # Heading Mouth
#            "Speed == 2 and Trigger == 'blow'", At("Kitty_BJ_MouthHeading", Kitty_BJ_MouthAnim()),  #heading 
            "not renpy.showing('Kitty_BJ_Animation')", Null(),      
            "Speed == 2", At("Kitty_BJ_MouthHeading", Kitty_BJ_MouthAnim()),  #heading 
            "Speed == 5", At("Kitty_BJ_MouthHeading", Kitty_BJ_MouthAnimC()), #cumming high   
            "True", Null(),
            ),                  
        (0,0), ConditionSwitch(                                                                         
            #Spunk layer
            "'mouth' not in K_Spunk", Null(), 
            "Speed and renpy.showing('Kitty_BJ_Animation')", ConditionSwitch( 
                    # If in sucking position
                    "Speed == 1", "images/KittyBJFace/Kitty_BJ_Spunk_Tongue.png",  #licking
                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png", #sucking
                    "Speed == 4", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png", #deepthroat 
                    "True", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png", #cumming     
                    ),  
            "Speed >= 5 and renpy.showing('Kitty_TJ_Animation')", "images/KittyBJFace/Kitty_BJ_Spunk_Kiss.png",
            "K_Mouth == 'normal'", "images/KittyBJFace/Kitty_BJ_Spunk_Smile.png",
            "K_Mouth == 'lipbite'", "images/KittyBJFace/Kitty_BJ_Spunk_Lipbite.png",
            "K_Mouth == 'kiss'", "images/KittyBJFace/Kitty_BJ_Spunk_Kiss.png",
            "K_Mouth == 'sad'", "images/KittyBJFace/Kitty_BJ_Spunk_Kiss.png",
            "K_Mouth == 'smile'", "images/KittyBJFace/Kitty_BJ_Spunk_Smile.png",
            "K_Mouth == 'surprised'", "images/KittyBJFace/Kitty_BJ_Spunk_Surprised.png",
            "K_Mouth == 'tongue'", "images/KittyBJFace/Kitty_BJ_Spunk_Tongue.png",
            "K_Mouth == 'sucking'", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png", #fix add
            "True", Null(),
            ),       
        (0,0), ConditionSwitch(                                                                         
            #Brows
            "K_Brows == 'normal' and K_DynamicTan[0]", "images/KittyBJFace/Kitty_BJ_TBrows_Normal.png",
            "K_Brows == 'normal'", "images/KittyBJFace/Kitty_BJ_Brows_Normal.png",
            "K_Brows == 'angry' and K_DynamicTan[0]", "images/KittyBJFace/Kitty_BJ_TBrows_Angry.png",
            "K_Brows == 'angry'", "images/KittyBJFace/Kitty_BJ_Brows_Angry.png",
            "K_Brows == 'sad' and K_DynamicTan[0]", "images/KittyBJFace/Kitty_BJ_TBrows_Sad.png",
            "K_Brows == 'sad'", "images/KittyBJFace/Kitty_BJ_Brows_Sad.png",
            "K_Brows == 'surprised' and K_DynamicTan[0]", "images/KittyBJFace/Kitty_BJ_TBrows_Surprised.png",
            "K_Brows == 'surprised'", "images/KittyBJFace/Kitty_BJ_Brows_Surprised.png",        
            "K_Brows == 'confused' and K_DynamicTan[0]", "images/KittyBJFace/Kitty_BJ_TBrows_Confused.png",
            "K_Brows == 'confused'", "images/KittyBJFace/Kitty_BJ_Brows_Confused.png",
            "True", "images/KittyBJFace/Kitty_BJ_Brows_Normal.png",
            ),
        (0,0), "Kitty BJ Blink",                                                                
            #Eyes
        (0,0), ConditionSwitch(                                                                 
            #cum on the face
            "'facial' in K_Spunk", "images/KittyBJFace/Kitty_BJ_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                 
            #Hair overlay
            "K_Water or K_Hair == 'wet'", im.MatrixColor("images/KittyBJFace/Kitty_BJ_Hair" + GetHairColor(K_HairColor) + "_Wet.png",im.matrix.tint(float(K_HairCustomColor.red)/255.0, float(K_HairCustomColor.green)/255.0, float(K_HairCustomColor.blue)/255.0)),
            "K_Hair == 'long'", im.MatrixColor("images/KittyBJFace/Kitty_BJ_Hair" + GetHairColor(K_HairColor) + "_Long.png",im.matrix.tint(float(K_HairCustomColor.red)/255.0, float(K_HairCustomColor.green)/255.0, float(K_HairCustomColor.blue)/255.0)),
            "K_Hair == 'evo'", im.MatrixColor("images/KittyBJFace/Kitty_BJ_Hair" + GetHairColor(K_HairColor) + "_Evo.png",im.matrix.tint(float(K_HairCustomColor.red)/255.0, float(K_HairCustomColor.green)/255.0, float(K_HairCustomColor.blue)/255.0)),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                 
            #Hair water overlay
            "not K_Water", Null(),            
            "Speed > 2", "images/KittyBJFace/Kitty_BJ_Wet_HeadOpen.png",         
            "True", "images/KittyBJFace/Kitty_BJ_Wet_HeadClosed.png",
            ),        
        (0,0), ConditionSwitch(                                                                 
            #cum on the hair
            "'hair' in K_Spunk", "images/KittyBJFace/Kitty_BJ_Spunk_Hair.png",
            "True", Null(),
            ),
        )
    zoom 1.4
    anchor (0.5, 0.5)

image Kitty BJ Blink:                                                                           
        #eyeblinks
        ConditionSwitch(
            "K_Eyes == 'normal'", "images/KittyBJFace/Kitty_BJ_Eyes_Normal.png",  
            "K_Eyes == 'sexy'", "images/KittyBJFace/Kitty_BJ_Eyes_Sexy.png",  
            "K_Eyes == 'closed'", "images/KittyBJFace/Kitty_BJ_Eyes_Closed.png",
            "K_Eyes == 'surprised'", "images/KittyBJFace/Kitty_BJ_Eyes_Surprised.png",
            "K_Eyes == 'side'", "images/KittyBJFace/Kitty_BJ_Eyes_Side.png",
            "K_Eyes == 'stunned'", "images/KittyBJFace/Kitty_BJ_Eyes_Surprised.png",
            "K_Eyes == 'down'", "images/KittyBJFace/Kitty_BJ_Eyes_Down.png",
            "K_Eyes == 'manic'", "images/KittyBJFace/Kitty_BJ_Eyes_Surprised.png",
            "K_Eyes == 'squint'", "images/KittyBJFace/Kitty_BJ_Eyes_Squint.png",
            "True", "images/KittyBJFace/Kitty_BJ_Eyes_Normal.png",  
            ),
        choice:
            3.5
        choice:
            3.25
        choice:
            3    
        "images/KittyBJFace/Kitty_BJ_Eyes_Closed.png"
        .25
        repeat

image Kitty_BJ_MouthHeading:                                          
    #the mouth used for the heading animations
    contains:
        "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png"        
        zoom 1.4
        anchor (0.50,0.65)  #(0.40,0.65) 
        
image Kitty_BJ_MouthSuckingMask:                                          
    #the mask used for sucking animations
    contains:
        "images/KittyBJFace/Kitty_BJ_Mouth_SuckingMask.png"
        zoom 1.4
    contains: #see if this works, if not remove it
        ConditionSwitch(
            "'mouth' not in K_Spunk", Null(),  
            "Speed != 2 and Speed != 5", Null(),            
            "True", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png",            
            )   
        zoom 1.4
        
image Kitty_BJ_MaskHeading:                                           
    #the mask used for the heading image 
    contains:
        "images/KittyBJFace/Kitty_BJ_Mouth_SuckingMask.png"
        offset (-380,-595)

image Kitty_BJ_MaskHeadingComposite:                                  
    #The composite for the heading mask that goes over the face
    LiveComposite(    
        (858,928),
        (300,462), ConditionSwitch(           
            "Speed == 2", At("Kitty_BJ_MaskHeading", Kitty_BJ_MouthAnim()),   
            "Speed == 5", At("Kitty_BJ_MaskHeading", Kitty_BJ_MouthAnimC()),       
            "True", Null(),
            ),  
        )
    zoom 1.8
    
image Kitty_BJ_MaskHeadingSpunk:                                  
    #The composite for the heading mask that goes over the face
    At("KittySuckingSpunk", Kitty_BJ_MouthAnim())
    zoom 1.8
    
image KittySuckingSpunk:
    contains:
        "images/KittyBJFace/Kitty_BJ_Spunk_SuckingO.png"
        zoom 1.4
        anchor (0.5, 0.5)
    
transform Kitty_BJ_MouthAnim():                                       
        #The animation for the heading mouth
        subpixel True
        zoom 0.7 #0.90      
        block: #total time 1.0 down, 1.5 back up 2.5 total
            pause .40            
            easeout .40 zoom 0.69 #0.87
            linear .10 zoom 0.7 #0.9
            easein .45 zoom 0.65 #0.70 
            pause .15                           
            #1.5s to this point
            easeout .25 zoom 0.7#0.9
            linear .10 zoom 0.69#0.87
            easein .30 zoom 0.7#0.9   
            pause .35                           
            #1.0s to this point
            repeat
transform Kitty_BJ_MouthAnimC():                                       
        #The animation for the heading mouth
        subpixel True
        zoom 0.7 #0.90      
        block: #total time 10 down, 15 back up
            pause .20            
            ease .50 zoom 0.65 #0.87
            pause .60                
            ease .30 zoom 0.7#0.9  
            pause .10                
            ease .30 zoom 0.65#0.9   
            pause .20 
            ease .30 zoom 0.7#0.9  
            repeat
#            pause .50            
#            ease .50 zoom 0.65 #0.87
#            pause .50                
#            ease .50 zoom 0.7#0.9   
#            pause .50
#            repeat
            
image Blanket:    
    contains:
        "images/KittyBJFace/Kitty_BJFace_Blanket.png"
        alpha 0.5
        rotate 90
        block: 
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image Blanket = LiveComposite(
    (858,928),
    (0, 0), "images/KittyBJFace/Kitty_BJFace_Blanket.png"
    )

#Cock Animations for Kitty's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
transform Kitty_BJ_Cock_0():                            
    #The angled static animation for the cock for starting
    anchor (.5,.5)
    rotate -10
transform Kitty_BJ_Cock_1():                            
    #The licking animation for the cock
    subpixel True
    anchor (.5,.5)
    ease 0.5 rotate 0
    block:
        ease 2 rotate -5 #410
        pause .5
        ease 2.5 rotate 0
        repeat        
transform Kitty_BJ_Cock_2():                            
    #The vertical static animation for the cock used in most sucking
    anchor (.5,.5)
    rotate 0
#    alpha 0.9
#End Cock Animations for Kitty's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Head and Body Animations for Kitty's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /               
transform Kitty_BJ_Head_0():                                
    #The starting animation for her face
    subpixel True 
    ease 1.5 offset (0,0)    
transform Kitty_BJ_Body_0():                            
    #The starting animation for her body
    subpixel True 
    ease 1.5 offset (0,0)
    

transform Kitty_BJ_Head_1():                                
    #The licking animation for her face
    subpixel True 
    ease 0.5 offset (0,-35)  #top
    block:
        ease 2.5 offset (25,100) #bottom
        ease 2 offset (0,-35)  #top
        pause .5
        repeat
transform Kitty_BJ_Body_1():                             
    #The licking animation for her body
    subpixel True 
    ease 0.5 offset (0,-35)  #top
    block:
        ease 2.5 offset (30,90) #bottom 25,50
        ease 2 offset (0,-35)  #top
        pause .5
        repeat
        
transform Kitty_BJ_Head_2():                                 
    #The heading animation for her face
    subpixel True 
    offset (0,-40)     #top 
    block:
        ease 1 yoffset 35           #bottom         
        ease 1.5 offset (0,-40)     #top  
        repeat
transform Kitty_BJ_Body_2():                            
    #The heading animation for her body
    subpixel True 
    offset (0,-40)     #top 
    block:
        ease 1 yoffset 15           #bottom         
        ease 1.5 offset (0,-40)     #top  
        repeat
        
transform Kitty_BJ_Head_3():                                
    #The sucking animation for her face
    subpixel True
    ease 0.5 offset (0,50) 
    block:
        ease 1 yoffset 120 #100
        ease 1.5 offset (0,50) 
        repeat    
transform Kitty_BJ_Body_3():                            
    #The sucking animation for her body
    subpixel True 
    ease 0.5 offset (0,50)  
    block:
        ease 1 yoffset 100 #80      #bottom
        ease 1.5 offset (0,50) #top
        repeat
    
transform Kitty_BJ_Head_4():                                   
    #The deep animation for her face
    ease .5 offset (0,100) 
    block:
        subpixel True
        ease 1 yoffset 300
        pause .5
        ease 2 yoffset 100  
        repeat        
transform Kitty_BJ_Body_4():                               
    #The deep animation for her body
    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1.2 yoffset 250
        pause .5
        ease 1.8 yoffset 100   
        repeat    

transform Kitty_BJ_Head_5():                                 
    #The heading cumming animation for her face
    subpixel True 
    offset (0,-30)     #top 
    block:
        ease 1 yoffset -20           #bottom         
        ease 1.5 offset (0,-30)     #top  
        repeat
transform Kitty_BJ_Body_5():                            
    #The heading cumming animation for her body
    subpixel True 
    offset (0,-30)     #top 
    block:
        ease 1 yoffset -20           #bottom         
        ease 1.5 offset (0,-30)     #top  
        repeat        
        
transform Kitty_BJ_Head_6():                                   
    #The deep cumming animation for her face
    ease .5 offset (0,230) 
    block:
        subpixel True
        ease 1 yoffset 250
        pause .5
        ease 2 yoffset 230  
        repeat        
transform Kitty_BJ_Body_6():                               
    #The deep cumming animation for her body
    ease .5 offset (0,190)
    block:
        subpixel True
        ease 1.2 yoffset 200
        pause .5
        ease 1.8 yoffset 190   
        repeat    
        

#transform Kitty_BJ_Static():                                 
#    #The static animation for her face
#    subpixel True 
#    ease 1.5 offset (0,0)
#    repeat

#transform Kitty_BJ_StaticBody():                              
#    #The static animation for her face
#    subpixel True 
#    ease 1.5 offset (0,0)
                          
    
#Head and Body Animations for Kitty's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
                                                               #BJ Launchers  
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Kitty_BJ_Launch(Line = 0):    # The sequence to launch the Kitty BJ animations  
    if renpy.showing("Kitty_BJ_Animation"):
        return
    
    call Kitty_Hide
    if Line == "L" or Line == "cum":
        show Kitty_Sprite at SpriteLoc(StageCenter) zorder KittyLayer:
            alpha 1
            ease 1 zoom 2.5 offset (150,80) 
        with dissolve
    else:
        show Kitty_Sprite at SpriteLoc(StageCenter) zorder KittyLayer:
            alpha 1
            zoom 2.5 offset (150,80) 
        with dissolve
        
    if Taboo and Line == "L": # Kitty gets started. . .
        if not K_Blow:
            if R_Loc == bg_current:
                "Kitty looks back at Rogue to see if she's watching."
            elif E_Loc == bg_current:
                "Kitty looks back at Emma to see if she's watching."
            else:
                "Kitty looks around to see if anyone can see her."
            "Kitty hesitantly pulls down your pants and touches her mouth to your cock."
        else:
            if R_Loc == bg_current:
                "Kitty looks back at Rogue to see if she's watching."
            elif E_Loc == bg_current:
                "Kitty looks back at Emma to see if she's watching."
            else:
                "Kitty hesitantly looks around to see if anyone notices what she's doing."
            "She then bends down and puts her lips around you."
    elif Line == "L":    
        if not K_Blow:
            "Kitty hesitantly pulls down your pants and touches her mouth to your cock."
        else:
            "Kitty bends down and begins to suck on your cock."    
            
    $ Speed = 0
    
    if Line != "cum":
        $ Trigger = "blow"
    
    show Kitty_Sprite zorder KittyLayer:
        alpha 0
    show Kitty_BJ_Animation zorder 150: 
        pos (645,510) 
    return
    
label Kitty_BJ_Reset: # The sequence to the Kitty animations from BJ to default
    if not renpy.showing("Kitty_BJ_Animation"):
        return
#    hide Kitty_BJ_Animation
    call Kitty_Hide 
    $ Speed = 0
    
    show Kitty_Sprite at SpriteLoc(StageCenter) zorder KittyLayer:
        alpha 1
        zoom 2.5 offset (150,80) 
    with dissolve
    
    show Kitty_Sprite zorder KittyLayer:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)    
    show Kitty_Sprite at SpriteLoc(K_SpriteLoc) zorder KittyLayer:
        alpha 1
        zoom 1 offset (0,0)           
        
    return  

# End Kitty Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Start Kitty TJ Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Kitty TJ annimation element ///////////////////////////////////////////////////////////////////////////                                     Core Kitty BJ element

image Kitty_TJ_Animation:
    #core titjob animation   
    contains:
        ConditionSwitch(                                                              
            # Kitty's upper body
            "P_Sprite", ConditionSwitch(                                                               
                    # If during sex
                    "Speed == 1", "Kitty_TJ_Body_1",#slow
                    "Speed == 2", "Kitty_TJ_Body_2",#fast
                    "Speed == 3", "Kitty_TJ_Body_3",#licking
                    "Speed >= 5", "Kitty_TJ_Body_5",#cumming
                    "True",       "Kitty_TJ_Body_0",#Static
                    ),
            "True","Kitty_TJ_Body_0",#Static
            )    
    zoom 1.35 #0.8
    anchor (.5,.5)
    pos (600,605) #(600,705)#height for bj
    

image Kitty_TJ_Torso:                                                                        
    # Her torso for the sex, BJ, and TJ poses
    contains:
            #body
            "images/KittyBJFace/Kitty_TJ_Body.png"  
#    contains:
#            #chest clothing under layer for TJs
#            ConditionSwitch(    
#                "not renpy.showing('Kitty_TJ_Animation')", Null(),   # K_TitsUp = 0
#                "K_Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Bra_Sports_TJU.png",
#                "True", Null(),
#                ) 
#    contains:
#            # Chest clothing layer
#        ConditionSwitch(    
#            "not K_Chest or renpy.showing('Kitty_TJ_Animation')", Null(),   # K_TitsUp = 0
#            "K_Chest == 'corset'", "images/KittySex/Kitty_Sex_Bra_Corset_Up.png",   # K_TitsUp = 1
#            "K_Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Bra_Sports_Up.png",   # K_TitsUp = 1
#            "K_Chest == 'lace bra'", "images/KittySex/Kitty_Sex_Bra_Lace_Up.png",   # K_TitsUp = 1
#            "True", Null(),   # K_TitsUp = 0
#            )
#    contains:
#            # Over clothing layer
#        ConditionSwitch(   
#            "K_Over == 'jacket'", ConditionSwitch(   
#                    #if it's the ring pericings                       
#                    "renpy.showing('Kitty_TJ_Animation')", Null(),
##                    "renpy.showing('Kitty_TJ_Animation')", "images/KittySex/Kitty_Sex_Jacket_Down.png",
#                    "K_Chest == 'corset'", "images/KittySex/Kitty_Sex_Jacket_Up.png",   # K_TitsUp = 1
#                    "K_Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Jacket_Up.png",   # K_TitsUp = 1
#                    "K_Chest == 'lace bra'", "images/KittySex/Kitty_Sex_Jacket_Up.png",   # K_TitsUp = 1
#                    "True", "images/KittySex/Kitty_Sex_Jacket_Down.png",   # K_TitsUp = 0
#                    ),                
#            "K_Over == 'nighty'", ConditionSwitch(
#                    #if she has the nighty on     
#                    "renpy.showing('Kitty_TJ_Animation')", Null(),
#                    "K_Chest in ('corset', 'lace bra', 'sports bra')", "images/KittySex/Kitty_Sex_Nighty_Up.png",  
#                    "True", "images/KittySex/Kitty_Sex_Nighty_Down.png", 
#                    ),    
#            "True", Null(), 
#            )
#    contains:
#            # spunk on tits
#            ConditionSwitch(    
#                "'tits' not in K_Spunk", Null(),
#                "renpy.showing('Kitty_TJ_Animation')", "images/KittySex/Kitty_Spunk_Titjob_Under.png",
#                "True", "images/KittySex/Kitty_Spunk_Tits.png",
#                ) 

image Kitty_TJ_Arms:                                                                        
    # Her arms for the TJ poses
    contains:
            #body
            "images/KittyBJFace/Kitty_TJ_Arms.png"  
              
image Kitty_TJ_Tits:
    #core titjob breasts   
    contains:
            #base layer     
#            "images/KittyBJFace/Kitty_TJ_Tits.png"
        ConditionSwitch(    
            "P_Sprite and Speed", "images/KittyBJFace/Kitty_TJ_Tits_Smooshed.png", 
            "True", "images/KittyBJFace/Kitty_TJ_Tits.png",
            )
#    contains:
#            # piercings
#        ConditionSwitch(   
#            "not K_Pierce", Null(),
#            "K_Pierce == 'barbell'", ConditionSwitch(   
#                    #if it's the ring pericings   
##                    "K_Chest in ('corset', 'lace bra', 'sports bra')", Null(),  
#                    "True", "images/KittySex/Kitty_Pierce_Barbell_Tits_T.png", 
#                    ),    
#            "K_Pierce == 'ring'", ConditionSwitch(   
#                    #if it's the ring pericings   
##                    "K_Chest in ('corset', 'lace bra', 'sports bra')", Null(),  
#                    "True", "images/KittySex/Kitty_Pierce_Ring_Tits_T.png", 
#                    ),                    
#            "True", Null(), 
#            )
#    contains:
#            #chest clothing layer
#        ConditionSwitch(    
#            "not K_Chest", Null(),   # K_TitsUp = 0
#            "K_Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Bra_Sports_TJ.png",   # K_TitsUp = 1
#            "K_Chest == 'lace bra'", "images/KittySex/Kitty_Sex_Bra_Lace_TJ.png",   # K_TitsUp = 1
#            "True", Null(),   # K_TitsUp = 0
#            )
#    contains:
#            # piercings over clothes
#        ConditionSwitch(   
#            "not K_Pierce or not K_Chest", Null(),
#            "K_Pierce == 'barbell'", ConditionSwitch(   
#                    #if it's the ring pericings   
#                    "K_Chest in ('corset', 'lace bra', 'sports bra')", "images/KittySex/Kitty_Pierce_Barbell_Tits_TC.png", 
#                    "True", Null(),
#                    ),    
#            "K_Pierce == 'ring'", ConditionSwitch(   
#                    #if it's the ring pericings   
#                    "K_Chest in ('corset', 'lace bra', 'sports bra')", "images/KittySex/Kitty_Pierce_Ring_Tits_TC.png", 
#                    "True", Null(),
#                    ),                    
#            "True", Null(), 
#            )
#    contains:
#            # spunk on tits
#        ConditionSwitch(    
#                "'tits' in K_Spunk", "images/KittySex/Kitty_Spunk_Titjob_Over.png",
#                "True", Null(),
#                ) 


#image Kitty_TJ_MaskA:
#    #Test mask for showing her moving chest
#    contains:
##        Solid("#159457", xysize=(750,750))
#        "images/KittyBJFace/Kitty_TJ_Mask.png"

image Kitty_Mega_Mask:
    # giant green brick for use in finding where a mask is
    contains:
        Solid("#159457", xysize=(1750,1750))
        alpha .5


#  TJ animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Kitty_TJ_Body_0:                                                                        
        #Her Body in the TJ pose, idle
        contains:
                #Hair underlay
                "Kitty_BJ_HairBack"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (505,260) #bottom  #505
                subpixel True
                block:
                    ease 2.4 ypos 250 #top
                    ease 1.6 ypos 260 #bottom
                    repeat 
        contains:       
                #base body
                "Kitty_TJ_Torso"#"images/KittyBJFace/Kitty_TJ_Body.png"           
                pos (545,330)#(500,360)#pos (0,0) #bottom            
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.4 ypos 325 #top
                    ease 1.6 ypos 330 #bottom
                    repeat   
        contains:       
                #arms
                "Kitty_TJ_Arms"#"images/KittyBJFace/Kitty_TJ_Arms.png"                
                pos (545,330)#pos (0,0) #bottom            
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.4 ypos 325 #top
                    ease 1.6 ypos 330 #bottom
                    repeat   
        contains:
                #head
                "Kitty_BJ_Head"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (505,260) #bottom  #280
                subpixel True
                block:
                    ease 2.4 ypos 250 #top
                    ease 1.6 ypos 260 #bottom
                    repeat 
        contains:
                #tits underlayer
                "Kitty_TJ_Tits"             
                pos (545,330)#pos (0,0) #bottom            
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.4 ypos 325 #top
                    ease 1.6 ypos 330 #bottom
                    repeat   
        contains:
                #zero's cock
                ConditionSwitch(    
                    "P_Sprite", "Blowcock",
                    "True", Null(),
                    )      
                subpixel True
                pos (640,150) #bottom #150
                anchor (0.5,0.5)
                zoom 0.4   
#End TJ animation Speed 0
    
    
image Kitty_TJ_Mask_1:
        contains:
            "images/KittyBJFace/Kitty_TJ_Mask.png"
            pos (100,60) #bottom #pos (545,330)          
            anchor (0.5, 0.5)
            zoom 1.4           #temp
            subpixel True
            block:
                ease 2.9 ypos -40 #top 280
                ease 1 ypos 60 #bottom 330
                pause .1
                repeat  

image Kitty_TJ_Body_1:                                                                        
        #Her Body in the TJ pose, slow 1
        contains:
                #Hair underlay
                "Kitty_BJ_HairBack"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (505,260) #bottom  #505
                subpixel True
                block:
                    ease 3 ypos 210 #top
                    ease 1 ypos 260 #bottom
                    repeat 
        contains:       
                #base body
                "Kitty_TJ_Torso"#"images/KittyBJFace/Kitty_TJ_Body.png"           
                pos (545,330)#(500,360)#pos (0,0) #bottom            
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.8 ypos 280 #top
                    ease 1 ypos 330 #bottom
                    pause .2
                    repeat   
        contains:       
                #arms
                "Kitty_TJ_Arms"#"images/KittyBJFace/Kitty_TJ_Arms.png"                
                pos (545,330)#pos (0,0) #bottom            
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.85 ypos 280 #top
                    ease 1 ypos 330 #bottom
                    pause .15
                    repeat    
        contains:
                #head
                "Kitty_BJ_Head"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (505,260) #bottom  #280
                subpixel True
                block:
                    ease 2.9 ypos 210 #top
                    ease 1 ypos 260 #bottom
                    pause .1
                    repeat 
        contains:
                #tits underlayer
                "Kitty_TJ_Tits"             
                pos (545,330)#pos (0,0) #bottom            
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.9 ypos 280 #top
                    ease 1 ypos 330 #bottom
                    pause .1
                    repeat   
        contains:
                #zero's cock
                ConditionSwitch(    
                    "P_Sprite", AlphaMask("Blowcock", "Kitty_TJ_Mask_1"), 
                    "True", Null(),
                    )      
                subpixel True
                pos (665,500) #bottom #150
                anchor (0.5,0.5)
                zoom 0.4   
                block:
                    ease 2.8 ypos 490 #top
                    ease .8 ypos 500 #bottom
                    pause .4
                    repeat 
#End TJ animation Speed 1
    
    
image Kitty_TJ_Mask_2:
        contains:
            "images/KittyBJFace/Kitty_TJ_Mask.png"
            pos (100,60) #bottom #pos (545,330)            
            anchor (0.5, 0.5)
            zoom 1.4           #temp
            subpixel True
            block:
                ease .71 ypos -15 #top 280
                ease .27 ypos 60 #bottom 330
                pause .02
                repeat  

image Kitty_TJ_Body_2:                                                                        
        #Her Body in the TJ pose, fast 2
        contains:
                #Hair underlay
                "Kitty_BJ_HairBack"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (505,260) #bottom  #505
                subpixel True
                block:
                    ease .7 ypos 215 #top
                    ease .25 ypos 260 #bottom
                    pause .05
                    repeat 
        contains:       
                #base body
                "Kitty_TJ_Torso"#"images/KittyBJFace/Kitty_TJ_Body.png"           
                pos (545,330)#(500,360)#pos (0,0) #bottom            
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease .65 ypos 285 #top
                    ease .25 ypos 330 #bottom
                    pause .1
                    repeat   
        contains:       
                #arms
                "Kitty_TJ_Arms"#"images/KittyBJFace/Kitty_TJ_Arms.png"                
                pos (545,330)#pos (0,0) #bottom            
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease .68 ypos 285 #top
                    ease .25 ypos 330 #bottom
                    pause .07
                    repeat  
        contains:
                #tits underlayer
                "Kitty_TJ_Tits"             
                pos (545,330)#pos (0,0) #bottom            
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease .71 ypos 290 #top
                    ease .27 ypos 330 #bottom
                    pause .02
                    repeat    
        contains:
                #head
                "Kitty_BJ_Head"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (505,260) #bottom  #280
                subpixel True
                block:
                    ease .68 ypos 215 #top
                    ease .25 ypos 260 #bottom
                    pause .07
                    repeat  
        contains:
                #zero's cock
                ConditionSwitch(    
                    "P_Sprite", AlphaMask("Blowcock", "Kitty_TJ_Mask_2"), 
                    "True", Null(),
                    )      
                subpixel True
                pos (665,500) #bottom #150
                anchor (0.5,0.5)
                zoom 0.4   
                block:
                    ease .72 ypos 490 #top
                    ease .27 ypos 500 #bottom
                    pause .01
                    repeat 
#End TJ animation Speed 2
    
    
image Kitty_TJ_Mask_3:
        contains:
            "images/KittyBJFace/Kitty_TJ_Mask.png"
            pos (100,140) #bottom #pos (545,330)            
            anchor (0.5, 0.5)
            zoom 1.4           #temp
            subpixel True
            block:
                ease 2.2 ypos 90 #top 280
                ease .6 ypos 140 #bottom 330
                pause .2
                repeat  
                
image Kitty_TJ_Body_3:                                                                        
        #Her Body in the TJ pose, licking 3
        contains:
                #Hair underlay
                "Kitty_BJ_HairBack"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (500,260) #bottom  #505
                rotate 0
                subpixel True
                parallel:
                    block: 
                        #un tilted loop
                        ease 2 pos (500,290) #top
                        ease .6 pos (500,315) #bottom 
                        pause .4
                        repeat 2
                    block:
                        #left tilted loop
                        ease 2.2 pos (500,290) #top
                        ease .8 pos (520,320) #bottom 
                        ease 2.2 pos (510,290) #top
                        ease .8 pos (520,320) #bottom 
                    block: 
                        #un tilted loop
                        ease 2 pos (500,290) #top
                        ease .6 pos (500,315) #bottom  
                        pause .4
                        repeat 2
                    block:
                        #right tilted loop
                        ease 2.2 pos (500,290) #top
                        ease .8 pos (475,320) #bottom 
                        ease 2.2 pos (490,290) #top
                        ease .8 pos (475,320) #bottom 
                    repeat 
        contains:       
                #base body
                "Kitty_TJ_Torso"#"images/KittyBJFace/Kitty_TJ_Body.png"           
                pos (545,360)#(500,360)#pos (0,0) #bottom            
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.2 ypos 340 #top
                    ease .6 ypos 360 #bottom
                    pause .2
                    repeat   
        contains:       
                #arms
                "Kitty_TJ_Arms"#"images/KittyBJFace/Kitty_TJ_Arms.png"                
                pos (545,360)#pos (0,0) #bottom            
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.2 ypos 340 #top
                    ease .6 ypos 360 #bottom
                    pause .2
                    repeat   
        contains:
                #tits underlayer
                "Kitty_TJ_Tits"             
                pos (545,360)#pos (0,0) #bottom            
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.2 ypos 340 #top
                    ease .6 ypos 360 #bottom
                    pause .2
                    repeat  
        contains:
                #head
                "Kitty_BJ_Head"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (500,310) #bottom  #505
                subpixel True
                rotate 0
                parallel:
                    block: 
                        #un tilted loop
                        ease 2 pos (500,290) #top
                        ease .6 pos (500,315) #bottom 
                        pause .4
                        repeat 2
                    block:
                        #left tilted loop
                        ease 2.2 pos (500,290) #top
                        ease .8 pos (520,320) #bottom 
                        ease 2.2 pos (510,290) #top
                        ease .8 pos (520,320) #bottom 
                    block: 
                        #un tilted loop
                        ease 2 pos (500,290) #top
                        ease .6 pos (500,315) #bottom  
                        pause .4
                        repeat 2
                    block:
                        #right tilted loop
                        ease 2.2 pos (500,290) #top
                        ease .8 pos (475,320) #bottom 
                        ease 2.2 pos (490,290) #top
                        ease .8 pos (475,320) #bottom 
                    repeat 
                parallel:  
                    block:
                        #un tilted loop
                        ease 2.2 rotate 0  #top
                        pause 3.8 #bottom  
                    block:
                        #left tilted loop  
                        ease 2.2 rotate 0   #top
                        ease .8 rotate 10   #bottom
                        ease 2.2 rotate 0   #top
                        ease .8 rotate 5   #bottom
                    block:
                        #un tilted loop
                        ease 2.2 rotate 0  #top
                        pause 3.8 #bottom  
                    block:
                        #right tilted loop
                        ease 2.2 rotate 0   #top
                        ease .8 rotate -10   #bottom 
                        ease 2.2 rotate 0   #top
                        ease .8 rotate -5   #bottom  
                    repeat                  
        contains:
                #zero's cock
                ConditionSwitch(    
                    "P_Sprite", AlphaMask("Blowcock", "Kitty_TJ_Mask_3"), 
                    "True", Null(),
                    )      
                subpixel True
                pos (665,500) #bottom #150
                anchor (0.5,0.5)
                zoom 0.4   
#End TJ animation Speed 3
  
  
image Kitty_TJ_Mask_5:
        contains:
            "images/KittyBJFace/Kitty_TJ_Mask.png"
            pos (100,140) #bottom #pos (545,330)            
            anchor (0.5, 0.5)
            zoom 1.4           #temp
            subpixel True
            block:
                ease 2.2 ypos 120 #top 280 #90
                ease 1.6 ypos 140 #bottom 330
                pause .2
                repeat  

image Kitty_TJ_Body_5:                                                                        
        #Her Body in the TJ pose, cumming 5
        contains:
                #Hair underlay
                "Kitty_BJ_HairBack"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (500,260) #bottom  #505
                rotate 0
                subpixel True
                block: 
                    #un tilted loop
                    ease 2 pos (500,304) #top 280
                    ease 1.6 pos (500,307) #bottom 315
                    pause .4               
                    repeat 
        contains:       
                #base body
                "Kitty_TJ_Torso"#"images/KittyBJFace/Kitty_TJ_Body.png"           
                pos (545,360)#(500,360)#pos (0,0) #bottom            
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.2 ypos 350 #top
                    ease 1.6 ypos 360 #bottom
                    pause .2
                    repeat   
        contains:       
                #arms
                "Kitty_TJ_Arms"#"images/KittyBJFace/Kitty_TJ_Arms.png"                
                pos (545,360)#pos (0,0) #bottom            
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.2 ypos 350 #top
                    ease 1.6 ypos 360 #bottom
                    pause .2
                    repeat    
        contains:
                #head
                "Kitty_BJ_Head"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (500,307) #bottom  #505
                subpixel True
                rotate 0
                block: 
                    #un tilted loop
                    ease 2 pos (500,304) #top 280
                    ease 1.6 pos (500,307) #bottom 315
                    pause .4               
                    repeat             
        contains:
                #tits underlayer
                "Kitty_TJ_Tits"             
                pos (545,360)#pos (0,0) #bottom            
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.2 ypos 350 #top
                    ease 1.6 ypos 360 #bottom
                    pause .2
                    repeat   
    #    contains:
    #            #tits underlayer
    #            "Kitty_TJ_MaskA"             
    #            pos (545,360)#pos (0,0) #bottom            
    #            anchor (0.5, 0.5)
    #            zoom 0.55           #temp
    #            subpixel True
    #            block:
    #                ease 2.2 ypos 350 #top
    #                ease 1.6 ypos 360 #bottom
    #                pause .2
    #                repeat                  
        contains:
                #zero's cock
                ConditionSwitch(    
    #                "P_Sprite", AlphaMask("Kitty_Mega_Mask", "Kitty_TJ_Mask_5"), 
                    "P_Sprite", AlphaMask("Blowcock", "Kitty_TJ_Mask_5"), 
    #                "P_Sprite", AlphaMask("Blowcock", "Kitty_Mega_Mask"), 
                    "True", Null(),
                    )      
                subpixel True
                pos (665,500) #bottom #150
                anchor (0.5,0.5)
                zoom 0.4   
                    
    #    contains:
    #            #zero's cock
    #            ConditionSwitch(    
    #                "P_Sprite", "Blowcock",
    #                "True", Null(),
    #                )      
    #            subpixel True
    #            alpha 0.2
    #            pos (640,150) #bottom #150
    #            anchor (0.5,0.5)
    #            zoom 0.4     
    #    contains:
    #            #tits
    #            "Kitty_Tits_Mask"            
    #            pos (545,360)#pos (0,0) #bottom            
    #            anchor (0.5, 0.5)
    #            zoom 0.55           #temp
    #            subpixel True
    #            block:
    #                ease 2.2 ypos 340 #top
    #                ease .6 ypos 360 #bottom
    #                pause .2
    #                repeat   
#End TJ animation Speed 5 (cumming)
       
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


label Kitty_TJ_Launch(Line = 0):    # The sequence to launch the Kitty Titfuck animations   
    if renpy.showing("Kitty_TJ_Animation"):
        return
    call Kitty_Hide
    show Kitty_Sprite at SpriteLoc(K_SpriteLoc) zorder KittyLayer:
        alpha 1
        ease 1 zoom 2 xpos 700 yoffset 50 #offset (-100,50) 
    if Taboo: # Kitty gets started. . .
        if R_Loc == bg_current:
            "Kitty looks back at Rogue to see if she's watching."
        elif K_Loc == bg_current:
            "Kitty looks back at Kitty to see if she's watching."
        else:
            "Kitty looks around to see if anyone can see her."
    
    if K_Chest and K_Over:
        "She throws off her [K_Over] and her [K_Chest]."                
    elif K_Over:
        "She throws off her [K_Over], baring her breasts underneath."
    elif K_Chest:
        "She tugs off her [K_Chest] and throws it aside."
    $ K_Over = 0
    $ K_Chest = 0
    $ Kitty_Arms = 0
    
    call Kitty_First_Topless      #restore if topless          
     
    show blackscreen onlayer black with dissolve   
    show Kitty_Sprite zorder KittyLayer:
        alpha 0
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "titjob"
    show Kitty_TJ_Animation zorder 150 
    $ P_Sprite = 1
    hide blackscreen onlayer black with dissolve
    return
    
label Kitty_TJ_Reset: # The sequence to the Kitty animations from Titfuck to default
    if not renpy.showing("Kitty_TJ_Animation"):
        return
#    hide Kitty_TJ_Animation
    call Kitty_Hide 
    $ P_Sprite = 0
    
    show Kitty_Sprite at SpriteLoc(K_SpriteLoc) zorder KittyLayer:
        zoom 2 xpos 550 yoffset 50 #offset (-100,50)  #zoom 2 offset (-100,50)
    show Kitty_Sprite zorder KittyLayer:
        alpha 1
        ease 1 zoom 1.5 xpos 700 yoffset 50
        pause .5
        ease .5 zoom 1 xpos K_SpriteLoc yoffset 0   
    show Kitty_Sprite at SpriteLoc(K_SpriteLoc) zorder KittyLayer:
        alpha 1
        zoom 1 offset (0,0) xpos K_SpriteLoc        
#    "Kitty pulls back"
    return
            
# End Kitty TJ Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /






# Start Kitty Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Kitty Handjob element //////////////////////////////////////////////////////////////////////                                         Core Kitty HJ element

#image Zero_Handcock:
#    contains:
#        ConditionSwitch(    # Zero cock sucking
#            "P_Color == 'pink'", "images/RogueBJFace/handcock_P.png",
#            "P_Color == 'brown'", "images/RogueBJFace/handcock_B.png",             
#            "P_Color == 'green'", "images/RogueBJFace/handcock_G.png", 
#            "P_Color != 'pink'", Null(),
#            ),  
#    anchor (0.5,1.0)  #1.0
#    pos (200,400)#(200,400)
        
image Kitty_Hand_Under:
    ConditionSwitch(
        "K_Tan", "images/KittySprite/Thandkitty2.png",
        "True", "images/KittySprite/handkitty2.png",
        ),
    anchor (0.5,0.5)
    pos (0,0)
    
    
image Kitty_Hand_Over:
    ConditionSwitch(
        "K_Tan", "images/KittySprite/Thandkitty1.png",
        "True", "images/KittySprite/handkitty1.png",
        ), 
    anchor (0.5,0.5)
    pos (0,0)

#transform Handcock_1():
#    subpixel True
#    rotate_pad False
#    ease .5 ypos 450 rotate -2 #450
#    pause 0.25
#    ease 1.0 ypos 400 rotate 0 #400
#    pause 0.1
#    repeat

#transform Handcock_2():
#    subpixel True
#    rotate_pad False
#    ease .2 ypos 430 rotate -3 #410
#    ease .5 ypos 400 rotate 0
#    pause 0.1
#    repeat
    
transform Kitty_Hand_1():
    subpixel True
    ease .5 ypos 150 rotate 5 #500 #100 #rotate 10#   Bottom
    pause 0.25
    ease 1.0 ypos -100 rotate -5 #250#-150 #rotate -10#  Top
    pause 0.1
    repeat

transform Kitty_Hand_2():
    subpixel True
    ease 0.2 ypos 0 rotate 3   
    pause 0.1
    ease 0.4 ypos -100 rotate -3 
    pause 0.1
    repeat

image Kitty_HJ_Animation:  
    contains:
        ConditionSwitch(                                                # backside of the hand
            "not Speed", Transform("Kitty_Hand_Under"), 
            "Speed == 1", At("Kitty_Hand_Under", Kitty_Hand_1()),
            "Speed >= 2", At("Kitty_Hand_Under", Kitty_Hand_2()),
            "Speed", Null(),
            ),  
    contains:
        ConditionSwitch(                                                # cock
            "not Speed", Transform("Zero_Handcock"), 
            "Speed == 1", At("Zero_Handcock", Handcock_1()),
            "Speed >= 2", At("Zero_Handcock", Handcock_2()), 
            "Speed", Null(),
            ),  
        offset (0,0)
    contains:
        ConditionSwitch(                                                # fingers of the hand
            "not Speed", Transform("Kitty_Hand_Over"), 
            "Speed == 1", At("Kitty_Hand_Over", Kitty_Hand_1()),
            "Speed >= 2", At("Kitty_Hand_Over", Kitty_Hand_2()), 
            "Speed", Null(),
            ),   
    anchor (0.51, -1.3)
    zoom 0.4#0.6
        
        
label Kitty_HJ_Launch(Line = 0): 
    if renpy.showing("Kitty_HJ_Animation"):        
        $ Trigger = "hand"
        return
    call Kitty_Hide
    if Line == "L":      
        show Kitty_Sprite at SpriteLoc(StageRight) zorder KittyLayer:
            alpha 1
            ease 1 zoom 1.7 offset (-50,200)
    else:     
        show Kitty_Sprite at SpriteLoc(StageRight) zorder KittyLayer:
            alpha 1
            ease 1 zoom 1.7 offset (-50,200)
        with dissolve
   
#    if Taboo and Line == "L": # Rogue gets started. . .
#        if not R_Hand:
#            "Rogue looks around to see if anyone can see her."
#            "As you pull out your cock, Rogue pulls off her gloves, and hesitantly reaches for it. She starts to roughly stroke on it."
#        else:
#            "Rogue hesitantly looks around to see if anyone notices what she's doing, but then leans over and grabs your cock,"
#    elif Line == "L":    
#        if not R_Hand:
#            "As you pull out your cock, Rogue pulls off her gloves, and hesitantly reaches for it. She starts to roughly stroke on it."
#        else:
#            "Rogue bends down and grabs your cock."
#    else:
#        "Rogue bends down and grabs your cock."
            
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    else:
        $ Speed = 1
    pause .5
    show Kitty_HJ_Animation at SpriteLoc(StageCenter) zorder 150 with easeinbottom:
        #xoffset 150
        offset (100,250)#(75,250)
    return
    
label Kitty_HJ_Reset: # The sequence to the Rogue animations from handjob to default
    if not renpy.showing("Kitty_HJ_Animation"):
        return    
    $ Speed = 0
    hide Kitty_HJ_Animation with easeoutbottom
    call Kitty_Hide 
    show Kitty_Sprite at SpriteLoc(K_SpriteLoc) zorder KittyLayer:
        alpha 1
        zoom 1.7 offset (-50,200)
    show Kitty_Sprite at SpriteLoc(K_SpriteLoc) zorder KittyLayer:
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause .5
        ease .5 zoom 1 offset (0,0)    
    show Kitty_Sprite at SpriteLoc(K_SpriteLoc) zorder KittyLayer:
        alpha 1
        zoom 1 offset (0,0)  
    return
    

label K_Kissing_Launch(T = Trigger):    
    call Kitty_Hide
    $ Trigger = T
    show Kitty_Sprite at SpriteLoc(K_SpriteLoc) zorder KittyLayer
    show Kitty_Sprite at SpriteLoc(StageCenter):
            ease 0.5 offset (0,0) zoom 2 alpha 1
    return
    
label K_Kissing_Smooch:   
    call KittyFace("kiss")  
    show Kitty_Sprite at SpriteLoc(StageCenter) zorder KittyLayer:
        ease 0.5 xpos StageCenter offset (0,0) zoom 2 alpha 1
        pause 1
        ease 0.5 xpos K_SpriteLoc zoom 1        
    call KittyFace("sexy")  
    return
                
label K_Breasts_Launch(T = Trigger):    
    call Kitty_Hide
    $ Trigger = T
    show Kitty_Sprite at SpriteLoc(K_SpriteLoc) zorder KittyLayer:
        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1 # pos (900,-50)
    return
        
label K_Pussy_Launch(T = Trigger):
    call Kitty_Hide    
    $ Trigger = T
    show Kitty_Sprite at SpriteLoc(K_SpriteLoc) zorder KittyLayer:
        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
    return
        
label K_Pos_Reset(Pose = 0):
    call Kitty_Hide 
    show Kitty_Sprite at SpriteLoc(K_SpriteLoc) zorder KittyLayer:
        ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1 
    show Kitty_Sprite zorder KittyLayer:
        offset (0,0) 
        anchor (0.5, 0.0)
        zoom 1   
        xzoom 1 
        yzoom 1
        alpha 1
        pos (K_SpriteLoc,50)
    $ Trigger = Pose
    return
    
#MOD MARKER HIDE
label Kitty_Hide:
        if renpy.showing("Kitty_SexSprite") or renpy.showing("Kitty_Doggy"):
            call Kitty_Sex_Reset
        call mod_hide_Kitty_SexSprite
        hide Kitty_HJ_Animation
        hide Kitty_BJ_Animation
        hide Kitty_TJ_Animation 
        return

label KThreewayBreasts_Launch:    
        show Kitty_Sprite at SpriteLoc(K_SpriteLoc) zorder KittyLayer:
    #      ease 0.5 pos (800,200) zoom 1.3
            ease 0.5 pos (700,200) xzoom -1.5 yzoom 1.5
        $ Kitty_Arms = 1
        return


# End Kitty Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    
    
    
    
    
    
# Start Kitty Fondling Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    
    
# Interface items //////////////////////////////////////////////////////////////////////////////

image GropeLeftBreast_K:    
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65#.7
        pos (215,420)#(300,420)230
        anchor (0.5,0.5)
        alpha 0.5
        rotate 90
        block: 
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image GropeRightBreast_K:    
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (120,410)#(180,410) 150
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block: 
            ease 1 rotate -30
            ease 1 rotate -60 
            repeat

#image GropeBreast:
image LickRightBreast_K:   
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5 
        xzoom -0.45
        pos (115,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block: 
            ease .5 rotate -40 pos (95,370)            
            pause .5
            ease 1.5 rotate 30 pos (115,400)
            repeat
            
image LickLeftBreast_K:   
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5 
        xzoom -0.45
        pos (200,410) #(115,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block: 
            ease .5 rotate -40 pos (190,380)#(95,370)            
            pause .5
            ease 1.5 rotate 30 pos (200,410)#(115,400)
            repeat

image GropeThigh_K: 
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (200,720)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        parallel: 
            pause .5
            ease 1 ypos 780
            ease 1 ypos 720           
            repeat
        parallel:            
            pause .5
            ease 1 rotate 110 xpos 180 
            ease 1 rotate 100 xpos 200   
            repeat

image GropePussy_K: 
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (210,640)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice: 
                ease .5 rotate 190 pos (210,625)
                ease .75 rotate 170 pos (210,640)   
            choice: 
                ease .5 rotate 190 pos (210,625)
                pause .25
                ease 1 rotate 170 pos (210,640)             
            repeat

image FingerPussy_K: 
    contains:
        subpixel True
        "UI_Finger"       
        zoom 0.65
        pos (220,730)#(230,720)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice: 
                ease 1 rotate 40 pos (230,695)#(240,685)
                pause .5
                ease 1 rotate 50 pos (220,730)  #(230,720)   
            choice:                          
                ease .5 rotate 40 pos (230,695)
                pause .5
                ease 1.75 rotate 50 pos (220,730)  
            choice:                          
                ease 2 rotate 40 pos (230,695)
                pause .5
                ease 1 rotate 50 pos (220,730)  
            choice:                          
                ease .25 rotate 40 pos (230,695)
                ease .25 rotate 50 pos (220,730) 
                ease .25 rotate 40 pos (230,695)
                ease .25 rotate 50 pos (220,730)
            repeat
            
image Lickpussy_K:   
    contains:
        subpixel True
        "UI_Tongue"        
        yzoom 0.45
        xzoom -0.45
        pos (240,680)#(250,670)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block: 
            easeout .5 rotate -50 pos (220,660) #(230,650)  
            linear .5 rotate -60 pos (210,670) #(220,660)
            easein 1 rotate 10 pos (240,680) #(250,670)
            repeat

image VibratorRightBreast_K: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (150,380)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 370
            pause .25
            ease 1 rotate 55 ypos 380           
            pause .25
            repeat

image VibratorLeftBreast_K: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (270,400)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 390
            pause .25
            ease 1 rotate 55 ypos 400           
            pause .25
            repeat
            
image VibratorPussy_K: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (240,665)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 70
        block:
            ease 1 rotate 35 xpos 230 ypos 655
            pause .25
            ease 1 rotate 70 xpos 240 ypos 665           
            pause .25
            repeat

image VibratorAnal_K: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (270,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 10
        block:
            ease 1 rotate 0 xpos 260 ypos 655
            pause .25
            ease 1 rotate 10 xpos 270 ypos 665           
            pause .25
            repeat
            
image VibratorPussyInsert_K: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_K: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0



#Lesbian action animations.
image GirlGropeLeftBreast_K:  
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (240,400)#(300,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -20
        block: 
            ease 1 rotate -40 pos (230,390)#(280,390)
            ease 1 rotate -20 pos (240,400)
            repeat

image GirlGropeRightBreast_K:    
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (110,380) #(160,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10#-30
        block: 
            ease 1 rotate -30 pos (110,410)#(160,410)
            ease 1 rotate -10 pos (110,380)
            repeat

image GirlGropeThigh_K: 
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (210,730)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        parallel: 
            pause .5
            ease 1 ypos 780
            ease 1 ypos 730            
            repeat
        parallel:            
            pause .5
            ease .5 xpos 213
            ease .5 xpos 210
            ease .5 xpos 213
            ease .5 xpos 210
            repeat

image GirlGropePussy_K: 
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (210,625)#(230,615)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (215,640)
                ease .5 rotate 195 
                ease .75 rotate 210 
                ease .5 rotate 195 
            choice: #slow rub
                ease .5 rotate 210 pos (215,640)#-10+20
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
#                ease .5 rotate 205 pos (225,620)
#                ease .75 rotate 200 pos (225,625)
                ease .5 rotate 205 pos (215,640)
                ease .75 rotate 200 pos (215,645)
                ease .5 rotate 205 pos (215,640)
                ease .75 rotate 200 pos (215,645)
            choice: #Fast stroke
                ease .3 rotate 205 pos (215,640)
                ease .3 rotate 200 pos (215,650)
                ease .3 rotate 205 pos (215,640)
                ease .3 rotate 200 pos (215,650)
            repeat

image GirlFingerPussy_K: 
    contains:
        subpixel True
        "UI_GirlFinger"       
        zoom .6
        pos (220,640)#(220,635)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (220,645)
                ease .5 rotate 195 
                ease .75 rotate 210 
                ease .5 rotate 195 
            choice: #slow rub
                ease .5 rotate 210 pos (220,645)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (220,655)
                ease .75 rotate 200 pos (220,660)
                ease .5 rotate 205 pos (220,655)
                ease .75 rotate 200 pos (220,660)
            choice: #Fast stroke
                ease .3 rotate 205 pos (220,655)
                ease .3 rotate 200 pos (220,665)
                ease .3 rotate 205 pos (220,655)
                ease .3 rotate 200 pos (220,665)
            repeat
            


# Start Kitty Faces / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label KittyFace(Emote = K_Emote, B = K_Blush, M = 0, Mouth = 0, Eyes = 0, Brows = 0):
        # Emote is the chosen emote, B is the lush state
        # M is whether the character is in a  manic state
        $ Emote = K_Emote if Emote == 5 else Emote
        $ B = K_Blush if B == 5 else B
        
        if (K_Forced or "angry" in K_RecentActions) and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "angry"     
        elif K_ForcedCount > 0 and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "sad"  
            
        if Emote == "normal":
                $ K_Mouth = "normal"
                $ K_Brows = "normal"
                $ K_Eyes = "normal"
        elif Emote == "angry":
                $ K_Mouth = "sad"
                $ K_Brows = "angry"
                $ K_Eyes = "sexy"
        elif Emote == "bemused":
                $ K_Mouth = "lipbite"
                $ K_Brows = "sad"
                $ K_Eyes = "squint"
        elif Emote == "closed":
                $ K_Mouth = "normal"
                $ K_Brows = "sad"
                $ K_Eyes = "closed"  
        elif Emote == "confused":
                $ K_Mouth = "kiss"
                $ K_Brows = "confused"
                $ K_Eyes = "surprised"
        elif Emote == "kiss":
                $ K_Mouth = "kiss"
                $ K_Brows = "normal"
                $ K_Eyes = "closed"
        elif Emote == "tongue":
                $ K_Mouth = "tongue"
                $ K_Brows = "sad"
                $ K_Eyes = "sexy" #"stunned"
        elif Emote == "manic":
                $ K_Mouth = "smile"
                $ K_Brows = "sad"
                $ K_Eyes = "surprised"
                $ K_Blush = 1
        elif Emote == "sad":
                $ K_Mouth = "sad"
                $ K_Brows = "sad"
                $ K_Eyes = "sexy"
        elif Emote == "sadside":
                $ K_Mouth = "sad"
                $ K_Brows = "sad"
                $ K_Eyes = "side"
        elif Emote == "sexy":
                $ K_Mouth = "lipbite"
                $ K_Brows = "normal"
                $ K_Eyes = "sexy"
        elif Emote == "smile":
                $ K_Mouth = "smile"
                $ K_Brows = "normal"
                $ K_Eyes = "normal"
        elif Emote == "sucking":
                $ K_Mouth = "sucking"
                $ K_Brows = "normal"
                $ K_Eyes = "closed"
        elif Emote == "surprised":
                $ K_Mouth = "surprised"
                $ K_Brows = "surprised"
                $ K_Eyes = "surprised"
        elif Emote == "startled":
                $ K_Mouth = "smile"
                $ K_Brows = "surprised"
                $ K_Eyes = "surprised"
        elif Emote == "down":
                $ K_Mouth = "surprised"
                $ K_Brows = "sad"
                $ K_Eyes = "down"  
        elif Emote == "perplexed":
                $ K_Mouth = "smile"
                $ K_Brows = "sad"
                $ K_Eyes = "normal"
        elif Emote == "sly":
                $ K_Mouth = "smile"
                $ K_Brows = "normal"
                $ K_Eyes = "squint"
            
        if M:
                $ K_Eyes = "surprised"        
        if B > 1:
                $ K_Blush = 2
        elif B:
                $ K_Blush = 1
        else:
                $ K_Blush = 0
        
        if Mouth:
                $ K_Mouth = Mouth
        if Eyes:
                $ K_Eyes = Eyes
        if Brows:
                $ K_Brows = Brows
        
        return