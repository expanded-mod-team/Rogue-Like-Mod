label  Mod_Tan(Girl = "Kitty", time = 5):
    if Girl == "Kitty":
        ch_k "Let's get tanned"
        #K_DynamicTan = [0,0,0,0,0,0,0,0]  #controller, over, legs, chest, panties, gloves? choker?, extra
        $ K_DynamicTan[0] = time #in days
        $ K_DynamicTan[1] = K_Over
        $ K_DynamicTan[2] = K_Legs
        $ K_DynamicTan[3] = K_Chest
        $ K_DynamicTan[4] = K_Panties
        $ K_DynamicTan[5] = K_Hose
        call Wait(0,0)
        "Kitty sunbathes for a while"
        hide blackscreen onlayer black
        ch_k "I look amazing, don't I"

    elif Girl == "Rogue":
        ch_r "Let's get tanned"
        #R_DynamicTan = [0,0,0,0,0,0,0,0]  #controller, over, legs, chest, panties, gloves? choker?, extra
        $ R_DynamicTan[0] = time #in days
        $ R_DynamicTan[1] = R_Over
        $ R_DynamicTan[2] = R_Legs
        $ R_DynamicTan[3] = R_Chest
        $ R_DynamicTan[4] = R_Panties
        $ R_DynamicTan[5] = R_Hose
        call Wait(0,0)
        "Rogue sunbathes for a while"
        hide blackscreen onlayer black
        ch_r "I look amazing, don't I"

    return