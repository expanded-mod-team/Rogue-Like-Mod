## Laura's Clothes ///////////////////
label Laura_Modded_Clothes:
    menu:
        "Poses":
                jump Laura_Posing
        "Let me select you hair color":
            if ApprovalCheck("Laura", 700):
                ch_l "You think?"
                call Recolor_Hair("Laura")
                call SetHairColorLaura("custom")
            else:
                ch_l "I don't know, it's fine like this."
            jump Laura_Modded_Clothes

        "Apply color to pubes as well" if L_HairColor == "custom" and not L_PubesColor:
            $ L_PubesColor = 1

        "Reset pubes color" if L_PubesColor:
            $ L_PubesColor = 0
    
        "You could lose the hose." if L_Hose:     
            $ L_Hose = 0  
        "The fishnets would look good with that." if L_Hose != "modded fishnets":     
            $ L_Hose = "modded fishnets"

        "Try on that red turtleneck." if L_Over != "modded turtleneck":
            call LauraFace("bemused")
            ch_l "Yeah, ok."          
            $ L_Over = "modded turtleneck"

        "Nevermind":
            jump Laura_Clothes
            # return
    jump Laura_Modded_Clothes

# label Laura_Modded_Clothes_Misc_Hair:
#                     if ApprovalCheck("Laura", 700):
#                         ch_l "You think?"
#                         call Recolor_Hair("Laura")
#                         call SetHairColorLaura("custom")
#                     else:
#                         ch_l "I don't know, it's fine like this."
#                     jump Laura_Clothes

label SetChestLaura(Outfit = "modded tape"):
    $ L_Chest = Outfit
    call Mod_Update_Laura_Image
    return

label SetOverLaura(Outfit = "modded white mesh top"):
    $ L_Over = Outfit
    call Mod_Update_Laura_Image
    return

label SetLegsLaura(Outfit = "modded black large panties"):
    $ L_Legs = Outfit
    call Mod_Update_Laura_Image
    return

label SetPantiesLaura(Outfit = "modded black large panties"):
    $ L_Panties = Outfit
    call Mod_Update_Laura_Image
    return

label SetHoseLaura(Outfit = "modded fishnet"):
    $ L_Hose = Outfit
    call Mod_Update_Laura_Image
    return

label SetNeckLaura(Outfit = "modded fishnet"):
    $ L_Neck = Outfit
    call Mod_Update_Laura_Image
    return

label SetHairColorLaura(Outfit = ""):
    $ L_HairColor = Outfit
    call Mod_Update_Laura_Image
    return

label Mod_Update_Laura_Image:
    if renpy.showing("Laura_Sprite"):
        show Laura_Sprite 
    elif renpy.showing("Laura_Doggy"):
        show Laura_Doggy 
    elif renpy.showing("Laura_Missionary"):
        show Laura_Missionary 
    elif renpy.showing("Laura_SexSprite"):
        show Laura_SexSprite   
    elif renpy.showing("Laura_BJ_Animation"):
        show Laura_BJ_Animation   
    elif renpy.showing("Laura_HJ_Animation"):
        show Laura_HJ_Animation   
    elif renpy.showing("Laura_TJ_Animation"):
        show Laura_TJ_Animation   
    return

label Laura_Posing:
    $ TempP_Sprite = P_Sprite
    $ P_Sprite = 0
    menu Laura_Posing_Menu:
        "Body":
            call L_Pussy_Launch(0)
        # "Doggy":
        #     hide Laura_Sprite
        #     hide Laura_SexSprite
        #     hide Laura_Missionary

        #     show Laura_Doggy at SpriteLoc(StageCenter+50) zorder 150
        "Missionary":
            hide Laura_Sprite
            # hide Laura_Doggy
            # hide Laura_SexSprite

            show Laura_SexSprite zorder 150:
                pos (450,500)
        # "Cowgirl":
        #     hide Laura_Sprite
        #     hide Laura_Doggy
        #     hide Laura_Missionary

        #     show Laura_SexSprite zorder 150:
        #         pos (575,470)
        "Return":
            hide Laura_SexSprite
            # hide Laura_Doggy
            # hide Laura_Missionary
            call Laura_Hide
            call L_Pos_Reset
            $ P_Sprite = TempP_Sprite
            jump Laura_Modded_Clothes

    jump Laura_Posing_Menu
    
init python:
    
    def IsOutfitModdedLaura(Type = "Over"):
        if Type == "Over":
            if L_Over:
                if "modded" in L_Over:
                    return 1
            else:
                return 0
        elif Type == "Chest":
            if L_Chest:
                if "modded" in L_Chest:
                    return 1
            else:
                return 0
        elif Type == "Legs":
            if L_Legs:
                if "modded" in L_Legs:
                    return 1
            else:
                return 0
        elif Type == "Panties":
            if L_Panties:
                if "modded" in L_Panties:
                    return 1
            else:
                return 0
        elif Type == "Hose":
            if L_Hose:
                if "modded" in L_Hose:
                    return 1
            else:
                return 0
        elif Type == "Neck":
            if L_Neck:
                if "modded" in L_Neck:
                    return 1
            else:
                return 0

        return 0

    def Mod_Laura_OutfitShame(Type = "Chest"):                                                                             #sets custom outfit    
  
        if Type == "Chest":
            # if R_Chest == "tank":                                              
            #     $ Count = 20
            # elif R_BodySuit == "classic uniform":
            #     $ Count = 20 
            # elif R_BodySuit == "swimsuit1":
            #     $ Count = 20
            # elif R_BodySuit == "swimsuit2":
            #     $ Count = 10
            if L_Chest == "modded black corset":  
                return 15
            elif L_Chest == "modded white sports bra":  
                return 15
            elif L_Chest == "modded red sports bra":  
                return 15
            elif L_Chest == "modded NewX":  
                return 10
            # elif L_Chest == "modded bikini":  
            #     return 15
            elif L_Chest == "modded NewX black":  
                return 10
            else:
                return 0

        if Type == "Over":
            if L_Over == "modded turtleneck":                                             
                return 15
            elif L_Over == "modded black cape":
                return 20
            elif L_Over == "modded cape":
                return 20
            else:      
                return 0

        if Type == "Legs":
            if L_Legs == "modded black pants":
                return 25 
            elif L_Legs == "modded NewX":
                return 25 
            elif L_Legs == "modded NewX black":
                return 25 
            elif L_Legs == "modded white sports shorts":
                return 20 
            elif L_Legs == "modded red sports shorts":
                return 20 
            else:
                return 0  

        if Type == "Panties":
                       
            if L_Panties == "modded black panties":      #If wearing only black panties
                return 10
            # elif L_Panties == "modded bikini":      #If wearing only bikini
            #     return 15
            else:
                return 0

        return 0    


#End Rogue Wardrobe