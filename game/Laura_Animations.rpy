﻿# Basic character Sprites

image Laura_Sprite:
    LiveComposite(                
        (402,965), 
        (0,0), "Laura_Sprite_HairBack", 
        (0,0), ConditionSwitch(            
            #panties down back        
            "not LauraX.Panties or not LauraX.PantiesDown or (LauraX.Legs and LauraX.Legs != 'skirt' and not LauraX.Upskirt)", Null(), 
            "LauraX.Panties == 'wolvie panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Back.png",   
            "LauraX.Panties == 'bikini bottoms'", "images/LauraSprite/Laura_Sprite_Panties_Bikini_Back.png",   
            "True", "images/LauraSprite/Laura_Sprite_Panties_Lace_Back.png",   
            ), 
        (0,0), ConditionSwitch(
            #backside of arms
            "LauraX.ArmPose == 2", "images/LauraSprite/Laura_Sprite_Arm_Back2.png",   
            "True", "images/LauraSprite/Laura_Sprite_Arm_Back1.png", #if LauraX.Arms == 1 
            ),     
#        (0,0), ConditionSwitch(
#            #arms wristband
#            "LauraX.Arms == 'wrists'", "images/LauraSprite/Laura_Sprite_Wrist_Right.png", # one hand up
#            "True", Null(),     
#            ), 
        (0,0), ConditionSwitch(
            #L Over under
            "LauraX.Uptop and LauraX.Over == 'jacket'", "images/LauraSprite/Laura_Sprite_Jacket_Back_Up.png", # one hand up
            "LauraX.Over == 'jacket'", "images/LauraSprite/Laura_Sprite_Jacket_Back.png", # one hand up
            "True", Null(),     
            ), 
        #body
        (0,0), "images/LauraSprite/Laura_Sprite_Body.png",
        
        #shifted here
        (0,0), ConditionSwitch(
            #arms midlayer
            "LauraX.ArmPose == 2", "images/LauraSprite/Laura_Sprite_Arm_Mid2.png",         # one hand up
            "True", "images/LauraSprite/Laura_Sprite_Arm_Mid1.png", #if LauraX.Arms == 1   # Crossed        
            ),  
        # tits
        (0,0), "images/LauraSprite/Laura_Sprite_Tits.png", 
        (0,0), ConditionSwitch(
            #Water effect 
            "LauraX.Water and LauraX.ArmPose == 1", "images/LauraSprite/Laura_Sprite_Water1.png",   
            "LauraX.Water", "images/LauraSprite/Laura_Sprite_Water2.png",   
            "True", Null(),        
            ),       
        (0,0), ConditionSwitch(
            #arms wristband
            "LauraX.Arms == 'wrists' and LauraX.ArmPose == 2", "images/LauraSprite/Laura_Sprite_Wrist2.png", # one hand up
            "LauraX.Arms == 'wrists'", "images/LauraSprite/Laura_Sprite_Wrist1.png", # one hand up
            "True", Null(),     
            ),   
        #shifted here
        
        (145,560), ConditionSwitch(    #(225,560)                                                                     
            #Personal Wetness            
            "not LauraX.Wet", Null(),
            "LauraX.Legs and LauraX.Legs != 'skirt' and not LauraX.Upskirt", Null(),   
            "LauraX.Panties and not LauraX.PantiesDown and LauraX.Wet <= 1", Null(),   
            "LauraX.Wet == 1", ConditionSwitch( #Wet = 1
                    "LauraX.Panties and LauraX.PantiesDown", AlphaMask("Wet_Drip","Laura_Drip_MaskP"),  
                    "LauraX.Legs and LauraX.Legs != 'skirt'", AlphaMask("Wet_Drip","Laura_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip","Laura_Drip_Mask"), #only plays if nothing is in the way
                    ),
            "True", ConditionSwitch( #Wet = 2+
                    "LauraX.Panties and LauraX.PantiesDown", AlphaMask("Wet_Drip2","Laura_Drip_MaskP"),
                    "LauraX.Legs and LauraX.Legs != 'skirt'", AlphaMask("Wet_Drip2","Laura_Drip_MaskP"),
                    "LauraX.Panties", AlphaMask("Wet_Drip","Laura_Drip_Mask"), #"Wet_Drip2",# 
                    "True", AlphaMask("Wet_Drip2","Laura_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (145,560), ConditionSwitch(    #(225,560)                                                                     
            #dripping spunk            
            "'in' not in LauraX.Spunk and 'anal' not in LauraX.Spunk", Null(),
            "LauraX.Legs and LauraX.Legs != 'skirt' and not LauraX.Upskirt", Null(),   
            "LauraX.Panties and not LauraX.PantiesDown and LauraX.Wet <= 1", Null(),   
            "True", ConditionSwitch( #Wet = 2+
                    "LauraX.Panties and LauraX.PantiesDown", AlphaMask("Spunk_Drip2","Laura_Drip_MaskP"),
#                    "LauraX.Legs and LauraX.Legs != 'skirt'", AlphaMask("Spunk_Drip2","Laura_Drip_MaskP"), #add if pantes have down art
                    "LauraX.Panties", AlphaMask("Spunk_Drip","Laura_Drip_Mask"), #"Wet_Drip2",# 
                    "True", AlphaMask("Spunk_Drip2","Laura_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (0,0), ConditionSwitch(
            #pubes 
            "LauraX.Pubes", "images/LauraSprite/Laura_Sprite_Pubes.png",   
            "True", Null(),        
            ),      
        (0,0), ConditionSwitch(
            #nude lower piercings        
            "not LauraX.Pierce", Null(),  
            "LauraX.Panties and not LauraX.PantiesDown", Null(), 
            "LauraX.Legs != 'skirt' and LauraX.Legs and not LauraX.Upskirt", Null(), #skirt if wearing a skirt
            "LauraX.Pierce == 'barbell'", "images/LauraSprite/Laura_Sprite_Barbell_Pussy.png",  
            "LauraX.Pierce == 'ring'", "images/LauraSprite/Laura_Sprite_Ring_Pussy.png",  
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(
            #stockings    
            "LauraX.Hose == 'stockings' or LauraX.Hose == 'stockings and garterbelt'", "images/LauraSprite/Laura_Sprite_Stockings.png",
            "True", Null(),
            ),     
        (0,0), ConditionSwitch(
            #garterbelt    
            "LauraX.Hose == 'stockings and garterbelt' or LauraX.Hose == 'garterbelt'", "images/LauraSprite/Laura_Sprite_Garters.png",
            "True", Null(),
            ),              
        (0,0), ConditionSwitch(
            #panties    
            "not LauraX.Panties", Null(),
            "LauraX.PantiesDown", ConditionSwitch(                   
                    #if the panties are down
                    "not LauraX.Legs or LauraX.Upskirt or LauraX.Legs == 'skirt'", ConditionSwitch(                   
                            #if she's wearing a skirt or nothing else                    
                            "LauraX.Panties == 'wolvie panties' and LauraX.Wet", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Down_W.png", 
                            "LauraX.Panties == 'wolvie panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Down.png",                             
                            "LauraX.Panties == 'lace panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace_Down.png", 
                            "LauraX.Panties == 'bikini bottoms'", "images/LauraSprite/Laura_Sprite_Panties_Bikini_Down.png", 
                            "True", "images/LauraSprite/Laura_Sprite_Panties_Lace_Down.png", #fix
                            ),         
                    "True", Null(),
                    ),                    
            "True", ConditionSwitch(                
                    #if she's got panties and they are not down
                    "LauraX.Wet", ConditionSwitch(   
                        #if she's  wet                            
                        "LauraX.Panties == 'wolvie panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_W.png",
                        "LauraX.Panties == 'lace panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace.png", 
                        "LauraX.Panties == 'bikini bottoms'", "images/LauraSprite/Laura_Sprite_Panties_Bikini.png", 
                        "True", "images/LauraSprite/Laura_Sprite_Panties_Leather.png", 
                        ),
                    "True", ConditionSwitch(   
                        #if she's not wet                            
                        "LauraX.Panties == 'wolvie panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie.png",
                        "LauraX.Panties == 'lace panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace.png", 
                        "LauraX.Panties == 'bikini bottoms'", "images/LauraSprite/Laura_Sprite_Panties_Bikini.png", 
                        "True", "images/LauraSprite/Laura_Sprite_Panties_Leather.png", 
                        ),                    
                    ),    
            ),            
        (0,0), ConditionSwitch(
            #pants    
            "not LauraX.Legs", Null(),
            "LauraX.Upskirt", ConditionSwitch(                
                        #if the skirt's up or pants down 
                        "LauraX.Legs == 'skirt'", "images/LauraSprite/Laura_Sprite_Skirt_Up.png", 
                        "True", Null(),                       
                        ),                    
            "True", ConditionSwitch(                
                    #if it's the ring pericings
                    "LauraX.Wet", ConditionSwitch(   
                        #if she's not wet
                        "LauraX.Legs == 'leather pants'", "images/LauraSprite/Laura_Sprite_Pants_Leather.png",  
                        "LauraX.Legs == 'mesh pants'", "images/LauraSprite/Laura_Sprite_Pants_Mesh.png",   
#                        "LauraX.Legs == 'yoga pants'", "images/LauraSprite/Laura_Sprite_Pants_YogaWet.png",       
                        "LauraX.Legs == 'skirt'", "images/LauraSprite/Laura_Sprite_Skirt.png", 
                        "True", Null(),
                        ),                    
                    "True", ConditionSwitch(   
                        #if she's wet
                        "LauraX.Legs == 'leather pants'", "images/LauraSprite/Laura_Sprite_Pants_Leather.png",   
                        "LauraX.Legs == 'mesh pants'", "images/LauraSprite/Laura_Sprite_Pants_Mesh.png",  
#                        "LauraX.Legs == 'yoga pants'", "images/LauraSprite/Laura_Sprite_Pants_Yoga.png",       
                        "LauraX.Legs == 'skirt'", "images/LauraSprite/Laura_Sprite_Skirt.png", 
                        "True", Null(),
                        ),                    
                    ),                  
            ),    
        (0,0), ConditionSwitch(
            #clothed lower piercings         
            "LauraX.Legs == 'skirt'", Null(),
            "LauraX.Pierce == 'barbell'", ConditionSwitch(   
                    #if it's the barbell pericings 
                    "LauraX.Legs and not LauraX.Upskirt", "images/LauraSprite/Laura_Sprite_Barbell_PussyC.png",  
                    "LauraX.Panties and not LauraX.PantiesDown", "images/LauraSprite/Laura_Sprite_Barbell_PussyC.png", 
                    "True", Null(),
                    ),    
            "LauraX.Pierce == 'ring'", ConditionSwitch(   
                    #if it's the ring pericings
                    "LauraX.Legs and not LauraX.Upskirt", "images/LauraSprite/Laura_Sprite_Ring_PussyC.png",  
                    "LauraX.Panties and not LauraX.PantiesDown", "images/LauraSprite/Laura_Sprite_Ring_PussyC.png", 
                    "True", Null(),
                    ),
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(
            #Personal Wetness            
            "not LauraX.Wet", Null(),
            "LauraX.Legs and LauraX.Wet <= 1", Null(),
            "LauraX.Legs == 'skirt'", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Wetness.png",       #LauraX.Wet >1
            ),     
        (0,0), ConditionSwitch(
            #pussy spunk 
            "LauraX.Legs and not LauraX.Upskirt", Null(),
            "'in' in LauraX.Spunk or 'anal' in LauraX.Spunk", "images/LauraSprite/Laura_Sprite_Spunk_Pussy.png",
            "True", Null(), 
            ),  
        #where arms and tits were before
        (0,0), ConditionSwitch(
            #nude peircings      
            "not LauraX.Pierce", Null(),  
            "LauraX.Pierce == 'barbell'", "images/LauraSprite/Laura_Sprite_Barbell_Tits.png",   
            "LauraX.Pierce == 'ring'", "images/LauraSprite/Laura_Sprite_Ring_Tits.png",               
            "True", Null(),              
            ),    
        (0,0), ConditionSwitch(               
            #neck            
            "LauraX.Neck == 'leash choker'", "images/LauraSprite/Laura_Sprite_Neck_Leash.png",       
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(                                                                        
            #Chest layer
            "LauraX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "LauraX.Chest == 'leather bra'", "images/LauraSprite/Laura_Sprite_Bra_Leather_Up.png", 
                    "LauraX.Chest == 'wolvie top'", "images/LauraSprite/Laura_Sprite_Top_Wolvie_Up.png",   
                    "LauraX.Chest == 'bikini top'", "images/LauraSprite/Laura_Sprite_Top_Bikini_Up.png",   
                    "LauraX.Chest == 'corset'", "images/LauraSprite/Laura_Sprite_Top_Corset_Up.png",   
                    "LauraX.Chest == 'lace corset'", "images/LauraSprite/Laura_Sprite_Top_Corset_Lace_Up.png",   
                    "True", Null(),     
                    ),     
            "LauraX.Chest == 'leather bra'", "images/LauraSprite/Laura_Sprite_Bra_Leather.png", 
            "LauraX.Chest == 'wolvie top'", "images/LauraSprite/Laura_Sprite_Top_Wolvie.png",   
            "LauraX.Chest == 'bikini top'", "images/LauraSprite/Laura_Sprite_Top_Bikini.png",   
            "LauraX.Chest == 'corset'", "images/LauraSprite/Laura_Sprite_Top_Corset.png",   
            "LauraX.Chest == 'lace corset'", "images/LauraSprite/Laura_Sprite_Top_Corset_Lace.png",   
            "True", Null(),              
            ),     

        (0,0), ConditionSwitch(
            #L Over
            "LauraX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "LauraX.Over == 'jacket' and LauraX.ArmPose == 2", "images/LauraSprite/Laura_Sprite_Jacket_A2_Up.png", # one hand up
                    "LauraX.Over == 'jacket'", "images/LauraSprite/Laura_Sprite_Jacket_A1_Up.png", # one hand up
#                    "LauraX.Over == 'towel'", "images/LauraSprite/Laura_Sprite_Towel.png",
                    "True", Null(),     
                    ),                
            "LauraX.Over == 'jacket' and LauraX.ArmPose == 2", "images/LauraSprite/Laura_Sprite_Jacket_A2.png", # one hand up
            "LauraX.Over == 'jacket'", "images/LauraSprite/Laura_Sprite_Jacket_A1.png", # one hand up
            "LauraX.Over == 'towel'", "images/LauraSprite/Laura_Sprite_Towel.png",
            "True", Null(),     
            ),         
        (0,0), ConditionSwitch(                                                                        
            #clothed peircings        
            "not LauraX.Pierce or (not LauraX.Over and not LauraX.Chest)", Null(),  
            "LauraX.Over == 'jacket'", Null(),
            "LauraX.Pierce == 'barbell'",  "images/LauraSprite/Laura_Sprite_Barbell_TitsC.png", 
            "LauraX.Pierce == 'ring'", "images/LauraSprite/Laura_Sprite_Ring_TitsC.png", 
            "True", Null(), 
            ),   
                
        (0,0), ConditionSwitch(
            #belly spunk 
            "'belly' in LauraX.Spunk", "images/LauraSprite/Laura_Sprite_Spunk_Belly.png",
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(
            #breast spunk      
            "'tits' in LauraX.Spunk", "images/LauraSprite/Laura_Sprite_Spunk_Tits.png",  
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
            "LauraX.ArmPose == 2", "images/LauraSprite/Laura_Sprite_Arm_Left2.png", # one hand up
            "True", Null(),     
            ), 
        (0,0), ConditionSwitch(
            #Water effect 
            "LauraX.Water and LauraX.ArmPose == 2", "images/LauraSprite/Laura_Sprite_Water2top.png",  
            "True", Null(),     
            ), 
        (0,0), ConditionSwitch(
            #arms wristband
            "LauraX.ArmPose == 2 and LauraX.Arms == 'wrists'", "images/LauraSprite/Laura_Sprite_Wrist_Left2.png", # one hand up
            "True", Null(),     
            ), 
        (0,0), ConditionSwitch(
            #jacket arm toplayer
            "LauraX.Over == 'jacket' and LauraX.ArmPose == 2", "images/LauraSprite/Laura_Sprite_Jacket_A2Top.png", # one hand up
            "True", Null(),     
            ), 
        (0,0), ConditionSwitch(
            #claws
            "LauraX.ArmPose == 2 and LauraX.Claws", "images/LauraSprite/Laura_Sprite_Claws2.png", # one hand up
            "True", Null(),     
            ), 
        
        (0,0), ConditionSwitch( 
            #hand spunk 
            "LauraX.ArmPose == 2 or 'hand' not in LauraX.Spunk", Null(),  
            "True", "images/LauraSprite/Laura_Sprite_Spunk_Hand.png",   
            ),  
#        (0,0), ConditionSwitch(                                                                         #Props
#            "not LauraX.Held or LauraX.ArmPose != 2", Null(), 
#            "LauraX.ArmPose == 2 and LauraX.Held == 'phone'", "images/LauraSprite/Laura_held_phone.png",
#            "LauraX.ArmPose == 2 and LauraX.Held == 'dildo'", "images/LauraSprite/Laura_held_dildo.png",
#            "LauraX.ArmPose == 2 and LauraX.Held == 'vibrator'", "images/LauraSprite/Laura_held_vibrator.png",
#            "LauraX.ArmPose == 2 and LauraX.Held == 'panties'", "images/LauraSprite/Laura_held_panties.png",
#            "True", Null(), 
#            ),        
        (0,0), ConditionSwitch(
            #UI tool for When Laura is masturbating using Trigger3 actions
            "Trigger == 'lesbian' or not Trigger3 or Ch_Focus != LauraX", Null(),
            
            #this is not a lesbian thing, and a trigger is set, and Laura is the primary. . .
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_LauraSelf",  
            "Trigger3 == 'fondle breasts'", ConditionSwitch(                                                                      
                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeLeftBreast_Laura", 
                        #When zero is working the right breast, fondle left
                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeRightBreast_Laura",   
                        #When zero is working the left breast, fondle right
                    "True", "GirlGropeBothBreast_Laura",
                        #else, fondle both
                    ),  
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast_Laura",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy_Laura",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy_Laura",
            "Trigger3 == 'vibrator anal'", "VibratorAnal_Laura",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy_Laura",            
            "True", Null(),             
            ),                        
        (0,0), ConditionSwitch(  
            #UI tool for Trigger5(Threesome masutrbation) actions
            "not Trigger5 or Trigger4 != 'masturbation' or Ch_Focus == LauraX", Null(), 
            
            #Laura is not primary, and T4 is masturbation, and a T5 is selected
            "Trigger5 == 'fondle pussy' and Trigger != 'sex' and LauraX.Lust >= 70", "GirlFingerPussy_Laura",
            "Trigger5 == 'fondle pussy'", "GirlGropePussy_Laura",            
            "Trigger5 == 'fondle breasts'", "GirlGropeRightBreast_Laura",
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
            "not Trigger or Ch_Focus != LauraX", Null(),            
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast_Laura",
            "Trigger == 'fondle thighs'", "GropeThigh_Laura",            
            "Trigger == 'fondle breasts'", "GropeLeftBreast_Laura",
            "Trigger == 'suck breasts'", "LickRightBreast_Laura",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_Laura",
            "Trigger == 'fondle pussy'", "GropePussy_Laura",
            "Trigger == 'lick pussy'", "Lickpussy_Laura",
            "Trigger == 'vibrator pussy'", "VibratorPussy_Laura",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy_Laura",
            "Trigger == 'vibrator anal'", "VibratorAnal_Laura",
            "Trigger == 'vibrator anal insert'", "VibratorPussy_Laura",            
            "True", Null(), 
            ),            
        (0,0), ConditionSwitch(                
            #UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus != LauraX", Null(),
            
            #Laura is primary and an offhand trigger is active            
            "Trigger2 == 'fondle breasts'", ConditionSwitch(                                                                      
                    "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast_Laura", 
                        #When zero is sucking on the right breast, fondle left
                    "True", "GropeRightBreast_Laura",
                        #else, fondle right
                    ),  
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast_Laura",       
                #When sucking right breast, vibrator left            
            "Trigger2 == Trigger", Null(),
                #When both triggers are the same, do nothing              
            "Trigger2 == 'suck breasts'", "LickLeftBreast_Laura",        
            "Trigger2 == 'fondle pussy'", "GropePussy_Laura",
            "Trigger2 == 'lick pussy'", "Lickpussy_Laura",       
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast_Laura",
            "Trigger2 == 'vibrator pussy'", "VibratorPussy_Laura",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy_Laura",
            "Trigger2 == 'vibrator anal'", "VibratorAnal_Laura",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy_Laura",            
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(  
            #UI tool for Trigger4(Threesome) actions (ie Rogue's hand on her)
            "not Trigger4 or Ch_Focus != LauraX", Null(),
            
            # There is a threesome trigger set and Laura is the target of it
            "Trigger4 == 'fondle pussy' and Trigger != 'sex' and LauraX.Lust >= 70", "GirlFingerPussy_Laura",
            "Trigger4 == 'fondle pussy'", "GirlGropePussy_Laura",            
            "Trigger4 == 'lick pussy'", "Lickpussy_Laura",
            "Trigger4 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Laura", 
            "Trigger4 == 'suck breasts'", "LickRightBreast_Laura",      
            "Trigger4 == 'fondle breasts'", ConditionSwitch( 
                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeLeftBreast_Laura", #When zero is working the right breast, fondle left                                                  
#                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeRightBreast_Laura",  #When zero is working the left breast, fondle right                                         
#                    "Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts'", "GirlGropeRightBreast_Laura", #When zero is working the left breast, fondle right 
                    "True", "GirlGropeRightBreast_Laura",#else, fondle right
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
            "Trigger != 'lesbian' or Ch_Focus == LauraX or not Trigger3", Null(),            
            
            # If there is a Trigger3 and Laura is not the focus
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and LauraX.Lust >= 70", "GirlFingerPussy_Laura",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_Laura",            
            "Trigger3 == 'lick pussy'", "Lickpussy_Laura",
            "Trigger3 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Laura", 
            "Trigger3 == 'suck breasts'", "LickRightBreast_Laura",            
            "Trigger3 == 'fondle breasts'", ConditionSwitch( 
                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeLeftBreast_Laura",                    
                        #When zero is working the right breast, fondle left                                                  
                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeRightBreast_Laura", 
                        #When zero is working the left breast, fondle right                                         
                    "Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts'", "GirlGropeLeftBreast_Laura", 
                        #When zero is working the right breast, fondle left 
                    "True", "GirlGropeRightBreast_Laura",                    
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
            "not LauraX.Hair", Null(),
            "renpy.showing('Laura_BJ_Animation')", Null(), 
#            "renpy.showing('Laura_SexSprite')", "images/LauraSex/Laura_Sprite_Hair_Long_UnderSex.png",
            "LauraX.Hair == 'wet' or LauraX.Water", "images/LauraSprite/Laura_Sprite_Hair_Wet_Under.png",
            "LauraX.Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Under.png",   
            "True", Null(),        
            ),   
#    "images/LauraSprite/Laura_Sprite_Hair_Long_Under.png"       
    anchor (0.6, 0.0)                
    zoom .5                   

image Laura_Sprite_HairMid: 
    ConditionSwitch(
            #hair back 
            "not LauraX.Hair", Null(),
            "renpy.showing('Laura_BJ_Animation')", Null(), 
#            "renpy.showing('Laura_SexSprite')", "images/LauraSex/Laura_Sprite_Hair_Long_UnderSex.png",
            "LauraX.Hair == 'wet' or LauraX.Water", Null(),
            "LauraX.Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Mid.png",   
            "True", Null(),        
            ),     
    anchor (0.6, 0.0)                
    zoom .5 
 
image Laura_Sprite_HairTop: 
    ConditionSwitch(
            #hair back 
            "not LauraX.Hair", Null(),
            "renpy.showing('Laura_SexSprite')", "images/LauraSex/Laura_Sprite_Hair_Long_OverSex.png",
            "LauraX.Hair == 'wet' or LauraX.Water", "images/LauraSprite/Laura_Sprite_Hair_Wet_Over.png",
            "LauraX.Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Over.png",
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
                "renpy.showing('Laura_SexSprite')", "images/LauraSex/Laura_Sprite_Hair_Long_UnderSex.png", 
                "True", Null(),                        
                ),         
        (0,0), ConditionSwitch(
                # Face background plate
                "LauraX.Blush == 2", "images/LauraSprite/Laura_Sprite_Head_Blush2.png", 
                "LauraX.Blush", "images/LauraSprite/Laura_Sprite_Head_Blush.png",  
                "True", "images/LauraSprite/Laura_Sprite_Head.png",                        
                ),        
        (0,0), ConditionSwitch(#chin spunk
            "'chin' not in LauraX.Spunk", Null(),
            "renpy.showing('Laura_BJ_Animation') and Speed >= 2", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Spunk_Chin.png",            
            ),                
        (0,0), ConditionSwitch(#Mouths 
            "renpy.showing('Laura_BJ_Animation')", "images/LauraSprite/Laura_Sprite_Mouth_SuckingBJ.png", #and Speed >= 2
            "LauraX.Mouth == 'normal'", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png",
            "LauraX.Mouth == 'lipbite'", "images/LauraSprite/Laura_Sprite_Mouth_Lipbite.png",
            "LauraX.Mouth == 'sucking'", "images/LauraSprite/Laura_Sprite_Mouth_Sucking.png",            
            "LauraX.Mouth == 'kiss'", "images/LauraSprite/Laura_Sprite_Mouth_Kiss.png",
            "LauraX.Mouth == 'sad'", "images/LauraSprite/Laura_Sprite_Mouth_Sad.png",
            "LauraX.Mouth == 'smile'", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png",
            "LauraX.Mouth == 'surprised'", "images/LauraSprite/Laura_Sprite_Mouth_Surprised.png",            
            "LauraX.Mouth == 'tongue'", "images/LauraSprite/Laura_Sprite_Mouth_Tongue.png",                
            "LauraX.Mouth == 'grimace'", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png",              
            "LauraX.Mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Mouth_Smirk.png",                    
#            "LauraX.Mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png",         
            "True", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png",
            ),         
        (0,0), ConditionSwitch(#Mouth spunk 
            "'mouth' not in LauraX.Spunk", Null(),
            "renpy.showing('Laura_BJ_Animation')", "images/LauraSprite/Laura_Sprite_Spunk_MouthSuck.png", #and Speed >= 2
            "LauraX.Mouth == 'normal'", "images/LauraSprite/Laura_Sprite_Spunk_MouthNeutral.png",
            "LauraX.Mouth == 'lipbite'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmirk.png",
            "LauraX.Mouth == 'sucking'", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",            
            "LauraX.Mouth == 'kiss'", "images/LauraSprite/Laura_Sprite_Spunk_MouthKiss.png",
            "LauraX.Mouth == 'sad'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSad.png",
            "LauraX.Mouth == 'smile'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmile.png",
            "LauraX.Mouth == 'surprised'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSad.png",            
            "LauraX.Mouth == 'tongue'", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",                
            "LauraX.Mouth == 'grimace'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmile.png",              
            "LauraX.Mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmirk.png",      
            "True", "images/LauraSprite/Laura_Sprite_Spunk_MouthNeutral.png",
            ),                                                        
        (0,0), ConditionSwitch(                                                                       
            #brows
            "LauraX.Blush >= 2", ConditionSwitch(
                    "LauraX.Brows == 'normal'", "images/LauraSprite/Laura_Sprite_Brows_Normal_B.png",
                    "LauraX.Brows == 'angry'", "images/LauraSprite/Laura_Sprite_Brows_Angry_B.png",
                    "LauraX.Brows == 'sad'", "images/LauraSprite/Laura_Sprite_Brows_Sad_B.png",
                    "LauraX.Brows == 'surprised'", "images/LauraSprite/Laura_Sprite_Brows_Surprised_B.png",        
                    "LauraX.Brows == 'confused'", "images/LauraSprite/Laura_Sprite_Brows_Confused_B.png",
                    "True", "images/LauraSprite/Laura_Sprite_Brows_Normal_B.png",
                    ),
            "True", ConditionSwitch(
                    "LauraX.Brows == 'normal'", "images/LauraSprite/Laura_Sprite_Brows_Normal.png",
                    "LauraX.Brows == 'angry'", "images/LauraSprite/Laura_Sprite_Brows_Angry.png",
                    "LauraX.Brows == 'sad'", "images/LauraSprite/Laura_Sprite_Brows_Sad.png",
                    "LauraX.Brows == 'surprised'", "images/LauraSprite/Laura_Sprite_Brows_Surprised.png",        
                    "LauraX.Brows == 'confused'", "images/LauraSprite/Laura_Sprite_Brows_Confused.png",
                    "True", "images/LauraSprite/Laura_Sprite_Brows_Normal.png",
                    ),
            ),        
        (0,0), "Laura Blink",     #Eyes    
        (0,0), ConditionSwitch(                
            #Hair mid
            "LauraX.Over == 'jacket'", Null(),            
            "renpy.showing('Laura_TJ_Animation')", Null(),
            "renpy.showing('Laura_Sex_Animation')", Null(),     
            "LauraX.Hair == 'wet' or LauraX.Water", Null(),
            "LauraX.Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Mid.png",
            "True", Null(),
            ),           
#        (0,0), ConditionSwitch(
#            #Face Water
#            "not LauraX.Water", Null(),
#            "True", "images/LauraSprite/Laura_Sprite_Wet_Head.png",
#            ),  
        (0,0), ConditionSwitch(                                                                         
            #Hair over
            "not LauraX.Hair", Null(),
            "renpy.showing('Laura_TJ_Animation')", Null(),
            "renpy.showing('Laura_SexSprite')", "images/LauraSex/Laura_Sprite_Hair_Long_OverSex.png",
            "LauraX.Hair == 'wet' or LauraX.Water", "images/LauraSprite/Laura_Sprite_Hair_Wet_Over.png",
            "LauraX.Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Over.png",
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(
            #Hair Water
            "not LauraX.Water", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Head_Wet.png",
#            "True", "images/LauraSprite/Laura_Sprite_Hair_Wet.png",
            ),
        (0,0), ConditionSwitch(
            #facial spunk               
            "'hair' in LauraX.Spunk", "images/LauraSprite/Laura_Sprite_Spunk_Facial2.png",  
            "'facial' in LauraX.Spunk", "images/LauraSprite/Laura_Sprite_Spunk_Facial1.png",            
            "True", Null(),            
            ),  
        )                
    anchor (0.6, 0.0)                
    zoom .5                      

image Laura Blink:            
    ConditionSwitch(
    "LauraX.Eyes == 'sexy'", "images/LauraSprite/Laura_Sprite_Eyes_Squint.png",
    "LauraX.Eyes == 'side'", "images/LauraSprite/Laura_Sprite_Eyes_Side.png",
    "LauraX.Eyes == 'surprised'", "images/LauraSprite/Laura_Sprite_Eyes_Surprised.png",
    "LauraX.Eyes == 'normal'", "images/LauraSprite/Laura_Sprite_Eyes_Normal.png",    
    "LauraX.Eyes == 'stunned'", "images/LauraSprite/Laura_Sprite_Eyes_Stunned.png",
    "LauraX.Eyes == 'down'", "images/LauraSprite/Laura_Sprite_Eyes_Down.png",
    "LauraX.Eyes == 'closed'", "images/LauraSprite/Laura_Sprite_Eyes_Closed.png",
    "LauraX.Eyes == 'leftside'", "images/LauraSprite/Laura_Sprite_Eyes_Leftside.png",
    "LauraX.Eyes == 'manic'", "images/LauraSprite/Laura_Sprite_Eyes_Normal.png",
    "LauraX.Eyes == 'squint'", "Laura_Squint",
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
            "Player.Cock == 'in'", ConditionSwitch(                                                               
                    # If during sex
                    "Speed == 1", "Laura_Sex_Body_S1",#heading
                    "Speed == 2", "Laura_Sex_Body_S2",#slow
                    "Speed == 3", "Laura_Sex_Body_S3",#fast
                    "Speed >= 4", "Laura_Sex_Body_S4",#cumming
                    "True",       "Laura_Sex_Body_S0",#Static
                    ),
            "Player.Cock == 'anal'", ConditionSwitch(                                                              
#                    # If during Anal
                    "Speed == 1", "Laura_Sex_Body_A1",#heading
                    "Speed == 2", "Laura_Sex_Body_A2",#slow
                    "Speed == 3", "Laura_Sex_Body_A3",#fast
                    "Speed >= 4", "Laura_Sex_Body_A4",#cumming
                    "True",       "Laura_Sex_Body_A0",#Static
                    ),                    
            "Player.Cock == 'foot'", ConditionSwitch(                                      
                    # If during Footjob
                    "not Player.Sprite","Laura_Sex_Body_F0",#Static
                    "Speed == 1", "Laura_Sex_Body_F1",#heading
                    "Speed >= 4", "Laura_Sex_Body_F0",#cumming
                    "Speed >= 2", "Laura_Sex_Body_F2",#slow
                    "True",       "Laura_Sex_Body_F0",#Static
                    ),    
            
            "True", ConditionSwitch(                                                              
                    # If neither
                    "not Player.Sprite","Laura_Sex_Body_H0",#Static
                    "Speed == 1", "Laura_Sex_Body_H1",#slow
                    "Speed == 4", "Laura_Sex_Body_H0",#cumming
                    "Speed >= 2", "Laura_Sex_Body_H2",#fast
                    "True",       "Laura_Sex_Body_H0",#Static
                    ),
            )
    contains:
        ConditionSwitch(                                                               
            # Laura's lower body
            "Player.Cock == 'in'", ConditionSwitch(                                                               
                    # If during sex
                    "Speed == 1", "Laura_Sex_Legs_S1",#heading
                    "Speed == 2", "Laura_Sex_Legs_S2",#slow
                    "Speed == 3", "Laura_Sex_Legs_S3",#fast
                    "Speed >= 4", "Laura_Sex_Legs_S4",#cumming
                    "True", "Laura_Sex_Legs_S0",#Static
                    ),
            "Player.Cock == 'anal'", ConditionSwitch(                                                              
                    # If during Anal
                    "Speed == 1", "Laura_Sex_Legs_A1",#heading
                    "Speed == 2", "Laura_Sex_Legs_A2",#slow
                    "Speed == 3", "Laura_Sex_Legs_A3",#fast
                    "Speed >= 4", "Laura_Sex_Legs_A4",#cumming
                    "True", "Laura_Sex_Legs_A0",#Static
                    ),
            "Player.Cock == 'foot'", ConditionSwitch(                                      
                    # If during Footjob
                    "not Player.Sprite","Laura_Sex_Legs_F0",#Static
                    "Speed == 1", "Laura_Sex_Legs_F1",#heading
                    "Speed >= 4", "Laura_Sex_Legs_F0",#cumming
                    "Speed >= 2", "Laura_Sex_Legs_F2",#slow
                    "True",       "Laura_Sex_Legs_F0",#Static   
                    ),     
            "True", ConditionSwitch(                                                               
                    # If neither
                    "not Player.Sprite","Laura_Sex_Legs_H0",#Static
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
#            "images/LauraSex/Laura_Sex_Hand.png"
                    
            ConditionSwitch(
                    "Player.Cock == 'foot'", Null(), 
                    "True", "images/LauraSex/Laura_Sex_Hand.png"       
                    ) 
    contains:
            # Over under layer
        ConditionSwitch(   
            "not LauraX.Over", Null(), 
            "LauraX.Uptop", ConditionSwitch(   
                    #if uptop                       
                    "LauraX.Over == 'jacket'", "images/LauraSex/Laura_Sex_Jacket_Back_Up.png",
                    "True", Null(),
                    ),                
            "True", ConditionSwitch(
                    #if not uptop        
                    "LauraX.Over == 'jacket'", "images/LauraSex/Laura_Sex_Jacket_Back.png",
                    "True", Null(),
                    ),    
            )
    contains:
            # body
            "images/LauraSex/Laura_Sex_Body.png"
    contains:
            # piercings tits
        ConditionSwitch(   
            "not LauraX.Pierce", Null(),
            "LauraX.Pierce == 'barbell'", "images/LauraSex/Laura_Sex_Barbell_Tits.png", 
            "LauraX.Pierce == 'ring'", "images/LauraSex/Laura_Sex_Ring_Tits.png", 
            "True", Null(), 
            )
    contains:
            # Chest clothing layer
        ConditionSwitch(    
            "LauraX.Neck == 'leash choker'", "images/LauraSex/Laura_Sex_Leash.png", 
            "True", Null(),  
            )
    contains:
            # garters
        ConditionSwitch(    
            "LauraX.Hose == 'stockings and garterbelt' or LauraX.Hose == 'garterbelt'", "images/LauraSex/Laura_Sex_Garter.png", 
            "True", Null(),  
            )
    contains:
            # Chest clothing layer
        ConditionSwitch(    
            "not LauraX.Chest", Null(),              
            "LauraX.Uptop",ConditionSwitch(  
                    #if the top is up. . .
                    "not LauraX.Chest", Null(),  
                    "LauraX.Chest == 'leather bra'", "images/LauraSex/Laura_Sex_Bra_Leather_Up.png", 
                    "LauraX.Chest == 'wolvie top'", "images/LauraSex/Laura_Sex_Top_Wolvie_Up.png", 
                    "LauraX.Chest == 'corset'", "images/LauraSex/Laura_Sex_Corset_Up.png",   
                    "LauraX.Chest == 'lace corset'", "images/LauraSex/Laura_Sex_Corset_Lace_Up.png",   
                    "LauraX.Chest == 'bikini top'", "images/LauraSex/Laura_Sex_Top_Bikini_Up.png",  
#                    "LauraX.Chest == 'sports bra'", "images/LauraSex/Laura_Sex_Bra_Sports_Up.png",  
#                    "LauraX.Chest == 'lace bra'", "images/LauraSex/Laura_Sex_Bra_Lace_Up.png",  
                    "True", Null(),  
                    ),     
            # else. . .
            "LauraX.Chest == 'leather bra'", "images/LauraSex/Laura_Sex_Bra_Leather.png", 
            "LauraX.Chest == 'wolvie top'", "images/LauraSex/Laura_Sex_Top_Wolvie.png", 
            "LauraX.Chest == 'corset'", "images/LauraSex/Laura_Sex_Corset.png",   
            "LauraX.Chest == 'lace corset'", "images/LauraSex/Laura_Sex_Corset_Lace.png",   
            "LauraX.Chest == 'bikini top'", "images/LauraSex/Laura_Sex_Top_Bikini.png",  
#            "LauraX.Chest == 'sports bra'", "images/LauraSex/Laura_Sex_Bra_Sports.png",  
#            "LauraX.Chest == 'lace bra'", "images/LauraSex/Laura_Sex_Bra_Lace.png",  
            "True", Null(),  
            )
    contains:
            # piercings tits over clothes
        ConditionSwitch(   
            "not LauraX.Pierce or LauraX.Uptop", Null(),
            "LauraX.Pierce == 'barbell'", "images/LauraSex/Laura_Sex_Barbell_Tits_C.png", 
            "LauraX.Pierce == 'ring'", "images/LauraSex/Laura_Sex_Ring_Tits_C.png", 
            "True", Null(), 
            )
    contains:
            # Over clothing layer
        ConditionSwitch(   
            "not LauraX.Over", Null(), 
            "LauraX.Uptop", ConditionSwitch(   
                    #if uptop                       
                    "LauraX.Over == 'jacket'", "images/LauraSex/Laura_Sex_Jacket_Up.png",
#                    "LauraX.Over == 'towel'", "images/LauraSex/Laura_Sex_Towel_Up.png",
                    "True", Null(),
                    ),                
            "True", ConditionSwitch(
                    #if not uptop        
                    "LauraX.Over == 'jacket'", "images/LauraSex/Laura_Sex_Jacket.png",
#                    "LauraX.Over == 'towel'", "images/LauraSex/Laura_Sex_Towel.png",
                    "True", Null(),
                    ),    
            )
    contains:
            # spunk
        ConditionSwitch(    
            "'belly' in LauraX.Spunk", "images/LauraSex/Laura_Sex_Spunk_Belly.png", 
            "True", Null(),
            ) 
    contains:
            # spunk on tits
            ConditionSwitch(    
                "'tits' not in LauraX.Spunk", Null(),
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
            "LauraX.Legs == 'skirt'", "images/LauraSex/Laura_Sex_Skirt_Back.png",  
            "True", Null(),
            )
#    contains:
#            # spunk
#        ConditionSwitch(    
#            "'anal' in LauraX.Spunk or 'in' in LauraX.Spunk", "images/LauraSex/Laura_Spunk_Sex.png", 
#            "True", Null(),
#            )
    contains:
            # Legs base
        ConditionSwitch(    
            "Player.Cock == 'foot'", "images/LauraSex/Laura_Sex_Legs_Foot.png", 
            "True", "images/LauraSex/Laura_Sex_Legs_High.png", 
            )
    contains:
            # anus
        ConditionSwitch(    
            "Player.Cock == 'anal' and Speed > 1", "images/LauraSex/Laura_Sex_Anus_L.png", #and speed above heading?
            "Player.Cock == 'anal' and Speed > 0", "images/LauraSex/Laura_Sex_Anus_M.png", #and speed above heading?
            "'anal' in LauraX.Spunk", "images/LauraSex/Laura_Sex_Anus_M.png", # If it's full. . .
            "True", "images/LauraSex/Laura_Sex_Anus_S.png", 
            )  
    contains:
            # anal spunk
        ConditionSwitch(    
            "'anal' not in LauraX.Spunk", Null(),
            "Player.Cock == 'anal' and Speed > 1", "images/LauraSex/Laura_Sex_Spunk_Anal_U.png", #speed above heading?
            "True", "images/LauraSex/Laura_Sex_Spunk_Anal.png", 
            ) 
    contains:
            # pussy
        ConditionSwitch(    
            "Player.Cock == 'in' and Speed > 1", "images/LauraSex/Laura_Sex_Pussy_Open.png", #and speed above heading?
            "Player.Cock == 'in' and Speed > 0", "images/LauraSex/Laura_Sex_Pussy_Mid.png", #and speed heading?
            "True", "images/LauraSex/Laura_Sex_Pussy_Closed.png", 
            )  
    contains:
            # pussy wetness
        ConditionSwitch(    
            "not LauraX.Wet", Null(),
            "True", "images/LauraSex/Laura_Sex_Wet.png", 
            ) 
    contains:
            # pussy spunk
        ConditionSwitch(    
            "'in' not in LauraX.Spunk", Null(),
            "Player.Cock == 'in' and Speed > 1", "images/LauraSex/Laura_Sex_Spunk_Pussy_Open.png", #and speed above heading?
            "True", "images/LauraSex/Laura_Sex_Spunk_Pussy.png", 
            ) 
    contains:
            # pubes
        ConditionSwitch(    
            "not LauraX.Pubes", Null(),
            "Player.Cock == 'in' and Speed > 1", "images/LauraSex/Laura_Sex_Pubes_Open.png", #and speed above heading?
            "Player.Cock == 'in' and Speed > 0", "images/LauraSex/Laura_Sex_Pubes_Mid.png", #and speed heading?
            "True", "images/LauraSex/Laura_Sex_Pubes_Closed.png", 
            )  
    contains:
            # piercings
        ConditionSwitch(    
            "LauraX.Pierce == 'barbell' and Player.Cock == 'in' and Speed > 1", "images/LauraSex/Laura_Sex_Barbell_Pussy_O.png", #and speed above heading?
            "LauraX.Pierce == 'barbell'", "images/LauraSex/Laura_Sex_Barbell_Pussy.png", 
            "LauraX.Pierce == 'ring' and Player.Cock == 'in' and Speed > 1", "images/LauraSex/Laura_Sex_Ring_Pussy_O.png", #and speed above heading?
            "LauraX.Pierce == 'ring'", "images/LauraSex/Laura_Sex_Ring_Pussy.png",
            "True", Null(), 
            )       
    contains:
            # panties
        ConditionSwitch(    
            "LauraX.PantiesDown", Null(),
#            "LauraX.Panties == 'wolvie panties' and LauraX.Wet", "images/LauraSex/Laura_Sex_Panties_Sport_SW.png", 
            "LauraX.Panties == 'bikini bottoms'", "images/LauraSex/Laura_Sex_Panties_Bikini.png", 
            "LauraX.Panties == 'wolvie panties'", "images/LauraSex/Laura_Sex_Panties_Wolvie.png", 
            "LauraX.Panties == 'lace panties'", "images/LauraSex/Laura_Sex_Panties_Lace.png", 
            "LauraX.Panties", "images/LauraSex/Laura_Sex_Panties_Black.png", 
            "True", Null(),
            )         
    contains:
            # hose base layer
        ConditionSwitch(    
            "Player.Cock == 'foot' and (LauraX.Hose == 'stockings and garterbelt' or LauraX.Hose == 'stockings')", "images/LauraSex/Laura_Sex_Stockings_Base_Foot.png", 
            "LauraX.Hose == 'stockings and garterbelt' or LauraX.Hose == 'stockings'", "images/LauraSex/Laura_Sex_Stockings_Base_Up.png", 
            "True", Null(),
            )              
    contains:
            # legs
        ConditionSwitch(    
            "LauraX.Legs == 'skirt'", "images/LauraSex/Laura_Sex_Skirt.png", 
            "LauraX.Upskirt", Null(),
            "LauraX.Legs == 'leather pants' and Player.Cock == 'foot'", "images/LauraSex/Laura_Sex_Pants_Base_Foot.png", 
            "LauraX.Legs == 'leather pants'", "images/LauraSex/Laura_Sex_Pants_Base_Up.png", 
            "True", Null(),
            )
    contains:
            # piercings
        ConditionSwitch(    
#            "LauraX.Panties and LauraX.PantiesDown", Null(), #don't show if panties are down
#            "LauraX.Legs == 'skirt' or (LauraX.Legs and LauraX.Upskirt)", Null(), #don't show if pants are down
            "LauraX.Pierce == 'barbell'", "images/LauraSex/Laura_Sex_Barbell_Pussy_C.png", 
            "LauraX.Pierce == 'ring'", "images/LauraSex/Laura_Sex_Ring_Pussy_C.png",
            "True", Null(), 
            ) 
#    contains:
#            # Over
#        ConditionSwitch(    
#            "LauraX.Over == 'nighty'", "images/LauraSex/Laura_Sex_Nighty_Pussy.png", 
#            "True", Null(),
#            )
    contains:
            # Feet
        ConditionSwitch(    
            "Player.Cock == 'foot'", "Laura_Footjob_Foot", 
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
            "LauraX.Hose == 'stockings and garterbelt' or LauraX.Hose == 'stockings'", "images/LauraSex/Laura_Sex_Stockings_Up.png", 
            "True", "images/LauraSex/Laura_Sex_FootHigh.png" #base
            )              
    contains:
            # legs
        ConditionSwitch(    
            "LauraX.Upskirt", Null(),
            "LauraX.Legs == 'leather pants'", "images/LauraSex/Laura_Sex_Pants_Up.png", 
            "True", Null(),
            )     
        xoffset  -2 #this shouldn't be needed, but otherwise there's a gap between the knee and leg. 
    transform_anchor True
    zoom 1 
#    alpha 0.2
    pos (988,-553)#(988,-553)

#image Laura_Footjob_Foot:
#    #her movable foot in the footjob poses
#    contains:
#            # hose/base
#        ConditionSwitch(    
#            "LauraX.Hose == 'stockings and garterbelt' or LauraX.Hose == 'stockings'", "images/LauraSex/Laura_Sex_Stockings_Foot.png", 
#            "True", "images/LauraSex/Laura_Sex_Foot.png"
#            )              
#    contains:
#            # legs
#        ConditionSwitch(    
#            "LauraX.Upskirt", Null(),
#            "LauraX.Legs == 'leather pants'", "images/LauraSex/Laura_Sex_Pants_Foot.png", 
#            "True", Null(),
#            )      
#    transform_anchor True
#    zoom 1 

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
                "'in' not in LauraX.Spunk", Null(),
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
                "'in' not in LauraX.Spunk", Null(),
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
                "'in' not in LauraX.Spunk", Null(),
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
                "'anal' not in LauraX.Spunk", Null(),
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
                "'anal' not in LauraX.Spunk", Null(),
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
                "'anal' not in LauraX.Spunk", Null(),
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
            "Player.Sprite", "Zero_Doggy_Insert",# Zero's cock, changes color and properties
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
   
   

# Laura Footjob  Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Laura_Footjob_Foot:
    #her movable foot in the footjob poses
    contains:
            # hose/base
        ConditionSwitch(    
            "LauraX.Hose == 'stockings and garterbelt' or LauraX.Hose == 'stockings'", "images/LauraSex/Laura_Sex_Stockings_Foot.png", 
            "True", "images/LauraSex/Laura_Sex_Foot.png"
            )              
    contains:
            # legs
        ConditionSwitch(    
            "LauraX.Upskirt", Null(),
            "LauraX.Legs == 'leather pants'", "images/LauraSex/Laura_Sex_Pants_Foot.png", 
            "True", Null(),
            )      
    offset (1105,140) #
    zoom 1 
    
image Laura_Sex_Zero_Anim_F:
            #cock used in laura's sex pose
            "Zero_Blowcock"
            zoom .7
            anchor (0.5, 0.9)
            offset (270,650)#(220,350)
            rotate 0
            
# Start F1 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
   
image Laura_Sex_Body_F0:                                                                        
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
    yoffset -100
            
image Laura_Sex_Legs_F0:
    # Her Legs in the hotdogging pose, static
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 3s
                pause 0.6
                easeout 0.8 ypos -2 #-50
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat         
    contains:
            #Foot
            "Laura_Footjob_Foot"
            subpixel True  
            anchor (1100,140)
            transform_anchor True       
            pos (0,0) #top 
            rotate 0
            parallel:#total 3s
                pause 0.6
                easeout 0.8 ypos -2 #-2
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-4
                easein 0.9 ypos 0 #out
                repeat  
            parallel:#total 3s
                ease 2 rotate 5 #20  
                ease 2 rotate -5 #0   
                pause .5
                repeat    
    contains:
            "Laura_Sex_Zero_Anim_F"
            subpixel True
            transform_anchor True  
            pos (558,580) #538,475
            rotate -5
            parallel:#total 3s
                pause 0.6
                easeout 0.8 ypos 578 #578
                easein 0.2 ypos 575 #out 575 
                easeout 0.5 ypos 576 #575
                easein 0.9 ypos 580 #out  580                
                repeat
            parallel:#total 3s
                easeout 1 rotate -5 #-20  
                easein 1 rotate -10 #-28  
                pause .2
                easeout .8 rotate -5 #-20   
                easein 1 rotate 0 #-5  
                pause .5
                repeat   
    
    yoffset -100
    # End Legs hotdogging static
                    
            
# End F0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


# Start F1 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
   
image Laura_Sex_Body_F1:                                                                        
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
    yoffset -100
            
image Laura_Sex_Legs_F1:
    # Her Legs in the hotdogging pose, static
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 3s
                pause 0.6
                easeout 0.8 ypos -2 #-50
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat            
    contains:
            "Laura_Sex_Zero_Anim_F"
            subpixel True
            transform_anchor True  
            pos (558,580) #538,475
            rotate -5
            parallel:#total 3s
                pause 0.6
                easeout 0.8 ypos 578 #455
                easein 0.2 ypos 575 #out  
                easeout 0.5 ypos 576 #455
                easein 0.9 ypos 580 #out                  
                repeat
            parallel:#total 3s
                easeout 1 rotate -20 #-50  
                easein 1 rotate -28 #-50  
                pause .2
                easeout .8 rotate -20 #-50   
                easein 1 rotate -5 #-50  
                pause .5
                repeat  
    contains:
            #Foot
            "Laura_Footjob_Foot"
            subpixel True  
            anchor (1100,140)
            transform_anchor True       
            pos (0,0) #top 
            rotate 0
            parallel:#total 3s
                pause 0.6
                easeout 0.8 ypos -2 #-50
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat  
            parallel:#total 3s
                ease 2 rotate 20 #-50  
                ease 2 rotate 0 #-50   
                pause .5
                repeat  
    
    yoffset -100
    # End Legs hotdogging static
                              
# End F1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


# Start F2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
   
image Laura_Sex_Body_F2:                                                                        
    #Her Body in the hotdogging pose, fast
    contains:
        "Laura_Sex_Body"      
        subpixel True       
        pos (0,0) #top (0,-10)
        block:#total 2s
            ease .7 ypos -10 #in
            ease .7 ypos 0 #out
            repeat
    rotate 15
    yoffset -250
    xoffset 500#400
    xzoom -1
                
image Laura_Sex_Legs_F2:
    # Her Legs in the hotdogging pose, fast
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 3
                ease 0.5 ypos -2 #-50
                ease 1 ypos -10 #-50
                pause .1
                repeat                      
    contains:
            "Laura_Sex_Zero_Anim_F"
            subpixel True
            transform_anchor True  
            pos (808,380) #(558,580)
            rotate -55
            parallel:#total 3s
                easeout .25 rotate -58 #-20  
                easein .25 rotate -60 #-28  
                pause .1
                easeout .4 rotate -58 #-20   
                easein .5 rotate -55 #-5  
                pause .1#.25
                repeat  
    contains:
            #Foot
            "Laura_Footjob_Foot"
            subpixel True  
            anchor (1100,140)
            transform_anchor True       
            pos (0,0) #top 
            rotate 0
            parallel:#total 3s
                pause 0.15
                easeout 0.2 ypos -2 #-50
                easein 0.05 ypos -5 #out
                easeout 0.25 ypos -4 #-50
                easein 0.45 ypos 0 #out
                repeat  
            parallel:#total 3s
                ease .5 rotate 20 #-50  top
                ease 1 rotate 0 #-50   
                pause .1#.25
                repeat  
    
    yoffset -400
    xoffset 300#200
    rotate 50
    # End Legs hotdogging fast
                               
            
# End F2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
                    
#End Footjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#End Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Laura_SexMaskX:                    
    transform_anchor True
    contains:
        "images/LauraSex/Laura_Sex_MaskPussyX.png"
        pos (200,303)#(0,0)#(-300,-300) #
        anchor (.5,.5)
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
        if renpy.showing("Laura_SexSprite"):
            return 
        $ Player.Sprite = 1
        hide Laura_Sprite      
        if renpy.showing("Laura_BJ_Animation"):
            hide Laura_BJ_Animation
        if renpy.showing("Laura_HJ_Animation"):
            hide Laura_HJ_Animation
        if renpy.showing("Laura_TJ_Animation"):
            hide Laura_TJ_Animation
        call Speed_Shift(0) 
        
        if Trigger == "in" or Trigger == "anal": 
                if LauraX.Legs or LauraX.HoseNum() >= 5:      
                    $ LauraX.Upskirt = 1
                if LauraX.Panties:     
                    $ LauraX.PantiesDown = 1
                            
        show Laura_SexSprite zorder 150:
            pos (450,500)
        with dissolve
        return
    
label Laura_Sex_Reset:
        if not renpy.showing("Laura_SexSprite"):
            return
        $ LauraX.ArmPose = 2     
        hide Laura_SexSprite  
        call Laura_Hide 
        show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
            alpha 1
            zoom 1 offset (0,0) 
            anchor (0.5, 0.0)
        with dissolve
        $ Speed = 0
        return
label Laura_Doggy_Reset:
        return


# Laura's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
            
            
            
            
# Laura's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
                                                 

              
image Laura_BJ_Animation:                
    #core blowjob animation   
    contains:
        ConditionSwitch(
            # Laura's upper body
#            "Player.Sprite", ConditionSwitch(                                                               
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
            "not LauraX.Hair", Null(),
            "LauraX.Hair == 'wet' or LauraX.Water", "images/LauraSprite/Laura_Sprite_Hair_Wet_Under.png",
            "LauraX.Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Under.png",
            "True", Null(),
            )        
                    
image Laura_Sprite_BJ_Head:
    #This is the version of the head used in the BJ pose
    LiveComposite(
        (806,806),         
        (0,0), ConditionSwitch(
                # Face background plate
                "LauraX.Blush == 2", "images/LauraSprite/Laura_Sprite_Head_Blush2.png", 
                "LauraX.Blush", "images/LauraSprite/Laura_Sprite_Head_Blush.png",  
                "True", "images/LauraSprite/Laura_Sprite_Head.png",                        
                ),        
        (0,0), ConditionSwitch(#chin spunk
            "'chin' not in LauraX.Spunk", Null(),
            "Speed >= 2", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Spunk_Chin.png",
            ),    
        (0,0), ConditionSwitch(#Mouths 
            "Speed >= 2", "images/LauraSprite/Laura_Sprite_Mouth_SuckingBJ.png",   #sucking       
            "Speed == 1", "images/LauraSprite/Laura_Sprite_Mouth_Tongue.png",     #licking 
            "LauraX.Mouth == 'normal'", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png",
            "LauraX.Mouth == 'lipbite'", "images/LauraSprite/Laura_Sprite_Mouth_Lipbite.png",
            "LauraX.Mouth == 'sucking'", "images/LauraSprite/Laura_Sprite_Mouth_Sucking.png",            
            "LauraX.Mouth == 'kiss'", "images/LauraSprite/Laura_Sprite_Mouth_Kiss.png",
            "LauraX.Mouth == 'sad'", "images/LauraSprite/Laura_Sprite_Mouth_Sad.png",
            "LauraX.Mouth == 'smile'", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png",
            "LauraX.Mouth == 'surprised'", "images/LauraSprite/Laura_Sprite_Mouth_Surprised.png",            
            "LauraX.Mouth == 'tongue'", "images/LauraSprite/Laura_Sprite_Mouth_Tongue.png",                
            "LauraX.Mouth == 'grimace'", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png",              
            "LauraX.Mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Mouth_Smirk.png",                    
#            "LauraX.Mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png",         
            "True", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png",
            ),         
        (0,0), ConditionSwitch(#Mouth spunk 
            "'mouth' not in LauraX.Spunk", Null(),
            "Speed >= 2", "images/LauraSprite/Laura_Sprite_Spunk_MouthSuck.png",   #sucking       
            "Speed == 1", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",     #licking             
            "LauraX.Mouth == 'normal'", "images/LauraSprite/Laura_Sprite_Spunk_MouthNeutral.png",
            "LauraX.Mouth == 'lipbite'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmirk.png",
            "LauraX.Mouth == 'sucking'", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",            
            "LauraX.Mouth == 'kiss'", "images/LauraSprite/Laura_Sprite_Spunk_MouthKiss.png",
            "LauraX.Mouth == 'sad'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSad.png",
            "LauraX.Mouth == 'smile'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmile.png",
            "LauraX.Mouth == 'surprised'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSad.png",            
            "LauraX.Mouth == 'tongue'", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",                
            "LauraX.Mouth == 'grimace'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmile.png",              
            "LauraX.Mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmirk.png",      
            "True", "images/LauraSprite/Laura_Sprite_Spunk_MouthNeutral.png",
            ),     
        (0,0), ConditionSwitch(#Mouth spunk over 
            "Speed >= 2 and 'mouth' in LauraX.Spunk", "images/LauraSprite/Laura_Sprite_SpunkSuckingO.png",   #sucking  
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(#wet tongue
            "Speed == 1", "images/LauraSprite/Laura_Sprite_Wet_Tongue.png",     #licking   
            "True", Null(),
            ),                                                              
        (0,0), ConditionSwitch(                                                                       
            #brows
            "LauraX.Blush >= 2", ConditionSwitch(
                    "LauraX.Brows == 'normal'", "images/LauraSprite/Laura_Sprite_Brows_Normal_B.png",
                    "LauraX.Brows == 'angry'", "images/LauraSprite/Laura_Sprite_Brows_Angry_B.png",
                    "LauraX.Brows == 'sad'", "images/LauraSprite/Laura_Sprite_Brows_Sad_B.png",
                    "LauraX.Brows == 'surprised'", "images/LauraSprite/Laura_Sprite_Brows_Surprised_B.png",        
                    "LauraX.Brows == 'confused'", "images/LauraSprite/Laura_Sprite_Brows_Confused_B.png",
                    "True", "images/LauraSprite/Laura_Sprite_Brows_Normal_B.png",
                    ),
            "True", ConditionSwitch(
                    "LauraX.Brows == 'normal'", "images/LauraSprite/Laura_Sprite_Brows_Normal.png",
                    "LauraX.Brows == 'angry'", "images/LauraSprite/Laura_Sprite_Brows_Angry.png",
                    "LauraX.Brows == 'sad'", "images/LauraSprite/Laura_Sprite_Brows_Sad.png",
                    "LauraX.Brows == 'surprised'", "images/LauraSprite/Laura_Sprite_Brows_Surprised.png",        
                    "LauraX.Brows == 'confused'", "images/LauraSprite/Laura_Sprite_Brows_Confused.png",
                    "True", "images/LauraSprite/Laura_Sprite_Brows_Normal.png",
                    ),
            ),        
        (0,0), "Laura Blink",     #Eyes    
        (0,0), ConditionSwitch(                
            #Hair mid
            "LauraX.Over == 'jacket'", Null(),
            "LauraX.Hair == 'wet' or LauraX.Water", Null(),
            "LauraX.Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Mid.png",
            "True", Null(),
            ),       
#        (0,0), ConditionSwitch(
#            #Face Water
#            "not LauraX.Water", Null(),
#            "True", "images/LauraSprite/Laura_Sprite_Wet_Head.png",
#            ),
        (0,0), ConditionSwitch(                                                                         
            #Hair over
            "not LauraX.Hair", Null(),
            "LauraX.Hair == 'wet' or LauraX.Water", "images/LauraSprite/Laura_Sprite_Hair_Wet_Over.png",
            "LauraX.Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Over.png",
            "True", Null(),
            ),        
        (0,0), ConditionSwitch(
            #Hair Water
            "not LauraX.Water", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Head_Wet.png",
#            "True", "images/LauraSprite/Laura_Sprite_Hair_Wet.png",
            ),
        (0,0), ConditionSwitch(
            #facial spunk               
            "'hair' in LauraX.Spunk", "images/LauraSprite/Laura_Sprite_Spunk_Facial2.png",  
            "'facial' in LauraX.Spunk", "images/LauraSprite/Laura_Sprite_Spunk_Facial1.png",            
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
#                "Player.Sprite", "Blowcock",
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
#                "Player.Sprite", "Blowcock",
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
#                "Player.Sprite", "Blowcock",
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
#                "Player.Sprite", "Blowcock",
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
#                "Player.Sprite", "Blowcock",
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
#                "Player.Sprite", "Blowcock",
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
#                "Player.Sprite", "Blowcock",
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

label Laura_BJ_Launch(Line = 0):    
    # The sequence to launch the Laura BJ animations 
    $ LauraX.ArmPose = 1
    if renpy.showing("Laura_BJ_Animation"):
        return
    
    call Laura_Hide
    if Line == "L" or Line == "cum":
        show Laura_Sprite at SpriteLoc(StageCenter) zorder LauraX.Layer:
            alpha 1
            ease 1 zoom 2.5 offset (150,80) 
        with dissolve
    else:
        show Laura_Sprite at SpriteLoc(StageCenter) zorder LauraX.Layer:
            alpha 1
            zoom 2.5 offset (150,80) 
        with dissolve
        
    $ Speed = 0
    if Line == "L": # Laura gets started. . .
            if Taboo: 
                if len(Present) >= 2:
                    if Present[0] != LauraX:
                            "[LauraX.Name] looks back at [Present[0].Name] to see if she's watching."
                    elif Present[1] != LauraX:
                            "[LauraX.Name] looks back at [Present[1].Name] to see if she's watching."
                else:
                            "[LauraX.Name] casually glances around to see if anyone can see her."
            "[LauraX.Name] smoothly bends down and places your cock against her cheek."   
            
    if Line != "cum":
        $ Trigger = "blow"
    
    show Laura_Sprite zorder LauraX.Layer:
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
    
    show Laura_Sprite at SpriteLoc(StageCenter) zorder LauraX.Layer:
        alpha 1
        zoom 2.5 offset (150,80) 
    with dissolve
    
    show Laura_Sprite zorder LauraX.Layer:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)      
    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
        alpha 1
        zoom 1 offset (0,0)    
    return  

# End Laura Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Laura Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Laura Handjob element //////////////////////////////////////////////////////////////////////   

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
        ConditionSwitch(                                                
            # backside of the hand
            "not Speed", Transform("Laura_Hand_Under"), 
            "Speed == 1", At("Laura_Hand_Under", Laura_Hand_1()),
            "Speed >= 2", At("Laura_Hand_Under", Laura_Hand_2()),            
            "Speed", Null(),
            ),  
    contains:
        ConditionSwitch(                                                
            # cock
            "not Speed", Transform("Zero_Handcock"), 
            "Speed == 1", At("Zero_Handcock", Handcock_1L()),
            "Speed >= 2", At("Zero_Handcock", Handcock_2L()), 
            "Speed", Null(),
            ),  
        offset (0,0)
    contains:
        ConditionSwitch(                                               
            # fingers of the hand
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
        show Laura_Sprite at SpriteLoc(StageRight) zorder LauraX.Layer:
            alpha 1
            ease 1 zoom 1.7 offset (-150,200)#(0,200)
    else:     
        show Laura_Sprite at SpriteLoc(StageRight) zorder LauraX.Layer:
            alpha 1
            ease 1 zoom 1.7 offset (-150,200)#(0,200)
        with dissolve
            
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    else:
        $ Speed = 1
    pause .5
    $ LauraX.ArmPose = 1
    show Laura_HJ_Animation at SpriteLoc(StageCenter) zorder 150 with easeinbottom:
        #xoffset 150
        offset (250,250)#(100,250)
    return
    
label Laura_HJ_Reset: # The sequence to the Laura animations from handjob to default
    if not renpy.showing("Laura_HJ_Animation"):
        return    
    $ Speed = 0            
    $ LauraX.ArmPose = 1
    hide Laura_HJ_Animation with easeoutbottom
    call Laura_Hide 
    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
        alpha 1
        zoom 1.7 offset (-50,200)
    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause .5
        ease .5 zoom 1 offset (0,0) 
    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
        alpha 1
        zoom 1 offset (0,0)     
    return
    
# End Laura Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    




# Laura's TJ animations start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Animation components / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# start base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Laura_TJ_Animation:
            #core TJ animation   
            contains:
                ConditionSwitch(                                                              
                    # Laura's upper body     
                    "not Player.Sprite","Laura_TJ_0",#Static
                    "Speed == 1", "Laura_TJ_1",#slow
                    "Speed == 4", "Laura_TJ_4",#cumming high
                    "Speed == 5", "Laura_TJ_5",#cumming low
                    "Speed >= 2", "Laura_TJ_2",#fast
                    "True",       "Laura_TJ_0",#Static
                    )
            zoom .7 #0.6
            transform_anchor True
            anchor (.5,.5)
# end base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
            
            
    
image Laura_TJ_HairBack:
            #Hair underlay
            "Laura_Sprite_HairBack"
            transform_anchor True
            zoom 2.5
            anchor (0.5, 0.5)
            offset (320,100)
            rotate 0
  
image Laura_TJ_Head:
            #Hair underlay
            "Laura_Sprite_Head"
            transform_anchor True
            zoom 2.5
            anchor (0.5, 0.5)
            offset (320,100)
            rotate 0
    
image Laura_TJ_HairMid:
            #Hair midlayer
            "Laura_Sprite_HairMid"
            transform_anchor True
            zoom 2.5
            anchor (0.5, 0.5)
            rotate 20
            offset (320,100)
            rotate 0

image Laura_TJ_HairTop:
            #Hair overlay
            "Laura_Sprite_HairTop"
            transform_anchor True
            zoom 2.5 #2.1
            anchor (0.5, 0.5)
            offset (320,100) # (300,275)
            rotate 0

image Laura_TJ_ZeroCock:
            #cock used in laura's sex pose
            "Zero_Blowcock"
            transform_anchor True
            zoom .7
            anchor (0.5, 0.5)
            offset (220,670)#(300,750)
            rotate 0

image Laura_TJ_Body:
            #body underlay
            contains:
                "images/LauraSex/Laura_Titjob_Body.png"  
            contains:               
                ConditionSwitch(
                        "not LauraX.Neck",Null(),                                
                        "True",       "images/LauraSex/Laura_Titjob_Neck_[LauraX.Neck].png",
                        )      
            contains:               
                ConditionSwitch(
                        "'tits' not in LauraX.Spunk",Null(),                                
                        "True",       "images/LauraSex/Laura_Titjob_Spunk_Chest.png",
                        )                 
            transform_anchor True
            zoom 1
            anchor (0.4, 1.0)
            offset (410,770) # (300,275)
            rotate 0
    
  
image Laura_TJ_LeftArm:
            #left arm
            contains:
                "images/LauraSex/Laura_Titjob_LeftHand.png" 
            contains:               
                ConditionSwitch(
                        "not LauraX.Arms",Null(),                                
                        "True",       "images/LauraSex/Laura_Titjob_[LauraX.Arms].png",
                        )   
            contains:
                # Left Piercings
                ConditionSwitch(
                        "not LauraX.Pierce",Null(),        
                        "True",       "images/LauraSex/Laura_Titjob_Left_[LauraX.Pierce].png",
                        )    
    
# Animations start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start 0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Laura_TJ_0:                                                                        
        #Her Body in the TJ pose, static
        contains:
                #hairback
                "Laura_TJ_HairBack"   
                subpixel True       
                pos (0,0) #top (0,-10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat  
                parallel:
                    pause .1
                    ease 2 rotate -5
                    pause .1
                    ease 2 rotate 0
                    repeat  
        contains:
                #base body test
                "Laura_TJ_Body"  
                subpixel True       
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat 
        contains:
                #right hand backside
                "images/LauraSex/Laura_Titjob_RightHandBack.png"      
                subpixel True       
                pos (0,-15) #top (0,-10)    
                transform_anchor True 
                parallel:
                    ease 2 ypos -5
                    pause .1
                    ease 2 ypos -15
                    pause .1
                    repeat 
        contains:
                contains:
                    "images/LauraSex/Laura_Titjob_RightTit.png"            
                contains:
                    ConditionSwitch(
                            "'tits' not in LauraX.Spunk",Null(),                                
                            "True",       "images/LauraSex/Laura_Titjob_Spunk_Right.png",
                            )      
                subpixel True       
                pos (0,-15) #top (0,-10)
                transform_anchor True 
                parallel:
                    pause .1
                    ease 2 ypos -5
                    pause .1
                    ease 2 ypos -15
                    repeat 
        contains:
                #right hand
                contains:
                    "images/LauraSex/Laura_Titjob_RightHand.png"    
                contains:
                    # Right Piercings                    
                    ConditionSwitch(
                            "not LauraX.Pierce",Null(),                                
                            "True",       "images/LauraSex/Laura_Titjob_Right_[LauraX.Pierce].png",
                            )                           
                subpixel True     
                pos (0,-15) #top (0,-10)  
                transform_anchor True 
                parallel:
                    ease 2 ypos -5
                    pause .1
                    ease 2 ypos -15
                    pause .1
                    repeat 
        contains:
                #head
                "Laura_TJ_Head"   
                subpixel True       
                pos (0,0) #top (0,-10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat  
                parallel:
                    pause .1
                    ease 2 rotate -5
                    pause .1
                    ease 2 rotate 0
                    repeat  
        contains:
                #zero cock
                subpixel True
                "Laura_TJ_ZeroCock"
                pos (0,30) #top (0,-10)
                transform_anchor True
                rotate -2
                parallel:
                    ease 2 rotate -2
                    pause .1
                    ease 2 rotate 3
                    pause .1
                    repeat      
        contains:
                #left tit
                contains:
                    "images/LauraSex/Laura_Titjob_LeftTit.png"    
                contains:
                    ConditionSwitch(
                            "'tits' not in LauraX.Spunk",Null(),                                
                            "True",       "images/LauraSex/Laura_Titjob_Spunk_Left.png",
                            )                            
                subpixel True       
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    pause .1
                    ease 2 ypos -40
                    pause .1
                    ease 2 ypos 0
                    repeat 
        contains:
                #left hand
                "Laura_TJ_LeftArm"
#                contains:
#                    "images/LauraSex/Laura_Titjob_LeftHand.png"    
#                contains:
#                    # Left Piercings
#                    ConditionSwitch(
#                            "not LauraX.Pierce",Null(),        
#                            "True",       "images/LauraSex/Laura_Titjob_Left_[LauraX.Pierce].png",
#                            )  
                subpixel True       
                pos (0,0) #top (0,-10)   
                transform_anchor True
                parallel:
                    ease 2 ypos -40
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat 
        contains:
                #mid hair
                "Laura_TJ_HairMid"   
                subpixel True       
                pos (0,0) #top (0,+10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat  
                parallel:
                    pause .1
                    ease 2 rotate -5
                    pause .1
                    ease 2 rotate 0
                    repeat   
        contains:
                #head
                "Laura_TJ_HairTop"   
                subpixel True       
                pos (0,0) #top (0,-10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat    
                parallel:
                    pause .1
                    ease 2 rotate -5
                    pause .1
                    ease 2 rotate 0
                    repeat  
# End Laura TJ Pose 0 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start 1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Laura_TJ_1:                                                                        
        #Her Body in the TJ pose, slow
        contains:
                #hairback
                "Laura_TJ_HairBack"   
                subpixel True       
                pos (0,150) #top (0,-10)
                transform_anchor True
                rotate -5
                parallel:
                    ease 2 ypos 0
                    pause .2
                    ease 2 ypos 150
                    pause .5
                    repeat    
                parallel:
                    ease 2 rotate 0
                    pause .2
                    ease 2 rotate -5
                    pause .5
                    repeat  
        contains:
                #base body
                "Laura_TJ_Body"      
                subpixel True       
                pos (0,150) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos 0
                    pause .2
                    ease 2 ypos 150
                    pause .5
                    repeat  
        contains:
                #right hand backside
                "images/LauraSex/Laura_Titjob_RightHandBack.png"      
                subpixel True       
                pos (0,150) #top (0,-10)    
                transform_anchor True  
                block:
                    ease 2 ypos -20
                    pause .4
                    ease 1.8 ypos 150
                    pause .5
                    repeat  
        contains:
                contains:
                    "images/LauraSex/Laura_Titjob_RightTit.png"            
                contains:
                    ConditionSwitch(
                            "'tits' not in LauraX.Spunk",Null(),                                
                            "True",       "images/LauraSex/Laura_Titjob_Spunk_Right.png",
                            )        
                subpixel True       
                pos (0,150) #top (0,-10)
                transform_anchor True
                block:
                    pause .1
                    ease 1.9 ypos -20
                    pause .4
                    ease 1.8 ypos 150
                    ease .5 ypos 140   
                    repeat
        contains:
                #right hand
                contains:
                    "images/LauraSex/Laura_Titjob_RightHand.png"    
                contains:
                    # Right Piercings                    
                    ConditionSwitch(
                            "not LauraX.Pierce",Null(),                                
                            "True",       "images/LauraSex/Laura_Titjob_Right_[LauraX.Pierce].png",
                            )                           
                subpixel True     
                pos (0,150) #top (0,-10)  
                transform_anchor True 
                block:
                    ease 2 ypos -20                    
                    pause .4
                    ease 1.8 ypos 150
                    pause .5
                    repeat  
        contains:
                #head
                "Laura_TJ_Head"   
                subpixel True       
                pos (0,150) #top (0,-10)
                transform_anchor True
                rotate -5
                parallel:
                    ease 2 ypos 0
                    pause .2
                    ease 2 ypos 150
                    pause .5
                    repeat    
                parallel:
                    ease 2 rotate 0
                    pause .2
                    ease 2 rotate -5
                    pause .5
                    repeat  
        contains:
                #zero cock
                subpixel True
                "Laura_TJ_ZeroCock"
                pos (0,25) #top (0,-10)
                transform_anchor True
                rotate -5
                parallel:                  
                    ease 2 ypos 0
                    pause .4
                    ease 1.8 ypos 25
                    pause .5
                    repeat     
                parallel:
                    ease 2 rotate 0
                    pause .2
                    ease 2 rotate -5
                    pause .5
                    repeat      
        contains:
                #left tit
                contains:
                    "images/LauraSex/Laura_Titjob_LeftTit.png"      
                contains:
                    ConditionSwitch(
                            "'tits' not in LauraX.Spunk",Null(),                                
                            "True",       "images/LauraSex/Laura_Titjob_Spunk_Left.png",
                            )                           
                subpixel True       
                pos (0,150) #top (0,-10)
                transform_anchor True
                block:
                    pause .1
                    ease 1.9 ypos -20
                    pause .4
                    ease 1.8 ypos 150
                    ease .5 ypos 140    
                    repeat
        contains:
                #left hand
                "Laura_TJ_LeftArm"
                subpixel True       
                pos (0,150) #top (0,-10)   
                transform_anchor True
                block:
                    ease 2 ypos -20
                    pause .4
                    ease 1.8 ypos 150
                    pause .5
                    repeat  
        contains:
                #mid hair
                "Laura_TJ_HairMid"   
                subpixel True       
                pos (0,160) #top (0,150)
                transform_anchor True
                rotate -5
                parallel:
                    ease 2 ypos -20#-20
                    pause .4
                    ease 1.8 ypos 160
                    pause .5
                    repeat   
                parallel:
                    ease 2 rotate 0
                    pause .2
                    ease 2 rotate -5
                    pause .5
                    repeat  
        contains:
                #head
                "Laura_TJ_HairTop"   
                subpixel True       
                pos (0,150) #top (0,-10)
                transform_anchor True
                rotate -5
                parallel:
                    ease 2 ypos 0
                    pause .2
                    ease 2 ypos 150
                    pause .5
                    repeat    
                parallel:
                    ease 2 rotate 0
                    pause .2
                    ease 2 rotate -5
                    pause .5
                    repeat  
# End Laura TJ Pose 1 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
             
 
# Start 2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Laura_TJ_2:                                                                        
        #Her Body in the TJ pose, fast
        contains:
                #hairback
                "Laura_TJ_HairBack"   
                subpixel True       
                pos (0,80) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 1 ypos -20
                    pause .1
                    ease .5 ypos 80
                    repeat    
                parallel:
                    ease 1 rotate 0
                    pause .1
                    ease .5 rotate -5
                    repeat  
        contains:
                #base body
                "Laura_TJ_Body"      
                subpixel True       
                pos (0,80) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 1 ypos -20
                    pause .1
                    ease .5 ypos 80
                    repeat   
        contains:
                #right hand backside
                "images/LauraSex/Laura_Titjob_RightHandBack.png"      
                subpixel True       
                pos (0,80) #top (0,-10)    
                transform_anchor True  
                block:
                    ease 1 ypos -40
                    pause .2
                    ease .4 ypos 80
                    repeat  
        contains:
                contains:
                    "images/LauraSex/Laura_Titjob_RightTit.png"            
                contains:
                    ConditionSwitch(
                            "'tits' not in LauraX.Spunk",Null(),                                
                            "True",       "images/LauraSex/Laura_Titjob_Spunk_Right.png",
                            )      
                subpixel True       
                pos (0,80) #top (0,-10)
                transform_anchor True                
                block:
                    ease .3 ypos 40  
                    ease .7 ypos -40
                    pause .2
                    ease .4 ypos 80
                    repeat
        contains:
                #right hand
                contains:
                    "images/LauraSex/Laura_Titjob_RightHand.png"    
                contains:
                    # Right Piercings                    
                    ConditionSwitch(
                            "not LauraX.Pierce",Null(),                                
                            "True",       "images/LauraSex/Laura_Titjob_Right_[LauraX.Pierce].png",
                            )                           
                subpixel True     
                pos (0,80) #top (0,-10)  
                transform_anchor True 
                block:
                    ease 1 ypos -40
                    pause .2
                    ease .4 ypos 80
                    repeat  
        contains:
                #head
                "Laura_TJ_Head"   
                subpixel True       
                pos (0,80) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 1 ypos -20
                    pause .1
                    ease .5 ypos 80
                    repeat    
                parallel:
                    ease 1 rotate 0
                    pause .1
                    ease .5 rotate -5
                    repeat  
        contains:
                #zero cock
                subpixel True
                "Laura_TJ_ZeroCock"
                pos (0,30) #top (0,-10)
                transform_anchor True
                rotate -2
                parallel:                  
                    ease 1 ypos 0
                    pause .2
                    ease .4 ypos 30
                    repeat     
                parallel:
                    ease 1 rotate 0
                    pause .1
                    ease .5 rotate -2
                    repeat      
        contains:
                #left tit
                contains:
                    "images/LauraSex/Laura_Titjob_LeftTit.png"        
                contains:
                    ConditionSwitch(
                            "'tits' not in LauraX.Spunk",Null(),                                
                            "True",       "images/LauraSex/Laura_Titjob_Spunk_Left.png",
                            )                         
                subpixel True       
                pos (0,80) #top (0,-10)
                transform_anchor True
                block:
                    ease .3 ypos 40  
                    ease .7 ypos -40
                    pause .2
                    ease .4 ypos 80   
                    repeat
        contains:
                #left hand
                "Laura_TJ_LeftArm"
                subpixel True       
                pos (0,80) #top (0,-10)   
                transform_anchor True
                block:
                    ease 1 ypos -40
                    pause .2
                    ease .4 ypos 80
                    repeat  
        contains:
                #mid hair
                "Laura_TJ_HairMid"   
                subpixel True       
                pos (0,90) #top (0,+10)
                transform_anchor True
                rotate -5
                parallel:
                    ease 1 ypos -40#-20
                    pause .2
                    ease .4 ypos 90
                    repeat   
                parallel:
                    ease 1 rotate 0
                    pause .2
                    ease .4 rotate -5
                    repeat  
        contains:
                #head
                "Laura_TJ_HairTop"   
                subpixel True       
                pos (0,80) #top (0,-10)
                transform_anchor True
                rotate -5
                parallel:
                    ease 1 ypos -20
                    pause .1
                    ease .5 ypos 80
                    repeat    
                parallel:
                    ease 1 rotate 0
                    pause .1
                    ease .5 rotate -5
                    repeat  
# End Laura TJ Pose 2 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
                   
                   
# Start 4 (cumming high) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Laura_TJ_4:                                                                        
        #Her Body in the TJ pose, cumming
        contains:
                #hairback
                "Laura_TJ_HairBack"   
                subpixel True       
                pos (0,0) #top (0,-10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat  
                parallel:
                    pause .1
                    ease 2 rotate -5
                    pause .1
                    ease 2 rotate 0
                    repeat  
        contains:
                #base body
                "Laura_TJ_Body"      
                subpixel True       
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat 
        contains:
                #right hand backside
                "images/LauraSex/Laura_Titjob_RightHandBack.png"      
                subpixel True       
                pos (0,0) #top (0,-10)    
                transform_anchor True 
                parallel:
                    ease 2 ypos -30
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat  
        contains:
                contains:
                    "images/LauraSex/Laura_Titjob_RightTit.png"            
                contains:
                    ConditionSwitch(
                            "'tits' not in LauraX.Spunk",Null(),                                
                            "True",       "images/LauraSex/Laura_Titjob_Spunk_Right.png",
                            )        
                subpixel True       
                pos (0,5) #top (0,-10)
                transform_anchor True 
                parallel:
                    pause .2
                    ease 1.9 ypos -30
                    pause .2
                    ease 1.9 ypos 5
                    repeat  
        contains:
                #right hand
                contains:
                    "images/LauraSex/Laura_Titjob_RightHand.png"    
                contains:
                    # Right Piercings                    
                    ConditionSwitch(
                            "not LauraX.Pierce",Null(),                                
                            "True",       "images/LauraSex/Laura_Titjob_Right_[LauraX.Pierce].png",
                            )                           
                subpixel True     
                pos (0,0) #top (0,-10)  
                transform_anchor True 
                parallel:
                    ease 2 ypos -30
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat  
        contains:
                #head
                "Laura_TJ_Head"   
                subpixel True       
                pos (0,0) #top (0,-10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat  
                parallel:
                    pause .1
                    ease 2 rotate -5
                    pause .1
                    ease 2 rotate 0
                    repeat  
        contains:
                #zero cock
                subpixel True
                "Laura_TJ_ZeroCock"
                pos (0,20) #top (0,-10)
                transform_anchor True
                rotate 2
                parallel:                  
                    ease 2 ypos 0    
                    pause .1
                    ease 2 ypos 20
                    pause .1
                    repeat         
        contains:
                #left tit
                contains:
                    "images/LauraSex/Laura_Titjob_LeftTit.png"        
                contains:
                    ConditionSwitch(
                            "'tits' not in LauraX.Spunk",Null(),                                
                            "True",       "images/LauraSex/Laura_Titjob_Spunk_Left.png",
                            )                         
                subpixel True       
                pos (0,5) #top (0,-10)
                transform_anchor True
                parallel:
                    pause .2
                    ease 1.9 ypos -30
                    pause .2
                    ease 1.9 ypos 5
                    repeat  
        contains:
                #left hand
                "Laura_TJ_LeftArm"
                subpixel True       
                pos (0,0) #top (0,-10)   
                transform_anchor True
                parallel:
                    ease 2 ypos -30
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat  
        contains:
                #mid hair
                "Laura_TJ_HairMid"   
                subpixel True       
                pos (0,0) #top (0,+10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos -15
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat  
                parallel:
                    pause .1
                    ease 2 rotate -5
                    pause .1
                    ease 2 rotate 0
                    repeat   
        contains:
                #head
                "Laura_TJ_HairTop"   
                subpixel True       
                pos (0,0) #top (0,-10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat    
                parallel:
                    pause .1
                    ease 2 rotate -5
                    pause .1
                    ease 2 rotate 0
                    repeat  
# End Laura TJ Pose 4 cumming / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start 5 (cumming low) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Laura_TJ_5:                                                                        
        #Her Body in the TJ pose, cumming low
        contains:
                #hairback
                "Laura_TJ_HairBack"   
                subpixel True    
                pos (-30,155)
                transform_anchor True
                rotate -20
                parallel:
                    ease 2 ypos 140
                    pause .1
                    ease 2 ypos 155
                    pause .1
                    repeat
#        contains:
#                #base body
#                contains:
#                    "images/LauraSex/Laura_Titjob_Body.png"      
#                subpixel True   
#                pos (-80,-200)
#                transform_anchor True
#                rotate -20
#                parallel:
#                    ease 2 ypos -220
#                    pause .1
#                    ease 2 ypos -200
#                    pause .1
#                    repeat 
        contains:
                #base body 
                "Laura_TJ_Body"      
                subpixel True        
                pos (185,70)
                transform_anchor True
                rotate -20
                parallel:
                    ease 2 ypos 50
                    pause .1
                    ease 2 ypos 70
                    pause .1
                    repeat                   
        contains:
                #right hand backside
                contains:
                    "images/LauraSex/Laura_Titjob_RightHandBack.png"      
                subpixel True     
                pos (-80,-180)
                transform_anchor True
                rotate -10
                parallel:
                    ease 2 ypos -200
                    pause .1
                    ease 2 ypos -180
                    pause .1
                    repeat  
        contains:
                #right tit
                contains:
                    "images/LauraSex/Laura_Titjob_RightTit.png"            
                contains:
                    ConditionSwitch(
                            "'tits' not in LauraX.Spunk",Null(),                                
                            "True",       "images/LauraSex/Laura_Titjob_Spunk_Right.png",
                            )       
                subpixel True       
                pos (-80,-160)
                transform_anchor True
                rotate -10
                parallel:
                    ease .4 ypos -170
                    ease 1.7 ypos -190
                    pause .1
                    ease 2 ypos -160
                    repeat  
        contains:
                #right hand
                contains:
                    "images/LauraSex/Laura_Titjob_RightHand.png"    
                contains:
                    # Right Piercings                    
                    ConditionSwitch(
                            "not LauraX.Pierce",Null(),                                
                            "True",       "images/LauraSex/Laura_Titjob_Right_[LauraX.Pierce].png",
                            )                           
                subpixel True     
                pos (-80,-180)
                transform_anchor True
                rotate -10
                parallel:
                    ease 2 ypos -200
                    pause .1
                    ease 2 ypos -180
                    pause .1
                    repeat   
        contains:
                #head
                "Laura_TJ_Head"   
                subpixel True       
                pos (-30,155)
                transform_anchor True
                rotate -20
                parallel:
                    ease 2 ypos 140
                    pause .1
                    ease 2 ypos 155
                    pause .1
                    repeat 
        contains:
                #zero cock
                subpixel True
                "Laura_TJ_ZeroCock"
                pos (0,20) #top (0,-10)
                transform_anchor True
                rotate 2  
                parallel:                  
                    ease 2 ypos 0    
                    pause .1
                    ease 2 ypos 20
                    pause .1
                    repeat 
        contains:
                #left tit
                contains:
                    "images/LauraSex/Laura_Titjob_LeftTit.png"         
                contains:
                    ConditionSwitch(
                            "'tits' not in LauraX.Spunk",Null(),                                
                            "True",       "images/LauraSex/Laura_Titjob_Spunk_Left.png",
                            )                           
                subpixel True   
                pos (-80,-160)
                transform_anchor True
                rotate -10
                parallel:
                    ease .4 ypos -170
                    ease 1.7 ypos -190
                    pause .1
                    ease 2 ypos -160
                    repeat  
        contains:
                #left hand
                "Laura_TJ_LeftArm"
                subpixel True     
                pos (-80,-180)
                transform_anchor True
                rotate -10
                parallel:
                    ease 2 ypos -200
                    pause .1
                    ease 2 ypos -180
                    pause .1
                    repeat  
        contains:
                #mid hair
                "Laura_TJ_HairMid"   
                subpixel True   
                pos (-30,115)
                transform_anchor True
                rotate -10
                parallel:
                    ease 2 ypos 95
                    pause .1
                    ease 2 ypos 115
                    pause .1
                    repeat  
        contains:
                #head
                "Laura_TJ_HairTop"   
                subpixel True    
                pos (-30,155)
                transform_anchor True
                rotate -20
                parallel:
                    ease 2 ypos 140
                    pause .1
                    ease 2 ypos 155
                    pause .1
                    repeat  
# End Laura TJ Pose 5 cumming / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Laura's TJ animations end / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Laura_TJ_Launch(Line = 0):    # The sequence to launch the Laura Titfuck animations   
    if renpy.showing("Laura_TJ_Animation"):
        return
    call Laura_Hide
    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
        alpha 1
        ease 1 zoom 2.3 xpos 750 yoffset -100
    if Line == "L": # Laura gets started. . .
            if Taboo: 
                if len(Present) >= 2:
                    if Present[0] != LauraX:
                            "[LauraX.Name] looks back at [Present[0].Name] to see if she's watching."
                    elif Present[1] != LauraX:
                            "[LauraX.Name] looks back at [Present[1].Name] to see if she's watching."
                else:
                            "[LauraX.Name] casually glances around to see if anyone can see her."
            "[LauraX.Name] bends over and places your cock between her breasts."   
    
    if LauraX.Chest and LauraX.Over:
        "She throws off her [LauraX.Over] and her [LauraX.Chest]."                
    elif LauraX.Over:
        "She throws off her [LauraX.Over], baring her breasts underneath."
    elif LauraX.Chest:
        "She tugs off her [LauraX.Chest] and throws it aside."
    $ LauraX.Over = 0
    $ LauraX.Chest = 0
    $ LauraX.ArmPose = 0
    
    call Laura_First_Topless           
     
    show blackscreen onlayer black with dissolve   
    show Laura_Sprite zorder LauraX.Layer:
        alpha 0
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "titjob"
    show Laura_TJ_Animation zorder 150:
        pos (700,520) #700,420)
    $ Player.Sprite = 1
    hide blackscreen onlayer black with dissolve
    return
    
label Laura_TJ_Reset: 
    # The sequence to the Laura animations from Titfuck to default
    if not renpy.showing("Laura_TJ_Animation"):
        return
#    hide Laura_TJ_Animation
    call Laura_Hide 
    $ Player.Sprite = 0
    
    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
        zoom 2.3 xpos 750 yoffset -100
    show Laura_Sprite zorder LauraX.Layer:
        alpha 1
        ease 1 zoom 1.5 xpos 700 yoffset 50
        pause .5
        ease .5 zoom 1 xpos LauraX.SpriteLoc yoffset 0         
    "Laura pulls back"
    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
        alpha 1
        zoom 1 offset (0,0) xpos LauraX.SpriteLoc  
    return
            
# End Laura TJ Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /







# Laura Misc Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
       
        
        
label Laura_Kissing_Launch(T = Trigger):    
    call Laura_Hide
    $ Trigger = T
    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer
    show Laura_Sprite at SpriteLoc(StageCenter) zorder LauraX.Layer:
        ease 0.5 offset (0,0) zoom 2 alpha 1
    return
    
label Laura_Kissing_Smooch:   
    $ LauraX.FaceChange("kiss")
    show Laura_Sprite at SpriteLoc(StageCenter) zorder LauraX.Layer:
        ease 0.5 xpos StageCenter offset (0,0) zoom 2 alpha 1
        pause 1
        ease 0.5 xpos LauraX.SpriteLoc zoom 1      
    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
        zoom 1
    $ LauraX.FaceChange("sexy") 
    return
            
label Laura_Breasts_Launch(T = Trigger):    
    call Laura_Hide
    $ Trigger = T
    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
#        ease 0.5 offset (-100,-200) zoom 2
        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
    return
        
label Laura_Pussy_Launch(T = Trigger):
    call Laura_Hide    
    $ Trigger = T
    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
    return
        
label Laura_Pos_Reset(Pose = 0):  
    if LauraX.Loc != bg_current:
            return
    call Laura_Hide 
    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
            ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
    show Laura_Sprite zorder LauraX.Layer:
            offset (0,0) 
            anchor (0.5, 0.0)
            zoom 1  
            xzoom 1 
            yzoom 1 
            alpha 1
            pos (LauraX.SpriteLoc,50)
    $ Trigger = Pose
    return
    
label Laura_Hide(Sprite=0):
        if renpy.showing("Laura_SexSprite"):
            call Laura_Sex_Reset
        hide Laura_SexSprite
        hide Laura_HJ_Animation
        hide Laura_BJ_Animation
        hide Laura_TJ_Animation 
        if Sprite:
                hide Laura_Sprite    
        return

# Interface items //////////////////////////////////////////////////////////////////////////////

image GropeLeftBreast_Laura:    
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

image GropeRightBreast_Laura:    
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
image LickRightBreast_Laura:   
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
            
image LickLeftBreast_Laura:   
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

image GropeThigh_Laura: 
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

image GropePussy_Laura: 
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

image FingerPussy_Laura: 
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
            
image Lickpussy_Laura:   
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

image VibratorRightBreast_Laura: 
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

image VibratorLeftBreast_Laura: 
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
            
image VibratorPussy_Laura: 
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

image VibratorAnal_Laura: 
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
            
image VibratorPussyInsert_Laura: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_Laura: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0



#Lesbian action animations.
image GirlGropeBothBreast_Laura: 
    contains:
        "GirlGropeLeftBreast_Laura"
    contains:
        "GirlGropeRightBreast_Laura"
    
image GirlGropeLeftBreast_Laura:  
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

image GirlGropeRightBreast_Laura:    
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

image GirlGropeThigh_Laura: 
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

image GirlGropePussy_LauraSelf:
    contains:
        "GirlGropePussy_Laura"
        anchor (0.5,0.5)
        rotate -40
#        yzoom -1
        pos (100,500) #(120,530)
    
image GirlGropePussy_Laura: 
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

image GirlFingerPussy_Laura: 
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

## Start Laura Faces / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
#label LauraFace(Emote = LauraX.Emote, B = LauraX.Blush, M = 0, Mouth = 0, Eyes = 0, Brows = 0):
#        # Emote is the chosen emote, B is the lush state
#        # M is whether the character is in a  manic state                 
#        $ Emote = LauraX.Emote if Emote == 5 else Emote
#        $ B = LauraX.Blush if B == 5 else B
        
#        if (LauraX.Forced or "angry" in LauraX.RecentActions) and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
#                $ Emote = "angry"     
#        elif LauraX.ForcedCount > 0 and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
#                $ Emote = "sad"  
            
#        if Emote == "normal":
#                $ LauraX.Mouth = "normal"
#                $ LauraX.Brows = "normal"
#                $ LauraX.Eyes = "normal"
#        elif Emote == "angry":
#                $ LauraX.Mouth = "kiss"
#                $ LauraX.Brows = "angry"
#                $ LauraX.Eyes = "sexy"
#        elif Emote == "bemused":
#                $ LauraX.Mouth = "lipbite"
#                $ LauraX.Brows = "sad"
#                $ LauraX.Eyes = "squint"
#        elif Emote == "closed":
#                $ LauraX.Mouth = "normal"
#                $ LauraX.Brows = "sad"
#                $ LauraX.Eyes = "closed"  
#        elif Emote == "confused":
#                $ LauraX.Mouth = "kiss"
#                $ LauraX.Brows = "confused"
#                $ LauraX.Eyes = "squint"
#        elif Emote == "kiss":
#                $ LauraX.Mouth = "kiss"
#                $ LauraX.Brows = "sad"
#                $ LauraX.Eyes = "closed"
#        elif Emote == "tongue":
#                $ LauraX.Mouth = "tongue"
#                $ LauraX.Brows = "sad"
#                $ LauraX.Eyes = "stunned" #"stunned"
#        elif Emote == "manic":
#                $ LauraX.Mouth = "lipbite"
#                $ LauraX.Brows = "sad"
#                $ LauraX.Eyes = "surprised"
#                $ LauraX.Blush = 1
#        elif Emote == "sad":
#                $ LauraX.Mouth = "sad"
#                $ LauraX.Brows = "sad"
#                $ LauraX.Eyes = "sexy"
#        elif Emote == "sadside":
#                $ LauraX.Mouth = "sad"
#                $ LauraX.Brows = "sad"
#                $ LauraX.Eyes = "side"
#        elif Emote == "sexy":
#                $ LauraX.Mouth = "lipbite"
#                $ LauraX.Brows = "sad"
#                $ LauraX.Eyes = "squint"
#        elif Emote == "smile":
#                if LauraX.Love >= 700:
#                    $ LauraX.Mouth = "smile"
#                else:
#                    $ LauraX.Mouth = "smirk"                
#                $ LauraX.Brows = "normal"
#                $ LauraX.Eyes = "normal"
#        elif Emote == "sucking":
#                $ LauraX.Mouth = "sucking"
#                $ LauraX.Brows = "sad"
#                $ LauraX.Eyes = "closed"
#        elif Emote == "surprised":
#                $ LauraX.Mouth = "kiss"
#                $ LauraX.Brows = "surprised"
#                $ LauraX.Eyes = "surprised"
#        elif Emote == "startled":
#                $ LauraX.Mouth = "smile"
#                $ LauraX.Brows = "surprised"
#                $ LauraX.Eyes = "surprised"
#        elif Emote == "down":
#                $ LauraX.Mouth = "sad"
#                $ LauraX.Brows = "sad"
#                $ LauraX.Eyes = "down"  
#        elif Emote == "perplexed":
#                $ LauraX.Mouth = "smile"
#                $ LauraX.Brows = "sad"
#                $ LauraX.Eyes = "surprised"
#        elif Emote == "sly":
#                if LauraX.Love >= 700:
#                    $ LauraX.Mouth = "smile"
#                else:
#                    $ LauraX.Mouth = "smirk" 
#                $ LauraX.Brows = "confused"
#                $ LauraX.Eyes = "squint"
            
#        if M:
#                $ LauraX.Eyes = "surprised"        
#        if B > 1:
#                $ LauraX.Blush = 2
#        elif B:
#                $ LauraX.Blush = 1
#        else:
#                $ LauraX.Blush = 0
        
#        if Mouth:
#                $ LauraX.Mouth = Mouth
#        if Eyes:
#                $ LauraX.Eyes = Eyes
#        if Brows:
#                $ LauraX.Brows = Brows
        
#        return
        
        
## Laura's Wardrobe //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#label LauraWardrobe:
#    menu:      
#        "View":
#            while True:
#                menu:
#                    "Default":
#                        call Laura_Pos_Reset
#                    "Face":
#                        call Laura_Kissing_Launch(0)
#                    "Body":
#                        call Laura_Pussy_Launch(0)
#                    "Back":
#                        jump LauraWardrobe 
#        # Outfits
##        "Teacher outfit":
##            $ LauraX.Outfit = "teacher"
##            call LauraOutfit
##        "Super outfit":
##            $ LauraX.Outfit = "costume"
##            call LauraOutfit
#        "Nude":
#            $ LauraX.Over = 0
#            $ LauraX.Chest = 0
#            $ LauraX.Legs = 0
#            $ LauraX.Panties = 0
#            $ LauraX.Gloves = 0
#            $ LauraX.Neck = 0
##            $ LauraX.Outfit = "nude"
##            call LauraOutfit
#        "Over":              
#            while True:
#                menu:
#                    # Overshirts    
#                    "Remove [LauraX.Over]" if LauraX.Over:
#                        $ LauraX.Over = 0
#                    "Add Jacket":
#                        $ LauraX.Over = "jacket"  
#                    "Add Towel":
#                        $ LauraX.Over = "towel" 
#                    "Toggle up-top":
#                        if LauraX.Uptop:
#                            $ LauraX.Uptop = 0
#                        else:
#                            $ LauraX.Uptop = 1   
#                    "Back":
#                        jump LauraWardrobe                
#        "Chests":            
#            while True:
#                menu:
#                    # Tops    
#                    "Remove [LauraX.Chest]" if LauraX.Chest:
#                        $ LauraX.Chest = 0
#                    "Add leather bra":
#                        $ LauraX.Chest = "leather bra"
#                    "Add wolvie top":
#                        $ LauraX.Chest = "wolvie top"
#                    "Add bikini top":
#                        $ LauraX.Chest = "bikini top"
#                    "Add corset":
#                        $ LauraX.Chest = "corset"
#                    "Add lace corset":
#                        $ LauraX.Chest = "lace corset"                       
#                    "Toggle Piercings":
#                        if LauraX.Pierce == "ring":
#                            $ LauraX.Pierce = "barbell"
#                        elif LauraX.Pierce == "barbell":
#                            $ LauraX.Pierce = 0
#                        else:
#                            $ LauraX.Pierce = "ring"
#                    "Toggle up-top":
#                        if LauraX.Uptop:
#                            $ LauraX.Uptop = 0
#                        else:
#                            $ LauraX.Uptop = 1   
#                    "Back":
#                        jump LauraWardrobe             
        
#        "Legs":            
#            while True:
#                menu:
#                    # Legs   
#                    "Remove legs" if LauraX.Legs:     
#                        $ LauraX.Legs = 0
#                    "Add leather pants":
#                        $ LauraX.Legs = "leather pants"
#                        $ LauraX.Upskirt = 0
#                    "Add mesh pants":
#                        $ LauraX.Legs = "mesh pants"
#                        $ LauraX.Upskirt = 0
#                    "Add skirt":
#                        $ LauraX.Legs = "skirt"
#                    "Toggle upskirt":
#                        if LauraX.Upskirt:
#                            $ LauraX.Upskirt = 0
#                        else:
#                            $ LauraX.Upskirt = 1
#                    "Back":
#                        jump LauraWardrobe    
        
#        "Underwear":            
#            while True:
#                menu:
#                    # Underwear
#                    "Hose":
#                        menu:
#                            "Add hose":     
#                                $ LauraX.Hose = "stockings"  
#                            "Add garter":     
#                                $ LauraX.Hose = "garterbelt"  
#                            "Add stockings and garter":     
#                                $ LauraX.Hose = "stockings and garterbelt"  
##                            "Add pantyhose":     
##                                $ LauraX.Hose = "pantyhose"   
##                            "Add tights":     
##                                $ LauraX.Hose = "tights"   
##                            "Add ripped hose":     
##                                $ LauraX.Hose = "ripped pantyhose"   
##                            "Add ripped tights":     
##                                $ LauraX.Hose = "ripped tights"   
##                            "Add tights":     
##                                $ LauraX.Hose = "tights"    
#                            "Remove hose" if LauraX.Hose:     
#                                $ LauraX.Hose = 0  

##                    "toggle boots":    
##                        if not LauraX.Boots:
##                            $ LauraX.Boots = "thigh boots"   
##                        else:
##                            $ LauraX.Boots = 0     
                        
#                    "Remove panties" if LauraX.Panties:     
#                        $ LauraX.Panties = 0     
#                    "Add black panties":
#                        $ LauraX.Panties = "black panties"
##                    "Add shorts":
##                        $ LauraX.Panties = "shorts"
#                    "Add wolvie panties":
#                        $ LauraX.Panties = "wolvie panties"  
#                    "Add bikini bottoms":
#                        $ LauraX.Panties = "bikini bottoms"  
#                    "Add lace panties":
#                        $ LauraX.Panties = "lace panties"    
#                    "pull down-up panties":
#                        if LauraX.PantiesDown:
#                            $ LauraX.PantiesDown = 0
#                        else:
#                            $ LauraX.PantiesDown = 1
#                    "Back":
#                        jump LauraWardrobe    
#        "Face":
#            while True:
#                menu: 
#                    "Brows=[LauraX.Brows], Eyes=[LauraX.Eyes], Mouth=[LauraX.Mouth]"
#                    "Emotions":
#                            call LauraEmotionEditor
#                    "Toggle Brows":
#                            if LauraX.Brows == "normal":
#                                $ LauraX.Brows = "angry"
#                            elif LauraX.Brows == "angry":
#                                $ LauraX.Brows = "confused"
#                            elif LauraX.Brows == "confused":
#                                $ LauraX.Brows = "sad"
#                            elif LauraX.Brows == "sad":
#                                $ LauraX.Brows = "surprised"
#                            else:
#                                $ LauraX.Brows = "normal"
#                    "Toggle Eyes Emotions":
#                            if LauraX.Eyes == "normal":                          
#                                $ LauraX.Eyes = "surprised"
#                            elif LauraX.Eyes == "surprised":
#                                $ LauraX.Eyes = "sexy"
#                            elif LauraX.Eyes == "sexy":
#                                $ LauraX.Eyes = "squint"
#                            elif LauraX.Eyes == "squint":
#                                $ LauraX.Eyes = "closed"
#                            else:
#                                $ LauraX.Eyes = "normal"
#                    "Toggle Eyes Directions":
#                            if LauraX.Eyes == "normal":
#                                $ LauraX.Eyes = "side"
#                            elif LauraX.Eyes == "side":
#                                $ LauraX.Eyes = "down"
#                            elif LauraX.Eyes == "down":
#                                $ LauraX.Eyes = "leftside"
#                            elif LauraX.Eyes == "leftside":
#                                $ LauraX.Eyes = "stunned"
#                            else:
#                                $ LauraX.Eyes = "normal"  
#                    "Toggle Mouth Normal":
#                            if LauraX.Mouth  == "normal":
#                                $ LauraX.Mouth = "sad"
#                            elif LauraX.Mouth == "sad":
#                                $ LauraX.Mouth = "smile"
#                            elif LauraX.Mouth == "smile":
#                                $ LauraX.Mouth = "surprised"
#                            else:
#                                $ LauraX.Mouth = "normal"  
#                    "Toggle Mouth Sexy":
#                            if LauraX.Mouth  == "normal":
#                                $ LauraX.Mouth = "kiss"
#                            elif LauraX.Mouth == "kiss":
#                                $ LauraX.Mouth = "sucking"
#                            elif LauraX.Mouth == "sucking":
#                                $ LauraX.Mouth = "tongue"
#                            elif LauraX.Mouth == "tongue":
#                                $ LauraX.Mouth = "lipbite"
#                            else:
#                                $ LauraX.Mouth = "normal"  
#                    "Toggle Blush":
#                        if LauraX.Blush == 1:
#                            $ LauraX.Blush = 2
#                        elif LauraX.Blush:
#                            $ LauraX.Blush = 0
#                        else:
#                            $ LauraX.Blush = 1
                            
#                    "Back":
#                            jump LauraWardrobe    
#        "Misc":
#            while True:
#                menu: 
#                    "Toggle Arm pose":
#                        if LauraX.ArmPose == 1:
#                            $ LauraX.ArmPose = 2
#                        else:
#                            $ LauraX.ArmPose = 1
#                    "Toggle Claws":
#                        if LauraX.Claws:
#                            $ LauraX.Claws = 0
#                        else:
#                            $ LauraX.Claws = 1
#                    "Toggle Wetness" if True:
#                        if not LauraX.Wet:
#                            $ LauraX.Wet = 1
#                        elif LauraX.Wet == 1:
#                            $ LauraX.Wet = 2
#                        else:
#                            $ LauraX.Wet  = 0
#                    "Toggle wet look" if True:
#                        if not LauraX.Water:
#                            $ LauraX.Water = 1
#                        elif LauraX.Water == 1:
#                            $ LauraX.Water = 3
#                        else:
#                            $ LauraX.Water  = 0
#                    "Toggle pubes":
#                        if not LauraX.Pubes:
#                            $ LauraX.Pubes = 1
#                        else:
#                            $ LauraX.Pubes = 0
#                    "Spunk":
#                        menu:                            
#                            "Toggle Mouth Spunk":
#                                if "mouth" in LauraX.Spunk:
#                                    $ LauraX.Spunk.remove("mouth")
#                                else:
#                                    $ LauraX.Spunk.append("mouth")
#                            "Toggle hand Spunk":
#                                if "hand" in LauraX.Spunk:
#                                    $ LauraX.Spunk.remove("hand")
#                                else:
#                                    $ LauraX.Spunk.append("hand")                                    
#                            "Toggle Facial Spunk":
#                                if "facial" in LauraX.Spunk and "hair" not in LauraX.Spunk:
#                                    $ LauraX.Spunk.append("hair")
#                                elif "facial" in LauraX.Spunk:
#                                    $ LauraX.Spunk.remove("facial")                
#                                    $ LauraX.Spunk.remove("hair")
#                                else:
#                                    $ LauraX.Spunk.append("facial")                
#                            "Toggle Pussy Spunk" if True:
#                                if "in" in LauraX.Spunk:
#                                    $ LauraX.Spunk.remove("in")
#                                else:
#                                    $ LauraX.Spunk.append("in")             
#                            "Toggle Anal Spunk" if True:
#                                if "anal" in LauraX.Spunk:
#                                    $ LauraX.Spunk.remove("anal")
#                                else:
#                                    $ LauraX.Spunk.append("anal")        
#                            "Toggle Belly Spunk" if True:
#                                if "belly" in LauraX.Spunk:
#                                    $ LauraX.Spunk.remove("belly")
#                                else:
#                                    $ LauraX.Spunk.append("belly")        
#                            "Toggle Tits Spunk" if True:
#                                if "tits" in LauraX.Spunk:
#                                    $ LauraX.Spunk.remove("tits")
#                                else:
#                                    $ LauraX.Spunk.append("tits")
#                    "Toggle Piercings":
#                        if LauraX.Pierce == "ring":
#                            $ LauraX.Pierce = "barbell"
#                        elif LauraX.Pierce == "barbell":
#                            $ LauraX.Pierce = 0
#                        else:
#                            $ LauraX.Pierce = "ring"
#                    "Add leash choker" if not LauraX.Neck:
#                        $ LauraX.Neck = "leash choker"
#                    "Remove choker" if LauraX.Neck:
#                        $ LauraX.Neck = 0
                        
#                    "Add wristbands" if not LauraX.Arms:
#                        $ LauraX.Arms = "wrists"
#                    "Remove Gloves" if LauraX.Arms:
#                        $ LauraX.Arms = 0
#                    "Back":
#                        jump LauraWardrobe               
##        "Set Custom Outfit #1.":
##            $ LauraX.Custom[0] = 1
##            $ LauraX.Custom[1] = LauraX.Arms
##            $ LauraX.Custom[2] = LauraX.Legs
##            $ LauraX.Custom[3] = LauraX.Over
##            $ LauraX.Custom[4] = LauraX.Under #fix, this can be changed to something else, no longer necessary
##            $ LauraX.Custom[5] = LauraX.Chest
##            $ LauraX.Custom[6] = LauraX.Panties 
##            $ LauraX.Custom[7] = LauraX.Pubes 
##            $ LauraX.Custom[8] = LauraX.Hair
##            $ LauraX.Custom[9] = LauraX.Hose
##        "Wear Custom Outfit #[LauraX.Custom[0]]." if LauraX.Custom[0]:
##            $ Line = LauraX.Outfit
##            $ LauraX.Outfit = "custom1"
##            call RogueOutfit
##            $ LauraX.Outfit = Line
#        "Nothing":
#            return
#    jump LauraWardrobe
#return

#label LauraEmotionEditor(CountStore = "normal"):
#    menu:
#        "Emotions1: Normal Angry Smiling Sexy Surprised Bemused Manic.":        
#            menu:
#                "Normal":
#                    $ LauraX.Emote = "normal"
#                    call LauraFace
#                "Angry":
#                    $ LauraX.Emote = "angry"
#                    call LauraFace
#                "Smiling":
#                    $ LauraX.Emote = "smile"
#                    call LauraFace
#                "Sexy":
#                    $ LauraX.Emote = "sexy"
#                    call LauraFace
#                "Suprised":
#                    $ LauraX.Emote = "surprised"
#                    call LauraFace
#                "Bemused":
#                    $ LauraX.Emote = "bemused"
#                    call LauraFace
#                "Manic":
#                    $ LauraX.Emote = "manic"
#                    call LauraFace
                    
#        "Emotions2: Sad Sucking Kiss Tongue Confused Closed Down.":  
#            menu:
#                "Sad":
#                    $ LauraX.Emote = "sad"
#                    call LauraFace
#                "Sucking":
#                    $ LauraX.Emote = "sucking"
#                    call LauraFace
#                "kiss":
#                    $ LauraX.Emote = "kiss"
#                    call LauraFace
#                "Tongue":
#                    $ LauraX.Emote = "tongue"
#                    call LauraFace
#                "confused":
#                    $ LauraX.Emote = "confused"
#                    call LauraFace
#                "Closed":
#                    $ LauraX.Emote = "closed"
#                    call LauraFace
#                "Down":
#                    $ LauraX.Emote = "down"
#                    call LauraFace
                    
#        "Emotions3: Sadside Startled Perplexed Sly":  
#            menu:
#                "Sadside":
#                    $ LauraX.Emote = "sadside"
#                    call LauraFace
#                "Startled":
#                    $ LauraX.Emote = "startled"
#                    call LauraFace
#                "Perplexed":
#                    $ LauraX.Emote = "perplexed"
#                    call LauraFace
#                "Sly":
#                    $ LauraX.Emote = "sly"
#                    call LauraFace
#        "Toggle Mouth Spunk":
#            if "mouth" in LauraX.Spunk:
#                $ LauraX.Spunk.remove("mouth")
#            else:
#                $ LauraX.Spunk.append("mouth")
#        "Toggle hand Spunk":
#            if "hand" in LauraX.Spunk:
#                $ LauraX.Spunk.remove("hand")
#            else:
#                $ LauraX.Spunk.append("hand")
                
#        "Toggle Facial Spunk":
#            if "facial" in LauraX.Spunk and "hair" not in LauraX.Spunk:
#                $ LauraX.Spunk.append("hair")
#            elif "facial" in LauraX.Spunk:
#                $ LauraX.Spunk.remove("facial")                
#                $ LauraX.Spunk.remove("hair")
#            else:
#                $ LauraX.Spunk.append("facial")
            
#        "Blush":
#            if LauraX.Blush == 2:
#                $ LauraX.Blush = 0
#            elif LauraX.Blush:
#                $ LauraX.Blush = 2
#            else:
#                $ LauraX.Blush = 1  
#        "Exit.":
#            return
#    jump LauraEmotionEditor
return