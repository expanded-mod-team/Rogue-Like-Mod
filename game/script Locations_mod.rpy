# //////////////////////////////////////////////////////////////////////                World Map Interface 
init python:
    def IsGirlAround(Girl = "Any"):

        if Girl == "Any":
            if (R_Loc == bg_current or "Rogue" in Party):
                    return 1
            elif (K_Loc == bg_current or "Kitty" in Party):   
                    return 1
            elif (E_Loc == bg_current or "Emma" in Party):         
                    return 1
            elif (L_Loc == bg_current or "Laura" in Party):    
                    return 1
        return 0

    def IsGirlInParty(Girl = "Any"):

        if Girl == "Any":
            if ("Rogue" in Party):
                    return 1
            elif ("Kitty" in Party):   
                    return 1
            elif ("Emma" in Party):         
                    return 1
            elif ("Laura" in Party):    
                    return 1
        return 0

label Mod_EventCalls:
    call Get_Dressed

    if Current_Time == "Evening" and "yesdate" in P_DailyActions:
            if bg_current == "bg campus": 
                    call DateNight
                    if "yesdate" in P_DailyActions:
                            $ P_DailyActions.remove("yesdate")
                    return
            else:
                
                    menu:
                        "You have a date to get to, head for the square?"
                        "Yes":
                            $ renpy.pop_call()
                            call Leave_Brotherhood_Area
                            jump Campus_Entry
                        "No":
                            "Suit yourself. . ."
                            
    if Current_Time == "Night" and "met" not in newgirl["Mystique"].History :
        if Day >= 5:
            if bg_current != "bg player" and not IsGirlAround():
                call Mod_Display_Background
                "It's late, so you decide to head back to your room"
                $ bg_current = "bg player"
                call Mod_Display_Background
                call MystiqueMeet
                return 
    
    if R_Loc != bg_current and "Rogue" in Digits and R_Nude:
        call Mod_Nude("Rogue")
    if K_Loc != bg_current and "Kitty" in Digits and K_Nude:
        call Mod_Nude("Kitty")
    if E_Loc != bg_current and "Emma" in Digits and E_Nude:
        call Mod_Nude("Emma")
    if L_Loc != bg_current and "Laura" in Digits and L_Nude:
        call Mod_Nude("Laura")

    return

label Mod_Chat:
            menu:
                "Chat with Mystique" if newgirl["Mystique"].Loc == bg_current:                     
                        call Mystique_Chat

                # "Text Mystique" if newgirl["Mystique"].Loc != bg_current and "met" in E_History: 
                #         if "Mystique" in Digits:
                #             "You send Mystique a text."                 
                #             call Mystique_Chat
                #         else:
                #             "You don't know her number, you'll have to go to her." 
                #             return   

                "Never Mind":
                    pass
            return

label Mod_Display_Background(Entry = 0): 
        # call Mod_Display_Background(1)              
        #Displays the current background
        if Entry:
                                scene bg_entry onlayer backdrop
        elif bg_current == "bg player":
                                scene bg_player onlayer backdrop
        elif bg_current == "bg Mystique":
                                scene bg_Mystique onlayer backdrop
        elif bg_current == "bg Brotherhood":
                                scene bg_Brotherhood onlayer backdrop

        else: # if 'bg campus' or anything else        
                                scene bg_campus onlayer backdrop   
        return

image bg_Mystique = "images/mystiqueroom.png"  
image bg_Brotherhood = "images/Brotherhood.png"  

label Display_Mystique(Dress = 1, DLoc = newgirl["Mystique"].SpriteLoc, Location = newgirl["Mystique"].Loc):
    # If Dress, then check whether the character is underdressed when displaying her
    if Taboo and Dress and newgirl["Mystique"].Loc != "bg pool": #If not in the showers, get dressed and dry off        
            call MystiqueOutfit
            #$ newgirl["Mystique"].Wet = 0
              
    if newgirl["Mystique"].Loc != "bg showerroom" and newgirl["Mystique"].Loc != "bg pool":
            $ newgirl["Mystique"].Water = 0
        
    $ newgirl["Mystique"].SpriteLoc = DLoc
    
    # resets triggers
    $ Trigger = 0    
    $ Trigger2 = 0 if Trigger2 != "jackin" else "jackin"
    $ Trigger3 = 0
    $ Trigger4 = 0
    $ Trigger5 = 0
    
    if "Mystique" in Party or Location == bg_current:         
            #displays Mystique if present, Sets her as local if in a party
            if "Mystique" in Party: 
                    $ newgirl["Mystique"].Loc = bg_current 
            
            if Taboo and Dress:                       #If in public, check to see if clothes are too sexy, and change them if necessary
                call Mystique_OutfitShame
                
            
            #Display Mystique
            show Mystique_Sprite at SpriteLoc(DLoc) zorder newgirl["Mystique"].GirlLayer:
                    alpha 1
                    zoom 1
                    offset (0,0)
                    anchor (0.5, 0.0)
    else:
            # If Mystique isn't there, put her away
            hide Mystique_Sprite
            #call Mystique_Hide
    return     

label MystiqueOutfit(M_OutfitTemp = newgirl["Mystique"].Outfit, Spunk = 0, Undressed = 0, Changed = 0):   
        # M_OutfitTemp is the chosen new outfit, Spunk removes sperm on her, Undressed determines whether she is under dressed  
        
        if renpy.showing("NightMask", layer='nightmask') and Current_Time == "Morning":
            #Skips theis check if it's a sleepover
            return

        if newgirl["Mystique"].Gag:
            "She removes her gag"
            $ newgirl["Mystique"].Gag = 0
        
        if M_OutfitTemp != newgirl["Mystique"].Outfit:
                #if her new outfit is not what she was wearing before,
                #don't flag the undressed mechanic
                $ Changed = 1    
        if "Mystique" in Party and M_OutfitTemp == newgirl["Mystique"].OutfitDay:
                #this ignores her daily outfit if she's in a party
                $ M_OutfitTemp = newgirl["Mystique"].Outfit
        if newgirl["Mystique"].Loc == "bg teacher" or newgirl["Mystique"].Loc == "bg classroom":
                #this ignores her daily outfit if she's in the classroom
                $ M_OutfitTemp = "teacher"
        if newgirl["Mystique"].Loc == "bg showerroom" and "Mystique" not in Party and M_OutfitTemp != "nude":
                #Automatically puts her in the towel while in the shower
                $ M_OutfitTemp = "towel"                                  
        elif newgirl["Mystique"].Loc != "bg showerroom" and newgirl["Mystique"].Loc != "bg pool":
                #Dries her off
                $ newgirl["Mystique"].Water = 0
                
        if newgirl["Mystique"].Spunk:
                if "painted" not in newgirl["Mystique"].DailyActions or "cleaned" not in newgirl["Mystique"].DailyActions:        
                    $ del newgirl["Mystique"].Spunk[:] 
                
        $ newgirl["Mystique"].Upskirt = 0
        $ newgirl["Mystique"].Uptop = 0
        $ newgirl["Mystique"].PantiesDown = 0
        if M_OutfitTemp == "teacher":
                    if 0 in (newgirl["Mystique"].Legs,newgirl["Mystique"].Over,newgirl["Mystique"].Chest,newgirl["Mystique"].Hose):
                            $ Undressed = 1
                    elif newgirl["Mystique"].Panties == 0 and "pantyless" not in newgirl["Mystique"].DailyActions:                        
                            $ Undressed = 1   
                    $ newgirl["Mystique"].Arms = 0
                    $ newgirl["Mystique"].Legs = "black skirt"
                    $ newgirl["Mystique"].Over = "red shirt"
                    $ newgirl["Mystique"].Chest = "black bra"
                    $ newgirl["Mystique"].Panties = "black panties"        
                    $ newgirl["Mystique"].Neck = 0
                    $ newgirl["Mystique"].Hair = "basic"
                    $ newgirl["Mystique"].Hose = "stockings"  
                    $ newgirl["Mystique"].Glasses = "glasses"  
        if M_OutfitTemp == "regular":
                    if 0 in (newgirl["Mystique"].Legs,newgirl["Mystique"].Chest,newgirl["Mystique"].Hose):
                            $ Undressed = 1
                    elif newgirl["Mystique"].Panties == 0 and "pantyless" not in newgirl["Mystique"].DailyActions:                        
                            $ Undressed = 1   
                    $ newgirl["Mystique"].Arms = 0
                    $ newgirl["Mystique"].Legs = "black skirt"
                    $ newgirl["Mystique"].Over = 0
                    $ newgirl["Mystique"].Chest = "top"
                    $ newgirl["Mystique"].Panties = "black panties"        
                    $ newgirl["Mystique"].Neck = 0
                    $ newgirl["Mystique"].Hair = "basic"
                    $ newgirl["Mystique"].Hose = 'stockings'  
                    $ newgirl["Mystique"].Glasses = 0  
        elif M_OutfitTemp == "costume":
                    if 0 in (newgirl["Mystique"].Legs,newgirl["Mystique"].Chest):
                            $ Undressed = 1
                    elif newgirl["Mystique"].Panties == 0 and "pantyless" not in newgirl["Mystique"].DailyActions:                        
                            $ Undressed = 1   
                    $ newgirl["Mystique"].Arms = "white gloves"
                    $ newgirl["Mystique"].Legs = "pants"
                    $ newgirl["Mystique"].Over = 0
                    $ newgirl["Mystique"].Chest = "corset"
                    $ newgirl["Mystique"].Panties = "white panties"        
                    $ newgirl["Mystique"].Neck = "choker"
                    $ newgirl["Mystique"].Hair = "basic"
                    $ newgirl["Mystique"].Hose = 0 
                    $ newgirl["Mystique"].Glasses = 0  
        elif M_OutfitTemp == "bikini":
                    if newgirl["Mystique"].Chest == 0:
                            $ Undressed = 1
                    elif newgirl["Mystique"].Panties == 0 and "pantyless" not in newgirl["Mystique"].DailyActions:                        
                            $ Undressed = 1   
                    $ newgirl["Mystique"].Arms = 0
                    $ newgirl["Mystique"].Legs = 0
                    $ newgirl["Mystique"].Over = 0
                    $ newgirl["Mystique"].Chest = "yellow bikini"
                    $ newgirl["Mystique"].Panties = "yellow bikini"        
                    $ newgirl["Mystique"].Neck = 0
                    $ newgirl["Mystique"].Hair = "basic"
                    $ newgirl["Mystique"].Hose = 0     
                    $ newgirl["Mystique"].Glasses = 0  
        elif M_OutfitTemp == "towel":
                    if newgirl["Mystique"].Over == 0:
                            $ Undressed = 2
                    $ newgirl["Mystique"].Arms = 0
                    $ newgirl["Mystique"].Legs = 0
                    $ newgirl["Mystique"].Chest = 0
                    $ newgirl["Mystique"].Over = "towel"
                    $ newgirl["Mystique"].Panties = 0        
                    $ newgirl["Mystique"].Hose = 0          
                    $ newgirl["Mystique"].Neck = 0  
                    $ newgirl["Mystique"].Hair = "bun" 
                    $ newgirl["Mystique"].Shame = 35
        elif M_OutfitTemp == "nude":
                    $ newgirl["Mystique"].Arms = 0
                    $ newgirl["Mystique"].Legs = 0
                    $ newgirl["Mystique"].Chest = 0
                    $ newgirl["Mystique"].Over = 0
                    $ newgirl["Mystique"].Panties = 0              
                    $ newgirl["Mystique"].Neck = 0
                    $ newgirl["Mystique"].Hose = 0   
                    $ newgirl["Mystique"].Shame = 50
        elif M_OutfitTemp == "naked pool":
                    $ newgirl["Mystique"].Arms = 0
                    $ newgirl["Mystique"].Legs = 0
                    $ newgirl["Mystique"].Over = 0
                    $ newgirl["Mystique"].Chest = "naked pool"
                    $ newgirl["Mystique"].Panties = "naked pool"              
                    $ newgirl["Mystique"].Neck = 0
                    $ newgirl["Mystique"].Hair = "wavy"
                    $ newgirl["Mystique"].Hose = 0   
        elif M_OutfitTemp == "custom1":
                    if not newgirl["Mystique"].Legs and newgirl["Mystique"].Custom[2]:            
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Over and newgirl["Mystique"].Custom[3]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Chest and newgirl["Mystique"].Custom[5]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Panties and newgirl["Mystique"].Custom[6] and "pantyless" not in newgirl["Mystique"].DailyActions:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Hose and newgirl["Mystique"].Custom[9]:          
                            $ Undressed = 1
                    
                    $ newgirl["Mystique"].Arms = newgirl["Mystique"].Custom[1]
                    $ newgirl["Mystique"].Legs = newgirl["Mystique"].Custom[2]
                    $ newgirl["Mystique"].Over = newgirl["Mystique"].Custom[3]    
                    $ newgirl["Mystique"].Neck = newgirl["Mystique"].Custom[4]
                    $ newgirl["Mystique"].Chest = newgirl["Mystique"].Custom[5]
                    $ newgirl["Mystique"].Panties = newgirl["Mystique"].Custom[6]  
                    $ newgirl["Mystique"].Hair = newgirl["Mystique"].Custom[8] if newgirl["Mystique"].Custom[8] else newgirl["Mystique"].Hair 
                    $ newgirl["Mystique"].Hose = newgirl["Mystique"].Custom[9]                     
                    $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[3]
        elif M_OutfitTemp == "custom2":
                    if not newgirl["Mystique"].Legs and newgirl["Mystique"].Custom2[2]:            
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Over and newgirl["Mystique"].Custom2[3]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Chest and newgirl["Mystique"].Custom2[5]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Panties and newgirl["Mystique"].Custom2[6] and "pantyless" not in newgirl["Mystique"].DailyActions:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Hose and newgirl["Mystique"].Custom2[9]:          
                            $ Undressed = 1
                        
                    $ newgirl["Mystique"].Arms = newgirl["Mystique"].Custom2[1]
                    $ newgirl["Mystique"].Legs = newgirl["Mystique"].Custom2[2]
                    $ newgirl["Mystique"].Over = newgirl["Mystique"].Custom2[3]   
                    $ newgirl["Mystique"].Neck = newgirl["Mystique"].Custom2[4]
                    $ newgirl["Mystique"].Chest = newgirl["Mystique"].Custom2[5]
                    $ newgirl["Mystique"].Panties = newgirl["Mystique"].Custom2[6] 
                    $ newgirl["Mystique"].Hair = newgirl["Mystique"].Custom2[8] if newgirl["Mystique"].Custom2[8] else newgirl["Mystique"].Hair
                    $ newgirl["Mystique"].Hose = newgirl["Mystique"].Custom2[9]                      
                    $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[5]
        elif M_OutfitTemp == "custom3":
                    if not newgirl["Mystique"].Legs and newgirl["Mystique"].Custom3[2]:            
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Over and newgirl["Mystique"].Custom3[3]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Chest and newgirl["Mystique"].Custom3[5]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Panties and newgirl["Mystique"].Custom3[6] and "pantyless" not in newgirl["Mystique"].DailyActions:         
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Hose and newgirl["Mystique"].Custom3[9]:          
                            $ Undressed = 1
                        
                    $ newgirl["Mystique"].Arms = newgirl["Mystique"].Custom3[1]
                    $ newgirl["Mystique"].Legs = newgirl["Mystique"].Custom3[2]
                    $ newgirl["Mystique"].Over = newgirl["Mystique"].Custom3[3]
                    $ newgirl["Mystique"].Neck = newgirl["Mystique"].Custom3[4]
                    $ newgirl["Mystique"].Chest = newgirl["Mystique"].Custom3[5]
                    $ newgirl["Mystique"].Panties = newgirl["Mystique"].Custom3[6]  
                    $ newgirl["Mystique"].Hair = newgirl["Mystique"].Custom3[8] if newgirl["Mystique"].Custom3[8] else newgirl["Mystique"].Hair  
                    $ newgirl["Mystique"].Hose = newgirl["Mystique"].Custom3[9]                         
                    $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[6]
        elif M_OutfitTemp == "custom4":
                    if not newgirl["Mystique"].Legs and newgirl["Mystique"].Custom4[2]:            
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Over and newgirl["Mystique"].Custom4[3]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Chest and newgirl["Mystique"].Custom4[5]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Panties and newgirl["Mystique"].Custom4[6] and "pantyless" not in newgirl["Mystique"].DailyActions:         
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Hose and newgirl["Mystique"].Custom4[9]:          
                            $ Undressed = 1
                        
                    $ newgirl["Mystique"].Arms = newgirl["Mystique"].Custom4[1]
                    $ newgirl["Mystique"].Legs = newgirl["Mystique"].Custom4[2]
                    $ newgirl["Mystique"].Over = newgirl["Mystique"].Custom4[3]
                    $ newgirl["Mystique"].Neck = newgirl["Mystique"].Custom4[4]
                    $ newgirl["Mystique"].Chest = newgirl["Mystique"].Custom4[5]
                    $ newgirl["Mystique"].Panties = newgirl["Mystique"].Custom4[6]  
                    $ newgirl["Mystique"].Hair = newgirl["Mystique"].Custom4[8] if newgirl["Mystique"].Custom4[8] else newgirl["Mystique"].Hair  
                    $ newgirl["Mystique"].Hose = newgirl["Mystique"].Custom4[9]                         
                    $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[11]
        elif M_OutfitTemp == "custom5":
                    if not newgirl["Mystique"].Legs and newgirl["Mystique"].Custom5[2]:            
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Over and newgirl["Mystique"].Custom5[3]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Chest and newgirl["Mystique"].Custom5[5]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Panties and newgirl["Mystique"].Custom5[6] and "pantyless" not in newgirl["Mystique"].DailyActions:         
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Hose and newgirl["Mystique"].Custom5[9]:          
                            $ Undressed = 1
                        
                    $ newgirl["Mystique"].Arms = newgirl["Mystique"].Custom5[1]
                    $ newgirl["Mystique"].Legs = newgirl["Mystique"].Custom5[2]
                    $ newgirl["Mystique"].Over = newgirl["Mystique"].Custom5[3]
                    $ newgirl["Mystique"].Neck = newgirl["Mystique"].Custom5[4]
                    $ newgirl["Mystique"].Chest = newgirl["Mystique"].Custom5[5]
                    $ newgirl["Mystique"].Panties = newgirl["Mystique"].Custom5[6]  
                    $ newgirl["Mystique"].Hair = newgirl["Mystique"].Custom5[8] if newgirl["Mystique"].Custom5[8] else newgirl["Mystique"].Hair  
                    $ newgirl["Mystique"].Hose = newgirl["Mystique"].Custom5[9]                         
                    $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[12]
        elif M_OutfitTemp == "custom6":
                    if not newgirl["Mystique"].Legs and newgirl["Mystique"].Custom6[2]:            
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Over and newgirl["Mystique"].Custom6[3]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Chest and newgirl["Mystique"].Custom6[5]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Panties and newgirl["Mystique"].Custom6[6] and "pantyless" not in newgirl["Mystique"].DailyActions:         
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Hose and newgirl["Mystique"].Custom6[9]:          
                            $ Undressed = 1
                        
                    $ newgirl["Mystique"].Arms = newgirl["Mystique"].Custom6[1]
                    $ newgirl["Mystique"].Legs = newgirl["Mystique"].Custom6[2]
                    $ newgirl["Mystique"].Over = newgirl["Mystique"].Custom6[3]
                    $ newgirl["Mystique"].Neck = newgirl["Mystique"].Custom6[4]
                    $ newgirl["Mystique"].Chest = newgirl["Mystique"].Custom6[5]
                    $ newgirl["Mystique"].Panties = newgirl["Mystique"].Custom6[6]  
                    $ newgirl["Mystique"].Hair = newgirl["Mystique"].Custom6[8] if newgirl["Mystique"].Custom6[8] else newgirl["Mystique"].Hair  
                    $ newgirl["Mystique"].Hose = newgirl["Mystique"].Custom6[9]                         
                    $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[13]
        elif M_OutfitTemp == "custom7":
                    if not newgirl["Mystique"].Legs and newgirl["Mystique"].Custom7[2]:            
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Over and newgirl["Mystique"].Custom7[3]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Chest and newgirl["Mystique"].Custom7[5]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Panties and newgirl["Mystique"].Custom7[6] and "pantyless" not in newgirl["Mystique"].DailyActions:         
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Hose and newgirl["Mystique"].Custom7[9]:          
                            $ Undressed = 1
                        
                    $ newgirl["Mystique"].Arms = newgirl["Mystique"].Custom7[1]
                    $ newgirl["Mystique"].Legs = newgirl["Mystique"].Custom7[2]
                    $ newgirl["Mystique"].Over = newgirl["Mystique"].Custom7[3]
                    $ newgirl["Mystique"].Neck = newgirl["Mystique"].Custom7[4]
                    $ newgirl["Mystique"].Chest = newgirl["Mystique"].Custom7[5]
                    $ newgirl["Mystique"].Panties = newgirl["Mystique"].Custom7[6]  
                    $ newgirl["Mystique"].Hair = newgirl["Mystique"].Custom7[8] if newgirl["Mystique"].Custom7[8] else newgirl["Mystique"].Hair  
                    $ newgirl["Mystique"].Hose = newgirl["Mystique"].Custom7[9]                         
                    $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[14]
        elif M_OutfitTemp == "sleep":  
                    if not newgirl["Mystique"].Legs and newgirl["Mystique"].Sleepwear[2]:            
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Over and newgirl["Mystique"].Sleepwear[3]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Chest and newgirl["Mystique"].Sleepwear[5]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Panties and newgirl["Mystique"].Sleepwear[6] and "pantyless" not in newgirl["Mystique"].DailyActions:        
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Hose and newgirl["Mystique"].Sleepwear[9]:          
                            $ Undressed = 1
                        
                    $ newgirl["Mystique"].Arms = newgirl["Mystique"].Sleepwear[1] #0
                    $ newgirl["Mystique"].Legs = newgirl["Mystique"].Sleepwear[2] #shorts
                    $ newgirl["Mystique"].Over = newgirl["Mystique"].Sleepwear[3] #0
                    $ newgirl["Mystique"].Neck = newgirl["Mystique"].Sleepwear[4] #0
                    $ newgirl["Mystique"].Chest = newgirl["Mystique"].Sleepwear[5] #"cami"
                    $ newgirl["Mystique"].Panties = newgirl["Mystique"].Sleepwear[6] #"green panties"
                    $ newgirl["Mystique"].Hair = newgirl["Mystique"].Sleepwear[8] if newgirl["Mystique"].Sleepwear[8] else newgirl["Mystique"].Hair 
                    $ newgirl["Mystique"].Hose = newgirl["Mystique"].Sleepwear[9] #0  
                    
                    $ newgirl["Mystique"].Hair = "long"
                    $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[4]
                    
        elif M_OutfitTemp == "gym":
                    if not newgirl["Mystique"].Legs and newgirl["Mystique"].Gym[2]:            
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Over and newgirl["Mystique"].Gym[3]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Chest and newgirl["Mystique"].Gym[5]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Panties and newgirl["Mystique"].Gym[6] and "pantyless" not in newgirl["Mystique"].DailyActions:        
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Hose and newgirl["Mystique"].Gym[9]:          
                            $ Undressed = 1
                        
                    $ newgirl["Mystique"].Arms = newgirl["Mystique"].Gym[1]
                    $ newgirl["Mystique"].Legs = newgirl["Mystique"].Gym[2]
                    $ newgirl["Mystique"].Over = newgirl["Mystique"].Gym[3] 
                    $ newgirl["Mystique"].Neck = newgirl["Mystique"].Gym[4]
                    $ newgirl["Mystique"].Chest = newgirl["Mystique"].Gym[5]
                    $ newgirl["Mystique"].Panties = newgirl["Mystique"].Gym[6]   
                    $ newgirl["Mystique"].Hair = newgirl["Mystique"].Gym[8] if newgirl["Mystique"].Gym[8] else newgirl["Mystique"].Hair 
                    $ newgirl["Mystique"].Hose = newgirl["Mystique"].Gym[9]     
                    $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[7]   
                
        if newgirl["Mystique"].Panties and "pantyless" in newgirl["Mystique"].DailyActions:       
                    # This checks the pantyless state from flirting 
                    if newgirl["Mystique"].Legs == "tights" or HoseNum("Mystique") >= 10:
                        $ newgirl["Mystique"].Shame -= 5    
                    elif newgirl["Mystique"].Legs:
                        $ newgirl["Mystique"].Shame -= 10  
                    elif newgirl["Mystique"].Panties == "green panties":
                        $ newgirl["Mystique"].Shame -= 20  
                    elif newgirl["Mystique"].Panties == "lace panties":
                        $ newgirl["Mystique"].Shame -= 25             
                    else:
                        $ newgirl["Mystique"].Shame -= 23  
                    
                    $ newgirl["Mystique"].Panties = 0        
                    $ newgirl["Mystique"].Shame = 0 if newgirl["Mystique"].Shame < 0 else newgirl["Mystique"].Shame
                    
        call Mod_Update_Mystique_Image(1)
        if not Changed and M_OutfitTemp == newgirl["Mystique"].Outfit and newgirl["Mystique"].Loc == bg_current:
                #If she was partially dressed then it says she gets dressed
                if Undressed == 2:
                        "She throws on a towel."
                elif Undressed:
                        "She throws her clothes back on."  
        # call Mystique_Tits_Up
        
        $ newgirl["Mystique"].Outfit = M_OutfitTemp


        return

label Mod_Set_The_Scene(Chr = 1, Entry = 0, Dress = 1, TrigReset = 1, Quiet=0):
        # If Chr, then display the characters in the room
        # If Entry, then show the "entry" version of a room, such as a closed door, does not display characters
        # If Dress, then check whether the character is underdressed when displaying her
        # Trigreset resets triggers
        # if Quiet, no fade to black
        if renpy.showing("Gwen_Sprite") and bg_current != "bg Brotherhood":
            hide Gwen_Sprite
        if not Quiet:
            show blackscreen onlayer black 
        
        if Entry:
            $ Chr = 0
            call AllHide 
            
        call Mod_Display_Background(Entry) 
        
        if Current_Time == 'Night':
                show NightMask onlayer nightmask
        else:          
                hide NightMask onlayer nightmask  
        
        if Chr:
                # call Present_Check  #culls out Party to 2, 
                $ Party = []
                #sets location to bg_current, removes extra girls, sets Focus to a girl in the room   
                
                # if Ch_Focus == "Kitty" and K_Loc == bg_current: 
                #         $ E_SpriteLoc = StageRight   
                #         $ R_SpriteLoc = StageRight
                #         $ L_SpriteLoc = StageRight
                #         $ K_SpriteLoc = StageCenter
                #         $ RogueLayer = 75
                #         $ EmmaLayer = 75
                #         $ LauraLayer = 75
                #         $ KittyLayer = 100
                #         call Display_Emma(Dress,TrigReset)
                #         call Display_Rogue(Dress,TrigReset)
                #         call Display_Laura(Dress,TrigReset)
                #         call Display_Kitty(Dress,TrigReset)
                        
                # elif Ch_Focus == "Emma" and E_Loc == bg_current:  
                #         $ K_SpriteLoc = StageRight  
                #         $ R_SpriteLoc = StageRight
                #         $ L_SpriteLoc = StageRight
                #         $ E_SpriteLoc = StageCenter
                #         $ KittyLayer = 75
                #         $ RogueLayer = 75
                #         $ LauraLayer = 75
                #         $ EmmaLayer = 100
                #         call Display_Rogue(Dress,TrigReset)
                #         call Display_Kitty(Dress,TrigReset)
                #         call Display_Laura(Dress,TrigReset)
                #         call Display_Emma(Dress,TrigReset)
                        
                # elif Ch_Focus == "Laura" and L_Loc == bg_current:  
                #         $ K_SpriteLoc = StageRight  
                #         $ R_SpriteLoc = StageRight
                #         $ E_SpriteLoc = StageRight
                #         $ L_SpriteLoc = StageCenter
                #         $ KittyLayer = 75
                #         $ RogueLayer = 75
                #         $ EmmaLayer = 75
                #         $ LauraLayer = 100
                #         call Display_Rogue(Dress,TrigReset)
                #         call Display_Kitty(Dress,TrigReset)
                #         call Display_Emma(Dress,TrigReset)
                #         call Display_Laura(Dress,TrigReset)
                
                # else: #if Ch_Focus == "Rogue" and R_Loc == bg_current:   
                #         $ K_SpriteLoc = StageRight
                #         $ E_SpriteLoc = StageRight
                #         $ L_SpriteLoc = StageRight
                #         $ R_SpriteLoc = StageCenter
                #         $ KittyLayer = 75
                #         $ EmmaLayer = 75
                #         $ LauraLayer = 75
                #         $ RogueLayer = 100
                #         call Display_Emma(Dress,TrigReset)
                #         call Display_Kitty(Dress,TrigReset)
                #         call Display_Laura(Dress,TrigReset)
                #         call Display_Rogue(Dress,TrigReset)

                call Display_Mystique(Dress)

                if bg_current == "bg study" and Current_Time != "Night":   
                        show Professor at SpriteLoc(StageLeft) zorder 25 
                else:
                        hide Professor
                
        else:            
            call AllHide(1) #removes all girls that aren't there.  
        show Chibi_UI
        hide Cellphone
        
        if TrigReset and Dress:            
                call Get_Dressed
            
        hide blackscreen onlayer black
        return

label Brotherhood_Entry:
    hide screen R_Status_screen
    show screen Mod_Status_screen
    # $ Ch_Focus = "Mystique"
    $ bg_current = "bg Brotherhood"
    call Mod_Daily_Math
    call Mod_Set_The_Scene(Entry = 1)
    call Taboo_Level
    # $ D20 = renpy.random.randint(1, 20)
    
    $ bg_current = "bg Brotherhood"         
    call Mod_EventCalls
    if bg_current != "bg Brotherhood":
        jump Misplaced
            
label Brotherhood_Hall:
    $ bg_current = "bg Brotherhood"
    call Mod_Set_The_Scene
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")
    call Taboo_Level
    call QuickEvents
    call Checkout(1)
    if Round <= 10: 
                call Mod_Round10
                call Girls_Location
                call Mod_EventCalls
    
    call GirlsAngry
    call Mod_Set_The_Scene
    
# Brotherhood's Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if "Gwentro" in L_History and not GwenStage: #Gwen welcomes player
                $ GwenStage = 1
                call GwenBrotherhood
    if GwenStage:
        call GwenFace("smile", 0)
        show Gwen_Sprite at SpriteLoc(650) zorder 25
    $ Line = "You are in the Brotherhood. What would you like to do?"
    menu:
        "[Line]"
        
        "Chat with Gwen" if GwenStage:
                    call Gwen_Chat
                    pass
        
        "Wait." if Current_Time != "Night":
                    call Mod_Round10
                    call Girls_Location
                    call Mod_EventCalls
                            
        # "Return to Your Room" if TravelMode:            
        #             call Leave_Brotherhood_Area
        #             jump Player_Room_Entry
        # # "Go to the Showers" if TravelMode:            
        # #             jump Shower_Room_Entry
        "Go to Mystique's Room":
                jump Mystique_Room_Entry
        "Leave [[Return to Xavier Institute]":
                    if TravelMode:
                        call Leave_Brotherhood_Area
                        jump Campus_Entry
                    else:
                        call Leave_Brotherhood_Area
                        call Worldmap
    
    jump Brotherhood_Hall

label Mystique_Room_Entry:
    # call Shift_Focus("Mystique")
    hide screen R_Status_screen
    show screen Mod_Status_screen
    $ Ch_Focus = "Mystique"
    $ bg_current = "bg Mystique"           
    $ newgirl["Mystique"].LooksLike = "Mystique"
    call Mod_Set_The_Scene(Entry = 1)
    call Taboo_Level
    $ D20 = renpy.random.randint(1, 20)
    
    $ bg_current = "bg Mystique"         
    call Mod_EventCalls
    if bg_current != "bg Mystique":
        jump Misplaced
            
label Mystique_Room:
    $ newgirl["Mystique"].LooksLike = "Mystique"
    $ bg_current = "bg Mystique"
    call Mod_Set_The_Scene(Quiet = 1)
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")
    call Taboo_Level
    call QuickEvents
    call Checkout(1)
    if Round <= 10: 
                call Mod_Round10
                call Girls_Location
                call Mod_EventCalls
    
    call GirlsAngry
    call Mod_Set_The_Scene(Quiet = 1)
    
# Mystique's Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if newgirl["Mystique"].Loc == bg_current:
        $ Line = "You are in " + newgirl["Mystique"].name + "'s room. What would you like to do?"
    else:
        $ Line = "You are in " + newgirl["Mystique"].name + "'s room, but she isn't here. What would you like to do?"
    menu:
        "[Line]"
        
        "Chat":
                    call Mod_Chat
        
        # "Would you like to study?" if newgirl["Mystique"].Loc == bg_current:                
        #             call Mystique_Study
            
        "Sleep." if Current_Time == "Night" and newgirl["Mystique"].Loc == bg_current:
                    call Mod_Round10
                    call Girls_Location
                    call Mod_EventCalls
                    
        "Wait." if Current_Time != "Night":
                    call Mod_Round10
                    call Girls_Location
                    call Mod_EventCalls
                            
        # "Return to Your Room" if TravelMode:            
        #             call Leave_Brotherhood_Area
        #             jump Player_Room_Entry
        # # "Go to the Showers" if TravelMode:            
        # #             jump Shower_Room_Entry
        "Back to Brotherhood":
                    jump Brotherhood_Hall
        "Leave [[Return to Xavier Institute]":
                    if TravelMode:
                        call Leave_Brotherhood_Area
                        jump Campus_Entry
                    else:
                        call Leave_Brotherhood_Area
                        call Worldmap
    if "angry" in newgirl["Mystique"].RecentActions:
            call MystiqueFace("angry")
            ch_m "Go. Now."
            "Mystique pushes you back into the hall and slams the door. You head back to your room."
            $ Line = 0
            $ Trigger = 0
            call Leave_Brotherhood_Area
            jump Player_Room
    jump Mystique_Room


label GwenBrotherhood:
    
        # call GwenFace("angry")
        # $ GwenStage = 1
        call GwenFace("surprised")
        show Gwen_Sprite at SpriteLoc(650) zorder 25 with easeinright #call Display_Gwen
        ch_g "Hey, It's you again."
        call GwenFace("smile",1)
        ch_g "Remember me? I was there when Laura was giving you a blowjob."
        # show Gwen_Sprite at SpriteLoc(1500) zorder 25:
        #         xzoom -1 
        # pause .1
        call GwenFace("confused",2,Eyes="side")
        ch_g "You're probably wondering what I'm doing here right?" 
        call GwenFace("smile",1)
        ch_g "Looks like one of the devs of this mod has a thing for me or something." 
        call GwenFace("sad",1)
        ch_g "But I still can't take these damm clothes off." 
        ch_g "I can't even take this mask off. Boooooring."
        ch_g "No art yet by the looks of it." 
        call GwenFace("surprised")
        ch_g "Hey, maybe you can help out huh?"
        call GwenFace("smile",1)
        ch_g "You can draw it and send it to the mod devs."
        ch_g "I'll be waiting here. Make me proud [Playername]"
        call GwenFace("surprised",0)
        ch_g "Oh, if you're looking for Mystique, she's upstairs, last room to the left"
        call GwenFace("smile")
        ch_g "Just kidding, select \"Go to Mystique\'s Room\" on the menu thingy"
        return
label Gwen_Chat:
        if GwenStage < 5:
            $ GwenStage += 1
            $ d20roll = renpy.random.randint(1, 5)
            
            if d20roll == 1:                             
                call GwenFace("confused")
                ch_g "Did you know this game was made by a guy named Oni? You should check his patreon and support the guy."
            elif d20roll == 2:              
                call GwenFace("smile")
                ch_g "Hey, do you think Spider-Gwen'll ever show up around these parts?"
                ch_g "We could have a very crazy threesome right?"    
            elif d20roll == 3:              
                call GwenFace("confused")
                ch_g "How does Professor X telepathically tells you to get to his study if powers don't work on you? Weird right?"
            elif d20roll == 4:              
                call GwenFace("closed")
                ch_g "Hey, who do you want to be the next girl added to this game?"
                call GwenFace("smile")
                ch_g "I'm cheering for either Jean or Storm."
            elif d20roll == 5:              
                call GwenFace("smile")
                ch_g "Did you know Laura used to be a prostitute? I'd gladly pay for her services."
        else:
            $ GwenStage = 1
            call GwenFace("angry")
            ch_g "Did I ever tell you what the definition of insanity is?"
            ch_g "Insanity is doing the exact... same fucking thing... over and over again expecting... shit to change..."
            ch_g "That. Is. Crazy."

        return

label Leave_Brotherhood_Area:
    hide Mystique_Sprite
    hide Gwen_Sprite
    hide screen Mod_Status_screen
    show screen R_Status_screen
    return