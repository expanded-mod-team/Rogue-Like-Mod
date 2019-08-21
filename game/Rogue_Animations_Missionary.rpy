#Rogue_Missionary 
image Rogue_Head:               
    LiveComposite(
        (416,610),    
        (0,0), ConditionSwitch(
            "R_DynamicTan[0] and R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_thead_evowet.png",
            "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_head_evowet.png",
            "R_DynamicTan[0] and R_Hair == 'evo' and R_Blush == 2", "images/RogueSprite/Rogue_thead_evo_blush2.png",
            "R_Hair == 'evo' and R_Blush == 2", "images/RogueSprite/Rogue_head_evo_blush2.png",
            "R_DynamicTan[0] and R_Hair == 'evo' and R_Blush", "images/RogueSprite/Rogue_thead_evo_blush.png",
            "R_Hair == 'evo' and R_Blush", "images/RogueSprite/Rogue_head_evo_blush.png",
            "R_DynamicTan[0] and R_Hair == 'evo'", "images/RogueSprite/Rogue_thead_evo.png",
            "R_Hair == 'evo'", "images/RogueSprite/Rogue_head_evo.png",
            "R_DynamicTan[0]", "images/RogueSprite/Rogue_thead_evo.png",
            "True", "images/RogueSprite/Rogue_head_evo.png",
            ),     
        (0,0), ConditionSwitch(
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
        (0,0), ConditionSwitch(  
            # "'mouth' in R_Spunk and R_Gag == 'ringgag'", "images/RogueSprite/Rogue_mouth_ringgag_w.png",                                                                       #Mouths        
            # "R_Gag == 'ringgag'", "images/RogueSprite/Rogue_mouth_ringgag.png",                                                                       #Mouths        
            # "R_Gag == 'ballgag'", "images/RogueSprite/Rogue_mouth_Ballgag.png",                                                                       #Mouths        
            "'mouth' in R_Spunk and R_Mouth == 'sucking'", "images/RogueSprite/Rogue_mouth_sucking_w.png",
            "'mouth' in R_Spunk and R_Mouth == 'surprised'", "images/RogueSprite/Rogue_mouth_sucking_w.png",
            "'mouth' in R_Spunk and R_Mouth == 'sad'", "images/RogueSprite/Rogue_mouth_sad_w.png",
            "'mouth' in R_Spunk and R_Mouth == 'kiss'", "images/RogueSprite/Rogue_mouth_sad_w.png",
            "'mouth' in R_Spunk and R_Mouth == 'smile'", "images/RogueSprite/Rogue_mouth_smile_w.png",
            "'mouth' in R_Spunk and R_Mouth == 'tongue'", "images/RogueSprite/Rogue_mouth_tongue_w.png",
            "R_DynamicTan[0] and 'mouth' in R_Spunk", "images/RogueSprite/Rogue_tmouth_lipbite_w.png",
            "'mouth' in R_Spunk", "images/RogueSprite/Rogue_mouth_lipbite_w.png",
            "R_Mouth == 'normal'", "images/RogueSprite/Rogue_mouth_normal.png",
            "R_DynamicTan[0] and R_Mouth == 'lipbite'", "images/RogueSprite/Rogue_tmouth_lipbite.png",
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
        (0,0), ConditionSwitch(
            "R_Hair == 'newhair' and R_Water", "images/RogueSprite/Rogue_hair_wet_newhair.png",
            "R_Hair == 'newhair'", "images/RogueSprite/Rogue_hair_evo_newhair.png",
            "R_HairColor == 'custom'", Null(),
            "R_Water", "images/RogueSprite/Rogue_Hair" + GetHairColor(R_HairColor) + "_Wet.png",
            "R_Hair == 'evo'", "images/RogueSprite/Rogue_Hair" + GetHairColor(R_HairColor) + "_Evo.png",
            "R_Hair == 'long'", "images/RogueSprite/Rogue_Hair" + GetHairColor(R_HairColor) + "_Long.png",
            "R_Hair == 'wet'", "images/RogueSprite/Rogue_Hair" + GetHairColor(R_HairColor) + "_Wet.png",
            "True", "images/RogueSprite/Rogue_Hair" + GetHairColor(R_HairColor) + "_Evo.png",
            ),
        (0,0), ConditionSwitch(
            "R_Hair == 'newhair'", Null(),
            "R_HairColor != 'custom'", Null(),
            "R_Water", im.MatrixColor("images/RogueSprite/Rogue_HairWhite_Wet.png",im.matrix.tint(float(R_HairCustomColor.red)/255.0, float(R_HairCustomColor.green)/255.0, float(R_HairCustomColor.blue)/255.0)),
            "R_Hair == 'evo'", im.MatrixColor("images/RogueSprite/Rogue_HairWhite_Evo.png",im.matrix.tint(float(R_HairCustomColor.red)/255.0, float(R_HairCustomColor.green)/255.0, float(R_HairCustomColor.blue)/255.0)),
            "R_Hair == 'long'", im.MatrixColor("images/RogueSprite/Rogue_HairWhite_Long.png",im.matrix.tint(float(R_HairCustomColor.red)/255.0, float(R_HairCustomColor.green)/255.0, float(R_HairCustomColor.blue)/255.0)),
            "R_Hair == 'wet'", im.MatrixColor("images/RogueSprite/Rogue_HairWhite_Wet.png",im.matrix.tint(float(R_HairCustomColor.red)/255.0, float(R_HairCustomColor.green)/255.0, float(R_HairCustomColor.blue)/255.0)),
            "True", im.MatrixColor("images/RogueSprite/Rogue_HairWhite_Evo.png",im.matrix.tint(float(R_HairCustomColor.red)/255.0, float(R_HairCustomColor.green)/255.0, float(R_HairCustomColor.blue)/255.0)),
            ),
        (0,0), ConditionSwitch(
            "R_Hair == 'newhair'", Null(),
            "R_HairColorBangs != 'custom2'", Null(),
            "R_Water", im.MatrixColor("images/RogueSprite/Rogue_HairWhite_Wet1.png",im.matrix.tint(float(R_HairCustomColorBangs.red)/255.0, float(R_HairCustomColorBangs.green)/255.0, float(R_HairCustomColorBangs.blue)/255.0)),
            "R_Hair == 'evo'", im.MatrixColor("images/RogueSprite/Rogue_HairWhite_Evo1.png",im.matrix.tint(float(R_HairCustomColorBangs.red)/255.0, float(R_HairCustomColorBangs.green)/255.0, float(R_HairCustomColorBangs.blue)/255.0)),
            "R_Hair == 'long'", im.MatrixColor("images/RogueSprite/Rogue_HairWhite_Long1.png",im.matrix.tint(float(R_HairCustomColorBangs.red)/255.0, float(R_HairCustomColorBangs.green)/255.0, float(R_HairCustomColorBangs.blue)/255.0)),
            "R_Hair == 'wet'", im.MatrixColor("images/RogueSprite/Rogue_HairWhite_Wet1.png",im.matrix.tint(float(R_HairCustomColorBangs.red)/255.0, float(R_HairCustomColorBangs.green)/255.0, float(R_HairCustomColorBangs.blue)/255.0)),
            "True", im.MatrixColor("images/RogueSprite/Rogue_HairWhite_Evo1.png",im.matrix.tint(float(R_HairCustomColorBangs.red)/255.0, float(R_HairCustomColorBangs.green)/255.0, float(R_HairCustomColorBangs.blue)/255.0)),
            ),
        (0,0), ConditionSwitch(
            "'facial' in R_Spunk", "images/RogueSprite/Rogue_facial.png",
            "True", Null(),
            ),     
        )
image Rogue_HairBack:
    LiveComposite(
        (416,610),    
        (0,0), ConditionSwitch(
            "R_Hair == 'newhair'", Null(),
            "R_HairColor == 'custom'", Null(),
            "R_Water or R_Hair == 'evo'", "images/RogueSprite/Rogue_hair" + GetHairColor(R_HairColor) + "_wet.png",
            "R_Hair == 'evo'", "images/RogueSprite/Rogue_hair" + GetHairColor(R_HairColor) + "_evo.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "R_Hair == 'newhair'", Null(),
            "R_HairColor != 'custom'", Null(),
            "R_Water or R_Hair == 'evo'", im.MatrixColor("images/RogueSprite/Rogue_hairWhite_wet.png",im.matrix.tint(float(R_HairCustomColor.red)/255.0, float(R_HairCustomColor.green)/255.0, float(R_HairCustomColor.blue)/255.0)),
            "R_Hair == 'evo'", im.MatrixColor("images/RogueSprite/Rogue_hairWhite_evo.png",im.matrix.tint(float(R_HairCustomColor.red)/255.0, float(R_HairCustomColor.green)/255.0, float(R_HairCustomColor.blue)/255.0)),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "R_Hair == 'newhair'", Null(),
            "R_HairColorBangs != 'custom2'", Null(),
            "R_Water or R_Hair == 'evo'", im.MatrixColor("images/RogueSprite/Rogue_hairWhite_wet1.png",im.matrix.tint(float(R_HairCustomColorBangs.red)/255.0, float(R_HairCustomColorBangs.green)/255.0, float(R_HairCustomColorBangs.blue)/255.0)),
            "R_Hair == 'evo'", im.MatrixColor("images/RogueSprite/Rogue_hairWhite_evo1.png",im.matrix.tint(float(R_HairCustomColorBangs.red)/255.0, float(R_HairCustomColorBangs.green)/255.0, float(R_HairCustomColorBangs.blue)/255.0)),
            "True", Null(),
            ),
        )
#    anchor (0.6, 0.0)
#    zoom .5
# Rogue Sex Sprite ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


image Rogue_SexSprite:            
    LiveComposite(                                                                                 #Base body
        (1120,840),  
        (0,0), ConditionSwitch(                                                        
                #Shows different upper body motion depending on events  
                "not P_Sprite", "Rogue_Sex_Body_Static", 
                "P_Cock == 'anal'", ConditionSwitch( 
                        #if the top's down. . .
                        "Speed >= 3", "Rogue_Sex_Body_Anim3",
                        "Speed >= 2", "Rogue_Sex_Body_Anim2",
                        "Speed", "Rogue_Sex_Body_Anim1",
                        "True", "Rogue_Sex_Body_Static",   
                        ),            
                "P_Cock == 'in'", ConditionSwitch( 
                        #if the top's down. . .
                        "Speed >= 3", "Rogue_Sex_Body_Anim3",
                        "Speed >= 2", "Rogue_Sex_Body_Anim2",
                        "Speed", "Rogue_Sex_Body_Anim1",
                        "True", "Rogue_Sex_Body_Static",   
                        ),             
                "P_Cock == 'foot'", ConditionSwitch( 
                        #if the top's down. . .
                        "Speed >= 2", "Rogue_Sex_Body_FootAnim2",
                        "Speed", "Rogue_Sex_Body_FootAnim1",
                        "True", "Rogue_Sex_Body_FootAnimStatic",   
                        ),            
                "P_Cock == 'out' and Speed >= 2","Rogue_Hotdog_Body_Anim2",                                    
                "True", "Rogue_Sex_Body_Static",           
                ),              
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events            
                "not P_Sprite", "Rogue_Sex_Legs_Static", 
                "P_Cock == 'anal'", ConditionSwitch( 
                        #if the top's down. . .
                        "Speed >= 3", "Rogue_Sex_Legs_Anim3",
                        "Speed >= 2", "Rogue_Sex_Legs_Anim2",
                        "Speed", "Rogue_Sex_Legs_Anim1",
                        "True", "Rogue_Sex_Legs_Static",   
                        ),            
                "P_Cock == 'in'", ConditionSwitch( 
                        #if the top's down. . .
                        "Speed >= 3", "Rogue_Sex_Legs_Anim3",
                        "Speed >= 2", "Rogue_Sex_Legs_Anim2",
                        "Speed", "Rogue_Sex_Legs_Anim1",
                        "True", "Rogue_Sex_Legs_Static",   
                        ),             
                "P_Cock == 'foot'", ConditionSwitch( 
                        #if the top's down. . .
                        "Speed >= 2", "Rogue_Sex_Legs_FootAnim2",
                        "Speed", "Rogue_Sex_Legs_FootAnim1",
                        "True", "Rogue_Sex_Legs_FootAnimStatic",   
                        ),            
                "P_Cock == 'out' and Speed >= 2","Rogue_Hotdog_Legs_Anim2",                                    
                "True", "Rogue_Sex_Legs_Static",           
                ),
        ) 
    align (0.6,0.0)
    pos (650,230)#(750,230)
    zoom 0.7

image Rogue_Sex_Body_Static:
    contains:
            "Rogue_Sex_Body"
    pos (650,230)
            
image Rogue_Sex_Legs_Static:
    contains:
            "Rogue_Sex_Legs"
    pos (650,230)

image Rogue_Sex_Body:
    LiveComposite(                                                                                
        #the torso/head used in the sex pose, referenced by Rogue_SexSprite
        (1120,840),
        (140,-240), "Rogue_HairBack_Sex",                                                                                      #Hair underlayer
        (0,0), ConditionSwitch(                                                                                 #Body Base
            "R_DynamicTan[0]", "images/RogueSex/Rogue_tSex_Body.png",  
            "True", "images/RogueSex/Rogue_Sex_Body.png",             
            ),
        (0,0), ConditionSwitch(   
            "not R_DynamicTan[0] or not R_DynamicTan[3]", Null(),
            "True", AlphaMask("images/RogueSex/Rogue_Sex_Body.png", GetModdedStringTanRogue("3", ".png", "Sex")),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(   
            "not R_DynamicTan[0] or not R_DynamicTan[1]", Null(),
            "True", AlphaMask("images/RogueSex/Rogue_Sex_Body.png", GetModdedStringTanRogue("1", ".png", "Sex")),
            "True", Null(),
            ),
        (140,-240), "Rogue_Head_Sex",  #check positioning (400,-300)
        #Eyes
        # (0,0), ConditionSwitch(                                                                                 #necklace
        #     "R_Neck == 'gold necklace'", "images/RogueSex/Rogue_Sex_Neck_Gold.png",
        #     "R_Neck == 'star necklace'", "images/RogueSex/Rogue_Sex_Neck_Star.png",
        #     "True", Null(),
        #     ),  
        (0,0), ConditionSwitch(                                                                                 #Body Base
            "not R_Pierce", Null(),
            #"R_Pierce", "images/RogueSex/Rogue_Sex_Body_Tits_" + str(R_Pierce) + ".png",
            "R_Pierce == 'barbell'", "images/RogueSex/Rogue_Sex_Body_Tits_Barbell.png",   
            "R_Pierce == 'ring'", "images/RogueSex/Rogue_Sex_Body_Tits_Ring.png",   
            "True", Null(),             
            ), 
        (0,0), ConditionSwitch(        
            "not R_Hose", Null(),     
            "True", GetOutfitString("images/RogueSex/Rogue_Sex_Hose_", R_Hose, ".png"),
            ), 
        (0,0), ConditionSwitch(                                                                                 #tanktop
            "not R_Chest", Null(),        
            "True", GetOutfitString("images/RogueSex/Rogue_Sex_Chest_", R_Chest, ".png"),
            # "R_Chest == 'modded SR7 tank short'", "images/RogueSex/Rogue_Sex_SR7_Tank_Short.png",
            # "R_Chest == 'bra'", "images/RogueSex/Rogue_Sex_Under_Bra.png",
            "True", Null(),            
            ), 
        # (0,0), ConditionSwitch(
        #     "R_BodySuitOff and R_BodySuit != 'classic uniform damaged'", Null(),  
        #     "R_BodySuit == 'classic uniform'", "images/RogueSex/Rogue_Sex_XCatsuit_Top.png",
        #     "R_BodySuit == 'classic uniform damaged'", "images/RogueSex/Rogue_Sex_XCatsuit_Top_Dmg.png",
        #     "True", Null(),                     
        #     ),
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "R_Water", "images/RogueSex/Rogue_Sex_Water_Body.png",   
            "True", Null(),              
            ), 
        (0,0), ConditionSwitch(                                                                         #accessories
            "R_Accessory == 'modded classic belt'", "images/RogueSex/Rogue_Sex_Over_XBelt.png",
            "True", Null(),
            ), 
        (0,0), ConditionSwitch(                                                                                 #Overshirt
            "not R_Over", Null(),
            "True", GetOutfitString("images/RogueSex/Rogue_Sex_Over_", R_Over, ".png"),
            # "R_Over == 'armbinder'", "images/RogueSex/RogueSexArmbinderOvershirt.png",
            # "R_Over == 'modded classic jacket'", "images/RogueSex/Rogue_Sex_Over_XJacket.png",           
            # "R_Over == 'modded SR7 mesh top'", "images/RogueSex/Rogue_Sex_Over_SR7_Mesh_Top.png",           
            # "R_Over == 'modded blue dress'", "images/RogueSex/Rogue_Sex_Bluedress.png",           
            # "R_Over == 'modded red dress'", "images/RogueSex/Rogue_Sex_Reddress.png",           
            "True", Null(), 
            ),  
        (140,-240), "Rogue_Head_Sex",  #check positioning (400,-300)
        #Eyes
        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'belly' in R_Spunk", "images/RogueSex/Rogue_Sex_Spunk_Body.png",   
            "True", Null(),  
            ),  
        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'belly' in R_Spunk", "images/RogueSex/Rogue_Sex_Spunk_Body.png",   
            "True", Null(),  
            ),  
        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'tits' in R_Spunk", "images/RogueSex/Rogue_Sex_Spunk_Tits.png",   
            "True", Null(),  
            ),  
        )

image Rogue_Head_Sex:
    # The head used for the sex pose, referenced by Rogue_Sex_Body
    "Rogue_Head"
    zoom 1.4
    anchor (0.5,0.5)
    #rotate -10
    
image Rogue_HairBack_Sex:
    # The hair behind the head for the sex pose, referenced by Rogue_Sex_Body            
    "Rogue_HairBack"
    zoom 1.4
    anchor (0.5,0.5)   
    #rotate -10         

#image Rogue_Sex_Legs = LiveComposite(  
image Rogue_Sex_Legs:
    LiveComposite(  
        #the legs used in the sex pose, referenced by Rogue_SexSprite
        (1120,840), 
        # (0,0), ConditionSwitch(                                                                                 #Legs Layer
        #     "R_Legs == 'blue skirt'", "images/RogueSex/Rogue_Sex_Skirt_Back.png",   
        #     "True", Null(),                      
        #     ),  
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "R_DynamicTan[0]", "images/RogueSex/Rogue_tSex_Legs.png",   
            "True", "images/RogueSex/Rogue_Sex_Legs.png",              
            ),                                                         #Legs Base
        (0,0), ConditionSwitch(   
            "not R_DynamicTan[0] or not R_DynamicTan[4]", Null(),
            "True", AlphaMask("images/RogueSex/Rogue_Sex_Legs.png", GetModdedStringTanRogue("4", ".png", "Sex")),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(  
            "not R_DynamicTan[0] or not R_DynamicTan[5]", Null(), #hose
            "True", AlphaMask("images/RogueSex/Rogue_Sex_Legs.png", GetModdedStringTanRogue("5", "_Legs.png", "Sex")),
            ),
        (0,0), ConditionSwitch(  
            "not R_DynamicTan[0] or not R_DynamicTan[2]", Null(),
            "True", AlphaMask("images/RogueSex/Rogue_Sex_Legs.png", GetModdedStringTanRogue("2", "_Legs.png", "Sex")),
            "True", Null(),   
            ),
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "R_Water", "images/RogueSex/Rogue_Sex_Water_Legs.png",   
            "True", Null(),              
            ),  
        (0,0), "Rogue_Sex_Anus",                                                                          #Anus Composite 

        (0,0), "Rogue_Sex_Pussy",                                                                         #Pussy Composite

        (0,0), ConditionSwitch(                                                                                 #Panties if up
            "R_PantiesDown or not R_Panties", Null(),     
            "R_Wet", GetOutfitString("images/RogueSex/Rogue_Sex_Panties_", R_Panties, "_Wet.png"),
            "True", GetOutfitString("images/RogueSex/Rogue_Sex_Panties_", R_Panties, ".png"),
            ),  
        (0,0), ConditionSwitch(        
            "not R_Hose", Null(),     
            "True", GetOutfitString("images/RogueSex/Rogue_Sex_Hose_", R_Hose, "_Legs.png"),
            ), 
        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            "not R_Legs", Null(),     
            "R_Wet", GetOutfitString("images/RogueSex/Rogue_Sex_Legs_", R_Legs, "_Legs_Wet.png"),
            "True", GetOutfitString("images/RogueSex/Rogue_Sex_Legs_", R_Legs, "_Legs.png"),
            ),   
        # (0,0), ConditionSwitch(                                                                                 #Over Layer
        #     "R_Over == 'towel'", "images/RogueSex/Rogue_Sex_Towel_Legs.png",
        #     "True", Null(),                    
        #     ),   
        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'belly' in R_Spunk", "images/RogueSex/Rogue_Sex_Spunk_Pelvis.png",   
            "True", Null(),  
            ),  
        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer  
            "not P_Sprite or P_Cock != 'out'", Null(),                    
            "Speed >= 2", "Rogue_Hotdog_Zero_Anim2",
            "Speed", "Rogue_Hotdog_Zero_Anim1",
            "True", "Rogue_Hotdog_Zero_Anim0",   
            ), 
        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer  
            "not P_Sprite or P_Cock != 'foot'", Null(),                    
            "Speed >= 2", "Rogue_Footcock_Zero_Anim2",
            "Speed", "Rogue_Footcock_Zero_Anim1",
            "True", "Rogue_Footcock_Static",   
            ),
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "not Speed", "Rogue_Sex_Feet",  
            "P_Cock == 'anal' or P_Cock == 'in' or P_Cock == 'out'", AlphaMask("Rogue_Sex_Feet", "images/RogueSex/Rogue_Sex_FeetMask.png"), 
            "True", "Rogue_Sex_Feet",            
            ),
        )
    
image Rogue_Sex_Feet:
    LiveComposite(                                                                                          
        #the lower legs used in the sex pose, referenced by Rogue_Sex_Legs
        (1120,840), 
        (0,0), ConditionSwitch(
            "R_DynamicTan[0]", "images/RogueSex/Rogue_tSex_Feet.png",                                                         #Legs Base
            "True", "images/RogueSex/Rogue_Sex_Feet.png",
            ),                                                         #Legs Base
        (0,0), ConditionSwitch(  
            "not R_DynamicTan[0] or not R_DynamicTan[5]", Null(), #hose
            "True", AlphaMask("images/RogueSex/Rogue_Sex_Feet.png", GetModdedStringTanRogue("5", "_Feet.png", "SexFeet")),
            ),
        (0,0), ConditionSwitch(  
            "not R_DynamicTan[0] or not R_DynamicTan[2]", Null(),
            "True", AlphaMask("images/RogueSex/Rogue_Sex_Feet.png", GetModdedStringTanRogue("2", "_Feet.png", "SexFeet")),
            ),
        (0,0), ConditionSwitch(
            "not R_Hose", Null(),     
            "True", GetOutfitString("images/RogueSex/Rogue_Sex_Hose_", R_Hose, "_Feet.png"),
            ),
        (0,0), ConditionSwitch(
            "not R_Legs", Null(),     
            "True", GetOutfitString("images/RogueSex/Rogue_Sex_Legs_", R_Legs, "_Feet.png"),
            ), 
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "R_Water", "images/RogueSex/Rogue_Sex_Water_Feet.png",   
            "True", Null(),              
            ),  
        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            "R_Upskirt", Null(),                               
            # "R_Legs == 'capris'", "images/RogueSex/Rogue_Sex_Feet_Blue.png",
            # "R_Legs == 'black jeans'", "images/RogueSex/Rogue_Sex_Feet_Black.png",
            # "R_Legs == 'yoga pants'", "images/RogueSex/Rogue_Sex_Feet_Yoga.png",
            "True", Null(),                      
            ),   
        )
           
image TestingSolid:
        #this is a blank solid I use to test things.
        contains:
            Solid("#75d7ec", xysize=(1500,1500))
            alpha 0.2
            
#Start Animations for Rogue's Pussy during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Missionary_Pussy_Fucking0:
    # This is the visual for her pussy during the Speed 0 mode (static). 
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "R_DynamicTan[0]", "images/RogueSex/Rogue_tSex_Pussy_Open.png",
                "True", "images/RogueSex/Rogue_Sex_Pussy_Open.png",
                ),
    contains:
            # pubes
            ConditionSwitch(             
                "not R_Pubes", Null(),         
                "True", "images/RogueSex/Rogue_Sex_Pubes_Open.png",  
                ),  
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Sex_Zero_Anim0", "Rogue_Pussy_Open_Mask") 
            
image Rogue_Missionary_Pussy_Fucking1:
    # This is the visual for her pussy during the Speed 1 mode (heading). 
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "R_DynamicTan[0]", "images/RogueSex/Rogue_tSex_Pussy_Open.png",
                "True", "images/RogueSex/Rogue_Sex_Pussy_Open.png",
                ),
    contains:
            # pubes
            ConditionSwitch(             
                "not R_Pubes", Null(),         
                "True", "images/RogueSex/Rogue_Sex_Pubes_Open.png",  
                ),  
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Sex_Zero_Anim1", "Rogue_Pussy_Open_Mask") 

image Rogue_Missionary_Pussy_Fucking2:
    # This is the visual for her pussy during the Speed 2 mode (slow). 
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "R_DynamicTan[0]", "images/RogueSex/Rogue_tSex_Pussy_Fucking.png",
                "True", "images/RogueSex/Rogue_Sex_Pussy_Fucking.png",
                ),
    contains:
            # pubes
            ConditionSwitch(             
                "not R_Pubes", Null(),         
                "True", "images/RogueSex/Rogue_Sex_Pubes_Fucking.png",  
                ),  
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Sex_Zero_Anim2", "Rogue_Missionary_Pussy_Fucking_Mask") 
image Rogue_Missionary_Pussy_Fucking3:  #rename this to 3
    # This is the visual for her pussy during the Speed 3 mode (fast). 
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "R_DynamicTan[0]", "images/RogueSex/Rogue_tSex_Pussy_Fucking.png",
                "True", "images/RogueSex/Rogue_Sex_Pussy_Fucking.png",
                ),
    contains:
            # pubes
            ConditionSwitch(             
                "not R_Pubes", Null(),         
                "True", "images/RogueSex/Rogue_Sex_Pubes_Fucking.png",  
                ),  
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Sex_Zero_Anim3", "Rogue_Missionary_Pussy_Fucking_Mask") 
            
image Rogue_Missionary_Pussy_Fucking_Mask:
        #This is the mask image for Rogue's wide open pussy
        contains:
            "images/RogueSex/Rogue_Sex_Pussy_Mask.png"   

image Rogue_Pussy_Open_Mask:                
        #This is the mask image for Rogue's wide open pussy
        contains:
            "images/RogueSex/Rogue_Sex_Pussy_Mask.png"  
            yoffset 3            
            

image Rogue_Pussy_Spunk_Heading:                
    "images/RogueSex/Rogue_Sex_Spunk_Puss_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8
            
image Rogue_Sex_Pussy:            
    # This is the visual for her pussy during the Speed 0 mode (static).     
    contains:
            # The background plate of her pussy            
            ConditionSwitch(
                "P_Sprite and P_Cock == 'in' and Speed >= 2 and R_DynamicTan[0]", "images/RogueSex/Rogue_tSex_Pussy_Fucking.png",
                "P_Sprite and P_Cock == 'in' and Speed >= 2", "images/RogueSex/Rogue_Sex_Pussy_Fucking.png",
                "P_Sprite and P_Cock == 'in' and Speed and R_DynamicTan[0]", "images/RogueSex/Rogue_tSex_Pussy_Open.png",
                "P_Sprite and P_Cock == 'in' and Speed", "images/RogueSex/Rogue_Sex_Pussy_Open.png",
                "P_Sprite and P_Cock == 'in' and R_DynamicTan[0]", "images/RogueSex/Rogue_tSex_Pussy_Closed.png",
                "P_Sprite and P_Cock == 'in'", "images/RogueSex/Rogue_Sex_Pussy_Closed.png",
                "Trigger == 'lick pussy' and R_DynamicTan[0]", "images/RogueSex/Rogue_tSex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/RogueSex/Rogue_Sex_Pussy_Open.png",
                "True and R_DynamicTan[0]", "images/RogueSex/Rogue_tSex_Pussy_Closed.png",
                "True", "images/RogueSex/Rogue_Sex_Pussy_Closed.png",
                )
    contains:
            ConditionSwitch(   
                "not R_DynamicTan[0] or not R_DynamicTan[4]", Null(),
                "P_Sprite and P_Cock == 'in' and Speed >= 2", AlphaMask("images/RogueSex/Rogue_Sex_Pussy_Fucking.png", GetModdedStringTanRogue("4", ".png", "Sex")),
                "P_Sprite and P_Cock == 'in' and Speed", AlphaMask("images/RogueSex/Rogue_Sex_Pussy_Open.png", GetModdedStringTanRogue("4", ".png", "Sex")),
                "P_Sprite and P_Cock == 'in'", AlphaMask("images/RogueSex/Rogue_Sex_Pussy_Closed.png", GetModdedStringTanRogue("4", ".png", "Sex")),
                "Trigger == 'lick pussy'", AlphaMask("images/RogueSex/Rogue_Sex_Pussy_Open.png", GetModdedStringTanRogue("4", ".png", "Sex")),
                "True", AlphaMask("images/RogueSex/Rogue_Sex_Pussy_Closed.png", GetModdedStringTanRogue("4", ".png", "Sex")),
                ),
    contains:
            ConditionSwitch(  
                "not R_DynamicTan[0] or not R_DynamicTan[5]", Null(), #hose
                "P_Sprite and P_Cock == 'in' and Speed >= 2", AlphaMask("images/RogueSex/Rogue_Sex_Pussy_Fucking.png", GetModdedStringTanRogue("5", "_Legs.png", "Sex")),
                "P_Sprite and P_Cock == 'in' and Speed", AlphaMask("images/RogueSex/Rogue_Sex_Pussy_Open.png", GetModdedStringTanRogue("5", "_Legs.png", "Sex")),
                "P_Sprite and P_Cock == 'in'", AlphaMask("images/RogueSex/Rogue_Sex_Pussy_Closed.png", GetModdedStringTanRogue("5", "_Legs.png", "Sex")),
                "Trigger == 'lick pussy'", AlphaMask("images/RogueSex/Rogue_Sex_Pussy_Open.png", GetModdedStringTanRogue("5", "_Legs.png", "Sex")),
                "True", AlphaMask("images/RogueSex/Rogue_Sex_Pussy_Closed.png", GetModdedStringTanRogue("5", "_Legs.png", "Sex")),
                ),
    contains:
            ConditionSwitch(  
                "not R_DynamicTan[0] or not R_DynamicTan[2]", Null(),
                "P_Sprite and P_Cock == 'in' and Speed >= 2", AlphaMask("images/RogueSex/Rogue_Sex_Pussy_Fucking.png", GetModdedStringTanRogue("2", "_Legs.png", "Sex")),
                "P_Sprite and P_Cock == 'in' and Speed", AlphaMask("images/RogueSex/Rogue_Sex_Pussy_Open.png", GetModdedStringTanRogue("2", "_Legs.png", "Sex")),
                "P_Sprite and P_Cock == 'in'", AlphaMask("images/RogueSex/Rogue_Sex_Pussy_Closed.png", GetModdedStringTanRogue("2", "_Legs.png", "Sex")),
                "Trigger == 'lick pussy'", AlphaMask("images/RogueSex/Rogue_Sex_Pussy_Open.png", GetModdedStringTanRogue("2", "_Legs.png", "Sex")),
                "True", AlphaMask("images/RogueSex/Rogue_Sex_Pussy_Closed.png", GetModdedStringTanRogue("2", "_Legs.png", "Sex")),
                ),    
    contains:
            # The background plate of her pussy            
            ConditionSwitch(    
                "not R_Wet", Null(),  
                "P_Sprite and P_Cock == 'in' and Speed >= 2", "images/RogueSex/Rogue_Sex_WetPussy_F.png",
                "True", "images/RogueSex/Rogue_Sex_WetPussy_C.png",
                )
    contains: 
            #ring piercing
            ConditionSwitch(  
                "R_Pierce != 'ring'", Null(),
                "not P_Sprite or P_Cock != 'in' or Speed <= 1", "images/RogueSex/Rogue_Sex_Pussy_Ring.png",
                "True", "images/RogueSex/Rogue_Sex_Pussy_RingF.png",
                ) 
    contains: 
            #barbell piercing
            ConditionSwitch(  
                "R_Pierce != 'barbell'", Null(),
                "not P_Sprite or P_Cock != 'in' or Speed <= 1", "images/RogueSex/Rogue_Sex_Pussy_Barbell.png",
                "True", "images/RogueSex/Rogue_Sex_Pussy_BarbellF.png",
                )  
    #contains:
    #        ConditionSwitch(
    #        "R_PantiesDown and P_Cock != 'anal' and R_Panties == 'swimsuit3'", "images/RogueSex/Rogue_Sex_Swimsuit3_BottomPush.png",
    #        "True", Null(), 
    #        ),  

    contains:
            # pubes
            ConditionSwitch(    
                "not R_Pubes", Null(),         
                "R_BodySuit and R_BodySuit != 'classic uniform damaged' and not R_BodySuitOff", Null(),
                #"P_Sprite and P_Cock == 'in' and Speed >= 2 and R_HairColor == 'black'", "images/RogueSex/Rogue_Sex_PubesBlack_Fucking.png",
                #"P_Sprite and P_Cock == 'in' and Speed >= 2", "images/RogueSex/Rogue_Sex_Pubes_Fucking.png",
                #"P_Sprite and P_Cock == 'in' and Speed and R_HairColor == 'black'", "images/RogueSex/Rogue_Sex_PubesBlack_Open.png",
                #"P_Sprite and P_Cock == 'in' and Speed", "images/RogueSex/Rogue_Sex_Pubes_Open.png",
                #"P_Sprite and P_Cock == 'in' and R_HairColor == 'black'", "images/RogueSex/Rogue_Sex_PubesBlack_Closed.png", 
                #"P_Sprite and P_Cock == 'in'", "images/RogueSex/Rogue_Sex_Pubes_Closed.png", 
                #"Trigger == 'lick pussy' and R_HairColor == 'black'", "images/RogueSex/Rogue_Sex_PubesBlack_Open.png", 
                #"Trigger == 'lick pussy'", "images/RogueSex/Rogue_Sex_Pubes_Open.png", 
                #"True and R_HairColor == 'black'", "images/RogueSex/Rogue_Sex_PubesBlack_Closed.png",
                #"True", "images/RogueSex/Rogue_Sex_Pubes_Closed.png",
                "R_HairColor == 'blonde' or R_HairColor == 'blondewhite'", "images/RogueSex/Rogue_Sex_Pubes_Blonde.png",
                "R_HairColor == 'black' or R_HairColor == 'blackwhite'", "images/RogueSex/Rogue_Sex_Pubes_Black.png",
                "True", "images/RogueSex/Rogue_Sex_Pubes.png",
                )
    #contains:
    #        ConditionSwitch(
    #        "R_PantiesDown and R_Panties == 'zipper panties'", "images/RogueSex/RogueSexBDPantyOpenTop.png",
    #        "R_PantiesDown and R_Panties == 'zipper panties open'", "images/RogueSex/RogueSexBDPantyOpenTop.png",
    #        "True", Null(), 
    #        ),

    
    contains:
            #Spunk under penis
            ConditionSwitch(    
                "'in' in R_Spunk", "images/RogueSex/Rogue_Sex_Spunk_Puss_Under.png",   
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
                "'in' not in R_Spunk or not P_Sprite or P_Cock != 'in' or not Speed", Null(), 
                "Speed <= 1", "Kitty_Pussy_Spunk_Heading",   
                "True", "images/RogueSex/Rogue_Sex_Spunk_Puss_Over.png",  
                )  
            
    #End Rogue Pussy composite
            
#End Animations for Rogue's Pussy during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Zero's Cock during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Sex_Zero_Anim0:
        #this is Rogue's sex animation, Speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (498,530) #X less is left, Y less is up (498,520)
            zoom 1.4
            
image Rogue_Sex_Zero_Anim1:
        #this is Rogue's sex animation, Speed 1 (heading)
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
            
image Rogue_Sex_Zero_Anim2:
        #this is Rogue's sex animation, Speed 2 (slow)
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
            
image Rogue_Sex_Zero_Anim3:
        #this is Rogue's sex animation, Speed 3 (fast)
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

#Start Animations for Rogue's Legs during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Sex_Legs_Anim1:
        #this is the animation for Rogue's lower body during sex, Speed 1 (heading)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .25
                easein 1 pos (0,-5)
                pause 1
                ease 2.75 pos (0,0)
                repeat 
            
image Rogue_Sex_Legs_Anim2:            
        #this is the animation for Rogue's lower body during sex, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .5 pos (0,-15)
                ease .25 pos (0,-10)
                pause 1
                ease 2.75 pos (0,0)
                repeat 
            
image Rogue_Sex_Legs_Anim3:
        #this is the animation for Rogue's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds   
                pause .15
                easein .15 pos (0,-20)
                ease .10 pos (0,-15) 
                pause .20
                ease 1.4 pos (0,0)
                repeat 
#End Animations for Rogue's Legs during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Rogue's Body during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Sex_Body_Anim1:
        #this is the animation for Rogue's upper body during sex, Speed 1 (heading)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 pos (0,-5)
                pause 1.25
                ease 2.5 pos (0,0)
                repeat 
            
image Rogue_Sex_Body_Anim2:            
        #this is the animation for Rogue's upper body during sex, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .6
                easein .4 pos (0,-10)
                ease .25 pos (0,-5)
                pause 1
                ease 2.75 pos (0,10)
                repeat 
            
image Rogue_Sex_Body_Anim3:
        #this is the animation for Rogue's upper body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds   
                pause .17
                easein .13 pos (0,-20)
                ease .10 pos (0,-15) 
                pause .20
                ease 1.4 pos (0,10)
                repeat 
#End Animations for Rogue's Body during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /            





#Start Animations for Rogue's Pussy during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Rogue_Sex_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(                                                                                             
            "P_Sprite and P_Cock == 'anal' and Speed >= 3", "images/RogueSex/Rogue_Sex_Hole_Open.png",         
            "P_Sprite and P_Cock == 'anal' and Speed >= 2", "images/RogueSex/Rogue_Sex_Hole_Open.png",
            "P_Sprite and P_Cock == 'anal' and Speed", "Rogue_Anal_Heading_missionary",
            "P_Sprite and P_Cock == 'anal'", "Rogue_Anal_Tip", 
            "R_Loose", "images/RogueSex/Rogue_Sex_Hole_Loose.png",   
            "True", "images/RogueSex/Rogue_Sex_Hole_Tight.png", 
            )    
    contains:
            #Spunk under penis
            ConditionSwitch(    
                "'anal' not in R_Spunk", Null(),  
                "P_Sprite and P_Cock != 'anal' and Speed >= 1", "images/RogueSex/Rogue_Sex_Spunk_Anal_Under.png",  
                "P_Sprite and P_Cock != 'anal' and Speed == 1", "Rogue_Anal_Spunk_Heading_Under",
                "True", "images/RogueSex/Rogue_Sex_Spunk_Anal_Closed.png",  
                )  
    contains:
            # The animation of Zero's moving penis, masked by her anus shape
            ConditionSwitch(               
            "not P_Sprite or P_Cock != 'anal'", Null(),                                                                                    
            "Speed >= 3",  AlphaMask("Rogue_Anal_Zero_Anim3", "Rogue_Missionary_Anal_Fucking_Mask"),        
            "Speed >= 2", AlphaMask("Rogue_Anal_Zero_Anim2", "Rogue_Missionary_Anal_Fucking_Mask"),
            "Speed", AlphaMask("Rogue_Anal_Zero_Anim1", "Rogue_Missionary_Anal_Fucking_Mask"),
            "True", AlphaMask("Rogue_Anal_Zero_Anim0", "Rogue_Missionary_Anal_Fucking_Mask"), 
            )    
    contains:
            #Spunk over penis
            ConditionSwitch(    
                "'anal' not in R_Spunk or not P_Sprite or P_Cock != 'anal' or not Speed", Null(),  
                "Speed == 1", "Rogue_Anal_Spunk_Heading_Over",
                "True", "images/RogueSex/Rogue_Sex_Spunk_Anal_Over.png",  
                )  
            
                
image Rogue_Missionary_Anal_Fucking0:
    # This is the visual for her pussy during the Speed 0 mode (static). 
    contains:
            # The background plate of her pussy
            "Rogue_Anal_Tip"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Anal_Zero_Anim0", "Rogue_Missionary_Anal_Fucking_Mask") 
            
image Rogue_Missionary_Anal_Fucking1:
    # This is the visual for her pussy during the Speed 1 mode (heading). 
    contains:
            # The background plate of her pussy
            "Rogue_Anal_Heading_missionary"
#            "images/RogueSex/Rogue_Sex_Hole_Open.png"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Anal_Zero_Anim1", "Rogue_Missionary_Anal_Fucking_Mask") 

image Rogue_Missionary_Anal_Fucking2:
    # This is the visual for her pussy during the Speed 2 mode (slow). 
    contains:
            # The background plate of her pussy
            "images/RogueSex/Rogue_Sex_Hole_Open.png"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Anal_Zero_Anim2", "Rogue_Missionary_Anal_Fucking_Mask") 
            
image Rogue_Missionary_Anal_Fucking3:  
    # This is the visual for her pussy during the Speed 3 mode (fast). 
    contains:
            # The background plate of her pussy
            "images/RogueSex/Rogue_Sex_Hole_Open.png"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Anal_Zero_Anim3", "Rogue_Missionary_Anal_Fucking_Mask") 
            
image Rogue_Missionary_Anal_Fucking_Mask:
        #This is the mask image for Rogue's wide open pussy
        contains:
            "images/RogueSex/Rogue_Sex_Hole_Mask.png"               

image Rogue_Anal_Open_Mask:            
        #This is the mask image for Rogue's wide open pussy
        contains:
            "images/RogueSex/Rogue_Sex_Hole_Mask.png"  
            yoffset 3

image Rogue_Anal_Heading_missionary:                
    "images/RogueSex/Rogue_Sex_Hole_Open.png"
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

image Rogue_Anal_Spunk_Heading_Over:                
    "images/RogueSex/Rogue_Sex_Spunk_Anal_Over.png"
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
image Rogue_Anal_Spunk_Heading_Under:                
    "images/RogueSex/Rogue_Sex_Spunk_Anal_Under.png"
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

image Rogue_Anal_Tip:                
    "images/RogueSex/Rogue_Sex_Hole_Open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
            
#End Animations for Rogue's Pussy during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Zero's Cock during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Anal_Zero_Anim0:
        #this is Rogue's sex animation, Speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,600) #X less is left, Y less is up (498,520)
            zoom 1.4
            
image Rogue_Anal_Zero_Anim1:
        #this is Rogue's sex animation, Speed 1 (heading)
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
            
image Rogue_Anal_Zero_Anim2:
        #this is Rogue's sex animation, Speed 2 (slow)
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
            
image Rogue_Anal_Zero_Anim3:
        #this is Rogue's sex animation, Speed 3 (fast)
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
image Rogue_Hotdog_Zero_Anim0:
        #this is Rogue's sex animation, Speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (498,570) #X less is left, Y less is up
            zoom 1.4
            
image Rogue_Hotdog_Zero_Anim1:
        #this is Rogue's sex animation, Speed 1 (heading)
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

image Rogue_Hotdog_Zero_Anim2:
        #this is Rogue's sex animation, Speed 3 (fast)
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

image Rogue_Hotdog_Body_Anim2:
        #this is the animation for Rogue's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds   
                pause .30
                ease .50 pos (0,-10)
                pause .20
                ease 1 pos (0,0)
                repeat 
                
image Rogue_Hotdog_Legs_Anim2:
        #this is the animation for Rogue's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds   
                pause .20
                ease .50 pos (0,-10)
                pause .20
                ease 1.1 pos (0,0)
                repeat 
                
#End Animations for Zero's Cock during Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Rogue's Legs during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Rogue_Footcock:   
    contains:
            subpixel True
            "Blowcock"
            alpha 0.8
            zoom 0.7
            anchor (0.5,0.5)
            offset (465,70)
            pos (0,0)
    pos (750,230)

image Rogue_Footcock_Static:    
    contains:
            subpixel True
            "Rogue_Footcock"
            pos (392,295)
    pos (750,230)
                
image Rogue_Footcock_Zero_Anim1:
    contains:
            subpixel True
            "Rogue_Footcock"
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
              
image Rogue_Footcock_Zero_Anim2:
    contains:
            subpixel True
            "Rogue_Footcock"
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

transform Rogue_Footcock_Zero_Anim1A():
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
                
transform Rogue_Footcock_Zero_Anim2A():
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
                
transform Rogue_Footcock_StaticA():  
            subpixel True
            offset (0,-5)
            block:
                #Total time, 4 seconds
                pause .5
                ease 1 yoffset 0
                pause 1
                ease 1.50 yoffset -5
                repeat 
            
image Rogue_Sex_Legs_FootAnim1:            
        #this is the animation for Rogue's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
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
                
image Rogue_Sex_Legs_FootAnim2:            
        #this is the animation for Rogue's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
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
                
image Rogue_Sex_Legs_FootAnimStatic:            
        #this is the animation for Rogue's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
        pos (750,230)
           
transform Rogue_Sex_Legs_FootAnim1A():            
        #this is the animation for Rogue's lower body during Footjobs, Speed 2 (slow)
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
                
transform Rogue_Sex_Legs_FootAnim2A():            
        #this is the animation for Rogue's lower body during Footjobs, Speed 2 (slow)
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
                
transform Rogue_Sex_Legs_FootAnimStaticA():            
        #this is the animation for Rogue's lower body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                ease 1 yoffset -5
                pause 1
                ease 1.50 yoffset 0
                repeat 
                
#End Animations for Rogue's Legs during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Rogue's Body during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
            
image Rogue_Sex_Body_FootAnim1:            
        #this is the animation for Rogue's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Body"
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
  
image Rogue_Sex_Body_FootAnim2:            
        #this is the animation for Rogue's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Body"
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
                
image Rogue_Sex_Body_FootAnimStatic:            
        #this is the animation for Rogue's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            pos (0,0) #X less is left, Y less is up
        pos (750,230)
 
transform Rogue_Sex_Body_FootAnim1A():            
        #this is the animation for Rogue's upper body during Footjobs, Speed 2 (slow)
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
  
transform Rogue_Sex_Body_FootAnim2A():            
        #this is the animation for Rogue's upper body during Footjobs, Speed 2 (slow)
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
                
transform Rogue_Sex_Body_FootAnimStaticA():            
        #this is the animation for Rogue's upper body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                ease 1 yoffset -5
                pause 1
                ease 1.50 yoffset 0
                repeat 
#End Animations for Rogue's Body during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     Sex Launch/Reset
label Rogue_Sex_Launch(Line = "solo"): 
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
    if renpy.showing("Rogue_SexSprite"):
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
    show Rogue_SexSprite zorder 150
#    show Rogue_SexSprite zorder 150:
#        pos (750,230)

    with dissolve
    return
    
# End Rogue Sex pose Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    
###ANON MOD CODE BLOCK STOP ######
