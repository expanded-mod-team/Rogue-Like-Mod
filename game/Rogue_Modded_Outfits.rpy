# Rogue's Clothes ///////////////////
label Rogue_Modded_Clothes_Menu:    
    call RogueFace
    menu:
        ch_r "So what did you want to tell me about my clothes again?"
        "Let's talk about your over shirts.":
                jump Rogue_Modded_Clothes_Over        
        "Let's talk about your legwear.":
                jump Rogue_Modded_Clothes_Legs
        "Let's talk about your underwear.":
                jump Rogue_Modded_Clothes_Under
        # "Let's talk about your bodysuits.":
        #         jump Rogue_Modded_Clothes_BodySuits
        "Let's talk about the other stuff.":
                jump Rogue_Modded_Clothes_Misc
        "Save as main menu background clothes.":
                "This option will save this Rogue at the main menu background, are you sure?"
                menu:
                    "Yes":
                        "do it"
                        $ persistent.R_BG_Over = R_Over
                        $ persistent.R_BG_Chest = R_Chest
                        $ persistent.R_BG_BodySuit = R_BodySuit
                        $ persistent.R_BG_Neck = R_Neck
                        $ persistent.R_BG_Legs = R_Legs
                        $ persistent.R_BG_Panties = R_Panties
                        $ persistent.R_BG_Arms = R_Arms
                        $ persistent.R_BG_Accessory = R_Accessory
                        $ persistent.R_BG_Glasses = R_Glasses
                        # $ persistent.R_BG_Gloves = R_Gloves
                        $ persistent.R_BG_Tan = R_Tan
                        # $ persistent.R_BG_DynamicTan = R_DynamicTan
                        $ persistent.R_BG_Pierce = R_Pierce
                        $ persistent.R_BG_Hair = R_Hair
                        $ persistent.R_BG_Water = R_Water
                        $ persistent.R_BG_HairColor = R_HairColor
                        $ persistent.R_BG_Pubes = R_Pubes
                        $ persistent.R_BG_Hose = R_Hose
                        $ persistent.R_BG_Headband = R_Headband
                        $ persistent.R_BG_Gag = R_Gag
                        # $ persistent.R_BG_Blindfold = R_Blindfold
                        $ persistent.R_BG_Boots = R_Boots

                    "No":
                        pass
        "Never mind, you look good like that. [[return]":            
                jump Rogue_Clothes
            
    jump Rogue_Modded_Clothes_Menu
    #End of Rogue Wardrobe Main Menu

    menu Rogue_Modded_Clothes_Over:                                                                                            # Overshirts    
        "Why don't you go with no Overshirt?" if R_Over:
                        call RogueFace("bemused", 1)
                        if R_Chest or R_BodySuit or (R_SeenChest and ApprovalCheck("Rogue", 600)):
                            ch_r "Sure."
                        elif ApprovalCheck("Rogue", 1100, TabM=0):
                            ch_r "I guess I don't really mind if you see them. . ."                
                            call Rogue_First_Topless
                        else:
                            ch_r "I'm afraid I don't have anything on under this."
                            jump Rogue_Modded_Clothes_Menu   
                        $ R_Over = 0
                        
        "Try on a mesh top.":
                        call RogueFace("bemused", 1)
                        if R_Chest or R_BodySuit  or (R_SeenChest and ApprovalCheck("Rogue", 500)):
                            ch_r "Sure."
                        elif ApprovalCheck("Rogue", 1100, TabM=0):
                            ch_r "I guess I don't really mind if you see them. . ."                
                            call Rogue_First_Topless
                        else:
                            ch_r "I'm afraid that top is a bit sheer to have nothing under it."
                            jump Rogue_Modded_Clothes_Menu
                        menu:
                            ch_r "Which do you prefer?"
                            "The green one looks good on you." if R_Over != "mesh top":
                                call SetOverRogue("mesh top")
                            "The white one gives off a good vibe." if R_Over != "modded white mesh top":
                                call SetOverRogue("modded white mesh top")
                            "The blue one looks nice on you." if R_Over != "modded blue mesh top":
                                call SetOverRogue("modded blue mesh top")
                            "{i}Love{/i} the red one." if R_Over != "modded red mesh top":
                                call SetOverRogue("modded red mesh top")
                            "The yellow one makes me nostalgic." if R_Over != "modded yellow mesh top":
                                call SetOverRogue("modded yellow mesh top")
                            "I like the black one." if R_Over != "modded black mesh top":
                                call SetOverRogue("modded black mesh top")
                            "I like the SR7 one." if R_Over != "modded SR7 mesh top":
                                call SetOverRogue("modded SR7 mesh top")
                        menu:
                            ch_r "With the collar?"
                            "Yes":
                                $ R_Neck = "spiked collar"
                            "No":
                                $ R_Neck = 0
                        if R_Chest == "buttoned tank":
                            $ R_Chest = "tank"
                            
        "How about your top?":
                        menu:
                            ch_r "Which one do you like?"
                            "The pink one looks good on you." if R_Over != "pink top":
                                call SetOverRogue("pink top")
                                $ R_Neck = 0
                            "I like the red one." if R_Over != "modded red top":
                                call SetOverRogue("modded red top")
                                $ R_Neck = 0   
                        
        "How about your hoodie?":
                        menu:
                            ch_r "Which one do you like?"
                            "The green one suits you well." if R_Over != "hoodie":
                                call SetOverRogue("hoodie")
                            "The blue one looks nice on you." if R_Over != "modded blue hoodie":
                                call SetOverRogue("modded blue hoodie")
                            "The red one looks hot." if R_Over != "modded red hoodie":
                                call SetOverRogue("modded red hoodie")
                            "The yellow one is pretty good." if R_Over != "modded yellow hoodie":
                                call SetOverRogue("modded yellow hoodie")
                            "The black one is nice." if R_Over != "modded black hoodie":
                                call SetOverRogue("modded black hoodie")
                            "I like the white one" if R_Over != "modded white hoodie":
                                call SetOverRogue("modded white hoodie")

        "How about your jacket?" if R_Over != "modded classic jacket":
                call SetOverRogue("modded classic jacket")

                        
        "Maybe just throw on a towel?" if R_Over != "towel":
            call RogueFace("bemused", 1)
            if R_Chest or R_BodySuit  or R_SeenChest:
                ch_r "Fresh."
            elif ApprovalCheck("Rogue", 900, TabM=0):
                call RogueFace("perplexed", 1)
                ch_r "I suppose? . ."          
            else:
                ch_r "That don't leave much to the imagination. . ."
                jump Rogue_Modded_Clothes_Menu  
            call SetOverRogue("towel")

        # "How about that red dress?" if R_Over != "modded red dress":
        #     if R_Legs:
        #         ch_r "I can't really wear that with my [R_Legs] on."
        #     elif ApprovalCheck("Rogue", 1000) or R_BodySuit:
        #         ch_r "Sure. . ."
        #         call SetOverRogue("modded red dress")

        #     else:
        #         ch_r "That's a bit . . . revealing."   

        # "How about that blue dress?" if R_Over != "modded blue dress":
        #     if R_Legs:
        #         ch_r "I can't really wear that with my [R_Legs] on."
        #     elif ApprovalCheck("Rogue", 1000) or R_BodySuit :
        #         ch_r "Sure. . ."
        #         call SetOverRogue("modded blue dress")

        #     else:
        #         ch_r "That's a bit . . . revealing."    
            
        "How about that green nighty I got you?" if R_Over != "nighty" and "nighty" in R_Inventory:
                        if R_Legs:
                            ch_r "I can't really wear that with my [R_Legs] on."
                        elif ApprovalCheck("Rogue", 1100, TabM=3):
                            ch_r "Sure. . ."
                            call SetOverRogue("nighty")
                            if "lace bra" in R_Inventory:
                                call SetChestRogue("lace bra")
                            else:
                                call SetChestRogue("bra")
                            if "lace panties" in R_Inventory:
                                call SetPantiesRogue("lace panties")
                            else:
                                call SetPantiesRogue("black panties")
                            menu:
                                extend ""
                                "Nice.":
                                    pass
                                "I meant {i}just{/i} the nighty.":
                                    if ApprovalCheck("Rogue", 1400, TabM=3):
                                        "She shrugs off her bra and then pulls the nighty back up."
                                        $ R_Panties = 0
                                        $ R_Chest = 0
                                        $ R_BodySuit = 0
                                        ch_r "Hmmm, alright. . ."
                                    elif ApprovalCheck("Rogue", 1200, TabM=3):
                                        $ R_Chest = 0
                                        $ R_BodySuit = 0
                                        ch_r "I'll keep my panties on, thanks."
                                    else:
                                        ch_r "Be happy with what you get."
                        else:
                            ch_r "That's a bit . . . revealing."
                
        "Never mind":
            pass           
    jump Rogue_Modded_Clothes_Menu
    #End of Rogue Top
                       
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<                        
                       
    menu Rogue_Modded_Clothes_Legs:                                                                                                    # Leggings   
        "Lose the skirt. . ." if R_Legs == "skirt" or R_Legs == "modded cheerleader skirt": 
                        call RogueFace("sexy", 1)
                        if R_BodySuit:
                            ch_r "Sure."
                            $ R_Legs = 0
                        elif R_SeenPanties and R_Panties and ApprovalCheck("Rogue", 500, TabM=5):
                            ch_r "Sure."             
                            $ R_Legs = 0
                        elif R_SeenPussy and ApprovalCheck("Rogue", 800, TabM=4):
                            ch_r "Sure, why not?"             
                            $ R_Legs = 0
                        elif ApprovalCheck("Rogue", 1100, TabM=2) and R_Panties: 
                            ch_r "Well, I suppose if it's for you. . ."
                            $ R_SeenPanties = 1             
                            $ R_Legs = 0
                        elif ApprovalCheck("Rogue", 1400, TabM=3): #No panties
                            ch_r "Well, I suppose if it's for you. . ."                
                            $ R_Legs = 0
                            call Rogue_First_Bottomless
                        elif Taboo:
                            ch_r "Not in public, [R_Petname]."
                        else:
                            ch_r "Not in front of you, [R_Petname]."
                            if not R_Panties:
                                ch_r "Maybe if I put some panties on first. . ."

        "Lose the short skirt. . ." if R_Legs == "modded skirtshort" or R_Legs == "modded SR7 skirtshort" or R_Legs == "modded cheerleader skirtshort": 
                        call RogueFace("sexy", 1)
                        if R_BodySuit:
                            ch_r "Sure."
                            $ R_Legs = 0
                        elif R_SeenPanties and R_Panties and ApprovalCheck("Rogue", 500, TabM=5):
                            ch_r "Sure."             
                            $ R_Legs = 0
                        elif R_SeenPussy and ApprovalCheck("Rogue", 800, TabM=4):
                            ch_r "Sure, why not?"             
                            $ R_Legs = 0
                        elif ApprovalCheck("Rogue", 1100, TabM=2) and R_Panties: 
                            ch_r "Well, I suppose if it's for you. . ."
                            $ R_SeenPanties = 1             
                            $ R_Legs = 0
                        elif ApprovalCheck("Rogue", 1400, TabM=3): #No panties
                            ch_r "Well, I suppose if it's for you. . ."                
                            $ R_Legs = 0
                            call Rogue_First_Bottomless
                        elif Taboo:
                            ch_r "Not in public, [R_Petname]."
                        else:
                            ch_r "Not in front of you, [R_Petname]."
                            #if not R_Panties:
                            #    ch_r "Maybe if I put some panties on first. . ."
                                
        "How about that skirt?":
                        menu:
                            ch_r "Which version of my skirt?"
                            "The normal one" if R_Legs != "skirt":  
                              $ R_Legs = "skirt"
                              $ R_Upskirt = 0
                            "The cheerleader one" if R_Legs != "modded cheerleader skirt":  
                              call SetLegsRogue("modded cheerleader skirt")
                              $ R_Upskirt = 0

        "How about that short skirt?":
                        menu:
                            ch_r "Which version of my skirt?"
                            "The SR7 one" if R_Legs != "modded SR7 skirtshort":
                                 call RogueFace("sexy", 1)
                                 if R_BodySuit:
                                      ch_r "Sure."
                                      call SetLegsRogue("modded SR7 skirtshort")
                                      $ R_Upskirt = 0
                                 elif R_SeenPanties and R_Panties and ApprovalCheck("Rogue", 400, TabM=5):
                                      ch_r "Sure."             
                                      call SetLegsRogue("modded SR7 skirtshort")
                                      $ R_Upskirt = 0
                                 elif R_SeenPussy and ApprovalCheck("Rogue", 700, TabM=4):
                                      ch_r "Sure, why not?"             
                                      call SetLegsRogue("modded SR7 skirtshort")
                                      $ R_Upskirt = 0
                                 elif ApprovalCheck("Rogue", 1000, TabM=2) and R_Panties: 
                                      ch_r "Well, I suppose if it's for you. . ."
                                      $ R_SeenPanties = 1             
                                      call SetLegsRogue("modded SR7 skirtshort")
                                      $ R_Upskirt = 0
                                 elif ApprovalCheck("Rogue", 1300, TabM=3): #No panties
                                      ch_r "Well, I suppose if it's for you. . ."                
                                      call SetLegsRogue("modded SR7 skirtshort")
                                      $ R_Upskirt = 0
                                      call Rogue_First_Bottomless
                                 elif Taboo:
                                      ch_r "Not in public, [R_Petname]."
                                 else:
                                      ch_r "No, it's too short, [R_Petname]."
                            "The normal one" if R_Legs != "modded skirtshort":
                                 call RogueFace("sexy", 1)
                                 if R_BodySuit:
                                      ch_r "Sure."
                                      call SetLegsRogue("modded skirtshort")
                                      $ R_Upskirt = 0
                                 elif R_SeenPanties and R_Panties and ApprovalCheck("Rogue", 400, TabM=5):
                                      ch_r "Sure."             
                                      call SetLegsRogue("modded skirtshort")
                                      $ R_Upskirt = 0
                                 elif R_SeenPussy and ApprovalCheck("Rogue", 700, TabM=4):
                                      ch_r "Sure, why not?"             
                                      call SetLegsRogue("modded skirtshort")
                                      $ R_Upskirt = 0
                                 elif ApprovalCheck("Rogue", 1000, TabM=2) and R_Panties: 
                                      ch_r "Well, I suppose if it's for you. . ."
                                      $ R_SeenPanties = 1             
                                      call SetLegsRogue("modded skirtshort")
                                      $ R_Upskirt = 0
                                 elif ApprovalCheck("Rogue", 1300, TabM=3): #No panties
                                      ch_r "Well, I suppose if it's for you. . ."                
                                      call SetLegsRogue("modded skirtshort")
                                      $ R_Upskirt = 0
                                      call Rogue_First_Bottomless
                                 elif Taboo:
                                      ch_r "Not in public, [R_Petname]."
                                 else:
                                      ch_r "No, it's too short, [R_Petname]."
                            "The cheerleader one" if R_Legs != "modded cheerleader skirtshort":
                                call RogueFace("sexy", 1)
                                if R_BodySuit:
                                      ch_r "Sure."
                                      call SetLegsRogue("modded cheerleader skirtshort")
                                      $ R_Upskirt = 0
                                elif R_SeenPanties and R_Panties and ApprovalCheck("Rogue", 400, TabM=5):
                                      ch_r "Sure."             
                                      call SetLegsRogue("modded cheerleader skirtshort")
                                      $ R_Upskirt = 0
                                elif R_SeenPussy and ApprovalCheck("Rogue", 700, TabM=4):
                                      ch_r "Sure, why not?"             
                                      call SetLegsRogue("modded cheerleader skirtshort")
                                      $ R_Upskirt = 0
                                elif ApprovalCheck("Rogue", 1000, TabM=2) and R_Panties: 
                                      ch_r "Well, I suppose if it's for you. . ."
                                      $ R_SeenPanties = 1             
                                      call SetLegsRogue("modded cheerleader skirtshort")
                                      $ R_Upskirt = 0
                                elif ApprovalCheck("Rogue", 1300, TabM=3): #No panties
                                      ch_r "Well, I suppose if it's for you. . ."                
                                      call SetLegsRogue("modded cheerleader skirtshort")
                                      $ R_Upskirt = 0
                                      call Rogue_First_Bottomless
                                elif Taboo:
                                      ch_r "Not in public, [R_Petname]."
                                else:
                                      ch_r "No, it's too short, [R_Petname]."

        "Maybe go without the jeans." if R_Legs == "pants":
                        call RogueFace("sexy", 1)
                        if R_BodySuit:
                             ch_r "Sure."
                             $ R_Legs = 0
                        elif R_SeenPanties and R_Panties and ApprovalCheck("Rogue", 500, TabM=5):
                            $ R_Legs = 0    
                            ch_r "Sure."
                        elif R_SeenPussy and ApprovalCheck("Rogue", 900, TabM=4):
                            $ R_Legs = 0    
                            ch_r "Sure, why not?"
                        elif ApprovalCheck("Rogue", 1100, TabM=2) and R_Panties:
                            ch_r "Well, I suppose if it's for you. . ."
                            $ R_SeenPanties = 1
                            $ R_Legs = 0    
                        elif ApprovalCheck("Rogue", 1400, TabM=3) and not R_Panties:
                            ch_r "Well, I suppose if it's for you. . ."
                            $ R_Legs = 0    
                            call Rogue_First_Bottomless
                        else:
                            ch_r "Not in front of you, [R_Petname]."
                            if not R_Panties:
                                ch_r "Maybe if I put some panties on first. . ."
                                
        "Your ass looks tight in those jeans." if R_Legs != "pants":
                        $ R_Legs = "pants"
                        $ R_Hose = 0
                
        "The tights would look good with that." if R_Hose != 'tights' and R_Legs != "pants":     
                        $ R_Hose = "tights"                   
        "Your ripped tights would look good with that." if R_Hose != 'ripped tights' and "ripped tights" in R_Inventory and R_Legs != "pants":     
                        $ R_Hose = "ripped tights"           
        "You could lose the tights." if R_Hose == 'ripped tights' or R_Hose == 'tights':     
                        $ R_Hose = 0  
            
        "What about wearing your shorts?":
                        menu:
                          ch_r "Which color would suit me best?"
                          "The green one suits you well." if R_Panties != "shorts":
                                ch_r "Alright."
                                call SetPantiesRogue("shorts")
                          "The blue one looks nice on you." if R_Panties != "modded blue shorts":
                                ch_r "Alright."
                                call SetPantiesRogue("modded blue shorts")
                          "The red one looks hot." if R_Panties != "modded red shorts":
                                ch_r "Alright."
                                call SetPantiesRogue("modded red shorts")
                                
                                            
        "Why don't you lose the shorts?" if R_Panties == "shorts" or R_Panties == "modded red shorts" or R_Panties == "modded blue shorts":
                        call RogueFace("sexy", 1)
                        if R_BodySuit:
                             ch_r "Sure."
                        elif R_SeenPussy and ApprovalCheck("Rogue", 500, TabM=4): # You've seen her pussy
                            if ApprovalCheck("Rogue", 800, "L"):               
                                ch_r "Well aren't you cheeky. . ."
                            elif ApprovalCheck("Rogue", 500, "O"):
                                ch_r "Fine by me."
                            elif ApprovalCheck("Rogue", 350, "I"):
                                ch_r "Oooh, naughty."
                            else:
                                ch_r "Oh, I guess I could."    
                                
                        elif not R_Legs:                       #she's not wearing anything over them
                            ch_r "I'm not wearing anything under these, you know. . ."
                            menu:
                                "Then you could slip on the green panties. . .":
                                            if ApprovalCheck("Rogue", 1100, TabM=3):
                                                $ R_SeenPanties = 1
                                                ch_r "Sure, ok."
                                                call SetPantiesRogue("green panties")
                                            else:
                                                ch_r "You'll have to wait, [R_Petname]."
                                                jump Rogue_Modded_Clothes_Legs

                                "Then you could slip on the black large panties. . .":
                                            if ApprovalCheck("Rogue", 1100, TabM=3):
                                                $ R_SeenPanties = 1
                                                ch_r "Sure, ok."
                                                call SetPantiesRogue("modded black large panties")
                                            else:
                                                ch_r "You'll have to wait, [R_Petname]."
                                                jump Rogue_Modded_Clothes_Legs
                                        
                                "Then you could wear the black panties. . .":
                                            if ApprovalCheck("Rogue", 1200, TabM=3):
                                                $ R_SeenPanties = 1
                                                ch_r "Alright."                
                                                call SetPantiesRogue("black panties")
                                            else:
                                                ch_r "Maybe some other time, [R_Petname]."  
                                                jump Rogue_Modded_Clothes_Legs                                      
                                        
                                "Then you could wear the lace panties. . .":
                                            if ApprovalCheck("Rogue", 1200, TabM=3):
                                                $ R_SeenPanties = 1
                                                ch_r "Alright."                
                                                call SetPantiesRogue("lace panties")
                                            else:
                                                ch_r "Maybe some other time, [R_Petname]."
                                                jump Rogue_Modded_Clothes_Legs
                                                
                                "You could always just wear nothing at all. . .":
                                            if ApprovalCheck("Rogue", 1100, "LI", TabM=3) and R_Love > R_Inbt:               
                                                ch_r "Well aren't you cheeky. . . I suppose I could give you a show. . ."
                                            elif ApprovalCheck("Rogue", 750, "OI", TabM=3) and R_Obed > R_Inbt:
                                                ch_r "If that's what you want."
                                            elif ApprovalCheck("Rogue", 500, "I", TabM=3):
                                                ch_r "Oooh, naughty."
                                            elif ApprovalCheck("Rogue", 1400, TabM=3):
                                                ch_r "Oh, fine. You've been a good boy."
                                            else: 
                                                call RogueFace("surprised")
                                                $ R_Brows = "angry"
                                                if Taboo:
                                                    ch_r "Not here,[R_Petname]!"
                                                else:
                                                    ch_r "Not with you around,[R_Petname]!"
                                                jump Rogue_Modded_Clothes_Menu
                                            "She slips off her [R_Panties]."
                                            $ R_Panties  = 0
                                            call Rogue_First_Bottomless
                                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2)  #fix add regular check    
                                            jump Rogue_Modded_Clothes_Legs
                                        
                                "Never mind.":
                                            ch_r "Ok. . ."  
                                            jump Rogue_Modded_Clothes_Legs
                                            
                        else:                                                       #she's wearing legs
                            if not ApprovalCheck("Rogue", 700, TabM=3): #700+1200
                                ch_r "I'm not really comfortable with that right now. . ."
                                jump Rogue_Modded_Clothes_Legs                    
                            elif ApprovalCheck("Rogue", 800, "L", TabM=3):               
                                ch_r "Well aren't you cheeky. . ."
                            elif ApprovalCheck("Rogue", 500, "O", TabM=3): #500+400
                                ch_r "Fine by me."
                            elif ApprovalCheck("Rogue", 350, "I", TabM=3):
                                ch_r "Oooh, naughty."
                            else:
                                ch_r "Oh, I guess I could."  
                                
                        $ R_Panties  = 0   
                        "She pulls her shorts off."
                                
        "Never mind":
            pass
    jump Rogue_Modded_Clothes_Menu
    #End of Rogue Pants
        
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
        
    menu Rogue_Modded_Clothes_Under: 
        "Tops and bras":
            menu Rogue_Modded_Clothes_Under_Top:
                                                                                                            # Tops    
                "How about you lose the [R_Chest]?" if R_Chest and "swimsuit" not in R_Chest:
                        call RogueFace("bemused", 1)
                        if R_BodySuit:
                            ch_r "Sure."
                        elif R_SeenChest and ApprovalCheck("Rogue", 1100, TabM=2):
                            ch_r "Sure."    
                        elif ApprovalCheck("Rogue", 1100, TabM=2):
                            ch_r "I guess I don't really mind if you see them. . ."
                        elif R_Over == "hoodie" and ApprovalCheck("Rogue", 500, TabM=2):
                            ch_r "I guess this covers enough. . ."
                        elif R_Over == "modded blue hoodie" and ApprovalCheck("Rogue", 500, TabM=2):
                            ch_r "I guess this covers enough. . ."
                        elif R_Over == "modded red hoodie" and ApprovalCheck("Rogue", 500, TabM=2):
                            ch_r "I guess this covers enough. . ."
                        elif R_Over == "modded yellow hoodie" and ApprovalCheck("Rogue", 500, TabM=2):
                            ch_r "I guess this covers enough. . ."
                        elif R_Over == "modded black hoodie" and ApprovalCheck("Rogue", 500, TabM=2):
                            ch_r "I guess this covers enough. . ."
                        elif R_Over == "modded white hoodie" and ApprovalCheck("Rogue", 500, TabM=2):
                            ch_r "I guess this covers enough. . ."      
                        elif R_Over == "pink top" and ApprovalCheck("Rogue", 950, TabM=2):
                            ch_r "This look is a bit revealing. . ."  
                            call Rogue_First_Topless
                        elif R_Over == "modded red top" and ApprovalCheck("Rogue", 950, TabM=2):
                            ch_r "This look is a bit revealing. . ."  
                            call Rogue_First_Topless
                        elif R_Over == "modded classic jacket":
                            ch_r "In this top? That ould leave nothing to the imagination!" 
                            jump Rogue_Modded_Clothes_Under_Top
                        elif R_Over == "mesh top":
                            ch_r "In this top? That would leave nothing to the imagination!" 
                            jump Rogue_Modded_Clothes_Under_Top
                        elif R_Over == "modded SR7 mesh top":
                            ch_r "In this top? That would leave nothing to the imagination!" 
                            jump Rogue_Modded_Clothes_Under_Top
                        elif R_Over == "modded white mesh top":
                            ch_r "In this top? That would leave nothing to the imagination!" 
                            jump Rogue_Modded_Clothes_Under_Top
                        elif R_Over == "modded red mesh top":
                            ch_r "In this top? That would leave nothing to the imagination!" 
                            jump Rogue_Modded_Clothes_Under_Top
                        elif R_Over == "modded yellow mesh top":
                            ch_r "In this top? That would leave nothing to the imagination!" 
                            jump Rogue_Modded_Clothes_Under_Top
                        elif R_Over == "modded black mesh top":
                            ch_r "In this top? That would leave nothing to the imagination!" 
                            jump Rogue_Modded_Clothes_Under_Top
                        elif R_Over == "modded blue mesh top":
                            ch_r "In this top? That would leave nothing to the imagination!" 
                            jump Rogue_Modded_Clothes_Under_Top
                        elif not R_Over:
                            ch_r "Not without a little coverage, for modesty."
                            jump Rogue_Modded_Clothes_Under_Top                            
                        else:
                            ch_r "I don't think so, [R_Petname]."
                            jump Rogue_Modded_Clothes_Under_Top 
                        $ R_Chest = 0
                        jump Rogue_Modded_Clothes_Under_Top 

                "Try on that cheerleader top." if R_Chest != "modded cheerleader":
                                # call Rogue_Swimsuit_Change_Top
                                call SetChestRogue("modded cheerleader")
                                jump Rogue_Modded_Clothes_Under_Top
                    
                "Try on that black tank top." if R_Chest != "tank":
                                # call Rogue_Swimsuit_Change_Top
                                $ R_Chest = "tank"
                                jump Rogue_Modded_Clothes_Under_Top
        
                "Try on that short black tank top." if R_Chest != "modded tank short":
                                # call Rogue_Swimsuit_Change_Top
                                call SetChestRogue("modded tank short")
                                jump Rogue_Modded_Clothes_Under_Top

                "Try on that SR7 black tank top." if R_Chest != "modded SR7 tank short":
                                # call Rogue_Swimsuit_Change_Top
                                call SetChestRogue("modded SR7 tank short")
                                jump Rogue_Modded_Clothes_Under_Top

                "Try on that short black slut tank top." if R_Chest != "modded slut tank short":
                                # call Rogue_Swimsuit_Change_Top
                                call SetChestRogue("modded slut tank short")
                                jump Rogue_Modded_Clothes_Under_Top

                "Try on that green crop top." if R_Chest != "modded green crop top":
                                # call Rogue_Swimsuit_Change_Top
                                call SetChestRogue("modded green crop top")
                                jump Rogue_Modded_Clothes_Under_Top

                "Try on that black crop top." if R_Chest != "modded black crop top":
                                # call Rogue_Swimsuit_Change_Top
                                call SetChestRogue("modded black crop top")
                                jump Rogue_Modded_Clothes_Under_Top

                "I like that buttoned tank top." if (R_Chest != "buttoned tank" and R_Over != "mesh top") or (R_Chest != "buttoned tank" and R_Over != "modded white mesh top") or (R_Chest != "buttoned tank" and R_Over != "modded blue mesh top") or (R_Chest != "buttoned tank" and R_Over != "modded yellow mesh top") or (R_Chest != "buttoned tank" and R_Over != "modded red mesh top") or (R_Chest != "buttoned tank" and R_Over != "modded black mesh top") or (R_Chest != "buttoned tank" and R_Over != "modded SR7 mesh top"):
                                # call Rogue_Swimsuit_Change_Top
                                call SetChestRogue("buttoned tank")
                                jump Rogue_Modded_Clothes_Under_Top
                    
                "I like your sport bras.":
                        if (R_SeenChest and ApprovalCheck("Rogue", 600)) or ApprovalCheck("Rogue", 900, TabM=2) or R_BodySuit:
                            # call Rogue_Swimsuit_Change_Top
                            menu:
                                ch_r "Oh? Which color suits your fancy then?"
                                "Green looks nice on you." if R_Chest != "sports bra":
                                    ch_r "Sure."
                                    call SetChestRogue("sports bra")
                                "I like the red one." if R_Chest != "modded red sports bra":
                                    ch_r "Sure."
                                    call SetChestRogue("modded red sports bra")
                                "The blue one suits you." if R_Chest != "modded blue sports bra":
                                    ch_r "Sure."   
                                    call SetChestRogue("modded blue sports bra")
                        else:
                            ch_r "I don't know about wearing it with this. . ." 
                        jump Rogue_Modded_Clothes_Under_Top

                "I like that black bra." if R_Chest != "bra":
                        if (R_SeenChest and ApprovalCheck("Rogue", 600)) or ApprovalCheck("Rogue", 1100, TabM=2) or R_BodySuit:
                            # call Rogue_Swimsuit_Change_Top
                            ch_r "Sure."   
                            call SetChestRogue("bra")
                        else:                
                            ch_r "That's a bit too revealing. . ."  
                        jump Rogue_Modded_Clothes_Under_Top

                "I like that lace bra." if "lace bra" in R_Inventory and R_Chest != "lace bra":
                        if (R_SeenChest and ApprovalCheck("Rogue", 800)) or ApprovalCheck("Rogue", 1100, TabM=2):
                            # call Rogue_Swimsuit_Change_Top
                            ch_r "Sure."   
                            call SetChestRogue("lace bra")
                        else:                
                            ch_r "That's a bit too revealing. . ." 
                        jump Rogue_Modded_Clothes_Under_Top

                "Just put some tape on your nipples." if R_Chest != "modded tape":
                        if (R_SeenChest and ApprovalCheck("Rogue", 1000)) or ApprovalCheck("Rogue", 1200, TabM=2):
                            # call Rogue_Swimsuit_Change_Top
                            ch_r "Sure."   
                            call SetChestRogue("modded tape")
                        else:                
                            ch_r "That's too revealing. . ." 
                        jump Rogue_Modded_Clothes_Under_Top

                "Nevermind.":
                        jump Rogue_Modded_Clothes_Under

        "Panties":
            menu Rogue_Modded_Clothes_Under_Panties:

                "You could lose those panties. . ." if R_Panties and (R_Panties != "shorts" or R_Panties != "modded red shorts" or R_Panties != "modded blue shorts") and "swimsuit" not in R_Panties:
                                call RogueFace("bemused", 1)
                                if (R_SeenPussy and ApprovalCheck("Rogue", 900) or R_BodySuit) and not Taboo: # You've seen her pussy
                                    if ApprovalCheck("Rogue", 850, "L", TabM=2):               
                                        ch_r "Well aren't you cheeky. . ."
                                    elif ApprovalCheck("Rogue", 500, "O", TabM=2):
                                        ch_r "Fine by me."
                                    elif ApprovalCheck("Rogue", 350, "I", TabM=2):
                                        ch_r "Oooh, naughty."                            
                                    else:
                                        ch_r "Oh, I guess I could."         
                                else:                       #You've never seen it
                                    if ApprovalCheck("Rogue", 1100, "LI", TabM=2):               
                                        ch_r "Well aren't you cheeky. . . I suppose I could give you a show. . ."
                                    elif ApprovalCheck("Rogue", 750, "OI", TabM=2):
                                        ch_r "If that's what you want."
                                    elif ApprovalCheck("Rogue", 500, "I", TabM=2):
                                        ch_r "Oooh, naughty."
                                    elif ApprovalCheck("Rogue", 1400, TabM=3):
                                        ch_r "Oh, fine. You've been a good boy."
                                    else: 
                                        call RogueFace("surprised")
                                        $ R_Brows = "angry"
                                        ch_r "Not with you around,[R_Petname]!"
                                        jump Rogue_Modded_Clothes_Menu 
                                
                                $ R_Panties = 0  
                                if (not R_Legs or (R_Legs == "modded skirtshort" or R_Legs == "modded SR7 skirtshort" or R_Legs == "modded cheerleader skirtshort")) and not R_BodySuit:
                                    call Rogue_First_Bottomless
                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2)  
                                jump Rogue_Modded_Clothes_Under_Panties
                                    
                "Why don't you wear the green panties instead?" if R_Panties and R_Panties != "green panties":
                                if ApprovalCheck("Rogue", 1000, TabM=3):
                                    # call Rogue_Swimsuit_Change_Bottom
                                    ch_r "Sure, ok."
                                    call SetPantiesRogue("green panties")
                                elif (R_Panties == "shorts" or R_Panties == "modded red shorts" or R_Panties == "modded blue shorts"):
                                    ch_r "Heh, no, I think I'll stick with these, thanks."
                                else:
                                    ch_r "I think I'll choose my own underwear, thank you."
        
                "Why don't you wear the black large panties instead?" if R_Panties and R_Panties != "modded black large panties":
                                if ApprovalCheck("Rogue", 1000, TabM=3):
                                    # call Rogue_Swimsuit_Change_Bottom
                                    ch_r "Sure, ok."
                                    call SetPantiesRogue("modded black large panties")
                                elif (R_Panties == "shorts" or R_Panties == "modded red shorts" or R_Panties == "modded blue shorts"):
                                    ch_r "Heh, no, I think I'll stick with these, thanks."
                                else:
                                    ch_r "I think I'll choose my own underwear, thank you."
                                jump Rogue_Modded_Clothes_Under_Panties

                        
                "Why don't you wear the black panties instead?" if R_Panties and R_Panties != "black panties":
                                if ApprovalCheck("Rogue", 1100, TabM=3):
                                    # call Rogue_Swimsuit_Change_Bottom
                                    ch_r "Sure."
                                    call SetPantiesRogue("black panties")
                                elif (R_Panties == "shorts" or R_Panties == "modded red shorts" or R_Panties == "modded blue shorts"):
                                    ch_r "Heh, no, I think I'll stick with these, thanks."
                                else:
                                    ch_r "I don't see how that's any business of yours, [R_Petname]."
                                jump Rogue_Modded_Clothes_Under_Panties

                                    
                "Why don't you wear the lace panties instead?" if "lace panties" in R_Inventory and R_Panties and R_Panties != "lace panties":
                                if ApprovalCheck("Rogue", 1200, TabM=3):
                                    # call Rogue_Swimsuit_Change_Bottom
                                    ch_r "Sure."
                                    call SetPantiesRogue("lace panties")
                                elif (R_Panties == "shorts" or R_Panties == "modded red shorts" or R_Panties == "modded blue shorts"):
                                    ch_r "Heh, no, I think I'll stick with these, thanks."
                                else:
                                    ch_r "I don't see how that's any business of yours, [R_Petname]."
                                jump Rogue_Modded_Clothes_Under_Panties
        
                "You know, you could wear some panties with that. . ." if not R_Panties:
                                call RogueFace("bemused", 1)
                                if (R_Love+R_Obed) <= (1.5* R_Inbt):
                                    $ R_Mouth = "smile"
                                    ch_r "No thanks, [R_Petname]."
                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2)
                                    menu:
                                        "Wear them":
                                            pass
                                        "Ok":
                                            jump Rogue_Modded_Clothes_Menu
                                # call Rogue_Swimsuit_Change_Bottom
                                ch_r "Well, I suppose you're right. . ."
                                menu:
                                    extend ""
                                    "How about the green ones?":
                                        ch_r "Sure, ok."
                                        call SetPantiesRogue("green panties")
                                    "How about the black large ones?":
                                        ch_r "Sure, ok."
                                        call SetPantiesRogue("modded black large panties")
                                    "How about the black ones?":
                                        ch_r "Alright."                
                                        call SetPantiesRogue("black panties")
                                    "How about the lace ones?" if "lace panties" in R_Inventory:
                                        ch_r "Alright."                
                                        call SetPantiesRogue("lace panties")
                                jump Rogue_Modded_Clothes_Under_Panties

                "Nevermind.":
                        jump Rogue_Modded_Clothes_Under

        "Hoses and stockings":
            menu Rogue_Modded_Clothes_Under_Hoses:
        
                "The thigh-high hose would look good with that." if R_Hose != "stockings" and R_Legs != "pants":     
                                $ R_Hose = "stockings"  
                                jump Rogue_Modded_Clothes_Under_Hoses
                "The pantyhose would look good with that." if R_Hose != "pantyhose" and R_Legs != "pants":     
                                $ R_Hose = "pantyhose" 
                                jump Rogue_Modded_Clothes_Under_Hoses
                "The stockings would look good with that." if R_Hose != "stockings and garterbelt" and "stockings and garterbelt" in R_Inventory and R_Legs != "pants":     
                                $ R_Hose = "stockings and garterbelt"  
                                jump Rogue_Modded_Clothes_Under_Hoses
                "Your ripped pantyhose would look good with that." if R_Hose != "ripped pantyhose" and "ripped pantyhose" in R_Inventory and R_Legs != "pants":     
                                $ R_Hose = "ripped pantyhose"                
                                jump Rogue_Modded_Clothes_Under_Hoses
                "You could use that fishnet" if R_Hose != "modded fishnet" and R_Legs != "pants":
                                call SetHoseRogue("modded fishnet")
                                jump Rogue_Modded_Clothes_Under_Hoses

                "You could use that SR7 hose" if R_Hose != "modded SR7 hose" and R_Legs != "pants":
                                call SetHoseRogue("modded SR7 hose")
                                jump Rogue_Modded_Clothes_Under_Hoses
        
                "You could lose the hose." if R_Hose and R_Hose != 'ripped tights' and R_Hose != 'tights':     
                                $ R_Hose = 0 
                                jump Rogue_Modded_Clothes_Under_Hoses

                "Nevermind.":
                        jump Rogue_Modded_Clothes_Under 

        # "Swimsuits":

        #     menu Rogue_Modded_Clothes_Under_SwimSuits:

        #         "Why don't you wear the swimsuit1" if R_BodySuit != "swimsuit1":
        #                         if ApprovalCheck("Rogue", 800, TabM=3):
        #                             ch_r "Sure."
        #                             $ R_BodySuit = "swimsuit1"
        #                             # call SetChestRogue("swimsuit1")
        #                         # elif (R_Panties == "shorts" or R_Panties == "modded red shorts" or R_Panties == "modded blue shorts"):
        #                         #     ch_r "Heh, no, I think I'll stick with these, thanks."
        #                         else:
        #                             ch_r "I don't see how that's any business of yours, [R_Petname]."
        #                         jump Rogue_Modded_Clothes_Under_SwimSuits
        
        #         "Why don't you wear the swimsuit2" if R_BodySuit != "swimsuit2":
        #                         if ApprovalCheck("Rogue", 1200, TabM=3):
        #                             ch_r "Sure."
        #                             $ R_BodySuit = "swimsuit2"
        #                             # call SetChestRogue("swimsuit2")
        #                         # elif (R_Panties == "shorts" or R_Panties == "modded red shorts" or R_Panties == "modded blue shorts"):
        #                         #     ch_r "Heh, no, I think I'll stick with these, thanks."
        #                         else:
        #                             ch_r "I don't see how that's any business of yours, [R_Petname]."
        #                         jump Rogue_Modded_Clothes_Under_SwimSuits

        #         "Remove the swimsuit" if R_BodySuit == "swimsuit2" or R_BodySuit == "swimsuit1":
        #                         $ R_BodySuit = 0
        #                         jump Rogue_Modded_Clothes_Under_SwimSuits

        #         "Nevermind.":
        #                 jump Rogue_Modded_Clothes_Under 
        
        
        "Never mind":
                        pass
    jump Rogue_Modded_Clothes_Menu
    #End of Rogue Underwear
    
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
        
    menu Rogue_Modded_Clothes_BodySuits: 
        "BodySuits":
            menu Rogue_Modded_Clothes_BodySuits_Body:

                "You could lose that bodysuit. . ." if R_BodySuit:
                                call RogueFace("bemused", 1)
                                if (not R_Panties and R_SeenPussy and ApprovalCheck("Rogue", 900)) and not Taboo: # You've seen her pussy
                                    if ApprovalCheck("Rogue", 850, "L", TabM=2):               
                                        ch_r "Well aren't you cheeky. . ."
                                    elif ApprovalCheck("Rogue", 500, "O", TabM=2):
                                        ch_r "Fine by me."
                                    elif ApprovalCheck("Rogue", 350, "I", TabM=2):
                                        ch_r "Oooh, naughty."                            
                                    else:
                                        ch_r "Oh, I guess I could."  
                                elif R_Panties and R_Chest:
                                    ch_r "Oh, I guess I could." 
                                else:
                                    if ApprovalCheck("Rogue", 1100, "LI", TabM=2):               
                                        ch_r "Well aren't you cheeky. . . I suppose I could give you a show. . ."
                                    elif ApprovalCheck("Rogue", 750, "OI", TabM=2):
                                        ch_r "If that's what you want."
                                    elif ApprovalCheck("Rogue", 500, "I", TabM=2):
                                        ch_r "Oooh, naughty."
                                    elif ApprovalCheck("Rogue", 1400, TabM=3):
                                        ch_r "Oh, fine. You've been a good boy."
                                    else: 
                                        $ R_Eyes = "surprised"
                                        $ R_Blush = 2
                                        ch_r "I'm not exactly decent under this, you know."
                                        jump Rogue_Modded_Clothes_Menu 
                                
                                $ R_BodySuit = 0  
                                if not R_Over and not R_Chest:
                                    call Rogue_First_Topless
                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2)  
                                if (not R_Legs or (R_Legs == "modded skirtshort" or R_Legs == "modded SR7 skirtshort" or R_Legs == "modded cheerleader skirtshort")) and not R_Panties:
                                    call Rogue_First_Bottomless
                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2)  
                                jump Rogue_Modded_Clothes_BodySuits_Body
                                    
                "Wear your classic uniform?" if R_BodySuit != "classic uniform":
                                ch_r "Sure, ok."
                                # call SetPantiesRogue("bodysuit")
                                # call SetChestRogue("bodysuit")
                                $ R_BodySuit = "classic uniform"  
        
                        
                "You know, you could wear some panties with that. . ." if not R_Panties:
                                call RogueFace("bemused", 1)
                                if (R_Love+R_Obed) <= (1.5* R_Inbt):
                                    $ R_Mouth = "smile"
                                    ch_r "No thanks, [R_Petname]."
                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2)
                                    menu:
                                        "Wear them":
                                            pass
                                        "Ok":
                                            jump Rogue_Modded_Clothes_Menu
                                # call Rogue_Swimsuit_Change_Bottom
                                ch_r "Well, I suppose you're right. . ."
                                menu:
                                    extend ""
                                    "How about the green ones?":
                                        ch_r "Sure, ok."
                                        call SetPantiesRogue("green panties")
                                    "How about the black large ones?":
                                        ch_r "Sure, ok."
                                        call SetPantiesRogue("modded black large panties")
                                    "How about the black ones?":
                                        ch_r "Alright."                
                                        call SetPantiesRogue("black panties")
                                    "How about the lace ones?" if "lace panties" in R_Inventory:
                                        ch_r "Alright."                
                                        call SetPantiesRogue("lace panties")
                                jump Rogue_Modded_Clothes_BodySuits_Body

                "Nevermind.":
                        jump Rogue_Modded_Clothes_BodySuits

        "Never mind":
                        pass
    jump Rogue_Modded_Clothes_Menu
    #End of Rogue Underwear
    
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


            
    menu Rogue_Modded_Clothes_Misc:   
        # "Put on that headband of yours." if R_Headband != "classic headband":
        #                 $ R_Headband = "classic headband"
        # "Take off that headband." if R_Headband:
        #                 $ R_Headband = 0

        # "Put on that utility belt." if R_Accessory != "classic belt":
        #                 $ R_Accessory = "classic belt"
        # "Take off that [R_Accessory]." if R_Accessory:
        #                 $ R_Accessory = 0
        #                                                                                                                                  #Misc
        # "Throw the gloves on." if R_Arms != "gloved":
        #                 $ R_Arms = "gloved"
        # "Throw the yellow gloves on." if R_Arms != "classic gloves":
        #                 $ R_Arms = "classic gloves"
        # "Take a little risk, no gloves." if R_Arms:
        #                 $ R_Arms = 0
                        
        # "I like that spiked collar." if R_Neck != "spiked collar":
        #                 $ R_Neck = "spiked collar"
        # "You could lose that spiked collar." if R_Neck == "spiked collar":
        #                 $ R_Neck = 0

        # "I like those glasses." if not R_Glasses:
        #                 $ R_Glasses = "glasses"
        # "You could lose those glasses." if R_Glasses:
        #                 $ R_Glasses = 0

        # "Wear those black boots." if R_Boots != "boots":
        #                 $ R_Boots = "boots"
        # "Wear those boots from the classic uniform" if R_Boots != "classic boots":
        #                 $ R_Boots = "classic boots"

        # "You could lose those boots." if R_Boots:
        #                 $ R_Boots = 0

        "Dye your hair.":
            if ApprovalCheck("Rogue", 800):
                ch_r "Which color?"

                menu:
                    "Black" if R_HairColor != "black":
                        ch_r "Like this?"
                        call SetHairColorRogue("black")

                    "Black with white streak" if R_HairColor != "blackwhite":
                        ch_r "Like this?"
                        call SetHairColorRogue("blackwhite")

                    "Blonde" if R_HairColor != "blonde":
                        ch_r "Like this?"
                        call SetHairColorRogue("blonde")

                    "Blonde with white streak" if R_HairColor != "blondewhite":
                        ch_r "Like this?"
                        call SetHairColorRogue("blondewhite")

                    "Let me select the color.":
                        ch_k "You think so?"
                        call Recolor_Hair("Rogue")
                        call SetHairColorRogue("custom")

                #ch_r "You think so?"
                #"She rummages in her bag and grabs some gel, running it through her hair."
            else:
                ch_r "It's too high maintenance."

        "Change the color of you hair back." if R_HairColor:
            if ApprovalCheck("Rogue", 800):
                ch_r "You think so?"
                #"She rummages in her bag and grabs some gel, running it through her hair."
                ch_r "Like this?"
                call SetHairColorRogue("")
            else:
                ch_r "It's too high maintenance."

        "You know, I like some nice hair down there. Maybe grow it out." if not R_Pubes and "pubes" in R_Todo:
                        call RogueFace("bemused", 1)
                        ch_r "Yeah, I know, [R_Petname]. It doesn't grow out overnight!"
        "You know, I like some nice hair down there. Maybe grow it out." if not R_Pubes:
                        call RogueFace("bemused", 1)
                        $ Approval = ApprovalCheck("Rogue", 1150, TabM=0)
                        
                        if ApprovalCheck("Rogue", 850, "L", TabM=0) or (Approval and R_Love > R_Obed):               
                            ch_r "Well. . . if that's how you like it. . ."
                        elif ApprovalCheck("Rogue", 500, "O", TabM=0) or (Approval and R_Obed > R_Inbt):
                            ch_r "If that's what you want."
                        elif ApprovalCheck("Rogue", 500, "I", TabM=0) or Approval:
                            ch_r "Heh, I like a man knows what he wants, [R_Petname]."
                        else: 
                            call RogueFace("surprised")
                            $ R_Brows = "angry"
                            ch_r "Well I don't see how that's any of your business, [R_Petname]."
                            jump Rogue_Modded_Clothes_Menu
                        $ R_Todo.append("pubes")
                        $ R_PubeC = 6
        
        "I like it waxed clean down there." if R_Pubes == 1:
                        call RogueFace("bemused", 1)
                        if "shave" in R_Todo:
                            ch_r "I know, I'll get on that. Not right this second, obviously."
                        else:
                            $ Approval = ApprovalCheck("Rogue", 1150, TabM=0)
                            if ApprovalCheck("Rogue", 850, "L", TabM=0) or (Approval and R_Love > R_Obed):             
                                ch_r "I can keep it tidy if you like. . ."
                            elif ApprovalCheck("Rogue", 500, "O", TabM=0) or (Approval and R_Obed > R_Inbt):
                                ch_r "I'll take care of it."
                            elif ApprovalCheck("Rogue", 500, "I", TabM=0) or Approval:
                                ch_r "You better earn it, [R_Petname]."
                            else: 
                                call RogueFace("surprised")
                                $ R_Brows = "angry"
                                ch_r "I don't see how that's any of your beeswax, [R_Petname]."
                                jump Rogue_Modded_Clothes_Menu
                            $ R_Todo.append("shave")        
        "Piercings. [[See what she looks like without them first] (locked)" if not R_SeenPussy and not R_SeenChest:
                        pass
            
        "You know, you'd look really nice with some ring body piercings." if R_Pierce != "ring" and (R_SeenPussy or R_SeenChest) and "ring" not in R_Todo:
                        call RogueFace("bemused", 1)
                        $ Approval = ApprovalCheck("Rogue", 1350, TabM=0)
                        if ApprovalCheck("Rogue", 950, "L", TabM=0) or (Approval and R_Love > R_Obed):   
                            ch_r "You really like those? Well, I suppose. . ."
                        elif ApprovalCheck("Rogue", 600, "O", TabM=0) or (Approval and R_Obed > R_Inbt):
                            ch_r "I'll go get that taken care of."
                        elif ApprovalCheck("Rogue", 600, "I", TabM=0) or Approval:
                            ch_r "I've always kind of liked the look of those. . ."
                        else: 
                            call RogueFace("surprised")
                            $ R_Brows = "angry"
                            ch_r "I don't see how that's any of your beeswax, [R_Petname]."
                            jump Rogue_Modded_Clothes_Menu           
                        $ R_Todo.append("ring")
        
        "You know, you'd look really nice with some barbell body piercings." if R_Pierce != "barbell" and (R_SeenPussy or R_SeenChest)and "barbell" not in R_Todo:
                        call RogueFace("bemused", 1)
                        $ Approval = ApprovalCheck("Rogue", 1350, TabM=0)
                        if ApprovalCheck("Rogue", 900, "L", TabM=0) or (Approval and R_Love > R_Obed):   
                            ch_r "You really like those? Well, I suppose. . ."
                        elif ApprovalCheck("Rogue", 600, "O", TabM=0) or (Approval and R_Obed > R_Inbt):
                            ch_r "I'll go get that taken care of."
                        elif ApprovalCheck("Rogue", 600, "I", TabM=0) or Approval:
                            ch_r "I've always kind of liked the look of those. . ."
                        else: 
                            call RogueFace("surprised")
                            $ R_Brows = "angry"
                            ch_r "I don't see how that's any of your beeswax, [R_Petname]."
                            jump Rogue_Modded_Clothes_Menu               
                        $ R_Todo.append("barbell")
                        $ R_Pierce = "barbell"
                        
        "You know, you'd look better without those piercings." if R_Pierce:
                        call RogueFace("bemused", 1)
                        $ Approval = ApprovalCheck("Rogue", 1350, TabM=0)
                        if ApprovalCheck("Rogue", 950, "L", TabM=0) or (Approval and R_Love > R_Obed):   
                            ch_r "You really think so? I guess I could lose them. . ."
                        elif ApprovalCheck("Rogue", 600, "O", TabM=0) or (Approval and R_Obed > R_Inbt):
                            ch_r "I'll take them out then."
                        elif ApprovalCheck("Rogue", 600, "I", TabM=0) or Approval:
                            ch_r "I guess I prefered not having them in. . ."                
                        else: 
                            call RogueFace("surprised")
                            $ R_Brows = "angry"
                            ch_r "I'll keep them, if you don't mind."
                            jump Rogue_Modded_Clothes_Menu           
                        $ R_Pierce = 0 
                        
        "Never mind":
            pass      
    jump Rogue_Modded_Clothes_Menu
    #End of Rogue Misc Wardrobe
    
    return

label SetChestRogue(Outfit = "modded tape"):
    $ R_Chest = Outfit
    call Mod_Update_Rogue_Image
    return

label SetOverRogue(Outfit = "modded white mesh top"):
    $ R_Over = Outfit
    call Mod_Update_Rogue_Image
    return

label SetLegsRogue(Outfit = "modded black large panties"):
    $ R_Legs = Outfit
    call Mod_Update_Rogue_Image
    return

label SetPantiesRogue(Outfit = "modded black large panties"):
    $ R_Panties = Outfit
    call Mod_Update_Rogue_Image
    return

label SetHoseRogue(Outfit = "modded fishnet"):
    $ R_Hose = Outfit
    call Mod_Update_Rogue_Image
    return

label SetHairColorRogue(Outfit = ""):
    $ R_HairColor = Outfit
    call Mod_Update_Rogue_Image
    return

label Mod_Update_Rogue_Image:
    if renpy.showing("Rogue"):
        show Rogue 
    elif renpy.showing("Rogue_Doggy"):
        show Rogue_Doggy 
    elif renpy.showing("Rogue_SexSprite"):
        show Rogue_SexSprite   
    elif renpy.showing("Rogue_BJ_Animation"):
        show Rogue_BJ_Animation   
    elif renpy.showing("Rogue_HJ_Animation"):
        show Rogue_HJ_Animation   
    elif renpy.showing("Rogue_TJ_Animation"):
        show Rogue_TJ_Animation   
    return
    
init python:
    def ModPantsNum(Chr = "Rogue"): 
                #This function determines how much pants are on, 10 for pants, 5 for skirt, <5 for less.
                if Chr == "Rogue":
                        # if R_Upskirt and R_Legs:
                        #     return 1"modded SR7 skirtshort" or R_Legs == "modded cheerleader skirtshort"
                        if R_Legs == "modded skirtshort":
                            return 5
                        elif R_Legs == "modded SR7 skirtshort":
                            return 5
                        elif R_Legs == "modded cheerleader skirtshort":
                            return 5
                        elif R_Legs == "modded cheerleader skirt":
                            return 5
                        # elif R_Panties == "shorts":
                        #     return 6
                        else:
                            return 0
                elif Chr == "Kitty":
                        # if K_Upskirt and K_Legs:
                        #     return 1
                        if K_Legs == "modded orange skirt":
                            return 5            
                        elif K_Legs == "modded black skirt":
                            return 5    
                        elif K_Legs == "modded white skirt":
                            return 5                    
                        # elif K_Legs == "shorts":
                        #     return 6       
                        # elif K_Legs == "blue skirt":
                        #     return 5
                        else:
                            return 0
                elif Chr == "Emma":
                        # if E_Upskirt and E_Legs:
                        #     return 1
                        if E_Legs == "modded black pants":
                            return 10 
                        elif E_Legs == "modded NewX":
                            return 6 
                        elif E_Legs == "modded NewX black":
                            return 6 
                        elif E_Legs == "modded white sports shorts":
                            return 6 
                        elif E_Legs == "modded red sports shorts":
                            return 6 
                        else:
                            return 0  
                elif Chr == "Laura":
                        # if L_Upskirt and L_Legs:
                        #     return 1
                        if L_Legs == "leather pants":
                            return 10        
                        elif L_Legs == "skirt":
                            return 5   
                        elif L_Legs == "mesh pants":
                            return 2        
                        else:
                            return 0

                elif Chr in ModdedGirls:
                        if newgirl[Chr].Legs == "pants":
                            return 10
                        if newgirl[Chr].Legs == "workout pants":
                            return 10
                        elif newgirl[Chr].Legs == "skirt":
                            return 3
                        elif newgirl[Chr].Legs == "black skirt":
                            return 3
                        elif newgirl[Chr].Legs == "split skirt":
                            return 3
                        else:
                            return 0
                            
                #if it falls though. . .
                return 0 

    def ModHoseNum(Chr = "Rogue"): 
            #This function determines how seethrough her hose is, 5 for "visible," 10 for "solid"
                # if Chr == "Rogue":
                #             if R_Hose == "stockings":
                #                 return 1
                #             elif R_Hose == "pantyhose":
                #                 return 6
                #             elif R_Hose == "tights":
                #                 return 10
                #             elif R_Hose == "ripped pantyhose":
                #                 return 5
                #             elif R_Hose == "ripped tights":
                #                 return 5
                #             elif R_Hose == "fishnet":
                #                 return 1
                #             elif R_Hose == "SR7 hose":
                #                 return 1
                #             else:
                #                 return 0
                                
                # elif Chr == "Kitty":
                #             if K_Hose == "stockings":
                #                 return 1
                #             else:
                #                 return 0
                # elif Chr == "Emma":
                #             if E_Hose == "stockings":
                #                 return 1
                #             else:
                #                 return 0
                if Chr in ModdedGirls:
                            if newgirl[Chr].Hose == "stockings":
                                return 1
                            else:
                                return 0
                                
                #if it falls though. . .        
                return 0 

    def IsOutfitModdedRogue(Type = "Over"):
        if Type == "Over":
            if R_Over:
                if "modded" in R_Over:
                    return 1
            else:
                return 0
        if Type == "Chest":
            if R_Chest:
                if "modded" in R_Chest:
                    return 1
            else:
                return 0
        if Type == "Legs":
            if R_Legs:
                if "modded" in R_Legs:
                    return 1
            else:
                return 0
        if Type == "Panties":
            if R_Panties:
                if "modded" in R_Panties:
                    return 1
            else:
                return 0
        return 0

    def Mod_Rogue_OutfitShame(Type = "Chest"):                                                                             #sets custom outfit    
  
        if Type == "Chest":
            # if R_Chest == "tank":                                              
            #     $ Count = 20
            # elif R_BodySuit == "classic uniform":
            #     $ Count = 20 
            # elif R_BodySuit == "swimsuit1":
            #     $ Count = 20
            # elif R_BodySuit == "swimsuit2":
            #     $ Count = 10
            if R_Chest == "modded cheerleader":
                return 20
            elif R_Chest == "modded slut tank short":                                              
                return -5
            elif R_Chest == "modded SR7 tank short":                                              
                return 5
            elif R_Chest == "modded green crop top":                                              
                return 20
            elif R_Chest == "modded black crop top":                                              
                return 20
            elif R_Chest == "modded tape":                                              
                return 5
            elif R_Chest == "modded red sports bra":
                return 15
            elif R_Chest == "modded blue sports bra":
                return 15

        if Type == "Over":
            if R_Over == "modded red top":                                             
                return 15
            elif R_Over == "modded classic jacket":      
                return 5
            elif R_Over == "modded blue hoodie":      
                return 15
            elif R_Over == "modded red hoodie":      
                return 15
            elif R_Over == "modded yellow hoodie":      
                return 15
            elif R_Over == "modded black hoodie":      
                return 15
            elif R_Over == "modded white hoodie":      
                return 15 
            elif R_Over == "modded SR7 mesh top":      
                return 5
            elif R_Over == "modded white mesh top":      
                return 5
            elif R_Over == "modded blue mesh top":      
                return 5
            elif R_Over == "modded red mesh top":      
                return 5
            elif R_Over == "modded yellow mesh top":      
                return 5
            elif R_Over == "modded black mesh top":      
                return 5      
            elif R_Over == "modded red dress":      
                return 40  
            elif R_Over == "modded blue dress":      
                return 40  

        if Type == "Legs":
            # if R_BodySuit == "classic uniform":
            #     $ Count = 25
            # if R_Over == "blue dress":      
            #     $ Count = 20  
            # elif R_Over == "red dress":      
            #     $ Count = 20  
            if R_Legs == "skirtshort":            #If wearing a short skirt commando
                return 0
            elif R_Legs == "SR7 skirtshort":            #If wearing a short skirt commando
                return 0
            elif R_Legs == "cheerleader skirt":                 #If wearing a cheerleader skirt commando
                return 20
            elif R_Legs == "cheerleader skirtshort":            #If wearing a short cheerleader skirt commando
                return 0   
        

        if Type == "Panties":
                       
            if R_Panties == "red shorts":             #If wearing shorts
                return 25
            elif R_Panties == "blue shorts":             #If wearing shorts
                return 25  
            elif R_Panties == "black large panties":      #If wearing only green panties
                return 10
            # elif R_Panties == "swimsuit1":
            #     return 40
            # elif R_Panties == "swimsuit2":
            #     $ Count = 30
            # elif R_Panties:                         #If wearing only any other panties
            #     $ Count = 7
            # if R_BodySuit == "swimsuit1":
            #     $ Count += 10
            # elif R_BodySuit == "swimsuit2":
            #     $ Count += 5

        return 0    
    def GetModdedString(first = "images/RogueSprite/Rogue_panties_", second = "test", third = ".png"):
        if second:
            if "modded" in second:
                string = first + second + third
                # if renpy.showing("Rogue"):
                #     renpy.hide("Rogue")
                #     renpy.show("Rogue")
                # elif renpy.showing("Rogue_Doggy"):
                #     renpy.show("Rogue_Doggy")
                # elif renpy.showing("Rogue_SexSprite"):
                #     renpy.show("Rogue_SexSprite")
                # elif renpy.showing("Rogue_BJ_Animation"):
                #     renpy.show("Rogue_BJ_Animation")
                # elif renpy.showing("Rogue_HJ_Animation"):
                #     renpy.show("Rogue_HJ_Animation")
                # elif renpy.showing("Rogue_TJ_Animation"):
                #     renpy.show("Rogue_TJ_Animation")
                if not renpy.loadable(string):
                    # if not string in SomethingWrongDesu:
                    #     SomethingWrongDesu.append(string)
                    #     f = open("SomethingWrongDesu.txt")
                    #     f.write(string + "\n")
                    #     f.close()
                    #string2 = "something wrong loading " + string + ", warn the modders"
                    #renpy.call_in_new_context(narrator(string2))
                    #renpy.say(Character('???', color="#85bb65", image = "arrow", show_two_window=True), string2)
                    #renpy.say(ch_u,"something wrong loading [string], warn the modders")
                    string = Null()
            else:
                string = Null()
        else:
            string = Null()
        return string

    def GetOutfitString(first = "images/RogueSprite/Rogue_panties_", second = "test", third = ".png"):
        if second:
            string = first + second + third
            if not renpy.loadable(string):
                string = Null()
        else:
            string = Null()
        return string

    def GetModdedString2Kitty(first = "images/RogueSprite/Rogue_panties_", second = "3", third = ".png"):
        second_ = int(second)
        if K_DynamicTan[second_]:
            if "modded" in K_DynamicTan[second_]:
                string = first + K_DynamicTan[second_] + third
                # if renpy.showing("Rogue"):
                #     renpy.hide("Rogue")
                #     renpy.show("Rogue")
                # elif renpy.showing("Rogue_Doggy"):
                #     renpy.show("Rogue_Doggy")
                # elif renpy.showing("Rogue_SexSprite"):
                #     renpy.show("Rogue_SexSprite")
                # elif renpy.showing("Rogue_BJ_Animation"):
                #     renpy.show("Rogue_BJ_Animation")
                # elif renpy.showing("Rogue_HJ_Animation"):
                #     renpy.show("Rogue_HJ_Animation")
                # elif renpy.showing("Rogue_TJ_Animation"):
                #     renpy.show("Rogue_TJ_Animation")
                if not renpy.loadable(string):
                    # if not string in SomethingWrongDesu:
                    #     SomethingWrongDesu.append(string)
                    #     f = open("SomethingWrongDesu.txt")
                    #     f.write(string + "\n")
                    #     f.close()
                    #string2 = "something wrong loading " + string + ", warn the modders"
                    #renpy.call_in_new_context(narrator(string2))
                    #renpy.say(Character('???', color="#85bb65", image = "arrow", show_two_window=True), string2)
                    #renpy.say(ch_u,"something wrong loading [string], warn the modders")
                    string = Null()
            else:
                string = Null()
        else:
            string = Null()
        return string

    def GetModdedStringTanRogue(first = "3", second = ".png", third = "Sprite"):
        first_ = int(first)
        if R_DynamicTan[first_]:
            if first_ == 3: #chest
                if "modded" in R_DynamicTan[first_] or third == "Sex":
                    string = "images/Rogue" + str(third) + "/Rogue_" + str(third) + "_Chest_" + str(R_DynamicTan[first_]) + second
                    if not renpy.loadable(string):
                        string = "images/Rogue" + str(third) + "/Rogue_" + str(third) + "_Chest_" + str(R_DynamicTan[first_]) + ".png"
                        if not renpy.loadable(string):
                            string = Null()
                
                else:
                    string = "images/Rogue" + str(third) + "/RogueTan/Rogue_" + str(third) + "_Chest_tan " + str(R_DynamicTan[first_]) + second
                    if not renpy.loadable(string):
                        string = "images/Rogue" + str(third) + "/RogueTan/Rogue_" + str(third) + "_Chest_tan " + str(R_DynamicTan[first_]) + ".png"
                        if not renpy.loadable(string):
                            string = Null()

            elif first_ == 1: #over
                if "modded" in R_DynamicTan[first_] or third == "Sex":
                    string = "images/Rogue" + str(third) + "/Rogue_" + str(third) + "_Over_" + str(R_DynamicTan[first_]) + second
                    if not renpy.loadable(string):
                        string = "images/Rogue" + str(third) + "/Rogue_" + str(third) + "_Over_" + str(R_DynamicTan[first_]) + ".png"
                        if not renpy.loadable(string):
                            string = Null()
                
                else:
                    string = "images/Rogue" + str(third) + "/RogueTan/Rogue_" + str(third) + "_Over_tan " + str(R_DynamicTan[first_]) + second
                    if not renpy.loadable(string):
                        string = "images/Rogue" + str(third) + "/RogueTan/Rogue_" + str(third) + "_Over_tan " + str(R_DynamicTan[first_]) + ".png"
                        if not renpy.loadable(string):
                            string = Null()

            elif first_ == 4: #panties
                if "modded" in R_DynamicTan[first_] or third == "Sex":
                    string = "images/Rogue" + str(third) + "/Rogue_" + str(third) + "_Panties_" + str(R_DynamicTan[first_]) + second
                    if not renpy.loadable(string):
                        # string = "images/Rogue" + str(third) + "/Rogue_" + str(third) + "_Panties_" + str(R_DynamicTan[first_]) + ".png"
                        # if not renpy.loadable(string):
                            string = Null()
                
                else:
                    string = "images/Rogue" + str(third) + "/RogueTan/Rogue_" + str(third) + "_Panties_tan " + str(R_DynamicTan[first_]) + second
                    if not renpy.loadable(string):
                        # string = "images/Rogue" + str(third) + "/Rogue_" + str(third) + "_Panties_" + str(R_DynamicTan[first_]) + ".png"
                        # if not renpy.loadable(string):
                            string = Null()

            elif first_ == 2: #legs
                # if third == "SexFeet":
                #     if "modded" in R_DynamicTan[first_] or third == "Sex":
                #         string = "images/RogueSex/Rogue_Sex_Feet_" + str(R_DynamicTan[first_]) + second
                #         if not renpy.loadable(string):
                #                 string = Null()
                    
                #     else:
                #         string = "images/RogueSex/RogueTan/Rogue_Sex_Feet_tan " + str(R_DynamicTan[first_]) + second
                #         if not renpy.loadable(string):
                #                 string = Null()
                # else:
                    if "skirt" in R_DynamicTan[first_] and third == "Sex":
                        string = "images/Rogue" + str(third) + "/RogueTan/Rogue_" + str(third) + "_Legs_tan skirts.png"

                    elif "modded" in R_DynamicTan[first_] or third == "Sex":
                        string = "images/Rogue" + str(third) + "/Rogue_" + str(third) + "_Legs_" + str(R_DynamicTan[first_]) + second
                        if not renpy.loadable(string):
                            # string = "images/Rogue" + str(third) + "/Rogue_" + str(third) + "_Legs_" + str(R_DynamicTan[first_]) + ".png"
                            # if not renpy.loadable(string):
                                string = Null()
                    
                    else:
                        string = "images/Rogue" + str(third) + "/RogueTan/Rogue_" + str(third) + "_Legs_tan " + str(R_DynamicTan[first_]) + second
                        if not renpy.loadable(string):
                            # string = "images/Rogue" + str(third) + "/Rogue_" + str(third) + "_Legs_" + str(R_DynamicTan[first_]) + ".png"
                            # if not renpy.loadable(string):
                                string = Null()

            elif first_ == 5: #hose
                # if third == "SexFeet":
                #     if "modded" in R_DynamicTan[first_] or third == "Sex":
                #         string = "images/RogueSex/Rogue_Sex_Feet_" + str(R_DynamicTan[first_]) + second
                #         if not renpy.loadable(string):
                #                 string = Null()
                    
                #     else:
                #         string = "images/RogueSex/RogueTan/Rogue_Sex_Feet_tan " + str(R_DynamicTan[first_]) + second
                #         if not renpy.loadable(string):
                #                 string = Null()
                # else:
                    if "modded" in R_DynamicTan[first_] or third == "Sex":
                        string = "images/Rogue" + str(third) + "/Rogue_" + str(third) + "_Hose_" + str(R_DynamicTan[first_]) + second
                        if not renpy.loadable(string):
                            # string = "images/Rogue" + str(third) + "/Rogue_" + str(third) + "_Hose_" + str(R_DynamicTan[first_]) + ".png"
                            # if not renpy.loadable(string):
                                string = Null()
                    
                    else:
                        string = "images/Rogue" + str(third) + "/RogueTan/Rogue_" + str(third) + "_Hose_tan " + str(R_DynamicTan[first_]) + second
                        if not renpy.loadable(string):
                            # string = "images/Rogue" + str(third) + "/Rogue_" + str(third) + "_Hose_" + str(R_DynamicTan[first_]) + ".png"
                            # if not renpy.loadable(string):
                                string = Null()
        else:
            string = Null()
        return string


#End Rogue Wardrobe