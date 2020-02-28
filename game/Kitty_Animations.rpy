# Basic Kitty Sprites
       
image Kitty_Sprite:        
    LiveComposite(
        (480,960),                                                                    
        (124,0), ConditionSwitch(
            "renpy.showing('Kitty_BJ_Animation')", Null(),
            "True", "Kitty_HairBack",   
            ),         
        (0,0), ConditionSwitch(                                                                         
            #Arms1               
            "not KittyX.ArmPose", "images/KittySprite/Kitty_Sprite_Arms1.png",
            "True", Null(),               
            ), 
        (0,0), ConditionSwitch(                                                                        
            #back of the shirt
            "KittyX.Over == 'pink top' and KittyX.ArmPose", "images/KittySprite/Kitty_Sprite_Under_Pink2.png",       #2
            "KittyX.Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Under_Pink1.png",                  #1
            "True", Null(),               
            ),
        (0,0), ConditionSwitch(                                                                         
            #body
            "KittyX.ArmPose and KittyX.Pubes", "images/KittySprite/Kitty_Sprite_Body_Hair2.png",     
            "KittyX.ArmPose", "images/KittySprite/Kitty_Sprite_Body_Bare2.png",               
            "KittyX.Pubes", "images/KittySprite/Kitty_Sprite_Body_Hair1.png",     
            "True", "images/KittySprite/Kitty_Sprite_Body_Bare1.png",    
            ),
        
#        (0,0), ConditionSwitch(                                                                         
#            #wet look
#            "KittyX.Water and KittyX.ArmPose", "images/KittySprite/Kitty_Sprite_Water2.png",
#            "KittyX.Water", "images/KittySprite/Kitty_Sprite_Water1.png",
#            "True", Null(),
#            ),  
        (0,0), ConditionSwitch(                                                                         
            #piercings bottom
            "not KittyX.Pierce or (KittyX.Panties and not KittyX.PantiesDown)", Null(),                       
            "KittyX.Pierce == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingB.png",      
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallB.png",   
            ),    
        
#        (0,0), ConditionSwitch(                                                                         
#            #panties
#            "not KittyX.Panties or KittyX.PantiesDown", Null(),
#            "KittyX.Legs or KittyX.Upskirt", Null(), #If panties are down, and pants are either off or down, skip this
            
#            "not KittyX.Panties or not KittyX.PantiesDown", Null(), #If panties are not down or if  pants are on and up, skip this
#            "KittyX.Legs and KittyX.Legs != 'blue skirt' and not KittyX.Upskirt", Null(), #If panties are not down or if  pants are on and up, skip this
            
#            "KittyX.Wet and KittyX.Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Wet.png",
#            "KittyX.Wet and KittyX.Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Wet.png",     
#            "KittyX.Wet and KittyX.Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_Wet.png",          
#            "KittyX.Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green.png",
#            "KittyX.Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace.png",
#            "KittyX.Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini.png", 
#            "True", Null(),
#            ),  
#        (0,0), ConditionSwitch(                                                                         
#            #panties down
#            "not KittyX.Panties or not KittyX.PantiesDown", Null(), #If panties are not down or if  pants are on and up, skip this
#            "KittyX.Legs and KittyX.Legs != 'blue skirt' and not KittyX.Upskirt", Null(), #If panties are not down or if  pants are on and up, skip this
#            "KittyX.Wet and KittyX.Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Down_Wet.png",
#            "KittyX.Wet and KittyX.Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Down_Wet.png",
#            "KittyX.Wet and KittyX.Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_DownW.png", 
#            "KittyX.Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Down.png",
#            "KittyX.Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Down.png",
#            "KittyX.Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_Down.png", 
#            "True", Null(),
#            ),  
        
        (0,0), ConditionSwitch(                                                                         
            #panties layer           
            "not KittyX.Panties", Null(),               
            "not KittyX.PantiesDown or (KittyX.Legs and KittyX.Legs != 'blue skirt' and not KittyX.Upskirt)", ConditionSwitch( 
                    # if the panties aren't down. . .
                    # and she's not wearing pants that are up
                    "KittyX.Wet", ConditionSwitch( 
                            # if they're up and wet. . .
                            "KittyX.Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Wet.png",
                            "KittyX.Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Wet.png",     
                            "KittyX.Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_Wet.png", 
                            "True", Null(),     
                            ),
                    "True", ConditionSwitch( 
                            #if they're just up. . .       
                            "KittyX.Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green.png",
                            "KittyX.Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace.png",
                            "KittyX.Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini.png", 
                            "True", Null(),     
                            ),    
                    ),                    
            "KittyX.Wet", ConditionSwitch( 
                    #if wet and down. . .
#                    "KittyX.Legs and KittyX.Legs != 'blue skirt' and not KittyX.Upskirt", Null(), #If nor wearing a skirt, they would be invisible 
                    "KittyX.Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Down_Wet.png",
                    "KittyX.Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Down_Wet.png",
                    "KittyX.Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_DownW.png", 
                    "True", Null(),     
                    ),
            "True", ConditionSwitch(
                    # if not wet, but down
#                    "KittyX.Legs and KittyX.Legs != 'blue skirt' and not KittyX.Upskirt", Null(), #If nor wearing a skirt, they would be invisible                     
                    "KittyX.Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Down.png",
                    "KittyX.Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Down.png",
                    "KittyX.Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_Down.png", 
                    "True", Null(),     
                    ),
            ),
        
        (225,560), ConditionSwitch(                                                                         
            #Personal Wetness            
            "not KittyX.Wet", Null(),
            "KittyX.Legs and not KittyX.Upskirt", Null(),   
            "KittyX.Panties and not KittyX.PantiesDown and KittyX.Wet <= 1", Null(),                   
            "KittyX.Wet == 1", ConditionSwitch( #Wet = 1
                    "KittyX.Panties and KittyX.PantiesDown", AlphaMask("Wet_Drip","Kitty_Drip_MaskP"),  
                    "KittyX.Legs", AlphaMask("Wet_Drip","Kitty_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip","Kitty_Drip_Mask"), #only plays if nothing is in the way
                    ),
            "True", ConditionSwitch( #Wet = 2+
                    "KittyX.Panties and KittyX.PantiesDown", AlphaMask("Wet_Drip2","Kitty_Drip_MaskP"), #"Wet_Drip2",# 
                    "KittyX.Legs", AlphaMask("Wet_Drip2","Kitty_Drip_MaskP"),
                    "KittyX.Panties", AlphaMask("Wet_Drip","Kitty_Drip_Mask"), #"Wet_Drip2",# 
                    "True", AlphaMask("Wet_Drip2","Kitty_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (0,0), ConditionSwitch(                                                                         
            #wetness                    
            "KittyX.Legs or not KittyX.Wet", Null(),             
            "KittyX.Panties and not KittyX.PantiesDown and KittyX.Wet < 2", Null(),
            "KittyX.Panties and not KittyX.PantiesDown", "images/KittySprite/Kitty_Sprite_Wet1.png",
            "KittyX.Wet == 2", "images/KittySprite/Kitty_Sprite_Wet2.png",
            "True", "images/KittySprite/Kitty_Sprite_Wet1.png",
            ),  
        (225,560), ConditionSwitch(                                                                         
            #Spunk nethers        
            "'in' not in KittyX.Spunk and 'anal' not in KittyX.Spunk", Null(),
            "KittyX.Legs and not KittyX.Upskirt", Null(),   
            "True", ConditionSwitch( #Wet = 2+
                    "KittyX.Panties and KittyX.PantiesDown", AlphaMask("Spunk_Drip2","Kitty_Drip_MaskP"), #"Wet_Drip2",# 
                    "KittyX.Legs", AlphaMask("Spunk_Drip2","Kitty_Drip_MaskP"),
                    "True", AlphaMask("Spunk_Drip2","Kitty_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),     
        (0,0), ConditionSwitch(                                                                        
            #pants         
            "KittyX.Legs == 'blue skirt' and KittyX.Upskirt", "images/KittySprite/Kitty_Sprite_Skirt_Up.png",       
            "KittyX.Legs == 'blue skirt'", "images/KittySprite/Kitty_Sprite_Skirt.png",          
            "not KittyX.Legs or KittyX.Upskirt", Null(),
            "KittyX.Legs == 'capris'", "images/KittySprite/Kitty_Sprite_Pants_Blue.png",
            "KittyX.Legs == 'black jeans'", "images/KittySprite/Kitty_Sprite_Pants_Black.png",
            "KittyX.Wet and KittyX.Legs == 'yoga pants'", "images/KittySprite/Kitty_Sprite_Pants_Yoga_Wet.png",   
            "KittyX.Legs == 'yoga pants'", "images/KittySprite/Kitty_Sprite_Pants_Yoga.png",   
            "KittyX.Wet and KittyX.Legs == 'shorts'", "images/KittySprite/Kitty_Sprite_Shorts_Wet.png",    
            "KittyX.Legs == 'shorts'", "images/KittySprite/Kitty_Sprite_Shorts.png",            
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(                                                                         
            #Arms2               
            "KittyX.ArmPose", "images/KittySprite/Kitty_Sprite_Arms2.png",
            "True", Null(),               
            ), 
        
        (0,0), "images/KittySprite/Kitty_Sprite_Chest_Bare.png", 
        (0,0), ConditionSwitch(   
            #piercings top
            "not KittyX.Pierce", Null(),                       
            "KittyX.Pierce == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingT.png",      
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallT.png",   
            ),    
#        (0,0), ConditionSwitch(                                                                         
#            #Bra
#            "not KittyX.Chest", Null(),
#            "KittyX.ArmPose and KittyX.Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami2.png",
#            "KittyX.ArmPose and KittyX.Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini2.png",
#            "KittyX.Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini1.png",
#            "KittyX.Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace.png",
#            "KittyX.Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport.png",
#            "KittyX.Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic.png",
#            "KittyX.Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1.png",
#            "KittyX.Chest == 0 and KittyX.Over == 'pink top'", Null(),   #use for when bra and top clash  
#            "True", Null(),       
#            ),  
        
        (0,0), ConditionSwitch(                                                                        
            #necklace
            "KittyX.Neck == 'gold necklace'", "images/KittySprite/Kitty_Sprite_Necklace1.png",
            "KittyX.Neck == 'star necklace'", "images/KittySprite/Kitty_Sprite_Necklace2.png",
            "True", Null(),
            ),   
        (0,0), ConditionSwitch(                                                                         
            #bra layer           
            "not KittyX.Chest", Null(),                  
            "not KittyX.Uptop", ConditionSwitch( 
                    #if the top's down. . .
                    "KittyX.ArmPose and KittyX.Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami2.png",
                    "KittyX.ArmPose and KittyX.Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini2.png",
                    "KittyX.Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini1.png",
                    "KittyX.Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace.png",
                    "KittyX.Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport.png",
                    "KittyX.Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic.png",
                    "KittyX.Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1.png",
                    "True", Null(),     
                    ),
            "KittyX.Over", ConditionSwitch(
                    # If she's wearing a shirt over the bra                        
#                    "KittyX.ArmPose and KittyX.Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1_UpS.png",
#                    "KittyX.ArmPose and KittyX.Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini2_UpS.png",
                    "KittyX.Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini1_Up.png",
                    "KittyX.Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace1_UpS.png",
                    "KittyX.Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport1_UpS.png",
                    "KittyX.Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic1_Up.png",
                    "KittyX.Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1_UpS.png",    
                    "True", Null(),     
                    ),
            "True", ConditionSwitch(
                    # if she's not wearing a shirt
                    "KittyX.ArmPose", ConditionSwitch(
                            # if Arms 2
                            "KittyX.Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini2_Up.png",
                            "KittyX.Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace2_Up.png",
                            "KittyX.Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport2_Up.png",
                            "KittyX.Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic2_Up.png",
                            "KittyX.Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami2_Up.png",            
                            "True", Null(),     
                            ),                    
                    "True", ConditionSwitch(
                            # if Arms 1
                            "KittyX.Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini1_Up.png",
                            "KittyX.Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace1_Up.png",
                            "KittyX.Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport1_Up.png",
                            "KittyX.Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic1_Up.png",
                            "KittyX.Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1_Up.png",            
                            "True", Null(),     
                            ),            
                    "True", Null(),     
                    ),
            ),
            
        (0,0), ConditionSwitch(                                                                        
            #piercings over shirt
            "not KittyX.Pierce or not KittyX.Chest or KittyX.Uptop", Null(),                       
            "KittyX.Pierce == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingOver.png",      
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallOver.png",   
            ),    
        (0,0), ConditionSwitch(                                                                        
            #wet look
            "KittyX.Water and KittyX.ArmPose", "images/KittySprite/Kitty_Sprite_Water2.png",
            "KittyX.Water", "images/KittySprite/Kitty_Sprite_Water1.png",
            "True", Null(),
            ),  
        
#        (0,0), ConditionSwitch(                                                                         
#            #shirt
#            "not KittyX.Over", Null(),
#            "KittyX.ArmPose and KittyX.Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink2.png",
#            "KittyX.ArmPose and KittyX.Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew2.png",
#            "KittyX.ArmPose and KittyX.Over == 'towel'", "images/KittySprite/Kitty_Sprite_Over_Towel2.png",
#            "KittyX.Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink1.png",
#            "KittyX.Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew1.png",
#            "KittyX.Over == 'towel'", "images/KittySprite/Kitty_Sprite_Over_Towel1.png",
#            "True", Null(),
#            ),   
                    
        (0,0), ConditionSwitch(                                                                         
            #shirt layer           
            "not KittyX.Over", Null(),                  
            "not KittyX.Uptop", ConditionSwitch( 
                    #if the top's down. . .
                    "KittyX.ArmPose and KittyX.Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink2.png",
                    "KittyX.ArmPose and KittyX.Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew2.png",
                    "KittyX.ArmPose and KittyX.Over == 'towel'", "images/KittySprite/Kitty_Sprite_Over_Towel2.png",
                    "KittyX.Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink1.png",
                    "KittyX.Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew1.png",
                    "KittyX.Over == 'towel'", "images/KittySprite/Kitty_Sprite_Over_Towel1.png",
                    "True", Null(),     
                    ),            
            "True", ConditionSwitch(
                    # if she's not wearing a shirt                    
                    "KittyX.ArmPose and KittyX.Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink2_Up.png",
                    "KittyX.ArmPose and KittyX.Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew2_Up.png",
#                    "KittyX.ArmPose and KittyX.Over == 'towel'", "images/KittySprite/Kitty_Sprite_Over_Towel2.png",
                    "KittyX.Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink1_Up.png",
                    "KittyX.Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew1_Up.png",            
#                    "KittyX.Over == 'towel'", "images/KittySprite/Kitty_Sex_Over_Towel.png",   
                    "True", Null(),     
                    ),
            ),
            
        (0,0), ConditionSwitch(                                                                         
            #bra over shirt layer           
            "not KittyX.Over or not KittyX.Chest or not KittyX.Uptop", Null(),   
            "KittyX.Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami_Over.png", 
            "KittyX.Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace_Over.png",
            "KittyX.Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport_Over.png",
            "KittyX.Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic_Over.png",
            "KittyX.Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini_Over.png",
            "True", Null(),  
            ),
            
        (124,0), ConditionSwitch(
            "renpy.showing('Kitty_BJ_Animation')", Null(),
            "True", "Kitty_Head",   
            ), 
        
        (0,0), ConditionSwitch(                                                                        
            #anal spunk
            "KittyX.Legs and not KittyX.Upskirt", Null(), 
            "KittyX.Panties and not KittyX.PantiesDown", Null(), 
            "'anal' in KittyX.Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Anal.png",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(                                                                        
            #pussy spunk
            "KittyX.Legs and not KittyX.Upskirt", Null(), 
            "KittyX.Panties and not KittyX.PantiesDown", Null(), 
            "'in' in KittyX.Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Pussy.png",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(                                                                         
            #belly spunk
            "'belly' in KittyX.Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Belly.png",
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(                                                                         
            #tits spunk
            "'tits' in KittyX.Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Tits.png",
            "True", Null(), 
            ),   
            
        (0,0), ConditionSwitch(
            #UI tool for When Kitty is masturbating using Trigger3 actions
            "Trigger == 'lesbian' or not Trigger3 or Ch_Focus != KittyX", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and KittyX.Lust >= 70", "GirlFingerPussy_Kitty",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_Kitty",            
            "Trigger3 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeLeftBreast_Kitty",    #When zero is working the right breast, fondle left
            "Trigger3 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeRightBreast_Kitty", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts'", "GirlGropeRightBreast_Kitty",
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast_Kitty",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy_Kitty",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy_Kitty",
            "Trigger3 == 'vibrator anal'", "VibratorAnal_Kitty",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy_Kitty",            
            "True", Null(),             
            ),                        
        (0,0), ConditionSwitch(  
            #UI tool for Trigger5(Threesome masutrbation) actions
            "not Trigger5 or Trigger4 != 'masturbation' or Ch_Focus == KittyX", Null(), 
            #this doesn't activate unless Kitty is not primary, and actively masturbating
            "Trigger5 == 'fondle pussy' and Trigger != 'sex' and KittyX.Lust >= 70", "GirlFingerPussy_Kitty",
            "Trigger5 == 'fondle pussy'", "GirlGropePussy_Kitty",
            "Trigger5 == 'fondle breasts'", "GirlGropeRightBreast_Kitty",
            "Trigger5 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger5 == 'vibrator pussy'", "VibratorPussy",
            "Trigger5 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger5 == 'vibrator anal'", "VibratorAnal",
            "Trigger5 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(), 
            ),               
        (0,0), ConditionSwitch(                
            #UI tool for Trigger1(primary) actions
            "not Trigger or Ch_Focus != KittyX", Null(),
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast_Kitty",
            "Trigger == 'fondle thighs'", "GropeThigh_Kitty",
            "Trigger == 'fondle breasts'", "GropeLeftBreast_Kitty",
            "Trigger == 'suck breasts'", "LickRightBreast_Kitty",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_Kitty",
            "Trigger == 'fondle pussy'", "GropePussy_Kitty",
            "Trigger == 'lick pussy'", "Lickpussy_Kitty",
            "Trigger == 'vibrator pussy'", "VibratorPussy_Kitty",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy_Kitty",
            "Trigger == 'vibrator anal'", "VibratorAnal_Kitty",
            "Trigger == 'vibrator anal insert'", "VibratorPussy_Kitty",
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                
            #UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus != KittyX", Null(),
            "not Trigger2 and not Trigger4 and Trigger == 'fondle breasts'", "GropeRightBreast_Kitty",        
            #When doing nothing offhand, use both hands on breasts.
            "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast_Kitty",            
            #When sucking right breast, fondle left
            "Trigger2 == 'fondle breasts'", "GropeRightBreast_Kitty",
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast_Kitty",       
            #When sucking right breast, vibrator left
            "Trigger2 == Trigger", Null(),
            #When both triggers are the same, do nothing              
            "Trigger2 == 'suck breasts'", "LickLeftBreast_Kitty",        
            "Trigger2 == 'fondle pussy'", "GropePussy_Kitty",
            "Trigger2 == 'lick pussy'", "Lickpussy_Kitty",       
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast_Kitty",
            "Trigger2 == 'vibrator pussy'", "VibratorPussy_Kitty",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy_Kitty",
            "Trigger2 == 'vibrator anal'", "VibratorAnal_Kitty",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy_Kitty",
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(  
            #UI tool for Trigger4(Threesome) actions (ie Rogue's hand on her)
            "not Trigger4 or Ch_Focus != KittyX", Null(),
            "Trigger4 == 'fondle pussy' and Trigger != 'sex' and KittyX.Lust >= 70", "GirlFingerPussy_Kitty",
            "Trigger4 == 'fondle pussy'", "GirlGropePussy_Kitty",            
            "Trigger4 == 'lick pussy'", "Lickpussy_Kitty",
            "Trigger4 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Kitty", 
            "Trigger4 == 'suck breasts'", "LickRightBreast_Kitty",  
            "Trigger4 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Kitty",    #When zero is working the right breast, fondle left
            "Trigger4 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Kitty", #When zero is working the left breast, fondle right  
            "Trigger4 == 'fondle breasts' and (Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts')", "GirlGropeLeftBreast_Kitty", #When zero is working the left breast, fondle right  
            "Trigger4 == 'fondle breasts'", "GirlGropeRightBreast_Kitty",
            "Trigger4 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger4 == 'vibrator pussy'", "VibratorPussy",
            "Trigger4 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger4 == 'vibrator anal'", "VibratorAnal",
            "Trigger4 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),             
            ),    
        (0,0), ConditionSwitch(  
            #UI tool for Trigger3(lesbian) actions (ie Rogue's hand on her when Kitty is secondary)
            "Trigger != 'lesbian' or not Trigger3 or Ch_Focus == KittyX", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and KittyX.Lust >= 70", "GirlFingerPussy_Kitty",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_Kitty",            
            "Trigger3 == 'lick pussy'", "Lickpussy_Kitty",
            "Trigger3 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Kitty", 
            "Trigger3 == 'suck breasts'", "LickRightBreast_Kitty",  
            "Trigger3 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Kitty",    #When zero is working the right breast, fondle left
            "Trigger3 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Kitty", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts' and (Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts')", "GirlGropeLeftBreast_Kitty", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts'", "GirlGropeRightBreast_Kitty",
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
    pos (500,100) #fix remove diagnostic                   


image Kitty_Head:               
    LiveComposite(
        (416,610),    
#        (0,0), ConditionSwitch(
#            "KittyX.Water", "images/KittySprite/Kitty_Sprite_Hair_Wet_Back.png",
#            "KittyX.Hair == 'long'", "images/KittySprite/Kitty_Sprite_Hair_Long_Back.png",
#            "True", Null(),
#            ),    
        (0,0), ConditionSwitch(
            "KittyX.Water and KittyX.Blush == 1", "images/KittySprite/Kitty_Sprite_Head_Wet_Blush1.png",
            "KittyX.Water and KittyX.Blush == 2", "images/KittySprite/Kitty_Sprite_Head_Wet_Blush2.png",
            "KittyX.Water", "images/KittySprite/Kitty_Sprite_Head_Wet_Base.png",
            "KittyX.Blush == 1", "images/KittySprite/Kitty_Sprite_Head_Evo_Blush1.png",
            "KittyX.Blush == 2", "images/KittySprite/Kitty_Sprite_Head_Evo_Blush2.png",
            "True", "images/KittySprite/Kitty_Sprite_Head_Evo_Base.png",
            ),     
        (0,0), ConditionSwitch(
            "KittyX.Brows == 'normal'", "images/KittySprite/Kitty_Sprite_Brows_Normal.png",
            "KittyX.Brows == 'angry'", "images/KittySprite/Kitty_Sprite_Brows_Angry.png",
            "KittyX.Brows == 'sad'", "images/KittySprite/Kitty_Sprite_Brows_Sad.png",
            "KittyX.Brows == 'surprised'", "images/KittySprite/Kitty_Sprite_Brows_Surprised.png",
            "KittyX.Brows == 'confused'", "images/KittySprite/Kitty_Sprite_Brows_Confused.png",
            "True", "images/KittySprite/Kitty_Sprite_Brows_Normal.png",
            ),
        (0,0), ConditionSwitch(
            "KittyX.Mouth == 'normal'", "images/KittySprite/Kitty_Sprite_Mouth_Normal.png",
            "KittyX.Mouth == 'lipbite'", "images/KittySprite/Kitty_Sprite_Mouth_Lipbite.png",
            "KittyX.Mouth == 'kiss'", "images/KittySprite/Kitty_Sprite_Mouth_Kiss.png",
            "KittyX.Mouth == 'sad'", "images/KittySprite/Kitty_Sprite_Mouth_Sad.png",
            "KittyX.Mouth == 'smile'", "images/KittySprite/Kitty_Sprite_Mouth_Smile.png",
            "KittyX.Mouth == 'surprised'", "images/KittySprite/Kitty_Sprite_Mouth_Surprised.png",
            "KittyX.Mouth == 'tongue'", "images/KittySprite/Kitty_Sprite_Mouth_Tongue.png",
            "KittyX.Mouth == 'sucking'", "images/KittySprite/Kitty_Sprite_Mouth_Tongue.png", #fix add
            "True", "images/KittySprite/Kitty_Sprite_Mouth_Normal.png",
            ),      
        (0,0), ConditionSwitch(
            "'mouth' not in KittyX.Spunk", Null(),            
            "KittyX.Mouth == 'normal'", "images/KittySprite/Kitty_Sprite_Spunk_Normal.png",
            "KittyX.Mouth == 'lipbite'", "images/KittySprite/Kitty_Sprite_Spunk_Normal.png",
            "KittyX.Mouth == 'kiss'", "images/KittySprite/Kitty_Sprite_Spunk_Kiss.png",
            "KittyX.Mouth == 'sad'", "images/KittySprite/Kitty_Sprite_Spunk_Sad.png",
            "KittyX.Mouth == 'smile'", "images/KittySprite/Kitty_Sprite_Spunk_Smile.png",
            "KittyX.Mouth == 'surprised'", "images/KittySprite/Kitty_Sprite_Spunk_Surprised.png",
            "KittyX.Mouth == 'tongue'", "images/KittySprite/Kitty_Sprite_Spunk_Tongue.png",
            "KittyX.Mouth == 'sucking'", "images/KittySprite/Kitty_Sprite_Spunk_Sucking.png", #fix add
            "True", Null(),
            ),       
        (0,0), ConditionSwitch(
            "'facial' in KittyX.Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Facial.png",
            "True", Null(),
            ),     
        (0,0), "Kitty Blink",
        (0,0), ConditionSwitch(
            "KittyX.Water", "images/KittySprite/Kitty_Sprite_Hair_Wet.png",
            "KittyX.Hair == 'evo'", "images/KittySprite/Kitty_Sprite_Hair_Evo.png",
            "KittyX.Hair == 'long'", "images/KittySprite/Kitty_Sprite_Hair_Long.png",
            "KittyX.Hair == 'wet'", "images/KittySprite/Kitty_Sprite_Hair_Wet.png",
            "True", "images/KittySprite/Kitty_Sprite_Hair_Evo.png",
            ),     
        (0,0), ConditionSwitch(
            "KittyX.Water", "images/KittySprite/Kitty_Sprite_Wet_Head.png",
            "True", Null(),
            ),     
        (0,0), ConditionSwitch(
            "KittyX.Hair == 'evo' and 'hair' in KittyX.Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Evohair.png",
            "KittyX.Hair == 'long' and 'hair' in KittyX.Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Evohair.png",
#            "KittyX.Hair == 'evo' and 'hair' in KittyX.Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Evohair.png",
            "True", Null(),
            ),     
        )
#    anchor (0.6, 0.0)
    zoom .5

image Kitty_HairBack:
    LiveComposite(
        (416,610),    
        (0,0), ConditionSwitch(
            "KittyX.Water or KittyX.Hair == 'wet'", "images/KittySprite/Kitty_Sprite_Hair_Wet_Back.png",
            "KittyX.Hair == 'long'", "images/KittySprite/Kitty_Sprite_Hair_Long_Back.png",
            "True", Null(),
            ),    
        )
#    anchor (0.6, 0.0)
    zoom .5
    
image Kitty Blink:
    ConditionSwitch( 
    "KittyX.Eyes == 'sexy'", "images/KittySprite/Kitty_Sprite_Eyes_Sexy.png", 
    "KittyX.Eyes == 'side'", "images/KittySprite/Kitty_Sprite_Eyes_Side.png",  
    "KittyX.Eyes == 'surprised'", "images/KittySprite/Kitty_Sprite_Eyes_Surprised.png",  
    "KittyX.Eyes == 'manic'", "images/KittySprite/Kitty_Sprite_Eyes_Surprised.png",  
    "KittyX.Eyes == 'normal'", "images/KittySprite/Kitty_Sprite_Eyes_Normal.png",  
    "KittyX.Eyes == 'down'", "images/KittySprite/Kitty_Sprite_Eyes_Down.png",  
    "KittyX.Eyes == 'stunned'", "images/KittySprite/Kitty_Sprite_Eyes_Down.png",  
    "KittyX.Eyes == 'squint'", "Kitty_Squint",  
    "KittyX.Eyes == 'leftside'", "images/KittySprite/Kitty_Sprite_Eyes_SideLeft.png",
    "KittyX.Eyes == 'closed'", "images/KittySprite/Kitty_Sprite_Eyes_Closed.png",    
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
                "not Player.Sprite", "Kitty_Sex_Body_Static", 
                "Player.Cock == 'anal'", ConditionSwitch( 
                        #if the top's down. . .
                        "Speed >= 3", "Kitty_Sex_Body_Anim3",
                        "Speed >= 2", "Kitty_Sex_Body_Anim2",
                        "Speed", "Kitty_Sex_Body_Anim1",
                        "True", "Kitty_Sex_Body_Static",   
                        ),            
                "Player.Cock == 'in'", ConditionSwitch( 
                        #if the top's down. . .
                        "Speed >= 3", "Kitty_Sex_Body_Anim3",
                        "Speed >= 2", "Kitty_Sex_Body_Anim2",
                        "Speed", "Kitty_Sex_Body_Anim1",
                        "True", "Kitty_Sex_Body_Static",   
                        ),             
                "Player.Cock == 'foot'", ConditionSwitch( 
                        #if the top's down. . .
                        "Speed >= 2", "Kitty_Sex_Body_FootAnim2",
                        "Speed", "Kitty_Sex_Body_FootAnim1",
                        "True", "Kitty_Sex_Body_FootAnimStatic",   
                        ),            
                "Player.Cock == 'out' and Speed >= 2","Kitty_Hotdog_Body_Anim2",                                    
                "True", "Kitty_Sex_Body_Static",           
                ),              
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events            
                "not Player.Sprite", "Kitty_Sex_Legs_Static", 
                "Player.Cock == 'anal'", ConditionSwitch( 
                        #if the top's down. . .
                        "Speed >= 3", "Kitty_Sex_Legs_Anim3",
                        "Speed >= 2", "Kitty_Sex_Legs_Anim2",
                        "Speed", "Kitty_Sex_Legs_Anim1",
                        "True", "Kitty_Sex_Legs_Static",   
                        ),            
                "Player.Cock == 'in'", ConditionSwitch( 
                        #if the top's down. . .
                        "Speed >= 3", "Kitty_Sex_Legs_Anim3",
                        "Speed >= 2", "Kitty_Sex_Legs_Anim2",
                        "Speed", "Kitty_Sex_Legs_Anim1",
                        "True", "Kitty_Sex_Legs_Static",   
                        ),             
                "Player.Cock == 'foot'", ConditionSwitch( 
                        #if the top's down. . .
                        "Speed >= 2", "Kitty_Sex_Legs_FootAnim2",
                        "Speed", "Kitty_Sex_Legs_FootAnim1",
                        "True", "Kitty_Sex_Legs_FootAnimStatic",   
                        ),            
                "Player.Cock == 'out' and Speed >= 2","Kitty_Hotdog_Legs_Anim2",                                    
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

image Kitty_Sex_Body = LiveComposite(                                                                                
        #the torso/head used in the sex pose, referenced by Kitty_SexSprite
        (1120,840),
#        (0,0), ConditionSwitch(                                                                                 #Hair underlayer, delete once this is working
#            "KittyX.Water", Null(), 
#            "KittyX.Hair == 'evo'", "images/KittySex/Kitty_Sex_HairB.png",   
#            "True", Null(),                   
#            ),   
        (260,-350), "Kitty_HairBack_Sex",                                                                                      #Hair underlayer
        (0,0), ConditionSwitch(                                                                                 #Body Base
            "KittyX.Pierce == 'barbell'", "images/KittySex/Kitty_Sex_Body_Barbell.png",   
            "KittyX.Pierce == 'ring'", "images/KittySex/Kitty_Sex_Body_Ring.png",   
            "True", "images/KittySex/Kitty_Sex_Body.png",             
            ),            
        (260,-350), "Kitty_Head_Sex",  #check positioning (400,-300)
        #Eyes
        (0,0), ConditionSwitch(                                                                                 #necklace
            "KittyX.Neck == 'gold necklace'", "images/KittySex/Kitty_Sex_Neck_Gold.png",
            "KittyX.Neck == 'star necklace'", "images/KittySex/Kitty_Sex_Neck_Star.png",
            "True", Null(),
            ),  
#        (0,0), ConditionSwitch(                                                                                 #tanktop
#            "not KittyX.Chest", Null(),        
#            "KittyX.Chest == 'cami'", "images/KittySex/Kitty_Sex_Under_Cami.png",
#            "KittyX.Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Under_SportsBra.png",
#            "KittyX.Chest == 'bra'", "images/KittySex/Kitty_Sex_Under_Bra.png",
#            "KittyX.Chest == 'lace bra'", "images/KittySex/Kitty_Sex_Under_LaceBra.png",
#            "True", Null(),            
#            ), 
        
        (0,0), ConditionSwitch(                                                                         
            #bra layer           
            "not KittyX.Chest", Null(),                  
            "not KittyX.Uptop", ConditionSwitch( 
                    #if the top's down. . .
                    "KittyX.Chest == 'cami'", "images/KittySex/Kitty_Sex_Under_Cami.png",
                    "KittyX.Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Under_SportsBra.png",
                    "KittyX.Chest == 'bra'", "images/KittySex/Kitty_Sex_Under_Bra.png",
                    "KittyX.Chest == 'bikini top'", "images/KittySex/Kitty_Sex_Under_Bikini.png",
                    "KittyX.Chest == 'lace bra'", "images/KittySex/Kitty_Sex_Under_LaceBra.png",
                    "True", Null(),     
                    ),
            "KittyX.Over", ConditionSwitch(
                    # If she's wearing a shirt over the bra
                    "KittyX.Chest == 'cami'", "images/KittySex/Kitty_Sex_Under_Cami_UpS.png",
                    "KittyX.Chest == 'bikini top'", "images/KittySex/Kitty_Sex_Under_Bikini_Up.png",
                    "KittyX.Chest == 'sports bra' and KittyX.Over == 'red shirt'", "images/KittySex/Kitty_Sex_Under_SportsBra_UpS.png",
                    "KittyX.Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Under_SportsBra_Up.png",
                    "True", Null(),     
                    ),
            "True", ConditionSwitch(
                    # if she's not wearing a shirt
                    "KittyX.Chest == 'cami'", "images/KittySex/Kitty_Sex_Under_Cami_Up.png",
                    "KittyX.Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Under_SportsBra_Up.png",
                    "KittyX.Chest == 'bra'", "images/KittySex/Kitty_Sex_Under_Bra_Up.png",
                    "KittyX.Chest == 'bikini top'", "images/KittySex/Kitty_Sex_Under_Bikini_Up.png",
                    "KittyX.Chest == 'lace bra'", "images/KittySex/Kitty_Sex_Under_LaceBra_Up.png",
                    "True", Null(),     
                    ),
            ),
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "KittyX.Water", "images/KittySex/Kitty_Sex_Water_Body.png",   
            "True", Null(),              
            ), 
#        (0,0), ConditionSwitch(                                                                                 #Wet look
#            "KittyX.Pierce == 'barbell'", "images/KittySex/Kitty_Sex_Body_Barbell.png",   
#            "KittyX.Pierce == 'ring'", "images/KittySex/Kitty_Sex_Body_Ring.png",   
#            "True", Null(),              
#            ), 
        
#        (0,0), ConditionSwitch(                                                                                 #Overshirt
#            "not KittyX.Over", Null(),
#            "KittyX.Over == 'pink top'", "images/KittySex/Kitty_Sex_Over_PinkShirt.png",           
#            "KittyX.Over == 'red shirt'", "images/KittySex/Kitty_Sex_Over_RedShirt.png",   
#            "KittyX.Over == 'towel'", "images/KittySex/Kitty_Sex_Over_Towel.png",       
#            "True", Null(), 
#            ), 
        
        (0,0), ConditionSwitch(                                                                         
            #shirt layer           
            "not KittyX.Over", Null(),                  
            "not KittyX.Uptop", ConditionSwitch( 
                    #if the top's down. . .
                    "KittyX.Over == 'pink top'", "images/KittySex/Kitty_Sex_Over_PinkShirt.png",           
                    "KittyX.Over == 'red shirt'", "images/KittySex/Kitty_Sex_Over_RedShirt.png",   
                    "KittyX.Over == 'towel'", "images/KittySex/Kitty_Sex_Over_Towel.png",   
                    "True", Null(),     
                    ),            
            "True", ConditionSwitch(
                    # if she's not wearing a shirt
                    "KittyX.Over == 'pink top' and KittyX.Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Over_PinkShirt_UpS.png", 
                    "KittyX.Over == 'pink top'", "images/KittySex/Kitty_Sex_Over_PinkShirt_Up.png",           
                    "KittyX.Over == 'red shirt'", "images/KittySex/Kitty_Sex_Over_RedShirt_Up.png",   
#                    "KittyX.Over == 'towel'", "images/KittySex/Kitty_Sex_Over_Towel.png",   
                    "True", Null(),     
                    ),
            ),
        (0,0), ConditionSwitch(                                                                         
            #bra layer over the shirt          
            "not KittyX.Chest or not KittyX.Over or not KittyX.Uptop", Null(),    
            # if she's not wearing a shirt
            "KittyX.Chest == 'bra'", "images/KittySex/Kitty_Sex_Under_Bra_Up.png",
            "KittyX.Chest == 'lace bra'", "images/KittySex/Kitty_Sex_Under_LaceBra_UpS.png",
            "True", Null(),    
            ),
        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'belly' in KittyX.Spunk", "images/KittySex/Kitty_Sex_Spunk_Body.png",   
            "True", Null(),  
            ),  
        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'tits' in KittyX.Spunk", "images/KittySex/Kitty_Sex_Spunk_Tits.png",   
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
            "KittyX.Legs == 'blue skirt'", "images/KittySex/Kitty_Sex_Skirt_Back.png",   
            "True", Null(),                      
            ),  
        (0,0), "images/KittySex/Kitty_Sex_Legs.png",                                                         #Legs Base
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "KittyX.Water", "images/KittySex/Kitty_Sex_Water_Legs.png",   
            "True", Null(),              
            ),  
        (0,0), "Kitty_Sex_Anus",                                                                          #Anus Composite 

        (0,0), "Kitty_Sex_Pussy",                                                                         #Pussy Composite

        (0,0), ConditionSwitch(                                                                                 #Panties if up
            "KittyX.PantiesDown", Null(),     
            "KittyX.Panties == 'green panties' and KittyX.Wet", "images/KittySex/Kitty_Sex_Panties_Green_Wet.png",          
            "KittyX.Panties == 'green panties'", "images/KittySex/Kitty_Sex_Panties_Green.png",    
            "KittyX.Panties == 'lace panties' and KittyX.Wet", "images/KittySex/Kitty_Sex_Panties_Lace_Wet.png",       
            "KittyX.Panties == 'lace panties'", "images/KittySex/Kitty_Sex_Panties_Lace.png",    
            "KittyX.Panties == 'bikini bottoms' and KittyX.Wet", "images/KittySex/Kitty_Sex_Panties_Bikini_Wet.png",       
            "KittyX.Panties == 'bikini bottoms'", "images/KittySex/Kitty_Sex_Panties_Bikini.png",    
            "True", Null(),                     
            ),  
        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            "KittyX.Legs == 'blue skirt'", "images/KittySex/Kitty_Sex_Skirt.png",   
            "KittyX.Upskirt", Null(),                            
            "KittyX.Legs == 'capris' and KittyX.Wet > 1", "images/KittySex/Kitty_Sex_Pants_Blue_Wet.png",
            "KittyX.Legs == 'capris'", "images/KittySex/Kitty_Sex_Pants_Blue.png",
            "KittyX.Legs == 'black jeans' and KittyX.Wet > 1", "images/KittySex/Kitty_Sex_Pants_Black_Wet.png",
            "KittyX.Legs == 'black jeans'", "images/KittySex/Kitty_Sex_Pants_Black.png",
            "KittyX.Legs == 'shorts' and KittyX.Wet > 1", "images/KittySex/Kitty_Sex_Shorts_Wet.png",
            "KittyX.Legs == 'shorts'", "images/KittySex/Kitty_Sex_Shorts.png",
            "KittyX.Legs == 'yoga pants' and KittyX.Wet > 1", "images/KittySex/Kitty_Sex_Pants_Yoga_Wet.png",
            "KittyX.Legs == 'yoga pants'", "images/KittySex/Kitty_Sex_Pants_Yoga.png",
            "True", Null(),                      
            ),   
        (0,0), ConditionSwitch(                                                                                 #Over Layer
            "KittyX.Over == 'towel'", "images/KittySex/Kitty_Sex_Towel_Legs.png",
            "True", Null(),                    
            ),   
        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'belly' in KittyX.Spunk", "images/KittySex/Kitty_Sex_Spunk_Pelvis.png",   
            "True", Null(),  
            ),  
        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer  
            "not Player.Sprite or Player.Cock != 'out'", Null(),                    
            "Speed >= 2", "Kitty_Hotdog_Zero_Anim2",
            "Speed", "Kitty_Hotdog_Zero_Anim1",
            "True", "Kitty_Hotdog_Zero_Anim0",   
            ), 
        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer  
            "not Player.Sprite or Player.Cock != 'foot'", Null(),                    
            "Speed >= 2", "Kitty_Footcock_Zero_Anim2",
            "Speed", "Kitty_Footcock_Zero_Anim1",
            "True", "Kitty_Footcock_Static",   
            ),
#        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer  
#            "not Player.Sprite or Player.Cock != 'foot'", Null(),                    
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
            "Player.Cock == 'anal' or Player.Cock == 'in' or Player.Cock == 'out'", AlphaMask("Kitty_Sex_Feet", "images/KittySex/Kitty_Sex_FeetMask.png"), 
            "True", "Kitty_Sex_Feet",            
            ),
        )
    
image Kitty_Sex_Feet = LiveComposite(                                                                                          
        #the lower legs used in the sex pose, referenced by Kitty_Sex_Legs
        (1120,840), 
        (0,0), "images/KittySex/Kitty_Sex_Feet.png",                                                         #Legs Base
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "KittyX.Water", "images/KittySex/Kitty_Sex_Water_Feet.png",   
            "True", Null(),              
            ),  
        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            "KittyX.Upskirt", Null(),                               
            "KittyX.Legs == 'capris'", "images/KittySex/Kitty_Sex_Feet_Blue.png",
            "KittyX.Legs == 'black jeans'", "images/KittySex/Kitty_Sex_Feet_Black.png",
            "KittyX.Legs == 'yoga pants'", "images/KittySex/Kitty_Sex_Feet_Yoga.png",
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
                "not KittyX.Pubes", Null(),         
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
                "not KittyX.Pubes", Null(),         
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
                "not KittyX.Pubes", Null(),         
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
                "not KittyX.Pubes", Null(),         
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
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/KittySex/Kitty_Sex_Pussy_Fucking.png",
                "Player.Sprite and Player.Cock == 'in' and Speed", "images/KittySex/Kitty_Sex_Pussy_Open.png",
                "Player.Sprite and Player.Cock == 'in'", "images/KittySex/Kitty_Sex_Pussy_Closed.png",    
                "Trigger == 'lick pussy'", "images/KittySex/Kitty_Sex_Pussy_Open.png",   
                "True", "images/KittySex/Kitty_Sex_Pussy_Closed.png",
                )
    contains:
            # The background plate of her pussy            
            ConditionSwitch(    
                "not KittyX.Wet", Null(),  
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/KittySex/Kitty_Sex_WetPussy_F.png",
                "True", "images/KittySex/Kitty_Sex_WetPussy_C.png",
                )
    contains: 
            #ring piercing
            ConditionSwitch(  
                "KittyX.Pierce != 'ring'", Null(),
                "not Player.Sprite or Player.Cock != 'in' or Speed <= 1", "images/KittySex/Kitty_Sex_Pussy_Ring.png",
                "True", "images/KittySex/Kitty_Sex_Pussy_RingF.png",
                ) 
    contains: 
            #barbell piercing
            ConditionSwitch(  
                "KittyX.Pierce != 'barbell'", Null(),
                "not Player.Sprite or Player.Cock != 'in' or Speed <= 1", "images/KittySex/Kitty_Sex_Pussy_Barbell.png",
                "True", "images/KittySex/Kitty_Sex_Pussy_BarbellF.png",
                )             
    contains:
            # pubes
            ConditionSwitch(    
                "not KittyX.Pubes", Null(),         
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/KittySex/Kitty_Sex_Pubes_Fucking.png",
                "Player.Sprite and Player.Cock == 'in' and Speed", "images/KittySex/Kitty_Sex_Pubes_Open.png",
                "Player.Sprite and Player.Cock == 'in'", "images/KittySex/Kitty_Sex_Pubes_Closed.png", 
                "Trigger == 'lick pussy'", "images/KittySex/Kitty_Sex_Pubes_Open.png", 
                "True", "images/KittySex/Kitty_Sex_Pubes_Closed.png",
                )
    contains:
            #Spunk under penis
            ConditionSwitch(    
                "'in' in KittyX.Spunk", "images/KittySex/Kitty_Sex_Spunk_Puss_Under.png",   
                "True", Null(),  
                )  
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            ConditionSwitch(    
                "not Player.Sprite", Null(),  
                "Player.Sprite and Player.Cock == 'in' and Speed >= 3", AlphaMask("Kitty_Sex_Zero_Anim3", "Kitty_Pussy_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", AlphaMask("Kitty_Sex_Zero_Anim2", "Kitty_Pussy_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and Speed", AlphaMask("Kitty_Sex_Zero_Anim1", "Kitty_Pussy_Open_Mask"),
                "Player.Sprite and Player.Cock == 'in'", AlphaMask("Kitty_Sex_Zero_Anim0", "Kitty_Pussy_Open_Mask"),  
                "True", Null(),  
                )  
    contains:
            #Spunk over penis
            ConditionSwitch(    
                "'in' not in KittyX.Spunk or not Player.Sprite or Player.Cock != 'in' or not Speed", Null(), 
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
            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/KittySex/Kitty_Sex_Hole_Open.png",         
            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/KittySex/Kitty_Sex_Hole_Open.png",
            "Player.Sprite and Player.Cock == 'anal' and Speed", "Kitty_Anal_Heading",
            "Player.Sprite and Player.Cock == 'anal'", "Kitty_Anal_Tip", 
            "KittyX.Loose", "images/KittySex/Kitty_Sex_Hole_Loose.png",   
            "True", "images/KittySex/Kitty_Sex_Hole_Tight.png", 
            )    
    contains:
            #Spunk under penis
            ConditionSwitch(    
                "'anal' not in KittyX.Spunk", Null(),  
                "Player.Sprite and Player.Cock != 'anal' and Speed >= 1", "images/KittySex/Kitty_Sex_Spunk_Anal_Under.png",  
                "Player.Sprite and Player.Cock != 'anal' and Speed == 1", "Kitty_Anal_Spunk_Heading_Under",
                "True", "images/KittySex/Kitty_Sex_Spunk_Anal_Closed.png",  
                )  
    contains:
            # The animation of Zero's moving penis, masked by her anus shape
            ConditionSwitch(               
            "not Player.Sprite or Player.Cock != 'anal'", Null(),                                                                                    
            "Speed >= 3",  AlphaMask("Kitty_Anal_Zero_Anim3", "Kitty_Anal_Fucking_Mask"),        
            "Speed >= 2", AlphaMask("Kitty_Anal_Zero_Anim2", "Kitty_Anal_Fucking_Mask"),
            "Speed", AlphaMask("Kitty_Anal_Zero_Anim1", "Kitty_Anal_Fucking_Mask"),
            "True", AlphaMask("Kitty_Anal_Zero_Anim0", "Kitty_Anal_Fucking_Mask"), 
            )    
    contains:
            #Spunk over penis
            ConditionSwitch(    
                "'anal' not in KittyX.Spunk or not Player.Sprite or Player.Cock != 'anal' or not Speed", Null(),  
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
        $ Player.Cock = "in"
    elif Line == "anal":
        $ Player.Cock = "anal"
    elif Line == "solo":   
        $ Player.Sprite = 0
        $ Player.Cock = "out"
    elif Line == "hotdog":          
        $ Player.Cock = "out"
    elif Line == "foot":          
        $ Player.Cock = "foot"
    if not Trigger:
        $ Trigger = Line
    if renpy.showing("Kitty_SexSprite"):
        return 
    $ Player.Sprite = 1
    $ Speed = 0
    hide Kitty_Sprite    
    call Kitty_Hide 
    show Kitty_SexSprite zorder 150
#    show Kitty_SexSprite zorder 150:
#        pos (750,230)

    with dissolve
    return
    
label Kitty_Sex_Reset:
    if not renpy.showing("Kitty_SexSprite"):
        return
    $ KittyX.ArmPose = 2     
    hide Kitty_SexSprite
    call Kitty_Hide 
#    call Set_The_Scene(Dress = 0)    
    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer:
        alpha 1
        zoom 1 offset (0,0) 
        anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return
label Kitty_Doggy_Reset:
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
            "Speed < 3 or 'mouth' not in KittyX.Spunk", Null(),
            "Speed == 3", At("KittySuckingSpunk", Kitty_BJ_Head_3()), #Sucking
            "Speed == 4", At("KittySuckingSpunk", Kitty_BJ_Head_4()), #Deepthroat
            "Speed == 6", At("KittySuckingSpunk", Kitty_BJ_Head_6()), #Cumming Deep
            "True", Null(),
            ),    
        (325,490), ConditionSwitch(                                                                 
            # same as above, but for the heading animation
            "Speed == 2 and 'mouth' in KittyX.Spunk", At("Kitty_BJ_MaskHeadingSpunk", Kitty_BJ_Head_2()), #Heading
            "Speed == 5 and 'mouth' in KittyX.Spunk", At("Kitty_BJ_MaskHeadingSpunk", Kitty_BJ_Head_5()), #Cumming High
            "True", Null(),
            ),   
        )
    zoom .55
    anchor (.5,.5)
    
image Kitty_BJ_HairBack:
    #Hair underlay
    ConditionSwitch(                                                                            
            "KittyX.Water and KittyX.Hair == 'evo'", "images/KittyBJFace/Kitty_BJ_HairBackWet.png",
            "KittyX.Hair == 'long'", "images/KittyBJFace/Kitty_BJ_HairBackWet.png",            
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
            "'blanket' in KittyX.RecentActions", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                         
            #red shirt under
            "KittyX.Over == 'red shirt'", "images/KittyBJFace/Kitty_BJ_Over_RedUnder.png",
            "True", Null(),
            ),  
        (0,0),"images/KittyBJFace/Kitty_BJ_Body.png",                                                   
            #body
        (0,0), ConditionSwitch(                                                                         
            #necklace
            "KittyX.Neck == 'gold necklace'", "images/KittyBJFace/Kitty_BJ_Neck_Gold.png",
            "KittyX.Neck == 'star necklace'", "images/KittyBJFace/Kitty_BJ_Neck_Star.png",
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                  
            # piercings
            "not KittyX.Pierce", Null(),                       
            "KittyX.Pierce == 'ring'", "images/KittyBJFace/Kitty_BJ_PierceRing.png",      
            "True", "images/KittyBJFace/Kitty_BJ_PierceBall.png",   
            ),   
        (0,0), ConditionSwitch(                                                                         
            # wet body
            "not KittyX.Water", Null(),
            "True", "images/KittyBJFace/Kitty_BJ_Wet_Body.png",
            ),  
            
        (0,0), ConditionSwitch(                                                                        
            #Bra
            "not KittyX.Chest", Null(),
            "KittyX.Chest == 'lace bra'", "images/KittyBJFace/Kitty_BJ_Bra_Lace.png",
            "KittyX.Chest == 'sports bra'", "images/KittyBJFace/Kitty_BJ_Bra_Sport.png",
            "KittyX.Chest == 'bra'", "images/KittyBJFace/Kitty_BJ_Bra.png",
            "KittyX.Chest == 'cami'", "images/KittyBJFace/Kitty_BJ_Bra_Cami.png",
            "True", Null(),       
            ),  
            
        (0,0), ConditionSwitch(                                                                         
            #Shirt
            "not KittyX.Over", Null(),
            "KittyX.Over == 'pink top'", "images/KittyBJFace/Kitty_BJ_Over_PinkShirt.png",
            "KittyX.Over == 'red shirt'", "images/KittyBJFace/Kitty_BJ_Over_RedShirt.png",
            "KittyX.Over == 'towel'", "images/KittyBJFace/Kitty_BJ_Over_Towel.png",
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                         
            #Spunk
            "'tits' not in KittyX.Spunk", Null(),
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
            "KittyX.Water or KittyX.Hair == 'wet'", "images/KittyBJFace/Kitty_BJ_HairBackWet.png", #AlphaMask("images/KittyBJFace/Kitty_BJ_HairBackWet.png", "Kitty_BJ_Backdrop"),
            "True", Null(),
            ),   
#        (0,0), ConditionSwitch(       #Legacy, the bellow version should do the same role                                                          
#            # Underface for sucking 
#            "Speed > 2 and Speed != 5", Null(),            
#            "KittyX.Water and KittyX.Blush", "images/KittyBJFace/Kitty_BJ_FaceClosed_Wet_Blush.png",    
#            "KittyX.Water", "images/KittyBJFace/Kitty_BJ_FaceClosed_Wet.png", 
#            "KittyX.Blush", "images/KittyBJFace/Kitty_BJ_FaceClosed_Blush.png",              
#            "True", "images/KittyBJFace/Kitty_BJ_FaceClosed.png"
#            ),   
#        (0,0), ConditionSwitch(                                                                 
#            # Underface for not sucking 
#            "Speed <= 2 or Speed == 5", Null(),   #"Speed <= 2 or Trigger != 'blow' or Speed == 5", Null(), 
#            "KittyX.Water and KittyX.Blush", "images/KittyBJFace/Kitty_BJ_FaceOpen_Wet_Blush.png",    
#            "KittyX.Water", "images/KittyBJFace/Kitty_BJ_FaceOpen_Wet.png", 
#            "KittyX.Blush", "images/KittyBJFace/Kitty_BJ_FaceOpen_Blush.png",              
#            "True", "images/KittyBJFace/Kitty_BJ_FaceOpen.png"
#            ),          
        (0,0), ConditionSwitch(
            # Basic Face layer
            "Speed <= 2 or Speed == 5 or not renpy.showing('Kitty_BJ_Animation')", ConditionSwitch( 
                    # If the animation isn't sucking, or if not in BJ pose                    
                    "KittyX.Water", ConditionSwitch( 
                            # If she's wet
                            "KittyX.Blush", "images/KittyBJFace/Kitty_BJ_FaceClosed_Wet_Blush.png",             
                            "True", "images/KittyBJFace/Kitty_BJ_FaceClosed_Wet.png", 
                            ),  
                    "KittyX.Blush", "images/KittyBJFace/Kitty_BJ_FaceClosed_Blush.png",              
                    "True", "images/KittyBJFace/Kitty_BJ_FaceClosed.png"
                    ), 
            #if it is in the open, sucking position
            "KittyX.Water", ConditionSwitch( 
                    # If she's wet
                    "KittyX.Blush", "images/KittyBJFace/Kitty_BJ_FaceOpen_Wet_Blush.png",              
                    "True", "images/KittyBJFace/Kitty_BJ_FaceOpen_Wet.png", 
                    ),  
            "KittyX.Blush", "images/KittyBJFace/Kitty_BJ_FaceOpen_Blush.png",             
            "True",  "images/KittyBJFace/Kitty_BJ_FaceOpen.png"
            ),    
        (0,0), ConditionSwitch(                                                                         
            #Mouth
            "Speed and renpy.showing('Kitty_BJ_Animation')", ConditionSwitch( 
                    # If in sucking position
                    "Speed == 1", "images/KittyBJFace/Kitty_BJ_Mouth_Tongue.png",  #licking
                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png", #sucking
                    "Speed == 4", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png", #deepthroat     
                    "Speed == 6", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png", #cumming      
                    "True", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png", #cumming     
                    ),  
            "Speed == 3 and renpy.showing('Kitty_TJ_Animation')", "images/KittyBJFace/Kitty_BJ_Mouth_Tongue.png",                        
            "Speed >= 5 and renpy.showing('Kitty_TJ_Animation')", "images/KittyBJFace/Kitty_BJ_Mouth_Kiss.png",
            "KittyX.Mouth == 'normal'", "images/KittyBJFace/Kitty_BJ_Mouth_Smile.png",
            "KittyX.Mouth == 'lipbite'", "images/KittyBJFace/Kitty_BJ_Mouth_Lipbite.png",
            "KittyX.Mouth == 'sucking'", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png",            
            "KittyX.Mouth == 'kiss'", "images/KittyBJFace/Kitty_BJ_Mouth_Kiss.png",
            "KittyX.Mouth == 'sad'", "images/KittyBJFace/Kitty_BJ_Mouth_Sad.png",
            "KittyX.Mouth == 'smile'", "images/KittyBJFace/Kitty_BJ_Mouth_Smile.png",            
            "KittyX.Mouth == 'grimace'", "images/KittyBJFace/Kitty_BJ_Mouth_Smile.png",
            "KittyX.Mouth == 'surprised'", "images/KittyBJFace/Kitty_BJ_Mouth_Surprised.png",          
            "KittyX.Mouth == 'tongue'", "images/KittyBJFace/Kitty_BJ_Mouth_Tongue.png",    
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
            "'mouth' not in KittyX.Spunk", Null(), 
            "Speed and renpy.showing('Kitty_BJ_Animation')", ConditionSwitch( 
                    # If in sucking position
                    "Speed == 1", "images/KittyBJFace/Kitty_BJ_Spunk_Tongue.png",  #licking
                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png", #sucking
                    "Speed == 4", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png", #deepthroat 
                    "True", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png", #cumming     
                    ),  
            "Speed >= 5 and renpy.showing('Kitty_TJ_Animation')", "images/KittyBJFace/Kitty_BJ_Spunk_Kiss.png",
            "KittyX.Mouth == 'normal'", "images/KittyBJFace/Kitty_BJ_Spunk_Smile.png",
            "KittyX.Mouth == 'lipbite'", "images/KittyBJFace/Kitty_BJ_Spunk_Lipbite.png",
            "KittyX.Mouth == 'kiss'", "images/KittyBJFace/Kitty_BJ_Spunk_Kiss.png",
            "KittyX.Mouth == 'sad'", "images/KittyBJFace/Kitty_BJ_Spunk_Kiss.png",
            "KittyX.Mouth == 'smile'", "images/KittyBJFace/Kitty_BJ_Spunk_Smile.png",
            "KittyX.Mouth == 'surprised'", "images/KittyBJFace/Kitty_BJ_Spunk_Surprised.png",
            "KittyX.Mouth == 'tongue'", "images/KittyBJFace/Kitty_BJ_Spunk_Tongue.png",
            "KittyX.Mouth == 'sucking'", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png", #fix add
            "True", Null(),
            ),       
        (0,0), ConditionSwitch(                                                                         
            #Brows
            "KittyX.Brows == 'normal'", "images/KittyBJFace/Kitty_BJ_Brows_Normal.png",
            "KittyX.Brows == 'angry'", "images/KittyBJFace/Kitty_BJ_Brows_Angry.png",
            "KittyX.Brows == 'sad'", "images/KittyBJFace/Kitty_BJ_Brows_Sad.png",
            "KittyX.Brows == 'surprised'", "images/KittyBJFace/Kitty_BJ_Brows_Surprised.png",        
            "KittyX.Brows == 'confused'", "images/KittyBJFace/Kitty_BJ_Brows_Confused.png",
            "True", "images/KittyBJFace/Kitty_BJ_Brows_Normal.png",
            ),
        (0,0), "Kitty BJ Blink",                                                                
            #Eyes
        (0,0), ConditionSwitch(                                                                 
            #cum on the face
            "'facial' in KittyX.Spunk", "images/KittyBJFace/Kitty_BJ_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                 
            #Hair overlay
            "KittyX.Water or KittyX.Hair == 'wet'", "images/KittyBJFace/Kitty_BJ_Hair_Wet.png",
            "KittyX.Hair == 'long'", "images/KittyBJFace/Kitty_BJ_Hair_Long.png",
            "KittyX.Hair == 'evo'", "images/KittyBJFace/Kitty_BJ_Hair_Evo.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                 
            #Hair water overlay
            "not KittyX.Water", Null(),            
            "Speed > 2", "images/KittyBJFace/Kitty_BJ_Wet_HeadOpen.png",         
            "True", "images/KittyBJFace/Kitty_BJ_Wet_HeadClosed.png",
            ),        
        (0,0), ConditionSwitch(                                                                 
            #cum on the hair
            "'hair' in KittyX.Spunk", "images/KittyBJFace/Kitty_BJ_Spunk_Hair.png",
            "True", Null(),
            ),
        )
    zoom 1.4
    anchor (0.5, 0.5)

image Kitty BJ Blink:                                                                           
        #eyeblinks
        ConditionSwitch(
            "KittyX.Eyes == 'normal'", "images/KittyBJFace/Kitty_BJ_Eyes_Normal.png",  
            "KittyX.Eyes == 'sexy'", "images/KittyBJFace/Kitty_BJ_Eyes_Sexy.png",  
            "KittyX.Eyes == 'closed'", "images/KittyBJFace/Kitty_BJ_Eyes_Closed.png",
            "KittyX.Eyes == 'surprised'", "images/KittyBJFace/Kitty_BJ_Eyes_Surprised.png",
            "KittyX.Eyes == 'side'", "images/KittyBJFace/Kitty_BJ_Eyes_Side.png",
            "KittyX.Eyes == 'stunned'", "images/KittyBJFace/Kitty_BJ_Eyes_Surprised.png",
            "KittyX.Eyes == 'down'", "images/KittyBJFace/Kitty_BJ_Eyes_Down.png",
            "KittyX.Eyes == 'manic'", "images/KittyBJFace/Kitty_BJ_Eyes_Surprised.png",
            "KittyX.Eyes == 'squint'", "images/KittyBJFace/Kitty_BJ_Eyes_Squint.png",
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
            "'mouth' not in KittyX.Spunk", Null(),  
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
        
    
#Head and Body Animations for Kitty's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
                                                               #BJ Launchers  
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Kitty_BJ_Launch(Line = 0):    # The sequence to launch the Kitty BJ animations  
    if renpy.showing("Kitty_BJ_Animation"):
            return
    
    call Kitty_Hide
    if Line == "L" or Line == "cum":
        show Kitty_Sprite at SpriteLoc(StageCenter) zorder KittyX.Layer:
            alpha 1
            ease 1 zoom 2.5 offset (150,80) 
        with dissolve
    else:
        show Kitty_Sprite at SpriteLoc(StageCenter) zorder KittyX.Layer:
            alpha 1
            zoom 2.5 offset (150,80) 
        with dissolve
        
    if Line == "L": 
            if Taboo: 
                if len(Present) >= 2:
                    if Present[0] != KittyX:
                            "[KittyX.Name] looks back at [Present[0].Name] to see if she's watching."
                    elif Present[1] != KittyX:
                            "[KittyX.Name] looks back at [Present[1].Name] to see if she's watching."
                else:
                            "[KittyX.Name] casually glances around to see if anyone can see her."
            if not KittyX.Blow:
                "[KittyX.Name] hesitantly kneels down and touches her mouth to your cock."
            else:
                "[KittyX.Name] kneels down and begins to suck on your cock."
            
    $ Speed = 0
    
    if Line != "cum":
        $ Trigger = "blow"
    
    show Kitty_Sprite zorder KittyX.Layer:
        alpha 0
    show Kitty_BJ_Animation zorder 150: 
        pos (645,510) 
    return
    
label Kitty_BJ_Reset: # The sequence to the Kitty animations from BJ to default
    if not renpy.showing("Kitty_BJ_Animation"):
            return
    call Kitty_Hide 
    $ Speed = 0
    
    show Kitty_Sprite at SpriteLoc(StageCenter) zorder KittyX.Layer:
        alpha 1
        zoom 2.5 offset (150,80) 
    with dissolve
    
    show Kitty_Sprite zorder KittyX.Layer:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)    
    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer:
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
            "Player.Sprite", ConditionSwitch(                                                               
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
#                "not renpy.showing('Kitty_TJ_Animation')", Null(),   # KittyX.TitsUp = 0
#                "KittyX.Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Bra_Sports_TJU.png",
#                "True", Null(),
#                ) 
#    contains:
#            # Chest clothing layer
#        ConditionSwitch(    
#            "not KittyX.Chest or renpy.showing('Kitty_TJ_Animation')", Null(),   # KittyX.TitsUp = 0
#            "KittyX.Chest == 'corset'", "images/KittySex/Kitty_Sex_Bra_Corset_Up.png",   # KittyX.TitsUp = 1
#            "KittyX.Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Bra_Sports_Up.png",   # KittyX.TitsUp = 1
#            "KittyX.Chest == 'lace bra'", "images/KittySex/Kitty_Sex_Bra_Lace_Up.png",   # KittyX.TitsUp = 1
#            "True", Null(),   # KittyX.TitsUp = 0
#            )
#    contains:
#            # Over clothing layer
#        ConditionSwitch(   
#            "KittyX.Over == 'jacket'", ConditionSwitch(   
#                    #if it's the ring pericings                       
#                    "renpy.showing('Kitty_TJ_Animation')", Null(),
##                    "renpy.showing('Kitty_TJ_Animation')", "images/KittySex/Kitty_Sex_Jacket_Down.png",
#                    "KittyX.Chest == 'corset'", "images/KittySex/Kitty_Sex_Jacket_Up.png",   # KittyX.TitsUp = 1
#                    "KittyX.Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Jacket_Up.png",   # KittyX.TitsUp = 1
#                    "KittyX.Chest == 'lace bra'", "images/KittySex/Kitty_Sex_Jacket_Up.png",   # KittyX.TitsUp = 1
#                    "True", "images/KittySex/Kitty_Sex_Jacket_Down.png",   # KittyX.TitsUp = 0
#                    ),                
#            "KittyX.Over == 'nighty'", ConditionSwitch(
#                    #if she has the nighty on     
#                    "renpy.showing('Kitty_TJ_Animation')", Null(),
#                    "KittyX.Chest in ('corset', 'lace bra', 'sports bra')", "images/KittySex/Kitty_Sex_Nighty_Up.png",  
#                    "True", "images/KittySex/Kitty_Sex_Nighty_Down.png", 
#                    ),    
#            "True", Null(), 
#            )
#    contains:
#            # spunk on tits
#            ConditionSwitch(    
#                "'tits' not in KittyX.Spunk", Null(),
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
            "Player.Sprite and Speed", "images/KittyBJFace/Kitty_TJ_Tits_Smooshed.png", 
            "True", "images/KittyBJFace/Kitty_TJ_Tits.png",
            )
#    contains:
#            # piercings
#        ConditionSwitch(   
#            "not KittyX.Pierce", Null(),
#            "KittyX.Pierce == 'barbell'", ConditionSwitch(   
#                    #if it's the ring pericings   
##                    "KittyX.Chest in ('corset', 'lace bra', 'sports bra')", Null(),  
#                    "True", "images/KittySex/Kitty_Pierce_Barbell_Tits_T.png", 
#                    ),    
#            "KittyX.Pierce == 'ring'", ConditionSwitch(   
#                    #if it's the ring pericings   
##                    "KittyX.Chest in ('corset', 'lace bra', 'sports bra')", Null(),  
#                    "True", "images/KittySex/Kitty_Pierce_Ring_Tits_T.png", 
#                    ),                    
#            "True", Null(), 
#            )
#    contains:
#            #chest clothing layer
#        ConditionSwitch(    
#            "not KittyX.Chest", Null(),   # KittyX.TitsUp = 0
#            "KittyX.Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Bra_Sports_TJ.png",   # KittyX.TitsUp = 1
#            "KittyX.Chest == 'lace bra'", "images/KittySex/Kitty_Sex_Bra_Lace_TJ.png",   # KittyX.TitsUp = 1
#            "True", Null(),   # KittyX.TitsUp = 0
#            )
#    contains:
#            # piercings over clothes
#        ConditionSwitch(   
#            "not KittyX.Pierce or not KittyX.Chest", Null(),
#            "KittyX.Pierce == 'barbell'", ConditionSwitch(   
#                    #if it's the ring pericings   
#                    "KittyX.Chest in ('corset', 'lace bra', 'sports bra')", "images/KittySex/Kitty_Pierce_Barbell_Tits_TC.png", 
#                    "True", Null(),
#                    ),    
#            "KittyX.Pierce == 'ring'", ConditionSwitch(   
#                    #if it's the ring pericings   
#                    "KittyX.Chest in ('corset', 'lace bra', 'sports bra')", "images/KittySex/Kitty_Pierce_Ring_Tits_TC.png", 
#                    "True", Null(),
#                    ),                    
#            "True", Null(), 
#            )
#    contains:
#            # spunk on tits
#        ConditionSwitch(    
#                "'tits' in KittyX.Spunk", "images/KittySex/Kitty_Spunk_Titjob_Over.png",
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
                    "Player.Sprite", "Blowcock",
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
                    "Player.Sprite", AlphaMask("Blowcock", "Kitty_TJ_Mask_1"), 
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
                    "Player.Sprite", AlphaMask("Blowcock", "Kitty_TJ_Mask_2"), 
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
                    "Player.Sprite", AlphaMask("Blowcock", "Kitty_TJ_Mask_3"), 
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
    #                "Player.Sprite", AlphaMask("Kitty_Mega_Mask", "Kitty_TJ_Mask_5"), 
                    "Player.Sprite", AlphaMask("Blowcock", "Kitty_TJ_Mask_5"), 
    #                "Player.Sprite", AlphaMask("Blowcock", "Kitty_Mega_Mask"), 
                    "True", Null(),
                    )      
                subpixel True
                pos (665,500) #bottom #150
                anchor (0.5,0.5)
                zoom 0.4   
                    
    #    contains:
    #            #zero's cock
    #            ConditionSwitch(    
    #                "Player.Sprite", "Blowcock",
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
    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer:
        alpha 1
        ease 1 zoom 2 xpos 700 yoffset 50 #offset (-100,50) 
    if Line == "L" and Taboo: 
                if len(Present) >= 2:
                    if Present[0] != KittyX:
                            "[KittyX.Name] looks back at [Present[0].Name] to see if she's watching."
                    elif Present[1] != KittyX:
                            "[KittyX.Name] looks back at [Present[1].Name] to see if she's watching."
                else:
                            "[KittyX.Name] casually glances around to see if anyone can see her."
    if KittyX.Chest and KittyX.Over:
        "She throws off her [KittyX.Over] and her [KittyX.Chest]."                
    elif KittyX.Over:
        "She throws off her [KittyX.Over], baring her breasts underneath."
    elif KittyX.Chest:
        "She tugs off her [KittyX.Chest] and throws it aside."
    $ KittyX.Over = 0
    $ KittyX.Chest = 0
    $ KittyX.ArmPose = 0
    call Kitty_First_Topless      #restore if topless   
    if Line == "L":
            if not KittyX.Tit:
                "She hesitantly presses your cock against her chest."
            else:
                "She squeezes her breasts around your cock."
           
     
    show blackscreen onlayer black with dissolve   
    show Kitty_Sprite zorder KittyX.Layer:
        alpha 0
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "titjob"
    show Kitty_TJ_Animation zorder 150 
    $ Player.Sprite = 1
    hide blackscreen onlayer black with dissolve
    return
    
label Kitty_TJ_Reset: # The sequence to the Kitty animations from Titfuck to default
    if not renpy.showing("Kitty_TJ_Animation"):
            return
    call Kitty_Hide 
    $ Player.Sprite = 0
    
    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer:
            zoom 2 xpos 550 yoffset 50 #offset (-100,50)  #zoom 2 offset (-100,50)
    show Kitty_Sprite zorder KittyX.Layer:
            alpha 1
            ease 1 zoom 1.5 xpos 700 yoffset 50
            pause .5
            ease .5 zoom 1 xpos KittyX.SpriteLoc yoffset 0   
    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer:
            alpha 1
            zoom 1 offset (0,0) xpos KittyX.SpriteLoc        
#    "Kitty pulls back"
    return
            
# End Kitty TJ Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /






# Start Kitty Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Kitty Handjob element //////////////////////////////////////////////////////////////////////                                         Core Kitty HJ element

#image Zero_Handcock:
#    contains:
#        ConditionSwitch(    # Zero cock sucking
#            "Player.Color == 'pink'", "images/RogueBJFace/handcock_P.png",
#            "Player.Color == 'brown'", "images/RogueBJFace/handcock_B.png",             
#            "Player.Color == 'green'", "images/RogueBJFace/handcock_G.png", 
#            "Player.Color != 'pink'", Null(),
#            ),  
#    anchor (0.5,1.0)  #1.0
#    pos (200,400)#(200,400)
        
image Kitty_Hand_Under:
    "images/KittySprite/handkitty2.png"
    anchor (0.5,0.5)
    pos (0,0)
    
    
image Kitty_Hand_Over:
    "images/KittySprite/handkitty1.png"    
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
        show Kitty_Sprite at SpriteLoc(StageRight) zorder KittyX.Layer:
            alpha 1
            ease 1 zoom 1.7 offset (-50,200)
    else:     
        show Kitty_Sprite at SpriteLoc(StageRight) zorder KittyX.Layer:
            alpha 1
            ease 1 zoom 1.7 offset (-50,200)
        with dissolve
   
    if Line == "L":
            if Taboo: 
                if len(Present) >= 2:
                    if Present[0] != KittyX:
                            "[KittyX.Name] looks back at [Present[0].Name] to see if she's watching."
                    elif Present[1] != KittyX:
                            "[KittyX.Name] looks back at [Present[1].Name] to see if she's watching."
                else:
                            "[KittyX.Name] casually glances around to see if anyone can see her."
            
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
    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer:
            alpha 1
            zoom 1.7 offset (-50,200)
    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer:
            alpha 1
            ease 1 zoom 1.5 offset (-150,50)
            pause .5
            ease .5 zoom 1 offset (0,0)    
    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer:
            alpha 1
            zoom 1 offset (0,0)  
    return
    

label Kitty_Kissing_Launch(T = Trigger):    
    call Kitty_Hide
    $ Trigger = T
    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer
    show Kitty_Sprite at SpriteLoc(StageCenter):
            ease 0.5 offset (0,0) zoom 2 alpha 1
    return
    
label Kitty_Kissing_Smooch:   
    $ KittyX.FaceChange("kiss")
    show Kitty_Sprite at SpriteLoc(StageCenter) zorder KittyX.Layer:
        ease 0.5 xpos StageCenter offset (0,0) zoom 2 alpha 1
        pause 1
        ease 0.5 xpos KittyX.SpriteLoc zoom 1   
    $ KittyX.FaceChange("sexy")
    return
                
label Kitty_Breasts_Launch(T = Trigger):    
    call Kitty_Hide
    $ Trigger = T
    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer:
        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1 # pos (900,-50)
    return
        
label Kitty_Pussy_Launch(T = Trigger):
    call Kitty_Hide    
    $ Trigger = T
    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer:
        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
    return
        
label Kitty_Pos_Reset(Pose = 0): 
    if KittyX.Loc != bg_current:
            return
    call Kitty_Hide 
    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer:
        ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1 
    show Kitty_Sprite zorder KittyX.Layer:
        offset (0,0) 
        anchor (0.5, 0.0)
        zoom 1   
        xzoom 1 
        yzoom 1
        alpha 1
        pos (KittyX.SpriteLoc,50)
    $ Trigger = Pose
    return
    
label Kitty_Hide(Sprite=0):
        if renpy.showing("Kitty_SexSprite"):
            call Kitty_Sex_Reset
        hide Kitty_SexSprite
        hide Kitty_HJ_Animation
        hide Kitty_BJ_Animation
        hide Kitty_TJ_Animation 
        if Sprite:
                hide Kitty_Sprite    
        return

label Kitty_ThreewayBreasts_Launch:    
        show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer:
    #      ease 0.5 pos (800,200) zoom 1.3
            ease 0.5 pos (700,200) xzoom -1.5 yzoom 1.5
        $ KittyX.ArmPose = 1
        return


# End Kitty Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    
    
    
    
    
    
# Start Kitty Fondling Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    
    
# Interface items //////////////////////////////////////////////////////////////////////////////

image GropeLeftBreast_Kitty:    
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

image GropeRightBreast_Kitty:    
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
image LickRightBreast_Kitty:   
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
            
image LickLeftBreast_Kitty:   
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

image GropeThigh_Kitty: 
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

image GropePussy_Kitty: 
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

image FingerPussy_Kitty: 
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
            
image Lickpussy_Kitty:   
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

image VibratorRightBreast_Kitty: 
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

image VibratorLeftBreast_Kitty: 
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
            
image VibratorPussy_Kitty: 
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

image VibratorAnal_Kitty: 
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
            
image VibratorPussyInsert_Kitty: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_Kitty: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0



#Lesbian action animations.
image GirlGropeLeftBreast_Kitty:  
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

image GirlGropeRightBreast_Kitty:    
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

image GirlGropeThigh_Kitty: 
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

image GirlGropePussy_Kitty: 
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

image GirlFingerPussy_Kitty: 
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
            