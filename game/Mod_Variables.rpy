init python:
    class SetColor(object):
        def __init__(self, name = "Kitty", outfit = "Hair"):
            self.red = 255
            self.green = 255
            self.blue = 255
            self.tempred = 255
            self.tempgreen = 255
            self.tempblue = 255
            self.name = name
            self.outfit = outfit
        
        def set_color(self):
            return self.red, self.green, self.blue, 0
            
        def screen_loop(self):
            renpy.show_screen("recolor_screen_"+str(self.name)+"_"+str(self.outfit)) #recolor_screen_Kitty_Hair
            self.tempred = self.red
            self.tempgreen = self.green
            self.tempblue = self.blue
            while True:
                result = ui.interact()
                
                if result[0] == "apply":
                    self.red = self.tempred
                    self.green = self.tempgreen
                    self.blue = self.tempblue
                    
                if result[0] == "quit":
                    renpy.hide_screen("recolor_screen_"+str(self.name)+"_"+str(self.outfit)) #recolor_screen_Kitty_Hair
                    return

label  mod_default_Variables:
    default CheatsEnabled = 1
    default R_Tan = 0
    default R_BodySuit = 0
    default R_HairColor = ""
    default R_HairColorBangs = ""
    default R_HairTint = 0
    default R_Headband = ""
    default R_Plugged = 0
    default R_BodySuitOff = 0
    default R_Accessory = 0
    default R_DynamicTan = [0,0,0,0,0,0,0,0]  #controller, over, legs, chest, panties, hose, gloves? choker?
    default R_Glasses = ""
    default R_Boots = ""
    default K_Tan = 0
    default K_HairColor = ""
    default K_HairTint = 0
    default K_DynamicTan = [0,0,0,0,0,0,0,0]  #controller, over, legs, chest, panties, hose, gloves? choker?
    default K_Gloves = 0
    default K_Blindfold = 0
    default K_Headband = ""
    default K_Plugged = 0
    default K_Spank = 0
    default E_Tan = 0
    default E_HairColor = ""
    default E_DynamicTan = [0,0,0,0,0,0,0,0]  #controller, over, legs, chest, panties, hose, gloves? choker?
    default E_Gloves = 0
    default E_Blindfold = 0
    default E_Headband = ""
    default E_Plugged = 0
    default E_Spank = 0
    default E_LegsUp = 0

    default L_HairColor = ""
    default L_Headband = ""

    default R_Custom4 = [0,0,0,0,0,0,0,0,0,0,0]
    default R_Custom5 = [0,0,0,0,0,0,0,0,0,0,0]
    default R_Custom6 = [0,0,0,0,0,0,0,0,0,0,0]
    default R_Custom7 = [0,0,0,0,0,0,0,0,0,0,0]
    default R_Custom8 = [0,0,0,0,0,0,0,0,0,0,0]
    default R_Custom9 = [0,0,0,0,0,0,0,0,0,0,0]

    default K_Custom4 = [0,0,0,0,0,0,0,0,0,0,0]
    default K_Custom5 = [0,0,0,0,0,0,0,0,0,0,0]
    default K_Custom6 = [0,0,0,0,0,0,0,0,0,0,0]
    default K_Custom7 = [0,0,0,0,0,0,0,0,0,0,0]
    default K_Custom8 = [0,0,0,0,0,0,0,0,0,0,0]
    default K_Custom9 = [0,0,0,0,0,0,0,0,0,0,0]

    default E_Custom4 = [0,0,0,0,0,0,0,0,0,0,0]
    default E_Custom5 = [0,0,0,0,0,0,0,0,0,0,0]
    default E_Custom6 = [0,0,0,0,0,0,0,0,0,0,0]
    default E_Custom7 = [0,0,0,0,0,0,0,0,0,0,0]
    default E_Custom8 = [0,0,0,0,0,0,0,0,0,0,0]
    default E_Custom9 = [0,0,0,0,0,0,0,0,0,0,0]

    default L_Custom4 = [0,0,0,0,0,0,0,0,0,0,0]
    default L_Custom5 = [0,0,0,0,0,0,0,0,0,0,0]
    default L_Custom6 = [0,0,0,0,0,0,0,0,0,0,0]
    default L_Custom7 = [0,0,0,0,0,0,0,0,0,0,0]
    default L_Custom8 = [0,0,0,0,0,0,0,0,0,0,0]
    default L_Custom9 = [0,0,0,0,0,0,0,0,0,0,0]

    # default R_OutfitShame = [50,0,0,0,20,0,0,10,0,0,0,0,0,0,0,0,0,0,0,0,0]
    # default K_OutfitShame = [50,0,0,0,20,0,0,10,0,0,0,0,0,0,0,0,0,0,0,0,0]
    # default E_OutfitShame = [50,0,5,0,25,0,0,10,0,0,0,0,0,0,0,0,0,0,0,0,0]
    # default L_OutfitShame = [50,0,5,0,25,0,0,10,0,0,0,0,0,0,0,0,0,0,0,0,0]
    default K_tempimage = 0

    default KittyLayer_ = -10
    default Test_Desu = "alpha.png"

    default K_HairCustomColor = SetColor("Kitty","Hair")
    default E_HairCustomColor = SetColor("Emma","Hair")
    default L_HairCustomColor = SetColor("Laura","Hair")
    default R_HairCustomColor = SetColor("Rogue","Hair")
    default R_HairCustomColorBangs = SetColor("Rogue","HairBangs")
    default newgirl = {"Mystique" : Girlnew("Mystique"),    #The LikeOtherGirl attribute should be set for each new girl
                       # "Laura" : Girlnew("Laura")
                        }
    default ModdedGirls = ["Mystique"] #List with all modded girls
    default GwenStage = 0
    default P_Hands = 0

    default R_Nude = 1
    default R_Nude_Overlay = 0
    default R_NudeDay = 0
    default R_NudeCurrent_Time = 0
    default K_Nude = 1
    default K_Nude_Overlay = 0
    default K_NudeDay = 0
    default K_NudeCurrent_Time = 0
    default E_Nude = 1
    default E_Nude_Overlay = 0
    default E_NudeDay = 0
    default E_NudeCurrent_Time = 0
    default L_Nude = 1
    default L_Nude_Overlay = 0
    default L_NudeDay = 0
    default L_NudeCurrent_Time = 0

    default R_PubesColor = 0
    default K_PubesColor = 0
    default E_PubesColor = 0
    default L_PubesColor = 0

    define ch_m = Character('[newgirl[Mystique].GirlName]', color="#646dbb", image = "arrow", show_two_window=True)

    return

label  mod_Save_Version:
    
    if getattr(K_HairCustomColor, "outfit", None) == None:
        $ K_HairCustomColor = SetColor("Kitty","Hair")

    if K_Headband == 0:
        $ K_Headband = ""
        $ E_Headband = ""
        $ newgirl["Mystique"].Headband = ""

    if persistent.K_BG_HeadBand == 0:
        $ persistent.E_BG_HeadBand = ""

    if persistent.R_BG_HeadBand == 0:
        $ persistent.E_BG_HeadBand = ""

    if persistent.E_BG_HeadBand == 0:
        $ persistent.E_BG_HeadBand = ""

    if persistent.L_BG_HeadBand == 0:
        $ persistent.L_BG_HeadBand = ""


    if R_HairColor == 0:
        $ R_HairColor = ""
    if K_HairColor == 0:
        $ K_HairColor = ""
    if E_HairColor == 0:
        $ E_HairColor = ""
    if L_HairColor == 0:
        $ L_HairColor = ""



    if len(R_OutfitShame) < 21:
        $ R_OutfitShame.append(0) #[15] 16
        $ R_OutfitShame.append(0)
        $ R_OutfitShame.append(0)
        $ R_OutfitShame.append(0)
        $ R_OutfitShame.append(0)
        $ R_OutfitShame.append(0)

    if len(K_OutfitShame) < 21:
        $ K_OutfitShame.append(0) #[15] 16
        $ K_OutfitShame.append(0)
        $ K_OutfitShame.append(0)
        $ K_OutfitShame.append(0)
        $ K_OutfitShame.append(0)
        $ K_OutfitShame.append(0)

    if len(E_OutfitShame) < 21:
        $ E_OutfitShame.append(0) #[15] 16
        $ E_OutfitShame.append(0)
        $ E_OutfitShame.append(0)
        $ E_OutfitShame.append(0)
        $ E_OutfitShame.append(0)
        $ E_OutfitShame.append(0)

    if len(L_OutfitShame) < 21:
        $ L_OutfitShame.append(0) #[15] 16
        $ L_OutfitShame.append(0)
        $ L_OutfitShame.append(0)
        $ L_OutfitShame.append(0)
        $ L_OutfitShame.append(0)
        $ L_OutfitShame.append(0)
    

    return

# screen Kitty_Sprite():
        # tag Kitty_Sprite
        
        # use Kitty_Sprite zoom 0.75 
transform Transform_Kitty_BJ:
    ease 1 offset (150,80) 

screen Kitty_Test(SpriteLoc = K_SpriteLoc, zoom_ = 0.75, type = 0):
    tag Kitty_Sprite_Screen
    if type:
        frame:
            style "empty"
            at Transform_Kitty_BJ
            use Kitty_Sprite(SpriteLoc = SpriteLoc, zoom_ = zoom_)
    else:
        frame:
            style "empty"
            use Kitty_Sprite(SpriteLoc = SpriteLoc, zoom_ = zoom_)


screen Kitty_Sprite(SpriteLoc = K_SpriteLoc, zoom_ = 0.75, type = 0):
    tag Kitty_Sprite_Screen
    $ KittyLayer_ = -10
    if KittyLayer == 100:
        $ KittyLayer_ = -25
    elif KittyLayer == 75:
        $ KittyLayer_ = -50
    elif KittyLayer == 50:
        $ KittyLayer_ = -75
    elif KittyLayer == 25:
        $ KittyLayer_ = -100
    else:
        $ KittyLayer_ = -10
    zorder KittyLayer_
    frame:
        # it type:
        #     at Transform_Kitty_BJ
        style "empty"
        anchor (0.6, 0.0)
        #pos (480,960)
        xpos 435 + SpriteLoc
        ypos 50
        # zoom zoom_ #attributes marker
    # add "Kitty_Sprite" xpos Sta zoom zoom_ #attributes markergeCenter
    # add "images/" + str(Test_Desu) zoom zoom_ #attributes marker
    # fixed:
    #     xpos 480
    #     ypos 960
    #     xanchor 0.6
    #     yanchor 0.0
    # zoom zoom_ #attributes marker                                                                   
    
        add ConditionSwitch(
            "renpy.showing('Kitty_BJ_Animation')", Null(),
            "True", "Kitty_HairBack",   
            ) xpos 93 zoom zoom_ #attributes marker
        add ConditionSwitch(                                                                         
            #Arms1               
            "not Kitty_Arms and K_DynamicTan[0]", "images/KittySprite/Kitty_Sprite_T3Arms1.png",
            "not Kitty_Arms", "images/KittySprite/Kitty_Sprite_Arms1.png",
            "True", Null(),               
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(                                                                        
            "not K_DynamicTan[3] or Kitty_Arms or not K_DynamicTan[0]", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", GetModdedStringTanKitty("3", "1.png")),
            # "'modded' in K_DynamicTan[3]", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", GetModdedString("images/KittySprite/Kitty_Sprite_Chest_", K_DynamicTan[3], "1.png")),
            # "K_DynamicTan[3] == 'bikini top'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Bikini1.png"),
            # "K_DynamicTan[3] == 'lace bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Bra_Lace.png"),
            # "K_DynamicTan[3] == 'sports bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Bra_Sport.png"),
            # "K_DynamicTan[3] == 'bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Bra_Basic.png"),
            # "K_DynamicTan[3] == 'cami'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Cami1.png"),
            #"True", Null(),
            ) zoom zoom_ #attributes marker
        
        add ConditionSwitch(   
            "not K_DynamicTan[1] or Kitty_Arms or not K_DynamicTan[0]", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", GetModdedStringTanKitty("1", "1.png")),
            # "'modded' in K_DynamicTan[1]", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", GetModdedString("images/KittySprite/Kitty_Sprite_Over_", K_DynamicTan[1], "1.png")),
            # "K_DynamicTan[1] == 'pink top'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Over_Pink1.png"),
            # "K_DynamicTan[1] == 'red shirt'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Over_Crew1.png"),
            # "K_DynamicTan[1] == 'towel'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Over_Towel1.png"),
            # "True", Null(),
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(               #back of the shirt
            "not K_Over", Null(),
            "Kitty_Arms and 'modded' in K_Over and 'top' in K_Over", GetModdedString("images/KittySprite/Kitty_Sprite_Under_", K_Over, "2.png"),
            "'modded' in K_Over and 'top' in K_Over", GetModdedString("images/KittySprite/Kitty_Sprite_Under_", K_Over, "1.png"),
            "K_Over == 'pink top' and Kitty_Arms", "images/KittySprite/Kitty_Sprite_Under_Pink2.png",       #2
            "K_Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Under_Pink1.png",                  #1
            "True", Null(),               
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(                                                                         
            #body
            "Kitty_Arms and K_DynamicTan[0]", "images/KittySprite/Kitty_Sprite_T3Body_Bare2.png",               
            "Kitty_Arms", "images/KittySprite/Kitty_Sprite_Body_Bare2.png",               
            "True and K_DynamicTan[0]", "images/KittySprite/Kitty_Sprite_T3Body_Bare1.png",    
            "True", "images/KittySprite/Kitty_Sprite_Body_Bare1.png",    
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(                                                                     #body
            "not K_DynamicTan[3] or not K_DynamicTan[0]", Null(),
            "Kitty_Arms", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", GetModdedStringTanKitty("3", "2.png")),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", GetModdedStringTanKitty("3", "1.png")),
            
            # "K_DynamicTan[0] and Kitty_Arms and 'modded' in K_DynamicTan[3]", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", GetModdedString("images/KittySprite/Kitty_Sprite_Chest_", K_DynamicTan[3], "2.png")),
            # "K_DynamicTan[0] and Kitty_Arms and K_DynamicTan[3] == 'bikini top'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_Bikini2.png"),
            # "K_DynamicTan[0] and Kitty_Arms and K_DynamicTan[3] == 'cami'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_Cami2.png"),
            
            # "K_DynamicTan[0] and 'modded' in K_DynamicTan[3]", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", GetModdedString("images/KittySprite/Kitty_Sprite_Chest_", K_DynamicTan[3], "1.png")),
            # "K_DynamicTan[0] and K_DynamicTan[3] == 'lace bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Bra_Lace.png"),
            # "K_DynamicTan[0] and K_DynamicTan[3] == 'sports bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Bra_Sport.png"),
            # "K_DynamicTan[0] and K_DynamicTan[3] == 'bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Bra_Basic.png"),
            # "K_DynamicTan[0] and K_DynamicTan[3] == 'cami'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Cami1.png"),
            # "True", Null(),
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(                                                                     #body
            "not K_DynamicTan[4] or not K_DynamicTan[0]", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", GetModdedStringTanKitty("4", ".png")),
            # "K_DynamicTan[0] and 'modded' in K_DynamicTan[4]", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", GetModdedString("images/KittySprite/Kitty_Sprite_Chest_", K_DynamicTan[4], ".png")),
            # "K_DynamicTan[0] and K_DynamicTan[4] == 'bikini bottoms'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Panties_Bikini.png"),
            # "K_DynamicTan[0] and K_DynamicTan[4] == 'green panties'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Panties_Green.png"),
            # "K_DynamicTan[0] and K_DynamicTan[4] == 'lace panties'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Panties_Lace.png"),
            # "True", Null(),             
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(                                                                     #body
            "not K_DynamicTan[2] or not K_DynamicTan[0]", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", GetModdedStringTanKitty("2", ".png")),
            # "K_DynamicTan[0] and 'modded' in K_DynamicTan[2]", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", GetModdedString("images/KittySprite/Kitty_Sprite_Legs_", K_DynamicTan[2], ".png")),
            # "K_DynamicTan[0] and K_DynamicTan[2] == 'blue skirt'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Skirt.png"),
            # "K_DynamicTan[0] and K_DynamicTan[2] == 'capris'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Pants_Blue.png"),
            # "K_DynamicTan[0] and K_DynamicTan[2] == 'black jeans'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Pants_Black.png"),
            # "K_DynamicTan[0] and K_DynamicTan[2] == 'yoga pants'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Pants_Yoga.png"),  
            # "K_DynamicTan[0] and K_DynamicTan[2] == 'shorts'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Shorts.png"),            
            # "True", Null(),             
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(   
            "not K_DynamicTan[1] or not K_DynamicTan[0]", Null(),
            "Kitty_Arms", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", GetModdedStringTanKitty("1", "2.png")),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", GetModdedStringTanKitty("1", "1.png")),
            # "Kitty_Arms and K_DynamicTan[0] and 'modded' in K_DynamicTan[1]", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", GetModdedString("images/KittySprite/Kitty_Sprite_Over_", K_DynamicTan[1], "2.png")),
            # "Kitty_Arms and K_DynamicTan[0] and K_DynamicTan[1] == 'pink top'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_Over_Pink2.png"),
            # "Kitty_Arms and K_DynamicTan[0] and K_DynamicTan[1] == 'red shirt'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_Over_Crew2.png"),
            # "Kitty_Arms and K_DynamicTan[0] and K_DynamicTan[1] == 'towel'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_Over_Towel2.png"),
            # "K_DynamicTan[0] and 'modded' in K_DynamicTan[1]", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", GetModdedString("images/KittySprite/Kitty_Sprite_Over_", K_DynamicTan[1], "1.png")),
            # "K_DynamicTan[0] and K_DynamicTan[1] == 'pink top'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Over_Pink1.png"),
            # "K_DynamicTan[0] and K_DynamicTan[1] == 'red shirt'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Over_Crew1.png"),
            # "K_DynamicTan[0] and K_DynamicTan[1] == 'towel'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Over_Towel1.png"),
            # "True", Null(),
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(                                                                         #body
            "K_Pubes and K_HairColor == 'black'", "images/KittySprite/Kitty_Sprite_Body_Hair_PubesBlack.png",               
            "K_Pubes", "images/KittySprite/Kitty_Sprite_Body_Hair_Pubes.png",               
            "True", Null(),  
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(                                                                         
            #piercings bottom
            "not K_Pierce or (K_Panties and not K_PantiesDown)", Null(),                       
            "K_Pierce == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingB.png",      
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallB.png",   
            ) zoom zoom_ #attributes marker
        
        
        add ConditionSwitch(                                                                         
            #panties layer           
            "not K_Panties", Null(),               
            "not K_PantiesDown or (K_Legs and K_Legs != 'blue skirt' and not K_Upskirt)", ConditionSwitch( 
                    # if the panties aren't down. . .
                    # and she's not wearing pants that are up
                    "K_Wet", ConditionSwitch( 
                            # if they're up and wet. . .
                            "'modded' in K_Panties", GetModdedString("images/KittySprite/Kitty_Sprite_Panties_", K_Panties, "_Wet.png"),
                            "K_Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Wet.png",
                            "K_Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Wet.png",     
                            "K_Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_Wet.png", 
                            "True", Null(),     
                            ),
                    "True", ConditionSwitch( 
                            #if they're just up. . .       
                            "'modded' in K_Panties", GetModdedString("images/KittySprite/Kitty_Sprite_Panties_", K_Panties, ".png"),
                            "K_Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green.png",
                            "K_Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace.png",
                            "K_Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini.png", 
                            "True", Null(),     
                            ),    
                    ),                    
            "K_Wet", ConditionSwitch( 
                    #if wet and down. . .
                    "'modded' in K_Panties", GetModdedString("images/KittySprite/Kitty_Sprite_Panties_", K_Panties, "_Down_Wet.png"),
                    "K_Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Down_Wet.png",
                    "K_Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Down_Wet.png",
                    "K_Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_DownW.png", 
                    "True", Null(),     
                    ),
            "True", ConditionSwitch(
                    # if not wet, but down
                    "'modded' in K_Panties", GetModdedString("images/KittySprite/Kitty_Sprite_Panties_", K_Panties, "_Down.png"),
                    "K_Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Down.png",
                    "K_Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Down.png",
                    "K_Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_Down.png", 
                    "True", Null(),     
                    ),
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(                                                                         
            #Personal Wetness            
            "not K_Wet", Null(),
            "K_Legs and not K_Upskirt", Null(),   
            "K_Panties and not K_PantiesDown and K_Wet <= 1", Null(),                   
            "K_Wet == 1", ConditionSwitch( #Wet = 1
                    "K_Panties and K_PantiesDown", AlphaMask("Wet_Drip","Kitty_Drip_MaskP"),  
                    "K_Legs", AlphaMask("Wet_Drip","Kitty_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip","Kitty_Drip_Mask"), #only plays if nothing is in the way
                    ),
            "True", ConditionSwitch( #Wet = 2+
                    "K_Panties and K_PantiesDown", AlphaMask("Wet_Drip2","Kitty_Drip_MaskP"), #"Wet_Drip2",# 
                    "K_Legs", AlphaMask("Wet_Drip2","Kitty_Drip_MaskP"),
                    "K_Panties", AlphaMask("Wet_Drip","Kitty_Drip_Mask"), #"Wet_Drip2",# 
                    "True", AlphaMask("Wet_Drip2","Kitty_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ) xpos 169 ypos 420 zoom zoom_ #attributes marker
        add ConditionSwitch(                                                                         
            #wetness                    
            "K_Legs or not K_Wet", Null(),             
            "K_Panties and not K_PantiesDown and K_Wet < 2", Null(),
            "K_Panties and not K_PantiesDown", "images/KittySprite/Kitty_Sprite_Wet1.png",
            "K_Wet == 2", "images/KittySprite/Kitty_Sprite_Wet2.png",
            "True", "images/KittySprite/Kitty_Sprite_Wet1.png",
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(                                                                         
            #Spunk nethers        
            "'in' not in K_Spunk and 'anal' not in K_Spunk", Null(),
            "K_Legs and not K_Upskirt", Null(),   
            "True", ConditionSwitch( #Wet = 2+
                    "K_Panties and K_PantiesDown", AlphaMask("Spunk_Drip2","Kitty_Drip_MaskP"), #"Wet_Drip2",# 
                    "K_Legs", AlphaMask("Spunk_Drip2","Kitty_Drip_MaskP"),
                    "True", AlphaMask("Spunk_Drip2","Kitty_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ) xpos 169 ypos 420 zoom zoom_ #attributes marker
        add ConditionSwitch(                                                                        
            #pants         
            "K_Legs == 'blue skirt' and K_Upskirt", "images/KittySprite/Kitty_Sprite_Skirt_Up.png",       
            "K_Legs == 'blue skirt'", "images/KittySprite/Kitty_Sprite_Skirt.png",          
            "not K_Legs", Null(),
            "K_Upskirt and 'modded' in K_Legs", GetModdedString("images/KittySprite/Kitty_Sprite_Legs_", K_Legs, "_Down.png"),
            "K_Wet and 'modded' in K_Legs", GetModdedString("images/KittySprite/Kitty_Sprite_Legs_", K_Legs, "_Wet.png"),
            "'modded' in K_Legs", GetModdedString("images/KittySprite/Kitty_Sprite_Legs_", K_Legs, ".png"),
            "not K_Legs or K_Upskirt", Null(),
            #"'modded' in K_Legs and K_Upskirt", GetModdedString("images/KittySprite/Kitty_Sprite_Legs", K_Legs, ".png"),
            "K_Legs == 'capris'", "images/KittySprite/Kitty_Sprite_Pants_Blue.png",
            "K_Legs == 'black jeans'", "images/KittySprite/Kitty_Sprite_Pants_Black.png",
            "K_Wet and K_Legs == 'yoga pants'", "images/KittySprite/Kitty_Sprite_Pants_Yoga_Wet.png",   
            "K_Legs == 'yoga pants'", "images/KittySprite/Kitty_Sprite_Pants_Yoga.png",   
            "K_Wet and K_Legs == 'shorts'", "images/KittySprite/Kitty_Sprite_Shorts_Wet.png",    
            "K_Legs == 'shorts'", "images/KittySprite/Kitty_Sprite_Shorts.png",            
            "True", Null(),
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(                                                                         
            #Arms2               
            "Kitty_Arms and K_DynamicTan[0]", "images/KittySprite/Kitty_Sprite_T3Arms2.png",
            "Kitty_Arms", "images/KittySprite/Kitty_Sprite_Arms2.png",
            "True", Null(),               
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(                                                                         #Arms2               
            "not K_DynamicTan[3] or not K_DynamicTan[0] or not Kitty_Arms", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Arms2.png", GetModdedStringTanKitty("3", "2.png")),
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(   
            "not K_DynamicTan[1] or not K_DynamicTan[0] or not Kitty_Arms", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Arms2.png", GetModdedStringTanKitty("1", "2.png")),
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(                                                                         #chest
            "True and K_DynamicTan[0]", "images/KittySprite/Kitty_Sprite_T3chest_bare.png",
            "True", "images/KittySprite/Kitty_Sprite_Chest_Bare.png",
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(                                                                     #body
            "not K_DynamicTan[3] or not K_DynamicTan[0]", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Chest_Bare.png", GetModdedStringTanKitty("3", "1.png")),
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(   
            "not K_DynamicTan[1] or not K_DynamicTan[0]", Null(),
            "True", AlphaMask("images/KittySprite/Kitty_Sprite_Chest_Bare.png", GetModdedStringTanKitty("1", "1.png")),
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(   
            #piercings top
            "not K_Pierce", Null(),                       
            "K_Pierce == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingT.png",      
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallT.png",   
            ) zoom zoom_ #attributes marker
        
        add ConditionSwitch(                                                                        
            #necklace
            "K_Neck == 'gold necklace'", "images/KittySprite/Kitty_Sprite_Necklace1.png",
            "K_Neck == 'star necklace'", "images/KittySprite/Kitty_Sprite_Necklace2.png",
            "True", Null(),
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(                                                                         
            #bra layer           
            "not K_Chest", Null(),                  
            "not K_Uptop", ConditionSwitch( 
                    #if the top's down. . .
                    "Kitty_Arms and 'modded' in K_Chest", GetModdedString("images/KittySprite/Kitty_Sprite_Chest_", K_Chest, "2.png"),
                    "'modded' in K_Chest", GetModdedString("images/KittySprite/Kitty_Sprite_Chest_", K_Chest, "1.png"),
                    "Kitty_Arms and K_Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami2.png",
                    "Kitty_Arms and K_Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini2.png",
                    "K_Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini1.png",
                    "K_Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace.png",
                    "K_Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport.png",
                    "K_Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic.png",
                    "K_Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1.png",
                    "True", Null(),     
                    ),
            "K_Over", ConditionSwitch(
                    # If she's wearing a shirt over the bra                        
                    "K_Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini1_Up.png",
                    "K_Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace1_UpS.png",
                    "K_Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport1_UpS.png",
                    "K_Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic1_Up.png",
                    "K_Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1_UpS.png",    
                    "True", Null(),     
                    ),
            "True", ConditionSwitch(
                    # if she's not wearing a shirt
                    "Kitty_Arms", ConditionSwitch(
                            # if Arms 2
                            "K_Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini2_Up.png",
                            "K_Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace2_Up.png",
                            "K_Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport2_Up.png",
                            "K_Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic2_Up.png",
                            "K_Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami2_Up.png",            
                            "True", Null(),     
                            ),                    
                    "True", ConditionSwitch(
                            # if Arms 1
                            "K_Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini1_Up.png",
                            "K_Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace1_Up.png",
                            "K_Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport1_Up.png",
                            "K_Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic1_Up.png",
                            "K_Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1_Up.png",            
                            "True", Null(),     
                            ),            
                    "True", Null(),     
                    ),
            ) zoom zoom_ #attributes marker
            
        add ConditionSwitch(                                                                        
            #piercings over shirt
            "not K_Pierce or not K_Chest or K_Uptop", Null(),                       
            "K_Pierce == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingOver.png",      
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallOver.png",   
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(                                                                        
            #wet look
            "K_Water and Kitty_Arms", "images/KittySprite/Kitty_Sprite_Water2.png",
            "K_Water", "images/KittySprite/Kitty_Sprite_Water1.png",
            "True", Null(),
            ) zoom zoom_ #attributes marker
        
                   
        add ConditionSwitch(                                                                         
            #shirt layer           
            "not K_Over", Null(),                  
            "not K_Uptop", ConditionSwitch( 
                    #if the top's down. . .
                    "Kitty_Arms and 'modded' in K_Over", GetModdedString("images/KittySprite/Kitty_Sprite_Over_", K_Over, "2.png"),
                    "'modded' in K_Over", GetModdedString("images/KittySprite/Kitty_Sprite_Over_", K_Over, "1.png"),
                    "Kitty_Arms and K_Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink2.png",
                    "Kitty_Arms and K_Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew2.png",
                    "Kitty_Arms and K_Over == 'towel'", "images/KittySprite/Kitty_Sprite_Over_Towel2.png",
                    "K_Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink1.png",
                    "K_Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew1.png",
                    "K_Over == 'towel'", "images/KittySprite/Kitty_Sprite_Over_Towel1.png",
                    "True", Null(),     
                    ),            
            "True", ConditionSwitch(
                    # if she's not wearing a shirt                    
                    "Kitty_Arms and K_Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink2_Up.png",
                    "Kitty_Arms and K_Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew2_Up.png",
                    "K_Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink1_Up.png",
                    "K_Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew1_Up.png",            
                    "True", Null(),     
                    ),
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(                                                                         
            #bra over shirt layer           
            "not K_Over or not K_Chest or not K_Uptop", Null(),   
            "K_Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami_Over.png", 
            "K_Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace_Over.png",
            "K_Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport_Over.png",
            "K_Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic_Over.png",
            "K_Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini_Over.png",
            "True", Null(),  
            ) zoom zoom_ #attributes marker
            
        add ConditionSwitch(
            "renpy.showing('Kitty_BJ_Animation')", Null(),
            "True", "Kitty_Head",   
            ) xpos 93 zoom zoom_ #attributes marker
        add ConditionSwitch(                                                                        
            #anal spunk
            "K_Legs and not K_Upskirt", Null(), 
            "K_Panties and not K_PantiesDown", Null(), 
            "'anal' in K_Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Anal.png",
            "True", Null(), 
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(                                                                        
            #pussy spunk
            "K_Legs and not K_Upskirt", Null(), 
            "K_Panties and not K_PantiesDown", Null(), 
            "'in' in K_Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Pussy.png",
            "True", Null(), 
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(                                                                         
            #belly spunk
            "'belly' in K_Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Belly.png",
            "True", Null(), 
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(                                                                         
            #tits spunk
            "'tits' in K_Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Tits.png",
            "True", Null(), 
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(
            #UI tool for When Kitty is masturbating using Trigger3 actions
            "Trigger == 'lesbian' or not Trigger3 or Ch_Focus != 'Kitty'", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and K_Lust >= 70", "GirlFingerPussy_K",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_K",            
            "Trigger3 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeLeftBreast_K",    #When zero is working the right breast, fondle left
            "Trigger3 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeRightBreast_K", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts'", "GirlGropeRightBreast_K",
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast_K",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy_K",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy_K",
            "Trigger3 == 'vibrator anal'", "VibratorAnal_K",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy_K",            
            "True", Null(),             
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(  
            #UI tool for Trigger5(Threesome masutrbation) actions
            "not Trigger5 or Trigger4 != 'masturbation' or Ch_Focus == 'Kitty'", Null(), 
            #this doesn't activate unless Kitty is not primary, and actively masturbating
            "Trigger5 == 'fondle pussy' and Trigger != 'sex' and K_Lust >= 70", "GirlFingerPussy_K",
            "Trigger5 == 'fondle pussy'", "GirlGropePussy_K",
            "Trigger5 == 'fondle breasts'", "GirlGropeRightBreast_K",
            "Trigger5 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger5 == 'vibrator pussy'", "VibratorPussy",
            "Trigger5 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger5 == 'vibrator anal'", "VibratorAnal",
            "Trigger5 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(), 
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(                
            #UI tool for Trigger1(primary) actions
            "not Trigger or Ch_Focus != 'Kitty'", Null(),
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast_K",
            "Trigger == 'fondle thighs'", "GropeThigh_K",
            "Trigger == 'fondle breasts'", "GropeLeftBreast_K",
            "Trigger == 'suck breasts'", "LickRightBreast_K",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_K",
            "Trigger == 'fondle pussy'", "GropePussy_K",
            "Trigger == 'lick pussy'", "Lickpussy_K",
            "Trigger == 'vibrator pussy'", "VibratorPussy_K",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy_K",
            "Trigger == 'vibrator anal'", "VibratorAnal_K",
            "Trigger == 'vibrator anal insert'", "VibratorPussy_K",
            "True", Null(), 
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(                
            #UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus != 'Kitty'", Null(),
            "not Trigger2 and not Trigger4 and Trigger == 'fondle breasts'", "GropeRightBreast_K",        
            #When doing nothing offhand, use both hands on breasts.
            "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast_K",            
            #When sucking right breast, fondle left
            "Trigger2 == 'fondle breasts'", "GropeRightBreast_K",
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast_K",       
            #When sucking right breast, vibrator left
            "Trigger2 == Trigger", Null(),
            #When both triggers are the same, do nothing              
            "Trigger2 == 'suck breasts'", "LickLeftBreast_K",        
            "Trigger2 == 'fondle pussy'", "GropePussy_K",
            "Trigger2 == 'lick pussy'", "Lickpussy_K",       
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast_K",
            "Trigger2 == 'vibrator pussy'", "VibratorPussy_K",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy_K",
            "Trigger2 == 'vibrator anal'", "VibratorAnal_K",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy_K",
            "True", Null(), 
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(  
            #UI tool for Trigger4(Threesome) actions (ie Rogue's hand on her)
            "not Trigger4 or Ch_Focus != 'Kitty'", Null(),
            "Trigger4 == 'fondle pussy' and Trigger != 'sex' and K_Lust >= 70", "GirlFingerPussy_K",
            "Trigger4 == 'fondle pussy'", "GirlGropePussy_K",            
            "Trigger4 == 'lick pussy'", "Lickpussy_K",
            "Trigger4 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_K", 
            "Trigger4 == 'suck breasts'", "LickRightBreast_K",  
            "Trigger4 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_K",    #When zero is working the right breast, fondle left
            "Trigger4 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_K", #When zero is working the left breast, fondle right  
            "Trigger4 == 'fondle breasts' and (Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts')", "GirlGropeLeftBreast_K", #When zero is working the left breast, fondle right  
            "Trigger4 == 'fondle breasts'", "GirlGropeRightBreast_K",
            "Trigger4 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger4 == 'vibrator pussy'", "VibratorPussy",
            "Trigger4 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger4 == 'vibrator anal'", "VibratorAnal",
            "Trigger4 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),             
            ) zoom zoom_ #attributes marker
        add ConditionSwitch(  
            #UI tool for Trigger3(lesbian) actions (ie Rogue's hand on her when Kitty is secondary)
            "Trigger != 'lesbian' or not Trigger3 or Ch_Focus == 'Kitty'", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and K_Lust >= 70", "GirlFingerPussy_K",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_K",            
            "Trigger3 == 'lick pussy'", "Lickpussy_K",
            "Trigger3 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_K", 
            "Trigger3 == 'suck breasts'", "LickRightBreast_K",  
            "Trigger3 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_K",    #When zero is working the right breast, fondle left
            "Trigger3 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_K", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts' and (Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts')", "GirlGropeLeftBreast_K", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts'", "GirlGropeRightBreast_K",
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger3 == 'vibrator anal'", "VibratorAnal",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),             
            ) zoom zoom_ #attributes marker
        # anchor (0.6, 0.0)
                #              
    

screen Rogue():
    tag Rogue
    if RogueLayer == 100:
        $ RogueLayer_ = -25
    elif RogueLayer == 75:
        $ RogueLayer_ = -50
    elif RogueLayer == 50:
        $ RogueLayer_ = -75
    elif RogueLayer == 25:
        $ RogueLayer_ = -100
    else:
        $ RogueLayer_ = -10
    zorder RogueLayer_
    frame:
        style "empty"
        anchor (0.6, 0.0)
        #pos (480,960)
        xpos 435 + R_SpriteLoc
        ypos 50


        
        add ConditionSwitch(                                                                         
            #back of hair
            "renpy.showing('Rogue_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Rogue_TJ_Animation')", Null(),
            "R_Hair == 'evo' and R_Water", Null(),
            "R_Hair == 'evo'", "images/RogueSprite/Rogue_hair_evo_back.png",
            "True", Null(),
            ) zoom zoom_
        add ConditionSwitch(                                                                         
            #shirt layer           
            "not R_Over", Null(),    
            "'modded' in R_Over and 'hoodie' in R_Over", GetModdedString("images/RogueSprite/Rogue_over_", R_Over, "B.png"),
            "R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodieB.png",         
            "R_Uptop", ConditionSwitch( 
                    #if the top's down. . .
                    "Rogue_Arms == 1", ConditionSwitch( 
                            #if the arms are down. . .
                            "R_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh1_Up.png",           
                            #"R_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink1_Up.png",
                            #"R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie1_Up.png",
                            "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty_Up.png",
                            #"R_Over == 'towel'", Null(), 
                            "True", Null(),     
                            ),  
                    "True", ConditionSwitch( 
                            #if the arms are up. . .
                            "R_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh2_Up.png", 
                            #"R_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink2_Up.png",
                            #"R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie2_Up.png",
                            "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty_Up.png",
                            #"R_Over == 'towel'", Null(),       
                            "True", Null(),     
                            ),       
                    ),            
            "True", ConditionSwitch(
                    #if the top's up. . .
                    "Rogue_Arms == 1", ConditionSwitch( 
                            #if the arms are down. . .
                            "'modded' in R_Over and 'mesh top' in R_Over", GetModdedString("images/RogueSprite/Rogue_over_", R_Over, "1.png"),
                            "R_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh1.png",           
                            #"R_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink1.png",
                            #"R_Over == 'towel'", "images/RogueSprite/Rogue_over_towel1.png",
                            "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty1.png",
                            #"R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie1.png",
                            "True", Null(),     
                            ),  
                    "True", ConditionSwitch( 
                            #if the arms are up. . .
                            "'modded' in R_Over and 'mesh top' in R_Over", GetModdedString("images/RogueSprite/Rogue_over_", R_Over, "2.png"),
                            "R_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh2.png", 
                            #"R_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink2.png",
                            #"R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie2.png",
                            "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty2.png",
                            #"R_Over == 'towel'", "images/RogueSprite/Rogue_over_towel2.png",      
                            "True", Null(),     
                            ),       
                    ),       
            ) zoom zoom_
        add ConditionSwitch(                                                                         
            #body 
            "R_Pubes and R_Pierce == 'ring'", "images/RogueSprite/Rogue_bodyhaired_ring.png",
            "R_Pubes and R_Pierce == 'barbell'", "images/RogueSprite/Rogue_bodyhaired_barbell.png",
            "R_Pierce == 'ring'", "images/RogueSprite/Rogue_body_ring.png",            
            "R_Pierce == 'barbell'", "images/RogueSprite/Rogue_body_barbell.png",
            "R_Pubes", "images/RogueSprite/Rogue_bodyhaired_bare.png",   
            "True", "images/RogueSprite/Rogue_body_bare.png",         
            ) zoom zoom_
        add ConditionSwitch(                                                                         
            #head 
            "renpy.showing('Rogue_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Rogue_TJ_Animation')", Null(),
            "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_head_evowet.png",
            "R_Hair == 'evo' and R_Blush == 2", "images/RogueSprite/Rogue_head_evo_blush2.png",
            "R_Hair == 'evo' and R_Blush", "images/RogueSprite/Rogue_head_evo_blush.png",
            "R_Hair == 'evo'", "images/RogueSprite/Rogue_head_evo.png",
            "True", "images/RogueSprite/Rogue_head_evo.png",
            ) zoom zoom_
        add ConditionSwitch(                                                                         
            #pants backing/hose    
            "R_Hose == 'stockings'", "images/RogueSprite/Rogue_hose.png",     
            "R_Legs == 'pants' and R_Upskirt", "images/RogueSprite/Rogue_pantsback.png", 
            "True", Null(), 
            ) zoom zoom_
        #add ConditionSwitch(                                                                         
        #    #Panties            
        #    "not R_Panties", Null(),
        #    "R_Legs == 'pants' and not R_Upskirt", "images/RogueSprite/Rogue_panties.png",             
        #    "R_Panties == 'shorts' and R_PantiesDown and R_Wet > 1", "images/RogueSprite/Rogue_shorts_down_wet.png",
        #    "R_Panties == 'shorts' and R_PantiesDown", "images/RogueSprite/Rogue_shorts_down.png",  
        #    "R_Panties == 'shorts' and R_Wet > 1", "images/RogueSprite/Rogue_shorts_wet.png",          
        #    "R_Panties == 'shorts'", "images/RogueSprite/Rogue_shorts.png",
        #    "R_Panties == 'green panties' and R_PantiesDown and R_Wet > 1", "images/RogueSprite/Rogue_undies_down_wet.png",
        #    "R_Panties == 'green panties' and R_PantiesDown", "images/RogueSprite/Rogue_undies_down.png",  
        #    "R_Panties == 'green panties' and R_Wet > 1", "images/RogueSprite/Rogue_undies_wet.png",          
        #    "R_Panties == 'green panties'", "images/RogueSprite/Rogue_undies.png",
        #    "R_Panties and R_PantiesDown", "images/RogueSprite/Rogue_panties_down.png",      
        #    "R_Panties == 'lace panties'", "images/RogueSprite/Rogue_lacepanties.png",         
        #    "True", "images/RogueSprite/Rogue_panties.png",            
        #    ) zoom zoom_
        add ConditionSwitch(                                                                         
            #panties           
            "not R_Panties", Null(),     
            "R_Legs == 'pants' and not R_Upskirt", "images/RogueSprite/Rogue_panties.png",          
            "R_PantiesDown", ConditionSwitch( 
                    #if the panties's down. . .
                    "R_Wet > 1", ConditionSwitch( 
                            #if the panties's are wet. . .
                            "'modded' in R_Panties", GetModdedString("images/RogueSprite/Rogue_panties_", R_Panties, "_down_wet.png"),
                            "R_Panties == 'shorts'", "images/RogueSprite/Rogue_shorts_down_wet.png",
                            "R_Panties == 'green panties'", "images/RogueSprite/Rogue_undies_down_wet.png",
                            "R_Panties == 'bikini bottoms'", "images/RogueSprite/Rogue_panties_bikini_down.png",  
                            "True", "images/RogueSprite/Rogue_panties_down.png", 
                            ),    
                    "True", ConditionSwitch( 
                            #if the panties's are not wet. . .
                            "'modded' in R_Panties", GetModdedString("images/RogueSprite/Rogue_panties_", R_Panties, "_down.png"),
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
                            "'modded' in R_Panties", GetModdedString("images/RogueSprite/Rogue_panties_", R_Panties, "_wet.png"),
                            "R_Panties == 'shorts' and R_Wet > 1", "images/RogueSprite/Rogue_shorts_wet.png",     
                            "R_Panties == 'green panties' and R_Wet > 1", "images/RogueSprite/Rogue_undies_wet.png",     
                            "R_Panties == 'lace panties'", "images/RogueSprite/Rogue_lacepanties.png",    
                            "R_Panties == 'bikini bottoms'", "images/RogueSprite/Rogue_panties_bikini.png",       
                            "True", "images/RogueSprite/Rogue_panties.png",     
                            ),    
                    "True", ConditionSwitch( 
                            #if the panties's are not wet. . .     
                            #modded
                            #"R_Panties[:6] == 'modded'", GetModdedString("images/RogueSprite/Rogue_panties_", R_Panties, ".png"),
                            "'modded' in R_Panties", GetModdedString("images/RogueSprite/Rogue_panties_", R_Panties, ".png"),
                            #"R_Panties[:6] == 'modded'", "images/RogueSprite/Rogue_panties_" + R_Panties + ".png",
                            #"'modded' in R_Panties", "images/RogueSprite/Rogue_panties_" + R_Panties + ".png",
                            "R_Panties == 'shorts'", "images/RogueSprite/Rogue_shorts.png",       
                            "R_Panties == 'green panties'", "images/RogueSprite/Rogue_undies.png",   
                            "R_Panties == 'lace panties'", "images/RogueSprite/Rogue_lacepanties.png",   
                            "R_Panties == 'bikini bottoms'", "images/RogueSprite/Rogue_panties_bikini.png",       
                            "True", "images/RogueSprite/Rogue_panties.png",         
                            ),    
                    ),       
            ) zoom zoom_
        add ConditionSwitch(                                                                         
            #full hose/tights              
            "not R_Hose", Null(),
            "'modded' in R_Hose", GetModdedString("images/RogueSprite/Rogue_hose_", R_Hose, ".png"),
            "R_Panties and R_PantiesDown", Null(), 
            "R_Hose == 'stockings and garterbelt'", "images/RogueSprite/Rogue_hose_garter.png",  
            "R_Hose == 'garterbelt'", "images/RogueSprite/Rogue_garters.png",                 
            "R_Hose == 'pantyhose'", "images/RogueSprite/Rogue_hosefull.png",       
            "R_Hose == 'tights' and R_Wet", "images/RogueSprite/Rogue_tights_wet.png",
            "R_Hose == 'tights'", "images/RogueSprite/Rogue_tights.png",
            "R_Hose == 'ripped pantyhose'", "images/RogueSprite/Rogue_hose_holed.png", 
            "R_Hose == 'ripped tights'", "images/RogueSprite/Rogue_tights_holed.png",   
            "True", Null(), 
            ) zoom zoom_
        add ConditionSwitch(                                                                         
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
            ) xpos 180 ypos 420 zoom zoom_
        add ConditionSwitch(                                                                         
            #Personal Wetness            
            "not R_Wet", Null(),
            "R_Legs and R_Wet <= 1", Null(),
            "R_Legs", "images/RogueSprite/Rogue_wet.png",
            "R_Wet == 1", "images/RogueSprite/Rogue_wet.png",
            "True", "images/RogueSprite/Rogue_wet2.png",       #R_Wet >1
            ) zoom zoom_
        add ConditionSwitch(                                                                         
            #Spunk nethers        
            "'in' not in R_Spunk and 'anal' not in R_Spunk", Null(),
            "R_Legs == 'pants' and not R_Upskirt", Null(),   
            "True", ConditionSwitch( #Wet = 2+
                    "R_Panties and R_PantiesDown", AlphaMask("Spunk_Drip2","Rogue_Drip_MaskP"), #"Wet_Drip2",# 
                    "R_Panties and R_Legs == 'pants'", AlphaMask("Spunk_Drip","Rogue_Drip_MaskPn"), #"Wet_Drip2",# 
                    "R_Legs == 'pants'", AlphaMask("Spunk_Drip2","Rogue_Drip_MaskPn"),
                    "True", AlphaMask("Spunk_Drip2","Rogue_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ) xpos 180 ypos 420 zoom zoom_
        #add ConditionSwitch(                                                                         
        #    #Spunk Nethers over          
        #    "'in' not in R_Spunk and 'anal' not in R_Spunk", Null(),
        #    "R_Legs == 'pants' and not R_Upskirt", Null(),   
        #    "R_Panties and not R_PantiesDown", Null(),     
        #    "True", "images/RogueSprite/Rogue_wet2.png",       #R_Wet >1
        #    ) zoom zoom_
        add ConditionSwitch(                                                                         
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
            ) zoom zoom_
        #add ConditionSwitch(                                                                         
        #    #Blush
        #    "R_Blush", "images/RogueSprite/Rogue_blush.png",
        #    "True", Null(), 
        #    ) zoom zoom_
        add ConditionSwitch(                                                                         
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
            ) zoom zoom_
        add "Rogue Blink" zoom zoom_                                                                           
            #Eyes
            
        add ConditionSwitch(                                                                         
            #Pants and Skirts
            "not R_Legs", Null(),
            "'modded' in R_Legs and R_Upskirt", GetModdedString("images/RogueSprite/Rogue_legs_", R_Legs, "_up.png"),
            "'modded' in R_Legs", GetModdedString("images/RogueSprite/Rogue_legs_", R_Legs, ".png"),
            "R_Legs == 'pants' and R_Upskirt", "images/RogueSprite/Rogue_legs_pants_down.png", 
            "R_Legs == 'pants'", "images/RogueSprite/Rogue_legs_pants.png",          
            "R_Legs == 'skirt' and R_Upskirt", "images/RogueSprite/Rogue_legs_skirt_up.png",
            "R_Legs == 'skirt'", "images/RogueSprite/Rogue_legs_skirt.png",          
            "True", Null(),   
            ) zoom zoom_
        add ConditionSwitch(                                                                        
            #Arms and gloves
            "Rogue_Arms == 1 and R_Arms == 'gloved' and R_Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms1a_gloved.png",       #Gloves and collar 
            "Rogue_Arms == 1 and R_Arms == 'gloved'", "images/RogueSprite/Rogue_arms1b_gloved.png",                                     #Gloves, no collar
            "Rogue_Arms == 1 and R_Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms1a_bare.png",                                #No Gloves, collar 
            "Rogue_Arms == 1", "images/RogueSprite/Rogue_arms1b_bare.png",                                                              #No gloves, no collar
            "R_Arms == 'gloved' and R_Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms2a_gloved.png",                           #Gloves and collar 
            "R_Arms == 'gloved'", "images/RogueSprite/Rogue_arms2b_gloved.png",                                                         #Gloved, no collar
            "R_Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms2a_bare.png",                                                    #No gloves, collar
            "True", "images/RogueSprite/Rogue_arms2b_bare.png",    
            ) zoom zoom_
        add ConditionSwitch(                                                                         
            #chest layer
            "R_Pierce == 'barbell'", "images/RogueSprite/Rogue_chest_barbell.png",            
            "R_Pierce == 'ring'", "images/RogueSprite/Rogue_chest_rings.png",      
            "True", "images/RogueSprite/Rogue_chest_bare.png",    
            ) zoom zoom_
        #add ConditionSwitch(                                                                         
        #    #chest clothes layer
        #    "R_Chest == 'tank'", "images/RogueSprite/Rogue_chest_tank.png",
        #    "R_Chest == 'buttoned tank'", "images/RogueSprite/Rogue_chest_tank2.png",            
        #    "R_Chest == 'bra'", "images/RogueSprite/Rogue_chest_bra.png",                         
        #    "R_Chest == 'sports bra'", "images/RogueSprite/Rogue_chest_sportsbra.png",
        #    "R_Chest == 'lace bra'", "images/RogueSprite/Rogue_chest_lacebra.png",  
        #    "True", Null(),               
        #    ) zoom zoom_
        add ConditionSwitch(                                                                         
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
                    "True", Null(),    
                    ),            
            "True", ConditionSwitch(
                    #if the top's up. . .
                    "'modded' in R_Chest and 'crop top' in R_Chest", ConditionSwitch(
                        "Rogue_Arms == 1", GetModdedString("images/RogueSprite/Rogue_chest_", R_Chest, "1.png"),
                        "True", GetModdedString("images/RogueSprite/Rogue_chest_", R_Chest, "2.png"),
                        ),
                    "'modded' in R_Chest", GetModdedString("images/RogueSprite/Rogue_chest_", R_Chest, ".png"),
                    "R_Chest == 'tank'", "images/RogueSprite/Rogue_chest_tank.png",
                    "R_Chest == 'buttoned tank'", "images/RogueSprite/Rogue_chest_tank2.png",            
                    "R_Chest == 'bra'", "images/RogueSprite/Rogue_chest_bra.png",                         
                    "R_Chest == 'sports bra'", "images/RogueSprite/Rogue_chest_sportsbra.png",
                    "R_Chest == 'lace bra'", "images/RogueSprite/Rogue_chest_lacebra.png",        
                    "R_Chest == 'bikini top'", "images/RogueSprite/Rogue_chest_bikini.png",          
                    "True", Null(),    
                    ),       
            ) zoom zoom_
        add ConditionSwitch(                                                                         
            #water
            "R_Water and Rogue_Arms == 1", "images/RogueSprite/Rogue_body_wet1.png",
            "R_Water", "images/RogueSprite/Rogue_body_wet2.png",
            "True", Null(),                 
            ) zoom zoom_
        add ConditionSwitch(                                                                         
            #soap
            "R_Water == 3", "images/RogueSprite/Rogue_body_wet3.png",
            "True", Null(),                 
            ) zoom zoom_
        #add ConditionSwitch(                                                                         
        #    #Overshirt layer
        #    "Rogue_Arms == 1 and R_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh1.png",           
        #    "Rogue_Arms == 1 and R_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink1.png",
        #    "Rogue_Arms == 1 and R_Over == 'towel'", "images/RogueSprite/Rogue_over_towel1.png",
        #    "Rogue_Arms == 1 and R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty1.png",
        #    "Rogue_Arms == 1 and R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie1.png",
        #    "R_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh2.png", 
        #    "R_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink2.png",
        #    "R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie2.png",
        #    "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty2.png",
        #    "R_Over == 'towel'", "images/RogueSprite/Rogue_over_towel2.png",              
        #    "True", Null(), 
        #    ) zoom zoom_
            
        add ConditionSwitch(                                                                         
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
                            #"R_Over == 'towel'", Null(), 
                            "True", Null(),     
                            ),  
                    "True", ConditionSwitch( 
                            #if the arms are up. . .
                            "R_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh2_Up.png", 
                            "R_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink2_Up.png",
                            "R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie2_Up.png",
                            "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty_Up.png",
                            #"R_Over == 'towel'", Null(),       
                            "True", Null(),     
                            ),       
                    ),            
            "True", ConditionSwitch(
                    #if the top's up. . .
                    "Rogue_Arms == 1", ConditionSwitch( 
                            #if the arms are down. . .
                            "'modded' in R_Over", GetModdedString("images/RogueSprite/Rogue_over_", R_Over, "1.png"),
                            "R_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh1.png",           
                            "R_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink1.png",
                            "R_Over == 'towel'", "images/RogueSprite/Rogue_over_towel1.png",
                            "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty1.png",
                            "R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie1.png",
                            "True", Null(),     
                            ),  
                    "True", ConditionSwitch( 
                            #if the arms are up. . .
                            "'modded' in R_Over", GetModdedString("images/RogueSprite/Rogue_over_", R_Over, "2.png"),
                            "R_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh2.png", 
                            "R_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink2.png",
                            "R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie2.png",
                            "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty2.png",
                            "R_Over == 'towel'", "images/RogueSprite/Rogue_over_towel2.png",      
                            "True", Null(),     
                            ),       
                    ),       
            ) zoom zoom_
        add ConditionSwitch(                                                                         
            #Hair
            "renpy.showing('Rogue_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Rogue_TJ_Animation')", Null(),
            "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_hair_wet.png",
            "R_Hair == 'evo'", "images/RogueSprite/Rogue_hair_evo.png",
            "True", Null(), 
            ) zoom zoom_
        add ConditionSwitch(                                                                         
            #hand spunk
            "'hand' in R_Spunk and Rogue_Arms == 2", "images/RogueSprite/Rogue_spunkhand.png",                
            "True", Null(), 
            ) zoom zoom_
        add ConditionSwitch(                                                                        
            #tits spunk
            "'tits' in R_Spunk", "images/RogueSprite/Rogue_spunktits.png",
            "True", Null(), 
            ) zoom zoom_
        add ConditionSwitch(                                                                        
            #face spunk
            "'facial' in R_Spunk", "images/RogueSprite/Rogue_facial.png",
            "True", Null(), 
            ) zoom zoom_
        add ConditionSwitch(                                                                        
            #Props
            "not R_Held or Rogue_Arms != 2", Null(), 
            "Rogue_Arms == 2 and R_Held == 'phone'", "images/RogueSprite/Rogue_held_phone.png",
            "Rogue_Arms == 2 and R_Held == 'dildo'", "images/RogueSprite/Rogue_held_dildo.png",            
            "Rogue_Arms == 2 and R_Held == 'vibrator'", "images/RogueSprite/Rogue_held_vibrator.png",
            "Rogue_Arms == 2 and R_Held == 'panties'", "images/RogueSprite/Rogue_held_panties.png",
            "True", Null(), 
            ) zoom zoom_
        add ConditionSwitch(
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
            ) zoom zoom_
        add ConditionSwitch(  
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
            ) zoom zoom_
        add ConditionSwitch(                                                                          
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
            ) zoom zoom_
        add ConditionSwitch(                                                                        
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
            ) zoom zoom_
        add ConditionSwitch(  
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
            ) zoom zoom_
        add ConditionSwitch(  
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
            ) zoom zoom_

# image testdesu = im.MatrixColor(
#     "images/KittyBJFace/Kitty_BJ_Hair_Evo.png",
#     # im.matrix.desaturate()
#     im.matrix.tint(1, 0.16, 0.39)
#     )

# image testdesss = im.MatrixColor("images/bg.png",im.matrix.tint(.75,.75,1.0))

label Recolor_Hair(Girl = "Kitty", Outfit = "Hair"):

    if Girl == "Kitty":                    
        $ K_HairCustomColor.screen_loop()
        call Mod_Update_Kitty_Image
    elif Girl == "Emma":
        $ E_HairCustomColor.screen_loop()
        call Mod_Update_Emma_Image
    elif Girl == "Laura":
        $ L_HairCustomColor.screen_loop()
        call Mod_Update_Laura_Image
    elif Girl == "Rogue":
        if Outfit == "HairBangs":
            $ R_HairCustomColorBangs.screen_loop()
        else:
            $ R_HairCustomColor.screen_loop()
        call Mod_Update_Rogue_Image
    return


screen recolor_screen_Kitty_Hair:

    # add(im.MatrixColor("images/EmmaSprite/EmmaSprite_Head_HairBack_White.png",im.matrix.tint(float(K_HairCustomColor.tempred)/255.0, float(K_HairCustomColor.tempgreen)/255.0, float(K_HairCustomColor.tempblue)/255.0))) align(0.5, 0.1)
    add(im.MatrixColor("images/KittyBJFace/Kitty_BJ_HairWhite_Evo.png",im.matrix.tint(float(K_HairCustomColor.tempred)/255.0, float(K_HairCustomColor.tempgreen)/255.0, float(K_HairCustomColor.tempblue)/255.0))) align(0.5, 0.1)
        
    text ("{size=-5}RGB Values: Red: %s, Green: %s, Blue: %s !!!"%(K_HairCustomColor.tempred, K_HairCustomColor.tempgreen, K_HairCustomColor.tempblue)) align(0.5, 0.6)    
        
    vbox align(0.5, 0.7):
        bar:
            xalign 0.5
            value FieldValue(K_HairCustomColor, 'tempred', 255, max_is_zero=False, style='scrollbar', offset=0, step=1)
            xmaximum 255
            
        bar:
            xalign 0.5
            value FieldValue(K_HairCustomColor, 'tempgreen', 255, max_is_zero=False, style='scrollbar', offset=0, step=1)
            xmaximum 255
            
        bar:
            xalign 0.5
            value FieldValue(K_HairCustomColor, 'tempblue', 255, max_is_zero=False, style='scrollbar', offset=0, step=1)
            xmaximum 255
    
    textbutton "Apply" align(0.45, 0.95):
        action Return(['apply'])
    textbutton "Quit" align(0.55, 0.95):
        action Return(['quit'])

screen recolor_screen_Emma_Hair:

    add(im.MatrixColor("images/EmmaSprite/EmmaSprite_Head_HairWhiteBack.png",im.matrix.tint(float(E_HairCustomColor.tempred)/255.0, float(E_HairCustomColor.tempgreen)/255.0, float(E_HairCustomColor.tempblue)/255.0))) align(0.5, 0.1)
        
    text ("{size=-5}RGB Values: Red: %s, Green: %s, Blue: %s !!!"%(E_HairCustomColor.tempred, E_HairCustomColor.tempgreen, E_HairCustomColor.tempblue)) align(0.5, 0.6)    
        
    vbox align(0.5, 0.7):
        bar:
            xalign 0.5
            value FieldValue(E_HairCustomColor, 'tempred', 255, max_is_zero=False, style='scrollbar', offset=0, step=1)
            xmaximum 255
            
        bar:
            xalign 0.5
            value FieldValue(E_HairCustomColor, 'tempgreen', 255, max_is_zero=False, style='scrollbar', offset=0, step=1)
            xmaximum 255
            
        bar:
            xalign 0.5
            value FieldValue(E_HairCustomColor, 'tempblue', 255, max_is_zero=False, style='scrollbar', offset=0, step=1)
            xmaximum 255
    
    textbutton "Apply" align(0.45, 0.95):
        action Return(['apply'])
    textbutton "Quit" align(0.55, 0.95):
        action Return(['quit'])

screen recolor_screen_Laura_Hair:

    add(im.MatrixColor("images/LauraSprite/Laura_Sprite_HairWhite_Long_Over.png",im.matrix.tint(float(L_HairCustomColor.tempred)/255.0, float(L_HairCustomColor.tempgreen)/255.0, float(L_HairCustomColor.tempblue)/255.0))) align(0.5, 0.1)
        
    text ("{size=-5}RGB Values: Red: %s, Green: %s, Blue: %s !!!"%(L_HairCustomColor.tempred, L_HairCustomColor.tempgreen, L_HairCustomColor.tempblue)) align(0.5, 0.6)    
        
    vbox align(0.5, 0.7):
        bar:
            xalign 0.5
            value FieldValue(L_HairCustomColor, 'tempred', 255, max_is_zero=False, style='scrollbar', offset=0, step=1)
            xmaximum 255
            
        bar:
            xalign 0.5
            value FieldValue(L_HairCustomColor, 'tempgreen', 255, max_is_zero=False, style='scrollbar', offset=0, step=1)
            xmaximum 255
            
        bar:
            xalign 0.5
            value FieldValue(L_HairCustomColor, 'tempblue', 255, max_is_zero=False, style='scrollbar', offset=0, step=1)
            xmaximum 255
    
    textbutton "Apply" align(0.45, 0.95):
        action Return(['apply'])
    textbutton "Quit" align(0.55, 0.95):
        action Return(['quit'])


screen recolor_screen_Rogue_Hair:
    
    if R_HairColorBangs:
        add(im.MatrixColor("images/RogueBJFace/Rogue_bj_hairWhite_back.png",im.matrix.tint(float(R_HairCustomColor.tempred)/255.0, float(R_HairCustomColor.tempgreen)/255.0, float(R_HairCustomColor.tempblue)/255.0))) align(0.5, 0.1)
        add(im.MatrixColor("images/RogueBJFace/Rogue_bj_hairWhite_back1.png",im.matrix.tint(float(R_HairCustomColorBangs.tempred)/255.0, float(R_HairCustomColorBangs.tempgreen)/255.0, float(R_HairCustomColorBangs.tempblue)/255.0))) align(0.5, 0.1)
    else:
        add(im.MatrixColor("images/RogueBJFace/Rogue_bj_hairWhite_back.png",im.matrix.tint(float(R_HairCustomColor.tempred)/255.0, float(R_HairCustomColor.tempgreen)/255.0, float(R_HairCustomColor.tempblue)/255.0))) align(0.5, 0.1)
        
        
    text ("{size=-5}RGB Values: Red: %s, Green: %s, Blue: %s !!!"%(R_HairCustomColor.tempred, R_HairCustomColor.tempgreen, R_HairCustomColor.tempblue)) align(0.5, 0.6)    
        
    vbox align(0.5, 0.7):
        bar:
            xalign 0.5
            value FieldValue(R_HairCustomColor, 'tempred', 255, max_is_zero=False, style='scrollbar', offset=0, step=1)
            xmaximum 255
            
        bar:
            xalign 0.5
            value FieldValue(R_HairCustomColor, 'tempgreen', 255, max_is_zero=False, style='scrollbar', offset=0, step=1)
            xmaximum 255
            
        bar:
            xalign 0.5
            value FieldValue(R_HairCustomColor, 'tempblue', 255, max_is_zero=False, style='scrollbar', offset=0, step=1)
            xmaximum 255
    
    textbutton "Apply" align(0.45, 0.95):
        action Return(['apply'])
    textbutton "Quit" align(0.55, 0.95):
        action Return(['quit'])

screen recolor_screen_Rogue_HairBangs:

    add(im.MatrixColor("images/RogueBJFace/Rogue_bj_hairWhite_back.png",im.matrix.tint(float(R_HairCustomColor.tempred)/255.0, float(R_HairCustomColor.tempgreen)/255.0, float(R_HairCustomColor.tempblue)/255.0))) align(0.5, 0.1)
    add(im.MatrixColor("images/RogueBJFace/Rogue_bj_hairWhite_back1.png",im.matrix.tint(float(R_HairCustomColorBangs.tempred)/255.0, float(R_HairCustomColorBangs.tempgreen)/255.0, float(R_HairCustomColorBangs.tempblue)/255.0))) align(0.5, 0.1)
        
    text ("{size=-5}RGB Values: Red: %s, Green: %s, Blue: %s !!!"%(R_HairCustomColorBangs.tempred, R_HairCustomColorBangs.tempgreen, R_HairCustomColorBangs.tempblue)) align(0.5, 0.6)    
        
    vbox align(0.5, 0.7):
        bar:
            xalign 0.5
            value FieldValue(R_HairCustomColorBangs, 'tempred', 255, max_is_zero=False, style='scrollbar', offset=0, step=1)
            xmaximum 255
            
        bar:
            xalign 0.5
            value FieldValue(R_HairCustomColorBangs, 'tempgreen', 255, max_is_zero=False, style='scrollbar', offset=0, step=1)
            xmaximum 255
            
        bar:
            xalign 0.5
            value FieldValue(R_HairCustomColorBangs, 'tempblue', 255, max_is_zero=False, style='scrollbar', offset=0, step=1)
            xmaximum 255
    
    textbutton "Apply" align(0.45, 0.95):
        action Return(['apply'])
    textbutton "Quit" align(0.55, 0.95):
        action Return(['quit'])