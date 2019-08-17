label  mod_hide_Rogue_SexSprite:
    if renpy.showing("Rogue_SexSprite"):
        hide Rogue_SexSprite
    elif renpy.showing("Rogue_Doggy"):
        hide Rogue_Doggy
        if R_Gag == "ballgag":
            $ R_Gag = 0
    return