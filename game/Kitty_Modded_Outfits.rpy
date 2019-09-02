## Kitty's Clothes ///////////////////
label Kitty_Modded_Clothes_Menu:    
    call KittyFace 
    menu:
        ch_k "So[K_like]you wanted to talk about my clothes?"
        "Stop sending me nudes." if K_Nude:
                    $ K_Nude = 0
                    ch_k "Ok"
        "Keep sending me nudes." if not K_Nude:
                    $ K_Nude = 1
                    ch_k "Ok"
        "Let's talk about your over shirts.":
                    jump Kitty_Modded_Clothes_Over        
        "Let's talk about your legwear.":
                    jump Kitty_Modded_Clothes_Legs
        "Let's talk about your underwear.":
                    jump Kitty_Modded_Clothes_Under
        "Let's talk about the other stuff.":
                    jump Kitty_Modded_Clothes_Misc
        "Save as main menu background clothes.":
                "This option will save this Kitty at the main menu background, are you sure?"
                menu:
                    "Yes":
                        "do it"
                        $ persistent.K_BG_Over = K_Over
                        $ persistent.K_BG_Chest = K_Chest
                        $ persistent.K_BG_Neck = K_Neck
                        $ persistent.K_BG_Legs = K_Legs
                        $ persistent.K_BG_Panties = K_Panties
                        # $ persistent.K_BG_Arms = K_Arms  #arm pose
                        $ persistent.K_BG_Gloves = K_Gloves
                        $ persistent.K_BG_Tan = K_Tan
                        $ persistent.K_BG_DynamicTan = K_DynamicTan
                        $ persistent.K_BG_Pierce = K_Pierce
                        $ persistent.K_BG_Hair = K_Hair
                        $ persistent.K_BG_Water = K_Water
                        $ persistent.K_BG_HairColor = K_HairColor
                        $ persistent.K_BG_Pubes = K_Pubes
                        $ persistent.K_BG_Hose = K_Hose
                        $ persistent.K_BG_Headband = K_Headband
                        $ persistent.K_BG_Gag = K_Gag
                        $ persistent.K_BG_Blindfold = K_Blindfold
                        # $ persistent.K_BG_Boots = K_Boots

                    "No":
                        pass
        "Never mind, you look good like that.":
                jump Kitty_Clothes
            
    jump Kitty_Modded_Clothes_Menu
    #End of Kitty Wardrobe Main Menu
        

    menu Kitty_Modded_Clothes_Over:                                                                                            # Overshirts
        "Why don't you go with no Overshirt?" if K_Over:
            call KittyFace("bemused", 1) 
            if ApprovalCheck("Kitty", 800, TabM=3) and (K_Chest or K_SeenChest):
                ch_k "Why not?"
            elif ApprovalCheck("Kitty", 1200, TabM=0):
                call Kitty_NoBra 
                if not _return:
                    jump Kitty_Modded_Clothes_Menu
            $ Line = K_Over
            $ K_Over = 0
            "She lets her [Line] drop to her feet."
            
        "Try on that dark shirt you have." if K_Over != "modded dark top":
            call KittyFace("bemused") 
            if K_Chest or K_SeenChest:
                ch_k "K."
            elif ApprovalCheck("Kitty", 800, TabM=0):
                ch_k "Yeah, ok."          
            else:
                call KittyFace("bemused", 1) 
                ch_k "This top is a little skimpy for what I have on under it."
                jump Kitty_Modded_Clothes_Menu    
            call SetOverKitty("modded dark top")
                
        "How about that purple t-shirt you have?" if K_Over != "modded purple shirt":
            call SetOverKitty("modded purple shirt")
            ch_k "This one?"

        "How about that violet shirt you have?" if K_Over != "modded violet shirt scarfless":
            call SetOverKitty("modded violet shirt scarfless")
            ch_k "This one?"
            
        # "Maybe just throw on a towel?" if K_Over != "towel":
        #     call KittyFace("bemused", 1) 
        #     if K_Chest or K_SeenChest:
        #         ch_k "Weirdo."
        #     elif ApprovalCheck("Kitty", 1000, TabM=0):
        #         call KittyFace("perplexed", 1) 
        #         ch_k "I guess? . ."          
        #     else:
        #         ch_k "I don't think so with what I have on under it."
        #         jump Kitty_Modded_Clothes_Menu    
        #     $ K_Over = "towel"  

        # "How about that black dress?" if K_Over != "modded black dress":
        #     if K_Legs:
        #         ch_k "I can't really wear that with my [K_Legs] on."
        #     elif ApprovalCheck("Kitty", 1100, TabM=3):
        #         ch_k "Sure. . ."
        #         call SetOverKitty("modded black dress")

        #     else:
        #         ch_k "That's a bit . . . revealing."  
                            
        "Never mind":
            pass
    jump Kitty_Modded_Clothes_Menu
    #End of Kitty Top
            

    menu Kitty_Modded_Clothes_Legs:                                                                                                    # Leggings    
        "Maybe go without the pants." if PantsNum("Kitty") > 6:
            call KittyFace("sexy", 1) 
            if K_SeenPanties and K_Panties and ApprovalCheck("Kitty", 500, TabM=5):
                ch_k "K."
            elif K_SeenPussy and ApprovalCheck("Kitty", 900, TabM=4):
                ch_k "Yeah, ok."
            elif ApprovalCheck("Kitty", 1300, TabM=2) and K_Panties:
                ch_k "For you, I guess. . ."
            elif ApprovalCheck("Kitty", 800) and not K_Panties:
                call Kitty_NoPantiesOn 
                if not _return:
                    jump Kitty_Modded_Clothes_Menu
            else:
                ch_k "Lol, not around you."
                if not K_Panties:
                    ch_k "I not {i}wearing any panties{/i}. . ."
                jump Kitty_Modded_Clothes_Menu
            $ K_Legs = 0    
            "She lets her pants drop through her to the ground."
            if K_Panties:                
                $ K_SeenPanties = 1
            else:
                call Kitty_First_Bottomless
        
        "Why don't you lose the shorts?" if PantsNum("Kitty") == 6:
            call KittyFace("sexy", 1) 
            if K_SeenPussy and ApprovalCheck("Kitty", 900, TabM=4): 
                # You've seen her pussy
                if ApprovalCheck("Kitty", 800, "L"):                  
                    ch_k "Well, not that I mind you seeing it. . ."
                elif ApprovalCheck("Kitty", 500, "O"):
                    ch_k "I guess. . ."
                elif ApprovalCheck("Kitty", 350, "I"):
                    ch_k "Hrmm. . ."
                else:
                    ch_k "Okay, okay."
                    
            elif ApprovalCheck("Kitty", 800) and not K_Panties:                       
                #she's not wearing anything over them
                call Kitty_NoPantiesOn 
                if not _return:
                    jump Kitty_Modded_Clothes_Menu
                    
            else:                                                      
                #she's wearing panties
                if not ApprovalCheck("Kitty", 700, TabM=3): #700+1200
                        ch_k "I'm not really comfortable with that right now. . ."
                        jump Kitty_Modded_Clothes_Under                    
                elif ApprovalCheck("Kitty", 800, "L", TabM=3):               
                        ch_k "Well aren't you cheeky. . ."
                elif ApprovalCheck("Kitty", 500, "O", TabM=3): #500+400
                        ch_k "Fine by me."
                elif ApprovalCheck("Kitty", 350, "I", TabM=3):
                        ch_k "Oooh, naughty."
                else:
                        ch_k "Oh, I guess I could."  
                    
            $ K_Legs  = 0       
            "She lets her shorts fall to the ground."
            
            if K_Panties:                
                $ K_SeenPanties = 1
            else:
                call Kitty_First_Bottomless 
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2)  


        "Why don't you lose the skirt?" if PantsNum("Kitty") == 5:
            call KittyFace("sexy", 1) 
            if K_SeenPussy and ApprovalCheck("Kitty", 900, TabM=4): 
                # You've seen her pussy
                if ApprovalCheck("Kitty", 800, "L"):                  
                    ch_k "Well, not that I mind you seeing it. . ."
                elif ApprovalCheck("Kitty", 500, "O"):
                    ch_k "I guess. . ."
                elif ApprovalCheck("Kitty", 350, "I"):
                    ch_k "Hrmm. . ."
                else:
                    ch_k "Okay, okay."
                    
            elif ApprovalCheck("Kitty", 800) and not K_Panties:                       
                #she's not wearing anything over them
                call Kitty_NoPantiesOn 
                if not _return:
                    jump Kitty_Modded_Clothes_Menu
                    
            else:                                                      
                #she's wearing panties
                if not ApprovalCheck("Kitty", 700, TabM=3): #700+1200
                        ch_k "I'm not really comfortable with that right now. . ."
                        jump Kitty_Modded_Clothes_Under                    
                elif ApprovalCheck("Kitty", 800, "L", TabM=3):               
                        ch_k "Well aren't you cheeky. . ."
                elif ApprovalCheck("Kitty", 500, "O", TabM=3): #500+400
                        ch_k "Fine by me."
                elif ApprovalCheck("Kitty", 350, "I", TabM=3):
                        ch_k "Oooh, naughty."
                else:
                        ch_k "Oh, I guess I could."  
                    
            $ K_Legs  = 0       
            "She lets her skirt fall to the ground."
            
            if K_Panties:                
                $ K_SeenPanties = 1
            else:
                call Kitty_First_Bottomless 
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2)  
            
        
        "You look great in those black blue pants." if K_Legs != "modded black blue pants":
            ch_k "K, no problem."
            $ K_Legs = "modded black blue pants"
        
        "What about wearing your blue shorts?" if K_Legs != "modded blue shorts":
            ch_k "K, no problem."
            $ K_Legs = "modded blue shorts"

        "What about wearing your white shorts?" if K_Legs != "modded white shorts":
            ch_k "K, no problem."
            $ K_Legs = "modded white shorts"

        "Your butt looks cute in that orange skirt." if K_Legs != "modded orange skirt":
            ch_k "Meoww~"
            $ K_Legs = "modded orange skirt"

        "Your butt looks cute in that white skirt." if K_Legs != "modded white skirt":
            ch_k "Meoww~"
            $ K_Legs = "modded white skirt"

        "Your butt looks cute in that black skirt." if K_Legs != "modded black skirt":
            ch_k "Meoww~"
            $ K_Legs = "modded black skirt"

        "Those leather pants look real tight on you." if K_Legs != "modded leather pants":
            ch_k "Mm~ That's hot."
            $ K_Legs = "modded leather pants"
            
                   
                                
        "Never mind":
            pass
    jump Kitty_Modded_Clothes_Menu
    #End of Kitty Pants
    

    menu Kitty_Modded_Clothes_Under:                                                                                                 # Tops    
        

        "Tops and bras":
            menu Kitty_Modded_Clothes_Under_Tops:  

                "How about you lose the [K_Chest]?" if K_Chest:
                    call KittyFace("bemused", 1) 
                    if K_SeenChest and ApprovalCheck("Kitty", 900, TabM=2.7):
                        ch_k "Sure."    
                    elif ApprovalCheck("Kitty", 1100, TabM=2):
                        if Taboo:
                            ch_k "I'm kind of nervous. . ."
                        else:
                            ch_k "If it's just you. . ."
                    elif K_Over == "pink top" or K_Over == "modded dark top" and ApprovalCheck("Kitty", 600, TabM=2):
                        ch_k "This look is a bit revealing. . ."  
                    elif K_Over == "red shirt" or K_Over == "modded purple shirt" or K_Over == "modded violet shirt scarfless" or K_Over == "modded violet shirt scarf" and ApprovalCheck("Kitty", 500, TabM=2):
                        ch_k "I guess I could. . ."  
                    elif not K_Over:
                        ch_k "Not without a little coverage, for modesty."
                        jump Kitty_Modded_Clothes_Menu
                    else:
                        ch_k "I don't think so, [K_Petname]."
                        jump Kitty_Modded_Clothes_Menu
                    $ Line = K_Chest
                    $ K_Chest = 0
                    if K_Over:
                        "She reaches into her [K_Over] grabs her [Line], and pulls it out, dropping it to the ground."
                    else:
                        "She lets her [Line] fall to the ground."
                    jump Kitty_Modded_Clothes_Under_Tops 
            
                "Try on that white camisole." if K_Chest != "modded white cami":
                    # call Kitty_Swimsuit_Change_Top 
                    ch_k "Ok."
                    call SetChestKitty("modded white cami")
                    jump Kitty_Modded_Clothes_Under_Tops
                             
                "Try on that orange top." if K_Chest != "modded orange top":
                    # call Kitty_Swimsuit_Change_Top 
                    ch_k "Ok."
                    call SetChestKitty("modded orange top")
                    jump Kitty_Modded_Clothes_Under_Tops  

                "Try on that black mfg top." if K_Chest != "modded black top":
                    # call Kitty_Swimsuit_Change_Top 
                    ch_k "Ok."
                    call SetChestKitty("modded black top")
                    jump Kitty_Modded_Clothes_Under_Tops          
        
                "How about that leather top?" if K_Chest != "modded leather top":
                    # call Kitty_Swimsuit_Change_Top 
                    ch_k "Mkay."
                    call SetChestKitty("modded leather top")
                    jump Kitty_Modded_Clothes_Under_Tops
                    
                "I like that darker lace bra." if K_Chest != "modded darker lace bra":
                    if K_SeenChest or ApprovalCheck("Kitty", 1300, TabM=2):
                        # call Kitty_Swimsuit_Change_Top 
                        ch_k "K."   
                        call SetChestKitty("modded darker lace bra")
                    else:                
                        ch_k "It's pretty skimpy. . ." 
                    jump Kitty_Modded_Clothes_Under_Tops 

                "I like that kitty lingerie top." if K_Chest != "modded kitty lingerie top":
                    if K_SeenChest or ApprovalCheck("Kitty", 1300, TabM=2):
                        # call Kitty_Swimsuit_Change_Top 
                        ch_k "K."   
                        call SetChestKitty("modded kitty lingerie top")
                    else:                
                        ch_k "It's pretty skimpy. . ." 
                    jump Kitty_Modded_Clothes_Under_Tops 
                    
                "Go back":  
                    jump Kitty_Modded_Clothes_Under

                
                                                                                                                            #Panties        
        
        "Panties": 
            
            menu Kitty_Modded_Clothes_Under_Panties:  

                "You could lose those panties. . ." if K_Panties:
                    call KittyFace("bemused", 1) 
                    if ApprovalCheck("Kitty", 900) and (K_Legs or (K_SeenPussy and not Taboo)):
                        #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
                        
                        if ApprovalCheck("Kitty", 850, "L"):               
                                ch_k "Well, if you ask me nicely. . ."
                        elif ApprovalCheck("Kitty", 500, "O"):
                                ch_k "For you, ok."
                        elif ApprovalCheck("Kitty", 350, "I"):
                                ch_k "[[snort]."
                        else:
                                ch_k "Yeah, I guess."         
                    else:                       #low approval or not wearing pants or in public 
                        if ApprovalCheck("Kitty", 1100, "LI", TabM=3) and K_Love > K_Inbt:               
                                ch_k "Well, not that I mind you seeing it. . ."
                        elif ApprovalCheck("Kitty", 700, "OI", TabM=3) and K_Obed > K_Inbt:
                                ch_k "I guess. . ."
                        elif ApprovalCheck("Kitty", 600, "I", TabM=3):
                                ch_k "Hrmm. . ."
                        elif ApprovalCheck("Kitty", 1300, TabM=3):
                                ch_k "Okay, okay."
                        else: 
                                call KittyFace("surprised") 
                                $ K_Brows = "angry"
                                if Taboo:
                                    ch_k "Not in public, [K_Petname]!"
                                else:
                                    ch_k "I don't like you that much, [K_Petname]!"
                                jump Kitty_Modded_Clothes_Menu
                                
                                
                    $ Line = K_Panties
                    $ K_Panties = 0  
                    if K_Legs:
                        "She reaches into her pocket, grabs hold of something, and then pulls her [Line] out, droping them to the ground."                
                    else:
                        "She lets her [Line] drop to the ground."
                        call Kitty_First_Bottomless 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2) 
                    jump Kitty_Modded_Clothes_Under_Panties  

                "Why don't you wear the white panties instead?" if K_Panties and K_Panties != "modded white panties":
                    if ApprovalCheck("Kitty", 1100, TabM=3):
                            # call Kitty_Swimsuit_Change_Bottom 
                            ch_k "K."
                            $ K_Panties = "modded white panties"
                    else:                
                            ch_k "I don't think that's any of your beeswax."
                    jump Kitty_Modded_Clothes_Under_Panties
                        
                "Why don't you wear the darker lace panties instead?" if K_Panties and K_Panties != "modded darker lace panties":
                    if ApprovalCheck("Kitty", 1300, TabM=3):
                            # call Kitty_Swimsuit_Change_Bottom 
                            ch_k "I guess."
                            $ K_Panties = "modded darker lace panties"
                    else:
                            ch_k "That's[K_like]none of your business."
                    jump Kitty_Modded_Clothes_Under_Panties

                "Why don't you wear the kitty lingerie panties instead?" if K_Panties != "modded kitty lingerie panties":
                    if ApprovalCheck("Kitty", 1300, TabM=3):
                            # call Kitty_Swimsuit_Change_Bottom 
                            ch_k "I guess."
                            $ K_Panties = "modded kitty lingerie panties"
                    else:
                            ch_k "That's[K_like]none of your business."
                    jump Kitty_Modded_Clothes_Under_Panties

                "You know, you could wear some panties with that. . ." if not K_Panties:
                    call KittyFace("bemused", 1) 
                    if (K_Love+K_Obed) <= (2* K_Inbt):
                        $ K_Mouth = "smile"
                        ch_k "I think I'd. . . rather not."
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2)
                        menu:
                            "Wear them":
                                pass
                            "Ok":
                                jump Kitty_Modded_Clothes_Menu
                    # call Kitty_Swimsuit_Change_Bottom 
                    menu:
                        ch_k "I guess. . ."
                        "How about the green ones?":
                            ch_k "Sure, ok."
                            $ K_Panties = "green panties"
                        "How about the white ones?":
                            ch_k "Sure, ok."
                            $ K_Panties = "modded white panties"
                        "How about the purple bikini?":
                            ch_k "Sure, ok."
                            $ K_Panties = "modded purple bikini panties"
                        "How about the lace ones?" if "lace panties" in K_Inventory:
                            ch_k "Alright."                
                            $ K_Panties  = "lace panties"
                        "How about the darker lace ones?":
                            ch_k "Alright."                
                            $ K_Panties = "modded darker lace panties"
                        "How about the kitty lingerie ones?":
                            ch_k "Alright."                
                            $ K_Panties = "modded kitty lingerie panties"
                    jump Kitty_Modded_Clothes_Under_Panties

                "Go back":  
                    jump Kitty_Modded_Clothes_Under

        "Socks and Stockings": 
            
            menu Kitty_Modded_Clothes_Under_Hoses:  

                "You could lose those socks. . ." if K_Hose and K_Hose != "modded stockings":
                    ch_k "K."
                    call SetHoseKitty(0)
                    jump Kitty_Modded_Clothes_Under_Hoses  

                "You could lose those stockings. . ." if K_Hose == "modded stockings":
                    ch_k "K."
                    call SetHoseKitty(0)
                    jump Kitty_Modded_Clothes_Under_Hoses  

                "Why don't you wear those stockings?" if K_Hose != "modded stockings":
                    ch_k "K."
                    call SetHoseKitty("modded stockings")
                    jump Kitty_Modded_Clothes_Under_Hoses

                "Why don't you wear those black socks" if K_Hose != "modded black socks":
                    ch_k "K."
                    call SetHoseKitty("modded black socks")
                    jump Kitty_Modded_Clothes_Under_Hoses

                "Why don't you wear those white socks" if K_Hose != "modded white socks":
                    ch_k "K."
                    call SetHoseKitty("modded white socks")
                    jump Kitty_Modded_Clothes_Under_Hoses

                "Why don't you wear those pink socks" if K_Hose != "modded pink socks":
                    ch_k "K."
                    call SetHoseKitty("modded pink socks")
                    jump Kitty_Modded_Clothes_Under_Hoses

                "Go back":  
                    jump Kitty_Modded_Clothes_Under

        "How about your swimsuits.":

            menu Kitty_Modded_Clothes_Under_SwimSuits:

                # "Why don't you wear the swimsuit3" if K_Panties != "swimsuit3" or K_Chest != "swimsuit3":
                #     if ApprovalCheck("Kitty", 1200, TabM=3):
                #         ch_k "Sure."
                #         $ K_Panties = "swimsuit3"
                #         $ K_Chest = "swimsuit3"
                #     else:
                #         ch_r "I don't see how that's any business of yours, [K_Petname]."
                #     jump Kitty_Modded_Clothes_Under_SwimSuits

                # "Remove the swimsuit" if K_Panties == "swimsuit3" or K_Chest == "swimsuit3":
                #                 call Kitty_Remove_Swimsuit 
                #                 jump Kitty_Modded_Clothes_Under_SwimSuits

                "Why don't you wear the purple bikini bra?" if K_Chest != "modded purple bikini bra":
                    if ApprovalCheck("Kitty", 1100, TabM=3):
                            # call Kitty_Swimsuit_Change_Top 
                            ch_k "K."
                            call SetChestKitty("modded purple bikini bra")
                    else:                
                            ch_k "I don't think that's any of your beeswax."
                    jump Kitty_Modded_Clothes_Under_SwimSuits

                "Why don't you wear the purple bikini panties?" if K_Panties != "modded purple bikini panties":
                    if ApprovalCheck("Kitty", 1100, TabM=3):
                            # call Kitty_Swimsuit_Change_Bottom 
                            ch_k "K."
                            $ K_Panties = "modded purple bikini panties"
                    else:                
                            ch_k "I don't think that's any of your beeswax."
                    jump Kitty_Modded_Clothes_Under_SwimSuits

                "Why don't you wear the red bikini bra?" if K_Chest != "modded red bikini bra":
                    if ApprovalCheck("Kitty", 1100, TabM=3):
                            # call Kitty_Swimsuit_Change_Top 
                            ch_k "K."
                            call SetChestKitty("modded red bikini bra")
                    else:                
                            ch_k "I don't think that's any of your beeswax."
                    jump Kitty_Modded_Clothes_Under_SwimSuits

                "Nevermind":
                    jump Kitty_Modded_Clothes_Under

        "Never mind":
            pass
    jump Kitty_Modded_Clothes_Menu
    #End of Kitty Underwear
       
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  
        
    menu Kitty_Modded_Clothes_Misc:
        "Put on that pink kitty headband of yours." if K_Headband != "pink":
                        $ K_Headband = "pink"
        "Put on that pink kitty headband of yours." if K_Headband != "black":
                        $ K_Headband = "black"
        "Put on that cruiser dva headphone of yours." if K_Headband != "cruiser dva":
                        $ K_Headband = "cruiser dva"
        "Take off that headband." if K_Headband:
                        $ K_Headband = ""
        "Let's talk about your hair":
            menu Kitty_Modded_Clothes_Misc_Hair:                                                                                                                    #Misc
        
                "You look good with your hair up." if K_Hair != "evo":
                    if ApprovalCheck("Kitty", 600):
                        ch_k "Like this?"
                        $ K_Hair = "evo"
                    else:
                        ch_k "Yeah, I know that."
                    jump Kitty_Modded_Clothes_Misc_Hair

                "Maybe let your hair down." if K_Hair != "long":
                    if ApprovalCheck("Kitty", 600):
                        ch_k "You think?"
                        $ K_Hair = "long"
                    else:
                        ch_k "I[K_like]kinda prefer to keep it up."
                    jump Kitty_Modded_Clothes_Misc_Hair

                "You should go for that wet look with your hair." if K_Hair != "wet":
                    if ApprovalCheck("Kitty", 800):
                        ch_k "You think so?"
                        "She rummages in her bag and grabs some gel, running it through her hair."
                        ch_k "Like this?"
                        $ K_Hair = "wet"
                    else:
                        ch_k "It's too high maintenance."
                    jump Kitty_Modded_Clothes_Misc_Hair

                "Dye your hair black." if K_HairColor != "black":
                    if ApprovalCheck("Kitty", 800):
                        ch_k "You think so?"
                        #"She rummages in her bag and grabs some gel, running it through her hair."
                        ch_k "Like this?"
                        $ K_HairCustomColor.red = 255
                        $ K_HairCustomColor.green = 255
                        $ K_HairCustomColor.blue = 255
                        call SetHairColorKitty("black")
                    else:
                        ch_k "It's too high maintenance."
                    jump Kitty_Modded_Clothes_Misc_Hair

                "Dye your hair blonde." if K_HairColor != "blonde":
                    if ApprovalCheck("Kitty", 800):
                        ch_k "You think so?"
                        #"She rummages in her bag and grabs some gel, running it through her hair."
                        ch_k "Like this?"
                        $ K_HairCustomColor.red = 255
                        $ K_HairCustomColor.green = 255
                        $ K_HairCustomColor.blue = 255
                        call SetHairColorKitty("blonde")
                    else:
                        ch_k "It's too high maintenance."
                    jump Kitty_Modded_Clothes_Misc_Hair

                "Dye your hair red." if K_HairColor != "red":
                    if ApprovalCheck("Kitty", 800):
                        ch_k "You think so?"
                        #"She rummages in her bag and grabs some gel, running it through her hair."
                        ch_k "Like this?"
                        $ K_HairCustomColor.red = 255
                        $ K_HairCustomColor.green = 255
                        $ K_HairCustomColor.blue = 255
                        call SetHairColorKitty("red")
                    else:
                        ch_k "It's too high maintenance."
                    jump Kitty_Modded_Clothes_Misc_Hair

                "Let me select the color.":
                    if ApprovalCheck("Kitty", 800):
                        ch_k "You think so?"
                        #"She rummages in her bag and grabs some gel, running it through her hair."
                        # ch_k "Like this?"
                        # "WARNING: This is gonna apply to all of her hair colors, to reset it either put all values into 255 or select option Change the color of you hair back."
                        $ K_HairCustomColor.red = 255
                        $ K_HairCustomColor.green = 255
                        $ K_HairCustomColor.blue = 255
                        call Recolor_Hair("Kitty")
                        call SetHairColorKitty("White")
                    else:
                        ch_k "It's too high maintenance."
                    jump Kitty_Modded_Clothes_Misc_Hair

                "Change the color of you hair back." if K_HairColor:    
                    if ApprovalCheck("Kitty", 800):
                        ch_k "You think so?"
                        #"She rummages in her bag and grabs some gel, running it through her hair."
                        ch_k "Like this?"
                        $ K_HairCustomColor.red = 255
                        $ K_HairCustomColor.green = 255
                        $ K_HairCustomColor.blue = 255
                        call SetHairColorKitty("")
                    else:
                        ch_k "It's too high maintenance."
                    jump Kitty_Modded_Clothes_Misc_Hair

                "Go back":
                    jump Kitty_Modded_Clothes_Misc

        "You know, I like some nice hair down there. Maybe grow it out." if not K_Pubes and "pubes" in K_Todo:
            call KittyFace("bemused", 1) 
            ch_k "[[snort] You've got to give it some time!"
        "You know, I like some nice hair down there. Maybe grow it out." if not K_Pubes and "pubes" not in K_Todo:
            call KittyFace("bemused", 1) 
            $ Approval = ApprovalCheck("Kitty", 1150, TabM=0)
            if ApprovalCheck("Kitty", 850, "L", TabM=0) or (Approval and K_Love > 2 * K_Obed):               
                ch_k "I guess I could. . ."
            elif ApprovalCheck("Kitty", 500, "I", TabM=0) or (Approval and K_Inbt > K_Obed):
                ch_k "You want a furry kitty to pet?"
            elif ApprovalCheck("Kitty", 400, "O", TabM=0) or Approval:
                ch_k "If you want me to. . ."
            else: 
                call KittyFace("surprised") 
                $ K_Brows = "angry"
                ch_k "Not that it's any of your business, [K_Petname]."
                jump Kitty_Modded_Clothes_Menu
            $ K_Todo.append("pubes")
            $ K_PubeC = 6
        
        "I like it waxed clean down there." if K_Pubes == 1:
            call KittyFace("bemused", 1) 
            if "shave" in K_Todo:
                ch_k "I know, I know. I'll take care of it later."
            else:
                $ Approval = ApprovalCheck("Kitty", 1150, TabM=0)
                
                if ApprovalCheck("Kitty", 850, "L", TabM=0) or (Approval and K_Love > 2 * K_Obed):               
                    ch_k "I guess I could tidy up a bit. . ."
                elif ApprovalCheck("Kitty", 500, "I", TabM=0) or (Approval and K_Inbt > K_Obed):
                    ch_k "I'll keep it smooth."
                elif ApprovalCheck("Kitty", 400, "O", TabM=0) or Approval:
                    ch_k "I'll get it done."
                else: 
                    call KittyFace("surprised") 
                    $ K_Brows = "angry"
                    ch_k "Not that it's any of your business, [K_Petname]."
                    jump Kitty_Modded_Clothes_Menu
                $ K_Todo.append("shave")        
        "Piercings. [[See what she looks like without them first] (locked)" if not K_SeenPussy and not K_SeenChest:
            pass
            
        "You know, you'd look really nice with some ring body piercings." if K_Pierce != "ring" and (K_SeenPussy or K_SeenChest) and "ring" not in K_Todo:
            call KittyFace("bemused", 1) 
            $ Approval = ApprovalCheck("Kitty", 1350, TabM=0)
            if ApprovalCheck("Kitty", 900, "L", TabM=0) or (Approval and K_Love > 2* K_Obed):   
                ch_k "If you think they'd look good on me. . ."
            elif ApprovalCheck("Kitty", 600, "I", TabM=0) or (Approval and K_Inbt > K_Obed):
                ch_k "I think they'd look great too!"
            elif ApprovalCheck("Kitty", 500, "O", TabM=0) or Approval:
                ch_k "K, I'll take care of it."
            else: 
                call KittyFace("surprised") 
                $ K_Brows = "angry"
                ch_k "Not that it's any of your business, [K_Petname]."
                jump Kitty_Modded_Clothes_Menu            
            $ K_Todo.append("ring")
        
        "You know, you'd look really nice with some barbell body piercings." if K_Pierce != "barbell" and (K_SeenPussy or K_SeenChest)and "barbell" not in K_Todo:
            call KittyFace("bemused", 1) 
            $ Approval = ApprovalCheck("Kitty", 1350, TabM=0)
            if ApprovalCheck("Kitty", 900, "L", TabM=0) or (Approval and K_Love > 2 * K_Obed): 
                ch_k "If you think they'd look good on me. . ."
            elif ApprovalCheck("Kitty", 600, "I", TabM=0) or (Approval and K_Inbt > K_Obed):
                ch_k "I think they'd look great too!"
            elif ApprovalCheck("Kitty", 500, "O", TabM=0) or Approval:
                ch_k "K, I'll take care of it."
            else: 
                call KittyFace("surprised") 
                $ K_Brows = "angry"
                ch_k "Not that it's any of your business, [K_Petname]."
                jump Kitty_Modded_Clothes_Menu                
            $ K_Todo.append("barbell")
            $ K_Pierce = "barbell"
            
        "You know, you'd look better without those piercings." if K_Pierce:
            call KittyFace("bemused", 1) 
            $ Approval = ApprovalCheck("Kitty", 1350, TabM=0)
            if ApprovalCheck("Kitty", 950, "L", TabM=0) or (Approval and K_Love > K_Obed):   
                ch_k "I guess if they're getting in the way . ."
            elif ApprovalCheck("Kitty", 700, "I", TabM=0) or (Approval and K_Inbt > K_Obed):
                ch_k "They were getting a little annoying."
            elif ApprovalCheck("Kitty", 600, "O", TabM=0) or Approval:
                ch_k "I'll take them out then."
            else: 
                call KittyFace("surprised") 
                $ K_Brows = "angry"
                ch_k "Well {i}I{/i} kinda like'em."
                jump Kitty_Modded_Clothes            
            $ K_Pierce = 0 
        "Why don't you try on that gold necklace." if K_Neck != "gold necklace":
            ch_k "Ok. . ."         
            $ K_Neck = "gold necklace"
        "Why don't you try on that star necklace." if K_Neck != "star necklace":
            ch_k "Ok. . ."         
            $ K_Neck = "star necklace"
    #     "Why don't you try on that scarf." if K_Neck != "scarf":
    #         ch_k "Ok. . ."         
    #         $ K_Neck = "scarf"
        "Maybe go without a necklace." if K_Neck and K_Neck != "scarf":
            ch_k "Ok. . ."         
            $ K_Neck = 0
    #     "Maybe go without the scarf." if (K_Neck and K_Neck == "scarf"):
    #         ch_k "Ok. . ."         
    #         $ K_Neck = 0

    #     "Why don't you wear those black gloves." if not K_Gloves:
    #         ch_k "Ok. . ."         
    #         $ K_Gloves = "black gloves"
    #     "Why don't you remove these gloves." if K_Gloves:
    #         ch_k "Ok. . ."         
    #         $ K_Gloves = 0
            
        "Never mind":
            jump Kitty_Modded_Clothes_Menu
            
    jump Kitty_Modded_Clothes_Misc
    #End of Kitty Misc Wardrobe
    
return
#End Kitty Wardrobe

label SetChestKitty(Outfit = "modded tape"):
    $ K_Chest = Outfit
    call Mod_Update_Kitty_Image
    return

label SetOverKitty(Outfit = "modded white mesh top"):
    $ K_Over = Outfit
    call Mod_Update_Kitty_Image
    return

label SetLegsKitty(Outfit = "modded black large panties"):
    $ K_Legs = Outfit
    call Mod_Update_Kitty_Image
    return

label SetPantiesKitty(Outfit = "modded black large panties"):
    $ K_Panties = Outfit
    call Mod_Update_Kitty_Image
    return

label SetHoseKitty(Outfit = "modded fishnet"):
    $ K_Hose = Outfit
    call Mod_Update_Kitty_Image
    return

label SetHairColorKitty(Outfit = ""):
    $ K_HairColor = Outfit
    call Mod_Update_Kitty_Image
    return

label Mod_Update_Kitty_Image:
    if renpy.showing("Kitty_Sprite"):
        show Kitty_Sprite 
    elif renpy.showing("Kitty_Doggy"):
        show Kitty_Doggy 
    elif renpy.showing("Kitty_SexSprite"):
        show Kitty_SexSprite   
    elif renpy.showing("Kitty_BJ_Animation"):
        show Kitty_BJ_Animation   
    elif renpy.showing("Kitty_HJ_Animation"):
        show Kitty_HJ_Animation   
    elif renpy.showing("Kitty_TJ_Animation"):
        show Kitty_TJ_Animation   
    return
    
init python:
    
    def IsOutfitModdedKitty(Type = "Over"):
        if Type == "Over":
            if K_Over:
                if "modded" in K_Over:
                    return 1
            else:
                return 0
        if Type == "Chest":
            if K_Chest:
                if "modded" in K_Chest:
                    return 1
            else:
                return 0
        if Type == "Legs":
            if K_Legs:
                if "modded" in K_Legs:
                    return 1
            else:
                return 0
        if Type == "Panties":
            if K_Panties:
                if "modded" in K_Panties:
                    return 1
            else:
                return 0
        return 0

    def Mod_Kitty_OutfitShame(Type = "Chest"):                                                                             #sets custom outfit    
  
        if Type == "Chest":
            # if R_Chest == "tank":                                              
            #     $ Count = 20
            # elif R_BodySuit == "classic uniform":
            #     $ Count = 20 
            # elif R_BodySuit == "swimsuit1":
            #     $ Count = 20
            # elif R_BodySuit == "swimsuit2":
            #     $ Count = 10
            if K_Chest == "modded white cami":  
                return 15
            elif K_Chest == "modded purple bikini bra":
                return 15
            elif K_Chest == "modded red bikini bra":
                return 15
            elif K_Chest == "modded orange top":
                return 25
            elif K_Chest == "modded black top":
                return 25
            elif K_Chest == "modded leather top":
                return 25
            elif K_Chest == "modded darker lace bra":
                return 5   
            elif K_Chest == "modded kitty lingerie top":
                return 5   
            elif K_Chest == "modded bustier bra":
                return 5
            else:
                return 0

        if Type == "Over":
            if K_Over == "modded dark top":                                             
                return 15
            elif K_Over == "modded violet shirt scarfless":      
                return 20
            elif K_Over == "modded violet shirt scarf":      
                return 20
            elif K_Over == "modded purple shirt":      
                return 20
            # elif K_Over == "modded black dress":                                             
            #     return 40
            else:      
                return 0

        if Type == "Legs":
            if K_Legs == "modded black blue pants":
                return 25 
            elif K_Legs == "modded leather pants":
                return 25 
            elif K_Legs == "modded white shorts":                #If wearing shorts
                return 25 
            elif K_Legs == "modded blue shorts":                #If wearing shorts
                return 25 
            elif K_Legs == "modded orange skirt":                #If wearing skirt
                return 20 
            elif K_Legs == "modded white skirt":                #If wearing skirt
                return 20 
            elif K_Legs == "modded black skirt":                #If wearing skirt
                return 20 
            else:
                return 0  
        

        if Type == "Panties":
                       
            if K_Panties == "modded purple bikini panties":      #If wearing only bikini purple
                return 15      
            elif K_Panties == "modded white panties":      #If wearing only green panties
                return 10
            elif K_Panties == "modded darker lace panties":       #If wearing only lace panties
                return 5
            elif K_Panties == "modded kitty lingerie panties":       #If wearing only kitty lingerie panties
                return 5
            # elif K_Panties == "swimsuit3":
            #     return 30
            elif K_Panties == "modded zipper panties":
                return 3
            else:
                return 0
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
    def GetModdedStringTanKitty(first = "3", second = ".png", third = "Sprite"):
        first_ = int(first)
        if K_DynamicTan[first_]:
            if first_ == 3: #chest
                if "modded" in K_DynamicTan[first_] or third == "Doggy":
                    string = "images/Kitty" + str(third) + "/Kitty_" + str(third) + "_Chest_" + str(K_DynamicTan[first_]) + second
                    if not renpy.loadable(string):
                        string = "images/Kitty" + str(third) + "/Kitty_" + str(third) + "_Chest_" + str(K_DynamicTan[first_]) + ".png"
                        if not renpy.loadable(string):
                            string = Null()
                
                else:
                    string = "images/Kitty" + str(third) + "/KittyTan/Kitty_" + str(third) + "_Chest_tan " + str(K_DynamicTan[first_]) + second
                    if not renpy.loadable(string):
                        string = "images/Kitty" + str(third) + "KittyTan/Kitty_" + str(third) + "_Chest_tan " + str(K_DynamicTan[first_]) + ".png"
                        if not renpy.loadable(string):
                            string = Null()

            elif first_ == 1: #over
                if "modded" in K_DynamicTan[first_] or third == "Doggy":
                    string = "images/Kitty" + str(third) + "/Kitty_" + str(third) + "_Over_" + str(K_DynamicTan[first_]) + second
                    if not renpy.loadable(string):
                        string = "images/Kitty" + str(third) + "/Kitty_" + str(third) + "_Over_" + str(K_DynamicTan[first_]) + ".png"
                        if not renpy.loadable(string):
                            string = Null()
                
                else:
                    string = "images/Kitty" + str(third) + "/KittyTan/Kitty_" + str(third) + "_Over_tan " + str(K_DynamicTan[first_]) + second
                    if not renpy.loadable(string):
                        string = "images/Kitty" + str(third) + "KittyTan/Kitty_" + str(third) + "_Over_tan " + str(K_DynamicTan[first_]) + ".png"
                        if not renpy.loadable(string):
                            string = Null()

            elif first_ == 4: #panties
                if "modded" in K_DynamicTan[first_] or third == "Doggy":
                    string = "images/Kitty" + str(third) + "/Kitty_" + str(third) + "_Panties_" + str(K_DynamicTan[first_]) + second
                    if not renpy.loadable(string):
                        # string = "images/Kitty" + str(third) + "/Kitty_" + str(third) + "_Panties_" + str(K_DynamicTan[first_]) + ".png"
                        # if not renpy.loadable(string):
                            string = Null()
                
                else:
                    string = "images/Kitty" + str(third) + "/KittyTan/Kitty_" + str(third) + "_Panties_tan " + str(K_DynamicTan[first_]) + second
                    if not renpy.loadable(string):
                        # string = "images/Kitty" + str(third) + "/Kitty_" + str(third) + "_Panties_" + str(K_DynamicTan[first_]) + ".png"
                        # if not renpy.loadable(string):
                            string = Null()

            elif first_ == 2: #legs
                if third == "SexFeet":
                    if "modded" in K_DynamicTan[first_] or third == "Doggy":
                        string = "images/KittySex/Kitty_Sex_Feet_" + str(K_DynamicTan[first_]) + second
                        if not renpy.loadable(string):
                                string = Null()
                    
                    else:
                        string = "images/KittySex/KittyTan/Kitty_Sex_Feet_tan " + str(K_DynamicTan[first_]) + second
                        if not renpy.loadable(string):
                                string = Null()
                else:
                    if "skirt" in K_DynamicTan[first_] and third == "Sex":
                        string = "images/Kitty" + str(third) + "/KittyTan/Kitty_" + str(third) + "_Legs_tan skirts.png"

                    elif "modded" in K_DynamicTan[first_] or third == "Doggy":
                        string = "images/Kitty" + str(third) + "/Kitty_" + str(third) + "_Legs_" + str(K_DynamicTan[first_]) + second
                        if not renpy.loadable(string):
                            # string = "images/Kitty" + str(third) + "/Kitty_" + str(third) + "_Legs_" + str(K_DynamicTan[first_]) + ".png"
                            # if not renpy.loadable(string):
                                string = Null()
                    
                    else:
                        string = "images/Kitty" + str(third) + "/KittyTan/Kitty_" + str(third) + "_Legs_tan " + str(K_DynamicTan[first_]) + second
                        if not renpy.loadable(string):
                            # string = "images/Kitty" + str(third) + "/Kitty_" + str(third) + "_Legs_" + str(K_DynamicTan[first_]) + ".png"
                            # if not renpy.loadable(string):
                                string = Null()
            elif first_ == 5: #hose
                    # if "modded" in K_DynamicTan[first_] or third == "Doggy":
                    if "modded" in K_DynamicTan[first_]:
                        string = "images/Kitty" + str(third) + "/Kitty_" + str(third) + "_Hose_" + str(K_DynamicTan[first_]) + second
                        if not renpy.loadable(string):
                            # string = "images/Kitty" + str(third) + "/Kitty_" + str(third) + "_Hose_" + str(K_DynamicTan[first_]) + ".png"
                            # if not renpy.loadable(string):
                                string = Null()
                    
                    else:
                        # string = "images/Kitty" + str(third) + "/KittyTan/Kitty_" + str(third) + "_Hose_tan " + str(K_DynamicTan[first_]) + second
                        # if not renpy.loadable(string):
                        #     # string = "images/Kitty" + str(third) + "/Kitty_" + str(third) + "_Hose_" + str(K_DynamicTan[first_]) + ".png"
                        #     # if not renpy.loadable(string):
                                string = Null()
        else:
            string = Null()
        return string

    def GetHairColor(HairColor = 0):
        if HairColor == 0:
            return ""
        elif HairColor == "custom":
            return "white"
        else:
            return HairColor


#End Rogue Wardrobe