        
screen Mod_Status_screen:
    
    default tt = Tooltip(" ")
    
    # if Ch_Focus == "Mystique":
    $ Ch_Focus = "Mystique"
    add "images/BarBackdrop_M.png"
    frame:  
        style_group "stat_bar" 
        xminimum 130       
        background None
        has vbox     
        hbox:
            imagebutton idle "images/iconlove.png" hover "images/iconlove.png" action NullAction() hovered tt.Action("Love: " + str(newgirl["Mystique"].Love))
            bar range 100 value VariableValue2("Love", Ch_Focus, 1000) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0 
        hbox:
            imagebutton idle "images/iconlust.png" hover "images/iconlust.png" action NullAction() hovered tt.Action("Lust: " + str(newgirl["Mystique"].Lust))
            bar range 100 value VariableValue2("Lust", Ch_Focus, 100) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
    frame:
        xminimum 130
        xpos 130    
        background None
        has vbox
        hbox:
            imagebutton idle "images/iconobed.png" hover "images/iconobed.png" action NullAction() hovered tt.Action("Obedience: " + str(newgirl["Mystique"].Obed))
            bar range 100 value VariableValue2("Obed", Ch_Focus, 1000) xmaximum 100 left_bar "images/barfullO.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
        hbox:
            imagebutton idle "images/iconaddict.png" hover "images/iconaddict.png" action NullAction() hovered tt.Action("Addiction: " + str(newgirl["Mystique"].Addict))
            bar range 100 value VariableValue2("Addict", Ch_Focus, 100) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 6 thumb None thumb_offset 0
    frame:
        xminimum 130
        xpos 260    
        background None
        has vbox
        hbox:
            imagebutton idle "images/iconinbt.png" hover "images/iconinbt.png" action NullAction() hovered tt.Action("Inhibitions: " + str(newgirl["Mystique"].Inbt))
            bar range 100 value VariableValue2("Inbt", Ch_Focus, 1000) xmaximum 100 left_bar "images/barfulli.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0        
        hbox:
            imagebutton idle "images/iconaddictrate.png" hover "images/iconaddictrate.png" action NullAction() hovered tt.Action("Addiciton Rate: " + str(newgirl["Mystique"].Addictionrate))
            bar range 100 value VariableValue2("Addictionrate", Ch_Focus, 10) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0        
    showif not Trigger:
        imagebutton auto "images/Button_Mystique_%s.png" action ShowTransient("Mod_Test_Focus_Map") xpos 690 ypos 5 focus_mask True #xpos 690 ypos 5 
    showif config.developer: #nothing here
        imagebutton auto "images/Button_Mystique_%s.png" action ui.callsinnewcontext("NewGirlStats", "Mystique") xpos 730 ypos 5 focus

    #end Under bar
    
    #Primary bar
    #Kitty's stats
    # if Ch_Focus == "Kitty":
    #     add "images/BarBackdrop_K.png"        
    #     frame:  
    #         style_group "stat_bar" 
    #         xminimum 130       
    #         background None
    #         has vbox     
    #         hbox:
    #             imagebutton idle "images/iconlove.png" hover "images/iconlove.png" action NullAction() hovered tt.Action("Love: [K_Love]")
    #             bar range 100 value VariableValue("K_Love", 1000) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0 
    #         hbox:
    #             imagebutton idle "images/iconlust.png" hover "images/iconlust.png" action NullAction() hovered tt.Action("Lust: [K_Lust]")
    #             bar range 100 value VariableValue("K_Lust", 100) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
    #     frame:
    #         xminimum 130
    #         xpos 130    
    #         background None
    #         has vbox
    #         hbox:
    #             imagebutton idle "images/iconobed.png" hover "images/iconobed.png" action NullAction() hovered tt.Action("Obedience: [K_Obed]")
    #             bar range 100 value VariableValue("K_Obed", 1000) xmaximum 100 left_bar "images/barfullO.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
    #         hbox:
    #             imagebutton idle "images/iconaddict.png" hover "images/iconaddict.png" action NullAction() hovered tt.Action("Addiction: [K_Addict]")
    #             bar range 100 value VariableValue("K_Addict", 100) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 6 thumb None thumb_offset 0
    #     frame:
    #         xminimum 130
    #         xpos 260    
    #         background None
    #         has vbox
    #         hbox:
    #             imagebutton idle "images/iconinbt.png" hover "images/iconinbt.png" action NullAction() hovered tt.Action("Inhibitions: [K_Inbt]")
    #             bar range 100 value VariableValue("K_Inbt", 1000) xmaximum 100 left_bar "images/barfulli.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0        
    #         hbox:
    #             imagebutton idle "images/iconaddictrate.png" hover "images/iconaddictrate.png" action NullAction() hovered tt.Action("Addiciton Rate: [K_Addictionrate]")
    #             bar range 100 value VariableValue("K_Addictionrate", 10) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
    #     showif not Trigger:
    #         imagebutton auto "images/Button_Kitty_%s.png" action ShowTransient("Mod_Test_Focus_Map") xpos 690 ypos 5 focus_mask True #xpos 690 ypos 5 
    #     showif config.developer:
    #         imagebutton auto "images/Button_Kitty_%s.png" action ui.callsinnewcontext("KittyStats") xpos 730 ypos 5 focus
    # #Emma's Stats
    # elif Ch_Focus == "Emma":
    #     add "images/BarBackdrop_E.png"
    #     frame:  
    #         style_group "stat_bar" 
    #         xminimum 130       
    #         background None
    #         has vbox     
    #         hbox:
    #             imagebutton idle "images/iconlove.png" hover "images/iconlove.png" action NullAction() hovered tt.Action("Love: [E_Love]")
    #             bar range 100 value VariableValue("E_Love", 1000) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0 
    #         hbox:
    #             imagebutton idle "images/iconlust.png" hover "images/iconlust.png" action NullAction() hovered tt.Action("Lust: [E_Lust]")
    #             bar range 100 value VariableValue("E_Lust", 100) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
    #     frame:
    #         xminimum 130
    #         xpos 130    
    #         background None
    #         has vbox
    #         hbox:
    #             imagebutton idle "images/iconobed.png" hover "images/iconobed.png" action NullAction() hovered tt.Action("Obedience: [E_Obed]") #action NullAction("none")?
    #             bar range 100 value VariableValue("E_Obed", 1000) xmaximum 100 left_bar "images/barfullO.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
    #         hbox:
    #             imagebutton idle "images/iconaddict.png" hover "images/iconaddict.png" action NullAction() hovered tt.Action("Addiction: [E_Addict]")
    #             bar range 100 value VariableValue("E_Addict", 100) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 6 thumb None thumb_offset 0
    #     frame:
    #         xminimum 130
    #         xpos 260    
    #         background None
    #         has vbox
    #         hbox:
    #             imagebutton idle "images/iconinbt.png" hover "images/iconinbt.png" action NullAction() hovered tt.Action("Inhibitions: [E_Inbt]")
    #             bar range 100 value VariableValue("E_Inbt", 1000) xmaximum 100 left_bar "images/barfulli.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0        
    #         hbox:
    #             imagebutton idle "images/iconaddictrate.png" hover "images/iconaddictrate.png" action NullAction() hovered tt.Action("Addiction Rate: [E_Addictionrate]")
    #             bar range 100 value VariableValue("E_Addictionrate", 10) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0        
    #     showif not Trigger:
    #         imagebutton auto "images/Button_Emma_%s.png" action ShowTransient("Mod_Test_Focus_Map") xpos 690 ypos 5 focus_mask True #xpos 690 ypos 5 
    #     showif config.developer:
    #         imagebutton auto "images/Button_Emma_%s.png" action ui.callsinnewcontext("EmmaStats") xpos 730 ypos 5 focus
    # elif Ch_Focus == "Laura":
    #     add "images/BarBackdrop_L.png" #change to L
    #     frame:  
    #         style_group "stat_bar" 
    #         xminimum 130       
    #         background None
    #         has vbox     
    #         hbox:
    #             imagebutton idle "images/iconlove.png" hover "images/iconlove.png" action NullAction() hovered tt.Action("Love: [L_Love]")
    #             bar range 100 value VariableValue("L_Love", 1000) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0 
    #         hbox:
    #             imagebutton idle "images/iconlust.png" hover "images/iconlust.png" action NullAction() hovered tt.Action("Lust: [L_Lust]")
    #             bar range 100 value VariableValue("L_Lust", 100) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
    #     frame:
    #         xminimum 130
    #         xpos 130    
    #         background None
    #         has vbox
    #         hbox:
    #             imagebutton idle "images/iconobed.png" hover "images/iconobed.png" action NullAction() hovered tt.Action("Obedience: [L_Obed]") #action NullAction("none")?
    #             bar range 100 value VariableValue("L_Obed", 1000) xmaximum 100 left_bar "images/barfullO.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
    #         hbox:
    #             imagebutton idle "images/iconaddict.png" hover "images/iconaddict.png" action NullAction() hovered tt.Action("Addiction: [L_Addict]")
    #             bar range 100 value VariableValue("L_Addict", 100) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 6 thumb None thumb_offset 0
    #     frame:
    #         xminimum 130
    #         xpos 260    
    #         background None
    #         has vbox
    #         hbox:
    #             imagebutton idle "images/iconinbt.png" hover "images/iconinbt.png" action NullAction() hovered tt.Action("Inhibitions: [L_Inbt]")
    #             bar range 100 value VariableValue("L_Inbt", 1000) xmaximum 100 left_bar "images/barfulli.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0        
    #         hbox:
    #             imagebutton idle "images/iconaddictrate.png" hover "images/iconaddictrate.png" action NullAction() hovered tt.Action("Addiction Rate: [L_Addictionrate]")
    #             bar range 100 value VariableValue("L_Addictionrate", 10) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0        
    #     showif not Trigger:
    #         imagebutton auto "images/Button_Laura_%s.png" action ShowTransient("Mod_Test_Focus_Map") xpos 690 ypos 5 focus_mask True #xpos 690 ypos 5 
    #     showif config.developer:
    #         imagebutton auto "images/Button_Laura_%s.png" action ui.callsinnewcontext("LauraStats") xpos 730 ypos 5 focus
    # #Rogue's Stats
    # else: #if Ch_Focus == "Rogue":
    #     add "images/BarBackdrop_R.png"
    #     frame:  
    #         style_group "stat_bar" 
    #         xminimum 130       
    #         background None
    #         has vbox     
    #         hbox:
    #             imagebutton idle "images/iconlove.png" hover "images/iconlove.png" action NullAction() hovered tt.Action("Love: [R_Love]")
    #             bar range 100 value VariableValue("R_Love", 1000) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0 
    #         hbox:
    #             imagebutton idle "images/iconlust.png" hover "images/iconlust.png" action NullAction() hovered tt.Action("Lust: [R_Lust]")
    #             bar range 100 value VariableValue("R_Lust", 100) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
    #     frame:
    #         xminimum 130
    #         xpos 130    
    #         background None
    #         has vbox
    #         hbox:
    #             imagebutton idle "images/iconobed.png" hover "images/iconobed.png" action NullAction() hovered tt.Action("Obedience: [R_Obed]") #action NullAction("none")?
    #             bar range 100 value VariableValue("R_Obed", 1000) xmaximum 100 left_bar "images/barfullO.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
    #         hbox:
    #             imagebutton idle "images/iconaddict.png" hover "images/iconaddict.png" action NullAction() hovered tt.Action("Addiction: [R_Addict]")
    #             bar range 100 value VariableValue("R_Addict", 100) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 6 thumb None thumb_offset 0
    #     frame:
    #         xminimum 130
    #         xpos 260    
    #         background None
    #         has vbox
    #         hbox:
    #             imagebutton idle "images/iconinbt.png" hover "images/iconinbt.png" action NullAction() hovered tt.Action("Inhibitions: [R_Inbt]")
    #             bar range 100 value VariableValue("R_Inbt", 1000) xmaximum 100 left_bar "images/barfulli.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0        
    #         hbox:
    #             imagebutton idle "images/iconaddictrate.png" hover "images/iconaddictrate.png" action NullAction() hovered tt.Action("Addiction Rate: [R_Addictionrate]")
    #             bar range 100 value VariableValue("R_Addictionrate", 10) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0        
        
    #     showif not Trigger:
    #         imagebutton auto "images/Button_Rogue_%s.png" action ShowTransient("Mod_Test_Focus_Map") xpos 690 ypos 5 focus_mask True #xpos 690 ypos 5 
    #     showif config.developer:
    #         imagebutton auto "images/Button_Rogue_%s.png" action ui.callsinnewcontext("RogueStats") xpos 730 ypos 5 focus


    frame:
        #Focus meter (dick)
        xminimum 130
        xpos 390    
        background None
        has vbox
        hbox:            
            bar range 100 value VariableValue("P_Focus", 100) xmaximum 100 left_bar "images/barfullP.png" right_bar "images/baremptyP.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0 
        hbox:
            bar range 100 value VariableValue("P_Semen", 5) xmaximum 100 left_bar "images/barfullS.png" right_bar "images/baremptyS.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
        imagebutton auto "images/Button_Emma_%s.png" action ui.callsinnewcontext("EmmaStats") xpos 730 ypos 5 focus

    frame:
        # Money and level
        xminimum 75
        xpos 500    
        ypos -5   
        background None
        has vbox
        hbox:            
            text "Money: $[P_Cash]" size 12
        hbox:
            text "Level: [P_Lvl]" size 12 
        # if Ch_Focus == 'Emma':
        #     hbox:
        #         text "Actions Left: [E_Action]" size 12
        #     hbox:
        #         text "Forced: [E_ForcedCount]" size 12
        # elif Ch_Focus == 'Kitty':
        #     hbox:
        #         text "Actions Left: [K_Action]" size 12
        #     hbox:
        #         text "Forced: [K_ForcedCount]" size 12
        # elif Ch_Focus == 'Rogue':
        #     hbox:
        #         text "Actions Left: [R_Action]" size 12
        #     hbox:
        #         text "Forced: [R_ForcedCount]" size 12
        # # elif Ch_Focus == 'Mystique':
        # #     hbox:
        # #         text "Actions Left: [newgirl[Mystique].Action]" size 12
        # #     hbox:
        # #         text "Forced: [newgirl[Mystique].ForcedCount]" size 12
        # elif Ch_Focus == 'Laura':
        if Ch_Focus == 'Mystique':
            hbox:
                text "Actions Lefts: " + str(newgirl[Ch_Focus].Action) size 12
            hbox:
                text "Forced: " + str(newgirl[Ch_Focus].ForcedCount) size 12
        # this block is the name tag
        window:         
            pos (90,-40)#(-15,-8)
            anchor (0,0)
            style "say_who_window"
            text "[Ch_Focus]" size 12 font "CRIMFBRG.ttf" color "#000000" #id "Ch_Focus"            
                    
    frame:
        #Clock
        xpos 900  
        ypos 20
        background None

        add "images/Clockbase.png":
            anchor (0.5,0.5)
            yzoom -1
            subpixel True

        if Round < 50:
            add "images/Clockred.png" at rotate_red(Round):
                anchor (0.5,0.5)
                subpixel True
        else:
            add "images/Clockwhite.png" at rotate_white(Round):
                anchor (0.5,0.5)
                subpixel True

        imagebutton idle "images/Clockface.png" hover "images/Clockface.png" action NullAction() hovered tt.Action("Time Left: [Round]%") anchor (0.5,0.5)
            
    frame:
        # Date and time
        xminimum 130
        xpos 920    
        background None
        has vbox
        hbox:            
            text "Day: [Day] [DayofWeek]" size 12
        hbox:            
            text "Time: [Current_Time]" size 12
    frame:     
        #displays small icons for nearby characters
        xpos 920
        ypos 30
        background None
        vbox:
            hbox:
                if "Rogue" in Nearby:
                    imagebutton auto "images/Button_Rogue_%s.png" action NullAction() hovered tt.Action("Rogue") at TinyButtons
                if "Kitty" in Nearby:
                    imagebutton auto "images/Button_Kitty_%s.png" action NullAction() hovered tt.Action("Kitty") at TinyButtons
                if "Emma" in Nearby:
                    imagebutton auto "images/Button_Emma_%s.png" action NullAction() hovered tt.Action("Emma") at TinyButtons 
                if "Laura" in Nearby:
                    imagebutton auto "images/Button_Laura_%s.png" action NullAction() hovered tt.Action("Laura") at TinyButtons
        
    
    if tt.value != " ":
        # Pop-up mouse-over labels
        frame :
            xpos 500 ypos 60
            has vbox:
                text tt.value 


           
screen Mod_Test_Focus_Map:
    #changes focal character with dropdown box
    imagebutton auto "images/Button_X_%s.png" action Hide("Mod_Test_Focus_Map") xpos 690 ypos 5 focus_mask True
    # frame:            
    #     xpos 684 
    #     ypos 44
        # hbox:
        #     vbox:
        #         imagebutton auto "images/Button_Rogue_%s.png" action ui.callsinnewcontext("Shift_Focus", "Rogue") focus_mask True
        #         if "met" in K_History:
        #             imagebutton auto "images/Button_Kitty_%s.png" action ui.callsinnewcontext("Shift_Focus", "Kitty") focus_mask True
                 
        #     vbox:
        #         if "met" in E_History:
        #             imagebutton auto "images/Button_Emma_%s.png" action ui.callsinnewcontext("Shift_Focus", "Emma") focus_mask True
        #         if "met" in L_History:
        #             imagebutton auto "images/Button_Laura_%s.png" action ui.callsinnewcontext("Shift_Focus", "Laura") focus_mask True
