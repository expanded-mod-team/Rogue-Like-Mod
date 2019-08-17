label  mod_hide_Kitty_SexSprite:
    if renpy.showing("Kitty_SexSprite"):
        hide Kitty_SexSprite
    elif renpy.showing("Kitty_Doggy"):
        hide Kitty_Doggy
        if K_Gag == "ballgag":
            $ K_Gag = 0
    return