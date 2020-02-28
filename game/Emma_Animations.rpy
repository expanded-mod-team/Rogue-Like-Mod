# Basic character Sprites
image Emma_Sprite:
    LiveComposite(
        (402,965), 
#        (55,0), ConditionSwitch(                                                                         #hair back temporary
#            "not EmmaX.Hair", Null(),
#            "EmmaX.Hair == 'wet' or EmmaX.Water", "images/EmmaSprite/EmmaSprite_Head_HairBackWet.png",
#            "True", Null(),        
#            ),   
        (0,0), ConditionSwitch(                                                                         
            #cape layer       
            "EmmaX.Uptop or EmmaX.Over == 'jacket' or EmmaX.Chest != 'corset'", Null(),  
            "EmmaX.ArmPose == 2", "images/EmmaSprite/EmmaSprite_Cape2.png",              
            "True", "images/EmmaSprite/EmmaSprite_Cape1.png",   
            ), 
        (0,0), ConditionSwitch(                                                                         
            #Overshirt back layer       
            "EmmaX.Over and EmmaX.Uptop and EmmaX.Over == 'jacket'", "images/EmmaSprite/EmmaSprite_Jacket_Back.png",  
            "True", Null(), 
            ), 
        (0,0), ConditionSwitch(
            #hair back 
            "not EmmaX.Hair", Null(),
            "EmmaX.Hair == 'wet' or EmmaX.Water", "images/EmmaSprite/EmmaSprite_HairbackWet.png",
            "EmmaX.Hair", "images/EmmaSprite/EmmaSprite_Hairback.png",   
            "True", Null(),        
            ),     
        (0,0), ConditionSwitch(
            #nighty underlayer
            "EmmaX.Over == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_Under.png", 
            "True", Null(),              
            ), 
        (0,0), ConditionSwitch(            
            #panties down back 
            "not EmmaX.Panties or not EmmaX.PantiesDown or (EmmaX.Legs == 'pants' and not EmmaX.Upskirt)", Null(), 
            "EmmaX.Panties == 'sports panties'", "images/EmmaSprite/EmmaSprite_Panties_Sports_DownBack.png",   
            "EmmaX.Panties == 'bikini bottoms'", "images/EmmaSprite/EmmaSprite_Panties_Bikini_DownBack.png",  
            "True", "images/EmmaSprite/EmmaSprite_Panties_DownBack.png",   
            ),  
        (0,0), ConditionSwitch(
            #legs/torso 
            "EmmaX.ArmPose == 2", "images/EmmaSprite/EmmaSprite_Legs_Arms2.png",   
            "True", "images/EmmaSprite/EmmaSprite_Legs_Arms1.png", #if EmmaX.Arms == 1 
            ),     
        
        (215,540), ConditionSwitch(                                                                         
            #Personal Wetness            
            "not EmmaX.Wet", Null(),
            "EmmaX.Legs == 'pants' and not EmmaX.Upskirt", Null(),   
            "EmmaX.Panties and not EmmaX.PantiesDown and EmmaX.Wet <= 1", Null(),                   
            "EmmaX.Wet == 1", ConditionSwitch( #Wet = 1
                    "EmmaX.Panties and EmmaX.PantiesDown", AlphaMask("Wet_Drip","Emma_Drip_MaskP"),  
                    "EmmaX.Legs == 'pants'", AlphaMask("Wet_Drip","Emma_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip","Emma_Drip_Mask"), #only plays if nothing is in the way
                    ),
            "True", ConditionSwitch( #Wet = 2+
                    "EmmaX.Panties and EmmaX.PantiesDown", AlphaMask("Wet_Drip2","Emma_Drip_MaskP"), #"Wet_Drip2",# 
                    "EmmaX.Legs == 'pants'", AlphaMask("Wet_Drip2","Emma_Drip_MaskP"),
                    "EmmaX.Panties", AlphaMask("Wet_Drip","Emma_Drip_Mask"), #"Wet_Drip2",# 
                    "True", AlphaMask("Wet_Drip2","Emma_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (0,0), ConditionSwitch(
            #Personal Wetness            
            "not EmmaX.Wet", Null(),
            "EmmaX.Legs and EmmaX.Wet <= 1", Null(),
            "EmmaX.Legs", "images/EmmaSprite/EmmaSprite_Wet.png",
            "EmmaX.Wet == 1", "images/EmmaSprite/EmmaSprite_Wet.png",
            "True", "images/EmmaSprite/EmmaSprite_Wet.png",       #EmmaX.Wet >1
            ),     
        
        (215,540), ConditionSwitch(                                                                         
            #Spunk nethers        
            "'in' not in EmmaX.Spunk and 'anal' not in EmmaX.Spunk", Null(),
            "EmmaX.Legs == 'pants' and not EmmaX.Upskirt", Null(),   
            "True", ConditionSwitch( #Wet = 2+
                    "EmmaX.Panties and EmmaX.PantiesDown", AlphaMask("Spunk_Drip","Emma_Drip_MaskP"), #"Wet_Drip2",# 
                    "EmmaX.Legs == 'pants'", AlphaMask("Spunk_Drip","Emma_Drip_MaskP"),
                    "True", AlphaMask("Spunk_Drip","Emma_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),    
        (0,0), ConditionSwitch(
            #pubes 
            "EmmaX.Pubes", "images/EmmaSprite/EmmaSprite_Pubes.png",   
            "True", Null(),        
            ),      
        (0,0), ConditionSwitch(
            #nude lower piercings        
            "not EmmaX.Pierce", Null(),  
            "EmmaX.Panties and not EmmaX.PantiesDown", Null(), 
            "EmmaX.Legs != 'skirt' and EmmaX.Legs and not EmmaX.Upskirt", Null(), #skirt if wearing a skirt
            "EmmaX.Pierce == 'barbell'", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_Barbell.png",  
            "EmmaX.Pierce == 'ring'", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_Ring.png",  
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(
            #Water effect 
            "EmmaX.Water", "images/EmmaSprite/EmmaSprite_Water_Legs.png",   
            "True", Null(),        
            ),               
        (0,0), ConditionSwitch( 
            # stockings   
            "renpy.showing('Emma_FJ_Animation')", Null(),                    
            "EmmaX.Hose == 'stockings'", "images/EmmaSprite/EmmaSprite_Stockings.png",   
            "EmmaX.Hose == 'stockings and garterbelt'", "images/EmmaSprite/EmmaSprite_StockingsGarter.png",   
            "EmmaX.Hose == 'garterbelt'", "images/EmmaSprite/EmmaSprite_Garter.png",   
            "True", Null(),        
            ),                  
        (0,0), ConditionSwitch(
            #boots    
            "EmmaX.PantiesDown and EmmaX.Acc == 'thigh boots' and (EmmaX.Legs == 'skirt' or not EmmaX.Legs)", "images/EmmaSprite/EmmaSprite_Boots.png",    
            "True", Null(), 
            ),     
        (0,0), ConditionSwitch(
            #panties down if not wearing pants
            "not EmmaX.Panties or not EmmaX.PantiesDown or (EmmaX.Legs == 'pants' and not EmmaX.Upskirt)", Null(),   
            "EmmaX.Panties == 'sports panties' and EmmaX.Wet", "images/EmmaSprite/EmmaSprite_Panties_Sports_DownWet.png",  
            "EmmaX.Panties == 'sports panties'", "images/EmmaSprite/EmmaSprite_Panties_Sports_Down.png",              
            "EmmaX.Panties == 'lace panties' and EmmaX.Wet", "images/EmmaSprite/EmmaSprite_Panties_Lace_DownWet.png",  
            "EmmaX.Panties == 'lace panties'", "images/EmmaSprite/EmmaSprite_Panties_Lace_Down.png",   
            "EmmaX.Panties == 'bikini bottoms'", "images/EmmaSprite/EmmaSprite_Panties_Bikini_Down.png",  
#            "EmmaX.Wet", "images/EmmaSprite/EmmaSprite_Panties_DownWet.png",  
            "True", "images/EmmaSprite/EmmaSprite_Panties_Down.png",  
            ),                
        (0,0), ConditionSwitch(
            #panties up
            "EmmaX.PantiesDown or not EmmaX.Panties", Null(),   
#            "EmmaX.Panties == 'sports panties' and EmmaX.Wet", "images/EmmaSprite/EmmaSprite_Panties_Sports_Wet.png",     
            "EmmaX.Panties == 'sports panties'", "images/EmmaSprite/EmmaSprite_Panties_Sports.png",  
            "EmmaX.Panties == 'lace panties' and EmmaX.Wet", "images/EmmaSprite/EmmaSprite_Panties_Lace_Wet.png", 
            "EmmaX.Panties == 'lace panties'", "images/EmmaSprite/EmmaSprite_Panties_Lace.png",  
            "EmmaX.Panties == 'bikini bottoms'", "images/EmmaSprite/EmmaSprite_Panties_Bikini.png",  
#            "EmmaX.Wet", "images/EmmaSprite/EmmaSprite_Panties_Wet.png", #readd when sprite works 
            "True", "images/EmmaSprite/EmmaSprite_Panties.png",  
            ),              
        (0,0), ConditionSwitch(
            # pantyhose
            "renpy.showing('Emma_FJ_Animation')", Null(),  
            "EmmaX.Hose == 'pantyhose' and not EmmaX.PantiesDown", "images/EmmaSprite/EmmaSprite_Hose.png",   
            "True", Null(),        
            ),    
        (0,0), ConditionSwitch(
            #pussy spunk 
            "EmmaX.Legs and EmmaX.Legs != 'skirt' and not EmmaX.Upskirt", Null(),
            "'in' in EmmaX.Spunk or 'anal' in EmmaX.Spunk", "images/EmmaSprite/EmmaSprite_Spunk_Pussy.png",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(
            #pants    
            "not EmmaX.Legs", Null(),
            "EmmaX.Upskirt", ConditionSwitch(                   
                        #if the skirt's up or pants down 
                        "EmmaX.Legs == 'skirt'", "images/EmmaSprite/EmmaSprite_SkirtUp.png", 
                        "EmmaX.Acc", Null(),
                        "EmmaX.Legs == 'pants'", "images/EmmaSprite/EmmaSprite_Pants_Down.png",   
                        "EmmaX.Legs == 'yoga pants'", "images/EmmaSprite/EmmaSprite_Pants_Yoga_Down.png",   
                        "True", Null(),
                        ),                    
            "True", ConditionSwitch(                
                    #if it's the ring pericings
                    "EmmaX.Wet", ConditionSwitch(   
                        #if she's not wet
                        "EmmaX.Legs == 'pants'", "images/EmmaSprite/EmmaSprite_Pants.png",   
                        "EmmaX.Legs == 'yoga pants'", "images/EmmaSprite/EmmaSprite_Pants_YogaWet.png",       
                        "EmmaX.Legs == 'skirt'", "images/EmmaSprite/EmmaSprite_Skirt.png", 
                        "True", Null(),
                        ),
                    "True", ConditionSwitch(   
                        #if she's wet
                        "EmmaX.Legs == 'pants'", "images/EmmaSprite/EmmaSprite_Pants.png",   
                        "EmmaX.Legs == 'yoga pants'", "images/EmmaSprite/EmmaSprite_Pants_Yoga.png",       
                        "EmmaX.Legs == 'skirt'", "images/EmmaSprite/EmmaSprite_Skirt.png", 
                        "True", Null(),
                        ),                    
                    ),    
            ),                   
        (0,0), ConditionSwitch(
            #boots    
            "not EmmaX.PantiesDown and EmmaX.Acc == 'thigh boots'", "images/EmmaSprite/EmmaSprite_Boots.png",    
            "True", Null(), 
            ),     
        (0,0), ConditionSwitch(
            #clothed lower piercings         
            "EmmaX.Legs == 'skirt'", Null(),
            "EmmaX.Pierce == 'barbell'", ConditionSwitch(   
                    #if it's the barbell pericings 
                    "EmmaX.Legs and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_BarOut.png",  
                    "EmmaX.Panties and not EmmaX.PantiesDown", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_BarOut.png", 
                    "True", Null(),
                    ),    
            "EmmaX.Pierce == 'ring'", ConditionSwitch(   
                    #if it's the ring pericings
                    "EmmaX.Legs and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_RingOut.png",  
                    "EmmaX.Panties and not EmmaX.PantiesDown", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_RingOut.png", 
                    "True", Null(),
                    ),
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(
            #Chest underlayer
            "EmmaX.Chest == 'sports bra' and not EmmaX.Uptop", "images/EmmaSprite/EmmaSprite_Bra_Sports_Under.png",   
            "EmmaX.Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Bra_Lace_Under.png",   
            "EmmaX.Chest == 'corset'", "images/EmmaSprite/EmmaSprite_CorsetUnder.png",   
            "EmmaX.Chest == 'bikini top'", "images/EmmaSprite/EmmaSprite_Bra_Bikini_Under.png",   
            "True", Null(),              
            ), 
        (0,0), ConditionSwitch(
            #Over underlayer
            "EmmaX.Over == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_Under.png", 
            "EmmaX.Over == 'towel'", "images/EmmaSprite/EmmaSprite_Towel_Under.png",   
            "True", Null(),              
            ),          
        (0,0), ConditionSwitch(
            #belly spunk 
            "'belly' in EmmaX.Spunk", "images/EmmaSprite/EmmaSprite_Spunk_Belly.png",
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(
            #arms 
            "EmmaX.ArmPose == 2", "images/EmmaSprite/EmmaSprite_Arms2.png",         # one hand up
            "True", "images/EmmaSprite/EmmaSprite_Arms1.png", #if EmmaX.Arms == 1   # Crossed        
            ),  
        (0,0), ConditionSwitch(
            #Water effect on arms
            "not EmmaX.Water", Null(),             
            "EmmaX.ArmPose == 1", "images/EmmaSprite/EmmaSprite_Water_Arms1.png",   
            "True", "images/EmmaSprite/EmmaSprite_Water_Arms2.png", #if EmmaX.Arms == 1      
            ), 
        (0,0), ConditionSwitch(
            #gloves 
            "not EmmaX.Arms", Null(),  
            "EmmaX.ArmPose == 2", "images/EmmaSprite/EmmaSprite_Gloves_Arms2.png",   
            "True", "images/EmmaSprite/EmmaSprite_Gloves_Arms1.png", #if EmmaX.Arms == 1         
            ),   
        
        (0,0), ConditionSwitch(                                                                         
            # jacket arms in "up" pose  
            "not EmmaX.Uptop or EmmaX.Over != 'jacket'", Null(),  
            "EmmaX.ArmPose == 2", "images/EmmaSprite/EmmaSprite_Jacket_2Arm_Up.png",              
            "True", "images/EmmaSprite/EmmaSprite_Jacket_1Arm_Up.png",   
            ), 
        (0,0), ConditionSwitch(
            #tits
            "EmmaX.ArmPose == 1", "images/EmmaSprite/EmmaSprite_TitsUp.png",   # EmmaX.TitsUp = 1
            "EmmaX.Chest in ('corset','lace bra','sports bra','bikini top')", "images/EmmaSprite/EmmaSprite_TitsUp.png",   # EmmaX.TitsUp = 1
            "True", "images/EmmaSprite/EmmaSprite_TitsDown.png",   # EmmaX.TitsUp = 0
            ), 
        (0,0), ConditionSwitch(
            #nude peircings      
            #something about this entry makes all subsequent entries mis-aligned
            "not EmmaX.Pierce", Null(),  
            "EmmaX.Pierce == 'barbell'", ConditionSwitch(   
                    #if it's the barbell pericings
                    "EmmaX.ArmPose == 1", "images/EmmaSprite/EmmaSprite_Pierce_Up_Barbell.png",                     
                    "EmmaX.Chest in ('corset','lace bra','sports bra','bikini top')", "images/EmmaSprite/EmmaSprite_Pierce_Up_Barbell.png",   
#                    "EmmaX.Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_Barbell.png",    
#                    "EmmaX.Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_Barbell.png",  
                    "True", "images/EmmaSprite/EmmaSprite_Pierce_Down_Barbell.png",        
                    ),                        
            "EmmaX.Pierce == 'ring'", ConditionSwitch(                      
                    #if it's the ring pericings                                 
                    "EmmaX.ArmPose == 1", "images/EmmaSprite/EmmaSprite_Pierce_Up_Ring.png", 
                    "EmmaX.Chest in ('corset','lace bra','sports bra','bikini top')", "images/EmmaSprite/EmmaSprite_Pierce_Up_Ring.png",                          
#                    "EmmaX.Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_Ring.png", 
#                    "EmmaX.Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_Ring.png", 
                    "True", "images/EmmaSprite/EmmaSprite_Pierce_Down_Ring.png", 
                    ),       
            "True", Null(),  
            ),    
        (0,0), ConditionSwitch(                          
            #neck
            "EmmaX.Neck == 'choker'", "images/EmmaSprite/EmmaSprite_Neck_Choker.png",       
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(
            #Water effect 
            "not EmmaX.Water", Null(),             
            "EmmaX.ArmPose == 1 or EmmaX.Chest == 'corset'", "images/EmmaSprite/EmmaSprite_Water_TitsUp.png",  
            "True", "images/EmmaSprite/EmmaSprite_Water_TitsDown.png", #if EmmaX.Arms == 1      
            ), 
        (0,0), ConditionSwitch(                                                                         #Chest layer
            "EmmaX.Uptop and EmmaX.Chest", ConditionSwitch(   
                            #if her top is up. . .
                            "EmmaX.Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Bra_Sports_Up.png",   
                            "EmmaX.Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Bra_Lace_Up.png",   
                            "EmmaX.Chest == 'bikini top'", "images/EmmaSprite/EmmaSprite_Bra_Bikini_Up.png",      
                            "EmmaX.Chest == 'corset'", "images/EmmaSprite/EmmaSprite_CorsetTits_Up.png",  
                            "True", Null(), 
                            ),    
            "EmmaX.Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Bra_Sports.png",   
            "EmmaX.Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Bra_Lace.png",   
            "EmmaX.Chest == 'bikini top'", "images/EmmaSprite/EmmaSprite_Bra_Bikini.png",   
            "EmmaX.Chest == 'corset' and EmmaX.Over", "images/EmmaSprite/EmmaSprite_CorsetTitsX.png",   
            "EmmaX.Chest == 'corset'", "images/EmmaSprite/EmmaSprite_CorsetTits.png",   
            "True", Null(),              
            ),       
#        (0,0), ConditionSwitch(                                                                         #soap
#            "EmmaX.Water == 3", "images/EmmaSprite/Emma_body_wet3.png",
#            "True", Null(),                 
#            ),
        (0,0), ConditionSwitch(                                                                         #cape layer       
            "EmmaX.Uptop or EmmaX.Over == 'jacket' or EmmaX.Chest != 'corset'", Null(),  
            "EmmaX.ArmPose == 2", "images/EmmaSprite/EmmaSprite_Cape2.png",              
            "True", "images/EmmaSprite/EmmaSprite_Cape1.png",   
            ), 
        (0,0), ConditionSwitch(                                                                         #Overshirt layer       
            "not EmmaX.Over", Null(),  
            "EmmaX.ArmPose == 2", ConditionSwitch(   
                    #if her arms are down, allowing her breasts to sink                    
                    "EmmaX.Uptop", ConditionSwitch(   
                                    "EmmaX.Chest in ('corset','lace bra','sports bra','bikini top')", ConditionSwitch(   
                                            #If she's wearing a supporting bra. . .
                                            "EmmaX.Over == 'jacket'", "images/EmmaSprite/EmmaSprite_Jacket_2Up_Up.png",  
                                            "EmmaX.Over == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_Up2_Up.png",   
                                            "True", Null(), 
                                            ),  
                                    #if she's not wearing a supporting bra. . .
                                    "EmmaX.Over == 'jacket'", "images/EmmaSprite/EmmaSprite_Jacket_2Down_Up.png",  
                                    "EmmaX.Over == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_Up2_Up.png", 
                                    "True", Null(), 
                                    ),    
                    #if not Uptop. . .
                    "EmmaX.Chest in ('corset','lace bra','sports bra','bikini top')", ConditionSwitch(   
                            #If she's wearing a supporting bra. . .
                            "EmmaX.Over == 'jacket'", "images/EmmaSprite/EmmaSprite_Jacket_2Up.png",  
                            "EmmaX.Over == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_2Up.png",      
                            "EmmaX.Over == 'towel'", "images/EmmaSprite/EmmaSprite_Towel_Up2.png",  
                            "True", Null(), 
                            ),  
                    #if she's not wearing a supporting bra. . .
                    "EmmaX.Over == 'jacket'", "images/EmmaSprite/EmmaSprite_Jacket_2Down.png",  
                    "EmmaX.Over == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_2Down.png",      
                    "EmmaX.Over == 'towel'", "images/EmmaSprite/EmmaSprite_Towel_Down2.png",  
                    "True", Null(), 
                    ),   
            #if her arms are up, preventng her breasts from sinking
            "EmmaX.Uptop", ConditionSwitch(   
                            #if her top is up. . .
                            "EmmaX.Over == 'jacket'", "images/EmmaSprite/EmmaSprite_Jacket_1Up_Up.png",  
                            "EmmaX.Over == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_Up1_Up.png",   
                            "True", Null(), 
                            ),    
            #if her top is not up. . .
            "EmmaX.Over == 'jacket'", "images/EmmaSprite/EmmaSprite_Jacket_1Up.png",  
            "EmmaX.Over == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_1Up.png",      
            "EmmaX.Over == 'towel'", "images/EmmaSprite/EmmaSprite_Towel_Up1.png",               
            "True", Null(), 
            ), 
        (0,0), ConditionSwitch(                                                                         #clothed peircings        
            "not EmmaX.Pierce or EmmaX.Uptop or (not EmmaX.Over and not EmmaX.Chest)", Null(),  
            "EmmaX.Pierce == 'barbell'", ConditionSwitch(   
                    #if it's the barbell pericings
                    "EmmaX.ArmPose == 1", "images/EmmaSprite/EmmaSprite_Pierce_Up_BarOut.png",  
                    "EmmaX.Chest in ('corset','lace bra','sports bra','bikini top')", "images/EmmaSprite/EmmaSprite_Pierce_Up_BarOut.png",   
#                    "EmmaX.Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_BarOut.png",    
#                    "EmmaX.Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_BarOut.png",  
                    "True", "images/EmmaSprite/EmmaSprite_Pierce_Down_BarOut.png", 
                    ),    
            "EmmaX.Pierce == 'ring'", ConditionSwitch(   
                    #if it's the ring pericings
                    "EmmaX.ArmPose == 1", "images/EmmaSprite/EmmaSprite_Pierce_Up_RingOut.png",  
                    "EmmaX.Chest in ('corset','lace bra','sports bra','bikini top')", "images/EmmaSprite/EmmaSprite_Pierce_Up_RingOut.png",   
#                    "EmmaX.Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_RingOut.png",    
#                    "EmmaX.Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_RingOut.png",  
                    "True", "images/EmmaSprite/EmmaSprite_Pierce_Down_RingOut.png", 
                    ),                 
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(
            #breast spunk      
            "'tits' in EmmaX.Spunk", ConditionSwitch(   
                    #if it's the barbell pericings
                    "EmmaX.ArmPose == 1", "images/EmmaSprite/EmmaSprite_Spunk_TitsU.png",                     
                    "EmmaX.Chest == 'corset'", "images/EmmaSprite/EmmaSprite_Spunk_TitsU.png",   
                    "EmmaX.Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Spunk_TitsU.png",    
                    "EmmaX.Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Spunk_TitsU.png",  
                    "True", "images/EmmaSprite/EmmaSprite_Spunk_TitsD.png",        
                    ),       
            "True", Null(),  
            ),   
        (55,0), "EmmaSprite_Head", #Head
        (0,0), ConditionSwitch( 
            #hand spunk 
            "EmmaX.ArmPose != 2 or 'hand' not in EmmaX.Spunk", Null(),  
            "'mouth' in EmmaX.Spunk", "images/EmmaSprite/EmmaSprite_Spunk_HandM.png", 
            "True", "images/EmmaSprite/EmmaSprite_Spunk_Hand.png",   
            ),  
#        (0,0), ConditionSwitch(                                                                         #Props
#            "not EmmaX.Held or EmmaX.ArmPose != 2", Null(), 
#            "EmmaX.ArmPose == 2 and EmmaX.Held == 'phone'", "images/EmmaSprite/Emma_held_phone.png",
#            "EmmaX.ArmPose == 2 and EmmaX.Held == 'dildo'", "images/EmmaSprite/Emma_held_dildo.png",
#            "EmmaX.ArmPose == 2 and EmmaX.Held == 'vibrator'", "images/EmmaSprite/Emma_held_vibrator.png",
#            "EmmaX.ArmPose == 2 and EmmaX.Held == 'panties'", "images/EmmaSprite/Emma_held_panties.png",
#            "True", Null(), 
#            ),        
        (0,0), ConditionSwitch(
            #UI tool for When Emma is masturbating using Trigger3 actions
            "EmmaX.Loc == 'bg teacher'", Null(),
            "Trigger == 'lesbian' or not Trigger3 or Ch_Focus != EmmaX", Null(),
            
            #this is not a lesbian thing, and a trigger is set, and Emma is the primary. . .
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_EmmaSelf",  
            "Trigger3 == 'fondle breasts'", ConditionSwitch(                                                                      
                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeLeftBreast_Emma", 
                        #When zero is working the right breast, fondle left
                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeRightBreast_Emma",   
                        #When zero is working the left breast, fondle right
                    "True", "GirlGropeBothBreast_Emma",
                        #else, fondle both
                    ),  
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast_Emma",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy_Emma",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy_Emma",
            "Trigger3 == 'vibrator anal'", "VibratorAnal_Emma",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy_Emma",            
            "True", Null(),             
            ),                        
        (0,0), ConditionSwitch(  
            #UI tool for Trigger5(Threesome masutrbation) actions
            "EmmaX.Loc == 'bg teacher'", Null(),
            "not Trigger5 or Trigger4 != 'masturbation' or Ch_Focus == EmmaX", Null(), 
            
            #Emma is not primary, and T4 is masturbation, and a T5 is selected
            "Trigger5 == 'fondle pussy' and Trigger != 'sex' and EmmaX.Lust >= 70", "GirlFingerPussy_Emma",
            "Trigger5 == 'fondle pussy'", "GirlGropePussy_Emma",
            "Trigger5 == 'fondle breasts'", "GirlGropeRightBreast_Emma",
            "Trigger5 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger5 == 'vibrator pussy'", "VibratorPussy",
            "Trigger5 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger5 == 'vibrator anal'", "VibratorAnal",
            "Trigger5 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(), 
            ),               
        (0,0), ConditionSwitch(                
            #UI tool for Trigger1(primary) actions
            "EmmaX.Loc == 'bg teacher'", Null(),
            "not Trigger or Ch_Focus != EmmaX", Null(),
            
            # Emma is primary and a sex trigger is active
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast_Emma",
            "Trigger == 'fondle thighs'", "GropeThigh_Emma",
            "Trigger == 'fondle breasts'", "GropeLeftBreast_Emma",
            "Trigger == 'suck breasts'", "LickRightBreast_Emma",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_Emma",
            "Trigger == 'fondle pussy'", "GropePussy_Emma",
            "Trigger == 'lick pussy'", "Lickpussy_Emma",
            "Trigger == 'vibrator pussy'", "VibratorPussy_Emma",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy_Emma",
            "Trigger == 'vibrator anal'", "VibratorAnal_Emma",
            "Trigger == 'vibrator anal insert'", "VibratorPussy_Emma",
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                
            #UI tool for Trigger2(secondary) actions
            "EmmaX.Loc == 'bg teacher'", Null(),
            "not Trigger2 or Ch_Focus != EmmaX", Null(),
            
            #Emma is primary and an offhand trigger is active            
            "Trigger2 == 'fondle breasts'", ConditionSwitch(                                                                      
                    "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast_Emma", 
                        #When zero is sucking on the right breast, fondle left
                    "True", "GropeRightBreast_Emma",
                        #else, fondle right
                    ),  
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast_Emma",       
                #When sucking right breast, vibrator left            
            "Trigger2 == Trigger", Null(),
                #When both triggers are the same, do nothing              
            "Trigger2 == 'suck breasts'", "LickLeftBreast_Emma",        
            "Trigger2 == 'fondle pussy'", "GropePussy_Emma",
            "Trigger2 == 'lick pussy'", "Lickpussy_Emma",       
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast_Emma",
            "Trigger2 == 'vibrator pussy'", "VibratorPussy_Emma",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy_Emma",
            "Trigger2 == 'vibrator anal'", "VibratorAnal_Emma",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy_Emma",
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(  
            #UI tool for Trigger4(Threesome) actions (ie Rogue's hand on her)
            "EmmaX.Loc == 'bg teacher'", Null(),
            "not Trigger4 or Ch_Focus != EmmaX", Null(),
            
            # There is a threesome trigger set and Emma is the target of it
            "Trigger4 == 'fondle pussy' and Trigger != 'sex' and EmmaX.Lust >= 70", "GirlFingerPussy_Emma",
            "Trigger4 == 'fondle pussy'", "GirlGropePussy_Emma",            
            "Trigger4 == 'lick pussy'", "Lickpussy_Emma",
            "Trigger4 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Emma", 
            "Trigger4 == 'suck breasts'", "LickRightBreast_Emma",              
            "Trigger4 == 'fondle breasts'", ConditionSwitch( 
                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeLeftBreast_Emma",   
                        #When zero is working the right breast, fondle left                                                  
#                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeRightBreast_Emma", 
#                        #When zero is working the left breast, fondle right                                         
#                    "Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts'", "GirlGropeRightBreast_Emma", 
#                        #When zero is working the left breast, fondle right 
                    "True", "GirlGropeRightBreast_Emma",
                        #else, fondle right
                    ),                  
            "Trigger4 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger4 == 'vibrator pussy'", "VibratorPussy",
            "Trigger4 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger4 == 'vibrator anal'", "VibratorAnal",
            "Trigger4 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),             
            ),    
        (0,0), ConditionSwitch(             
            #UI tool for Trigger3(lesbian) actions (ie Rogue's hand on her when Emma is secondary)
            "EmmaX.Loc == 'bg teacher'", Null(),
            "Trigger != 'lesbian' or Ch_Focus == EmmaX or not Trigger3", Null(),
            
            # If there is a Trigger3 and Emma is not the focus
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and EmmaX.Lust >= 70", "GirlFingerPussy_Emma",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_Emma",            
            "Trigger3 == 'lick pussy'", "Lickpussy_Emma",
            "Trigger3 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Emma", 
            "Trigger3 == 'suck breasts'", "LickRightBreast_Emma",              
            "Trigger3 == 'fondle breasts'", ConditionSwitch( 
                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeLeftBreast_Emma",   
                        #When zero is working the right breast, fondle left                                                  
                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeRightBreast_Emma", 
                        #When zero is working the left breast, fondle right                                         
                    "Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts'", "GirlGropeLeftBreast_Emma", 
                        #When zero is working the right breast, fondle left 
                    "True", "GirlGropeRightBreast_Emma",
                        #else, fondle right
                    ),                             
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

image TempHairBack:
    "images/EmmaSprite/EmmaSprite_Head_HairBackWet.png"         
    anchor (0.6, 0.0)                
    zoom .5                   
    
image EmmaSprite_Head:
    LiveComposite(
        (555,673), 
#        (0,0), ConditionSwitch(                                                                         #hair back 
#            "EmmaX.Hair", "images/EmmaSprite/EmmaSprite_Hairback.png",   
#            "True", Null(),        
#            ),      

#        (0,0), ConditionSwitch(                                                                         #Face no blush not wet
#            "EmmaX.Blush or EmmaX.Hair == 'wet' or EmmaX.Water", Null(),        
#            "EmmaX.Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_Angry.png",
#            "EmmaX.Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_Sad.png",
#            "EmmaX.Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_Surprised.png",     
#            "EmmaX.Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_Confused.png", 
#            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_Normal.png", #EmmaX.Brows == 'normal'
#            ),
#        (0,0), ConditionSwitch(                                                                         #Face blush 1 not wet
#            "EmmaX.Blush != 1 or EmmaX.Hair == 'wet' or EmmaX.Water", Null(),        
#            "EmmaX.Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_AngryB1.png",
#            "EmmaX.Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_SadB1.png",
#            "EmmaX.Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_SurprisedB1.png",   
#            "EmmaX.Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_ConfusedB1.png", 
#            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_NormalB1.png", #EmmaX.Brows == 'normal'
#            ),
#        (0,0), ConditionSwitch(                                                                         #Face blush 2 not wet
#            "EmmaX.Blush != 2 or EmmaX.Hair == 'wet' or EmmaX.Water", Null(),        
#            "EmmaX.Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_AngryB2.png",
#            "EmmaX.Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_SadB2.png",
#            "EmmaX.Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_SurprisedB2.png",    
#            "EmmaX.Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_ConfusedB2.png", 
#            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_NormalB2.png", #EmmaX.Brows == 'normal'
#            ),
        
#         (0,0), ConditionSwitch(                                                                         #Face no blush wet
#            "EmmaX.Blush or (EmmaX.Hair != 'wet' and not EmmaX.Water)", Null(),        
#            "EmmaX.Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_Angry.png",
#            "EmmaX.Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_Sad.png",
#            "EmmaX.Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_Surprised.png",    
#            "EmmaX.Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_Confused.png",  
#            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_Normal.png", #EmmaX.Brows == 'normal'
#            ),
#        (0,0), ConditionSwitch(                                                                         #Face blush 1 wet
#            "EmmaX.Blush != 1 or (EmmaX.Hair != 'wet' and not EmmaX.Water)", Null(),        
#            "EmmaX.Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_AngryB1.png",
#            "EmmaX.Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_SadB1.png",
#            "EmmaX.Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_SurprisedB1.png",    
#            "EmmaX.Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_ConfusedB1.png",    
#            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_NormalB1.png", #EmmaX.Brows == 'normal'
#            ),
#        (0,0), ConditionSwitch(                                                                         #Face blush 2 wet
#            "EmmaX.Blush != 2 or (EmmaX.Hair != 'wet' and not EmmaX.Water)", Null(),        
#            "EmmaX.Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_AngryB2.png",
#            "EmmaX.Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_SadB2.png",
#            "EmmaX.Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_SurprisedB2.png",    
#            "EmmaX.Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_ConfusedB2.png",    
#            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_NormalB2.png", #EmmaX.Brows == 'normal'
#            ),
        
        (0,0), ConditionSwitch(
                # Face background plate
                "not EmmaX.Blush", ConditionSwitch(
                    #If no Blush
                    "EmmaX.Hair == 'wet' or EmmaX.Water", ConditionSwitch(
                            #If the hair is wet
                            "EmmaX.Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_Angry.png",
                            "EmmaX.Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_Sad.png",
                            "EmmaX.Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_Surprised.png",    
                            "EmmaX.Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_Confused.png",  
                            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_Normal.png", #EmmaX.Brows == 'normal'
                            ),
                    "True", ConditionSwitch(
                            #If the hair is not wet
                            "EmmaX.Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_Angry.png",
                            "EmmaX.Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_Sad.png",
                            "EmmaX.Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_Surprised.png",     
                            "EmmaX.Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_Confused.png", 
                            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_Normal.png", #EmmaX.Brows == 'normal'
                            ),
                    ),
                "EmmaX.Blush == 1", ConditionSwitch(
                    #If the first tier blush
                    "EmmaX.Hair == 'wet' or EmmaX.Water", ConditionSwitch(
                            #If the hair is wet
                            "EmmaX.Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_AngryB1.png",
                            "EmmaX.Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_SadB1.png",
                            "EmmaX.Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_SurprisedB1.png",    
                            "EmmaX.Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_ConfusedB1.png",    
                            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_NormalB1.png", #EmmaX.Brows == 'normal'
                            ),
                    "True", ConditionSwitch(
                            #If the hair is not wet
                            "EmmaX.Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_AngryB1.png",
                            "EmmaX.Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_SadB1.png",
                            "EmmaX.Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_SurprisedB1.png",   
                            "EmmaX.Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_ConfusedB1.png", 
                            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_NormalB1.png", #EmmaX.Brows == 'normal'
                            ),
                    ),            
                "True", ConditionSwitch(
                    #else, 2nd tier blush
                    "EmmaX.Hair == 'wet' or EmmaX.Water", ConditionSwitch(
                            #If the hair is wet
                            "EmmaX.Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_AngryB2.png",
                            "EmmaX.Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_SadB2.png",
                            "EmmaX.Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_SurprisedB2.png",    
                            "EmmaX.Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_ConfusedB2.png",    
                            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_NormalB2.png", #EmmaX.Brows == 'normal'
                            ),
                    "True", ConditionSwitch(
                            #If the hair is not wet
                            "EmmaX.Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_AngryB2.png",
                            "EmmaX.Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_SadB2.png",
                            "EmmaX.Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_SurprisedB2.png",    
                            "EmmaX.Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_ConfusedB2.png", 
                            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_NormalB2.png", #EmmaX.Brows == 'normal'
                            ),
                    ),                    
                ),        
        (0,0), ConditionSwitch(                                                                         #Mouths        
            "EmmaX.Mouth == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Normal.png",
            "EmmaX.Mouth == 'lipbite'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Lipbite.png",
            "EmmaX.Mouth == 'sucking'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Surprised.png",            
            "EmmaX.Mouth == 'kiss'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Kiss.png",
            "EmmaX.Mouth == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Sad.png",
            "EmmaX.Mouth == 'smile'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Smile.png",
            "EmmaX.Mouth == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Surprised.png",            
            "EmmaX.Mouth == 'tongue'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Tongue.png",                
            "EmmaX.Mouth == 'grimace'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Smile.png",                 
            "EmmaX.Mouth == 'smirk'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Smirk.png",         
            "True", "images/EmmaSprite/EmmaSprite_Head_Mouth_Normal.png",
            ),   
        
        (0,0), ConditionSwitch(                                                                         #Mouth spunk               
            "'mouth' not in EmmaX.Spunk", Null(),
            "EmmaX.Mouth == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Spunk_MouthOpen.png",            
            "EmmaX.Mouth == 'tongue'", "images/EmmaSprite/EmmaSprite_Head_Spunk_MouthTongue.png",            
            "True", "images/EmmaSprite/EmmaSprite_Head_Spunk_Mouth.png",  
            ),  
        
        (0,0), "Emma Blink",                                                                           #Eyes        
        (0,0), ConditionSwitch(                                                                         #brows
            "EmmaX.Brows == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal.png",
            "EmmaX.Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Brows_Angry.png",
            "EmmaX.Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Brows_Sad.png",
            "EmmaX.Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Brows_Surprised.png",        
            "EmmaX.Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Brows_Confused.png",
            "True", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal.png",
            ),         
        (0,0), ConditionSwitch(                                                                         #facial spunk               
            "'facial' in EmmaX.Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_Face.png",             
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                         #Hair
            "not EmmaX.Hair", Null(),
            "EmmaX.Hair == 'wet' or EmmaX.Water", "images/EmmaSprite/EmmaSprite_Head_HairWet.png",
            "EmmaX.Hair", "images/EmmaSprite/EmmaSprite_Head_Hair.png",
            "True", Null(),
            ),        
        (0,0), ConditionSwitch(                                                                         #Hair Water
            "not EmmaX.Water", Null(),
            "EmmaX.Hair == 'wet'", "images/EmmaSprite/EmmaSprite_Head_Water.png",
            "True", "images/EmmaSprite/EmmaSprite_Head_Water.png",
            ),
        (0,0), ConditionSwitch(                                                                         #hair spunk               
            "'hair' in EmmaX.Spunk and (EmmaX.Hair == 'wet' or EmmaX.Water)", "images/EmmaSprite/EmmaSprite_Head_Spunk_HairWet.png",                         
            "'hair' in EmmaX.Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_HairWave.png",              
            "True", Null(),
            ),  
        )                
    anchor (0.6, 0.0)                
    zoom .5   

image Emma Blink:
    ConditionSwitch(
        "EmmaX.Eyes == 'sexy'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Sexy.png",
        "EmmaX.Eyes == 'side'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Side.png",
        "EmmaX.Eyes == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Surprised.png",
        "EmmaX.Eyes == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Normal.png",    
        "EmmaX.Eyes == 'stunned'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Agao.png",
        "EmmaX.Eyes == 'down'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Down.png",
        "EmmaX.Eyes == 'closed'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Closed.png",
        "EmmaX.Eyes == 'manic'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Surprised.png",
        "EmmaX.Eyes == 'squint'", "Emma_Squint",
        "True", "images/EmmaSprite/EmmaSprite_Head_Eyes_Normal.png", 
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/EmmaSprite/EmmaSprite_Head_Eyes_Closed.png"
    .25
    repeat                

image Emma_Squint:            
    "images/EmmaSprite/EmmaSprite_Head_Eyes_Sexy.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/EmmaSprite/EmmaSprite_Head_Eyes_Squint.png"
    .25
    repeat   
            
            
image Emma_Drip_Mask:
    #This is the mask for her drip pattern
    contains:
        "images/EmmaSprite/EmmaSprite_WetMask.png"      
        offset (-215,-540)

image Emma_Drip_MaskP:
    #This is the mask for her drip pattern in panties down mode
    contains:
        "images/EmmaSprite/EmmaSprite_WetMaskP.png"      
        offset (-215,-540)  
            
# End Emma Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Emma Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Emma Sex element ///////////////////////////////////////////////////////////////////////////      

image Emma_SexSprite:
    #core sex animation   
    contains:
        ConditionSwitch(                                                               
            # Emma's lower body
            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(                                                               
                    # If during sex
                    "Speed == 1", "Emma_Sex_Legs_S1",#heading
                    "Speed == 2", "Emma_Sex_Legs_S2",#slow
                    "Speed == 3", "Emma_Sex_Legs_S3",#fast
                    "Speed >= 4", "Emma_Sex_Legs_S4",#cumming
                    "True", "Emma_Sex_Legs_S0",#Static
                    ),
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(                                                              
                    # If during Anal
                    "Speed == 1", "Emma_Sex_Legs_A1",#heading
                    "Speed == 2", "Emma_Sex_Legs_A2",#slow
                    "Speed == 3", "Emma_Sex_Legs_A3",#fast
                    "Speed >= 4", "Emma_Sex_Legs_A4",#cumming
                    "True", "Emma_Sex_Legs_A0",#Static
                    ),
            "True", ConditionSwitch(                                                               
                    # If neither
                    "Speed == 1", "Emma_Sex_Legs_H1",#heading
                    "Speed == 4", "Emma_Sex_Legs_H4",#cumming
                    "Speed >= 2", "Emma_Sex_Legs_H2",#slow
                    "True", "Emma_Sex_Legs_H0",#Static
                    ),
            ) 
    contains:
        ConditionSwitch(                                                              
            # Emma's upper body
            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(                                                               
                    # If during sex
                    "Speed == 1", "Emma_Sex_Body_S1",#heading
                    "Speed == 2", "Emma_Sex_Body_S2",#slow
                    "Speed == 3", "Emma_Sex_Body_S3",#fast
                    "Speed >= 4", "Emma_Sex_Body_S4",#cumming
                    "True",       "Emma_Sex_Body_S0",#Static
                    ),
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(                                                              
#                    # If during Anal
                    "Speed == 1", "Emma_Sex_Body_A1",#heading
                    "Speed == 2", "Emma_Sex_Body_A2",#slow
                    "Speed == 3", "Emma_Sex_Body_A3",#fast
                    "Speed >= 4", "Emma_Sex_Body_A4",#cumming
                    "True",       "Emma_Sex_Body_A0",#Static
                    ),
            "True", ConditionSwitch(                                                              
                    # If neither
                    "Speed == 1", "Emma_Sex_Body_H1",#heading
                    "Speed == 4", "Emma_Sex_Body_H4",#cumming
                    "Speed >= 2", "Emma_Sex_Body_H2",#slow
                    "True",       "Emma_Sex_Body_H0",#Static
                    ),
            )
    zoom 0.8
    anchor (.5,.5)
    
image Emma_Sex_HairBack:
    #Hair underlay
    "Emma_BJ_HairBack"
    zoom 0.48
    anchor (0.5, 0.5)
    pos (505,260)
  
image Emma_Sex_Head:
    #Hair underlay
    "Emma_BJ_Head"
    zoom 0.48
    anchor (0.5, 0.5)
    pos (505,260)
                    

                    
# Emma's sex body torso / / / / / torso / / / / / torso / / / / / torso / / / / / torso / / / / /

image Emma_Sex_Tits:
    #the tits used in the sex pose
    contains:
            # tits
        ConditionSwitch(   
            "renpy.showing('Emma_TJ_Animation')", Null(),
            "EmmaX.Chest == 'corset'", "images/EmmaSex/Emma_Sex_Tits_Up.png",   # EmmaX.TitsUp = 1
            "EmmaX.Chest == 'sports bra' or EmmaX.Chest == 'lace bra'", "images/EmmaSex/Emma_Sex_Tits_Up.png",   # EmmaX.TitsUp = 1
            "True", "images/EmmaSex/Emma_Sex_Tits_Down.png",   # EmmaX.TitsUp = 0
            )
    contains:
            # piercings tits
        ConditionSwitch(   
            "renpy.showing('Emma_TJ_Animation')", Null(),
            "not EmmaX.Pierce or EmmaX.Chest", Null(),
            "EmmaX.Over == 'nighty'", Null(),
            "EmmaX.Pierce == 'barbell'", ConditionSwitch(   
                    #if it's the ring pericings   
                    "EmmaX.Chest in ('corset', 'lace bra', 'sports bra')", Null(),  
                    "True", "images/EmmaSex/Emma_Pierce_Barbell_Tits_D.png", 
                    ),    
            "EmmaX.Pierce == 'ring'", ConditionSwitch(   
                    #if it's the ring pericings   
                    "EmmaX.Chest in ('corset', 'lace bra', 'sports bra')", Null(),  
                    "True", "images/EmmaSex/Emma_Pierce_Ring_Tits_D.png", 
                    ),                    
            "True", Null(), 
            )
            
image Emma_Sex_Torso:                                                                        
    #Her torso for the sex, BJ, and TJ poses
    contains:
            # body
            "images/EmmaSex/Emma_Sex_Body.png"
    contains:
            # tits
        ConditionSwitch(   
            "renpy.showing('Emma_TJ_Animation')", Null(),
            "EmmaX.Chest == 'corset'", "images/EmmaSex/Emma_Sex_Tits_Up.png",   # EmmaX.TitsUp = 1
            "EmmaX.Chest == 'sports bra' or EmmaX.Chest == 'lace bra'", "images/EmmaSex/Emma_Sex_Tits_Up.png",   # EmmaX.TitsUp = 1
            "True", "images/EmmaSex/Emma_Sex_Tits_Down.png",   # EmmaX.TitsUp = 0
            )
    contains:
            # piercings tits
        ConditionSwitch(   
            "renpy.showing('Emma_TJ_Animation')", Null(),
            "not EmmaX.Pierce or EmmaX.Over or EmmaX.Chest", Null(),
            "EmmaX.Pierce == 'barbell'", ConditionSwitch(   
                    #if it's the ring pericings   
                    "EmmaX.Chest in ('corset', 'lace bra', 'sports bra')", Null(),  
                    "True", "images/EmmaSex/Emma_Pierce_Barbell_Tits_D.png", 
                    ),    
            "EmmaX.Pierce == 'ring'", ConditionSwitch(   
                    #if it's the ring pericings   
                    "EmmaX.Chest in ('corset', 'lace bra', 'sports bra')", Null(),  
                    "True", "images/EmmaSex/Emma_Pierce_Ring_Tits_D.png", 
                    ),                    
            "True", Null(), 
            )
#    contains:
#            # tits
#        ConditionSwitch(   
#            "renpy.showing('Emma_TJ_Animation')", Null(),
#            "True", "Emma_Sex_Tits",
#            )
    contains:
            #chest clothing under layer for TJs
            ConditionSwitch(    
                "not renpy.showing('Emma_TJ_Animation')", Null(),   # EmmaX.TitsUp = 0
                "EmmaX.Chest == 'sports bra'", "images/EmmaSex/Emma_Sex_Bra_Sports_TJU.png",
                "True", Null(),
                ) 
    contains:
            # Chest clothing layer
        ConditionSwitch(    
            "not EmmaX.Chest or renpy.showing('Emma_TJ_Animation')", Null(),   # EmmaX.TitsUp = 0
            "EmmaX.Chest == 'corset'", "images/EmmaSex/Emma_Sex_Bra_Corset_Up.png",   # EmmaX.TitsUp = 1
            "EmmaX.Chest == 'sports bra'", "images/EmmaSex/Emma_Sex_Bra_Sports_Up.png",   # EmmaX.TitsUp = 1
            "EmmaX.Chest == 'lace bra'", "images/EmmaSex/Emma_Sex_Bra_Lace_Up.png",   # EmmaX.TitsUp = 1
            "True", Null(),   # EmmaX.TitsUp = 0
            )
    contains:
            # Over clothing layer
        ConditionSwitch(   
            "EmmaX.Over == 'jacket'", ConditionSwitch(   
                    #if it's the ring pericings                       
                    "renpy.showing('Emma_TJ_Animation')", Null(),
#                    "renpy.showing('Emma_TJ_Animation')", "images/EmmaSex/Emma_Sex_Jacket_Down.png",
                    "EmmaX.Chest == 'corset'", "images/EmmaSex/Emma_Sex_Jacket_Up.png",   # EmmaX.TitsUp = 1
                    "EmmaX.Chest == 'sports bra'", "images/EmmaSex/Emma_Sex_Jacket_Up.png",   # EmmaX.TitsUp = 1
                    "EmmaX.Chest == 'lace bra'", "images/EmmaSex/Emma_Sex_Jacket_Up.png",   # EmmaX.TitsUp = 1
                    "True", "images/EmmaSex/Emma_Sex_Jacket_Down.png",   # EmmaX.TitsUp = 0
                    ),                
            "EmmaX.Over == 'nighty'", ConditionSwitch(
                    #if she has the nighty on     
                    "renpy.showing('Emma_TJ_Animation')", Null(),
                    "EmmaX.Chest in ('corset', 'lace bra', 'sports bra')", "images/EmmaSex/Emma_Sex_Nighty_Up.png",  
                    "True", "images/EmmaSex/Emma_Sex_Nighty_Down.png", 
                    ),    
            "True", Null(), 
            )
    contains:
            # spunk on tits
            ConditionSwitch(    
                "'tits' not in EmmaX.Spunk", Null(),
                "renpy.showing('Emma_TJ_Animation')", "images/EmmaSex/Emma_Spunk_Titjob_Under.png",
                "True", "images/EmmaSex/Emma_Spunk_Tits.png",
                ) 
    zoom 1 
                
image Emma_Sex_Body:                                                                        
    #Her Body in the sex pose
    contains:
            "Emma_Sex_HairBack"
    contains:
            # body
            "Emma_Sex_Torso"
    contains:
            # Arms
        ConditionSwitch(    
            "EmmaX.ArmPose == 3", Null(),   # Neither arms
            "EmmaX.ArmPose == 4", AlphaMask("Emma_SexArms", "images/EmmaSex/Emma_Sex_ArmsMask_R.png"),   # Right arm only
            "EmmaX.ArmPose == 5", AlphaMask("Emma_SexArms", "images/EmmaSex/Emma_Sex_ArmsMask_L.png"),   # Left arm only
            "True", AlphaMask("Emma_SexArms", "images/EmmaSex/Emma_Sex_ArmsMask.png"),  # Both Arms
            )
    contains:
            "Emma_Sex_Head"
    zoom 1 
#    offset (0,0)
# end Emma's sex body torso / / / / / torso / / / / / torso / / / / / torso / / / / / torso / / / / /


image Emma_SexArms:
    contains:
            # Base Arms
        ConditionSwitch(    
            "EmmaX.Over == 'jacket'", Null(),
            "EmmaX.Chest == 'corset'", "images/EmmaSex/Emma_Sex_Arms_U.png",   # EmmaX.TitsUp = 1
            "EmmaX.Chest == 'sports bra'", "images/EmmaSex/Emma_Sex_Arms_U.png",   # EmmaX.TitsUp = 1
            "EmmaX.Chest == 'lace bra'", "images/EmmaSex/Emma_Sex_Arms_U.png",   # EmmaX.TitsUp = 1
            "True", "images/EmmaSex/Emma_Sex_Arms_D.png",   # EmmaX.TitsUp = 0
            )
    contains:
            # Arm clothing
        ConditionSwitch(    
            "EmmaX.Over == 'jacket'", Null(),
            "EmmaX.Chest == 'sports bra'", "images/EmmaSex/Emma_Sex_Bra_Sports_Arms.png",   # EmmaX.TitsUp = 1
            "True", Null(),
            )
    contains:
            # Arm clothing Over
        ConditionSwitch(    
            "EmmaX.Over == 'jacket'", "images/EmmaSex/Emma_Sex_Arms_Jacket.png",   # EmmaX.TitsUp = 1
            "EmmaX.Arms", "images/EmmaSex/Emma_Sex_Gloves.png",           
            "True", Null(),
            )



# Emma's sex body legs / / / / / legs / / / / / legs / / / / / legs / / / / / legs / / / / /
image Emma_Sex_Legs_S:                                                                        
    #Her Legs during sex
    contains:
            # spunk
        ConditionSwitch(    
            "'anal' in EmmaX.Spunk or 'in' in EmmaX.Spunk", "images/EmmaSex/Emma_Spunk_Sex.png", 
            "True", Null(),
            )
    contains:
            # Legs base
        ConditionSwitch(    
            "Trigger == 'hotdog'", "images/EmmaSex/Emma_Sex_Legs_Hotdog.png", 
            "True", "images/EmmaSex/Emma_Sex_Legs_Sex.png", 
            )
    contains:
            # piercings
        ConditionSwitch(    
            "EmmaX.Panties and not EmmaX.PantiesDown", Null(), 
            "EmmaX.Legs and not EmmaX.Upskirt", Null(), 
            "EmmaX.Pierce == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_S.png", 
            "EmmaX.Pierce == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S.png",
            "True", Null(), 
            )
    contains:
            # pubes
        ConditionSwitch(    
            "EmmaX.Pubes", "images/EmmaSex/Emma_Pubes_Sex.png", 
            "True", Null(),
            )        
    contains:
            # panties
        ConditionSwitch(    
            "EmmaX.PantiesDown", Null(),
            "EmmaX.Panties == 'sports panties' and EmmaX.Wet", "images/EmmaSex/Emma_Sex_Panties_Sport_SW.png", 
            "EmmaX.Panties == 'sports panties'", "images/EmmaSex/Emma_Sex_Panties_Sport_S.png", 
            "EmmaX.Panties and EmmaX.Wet", "images/EmmaSex/Emma_Sex_Panties_SW.png", 
            "EmmaX.Panties", "images/EmmaSex/Emma_Sex_Panties_S.png", 
            "True", Null(),
            )         
    contains:
            # boots
        ConditionSwitch(    
            "EmmaX.Acc == 'thigh boots'", "images/EmmaSex/Emma_Sex_Boots_Pussy.png", 
            "True", Null(),
            )              
    contains:
            # legs
        ConditionSwitch(    
            "EmmaX.Legs == 'skirt'", "images/EmmaSex/Emma_Sex_Skirt_Pussy.png", 
            "EmmaX.Upskirt", Null(),
            "EmmaX.Legs == 'pants' and EmmaX.Wet >= 2", "images/EmmaSex/Emma_Sex_Pants_SW.png", 
            "EmmaX.Legs == 'pants'", "images/EmmaSex/Emma_Sex_Pants_S.png", 
            "True", Null(),
            )
    contains:
            # Over
        ConditionSwitch(    
            "EmmaX.Over == 'nighty'", "images/EmmaSex/Emma_Sex_Nighty_Pussy.png", 
            "True", Null(),
            )
    contains:
            # spunk
        ConditionSwitch(    
            "'belly' in EmmaX.Spunk", "images/EmmaSex/Emma_Spunk_Belly.png", 
            "True", Null(),
            )
    zoom 1 
#    offset (0,0)

image Emma_Sex_Legs_A:                        
    #Her Legs during anal
    contains:
            # anal spunk
        ConditionSwitch(    
            "'anal' in EmmaX.Spunk and not Speed", "images/EmmaSex/Emma_Spunk_Anal_Closed.png", 
            "True", Null(),
            )
    contains:
            # Legs Base
            "images/EmmaSex/Emma_Sex_Legs_Anal.png"
    contains:
            #Anus
        ConditionSwitch(  
            "Player.Sprite and Player.Cock == 'anal' and Speed", ConditionSwitch(                                                              
                    # If during Anal
                    "Speed == 1", "Emma_Sex_Anus_A1",#heading
                    "True", "Emma_Sex_Anus_A2",#faster
                    ),
            "True", "Emma_Sex_Anus_A0",
            ) 
    contains:
            # pubes
        ConditionSwitch(    
            "EmmaX.Pubes", "images/EmmaSex/Emma_Pubes_Anal.png", 
            "True", Null(),
            )
    contains:
            # piercings
        ConditionSwitch(    
            "EmmaX.Panties and not EmmaX.PantiesDown", Null(), 
            "EmmaX.Legs and not EmmaX.Upskirt", Null(), 
            "EmmaX.Pierce == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_A.png", 
            "EmmaX.Pierce == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_A.png",
            "True", Null(), 
            )        
    contains:
            # panties
        ConditionSwitch(    
            "EmmaX.PantiesDown", Null(),
            "EmmaX.Panties == 'sports panties' and EmmaX.Wet", "images/EmmaSex/Emma_Sex_Panties_Sport_AW.png", 
            "EmmaX.Panties == 'sports panties'", "images/EmmaSex/Emma_Sex_Panties_Sport_A.png", 
            "EmmaX.Panties and EmmaX.Wet", "images/EmmaSex/Emma_Sex_Panties_AW.png", 
            "EmmaX.Panties", "images/EmmaSex/Emma_Sex_Panties_A.png", 
            "True", Null(),
            )
    contains:
            # pussy spunk
        ConditionSwitch(    
            "'in' in EmmaX.Spunk", "images/EmmaSex/Emma_Spunk_Anal_Pussy.png", 
            "True", Null(),
            )         
    contains:
            # boots
        ConditionSwitch(    
            "EmmaX.Acc == 'thigh boots'", "images/EmmaSex/Emma_Sex_Boots_Anal.png", 
            "True", Null(),
            )              
    contains:
            # legs
        ConditionSwitch(    
            "EmmaX.Legs == 'skirt'", "images/EmmaSex/Emma_Sex_Skirt_Anal.png", 
            "EmmaX.Upskirt", Null(),
            "EmmaX.Legs == 'pants' and EmmaX.Wet >= 2", "images/EmmaSex/Emma_Sex_Pants_AW.png", 
            "EmmaX.Legs == 'pants'", "images/EmmaSex/Emma_Sex_Pants_A.png", 
            "True", Null(),
            )
    contains:
            # Over
        ConditionSwitch(    
            "EmmaX.Over == 'nighty'", "images/EmmaSex/Emma_Sex_Nighty_Anal.png", 
            "True", Null(),
            )
    contains:
            # spunk
        ConditionSwitch(    
            "'belly' in EmmaX.Spunk", "images/EmmaSex/Emma_Spunk_Belly.png", 
            "True", Null(),
            )
        ypos -40
    zoom 1 
#    offset (0,0)

image Emma_Sex_Pussy_Mask:
    contains:
            "images/EmmaSex/Emma_Sex_Pussy_Mask.png"
    contains:       
            # piercings
        ConditionSwitch(    
            "EmmaX.Panties and not EmmaX.PantiesDown", Null(), 
            "EmmaX.Legs and not EmmaX.Upskirt", Null(), 
            "EmmaX.Pierce == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_S.png", 
            "EmmaX.Pierce == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S.png",
            "True", Null(), 
            ) 

image Emma_Sex_Hotdog_Mask:
    contains:
            "images/EmmaSex/Emma_Sex_Legs_HotdogMask.png"
#            yoffset 3
    contains:       
            # piercings
        ConditionSwitch(    
            "EmmaX.Panties and not EmmaX.PantiesDown", Null(), 
            "EmmaX.Legs and not EmmaX.Upskirt", Null(), 
            "EmmaX.Pierce == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_S.png", 
            "EmmaX.Pierce == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S.png",
            "True", Null(), 
            ) 
    contains:
            # piercings
        ConditionSwitch(    
            "EmmaX.Panties and not EmmaX.PantiesDown", Null(), 
            "EmmaX.Legs and not EmmaX.Upskirt", Null(), 
            "EmmaX.Pierce == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_S.png", 
            "EmmaX.Pierce == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S.png",
            "True", Null(), 
            )
            
# Emma's sex body legs / / / / / legs / / / / / legs / / / / / legs / / / / / legs / / / / /



#  Sex animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_Sex_Body_H0:                                                                        
    #Her Body in the hotdog pose, idle
    contains:
        "Emma_Sex_Body"   
        subpixel True          
        pos (0,-10) #top
        block:
            ease 2 pos (0,0) #bottom
            ease 2 pos (0,-10) #top
            repeat

image Emma_Sex_Body_H1:                                                                        
    #Her Body in the hotdog pose, slow
    contains:
        "Emma_Sex_Body"     
        subpixel True        
        pos (0,-10) #top
        block:
            ease 1.5 pos (0,0) #bottom
            ease 1.5 pos (0,-10) #top
            repeat

image Emma_Sex_Body_H2:                                                                        
    #Her Body in the hotdog pose, fast
    contains:
        "Emma_Sex_Body" 
        subpixel True            
        pos (0,-10) #top
        block:
            ease .6 pos (0,10) #bottom
            ease .4 pos (0,-10) #top
            repeat

image Emma_Sex_Body_H4:                                                                        
    #Her Body in the hotdog pose, cumming
    contains:
        "Emma_Sex_Body"   
        subpixel True          
        pos (0,-80) #top
        block:
            ease 1.5 pos (0,-70) #bottom
            ease 2 pos (0,-80) #top
            pause .5
            repeat
            
image Emma_Sex_Body_S0:                                                                        
    #Her Body in the sex pose, idle
    contains:
        "Emma_Sex_Body"      
        subpixel True       
        pos (0,-60) #top (0,-10)
        block:
            ease 1 pos (0,-50) #bottom (0,0)
            ease 1 pos (0,-60) #top
            repeat

image Emma_Sex_Body_S1:                                                                        
    #Her Body in the sex pose, slow
    contains:
        "Emma_Sex_Body"  
        subpixel True           
        pos (0,-20) #top
        block:
            ease .75 pos (0,0) #bottom
            ease 1.5 pos (0,-20) #top
            pause 0.75
            repeat
            
image Emma_Sex_Body_S2:                                                                        
    #Her Body in the sex pose, fast
    contains:
        "Emma_Sex_Body"   
        subpixel True          
        pos (0,-50) #top
        block:
            ease 0.5 pos (0,20) #bottom
            ease 1.5 pos (0,-50) #top
#            pause 0.5
            repeat

image Emma_Sex_Body_S3:                                                                        
    #Her Body in the sex pose, superfast
    contains:
        "Emma_Sex_Body" 
        subpixel True            
        pos (0,-50) #top
        block:
            ease 0.25 pos (0,0) #bottom
            ease 0.5 pos (0,-50) #top
            repeat

image Emma_Sex_Body_S4:                                                                        
    #Her Body in the sex pose, cumming
    contains:
        "Emma_Sex_Body"      
        subpixel True       
        pos (0,-20) #top
        block:
            ease 0.5 pos (0,0) #bottom
            ease 1 pos (0,-20) #top
            repeat
            
image Emma_Sex_Body_A0:                                                                       
    #Her Body in the anal pose, idle
    contains:
        "Emma_Sex_Body"    
        subpixel True         
        pos (0,-115) #top (0,-20)
        block:
            ease 1 pos (0,-95) #bottom (0,-10)
            ease 1 pos (0,-115) #top
            repeat

image Emma_Sex_Body_A1:                                                                        
    #Her Body in the anal pose, slow
    contains:
        "Emma_Sex_Body"  
        subpixel True   
        pos (0,-80) #top (0,-40)
        block:
            easeout 1 pos (0,-60) #bottom   (0,-20)
            easein 2 pos (0,-40) #bottom  (0,0)
            pause 1
            easeout 1 pos (0,-60) #top (0,-20)
            easein 2 pos (0,-80) #top
            pause 1
            repeat
            
image Emma_Sex_Body_A2:                                                                       
    #Her Body in the anal pose, fast
    contains:
        "Emma_Sex_Body"  
        subpixel True           
        pos (0,-10) #top
        block:
            ease .30 pos (0,10) #mid   
            ease .50 pos (0,50) #bottom  
            pause .3
            ease .80 pos (0,-10) #top
            pause .1
            repeat

image Emma_Sex_Body_A3:                                                                       
    #Her Body in the anal pose, very fast
    contains:
        "Emma_Sex_Body"  
        subpixel True      
        pos (0,-10) #top
        block:  
            ease .40 pos (0,50) #bottom  
            ease .60 pos (0,-10) #top
            repeat

image Emma_Sex_Body_A4:                                                                       
    #Her Body in the anal pose, cumming
    contains:
        "Emma_Sex_Body"    
        subpixel True         
        pos (0,20) #top (0,-20)
        block:
            ease 1 pos (0,40) #bottom (0,-10)
            ease 1 pos (0,20) #top
            repeat
            
# Leg animations / / / / / / Legs / / / / / / Legs / / / / / / Legs / / / / / / Legs / / / / / /
image Emma_Sex_Legs_H0:
    # Her Legs in the Hotdog pose, idle
    contains:
            #Body
            "Emma_Sex_Legs_S"
            subpixel True
            anchor (.515,.5)
            pos (528,340) #top (528,300)
            zoom .95   
            parallel:
                ease 2 zoom .98 #bottom
                ease 2 zoom .95 #top
#                pause .3
                repeat
            parallel:
                ease 2 ypos 360 #bottom
                ease 2 ypos 340 #top
#                pause .3
                repeat    
    contains:
            #Cock
            ConditionSwitch(  
                "Player.Sprite", "Zero_Doggy_Insert", 
                "True", Null(),
                )          
            alpha 1
            zoom 1.2
            pos (450,590)
    contains:
            #Overlay
            AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Hotdog_Mask")#"images/EmmaSex/Emma_Sex_Legs_HotdogMask.png")
            subpixel True
            anchor (.515,.5)
            pos (528,340) #top (528,300)
            zoom .95    
            parallel:
                ease 2 zoom .98 #bottom
                ease 2 zoom .95 #top
#                pause .3
                repeat
            parallel:
                ease 2 ypos 360 #bottom
                ease 2 ypos 340 #top
#                pause .3
                repeat     
    # End Legs Hotdog Idle

image Emma_Sex_Legs_H1:
    # Her Legs in the Hotdog pose, slow
    contains:
            #Body
            "Emma_Sex_Legs_S"
            subpixel True
            anchor (.515,.5)
            pos (528,300) #top (528,300)
            zoom .9   
            parallel:
                ease 1.5 zoom 1 #bottom
                ease 1.5 zoom .9 #top
                pause .3
                repeat
            parallel:
                ease 1.5 ypos 390 #bottom
                ease 1.5 ypos 300 #top
                pause .3
                repeat    
    contains:
            #Cock
            ConditionSwitch(  
                "Player.Sprite", "Zero_Doggy_Insert", 
                "True", Null(),
                )          
            alpha 1
            zoom 1.2
            pos (450,590)
    contains:
            #Overlay
            AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Hotdog_Mask")#"images/EmmaSex/Emma_Sex_Legs_HotdogMask.png")
            subpixel True
            anchor (.515,.5)
            pos (528,300) #top(515,300) 
            zoom .9   
            parallel:
                ease 1.5 zoom 1 #bottom
                ease 1.5 zoom .9 #top
                pause .3
                repeat
            parallel:
                ease 1.5 ypos 390 #bottom
                ease 1.5 ypos 300 #top
                pause .3
                repeat    
    # End Legs Hotdog slow

image Emma_Sex_Legs_H2:
    # Her Legs in the Hotdog pose, fast
    contains:
            #Body
            "Emma_Sex_Legs_S"
            subpixel True
            anchor (.515,.5)
            pos (528,340) #top (528,300)
            zoom .95   
            parallel:
                ease .6 zoom 1 #bottom
                ease .4 zoom .95 #top
#                pause .3
                repeat
            parallel:
                ease .6 ypos 390 #bottom
                ease .4 ypos 340 #top
#                pause .3
                repeat    
    contains:
            #Cock
            ConditionSwitch(  
                "Player.Sprite", "Zero_Doggy_Insert", 
                "True", Null(),
                )          
            alpha 1
            zoom 1.2
            pos (450,590)
    contains:
            #Overlay
            AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Hotdog_Mask")#"images/EmmaSex/Emma_Sex_Legs_HotdogMask.png")
            subpixel True
            anchor (.515,.5)
            pos (528,340) #top (528,300)
            zoom .95   
            parallel:
                ease .6 zoom 1 #bottom
                ease .4 zoom .95 #top
#                pause .3
                repeat
            parallel:
                ease .6 ypos 390 #bottom
                ease .4 ypos 340 #top
#                pause .3
                repeat    
    # End Legs Hotdog fast
  
image Emma_Sex_Legs_H4:
    # Her Legs in the Hotdog pose, cumming
    contains:
            #Body
            "Emma_Sex_Legs_S"
            subpixel True
#            anchor (.515,.5)
            pos (0,-80) #top
            parallel:
                ease 2 ypos -70 #bottom
                ease 2 ypos -80 #top
                repeat
                
    contains:
            #Cock
            "Blowcock" 
            alpha 0.9
            zoom 0.5
            pos (680,440)   
#    contains:
#            #Cock
#            ConditionSwitch(  
#                "Player.Sprite", "Zero_Doggy_Insert", 
#                "True", Null(),
#                )          
#            alpha 1
#            zoom 1.2
#            pos (450,590)
#    contains:
#            #Overlay
#            AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Hotdog_Mask")#"images/EmmaSex/Emma_Sex_Legs_HotdogMask.png")
#            subpixel True
#            anchor (.515,.5)
#            pos (528,340) #top (528,300)
#            zoom .95    
#            parallel:
#                ease 2 zoom .98 #bottom
#                ease 2 zoom .95 #top
##                pause .3
#                repeat
#            parallel:
#                ease 2 ypos 360 #bottom
#                ease 2 ypos 340 #top
##                pause .3
#                repeat     
    # End Legs Hotdog Idle
                
# Emma's sex legs animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_Sex_Legs_S0:
    # Her Legs in the Sex pose, idle
    contains:
            #Body
            "Emma_Sex_Legs_S"
            subpixel True
            pos (0,-140) #top
            parallel:
                ease 1 ypos -135 #bottom
                ease 1 ypos -140 #top
                repeat
            parallel:
                ease 2 xpos -8 #bottom
                ease 2 xpos 8 #top
                repeat
    contains:
            #Cock
            "Blowcock" 
            alpha 0.9
            zoom 0.5
            pos (680,400)         
    contains:
            #Overlay
            AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Pussy_Mask")#"images/EmmaSex/Emma_Sex_Pussy_Mask.png")
            subpixel True
            pos (0,-140) #top
            parallel:
                ease 1 ypos -135 #bottom
                ease 1 ypos -140 #top
                repeat
            parallel:
                ease 2 xpos -8 #bottom
                ease 2 xpos 8 #top
                repeat
    # End Legs Sex Idle

image Emma_Sex_Legs_S1:
    # Her Legs in the Sex pose, slow
    contains:
            #Body
            "Emma_Sex_Legs_S"
            subpixel True
            pos (0,-120) #top
            block:
                ease 0.75 ypos -50 #bottom
                pause 0.75
                ease 1.5 ypos -120 #top
                repeat
    contains:
            #Cock
            "Blowcock"      
            subpixel True
            alpha 0.9
            zoom 0.5
            pos (680,400)
            block:
                ease 0.8 ypos 410
                pause 1
                ease 1.2 ypos 400
                repeat
    contains:
            #Overlay
            AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Pussy_Mask")
            subpixel True
            pos (0,-120) #top
            block:
                ease 0.75 ypos -50  #bottom
                pause 0.75
                ease 1.5 ypos -120 #top
                repeat
    # End Legs Sex slow
    
image Emma_Sex_Legs_S2:
    # Her Legs in the Sex pose, fast
    contains:
            #Body
            "Emma_Sex_Legs_S"
            subpixel True
            pos (0,-150) #top
            block:
                ease 0.5 ypos 0 #bottom
                pause 0.5
                ease 1 ypos -150 #top
                repeat
    contains:
            #Cock
            "Blowcock"     
            subpixel True 
            alpha 0.9
            zoom 0.5
            pos (680,400)
            block:
                ease 0.4 ypos 430
                pause 1
                ease 0.6 ypos 400
                repeat
    contains:
            #Overlay
            AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Pussy_Mask")
            subpixel True
            pos (0,-150) #top
            block:
                ease 0.5 ypos 0 #bottom
                pause 0.5
                ease 1 ypos -150 #top
                repeat
    # End Legs Sex fast

image Emma_Sex_Legs_S3:
    # Her Legs in the Sex pose, very fast
    contains:
            #Body
            "Emma_Sex_Legs_S"
            subpixel True
            pos (0,-120) #top
            block:
                ease 0.25 ypos 10 #bottom
                ease 0.5 ypos -120 #top
                repeat
    contains:
            #Cock
            "Blowcock"      
            subpixel True
            alpha 0.9
            zoom 0.5
            pos (680,400)
            block:
                ease 0.2 ypos 430
                ease 0.55 ypos 400
                repeat
    contains:
            #Overlay
            AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Pussy_Mask")
            subpixel True
            pos (0,-120) #top
            block:
                ease 0.25 ypos 10 #bottom
                ease 0.5 ypos -120 #top
                repeat
    # End Legs Sex very fast

image Emma_Sex_Legs_S4:
    # Her Legs in the Sex pose, cumming
    contains:
            #Body
            "Emma_Sex_Legs_S"
            subpixel True
            pos (0,0) #top
            block:
                ease 0.5 ypos 10 #bottom
                ease 1 ypos 0 #top
                repeat
    contains:
            #Cock
            "Blowcock"      
            subpixel True
            alpha 0.9
            zoom 0.5
            pos (680,430)
    contains:
            #Overlay
            AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Pussy_Mask")
            subpixel True
            pos (0,0) #top
            block:
                ease 0.5 ypos 10 #bottom
                ease 1 ypos 0 #top
                repeat
    # End Legs Sex cumming
# Anal / / / / / / Anal / / / / / / Anal / / / / / / Anal / / / / / / Anal / / / / / /    
image Emma_Sex_Legs_A0:
    # Her Legs in the anal pose, idle
    contains:
            #Base Legs
            "Emma_Sex_Legs_A"   
            subpixel True
            pos (0,-138) #top
            block:
                ease 1 ypos -134 #bottom
                ease 1 ypos -138 #top
                repeat
    contains:
            #Cock
            "Blowcock"
            alpha 0.9
            zoom 0.5
            pos (681,420)
    # End Sex Legs Anal Idle

image Emma_Sex_Legs_A1:
    # Her Legs in the anal pose, slow
    contains:
            #Base Legs
            "Emma_Sex_Legs_A"   
            subpixel True
            pos (0,-130) #top
            block:
                ease 4 ypos -80 #bottom
                ease 4 ypos -130 #top
                repeat
    contains:
            #Cock
            "Blowcock"
            alpha 0.9
            zoom 0.5
            pos (681,420)
    contains:
            #Overlay
            AlphaMask("Emma_Sex_Legs_A", "Emma_Sex_Anus_Mask_A1")  
            subpixel True
            pos (0,-130) #top
            block:
                ease 4 ypos -80 #bottom
                ease 4 ypos -130 #top
                repeat          
    # End Sex Legs Anal slow
 
image Emma_Sex_Anus_Mask_A1:
    #mask for the slow anal pose
    contains:        
        contains:
            "images/EmmaSex/Emma_Sex_Anus_Mask.png" 
        contains:
                # spunk
            ConditionSwitch(    
                "'anal' in EmmaX.Spunk", "images/EmmaSex/Emma_Spunk_Anal_Open.png",
                "True", Null(),
                )
        subpixel True
        xzoom 0.5
        xpos  250 
        parallel:
            #8 total
            pause .2
            ease 2.2 xzoom 0.9 #bottom
            ease 0.6 xzoom 0.85 #bottom
            
            ease 0.75 xzoom 0.9 #bottom
            pause 0.5            
            ease 0.75 xzoom 0.85 #bottom
            
            ease 0.6 xzoom 0.9 #bottom
            ease 2.2 xzoom 0.5 #top
            pause .2
            repeat  
        parallel:
            pause .2  
            ease 2.2 xpos 50 #bottom
            ease 0.6 xpos 75 #bottom 125=75%
            
            ease 0.75 xpos 50 #bottom
            pause 0.5
            ease 0.75 xpos 75 #bottom
            
            ease 0.6 xpos 50 #bottom
            ease 2.2 xpos 250 #top
            pause .2
            repeat
    #end animation for mask in slow anal

image Emma_Sex_Legs_A2:
    # Her Legs in the anal pose, fast
    contains:
            #Base Legs
            "Emma_Sex_Legs_A"   
            pos (0,-80) #top
            subpixel True
            block:
                ease 1 ypos 0 #bottom
                ease 1 ypos -80 #top
                repeat
    contains:
            #Cock
            "Blowcock"
            subpixel True
            alpha 0.9
            zoom 0.5
            pos (681,420)
            block:
                ease 1 ypos 430
                ease 1 ypos 400
                repeat
    contains:
            #Overlay
            contains:
                    AlphaMask("Emma_Sex_Legs_A", "images/EmmaSex/Emma_Sex_Anus_Mask.png" )
            contains:
                    # spunk
                ConditionSwitch(    
                    "'anal' in EmmaX.Spunk", "images/EmmaSex/Emma_Spunk_Anal_Open.png",
                    "True", Null(),
                    )   
            subpixel True  
            pos (0,-80) #top
            block:
                ease 1 ypos 0 #bottom
                ease 1 ypos -80 #top
                repeat    
    # End Sex Legs Anal fast
    
image Emma_Sex_Legs_A3:
    # Her Legs in the anal pose, very fast
    contains:
            #Base Legs
            "Emma_Sex_Legs_A"   
            subpixel True
            pos (0,-80) #top
            block:
                ease 0.5 ypos 20 #bottom
                ease 0.5 ypos -80 #top
                repeat
    contains:
            #Cock
            "Blowcock"
            subpixel True
            alpha 0.9
            zoom 0.5
            pos (681,420)
            block:
                ease 0.5 ypos 430
                ease 0.5 ypos 400
                repeat
    contains:
            #Overlay
            contains:
                    AlphaMask("Emma_Sex_Legs_A", "images/EmmaSex/Emma_Sex_Anus_Mask.png" )
            contains:
                    # spunk
                ConditionSwitch(    
                    "'anal' in EmmaX.Spunk", "images/EmmaSex/Emma_Spunk_Anal_Open.png",
                    "True", Null(),
                    )     
            subpixel True
            pos (0,-80) #top
            block:
                ease 0.5 ypos 20 #bottom
                ease 0.5 ypos -80 #top
                repeat 
    # End Sex Legs Anal very fast

image Emma_Sex_Legs_A4:
    # Her Legs in the anal pose, cumming
    contains:
            #Base Legs
            "Emma_Sex_Legs_A"   
            subpixel True
            pos (0,15) #top
            block:
                ease 1 ypos 20 #bottom
                ease 1 ypos 15 #top
                repeat
    contains:
            #Cock
            "Blowcock"
            subpixel True
            alpha 0.9
            zoom 0.5
            pos (681,430)
    contains:
            #Overlay
            contains:
                    AlphaMask("Emma_Sex_Legs_A", "images/EmmaSex/Emma_Sex_Anus_Mask.png" )
            contains:
                    # spunk
                ConditionSwitch(    
                    "'anal' in EmmaX.Spunk", "images/EmmaSex/Emma_Spunk_Anal_Open.png",
                    "True", Null(),
                    )     
            subpixel True
            pos (0,15) #top
            block:
                ease 1 ypos 20 #bottom
                ease 1 ypos 15 #top
                repeat 
    # End Sex Legs Anal cumming
    
image Emma_Sex_Anus_A0:
        #this is the animated stretched anus 
        "images/EmmaSex/Emma_Sex_Anus_Tight.png"
        xpos  0 
        
image Emma_Sex_Anus_A1:                    
        #this is the animated stretched anus 
        contains:
            "images/EmmaSex/Emma_Sex_Anus_Open.png"          
        contains:
                # spunk
            ConditionSwitch(    
                "'anal' in EmmaX.Spunk", "images/EmmaSex/Emma_Spunk_Anal_Under.png",
                "True", Null(),
                )
        subpixel True
        xzoom 0.5
        xpos  250 
        parallel:
            #8 total
            pause .2
            ease 2.2 xzoom 0.9 #bottom
            ease 0.6 xzoom 0.85 #bottom
            
            ease 0.75 xzoom 0.9 #bottom
            pause 0.5            
            ease 0.75 xzoom 0.85 #bottom
            
            ease 0.6 xzoom 0.9 #bottom
            ease 2.2 xzoom 0.5 #top
            pause .2
            repeat  
        parallel:
            pause .2  
            ease 2.2 xpos 50 #bottom
            ease 0.6 xpos 75 #bottom 125=75%
            
            ease 0.75 xpos 50 #bottom
            pause 0.5
            ease 0.75 xpos 75 #bottom
            
            ease 0.6 xpos 50 #bottom
            ease 2.2 xpos 250 #top
            pause .2
            repeat
        #end animation for anus in slow animation
            
image Emma_Sex_Anus_A2:
        #this is the animated stretched anus 
        contains:
            "images/EmmaSex/Emma_Sex_Anus_Open.png"  
        contains:
                # spunk
            ConditionSwitch(    
                "'anal' in EmmaX.Spunk", "images/EmmaSex/Emma_Spunk_Anal_Under.png",
                "True", Null(),
                )
        xpos  0 
      
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Emma_Sex_Launch(Line = "solo"): 
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
        if renpy.showing("Emma_SexSprite"):
            return 
        $ Player.Sprite = 1
        $ Speed = 0
        hide Emma_Sprite      
        if renpy.showing("Emma_BJ_Animation"):
            hide Emma_BJ_Animation
        if renpy.showing("Emma_HJ_Animation"):
            hide Emma_HJ_Animation
        if renpy.showing("Emma_TJ_Animation"):
            hide Emma_TJ_Animation
        
        if EmmaX.Legs or EmmaX.HoseNum() >=5:          #temporary, change or remove when other clothing options are available
            $ EmmaX.Upskirt = 1
        if EmmaX.Panties:       #temporary, change or remove when other clothing options are available
            $ EmmaX.PantiesDown = 1
                    
        show Emma_SexSprite zorder 150:
            pos (575,470)
        with dissolve
        return
    
label Emma_Sex_Reset:
        if not renpy.showing("Emma_SexSprite"):
            return
        $ EmmaX.ArmPose = 2     
        hide Emma_SexSprite  
        call Emma_Hide 
        show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
            alpha 1
            zoom 1 offset (0,0) 
            anchor (0.5, 0.0)
        with dissolve
        $ Speed = 0
        return
label Emma_Doggy_Reset:
        return

# End Emma Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Emma TJ Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Emma TJ annimation element ///////////////////////////////////////////////////////////////////////////                                     Core Emma BJ element
                
image Emma_TJ_Animation:
    #core titjob animation   
    contains:
        ConditionSwitch(                                                              
            # Emma's upper body
            "Player.Sprite", ConditionSwitch(                                                               
                    # If during sex
                    "Speed == 1", "Emma_TJ_Body_1",#slow
                    "Speed == 2", "Emma_TJ_Body_2",#fast
                    "Speed == 3", "Emma_TJ_Body_3",#licking
                    "Speed == 5", "Emma_TJ_Body_5",#cumming
                    "True",       "Emma_TJ_Body_0",#Static
                    ),
            "True","Emma_TJ_Body_0",#Static
            )    
    zoom 1.35 #0.8
    anchor (.5,.5)
    pos (600,605) #(600,705)#height for bj
  
image Emma_TJ_Tits:
    #core titjob breasts   
    contains:
            #base layer
            "images/EmmaSex/Emma_Sex_Tits_TJ.png"
    contains:
            # piercings
        ConditionSwitch(   
            "not EmmaX.Pierce", Null(),
            "EmmaX.Pierce == 'barbell'", ConditionSwitch(   
                    #if it's the ring pericings   
#                    "EmmaX.Chest in ('corset', 'lace bra', 'sports bra')", Null(),  
                    "True", "images/EmmaSex/Emma_Pierce_Barbell_Tits_T.png", 
                    ),    
            "EmmaX.Pierce == 'ring'", ConditionSwitch(   
                    #if it's the ring pericings   
#                    "EmmaX.Chest in ('corset', 'lace bra', 'sports bra')", Null(),  
                    "True", "images/EmmaSex/Emma_Pierce_Ring_Tits_T.png", 
                    ),                    
            "True", Null(), 
            )
    contains:
            #chest clothing layer
        ConditionSwitch(    
            "not EmmaX.Chest", Null(),   # EmmaX.TitsUp = 0
            "EmmaX.Chest == 'sports bra'", "images/EmmaSex/Emma_Sex_Bra_Sports_TJ.png",   # EmmaX.TitsUp = 1
            "EmmaX.Chest == 'lace bra'", "images/EmmaSex/Emma_Sex_Bra_Lace_TJ.png",   # EmmaX.TitsUp = 1
            "True", Null(),   # EmmaX.TitsUp = 0
            )
    contains:
            # piercings over clothes
        ConditionSwitch(   
            "not EmmaX.Pierce or not EmmaX.Chest", Null(),
            "EmmaX.Pierce == 'barbell'", ConditionSwitch(   
                    #if it's the ring pericings   
                    "EmmaX.Chest in ('corset', 'lace bra', 'sports bra')", "images/EmmaSex/Emma_Pierce_Barbell_Tits_TC.png", 
                    "True", Null(),
                    ),    
            "EmmaX.Pierce == 'ring'", ConditionSwitch(   
                    #if it's the ring pericings   
                    "EmmaX.Chest in ('corset', 'lace bra', 'sports bra')", "images/EmmaSex/Emma_Pierce_Ring_Tits_TC.png", 
                    "True", Null(),
                    ),                    
            "True", Null(), 
            )
    contains:
            # spunk on tits
        ConditionSwitch(    
                "'tits' in EmmaX.Spunk", "images/EmmaSex/Emma_Spunk_Titjob_Over.png",
                "True", Null(),
                ) 

#image Emma_TJ_HairBack:
#    #Hair underlay
#    "Emma_BJ_HairBack"
#    zoom 0.41
#    anchor (0.5, 0.5)
#    pos (505,250)
            
#image Emma_TJ_Head:
#    #Hair underlay
#    "Emma_BJ_Head"
#    zoom 0.41
#    anchor (0.5, 0.5)
#    pos (505,250)

#  TJ animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_TJ_Body_0:                                                                        
    #Her Body in the TJ pose, idle
    contains:
            #Hair underlay
            "Emma_BJ_HairBack"
            zoom 0.41
            anchor (0.5, 0.5)
            pos (505,260) #bottom
            subpixel True
            block:
                ease 2.4 ypos 250 #top
                ease 1.6 ypos 260 #bottom
                repeat   
    contains:       
            #base body
            "Emma_Sex_Torso"           
            pos (0,0) #bottom
            subpixel True
            block:
                ease 2 ypos -5 #top
                ease 2 ypos 5 #bottom
                repeat   

    contains:
            #head
            "Emma_BJ_Head"
            zoom 0.41
            anchor (0.5, 0.5)
            pos (505,260) #bottom  #280
            subpixel True
            block:
                ease 2.4 ypos 250 #top
                ease 1.6 ypos 260 #bottom
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
            rotate -3
            parallel:
                pause 0.1
                ease 1.6 ypos 170 #top
                pause 0.1
                ease 1.4 ypos 150 #bottom
                repeat
            parallel:
                pause 0.1
                ease 1.6 rotate 4 #top
                pause 0.1
                ease 1.4 rotate -3 #bottom
                repeat
    contains:
            #tits
            "Emma_TJ_Tits"        
            pos (290,270) #bottom
            rotate -3
            subpixel True
            size (1000,1000)
            anchor (500,500)
            parallel:
                ease 1.5 rotate 4 #top
                pause 0.1
                ease 1.5 rotate -3 #bottom
                pause 0.1
                repeat
    #End TJ animation Speed 1


image Emma_TJ_Body_1:                                                                        
    #Her Body in the TJ pose, slow
    contains:
            #Hair underlay
            "Emma_BJ_HairBack"
            zoom 0.41
            anchor (0.5, 0.5)
            pos (505,250) #bottom
            subpixel True
            block:
                pause 0.2
                ease 1.4 ypos 240 #top
                pause 0.3
                ease 0.6 ypos 250 #bottom
                repeat
    contains:       
            #base body
            "Emma_Sex_Torso"           
            pos (0,0) #bottom
            subpixel True
            block:
                pause 0.2
                ease 1.4 ypos -20 #top
                pause 0.3
                ease 0.6 ypos 0 #bottom
                repeat
    contains:
            #zero's cock
            "Blowcock" 
            subpixel True
            pos (640,150) #bottom 
            #pos (640,90) #height for bj
            anchor (0.5,0.5)
            zoom 0.4                
            block:
                pause 0.2
                ease 1.4 ypos 140 #top
                pause 0.3
                ease 0.6 ypos 150 #bottom
                repeat  
    contains:
            #head
            "Emma_BJ_Head"
            zoom 0.41
            anchor (0.5, 0.5)
            pos (505,250) #bottom  
            subpixel True
            block:
                pause 0.2
                ease 1.4 ypos 240 #top
                pause 0.3
                ease 0.6 ypos 250 #bottom
                repeat             
    contains:
            #tits
            "Emma_TJ_Tits"        
            pos (290,290) #bottom
            rotate 0
            subpixel True
            size (1000,1000)
            anchor (500,500)
            parallel:
                ease 1.5 ypos 230 #top
                pause 0.3
                ease 0.7 ypos 290 #bottom
                repeat
            parallel:
                ease .5 rotate 1 #topS
                ease .5 rotate -1 #bottom
                ease .7 rotate 1 #bottom
                ease .8 rotate 0 #bottom
                repeat
    #End TJ animation Speed 1
    

image Emma_TJ_Body_2:                                                                        
    #Her Body in the TJ pose, fast
    contains:
            #Hair underlay
            "Emma_BJ_HairBack"
            zoom 0.41
            anchor (0.5, 0.5)
            pos (505,250) #bottom
            subpixel True
            block:
                pause 0.1
                ease .6 ypos 250 #top
                ease .3 ypos 270 #bottom
                repeat
    contains:       
            #base body
            "Emma_Sex_Torso"           
            pos (0,0) #bottom
            subpixel True
            block:
                pause .1
                ease .5 ypos -20 #top
                ease .3 ypos 15 #bottom
                pause .1
                repeat
    contains:
            #zero's cock
            "Blowcock" 
            subpixel True
            pos (640,150) #bottom 
            #pos (640,90) #height for bj
            anchor (0.5,0.5)
            zoom 0.4                
            block:
                pause .05
                ease .65 ypos 140 #top
                ease .3 ypos 150 #bottom
                repeat  
    contains:
            #head
            "Emma_BJ_Head"
            zoom 0.41
            anchor (0.5, 0.5)
            pos (505,250) #bottom  
            subpixel True
            block:
                pause 0.1
                ease .6 ypos 250 #top
                ease 0.3 ypos 270 #bottom
                repeat             
    contains:
            #tits
            "Emma_TJ_Tits"        
            pos (290,290) #bottom
            rotate 0
            subpixel True
            size (1000,1000)
            anchor (500,500)
            parallel:
                ease .6 ypos 220 #top
                ease .3 ypos 300 #bottom
                pause .1
                repeat
    #End TJ animation Speed 2
    
image Emma_TJ_Body_3:                                                                        
    #Her Body in the TJ pose, slow with licking
    contains:
            #Hair underlay
            "Emma_BJ_HairBack"
            zoom 0.41
            anchor (0.5, 0.5)
            pos (500,290) #bottom
            subpixel True
            block:
                ease 1.5 ypos 260 #top
                pause .7
                ease .3 ypos 290 #bottom
                pause .5
                repeat   
    contains:       
            #base body
            "Emma_Sex_Torso"           
            pos (0,0) #bottom
            subpixel True
            block:
                ease 1.6 ypos -20 #top
                pause .7
                ease .2 ypos 0 #bottom
                pause .5
                repeat   
    contains:
            #head
            "Emma_BJ_Head"
            zoom 0.41
            anchor (0.5, 0.5)
            pos (500,290) #bottom  #280
            subpixel True
            block:
                ease 1.5 ypos 260 #top
                pause .7
                ease .3 ypos 290 #bottom
                pause .5
                repeat   
    contains:
            #zero's cock
            "Blowcock" 
            subpixel True
            pos (640,130) #bottom #150
            anchor (0.5,0.5)
            zoom 0.4                
            block:
                pause .2
                ease 1.6 ypos 120 #top
                pause .4
                ease .3 ypos 130 #bottom
                pause .5
                repeat            
    contains:
            #tits
            "Emma_TJ_Tits"        
            pos (290,290) #bottom
            rotate 0
            subpixel True
            size (1000,1000)
            anchor (500,500)
            parallel:
                ease 1.8 ypos 240 #top
                pause .3
                ease .4 ypos 290 #bottom
                pause .5
                repeat   
    #End TJ animation Speed 3

            
                
image Emma_TJ_Body_5:                                                                        
    #Her Body in the TJ pose, slow with licking
    contains:
            #Hair underlay
            "Emma_BJ_HairBack"
            zoom 0.41
            anchor (0.5, 0.5)
            pos (500,290) #bottom
            subpixel True
            block:
                ease 1.5 ypos 288 #top
                pause .7
                ease .3 ypos 290 #bottom
                pause .5
                repeat   
    contains:       
            #base body
            "Emma_Sex_Torso"           
            pos (0,0) #bottom
            subpixel True
            block:
                ease 1.3 ypos -5 #top
                pause .7
                ease .5 ypos 0 #bottom
                pause .5
                repeat   
    contains:
            #head
            "Emma_BJ_Head"
            zoom 0.41
            anchor (0.5, 0.5)
            pos (500,290) #bottom  #280
            subpixel True
            block:
                ease 1.5 ypos 288 #top
                pause .7
                ease .3 ypos 290 #bottom
                pause .5
                repeat   
    contains:
            #zero's cock
            "Blowcock" 
            subpixel True
            pos (640,130) #bottom #150
            anchor (0.5,0.5)
            zoom 0.4                
            block:
                pause .2
                ease 1.6 ypos 128 #top
                pause .4
                ease .3 ypos 130 #bottom
                pause .5
                repeat            
    contains:
            #tits
            "Emma_TJ_Tits"        
            pos (290,290) #bottom
            rotate 0
            subpixel True
            size (1000,1000)
            anchor (500,500)
            parallel:
                ease 1.3 ypos 270 #top
                pause .3
                ease .9 ypos 290 #bottom
                pause .5
                repeat   
    #End TJ animation Speed 5
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Emma_TJ_Launch(Line = 0):    # The sequence to launch the Emma Titfuck animations   
    if renpy.showing("Emma_TJ_Animation"):
        return
    call Emma_Hide
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
        alpha 1
        ease 1 zoom 2 xpos 550 yoffset 50 #offset (-100,50) 
    if Taboo: # Emma gets started. . .
        if len(Present) >= 2:
            if Present[0] != EmmaX:
                    "[EmmaX.Name] looks back at [Present[0].Name] to see if she's watching."
            elif Present[1] != EmmaX:
                    "[EmmaX.Name] looks back at [Present[1].Name] to see if she's watching."
        else:
                    "[EmmaX.Name] looks around to see if anyone can see her."
            
#    if EmmaX.Chest and EmmaX.Over:
#        "She throws off her [EmmaX.Over] and her [EmmaX.Chest]."                
#    elif EmmaX.Over:
#        "She throws off her [EmmaX.Over], baring her breasts underneath."
#    elif EmmaX.Chest:
#        "She tugs off her [EmmaX.Chest] and throws it aside."
#    $ EmmaX.Over = 0
#    $ EmmaX.Chest = 0
    $ EmmaX.ArmPose = 0
    
    call Emma_First_Topless        
    
    if not EmmaX.Tit and Line == "L": #first time
        if not EmmaX.Chest and not EmmaX.Over:
            "As you pull out your cock, [EmmaX.Name] cautiously places it between her breasts and starts to rub them up and down the shaft."
        elif EmmaX.Chest and not EmmaX.Over:
            "As you pull out your cock, [EmmaX.Name] cautiously places it under her [EmmaX.Chest], between her breasts and starts to rub them up and down the shaft."
        elif EmmaX.Chest and EmmaX.Over:
            "As you pull out your cock, [EmmaX.Name] cautiously places it under her [EmmaX.Over], between her breasts and starts to rub them up and down the shaft."
        else:
            "As you pull out your cock, [EmmaX.Name] cautiously places it under her clothes, between her breasts and starts to rub them up and down the shaft."
    elif Line == "L": #any other time
        if not EmmaX.Chest and not EmmaX.Over:
            "As you pull out your cock, [EmmaX.Name] places it between her breasts and starts to rub them up and down the shaft."
        elif EmmaX.Chest and not EmmaX.Over:
            "As you pull out your cock, [EmmaX.Name] places it under her [EmmaX.Chest], between her breasts and starts to rub them up and down the shaft."
        elif EmmaX.Chest and EmmaX.Over:
            "As you pull out your cock, [EmmaX.Name] places it under her [EmmaX.Over], between her breasts and starts to rub them up and down the shaft."
        else:
            "As you pull out your cock, [EmmaX.Name] places it under her clothes, between her breasts and starts to rub them up and down the shaft."    
    else:
            "[EmmaX.Name] wraps her tits around your cock."
#    hide Emma_Sprite    
    show blackscreen onlayer black with dissolve    
    show Emma_Sprite zorder EmmaX.Layer:
        alpha 0
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "titjob"
    show Emma_TJ_Animation zorder 150 
    $ Player.Sprite = 1
    hide blackscreen onlayer black with dissolve
    return
    
label Emma_TJ_Reset: # The sequence to the Emma animations from Titfuck to default
    if not renpy.showing("Emma_TJ_Animation"):
        return
#    hide Emma_TJ_Animation
    call Emma_Hide 
    $ Player.Sprite = 0
    
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
        zoom 2 xpos 550 yoffset 50 #offset (-100,50)  #zoom 2 offset (-100,50)
    show Emma_Sprite zorder EmmaX.Layer:
        alpha 1
        ease 1 zoom 1.5 xpos 500 yoffset 50
        pause .5
        ease .5 zoom 1 xpos EmmaX.SpriteLoc yoffset 0
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
        alpha 1
        zoom 1 offset (0,0) xpos EmmaX.SpriteLoc 
        
    "[EmmaX.Name] pulls back"
    return
            
# End Emma TJ Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Emma Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Emma BJ element ///////////////////////////////////////////////////////////////////////////                                     Core Emma BJ element
#Emma BJ Over Sprite Compositing

        
image Emma_BJ_Animation:#BJ_NewTest:                                                                #core BJ animation   
    LiveComposite(    
        (858,928),  
        (-270,-160), ConditionSwitch( #-270,-160                                                                
            # Emma's hair backside 
            "Speed == 0", At("Emma_BJ_HairBack", Emma_BJ_Head_0()),               #Static
            "Speed == 1", At("Emma_BJ_HairBack", Emma_BJ_Head_1()),               #Licking
            "Speed == 2", At("Emma_BJ_HairBack", Emma_BJ_Head_2()),               #Heading
            "Speed == 3", At("Emma_BJ_HairBack", Emma_BJ_Head_3()),               #Sucking
            "Speed == 4", At("Emma_BJ_HairBack", Emma_BJ_Head_4()),               #Deepthroat
            "Speed == 5", At("Emma_BJ_HairBack", Emma_BJ_Head_5()),               #Cumming High
            "Speed == 6", At("Emma_BJ_HairBack", Emma_BJ_Head_6()),               #Cumming Deep
            "True", Null(),
            ),  
        (-20,270), ConditionSwitch(                                                                 
            # Emma's body, everything below the chin
            "Speed == 0", At("Emma_BJ_Backdrop", Emma_BJ_Body_0()),           #Static
            "Speed == 1", At("Emma_BJ_Backdrop", Emma_BJ_Body_1()),           #Licking
            "Speed == 2", At("Emma_BJ_Backdrop", Emma_BJ_Body_2()),           #Heading
            "Speed == 3", At("Emma_BJ_Backdrop", Emma_BJ_Body_3()),           #Sucking
            "Speed == 4", At("Emma_BJ_Backdrop", Emma_BJ_Body_4()),           #Deepthroat
            "Speed == 5", At("Emma_BJ_Backdrop", Emma_BJ_Body_5()),           #Cumming High
            "Speed == 6", At("Emma_BJ_Backdrop", Emma_BJ_Body_6()),           #Cumming Deep
            "True", Null(),
            ),    
        (-270,-160), ConditionSwitch(                                                                 
            # Emma's head Underlay
            "Speed == 0", At("Emma_BJ_Head", Emma_BJ_Head_0()),               #Static
            "Speed == 1", At("Emma_BJ_Head", Emma_BJ_Head_1()),               #Licking
            "Speed == 2", At("Emma_BJ_Head", Emma_BJ_Head_2()),               #Heading
            "Speed == 3", At("Emma_BJ_Head", Emma_BJ_Head_3()),               #Sucking
            "Speed == 4", At("Emma_BJ_Head", Emma_BJ_Head_4()),               #Deepthroat
            "Speed == 5", At("Emma_BJ_Head", Emma_BJ_Head_5()),               #Cumming High
            "Speed == 6", At("Emma_BJ_Head", Emma_BJ_Head_6()),               #Cumming Deep
            "True", Null(),
            ),   
        (0,0), ConditionSwitch(                                                                 
            # Cock
            "Speed == 0", At("Blowcock", Emma_BJ_Cock_0()),                    #Static
            "Speed == 1", At("Blowcock", Emma_BJ_Cock_1()),                    #Licking                        
            "Speed >= 2", At("Blowcock", Emma_BJ_Cock_2()),                    #Heading+                        
#            "Speed == 2", At("Blowcock", Emma_BJ_Cock_2()),                    #Heading
#            "Speed == 3", At("Blowcock", Emma_BJ_Cock_2()),                    #Sucking                     
#            "Speed == 4", At("Blowcock", Emma_BJ_Cock_2()),                    #Deepthroat
            "True", Null(),
            ),    
        (-270,-160), ConditionSwitch(                                                                 
            # the masked overlay for when her head overlaps the cock
            "Speed < 3", Null(), 
            "Speed == 3", At(AlphaMask("Emma_BJ_Head", "Emma_BJ_MouthSuckingMask"), Emma_BJ_Head_3()), #Sucking
            "Speed == 4", At(AlphaMask("Emma_BJ_Head", "Emma_BJ_MouthSuckingMask"), Emma_BJ_Head_4()), #Deepthroat
            "Speed == 6", At(AlphaMask("Emma_BJ_Head", "Emma_BJ_MouthSuckingMask"), Emma_BJ_Head_6()), #Cumming Deep
            "True", Null(),
            ),    
        (-270,-160), ConditionSwitch(                                                                 
            # same as above, but for the heading animation
            "Speed == 2", At(AlphaMask("Emma_BJ_Head", "Emma_BJ_MaskHeadingComposite"), Emma_BJ_Head_2()), #Heading
            "Speed == 5", At(AlphaMask("Emma_BJ_Head", "Emma_BJ_MaskHeadingComposite"), Emma_BJ_Head_5()), #Cumming High
            "True", Null(),
            ),            
        (325,490), ConditionSwitch(                                                                
            # the over part of spunk
            "Speed < 3 or 'mouth' not in EmmaX.Spunk", Null(),
            "Speed == 3", At("EmmaSuckingSpunk", Emma_BJ_Head_3()), #Sucking
            "Speed == 4", At("EmmaSuckingSpunk", Emma_BJ_Head_4()), #Deepthroat
            "Speed == 6", At("EmmaSuckingSpunk", Emma_BJ_Head_6()), #Cumming Deep
            "True", Null(),
            ),    
        (325,490), ConditionSwitch(         #(325,490)                                                        
            # same as above, but for the heading animation
            "Speed == 2 and 'mouth' in EmmaX.Spunk", At("Emma_BJ_MaskHeadingSpunk", Emma_BJ_Head_2()), #Heading
#            "Speed == 5 and 'mouth' in EmmaX.Spunk", At("Emma_BJ_MaskHeadingSpunkB", Emma_BJ_Head_5()), #Cumming High
            "True", Null(),
            ),   
        )
    zoom .55
    anchor (.5,.5)
    
image Emma_BJ_HairBack:
    #Hair underlay
    ConditionSwitch(                                 
            "EmmaX.Water or EmmaX.Hair == 'wet'", Null(),
            "True", "images/EmmaBJFace/Emma_BJ_Hair_Wave_Back.png", 
            ),
    zoom 1.4
    anchor (0.5, 0.5)
    
image Emma_BJ_Backdrop:
    contains:                                                                   
            #blanket     
            ConditionSwitch(      
                "'blanket' in EmmaX.RecentActions", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
                "True", Null(),
                ),                  
            zoom 2
            anchor (.5,.5)
            pos (350,600)
    contains:
            #body backdrop
            "Emma_Sex_Torso"
            zoom 2.5
            anchor (.5,.5)
            pos (160,750)
#    zoom 1.5 
#    offset (-300,-200)
            
image Emma_BJ_Head:                                                                            #These are all the details of the face
    LiveComposite(    
        (858,928), 
         (0,0), ConditionSwitch(                                                                 
            #Hair behind face above body
            "EmmaX.Water or EmmaX.Hair == 'wet'", "images/EmmaBJFace/Emma_BJ_Hair_Wet_Mid.png",
            "True", "images/EmmaBJFace/Emma_BJ_Hair_Wave_Mid.png",
            ),
        (0,0), ConditionSwitch(
            # Basic Face layer
            "Speed <= 2 or Speed == 5 or not renpy.showing('Emma_BJ_Animation')", ConditionSwitch( 
                    # If the animation isn't sucking, or if not in BJ pose
                    "EmmaX.Blush", "images/EmmaBJFace/Emma_BJ_FaceClosed_Blush.png",              
                    "True", "images/EmmaBJFace/Emma_BJ_FaceClosed.png",
                    ),  
            "EmmaX.Blush", "images/EmmaBJFace/Emma_BJ_FaceOpen_Blush.png",              
            "True", "images/EmmaBJFace/Emma_BJ_FaceOpen.png"
            ),           
        (0,0), ConditionSwitch(                                                                         
            #Mouth
#            "(Speed == 2 or Speed == 5) and renpy.showing('Emma_BJ_Animation')", ConditionSwitch( 
#                    # If the Heading animation is active
##                    "EmmaX.Blush", "images/EmmaBJFace/Emma_BJ_FaceClosed_Blush.png",              
##                    "True", "images/EmmaBJFace/Emma_BJ_FaceClosed.png"
#                    ),  
            "Speed and renpy.showing('Emma_BJ_Animation')", ConditionSwitch( 
                    # If in sucking position
                    "Speed == 1", "images/EmmaBJFace/Emma_BJ_Mouth_Tongue.png",  #licking
                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", "images/EmmaBJFace/Emma_BJ_Mouth_Sucking.png", #sucking
                    "Speed == 4", "images/EmmaBJFace/Emma_BJ_Mouth_Sucking.png", #deepthroat     
                    "Speed == 6", "images/EmmaBJFace/Emma_BJ_Mouth_Sucking.png", #cumming    
                    ),  
            "Speed == 3 and renpy.showing('Emma_TJ_Animation')", "images/EmmaBJFace/Emma_BJ_Mouth_Tongue.png",
            "EmmaX.Mouth == 'normal'", "images/EmmaBJFace/Emma_BJ_Mouth_Smile.png",
            "EmmaX.Mouth == 'lipbite'", "images/EmmaBJFace/Emma_BJ_Mouth_Lipbite.png",
            "EmmaX.Mouth == 'sucking'", "images/EmmaBJFace/Emma_BJ_Mouth_Sucking.png",            
            "EmmaX.Mouth == 'kiss'", "images/EmmaBJFace/Emma_BJ_Mouth_Kiss.png",
            "EmmaX.Mouth == 'sad'", "images/EmmaBJFace/Emma_BJ_Mouth_Sad.png",
            "EmmaX.Mouth == 'smile'", "images/EmmaBJFace/Emma_BJ_Mouth_Smile.png",  
            "EmmaX.Mouth == 'smirk'", "images/EmmaBJFace/Emma_BJ_Mouth_Smirk.png",           
            "EmmaX.Mouth == 'grimace'", "images/EmmaBJFace/Emma_BJ_Mouth_Smile.png",
            "EmmaX.Mouth == 'surprised'", "images/EmmaBJFace/Emma_BJ_Mouth_Surprised.png",          
            "EmmaX.Mouth == 'tongue'", "images/EmmaBJFace/Emma_BJ_Mouth_Tongue.png",    
            "True", "images/EmmaBJFace/Emma_BJ_Mouth_Smile.png",
            ),       
        (428,605), ConditionSwitch(   
            # Heading Mouth
#            "Speed == 2 and Trigger == 'blow'", At("Emma_BJ_MouthHeading", Emma_BJ_MouthAnim()),  #heading 
            "not renpy.showing('Emma_BJ_Animation')", Null(),                       #heading
            "Speed == 2", At("Emma_BJ_MouthHeading", Emma_BJ_MouthAnim()),  #heading 
            "Speed == 5", At("Emma_BJ_MouthHeading", Emma_BJ_MouthAnimC()), #cumming high    
            "True", Null(),
            ),  
        
        (0,0), ConditionSwitch(                                                                         
            #Spunk layer
            "'mouth' not in EmmaX.Spunk", Null(), 
            "Speed and renpy.showing('Emma_BJ_Animation')", ConditionSwitch( 
                    # If in sucking position
                    "Speed == 1", "images/EmmaBJFace/Emma_BJ_Spunk_Tongue.png",  #licking
                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", "images/EmmaBJFace/Emma_BJ_Spunk_SuckingUnder.png", #sucking
                    "Speed == 4", "images/EmmaBJFace/Emma_BJ_Spunk_SuckingUnder.png", #deepthroat     
                    "Speed == 6", "images/EmmaBJFace/Emma_BJ_Spunk_SuckingUnder.png", #cumming    
                    ),  
            "EmmaX.Mouth == 'normal'", "images/EmmaBJFace/Emma_BJ_Spunk_Smile.png",
            "EmmaX.Mouth == 'lipbite'", "images/EmmaBJFace/Emma_BJ_Spunk_Lipbite.png",
            "EmmaX.Mouth == 'kiss'", "images/EmmaBJFace/Emma_BJ_Spunk_Kiss.png",
            "EmmaX.Mouth == 'sad'", "images/EmmaBJFace/Emma_BJ_Spunk_Sad.png",
            "EmmaX.Mouth == 'smile'", "images/EmmaBJFace/Emma_BJ_Spunk_Smile.png", 
            "EmmaX.Mouth == 'smirk'", "images/EmmaBJFace/Emma_BJ_Spunk_Smirk.png",
            "EmmaX.Mouth == 'surprised'", "images/EmmaBJFace/Emma_BJ_Spunk_Surprised.png",
            "EmmaX.Mouth == 'tongue'", "images/EmmaBJFace/Emma_BJ_Spunk_Tongue.png",
            "EmmaX.Mouth == 'sucking'", "images/EmmaBJFace/Emma_BJ_Spunk_SuckingUnder.png",
            "True", "images/EmmaBJFace/Emma_BJ_Spunk_Smile.png",
            ),       
        (0,0), ConditionSwitch(                                                                         
            #Brows
            "EmmaX.Brows == 'normal'", "images/EmmaBJFace/Emma_BJ_Brows_Normal.png",
            "EmmaX.Brows == 'angry'", "images/EmmaBJFace/Emma_BJ_Brows_Angry.png",
            "EmmaX.Brows == 'sad'", "images/EmmaBJFace/Emma_BJ_Brows_Sad.png",
            "EmmaX.Brows == 'surprised'", "images/EmmaBJFace/Emma_BJ_Brows_Surprised.png",        
            "EmmaX.Brows == 'confused'", "images/EmmaBJFace/Emma_BJ_Brows_Confused.png",
            "True", "images/EmmaBJFace/Emma_BJ_Brows_Normal.png",
            ),
        (0,0), "Emma BJ Blink",                                                                
            #Eyes
        (0,0), ConditionSwitch(                                                                 
            #cum on the face
            "'facial' in EmmaX.Spunk", "images/EmmaBJFace/Emma_BJ_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                 
            #Hair overlay
            "EmmaX.Water or EmmaX.Hair == 'wet'", "images/EmmaBJFace/Emma_BJ_Hair_Wet_Top.png",
            "True", "images/EmmaBJFace/Emma_BJ_Hair_Wave_Top.png",
            ),
#        (0,0), ConditionSwitch(                                                                 
#            #Hair water overlay
#            "not EmmaX.Water", Null(),            
#            "Speed > 2", "images/EmmaBJFace/Emma_BJ_Wet_HeadOpen.png",         
#            "True", "images/EmmaBJFace/Emma_BJ_Wet_HeadClosed.png",
#            ),        
#        (0,0), ConditionSwitch(                                                                 
#            #cum on the hair
#            "'hair' in EmmaX.Spunk", "images/EmmaBJFace/Emma_BJ_Spunk_Hair.png",
#            "True", Null(),
#            ),
        )
    zoom 1.4
    anchor (0.5, 0.5)

image Emma BJ Blink:                                                                           
        #eyeblinks
        ConditionSwitch(
            "EmmaX.Eyes == 'normal'", "images/EmmaBJFace/Emma_BJ_Eyes_Sexy.png",  
            "EmmaX.Eyes == 'sexy'", "images/EmmaBJFace/Emma_BJ_Eyes_Sexy.png",  
            "EmmaX.Eyes == 'closed'", "images/EmmaBJFace/Emma_BJ_Eyes_Closed.png",
            "EmmaX.Eyes == 'surprised'", "images/EmmaBJFace/Emma_BJ_Eyes_Surprised.png",
            "EmmaX.Eyes == 'side'", "images/EmmaBJFace/Emma_BJ_Eyes_Side.png",
            "EmmaX.Eyes == 'stunned'", "images/EmmaBJFace/Emma_BJ_Eyes_Surprised.png",
            "EmmaX.Eyes == 'down'", "images/EmmaBJFace/Emma_BJ_Eyes_Down.png",
            "EmmaX.Eyes == 'manic'", "images/EmmaBJFace/Emma_BJ_Eyes_Surprised.png",
            "EmmaX.Eyes == 'squint'", "images/EmmaBJFace/Emma_BJ_Eyes_Squint.png",
            "True", "images/EmmaBJFace/Emma_BJ_Eyes_Sexy.png",  
            ),
        choice:
            3.5
        choice:
            3.25
        choice:
            3    
        "images/EmmaBJFace/Emma_BJ_Eyes_Closed.png"
        .25
        repeat

image Emma_BJ_MouthHeading:                                          
    #the mouth used for the heading animations
    contains:
        "images/EmmaBJFace/Emma_BJ_Mouth_Sucking.png"        
        zoom 1.4
        anchor (0.50,0.65)  #(0.50,0.65) 
        
image Emma_BJ_MouthSuckingMask:                                          
    #the mask used for sucking animations
    contains:
        "images/EmmaBJFace/Emma_BJ_Mouth_SuckingMask.png"
        zoom 1.4
#    contains: #see if this works, if not remove it
#        ConditionSwitch(
#            "'mouth' not in EmmaX.Spunk", Null(),  
#            "Speed != 2 and Speed != 5", Null(),            
#            "True", "images/EmmaBJFace/Emma_BJ_Spunk_SuckingOver.png",            
#            )   
#        zoom 1.4
        
image Emma_BJ_MaskHeading:                                           
    #the mask used for the heading image 
    contains:
        "images/EmmaBJFace/Emma_BJ_Mouth_SuckingMask.png"
        offset (-380,-595)

image Emma_BJ_MaskHeadingComposite:                                  
    #The composite for the heading mask that goes over the face
    LiveComposite(    
        (858,928),
        (300,462), ConditionSwitch(            
            "Speed == 2", At("Emma_BJ_MaskHeading", Emma_BJ_MouthAnim()),   
            "Speed == 5", At("Emma_BJ_MaskHeading", Emma_BJ_MouthAnimC()),      
            "True", Null(),
            ),  
        )
    zoom 1.8
    
image Emma_BJ_MaskHeadingSpunk:                                  
    #The composite for the heading mask that goes over the face
    contains:
#            "EmmaSuckingSpunk"
            "images/EmmaBJFace/Emma_BJ_Spunk_SuckingOver.png"
            subpixel True
            anchor (0.5, 0.65)
            zoom 0.58 #0.58 = top of heading, 0.66 = crown, 0.60 = valley, 0.68 = base      
            block: #total time 1.0 down, 1.5 back up 2.5 total
                pause .20
                easeout .15 zoom 0.66
                linear .15 zoom 0.60
                easein .25 zoom 0.68 
                pause .25                           
                #1.0s to this point
                pause .40            
                easeout .40 zoom 0.60
                linear .10 zoom 0.66
                easein .30 zoom 0.58 
                pause .30                           
                #1.5s to this point            
                repeat
#    contains:
#            At("EmmaSuckingSpunk", Emma_BJ_MouthAnim())
    zoom 2.5 #1.8
    yoffset 210#130
            
image EmmaSuckingSpunk:
    contains:
        "images/EmmaBJFace/Emma_BJ_Spunk_SuckingOver.png"
        zoom 1.4
        anchor (0.5, 0.5)

            
transform Emma_BJ_MouthAnim():                                       
        #The animation for the heading mouth
        subpixel True
        zoom 0.58 #0.58 = top of heading, 0.66 = crown, 0.60 = valley, 0.68 = base      
        block: #total time 1.0 down, 1.5 back up 2.5 total
            pause .20
            easeout .15 zoom 0.66
            linear .15 zoom 0.60
            easein .25 zoom 0.68 
            pause .25                           
            #1.0s to this point
            pause .40            
            easeout .40 zoom 0.60
            linear .10 zoom 0.66
            easein .30 zoom 0.58 
            pause .30                           
            #1.5s to this point            
            repeat


#            pause .40            
#            easein .40 zoom 0.69 #0.87
#            linear .10 zoom 0.7 #0.9
#            easeout .45 zoom 0.65 #0.70 
#            pause .15                           
#            #1.5s to this point
#            easein .25 zoom 0.7#0.9
#            linear .10 zoom 0.69#0.87
#            easeout .30 zoom 0.7#0.9   
#            pause .35                           
#            #1.0s to this point
#            repeat
   
transform Emma_BJ_Head_2():                                 
    #The heading animation for her face
    subpixel True 
    offset (0,-40)     #top (0,-40), -20 is crown, 0 is mid
    block:
        ease 1 yoffset 40           #bottom         
        ease 1.5 offset (0,-40)     #top  
        repeat


#        ease 1 yoffset 35           #bottom         
#        ease 1.5 offset (0,-40)     #top  
#        repeat

transform Emma_BJ_MouthAnimC():                                       
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


#Cock Animations for Emma's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
transform Emma_BJ_Cock_0():                            
    #The angled static animation for the cock for starting
    anchor (.5,.5)
    rotate -10
transform Emma_BJ_Cock_1():                            
    #The licking animation for the cock
    subpixel True
    anchor (.5,.5)
    ease 0.5 rotate 0
    block:
        ease 2 rotate -5 #410
        pause .5
        ease 2.5 rotate 0
        repeat        
transform Emma_BJ_Cock_2():                            
    #The vertical static animation for the cock used in most sucking
    anchor (.5,.5)
    rotate 0
    alpha 1
#End Cock Animations for Emma's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Head and Body Animations for Emma's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /               
transform Emma_BJ_Head_0():                                
    #The starting animation for her face
    subpixel True 
    ease 1.5 offset (0,0)    
transform Emma_BJ_Body_0():                            
    #The starting animation for her body
    subpixel True 
    ease 1.5 offset (0,0)
    

transform Emma_BJ_Head_1():                                
    #The licking animation for her face
    subpixel True 
    ease 0.5 offset (0,-35)  #top
    block:
        ease 2.5 offset (25,100) #bottom
        ease 2 offset (0,-35)  #top
        pause .5
        repeat
transform Emma_BJ_Body_1():                             
    #The licking animation for her body
    subpixel True 
    ease 0.5 offset (0,-35)  #top
    block:
        ease 2.5 offset (30,90) #bottom 25,50
        ease 2 offset (0,-35)  #top
        pause .5
        repeat
        
#transform Emma_BJ_Head_2():                                 
#    #The heading animation for her face
#    subpixel True 
#    offset (0,-40)     #top 
#    block:
#        ease 1 yoffset 35           #bottom         
#        ease 1.5 offset (0,-40)     #top  
#        repeat
##        ease 1 yoffset 35           #bottom         
##        ease 1.5 offset (0,-40)     #top  
##        repeat
            
transform Emma_BJ_Body_2():                            
    #The heading animation for her body
    subpixel True 
    offset (0,-40)     #top 
    block:
        ease 1 yoffset 15           #bottom         
        ease 1.5 offset (0,-40)     #top  
        repeat
        
transform Emma_BJ_Head_3():                                
    #The sucking animation for her face
    subpixel True
    ease 0.5 offset (0,50) 
    block:
        ease 1 yoffset 120 #100
        ease 1.5 offset (0,50) 
        repeat    
transform Emma_BJ_Body_3():                            
    #The sucking animation for her body
    subpixel True 
    ease 0.5 offset (0,50)  
    block:
        ease 1 yoffset 100 #80      #bottom
        ease 1.5 offset (0,50) #top
        repeat
    
transform Emma_BJ_Head_4():                                   
    #The deep animation for her face
    ease .5 offset (0,100) 
    block:
        subpixel True
        ease 1 yoffset 300
        pause .5
        ease 2 yoffset 100  
        repeat        
transform Emma_BJ_Body_4():                               
    #The deep animation for her body
    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1.2 yoffset 250
        pause .5
        ease 1.8 yoffset 100   
        repeat    

transform Emma_BJ_Head_5():                                 
    #The heading cumming animation for her face
    subpixel True 
    offset (0,-30)     #top 
    block:
        ease 1 yoffset -20           #bottom         
        ease 1.5 offset (0,-30)     #top  
        repeat
transform Emma_BJ_Body_5():                            
    #The heading cumming animation for her body
    subpixel True 
    offset (0,-30)     #top 
    block:
        ease 1 yoffset -20           #bottom         
        ease 1.5 offset (0,-30)     #top  
        repeat        
        
transform Emma_BJ_Head_6():                                   
    #The deep cumming animation for her face
    ease .5 offset (0,230) 
    block:
        subpixel True
        ease 1 yoffset 250
        pause .5
        ease 2 yoffset 230  
        repeat        
transform Emma_BJ_Body_6():                               
    #The deep cumming animation for her body
    ease .5 offset (0,190)
    block:
        subpixel True
        ease 1.2 yoffset 200
        pause .5
        ease 1.8 yoffset 190   
        repeat    
        

#transform Emma_BJ_Static():                                 
#    #The static animation for her face
#    subpixel True 
#    ease 1.5 offset (0,0)
#    repeat

#transform Emma_BJ_StaticBody():                              
#    #The static animation for her face
#    subpixel True 
#    ease 1.5 offset (0,0)
                          
    
#Head and Body Animations for Emma's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
                                                               #BJ Launchers  
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Emma_BJ_Launch(Line = 0):    # The sequence to launch the Emma BJ animations  
    if renpy.showing("Emma_BJ_Animation"):
        return
    
    call Emma_Hide
    if Line == "L" or Line == "cum":
        show Emma_Sprite at SpriteLoc(StageCenter) zorder EmmaX.Layer:
            alpha 1
            ease 1 zoom 2.5 offset (150,80) 
        with dissolve
    else:
        show Emma_Sprite at SpriteLoc(StageCenter) zorder EmmaX.Layer:
            alpha 1
            zoom 2.5 offset (150,80) 
        with dissolve
        
    $ Speed = 0
    if Taboo and Line == "L": # Emma gets started. . .
            if len(Present) >= 2:
                if Present[0] != EmmaX:
                        "[EmmaX.Name] looks back at [Present[0].Name] to see if she's watching."
                elif Present[1] != EmmaX:
                        "[EmmaX.Name] looks back at [Present[1].Name] to see if she's watching."
            else:
                        "[EmmaX.Name] looks around to see if anyone can see her."
            "She then bends down and puts your cock to her mouth."
    elif Line == "L":    
            "[EmmaX.Name] smoothly bends down and places your cock against her cheek."    
            
    
    if Line != "cum":
        $ Trigger = "blow"
    
    show Emma_Sprite zorder EmmaX.Layer:
        alpha 0
    show Emma_BJ_Animation zorder 150: 
        pos (645,510) 
    return
    
label Emma_BJ_Reset: # The sequence to the Emma animations from BJ to default
    if not renpy.showing("Emma_BJ_Animation"):
        return
#    hide Emma_BJ_Animation
    call Emma_Hide 
    $ Speed = 0
    
    show Emma_Sprite at SpriteLoc(StageCenter) zorder EmmaX.Layer:
        alpha 1
        zoom 2.5 offset (150,80) 
    with dissolve
    
    show Emma_Sprite zorder EmmaX.Layer:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)      
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
        alpha 1
        zoom 1 offset (0,0)    
    return  

# End Emma Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Start Emma Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Emma Handjob element //////////////////////////////////////////////////////////////////////                                         Core Emma HJ element

image Emma_Hand_Under:
    "images/EmmaSprite/handemma2.png"
    anchor (0.5,0.5)
    pos (-10,0)
    
    
image Emma_Hand_Over:
    "images/EmmaSprite/handemma1.png"    
    anchor (0.5,0.5)
    pos (-10,0)
    
transform Emma_Hand_1():
    subpixel True
    pos (-20,-100) 
    rotate 5
    block:
        ease .5 pos (0,150) rotate -5 #ypos 150 rotate 5 Bottom
        pause 0.25
        ease 1.0 pos (-20,-100) rotate 5 #250#-150 #rotate -10#  Top
        pause 0.1
        repeat

transform Emma_Hand_2():
    subpixel True    
    pos (-15,-120) 
    rotate 10 
    block:
        ease 0.2 pos (-15,0) rotate 0   
        pause 0.1
        ease 0.4 pos (-15,-120) rotate 10 
        pause 0.1
        repeat

transform Handcock_3():
    subpixel True
    rotate_pad False    
    ypos 400 
    rotate 0 #400
    block:
        ease .5 ypos 450 rotate -2 #450
        pause 0.25
        ease 1.0 ypos 400 rotate 0 #400
        pause 0.1
        repeat

transform Handcock_4():
    subpixel True
    rotate_pad False    
    ypos 400 
    rotate 0
    block:
        ease .2 ypos 430 rotate -3 #410
        ease .5 ypos 400 rotate 0
        pause 0.1
        repeat
     
transform Handcock_1E():
    subpixel True
    rotate_pad False    
    ypos 400 
    rotate 0 #400
    block:
        ease .5 ypos 450 rotate -2 #450
        pause 0.25
        ease 1.0 ypos 400 rotate 0 #400
        pause 0.1
        repeat

transform Handcock_2E():
    subpixel True
    rotate_pad False
    ypos 400 
    rotate 0
    block:
        ease .2 ypos 430 rotate -3 #410
        ease .5 ypos 400 rotate 0
        pause 0.1
        repeat
    
image Emma_HJ_Animation:  
    contains:
        ConditionSwitch(                                                # backside of the hand
            "not Speed", Transform("Emma_Hand_Under"), 
            "Speed == 1", At("Emma_Hand_Under", Emma_Hand_1()),
            "Speed >= 2", At("Emma_Hand_Under", Emma_Hand_2()),            
            "Speed", Null(),
            ),  
    contains:
        ConditionSwitch(                                                # cock
            "not Speed", Transform("Zero_Handcock"), 
            "Speed == 1", At("Zero_Handcock", Handcock_1E()),
            "Speed >= 2", At("Zero_Handcock", Handcock_2E()), 
            "Speed", Null(),
            ),  
        offset (0,0)
    contains:
        ConditionSwitch(                                                # fingers of the hand
            "not Speed", Transform("Emma_Hand_Over"), 
            "Speed == 1", At("Emma_Hand_Over", Emma_Hand_1()),
            "Speed >= 2", At("Emma_Hand_Over", Emma_Hand_2()), 
            "Speed", Null(),
            ),   
    anchor (0.51, -1.3)
    zoom 0.4#0.6
        
        
label Emma_HJ_Launch(Line = 0): 
    if renpy.showing("Emma_HJ_Animation"):        
        $ Trigger = "hand"
        return
    call Emma_Hide
    if Line == "L":      
        show Emma_Sprite at SpriteLoc(StageRight) zorder EmmaX.Layer:
            alpha 1
            ease 1 zoom 1.7 offset (0,200)#(-50,200)
    else:     
        show Emma_Sprite at SpriteLoc(StageRight) zorder EmmaX.Layer:
            alpha 1
            ease 1 zoom 1.7 offset (0,200)#(-50,200)
        with dissolve
   
    if Line == "L": # Rogue gets started. . .
        if Taboo:
            if len(Present) >= 2:
                if Present[0] != EmmaX:
                        "[EmmaX.Name] looks back at [Present[0].Name] to see if she's watching."
                elif Present[1] != EmmaX:
                        "[EmmaX.Name] looks back at [Present[1].Name] to see if she's watching."
            else:
                        "[EmmaX.Name] looks around to see if anyone can see her."
            "She then bends down and grabs your cock."
        else:
            "[EmmaX.Name] bends down and grabs your cock."
            
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    else:
        $ Speed = 1
    pause .5
    $ EmmaX.ArmPose = 1
    show Emma_HJ_Animation at SpriteLoc(StageCenter) zorder 150 with easeinbottom:
        #xoffset 150
        offset (100,250)#(100,250)
    return
    
label Emma_HJ_Reset: # The sequence to the Rogue animations from handjob to default
    if not renpy.showing("Emma_HJ_Animation"):
        return    
    $ Speed = 0            
    $ EmmaX.ArmPose = 1
    hide Emma_HJ_Animation with easeoutbottom
    call Emma_Hide 
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
        alpha 1
        zoom 1.7 offset (-50,200)
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause .5
        ease .5 zoom 1 offset (0,0) 
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
        alpha 1
        zoom 1 offset (0,0)     
    return
    
# End Emma Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    
    

            
# Start Emma Footjob animations  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /   
image Emma_FJ_Chair:
    #footjob chair   
    contains:        
        ConditionSwitch(
            #Foot    
            "not renpy.showing('Emma_FJ_Animation')", Null(),
            "True", "images/EmmaSprite/EmmaSprite_Chair.png" 
            )   
        anchor (0.6, 0.05)
        zoom 0.75  
        
image Emma_FJ_Mask:
    #core footjob animation   
    contains:
        "images/EmmaSprite/EmmaSprite_FJMask.png"    
        anchor (0.6, 0.0)
        zoom 0.75
        pos (200,0)      
        
image Emma_FJ_Animation:
    #core footjob animation   
    contains:
        ConditionSwitch(                                                                         
            #Personal Wetness            
            "not EmmaX.Wet", Null(),
            "EmmaX.Legs == 'pants' and not EmmaX.Upskirt", Null(),   
            "EmmaX.Panties and not EmmaX.PantiesDown and EmmaX.Wet <= 1", Null(),                   
            "EmmaX.Wet == 1", AlphaMask("Wet_Drip","Emma_Drip_Mask"), #only plays if nothing is in the way
            "True", AlphaMask("Wet_Drip2","Emma_Drip_Mask"), #only plays if nothing is in the way
            )
        pos (160,400)   
    contains:    
        ConditionSwitch(                                                                         
            #Spunk nethers        
            "'in' not in EmmaX.Spunk and 'anal' not in EmmaX.Spunk", Null(),
            "EmmaX.Legs == 'pants' and not EmmaX.Upskirt", Null(),   
            "True", ConditionSwitch( #Wet = 2+
                    "EmmaX.Panties and EmmaX.PantiesDown", AlphaMask("Spunk_Drip","Emma_Drip_MaskP"), #"Wet_Drip2",# 
                    "EmmaX.Legs == 'pants'", AlphaMask("Spunk_Drip","Emma_Drip_MaskP"),
                    "True", AlphaMask("Spunk_Drip","Emma_Drip_Mask"), #only plays if nothing is in the way
                    ),
            )    
        pos (160,400) 
    contains:
        #her basic body, masked to hide the legs
        AlphaMask("Emma_Sprite", "Emma_FJ_Mask")
#        zoom 1.1
    contains:        
        #her basic legs rightside
        "images/EmmaSprite/EmmaSprite_FJRight.png"
        zoom 0.75
    contains:
        #Hose
        ConditionSwitch(    
            "EmmaX.Hose == 'pantyhose' and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_FJRight_Pantyhose.png",
            "EmmaX.Hose == 'stockings' or EmmaX.Hose == 'stockings and garterbelt'", "images/EmmaSprite/EmmaSprite_FJRight_Stocking.png",                 
            "True", Null(),#Static
            ) 
        zoom 0.75        
    contains:
        ConditionSwitch(
            #Personal Wetness            
            "not EmmaX.Wet", Null(),
            "EmmaX.Legs and EmmaX.Wet <= 1", Null(),
            "EmmaX.Legs", "images/EmmaSprite/EmmaSprite_Wet.png",
            "EmmaX.Wet == 1", "images/EmmaSprite/EmmaSprite_Wet.png",
            "True", "images/EmmaSprite/EmmaSprite_Wet.png",       #EmmaX.Wet >1
            ) 
        zoom .75
    contains:
        #Garter
        ConditionSwitch(    
            "EmmaX.Hose == 'garterbelt' or EmmaX.Hose == 'stockings and garterbelt'", "images/EmmaSprite/EmmaSprite_FJRight_Garter.png",                 
            "True", Null(),#Static
            ) 
        zoom 0.75
    contains:
        #her basic pants rightside
        ConditionSwitch(
            #pants    
            "not EmmaX.Legs", Null(),
            "EmmaX.Upskirt", ConditionSwitch(                   
                        #if the skirt's up or pants down 
                        "EmmaX.Legs == 'skirt'", "images/EmmaSprite/EmmaSprite_SkirtUp.png", 
                        "True", Null(),
                        ),                    
            "True", ConditionSwitch(  
                        "EmmaX.Legs == 'pants'", "images/EmmaSprite/EmmaSprite_FJRight_Pants.png",   
                        "EmmaX.Legs == 'yoga pants'", "images/EmmaSprite/EmmaSprite_FJRight_Yoga.png",       
                        "EmmaX.Legs == 'skirt'", "images/EmmaSprite/EmmaSprite_FJRight_Skirt.png", 
                        "True", Null(),
                        ),   
            )  
        zoom 0.75
    contains:
        #boots
        ConditionSwitch(       
            "EmmaX.Upskirt and EmmaX.Legs and EmmaX.Legs != 'skirt'", Null(),   
            "EmmaX.Acc", "images/EmmaSprite/EmmaSprite_FJRight_Boot.png",       
            "True", Null(),#Static
            ) 
        zoom 0.75        
    contains:
        ConditionSwitch(                                                               
            # Emma's lower body
#            "Player.Cock != 'foot'", Null(),                                                             
            # If neither
            "Speed == 1", "Emma_FJ_Legs_1",#slow
            "Speed == 4", "Emma_FJ_Legs_4",#cumming
            "Speed >= 2", "Emma_FJ_Legs_2",#faster
            "True", "Emma_FJ_Legs_0",#Static
            ) 
        pos (450,20) #(430,20)
        zoom 0.7
    anchor (0.6, 0.0)                
    zoom .85  
    subpixel True
    block:
        ease 1 yoffset -2
        ease 1 yoffset 0
        repeat
#End core Footjob animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




image Emma_FJ_Legs_0:
    #Footjob speed 0 static
    contains:
        #her basic legs left thigh
        ConditionSwitch(
            #pants    
            "EmmaX.Legs == 'pants' and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png",   
            "EmmaX.Legs == 'yoga pants' and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png", 
            "EmmaX.Hose == 'pantyhose' and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Pantyhose.png",
            "EmmaX.Hose == 'stockings' or EmmaX.Hose == 'stockings and garterbelt'", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Stocking.png",
            "True", "images/EmmaSprite/EmmaSprite_FJLeftThigh.png", 
            )    
        subpixel True
        transform_anchor True
        anchor (.70,.63)
        pos (290,630)
        rotate 12
        parallel:
            ease 2.5 ypos 610
            ease 2.5 ypos 630
            repeat       
        parallel:
            ease 2.5 rotate 10
            ease 2.5 rotate 12
            repeat  
    contains:
        "Emma_FJ_Calf"
        subpixel True
        transform_anchor True
        pos (340,510) #(360,450) 
        rotate 20
        parallel:
            ease 2.5 ypos 490
            ease 2.5 ypos 510
            repeat       
        parallel:
            ease 2.5 rotate 15
            ease 2.5 rotate 20
            repeat  
    contains:
        #her basic legs left foot 
        ConditionSwitch(
            #Foot    
            "EmmaX.Hose and EmmaX.Hose != 'garterbelt'", "images/EmmaSprite/EmmaSprite_FJFoot_Stocking.png",
            "True", "images/EmmaSprite/EmmaSprite_FJFoot.png",
            )    
        transform_anchor True
        anchor (.6,.8)
        pos (200,680)
        rotate 25 
        parallel:
            easeout 2 rotate -5
            easein .5 rotate -10
            easeout 2 rotate 20
            easein .5 rotate 25
            repeat
    contains:
        #Cock
        "Zero_Emma_FootCock"   
        transform_anchor True  
        rotate 0
        block:          
            pause .5
            easeout 1.5 rotate -5
            easein .5 rotate -7
            pause .5
            easeout 1 rotate -3
            easein 1 rotate 0
            repeat
    anchor (0.6, 0.0)    
# End Emma Footjob Speed 0

image Emma_FJ_Legs_1:
    #Footjob speed 1 slow
    contains:
        #her basic legs left thigh
        ConditionSwitch(
            #pants    
            "EmmaX.Legs == 'pants' and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png",   
            "EmmaX.Legs == 'yoga pants' and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png", 
            "EmmaX.Hose == 'pantyhose' and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Pantyhose.png",
            "EmmaX.Hose == 'stockings' or EmmaX.Hose == 'stockings and garterbelt'", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Stocking.png",
            "True", "images/EmmaSprite/EmmaSprite_FJLeftThigh.png", 
            )    
        transform_anchor True
        anchor (.70,.63)
        pos (280,615)
        rotate 10
        parallel:
            pause 1.3
            ease 2.2 ypos 630
            ease 1 ypos 615
            repeat     
        parallel:            
            easein .5 rotate 12
            pause 1
            ease 1.5 rotate 18
            pause .5
            easeout 1 rotate 14
            repeat   
    contains:
        "Emma_FJ_Calf"
        transform_anchor True
        pos (350,475) #(360,450) 
        rotate 15  
        parallel:
            pause 1.5
            ease 2 ypos 515 #525
            ease 1 ypos 475
            repeat         
        parallel:
            ease 1 rotate 8 #top 5-10-12-10
            ease 1 rotate 18
            ease 2 rotate 20
            ease .5 rotate 18
            repeat
    contains:
        #her basic legs left foot 
        ConditionSwitch(
            #Foot    
            "EmmaX.Hose and EmmaX.Hose != 'garterbelt'", "images/EmmaSprite/EmmaSprite_FJFoot_Stocking.png",
            "True", "images/EmmaSprite/EmmaSprite_FJFoot.png",
            )    
        transform_anchor True
        anchor (.6,.8)
        pos (200,680)
        rotate 25 
        parallel:
            ease 1 xpos 240#(240,870)
            ease 1 xpos 200
            pause 2.5
            repeat  
        parallel:
            pause 1.5
            ease 2 ypos 730
            ease 1 ypos 680#(240,870)
            repeat 
        parallel:
            easein 1 rotate 0
            easeout 1 rotate 25
            easein 2 rotate 35
            easeout .5 rotate 25
            repeat
    contains:
        #Cock
        "Zero_Emma_FootCock"   
        transform_anchor True 
        block:                
            easein 1 rotate 0
            ease 2.5 rotate -5
            easeout 1 rotate 2
            repeat
    anchor (0.6, 0.0)    
# End Emma Footjob Speed 1

image Emma_FJ_Legs_2:
    #Footjob speed 1 Fast
    contains:
        #her basic legs left thigh
        ConditionSwitch(
            #pants    
            "EmmaX.Legs == 'pants' and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png",   
            "EmmaX.Legs == 'yoga pants' and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png", 
            "EmmaX.Hose == 'pantyhose' and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Pantyhose.png",
            "EmmaX.Hose == 'stockings' or EmmaX.Hose == 'stockings and garterbelt'", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Stocking.png",
            "True", "images/EmmaSprite/EmmaSprite_FJLeftThigh.png", 
            )    
        transform_anchor True
        anchor (.70,.63)
        pos (290,610)
        rotate 10
        parallel:
            ease.5 ypos 630 #bottom high = bottom 480
            ease 1 ypos 610
            repeat   
        parallel:
            ease .5 rotate 0
            ease 1 rotate 10
            repeat   
    contains:
        "Emma_FJ_Calf"
        transform_anchor True
        pos (380,450) #360,460  
        rotate 15
        parallel:
            ease .5 pos (320,500) #bottom high = bottom 480
            ease 1 pos (380,460)
            repeat            
        parallel:
            ease .5 rotate -5
            ease 1 rotate 15
            repeat
    contains:
        #her basic legs left foot 
        ConditionSwitch(
            #Foot    
            "EmmaX.Hose and EmmaX.Hose != 'garterbelt'", "images/EmmaSprite/EmmaSprite_FJFoot_Stocking.png",
            "True", "images/EmmaSprite/EmmaSprite_FJFoot.png",
            )    
        transform_anchor True
        anchor (.6,.8)
        pos (240,670)
        rotate 30
        parallel:
            ease .5 pos (240,870)
            ease 1 pos (240,670)
            repeat            
        parallel:
            ease .5 rotate 20
            ease 1 rotate 30
            repeat
    contains:
        #Cock
        "Zero_Emma_FootCock"   
        transform_anchor True   
        block:
            ease .5 rotate -8
            ease 1 rotate 0
            repeat
    anchor (0.6, 0.0)    
# End Emma Footjob Speed 2
    
    
image Emma_FJ_Legs_4:
    #Footjob speed 4 Cumming
    contains:
        #her basic legs left thigh
        ConditionSwitch(
            #pants    
            "EmmaX.Legs == 'pants' and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png",   
            "EmmaX.Legs == 'yoga pants' and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png", 
            "EmmaX.Hose == 'pantyhose' and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Pantyhose.png",
            "EmmaX.Hose == 'stockings' or EmmaX.Hose == 'stockings and garterbelt'", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Stocking.png",
            "True", "images/EmmaSprite/EmmaSprite_FJLeftThigh.png", 
            )    
        transform_anchor True
        anchor (.70,.63)
        pos (290,610)
        rotate 10  
        parallel:
            ease 1 rotate 0
            ease 1.3 rotate 23
            pause.5
            repeat   
    contains:
        "Emma_FJ_Calf"
        transform_anchor True
        pos (380,450) #360,460  
        rotate 15
#        alpha 0.3
        parallel:
            ease 1 pos (320,480) #bottom high = bottom
            ease 1.3 pos (380,450)
            pause.5
            repeat            
        parallel:
            ease 1 rotate 5
            ease 1.3 rotate 15
            pause.5
            repeat
    contains:
        #her basic legs left foot 
        ConditionSwitch(
            #Foot    
            "EmmaX.Hose and EmmaX.Hose != 'garterbelt'", "images/EmmaSprite/EmmaSprite_FJFoot_Stocking.png",
            "True", "images/EmmaSprite/EmmaSprite_FJFoot.png",
            )    
        transform_anchor True
        anchor (.6,.8)
        pos (240,670)
        rotate 40
        parallel:
            ease 1 pos (200,750) #(240,870)
            ease 1.3 pos (220,670)
            pause.5
            repeat            
        parallel:
            ease 1 rotate 30
            ease 1.3 rotate 40
            pause.5
            repeat

    contains:
        #Cock
        "Zero_Emma_FootCock"   
        transform_anchor True  
        block:
            pause .1
            ease .9 rotate -8
            ease 1.3 rotate 0
            pause.5
            repeat
    anchor (0.6, 0.0)  
# End Emma Footjob Speed 4

    
image Zero_Emma_FootCock:
    #cock used in Emma's FJ animation
    contains:
        ConditionSwitch(  
                "Player.Sprite", "Blowcock", 
                "True", Null(),
                )          
    pos (200,1000) 
    zoom .9
    anchor (-.4,0.7)
        
        
image Emma_FJ_Calf:
    #calf for footjob animation   
    contains:        
        ConditionSwitch(
            #calf    
            "EmmaX.Hose and EmmaX.Hose != 'garterbelt'", "images/EmmaSprite/EmmaSprite_FJLeftCalf_Stocking.png",
            "True", "images/EmmaSprite/EmmaSprite_FJLeftCalf.png",
            )            
    contains:
        #her basic legs left calf 
        ConditionSwitch(
            #pants    
            "not EmmaX.Legs or EmmaX.Upskirt", Null(), 
            "EmmaX.Legs == 'pants'", "images/EmmaSprite/EmmaSprite_FJLeftCalf_Pants.png",   
            "EmmaX.Legs == 'yoga pants'", "images/EmmaSprite/EmmaSprite_FJLeftCalf_Yoga.png", 
            "True", Null(),
            )   
    anchor (.31,.63)#.3.6
    
# End footjob animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Emma_FJ_Launch(Line = 0):    # The sequence to launch the Emma footjob animations   
    $ Trigger = "foot"
    if renpy.showing("Emma_FJ_Animation"):
        return
    call Emma_Hide
    show Emma_FJ_Chair zorder 10:
        xpos 1580 
        yoffset 170
        alpha 1
        ease .5 xpos 590
    show Emma_FJ_Animation zorder 150:  
        alpha 0
        pos (950,200)  
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
        alpha 1
        ease 1 zoom .8 xpos 580 yoffset 150
    pause 1

    show Emma_FJ_Chair zorder 10:
        alpha 1
        xpos 590
    show Emma_Sprite zorder EmmaX.Layer:
        alpha 0
    $ Speed = 0    
    show Emma_FJ_Animation zorder 150:  
        ease .5 alpha 1
    pause 0.5
    show Emma_FJ_Animation zorder 150: 
        alpha 1        
    $ Player.Sprite = 1
    return
    
label Emma_FJ_Reset: # The sequence to the Emma animations from Titfuck to default
    if not renpy.showing("Emma_FJ_Animation"):
        return
    call Emma_Hide 
    $ Player.Sprite = 0
    
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
        zoom .8 xpos 580 yoffset 150 #offset (-100,50)      
    show Emma_Sprite zorder EmmaX.Layer:
        alpha 1
        ease .5 zoom 1 xpos EmmaX.SpriteLoc yoffset 0 alpha 1  
    pause .5
    
    hide Emma_FJ_Chair zorder 10
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
        alpha 1
        zoom 1 offset (0,0) xpos EmmaX.SpriteLoc 
        
    "[EmmaX.Name] stands back up."
    return

# End Emma Footjob animations  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /       




# Emma Misc Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#image Test_Object:                 #this is the yellow rectangle
#    contains:
#        Solid("#d5f623", xysize=(1024, 678))
#    anchor (0,0)
#    alpha .8
    
#image Emma_At_DeskB:
#    contains:
#        subpixel True
#        "Emma_Sprite"
#        zoom 0.29
#        pos (450,190) #(500,200)
#    contains:        
##        AlphaMask("Test_Object", "images/ClassroomFront.png")
#        AlphaMask("images/Classroom.jpg", "images/ClassroomFront.png")
#    contains:
#        ConditionSwitch(        
#                "bg_current != 'bg classroom' or Current_Time == 'Evening' or Current_Time == 'Night' or Weekday >= 5", Null(),                
#                "True", "images/ClassroomPupils.png",                
#                )      

#image Emma_At_PodiumB:
#    contains:
#        subpixel True
#        "Emma_Sprite"
#        zoom 0.29
#        pos (670,180) #(500,200)
#    contains:        
##        AlphaMask("Test_Object", "images/ClassroomFront.png")
#        AlphaMask("images/Classroom.jpg", "images/ClassroomFront.png")
#    contains:
#        ConditionSwitch(        
#                "bg_current != 'bg classroom' or Current_Time == 'Evening' or Current_Time == 'Night' or Weekday >= 5", Null(),                
#                "True", "images/ClassroomPupils.png",                
#                )                     
        
image Emma_At_Desk:
    contains:
        subpixel True
        "Emma_Sprite"
        zoom 0.29
        pos (450,190) #(500,200)

image Emma_At_Podium:
    contains:
        subpixel True
        "Emma_Sprite"
        zoom 0.29
        pos (670,180) #(500,200)
            
        
        
        
        
label Emma_Kissing_Launch(T = Trigger):    
    call Emma_Hide
    $ Trigger = T
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer
    show Emma_Sprite at SpriteLoc(StageCenter) zorder EmmaX.Layer:
        ease 0.5 offset (0,0) zoom 2 alpha 1
    return
    
label Emma_Kissing_Smooch:  
    $ EmmaX.FaceChange("kiss")
    show Emma_Sprite at SpriteLoc(StageCenter) zorder EmmaX.Layer:
        ease 0.5 xpos StageCenter offset (0,0) zoom 2 alpha 1
        pause 1
        ease 0.5 xpos EmmaX.SpriteLoc zoom 1      
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
        zoom 1
    $ EmmaX.FaceChange("sexy") 
    return
            
label Emma_Breasts_Launch(T = Trigger):    
    call Emma_Hide
    $ Trigger = T
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
#        ease 0.5 offset (-100,-200) zoom 2
        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
    return
        
label Emma_Pussy_Launch(T = Trigger):
    call Emma_Hide    
    $ Trigger = T
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
    return
        
label Emma_Pos_Reset(Pose = 0):     
    if EmmaX.Loc != bg_current:
            return
    call Emma_Hide 
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
        ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
    show Emma_Sprite zorder EmmaX.Layer:
        offset (0,0) 
        anchor (0.5, 0.0)
        zoom 1   
        xzoom 1 
        yzoom 1
        alpha 1
        pos (EmmaX.SpriteLoc,50)
    $ Trigger = Pose
    return
    
label Emma_Hide(Sprite=0):
        if renpy.showing("Emma_SexSprite"):
            call Emma_Sex_Reset
        hide Emma_SexSprite
        hide Emma_HJ_Animation
        hide Emma_BJ_Animation
        hide Emma_TJ_Animation 
        hide Emma_FJ_Animation 
        if Sprite:
                hide Emma_Sprite    
        return

# Interface items //////////////////////////////////////////////////////////////////////////////

image GropeLeftBreast_Emma:    
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65#.7
        pos (215,400)#(215,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 90
        block: 
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image GropeRightBreast_Emma:    
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (110,400)#(120,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -90
        block: 
            ease 1 rotate -60 #-30
            ease 1 rotate -90 #-60 
            repeat

#image GropeBreast:
image LickRightBreast_Emma:   
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5 
        xzoom -0.45
        pos (105,375)#(115,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block: 
            ease .5 rotate -40 pos (85,345)#(95,370)            
            pause .5
            ease 1.5 rotate 30 pos (105,375)#(115,400)
            repeat
            
image LickLeftBreast_Emma:   
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5 
        xzoom -0.45
        pos (205,370) #(200,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block: 
            ease .5 rotate -40 pos (190,350)#(190,380)            
            pause .5
            ease 1.5 rotate 30 pos (205,370)#(200,410)
            repeat

image GropeThigh_Emma: 
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (180,670)#(200,720)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        block:
            pause .5
            ease 1 rotate 110 pos (150,750) 
            ease 1 rotate 100 pos (180,670)   
            repeat

image GropePussy_Emma: 
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (200,600)#(210,640) -20
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice: 
                ease .5 rotate 190 pos (200,585)
                ease .75 rotate 170 pos (200,600)   
            choice: 
                ease .5 rotate 190 pos (200,585)
                pause .25
                ease 1 rotate 170 pos (200,600)             
            repeat

image FingerPussy_Emma: 
    contains:
        subpixel True
        "UI_Finger"       
        zoom 0.65
        pos (210,665)#(220,730)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice: 
                ease 1 rotate 40 pos (220,640)#(230,695)
                pause .5
                ease 1 rotate 50 pos (210,665)  #(220,730)     
            choice:                          
                ease .5 rotate 40 pos (220,640)
                pause .5
                ease 1.75 rotate 50 pos (210,665)  
            choice:                          
                ease 2 rotate 40 pos (220,640)
                pause .5
                ease 1 rotate 50 pos (210,665)  
            choice:                          
                ease .25 rotate 40 pos (220,640)
                ease .25 rotate 50 pos (210,665) 
                ease .25 rotate 40 pos (220,640)
                ease .25 rotate 50 pos (210,665)
            repeat
            
image Lickpussy_Emma:   
    contains:
        subpixel True
        "UI_Tongue"        
        yzoom 0.45
        xzoom -0.45
        pos (230,625)#(240,680)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block: 
            easeout .5 rotate -50 pos (210,605) #(220,660)
            linear .5 rotate -60 pos (200,615) #(210,670)
            easein 1 rotate 10 pos (230,625) #(240,680)
            repeat

image VibratorRightBreast_Emma: 
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

image VibratorLeftBreast_Emma: 
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
            
image VibratorPussy_Emma: 
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

image VibratorAnal_Emma: 
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
            
image VibratorPussyInsert_Emma: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_Emma: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0



#Lesbian action animations.
image GirlGropeBothBreast_Emma: 
    contains:
        "GirlGropeLeftBreast_Emma"
    contains:
        "GirlGropeRightBreast_Emma"
    
image GirlGropeLeftBreast_Emma:  
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (240,370)#(240,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -20
        block: 
            ease 1 rotate -40 pos (230,360)#(280,390)
            ease 1 rotate -20 pos (240,370)
            repeat

image GirlGropeRightBreast_Emma:    
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (90,380) #(110,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10#-30
        block: 
            ease 1 rotate -30 pos (90,410)#(110,410)
            ease 1 rotate -10 pos (90,380)
            repeat

image GirlGropeThigh_Emma: 
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

image GirlGropePussy_EmmaSelf:
    contains:
        "GirlGropePussy_Emma"
        anchor (0.5,0.5)
        rotate -40
#        yzoom -1
        pos (120,530)
    
image GirlGropePussy_Emma: 
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (200,575)#(210,625)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (205,590)
                ease .5 rotate 195 
                ease .75 rotate 210 
                ease .5 rotate 195 
            choice: #slow rub
                ease .5 rotate 210 pos (205,590)#-10+20
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (205,590)
                ease .75 rotate 200 pos (205,595)
                ease .5 rotate 205 pos (205,590)
                ease .75 rotate 200 pos (205,595)
            choice: #Fast stroke
                ease .3 rotate 205 pos (205,590)
                ease .3 rotate 200 pos (205,600)
                ease .3 rotate 205 pos (205,590)
                ease .3 rotate 200 pos (205,600)
            repeat

image GirlFingerPussy_Emma: 
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

        