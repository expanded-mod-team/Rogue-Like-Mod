# Basic character Sprites
image Emma_Sprite:
    LiveComposite(
        (402,965), 
#        (55,0), ConditionSwitch(                                                                         #hair back temporary
#            "not E_Hair", Null(),
#            "E_Hair == 'wet' or E_Water", "images/EmmaSprite/EmmaSprite_Head_HairBackWet.png",
#            "True", Null(),        
#            ),   
        (0,0), ConditionSwitch(                                                                         
            #cape layer       
            "E_Uptop or E_Over == 'jacket' or E_Over == 'modded black jacket' or (E_Chest != 'corset' and E_Chest != 'modded black corset')", Null(),  
            "Emma_Arms == 2 and E_Chest == 'modded black corset'", "images/EmmaSprite/EmmaSprite_Chest_modded black corset_cape2.png",              
            "E_Chest == 'modded black corset'", "images/EmmaSprite/EmmaSprite_Chest_modded black corset_cape1.png",
            "Emma_Arms == 2", "images/EmmaSprite/EmmaSprite_Cape2.png",              
            "True", "images/EmmaSprite/EmmaSprite_Cape1.png",   
            ), 
        (0,0), ConditionSwitch(                                                                         
            #Overshirt back layer       
            "E_Over and E_Uptop and E_Over == 'jacket'", "images/EmmaSprite/EmmaSprite_Jacket_Back.png",  
            "True", Null(), 
            ), 
        (0,0), ConditionSwitch(
            #hair back 
            "not E_Hair or E_HairColor", Null(),
            "E_Hair == 'wet' or E_Water", "images/EmmaSprite/EmmaSprite_HairbackWet.png",
            "E_Hair", "images/EmmaSprite/EmmaSprite_Hairback.png",   
            "True", Null(),        
            ), 
        (0,0), ConditionSwitch(
            #hair back 
            "not E_Hair or not E_HairColor", Null(),
            "E_Hair == 'wet' or E_Water", im.MatrixColor("images/EmmaSprite/EmmaSprite_HairWhitebackWet.png",im.matrix.tint(float(E_HairCustomColor.red)/255.0, float(E_HairCustomColor.green)/255.0, float(E_HairCustomColor.blue)/255.0)),
            "E_Hair", im.MatrixColor("images/EmmaSprite/EmmaSprite_HairWhiteback.png",im.matrix.tint(float(E_HairCustomColor.red)/255.0, float(E_HairCustomColor.green)/255.0, float(E_HairCustomColor.blue)/255.0)),
            "True", Null(),        
            ),     
        (0,0), ConditionSwitch(
            #nighty underlayer
            "IsOutfitModdedEmma('Over')", GetModdedString("images/EmmaSprite/EmmaSprite_Over_", E_Over, "_Back.png"),
            "E_Over == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_Under.png", 
            "True", Null(),              
            ), 
        (0,0), ConditionSwitch(            
            #panties down back 
            "not E_Panties or not E_PantiesDown or (PantsNum('Emma') > 5 and not E_Upskirt)", Null(), 
            "IsOutfitModdedEmma('Panties')", GetModdedString("images/EmmaSprite/EmmaSprite_Panties_", E_Panties, "_DownBack.png"),
            "E_Panties == 'sports panties'", "images/EmmaSprite/EmmaSprite_Panties_Sports_DownBack.png",   
            "E_Panties == 'bikini bottoms'", "images/EmmaSprite/EmmaSprite_Panties_Bikini_DownBack.png",  
            "True", "images/EmmaSprite/EmmaSprite_Panties_DownBack.png",   
            ),  
        (0,0), ConditionSwitch(
            #legs/torso 
            "Emma_Arms == 2", "images/EmmaSprite/EmmaSprite_Legs_Arms2.png",   
            "True", "images/EmmaSprite/EmmaSprite_Legs_Arms1.png", #if E_Arms == 1 
            ),     
        
        (215,540), ConditionSwitch(                                                                         
            #Personal Wetness            
            "not E_Wet", Null(),
            "PantsNum('Emma') > 5 and not E_Upskirt", Null(),   
            "E_Panties and not E_PantiesDown and E_Wet <= 1", Null(),                   
            "E_Wet == 1", ConditionSwitch( #Wet = 1
                    "E_Panties and E_PantiesDown", AlphaMask("Wet_Drip","Emma_Drip_MaskP"),  
                    "E_Legs == 'pants'", AlphaMask("Wet_Drip","Emma_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip","Emma_Drip_Mask"), #only plays if nothing is in the way
                    ),
            "True", ConditionSwitch( #Wet = 2+
                    "E_Panties and E_PantiesDown", AlphaMask("Wet_Drip2","Emma_Drip_MaskP"), #"Wet_Drip2",# 
                    "E_Legs == 'pants'", AlphaMask("Wet_Drip2","Emma_Drip_MaskP"),
                    "E_Panties", AlphaMask("Wet_Drip","Emma_Drip_Mask"), #"Wet_Drip2",# 
                    "True", AlphaMask("Wet_Drip2","Emma_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (0,0), ConditionSwitch(
            #Personal Wetness            
            "not E_Wet", Null(),
            "E_Legs and E_Wet <= 1", Null(),
            "E_Legs", "images/EmmaSprite/EmmaSprite_Wet.png",
            "E_Wet == 1", "images/EmmaSprite/EmmaSprite_Wet.png",
            "True", "images/EmmaSprite/EmmaSprite_Wet.png",       #E_Wet >1
            ),     
        
        (215,540), ConditionSwitch(                                                                         
            #Spunk nethers        
            "'in' not in E_Spunk and 'anal' not in E_Spunk", Null(),
            "E_Legs == 'pants' and not E_Upskirt", Null(),   
            "True", ConditionSwitch( #Wet = 2+
                    "E_Panties and E_PantiesDown", AlphaMask("Spunk_Drip","Emma_Drip_MaskP"), #"Wet_Drip2",# 
                    "E_Legs == 'pants'", AlphaMask("Spunk_Drip","Emma_Drip_MaskP"),
                    "True", AlphaMask("Spunk_Drip","Emma_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),    
        (0,0), ConditionSwitch(
            #pubes 
            "E_Pubes", "images/EmmaSprite/EmmaSprite_Pubes.png",   
            "True", Null(),        
            ),      
        (0,0), ConditionSwitch(
            #nude lower piercings        
            "not E_Pierce", Null(),  
            "E_Panties and not E_PantiesDown", Null(), 
            "E_Legs != 'skirt' and E_Legs and not E_Upskirt", Null(), #skirt if wearing a skirt
            "E_Pierce == 'barbell'", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_Barbell.png",  
            "E_Pierce == 'ring'", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_Ring.png",  
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(
            #Water effect 
            "E_Water", "images/EmmaSprite/EmmaSprite_Water_Legs.png",   
            "True", Null(),        
            ),               
        (0,0), ConditionSwitch(
            # stockings
            "renpy.showing('Emma_FJ_Animation')", Null(),                    
            "IsOutfitModdedEmma('Hose')", GetModdedString("images/EmmaSprite/EmmaSprite_Hose_", E_Hose, ".png"),
            "E_Hose == 'stockings'", "images/EmmaSprite/EmmaSprite_Stockings.png",   
            "E_Hose == 'stockings and garterbelt'", "images/EmmaSprite/EmmaSprite_StockingsGarter.png",   
            "E_Hose == 'garterbelt'", "images/EmmaSprite/EmmaSprite_Garter.png",   
            "True", Null(),        
            ),                  
        (0,0), ConditionSwitch(
            #boots    
            "E_PantiesDown and E_Boots == 'thigh boots' and (PantsNum('Emma') >= 5 or not E_Legs)", "images/EmmaSprite/EmmaSprite_Boots.png",    
            "True", Null(), 
            ),     
        (0,0), ConditionSwitch(
            #panties down if not wearing pants
            "not E_Panties or not E_PantiesDown or (PantsNum('Emma') > 5 and not E_Upskirt)", Null(),   
            "IsOutfitModdedEmma('Panties') and E_Wet", GetModdedString("images/EmmaSprite/EmmaSprite_Panties_", E_Panties, "_DownWet.png"),
            "IsOutfitModdedEmma('Panties')", GetModdedString("images/EmmaSprite/EmmaSprite_Panties_", E_Panties, "_Down.png"),
            "E_Panties == 'sports panties' and E_Wet", "images/EmmaSprite/EmmaSprite_Panties_Sports_DownWet.png",  
            "E_Panties == 'sports panties'", "images/EmmaSprite/EmmaSprite_Panties_Sports_Down.png",              
            "E_Panties == 'lace panties' and E_Wet", "images/EmmaSprite/EmmaSprite_Panties_Lace_DownWet.png",  
            "E_Panties == 'lace panties'", "images/EmmaSprite/EmmaSprite_Panties_Lace_Down.png",   
            "E_Panties == 'bikini bottoms'", "images/EmmaSprite/EmmaSprite_Panties_Bikini_Down.png",  
#            "E_Wet", "images/EmmaSprite/EmmaSprite_Panties_DownWet.png",  
            "True", "images/EmmaSprite/EmmaSprite_Panties_Down.png",  
            ),                
        (0,0), ConditionSwitch(
            #panties up
            "E_PantiesDown or not E_Panties", Null(),   
#            "E_Panties == 'sports panties' and E_Wet", "images/EmmaSprite/EmmaSprite_Panties_Sports_Wet.png",     
            "IsOutfitModdedEmma('Panties') and E_Wet", GetModdedString("images/EmmaSprite/EmmaSprite_Panties_", E_Panties, "_Wet.png"),
            "IsOutfitModdedEmma('Panties')", GetModdedString("images/EmmaSprite/EmmaSprite_Panties_", E_Panties, ".png"),
            "E_Panties == 'sports panties'", "images/EmmaSprite/EmmaSprite_Panties_Sports.png",  
            "E_Panties == 'lace panties' and E_Wet", "images/EmmaSprite/EmmaSprite_Panties_Lace_Wet.png", 
            "E_Panties == 'lace panties'", "images/EmmaSprite/EmmaSprite_Panties_Lace.png",  
            "E_Panties == 'bikini bottoms'", "images/EmmaSprite/EmmaSprite_Panties_Bikini.png",  
#            "E_Wet", "images/EmmaSprite/EmmaSprite_Panties_Wet.png", #readd when sprite works 
            "True", "images/EmmaSprite/EmmaSprite_Panties.png",  
            ),              
        (0,0), ConditionSwitch(
            # pantyhose
            "renpy.showing('Emma_FJ_Animation')", Null(),  
            "E_Hose == 'pantyhose' and not E_PantiesDown", "images/EmmaSprite/EmmaSprite_Hose.png",   
            "True", Null(),        
            ),    
        (0,0), ConditionSwitch(
            #pussy spunk 
            "E_Legs and PantsNum('Emma') != 5 and not E_Upskirt", Null(),
            "'in' in E_Spunk or 'anal' in E_Spunk", "images/EmmaSprite/EmmaSprite_Spunk_Pussy.png",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(
            #pants    
            "not E_Legs", Null(),
            "E_Upskirt", ConditionSwitch(                   
                        #if the skirt's up or pants down 
                        "E_Legs == 'skirt'", "images/EmmaSprite/EmmaSprite_SkirtUp.png", 
                        "IsOutfitModdedEmma('Legs')", GetModdedString("images/EmmaSprite/EmmaSprite_Legs_", E_Legs, "_Down.png"),
                        "E_Boots", Null(),
                        "E_Legs == 'pants'", "images/EmmaSprite/EmmaSprite_Pants_Down.png",   
                        "E_Legs == 'yoga pants'", "images/EmmaSprite/EmmaSprite_Pants_Yoga_Down.png",   
                        "True", Null(),
                        ),                    
            "True", ConditionSwitch(                
                    #if it's the ring pericings
                    "E_Wet", ConditionSwitch(   
                        #if she's not wet
                        "IsOutfitModdedEmma('Legs')", GetModdedString("images/EmmaSprite/EmmaSprite_Legs_", E_Legs, "_Wet.png"),
                        "E_Legs == 'pants'", "images/EmmaSprite/EmmaSprite_Pants.png",   
                        "E_Legs == 'yoga pants'", "images/EmmaSprite/EmmaSprite_Pants_YogaWet.png",       
                        "E_Legs == 'skirt'", "images/EmmaSprite/EmmaSprite_Skirt.png", 
                        "True", Null(),
                        ),
                    "True", ConditionSwitch(   
                        #if she's wet
                        "IsOutfitModdedEmma('Legs')", GetModdedString("images/EmmaSprite/EmmaSprite_Legs_", E_Legs, ".png"),
                        "E_Legs == 'pants'", "images/EmmaSprite/EmmaSprite_Pants.png",   
                        "E_Legs == 'yoga pants'", "images/EmmaSprite/EmmaSprite_Pants_Yoga.png",       
                        "E_Legs == 'skirt'", "images/EmmaSprite/EmmaSprite_Skirt.png", 
                        "True", Null(),
                        ),                    
                    ),    
            ),                   
        (0,0), ConditionSwitch(
            #boots    
            "not E_PantiesDown and E_Boots == 'thigh boots'", "images/EmmaSprite/EmmaSprite_Boots.png",    
            "True", Null(), 
            ),     
        (0,0), ConditionSwitch(
            #clothed lower piercings         
            "E_Legs == 'skirt'", Null(),
            "E_Pierce == 'barbell'", ConditionSwitch(   
                    #if it's the barbell pericings 
                    "E_Legs and not E_Upskirt", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_BarOut.png",  
                    "E_Panties and not E_PantiesDown", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_BarOut.png", 
                    "True", Null(),
                    ),    
            "E_Pierce == 'ring'", ConditionSwitch(   
                    #if it's the ring pericings
                    "E_Legs and not E_Upskirt", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_RingOut.png",  
                    "E_Panties and not E_PantiesDown", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_RingOut.png", 
                    "True", Null(),
                    ),
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(
            #Chest underlayer
            "IsOutfitModdedEmma('Chest') and not E_Uptop", GetModdedString("images/EmmaSprite/EmmaSprite_Chest_", E_Chest, "_Under.png"),
            "E_Chest == 'sports bra' and not E_Uptop", "images/EmmaSprite/EmmaSprite_Bra_Sports_Under.png",   
            "E_Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Bra_Lace_Under.png",   
            "E_Chest == 'corset'", "images/EmmaSprite/EmmaSprite_CorsetUnder.png",   
            "E_Chest == 'bikini top'", "images/EmmaSprite/EmmaSprite_Bra_Bikini_Under.png",   
            "True", Null(),              
            ), 
        (0,0), ConditionSwitch(
            #Over underlayer
            "E_Over == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_Under.png", 
            "E_Over == 'towel'", "images/EmmaSprite/EmmaSprite_Towel_Under.png",   
            "True", Null(),              
            ),          
        (0,0), ConditionSwitch(
            #belly spunk 
            "'belly' in E_Spunk", "images/EmmaSprite/EmmaSprite_Spunk_Belly.png",
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(
            #arms 
            "Emma_Arms == 2", "images/EmmaSprite/EmmaSprite_Arms2.png",         # one hand up
            "True", "images/EmmaSprite/EmmaSprite_Arms1.png", #if E_Arms == 1   # Crossed        
            ),  
        (0,0), ConditionSwitch(
            #Water effect on arms
            "not E_Water", Null(),             
            "Emma_Arms == 1", "images/EmmaSprite/EmmaSprite_Water_Arms1.png",   
            "True", "images/EmmaSprite/EmmaSprite_Water_Arms2.png", #if E_Arms == 1      
            ), 
        (0,0), ConditionSwitch(
            #gloves 
            "not E_Arms", Null(),  
            "Emma_Arms == 2", "images/EmmaSprite/EmmaSprite_Gloves_Arms2.png",   
            "True", "images/EmmaSprite/EmmaSprite_Gloves_Arms1.png", #if E_Arms == 1         
            ),   
        
        (0,0), ConditionSwitch(                                                                         
            # jacket arms in "up" pose  
            "not E_Uptop or E_Over != 'jacket'", Null(),  
            "Emma_Arms == 2", "images/EmmaSprite/EmmaSprite_Jacket_2Arm_Up.png",              
            "True", "images/EmmaSprite/EmmaSprite_Jacket_1Arm_Up.png",   
            ), 
        (0,0), ConditionSwitch(
            #tits
            "Emma_Arms == 1", "images/EmmaSprite/EmmaSprite_TitsUp.png",   # E_TitsUp = 1
            "E_Chest in ('corset','lace bra','sports bra','bikini top') or E_Chest in ('modded black corset','modded red sports bra','modded white sports bra', 'modded NewX', 'modded NewX black')", "images/EmmaSprite/EmmaSprite_TitsUp.png",   # E_TitsUp = 1
            #"E_Chest in ('modded black corset','modded red sports bra','modded white sports bra', 'modded NewX', 'modded NewX black')", "images/EmmaSprite/EmmaSprite_TitsUp.png",   # E_TitsUp = 1
            "True", "images/EmmaSprite/EmmaSprite_TitsDown.png",   # E_TitsUp = 0
            ), 
        (0,0), ConditionSwitch(
            #nude peircings      
            #something about this entry makes all subsequent entries mis-aligned
            "not E_Pierce", Null(),  
            "E_Pierce == 'barbell'", ConditionSwitch(   
                    #if it's the barbell pericings
                    "Emma_Arms == 1", "images/EmmaSprite/EmmaSprite_Pierce_Up_Barbell.png",                     
                    "E_Chest in ('corset','lace bra','sports bra','bikini top') or E_Chest in ('modded black corset','modded red sports bra','modded white sports bra', 'modded NewX', 'modded NewX black')", "images/EmmaSprite/EmmaSprite_Pierce_Up_Barbell.png",   
#                    "E_Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_Barbell.png",    
#                    "E_Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_Barbell.png",  
                    "True", "images/EmmaSprite/EmmaSprite_Pierce_Down_Barbell.png",        
                    ),                        
            "E_Pierce == 'ring'", ConditionSwitch(                      
                    #if it's the ring pericings                                 
                    "Emma_Arms == 1", "images/EmmaSprite/EmmaSprite_Pierce_Up_Ring.png", 
                    "E_Chest in ('corset','lace bra','sports bra','bikini top') or E_Chest in ('modded black corset','modded red sports bra','modded white sports bra', 'modded NewX', 'modded NewX black')", "images/EmmaSprite/EmmaSprite_Pierce_Up_Ring.png",                          
#                    "E_Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_Ring.png", 
#                    "E_Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_Ring.png", 
                    "True", "images/EmmaSprite/EmmaSprite_Pierce_Down_Ring.png", 
                    ),       
            "True", Null(),  
            ),    
        (0,0), ConditionSwitch(                          
            #neck
            "IsOutfitModdedEmma('Neck')", GetModdedString("images/EmmaSprite/EmmaSprite_Neck_", E_Neck, ".png"),
            "E_Neck == 'choker'", "images/EmmaSprite/EmmaSprite_Neck_Choker.png",       
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(
            #Water effect 
            "not E_Water", Null(),             
            "Emma_Arms == 1 or E_Chest == 'corset'", "images/EmmaSprite/EmmaSprite_Water_TitsUp.png",  
            "True", "images/EmmaSprite/EmmaSprite_Water_TitsDown.png", #if E_Arms == 1      
            ), 
        (0,0), ConditionSwitch(                                                                         #Chest layer
            "E_Uptop and E_Chest", ConditionSwitch(   
                            #if her top is up. . .
                            "E_Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Bra_Sports_Up.png",   
                            "E_Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Bra_Lace_Up.png",   
                            "E_Chest == 'bikini top'", "images/EmmaSprite/EmmaSprite_Bra_Bikini_Up.png",      
                            "E_Chest == 'corset'", "images/EmmaSprite/EmmaSprite_CorsetTits_Up.png",  
                            "True", Null(), 
                            ),    
            "not E_Chest", Null(),
            "E_Chest == 'modded black corset' and E_Over", "images/EmmaSprite/EmmaSprite_Chest_modded black corset_TitsX.png",   
            "IsOutfitModdedEmma('Chest')", GetModdedString("images/EmmaSprite/EmmaSprite_Chest_", E_Chest, ".png"),
            "E_Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Bra_Sports.png",   
            "E_Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Bra_Lace.png",   
            "E_Chest == 'bikini top'", "images/EmmaSprite/EmmaSprite_Bra_Bikini.png",   
            "E_Chest == 'corset' and E_Over", "images/EmmaSprite/EmmaSprite_CorsetTitsX.png",   
            "E_Chest == 'corset'", "images/EmmaSprite/EmmaSprite_CorsetTits.png",   
            "True", Null(),              
            ),       
#        (0,0), ConditionSwitch(                                                                         #soap
#            "E_Water == 3", "images/EmmaSprite/Emma_body_wet3.png",
#            "True", Null(),                 
#            ),
        (0,0), ConditionSwitch(                                                                         #cape layer       
            "E_Uptop or E_Over == 'jacket' or E_Over == 'modded black jacket' or (E_Chest != 'corset' and E_Chest != 'modded black corset')", Null(),  
            "Emma_Arms == 2 and E_Chest == 'modded black corset'", "images/EmmaSprite/EmmaSprite_Chest_modded black corset_cape2.png",              
            "E_Chest == 'modded black corset'", "images/EmmaSprite/EmmaSprite_Chest_modded black corset_cape1.png",
            "Emma_Arms == 2", "images/EmmaSprite/EmmaSprite_Cape2.png",              
            "True", "images/EmmaSprite/EmmaSprite_Cape1.png",  
            ), 
        (0,0), ConditionSwitch(                                                                         #Overshirt layer       
            "not E_Over", Null(),  
            "Emma_Arms == 2", ConditionSwitch(   
                    #if her arms are down, allowing her breasts to sink                    
                    "E_Uptop", ConditionSwitch(   
                                    "E_Chest in ('corset','lace bra','sports bra','bikini top') or E_Chest in ('modded black corset','modded red sports bra','modded white sports bra', 'modded NewX', 'modded NewX black')", ConditionSwitch(   
                                            #If she's wearing a supporting bra. . .
                                            "E_Over == 'jacket'", "images/EmmaSprite/EmmaSprite_Jacket_2Up_Up.png",  
                                            "E_Over == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_Up2_Up.png",   
                                            "True", Null(), 
                                            ),  
                                    #if she's not wearing a supporting bra. . .
                                    "E_Over == 'jacket'", "images/EmmaSprite/EmmaSprite_Jacket_2Down_Up.png",  
                                    "E_Over == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_Up2_Up.png", 
                                    "True", Null(), 
                                    ),    
                    #if not Uptop. . .
                    "E_Chest in ('corset','lace bra','sports bra','bikini top') or E_Chest in ('modded black corset','modded red sports bra','modded white sports bra', 'modded NewX', 'modded NewX black')", ConditionSwitch(   
                            #If she's wearing a supporting bra. . .
                            "IsOutfitModdedEmma('Over')", GetModdedString("images/EmmaSprite/EmmaSprite_Over_", E_Over, "_2Up.png"),
                            "E_Over == 'jacket'", "images/EmmaSprite/EmmaSprite_Jacket_2Up.png",  
                            "E_Over == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_2Up.png",      
                            "E_Over == 'towel'", "images/EmmaSprite/EmmaSprite_Towel_Up2.png",  
                            "True", Null(), 
                            ),  
                    #if she's not wearing a supporting bra. . .
                    "IsOutfitModdedEmma('Over')", GetModdedString("images/EmmaSprite/EmmaSprite_Over_", E_Over, "_2Down.png"),
                    "E_Over == 'jacket'", "images/EmmaSprite/EmmaSprite_Jacket_2Down.png",  
                    "E_Over == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_2Down.png",      
                    "E_Over == 'towel'", "images/EmmaSprite/EmmaSprite_Towel_Down2.png",  
                    "True", Null(), 
                    ),   
            #if her arms are up, preventng her breasts from sinking
            "E_Uptop", ConditionSwitch(   
                            #if her top is up. . .
                            "E_Over == 'jacket'", "images/EmmaSprite/EmmaSprite_Jacket_1Up_Up.png",  
                            "E_Over == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_Up1_Up.png",   
                            "True", Null(), 
                            ),    
            #if her top is not up. . .
            "IsOutfitModdedEmma('Over')", GetModdedString("images/EmmaSprite/EmmaSprite_Over_", E_Over, "_1Up.png"),
            "E_Over == 'jacket'", "images/EmmaSprite/EmmaSprite_Jacket_1Up.png",  
            "E_Over == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_1Up.png",      
            "E_Over == 'towel'", "images/EmmaSprite/EmmaSprite_Towel_Up1.png",               
            "True", Null(), 
            ), 
        (0,0), ConditionSwitch(                                                                         #clothed peircings        
            "not E_Pierce or E_Uptop or (not E_Over and not E_Chest)", Null(),  
            "E_Pierce == 'barbell'", ConditionSwitch(   
                    #if it's the barbell pericings
                    "Emma_Arms == 1", "images/EmmaSprite/EmmaSprite_Pierce_Up_BarOut.png",  
                    "E_Chest in ('corset','lace bra','sports bra','bikini top') or E_Chest in ('modded black corset','modded red sports bra','modded white sports bra', 'modded NewX', 'modded NewX black')", "images/EmmaSprite/EmmaSprite_Pierce_Up_BarOut.png",   
#                    "E_Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_BarOut.png",    
#                    "E_Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_BarOut.png",  
                    "True", "images/EmmaSprite/EmmaSprite_Pierce_Down_BarOut.png", 
                    ),    
            "E_Pierce == 'ring'", ConditionSwitch(   
                    #if it's the ring pericings
                    "Emma_Arms == 1", "images/EmmaSprite/EmmaSprite_Pierce_Up_RingOut.png",  
                    "E_Chest in ('corset','lace bra','sports bra','bikini top') or E_Chest in ('modded black corset','modded red sports bra','modded white sports bra', 'modded NewX', 'modded NewX black')", "images/EmmaSprite/EmmaSprite_Pierce_Up_RingOut.png",   
#                    "E_Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_RingOut.png",    
#                    "E_Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_RingOut.png",  
                    "True", "images/EmmaSprite/EmmaSprite_Pierce_Down_RingOut.png", 
                    ),                 
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(
            #breast spunk      
            "'tits' in E_Spunk", ConditionSwitch(   
                    #if it's the barbell pericings
                    "Emma_Arms == 1", "images/EmmaSprite/EmmaSprite_Spunk_TitsU.png",                     
                    "E_Chest == 'corset'", "images/EmmaSprite/EmmaSprite_Spunk_TitsU.png",   
                    "E_Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Spunk_TitsU.png",    
                    "E_Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Spunk_TitsU.png",  
                    "E_Chest", "images/EmmaSprite/EmmaSprite_Spunk_TitsU.png",        
                    "True", "images/EmmaSprite/EmmaSprite_Spunk_TitsD.png",        
                    ),       
            "True", Null(),  
            ),   
        (55,0), "EmmaSprite_Head", #Head
        (0,0), ConditionSwitch( 
            #hand spunk 
            "Emma_Arms != 2 or 'hand' not in E_Spunk", Null(),  
            "'mouth' in E_Spunk", "images/EmmaSprite/EmmaSprite_Spunk_HandM.png", 
            "True", "images/EmmaSprite/EmmaSprite_Spunk_Hand.png",   
            ),  
#        (0,0), ConditionSwitch(                                                                         #Props
#            "not E_Held or Emma_Arms != 2", Null(), 
#            "Emma_Arms == 2 and E_Held == 'phone'", "images/EmmaSprite/Emma_held_phone.png",
#            "Emma_Arms == 2 and E_Held == 'dildo'", "images/EmmaSprite/Emma_held_dildo.png",
#            "Emma_Arms == 2 and E_Held == 'vibrator'", "images/EmmaSprite/Emma_held_vibrator.png",
#            "Emma_Arms == 2 and E_Held == 'panties'", "images/EmmaSprite/Emma_held_panties.png",
#            "True", Null(), 
#            ),        
        (0,0), ConditionSwitch(
            #UI tool for When Emma is masturbating using Trigger3 actions
            "E_Loc == 'bg teacher'", Null(),
            "Trigger == 'lesbian' or not Trigger3 or Ch_Focus != 'Emma'", Null(),
            
            #this is not a lesbian thing, and a trigger is set, and Emma is the primary. . .
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_ESelf",  
            "Trigger3 == 'fondle breasts'", ConditionSwitch(                                                                      
                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeLeftBreast_E", 
                        #When zero is working the right breast, fondle left
                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeRightBreast_E",   
                        #When zero is working the left breast, fondle right
                    "True", "GirlGropeBothBreast_E",
                        #else, fondle both
                    ),  
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast_E",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy_E",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy_E",
            "Trigger3 == 'vibrator anal'", "VibratorAnal_E",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy_E",            
            "True", Null(),             
            ),                        
        (0,0), ConditionSwitch(  
            #UI tool for Trigger5(Threesome masutrbation) actions
            "E_Loc == 'bg teacher'", Null(),
            "not Trigger5 or Trigger4 != 'masturbation' or Ch_Focus == 'Emma'", Null(), 
            
            #Emma is not primary, and T4 is masturbation, and a T5 is selected
            "Trigger5 == 'fondle pussy' and Trigger != 'sex' and E_Lust >= 70", "GirlFingerPussy_E",
            "Trigger5 == 'fondle pussy'", "GirlGropePussy_E",
            "Trigger5 == 'fondle breasts'", "GirlGropeRightBreast_E",
            "Trigger5 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger5 == 'vibrator pussy'", "VibratorPussy",
            "Trigger5 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger5 == 'vibrator anal'", "VibratorAnal",
            "Trigger5 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(), 
            ),               
        (0,0), ConditionSwitch(                
            #UI tool for Trigger1(primary) actions
            "E_Loc == 'bg teacher'", Null(),
            "not Trigger or Ch_Focus != 'Emma'", Null(),
            
            # Emma is primary and a sex trigger is active
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast_E",
            "Trigger == 'fondle thighs'", "GropeThigh_E",
            "Trigger == 'fondle breasts'", "GropeLeftBreast_E",
            "Trigger == 'suck breasts'", "LickRightBreast_E",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_E",
            "Trigger == 'fondle pussy'", "GropePussy_E",
            "Trigger == 'lick pussy'", "Lickpussy_E",
            "Trigger == 'vibrator pussy'", "VibratorPussy_E",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy_E",
            "Trigger == 'vibrator anal'", "VibratorAnal_E",
            "Trigger == 'vibrator anal insert'", "VibratorPussy_E",
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                
            #UI tool for Trigger2(secondary) actions
            "E_Loc == 'bg teacher'", Null(),
            "not Trigger2 or Ch_Focus != 'Emma'", Null(),
            
            #Emma is primary and an offhand trigger is active            
            "Trigger2 == 'fondle breasts'", ConditionSwitch(                                                                      
                    "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast_E", 
                        #When zero is sucking on the right breast, fondle left
                    "True", "GropeRightBreast_E",
                        #else, fondle right
                    ),  
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast_E",       
                #When sucking right breast, vibrator left            
            "Trigger2 == Trigger", Null(),
                #When both triggers are the same, do nothing              
            "Trigger2 == 'suck breasts'", "LickLeftBreast_E",        
            "Trigger2 == 'fondle pussy'", "GropePussy_E",
            "Trigger2 == 'lick pussy'", "Lickpussy_E",       
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast_E",
            "Trigger2 == 'vibrator pussy'", "VibratorPussy_E",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy_E",
            "Trigger2 == 'vibrator anal'", "VibratorAnal_E",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy_E",
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(  
            #UI tool for Trigger4(Threesome) actions (ie Rogue's hand on her)
            "E_Loc == 'bg teacher'", Null(),
            "not Trigger4 or Ch_Focus != 'Emma'", Null(),
            
            # There is a threesome trigger set and Emma is the target of it
            "Trigger4 == 'fondle pussy' and Trigger != 'sex' and E_Lust >= 70", "GirlFingerPussy_E",
            "Trigger4 == 'fondle pussy'", "GirlGropePussy_E",            
            "Trigger4 == 'lick pussy'", "Lickpussy_E",
            "Trigger4 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_E", 
            "Trigger4 == 'suck breasts'", "LickRightBreast_E",              
            "Trigger4 == 'fondle breasts'", ConditionSwitch( 
                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeLeftBreast_E",   
                        #When zero is working the right breast, fondle left                                                  
#                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeRightBreast_E", 
#                        #When zero is working the left breast, fondle right                                         
#                    "Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts'", "GirlGropeRightBreast_E", 
#                        #When zero is working the left breast, fondle right 
                    "True", "GirlGropeRightBreast_E",
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
            "E_Loc == 'bg teacher'", Null(),
            "Trigger != 'lesbian' or Ch_Focus == 'Emma' or not Trigger3", Null(),
            
            # If there is a Trigger3 and Emma is not the focus
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and E_Lust >= 70", "GirlFingerPussy_E",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_E",            
            "Trigger3 == 'lick pussy'", "Lickpussy_E",
            "Trigger3 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_E", 
            "Trigger3 == 'suck breasts'", "LickRightBreast_E",              
            "Trigger3 == 'fondle breasts'", ConditionSwitch( 
                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeLeftBreast_E",   
                        #When zero is working the right breast, fondle left                                                  
                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeRightBreast_E", 
                        #When zero is working the left breast, fondle right                                         
                    "Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts'", "GirlGropeLeftBreast_E", 
                        #When zero is working the right breast, fondle left 
                    "True", "GirlGropeRightBreast_E",
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
    (0,0), ConditionSwitch(             
        "not E_HairColor", "images/EmmaSprite/EmmaSprite_Head_HairBackWet.png",             
        "True", im.MatrixColor("images/EmmaSprite/EmmaSprite_Head_HairWhiteBackWet.png",im.matrix.tint(float(E_HairCustomColor.red)/255.0, float(E_HairCustomColor.green)/255.0, float(E_HairCustomColor.blue)/255.0)),             
        ),  
    anchor (0.6, 0.0)                
    zoom .5                   
    
image EmmaSprite_Head:
    LiveComposite(
        (555,673), 
#        (0,0), ConditionSwitch(                                                                         #hair back 
#            "E_Hair", "images/EmmaSprite/EmmaSprite_Hairback.png",   
#            "True", Null(),        
#            ),      

#        (0,0), ConditionSwitch(                                                                         #Face no blush not wet
#            "E_Blush or E_Hair == 'wet' or E_Water", Null(),        
#            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_Angry.png",
#            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_Sad.png",
#            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_Surprised.png",     
#            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_Confused.png", 
#            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_Normal.png", #E_Brows == 'normal'
#            ),
#        (0,0), ConditionSwitch(                                                                         #Face blush 1 not wet
#            "E_Blush != 1 or E_Hair == 'wet' or E_Water", Null(),        
#            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_AngryB1.png",
#            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_SadB1.png",
#            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_SurprisedB1.png",   
#            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_ConfusedB1.png", 
#            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_NormalB1.png", #E_Brows == 'normal'
#            ),
#        (0,0), ConditionSwitch(                                                                         #Face blush 2 not wet
#            "E_Blush != 2 or E_Hair == 'wet' or E_Water", Null(),        
#            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_AngryB2.png",
#            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_SadB2.png",
#            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_SurprisedB2.png",    
#            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_ConfusedB2.png", 
#            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_NormalB2.png", #E_Brows == 'normal'
#            ),
        
#         (0,0), ConditionSwitch(                                                                         #Face no blush wet
#            "E_Blush or (E_Hair != 'wet' and not E_Water)", Null(),        
#            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_Angry.png",
#            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_Sad.png",
#            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_Surprised.png",    
#            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_Confused.png",  
#            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_Normal.png", #E_Brows == 'normal'
#            ),
#        (0,0), ConditionSwitch(                                                                         #Face blush 1 wet
#            "E_Blush != 1 or (E_Hair != 'wet' and not E_Water)", Null(),        
#            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_AngryB1.png",
#            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_SadB1.png",
#            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_SurprisedB1.png",    
#            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_ConfusedB1.png",    
#            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_NormalB1.png", #E_Brows == 'normal'
#            ),
#        (0,0), ConditionSwitch(                                                                         #Face blush 2 wet
#            "E_Blush != 2 or (E_Hair != 'wet' and not E_Water)", Null(),        
#            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_AngryB2.png",
#            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_SadB2.png",
#            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_SurprisedB2.png",    
#            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_ConfusedB2.png",    
#            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_NormalB2.png", #E_Brows == 'normal'
#            ),
        
        (0,0), ConditionSwitch(
                # Face background plate
                "not E_Blush", ConditionSwitch(
                    #If no Blush
                    "E_Hair == 'wet' or E_Water", ConditionSwitch(
                            #If the hair is wet
                            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_Angry.png",
                            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_Sad.png",
                            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_Surprised.png",    
                            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_Confused.png",  
                            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_Normal.png", #E_Brows == 'normal'
                            ),
                    "True", ConditionSwitch(
                            #If the hair is not wet
                            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_Angry.png",
                            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_Sad.png",
                            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_Surprised.png",     
                            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_Confused.png", 
                            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_Normal.png", #E_Brows == 'normal'
                            ),
                    ),
                "E_Blush == 1", ConditionSwitch(
                    #If the first tier blush
                    "E_Hair == 'wet' or E_Water", ConditionSwitch(
                            #If the hair is wet
                            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_AngryB1.png",
                            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_SadB1.png",
                            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_SurprisedB1.png",    
                            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_ConfusedB1.png",    
                            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_NormalB1.png", #E_Brows == 'normal'
                            ),
                    "True", ConditionSwitch(
                            #If the hair is not wet
                            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_AngryB1.png",
                            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_SadB1.png",
                            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_SurprisedB1.png",   
                            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_ConfusedB1.png", 
                            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_NormalB1.png", #E_Brows == 'normal'
                            ),
                    ),            
                "True", ConditionSwitch(
                    #else, 2nd tier blush
                    "E_Hair == 'wet' or E_Water", ConditionSwitch(
                            #If the hair is wet
                            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_AngryB2.png",
                            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_SadB2.png",
                            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_SurprisedB2.png",    
                            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_ConfusedB2.png",    
                            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_NormalB2.png", #E_Brows == 'normal'
                            ),
                    "True", ConditionSwitch(
                            #If the hair is not wet
                            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_AngryB2.png",
                            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_SadB2.png",
                            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_SurprisedB2.png",    
                            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_ConfusedB2.png", 
                            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_NormalB2.png", #E_Brows == 'normal'
                            ),
                    ),                    
                ),        
        (0,0), ConditionSwitch(                                                                         #Mouths        
            "E_Mouth == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Normal.png",
            "E_Mouth == 'lipbite'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Lipbite.png",
            "E_Mouth == 'sucking'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Surprised.png",            
            "E_Mouth == 'kiss'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Kiss.png",
            "E_Mouth == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Sad.png",
            "E_Mouth == 'smile'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Smile.png",
            "E_Mouth == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Surprised.png",            
            "E_Mouth == 'tongue'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Tongue.png",                
            "E_Mouth == 'grimace'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Smile.png",                 
            "E_Mouth == 'smirk'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Smirk.png",         
            "True", "images/EmmaSprite/EmmaSprite_Head_Mouth_Normal.png",
            ),   
        
        (0,0), ConditionSwitch(                                                                         #Mouth spunk               
            "'mouth' not in E_Spunk", Null(),
            "E_Mouth == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Spunk_MouthOpen.png",            
            "E_Mouth == 'tongue'", "images/EmmaSprite/EmmaSprite_Head_Spunk_MouthTongue.png",            
            "True", "images/EmmaSprite/EmmaSprite_Head_Spunk_Mouth.png",  
            ),  
        
        (0,0), "Emma Blink",                                                                           #Eyes        
        (0,0), ConditionSwitch(                                                                         #brows
            "E_Brows == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal.png",
            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Brows_Angry.png",
            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Brows_Sad.png",
            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Brows_Surprised.png",        
            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Brows_Confused.png",
            "True", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal.png",
            ),         
        (0,0), ConditionSwitch(                                                                         #facial spunk               
            "'facial' in E_Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_Face.png",             
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                         #Hair
            "not E_Hair or E_HairColor", Null(),
            "E_Hair == 'wet' or E_Water", "images/EmmaSprite/EmmaSprite_Head_HairWet.png",
            "E_Hair", "images/EmmaSprite/EmmaSprite_Head_Hair.png",
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                         #Hair
            "not E_Hair or not E_HairColor", Null(),
            "E_Hair == 'wet' or E_Water", im.MatrixColor("images/EmmaSprite/EmmaSprite_Head_HairWhiteWet.png",im.matrix.tint(float(E_HairCustomColor.red)/255.0, float(E_HairCustomColor.green)/255.0, float(E_HairCustomColor.blue)/255.0)),
            "E_Hair", im.MatrixColor("images/EmmaSprite/EmmaSprite_Head_HairWhite.png",im.matrix.tint(float(E_HairCustomColor.red)/255.0, float(E_HairCustomColor.green)/255.0, float(E_HairCustomColor.blue)/255.0)),
            "True", Null(),
            ),        
        (0,0), ConditionSwitch(                                                                         #Hair Water
            "not E_Water", Null(),
            "E_Hair == 'wet'", "images/EmmaSprite/EmmaSprite_Head_Water.png",
            "True", "images/EmmaSprite/EmmaSprite_Head_Water.png",
            ),
        (0,0), ConditionSwitch(                                                                         #hair spunk               
            "'hair' in E_Spunk and (E_Hair == 'wet' or E_Water)", "images/EmmaSprite/EmmaSprite_Head_Spunk_HairWet.png",                         
            "'hair' in E_Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_HairWave.png",              
            "True", Null(),
            ),  
        )                
    anchor (0.6, 0.0)                
    zoom .5   

image Emma Blink:
    ConditionSwitch(
        "E_Eyes == 'sexy'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Sexy.png",
        "E_Eyes == 'side'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Side.png",
        "E_Eyes == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Surprised.png",
        "E_Eyes == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Normal.png",    
        "E_Eyes == 'stunned'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Agao.png",
        "E_Eyes == 'down'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Down.png",
        "E_Eyes == 'closed'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Closed.png",
        "E_Eyes == 'manic'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Surprised.png",
        "E_Eyes == 'squint'", "Emma_Squint",
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
            "P_Sprite and P_Cock == 'in'", ConditionSwitch(                                                               
                    # If during sex
                    "Speed == 1", "Emma_Sex_Legs_S1",#heading
                    "Speed == 2", "Emma_Sex_Legs_S2",#slow
                    "Speed == 3", "Emma_Sex_Legs_S3",#fast
                    "Speed >= 4", "Emma_Sex_Legs_S4",#cumming
                    "True", "Emma_Sex_Legs_S0",#Static
                    ),
            "P_Sprite and P_Cock == 'anal'", ConditionSwitch(                                                              
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
            "P_Sprite and P_Cock == 'in'", ConditionSwitch(                                                               
                    # If during sex
                    "Speed == 1", "Emma_Sex_Body_S1",#heading
                    "Speed == 2", "Emma_Sex_Body_S2",#slow
                    "Speed == 3", "Emma_Sex_Body_S3",#fast
                    "Speed >= 4", "Emma_Sex_Body_S4",#cumming
                    "True",       "Emma_Sex_Body_S0",#Static
                    ),
            "P_Sprite and P_Cock == 'anal'", ConditionSwitch(                                                              
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
            "E_Chest == 'corset'", "images/EmmaSex/Emma_Sex_Tits_Up.png",   # E_TitsUp = 1
            "E_Chest == 'sports bra' or E_Chest == 'lace bra'", "images/EmmaSex/Emma_Sex_Tits_Up.png",   # E_TitsUp = 1
            "True", "images/EmmaSex/Emma_Sex_Tits_Down.png",   # E_TitsUp = 0
            )
    contains:
            # piercings tits
        ConditionSwitch(   
            "renpy.showing('Emma_TJ_Animation')", Null(),
            "not E_Pierce or E_Chest", Null(),
            "E_Over == 'nighty'", Null(),
            "E_Pierce == 'barbell'", ConditionSwitch(   
                    #if it's the ring pericings   
                    "E_Chest in ('corset', 'lace bra', 'sports bra')", Null(),  
                    "True", "images/EmmaSex/Emma_Pierce_Barbell_Tits_D.png", 
                    ),    
            "E_Pierce == 'ring'", ConditionSwitch(   
                    #if it's the ring pericings   
                    "E_Chest in ('corset', 'lace bra', 'sports bra')", Null(),  
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
            "E_Chest == 'corset'", "images/EmmaSex/Emma_Sex_Tits_Up.png",   # E_TitsUp = 1
            "E_Chest == 'sports bra' or E_Chest == 'lace bra'", "images/EmmaSex/Emma_Sex_Tits_Up.png",   # E_TitsUp = 1
            "True", "images/EmmaSex/Emma_Sex_Tits_Down.png",   # E_TitsUp = 0
            )
    contains:
            # piercings tits
        ConditionSwitch(   
            "renpy.showing('Emma_TJ_Animation')", Null(),
            "not E_Pierce or E_Over or E_Chest", Null(),
            "E_Pierce == 'barbell'", ConditionSwitch(   
                    #if it's the ring pericings   
                    "E_Chest in ('corset', 'lace bra', 'sports bra')", Null(),  
                    "True", "images/EmmaSex/Emma_Pierce_Barbell_Tits_D.png", 
                    ),    
            "E_Pierce == 'ring'", ConditionSwitch(   
                    #if it's the ring pericings   
                    "E_Chest in ('corset', 'lace bra', 'sports bra')", Null(),  
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
                "not renpy.showing('Emma_TJ_Animation')", Null(),   # E_TitsUp = 0
                "E_Chest == 'sports bra'", "images/EmmaSex/Emma_Sex_Bra_Sports_TJU.png",
                "True", Null(),
                ) 
    contains:
            # Chest clothing layer
        ConditionSwitch(    
            "not E_Chest or renpy.showing('Emma_TJ_Animation')", Null(),   # E_TitsUp = 0
            "E_Chest == 'corset'", "images/EmmaSex/Emma_Sex_Bra_Corset_Up.png",   # E_TitsUp = 1
            "E_Chest == 'sports bra'", "images/EmmaSex/Emma_Sex_Bra_Sports_Up.png",   # E_TitsUp = 1
            "E_Chest == 'lace bra'", "images/EmmaSex/Emma_Sex_Bra_Lace_Up.png",   # E_TitsUp = 1
            "True", Null(),   # E_TitsUp = 0
            )
    contains:
            # Over clothing layer
        ConditionSwitch(   
            "E_Over == 'jacket'", ConditionSwitch(   
                    #if it's the ring pericings                       
                    "renpy.showing('Emma_TJ_Animation')", Null(),
#                    "renpy.showing('Emma_TJ_Animation')", "images/EmmaSex/Emma_Sex_Jacket_Down.png",
                    "E_Chest == 'corset'", "images/EmmaSex/Emma_Sex_Jacket_Up.png",   # E_TitsUp = 1
                    "E_Chest == 'sports bra'", "images/EmmaSex/Emma_Sex_Jacket_Up.png",   # E_TitsUp = 1
                    "E_Chest == 'lace bra'", "images/EmmaSex/Emma_Sex_Jacket_Up.png",   # E_TitsUp = 1
                    "True", "images/EmmaSex/Emma_Sex_Jacket_Down.png",   # E_TitsUp = 0
                    ),                
            "E_Over == 'nighty'", ConditionSwitch(
                    #if she has the nighty on     
                    "renpy.showing('Emma_TJ_Animation')", Null(),
                    "E_Chest in ('corset', 'lace bra', 'sports bra')", "images/EmmaSex/Emma_Sex_Nighty_Up.png",  
                    "True", "images/EmmaSex/Emma_Sex_Nighty_Down.png", 
                    ),    
            "True", Null(), 
            )
    contains:
            # spunk on tits
            ConditionSwitch(    
                "'tits' not in E_Spunk", Null(),
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
            "Emma_Arms == 3", Null(),   # Neither arms
            "Emma_Arms == 4", AlphaMask("Emma_Arms", "images/EmmaSex/Emma_Sex_ArmsMask_R.png"),   # Right arm only
            "Emma_Arms == 5", AlphaMask("Emma_Arms", "images/EmmaSex/Emma_Sex_ArmsMask_L.png"),   # Left arm only
            "True", AlphaMask("Emma_Arms", "images/EmmaSex/Emma_Sex_ArmsMask.png"),  # Both Arms
            )
    contains:
            "Emma_Sex_Head"
    zoom 1 
#    offset (0,0)
# end Emma's sex body torso / / / / / torso / / / / / torso / / / / / torso / / / / / torso / / / / /


image Emma_Arms:
    contains:
            # Base Arms
        ConditionSwitch(    
            "E_Over == 'jacket'", Null(),
            "E_Chest == 'corset'", "images/EmmaSex/Emma_Sex_Arms_U.png",   # E_TitsUp = 1
            "E_Chest == 'sports bra'", "images/EmmaSex/Emma_Sex_Arms_U.png",   # E_TitsUp = 1
            "E_Chest == 'lace bra'", "images/EmmaSex/Emma_Sex_Arms_U.png",   # E_TitsUp = 1
            "True", "images/EmmaSex/Emma_Sex_Arms_D.png",   # E_TitsUp = 0
            )
    contains:
            # Arm clothing
        ConditionSwitch(    
            "E_Over == 'jacket'", Null(),
            "E_Chest == 'sports bra'", "images/EmmaSex/Emma_Sex_Bra_Sports_Arms.png",   # E_TitsUp = 1
            "True", Null(),
            )
    contains:
            # Arm clothing Over
        ConditionSwitch(    
            "E_Over == 'jacket'", "images/EmmaSex/Emma_Sex_Arms_Jacket.png",   # E_TitsUp = 1
            "E_Arms", "images/EmmaSex/Emma_Sex_Gloves.png",           
            "True", Null(),
            )



# Emma's sex body legs / / / / / legs / / / / / legs / / / / / legs / / / / / legs / / / / /
image Emma_Sex_Legs_S:                                                                        
    #Her Legs during sex
    contains:
            # spunk
        ConditionSwitch(    
            "'anal' in E_Spunk or 'in' in E_Spunk", "images/EmmaSex/Emma_Spunk_Sex.png", 
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
            "E_Panties and not E_PantiesDown", Null(), 
            "E_Legs and not E_Upskirt", Null(), 
            "E_Pierce == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_S.png", 
            "E_Pierce == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S.png",
            "True", Null(), 
            )
    contains:
            # pubes
        ConditionSwitch(    
            "E_Pubes", "images/EmmaSex/Emma_Pubes_Sex.png", 
            "True", Null(),
            )        
    contains:
            # panties
        ConditionSwitch(    
            "E_PantiesDown", Null(),
            "E_Panties == 'sports panties' and E_Wet", "images/EmmaSex/Emma_Sex_Panties_Sport_SW.png", 
            "E_Panties == 'sports panties'", "images/EmmaSex/Emma_Sex_Panties_Sport_S.png", 
            "E_Panties and E_Wet", "images/EmmaSex/Emma_Sex_Panties_SW.png", 
            "E_Panties", "images/EmmaSex/Emma_Sex_Panties_S.png", 
            "True", Null(),
            )         
    contains:
            # boots
        ConditionSwitch(    
            "E_Boots == 'thigh boots'", "images/EmmaSex/Emma_Sex_Boots_Pussy.png", 
            "True", Null(),
            )              
    contains:
            # legs
        ConditionSwitch(    
            "E_Legs == 'skirt'", "images/EmmaSex/Emma_Sex_Skirt_Pussy.png", 
            "E_Upskirt", Null(),
            "E_Legs == 'pants' and E_Wet >= 2", "images/EmmaSex/Emma_Sex_Pants_SW.png", 
            "E_Legs == 'pants'", "images/EmmaSex/Emma_Sex_Pants_S.png", 
            "True", Null(),
            )
    contains:
            # Over
        ConditionSwitch(    
            "E_Over == 'nighty'", "images/EmmaSex/Emma_Sex_Nighty_Pussy.png", 
            "True", Null(),
            )
    contains:
            # spunk
        ConditionSwitch(    
            "'belly' in E_Spunk", "images/EmmaSex/Emma_Spunk_Belly.png", 
            "True", Null(),
            )
    zoom 1 
#    offset (0,0)

image Emma_Sex_Legs_A:                        
    #Her Legs during anal
    contains:
            # anal spunk
        ConditionSwitch(    
            "'anal' in E_Spunk and not Speed", "images/EmmaSex/Emma_Spunk_Anal_Closed.png", 
            "True", Null(),
            )
    contains:
            # Legs Base
            "images/EmmaSex/Emma_Sex_Legs_Anal.png"
    contains:
            #Anus
        ConditionSwitch(  
            "P_Sprite and P_Cock == 'anal' and Speed", ConditionSwitch(                                                              
                    # If during Anal
                    "Speed == 1", "Emma_Sex_Anus_A1",#heading
                    "True", "Emma_Sex_Anus_A2",#faster
                    ),
            "True", "Emma_Sex_Anus_A0",
            ) 
    contains:
            # pubes
        ConditionSwitch(    
            "E_Pubes", "images/EmmaSex/Emma_Pubes_Anal.png", 
            "True", Null(),
            )
    contains:
            # piercings
        ConditionSwitch(    
            "E_Panties and not E_PantiesDown", Null(), 
            "E_Legs and not E_Upskirt", Null(), 
            "E_Pierce == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_A.png", 
            "E_Pierce == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_A.png",
            "True", Null(), 
            )        
    contains:
            # panties
        ConditionSwitch(    
            "E_PantiesDown", Null(),
            "E_Panties == 'sports panties' and E_Wet", "images/EmmaSex/Emma_Sex_Panties_Sport_AW.png", 
            "E_Panties == 'sports panties'", "images/EmmaSex/Emma_Sex_Panties_Sport_A.png", 
            "E_Panties and E_Wet", "images/EmmaSex/Emma_Sex_Panties_AW.png", 
            "E_Panties", "images/EmmaSex/Emma_Sex_Panties_A.png", 
            "True", Null(),
            )
    contains:
            # pussy spunk
        ConditionSwitch(    
            "'in' in E_Spunk", "images/EmmaSex/Emma_Spunk_Anal_Pussy.png", 
            "True", Null(),
            )         
    contains:
            # boots
        ConditionSwitch(    
            "E_Boots == 'thigh boots'", "images/EmmaSex/Emma_Sex_Boots_Anal.png", 
            "True", Null(),
            )              
    contains:
            # legs
        ConditionSwitch(    
            "E_Legs == 'skirt'", "images/EmmaSex/Emma_Sex_Skirt_Anal.png", 
            "E_Upskirt", Null(),
            "E_Legs == 'pants' and E_Wet >= 2", "images/EmmaSex/Emma_Sex_Pants_AW.png", 
            "E_Legs == 'pants'", "images/EmmaSex/Emma_Sex_Pants_A.png", 
            "True", Null(),
            )
    contains:
            # Over
        ConditionSwitch(    
            "E_Over == 'nighty'", "images/EmmaSex/Emma_Sex_Nighty_Anal.png", 
            "True", Null(),
            )
    contains:
            # spunk
        ConditionSwitch(    
            "'belly' in E_Spunk", "images/EmmaSex/Emma_Spunk_Belly.png", 
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
            "E_Panties and not E_PantiesDown", Null(), 
            "E_Legs and not E_Upskirt", Null(), 
            "E_Pierce == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_S.png", 
            "E_Pierce == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S.png",
            "True", Null(), 
            ) 

image Emma_Sex_Hotdog_Mask:
    contains:
            "images/EmmaSex/Emma_Sex_Legs_HotdogMask.png"
#            yoffset 3
    contains:       
            # piercings
        ConditionSwitch(    
            "E_Panties and not E_PantiesDown", Null(), 
            "E_Legs and not E_Upskirt", Null(), 
            "E_Pierce == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_S.png", 
            "E_Pierce == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S.png",
            "True", Null(), 
            ) 
    contains:
            # piercings
        ConditionSwitch(    
            "E_Panties and not E_PantiesDown", Null(), 
            "E_Legs and not E_Upskirt", Null(), 
            "E_Pierce == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_S.png", 
            "E_Pierce == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S.png",
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
                "P_Sprite", "Zero_Doggy_Insert", 
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
                "P_Sprite", "Zero_Doggy_Insert", 
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
                "P_Sprite", "Zero_Doggy_Insert", 
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
#                "P_Sprite", "Zero_Doggy_Insert", 
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
                "'anal' in E_Spunk", "images/EmmaSex/Emma_Spunk_Anal_Open.png",
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
                    "'anal' in E_Spunk", "images/EmmaSex/Emma_Spunk_Anal_Open.png",
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
                    "'anal' in E_Spunk", "images/EmmaSex/Emma_Spunk_Anal_Open.png",
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
                    "'anal' in E_Spunk", "images/EmmaSex/Emma_Spunk_Anal_Open.png",
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
                "'anal' in E_Spunk", "images/EmmaSex/Emma_Spunk_Anal_Under.png",
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
                "'anal' in E_Spunk", "images/EmmaSex/Emma_Spunk_Anal_Under.png",
                "True", Null(),
                )
        xpos  0 
      
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Emma_Sex_Launch(Line = "solo"): 
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
    if renpy.showing("Emma_SexSprite"):
        return 
    $ P_Sprite = 1
    $ Speed = 0
    hide Emma_Sprite      
    if renpy.showing("Emma_BJ_Animation"):
        hide Emma_BJ_Animation
    if renpy.showing("Emma_HJ_Animation"):
        hide Emma_HJ_Animation
    if renpy.showing("Emma_TJ_Animation"):
        hide Emma_TJ_Animation
    
    if E_Legs:          #temporary, change or remove when other clothing options are available
        $ E_Upskirt = 1
    if E_Panties:       #temporary, change or remove when other clothing options are available
        $ E_PantiesDown = 1
                
    show Emma_SexSprite zorder 150:
        pos (575,470)
    with dissolve
    return
    
#MOD MARKER RESET
label Emma_Sex_Reset:
    if not renpy.showing("Emma_SexSprite") and not renpy.showing("Emma_Doggy"):
        return
    $ Emma_Arms = 2     
    call mod_hide_Emma_SexSprite  
    call Emma_Hide 
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
        alpha 1
        zoom 1 offset (0,0) 
        anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return

# End Emma Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Emma TJ Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Emma TJ annimation element ///////////////////////////////////////////////////////////////////////////                                     Core Emma BJ element
                
image Emma_TJ_Animation:
    #core titjob animation   
    contains:
        ConditionSwitch(                                                              
            # Emma's upper body
            "P_Sprite", ConditionSwitch(                                                               
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
            "not E_Pierce", Null(),
            "E_Pierce == 'barbell'", ConditionSwitch(   
                    #if it's the ring pericings   
#                    "E_Chest in ('corset', 'lace bra', 'sports bra')", Null(),  
                    "True", "images/EmmaSex/Emma_Pierce_Barbell_Tits_T.png", 
                    ),    
            "E_Pierce == 'ring'", ConditionSwitch(   
                    #if it's the ring pericings   
#                    "E_Chest in ('corset', 'lace bra', 'sports bra')", Null(),  
                    "True", "images/EmmaSex/Emma_Pierce_Ring_Tits_T.png", 
                    ),                    
            "True", Null(), 
            )
    contains:
            #chest clothing layer
        ConditionSwitch(    
            "not E_Chest", Null(),   # E_TitsUp = 0
            "E_Chest == 'sports bra'", "images/EmmaSex/Emma_Sex_Bra_Sports_TJ.png",   # E_TitsUp = 1
            "E_Chest == 'lace bra'", "images/EmmaSex/Emma_Sex_Bra_Lace_TJ.png",   # E_TitsUp = 1
            "True", Null(),   # E_TitsUp = 0
            )
    contains:
            # piercings over clothes
        ConditionSwitch(   
            "not E_Pierce or not E_Chest", Null(),
            "E_Pierce == 'barbell'", ConditionSwitch(   
                    #if it's the ring pericings   
                    "E_Chest in ('corset', 'lace bra', 'sports bra')", "images/EmmaSex/Emma_Pierce_Barbell_Tits_TC.png", 
                    "True", Null(),
                    ),    
            "E_Pierce == 'ring'", ConditionSwitch(   
                    #if it's the ring pericings   
                    "E_Chest in ('corset', 'lace bra', 'sports bra')", "images/EmmaSex/Emma_Pierce_Ring_Tits_TC.png", 
                    "True", Null(),
                    ),                    
            "True", Null(), 
            )
    contains:
            # spunk on tits
        ConditionSwitch(    
                "'tits' in E_Spunk", "images/EmmaSex/Emma_Spunk_Titjob_Over.png",
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
                "P_Sprite", "Blowcock",
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
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
        alpha 1
        ease 1 zoom 2 xpos 550 yoffset 50 #offset (-100,50) 
    if Taboo: # Emma gets started. . .
        if R_Loc == bg_current:
            "Emma looks back at Rogue to see if she's watching."
        elif K_Loc == bg_current:
            "Emma looks back at Kitty to see if she's watching."
        else:
            "Emma looks around to see if anyone can see her."
    
#    if E_Chest and E_Over:
#        "She throws off her [E_Over] and her [E_Chest]."                
#    elif E_Over:
#        "She throws off her [E_Over], baring her breasts underneath."
#    elif E_Chest:
#        "She tugs off her [E_Chest] and throws it aside."
#    $ E_Over = 0
#    $ E_Chest = 0
    $ Emma_Arms = 0
    
#    call Emma_First_Topless      #restore if topless          
    
#    if not E_Tit and Line == "L": #first time
#        if not E_Chest and not E_Over:
#            "As you pull out your cock, Emma hesitantly places it between her breasts and starts to rub them up and down the shaft."
#        elif E_Chest and not E_Over:
#            "As you pull out your cock, Emma hesitantly places it under her [E_Chest], between her breasts and starts to rub them up and down the shaft."
#        elif E_Chest and E_Over:
#            "As you pull out your cock, Emma hesitantly places it under her [E_Over], between her breasts and starts to rub them up and down the shaft."
#        else:
#            "As you pull out your cock, Emma hesitantly places it under her clothes, between her breasts and starts to rub them up and down the shaft."
#    elif Line == "L": #any other time
#        if not E_Chest and not E_Over:
#            "As you pull out your cock, Emma places it between her breasts and starts to rub them up and down the shaft."
#        elif E_Chest and not E_Over:
#            "As you pull out your cock, Emma places it under her [E_Chest], between her breasts and starts to rub them up and down the shaft."
#        elif E_Chest and E_Over:
#            "As you pull out your cock, Emma places it under her [E_Over], between her breasts and starts to rub them up and down the shaft."
#        else:
#            "As you pull out your cock, Emma places it under her clothes, between her breasts and starts to rub them up and down the shaft."    
#    else:
#        "Emma wraps her tits around your cock."
#    hide Emma_Sprite    
    show blackscreen onlayer black with dissolve    
    if E_Over:
        $ E_Over = 0
    if E_Chest == "corset": #test, should I put this back in? 
        $ E_Over = 0
    show Emma_Sprite zorder EmmaLayer:
        alpha 0
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "titjob"
    show Emma_TJ_Animation zorder 150 
    $ P_Sprite = 1
    hide blackscreen onlayer black with dissolve
    return
    
label Emma_TJ_Reset: # The sequence to the Emma animations from Titfuck to default
    if not renpy.showing("Emma_TJ_Animation"):
        return
#    hide Emma_TJ_Animation
    call Emma_Hide 
    $ P_Sprite = 0
    
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
        zoom 2 xpos 550 yoffset 50 #offset (-100,50)  #zoom 2 offset (-100,50)
    show Emma_Sprite zorder EmmaLayer:
        alpha 1
        ease 1 zoom 1.5 xpos 500 yoffset 50
        pause .5
        ease .5 zoom 1 xpos E_SpriteLoc yoffset 0
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
        alpha 1
        zoom 1 offset (0,0) xpos E_SpriteLoc 
        
#    "Emma pulls back"
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
            "Speed < 3 or 'mouth' not in E_Spunk", Null(),
            "Speed == 3", At("EmmaSuckingSpunk", Emma_BJ_Head_3()), #Sucking
            "Speed == 4", At("EmmaSuckingSpunk", Emma_BJ_Head_4()), #Deepthroat
            "Speed == 6", At("EmmaSuckingSpunk", Emma_BJ_Head_6()), #Cumming Deep
            "True", Null(),
            ),    
        (325,490), ConditionSwitch(         #(325,490)                                                        
            # same as above, but for the heading animation
            "Speed == 2 and 'mouth' in E_Spunk", At("Emma_BJ_MaskHeadingSpunk", Emma_BJ_Head_2()), #Heading
#            "Speed == 5 and 'mouth' in E_Spunk", At("Emma_BJ_MaskHeadingSpunkB", Emma_BJ_Head_5()), #Cumming High
            "True", Null(),
            ),   
        )
    zoom .55
    anchor (.5,.5)
    
image Emma_BJ_HairBack:
    #Hair underlay
    ConditionSwitch(                                 
            "E_Water or E_Hair == 'wet'", Null(),
            "E_HairColor", im.MatrixColor("images/EmmaBJFace/Emma_BJ_HairWhite_Wave_Back.png",im.matrix.tint(float(E_HairCustomColor.red)/255.0, float(E_HairCustomColor.green)/255.0, float(E_HairCustomColor.blue)/255.0)),
            "True", "images/EmmaBJFace/Emma_BJ_Hair_Wave_Back.png",
            ),
    zoom 1.4
    anchor (0.5, 0.5)
    
image Emma_BJ_Backdrop:
    contains:                                                                   
            #blanket     
            ConditionSwitch(      
                "'blanket' in E_RecentActions", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
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
            "E_HairColor and (E_Water or E_Hair == 'wet')", im.MatrixColor("images/EmmaBJFace/Emma_BJ_HairWhite_Wet_Mid.png",im.matrix.tint(float(E_HairCustomColor.red)/255.0, float(E_HairCustomColor.green)/255.0, float(E_HairCustomColor.blue)/255.0)),
            "E_Water or E_Hair == 'wet'", "images/EmmaBJFace/Emma_BJ_Hair_Wet_Mid.png",
            "E_HairColor", im.MatrixColor("images/EmmaBJFace/Emma_BJ_HairWhite_Wave_Mid.png",im.matrix.tint(float(E_HairCustomColor.red)/255.0, float(E_HairCustomColor.green)/255.0, float(E_HairCustomColor.blue)/255.0)),
            "True", "images/EmmaBJFace/Emma_BJ_Hair_Wave_Mid.png",
            ),
        (0,0), ConditionSwitch(
            # Basic Face layer
            "Speed <= 2 or Speed == 5 or not renpy.showing('Emma_BJ_Animation')", ConditionSwitch( 
                    # If the animation isn't sucking, or if not in BJ pose
                    "E_Blush", "images/EmmaBJFace/Emma_BJ_FaceClosed_Blush.png",              
                    "True", "images/EmmaBJFace/Emma_BJ_FaceClosed.png",
                    ),  
            "E_Blush", "images/EmmaBJFace/Emma_BJ_FaceOpen_Blush.png",              
            "True", "images/EmmaBJFace/Emma_BJ_FaceOpen.png"
            ),           
        (0,0), ConditionSwitch(                                                                         
            #Mouth
#            "(Speed == 2 or Speed == 5) and renpy.showing('Emma_BJ_Animation')", ConditionSwitch( 
#                    # If the Heading animation is active
##                    "E_Blush", "images/EmmaBJFace/Emma_BJ_FaceClosed_Blush.png",              
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
            "E_Mouth == 'normal'", "images/EmmaBJFace/Emma_BJ_Mouth_Smile.png",
            "E_Mouth == 'lipbite'", "images/EmmaBJFace/Emma_BJ_Mouth_Lipbite.png",
            "E_Mouth == 'sucking'", "images/EmmaBJFace/Emma_BJ_Mouth_Sucking.png",            
            "E_Mouth == 'kiss'", "images/EmmaBJFace/Emma_BJ_Mouth_Kiss.png",
            "E_Mouth == 'sad'", "images/EmmaBJFace/Emma_BJ_Mouth_Sad.png",
            "E_Mouth == 'smile'", "images/EmmaBJFace/Emma_BJ_Mouth_Smile.png",  
            "E_Mouth == 'smirk'", "images/EmmaBJFace/Emma_BJ_Mouth_Smirk.png",           
            "E_Mouth == 'grimace'", "images/EmmaBJFace/Emma_BJ_Mouth_Smile.png",
            "E_Mouth == 'surprised'", "images/EmmaBJFace/Emma_BJ_Mouth_Surprised.png",          
            "E_Mouth == 'tongue'", "images/EmmaBJFace/Emma_BJ_Mouth_Tongue.png",    
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
            "'mouth' not in E_Spunk", Null(), 
            "Speed and renpy.showing('Emma_BJ_Animation')", ConditionSwitch( 
                    # If in sucking position
                    "Speed == 1", "images/EmmaBJFace/Emma_BJ_Spunk_Tongue.png",  #licking
                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", "images/EmmaBJFace/Emma_BJ_Spunk_SuckingUnder.png", #sucking
                    "Speed == 4", "images/EmmaBJFace/Emma_BJ_Spunk_SuckingUnder.png", #deepthroat     
                    "Speed == 6", "images/EmmaBJFace/Emma_BJ_Spunk_SuckingUnder.png", #cumming    
                    ),  
            "E_Mouth == 'normal'", "images/EmmaBJFace/Emma_BJ_Spunk_Smile.png",
            "E_Mouth == 'lipbite'", "images/EmmaBJFace/Emma_BJ_Spunk_Lipbite.png",
            "E_Mouth == 'kiss'", "images/EmmaBJFace/Emma_BJ_Spunk_Kiss.png",
            "E_Mouth == 'sad'", "images/EmmaBJFace/Emma_BJ_Spunk_Sad.png",
            "E_Mouth == 'smile'", "images/EmmaBJFace/Emma_BJ_Spunk_Smile.png", 
            "E_Mouth == 'smirk'", "images/EmmaBJFace/Emma_BJ_Spunk_Smirk.png",
            "E_Mouth == 'surprised'", "images/EmmaBJFace/Emma_BJ_Spunk_Surprised.png",
            "E_Mouth == 'tongue'", "images/EmmaBJFace/Emma_BJ_Spunk_Tongue.png",
            "E_Mouth == 'sucking'", "images/EmmaBJFace/Emma_BJ_Spunk_SuckingUnder.png",
            "True", "images/EmmaBJFace/Emma_BJ_Spunk_Smile.png",
            ),       
        (0,0), ConditionSwitch(                                                                         
            #Brows
            "E_Brows == 'normal'", "images/EmmaBJFace/Emma_BJ_Brows_Normal.png",
            "E_Brows == 'angry'", "images/EmmaBJFace/Emma_BJ_Brows_Angry.png",
            "E_Brows == 'sad'", "images/EmmaBJFace/Emma_BJ_Brows_Sad.png",
            "E_Brows == 'surprised'", "images/EmmaBJFace/Emma_BJ_Brows_Surprised.png",        
            "E_Brows == 'confused'", "images/EmmaBJFace/Emma_BJ_Brows_Confused.png",
            "True", "images/EmmaBJFace/Emma_BJ_Brows_Normal.png",
            ),
        (0,0), "Emma BJ Blink",                                                                
            #Eyes
        (0,0), ConditionSwitch(                                                                 
            #cum on the face
            "'facial' in E_Spunk", "images/EmmaBJFace/Emma_BJ_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                 
            #Hair overlay
            "E_HairColor and (E_Water or E_Hair == 'wet')", im.MatrixColor("images/EmmaBJFace/Emma_BJ_HairWhite_Wet_Top.png",im.matrix.tint(float(E_HairCustomColor.red)/255.0, float(E_HairCustomColor.green)/255.0, float(E_HairCustomColor.blue)/255.0)),
            "E_Water or E_Hair == 'wet'", "images/EmmaBJFace/Emma_BJ_Hair_Wet_Top.png",
            "E_HairColor", im.MatrixColor("images/EmmaBJFace/Emma_BJ_HairWhite_Wave_Top.png",im.matrix.tint(float(E_HairCustomColor.red)/255.0, float(E_HairCustomColor.green)/255.0, float(E_HairCustomColor.blue)/255.0)),
            "True", "images/EmmaBJFace/Emma_BJ_Hair_Wave_Top.png",
            ),
#        (0,0), ConditionSwitch(                                                                 
#            #Hair water overlay
#            "not E_Water", Null(),            
#            "Speed > 2", "images/EmmaBJFace/Emma_BJ_Wet_HeadOpen.png",         
#            "True", "images/EmmaBJFace/Emma_BJ_Wet_HeadClosed.png",
#            ),        
#        (0,0), ConditionSwitch(                                                                 
#            #cum on the hair
#            "'hair' in E_Spunk", "images/EmmaBJFace/Emma_BJ_Spunk_Hair.png",
#            "True", Null(),
#            ),
        )
    zoom 1.4
    anchor (0.5, 0.5)

image Emma BJ Blink:                                                                           
        #eyeblinks
        ConditionSwitch(
            "E_Eyes == 'normal'", "images/EmmaBJFace/Emma_BJ_Eyes_Sexy.png",  
            "E_Eyes == 'sexy'", "images/EmmaBJFace/Emma_BJ_Eyes_Sexy.png",  
            "E_Eyes == 'closed'", "images/EmmaBJFace/Emma_BJ_Eyes_Closed.png",
            "E_Eyes == 'surprised'", "images/EmmaBJFace/Emma_BJ_Eyes_Surprised.png",
            "E_Eyes == 'side'", "images/EmmaBJFace/Emma_BJ_Eyes_Side.png",
            "E_Eyes == 'stunned'", "images/EmmaBJFace/Emma_BJ_Eyes_Surprised.png",
            "E_Eyes == 'down'", "images/EmmaBJFace/Emma_BJ_Eyes_Down.png",
            "E_Eyes == 'manic'", "images/EmmaBJFace/Emma_BJ_Eyes_Surprised.png",
            "E_Eyes == 'squint'", "images/EmmaBJFace/Emma_BJ_Eyes_Squint.png",
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
#            "'mouth' not in E_Spunk", Null(),  
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
        show Emma_Sprite at SpriteLoc(StageCenter) zorder EmmaLayer:
            alpha 1
            ease 1 zoom 2.5 offset (150,80) 
        with dissolve
    else:
        show Emma_Sprite at SpriteLoc(StageCenter) zorder EmmaLayer:
            alpha 1
            zoom 2.5 offset (150,80) 
        with dissolve
        
    $ Speed = 0
    if Taboo and Line == "L": # Emma gets started. . .
            if R_Loc == bg_current:
                "Emma looks back at Rogue to see if she's watching."
            elif K_Loc == bg_current:
                "Emma looks back at Kitty to see if she's watching."
            else:
                "Emma casually glaces around to see if anyone notices what she's doing"
            "She then bends down and puts your cock to her mouth."
    elif Line == "L":    
            "Emma smoothly bends down and places your cock against her cheek."    
            
    
    if Line != "cum":
        $ Trigger = "blow"
    
    show Emma_Sprite zorder EmmaLayer:
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
    
    show Emma_Sprite at SpriteLoc(StageCenter) zorder EmmaLayer:
        alpha 1
        zoom 2.5 offset (150,80) 
    with dissolve
    
    show Emma_Sprite zorder EmmaLayer:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)      
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
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
        show Emma_Sprite at SpriteLoc(StageRight) zorder EmmaLayer:
            alpha 1
            ease 1 zoom 1.7 offset (0,200)#(-50,200)
    else:     
        show Emma_Sprite at SpriteLoc(StageRight) zorder EmmaLayer:
            alpha 1
            ease 1 zoom 1.7 offset (0,200)#(-50,200)
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
    $ Emma_Arms = 1
    show Emma_HJ_Animation at SpriteLoc(StageCenter) zorder 150 with easeinbottom:
        #xoffset 150
        offset (100,250)#(100,250)
    return
    
label Emma_HJ_Reset: # The sequence to the Rogue animations from handjob to default
    if not renpy.showing("Emma_HJ_Animation"):
        return    
    $ Speed = 0            
    $ Emma_Arms = 1
    hide Emma_HJ_Animation with easeoutbottom
    call Emma_Hide 
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
        alpha 1
        zoom 1.7 offset (-50,200)
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause .5
        ease .5 zoom 1 offset (0,0) 
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
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
            "not E_Wet", Null(),
            "E_Legs == 'pants' and not E_Upskirt", Null(),   
            "E_Panties and not E_PantiesDown and E_Wet <= 1", Null(),                   
            "E_Wet == 1", AlphaMask("Wet_Drip","Emma_Drip_Mask"), #only plays if nothing is in the way
            "True", AlphaMask("Wet_Drip2","Emma_Drip_Mask"), #only plays if nothing is in the way
            )
        pos (160,400)   
    contains:    
        ConditionSwitch(                                                                         
            #Spunk nethers        
            "'in' not in E_Spunk and 'anal' not in E_Spunk", Null(),
            "E_Legs == 'pants' and not E_Upskirt", Null(),   
            "True", ConditionSwitch( #Wet = 2+
                    "E_Panties and E_PantiesDown", AlphaMask("Spunk_Drip","Emma_Drip_MaskP"), #"Wet_Drip2",# 
                    "E_Legs == 'pants'", AlphaMask("Spunk_Drip","Emma_Drip_MaskP"),
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
            "E_Hose == 'pantyhose' and not E_Upskirt", "images/EmmaSprite/EmmaSprite_FJRight_Pantyhose.png",
            "E_Hose == 'stockings' or E_Hose == 'stockings and garterbelt'", "images/EmmaSprite/EmmaSprite_FJRight_Stocking.png",                 
            "True", Null(),#Static
            ) 
        zoom 0.75        
    contains:
        ConditionSwitch(
            #Personal Wetness            
            "not E_Wet", Null(),
            "E_Legs and E_Wet <= 1", Null(),
            "E_Legs", "images/EmmaSprite/EmmaSprite_Wet.png",
            "E_Wet == 1", "images/EmmaSprite/EmmaSprite_Wet.png",
            "True", "images/EmmaSprite/EmmaSprite_Wet.png",       #E_Wet >1
            ) 
        zoom .75
    contains:
        #Garter
        ConditionSwitch(    
            "E_Hose == 'garterbelt' or E_Hose == 'stockings and garterbelt'", "images/EmmaSprite/EmmaSprite_FJRight_Garter.png",                 
            "True", Null(),#Static
            ) 
        zoom 0.75
    contains:
        #her basic pants rightside
        ConditionSwitch(
            #pants    
            "not E_Legs", Null(),
            "E_Upskirt", ConditionSwitch(                   
                        #if the skirt's up or pants down 
                        "E_Legs == 'skirt'", "images/EmmaSprite/EmmaSprite_SkirtUp.png", 
                        "True", Null(),
                        ),                    
            "True", ConditionSwitch(  
                        "E_Legs == 'pants'", "images/EmmaSprite/EmmaSprite_FJRight_Pants.png",   
                        "E_Legs == 'yoga pants'", "images/EmmaSprite/EmmaSprite_FJRight_Yoga.png",       
                        "E_Legs == 'skirt'", "images/EmmaSprite/EmmaSprite_FJRight_Skirt.png", 
                        "True", Null(),
                        ),   
            )  
        zoom 0.75
    contains:
        #boots
        ConditionSwitch(       
            "E_Upskirt and E_Legs and E_Legs != 'skirt'", Null(),   
            "E_Boots", "images/EmmaSprite/EmmaSprite_FJRight_Boot.png",       
            "True", Null(),#Static
            ) 
        zoom 0.75        
    contains:
        ConditionSwitch(                                                               
            # Emma's lower body
#            "P_Cock != 'foot'", Null(),                                                             
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
            "E_Legs == 'pants' and not E_Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png",   
            "E_Legs == 'yoga pants' and not E_Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png", 
            "E_Hose == 'pantyhose' and not E_Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Pantyhose.png",
            "E_Hose == 'stockings' or E_Hose == 'stockings and garterbelt'", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Stocking.png",
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
            "E_Hose and E_Hose != 'garterbelt'", "images/EmmaSprite/EmmaSprite_FJFoot_Stocking.png",
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
            "E_Legs == 'pants' and not E_Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png",   
            "E_Legs == 'yoga pants' and not E_Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png", 
            "E_Hose == 'pantyhose' and not E_Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Pantyhose.png",
            "E_Hose == 'stockings' or E_Hose == 'stockings and garterbelt'", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Stocking.png",
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
            "E_Hose and E_Hose != 'garterbelt'", "images/EmmaSprite/EmmaSprite_FJFoot_Stocking.png",
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
            "E_Legs == 'pants' and not E_Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png",   
            "E_Legs == 'yoga pants' and not E_Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png", 
            "E_Hose == 'pantyhose' and not E_Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Pantyhose.png",
            "E_Hose == 'stockings' or E_Hose == 'stockings and garterbelt'", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Stocking.png",
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
            "E_Hose and E_Hose != 'garterbelt'", "images/EmmaSprite/EmmaSprite_FJFoot_Stocking.png",
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
            "E_Legs == 'pants' and not E_Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png",   
            "E_Legs == 'yoga pants' and not E_Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png", 
            "E_Hose == 'pantyhose' and not E_Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Pantyhose.png",
            "E_Hose == 'stockings' or E_Hose == 'stockings and garterbelt'", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Stocking.png",
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
            "E_Hose and E_Hose != 'garterbelt'", "images/EmmaSprite/EmmaSprite_FJFoot_Stocking.png",
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
                "P_Sprite", "Blowcock", 
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
            "E_Hose and E_Hose != 'garterbelt'", "images/EmmaSprite/EmmaSprite_FJLeftCalf_Stocking.png",
            "True", "images/EmmaSprite/EmmaSprite_FJLeftCalf.png",
            )            
    contains:
        #her basic legs left calf 
        ConditionSwitch(
            #pants    
            "not E_Legs or E_Upskirt", Null(), 
            "E_Legs == 'pants'", "images/EmmaSprite/EmmaSprite_FJLeftCalf_Pants.png",   
            "E_Legs == 'yoga pants'", "images/EmmaSprite/EmmaSprite_FJLeftCalf_Yoga.png", 
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
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
        alpha 1
        ease 1 zoom .8 xpos 580 yoffset 150
    pause 1

    show Emma_FJ_Chair zorder 10:
        alpha 1
        xpos 590
    show Emma_Sprite zorder EmmaLayer:
        alpha 0
    $ Speed = 0    
    show Emma_FJ_Animation zorder 150:  
        ease .5 alpha 1
    pause 0.5
    show Emma_FJ_Animation zorder 150: 
        alpha 1        
    $ P_Sprite = 1
    return
    
label Emma_FJ_Reset: # The sequence to the Emma animations from Titfuck to default
    if not renpy.showing("Emma_FJ_Animation"):
        return
    call Emma_Hide 
    $ P_Sprite = 0
    
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
        zoom .8 xpos 580 yoffset 150 #offset (-100,50)      
    show Emma_Sprite zorder EmmaLayer:
        alpha 1
        ease .5 zoom 1 xpos E_SpriteLoc yoffset 0 alpha 1  
    pause .5
    
    hide Emma_FJ_Chair zorder 10
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
        alpha 1
        zoom 1 offset (0,0) xpos E_SpriteLoc 
        
    "Emma stands back up."
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
            
        
        
        
        
label E_Kissing_Launch(T = Trigger):    
    call Emma_Hide
    $ Trigger = T
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer
    show Emma_Sprite at SpriteLoc(StageCenter) zorder EmmaLayer:
        ease 0.5 offset (0,0) zoom 2 alpha 1
    return
    
label E_Kissing_Smooch:   
    call EmmaFace("kiss")  
    show Emma_Sprite at SpriteLoc(StageCenter) zorder EmmaLayer:
        ease 0.5 xpos StageCenter offset (0,0) zoom 2 alpha 1
        pause 1
        ease 0.5 xpos E_SpriteLoc zoom 1      
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
        zoom 1
    call EmmaFace("sexy")  
    return
            
label E_Breasts_Launch(T = Trigger):    
    call Emma_Hide
    $ Trigger = T
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
#        ease 0.5 offset (-100,-200) zoom 2
        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
    return
        
label E_Pussy_Launch(T = Trigger):
    call Emma_Hide    
    $ Trigger = T
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
    return
        
label E_Pos_Reset(Pose = 0):    
    call Emma_Hide 
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
        ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
    show Emma_Sprite zorder EmmaLayer:
        offset (0,0) 
        anchor (0.5, 0.0)
        zoom 1   
        xzoom 1 
        yzoom 1
        alpha 1
        pos (E_SpriteLoc,50)
    $ Trigger = Pose
    return
    
#MOD MARKER HIDE
label Emma_Hide:
        if renpy.showing("Emma_SexSprite") or renpy.showing("Emma_Doggy"):
            call Emma_Sex_Reset
        call mod_hide_Emma_SexSprite
        hide Emma_HJ_Animation
        hide Emma_BJ_Animation
        hide Emma_TJ_Animation 
        hide Emma_FJ_Animation 
        return

# Interface items //////////////////////////////////////////////////////////////////////////////

image GropeLeftBreast_E:    
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

image GropeRightBreast_E:    
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
image LickRightBreast_E:   
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
            
image LickLeftBreast_E:   
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

image GropeThigh_E: 
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

image GropePussy_E: 
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

image FingerPussy_E: 
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
            
image Lickpussy_E:   
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

image VibratorRightBreast_E: 
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

image VibratorLeftBreast_E: 
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
            
image VibratorPussy_E: 
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

image VibratorAnal_E: 
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
            
image VibratorPussyInsert_E: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_E: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0



#Lesbian action animations.
image GirlGropeBothBreast_E: 
    contains:
        "GirlGropeLeftBreast_E"
    contains:
        "GirlGropeRightBreast_E"
    
image GirlGropeLeftBreast_E:  
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

image GirlGropeRightBreast_E:    
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

image GirlGropeThigh_E: 
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

image GirlGropePussy_ESelf:
    contains:
        "GirlGropePussy_E"
        anchor (0.5,0.5)
        rotate -40
#        yzoom -1
        pos (120,530)
    
image GirlGropePussy_E: 
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

image GirlFingerPussy_E: 
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

# Start Emma Faces / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label EmmaFace(Emote = E_Emote, B = E_Blush, M = 0, Mouth = 0, Eyes = 0, Brows = 0):
        # Emote is the chosen emote, B is the lush state
        # M is whether the character is in a  manic state                 
        $ Emote = E_Emote if Emote == 5 else Emote
        $ B = E_Blush if B == 5 else B
        
        if (E_Forced or "angry" in E_RecentActions) and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "angry"     
        elif E_ForcedCount > 0 and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "sad"  
            
        if Emote == "normal":
                $ E_Mouth = "normal"
                $ E_Brows = "normal"
                $ E_Eyes = "normal"
        elif Emote == "angry":
                $ E_Mouth = "sad"
                $ E_Brows = "angry"
                $ E_Eyes = "sexy"
        elif Emote == "bemused":
                $ E_Mouth = "normal"
                $ E_Brows = "sad"
                $ E_Eyes = "squint"
        elif Emote == "closed":
                $ E_Mouth = "normal"
                $ E_Brows = "sad"
                $ E_Eyes = "closed"  
        elif Emote == "confused":
                $ E_Mouth = "kiss"
                $ E_Brows = "confused"
                $ E_Eyes = "squint"
        elif Emote == "kiss":
                $ E_Mouth = "kiss"
                $ E_Brows = "sad"
                $ E_Eyes = "closed"
        elif Emote == "tongue":
                $ E_Mouth = "tongue"
                $ E_Brows = "sad"
                $ E_Eyes = "stunned" #"stunned"
        elif Emote == "manic":
                $ E_Mouth = "smile"
                $ E_Brows = "sad"
                $ E_Eyes = "surprised"
                $ E_Blush = 1
        elif Emote == "sad":
                $ E_Mouth = "sad"
                $ E_Brows = "sad"
                $ E_Eyes = "sexy"
        elif Emote == "sadside":
                $ E_Mouth = "sad"
                $ E_Brows = "sad"
                $ E_Eyes = "side"
        elif Emote == "sexy":
                $ E_Mouth = "lipbite"
                $ E_Brows = "normal"
                $ E_Eyes = "squint"
        elif Emote == "smile":
                $ E_Mouth = "smile"
                $ E_Brows = "normal"
                $ E_Eyes = "normal"
        elif Emote == "sucking":
                $ E_Mouth = "sucking"
                $ E_Brows = "surprised"
                $ E_Eyes = "closed"
        elif Emote == "surprised":
                $ E_Mouth = "kiss"
                $ E_Brows = "surprised"
                $ E_Eyes = "surprised"
        elif Emote == "startled":
                $ E_Mouth = "smile"
                $ E_Brows = "surprised"
                $ E_Eyes = "surprised"
        elif Emote == "down":
                $ E_Mouth = "sad"
                $ E_Brows = "sad"
                $ E_Eyes = "down"  
        elif Emote == "perplexed":
                $ E_Mouth = "smile"
                $ E_Brows = "sad"
                $ E_Eyes = "normal"
        elif Emote == "sly":
                $ E_Mouth = "smirk"
                $ E_Brows = "normal"
                $ E_Eyes = "squint"
            
        if M:
                $ E_Eyes = "surprised"        
        if B > 1:
                $ E_Blush = 2
        elif B:
                $ E_Blush = 1
        else:
                $ E_Blush = 0
        
        if Mouth:
                $ E_Mouth = Mouth
        if Eyes:
                $ E_Eyes = Eyes
        if Brows:
                $ E_Brows = Brows
        
        return
        
        
# Emma's Wardrobe //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label EmmaWardrobe:
    menu:      
        "View":
            while True:
                menu:
                    "Default":
                        call E_Pos_Reset
                    "Face":
                        call E_Kissing_Launch(0)
                    "Body":
                        call E_Pussy_Launch(0)
                    "Back":
                        jump EmmaWardrobe 
        # Outfits
#        "Teacher outfit":
#            $ E_Outfit = "teacher"
#            call EmmaOutfit
#        "Super outfit":
#            $ E_Outfit = "costume"
#            call EmmaOutfit
        "Nude":
            $ E_Over = 0
            $ E_Chest = 0
            $ E_Legs = 0
            $ E_Panties = 0
            $ E_Gloves = 0
            $ E_Neck = 0
#            $ E_Outfit = "nude"
#            call EmmaOutfit
        "Over":              
            while True:
                menu:
                    # Overshirts    
                    "Remove [E_Over]" if E_Over:
                        $ E_Over = 0
                    "Add Jacket":
                        $ E_Over = "jacket"  
                    "Add Towel":
                        $ E_Over = "towel" 
                    "Add nighty":
                        $ E_Over = "nighty"   
                    "Toggle up-top":
                        if E_Uptop:
                            $ E_Uptop = 0
                        else:
                            $ E_Uptop = 1  
                    "Toggle Arms":
                        if Emma_Arms == 1:
                            $ Emma_Arms = 2
                        else:
                            $ Emma_Arms = 1 
                    "Back":
                        jump EmmaWardrobe                
        "Tops":            
            while True:
                menu:
                    # Tops    
                    "Remove [E_Chest]" if E_Chest:
                        $ E_Chest = 0
                    "Add corset":
                        $ E_Chest = "corset"
                    "Add sports bra":
                        $ E_Chest = "sports bra"
#                    "Add buttoned tank top" if E_Over != "mesh top":
#                        $ E_Chest = "buttoned tank"
                    "Add lace bra":
                        $ E_Chest = "lace bra"
                    "Add bikini":
                        $ E_Chest = "bikini top"
#                    "Add bra":
#                        $ E_Chest = "bra"                            
                    "Toggle Piercings":
                        if E_Pierce == "ring":
                            $ E_Pierce = "barbell"
                        elif E_Pierce == "barbell":
                            $ E_Pierce = 0
                        else:
                            $ E_Pierce = "ring"   
                    "Toggle up-top":
                        if E_Uptop:
                            $ E_Uptop = 0
                        else:
                            $ E_Uptop = 1 
                    "Toggle Arms":
                        if Emma_Arms == 1:
                            $ Emma_Arms = 2
                        else:
                            $ Emma_Arms = 1
                    "Back":
                        jump EmmaWardrobe             
        
        "Legs":            
            while True:
                menu:
                    # Legs   
                    "Remove legs" if E_Legs:     
                        $ E_Legs = 0
                    "Add pants":
                        $ E_Legs = "pants"
                        $ E_Upskirt = 0
                    "Add yoga pants":
                        $ E_Legs = "yoga pants"
                        $ E_Upskirt = 0
                    "Add skirt":
                        $ E_Legs = "skirt"
                        $ E_Upskirt = 0
                    "Toggle upskirt":
                        if E_Upskirt:
                            $ E_Upskirt = 0
                        else:
                            $ E_Upskirt = 1
                    "Back":
                        jump EmmaWardrobe    
        
        "Underwear":            
            while True:
                menu:
                    # Underwear
                    "Hose":
                        menu:
                            "Add hose":     
                                $ E_Hose = "stockings"  
                            "Add garter":     
                                $ E_Hose = "garterbelt"  
                            "Add stockings and garter":     
                                $ E_Hose = "stockings and garterbelt"  
                            "Add pantyhose":     
                                $ E_Hose = "pantyhose"   
#                            "Add tights":     
#                                $ E_Hose = "tights"   
#                            "Add ripped hose":     
#                                $ E_Hose = "ripped pantyhose"   
#                            "Add ripped tights":     
#                                $ E_Hose = "ripped tights"   
#                            "Add tights":     
#                                $ E_Hose = "tights"    
                            "Remove hose" if E_Hose:     
                                $ E_Hose = 0  

                    "toggle boots":    
                        if not E_Boots:
                            $ E_Boots = "thigh boots"   
                        else:
                            $ E_Boots = 0     
                        
                    "Remove panties" if E_Panties:     
                        $ E_Panties = 0     
                    "Add black panties":
                        $ E_Panties = "white panties"
#                    "Add shorts":
#                        $ E_Panties = "shorts"
                    "Add sports panties":
                        $ E_Panties = "sports panties"  
                    "Add bikini panties":
                        $ E_Panties = "bikini bottoms"  
                    "Add lace panties":
                        $ E_Panties = "lace panties"    
                    "pull down-up panties":
                        if E_PantiesDown:
                            $ E_PantiesDown = 0
                        else:
                            $ E_PantiesDown = 1
                    "Back":
                        jump EmmaWardrobe    
        "Misc":
            while True:
                menu: 
                    "Emotions":
                        call EmmaEmotionEditor
                    "Toggle Arms":
                        if Emma_Arms == 1:
                            $ Emma_Arms = 2
                        else:
                            $ Emma_Arms = 1
                    "Toggle Wetness":
                        if not E_Wet:
                            $ E_Wet = 1
                        elif E_Wet == 1:
                            $ E_Wet = 2
                        else:
                            $ E_Wet  = 0
                    "Toggle wet look":
                        if not E_Water:
                            $ E_Water = 1
                        elif E_Water == 1:
                            $ E_Water = 3
                        else:
                            $ E_Water  = 0
                    "Toggle pubes":
                        if not E_Pubes:
                            $ E_Pubes = 1
                        else:
                            $ E_Pubes = 0
                    "Toggle Pussy Spunk":
                        if "in" in E_Spunk:
                            $ E_Spunk.remove("in")
                        else:
                            $ E_Spunk.append("in")
                    "Toggle Piercings":
                        if E_Pierce == "ring":
                            $ E_Pierce = "barbell"
                        elif E_Pierce == "barbell":
                            $ E_Pierce = 0
                        else:
                            $ E_Pierce = "ring"
                    "Add choker" if not E_Neck:
                        $ E_Neck = "choker"
                    "Remove choker" if E_Neck:
                        $ E_Neck = 0
                        
                    "Add Gloves" if not E_Arms:
                        $ E_Arms = "white gloves"
                    "Remove Gloves" if E_Arms:
                        $ E_Arms = 0
                    "Back":
                        jump EmmaWardrobe               
#        "Set Custom Outfit #1.":
#            $ E_Custom[0] = 1
#            $ E_Custom[1] = E_Arms
#            $ E_Custom[2] = E_Legs
#            $ E_Custom[3] = E_Over
#            $ E_Custom[4] = E_Under #fix, this can be changed to something else, no longer necessary
#            $ E_Custom[5] = E_Chest
#            $ E_Custom[6] = E_Panties 
#            $ E_Custom[7] = E_Pubes 
#            $ E_Custom[8] = E_Hair
#            $ E_Custom[9] = E_Hose
#        "Wear Custom Outfit #[E_Custom[0]]." if E_Custom[0]:
#            $ Line = E_Outfit
#            $ E_Outfit = "custom1"
#            call RogueOutfit
#            $ E_Outfit = Line
        "Nothing":
            return
    jump EmmaWardrobe
return

label EmmaEmotionEditor(CountStore = "normal"):
    menu:
        "Emotions1: Normal Angry Smiling Sexy Surprised Bemused Manic.":        
            menu:
                "Normal":
                    $ E_Emote = "normal"
                    call EmmaFace
                "Angry":
                    $ E_Emote = "angry"
                    call EmmaFace
                "Smiling":
                    $ E_Emote = "smile"
                    call EmmaFace
                "Sexy":
                    $ E_Emote = "sexy"
                    call EmmaFace
                "Suprised":
                    $ E_Emote = "surprised"
                    call EmmaFace
                "Bemused":
                    $ E_Emote = "bemused"
                    call EmmaFace
                "Manic":
                    $ E_Emote = "manic"
                    call EmmaFace
                    
        "Emotions2: Sad Sucking Kiss Tongue Confused Closed Down.":  
            menu:
                "Sad":
                    $ E_Emote = "sad"
                    call EmmaFace
                "Sucking":
                    $ E_Emote = "sucking"
                    call EmmaFace
                "kiss":
                    $ E_Emote = "kiss"
                    call EmmaFace
                "Tongue":
                    $ E_Emote = "tongue"
                    call EmmaFace
                "confused":
                    $ E_Emote = "confused"
                    call EmmaFace
                "Closed":
                    $ E_Emote = "closed"
                    call EmmaFace
                "Down":
                    $ E_Emote = "down"
                    call EmmaFace
                    
        "Emotions3: Sadside Startled Perplexed Sly":  
            menu:
                "Sadside":
                    $ E_Emote = "sadside"
                    call EmmaFace
                "Startled":
                    $ E_Emote = "startled"
                    call EmmaFace
                "Perplexed":
                    $ E_Emote = "perplexed"
                    call EmmaFace
                "Sly":
                    $ E_Emote = "sly"
                    call EmmaFace
        "Toggle Mouth Spunk":
            if "mouth" in E_Spunk:
                $ E_Spunk.remove("mouth")
            else:
                $ E_Spunk.append("mouth")
        "Toggle hand Spunk":
            if "hand" in E_Spunk:
                $ E_Spunk.remove("hand")
            else:
                $ E_Spunk.append("hand")
                
        "Toggle Facial Spunk":
            if "facial" in E_Spunk and "hair" not in E_Spunk:
                $ E_Spunk.append("hair")
            elif "facial" in E_Spunk:
                $ E_Spunk.remove("facial")                
                $ E_Spunk.remove("hair")
            else:
                $ E_Spunk.append("facial")
            
        "Blush":
            if E_Blush == 2:
                $ E_Blush = 1
            elif E_Blush:
                $ E_Blush = 0
            else:
                $ E_Blush = 2  
        "Exit.":
            return
    jump EmmaEmotionEditor
return