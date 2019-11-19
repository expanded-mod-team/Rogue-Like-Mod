# Basic character Sprites
image Rogue:
    LiveComposite(
        (480,960),
#        (0,0), ConditionSwitch(                                                                         
#            #Overhsirt backing
#            "R_Over == 'mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_mesh1.png",
#            "R_Over == 'mesh top' and Rogue_Arms == 2", "images/RogueSprite/Rogue_under_mesh2.png", 
#            "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty1.png",
#            "R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodieB.png",
#            "True", Null(), 
#            ), 
        
        (0,0), ConditionSwitch(                                                                         
            #back of hair
            "renpy.showing('Rogue_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Rogue_TJ_Animation')", Null(),
            "R_Hair == 'evo' and R_Water", Null(),
            "R_Hair == 'evo'", "images/RogueSprite/Rogue_hair_evo_back.png",
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                         
            #shirt layer           
            "not R_Over", Null(),    
            "R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodieB.png",         
            "R_Uptop", ConditionSwitch( 
                    #if the top's down. . .
                    "Rogue_Arms == 1", ConditionSwitch( 
                            #if the arms are down. . .
                            "R_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh1_Up.png",           
#                            "R_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink1_Up.png",
#                            "R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie1_Up.png",
                            "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty_Up.png",
#                            "R_Over == 'towel'", Null(), 
                            "True", Null(),     
                            ),  
                    "True", ConditionSwitch( 
                            #if the arms are up. . .
                            "R_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh2_Up.png", 
#                            "R_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink2_Up.png",
#                            "R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie2_Up.png",
                            "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty_Up.png",
#                            "R_Over == 'towel'", Null(),       
                            "True", Null(),     
                            ),       
                    ),            
            "True", ConditionSwitch(
                    #if the top's up. . .
                    "Rogue_Arms == 1", ConditionSwitch( 
                            #if the arms are down. . .
                            "R_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh1.png",           
#                            "R_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink1.png",
#                            "R_Over == 'towel'", "images/RogueSprite/Rogue_over_towel1.png",
                            "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty1.png",
#                            "R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie1.png",
                            "True", Null(),     
                            ),  
                    "True", ConditionSwitch( 
                            #if the arms are up. . .
                            "R_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh2.png", 
#                            "R_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink2.png",
#                            "R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie2.png",
                            "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty2.png",
#                            "R_Over == 'towel'", "images/RogueSprite/Rogue_over_towel2.png",      
                            "True", Null(),     
                            ),       
                    ),       
            ),
        (0,0), ConditionSwitch(                                                                         
            #body 
            "R_Pubes and R_Pierce == 'ring'", "images/RogueSprite/Rogue_bodyhaired_ring.png",
            "R_Pubes and R_Pierce == 'barbell'", "images/RogueSprite/Rogue_bodyhaired_barbell.png",
            "R_Pierce == 'ring'", "images/RogueSprite/Rogue_body_ring.png",            
            "R_Pierce == 'barbell'", "images/RogueSprite/Rogue_body_barbell.png",
            "R_Pubes", "images/RogueSprite/Rogue_bodyhaired_bare.png",   
            "True", "images/RogueSprite/Rogue_body_bare.png",         
            ),              
        (0,0), ConditionSwitch(                                                                         
            #head 
            "renpy.showing('Rogue_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Rogue_TJ_Animation')", Null(),
#            "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_head_evowet.png",
            "R_Hair == 'evo' and R_Blush == 2", "images/RogueSprite/Rogue_head_evo_blush2.png",
            "R_Hair == 'evo' and R_Blush", "images/RogueSprite/Rogue_head_evo_blush.png",
            "R_Hair == 'evo'", "images/RogueSprite/Rogue_head_evo.png",
            "True", "images/RogueSprite/Rogue_head_evo.png",
            ),  
        (0,0), ConditionSwitch(                                                                         
            #pants backing/hose    
            "R_Hose == 'stockings'", "images/RogueSprite/Rogue_hose.png",     
            "R_Legs == 'pants' and R_Upskirt", "images/RogueSprite/Rogue_pantsback.png", 
            "True", Null(), 
            ),
#        (0,0), ConditionSwitch(                                                                         
#            #Panties            
#            "not R_Panties", Null(),
#            "R_Legs == 'pants' and not R_Upskirt", "images/RogueSprite/Rogue_panties.png",             
#            "R_Panties == 'shorts' and R_PantiesDown and R_Wet > 1", "images/RogueSprite/Rogue_shorts_down_wet.png",
#            "R_Panties == 'shorts' and R_PantiesDown", "images/RogueSprite/Rogue_shorts_down.png",  
#            "R_Panties == 'shorts' and R_Wet > 1", "images/RogueSprite/Rogue_shorts_wet.png",          
#            "R_Panties == 'shorts'", "images/RogueSprite/Rogue_shorts.png",
#            "R_Panties == 'green panties' and R_PantiesDown and R_Wet > 1", "images/RogueSprite/Rogue_undies_down_wet.png",
#            "R_Panties == 'green panties' and R_PantiesDown", "images/RogueSprite/Rogue_undies_down.png",  
#            "R_Panties == 'green panties' and R_Wet > 1", "images/RogueSprite/Rogue_undies_wet.png",          
#            "R_Panties == 'green panties'", "images/RogueSprite/Rogue_undies.png",
#            "R_Panties and R_PantiesDown", "images/RogueSprite/Rogue_panties_down.png",      
#            "R_Panties == 'lace panties'", "images/RogueSprite/Rogue_lacepanties.png",         
#            "True", "images/RogueSprite/Rogue_panties.png",            
#            ),       
        (0,0), ConditionSwitch(                                                                         
            #panties           
            "not R_Panties", Null(),     
            "R_Legs == 'pants' and not R_Upskirt", "images/RogueSprite/Rogue_panties.png",          
            "R_PantiesDown", ConditionSwitch( 
                    #if the panties's down. . .
                    "R_Wet > 1", ConditionSwitch( 
                            #if the panties's are wet. . .
                            "R_Panties == 'shorts'", "images/RogueSprite/Rogue_shorts_down_wet.png",
                            "R_Panties == 'green panties'", "images/RogueSprite/Rogue_undies_down_wet.png",
                            "R_Panties == 'bikini bottoms'", "images/RogueSprite/Rogue_panties_bikini_down.png",  
                            "True", "images/RogueSprite/Rogue_panties_down.png", 
                            ),    
                    "True", ConditionSwitch( 
                            #if the panties's are not wet. . .
                            "R_Panties == 'shorts'", "images/RogueSprite/Rogue_shorts_down.png",  
                            "R_Panties == 'green panties'", "images/RogueSprite/Rogue_undies_down.png",  
                            "R_Panties == 'bikini bottoms'", "images/RogueSprite/Rogue_panties_bikini_down.png",  
                            "True", "images/RogueSprite/Rogue_panties_down.png",     
                            ),     
                    ),            
            "True", ConditionSwitch(
                    #if the panties's up. . .
                    "R_Wet > 1", ConditionSwitch( 
                            #if the panties's are wet. . .
                            "R_Panties == 'shorts' and R_Wet > 1", "images/RogueSprite/Rogue_shorts_wet.png",     
                            "R_Panties == 'green panties' and R_Wet > 1", "images/RogueSprite/Rogue_undies_wet.png",     
                            "R_Panties == 'lace panties'", "images/RogueSprite/Rogue_lacepanties.png",    
                            "R_Panties == 'bikini bottoms'", "images/RogueSprite/Rogue_panties_bikini.png",       
                            "True", "images/RogueSprite/Rogue_panties.png",     
                            ),    
                    "True", ConditionSwitch( 
                            #if the panties's are not wet. . .     
                            "R_Panties == 'shorts'", "images/RogueSprite/Rogue_shorts.png",       
                            "R_Panties == 'green panties'", "images/RogueSprite/Rogue_undies.png",   
                            "R_Panties == 'lace panties'", "images/RogueSprite/Rogue_lacepanties.png",   
                            "R_Panties == 'bikini bottoms'", "images/RogueSprite/Rogue_panties_bikini.png",       
                            "True", "images/RogueSprite/Rogue_panties.png",         
                            ),    
                    ),       
            ),
        (0,0), ConditionSwitch(                                                                         
            #full hose/tights              
            "R_Panties and R_PantiesDown", Null(), 
            "R_Hose == 'stockings and garterbelt'", "images/RogueSprite/Rogue_hose_garter.png",  
            "R_Hose == 'garterbelt'", "images/RogueSprite/Rogue_garters.png",                 
            "R_Hose == 'pantyhose'", "images/RogueSprite/Rogue_hosefull.png",       
            "R_Hose == 'tights' and R_Wet", "images/RogueSprite/Rogue_tights_wet.png",
            "R_Hose == 'tights'", "images/RogueSprite/Rogue_tights.png",
            "R_Hose == 'ripped pantyhose'", "images/RogueSprite/Rogue_hose_holed.png", 
            "R_Hose == 'ripped tights'", "images/RogueSprite/Rogue_tights_holed.png",   
            "True", Null(), 
            ),
        (240,560), ConditionSwitch(                                                                         
            #Personal Wetness            
            "not R_Wet", Null(),
            "R_Legs == 'pants' and not R_Upskirt", Null(),   
            "R_Panties and not R_PantiesDown and R_Wet <= 1", Null(),                   
            "R_Wet == 1", ConditionSwitch( #Wet = 1
                    "R_Panties and R_PantiesDown", AlphaMask("Wet_Drip","Rogue_Drip_MaskP"),  
                    "R_Legs == 'pants'", AlphaMask("Wet_Drip","Rogue_Drip_MaskPn"),
                    "True", AlphaMask("Wet_Drip","Rogue_Drip_Mask"), #only plays if nothing is in the way
                    ),
            "True", ConditionSwitch( #Wet = 2+
                    "R_Panties and R_PantiesDown", AlphaMask("Wet_Drip2","Rogue_Drip_MaskP"), #"Wet_Drip2",# 
                    "R_Panties and R_Legs == 'pants'", AlphaMask("Wet_Drip","Rogue_Drip_MaskPn"), #"Wet_Drip2",# 
                    "R_Legs == 'pants'", AlphaMask("Wet_Drip2","Rogue_Drip_MaskPn"),
                    "R_Panties", AlphaMask("Wet_Drip","Rogue_Drip_Mask"), #"Wet_Drip2",# 
                    "True", AlphaMask("Wet_Drip2","Rogue_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (0,0), ConditionSwitch(                                                                         
            #Personal Wetness            
            "not R_Wet", Null(),
            "R_Legs and R_Wet <= 1", Null(),
            "R_Legs", "images/RogueSprite/Rogue_wet.png",
            "R_Wet == 1", "images/RogueSprite/Rogue_wet.png",
            "True", "images/RogueSprite/Rogue_wet2.png",       #R_Wet >1
            ),  
        (240,560), ConditionSwitch(                                                                         
            #Spunk nethers        
            "'in' not in R_Spunk and 'anal' not in R_Spunk", Null(),
            "R_Legs == 'pants' and not R_Upskirt", Null(),   
            "True", ConditionSwitch( #Wet = 2+
                    "R_Panties and R_PantiesDown", AlphaMask("Spunk_Drip2","Rogue_Drip_MaskP"), #"Wet_Drip2",# 
                    "R_Panties and R_Legs == 'pants'", AlphaMask("Spunk_Drip","Rogue_Drip_MaskPn"), #"Wet_Drip2",# 
                    "R_Legs == 'pants'", AlphaMask("Spunk_Drip2","Rogue_Drip_MaskPn"),
                    "True", AlphaMask("Spunk_Drip2","Rogue_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),   
#        (0,0), ConditionSwitch(                                                                         
#            #Spunk Nethers over          
#            "'in' not in R_Spunk and 'anal' not in R_Spunk", Null(),
#            "R_Legs == 'pants' and not R_Upskirt", Null(),   
#            "R_Panties and not R_PantiesDown", Null(),     
#            "True", "images/RogueSprite/Rogue_wet2.png",       #R_Wet >1
#            ),           
        (0,0), ConditionSwitch(                                                                         
            #brows
            "R_Brows == 'normal' and R_Blush == 2", "images/RogueSprite/Rogue_brows_normal_b.png",
            "R_Brows == 'angry' and R_Blush == 2", "images/RogueSprite/Rogue_brows_angry_b.png",
            "R_Brows == 'sad' and R_Blush == 2", "images/RogueSprite/Rogue_brows_sad_b.png",
            "R_Brows == 'surprised' and R_Blush == 2", "images/RogueSprite/Rogue_brows_surprised_b.png",        
            "R_Brows == 'confused' and R_Blush == 2", "images/RogueSprite/Rogue_brows_confused_b.png",
            "R_Brows == 'normal'", "images/RogueSprite/Rogue_brows_normal.png",
            "R_Brows == 'angry'", "images/RogueSprite/Rogue_brows_angry.png",
            "R_Brows == 'sad'", "images/RogueSprite/Rogue_brows_sad.png",
            "R_Brows == 'surprised'", "images/RogueSprite/Rogue_brows_surprised.png",        
            "R_Brows == 'confused'", "images/RogueSprite/Rogue_brows_confused.png",
            "True", "images/RogueSprite/Rogue_brows_normal.png",
            ),
#        (0,0), ConditionSwitch(                                                                         
#            #Blush
#            "R_Blush", "images/RogueSprite/Rogue_blush.png",
#            "True", Null(), 
#            ),
        (0,0), ConditionSwitch(                                                                         
            #Mouths        
            "'mouth' in R_Spunk and R_Mouth == 'sucking'", "images/RogueSprite/Rogue_mouth_sucking_w.png",
            "'mouth' in R_Spunk and R_Mouth == 'surprised'", "images/RogueSprite/Rogue_mouth_sucking_w.png",
            "'mouth' in R_Spunk and R_Mouth == 'sad'", "images/RogueSprite/Rogue_mouth_sad_w.png",
            "'mouth' in R_Spunk and R_Mouth == 'kiss'", "images/RogueSprite/Rogue_mouth_sad_w.png",
            "'mouth' in R_Spunk and R_Mouth == 'smile'", "images/RogueSprite/Rogue_mouth_smile_w.png",
            "'mouth' in R_Spunk and R_Mouth == 'tongue'", "images/RogueSprite/Rogue_mouth_tongue_w.png",
            "'mouth' in R_Spunk", "images/RogueSprite/Rogue_mouth_lipbite_w.png",
            "R_Mouth == 'normal'", "images/RogueSprite/Rogue_mouth_normal.png",
            "R_Mouth == 'lipbite'", "images/RogueSprite/Rogue_mouth_lipbite.png",
            "R_Mouth == 'sucking'", "images/RogueSprite/Rogue_mouth_sucking.png",            
            "R_Mouth == 'kiss'", "images/RogueSprite/Rogue_mouth_kiss.png",
            "R_Mouth == 'sad'", "images/RogueSprite/Rogue_mouth_sad.png",
            "R_Mouth == 'smile'", "images/RogueSprite/Rogue_mouth_smile.png",
            "R_Mouth == 'surprised'", "images/RogueSprite/Rogue_mouth_surprised.png",            
            "R_Mouth == 'tongue'", "images/RogueSprite/Rogue_mouth_tongue.png",                
            "R_Mouth == 'grimace'", "images/RogueSprite/Rogue_mouth_grimace.png",           
            "True", "images/RogueSprite/Rogue_mouth_normal.png",
            ),            
        (0,0), "Rogue Blink",                                                                           
            #Eyes
            
        (0,0), ConditionSwitch(                                                                         
            #Pants and Skirts
            "R_Legs == 'pants' and R_Upskirt", "images/RogueSprite/Rogue_legs_pants_down.png", 
            "R_Legs == 'pants'", "images/RogueSprite/Rogue_legs_pants.png",          
            "R_Legs == 'skirt' and R_Upskirt", "images/RogueSprite/Rogue_legs_skirt_up.png",
            "R_Legs == 'skirt'", "images/RogueSprite/Rogue_legs_skirt.png",          
            "True", Null(),   
            ),
        (0,0), ConditionSwitch(                                                                        
            #Arms and gloves
            "Rogue_Arms == 1 and R_Arms == 'gloved' and R_Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms1a_gloved.png",       #Gloves and collar 
            "Rogue_Arms == 1 and R_Arms == 'gloved'", "images/RogueSprite/Rogue_arms1b_gloved.png",                                     #Gloves, no collar
            "Rogue_Arms == 1 and R_Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms1a_bare.png",                                #No Gloves, collar 
            "Rogue_Arms == 1", "images/RogueSprite/Rogue_arms1b_bare.png",                                                              #No gloves, no collar
            "R_Arms == 'gloved' and R_Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms2a_gloved.png",                           #Gloves and collar 
            "R_Arms == 'gloved'", "images/RogueSprite/Rogue_arms2b_gloved.png",                                                         #Gloved, no collar
            "R_Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms2a_bare.png",                                                    #No gloves, collar
            "True", "images/RogueSprite/Rogue_arms2b_bare.png",    
            ), 
        (0,0), ConditionSwitch(                                                                         
            #chest layer
            "R_Pierce == 'barbell'", "images/RogueSprite/Rogue_chest_barbell.png",            
            "R_Pierce == 'ring'", "images/RogueSprite/Rogue_chest_rings.png",      
            "True", "images/RogueSprite/Rogue_chest_bare.png",    
            ),   
#        (0,0), ConditionSwitch(                                                                         
#            #chest clothes layer
#            "R_Chest == 'tank'", "images/RogueSprite/Rogue_chest_tank.png",
#            "R_Chest == 'buttoned tank'", "images/RogueSprite/Rogue_chest_tank2.png",            
#            "R_Chest == 'bra'", "images/RogueSprite/Rogue_chest_bra.png",                         
#            "R_Chest == 'sports bra'", "images/RogueSprite/Rogue_chest_sportsbra.png",
#            "R_Chest == 'lace bra'", "images/RogueSprite/Rogue_chest_lacebra.png",  
#            "True", Null(),               
#            ),   
        (0,0), ConditionSwitch(                                                                         
            #bra layer           
            "not R_Chest", Null(),             
            "R_Uptop", ConditionSwitch( 
                    #if the top's down. . .
                    "R_Chest == 'tank'", "images/RogueSprite/Rogue_chest_tank_Up.png",
                    "R_Chest == 'buttoned tank'", "images/RogueSprite/Rogue_chest_tank2_Up.png",            
                    "R_Chest == 'bra'", "images/RogueSprite/Rogue_chest_bra_Up.png",                         
                    "R_Chest == 'sports bra'", "images/RogueSprite/Rogue_chest_sportsbra_Up.png",
                    "R_Chest == 'lace bra'", "images/RogueSprite/Rogue_chest_lacebra_Up.png",            
                    "R_Chest == 'bikini top'", "images/RogueSprite/Rogue_chest_bikini_Up.png",     
                    ),            
            "True", ConditionSwitch(
                    #if the top's up. . .
                    "R_Chest == 'tank'", "images/RogueSprite/Rogue_chest_tank.png",
                    "R_Chest == 'buttoned tank'", "images/RogueSprite/Rogue_chest_tank2.png",            
                    "R_Chest == 'bra'", "images/RogueSprite/Rogue_chest_bra.png",                         
                    "R_Chest == 'sports bra'", "images/RogueSprite/Rogue_chest_sportsbra.png",
                    "R_Chest == 'lace bra'", "images/RogueSprite/Rogue_chest_lacebra.png",        
                    "R_Chest == 'bikini top'", "images/RogueSprite/Rogue_chest_bikini.png",          
                    "True", Null(),    
                    ),       
            ),
        (0,0), ConditionSwitch(                                                                         
            #water
            "R_Water and Rogue_Arms == 1", "images/RogueSprite/Rogue_body_wet1.png",
            "R_Water", "images/RogueSprite/Rogue_body_wet2.png",
            "True", Null(),                 
            ),
        (0,0), ConditionSwitch(                                                                         
            #soap
            "R_Water == 3", "images/RogueSprite/Rogue_body_wet3.png",
            "True", Null(),                 
            ),
#        (0,0), ConditionSwitch(                                                                         
#            #Overshirt layer
#            "Rogue_Arms == 1 and R_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh1.png",           
#            "Rogue_Arms == 1 and R_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink1.png",
#            "Rogue_Arms == 1 and R_Over == 'towel'", "images/RogueSprite/Rogue_over_towel1.png",
#            "Rogue_Arms == 1 and R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty1.png",
#            "Rogue_Arms == 1 and R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie1.png",
#            "R_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh2.png", 
#            "R_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink2.png",
#            "R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie2.png",
#            "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty2.png",
#            "R_Over == 'towel'", "images/RogueSprite/Rogue_over_towel2.png",              
#            "True", Null(), 
#            ),  
            
        (0,0), ConditionSwitch(                                                                         
            #shirt layer           
            "not R_Over", Null(),             
            "R_Uptop", ConditionSwitch( 
                    #if the top's down. . .
                    "Rogue_Arms == 1", ConditionSwitch( 
                            #if the arms are down. . .
                            "R_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh1_Up.png",           
                            "R_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink1_Up.png",
                            "R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie1_Up.png",
                            "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty_Up.png",
#                            "R_Over == 'towel'", Null(), 
                            "True", Null(),     
                            ),  
                    "True", ConditionSwitch( 
                            #if the arms are up. . .
                            "R_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh2_Up.png", 
                            "R_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink2_Up.png",
                            "R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie2_Up.png",
                            "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty_Up.png",
#                            "R_Over == 'towel'", Null(),       
                            "True", Null(),     
                            ),       
                    ),            
            "True", ConditionSwitch(
                    #if the top's up. . .
                    "Rogue_Arms == 1", ConditionSwitch( 
                            #if the arms are down. . .
                            "R_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh1.png",           
                            "R_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink1.png",
                            "R_Over == 'towel'", "images/RogueSprite/Rogue_over_towel1.png",
                            "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty1.png",
                            "R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie1.png",
                            "True", Null(),     
                            ),  
                    "True", ConditionSwitch( 
                            #if the arms are up. . .
                            "R_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh2.png", 
                            "R_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink2.png",
                            "R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie2.png",
                            "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty2.png",
                            "R_Over == 'towel'", "images/RogueSprite/Rogue_over_towel2.png",      
                            "True", Null(),     
                            ),       
                    ),       
            ),
        (0,0), ConditionSwitch(                                                                         
            #Hair
            "renpy.showing('Rogue_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Rogue_TJ_Animation')", Null(),
            "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_hair_wet.png",
            "R_Hair == 'wet'", "images/RogueSprite/Rogue_hair_wet.png",
            "True", "images/RogueSprite/Rogue_hair_evo.png",
            ),                           
        (0,0), ConditionSwitch(                                                                         
            #hand spunk
            "'hand' in R_Spunk and Rogue_Arms == 2", "images/RogueSprite/Rogue_spunkhand.png",                
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                                                                        
            #tits spunk
            "'tits' in R_Spunk", "images/RogueSprite/Rogue_spunktits.png",
            "True", Null(), 
            ),      
        (0,0), ConditionSwitch(                                                                        
            #face spunk
            "'facial' in R_Spunk", "images/RogueSprite/Rogue_facial.png",
            "True", Null(), 
            ),                
        (0,0), ConditionSwitch(                                                                        
            #Props
            "not R_Held or Rogue_Arms != 2", Null(), 
            "Rogue_Arms == 2 and R_Held == 'phone'", "images/RogueSprite/Rogue_held_phone.png",
            "Rogue_Arms == 2 and R_Held == 'dildo'", "images/RogueSprite/Rogue_held_dildo.png",            
            "Rogue_Arms == 2 and R_Held == 'vibrator'", "images/RogueSprite/Rogue_held_vibrator.png",
            "Rogue_Arms == 2 and R_Held == 'panties'", "images/RogueSprite/Rogue_held_panties.png",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(
            #UI tool for When Rogue is masturbating using Trigger3 actions
            "Trigger == 'lesbian' or not Trigger3 or Ch_Focus != 'Rogue'", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and R_Lust >= 70", "GirlFingerPussy",
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
            "not Trigger5 or Trigger4 != 'masturbation' or Ch_Focus == 'Rogue'", Null(), 
            #this doesn't activate unless Rogue is not primary, and is actively masturbating
            "Trigger5 == 'fondle pussy' and Trigger != 'sex' and R_Lust >= 70", "GirlFingerPussy",
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
            "not Trigger or Ch_Focus != 'Rogue'", Null(),
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
            "not Trigger2 or Ch_Focus != 'Rogue'", Null(),
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
            "not Trigger4 or Ch_Focus != 'Rogue'", Null(),
            "Trigger4 == 'fondle pussy' and Trigger != 'sex' and R_Lust >= 70", "GirlFingerPussy",
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
            "Trigger != 'lesbian' or not Trigger3 or Ch_Focus == 'Rogue'", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and R_Lust >= 70", "GirlFingerPussy",
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
    "R_Eyes == 'sexy'", "images/RogueSprite/Rogue_eyes_sexy.png",
    "R_Eyes == 'side'", "images/RogueSprite/Rogue_eyes_side.png",
    "R_Eyes == 'surprised'", "images/RogueSprite/Rogue_eyes_surprised.png",
    "R_Eyes == 'normal'", "images/RogueSprite/Rogue_eyes_normal.png",    
    "R_Eyes == 'stunned'", "images/RogueSprite/Rogue_eyes_stunned.png",
    "R_Eyes == 'down'", "images/RogueSprite/Rogue_eyes_down.png",
    "R_Eyes == 'closed'", "images/RogueSprite/Rogue_eyes_closed.png",
    "R_Eyes == 'manic'", "images/RogueSprite/Rogue_eyes_manic.png",
    "R_Eyes == 'squint'", "Rogue_Squint",
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
#                "Current_Time == 'Evening'",    "images/Crossroads_Evening.jpg",
#                "Current_Time == 'Night'",      "images/Crossroads_Night.jpg",    
#                "True",                         "images/Crossroads_Day.jpg",
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
                "E_Loc == 'bg teacher'", "Emma_At_Podium",
                "E_Loc == 'bg desk'", "Emma_At_Desk",
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
image Rogue_Doggy:
    LiveComposite(                                                                                 
        #Base body
        (420,750),  
        (0,0), ConditionSwitch(                                                         
            #Shows different upper body motion depending on events  
            "not P_Sprite", "Rogue_Doggy_Body",
            "P_Cock == 'anal'", ConditionSwitch( 
                    "Speed > 2", "Rogue_Doggy_Fuck2_Top",
                    "Speed > 1", "Rogue_Doggy_Fuck_Top",
                    "Speed", "Rogue_Doggy_Anal_Head_Top", 
                    "True", "Rogue_Doggy_Body",   
                    ),
            "P_Cock == 'in'", ConditionSwitch(   
                    "Speed > 2", "Rogue_Doggy_Fuck2_Top",
                    "Speed > 1", "Rogue_Doggy_Fuck_Top",
                    "True", "Rogue_Doggy_Body",                    
                    ),
            "True", "Rogue_Doggy_Body",           
            ),  
        (0,0), ConditionSwitch(                                                         
            #Shows different lower body motion depending on events
            "not P_Sprite", "Rogue_Doggy_Ass",
            "P_Cock == 'anal'", ConditionSwitch( 
                    "Speed > 2", "Rogue_Doggy_Fuck2_Ass",
                    "Speed > 1", "Rogue_Doggy_Fuck_Ass",
                    "Speed", "Rogue_Doggy_Anal_Head_Ass", 
                    "True", "Rogue_Doggy_Ass",   
                    ),
            "P_Cock == 'in'", ConditionSwitch(   
                    "Speed > 2", "Rogue_Doggy_Fuck2_Ass",
                    "Speed > 1", "Rogue_Doggy_Fuck_Ass",
                    "True", "Rogue_Doggy_Ass",                    
                    ),
            "True", "Rogue_Doggy_Ass",           
            ),  
        (0,0), ConditionSwitch(                                                         
            #Shows different lower body motion depending on events
            "P_Cock == 'foot'", ConditionSwitch( 
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
            "R_Water", Null(), 
            "R_Hair == 'evo'", "images/RogueDoggy/Rogue_Doggy_HairB.png",   
            "True", Null(), 
            ),   
        (0,0), "images/RogueDoggy/Rogue_Doggy_Body.png", #Body base
        (0,0), ConditionSwitch(             
            #Mouth
            "'mouth' in R_Spunk", ConditionSwitch( 
                    "R_Mouth == 'lipbite'", "images/RogueDoggy/Rogue_Doggy_Mouth_LipbiteW.png",
                    "R_Mouth == 'surprised'", "images/RogueDoggy/Rogue_Doggy_Mouth_SurprisedW.png",
                    "R_Mouth == 'sucking'", "images/RogueDoggy/Rogue_Doggy_Mouth_BlowW.png",
                    "R_Mouth == 'sad'", "images/RogueDoggy/Rogue_Doggy_Mouth_SadW.png",
                    "R_Mouth == 'smile'", "images/RogueDoggy/Rogue_Doggy_Mouth_SmileW.png",   
                    "R_Mouth == 'tongue'", "images/RogueDoggy/Rogue_Doggy_Mouth_TongueW.png",  
                    "True", "images/RogueDoggy/Rogue_Doggy_Mouth_NormalW.png",   
                    ),
            "R_Mouth == 'normal'", "images/RogueDoggy/Rogue_Doggy_Mouth_Normal.png",
            "R_Mouth == 'lipbite'", "images/RogueDoggy/Rogue_Doggy_Mouth_Lipbite.png",
            "R_Mouth == 'sucking'", "images/RogueDoggy/Rogue_Doggy_Mouth_Blow.png",            
            "R_Mouth == 'kiss'", "images/RogueDoggy/Rogue_Doggy_Mouth_Surprised.png",
            "R_Mouth == 'sad'", "images/RogueDoggy/Rogue_Doggy_Mouth_Sad.png",
            "R_Mouth == 'smile'", "images/RogueDoggy/Rogue_Doggy_Mouth_Smile.png",
            "R_Mouth == 'grimace'", "images/RogueDoggy/Rogue_Doggy_Mouth_Smile.png",
            "R_Mouth == 'surprised'", "images/RogueDoggy/Rogue_Doggy_Mouth_Surprised.png",       
            "R_Mouth == 'tongue'", "images/RogueDoggy/Rogue_Doggy_Mouth_Tongue.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Mouth_Smile.png", 
            ),
        (0,0), ConditionSwitch( 
            #Blush
            "R_Blush", "images/RogueDoggy/Rogue_Doggy_BlushEvo.png",
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(
            #Brows
            "R_Brows == 'normal'", "images/RogueDoggy/Rogue_Doggy_Brows_Normal.png",
            "R_Brows == 'angry'", "images/RogueDoggy/Rogue_Doggy_Brows_Angry.png",
            "R_Brows == 'sad'", "images/RogueDoggy/Rogue_Doggy_Brows_Sad.png",
            "R_Brows == 'surprised'", "images/RogueDoggy/Rogue_Doggy_Brows_Surprised.png",        
            "R_Brows == 'confused'", "images/RogueDoggy/Rogue_Doggy_Brows_Normal.png",
            "True", "images/RogueDoggy/Rogue_Doggy_Brows_Normal.png",
            ),     
        (0,0), "Rogue Doggy Blink",#Eyes
        (0,0), ConditionSwitch( 
            #Collar
            "R_Neck == 'spiked collar'", "images/RogueDoggy/Rogue_Doggy_Collar.png",   
            "True", Null(),                #R_Arms == 'gloved' or not R_Arms
            ),  
        (0,0), ConditionSwitch(   
            #tanktop
            "not R_Chest", Null(),        
            "R_Chest == 'tank'", "images/RogueDoggy/Rogue_Doggy_Chest_Tank.png",
            "R_Chest == 'buttoned tank'", "images/RogueDoggy/Rogue_Doggy_Chest_ButtonTank.png",
            "R_Chest == 'sports bra'", "images/RogueDoggy/Rogue_Doggy_Chest_SportsBra.png",
            "R_Chest == 'bikini top'", "images/RogueDoggy/Rogue_Doggy_Chest_Bikini.png",  
            "R_Chest", "images/RogueDoggy/Rogue_Doggy_Chest_Bra.png",
            "True", Null(),   
            ), 
        (0,0), ConditionSwitch(                                                                   
            #Wet look
            "R_Water", "images/RogueDoggy/Rogue_Doggy_WetTop.png",   
            "True", Null(),              
            ),  
        (0,0), ConditionSwitch(                     
            #Overshirt
            "not R_Over", Null(),
            "R_Over == 'mesh top'", "images/RogueDoggy/Rogue_Doggy_Over_Mesh.png",           
            "R_Over == 'pink top'", "images/RogueDoggy/Rogue_Doggy_Over_Pink.png",            
            "R_Over == 'hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_Hoodie.png",           
            "R_Over == 'nighty'", "images/RogueDoggy/Rogue_Doggy_Over_NightyTop.png",         
            "R_Over == 'towel'", "images/RogueDoggy/Rogue_Doggy_Over_TowelTop.png",
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(                                   
            #Hair
            "R_Water", "images/RogueDoggy/Rogue_Doggy_HairWet.png",   
            "R_Hair == 'evo'", "images/RogueDoggy/Rogue_Doggy_HairF.png",   
            "True", "images/RogueDoggy/Rogue_Doggy_HairF.png",                     
            ),  
        (0,0), ConditionSwitch(                                       
            #face spunk
            "not R_Spunk", Null(),
            "'facial' in R_Spunk", "images/RogueDoggy/Rogue_Doggy_Facial.png",
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                                                                             
            #Hair            
            "R_Over == 'hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_Hood.png", 
            "True", Null(),    
            ),  
        )

image Rogue_Doggy_Ass = LiveComposite(                                                                                          #Lower body
        (420,750), #(210,375), #(419,750), 
        (0,0), ConditionSwitch(                                                                               
            #Panties back
            "not R_PantiesDown or (R_Legs == 'pants' and not R_Upskirt)", Null(),  
            "R_Panties == 'shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts_Back.png",    
            "R_Panties == 'green panties'", "images/RogueDoggy/Rogue_Doggy_Undies_Back.png",  
            "R_Panties == 'bikini bottoms'", "images/RogueDoggy/Rogue_Doggy_Panties_Bikini_Back.png",   
            "R_Panties", "images/RogueDoggy/Rogue_Doggy_Panties_Back.png",  
            "True", Null(),  
            ),  
        (0,0), "images/RogueDoggy/Rogue_Doggy_Ass.png", #Ass Base
        (0,0), ConditionSwitch(
            #Wet look
            "R_Water", "images/RogueDoggy/Rogue_Doggy_WetAss.png",   
            "True", Null(),              
            ),  
        (0,0), ConditionSwitch(        
            #Hose
            "R_Hose == 'stockings'", "images/RogueDoggy/Rogue_Doggy_Hose.png",
            "True", Null(),
            ),             
        (0,0), ConditionSwitch(          
            #Panties if Down
            "not R_PantiesDown or (R_Legs == 'pants' and not R_Upskirt)", Null(),
            "R_Panties == 'shorts' and R_Wet > 1", "images/RogueDoggy/Rogue_Doggy_Shorts_Down_Wet.png", #fix turn this on when graphics fixed
            "R_Panties == 'shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts_Down.png", 
            "R_Panties == 'green panties' and R_Wet > 1", "images/RogueDoggy/Rogue_Doggy_Undies_Down_Wet.png",
            "R_Panties == 'green panties'", "images/RogueDoggy/Rogue_Doggy_Undies_Down.png",  
            "R_Panties == 'bikini bottoms'", "images/RogueDoggy/Rogue_Doggy_Panties_Bikini_Down.png",  
            "R_Panties", "images/RogueDoggy/Rogue_Doggy_Panties_Down.png",  
            "True", Null(),      
            ),  
            
            
        (0,0), ConditionSwitch(    
            #Pussy Composite      
            "P_Sprite and P_Cock == 'in'", ConditionSwitch(                     
                    "Speed > 2", "Rogue_Pussy_Fucking3",#Speed 3
                    "Speed > 1", "Rogue_Pussy_Fucking2",#Speed 2
                    "Speed", "Rogue_Pussy_Heading",      #Speed 1
                    "True", "Rogue_Pussy_Static",              #Speed 0
                    ),   
            "Trigger == 'lick pussy'", "images/RogueDoggy/Rogue_Doggy_Pussy_Open.png",   
            "True", "images/RogueDoggy/Rogue_Doggy_Pussy_Closed.png", 
            ),   
            
            
#        (0,0), ConditionSwitch(                                                                                 #spunkpussy Layer
#            "R_Spunk == 'in' and P_Cock == 'in'", "images/RogueDoggy/Rogue_Doggy_SpunkPussyOpen.png",  #fix for R_Spunk is used later
#            "R_Spunk == 'in'", "images/RogueDoggy/Rogue_Doggy_SpunkPussyClosed.png", 
#            "R_Wet and P_Cock == 'in'", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png", 
#            "R_Wet", "images/RogueDoggy/Rogue_Doggy_WetPussyClosed.png", 
#            "True", Null(),                    
#            ),   
        (0,0), ConditionSwitch(  
            #pubes              
            "not R_Pubes", Null(),         
            "P_Sprite and P_Cock == 'in'", Null(),
            "R_Legs == 'pants' and not R_Upskirt", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",   
            "R_PantiesDown", "images/RogueDoggy/Rogue_Doggy_Pubes.png",  
            "R_Panties", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",
            "R_Hose and R_Hose != 'stockings'", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",   
            "True", "images/RogueDoggy/Rogue_Doggy_Pubes.png",  
            ),  
        (0,0), ConditionSwitch(   
            #Pussy Piercings          
            "P_Sprite", Null(),             
            "R_Pierce == 'ring'", "images/RogueDoggy/Rogue_Doggy_PussyRing.png",            
            "R_Pierce == 'barbell'", "images/RogueDoggy/Rogue_Doggy_PussyBarbell.png",
            "True", Null(),  
            ),   
            
            
        (0,0), ConditionSwitch(    
            #Anus Composite 
            "P_Sprite and P_Cock == 'anal'", ConditionSwitch(                     
                    "Speed > 2", "Rogue_Anal_Fucking2", #Speed 3
                    "Speed > 1", "Rogue_Anal_Fucking",  #Speed 2
                    "Speed", "Rogue_Anal_Heading",      #Speed 1
                    "True", "Rogue_Anal",               #Speed 0
                    ),    
#            "Action == 'plug'", "Rogue_Anal_Plug",  
#            "Action == 'plug'", "test_case",
            "R_Loose", "images/RogueDoggy/Rogue_Doggy_Asshole_Loose.png",   
            "True", "images/RogueDoggy/Rogue_Doggy_Asshole_Tight.png", 
            ),    
            
            
        (0,0), ConditionSwitch( 
            #spunkanal Layer
            "'anal' not in R_Spunk or P_Sprite", Null(),   
            "P_Cock == 'anal'", "images/RogueDoggy/Rogue_Doggy_SpunkAnalOpen.png",  
            "R_Loose", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png", 
            ),   
        (0,0), ConditionSwitch(   
            #Panties if up
            "R_PantiesDown or not R_Panties", Null(),     
            "P_Sprite and (P_Cock == 'in' or P_Cock == 'anal')", Null(),
            "R_Panties == 'shorts' and R_Wet", "images/RogueDoggy/Rogue_Doggy_Shorts_Wet.png",          
            "R_Panties == 'shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts.png",
            "R_Panties == 'green panties' and R_Wet", "images/RogueDoggy/Rogue_Doggy_Undies_Wet.png",          
            "R_Panties == 'green panties'", "images/RogueDoggy/Rogue_Doggy_Undies.png",          
            "R_Panties == 'lace panties'", "images/RogueDoggy/Rogue_Doggy_PantiesLace.png",       
            "R_Panties == 'bikini bottoms'", "images/RogueDoggy/Rogue_Doggy_Panties_Bikini.png",                             
            "True", "images/RogueDoggy/Rogue_Doggy_Panties.png", 
            ),  
        (0,0), ConditionSwitch( 
            #full hose/tights  
            "P_Sprite and (P_Cock == 'in' or P_Cock == 'anal')", Null(),  
#            "R_Panties and R_PantiesDown and R_Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png", 
            "R_Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png", 
            "R_Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",  
            "R_Panties and R_PantiesDown", Null(),    
            "R_Hose == 'tights' and R_Wet", "images/RogueDoggy/Rogue_Doggy_Tights_Wet.png",
            "R_Hose == 'tights'", "images/RogueDoggy/Rogue_Doggy_Tights.png",
            "R_Hose == 'pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose.png",   
            "R_Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png", 
            "R_Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",            
            "True", Null(), 
            ),
        (0,0), ConditionSwitch( 
            #Legs Layer 
            "R_Legs == 'pants'", ConditionSwitch(    
                    "R_Upskirt", "images/RogueDoggy/Rogue_Doggy_Legs_Pants_Down.png",            
                    "R_Wet > 1", "images/RogueDoggy/Rogue_Doggy_Legs_Pants_Wet.png",
                    "True", "images/RogueDoggy/Rogue_Doggy_Legs_Pants.png",
                    ),     
            "R_Legs == 'skirt'", ConditionSwitch(    
                    "R_Upskirt and P_Sprite and P_Cock == 'anal' and Speed" , "images/RogueDoggy/Rogue_Doggy_Legs_Skirt_UpAnal.png",   
                    "R_Upskirt", "images/RogueDoggy/Rogue_Doggy_Legs_Skirt_Up.png",   
                    "True", "images/RogueDoggy/Rogue_Doggy_Legs_Skirt.png", 
                    ),          
            "True", Null(),                      
            ),   
        (0,0), ConditionSwitch(              
            #Over Layer
            "R_Over == 'nighty' and R_Upskirt", "images/RogueDoggy/Rogue_Doggy_Over_NightyAss_Up.png",            
            "R_Over == 'nighty'", "images/RogueDoggy/Rogue_Doggy_Over_NightyAss.png",
            "R_Over == 'towel' and R_Upskirt", "images/RogueDoggy/Rogue_Doggy_Over_TowelAss_Up.png",            
            "R_Over == 'towel'", "images/RogueDoggy/Rogue_Doggy_Over_TowelAss.png",
            "True", Null(),                    
            ),   
        (0,0), ConditionSwitch(  
            #spunk back Layer
            "'back' in R_Spunk", "images/RogueDoggy/Rogue_Doggy_SpunkAss.png",  
            "True", Null(),                    
            ),   
        (0,0), ConditionSwitch(  
            #Hotdogging underlayer
            "not P_Sprite or P_Cock != 'out'", Null(),   
            "R_Legs == 'skirt' and R_Upskirt", "images/RogueDoggy/Rogue_Doggy_HotdogUpskirtBack.png",  
            "True", "images/RogueDoggy/Rogue_Doggy_HotdogBack.png", 
            ),    
        (0,0), ConditionSwitch( 
            #Hotdogging Cock w/ alpha
            "not P_Sprite or P_Cock != 'out'", Null(),            
            "R_Legs == 'skirt' and R_Upskirt and Speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "R_Legs == 'skirt' and R_Upskirt", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
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
    "R_Eyes == 'sexy'", "images/RogueDoggy/Rogue_Doggy_Eyes_Sexy.png",
    "R_Eyes == 'side'", "images/RogueDoggy/Rogue_Doggy_Eyes_Side.png",
    "R_Eyes == 'normal'", "images/RogueDoggy/Rogue_Doggy_Eyes_Normal.png",
    "R_Eyes == 'closed'", "images/RogueDoggy/Rogue_Doggy_Eyes_Closed.png",
    "R_Eyes == 'manic'", "images/RogueDoggy/Rogue_Doggy_Eyes_Surprised.png",
    "R_Eyes == 'down'", "images/RogueDoggy/Rogue_Doggy_Eyes_Sexy.png",           
    "R_Eyes == 'stunned'", "images/RogueDoggy/Rogue_Doggy_Eyes_Stunned.png",
    "R_Eyes == 'surprised'", "images/RogueDoggy/Rogue_Doggy_Eyes_Surprised.png",
    "R_Eyes == 'squint'", "images/RogueDoggy/Rogue_Doggy_Eyes_Sexy.png",
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
            

image Rogue_Doggy_FeetB:        
    #Rogue's footjob feet toes
    contains:
        "images/RogueDoggy/Rogue_Doggy_Toes.png"
    contains:
            #hose
        ConditionSwitch(   
            "not R_Hose", Null(), 
            "R_Hose == 'stockings'", "images/RogueDoggy/Rogue_Doggy_Feet_Hose.png",              
            "R_Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Feet_Hose.png",   
            "R_Hose == 'tights'", "images/RogueDoggy/Rogue_Doggy_Feet_Tights.png",
            "R_Hose == 'pantyhose'", "images/RogueDoggy/Rogue_Doggy_Feet_Hose.png",   
            "R_Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_Feet_Hose_Holed.png", 
            "R_Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Feet_Tights_Holed.png",      
            "True", Null(),                
            )
    contains:
        #pants
        ConditionSwitch(     
            "R_Legs == 'pants'", "images/RogueDoggy/Rogue_Doggy_Feet_Pants.png",
            "True", Null(),           
            )
#    pos (0,0)

image Rogue_Doggy_Shins:                                             
    #Rogue's footjob shins
    contains:
        "images/RogueDoggy/Rogue_Doggy_Shins.png"
    contains:
        #pants
        ConditionSwitch(     
            "R_Legs == 'pants'", "images/RogueDoggy/Rogue_Doggy_Feet_Pants.png",
            "True", Null(),           
            )
    contains:
        "images/RogueDoggy/Rogue_Doggy_Feet.png"
    contains:
            #hose
        ConditionSwitch(  
            "not R_Hose", Null(),    
            "R_Hose == 'stockings'", "images/RogueDoggy/Rogue_Doggy_Feet_Hose.png",           
            "R_Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Feet_Hose.png",   
            "R_Hose == 'tights'", "images/RogueDoggy/Rogue_Doggy_Feet_Tights.png",
            "R_Hose == 'pantyhose'", "images/RogueDoggy/Rogue_Doggy_Feet_Hose.png",   
            "R_Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_Feet_Hose_Holed.png", 
            "R_Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Feet_Tights_Holed.png",      
            "True", Null(),                
            )
#    pos (0,0)      

#Hotdogging animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Zero_Doggy_Up:                                                                                  
    #Cock when out (hotdog)
    contains:
        ConditionSwitch(    
            "P_Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Cock_U_P.png",
            "P_Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Cock_U_B.png",             
            "True", "images/RogueDoggy/Rogue_Doggy_Cock_U_G.png", 
            ), 
    contains:
        ConditionSwitch(    
            "P_Wet", "images/RogueDoggy/Rogue_Doggy_Cock_U_W.png",
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
            "P_Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Cock_In_P.png",
            "P_Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Cock_In_B.png",             
            "True", "images/RogueDoggy/Rogue_Doggy_Cock_In_G.png", 
            ), 
    contains:
        ConditionSwitch(    
            "P_Wet", "images/RogueDoggy/Rogue_Doggy_Cock_In_Wet.png",           
            "True", Null(),
            ), 
    contains:
        ConditionSwitch(    
            "P_Spunk", "images/RogueDoggy/Rogue_Doggy_Cock_In_Spunk.png",           
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
#            "R_PantiesDown", Null(), 
#            "R_Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",    
#            "R_Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",    
##            "R_Hose == 'tights' and R_Wet", "images/RogueDoggy/Rogue_Doggy_Tights_Wet.png",
##            "R_Hose == 'tights'", "images/RogueDoggy/Rogue_Doggy_Tights.png",
##            "R_Hose == 'pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose.png",   
#            "R_Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png", 
#            "R_Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",            
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
            "R_Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",    
            "R_Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",  
            "R_Panties and R_PantiesDown", Null(), 
            "R_Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png", 
            "R_Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",            
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
            "R_Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",    
            "R_Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",  
            "R_Panties and R_PantiesDown", Null(), 
            "R_Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png", 
            "R_Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",            
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
            "R_Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",    
            "R_Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",  
            "R_Panties and R_PantiesDown", Null(), 
            "R_Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png", 
            "R_Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",            
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
            "R_Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",    
            "R_Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",  
            "R_Panties and R_PantiesDown", Null(),   
            "R_Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png", 
            "R_Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",            
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
            "R_Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",    
            "R_Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",   
            "R_Panties and R_PantiesDown", Null(),  
            "R_Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png", 
            "R_Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",            
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
            "R_Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",    
            "R_Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",  
            "R_Panties and R_PantiesDown", Null(),   
            "R_Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png", 
            "R_Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",            
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
            "R_Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",    
            "R_Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",  
            "R_Panties and R_PantiesDown", Null(),  
            "R_Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png", 
            "R_Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",            
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
            "R_Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",    
            "R_Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",  
            "R_Panties and R_PantiesDown", Null(), 
            "R_Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png", 
            "R_Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",            
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
            "R_Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",    
            "R_Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",  
            "R_Panties and R_PantiesDown", Null(), 
            "R_Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png", 
            "R_Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",            
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
                "P_Sprite", "Zero_Doggy_Up",            
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
            
#pos (100,450) #follow through  point r-60
#        pos (500,380) #high point r-40        
#        pos (310,520) #impact point r-60
#        block: 
#            ease 1 rotate 60
#            ease 1 rotate 90
#            repeat
            

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     
#Doggy Launch/Reset
label Rogue_Doggy_Launch(Line = "massage"): 
    if Line == "sex":        
        $ P_Cock = "in"
    elif Line == "anal":
        $ P_Cock = "anal"
    elif Line == "solo":   
        $ P_Sprite = 0
        $ P_Cock = "out"
    elif Line == "massage":   
        $ P_Sprite = 0
        $ P_Cock = 0
    elif Line == "hotdog":          
        $ P_Cock = "out"
    elif Line == "foot":          
        $ P_Cock = "foot"
    if not Trigger:
        $ Trigger = Line
    if renpy.showing("Rogue_Doggy"):
        return     
    $ P_Sprite = 1
    $ Speed = 0
    hide Rogue 
    if renpy.showing("Rogue_BJ_Animation"):
        hide Rogue_BJ_Animation   
    if renpy.showing("Rogue_HJ_Animation"):
        hide Rogue_HJ_Animation   
    if renpy.showing("Rogue_TJ_Animation"):
        hide Rogue_TJ_Animation   
    show Rogue_Doggy at SpriteLoc(StageCenter+50) zorder 150
    with dissolve
    return
    
label Rogue_Doggy_Reset:
    if not renpy.showing("Rogue_Doggy"):
        return
#    $ Trigger = 0               #fix, not sure this is a good idea
    $ Rogue_Arms = 2      
    $ R_SpriteVer = 0
    hide Rogue_Doggy
    call Rogue_Hide 
    show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
                    alpha 1
                    zoom 1
                    offset (0,0)
                    anchor (0.6, 0.0)
    with dissolve
    $ Speed = 0
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
            "R_Water and R_Hair == 'evo'", "images/RogueBJFace/Rogue_bj_hair_back_wet.png",
            "R_Hair == 'wet'", "images/RogueBJFace/Rogue_bj_hair_back_wet.png",
            "True", "images/RogueBJFace/Rogue_bj_hair_back.png",
            ),
    
image BJ_Backdrop:                                                                        #Her Body under the head
    "Rogue"
    zoom 4.5
    pos (175,-110)
    offset (-615, -125)
    
image BJ_Head:                                                                            #These are all the details of the face
    LiveComposite(    
        (787,913),     
        (0,0), ConditionSwitch(                                                                 #Hair back
            "R_Water and R_Hair == 'evo'", AlphaMask("images/RogueBJFace/Rogue_bj_hair_back_wet.png", "BJ_Backdrop"),
            "R_Hair == 'wet'", AlphaMask("images/RogueBJFace/Rogue_bj_hair_back_wet.png", "BJ_Backdrop"),
            "True", AlphaMask("images/RogueBJFace/Rogue_bj_hair_back.png", "BJ_Backdrop"),
            ),   
        (0,0), ConditionSwitch(                     
            "not Speed", "images/RogueBJFace/Rogue_bj_face_base.png",    
            "True", "images/RogueBJFace/Rogue_bj_face_base_s.png"
            ),   
        (0,0), ConditionSwitch(                                                                                 #Mouth for under layer
            "renpy.showing('Rogue_BJ_Animation') and Speed", ConditionSwitch(   
                    #if the BJface is happening
                    "Speed == 1 and 'mouth' in R_Spunk", "images/RogueBJFace/Rogue_bj_mouth_lickingS.png",
                    "Speed == 1", "images/RogueBJFace/Rogue_bj_mouth_licking.png", #licking
                    "Speed == 2", Null(),                                               #heading Rogue_BJ_HeadingMouth()
                    "Speed == 3", "images/RogueBJFace/Rogue_bj_mouth_sucking.png", #sucking
                    "Speed >= 4", "images/RogueBJFace/Rogue_bj_mouth_sucking.png", #deepthroat      
                    "True", Null(), 
                    ),        
            "'mouth' in R_Spunk", ConditionSwitch(   
                    #if spunk in mouth
                    "R_Mouth == 'sucking'", "images/RogueBJFace/Rogue_bj_mouth_surprisedS.png",
                    "R_Mouth == 'surprised'", "images/RogueBJFace/Rogue_bj_mouth_surprisedS.png",
                    "R_Mouth == 'sad'", "images/RogueBJFace/Rogue_bj_mouth_sadS.png",
                    "R_Mouth == 'kiss'", "images/RogueBJFace/Rogue_bj_mouth_sadS.png",
                    "R_Mouth == 'smile'", "images/RogueBJFace/Rogue_bj_mouth_lipbiteS.png",              
                    "R_Mouth == 'tongue'", "images/RogueBJFace/Rogue_bj_mouth_lickingS.png",
                    "True", "images/RogueBJFace/Rogue_bj_mouth_lipbiteS.png",  
                    ),    
            "True", ConditionSwitch(  
                    #if no Spunk
                    "R_Mouth == 'normal'", "images/RogueBJFace/Rogue_bj_mouth_normal.png",
                    "R_Mouth == 'lipbite'", "images/RogueBJFace/Rogue_bj_mouth_lipbite.png",
                    "R_Mouth == 'sucking'", "images/RogueBJFace/Rogue_bj_mouth_surprised.png",            
                    "R_Mouth == 'kiss'", "images/RogueBJFace/Rogue_bj_mouth_kiss.png",
                    "R_Mouth == 'sad'", "images/RogueBJFace/Rogue_bj_mouth_sad.png",
                    "R_Mouth == 'smile'", "images/RogueBJFace/Rogue_bj_mouth_smile.png",            
                    "R_Mouth == 'grimace'", "images/RogueBJFace/Rogue_bj_mouth_smile.png",
                    "R_Mouth == 'surprised'", "images/RogueBJFace/Rogue_bj_mouth_surprised.png",          
                    "R_Mouth == 'tongue'", "images/RogueBJFace/Rogue_bj_mouth_licking.png",    
                    "True", "images/RogueBJFace/Rogue_bj_mouth_normal.png",
                    ),    
            ),     
#            "Speed == 1 and Trigger == 'blow' and 'mouth' in R_Spunk", "images/RogueBJFace/Rogue_bj_mouth_lickingS.png",
#            "Speed == 1 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_mouth_licking.png", #licking
#            "Speed == 2 and Trigger == 'blow'", Null(),                                #heading Rogue_BJ_HeadingMouth()
#            "Speed == 3 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_mouth_sucking.png", #sucking
#            "Speed == 4 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_mouth_sucking.png", #deepthroat         
#            "'mouth' in R_Spunk and R_Mouth == 'sucking'", "images/RogueBJFace/Rogue_bj_mouth_surprisedS.png",
#            "'mouth' in R_Spunk and R_Mouth == 'surprised'", "images/RogueBJFace/Rogue_bj_mouth_surprisedS.png",
#            "'mouth' in R_Spunk and R_Mouth == 'sad'", "images/RogueBJFace/Rogue_bj_mouth_sadS.png",
#            "'mouth' in R_Spunk and R_Mouth == 'kiss'", "images/RogueBJFace/Rogue_bj_mouth_sadS.png",
#            "'mouth' in R_Spunk and R_Mouth == 'smile'", "images/RogueBJFace/Rogue_bj_mouth_lipbiteS.png",              
#            "'mouth' in R_Spunk and R_Mouth == 'tongue'", "images/RogueBJFace/Rogue_bj_mouth_lickingS.png",
#            "'mouth' in R_Spunk", "images/RogueBJFace/Rogue_bj_mouth_lipbiteS.png",
#            "R_Mouth == 'normal'", "images/RogueBJFace/Rogue_bj_mouth_normal.png",
#            "R_Mouth == 'lipbite'", "images/RogueBJFace/Rogue_bj_mouth_lipbite.png",
#            "R_Mouth == 'sucking'", "images/RogueBJFace/Rogue_bj_mouth_surprised.png",            
#            "R_Mouth == 'kiss'", "images/RogueBJFace/Rogue_bj_mouth_kiss.png",
#            "R_Mouth == 'sad'", "images/RogueBJFace/Rogue_bj_mouth_sad.png",
#            "R_Mouth == 'smile'", "images/RogueBJFace/Rogue_bj_mouth_smile.png",            
#            "R_Mouth == 'grimace'", "images/RogueBJFace/Rogue_bj_mouth_smile.png",
#            "R_Mouth == 'surprised'", "images/RogueBJFace/Rogue_bj_mouth_surprised.png",          
#            "R_Mouth == 'tongue'", "images/RogueBJFace/Rogue_bj_mouth_licking.png",    
#            "True", "images/RogueBJFace/Rogue_bj_mouth_normal.png",
#            ),   
        (316,590), ConditionSwitch(      #600               
            "renpy.showing('Rogue_BJ_Animation') and Speed == 2", At("BJ_MouthHeading", BJ_MouthAnim()),     
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                                 #cum for under layer
            "'facial' in R_Spunk", "images/RogueBJFace/Rogue_bj_facial_under.png",
            "not R_Spunk or Trigger != 'blow' or 'mouth' not in R_Spunk", Null(),
#            "Speed == 2", "images/RogueBJFace/Rogue_bj_face_under_heading_cum.png", 
            "Speed == 3", "images/RogueBJFace/Rogue_bj_face_under_sucking_cum.png",
            "Speed == 4", "images/RogueBJFace/Rogue_bj_face_under_sucking_cum.png",  
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(                                                                 #Brows
            "R_Brows == 'normal'", "images/RogueBJFace/Rogue_bj_face_brows_normal.png",
            "R_Brows == 'angry'", "images/RogueBJFace/Rogue_bj_face_brows_angry.png",
            "R_Brows == 'sad'", "images/RogueBJFace/Rogue_bj_face_brows_sad.png",
            "R_Brows == 'surprised'", "images/RogueBJFace/Rogue_bj_face_brows_surprised.png",        
            "R_Brows == 'confused'", "images/RogueBJFace/Rogue_bj_face_brows_confused.png",
            "True", "images/RogueBJFace/Rogue_bj_face_brows_normal.png",
            ),
        (0,0), "BJ Blink",                                                                #Eyes
        (0,0), ConditionSwitch(                                                                 #cum on the face
                "'facial' in R_Spunk", "images/RogueBJFace/Rogue_bj_facial_over.png",
                "not R_Spunk or Trigger != 'blow' or 'mouth' not in R_Spunk", Null(),
#                "Speed == 2", "images/RogueBJFace/Rogue_bj_face_over_heading_cum.png", 
                "Speed == 3", "images/RogueBJFace/Rogue_bj_face_over_sucking_cum.png",
                "Speed == 4", "images/RogueBJFace/Rogue_bj_face_over_sucking_cum.png",  
                "True", Null(),
                ),
        (0,0), ConditionSwitch(                                                                 #Hair overlay
            "R_Water and R_Hair == 'evo'", "images/RogueBJFace/Rogue_bj_hair_wet.png",
            "R_Hair == 'wet'", "images/RogueBJFace/Rogue_bj_hair_wet.png",
            "True", "images/RogueBJFace/Rogue_bj_hair.png",
            ),
        )


image BJ Blink:                                                                           #eyeblinks
    ConditionSwitch(
        "R_Eyes == 'normal'", "images/RogueBJFace/Rogue_bj_face_eyes_normal.png",  
        "R_Eyes == 'sexy'", "images/RogueBJFace/Rogue_bj_face_eyes_sexy.png",  
        "R_Eyes == 'closed'", "images/RogueBJFace/Rogue_bj_face_eyes_closed.png",
        "R_Eyes == 'surprised'", "images/RogueBJFace/Rogue_bj_face_eyes_surprised.png",
        "R_Eyes == 'side'", "images/RogueBJFace/Rogue_bj_face_eyes_side.png",
        "R_Eyes == 'stunned'", "images/RogueBJFace/Rogue_bj_face_eyes_stunned.png",
        "R_Eyes == 'down'", "images/RogueBJFace/Rogue_bj_face_eyes_down.png",
        "R_Eyes == 'manic'", "images/RogueBJFace/Rogue_bj_face_eyes_surprised.png",
        "R_Eyes == 'squint'", "images/RogueBJFace/Rogue_bj_face_eyes_squint.png",
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

image BJ_MouthHeading:                                          #the mouth used for the heading animations
    contains:
        ConditionSwitch(   
            #if spunk in mouth
            "'mouth' in R_Spunk", "images/RogueBJFace/Rogue_bj_mouth_suckingS.png",
            "True", "images/RogueBJFace/Rogue_bj_mouth_sucking.png",  
            )   
#        "images/RogueBJFace/Rogue_bj_mouth_sucking.png"
        anchor (0.40,0.65) 
        
image BJ_MaskHeading:                                           #the mask used for the heading image 
    contains:
        "images/RogueBJFace/Rogue_bj_facemask.png"
        anchor (0.4,0.65)    

image BJ_MaskHeadingComposite:                                  #The composite for the heading mask that goes over the face
    LiveComposite(    
        (787,913),  
        (316,590), ConditionSwitch(      #600               
            "Speed == 2", At("BJ_MaskHeading", BJ_MouthAnim()),     
            "True", Null(),
            ),  
        )
    
transform BJ_MouthAnim():                                       #The animation for the heading mouth
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
            
#            pause .15                
#            easein .4 zoom 0.87
#            linear .1 zoom 0.9
#            easeout .45 zoom 0.70 
#            pause .50                        
#            easein .25 zoom 0.9
#            linear .1 zoom 0.87
#            easeout .3 zoom 0.9  
#            pause .25
            repeat
            
image Blowcock:
    contains:
        ConditionSwitch(        
            "P_Color == 'pink'", "images/RogueBJFace/Zero_Cock_P.png",
            "P_Color == 'brown'", "images/RogueBJFace/Zero_Cock_B.png",             
            "P_Color == 'green'", "images/RogueBJFace/Zero_Cock_G.png", 
            "True", Null(),
            ),   
    contains:
        ConditionSwitch(                 
            "P_Wet", "images/RogueBJFace/Zero_Cock_Wet.png", 
            "True", Null(),
            ),       
    contains:
        ConditionSwitch(    
            "P_Spunk", "images/RogueBJFace/Zero_Cock_S.png", 
            "True", Null(),
            ),  
    anchor (0.5,0.5)
    zoom 1.0
    alpha 1.0
    offset (26,350)#(-175,450)
    
transform Cock_BJ_Starting():                            #The static animation for the cock
    anchor (.5,.5)
    rotate -10

transform Cock_BJ_Licking():                            #The licking animation for the cock
    subpixel True
    anchor (.5,.5)
    ease 0.5 rotate 0
    block:
        ease 2 rotate -5 #410
        pause .5
        ease 2.5 rotate 0
        repeat
        
transform Cock_BJ_Straight():                            #The static animation for the cock
    anchor (.5,.5)
    rotate 0
    
transform BJ_Licking():                                 #The licking animation for her face
    subpixel True 
    ease 0.5 offset (0,-35)  #top
    block:
        ease 2.5 offset (25,100) #bottom
        ease 2 offset (0,-35)  #top
        pause .5
        repeat

transform BJ_LickingBody():                             #The licking animation for her body
    subpixel True 
    ease 0.5 offset (0,-35)  #top
    block:
        ease 2.5 offset (30,90) #bottom 25,50
        ease 2 offset (0,-35)  #top
        pause .5
        repeat
        
transform BJ_Heading():                                 #The heading animation for her face
    subpixel True 
    offset (0,-40)     #top 
    block:
        ease 1 yoffset 35           #bottom         
        ease 1.5 offset (0,-40)     #top  
        repeat

transform BJ_HeadingBody():                             #The heading animation for her body
    subpixel True 
    offset (0,-40)     #top 
    block:
        ease 1 yoffset 15           #bottom         
        ease 1.5 offset (0,-40)     #top  
        repeat
        
transform BJ_Sucking():                                 #The sucking animation for her face
    subpixel True
    ease 0.5 offset (0,50) 
    block:
        ease 1 yoffset 120 #100
        ease 1.5 offset (0,50) 
        repeat
    
transform BJ_SuckingBody():                             #The sucking animation for her body
    subpixel True 
    ease 0.5 offset (0,50)  
    block:
        ease 1 yoffset 100 #80      #bottom
        ease 1.5 offset (0,50) #top
        repeat
    
transform BJ_Deep():                                    #The deep animation for her face
    ease .5 offset (0,100) 
    block:
        subpixel True
        ease 1 yoffset 300
        pause .5
        ease 2 yoffset 100  
        repeat
        
transform BJ_DeepBody():                                #The deep animation for her body
    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1.2 yoffset 250
        pause .5
        ease 1.8 yoffset 100   
        repeat    

transform BJ_Static():                                  #The static animation for her face
    subpixel True 
    ease 1.5 offset (0,0)
    repeat

transform BJ_StaticBody():                              #The static animation for her face
    subpixel True 
    ease 1.5 offset (0,0)
                                         
transform BJ_Starting():                                #The starting animation for her face
    subpixel True 
    ease 1.5 offset (0,0)
    
transform BJ_StartingBody():                            #The starting animation for her face
    subpixel True 
    ease 1.5 offset (0,0)
                                                               #BJ Launchers  
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Rogue_BJ_Launch(Line = 0):    # The sequence to launch the Rogue BJ animations  
    if renpy.showing("Rogue_BJ_Animation"):
        return
    
    call Rogue_Hide
    if Line == "L" or Line == "cum":
        show Rogue at SpriteLoc(StageCenter) zorder RogueLayer:
            alpha 1
#            zoom 1 offset (0,0)
            ease 1 zoom 2.5 offset (70,140) #(-90,140) offset (150,80) 
        with dissolve
    else:
        show Rogue at SpriteLoc(StageCenter) zorder RogueLayer:
            alpha 1
            zoom 2.5 offset (70,140) #(-90,140) 
        with dissolve
        
#    show Rogue:
#        pos (715,50)
#        alpha 1
#        zoom 2.5 offset (-90,140) 
#    with dissolve
        
    if Taboo and Line == "L": # Rogue gets started. . .
        if not R_Blow:
            if K_Loc == bg_current:
                "Rogue looks back at Kitty to see if she's watching."
            elif E_Loc == bg_current:
                "Rogue looks back at Emma to see if she's watching."
            else:
                "Rogue looks around to see if anyone can see her."
            "Rogue hesitantly pulls down your pants and touches her mouth to your cock."
        else:
            if K_Loc == bg_current:
                "Rogue looks back at Kitty to see if she's watching."
            elif E_Loc == bg_current:
                "Rogue looks back at Emma to see if she's watching."
            else:
                "Rogue hesitantly looks around to see if anyone notices what she's doing."
            "She then bends down and puts her lips around you."
    elif Line == "L":    
        if not R_Blow:
            "Rogue hesitantly pulls down your pants and touches her mouth to your cock."
        else:
            "Rogue bends down and begins to suck on your cock."    
            
    $ Speed = 0
    
    if Line != "cum":
        $ Trigger = "blow"
    
    show Rogue zorder RogueLayer:
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
    
    show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:        
        zoom 2 offset (70,140)
        alpha 1
        block:
            pause .5
            ease 1 zoom 1.5 offset (-50,50)
            pause .5
            ease .5 zoom 1 offset (0,0)    
    show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
        alpha 1
        zoom 1 offset (0,0)    
    call RogueFace("sexy")        
    return  
    
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////


#       Face currently used for titfucking. Remove once titfucking uses new facial system


image Rogue_BJFace:
    LiveComposite(    
        (787,912),     
        (0,0), ConditionSwitch(
            "R_Blush and Trigger != 'blow'", "images/RogueBJFace/Rogue_bj_face_over_blush.png",
            "Trigger != 'blow'", Null(),
            "Speed == 3 and R_Blush", "images/RogueBJFace/Rogue_bj_face_over_suckingB.png",
            "Speed == 3 and not R_Blush", "images/RogueBJFace/Rogue_bj_face_over_sucking.png",
            "Speed == 2 and R_Blush", "images/RogueBJFace/Rogue_bj_face_over_headingB.png",
            "Speed == 2 and not R_Blush", "images/RogueBJFace/Rogue_bj_face_over_heading.png",
            "Speed == 4 and R_Blush", "images/RogueBJFace/Rogue_bj_face_over_suckingB.png",
            "Speed == 4 and not R_Blush", "images/RogueBJFace/Rogue_bj_face_over_sucking.png",
            "R_Blush", "images/RogueBJFace/Rogue_bj_face_over_blush.png",
            "True", Null(),
            ),       
        (0,0), ConditionSwitch(
            "R_Brows == 'normal'", "images/RogueBJFace/Rogue_bj_face_brows_normal.png",
            "R_Brows == 'angry'", "images/RogueBJFace/Rogue_bj_face_brows_angry.png",
            "R_Brows == 'sad'", "images/RogueBJFace/Rogue_bj_face_brows_sad.png",
            "R_Brows == 'surprised'", "images/RogueBJFace/Rogue_bj_face_brows_surprised.png",        
            "R_Brows == 'confused'", "images/RogueBJFace/Rogue_bj_face_brows_confused.png",
            "True", "images/RogueBJFace/Rogue_bj_face_brows_normal.png",
            ),
        (0,0), "Rogue_BJ Blink",  
        (0,0), ConditionSwitch(
                "not R_Spunk", Null(),
                "'mouth' in R_Spunk and Speed == 2 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_face_over_heading_cum.png", 
                "'mouth' in R_Spunk and Speed == 3 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_face_over_sucking_cum.png",
                "'mouth' in R_Spunk and Speed == 4 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_face_over_sucking_cum.png",  
                "True", Null(),
                ),
        (0,0), ConditionSwitch(
                "not R_Spunk", Null(),
                "'facial' in R_Spunk", "images/RogueBJFace/Rogue_bj_facial_over.png", 
                "True", Null(),
                ),
        (0,0), ConditionSwitch(
            "R_Hair == 'evo'", "images/RogueBJFace/Rogue_bj_hair.png",
            "True", "images/RogueBJFace/Rogue_bj_hair.png",
            ),              
        )

#Rogue BJ Under Sprite Compositing
image Rogue_BJChin:
    LiveComposite(
        (787,912),     
        (0,0), "images/RogueBJFace/Rogue_bj_face_under.png", 
        (0,0), ConditionSwitch(    
            "Speed == 1 and Trigger == 'blow' and 'mouth' in R_Spunk", "images/RogueBJFace/Rogue_bj_mouth_lickingS.png",
            "Speed == 1 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_mouth_licking.png",
            "Speed == 2 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_mouth_heading.png", 
            "Speed == 3 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_mouth_sucking.png",
            "Speed == 4 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_mouth_sucking.png",           
            "'mouth' in R_Spunk and R_Mouth == 'sucking'", "images/RogueBJFace/Rogue_bj_mouth_surprisedS.png",
            "'mouth' in R_Spunk and R_Mouth == 'surprised'", "images/RogueBJFace/Rogue_bj_mouth_surprisedS.png",
            "'mouth' in R_Spunk and R_Mouth == 'sad'", "images/RogueBJFace/Rogue_bj_mouth_sadS.png",
            "'mouth' in R_Spunk and R_Mouth == 'kiss'", "images/RogueBJFace/Rogue_bj_mouth_sadS.png",
            "'mouth' in R_Spunk and R_Mouth == 'smile'", "images/RogueBJFace/Rogue_bj_mouth_lipbiteS.png",              
            "'mouth' in R_Spunk and R_Mouth == 'tongue'", "images/RogueBJFace/Rogue_bj_mouth_lickingS.png",
            "'mouth' in R_Spunk", "images/RogueBJFace/Rogue_bj_mouth_lipbiteS.png",
            "R_Mouth == 'normal'", "images/RogueBJFace/Rogue_bj_mouth_normal.png",
            "R_Mouth == 'lipbite'", "images/RogueBJFace/Rogue_bj_mouth_lipbite.png",
            "R_Mouth == 'sucking'", "images/RogueBJFace/Rogue_bj_mouth_surprised.png",            
            "R_Mouth == 'kiss'", "images/RogueBJFace/Rogue_bj_mouth_kiss.png",
            "R_Mouth == 'sad'", "images/RogueBJFace/Rogue_bj_mouth_sad.png",
            "R_Mouth == 'smile'", "images/RogueBJFace/Rogue_bj_mouth_smile.png",            
            "R_Mouth == 'grimace'", "images/RogueBJFace/Rogue_bj_mouth_smile.png",
            "R_Mouth == 'surprised'", "images/RogueBJFace/Rogue_bj_mouth_surprised.png",          
            "R_Mouth == 'tongue'", "images/RogueBJFace/Rogue_bj_mouth_licking.png",    
            "True", "images/RogueBJFace/Rogue_bj_mouth_normal.png",
            ),       
        (0,0), ConditionSwitch(
                "not R_Spunk", Null(),
                "'mouth' in R_Spunk and Speed == 2 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_face_under_heading_cum..png", 
                "'mouth' in R_Spunk and Speed == 3 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_face_under_sucking_cum.png",
                "'mouth' in R_Spunk and Speed == 4 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_face_under_sucking_cum.png",  
                "True", Null(),
                ),
        (0,0), ConditionSwitch(
                "not R_Spunk", Null(),
                "'facial' in R_Spunk", "images/RogueBJFace/Rogue_bj_facial_under.png", 
                "True", Null(),
                ),
        )

image Rogue_BJ Blink:
    ConditionSwitch(
        "R_Eyes == 'normal'", "images/RogueBJFace/Rogue_bj_face_eyes_normal.png",  
        "R_Eyes == 'sexy'", "images/RogueBJFace/Rogue_bj_face_eyes_sexy.png",  
        "R_Eyes == 'closed'", "images/RogueBJFace/Rogue_bj_face_eyes_closed.png",
        "R_Eyes == 'surprised'", "images/RogueBJFace/Rogue_bj_face_eyes_surprised.png",
        "R_Eyes == 'side'", "images/RogueBJFace/Rogue_bj_face_eyes_side.png",
        "R_Eyes == 'stunned'", "images/RogueBJFace/Rogue_bj_face_eyes_stunned.png",
        "R_Eyes == 'down'", "images/RogueBJFace/Rogue_bj_face_eyes_down.png",
        "R_Eyes == 'manic'", "images/RogueBJFace/Rogue_bj_face_eyes_surprised.png",
        "R_Eyes == 'squint'", "images/RogueBJFace/Rogue_bj_face_eyes_sexy.png",
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
            "P_Color == 'pink'", "images/RogueBJFace/Zero_Cock_P.png",
            "P_Color == 'brown'", "images/RogueBJFace/Zero_Cock_B.png",             
            "P_Color == 'green'", "images/RogueBJFace/Zero_Cock_G.png", 
            "True", Null(),
            ),   
        (0,0), ConditionSwitch(                 
            "P_Wet", "images/RogueBJFace/Zero_Cock_Wet.png", 
            "True", Null(),
            ),       
        (0,0), ConditionSwitch(    
            "P_Spunk", "images/RogueBJFace/Zero_Cock_S.png", 
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
            "'tits' in R_Spunk", "images/RogueBJFace/Rogue_tj_spunkU.png",
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
            "R_Pierce == 'barbell'", "images/RogueBJFace/Rogue_tj_tits_b.png", 
            "R_Pierce == 'ring'", "images/RogueBJFace/Rogue_tj_tits_r.png",
            "R_Pierce != 'barbell'", "images/RogueBJFace/Rogue_tj_tits.png",
            ),
    contains:
        ConditionSwitch( 
            "'tits' in R_Spunk", "images/RogueBJFace/Rogue_tj_spunk.png",
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
        
        
transform Zero_TJ_Cock():                            #The sucking animation for the cock
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



image Rogue_TJ_Animation:                                                                                               #core TJ animation
    contains:
        ConditionSwitch(                                                                          # Zero cock sucking
            "not Speed", Transform("Rogue_TJ_Under"), 
            "Speed == 1", At("Rogue_TJ_Under", Rogue_TJ_Under_1()),
            "Speed >= 2", At("Rogue_TJ_Under", Rogue_TJ_Under_2()),
            "Speed", Null(),
            ),  
    
    contains:
        ConditionSwitch(                                                                          # Zero cock sucking
            "not Speed", At("Zero_Blowcock", Zero_TJ_Cock()),
            "Speed == 1", At("Zero_Blowcock", Zero_TJ_Cock_1()),
            "Speed >= 2", At("Zero_Blowcock", Zero_TJ_Cock_2()),
            "Speed", Null(),
            ),  
        
    contains:
        ConditionSwitch(                                                                          # Zero cock sucking
            "not Speed", Transform("Rogue_TJ_Over"), 
            "Speed == 1", At("Rogue_TJ_Over", Rogue_TJ_Over_1()),
            "Speed >= 2", At("Rogue_TJ_Over", Rogue_TJ_Over_2()), 
            "Speed", Null(),
            ),     
    anchor (0.6, 0.0)
    offset (-75, 250)
    zoom .55
        
label Rogue_TJ_Launch(Line = 0):    # The sequence to launch the Rogue Titfuck animations   
    if renpy.showing("Rogue_TJ_Animation"):
        return
    call Rogue_Hide
    show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
        alpha 1
        ease 1 zoom 2 xpos 550 yoffset 50 #offset (-100,50) 
    if Taboo: # Rogue gets started. . .
            if K_Loc == bg_current:
                "Rogue looks back at Kitty to see if she's watching."
            elif E_Loc == bg_current:
                "Rogue looks back at Emma to see if she's watching."
            else:
                "Rogue looks around to see if anyone can see her."
    
    if R_Chest and R_Over:
        "She throws off her [R_Over] and her [R_Chest]."                
    elif R_Over:
        "She throws off her [R_Over], baring her breasts underneath."
    elif R_Chest:
        "She tugs off her [R_Chest] and throws it aside."
    $ R_Over = 0
    $ R_Chest = 0
    $ R_Arms = 0
    
    call Rogue_First_Topless                
    
    if not R_Tit and Line == "L": #first time
        if not R_Chest and not R_Over:
            "As you pull out your cock, Rogue hesitantly places it between her breasts and starts to rub them up and down the shaft."
        elif R_Chest and not R_Over:
            "As you pull out your cock, Rogue hesitantly places it under her [R_Chest], between her breasts and starts to rub them up and down the shaft."
        elif R_Chest and R_Over:
            "As you pull out your cock, Rogue hesitantly places it under her [R_Over], between her breasts and starts to rub them up and down the shaft."
        else:
            "As you pull out your cock, Rogue hesitantly places it under her clothes, between her breasts and starts to rub them up and down the shaft."
    elif Line == "L": #any other time
        if not R_Chest and not R_Over:
            "As you pull out your cock, Rogue places it between her breasts and starts to rub them up and down the shaft."
        elif R_Chest and not R_Over:
            "As you pull out your cock, Rogue places it under her [R_Chest], between her breasts and starts to rub them up and down the shaft."
        elif R_Chest and R_Over:
            "As you pull out your cock, Rogue places it under her [R_Over], between her breasts and starts to rub them up and down the shaft."
        else:
            "As you pull out your cock, Rogue places it under her clothes, between her breasts and starts to rub them up and down the shaft."    
    else:
        "Rogue wraps her tits around your cock."
#    hide Rogue    
    show blackscreen onlayer black with dissolve
    show Rogue zorder RogueLayer:
        alpha 0
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "titjob"
    show Rogue_TJ_Animation at SpriteLoc(StageRight) zorder 150 
    hide blackscreen onlayer black with dissolve
    return
    
label Rogue_TJ_Reset: # The sequence to the Rogue animations from Titfuck to default
    if not renpy.showing("Rogue_TJ_Animation"):
        return
    hide Rogue_TJ_Animation
    call Rogue_Hide 
    show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
        zoom 2 xpos 550 yoffset 50 #offset (-100,50)  #zoom 2 offset (-100,50)
    show Rogue zorder RogueLayer:
        alpha 1
        ease 1 zoom 1.5 xpos 500 yoffset 50
        pause .5
        ease .5 zoom 1 xpos R_SpriteLoc yoffset 0
    show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
        alpha 1
        zoom 1 xpos R_SpriteLoc yoffset 0   
        
    "Rogue pulls back"
    return
    

# Core Rogue Handjob element //////////////////////////////////////////////////////////////////////                                         Core Rogue HJ element

image Zero_Handcock:
    contains:
        ConditionSwitch(    # Zero cock sucking
            "P_Color == 'pink'", "images/RogueBJFace/handcock_P.png",
            "P_Color == 'brown'", "images/RogueBJFace/handcock_B.png",             
            "P_Color == 'green'", "images/RogueBJFace/handcock_G.png", 
            "P_Color != 'pink'", Null(),
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
    $ R_Arms = 0
    $ Rogue_Arms = 1    
    if not renpy.showing("Rogue"): 
        show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
            alpha 1
            zoom 1.7 xpos 700 yoffset 200 #offset (-50,200)
        with dissolve    
    show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
        alpha 1
        ease 1 zoom 1.7 xpos 700 yoffset 200 #offset (-50,200)
   
    if Taboo and Line == "L": # Rogue gets started. . .
        if not R_Hand:
            if K_Loc == bg_current:
                "Rogue looks back at Kitty to see if she's watching."
            elif E_Loc == bg_current:
                "Rogue looks back at Emma to see if she's watching."
            else:
                "Rogue looks around to see if anyone can see her."
            "As you pull out your cock, Rogue pulls off her gloves, and hesitantly reaches for it. She starts to roughly stroke on it."
        else:
            if K_Loc == bg_current:
                "Rogue looks back at Kitty to see if she's watching."
            elif E_Loc == bg_current:
                "Rogue looks back at Emma to see if she's watching."
            else:
                "Rogue hesitantly looks around to see if anyone notices what she's doing."
            "She then leans over and grabs your cock."
    elif Line == "L":    
        if not R_Hand:
            "As you pull out your cock, Rogue pulls off her gloves, and hesitantly reaches for it. She starts to roughly stroke on it."
        else:
            "Rogue bends down and grabs your cock."
    else:
        "Rogue bends down and grabs your cock."
            
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    show Rogue_HJ_Animation at SpriteLoc(R_SpriteLoc) zorder 150 with easeinbottom
    return
    
label Rogue_HJ_Reset: # The sequence to the Rogue animations from handjob to default
    if not renpy.showing("Rogue_HJ_Animation"):
        return    
    $ Speed = 0
    hide Rogue_HJ_Animation
    with dissolve    
    call Rogue_Hide 
    show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
        alpha 1
        zoom 1.7  xpos 700 yoffset 200
    show Rogue zorder RogueLayer:
        alpha 1
        ease 1 zoom 1.5 yoffset 50
        pause .5
        ease .5 zoom 1 xpos R_SpriteLoc yoffset 0   
    show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
        alpha 1
        zoom 1  xpos R_SpriteLoc yoffset 0        
    return
    
# All Reset ////////////////////////////////////////////////////////////////////////////////////
label AllReset(chr = "Rogue"): 
    #call AllReset("all")
    if chr == "Rogue" or chr == "all":
        if renpy.showing("Rogue_Doggy"): 
            call Rogue_Doggy_Reset
        if renpy.showing("Rogue_HJ_Animation"): 
            call Rogue_HJ_Reset
        if renpy.showing("Rogue_BJ_Animation"):   
            call Rogue_BJ_Reset
        if renpy.showing("Rogue_TJ_Animation"):   
            call Rogue_TJ_Reset
        call Rogue_Hide
        if R_Loc == bg_current:
            show Rogue at SpriteLoc(R_SpriteLoc,50) zorder RogueLayer:
                ease .5 zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.6, 0.0)
            show Rogue:
                zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.6, 0.0) pos (R_SpriteLoc,50)
        else:
            hide Rogue           
            
                    
    if chr == "Kitty" or chr == "all":
        if renpy.showing("Kitty_SexSprite"): 
            call Kitty_Sex_Reset
        if renpy.showing("Kitty_HJ_Animation"): 
            call Kitty_HJ_Reset
        if renpy.showing("Kitty_BJ_Animation"):   
            call Kitty_BJ_Reset
        if renpy.showing("Kitty_TJ_Animation"):   
            call Kitty_TJ_Reset
        call Kitty_Hide
        if K_Loc == bg_current:
            show Kitty_Sprite at SpriteLoc(K_SpriteLoc,50) zorder KittyLayer:
                ease .5 zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0)
            show Kitty_Sprite:
                zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0) pos (K_SpriteLoc,50)
        else:
            hide Kitty_Sprite
    if chr == "Emma" or chr == "all":
        if renpy.showing("Emma_SexSprite"): 
            call Emma_Sex_Reset
        if renpy.showing("Emma_HJ_Animation"): 
            call Emma_HJ_Reset
        if renpy.showing("Emma_BJ_Animation"):   
            call Emma_BJ_Reset
        if renpy.showing("Emma_TJ_Animation"):   
            call Emma_TJ_Reset
        if renpy.showing("Emma_FJ_Animation"):   
            call Emma_FJ_Reset
        call Emma_Hide
        if E_Loc == bg_current:
            show Emma_Sprite at SpriteLoc(E_SpriteLoc,50) zorder EmmaLayer:
                ease .5 zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0)
            show Emma_Sprite:
                zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0) pos (E_SpriteLoc,50)
        else:
            hide Emma_Sprite
    if chr == "Laura" or chr == "all":
        if renpy.showing("Laura_SexSprite"): 
            call Laura_Sex_Reset
        if renpy.showing("Laura_HJ_Animation"): 
            call Laura_HJ_Reset
        if renpy.showing("Laura_BJ_Animation"):   
            call Laura_BJ_Reset
        if renpy.showing("Laura_TJ_Animation"):   
            call Laura_TJ_Reset
        call Laura_Hide
        if L_Loc == bg_current:
            show Laura_Sprite at SpriteLoc(L_SpriteLoc,50) zorder LauraLayer:
                ease .5 zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0)
            show Laura_Sprite:
                zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0) pos (L_SpriteLoc,50)
        else:
            hide Laura_Sprite
    return
            
            
# Interface items //////////////////////////////////////////////////////////////////////////////

transform Vibrate():
    subpixel True
    block:
        linear .5 xoffset 2
        linear .5 xoffset -2
        repeat


image UI_Vibrator = LiveComposite(                                                                                 #Base body
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
            "P_Color == 'pink'", "images/Chibi_Cock_P.png",
            "P_Color == 'brown'", "images/Chibi_Cock_B.png",             
            "P_Color == 'green'", "images/Chibi_Cock_G.png", 
            "True", Null(),
            ),   
#        (0,0), ConditionSwitch(                 
#            "P_Wet", "images/RogueBJFace/Zero_Cock_Wet.png", 
#            "True", Null(),
#            ),       
#        (0,0), ConditionSwitch(    
#            "P_Spunk", "images/RogueBJFace/Zero_Cock_Spunk.png", 
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
            "Partner == 'Rogue'", "Chibi_Mouth_Rogue",             
            "Partner == 'Kitty'", "Chibi_Mouth_Kitty", 
            "Partner == 'Emma'", "Chibi_Mouth_Emma",
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
            "'cockout' not in P_RecentActions", Null(),
            "Trigger2 == 'jackin'", "Chibi_Jackin",
            "Trigger3 == 'hand' or Trigger4 == 'hand'", "Chibi_Handy",             
            "Trigger4 == 'blow'", "Chibi_Sucking", 
            "True", "Chibi_Null", 
            )
#    anchor (0.5,0.5)
#    pos (75,675)

label R_Kissing_Launch(T = Trigger):    
    call Rogue_Hide
    $ Trigger = T
    show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer
    show Rogue at SpriteLoc(StageCenter) zorder RogueLayer:
        ease 0.5 offset (0,0) zoom 2 alpha 1
    return

label R_Kissing_Smooch:   
    call RogueFace("kiss")  
    show Rogue at SpriteLoc(StageCenter) zorder RogueLayer:
        offset (0,0) 
        alpha 1
        ease 0.5 xpos StageCenter zoom 2
        pause 1
        ease 0.5 xpos R_SpriteLoc zoom 1        
    call RogueFace("sexy")  
    return
    
label R_Breasts_Launch(T = Trigger):    
    call Rogue_Hide
    $ Trigger = T
    show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
        ease 0.5 pos (700,-50) zoom 2 offset (0,0) alpha 1 #offset (-100,-200) 
    return
        
label R_Pussy_Launch(T = Trigger):
    call Rogue_Hide    
    $ Trigger = T
    show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
        ease 0.5 pos (700,-400) zoom 2 offset (0,0) alpha 1 #ease 0.5 offset (-100,-550) zoom 2
    return
        
label R_Pos_Reset(Pose = 0):  
    if R_Loc != bg_current:
            return   
    call Rogue_Hide 
    show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
        ease .5 offset (0,0) anchor (0.6, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
    show Rogue zorder RogueLayer:
        offset (0,0) 
        anchor (0.6, 0.0)
        zoom 1  
        xzoom 1 
        yzoom 1
        alpha 1
        pos (R_SpriteLoc,50)
    $ Trigger = Pose
    return
    
label Rogue_Hide:
    if renpy.showing("Rogue_Doggy"):
        call Rogue_Doggy_Reset
    hide Rogue_Doggy       
    hide Rogue_HJ_Animation
    hide Rogue_BJ_Animation
    hide Rogue_TJ_Animation 
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
            "Zero_Loc(Ch_Focus) == 'bg rogue'","PhoneRG",
            "Zero_Loc(Ch_Focus) == 'bg kitty'", "bg_kitty",
            "Zero_Loc(Ch_Focus) == 'bg laura'", "bg_laura",
            "Zero_Loc(Ch_Focus) == 'bg emma'", "bg_emma",
            "Zero_Loc(Ch_Focus) == 'bg classroom'", "bg_class",
            "True", "bg_shower", 
            ) 
        offset (-800,-300)
        zoom 1.5
    contains:
        #girl
        ConditionSwitch(
            "Ch_Focus == 'Rogue'", "Rogue",
            "Ch_Focus == 'Kitty'", "Kitty_Sprite",
            "Ch_Focus == 'Emma'", "Emma_Sprite",
            "Ch_Focus == 'Laura'", "Laura_Sprite",
            "True", Null(),        
            ) 
        offset (290,50)
        zoom 1.1



    
# Rogue's Faces //////////////////////////////////////////////
label RogueFace(Emote = R_Emote, B = R_Blush, M = 0, Mouth = 0, Eyes = 0, Brows = 0):
        # Emote is the chosen emote, B is the lush state, 
        # M is whether the character is in a  manic state         
        $ Emote = R_Emote if Emote == 5 else Emote
        $ B = R_Blush if B == 5 else B
        
        if (R_Forced or "angry" in R_RecentActions) and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "angry"   
        elif R_ForcedCount > 0 and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "sad" 
                
        if Emote == "normal":
                $ R_Mouth = "normal"
                $ R_Brows = "normal"
                $ R_Eyes = "normal"
        elif Emote == "angry":
                $ R_Mouth = "sad"
                $ R_Brows = "angry"
                $ R_Eyes = "sexy"
        elif Emote == "bemused":
                $ R_Mouth = "lipbite"
                $ R_Brows = "sad"
                $ R_Eyes = "squint"
        elif Emote == "closed":
                $ R_Mouth = "lipbite"
                $ R_Brows = "sad"
                $ R_Eyes = "closed"  
        elif Emote == "confused":
                $ R_Mouth = "kiss"
                $ R_Brows = "confused"
                $ R_Eyes = "surprised"
        elif Emote == "kiss":
                $ R_Mouth = "kiss"
                $ R_Brows = "normal"
                $ R_Eyes = "closed"
        elif Emote == "tongue":
                $ R_Mouth = "tongue"
                $ R_Brows = "sad"
                $ R_Eyes = "sexy"
        elif Emote == "manic":
                $ R_Mouth = "grimace"
                $ R_Brows = "sad"
                $ R_Eyes = "manic"
                $ R_Blush = 1
        elif Emote == "sad":
                $ R_Mouth = "sad"
                $ R_Brows = "sad"
                $ R_Eyes = "sexy"
        elif Emote == "sadside":
                $ R_Mouth = "sad"
                $ R_Brows = "sad"
                $ R_Eyes = "side"
        elif Emote == "sexy":
                $ R_Mouth = "lipbite"
                $ R_Brows = "normal"
                $ R_Eyes = "sexy"
        elif Emote == "smile":
                $ R_Mouth = "smile"
                $ R_Brows = "normal"
                $ R_Eyes = "normal"
        elif Emote == "sucking":
                $ R_Mouth = "sucking"
                $ R_Brows = "normal"
                $ R_Eyes = "closed"
        elif Emote == "surprised":
                $ R_Mouth = "surprised"
                $ R_Brows = "surprised"
                $ R_Eyes = "surprised"
        elif Emote == "oh":
                $ R_Mouth = "kiss"
                $ R_Brows = "surprised"
                $ R_Eyes = "surprised"
        elif Emote == "startled":
                $ R_Mouth = "grimace"
                $ R_Brows = "surprised"
                $ R_Eyes = "surprised"
        elif Emote == "down":
                $ R_Mouth = "surprised"
                $ R_Brows = "sad"
                $ R_Eyes = "down"  
        elif Emote == "perplexed":
                $ R_Mouth = "sad"
                $ R_Brows = "confused"
                $ R_Eyes = "normal"
        elif Emote == "sly":
                $ R_Mouth = "grimace"
                $ R_Brows = "normal"
                $ R_Eyes = "squint" 
            
        if M:
                $ R_Eyes = "manic"        
        if B > 1:
                $ R_Blush = 2
        elif B:
                $ R_Blush = 1
        else:
                $ R_Blush = 0
                
        if Mouth:
                $ R_Mouth = Mouth
        if Eyes:
                $ R_Eyes = Eyes
        if Brows:
                $ R_Brows = Brows
                
        return
# End Rogue Faces / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



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
                    "Emotions":
                            call LauraEmotionEditor
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
    if GirlA == "Rogue" or GirlB == "Rogue":            
            if GirlA == "Rogue":
                #If Rogue is lead
                $ Rogue_Arms = 2
                $ RogueLayer = 100
                $ XLoc = 550
                $ YLoc = 100
                $ XZoom = -1.3
            else:
                #If the other girl is lead
                $ Rogue_Arms = 2
                $ RogueLayer = 75
                $ XLoc = 715
                $ YLoc = 100
                $ XZoom = 1.3
            call Rogue_Hide  
            show Rogue at SpriteLoc(XLoc,YLoc) zorder RogueLayer:
                    alpha 1
                    zoom 1
                    xzoom XZoom
                    yzoom 1.3
                    offset (0,0)
                    anchor (0.6, 0.0)
            
    if GirlA == "Kitty" or GirlB == "Kitty":  
            if GirlA == "Kitty":
                $ Kitty_Arms = 1
                $ KittyLayer = 100               
                $ XLoc = 450
                $ YLoc = 100
                $ XZoom = -1.3
            else:
                $ Kitty_Arms = 1
                $ KittyLayer = 75
                $ XLoc = 715
                $ YLoc = 100
                $ XZoom = 1.3
            call Kitty_Hide  
            show Kitty_Sprite at SpriteLoc(XLoc,YLoc) zorder KittyLayer:
                    alpha 1
                    zoom 1
                    xzoom XZoom
                    yzoom 1.3
                    offset (0,0)
                    anchor (0.5, 0.0)
        
    if GirlA == "Emma" or GirlB == "Emma": 
            if GirlA == "Emma":
                $ Emma_Arms = 2
                $ EmmaLayer = 100
                $ XLoc = 500
                $ YLoc = 100
                $ XZoom = 1.3
            else:
                $ Emma_Arms = 2
                $ EmmaLayer = 75
                $ XLoc = 700
                $ YLoc = 100
                $ XZoom = 1.3
            call Emma_Hide  
            show Emma_Sprite at SpriteLoc(XLoc,YLoc) zorder EmmaLayer:
                    alpha 1
                    zoom 1
                    xzoom XZoom
                    yzoom 1.3
                    offset (0,0)
                    anchor (0.5, 0.0)
    
    if GirlA == "Laura" or GirlB == "Laura": 
            if GirlA == "Laura":
                $ Laura_Arms = 1
                $ LauraLayer = 100
                $ XLoc = 500
                $ YLoc = 100
                $ XZoom = 1.3
            else:
                $ Laura_Arms = 1
                $ LauraLayer = 75
                $ XLoc = 700
                $ YLoc = 100
                $ XZoom = 1.3
            call Laura_Hide  
            show Laura_Sprite at SpriteLoc(XLoc,YLoc) zorder LauraLayer:
                    alpha 1
                    zoom 1
                    xzoom XZoom
                    yzoom 1.3
                    offset (0,0)
                    anchor (0.5, 0.0)
    return
    
label QuickReset(Girl=0):
    if "Rogue" == Girl:
        call R_Pos_Reset
    if "Kitty" == Girl:
        call K_Pos_Reset
    if "Emma" == Girl:
        call E_Pos_Reset
    if "Laura" == Girl:
        call L_Pos_Reset
    return
    
label Les_Launch(Girl=0,XLoc=0,YLoc=0,XZoom=0):  
    # Launches the lesbian sex positions
    # Girl is the lead, Partner is the other girl
    # the Loc and Zoom values are generated based on which is which
    if Girl == "Rogue" or Partner == "Rogue":            
            if Girl == "Rogue":
                #If Rogue is lead
                if "unseen" not in R_RecentActions:
                    $ R_Eyes = "side"
                else:     
                    $ R_Eyes = "closed"
                $ Rogue_Arms = 2
                $ RogueLayer = 50
                $ XLoc = 550
                $ YLoc = 100
                $ XZoom = -1.3
            else:
                #If the other girl is lead
                if "unseen" not in R_RecentActions:
                    $ R_Eyes = "side"
                else:     
                    $ R_Eyes = "closed"
                $ Rogue_Arms = 2
                $ RogueLayer = 75
                $ XLoc = 715
                $ YLoc = 100
                $ XZoom = 1.3
            call Rogue_Hide  
            show Rogue at SpriteLoc(XLoc,YLoc) zorder RogueLayer:
                    alpha 1
                    zoom 1
                    xzoom XZoom
                    yzoom 1.3
                    offset (0,0)
                    anchor (0.6, 0.0)
    else:
            # if Rogue is neither of these things, she should be removed from the scene.
            call Rogue_Hide  
            hide Rogue
            
    if Girl == "Kitty" or Partner == "Kitty":  
            if Girl == "Kitty":
                if "unseen" not in K_RecentActions:
                    $ K_Eyes = "leftside"
                else:     
                    $ K_Eyes = "closed"
                $ Kitty_Arms = 1
                $ KittyLayer = 100               
                $ XLoc = 450
                $ YLoc = 100
                $ XZoom = -1.3
            else:
                if "unseen" not in K_RecentActions:
                    $ K_Eyes = "side"
                else:     
                    $ K_Eyes = "closed"
                $ Kitty_Arms = 1
                if Girl == "Rogue" or Partner == "Rogue":
                        $ KittyLayer = 100
                else:
                        $ KittyLayer = 25 
                $ XLoc = 715
                $ YLoc = 100
                $ XZoom = 1.3
            call Kitty_Hide  
            show Kitty_Sprite at SpriteLoc(XLoc,YLoc) zorder KittyLayer:
                    alpha 1
                    zoom 1
                    xzoom XZoom
                    yzoom 1.3
                    offset (0,0)
                    anchor (0.5, 0.0)
    else:
            # if Kitty is neither of these things, she should be removed from the scene.
            call Kitty_Hide  
            hide Kitty_Sprite
        
    if Girl == "Emma" or Partner == "Emma": 
            if Girl == "Emma":
                if "unseen" not in E_RecentActions:
                    $ E_Eyes = "sly"
                else:     
                    $ E_Eyes = "closed"
                $ Emma_Arms = 2
                $ EmmaLayer = 75
                $ XLoc = 500
                $ YLoc = 100
                $ XZoom = 1.3
            else:
                if "unseen" not in E_RecentActions:
                    $ E_Eyes = "side"
                else:     
                    $ E_Eyes = "closed"
                $ Emma_Arms = 2
                $ EmmaLayer = 50
                $ XLoc = 700
                $ YLoc = 100
                $ XZoom = 1.3
            call Emma_Hide  
            show Emma_Sprite at SpriteLoc(XLoc,YLoc) zorder EmmaLayer:
                    alpha 1
                    zoom 1
                    xzoom XZoom
                    yzoom 1.3
                    offset (0,0)
                    anchor (0.5, 0.0)
    else:
            # if Emma is neither of these things, she should be removed from the scene.
            call Emma_Hide  
            hide Emma_Sprite
    
    if Girl == "Laura" or Partner == "Laura": 
            if Girl == "Laura":
                if "unseen" not in L_RecentActions:
                    $ L_Eyes = "leftside"
                else:     
                    $ L_Eyes = "closed"
                $ Laura_Arms = 1
                $ LauraLayer = 75
                $ XLoc = 500
                $ YLoc = 100
                $ XZoom = 1.3
            else:
                if "unseen" not in L_RecentActions:
                    $ L_Eyes = "side"
                else:     
                    $ L_Eyes = "closed"
                $ Laura_Arms = 1
                $ LauraLayer = 50
                $ XLoc = 700
                $ YLoc = 100
                $ XZoom = 1.3
            call Laura_Hide  
            show Laura_Sprite at SpriteLoc(XLoc,YLoc) zorder LauraLayer:
                    alpha 1
                    zoom 1
                    xzoom XZoom
                    yzoom 1.3
                    offset (0,0)
                    anchor (0.5, 0.0)
    else:
            # if Laura is neither of these things, she should be removed from the scene.
            call Laura_Hide  
            hide Laura_Sprite
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
        
    