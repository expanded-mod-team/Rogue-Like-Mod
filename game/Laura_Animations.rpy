# Basic character Sprites

image Laura_Sprite:
    LiveComposite(                
        (402,965), 
        (0,0), "Laura_Sprite_HairBack", 
        (0,0), ConditionSwitch(            
            #panties down back        
            "not L_Panties or not L_PantiesDown or (L_Legs and L_Legs != 'skirt' and not L_Upskirt)", Null(), 
            "L_Panties == 'wolvie panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Back.png",   
            "L_Panties == 'bikini bottoms'", "images/LauraSprite/Laura_Sprite_Panties_Bikini_Back.png",   
            "True", "images/LauraSprite/Laura_Sprite_Panties_Lace_Back.png",   
            ), 
        (0,0), ConditionSwitch(
            #backside of arms
            "Laura_Arms == 2", "images/LauraSprite/Laura_Sprite_Arm_Back2.png",   
            "True", "images/LauraSprite/Laura_Sprite_Arm_Back1.png", #if L_Arms == 1 
            ),     
#        (0,0), ConditionSwitch(
#            #arms wristband
#            "L_Arms == 'wrists'", "images/LauraSprite/Laura_Sprite_Wrist_Right.png", # one hand up
#            "True", Null(),     
#            ), 
        (0,0), ConditionSwitch(
            #L Over under
            "L_Uptop and L_Over == 'jacket'", "images/LauraSprite/Laura_Sprite_Jacket_Back_Up.png", # one hand up
            "L_Over == 'jacket'", "images/LauraSprite/Laura_Sprite_Jacket_Back.png", # one hand up
            "True", Null(),     
            ), 
        #body
        (0,0), "images/LauraSprite/Laura_Sprite_Body.png",
        
        #shifted here
        (0,0), ConditionSwitch(
            #arms midlayer
            "Laura_Arms == 2", "images/LauraSprite/Laura_Sprite_Arm_Mid2.png",         # one hand up
            "True", "images/LauraSprite/Laura_Sprite_Arm_Mid1.png", #if L_Arms == 1   # Crossed        
            ),  
        # tits
        (0,0), "images/LauraSprite/Laura_Sprite_Tits.png", 
        (0,0), ConditionSwitch(
            #Water effect 
            "L_Water and Laura_Arms == 1", "images/LauraSprite/Laura_Sprite_Water1.png",   
            "L_Water", "images/LauraSprite/Laura_Sprite_Water2.png",   
            "True", Null(),        
            ),       
        (0,0), ConditionSwitch(
            #arms wristband
            "L_Arms == 'wrists' and Laura_Arms == 2", "images/LauraSprite/Laura_Sprite_Wrist2.png", # one hand up
            "L_Arms == 'wrists'", "images/LauraSprite/Laura_Sprite_Wrist1.png", # one hand up
            "True", Null(),     
            ),   
        #shifted here
        
        (145,560), ConditionSwitch(    #(225,560)                                                                     
            #Personal Wetness            
            "not L_Wet", Null(),
            "L_Legs and L_Legs != 'skirt' and not L_Upskirt", Null(),   
            "L_Panties and not L_PantiesDown and L_Wet <= 1", Null(),   
            "L_Wet == 1", ConditionSwitch( #Wet = 1
                    "L_Panties and L_PantiesDown", AlphaMask("Wet_Drip","Laura_Drip_MaskP"),  
                    "L_Legs and L_Legs != 'skirt'", AlphaMask("Wet_Drip","Laura_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip","Laura_Drip_Mask"), #only plays if nothing is in the way
                    ),
            "True", ConditionSwitch( #Wet = 2+
                    "L_Panties and L_PantiesDown", AlphaMask("Wet_Drip2","Laura_Drip_MaskP"),
                    "L_Legs and L_Legs != 'skirt'", AlphaMask("Wet_Drip2","Laura_Drip_MaskP"),
                    "L_Panties", AlphaMask("Wet_Drip","Laura_Drip_Mask"), #"Wet_Drip2",# 
                    "True", AlphaMask("Wet_Drip2","Laura_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (145,560), ConditionSwitch(    #(225,560)                                                                     
            #dripping spunk            
            "'in' not in L_Spunk and 'anal' not in L_Spunk", Null(),
            "L_Legs and L_Legs != 'skirt' and not L_Upskirt", Null(),   
            "L_Panties and not L_PantiesDown and L_Wet <= 1", Null(),   
            "True", ConditionSwitch( #Wet = 2+
                    "L_Panties and L_PantiesDown", AlphaMask("Spunk_Drip2","Laura_Drip_MaskP"),
#                    "L_Legs and L_Legs != 'skirt'", AlphaMask("Spunk_Drip2","Laura_Drip_MaskP"), #add if pantes have down art
                    "L_Panties", AlphaMask("Spunk_Drip","Laura_Drip_Mask"), #"Wet_Drip2",# 
                    "True", AlphaMask("Spunk_Drip2","Laura_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (0,0), ConditionSwitch(
            #pubes 
            "L_Pubes", "images/LauraSprite/Laura_Sprite_Pubes.png",   
            "True", Null(),        
            ),      
        (0,0), ConditionSwitch(
            #nude lower piercings        
            "not L_Pierce", Null(),  
            "L_Panties and not L_PantiesDown", Null(), 
            "L_Legs != 'skirt' and L_Legs and not L_Upskirt", Null(), #skirt if wearing a skirt
            "L_Pierce == 'barbell'", "images/LauraSprite/Laura_Sprite_Barbell_Pussy.png",  
            "L_Pierce == 'ring'", "images/LauraSprite/Laura_Sprite_Ring_Pussy.png",  
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(
            #stockings    
            "L_Hose == 'stockings' or L_Hose == 'stockings and garterbelt'", "images/LauraSprite/Laura_Sprite_Stockings.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "not L_Hose", Null(),
            "'modded' in L_Hose", "images/LauraSprite/Laura_Sprite_Hose_[L_Hose].png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #garterbelt    
            "L_Hose == 'stockings and garterbelt' or L_Hose == 'garterbelt'", "images/LauraSprite/Laura_Sprite_Garters.png",
            "True", Null(),
            ),              
        (0,0), ConditionSwitch(
            #panties    
            "not L_Panties", Null(),
            "L_PantiesDown", ConditionSwitch(                   
                    #if the panties are down
                    "not L_Legs or L_Upskirt or L_Legs == 'skirt'", ConditionSwitch(                   
                            #if she's wearing a skirt or nothing else                    
                            "L_Panties == 'wolvie panties' and L_Wet", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Down_W.png", 
                            "L_Panties == 'wolvie panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Down.png",                             
                            "L_Panties == 'lace panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace_Down.png", 
                            "L_Panties == 'bikini bottoms'", "images/LauraSprite/Laura_Sprite_Panties_Bikini_Down.png", 
                            "True", "images/LauraSprite/Laura_Sprite_Panties_Lace_Down.png", #fix
                            ),         
                    "True", Null(),
                    ),                    
            "True", ConditionSwitch(                
                    #if she's got panties and they are not down
                    "L_Wet", ConditionSwitch(   
                        #if she's  wet                            
                        "L_Panties == 'wolvie panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_W.png",
                        "L_Panties == 'lace panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace.png", 
                        "L_Panties == 'bikini bottoms'", "images/LauraSprite/Laura_Sprite_Panties_Bikini.png", 
                        "True", "images/LauraSprite/Laura_Sprite_Panties_Leather.png", 
                        ),
                    "True", ConditionSwitch(   
                        #if she's not wet                            
                        "L_Panties == 'wolvie panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie.png",
                        "L_Panties == 'lace panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace.png", 
                        "L_Panties == 'bikini bottoms'", "images/LauraSprite/Laura_Sprite_Panties_Bikini.png", 
                        "True", "images/LauraSprite/Laura_Sprite_Panties_Leather.png", 
                        ),                    
                    ),    
            ),            
        (0,0), ConditionSwitch(
            #pants    
            "not L_Legs", Null(),
            "L_Upskirt", ConditionSwitch(                
                        #if the skirt's up or pants down 
                        "L_Legs == 'skirt'", "images/LauraSprite/Laura_Sprite_Skirt_Up.png", 
                        "True", Null(),                       
                        ),                    
            "True", ConditionSwitch(                
                    #if it's the ring pericings
                    "L_Wet", ConditionSwitch(   
                        #if she's not wet
                        "L_Legs == 'leather pants'", "images/LauraSprite/Laura_Sprite_Pants_Leather.png",  
                        "L_Legs == 'mesh pants'", "images/LauraSprite/Laura_Sprite_Pants_Mesh.png",   
#                        "L_Legs == 'yoga pants'", "images/LauraSprite/Laura_Sprite_Pants_YogaWet.png",       
                        "L_Legs == 'skirt'", "images/LauraSprite/Laura_Sprite_Skirt.png", 
                        "True", Null(),
                        ),                    
                    "True", ConditionSwitch(   
                        #if she's wet
                        "L_Legs == 'leather pants'", "images/LauraSprite/Laura_Sprite_Pants_Leather.png",   
                        "L_Legs == 'mesh pants'", "images/LauraSprite/Laura_Sprite_Pants_Mesh.png",  
#                        "L_Legs == 'yoga pants'", "images/LauraSprite/Laura_Sprite_Pants_Yoga.png",       
                        "L_Legs == 'skirt'", "images/LauraSprite/Laura_Sprite_Skirt.png", 
                        "True", Null(),
                        ),                    
                    ),                  
            ),    
        (0,0), ConditionSwitch(
            #clothed lower piercings         
            "L_Legs == 'skirt'", Null(),
            "L_Pierce == 'barbell'", ConditionSwitch(   
                    #if it's the barbell pericings 
                    "L_Legs and not L_Upskirt", "images/LauraSprite/Laura_Sprite_Barbell_PussyC.png",  
                    "L_Panties and not L_PantiesDown", "images/LauraSprite/Laura_Sprite_Barbell_PussyC.png", 
                    "True", Null(),
                    ),    
            "L_Pierce == 'ring'", ConditionSwitch(   
                    #if it's the ring pericings
                    "L_Legs and not L_Upskirt", "images/LauraSprite/Laura_Sprite_Ring_PussyC.png",  
                    "L_Panties and not L_PantiesDown", "images/LauraSprite/Laura_Sprite_Ring_PussyC.png", 
                    "True", Null(),
                    ),
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(
            #Personal Wetness            
            "not L_Wet", Null(),
            "L_Legs and L_Wet <= 1", Null(),
            "L_Legs == 'skirt'", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Wetness.png",       #L_Wet >1
            ),     
        (0,0), ConditionSwitch(
            #pussy spunk 
            "L_Legs and not L_Upskirt", Null(),
            "'in' in L_Spunk or 'anal' in L_Spunk", "images/LauraSprite/Laura_Sprite_Spunk_Pussy.png",
            "True", Null(), 
            ),  
        #where arms and tits were before
        (0,0), ConditionSwitch(
            #nude peircings      
            "not L_Pierce", Null(),  
            "L_Pierce == 'barbell'", "images/LauraSprite/Laura_Sprite_Barbell_Tits.png",   
            "L_Pierce == 'ring'", "images/LauraSprite/Laura_Sprite_Ring_Tits.png",               
            "True", Null(),              
            ),    
        (0,0), ConditionSwitch(               
            #neck            
            "L_Neck == 'leash choker'", "images/LauraSprite/Laura_Sprite_Neck_Leash.png",       
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(                                                                        
            #Chest layer
            "L_Uptop", ConditionSwitch(
                    # if top is up. . .
                    "L_Chest == 'leather bra'", "images/LauraSprite/Laura_Sprite_Bra_Leather_Up.png", 
                    "L_Chest == 'wolvie top'", "images/LauraSprite/Laura_Sprite_Top_Wolvie_Up.png",   
                    "L_Chest == 'bikini top'", "images/LauraSprite/Laura_Sprite_Top_Bikini_Up.png",   
                    "L_Chest == 'corset'", "images/LauraSprite/Laura_Sprite_Top_Corset_Up.png",   
                    "L_Chest == 'lace corset'", "images/LauraSprite/Laura_Sprite_Top_Corset_Lace_Up.png",   
                    "True", Null(),     
                    ),     
            "L_Chest == 'leather bra'", "images/LauraSprite/Laura_Sprite_Bra_Leather.png", 
            "L_Chest == 'wolvie top'", "images/LauraSprite/Laura_Sprite_Top_Wolvie.png",   
            "L_Chest == 'bikini top'", "images/LauraSprite/Laura_Sprite_Top_Bikini.png",   
            "L_Chest == 'corset'", "images/LauraSprite/Laura_Sprite_Top_Corset.png",   
            "L_Chest == 'lace corset'", "images/LauraSprite/Laura_Sprite_Top_Corset_Lace.png",   
            "True", Null(),              
            ),     

        (0,0), ConditionSwitch(
            #L Over
            "L_Uptop", ConditionSwitch(
                    # if top is up. . .
                    "L_Over == 'jacket' and Laura_Arms == 2", "images/LauraSprite/Laura_Sprite_Jacket_A2_Up.png", # one hand up
                    "L_Over == 'jacket'", "images/LauraSprite/Laura_Sprite_Jacket_A1_Up.png", # one hand up
#                    "L_Over == 'towel'", "images/LauraSprite/Laura_Sprite_Towel.png",
                    "True", Null(),     
                    ),                
            "L_Over == 'jacket' and Laura_Arms == 2", "images/LauraSprite/Laura_Sprite_Jacket_A2.png", # one hand up
            "L_Over == 'jacket'", "images/LauraSprite/Laura_Sprite_Jacket_A1.png", # one hand up
            "L_Over == 'towel'", "images/LauraSprite/Laura_Sprite_Towel.png",
            "True", Null(),     
            ),         
        (0,0), ConditionSwitch(                                                                        
            #clothed peircings        
            "not L_Pierce or (not L_Over and not L_Chest)", Null(),  
            "L_Over == 'jacket'", Null(),
            "L_Pierce == 'barbell'",  "images/LauraSprite/Laura_Sprite_Barbell_TitsC.png", 
            "L_Pierce == 'ring'", "images/LauraSprite/Laura_Sprite_Ring_TitsC.png", 
            "True", Null(), 
            ),   
                
        (0,0), ConditionSwitch(
            #belly spunk 
            "'belly' in L_Spunk", "images/LauraSprite/Laura_Sprite_Spunk_Belly.png",
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(
            #breast spunk      
            "'tits' in L_Spunk", "images/LauraSprite/Laura_Sprite_Spunk_Tits.png",  
            "True", Null(),  
            ),   
        #Head
#        (0,0), "Laura_Sprite_Head", #(55,0)
        (0,0), ConditionSwitch(
            # head
            "renpy.showing('Laura_BJ_Animation')", Null(),  
            "True", "Laura_Sprite_Head",   
            ),         
        (0,0), ConditionSwitch(
            #arms toplayer
            "Laura_Arms == 2", "images/LauraSprite/Laura_Sprite_Arm_Left2.png", # one hand up
            "True", Null(),     
            ), 
        (0,0), ConditionSwitch(
            #Water effect 
            "L_Water and Laura_Arms == 2", "images/LauraSprite/Laura_Sprite_Water2top.png",  
            "True", Null(),     
            ), 
        (0,0), ConditionSwitch(
            #arms wristband
            "Laura_Arms == 2 and L_Arms == 'wrists'", "images/LauraSprite/Laura_Sprite_Wrist_Left2.png", # one hand up
            "True", Null(),     
            ), 
        (0,0), ConditionSwitch(
            #jacket arm toplayer
            "L_Over == 'jacket' and Laura_Arms == 2", "images/LauraSprite/Laura_Sprite_Jacket_A2Top.png", # one hand up
            "True", Null(),     
            ), 
        (0,0), ConditionSwitch(
            #claws
            "Laura_Arms == 2 and L_Claws", "images/LauraSprite/Laura_Sprite_Claws2.png", # one hand up
            "True", Null(),     
            ), 
        
        (0,0), ConditionSwitch( 
            #hand spunk 
            "Laura_Arms == 2 or 'hand' not in L_Spunk", Null(),  
            "True", "images/LauraSprite/Laura_Sprite_Spunk_Hand.png",   
            ),  
#        (0,0), ConditionSwitch(                                                                         #Props
#            "not L_Held or Laura_Arms != 2", Null(), 
#            "Laura_Arms == 2 and L_Held == 'phone'", "images/LauraSprite/Laura_held_phone.png",
#            "Laura_Arms == 2 and L_Held == 'dildo'", "images/LauraSprite/Laura_held_dildo.png",
#            "Laura_Arms == 2 and L_Held == 'vibrator'", "images/LauraSprite/Laura_held_vibrator.png",
#            "Laura_Arms == 2 and L_Held == 'panties'", "images/LauraSprite/Laura_held_panties.png",
#            "True", Null(), 
#            ),        
        (0,0), ConditionSwitch(
            #UI tool for When Laura is masturbating using Trigger3 actions
            "Trigger == 'lesbian' or not Trigger3 or Ch_Focus != 'Laura'", Null(),
            
            #this is not a lesbian thing, and a trigger is set, and Laura is the primary. . .
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_LSelf",  
            "Trigger3 == 'fondle breasts'", ConditionSwitch(                                                                      
                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeLeftBreast_L", 
                        #When zero is working the right breast, fondle left
                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeRightBreast_L",   
                        #When zero is working the left breast, fondle right
                    "True", "GirlGropeBothBreast_L",
                        #else, fondle both
                    ),  
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast_L",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy_L",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy_L",
            "Trigger3 == 'vibrator anal'", "VibratorAnal_L",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy_L",            
            "True", Null(),             
            ),                        
        (0,0), ConditionSwitch(  
            #UI tool for Trigger5(Threesome masutrbation) actions
            "not Trigger5 or Trigger4 != 'masturbation' or Ch_Focus == 'Laura'", Null(), 
            
            #Laura is not primary, and T4 is masturbation, and a T5 is selected
            "Trigger5 == 'fondle pussy' and Trigger != 'sex' and L_Lust >= 70", "GirlFingerPussy_L",
            "Trigger5 == 'fondle pussy'", "GirlGropePussy_L",            
            "Trigger5 == 'fondle breasts'", "GirlGropeRightBreast_L",
            "Trigger5 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger5 == 'vibrator pussy'", "VibratorPussy",
            "Trigger5 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger5 == 'vibrator anal'", "VibratorAnal",
            "Trigger5 == 'vibrator anal insert'", "VibratorPussy",            
            "True", Null(), 
            ),                              
        (0,0), ConditionSwitch( 
            #UI tool for Trigger1(primary) actions
            #Laura is primary and a sex trigger is active
            "not Trigger or Ch_Focus != 'Laura'", Null(),            
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast_L",
            "Trigger == 'fondle thighs'", "GropeThigh_L",            
            "Trigger == 'fondle breasts'", "GropeLeftBreast_L",
            "Trigger == 'suck breasts'", "LickRightBreast_L",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_L",
            "Trigger == 'fondle pussy'", "GropePussy_L",
            "Trigger == 'lick pussy'", "Lickpussy_L",
            "Trigger == 'vibrator pussy'", "VibratorPussy_L",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy_L",
            "Trigger == 'vibrator anal'", "VibratorAnal_L",
            "Trigger == 'vibrator anal insert'", "VibratorPussy_L",            
            "True", Null(), 
            ),            
        (0,0), ConditionSwitch(                
            #UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus != 'Laura'", Null(),
            
            #Laura is primary and an offhand trigger is active            
            "Trigger2 == 'fondle breasts'", ConditionSwitch(                                                                      
                    "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast_L", 
                        #When zero is sucking on the right breast, fondle left
                    "True", "GropeRightBreast_L",
                        #else, fondle right
                    ),  
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast_L",       
                #When sucking right breast, vibrator left            
            "Trigger2 == Trigger", Null(),
                #When both triggers are the same, do nothing              
            "Trigger2 == 'suck breasts'", "LickLeftBreast_L",        
            "Trigger2 == 'fondle pussy'", "GropePussy_L",
            "Trigger2 == 'lick pussy'", "Lickpussy_L",       
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast_L",
            "Trigger2 == 'vibrator pussy'", "VibratorPussy_L",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy_L",
            "Trigger2 == 'vibrator anal'", "VibratorAnal_L",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy_L",            
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(  
            #UI tool for Trigger4(Threesome) actions (ie Rogue's hand on her)
            "not Trigger4 or Ch_Focus != 'Laura'", Null(),
            
            # There is a threesome trigger set and Laura is the target of it
            "Trigger4 == 'fondle pussy' and Trigger != 'sex' and L_Lust >= 70", "GirlFingerPussy_L",
            "Trigger4 == 'fondle pussy'", "GirlGropePussy_L",            
            "Trigger4 == 'lick pussy'", "Lickpussy_L",
            "Trigger4 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_L", 
            "Trigger4 == 'suck breasts'", "LickRightBreast_L",      
            "Trigger4 == 'fondle breasts'", ConditionSwitch( 
                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeLeftBreast_L", #When zero is working the right breast, fondle left                                                  
#                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeRightBreast_L",  #When zero is working the left breast, fondle right                                         
#                    "Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts'", "GirlGropeRightBreast_L", #When zero is working the left breast, fondle right 
                    "True", "GirlGropeRightBreast_L",#else, fondle right
                    ),       
            "Trigger4 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger4 == 'vibrator pussy'", "VibratorPussy",
            "Trigger4 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger4 == 'vibrator anal'", "VibratorAnal",
            "Trigger4 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),             
            ),
        (0,0), ConditionSwitch(             
            #UI tool for Trigger3(lesbian) actions (ie Rogue's hand on her when Laura is secondary)
            "Trigger != 'lesbian' or Ch_Focus == 'Laura' or not Trigger3", Null(),            
            
            # If there is a Trigger3 and Laura is not the focus
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and L_Lust >= 70", "GirlFingerPussy_L",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_L",            
            "Trigger3 == 'lick pussy'", "Lickpussy_L",
            "Trigger3 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_L", 
            "Trigger3 == 'suck breasts'", "LickRightBreast_L",            
            "Trigger3 == 'fondle breasts'", ConditionSwitch( 
                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeLeftBreast_L",                    
                        #When zero is working the right breast, fondle left                                                  
                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeRightBreast_L", 
                        #When zero is working the left breast, fondle right                                         
                    "Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts'", "GirlGropeLeftBreast_L", 
                        #When zero is working the right breast, fondle left 
                    "True", "GirlGropeRightBreast_L",                    
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
    yoffset 15            
    zoom .75                

image Laura_Sprite_HairBack: 
    ConditionSwitch(
            #hair back 
            "not L_Hair", Null(),
            "renpy.showing('Laura_BJ_Animation')", Null(), 
#            "renpy.showing('Laura_SexSprite')", "images/LauraSex/Laura_Sprite_Hair_Long_UnderSex.png",
            "L_HairColor and L_Hair == 'wet' or L_Water", im.MatrixColor("images/LauraSprite/Laura_Sprite_HairWhite_Wet_Under.png",im.matrix.tint(float(L_HairCustomColor.red)/255.0, float(L_HairCustomColor.green)/255.0, float(L_HairCustomColor.blue)/255.0)),
            "L_Hair == 'wet' or L_Water", "images/LauraSprite/Laura_Sprite_Hair_Wet_Under.png",
            "L_HairColor and L_Hair", im.MatrixColor("images/LauraSprite/Laura_Sprite_HairWhite_Long_Under.png",im.matrix.tint(float(L_HairCustomColor.red)/255.0, float(L_HairCustomColor.green)/255.0, float(L_HairCustomColor.blue)/255.0)),
            "L_Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Under.png",   
            "True", Null(),        
            ),   
#    "images/LauraSprite/Laura_Sprite_Hair_Long_Under.png"       
    anchor (0.6, 0.0)                
    zoom .5                   
    
image Laura_Sprite_Head:            
    LiveComposite(
        (806,806),      
        (0,0), ConditionSwitch(
                # hair behind face
                "L_HairColor and renpy.showing('Laura_SexSprite')", im.MatrixColor("images/LauraSex/Laura_Sprite_HairWhite_Long_UnderSex.png",im.matrix.tint(float(L_HairCustomColor.red)/255.0, float(L_HairCustomColor.green)/255.0, float(L_HairCustomColor.blue)/255.0)),
                "renpy.showing('Laura_SexSprite')", "images/LauraSex/Laura_Sprite_Hair_Long_UnderSex.png", 
                "True", Null(),                        
                ),         
        (0,0), ConditionSwitch(
                # Face background plate
                "L_Blush == 2", "images/LauraSprite/Laura_Sprite_Head_Blush2.png", 
                "L_Blush", "images/LauraSprite/Laura_Sprite_Head_Blush.png",  
                "True", "images/LauraSprite/Laura_Sprite_Head.png",                        
                ),        
        (0,0), ConditionSwitch(#chin spunk
            "'chin' not in L_Spunk", Null(),
            "renpy.showing('Laura_BJ_Animation') and Speed >= 2", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Spunk_Chin.png",            
            ),                
        (0,0), ConditionSwitch(#Mouths 
            "renpy.showing('Laura_BJ_Animation')", "images/LauraSprite/Laura_Sprite_Mouth_SuckingBJ.png", #and Speed >= 2
            "L_Mouth == 'normal'", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png",
            "L_Mouth == 'lipbite'", "images/LauraSprite/Laura_Sprite_Mouth_Lipbite.png",
            "L_Mouth == 'sucking'", "images/LauraSprite/Laura_Sprite_Mouth_Sucking.png",            
            "L_Mouth == 'kiss'", "images/LauraSprite/Laura_Sprite_Mouth_Kiss.png",
            "L_Mouth == 'sad'", "images/LauraSprite/Laura_Sprite_Mouth_Sad.png",
            "L_Mouth == 'smile'", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png",
            "L_Mouth == 'surprised'", "images/LauraSprite/Laura_Sprite_Mouth_Surprised.png",            
            "L_Mouth == 'tongue'", "images/LauraSprite/Laura_Sprite_Mouth_Tongue.png",                
            "L_Mouth == 'grimace'", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png",              
            "L_Mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Mouth_Smirk.png",                    
#            "L_Mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png",         
            "True", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png",
            ),         
        (0,0), ConditionSwitch(#Mouth spunk 
            "'mouth' not in L_Spunk", Null(),
            "renpy.showing('Laura_BJ_Animation')", "images/LauraSprite/Laura_Sprite_Spunk_MouthSuck.png", #and Speed >= 2
            "L_Mouth == 'normal'", "images/LauraSprite/Laura_Sprite_Spunk_MouthNeutral.png",
            "L_Mouth == 'lipbite'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmirk.png",
            "L_Mouth == 'sucking'", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",            
            "L_Mouth == 'kiss'", "images/LauraSprite/Laura_Sprite_Spunk_MouthKiss.png",
            "L_Mouth == 'sad'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSad.png",
            "L_Mouth == 'smile'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmile.png",
            "L_Mouth == 'surprised'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSad.png",            
            "L_Mouth == 'tongue'", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",                
            "L_Mouth == 'grimace'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmile.png",              
            "L_Mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmirk.png",      
            "True", "images/LauraSprite/Laura_Sprite_Spunk_MouthNeutral.png",
            ),                                                        
        (0,0), ConditionSwitch(                                                                       
            #brows
            "L_Blush >= 2", ConditionSwitch(
                    "L_Brows == 'normal'", "images/LauraSprite/Laura_Sprite_Brows_Normal_B.png",
                    "L_Brows == 'angry'", "images/LauraSprite/Laura_Sprite_Brows_Angry_B.png",
                    "L_Brows == 'sad'", "images/LauraSprite/Laura_Sprite_Brows_Sad_B.png",
                    "L_Brows == 'surprised'", "images/LauraSprite/Laura_Sprite_Brows_Surprised_B.png",        
                    "L_Brows == 'confused'", "images/LauraSprite/Laura_Sprite_Brows_Confused_B.png",
                    "True", "images/LauraSprite/Laura_Sprite_Brows_Normal_B.png",
                    ),
            "True", ConditionSwitch(
                    "L_Brows == 'normal'", "images/LauraSprite/Laura_Sprite_Brows_Normal.png",
                    "L_Brows == 'angry'", "images/LauraSprite/Laura_Sprite_Brows_Angry.png",
                    "L_Brows == 'sad'", "images/LauraSprite/Laura_Sprite_Brows_Sad.png",
                    "L_Brows == 'surprised'", "images/LauraSprite/Laura_Sprite_Brows_Surprised.png",        
                    "L_Brows == 'confused'", "images/LauraSprite/Laura_Sprite_Brows_Confused.png",
                    "True", "images/LauraSprite/Laura_Sprite_Brows_Normal.png",
                    ),
            ),        
        (0,0), "Laura Blink",     #Eyes    
        (0,0), ConditionSwitch(                
            #Hair mid
            "L_Over == 'jacket'", Null(),            
            "renpy.showing('Laura_Sex_Animation')", Null(),     
            "L_Hair == 'wet' or L_Water", Null(),
            "L_HairColor and L_Hair", im.MatrixColor("images/LauraSprite/Laura_Sprite_HairWhite_Long_Mid.png",im.matrix.tint(float(L_HairCustomColor.red)/255.0, float(L_HairCustomColor.green)/255.0, float(L_HairCustomColor.blue)/255.0)),
            "L_Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Mid.png",
            "True", Null(),
            ),           
#        (0,0), ConditionSwitch(
#            #Face Water
#            "not L_Water", Null(),
#            "True", "images/LauraSprite/Laura_Sprite_Wet_Head.png",
#            ),  
        (0,0), ConditionSwitch(                                                                         
            #Hair over
            "not L_Hair or L_HairColor", Null(),
            "renpy.showing('Laura_SexSprite')", "images/LauraSex/Laura_Sprite_Hair_Long_OverSex.png",
            "L_Hair == 'wet' or L_Water", "images/LauraSprite/Laura_Sprite_Hair_Wet_Over.png",
            "L_Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Over.png",
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                         
            #Hair over
            "not L_Hair or not L_HairColor", Null(),
            "renpy.showing('Laura_SexSprite')", im.MatrixColor("images/LauraSex/Laura_Sprite_HairWhite_Long_OverSex.png",im.matrix.tint(float(L_HairCustomColor.red)/255.0, float(L_HairCustomColor.green)/255.0, float(L_HairCustomColor.blue)/255.0)),
            "L_Hair == 'wet' or L_Water", im.MatrixColor("images/LauraSprite/Laura_Sprite_HairWhite_Wet_Over.png",im.matrix.tint(float(L_HairCustomColor.red)/255.0, float(L_HairCustomColor.green)/255.0, float(L_HairCustomColor.blue)/255.0)),
            "L_Hair", im.MatrixColor("images/LauraSprite/Laura_Sprite_HairWhite_Long_Over.png",im.matrix.tint(float(L_HairCustomColor.red)/255.0, float(L_HairCustomColor.green)/255.0, float(L_HairCustomColor.blue)/255.0)),
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(
            #Hair Water
            "not L_Water", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Head_Wet.png",
#            "True", "images/LauraSprite/Laura_Sprite_Hair_Wet.png",
            ),
        (0,0), ConditionSwitch(
            #facial spunk               
            "'hair' in L_Spunk", "images/LauraSprite/Laura_Sprite_Spunk_Facial2.png",  
            "'facial' in L_Spunk", "images/LauraSprite/Laura_Sprite_Spunk_Facial1.png",            
            "True", Null(),            
            ),  
        )                
    anchor (0.6, 0.0)                
    zoom .5                      

image Laura Blink:            
    ConditionSwitch(
    "L_Eyes == 'sexy'", "images/LauraSprite/Laura_Sprite_Eyes_Squint.png",
    "L_Eyes == 'side'", "images/LauraSprite/Laura_Sprite_Eyes_Side.png",
    "L_Eyes == 'surprised'", "images/LauraSprite/Laura_Sprite_Eyes_Surprised.png",
    "L_Eyes == 'normal'", "images/LauraSprite/Laura_Sprite_Eyes_Normal.png",    
    "L_Eyes == 'stunned'", "images/LauraSprite/Laura_Sprite_Eyes_Stunned.png",
    "L_Eyes == 'down'", "images/LauraSprite/Laura_Sprite_Eyes_Down.png",
    "L_Eyes == 'closed'", "images/LauraSprite/Laura_Sprite_Eyes_Closed.png",
    "L_Eyes == 'leftside'", "images/LauraSprite/Laura_Sprite_Eyes_Leftside.png",
    "L_Eyes == 'manic'", "images/LauraSprite/Laura_Sprite_Eyes_Normal.png",
    "L_Eyes == 'squint'", "Laura_Squint",
    "True", "images/LauraSprite/Laura_Sprite_Eyes_Normal.png", 
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/LauraSprite/Laura_Sprite_Eyes_Closed.png"
    .25
    repeat                

image Laura_Squint:       
    "images/LauraSprite/Laura_Sprite_Eyes_Normal.png"            
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/LauraSprite/Laura_Sprite_Eyes_Squint.png"
    .25
    repeat                         
            
            

image Laura_Drip_Mask:
    #This is the mask for her drip pattern
    contains:
        "images/LauraSprite/Laura_Sprite_WetMask.png"      
        offset (-145,-560)#(-225,-560)

image Laura_Drip_MaskP:
    #This is the mask for her drip pattern in panties down mode
    contains:
        "images/LauraSprite/Laura_Sprite_WetMaskP.png"      
        offset (-145,-560)#(-225,-560)
            
# End Laura Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /






# Start Laura Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Laura Sex element //////////////////////////////////////////////////////////////////////////// / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /   

image Laura_SexSprite:
    #core sex animation   
    contains:
        ConditionSwitch(                                                              
            # Laura's upper body
            "P_Cock == 'in'", ConditionSwitch(                                                               
                    # If during sex
                    "Speed == 1", "Laura_Sex_Body_S1",#heading
                    "Speed == 2", "Laura_Sex_Body_S2",#slow
                    "Speed == 3", "Laura_Sex_Body_S3",#fast
                    "Speed >= 4", "Laura_Sex_Body_S4",#cumming
                    "True",       "Laura_Sex_Body_S0",#Static
                    ),
            "P_Cock == 'anal'", ConditionSwitch(                                                              
#                    # If during Anal
                    "Speed == 1", "Laura_Sex_Body_A1",#heading
                    "Speed == 2", "Laura_Sex_Body_A2",#slow
                    "Speed == 3", "Laura_Sex_Body_A3",#fast
                    "Speed >= 4", "Laura_Sex_Body_A4",#cumming
                    "True",       "Laura_Sex_Body_A0",#Static
                    ),
            "True", ConditionSwitch(                                                              
                    # If neither
                    "not P_Sprite","Laura_Sex_Body_H0",#Static
                    "Speed == 1", "Laura_Sex_Body_H1",#slow
                    "Speed == 4", "Laura_Sex_Body_H0",#cumming
                    "Speed >= 2", "Laura_Sex_Body_H2",#fast
                    "True",       "Laura_Sex_Body_H0",#Static
                    ),
            )
    contains:
        ConditionSwitch(                                                               
            # Laura's lower body
            "P_Cock == 'in'", ConditionSwitch(                                                               
                    # If during sex
                    "Speed == 1", "Laura_Sex_Legs_S1",#heading
                    "Speed == 2", "Laura_Sex_Legs_S2",#slow
                    "Speed == 3", "Laura_Sex_Legs_S3",#fast
                    "Speed >= 4", "Laura_Sex_Legs_S4",#cumming
                    "True", "Laura_Sex_Legs_S0",#Static
                    ),
            "P_Cock == 'anal'", ConditionSwitch(                                                              
                    # If during Anal
                    "Speed == 1", "Laura_Sex_Legs_A1",#heading
                    "Speed == 2", "Laura_Sex_Legs_A2",#slow
                    "Speed == 3", "Laura_Sex_Legs_A3",#fast
                    "Speed >= 4", "Laura_Sex_Legs_A4",#cumming
                    "True", "Laura_Sex_Legs_A0",#Static
                    ),
            "True", ConditionSwitch(                                                               
                    # If neither
                    "not P_Sprite","Laura_Sex_Legs_H0",#Static
                    "Speed == 1", "Laura_Sex_Legs_H1",#heading
                    "Speed == 4", "Laura_Sex_Legs_H0",#cumming
                    "Speed >= 2", "Laura_Sex_Legs_H2",#slow
                    "True", "Laura_Sex_Legs_H0",#Static
                    ),
            )    
    zoom .6 #0.6
    transform_anchor True
    anchor (.5,.5)
#    rotate -30
    
image Laura_Sex_HairBack:
    #Hair underlay
    "Laura_Sprite_HairBack"
    transform_anchor True
    zoom 1.8
    anchor (0.5, 0.5)
    rotate 10
    pos (800,100)
  
image Laura_Sex_Head:
    #Hair underlay
    "Laura_Sprite_Head"
    transform_anchor True
    zoom 1.8
    anchor (0.5, 0.5)
    rotate 10
    pos (800,100)
                    


image Laura_Sex_Body:                                                                        
    #Her torso for the sex pose
    contains:
            "Laura_Sex_HairBack"        
    contains:
            # hand
            "images/LauraSex/Laura_Sex_Hand.png"
    contains:
            # Over under layer
        ConditionSwitch(   
            "not L_Over", Null(), 
            "L_Uptop", ConditionSwitch(   
                    #if uptop                       
                    "L_Over == 'jacket'", "images/LauraSex/Laura_Sex_Jacket_Back_Up.png",
                    "True", Null(),
                    ),                
            "True", ConditionSwitch(
                    #if not uptop        
                    "L_Over == 'jacket'", "images/LauraSex/Laura_Sex_Jacket_Back.png",
                    "True", Null(),
                    ),    
            )
    contains:
            # body
            "images/LauraSex/Laura_Sex_Body.png"
    contains:
            # piercings tits
        ConditionSwitch(   
            "not L_Pierce", Null(),
            "L_Pierce == 'barbell'", "images/LauraSex/Laura_Sex_Barbell_Tits.png", 
            "L_Pierce == 'ring'", "images/LauraSex/Laura_Sex_Ring_Tits.png", 
            "True", Null(), 
            )
    contains:
            # Chest clothing layer
        ConditionSwitch(    
            "L_Neck == 'leash choker'", "images/LauraSex/Laura_Sex_Leash.png", 
            "True", Null(),  
            )
    contains:
            # garters
        ConditionSwitch(    
            "L_Hose == 'stockings and garterbelt' or L_Hose == 'garterbelt'", "images/LauraSex/Laura_Sex_Garter.png", 
            "True", Null(),  
            )
    contains:
            # Chest clothing layer
        ConditionSwitch(    
            "not L_Chest", Null(),              
            "L_Uptop",ConditionSwitch(  
                    #if the top is up. . .
                    "not L_Chest", Null(),  
                    "L_Chest == 'leather bra'", "images/LauraSex/Laura_Sex_Bra_Leather_Up.png", 
                    "L_Chest == 'wolvie top'", "images/LauraSex/Laura_Sex_Top_Wolvie_Up.png", 
                    "L_Chest == 'corset'", "images/LauraSex/Laura_Sex_Corset_Up.png",   
                    "L_Chest == 'lace corset'", "images/LauraSex/Laura_Sex_Corset_Lace_Up.png",   
                    "L_Chest == 'bikini top'", "images/LauraSex/Laura_Sex_Top_Bikini_Up.png",  
#                    "L_Chest == 'sports bra'", "images/LauraSex/Laura_Sex_Bra_Sports_Up.png",  
#                    "L_Chest == 'lace bra'", "images/LauraSex/Laura_Sex_Bra_Lace_Up.png",  
                    "True", Null(),  
                    ),     
            # else. . .
            "L_Chest == 'leather bra'", "images/LauraSex/Laura_Sex_Bra_Leather.png", 
            "L_Chest == 'wolvie top'", "images/LauraSex/Laura_Sex_Top_Wolvie.png", 
            "L_Chest == 'corset'", "images/LauraSex/Laura_Sex_Corset.png",   
            "L_Chest == 'lace corset'", "images/LauraSex/Laura_Sex_Corset_Lace.png",   
            "L_Chest == 'bikini top'", "images/LauraSex/Laura_Sex_Top_Bikini.png",  
#            "L_Chest == 'sports bra'", "images/LauraSex/Laura_Sex_Bra_Sports.png",  
#            "L_Chest == 'lace bra'", "images/LauraSex/Laura_Sex_Bra_Lace.png",  
            "True", Null(),  
            )
    contains:
            # piercings tits over clothes
        ConditionSwitch(   
            "not L_Pierce or L_Uptop", Null(),
            "L_Pierce == 'barbell'", "images/LauraSex/Laura_Sex_Barbell_Tits_C.png", 
            "L_Pierce == 'ring'", "images/LauraSex/Laura_Sex_Ring_Tits_C.png", 
            "True", Null(), 
            )
    contains:
            # Over clothing layer
        ConditionSwitch(   
            "not L_Over", Null(), 
            "L_Uptop", ConditionSwitch(   
                    #if uptop                       
                    "L_Over == 'jacket'", "images/LauraSex/Laura_Sex_Jacket_Up.png",
#                    "L_Over == 'towel'", "images/LauraSex/Laura_Sex_Towel_Up.png",
                    "True", Null(),
                    ),                
            "True", ConditionSwitch(
                    #if not uptop        
                    "L_Over == 'jacket'", "images/LauraSex/Laura_Sex_Jacket.png",
#                    "L_Over == 'towel'", "images/LauraSex/Laura_Sex_Towel.png",
                    "True", Null(),
                    ),    
            )
    contains:
            # spunk
        ConditionSwitch(    
            "'belly' in L_Spunk", "images/LauraSex/Laura_Sex_Spunk_Belly.png", 
            "True", Null(),
            ) 
    contains:
            # spunk on tits
            ConditionSwitch(    
                "'tits' not in L_Spunk", Null(),
                "True", "images/LauraSex/Laura_Sex_Spunk_Tits.png",
                )     
    contains:
            "Laura_Sex_Head"
    transform_anchor True
    zoom .9 #1 
    offset (55,55)
#    rotate 30
#end Laura Body base

image Laura_Sex_Legs:                                                                        
    #Her Legs during sex             
    contains:
            # legs under
        ConditionSwitch(    
            "L_Legs == 'skirt'", "images/LauraSex/Laura_Sex_Skirt_Back.png",  
            "True", Null(),
            )
#    contains:
#            # spunk
#        ConditionSwitch(    
#            "'anal' in L_Spunk or 'in' in L_Spunk", "images/LauraSex/Laura_Spunk_Sex.png", 
#            "True", Null(),
#            )
    contains:
            # Legs base
        ConditionSwitch(    
            "P_Cock == 'foot'", "images/LauraSex/Laura_Sex_Legs_Foot.png", 
            "True", "images/LauraSex/Laura_Sex_Legs_High.png", 
            )
    contains:
            # anus
        ConditionSwitch(    
            "P_Cock == 'anal' and Speed > 1", "images/LauraSex/Laura_Sex_Anus_L.png", #and speed above heading?
            "P_Cock == 'anal' and Speed > 0", "images/LauraSex/Laura_Sex_Anus_M.png", #and speed above heading?
            "'anal' in L_Spunk", "images/LauraSex/Laura_Sex_Anus_M.png", # If it's full. . .
            "True", "images/LauraSex/Laura_Sex_Anus_S.png", 
            )  
    contains:
            # anal spunk
        ConditionSwitch(    
            "'anal' not in L_Spunk", Null(),
            "P_Cock == 'anal' and Speed > 1", "images/LauraSex/Laura_Sex_Spunk_Anal_U.png", #speed above heading?
            "True", "images/LauraSex/Laura_Sex_Spunk_Anal.png", 
            ) 
    contains:
            # pussy
        ConditionSwitch(    
            "P_Cock == 'in' and Speed > 1", "images/LauraSex/Laura_Sex_Pussy_Open.png", #and speed above heading?
            "P_Cock == 'in' and Speed > 0", "images/LauraSex/Laura_Sex_Pussy_Mid.png", #and speed heading?
            "True", "images/LauraSex/Laura_Sex_Pussy_Closed.png", 
            )  
    contains:
            # pussy wetness
        ConditionSwitch(    
            "not L_Wet", Null(),
            "True", "images/LauraSex/Laura_Sex_Wet.png", 
            ) 
    contains:
            # pussy spunk
        ConditionSwitch(    
            "'in' not in L_Spunk", Null(),
            "P_Cock == 'in' and Speed > 1", "images/LauraSex/Laura_Sex_Spunk_Pussy_Open.png", #and speed above heading?
            "True", "images/LauraSex/Laura_Sex_Spunk_Pussy.png", 
            ) 
    contains:
            # pubes
        ConditionSwitch(    
            "not L_Pubes", Null(),
            "P_Cock == 'in' and Speed > 1", "images/LauraSex/Laura_Sex_Pubes_Open.png", #and speed above heading?
            "P_Cock == 'in' and Speed > 0", "images/LauraSex/Laura_Sex_Pubes_Mid.png", #and speed heading?
            "True", "images/LauraSex/Laura_Sex_Pubes_Closed.png", 
            )  
    contains:
            # piercings
        ConditionSwitch(    
            "L_Pierce == 'barbell' and P_Cock == 'in' and Speed > 1", "images/LauraSex/Laura_Sex_Barbell_Pussy_O.png", #and speed above heading?
            "L_Pierce == 'barbell'", "images/LauraSex/Laura_Sex_Barbell_Pussy.png", 
            "L_Pierce == 'ring' and P_Cock == 'in' and Speed > 1", "images/LauraSex/Laura_Sex_Ring_Pussy_O.png", #and speed above heading?
            "L_Pierce == 'ring'", "images/LauraSex/Laura_Sex_Ring_Pussy.png",
            "True", Null(), 
            )       
    contains:
            # panties
        ConditionSwitch(    
            "L_PantiesDown", Null(),
#            "L_Panties == 'wolvie panties' and L_Wet", "images/LauraSex/Laura_Sex_Panties_Sport_SW.png", 
            "L_Panties == 'bikini bottoms'", "images/LauraSex/Laura_Sex_Panties_Bikini.png", 
            "L_Panties == 'wolvie panties'", "images/LauraSex/Laura_Sex_Panties_Wolvie.png", 
            "L_Panties == 'lace panties'", "images/LauraSex/Laura_Sex_Panties_Lace.png", 
            "L_Panties", "images/LauraSex/Laura_Sex_Panties_Black.png", 
            "True", Null(),
            )         
    contains:
            # hose base layer
        ConditionSwitch(    
            "P_Cock == 'foot' and (L_Hose == 'stockings and garterbelt' or L_Hose == 'stockings')", "images/LauraSex/Laura_Sex_Stockings_Base_Foot.png", 
            "L_Hose == 'stockings and garterbelt' or L_Hose == 'stockings'", "images/LauraSex/Laura_Sex_Stockings_Base_Up.png", 
            "True", Null(),
            )
    contains:
            # hose base layer
        ConditionSwitch(    
            "not L_Hose", Null(),
            "not 'modded' in L_Hose", Null(),
            "P_Cock == 'foot'", "images/LauraSex/Laura_Sex_Hose_[L_Hose]_Base_Foot.png", 
            "True", "images/LauraSex/Laura_Sex_Hose_[L_Hose]_Base_Up.png", 
            # "True", Null(),
            )
    contains:
            # legs
        ConditionSwitch(    
            "L_Legs == 'skirt'", "images/LauraSex/Laura_Sex_Skirt.png", 
            "L_Upskirt", Null(),
            "L_Legs == 'leather pants' and P_Cock == 'foot'", "images/LauraSex/Laura_Sex_Pants_Base_Foot.png", 
            "L_Legs == 'leather pants'", "images/LauraSex/Laura_Sex_Pants_Base_Up.png", 
            "L_Legs == 'mesh pants' and P_Cock == 'foot'", "images/LauraSex/Laura_Sex_Pants_Mesh_Base_Foot.png", 
            "L_Legs == 'mesh pants'", "images/LauraSex/Laura_Sex_Pants_Mesh_Base_Up.png", 
            "True", Null(),
            )
    contains:
            # piercings
        ConditionSwitch(    
#            "L_Panties and L_PantiesDown", Null(), #don't show if panties are down
#            "L_Legs == 'skirt' or (L_Legs and L_Upskirt)", Null(), #don't show if pants are down
            "L_Pierce == 'barbell'", "images/LauraSex/Laura_Sex_Barbell_Pussy_C.png", 
            "L_Pierce == 'ring'", "images/LauraSex/Laura_Sex_Ring_Pussy_C.png",
            "True", Null(), 
            ) 
#    contains:
#            # Over
#        ConditionSwitch(    
#            "L_Over == 'nighty'", "images/LauraSex/Laura_Sex_Nighty_Pussy.png", 
#            "True", Null(),
#            )
    contains:
            # Feet
        ConditionSwitch(    
            "P_Cock == 'foot'", "Laura_Footjob_Foot", 
            "True", "Laura_Sex_Foot", 
            )
    transform_anchor True
    zoom 1 
#    rotate 30
#    offset (0,0)
# End Laura Legs base


image Laura_Sex_Foot:
    #her vertical foot in the sex poses
#    contains:
#            # base
#            "images/LauraSex/Laura_Sex_FootHigh.png"
    contains:
            # hose/foot
        ConditionSwitch(    
            "L_Hose == 'stockings and garterbelt' or L_Hose == 'stockings'", "images/LauraSex/Laura_Sex_Stockings_Up.png", 
            "True", "images/LauraSex/Laura_Sex_FootHigh.png" #base
            )              
    contains:
            # legs
        ConditionSwitch(    
            "L_Upskirt", Null(),
            "L_Legs == 'leather pants' or L_Legs == 'mesh pants'", "images/LauraSex/Laura_Sex_Pants_Up.png", 
            "True", Null(),
            )     
        xoffset  -2 #this shouldn't be needed, but otherwise there's a gap between the knee and leg. 
    transform_anchor True
    zoom 1 
#    alpha 0.2
    pos (988,-553)#(988,-553)

image Laura_Footjob_Foot:
    #her movable foot in the footjob poses
    contains:
            # hose/base
        ConditionSwitch(    
            "L_Hose == 'stockings and garterbelt' or L_Hose == 'stockings'", "images/LauraSex/Laura_Sex_Stockings_Foot.png", 
            "True", "images/LauraSex/Laura_Sex_Foot.png"
            )              
    contains:
            # legs
        ConditionSwitch(    
            "L_Upskirt", Null(),
            "L_Legs == 'leather pants' or L_Legs == 'mesh pants'", "images/LauraSex/Laura_Sex_Pants_Foot.png", 
            "True", Null(),
            )      
    transform_anchor True
    zoom 1 

image Laura_CockRef:
    "images/LauraSex/Laura_Sex_Cocktest.png"
    alpha 0.8
   
   
# Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Laura_SexMask:                    
    transform_anchor True
    contains:
        "images/LauraSex/Laura_Sex_MaskPussyX.png"
        pos (200,303)#(0,0)#(-300,-300) #303
        anchor (.5,.5)
    zoom 1 
    anchor (0.5,0.5)
                    
# Start S0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Laura_Sex_Body_S0:                                                                        
    #Her Body in the sex pose, static
    contains:
        "Laura_Sex_Body"      
        subpixel True       
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 0.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat

image Laura_Sex_Legs_S0:
    # Her Legs in the Sex pose, static
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2s
                pause 0.1
                ease 0.5 ypos -5 #in -25
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat                    
    contains:
            AlphaMask("Laura_Sex_Zero_Anim_S0", "Laura_SexMask")
            subpixel True
            pos (525,465)
            block:#total 2s
                pause 0.1
                ease 0.5 ypos 460 #in 470
                easeout 0.5 ypos 461 #471
                easein 0.9 ypos 465 #out 475                 
                repeat
    # End Legs Sex static
                    
image Laura_Sex_Zero_Anim_S0:
    #this is the cock for Laura's sex animation, Speed0 (static)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        alpha 0.8
        pos (125,170)#125,75
        block: #total 4s
                ease 2 ypos 115#-50
                easeout .5 ypos 120#60
                easein 1.5 ypos 170
                repeat
    
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
                    
# End S0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Start S1 (Heading) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Laura_Sex_Body_S1:                                                                        
    #Her Body in the sex pose, heading
    contains:
        "Laura_Sex_Body"      
        subpixel True       
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 0.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat

image Laura_Sex_Legs_S1:
    # Her Legs in the Sex pose, heading
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2s
                pause 0.1
                ease 0.5 ypos -5 #in -25
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat                    
    contains:
            AlphaMask("Laura_Sex_Zero_Anim_S1", "Laura_SexMask")
            subpixel True
            pos (525,485)
            block:#total 2s
                pause 0.1
                ease 0.5 ypos 480 #in 450
                easeout 0.5 ypos 481 #455
                easein 0.9 ypos 485 #out    #475              
                repeat
    # End Legs Sex heading
                    
image Laura_Sex_Zero_Anim_S1:
    #this is the cock for Laura's sex animation, Speed1 (heading)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,115)#125,75
        block: #total 2s
                ease .5 ypos 90#-50
                easeout .5 ypos 100#60
                easein 1 ypos 115
                repeat
    
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
                    
# End S1 (Heading) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Start S2 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Laura_Sex_Body_S2:                                                                        
    #Her Body in the sex pose, slow
    contains:
        "Laura_Sex_Body"      
        subpixel True       
        pos (0,10) #top (0,-10)
        block:
            pause 0.3
            ease 0.3 ypos -10 #in
            pause 0.20
            ease 1.70 ypos 10 #out
            repeat

image Laura_Sex_Legs_S2:
    # Her Legs in the Sex pose, slow
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:
                pause 0.25
                ease 0.3 ypos -25 #in
                easeout 0.45 ypos -20
                easein 1.5 ypos 0 #out
                repeat                    
    contains:
            AlphaMask("Laura_Sex_Zero_Anim_S2", "Laura_SexMask")
            subpixel True
            pos (525,478)
            block:
                pause 0.25
                ease 0.3 ypos 453 #in
                easeout 0.45 ypos 458 
                easein 1.5 ypos 478 #out                    
                repeat
    contains:
            # spunk
            ConditionSwitch(    
                "'in' not in L_Spunk", Null(),
                "True", "images/LauraSex/Laura_Sex_Spunk_Anal_O.png", 
                ) 
            subpixel True                
            pos (-15,-105) #top
            block:
                pause 0.25
                ease 0.3 ypos -130 #in 
                easeout 0.45 ypos -125
                easein 1.5 ypos -105 #out
                repeat         
    # End Legs Sex slow
                    
image Laura_Sex_Zero_Anim_S2:
    #this is the cock for Laura's sex animation, Speed 1 (slow)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,75)#130,75
        block: #total 2.5s
                ease .5 ypos -50#-50
                easeout 1.5 ypos 60#100
                easein .5 ypos 75
                repeat
    
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
# End S2 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


# Start S3 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Laura_Sex_Body_S3:                                                                        
    #Her Body in the sex pose, fast
    contains:
        "Laura_Sex_Body"      
        subpixel True       
        pos (0,10) #top (0,-10)
        block:#total 2.5s > 1.75 > 1.2
            pause 0.1
            ease 0.2 ypos -50 #in -10
            pause 0.2
            ease .7 ypos 10 #out
            repeat

image Laura_Sex_Legs_S3:
    # Her Legs in the Sex pose, slow
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -45 #in -25
                easeout 0.45 ypos -40 #-50
                easein .5 ypos 0 #out
                repeat                    
    contains:
            AlphaMask("Laura_Sex_Zero_Anim_S3", "Laura_SexMask")
            subpixel True
            pos (525,478) #(525,475)
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos 433 #in 450
                easeout 0.45 ypos 438 #455
                easein .5 ypos 478 #out                  
                repeat
#            block:#total 2.5s > 1.75 > 1.2
#                pause 0.05
#                ease 0.2 ypos 430 #in 450
#                easeout 0.45 ypos 435 #455
#                easein .5 ypos 475 #out                  
#                repeat
    contains:
            # spunk
            ConditionSwitch(    
                "'in' not in L_Spunk", Null(),
                "True", "images/LauraSex/Laura_Sex_Spunk_Anal_O.png", 
                ) 
            subpixel True                
            pos (-15,-105) #top(-15,-105)   
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -150 #in -45
                easeout 0.45 ypos -145 #-40
                easein .5 ypos -105 #out
                repeat     
    # End Legs Sex fast
                    
image Laura_Sex_Zero_Anim_S3:
    #this is the cock for Laura's sex animation, Speed3 (fast)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,75)#130,75
        block: #total 2.5s > 1.75 > 1.2
                ease .2 ypos -70#-50
                easeout .5 ypos 0#60
                easein .5 ypos 75
                repeat
    
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True                    
# End S3 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Start S4 (cumming) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Laura_Sex_Body_S4:                                                                        
    #Her Body in the sex pose, cumming
    contains:
        "Laura_Sex_Body"      
        subpixel True       
        pos (0,10) #top (0,10)
        block:#total 2.5s > 1.75 > 1.2
            pause 0.1
            ease 0.2 ypos 0 #in
            pause 0.2
            ease 1.7 ypos 10 #out
            repeat

image Laura_Sex_Legs_S4:
    # Her Legs in the Sex pose, slow
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -15 #in -25
                easeout 0.45 ypos -10 #-50
                easein 1.5 ypos 0 #out
                repeat                   
    contains:
            AlphaMask("Laura_Sex_Zero_Anim_S4", "Laura_SexMask")
            subpixel True
            pos (525,475)
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos 460 #in 450
                easeout 0.45 ypos 465 #455
                easein 1.5 ypos 475 #out                  
                repeat
    contains:
            # spunk
            ConditionSwitch(    
                "'in' not in L_Spunk", Null(),
                "True", "images/LauraSex/Laura_Sex_Spunk_Anal_O.png", 
                ) 
            subpixel True
            pos (-15,-105) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -120 #in -15
                easeout 0.45 ypos -115 #-10
                easein 1.5 ypos -105 #out
                repeat 
    # End Legs Sex fast
                    
image Laura_Sex_Zero_Anim_S4:
    #this is the cock for Laura's sex animation, Speed4 (cumming)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,-60)#130,75
        block: #total 
                ease .2 ypos -70
                easeout .5 ypos -68
                easein 1.5 ypos -60
                repeat
    
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
    
# End S4 (cumming) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Anal Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start A0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
 
image Laura_Sex_Body_A0:                                                                        
    #Her Body in the anal pose, static
    contains:
        "Laura_Sex_Body"      
        subpixel True       
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 1.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat
            
image Laura_Sex_Legs_A0:
    # Her Legs in the anal pose, static
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2s
                pause 0.6
                easeout 0.8 ypos -2 #-50
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat                  
    contains:
            AlphaMask("Laura_Sex_Zero_Anim_A0", "Laura_AnalMask")
            subpixel True
            pos (533,587) #538,580
            block:#total 2.5s > 1.75 > 1.2
                pause 0.6
                easeout 0.8 ypos 585 #578
                easein 0.2 ypos 582 #out  575
                easeout 0.5 ypos 583 #576
                easein 0.9 ypos 587 #out  580                
                repeat
    # End Legs anal static
    
image Laura_Sex_Zero_Anim_A0:
    #this is the cock for Laura's anal animation, Speed0 (static)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,115)#125,115
        block: #total 3s
                ease 1.5 ypos 110
                pause .5
                ease 1.0 ypos 115
                repeat         
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
    
# End A0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Start A1 (heading) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

                
image Laura_Sex_Body_A1:                                                                        
    #Her Body in the anal pose, heading
    contains:
        "Laura_Sex_Body"      
        subpixel True       
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 1.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat
            
image Laura_Sex_Legs_A1:
    # Her Legs in the anal pose, heading
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2s
                pause 0.6
                easeout 0.8 ypos -2 #-50
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat                  
    contains:
            AlphaMask("Laura_Sex_Zero_Anim_A1", "Laura_AnalMask")
            subpixel True
            pos (538,583) #525,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.6
                easeout 0.8 ypos 581 #455
                easein 0.2 ypos 578 #out  
                easeout 0.5 ypos 579 #455
                easein 0.9 ypos 583 #out                  
                repeat
    # End Legs anal heading
                    
image Laura_Sex_Zero_Anim_A1:
    #this is the cock for Laura's anal animation, Speed1 (heading)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,115)#125,75
        block: #total 3s
                easeout 1.2 ypos 100
                easein .3 ypos 90
                easeout .5 ypos 100
                easein 1 ypos 115
                repeat         
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
    
# End A1 (heading) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
# Start A2 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
 
image Laura_Sex_Body_A2:                                                                        
    #Her Body in the anal pose, slow
    contains:
        "Laura_Sex_Body"      
        subpixel True       
        pos (0,0) #top (0,-10)
        block:#total 2.5s > 1.75 > 1.2
            pause 0.3
            ease 0.3 ypos -20 #in
            pause 0.20
            ease 1.70 ypos 20 #out
            repeat
            
image Laura_Sex_Legs_A2:
    # Her Legs in the anal pose, slow
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.25
                ease 0.3 ypos -35 #in
                easeout 0.45 ypos -30
                easein 1.5 ypos 0 #out
                repeat            
    contains:
            AlphaMask("Laura_Sex_Zero_Anim_A2", "Laura_AnalMask")
            subpixel True
            pos (538,580) #525,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.25
                ease 0.3 ypos 545 #in 450
                easeout 0.45 ypos 550 #455
                easein 1.5 ypos 580 #out                  
                repeat
    contains:
            # spunk
            ConditionSwitch(    
                "'anal' not in L_Spunk", Null(),
                "True", "images/LauraSex/Laura_Sex_Spunk_Anal_O.png", 
                ) 
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.25
                ease 0.3 ypos -35 #in
                easeout 0.45 ypos -30
                easein 1.5 ypos 0 #out
                repeat 
    # End Legs anal slow
                    
image Laura_Sex_Zero_Anim_A2:
    #this is the cock for Laura's anal animation, Speed2 (slow)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,75)#130,75
        block: #total 2.5s > 1.75 > 1.2
                ease .5 ypos -50#-50
                easeout 1.5 ypos 60#60
                easein .5 ypos 75
                repeat                
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
    
# End A2 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
# Start A3 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Laura_Sex_Body_A3:                                                                        
    #Her Body in the anal pose, fast
    contains:
        "Laura_Sex_Body"      
        subpixel True       
        pos (0,0) #top (0,-10)
        block:#total 2.5s > 1.75 > 1.2
            pause 0.1
            ease 0.2 ypos -50 #in
            pause 0.2
            ease .7 ypos 00 #out
            repeat
                            
image Laura_Sex_Legs_A3:
    # Her Legs in the anal pose, fast
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -55 #in -25
                easeout 0.45 ypos -40 #-50
                easein .5 ypos 0 #out
                repeat                      
    contains:
            AlphaMask("Laura_Sex_Zero_Anim_A3", "Laura_AnalMask")
            subpixel True
            pos (538,580) #525,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos 525 #in 450
                easeout 0.45 ypos 540 #455
                easein .5 ypos 580 #out                  
                repeat
    contains:
            # Spunk
            ConditionSwitch(    
                "'anal' not in L_Spunk", Null(),
                "True", "images/LauraSex/Laura_Sex_Spunk_Anal_O.png", 
                ) 
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -55 #in -25
                easeout 0.45 ypos -40 #-50
                easein .5 ypos 0 #out
                repeat  
    # End Legs Anal fast
                    
image Laura_Sex_Zero_Anim_A3:
    #this is the cock for Laura's anal animation, Speed3 (fast)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,75)#130,75
        block: #total 2.5s > 1.75 > 1.2
                ease .2 ypos -70#-50
                easeout .7 ypos 0#60
                easein .3 ypos 75
                repeat
    
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
    
# End A3 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
# Start A4 (cumming) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Laura_Sex_Body_A4:                                                                        
    #Her Body in the anal pose, cumming
    contains:
        "Laura_Sex_Body"      
        subpixel True       
        pos (0,20) #top (0,-10)
        block:#total 2.5s > 1.75 > 1.2
            pause 0.1
            ease 0.2 ypos 00 #in
            pause 0.2
            ease 1.7 ypos 20 #out
            repeat

image Laura_Sex_Legs_A4:
    # Her Legs in the anal pose, cumming
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -15 #in -25
                easeout 0.45 ypos -10 #-50
                easein 1.5 ypos 0 #out
                repeat                   
    contains:
            AlphaMask("Laura_Sex_Zero_Anim_A4", "Laura_AnalMask")
            subpixel True
            pos (538,583) #525,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos 568 #in 450
                easeout 0.45 ypos 573 #455
                easein 1.5 ypos 583 #out                  
                repeat
    contains:
            # spunk
            ConditionSwitch(    
                "'anal' not in L_Spunk", Null(),
                "True", "images/LauraSex/Laura_Sex_Spunk_Anal_O.png", 
                ) 
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -15 #in -25
                easeout 0.45 ypos -10 #-50
                easein 1.5 ypos 0 #out
                repeat 
    # End Legs Anal cumming
                    
image Laura_Sex_Zero_Anim_A4:
    #this is the cock for Laura's anal animation, Speed4 (cumming)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,-60)#130,75
        block: #total 
                ease .2 ypos -70
                easeout .5 ypos -68
                easein 1.5 ypos -60
                repeat
    
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
# End A4 (cumming) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


# Start H0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
   
image Laura_Sex_Body_H0:                                                                        
    #Her Body in the hotdogging pose, static
    contains:
        "Laura_Sex_Body"      
        subpixel True       
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 1.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat
            
image Laura_Sex_Legs_H0:
    # Her Legs in the hotdogging pose, static
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2s
                pause 0.6
                easeout 0.8 ypos -2 #-50
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat                  
    contains:
            "Laura_Sex_Zero_Anim_H0"
#            AlphaMask("Laura_Sex_Zero_Anim_H0", "Laura_AnalMask")
            subpixel True
            pos (558,580) #538,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.6
                easeout 0.8 ypos 578 #455
                easein 0.2 ypos 575 #out  
                easeout 0.5 ypos 576 #455
                easein 0.9 ypos 580 #out                  
                repeat
    # End Legs hotdogging static
                    
image Laura_Sex_Zero_Anim_H0:
    #this is the cock for Laura's hotdogging animation, Speed0 (static)
    contains:
        subpixel True
        ConditionSwitch(            
            "P_Sprite", "Zero_Doggy_Insert",# Zero's cock, changes color and properties
            "True", Null(),
            )    
        
#        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,115)#125,75
        alpha 0.8    
        block: #total 3s
                ease 1.5 ypos 110
                pause .5
                ease 1.0 ypos 115
                repeat         
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
    
# End H0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Start H1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
        
image Laura_Sex_Body_H1:                                                                        
    #Her Body in the hotdogging pose, slow
    contains:
        "Laura_Sex_Body"      
        subpixel True       
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 1.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat
            
image Laura_Sex_Legs_H1:
    # Her Legs in the hotdogging pose, slow
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2s
                pause 0.6
                ease 1 ypos -10 #-50
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat                  
    contains:
            "Laura_Sex_Zero_Anim_H1"
#            AlphaMask("Laura_Sex_Zero_Anim_H0", "Laura_AnalMask")
            subpixel True
            pos (558,580) #538,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.6
                ease 1 ypos 570 #-50 
                easeout 0.5 ypos 576 #455
                easein 0.9 ypos 580 #out                  
                repeat
    # End Legs hotdogging slow
                    
image Laura_Sex_Zero_Anim_H1:
    #this is the cock for Laura's hotdogging animation, Speed1 (slow)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        alpha 0.8    
        pos (125,250)#125,75
        block: #total 3s
                ease 1.5 ypos 90 #110
                pause .5
                ease 1.0 ypos 250
                repeat         
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
    
# End H1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
                
# Start H2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Laura_Sex_Body_H2:                                                                        
    #Her Body in the hotdogging pose, fast
    contains:
        "Laura_Sex_Body"      
        subpixel True       
        pos (0,0) #top (0,-10)
        block:#total .75s
            pause .3
            ease .5 ypos -5 #in
            pause 0.3
            ease .4 ypos 0 #out
            repeat
            
image Laura_Sex_Legs_H2:
    # Her Legs in the hotdogging pose, fast
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total .75s
                pause 0.1
                ease .25 ypos -20 #-50
                easeout 0.15 ypos -18 #-50
                easein 0.25 ypos 0 #out
                repeat                  
    contains:
            "Laura_Sex_Zero_Anim_H2"
#            AlphaMask("Laura_Sex_Zero_Anim_H0", "Laura_AnalMask")
            subpixel True
            pos (558,580) #538,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.1
                ease .25 ypos 560 #-50
                easeout 0.15 ypos 562 #455
                easein 0.25 ypos 580 #out                  
                repeat
    # End Legs anal fast
                    
image Laura_Sex_Zero_Anim_H2:
    #this is the cock for Laura's hotdogging animation, Speed1 (fast)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        alpha 0.8    
        pos (125,230)#125,75
        block: #total .75s
                ease .25 ypos 150 #110
                easeout 0.25 ypos 170 
                easein 0.25 ypos 230   
                repeat         
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
    
# End H2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
                
             
image Laura_AnalMask:                    
    transform_anchor True
    contains:
        "images/LauraSex/Laura_Sex_MaskAnalX.png"
        pos (200,366)#(0,0)#(-300,-300) #323 -70
        anchor (.5,.5)
    zoom 1 
    anchor (0.5,0.5)
                    
#End Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





#image Laura_SexMask:
#    contains:
#        "images/LauraSex/Laura_Sex_PussyMaskTest2.png"
#        pos (-300,-300)   
##        block:
##                    ease 1 xzoom .5
##                    ease 1 xzoom 1
##                    repeat
#    zoom 1 
#    transform_anchor True
#    anchor (0.1,0.5)
##    rotate 30
                    
#image Laura_Sex_Zero_Anim0:
#        #this is the cock for Laura's sex animation, Speed 0 (static)
##        contains: 
##            "images/LauraSex/Laura_Sex_PussyMaskTestB.png"
##            pos (-200,0)
#        contains:
#            subpixel True
##            anchor (0.5,0)
#            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
##            pos (498,530) #X less is left, Y less is up (498,520)
#            zoom 1.6
#            alpha 0.5
#            pos(350,250) #466
##            rotate -30
#            block:
#                    ease 1.25 ypos 100#630
#                    ease 1.25 ypos 250#480
#                    repeat
#        size (1264,1061)#(1119,1186)
#        anchor (0.1,0.5)
#        transform_anchor True
##        rotate 30
    



image Laura_SexMaskX:                    
    transform_anchor True
    contains:
        "images/LauraSex/Laura_Sex_MaskPussyX.png"
        pos (200,303)#(0,0)#(-300,-300) #
        anchor (.5,.5)
#        block:
#            ease 0.5 ypos 490#270 #bottom
#            pause 0.5
#            ease 1 ypos 540#320 #top
#            repeat
#        block:
#                    ease 1 xzoom .5
#                    ease 1 xzoom 1
#                    repeat
#        block:
#                    ease .5 pos(0,0)
#                    ease .5 pos(0,2000)
#                    ease .5 pos(200,0)
#                    ease .5 pos(200,2000)
#                    ease .25 pos(400,0)
#                    ease .25 pos(400,2000)
#                    ease .25 pos(600,0)
#                    ease .25 pos(600,2000)
#                    ease .25 pos(800,0)
#                    ease .25 pos(800,2000)
#                    ease .25 pos(1000,0)
#                    ease .25 pos(1000,2000)
#                    ease .25 pos(1200,0)
#                    ease .25 pos(1200,2000)
#                    ease .25 pos(1400,0)
#                    ease .25 pos(1400,2000)
#                    repeat
    zoom 1 
#    transform_anchor True
    anchor (0.5,0.5)
#    rotate 30
                    
image Laura_Sex_Zero_AnimX:
        #this is the cock for Laura's sex animation, Speed 0 (static)
        contains: 
            Solid("#159457", xysize=(401,606))#(1264,1061))
            alpha 0.9
        contains:
            subpixel True
#            anchor (0.5,0)
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
#            pos (498,530) #X less is left, Y less is up (498,520)
            zoom 1.6
            alpha 0.5
            pos (130,100)#(390,550)#(350,250) #466
#            rotate -30
            block:
                    ease 1.25 ypos -50#630
                    ease 1.25 ypos 100#480
                    repeat
        
        size (401,606)#(88,266)(1264,1061)#(1119,1186)
        anchor (0.1,0.5)
        transform_anchor True
#        rotate 30


image Laura_Mega_Mask2:
    # giant green brick for use in finding where a mask is
    contains:
        "images/LauraSex/Laura_Sex_PussyMaskTest2.png"
#        Solid("#159457", xysize=(500,500))
#        offset (-100,100)
#        anchor (0.5,0.5)
#        zoom 1.0
#        alpha .5
#        pos (200,0)#(26,350)#(-175,450)
#        block:
#                    ease .25 offset(0,-500)
#                    ease .25 offset(0,1000)
#                    ease .25 offset(200,-500)
#                    ease .25 offset(200,1000)
#                    ease .25 offset(400,-500)
#                    ease .25 offset(400,1000)
#                    ease .25 offset(600,-500)
#                    ease .25 offset(600,1000)
#                    ease 1.5 offset(-800,-1000)
#                    ease 1.5 offset(-200,-100)
#                    ease .25 offset(-400,-500)
#                    ease .25 offset(-400,1000)
#                    ease .25 offset(-200,-500)
#                    ease .25 offset(-200,1000)
#                    repeat
    transform_anchor True
    zoom 1 
    rotate 30
#    block:
#                    ease 1 rotate 0
#                    ease 1 rotate 30
#                    repeat

image Laura_Mega_Mask:
    # giant green brick for use in finding where a mask is
    contains:
        "images/LauraSex/Laura_Sex_PussyMaskTestB.png"
#        Solid("#159457", xysize=(500,500))
#        offset (-100,100)
#        anchor (0.5,0.5)
#        zoom 1.0
        alpha .5
#        pos (200,0)#(26,350)#(-175,450)
#        block:
#                    ease 1.5 offset(-800,-1200)
#                    ease 1.5 offset(-200,-100)
#                    ease 1.5 offset(-600,-1200)
#                    ease 1.5 offset(-600,-600)
#                    ease 1.5 offset(-200,-1200)
#                    ease 1.5 offset(-200,-600)
#                    repeat
    transform_anchor True
    zoom 1 
    rotate 30
                    
# end Laura's Sex Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Laura_Sex_Launch(Line = "solo"): 
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
    if renpy.showing("Laura_SexSprite"):
        return 
    $ P_Sprite = 1
    hide Laura_Sprite      
    if renpy.showing("Laura_BJ_Animation"):
        hide Laura_BJ_Animation
    if renpy.showing("Laura_HJ_Animation"):
        hide Laura_HJ_Animation
    if renpy.showing("Laura_TJ_Animation"):
        hide Laura_TJ_Animation
    call Speed_Shift(0) 
    
    if Trigger == "in" or Trigger == "anal": 
            if L_Legs:          #temporary, change or remove when other clothing options are available
                $ L_Upskirt = 1
            if L_Panties:       #temporary, change or remove when other clothing options are available
                $ L_PantiesDown = 1
                        
    show Laura_SexSprite zorder 150:
        pos (450,500)
    with dissolve
    return
    
label Laura_Sex_Reset:
    if not renpy.showing("Laura_SexSprite"):
        return
    $ Laura_Arms = 2     
    hide Laura_SexSprite  
    call Laura_Hide 
    show Laura_Sprite at SpriteLoc(L_SpriteLoc) zorder LauraLayer:
        alpha 1
        zoom 1 offset (0,0) 
        anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return


# Laura's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
            
            
            
            
# Laura's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
                                                 

              
image Laura_BJ_Animation:                
    #core blowjob animation   
    contains:
        ConditionSwitch(
            # Laura's upper body
#            "P_Sprite", ConditionSwitch(                                                               
#                    # If during sex
            "Speed == 1", "Laura_BJ_Body_1",#Licking
            "Speed == 2", "Laura_BJ_Body_2",#Heading
            "Speed == 3", "Laura_BJ_Body_3",#Sucking
            "Speed == 4", "Laura_BJ_Body_4",#Deepthroat
            "Speed == 5", "Laura_BJ_Body_5",#Cumming high
            "Speed == 6", "Laura_BJ_Body_6",#Cumming deep
#                    "True",     "Laura_BJ_Body_0",#Static
#                    ),
            "True","Laura_BJ_Body_0",#Static
            )   
    zoom 1.35            
    anchor (.5,.5)                 
    pos (600,605)            
                 

#  BJ animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

                
#image Laura_Sprite_BJ_SuckingMask:
#    contains:
#            "images/LauraSprite/Laura_Sprite_SuckingMask.png"
##            pos (200,50)
#    contains:
#            "images/LauraSprite/Laura_Sprite_SpunkSuckingO.png"
#    pos (100,150)
#    alpha .8
            
image Laura_Sprite_BJ_HairBack:          
    #This is the version of the hair back used in the BJ pose
#    "images/LauraSprite/Laura_Sprite_Hair_Long_Under.png"      
    ConditionSwitch(                                                                         
            #Hair over
            "not L_Hair", Null(),
            "L_HairColor and L_Hair == 'wet' or L_Water", im.MatrixColor("images/LauraSprite/Laura_Sprite_HairWhite_Wet_Under.png",im.matrix.tint(float(L_HairCustomColor.red)/255.0, float(L_HairCustomColor.green)/255.0, float(L_HairCustomColor.blue)/255.0)),
            "L_Hair == 'wet' or L_Water", "images/LauraSprite/Laura_Sprite_Hair_Wet_Under.png",
            "L_HairColor and L_Hair", im.MatrixColor("images/LauraSprite/Laura_Sprite_HairWhite_Long_Under.png",im.matrix.tint(float(L_HairCustomColor.red)/255.0, float(L_HairCustomColor.green)/255.0, float(L_HairCustomColor.blue)/255.0)),
            "L_Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Under.png",
            "True", Null(),
            )        
                    
image Laura_Sprite_BJ_Head:
    #This is the version of the head used in the BJ pose
    LiveComposite(
        (806,806),         
        (0,0), ConditionSwitch(
                # Face background plate
                "L_Blush == 2", "images/LauraSprite/Laura_Sprite_Head_Blush2.png", 
                "L_Blush", "images/LauraSprite/Laura_Sprite_Head_Blush.png",  
                "True", "images/LauraSprite/Laura_Sprite_Head.png",                        
                ),        
        (0,0), ConditionSwitch(#chin spunk
            "'chin' not in L_Spunk", Null(),
            "Speed >= 2", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Spunk_Chin.png",
            ),    
        (0,0), ConditionSwitch(#Mouths 
            "Speed >= 2", "images/LauraSprite/Laura_Sprite_Mouth_SuckingBJ.png",   #sucking       
            "Speed == 1", "images/LauraSprite/Laura_Sprite_Mouth_Tongue.png",     #licking 
            "L_Mouth == 'normal'", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png",
            "L_Mouth == 'lipbite'", "images/LauraSprite/Laura_Sprite_Mouth_Lipbite.png",
            "L_Mouth == 'sucking'", "images/LauraSprite/Laura_Sprite_Mouth_Sucking.png",            
            "L_Mouth == 'kiss'", "images/LauraSprite/Laura_Sprite_Mouth_Kiss.png",
            "L_Mouth == 'sad'", "images/LauraSprite/Laura_Sprite_Mouth_Sad.png",
            "L_Mouth == 'smile'", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png",
            "L_Mouth == 'surprised'", "images/LauraSprite/Laura_Sprite_Mouth_Surprised.png",            
            "L_Mouth == 'tongue'", "images/LauraSprite/Laura_Sprite_Mouth_Tongue.png",                
            "L_Mouth == 'grimace'", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png",              
            "L_Mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Mouth_Smirk.png",                    
#            "L_Mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png",         
            "True", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png",
            ),         
        (0,0), ConditionSwitch(#Mouth spunk 
            "'mouth' not in L_Spunk", Null(),
            "Speed >= 2", "images/LauraSprite/Laura_Sprite_Spunk_MouthSuck.png",   #sucking       
            "Speed == 1", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",     #licking             
            "L_Mouth == 'normal'", "images/LauraSprite/Laura_Sprite_Spunk_MouthNeutral.png",
            "L_Mouth == 'lipbite'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmirk.png",
            "L_Mouth == 'sucking'", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",            
            "L_Mouth == 'kiss'", "images/LauraSprite/Laura_Sprite_Spunk_MouthKiss.png",
            "L_Mouth == 'sad'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSad.png",
            "L_Mouth == 'smile'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmile.png",
            "L_Mouth == 'surprised'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSad.png",            
            "L_Mouth == 'tongue'", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",                
            "L_Mouth == 'grimace'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmile.png",              
            "L_Mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmirk.png",      
            "True", "images/LauraSprite/Laura_Sprite_Spunk_MouthNeutral.png",
            ),     
        (0,0), ConditionSwitch(#Mouth spunk over 
            "Speed >= 2 and 'mouth' in L_Spunk", "images/LauraSprite/Laura_Sprite_SpunkSuckingO.png",   #sucking  
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(#wet tongue
            "Speed == 1", "images/LauraSprite/Laura_Sprite_Wet_Tongue.png",     #licking   
            "True", Null(),
            ),                                                              
        (0,0), ConditionSwitch(                                                                       
            #brows
            "L_Blush >= 2", ConditionSwitch(
                    "L_Brows == 'normal'", "images/LauraSprite/Laura_Sprite_Brows_Normal_B.png",
                    "L_Brows == 'angry'", "images/LauraSprite/Laura_Sprite_Brows_Angry_B.png",
                    "L_Brows == 'sad'", "images/LauraSprite/Laura_Sprite_Brows_Sad_B.png",
                    "L_Brows == 'surprised'", "images/LauraSprite/Laura_Sprite_Brows_Surprised_B.png",        
                    "L_Brows == 'confused'", "images/LauraSprite/Laura_Sprite_Brows_Confused_B.png",
                    "True", "images/LauraSprite/Laura_Sprite_Brows_Normal_B.png",
                    ),
            "True", ConditionSwitch(
                    "L_Brows == 'normal'", "images/LauraSprite/Laura_Sprite_Brows_Normal.png",
                    "L_Brows == 'angry'", "images/LauraSprite/Laura_Sprite_Brows_Angry.png",
                    "L_Brows == 'sad'", "images/LauraSprite/Laura_Sprite_Brows_Sad.png",
                    "L_Brows == 'surprised'", "images/LauraSprite/Laura_Sprite_Brows_Surprised.png",        
                    "L_Brows == 'confused'", "images/LauraSprite/Laura_Sprite_Brows_Confused.png",
                    "True", "images/LauraSprite/Laura_Sprite_Brows_Normal.png",
                    ),
            ),        
        (0,0), "Laura Blink",     #Eyes    
        (0,0), ConditionSwitch(                
            #Hair mid
            "L_Over == 'jacket'", Null(),
            "L_Hair == 'wet' or L_Water", Null(),
            "L_HairColor and L_Hair", im.MatrixColor("images/LauraSprite/Laura_Sprite_HairWhite_Long_Mid.png",im.matrix.tint(float(L_HairCustomColor.red)/255.0, float(L_HairCustomColor.green)/255.0, float(L_HairCustomColor.blue)/255.0)),
            "L_Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Mid.png",
            "True", Null(),
            ),       
#        (0,0), ConditionSwitch(
#            #Face Water
#            "not L_Water", Null(),
#            "True", "images/LauraSprite/Laura_Sprite_Wet_Head.png",
#            ),
        (0,0), ConditionSwitch(                                                                         
            #Hair over
            "not L_Hair or L_HairColor", Null(),
            "L_Hair == 'wet' or L_Water", "images/LauraSprite/Laura_Sprite_Hair_Wet_Over.png",
            "L_Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Over.png",
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                         
            #Hair over
            "not L_Hair or not L_HairColor", Null(),
            "L_Hair == 'wet' or L_Water", im.MatrixColor("images/LauraSprite/Laura_Sprite_HairWhite_Wet_Over.png",im.matrix.tint(float(L_HairCustomColor.red)/255.0, float(L_HairCustomColor.green)/255.0, float(L_HairCustomColor.blue)/255.0)),
            "L_Hair", im.MatrixColor("images/LauraSprite/Laura_Sprite_HairWhite_Long_Over.png",im.matrix.tint(float(L_HairCustomColor.red)/255.0, float(L_HairCustomColor.green)/255.0, float(L_HairCustomColor.blue)/255.0)),
            "True", Null(),
            ),        
        (0,0), ConditionSwitch(
            #Hair Water
            "not L_Water", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Head_Wet.png",
#            "True", "images/LauraSprite/Laura_Sprite_Hair_Wet.png",
            ),
        (0,0), ConditionSwitch(
            #facial spunk               
            "'hair' in L_Spunk", "images/LauraSprite/Laura_Sprite_Spunk_Facial2.png",  
            "'facial' in L_Spunk", "images/LauraSprite/Laura_Sprite_Spunk_Facial1.png",            
            "True", Null(),
            ),  
        )                
#    anchor (0.6, 0.0)                
#    zoom .5      
        
image Laura_BlowCock_Mask:   
    #This is a mask used by the blockcock during the Speed 3 sucking animation
    #it is a block moving in and out to prevent the cock sticking out the back. 
    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,0)#(640,198)# top
#        block:
#                pause 0.1
#                ease 1.6 offset (0,300)# bottom
#                pause 0.1
#                ease 1.4 offset (0,0)# top
#                repeat                    


#image Laura_BlowCock_Mask_3:   
#    This is a mask used by the blockcock during the Speed 4 deep throat animation
#    it is a block moving in and out to prevent the cock sticking out the back. 
#    contains:
#        Solid("#159457", xysize=(190,950))
#        offset (0,0)#(640,198)# top
#        block:
#                pause 0.1
#                ease 1.6 offset (0,300)# bottom
#                pause 0.1
#                ease 1.4 offset (0,0)# top
#                repeat   

image Laura_BJ_Body_0:                                                                        
    #Her Body in the BJ pose, static
    contains:
            #Hair underlay
            "Laura_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (490,400) #(535,340) #top
            rotate 0 #-30
            parallel:
                ease 1.1 ypos 405 #bottom
                pause 0.2
                ease 1.1 ypos 400 #top
                pause 0.2
                repeat           
    contains:       
            #base body
            "Laura_Sprite"   
            subpixel True   
            pos (650,800)#(673,740) #top
            zoom 2.2 #.75                    
            anchor (0.5, 0.5)
            rotate -20
            parallel:
                pause 0.1
                ease 1.1 ypos 810 #bottom
                pause 0.2
                ease 1 ypos 800 #top
                pause 0.1
                repeat    
    contains:
            #base head under cock
            subpixel True
            "Laura_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (490,400) #(535,340) #top
            rotate 0 #-30    
            parallel:
                ease 1.1 ypos 405 #bottom
                pause 0.2
                ease 1.1 ypos 400 #top
                pause 0.2
                repeat    
    contains:
            #zero's cock
#            ConditionSwitch(    
#                "P_Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Laura_BlowCock_Mask"), #Null(),
#                )      
            AlphaMask("Blowcock", "Laura_BlowCock_Mask")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4  
            alpha 1
            rotate 10    
            parallel:
                pause 0.1
#                easeout .1 rotate 1 #bottom .6
                ease .15 rotate -5 #bottom
                pause 0.4
                ease 1.95 rotate 10 #top
                repeat
            parallel:
                pause 0.1
#                easeout .1 pos (407,262) #bottom(637,168)
                ease .15 pos (405,255) #bottom(637,168)
                pause 0.4
                ease 1.95 pos (420,292) #top 412
                repeat
    #End BJ animation Speed 0
    

image Laura_BJ_Body_1:                                                                        
    #Her Body in the BJ pose, licking
    contains:
            #Hair underlay
            "Laura_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (535,340) #(523,380) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.4 rotate -50 #bottom
                pause 0.3
                ease 1.4 rotate -30 #top
                repeat  
            parallel:
                pause 0.1
                easeout 1.2 xpos 470 #bottom
                easein .2 xpos 460 #bottom 481 
                pause 0.3
                easeout .75 xpos 500 #top
                easein .65 xpos 535 #top
                repeat    
            parallel:
                pause 0.1
                ease 1.4 ypos 500 #bottom
                pause 0.3
                ease 1.4 ypos 340 #top
                repeat            
    contains:       
            #base body
            "Laura_Sprite"      
            pos (673,740)#(680,755) #top
            zoom 2.2 #.75                    
            anchor (0.5, 0.5)
            rotate -20
            subpixel True
            parallel:
                pause 0.15
                ease 1.25 rotate -40 #bottom
                pause 0.45
                ease 1.35 rotate -20 #top
                repeat 
            parallel:
                pause 0.15
                easeout .9 xpos 740 #bottom
                easein .35 xpos 740 #bottom 481 
                pause 0.5
                easeout .65 xpos 710 #top
                easein .65 xpos 673 #top
                repeat   
            parallel:
                pause 0.15
                ease 1.25 ypos 830 #bottom
                pause 0.45
                ease 1.35 ypos 740 #top
                repeat    
    contains:
            #base head under cock
            subpixel True
            "Laura_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (535,340) #(523,380) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.4 rotate -50 #bottom
                pause 0.3
                ease 1.4 rotate -30 #top
                repeat  
            parallel:
                pause 0.1
                easeout 1.2 xpos 470 #bottom
                easein .2 xpos 460 #bottom 481 
                pause 0.3
                easeout .75 xpos 500 #top
                easein .65 xpos 535 #top
                repeat    
            parallel:
                pause 0.1
                ease 1.4 ypos 500 #bottom
                pause 0.3
                ease 1.4 ypos 340 #top
                repeat    
    contains:
            #zero's cock
#            ConditionSwitch(    
#                "P_Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Laura_BlowCock_Mask"), #Null(),
#                )      
            AlphaMask("Blowcock", "Laura_BlowCock_Mask")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4  
            alpha 1
            rotate 10    
            parallel:
                pause 0.1
                easeout 1.2 rotate 1 #bottom
                easein .3 rotate -1 #bottom
                pause 0.4
                ease 1.2 rotate 10 #top
                repeat
            parallel:
                pause 0.1
                easeout 1.2 pos (407,262) #bottom(637,168)
                easein .3 pos (405,255) #bottom(637,168)
                pause 0.4
                ease 1.2 pos (412,292) #top
                repeat
    #End BJ animation Speed 1
    
image Laura_BJ_Body_2:                                                                        
    #Her Body in the BJ pose, heading
    contains:
            #Hair underlay
            "Laura_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (530,355) #(530,355) #top
            rotate -30 #-30            
            parallel:
                pause 0.1
                easeout 1.2 rotate -40 #bottom
                ease .6 rotate -32 #bottom
                pause 0.1
                ease 1.2 rotate -30 #top
                repeat  
            parallel:
                pause 0.1
                easeout 1.2 xpos 510 #bottom 510
                ease .7 xpos 520 #bottom
                pause 0.1
                ease 1.1 xpos 530 #top
                repeat  
            parallel:
                pause 0.1
                ease 1.6 ypos 400 #bottom
                pause 0.1
                ease 1.4 ypos 355 #top
                repeat   
    contains:       
            #base body
            "Laura_Sprite"      
            pos (680,755)#(680,755) #top
            zoom 2.2 #.75                    
            anchor (0.5, 0.5)
            rotate -20
            subpixel True
            parallel:
                pause 0.15
                ease 1.55 rotate -30 #bottom
                pause 0.15
                ease 1.35 rotate -20 #top
                repeat 
            parallel:
                pause 0.15   
                ease 1.35 xpos 730 #bottom 760
                pause 0.25
                ease 1.45 xpos 680 #top                    
                repeat   
            parallel:
                pause 0.15
                ease 1.55 ypos 780 #bottom
                pause 0.15
                ease 1.35 ypos 755 #top
                repeat   
    contains:
            #base head under cock
            subpixel True
            "Laura_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (530,355) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                easeout 1.2 rotate -40 #bottom
                ease .6 rotate -32 #bottom
                pause 0.1
                ease 1.2 rotate -30 #top
                repeat  
            parallel:
                pause 0.1
                easeout 1.2 xpos 510 #bottom 510
                ease .7 xpos 520 #bottom
                pause 0.1
                ease 1.1 xpos 530 #top
                repeat  
            parallel:
                pause 0.1
                ease 1.6 ypos 400 #bottom
                pause 0.1
                ease 1.4 ypos 355 #top
                repeat    
    contains:
            #zero's cock
#            ConditionSwitch(    
#                "P_Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Laura_BlowCock_Mask"), #Null(),
#                )      
            AlphaMask("Blowcock", "Laura_BlowCock_Mask")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4  
            alpha 1
            rotate 10    
            parallel:
                pause 1.3
                ease .4 rotate 8 #bottom
                pause .2
                ease 1 rotate 10 #top
                pause .3
                repeat
            parallel:
                pause 1.3
                ease .4 pos (410,285) #bottom(407,262)
                pause .2
                ease 1 pos (412,292) #top
                pause .3
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Laura_Sprite_BJ_Head", "images/LauraSprite/Laura_Sprite_SuckingMask.png")
            zoom 0.81
            anchor (0.5, 0.5)
            pos (530,355) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                easeout 1.2 rotate -40 #bottom
                ease .6 rotate -32 #bottom
                pause 0.1
                ease 1.2 rotate -30 #top
                repeat  
            parallel:
                pause 0.1
                easeout 1.2 xpos 510 #bottom 510
                ease .7 xpos 520 #bottom
                pause 0.1
                ease 1.1 xpos 530 #top
                repeat  
            parallel:
                pause 0.1
                ease 1.6 ypos 400 #bottom
                pause 0.1
                ease 1.4 ypos 355 #top
                repeat   
    #End BJ animation Speed 2
    


image Laura_BlowCock_Mask_3:   
    #This is a mask used by the blockcock during the Speed 3 sucking animation
    #it is a block moving in and out to prevent the cock sticking out the back. 
    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,100)#(640,198)# top
#        block:
#                pause 0.1
#                ease 1.6 offset (0,300)# bottom
#                pause 0.1
#                ease 1.4 offset (0,0)# top
#                repeat   

image Laura_BJ_Body_3:                                                                        
    #Her Body in the BJ pose, sucking
    contains:
            #Hair underlay
            "Laura_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
#                pause 0.2
                ease .7 rotate -50 #bottom
#                pause 0.1
                ease 1 rotate -30 #top
                repeat  
            parallel:
#                pause 0.2
                easeout .3 xpos 500 #bottom .7
                easein .4 xpos 481 #bottom .9
#                pause 0.1
                easeout .55 xpos 500 #top .75
                easein .45 xpos 523 #top .65
                repeat    
            parallel:
#                pause 0.2
                ease .7 ypos 450 #bottom
#                pause 0.1
                ease 1 ypos 380 #top
                repeat                  
    contains:       
            #base body
            "Laura_Sprite"      
            pos (673,780)#(680,755) #top
            zoom 2.2 #.75                    
            anchor (0.5, 0.5)
            rotate -20
            subpixel True
            parallel:
#                pause 0.15
                ease .7 rotate -40 #bottom
#                pause 0.15
                ease 1.0 rotate -20 #top
                repeat 
            parallel:
#                pause 0.15   
                easeout .3 xpos 710 #bottom
                easein .4 xpos 760 #bottom
#                pause 0.15
                easeout .55 xpos 710 #top
                easein .45 xpos 673 #top                    
                repeat   
            parallel:
#                pause 0.15
                ease .7 ypos 780 #bottom 830
#                pause 0.15
                ease 1.0 ypos 780 #top
                repeat   
    contains:
            #base head under cock
            subpixel True
            "Laura_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
#                pause 0.2
                ease .7 rotate -50 #bottom
#                pause 0.1
                ease 1 rotate -30 #top
                repeat  
            parallel:
#                pause 0.2
                easeout .3 xpos 500 #bottom .7
                easein .4 xpos 481 #bottom .9
#                pause 0.1
                easeout .55 xpos 500 #top .75
                easein .45 xpos 523 #top .65
                repeat    
            parallel:
#                pause 0.2
                ease .7 ypos 450 #bottom
#                pause 0.1
                ease 1 ypos 380 #top
                repeat    
    contains:
            #zero's cock
#            ConditionSwitch(    
#                "P_Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Laura_BlowCock_Mask"), #Null(),
#                )      
            AlphaMask("Blowcock", "Laura_BlowCock_Mask_3")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4  
            alpha 1
            rotate 10    
            parallel:
#                pause 0.2
                ease .7 rotate 0 #bottom
#                pause 0.1
                ease 1 rotate 10 #top
                repeat
            parallel:
#                pause 0.2
                ease .7 pos (407,262) #bottom(637,168)
#                pause 0.1
                ease 1 pos (412,292) #top
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Laura_Sprite_BJ_Head", "images/LauraSprite/Laura_Sprite_SuckingMask.png")   
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
#                pause 0.2
                ease .7 rotate -50 #bottom
#                pause 0.1
                ease 1 rotate -30 #top
                repeat  
            parallel:
#                pause 0.2
                easeout .3 xpos 500 #bottom .7
                easein .4 xpos 481 #bottom .9
#                pause 0.1
                easeout .55 xpos 500 #top .75
                easein .45 xpos 523 #top .65
                repeat    
            parallel:
#                pause 0.2
                ease .7 ypos 450 #bottom
#                pause 0.1
                ease 1 ypos 380 #top
                repeat   
    #End BJ animation Speed 3
    
    
image Laura_BlowCock_Mask_4:   
    #This is a mask used by the blockcock during the Speed 4 deep throat animation
    #it is a block moving in and out to prevent the cock sticking out the back. 
    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,0)#(640,198)# top
        block:
                pause 0.1
                ease 1.6 offset (0,300)# bottom
                pause 0.1
                ease 1.4 offset (0,0)# top
                repeat   

image Laura_BJ_Body_4:                                                                        
    #Her Body in the BJ pose, deep throat
    contains:
            #Hair underlay
            "Laura_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.6 rotate -50 #bottom
                pause 0.1
                ease 1.4 rotate -30 #top
                repeat  
            parallel:
                pause 0.1
                easeout .7 xpos 500 #bottom
                easein .9 xpos 481 #bottom
                pause 0.1
                easeout .75 xpos 500 #top
                easein .65 xpos 523 #top
                repeat    
            parallel:
                pause 0.1
                ease 1.6 ypos 500 #bottom
                pause 0.1
                ease 1.4 ypos 380 #top
                repeat                
    contains:       
            #base body
            "Laura_Sprite"      
            pos (673,780)#(680,755) #top
            zoom 2.2 #.75                    
            anchor (0.5, 0.5)
            rotate -20
            subpixel True
            parallel:
                pause 0.15
                ease 1.55 rotate -40 #bottom
                pause 0.15
                ease 1.35 rotate -20 #top
                repeat 
            parallel:
                pause 0.15   
                easeout .65 xpos 710 #bottom
                easein .9 xpos 760 #bottom
                pause 0.15
                easeout .70 xpos 710 #top
                easein .65 xpos 673 #top                    
                repeat   
            parallel:
                pause 0.15
                ease 1.55 ypos 830 #bottom
                pause 0.15
                ease 1.35 ypos 780 #top
                repeat   
    contains:
            #base head under cock
            subpixel True
            "Laura_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.6 rotate -50 #bottom
                pause 0.1
                ease 1.4 rotate -30 #top
                repeat  
            parallel:
                pause 0.1
                easeout .7 xpos 500 #bottom
                easein .9 xpos 481 #bottom
                pause 0.1
                easeout .75 xpos 500 #top
                easein .65 xpos 523 #top
                repeat    
            parallel:
                pause 0.1
                ease 1.6 ypos 500 #bottom
                pause 0.1
                ease 1.4 ypos 380 #top
                repeat    
    contains:
            #zero's cock
#            ConditionSwitch(    
#                "P_Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Laura_BlowCock_Mask"), #Null(),
#                )      
            AlphaMask("Blowcock", "Laura_BlowCock_Mask_4")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4  
            alpha 1
            rotate 10    
            parallel:
                pause 0.1
                ease 1.6 rotate 0 #bottom
                pause 0.1
                ease 1.4 rotate 10 #top
                repeat
            parallel:
                pause 0.1
                ease 1.6 pos (407,262) #bottom(637,168)
                pause 0.1
                ease 1.4 pos (412,292) #top
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Laura_Sprite_BJ_Head", "images/LauraSprite/Laura_Sprite_SuckingMask.png")
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.6 rotate -50 #bottom
                pause 0.1
                ease 1.4 rotate -30 #top
                repeat  
            parallel:
                pause 0.1
                easeout .7 xpos 500 #bottom
                easein .9 xpos 481 #bottom
                pause 0.1
                easeout .75 xpos 500 #top
                easein .65 xpos 523 #top
                repeat    
            parallel:
                pause 0.1
                ease 1.6 ypos 500 #bottom
                pause 0.1
                ease 1.4 ypos 380 #top
                repeat  
    #End BJ animation Speed 4
    
    
image Laura_BJ_Body_5:                                                                        
    #Her Body in the BJ pose, high cumming
    contains:
            #Hair underlay
            "Laura_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (520,375) #(530,355) #bottom
            rotate -50 #-30
            parallel:
                pause 1
                ease .3 rotate -30 #top
                easeout .3 rotate -32 #bottom
                easein .5 rotate -35 #bottom
                pause .5
                repeat  
            parallel:
                pause 1 
                easein .3 xpos 530 #top
                easeout .3 xpos 525 #bottom
                easein .5 xpos 520 #bottom
                pause .5
                repeat    
            parallel:
                pause 1
                ease .3 ypos 355 #top
                easeout .3 ypos 365 #bottom
                easein .5 ypos 375 #bottom
                pause .5
                repeat              
    contains:       
            #base body
            "Laura_Sprite"      
            subpixel True
            zoom 2.2 #.75                    
            anchor (0.5, 0.5)
            rotate -30
            pos (730,760)#(680,755) #bottom                
            parallel:
                pause 1
                ease .3 rotate -26 #top
                easeout .3 rotate -28 #bottom
                easein .5 rotate -30 #bottom
                pause .5
                repeat  
            parallel:
                pause 1 
                easein .3 xpos 710 #top 680
                easeout .3 xpos 720 #bottom
                easein .5 xpos 730 #bottom
                pause .5
                repeat    
            parallel:
                pause 1
                ease .3 ypos 750 #top 755
                easeout .3 ypos 755 #bottom
                easein .5 ypos 760 #bottom
                pause .5
                repeat                  
    contains:
            #base head under cock
            subpixel True
            "Laura_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (520,375) #(530,355) #bottom
            rotate -35 #-30
            parallel:
                pause 1
                ease .3 rotate -30 #top
                easeout .3 rotate -32 #bottom
                easein .5 rotate -35 #bottom
                pause .5
                repeat  
            parallel:
                pause 1 
                easein .3 xpos 530 #top
                easeout .3 xpos 525 #bottom
                easein .5 xpos 520 #bottom
                pause .5
                repeat    
            parallel:
                pause 1
                ease .3 ypos 355 #top
                easeout .3 ypos 365 #bottom
                easein .5 ypos 375 #bottom
                pause .5
                repeat                   
    contains:
            #zero's cock
#            ConditionSwitch(    
#                "P_Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Laura_BlowCock_Mask"), #Null(),
#                )      
            AlphaMask("Blowcock", "Laura_BlowCock_Mask")
            subpixel True
            pos (410,292) #bottom
            zoom 0.4  
            alpha 1
            rotate 12    
            parallel:
                pause 1
                ease .3 rotate 10 #top
                ease .3 rotate 12 #bottom
                pause 1
                repeat
            parallel:
                pause 1
                ease .3 pos (412,285) #top
                ease .3 pos (410,292) #bottom(637,168)
                pause 1
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Laura_Sprite_BJ_Head", "images/LauraSprite/Laura_Sprite_SuckingMask.png")
            zoom 0.81
            anchor (0.5, 0.5)
            pos (520,375) #(530,355) #bottom
            rotate -35 #-30
            parallel:
                pause 1
                ease .3 rotate -30 #top
                easeout .3 rotate -32 #bottom
                easein .5 rotate -35 #bottom
                pause .5
                repeat  
            parallel:
                pause 1 
                easein .3 xpos 530 #top
                easeout .3 xpos 525 #bottom
                easein .5 xpos 520 #bottom
                pause .5
                repeat    
            parallel:
                pause 1
                ease .3 ypos 355 #top
                easeout .3 ypos 365 #bottom
                easein .5 ypos 375 #bottom
                pause .5
                repeat   
    #End BJ animation Speed 5
    
image Laura_BlowCock_Mask_6:   
    #This is a mask used by the blockcock during the Speed 4 deep throat animation
    #it is a block moving in and out to prevent the cock sticking out the back. 
    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,300)#(640,198)# top
#        block:
#                pause 0.1
#                ease 1.6 offset (0,300)# bottom
#                pause 0.1
#                ease 1.4 offset (0,0)# top
#                repeat   
                
image Laura_BJ_Body_6:                                                                        
    #Her Body in the BJ pose, deep throat cumming
    contains:
            #Hair underlay
            "Laura_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (481,500) #(530,355) #bottom
            rotate -50 #-30
            parallel:
                pause 1
                ease .3 rotate -45 #top
                easeout .3 rotate -48 #bottom
                easein .5 rotate -50 #bottom
                pause .5
                repeat  
            parallel:
                pause 1 
                easein .3 xpos 490 #top
                easeout .3 xpos 485 #bottom
                easein .5 xpos 481 #bottom
                pause .5
                repeat    
            parallel:
                pause 1
                ease .3 ypos 490 #top
                easeout .3 ypos 496 #bottom
                easein .5 ypos 500 #bottom
                pause .5
                repeat                 
    contains:       
            #base body
            "Laura_Sprite"      
            subpixel True
            zoom 2.2 #.75                    
            anchor (0.5, 0.5)
            rotate -40
            pos (760,830)#(680,755) #bottom                
            parallel:
                pause 1
                ease .3 rotate -38 #top
                easeout .3 rotate -39 #bottom
                easein .5 rotate -40 #bottom
                pause .5
                repeat  
            parallel:
                pause 1 
                easein .3 xpos 750 #top
                easeout .3 xpos 756 #bottom
                easein .5 xpos 760 #bottom
                pause .5
                repeat    
            parallel:
                pause 1
                ease .3 ypos 835 #top
                easeout .3 ypos 830 #bottom
                easein .5 ypos 830 #bottom
                pause .5
                repeat  
    contains:
            #base head under cock
            subpixel True
            "Laura_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (481,500) #(530,355) #bottom
            rotate -50 #-30
            parallel:
                pause 1
                ease .3 rotate -45 #top
                easeout .3 rotate -48 #bottom
                easein .5 rotate -50 #bottom
                pause .5
                repeat  
            parallel:
                pause 1 
                easein .3 xpos 490 #top
                easeout .3 xpos 485 #bottom
                easein .5 xpos 481 #bottom
                pause .5
                repeat    
            parallel:
                pause 1
                ease .3 ypos 490 #top
                easeout .3 ypos 496 #bottom
                easein .5 ypos 500 #bottom
                pause .5
                repeat   
    contains:
            #zero's cock
#            ConditionSwitch(    
#                "P_Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Laura_BlowCock_Mask"), #Null(),
#                )      
            AlphaMask("Blowcock", "Laura_BlowCock_Mask_6")
            subpixel True
            pos (407,262) #bottom
            zoom 0.4  
            alpha 1
            rotate 0    
            parallel:
                pause 1
                ease .3 rotate 2 #top
                ease .3 rotate 0 #bottom
                pause 1
                repeat
            parallel:
                pause 1
                ease .3 pos (409,268) #top
                ease .3 pos (407,262) #bottom(637,168)
                pause 1
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Laura_Sprite_BJ_Head", "images/LauraSprite/Laura_Sprite_SuckingMask.png")
            zoom 0.81
            anchor (0.5, 0.5)
            pos (481,500) #(530,355) #bottom
            rotate -50 #-30
            parallel:
                pause 1
                ease .3 rotate -45 #top
                easeout .3 rotate -48 #bottom
                easein .5 rotate -50 #bottom
                pause .5
                repeat  
            parallel:
                pause 1 
                easein .3 xpos 490 #top
                easeout .3 xpos 485 #bottom
                easein .5 xpos 481 #bottom
                pause .5
                repeat    
            parallel:
                pause 1
                ease .3 ypos 490 #top
                easeout .3 ypos 496 #bottom
                easein .5 ypos 500 #bottom
                pause .5
                repeat  
    #End BJ animation Speed 6
#Head and Body Animations for Laura's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
                                                               #BJ Launchers  
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                               #BJ Launchers  
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Laura_BJ_Launch(Line = 0):    # The sequence to launch the Laura BJ animations 
    $ Laura_Arms = 1
    if renpy.showing("Laura_BJ_Animation"):
        return
    
    call Laura_Hide
    if Line == "L" or Line == "cum":
        show Laura_Sprite at SpriteLoc(StageCenter) zorder LauraLayer:
            alpha 1
            ease 1 zoom 2.5 offset (150,80) 
        with dissolve
    else:
        show Laura_Sprite at SpriteLoc(StageCenter) zorder LauraLayer:
            alpha 1
            zoom 2.5 offset (150,80) 
        with dissolve
        
    $ Speed = 0
    if Taboo and Line == "L": # Laura gets started. . .
            if R_Loc == bg_current:
                "Laura looks back at Rogue to see if she's watching."
            elif K_Loc == bg_current:
                "Laura looks back at Kitty to see if she's watching."
            else:
                "Laura casually glaces around to see if anyone notices what she's doing"
            "She then bends down and puts your cock to her mouth."
    elif Line == "L":    
            "Laura smoothly bends down and places your cock against her cheek."    
            
    
    if Line != "cum":
        $ Trigger = "blow"
    
    show Laura_Sprite zorder LauraLayer:
        alpha 0
    show Laura_BJ_Animation zorder 150: 
        pos (645,510) 
    return
    
label Laura_BJ_Reset: # The sequence to the Laura animations from BJ to default
    if not renpy.showing("Laura_BJ_Animation"):
        return
#    hide Laura_BJ_Animation
    call Laura_Hide 
    $ Speed = 0
    
    show Laura_Sprite at SpriteLoc(StageCenter) zorder LauraLayer:
        alpha 1
        zoom 2.5 offset (150,80) 
    with dissolve
    
    show Laura_Sprite zorder LauraLayer:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)      
    show Laura_Sprite at SpriteLoc(L_SpriteLoc) zorder LauraLayer:
        alpha 1
        zoom 1 offset (0,0)    
    return  

# End Laura Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Emma Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Emma Handjob element //////////////////////////////////////////////////////////////////////                                         Core Emma HJ element

image Laura_Hand_Under:
    "images/LauraSprite/handlaura2.png"
    anchor (0.5,0.5)
    pos (-10,0)
    
    
image Laura_Hand_Over:
    "images/LauraSprite/handlaura1.png"    
    anchor (0.5,0.5)
    pos (-10,0)
    
transform Laura_Hand_1():
    subpixel True
    pos (-20,-100) 
    rotate 5
    block:
        ease .5 pos (0,150) rotate -5 #ypos 150 rotate 5 Bottom
        pause 0.25
        ease 1.0 pos (-20,-100) rotate 5 #250#-150 #rotate -10#  Top
        pause 0.1
        repeat

transform Laura_Hand_2():
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
     
transform Handcock_1L():
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

transform Handcock_2L():
    subpixel True
    rotate_pad False
    ypos 400 
    rotate 0
    block:
        ease .2 ypos 430 rotate -3 #410
        ease .5 ypos 400 rotate 0
        pause 0.1
        repeat
    
image Laura_HJ_Animation:  
    contains:
        ConditionSwitch(                                                # backside of the hand
            "not Speed", Transform("Laura_Hand_Under"), 
            "Speed == 1", At("Laura_Hand_Under", Laura_Hand_1()),
            "Speed >= 2", At("Laura_Hand_Under", Laura_Hand_2()),            
            "Speed", Null(),
            ),  
    contains:
        ConditionSwitch(                                                # cock
            "not Speed", Transform("Zero_Handcock"), 
            "Speed == 1", At("Zero_Handcock", Handcock_1L()),
            "Speed >= 2", At("Zero_Handcock", Handcock_2L()), 
            "Speed", Null(),
            ),  
        offset (0,0)
    contains:
        ConditionSwitch(                                                # fingers of the hand
            "not Speed", Transform("Laura_Hand_Over"), 
            "Speed == 1", At("Laura_Hand_Over", Laura_Hand_1()),
            "Speed >= 2", At("Laura_Hand_Over", Laura_Hand_2()), 
            "Speed", Null(),
            ),   
    anchor (0.51, -1.3)
    zoom 0.4#0.6
        
        
label Laura_HJ_Launch(Line = 0): 
    if renpy.showing("Laura_HJ_Animation"):        
        $ Trigger = "hand"
        return
    call Laura_Hide
    if Line == "L":      
        show Laura_Sprite at SpriteLoc(StageRight) zorder LauraLayer:
            alpha 1
            ease 1 zoom 1.7 offset (-150,200)#(0,200)
    else:     
        show Laura_Sprite at SpriteLoc(StageRight) zorder LauraLayer:
            alpha 1
            ease 1 zoom 1.7 offset (-150,200)#(0,200)
        with dissolve
            
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    else:
        $ Speed = 1
    pause .5
    $ Laura_Arms = 1
    show Laura_HJ_Animation at SpriteLoc(StageCenter) zorder 150 with easeinbottom:
        #xoffset 150
        offset (250,250)#(100,250)
    return
    
label Laura_HJ_Reset: # The sequence to the Rogue animations from handjob to default
    if not renpy.showing("Laura_HJ_Animation"):
        return    
    $ Speed = 0            
    $ Laura_Arms = 1
    hide Laura_HJ_Animation with easeoutbottom
    call Laura_Hide 
    show Laura_Sprite at SpriteLoc(L_SpriteLoc) zorder LauraLayer:
        alpha 1
        zoom 1.7 offset (-50,200)
    show Laura_Sprite at SpriteLoc(L_SpriteLoc) zorder LauraLayer:
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause .5
        ease .5 zoom 1 offset (0,0) 
    show Laura_Sprite at SpriteLoc(L_SpriteLoc) zorder LauraLayer:
        alpha 1
        zoom 1 offset (0,0)     
    return
    
# End Laura Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    

# Laura Misc Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
       
        
        
label L_Kissing_Launch(T = Trigger):    
    call Laura_Hide
    $ Trigger = T
    show Laura_Sprite at SpriteLoc(L_SpriteLoc) zorder LauraLayer
    show Laura_Sprite at SpriteLoc(StageCenter) zorder LauraLayer:
        ease 0.5 offset (0,0) zoom 2 alpha 1
    return
    
label L_Kissing_Smooch:   
    call LauraFace("kiss")  
    show Laura_Sprite at SpriteLoc(StageCenter) zorder LauraLayer:
        ease 0.5 xpos StageCenter offset (0,0) zoom 2 alpha 1
        pause 1
        ease 0.5 xpos L_SpriteLoc zoom 1      
    show Laura_Sprite at SpriteLoc(L_SpriteLoc) zorder LauraLayer:
        zoom 1
    call LauraFace("sexy")  
    return
            
label L_Breasts_Launch(T = Trigger):    
    call Laura_Hide
    $ Trigger = T
    show Laura_Sprite at SpriteLoc(L_SpriteLoc) zorder LauraLayer:
#        ease 0.5 offset (-100,-200) zoom 2
        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
    return
        
label L_Pussy_Launch(T = Trigger):
    call Laura_Hide    
    $ Trigger = T
    show Laura_Sprite at SpriteLoc(L_SpriteLoc) zorder LauraLayer:
        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
    return
        
label L_Pos_Reset(Pose = 0):    
    call Laura_Hide 
    show Laura_Sprite at SpriteLoc(L_SpriteLoc) zorder LauraLayer:
        ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
    show Laura_Sprite zorder LauraLayer:
        offset (0,0) 
        anchor (0.5, 0.0)
        zoom 1  
        xzoom 1 
        yzoom 1 
        alpha 1
        pos (L_SpriteLoc,50)
    $ Trigger = Pose
    return
    
label Laura_Hide:
        if renpy.showing("Laura_SexSprite"):
            call Laura_Sex_Reset
        hide Laura_SexSprite
        hide Laura_HJ_Animation
        hide Laura_BJ_Animation
        hide Laura_TJ_Animation 
        return

# Interface items //////////////////////////////////////////////////////////////////////////////

image GropeLeftBreast_L:    
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65#.7
        pos (195,380)#(215,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 60
        block: 
            ease 1 rotate 30
            ease 1 rotate 60
            repeat

image GropeRightBreast_L:    
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (110,380)#(120,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block: 
            ease 1 rotate -30 #-30
            ease 1 rotate -60 #-60 
            repeat

#image GropeBreast:
image LickRightBreast_L:   
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5 
        xzoom -0.45
        pos (95,355)#(105,375)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block: 
            ease .5 rotate -40 pos (75,330)#(85,345)  top         
            pause .5
            ease 1.5 rotate 30 pos (95,355)#(105,375) bottom
            repeat
            
image LickLeftBreast_L:   
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5 
        xzoom -0.45
        pos (195,360) #(200,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block: 
            ease .5 rotate -40 pos (190,340)#(190,380)            
            pause .5
            ease 1.5 rotate 30 pos (195,360)#(200,410)
            repeat

image GropeThigh_L: 
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (115,690)#(180,670)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        block:
            pause .5
            ease 1 rotate 110 pos (105,780) #(150,750) bottom
            ease 1 rotate 100 pos (115,690)   
            repeat

image GropePussy_L: 
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (120,620)#(200,600) -20
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice: 
                ease .5 rotate 190 pos (120,605) #(200,585)
                ease .75 rotate 170 pos (120,620)   
            choice: 
                ease .5 rotate 190 pos (120,605)
                pause .25
                ease 1 rotate 170 pos (120,620)             
            repeat

image FingerPussy_L: 
    contains:
        subpixel True
        "UI_Finger"       
        zoom 0.65
        pos (140,700)#(210,665)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice: 
                ease 1 rotate 40 pos (150,665)#(220,640)
                pause .5
                ease 1 rotate 50 pos (140,700)  #(210,665)     
            choice:                          
                ease .5 rotate 40 pos (150,665)
                pause .5
                ease 1.75 rotate 50 pos (140,700)  
            choice:                          
                ease 2 rotate 40 pos (150,665)
                pause .5
                ease 1 rotate 50 pos (140,700) 
            choice:                          
                ease .25 rotate 40 pos (150,665)
                ease .25 rotate 50 pos (140,700)
                ease .25 rotate 40 pos (150,665)
                ease .25 rotate 50 pos (140,700)
            repeat
            
image Lickpussy_L:   
    contains:
        subpixel True
        "UI_Tongue"        
        yzoom 0.45
        xzoom -0.45
        pos (155,650)#(230,625)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block: 
            easeout .5 rotate -50 pos (145,630) #(210,605)
            linear .5 rotate -60 pos (135,640) #(200,615)
            easein 1 rotate 10 pos (155,650) #(230,625)
            repeat

image VibratorRightBreast_L: 
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

image VibratorLeftBreast_L: 
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
            
image VibratorPussy_L: 
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

image VibratorAnal_L: 
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
            
image VibratorPussyInsert_L: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_L: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0



#Lesbian action animations.
image GirlGropeBothBreast_L: 
    contains:
        "GirlGropeLeftBreast_L"
    contains:
        "GirlGropeRightBreast_L"
    
image GirlGropeLeftBreast_L:  
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (220,370)#(240,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block: 
            ease 1 rotate 10 pos (220,380)#(280,390)
            ease 1 rotate -10 pos (220,370)
            repeat

image GirlGropeRightBreast_L:    
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (90,370) #(90,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10#-30
        block: 
            ease 1 rotate -40 pos (90,380)#(90,410)
            ease 1 rotate -10 pos (90,370)
            repeat

image GirlGropeThigh_L: 
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

image GirlGropePussy_LSelf:
    contains:
        "GirlGropePussy_L"
        anchor (0.5,0.5)
        rotate -40
#        yzoom -1
        pos (100,500) #(120,530)
    
image GirlGropePussy_L: 
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (130,595) #(205,595)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (130,590)
                ease .5 rotate 195 
                ease .75 rotate 210 
                ease .5 rotate 195 
            choice: #slow rub
                ease .5 rotate 210 pos (130,590)#-10+20
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (130,590) #(205,590)
                ease .75 rotate 200 pos (130,595) #(205,595)
                ease .5 rotate 205 pos (130,590)
                ease .75 rotate 200 pos (130,595)
            choice: #Fast stroke
                ease .3 rotate 205 pos (130,590)
                ease .3 rotate 200 pos (130,600)
                ease .3 rotate 205 pos (130,590)
                ease .3 rotate 200 pos (130,600)
            repeat

image GirlFingerPussy_L: 
    contains:
        subpixel True
        "UI_GirlFinger"       
        zoom .6
        pos (140,605)#(220,640)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (140,610)
                ease .5 rotate 195 
                ease .75 rotate 210 
                ease .5 rotate 195 
            choice: #slow rub
                ease .5 rotate 210 pos (140,610)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 ypos 620
                ease .75 rotate 200 ypos 625
                ease .5 rotate 205 ypos 620
                ease .75 rotate 200 ypos 625
            choice: #Fast stroke
                ease .3 rotate 205 ypos 620
                ease .3 rotate 200 ypos 630
                ease .3 rotate 205 ypos 620
                ease .3 rotate 200 ypos 630
            repeat

# Start Laura Faces / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label LauraFace(Emote = L_Emote, B = L_Blush, M = 0, Mouth = 0, Eyes = 0, Brows = 0):
        # Emote is the chosen emote, B is the lush state
        # M is whether the character is in a  manic state                 
        $ Emote = L_Emote if Emote == 5 else Emote
        $ B = L_Blush if B == 5 else B
        
        if (L_Forced or "angry" in L_RecentActions) and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "angry"     
        elif L_ForcedCount > 0 and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "sad"  
            
        if Emote == "normal":
                $ L_Mouth = "normal"
                $ L_Brows = "normal"
                $ L_Eyes = "normal"
        elif Emote == "angry":
                $ L_Mouth = "kiss"
                $ L_Brows = "angry"
                $ L_Eyes = "sexy"
        elif Emote == "bemused":
                $ L_Mouth = "lipbite"
                $ L_Brows = "sad"
                $ L_Eyes = "squint"
        elif Emote == "closed":
                $ L_Mouth = "normal"
                $ L_Brows = "sad"
                $ L_Eyes = "closed"  
        elif Emote == "confused":
                $ L_Mouth = "kiss"
                $ L_Brows = "confused"
                $ L_Eyes = "squint"
        elif Emote == "kiss":
                $ L_Mouth = "kiss"
                $ L_Brows = "sad"
                $ L_Eyes = "closed"
        elif Emote == "tongue":
                $ L_Mouth = "tongue"
                $ L_Brows = "sad"
                $ L_Eyes = "stunned" #"stunned"
        elif Emote == "manic":
                $ L_Mouth = "lipbite"
                $ L_Brows = "sad"
                $ L_Eyes = "surprised"
                $ L_Blush = 1
        elif Emote == "sad":
                $ L_Mouth = "sad"
                $ L_Brows = "sad"
                $ L_Eyes = "sexy"
        elif Emote == "sadside":
                $ L_Mouth = "sad"
                $ L_Brows = "sad"
                $ L_Eyes = "side"
        elif Emote == "sexy":
                $ L_Mouth = "lipbite"
                $ L_Brows = "sad"
                $ L_Eyes = "squint"
        elif Emote == "smile":
                if L_Love >= 700:
                    $ L_Mouth = "smile"
                else:
                    $ L_Mouth = "smirk"                
                $ L_Brows = "normal"
                $ L_Eyes = "normal"
        elif Emote == "sucking":
                $ L_Mouth = "sucking"
                $ L_Brows = "sad"
                $ L_Eyes = "closed"
        elif Emote == "surprised":
                $ L_Mouth = "kiss"
                $ L_Brows = "surprised"
                $ L_Eyes = "surprised"
        elif Emote == "startled":
                $ L_Mouth = "smile"
                $ L_Brows = "surprised"
                $ L_Eyes = "surprised"
        elif Emote == "down":
                $ L_Mouth = "sad"
                $ L_Brows = "sad"
                $ L_Eyes = "down"  
        elif Emote == "perplexed":
                $ L_Mouth = "smile"
                $ L_Brows = "sad"
                $ L_Eyes = "surprised"
        elif Emote == "sly":
                if L_Love >= 700:
                    $ L_Mouth = "smile"
                else:
                    $ L_Mouth = "smirk" 
                $ L_Brows = "confused"
                $ L_Eyes = "squint"
            
        if M:
                $ L_Eyes = "surprised"        
        if B > 1:
                $ L_Blush = 2
        elif B:
                $ L_Blush = 1
        else:
                $ L_Blush = 0
        
        if Mouth:
                $ L_Mouth = Mouth
        if Eyes:
                $ L_Eyes = Eyes
        if Brows:
                $ L_Brows = Brows
        
        return
        
        
# Laura's Wardrobe //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label LauraWardrobe:
    menu:      
        "View":
            while True:
                menu:
                    "Default":
                        call L_Pos_Reset
                    "Face":
                        call L_Kissing_Launch(0)
                    "Body":
                        call L_Pussy_Launch(0)
                    "Back":
                        jump LauraWardrobe 
        # Outfits
#        "Teacher outfit":
#            $ L_Outfit = "teacher"
#            call LauraOutfit
#        "Super outfit":
#            $ L_Outfit = "costume"
#            call LauraOutfit
        "Nude":
            $ L_Over = 0
            $ L_Chest = 0
            $ L_Legs = 0
            $ L_Panties = 0
            $ L_Gloves = 0
            $ L_Neck = 0
#            $ L_Outfit = "nude"
#            call LauraOutfit
        "Over":              
            while True:
                menu:
                    # Overshirts    
                    "Remove [L_Over]" if L_Over:
                        $ L_Over = 0
                    "Add Jacket":
                        $ L_Over = "jacket"  
                    "Add Towel":
                        $ L_Over = "towel" 
                    "Toggle up-top":
                        if L_Uptop:
                            $ L_Uptop = 0
                        else:
                            $ L_Uptop = 1   
                    "Back":
                        jump LauraWardrobe                
        "Chests":            
            while True:
                menu:
                    # Tops    
                    "Remove [L_Chest]" if L_Chest:
                        $ L_Chest = 0
                    "Add leather bra":
                        $ L_Chest = "leather bra"
                    "Add wolvie top":
                        $ L_Chest = "wolvie top"
                    "Add bikini top":
                        $ L_Chest = "bikini top"
                    "Add corset":
                        $ L_Chest = "corset"
                    "Add lace corset":
                        $ L_Chest = "lace corset"                       
                    "Toggle Piercings":
                        if L_Pierce == "ring":
                            $ L_Pierce = "barbell"
                        elif L_Pierce == "barbell":
                            $ L_Pierce = 0
                        else:
                            $ L_Pierce = "ring"
                    "Toggle up-top":
                        if L_Uptop:
                            $ L_Uptop = 0
                        else:
                            $ L_Uptop = 1   
                    "Back":
                        jump LauraWardrobe             
        
        "Legs":            
            while True:
                menu:
                    # Legs   
                    "Remove legs" if L_Legs:     
                        $ L_Legs = 0
                    "Add leather pants":
                        $ L_Legs = "leather pants"
                        $ L_Upskirt = 0
                    "Add mesh pants":
                        $ L_Legs = "mesh pants"
                        $ L_Upskirt = 0
                    "Add skirt":
                        $ L_Legs = "skirt"
                    "Toggle upskirt":
                        if L_Upskirt:
                            $ L_Upskirt = 0
                        else:
                            $ L_Upskirt = 1
                    "Back":
                        jump LauraWardrobe    
        
        "Underwear":            
            while True:
                menu:
                    # Underwear
                    "Hose":
                        menu:
                            "Add hose":     
                                $ L_Hose = "stockings"  
                            "Add garter":     
                                $ L_Hose = "garterbelt"  
                            "Add stockings and garter":     
                                $ L_Hose = "stockings and garterbelt"  
#                            "Add pantyhose":     
#                                $ L_Hose = "pantyhose"   
#                            "Add tights":     
#                                $ L_Hose = "tights"   
#                            "Add ripped hose":     
#                                $ L_Hose = "ripped pantyhose"   
#                            "Add ripped tights":     
#                                $ L_Hose = "ripped tights"   
#                            "Add tights":     
#                                $ L_Hose = "tights"    
                            "Remove hose" if L_Hose:     
                                $ L_Hose = 0  

#                    "toggle boots":    
#                        if not L_Boots:
#                            $ L_Boots = "thigh boots"   
#                        else:
#                            $ L_Boots = 0     
                        
                    "Remove panties" if L_Panties:     
                        $ L_Panties = 0     
                    "Add black panties":
                        $ L_Panties = "black panties"
#                    "Add shorts":
#                        $ L_Panties = "shorts"
                    "Add wolvie panties":
                        $ L_Panties = "wolvie panties"  
                    "Add bikini bottoms":
                        $ L_Panties = "bikini bottoms"  
                    "Add lace panties":
                        $ L_Panties = "lace panties"    
                    "pull down-up panties":
                        if L_PantiesDown:
                            $ L_PantiesDown = 0
                        else:
                            $ L_PantiesDown = 1
                    "Back":
                        jump LauraWardrobe    
        "Face":
            while True:
                menu: 
                    "Brows=[L_Brows], Eyes=[L_Eyes], Mouth=[L_Mouth]"
                    "Emotions":
                            call LauraEmotionEditor
                    "Toggle Brows":
                            if L_Brows == "normal":
                                $ L_Brows = "angry"
                            elif L_Brows == "angry":
                                $ L_Brows = "confused"
                            elif L_Brows == "confused":
                                $ L_Brows = "sad"
                            elif L_Brows == "sad":
                                $ L_Brows = "surprised"
                            else:
                                $ L_Brows = "normal"
                    "Toggle Eyes Emotions":
                            if L_Eyes == "normal":                          
                                $ L_Eyes = "surprised"
                            elif L_Eyes == "surprised":
                                $ L_Eyes = "sexy"
                            elif L_Eyes == "sexy":
                                $ L_Eyes = "squint"
                            elif L_Eyes == "squint":
                                $ L_Eyes = "closed"
                            else:
                                $ L_Eyes = "normal"
                    "Toggle Eyes Directions":
                            if L_Eyes == "normal":
                                $ L_Eyes = "side"
                            elif L_Eyes == "side":
                                $ L_Eyes = "down"
                            elif L_Eyes == "down":
                                $ L_Eyes = "leftside"
                            elif L_Eyes == "leftside":
                                $ L_Eyes = "stunned"
                            else:
                                $ L_Eyes = "normal"  
                    "Toggle Mouth Normal":
                            if L_Mouth  == "normal":
                                $ L_Mouth = "sad"
                            elif L_Mouth == "sad":
                                $ L_Mouth = "smile"
                            elif L_Mouth == "smile":
                                $ L_Mouth = "surprised"
                            else:
                                $ L_Mouth = "normal"  
                    "Toggle Mouth Sexy":
                            if L_Mouth  == "normal":
                                $ L_Mouth = "kiss"
                            elif L_Mouth == "kiss":
                                $ L_Mouth = "sucking"
                            elif L_Mouth == "sucking":
                                $ L_Mouth = "tongue"
                            elif L_Mouth == "tongue":
                                $ L_Mouth = "lipbite"
                            else:
                                $ L_Mouth = "normal"  
                    "Toggle Blush":
                        if L_Blush == 1:
                            $ L_Blush = 2
                        elif L_Blush:
                            $ L_Blush = 0
                        else:
                            $ L_Blush = 1
                            
                    "Back":
                            jump LauraWardrobe    
        "Misc":
            while True:
                menu: 
                    "Toggle Arm pose":
                        if Laura_Arms == 1:
                            $ Laura_Arms = 2
                        else:
                            $ Laura_Arms = 1
                    "Toggle Claws":
                        if L_Claws:
                            $ L_Claws = 0
                        else:
                            $ L_Claws = 1
                    "Toggle Wetness" if True:
                        if not L_Wet:
                            $ L_Wet = 1
                        elif L_Wet == 1:
                            $ L_Wet = 2
                        else:
                            $ L_Wet  = 0
                    "Toggle wet look" if True:
                        if not L_Water:
                            $ L_Water = 1
                        elif L_Water == 1:
                            $ L_Water = 3
                        else:
                            $ L_Water  = 0
                    "Toggle pubes":
                        if not L_Pubes:
                            $ L_Pubes = 1
                        else:
                            $ L_Pubes = 0
                    "Spunk":
                        menu:                            
                            "Toggle Mouth Spunk":
                                if "mouth" in L_Spunk:
                                    $ L_Spunk.remove("mouth")
                                else:
                                    $ L_Spunk.append("mouth")
                            "Toggle hand Spunk":
                                if "hand" in L_Spunk:
                                    $ L_Spunk.remove("hand")
                                else:
                                    $ L_Spunk.append("hand")                                    
                            "Toggle Facial Spunk":
                                if "facial" in L_Spunk and "hair" not in L_Spunk:
                                    $ L_Spunk.append("hair")
                                elif "facial" in L_Spunk:
                                    $ L_Spunk.remove("facial")                
                                    $ L_Spunk.remove("hair")
                                else:
                                    $ L_Spunk.append("facial")                
                            "Toggle Pussy Spunk" if True:
                                if "in" in L_Spunk:
                                    $ L_Spunk.remove("in")
                                else:
                                    $ L_Spunk.append("in")             
                            "Toggle Anal Spunk" if True:
                                if "anal" in L_Spunk:
                                    $ L_Spunk.remove("anal")
                                else:
                                    $ L_Spunk.append("anal")        
                            "Toggle Belly Spunk" if True:
                                if "belly" in L_Spunk:
                                    $ L_Spunk.remove("belly")
                                else:
                                    $ L_Spunk.append("belly")        
                            "Toggle Tits Spunk" if True:
                                if "tits" in L_Spunk:
                                    $ L_Spunk.remove("tits")
                                else:
                                    $ L_Spunk.append("tits")
                    "Toggle Piercings":
                        if L_Pierce == "ring":
                            $ L_Pierce = "barbell"
                        elif L_Pierce == "barbell":
                            $ L_Pierce = 0
                        else:
                            $ L_Pierce = "ring"
                    "Add leash choker" if not L_Neck:
                        $ L_Neck = "leash choker"
                    "Remove choker" if L_Neck:
                        $ L_Neck = 0
                        
                    "Add wristbands" if not L_Arms:
                        $ L_Arms = "wrists"
                    "Remove Gloves" if L_Arms:
                        $ L_Arms = 0
                    "Back":
                        jump LauraWardrobe               
#        "Set Custom Outfit #1.":
#            $ L_Custom[0] = 1
#            $ L_Custom[1] = L_Arms
#            $ L_Custom[2] = L_Legs
#            $ L_Custom[3] = L_Over
#            $ L_Custom[4] = L_Under #fix, this can be changed to something else, no longer necessary
#            $ L_Custom[5] = L_Chest
#            $ L_Custom[6] = L_Panties 
#            $ L_Custom[7] = L_Pubes 
#            $ L_Custom[8] = L_Hair
#            $ L_Custom[9] = L_Hose
#        "Wear Custom Outfit #[L_Custom[0]]." if L_Custom[0]:
#            $ Line = L_Outfit
#            $ L_Outfit = "custom1"
#            call RogueOutfit
#            $ L_Outfit = Line
        "Nothing":
            return
    jump LauraWardrobe
return

label LauraEmotionEditor(CountStore = "normal"):
    menu:
        "Emotions1: Normal Angry Smiling Sexy Surprised Bemused Manic.":        
            menu:
                "Normal":
                    $ L_Emote = "normal"
                    call LauraFace
                "Angry":
                    $ L_Emote = "angry"
                    call LauraFace
                "Smiling":
                    $ L_Emote = "smile"
                    call LauraFace
                "Sexy":
                    $ L_Emote = "sexy"
                    call LauraFace
                "Suprised":
                    $ L_Emote = "surprised"
                    call LauraFace
                "Bemused":
                    $ L_Emote = "bemused"
                    call LauraFace
                "Manic":
                    $ L_Emote = "manic"
                    call LauraFace
                    
        "Emotions2: Sad Sucking Kiss Tongue Confused Closed Down.":  
            menu:
                "Sad":
                    $ L_Emote = "sad"
                    call LauraFace
                "Sucking":
                    $ L_Emote = "sucking"
                    call LauraFace
                "kiss":
                    $ L_Emote = "kiss"
                    call LauraFace
                "Tongue":
                    $ L_Emote = "tongue"
                    call LauraFace
                "confused":
                    $ L_Emote = "confused"
                    call LauraFace
                "Closed":
                    $ L_Emote = "closed"
                    call LauraFace
                "Down":
                    $ L_Emote = "down"
                    call LauraFace
                    
        "Emotions3: Sadside Startled Perplexed Sly":  
            menu:
                "Sadside":
                    $ L_Emote = "sadside"
                    call LauraFace
                "Startled":
                    $ L_Emote = "startled"
                    call LauraFace
                "Perplexed":
                    $ L_Emote = "perplexed"
                    call LauraFace
                "Sly":
                    $ L_Emote = "sly"
                    call LauraFace
        "Toggle Mouth Spunk":
            if "mouth" in L_Spunk:
                $ L_Spunk.remove("mouth")
            else:
                $ L_Spunk.append("mouth")
        "Toggle hand Spunk":
            if "hand" in L_Spunk:
                $ L_Spunk.remove("hand")
            else:
                $ L_Spunk.append("hand")
                
        "Toggle Facial Spunk":
            if "facial" in L_Spunk and "hair" not in L_Spunk:
                $ L_Spunk.append("hair")
            elif "facial" in L_Spunk:
                $ L_Spunk.remove("facial")                
                $ L_Spunk.remove("hair")
            else:
                $ L_Spunk.append("facial")
            
        "Blush":
            if L_Blush == 2:
                $ L_Blush = 0
            elif L_Blush:
                $ L_Blush = 2
            else:
                $ L_Blush = 1  
        "Exit.":
            return
    jump LauraEmotionEditor
return