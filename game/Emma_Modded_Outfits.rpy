## Emma's Clothes ///////////////////
label Emma_Modded_Clothes_Menu:    
    call EmmaFace 
    menu:
        ch_e "You wanted to discuss my clothing choices?"
        "Let's talk about your over shirts.":
                    jump Emma_Modded_Clothes_Over        
        "Let's talk about your legwear.":
                    jump Emma_Modded_Clothes_Legs
        "Let's talk about your underwear.":
                    jump Emma_Modded_Clothes_Under
        "Let's talk about the other stuff.":
                    jump Emma_Modded_Clothes_Misc
        "Save as main menu background clothes.":
                "This option will save this Emma at the main menu background, are you sure?"
                menu:
                    "Yes":
                        "do it"
                        $ persistent.E_BG_Over = E_Over
                        $ persistent.E_BG_Chest = E_Chest
                        $ persistent.E_BG_Neck = E_Neck
                        $ persistent.E_BG_Legs = E_Legs
                        $ persistent.E_BG_Panties = E_Panties
                        $ persistent.E_BG_Arms = E_Arms
                        # $ persistent.E_BG_Gloves = E_Gloves
                        # $ persistent.E_BG_Tan = E_Tan
                        $ persistent.E_BG_Pierce = E_Pierce
                        $ persistent.E_BG_Hair = E_Hair
                        $ persistent.E_BG_HairColor = E_HairColor
                        $ persistent.E_BG_Pubes = E_Pubes
                        $ persistent.E_BG_Hose = E_Hose
                        # $ persistent.E_BG_Boots = E_Boots

                    "No":
                        pass
        "Never mind, you look good like that.":
                jump Emma_Clothes
            
    jump Emma_Modded_Clothes_Menu
    #End of Emma Wardrobe Main Menu
        
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Emma_Modded_Clothes_Over:                                                                                            # Overshirts
        "Why don't you go with no Overshirt?" if E_Over:
            call EmmaFace("bemused", 1)
            if ApprovalCheck("Emma", 800, TabM=(3-Public)) and (E_Chest or E_SeenChest):
                ch_e "Certainly."
            elif ApprovalCheck("Emma", 1200, TabM=0):
                call Emma_NoBra
                if not _return:
                    jump Emma_Modded_Clothes_Menu                    
            $ Line = E_Over
            $ E_Over = 0   
            call Emma_Tits_Up
            "She shrugs off her [Line]."
            if not E_Chest:
                call Emma_First_Topless
            
        "Try on that white jacket you have." if E_Over != "jacket":
            call EmmaFace("bemused")
            if E_Chest or E_SeenChest or ApprovalCheck("Emma", 500, TabM=(3-Public)):
                ch_e "Yeah, ok."          
            else:
                call EmmaFace("bemused", 1)
                ch_e "I'm not sure this is appropriate without something more substantial underneath."
                jump Emma_Modded_Clothes_Menu    
            $ E_Over = "jacket"

        "Try on that black jacket you have." if E_Over != "modded black jacket":
            call EmmaFace("bemused")
            if E_Chest or E_SeenChest or ApprovalCheck("Emma", 500, TabM=(3-Public)):
                ch_e "Yeah, ok."          
            else:
                call EmmaFace("bemused", 1)
                ch_e "I'm not sure this is appropriate without something more substantial underneath."
                jump Emma_Modded_Clothes_Menu    
            call SetOverEmma("modded black jacket")

        "Try on that white cape you have." if E_Over != "modded cape":
            call EmmaFace("bemused")
            if E_Chest or E_SeenChest or ApprovalCheck("Emma", 500, TabM=(3-Public)):
                ch_e "Yeah, ok."          
            else:
                call EmmaFace("bemused", 1)
                ch_e "I'm not sure this is appropriate without something more substantial underneath."
                jump Emma_Modded_Clothes_Menu    
            call SetOverEmma("modded cape")

        "Try on that black cape you have." if E_Over != "modded black cape":
            call EmmaFace("bemused")
            if E_Chest or E_SeenChest or ApprovalCheck("Emma", 500, TabM=(3-Public)):
                ch_e "Yeah, ok."          
            else:
                call EmmaFace("bemused", 1)
                ch_e "I'm not sure this is appropriate without something more substantial underneath."
                jump Emma_Modded_Clothes_Menu    
            call SetOverEmma("modded black cape")
                
            
        "Maybe just throw on a towel?" if E_Over != "towel":
            call EmmaFace("bemused", 1)
            $ Bonus = 5 if bg_current == "bg showerroom" else 0
            if E_Chest or (E_SeenChest and ApprovalCheck("Emma", 500, TabM=(3-Public-Bonus))):
                ch_e "Oh, you like this?"
            elif ApprovalCheck("Emma", 1000, TabM=(3-Public-Bonus)):
                call EmmaFace("perplexed", 1)
                ch_e "Fine."          
            else:
                ch_e "This wouldn't leave much to the imagination."
                jump Emma_Modded_Clothes_Menu  
            call Emma_NoBra
            if not _return:
                jump Emma_Modded_Clothes_Menu
            $ E_Over = "towel"       
            call Emma_Tits_Up

        "How about that nighty I got you?" if E_Over != "nighty" and "nighty" in E_Inventory:
                        if E_Legs:
                            ch_e "I can't really wear that with my [E_Legs] on."
                        elif ApprovalCheck("Emma", 1100, TabM=3):
                            ch_e "Sure. . ."
                            $ E_Over = "nighty"   
                            if "lace bra" in E_Inventory:
                                $ E_Chest = "lace bra"
                            else:
                                $ E_Chest = "bra"
                            if "lace panties" in E_Inventory:
                                $ E_Panties = "lace panties"
                            else:
                                call SetPantiesEmma("modded black panties")
                            menu:
                                extend ""
                                "Nice.":
                                    pass
                                "I meant {i}just{/i} the nighty.":
                                    if ApprovalCheck("Emma", 1400, TabM=3):
                                        "She shrugs off her bra and then pulls the nighty back up."
                                        $ E_Panties = 0
                                        $ E_Chest = 0
                                        ch_e "Hmmm, alright. . ."
                                    elif ApprovalCheck("Emma", 1200, TabM=3):
                                        $ E_Chest = 0
                                        ch_e "I'll keep my panties on, thanks."
                                    else:
                                        ch_e "Be happy with what you get."
                        else:
                            ch_e "That's a bit . . . revealing."

        # "How about that nighty you have?" if E_Over != "nighty":
        #                 if E_Legs:
        #                     ch_e "I can't really wear that with my [E_Legs] on."
        #                     ch_p "Just take them off."
        #                     call EmmaFace("sexy", 1)
        #                     if E_SeenPanties and E_Panties and ApprovalCheck("Emma", 500, TabM=(6-Public)):
        #                         ch_e "Fine."
        #                     elif E_SeenPussy and ApprovalCheck("Emma", 900, TabM=(5-Public)):
        #                         ch_e "Fine."
        #                     elif ApprovalCheck("Emma", 1300, TabM=(2-Public)) and E_Panties:
        #                         ch_e "It's not like I haven't worn this look before. . ."
        #                     elif ApprovalCheck("Emma", 800) and not E_Panties:
        #                         call Emma_NoPantiesOn
        #                     else:
        #                         ch_e "I'm afraid not."
        #                         if not E_Panties:
        #                             ch_e "You understand, it could get. . . drafty. . ."
        #                         jump Emma_Modded_Clothes_Over
        #                     $ E_Legs = 0    
        #                     "She peels her pants off."
        #                     if E_Panties:                
        #                         $ E_SeenPanties = 1
        #                     else:
        #                         call Emma_First_Bottomless
        #                     $ E_Over = "nighty"   
        #                     if "lace bra" in E_Inventory:
        #                         $ E_Chest = "lace bra"
        #                     else:
        #                         $ E_Chest = "bra"
        #                     if "lace panties" in E_Inventory:
        #                         $ E_Panties = "lace panties"
        #                     else:
        #                         call SetPantiesEmma("modded black panties")
        #                     menu:
        #                         extend ""
        #                         "Nice.":
        #                             pass
        #                         "I meant {i}just{/i} the nighty.":
        #                             if ApprovalCheck("Emma", 1400, TabM=3):
        #                                 "She shrugs off her bra and then pulls the nighty back up."
        #                                 $ E_Panties = 0
        #                                 $ E_Chest = 0
        #                                 ch_e "Hmmm, alright. . ."
        #                             elif ApprovalCheck("Emma", 1200, TabM=3):
        #                                 $ E_Chest = 0
        #                                 ch_e "I'll keep my panties on, thanks."
        #                             else:
        #                                 ch_e "Be happy with what you get."
        #                 elif ApprovalCheck("Emma", 1100, TabM=3):
        #                     ch_e "Sure. . ."
        #                     $ E_Over = "nighty"   
        #                     if "lace bra" in E_Inventory:
        #                         $ E_Chest = "lace bra"
        #                     else:
        #                         $ E_Chest = "bra"
        #                     if "lace panties" in E_Inventory:
        #                         $ E_Panties = "lace panties"
        #                     else:
        #                         call SetPantiesEmma("modded black panties")
        #                     menu:
        #                         extend ""
        #                         "Nice.":
        #                             pass
        #                         "I meant {i}just{/i} the nighty.":
        #                             if ApprovalCheck("Emma", 1400, TabM=3):
        #                                 "She shrugs off her bra and then pulls the nighty back up."
        #                                 $ E_Panties = 0
        #                                 $ E_Chest = 0
        #                                 ch_e "Hmmm, alright. . ."
        #                             elif ApprovalCheck("Emma", 1200, TabM=3):
        #                                 $ E_Chest = 0
        #                                 ch_e "I'll keep my panties on, thanks."
        #                             else:
        #                                 ch_e "Be happy with what you get."
        #                 else:
        #                     ch_e "That's a bit . . . revealing."
                            
        "Never mind":
            pass
    jump Emma_Modded_Clothes_Menu
    #End of Emma Top
            
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Emma_Modded_Clothes_Legs:                                                                                                    # Leggings    
        "Maybe go without the pants." if PantsNum("Emma") > 5:
            call EmmaFace("sexy", 1)
            if E_SeenPanties and E_Panties and ApprovalCheck("Emma", 500, TabM=(6-Public)):
                ch_e "Fine."
            elif E_SeenPussy and ApprovalCheck("Emma", 900, TabM=(5-Public)):
                ch_e "Fine."
            elif ApprovalCheck("Emma", 1300, TabM=(2-Public)) and E_Panties:
                ch_e "It's not like I haven't worn this look before. . ."
            elif ApprovalCheck("Emma", 800) and not E_Panties:
                call Emma_NoPantiesOn
                if not _return:
                    jump Emma_Modded_Clothes_Menu
            else:
                ch_e "I'm afraid not."
                if not E_Panties:
                    ch_e "You understand, it could get. . . drafty. . ."
                jump Emma_Modded_Clothes_Menu
            $ E_Legs = 0    
            "She peels her pants off."
            if E_Panties:                
                $ E_SeenPanties = 1
            else:
                call Emma_First_Bottomless
        
        "You look great in that white skirt." if E_Legs != "skirt":
            ch_e "I know."
            $ E_Legs = "skirt"

        "You look great in those white pants." if E_Legs != "pants":
            ch_e "I know."
            $ E_Legs = "pants"

        "You look great in those black pants." if E_Legs != "modded black pants":
            ch_e "I know."
            call SetLegsEmma("modded black pants")

        "You look great in those white shorts." if E_Legs != "modded NewX":
            ch_e "I know."
            call SetLegsEmma("modded NewX")
        
        "You look great in those black shorts." if E_Legs != "modded NewX black":
            ch_e "I know."
            call SetLegsEmma("modded NewX black")

        "You look great in those white sports shorts." if E_Legs != "modded white sports shorts":
            ch_e "I know."
            call SetLegsEmma("modded white sports shorts")

        "You look great in those red sports shorts." if E_Legs != "modded red sports shorts":
            ch_e "I know."
            call SetLegsEmma("modded red sports shorts")
                
                   
        "Never mind":
            pass
    jump Emma_Modded_Clothes_Menu
    #End of Emma Pants
    
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
    
    menu Emma_Modded_Clothes_Under:                                                                                                 # Tops    
        "How about you lose the [E_Chest]?" if E_Chest:
            call EmmaFace("bemused", 1)
            if E_SeenChest and ApprovalCheck("Emma", 900, TabM=(4-Public)):
                ch_e "Of course."    
            elif ApprovalCheck("Emma", 1100, TabM=2):
                if Taboo:
                    ch_e "I'd rather not out here. . ."
                else:
                    ch_e "I suppose for you. . ."
            elif E_Over == "jacket" or E_Over == "modded black jacket" and ApprovalCheck("Emma", 700, TabM=(3-Public)):
                ch_e "This is a bit daring without anything under it. . ."  
            elif not E_Over:
                ch_e "I don't think that would be appropriate."
                jump Emma_Modded_Clothes_Menu 
            else:
                ch_e "I'm afraid not, [E_Petname]."
                jump Emma_Modded_Clothes_Menu 
            $ Line = E_Chest
            $ E_Chest = 0
            call Emma_Tits_Up
            if E_Over:
                "She reaches under her [E_Over] grabs her [Line], and pulls it out, dropping it to the ground."
            else:
                "She lets her [Line] fall to the ground."
            call Emma_First_Topless
          
        "I like that corset you have." if E_Chest != "corset":
            if E_SeenChest or ApprovalCheck("Emma", 1000, TabM=(3-Public)):
                ch_e "So do I."   
                $ E_Chest = "corset"  
                $ E_TitsUp = 1
            else:                
                ch_e "I don't think that would be appropriate. . ."  

        "I like that black corset you have." if E_Chest != "modded black corset":
            if E_SeenChest or ApprovalCheck("Emma", 1000, TabM=(3-Public)):
                ch_e "So do I."   
                call SetChestEmma("modded black corset")
                $ E_TitsUp = 1
            else:                
                ch_e "I don't think that would be appropriate. . ."    

        "I like that NewX corset you have." if E_Chest != "modded NewX":
            if E_SeenChest or ApprovalCheck("Emma", 1000, TabM=(3-Public)):
                ch_e "So do I."   
                call SetChestEmma("modded NewX")
                $ E_TitsUp = 1
            else:                
                ch_e "I don't think that would be appropriate. . ."    

        "I like that NewX black corset you have." if E_Chest != "modded NewX black":
            if E_SeenChest or ApprovalCheck("Emma", 1000, TabM=(3-Public)):
                ch_e "So do I."   
                call SetChestEmma("modded NewX black")
                $ E_TitsUp = 1
            else:                
                ch_e "I don't think that would be appropriate. . ." 

        "I like that white sports bra you have." if E_Chest != "modded white sports bra":
            if E_SeenChest or ApprovalCheck("Emma", 1000, TabM=(3-Public)):
                ch_e "So do I."   
                call SetChestEmma("modded white sports bra")
                $ E_TitsUp = 1
            else:                
                ch_e "I don't think that would be appropriate. . ."  

        "I like that red sports bra you have." if E_Chest != "modded red sports bra":
            if E_SeenChest or ApprovalCheck("Emma", 1000, TabM=(3-Public)):
                ch_e "So do I."   
                call SetChestEmma("modded red sports bra")
                $ E_TitsUp = 1
            else:                
                ch_e "I don't think that would be appropriate. . ."  

        "I like that sports bra you have." if E_Chest != "sports bra":
            if E_SeenChest or ApprovalCheck("Emma", 1000, TabM=(3-Public)):
                ch_e "So do I."   
                $ E_Chest = "sports bra"  
                $ E_TitsUp = 1
            else:                
                ch_e "I don't think that would be appropriate. . ." 

        "I like that lace bra you have." if E_Chest != "lace bra":
            if E_SeenChest or ApprovalCheck("Emma", 1200, TabM=(3-Public)):
                ch_e "So do I."   
                $ E_Chest = "lace bra"  
                $ E_TitsUp = 1
            else:                
                ch_e "I don't think that would be appropriate. . ."  

        # "I like that bikini top you have." if E_Chest != "modded bikini":
        #     if E_SeenChest or ApprovalCheck("Emma", 1000, TabM=(3-Public)):
        #         ch_e "So do I."   
        #         call SetChestEmma("modded bikini")
        #         $ E_TitsUp = 1
        #     else:                
        #         ch_e "I don't think that would be appropriate. . ."  

                                                                                                                            #Panties        
        "You could lose those panties. . ." if E_Panties:
            call EmmaFace("bemused", 1)
            if (ApprovalCheck("Emma", 900) or E_SeenPussy) and not Taboo:
                #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
                
                if ApprovalCheck("Emma", 850, "L"):               
                        ch_e "You like the view?"
                elif ApprovalCheck("Emma", 500, "O"):
                        ch_e "If you'd like."
                elif ApprovalCheck("Emma", 350, "I"):
                        ch_e "I do enjoy going without them. . ."
                else:
                        ch_e "Very well."         
            else:                       
                #low approval or not wearing pants or in public 
                if ApprovalCheck("Emma", 1100, "LI", TabM=(4-Public)) and E_Love > E_Inbt:               
                        ch_e "I don't exactly mind you seeing. . ."
                elif ApprovalCheck("Emma", 700, "OI", TabM=(4-Public)) and E_Obed > E_Inbt:
                        ch_e "I suppose I could. . ."
                elif ApprovalCheck("Emma", 600, "I", TabM=(4-Public)):
                        ch_e "Why not."
                elif ApprovalCheck("Emma", 1300, TabM=(4-Public)):
                        ch_e "Fine."
                else: 
                        call EmmaFace("surprised")
                        $ E_Brows = "angry"
                        if Taboo:
                            ch_e "I don't think I could out here, [E_Petname]!"
                        else:
                            ch_e "I could, but I won't, [E_Petname]!"
                        jump Emma_Modded_Clothes_Menu
                        
                        
            $ Line = E_Panties
            $ E_Panties = 0  
            if E_Legs:
                if Taboo or ApprovalCheck("Emma", 1100) or E_SeenPussy:
                    "She pulls off her [E_Legs] then pulls her [Line] off, droping them to the ground, before putting them back on." 
                    call Emma_First_Bottomless
                else:
                    "She asks you to turn around. After a few seconds, you turn back to her as she drops the [Line] to the ground."               
            else:
                "She pulls off her [Line] and lets them drop to the ground."
                call Emma_First_Bottomless
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2) 

        "Why don't you wear the sports panties instead?" if E_Panties and E_Panties != "sports panties":
            if ApprovalCheck("Emma", 800, TabM=(4-Public)):
                    ch_e "Ok."
                    $ E_Panties = "sports panties"  
            else:                
                    ch_e "I really don't see how that's any of your concern." 
                
        "Why don't you wear the white panties instead?" if E_Panties and E_Panties != "white panties":
            if ApprovalCheck("Emma", 1100, TabM=(4-Public)):
                    ch_e "Ok."
                    $ E_Panties = "white panties"  
            else:                
                    ch_e "I really don't see how that's any of your concern."

        "Why don't you wear the black panties instead?" if E_Panties and E_Panties != "modded black panties":
            if ApprovalCheck("Emma", 1100, TabM=(4-Public)):
                    ch_e "Ok."
                    call SetPantiesEmma("modded black panties")
            else:                
                    ch_e "I really don't see how that's any of your concern."

        # "Why don't you wear that bikini panties?" if E_Panties and E_Panties != "modded bikini":
        #     if ApprovalCheck("Emma", 1100, TabM=(4-Public)):
        #             ch_e "Ok."
        #             call SetPantiesEmma("modded bikini")
        #     else:                
        #             ch_e "I really don't see how that's any of your concern."
                
        "Why don't you wear the lace panties instead?" if "lace panties" in E_Inventory and E_Panties and E_Panties != "lace panties":
            if ApprovalCheck("Emma", 1300, TabM=(4-Public)):
                    ch_e "Fine."
                    $ E_Panties = "lace panties"
            else:
                    ch_e "I really don't see how that's any of your concern."
                
        "You know, you could wear some panties with that. . ." if not E_Panties:
            call EmmaFace("bemused", 1)
            if (E_Love+E_Obed) <= (2* E_Inbt):
                $ E_Mouth = "smile"
                ch_e "I could, but won't."
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2)
                menu:
                    "Wear them":
                        pass
                    "Ok":
                        jump Emma_Modded_Clothes_Menu
            menu:
                ch_e "If you insist. . ."
                "How about the sports ones?":
                    ch_e "Fine."
                    $ E_Panties = "sports panties"
                "How about the white ones?":
                    ch_e "Fine."
                    $ E_Panties = "white panties"
                "How about the black ones?":
                    ch_e "Fine."
                    call SetPantiesEmma("modded black panties")
                "How about the lace ones?" if "lace panties" in E_Inventory:
                    ch_e "Fine."                
                    $ E_Panties  = "lace panties"
        "Socks and Stockings": 
            
            menu Emma_Modded_Clothes_Under_Hoses:  

                "You could lose those stockings. . ." if E_Hose:
                    ch_k "Fine."
                    $ E_Hose = 0
                    jump Emma_Modded_Clothes_Under_Hoses  

                "Why don't you wear those white thigh highs?" if E_Hose != "modded white thigh high":
                    ch_k "Fine."
                    call SetHoseEmma("modded white thigh high")
                    jump Emma_Modded_Clothes_Under_Hoses

                "Why don't you wear those black thigh highs?" if E_Hose != "modded black thigh high":
                    ch_k "Fine."
                    call SetHoseEmma("modded black thigh high")
                    jump Emma_Modded_Clothes_Under_Hoses

                "Go back":  
                    jump Emma_Modded_Clothes_Under
        "Never mind":
            pass
    jump Emma_Modded_Clothes_Menu
    #End of Emma Underwear
       
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  
        
    menu Emma_Modded_Clothes_Misc:                     
    #     #Misc
    #     "Maybe lose the gloves." if E_Arms:
    #         $ E_Arms = 0
    #         ch_e "Ok."
    #     "Put your white gloves on." if E_Arms != "white gloves":
    #         $ E_Arms = "white gloves"
    #         ch_e "Ok." 
    #     "Put your black gloves on." if E_Arms != "black gloves":
    #         $ E_Arms = "black gloves"
    #         ch_e "Ok."     

        "Hair options":

            menu Emma_Modded_Clothes_Misc_Hair:

                "You look good with your hair flowing." if E_Hair != "wave":
                    if ApprovalCheck("Emma", 600):
                        ch_e "Like this?"
                        $ E_Hair = "wave"
                    else:
                        ch_e "Yes, I do."
                    jump Emma_Modded_Clothes_Misc_Hair
                        
                "Maybe keep your hair straight." if E_Hair != "wet":
                    if ApprovalCheck("Emma", 600):
                        ch_e "You think?"
                        $ E_Hair = "wet"
                    else:
                        ch_e "I tend to prefer it a bit more loose."
                    jump Emma_Modded_Clothes_Misc_Hair
        
                # "Maybe dye your hair black." if E_HairColor != "black":
                #     if ApprovalCheck("Emma", 600):
                #         ch_e "You think?"
                #         $ E_HairColor = "black"
                #     else:
                #         ch_e "I tend to prefer it the way it is."
                #     jump Emma_Modded_Clothes_Misc_Hair

                # "Maybe dye your hair red." if E_HairColor != "red":
                #     if ApprovalCheck("Emma", 600):
                #         ch_e "You think?"
                #         $ E_HairColor = "red"
                #     else:
                #         ch_e "I tend to prefer it the way it is."
                #     jump Emma_Modded_Clothes_Misc_Hair


                "Maybe dye your hair.":
                    if ApprovalCheck("Emma", 600):
                        ch_e "You think?"
                        call Recolor_Hair("Emma")
                        call SetHairColorEmma("custom")
                    else:
                        ch_e "I tend to prefer it the way it is."
                    jump Emma_Modded_Clothes_Misc_Hair

        
                "Maybe dye your hair back to blonde." if E_HairColor:
                    if ApprovalCheck("Emma", 600):
                        ch_e "You think?"
                        # $ E_HairCustomColor.red = 255
                        # $ E_HairCustomColor.green = 255
                        # $ E_HairCustomColor.blue = 255
                        call SetHairColorEmma("")
                    else:
                        ch_e "I tend to prefer it the way it is."
                    jump Emma_Modded_Clothes_Misc_Hair

                "Nevermind":
                    jump Emma_Modded_Clothes_Misc

        "Neck options":
            menu Emma_Modded_Clothes_Misc_Neck:
                "Why don't you try on that white choker." if E_Neck != "choker":
                    ch_e "Ok. . ."         
                    $ E_Neck = "choker"
                    jump Emma_Modded_Clothes_Misc_Neck
        
                "Why don't you try on that black choker." if E_Neck != "black choker":
                    ch_e "Ok. . ."         
                    call SetNeckEmma("modded black choker")
                    jump Emma_Modded_Clothes_Misc_Neck
        
                "Why don't you try on that NewX neck piece." if E_Neck != "modded NewX":
                    ch_e "Ok. . ."         
                    call SetNeckEmma("modded NewX")
                    jump Emma_Modded_Clothes_Misc_Neck
                "Why don't you try on that black NewX neck piece." if E_Neck != "modded NewX black":
                    ch_e "Ok. . ."         
                    call SetNeckEmma("modded NewX black")
                    jump Emma_Modded_Clothes_Misc_Neck
        #        "Why don't you try on that star necklace." if E_Neck != "star necklace":
        #            ch_e "Ok. . ."         
        #            $ E_Neck = "star necklace"
                "Maybe go without a collar." if E_Neck:
                    ch_e "Ok. . ."         
                    $ E_Neck = 0
                    jump Emma_Modded_Clothes_Misc_Neck
                "Nevermind":
                    jump Emma_Modded_Clothes_Misc
                        
    #     "You know, I like some nice hair down there. Maybe grow it out." if not E_Pubes and "pubes" in E_Todo:
    #         call EmmaFace("bemused", 1)
    #         ch_e "Rome wasn't built in a day. . ."
    #     "I like some hair down there." if not E_Pubes and "pubes" not in E_Todo:
    #         call EmmaFace("bemused", 1)
    #         $ Approval = ApprovalCheck("Emma", 1150, TabM=0)
    #         if ApprovalCheck("Emma", 850, "L", TabM=0) or (Approval and E_Love > 2 * E_Obed):               
    #             ch_e "If you like that sort of thing. . ."
    #         elif ApprovalCheck("Emma", 500, "I", TabM=0) or (Approval and E_Inbt > E_Obed):
    #             ch_e "I could go a bit more. . . wild."
    #         elif ApprovalCheck("Emma", 400, "O", TabM=0) or Approval:
    #             ch_e "If you insist. . ."
    #         else: 
    #             call EmmaFace("surprised")
    #             $ E_Brows = "angry"
    #             ch_e "I don't see how that's your concern, [E_Petname]."
    #             jump Emma_Modded_Clothes_Menu
    #         $ E_Todo.append("pubes")
    #         $ E_PubeC = 6
        
    #     "I like it waxed clean down there." if E_Pubes == 1:
    #         call EmmaFace("bemused", 1)
    #         if "shave" in E_Todo:
    #             ch_e "Yes, yes, it's on my schedule."
    #         else:
    #             $ Approval = ApprovalCheck("Emma", 1150, TabM=0)
                
    #             if ApprovalCheck("Emma", 850, "L", TabM=0) or (Approval and E_Love > 2 * E_Obed):               
    #                 ch_e "I know you love it."
    #             elif ApprovalCheck("Emma", 500, "I", TabM=0) or (Approval and E_Inbt > E_Obed):
    #                 ch_e "I like it kept tidy."
    #             elif ApprovalCheck("Emma", 400, "O", TabM=0) or Approval:
    #                 ch_e "If you insist."
    #             else: 
    #                 call EmmaFace("surprised")
    #                 $ E_Brows = "angry"
    #                 ch_e "I don't see how that's your concern, [E_Petname]."
    #                 jump Emma_Modded_Clothes_Menu
    #             $ E_Todo.append("shave")        
    #     "Piercings. [[See what she looks like without them first] (locked)" if not E_SeenPussy and not E_SeenChest:
    #         pass
            
    #     "You know, you'd look really nice with some ring body piercings." if E_Pierce != "ring" and (E_SeenPussy or E_SeenChest):
    #         call EmmaFace("bemused", 1)
    #         $ Approval = ApprovalCheck("Emma", 1350, TabM=0)
    #         if ApprovalCheck("Emma", 900, "L", TabM=0) or (Approval and E_Love > 2* E_Obed):   
    #                 ch_e "A little handhold, I assume?"
    #         elif ApprovalCheck("Emma", 600, "I", TabM=0) or (Approval and E_Inbt > E_Obed):
    #                 ch_e "I do like a nice ring. . ."
    #         elif ApprovalCheck("Emma", 500, "O", TabM=0) or Approval:
    #                 ch_e "I didn't know you were into that sort of thing."
    #         else: 
    #                 call EmmaFace("surprised")
    #                 $ E_Brows = "angry"
    #                 ch_e "Well, I'm just not ready for that sort of thing, [E_Petname]."
    #                 jump Emma_Modded_Clothes_Menu            
    #         $ E_Pierce = "ring"
    #         #$ E_Todo.append("ring")
        
    #     "You know, you'd look really nice with some barbell body piercings." if E_Pierce != "barbell" and (E_SeenPussy or E_SeenChest):
    #         call EmmaFace("bemused", 1)
    #         $ Approval = ApprovalCheck("Emma", 1350, TabM=0)
    #         if ApprovalCheck("Emma", 900, "L", TabM=0) or (Approval and E_Love > 2 * E_Obed): 
    #             ch_e "A little handhold, I assume?"
    #         elif ApprovalCheck("Emma", 600, "I", TabM=0) or (Approval and E_Inbt > E_Obed):
    #             ch_e "They might look nice on these. . ."
    #         elif ApprovalCheck("Emma", 500, "O", TabM=0) or Approval:
    #             ch_e "I didn't know you were into that sort of thing."
    #         else: 
    #             call EmmaFace("surprised")
    #             $ E_Brows = "angry"
    #             ch_e "Well, I'm just not ready for that sort of thing, [E_Petname]."
    #             jump Emma_Modded_Clothes_Menu                
    #         #$ E_Todo.append("barbell")
    #         $ E_Pierce = "barbell"
            
    #     "You know, you'd look better without those piercings." if E_Pierce:
    #         call EmmaFace("bemused", 1)
    #         $ Approval = ApprovalCheck("Emma", 1350, TabM=0)
    #         if ApprovalCheck("Emma", 950, "L", TabM=0) or (Approval and E_Love > E_Obed):   
    #             ch_e "If they aren't working for you. . ."
    #         elif ApprovalCheck("Emma", 700, "I", TabM=0) or (Approval and E_Inbt > E_Obed):
    #             ch_e "They were being a nuisance."
    #         elif ApprovalCheck("Emma", 600, "O", TabM=0) or Approval:
    #             ch_e "I'll remove them then."
    #         else: 
    #             call EmmaFace("surprised")
    #             $ E_Brows = "angry"
    #             ch_e "Well {i}I{/i} enjoy them."
    #             jump Emma_Modded_Clothes_Menu            
    #         $ E_Pierce = 0 


            
        "Never mind":
            pass         
    jump Emma_Modded_Clothes_Menu
    # #End of Emma Misc Wardrobe
    
return
#End Emma Wardrobe

label SetChestEmma(Outfit = "modded tape"):
    $ E_Chest = Outfit
    call Mod_Update_Emma_Image
    return

label SetOverEmma(Outfit = "modded white mesh top"):
    $ E_Over = Outfit
    call Mod_Update_Emma_Image
    return

label SetLegsEmma(Outfit = "modded black large panties"):
    $ E_Legs = Outfit
    call Mod_Update_Emma_Image
    return

label SetPantiesEmma(Outfit = "modded black large panties"):
    $ E_Panties = Outfit
    call Mod_Update_Emma_Image
    return

label SetHoseEmma(Outfit = "modded fishnet"):
    $ E_Hose = Outfit
    call Mod_Update_Emma_Image
    return

label SetNeckEmma(Outfit = "modded fishnet"):
    $ E_Neck = Outfit
    call Mod_Update_Emma_Image
    return

label SetHairColorEmma(Outfit = ""):
    $ E_HairColor = Outfit
    call Mod_Update_Emma_Image
    return

label Mod_Update_Emma_Image:
    if renpy.showing("Emma_Sprite"):
        show Emma_Sprite 
    elif renpy.showing("Emma_Doggy"):
        show Emma_Doggy 
    elif renpy.showing("Emma_Missionary"):
        show Emma_Missionary 
    elif renpy.showing("Emma_SexSprite"):
        show Emma_SexSprite   
    elif renpy.showing("Emma_BJ_Animation"):
        show Emma_BJ_Animation   
    elif renpy.showing("Emma_HJ_Animation"):
        show Emma_HJ_Animation   
    elif renpy.showing("Emma_TJ_Animation"):
        show Emma_TJ_Animation   
    return
    
init python:
    
    def IsOutfitModdedEmma(Type = "Over"):
        if Type == "Over":
            if E_Over:
                if "modded" in E_Over:
                    return 1
            else:
                return 0
        elif Type == "Chest":
            if E_Chest:
                if "modded" in E_Chest:
                    return 1
            else:
                return 0
        elif Type == "Legs":
            if E_Legs:
                if "modded" in E_Legs:
                    return 1
            else:
                return 0
        elif Type == "Panties":
            if E_Panties:
                if "modded" in E_Panties:
                    return 1
            else:
                return 0
        elif Type == "Hose":
            if E_Hose:
                if "modded" in E_Hose:
                    return 1
            else:
                return 0
        elif Type == "Neck":
            if E_Neck:
                if "modded" in E_Neck:
                    return 1
            else:
                return 0

        return 0

    def Mod_Emma_OutfitShame(Type = "Chest"):                                                                             #sets custom outfit    
  
        if Type == "Chest":
            # if R_Chest == "tank":                                              
            #     $ Count = 20
            # elif R_BodySuit == "classic uniform":
            #     $ Count = 20 
            # elif R_BodySuit == "swimsuit1":
            #     $ Count = 20
            # elif R_BodySuit == "swimsuit2":
            #     $ Count = 10
            if E_Chest == "modded black corset":  
                return 15
            elif E_Chest == "modded white sports bra":  
                return 15
            elif E_Chest == "modded red sports bra":  
                return 15
            elif E_Chest == "modded NewX":  
                return 10
            # elif E_Chest == "modded bikini":  
            #     return 15
            elif E_Chest == "modded NewX black":  
                return 10
            else:
                return 0

        if Type == "Over":
            if E_Over == "modded black jacket":                                             
                return 15
            elif E_Over == "modded black cape":
                return 20
            elif E_Over == "modded cape":
                return 20
            else:      
                return 0

        if Type == "Legs":
            if E_Legs == "modded black pants":
                return 25 
            elif E_Legs == "modded NewX":
                return 25 
            elif E_Legs == "modded NewX black":
                return 25 
            elif E_Legs == "modded white sports shorts":
                return 20 
            elif E_Legs == "modded red sports shorts":
                return 20 
            else:
                return 0  

        if Type == "Panties":
                       
            if E_Panties == "modded black panties":      #If wearing only black panties
                return 10
            # elif E_Panties == "modded bikini":      #If wearing only bikini
            #     return 15
            else:
                return 0

        return 0    


#End Rogue Wardrobe