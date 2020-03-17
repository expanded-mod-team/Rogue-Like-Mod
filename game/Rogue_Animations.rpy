# Basic character Sprites
image Rogue_Sprite:
    LiveComposite(
        (480,960),
#        (0,0), ConditionSwitch(                                                                         
#            #Overhsirt backing
#            "RogueX.Over == 'mesh top' and RogueX.ArmPose == 1", "images/RogueSprite/Rogue_under_mesh1.png",
#            "RogueX.Over == 'mesh top' and RogueX.ArmPose == 2", "images/RogueSprite/Rogue_under_mesh2.png", 
#            "RogueX.Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty1.png",
#            "RogueX.Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodieB.png",
#            "True", Null(), 
#            ), 
        
        (0,0), ConditionSwitch(                                                                         
            #back of hair
            "renpy.showing('Rogue_BJ_Animation') or renpy.showing('Rogue_TJ_Animation')", Null(),
            "RogueX.Hair == 'evo' and RogueX.Water", Null(),
            "RogueX.Hair == 'evo'", "images/RogueSprite/Rogue_hair_evo_back.png",
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                         
            #shirt layer           
            "not RogueX.Over", Null(),    
            "RogueX.Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodieB.png",         
            "RogueX.Uptop", ConditionSwitch( 
                    #if the top's down. . .
                    "RogueX.ArmPose == 1", ConditionSwitch( 
                            #if the arms are down. . .
                            "RogueX.Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh1_Up.png",           
#                            "RogueX.Over == 'pink top'", "images/RogueSprite/Rogue_over_pink1_Up.png",
#                            "RogueX.Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie1_Up.png",
                            "RogueX.Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty_Up.png",
#                            "RogueX.Over == 'towel'", Null(), 
                            "True", Null(),     
                            ),  
                    "True", ConditionSwitch( 
                            #if the arms are up. . .
                            "RogueX.Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh2_Up.png", 
#                            "RogueX.Over == 'pink top'", "images/RogueSprite/Rogue_over_pink2_Up.png",
#                            "RogueX.Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie2_Up.png",
                            "RogueX.Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty_Up.png",
#                            "RogueX.Over == 'towel'", Null(),       
                            "True", Null(),     
                            ),       
                    ),            
            "True", ConditionSwitch(
                    #if the top's up. . .
                    "RogueX.ArmPose == 1", ConditionSwitch( 
                            #if the arms are down. . .
                            "RogueX.Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh1.png",           
#                            "RogueX.Over == 'pink top'", "images/RogueSprite/Rogue_over_pink1.png",
#                            "RogueX.Over == 'towel'", "images/RogueSprite/Rogue_over_towel1.png",
                            "RogueX.Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty1.png",
#                            "RogueX.Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie1.png",
                            "True", Null(),     
                            ),  
                    "True", ConditionSwitch( 
                            #if the arms are up. . .
                            "RogueX.Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh2.png", 
#                            "RogueX.Over == 'pink top'", "images/RogueSprite/Rogue_over_pink2.png",
#                            "RogueX.Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie2.png",
                            "RogueX.Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty2.png",
#                            "RogueX.Over == 'towel'", "images/RogueSprite/Rogue_over_towel2.png",      
                            "True", Null(),     
                            ),       
                    ),       
            ),
        (0,0), ConditionSwitch(                                                                         
            #body 
            "RogueX.Pubes and RogueX.Pierce == 'ring'", "images/RogueSprite/Rogue_bodyhaired_ring.png",
            "RogueX.Pubes and RogueX.Pierce == 'barbell'", "images/RogueSprite/Rogue_bodyhaired_barbell.png",
            "RogueX.Pierce == 'ring'", "images/RogueSprite/Rogue_body_ring.png",            
            "RogueX.Pierce == 'barbell'", "images/RogueSprite/Rogue_body_barbell.png",
            "RogueX.Pubes", "images/RogueSprite/Rogue_bodyhaired_bare.png",   
            "True", "images/RogueSprite/Rogue_body_bare.png",         
            ),              
        (0,0), ConditionSwitch(                                                                         
            #head 
            "renpy.showing('Rogue_BJ_Animation') or renpy.showing('Rogue_TJ_Animation')", Null(),
#            "RogueX.Hair == 'evo' and RogueX.Water", "images/RogueSprite/Rogue_head_evowet.png",
            "RogueX.Hair == 'evo' and RogueX.Blush == 2", "images/RogueSprite/Rogue_head_evo_blush2.png",
            "RogueX.Hair == 'evo' and RogueX.Blush", "images/RogueSprite/Rogue_head_evo_blush.png",
            "RogueX.Hair == 'evo'", "images/RogueSprite/Rogue_head_evo.png",
            "True", "images/RogueSprite/Rogue_head_evo.png",
            ),  
        (0,0), ConditionSwitch(                                                                         
            #pants backing/hose    
            "RogueX.Hose == 'stockings'", "images/RogueSprite/Rogue_hose.png",     
            "RogueX.Legs == 'pants' and RogueX.Upskirt", "images/RogueSprite/Rogue_pantsback.png", 
            "True", Null(), 
            ),
#        (0,0), ConditionSwitch(                                                                         
#            #Panties            
#            "not RogueX.Panties", Null(),
#            "RogueX.Legs == 'pants' and not RogueX.Upskirt", "images/RogueSprite/Rogue_panties.png",             
#            "RogueX.Panties == 'shorts' and RogueX.PantiesDown and RogueX.Wet > 1", "images/RogueSprite/Rogue_shorts_down_wet.png",
#            "RogueX.Panties == 'shorts' and RogueX.PantiesDown", "images/RogueSprite/Rogue_shorts_down.png",  
#            "RogueX.Panties == 'shorts' and RogueX.Wet > 1", "images/RogueSprite/Rogue_shorts_wet.png",          
#            "RogueX.Panties == 'shorts'", "images/RogueSprite/Rogue_shorts.png",
#            "RogueX.Panties == 'green panties' and RogueX.PantiesDown and RogueX.Wet > 1", "images/RogueSprite/Rogue_undies_down_wet.png",
#            "RogueX.Panties == 'green panties' and RogueX.PantiesDown", "images/RogueSprite/Rogue_undies_down.png",  
#            "RogueX.Panties == 'green panties' and RogueX.Wet > 1", "images/RogueSprite/Rogue_undies_wet.png",          
#            "RogueX.Panties == 'green panties'", "images/RogueSprite/Rogue_undies.png",
#            "RogueX.Panties and RogueX.PantiesDown", "images/RogueSprite/Rogue_panties_down.png",      
#            "RogueX.Panties == 'lace panties'", "images/RogueSprite/Rogue_lacepanties.png",         
#            "True", "images/RogueSprite/Rogue_panties.png",            
#            ),       
        (0,0), ConditionSwitch(                                                                         
            #panties           
            "not RogueX.Panties", Null(),     
            "RogueX.Legs == 'pants' and not RogueX.Upskirt", "images/RogueSprite/Rogue_panties.png",          
            "RogueX.PantiesDown", ConditionSwitch( 
                    #if the panties's down. . .
                    "RogueX.Wet > 1", ConditionSwitch( 
                            #if the panties's are wet. . .
                            "RogueX.Panties == 'shorts'", "images/RogueSprite/Rogue_shorts_down_wet.png",
                            "RogueX.Panties == 'green panties'", "images/RogueSprite/Rogue_undies_down_wet.png",
                            "RogueX.Panties == 'bikini bottoms'", "images/RogueSprite/Rogue_panties_bikini_down.png",  
                            "True", "images/RogueSprite/Rogue_panties_down.png", 
                            ),    
                    "True", ConditionSwitch( 
                            #if the panties's are not wet. . .
                            "RogueX.Panties == 'shorts'", "images/RogueSprite/Rogue_shorts_down.png",  
                            "RogueX.Panties == 'green panties'", "images/RogueSprite/Rogue_undies_down.png",  
                            "RogueX.Panties == 'bikini bottoms'", "images/RogueSprite/Rogue_panties_bikini_down.png",  
                            "True", "images/RogueSprite/Rogue_panties_down.png",     
                            ),     
                    ),            
            "True", ConditionSwitch(
                    #if the panties's up. . .
                    "RogueX.Wet > 1", ConditionSwitch( 
                            #if the panties's are wet. . .
                            "RogueX.Panties == 'shorts' and RogueX.Wet > 1", "images/RogueSprite/Rogue_shorts_wet.png",     
                            "RogueX.Panties == 'green panties' and RogueX.Wet > 1", "images/RogueSprite/Rogue_undies_wet.png",     
                            "RogueX.Panties == 'lace panties'", "images/RogueSprite/Rogue_lacepanties.png",    
                            "RogueX.Panties == 'bikini bottoms'", "images/RogueSprite/Rogue_panties_bikini.png",       
                            "True", "images/RogueSprite/Rogue_panties.png",     
                            ),    
                    "True", ConditionSwitch( 
                            #if the panties's are not wet. . .     
                            "RogueX.Panties == 'shorts'", "images/RogueSprite/Rogue_shorts.png",       
                            "RogueX.Panties == 'green panties'", "images/RogueSprite/Rogue_undies.png",   
                            "RogueX.Panties == 'lace panties'", "images/RogueSprite/Rogue_lacepanties.png",   
                            "RogueX.Panties == 'bikini bottoms'", "images/RogueSprite/Rogue_panties_bikini.png",       
                            "True", "images/RogueSprite/Rogue_panties.png",         
                            ),    
                    ),       
            ),
        (0,0), ConditionSwitch(                                                                         
            #full hose/tights              
            "RogueX.Panties and RogueX.PantiesDown", Null(), 
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueSprite/Rogue_hose_garter.png",  
            "RogueX.Hose == 'garterbelt'", "images/RogueSprite/Rogue_garters.png",                 
            "RogueX.Hose == 'pantyhose'", "images/RogueSprite/Rogue_hosefull.png",       
            "RogueX.Hose == 'tights' and RogueX.Wet", "images/RogueSprite/Rogue_tights_wet.png",
            "RogueX.Hose == 'tights'", "images/RogueSprite/Rogue_tights.png",
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueSprite/Rogue_hose_holed.png", 
            "RogueX.Hose == 'ripped tights'", "images/RogueSprite/Rogue_tights_holed.png",   
            "True", Null(), 
            ),
        (240,560), ConditionSwitch(                                                                         
            #Personal Wetness            
            "not RogueX.Wet", Null(),
            "RogueX.Legs == 'pants' and not RogueX.Upskirt", Null(),   
            "RogueX.Panties and not RogueX.PantiesDown and RogueX.Wet <= 1", Null(),                   
            "RogueX.Wet == 1", ConditionSwitch( #Wet = 1
                    "RogueX.Panties and RogueX.PantiesDown", AlphaMask("Wet_Drip","Rogue_Drip_MaskP"),  
                    "RogueX.Legs == 'pants'", AlphaMask("Wet_Drip","Rogue_Drip_MaskPn"),
                    "True", AlphaMask("Wet_Drip","Rogue_Drip_Mask"), #only plays if nothing is in the way
                    ),
            "True", ConditionSwitch( #Wet = 2+
                    "RogueX.Panties and RogueX.PantiesDown", AlphaMask("Wet_Drip2","Rogue_Drip_MaskP"), #"Wet_Drip2",# 
                    "RogueX.Panties and RogueX.Legs == 'pants'", AlphaMask("Wet_Drip","Rogue_Drip_MaskPn"), #"Wet_Drip2",# 
                    "RogueX.Legs == 'pants'", AlphaMask("Wet_Drip2","Rogue_Drip_MaskPn"),
                    "RogueX.Panties", AlphaMask("Wet_Drip","Rogue_Drip_Mask"), #"Wet_Drip2",# 
                    "True", AlphaMask("Wet_Drip2","Rogue_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (0,0), ConditionSwitch(                                                                         
            #Personal Wetness            
            "not RogueX.Wet", Null(),
            "RogueX.Legs and RogueX.Wet <= 1", Null(),
            "RogueX.Legs", "images/RogueSprite/Rogue_wet.png",
            "RogueX.Wet == 1", "images/RogueSprite/Rogue_wet.png",
            "True", "images/RogueSprite/Rogue_wet2.png",       #RogueX.Wet >1
            ),  
        (240,560), ConditionSwitch(                                                                         
            #Spunk nethers        
            "'in' not in RogueX.Spunk and 'anal' not in RogueX.Spunk", Null(),
            "RogueX.Legs == 'pants' and not RogueX.Upskirt", Null(),   
            "True", ConditionSwitch( #Wet = 2+
                    "RogueX.Panties and RogueX.PantiesDown", AlphaMask("Spunk_Drip2","Rogue_Drip_MaskP"), #"Wet_Drip2",# 
                    "RogueX.Panties and RogueX.Legs == 'pants'", AlphaMask("Spunk_Drip","Rogue_Drip_MaskPn"), #"Wet_Drip2",# 
                    "RogueX.Legs == 'pants'", AlphaMask("Spunk_Drip2","Rogue_Drip_MaskPn"),
                    "True", AlphaMask("Spunk_Drip2","Rogue_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),   
#        (0,0), ConditionSwitch(                                                                         
#            #Spunk Nethers over          
#            "'in' not in RogueX.Spunk and 'anal' not in RogueX.Spunk", Null(),
#            "RogueX.Legs == 'pants' and not RogueX.Upskirt", Null(),   
#            "RogueX.Panties and not RogueX.PantiesDown", Null(),     
#            "True", "images/RogueSprite/Rogue_wet2.png",       #RogueX.Wet >1
#            ),           
        (0,0), ConditionSwitch(                                                                         
            #brows
            "RogueX.Brows == 'normal' and RogueX.Blush == 2", "images/RogueSprite/Rogue_brows_normal_b.png",
            "RogueX.Brows == 'angry' and RogueX.Blush == 2", "images/RogueSprite/Rogue_brows_angry_b.png",
            "RogueX.Brows == 'sad' and RogueX.Blush == 2", "images/RogueSprite/Rogue_brows_sad_b.png",
            "RogueX.Brows == 'surprised' and RogueX.Blush == 2", "images/RogueSprite/Rogue_brows_surprised_b.png",        
            "RogueX.Brows == 'confused' and RogueX.Blush == 2", "images/RogueSprite/Rogue_brows_confused_b.png",
            "RogueX.Brows == 'normal'", "images/RogueSprite/Rogue_brows_normal.png",
            "RogueX.Brows == 'angry'", "images/RogueSprite/Rogue_brows_angry.png",
            "RogueX.Brows == 'sad'", "images/RogueSprite/Rogue_brows_sad.png",
            "RogueX.Brows == 'surprised'", "images/RogueSprite/Rogue_brows_surprised.png",        
            "RogueX.Brows == 'confused'", "images/RogueSprite/Rogue_brows_confused.png",
            "True", "images/RogueSprite/Rogue_brows_normal.png",
            ),
#        (0,0), ConditionSwitch(                                                                         
#            #Blush
#            "RogueX.Blush", "images/RogueSprite/Rogue_blush.png",
#            "True", Null(), 
#            ),
        (0,0), ConditionSwitch(                                                                         
            #Mouths        
            "'mouth' in RogueX.Spunk and RogueX.Mouth == 'sucking'", "images/RogueSprite/Rogue_mouth_sucking_w.png",
            "'mouth' in RogueX.Spunk and RogueX.Mouth == 'surprised'", "images/RogueSprite/Rogue_mouth_sucking_w.png",
            "'mouth' in RogueX.Spunk and RogueX.Mouth == 'sad'", "images/RogueSprite/Rogue_mouth_sad_w.png",
            "'mouth' in RogueX.Spunk and RogueX.Mouth == 'kiss'", "images/RogueSprite/Rogue_mouth_sad_w.png",
            "'mouth' in RogueX.Spunk and RogueX.Mouth == 'smile'", "images/RogueSprite/Rogue_mouth_smile_w.png",
            "'mouth' in RogueX.Spunk and RogueX.Mouth == 'tongue'", "images/RogueSprite/Rogue_mouth_tongue_w.png",
            "'mouth' in RogueX.Spunk", "images/RogueSprite/Rogue_mouth_lipbite_w.png",
            "RogueX.Mouth == 'normal'", "images/RogueSprite/Rogue_mouth_normal.png",
            "RogueX.Mouth == 'lipbite'", "images/RogueSprite/Rogue_mouth_lipbite.png",
            "RogueX.Mouth == 'sucking'", "images/RogueSprite/Rogue_mouth_sucking.png",            
            "RogueX.Mouth == 'kiss'", "images/RogueSprite/Rogue_mouth_kiss.png",
            "RogueX.Mouth == 'sad'", "images/RogueSprite/Rogue_mouth_sad.png",
            "RogueX.Mouth == 'smile'", "images/RogueSprite/Rogue_mouth_smile.png",
            "RogueX.Mouth == 'surprised'", "images/RogueSprite/Rogue_mouth_surprised.png",            
            "RogueX.Mouth == 'tongue'", "images/RogueSprite/Rogue_mouth_tongue.png",                
            "RogueX.Mouth == 'grimace'", "images/RogueSprite/Rogue_mouth_grimace.png",           
            "True", "images/RogueSprite/Rogue_mouth_normal.png",
            ),            
        (0,0), "Rogue Blink",                                                                           
            #Eyes
            
        (0,0), ConditionSwitch(                                                                         
            #Pants and Skirts
            "RogueX.Legs == 'pants' and RogueX.Upskirt", "images/RogueSprite/Rogue_legs_pants_down.png", 
            "RogueX.Legs == 'pants'", "images/RogueSprite/Rogue_legs_pants.png",          
            "RogueX.Legs == 'skirt' and RogueX.Upskirt", "images/RogueSprite/Rogue_legs_skirt_up.png",
            "RogueX.Legs == 'skirt'", "images/RogueSprite/Rogue_legs_skirt.png",          
            "True", Null(),   
            ),
        (0,0), ConditionSwitch(                                                                        
            #Arms and gloves
            "RogueX.ArmPose == 1 and RogueX.Arms == 'gloves' and RogueX.Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms1a_gloved.png",       #Gloves and collar 
            "RogueX.ArmPose == 1 and RogueX.Arms == 'gloves'", "images/RogueSprite/Rogue_arms1b_gloved.png",                                     #Gloves, no collar
            "RogueX.ArmPose == 1 and RogueX.Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms1a_bare.png",                                #No Gloves, collar 
            "RogueX.ArmPose == 1", "images/RogueSprite/Rogue_arms1b_bare.png",                                                              #No gloves, no collar
            "RogueX.Arms == 'gloves' and RogueX.Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms2a_gloved.png",                           #Gloves and collar 
            "RogueX.Arms == 'gloves'", "images/RogueSprite/Rogue_arms2b_gloved.png",                                                         #Gloved, no collar
            "RogueX.Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms2a_bare.png",                                                    #No gloves, collar
            "True", "images/RogueSprite/Rogue_arms2b_bare.png",    
            ), 
        (0,0), ConditionSwitch(                                                                         
            #chest layer
            "RogueX.Pierce == 'barbell'", "images/RogueSprite/Rogue_chest_barbell.png",            
            "RogueX.Pierce == 'ring'", "images/RogueSprite/Rogue_chest_rings.png",      
            "True", "images/RogueSprite/Rogue_chest_bare.png",    
            ),   
#        (0,0), ConditionSwitch(                                                                         
#            #chest clothes layer
#            "RogueX.Chest == 'tank'", "images/RogueSprite/Rogue_chest_tank.png",
#            "RogueX.Chest == 'buttoned tank'", "images/RogueSprite/Rogue_chest_tank2.png",            
#            "RogueX.Chest == 'bra'", "images/RogueSprite/Rogue_chest_bra.png",                         
#            "RogueX.Chest == 'sports bra'", "images/RogueSprite/Rogue_chest_sportsbra.png",
#            "RogueX.Chest == 'lace bra'", "images/RogueSprite/Rogue_chest_lacebra.png",  
#            "True", Null(),               
#            ),   
        (0,0), ConditionSwitch(                                                                         
            #bra layer           
            "not RogueX.Chest", Null(),             
            "RogueX.Uptop", ConditionSwitch( 
                    #if the top's down. . .
                    "RogueX.Chest == 'tank'", "images/RogueSprite/Rogue_chest_tank_Up.png",
                    "RogueX.Chest == 'buttoned tank'", "images/RogueSprite/Rogue_chest_tank2_Up.png",            
                    "RogueX.Chest == 'bra'", "images/RogueSprite/Rogue_chest_bra_Up.png",                         
                    "RogueX.Chest == 'sports bra'", "images/RogueSprite/Rogue_chest_sportsbra_Up.png",
                    "RogueX.Chest == 'lace bra'", "images/RogueSprite/Rogue_chest_lacebra_Up.png",            
                    "RogueX.Chest == 'bikini top'", "images/RogueSprite/Rogue_chest_bikini_Up.png",     
                    ),            
            "True", ConditionSwitch(
                    #if the top's up. . .
                    "RogueX.Chest == 'tank'", "images/RogueSprite/Rogue_chest_tank.png",
                    "RogueX.Chest == 'buttoned tank'", "images/RogueSprite/Rogue_chest_tank2.png",            
                    "RogueX.Chest == 'bra'", "images/RogueSprite/Rogue_chest_bra.png",                         
                    "RogueX.Chest == 'sports bra'", "images/RogueSprite/Rogue_chest_sportsbra.png",
                    "RogueX.Chest == 'lace bra'", "images/RogueSprite/Rogue_chest_lacebra.png",        
                    "RogueX.Chest == 'bikini top'", "images/RogueSprite/Rogue_chest_bikini.png",          
                    "True", Null(),    
                    ),       
            ),
        (0,0), ConditionSwitch(                                                                         
            #water
            "RogueX.Water and RogueX.ArmPose == 1", "images/RogueSprite/Rogue_body_wet1.png",
            "RogueX.Water", "images/RogueSprite/Rogue_body_wet2.png",
            "True", Null(),                 
            ),
        (0,0), ConditionSwitch(                                                                         
            #soap
            "RogueX.Water == 3", "images/RogueSprite/Rogue_body_wet3.png",
            "True", Null(),                 
            ),
#        (0,0), ConditionSwitch(                                                                         
#            #Overshirt layer
#            "RogueX.ArmPose == 1 and RogueX.Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh1.png",           
#            "RogueX.ArmPose == 1 and RogueX.Over == 'pink top'", "images/RogueSprite/Rogue_over_pink1.png",
#            "RogueX.ArmPose == 1 and RogueX.Over == 'towel'", "images/RogueSprite/Rogue_over_towel1.png",
#            "RogueX.ArmPose == 1 and RogueX.Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty1.png",
#            "RogueX.ArmPose == 1 and RogueX.Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie1.png",
#            "RogueX.Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh2.png", 
#            "RogueX.Over == 'pink top'", "images/RogueSprite/Rogue_over_pink2.png",
#            "RogueX.Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie2.png",
#            "RogueX.Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty2.png",
#            "RogueX.Over == 'towel'", "images/RogueSprite/Rogue_over_towel2.png",              
#            "True", Null(), 
#            ),  
            
        (0,0), ConditionSwitch(                                                                         
            #shirt layer           
            "not RogueX.Over", Null(),             
            "RogueX.Uptop", ConditionSwitch( 
                    #if the top's down. . .
                    "RogueX.ArmPose == 1", ConditionSwitch( 
                            #if the arms are down. . .
                            "RogueX.Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh1_Up.png",           
                            "RogueX.Over == 'pink top'", "images/RogueSprite/Rogue_over_pink1_Up.png",
                            "RogueX.Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie1_Up.png",
                            "RogueX.Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty_Up.png",
#                            "RogueX.Over == 'towel'", Null(), 
                            "True", Null(),     
                            ),  
                    "True", ConditionSwitch( 
                            #if the arms are up. . .
                            "RogueX.Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh2_Up.png", 
                            "RogueX.Over == 'pink top'", "images/RogueSprite/Rogue_over_pink2_Up.png",
                            "RogueX.Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie2_Up.png",
                            "RogueX.Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty_Up.png",
#                            "RogueX.Over == 'towel'", Null(),       
                            "True", Null(),     
                            ),       
                    ),            
            "True", ConditionSwitch(
                    #if the top's up. . .
                    "RogueX.ArmPose == 1", ConditionSwitch( 
                            #if the arms are down. . .
                            "RogueX.Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh1.png",           
                            "RogueX.Over == 'pink top'", "images/RogueSprite/Rogue_over_pink1.png",
                            "RogueX.Over == 'towel'", "images/RogueSprite/Rogue_over_towel1.png",
                            "RogueX.Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty1.png",
                            "RogueX.Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie1.png",
                            "True", Null(),     
                            ),  
                    "True", ConditionSwitch( 
                            #if the arms are up. . .
                            "RogueX.Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh2.png", 
                            "RogueX.Over == 'pink top'", "images/RogueSprite/Rogue_over_pink2.png",
                            "RogueX.Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie2.png",
                            "RogueX.Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty2.png",
                            "RogueX.Over == 'towel'", "images/RogueSprite/Rogue_over_towel2.png",      
                            "True", Null(),     
                            ),       
                    ),       
            ),
        (0,0), ConditionSwitch(                                                                         
            #Hair
            "renpy.showing('Rogue_BJ_Animation') or renpy.showing('Rogue_TJ_Animation')", Null(),
            "RogueX.Hair == 'evo' and RogueX.Water", "images/RogueSprite/Rogue_hair_wet.png",
            "RogueX.Hair == 'wet'", "images/RogueSprite/Rogue_hair_wet.png",
            "True", "images/RogueSprite/Rogue_hair_evo.png",
            ),                           
        (0,0), ConditionSwitch(                                                                         
            #hand spunk
            "'hand' in RogueX.Spunk and RogueX.ArmPose == 2", "images/RogueSprite/Rogue_spunkhand.png",                
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                                                                        
            #tits spunk
            "'tits' in RogueX.Spunk", "images/RogueSprite/Rogue_spunktits.png",
            "True", Null(), 
            ),      
        (0,0), ConditionSwitch(                                                                        
            #face spunk
            "'facial' in RogueX.Spunk", "images/RogueSprite/Rogue_facial.png",
            "True", Null(), 
            ),                
        (0,0), ConditionSwitch(                                                                        
            #Props
            "not RogueX.Held or RogueX.ArmPose != 2", Null(), 
            "RogueX.ArmPose == 2 and RogueX.Held == 'phone'", "images/RogueSprite/Rogue_held_phone.png",
            "RogueX.ArmPose == 2 and RogueX.Held == 'dildo'", "images/RogueSprite/Rogue_held_dildo.png",            
            "RogueX.ArmPose == 2 and RogueX.Held == 'vibrator'", "images/RogueSprite/Rogue_held_vibrator.png",
            "RogueX.ArmPose == 2 and RogueX.Held == 'panties'", "images/RogueSprite/Rogue_held_panties.png",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(
            #UI tool for When Rogue is masturbating using Trigger3 actions
            "Trigger == 'lesbian' or not Trigger3 or Ch_Focus != RogueX", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and RogueX.Lust >= 70", "GirlFingerPussy",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy",
            "Trigger3 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeLeftBreast",    #When zero is working the right breast, fondle left
            "Trigger3 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeRightBreast", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts'", "GirlGropeRightBreast",
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger3 == 'vibrator anal'", "VibratorAnal",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy",  
            "True", Null(), 
            ),     
        (0,0), ConditionSwitch(  
            #UI tool for Trigger5(Threesome masutrbation) actions
            "not Trigger5 or Trigger4 != 'masturbation' or Ch_Focus == RogueX", Null(), 
            #this doesn't activate unless Rogue is not primary, and is actively masturbating
            "Trigger5 == 'fondle pussy' and Trigger != 'sex' and RogueX.Lust >= 70", "GirlFingerPussy",
            "Trigger5 == 'fondle pussy'", "GirlGropePussy",
            "Trigger5 == 'fondle breasts'", "GirlGropeRightBreast",
            "Trigger5 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger5 == 'vibrator pussy'", "VibratorPussy",
            "Trigger5 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger5 == 'vibrator anal'", "VibratorAnal",
            "Trigger5 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(                                                                          
            #UI tool for Trigger1(primary) actions
            "not Trigger or Ch_Focus != RogueX", Null(),
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast",
            "Trigger == 'fondle thighs'", "GropeThigh",
            "Trigger == 'fondle breasts'", "GropeRightBreast",
            "Trigger == 'suck breasts'", "LickRightBreast",
            "Trigger == 'vibrator pussy'", "VibratorPussy",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger == 'vibrator anal'", "VibratorAnal",
            "Trigger == 'vibrator anal insert'", "VibratorPussy",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy",
            "Trigger == 'fondle pussy'", "GropePussy",
            "Trigger == 'lick pussy'", "Lickpussy",
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                                                                        
            #UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus != RogueX", Null(),
            "Trigger == 'fondle breasts' and not Trigger3 and not Trigger4 and not Trigger5", "GropeRightBreast",        
            #When doing nothing offhand, use both hands on breasts.
            "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast",            
            #When sucking right breast, fondle left
            "Trigger2 == 'fondle breasts'", "GropeLeftBreast",
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast",       
            #When sucking right breast, vibrator left
            "Trigger2 == Trigger", Null(),                                              
            #When both triggers are the same, do nothing  
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast",
            "Trigger2 == 'suck breasts'", "LickLeftBreast",  
            "Trigger2 == 'vibrator pussy'", "VibratorPussy",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger2 == 'vibrator anal'", "VibratorAnal",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy",
            "Trigger2 == 'fondle pussy'", "GropePussy",
            "Trigger2 == 'lick pussy'", "Lickpussy",
            "Trigger2 == 'fondle thighs'", "GropeThigh",
            "True", Null(), 
            ),     
        (0,0), ConditionSwitch(  
            #UI tool for Trigger4(Threesome) actions (ie Kitty's hand on her)
            "not Trigger4 or Ch_Focus != RogueX", Null(),
            "Trigger4 == 'fondle pussy' and Trigger != 'sex' and RogueX.Lust >= 70", "GirlFingerPussy",
            "Trigger4 == 'fondle pussy'", "GirlGropePussy",            
            "Trigger4 == 'lick pussy'", "Lickpussy",
            "Trigger4 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast", 
            "Trigger4 == 'suck breasts'", "LickRightBreast",          
            "Trigger4 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger4 == 'vibrator pussy'", "VibratorPussy",
            "Trigger4 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger4 == 'vibrator anal'", "VibratorAnal",
            "Trigger4 == 'vibrator anal insert'", "VibratorPussy",
            "Trigger4 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast",    #When zero is working the right breast, fondle left
            "Trigger4 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast", #When zero is working the left breast, fondle right  
            "Trigger4 == 'fondle breasts'", "GirlGropeRightBreast",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(  
            #UI tool for Trigger3(lesbian) actions (ie Kitty's hand on her when Rogue is secondary)
            "Trigger != 'lesbian' or not Trigger3 or Ch_Focus == RogueX", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and RogueX.Lust >= 70", "GirlFingerPussy",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy",            
            "Trigger3 == 'lick pussy'", "Lickpussy",
            "Trigger3 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast", 
            "Trigger3 == 'suck breasts'", "LickRightBreast",          
            "Trigger3 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast",    #When zero is working the right breast, fondle left
            "Trigger3 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts'", "GirlGropeRightBreast",
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
    
image Rogue Blink:
    ConditionSwitch(
    "RogueX.Eyes == 'sexy'", "images/RogueSprite/Rogue_eyes_sexy.png",
    "RogueX.Eyes == 'side'", "images/RogueSprite/Rogue_eyes_side.png",
    "RogueX.Eyes == 'surprised'", "images/RogueSprite/Rogue_eyes_surprised.png",
    "RogueX.Eyes == 'normal'", "images/RogueSprite/Rogue_eyes_normal.png",    
    "RogueX.Eyes == 'stunned'", "images/RogueSprite/Rogue_eyes_stunned.png",
    "RogueX.Eyes == 'down'", "images/RogueSprite/Rogue_eyes_down.png",
    "RogueX.Eyes == 'closed'", "images/RogueSprite/Rogue_eyes_closed.png",
    "RogueX.Eyes == 'manic'", "images/RogueSprite/Rogue_eyes_manic.png",
    "RogueX.Eyes == 'squint'", "Rogue_Squint",
    "True", "images/RogueSprite/Rogue_eyes_normal.png", 
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/RogueSprite/Rogue_eyes_closed.png"
    .25
    repeat                

image Rogue_Squint:
    "images/RogueSprite/Rogue_eyes_sexy.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/RogueSprite/Rogue_eyes_squint.png"
    .25
    repeat  
    

image Rogue_Drip_Mask:
    #This is the mask for her drip pattern
    contains:
        "images/RogueSprite/Rogue_WetMask.png"      
        offset (-240,-560)

image Rogue_Drip_MaskP:
    #This is the mask for her drip pattern in panties down mode
    contains:
        "images/RogueSprite/Rogue_WetMaskP.png"      
        offset (-240,-560)
            
image Rogue_Drip_MaskPn:
    #This is the mask for her drip pattern in pants down mode
    contains:
        "images/RogueSprite/Rogue_WetMaskPn.png"      
        offset (-240,-560)
    
#Xavier Sprite Compositing
image Professor:
    LiveComposite(
        (429,521),
        (0,0), "images/NPC/Xavier_body.png",
        (0,0), ConditionSwitch(
            "X_Brows == 'concentrate'", "images/NPC/Xavier_brows_concentrate.png",
            "X_Brows == 'happy'", "images/NPC/Xavier_brows_happy.png",
            "X_Brows == 'shocked'", "images/NPC/Xavier_brows_shocked.png",
            "X_Brows == 'neutral'", "images/NPC/Xavier_brows_neutral.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "X_Mouth == 'concentrate'", "images/NPC/Xavier_mouth_stern.png",            
            "X_Mouth == 'happy'", "images/NPC/Xavier_mouth_smile.png",
            "X_Mouth == 'neutral'", "images/NPC/Xavier_mouth_neutral.png",
            "True", Null(),
            ),
        (0,0), "Xavier Blink",
        (0,0), ConditionSwitch(
            "X_Psychic == 1", "images/NPC/Xavier_psychic.png",        
            "True", Null(),
            ),
        )           
    anchor (0.5, 0.0)
    offset (0,150)#200)
    zoom 1.1
        
image Xavier Blink:
    ConditionSwitch(
    "X_Eyes == 'concentrate'", "images/NPC/Xavier_eyes_closed.png",  
    "X_Eyes == 'hypno'", "images/NPC/Xavier_eyes_hypno.png",        
    "X_Eyes == 'shocked'", "images/NPC/Xavier_eyes_shocked.png",
    "True", "images/NPC/Xavier_eyes_happy.png",  
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    # This randomizes the time between blinking.
    "images/NPC/Xavier_eyes_closed.png"
    .25
    repeat        


#Night composite
image setting = LiveComposite(
    (1024,768),
    (0, 0), ConditionSwitch(        
        "Current_Time == 'Evening'", "images/sky_sunset.jpg",
        "Current_Time == 'Night'", "images/sky_night.jpg",        
        "True", "images/sky_day.jpg",        
        ),
    (0, 0), ConditionSwitch(           
        "bg_current == 'bg study'", "images/study.jpg",
        "bg_current == 'bg player'", "images/playerroom.png",            
        "bg_current == 'bg dangerroom'", "images/dangerroom.jpg",        
        "bg_current == 'bg showerroom'", "images/Shower.jpg",
        "bg_current == 'bg rogue'", "images/Rogueroom.png",
        "bg_current == 'bg movies'", "images/Movies.jpg",               
        "bg_current == 'bg restaurant'", "images/Restaurant.jpg",
        "bg_current == 'bg kitty'", "images/kittyroom.png",     
        "bg_current == 'bg emma'", "images/emmaroom.png",            
#        "bg_current == 'bg classroom'", "images/ClassroomLit.jpg",        
        # if bg_current == 'bg campus' or anything else        
        "Current_Time == 'Evening'",    "images/Crossroads_Evening.jpg",
        "Current_Time == 'Night'",      "images/Crossroads_Night.jpg",    
        "True",                         "images/Crossroads_Day.jpg",  
        ),     
    )
        
label Display_Background(Entry = 0): 
        # call Display_Background(1)              
        #Displays the current background
        if Entry:     
                                scene bg_entry onlayer backdrop   
        elif bg_current == "bg player":        
                                scene bg_player onlayer backdrop         
        elif bg_current == "bg rogue":        
                                scene bg_rogue onlayer backdrop   
        elif bg_current == "bg kitty":        
                                scene bg_kitty onlayer backdrop      
        elif bg_current == "bg emma":        
                                scene bg_emma onlayer backdrop    
        elif bg_current == "bg laura":        
                                scene bg_laura onlayer backdrop   
        elif bg_current == "bg classroom":        
                                scene bg_class onlayer backdrop 
        elif bg_current == "bg dangerroom":        
                                scene bg_danger onlayer backdrop           
        elif bg_current == "bg showerroom":        
                                scene bg_shower onlayer backdrop  
        elif bg_current == "bg study":        
                                scene bg_study onlayer backdrop    
        elif bg_current == "bg movies":        
                                scene bg_movies onlayer backdrop          
        elif bg_current == "bg restaurant":        
                                scene bg_rest onlayer backdrop   
        elif bg_current == "bg pool":        
                                scene bg_pool onlayer backdrop 
        else: # if 'bg campus' or anything else        
                                scene bg_campus onlayer backdrop   
        return

image bg_entry = "images/Door.jpg"        
image bg_player:
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Current_Time == 'Evening'", "images/sky_sunset.jpg",
                "Current_Time == 'Night'", "images/sky_night.jpg",        
                "True", "images/sky_day.jpg",
                )   
        contains: 
                "images/playerroom.png"
image bg_rogue:
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Current_Time == 'Evening'", "images/sky_sunset.jpg",
                "Current_Time == 'Night'", "images/sky_night.jpg",        
                "True", "images/sky_day.jpg",
                )   
        contains:
                "images/Rogueroom.png"        
image bg_kitty:
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Current_Time == 'Evening'", "images/sky_sunset.jpg",
                "Current_Time == 'Night'", "images/sky_night.jpg",        
                "True", "images/sky_day.jpg",
                )   
        contains: 
                "images/kittyroom.png"
        
image bg_emma:
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Current_Time == 'Evening'", "images/sky_sunset.jpg",
                "Current_Time == 'Night'", "images/sky_night.jpg",        
                "True", "images/sky_day.jpg",
                )   
        contains: 
                "images/emmaroom.png"
        
image bg_laura:
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Current_Time == 'Evening'", "images/sky_sunset.jpg",
                "Current_Time == 'Night'", "images/sky_night.jpg",        
                "True", "images/sky_day.jpg",
                )   
        contains: 
                "images/lauraroom.png"
        
image bg_campus:
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Current_Time == 'Evening'",    "images/Campus_Evening.png",
                "Current_Time == 'Night'",      "images/Campus_Night.png",    
                "True",                         "images/Campus_Day.png",
                )       

image bg_pool:
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Current_Time == 'Evening'",    "images/pool_evening.png",
                "Current_Time == 'Night'",      "images/pool_night.png",    
                "True",                         "images/pool_day.png",
                )   
        
image bg_class:
        contains:
            "images/Classroom.jpg"
        contains:
            ConditionSwitch(        
                "EmmaX.Loc == 'bg teacher'", "Emma_At_Podium",
                "EmmaX.Loc == 'bg desk'", "Emma_At_Desk",
                "True", Null(),
                )
        contains:
            #The overlay Podium
            "images/ClassroomFront.png"
        contains:
            ConditionSwitch(        
                "bg_current != 'bg classroom' or Current_Time == 'Evening' or Current_Time == 'Night' or Weekday >= 5", Null(),
                "True", "images/ClassroomPupils.png",
                )

image bg_study:
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Current_Time == 'Night'",      "images/StudyNight.jpg",    
                "True",                         "images/StudyDay.jpg",
                )       
        
#image bg_classlit = "images/ClassroomLit.jpg"
#image bg_classnight = "images/ClassroomNight.jpg"
image bg_danger = "images/dangerroom.jpg"      
image bg_shower = "images/Shower.jpg"
#image bg_study = "images/study.jpg"
image bg_movies = "images/Movies.jpg"     
image bg_rest = "images/Restaurant.jpg"



# Rogue Doggy Compositing ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#image Rogue_Doggy_Base = LiveComposite(
image Rogue_Doggy_Animation: #nee Rogue_Doggy
    LiveComposite(                                                                                 
        #Base body
        (420,750),  
        (0,0), ConditionSwitch(                                                         
            #Shows different upper body motion depending on events  
            "not Player.Sprite", "Rogue_Doggy_Body",
            "Player.Cock == 'anal'", ConditionSwitch( 
                    "Speed > 2", "Rogue_Doggy_Fuck2_Top",
                    "Speed > 1", "Rogue_Doggy_Fuck_Top",
                    "Speed", "Rogue_Doggy_Anal_Head_Top", 
                    "True", "Rogue_Doggy_Body",   
                    ),
            "Player.Cock == 'in'", ConditionSwitch(   
                    "Speed > 2", "Rogue_Doggy_Fuck2_Top",
                    "Speed > 1", "Rogue_Doggy_Fuck_Top",
                    "True", "Rogue_Doggy_Body",                    
                    ),
            "True", "Rogue_Doggy_Body",           
            ),  
        (0,0), ConditionSwitch(                                                         
            #Shows different lower body motion depending on events
            "not Player.Sprite", "Rogue_Doggy_Ass",
            "Player.Cock == 'anal'", ConditionSwitch( 
                    "Speed > 2", "Rogue_Doggy_Fuck2_Ass",
                    "Speed > 1", "Rogue_Doggy_Fuck_Ass",
                    "Speed", "Rogue_Doggy_Anal_Head_Ass", 
                    "True", "Rogue_Doggy_Ass",   
                    ),
            "Player.Cock == 'in'", ConditionSwitch(   
                    "Speed > 2", "Rogue_Doggy_Fuck2_Ass",
                    "Speed > 1", "Rogue_Doggy_Fuck_Ass",
                    "True", "Rogue_Doggy_Ass",                    
                    ),
            "True", "Rogue_Doggy_Ass",           
            ),  
        (0,0), ConditionSwitch(                                                         
            #Shows different lower body motion depending on events
            "Player.Cock == 'foot'", ConditionSwitch( 
                    "Speed > 1", "Rogue_Doggy_Feet2",
                    "Speed", "Rogue_Doggy_Feet1",
                    "True", "Rogue_Doggy_Feet0",   
                    ),
            "True", Null(),           
            ),  
        )
    align (0.6,0.0)
    
            
image Rogue_Doggy_Body = LiveComposite(                                                                                         #Upper body
        (420,750),
        (0,0), ConditionSwitch(
            #Hair underlayer
            "RogueX.Water", Null(), 
            "RogueX.Hair == 'evo'", "images/RogueDoggy/Rogue_Doggy_HairB.png",   
            "True", Null(), 
            ),   
        (0,0), "images/RogueDoggy/Rogue_Doggy_Body.png", #Body base
        (0,0), ConditionSwitch(             
            #Mouth
            "'mouth' in RogueX.Spunk", ConditionSwitch( 
                    "RogueX.Mouth == 'lipbite'", "images/RogueDoggy/Rogue_Doggy_Mouth_LipbiteW.png",
                    "RogueX.Mouth == 'surprised'", "images/RogueDoggy/Rogue_Doggy_Mouth_SurprisedW.png",
                    "RogueX.Mouth == 'sucking'", "images/RogueDoggy/Rogue_Doggy_Mouth_BlowW.png",
                    "RogueX.Mouth == 'sad'", "images/RogueDoggy/Rogue_Doggy_Mouth_SadW.png",
                    "RogueX.Mouth == 'smile'", "images/RogueDoggy/Rogue_Doggy_Mouth_SmileW.png",   
                    "RogueX.Mouth == 'tongue'", "images/RogueDoggy/Rogue_Doggy_Mouth_TongueW.png",  
                    "True", "images/RogueDoggy/Rogue_Doggy_Mouth_NormalW.png",   
                    ),
            "RogueX.Mouth == 'normal'", "images/RogueDoggy/Rogue_Doggy_Mouth_Normal.png",
            "RogueX.Mouth == 'lipbite'", "images/RogueDoggy/Rogue_Doggy_Mouth_Lipbite.png",
            "RogueX.Mouth == 'sucking'", "images/RogueDoggy/Rogue_Doggy_Mouth_Blow.png",            
            "RogueX.Mouth == 'kiss'", "images/RogueDoggy/Rogue_Doggy_Mouth_Surprised.png",
            "RogueX.Mouth == 'sad'", "images/RogueDoggy/Rogue_Doggy_Mouth_Sad.png",
            "RogueX.Mouth == 'smile'", "images/RogueDoggy/Rogue_Doggy_Mouth_Smile.png",
            "RogueX.Mouth == 'grimace'", "images/RogueDoggy/Rogue_Doggy_Mouth_Smile.png",
            "RogueX.Mouth == 'surprised'", "images/RogueDoggy/Rogue_Doggy_Mouth_Surprised.png",       
            "RogueX.Mouth == 'tongue'", "images/RogueDoggy/Rogue_Doggy_Mouth_Tongue.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Mouth_Smile.png", 
            ),
        (0,0), ConditionSwitch( 
            #Blush
            "RogueX.Blush", "images/RogueDoggy/Rogue_Doggy_BlushEvo.png",
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(
            #Brows
            "RogueX.Brows == 'normal'", "images/RogueDoggy/Rogue_Doggy_Brows_Normal.png",
            "RogueX.Brows == 'angry'", "images/RogueDoggy/Rogue_Doggy_Brows_Angry.png",
            "RogueX.Brows == 'sad'", "images/RogueDoggy/Rogue_Doggy_Brows_Sad.png",
            "RogueX.Brows == 'surprised'", "images/RogueDoggy/Rogue_Doggy_Brows_Surprised.png",        
            "RogueX.Brows == 'confused'", "images/RogueDoggy/Rogue_Doggy_Brows_Normal.png",
            "True", "images/RogueDoggy/Rogue_Doggy_Brows_Normal.png",
            ),     
        (0,0), "Rogue Doggy Blink",#Eyes
        (0,0), ConditionSwitch( 
            #Collar
            "RogueX.Neck == 'spiked collar'", "images/RogueDoggy/Rogue_Doggy_Collar.png",   
            "True", Null(),                #RogueX.Arms == 'gloves' or not RogueX.Arms
            ),  
        (0,0), ConditionSwitch(   
            #tanktop
            "not RogueX.Chest", Null(),        
            "RogueX.Chest == 'tank'", "images/RogueDoggy/Rogue_Doggy_Chest_Tank.png",
            "RogueX.Chest == 'buttoned tank'", "images/RogueDoggy/Rogue_Doggy_Chest_ButtonTank.png",
            "RogueX.Chest == 'sports bra'", "images/RogueDoggy/Rogue_Doggy_Chest_SportsBra.png",
            "RogueX.Chest == 'bikini top'", "images/RogueDoggy/Rogue_Doggy_Chest_Bikini.png",  
            "RogueX.Chest", "images/RogueDoggy/Rogue_Doggy_Chest_Bra.png",
            "True", Null(),   
            ), 
        (0,0), ConditionSwitch(                                                                   
            #Wet look
            "RogueX.Water", "images/RogueDoggy/Rogue_Doggy_WetTop.png",   
            "True", Null(),              
            ),  
        (0,0), ConditionSwitch(                     
            #Overshirt
            "not RogueX.Over", Null(),
            "RogueX.Over == 'mesh top'", "images/RogueDoggy/Rogue_Doggy_Over_Mesh.png",           
            "RogueX.Over == 'pink top'", "images/RogueDoggy/Rogue_Doggy_Over_Pink.png",            
            "RogueX.Over == 'hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_Hoodie.png",           
            "RogueX.Over == 'nighty'", "images/RogueDoggy/Rogue_Doggy_Over_NightyTop.png",         
            "RogueX.Over == 'towel'", "images/RogueDoggy/Rogue_Doggy_Over_TowelTop.png",
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(                                   
            #Hair
            "RogueX.Water", "images/RogueDoggy/Rogue_Doggy_HairWet.png",   
            "RogueX.Hair == 'evo'", "images/RogueDoggy/Rogue_Doggy_HairF.png",   
            "True", "images/RogueDoggy/Rogue_Doggy_HairF.png",                     
            ),  
        (0,0), ConditionSwitch(                                       
            #face spunk
            "not RogueX.Spunk", Null(),
            "'facial' in RogueX.Spunk", "images/RogueDoggy/Rogue_Doggy_Facial.png",
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                                                                             
            #Hair            
            "RogueX.Over == 'hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_Hood.png", 
            "True", Null(),    
            ),  
        )

image Rogue_Doggy_Ass = LiveComposite(                                                                                          #Lower body
        (420,750), #(210,375), #(419,750), 
        (0,0), ConditionSwitch(                                                                               
            #Panties back
            "not RogueX.PantiesDown or (RogueX.Legs == 'pants' and not RogueX.Upskirt)", Null(),  
            "RogueX.Panties == 'shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts_Back.png",    
            "RogueX.Panties == 'green panties'", "images/RogueDoggy/Rogue_Doggy_Undies_Back.png",  
            "RogueX.Panties == 'bikini bottoms'", "images/RogueDoggy/Rogue_Doggy_Panties_Bikini_Back.png",   
            "RogueX.Panties", "images/RogueDoggy/Rogue_Doggy_Panties_Back.png",  
            "True", Null(),  
            ),  
        (0,0), "images/RogueDoggy/Rogue_Doggy_Ass.png", #Ass Base
        (0,0), ConditionSwitch(
            #Wet look
            "RogueX.Water", "images/RogueDoggy/Rogue_Doggy_WetAss.png",   
            "True", Null(),              
            ),  
        (0,0), ConditionSwitch(        
            #Hose
            "RogueX.Hose == 'stockings'", "images/RogueDoggy/Rogue_Doggy_Hose.png",
            "True", Null(),
            ),             
        (0,0), ConditionSwitch(          
            #Panties if Down
            "not RogueX.PantiesDown or (RogueX.Legs == 'pants' and not RogueX.Upskirt)", Null(),
            "RogueX.Panties == 'shorts' and RogueX.Wet > 1", "images/RogueDoggy/Rogue_Doggy_Shorts_Down_Wet.png", #fix turn this on when graphics fixed
            "RogueX.Panties == 'shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts_Down.png", 
            "RogueX.Panties == 'green panties' and RogueX.Wet > 1", "images/RogueDoggy/Rogue_Doggy_Undies_Down_Wet.png",
            "RogueX.Panties == 'green panties'", "images/RogueDoggy/Rogue_Doggy_Undies_Down.png",  
            "RogueX.Panties == 'bikini bottoms'", "images/RogueDoggy/Rogue_Doggy_Panties_Bikini_Down.png",  
            "RogueX.Panties", "images/RogueDoggy/Rogue_Doggy_Panties_Down.png",  
            "True", Null(),      
            ),  
            
            
        (0,0), ConditionSwitch(    
            #Pussy Composite      
            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(                     
                    "Speed > 2", "Rogue_Pussy_Fucking3",#Speed 3
                    "Speed > 1", "Rogue_Pussy_Fucking2",#Speed 2
                    "Speed", "Rogue_Pussy_Heading",      #Speed 1
                    "True", "Rogue_Pussy_Static",              #Speed 0
                    ),   
            "Trigger == 'lick pussy'", "images/RogueDoggy/Rogue_Doggy_Pussy_Open.png",   
            "True", "images/RogueDoggy/Rogue_Doggy_Pussy_Closed.png", 
            ),   
            
            
#        (0,0), ConditionSwitch(                                                                                 #spunkpussy Layer
#            "RogueX.Spunk == 'in' and Player.Cock == 'in'", "images/RogueDoggy/Rogue_Doggy_SpunkPussyOpen.png",  #fix for RogueX.Spunk is used later
#            "RogueX.Spunk == 'in'", "images/RogueDoggy/Rogue_Doggy_SpunkPussyClosed.png", 
#            "RogueX.Wet and Player.Cock == 'in'", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png", 
#            "RogueX.Wet", "images/RogueDoggy/Rogue_Doggy_WetPussyClosed.png", 
#            "True", Null(),                    
#            ),   
        (0,0), ConditionSwitch(  
            #pubes              
            "not RogueX.Pubes", Null(),         
            "Player.Sprite and Player.Cock == 'in'", Null(),
            "RogueX.Legs == 'pants' and not RogueX.Upskirt", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",   
            "RogueX.PantiesDown", "images/RogueDoggy/Rogue_Doggy_Pubes.png",  
            "RogueX.Panties", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",
            "RogueX.Hose and RogueX.Hose != 'stockings'", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",   
            "True", "images/RogueDoggy/Rogue_Doggy_Pubes.png",  
            ),  
        (0,0), ConditionSwitch(   
            #Pussy Piercings          
            "Player.Sprite", Null(),             
            "RogueX.Pierce == 'ring'", "images/RogueDoggy/Rogue_Doggy_PussyRing.png",            
            "RogueX.Pierce == 'barbell'", "images/RogueDoggy/Rogue_Doggy_PussyBarbell.png",
            "True", Null(),  
            ),   
            
            
        (0,0), ConditionSwitch(    
            #Anus Composite 
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(                     
                    "Speed > 2", "Rogue_Anal_Fucking2", #Speed 3
                    "Speed > 1", "Rogue_Anal_Fucking",  #Speed 2
                    "Speed", "Rogue_Anal_Heading",      #Speed 1
                    "True", "Rogue_Anal",               #Speed 0
                    ),    
#            "Action == 'plug'", "Rogue_Anal_Plug",  
#            "Action == 'plug'", "test_case",
            "RogueX.Loose", "images/RogueDoggy/Rogue_Doggy_Asshole_Loose.png",   
            "True", "images/RogueDoggy/Rogue_Doggy_Asshole_Tight.png", 
            ),    
            
            
        (0,0), ConditionSwitch( 
            #spunkanal Layer
            "'anal' not in RogueX.Spunk or Player.Sprite", Null(),   
            "Player.Cock == 'anal'", "images/RogueDoggy/Rogue_Doggy_SpunkAnalOpen.png",  
            "RogueX.Loose", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png", 
            ),   
        (0,0), ConditionSwitch(   
            #Panties if up
            "RogueX.PantiesDown or not RogueX.Panties", Null(),     
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
            "RogueX.Panties == 'shorts' and RogueX.Wet", "images/RogueDoggy/Rogue_Doggy_Shorts_Wet.png",          
            "RogueX.Panties == 'shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts.png",
            "RogueX.Panties == 'green panties' and RogueX.Wet", "images/RogueDoggy/Rogue_Doggy_Undies_Wet.png",          
            "RogueX.Panties == 'green panties'", "images/RogueDoggy/Rogue_Doggy_Undies.png",          
            "RogueX.Panties == 'lace panties'", "images/RogueDoggy/Rogue_Doggy_PantiesLace.png",       
            "RogueX.Panties == 'bikini bottoms'", "images/RogueDoggy/Rogue_Doggy_Panties_Bikini.png",                             
            "True", "images/RogueDoggy/Rogue_Doggy_Panties.png", 
            ),  
        (0,0), ConditionSwitch( 
            #full hose/tights  
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),  
#            "RogueX.Panties and RogueX.PantiesDown and RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png", 
            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png", 
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",  
            "RogueX.Panties and RogueX.PantiesDown", Null(),    
            "RogueX.Hose == 'tights' and RogueX.Wet", "images/RogueDoggy/Rogue_Doggy_Tights_Wet.png",
            "RogueX.Hose == 'tights'", "images/RogueDoggy/Rogue_Doggy_Tights.png",
            "RogueX.Hose == 'pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose.png",   
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png", 
            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",            
            "True", Null(), 
            ),
        (0,0), ConditionSwitch( 
            #Legs Layer 
            "RogueX.Legs == 'pants'", ConditionSwitch(    
                    "RogueX.Upskirt", "images/RogueDoggy/Rogue_Doggy_Legs_Pants_Down.png",            
                    "RogueX.Wet > 1", "images/RogueDoggy/Rogue_Doggy_Legs_Pants_Wet.png",
                    "True", "images/RogueDoggy/Rogue_Doggy_Legs_Pants.png",
                    ),     
            "RogueX.Legs == 'skirt'", ConditionSwitch(    
                    "RogueX.Upskirt and Player.Sprite and Player.Cock == 'anal' and Speed" , "images/RogueDoggy/Rogue_Doggy_Legs_Skirt_UpAnal.png",   
                    "RogueX.Upskirt", "images/RogueDoggy/Rogue_Doggy_Legs_Skirt_Up.png",   
                    "True", "images/RogueDoggy/Rogue_Doggy_Legs_Skirt.png", 
                    ),          
            "True", Null(),                      
            ),   
        (0,0), ConditionSwitch(              
            #Over Layer
            "RogueX.Over == 'nighty' and RogueX.Upskirt", "images/RogueDoggy/Rogue_Doggy_Over_NightyAss_Up.png",            
            "RogueX.Over == 'nighty'", "images/RogueDoggy/Rogue_Doggy_Over_NightyAss.png",
            "RogueX.Over == 'towel' and RogueX.Upskirt", "images/RogueDoggy/Rogue_Doggy_Over_TowelAss_Up.png",            
            "RogueX.Over == 'towel'", "images/RogueDoggy/Rogue_Doggy_Over_TowelAss.png",
            "True", Null(),                    
            ),   
        (0,0), ConditionSwitch(  
            #spunk back Layer
            "'back' in RogueX.Spunk", "images/RogueDoggy/Rogue_Doggy_SpunkAss.png",  
            "True", Null(),                    
            ),   
        (0,0), ConditionSwitch(  
            #Hotdogging underlayer
            "not Player.Sprite or Player.Cock != 'out'", Null(),   
            "RogueX.Legs == 'skirt' and RogueX.Upskirt", "images/RogueDoggy/Rogue_Doggy_HotdogUpskirtBack.png",  
            "True", "images/RogueDoggy/Rogue_Doggy_HotdogBack.png", 
            ),    
        (0,0), ConditionSwitch( 
            #Hotdogging Cock w/ alpha
            "not Player.Sprite or Player.Cock != 'out'", Null(),            
            "RogueX.Legs == 'skirt' and RogueX.Upskirt and Speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "RogueX.Legs == 'skirt' and RogueX.Upskirt", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "Speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),    
            "True", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            ),
#        (0,0), ConditionSwitch(  
#            #UI tool layer
#            "not UI_Tool", Null(),   
#            "UI_Tool", "Slap_Ass",  
#            "True", Null(),   
#            ),   
        )
        
image Rogue Doggy Blink:                                                                                        #Eyes
    ConditionSwitch(          
    "RogueX.Eyes == 'sexy'", "images/RogueDoggy/Rogue_Doggy_Eyes_Sexy.png",
    "RogueX.Eyes == 'side'", "images/RogueDoggy/Rogue_Doggy_Eyes_Side.png",
    "RogueX.Eyes == 'normal'", "images/RogueDoggy/Rogue_Doggy_Eyes_Normal.png",
    "RogueX.Eyes == 'closed'", "images/RogueDoggy/Rogue_Doggy_Eyes_Closed.png",
    "RogueX.Eyes == 'manic'", "images/RogueDoggy/Rogue_Doggy_Eyes_Surprised.png",
    "RogueX.Eyes == 'down'", "images/RogueDoggy/Rogue_Doggy_Eyes_Sexy.png",           
    "RogueX.Eyes == 'stunned'", "images/RogueDoggy/Rogue_Doggy_Eyes_Stunned.png",
    "RogueX.Eyes == 'surprised'", "images/RogueDoggy/Rogue_Doggy_Eyes_Surprised.png",
    "RogueX.Eyes == 'squint'", "images/RogueDoggy/Rogue_Doggy_Eyes_Sexy.png",
    "True", "images/RogueDoggy/Rogue_Doggy_Eyes_Normal.png",
    ),
#    choice:
#        3.5
#    choice:
#        3.25
#    choice:
#        3
    3
    # This randomizes the time between blinking.
    "images/RogueDoggy/Rogue_Doggy_Eyes_Closed.png"
    .25
    repeat 
 

image Rogue_Doggy_Feet: 
    contains:
            AlphaMask("Rogue_Doggy_Shins", "images/RogueDoggy/Rogue_Doggy_Toes.png")
           
image Rogue_Doggy_Shins:                                             
    #Rogue's footjob shins
    contains:
        "images/RogueDoggy/Rogue_Doggy_Shins.png"
    contains:
        #pants
        ConditionSwitch(     
            "RogueX.Legs == 'pants'", "images/RogueDoggy/Rogue_Doggy_Feet_Pants.png",
            "True", Null(),           
            )
    contains:
        "images/RogueDoggy/Rogue_Doggy_Feet.png"
    contains:
            #hose
        ConditionSwitch(  
            "not RogueX.Hose", Null(),    
            "RogueX.Hose == 'stockings'", "images/RogueDoggy/Rogue_Doggy_Feet_Hose.png",           
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Feet_Hose.png",   
            "RogueX.Hose == 'tights'", "images/RogueDoggy/Rogue_Doggy_Feet_Tights.png",
            "RogueX.Hose == 'pantyhose'", "images/RogueDoggy/Rogue_Doggy_Feet_Hose.png",   
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_Feet_Hose_Holed.png", 
            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Feet_Tights_Holed.png",      
            "True", Null(),                
            )
#    pos (0,0)      

#Hotdogging animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Zero_Doggy_Up:                                                                                  
    #Cock when out (hotdog)
    contains:
        ConditionSwitch(    
            "Player.Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Cock_U_P.png",
            "Player.Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Cock_U_B.png",             
            "True", "images/RogueDoggy/Rogue_Doggy_Cock_U_G.png", 
            ), 
    contains:
        ConditionSwitch(    
            "Player.Wet", "images/RogueDoggy/Rogue_Doggy_Cock_U_W.png",
            "True", Null(), 
            ),

image Zero_Hotdog_Static:
    # The unmoving version of the hotdog cock
    # called in Doggy Ass LC
    contains:        
        "Zero_Doggy_Up"
        pos (175, 370)

image Zero_Hotdog_Moving:
    # The moving version of the hotdog cock
    # called in Doggy Ass LC
    contains:
        "Zero_Doggy_Up"
        pos (175, 370) 
        block:
            ease 1 ypos 330
            ease 1 ypos 420
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                                                                                  
#Insert cock animations
image Zero_Doggy_Insert:                                                                                
    #Insert cock
    contains:
        ConditionSwitch(    
            "Player.Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Cock_In_P.png",
            "Player.Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Cock_In_B.png",             
            "True", "images/RogueDoggy/Rogue_Doggy_Cock_In_G.png", 
            ), 
    contains:
        ConditionSwitch(    
            "Player.Wet", "images/RogueDoggy/Rogue_Doggy_Cock_In_Wet.png",           
            "True", Null(),
            ), 
    contains:
        ConditionSwitch(    
            "Player.Spunk", "images/RogueDoggy/Rogue_Doggy_Cock_In_Spunk.png",           
            "True", Null(),
            ), 

#image Zero_Doggy_Static:
#    # Sex Speed 2 motions
#    contains:
#        "Zero_Doggy_Insert"
#        pos (169,500)
#        block:
#            ease .5 ypos 540
#            pause .25
#            ease 1.75 ypos 545
#            repeat
            
image Zero_Doggy_Static:
    # Sex Speed 0 motions
    contains:
        subpixel True
        "Zero_Doggy_Insert"    
        pos (169,545)
        block:
            ease 1 ypos 540 #in stroke
            pause 1
            ease 3 ypos 545 #out stroke
            repeat
            
image Zero_Doggy_Heading:
    # Sex Speed 1 motions
    contains:
        subpixel True
        "Zero_Doggy_Insert"    
        pos (171,545)
        block:
            ease 1 xpos 168 ypos 500 #in stroke
            pause 1
            ease 3 xpos 171 ypos 545 #out stroke
            repeat

image Zero_Doggy_Fucking2:
    # Sex Speed 2 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat
            
image Zero_Doggy_Fucking3:
    # Sex Speed 3 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .2 ypos 440
            pause .1
            ease .6 ypos 500
            repeat
            
image Rogue_Pussy_Mask:                 
    #AlphaMask used to prevent the cock from moving past the pussy
    #Called in "Rogue_Pussy_Moving"
    contains:                                                                                   
        #Base
        "images/RogueDoggy/Rogue_Doggy_SexMask.png"    
        anchor (0.52,0.69)
        pos (217,518) 
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat 

image Rogue_Pussy_Mask_Static:                 
    #AlphaMask used to prevent the cock from moving past the pussy in static pose
    #Called in "Rogue_Pussy_Moving"
    contains:                                                                                   
        #Base
        "images/RogueDoggy/Rogue_Doggy_SexMask.png"    
        anchor (0.52,0.69)
        pos (217,518) 
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>             
#Pussy fucking animations    
#image Rogue_Pussy:        
#    #Full Animation for speed 0    
#    contains:                                                                                   
#        #Base
#        "images/RogueDoggy/Rogue_Doggy_Pussy_FBase.png"  
#    contains:
#        ConditionSwitch( 
#            #full hose/tights  
#            "RogueX.PantiesDown", Null(), 
#            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",    
#            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",    
##            "RogueX.Hose == 'tights' and RogueX.Wet", "images/RogueDoggy/Rogue_Doggy_Tights_Wet.png",
##            "RogueX.Hose == 'tights'", "images/RogueDoggy/Rogue_Doggy_Tights.png",
##            "RogueX.Hose == 'pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose.png",   
#            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png", 
#            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",            
#            "True", Null(), 
#            ),  
##    contains:                                                                                   
##        #Cock
##        "Zero_Doggy_Insert"
##        pos (169,460) #Out stroke
##    contains:                                                                                   
##        #Masking overlay
##        "images/RogueDoggy/Rogue_Doggy_Pussy_FMask.png"
    
#    contains:                                                                                  
#        #Cock        
#        AlphaMask("Zero_Doggy_Insert", "images/RogueDoggy/Rogue_Doggy_SexMask.png")


image Rogue_Pussy_Static:     
    #Full Animation for speed 0
    subpixel True
    contains:                                                                                   
        #Base
        "images/RogueDoggy/Rogue_Doggy_Pussy_FBase.png"    
        anchor (0.52,0.69)
        pos (220,518) 
        xzoom 1
    contains:                                                                                   
        #moving hole
        "images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png"    
        subpixel True
        anchor (0.52,0.69)
        pos (217,518) 
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat 
    contains:
        ConditionSwitch( 
            #full hose/tights              
            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",    
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",  
            "RogueX.Panties and RogueX.PantiesDown", Null(), 
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png", 
            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",            
            "True", Null(), 
            ),
    contains:                                                                                  
        #Cock
        AlphaMask("Zero_Doggy_Static", "Rogue_Pussy_Mask_Static")
    
    contains:                                                                                   
        # expanding pussy flap
        AlphaMask("Rogue_PussyHole_Static", "Rogue_Pussy_Hole_Mask_Static")  
                
image Rogue_Pussy_Hole_Mask_Static: 
    # This is the alpha used for the little flap in the heading animation "Rogue_Pussy_Moving"
    contains:                                                                                 
        #Base
        AlphaMask("images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518) 
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat 
            
image Rogue_PussyHole_Static: 
    #This is the image impacted by the mask for the pussy flap in "Rogue_Pussy_Moving"
    contains:                                                                                  
        #Mask
        "images/RogueDoggy/Rogue_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha .9
        block:
            ease 1 ypos 512
            pause 1
            ease 3 ypos 515
            repeat


image Rogue_Pussy_Heading:     
    #Full Animation for speed 1
    subpixel True
    contains:                                                                                   
        #Base
        "images/RogueDoggy/Rogue_Doggy_Pussy_FBase.png"    
        anchor (0.52,0.69)
        pos (220,518) # fix this back once re-exported(217,518) 
        xzoom 1
    contains:                                                                                   
        #moving hole
        "images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png"    
        subpixel True
        anchor (0.52,0.69)
        pos (217,518) 
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat 
    contains:
        ConditionSwitch( 
            #full hose/tights  
            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",    
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",  
            "RogueX.Panties and RogueX.PantiesDown", Null(), 
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png", 
            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",            
            "True", Null(), 
            ),
    contains:                                                                                  
        #Cock
        AlphaMask("Zero_Doggy_Heading", "Rogue_Pussy_Mask")
    
    contains:                                                                                   
        # expanding pussy flap
        AlphaMask("Rogue_Pussy_Heading_Flap", "Rogue_Pussy_Hole_Mask")  
        
        
image Rogue_Pussy_Hole_Mask: 
    # This is the alpha used for the little flap in the heading animation "Rogue_Pussy_Heading"
    contains:                                                                                 
        #Base
        AlphaMask("images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518) 
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat 
            
image Rogue_Pussy_Heading_Flap: 
    #This is the image impacted by the mask for the pussy flap in "Rogue_Pussy_Heading"
    contains:                                                                                  
        #Mask
        "images/RogueDoggy/Rogue_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha .9
        block:
            ease 1 ypos 505
            pause 1
            ease 3 ypos 515
            repeat

# > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

image Rogue_Pussy_Fucking2:                                                                                      
    #Full Animation for speed 2
    contains:                                                                                   
        #Base
        "images/RogueDoggy/Rogue_Doggy_Pussy_FBase.png"    
    contains:                                                                                 
        #Base
        "images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png"  
    contains:
        ConditionSwitch( 
            #full hose/tights  
            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",    
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",  
            "RogueX.Panties and RogueX.PantiesDown", Null(), 
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png", 
            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",            
            "True", Null(), 
            ),
    contains:                                                                                  
        #Cock        
        AlphaMask("Zero_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        

image Rogue_Pussy_Fucking3:                                                                                     
    #Full Animation for speed 3
    contains:                                                                                   
        #Base
        "images/RogueDoggy/Rogue_Doggy_Pussy_FBase.png"    
    contains:                                                                                 
        #Base
        "images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png"  
    contains:
        ConditionSwitch( 
            #full hose/tights  
            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",    
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",  
            "RogueX.Panties and RogueX.PantiesDown", Null(),   
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png", 
            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",            
            "True", Null(), 
            ),
    contains:                                                                                   
        #Cock        
        AlphaMask("Zero_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        
        
        
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        

image Rogue_Anal:                                                                                              
    #Anal static Loose
    contains:                                                                                
        #Base
        "images/RogueDoggy/Rogue_Doggy_Asshole_Loose.png"   
        anchor (0.50,0.69)
        pos (208,500)
        zoom 1.25
    contains:
        ConditionSwitch( 
            #full hose/tights  
            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",    
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",   
            "RogueX.Panties and RogueX.PantiesDown", Null(),  
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png", 
            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",            
            "True", Null(), 
            )
    contains:                                                                                   
        #Cock
        "Zero_Doggy_Insert"
        pos (172,500)

        
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Rogue_Anal_Heading:                                                                                      
    #Animation for speed 1   
    contains:                                                                                 
        #Base
        "images/RogueDoggy/Rogue_Doggy_Anal_FullBase.png"    
    contains:                                
        #Hole
        "images/RogueDoggy/Rogue_Doggy_Anal_FullHole.png"     
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .5
            repeat 
    contains:
        ConditionSwitch( 
            #full hose/tights  
            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",    
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",  
            "RogueX.Panties and RogueX.PantiesDown", Null(),   
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png", 
            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",            
            "True", Null(), 
            )
    contains:                                                                                   
        #Cock masking fixer (for when the bottom part tries to cut off)
        AlphaMask("Zero_Doggy_Anal_Heading", "Zero_Doggy_Anal_HeadingJunk")
    contains:                                                                                   
        #Cock with mask
        AlphaMask("Zero_Doggy_Anal_Heading", "Rogue_Doggy_Anal_Heading_Mask")

image Zero_Doggy_Anal_Heading:
        #the cock anal heading animation
    contains:
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 500#505
            repeat

image Zero_Doggy_Anal_HeadingJunk:
    #this is a mask to correct an annoying glitch in the core mask
    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease .5 ypos 550
            pause .25
            ease 1.75 ypos 600#505
            repeat
            
image Rogue_Doggy_Anal_Heading_Mask:   
    #the masking animation for the anal heading
    contains:
        "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .5
            repeat  

image Rogue_Doggy_Anal_Head_Top:               
#animation for anal fucking top half
    contains:
        subpixel True
        "Rogue_Doggy_Body"         
        ypos 0
        block:     
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat
            
image Rogue_Doggy_Anal_Head_Ass:               
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Rogue_Doggy_Ass"
        ypos 0
        block:     
            pause .4
            ease .2 ypos -10
            easeout .1 ypos -7          
            easein .9 ypos 0
            pause .9
            repeat
            
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Doggy_Anal1:                                                                                        
    #Animation for speed 2 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat
            
image Rogue_Anal_Fucking:                                                                                       
    #Animation for speed 2 Ass
    contains:                                                                                   
        #Base
        "images/RogueDoggy/Rogue_Doggy_Anal_FullBase.png"    
    contains:                                                                                  
        #Hole
        "images/RogueDoggy/Rogue_Doggy_Anal_FullHole.png" 
    contains:                                                                                   
        #Cheeks
        "images/RogueDoggy/Rogue_Doggy_Anal_FullCheeks.png"
    contains:
        ConditionSwitch( 
            #full hose/tights  
            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",    
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",  
            "RogueX.Panties and RogueX.PantiesDown", Null(),  
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png", 
            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",            
            "True", Null(), 
            ),    
    contains:                                                                                   
        #Cock
        AlphaMask("Zero_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")

image Rogue_Doggy_Anal_FullMask:    
    contains:                                                                                 
        #Mask
        "images/RogueDoggy/Rogue_Doggy_Anal_FullMask.png"
    contains:                                                                                   
        #Cheeks
        "images/RogueDoggy/Rogue_Doggy_Anal_FullCheeks.png"
    contains:
        ConditionSwitch( 
            #full hose/tights  
            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",    
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",  
            "RogueX.Panties and RogueX.PantiesDown", Null(), 
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png", 
            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",            
            "True", Null(), 
            )
        
image Rogue_Doggy_Fuck_Top:                
    #animation for anal fucking top half
    contains:
        subpixel True
        "Rogue_Doggy_Body"         
        ypos 15#28
        pause .4
        block: 
            ease .2 ypos 5#10
            pause .3
            ease 2 ypos 15#28 
            repeat
            
image Rogue_Doggy_Fuck_Ass:                
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Rogue_Doggy_Ass"
        ypos 0
        block:     
            pause .4
            ease .2 ypos -15#-25
            ease .1 ypos -5#-15
            pause .2
            ease 1.6 ypos 0   
            repeat


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>              
image Zero_Doggy_Anal2:                                                                                        
    #Animation for speed 3 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
            repeat
                      
image Rogue_Anal_Fucking2:                                                                                   
    #Animation for speed 3 Ass
    contains:                                                                                   
        #Base
        "images/RogueDoggy/Rogue_Doggy_Anal_FullBase.png"    
    contains:                                                                                  
        #Hole
        "images/RogueDoggy/Rogue_Doggy_Anal_FullHole.png"        
#    contains:                                                                                  
#        #Mask
#        "images/RogueDoggy/Rogue_Doggy_Anal_FullMask.png"
    contains:                                                                                  
        #Cheeks
        "images/RogueDoggy/Rogue_Doggy_Anal_FullCheeks.png"
    contains:
        ConditionSwitch( 
            #full hose/tights  
            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",    
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",  
            "RogueX.Panties and RogueX.PantiesDown", Null(), 
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png", 
            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",            
            "True", Null(), 
            )
    contains:                                                                                  
        #Cock
        AlphaMask("Zero_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png") 

image Rogue_Doggy_Fuck2_Top:               
    #animation for anal fucking2 top half
    contains:
        subpixel True
        "Rogue_Doggy_Body"         
        ypos 20
        block: 
            pause .15
            ease .1 ypos 0
            pause .1
            easein .5 ypos 20             
            pause .05
            repeat
            
image Rogue_Doggy_Fuck2_Ass:                
    #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Rogue_Doggy_Ass"
        ypos 5
        block:     
            pause .15
            ease .1 ypos -25
            ease .1 ypos -15
            pause .1
            ease .4 ypos 5 
            pause .05
            repeat


# Footjob animations > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

image Rogue_Doggy_Feet0:
    #static animation
    contains:
        "Rogue_Doggy_Shins"
        pos (0, 0) #(0,0) top
        block:
            subpixel True
            pause .5
            ease 2 ypos 20
            pause .5
            ease 2 ypos 0
            repeat    
    contains:
        ConditionSwitch(    
                "Player.Sprite", "Zero_Doggy_Up",            
                "True", Null(),
                )  
        zoom 1.2
        pos (145,480) 
    contains:
        "Rogue_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            subpixel True
            pause .5
            ease 2 ypos 20
            pause .5
            ease 2 ypos 0
            repeat    

image Rogue_Doggy_Feet1:
    #slow animation
    contains:
        "Rogue_Doggy_Shins"
        pos (0, 0) #(0,0) top
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat    
    contains:
        "Zero_Doggy_Up"
        zoom 1.2
        pos (145,480)
        block:
            pause .4
            ease 1.7 ypos 500
            ease .9 ypos 480
            repeat
    contains:
        "Rogue_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat     
    
image Rogue_Doggy_Feet2:
    #fast animation
    contains:
        "Rogue_Doggy_Shins"
        pos (0, 0) #(0,0) top
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos 0
            repeat    
    contains:
        "Zero_Doggy_Up"
        zoom 1.2
        pos (145,480)
        block:
            pause .07
            ease .6 ypos 500
            ease .28 ypos 480
            repeat
    contains:
        "Rogue_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos 0
            repeat 
# Footjob animations end > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >
            
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>             UI Tool animations

image Slap_Ass:    
    contains:
        "SlapHand"
        pause 1.2
        Null()

image Slap_Ass:
    contains:
        "UI_Hand"    
        subpixel True        
        zoom 1        
        alpha 0.5
        anchor (0.5,0.5)
        pos (600,380)         
        rotate 40 
        block:
            parallel:
                ease .5 xpos 300 rotate 80                
                ease .1 xpos 310 rotate 80
                pause .5
            parallel:
                ease .2 ypos 520
                pause .9        
            
image NotSlap_Ass:    
    contains:
        subpixel True
        "UI_Hand"
        zoom 1
        pos (600,380) #follow through  point r-60
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            pos (600,380)            
            rotate 40
            parallel:
                ease .5 xpos 300 rotate 80                
                ease .1 xpos 310 rotate 80
                pause .5
            parallel:
                ease .2 ypos 520
                pause .9
            repeat
                        

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     
#Doggy Launch/Reset
label Rogue_Doggy_Launch(Line = "massage"): 
    if Line == "sex":        
        $ Player.Cock = "in"
    elif Line == "anal":
        $ Player.Cock = "anal"
    elif Line == "solo":   
        $ Player.Sprite = 0
        $ Player.Cock = "out"
    elif Line == "massage":   
        $ Player.Sprite = 0
        $ Player.Cock = 0
    elif Line == "hotdog":          
        $ Player.Cock = "out"
    elif Line == "foot":          
        $ Player.Cock = "foot"
    if not Trigger:
        $ Trigger = Line
    if renpy.showing("Rogue_Doggy_Animation"):
        return     
    $ Player.Sprite = 1
    $ Speed = 0
    hide Rogue_Sprite 
    if renpy.showing("Rogue_BJ_Animation"):
            hide Rogue_BJ_Animation   
    if renpy.showing("Rogue_HJ_Animation"):
            hide Rogue_HJ_Animation   
    if renpy.showing("Rogue_TJ_Animation"):
            hide Rogue_TJ_Animation   
    show Rogue_Doggy_Animation at SpriteLoc(StageCenter+50) zorder 150
    with dissolve
    return
    
label Rogue_Doggy_Reset:
    if not renpy.showing("Rogue_Doggy_Animation"):
        return
#    $ Trigger = 0               #fix, not sure this is a good idea
    $ RogueX.ArmPose = 2      
    $ RogueX.SpriteVer = 0
    hide Rogue_Doggy_Animation
    call Rogue_Hide 
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
                    alpha 1
                    zoom 1
                    offset (0,0)
                    anchor (0.6, 0.0)
    with dissolve
    $ Speed = 0
    return
    
label Rogue_Sex_Reset:
    #make this a thing later once implemented
    return
    
               
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# Core Rogue BJ element ///////////////////////////////////////////////////////////////////////////                                     Core Rogue BJ element
#Rogue BJ Over Sprite Compositing


image Rogue_BJ_Animation:#BJ_NewTest:                                                                #core BJ animation   
    LiveComposite(    
        (787,913),             
        (0,0), ConditionSwitch(                                                                 # back of the hair, which needs to go behind the body
            "Speed == 0", At("BJ_HairBack", BJ_Starting()),                         
            "Speed == 1", At("BJ_HairBack", BJ_Licking()),                         
            "Speed == 2", At("BJ_HairBack", BJ_Heading()),                        
            "Speed == 3", At("BJ_HairBack", BJ_Sucking()),
            "Speed == 4", At("BJ_HairBack", BJ_Deep()), 
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(                                                                 # body, everything below the chin
            "Speed == 0", At("BJ_Backdrop", BJ_StartingBody()),                       
            "Speed == 1", At("BJ_Backdrop", BJ_LickingBody()),                        
            "Speed == 2", At("BJ_Backdrop", BJ_HeadingBody()),                 
            "Speed == 3", At("BJ_Backdrop", BJ_SuckingBody()),
            "Speed == 4", At("BJ_Backdrop", BJ_DeepBody()), 
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(                                                                 # her head
            "Speed == 0", At("BJ_Head", BJ_Starting()),                       
            "Speed == 1", At("BJ_Head", BJ_Licking()),                       
            "Speed == 2", At("BJ_Head", BJ_Heading()),                     
            "Speed == 3", At("BJ_Head", BJ_Sucking()),
            "Speed == 4", At("BJ_Head", BJ_Deep()), 
            "True", Null(),
            ),   
#        (0,0), Transform("images/RogueBJFace/Rogue_bj_markercard.png", alpha=(.2)),
        (0,0), ConditionSwitch(                                                                 # cock
            "Speed == 0", At("Blowcock", Cock_BJ_Starting()),   
            "Speed == 1", At("Blowcock", Cock_BJ_Licking()),                                  
            "Speed == 2", At("Blowcock", Cock_BJ_Straight()),
            "Speed == 3", At("Blowcock", Cock_BJ_Straight()),                          
            "Speed == 4", At("Blowcock", Cock_BJ_Straight()), 
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(                                                                 # the masked overlay for when her head overlaps the cock
            "Speed < 3", Null(), 
            "Speed == 3", At(AlphaMask("BJ_Head", "images/RogueBJFace/Rogue_bj_facemask.png"), BJ_Sucking()),
            "Speed == 4", At(AlphaMask("BJ_Head", "images/RogueBJFace/Rogue_bj_facemask.png"), BJ_Deep()), 
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(                                                                 # same as above, but for the heading animation
            "Speed == 2", At(AlphaMask("BJ_Head", "BJ_MaskHeadingComposite"), BJ_Heading()),
            "True", Null(),
            ),    
        )
    zoom .55
    anchor (.5,.5)
    
image BJ_HairBack:
    ConditionSwitch(                                                                            #Hair underlay
            "RogueX.Water and RogueX.Hair == 'evo'", "images/RogueBJFace/Rogue_bj_hair_back_wet.png",
            "RogueX.Hair == 'wet'", "images/RogueBJFace/Rogue_bj_hair_back_wet.png",
            "True", "images/RogueBJFace/Rogue_bj_hair_back.png",
            ),
    
image BJ_Backdrop:                                                                        #Her Body under the head
    "Rogue_Sprite"
    zoom 4.5
    pos (175,-110)
    offset (-615, -125)
    
image BJ_Head:                                                                            #These are all the details of the face
    LiveComposite(    
        (787,913),     
        (0,0), ConditionSwitch(                                                                 #Hair back
            "RogueX.Water and RogueX.Hair == 'evo'", AlphaMask("images/RogueBJFace/Rogue_bj_hair_back_wet.png", "BJ_Backdrop"),
            "RogueX.Hair == 'wet'", AlphaMask("images/RogueBJFace/Rogue_bj_hair_back_wet.png", "BJ_Backdrop"),
            "True", AlphaMask("images/RogueBJFace/Rogue_bj_hair_back.png", "BJ_Backdrop"),
            ),   
        (0,0), ConditionSwitch(                     
            "not Speed", "images/RogueBJFace/Rogue_bj_face_base.png",    
            "True", "images/RogueBJFace/Rogue_bj_face_base_s.png"
            ),   
        (0,0), ConditionSwitch(                                                                                 #Mouth for under layer
            "renpy.showing('Rogue_BJ_Animation') and Speed", ConditionSwitch(   
                    #if the BJface is happening
                    "Speed == 1 and 'mouth' in RogueX.Spunk", "images/RogueBJFace/Rogue_bj_mouth_lickingS.png",
                    "Speed == 1", "images/RogueBJFace/Rogue_bj_mouth_licking.png", #licking
                    "Speed == 2", Null(),                                               #heading Rogue_BJ_HeadingMouth()
                    "Speed == 3", "images/RogueBJFace/Rogue_bj_mouth_sucking.png", #sucking
                    "Speed >= 4", "images/RogueBJFace/Rogue_bj_mouth_sucking.png", #deepthroat      
                    "True", Null(), 
                    ),        
            "'mouth' in RogueX.Spunk", ConditionSwitch(   
                    #if spunk in mouth
                    "RogueX.Mouth == 'sucking'", "images/RogueBJFace/Rogue_bj_mouth_surprisedS.png",
                    "RogueX.Mouth == 'surprised'", "images/RogueBJFace/Rogue_bj_mouth_surprisedS.png",
                    "RogueX.Mouth == 'sad'", "images/RogueBJFace/Rogue_bj_mouth_sadS.png",
                    "RogueX.Mouth == 'kiss'", "images/RogueBJFace/Rogue_bj_mouth_sadS.png",
                    "RogueX.Mouth == 'smile'", "images/RogueBJFace/Rogue_bj_mouth_lipbiteS.png",              
                    "RogueX.Mouth == 'tongue'", "images/RogueBJFace/Rogue_bj_mouth_lickingS.png",
                    "True", "images/RogueBJFace/Rogue_bj_mouth_lipbiteS.png",  
                    ),    
            "True", ConditionSwitch(  
                    #if no Spunk
                    "RogueX.Mouth == 'normal'", "images/RogueBJFace/Rogue_bj_mouth_normal.png",
                    "RogueX.Mouth == 'lipbite'", "images/RogueBJFace/Rogue_bj_mouth_lipbite.png",
                    "RogueX.Mouth == 'sucking'", "images/RogueBJFace/Rogue_bj_mouth_surprised.png",            
                    "RogueX.Mouth == 'kiss'", "images/RogueBJFace/Rogue_bj_mouth_kiss.png",
                    "RogueX.Mouth == 'sad'", "images/RogueBJFace/Rogue_bj_mouth_sad.png",
                    "RogueX.Mouth == 'smile'", "images/RogueBJFace/Rogue_bj_mouth_smile.png",            
                    "RogueX.Mouth == 'grimace'", "images/RogueBJFace/Rogue_bj_mouth_smile.png",
                    "RogueX.Mouth == 'surprised'", "images/RogueBJFace/Rogue_bj_mouth_surprised.png",          
                    "RogueX.Mouth == 'tongue'", "images/RogueBJFace/Rogue_bj_mouth_licking.png",    
                    "True", "images/RogueBJFace/Rogue_bj_mouth_normal.png",
                    ),    
            ),     
#            "Speed == 1 and Trigger == 'blow' and 'mouth' in RogueX.Spunk", "images/RogueBJFace/Rogue_bj_mouth_lickingS.png",
#            "Speed == 1 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_mouth_licking.png", #licking
#            "Speed == 2 and Trigger == 'blow'", Null(),                                #heading Rogue_BJ_HeadingMouth()
#            "Speed == 3 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_mouth_sucking.png", #sucking
#            "Speed == 4 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_mouth_sucking.png", #deepthroat         
#            "'mouth' in RogueX.Spunk and RogueX.Mouth == 'sucking'", "images/RogueBJFace/Rogue_bj_mouth_surprisedS.png",
#            "'mouth' in RogueX.Spunk and RogueX.Mouth == 'surprised'", "images/RogueBJFace/Rogue_bj_mouth_surprisedS.png",
#            "'mouth' in RogueX.Spunk and RogueX.Mouth == 'sad'", "images/RogueBJFace/Rogue_bj_mouth_sadS.png",
#            "'mouth' in RogueX.Spunk and RogueX.Mouth == 'kiss'", "images/RogueBJFace/Rogue_bj_mouth_sadS.png",
#            "'mouth' in RogueX.Spunk and RogueX.Mouth == 'smile'", "images/RogueBJFace/Rogue_bj_mouth_lipbiteS.png",              
#            "'mouth' in RogueX.Spunk and RogueX.Mouth == 'tongue'", "images/RogueBJFace/Rogue_bj_mouth_lickingS.png",
#            "'mouth' in RogueX.Spunk", "images/RogueBJFace/Rogue_bj_mouth_lipbiteS.png",
#            "RogueX.Mouth == 'normal'", "images/RogueBJFace/Rogue_bj_mouth_normal.png",
#            "RogueX.Mouth == 'lipbite'", "images/RogueBJFace/Rogue_bj_mouth_lipbite.png",
#            "RogueX.Mouth == 'sucking'", "images/RogueBJFace/Rogue_bj_mouth_surprised.png",            
#            "RogueX.Mouth == 'kiss'", "images/RogueBJFace/Rogue_bj_mouth_kiss.png",
#            "RogueX.Mouth == 'sad'", "images/RogueBJFace/Rogue_bj_mouth_sad.png",
#            "RogueX.Mouth == 'smile'", "images/RogueBJFace/Rogue_bj_mouth_smile.png",            
#            "RogueX.Mouth == 'grimace'", "images/RogueBJFace/Rogue_bj_mouth_smile.png",
#            "RogueX.Mouth == 'surprised'", "images/RogueBJFace/Rogue_bj_mouth_surprised.png",          
#            "RogueX.Mouth == 'tongue'", "images/RogueBJFace/Rogue_bj_mouth_licking.png",    
#            "True", "images/RogueBJFace/Rogue_bj_mouth_normal.png",
#            ),   
        (316,590), ConditionSwitch(      #600               
            "renpy.showing('Rogue_BJ_Animation') and Speed == 2", At("BJ_MouthHeading", BJ_MouthAnim()),     
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                                 #cum for under layer
            "'facial' in RogueX.Spunk", "images/RogueBJFace/Rogue_bj_facial_under.png",
            "not RogueX.Spunk or Trigger != 'blow' or 'mouth' not in RogueX.Spunk", Null(),
#            "Speed == 2", "images/RogueBJFace/Rogue_bj_face_under_heading_cum.png", 
            "Speed == 3", "images/RogueBJFace/Rogue_bj_face_under_sucking_cum.png",
            "Speed == 4", "images/RogueBJFace/Rogue_bj_face_under_sucking_cum.png",  
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(                                                                 #Brows
            "RogueX.Brows == 'normal'", "images/RogueBJFace/Rogue_bj_face_brows_normal.png",
            "RogueX.Brows == 'angry'", "images/RogueBJFace/Rogue_bj_face_brows_angry.png",
            "RogueX.Brows == 'sad'", "images/RogueBJFace/Rogue_bj_face_brows_sad.png",
            "RogueX.Brows == 'surprised'", "images/RogueBJFace/Rogue_bj_face_brows_surprised.png",        
            "RogueX.Brows == 'confused'", "images/RogueBJFace/Rogue_bj_face_brows_confused.png",
            "True", "images/RogueBJFace/Rogue_bj_face_brows_normal.png",
            ),
        (0,0), "BJ Blink",                                                                #Eyes
        (0,0), ConditionSwitch(                                                                 #cum on the face
                "'facial' in RogueX.Spunk", "images/RogueBJFace/Rogue_bj_facial_over.png",
                "not RogueX.Spunk or Trigger != 'blow' or 'mouth' not in RogueX.Spunk", Null(),
#                "Speed == 2", "images/RogueBJFace/Rogue_bj_face_over_heading_cum.png", 
                "Speed == 3", "images/RogueBJFace/Rogue_bj_face_over_sucking_cum.png",
                "Speed == 4", "images/RogueBJFace/Rogue_bj_face_over_sucking_cum.png",  
                "True", Null(),
                ),
        (0,0), ConditionSwitch(                                                                 #Hair overlay
            "RogueX.Water and RogueX.Hair == 'evo'", "images/RogueBJFace/Rogue_bj_hair_wet.png",
            "RogueX.Hair == 'wet'", "images/RogueBJFace/Rogue_bj_hair_wet.png",
            "True", "images/RogueBJFace/Rogue_bj_hair.png",
            ),
        )


image BJ Blink:                                                                           #eyeblinks
    ConditionSwitch(
        "RogueX.Eyes == 'normal'", "images/RogueBJFace/Rogue_bj_face_eyes_normal.png",  
        "RogueX.Eyes == 'sexy'", "images/RogueBJFace/Rogue_bj_face_eyes_sexy.png",  
        "RogueX.Eyes == 'closed'", "images/RogueBJFace/Rogue_bj_face_eyes_closed.png",
        "RogueX.Eyes == 'surprised'", "images/RogueBJFace/Rogue_bj_face_eyes_surprised.png",
        "RogueX.Eyes == 'side'", "images/RogueBJFace/Rogue_bj_face_eyes_side.png",
        "RogueX.Eyes == 'stunned'", "images/RogueBJFace/Rogue_bj_face_eyes_stunned.png",
        "RogueX.Eyes == 'down'", "images/RogueBJFace/Rogue_bj_face_eyes_down.png",
        "RogueX.Eyes == 'manic'", "images/RogueBJFace/Rogue_bj_face_eyes_surprised.png",
        "RogueX.Eyes == 'squint'", "images/RogueBJFace/Rogue_bj_face_eyes_squint.png",
        "True", "images/RogueBJFace/Rogue_bj_face_eyes_normal.png",  
        )
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/RogueBJFace/Rogue_bj_face_eyes_closed.png"
    .25
    repeat

image BJ_MouthHeading:                                          
    #the mouth used for the heading animations
    contains:
        ConditionSwitch(   
            #if spunk in mouth
            "'mouth' in RogueX.Spunk", "images/RogueBJFace/Rogue_bj_mouth_suckingS.png",
            "True", "images/RogueBJFace/Rogue_bj_mouth_sucking.png",  
            )   
#        "images/RogueBJFace/Rogue_bj_mouth_sucking.png"
        anchor (0.40,0.65) 
        
image BJ_MaskHeading:                                           
    #the mask used for the heading image 
    contains:
        "images/RogueBJFace/Rogue_bj_facemask.png"
        anchor (0.4,0.65)    

image BJ_MaskHeadingComposite:                                 
    #The composite for the heading mask that goes over the face
    LiveComposite(    
        (787,913),  
        (316,590), ConditionSwitch(      #600               
            "Speed == 2", At("BJ_MaskHeading", BJ_MouthAnim()),     
            "True", Null(),
            ),  
        )
    
transform BJ_MouthAnim():                                       
        #The animation for the heading mouth
        subpixel True
        zoom 0.90     #small 
        block: #total time 10 down, 15 back up
            pause .40            
            easeout .40 zoom 0.87
            linear .10 zoom 0.9
            easein .45 zoom 0.70 
            pause .15                       
            easeout .25 zoom 0.9
            linear .10 zoom 0.87
            easein .30 zoom 0.9   
            pause .35
            
            
image Blowcock:
    contains:
        ConditionSwitch(        
            "Player.Color == 'pink'", "images/RogueBJFace/Zero_Cock_P.png",
            "Player.Color == 'brown'", "images/RogueBJFace/Zero_Cock_B.png",             
            "Player.Color == 'green'", "images/RogueBJFace/Zero_Cock_G.png", 
            "True", Null(),
            ),   
    contains:
        ConditionSwitch(                 
            "Player.Wet", "images/RogueBJFace/Zero_Cock_Wet.png", 
            "True", Null(),
            ),       
    contains:
        ConditionSwitch(    
            "Player.Spunk", "images/RogueBJFace/Zero_Cock_S.png", 
            "True", Null(),
            ),  
    anchor (0.5,0.5)
    zoom 1.0
    alpha 1.0
    offset (26,350)#(-175,450)
    
transform Cock_BJ_Starting():                           
    #The static animation for the cock
    anchor (.5,.5)
    rotate -10

transform Cock_BJ_Licking():                            
    #The licking animation for the cock
    subpixel True
    anchor (.5,.5)
    ease 0.5 rotate 0
    block:
        ease 2 rotate -5 #410
        pause .5
        ease 2.5 rotate 0
        repeat
        
transform Cock_BJ_Straight():                            
    #The static animation for the cock
    anchor (.5,.5)
    rotate 0
    
transform BJ_Licking():                                
    #The licking animation for her face
    subpixel True 
    ease 0.5 offset (0,-35)  #top
    block:
        ease 2.5 offset (25,100) #bottom
        ease 2 offset (0,-35)  #top
        pause .5
        repeat

transform BJ_LickingBody():                            
    #The licking animation for her body
    subpixel True 
    ease 0.5 offset (0,-35)  #top
    block:
        ease 2.5 offset (30,90) #bottom 25,50
        ease 2 offset (0,-35)  #top
        pause .5
        repeat
        
transform BJ_Heading():                                
    #The heading animation for her face
    subpixel True 
    offset (0,-40)     #top 
    block:
        ease 1 yoffset 35           #bottom         
        ease 1.5 offset (0,-40)     #top  
        repeat

transform BJ_HeadingBody():                             
    #The heading animation for her body
    subpixel True 
    offset (0,-40)     #top 
    block:
        ease 1 yoffset 15           #bottom         
        ease 1.5 offset (0,-40)     #top  
        repeat
        
transform BJ_Sucking():                                 
    #The sucking animation for her face
    subpixel True
    ease 0.5 offset (0,50) 
    block:
        ease 1 yoffset 120 #100
        ease 1.5 offset (0,50) 
        repeat
    
transform BJ_SuckingBody():                            
    #The sucking animation for her body
    subpixel True 
    ease 0.5 offset (0,50)  
    block:
        ease 1 yoffset 100 #80      #bottom
        ease 1.5 offset (0,50) #top
        repeat
    
transform BJ_Deep():                                   
    #The deep animation for her face
    ease .5 offset (0,100) 
    block:
        subpixel True
        ease 1 yoffset 300
        pause .5
        ease 2 yoffset 100  
        repeat
        
transform BJ_DeepBody():                               
    #The deep animation for her body
    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1.2 yoffset 250
        pause .5
        ease 1.8 yoffset 100   
        repeat    

transform BJ_Static():                                  
    #The static animation for her face
    subpixel True 
    ease 1.5 offset (0,0)
    repeat

transform BJ_StaticBody():                              
    #The static animation for her face
    subpixel True 
    ease 1.5 offset (0,0)
                                         
transform BJ_Starting():                                
    #The starting animation for her face
    subpixel True 
    ease 1.5 offset (0,0)
    
transform BJ_StartingBody():                           
    #The starting animation for her face
    subpixel True 
    ease 1.5 offset (0,0)
                                                               #BJ Launchers  
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Rogue_BJ_Launch(Line = 0):    
    # The sequence to launch the Rogue BJ animations  
    if renpy.showing("Rogue_BJ_Animation"):
        return
    
    call Rogue_Hide
    if Line == "L" or Line == "cum":
        show Rogue_Sprite at SpriteLoc(StageCenter) zorder RogueX.Layer:
            alpha 1
#            zoom 1 offset (0,0)
            ease 1 zoom 2.5 offset (70,140) #(-90,140) offset (150,80) 
        with dissolve
    else:
        show Rogue_Sprite at SpriteLoc(StageCenter) zorder RogueX.Layer:
            alpha 1
            zoom 2.5 offset (70,140) #(-90,140) 
        with dissolve
                
    if Taboo and Line == "L": 
            # Rogue gets started. . .
            if len(Present) >= 2:
                if Present[0] != RogueX:
                        "[RogueX.Name] looks back at [Present[0].Name] to see if she's watching."
                elif Present[1] != RogueX:
                        "[RogueX.Name] looks back at [Present[1].Name] to see if she's watching."
            else:
                        "[RogueX.Name] looks around to see if anyone can see her."
    if Line == "L":    
            if not RogueX.Blow:
                "[RogueX.Name] hesitantly pulls down your pants and touches her mouth to your cock."
            else:
                "[RogueX.Name] bends down and begins to suck on your cock."    
            
    $ Speed = 0
    
    if Line != "cum":
        $ Trigger = "blow"
    
    show Rogue_Sprite zorder RogueX.Layer:
        alpha 0
    show Rogue_BJ_Animation zorder 150: 
        pos (645,510) 
    return
    
label Rogue_BJ_Reset: # The sequence to the Rogue animations from BJ to default
    if not renpy.showing("Rogue_BJ_Animation"):
        return
#    hide Rogue_BJ_Animation
    call Rogue_Hide 
    $ Speed = 0
    
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:        
        zoom 2 offset (70,140)
        alpha 1
        block:
            pause .5
            ease 1 zoom 1.5 offset (-50,50)
            pause .5
            ease .5 zoom 1 offset (0,0)    
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
        alpha 1
        zoom 1 offset (0,0)    
    $ RogueX.FaceChange("sexy")        
    return  
    
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////


#       Face currently used for titfucking. Remove once titfucking uses new facial system


image Rogue_BJFace:
    LiveComposite(    
        (787,912),     
        (0,0), ConditionSwitch(
            "RogueX.Blush and Trigger != 'blow'", "images/RogueBJFace/Rogue_bj_face_over_blush.png",
            "Trigger != 'blow'", Null(),
            "Speed == 3 and RogueX.Blush", "images/RogueBJFace/Rogue_bj_face_over_suckingB.png",
            "Speed == 3 and not RogueX.Blush", "images/RogueBJFace/Rogue_bj_face_over_sucking.png",
            "Speed == 2 and RogueX.Blush", "images/RogueBJFace/Rogue_bj_face_over_headingB.png",
            "Speed == 2 and not RogueX.Blush", "images/RogueBJFace/Rogue_bj_face_over_heading.png",
            "Speed == 4 and RogueX.Blush", "images/RogueBJFace/Rogue_bj_face_over_suckingB.png",
            "Speed == 4 and not RogueX.Blush", "images/RogueBJFace/Rogue_bj_face_over_sucking.png",
            "RogueX.Blush", "images/RogueBJFace/Rogue_bj_face_over_blush.png",
            "True", Null(),
            ),       
        (0,0), ConditionSwitch(
            "RogueX.Brows == 'normal'", "images/RogueBJFace/Rogue_bj_face_brows_normal.png",
            "RogueX.Brows == 'angry'", "images/RogueBJFace/Rogue_bj_face_brows_angry.png",
            "RogueX.Brows == 'sad'", "images/RogueBJFace/Rogue_bj_face_brows_sad.png",
            "RogueX.Brows == 'surprised'", "images/RogueBJFace/Rogue_bj_face_brows_surprised.png",        
            "RogueX.Brows == 'confused'", "images/RogueBJFace/Rogue_bj_face_brows_confused.png",
            "True", "images/RogueBJFace/Rogue_bj_face_brows_normal.png",
            ),
        (0,0), "Rogue_BJ Blink",  
        (0,0), ConditionSwitch(
                "not RogueX.Spunk", Null(),
                "'mouth' in RogueX.Spunk and Speed == 2 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_face_over_heading_cum.png", 
                "'mouth' in RogueX.Spunk and Speed == 3 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_face_over_sucking_cum.png",
                "'mouth' in RogueX.Spunk and Speed == 4 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_face_over_sucking_cum.png",  
                "True", Null(),
                ),
        (0,0), ConditionSwitch(
                "not RogueX.Spunk", Null(),
                "'facial' in RogueX.Spunk", "images/RogueBJFace/Rogue_bj_facial_over.png", 
                "True", Null(),
                ),
        (0,0), ConditionSwitch(
            "RogueX.Hair == 'evo'", "images/RogueBJFace/Rogue_bj_hair.png",
            "True", "images/RogueBJFace/Rogue_bj_hair.png",
            ),              
        )

#Rogue BJ Under Sprite Compositing
image Rogue_BJChin:
    LiveComposite(
        (787,912),     
        (0,0), "images/RogueBJFace/Rogue_bj_face_under.png", 
        (0,0), ConditionSwitch(    
            "Speed == 1 and Trigger == 'blow' and 'mouth' in RogueX.Spunk", "images/RogueBJFace/Rogue_bj_mouth_lickingS.png",
            "Speed == 1 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_mouth_licking.png",
            "Speed == 2 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_mouth_heading.png", 
            "Speed == 3 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_mouth_sucking.png",
            "Speed == 4 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_mouth_sucking.png",           
            "'mouth' in RogueX.Spunk and RogueX.Mouth == 'sucking'", "images/RogueBJFace/Rogue_bj_mouth_surprisedS.png",
            "'mouth' in RogueX.Spunk and RogueX.Mouth == 'surprised'", "images/RogueBJFace/Rogue_bj_mouth_surprisedS.png",
            "'mouth' in RogueX.Spunk and RogueX.Mouth == 'sad'", "images/RogueBJFace/Rogue_bj_mouth_sadS.png",
            "'mouth' in RogueX.Spunk and RogueX.Mouth == 'kiss'", "images/RogueBJFace/Rogue_bj_mouth_sadS.png",
            "'mouth' in RogueX.Spunk and RogueX.Mouth == 'smile'", "images/RogueBJFace/Rogue_bj_mouth_lipbiteS.png",              
            "'mouth' in RogueX.Spunk and RogueX.Mouth == 'tongue'", "images/RogueBJFace/Rogue_bj_mouth_lickingS.png",
            "'mouth' in RogueX.Spunk", "images/RogueBJFace/Rogue_bj_mouth_lipbiteS.png",
            "RogueX.Mouth == 'normal'", "images/RogueBJFace/Rogue_bj_mouth_normal.png",
            "RogueX.Mouth == 'lipbite'", "images/RogueBJFace/Rogue_bj_mouth_lipbite.png",
            "RogueX.Mouth == 'sucking'", "images/RogueBJFace/Rogue_bj_mouth_surprised.png",            
            "RogueX.Mouth == 'kiss'", "images/RogueBJFace/Rogue_bj_mouth_kiss.png",
            "RogueX.Mouth == 'sad'", "images/RogueBJFace/Rogue_bj_mouth_sad.png",
            "RogueX.Mouth == 'smile'", "images/RogueBJFace/Rogue_bj_mouth_smile.png",            
            "RogueX.Mouth == 'grimace'", "images/RogueBJFace/Rogue_bj_mouth_smile.png",
            "RogueX.Mouth == 'surprised'", "images/RogueBJFace/Rogue_bj_mouth_surprised.png",          
            "RogueX.Mouth == 'tongue'", "images/RogueBJFace/Rogue_bj_mouth_licking.png",    
            "True", "images/RogueBJFace/Rogue_bj_mouth_normal.png",
            ),       
        (0,0), ConditionSwitch(
                "not RogueX.Spunk", Null(),
                "'mouth' in RogueX.Spunk and Speed == 2 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_face_under_heading_cum..png", 
                "'mouth' in RogueX.Spunk and Speed == 3 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_face_under_sucking_cum.png",
                "'mouth' in RogueX.Spunk and Speed == 4 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_face_under_sucking_cum.png",  
                "True", Null(),
                ),
        (0,0), ConditionSwitch(
                "not RogueX.Spunk", Null(),
                "'facial' in RogueX.Spunk", "images/RogueBJFace/Rogue_bj_facial_under.png", 
                "True", Null(),
                ),
        )

image Rogue_BJ Blink:
    ConditionSwitch(
        "RogueX.Eyes == 'normal'", "images/RogueBJFace/Rogue_bj_face_eyes_normal.png",  
        "RogueX.Eyes == 'sexy'", "images/RogueBJFace/Rogue_bj_face_eyes_sexy.png",  
        "RogueX.Eyes == 'closed'", "images/RogueBJFace/Rogue_bj_face_eyes_closed.png",
        "RogueX.Eyes == 'surprised'", "images/RogueBJFace/Rogue_bj_face_eyes_surprised.png",
        "RogueX.Eyes == 'side'", "images/RogueBJFace/Rogue_bj_face_eyes_side.png",
        "RogueX.Eyes == 'stunned'", "images/RogueBJFace/Rogue_bj_face_eyes_stunned.png",
        "RogueX.Eyes == 'down'", "images/RogueBJFace/Rogue_bj_face_eyes_down.png",
        "RogueX.Eyes == 'manic'", "images/RogueBJFace/Rogue_bj_face_eyes_surprised.png",
        "RogueX.Eyes == 'squint'", "images/RogueBJFace/Rogue_bj_face_eyes_sexy.png",
        "True", "images/RogueBJFace/Rogue_bj_face_eyes_normal.png",  
        ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/RogueBJFace/Rogue_bj_face_eyes_closed.png"
    .25
    repeat
    
transform Zero_BJ_Static():                            #The static animation for the cock
    anchor (.5,.5)
#    pos (180,560) #(125,300)
    rotate -10
#    pos (-25,0)

transform Zero_BJ_Sucking():                            #The sucking animation for the cock
    anchor (.5,.5)
    rotate 0

    
transform Zero_BJ_Licking():                            #The licking animation for the cock
    subpixel True
    block:
        ease 2 rotate -5 #410
        pause .5
        ease 2.5 rotate 0
        repeat

image Zero_Blowcock:
    LiveComposite(                            #The compositived BJ cock
        (175,946),             
        (0,0), ConditionSwitch(        
            "Player.Color == 'pink'", "images/RogueBJFace/Zero_Cock_P.png",
            "Player.Color == 'brown'", "images/RogueBJFace/Zero_Cock_B.png",             
            "Player.Color == 'green'", "images/RogueBJFace/Zero_Cock_G.png", 
            "True", Null(),
            ),   
        (0,0), ConditionSwitch(                 
            "Player.Wet", "images/RogueBJFace/Zero_Cock_Wet.png", 
            "True", Null(),
            ),       
        (0,0), ConditionSwitch(    
            "Player.Spunk", "images/RogueBJFace/Zero_Cock_S.png", 
            "True", Null(),
            ),       
        )
    anchor (0.5,0.5)
    zoom 1.2
    xoffset 5

   

# Core Rogue Titfucking element //////////////////////////////////////////////////////////////////////                                         Core Rogue TJ element

image Rogue_TJ_Under: 
    contains:
        "images/RogueBJFace/Rogue_bj_hair_back.png"
        pos (150, -560)
        zoom .95
    contains:
        "images/RogueBJFace/Rogue_tj_base.png" 
    contains:
        ConditionSwitch( 
            "'tits' in RogueX.Spunk", "images/RogueBJFace/Rogue_tj_spunkU.png",
            "True", Null(),
            ),
    contains:
        "Rogue_BJChin"
        pos (150, -560)
        zoom .95
    contains:
        "Rogue_BJFace" 
        pos (150, -560)
        zoom .95
    pos (-60, 200)

image Rogue_TJ_Over:     
    contains:
        ConditionSwitch( 
            "RogueX.Pierce == 'barbell'", "images/RogueBJFace/Rogue_tj_tits_b.png", 
            "RogueX.Pierce == 'ring'", "images/RogueBJFace/Rogue_tj_tits_r.png",
            "RogueX.Pierce != 'barbell'", "images/RogueBJFace/Rogue_tj_tits.png",
            ),
    contains:
        ConditionSwitch( 
            "'tits' in RogueX.Spunk", "images/RogueBJFace/Rogue_tj_spunk.png",
            "True", Null(),
            ),
    pos (-60, 200)


transform Rogue_TJ_Under_1():
    ypos 200
    subpixel True
    block:
        ease 1 ypos 300
        easeout .2 ypos 300
        easein 1.3 ypos 120
        repeat

transform Rogue_TJ_Over_1():
    ypos 200
    subpixel True
    block:
        ease 1.20 ypos 300
        easeout .1 ypos 300
        easein 1.2 ypos 120
        repeat
        
transform Rogue_TJ_Under_2():
    ypos 200
    subpixel True
    block:
        ease .25 ypos 200
        ease .4 ypos 120
        ease .1 ypos 125
        repeat

transform Rogue_TJ_Over_2():
    ypos 200
    subpixel True
    block:
        ease .3 ypos 200
        ease .35 ypos 120
        ease .1 ypos 125          #high point
        repeat
        
        
transform Zero_TJ_Cock():                      
    #The sucking animation for the cock
    anchor (.5,.5)
    pos (440,1020) #220,1000 #(180,560)
    rotate 0
    
transform Zero_TJ_Cock_1():
    pos (440,1020)
    subpixel True
    block:
        ease 1 ypos 1050
        easeout .2 ypos 1060
        easein 1.3 ypos 1020
        repeat
        
transform Zero_TJ_Cock_2():
    pos (440,1020)
    subpixel True
    block:
        ease .35 ypos 1030
        ease .4 ypos 1020
#        pause .1
        repeat



image Rogue_TJ_Animation:                                                                                              
    #core TJ animation
    contains:
        ConditionSwitch(        
            "not Speed", Transform("Rogue_TJ_Under"), 
            "Speed == 1", At("Rogue_TJ_Under", Rogue_TJ_Under_1()),
            "Speed >= 2", At("Rogue_TJ_Under", Rogue_TJ_Under_2()),
            "Speed", Null(),
            ),  
    
    contains:
        ConditionSwitch(         
            "not Speed", At("Zero_Blowcock", Zero_TJ_Cock()),
            "Speed == 1", At("Zero_Blowcock", Zero_TJ_Cock_1()),
            "Speed >= 2", At("Zero_Blowcock", Zero_TJ_Cock_2()),
            "Speed", Null(),
            ),  
        
    contains:
        ConditionSwitch(         
            "not Speed", Transform("Rogue_TJ_Over"), 
            "Speed == 1", At("Rogue_TJ_Over", Rogue_TJ_Over_1()),
            "Speed >= 2", At("Rogue_TJ_Over", Rogue_TJ_Over_2()), 
            "Speed", Null(),
            ),     
    anchor (0.6, 0.0)
    offset (-75, 250)
    zoom .55
        
label Rogue_TJ_Launch(Line = 0):  
    # The sequence to launch the Rogue Titfuck animations   
    if renpy.showing("Rogue_TJ_Animation"):
        return
    call Rogue_Hide
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
        alpha 1
        ease 1 zoom 2 xpos 550 yoffset 50 #offset (-100,50) 
    if Taboo: # Rogue gets started. . .
            if len(Present) >= 2:
                if Present[0] != RogueX:
                        "[RogueX.Name] looks back at [Present[0].Name] to see if she's watching."
                elif Present[1] != RogueX:
                        "[RogueX.Name] looks back at [Present[1].Name] to see if she's watching."
            else:
                        "[RogueX.Name] looks around to see if anyone can see her."
    
    if RogueX.Chest and RogueX.Over:
        "She throws off her [RogueX.Over] and her [RogueX.Chest]."                
    elif RogueX.Over:
        "She throws off her [RogueX.Over], baring her breasts underneath."
    elif RogueX.Chest:
        "She tugs off her [RogueX.Chest] and throws it aside."
    $ RogueX.Over = 0
    $ RogueX.Chest = 0
    $ RogueX.Arms = 0
    
    call Rogue_First_Topless                
    
    if not RogueX.Tit and Line == "L": #first time
        if not RogueX.Chest and not RogueX.Over:
            "As you pull out your cock, [RogueX.Name] hesitantly places it between her breasts and starts to rub them up and down the shaft."
        elif RogueX.Chest and not RogueX.Over:
            "As you pull out your cock, [RogueX.Name] hesitantly places it under her [RogueX.Chest], between her breasts and starts to rub them up and down the shaft."
        elif RogueX.Chest and RogueX.Over:
            "As you pull out your cock, [RogueX.Name] hesitantly places it under her [RogueX.Over], between her breasts and starts to rub them up and down the shaft."
        else:
            "As you pull out your cock, [RogueX.Name] hesitantly places it under her clothes, between her breasts and starts to rub them up and down the shaft."
    elif Line == "L": #any other time
        if not RogueX.Chest and not RogueX.Over:
            "As you pull out your cock, [RogueX.Name] places it between her breasts and starts to rub them up and down the shaft."
        elif RogueX.Chest and not RogueX.Over:
            "As you pull out your cock, [RogueX.Name] places it under her [RogueX.Chest], between her breasts and starts to rub them up and down the shaft."
        elif RogueX.Chest and RogueX.Over:
            "As you pull out your cock, [RogueX.Name] places it under her [RogueX.Over], between her breasts and starts to rub them up and down the shaft."
        else:
            "As you pull out your cock, [RogueX.Name] places it under her clothes, between her breasts and starts to rub them up and down the shaft."    
    else:
            "[RogueX.Name] wraps her tits around your cock."
    show blackscreen onlayer black with dissolve
    show Rogue_Sprite zorder RogueX.Layer:
        alpha 0
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "titjob"
    show Rogue_TJ_Animation at SpriteLoc(StageRight) zorder 150 
    hide blackscreen onlayer black with dissolve
    return
    
label Rogue_TJ_Reset: 
    # The sequence to the Rogue animations from Titfuck to default
    if not renpy.showing("Rogue_TJ_Animation"):
            return
    hide Rogue_TJ_Animation
    call Rogue_Hide 
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
            zoom 2 xpos 550 yoffset 50
    show Rogue_Sprite zorder RogueX.Layer:
        alpha 1
        ease 1 zoom 1.5 xpos 500 yoffset 50
        pause .5
        ease .5 zoom 1 xpos RogueX.SpriteLoc yoffset 0
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
        alpha 1
        zoom 1 xpos RogueX.SpriteLoc yoffset 0   
        
    "[RogueX.Name] pulls back"
    return
    

# Core Rogue Handjob element //////////////////////////////////////////////////////////////////////                                         Core Rogue HJ element

image Zero_Handcock:
    contains:
        ConditionSwitch(    # Zero cock sucking
            "Player.Color == 'pink'", "images/RogueBJFace/handcock_P.png",
            "Player.Color == 'brown'", "images/RogueBJFace/handcock_B.png",             
            "Player.Color == 'green'", "images/RogueBJFace/handcock_G.png", 
            "Player.Color != 'pink'", Null(),
            ),  
    anchor (0.5,1.0)  #1.0
    pos (200,400)#(200,400)
        
image Rogue_Hand_Under:
    "images/RogueBJFace/hand2.png"
    anchor (0.5,0.5)
    pos (0,0)
    
    
image Rogue_Hand_Over:
    "images/RogueBJFace/hand1.png"    
    anchor (0.5,0.5)
    pos (0,0)

transform Handcock_1():
    subpixel True
    rotate_pad False
    ease .5 ypos 450 rotate -2 #450
    pause 0.25
    ease 1.0 ypos 400 rotate 0 #400
    pause 0.1
    repeat

transform Handcock_2():
    subpixel True
    rotate_pad False
    ease .2 ypos 430 rotate -3 #410
    ease .5 ypos 400 rotate 0
    pause 0.1
    repeat
    
transform Rogue_Hand_1():
    subpixel True
    ease .5 ypos 150 rotate 5 #500 #100 #rotate 10#   Bottom
    pause 0.25
    ease 1.0 ypos -100 rotate -5 #250#-150 #rotate -10#  Top
    pause 0.1
    repeat

transform Rogue_Hand_2():
    subpixel True
    ease 0.2 ypos 0 rotate 3   
    pause 0.1
    ease 0.4 ypos -100 rotate -3 
    pause 0.1
    repeat

image Rogue_HJ_Animation:  
    contains:
        ConditionSwitch(                                                # backside of the hand
            "not Speed", "Rogue_Hand_Under", 
            "Speed == 1", At("Rogue_Hand_Under", Rogue_Hand_1()),
            "Speed >= 2", At("Rogue_Hand_Under", Rogue_Hand_2()),
            "Speed", Null(),
            ),  
    contains:
        ConditionSwitch(                                                # cock
            "not Speed", "Zero_Handcock", 
            "Speed == 1", At("Zero_Handcock", Handcock_1()),
            "Speed >= 2", At("Zero_Handcock", Handcock_2()), 
            "Speed", Null(),
            ),  
        offset (0,0)
    contains:
        ConditionSwitch(                                                # fingers of the hand
            "not Speed", "Rogue_Hand_Over", 
            "Speed == 1", At("Rogue_Hand_Over", Rogue_Hand_1()),
            "Speed >= 2", At("Rogue_Hand_Over", Rogue_Hand_2()), 
            "Speed", Null(),
            ),   
    anchor (0.5,0.5)#anchor (0.51, -1.3)
    offset (200,800)
    zoom 0.6
        
label Rogue_HJ_Launch(Line = 0): 
    if renpy.showing("Rogue_HJ_Animation"):        
        $ Trigger = "hand"
        return
    call Rogue_Hide
    $ RogueX.Arms = 0
    $ RogueX.ArmPose = 1    
    if not renpy.showing("Rogue_Sprite"): 
        show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
            alpha 1
            zoom 1.7 xpos 700 yoffset 200 #offset (-50,200)
        with dissolve    
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
        alpha 1
        ease 1 zoom 1.7 xpos 700 yoffset 200 #offset (-50,200)
   
    if Taboo and Line == "L": 
        # Rogue gets started. . .
        if len(Present) >= 2:
            if Present[0] != RogueX:
                    "[RogueX.Name] looks back at [Present[0].Name] to see if she's watching."
            elif Present[1] != RogueX:
                    "[RogueX.Name] looks back at [Present[1].Name] to see if she's watching."
        else:
                    "[RogueX.Name] looks around to see if anyone can see her."
        if not RogueX.Hand and RogueX.Arms:
            "As you pull out your cock, [RogueX.Name] pulls off her gloves, and hesitantly reaches for it. She starts to roughly stroke on it."
        else:
            "She then leans over and grabs your cock."
    elif Line == "L":    
        if not RogueX.Hand and RogueX.Arms:
            "As you pull out your cock, [RogueX.Name] pulls off her gloves, and hesitantly reaches for it. She starts to roughly stroke on it."
        else:
            "[RogueX.Name] bends down and grabs your cock."
    else:
            "[RogueX.Name] bends down and grabs your cock."
            
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    show Rogue_HJ_Animation at SpriteLoc(RogueX.SpriteLoc) zorder 150 with easeinbottom
    return
    
label Rogue_HJ_Reset: # The sequence to the Rogue animations from handjob to default
    if not renpy.showing("Rogue_HJ_Animation"):
        return    
    $ Speed = 0
    hide Rogue_HJ_Animation
    with dissolve    
    call Rogue_Hide 
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
        alpha 1
        zoom 1.7  xpos 700 yoffset 200
    show Rogue_Sprite zorder RogueX.Layer:
        alpha 1
        ease 1 zoom 1.5 yoffset 50
        pause .5
        ease .5 zoom 1 xpos RogueX.SpriteLoc yoffset 0   
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
        alpha 1
        zoom 1  xpos RogueX.SpriteLoc yoffset 0        
    return
                
            
# Interface items //////////////////////////////////////////////////////////////////////////////

transform Vibrate():
    subpixel True
    block:
        linear .5 xoffset 2
        linear .5 xoffset -2
        repeat


image UI_Vibrator = LiveComposite( 
        (224,224),  
        (0,0), ConditionSwitch(
            "not Vibration", "UI_VibA", 
            "Vibration", At("UI_VibB", Vibrate()),
            ),  
        )        

image GropeLeftBreast:    
    contains:
        subpixel True
        "UI_Hand"
        zoom .7
        pos (300,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 90
        block: 
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image GropeRightBreast:    
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.7
        xzoom -0.7
        pos (180,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block: 
            ease 1 rotate -30
            ease 1 rotate -60 
            repeat

#image GropeBreast:
image LickRightBreast:   
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.5
        xzoom -0.5
        pos (160,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block: 
            ease .5 rotate -45 pos (150,370)            
            pause .5
            ease 1.5 rotate 30 pos (160,400)
            repeat

image LickLeftBreast:   
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.5
        xzoom -0.5
        pos (280,410)#(160,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block: 
            ease .5 rotate -45 pos (260,380)#(150,370)            
            pause .5
            ease 1.5 rotate 30 pos (280,410)#(160,400)
            repeat

image GropeThigh: 
    contains:
        subpixel True
        "UI_Hand"
        zoom .7
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

image GropePussy: 
    contains:
        subpixel True
        "UI_Hand"
        zoom .7
        pos (220,635)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice: 
                ease .5 rotate 190 pos (220,620)
                ease .75 rotate 170 pos (220,635)   
            choice: 
                ease .5 rotate 190 pos (220,620)
                pause .25
                ease 1 rotate 170 pos (220,635)             
            repeat

image FingerPussy: 
    contains:
        subpixel True
        "UI_Finger"       
        zoom 0.7
        pos (230,720)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice: 
                ease 1 rotate 40 pos (240,685)
                pause .5
                ease 1 rotate 50 pos (230,720)   
            choice:                          
                ease .5 rotate 40 pos (240,685)
                pause .5
                ease 1.75 rotate 50 pos (230,720)  
            choice:                          
                ease 2 rotate 40 pos (240,685)
                pause .5
                ease 1 rotate 50 pos (230,720)  
            choice:                          
                ease .25 rotate 40 pos (240,685)
                ease .25 rotate 50 pos (230,720) 
                ease .25 rotate 40 pos (240,685)
                ease .25 rotate 50 pos (230,720)
            repeat
            
image Lickpussy:   
    contains:
        subpixel True
        "UI_Tongue"        
        yzoom 0.5
        xzoom -0.5
        pos (250,670)#(0.5,0.5)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block: 
            easeout .5 rotate -50 pos (230,650)  
            linear .5 rotate -60 pos (220,660)
            easein 1 rotate 10 pos (250,670)
            repeat

image VibratorRightBreast: 
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

image VibratorLeftBreast: 
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
            
image VibratorPussy: 
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

image VibratorAnal: 
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
            
image VibratorPussyInsert: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0
        
image TestUIAnimation: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (270,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            ease 1 rotate 0 xpos 260 ypos 655
            pause .25
            ease 1 rotate 10 xpos 270 ypos 665           
            pause .25
            repeat

#Lesbian action animations.
image GirlGropeLeftBreast:  
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6#.7
        pos (300,400)#(300,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -20
        block: 
            ease 1 rotate -40 pos (280,390)
            ease 1 rotate -20 pos (300,400)
            repeat

image GirlGropeRightBreast:    
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (160,380) #(160,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10#-30
        block: 
            ease 1 rotate -30 pos (160,410)
            ease 1 rotate -10 pos (160,380)
            repeat

image GirlGropeThigh: 
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

image GirlGropePussy: 
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (230,615)#(220,635)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (225,620)
                ease .5 rotate 195 
                ease .75 rotate 210 
                ease .5 rotate 195 
            choice: #slow rub
                ease .5 rotate 210 pos (225,620)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (225,620)
                ease .75 rotate 200 pos (225,625)
                ease .5 rotate 205 pos (225,620)
                ease .75 rotate 200 pos (225,625)
            choice: #Fast stroke
                ease .3 rotate 205 pos (225,620)
                ease .3 rotate 200 pos (225,630)
                ease .3 rotate 205 pos (225,620)
                ease .3 rotate 200 pos (225,630)
            repeat

image GirlFingerPussy: 
    contains:
        subpixel True
        "UI_GirlFinger"       
        zoom .6
        pos (230,630)#(220,635)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (230,635)
                ease .5 rotate 195 
                ease .75 rotate 210 
                ease .5 rotate 195 
            choice: #slow rub
                ease .5 rotate 210 pos (230,635)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (230,635)
                ease .75 rotate 200 pos (230,640)
                ease .5 rotate 205 pos (230,635)
                ease .75 rotate 200 pos (230,640)
            choice: #Fast stroke
                ease .3 rotate 205 pos (230,635)
                ease .3 rotate 200 pos (230,645)
                ease .3 rotate 205 pos (230,635)
                ease .3 rotate 200 pos (230,645)
            repeat
        
# ////   Etc.   ////////////////////////////////////////////////

# Start Drip animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Spunk_Drip:  
        #the minor dripping animation
        contains:
            "images/SpermdropB.png"  
            zoom 0.3
            alpha 0
            block:
                choice:
                    pause 1
                choice:
                    pause .5
                choice:
                    pos (0,0)
                    alpha 1
                    easeout 2.5 ypos 70
                    easeout .9 ypos 350
                    alpha 0
                    pause 1
                choice:
                    pos (9,0)
                    pause .2
                    alpha 1
                    easeout 2.5 ypos 75
                    easeout .9 ypos 350
                    alpha 0
                    pause .4
                choice:
                    pos (6,0)
                    pause .4
                    alpha 1
                    easeout 2.5 ypos 65
                    easeout .9 ypos 350
                    alpha 0
                choice:
                    pos (12,0)
                    pause .8
                    alpha 1
                    easeout 2.5 ypos 60
                    easeout .9 ypos 350
                    alpha 0
                repeat
                
image Spunk_Drip2:
        #Dripping spunk
        contains:
            "images/SpermdropB.png"    
            pos (0,0)
            zoom 0.3
            parallel:
                pos (0,0)
                alpha 1
                easeout 2.5 ypos 70
                easeout .9 ypos 350
                alpha 0
                pause 1
                repeat
        contains:
            "images/SpermdropB.png"    
            pos (0,0)
            zoom 0.3
            parallel:
                pos (9,0)
                pause .2
                alpha 1
                easeout 2.5 ypos 75
                easeout .9 ypos 350
                alpha 0
                pause .4
                repeat    
        contains:
            "images/SpermdropB.png"   
            pos (0,0)
            zoom 0.3
            parallel:
                pos (6,0)
                pause .4
                alpha 1
                easeout 2.5 ypos 65
                easeout .9 ypos 350
                alpha 0
                repeat    
        contains:
            "images/SpermdropB.png"   
            pos (0,0)
            zoom 0.3
            parallel:
                pos (12,0)
                pause .8
                alpha 1
                easeout 2.5 ypos 60
                easeout .9 ypos 350
                alpha 0
                repeat
                

image Spunk_Dripp:  
        #the minor dripping animation
        contains:
            "images/SpermdropP.png"  
            zoom 0.3
            alpha 0
            block:
                choice:
                    pause 1
                choice:
                    pause .5
                choice:
                    pos (0,0)
                    alpha 1
                    easeout 2.5 ypos 70
                    easeout .9 ypos 350
                    alpha 0
                    pause 1
                choice:
                    pos (9,0)
                    pause .2
                    alpha 1
                    easeout 2.5 ypos 75
                    easeout .9 ypos 350
                    alpha 0
                    pause .4
                choice:
                    pos (6,0)
                    pause .4
                    alpha 1
                    easeout 2.5 ypos 65
                    easeout .9 ypos 350
                    alpha 0
                choice:
                    pos (12,0)
                    pause .8
                    alpha 1
                    easeout 2.5 ypos 60
                    easeout .9 ypos 350
                    alpha 0
                repeat
                
image Wet_Drip:  
        #the minor dripping animation
        contains:
            "images/Wetdrop.png"  
            zoom 0.2
            alpha 0
            block:
                choice:
                    pause 1
                choice:
                    pause .5
                choice:
                    pos (14,0)
                    alpha .8
                    easeout .9 ypos 70
                    easeout .9 ypos 350
                    alpha 0
                    pause 1
                choice:
                    pos (9,0)
                    pause .2
                    alpha .8
                    easeout .9 ypos 75
                    easeout .9 ypos 350
                    alpha 0
                    pause .4
                choice:
                    pos (6,0)
                    pause .4
                    alpha .8
                    easeout .9 ypos 65
                    easeout .9 ypos 350
                    alpha 0
                choice:
                    pos (12,0)
                    pause .8
                    alpha .8
                    easeout .9 ypos 60
                    easeout .9 ypos 350
                    alpha 0
                repeat

image Wet_Drip2:
        #The dripping wetness animation at 2x speed
        contains:
            "images/Wetdrop.png"    
            pos (0,0)
            zoom 0.2
            parallel:
                pos (14,0)
                alpha .8
                easeout .9 ypos 70
                easeout .9 ypos 350
                alpha 0
                pause 1.5
                repeat
        contains:
            "images/Wetdrop.png"    
            pos (0,0)
            zoom 0.2
            parallel:
                pos (9,0)
                pause .3
                alpha .8
                easeout .9 ypos 75
                easeout .9 ypos 350
                alpha 0
                pause .6
                repeat    
        contains:
            "images/Wetdrop.png"   
            pos (0,0)
            zoom 0.2
            parallel:
                pos (6,0)
                pause .6
                alpha .8
                easeout .9 ypos 65
                easeout .9 ypos 350
                alpha 0
                repeat    
        contains:
            "images/Wetdrop.png"   
            pos (0,0)
            zoom 0.2
            parallel:
                pos (12,0)
                pause .8
                alpha .8
                easeout .9 ypos 60
                easeout .9 ypos 350
                alpha 0
                pause .2
                repeat
# End Drip animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
            
image Zero_Chibicock:
    LiveComposite(                            #The compositived Chibi UI cock
        (225,350),             
        (0,0), ConditionSwitch(        
            "Player.Color == 'pink'", "images/Chibi_Cock_P.png",
            "Player.Color == 'brown'", "images/Chibi_Cock_B.png",             
            "Player.Color == 'green'", "images/Chibi_Cock_G.png", 
            "True", Null(),
            ),   
#        (0,0), ConditionSwitch(                 
#            "Player.Wet", "images/RogueBJFace/Zero_Cock_Wet.png", 
#            "True", Null(),
#            ),       
#        (0,0), ConditionSwitch(    
#            "Player.Spunk", "images/RogueBJFace/Zero_Cock_Spunk.png", 
#            "True", Null(),
#            ),       
        )
    anchor (0.5,0.5)


            
image Chibi_Null: 
    #The Blank Chibi-cock
    contains:
        "Zero_Chibicock"  
        anchor (0.5,0.5)
        pos (0,0)
        rotate 0 
        xzoom 1 
    pos (75,675)
    zoom 0.5
    
image Chibi_Jackin: 
    #the jackin it chibi cock
    contains:
        "Zero_Chibicock"   
        anchor (0.5,0.5)
        pos (0,0)
        rotate 0
        xzoom 1 
    contains:
        subpixel True
        "images/Chibi_Hand_M.png"   
        pos (-10,-80)
        anchor (0.5,0.5)
        rotate 20
        block:
                ease .3 rotate -10 pos (0,50)
                ease .7 rotate 20 pos (-10,-80)
                repeat
    pos (75,675)
    zoom 0.5
            
image Chibi_Handy: 
    #the girl handy chibicock
    contains:
        "Zero_Chibicock"  
        anchor (0.5,0.5)
        pos (0,0)
        rotate 0    
        xzoom 1 
    contains:
        subpixel True
        "images/Chibi_Hand_G.png"   
        pos (0,-110)
        anchor (0.5,0.5)
        rotate -10
        block:
                ease .3 rotate 0 pos (10,10)
                ease .7 rotate -10 pos (0,-130)
                repeat
    pos (75,675)
    zoom 0.5

image Chibi_Mouth_Mask:
    "images/Chibi_Mouth_Mask.png"
    anchor (0.5,0.5)
   
image Chibi_Mouth_Emma:
    "images/Chibi_Mouth_E.png"
    anchor (0.5,0.5)
image Chibi_Mouth_Rogue:
    "images/Chibi_Mouth_R.png"
    anchor (0.5,0.5)
image Chibi_Mouth_Kitty:
    "images/Chibi_Mouth_K.png"
    anchor (0.5,0.5)

image Chibi_Sucking:
    # The core sucking image
    contains:
        "Chibi_SuckingB" 
    pos (75,675)
    
image Chibi_SuckingB:
    #The composited Chibi UI cock
    LiveComposite(
        (225,350),             
        (0,0), ConditionSwitch(        
            "Partner == RogueX", "Chibi_Mouth_Rogue",
            "Partner == EmmaX", "Chibi_Mouth_Emma",
            "True", "Chibi_Mouth_Kitty"
            ),   
        (0,0), AlphaMask("Chibi_Sucking_Cock", "Chibi_Mouth_Mask") 
        )      
    subpixel True
    pos (7,0) #top
    anchor (0.5,0.5)
    zoom 0.5
    xzoom 0.71
    block:
        easeout .25 rotate 0 pos (2,48) xzoom 1 #middle
        easein .25 rotate 0 pos (6,92) xzoom 1 #bottom
        easeout .5 rotate 0 pos (2,48) xzoom 1 #middle
        easein .5 rotate 0 pos (5,0) xzoom 0.71 #top
        repeat

image Chibi_Sucking_Cock:
    #The animation for the cock used in the sucking cock animation
    contains:
        subpixel True
        "Zero_Chibicock"     
        pos (100,175) #top
        xzoom 1.5
        anchor (0.5,0.5)
#        alpha 0.5
        rotate 0
        block:
            easeout .25 rotate 0 pos (110,80) xzoom 1 #middle
            easein .25 rotate 0 pos (100,-10) xzoom 1 #bottom
            easeout .5 rotate 0 pos (110,80) xzoom 1 #middle
            easein .5 rotate 0 pos (100,175) xzoom 1.5 #top
            repeat


#>>>>>>>>>>

image Chibi_UI:
    # The basic chibi-UI image that is called 
    contains:
        ConditionSwitch(    
            "'cockout' not in Player.RecentActions", Null(),
            "Trigger2 == 'jackin'", "Chibi_Jackin",
            "Trigger3 == 'hand' or Trigger4 == 'hand'", "Chibi_Handy",             
            "Trigger4 == 'blow'", "Chibi_Sucking", 
            "True", "Chibi_Null", 
            )
#    anchor (0.5,0.5)
#    pos (75,675)

label Rogue_Kissing_Launch(T = Trigger):    
    call Rogue_Hide
    $ Trigger = T
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer
    show Rogue_Sprite at SpriteLoc(StageCenter) zorder RogueX.Layer:
        ease 0.5 offset (0,0) zoom 2 alpha 1
    return

label Rogue_Kissing_Smooch:   
    $ RogueX.FaceChange("kiss")  
    show Rogue_Sprite at SpriteLoc(StageCenter) zorder RogueX.Layer:
            offset (0,0) 
            alpha 1
            ease 0.5 xpos StageCenter zoom 2
            pause 1
            ease 0.5 xpos RogueX.SpriteLoc zoom 1 
    pause 1
    $ RogueX.FaceChange("sexy")  
    return
    
label Rogue_Breasts_Launch(T = Trigger):    
    call Rogue_Hide
    $ Trigger = T
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
            ease 0.5 pos (700,-50) zoom 2 offset (0,0) alpha 1 
    return
        
label Rogue_Pussy_Launch(T = Trigger):
    call Rogue_Hide    
    $ Trigger = T
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
        ease 0.5 pos (700,-400) zoom 2 offset (0,0) alpha 1
    return
        
label Rogue_Pos_Reset(Pose = 0):  
    if RogueX.Loc != bg_current:
            return   
    call Rogue_Hide 
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
            ease .5 offset (0,0) anchor (0.6, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
    show Rogue_Sprite zorder RogueX.Layer:
            offset (0,0) 
            anchor (0.6, 0.0)
            zoom 1  
            xzoom 1 
            yzoom 1
            alpha 1
            pos (RogueX.SpriteLoc,50)
    $ Trigger = Pose
    return
    
label Rogue_Hide(Sprite=0):
    if renpy.showing("Rogue_Doggy_Animation"):
        call Rogue_Doggy_Reset
    hide Rogue_Doggy_Animation       
    hide Rogue_HJ_Animation
    hide Rogue_BJ_Animation
    hide Rogue_TJ_Animation 
    if Sprite:
            hide Rogue_Sprite         
    return
    
image Cellphone:
    "images/Cellphone.png"
    xoffset 0 #-250
    yoffset 100


image PhoneSex:
    #this is the phone displayed during phone sex
    contains:
        #base
        "images/PhoneFrame.png"
    contains:
        #screen        
        AlphaMask("PhoneScreen", "images/PhoneMask.png")
    offset (300,50)

image PhoneRG:
    #Rogue's room for the phone (to make sure the bed is framed properly)
    "bg_rogue"
    xoffset 500
    
image PhoneScreen:
    #this is the screen displayed on "PhoneSex", alpha-masked
    contains:
        #backdrop
        ConditionSwitch(      
            "Ch_Focus.Loc == 'bg rogue'","PhoneRG",
            "Ch_Focus.Loc == 'bg kitty'", "bg_kitty",
            "Ch_Focus.Loc == 'bg laura'", "bg_laura",
            "Ch_Focus.Loc == 'bg emma'", "bg_emma",
            "Ch_Focus.Loc == 'bg classroom'", "bg_class",
            "Ch_Focus.Loc == 'bg teacher'", "bg_class",
            "True", "bg_shower", 
            ) 
        offset (-800,-300)
        zoom 1.5
    contains:
        #girl
        ConditionSwitch(
            "Ch_Focus.Tag == 'Rogue'", "Rogue_Sprite",
            "Ch_Focus.Tag == 'Kitty'", "Kitty_Sprite",
            "Ch_Focus.Tag == 'Emma'", "Emma_Sprite",
            "Ch_Focus.Tag == 'Laura'", "Laura_Sprite",
            "True", Null(),        
            ) 
        pos (0,0)
        offset (290,50)
        anchor (0.6,0)
        zoom 1.1


image DressScreen:
    #this is dressing screen displayed during wardrobe
    contains:
        #base
        "images/DressScreen.png"
    contains:
        #screen        
        AlphaMask("images/DressScreenShadow.png","DressShadow")
    zoom 1
    offset (375,225)
    
image DressShadow:
    #this is the shadow projected on that screen
    contains:
        #girl
        ConditionSwitch(
            "RogueX.Layer == 100", "Rogue_Sprite",
            "KittyX.Layer == 100", "Kitty_Sprite",
            "EmmaX.Layer == 100", "Emma_Sprite",
            "LauraX.Layer == 100", "Laura_Sprite",
#            "Ch_Focus == RogueX", "Rogue_Sprite",
#            "Ch_Focus == 'Kitty'", "Kitty_Sprite",
#            "Ch_Focus == 'Emma'", "Emma_Sprite",
#            "Ch_Focus == 'Laura'", "Laura_Sprite",
            "True", Null(),        
            ) 
        offset (210,-170)
        zoom 1

    
## Xavier Faces ///////////////////////////////

label XavierFace (Face = X_Emote):
        if Face == "psychic":
                $ X_Mouth = "concentrate"
                $ X_Brows = "concentrate"
                $ X_Eyes = "concentrate"
                $ X_Psychic = 1
        if Face == "hypno":
                $ X_Mouth = "neutral"
                $ X_Brows = "neutral"
                $ X_Eyes = "hypno"
        if Face == "shocked":
                $ X_Mouth = "neutral"
                $ X_Brows = "shocked"
                $ X_Eyes = "shocked"
                $ X_Psychic = 0
        if Face == "happy":
                $ X_Mouth = "happy"
                $ X_Brows = "happy"
                $ X_Eyes = "happy"        
                $ X_Psychic = 0
        if Face == "angry":
                $ X_Mouth = "concentrate"
                $ X_Brows = "concentrate"
                $ X_Eyes = "happy"
                $ X_Psychic = 0
        return
        
# Gwenpool sprites Start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /        
image Gwen_Sprite:
    LiveComposite(        
        (574,964),
        #body
        (0,0), "images/GS_B.png",
#        (0,0), "images/GS_H.png",
        #Head
        (80,15), "Gwen_Sprite_Head",       
        )           
    anchor (0.6, 0.0)                
    yoffset 15
    zoom .75                
        
        
        
image Gwen_Sprite_Head:            
    LiveComposite(
        (820,820),         
        (0,0), ConditionSwitch(
                # Face background plate
                "G_Blush", "images/NPC/Gwen_Sprite_Head_Blush.png",  
                "True", "images/NPC/Gwen_Sprite_Head.png",                        
                ),        
        (0,0), ConditionSwitch(#Mouths 
            "G_Mouth == 'open'", "images/NPC/Gwen_Sprite_Mouth_Open.png",          
            "G_Mouth == 'kiss'", "images/NPC/Gwen_Sprite_Mouth_Kiss.png",
            "G_Mouth == 'smile'", "images/NPC/Gwen_Sprite_Mouth_Smile.png",
            "G_Mouth == 'shocked'", "images/NPC/Gwen_Sprite_Mouth_Shocked.png",    
            "True", "images/NPC/Gwen_Sprite_Mouth_Smile.png",
            ),                                                               
        (0,0), ConditionSwitch(                                                                       
            #brows
            "G_Blush", ConditionSwitch(
                    "G_Brows == 'angry' or G_Eyes == 'angry'", "images/NPC/Gwen_Sprite_Brows_Angry_B.png",
                    "G_Brows == 'sad'", "images/NPC/Gwen_Sprite_Brows_Sad_B.png",
                    "True", "images/NPC/Gwen_Sprite_Brows_Normal.png",
                    ),
            "True", ConditionSwitch(
                    "G_Brows == 'angry' or G_Eyes == 'angry'", "images/NPC/Gwen_Sprite_Brows_Angry.png",
                    "G_Brows == 'sad'", "images/NPC/Gwen_Sprite_Brows_Sad.png",
                    "True", "images/NPC/Gwen_Sprite_Brows_Normal.png",
                    ),
            ),        
        (0,0), "Gwen Blink",     #Eyes        
        )                
    anchor (0.6, 0.0)                
    zoom .5  

image Gwen Blink:            
    ConditionSwitch(
    "G_Eyes == 'angry'", "images/NPC/Gwen_Sprite_Eyes_Angry.png",
    "G_Eyes == 'surprised'", "images/NPC/Gwen_Sprite_Eyes_Surprised.png",
    "G_Eyes == 'closed'", "images/NPC/Gwen_Sprite_Eyes_Closed.png",
    "True", "images/NPC/Gwen_Sprite_Eyes_Normal.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/NPC/Gwen_Sprite_Eyes_Closed.png"
    .20
    repeat       
    
default G_Mouth = "normal"
default G_Brows = "normal"
default G_Eyes = "normal"
default G_Blush = 0

label GwenFace(Emote = "normal", B = G_Blush, M = 0, Mouth = 0, Eyes = 0, Brows = 0):
        # Emote is the chosen emote, B is the lush state
        # M is whether the character is in a  manic state     
        $ B = G_Blush if B == 5 else B
        
        if Emote == "normal":
                $ G_Mouth = "normal"
                $ G_Brows = "normal"
                $ G_Eyes = "normal"
        elif Emote == "angry":
                $ G_Mouth = "kiss"
                $ G_Brows = "angry"
                $ G_Eyes = "angry"
        elif Emote == "closed":
                $ G_Mouth = "normal"
                $ G_Brows = "sad"
                $ G_Eyes = "closed"  
        elif Emote == "sad":
                $ G_Mouth = "kiss"
                $ G_Brows = "sad"
                $ G_Eyes = "normal"
        elif Emote == "smile":
                $ G_Mouth = "smile"             
                $ G_Brows = "normal"
                $ G_Eyes = "normal"
        elif Emote == "surprised":
                $ G_Mouth = "open"
                $ G_Brows = "normal"
                $ G_Eyes = "surprised"
        elif Emote == "shocked":
                $ G_Mouth = "shocked"
                $ G_Brows = "normal"
                $ G_Eyes = "surprised"
                 
        if B > 1:
                $ G_Blush = 2
        elif B:
                $ G_Blush = 1
        else:
                $ G_Blush = 0
        
        if Mouth:
                $ G_Mouth = Mouth
        if Eyes:
                $ G_Eyes = Eyes
        if Brows:
                $ G_Brows = Brows
        
        return

label Gwen_FaceEditor:
            while True:
                menu: 
                    "Brows=[G_Brows], Eyes=[G_Eyes], Mouth=[G_Mouth]"
                    "Toggle Brows":
                            if G_Brows == "normal":
                                $ G_Brows = "angry"
                            elif G_Brows == "angry":
                                $ G_Brows = "confused"
                            elif G_Brows == "confused":
                                $ G_Brows = "sad"
                            elif G_Brows == "sad":
                                $ G_Brows = "surprised"
                            else:
                                $ G_Brows = "normal"
                    "Toggle Eyes Emotions":
                            if G_Eyes == "normal":                          
                                $ G_Eyes = "surprised"
                            elif G_Eyes == "surprised":
                                $ G_Eyes = "sexy"
                            elif G_Eyes == "sexy":
                                $ G_Eyes = "squint"
                            elif G_Eyes == "squint":
                                $ G_Eyes = "closed"
                            else:
                                $ G_Eyes = "normal"
                    "Toggle Eyes Directions":
                            if G_Eyes == "normal":
                                $ G_Eyes = "side"
                            elif G_Eyes == "side":
                                $ G_Eyes = "down"
                            elif G_Eyes == "down":
                                $ G_Eyes = "leftside"
                            elif G_Eyes == "leftside":
                                $ G_Eyes = "stunned"
                            else:
                                $ G_Eyes = "normal"  
                    "Toggle Mouth Normal":
                            if G_Mouth  == "normal":
                                $ G_Mouth = "sad"
                            elif G_Mouth == "sad":
                                $ G_Mouth = "smile"
                            elif G_Mouth == "smile":
                                $ G_Mouth = "surprised"
                            else:
                                $ G_Mouth = "normal"  
                    "Toggle Mouth Sexy":
                            if G_Mouth  == "normal":
                                $ G_Mouth = "kiss"
                            elif G_Mouth == "kiss":
                                $ G_Mouth = "sucking"
                            elif G_Mouth == "sucking":
                                $ G_Mouth = "tongue"
                            elif G_Mouth == "tongue":
                                $ G_Mouth = "lipbite"
                            else:
                                $ G_Mouth = "normal"  
                    "Toggle Blush":
                        if G_Blush == 1:
                            $ G_Blush = 2
                        elif G_Blush:
                            $ G_Blush = 0
                        else:
                            $ G_Blush = 1
                            
                    "Back":
                            return
#image Gwen_Sprite_Head:            
#    LiveComposite(
#        (806,806),         
#        (0,0), ConditionSwitch(
#                # Face background plate
#                "L_Blush == 2", "images/LauraSprite/Laura_Sprite_Head_Blush2.png", 
#                "L_Blush", "images/LauraSprite/Laura_Sprite_Head_Blush.png",  
#                "True", "images/LauraSprite/Laura_Sprite_Head.png",                        
#                ), 
#        )                
#    anchor (0.6, 0.0)                
#    zoom .5   


label Display_Gwen(DLoc = 350, YLoc=50):
   # If Dress, then check whether the character is underdressed when displaying her
   
    #Display Gwen    
    show Gwen_Sprite:
            alpha 1
            zoom 1
            offset (0,0)
            anchor (0.5, 0.0)  
            easeout .5 pos (DLoc,YLoc)    
    show Gwen_Sprite:
            alpha 1
            zoom 1
            offset (0,0)
            anchor (0.5, 0.0)  
            pos (DLoc,YLoc)  
    return


label Close_Launch(GirlA=0,GirlB=0,XLoc=0,YLoc=0,XZoom=0):  
    # Launches the girls close to player
    # Girl is the lead, Partner is the other girl
    # the Loc and Zoom values are generated based on which is which  
    if GirlB:
        $ BO = [GirlA,GirlB] 
    elif GirlA:
        $ BO = [GirlA]         
    while BO:         
            if BO[0] == KittyX or BO[0] == LauraX:
                $ BO[0].ArmPose = 1 
            else:                                
                $ BO[0].ArmPose = 2   
            $ YLoc = 100                             
            if GirlA == BO[0]:
                    #If this girl is lead
                    if BO[0] == KittyX:          
                        $ XLoc = 450
                    elif BO[0] == RogueX:
                        $ XLoc = 550
                    else:
                        $ XLoc = 500 
                    $ BO[0].Layer = 100
                    $ XZoom = -1.3
            elif GirlB == BO[0]:
                    #If the other girl is lead
                    if BO[0] == EmmaX or LauraX:
                        $ XLoc = 700
                    else:
                        $ XLoc = 715
                    $ BO[0].Layer = 75
                    $ XZoom = 1.3 
                    
            if BO[0] == RogueX:   
                    call Rogue_Hide  
                    show Rogue_Sprite at SpriteLoc(XLoc,YLoc) zorder RogueX.Layer:
                            alpha 1
                            zoom 1
                            xzoom XZoom
                            yzoom 1.3
                            offset (0,0)
                            anchor (0.6, 0.0)
            elif BO[0] == KittyX: 
                    call Kitty_Hide  
                    show Kitty_Sprite at SpriteLoc(XLoc,YLoc) zorder KittyX.Layer:
                            alpha 1
                            zoom 1
                            xzoom XZoom
                            yzoom 1.3
                            offset (0,0)
                            anchor (0.5, 0.0)
            elif BO[0] == EmmaX: 
                    call Emma_Hide  
                    show Emma_Sprite at SpriteLoc(XLoc,YLoc) zorder EmmaX.Layer:
                            alpha 1
                            zoom 1
                            xzoom XZoom
                            yzoom 1.3
                            offset (0,0)
                            anchor (0.5, 0.0)
            elif BO[0] == LauraX: 
                    call Laura_Hide  
                    show Laura_Sprite at SpriteLoc(XLoc,YLoc) zorder LauraX.Layer:
                            alpha 1
                            zoom 1
                            xzoom XZoom
                            yzoom 1.3
                            offset (0,0)
                            anchor (0.5, 0.0)
            $ BO.remove(BO[0])
    return
    
label QuickReset(Girl=0):
    if RogueX == Girl:
                call Rogue_Pos_Reset
    if KittyX == Girl:
                call Kitty_Pos_Reset
    if EmmaX == Girl:
                call Emma_Pos_Reset
    if LauraX == Girl:
                call Laura_Pos_Reset
    return
    
label Les_Launch(Girl=0,XLoc=0,YLoc=0,XZoom=0,BO=[]):  
    # Launches the lesbian sex positions
    # Girl is the lead, Partner is the other girl
    # the Loc and Zoom values are generated based on which is which
    if Partner not in TotalGirls:
            return
    $ BO = [Girl,Partner] 
    while BO:  
            if "unseen" in BO[0].RecentActions:                
                        $ BO[0].Eyes = "closed"
            elif Girl == BO[0]:
                if Girl == RogueX:
                        $ BO[0].Eyes = "side"
                elif Girl == EmmaX:
                        $ BO[0].Eyes = "sly"
                else:
                        $ BO[0].Eyes = "leftside"                
            else:
                        $ BO[0].Eyes = "side"
                        
            if BO[0] == KittyX or BO[0] == LauraX:
                $ BO[0].ArmPose = 1 
            else:                                
                $ BO[0].ArmPose = 2   
            $ YLoc = 100                             
            if Girl == BO[0]:
                    #If this girl is lead
                    if BO[0] == KittyX:          
                        $ XLoc = 450
                    elif BO[0] == RogueX:
                        $ XLoc = 550
                    else:
                        $ XLoc = 500 
                    $ BO[0].Layer = 100
                    $ XZoom = -1.3
            else: #Partner == BO[0]:
                    #If the other girl is lead
                    if BO[0] == EmmaX or LauraX:
                        $ XLoc = 700
                    else:
                        $ XLoc = 715
                    if BO[0] == KittyX: 
                            if RogueX in (Partner,Girl):
                                    $ KittyX.Layer = 100
                            else:
                                    $ KittyX.Layer = 25
                    else:
                                    $ BO[0].Layer = 75
                    $ XZoom = 1.3 
                    
            if BO[0] == RogueX:   
                    call Rogue_Hide  
                    show Rogue_Sprite at SpriteLoc(XLoc,YLoc) zorder RogueX.Layer:
                            alpha 1
                            zoom 1
                            xzoom XZoom
                            yzoom 1.3
                            offset (0,0)
                            anchor (0.6, 0.0)
            elif BO[0] == KittyX: 
                    call Kitty_Hide  
                    show Kitty_Sprite at SpriteLoc(XLoc,YLoc) zorder KittyX.Layer:
                            alpha 1
                            zoom 1
                            xzoom XZoom
                            yzoom 1.3
                            offset (0,0)
                            anchor (0.5, 0.0)
            elif BO[0] == EmmaX: 
                    call Emma_Hide  
                    show Emma_Sprite at SpriteLoc(XLoc,YLoc) zorder EmmaX.Layer:
                            alpha 1
                            zoom 1
                            xzoom XZoom
                            yzoom 1.3
                            offset (0,0)
                            anchor (0.5, 0.0)
            elif BO[0] == LauraX: 
                    call Laura_Hide  
                    show Laura_Sprite at SpriteLoc(XLoc,YLoc) zorder LauraX.Layer:
                            alpha 1
                            zoom 1
                            xzoom XZoom
                            yzoom 1.3
                            offset (0,0)
                            anchor (0.5, 0.0)
            $ BO.remove(BO[0])
    return
    
image CircleTest: 
    contains:
        subpixel True
        "images/Clockbase.png"   
        anchor (0.5,0.5)
#        rotate 180
        yzoom -1
        
    contains:
         ConditionSwitch(
            "Round>= 50", "ClockWhite", 
            "True",Null(),
            ),  
    contains:
         ConditionSwitch(
            "Round<= 50", "ClockRed", 
            "True",Null(),
            ),  
    contains:
        subpixel True
        "images/Clockface.png" 
        anchor (0.5,0.5) 
    
image ClockWhite:
    contains:
        subpixel True
        "images/Clockwhite.png"  
        anchor (0.5,0.5)
        rotate -(int(Round *3.6))
    
image ClockRed:
    contains:
        subpixel True
        "images/Clockred.png"  
        anchor (0.5,0.5)
        rotate -(int(Round *3.6-180))
            
image BlueScreen:
    #used by Historia
    alpha .1
    contains:
        Solid("#00B3D6", xysize=(1024, 768))  